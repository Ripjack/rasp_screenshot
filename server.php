<?php
$post = file_get_contents('php://input');
$jsonobj = json_decode($post, true);
#var_dump($jsonobj)
$content = $jsonobj['file'];
#var_dump($content);
$name = $jsonobj['name'];
#var_dump($name);
$decodeddata = base64_decode($content);
$file = fopen($name, 'wb');
fwrite($file, $decodeddata);
fclose($file);
?>