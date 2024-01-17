import os
import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = os.environ['EMAIL_ADDRESS']
password = os.environ['STEPIK_PASS'] 

@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestStepik3_6_5():
    
    @pytest.mark.parametrize('link', [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
    ]
                             )
    def test_links_stepik(self, browser, link):
        browser.get(link)
        WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.ID, 'ember35'))
        )
        login_button = browser.find_element(By.ID, 'ember35')
        login_button.click()
        login_form = browser.find_element(By.CLASS_NAME, 'modal-dialog-inner')
        browser.find_element(By.NAME, 'login').send_keys(email)
        browser.find_element(By.NAME, 'password').send_keys(password)
        browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        """
        Просто использование ожидания element_located в случае сайта Stepik
        не сработало по причине того, что после закрытия login-формы сайт еще
        перезагружается с нуля, при этом до перезагрузки форма успевает
        заполниться. потом она очищается
        """
        WebDriverWait(browser, 10).until(
            EC.staleness_of(login_form)
        )
        text_area = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'textarea[required]')
            )
        )
        text_area.send_keys(math.log(int(time.time())))
        submit = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button.submit-submission')
            )
        )
        submit.click()
        hint_box = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        )
        hint_text = hint_box.text
        assert hint_text == 'Correct!', f'По ссылке {link=} оставлено сообщение {hint_text=}'
        