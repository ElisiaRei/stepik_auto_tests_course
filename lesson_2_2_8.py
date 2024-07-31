from selenium import webdriver
# webdriver это и есть набор команд для управления браузером

#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os 

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()    
    #открыть хром
    browser.get(link)
    #перейти по ссылке
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Elisa')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Rei')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('Elisa@gmail.elisa')
    #Вбиваем данные
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'elisa.txt')
    #определяем путь до файла
    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()  

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()











print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))