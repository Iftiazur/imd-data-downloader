import imdlib as imd
import os

# Take user input from command line interactively
start_yr = int(input("Enter start year (e.g., 2023): "))
end_yr = int(input("Enter end year (e.g., 2024): "))
lat = float(input("Enter latitude (e.g., 26.2584): "))
lon = float(input("Enter longitude (e.g., 91.4843): "))

# Create output directory
file_dir = "./output"
os.makedirs(file_dir, exist_ok=True)

# Download and save data
variables = ['rain', 'tmin', 'tmax']
for var in variables:
    print(f"Fetching {var} data...")
    imd.get_data(var, start_yr, end_yr, fn_format='yearwise')
    data = imd.open_data(var, start_yr, end_yr, fn_format='yearwise')

    output_path = os.path.join(file_dir, var)  # saves as ./output/rain.csv, etc.
    data.to_csv(file_name=output_path, lat=lat, lon=lon)

    print(f"{var} data saved to CSV in 'output' folder \n")

input("\nPress Enter to exit...")
