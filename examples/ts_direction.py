from examples.direction_fuzzy import f_set_down, f_set_up, f_set_left, f_set_right, f_set_forward, f_set_backward
from examples.speed_fuzzy import f_set_slow, f_set_fast, f_set_moderate
from pyPRUF import TSControl, Rule

SLOW_SPEED = 2.5
MEDIUM_SPEED = 5
FAST_SPEED = 7.5

def go_slow(direction, _input):
    return direction * SLOW_SPEED

def go_medium(direction, _input):
    return direction * MEDIUM_SPEED

def go_fast(direction, _input):
    return direction * FAST_SPEED


controller_ud = TSControl([
    Rule([ ("direction", f_set_down), ("speed", f_set_slow) ], lambda x: go_slow(-1, x)),
    Rule([ ("direction", f_set_down), ("speed", f_set_moderate) ], lambda x: go_medium(-1, x)),
    Rule([ ("direction", f_set_down), ("speed", f_set_fast) ], lambda x: go_fast(-1, x)),

    Rule([ ("direction", f_set_up), ("speed", f_set_slow) ], lambda x: go_slow(1, x)),
    Rule([ ("direction", f_set_up), ("speed", f_set_moderate) ], lambda x: go_medium(1, x)),
    Rule([ ("direction", f_set_up), ("speed", f_set_fast) ], lambda x: go_fast(1, x)),
])

controller_rl = TSControl([
    Rule([ ("direction", f_set_left), ("speed", f_set_slow) ], lambda x: go_slow(-1, x)),
    Rule([ ("direction", f_set_left), ("speed", f_set_moderate) ], lambda x: go_medium(-1, x)),
    Rule([ ("direction", f_set_left), ("speed", f_set_fast) ], lambda x: go_fast(-1, x)),

    Rule([ ("direction", f_set_right), ("speed", f_set_slow) ], lambda x: go_slow(1, x)),
    Rule([ ("direction", f_set_right), ("speed", f_set_moderate) ], lambda x: go_medium(1, x)),
    Rule([ ("direction", f_set_right), ("speed", f_set_fast) ], lambda x: go_fast(1, x)),
])

controller_fb = TSControl([
    Rule([ ("direction", f_set_forward), ("speed", f_set_slow) ], lambda x: go_slow(1, x)),
    Rule([ ("direction", f_set_forward), ("speed", f_set_moderate) ], lambda x: go_medium(1, x)),
    Rule([ ("direction", f_set_forward), ("speed", f_set_fast) ], lambda x: go_fast(1, x)),

    Rule([ ("direction", f_set_backward), ("speed", f_set_slow) ], lambda x: go_slow(-1, x)),
    Rule([ ("direction", f_set_backward), ("speed", f_set_moderate) ], lambda x: go_medium(-1, x)),
    Rule([ ("direction", f_set_backward), ("speed", f_set_fast) ], lambda x: go_fast(-1, x)),
])

i = { "direction": "nord", "speed": "Immediato"}

rl, fb, ud = (0, 0, 0)

try:
    rl = controller_rl.inference(i)
except:
    pass

try:
    fb = controller_fb.inference(i)
except:
    pass

try:
    ud = controller_ud.inference(i)
except:
    pass


print(f"RES is {rl} _ {fb} _ {ud}")
