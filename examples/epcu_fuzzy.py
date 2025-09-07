import pandas as pd

def get_series_from_csv(path):
    df = pd.read_csv(path, index_col="Nome")
    return df["Valore"].loc[~df["Valore"].index.duplicated(keep="first")]

# Complessità
low_complexity_series = get_series_from_csv("data/EPCU/low_complexity.csv")
moderate_complexity_series = get_series_from_csv("data/EPCU/moderate_complexity.csv")
high_complexity_series = get_series_from_csv("data/EPCU/high_complexity.csv")

# Durata
short_term_series = get_series_from_csv("data/EPCU/short_term.csv")
mid_term_series = get_series_from_csv("data/EPCU/mid_term.csv")
long_term_series = get_series_from_csv("data/EPCU/long_term.csv")

# Esperienza nell’uso dei tool
low_t_experience_series = get_series_from_csv("data/EPCU/low_tool_experience.csv")
moderate_t_experience_series = get_series_from_csv("data/EPCU/moderate_tool_experience.csv")
high_t_experience_series = get_series_from_csv("data/EPCU/high_tool_experience.csv")

# Rischio
low_risk_series = get_series_from_csv("data/EPCU/low_risk.csv")
moderate_risk_series = get_series_from_csv("data/EPCU/moderate_risk.csv")
high_risk_series = get_series_from_csv("data/EPCU/high_risk.csv")

# Esperienza della leadership
low_l_experience_series = get_series_from_csv("data/EPCU/low_lead_experience.csv")
moderate_l_experience_series = get_series_from_csv("data/EPCU/moderate_lead_experience.csv")
high_l_experience_series = get_series_from_csv("data/EPCU/high_lead_experience.csv")

# Motivazione
low_motivation_series = get_series_from_csv("data/EPCU/low_motivation.csv")
moderate_motivation_series = get_series_from_csv("data/EPCU/moderate_motivation.csv")
high_motivation_series = get_series_from_csv("data/EPCU/high_motivation.csv")

# Grandezza
low_size_series = get_series_from_csv("data/EPCU/low_size.csv")
moderate_size_series = get_series_from_csv("data/EPCU/moderate_size.csv")
big_size_series = get_series_from_csv("data/EPCU/big_size.csv")