from appium.webdriver.common.appiumby import AppiumBy

class BaseTest:
    def __init__(self, driver):
        self.driver = driver

    def getElement(self, id):
        return self.driver.find_element(by=AppiumBy.ID, value=id)

    def validate_result(self, actual_result, expected_result):
        self.assertEqual(expected_result, actual_result, "Expected result: " + expected_result + ", Actual result: " + actual_result)
        print("Test case '" + self._testMethodName + "' in '" + self.__class__.__name__ + "' passed")