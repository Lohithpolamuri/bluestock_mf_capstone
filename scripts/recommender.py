"""
Fund Recommendation Module

Generates mutual fund recommendations based on performance and risk metrics.
"""


import pandas as pd

scheme = pd.read_csv("../data/raw/07_scheme_performance.csv")

risk_level = "High"

recommendations = (
    scheme[scheme['risk_grade'] == risk_level]
    .sort_values('sharpe_ratio', ascending=False)
    [['scheme_name', 'sharpe_ratio']]
    .head(3)
)

print("Top 3 Recommended Funds:")
print(recommendations)