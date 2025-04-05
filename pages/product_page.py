from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_add_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_product_added_to_basket(self):
        self.should_be_message_with_product_in_basket()
        self.should_be_correct_product_added_to_basket()
        self.should_be_message_with_cost_of_basket()
        self.should_be_correct_cost_in_message_with_cost_of_basket()

    def should_be_message_with_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), "Не найдено сообщение о добавлении товара в корзину"

    def should_be_correct_product_added_to_basket(self):
        text1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        text2 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert text1 == text2, f"Не тот продукт в корзине, {text1} != {text2}"

    def should_be_message_with_cost_of_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_MESSAGE), "Не найдено сообщение о цене корзины"

    def should_be_correct_cost_in_message_with_cost_of_basket(self):
        text1 = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        text2 = self.browser.find_element(*ProductPageLocators.BASKET_COST_MESSAGE).text
        assert text1 == text2, f"Не та стоимость корзины, {text1} != {text2}"

