<?php
$id = $_GET['id'] ?? -1;
$tag = '';
$question = '';
$answer = '';

if ($id != -1) {
    load_data();
    $row = $data[$id];
    $tag = $row['tag'];
    $question = $row['question'];
    $question = str_replace("<br>", "\n", $question);
    $answer = $row['answer'];
    $answer = str_replace("<br>", "\n", $answer);
}
