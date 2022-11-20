from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://selenium1py.pythonanywhere.com/en-gb/basket/"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#content_inner p')

finally:
    browser.quit()