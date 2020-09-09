# %%
import csv
import numpy as np
import pandas as pd
import datetime
import os
# %%
filename = '[20200903] vdd_ranking_crawl_result.csv'
# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
df = pd.read_csv(filename)
print(df.head())

# %%

today = datetime.date.today()
formatted_today = "20200905"
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
    # return tf.norm(tf.multiply(vector1,vector2)/(tf.norm(vector1)*(tf.norm(vector2))))
    # return cp.dot(vector1, vector2)/(cp.linalg.norm(vector1)*(cp.linalg.norm(vector2)))
    return np.dot(vector1, vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))
    # return cp.cos(vector1, vector2)
    # return np.cos(vector1,vector2)
    # return tf.math.cos(vector1, vector2)

# %%
martix_df = pd.read_csv(fileName)
# %%
DDList = martix_df.columns.values.tolist() 
# %%
martix_df = martix_df.T

#%%
martix_df.iloc[1,0]
#%%
# 计算第一行和第五行的相似度
print(float(similarity(np.array(martix_df.iloc[10,1:-1],dtype=float),np.array(martix_df.iloc[1,1:-1],dtype=float))))

# %%
today = datetime.date.today()
formatted_today = "20200905"
fileName = "[" + formatted_today + "] vup_similarity_displayTable.csv"
fileHead = ["VUpName"]+DDList
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
for index in range(1,1032): # 164~169 
    tmpList = []
    for indexInner in range(1,1032):
        clear_output()
        print(str(index) + "/" + str(1032) +"：正在写入"+ str(indexInner) + "/" + str(1032) +"：" + "子内容："+ martix_df.iloc[0,indexInner])
        # tmpList.append((similarity(cp.asarray(list(martix_df.iloc[index,1:-1])),cp.asarray(list(martix_df.iloc[indexInner,1:-1])))))
        tmpList.append(similarity(list(martix_df.iloc[index,1:-1]),list(martix_df.iloc[indexInner,1:-1])))
    write_csv(martix_df.iloc[index,0],tmpList)  # VUp名称的一列
print("全部写入完成")
# %%
martix_df.index.stop
# %%
