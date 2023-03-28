# Name - result.py
# Purpose - webpage that outputs the result of a search string 

import pymongo, cgi, os, gridfs, re, html
from pprint import pprint

#connecting to the database, getting the landings collection
client = pymongo.MongoClient("mongodb://root:student@localhost:27017")
db = client["meteorcsv"]
coll = db["landings"]

print( 'Content-Type: text/html;charset=utf-8\r\n\r\n' )

print(html.header) #from html.py
print("<h2>Results: </h2>")
form = cgi.FieldStorage() #get data from url/form data

### REGEX
meteor_name = form.getvalue('meteor_name') #gets value of name from submitted form (GET)
regx = re.compile("^"+meteor_name, re.IGNORECASE) #uses regex module to create regex with variable, searches for substrings, ignores case
mydoc = coll.find(
  {'name':{'$regex':regx}}, #get name of regexed statement, returns name
  {'_id':0, 'name':1}
).limit(20) #limit query to 20

#same as meteorslist.py
for x in mydoc:
  convString = str(x)
  convString = convString[10:][:-2]
  print(f"<a href='/cgi-bin/info.py?meteor_name={convString}'>{convString}<a/></br>")

print(html.footer)