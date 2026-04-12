import requests

# WEATHER TOOL (WeatherAPI)
def get_weather(city):
    api_key = "bac8b60f3cbb49e98bb5512xxxxxxx"   # paste theB WeatherAPI key here
    
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Error: {response.text}"
    
    data = response.json()
    
    temp = data['current']['temp_c']
    desc = data['current']['condition']['text']
    
    return f"Weather in {city}: {temp}°C, {desc}"

def smart_agent():
    
    user_input = input("Enter your request: ").lower()

    if "weather" in user_input:
        city = input("Enter city name: ")
        return get_weather(city)

    else:
        return "Sorry, I don't understand."

print(smart_agent())