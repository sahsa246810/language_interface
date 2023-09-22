import time
from selenium.webdriver.common.by import By
def test_items(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(3)
    basket = None
    basket = browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert basket is not None, 'element not found'
