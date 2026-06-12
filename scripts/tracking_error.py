"""
Tracking Error Module

Calculates tracking error between mutual funds and benchmark indices.
"""


import pandas as pd
import numpy as np

nav = pd.read_csv("../data/raw/02_nav_history.csv")
benchmark = pd.read_csv("../data/raw/10_benchmark_indices.csv")

nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

fund = nav[nav["amfi_code"] == nav["amfi_code"].unique()[0]].copy()

fund["fund_return"] = fund["nav"].pct_change()

nifty50 = benchmark[benchmark["index_name"] == "NIFTY50"].copy()
nifty50["benchmark_return"] = nifty50["close_value"].pct_change()

merged = pd.merge(
    fund[["date", "fund_return"]],
    nifty50[["date", "benchmark_return"]],
    on="date"
)

tracking_error = (
    np.std(
        merged["fund_return"] -
        merged["benchmark_return"]
    ) * np.sqrt(252)
)

print("Tracking Error:", tracking_error)