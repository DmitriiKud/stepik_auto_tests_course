from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link1 = "http://suninjuly.github.io/registration1.html" #должна пройти
    link2 = "http://suninjuly.github.io/registration2.html" # должна упасть
    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".form-control.first[required]")
    input1.send_keys("Заполнено")
    input2 = browser.find_element_by_css_selector(".form-control.second[required]")
    input2.send_keys("Заполнено")
    input3 = browser.find_element_by_css_selector(".form-control.third[required]")
    input3.send_keys("Заполнено")
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    time.sleep(1)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()