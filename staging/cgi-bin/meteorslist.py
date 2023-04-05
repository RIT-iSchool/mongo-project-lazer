#!/usr/bin/env python3

# Name - meteorslist.py
# Purpose - main webpage that lists the initial meteors 

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

form = cgi.FieldStorage() #get data from url/form data

#get the value of page number in get request/url
pgNum = form.getvalue('pg')
pgNum = int(pgNum)

mydoc = coll.find(
  {},{'_id':0, 'id':1, 'name':1}
).limit(collLimit).skip(collSkip * (pgNum - 1)) #retrieving data from MongoDB
#limit output to 20 items, change 20 for desired number of items displayed

#count number of documents based off of previous query 
#number determines if next button should appear or not
mydocCount = coll.count_documents(
  {},
  skip=(collSkip * (pgNum - 1)), 
  limit=collLimit
)

print('''<h1>Meteorite List</h1>
          <ul class="meteor_list">''')
#instantiates variables from list of dictionary items
#prints out meteors name as links so user can view each individual meteor
for x in mydoc:
  meteorID = x['id']
  meteorName = x['name']
  print(f'''
  <li>
    <div class="meteor-container">
    <a href='/cgi-bin/info.py?meteorID={meteorID}'>{meteorName}</a>
    <img class="meteor-image" src="../assets/images/meteorite_test.jpeg" alt="{meteorName}">
  </li>
  ''')

print('''<form action="/cgi-bin/meteorslist.py" method="get">
          <input type="submit" value="Return Home"/>
          <input type="hidden" name="pg" value="1">
        </form></br></br>''')
#check if back or next need to appear
if pgNum > 1:
  print(f'<a href="/cgi-bin/meteorslist.py?pg={pgNum - 1}">Back</a>')
if mydocCount == collLimit:
  print(f'<a href="/cgi-bin/meteorslist.py?pg={pgNum + 1}">Next</a>')

print(html.footer)

