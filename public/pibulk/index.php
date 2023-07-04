<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="/main.css">
  <title>Pointel - Pubz (Power Intelligence)</title>
</head>

<body>
  <div id="topPointel">
    <img src="/assets/pointel.png" />
    <h1><a href="https://www.pointel.com.br/">Pointel</a></h1>
    <h2><a href="index.php">PiBulk</a></h2>
  </div> <?php
$files = array_diff(scandir('.'), array('.', '..', 'index.php'));
foreach ($files as $file) {
    if (!is_dir($file)) {
        echo '<h3><a href="' . $file . '">' . $file . '</a></h3>';
    }
}?>
</body>

</html>