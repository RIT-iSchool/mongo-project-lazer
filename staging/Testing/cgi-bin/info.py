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

### REGEX
meteor_name = form.getvalue('meteor_name')
author = form.getvalue('author')
comment = form.getvalue('comment')

regx = re.compile("^"+meteor_name, re.IGNORECASE)
mydoc = coll.find(
  {'name':{'$regex':regx}},
  {'_id':0, 'name':1, 'mass (g)':1, 'year':1}
).limit(20)

#Must have for loop in order to grab data
for x in mydoc:
  convString = str(x)
  convString = convString[1:][:-1]
  print(f"<p'>{convString}<p/></br>")

if author != " " and comment != " ":
  print("<h2>if statement works</h2>")

print(f'''<form action="/cgi-bin/info.py" method="get">
        <input type="hidden" name="meteor_name" value="{meteor_name}">
        Write a comment: </br>
        Author: <input type="text" name="author" value=" "/><br/>
        Comment: <input type="text" name="comment" value=" "/><br/>
        <input type="submit" value="Submit"/>
      </form>''')


print(html.footer)