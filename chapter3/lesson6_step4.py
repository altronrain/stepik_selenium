import os
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://stepik.org/lesson/236895/step/1'
email = os.environ['EMAIL_ADDRESS']
password = os.environ['STEPIK_PASS']

with webdriver.Chrome() as browser:
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'ember35'))
    )
    login_button = browser.find_element(By.ID, 'ember35')
    login_button.click()
    login_form = browser.find_element(By.CLASS_NAME, 'modal-dialog-inner')
    browser.find_element(By.NAME, 'login').send_keys(email)
    browser.find_element(By.NAME, 'password').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    # WebDriverWait(browser, 2).until(
    #     EC.staleness_of(login_form)
    # )
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
    )
    text_area = browser.find_element(By.TAG_NAME, 'textarea')
    answer = math.log(int(time.time()))
    text_area.send_keys(answer)
    submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
    submit.click()
    hint_text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    try:
        assert hint_text == 'Correct!'
    except AssertionError:
        print(f'По ссылке {link=} оставлено сообщение {hint_text=}')
