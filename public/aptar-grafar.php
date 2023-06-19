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
    $answer = $row['answer'];
}
