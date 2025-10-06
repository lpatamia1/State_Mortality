import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load both datasets
df_all = pd.read_csv("data/data-table.csv")
df_cancer = pd.read_csv("data/cancer-deaths.csv")

# ✅ 1️⃣ Average Mortality Rate Comparison (All vs. Cancer)
avg_all = df_all.groupby("YEAR")["RATE"].mean().reset_index()
avg_cancer = df_cancer.groupby("YEAR")["RATE"].mean().reset_index()

merged = pd.merge(avg_all, avg_cancer, on="YEAR", suffixes=("_All", "_Cancer"))

plt.figure(figsize=(10, 6))
plt.plot(merged["YEAR"], merged["RATE_All"], label="All Causes", marker="o")
plt.plot(merged["YEAR"], merged["RATE_Cancer"], label="Cancer", marker="o", color="red")
plt.title("Average Mortality Rate: All Causes vs. Cancer (2014–2023)")
plt.xlabel("Year")
plt.ylabel("Average Rate")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("static/compare_trend.png")
plt.close()

# ✅ 2️⃣ Correlation Heatmap (Latest Year)
latest_year = df_all["YEAR"].max()
df_all_latest = df_all[df_all["YEAR"] == latest_year][["STATE", "RATE"]].rename(columns={"RATE": "All_Rate"})
df_cancer_latest = df_cancer[df_cancer["YEAR"] == latest_year][["STATE", "RATE"]].rename(columns={"RATE": "Cancer_Rate"})

merged_states = pd.merge(df_all_latest, df_cancer_latest, on="STATE")
corr = merged_states[["All_Rate", "Cancer_Rate"]].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title(f"Correlation between Cancer and All Mortality Rates ({latest_year})")
plt.tight_layout()
plt.savefig("static/state_correlation.png")
plt.close()

# ✅ 3️⃣ Cancer Mortality Choropleth Map
cancer_latest = df_cancer[df_cancer["YEAR"] == df_cancer["YEAR"].max()]
fig_cancer = px.choropleth(
    cancer_latest,
    locations="STATE",
    locationmode="USA-states",
    color="RATE",
    color_continuous_scale="Reds",
    scope="usa",
    title=f"Cancer Mortality Rate by State ({latest_year})"
)
fig_cancer.write_html("static/cancer_heatmap.html")

print("✅ Analysis complete! Visuals saved in /static/")
