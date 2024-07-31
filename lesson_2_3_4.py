from selenium import webdriver
# webdriver это и есть набор команд для управления браузером

#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os 

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()    
    #открыть хром
    browser.get(link)
    #перейти по ссылке
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()  
    #находим кнопку и щелкаем по ней
    alert = browser.switch_to.alert
    #переключаемся на алерт
    alert.accept()
    #принимаем алерт
    x = int(browser.find_element(By.ID, "input_value").text)             #найти Х
    y = calc(x)    
    input_fields = browser.find_element(By.ID, "answer")
    input_fields.send_keys(y) 
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()











print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))