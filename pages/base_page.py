class Page:

    def __init__(self, driver):
        self.driver = driver

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

    def verify_url(self, expected_url):
     current_url = self.driver.current_url
     assert current_url == expected_url, f'Expected URL{expected_url} but got {current_url}'

    def verify_partial_url(self, expected_partial_url):
     current_url = self.driver.current_url
     assert expected_partial_url in current_url,  f'Expected partial URL{expected_partial_url} not in {current_url}'