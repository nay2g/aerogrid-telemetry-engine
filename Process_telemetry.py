import pandas as pd

def analyze_telemetry(file_path):
    print(f"Reading streaming data from: {file_path}")
    
    # Load the telemetry dataset
    df = pd.read_csv(file_path)
    
    # Hardware anomaly safety thresholds defined by the brief
    TEMP_THRESHOLD = 85.0
    VIBRATION_THRESHOLD = 15.0
    
    # Filter rows violating either the temperature or vibration limits
    anomalies = df[(df['temperature_c'] > TEMP_THRESHOLD) | (df['vibration_mm_s'] > VIBRATION_THRESHOLD)]
    
    # Extract unique Turbine IDs that triggered the anomalies
    failing_turbines = anomalies['turbine_id'].unique()
    
    # Print clean results to the console
    print("\n==============================")
    print("   DATA ANALYSIS COMPLETE")
    print("==============================")
    print(f"Total anomaly events logged: {len(anomalies)}")
    print(f"Turbines requiring urgent maintenance: {list(failing_turbines)}")
    print("==============================\n")
    
    return failing_turbines

if __name__ == "__main__":
    # Set to match your exact file name in the folder
    try:
        analyze_telemetry('telemetry_data(in).csv')
    except FileNotFoundError:
        print("Error: 'telemetry_data(in).csv' not found.")
        print("Please ensure the CSV file is placed directly in your VS Code folder.")