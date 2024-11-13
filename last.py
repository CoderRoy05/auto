from playwright.sync_api import sync_playwright
import random
import time

def simulate_visitors(number_of_visitors):
    with sync_playwright() as p:
        # Launch the browser (non-headless for UI, headless=True for headless mode)
        browser = p.chromium.launch(headless=False)

        for i in range(number_of_visitors):
            # Open a new page (a new visitor)
            page = browser.new_page()
            # Navigate to the website
            page.goto('https://royal-8vd.pages.dev')
            # Wait between 2 to 7 seconds
            time.sleep(random.uniform(2, 7))
            # Close the page
            page.close()

        # Close the browser
        browser.close()

# Set the number of visitors
simulate_visitors(number_of_visitors=20)
