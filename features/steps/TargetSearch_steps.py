from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



@given('user on the Target page')
def open_main(context):
    context.driver.get('https://www.target.com')


@when('user clicks on the Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//*[@id='headerPrimary']/a[5]").click()


@then('user can see message "Your cart is empty"')
def see_message(context):
    context.driver.find_element(By.XPATH, '//*[contains(text(), "Your cart is empty")]')

