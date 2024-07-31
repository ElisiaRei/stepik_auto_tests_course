from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()

service = Service(executable_path=path)

#browser = webdriver.Chrome(service=service)

link = "https://suninjuly.github.io/find_xpath_form"


try:
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Elisa")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Schepina")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Saint-Peterburg")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла