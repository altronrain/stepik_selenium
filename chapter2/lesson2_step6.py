import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/execute_script.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    answer_box = browser.find_element(By.ID, 'answer')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", answer_box
        )
    answer_box.send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn-primary.btn').click()
    time.sleep(30)
