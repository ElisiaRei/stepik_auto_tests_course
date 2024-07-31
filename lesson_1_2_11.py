from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()

service = Service(executable_path=path)

browser = webdriver.Chrome(service=service)

link = "http://suninjuly.github.io/simple_form_find_task.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

