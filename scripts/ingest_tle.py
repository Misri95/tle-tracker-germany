import requests

# ✅ This works: valid Starlink TLE group via Celestrak API
url = "https://celestrak.org/NORAD/elements/science.txt"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200 and "1 " in response.text and "2 " in response.text:
    with open("data/raw/starlink.txt", "w") as f:
        f.write(response.text)
    print("✅ TLE data saved to data/raw/starlink.txt")
else:
    print(f"❌ Failed to fetch valid TLE data (status: {response.status_code})")
    print(response.text[:300])  # preview error
