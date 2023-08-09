from bs4 import BeautifulSoup
import requests
import pandas as pd

city=input("Enter the city : ")
data = requests.get("https://www.google.com/search?q=latitude+and+longitude+of+"+city)#+"&client=opera&hs=vyo&ei=WXTSZJ2VEMelhwOyqrIw&oq=lattitude+and+long+of+bangalore&gs_lp=Egxnd3Mtd2l6LXNlcnAiH2xhdHRpdHVkZSBhbmQgbG9uZyBvZiBiYW5nYWxvcmUqAggAMgUQABiiBDIFEAAYogQyBRAAGKIESLgeULcGWMoRcAF4AZABAJgBsAGgAb4FqgEDMi40uAEByAEA-AEBwgIKEAAYRxjWBBiwA8ICDBAAGA0YgAQYRhj7AcICChAAGAgYHhgNGA_CAggQABiKBRiGA8ICChAhGKABGMMEGAriAwQYACBBiAYBkAYI&sclient=gws-wiz-serp")
data = BeautifulSoup(data.text,"html.parser")
latlong = str(data.text)
print(latlong)
a=(latlong.find("Coordinates"))+11
b = latlong.find("° N" )
lat=latlong[a:b]
latlong=latlong[b+5:]
b = latlong.find("° ")
long=latlong[:b]


d={}
#a = input("Enter the city url from(https://weather.com/en-IN/weather/today) : ")
a = "https://weather.com/en-IN/weather/today/l/"+lat+","+long
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
