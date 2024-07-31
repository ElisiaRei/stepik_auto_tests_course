from webdriver_manager.chrome import ChromeDriverManager
#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
import time
import math
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()

service = Service(executable_path=path)

#browser = webdriver.Chrome(service=service)

link = "https://suninjuly.github.io/math.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=service)
    browser.get(link)                                                       #Открыть страницу https://suninjuly.github.io/math.html.

    x_element = browser.find_element(By.ID, "input_value")  
    x = x_element.text                                                      #Считать значение для переменной x.
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