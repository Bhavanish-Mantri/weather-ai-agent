from weather_tool import get_weather

print("Hello! I am your AI Weather Agent.")

city = input("Enter city name: ")

weather = get_weather(city)

print(weather)