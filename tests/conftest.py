import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


@pytest.fixture(scope='function', autouse=True)
def browser_size():
    browser.config.window_height = '1920'
    browser.config.window_width = '1080'
