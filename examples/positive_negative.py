from examples.epcu_fuzzy import get_f_set_from_csv

f_set_ps = get_f_set_from_csv("data/words/po_fuzzy.csv", "Positive terms", sep=";")
f_set_ne = get_f_set_from_csv("data/words/ne_fuzzy.csv", "Neutral terms", sep=";")
f_set_ng = get_f_set_from_csv("data/words/ng_fuzzy.csv", "Negative terms", sep=";")