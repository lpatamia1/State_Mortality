# 🩺 State Mortality Dashboard — Makefile
# Automates setup, analysis, and running the Flask app

# --- DEFAULT ---
all: install analyze run
	@echo "🎉 State Mortality Dashboard ready at http://127.0.0.1:5000"

# --- VARIABLES ---
PYTHON := python3
APP := app.py
ANALYSIS := scripts/analyze_data.py
REQS := requirements.txt

# --- COMMANDS ---

install:
	@echo "📦 Installing Python dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r $(REQS)
	# Ensure compatibility for Plotly image export
	$(PYTHON) -m pip install kaleido==0.2.1 us	
	@echo "✅ Dependencies installed successfully."

analyze:
	@echo "📊 Running mortality data analysis..."
	$(PYTHON) $(ANALYSIS)
	@echo "✅ Data analysis completed. Results saved in /output and /static folders."

run:
	@echo "🚀 Starting Flask app..."
	$(PYTHON) $(APP)

clean:
	@echo "🧹 Cleaning up project..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "✅ Cleanup complete."
