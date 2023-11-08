import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementByLinkText:

    def locate_by_link_text():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        driver.find_element(By.LINK_TEXT, "Yatra for Business").click()
        time.sleep(4)

    def locate_by_partial_link_text():
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        driver.find_element(By.PARTIAL_LINK_TEXT, "Yatra for").click()
        time.sleep(4)


findById = FindElementByLinkText
findById.locate_by_link_text()
findById.locate_by_partial_link_text()
