"""
Live NAV Fetch Module

Fetches and processes the latest NAV data for mutual fund schemes.
"""


import requests
import pandas as pd

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

print("Scheme Name:", data["meta"]["scheme_name"])

nav_df = pd.DataFrame(data["data"])

nav_df.to_csv("../data/raw/hdfc_live_nav.csv", index=False)

print("Live NAV saved successfully!")