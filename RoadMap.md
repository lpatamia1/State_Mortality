## 🗺️ Project Roadmap

### ✅ Phase 1: Data Preparation
- [x] Collect raw mortality datasets from **NCHS / CDC**:
  - `data-table.csv` (All-Cause Mortality)
  - `cancer-deaths.csv` (Cancer Mortality)
  - `Provisional_COVID-19_Death_Counts_...csv` (COVID-19 Weekly Deaths)
- [x] Clean and normalize all numeric fields (`DEATHS`, `RATE`)
- [x] Convert state names → two-letter codes for mapping
- [x] Aggregate COVID data by year and state

---

### ✅ Phase 2: Analysis & Computation
- [x] Calculate **average mortality rates** by year and cause
- [x] Compute **correlation matrix** between all-cause and cancer mortality
- [x] Derive **Cancer Share %** and **COVID Share %** of total deaths
- [x] Identify **top 5 states** by cancer mortality
- [x] Scale and normalize rates (per 100,000 population)

---

### ✅ Phase 3: Visualization
- [x] Generate key charts with **Matplotlib & Seaborn**:
  - Trend line: All, Cancer, and COVID (2014–2023)
  - Mortality distribution comparison (KDE plots)
  - Correlation heatmap
  - Scatterplot: Cancer rate vs. death count
- [x] Create **interactive Plotly choropleths**:
  - All-Cause Heatmap
  - Cancer Heatmap
  - COVID-19 Heatmap (Peak 2021)
- [x] Export visuals as both `.html` (interactive) and `.png` (static)

---

### ✅ Phase 4: Web Integration (Flask)
- [x] Build Flask app to serve interactive dashboard
- [x] Add dropdown for map selection (All / Cancer / COVID)
- [x] Embed charts and insights in structured sections
- [x] Design responsive, clean layout with modern CSS styling

---

### 🚧 Phase 5: Deployment (Upcoming)
- [ ] Host dashboard on **Render**, **Railway**, or **Streamlit Cloud**
- [ ] Configure routes for `/static` and `/output` visualization files
- [ ] Add lightweight caching and error handling
- [ ] Optimize data loading for performance

---

### 🌱 Phase 6: Future Enhancements
- [ ] Integrate additional health metrics:
  - Chronic diseases (heart disease, diabetes)
  - Lung disease and smoking/vaping correlations
  - Mental health and substance-related deaths (opioids, alcohol)
  - Environmental and behavioral factors (air quality, obesity, inactivity)
- [ ] Add **year slider** for dynamic choropleth updates
- [ ] Build **API endpoints** for state-level queries
  → `/api/state/<state>` and `/api/year/<year>` returning JSON summaries
- [ ] Deploy a **live analytics dashboard** (Plotly Dash or Streamlit)
- [ ] Automate data updates from CDC/NCHS API and GitHub Actions
- [ ] Include demographic filters for health equity analysis
- [ ] Create downloadable reports summarizing key findings
- [ ] Incorporate real-time public health alerts or news feed integration
- [ ] Optimize visual design:
  - Accessible color palettes (color-blind friendly)
  - Hover tooltips with contextual insights
  - Regional clustering to highlight health inequities
- [ ] Add comparison dashboards:
  - State-to-state comparisons (e.g., IL vs KY)
  - Cause-to-cause correlations (e.g., Cancer vs Heart Disease)
- [ ] Host on a production server with analytics tracking and feedback form
---

### 🎯 Long-Term Vision
Create a **comprehensive U.S. Health Trends Dashboard** that:
- Combines mortality, chronic disease, and environmental health data
- Enables **interactive exploration** by state, year, and demographic
- Highlights **regional inequalities** and informs **public health policy**
