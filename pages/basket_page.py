from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_see_empty_basket_message(self):
        self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)

