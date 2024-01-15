import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

with webdriver.Chrome() as browser:
    browser.get(link)
    # Ожидаем нужной цены
    time_to_buy = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    
    if time_to_buy:
        browser.find_element(By.ID, 'book').click()

    answer = calc(int(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.ID, 'solve').click()
    alert_text = browser.switch_to.alert.text
    print(alert_text.split(':')[-1].strip())