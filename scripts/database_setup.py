import pandas as pd
import sqlite3

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

nav_history = pd.read_csv("../data/processed/02_nav_history_clean.csv")
scheme_performance = pd.read_csv("../data/processed/07_scheme_performance_clean.csv")
investor_transactions = pd.read_csv("../data/processed/08_investor_transactions_clean.csv")

conn = sqlite3.connect("../data/db/mutual_funds.db")

fund_master.to_sql("fund_master", conn, if_exists="replace", index=False)
nav_history.to_sql("nav_history", conn, if_exists="replace", index=False)
scheme_performance.to_sql("scheme_performance", conn, if_exists="replace", index=False)
investor_transactions.to_sql("investor_transactions", conn, if_exists="replace", index=False)

print("All tables loaded successfully!")

conn.close()