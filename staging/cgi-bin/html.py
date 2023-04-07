#!/usr/bin/env python3

# Name - html.py
# Purpose - file for storing the header and footer html code 

header =  """
  <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="khttps://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="../assets/css/styles.css">
  <title> Meteors List </title>
</head>

<body>
  <header>
    <div class="navbar">
      <figure>
        <img class="logo" src="/assets/logos/navbar_logo.png" alt="Company Logo">
      </figure>
      <nav>
        <ul class="navbar">
          <li>
            <form action="/cgi-bin/result.py" method="get">
              &emsp; <input class="meteor_search" type="text" name="meteor_name"
                placeholder="     Search for a meteorite..."/><br />
                <input type="hidden" name="pg" value="1">

                <input type="radio" id="name1" name="sort" value="name">
                <label for="name1">Name</label></br>

                <input type="radio" id="mass1" name="sort" value="mass (g)">
                <label for="mass1">Mass</label></br>

                <input type="radio" id="year1" name="sort" value="year">
                <label for="year1">Year</label>
                </br></br>
                <input type="radio" id="asc" name="direction" value="-1">
                <label for="asc">Ascending</label>
                <input type="radio" id="dsc" name="direction" value="1">
                <label for="dsc">Descending</label>
                <input type="submit" value="Submit">
            </form>
          </li>
          &emsp; &emsp;
          <li>
            <form action="/cgi-bin/georesult.py" method="get">
              Coordinates: &emsp; <input type="text" name="lat" placeholder="Latitude..." />
              <input type="text" name="long" placeholder="Longitude..." />
              <button class="meteor-search-btn" type="button" 
                onclick="if (document.getElementsByName('lat')[0].value !== '' && document.getElementsByName('long')[0].value !== '') 
                {this.form.submit()} else {alert('Please fill in both the latitude and longitude fields.')}">Search
              </button>
            </form>
          </li>
        </ul>
          <form action="/cgi-bin/result.py" method="get">
          
          </form>
      </nav>
    </div>
  </header>
  <main>
""" 

footer = """</main>
</body>
</html>"""

# Old Header/Footer
# header =  """
#   <!DOCTYPE html>
#   <html lang="en">
#   <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Meteors List</title>
#   </head>
#   <body>
#     <main>
#       <h1>Meteors List</h1>
#       <form action="/cgi-bin/meteorslist.py" method="get">
#         <input type="submit" value="Return Home"/>
#         <input type="hidden" name="pg" value="1">
#       </form></br></br>
#       <form action="/cgi-bin/result.py" method="get">
#         Search: <input type="text" name="meteor_name"/><br/>
#         <input type="submit" value="Submit"/>
#         <input type="hidden" name="pg" value="1">
#       </form>

#       <br/>
      
#       <form action="/cgi-bin/georesult.py" method="get">
#         Coordinates:<br/><input type="text" name="lat"/>
#         <input type="text" name="long"/><br/>
#         <input type="submit" value="Submit"/>
#         <input type="hidden" name="pg" value="1">
#       </form>
#       <br/>
# """ 

# footer = """</main>
# </body>
# </html>"""