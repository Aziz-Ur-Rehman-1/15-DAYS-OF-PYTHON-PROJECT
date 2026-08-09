import requests

API_KEY = "[186c956933e242b0968182220260908]" 
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            city_name = data["location"]["name"]
            country = data["location"]["country"]
            temp = data["current"]["temp_c"]
            feels_like = data["current"]["feelslike_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_kph"]
            
            print("\n" + "="*45)
            print(f" Live Weather Update: {city_name}, {country}")
            print("="*45)
            print(f" Temperature:    {temp} C (Feels like {feels_like} C)")
            print(f" Condition:      {condition}")
            print(f" Humidity:       {humidity}%")
            print(f" Wind Speed:     {wind_speed} km/h")
            print("="*45 + "\n")
        else:
            error_msg = data.get("error", {}).get("message", "Unknown error")
            print(f"\nError fetching data: {error_msg}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork/Connection Error: {e}\n")

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