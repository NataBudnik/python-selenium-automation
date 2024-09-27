# Created by smypboss at 9/24/24
Feature: Test for Target Search functionality

  Scenario:User can search for coffee

  Given Open target main page
    When Search for tea
    Then Verify that correct search results shown for tea

  Scenario Outline: User can search for product
    Given Open target main page
    When Search for <search_word>
    Then Verify that correct search results shown for <search_result>
    Examples:
    |search_word  |search_result |
    |coffee       |coffee        |
    |tea          |tea           |
    |mug          |mug           |
    |sugar        |sugar         |





