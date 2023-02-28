#string = "Ubiquitous"
#print(string[0:3])
#print(string[3:])

#Re module
import re
#dir(re)
#string = "The night was cold and dark"
#re.search("night", string)
#m = re.search("night", string)
#print(m)

#start = m.start()
#end = start + 5
#print(start)
#print(end)
#string[start:end]

#59
import re
import urllib.request

## STOCK
#https://www.google.com/finance?q=
#url = "https://www.google.com/finance?q="
#stock = input("Enter your stock: ")
#url = url + stock
#print(url)
#data = urllib.request.urlopen(url).read() #further we decode a data
#data1 = data.decode("utf-8")
#print(data1)

#m = re.search('meta itemprop = "price"', data1)
#print(m)
#start = m.start()
#end = start + 50
#newString = data1[start:end]
#print(newString)

#m = re.search('content="', newString)
#start = m.end()
#newString1 = newString[start:]
#print(newString1)

#m = re.search("/", newString1)
#start = 0
#end = m.end()-3
#final = newString1[0:end]
#print(final)
#print("The value of " + stock.upper() + "is "+ final)


## WEATHER FORECAST
#city = input("Enter your city: ")
# https://www.weather-forecast.com/locations/Seattle/forecasts/latest
#url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

#data = urllib.request.urlopen(url).read()
#data1 = data.decode("utf-8")
#print(data1)
# bgcolor="#CCCCCC" height="25"><span class="phrase">Moderate rain (total 11mm), heaviest on Thu morning.</span></td>

#m = re.search('span class="phrase"', data1)
#start = m.start()
#end = start + 100
#newString = data1[start:end]
#print(newString)

## DICTIONARY
#"https://www.dictionary.com/browse/"
try: 
    word = input("Enter your word: ")
    url = "https://www.dictionary.com/browse/" + word
    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")

#print(data1)
# <meta name="description" content="Octopus definition, any octopod of the genus Octopus, having a soft, oval body and eight sucker-bearing arms, 
# living mostly at the bottom of the sea. See more.">

    m = re.search('meta name="description" content="', data1)
    start = m.end()
    n = re.search("See more.", data1)
    end = n.start() - 1

    definition = data1[start:end]
    print(definition)

except:
    print("Sorry, your word is not in the dictionary!")
    


