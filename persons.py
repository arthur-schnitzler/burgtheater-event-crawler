import glob
import json
import os

import requests
from tqdm import tqdm

from utils import data, event_folder, person_base_url, person_folder

files = glob.glob(f"{event_folder}/*.json")
save_path = os.path.join(data, "persons.json")


ids = {}

for x in tqdm(files):
    with open(x, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        for item in data["crew"]:
            ids[item["_id"]] = item
        for item in data["cast"]:
            ids[item["_id"]] = item
        for item in data["authors"]:
            ids[item["_id"]] = item

print(f"{len(ids)=}")

with open(save_path, "w", encoding="utf-8") as fp:
    json.dump(ids, fp, ensure_ascii=False, indent=2)

for key, x in tqdm(ids.items(), total=len(ids)):
    item_id = x["_id"]
    save_path = os.path.join(person_folder, f"{item_id}.json")
    if os.path.exists(save_path):
        print(f"{save_path} exists, skipping")
        continue
    else:
        url = f"{person_base_url}{item_id}"
        print(url)
        r = requests.get(url)
        data = r.json()
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
