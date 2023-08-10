from bs4 import BeautifulSoup
import requests
import pandas as pd

latt, long = [], []
for i in range(1,9): 
 data = requests.get("https://www.latlong.net/category/cities-102-15-"+str(i)+ ".html")
 data = BeautifulSoup(data.text, "html.parser")
 for tr in data.find_all("tr"):
    temp = tr.find_all("td")
    if len(temp) == 3:
        latt.append(temp[1].text)
        long.append(temp[2].text)

all_weather = []
for i in range(len(latt)):
  weather = "https://weather.com/en-IN/weather/today/l/"+latt[i]+","+long[i]
  print(i+1 ,"rows loaded")
  weather = requests.get(weather)
  weather_bs = BeautifulSoup(weather.text,"html.parser")
  temperature_sec= weather_bs.find_all("section",{"data-testid":"TodayWeatherModule" })
  city=weather_bs.find("h1",{"class":"CurrentConditions--location--1YWj_"}).text
  for temperature in temperature_sec:
    column=temperature.find_all("span",{"data-testid":"TemperatureValue"})
    morning = column[0].text
    afternoon = column[1].text
    evening = column[2].text
    night = column[3].text
  value = {"City":city,"Morning":morning,"Afternoon":afternoon,"Evenving":evening,"Night":night}
  all_weather.append(value)
    
Today_weather = pd.DataFrame(all_weather)
Today_weather.set_index("City")
