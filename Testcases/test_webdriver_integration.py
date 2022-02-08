import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType
import pytest


def get_data():
    return [
        ("trainer@way2automation.com", "dfdsfjdsf"),
        ("java@way2automation.com", "sdf"),
    ]

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password, chrome_browser):
    driver = chrome_browser
    driver.find_element(By.ID, "email").send_keys(username)
    allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)
    driver.find_element(By.ID, "pass").send_keys(password)
    assert 1 == 1
