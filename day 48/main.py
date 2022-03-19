from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = "/home/rawang9/chromedriver_linux64/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.python.org/")
#driver.maximize_window()
#driver.implicitly_wait(5)
#driver.close()#for single tab
# price = driver.find_element(By.XPATH,'//*[@id="priceblock_ourprice_row"]/td[2]/span[1]')
# print(price.text)
# search_bar = driver.find_element(By.NAME,"q")
# print(search_bar.get_attribute("placeholder"))
documentation_link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
print(documentation_link.text)
driver.quit()#for quit the browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = "/home/rawang9/chromedriver_linux64/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.python.org/")
detail = {}
dates_data = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
for i in range(len(events)):
    detail[i] = {
        "time ": dates_data[i].text,
        "name ": dates_data[i].text
    }
print(detail)
driver.quit()

