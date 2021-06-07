import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys





driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://web.whatsapp.com/")
time.sleep(30)
d = input("something")
namebox1 = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
namebox1.send_keys('garima didi')
namebox1.send_keys(Keys.RETURN)
d = input('ok or not')
for i in range(100):
    textbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    textbox.send_keys('thik hai .... lekin koshish karte raho')
    textbox.send_keys(Keys.RETURN)


