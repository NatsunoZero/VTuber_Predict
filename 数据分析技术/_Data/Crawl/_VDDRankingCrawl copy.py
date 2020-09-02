# %%
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

# %%
import csv
import datetime
import os

today=datetime.date.today()
formatted_today=today.strftime('%Y%m%d')
fileName = "[" + formatted_today + "] vdd_ranking_crawl_result.csv"
fileHead = ["順位","ネーム", "ルームナンバー","info","登録者数"]
#%%
driver = webdriver.Chrome()                #用chrome浏览器打开

options = webdriver.ChromeOptions()
driver.get("https://vtbs.moe/dd")       
# %%
def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
execute_times(1)

# %%
html=driver.page_source
# %%
# print(html)
f = open("VDDAllRanking.html",'w',encoding="utf-8")
f.write(html)
# %%
f = open("VDDAllRanking.html",'r',encoding="utf-8")
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
def write_csv( rank, name, roomNumber, chanName, fansCount):
    '''逐行写入内容'''
    with open(fileName, 'a+', newline='', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        data_row = [rank, name, roomNumber, chanName, fansCount]
        csv_write.writerow(data_row)
def print_log_info(log):
    '''输出log'''
    os.system('cls')
    print(log)
# %%
# def execute():
#     rank = 1
#     _dataRaw = soup.findAll(name="div", attrs={"class":re.compile("^columns is-gapless")}) 

#     for item in _dataRaw:

# _icon = item.find(name="div", attrs={"class":"column smallBottomMarginTopBottomPadding is-6-mobile is-3-tablet is-3-desktop is-3-widescreen is-3-fullhd"}).img.get('src')

#%%
_dataRaw = soup.findAll(name="div", attrs={"class":re.compile("^columns is-gapless")}) 
#%%
item = _dataRaw[0]
#%%
ddIcon = item.img.get('src') # dd头像
ddName = item.find(name="div", attrs={"class":"column is-one-third"}).span.text.split()[-1] # dd名字
#%%
len(_dataRaw)
#%%

item.find_all(name="div", attrs={"class":"guard guard-0"}) # 总督
item.find_all(name="div", attrs={"class":"guard guard-1"}) # 提督
item.find_all(name="div", attrs={"class":"guard guard-2"}) # 舰长




#%%
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
write_csv(rank, upName, liveNO, intro, fansCount)
print_log_info("正在写入 "+str(rank)+"位: "+upName)
# rank += 1
# %%
def main():
    create_csv()
    execute()
if __name__=="__main__":
    main()
# %%
