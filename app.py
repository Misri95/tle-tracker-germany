import streamlit as st
import pandas as pd
from skyfield.api import EarthSatellite, load
import plotly.express as px

st.set_page_config(page_title="TLE Satellite Tracker", layout="centered")
st.title("🛰️ TLE Satellite Tracker – DLR/ESA Missions")

# Load parsed TLE CSV
tle_df = pd.read_csv("data/processed/parsed_tle.csv")

satellite_names = tle_df["name"].unique().tolist()
selected = st.selectbox("Select a satellite", satellite_names)

row = tle_df[tle_df["name"] == selected].iloc[0]
ts = load.timescale()
sat = EarthSatellite(row["line1"], row["line2"], row["name"], ts)
subpoint = sat.at(ts.now()).subpoint()

st.metric("Latitude", f"{subpoint.latitude.degrees:.2f}°")
st.metric("Longitude", f"{subpoint.longitude.degrees:.2f}°")
st.metric("Altitude", f"{subpoint.elevation.km:.2f} km")

map_df = pd.DataFrame({
    "name": [row["name"]],
    "lat": [subpoint.latitude.degrees],
    "lon": [subpoint.longitude.degrees]
})

fig = px.scatter_geo(map_df,
    lat="lat", lon="lon", text="name",
    title="Current Satellite Position",
    projection="natural earth"
)
fig.update_traces(marker=dict(size=10, color="red"))
st.plotly_chart(fig, use_container_width=True)

