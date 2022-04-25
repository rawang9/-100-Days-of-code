from configparser import Interpolation
from os import uname
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "/home/rawan/Desktop/Project_python/100days/day_48/selenium/chromedriver"
driver  = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/app/recs")

login = driver.find_element(By.XPATH,'//*[@id="q939012387"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(2)
try:
    fbook = driver.find_element(By.XPATH,'//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
except NoSuchElementException:
    more_op = driver.find_element(By.XPATH,'//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/button').click()
    time.sleep(2)
    fbook = driver.find_element(By.XPATH,'//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
time.sleep(1)
uname = driver.find_element(By.CSS_SELECTOR,'.login_form_label input').click()
print(uname)

#print(fbook)
driver.quit()