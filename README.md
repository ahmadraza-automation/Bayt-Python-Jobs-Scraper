# Bayt Python Jobs Scraper

Async Playwright scraper that extracts **Python jobs from Bayt.com (Pakistan)** with full pagination support and exports results to Excel.

## Features

- Full pagination (`?page=1`, `?page=2`, ...) — no page limit
- Collects all job URLs across pages
- Extracts Title, Company, Location, Description, URL
- Anti-detection (stealth user-agent + webdriver flag disabled)
- Human-like random delays
- Exports clean data to `bayt_python_jobs.xlsx`
- Duplicate URL removal

## Tech Stack

- Python 3
- Playwright (async)
- Pandas + openpyxl

## Setup

```bash
pip install -r requirements.txt
playwright install chromium
```

## Run

```bash
python bayt_scraper.py
```

Output file: `bayt_python_jobs.xlsx`

## Notes

- Runs with `headless=False` by default (visible browser)
- Stops automatically when a page returns 0 jobs
- Safety limit of 100 pages included

---

Built by [Ahmad Raza](https://github.com/ahmadraza-automation)
