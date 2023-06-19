<?php

$data = [];
$action = $_GET['action'] ?? $_POST['action'] ?? 'listar';

function unescape($str)
{
    $result = str_replace(' \" ', '"', $str);
    $result = str_replace(' \n ', "<br>", $result);
    $result = str_replace(' \b ', "<b>", $result);
    $result = str_replace(' /b ', "</b>", $result);
    $result = str_replace(' \i ', "<i>", $result);
    $result = str_replace(' /i ', "</i>", $result);
    $result = str_replace(' \u ', "<u>", $result);
    $result = str_replace(' /u ', "</u>", $result);
    return $result;
}

function escape($str)
{
    $result = str_replace('"', ' \" ', $str);
    $result = str_replace("<br>", ' \n ', $result);
    $result = str_replace("<b>", ' \b ', $result);
    $result = str_replace("</b>", ' /b ', $result);
    $result = str_replace("<i>", ' \i ', $result);
    $result = str_replace("</i>", ' /i ', $result);
    $result = str_replace("<u>", ' \u ', $result);
    $result = str_replace("</u>", ' /u ', $result);
    return $result;}

function load_data()
{
    global $data;
    if (($file = fopen("aptar.csv", "r")) !== false) {
        while (($row = fgetcsv($file)) !== false) {
            $tag = $row[0];
            $question = unescape($row[1]);
            $answer = unescape($row[2]);
            $data[] = [
                'tag' => $tag,
                'question' => $question,
                'answer' => $answer,
            ];
        }
        fclose($file);
    }
}

function save_data()
{
    global $data;
    if (($file = fopen("aptar.csv", "w")) !== false) {
        foreach ($data as $row) {
            $tag = $row['tag'];
            $question = escape($row['question']);
            $answer = escape($row['answer']);
            fputcsv($file, [$tag, $question, $answer]);
        }
        fclose($file);
    }
}

include 'aptar.phtml';
