# %%
import numpy as np
import pandas as pd
# %%
filename = '[20200905] vup_similarity_displayTable.csv'
df = pd.read_csv(filename)
icon = pd.read_csv('[20200913] vup_ranking_crawl_result.csv')

# %%
iconTB = icon.loc[:,['ネーム','アイコン']]
# %%
icon[icon['ネーム'].isin(['赤井心Official'])]['アイコン']
# %%
icon.loc['赤井心Official',['ネーム','アイコン']]
# df[df.iloc[:,0]=='赤井心Official']['花园Serena']
# %%
def query(target, head=True, ascending=False):
    if(target in df.columns):
        return df.loc[:,['VUpName',target]].sort_values(by = target, ascending=ascending).head(10)\
        if(head) else df.loc[:,['VUpName',target]].sort_values(by = target, ascending=ascending)
    else: return False
# %%
query('赤井心Official',True)
# %%
def iconQ(target):
    '''查找icon'''
    return icon[icon['ネーム'].isin([target])]['アイコン'].values[0]
# %%
# %%
VUpNameList = list(iconTB['ネーム'])
IconNameList = list(iconTB['アイコン'])
# %%
zipList = list(zip(VUpNameList,IconNameList))
# %%
# %%

IconNameList[0].replace('https://i2.hdslb.com/bfs/face/', '').replace('@256h_256w', '')

# %% 清除控制台输出的内容
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
# %%
# %%


# %%
# %% 下载所有头像到本地计算机
import requests
for i in enumerate(zipList):
    with open('./icon/{0}.jpg'.format(i[1][0]), 'wb') as file:
        file.write(requests.get(i[1][1]).content)
    clear_output()
    print(i[1][0]+"\t图片下载完成")
print("全部完成")
# %%
VUpNameList
# %%

import networkx as nx
from matplotlib import pyplot as plt
G = nx.Graph()
# %%
G.add_nodes_from(VUpNameList)
# %%

# %%
import matplotlib.image as mpimg
import glob

path = './icon/'
files = [f for f in glob.glob(path + "*.jpg")]
img = []
for f in files:
    img.append(mpimg.imread(f))
    clear_output();print(f)
# %%
N = len(files)

# %%
len(img)
# %%
for f in range(2036,2338):
    img.append(mpimg.imread(files[f]))
    clear_output();print(f)
# %%


# %%
df
# %%
VUpNameList
# %%
for item in VUpNameList:
    print(df.loc[item])
# %%
def Query(row, col):
    '''查找指定的行和列,手动归一化处理'''
    if(query('row',True)):
        value = df[df['VUpName'].isin([row])][col].values[0]
        if(0<value<0.1): return value * 10
        elif(0.333>value>0.1): return value * 3
        elif(0.5>value>0.34): return value * 2
        else:return value
# %%
Query('七濑胡桃menherachan', '喵田弥夜Miya')

# %%
query('喵田弥夜Miya',True)
# %%
VUpNameList[0]
# %%
for i in range(len(VUpNameList)):
    for j in range(i,len(VUpNameList)):
        G.add_edge(VUpNameList[i],VUpNameList[j],weight=Query(VUpNameList[j],VUpNameList[j]))
# %%

#以下语句绘制以带宽为线的宽度的图
nx.draw(G, with_labels=True, edge_color='b', node_color='g', node_size=1000)
plt.show()
# %%
plt.show()
# %%
