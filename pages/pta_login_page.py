from playwright.sync_api import Page

class LoginPage:
    # Capture the web elements
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_btn = page.locator("#submit")
        self.error_message = page.locator("#error")

    # Navigate to demo website
    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    # Type the credentials in login page
    def enter_credentials(self, user_name, password):
        self.username_input.fill(user_name)
        self.password_input.fill(password)

    # Click the login button
    def click_submit_btn(self):
        self.submit_btn.click()

    def verify_wrong_username_error(self):
        assert self.error_message.is_visible()
        assert self.error_message.text_content() == "Your username is invalid!"

    def verify_wrong_password_error(self):
        assert self.error_message.is_visible()
        assert self.error_message.text_content() == "Your password is invalid!"
