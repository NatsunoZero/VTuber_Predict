
# %%
import tensorflow as tf   
import numpy as np
import csv
import cupy as cp
import pandas as pd
import sys
import os

# %%
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9 # 占用GPU90%的显存
session = tf.compat.v1.Session(config=config)
# %%
filename = '[20200903] vdd_ranking_crawl_result.csv'
# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
df = pd.read_csv(filename)
print(df.head())
# %%
dList = df.iloc[:, -1]  # VUp名称的一列

# %%
DDList = list(df.iloc[:, 1])  # 用于存储所有DD的名字
# %%

today = "20200905"
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
def similarity(vector1, vector2):
    '''计算相似性，即计算余弦值'''
    return tf.norm(tf.multiply(vector1,vector2)/(tf.norm(vector1)*(tf.norm(vector2))))

# %%
martix_df = pd.read_csv(fileName)
# %%
list((martix_df.iloc[1,1:-1]))
# %%

#%%
# 计算第一行和第五行的相似度
print(float(similarity(np.array(martix_df.iloc[10,1:-1],dtype=float),np.array(martix_df.iloc[1,1:-1],dtype=float))))

# %%
fileName = "[" + formatted_today + "] vdd_similarity_displayTable.csv"
fileHead = ["DDName"]+DDList
# %%

def clear_output():
    """
    clear output for both jupyter notebook and the console
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    if 'ipykernel' in sys.modules:
        from IPython.display import clear_output as clear
        clear()

# %%

create_csv()
for index in range(1,164): # 164~169 
    tmpList = []
    for indexInner in range(18684):
        clear_output()
        print(str(index) + "/" + str(18685) +"：正在写入"+str(indexInner) + "/" + str(18685) +"：" + "子内容："+ martix_df.iloc[indexInner,0])
        tmpList.append(float(similarity(np.array(martix_df.iloc[index,1:-1],dtype=float),np.array(martix_df.iloc[indexInner,1:-1],dtype=float))))
    write_csv(martix_df.iloc[index,0],tmpList)  # VUp名称的一列
print("全部写入完成")
# %%

# %%
                        

# %%


# %%
