from flask import Flask, render_template_string, request
 
app = Flask(__name__) # pragma: no cover

@app.route("/") # pragma: no cover
def index():
    # Get the selected map option from the dropdown menu (default = all)
    selected_map = request.args.get("map", "all")

    # ✅ Add COVID-19 logic here
    if selected_map == "cancer":
        map_file = "cancer_heatmap.html"
    elif selected_map == "covid":
        map_file = "covid_heatmap.html"
    else:
        map_file = "heatmap.html"

    html = f"""
    <html>
    <head>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background-color: #f5f7fa;
            color: #222;
            margin: 0;
            padding: 20px 40px;
        }}
        h1 {{
            color: #004d7a;
            text-align: center;
        }}
        h2 {{
            color: #006f8e;
            border-bottom: 2px solid #00bcd4;
            padding-bottom: 4px;
            margin-top: 40px;
        }}
        h3 {{
            color: #004d7a;
        }}
        select {{
            padding: 6px;
            border-radius: 5px;
            border: 1px solid #bbb;
            background-color: #fff;
            font-size: 14px;
        }}
        iframe, img {{
            display: block;
            margin: 15px auto;
            border-radius: 10px;
            box-shadow: 0 0 8px rgba(0,0,0,0.15);
        }}
        ul {{
            line-height: 1.6;
        }}
        .insight-section {{
            background: #e3f2fd;
            border-left: 5px solid #2196f3;
            padding: 15px 20px;
            margin-top: 30px;
            border-radius: 8px;
        }}
        .highlight {{
            color: #d32f2f;
            font-weight: bold;
        }}
        footer {{
            text-align: center;
            font-size: 13px;
            color: #555;
            margin-top: 50px;
        }}
    </style>
    </head>
    <body>

    <h1>🩺 U.S. State Mortality Dashboard</h1>
    <p style="text-align:center;">Visualizing mortality data (2014–2023) from NCHS and CDC datasets.</p>

    <div style="text-align:center;">
        <form method="get">
            <label for="map"><b>Select Map:</b></label>
            <select name="map" id="map" onchange="this.form.submit()">
                <option value="all" {'selected' if selected_map == 'all' else ''}>All Mortality</option>
                <option value="cancer" {'selected' if selected_map == 'cancer' else ''}>Cancer Mortality</option>
                <option value="covid" {'selected' if selected_map == 'covid' else ''}>COVID-19 Mortality</option>
            </select>
        </form>
    </div>

    <h2>🗺️ Mortality Rate by State (Heat Map)</h2>
    <iframe src="/static/{map_file}" width="800" height="500" style="border:none;"></iframe>

    <h2>📉 Average Mortality Rate by Year (All, Cancer, and COVID-19)</h2>
    <img src="/static/compare_covid_trend.png" width="750">

    <h2>🏆 Top 5 States by Cancer Rate (Trend 2014–2023)</h2>
    <img src="/static/top_states.png" width="700">

    <h2>📊 Distribution of Mortality Rates (All vs. Cancer vs. COVID-19 – 2023 Comparison)</h2>
    <p style="text-align:center; font-size:13px; color:#555;">
        Comparison of 2023 mortality data; COVID-19 distribution reflects post-peak trends, while the map (below) shows the 2021 pandemic peak.
    </p>
    <img src="/static/distribution_comparison.png" width="700">

    <h2>🔬 Cancer Rate vs. Death Count</h2>
    <img src="/static/scatter_rate_deaths.png" width="650">

    <h2>📈 Correlation Between Cancer and All-Cause Rates</h2>
    <img src="/static/state_correlation.png" width="500">

    <h2>🧮 Cancer Share of Total Deaths by State</h2>
    <iframe src="/static/cancer_share.html" width="800" height="500" style="border:none;"></iframe>

    <div class="insight-section">
        <h2>🧠 Analysis & Key Insights</h2>

        <h3>1️⃣ National Mortality Trend</h3>
        <p>
            Mortality rates <span class="highlight">peaked in 2021</span> due to the COVID-19 pandemic.
            Both all-cause and COVID-specific deaths surged dramatically during this period,
            while cancer mortality remained steady. By 2023, deaths had declined nationally,
            signaling improved vaccine coverage and healthcare recovery.
        </p>

        <h3>2️⃣ Regional Differences</h3>
        <p>
            <span class="highlight">Southern and Appalachian states</span> — including Kentucky, West Virginia, Tennessee,
            and Mississippi — consistently record higher mortality rates due to a combination of
            chronic illness prevalence, limited healthcare access, economic hardship, and environmental stressors.
            Western and Northeastern states generally perform better, reflecting stronger preventive care systems
            and higher healthcare investment.
        </p>
        <h3>3️⃣ Cancer vs. All-Cause Mortality</h3>
        <p>
            Cancer mortality remains a <span class="highlight">smaller but stable portion</span> of total deaths nationwide.
            While total mortality fluctuated sharply during the pandemic, cancer-related rates stayed relatively steady.
            This suggests the persistence of long-term risk factors such as aging populations and delayed screenings,
            rather than acute health crises.
        </p>
        <h3>4️⃣ Correlation Between Rates</h3>
        <p>Strong positive correlation (r ≈ <span class="highlight">0.76</span>) between cancer and total mortality suggests shared socioeconomic and environmental risk factors. States with strong public health infrastructure show lower overlap in rates,
    emphasizing the role of systemic prevention and early intervention.</p>
       
        <h3>🧬 Cancer vs. COVID-19 Mortality</h3>
        <p>
            COVID-19 caused short-term spikes in mortality, while cancer remains a long-term challenge.
            Many states saw delayed screenings during the pandemic, highlighting the need for better
            healthcare continuity during crises.
        </p>

        <h3>5️⃣ Policy Takeaways</h3>
        <ul>
            <li>📉 National mortality is improving post-pandemic, but recovery remains uneven across regions.</li>
            <li>🏥 Focused investment needed in high-mortality states, especially across the rural South and Appalachia.</li>
            <li>🧬 Strengthen early screening, treatment access, and preventive programs targeting chronic diseases and cancers.</li>
            <li>🌍 Address structural health inequities through environmental justice, poverty reduction, and education programs.</li>
            <li>💧 Expand access to clean water, healthy food, and safe housing — critical environmental determinants of health.</li>
            <li>🌿 Support state-level data transparency initiatives to track mortality trends and guide community health planning.</li>
            <li>🧠 Promote cross-sector collaboration between healthcare, technology, and policy to modernize mortality surveillance.</li>
            <li>⚖️ Integrate social and environmental data into public health policy to identify at-risk populations more effectively.</li>
        </ul>
    </div>

    <footer>
        Data Source: National Center for Health Statistics (NCHS) <br>
        Visualization by <b>Lily Patamia</b>
    </footer>

    </body>
    </html>
    """

    return render_template_string(html)


if __name__ == "__main__": # pragma: no cover
    app.run(host="0.0.0.0", port=5000, debug=True)
