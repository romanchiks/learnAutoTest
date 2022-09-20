from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math
import os

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.CSS_SELECTOR, '#book')
    button.click()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = str(math.log(abs(12 * math.sin(int(x)))))
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(answer)

    submit_button = browser.find_element(
        By.XPATH, '//button[text()="Submit"]')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
