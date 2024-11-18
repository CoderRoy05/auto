# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://royal-8vd.pages.dev/")
#     page.get_by_role("link", name="Get in touch").click()
#     page.locator("#name").click()
#     page.locator("#name").fill("zoy")
#     page.locator("#email").click()
#     page.locator("#email").fill("smilie@gmail.com")
#     page.locator("#message").click()
#     page.locator("#message").fill("worked")
#     page.once("dialog", lambda dialog: dialog.dismiss())
#     page.get_by_role("button", name="Submit").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)



import requests
from faker import Faker

fake = Faker()

def generate_random_ip():
    return fake.ipv4()

def send_request(url, custom_ip=None):
    # Generate a random IP if one is not provided
    ip = custom_ip if custom_ip else generate_random_ip()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5',
        'X-Forwarded-For': ip
    }

    try:
        # Make the request to the specified URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        html = response.text
        print(f"Request successful. IP used: {ip}")
        
        # Additional processing can be done here on `html`
        if "#FAQ" in html:
            print("FAQ section found in the page HTML.")
        else:
            print("FAQ section not found in the page HTML.")

    except requests.exceptions.RequestException as e:
        print(f"Error requesting page: {url}")
        print(e)

# Run the request 50 times
url = "https://royal-8vd.pages.dev/"
for _ in range(50):
    send_request(url)
