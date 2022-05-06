from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    val_1 = browser.find_element_by_id("num1")
    val_2 = browser.find_element_by_id("num2")
    sum = int(val_1.text) + int(val_2.text)
    
    # ищем элемент с текстом str(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))
    
    #нажимаем кнопку submit
    button = browser.find_element_by_css_selector("button[class='btn btn-default']")
    time.sleep(3)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()