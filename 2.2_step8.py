import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Заполнено")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Заполнено")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Заполнено")
    time.sleep(1)
    
    # Вставляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    
    #нажимаем кнопку submit
    button = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    time.sleep(1)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()