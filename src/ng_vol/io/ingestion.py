import pandas as pd
from pathlib import Path

DATA_RAW = Path("data/raw")

def load_prices():
    return pd.read_csv(DATA_RAW / "ng_prices.csv", parse_dates=["date"]).set_index("date")

def load_curve():
    return pd.read_csv(DATA_RAW / "ng_futures_curve.csv", parse_dates=["date"]).set_index("date")

def load_storage():
    return pd.read_csv(DATA_RAW / "storage_eia_weekly.csv", parse_dates=["date"]).set_index("date")

def load_fundamentals():
    return pd.read_csv(DATA_RAW / "fundamentals_balances.csv", parse_dates=["date"]).set_index("date")

def load_weather():
    return pd.read_csv(DATA_RAW / "weather_degree_days.csv", parse_dates=["date"]).set_index("date")
