<?php
$id = $_GET['id'] ?? 0;
$tag = '';
$question = '';
$answer = '';

if ($id != 0) {
    load_data();
    $row = $data[$id];
    $tag = $row['tag'];
    $question = $row['question'];
    $answer = $row['answer'];
}
