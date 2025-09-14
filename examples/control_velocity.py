# OBIETTIVO
# Controllare la velocità di un motore DC in base a:
# l’errore e(t) tra velocità desiderata e attuale
# la derivata dell’errore de(t)
#
# INPUT
# e(t) → Errore = v_ref - v(t)
# de(t) → Derivata dell'errore
#
# OUTPUT
# u(t) → Tensione di controllo da inviare al motore
# | Regola | Condizione (e, de)            | u(t) = a·e + b·de + c     |
# | ------ | ----------------------------- | ------------------------- |
# | R1     | Se `e` è Neg e `de` è Neg     | u = -2.0·e - 1.0·de + 0.5 |
# | R2     | Se `e` è Zero e `de` è Zero   | u =  0.0·e + 0.0·de + 0.0 |
# | R3     | Se `e` è Pos e `de` è Pos     | u =  2.0·e + 1.0·de + 0.5 |
# | R4     | Se `e` è Zero e `de` è Neg    | u = -1.0·e - 0.5·de + 0.2 |
# | R5     | Se `e` è Pos e `de` è Neg     | u =  2.0·e - 1.0·de + 0.1 |


from numpy.ma.core import arange

from pyPRUF import FSet, TSControl, TSRule
from pyPRUF import trap_mf, tri_mf

negative_f_set = FSet(mu=lambda x: trap_mf(x, -5, -5, -1, 0), index=arange(-5, 0, 0.25))
zero_f_set = FSet(mu=lambda x: tri_mf(x, -1, 0 - 1), index=arange(-1, 0, 0.25))
positive_f_set = FSet(mu=lambda x: trap_mf(x, 0, 1, 5, 5), index=arange(0, 5, 0.25))

def rule_one(control_input):
    return -2 * control_input["e"] - control_input["de"] + 0.5

def rule_two(_control_input):
    return 0

def rule_three(control_input):
    return 2 * control_input["e"] + control_input["de"] + 0.5

def rule_four(control_input):
    return -1 * control_input["e"] - 0.5 * control_input["de"] + 0.2

def rule_five(control_input):
    return -2 * control_input["e"] - control_input["de"] + 0.1

controller = TSControl([
    TSRule([("e", negative_f_set), ("de", negative_f_set)], rule_one),
    TSRule([("e", zero_f_set), ("de", zero_f_set)], rule_two),
    TSRule([("e", positive_f_set), ("de", positive_f_set)], rule_three),
    TSRule([("e", zero_f_set), ("de", negative_f_set)], rule_four),
    TSRule([("e", positive_f_set), ("de", negative_f_set)], rule_five),
])

e_prev = 0.0
de_prev = 0.0
dt = 2  # 0.1 s
v_ref_arr = [3] * 11
v_measured_arr = [
    0.0, 0.5, 1.2, 2.0, 2.5,
    2.8, 2.95, 3.0, 3.0, 3.0, 3.0
]

for v_ref, v_measured in zip(v_ref_arr, v_measured_arr):
    e_curr = v_ref - v_measured
    de = (e_curr - e_prev) / dt

    control_res = controller.inference({"e": e_curr, "de": de})

    print(f"measured vel: {v_measured}\ntarget: {v_ref}\nerror: {e_curr:.2f}\nde: {de:.2f}\ncontrol res: {control_res:.2f}\n")

    e_prev = e_curr


temperature_f_set = FSet({
    "medium": 0.5,
    "warm": 0.8,
    "hot": 0.9,
    "boiling": 1
})

print(temperature_f_set)