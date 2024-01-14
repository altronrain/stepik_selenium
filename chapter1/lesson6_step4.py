import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# person_data = {
#     'first_name': 'Ivan',
#     'last_name': 'Petrov',
#     'city': 'Smolensk',
#     'country': 'Russia'
# }

# def fill_form(browser_instance, person_data):
#     input1 = browser_instance.find_element(By.TAG_NAME, 'input')
#     input1.send_keys(first_name)
#     input2 = browser_instance.find_element(By.NAME, 'last_name')
#     input2.send_keys(last_name)
#     input3 = browser_instance.find_element(By.CLASS_NAME, 'city')
#     input3.send_keys(city)
#     input4 = browser_instance.find_element(By.ID, 'country')
#     input4.send_keys(country)
#     button = browser_instance.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()    

def fill_form(browser_instance, person_data):
    for selector, data in person_data.items():
        input = browser_instance.find_element(By.CSS_SELECTOR, selector)
        input.send_keys(data)


if __name__ == '__main__':
    link = 'http://suninjuly.github.io/simple_form_find_task.html'
    person_data = {
        '[name="first_name"]': 'Ivan',
        '[name="last_name"]': 'Petrov',
        '.city': 'Smolensk',
        '#country': 'Russia'
    }
    
    with webdriver.Chrome() as browser:
        browser.get(link)
        fill_form(browser, person_data)
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        time.sleep(30)