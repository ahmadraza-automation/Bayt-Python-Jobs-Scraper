# Bayt Python Jobs Scraper

Async Playwright scraper that extracts **Python jobs from Bayt.com (Pakistan)** with full pagination support and exports results to Excel.

## Results

| Metric | Value |
|--------|-------|
| Jobs scraped | **281** |
| Source | [Bayt.com – Python Jobs (Pakistan)](https://www.bayt.com/en/pakistan/jobs/python-jobs/) |
| Output | `bayt_python_jobs.xlsx` |
| Fields | Title, Company, Location, Description, URL |

## Features

- Full pagination (`?page=1`, `?page=2`, ...) — no page limit
- Collects all job URLs across pages
- Extracts Title, Company, Location, Description, URL
- Anti-detection (stealth user-agent + webdriver flag disabled)
- Human-like random delays
- Exports clean data to Excel
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

## Sample Output

See `sample_jobs.csv` for a sample of scraped jobs.

## Notes

- Runs with `headless=False` by default (visible browser)
- Stops automatically when a page returns 0 jobs
- Safety limit of 100 pages included

---

Built by [Ahmad Raza](https://github.com/ahmadraza-automation) · [Portfolio](https://github.com/ahmadraza-automation/Ahmad-Raza-Automation-Portfolio)
