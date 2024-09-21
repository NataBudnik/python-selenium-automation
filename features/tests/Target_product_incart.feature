# Created by smypboss at 9/20/24
Feature: Add product in cart and verify
  Scenario: add product into the cart and check the product is there

    Given Open Target page
    When Search a product juice
    And Select the first product form the search results
    And Add product to the cart
    Then Verify that product is in the cart