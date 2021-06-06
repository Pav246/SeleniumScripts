from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='D://chromedriver//chromedriver_win32//chromedriver.exe')

class DragAndDrop():

    def testingDragAndDrop(self):

        driver.get("http://jqueryui.com/droppable/")

        pathIframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(pathIframe)

        fromElement = driver.find_element_by_xpath("//div[@id='draggable']")
        toElement = driver.find_element_by_xpath("//div[@id='droppable']")

        action = ActionChains(driver)
        action.drag_and_drop(fromElement, toElement)
        action.perform()

        time.sleep(10)

DragAndDrop = DragAndDrop()
DragAndDrop.testingDragAndDrop()
driver.quit()


