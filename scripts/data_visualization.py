import pandas as pd
import matplotlib.pyplot as plt

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

category_counts = fund_master["category"].value_counts()

plt.figure(figsize=(6,4))
category_counts.plot(kind="bar")

plt.title("Mutual Fund Categories")
plt.xlabel("Category")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("../reports/category_distribution.png")

print("Chart Saved Successfully!")