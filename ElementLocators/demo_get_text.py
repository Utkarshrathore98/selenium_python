import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class GetText:

    def get_text(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://yatra.com")
        text = driver.find_element(By.XPATH, "//body/div[@class='theme-snipe']/div[@id='themeSnipe']/section[@class='wrapper']/div[@class='right_data']/div[@class='inlineFlex']/div[@class='inlineFlex']/div[@class='aboutYt-new']/p[1]").text
        print(text)
        time.sleep(2)


getText = GetText()
getText.get_text()
