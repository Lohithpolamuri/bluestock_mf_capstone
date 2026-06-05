import pandas as pd
import matplotlib.pyplot as plt

nav = pd.read_csv("../data/raw/02_nav_history.csv")
benchmark = pd.read_csv("../data/raw/10_benchmark_indices.csv")

nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

top_fund = nav["amfi_code"].unique()[0]

fund = nav[nav["amfi_code"] == top_fund]

plt.figure(figsize=(12,6))

plt.plot(
    fund["date"],
    fund["nav"],
    label="Fund"
)

for idx in ["NIFTY50", "NIFTY100"]:
    temp = benchmark[
        benchmark["index_name"] == idx
    ]

    plt.plot(
        temp["date"],
        temp["close_value"],
        label=idx
    )

plt.legend()
plt.title("Fund vs Benchmark Comparison")
plt.tight_layout()

plt.savefig(
    "../reports/benchmark_comparison_chart.png"
)

print("Chart saved successfully")