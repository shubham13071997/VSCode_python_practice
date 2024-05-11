from selenium import webdriver
import pandas as pd
# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print(time.ctime())
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
driver = webdriver.Chrome(r"C:\Users\kahaa\OneDrive - esmsys pvt ltd\Desktop\chromedriver-win64\chromedriver-win64 (6)\chromedriver-win64\chromedriver.exe" , options = chrome_options)
# DataStore
database = []
 
# Gujarat Website Url
driver.get("https://anyror.gujarat.gov.in/LandRecordRural.aspx")
 
drop = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_drpLandRecord"]/option[5]').click()
time.sleep(3)
# state extract Dropdown Data here
dis_db = []
dis = driver.find_element_by_id('ContentPlaceHolder1_ddlDistrict')
dis_db.extend(dis.text.split('\n'))
try:
    for i in range(2,len(dis_db)+1):
        time.sleep(4)
        dis = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlDistrict"]/option[{i}]')
        dis.click()
        print(dis)
        wait = WebDriverWait(driver, 180)
        # element = wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_MainContent_ddlCTaluk')))
        # c = driver.find_element_by_id('ContentPlaceHolder1_ddlTaluka')
        # wait.until(EC.staleness_of(c))
 
        # district extract Dropdown Data here
        teh_db = []
        teh = driver.find_element_by_id('ContentPlaceHolder1_ddlTaluka')
        teh_db.extend(teh.text.split('\n'))
        for j in range(2,len(teh_db)+1):
            time.sleep(5)
            teh_1 = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_ddlTaluka"]/option[{j}]')
            teh_1.click()
            d = driver.find_element_by_id('ContentPlaceHolder1_ddlVillage')
           
 
            rani_db = []
            wait = WebDriverWait(driver, 180)
            element = wait.until(EC.element_to_be_clickable((By.ID, 'ContentPlaceHolder1_ddlVillage')))
            rani = driver.find_element_by_id('ContentPlaceHolder1_ddlVillage')
            rani_db.extend(rani.text.split('\n'))
            for l in range(2,len(rani_db)+1):
               
        # DataAppend in DataFrame
                database.append(dis_db[i-1]+'%'+teh_db[j-1]+'%'+rani_db[l-1])
                print(dis_db[i-1]+'%'+teh_db[j-1]+'%'+rani_db[l-1])
 
 
        # # Create DataFrame and DataStore in Excel
        a = [i.split('%') for i in  database]
        df = pd.DataFrame(a,columns=['District','Taluka','Village'])
        df.to_excel(f'Gujarat_ws_May24.xlsx',index=True,  engine='xlsxwriter')
        print(time.ctime())
except Exception as e:
    print(str(e))
    # Create DataFrame and DataStore in Excel
    a = [i.split('%') for i in  database]
    df = pd.DataFrame(a,columns=['District','Taluk','Village'])
    df.to_excel('Gujarat_ws_May24(e).xlsx',index=True,  engine='xlsxwriter')
    print(time.ctime())