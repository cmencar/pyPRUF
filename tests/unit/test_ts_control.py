import unittest

from pyPRUF.fset import FSet
from pyPRUF.ts_control import TSControl, TSRule


def low_level(_any):
    return 50

def high_level(_any):
    return -50

class TestTSControl(unittest.TestCase):
    water_f_set_low = FSet({
        "altissimo": 0,
        "alto": 0.2,
        "medio": 0.5,
        "basso": 0.8,
        "bassissimo": 1,
    }, name="low_level_water")

    water_f_set_high = FSet({
        "altissimo": 1,
        "alto": 0.8,
        "medio": 0.5,
        "basso": 0.2,
        "bassissimo": 0,
    }, name="high_level_water")

    def test_rule(self):
        rule = TSRule([("wl_1", self.water_f_set_low), ("wl_2", self.water_f_set_low)], low_level)
        self.assertEqual(len(rule.rule_items), 2)
        self.assertEqual(rule.rule_items[0][0], "wl_1")
        self.assertEqual(rule.rule_items[1][0], "wl_2")

        firing_strength_prod = rule.firing_strength({
            "wl_1": "alto",
            "wl_2": "medio"
        })
        firing_strength_min = rule.firing_strength({
            "wl_1": "alto",
            "wl_2": "medio"
        }, "min")

        self.assertEqual(firing_strength_prod, 0.1)
        self.assertEqual(firing_strength_min, 0.2)

    def test_ts_control(self):
        ts_control = TSControl([
            TSRule([("wl", self.water_f_set_low)], low_level),
            TSRule([("wl", self.water_f_set_high)], high_level)
        ])

        self.assertEqual(len(ts_control.rules), 2)
        self.assertEqual(ts_control.rules[0].rule_items[0][0], "wl")
        self.assertEqual(ts_control.rules[1].rule_items[0][0], "wl")

        result_a = ts_control.inference({"wl": "medio"})
        result_b = ts_control.inference({"wl": "alto"})

        self.assertEqual(result_a, 0)
        self.assertEqual(result_b, -30)