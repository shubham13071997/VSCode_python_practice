from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://qa.easyime.org/")
driver.maximize_window()

time.sleep(4)

# JavascriptExecutor js = (JavascriptExecutor) driver;
# js.executeScript("window.scrollBy(0,250)", "");
driver.execute_script("window.scrollBy(0, 200)")

driver.find_element(By.CLASS_NAME,"browse_button").click()

time.sleep(2)
wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/div/div[2]/div[1]/div[2]/ul/li[1]/a')))
driver.find_element(By.XPATH,"/html/body/main/div/div[2]/div[1]/div[2]/ul/li[1]/a").click()

time.sleep(3)
current_url= driver.current_url
print(current_url)
assert current_url =="https://qa.easyime.org/uscis-immigration-doctors-los-angeles"
time.sleep(2)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='btn48822']/form/button").click()
# driver.execute_script("window.scrollBy(0, 500)")
# time.sleep(7)

# driver.find_element(By.XPATH,"//*[@id='Schedule_7361']/ul/li[4]/div").click()
driver.find_element(By.CSS_SELECTOR,'#Schedule_6911 > ul > li:nth-child(4) > div > span > svg > path').click()
time.sleep(7)

driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/table/tbody/tr[3]/td[7]").click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="pane_6911_0"]/div[2]/div[2]/button[2]').click()
driver.find_element(By.XPATH,'//*[@id="BtnEnable_6911"]').click()
time.sleep(10)

Booking_appointment_Page_url = driver.current_url
assert Booking_appointment_Page_url == "https://qa.easyime.org/applicant/verify"
print (Booking_appointment_Page_url)

driver.find_element(By.ID,'MobiletxtFirstName').send_keys("Hari")

driver.find_element(By.ID,"MobiletxtLastName").send_keys("Patel")
driver.find_element(By.ID,"mailtip").send_keys("Hari@yopmail.com")

driver.find_element(By.ID,"btnsubmit").click()
time.sleep(5)


Booking_appointment_Page_url_1 = driver.current_url
assert Booking_appointment_Page_url_1 == "https://qa.easyime.org/applicant/request-appointment"
print (Booking_appointment_Page_url_1)

time.sleep(2)
mobile_number=driver.find_element(By.ID,"txtPrimaryPhone")
mobile_number.click()
time.sleep(0.5)
mobile_number.send_keys("9876543410")


dropdown= Select(driver.find_element(By.ID,"ddlgender"))
dropdown.select_by_value("M")
time.sleep(3)

driver.find_element(By.ID,"txtdateofbirth").click()

driver.find_element(By.XPATH,"/html/body/div[8]/div[1]/table/tbody/tr[3]/td[3]").click()
time.sleep(3)

driver.find_element(By.XPATH,'/html/body/form/div[2]/div/div[1]/div/div[1]/div[11]/label').click()

driver.find_element(By.ID,"btnsubmit").click()
time.sleep(7)


