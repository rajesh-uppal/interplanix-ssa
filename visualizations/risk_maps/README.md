# 🛰️ Satellite Risk Maps

This folder contains raw and historical visualizations of satellite risk levels based on TLE data and inclination-based classification.

## Contents

- `*.html` – Interactive visual maps generated using Plotly.
- `*.png` – Static snapshots for reports and thumbnails.
- `*_risk_data.csv` – The processed dataset used to render the map.

## How to Generate

Run `notebooks/satellite_risk_map.ipynb` or `src/generate_map.py` to recreate maps.

## Note

Only the latest map is published at `/docs/satellite_risk_map_sample.html`. Older versions remain here for tracking and auditing.
