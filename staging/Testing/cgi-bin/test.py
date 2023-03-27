import pymongo
from pprint import pprint
myclient = pymongo.MongoClient("mongodb://root:student@localhost:27017")

print( 'Content-Type: text/html;charset=utf-8\r\n\r\n' )

print( """
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TESTING CGI-BIN</title>
  </head>
  <body>
    <main>
      <h1>TESTING CGI-BIN</h1>
      <p><a href="../">Back to form</a></p>
""" )

mydb = myclient["meteorcsv"]
mycol = mydb["landings"]

mydoc = mycol.find()
mydoc.limit(10)
for x in mydoc:
  print(f"<p>{x}<p>")

print("""</main>
</body>
</html>""")