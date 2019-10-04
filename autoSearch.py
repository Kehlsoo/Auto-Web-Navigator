import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Using Chrome to access web
#driver = webdriver.Chrome('C:/Users/kehlsey.lewis/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
driver = webdriver.Chrome(options=chromeOptions) #Would like chrome to start in fullscreen


# go to website
driver.get('https://www.google.com/')

# Find search box
searchForm = driver.find_element_by_name('q')

# type in what you want to search
searchForm.send_keys('puppies')
time.sleep(2)

#search
searchForm.submit()
time.sleep(5)
driver.quit()