import pandas as pd
from pyPRUF import FSet


def get_series_from_csv(path):
    df = pd.read_csv(path, index_col="Nome")
    return df["Valore"].loc[~df["Valore"].index.duplicated(keep="first")]

def get_f_set_from_csv(path, name, sep = ";"):
    df = pd.read_csv(path, index_col="Nome", sep=sep)
    return FSet(mu=df["Valore"].loc[~df["Valore"].index.duplicated(keep="first")], name=name)