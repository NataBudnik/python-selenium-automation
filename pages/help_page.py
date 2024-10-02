from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class HelpPage (Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self):
        dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(dd)
        select.select_by_value('Promotions & Coupons')

    def verify_returns_opened(self):
          self.wait_for_element_to_appear(*self.HEADER_RETURNS)

    def verify_promotions_opened(self):
        self.wait_for_element_to_appear(*self.HEADER_PROMOTIONS)