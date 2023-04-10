#!/usr/bin/env python3

# Name - georesult.py
# Purpose - webpage that outputs the result of a geosearch string

import pymongo, cgi, os, gridfs, re, html, csv
from pprint import pprint
from pymongo import MongoClient
from pymongo import GEO2D

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

### REGEX
coll.drop_indexes
coll.create_index([("location", GEO2D)])

meteor_lat = form.getvalue('lat') #gets value of name from submitted form (GET)
meteor_long = form.getvalue('long')
met_lat = float(meteor_lat)
met_long = float(meteor_long)
max_distance = 100000

results = coll.find({
  "location": {
    "$near": {
      "$geometry": {
        "type": "Point",
        "coordinates": [met_long, met_lat]
      },
      "$maxDistance": max_distance
    }
  }
})

gquery = coll.find({
    "$and": [
    {"reclat": { "$gt":met_lat-1, "$lt":met_lat+1 }},
    {"reclong": { "$gt":met_long-1, "$lt":met_long+1 }}
  ]
})

print('''<h1>Meteorite List</h1>
          <ul class="meteor_list">''')
#instantiates variables from list of dictionary items
for x in gquery:
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

print('''<form action="/cgi-bin/meteorslist.py" method="get">
          <input type="submit" value="Return Home"/>
          <input type="hidden" name="pg" value="1">
        </form></br></br>''')

print('</br>')

print(html.footer)

# Outdated code:

#with open('Meteorite_Landings.csv', newline='', encoding='utf-8') as csvfile:
#  reader = csv.DictReader(csvfile)
#  places = [row for row in reader]

#for place in places:
#  geolocation = place["GeoLocation"] 
#  try:
#    latitude, longitude = geolocation.strip('()').split(', ')
#    latitude, longitude = float(latitude), float(longitude)
#    place["location"] = {"type": "Point", "coordinates": [float(longitude), float(latitude)]}
#    del place["GeoLocation"]
#  except ValueError:
#    pass

#coll.insert_many(places)

#new
#print( "meteor_lat: " + str(met_lat) );
#print( "meteor_long: " + str(met_long) );
#for result in results:
#  print(result)

#print(coll.index_information())

#gquery = {"location": {"$near": {"$geometry": {"type": "Point", "coordinates": [met_lat, met_long]}, "$maxDistance": max_distance}}}
#mydoc = coll.find(gquery)

#for result in mydoc:
  #print(result)

#for doc in coll.find({"loc": {"$near":[float(meteor_lat), float(meteor_long)]}}).limit(20):    -- for testing
  #pprint.pprint(doc)

#import cgitb
#cgitb.enable()

#from bson.son import SON
#gquery = {'loc': SON([("$near", [meteor_long, meteor_lat]), ("$maxDistance", 100)])}, {'_id':0, 'id':1, 'name':1, 'reclat':1, 'reclong':1} 

#gquery = {
#  "loc": {
#    "$near": {
#      "$geometry": {
#        "type": "Point" ,
#        "coordinates": [ float(meteor_long), float(meteor_lat) ]
#      },
#      "$maxDistance": 100
#    }
#  }
#}

#project = {'_id':0, 'id':1, 'name':1, 'reclat':1, 'reclong':1}
#print("<pre>" + str(gquery) + "</pre>")
#mydoc = coll.find(gquery,project).limit(collLimit).skip(collSkip * (pgNum - 1)) #limit query to 20
#print(mydoc)

#for mydoc in coll.find({"loc": {"$near": [meteor_long, meteor_lat]}}).limit(20):
#  gquery = pprint.pprint(mydoc)
