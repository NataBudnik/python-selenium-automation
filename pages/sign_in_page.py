from selenium.webdriver.common.by import By

from pages.base_page import Page



class SignInPage(Page):

    #SIGN_IN_OPENED = (By.XPATH, '//a[text()="Sign in"]')

    TERM_LINK = (By.LINK_TEXT, '//*[@id="__next"]/div/div/div/div[1]/div/div[6]/a')


    def open_target_signin(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    #def verify_signin_form(self):
    # expected_text = "Sign in form opened"
     #actual_text = self.driver.find_element(*self.SIGN_IN_OPENED).text
     #assert expected_text == actual_text, f' Expected {expected_text} did not match Actual{actual_text}'



    def click_term_link(self):
         self.wait_to_be_clickable_click(*self.TERM_LINK)

    def verify_term_link_opened(self):
        self.verify_partial_url('target-terms-and-conditions')
