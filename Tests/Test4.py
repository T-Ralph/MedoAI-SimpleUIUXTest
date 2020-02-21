#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#set the Chrome driver
driver = webdriver.Chrome("../driver/chromedriver.exe")

#navigate to the page
driver.get("https://medo.ai/career/test-challenge/index.html")

#find the div id buttons
div_button_1 = driver.find_element_by_xpath("//div[@id='test-4-div']/button[1]")
div_button_2 = driver.find_element_by_xpath("//div[@id='test-4-div']/button[2]")

#assert frst button is enabled
assert div_button_1.is_enabled() == True

if div_button_1.is_enabled() == True:
    print ("First button is enabled")
else:
    print ("First button is disabled")

#assert second button is disabled
assert div_button_2.is_enabled() == False

if div_button_2.is_enabled() == False:
    print ("Second button is disabled")
else:
    print ("Second button is enabled")

#remove comment to close the Chrome driver
#driver.close()
