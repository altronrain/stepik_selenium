import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

with webdriver.Chrome() as browser:
    browser.get(link)
    # current_window = browser.current_window_handle
    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    # new_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])

    answer = calc(int(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, '.btn-primary.btn').click()
    alert_text = browser.switch_to.alert.text
    print(alert_text.split(':')[-1].strip())