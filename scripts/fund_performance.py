"""
Fund Performance Module

Calculates and evaluates mutual fund performance metrics and returns.
"""


import pandas as pd
import numpy as np


performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

performance["return_rank"] = performance["return_3yr_pct"].rank(ascending=False)
performance["sharpe_rank"] = performance["sharpe_ratio"].rank(ascending=False)
performance["alpha_rank"] = performance["alpha"].rank(ascending=False)

performance["expense_rank"] = performance["expense_ratio_pct"].rank(ascending=True)

performance["drawdown_rank"] = performance["max_drawdown_pct"].rank(ascending=False)

performance["fund_score"] = (
    30 * (1 / performance["return_rank"]) +
    25 * (1 / performance["sharpe_rank"]) +
    20 * (1 / performance["alpha_rank"]) +
    15 * (1 / performance["expense_rank"]) +
    10 * (1 / performance["drawdown_rank"])
)

scorecard = performance[[
    "amfi_code",
    "scheme_name",
    "fund_score"
]].sort_values(
    by="fund_score",
    ascending=False
)

scorecard.to_csv(
    "../reports/fund_scorecard.csv",
    index=False
)

print("Fund Scorecard saved successfully")