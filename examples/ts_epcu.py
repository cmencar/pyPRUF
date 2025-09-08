from examples.epcu_fuzzy import low_complexity_f_set, short_term_f_set, high_t_experience_f_set, low_risk_f_set, \
    high_l_experience_f_set, high_motivation_f_set, low_size_f_set, moderate_complexity_f_set, high_complexity_f_set, \
    high_risk_f_set, low_t_experience_f_set, low_motivation_f_set, long_term_f_set, moderate_size_f_set, \
    moderate_l_experience_f_set, low_l_experience_f_set, moderate_risk_f_set, moderate_motivation_f_set
from pyPRUF import TSControl, Rule

def rule_1_out(input):
    return 0.6 + (
        0.8 * low_complexity_f_set.mu(input["complexity"])
        + 0.5 * short_term_f_set(input["duration"])
        + 0.9 * high_t_experience_f_set(input["tool_exp"])
        + 0.7 * low_risk_f_set.mu(input["risk"])
        + 0.9 * high_l_experience_f_set.mu(input["lead_exp"])
        + 0.8 * high_motivation_f_set.mu(input["motivation"])
        + 0.6 * low_size_f_set(input["size"])
    )

def rule_2_out(input):
    return 0.8 + (
        0.7 * moderate_complexity_f_set(input["complexity"])
        + 0.6 * high_t_experience_f_set(input["tool_exp"])
        + 0.7 * low_risk_f_set.mu(input["risk"])
        + 0.6 * high_l_experience_f_set.mu(input["lead_exp"])
    )

def rule_3_out(input):
    return 1.0 + (
        0.9 * low_complexity_f_set(input["complexity"])
        + 0.7 * high_t_experience_f_set(input["tool_exp"])
        + 0.7 * high_motivation_f_set.mu(input["motivation"])
        + 0.8 * high_l_experience_f_set.mu(input["lead_exp"])
    )

def rule_4_out(input):
    return 1.6 + (
        0.75 * high_risk_f_set.mu(input["risk"])
        + 0.6 * low_complexity_f_set.mu(input["complexity"])
        + 0.9 * low_t_experience_f_set.mu(input["tool_exp"])
    )

def rule_5_out(input):
    return 2.0 + (
        0.9 * low_l_experience_f_set.mu(input["lead_exp"])
        + 0.8 * low_complexity_f_set.mu(input["complexity"])
        + 0.7 * low_motivation_f_set.mu(input["motivation"])
    )

def rule_6_out(input):
    return 1.0 + (
        0.7 * long_term_f_set.mu(input["duration"])
        + 0.6 * low_risk_f_set.mu(input["risk"])
        + 0.8 * moderate_motivation_f_set.mu(input["motivation"])
    )

def rule_7_out(input):
    return 1.3 + (
        0.5 * low_complexity_f_set.mu(input["complexity"])
        + 0.6 * moderate_complexity_f_set.mu(input["complexity"])
        + 0.6 * moderate_motivation_f_set.mu(input["motivation"]) +
        0.7 * low_size_f_set(input["size"])
    )

def rule_8_out(input):
    return 1.0 + (
        0.85 * moderate_size_f_set(input["size"])
        + 0.75 * moderate_l_experience_f_set.mu(input["lead_exp"])
        + 0.7*high_t_experience_f_set.mu(input["tool_exp"])
    )

def rule_9_out(input):
    return  2.0 + (
        0.8 * long_term_f_set.mu(input["duration"])
        + 0.9 * high_risk_f_set.mu(input["risk"])
    )

def rule_10_out(input):
    return 1.0 + (
        0.85 * low_t_experience_f_set.mu(input["tool_exp"])
        + 0.9 * low_l_experience_f_set.mu(input["lead_exp"])
    )

def rule_11_out(input):
    return 0.8 + (
        0.7 * moderate_risk_f_set.mu(input["risk"])
        + 0.8 * high_motivation_f_set.mu(input["motivation"])
    )

def rule_12_out(input):
    return 0.8 + (
        0.7 * moderate_risk_f_set.mu(input["risk"])
        + 0.8 * high_motivation_f_set.mu(input["motivation"])
    )

def rule_13_out(input):
    return 0.8 + (
        0.7 * moderate_risk_f_set.mu(input["risk"])
        + 0.8 * high_motivation_f_set.mu(input["motivation"])
    )

def rule_14_out(input):
    return 1.6 + (
        0.9 * low_complexity_f_set.mu(input["complexity"])
        + 0.6 * moderate_l_experience_f_set.mu(input["lead_exp"])
    )

def rule_15_out(input):
    return 1.0 + (
        0.8 * moderate_complexity_f_set.mu(input["complexity"])
        + 0.85 * low_motivation_f_set.mu(input["motivation"])
    )

def rule_16_out(input):
    return  1.6 + (
        0.1 * short_term_f_set.mu(input["duration"])
        + 0.9*high_risk_f_set.mu(input["risk"])
    )


ts_epcu = TSControl([
    Rule([
        ( "complexity", low_complexity_f_set ), ( "duration", short_term_f_set ), ( "tool_exp", high_t_experience_f_set ),
        ( "risk", low_risk_f_set ), ( "lead_exp", high_l_experience_f_set ), ( "motivation", high_motivation_f_set ),
        ( "size", low_size_f_set )
    ], rule_1_out),
    Rule([
        ( "complexity", moderate_complexity_f_set ), ( "tool_exp", high_t_experience_f_set ),
        ( "risk", low_risk_f_set ), ( "lead_exp", high_l_experience_f_set )
    ], rule_2_out),
    Rule([
        ( "complexity", high_complexity_f_set ), ( "tool_exp", high_t_experience_f_set ),
        ( "motivation", high_motivation_f_set ), ( "lead_exp", high_l_experience_f_set ),
    ], rule_3_out),
    Rule([
        ( "risk", high_risk_f_set ), ( "complexity", high_complexity_f_set ),
        ( "tool_exp", low_t_experience_f_set )
    ], rule_4_out),
    Rule([
        ( "lead_exp", low_t_experience_f_set ), ( "complexity", high_complexity_f_set ),
        ( "motivation", low_motivation_f_set )
    ], rule_5_out),
    Rule([
        ( "duration", long_term_f_set ), ( "risk", low_risk_f_set ),
        ( "motivation", moderate_complexity_f_set )
    ], rule_6_out),
    Rule([
        ( "complexity", low_size_f_set ), ( "complexity", moderate_complexity_f_set ),
        ( "motivation", moderate_complexity_f_set )
    ], rule_7_out),
    Rule([
        ( "size", moderate_size_f_set ), ( "lead_exp", moderate_l_experience_f_set ),
        ( "tool_exp", high_t_experience_f_set )
    ], rule_8_out),
    Rule([
        ( "duration", moderate_size_f_set ), ( "risk", high_risk_f_set ),
    ], rule_9_out),
    Rule([
        ( "tool_exp", low_t_experience_f_set ), ( "lead_exp", low_l_experience_f_set ),
    ], rule_10_out),
    Rule([
        ( "risk", moderate_risk_f_set ), ( "motivation", high_motivation_f_set ),
    ], rule_11_out),
    Rule([
        ( "risk", moderate_risk_f_set ), ( "motivation", high_motivation_f_set ),
    ], rule_12_out),
    Rule([
        ( "risk", moderate_risk_f_set ), ( "motivation", high_motivation_f_set ),
    ], rule_13_out),
    Rule([
        ( "complexity", high_complexity_f_set ), ( "lead_exp", moderate_complexity_f_set ),
    ], rule_14_out),
    Rule([
        ( "complexity", moderate_complexity_f_set ), ( "motivation", low_motivation_f_set ),
    ], rule_15_out),
    Rule([
        ( "duration", short_term_f_set ), ( "risk", high_risk_f_set ),
    ], rule_16_out),
])