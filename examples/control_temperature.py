import numpy as np

from pyPRUF import FSet, trapf, trimf
from pyPRUF import TSControl, Rule

bg_negative_fs = FSet(
    mu=lambda x: trapf(x, -10, -10, -7.5, -5),
    index=np.arange(-10, -4, 0.5)
)

sm_negative_fs = FSet(
    mu=lambda x: trapf(x, -7.5, -5, -2, 0),
    index=np.arange(-7.5, 0, 0.5)
)

zero_fs = FSet(
    mu=lambda x: trimf(x, -2, 0, 2),
    index=np.arange(-2, 2, 0.5)
)

sm_positive_fs = FSet(
    mu=lambda x: trapf(x, 0, 2, 5, 7.5),
    index=np.arange(0, 7.5, 0.5)
)

bg_positive_fs = FSet(
    mu=lambda x: trapf(x, 5, 7.5, 10, 10),
    index=np.arange(5, 10, 0.5)
)

def out_temp(a, b, c, ee, e):
    return a * e + b * ee + c

def rule_1_out(input_c):
    return out_temp(20, 18, 15, input_c["ee"], input_c["e"])

def rule_2_out(input_c, *other):
    return out_temp(15, 13, 10, input_c["ee"], input_c["e"])

def rule_3_out(input_c):
    return out_temp(10, 8, 5, input_c["ee"], input_c["e"])

def rule_4_out(input_c):
    return out_temp(5, 3, 0, input_c["ee"], input_c["e"])

def rule_5_out(input_c):
    return out_temp(0, -2, -5, input_c["ee"], input_c["e"])

ts_control = TSControl([
    Rule( [ ("e", bg_negative_fs), ("ee", bg_negative_fs) ], rule_1_out ),
    Rule( [ ("e", sm_negative_fs), ("ee", zero_fs) ], rule_2_out ),
    Rule( [ ("e", zero_fs), ("ee", zero_fs) ], rule_3_out ),
    Rule( [ ("e", sm_positive_fs), ("ee", zero_fs) ], rule_4_out ),
    Rule( [ ("e", bg_positive_fs), ("ee", bg_positive_fs) ], rule_5_out ),
])

res = ts_control.calculate({
    "e": -8,
    "ee": -6
})

print(res)