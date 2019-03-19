import urllib.request as ur
import json

url = input("Enter location: ")
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
file = json.loads(data)

soc = 0
tot = 0

for comment in file["comments"]:
    soc += int(comment["count"])
    tot += 1

print('Count:', tot)
print('Sum:', soc)
