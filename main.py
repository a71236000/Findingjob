from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import json
import requests

data={
    "Number":"content"
}
def crawl():
    wd = webdriver.Chrome(service=Service('C:\chromedriver.exe'))
    wd.implicitly_wait(8)
    wd.maximize_window()
    wd.get("https://www.104.com.tw")
    element = WebDriverWait(wd, 10).until(
        EC.presence_of_element_located((By.ID, "icity"))
    )
    #選擇地區
    wd.find_element(By.ID,"icity").click()

    wd.find_element(By.XPATH,"/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/li[1]/a/span[1]/input").click()
    wd.find_element(By.XPATH,"/html/body/div[12]/div/div[2]/div/div[3]/button").click()

    #選擇職務類別
    wd.find_element(By.XPATH,"/html/body/article[1]/div/div/div[4]/div/div[2]/span").click()

    wd.find_element(By.XPATH,"/html/body/div[12]/div/div[2]/div/div[2]/div[1]/li[16]/a/span[2]").click()
    wd.find_element(By.XPATH,"/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/li[3]/button").click()

    wd.find_element(By.XPATH,"/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/ul[3]/div/li[5]/a/span[1]/input").click()
    wd.find_element(By.XPATH,"/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/ul[3]/div/li[7]/a/span[1]/input").click()
    wd.find_element(By.XPATH,"/html/body/div[12]/div/div[2]/div/div[3]/button").click()

    #搜尋關鍵字
    keyword=wd.find_element(By.ID,"ikeyword")
    keyword.send_keys("QA engineer\n")
    element = WebDriverWait(wd,10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/main/div[2]/div[3]/div[1]/ul[1]/li[4]/span"))
    )
    #選擇更新日期三日內
    wd.find_element(By.XPATH,"/html/body/main/div[2]/div[3]/div[1]/ul[1]/li[1]/span").click()
    wd.find_element(By.XPATH,"/html/body/main/div[2]/div[3]/div[2]/div/div[1]/label[2]/span").click()
    #選擇經歷
    wd.find_element(By.XPATH,"/html/body/main/div[2]/div[3]/div[1]/ul[1]/li[4]/span").click()

    wd.find_element(By.XPATH,"/html/body/main/div[2]/div[3]/div[2]/div/div[4]/label[1]/span").click()
    wd.find_element(By.XPATH,"/html/body/main/div[2]/div[3]/div[2]/div/div[4]/label[2]/span").click()
    wd.find_element(By.XPATH,"/html/body/main/div[2]/div[3]/div[1]/ul[1]/li[4]/span").click()

    #日期排序

    element = WebDriverWait(wd,10).until(
        EC.visibility_of_all_elements_located((By.XPATH,"/html/body/main/div[3]/div/div[1]/div[1]/label[2]/select/option[2]"))
    )
    wd.find_element(By.XPATH,"/html/body/main/div[3]/div/div[1]/div[1]/label[2]/select/option[2]").click()
    #列表顯示
    WebDriverWait(wd,10).until(
        EC.visibility_of_all_elements_located((By.XPATH,"/html/body/main/div[3]/div/div[1]/div[1]/ul/li[2]/a"))
    )
    wd.find_element(By.XPATH,"/html/body/main/div[3]/div/div[1]/div[1]/ul/li[2]/a").click()
    print("職缺如下:")
    time.sleep(0.5)

    #定位頁數選單
    page_button=wd.find_element(By.CLASS_NAME,"page-select.js-paging-select.gtm-paging-top")
    pages=page_button.find_elements(By.TAG_NAME,"option")
    s=0
    for page in range(1,len(pages)+1):
        #跳到下一個頁數
        page_button.click()
        WebDriverWait(wd, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,f"/html/body/main/div[3]/div/div[1]/div[1]/label[1]/select/option{[page]}")))
        a=wd.find_element(By.XPATH,f"/html/body/main/div[3]/div/div[1]/div[1]/label[1]/select/option{[page]}")
        a.click()
        WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".job-mode.js-mode-l.js-job-item")))
        #定位目前頁數的job data
        jobs = wd.find_elements(By.CSS_SELECTOR, ".job-mode.js-mode-l.js-job-item")

        for job in jobs:
            s=s+1
            print([job.text])
            #將data存入字典
            data[s]=job.text

    print(f"總共有{s}個職缺")
    return data
def output_json():
    with open('data.json', 'w',encoding='utf-8') as file:
        json.dump(data, file,ensure_ascii=False)



crawl()



