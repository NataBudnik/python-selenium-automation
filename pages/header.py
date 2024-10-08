from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SIGN_IN_BTN = (By.XPATH,"//*[@id='headerPrimary']/a[4]/span")
    SIGN_IN_RSIDE =(By.XPATH, "//*[@id='listaccountNav-signIn']/a/span")



    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.click(*self.CART_BTN)





    def click_sign_in(self):
            self.click(*self.SIGN_IN_BTN)

    def nav_sign_in_rside(self):
     self.click(*self.SIGN_IN_RSIDE)
