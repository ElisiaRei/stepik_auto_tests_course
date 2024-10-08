from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
#import math
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()

service = Service(executable_path=path)

#browser = webdriver.Chrome(service=service)

#link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("a")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла