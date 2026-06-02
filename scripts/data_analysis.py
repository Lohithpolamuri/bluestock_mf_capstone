import pandas as pd

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

print("Category Counts:")
print(fund_master["category"].value_counts())

print("\nRisk Category Counts:")
print(fund_master["risk_category"].value_counts())

print("\nTop 5 Fund Houses:")
print(fund_master["fund_house"].value_counts().head())