from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Petrov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'lesson2_step8.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    submit = browser.find_element_by_tag_name("button")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
