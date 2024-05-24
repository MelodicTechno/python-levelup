from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/_files/stock1.html')

element1 = wd.find_element(By.ID, 'kw')

element1.send_keys('通讯\n')

element2 = wd.find_element(By.ID, '1')

print('Outer html:', element2.get_attribute('outerHTML'))
