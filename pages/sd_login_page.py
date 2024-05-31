from playwright.sync_api import Page

class LoginPage:
    # Capture the web elements
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.error_message = page.locator(".error-button")

    # Navigate to demo website
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/v1/")

    # Type the credentials in login page
    def enter_credentials(self, user_name, password):
        self.username_input.fill(user_name)
        self.password_input.fill(password)

    # Click the login button
    def click_login_btn(self):
        self.login_btn.click()

    # Verify the login error message if it occurs
    def verify_login_error(self):
        assert self.error_message.is_visible()
