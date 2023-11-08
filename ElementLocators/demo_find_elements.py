import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElements:

    def locate_by_tag_name(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        lst = driver.find_elements(By.TAG_NAME, 'a')
        print(len(lst))
        for i in lst:
            print(i.text)
        time.sleep(4)


findElements = FindElements()
findElements.locate_by_tag_name()
