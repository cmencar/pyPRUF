from examples.epcu_fuzzy import get_f_set_from_csv

f_set_slow = get_f_set_from_csv('data/direction/slow.csv', name="Slow speed terms", sep=",")
f_set_moderate = get_f_set_from_csv('data/direction/moderate.csv', name="Moderate speed terms", sep=",")
f_set_fast = get_f_set_from_csv('data/direction/fast.csv', name="Fast speed terms", sep=",")
