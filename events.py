import glob
import json
import os

import requests
from tqdm import tqdm

data = "data"
base_url = "https://kulturerbe-import.burgtheater.at/api/api/v1/"
event_folder = os.path.join(data, "events")
calendar_folder = os.path.join(data, "calendar")
save_path = os.path.join(data, "events.json")
event_base_url = f"{base_url}performance/"

years = glob.glob(f"./{calendar_folder}/*.json")

ids = {}

for x in years:
    with open(x, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        for y in data:
            ids[y["_id"]] = y

with open(save_path, "w", encoding="utf-8") as fp:
    json.dump(ids, fp, ensure_ascii=False, indent=2)

print(f"{len(ids)=}")


for x in tqdm(data, total=len(data)):
    item_id = x["_id"]
    save_path = os.path.join(event_folder, f"{item_id}.json")
    if os.path.exists(save_path):
        print(f"{save_path} exists, skipping")
        continue
    else:
        url = f"{event_base_url}{item_id}"
        r = requests.get(url)
        data = r.json()
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
