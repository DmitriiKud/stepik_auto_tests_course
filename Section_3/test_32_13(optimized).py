from selenium import webdriver
import time
import unittest

try:
    browser = webdriver.Chrome()

    def link(url):

        browser.get(url)
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
        button.click()
        # ждем загрузки страицы
        time.sleep(2)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # возвращаем текст из элемента welcome_text_elt
        return welcome_text_elt.text
      
    # создаем класс TestText, который наследуется от unittest.TestCase и методы test_text1 и test_text2  проверяющий совпадение текста
    class TestText(unittest.TestCase):
        def test_text1(self):  
            url1 = "http://suninjuly.github.io/registration1.html"
            self.assertEqual(link(url1), "Congratulations! You have successfully registered!", "Register failure")
        
        def test_text2(self):
            url2 = "http://suninjuly.github.io/registration2.html"
            self.assertEqual(link(url2), "Congratulations! You have successfully registered!", "Register failure")

    # с помощью метода test_text проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    if __name__ == "__main__":
        unittest.main()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()