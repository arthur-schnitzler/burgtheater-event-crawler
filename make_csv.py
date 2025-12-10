import json
import os

import pandas as pd

from utils import data

input_json = os.path.join(data, "persons.json")
output_csv = os.path.join(data, "persons.csv")

with open(input_json, "r", encoding="utf-8") as fp:
    data = json.load(fp)

items = data.values()

df = pd.DataFrame(items)
df["occupation"] = "Schauspieler"
df.to_csv(output_csv, index=False)
