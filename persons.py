import glob
import json
import os

from tqdm import tqdm

from utils import data, event_folder

files = glob.glob(f"{event_folder}/*.json")
save_path = os.path.join(data, "persons.json")


ids = {}

for x in tqdm(files):
    with open(x, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        for production in data["productions"]:
            for person in production["cast"]:
                ids[person["_id"]] = person
            for person in production["crew"]:
                ids[person["_id"]] = person
            for person in production["authors"]:
                ids[person["_id"]] = person
print(f"{len(ids)=}")

with open(save_path, "w", encoding="utf-8") as fp:
    json.dump(ids, fp, ensure_ascii=False, indent=2)
