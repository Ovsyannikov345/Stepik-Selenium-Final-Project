from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ITEM_ADDED_MESSAGE
        ), "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_be_product_name(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME
        ), "Product name is not present"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART_BUTTON
        ), "Add to cart button is not present"

    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_text = self.browser.find_element(
            *ProductPageLocators.ITEM_ADDED_MESSAGE
        ).text
        assert (
            product_name == message_text
        ), "Success mesasge text doesn't contain product name"

    def should_be_cart_price_equal_to_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert (
            product_price in cart_price
        ), f"Expected cart price to be {product_price} but got {cart_price}"
