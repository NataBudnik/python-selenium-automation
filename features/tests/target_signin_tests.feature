# Created by smypboss at 9/29/24
Feature: Tests for Target Sign In page

  Scenario: User can open and close Terms and Conditions from sign in page

    Given Open Target "sign in" page
 When Store original window
 And Click on Target terms and conditions link
 And Switch to the newly opened window
 Then Verify Terms and Conditions page is opened
 And User can close new window and switch back to original
