#!/usr/bin/env python3

# Name - info.py
# Purpose - webpage that shows user info of selected meteor 

import pymongo, cgi, os, gridfs, re, html
from pprint import pprint

client = pymongo.MongoClient("mongodb://root:student@localhost:27017")
db = client["meteorcsv"]
coll = db["landings"]

print( 'Content-Type: text/html;charset=utf-8\r\n\r\n' )

print(html.header)
print("<h2>Info: </h2>")
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
  {"_id":0, "name":1, "mass (g)":1, "year":1, "userComment":1} #can be changed to view desired info
)

#instantiates variables from returned dictionary
meteorName = mydoc['name']
meteorMass = mydoc['mass (g)']
meteorYear = mydoc['year']
if 'userComment' in str(mydoc): #check if comments already exists
  meteorComment = mydoc['userComment']
print(f"<p'>Name: {meteorName}<p/>")
print(f"<p'>Mass: {meteorMass}(g)<p/>")
print(f"<p'>Year: {meteorYear}<p/>")

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


print(html.footer)
