# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
from matplotlib import colors  # 注意！为了调整“色盘”，需要导入colors
# %%
data = pd.read_csv("data.csv")
# %%
x = data.columns[0]
y = data.columns[1]
z = data.columns[2]
# %%
changecolor = colors.Normalize(vmin=data[z].min(), vmax=data[z].max())
colors = data[z]
plt.scatter(data[x],data[y],  c=colors, alpha=0.3, cmap='viridis')
plt.colorbar()  # 显示颜色条
# %%

# %%
