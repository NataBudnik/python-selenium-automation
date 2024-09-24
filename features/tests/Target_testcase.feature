# Created by smypboss at 9/24/24
Feature: Verify product name and image on Target search results page

  Scenario:User searches for a product and verify product name and image

    Given user on the Target homepage
    When user search  "Tea"
    Then each product in the search results should have a name
    And each product in the search results should have an image