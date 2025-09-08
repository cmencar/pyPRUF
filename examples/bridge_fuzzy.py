from examples.epcu_fuzzy import get_series_from_csv, get_f_set_from_csv

poor_foundation_cond_f_set = get_f_set_from_csv("data/bridge/poor_foundation_condition.csv", "Poor foundation condition")
medium_foundation_cond_f_set = get_f_set_from_csv("data/bridge/medium_foundation_condition.csv", "Medium foundation condition")
good_foundation_cond_f_set = get_f_set_from_csv("data/bridge/good_foundation_condition.csv", "Good foundation condition")

poor_surrounding_cond_f_set = get_f_set_from_csv("data/bridge/poor_surrounding_condition.csv", "Poor surrounding condition")
medium_surrounding_cond_f_set = get_f_set_from_csv("data/bridge/medium_surrounding_condition.csv", "Medium surrounding condition")
good_surrounding_cond_f_set = get_f_set_from_csv("data/bridge/good_surrounding_condition.csv", "Good surrounding condition")

low_changes_f_set = get_f_set_from_csv("data/bridge/low_changes_made.csv", "Low changes")
moderate_changes_f_set = get_f_set_from_csv("data/bridge/moderate_changes_made.csv", "Medium changes")
high_changes_f_set = get_f_set_from_csv("data/bridge/high_changes_made.csv", "High changes")

low_doc_quality_f_set = get_f_set_from_csv("data/bridge/low_doc_quality.csv", "Low doc quality")
moderate_doc_quality_f_set = get_f_set_from_csv("data/bridge/moderate_doc_quality.csv", "Medium doc quality")
high_doc_quality_f_set = get_f_set_from_csv("data/bridge/high_doc_quality.csv", "High doc quality")

poor_env_peculiarity_f_set = get_f_set_from_csv("data/bridge/poor_env_peculiarity.csv", "Poor env peculiarity")
medium_env_peculiarity_f_set = get_f_set_from_csv("data/bridge/medium_env_peculiarity.csv", "Medium env peculiarity")
high_env_peculiarity_f_set = get_f_set_from_csv("data/bridge/high_env_peculiarity.csv", "High env peculiarity")

low_external_degradation_f_set = get_f_set_from_csv("data/bridge/low_external_degradation.csv", "Low external degradation")
moderate_external_degradation_f_set = get_f_set_from_csv("data/bridge/moderate_external_degradation.csv", "Moderate external degradation")
high_external_degradation_f_set = get_f_set_from_csv("data/bridge/high_external_degradation.csv", "High external degradation")

low_maintenance_eff_f_set = get_f_set_from_csv("data/bridge/low_maintenance_eff.csv", "Low maintenance efficiency")
moderate_maintenance_eff_f_set = get_f_set_from_csv("data/bridge/moderate_maintenance_eff.csv", "Moderate maintenance efficiency")
high_maintenance_eff_f_set = get_f_set_from_csv("data/bridge/high_maintenance_eff.csv", "High maintenance efficiency")

low_network_importance_f_set = get_f_set_from_csv("data/bridge/low_network_importance.csv", "Low network importance")
moderate_network_importance_f_set = get_f_set_from_csv("data/bridge/moderate_network_importance.csv", "Moderate network importance")
high_network_importance_f_set = get_f_set_from_csv("data/bridge/high_network_importance.csv", "High network importance")

low_seismic_hazard_series = get_series_from_csv("data/bridge/low_seismic_hazard.csv")
moderate_seismic_hazard_series = get_series_from_csv("data/bridge/moderate_seismic_hazard.csv")
high_seismic_hazard_series = get_series_from_csv("data/bridge/high_seismic_hazard.csv")

low_seismic_hazard_f_set = get_f_set_from_csv("data/bridge/low_seismic_hazard.csv", "Low seismic hazard")
moderate_seismic_hazard_f_set = get_f_set_from_csv("data/bridge/moderate_seismic_hazard.csv", "Moderate seismic hazard")
high_seismic_hazard_f_set = get_f_set_from_csv("data/bridge/high_seismic_hazard.csv", "High seismic hazard")

low_static_load_f_set = get_f_set_from_csv("data/bridge/low_static_load.csv", "Low static load")
moderate_static_load_f_set = get_f_set_from_csv("data/bridge/moderate_static_load.csv", "Moderate static load")
high_static_load_f_set = get_f_set_from_csv("data/bridge/high_static_load.csv", "High static load")

low_traffic_f_set = get_f_set_from_csv("data/bridge/low_traffic.csv", "Low traffic")
moderate_traffic_f_set = get_f_set_from_csv("data/bridge/moderate_traffic.csv", "Moderate traffic")
high_traffic_f_set = get_f_set_from_csv("data/bridge/high_traffic.csv.csv", "High traffic")