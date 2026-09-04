# Bayt Python Jobs Scraper

**Async Playwright scraper** that extracts Python jobs from Bayt.com (Pakistan) with full pagination and exports to Excel.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Async-green?logo=playwright)](https://playwright.dev/python/)
[![GitHub](https://img.shields.io/badge/GitHub-ahmadraza--automation-181717?logo=github)](https://github.com/ahmadraza-automation)

---

### Results

| Metric | Value |
|--------|-------|
| Jobs scraped | **281+** |
| Source | [Bayt.com – Python Jobs (Pakistan)](https://www.bayt.com/en/pakistan/jobs/python-jobs/) |
| Output | `bayt_python_jobs.xlsx` |
| Fields | Title, Company, Location, Description, URL |

---

### Features

- Full pagination support
- Collects all job URLs across pages
- Extracts Title, Company, Location, Description, URL
- Anti-detection (stealth user-agent + webdriver disabled)
- Human-like random delays
- Clean Excel export
- Duplicate URL removal

---

### Installation

```bash
pip install -r requirements.txt
playwright install chromium
```

---

### Usage

```bash
python bayt_scraper.py
```

---

### Author

**Ahmad Raza** — Python Automation Engineer  

- GitHub: [ahmadraza-automation](https://github.com/ahmadraza-automation)
- LinkedIn: [Ahmad Raza](https://www.linkedin.com/in/ahmad-raza-67462b413)
- Portfolio: [Live Portfolio](https://ahmadraza-automation.github.io/Ahmad-Raza-Automation-Portfolio/)

---

If you find this useful, please give it a ⭐
