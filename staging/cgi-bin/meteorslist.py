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
collLimit = 20
collSkip = 20

print(html.header) #from html.py

form = cgi.FieldStorage() #get data from url/form data

#get the value of page number in get request/url
pgNum = form.getvalue('pg')
pgNum = int(pgNum)

mydoc = coll.find(
  {},{'_id':0, 'name':1}
).limit(collLimit).skip(collSkip * (pgNum - 1)) #retrieving data from MongoDB
#limit output to 20 items, change 20 for desired number of items displayed

#count number of documents based off of previous query 
#number determines if next button should appear or not
mydocCount = coll.count_documents(
  {},
  skip=(collSkip * (pgNum - 1)), 
  limit=collLimit
)

#takes query from MongoDB and converts dictionary type object to string
#prints out meteors name as links so user can view each individual meteor
for x in mydoc:
  convString = str(x)
  convString = convString[10:][:-2] #substring to clean string
  print(f"<a href='/cgi-bin/info.py?meteor_name={convString}'>{convString}</a></br>")

print('</br>')
#check if back or next need to appear
if pgNum > 1:
  print(f'<a href="/cgi-bin/meteorslist.py?pg={pgNum - 1}">Back</a>')
if mydocCount == collLimit:
  print(f'<a href="/cgi-bin/meteorslist.py?pg={pgNum + 1}">Next</a>')

print(html.footer)

