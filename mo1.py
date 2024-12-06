from playwright.sync_api import sync_playwright
import random
import time

def simulate_visitors(number_of_visitors):
    """
    Simulate visitors to a website with different device types and allow body clicks.

    Args:
    - number_of_visitors: Number of virtual visitors to simulate.
    """
    with sync_playwright() as p:
        # Launch the browser (headless=True for headless mode)
        browser = p.chromium.launch(headless=True)

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

                # Open a new page within the context
                page = context.new_page()

                # Navigate to the website
                page.goto('https://royal-8vd.pages.dev/')

                # Simulate random interactions (e.g., scrolling)
                if random.choice([True, False]):  # Randomly decide to scroll
                    for _ in range(random.randint(1, 3)):
                        page.evaluate("window.scrollBy(0, window.innerHeight);")
                        time.sleep(random.uniform(1, 3))  # Pause between scrolls

                # Simulate random clicks on the page body
                body = page.locator("body")
                if body.is_visible():
                    # Perform a random click within the body element
                    x = random.randint(0, page.viewport_size['width'] - 1)
                    y = random.randint(0, page.viewport_size['height'] - 1)
                    page.mouse.click(x, y)
                    print(f"Clicked on coordinates ({x}, {y}) in the body.")

                # Wait between 2 to 7 seconds to mimic real visitor behavior
                time.sleep(random.uniform(4, 7))

                # Close the page and context
                page.close()
                context.close()

                print(f"Visitor {i + 1} simulated with device: {device_name}")

            except Exception as e:
                print(f"Error during simulation for visitor {i + 1}: {e}")

        # Close the browser
        browser.close()

# Simulate 500 visitors
simulate_visitors(number_of_visitors=500)



# nav with clickable for ads 
