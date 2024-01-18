IS_EMULATOR = True
APPIUM_SERVER_URL = 'http://localhost:4723'

if (IS_EMULATOR):
    SETTINGS = dict(
                platformName='Android',
                automationName='uiautomator2',
                deviceName='Android',
                appPackage='com.android.calculator2', 
                appActivity='com.android.calculator2.Calculator',
                language='en',
                locale='US'
            )
else:
    SETTINGS = dict(
                platformName='Android',
                automationName='uiautomator2',
                deviceName='Pixel',
                appPackage='com.google.android.calculator',
                appActivity='com.android.calculator2.Calculator',
                language='en',
                locale='US'
            )