"""
Data Analysis Module

Performs exploratory data analysis and generates insights from mutual fund datasets.
"""


import pandas as pd
import matplotlib.pyplot as plt

performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

top_expense = performance.sort_values(
    by="expense_ratio_pct",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))
plt.bar(top_expense["scheme_name"], top_expense["expense_ratio_pct"])

plt.title("Top 10 Funds by Expense Ratio")
plt.xlabel("Scheme")
plt.ylabel("Expense Ratio (%)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("../reports/top_expense_ratio.png")

print("Chart saved successfully")