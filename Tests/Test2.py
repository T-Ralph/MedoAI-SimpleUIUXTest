#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#set the Chrome driver
driver = webdriver.Chrome("../driver/chromedriver.exe")

#navigate to the page
driver.get("https://medo.ai/career/test-challenge/index.html")

#find the div id, ul class and li class
div = driver.find_element_by_id("test-2-div")
ul = div.find_element_by_xpath("//ul[@class='list-group']")
li = ul.find_elements_by_xpath("//li[@class='list-group-item justify-content-between']")

#assert the length of li elements
assert len(li) == 3

if len(li) == 3:
    print ("Li listgroup has 3 items")
else:
    print ("Li listgroup has " + str(len(li)) + " items")

#assert the length of badge elements
badge = 0

for li_each in li:
    if li_each.find_element_by_xpath("//span[@class='badge badge-pill badge-primary']"):
        badge += 1

assert badge == 3

if badge == 3:
    print ("Li badge has 3 values")
else:
    print ("Li badge has " + str(badge) + " values")

#assert that second list is "List Item 2"
li_second = ul.find_element_by_xpath("//li[@class='list-group-item justify-content-between'][2]")

assert li_second.text[:-2] == "List Item 2"

if li_second.text[:-2] == "List Item 2":
    print ("The second list item is 'List Item 2'")
else:
    print ("The second list item is not 'List Item 2', it is '" + li_second.text[:-2] + "'")

#assert that second list item's badge value is 6
badge_second = li_second.find_element_by_tag_name("span")

assert badge_second.text == "6"

if badge_second.text == "6":
    print ("The second list badge value is '6'")
else:
    print ("The second list badge value is not '6', it is '" + badge_second.text + "'")

#remove comment to close the Chrome driver
#driver.close()
