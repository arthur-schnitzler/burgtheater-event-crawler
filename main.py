import requests
import os
import json


data = "data"
calendar_folder = os.path.join(data, "calendar")


years = range(1880, 1938)
base_url = "https://kulturerbe-import.burgtheater.at/api/api/v1/"
year_url = f"{base_url}calendar/"


def main():
    print("Hello from burgtherater-event-crawler!")
    for x in years:
        save_path = os.path.join(calendar_folder, f"{x}.json")
        url = f"{year_url}{x}"
        print(url)
        r = requests.get(url)
        data = r.json()
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
