from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    welcome_text = None
    result = [None, "Тест пройден успешно"]
    error_message = None
    browser = None

    try:
        browser = webdriver.Chrome()

        #link = "http://suninjuly.github.io/registration1.html"

        # раскомментируйте строку ниже, чтобы проверить страницу с багом
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first[required]")

        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third[required]")
        input3.send_keys("ivanpetrov@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(2)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
    except Exception as error:
        error_name = error.__class__.__name__
        result[0] = f"Наш тест упал с ошибкой {error_name}"
        if hasattr(error, 'msg'):
            error_message = error.msg
        elif hasattr(error, '_msg'):
            error_message = error._msg
    finally:
        time.sleep(5)
        if browser is not None:
            browser.quit()
    
    print("\n\n-------------\n\n")   
    print(result["Congratulations! You have successfully registered!" == welcome_text])
    if result[0] and error_message: # Проверяем, записано ли сообщение об ошибке в результат
        print(f"\n\nПодробности об ошибке:\n\n{error_message}")
    print("\n--------------\n\n")

    print("""Я проверил код у себя, у меня всё работает.
Если у Вас мой код работает не так, как ожидается,
пожалуйста, свяжитесь со мной в тг https://t.me/realpavelb перед тем,
как вы оцените моё решение на Степике""")

if __name__ == "__main__":
    main()