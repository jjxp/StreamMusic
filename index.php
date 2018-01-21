<html>
<head>
	<title>StreamMusic</title>
	<link href="style.css" rel="stylesheet" type="text/css"/>
	<meta charset="UTF-8">
</head>
<body>
	<div class="container">  
	  <form id="contact" action="addsong.php" method="post">
		<h3>Nueva lista</h3>
		<h4>StreamMusic</h4>
		<textarea placeholder="Escribe aquí las canciones que quieras, una por línea." name="songs" cols="40" rows="5" required autofocus></textarea>
		
		<button name="submit" type="submit" id="contact-submit" data-submit="Procesando...">Aceptar</button>
		</fieldset>
		<p class="copyright">StreamMusic</p>
	  </form>
	</div>
</body>
</html>