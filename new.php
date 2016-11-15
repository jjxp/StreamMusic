<html>
<head>
	<title>StreamMusic | Add new song</title>
	<link href="style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
	<div class="container">  
	  <form id="contact" action="addsong.php" method="post">
		<h3>Add a new song</h3>
		<h4>StreamMusic</h4>
		<fieldset>
		  <input placeholder="Song name" type="text" name="title" tabindex="1" required autofocus>
		</fieldset>
		<fieldset>
		  <input placeholder="Artist name" type="text" name="artist" tabindex="2" required>
		</fieldset>
		<fieldset>
		  <input placeholder="Album name" type="text" name="album" tabindex="3" required>
		</fieldset>
		<fieldset>
		  <input placeholder="YouTube URL" type="url" name="url" tabindex="4" required>
		</fieldset>
		<fieldset>
		  <button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Submit</button>
		</fieldset>
		<p class="copyright">StreamMusic</p>
	  </form>
	</div>
</body>
</html>