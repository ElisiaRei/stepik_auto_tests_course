from selenium import webdriver
# webdriver это и есть набор команд для управления браузером

from webdriver_manager.chrome import ChromeDriverManager
#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
path = ChromeDriverManager().install()

service = Service(executable_path=path)

#browser = webdriver.Chrome(service=service)

link = "https://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome(service=service)
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()