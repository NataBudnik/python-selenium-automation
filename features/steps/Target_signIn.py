from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('user on the Target main page')
def main(context):
 context.driver.get('https://www.target.com')

@when('user clicks on Sign in link')
def click_signin(context):
 context.app.header.click_sign_in()

#context.driver.find_element(By.XPATH,"//*[@id='headerPrimary']/a[4]/span").click()



@when('user clicks Sign in from right side navigation menu')
def navmenu(context):
 context.app.header.nav_sign_in_rside()

# context.driver.find_element(By.XPATH, "//*[@id='listaccountNav-signIn']/a/span").click()




@then('Sign in form opened')
def verify(context):
 context.app.sign_in_page.verify_signin_form()

# sign_in_form = context.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]')
 #assert sign_in_form.is_displayed(), f'"{sign_in_form.text}" is not displayed'

 context.driver.quit()