import json

data = '''
[{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
},
{
 "name":"akhil",
 "phone":"9866767676"}]'''

info = json.loads(data)
#print('Name:', info["name"])
#print('Phone:',info["phone"]["type"])
#print('Hide:', info["email"]["hide"])
print(len(info))
