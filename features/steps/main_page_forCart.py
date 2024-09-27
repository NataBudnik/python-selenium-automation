from selenium.webdriver.common.by import By
from behave import given, when, then



@given('user on a target page')
def open_main(context):
    context.app.main_page.open_main()


@when('user click on cart icon')
def click_cart(context):
    context.app.header.click_cart()



@then('Verify "You cart is empty" message shown')
def verify_cart_empty(context):
  context.app.cart_page.verify_cart_empty()