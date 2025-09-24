from examples.utils import get_f_set_from_csv

# Complessità
low_complexity_f_set = get_f_set_from_csv("data/EPCU/low_complexity.csv", name="Low complexity", sep=",")
moderate_complexity_f_set = get_f_set_from_csv("data/EPCU/moderate_complexity.csv", name="Moderate complexity", sep=",")
high_complexity_f_set = get_f_set_from_csv("data/EPCU/high_complexity.csv", name="High complexity", sep=",")

# Durata
short_term_f_set = get_f_set_from_csv("data/EPCU/short_term.csv", name="Short term", sep=",")
mid_term_f_set = get_f_set_from_csv("data/EPCU/mid_term.csv", name="Mid term", sep=",")
long_term_f_set = get_f_set_from_csv("data/EPCU/long_term.csv", name="Long term", sep=",")

# Esperienza nell’uso dei tool
low_t_experience_f_set = get_f_set_from_csv("data/EPCU/low_tool_experience.csv", name="Low tool exp", sep=",")
moderate_t_experience_f_set = get_f_set_from_csv("data/EPCU/moderate_tool_experience.csv", name="Moderate tool exp", sep=",")
high_t_experience_f_set = get_f_set_from_csv("data/EPCU/high_tool_experience.csv", name="High tool exp", sep=",")

# Rischio
low_risk_f_set = get_f_set_from_csv("data/EPCU/low_risk.csv", name="Low risk", sep=",")
moderate_risk_f_set = get_f_set_from_csv("data/EPCU/moderate_risk.csv", name="Moderate risk", sep=",")
high_risk_f_set = get_f_set_from_csv("data/EPCU/high_risk.csv", name="High risk", sep=",")

# Esperienza della leadership
low_l_experience_f_set = get_f_set_from_csv("data/EPCU/low_lead_experience.csv", name="Low lead exp", sep=",")
moderate_l_experience_f_set = get_f_set_from_csv("data/EPCU/moderate_lead_experience.csv", name="Moderate lead exp", sep=",")
high_l_experience_f_set = get_f_set_from_csv("data/EPCU/high_lead_experience.csv", name="High lead exp", sep=",")

# Motivazione
low_motivation_f_set = get_f_set_from_csv("data/EPCU/low_motivation.csv", name="Low motivation", sep=",")
moderate_motivation_f_set = get_f_set_from_csv("data/EPCU/moderate_motivation.csv", name="Moderate motivation", sep=",")
high_motivation_f_set = get_f_set_from_csv("data/EPCU/high_motivation.csv", name="High motivation", sep=",")

# Grandezza
low_size_f_set = get_f_set_from_csv("data/EPCU/low_size.csv", name="Low size", sep=",")
moderate_size_f_set = get_f_set_from_csv("data/EPCU/moderate_size.csv", name="Moderate size", sep=",")
big_size_f_set = get_f_set_from_csv("data/EPCU/big_size.csv", name="Big size", sep=",")