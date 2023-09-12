import requests


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=238604581d7d15f3cc369eb14b19b911"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == "404":
        print("City not found. Please try again.")
        return None

    temperature = data["main"]["temp"]
    condition = data["weather"][0]["main"]
    humidity = data["main"]["humidity"]

    return temperature, condition, humidity


def main():
    print("Welcome to Weather Scraper!\n")

    while True:
        city = input("Enter the city name: ")
        weather_data = get_weather(city)

        if weather_data is not None:
            temperature, condition, humidity = weather_data
            print(f"\nWeather for {city}:")
            print(f"Temperature: {temperature}°F")
            print(f"Condition: {condition}")
            print(f"Humidity: {humidity}%\n")

        another_city = input("Do you want to check another city? (yes/no): ")
        if another_city.lower() != "yes":
            break

    print("Thank you for using Weather Scraper! Have a great day!")


if __name__ == "__main__":
    main()
