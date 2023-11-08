import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementByXpath:

    def locate_by_xpath():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys('test@test.com')
        time.sleep(4)


findById = FindElementByXpath
findById.locate_by_xpath()
