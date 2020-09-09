# %%
import numpy as np
import pandas as pd
# %%
filename = '[20200905] vup_similarity_displayTable.csv'
df = pd.read_csv(filename)

# %%

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
