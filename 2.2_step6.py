from selenium import webdriver
import time
import math

link = " http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #функция, которая рассчитывает значение
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    #находим значение X с помощью get_attribute и рассчитываем
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    #скролл страницу вниз с помощью js и вставляем значение
    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)
    #кликаем checkbox
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    #выбираем радиокнопку
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    #нажимаем кнопку submit
    button = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    time.sleep(1)
    button.click()
       
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()