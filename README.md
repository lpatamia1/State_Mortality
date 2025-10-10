<div align="center">

# 🩺 State Mortality Dashboard (2020–2023)

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas Badge">
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly Badge">
</p>

<em>Visualizing U.S. mortality trends (2020–2023) using real CDC data.</em>

This small project visualizes U.S. state-level mortality data using Python, Pandas, and Flask. It loads real NCHS data, creates simple charts, and serves them in a minimal web app.

</div>

<p align="center">── ✿ ──</p>

<div align="center">

## 🚀 How to Run in Codespaces

</div>

1. Clone this repo or upload your files.
2. Open a terminal and install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the data analysis:
   ```bash
   python scripts/analyze_data.py
4. Start the Flask web app:
   ```bash
   python app.py
   
<p align="center">── ✿ ──</p>

<div align="center">

## 📊 Extended Summary

</div>

- This project expands on the initial mortality dashboard by integrating multi-year and multi-cause analyses.  
- The data reveal a steady national recovery after the pandemic, persistent regional disparities, and a strong correlation between total and cancer-specific mortality.
  
The following visuals summarize key patterns in mortality trends, causes, and regional disparities across the U.S. between 2014 and 2023.

<p align="center">── ✿ ──</p>

<p align="center">
  <svg width="70%" height="2">
    <line x1="0" y1="1" x2="100%" y2="1" stroke="#ffb6c1" stroke-width="2" />
  </svg>
</p>

<div align="center">

## Data Insights Summary & Visuals from Analysis
</div>

### 1️⃣ Average Mortality Rate (All Causes, Cancer, COVID-19)
<p align="center">
  <img src="https://raw.githubusercontent.com/lpatamia1/State_Mortality/main/static/compare_covid_trend.png" width="600" alt="Average Mortality Rate Trend">
  <br>
  <em>Figure 1. Comparative trend of all-cause, cancer, and COVID-19 mortality (2020–2023), showing the pandemic peak in 2021 and a steady decline in total and COVID-related deaths thereafter.</em>
</p>
  
The line chart shows a **sharp decline** in the average mortality rate from 2021 to 2023.  
- **2020–2021:** The mortality rate spiked significantly, reflecting the peak of the COVID-19 pandemic.  
- **2021–2023:** Rates dropped steeply, suggesting recovery and stabilization as the pandemic waned.  

**Key takeaway:** The data shows a clear **post-pandemic improvement** in mortality rates across the U.S.
| Year | Trend | Explanation |
|------|--------|-------------|
| 2020 | High | Early pandemic impact |
| 2021 | Peak | Height of pandemic mortality |
| 2022 | Decline | Vaccination and recovery phase |
| 2023 | Stabilized | Return to near pre-pandemic rates |

**Conclusion:**  
The dataset reflects a story of **crisis and recovery** — a national health rebound after COVID-19, with regional outliers that highlight ongoing inequality in access to care and preventive health outcomes.

---

### 2️⃣ Mortality Distribution (All, Cancer, COVID)
<p align="center"> <img src="https://raw.githubusercontent.com/lpatamia1/State_Mortality/main/static/distribution_comparison.png" width="600" alt="Distribution Comparison"> <br> <em>Figure 2. Mortality distribution across causes (all, cancer, COVID-19), showing the shift in leading contributors over time.</em> </p>

This visualization highlights how different causes contributed to total mortality during and after the pandemic.
- In **2021**, COVID-19 temporarily dominated mortality rates, overtaking several chronic disease categories.
- By **2023**, deaths attributed to COVID declined sharply, while cancer and other chronic diseases returned as the most consistent drivers of state-level mortality.
- The relative stability of cancer mortality contrasts the volatility of infectious disease spikes.

**Interpretation:** Chronic diseases remain a long-term concern, while pandemic-related deaths, though severe, were more transient. This comparison underscores how **chronic illness continues to shape public health beyond short-term crises**.

---

### 3️⃣ Top 5 Cancer Mortality States
<p align="center"> <img src="https://raw.githubusercontent.com/lpatamia1/State_Mortality/main/static/top_states.png" width="600" alt="Top 5 Mortality States"> <br> <em>Figure 3. Top five states by total mortality in 2023, highlighting ongoing regional disparities in chronic disease and healthcare access.</em> </p>

The bar chart highlights the five states with the highest mortality rates in 2023:
- **Kentucky (KY)**
- **West Virginia (WV)**
- **Tennessee (TN)**
- **New Mexico (NM)**
- **Mississippi (MS)**

These states, concentrated in the **Southern and Appalachian regions**, tend to have higher rates of chronic disease, poverty, and limited healthcare access.

**Key takeaway:** Persistent **regional health disparities** remain a challenge even as national averages improve.

---

### 4️⃣ All-Cause Mortality Heatmap
<p align="center"> <img src="https://raw.githubusercontent.com/lpatamia1/State_Mortality/main/static/heatmap.png" width="600" alt="All-Cause Heatmap"> <br> <em>Figure 4. All-cause mortality heatmap indicating gradual national improvement after 2021, with localized persistently high rates.</em> </p>

This map captures the broader trend of recovery after the pandemic. 
- States in the **Northeast and West Coast** show consistent declines in mortality after 2021.  
- **Southern and Midwestern** states continue to report elevated rates, driven by socioeconomic disparities, aging populations, and limited preventive care infrastructure.  
- The overall improvement demonstrates successful vaccination campaigns and improved health interventions, but also highlights where **structural inequities** continue to drive higher death rates.

**Insight:** The map reveals a nation healing unevenly — mortality improved nationally, yet pockets of vulnerability persist where access to healthcare remains limited.

---

### 5️⃣ Cancer Mortality Heatmap
<p align="center"> <img src="https://raw.githubusercontent.com/lpatamia1/State_Mortality/main/static/cancer_heatmap.png" width="600" alt="Cancer Heatmap"> <br> <em>Figure 5. Cancer mortality heatmap (2014–2023), showing persistent clusters of high cancer deaths in Appalachian and Southern states.</em> </p>

Cancer-related deaths remain **geographically consistent** across the dataset’s decade span.  
- **Kentucky, West Virginia, and Mississippi** rank among the highest each year.  
- Environmental exposures, smoking prevalence, and lower screening rates contribute to these outcomes.  
- Unlike COVID-related mortality, cancer deaths show **long-term stagnation**, indicating structural challenges in prevention and healthcare delivery.

**Key takeaway:** Even as infectious disease mortality improves, **chronic disease mortality highlights persistent, slow-moving inequities** that require sustained public health attention.

---

### 6️⃣ COVID-19 Mortality Heatmap (2021 Peak)
<p align="center"> <img src="https://raw.githubusercontent.com/lpatamia1/State_Mortality/main/static/covid_heatmap.png" width="600" alt="COVID-19 Heatmap"> <br> <em>Figure 6. COVID-19 mortality heatmap illustrating 2021 pandemic hotspots concentrated across the South and Southwest.</em> </p>
  
The heatmap clearly shows the 2021 peak of pandemic-related deaths, concentrated in states such as **Florida, Texas, and Louisiana**.  
- Areas with **low vaccination coverage and delayed mitigation policies** experienced disproportionately high mortality.  
- By late 2022, these rates dropped substantially as immunity increased through vaccination and prior infection.

**Key takeaway:** The map visualizes the pandemic’s sharp but temporary impact — a surge that tested healthcare systems but ultimately subsided faster than long-term chronic disease patterns.

---

## 🧠 Key Insights & Takeaways

- U.S. mortality **peaked in 2021** during the COVID-19 pandemic but **declined sharply by 2023**, signaling a strong national recovery.  
- **Chronic diseases** such as cancer remain stable, long-term contributors to mortality, emphasizing the need for ongoing prevention efforts.  
- **Regional disparities**—especially in the South and Appalachian regions—highlight persistent inequities in healthcare access and outcomes.  
- This project demonstrates how **data visualization can transform public health data into clear, empathy-driven insights**, connecting complex health trends to real-world impact.

---

<p align="center">
  <em>Data Source: National Center for Health Statistics (NCHS), CDC.  
  Analysis and visualization by Lily Patamia.</em>
</p>
