import requests

def weather_info():
    url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url, timeout=10)
   
    if response.status_code == 200:
        data = response.json()
        print(f"Temperature = {data['current']['temperature_2m']}")
        print(f"Humidity = {data['current']['relative_humidity_2m']}")
        print(f"Wind Speed = {data['current']['wind_speed_10m']}")
        print(f"Temperature_unit = {data['current_units']['temperature_2m']}")
    else:
        raise Exception("Data not found")

def main():
    try:
        weather_info()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
