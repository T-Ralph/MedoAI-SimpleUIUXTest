#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#set the Chrome driver
driver = webdriver.Chrome("../driver/chromedriver.exe")

#navigate to the page
driver.get("https://medo.ai/career/test-challenge/index.html")

#find the form field elements and button
email = driver.find_element_by_id("inputEmail")
password = driver.find_element_by_id("inputPassword")
submit = driver.find_element_by_xpath("//form[@class='form-signin']/button[1]")

#assert the presence of the login fields and button
assert email
assert password
assert submit

if email:
    print("Email field present")
else:
    print("Email field not present")

if password:
    print("Password field present")
else:
    print("Password field not present")

if submit:
    print("Submit button present")
else:
    print("Submit button not present")

#clear any existing content and fill the form fields
email.clear()
password.clear()
email.send_keys("olaniyitralph@gmail.com")
password.send_keys("password")

#remove comment to close the Chrome driver
#driver.close()
