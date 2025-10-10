import glob
import pandas as pd
import os

def test_data_integrity():
    """Verify that all data files contain numeric columns and are valid CSVs."""
    files = glob.glob("data/*.csv")
    assert files, "No CSV files found in data directory."

    for path in files:
        df = pd.read_csv(path)
        assert len(df) > 0, f"{path} is empty"

        if "data-table" in path or "cancer" in path or "mortality" in path:
            assert any(col.lower() == "rate" for col in df.columns), f"{path} missing RATE column"

        numeric_cols = df.select_dtypes(include=['number']).columns
        assert len(numeric_cols) > 0, f"{path} has no numeric columns"
