from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Fire in the hole!!') 

chrome_options= webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options = chrome_options)

while True:
    driver.get("https://slate.lkouniv.ac.in/")
    driver.maximize_window()
    driver.find_element_by_link_text("Login").click()
    time.sleep(5)
    driver.find_element_by_name("input_email").send_keys("saurabh.kanaujia020@gmail.com")
    driver.find_element_by_name("input_password").send_keys("SAURABHk_2512")
    driver.find_element_by_name("login_btn").click()
    time.sleep(10)
    driver.find_element_by_class_name("fa-phone").click()
    time.sleep(5)
        
    try:
        driver.find_element_by_link_text("Ongoing").click()
        time.sleep(20)
        driver.switch_to.window(window_name=driver.window_handles[1])
        driver.find_element_by_class_name("icon-bbb-listen").click()
        print("Class is being attended")
        time.sleep(900)
        print("Class is Ended!\nAttendance Incremented")
        break            
    except:
        print("Class is Scheduled")  
        driver.refresh()
        time.sleep(60)
        
    

