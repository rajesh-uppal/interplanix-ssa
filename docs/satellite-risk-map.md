# 🛰️ Satellite Risk Map

This interactive visualization shows satellites classified by risk level based on proximity to the equator — a proxy for orbital crowding and collision risk.

## 🎯 Risk Classification Logic

| Risk Level | Distance from Equator | Description |
|------------|------------------------|-------------|
| 🟢 Low     | ≤ 10°                  | Near-equatorial orbits with generally lower collision probabilities |
| 🟡 Medium  | 10°–50°                | Medium-inclination orbits (often in LEO constellations) |
| 🔴 High    | > 50°                  | Polar or sun-synchronous orbits, often crowded with Earth-observing satellites |

> Classification is based on geodetic latitude of the satellite subpoint.

---

## 🌐 Live Visualization

<iframe src="https://rajesh-uppal.github.io/interplanix-visualizations/satellite_risk_map_sample.html" width="100%" height="600" style="border:none;"></iframe>

---

## 📦 Data & Tools

- **TLE Source**: [Celestrak.com](https://celestrak.com)
- **Library**: [`Skyfield`](https://rhodesmill.org/skyfield/)
- **Visualization**: [`Plotly`](https://plotly.com/python/)
- **Author**: Interplanix (2025)

---
