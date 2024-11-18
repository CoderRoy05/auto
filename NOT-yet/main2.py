

# this stimulate user behavior like scrolling then go back to 
# hero and make go to contact then make a submission slowly ,
# thn print out form submitted 
# but dont know why my gmail wont recieve the message 


# import time
# import random
# from playwright.sync_api import Playwright, sync_playwright, TimeoutError

# def simulate_user_behavior(page):
#     # Simulate scrolling with random pauses
#     for _ in range(random.randint(3, 10)):
#         page.mouse.wheel(0, random.randint(200, 600))  # Scroll down by random amount
#         time.sleep(random.uniform(1, 3))  # Random pause between scrolls

#     # Random interactions on the page
#     links = page.locator("a")
#     if links.count() > 0:
#         random_link = random.randint(0, links.count() - 1)
#         links.nth(random_link).click()
#         time.sleep(random.uniform(2, 5))  # Random pause after click

# def fill_and_submit_form(page):
#     # Wait for the form to be visible and fill in the details
#     try:
#         # Navigate to the form section
#         page.get_by_role("link", name="Get in touch").click()
#         time.sleep(2)  # Add a short delay to ensure the form is fully visible

#         # Fill the name input
#         page.locator("#name").click()
#         page.locator("#name").fill("zoy")
#         time.sleep(1)  # Add slight delay to mimic human input

#         # Fill the email input
#         page.locator("#email").click()
#         page.locator("#email").fill("smilie@gmail.com")
#         time.sleep(1)

#         # Fill the message input
#         page.locator("#message").click()
#         page.locator("#message").fill("This is an automated test message.")
#         time.sleep(1)

#         # Click submit
#         page.get_by_role("button", name="Submit").click()
#         print("Form submitted.")

#     except TimeoutError:
#         print("Form elements could not be found within the timeout period.")

# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(
#         user_agent=random.choice([
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0 Safari/537.36",
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
#             # Add more user agents to simulate different devices
#         ])
#     )
#     page = context.new_page()

#     try:
#         # Go to the target website
#         page.goto("https://royal-8vd.pages.dev/", timeout=15000)
        
#         # Simulate user behavior
#         simulate_user_behavior(page)

#         # Fill out and submit the form
#         fill_and_submit_form(page)

#     finally:
#         context.close()
#         browser.close()

# # Main execution
# with sync_playwright() as playwright:
#     run(playwright)




import time
import random
from faker import Faker
from playwright.sync_api import Playwright, sync_playwright, TimeoutError

fake = Faker()

def simulate_user_behavior(page):
    # Simulate scrolling with random pauses
    for _ in range(random.randint(3, 10)):
        page.mouse.wheel(0, random.randint(200, 600))
        time.sleep(random.uniform(1, 3))

    # Random interactions on the page
    links = page.locator("a")
    if links.count() > 0:
        random_link = random.randint(0, links.count() - 1)
        links.nth(random_link).click()
        time.sleep(random.uniform(2, 5))

def fill_and_submit_form(page):
    try:
        page.get_by_role("link", name="Get in touch").click()
        time.sleep(2)
        page.locator("#name").fill("zoy")
        time.sleep(1)
        page.locator("#email").fill("smilie@gmail.com")
        time.sleep(1)
        page.locator("#message").fill("This is an automated test message.")
        time.sleep(1)
        page.get_by_role("button", name="Submit").click()
        print("Form submitted.")
    except TimeoutError:
        print("Form elements could not be found within the timeout period.")

def run(playwright: Playwright) -> None:
    # Generate a random IP for the proxy
    proxy_ip = fake.ipv4()
    proxy_port = 8080  # Replace with the actual port if you have a proxy server

    browser = playwright.chromium.launch(
        headless=False,
        proxy={"server": f"http://{proxy_ip}:{proxy_port}"}
    )
    context = browser.new_context(
        user_agent=random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        ])
    )
    page = context.new_page()

    try:
        page.goto("https://royal-8vd.pages.dev/", timeout=15000)
        simulate_user_behavior(page)
        fill_and_submit_form(page)
    finally:
        context.close()
        browser.close()

# Main execution
with sync_playwright() as playwright:
    run(playwright)
