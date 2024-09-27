# Created by smypboss at 9/26/24
Feature: Cart functionality
  Scenario: "You cart is empty" message is shown

    Given user on a target page
     When  user click on cart icon
     Then  Verify "You cart is empty" message shown