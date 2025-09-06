import numpy as np

from pyPRUF import FSet, trap_mf

# price
fuzzy_low_price = FSet(
    mu=lambda x: trap_mf(x, 100, 100, 3000, 5000),
    index=np.arange(100, 5000, 100),
    name="Low price"
)

fuzzy_medium_price = FSet(
    mu=lambda x: trap_mf(x, 3500, 4000, 10000, 12000),
    index=np.arange(3500, 8000, 100),
    name="Medium price"
)

fuzzy_high_price = FSet(
    mu=lambda x: trap_mf(x, 10000, 13000, 50000, 50000),
    index=np.arange(10000, 50000, 100),
    name="High price"
)

# maintenance
fuzzy_low_maintenance = FSet(
    mu=lambda x: trap_mf(x, 50, 50, 200, 400),
    index=np.arange(50, 300, 50),
    name="Low maintenance price"
)

fuzzy_medium_maintenance = FSet(
    mu=lambda x: trap_mf(x, 200, 400, 800, 1000),
    index=np.arange(200, 1000, 50),
    name="Medium maintenance price"
)

fuzzy_high_maintenance = FSet(
    mu=lambda x: trap_mf(x, 800, 900, 10000, 10000),
    index=np.arange(800, 10000, 50),
    name="High maintenance price"
)

# mileage
fuzzy_low_mileage = FSet(
    mu=lambda x: trap_mf(x, 10000, 10000, 50000, 60000),
    index=np.arange(10000, 60000, 100),
    name="Low mileage"
)

fuzzy_medium_mileage = FSet(
    mu=lambda x: trap_mf(x, 60000, 70000, 90000, 120000),
    index=np.arange(60000, 120000, 100),
    name="Medium mileage"
)

fuzzy_high_mileage = FSet(
    mu=lambda x: trap_mf(x, 110000, 150000, 300000, 300000),
    index=np.arange(110000, 300000, 100),
    name="High mileage"
)

# Age
fuzzy_old_age = FSet(
    mu=lambda x: trap_mf(x, 10, 14, 50, 50),
    index=np.arange(11, 50, 1),
    name="Old car"
)

fuzzy_mid_age = FSet(
    mu=lambda x: trap_mf(x, 5, 6, 10, 12),
    index=np.arange(5, 12, 1),
    name="Mid Age car"
)

fuzzy_recent_age= FSet(
    mu=lambda x: trap_mf(x, 0, 0, 5, 6),
    index=np.arange(0, 6, 1),
    name="Recent car"
)

# Displacement
fuzzy_small_displacement = FSet(
    mu=lambda x: trap_mf(x, 0, 0, 1, 1.2),
    index=np.arange(0, 1.2, 0.1),
    name="Small displacement"
)

fuzzy_lower_medium_displacement = FSet(
    mu=lambda x: trap_mf(x, 1, 1.2, 1.4, 1.7),
    index=np.arange(1, 1.7, 0.1),
    name="Lower medium displacement"
)

fuzzy_upper_medium_displacement= FSet(
    mu=lambda x: trap_mf(x, 1.6, 1.8, 2, 2.3),
    index=np.arange(0, 6, 1),
    name="Upper medium displacement"
)

fuzzy_large_displacement= FSet(
    mu=lambda x: trap_mf(x, 2.2, 2.4, 7, 7),
    index=np.arange(2.2, 7, 0.1),
    name="Upper medium displacement"
)

# Efficient Consumption
fuzzy_very_efficient_consumption = FSet(
    mu=lambda x: trap_mf(x, 0, 0, 4, 4.5),
    index=np.arange(0, 4.5, 0.1),
    name="Very efficient consumption"
)

fuzzy_efficient_consumption = FSet(
    mu=lambda x: trap_mf(x, 4.2,  4.6, 5.5, 6.2),
    index=np.arange(4.2, 6.2, 0.1),
    name="Efficient consumption"
)

fuzzy_medium_consumption = FSet(
    mu=lambda x: trap_mf(x, 6, 7, 7.5, 8.2),
    index=np.arange(6, 8.2, 0.1),
    name="Medium consumption"
)

fuzzy_inefficient_consumption = FSet(
    mu=lambda x: trap_mf(x, 8, 8.4, 20, 20),
    index=np.arange(8, 20, 0.1),
    name="Inefficient consumption"
)

# Usage
fuzzy_low_usage = FSet(
    mu=lambda x: trap_mf(x, 0, 0, 1, 2),
    index=np.arange(0, 2, 1),
    name="Low usage"
)

fuzzy_medium_usage = FSet(
    mu=lambda x: trap_mf(x, 1,  3, 4, 5),
    index=np.arange(1, 5, 1),
    name="Medium usage"
)

fuzzy_high_usage = FSet(
    mu=lambda x: trap_mf(x, 3, 4, 10, 10),
    index=np.arange(3, 10, 1),
    name="High usage"
)

# Scratches
fuzzy_very_few_scratch = FSet(
    mu=lambda x: trap_mf(x, 0, 0, 2, 3),
    index=np.arange(0, 3, 1),
    name="Very Few scratches"
)

fuzzy_few_scratch = FSet(
    mu=lambda x: trap_mf(x, 1, 3, 4, 5),
    index=np.arange(1, 5, 1),
    name="Few scratches"
)

fuzzy_several_scratch = FSet(
    mu=lambda x: trap_mf(x, 4, 6, 8, 10),
    index=np.arange(1, 4, 10),
    name="Several scratches"
)

fuzzy_many_scratch = FSet(
    mu=lambda x: trap_mf(x, 7, 10, 40, 40),
    index=np.arange(7, 40, 1),
    name="Many scratches"
)

# Documentation
fuzzy_low_documentation = FSet(
    mu=lambda x: trap_mf(x, 0, 0, 4, 5),
    index=np.arange(0, 5, 1),
    name="Low documentation"
)

fuzzy_medium_documentation = FSet(
    mu=lambda x: trap_mf(x, 4, 6, 10, 12),
    index=np.arange(4, 10, 1),
    name="Medium documentation"
)

fuzzy_high_documentation = FSet(
    mu=lambda x: trap_mf(x, 11, 12, 40, 40),
    index=np.arange(11, 40, 1),
    name="High documentation"
)