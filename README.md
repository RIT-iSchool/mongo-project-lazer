[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10451123&assignment_repo_type=AssignmentRepo)

<h1>Important Links:</h1>
<ul>
	<li>https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh</li>
	<li>https://catalog.data.gov/dataset/meteorite-landings</li>
</ul>

<h1>Tech Stack:</h1>
<ul>
	<li>HTML/CSS</li>
	<li>Python</li>
	<li>MongoDB</li>
	<li>Linux</li>	
</ul>

<h1>Issues:</h1>
<ul>
	<li>Loaded in .json from NASA website, but might be hard to parse data. Need to discuss if .csv would be easier to use.</li>
	<li>After more testing/research, plain Javascript cannot be used. Switched to Python/HTML instead.</li>
	<li>Had to do research on how PyMongo and CGI modules worked.</li>
	<li>Figured out how to clean the data properly.</li>
	<li>Deciding how to sort and what to sort on.</li>
	<li>Figured out that instead of parsing dictionary object to str, instead instantiate variables using the dictionary</li>
	<li>Unsure how to send data from page to page</li>
	<li>Had to figure out how to properly correlate the images to the meteor name</li>
	<li>Figured out how to only have the necessary images in the images folder for each page</li>
	<li>In Windows, file names are not case-sensitive, where Linux is. Had to have the EXACT name for each image, case sensitive.</li>
	<li>Had trouble with foreign latin characters, figured out how to use encoding/decoding</li>
	<li>Issues with sorting as not every field contained information. For example, many meteors do not have year's or masses'</li>
	<li>Had to modify data, some documents had no values in field which messed up sorting, had to set default values</li>
	<li>Search should be able to organize selections by title, date, etc.</li>
	<li>User should be able to annotate the document with comments which then should be stored in the DB.</li>
</ul>

<h1>Completed:</h1>
<ul>
	<li>Loaded in data into DB</li>
	<li>Decide which stack to use: MERN or LAMJ (Linux, Apache, MongoDB, JavaScript)</li>
	<li>User should be able to view the document once entering into it</li>
	<li>User should be able to keep searching until they exit the application</li>
	<li>Create a GUI that can search the database off of a search string</li>
	<li>Search returns selection list of documents</li>
	<li>Clean GUI design</li>
	<li>Some documents should have images and should be stored using GridFS</li>
</ul>
<h1>To Do:</h1>
<ul>
	<li>In GUI, create another search field to find records in a certain area (using MongoGeo)</li>
</ul>
