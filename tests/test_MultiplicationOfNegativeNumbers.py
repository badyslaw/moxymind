import unittest
from tests.common.baseTest import BaseTest
from utilities.driver import Driver
from pageObjects.calculator import Calculator

class TestMultiplicationOfNegativeNumbers(unittest.TestCase, BaseTest):
    @classmethod
    def setUp(cls):
        Driver.setup_driver(cls)

    @classmethod
    def tearDown(cls):
        Driver.quit_driver(cls)

    #Test case: Check that multiplying negative numbers works correctly
    def test_multiply_negative_numbers(self):
        self.getElement(Calculator.elements.get("minus")).click()
        self.getElement(Calculator.elements.get("two")).click()
        self.getElement(Calculator.elements.get("multiply")).click()
        self.getElement(Calculator.elements.get("minus")).click()
        self.getElement(Calculator.elements.get("eight")).click()
        self.getElement(Calculator.elements.get("equals")).click()
        self.validate_result(self.getElement(Calculator.elements.get("result")).text, "16")
 
if __name__ == '__main__':
    unittest.main()