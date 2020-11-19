from selenium import webdriver                                          #Importing the libraries
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests



#This Bot is developed by saurabhkumar kanaujia. Feel free to ask me anything. 
#Connect with me on Github : https://github.com/saurabhkumarkanaujia



#discord script
sched = {
    'content':"No classes currently"
}
attend = {
    'content':"Hurray!\nClass is being attended\nEnjoy :)"
}
comp = {
    'content':"Congrats!\nClass has been attended :)"
}
header = {
    'authorization': #'Your dicord authorization id'
}
#/discord script

options=Options()
options.headless=True
options.add_argument("--log-level=3")




driver = webdriver.Chrome(options=options)


driver.get("https://slate.lkouniv.ac.in/")
driver.maximize_window()
driver.find_element_by_link_text("Login").click()
time.sleep(5)
driver.find_element_by_name("input_email").send_keys("<Your Email ID>")                           #Enter your Registered Email ID
driver.find_element_by_name("input_password").send_keys("<Your Password>")                        #Enter your Password  
driver.find_element_by_name("login_btn").click()
time.sleep(10)
driver.get("https://slate.lkouniv.ac.in/stuludent/all-class-list")
time.sleep(5)
while True:
    try:
        driver.find_element_by_link_text("Ongoing").click()
        time.sleep(20)
        driver.switch_to.window(window_name=driver.window_handles[1])
        driver.find_element_by_class_name("icon-bbb-listen").click()
        print("Class is being attended!")
        r = requests.post("<Your discord Request URL>",data = attend, headers = header)             #Enter your Discord Request URL
        time.sleep(900)
        print("Class is Ended!\nAttendance Incremented")   
        r = requests.post("<Your discord Request URL>",data = comp, headers = header)               #Enter your Discord Request URL
    except:
        print("No Classes Currently")  
        r = requests.post("<Your discord Request URL>",data = sched, headers = header)              #Enter your Discord Request URL
        driver.refresh()
        time.sleep(120)