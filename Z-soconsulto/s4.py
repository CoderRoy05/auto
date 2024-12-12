from playwright.sync_api import sync_playwright
import random
import time

def scroll_to_bottom(page):
    """
    Scroll to the bottom of the page dynamically.
    Continues scrolling until no more height is available.
    """
    try:
        while True:
            # Get the current scroll position and total scrollable height
            previous_height = page.evaluate("document.documentElement.scrollTop + window.innerHeight")
            
            # Scroll down by the window height
            page.evaluate("window.scrollBy(0, window.innerHeight);")
            
            # Wait to allow content to load (if any dynamic loading occurs)
            time.sleep(random.uniform(1, 2))
            
            # Get the new scroll position
            current_height = page.evaluate("document.documentElement.scrollTop + window.innerHeight")
            
            # Break if we have reached the bottom of the page
            if current_height == previous_height:
                break
    except Exception as e:
        print(f"Error during scrolling: {e}")

def simulate_random_navigation_with_devices(number_of_visitors):
    """
    Simulate visitors navigating randomly between website pages with device emulation and referrers.

    Args:
    - number_of_visitors: Number of virtual visitors to simulate.
    """
    with sync_playwright() as p:
        # Launch the browser (headless=True for headless mode)
        browser = p.chromium.launch(headless=False)

        # Define all pages on the website
        pages = [
            'https://sjr.pages.dev/',
            'https://sjr.pages.dev/order',
            'https://sjr.pages.dev/company',
            'https://sjr.pages.dev/faq',
            'https://sjr.pages.dev/contact'
        ]

        # Define a list of valid devices to emulate
        devices = [
            p.devices["iPhone 12"],
            p.devices["Galaxy S9+"],
            p.devices["iPad Pro 11"],
            p.devices["iPhone XR"],
            p.devices["Kindle Fire HDX"],
            p.devices["Moto G4 landscape"],
            p.devices["Desktop Chrome HiDPI"],
            p.devices["Desktop Edge HiDPI"],
            p.devices["Desktop Firefox HiDPI"],
            p.devices["Desktop Safari"],
            p.devices["Desktop Chrome"],
            p.devices["Desktop Edge"],
            p.devices["Desktop Firefox"],
            None,  # Default desktop device
        ]

        # Define a list of referrers for traffic simulation
        referrers = [
            "https://www.google.com",
            "https://www.bing.com",
            "https://www.instagram.com",
            "https://www.youtube.com", 
            "https://www.linkedin.com", 
        ]

        for i in range(number_of_visitors):
            try:
                # Randomly select a device or default to desktop
                device = random.choice(devices)

                if device:
                    # Create a context emulating the chosen device
                    context = browser.new_context(**device)
                    device_name = device.get("name", "Unknown Device")  # Safely access device name
                else:
                    # Create a default browser context
                    context = browser.new_context()
                    device_name = "Desktop"

                # Open a new page in the context
                page = context.new_page()

                # Set a random referrer for the visit
                referrer = random.choice(referrers)
                page.set_extra_http_headers({"Referer": referrer})

                # Randomly decide the number of pages this visitor will navigate
                num_pages_to_visit = random.randint(1, len(pages))

                # Randomly select pages to visit, without replacement
                selected_pages = random.sample(pages, num_pages_to_visit)

                for page_url in selected_pages:
                    # Navigate to the page
                    page.goto(page_url)

                    # Scroll dynamically to the bottom
                    scroll_to_bottom(page)

                    # Wait between 2 to 7 seconds to mimic real user behavior
                    time.sleep(random.uniform(7, 15))

                # Close the page and context after completing navigation
                page.close()
                context.close()

                # Simplified log output
                print(f"Visitor {i + 1} referrer: {referrer} navigated to {num_pages_to_visit} page(s) successfully.")

            except Exception as e:
                print(f"Error during simulation for visitor {i + 1}: {e}")

        # Close the browser
        browser.close()

# Simulate 5000 visitors with random navigation and device emulation
simulate_random_navigation_with_devices(number_of_visitors=100)


# # NAVigation to random pages !!NAV!! FOR SJR!!