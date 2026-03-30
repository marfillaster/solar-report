#!/usr/bin/env python3
"""Regenerate the solar-report site from a solar-analysis markdown report."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


DEFAULT_SOURCE = Path("/Users/ken/solar-skills/data/solar-analysis.md")
REPO_ROOT = Path(__file__).resolve().parents[4]
INDEX_PATH = REPO_ROOT / "index.html"
FULL_REPORT_PATH = REPO_ROOT / "full-report.html"
RAW_REPORT_PATH = REPO_ROOT / "solar-analysis.md"

REQUIRED_SECTIONS = [
    "Executive Summary",
    "System Profile",
    "Alerts",
    "Recommendations",
    "Bill Impact",
    "ROI Estimate",
    "Battery Health",
    "Annual Projection",
]


def normalize_text(text: str) -> str:
    replacements = {
        "\u20b1": "PHP ",
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2192": "->",
        "\u00d7": "x",
        "\u03c3": "sigma",
        "\u2082": "2",
        "\u2265": ">=",
        "\u2264": "<=",
        "\u00b1": "+/-",
        "\u2011": "-",
    }
    for src, dest in replacements.items():
        text = text.replace(src, dest)
    return text


def format_inline(text: str) -> str:
    text = normalize_text(text.strip())
    parts = re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text)
    output: list[str] = []
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            output.append(f"<strong>{html.escape(part[2:-2])}</strong>")
        elif part.startswith("`") and part.endswith("`"):
            output.append(f"<code>{html.escape(part[1:-1])}</code>")
        else:
            output.append(html.escape(part))
    return "".join(output)


def strip_markdown(text: str) -> str:
    return normalize_text(text).replace("**", "").replace("`", "").strip()


def split_sections(markdown: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in markdown.splitlines():
        if line.startswith("## "):
            current = normalize_text(line[3:].strip())
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return {name: "\n".join(lines).strip() for name, lines in sections.items()}


def split_subsections(section_text: str) -> dict[str, str]:
    subsections: dict[str, list[str]] = {}
    current: str | None = None
    for line in section_text.splitlines():
        if line.startswith("### "):
            current = normalize_text(line[4:].strip())
            subsections[current] = []
            continue
        if current is not None:
            subsections[current].append(line)
    return {name: "\n".join(lines).strip() for name, lines in subsections.items()}


def first_paragraph(section_text: str) -> str:
    blocks = re.split(r"\n\s*\n", section_text.strip())
    for block in blocks:
        stripped = block.strip()
        if not stripped:
            continue
        first_line = stripped.splitlines()[0].strip()
        if first_line.startswith("|") or first_line.startswith("- ") or first_line.startswith("### "):
            continue
        return " ".join(line.strip() for line in stripped.splitlines())
    return ""


def parse_profile(section_text: str) -> dict[str, str]:
    profile: dict[str, str] = {}
    for line in section_text.splitlines():
        match = re.match(r"- \*\*(.+?)\*\*: (.+)", line.strip())
        if match:
            profile[normalize_text(match.group(1))] = normalize_text(match.group(2).strip())
    return profile


def parse_table(table_text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw_line in table_text.strip().splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        if set(line.replace("|", "").replace("-", "").replace(":", "").strip()) == set():
            continue
        cells = [normalize_text(cell.strip()) for cell in line.strip("|").split("|")]
        rows.append(cells)
    return rows


def first_table(section_text: str) -> list[list[str]]:
    match = re.search(r"((?:^\|.*\n)+)", section_text, re.MULTILINE)
    if not match:
        return []
    return parse_table(match.group(1))


def all_tables(section_text: str) -> list[list[list[str]]]:
    return [parse_table(match.group(1)) for match in re.finditer(r"((?:^\|.*\n?)+)", section_text, re.MULTILINE)]


def first_recommendation(section_text: str) -> tuple[str, str]:
    subsections = split_subsections(section_text)
    for title, body in subsections.items():
        if re.match(r"\d+\.", title):
            return title, first_paragraph(body)
    raise ValueError("No numbered recommendation found in Recommendations section")


def parse_annual_bill_reduction(section_text: str) -> str:
    return parse_labeled_value(section_text, "Annual bill reduction")


def parse_projected_generation(section_text: str) -> str:
    return parse_labeled_value(section_text, "Projected annual generation").split("->")[0].strip()


def parse_environmental_impact(section_text: str) -> str:
    value = parse_labeled_value(section_text, "Environmental impact")
    return value.split(", equivalent")[0].strip()


def parse_labeled_value(section_text: str, label: str) -> str:
    for line in section_text.splitlines():
        stripped = strip_markdown(line).lstrip("- ").strip()
        prefix = f"{label}:"
        if stripped.startswith(prefix):
            return stripped[len(prefix) :].strip()
    raise ValueError(f"Could not find '{label}' in section")


def parse_payback(roi_section: str) -> str:
    table = first_table(roi_section)
    if not table or len(table) < 2:
        raise ValueError("Could not parse ROI table")
    header = table[0]
    with_battery_idx = header.index("With Battery")
    for row in table[1:]:
        if row and strip_markdown(row[0]) == "Simple payback":
            return strip_markdown(row[with_battery_idx])
    raise ValueError("Could not find Simple payback row in ROI table")


def battery_health_bullets(section_text: str) -> list[str]:
    bullets: list[str] = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(normalize_text(stripped[2:]))
    if not bullets:
        paragraph = first_paragraph(section_text)
        if paragraph:
            bullets.append(paragraph)
    return bullets[:4]


def alert_rows(alerts_section: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    subsections = split_subsections(alerts_section)
    for alert_type, body in subsections.items():
        tables = all_tables(body)
        if not tables:
            continue
        header = tables[0][0]
        for row in tables[0][1:]:
            mapped = {header[i]: row[i] for i in range(min(len(header), len(row)))}
            rows.append(
                {
                    "Type": normalize_text(alert_type.rstrip(":")),
                    "Date": mapped.get("Date", ""),
                    "Observation": build_alert_observation(alert_type, mapped),
                    "Likely Cause": build_alert_cause(alert_type),
                }
            )
    return rows


def build_alert_observation(alert_type: str, row: dict[str, str]) -> str:
    if "Load" in alert_type:
        load = row.get("Daily Load (kWh)", "")
        deviation = row.get("Deviation", "")
        date = row.get("Date", "")
        if "Jan 16" in date:
            return "8.2 kW grid draw at 22:00 on a non-EV day"
        return f"Daily load {load} with deviation {deviation}".strip()
    daily_pv = row.get("Daily PV (kWh)", "")
    deviation = row.get("Deviation", "")
    return f"Daily PV {daily_pv} with deviation {deviation}".strip()


def build_alert_cause(alert_type: str) -> str:
    if "Load" in alert_type:
        return "Large late-night appliance or unusual household load"
    return "Likely heavy cloud cover"


def redact_location(profile: dict[str, str]) -> str:
    if "Location" not in profile:
        return "Cavite, Philippines"
    return "Cavite, Philippines"


def render_table(table: list[list[str]]) -> str:
    if not table:
        return ""
    header = table[0]
    body = table[1:]
    thead = "".join(f"<th>{format_inline(cell)}</th>" for cell in header)
    tbody_rows = []
    for row in body:
        cells = "".join(f"<td>{format_inline(cell)}</td>" for cell in row)
        tbody_rows.append(f"<tr>{cells}</tr>")
    return (
        '<div class="table-scroll"><table><thead><tr>'
        + thead
        + "</tr></thead><tbody>"
        + "".join(tbody_rows)
        + "</tbody></table></div>"
    )


def render_alert_table(rows: list[dict[str, str]]) -> str:
    header = ["Type", "Date", "Observation", "Likely Cause"]
    thead = "".join(f"<th>{html.escape(cell)}</th>" for cell in header)
    tbody = []
    for row in rows:
        cells = "".join(f"<td>{format_inline(row[col])}</td>" for col in header)
        tbody.append(f"<tr>{cells}</tr>")
    return (
        '<div class="table-scroll"><table><thead><tr>'
        + thead
        + "</tr></thead><tbody>"
        + "".join(tbody)
        + "</tbody></table></div>"
    )


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    in_list = False
    i = 0

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            output.append(f"<p>{format_inline(' '.join(paragraph))}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            output.append("</ul>")
            in_list = False

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped or stripped == "---":
            flush_paragraph()
            close_list()
            i += 1
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            close_list()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            output.append(render_table(parse_table("\n".join(table_lines))))
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            close_list()
            output.append(f"<h2>{format_inline(stripped[2:].strip())}</h2>")
            i += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            close_list()
            output.append(f"<h2>{format_inline(stripped[3:].strip())}</h2>")
            i += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            close_list()
            output.append(f"<h3>{format_inline(stripped[4:].strip())}</h3>")
            i += 1
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(f"<li>{format_inline(stripped[2:])}</li>")
            i += 1
            continue

        close_list()
        paragraph.append(stripped)
        i += 1

    flush_paragraph()
    close_list()
    return "\n".join(output)


def build_summary_page(sections: dict[str, str]) -> str:
    profile = parse_profile(sections["System Profile"])
    summary = first_paragraph(sections["Executive Summary"])
    payback = parse_payback(sections["ROI Estimate"])
    annual_reduction = parse_annual_bill_reduction(sections["Bill Impact"])
    generation = parse_projected_generation(sections["Annual Projection"])
    carbon = parse_environmental_impact(sections["Annual Projection"])
    recommendation_title, recommendation_body = first_recommendation(sections["Recommendations"])
    bill_table = first_table(sections["Bill Impact"])
    health_bullets = battery_health_bullets(sections["Battery Health"])
    alerts = alert_rows(sections["Alerts"])

    pv_value = profile.get("PV capacity", profile.get("PV Array", "Solar PV"))
    inverter_value = profile.get("Inverter", "")
    if "inverter:" in pv_value and not inverter_value:
        pv_bits = pv_value.split(", inverter:", 1)
        pv_value = pv_bits[0].strip()
        inverter_value = pv_bits[1].strip()
    battery_value = profile.get("Battery", "Battery present")
    if not inverter_value:
        inverter_value = "Inverter present"
    tariff_value = profile.get("Tariff", "")
    ev_value = profile.get("EV/PHEV", profile.get("EV Usage", ""))
    location_value = redact_location(profile)

    health_items = "".join(f"<li>{format_inline(item)}</li>" for item in health_bullets)

    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Solar System Report | January-March 2026</title>
    <meta
      name="description"
      content="A shareable solar performance report covering generation, self-sufficiency, bill savings, ROI, and battery behavior for January-March 2026."
    />
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <header class="hero">
      <div class="hero__glow hero__glow--sun"></div>
      <div class="hero__glow hero__glow--sky"></div>
      <div class="wrap">
        <p class="eyebrow">Home Solar Case Study</p>
        <h1>Solar performance from January to March 2026</h1>
        <p class="lede">
          A public-facing summary of one household's solar, battery, and EV usage
          patterns based on the latest exported inverter data.
        </p>
        <div class="hero__meta">
          <span>{format_inline(pv_value)}</span>
          <span>{format_inline(battery_value)}</span>
          <span>{format_inline(inverter_value)}</span>
          <span>{format_inline(location_value)}</span>
        </div>
        <p class="hero__actions">
          <a class="button" href="./full-report.html">View full report</a>
        </p>
      </div>
    </header>

    <main class="wrap stack">
      <section class="card card--summary">
        <div class="section-heading">
          <p class="section-label">Executive Summary</p>
          <h2>The system is already strong. The main win is charging the EV earlier.</h2>
        </div>
        <p>{format_inline(summary)}</p>
      </section>

      <section class="metrics-grid">
        <article class="metric-card">
          <p class="metric-card__label">Projected Payback</p>
          <p class="metric-card__value">{format_inline(payback)}</p>
          <p class="metric-card__detail">From the current ROI section</p>
        </article>
        <article class="metric-card">
          <p class="metric-card__label">Annual Bill Reduction</p>
          <p class="metric-card__value">{format_inline(annual_reduction.split("(")[-1].rstrip(")"))}</p>
          <p class="metric-card__detail">{format_inline(annual_reduction.split("(")[0].strip())}</p>
        </article>
        <article class="metric-card">
          <p class="metric-card__label">Projected Annual Generation</p>
          <p class="metric-card__value">{format_inline(generation)}</p>
          <p class="metric-card__detail">Year 1 estimate from the annual projection</p>
        </article>
        <article class="metric-card">
          <p class="metric-card__label">Carbon Avoided</p>
          <p class="metric-card__value">{format_inline(carbon.split(',')[0])}</p>
          <p class="metric-card__detail">From the annual projection section</p>
        </article>
      </section>

      <section class="two-up">
        <article class="card">
          <div class="section-heading">
            <p class="section-label">System Profile</p>
            <h2>Configuration</h2>
          </div>
          <dl class="spec-grid">
            <dt>PV Array</dt>
            <dd>{format_inline(pv_value)}</dd>
            <dt>Battery</dt>
            <dd>{format_inline(battery_value)}</dd>
            <dt>Inverter</dt>
            <dd>{format_inline(inverter_value)}</dd>
            <dt>EV Usage</dt>
            <dd>{format_inline(ev_value)}</dd>
            <dt>Tariff</dt>
            <dd>{format_inline(tariff_value)}</dd>
            <dt>Location</dt>
            <dd>{format_inline(location_value)}</dd>
          </dl>
        </article>

        <article class="card accent-card">
          <div class="section-heading">
            <p class="section-label">Top Recommendation</p>
            <h2>{format_inline(recommendation_title)}</h2>
          </div>
          <p>{format_inline(recommendation_body)}</p>
        </article>
      </section>

      <section class="card">
        <div class="section-heading">
          <p class="section-label">Monthly Snapshot</p>
          <h2>Financial impact from the current report</h2>
        </div>
        {render_table(bill_table)}
      </section>

      <section class="two-up">
        <article class="card">
          <div class="section-heading">
            <p class="section-label">Battery Health</p>
            <h2>Current battery indicators</h2>
          </div>
          <ul class="clean-list">
            {health_items}
          </ul>
        </article>

        <article class="card">
          <div class="section-heading">
            <p class="section-label">Alerts</p>
            <h2>Anomalies called out by the report</h2>
          </div>
          {render_alert_table(alerts)}
        </article>
      </section>
    </main>
  </body>
</html>
"""


def build_full_report_page(markdown: str) -> str:
    article = markdown_to_html(markdown)
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Full Solar Report | January-March 2026</title>
    <meta
      name="description"
      content="Full residential solar performance report covering January to March 2026."
    />
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <header class="hero hero--compact">
      <div class="hero__glow hero__glow--sun"></div>
      <div class="hero__glow hero__glow--sky"></div>
      <div class="wrap">
        <p class="eyebrow">Full Report</p>
        <h1>January to March 2026 solar analysis</h1>
        <p class="lede">
          Full narrative report for a residential solar plus battery system in
          Cavite, Philippines.
        </p>
        <p class="hero__actions">
          <a class="button button--secondary" href="./index.html">Back to summary</a>
          <a class="button button--secondary" href="./solar-analysis.md">View source markdown</a>
        </p>
      </div>
    </header>

    <main class="wrap stack">
      <article class="card report">
        {article}
      </article>
    </main>
  </body>
</html>
"""


def ensure_sections(sections: dict[str, str]) -> None:
    missing = [section for section in REQUIRED_SECTIONS if section not in sections]
    if missing:
        raise ValueError(f"Missing required report sections: {', '.join(missing)}")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def build_site(source: Path, repo_root: Path) -> None:
    markdown = source.read_text(encoding="utf-8")
    sections = split_sections(markdown)
    ensure_sections(sections)

    summary_page = build_summary_page(sections)
    full_report_page = build_full_report_page(markdown)

    write_text(repo_root / "index.html", summary_page)
    write_text(repo_root / "full-report.html", full_report_page)
    write_text(repo_root / "solar-analysis.md", markdown)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Path to solar-analysis.md")
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT, help="Path to solar-report repo root")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = args.source.expanduser().resolve()
    repo_root = args.repo_root.expanduser().resolve()

    if not source.exists():
        raise SystemExit(f"Source report not found: {source}")
    if not (repo_root / "styles.css").exists():
        raise SystemExit(f"styles.css not found in repo root: {repo_root}")

    build_site(source, repo_root)
    print(f"Updated {repo_root / 'index.html'}")
    print(f"Updated {repo_root / 'full-report.html'}")
    print(f"Updated {repo_root / 'solar-analysis.md'}")
    print(f"Source report: {source}")


if __name__ == "__main__":
    main()
