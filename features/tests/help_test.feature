# Created by smypboss at 10/1/24
Feature: Test for help page
  Scenario: User can select Help topic Promotion & Coupon
    Given Open help page for return
    Then Verify help Return page opened
    When Select Help topic Promotion & Coupons
    Then Verify help Current promotion page opened