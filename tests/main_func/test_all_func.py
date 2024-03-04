import pytest, time
import logging
from logging import FileHandler
from framework import main_page

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = FileHandler('log.txt')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def test_burger_exists(driver):
    logger.info('Testing burger button!')
    burger_check_obj = main_page.MainPage(driver)
    assert burger_check_obj.burger_exists()

def test_app_settings(driver):
    logger.info('Testing app settings button!')
    burger_check_obj = main_page.MainPage(driver)
    assert burger_check_obj.settings_check()

def test_help(driver):
    logger.info('Testing app help button!')
    burger_check_obj = main_page.MainPage(driver)
    assert burger_check_obj.help_check()

def test_report(driver):
    logger.info('Testing app report button!')
    burger_check_obj = main_page.MainPage(driver)
    assert burger_check_obj.report_check()

def test_video_surv(driver):
    logger.info('Testing app video button!')
    burger_check_obj = main_page.MainPage(driver)
    assert burger_check_obj.video_surv_check()

def test_add_hub(driver):
    logger.info('Testing app add hub button!')
    burger_check_obj = main_page.MainPage(driver)
    assert burger_check_obj.add_hub_check()

def test_terms(driver):
    logger.info('Testing terms button!')
    burger_check_obj = main_page.MainPage(driver)
    assert burger_check_obj.terms_check()