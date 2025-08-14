import requests

userInput = input("Enter your city: ")

apiKey = 'adce47aa6210976762dcdb65769fbe1b'

weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=metric&appid={apiKey}")
if weatherData.status_code == 200:
    weather = weatherData.json()['weather'][0]['main']

    print(f'{userInput}\nWeather: {weather}')
else:
    print("An error has occured")