from pageObjects.common.basePageObject import BasePageObject
from settings import SETTINGS

class Calculator(BasePageObject):        
    elements = dict(
        zero = f"{SETTINGS.get('appPackage')}:id/digit_0",
        one = f"{SETTINGS.get('appPackage')}:id/digit_1",
        two = f"{SETTINGS.get('appPackage')}:id/digit_2",
        three = f"{SETTINGS.get('appPackage')}:id/digit_3",
        four = f"{SETTINGS.get('appPackage')}:id/digit_4",
        five = f"{SETTINGS.get('appPackage')}:id/digit_5",
        six = f"{SETTINGS.get('appPackage')}:id/digit_6",
        seven = f"{SETTINGS.get('appPackage')}:id/digit_7",
        eight = f"{SETTINGS.get('appPackage')}:id/digit_8",
        nine = f"{SETTINGS.get('appPackage')}:id/digit_9",
        plus = f"{SETTINGS.get('appPackage')}:id/op_add",
        minus = f"{SETTINGS.get('appPackage')}:id/op_sub",
        multiply = f"{SETTINGS.get('appPackage')}:id/op_mul",
        divide = f"{SETTINGS.get('appPackage')}:id/op_div",
        equals = f"{SETTINGS.get('appPackage')}:id/eq",
        dot = f"{SETTINGS.get('appPackage')}:id/dec_point",
        result = f"{SETTINGS.get('appPackage')}:id/result",
        formula = f"{SETTINGS.get('appPackage')}:id/formula"
    )