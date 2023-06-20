<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="/main.css">
  <title>Pointel - Pubz</title>
</head>

<body>
  <div>
    <a href="index.php">
      <img src="/assets/pointel.png" style="height: 36px; width: 36px;" />
      <h1>Pointel</h1>
      <h2>Pubz</h2>
    </a>
  </div> <?php
$files = array_diff(scandir('.'), array('.', '..', 'index.php'));
foreach ($files as $file) {
    if (!is_dir($file)) {
        echo '<h3><a href="' . $file . '">' . $file . '</a></h3>';
    }
}?>
</body>

</html>