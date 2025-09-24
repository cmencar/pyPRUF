from examples.utils import get_f_set_from_csv

f_set_left = get_f_set_from_csv("data/direction/left.csv", "Left terms", sep=",")
f_set_right = get_f_set_from_csv("data/direction/right.csv", "Right terms", sep=",")
f_set_up = get_f_set_from_csv("data/direction/up.csv", "Up terms", sep=",")
f_set_down = get_f_set_from_csv("data/direction/down.csv", "Down terms", sep=",")
f_set_forward = get_f_set_from_csv("data/direction/forward.csv", "Forward terms", sep=",")
f_set_backward = get_f_set_from_csv("data/direction/backward.csv", "Backward terms", sep=",")
