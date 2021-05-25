import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://www.facebook.com")
f=open("pass.txt","r")
file=f.readline()
password=str(file)
el1=driver.find_element_by_id("email")
el1.send_keys("your email here")
sleep(1)
el2=driver.find_element_by_id("pass")
el2.send_keys("password")
sleep(1)
el=driver.find_element_by_name("login")
el.click()
