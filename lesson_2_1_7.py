from selenium import webdriver
# webdriver это и есть набор команд для управления браузером

#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math


link = "https://suninjuly.github.io/get_attribute.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)                                                       #Открыть страницу https://suninjuly.github.io/math.html.

    x_element = browser.find_element(By.ID, "treasure")  
    x = x_element.get_attribute("valuex")                                   #Считать значение для переменной x.
    print(x)
    y = calc(x)                                                             #Посчитать математическую функцию от x
    input_fields = browser.find_element(By.ID, "answer")
    input_fields.send_keys(y)                                               #Ввести ответ в текстовое поле.
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()                                                        #Отметить checkbox "I'm the robot"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()                                                     #Выбрать radiobutton "Robots rule!".
    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()                                                          #Нажать на кнопку Submit.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()