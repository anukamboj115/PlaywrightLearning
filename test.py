from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #page.pause()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("mon.storozhenko@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.pause()
    page.get_by_test_id("handle-button").click()
    page.get_by_role("menuitem", name="My Orders").click()
    page.locator("iframe[title=\"My Orders\"]").content_frame.get_by_role("heading", name="My Orders").click()
    expect(page.locator("iframe[title=\"My Orders\"]").content_frame.get_by_role("heading",name="You haven't placed any orders")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
