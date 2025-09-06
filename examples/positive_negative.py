import pandas as pd
from pyPRUF import FSet

ps_df = pd.read_csv('./data/po_fuzzy.csv', sep=";", index_col="Nome")
ps_df_unique = ps_df["Valore"].loc[~ps_df["Valore"].index.duplicated(keep="first")]

ne_df = pd.read_csv('./data/ne_fuzzy.csv', sep=";", index_col="Nome")
ne_df_unique = ne_df["Valore"].loc[~ne_df["Valore"].index.duplicated(keep="first")]

ng_df = pd.read_csv('./data/ng_fuzzy.csv', sep=";", index_col="Nome")
ng_df_unique = ng_df["Valore"].loc[~ng_df["Valore"].index.duplicated(keep="first")]

f_set_ps = FSet(mu=ps_df_unique, name="Positive terms")
f_set_ne = FSet(mu=ne_df_unique, name="Positive terms")
f_set_ng = FSet(mu=ng_df_unique, name="Positive terms")