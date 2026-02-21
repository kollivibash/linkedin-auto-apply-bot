# 🤖 LinkedIn Auto-Apply Bot v2

> Automatically search and apply to LinkedIn Easy Apply jobs — no scraped URLs needed.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green?style=for-the-badge&logo=selenium)
![LinkedIn](https://img.shields.io/badge/LinkedIn-Easy%20Apply-0077B5?style=for-the-badge&logo=linkedin)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 🚀 What It Does

- Logs into LinkedIn with your credentials
- Searches directly on LinkedIn for Easy Apply jobs using your configured roles and locations
- Automatically clicks Easy Apply, fills in the form fields, and submits
- Handles multi-page applications (up to 15 pages per job)
- Prints a summary of applied vs skipped jobs at the end

---

## 📸 Preview

```
=======================================================
  🤖 LinkedIn Auto-Apply Bot v2
  Vibash Kolli | Hyderabad
=======================================================

🔐 Logging into LinkedIn...
✅ Logged in!

🔍 Searching: 'Full Stack Developer' in 'Hyderabad'
  Found 25 jobs — applying to up to 10...
  📝 Applying: Full Stack Developer @ TechCorp
  ✅ Applied!

=======================================================
  📊 FINAL SUMMARY
=======================================================
  ✅ Successfully Applied : 47
  ⏭️  Skipped              : 8
=======================================================
```

---

## ⚙️ How It Works

The bot searches LinkedIn using this URL pattern with Easy Apply filter (`f_AL=true`) enabled:

```
linkedin.com/jobs/search/?keywords=...&location=...&f_AL=true&f_E=1,2&sortBy=DD
```

For each job it finds, it:
1. Clicks the job card
2. Looks for the Easy Apply button
3. Fills text inputs by matching label/placeholder keywords (phone, name, city, salary, experience, notice period)
4. Handles `<select>` dropdowns — prefers "Immediate", then "Yes", then first option
5. Clicks through pages using Next/Continue/Review buttons
6. Submits and dismisses the confirmation modal

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Google Chrome
- Git

### Steps

```bash
# Clone the repo
git clone https://github.com/kollivibash/linkedin-auto-apply-bot.git
cd linkedin-auto-apply-bot

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🔧 Configuration

Edit the config block at the top of `linkedin_auto_apply_v2.py`:

```python
LINKEDIN_EMAIL = "your@email.com"

SEARCH_QUERIES = [
    "Full Stack Developer",
    "Python Developer",
    "React Developer",
    "Data Analyst",
    "Software Engineer",
]

LOCATIONS = ["Hyderabad", "Bengaluru", "Remote"]

DEFAULT_ANSWERS = {
    "phone":            "YOUR_PHONE_NUMBER",
    "first_name":       "Your First Name",
    "last_name":        "Your Last Name",
    "city":             "Your City",
    "notice_period":    "Immediate",
    "current_salary":   "0",
    "expected_salary":  "0",
    "years_experience": "0",
}

MAX_JOBS_PER_SEARCH = 10  # jobs to apply per search combination
```

The bot runs `len(SEARCH_QUERIES) × len(LOCATIONS)` search combinations — with the defaults that's **15 searches** and up to **150 applications**.

---

## ▶️ Usage

```bash
python linkedin_auto_apply_v2.py
```

You'll be securely prompted for your LinkedIn password (it won't show on screen). Chrome will open and the bot starts working automatically.

> 💡 Keep the browser visible — LinkedIn may ask for CAPTCHA or 2FA verification midway.

---

## 📁 Project Structure

```
linkedin-auto-apply-bot/
├── linkedin_auto_apply_v2.py   # Main bot script
├── requirements.txt             # Python dependencies
├── .gitignore                   # Ignores cache & secrets
├── LICENSE                      # MIT License
└── README.md                    # This file
```

---

## ⚠️ Disclaimer

This tool is for **personal and educational use only**. Using bots on LinkedIn may violate their Terms of Service. Use at your own risk. Never commit your email or password to a public repository.

---

## 📄 License

MIT © [Vibash Kolli](https://github.com/kollivibash)
