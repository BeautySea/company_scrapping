from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from openpyxl import Workbook
from openpyxl.styles import Alignment
import requests
import base64
import hashlib
import json
import re
import os
from datetime import datetime, timedelta
import time


# Path to your ChromeDriver
chrome_driver_path = "./drivers/chromedriver/chromedriver.exe"  # Update this path accordingly
requests.get("https://poit.bolagsverket.se/poit/rest/SokKungorelse?sokord=&kungorelseid=&kungorelseObjektPersonOrgnummer=&kungorelseObjektNamn=&tidsperiod=ANNAN_PERIOD&tidsperiodFrom=2024-09-17&tidsperiodTom=2024-09-17&amnesomradeId=2&kungorelsetypId=4&underRubrikId=6")
# Optional: specify the path to your Chrome executable if it's not in the default location
chrome_options = Options()
chrome_options.binary_location = "./chrome-win64/chrome.exe"
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")  # Ensure headless mode is enabled
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (necessary for some environments)
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Disable GPU usage for better performance in headless mode
chrome_options.add_argument("--remote-debugging-port=9222")  # Fix for DevToolsActivePort file doesn't exist
chrome_options.add_argument("--disable-software-rasterizer")  # Disables use of software rasterizer

# Set up the ChromeDriver service
service = Service(chrome_driver_path)
cookie_flag = 0
# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
# This is the one time function to remove cookie

def getRecordInformation(recId):
    global cookie_flag
    if cookie_flag==0:
        driver.get("https://poit.bolagsverket.se/poit-app/")
        cookie_button = WebDriverWait(driver, 200).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Neka alla cookies']"))  # Adjust selector based on actual ID   //Acceptera förvalda cookies
        )
        cookie_button.click()
        time.sleep(50)
    #     # Wait until the blocking element disappears
    #     WebDriverWait(driver, 30).until(
    #         EC.invisibility_of_element_located((By.CLASS_NAME, "cf26vr"))  # Adjust based on the blocking element
    #     )
    #     search_announce_btn = WebDriverWait(driver, 40).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/poit-app/sok"]'))  # Adjust selector based on actual ID
    #     )
    #     search_announce_btn.click()
    #     time.sleep(1)
    #     period_selection_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "tidsperiod"))
    #     )
    #     period_selection_btn.click()
    #     time.sleep(2)
    #     period_option_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//select[@id='tidsperiod']//option[@value='ANNAN_PERIOD']"))
    #     )
    #     period_option_btn.click()
    #     time.sleep(2)
    #     date_from_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "publiceringsdatum-from"))
    #     )
    #     date_from_btn.send_keys("10-03-2023")
    #     date_from_btn.click()
    #     time.sleep(2)
    #     date_to_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "publiceringsdatum-tom"))
    #     )
    #     date_to_btn.send_keys("10-03-2023")
    #     date_to_btn.click()
    #     show_more_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Visa fler sökalternativ')]"))
    #     )
    #     show_more_btn.click()
    #     subject_area_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "amnesomrade"))
    #     )
    #     subject_area_btn.click()

    #     subject_option_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//select[@id='amnesomrade']//option[contains(text(), 'Bolagsverkets registreringar')]"))
    #     )
    #     subject_option_btn.click()
    #     time.sleep(1)
    #     kungorelse_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "kungorelserubrik"))
    #     )
    #     kungorelse_btn.click()
    #     time.sleep(2)
    #     kungorelse_option_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//select[@id='kungorelserubrik']//option[contains(text(), 'Aktiebolagsregistret')]"))
    #     )
    #     kungorelse_option_btn.click()
    #     time.sleep(2)
    #     type_case_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "underrubrik"))
    #     )
    #     type_case_btn.click()
    #     time.sleep(2)
    #     type_option_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//select[@id='underrubrik']//option[contains(text(), 'Nyregistreringar')]"))
    #     )
    #     type_option_btn.click()
        # driver.find_element(By.TAG_NAME, 'body').click()
        # time.sleep(2)
        # Wait until the blocking element disappears
        # WebDriverWait(driver, 30).until(
        #     EC.invisibility_of_element_located((By.CLASS_NAME, "cf26vr"))  # Adjust based on the blocking element
        # )
        # search_btn = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "fieldset button"))
        # )

        # try:
        #     search_btn.click()
        # except ex as Exception:
        #     print(ex)

        # time.sleep(300)
    else:
        kungorelseid = recId.replace("/", "-")
        url=f'https://poit.bolagsverket.se/poit-app/kungorelse/{kungorelseid}'
        driver.get(url)
        webdriver.ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.F5).key_up(Keys.SHIFT).perform()
        time.sleep(1)
        element = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "kungorelse__link"))
        )
        element.click()
        cookie_flag=1
    time.sleep(20)
    # if(response.status_code==200):
    #     print("response_data==",response.data)
    #     encoded_string = response.text
    #     r = qb(encoded_string)
    #     a = base64.b64decode(r)
    #     s = (recId + hamtaKey).encode('utf-8')
    #     l = hashlib.sha256(s).digest()
    #     e = bytearray(l)
    #     a = bytearray(a)
    #     o = zb(a, e)
    #     # Convert result to a UTF-8 string and then parse JSON
    #     o_str = bytes(o).decode('utf-8')
    #     d = json.loads(o_str)
    #     kungorelseData = d['kungorelseText']
    #     # Extracting values
    #     org_nr = extract_value(kungorelseData, "Org nr")
    #     if org_nr is None:
    #         org_nr=""
    #     foretagsnamn = extract_value(kungorelseData, "Företagsnamn")
    #     if foretagsnamn is None:
    #         foretagsnamn=""
    #     sate = extract_value(kungorelseData, "Säte")
    #     if sate is None:
    #         sate=""
    #     post_address = extract_value(kungorelseData, "Postadress")
    #     if post_address is None:
    #         e_post=""
    #     e_post = extract_value(kungorelseData, "E-post")
    #     if e_post is None:
    #         e_post=""
    #     typ = extract_value(kungorelseData, "Typ")
    #     if typ is None:
    #         typ=""
    #     bildat = extract_value(kungorelseData, "Bildat")
    #     if bildat is None:
    #         bildat=""
    #     recData = {'publishId':recId,'companyName':foretagsnamn,'registrationNo':org_nr,\
    #             'municipality':sate, 'county':d['lan'], 'email':e_post, 'typ':typ,'founded':bildat,'published':d['publiceringsDatum']}
    #     return recData
    # else:
    #     print("There is not a data to get")

# Start and end dates
start_date = datetime(2023, 10, 4)
end_date = datetime(2023, 10, 5)

# URL for the GET request
# url = 'https://poit.bolagsverket.se/poit/rest/SokKungorelse'

# Iterate through each day in the range
current_date = start_date
totalCnt=0
while current_date <= end_date:
    # Format the date as a string in 'YYYY-MM-DD' format
    date_str = current_date.strftime('%Y-%m-%d')
    if os.path.exists(f'{date_str}.json'):
        print(f"{date_str}.json, exists")
        with open(f'{date_str}.json', 'r') as file:
            data = json.load(file)
            # Iterate through the list and print kungorelseid         
            cnt=0
            for entry in data:
                cnt+=1
                totalCnt+=1
                if cnt==1:
                    getRecordInformation(entry['kungorelseid'])
                    # ExcelRecord = getRecordInformation(entry['kungorelseid'])
                    # print(ExcelRecord['publishId'],ExcelRecord['companyName'],ExcelRecord['registrationNo'])
                    break
                time.sleep(1)
                # print(totalCnt,"=>",cnt,"->",entry['kungorelseid'])
    else:
        print(f"{date_str}.json, does not exist")

    
    # Move to the next day
    current_date += timedelta(days=1)
    
    # Sleep for 1 second to avoid overwhelming the server with requests
    time.sleep(1)
time.sleep(100000)