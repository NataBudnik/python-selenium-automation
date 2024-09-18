from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('user on the Target main page')
def main(context):
 context.driver.get('https://www.target.com')

@when('user clicks on Sign in link')
def click_signin(context):
 context.driver.find_element(By.XPATH,"//*[@id='headerPrimary']/a[4]/span").click()


@when('user clicks Sign in from right side navigation menu')
def navmenu(context):
 context.driver.find_element(By.XPATH, "//*[@id='listaccountNav-signIn']/a/span").click()


@then('Sign in form opened')
def verify(context):
 context.driver.find_element(By.ID, 'signInFormId')

 context.driver.quit()