[Streamlit App](https://img.shields.io/badge/Launch-Dashboard-ff4b4b?logo=streamlit&logoColor=white)](https://misri95-tle-tracker-germany-app-xpn1il.streamlit.app/)

## 🖥️ Streamlit Dashboard Preview
![Preview](data/output/dashboard_preview.png)


![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-complete-brightgreen.svg)

# 🛰️ TLE Satellite Tracker — DLR/ESA Missions

This Python project tracks real-time orbital positions of scientific satellites using public TLE data (CelesTrak), focused on ESA/DLR missions like POLAR, ODIN, SWIFT, and more.

## ✅ Features
- Ingests live TLEs from CelesTrak
- Parses and stores into SQLite database
- Computes real-time position using skyfield
- Visualizes orbits on Earth using matplotlib

## 🛠️ Tools
- Python 3.10
- skyfield, pandas, sqlite3, matplotlib
- Data from: https://celestrak.org

## 📂 Folder Structure
\\\
scripts/ → contains all pipeline steps (ingest, parse, DB, plot)  
data/    → raw TLEs, processed CSVs, output positions
\\\

## ▶️ How to Run

\\\powershell
# Step 0: Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Step 1: Download TLE data
python scripts\ingest_tle.py

# Step 2: Parse into structured format
python scripts\parse_tle.py

# Step 3: Store into SQLite
python scripts\store_to_sqlite.py

# Step 4: Visualize satellite positions
python scripts\query_orbit_plot.py
\\\

## 📈 Output

Your output PNG (matplotlib plot) is saved in:
\\\
data/output/dlr_esa_satellites.png
\\\

## 📜 License
MIT License

## 📈 Output

![DLR/ESA Satellite Positions](data/output/dlr_esa_satellites.png)

