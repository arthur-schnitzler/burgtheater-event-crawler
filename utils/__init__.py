import glob
import os

data = "data"
base_url = "https://kulturerbe-import.burgtheater.at/api/api/v1/"
event_base_url = f"{base_url}performance/"
person_base_url = f"{base_url}person/"
calendar_folder = os.path.join(data, "calendar")
event_folder = os.path.join(data, "events")
person_folder = os.path.join(data, "persons")
calendar_folder = os.path.join(data, "calendar")
year_range = range(1880, 1938)
years = glob.glob(f"./{calendar_folder}/*.json")
year_url = f"{base_url}calendar/"
