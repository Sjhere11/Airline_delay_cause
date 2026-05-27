# ✈️ Real-Time Terminal Flight Delay Analytics Pipeline

A lightweight, real-time data streaming simulation engine built in Python. This project converts static airline transactional telemetry data into an interactive, live-updating terminal monitoring dashboard complete with inline visualizations.

## 🚀 Key Features
- **Stream Ingestion Simulation:** Re-engineers historical data into a high-velocity, row-by-row data stream using precise execution pacing.
- **Dynamic Console UI:** Draws responsive bar charts, matrices, and formatted operational tables directly inside the IDE output console using `plotext`.
- **Interactive Query Routing:** Built-in instant text routing allows users to isolate and track specific airport hubs (e.g., `ORD`, `JFK`) or carriers (e.g., `Delta`) on the fly.
- **Automated Threshold Triggers:** Includes automated warning alerts that instantly flag operational breakdowns when system delay rates breach custom thresholds.

## 🛠️ Architecture & Tools Used
- **Language:** Python 3.x
- **Data Engine:** Pandas, NumPy
- **Visuals Framework:** Plotext (Terminal Graphic Processing Unit)
- **Data Source:** High-frequency Flight Operational Performance Dataset

## 📦 Project Directory Structure
```text
flight-delay/
├── data/
│   └── Airline_Delay_Cause.csv   # Local high-frequency dataset (Hidden via gitignore)
├── analysis.py                  # Core processing pipeline engine
├── .gitignore                   # Data protection configuration rules
└── README.md                    # System documentation
```

## ⚡ Setup & Execution Instructions

1. Clone this repository to your workstation:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the application root folder:
   ```bash
   cd Airline_delay_cause
   ```
3. Install the required operational dependencies:
   ```bash
   pip install pandas numpy plotext
   ```
4. Place your data file (`Airline_Delay_Cause.csv`) inside your project directory.
5. Initialize the streaming monitoring console:
   ```bash
   python data/analysis.py
   ```
