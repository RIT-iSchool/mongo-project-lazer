import pymongo, cgi, os, gridfs, re, html
from pprint import pprint

client = pymongo.MongoClient("mongodb://root:student@localhost:27017")
db = client["meteorcsv"]
coll = db["landings"]

print( 'Content-Type: text/html;charset=utf-8\r\n\r\n' )

print(html.header)
print("<h2>Info: </h2>")
form = cgi.FieldStorage()

### REGEX
meteor_name = form.getvalue('meteor_name')
regx = re.compile("^"+meteor_name, re.IGNORECASE)
mydoc = coll.find(
  {'name':{'$regex':regx}},
  {'_id':0, 'name':1, 'mass (g)':1, 'year':1}
).limit(20)

for x in mydoc:
  convString = str(x)
  convString = convString[1:][:-1]
  print(f"<p'>{convString}<p/></br>")

print(html.footer)