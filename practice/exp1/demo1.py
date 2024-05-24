from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, 'kw')

element.send_keys('通讯')

element1 = wd.find_element(By.ID, 'go')
element.click()

wd.quit()
