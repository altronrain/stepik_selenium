import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 10 link:
# link = "http://suninjuly.github.io/registration1.html"
# Step 11 link:
link = "https://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, 'input[required].first').send_keys('Agent')
    browser.find_element(By.CSS_SELECTOR, 'input[required].second').send_keys('007')
    browser.find_element(By.CSS_SELECTOR, 'input[required].third').send_keys('some@email.com')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # True:
    assert "Congratulations! You have successfully registered!" == welcome_text
    # False:
    # assert "Definitely not required text" == welcome_text