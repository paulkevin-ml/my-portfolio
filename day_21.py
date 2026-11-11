import requests

API_KEY = "bd13f00b64a12d738acae4d83e3830fc"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code==200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            print(f"{city}: {temp}°C, {description}")
        else:
            print("City not found. Try again.")
    except requests.exceptions.ConnectionError:
        print("No internet connection.")

while True:
    city = input("Enter a city(or'exit' to quit): ")
    if city.lower()=="exit":
        break
    get_weather(city)