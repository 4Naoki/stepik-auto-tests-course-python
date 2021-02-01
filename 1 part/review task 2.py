import time
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("//input[@type= 'text']")
    input1.send_keys("Vladimir")
    input1 = browser.find_element_by_tag_name("input[placeholder= 'Input your last name']")
    input1.send_keys("Sarychev")
    input1 = browser.find_element_by_tag_name("input[placeholder= 'Input your email']")
    input1.send_keys("232@cd.dekcm")
    input1 = browser.find_element_by_tag_name("input[placeholder= 'Input your phone:']")
    input1.send_keys("435435")
    input1 = browser.find_element_by_tag_name("input[placeholder= 'Input your address:']")
    input1.send_keys("cdsfcnjknc cnjkfdn9390239")
    btn1 = browser.find_element_by_tag_name("button[type = 'submit']")
    btn1.click()

    time.sleep(5)

    cong = browser.find_element_by_tag_name("h1")
    cong_t = cong.text
    print(cong_t)
    assert "Congratulations! You have successfully registered!" == cong_t

finally:
    time.sleep(5)
    browser.quit()
