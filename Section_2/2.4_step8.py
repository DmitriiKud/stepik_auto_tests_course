from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #нажимаем кнопку Book с условием
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    button.click()
    
    #функция, которая рассчитывает значение
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    #находим значение X с помощью get_attribute и рассчитываем
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # вставляем значение
    input = browser.find_element_by_id("answer")
    time.sleep(1)
    input.send_keys(y)
    
    #нажимаем кнопку submit но в этот раз по id, так как у нее одинаковый класс с Book
    button = browser.find_element_by_id("solve")
    time.sleep(1)
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()