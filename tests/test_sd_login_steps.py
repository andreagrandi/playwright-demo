from pytest_bdd import given, when, then, scenarios, parsers
from pages.sd_login_page import LoginPage
from pages.sd_product_page import ProductPage
from playwright.sync_api import Page

scenarios('../tests/sd_login.feature')

# Step definitions
@given("the user is on the login page")
def open_login_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()

@when(parsers.parse('the user enters username "{user}" and password "{password}"'))
def enter_valid_credentials(page: Page, user, password):
    login_page = LoginPage(page)
    login_page.enter_credentials(user, password)

@when('the user clicks the Login button')
def click_login_button(page: Page):
    login_page = LoginPage(page)
    login_page.click_login_btn()

@then('the user should be redirected to the product page')
def verify_dashboard_redirect(page: Page):
    product_page = ProductPage(page)
    product_page.verify_product_page_label()

@then('the user should see an error message')
def verify_error_message(page: Page):
    print("User can see an error message")
    login_page = LoginPage(page)
    login_page.verify_login_error()
