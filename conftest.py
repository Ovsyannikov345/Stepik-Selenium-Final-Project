import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        help="Choose language: en/es/fr/ru",
        default="en",
        choices=("en", "es", "fr", "ru"),
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language not in ["en", "es", "fr", "ru"]:
        raise pytest.UsageError("--language should be en/es/fr/ru")

    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test..(lang={language})")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test..(lang={language})")
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()