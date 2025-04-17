import os
import pandas as pd
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
DISCOS_API_KEY = os.getenv("DISCOS_API_KEY")
DISCOS_BASE_URL = "https://discosweb.esoc.esa.int/api/objects"

def get_discos_satellite_data(satno):
    headers = {
        "Authorization": f"Bearer {DISCOS_API_KEY}",
        "Accept": "application/json",
        "DiscosWeb-Api-Version": "2"
    }

    params = {
        "filter": f"eq(satno,{satno})"
    }

    response = requests.get(DISCOS_BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json().get("data", [{}])[0].get("attributes", {})
            satellite_info = {
                "SATNO": satno,
                "Name": data.get("name", "Unknown"),
                "COSPAR ID": data.get("cosparId", "N/A"),
                "Object Class": data.get("objectClass", "Unknown"),
                "Mission": data.get("mission", "Unknown"),
                "Mass (kg)": data.get("mass", "Unknown"),
                "Shape": data.get("shape", "Unknown"),
                "Width (m)": data.get("width", "Unknown"),
                "Height (m)": data.get("height", "Unknown"),
                "Diameter (m)": data.get("diameter", "Unknown"),
                "Span (m)": data.get("span", "Unknown"),
                "Cross-Section Max": data.get("xSectMax", "Unknown"),
                "Cross-Section Min": data.get("xSectMin", "Unknown"),
                "Cross-Section Avg": data.get("xSectAvg", "Unknown"),
                "First Epoch (Launch Date)": data.get("firstEpoch", "Unknown"),
                "Predicted Decay Date": data.get("predDecayDate", "N/A"),
                "Active Status": data.get("active", "Unknown"),
                "Catalogued Fragments": data.get("cataloguedFragments", "Unknown"),
                "On-Orbit Fragments": data.get("onOrbitCataloguedFragments", "Unknown"),
            }
            return satellite_info
        except Exception as e:
            return {"SATNO": satno, "Error": f"Data parsing error: {str(e)}"}
    else:
        return {"SATNO": satno, "Error": f"API Error {response.status_code}: {response.text}"}

def main():
    input_path = "data/input_satnos.csv"
    output_path = "output/satellite_data.csv"

    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        return

    df = pd.read_csv(input_path)

    if "Name" not in df.columns:
        print("Error: CSV must contain a 'Name' column with SATNO values.")
        return

    print(f"Fetching satellite data for {len(df)} entries...")

    sat_data = [get_discos_satellite_data(str(satno)) for satno in df["Name"]]
    df_satellite_info = pd.DataFrame(sat_data)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_satellite_info.to_csv(output_path, index=False)
    print(f"Satellite data saved to: {output_path}")

if __name__ == "__main__":
    main()
