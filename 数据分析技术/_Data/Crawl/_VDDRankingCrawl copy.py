# %%
# from selenium import webdriver
import numpy as np
# %%

# %%
import time
from bs4 import BeautifulSoup
import re

# %%
import csv
import cupy as cp
import pandas as pd
# %%

import datetime
import os
# %%

today = datetime.date.today()
formatted_today = today.strftime('%Y%m%d')
fileName = "[" + formatted_today + "] vdd_ranking_crawl_result.csv"
fileHead = ["順位", "ネーム", "ルームナンバー", "info", "登録者数"]
# %%
driver = webdriver.Chrome()  # 用chrome浏览器打开

options = webdriver.ChromeOptions()
driver.get("https://vtbs.moe/dd")
# %%


def execute_times(times):
    for i in range(times + 1):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


execute_times(1)

# %%
html = driver.page_source
# %%
# print(html)
f = open("VDDAllRanking.html", 'w', encoding="utf-8")
f.write(html)
# %%
f = open("VDDAllRanking.html", 'r', encoding="utf-8")
# f.write(html)
# %%
soup = BeautifulSoup(f.read(), 'lxml')
# soup=BeautifulSoup(f.read(),'html5lib')
# %%


def create_csv():
    '''创建用于保存的文件'''
    with open(fileName, 'w', newline='', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(fileHead)


def write_csv(rank, *name):
    '''逐行写入内容'''
    with open(fileName, 'a+', newline='', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        data_row = [rank]
        for item in name:
            data_row.append(item)
        csv_write.writerow(data_row)


def print_log_info(log):
    '''输出log'''
    os.system('cls')
    print(log)
# %%


def execute():
    rank = 1

    _dataRaw = soup.findAll(
        name="div", attrs={"class": re.compile("^columns is-gapless")})
    for item in _dataRaw:
        tmpVtbNameList = []
        tmpVtbIdList = []
        ddIcon = item.img.get('src')  # dd头像
        ddName = item.find(name="div", attrs={
                           "class": "column is-one-third"}).span.text.split()[-1]  # dd名字

        oshiList = item.findAll(
            name="a", attrs={"href": re.compile("^/detail/")})
        if(oshiList[0].get('title') == '这是一名本站收录的VTB/VUP'):
            oshiList.remove(oshiList[0])
        for vtbItem in oshiList:
            vtbId = vtbItem.get('href').split('/')[-1]
            vtbName = vtbItem.text.strip()
            tmpVtbIdList.append(vtbId)
            tmpVtbNameList.append(vtbName)

        # fansChangeCount = fansInfo[1].text.strip() # 粉丝变化数
        write_csv(rank, ddName, tmpVtbNameList)
        print_log_info("正在写入 "+str(rank)+"位DD: "+ddName)
        rank += 1
# %%


def main():
    execute()


if __name__ == "__main__":
    main()
# %%
# %%
filename = '[20200903] vdd_ranking_crawl_result.csv'
# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
df = pd.read_csv(filename)
print(df.head())
# %%
dList = df.iloc[:, -1]  # VUp名称的一列
# %%
type(dList)
# %%

pd.value_counts(list(dList))
# %%
df.columns  # 查看列表的列名称
# %%
VUpList = []  # 用于存储所有VUp的名字
# %%
for raw in dList:
    print("正在添加"+raw)
    for item in (raw[1:-1].split(",")):
        VUpList.append(item.strip()[1:-1])
print("添加完成")
# %%
len(VUpList)  # VUp个数 24745
# %%
VUpList = list(set(VUpList))  # 去重
# %%
len(VUpList)  # VUp个数 1031
# %%
DDList = list(df.iloc[:, 1])  # 用于存储所有DD的名字
# %%
(["DDName"]+VUpList)
# %%

today = datetime.date.today()
formatted_today = today.strftime('%Y%m%d')
fileName = "[" + formatted_today + "] vdd_OSHI_result.csv"
# fileHead = ["DDName"]+VUpList
# %%


def create_csv():
    '''创建用于保存的文件'''
    with open(fileName, 'w', newline='', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(fileHead)


def write_csv(rank, name):
    '''逐行写入内容'''
    with open(fileName, 'a+', newline='', encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        data_row = [rank]
        for item in name:
            data_row.append(item)
        csv_write.writerow(data_row)


# %%
create_csv()
for index in df.index:
    ddName = df.loc[index][1]
    DVUpListUnHandle = df.loc[index][2][1:-1].split(",")
    ThisDDVUpList = []
    for item in DVUpListUnHandle:
        ThisDDVUpList.append(item.strip()[1:-1])

    tmpDVUNum = []

    for vupitem in VUpList:
        if(vupitem in ThisDDVUpList):
            tmpDVUNum.append(1)
        else:
            tmpDVUNum.append(0)
    print("正在写入第"+str(index)+"位DD")
    write_csv(ddName, tmpDVUNum)
print("所有DD写入完成")
# %%
def similarity(vector1, vector2):
    '''计算相似性，即计算余弦值'''
    # return tf.norm(tf.multiply(vector1,vector2)/(tf.norm(vector1)*(tf.norm(vector2))))
    # return cp.dot(vector1, vector2)/(cp.linalg.norm(vector1)*(cp.linalg.norm(vector2)))
    return np.dot(vector1, vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))
    # return cp.cos(vector1, vector2)
    # return np.cos(vector1,vector2)
    # return tf.math.cos(vector1, vector2)

# %%
martix_df = pd.read_csv(fileName)
# %%
list((martix_df.iloc[1,1:-1]))
# %%

#%%
# 计算第一行和第五行的相似度
print(float(similarity(np.array(martix_df.iloc[10,1:-1],dtype=float),np.array(martix_df.iloc[1,1:-1],dtype=float))))

# %%
today = datetime.date.today()
formatted_today = today.strftime('%Y%m%d')
fileName = "[" + formatted_today + "] vdd_similarity_displayTable.csv"
fileHead = ["DDName"]+DDList
# %%
import sys
import os
def clear_output():
    """
    clear output for both jupyter notebook and the console
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    if 'ipykernel' in sys.modules:
        from IPython.display import clear_output as clear
        clear()

# %%
# create_csv()
for index in range(120,164): # 164~169 
    tmpList = []
    for indexInner in range(18684):
        clear_output()
        print(str(index) + "/" + str(18684) +"：正在写入"+str(indexInner) + "/" + str(18685) +"：" + "子内容："+ martix_df.iloc[indexInner,0])
        # tmpList.append((similarity(cp.asarray(list(martix_df.iloc[index,1:-1])),cp.asarray(list(martix_df.iloc[indexInner,1:-1])))))
        tmpList.append(similarity(list(martix_df.iloc[index,1:-1]),list(martix_df.iloc[indexInner,1:-1])))
    write_csv(martix_df.iloc[index,0],tmpList)  # VUp名称的一列
print("全部写入完成")

3

# %%
martix_df.index.stop
# %%
import tensorflow as tf                           

# %%
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9 # 占用GPU90%的显存
session = tf.compat.v1.Session(config=config)
# %%
