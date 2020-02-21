#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#set the Chrome driver
driver = webdriver.Chrome("../driver/chromedriver.exe")

#wait ... implicit wait
driver.implicitly_wait(500)

#navigate to the page
driver.get("https://medo.ai/career/test-challenge/index.html")

#wait and find the button, then, click
button = driver.find_element_by_id("test5-button")
if button:
    button.click()

#find the success message and assert
message = driver.find_element_by_id("test5-alert")

assert message

if message:
    print("Success message displayed")
else:
    print("Success message not displayed")

#assert button is disabled
assert button.is_enabled() == False

if button.is_enabled() == False:
    print ("Button is now disabled")
else:
    print ("Button is still enabled")

#remove comment to close the Chrome driver
#driver.close()
