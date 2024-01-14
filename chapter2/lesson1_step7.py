import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/get_attribute.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn-default.btn').click()
    time.sleep(30)
