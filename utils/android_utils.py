import subprocess
import re

def take_udid():
    result = subprocess.run(['adb', 'devices', '-l'], capture_output=True, text=True)
    output = result.stdout
    output = output.replace('\n\n', '\n').split('\n')
    output.remove('List of devices attached')
    output.remove('')
    udids = [string.split()[0] for string in output]
    return udids

def android_get_desired_capabilities():
    return {
        'platformName': 'Android',
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': take_udid()[0],
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
