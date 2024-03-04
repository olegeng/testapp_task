from .page import Page
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        driver.implicitly_wait(5)
        self.email_field = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'
        self.password_field = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'
        self.login_button = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button'
        self.submit_button = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
        self.main_menu_element = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/icNoHub"]'
        
    def select_log_in(self):
        self.click_element(self.find_element(self.login_button))
        return True
        
    def login(self, email, password):
        email_field = self.find_element(self.email_field)
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.find_element(self.password_field)
        password_field.clear()
        password_field.send_keys(password)

        self.click_element(self.find_element(self.submit_button))
        return self.find_elements(self.main_menu_element)



