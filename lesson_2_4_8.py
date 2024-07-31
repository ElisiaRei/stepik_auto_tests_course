from selenium import webdriver
# webdriver это и есть набор команд для управления браузером

#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os 

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()    

    browser.get(link)

      # говорим Selenium проверять в течение 20 секунд, пока цена не станет 100
    price = WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button = browser.find_element(By.ID, "book")
    button.click()


    x = int(browser.find_element(By.ID, "input_value").text)             #найти Х
    y = calc(x)    
    input_fields = browser.find_element(By.ID, "answer")
    input_fields.send_keys(y) 
    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()

    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()











print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))