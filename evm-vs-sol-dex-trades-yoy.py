# -*- coding: utf-8 -*-

from dune_client.client import DuneClient
from dune_client.query import QueryBase
from dune_client.types import QueryParameter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import creds
import matplotlib.ticker as ticker
    
dune = DuneClient(api_key=creds.api_key)
   
query = QueryBase(
    query_id=5845809)


df = dune.run_query_dataframe(query=query)

#show first 5 values in the dataset
print(df.head())
num_rows = len(df)
print(num_rows)
#check datatypes of column
print(df.dtypes)
print(df.describe(include='all'))
df['avg_usd'] = df['avg_usd'].round(1)


#using custom colours of these chains from the logos
custom_colors = ["#667ECA", "#6C00F6", "#26E5B3","#EEBA0F","#12AAFE","#0000FE"]

g = sns.relplot(
    data=df,
    x="year", y="avg_usd", col="blockchain", hue="blockchain", palette=custom_colors,
    kind="line", linewidth=2, zorder=5,
    col_wrap=3, height=2, aspect=2, legend=False, facet_kws={'sharey': False}
)
for ax in g.axes.flat:
    ax.tick_params(labelbottom=True, labelleft=True)
    ax.set_xlabel("year", visible=True)
    ax.set_ylabel("avg_usd", visible=True)
    ax.grid(True)

    
plt.tight_layout()
g.fig.suptitle("Avg. Tx Amount By Chain on DEX's", fontsize=16, y=1.1)
