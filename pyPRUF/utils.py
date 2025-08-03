import numpy as np

def is_list_out_of_range(x, inf, sup):
    return any(is_out_of_range(elem, inf, sup) for elem in x)

def is_out_of_range(x, inf, sup):
    return inf > x or x > sup

def is_list_not_unique(x):
    return np.unique(x).size != len(x)
