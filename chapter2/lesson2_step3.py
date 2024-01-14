import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'
# link = 'https://suninjuly.github.io/selects2.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    x = int(browser.find_element(By.ID, 'num1').text)
    y = int(browser.find_element(By.ID, 'num2').text)
    z = str(x + y)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(z)
    browser.find_element(By.CSS_SELECTOR, '.btn-default.btn').click()
    time.sleep(30)
