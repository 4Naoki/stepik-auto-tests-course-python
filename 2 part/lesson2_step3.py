import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    number_1 = browser.find_element_by_id("num1").text
    number_2 = browser.find_element_by_id("num2").text
    sum = str(int(number_1) + int(number_2))
    print(number_1)
    print(number_2)
    print(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    #select.select_by_value("1")
    
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
