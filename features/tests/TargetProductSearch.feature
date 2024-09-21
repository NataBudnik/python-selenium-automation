# Created by smypboss at 9/18/24
Feature: Test Target search functionality
  Scenario:User can search a product

    Given Open Target main page
    When Search for a product
    Then Verify that correct search results shown



    Scenario: Search for coffee

    Given Open target main page
    When Search for a product coffee
    Then Verify that correct search results shown for coffee


