import pytest
import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart(browser):
    browser.get(link)
    time.sleep(10) #для проверки других языков цензорами - не стал делать 30 сек
    add_to_basket = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert add_to_basket,  'Button is not found on the page'
