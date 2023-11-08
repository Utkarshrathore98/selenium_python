import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementById:

    def locate_by_id():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID, 'login-input').send_keys('test@test.com')
        time.sleep(4)

    def locate_by_name():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME, 'login-input').send_keys('test@test.com')
        time.sleep(4)


findById = FindElementById
findById.locate_by_id()
findById.locate_by_name()
