# name: Run Visitor Simulation Tests

# on:
#   push:
#     branches:
#       - main
#   pull_request:
#     branches:
#       - main

# jobs:
#   simulate-visitors:
#     runs-on: ubuntu-latest
#     strategy:
#       matrix:
#         batch: [1, 2, 3, 4, 5] # 5 batches

#     steps:
#     - name: Checkout Code
#       uses: actions/checkout@v3

#     - name: Set up Python
#       uses: actions/setup-python@v4
#       with:
#         python-version: '3.10'

#     - name: Install Playwright
#       run: |
#         python -m pip install --upgrade pip
#         pip install -r requirements.txt
#         playwright install-deps
#         playwright install

#     - name: Run Simulation Script (Batch ${{ matrix.batch }})
#       run: xvfb-run --auto-servernum -- python ro1.py $((5000 / 5)) # Adjust batch size














# from playwright.sync_api import sync_playwright
# import random
# import time
# import threading

# def simulate_visitors_batch(start, end):
#     """
#     Simulate a batch of visitors to a website.

#     Args:
#     - start: Starting index for this batch of visitors.
#     - end: Ending index for this batch of visitors.
#     """
#     with sync_playwright() as p:
#         # Launch the browser (headless=True for headless mode)
#         browser = p.chromium.launch(headless=True)

#         # Define a list of valid devices to emulate
#         devices = [
#             p.devices["iPhone 12"],
#             p.devices["Galaxy S9+"],
#             p.devices["iPad Pro 11"],
#             p.devices["iPhone XR"],
#             p.devices["Kindle Fire HDX"],
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

#         for i in range(start, end):
#             try:
#                 # Randomly select a device or default to desktop
#                 device = random.choice(devices)

#                 if device:
#                     # Create a context emulating the chosen device
#                     context = browser.new_context(**device)
#                 else:
#                     # Create a default browser context
#                     context = browser.new_context()

#                 # Open a new page within the context
#                 page = context.new_page()

#                 # Navigate to the website
#                 page.goto('https://royal-8vd.pages.dev')

#                 # Random scroll
#                 if random.choice([True, False]):
#                     page.evaluate("window.scrollBy(0, window.innerHeight);")

#                 # Random click on the page
#                 body = page.locator("body")
#                 if body.is_visible():
#                     x = random.randint(0, page.viewport_size['width'] - 1)
#                     y = random.randint(0, page.viewport_size['height'] - 1)
#                     page.mouse.click(x, y)

#                 # Random short wait
#                 time.sleep(random.uniform(1, 3))

#                 # Close the page and context
#                 page.close()
#                 context.close()

#                 # Log periodically
#                 if i % 100 == 0:
#                     print(f"Visitor {i} simulated.")

#             except Exception as e:
#                 print(f"Error during simulation for visitor {i}: {e}")

#         # Close the browser
#         browser.close()

# def simulate_visitors(number_of_visitors, threads=5):
#     """
#     Simulate visitors using multiple threads.
#     """
#     batch_size = number_of_visitors // threads
#     threads_list = []

#     for i in range(threads):
#         start = i * batch_size
#         end = start + batch_size if i < threads - 1 else number_of_visitors
#         thread = threading.Thread(target=simulate_visitors_batch, args=(start, end))
#         threads_list.append(thread)
#         thread.start()

#     for thread in threads_list:
#         thread.join()

# # Simulate 5000 visitors
# simulate_visitors(number_of_visitors=5000, threads=10)
