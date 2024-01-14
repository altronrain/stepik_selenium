import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"

file = list(Path.cwd().glob('*.txt'))[0].resolve()
print(file)
with webdriver.Chrome() as browser:
    browser.get(link)

    # Заполнение обязательных полей
    browser.find_element(By.NAME, 'firstname').send_keys('Agent')
    browser.find_element(By.NAME, 'lastname').send_keys('007')
    browser.find_element(By.NAME, 'email').send_keys('some@email.com')
    # Загружаем файл
    file_choose = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    print(file)
    file_choose.send_keys(str(file))
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)