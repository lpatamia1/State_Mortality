from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    html = """
    <h1>🩺 U.S. State Mortality Dashboard</h1>
    <p>Visualizing mortality rate data (2020–2023) from data-table.csv.</p>
    <h2>Average Mortality Rate by Year</h2>
    <img src="/static/avg_rate_trend.png" width="600">
    <h2>Top 5 States by Rate (Latest Year)</h2>
    <img src="/static/top_states.png" width="600">
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
