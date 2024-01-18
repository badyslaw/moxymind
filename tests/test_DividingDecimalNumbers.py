import unittest
from tests.common.baseTest import BaseTest
from utilities.driver import Driver
from pageObjects.calculator import Calculator

class TestDividingDecimalNumbers(unittest.TestCase, BaseTest):
    @classmethod
    def setUp(cls):
        Driver.setup_driver(cls)

    @classmethod
    def tearDown(cls):
        Driver.quit_driver(cls)
         
    #Test case: Check that the division of decimal numbers works correctly
    def test_divide_decimal_numbers(self):
        self.getElement(Calculator.elements.get("two")).click()
        self.getElement(Calculator.elements.get("dot")).click()
        self.getElement(Calculator.elements.get("five")).click()
        self.getElement(Calculator.elements.get("divide")).click()
        self.getElement(Calculator.elements.get("dot")).click()
        self.getElement(Calculator.elements.get("five")).click()
        self.validate_result(self.getElement(Calculator.elements.get("result")).text, "5")
 
if __name__ == '__main__':
    unittest.main()