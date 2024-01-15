from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Тест упадёт с ошибкой, так как кнопка появляется \
на странице с задержкой в 1 секунду.
Метод .find_element() ищет элемент только один раз, получив от \
метода .get() информацию о том что страница загружена.
То что страница загружена, не означает что JavaScript закончил выполнение.
Какие-то элементы могут продолжать загружаться и в целом быть интерактивными.
"""

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text