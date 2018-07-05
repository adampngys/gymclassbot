#! python3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import smtplib
import time
import re

def sendemail(email_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("<ENTER YOUR EMAIL>", "<ENTER YOUR APP PASSWORD>")
    to_addr = ["<ENTER ADDRESSEE'S EMAIL>"]
    msg = "\r\n".join([
            "From: <ENTER YOUR EMAIL>",
            "To: <ENTER ADDRESSEE'S EMAIL>",
            "Subject: <ENTER EMAIL SUBJECT> : {}".format(email_content),
            "",
            "<ENTER EMAIL CONTENT>"
            ])
    server.sendmail("<ENTER ADDRESSEE'S EMAIL>", to_addr, msg)
    server.quit()

chrome_path = r"<ENTER YOUR chromedriver.exe PATH>"
driver = webdriver.Chrome(chrome_path)
driver.get("https://trueclassbooking.com.sg/member/login.aspx")

#user login
user = driver.find_element_by_name("ctl00$cphContents$txtUsername")
user.send_keys("<ENTER YOUR TRUEFITNESS WEBSITE USERID>")
password = driver.find_element_by_name("ctl00$cphContents$txtPassword")
password.send_keys("<ENTER YOUR TRUEFITNESS WEBSITE PASSWORD>")
login = driver.find_element_by_name("ctl00$cphContents$btnLogin").click()

#enter class-booking interface
driver.find_element_by_class_name("btn-gradient").click()

#find gym location
driver.find_element_by_link_text("<ENTER GYM CLASS LOCATION>").click()

#find Cycling studio
driver.implicitly_wait(2)
button = driver.find_element_by_xpath("//*[@id='ctl00_cphContents_rdlStudio_0']")
driver.execute_script("arguments[0].click();", button)

###if class is on next week's schedule
##driver.find_element_by_link_text("NEXT WEEK").click()

#find class
select = Select(driver.find_element_by_name("ctl00$cphContents$ddlClassType"))
#select by visible text for class
select.select_by_visible_text("<ENTER CLASS NAME>")
#find trainer
select = Select(driver.find_element_by_name("ctl00$cphContents$ddlTrainer"))
#select by visible text for trainer
select.select_by_visible_text("<ENTER INSTRUCTOR NAME>")

#enter class-booking interface
elem = driver.find_element_by_partial_link_text("<ENTER CLASS TIME>")
#print (elem.get_attribute("href"))
elem_url = elem.get_attribute("href")
driver.get(elem_url)

while time.time() < timeout_start + timeout:
    try:
        driver.find_element_by_xpath("//*[@id='ctl00_cphContents_btnBook']").click()
        sendemail("BOOKED")
        break
    except NoSuchElementException:
        driver.refresh
        print ("Finding button...")
                 
#log out        
driver.get("https://trueclassbooking.com.sg/member/dashboard.aspx")
driver.find_element_by_partial_link_text("Logout").click()
driver.quit()
