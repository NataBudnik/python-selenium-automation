
from behave import given, when, then
from selenium import webdriver
#from adding_to_cart_page import AddingToCartPage


@given('user on the homepage Target')
def on_homepage(context):
 context.driver = webdriver.Chrome()
 context.driver.get("https://www.target.com")
 #context.page = AddingToCartPage(context.driver)

@when('user search "{product}"')
def search_for_product(context, product):
 context.page.search_for_product(product)

@when('user add first product to the cart')
def add_to_cart(context):
 context.page.add_first_product_to_cart()

@then('verify cart show "{item_count}item"')
def cart_displays_product_count(context, item_count):
 assert context.page.get_cart_item() == item_count
 context.driver.quit()