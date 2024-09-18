# Created by smypboss at 9/16/24

Feature: "target.com" Sign in Functionality
  Scenario: Verify that logged out user can navigate to Sign in

    Given user on the Target main page
    When user clicks on Sign in link
    And user clicks Sign in from right side navigation menu
    Then Sign in form opened