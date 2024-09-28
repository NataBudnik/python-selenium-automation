from selenium.webdriver.common.by import By


from pages.base_page import Page



class SignInPage(Page):

    SIGN_IN_OPENED = (By.XPATH, '//*[@id="__next"]/div/div/div/div[1]')

    def verify_signin_form(self):
     expected_text = "Sign in form opened"
     actual_text = self.driver.find_element(*self.SIGN_IN_OPENED).text
     assert expected_text == actual_text, f' Expected {expected_text} did not match Actual{actual_text}'