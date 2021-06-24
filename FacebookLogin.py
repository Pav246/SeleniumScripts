from selenium import webdriver
import time
from config.settings import USERNAME, PASSWORD
driver = webdriver.Chrome(executable_path='D://chromedriver//chromedriver_win32//chromedriver.exe')


class Facebook():

    def login(self):
        driver.get("http://facebook.com/")
        acceptAll = driver.find_element_by_xpath("//button[contains(text(),'Acceptă tot')]")
        acceptAll.click()

        email = driver.find_element_by_xpath("//input[@id='email']")
        email.send_keys("email@yahoo.com")

        password = driver.find_element_by_xpath("//input[@id='pass']")
        password.send_keys("parola")

        LogIn = driver.find_element_by_xpath("//button[contains(text(),'Conectează-te')]")
        LogIn.click()

#mail : //input[@id='email']
#parola : //input[@id='pass']

        time.sleep(10)


fb = Facebook()
fb.login()
driver.quit()



