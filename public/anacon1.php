<?php
$sender = "mail@pointel.com.br";
$headers = "MIME-Version: 1.1\n";
$headers .= "Content-type: text/plain; charset=UTF-8\n";
$headers .= "From: $sender\n";
$headers .= "Return-Path: $sender\n";
$name = $_POST['name'];
$fone = $_POST['fone'];
$mail = $_POST['mail'];
$uuid = uniqid(rand(), true);
$message = "Solicitação de Análise Contextual:\n";
$message .= "Nome: $name\n";
$message .= "Telefone: $fone\n";
$message .= "E-mail: $mail\n";
$message .= "UUID: $uuid\n";
$send = mail("emuvi@outlook.com.br", "Solicitação de Análise Contextual", $message, $headers, "-f$sender");
if ($send) {
    echo "Mensagem enviada com sucesso!";
    header('Location: anacon2.htm');
} else {
    echo "Erro ao enviar mensagem!";
}
exit(0);
