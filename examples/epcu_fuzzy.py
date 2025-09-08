import pandas as pd

from pyPRUF import FSet


def get_series_from_csv(path):
    df = pd.read_csv(path, index_col="Nome")
    return df["Valore"].loc[~df["Valore"].index.duplicated(keep="first")]

def get_f_set_from_csv(path, name):
    df = pd.read_csv(path, index_col="Nome")
    return FSet(mu=df["Valore"].loc[~df["Valore"].index.duplicated(keep="first")], name=name)

# Complessità
low_complexity_series = get_series_from_csv("data/EPCU/low_complexity.csv")
moderate_complexity_series = get_series_from_csv("data/EPCU/moderate_complexity.csv")
high_complexity_series = get_series_from_csv("data/EPCU/high_complexity.csv")

low_complexity_f_set = FSet(mu=low_complexity_series, name="Low complexity")
moderate_complexity_f_set = FSet(mu=moderate_complexity_series, name="Moderate complexity")
high_complexity_f_set = FSet(mu=high_complexity_series, name="High complexity")

# Durata
short_term_series = get_series_from_csv("data/EPCU/short_term.csv")
mid_term_series = get_series_from_csv("data/EPCU/mid_term.csv")
long_term_series = get_series_from_csv("data/EPCU/long_term.csv")

short_term_f_set = FSet(mu=short_term_series, name="Short term")
mid_term_f_set = FSet(mu=mid_term_series, name="Mid term")
long_term_f_set = FSet(mu=long_term_series, name="Long term")

# Esperienza nell’uso dei tool
low_t_experience_series = get_series_from_csv("data/EPCU/low_tool_experience.csv")
moderate_t_experience_series = get_series_from_csv("data/EPCU/moderate_tool_experience.csv")
high_t_experience_series = get_series_from_csv("data/EPCU/high_tool_experience.csv")

low_t_experience_f_set = FSet(mu=low_t_experience_series, name="Low tool exp")
moderate_t_experience_f_set = FSet(mu=moderate_t_experience_series, name="Moderate tool exp")
high_t_experience_f_set = FSet(mu=high_t_experience_series, name="High tool exp")

# Rischio
low_risk_series = get_series_from_csv("data/EPCU/low_risk.csv")
moderate_risk_series = get_series_from_csv("data/EPCU/moderate_risk.csv")
high_risk_series = get_series_from_csv("data/EPCU/high_risk.csv")

low_risk_f_set = FSet(mu=low_risk_series, name="Low risk")
moderate_risk_f_set = FSet(mu=moderate_risk_series, name="Moderate risk")
high_risk_f_set = FSet(mu=high_risk_series, name="High risk")

# Esperienza della leadership
low_l_experience_series = get_series_from_csv("data/EPCU/low_lead_experience.csv")
moderate_l_experience_series = get_series_from_csv("data/EPCU/moderate_lead_experience.csv")
high_l_experience_series = get_series_from_csv("data/EPCU/high_lead_experience.csv")

low_l_experience_f_set = FSet(mu=low_l_experience_series, name="Low lead exp")
moderate_l_experience_f_set = FSet(mu=moderate_l_experience_series, name="Moderate lead exp")
high_l_experience_f_set = FSet(mu=high_l_experience_series, name="High lead exp")

# Motivazione
low_motivation_series = get_series_from_csv("data/EPCU/low_motivation.csv")
moderate_motivation_series = get_series_from_csv("data/EPCU/moderate_motivation.csv")
high_motivation_series = get_series_from_csv("data/EPCU/high_motivation.csv")

low_motivation_f_set = FSet(mu=low_motivation_series, name="Low motivation")
moderate_motivation_f_set = FSet(mu=moderate_motivation_series, name="Moderate motivation")
high_motivation_f_set = FSet(mu=high_motivation_series, name="High motivation")

# Grandezza
low_size_series = get_series_from_csv("data/EPCU/low_size.csv")
moderate_size_series = get_series_from_csv("data/EPCU/moderate_size.csv")
big_size_series = get_series_from_csv("data/EPCU/big_size.csv")

low_size_f_set = FSet(mu=low_size_series, name="Low size")
moderate_size_f_set = FSet(mu=moderate_size_series, name="Moderate size")
high_size_f_set = FSet(mu=big_size_series, name="High size")