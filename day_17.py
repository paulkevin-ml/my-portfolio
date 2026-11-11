import requests

try:
    response = requests.get("https://api.agify.io/?name=paul")
    data = response.json()
    print(data)
    print("Predicted age: ", data["age"])
except requests.exceptions.ConnectionError:
    print("Error: could not connect to the internet.")
