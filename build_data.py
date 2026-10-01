"""Convert responses.xlsx (Google Forms export) into data.js for the dashboard.
Usage:  pip install pandas openpyxl && python build_data.py
Names and timestamps are dropped so no personal data is published."""
import json
import pandas as pd

KEYS = ["gender", "age", "year", "study_hours", "tm_rating", "planning", "balance",
        "challenge", "postpone", "mobile", "assign_diff", "perf_impact", "stress",
        "method", "improve", "reason"]
FIX = {"20-22": "20–22", "17-19": "17–19", "23-25": "23–25",
       "2-4hours": "2–4 hours", "4-6hours": "4–6 hours", "Less than 1hour": "Less than 1 hour",
       "1-3 hours": "1–3 hours", "3-5 hours": "3–5 hours",
       "Mobile remainders": "Mobile reminders", "Academic": "Academic work",
       "Social media usage": "Reduced social media usage"}

df = pd.read_excel("responses.xlsx")
df = df.iloc[:, 2:2 + len(KEYS)]          # skip timestamp + name
df.columns = KEYS
df = df.dropna(how="all").astype(str).apply(lambda s: s.str.strip().replace(FIX))
# "Social media" (challenge) must stay as-is; only the improve column uses the long label
df["challenge"] = df["challenge"].replace({"Reduced social media usage": "Social media"})
with open("data.js", "w", encoding="utf-8") as f:
    f.write("const DATA = " + json.dumps(df.to_dict("records"), ensure_ascii=False, indent=1) + ";\n")
print(f"Wrote data.js with {len(df)} responses")
