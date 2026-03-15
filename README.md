# Groww App Review Weekly Pulse

This project converts recent Groww app reviews into a weekly product pulse.

It was built for **NextLeap LIP Challenge – Milestone 3**.

---

# Workflow

Import reviews → Group themes → Generate weekly note → Draft email

The system uses a simple LLM workflow to summarize recent app reviews.

---

# Files

reviews.csv  
Sample dataset containing recent Groww app reviews.

app.py  
Streamlit prototype that converts reviews into a weekly product pulse.

weekly_pulse.md  
Example generated weekly note.

email_draft.md  
Example internal email summary.

---

# Theme Legend

KYC / Onboarding  
Customer Support  
App Performance  
Withdrawals / Payments  
Ease of Use

---

# How to Re-run for a New Week

1. Replace the data in `reviews.csv` with new reviews.
2. Run the Streamlit app.
3. Click **Generate Weekly Pulse** to produce the new report.

---

# Notes

- Only public review data is used.
- No personal information is included.
- Quotes are anonymized.
