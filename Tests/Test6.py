def find_value_of_cell(x, y):
    #import selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    #set the Chrome driver
    driver = webdriver.Chrome("../driver/chromedriver.exe")

    #navigate to the page
    driver.get("https://medo.ai/career/test-challenge/index.html")

    #find the div id and td xpath
    div = driver.find_element_by_id("test-6-div")
    td = div.find_element_by_xpath("//table[@class='table table-bordered table-dark']/tbody[1]/tr[" + str(x + 1) + "]/td[" + str(y + 1) + "]")

    #return value of cell
    return(td.text)

    #remove comment to close the Chrome driver
    #driver.close()

#assert method 2,2
assert find_value_of_cell(2, 2) == "45"

if find_value_of_cell(2, 2) == "45":
    print("Coordinates 2,2 has value '45'")
else:
    print("Coordinates 2,2 does not have value 45, it is '" + str(find_value_of_cell(2, 2)) + "'")
