# Created by smypboss at 9/28/24
Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    Then Store original window
    And Click Privacy Policy Link
    Then Switch to new window
    And verify Privacy Policy page opened
    And Close current page
    And Return to original window