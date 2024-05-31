from playwright.async_api import Page

class SuccessfulPage:
    # Capture the required elements
    def __init__(self, page: Page):
        self.page = page
        self.logout_button = page.get_by_text("Log out")

    # Verify the Successful page label
    def verify_successful_page_label(self):
        assert self.logout_button.is_visible()
