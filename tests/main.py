from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time
import math
import os


class Test_link():

    @pytest.mark.parametrize(
        'lesson_number',
        [i for i in range(236895, 236906) if (
            i > 236894 and i < 236900) or (i > 236902 and i < 236906)])
    def test_link(self, driver, lesson_number):
        link = f'https://stepik.org/lesson/{lesson_number}/step/1/'
        driver.get(link)
        textarea = driver.find_element(
            By.CSS_SELECTOR, 'textarea.string-quiz__textarea')
        textarea.send_keys(str(math.log(int(time.time()))))
        submit_button = driver.find_element(
            By.CSS_SELECTOR, 'button.submit-submission')
        submit_button.click()
        result = driver.find_element(
            By.CSS_SELECTOR, '.smart-hints__hint').text

        assert result == "Correct!", f'result "{result}" does not match "Correct!"'
