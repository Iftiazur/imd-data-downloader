
# 🌤 IMD Weather Data Downloader (Interactive Version)

This Python script allows users to **interactively download daily weather data** (Rainfall, Minimum Temperature, and Maximum Temperature) from the **Indian Meteorological Department (IMD)** using the [`imdlib`](https://github.com/imdevskp/imdlib) library.

---

## ✨ Features

- Interactive CLI: prompts user to enter start year, end year, latitude, and longitude
- Downloads **rainfall**, **minimum temperature**, and **maximum temperature** data
- Saves filtered CSV files for the selected coordinates into an `output/` folder

---


## 🚀 How to Use

### 🔧 Step-by-Step

1. **Clone or download** this script to your computer.

2. Open a terminal or command prompt and run the script:


3. **Enter the required inputs when prompted**:
   - Start year (e.g., `2022`)
   - End year (e.g., `2023`)
   - Latitude (e.g., `26.2584`)
   - Longitude (e.g., `91.4843`)

4. The script will:
   - Download IMD data for the selected years and coordinates
   - Save it as `rain.csv`, `tmin.csv`, and `tmax.csv` in the `./output` folder

5. Press **Enter** to exit after completion.

---

## 📁 Output Files

Each variable is saved in a separate CSV file:

- `output/rain.csv`
- `output/tmin.csv`
- `output/tmax.csv`

These contain daily data filtered to the closest grid point to the specified latitude and longitude.

---

## 🧪 Example Run

```bash
Enter start year (e.g., 2023): 2022
Enter end year (e.g., 2023): 2023
Enter latitude (e.g., 26.2584): 26.2584
Enter longitude (e.g., 91.4843): 91.4843

Fetching rain data...
rain data saved to CSV in 'output' folder 

Fetching tmin data...
tmin data saved to CSV in 'output' folder 

Fetching tmax data...
tmax data saved to CSV in 'output' folder 

Press Enter to exit...
```

---

## ❗ Notes & Troubleshooting

- **ModuleNotFoundError**: Run `pip install imdlib` if `imdlib` is not installed.
- **Empty CSV**: Ensure the coordinates are within the IMD dataset's coverage.
- **Permission denied**: Make sure you have write permissions to the project folder.

---

## 📝 License

This project is open-source and free to use under the MIT License.

---

## 🙌 Acknowledgments

- [imdlib](https://github.com/imdevskp/imdlib) - Python library to access IMD datasets.
- Indian Meteorological Department (IMD) for public data access.
