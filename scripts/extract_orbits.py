import pandas as pd
from skyfield.api import EarthSatellite, load
from datetime import datetime

df = pd.read_csv("data/processed/parsed_tle.csv")

results = []
ts = load.timescale()
now = datetime.utcnow()

for _, row in df.iterrows():
    try:
        satellite = EarthSatellite(row['line1'], row['line2'], row['name'], ts)
        geo = satellite.at(ts.now()).subpoint()
        lat = geo.latitude.degrees
        lon = geo.longitude.degrees
        alt_km = geo.elevation.km

        results.append({
            "name": row["name"],
            "latitude": round(lat, 2),
            "longitude": round(lon, 2),
            "altitude_km": round(alt_km, 2),
        })
    except Exception as e:
        continue  # skip malformed entries

pd.DataFrame(results).to_csv("data/output/sat_positions.csv", index=False)
print("✅ Satellite positions exported to data/output/sat_positions.csv")
