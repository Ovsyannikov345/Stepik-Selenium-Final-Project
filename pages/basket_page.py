from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM
        ), "Should not be any basket items"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_TEXT
        ), "Should present empty basket text"
