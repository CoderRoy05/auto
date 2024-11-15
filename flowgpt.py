from playwright.sync_api import sync_playwright
import random
import time

# List of diverse user-agents to simulate different devices and browsers
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",
]

# List of screen sizes to simulate different devices
SCREEN_SIZES = [
    {"width": 1920, "height": 1080},  # Desktop
    {"width": 1366, "height": 768},   # Smaller desktop
    {"width": 375, "height": 667},    # iPhone 6/7/8
    {"width": 414, "height": 896},    # iPhone XR
]

def simulate_visitors(number_of_visitors):
    with sync_playwright() as p:
        # Launch the browser (non-headless for visibility)
        browser = p.chromium.launch(headless=False)

        for i in range(number_of_visitors):
            # Choose a random user-agent and screen size for each visitor
            user_agent = random.choice(USER_AGENTS)
            screen_size = random.choice(SCREEN_SIZES)

            # Open a new incognito session with the chosen user-agent
            context = browser.new_context(user_agent=user_agent, viewport=screen_size)

            # Open a new page (representing a new visitor)
            page = context.new_page()

            # Navigate to the website
            page.goto('https://royal-8vd.pages.dev')

            # Mimic user interaction by scrolling down sometimes
            time.sleep(random.uniform(2, 5))  # Wait for initial page load
            if random.choice([True, False]):
                page.evaluate("window.scrollBy(0, document.body.scrollHeight)")  # Random scroll down
                time.sleep(random.uniform(1, 3))  # Wait after scrolling

            # Randomly stay on the page longer to mimic user engagement
            time.sleep(random.uniform(5, 20))

            # Close the page and context (incognito session)
            page.close()
            context.close()

        # Close the browser
        browser.close()

# Set the number of visitors
simulate_visitors(number_of_visitors=20)
