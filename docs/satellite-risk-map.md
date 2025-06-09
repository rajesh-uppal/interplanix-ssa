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
## 🛰️ Interactive Satellite Risk Map

This tool shows active satellites color-coded by risk level based on orbital inclination:

<iframe src="https://rajesh-uppal.github.io/interplanix-ssa/satellite_risk_map_sample.html" width="100%" height="600" style="border:none;"></iframe>

---

## 📦 Data & Tools

- **TLE Source**: [Celestrak.com](https://celestrak.com)
- **Library**: [`Skyfield`](https://rhodesmill.org/skyfield/)
- **Visualization**: [`Plotly`](https://plotly.com/python/)
- **Author**: Interplanix (2025)

---⚠️ *This is a simplified risk model and is intended for demonstration purposes only.*

---

## 🎯 Key Features

- 🌍 Real-time satellite positioning using TLE data  
- 🖼️ Interactive risk-layered orbital map  
- 🔍 Hoverable tooltips with satellite name, altitude, and risk level  
- 📁 Output as standalone HTML for easy sharing or hosting  

---

## 🔬 Use Cases

- Space Situational Awareness (SSA)  
- Collision threat modeling  
- Orbital traffic monitoring  
- Decision support for space operations

---

🄯 2025 **INTERPLANIX: Charting New Frontiers, Connecting Worlds**  
*Powered by Open-Source Technologies and the Astra WordPress Theme*

