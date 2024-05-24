import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
#声明使用Chrome
browser = webdriver.Chrome()
browser.get(r'http://www.51job.com')
#在搜索框输入关键词
browser.find_element(By.XPATH,'//*[@id="kwdselectid"]').send_keys('Python工程师')
#点击搜索按钮
browser.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/button').click()
#等待浏览器与服务器交互刷新数据，否则获取不到动态信息
time.sleep(5)

#提取目标数据
p_job = 'joblist-item-top'
p_salary = 'sal shrink-0'

jobs = browser.find_elements(By.CLASS_NAME, p_job)
# salaries = browser.find_elements(By.CLASS_NAME, p_salary)

job_name = []
job_sal = []

print(type(jobs))
#保存目标数据
for job in jobs:
    info = job.text
    info1, info2 = info.split('\n')
    job_name.append(info1)
    job_sal.append(info2)
    # print(job.text, info1, info2)
# 高级软件开发工程师（偏前端）\n1.5-2.2万·13薪

data = {'岗位':job_name,'薪水':job_sal}
data = pd.DataFrame(data)
# #创建Excel文件，保存目标数据
data.to_excel('岗位薪水.xlsx', index=False)
