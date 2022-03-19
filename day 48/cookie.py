#main project
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import threading
from selenium.common.exceptions import NoSuchElementException
import time
chrome_driver_path = "/home/rawang9/chromedriver_linux64/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get('https://orteil.dashnet.org/cookieclicker/')
#Get cookie to click on.
cookie = driver.find_element(By.ID,"bigCookie")
time.sleep(5)
#pass the cooki pop up
driver.find_element(By.LINK_TEXT,'Got it!').click()

done = False


def tick():
    global done
    if done:
        return
    try:
        #Get upgrade item ids.
        upgrade_tag = driver.find_element(By.CSS_SELECTOR,"div#upgrades div.enabled")
    except NoSuchElementException:
        product_tags = driver.find_elements(By.CSS_SELECTOR,
            "div#products div.enabled")
        if len(product_tags) > 0:
            product_tags[-1].click()
    else:
        upgrade_tag.click()
    finally:
        threading.Timer(10, tick).start()


def finish():
    global done
    print(driver.find_element(By.CSS_SELECTOR,'div#cookies div').text)
    done = True
tick()
threading.Timer(300, finish).start()
while not done:
    cookie.click()

driver.quit()