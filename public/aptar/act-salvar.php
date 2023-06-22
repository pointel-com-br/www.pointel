<?php
$id = $_POST['id'] ?? -1;
$tag = trim($_POST['tag'] ?? '');
$question = trim($_POST['question'] ?? '');
$question = str_replace("\n", "<br>", $question);
$question = str_replace("\r", "", $question);
$answer = trim($_POST['answer'] ?? '');
$answer = str_replace("\n", "<br>", $answer);
$answer = str_replace("\r", "", $answer);

$message = 'Processando...';
$retorno = 'index.php?action=sortear';
if ($tag == '' || $question == '' || $answer == '') {
    $message = 'Erro: dados incompletos.';
} else {
    load_data();
    if ($id != -1) {
        $data[$id]['tag'] = $tag;
        $data[$id]['question'] = $question;
        $data[$id]['answer'] = $answer;
        $retorno = 'index.php?action=grafar&id=' . $id;
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
