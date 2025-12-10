import json
import os

import pandas as pd

from utils import data as data_folder

input_json = os.path.join(data_folder, "persons.json")
output_csv = os.path.join(data_folder, "persons.csv")

with open(input_json, "r", encoding="utf-8") as fp:
    data = json.load(fp)

items = data.values()

df = pd.DataFrame(items)
df["occupation"] = "Schauspieler"
df.to_csv(output_csv, index=False)


input_json = os.path.join(data_folder, "events.json")
output_csv = os.path.join(data_folder, "events.csv")

with open(input_json, "r", encoding="utf-8") as fp:
    data = json.load(fp)

items = data.values()

df = pd.DataFrame(items)
df = df.sort_values("date", ascending=True)
df.to_csv(output_csv, index=False)
