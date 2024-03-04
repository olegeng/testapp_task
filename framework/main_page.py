from .page import Page
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        driver.implicitly_wait(5)
        self.burger_menu_button = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
        self.app_settings_button = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]'
        self.help_button = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Help"]'
        self.report_problem_button = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]'
        self.video_surv_button = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Video Surveillance"]'
        self.add_hub_button = '//android.widget.Button'
        self.terms_of_service_doc = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/documentation_text"]'
        self._back_button = '//android.widget.ImageButton[@resource-id="com.ajaxsystems:id/back"]'
        self._title = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/toolbarTitle"]'

    def burger_exists(self):
        self.click_element(self.find_element(self.burger_menu_button))
        return self.find_elements(self.burger_menu_button)

    def settings_check(self):
        self.click_element(self.find_element(self.app_settings_button))
        result = self.find_elements(self._title)
        self.click_element(self.find_element(self._back_button))
        return result

    def help_check(self):
        self.click_element(self.find_element(self.burger_menu_button))
        self.click_element(self.find_element(self.help_button))
        result = self.find_elements(self._title)
        self.click_element(self.find_element(self._back_button))
        return result
    
    def report_check(self):
        self.click_element(self.find_element(self.burger_menu_button))
        self.click_element(self.find_element(self.report_problem_button))
        result = self.find_elements('//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]')
        self.swipe_down()
        return result

    def video_surv_check(self):
        self.click_element(self.find_element(self.burger_menu_button))
        self.click_element(self.find_element(self.video_surv_button))
        result = self.find_elements(self._title)
        self.click_element(self.find_element('//android.widget.ImageView[@resource-id="com.ajaxsystems:id/back"]'))
        return result
        
    def add_hub_check(self):
        self.click_element(self.find_element(self.burger_menu_button))
        self.click_element(self.find_element(self.add_hub_button))
        result = self.find_elements(self._title)
        self.click_element(self.find_element('//android.widget.ImageButton[@resource-id="com.ajaxsystems:id/backButton"]'))
        return result

    def terms_check(self):
        self.click_element(self.find_element(self.burger_menu_button))
        self.click_element(self.find_element(self.terms_of_service_doc))
        result = self.find_elements(self._title)
        self.click_element(self.find_element(self._back_button))
        return result