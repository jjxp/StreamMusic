<?php

$title	=	$_POST["title"];
$artist	=	$_POST["artist"];
$album	=	$_POST["album"];
$url	=	$_POST["url"];

$script = 'python main.py "'.$title.'" "'.$artist.'" "'.$album.'" "'.$url.'"';

session_start();

$_SESSION["output"] = exec($script);

header('Location: new.php');

?>