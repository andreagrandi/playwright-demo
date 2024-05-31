from playwright.async_api import Page

class ProductPage:
    # Capture the required elements
    def __init__(self, page: Page):
        self.page = page
        self.product_page_label = page.inner_text(".product_label")

    # Verify the Product page label
    def verify_product_page_label(self):
        assert self.product_page_label == "Products"
