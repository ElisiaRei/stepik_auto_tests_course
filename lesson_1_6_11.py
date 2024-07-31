from webdriver_manager.chrome import ChromeDriverManager
#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()

service = Service(executable_path=path)

#browser = webdriver.Chrome(service=service)

link = "https://suninjuly.github.io/registration2.html"


try:
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys("Elisa")
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys("Schepina")
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys("elisa@elisa.elisa")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    # Ваш код, который заполняет обязательные поля
    time.sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()