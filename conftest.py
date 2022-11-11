import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options  as OptionsFirefox

import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)
    if browser_name == "chrome":
        print("\nstart browser chrome for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart browser firefox for test...")
        options_firefox = OptionsFirefox()
        options_firefox.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe',options=options_firefox)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser...")
    time.sleep(10)
    browser.quit()