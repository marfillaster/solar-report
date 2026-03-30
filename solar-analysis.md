# Solar System Recommendations

Based on analysis of solar data from January–March 2026 (89 days, 2,133 hourly rows).

---

## Executive Summary

Your 6.5 kWp system is performing well and on track for a **~3.8-year payback** on ₱400,000 invested. Self-sufficiency has improved consistently from 60% in January to 77% in March as the dry season strengthens — a 17-point gain in just two months. The most impactful single optimization is **shifting EV charging to 10:00–13:00**, which could cut EV-day grid import by ~3–5 kWh per session and save ₱3,200–5,300 annually. An unusual 8.2 kW grid draw on the night of Jan 16 warrants investigation but likely reflects a benign large-appliance event. Two generation dips (Feb 8 and Mar 17, both −44%) appear weather-related with no equipment fault signal. The system avoids ~4.5 tonnes of CO₂ annually — equivalent to planting ~206 trees.

---

## System Profile

- **PV capacity**: 6.5 kWp, inverter: 8 kW AC (DC/AC ratio: 0.81 — inverter is oversized for this array)
- **Battery**: 14.3 kWh nominal, ~14.3 kWh usable (SOC range 21%–89% typical)
- **EV/PHEV**: Present — detected on 19 of 89 days (~21% of days)
- **Tariff**: Flat rate ₱14/kWh import, ₱7/kWh feed-in (net metering at 50%)
- **Location**: General Trias, Cavite, Philippines

---

## Alerts

### Load Anomalies

Four non-EV days exceeded the expected load range by more than 2 standard deviations:

| Date | Daily Load (kWh) | Expected | Deviation |
|---|---|---|---|
| Jan 7 | 36.0 | ~24.2 ± 5.3 kWh | +2.2σ |
| Jan 16 | 35.1 | ~24.2 ± 5.3 kWh | +2.1σ |
| Mar 1 | 35.2 | ~24.2 ± 5.3 kWh | +2.1σ |
| Mar 13 | 36.1 | ~24.2 ± 5.3 kWh | +2.2σ |

Jan 7 falls within the extended Philippine holiday period, which likely explains guests or heavier appliance use. Jan 16 is the most notable: it also produced the highest grid draw on record — **8.2 kW at 22:00** on a night with no detected EV charging. A draw of that size at that hour points to a large appliance activating unexpectedly (water heater with a faulty thermostat, compressor, or multiple air conditioners running simultaneously). If the household doesn't routinely run heavy loads after 22:00, it's worth monitoring that circuit.

### PV Generation

Two days showed generation ~44% below their rolling baseline — likely heavy cloud cover:

| Date | Daily PV (kWh) | Expected | Deviation |
|---|---|---|---|
| Feb 8 | 10.9 | ~19.4 kWh | −44% |
| Mar 17 | 15.8 | ~28.3 kWh | −44% |

No action required unless either date was a clear-weather day in your recollection, in which case retrieve inverter fault logs. Mar 17 also shows a battery efficiency reading of 79% (vs. the 94–97% norm) — this is almost certainly a measurement artifact from the partial-generation day rather than a battery issue.

---

## Recommendations

### 1. Shift EV charging to 10:00–13:00 (highest impact)

On the 19 detected EV charging days, grid import averaged 17.5 kWh — nearly triple the 5.9 kWh on non-EV days. The bulk of that deficit occurs in the afternoon: at 15:00 on EV days, average load surges to 4,695W while PV has already begun its decline to ~1,679W; at 16:00 it's a 3,808W load against only 834W of PV, forcing 1,847W of grid draw; by 18:00 the grid is pulling 2,293W. The battery is depleted to just 27% SOC by evening on EV days, compared to 67% on non-EV days — there is nothing left to cover the overnight household load, which then comes entirely from the grid.

The system handles the morning portion of EV charging well. Between 09:00 and 12:00, PV is generating 2,300–4,200W and the battery is being charged simultaneously. Front-loading charging into this window — targeting charge completion by 13:00–14:00 rather than allowing it to run through the afternoon — shifts 3–5 kWh of grid import to solar per session. At ₱14 avoided import versus ₱7 that would otherwise be earned from export, that's a net gain of ₱7/kWh on the shifted energy, or ₱21–35 per session and ₱1,600–2,700/year from the rate differential alone. Adding the absolute avoided import savings, the total annual impact is ₱3,200–5,300.

If your EVSE supports scheduled charging, set a departure time or end-of-charge time of 13:00–14:00. If it uses a simple timer, set charging to start no later than 09:00 and stop by 13:30.

### 2. Identify and reduce the late-night base load

On non-EV nights, average load runs from 776W at midnight down to 612W at 04:00 before ticking back up as the household wakes. This overnight draw — approximately 14 kWh from midnight to 07:00 — is met by battery discharge and grid import, and drains the battery from ~67% SOC at dusk to ~24% by morning. A sustained overnight consumption of 600–800W suggests the household has significant standby or continuous loads: always-on air conditioning, a spare refrigerator, continuous water pump, or entertainment systems left in standby.

A 100W reduction in overnight base load saves ~0.7 kWh/day, or ₱3,600/year, and leaves the battery better-charged for the next morning's solar ramp-up. Use a smart plug with energy monitoring on candidate appliances for a week to identify the culprits. The Jan 16 event (8.2 kW at 22:00) is the most useful starting point — checking what triggered that spike may reveal an appliance that cycles intermittently at high power overnight.

### 3. Confirm battery SOC floor and backup reserve setting

The battery currently reaches an average morning minimum of 21% SOC. LFP chemistry handles this depth well, but if your inverter has a configurable backup reserve (for grid-outage scenarios), verify it is set to at least 20%. At 21% average morning SOC, the system is running very close to the floor. If the floor is set lower than 20%, the battery may be providing slightly less protection during outages than expected. This is a settings check, not a hardware issue — check the inverter's battery management settings and confirm the reserve aligns with your outage backup needs.

---

### Not Recommended

- **Grid-charging the battery off-peak**: The flat ₱14/kWh tariff means there is no off-peak rate to arbitrage. Grid-charged energy costs ₱14.40–14.90/kWh delivered (after round-trip losses), more expensive than simply importing when needed. Not viable without a TOU tariff with a significant off-peak discount.
- **Adding more panels**: No additional roof space is available, and the existing array is already well-matched to base-load consumption (PV/load ratio 0.91). More panels would only increase export earning ₱7/kWh — a lower return than the existing system's direct self-consumption savings.

---

## Bill Impact

### Monthly Electricity Cost Comparison

| Month | Without Solar | With Solar | Feed-in Credit | Net Savings |
|---|---|---|---|---|
| Jan 2026 | ₱11,628 | ₱4,654 | ₱76 | ₱7,051 |
| Feb 2026 | ₱10,763 | ₱2,912 | ₱624 | ₱8,474 |
| Mar 2026 | ₱12,341 | ₱2,899 | ₱874 | ₱10,317 |

- Estimated annual bill without solar: **₱142,440**
- Estimated annual bill with solar: **₱42,918** (including ~₱6,455 feed-in credits)
- **Annual bill reduction: ₱105,981 (74%)**

January's lower savings reflect weaker generation that month (16.7 kWh/day vs. 27.2 kWh/day in March). Feed-in credit was minimal in January because the battery was rarely full enough to export — the February and March improvements show the compounding effect of stronger sun filling the battery earlier, creating a longer daily export window.

---

## ROI Estimate

| Metric | With Battery | Without Battery |
|---|---|---|
| System cost | ₱400,000 | ₱300,000 |
| Annual savings (year 1) | ₱105,981 | ~₱81,240 |
| **Simple payback** | **~3.8 years** | **~3.7 years** |
| Remaining payback | ~3.5 years | ~3.4 years |
| 25-year lifetime savings | ₱2,496,483 | ~₱1,804,000 |

**Battery incremental ROI**: The ₱100,000 battery adds ~₱24,741/year by shifting energy that would otherwise be exported at ₱7/kWh into evening self-consumption worth ₱14/kWh. Battery-only payback is ~4.0 years — well within the battery's projected service life. At 234 cycles/year against a 6,000-cycle LFP rating, the battery is estimated to last ~25 years, meaning it will pay back its cost roughly six times over. The battery investment is justified.

Interestingly, the payback periods with and without battery are nearly identical (3.8 vs. 3.7 years) because the battery cost is almost exactly offset by its annual savings contribution. The difference in 25-year lifetime savings — ₱692,000 — represents the battery's compounding value over the system's life.

The projected annual savings (₱105,981) are based on 3 months of dry-season data. Wet-season months (June–October) will reduce generation by ~14%, bringing annualized savings somewhat lower. Re-running this analysis in July 2026 will provide a more calibrated figure.

---

## Key Metrics

| Metric | Non-EV Days | EV Days |
|---|---|---|
| Daily PV generation | ~22 kWh | ~24 kWh |
| Daily consumption | ~24.2 kWh | ~41.6 kWh |
| Daily grid import | ~5.9 kWh | ~17.5 kWh |
| Daily grid export | ~2.8 kWh | ~1.5 kWh |
| Evening SOC (18–20h) | ~67% | ~27% |

- **Self-consumption rate**: 96.3% (Jan) → 84.9% (Feb) → 82.6% (Mar) — declining as stronger sun fills the battery earlier in the day, creating an unavoidable export surplus
- **Self-sufficiency**: 60.0% (Jan) → 72.9% (Feb) → 76.5% (Mar) — improving consistently with the season
- Export is concentrated at 12:00–15:00, when the battery reaches ~87% SOC and PV still generates 1,400–3,600W of surplus
- On non-EV days, the battery drains from ~67% to ~24% SOC overnight (~43pp, ~6 kWh) — a clean, sustainable daily cycle
- On EV days, the battery depletes to ~27% SOC by evening, and the 14:00–19:00 charging surge draws 1,400–2,300W from the grid
- Non-EV base load of ~24.2 kWh/day closely matches daily PV output (~22 kWh) — the system is well-sized for the household's baseline needs

### Hourly Patterns

- **PV peak window**: 11:00–13:00, averaging 3,400–3,600W on non-EV days and up to 4,200W on EV days (brighter-sky sample bias)
- **Battery charge ramp**: Begins at 07:00, peaks around 10:00 at ~1,850W charge rate, tapers after 12:00 as SOC exceeds 80%
- **Export window**: 12:00–15:00 on non-EV days — battery is full, PV surplus spills to grid at an average of 1,038W at 13:00
- **Evening discharge**: Battery supplies 1,000–1,060W from 17:00–19:00, smoothly bridging the solar-to-grid transition
- **EV load spike**: Detected between 10:00 and 18:00 on EV days, peaking at 4,695W at 15:00 — a clear afternoon charging signature that competes with declining PV
- **Overnight grid import**: Averages 0.40–0.45 kWh/hour from midnight to 06:00 as battery drops below 40% SOC

### Weekday vs Weekend

Weekday and weekend self-sufficiency are nearly identical (75% vs. 77%), with daily loads of 24.1 and 24.3 kWh respectively. The pattern difference is in timing: weekends show ~440W higher load at 12:00–13:00 (occupants home during peak solar) — this is beneficial, as it substitutes direct solar consumption for what would otherwise be exported at ₱7/kWh. Weekday evenings at 20:00–22:00 run ~400W higher, requiring more grid import when no PV is available. If any weekday evening appliances (ironing, cooking, washing) can be shifted to 12:00–15:00 — feasible with timer-controlled appliances or a helper running chores during peak solar — they would convert ₱7/kWh export into ₱14/kWh avoided import.

### Peak Demand

- **Peak grid draw**: 8.2 kW on 2026-01-16 at 22:00 (non-EV day) — see Alerts
- Average daily peak grid draw: ~1.3 kW (non-EV), ~4.8 kW (EV days)
- **Peak PV output**: 5.4 kW on 2026-03-15 at 12:00 (84% of panel nameplate, 68% of inverter capacity)
- No demand charge tariff applies — these figures are informational

---

## System Size Assessment

No additional roof space is available for expansion.

### PV Array (6.5 kWp): Correctly sized for base load

- Peak output of 5,436W reached 84% of the 6,500W nameplate — normal for real-world conditions with temperature, cabling, and orientation losses
- **Inverter is oversized**: The 8 kW inverter was used to only 68% of its AC capacity at peak output. A 5.5–6 kW inverter would have been adequate for this array and more cost-effective. There is no operational impact — the inverter runs efficiently at partial load — but if it ever needs replacement, a smaller unit is the right choice
- No panel clipping detected (peak never exceeded 85% of nameplate). No inverter clipping detected
- Peak sun hours of 4.2 h/day in March is reasonable for Cavite in the pre-summer dry season; April and May will likely be the peak generation months
- Non-EV PV/load ratio of 0.91: the array generates slightly less than the base household load, with the gap covered by the battery cycling energy from daytime surplus to overnight demand — an efficient arrangement
- On EV days, average load jumps to 41.6 kWh against ~24 kWh of PV generation — the deficit is structural and cannot be solved by array sizing without exceeding available roof space

### Battery (14.3 kWh): Adequate for base load, stretched on EV days

- Non-EV cycle depth: ~60% (charging from ~24% to ~87% SOC), well within LFP comfort zone with headroom in both directions
- EV days push cycle depth to ~79%, with evening SOC depleted to 27% — the battery is working hard on charging days but not in a damaging way
- Round-trip efficiency: 96.7% (Jan) → 96.3% (Feb) → 94.5% (Mar) — all within LFP normal range (92–95% is typical; a new LFP cell often measures 95–97%)
- The ~2.3 kWh/day estimated avoidable import represents energy the battery couldn't fully offset due to the deep overnight drain — a second battery would reduce this, but the cost would take many years to recover given the marginal nature of the gain

### Verdict

The system is well-designed for the household's non-EV needs. Battery size is appropriate, and PV-to-load matching is good. The oversized inverter is a minor inefficiency that does not affect operations. On EV days, the constraint is timing rather than capacity — shifting charging earlier is the highest-leverage action available without any hardware change.

---

## Battery Health

- **Nominal capacity**: 14.3 kWh | **Estimated usable**: ~14.3 kWh (100% of nominal — consistent with a new LFP battery)
- **Round-trip efficiency**: 96.7% (Jan) → 96.3% (Feb) → 94.5% (Mar)
- **Daily equivalent full cycles**: ~0.64 (234/year)
- **Estimated cycle life remaining**: ~25 years at current usage (6,000-cycle LFP rating ÷ 234 cycles/year)

At 4 months of age, the battery is performing exactly as expected: full usable capacity, high round-trip efficiency, and healthy cycle depth. The 2.2pp efficiency decline from January to March is worth tracking month-to-month — it may reflect heavier cycling as March generation increases, or it may be measurement variability. If any month drops below 90%, investigate BMS calibration or inverter firmware.

---

## Month-over-Month Trends

| Metric | Jan 2026 | Feb 2026 | Change | Mar 2026 | Change |
|---|---|---|---|---|---|
| Avg daily PV | 16.7 kWh | 23.6 kWh | **+41%** | 27.2 kWh | +15% |
| Avg daily load | 26.8 kWh | 27.5 kWh | +2% | 29.4 kWh | +7% |
| Self-sufficiency | 60.0% | 72.9% | **+13pp** | 76.5% | +4pp |
| Grid dependence | 40.0% | 27.0% | −13pp | 23.0% | −4pp |
| Battery efficiency | 96.7% | 96.3% | −0.4pp | 94.5% | −1.8pp |

The dominant story is seasonal: solar generation rose 63% from January to March as the Philippine dry season intensified and the sun angle increased. Load grew more modestly (+10%), likely reflecting warmer temperatures and more air conditioning use — a trend that will probably continue into April and May. Self-sufficiency improvement is outpacing load growth, which is the ideal trajectory.

January's de-seasonalized baseline (15.6 kWh/day after removing the 1.07 dry-season factor) is notably lower than February (22.0) and March (25.4), suggesting January 2026 may have had unusual cloud cover or the system was still stabilizing in its first weeks. This pulls the annual projection baseline down; if January proves to be an outlier, the real annual output will be higher than projected.

---

## Annual Projection

- **Data coverage**: 3 months — moderate confidence (all dry-season months; no wet-season calibration yet)
- **De-seasonalized baseline**: 21.0 kWh/day (average of Jan 15.6, Feb 22.0, Mar 25.4 after removing 1.07 dry-season factor)
- **Projected annual generation**: ~7,681 kWh (year 1) → ~7,305 kWh (year 10) → ~6,776 kWh (year 25)
- **Projected annual self-consumed**: ~6,675 kWh
- **Projected annual grid export**: ~1,006 kWh
- **Environmental impact**: ~4.5 tonnes CO₂ avoided annually (at 0.68 kg CO₂/kWh for the Philippine grid), equivalent to ~206 trees planted or ~21,600 km of driving per year

Cavite's wet season (roughly June–October) brings consistent cloud cover and typhoon-related overcast periods that suppress generation. Projected wet-season months will average ~7% below the annual mean — about 19.5 kWh/day — compared to the ~25 kWh/day now being observed. Running this analysis after July 2026 will calibrate the wet-season adjustment and significantly improve projection confidence.

---

## Appendix

### Best and Worst Days

**Best day: 2026-03-19** — PV 30.0 kWh, Load 25.5 kWh, Grid import 1.4 kWh, Grid export 6.4 kWh. Non-EV day. Battery reached 100% SOC. A textbook clear dry-season day: generation comfortably exceeded household consumption, the battery filled by midday, and 6.4 kWh went to the grid. Self-sufficiency: **95%**.

**Worst day: 2026-01-02** — PV 4.7 kWh, Load 15.6 kWh, Grid import 12.5 kWh, Grid export 0 kWh. Non-EV day. Battery peaked at only 30% SOC, indicating heavy cloud from sunrise. Grid covered 80% of demand. Load was also lower than average (15.6 vs. 24.2 kWh), consistent with post-New Year reduced activity. Self-sufficiency: **20%**.

### Capacity Factor

| Month | Avg Daily kWh | Peak Sun Hours | Capacity Factor | Grid Dependence |
|---|---|---|---|---|
| Jan 2026 | 16.7 kWh | 2.6 h | 10.7% | 40.0% |
| Feb 2026 | 23.6 kWh | 3.6 h | 15.1% | 27.0% |
| Mar 2026 | 27.2 kWh | 4.2 h | 17.4% | 23.0% |

### Next Steps

- **Investigate Jan 16 night-time draw**: Use a smart plug or circuit breaker energy logger to identify what was drawing 8.2 kW at 22:00 — likely the most valuable diagnostic step from this report
- **Configure EVSE schedule**: Set charge completion time to 13:00–14:00 and compare next month's EV-day grid import to the current 17.5 kWh baseline
- **Re-run analysis after July 2026**: Wet-season data is needed to calibrate the annual projection and track battery efficiency trend through hotter, more humid months
- **Check inverter backup reserve setting**: Verify the configured SOC floor aligns with your outage backup requirements, given the 21% average morning minimum
- **Retrieve inverter logs for Feb 8 and Mar 17**: Only if those dates were clear-weather days; otherwise treat as weather events

### Assumptions and Limitations

- Self-consumed energy is calculated as `total_load − grid_import`, which measures actual solar offset of load and avoids inflating self-consumption figures by battery round-trip losses
- EV charging days are detected using a threshold of 8.4 kWh above the 27.9 kWh daily average (days exceeding ~36.3 kWh total load). The four load-anomaly days (36.0, 35.1, 35.2, 36.1 kWh) sit just below this threshold and were correctly classified as non-EV high-load days
- Annual projection uses 3 months of dry-season data (all with seasonal factor 1.07); wet-season performance has not yet been observed. The de-seasonalized baseline shows significant variance (15.6 → 22.0 → 25.4 kWh) beyond seasonal factors, possibly due to January 2026 cloud cover or early system stabilisation — this introduces additional uncertainty in the annual figure
- Panel degradation assumed at 0.5%/year (industry standard for monocrystalline silicon)
- Battery usable capacity estimated at 14.3 kWh (matching nominal), consistent with a new LFP system; actual BMS-reported usable capacity may differ slightly
- Bill impact assumes consistent monthly consumption patterns; seasonal increases in air conditioning load (likely April–June) are not modelled and will increase without-solar costs, improving the system's real savings above projections
- Feed-in tariff assumed constant at ₱7/kWh (50% of import rate); regulatory changes to net metering could affect export revenue

### Disclaimer

This report was generated by an AI model. While the numerical computations are performed by a deterministic script (`analyze.py`), the narrative interpretation, recommendations, and contextual inferences — seasonal adjustment factors, grid emission factors, sizing assessments, causal explanations — are AI-generated and may contain inaccuracies or misinterpretations. Verify critical findings, especially financial estimates and equipment diagnostics, against your own records, manufacturer specifications, or a qualified solar professional before making decisions based on this report.

### Data Sources

- `data/solar_hourly_2026-01.csv` — 31 days (Jan 1–31)
- `data/solar_hourly_2026-02.csv` — 28 days (Feb 1–28)
- `data/solar_hourly_2026-03.csv` — 30 days (Mar 1–30; Mar 31 excluded — no data yet)
