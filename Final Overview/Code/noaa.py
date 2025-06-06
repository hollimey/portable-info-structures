from flask import Flask, render_template
import pandas as pd
import requests
from io import StringIO

app = Flask(__name__)

def fetch_noaa_data():
    url = "https://www.ndbc.noaa.gov/data/latest_obs/latest_obs.txt"
    response = requests.get(url)
    raw_data = response.text

    # Remove comment lines starting with '#'
    lines = [line for line in raw_data.splitlines() 
             if not line.startswith('#') 
             and line.strip()]
    
    if len(lines) < 2:
        return pd.DataFrame()
    
    header_line = lines[0]
    column_names = [
        "Station #", "LAT", "LON", "YYYY", "MM", "DD", "HH", "MM", 
        "WDIR", "WSPD", "GST", "WVHT", "DPD", "APD", "MWD", "PRES", 
        "ATMP", "WTMP", "DEWP", "VIS", "TIDE"
    ]
    
    data_lines = lines[1:]  # All rows after the header line

    records = []
    for line in data_lines:
        parts = line.strip().split()
        if len(parts) >= len(column_names):
            record = parts[:len(column_names)]
            records.append(record)
    
    df = pd.DataFrame(records, columns=column_names)

    # Only allows 19 variables, unknown why
    # Drop two columns to combat this issue
    cols_to_drop = ['ATMP', 'DEWP']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

    return df

@app.route("/")
def dashboard():
    df = fetch_noaa_data()
    return render_template("dashboard.html", 
                           data=df.to_dict(orient="records"), 
                           columns=list(df.columns))

if __name__ == "__main__":
    app.run(debug=True)
