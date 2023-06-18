<?php

function unescape($str)
{
    $result = str_replace(' \" ', '"', $str);
    $result = str_replace(" \' ", "'", $result);
    $result = str_replace(' \n ', "<br>", $result);
    $result = str_replace(' \b ', "<b>", $result);
    $result = str_replace(' /b ', "</b>", $result);
    $result = str_replace(' \i ', "<i>", $result);
    $result = str_replace(' /i ', "</i>", $result);
    $result = str_replace(' \u ', "<u>", $result);
    $result = str_replace(' /u ', "</u>", $result);
    $result = str_replace(' \c ', "<code>", $result);
    $result = str_replace(' /c ', "</code>", $result);
    return $result;
}

$data = [];
if (($file = fopen("aptar.csv", "r")) !== false) {
    $id = 1;
    while (($row = fgetcsv($file)) !== false) {
        $tags = $row[0];
        $question = unescape($row[1]);
        $answer = unescape($row[2]);
        $data[] = [
            'id' => $id,
            'tags' => $tags,
            'question' => $question,
            'answer' => $answer,
        ];
        $id++;
    }
    fclose($file);
}
include 'aptar.phtml';
