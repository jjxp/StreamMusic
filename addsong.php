<?php

$songs	=	$_POST["songs"];

$script = 'python2.7 main.py "' . $songs . '"';

session_start();

$_SESSION["output"] = exec($script);

header('Location: index.php?playlistId=' . $_SESSION["output"]);

?>