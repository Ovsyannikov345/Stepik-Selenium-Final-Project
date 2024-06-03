from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, searchType, searchParameter):
        try:
            self.browser.find_element(searchType, searchParameter)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, searchType, searchParameter, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((searchType, searchParameter))
            )
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, searchType, searchParameter, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((searchType, searchParameter))
            )
        except TimeoutException:
            return False

        return True
