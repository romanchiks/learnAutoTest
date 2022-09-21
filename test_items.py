import time
import pytest
from selenium.webdriver.common.by import By


class TestProdictPage():

    def test_order_button(self, driver):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        driver.get(url)
        button_add_to_basket = driver.find_element(
            By.CSS_SELECTOR, 'button.btn-add-to-basket')
        assert bool(button_add_to_basket), 'Add to cart button not found'
