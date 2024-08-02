import unittest
from selenium import webdriver
# webdriver это и есть набор команд для управления браузером

from selenium.webdriver.common.by import By

class TestRegistration1(unittest.TestCase):
    def test_Registration1(self):
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input1.send_keys("Elisa")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input2.send_keys("Schepina")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input3.send_keys("elisa@elisa.elisa")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text)
        
    def test_Registration2(self):
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input1.send_keys("Elisa")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input2.send_keys("Schepina")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input3.send_keys("elisa@elisa.elisa")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text)
        
if __name__ == "__main__":
    unittest.main()