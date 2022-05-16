from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link_1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    link_1.send_keys('Pavel')
    link_2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    link_2.send_keys('Levap')
    link_3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    link_3.send_keys('stepik@mail.com')
    link_4 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone:']")
    link_4.send_keys('00000000')
    link_5 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address:']")
    link_5.send_keys('Ukraine')
    button = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']")
    button.click()

finally:
    time.sleep(2)
    browser.quit()