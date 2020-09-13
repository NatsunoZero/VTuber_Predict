# %%
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# %%
import csv
import datetime
import os
import re

today=datetime.date.today()
formatted_today=today.strftime('%Y%m%d')
fileName = "[" + formatted_today + "] vup_ranking_crawl_result.csv"
fileHead = ["順位","ネーム", "アイコン", "ルームナンバー","info","登録者数"]
#%%
driver = webdriver.Chrome()                #用chrome浏览器打开

options = webdriver.ChromeOptions()
driver.get("https://vtbs.moe/")       
# %%
def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
execute_times(230)

# %%
html=driver.page_source
# %%
print(html)
# %%
f = open("VUpAllRanking.html",'r',encoding="utf-8")
# f.write(html)
# %%
soup=BeautifulSoup(f.read(),'lxml')
# soup=BeautifulSoup(f.read(),'html5lib')
# %%
def create_csv():
    '''创建用于保存的文件'''
    with open(fileName,'w', newline='', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(fileHead)
def write_csv( rank, name, icon, roomNumber, chanName, fansCount):
    '''逐行写入内容'''
    with open(fileName, 'a+', newline='', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        data_row = [rank, name, icon, roomNumber, chanName, fansCount]
        csv_write.writerow(data_row)
def print_log_info(log):
    '''输出log'''
    os.system('cls')
    print(log)
# %%
def execute():
    rank = 1
    _dataRaw = soup.findAll(name="div", attrs={"class":re.compile("^columns is-mobile is-multiline card")}) 

    for item in _dataRaw:

        _icon = item.find(name="div", attrs={"class":"column smallBottomMarginTopBottomPadding is-6-mobile is-3-tablet is-3-desktop is-3-widescreen is-3-fullhd"}).img.get('src')
        _nameColumn = item.find(name="div", attrs={"class":"column is-12-mobile is-6-tablet is-6-desktop is-6-widescreen is-6-fullhd content smallBottomMarginTopBottomPadding"})
        nameANDliveNO = _nameColumn.find('h4')
        if( nameANDliveNO.text.split()[0]!="直播中"):
            upName = nameANDliveNO.text.split()[0] # Up名字
            liveNO = nameANDliveNO.text.split()[1] # 直播间号
        else:
            upName = nameANDliveNO.text.split()[1] # Up名字
            liveNO = nameANDliveNO.text.split()[2] # 直播间号
        intro = _nameColumn.p.text # 主播简介
        _fansColumn = item.find(name="div", attrs={"class":"column is-hidden-mobile is-3-mobile is-3-tablet is-3-desktop is-3-widescreen is-3-fullhd"})
        fansInfo = _fansColumn.findAll(name="div", attrs={"class":"column is-7"})
        fansCount = fansInfo[0].text.strip() # 粉丝数
        #fansChangeCount = fansInfo[1].text.strip() # 粉丝变化数
        write_csv(rank, upName, _icon, liveNO, intro, fansCount)
        print_log_info("正在写入 "+str(rank)+"位: "+upName)
        rank += 1
# %%
def main():
    create_csv()
    execute()
if __name__=="__main__":
    main()
# %%
