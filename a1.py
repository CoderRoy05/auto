from playwright.sync_api import sync_playwright
import random
import time

def simulate_visitors(number_of_visitors, url):
    """
    Simulate visitors to a website with network throttling and demographic details.
    
    Args:
    - number_of_visitors: The number of virtual visitors to simulate.
    - url: The URL of the website to visit.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Use headless mode for scalability

        # Define network conditions
        network_conditions = [
            {"download": 500 * 1024, "upload": 500 * 1024, "latency": 20},  # Fast 4G
            {"download": 100 * 1024, "upload": 100 * 1024, "latency": 100}, # Slow 3G
            {"download": 50 * 1024, "upload": 50 * 1024, "latency": 300},   # Slow 2G
        ]

        # Define demographic settings
        demographics = [
            {"geo": "US", "language": "en-US", "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
            {"geo": "NG", "language": "en-NG", "userAgent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"},
            {"geo": "IN", "language": "hi-IN", "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
            {"geo": "FR", "language": "fr-FR", "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
        ]

        for i in range(number_of_visitors):
            try:
                # Select random demographics and network condition
                demographic = random.choice(demographics)
                network_condition = random.choice(network_conditions)

                # Create a browser context with specific user-agent and language
                context = browser.new_context(
                    user_agent=demographic["userAgent"],
                    viewport={"width": 1280, "height": 720},
                    locale=demographic["language"]
                )

                # Intercept and throttle network requests
                def throttle(route):
                    time.sleep(network_condition["latency"] / 1000)  # Simulate latency
                    route.continue_()

                context.route("**/*", throttle)

                # Open a new page
                page = context.new_page()

                # Visit the website
                page.goto(url)

                # Simulate random interactions (e.g., scrolling)
                if random.choice([True, False]):  # Randomly decide whether to scroll
                    for _ in range(random.randint(1, 5)):
                        page.evaluate("window.scrollBy(0, window.innerHeight);")
                        time.sleep(random.uniform(1, 3))  # Pause between scrolls

                # Simulate random time spent on the page
                time.sleep(random.uniform(5, 15))

                # Close the context (closes all pages within it)
                context.close()

            except Exception as e:
                print(f"Error during simulation for visitor {i + 1}: {e}")

        browser.close()

# Example usage
simulate_visitors(number_of_visitors=50, url="https://royal-8vd.pages.dev")
