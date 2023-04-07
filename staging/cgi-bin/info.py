#!/usr/bin/env python3

# Name - info.py
# Purpose - webpage that shows user info of selected meteor 

import pymongo, cgi, os, gridfs, re, html
from pprint import pprint

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

print(html.header)

form = cgi.FieldStorage()

#Gets ID of meteor from GET request
formMeteorID = form.getvalue('meteorID')
meteorID = int(formMeteorID) #parsing form value
author = form.getvalue('author')
comment = form.getvalue('comment')

if(author != None and comment != None): #checks if Nothing is submitted
  if (author.isspace() == False and comment.isspace() == False):
    updateSearch = {"id": meteorID}
    updateComment = {
      "$push": {"userComment": {author:comment}} 
      }
    coll.update_one(updateSearch, updateComment)
  else:
    print("ERROR: Nothing Submitted")


mydoc = coll.find_one( #mydoc returns a dictionary variable
  {"id":meteorID},
  {"_id":0, 
   "name":1, 
   "mass (g)":1, 
   "year":1, 
   "userComment":1, 
   "GeoLocation":1, 
   "recclass":1,
   "nametype":1} #can be changed to view desired info
)

#instantiates variables from returned dictionary
meteorName = mydoc['name']
meteorName = meteorName.encode(encoding='ascii', errors="xmlcharrefreplace").decode('CP1252') #used to parse the latin characters
meteorMass = mydoc['mass (g)']
meteorYear = mydoc['year']
meteorGeo = mydoc['GeoLocation']
meteorClass = mydoc['recclass']
meteorNameType = mydoc['nametype']
if 'userComment' in str(mydoc): #check if comments already exists
  meteorComment = mydoc['userComment']

imgSearch = meteorName.lower() + ".jpg"
DEFAULT_IMG = 'default.jpg'

cursor = fsFilesColl.find({"filename":imgSearch}).limit(1)
for item in cursor:
  new_img = fs.get(item['_id']).read()
  filename = item['filename']

  with open(f"assets/images/{filename}", "wb") as outfile:
    outfile.write(new_img)

print(f'''<h1>{meteorName}</h1>
    <div class="info-container">''')
if os.path.isfile(f"assets/images/{meteorName.lower()}.jpg"): #if the name of the meteor is found in the image folder
  print(f'''
        <img src="../assets/images/{meteorName.lower()}.jpg" alt="Meteorite Image" class="meteor-info-img"/>
        <div class="info">
            <p><strong>Coordinates: </strong> {meteorGeo}</p>
            <p><strong>Fell In: </strong> {meteorYear}</p>
            <p><strong>Class: </strong> {meteorClass}</p>
            <p><strong>Mass: </strong> {meteorMass} (g)</p>
            <p><strong>Name Type: </strong> {meteorNameType}</p>
        </div>
    </div>
      ''')
else: #If image is not found in assets/images
  print(f'''
        <img src="../assets/logos/{DEFAULT_IMG}" alt="Meteorite Image" class="meteor-info-img"/>
        <div class="info">
            <p><strong>Coordinates: </strong> {meteorGeo}</p>
            <p><strong>Fell In: </strong> {meteorYear}</p>
            <p><strong>Class: </strong> {meteorClass}</p>
            <p><strong>Mass: </strong> {meteorMass} (g)</p>
            <p><strong>Name Type: </strong> {meteorNameType}</p>
        </div>
    </div>
      ''')

#check if comments already exists
if 'userComment' in str(mydoc):
  #iterating over the array of documents
  for document in meteorComment:
    for returnedAuthor, returnedComment in document.items(): #getting the key value pairs of each document
      print(f'''
        <ul>
          <li>Author: {returnedAuthor}</li>
          <li>{returnedComment}</li>
        </ul>
      ''')
    #print(f"<p>Comment: {list(userComment)}<p/>")

#changed form to use meteorID to send data
print(f'''<form action="/cgi-bin/info.py" method="get">
        <input type="hidden" name="meteorID" value="{meteorID}">
        Write a comment: </br>
        Author: <input type="text" name="author" value="" required/><br/>
        Comment: <input type="text" name="comment" value="" required/><br/>
        <input type="submit" value="Submit"/>
      </form>''')

print('''</br><form action="/cgi-bin/meteorslist.py" method="get">
          <input type="submit" value="Return Home"/>
          <input type="hidden" name="pg" value="1">
        </form></br></br>''')

print(html.footer)
