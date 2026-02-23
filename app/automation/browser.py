from playwright.async_api import async_playwright

class BrowserFactory:

    @staticmethod
    async def create(headless=False):
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()
        return playwright, browser, context, page
