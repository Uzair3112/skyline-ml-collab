# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 01 · EDA — Airline Passenger Satisfaction
#
# Exploratory analysis for **Module 05**. The raw CSVs are versioned with **DVC**, so run
# `dvc pull` before executing this notebook (they are never committed to git).
#
# The cleaning step lives in `src/ml_skyline/features.py` and is imported, not redefined —
# the notebook and the unit tests exercise the same code.
#
# Outputs are stripped on commit (nbstripout), so the PR diff stays text-only.

# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from ml_skyline.common import TARGET_INV_MAP, repo_path
from ml_skyline.features import SERVICE_COLUMNS, build_features
from ml_skyline.prepare import read_raw

sns.set_theme(style="whitegrid", context="notebook")
pd.set_option("display.max_columns", 40)

# %% [markdown]
# ## 1 · Load the raw data

# %%
raw_path = repo_path("data/raw/train.csv")
if not raw_path.exists():
    raise FileNotFoundError(f"{raw_path} is missing — run `dvc pull` first")

df = read_raw(raw_path)
print(f"rows = {df.shape[0]:,}   columns = {df.shape[1]}")
df.head()

# %% [markdown]
# ## 2 · Schema, missing values, duplicates

# %%
missing = df.isna().sum()
missing = missing[missing > 0]
print("columns with missing values:")
print(missing.to_string() if len(missing) else "  none")
print(f"duplicate rows : {df.duplicated().sum():,}")
print(f"dtypes         : {df.dtypes.value_counts().to_dict()}")
print(f"labels         : {sorted(df['satisfaction'].unique())}")
df.describe().T.head(8)

# %% [markdown]
# ## 3 · Target balance

# %%
target_share = df["satisfaction"].value_counts(normalize=True).sort_values()
print(target_share.round(4).to_string())

ax = target_share.plot.barh(figsize=(7, 2.2), title="Target balance")
ax.bar_label(ax.containers[0], fmt="{:.1%}")
ax.set_xlabel("share of rows")
plt.tight_layout()

# %% [markdown]
# ## 4 · Distributions of key features
#
# Age and flight distance are the main passenger numerics; the survey then rates 14
# service categories from 0 (worst) to 5 (best).

# %%
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
df["Age"].plot.hist(bins=30, ax=axes[0], title="Age")
df["Flight Distance"].plot.hist(bins=30, ax=axes[1], title="Flight distance")
plt.tight_layout()

# %%
service_means = df[list(SERVICE_COLUMNS)].mean().sort_values()
ax = service_means.plot.barh(figsize=(7, 5), title="Mean service rating (0-5)")
ax.set_xlabel("mean rating")
plt.tight_layout()

# %% [markdown]
# ## 5 · What moves satisfaction?
#
# `build_features` (unit-tested in `tests/test_features.py`) drops the id columns, imputes
# the missing arrival delays with the median and adds the row-wise `Service Score`.

# %%
features = build_features(df, target="satisfaction")
print(f"feature frame: {features.shape[0]:,} rows x {features.shape[1]} columns")
print(f"missing values after imputation: {int(features.isna().sum().sum())}")

# %%
corr = features.corr(numeric_only=True)["satisfaction"].drop("satisfaction")
corr = corr.reindex(corr.abs().sort_values(ascending=False).index)
ax = corr.head(10).plot.barh(figsize=(7, 4), title="Correlation with satisfaction")
ax.set_xlabel("Pearson r")
plt.tight_layout()

# %%
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
features.groupby("Class")["satisfaction"].mean().sort_values().plot.barh(
    ax=axes[0], title="Satisfied share by class"
)
features.groupby("Type of Travel")["satisfaction"].mean().sort_values().plot.barh(
    ax=axes[1], title="Satisfied share by travel type"
)
plt.tight_layout()

# %%
fig, ax = plt.subplots(figsize=(8, 3))
for label, group in features.groupby("satisfaction"):
    group["Service Score"].plot.hist(ax=ax, bins=30, alpha=0.55, label=TARGET_INV_MAP[int(label)])
ax.legend(title="satisfaction")
ax.set_xlabel("Service Score (mean of the 14 ratings)")
plt.tight_layout()

# %% [markdown]
# ## 6 · Conclusions
#
# 1. **Workable class balance** — 56.7 % neutral-or-dissatisfied vs 43.3 % satisfied, so
#    accuracy is a fair first metric without reweighting (the baseline of always guessing
#    the majority class is already 56.7 %).
# 2. **Service quality drives sentiment** — the strongest correlations with satisfaction are
#    `Online boarding` (0.50), the overall `Service Score` (0.50) and `Inflight
#    entertainment` (0.40); operational attributes barely matter (`Gate location` ≈ 0.00,
#    departure/arrival time convenience −0.05).
# 3. **Segment effect is large** — business/first-class and business-travel passengers are
#    satisfied at a much higher rate than economy/leisure passengers; any model that ignores
#    `Class` / `Type of Travel` would underperform.
# 4. **Data quality is good** — the only gaps are 310 missing `Arrival Delay in Minutes`
#    (0.30 % of rows), handled by the median imputation in `build_features`; no duplicate
#    rows, so no dedup step is needed.

# %%
summary = {
    "rows": int(df.shape[0]),
    "columns": int(df.shape[1]),
    "duplicate_rows": int(df.duplicated().sum()),
    "missing_arrival_delay": int(df["Arrival Delay in Minutes"].isna().sum()),
    "satisfied_share": round(float((df["satisfaction"] == "satisfied").mean()), 4),
    "strongest_correlations": corr.head(3).round(3).to_dict(),
    "weakest_correlations": corr.tail(3).round(3).to_dict(),
}
summary  # noqa: B018
