from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import base64
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.common.alert import Alert 
# from selenium.common.exceptions


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--kiosk-printing")


settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
        # file) 
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,

}

prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
         "savefile.default_directory": r'C:\Python practice\Test'}
chrome_options.add_experimental_option('prefs', prefs)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://anyror.gujarat.gov.in/")
driver.maximize_window()

time.sleep(10)


WebDriverWait (driver=driver,timeout=20).until (EC.visibility_of_element_located,
(By.ID,'ContentPlaceHolder1_lb_combo_1'))
driver.find_element(By.ID ,"ContentPlaceHolder1_lb_combo_1").click()

time.sleep(3)

url = driver.current_url
print (url)
assert url == "https://anyror.gujarat.gov.in/LandRecordRural.aspx"

time.sleep(5)

# Select select = new Select(driver.findElement(By.xpath("//*[@id='oldSelectMenu']")));## in java
test = Select(driver.find_element(By.ID,"ContentPlaceHolder1_drpLandRecord"))
test.select_by_value("1")
time.sleep(3)

test1 = Select(driver.find_element(By.ID,"ContentPlaceHolder1_ddlDistrict"))
test1.select_by_visible_text("ભાવનગર")

test2 = Select(driver.find_element(By.ID,"ContentPlaceHolder1_ddlTaluka"))
test2.select_by_visible_text("ઘોઘા")

test2 = Select(driver.find_element(By.ID,"ContentPlaceHolder1_ddlVillage"))
test2.select_by_visible_text("અવાણીયા - 006")

test4 = Select(driver.find_element(By.ID,"ContentPlaceHolder1_ddlSurveyNo"))
test4.select_by_visible_text("0z૧")

time.sleep(5)



# time.sleep(10)
# user_input = input("Enter the Captcha  ")

# driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_txt_captcha_1"]').send_keys(user_input)


# time.sleep(4)


# time.sleep(15)
 
# driver.find_element(By.ID,"ContentPlaceHolder1_btnGo").click()

time.sleep(4)

# if user_input != ele_captcha:
#     driver.switch_to_alert.accept


for i in range(5):
    ele_captcha = driver.find_element(By.XPATH,('//*[@id="ContentPlaceHolder1_i_captcha_1"]'))

# get the captcha as a base64 string
    img_captcha_base64 = driver.execute_async_script("""
        var ele = arguments[0], callback = arguments[1];
        ele.addEventListener('load', function fn(){
          ele.removeEventListener('load', fn, false);
          var cnv = document.createElement('canvas');
          cnv.width = this.width; cnv.height = this.height;
          cnv.getContext('2d').drawImage(this, 0, 0);
          callback(cnv.toDataURL('image/jpeg').substring(22));
        }, false);
        ele.dispatchEvent(new Event('load'));
        """, ele_captcha)

    # save the captcha to a file
    with open(r"captcha.jpg", 'wb') as f:
      f.write(base64.b64decode(img_captcha_base64))
    user_input = input("Enter the Captcha  ")
    driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_txt_captcha_1"]').send_keys(user_input)


  


    time.sleep(1)
    
    driver.find_element(By.ID,"ContentPlaceHolder1_btnGo").click()
    try:
      alert = Alert(driver) 
      if alert:
        alert.accept()
      else:
        break
    except:
      break
    
      
# # # get alert text 
# # print(alert.text) 
  
# # # accept the alert 
# # alert.accept() 

driver.execute_script('window.print();')
time.sleep(3)



