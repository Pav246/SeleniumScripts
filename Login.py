from selenium import webdriver
import time
from config.settings import USERNAME, PASSWORD

driver = webdriver.Chrome(executable_path='D://chromedriver//chromedriver_win32//chromedriver.exe')

class TestingLogin():
    def LoginNok(self, username, parola, testcase):
        driver.get("http://www.demo.guru99.com/V4/")

        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys(username)

        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        time.sleep(5)

        try:
            actualTitle = driver.title
            print(actualTitle)
            if actualTitle == "Guru99 Bank Manager HomePage":
                print("TEST CASE LOGIN NOK FAILED " + testcase)
            else:
                print("TEST CASE LOGIN NOK PASS " + testcase)
        except:
            print("TEST CASE LOGIN NOK PASSED " + testcase)


    def LoginOK(self,username, parola, testcase):
        driver.get("http://www.demo.guru99.com/V4/")

        #user=driver.find_element_by_name("uid")
        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys(username)
        #input[@name='uid']

        #password = driver.find_element_by_name("password")
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()
        try:
            actualTitle = driver.title
            print(actualTitle)
            if actualTitle == "Guru99 Bank Manager HomePage":
                print("TEST CASE LOGIN PASS " + testcase)
            else:
                print("TEST CASE LOGIN FAILED " + testcase)
        except:
            print("TEST CASE LOGIN FAILED  " + testcase)


test = TestingLogin()
#username = "mngr327236"
#parola = "rehavAs"
test.LoginOK(USERNAME, PASSWORD, "TC1")
test.LoginNok(USERNAME, "parolagresita", "TC2")
test.LoginNok("userNOK", PASSWORD, "TC3")
test.LoginNok("userNOK", "parolaNOK","tc4")
test.LoginNok("", PASSWORD, "tc5")
test.LoginNok(USERNAME, "", "tc6")
driver.quit()

