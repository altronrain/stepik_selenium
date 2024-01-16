import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestReg(unittest.TestCase):
    REG_LINK_1 = 'https://suninjuly.github.io/registration1.html'
    REG_LINK_2 = 'https://suninjuly.github.io/registration2.html'
    FIRSTNAME = 'Agent'
    LASTNAME = '007'
    EMAIL = 'some@email.com'
    
    def test_reg1(self):
        with webdriver.Chrome() as browser:
            browser.get(self.REG_LINK_1)
            browser.find_element(
                By.CSS_SELECTOR, 'input[required].first'
                ).send_keys(self.FIRSTNAME)
            browser.find_element(
                By.CSS_SELECTOR, 'input[required].second'
                ).send_keys(self.LASTNAME)
            browser.find_element(
                By.CSS_SELECTOR, 'input[required].third'
                ).send_keys(self.EMAIL)
            browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
            welcome_text_element = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.TAG_NAME, 'h1'))
            )
            welcome_text = welcome_text_element.text
            expected_text = 'Congratulations! You have successfully registered!'
            self.assertEqual(expected_text, welcome_text, \
                "Successful reg text expected!")


    def test_reg2(self):
        with webdriver.Chrome() as browser:
            browser.get(self.REG_LINK_2)
            browser.find_element(
                By.CSS_SELECTOR, 'input[required].first'
                ).send_keys(self.FIRSTNAME)
            browser.find_element(
                By.CSS_SELECTOR, 'input[required].second'
                ).send_keys(self.LASTNAME)
            browser.find_element(
                By.CSS_SELECTOR, 'input[required].third'
                ).send_keys(self.EMAIL)
            browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
            welcome_text_element = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.TAG_NAME, 'h1'))
            )
            welcome_text = welcome_text_element.text
            expected_text = 'Congratulations! You have successfully registered!'
            self.assertEqual(expected_text, welcome_text, \
                "Successful reg text expected!")

if __name__ == "__main__":    
    unittest.main()
            