import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    #ожидание до 5 секунд, пока искомый элемент не появится
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
class TestCorrectAnswer():

    def test_committed(self, browser, links):
        #вычисляемая переменная хранимая как строка
        answer = str(math.log(int(time.time())))
        #переменная, хранящая параметр
        link = links
        browser.get(link)
        input = browser.find_element_by_css_selector("textarea.ember-text-area.ember-view.textarea.string-quiz__textarea")
        input.send_keys(answer)

        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        time.sleep(2)
        #выводим комментарий системы
        msg = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))).text
        print(msg)
        #проверяем, что ответ "Correct!"
        commit = browser.find_element_by_css_selector("pre.smart-hints__hint")
        assert "Correct!" in commit.text
        
if __name__ == "__main__":
    pytest.main()
