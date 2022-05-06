from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #функция, которая рассчитывает значение
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    #находим значение X с помощью get_attribute и рассчитываем
    x_element = browser.find_element_by_id("treasure")
    x_attribute = x_element.get_attribute("valuex")
    x = x_attribute
    y = calc(x)
    #вставляем значение
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    #кликаем checkbox
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    #выбираем радиокнопку
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    #нажимаем кнопку submit
    button = browser.find_element_by_css_selector("button[class='btn btn-default']")
    time.sleep(3)
    button.click()
       
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()