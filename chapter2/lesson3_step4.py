import math
from selenium import webdriver
from selenium.webdriver.common.by import By

# CHROME_USER_CONFIG = '/home/altron/.config/google-chrome/'

link = 'https://suninjuly.github.io/alert_accept.html'
# course_task_link = 'https://stepik.org/lesson/184253/step/4'

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

# def send_to_stepik(course_task_link, step_answer):
#     options = Options()
#     # chrome_options.binary_location = SYSTEM_CHROME
#     options.add_argument(f"--user-data-dir={CHROME_USER_CONFIG}")
#     options.add_argument('--no-sandbox')
#     with webdriver.Chrome(options=options) as browser:
#         browser.get(course_task_link)
#         time.sleep(5)
#         answer_box = browser.find_element(By.CSS_SELECTOR, 'textarea[required]')
#         answer_box.send_keys(step_answer)
#         submit_button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
#         submit_button.click()

with webdriver.Chrome() as browser:
    browser.get(link)
    # Нажатие на кнопку
    browser.find_element(By.CSS_SELECTOR, '.btn-primary.btn').click()
    # Принятие alert'а
    browser.switch_to.alert.accept()

    # Чтение X со страницы и рассчет ответа
    answer = calc(int(browser.find_element(By.ID, 'input_value').text))
    # Запись ответа
    browser.find_element(By.ID, 'answer').send_keys(answer)
    # Нажатие на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, '.btn-primary.btn').click()
    # Запрос текста из alert'а с ответом на задание
    alert_text = browser.switch_to.alert.text
    print(alert_text.split(':')[-1].strip())
    
# Сдача задания
# send_to_stepik(course_task_link, step_answer)