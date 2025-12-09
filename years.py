import json
import os

import requests

from utils import calendar_folder, year_range, year_url

for x in year_range:
    save_path = os.path.join(calendar_folder, f"{x}.json")
    url = f"{year_url}{x}"
    print(url)
    r = requests.get(url)
    data = r.json()
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
