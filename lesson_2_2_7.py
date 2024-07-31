from selenium import webdriver
# webdriver это и есть набор команд для управления браузером

#необходимо установить webdriver_manager по совету из коментария к уроку 1.2 https://stepik.org/lesson/25969/step/7?discussion=4481246&unit=196192
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os 


print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))