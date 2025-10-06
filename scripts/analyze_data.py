import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/data-table.csv")

# Clean numeric columns
df['DEATHS'] = df['DEATHS'].astype(str).str.replace(',', '').astype(float)
df['RATE'] = df['RATE'].astype(float)

# Print summary
print("Data Summary:")
print(df.describe())

# Average mortality rate by year
avg_rate = df.groupby('YEAR')['RATE'].mean().reset_index()

# Plot average rate trend
plt.figure(figsize=(8,5))
plt.plot(avg_rate['YEAR'], avg_rate['RATE'], marker='o')
plt.title('Average Mortality Rate by Year')
plt.xlabel('Year')
plt.ylabel('Average Rate')
plt.grid(True)
os.makedirs("static", exist_ok=True)
plt.savefig("static/avg_rate_trend.png")
plt.close()

# Top 5 states by rate in latest year
latest_year = df['YEAR'].max()
top_states = (
    df[df['YEAR'] == latest_year]
    .sort_values(by='RATE', ascending=False)
    .head(5)
)
plt.figure(figsize=(8,5))
plt.bar(top_states['STATE'], top_states['RATE'], color='salmon')
plt.title(f'Top 5 States by Rate in {latest_year}')
plt.ylabel('Rate')
plt.savefig("static/top_states.png")
plt.close()

print("✅ Charts saved in static/ folder.")
