import subprocess
import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.android_utils import android_get_desired_capabilities
import logging

@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', 'localhost', '-p', '4727', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    app_driver = webdriver.Remote('http://localhost:4727', options=UiAutomator2Options().load_capabilities(android_get_desired_capabilities()))
    yield app_driver
    if app_driver:
        app_driver.quit()

def tearDown() -> None:
    if driver:
        driver.quit()