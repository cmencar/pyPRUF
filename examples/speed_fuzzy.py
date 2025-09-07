import pandas as pd
from pyPRUF import FSet

slow_df = pd.read_csv('data/direction/slow.csv', index_col="Nome")
slow_df_unique = slow_df["Valore"].loc[~slow_df["Valore"].index.duplicated(keep="first")]

moderate_df = pd.read_csv('data/direction/moderate.csv', index_col="Nome")
moderate_df_unique = moderate_df["Valore"].loc[~moderate_df["Valore"].index.duplicated(keep="first")]

fast_df = pd.read_csv('data/direction/fast.csv', index_col="Nome")
fast_df_unique = fast_df["Valore"].loc[~fast_df["Valore"].index.duplicated(keep="first")]

f_set_slow = FSet(mu=slow_df_unique, name="Slow terms")
f_set_moderate = FSet(mu=moderate_df_unique, name="Moderate terms")
f_set_fast = FSet(mu=fast_df_unique, name="Up terms")
