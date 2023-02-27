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
#https://www.google.com/finance?q=
url = "https://www.google.com/finance?q="
stock = input("Enter your stock: ")
url = url + stock
print(url)
data = urllib.request.urlopen(url).read() #further we decode a data
data1 = data.decode("utf-8")
print(data1)

m = re.search('meta itemprop = "price"', data1)
#print(m)
start = m.start()
end = start + 50
newString = data1[start:end]
print(newString)

m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]
print(newString1)

m = re.search("/", newString1)
start = 0
end = m.end()-3
final = newString1[0:end]
print(final)
print("The value of " + stock.upper() + "is "+ final)

