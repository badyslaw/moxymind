from appium import webdriver
from appium.options.android import UiAutomator2Options
from settings import SETTINGS, APPIUM_SERVER_URL

class Driver:
    def __init__(self):
        self.driver = None

    def setup_driver(self):
        self.driver = webdriver.Remote(APPIUM_SERVER_URL, options=UiAutomator2Options().load_capabilities(SETTINGS))

    def quit_driver(self):
        if self.driver:
            self.driver.quit()