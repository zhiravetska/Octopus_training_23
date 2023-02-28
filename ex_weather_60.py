import re
import re
import urllib
city = input("Enter your city: ")
# https://www.weather-forecast.com/locations/Seattle/forecasts/latest
url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print(data1)