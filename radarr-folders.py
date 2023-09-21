import requests
import os

# Radarr API settings
RADARR_API_URL = "http://your-radarr-url/api"
RADARR_API_KEY = "your-radarr-api-key"

# Function to make a GET request to Radarr API
def radarr_api_get(endpoint):
    headers = {"X-Api-Key": RADARR_API_KEY}
    response = requests.get(f"{RADARR_API_URL}/{endpoint}", headers=headers)
    response.raise_for_status()
    return response.json()

# Function to create directories if they do not exist
def create_movie_directories(movie_list):
    for movie in movie_list:
        movie_path = os.path.join(movie["path"], movie["title"])
        if not os.path.exists(movie_path):
            print(f"Creating directory: {movie_path}")
            os.makedirs(movie_path)

def main():
    try:
        # Get a list of all movies from Radarr
        movie_list = radarr_api_get("movie")

        # Create directories for each movie
        create_movie_directories(movie_list)

        print("All movie directories have been created.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
