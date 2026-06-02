import pandas as pd
import sqlite3

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

conn = sqlite3.connect("../data/db/mutual_funds.db")

fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

conn.close()