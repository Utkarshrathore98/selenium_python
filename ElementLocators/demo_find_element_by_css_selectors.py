import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementByCssSelector:

    def locate_by_css_selector(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys('test@test.com')
        time.sleep(4)


findById = FindElementByCssSelector()
findById.locate_by_css_selector()
