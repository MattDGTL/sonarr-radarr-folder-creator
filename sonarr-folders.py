import requests
import os

# Sonarr API settings
SONARR_API_URL = "http://your-sonarr-url/api"
SONARR_API_KEY = "your-sonarr-api-key"

# Function to make a GET request to Sonarr API
def sonarr_api_get(endpoint):
    headers = {"X-Api-Key": SONARR_API_KEY}
    response = requests.get(f"{SONARR_API_URL}/{endpoint}", headers=headers)
    response.raise_for_status()
    return response.json()

# Function to create directories if they do not exist
def create_series_directories(series_list):
    for series in series_list:
        series_path = series["path"]
        if not os.path.exists(series_path):
            print(f"Creating directory: {series_path}")
            os.makedirs(series_path)

def main():
    try:
        # Get a list of all series from Sonarr
        series_list = sonarr_api_get("series")

        # Create directories for each series
        create_series_directories(series_list)

        print("All series directories have been created.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
