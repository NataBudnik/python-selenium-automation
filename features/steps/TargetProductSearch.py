from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for a product {product_name}')
def search_product(context, product_name):
  context.driver.find_element(By.ID, 'search').send_keys(product_name)
  context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(4)


@then('Verify that correct search results shown for {product_name}')
def verify_results(context, product_name):
  actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
  expected_result = product_name
  assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'

sleep(4)