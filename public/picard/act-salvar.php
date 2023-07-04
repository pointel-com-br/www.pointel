<?php
$id = $_POST['id'] ?? -1;
$tag = trim($_POST['tag'] ?? '');
$question = trim($_POST['question'] ?? '');
$question = unescape_editor($question);
$answer = trim($_POST['answer'] ?? '');
$answer = unescape_editor($answer);

if (!str_ends_with($question, "?")) {
    $question .= "?";
}
if (!str_ends_with($answer, ".") || !str_ends_with($answer, "`")) {
    $answer .= ".";
}

$message = 'Processando...';
$retorno = 'index.php?action=grafar&tag=' . $tag;
if ($tag == '' || $question == '' || $answer == '') {
    $message = 'Erro: dados incompletos.';
} else {
    load_data();
    if ($id != -1) {
        $data[$id]['tag'] = $tag;
        $data[$id]['question'] = $question;
        $data[$id]['answer'] = $answer;
        $retorno = 'index.php?action=sortear';
    } else {
        $row = [
            'tag' => $tag,
            'question' => $question,
            'answer' => $answer,
        ];
        $data[] = $row;
    }
    save_data();
    $message = 'Salvo com sucesso.';
}
