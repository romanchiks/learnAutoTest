import time
from selenium.webdriver.common.by import By


def test_button_add_basket(driver):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    driver.get(url)

    assert driver.find_element(
        By.CSS_SELECTOR, 'button.btn-add-to-basket'), 'Add to cart button not found'
