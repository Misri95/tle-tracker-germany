import sqlite3
import pandas as pd

df = pd.read_csv("data/processed/parsed_tle.csv")

conn = sqlite3.connect("data/output/tle.db")
df.to_sql("satellites", conn, if_exists="replace", index=False)
conn.close()

print("✅ Data written to SQLite database: tle.db")
