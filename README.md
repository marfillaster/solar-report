# solar-report

Public GitHub Pages site for a residential solar performance summary covering January to March 2026.

## Files

- `index.html` - the shareable report page
- `styles.css` - the site styling
- `.codex/skills/update-solar-report-site/` - deterministic Codex skill for regenerating the site from `solar-analysis.md`

## Install For Codex

To make the repo skill available to Codex globally:

```bash
ln -s /Users/ken/solar-report/.codex/skills/update-solar-report-site \
  /Users/ken/.codex/skills/update-solar-report-site
```

Then invoke it in Codex with:

```text
Use $update-solar-report-site to refresh the public solar report site from the latest solar-analysis.md.
```

## Publish On GitHub Pages

1. Create a new GitHub repository named `solar-report`.
2. Add the remote:

```bash
git remote add origin git@github.com:<your-user>/solar-report.git
```

3. Commit and push:

```bash
git add .
git commit -m "Initial solar report site"
git branch -M main
git push -u origin main
```

4. In GitHub, open `Settings` -> `Pages`.
5. Under `Build and deployment`, choose:
   - `Source`: `Deploy from a branch`
   - `Branch`: `main`
   - `Folder`: `/ (root)`

The published site will use the redacted location `Cavite, Philippines`.
