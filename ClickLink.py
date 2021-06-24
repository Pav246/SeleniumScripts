from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D://chromedriver//chromedriver_win32//chromedriver.exe')


class TestingClickLink():

    def clickLink(self):

        driver.get("http://demo.guru99.com/test/link.html")

        links = driver.find_elements_by_link_text("click here")
        #att = link.get_attribute("href")

        for i in links:
            att = i.get_attribute("href")
            if att == "http://www.fb.com/":
                i.click()
                if "Facebook" in driver.title:
                    print("found")
                break

        '''att1 = link[0].get_attribute("href")
        att2 = link[1].get_attribute("href")

        if att1 == "http://www.fb.com/":
            link[0].click()
        elif att2 == "http://www.fb.com/":
            link[1].click()

        print("am ajuns aici") '''


test = TestingClickLink()
test.clickLink()
time.sleep(10)
driver.quit()

