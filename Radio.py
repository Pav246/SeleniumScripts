
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D://chromedriver//chromedriver_win32//chromedriver.exe')


class TestingRadioButton():
    driver.get("http://demo.guru99.com/test/radio.html")
    
    def selectElments(self, lista):
        for x in lista:
            if x.is_selected():
                print("button is selected")
            else:
                x.click()
                time.sleep(5)

    def RadioButton(self):

        radio = driver.find_elements_by_xpath("//input[@type='radio']")

        self.selectElments(radio)

    def CheckBox(self):

        checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")

        self.selectElments(checkbox)

radioandcheckbox = TestingRadioButton()
radioandcheckbox.RadioButton()
radioandcheckbox.CheckBox()
driver.quit()

