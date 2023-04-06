#!/usr/bin/env python3

# Name - georesult.py
# Purpose - webpage that outputs the result of a geosearch string

import pymongo, cgi, os, gridfs, re, html
from pprint import pprint

#connecting to the database, getting the landings collection
client = pymongo.MongoClient("mongodb://root:student@localhost:27017")
db = client["meteorcsv"]
coll = db["landings"]

print( 'Content-Type: text/html;charset=utf-8\r\n\r\n' )

#created variables for limit and skip for different pages
collLimit = 6
collSkip = 6

print(html.header) #from html.py
print("<h2>Results: </h2>")
form = cgi.FieldStorage() #get data from url/form data

#get the value of page number in get request/url
pgNum = form.getvalue('pg')
pgNum = int(pgNum)

### REGEX
# meteor_lat = form.getvalue('lat') #gets value of name from submitted form (GET)
# meteor_long = form.getvalue('long')

for doc in coll.find({"location":{"$near"[-99, 16]}}).limit(5):
    print(doc)

# #instantiates variables from list of dictionary items
# for x in mydoc:
#   meteorID = x['id']
#   meteorName = x['name']
#   meteorLat = x['reclat']
#   meteorLong = x['reclong']
#   print(f"<a href='/cgi-bin/info.py?meteorID={meteorID}'>{meteorName}</a></br>")

# #count number of documents based off of previous query 
# #number determines if next button should appear or not
# mydocCount = coll.count_documents(
#   gquery, 
#   skip=(collSkip * (pgNum - 1)), 
#   limit=collLimit
# )

# print('</br>')
# #check if back or next need to appear
# if pgNum > 1:
#   print(f'<a href="/cgi-bin/result.py?lat={meteor_lat}&long={meteor_long}&pg={pgNum - 1}">Back</a>')
# if mydocCount == collLimit:
#  print(f'<a href="/cgi-bin/result.py?lat={meteor_lat}&long={meteor_long}&pg={pgNum + 1}">Next</a>')

print(html.footer)
