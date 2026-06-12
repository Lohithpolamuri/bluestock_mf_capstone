"""
Data Ingestion Module

Loads and imports mutual fund datasets from source files into the project.
"""


import pandas as pd

print("Starting Data Ingestion...")

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")
nav_history = pd.read_csv("../data/raw/02_nav_history.csv")

print("\nFund Master Shape:", fund_master.shape)
print("NAV History Shape:", nav_history.shape)

print("\nFund Master Columns:")
print(fund_master.columns.tolist())

print("\nNAV History Columns:")
print(nav_history.columns.tolist())

print("\nData Loaded Successfully!")