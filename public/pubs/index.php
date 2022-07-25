<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pointel - Pubs</title>
</head>

<body>
  <h1>Pointel</h1>
  <h2>Pubs</h2> <?php
$files = array_diff(scandir('.'), array('.', '..', 'index.php'));
foreach ($files as $file) {
    if (!is_dir($file)) {
        echo '<h3><a href="' . $file . '">' . $file . '</a></h3>';
    }
}?>
</body>

</html>