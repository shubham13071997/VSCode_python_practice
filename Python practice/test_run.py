from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure
import allure_pytest


# @pytest.mark.smoke
def test_login():
 driver = webdriver.Chrome()
 driver.get("https://app.vwo.com/")
 driver.maximize_window()
 time.sleep(5)

#  driver.find_element(By.ID,)
test_login()

