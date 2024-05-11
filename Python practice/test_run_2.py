from selenium import webdriver
import time
import pytest
import logging

from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_open_website():
    
    driver = webdriver.Chrome()
    
    # Open the url
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    #clcik on Make appointment button
    element = driver.find_element(By.ID,"btn-make-appointment")
    element.click()
    time.sleep(10)
    
    #Verify url Changes
    # assert
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    print(driver.current_url)
    
    # Enter Credentials and clcik on Login button
    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")
    Loginbtn = driver.find_element(By.ID,"btn-login")
    Loginbtn.click()
   
    # Verify Make appointment text on the web page
    verify_Make_Appnt = driver.find_element(By.XPATH,"//div//h2")
    assert verify_Make_Appnt.text == "Make Appointment"
test_open_website()  