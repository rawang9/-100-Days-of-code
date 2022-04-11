from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
chrome_driver_path = '/home/rawan/Desktop/Project_python/100days/day_48/selenium/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
email = "Your id"
passw = "password"
url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(url)
sing_in = driver.find_element(By.CSS_SELECTOR,".nav__button-secondary")
sing_in.click()
id_box = driver.find_element(By.CSS_SELECTOR,"#username")
pass_box = driver.find_element(By.CSS_SELECTOR,"#password")
id_box.send_keys(email)
pass_box.send_keys(passw)
pass_box.send_keys(Keys.ENTER)
time.sleep(3)


all_jobs = driver.find_elements(By.CSS_SELECTOR,".jobs-search-two-pane__container ul li")
for jobs in all_jobs:
    time.sleep(3)
    jobs.click()
    time.sleep(3)
    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply--fadein")
        easy_apply.click()
        time.sleep(3)
        submit_button = driver.find_element(By.CSS_SELECTOR,".artdeco-button--primary")
        if(submit_button.text=="Submit application"):
            submit_button.click()
        else:
            close_but = driver.find_element(By.CSS_SELECTOR,".artdeco-modal__dismiss")
            close_but.click()
            time.sleep(3)
            disscard = driver.find_elements(By.CSS_SELECTOR,".artdeco-modal__confirm-dialog-btn")
            disscard[1].click()
        time.sleep(3)
        close_but1 = driver.find_element(By.CSS_SELECTOR,".artdeco-modal__dismiss")
        close_but1.click()
        time.sleep(3)
        continue
    except NoSuchElementException:
        print("already applied")
        continue