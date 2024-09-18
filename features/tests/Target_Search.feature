# Created by smypboss at 9/16/24


Feature: "Target.com" cart functionality
  Scenario: verify "your cart is empty" message is shown

    Given user on the Target page
    When user clicks on the Cart icon
    Then user can see message "Your cart is empty"
