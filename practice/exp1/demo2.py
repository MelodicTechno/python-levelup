from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://www.byhy.net/_files/stock1.html')

elements = wd.find_elements(By.CLASS_NAME, 'result-item')

for element in elements:
    print(element.text)
