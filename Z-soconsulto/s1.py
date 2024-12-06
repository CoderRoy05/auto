# from playwright.sync_api import sync_playwright
# import random
# import time

# def simulate_visitors(number_of_visitors):
#     """
#     Simulate visitors to a website with different device types and referrer traffic.

#     Args:
#     - number_of_visitors: Number of virtual visitors to simulate.
#     """
#     with sync_playwright() as p:
#         # Launch the browser (headless=True for headless mode)
#         browser = p.chromium.launch(headless=False)

#         # Define a list of valid devices to emulate
#         devices = [
#             p.devices["iPhone 12"],
#             p.devices["Galaxy S9+"],
#             p.devices["iPad Pro 11"],
#             p.devices["iPhone XR"],
#             p.devices["Kindle Fire HDX"],  # Adding variety
#             p.devices["Moto G4 landscape"],
#             p.devices["Desktop Chrome HiDPI"],
#             p.devices["Desktop Edge HiDPI"],
#             p.devices["Desktop Firefox HiDPI"],
#             p.devices["Desktop Safari"],
#             p.devices["Desktop Chrome"],
#             p.devices["Desktop Edge"],
#             p.devices["Desktop Firefox"],
#             None,  # Default desktop device
#         ]

#         # List of referrers for traffic simulation
#         referrers = [
#             "https://www.google.com",
#             "https://www.bing.com",
#             "https://www.facebook.com",
#             "https://www.twitter.com",
#             "https://www.instagram.com",
#         ]

#         for i in range(number_of_visitors):
#             try:
#                 # Randomly select a device or default to desktop
#                 device = random.choice(devices)

#                 if device:
#                     # Create a context emulating the chosen device
#                     context = browser.new_context(**device)
#                     device_name = device.get("name", "Unknown Device")  # Safely access device name
#                 else:
#                     # Create a default browser context
#                     context = browser.new_context()
#                     device_name = "Desktop"

#                 # Open a new page within the context
#                 page = context.new_page()

#                 # Set a random referrer for the visit
#                 referrer = random.choice(referrers)
#                 page.set_extra_http_headers({"Referer": referrer})

#                 # Navigate to the target website (Soconsulto page)
#                 page.goto('https://soconsulto.pages.dev/')

#                 # Simulate random actions (e.g., scrolling)
#                 if random.choice([True, False]):  # Randomly decide to scroll
#                     for _ in range(random.randint(3, 6)):
#                         page.evaluate("window.scrollBy(0, window.innerHeight);")
#                         time.sleep(random.uniform(3, 6))  # Pause between scrolls

#                 # Simulate time spent on the page (dwell time)
#                 time.sleep(random.uniform(5, 12))

#                 # Close the page and context
#                 page.close()
#                 context.close()

#                 # Log a simplified output message
#                 print(f"Visitor {i + 1} referrer: {referrer} successfully.")

#             except Exception as e:
#                 print(f"Error during simulation for visitor {i + 1}: {e}")

#         # Close the browser
#         browser.close()

# # Simulate 100 visitors
# simulate_visitors(number_of_visitors=50)



# # ONLY https://soconsulto.pages.dev/ !!NAV!! 



from playwright.sync_api import sync_playwright
import random
import time

def simulate_visitors(number_of_visitors):
    """
    Simulate visitors to a website with different device types and referrer traffic.

    Args:
    - number_of_visitors: Number of virtual visitors to simulate.
    """
    with sync_playwright() as p:
        # Launch the browser (headless=True for headless mode)
        browser = p.chromium.launch(headless=False)

        # Define a list of valid devices to emulate
        devices = [
            p.devices["iPhone 12"],
            p.devices["Galaxy S9+"],
            p.devices["iPad Pro 11"],
            p.devices["iPhone XR"],
            p.devices["Kindle Fire HDX"],  # Adding variety
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

        # List of referrers for traffic simulation
        referrers = [
            "https://www.google.com",
            "https://www.bing.com",
            "https://www.facebook.com",
            "https://www.twitter.com",
            "https://www.instagram.com",
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

                # Set a random referrer for the visit
                referrer = random.choice(referrers)
                page.set_extra_http_headers({"Referer": referrer})

                # Navigate to the target website (Soconsulto page)
                page.goto('https://soconsulto.pages.dev/')

                # Simulate scrolling to the bottom of the page
                for _ in range(random.randint(5, 10)):
                    page.evaluate("window.scrollBy(0, window.innerHeight);")  # Scroll by window height
                    time.sleep(random.uniform(3, 5))  # Pause between scrolls

                # Simulate time spent on the page (dwell time)
                time.sleep(random.uniform(5, 12))

                # Close the page and context
                page.close()
                context.close()

                # Log a simplified output message
                print(f"Visitor {i + 1} referrer: {referrer} successfully.")

            except Exception as e:
                print(f"Error during simulation for visitor {i + 1}: {e}")

        # Close the browser
        browser.close()

# Simulate 50 visitors
simulate_visitors(number_of_visitors=50)
