from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login") != -1, "Неверный URL для страницы входа"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Не найдена форма входа"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Не найдена форма регистрации"

    def register_new_user(self, email, password):
        self.input_data(*LoginPageLocators.REGISTER_EMAIL, email)
        self.input_data(*LoginPageLocators.REGISTER_PASSWD1, password)
        self.input_data(*LoginPageLocators.REGISTER_PASSWD2, password)
        self.interact(*LoginPageLocators.REGISTER_BUTTON)

