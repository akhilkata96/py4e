import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter location: ')
tot = 0
soc = 0

print('Retrieving', url)
file = ur.urlopen(url).read()
print('Retrieved', len(file), 'characters')

data = et.fromstring(file)
counts = data.findall('.//count')
for count in counts:
    soc += int(count.text)
    tot += 1

print('Count:', tot)
print('Sum:', soc)
