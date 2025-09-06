import pandas as pd
from pyPRUF import FSet

left_df = pd.read_csv('./data/left.csv', index_col="Nome")
left_df_unique = left_df["Valore"].loc[~left_df["Valore"].index.duplicated(keep="first")]

right_df = pd.read_csv('./data/right.csv', index_col="Nome")
right_df_unique = right_df["Valore"].loc[~right_df["Valore"].index.duplicated(keep="first")]

forward_df = pd.read_csv('./data/forward.csv', index_col="Nome")
forward_df_unique = forward_df["Valore"].loc[~forward_df["Valore"].index.duplicated(keep="first")]

backward_df = pd.read_csv('./data/backward.csv', index_col="Nome")
backward_df_unique = backward_df["Valore"].loc[~backward_df["Valore"].index.duplicated(keep="first")]

up_df = pd.read_csv('./data/up.csv', index_col="Nome")
up_df_unique = up_df["Valore"].loc[~up_df["Valore"].index.duplicated(keep="first")]

down_df = pd.read_csv('./data/down.csv', index_col="Nome")
down_df_unique = down_df["Valore"].loc[~down_df["Valore"].index.duplicated(keep="first")]

f_set_left = FSet(mu=left_df_unique, name="Left terms")
f_set_right = FSet(mu=right_df_unique, name="Right terms")
f_set_up = FSet(mu=up_df_unique, name="Up terms")
f_set_down = FSet(mu=down_df_unique, name="Down terms")
f_set_forward = FSet(mu=forward_df_unique, name="Forward terms")
f_set_backward = FSet(mu=backward_df_unique, name="Backward terms")
