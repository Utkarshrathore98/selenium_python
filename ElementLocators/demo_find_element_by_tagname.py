import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementByTagName:

    def locate_by_tag_name():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.TAG_NAME, "input").send_keys("test@test.com")
        time.sleep(4)

    def locate_by_class_name():
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys('test@test.com')
        time.sleep(4)


findByTagName = FindElementByTagName
findByTagName.locate_by_class_name()
