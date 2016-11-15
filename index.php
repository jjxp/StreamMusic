<html>
<head>
	<title>StreamMusic | Add new song</title>
	<link href="style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
	<div class="container">
		<div id="contact">
			<h3>StreamMusic</h3>
			<?php
				$path = '/var/www/javgarcal.com/public_html/streammusic/files/';
				$files = scandir($path);
				
				$i = 0;
				foreach($files as $f) {
					if($i++ < 2) {
						continue;
					}
					echo $f, '<br>';
					$albums = scandir($path . '' . $f . '/');
					$ii = 0;
					foreach($albums as $a) {
						if($ii++ < 2) {
							continue;
						}
						echo $a, '<br>';
						$songs = scandir($path . '' . $f . '/' . $a . '/');
						$iii = 0;
						foreach($songs as $s) {
							if($iii++ < 2) {
								continue;
							}
							echo '<a href="files/'.$f.'/'.$a.'/'.$s.'">'.$s.'</a>', '<br>';
						}
					}
					echo '<hr/>';
				}
			?>
			<p class="copyright">StreamMusic</p>
		</div>
	</div>
</body>
</html>