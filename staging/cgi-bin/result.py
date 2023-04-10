#!/usr/bin/env python3

# Name - result.py
# Purpose - webpage that outputs the result of a search string 

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
mydocCount = 0

print(html.header) #from html.py
form = cgi.FieldStorage() #get data from url/form data

#get the value of page number in get request/url
pgNum = form.getvalue('pg')
pgNum = int(pgNum)
DEFAULT_SORT = 1
resultDirection = 0
### REGEX
meteor_name = form.getvalue('meteor_name') #gets value of name from submitted form (GET)
resultSort = form.getvalue('sort')
resultDirection = form.getvalue('direction')
if resultDirection == None:
  resultDirection = DEFAULT_SORT
if meteor_name != None:
  regx = re.compile("^"+meteor_name, re.IGNORECASE) #uses regex module to create regex with variable, searches for substrings, ignores case
  mydoc = coll.find(
    {'name':{'$regex':regx}}, #get name of regexed statement, returns name
    {'_id':0, 'id':1, 'name':1} #include ID not in print but to query on
  ).limit(collLimit).skip(collSkip * (pgNum - 1)).sort(str(resultSort), int(resultDirection)) #limit query to 20

  #count number of documents based off of previous query 
  #number determines if next button should appear or not
  mydocCount = coll.count_documents(
    {'name':{'$regex':regx}}, 
    skip=(collSkip * (pgNum - 1)), 
    limit=collLimit
  )
else:
  mydoc = coll.find(
  {},{'_id':0, 'id':1, 'name':1}
).limit(collLimit).skip(collSkip * (pgNum - 1)).sort(str(resultSort), int(resultDirection)) #retrieving data from MongoDB

print('''<h1>Meteorite List</h1>
          <ul class="meteor_list">''')
#instantiates variables from list of dictionary items
for x in mydoc:
  meteorID = x['id']
  meteorName = x['name']
  meteorName = meteorName.encode(encoding='ascii', errors="xmlcharrefreplace").decode('CP1252') #used to parse the latin characters
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

print('</br>')
#check if back or next need to appear
if pgNum > 1:
  print(f'<a href="/cgi-bin/result.py?meteor_name={meteor_name}&pg={pgNum - 1}">Back</a>')
if mydocCount == collLimit:
  print(f'<a href="/cgi-bin/result.py?meteor_name={meteor_name}&pg={pgNum + 1}">Next</a>')

print(html.footer)
