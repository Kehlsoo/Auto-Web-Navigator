import os
from selenium import webdriver
import time

# Using Chrome to access web
driver = webdriver.Chrome('C:/Users/kehlsey.lewis/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')
# go to website
driver.get('https://www.google.com/')

# Find search box
searchForm = driver.find_element_by_name('q')
# Send search
searchForm.send_keys('puppies')
time.sleep()
searchForm.submit()
time.sleep(5)