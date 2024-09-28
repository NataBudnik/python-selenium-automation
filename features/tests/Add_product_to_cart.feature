# Created by smypboss at 9/27/24
Feature: Add product to cart

  Scenario:Add product to cart

    Given user on the homepage Target
    When user search "sofa"
    And user add first product to the cart
    Then verify cart show "1 item"
