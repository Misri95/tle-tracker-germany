import pandas as pd

raw_path = "data/raw/starlink.txt"
out_path = "data/processed/parsed_tle.csv"

with open(raw_path, "r") as file:
    lines = [line.strip() for line in file if line.strip() != ""]  # skip blanks

records = []
for i in range(0, len(lines), 3):
    try:
        name = lines[i]
        line1 = lines[i+1]
        line2 = lines[i+2]
        records.append((name, line1, line2))
    except IndexError:
        continue  # skip incomplete records

df = pd.DataFrame(records, columns=["name", "line1", "line2"])
df.to_csv(out_path, index=False)
print(f"✅ Parsed {len(df)} TLE entries → {out_path}")
