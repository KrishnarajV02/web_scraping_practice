from bs4 import BeautifulSoup
import requests
import pandas as pd

latt, long = [], []
for i in range(1,9): 
 data = requests.get("https://www.latlong.net/category/cities-102-15-"+str(i)+ ".html")#+"&client=opera&hs=vyo&ei=WXTSZJ2VEMelhwOyqrIw&oq=lattitude+and+long+of+bangalore&gs_lp=Egxnd3Mtd2l6LXNlcnAiH2xhdHRpdHVkZSBhbmQgbG9uZyBvZiBiYW5nYWxvcmUqAggAMgUQABiiBDIFEAAYogQyBRAAGKIESLgeULcGWMoRcAF4AZABAJgBsAGgAb4FqgEDMi40uAEByAEA-AEBwgIKEAAYRxjWBBiwA8ICDBAAGA0YgAQYRhj7AcICChAAGAgYHhgNGA_CAggQABiKBRiGA8ICChAhGKABGMMEGAriAwQYACBBiAYBkAYI&sclient=gws-wiz-serp")
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
  a= weather_bs.find_all("section",{"data-testid":"TodayWeatherModule" })
  city=weather_bs.find("h1",{"class":"CurrentConditions--location--1YWj_"}).text
  for i in a:
    z=i.find_all("span",{"data-testid":"TemperatureValue"})
    morning = z[0].text
    afternoon = z[1].text
    evening = z[2].text
    night = z[3].text
  h = {"City":city,"Morning":morning,"Afternoon":afternoon,"Evenving":evening,"Night":night}
  all_weather.append(h)
    
Today_weather = pd.DataFrame(all_weather)
Today_weather.set_index("City")
