from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction





class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, value):
        return self.driver.find_element(AppiumBy.XPATH, value)

    def find_elements(self, value):
        return self.driver.find_elements(AppiumBy.XPATH, value)

    def click_element(self, element):
        element.click()
        
    def swipe_down(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(532, 193)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(523, 1267)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
