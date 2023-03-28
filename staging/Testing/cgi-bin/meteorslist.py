import pymongo, cgi, os, gridfs, re, html
from pprint import pprint

client = pymongo.MongoClient("mongodb://root:student@localhost:27017")
db = client["meteorcsv"]
coll = db["landings"]

print( 'Content-Type: text/html;charset=utf-8\r\n\r\n' )

print(html.header)

form = cgi.FieldStorage()

mydoc = coll.find({},{'_id':0, 'name':1}).limit(20)

#prints out list of meteors limited to 20 at a time
#takes query from MongoDB and converts dictionary type object to string
#cleans string to be just name of meteor
#prints out meteors name as links so user can view each individual meteor
for x in mydoc:
  convString = str(x)
  convString = convString[1:][:-1].replace("'name': '", "")[:-1]
  print(f"<a href='/cgi-bin/info.py?meteor_name={convString}'>{convString}<a/></br>")

print(html.footer)

