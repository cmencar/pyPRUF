from examples.bridge_fuzzy import poor_foundation_cond_f_set, high_static_load_f_set, low_doc_quality_f_set, \
    good_surrounding_cond_f_set, high_traffic_f_set, high_changes_f_set, medium_foundation_cond_f_set, \
    moderate_external_degradation_f_set, high_env_peculiarity_f_set, low_static_load_f_set, high_maintenance_eff_f_set, \
    low_network_importance_f_set, high_seismic_hazard_f_set, moderate_traffic_f_set, low_external_degradation_f_set, \
    low_maintenance_eff_f_set, high_doc_quality_f_set, high_external_degradation_f_set, poor_surrounding_cond_f_set, \
    moderate_seismic_hazard_f_set, high_network_importance_f_set, good_foundation_cond_f_set, \
    medium_surrounding_cond_f_set, low_seismic_hazard_f_set, moderate_maintenance_eff_f_set, moderate_static_load_f_set, \
    moderate_network_importance_f_set
from pyPRUF import TSControl, TSRule

def rule_1_out(input):
    return 1.8 + (
        0.6 * poor_foundation_cond_f_set.mu(input["foundation"])
        + 0.5 * poor_surrounding_cond_f_set.mu(input["surroundings"])
        + 0.7 * high_seismic_hazard_f_set.mu(input["seismic"])
        + 0.4 * high_external_degradation_f_set.mu(input["external_deg"])
        - 0.3 * high_maintenance_eff_f_set.mu(input["maintenance"])
        - 0.2 * high_doc_quality_f_set.mu(input["doc_quality"])
    )

def rule_2_out(input):
    return  1.0 + (
        0.4 * low_doc_quality_f_set.mu(input["doc_quality"])
        - 0.5 * high_maintenance_eff_f_set.mu(input["maintenance"])
        + 0.2 * moderate_traffic_f_set.mu(input["traffic"])
        + 0.1 * moderate_static_load_f_set.mu(input["static_load"])
    )

def rule_3_out(input):
    return 1.5 + (
        0.45 * high_traffic_f_set.mu(input["traffic"])
        + 0.35 * high_static_load_f_set.mu(input["static_load"])
        + 0.25 * medium_foundation_cond_f_set.mu(input["foundation"])
        - 0.2 * high_maintenance_eff_f_set.mu(input["maintenance"])
    )

def rule_4_out(input):
    return 1.3 + (
        0.55 * high_changes_f_set.mu(input["changes"])
        + 0.4 * low_doc_quality_f_set.mu(input["doc_quality"])
        + 0.2 * high_env_peculiarity_f_set.mu(input["env_peculiarity"])
        - 0.15 * moderate_maintenance_eff_f_set.mu(input["maintenance"])
    )

def rule_5_out(input):
    return 0.7 + (
        - 0.4 * good_foundation_cond_f_set.mu(input["foundation"])
        - 0.3 * low_external_degradation_f_set.mu(input["external_deg"])
        - 0.35 * high_maintenance_eff_f_set.mu(input["maintenance"])
        + 0.2 * moderate_traffic_f_set.mu(input["traffic"])
    )

def rule_6_out(input):
    return 1.9 + (
        0.6 * high_network_importance_f_set.mu(input["network_importance"])
        + 0.7 * high_seismic_hazard_f_set.mu(input["seismic"])
        + 0.5 * high_external_degradation_f_set.mu(input["external_deg"])
        - 0.2 * moderate_maintenance_eff_f_set.mu(input["maintenance"])
    )

def rule_7_out(input):
    return 0.9 + (
        - 0.3 * good_surrounding_cond_f_set.mu(input["surroundings"])
        - 0.25 * low_static_load_f_set.mu(input["static_load"])
        + 0.15 * moderate_traffic_f_set.mu(input["traffic"])
    )

def rule_8_out(input):
    return 1.7 + (
        0.45 * poor_surrounding_cond_f_set.mu(input["surroundings"])
        + 0.4 * high_env_peculiarity_f_set.mu(input["env_peculiarity"])
        + 0.35 * high_traffic_f_set.mu(input["traffic"])
        - 0.25 * high_maintenance_eff_f_set.mu(input["maintenance"])
    )

def rule_9_out(input):
    return 0.8 + (
        - 0.35 * high_doc_quality_f_set.mu(input["doc_quality"])
        - 0.3 * high_maintenance_eff_f_set.mu(input["maintenance"])
        + 0.2 * medium_surrounding_cond_f_set.mu(input["surroundings"])
        + 0.1 * moderate_traffic_f_set.mu(input["traffic"])
    )

def rule_10_out(input):
    return 1.2 + (
        0.3 * moderate_external_degradation_f_set.mu(input["external_deg"])
        + 0.25 * moderate_traffic_f_set.mu(input["traffic"])
        + 0.2 * medium_foundation_cond_f_set.mu(input["foundation"])
        - 0.2 * moderate_maintenance_eff_f_set.mu(input["maintenance"])
    )

def rule_11_out(input):
    return 1.1 + (
        0.5 * low_doc_quality_f_set.mu(input["doc_quality"])
        - 0.6 * high_maintenance_eff_f_set.mu(input["maintenance"])
        + 0.15 * moderate_network_importance_f_set.mu(input["network_importance"])
    )

def rule_12_out(input):
    return 1.2 + (
        0.3 * medium_foundation_cond_f_set.mu(input["foundations"])
        + 0.4 * moderate_external_degradation_f_set.mu(input["external_deg"])
        + 0.35 * moderate_traffic_f_set.mu(input["traffic"])
        - 0.25 * moderate_maintenance_eff_f_set.mu(input["maintenance"])
    )

def rule_13_out(input):
    return 0.8 + (
        - 0.45 * good_surrounding_cond_f_set.mu(input["surroundings"])
        - 0.4 * low_static_load_f_set.mu(input["static_load"])
        - 0.5 * high_maintenance_eff_f_set.mu(input["maintenance"])
        + 0.2 * moderate_traffic_f_set.mu(input["traffic"])
    )

def rule_14_out(input):
    return 1.6 + (
        + 0.6 * high_changes_f_set.mu(input["changes"])
        + 0.5 * high_env_peculiarity_f_set.mu(input["env_peculiarity"])
        + 0.5 * low_doc_quality_f_set.mu(input["doc_quality"])
        - 0.2 * moderate_maintenance_eff_f_set.mu(input["maintenance"])
    )

def rule_15_out(input):
    return 1.0 + (
        + 0.6 * high_traffic_f_set.mu(input["traffic"])
        - 0.45 * low_network_importance_f_set.mu(input["network_importance"])
        - 0.6 * good_foundation_cond_f_set.mu(input["foundation"])
        + 0.25 * high_maintenance_eff_f_set.mu(input["maintenance"])
    )

ts_control = TSControl([
    TSRule([
        ("foundation", poor_foundation_cond_f_set), ("surroundings", poor_surrounding_cond_f_set),
        ("seismic", high_seismic_hazard_f_set)
    ], rule_1_out),
    TSRule([
        ("external_deg", high_external_degradation_f_set), ("maintenance", low_maintenance_eff_f_set)
    ], rule_2_out),
    TSRule([
        ("doc_quality", high_doc_quality_f_set), ("maintenance", high_maintenance_eff_f_set),
        ("surroundings", medium_surrounding_cond_f_set)
    ], rule_3_out),
    TSRule([
        ("static_load", high_static_load_f_set), ("traffic", high_traffic_f_set),
        ("foundation", medium_foundation_cond_f_set)
    ], rule_4_out),
    TSRule([
        ("network_importance", low_network_importance_f_set), ("static_load", low_static_load_f_set),
        ("seismic", low_seismic_hazard_f_set)
    ], rule_5_out),
    TSRule([
        ("changes", high_changes_f_set), ("doc_quality", low_doc_quality_f_set)
    ], rule_6_out),
    TSRule([
        ("surroundings", poor_surrounding_cond_f_set), ("env_peculiarity", high_env_peculiarity_f_set),
        ("traffic", high_traffic_f_set)
    ], rule_7_out),
    TSRule([
        ("foundation", good_foundation_cond_f_set), ("external_deg", low_external_degradation_f_set),
        ("maintenance", high_maintenance_eff_f_set)
    ], rule_8_out),
    TSRule([
        ("seismic", moderate_seismic_hazard_f_set), ("traffic", moderate_traffic_f_set),
        ("maintenance", moderate_maintenance_eff_f_set)
    ], rule_9_out),
    TSRule([
        ("network_importance", high_network_importance_f_set), ("seismic", high_seismic_hazard_f_set),
        ("external_deg", high_external_degradation_f_set)
    ], rule_10_out),
    TSRule([
        ("doc_quality", low_doc_quality_f_set), ("maintenance", high_maintenance_eff_f_set)
    ], rule_11_out),
    TSRule([
        ("foundation", medium_foundation_cond_f_set), ("external_deg", moderate_external_degradation_f_set),
        ("traffic", moderate_traffic_f_set)
    ], rule_12_out),
    TSRule([
        ("surroundings", good_surrounding_cond_f_set), ("static_load", low_static_load_f_set),
        ("maintenance", high_maintenance_eff_f_set)
    ], rule_13_out),
    TSRule([
        ("changes", high_changes_f_set), ("env_peculiarity", high_env_peculiarity_f_set),
        ("doc_quality", low_doc_quality_f_set)
    ], rule_14_out),
    TSRule([
        ("traffic", high_traffic_f_set), ("network_importance", low_network_importance_f_set),
        ("foundation", good_foundation_cond_f_set)
    ], rule_15_out),
])