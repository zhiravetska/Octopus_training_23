#import re
#import re
#import urllib
#city = input("Enter your city: ")
# https://www.weather-forecast.com/locations/Seattle/forecasts/latest
#url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

#data = urllib.request.urlopen(url).read()
#data1 = data.decode("utf-8")
#print(data1)

#Nr. 71, weather (no attribute 'find'?????)
import requests
from bs4 import *
data = requests.get("https://www.accuweather.com/en/fr/san-damiano/158758/weather-forecast/158758")
soup = BeautifulSoup(data.text, "html.parser")
data2 = soup.find('div', {'class':'info'})
data3 = data2.find('strong', {'class':'temp'})
data4 = data3.contents[0]


