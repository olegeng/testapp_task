import pytest

from framework.main_page import MainPage


@pytest.fixture(scope='function')
def user_actions_fixture(driver):
    yield MainPage(driver)
