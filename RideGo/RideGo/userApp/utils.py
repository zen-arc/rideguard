import requests
import time
def reverse_geocode(lat, lon):
    """
    Reverse geocode latitude and longitude to a location name using Nominatim.
    """
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    headers = {
        "User-Agent": "YourAppName/1.0 (your@email.com)"  # Set a custom User-Agent
    }
    try:
        time.sleep(1)  # Respect Nominatim's rate limit
        response = requests.get(url, headers=headers)
        print("Nominatim Reverse Geocode Response:", response.text)  # Log the raw response
        data = response.json()
        if data and 'display_name' in data:
            return data['display_name']  # Return the location name
        else:
            return f"{lat}, {lon}"  # Fallback to coordinates if no name is found
    except Exception as e:
        print(f"Error reverse geocoding: {str(e)}")
        return f"{lat}, {lon}"  # Fallback to coordinates on error