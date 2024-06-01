import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

wd = webdriver.Chrome()
# wd.get(r'https://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A030602&sj=2023')

time.sleep(3)

xpaths = [f'//*[@id="table_main"]/tbody/tr[{i}]/td[2]' for i in range(2, 22)]

nums = []

for xpath in xpaths:
    num = wd.find_element(By.XPATH, xpath).text
    nums.append(num)

data = {'数量': nums}
pd_data = pd.DataFrame(data)

pd_data.to_csv(r'exp\exp4\male.csp')

wd.close()
