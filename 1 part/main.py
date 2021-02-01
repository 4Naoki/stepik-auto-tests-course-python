from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://pulse.mail.ru"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".actions-0-2-41:nth-child(2)")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
