Feature: User Login

Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters username "student" and password "Password123"
    And the user clicks the Submit button
    Then the user should be redirected to the login successful page

Scenario: Login with invalid username
    Given the user is on the login page
    When the user enters username "InvalidUser" and password "Password123"
    And the user clicks the Submit button
    Then the user should see wrong username error message

Scenario: Login with invalid password
    Given the user is on the login page
    When the user enters username "student" and password "WrongPassword"
    And the user clicks the Submit button
    Then the user should see wrong password error message
