name = input("Enter file:")
emails=dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    email = line[5]
    email = email.split(":")
    hour = email[0]
    emails[hour] = emails.get(hour,0)+1
hourlist=[]
for k,v in emails.items():
    hourlist.append((k,v))
hourlist.sort()
for k,v in hourlist:
    print(k,v)
