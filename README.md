# webPrivacy-Audit-Project
# 🔒 Web Privacy Compliance & Tracker Detection System

### A Minor Project for B.Tech CSE (6th Semester)

## 📌 Project Overview
This tool is an automated privacy auditor designed to analyze educational websites for **"Pre-Consent Cookies."** It scans a list of university URLs, detects cookies planted before user consent, and classifies them into:
* **Safe:** Functional/Session Cookies (e.g., `JSESSIONID`, `CSRF-Token`)
* **Unsafe:** Analytics & Marketing Trackers (e.g., `_ga`, `_fbp`, `ads`)

The project generates a forensic CSV report and visualizes the data on an interactive **Web Dashboard**.

---

## 📂 Project Structure
Ensure your folder is organized as follows:
WebPrivacyAudit/ │ ├── app.py # Frontend: The Dashboard Code (Streamlit)
                                      ├── audit.py # Backend: The Scanner Script (Python + Requests) 
                                      ├── privacy_audit_report.csv # Database: Stores the scan results 
                                      ├── requirements.txt # Configuration: List of required libraries
                                       └── README.md # Documentation: This file
--- ##  Installation & Setup ### **
Step 1: Install Python** Ensure **Python 3.10+** is installed on your system. ### **
Step 2: Install Required Libraries** Open your terminal (PowerShell/CMD) in this folder and run: ```bash py -m pip install requests pandas openpyxl streamlit plotly
🚀 How to Run the Project
1. Run the Scanner (Backend)
This script visits the websites and updates the Excel file.
Bash
py audit.py
•	Wait for the "Scanning..." process to finish.
•	A file named privacy_audit_report.csv will be created/updated.
2. Launch the Dashboard (Frontend)
This command opens the graphical interface in your web browser.
Bash
py -m streamlit run app.py
•	The dashboard will automatically open in Chrome/Edge.
•	To stop the dashboard, press Ctrl + C in the terminal.
________________________________________
   How to Demo (For Examiners)
1.	Start the Dashboard using the command above.
2.	Show the "Safe" universities (Green rows).
3.	Show the "Violations" (Red rows) like LPU or UpGrad to demonstrate that the system successfully detects tracking cookies.
4.	Point out the "Compliance Ratio" Pie Chart to show the percentage of non-compliant websites.
________________________________________
Tech Stack
•	Language: Python 3.13
•	HTTP Client: Requests
•	Data Processing: Pandas
•	Visualization: Streamlit, Plotly Express

 Future Scope
•	Integration with Selenium to detect hidden JavaScript-based trackers.
•	Automated email alerts to university administrators upon detecting violations.
________________________________________
Developed by: [D V V SAIKRISHNA] Roll Number: [23CSE3040]

