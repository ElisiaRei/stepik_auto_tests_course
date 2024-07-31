from selenium import webdriver
# webdriver это и есть набор команд для управления браузером

from webdriver_manager.chrome import ChromeDriverManager
#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
import math


path = ChromeDriverManager().install()

service = Service(executable_path=path)

#browser = webdriver.Chrome(service=service)

link = "https://suninjuly.github.io/selects1.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=service)
    browser.get(link)                                                       #Открыть страницу https://suninjuly.github.io/math.html.

    sum = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)  #Посчитать сумму заданных чисел
    #print(sum)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))                                        # ищем элемент с текстом "Python"
    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()                                                          #Нажать на кнопку Submit.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()