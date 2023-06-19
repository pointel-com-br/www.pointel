<?php
$id = $_POST['id'] ?? -1;
$tag = trim($_POST['tag'] ?? '');
$question = trim($_POST['question'] ?? '');
$answer = trim($_POST['answer'] ?? '');

$message = 'Processando...';
if ($tag == '' || $question == '' || $answer == '') {
    $message = 'Erro: Dados incompletos.';
} else {
    load_data();
    if ($id != -1) {
        $data[$id]['tag'] = $tag;
        $data[$id]['question'] = $question;
        $data[$id]['answer'] = $answer;
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