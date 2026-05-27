import pandas as pd
import numpy as np
import time
import os
import plotext as plt


def clear_console():
    """Clears the terminal screen for a smooth live UI look."""
    os.system('cls' if os.name == 'nt' else 'clear')


def run_terminal_pipeline():
    # 1. Load Data Safely
    try:
        df = pd.read_csv("data/Airline_Delay_Csv.csv")
    except FileNotFoundError:
        try:
            df = pd.read_csv("Airline_Delay_Cause.csv")
        except FileNotFoundError:
            print("❌ Error: 'Airline_Delay_Csv.csv' not found.")
            return

    # Clean missing values instantly
    delay_cols = ['carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']
    for col in delay_cols:
        df[col] = df[col].fillna(0)
    df['arr_del15'] = df['arr_del15'].fillna(0)

    # 2. Add Search Filter Up Front
    print("=" * 70)
    print("✈️  REAL-TIME FLIGHT DATA ANALYSIS PIPELINE SETUP")
    print("=" * 70)
    search_query = input("🔍 Enter an Airport or Carrier to track (or press Enter for ALL): ").strip().upper()

    if search_query:
        mask = (
                df['airport'].astype(str).str.upper().str.contains(search_query) |
                df['carrier_name'].astype(str).str.upper().str.contains(search_query)
        )
        stream_data = df[mask]
        if stream_data.empty:
            print(f"⚠️ No matches found for '{search_query}'. Running with full dataset.")
            stream_data = df
    else:
        stream_data = df

    print(f"\n🚀 Pipeline initialized! Loaded {len(stream_data)} records.")
    print("Starting data ingestion stream in 1 second...")
    time.sleep(1)

    # 3. Stream Engine Loop Settings
    rolling_window_size = 30
    rolling_buffer = pd.DataFrame()

    for idx, row in stream_data.iterrows():
        current_row = pd.DataFrame([row])
        rolling_buffer = pd.concat([rolling_buffer, current_row], ignore_index=True)

        if len(rolling_buffer) > rolling_window_size:
            rolling_buffer = rolling_buffer.iloc[-rolling_window_size:]

        # --- CALCULATION LAYER ---
        carrier_mins = rolling_buffer['carrier_delay'].sum()
        weather_mins = rolling_buffer['weather_delay'].sum()
        nas_mins = rolling_buffer['nas_delay'].sum()
        security_mins = rolling_buffer['security_delay'].sum()
        late_mins = rolling_buffer['late_aircraft_delay'].sum()

        clear_console()

        # --- TITLE BANNER ---
        print("=" * 75)
        print(f"📡 TERMINAL LIVE METRICS  |  FILTER: {search_query if search_query else 'ALL'}  |  PROCESSED: {idx + 1}")
        print("=" * 75)

        # --- VISUAL CHART LAYER (PLOTEXT) ---
        reasons = ['Carrier', 'Weather', 'NAS', 'Security', 'Late AC']
        minutes = [carrier_mins, weather_mins, nas_mins, security_mins, late_mins]

        # If there are minutes to display, show a live text bar chart
        if sum(minutes) > 0:
            print("📊 LIVE DELAY DISTRIBUTION (MINUTES):")
            plt.clf()
            plt.bar(reasons, minutes, color="red")
            plt.plotsize(75, 12)  # Adjusts chart box size to fit neatly in console
            plt.theme("dark")
            plt.show()
            print("-" * 75)
        else:
            print("📊 LIVE DELAY DISTRIBUTION: [Waiting for delayed records...]\n" + "-" * 75)

        # --- VISUAL TABULAR LAYER (PANDAS STYLE) ---
        print("📋 LIVE INGESTION FEED BUFFER LOG (TABULAR VIEW):")
        display_cols = [c for c in ['airport', 'carrier_name', 'arr_flights', 'arr_del15'] if
                        c in rolling_buffer.columns]

        # Create a visually clean table format using standard pandas formatting rules
        table_snapshot = rolling_buffer[display_cols].tail(8).copy()
        table_snapshot.columns = ['AIRPORT', 'CARRIER NAME', 'TOTAL FLIGHTS', 'DELAYS']

        print(table_snapshot.to_string(index=False, justify='left', max_colwidth=25))
        print("=" * 75)
        print("Press Ctrl+C inside this console frame to terminate stream at any time.")

        time.sleep(0.5)


if __name__ == "__main__":
    run_terminal_pipeline()
