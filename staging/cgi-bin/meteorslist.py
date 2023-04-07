#!/usr/bin/env python3

# Name - meteorslist.py
# Purpose - main webpage that lists the initial meteors 

import pymongo, cgi, os, gridfs, re, html
from pprint import pprint

#connecting to the database, getting the landings collection
client = pymongo.MongoClient("mongodb://root:student@localhost:27017")
db = client["meteorcsv"]
coll = db["landings"]
fs = gridfs.GridFS(db)

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

fsFilesColl = db["fs.files"]
cursor = fsFilesColl.find({}).sort("_id", -1)
for item in cursor:
  new_img = fs.get(item['_id']).read()
  filename = item['filename']

  with open(f"assets/images/{filename}", "wb") as outfile:
    outfile.write(new_img)
  #print(f'<img alt="{filename}" src="../assets/images/{filename}" width=500') #sets img as file that was just written out to

print('''<h1>Meteorite List</h1>
          <ul class="meteor_list">''')
#instantiates variables from list of dictionary items
#prints out meteors name as links so user can view each individual meteor
for x in mydoc:
  meteorID = x['id']
  meteorName = x['name']
  DEFAULT_IMG = 'default.jpg'
  print(f'''
  <li>
    <div class="meteor-container">
    <a href='/cgi-bin/info.py?meteorID={meteorID}'>{meteorName}</a>
  ''')
  if os.path.isfile(f"assets/images/{meteorName}.jpg"): #if the name of the meteor is found in the image folder
    print(f'''
          <img class="meteor-image" src="../assets/images/{meteorName}.jpg" alt="{meteorName}">
        </div>
      </li>
    ''')
  else:
    print(f'''
          <img class="meteor-image" src="../assets/images/{DEFAULT_IMG}" alt="{meteorName}"> 
        </div>
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

