#!/usr/bin/env python3

# Name - images.py
# Purpose - fetch images of accessed meteors (may be rolled into other files?)

import pymongo, cgi, os, gridfs, re, html, codecs
from pprint import pprint

client = pymongo.MongoClient("mongodb://root:student@localhost:27017")
db = client["meteorcsv"]
coll = db["landings"]

print( 'Content-Type: text/html;charset=utf-8\r\n\r\n' )

fs = gridfs.GridFS(db)

print(html.header)
print("<h2>Info: </h2>")
form = cgi.FieldStorage()

#Gets ID of meteor from GET request
formMeteorID = form.getvalue('meteorID')
meteorID = int(formMeteorID) #parsing form value
author = form.getvalue('author')
comment = form.getvalue('comment')

mydoc = coll.find_one( #mydoc returns a dictionary variable
  {"id":meteorID},
  {"_id":0, "name":1, "mass (g)":1, "year":1} #can be changed to view desired info
)

# assumes database has section called "image" - can be changed - and is stored as base64 already
imageb64 = mydoc['image']

image = imageb64.decode('utf-8')

print(f"<img src=\"data:image/png;base64, {image}\"></img>")