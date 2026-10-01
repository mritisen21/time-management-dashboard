# Time Management Challenges Among College Students – Dashboard

A static dashboard (HTML + JavaScript, no server needed) for the survey data collected via Google Forms.

## Files
| File | Purpose |
|---|---|
| `index.html` | The dashboard |
| `data.js` | Survey responses (names and timestamps removed) |
| `responses.xlsx` | Original Google Forms export |
| `build_data.py` | Rebuilds `data.js` from `responses.xlsx` |

## Run locally
Double-click `index.html` (needs internet once for the Chart.js library).

## Deploy on GitHub Pages
1. Create a new repository on GitHub (e.g. `time-management-dashboard`).
2. Upload all files in this folder to the repository root.
3. Go to **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`, then **Save**.
4. After a minute your dashboard is live at `https://<your-username>.github.io/time-management-dashboard/`.

## Update with new responses
Replace `responses.xlsx` with a fresh Google Forms export, then run:
```
pip install pandas openpyxl
python build_data.py
```
Commit the new `data.js`. `responses.xlsx` contains respondents' names, so it is listed in `.gitignore` and stays off GitHub — keep it that way.
