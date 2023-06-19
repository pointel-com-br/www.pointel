<?php
load_data();
$id = array_rand($data);
$row = $data[$id];
$tag = $row['tag'];
$question = $row['question'];
$answer = $row['answer'];
