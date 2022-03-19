from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
chrome_web_driver = "/home/rawang9/chromedriver_linux64/chromedriver"
s = Service(chrome_web_driver)
driver = webdriver.Chrome(service = s)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# #print(count.text)
# #count.click()
# All_portals = driver.find_element(By.LINK_TEXT,"All portals")
# #All_portals.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# All_portals = driver.find_element(By.LINK_TEXT,"Python")
# All_portals.click()
driver.get("http://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element(By.NAME,"fName")
fName.send_keys("Akarshit")
lName = driver.find_element(By.NAME,"lName")
lName.send_keys("gupta")
email = driver.find_element(By.NAME,"email")
email.send_keys("ag123@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR,"form button")
submit.click()
email.send_keys(Keys.ENTER)
#driver.quit()