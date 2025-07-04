import sqlite3
import pandas as pd
from skyfield.api import EarthSatellite, load
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/output/tle.db")
df = pd.read_sql("""
    SELECT * FROM satellites
    WHERE name LIKE '%POLAR%' 
       OR name LIKE '%XMM%' 
       OR name LIKE '%SWIFT%'
       OR name LIKE '%NUSTAR%'
       OR name LIKE '%ODIN%'
""", conn)
conn.close()
ts = load.timescale()
now = ts.now()

positions = []
for _, row in df.iterrows():
    sat = EarthSatellite(row["line1"], row["line2"], row["name"], ts)
    subpoint = sat.at(now).subpoint()
    positions.append({
        "name": row["name"],
        "lat": subpoint.latitude.degrees,
        "lon": subpoint.longitude.degrees
    })

plot_df = pd.DataFrame(positions)

plt.figure(figsize=(10, 6))
plt.scatter(plot_df["lon"], plot_df["lat"], c="red")
for _, r in plot_df.iterrows():
    plt.text(r["lon"], r["lat"], r["name"], fontsize=8)
plt.title("Current Positions of DLR/ESA Satellites")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()

plt.savefig("data/output/dlr_esa_satellites.png", dpi=300)

