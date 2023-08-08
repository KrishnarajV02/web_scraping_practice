from bs4 import BeautifulSoup
import requests
import pandas as pd
d={}
#a = input("Enter the city url from(https://weather.com/en-IN/weather/today) : ")
a = "https://weather.com/en-IN/weather/today/l/02144e9a9a2fe048b3ecca9df91501293f98ee712846f78a5da25ba6690fd98c"
data = requests.get(a)
bs = BeautifulSoup(data.text,"html.parser")
a= bs.find_all("section",{"data-testid":"TodayWeatherModule" })
d["City"]=(bs.find("h1",{"class":"CurrentConditions--location--1YWj_"})).text
for i in a:
    z=i.find_all("span",{"data-testid":"TemperatureValue"})
    y= i.find_all("span",{"class":"Ellipsis--ellipsis--3ADai"})
for i in range(len(z)):
        d[y[i].text]=[z[i].text]
s=pd.DataFrame(d)
s.set_index("City")
