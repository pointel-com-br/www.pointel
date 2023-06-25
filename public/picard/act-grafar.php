<?php
$id = $_GET['id'] ?? -1;
$tag = '';
$question = '';
$answer = '';

if ($id != -1) {
    load_data();
    $row = $data[$id];
    $tag = $row['tag'];
    $question = escape_editor($row['question']);
    $answer = escape_editor($row['answer']);
}
