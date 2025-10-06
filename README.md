# 🩺 State Mortality Dashboard (2020–2023)

This small project visualizes U.S. state-level mortality data using Python, Pandas, and Flask. It loads real NCHS data, creates simple charts, and serves them in a minimal web app.

## 🚀 How to Run in Codespaces

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
   
---

## 📈 Data Insights Summary

### 1️⃣ Average Mortality Rate by Year
The line chart shows a **sharp decline** in the average mortality rate from 2021 to 2023.  
- **2020–2021:** The mortality rate spiked significantly, reflecting the peak of the COVID-19 pandemic.  
- **2021–2023:** Rates dropped steeply, suggesting recovery and stabilization as the pandemic waned.  

**Key takeaway:** The data shows a clear **post-pandemic improvement** in mortality rates across the U.S.

---

### 2️⃣ Top 5 States by Rate in 2023
The bar chart highlights the five states with the highest mortality rates in 2023:
- **Kentucky (KY)**
- **West Virginia (WV)**
- **Tennessee (TN)**
- **New Mexico (NM)**
- **Mississippi (MS)**

These states, concentrated in the **Southern and Appalachian regions**, tend to have higher rates of chronic disease, poverty, and limited healthcare access.

**Key takeaway:** Persistent **regional health disparities** remain a challenge even as national averages improve.

---

### 3️⃣ Overall Interpretation
| Year | Trend | Explanation |
|------|--------|-------------|
| 2020 | High | Early pandemic impact |
| 2021 | Peak | Height of pandemic mortality |
| 2022 | Decline | Vaccination and recovery phase |
| 2023 | Stabilized | Return to near pre-pandemic rates |

**Conclusion:**  
The dataset reflects a story of **crisis and recovery** — a national health rebound after COVID-19, with regional outliers that highlight ongoing inequality in access to care and preventive health outcomes.
