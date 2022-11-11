from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_basket(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "[type=\'submit\']")
    assert button ,"---- Add to busket button is not found ----"

