import pandas as pd

# Load datasets
nav_df = pd.read_csv("../data/raw/02_nav_history.csv")
txn_df = pd.read_csv("../data/raw/08_investor_transactions.csv")
perf_df = pd.read_csv("../data/raw/07_scheme_performance.csv")

print("Files loaded successfully")

# ==========================
# NAV HISTORY CLEANING
# ==========================

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)

nav_df = nav_df.drop_duplicates()

nav_df = nav_df[nav_df["nav"] > 0]

print("NAV cleaned")

# ==========================
# INVESTOR TRANSACTIONS
# ==========================

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .str.strip()
    .str.title()
)

txn_df = txn_df[txn_df["amount_inr"] > 0]

print("Transactions cleaned")

# ==========================
# SCHEME PERFORMANCE
# ==========================

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

print("Performance cleaned")

# ==========================
# SAVE CLEANED FILES
# ==========================

nav_df.to_csv(
    "../data/processed/02_nav_history_clean.csv",
    index=False
)

txn_df.to_csv(
    "../data/processed/08_investor_transactions_clean.csv",
    index=False
)

perf_df.to_csv(
    "../data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("All cleaned files saved successfully")