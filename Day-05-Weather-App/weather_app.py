import requests

def get_weather(city_name):
    try:

        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
        geo_res = requests.get(geo_url, timeout=10).json()
        
        if not geo_res.get("results"):
            print(f"\nError: City '{city_name}' not found. Please check spelling.\n")
            return

        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]
        name = geo_res["results"][0]["name"]
        country = geo_res["results"][0].get("country", "")

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        w_res = requests.get(weather_url, timeout=10).json()
        current = w_res["current_weather"]

        print("\n" + "="*45)
        print(f" Live Weather Update: {name}, {country}")
        print("="*45)
        print(f" Temperature:    {current['temperature']} C")
        print(f" Wind Speed:     {current['windspeed']} km/h")
        print("="*45 + "\n")

    except requests.exceptions.RequestException as e:
        print(f"\nNetwork Error: {e}\n")

def main():
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        if not city:
            print("Please enter a valid city name.")
            continue
            
        get_weather(city)

if __name__ == "__main__":
    main()