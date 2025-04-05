from selenium.webdriver.common.by import By
class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")
