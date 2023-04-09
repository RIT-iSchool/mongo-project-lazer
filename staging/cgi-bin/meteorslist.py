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
fsFilesColl = db["fs.files"]

#Deletes all images in images folder
imgDir = 'assets/images'
for f in os.listdir(imgDir):
  os.remove(os.path.join(imgDir, f))

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

#print(f'<img alt="{filename}" src="../assets/images/{filename}" width=500') #sets img as file that was just written out to

print('''<div class="filter-container">
      <h1>Meteorite List</h1>
      <form class="filter">
        
        <label class="radio-inline">
          Filter By:
          <input type="radio" name="optradio" checked>Year
        </label>
        <label class="radio-inline">
          <input type="radio" name="optradio">Mass
        </label>
        <label class="radio-inline">
          <input type="radio" name="optradio">Ascending
        </label>
        <label class="radio-inline">
          <input type="radio" name="optradio">Descending
        </label>
      </form>
    </div>
    <div class="meteor-list">
      <ul class="meteor_list">''')
#instantiates variables from list of dictionary items
#prints out meteors name as links so user can view each individual meteor
for x in mydoc:
  meteorID = x['id']
  meteorName = x['name']
  meteorName = meteorName.encode('unicode_escape').decode('CP1252') #used to parse the latin characters
  imgSearch = meteorName.lower() + ".jpg"
  DEFAULT_IMG = 'default.jpg'

  cursor = fsFilesColl.find({"filename":imgSearch}).limit(1)
  for item in cursor:
    new_img = fs.get(item['_id']).read()
    filename = item['filename']

    with open(f"assets/images/{filename}", "wb") as outfile:
      outfile.write(new_img)

  print(f'''
  <li>
    <div class="meteor-container">
    <a href='/cgi-bin/info.py?meteorID={meteorID}'>{meteorName}</a>
  ''')
  if os.path.isfile(f"assets/images/{meteorName.lower()}.jpg"): #if the name of the meteor is found in the image folder
    print(f'''
          <img class="meteor-image" src="../assets/images/{meteorName.lower()}.jpg" alt="{meteorName}">
        </div>
      </li>
    ''')
  else:
    print(f'''
          <img class="meteor-image" src="../assets/logos/{DEFAULT_IMG}" alt="{meteorName}"> 
        </div>
      </li>
    ''')

#check if back or next need to appear
if pgNum > 1:
  print(f'<a href="/cgi-bin/meteorslist.py?pg={pgNum - 1}">Back</a>')
if mydocCount == collLimit:
  print(f'<a href="/cgi-bin/meteorslist.py?pg={pgNum + 1}">Next</a>')

print(html.footer)

