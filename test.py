import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:5500/button.html")
    page.get_by_role("button", name="Click Me").click()
    page.get_by_role("button", name="Click Me").click()
    page.goto("https://www.w3schools.com/")
    page.get_by_role("link", name="PHP", exact=True).click()
    page.goto("https://www.w3schools.com/")
    page.locator("#pagetop").get_by_label("Login to your account").click()
    page.get_by_placeholder("email").click()
    page.get_by_placeholder("email").fill("royalalawode@gmail.com")
    page.get_by_placeholder("password").click()
    page.get_by_placeholder("password").fill("Codercaptainroy17$")
    page.get_by_role("button", name="Login").click()
    page.locator("#pagetop").get_by_label("Your W3Schools Profile", exact=True).click()
    page.get_by_label("avatar").first.click()
    # this is for failed attemppt -------
    page.wait_for_load_state("networkidle")
    # this is for failed attemppt -------
    page.get_by_placeholder("Add your last name").click()
    page.get_by_placeholder("Add your last name").fill("miyor")
    page.locator("#account-section").get_by_role("button", name="Save").click()
    page.goto("https://pathfinder.w3schools.com/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
