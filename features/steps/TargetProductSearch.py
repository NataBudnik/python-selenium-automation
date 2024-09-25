
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@when('Search for a product {coffee}')
def search_product(context, coffee):
  wait = WebDriverWait(context.driver, 10)
  search_box = wait.until(EC.presence_of_element_located((By.ID, 'search')))
  search_box.send_keys(coffee)

  search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='@web/Search/SearchButton']")))
  search_button.click()


  #context.driver.find_element(By.ID, 'search').send_keys(coffee)
  #context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#sleep(4)



@then('Verify correct search results shown for {coffee}')
def verify_results(context, coffee):
  actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
  expected_result = coffee
  assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'

#sleep(4)