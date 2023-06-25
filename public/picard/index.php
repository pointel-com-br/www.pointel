<?php

$data = [];
$action = $_GET['action'] ?? $_POST['action'] ?? 'listar';

function unescape(string $str): string
{
    $result = str_replace(' \" ', '"', $str);
    $result = str_replace(' \n ', "<br>", $result);
    $result = str_replace(' \s ', "&nbsp;", $result);
    $result = str_replace(' \b ', "<b>", $result);
    $result = str_replace(' /b ', "</b>", $result);
    $result = str_replace(' \i ', "<i>", $result);
    $result = str_replace(' /i ', "</i>", $result);
    $result = str_replace(' \u ', "<u>", $result);
    $result = str_replace(' /u ', "</u>", $result);
    return $result;
}

function escape(string $str): string
{
    $result = str_replace('"', ' \" ', $str);
    $result = str_replace("<br>", ' \n ', $result);
    $result = str_replace('&nbsp;', " \s ", $result);
    $result = str_replace("<b>", ' \b ', $result);
    $result = str_replace("</b>", ' /b ', $result);
    $result = str_replace("<i>", ' \i ', $result);
    $result = str_replace("</i>", ' /i ', $result);
    $result = str_replace("<u>", ' \u ', $result);
    $result = str_replace("</u>", ' /u ', $result);
    return $result;
}

function unescape_editor(string $str): string {
    $result = "";
    $was_break = false;
    foreach (mb_str_split(unescape($str)) as $char) {
        if ($char == "\n") {
            $was_break = true;
            $result .= "<br>";
        } else if ($char == "\r") {
        } else if ($char == " ") {
            if ($was_break) {
                $result .= "&nbsp;";
            } else {
                $result .= " ";
            }
        } else {
            $was_break = false;
            $result .= $char;
        }
    }
    return $result;
}

function escape_editor(string $str): string {
    $result = escape($str);
    $result = str_replace(' \n ', "\n", $result);
    $result = str_replace(' \s ', " ", $result);
    return $result;
}

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

require 'index.phtml';