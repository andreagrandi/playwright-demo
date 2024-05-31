from pytest_bdd import given, when, then, scenarios, parsers
from pages.pta_login_page import LoginPage
from pages.pta_successful_page import SuccessfulPage
from playwright.sync_api import Page

scenarios('../tests/pta_login.feature')

# Step definitions
@given("the user is on the login page")
def open_login_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()

@when(parsers.parse('the user enters username "{user}" and password "{password}"'))
def enter_valid_credentials(page: Page, user, password):
    login_page = LoginPage(page)
    login_page.enter_credentials(user, password)

@when('the user clicks the Submit button')
def click_login_button(page: Page):
    login_page = LoginPage(page)
    login_page.click_submit_btn()

@then('the user should be redirected to the login successful page')
def verify_dashboard_redirect(page: Page):
    successful_page = SuccessfulPage(page)
    successful_page.verify_successful_page_label()

@then('the user should see an error message')
def verify_error_message(page: Page):
    print("User can see an error message")
    login_page = LoginPage(page)
    login_page.verify_login_error()

@then("the user should see wrong username error message")
def verify_wrong_username_error(page: Page):
    login_page = LoginPage(page)
    login_page.verify_wrong_username_error()

@then("the user should see wrong password error message")
def verify_wrong_password_error(page: Page):
    login_page = LoginPage(page)
    login_page.verify_wrong_password_error()
