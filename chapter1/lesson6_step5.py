import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from lesson6_step4 import fill_form

starter_link='https://suninjuly.github.io/find_link_text'
form_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
person_data = {
    '[name="first_name"]': 'Ivan',
    '[name="last_name"]': 'Petrov',
    '.city': 'Smolensk',
    '#country': 'Russia'
}

with webdriver.Chrome() as browser:
    browser.get(starter_link)
    button = browser.find_element(By.LINK_TEXT, form_link)
    button.click()
    fill_form(browser, person_data)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(30)