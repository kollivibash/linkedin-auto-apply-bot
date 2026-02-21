# 🎯 LinkedIn Job Matcher — 100% FREE

No credit card. No paid APIs. Completely free.

---

## ✅ What's Free Here

| Tool | Purpose | Cost |
|------|---------|------|
| **JobSpy** | Scrapes LinkedIn, Indeed, Google Jobs | ₹0 — completely free |
| **Groq AI** | AI resume-job matching (Llama 3) | ₹0 — 14,400 requests/day free |

---

## ⚡ Setup (3 minutes)

### Step 1 — Install the library
```bash
pip install python-jobspy
```

### Step 2 — Get your FREE Groq API key
1. Go to 👉 https://console.groq.com
2. Sign up (takes 60 seconds, no credit card)
3. Click **API Keys** → **Create API Key**
4. Copy the key (starts with `gsk_...`)

### Step 3 — Add your key to the script
Open `job_matcher_free.py` and find line:
```python
GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE"
```
Replace with your actual key:
```python
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxx"
```

### Step 4 — Run it!
```bash
python job_matcher_free.py
```

---

## 📊 Output

An `output/` folder is created with:
- **`job_report_TIMESTAMP.html`** → Open in browser! Beautiful report with all matched jobs
- **`matched_jobs_TIMESTAMP.json`** → Raw data

---

## 🔧 Customize

In `job_matcher_free.py`:
```python
MATCH_THRESHOLD = 80    # Lower to 70 to see more jobs
MAX_JOBS_PER_SEARCH = 20  # Increase for more results

JOB_SEARCHES = [
    {"search_term": "Full Stack Developer", "location": "Hyderabad, India"},
    # Add more searches here...
]
```

---

## ⚠️ Tips

- If LinkedIn blocks you → Run again after 30 minutes (it rate-limits)
- Indeed usually works best without limits
- Each run takes ~10-15 minutes for 8 searches
- Run once a day to keep results fresh

---

## 🐛 Troubleshooting

**"No module named jobspy"** → Run `pip install python-jobspy`

**"No jobs found"** → LinkedIn may have rate-limited you. Wait 30 min and try again, or just use `site_name=["indeed", "google"]`

**Groq error 401** → Your API key is wrong. Check it at console.groq.com
