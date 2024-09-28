from selenium.webdriver.common.by import By

from pages.base_page import Page


class AddingToCartPage:

    SEARCH_BOX = (By.ID, "search")
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product-card")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart-button")
    CART_ICON = (By.CSS_SELECTOR, ".cart-icon span")

    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, product_name):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(product_name + "\n")

    def add_first_product_to_cart(self):
        self.driver.find_element(*self.PRODUCT_CARD).click()
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()

    def get_cart_item_count(self):
        return self.driver.find_element(*self.CART_ICON).text