from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/")
def index():
    selected_map = request.args.get("map", "all")
    map_file = "cancer_heatmap.html" if selected_map == "cancer" else "heatmap.html"

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
            margin-top: 20px;
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
    <p style="text-align:center;">Visualizing mortality rate data (2014–2023) from NCHS datasets.</p>

    <div style="text-align:center;">
        <form method="get">
            <label for="map"><b>Select Map:</b></label>
            <select name="map" id="map" onchange="this.form.submit()">
                <option value="all" {'selected' if selected_map == 'all' else ''}>All Mortality</option>
                <option value="cancer" {'selected' if selected_map == 'cancer' else ''}>Cancer Mortality</option>
            </select>
        </form>
    </div>

    <h2>🗺️ Mortality Rate by State (Heat Map)</h2>
    <iframe src="/static/{map_file}" width="800" height="500" style="border:none;"></iframe>

    <h2>📉 Average Mortality Rate by Year</h2>
    <img src="/static/avg_rate_trend.png" width="650">

    <h2>🏆 Top 5 States by Rate (Latest Year)</h2>
    <img src="/static/top_states.png" width="650">

    <h2>📊 Cancer vs. All Mortality Comparison</h2>
    <img src="/static/compare_trend.png" width="750">

    <h2>📈 Correlation Heatmap</h2>
    <img src="/static/state_correlation.png" width="500">

    <div class="insight-section">
        <h2>🧠 Analysis & Key Insights</h2>

        <h3>1️⃣ National Mortality Trend</h3>
        <p>Mortality rates <span class="highlight">peaked in 2021</span> during the height of the COVID-19 pandemic, followed by a steady recovery through 2023.</p>

        <h3>2️⃣ Regional Differences</h3>
        <p><span class="highlight">Southern and Appalachian states</span> — including Kentucky, West Virginia, Tennessee, and Mississippi — consistently record higher mortality rates due to chronic illness prevalence and limited healthcare access.</p>

        <h3>3️⃣ Cancer vs. All-Cause Mortality</h3>
        <p>Cancer mortality remains a <span class="highlight">smaller but stable portion</span> of total mortality. The cancer trendline shows resilience even during pandemic years.</p>

        <h3>4️⃣ Correlation Between Rates</h3>
        <p>Strong positive correlation (r ≈ <span class="highlight">0.76</span>) between cancer and total mortality suggests shared socioeconomic and environmental risk factors.</p>

        <h3>5️⃣ Policy Takeaways</h3>
        <ul>
            <li>📉 National mortality is improving post-pandemic.</li>
            <li>🏥 Focused investment needed in high-mortality states.</li>
            <li>🧬 Strengthen screening and prevention programs.</li>
            <li>🌍 Address structural health inequities regionally.</li>
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
