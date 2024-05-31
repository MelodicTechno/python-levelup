#Selenium模块是一个自动化测试工具，能够驱动浏览器模拟人的操作，如单击、键盘输入等。
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
import time

#从获取的网页源代码中提取目标数据
def extract_data(html_code):
    
    #目标数据的正则表达式
    p_job = 'class="jname text-cut">(.*?)</span>'
    p_salary = 'class="sal shrink-0">(.*?)</span>'
    p_needs_city =  '&quot;jobArea&quot;:&quot;(.*?)&quot;,&quot;'
    p_needs_exp =   'jobYear&quot;:&quot;(.*?)&quot;,'
    p_needs_xueli = 'jobDegree&quot;:&quot;(.*?)&quot;,&quot;'
    p_link = '<a data-v-3494039c="" href="(.*?)" target="_blank" '
    p_company = 'class="cname text-cut"> (.*?) </a>'

    #利用findall()函数提取目标数据
    job = re.findall(p_job, html_code, re.S)
    salary = re.findall(p_salary, html_code, re.S)
    needs_city = re.findall(p_needs_city, html_code, re.S)
    needs_exp = re.findall(p_needs_exp, html_code, re.S)
    needs_xueli = re.findall(p_needs_xueli, html_code, re.S)
    link = re.findall(p_link, html_code, re.S)
    company = re.findall(p_company, html_code, re.S)

    #将几个目标数据列表转换为一个字典
    data_dt = {'职位名称': job, '月薪': salary, '岗位城市': needs_city, '要求经验': needs_exp, '要求学历': needs_xueli, '职位申请链接': link, '公司名称': company}
    #用上面的字典创建一个DataFrame
    return pd.DataFrame(data_dt)
def get_pages(keyword, city, start, end):
    
    # 声明要模拟的浏览器是Chrome,并启用无界面浏览模式
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=chrome_options)
    # wait 10s if necessary
    # browser.implicitly_wait(10)
    # browser.maximize_window()

    # 通过get()函数控制浏览器发起请求，访问网址,获取源码
    url = 'https://www.51job.com/'
    browser.get(url)
    #模拟人操作浏览器，输入搜索关键词，点击搜索按钮
    browser.find_element(By.XPATH, '//*[@id="kwdselectid"]').clear()
    browser.find_element(By.XPATH, '//*[@id="kwdselectid"]').send_keys(keyword)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/button').click()
    
    # time.sleep(10)
    all_data = pd.DataFrame()
    data_list = []
    for page in range(start, end + 1):
        # 模拟人操作浏览器，输入搜索关键词，点击搜索按钮
        pre_window = browser.current_window_handle
        time.sleep(5)
        browser.find_element(By.CLASS_NAME, 'mytxt').clear()
        browser.find_element(By.CLASS_NAME, 'mytxt').send_keys(page)
        time.sleep(10)
        browser.find_element(By.CLASS_NAME, 'jumpPage').click()
        # 等待浏览器与服务器交互刷新数据，否则获取不到动态信息
        # time.sleep(10)
        #将提取的目标数据添加到DataFrame中
        # print(extract_data(browser.page_source))
        # all_data = all_data.append(extract_data(browser.page_source))
        work_info_list = []
        # for i in range(1, 19):
        #     xpath = f'//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{i}]/div[2]/div[1]/span[1]'
        #     link = browser.find_element(By.XPATH, xpath)
        #     original_window = browser.current_window_handle
            
        #     link.click()
        #     browser.switch_to.window(browser.window_handles[1])
        #     time.sleep(3)
        #     info_html = browser.page_source
        #     p_info = '<div class="bmsg job_msg inbox">\n(.*?)<a track-type="NewTrackButtonClick"'
        #     info = re.findall(p_info, info_html, re.S)
        #     work_info_list = info
        #     browser.close()
        #     browser.switch_to.window(original_window)
        # browser.switch_to.window(pre_window)
        new_data = extract_data(browser.page_source)
        # all_data = pd.concat([all_data, new_data])
        data_list.append(new_data)
        # extract_data(browser, browser.page_source)
    all_data = pd.concat(data_list)
    browser.quit()

    #将DataFrame保存为Excel
    all_data.to_excel('职位.xlsx', index=False)

get_pages('python','西安', 1, 3)
