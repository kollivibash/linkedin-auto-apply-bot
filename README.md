🤖 Multi-Step Web Automation Engine

A configurable browser automation framework designed to intelligently navigate and complete dynamic multi-page web workflows.

<img width="145" height="28" alt="image" src="https://github.com/user-attachments/assets/f0874b84-b1a6-400c-9e6a-5dd7a6970fa8" />

<img width="149" height="28" alt="image" src="https://github.com/user-attachments/assets/60af5152-1488-415d-85ac-f60fbd6b7673" />

<img width="125" height="28" alt="image" src="https://github.com/user-attachments/assets/008986be-27db-4108-8116-d998e8ccec7f" />



🚀 Overview

Multi-Step Web Automation Engine is a Selenium-based automation framework that dynamically interacts with complex web applications.

It is built to:

Navigate dynamic web listings

Detect and interact with form elements intelligently

Handle multi-step workflows (Next → Review → Submit logic)

Apply configurable input mapping logic

Generate structured execution summaries

This project focuses on building a reusable automation architecture, not a platform-specific script.

🧠 Key Engineering Highlights

Dynamic DOM parsing using Selenium WebDriver

Intelligent input field detection (label & placeholder matching)

Dropdown prioritization logic

Multi-page workflow state management

Skip & error handling mechanisms

Secure credential input (no hardcoded secrets)

Configurable search and workflow parameters

Execution summary reporting system

📸 Sample Execution Preview
=======================================================
  🤖 Multi-Step Web Automation Engine
  Vibash Kolli | Hyderabad
=======================================================

🔐 Authenticating session...
✅ Session established!

🔍 Searching with configured parameters
  Found 25 listings — processing up to 10...
  📝 Processing: Full Stack Developer @ ExampleCorp
  ✅ Workflow completed successfully!

=======================================================
  📊 FINAL SUMMARY
=======================================================
  ✅ Successfully Processed : 47
  ⏭️  Skipped               : 8
=======================================================
⚙️ How It Works

The engine:

Launches a controlled browser session

Navigates to a configured search endpoint

Iterates through discovered listings

Detects interactive form elements dynamically

Matches input fields using keyword-based logic

Applies dropdown prioritization strategy

Progresses through multi-step workflows

Submits and records final execution status

The system is designed to be adaptable to various structured web workflows.

🛠️ Installation
Prerequisites

Python 3.8+

Google Chrome

Git

Setup
# Clone the repository
git clone https://github.com/kollivibash/Multi-Step-Web-Automation-Engine.git
cd Multi-Step-Web-Automation-Engine

# Create virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
🔧 Configuration

Edit the configuration block in:

linkedin_auto_apply_v2.py

Example:

SEARCH_QUERIES = [
    "Full Stack Developer",
    "Python Developer",
]

LOCATIONS = ["Hyderabad", "Bengaluru", "Remote"]

DEFAULT_ANSWERS = {
    "phone": "YOUR_PHONE_NUMBER",
    "notice_period": "Immediate",
    "years_experience": "0",
}

The engine executes combinations of configured parameters to simulate structured workflow automation.

▶️ Usage
python linkedin_auto_apply_v2.py

The browser session will open and the engine will execute the configured workflow automatically.

📁 Project Structure
Multi-Step-Web-Automation-Engine/
├── linkedin_auto_apply_v2.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
🧩 Future Improvements

Structured logging system

Headless execution mode

Modular configuration (YAML/JSON)

Retry & rate-limiting mechanisms

Docker support

Unit test coverage

⚠️ Disclaimer

This project is developed for educational and automation research purposes.
Users are responsible for ensuring compliance with the terms of service of any platform where automation is applied.

📄 License

MIT © Vibash Kolli
