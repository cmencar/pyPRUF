from pathlib import Path

import numpy as np
import pandas as pd

here = Path(__file__).parent

# costruisci il percorso completo del CSV
csv_path = here / "autos.csv"

cars = pd.read_csv(csv_path, nrows=10000)
cars.set_index("index", inplace=True)
cars = cars.drop(
    columns=[
        "seller", "offerType", "abtest", "vehicleType", "gearbox", "model", "monthOfRegistration",
        "fuelType", "brand", "notRepairedDamage", "dateCreated", "postalCode", "lastSeen", "dateCrawled"
    ]
)

cars.rename(columns={
    'yearOfRegistration': "year",
    "powerPS": "power",
    "nrOfPictures": "n_pictures",
    "kilometer": "mileage",

}, inplace=True)
cars["displacement"] = np.random.choice(np.arange(1, 7.1, 0.1), size=len(cars))
cars["consumption"] = np.random.choice(np.arange(3, 8.2, 0.1), size=len(cars))
cars["maintenance"] = np.random.choice(np.arange(100, 950, 50), size=len(cars))
cars["n_scratches"] = np.random.choice(np.arange(0, 12, 1), size=len(cars))
cars["n_owners"] = np.random.choice(np.arange(0, 5, 1), size=len(cars))

cars["price"] = cars["price"].apply(lambda col: int(np.round(col / 100) * 100))

