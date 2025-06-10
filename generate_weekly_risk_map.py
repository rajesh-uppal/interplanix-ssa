# generate_weekly_risk_map.py

import os
import pandas as pd
from datetime import date
from your_existing_module import get_tle_data, extract_features, plot_satellite_risk_map  # Replace with real functions

# 🗓️ Use today's date
today = date.today().isoformat()

# 📥 Step 1: Get TLE data (simulate or replace with actual download)
tle_path = f"notebooks/tle_data_{today}.txt"
df = get_tle_data(tle_path)  # Should return a DataFrame

# ⚙️ Step 2: Extract features and assign risk
df_features = extract_features(df)

# 🗺️ Step 3: Plot and Save Map
fig = plot_satellite_risk_map(df_features, sample_size=50)

# 💾 Step 4: Save updated files
output_html = "docs/satellite_risk_map_sample.html"
output_csv = f"docs/risk_data_{today}.csv"
fig.write_html(output_html)
df_features.to_csv(output_csv, index=False)

print(f"✅ Updated map saved: {output_html}")
print(f"📊 Data saved: {output_csv}")
