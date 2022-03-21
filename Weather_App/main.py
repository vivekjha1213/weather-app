import requests
import time

#city = "Gurgram" + city +"&appid=0eee0acfc032ab0d4028233b6cb4b7f3"

#https://api.openweathermap.org/data/2.5/weather?q=

api = "api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
response = requests.get(api)
data  = response.json()
temp = round(data["main"]["temp"] - 273.15)
pressure = data["main"]["pressure"]
humidity = data["main"]["humidity"]
sun_rise = time.strftime("%I:%M:%p",time.gmtime(data["sys"]["sunrise"]-21600))
sun_set= time.strftime("%I:%M:%p",time.gmtime(data["sys"]["sunset"]-21600))

print(sun_rise)
print(sun_set)