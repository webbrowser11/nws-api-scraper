import requests

def scrape_nws():
    headers = {"User-Agent": "lo-weather/1.0 (terpstragraham@gmail.com)"}
    url = "https://api.weather.gov/gridpoints/PQR/114,97/forecast?units=us"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes (4xx or 5xx)
        
        data = response.json()
        periods = data.get("properties", {}).get("periods", [])
        
        print("--- NWS Forecast for Lake Oswego / Portland Area ---")
        for period in periods:
            print(f"{period['name']}: {period['temperature']}°{period['temperatureUnit']} — {period['shortForecast']}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from NWS API: {e}")

if __name__ == "__main__":
    scrape_nws()