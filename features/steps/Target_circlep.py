from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target Circle page')
def open_circle_page(context):
    context.driver.get('https://target.com/circle')

#@when('Locate benefit section')
#def locate_benefit(context):
  #context.driver.find_element(By.XPATH, "//section[@data-test='benefits-section']")


@then ('Verify 10 benefit cells')
def verify_benefit_cells(context):
    context.driver.find_elements(By.XPATH, "//div[contains(@class, 'benefit')]")



sleep(2)