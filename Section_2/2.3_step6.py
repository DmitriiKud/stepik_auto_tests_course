from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #нажимаем кнопку submit
    button = browser.find_element_by_css_selector("button[class='trollface btn btn-primary']")
    time.sleep(1)
    button.click()
    
    #переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
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
    
    #нажимаем кнопку submit второй раз
    button = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    time.sleep(1)
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()