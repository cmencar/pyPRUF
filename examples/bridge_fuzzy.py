from examples.utils import get_f_set_from_csv

poor_foundation_cond_f_set = get_f_set_from_csv("data/bridge/poor_foundation_condition.csv", "Poor foundation condition", sep=",")
medium_foundation_cond_f_set = get_f_set_from_csv("data/bridge/medium_foundation_condition.csv", "Medium foundation condition", sep=",")
good_foundation_cond_f_set = get_f_set_from_csv("data/bridge/good_foundation_condition.csv", "Good foundation condition", sep=",")

poor_surrounding_cond_f_set = get_f_set_from_csv("data/bridge/poor_surrounding_condition.csv", "Poor surrounding condition", sep=",")
medium_surrounding_cond_f_set = get_f_set_from_csv("data/bridge/medium_surrounding_condition.csv", "Medium surrounding condition", sep=",")
good_surrounding_cond_f_set = get_f_set_from_csv("data/bridge/good_surrounding_condition.csv", "Good surrounding condition", sep=",")

low_changes_f_set = get_f_set_from_csv("data/bridge/low_changes_made.csv", "Low changes", sep=",")
moderate_changes_f_set = get_f_set_from_csv("data/bridge/moderate_changes_made.csv", "Medium changes", sep=",")
high_changes_f_set = get_f_set_from_csv("data/bridge/high_changes_made.csv", "High changes", sep=",")

low_doc_quality_f_set = get_f_set_from_csv("data/bridge/low_doc_quality.csv", "Low doc quality", sep=",")
moderate_doc_quality_f_set = get_f_set_from_csv("data/bridge/moderate_doc_quality.csv", "Medium doc quality", sep=",")
high_doc_quality_f_set = get_f_set_from_csv("data/bridge/high_doc_quality.csv", "High doc quality", sep=",")

poor_env_peculiarity_f_set = get_f_set_from_csv("data/bridge/poor_env_peculiarity.csv", "Poor env peculiarity", sep=",")
medium_env_peculiarity_f_set = get_f_set_from_csv("data/bridge/medium_env_peculiarity.csv", "Medium env peculiarity", sep=",")
high_env_peculiarity_f_set = get_f_set_from_csv("data/bridge/high_env_peculiarity.csv", "High env peculiarity", sep=",")

low_external_degradation_f_set = get_f_set_from_csv("data/bridge/low_external_degradation.csv", "Low external degradation", sep=",")
moderate_external_degradation_f_set = get_f_set_from_csv("data/bridge/moderate_external_degradation.csv", "Moderate external degradation", sep=",")
high_external_degradation_f_set = get_f_set_from_csv("data/bridge/high_external_degradation.csv", "High external degradation", sep=",")

low_maintenance_eff_f_set = get_f_set_from_csv("data/bridge/low_maintenance_eff.csv", "Low maintenance efficiency", sep=",")
moderate_maintenance_eff_f_set = get_f_set_from_csv("data/bridge/moderate_maintenance_eff.csv", "Moderate maintenance efficiency", sep=",")
high_maintenance_eff_f_set = get_f_set_from_csv("data/bridge/high_maintenance_eff.csv", "High maintenance efficiency", sep=",")

low_network_importance_f_set = get_f_set_from_csv("data/bridge/low_network_importance.csv", "Low network importance", sep=",")
moderate_network_importance_f_set = get_f_set_from_csv("data/bridge/moderate_network_importance.csv", "Moderate network importance", sep=",")
high_network_importance_f_set = get_f_set_from_csv("data/bridge/high_network_importance.csv", "High network importance", sep=",")

#
low_seismic_hazard_f_set = get_f_set_from_csv("data/bridge/low_seismic_hazard.csv", "Low seismic hazard", sep=",")
moderate_seismic_hazard_f_set = get_f_set_from_csv("data/bridge/moderate_seismic_hazard.csv", "Moderate seismic hazard", sep=",")
high_seismic_hazard_f_set = get_f_set_from_csv("data/bridge/high_seismic_hazard.csv", "High seismic hazard", sep=",")

low_static_load_f_set = get_f_set_from_csv("data/bridge/low_static_load.csv", "Low static load", sep=",")
moderate_static_load_f_set = get_f_set_from_csv("data/bridge/moderate_static_load.csv", "Moderate static load", sep=",")
high_static_load_f_set = get_f_set_from_csv("data/bridge/high_static_load.csv", "High static load", sep=",")

low_traffic_f_set = get_f_set_from_csv("data/bridge/low_traffic.csv", "Low traffic", sep=",")
moderate_traffic_f_set = get_f_set_from_csv("data/bridge/moderate_traffic.csv", "Moderate traffic", sep=",")
high_traffic_f_set = get_f_set_from_csv("data/bridge/high_traffic.csv", "High traffic", sep=",")