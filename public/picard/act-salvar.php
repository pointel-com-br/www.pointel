<?php
$id = $_POST['id'] ?? -1;
$monitorar = $_POST['monitorar'] ?? 0;
$tag = trim($_POST['tag'] ?? '');
$question = trim($_POST['question'] ?? '');
$question = unescape_editor($question);
$answer = trim($_POST['answer'] ?? '');
$answer = unescape_editor($answer);

$question = strtoupper(substr($question, 0, 1)) . substr($question, 1);

if (!str_ends_with($question, "?") && !str_ends_with($question, ".")) {
    $question .= "?";
}

if (!str_ends_with($answer, ".") && !str_ends_with($answer, "`")) {
    $answer .= ".";
}

$message = 'Processando...';
$retorno = 'index.php?action=grafar&tag=' . $tag . '&monitorar=' . $monitorar;
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
