import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ✅ Ensure directories exist
os.makedirs("static", exist_ok=True)
os.makedirs("output", exist_ok=True)

# ✅ Load both datasets
df_all = pd.read_csv("data/data-table.csv")
df_cancer = pd.read_csv("data/cancer-deaths.csv")

# ✅ Clean and normalize numeric columns
for df in [df_all, df_cancer]:
    df["DEATHS"] = (
        df["DEATHS"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace(" ", "")
    )
    df["DEATHS"] = pd.to_numeric(df["DEATHS"], errors="coerce")
    df["RATE"] = pd.to_numeric(df["RATE"], errors="coerce")

# ✅ Scale all-cause mortality rates to per 100,000 if needed
mean_all = df_all["RATE"].mean(skipna=True)
if mean_all < 100:  # e.g. if average ~8–18
    print(f"⚙️ Scaling all-cause rates ×100 (mean before: {mean_all:.1f})")
    df_all["RATE"] *= 100

print(f"✅ Mean All-Cause RATE after scale: {df_all['RATE'].mean():.1f}")
print(f"✅ Mean Cancer RATE: {df_cancer['RATE'].mean():.1f}")

# ✅ Quick visual check (optional)
plt.figure(figsize=(8,5))
plt.hist(df_all["RATE"], bins=30, alpha=0.6, label="All Causes")
plt.hist(df_cancer["RATE"], bins=30, alpha=0.6, label="Cancer", color="red")
plt.legend()
plt.title("Distribution of Recorded Mortality Rates")
plt.xlabel("Mortality Rate (per 100,000)")
plt.ylabel("Number of States")
plt.show()

print("=== DEBUG SAMPLE VALUES ===")
print(df_all[["STATE", "YEAR", "RATE"]].head(10))
print("Mean all-cause rate:", df_all["RATE"].mean())
print(df_cancer[["STATE", "YEAR", "RATE"]].head(10))
print("Mean cancer rate:", df_cancer["RATE"].mean())

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
fig_cancer.write_image("static/cancer_heatmap.png")

import us  # pip install us

# ✅ Load CDC Provisional COVID-19 Mortality Data
df_covid = pd.read_csv("data/Provisional_COVID-19_Death_Counts_by_Week_Ending_Date_and_State_20251006.csv")

# Rename and keep only relevant columns
df_covid = df_covid.rename(columns={
    "State": "STATE",
    "COVID-19 Deaths": "DEATHS",
    "Week Ending Date": "WEEK_ENDING_DATE"
})

# Keep only weekly (not 'United States') data
df_covid = df_covid[df_covid["STATE"].ne("United States")]

# Extract year and clean up
df_covid["YEAR"] = pd.to_datetime(df_covid["WEEK_ENDING_DATE"], errors="coerce").dt.year
df_covid["DEATHS"] = pd.to_numeric(df_covid["DEATHS"], errors="coerce").fillna(0)

# Convert state names (e.g., 'California') to 2-letter codes for Plotly
# ✅ Convert state names to 2-letter abbreviations manually for full coverage
state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI',
    'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND',
    'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
    'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

df_covid["STATE"] = df_covid["STATE"].map(state_abbrev)

# Filter out non-state entries (territories, NYC, etc.)
df_covid = df_covid[df_covid["STATE"].notna()]

# Aggregate total yearly deaths per state
df_covid_yearly = df_covid.groupby(["YEAR", "STATE"])["DEATHS"].sum().reset_index()
# ✅ Load approximate 2021 state populations (in thousands)
state_pop = {
    "CA": 39538, "TX": 29145, "FL": 21538, "NY": 20201, "PA": 12803, "IL": 12588,
    "OH": 11799, "GA": 10736, "NC": 10488, "MI": 10077, "NJ": 9289, "VA": 8631,
    "WA": 7705, "AZ": 7151, "MA": 7029, "TN": 6911, "IN": 6786, "MO": 6163,
    "MD": 6177, "WI": 5894, "CO": 5774, "MN": 5706, "SC": 5210, "AL": 5030,
    "LA": 4658, "KY": 4512, "OR": 4246, "OK": 3973, "CT": 3606, "UT": 3340,
    "IA": 3190, "NV": 3139, "AR": 3021, "MS": 2961, "KS": 2938, "NM": 2127,
    "NE": 1961, "WV": 1794, "ID": 1839, "HI": 1460, "NH": 1389, "ME": 1360,
    "MT": 1084, "RI": 1096, "DE": 991, "SD": 887, "ND": 779, "AK": 732, "DC": 714,
    "VT": 645, "WY": 578
}

# ✅ Convert COVID deaths to per 100,000 population
df_covid_yearly["RATE"] = df_covid_yearly.apply(
    lambda x: (x["DEATHS"] / (state_pop.get(x["STATE"], 1000) * 1000)) * 100000,
    axis=1
)

print("Unique states:", df_covid["STATE"].unique())
print("Rows per year:", df_covid_yearly.groupby("YEAR")["STATE"].nunique())

# ✅ Compute yearly average for national comparison
avg_covid = (
    df_covid_yearly.groupby("YEAR")["DEATHS"]
    .mean()
    .reset_index()
    .rename(columns={"DEATHS": "RATE_Covid"})
)

# Merge with All vs. Cancer data for 3-line comparison chart
merged_covid = pd.merge(merged, avg_covid, on="YEAR", how="left")

plt.figure(figsize=(10, 6))
plt.plot(merged_covid["YEAR"], merged_covid["RATE_All"], label="All Causes", marker="o")
plt.plot(merged_covid["YEAR"], merged_covid["RATE_Cancer"], label="Cancer", marker="o", color="red")
plt.plot(merged_covid["YEAR"], merged_covid["RATE_Covid"], label="COVID-19", marker="o", color="purple")
plt.title("Average Mortality Rate: All Causes, Cancer, and COVID-19 (2014–2023)")
plt.xlabel("Year")
plt.ylabel("Mortality rate (per 100 000 population)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("static/compare_covid_trend.png")
plt.close()

# ✅ Create Choropleth Map for the Most Recent Year
# ✅ Use PEAK year (2021) for COVID heatmap visualization
peak_covid_year = 2021
covid_peak = df_covid_yearly[df_covid_yearly["YEAR"] == peak_covid_year]

print(f"COVID map year: {peak_covid_year}, rows: {len(covid_peak)}")

fig_covid = px.choropleth(
    covid_peak,
    locations="STATE",
    locationmode="USA-states",
    color="DEATHS",
    color_continuous_scale="Purples",
    scope="usa",
    title=f"COVID-19 Mortality by State (Peak Year: {peak_covid_year})"
)
fig_covid.write_html("static/covid_heatmap.html")
fig_covid.write_image("static/covid_heatmap.png")


print("✅ COVID-19 analysis complete! Added COVID visuals to /static/")

# ✅ 4️⃣ All-Cause Mortality Choropleth Map
all_latest = df_all[df_all["YEAR"] == latest_year]
fig_all = px.choropleth(
    all_latest,
    locations="STATE",
    locationmode="USA-states",
    color="RATE",
    color_continuous_scale="Blues",
    scope="usa",
    title=f"All-Cause Mortality Rate by State ({latest_year})"
)
fig_all.update_layout(coloraxis_colorbar_title="Rate per 100 000 population")
fig_all.write_html("static/heatmap.html")
fig_all.write_image("static/heatmap.png") 

# ✅ 5️⃣ Year-over-Year Trend (Top 5 States with Highest Cancer Mortality)
top5_states = (
    df_cancer[df_cancer["YEAR"] == latest_year]
    .sort_values("RATE", ascending=False)
    .head(5)["STATE"]
    .tolist()
)

trend_top5 = df_cancer[df_cancer["STATE"].isin(top5_states)]

plt.figure(figsize=(10, 6))
for state in top5_states:
    subset = trend_top5[trend_top5["STATE"] == state]
    plt.plot(subset["YEAR"], subset["RATE"], marker="o", label=state)
plt.title(f"Top 5 States by Cancer Mortality Trend (2014–{latest_year})")
plt.xlabel("Year")
plt.ylabel("Cancer Mortality Rate")
plt.legend(title="State", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("static/top_states.png")
plt.close()

# ✅ 6️⃣ Mortality Distribution Comparison (All vs. Cancer vs. COVID)
plt.figure(figsize=(10, 6))
sns.kdeplot(df_all[df_all["YEAR"] == latest_year]["RATE"], label="All Causes", fill=True)
sns.kdeplot(df_cancer[df_cancer["YEAR"] == latest_year]["RATE"], label="Cancer", fill=True, color="red")

# Use 2023 for baseline comparison, but COVID from 2021 (peak)
covid_compare = df_covid_yearly[df_covid_yearly["YEAR"] == 2021]
if "RATE" in covid_compare.columns:
    sns.kdeplot(covid_compare["RATE"], label="COVID-19 (2021 Peak)", fill=True, color="purple")

plt.title(f"Distribution of Mortality Rates (All, Cancer, COVID-19)")
plt.xlabel("Mortality Rate (per 100,000)")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.savefig("static/distribution_comparison.png")
plt.close()

# ✅ 7️⃣ Cancer Rate vs. Death Count Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=cancer_latest,
    x="RATE",
    y="DEATHS",
    hue="STATE",
    palette="Spectral",
    s=80,
    legend=False
)
plt.title(f"Cancer Mortality Rate vs. Death Count ({latest_year})")
plt.xlabel("Mortality Rate")
plt.ylabel("Number of Deaths")
plt.tight_layout()
plt.savefig("static/scatter_rate_deaths.png")
plt.close()

# ✅ 8️⃣ Cancer Share of All Deaths per State
merged_full = pd.merge(
    df_all[df_all["YEAR"] == latest_year][["STATE", "DEATHS"]],
    df_cancer[df_cancer["YEAR"] == latest_year][["STATE", "DEATHS"]],
    on="STATE",
    suffixes=("_All", "_Cancer")
)
merged_full = merged_full.dropna(subset=["DEATHS_All", "DEATHS_Cancer"])
merged_full["Cancer_Share_%"] = (merged_full["DEATHS_Cancer"] / merged_full["DEATHS_All"]) * 100

# ✅ Add COVID-19 deaths (2023) for comparison
covid_latest_year = 2023  # use 2023 since that’s your dashboard comparison year
df_covid_2023 = df_covid_yearly[df_covid_yearly["YEAR"] == covid_latest_year][["STATE", "DEATHS"]].rename(columns={"DEATHS": "DEATHS_Covid"})

# Merge COVID deaths into existing dataframe
merged_full = pd.merge(merged_full, df_covid_2023, on="STATE", how="left")

# Compute COVID share relative to all deaths
merged_full["Covid_Share_%"] = (merged_full["DEATHS_Covid"] / merged_full["DEATHS_All"]) * 100
merged_full = merged_full.fillna(0)

fig_share = px.bar(
    merged_full.sort_values("Cancer_Share_%", ascending=False),
    x="STATE",
    y=["Cancer_Share_%", "Covid_Share_%"],  # show both shares
    barmode="group",
    title=f"Cancer vs COVID-19 Share of Total Deaths by State ({latest_year})",
    labels={"value": "Share of Total Deaths (%)", "variable": "Cause"}
)
fig_share.update_layout(
    legend_title_text="Cause of Death",
    coloraxis_showscale=False,
    bargap=0.25,
    plot_bgcolor="white"
)
fig_share.write_html("static/cancer_share.html")

# ✅ 9️⃣ Summary Statistics Export
summary_stats = {
    "Average_All": round(merged["RATE_All"].mean(), 2),
    "Average_Cancer": round(merged["RATE_Cancer"].mean(), 2),
    "Correlation": round(corr.loc["All_Rate", "Cancer_Rate"], 2),
    "Top_5_States": ", ".join(top5_states)
}
pd.DataFrame([summary_stats]).to_csv("output/summary_stats.csv", index=False)

print("✅ Extended analysis complete! All visuals saved in /static/ and summary in /output/")
