from pages.product_page import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver
import time


def test_guest_can_add_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_name()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_in_success_message()
    page.should_be_cart_price_equal_to_product_price()
