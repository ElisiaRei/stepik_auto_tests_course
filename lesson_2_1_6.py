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
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"           #если чек не пустой(значит стоит), то прога продолжается, иначе выведется текст в кавычках                 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()