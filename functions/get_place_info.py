import os
import requests
import json

def get_place_info(latitude, longitude):
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{latitude},{longitude}",
        "radius": 1000,
        "key": api_key
    }

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch place info"}

# Example usage
if __name__ == "__main__":
    lat = 41.8781
    lon = -87.6298
    places = get_place_info(lat, lon)
    print(json.dumps(places, indent=2))
