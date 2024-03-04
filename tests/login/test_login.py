import pytest
import logging
from logging import FileHandler
from framework import login_page

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = FileHandler('log.txt')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def test_push_log_choice(driver):
    logger.info('Testing push log in button!')
    login_choice = login_page.LoginPage(driver)
    assert login_choice.select_log_in()

@pytest.mark.parametrize("login_ex, password_ex", [
    ('chiki@gmail.com', 'olega'),
    ('bambam@gmail.com', '111111111111111'),
    ('tuptuptup@gmail.com', 'sgagbsg'),
    ('sapfaaa@gmail.com', 'password_gasdag'),
])
def test_wrong_email_password(driver, login_ex, password_ex) -> None:
    logger.info('Testing passing wrong creds to log in!')
    login_test_page = login_page.LoginPage(driver)
    assert not login_test_page.login(login_ex, password_ex)

def test_correct_log_in(driver):
    logger.info('Testing passing correct creds to log in')
    login_test_page = login_page.LoginPage(driver)
    assert login_test_page.login('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
