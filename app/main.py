import asyncio
from app.db.database import init_db
from app.automation.browser import BrowserFactory

async def main():
    await init_db()

    playwright, browser, context, page = await BrowserFactory.create(headless=False)

    print("Opening browser...")
    await page.goto("https://example.com")
    await page.wait_for_timeout(5000)

    print("Closing browser...")
    await browser.close()
    await playwright.stop()

if __name__ == "__main__":
    asyncio.run(main())
