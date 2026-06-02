import pandas as pd

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

print("Missing Values:")
print(fund_master.isnull().sum())

print("\nDuplicate Rows:")
print(fund_master.duplicated().sum())