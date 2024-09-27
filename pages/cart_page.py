from selenium.webdriver.common.by import By


from pages.base_page import Page



class CartPage(Page):

    CART_EMPTY_TXT = (By.XPATH, '//*[@id="cart-container"]/div[1]/div/div/div[2]/h1')

    def verify_cart_empty(self):
     expected_text = "Your cart is empty"
     actual_text = self.driver.find_element(*self.CART_EMPTY_TXT).text
     assert expected_text == actual_text, f'Expected{expected_text} did not match Actual{actual_text}'