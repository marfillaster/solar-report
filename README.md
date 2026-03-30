# solar-report

Public GitHub Pages site for a residential solar performance summary covering January to March 2026.

## Files

- `index.html` - the shareable report page
- `styles.css` - the site styling

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
