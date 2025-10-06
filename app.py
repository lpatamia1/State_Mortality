from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/")
def index():
    # get query parameter ?map=all or ?map=cancer
    selected_map = request.args.get("map", "all")

    # choose which heatmap file to show
    if selected_map == "cancer":
        map_file = "cancer_heatmap.html"
    else:
        map_file = "heatmap.html"

    html = f"""
    <h1>🩺 U.S. State Mortality Dashboard</h1>
    <p>Visualizing mortality rate data (2014–2023) from NCHS datasets.</p>

    <form method="get">
        <label for="map">Select Map:</label>
        <select name="map" id="map" onchange="this.form.submit()">
            <option value="all" {'selected' if selected_map == 'all' else ''}>All Mortality</option>
            <option value="cancer" {'selected' if selected_map == 'cancer' else ''}>Cancer Mortality</option>
        </select>
    </form>

    <h2>🗺️ Mortality Rate by State (Heat Map)</h2>
    <iframe src="/static/{map_file}" width="800" height="500" style="border:none;"></iframe>

    <h2>Average Mortality Rate by Year</h2>
    <img src="/static/avg_rate_trend.png" width="600">

    <h2>Top 5 States by Rate (Latest Year)</h2>
    <img src="/static/top_states.png" width="600">

    <h2>📊 Cancer vs. All Mortality Comparison</h2>
    <img src="/static/compare_trend.png" width="700">

    <h2>📈 Correlation Heatmap</h2>
    <img src="/static/state_correlation.png" width="500">

    <hr>
    <h3>🧠 Key Insight:</h3>
    <p>Dark red states represent higher mortality rates in the most recent year.
       Southern and Appalachian areas like Kentucky, West Virginia, and Mississippi remain persistent hotspots.</p>
    """

    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
