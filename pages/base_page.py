
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)




    def wait_to_be_clickable(self, *locator):
     self.wait.until(EC.element_to_be_clickable(locator), message=f'Element by {locator} is not clickable')


    def wait_to_be_clickable_click(self, *locator):
     self.wait.until(EC.element_to_be_clickable(locator), message=f'Element by {locator} is not clickable').click()


    def verify_url(self, expected_url):
     current_url = self.driver.current_url
     assert current_url == expected_url, f'Expected URL{expected_url} but got {current_url}'

    def verify_partial_url(self, expected_partial_url):
     current_url = self.driver.current_url
     assert expected_partial_url in current_url,  f'Expected partial URL{expected_partial_url} not in {current_url}'