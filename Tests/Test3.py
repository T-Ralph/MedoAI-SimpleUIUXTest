#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#set the Chrome driver
driver = webdriver.Chrome("../driver/chromedriver.exe")

#navigate to the page
driver.get("https://medo.ai/career/test-challenge/index.html")

#find the button
button = driver.find_element_by_id("dropdownMenuButton")

#assert default selected value is "Option 1"
assert button.text == "Option 1"

if button.text == "Option 1":
    print ("The default selected value is 'Option 1'")
else:
    print ("The default selected value is not 'Option 1', it is '" + button.text + "'")

#select "Option 3" from dropdown
button.click()
dropdown_options = driver.find_element_by_class_name("dropdown-menu")
a_option_3 = dropdown_options.find_element_by_xpath("//a[@class='dropdown-item'][3]")
a_option_3.click()

#remove comment to close the Chrome driver
#driver.close()
