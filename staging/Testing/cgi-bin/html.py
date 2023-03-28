header =  """
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meteors List</title>
  </head>
  <body>
    <main>
      <h1>Meteors List</h1>
      <form action="/cgi-bin/meteorslist.py" method="get">
        <input type="submit" value="Return Home"/>
      </form></br></br>
      <form action="/cgi-bin/result.py" method="get">
        Search: <input type="text" name="meteor_name"/><br/>
        <input type="submit" value="Submit"/>
      </form>

      <br/>
      
      <form action="/cgi-bin/georesult.py" method="get">
        Coordinates:<br/><input type="text" name="lat"/>
        <input type="text" name="long"/><br/>
        <input type="submit" value="Submit"/>
      </form>
      <br/>
""" 

footer = """</main>
</body>
</html>"""