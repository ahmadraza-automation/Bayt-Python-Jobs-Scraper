"""
=========================================================
Bayt Python Jobs Scraper
Fixed Version - Full Pagination (No Limit)
=========================================================
"""

import asyncio
import random
import pandas as pd
from playwright.async_api import async_playwright


# ==============================
# CONFIG
# ==============================

BASE_URL = "https://www.bayt.com/en/pakistan/jobs/python-jobs/"
TIMEOUT = 60000
OUTPUT_FILE = "bayt_python_jobs.xlsx"


class BaytScraper:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.job_urls = []
        self.jobs = []

    async def start(self):
        self.playwright = await async_playwright().start()

        self.browser = await self.playwright.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        self.page = await self.browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/140.0.0.0 Safari/537.36"
            )
        )

        await self.page.add_init_script(
            """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
            """
        )
        print("Browser Started")

    async def delay(self, min_ms=1500, max_ms=3500):
        await self.page.wait_for_timeout(random.randint(min_ms, max_ms))

    async def open_page(self, url):
        print(f"\nOpening: {url}")
        await self.page.goto(url, wait_until="domcontentloaded", timeout=TIMEOUT)
        await self.delay()

    async def collect_urls(self):
        print("Collecting URLs...")

        try:
            await self.page.wait_for_selector("li[data-job-id]", timeout=10000)
        except:
            print("No job cards found on this page.")
            return 0

        cards = await self.page.locator("li[data-job-id]").all()
        print(f"Jobs found on this page: {len(cards)}")

        new_count = 0
        for card in cards:
            try:
                link = card.locator("a").first
                href = await link.get_attribute("href")

                if href:
                    if href.startswith("/"):
                        href = "https://www.bayt.com" + href

                    if href not in self.job_urls:
                        self.job_urls.append(href)
                        new_count += 1
            except:
                pass

        print(f"New URLs added: {new_count} | Total unique: {len(self.job_urls)}")
        return len(cards)

    async def scrape_pages(self):
        page_num = 1

        while True:
            if page_num == 1:
                url = BASE_URL
            else:
                url = f"{BASE_URL}?page={page_num}"

            print(f"\n========== PAGE {page_num} ==========")
            await self.open_page(url)

            jobs_on_page = await self.collect_urls()

            if jobs_on_page == 0:
                print(f"\nNo jobs found on page {page_num}. Stopping.")
                break

            page_num += 1

            if page_num > 100:
                print("Reached 100 pages safety limit.")
                break

        print(f"\n✅ Total Job URLs collected: {len(self.job_urls)}")

    async def extract_job(self, url):
        try:
            await self.page.goto(url, wait_until="domcontentloaded", timeout=TIMEOUT)
            await self.delay(1000, 2500)

            data = {
                "Title": "",
                "Company": "",
                "Location": "",
                "Description": "",
                "URL": url
            }

            title = self.page.locator("h1")
            if await title.count() > 0:
                data["Title"] = (await title.first.inner_text()).strip()

            company_selectors = [
                "[data-automation-id='job-company']",
                "span[class*='company']",
                "a[class*='company']",
                "div[class*='company']",
                "span[class*='jb-company']",
                ".t-company-name",
            ]
            for selector in company_selectors:
                company = self.page.locator(selector)
                if await company.count() > 0:
                    text = (await company.first.inner_text()).strip()
                    if text:
                        data["Company"] = text
                        break

            location_selectors = [
                "[data-automation-id='job-location']",
                "span[class*='location']",
                "div[class*='location']",
                ".t-loc",
                "span[class*='jb-loc']",
            ]
            for selector in location_selectors:
                loc = self.page.locator(selector)
                if await loc.count() > 0:
                    text = (await loc.first.inner_text()).strip()
                    if text:
                        data["Location"] = text
                        break

            desc_selectors = [
                "div#job-description",
                "div[class*='job-description']",
                "div[data-automation-id='job-description']",
                "div.t-job-description",
                "section.job-description",
            ]
            for selector in desc_selectors:
                desc = self.page.locator(selector)
                if await desc.count() > 0:
                    text = (await desc.first.inner_text()).strip()
                    if text and len(text) > 40:
                        data["Description"] = text
                        break

            if not data["Description"]:
                try:
                    desc = self.page.locator("div").filter(has_text="Job Description")
                    if await desc.count() > 0:
                        data["Description"] = (await desc.first.inner_text()).strip()
                except:
                    pass

            self.jobs.append(data)
            print(f"Saved: {data['Title'][:70]}")

        except Exception as e:
            print(f"Error on {url}: {e}")

    async def scrape_details(self):
        total = len(self.job_urls)
        print(f"\n========== Extracting {total} jobs ==========")

        for index, url in enumerate(self.job_urls, start=1):
            print(f"\nJob {index}/{total}")
            await self.extract_job(url)

    def save_excel(self):
        if not self.jobs:
            print("No jobs to save.")
            return

        df = pd.DataFrame(self.jobs)
        df.drop_duplicates(subset=["URL"], inplace=True)
        df.to_excel(OUTPUT_FILE, index=False)
        print(f"\n✅ Excel Saved: {OUTPUT_FILE}")
        print(f"Total unique jobs: {len(df)}")

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        print("Browser Closed")


async def main():
    scraper = BaytScraper()
    try:
        await scraper.start()
        await scraper.scrape_pages()
        await scraper.scrape_details()
        scraper.save_excel()
    finally:
        await scraper.close()


if __name__ == "__main__":
    asyncio.run(main())
