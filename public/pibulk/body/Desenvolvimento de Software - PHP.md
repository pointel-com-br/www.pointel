# Desenvolvimento de Software - PHP

Índice

1) PHP-Teoria

2) PHP - Questões Comentadas

3) PHP - Lista de Questões

Conceitos Básicos

PHP

INCIDÊNCIA EM PROVA: MÉDIA

O ano era 1994! Um programador dinamarquês chamado Rasmus Lerdorf criou uma série de scripts em Perl para utilizar em coisas simples de sua página pessoal. Empolgado com o resultado, ele reescreveu esses scripts em C - por questões de desempenho adicionando a capacidade de trabalhar com formulários web e bancos de dados.
Assim era possível criar páginas web dinâmicas, possibilitando que um navegador passasse parâmetros para outros programas alocados em um servidor web. Lerdorf condensou tudo isso em um pacote de scripts e chamou de Personal Home Page tools (PHP),que, inicialmente, não tinha a menor intenção de ser uma linguagem de programação.
Enfim, essa ideia evoluiu rapidamente e, no ano seguinte, foi lançado o PHP/FI (Fl = FormsInterpreter), que incluía um interpretador de comandos SQL. Ele, então,
resolveu publicar em um grupo de discussões (cujo link é apresentado a seguir), de modo a encontrar bugs e melhorar o código por meio das contribuições da comunidade.
Um pouco mais tarde, dois programadores israelenses chamados Zeev Suraski e
Andi Gutmans se juntaram para reescrever o parser, formando a base do PHP3, e modificando o nome da linguagem para PHP Hypertext Preprocessor (PHP). Em seguida, ambos começaram a reescrever o núcleo da linguagem, produzindo o Zend Engine!
E 0 que era Zend Engine, professor? Bem, o nome vinha da junção de Zeev e Andi. Ele era o interpretador do PHP! Mais adiante, foi lançado o PHP4 com mais recursos de orientação a objetos,porém com problemas sérios em relação aos ponteiros. Em 2004, foi lançado o PHP5 com inúmeras melhorias de performance e funcionalidades - atualmente está na versão 7.1.0.
Bem... dado esse breve histórico, vamos dar continuidade! Professor, afinal de contas 0 que é PHP?Ora, é uma linguagem de programação de scripts, interpretada, de alto nível, open-source,gratuita, server-side, dinamicamente/fracamente tipada, estruturada e orientada a objetos,portável, robusta e eficiente utilizada para desenvolvimento web.

Caraça, foi tanta coisa de uma vez que nem eu entendi! Vamos explicar por partes! Primeiro de tudo,é uma linguagem de programação de scripts, portanto - obviamente -
ela serve para programar scripts! E 0 que é isso, professor? É um conjunto de instruções que geralmente são executadas dentro de outras linguagens e/ou programas.
Voltando, então! O PHP é uma linguagem de programação de scripts, isto é,
escreve scripts que estendem as funcionalidades de outra linguagem de programação e/ou programas. Ok! Mas a definição diz que ela é interpretada! Bem, isso só complementa o que acabamos de ver, visto que todas as linguagens de script são interpretadas.
Percebam que aqui não ocorre compilação, criação de código-objeto, nada disso!
A Máquina Virtual recebe o código-fonte, interpreta e roda instrução a instrução em tempo de execução. Bacana?! EPHP é uma linguagem de alto nível? Sim, essa é fácil! É uma linguagem que se aproxima mais da linguagem humana do que da linguagem de máquina!
O nível de abstração é alto, isto é, o programador não acessa ponteiros,
não manipula a memória,
não escova bits, nada disso! Logo, é uma linguagem de alto nível. E ela é open-source? Sim! Na verdade, o PHP é atualmente o software open-source mais utilizado em empresas no planeta1, isto é, código aberto, distribuição livre e aquele blábláblá todo!
Ele também é gratuito! Ué, professor... você já disse que ele é livre!
Sim, mas ser livre não significa ser gratuito. No entanto, nesse caso ele é livre e gratuito! Ok, e ela é server-side! Isso significa que,no contexto de uma arquitetura cliente-servidor, todo processamento do código PHP ocorre no servidor e, não, no cliente.
Ahhh professor! Então toda linguagem de programação de scripts são server-side?
Claro que não!
JavaScript, por exemplo, roda do lado do cliente, isto é, é uma linguagem client-side! Simples, né?!Ela também é dinamicamente e fracamente tipada! O primeiro significa que os tipos das variáveis podem ser modificados em tempo de execução.
Portanto, é possível que uma variável inteira se transforme em booleana durante a execução do programa. Já o segundo significa que não é obrigatório declarar o tipo da variável. Portanto, é possível usar uma variável sem declarar seu tipo, que será decidido, também,durante a execução do programa. O PHP suporta tanto programação estruturada quanto programação orientada a objetos.
Simples assim! Calma, galera... estamos acabando! PHP é portável, isto é, ela é independente de plataforma. Costuma-se dizer que é uma Linguagem WORA (Write Once,Run Anywhere). Ela é capaz de rodar sobre Windows, Linux, Unix, etc. PHP é uma linguagem robusta! Ora, não é muito difícil adivinhar isso. É uma linguagem bastante antiga, intensamente testada e continuamente melhorada.
É comum que códigos escritos há muitos anos continuem funcionando perfeitamente hoje em dia!E PHP é eficiente? Sim! Consome poucos recursos do servidor e é, em geral, veloz. Por fim, PHP é utilizada para desenvolvimento de conteúdo dinâmico na web, mas não só isso!Pode ser usado como uma linguagem de propósito geral, sendo útil em interfaces gráficas ou em linha de comando.
1 Está instalado em mais de 244 milhões de websites e 2.1 milhões de web servers.

Agora veremos seu funcionamento! Primeiramente, para que ele funcione, é preciso que esteja instalado em um Servidor Web. Professor, eu não sei o que é um servidor web! Grosso modo, é um software que recebe Requisições HTTP e devolve Respostas HTTP. Grosso modo, trata-se de clientes representados por navegadores web requisitando páginas web, documentos, dados, etc.
Os Servidores Web mais populares são Apache (Software Livre) e IIS (Software
Proprietário). Uma vez instalado, configura-se o PHP, reinicia-se o servidor e está pronto para usar! Galera, o PHP fica embutido dentro do código HTML! Portanto, dentro da tag <body> do HTML,encontra-se a tag

<?php> do PHP! Vamos ver um exemplo abaixo:

<html>

<head>

<title> PHP Teste </title>

</head>

/ 121

/

<body>

<? php echo "<p>Olá, mundo! </p>"; ?>

</body>

</html>

Suponhamos que esse código foi salvo com o nome de olamundo.php e inserido no diretório raiz do servidor web www.exemplo.com. Bem, quando o cliente digitar o endereço www.exemplo.com/olamundo.php em seu navegador web, o servidor web irá procurar em seus diretórios, processando a página olamundo.php. Processando como, professor?
Ele irá interpretar o código PHP, executando tudo que for requisitado, substituir tudo que estiver dentro das tags PHP por código HTML puro e enviará o resultado para o usuário. Esse resultado é o código escrito acima? Não, é o código processado, como é apresentado abaixo:
<html>

<head>

<title> PHP Teste </title>

</head>

<body>

<? php echo "<p>Olá, mundo! </p>"; ?>

</body>

</html>

Percebam que esse não é o código que foi escrito originalmente, isto é,
esse é o código processado em que as tags PHP foram substituídas por tags HTML! Se tentarmos visualizar o código fonte da página recebida, não seremos capazes de ver código PHP, veremos apenas código puro HTML.Simples, não?! Ademais, todo código PHP deve estar delimitado, como mostra o código abaixo:
<? php > //Código aqui.

?>

<script language = "php"> // Código aqui.

</script>

<? php

//Código aqui.

?>

<?

//Código aqui.

?>

Os comentários seguem o mesmo padrão da linguagem C em uma ou mais linhas, como mostra o código abaixo:
<? php >

//Comentário de uma linha!

/* Comentário de quatro linhas! */
?>

Falemos agora sobre variáveis! Bem, toda variável começa com o símbolo "$". A seguir, a nomenclatura segue a seguinte regra de formação (Case Sensitive):
Letra|Underscore + Letra|Número|Underscore

<? php >

$var //Correto = Pode começar com letra!

/ 121

/

$_var //Correto = Pode-se começar com underscore!

$-var //Errado = Não se pode usar traço!

$Var //Correto = Segue o padrão e difere de $var!

$v_ar //Correto = Pode haver underscore no meio!

$900 //Errado = Não se pode começar com número

Galera, agora vamos ver outra coisa básica! As variáveis podem ser do tipo
Texto, Numérico ou
Booleanas, como vemos no exemplo a seguir! Observem que as variáveis do
Tipo Texto podem ser declaradas com aspas simples ou duplas. Ademais, os valores das variáveis do Tipo Booleano não são Case Sensitive, logo TRUE = true e FALSE = false.
<? php >

//Variável do Tipo TEXTO

$varl= "Teste";

$var2 = 'Teste';

//Variável do Tipo NUMÉRICO

$var3 = 3.14;

$var4 = 1000;

//Variável do Tipo BOOLEANO

$var5 = true;

$var6 = FALSE;

?>

/ 121

/

Agora uma coisa muito maneira em PHP: variáveis podem ter seu nome designado em tempo de execução. Como assim, professor?Isso não é impossível? Não! Vejam:
<? php

$varl ='Hello";

SHello = 'World1;

echo"$varl $$varl"; //Resultado: Hei lo World

?>

Cara, isso é muito legal! Observem o que acontece: a variável do tipo texto svari contém a string"Hello". Já a variável do tipo texto sHello contém a string
"World". Em seguida, pede-se para imprimir $van, isto é, "Hello". Depois, pede-se para imprimir ssvan,mas $van = "Hello", logo pede-se para imprimir sHello, isto é, "World". Resultando em "Hello World".
Sobre exceptions, lembre-se: exceções podem ser conceituadas como ocorrências de programação tidas como inválidas durante o processamento e que paralisam o programa até que sejam resolvidas.
Em PHP, exceções são objetos especiais e derivam da classe Exception,
possuindo métodos específicos de retorno. Selecione, a seguir, a alternativa que lista apenas métodos presentes na referida classe Exception do PHP:getMessage(), getCode(), getTraceAsString().
OPERADORES ARITMÉTICOS

ANOTAÇÃO | SIGNIFICADO | DESCRIÇÃO
|

+SA IDENTIDADE Conversão de $a para int ou float

-$A NEGAÇÃO Oposto de $a.

SA + SB ADIÇÃO Soma de $a e $b.

$A-$B SUBTRAÇÃO Diferença entre $a e $b.

$A*$B MULTIPLICAÇÃO Produto de $a e $b.

SA/SB DIVISÃO Quociente de $a e $b.

$A%$B MÓDULO Resto de $a dividido por $b.

$A**$B EXPONENCIAL Resultado de $a elevado a $b.

OPERADORES COMPARATIVOS

ANOTAÇÃO | SIGNIFICADO DESCRIÇÃO

/ 121

/

Verdadeiro (true) se $a é igual a $b.

Verdadeiro (true) se $a é igual a $b, e eles são do mesmo tipo.
Verdadeiro se $a não é igual a $b.

Verdadeiro se $a não é igual a $b.

Verdadeiro de $a não é igual a $b, ou eles não são do mesmo tipo
(introduzido no PHP4).

Verdadeiro se $a é estritamente menor que $b.
Verdadeiro se $a é estritamente maior que $b.
Verdadeiro se $a é menor ou igual a $b.

Verdadeiro se $a é maior ou igual a $b.

Um integer menor que, igual a ou maior que zero quando $aé,

respectivamente, menor que, igual a ou maior que $b.

OPERADORES INCREMENTAIS/DECREMENTAIS

ANOTAÇÃO | SIGNIFICADO | DESCRIÇÃO

++$A PRÉ-INCREMENTO Incrementa $a em um, e então retorna $a.

$A++ PÓS-INCREMENTO Retorna $a, e então incrementa $a em um.

-$A PRÉ-DECREMENTO Decrementa $a em um, e então retorna $a.

$A- PÓS-DECREMENTO Retorna $a, e então decrementa $a em um.

OPERADORES LÓGICOS

ANOTAÇÃO | SIGNIFICADO | DESCRIÇÃO
|

$A AND $B E Verdadeiro (true) se tanto $a quanto $b são verdadeiros.
$AOR$B OU Verdadeiro se $a ou $b são verdadeiros.

$A XOR $B XOR Verdadeiro se $a ou $b são verdadeiros, mas não ambos.

!$A NÃO Verdadeiro se $a não é verdadeiro.

$A88$B E Verdadeiro se tanto $a quanto $b são verdadeiros.

$A 11 $B OU Verdadeiro se $a ou $b são verdadeiros.

Bem, pessoal. É impossível esgotartodo assunto de PHP em uma aula online,
ademais o intuito aqui não é ensinar ninguém a programar. Portanto, não vou explicar para cada linguagem como x
/ 121

/

funciona conceitos básicos (Ex: laço condicional, laço de repetição),
porque eles funcionam quase sempre da mesma forma. Vou me ater apenas às diferenças!
Expressões Condicionais são de três tipos: if-elseif-else, operador ternário "?"
e switch. Observação:
a condição deve vir sempre entre parêntesis no if-elseif-else.

<?php if ($a >$b) {
echo "a é maior que b";

} elseif ($a == $b) {
echo "a é igual a b";

} else {

echo "a é menor que b";

}

?>

E no caso do Operador Ternário teríamos:

<?php

$varl = TRUE;

$var2 = FALSE;

$var3 = TRUE;

$var 1? $var2 : $var3;

?>

Com switch:

<?php

$varl = TRUE;

$var2 = FALSE;

$var3 = TRUE;

/ 121

/

$var 1? $var2 : $var3;

?>

Ou

<?php if($i == 0){
echo "i é igual a 0";

} elseif ($i == 1) {
echo "i é igual a 1";

} elseif ($i == 2) {
echo "i é igual a 2";

}

switch ($i) {
case 0:

echo "i é igual a 0";
break;

case 1:

echo "i é igual a 1";
break;

case 2:

echo "i é igual a 2";
break;

}

?>

Já as Expressões Iterativas são de quatro tipos: while, do-while, for e foreach. A única observação é que o foreach é um laço usado para arranjos.
<?php

/* exemplo 1 */

for ($i = 1; $i <= 10; $i++) {
echo $i;

}

/* exemplo 2 */

for ($i = 1;; $i++) {
if ($i > 10) {

break;

}

echo $i;

}

/* exemplo 3 */

$i = l;
for (;;) {

if ($i > 10) {
break;

}

echo $i;

$i++;

}

/* exemplo 4 */

for ($i = 1, $j = 0; $i <= 10; $j += $i, print $i, $i++);

Com while:

$i = i;

while ($i <= 10):
echo $i;

$i++;
endwhile;

Com Do-while:

<?php

$i = 0;
do {

echo $i;

} while ($i > 0);

/ 121

/

?>

Com Foreach:

<?php

$arr = array(l, 2, 3, 4);
foreach ($arr as &$valor) {

$valor = $valor * 2;

}

// $arr is now array(2, 4, 6, 8)

unset($valor); // quebra a referência com o último elemento

?>

Porfim, cabe salientar que PHP permite saltos de linha por meio do comando goto. Logo, pode-se saltar para qualquer linha de código por meio desse comando.
Com GOTO:

<?php goto a;echo 'Foo';

a:

echo 'Bar';

?>

E os arrays? Eles sempre vêm junto do símbolo "$" e pode ser de dois tipos: numérico, em que os índices/chaves são números inteiros e associativo, em que os índices/chaves são do tipo texto.Apresentam enorme versatilidade de declaração e construção! Em que sentido, professor? Oexemplo abaixo mostra três maneiras distintas de se declarar um mesmo vetor.

<?php

//Array com três numéricos

$array = array (10,20,30);

//Idêntico ao anterior

$array [0] = 10;

$array [1] = 20;

$array [2] = 30;

//Idêntico ao anterior

$array = array (0=>10, l=>20, 2=>30);

?>

No último exemplo, o operador "=>" associa um índice a um valor. Agora observem esse exemplo!Um mesmo vetor pode ter índices numéricos e textuais. Além disso, seus valores podem ser de qualquer tipo (Ex: String, Integer, Boolean, etc). É possível que classes em namespaces diferentes tenham o mesmo nome.
<?php

//Array com dois valores textuais e um numérico

$array = array("Flamengo", 3.14, "Matemática");

//Array com índices e valores textuais

$array["Dilma"] = "Presidente da República";

$array["Mantega"] = "Ministro da Fazenda";

$array["Arno"] = "Secretário do Tesouro";

//Array com índice textual e inteiro e valores inteiro e booleano, respectivamente
Jarray = array("Primeiro" => 1, 2 => TRUE);

Por fim, temos os arrays multidimensionais, que podem ter índices/chaves numéricos ou textuais e valores de qualquer tipo. Ademais, também se pode utilizar o operador
<?php

//Array de duas dimensões com índices e valores textuais e numéricos

$ar*ray[0] ["Coluna0" ] = "Um'r;

$array[0]["Colunai"] = "2";

Jarray[1]["Coluna0"] = "Três";

$array[l]["Colunai"] = 4;

//Idêntico ao anterior

Jarray = array(0 = > array("Um","2"), l=>array("Três",4));

Agora algumas curiosidades: arrays podem ser comparados assim como variáveis,
por meio dos operadores (==, !=, ===, !==). Um array será igual a outro se ambos tiverem os mesmos valores para os mesmos índices. Um array será triplamente igual a outro, se ambos tiverem os mesmos valores para os mesmos índices em uma mesma ordem.
Arrays multidimensionais podem ser incompletos, isto é, um Array 2x2
pode ter apenas três elementos (teoricamente, ele teria quatro). Além disso, caso o programador adicione um valor em um array sem mencionar em qual índice/chave, ele será adicionado após o último índice. Mudando novamente de assunto! Vamos falar agora sobre Funções.
Galera, esse assunto é uma pedra no sapato. Por que, professor? Cara,
existem mais de 5000
funções! E nada impede que a banca escolha qualquer uma delas e cobre sua funcionalidade.Portanto, veremos as mais comuns e vocês vão rezar para que somente elas caiam em prova! Antes de tudo, o próprio programador por criar facilmente uma função de maneira bastante simples:
<?php

//Código

Function MinnhaFuncao ($varl, $var2, $var3) {

//Funcionalidades

//Return é opcional

}

?>

Bem, uma função pode funcionar como um procedimento caso não retorne nenhum valor. Além disso, ela pode passar parâmetros por valor (sem "&") ou por referência (com
Bacana, mas vamos começar a falar um pouco sobre web? Tem um bocado de função importante nesse contexto também! Por exemplo, uma das principais características do PHPé que ele sabe

/ 121

/

lidar muito bem com formulários. É legal, porque qualquer elemento desses formulários fica disponível automaticamente para serem usados nos Scripts PHP.
Imaginem um formulário HTML (sem tags PHP) que utilize o método POST e envie dados (Nome eIdade) para uma página action.php, como mostra o exemplo abaixo:

<form action= "action.php" method="POST">

Seu nome: <input type="text" name="nome" />
Sua idade: <input type="text" name="idade"/>

<input type="submit">

</form>

Quando o usuário enviar os dados, automaticamente criar-se-á duas variáveis: $_POST["nome"J e
$_POST["idade"]. Essas variáveis conterão os dados recebidos no método
POST. O mesmo ocorre caso se utilize o método GET, porém com as variáveis: $_GET["nome"Je $_GET["idade"].
Agora imaginem uma página PHP que recebe esses dados e os armazena nessas variáveis,executando alguma ação:

Oi <?php echo $_POST["nome"]; ?> //Oi Diego
Você tem <?php echo $_PO5T["idade"]; ?> anos. //Você tem 25 anos

Agora vejam que interessante: essas variáveis são arrays associativos, isto é,
com índice/chave textual. E que texto é esse? O nome das variáveis! Portanto, $_POST e$_GET são vetores com dois índices que armazenam valores inseridos e enviados pelo usuário em um formulário HTTP. Ecookies, professor? PHP suporta cookies? Claro que sim!

Eles são criados por meio da função setcookie(nome, valor, validade, caminho,
domínio). Ela define um cookie para ser enviado juntamente com o resto dos cabeçalhos HTTP. Os cookies devem ser enviados antes de qualquer saída de script, aliás antes de todo e qualquer texto! Todos os argumentos, exceto o nome, são opcionais.
Bem, eu falei sobre Formulários e Cookies. Por que isso? Porque há uma variável global
$_REQUEST que consiste em uma array associativo que, por padrão,
contém informações de

$_GET, $_POST e $_COOKIE. Trata-se de uma variável automática, isto é, ela está disponível em todos os escopos e armazena os valores do Get, Post e Cookie. Beleza?
Quando enviamos um arquivo através de um formulário para o PHP, ele cria a super global $_FILES,no mesmo estilo das super globais $_GET e $_POST. Cada campo do tipo file é colocado em um array dentro de $_FILES.
E os frameworks, professor? Galera, os mais comuns são: Codelgniter,
Zend e Symfony. O
Codelgniter é um framework de desenvolvimento de aplicações PHP gratuito, leve,
rápido, que utiliza MVC, gera URLs limpas e requer uma engine específica para templates.Trata-se de um conjunto de ferramentas para desenvolver aplicações muito mais rápido do que poderíamos fazer sem utilizar o framework.
Já o Zend Framework é orientado a objetos, de código aberto, implementado em PHP 5 e foi desenvolvido para simplificar o desenvolvimento web enquanto promove as melhores práticas na comunidade de desenvolvedores PHP. E o Symphony também é um framework web livre, escrito em PHP e que segue o Padrão Movel-View-Controller.
Ele é projetado para permitir que os desenvolvedores apliquem princípios ágeis do desenvolvimento (tais como DRY, KISS ou XP) e foquem nas regras de negócio sem necessitar escrever muitos arquivos de configuração XML, comuns nos frameworks atuais. Além disso,permite construir aplicações robustas em contexto empresarial, e dar aos desenvolvedores controle total sobre a configuração.
Por fim, vamos falar rapidamente sobre um assunto que nunca caiu em prova, mas que -
se um dia cair - vocês já saberão do que se trata: Framework Laravel. O que é isso,professor? Cara, é um
Framework PHP, livre, open-source, que utiliza o Padrão MVC para criar aplicações seguras e performáticas de forma rápido, com código limpo e simples. Capiche?
Ele utiliza uma engine de template chamada Blade para criação da interface gráfica e possui uma pancada de ferramentas que auxiliam a criar aquelas interfaces bonitonas(e também funcionais)
que nós vemos por aí na web, porém de forma bastante rápida. Outra característica bacana é que o código é bonito, organizado e limpo. Sério, o código-fonte é uma obra de arte!
Ele possui uma sintaxe bastante expressiva, bonita, elegante, simples e fácil de ler. Bem, pessoal!Como eu disse, essa parada nunca caiu em prova até hoje, mas já veio em alguns editais. Logo, em breve, pode estar caindo com alguma frequência nas provas de desenvolvimento de sistemas.Guardem essas características básicas do framework e parte para o abraço na hora da prova.

/ 121

/

QUESTõES CoMENTADAS - DIVERSAS BANCAS

í. (FCC -TST - 2012) Considere a linguagem de programação PHP e seus operadores. A execução da sentença:
a) (A != B) retorna falso (false), considerando as variáveis A e B inicializadas com os valores 3 e 6,respectivamente.

b) (A %- B) atribui o valor 3 (três) para a variável A, considerando as variáveis
A e B inicializadas com os valores 10 e 3, respectivamente.
c) (A . = B) concatena o conteúdo das variáveis A e B e armazena o conteúdo em A.

d) !(A -- B) retorna falso (false), considerando as variáveis A e B
inicializadas com os valores 3 e
6, respectivamente.

e) (A = = = B) compara somente os tipos das variáveis A e B.

Comentários:

(a) Não, essa operação verifica se o valor de A é diferente do valor de B. O valor
3 é diferente de 6,
portanto retorna True e, não, False; (b) Não, essa operação verifica qual o resto da divisão de A por
B. 10/3 tem quociente 3 e resto 1, portanto retorna 1 e, não, uma atribuição; (c) SimIDe fato, essa operação concatena o conteúdo de A e B e armazena o resultado em A. (d)Não, essa operação verifica se o valor de A é diferente do valor de B e nega o resultado. O valor 3 é diferente de 6resultando em falso, que, negado, será verdadeiro, (e) Não, essa operação compara o tipo e o valor das variáveis A e B. Portanto, ela retornaria True, caso fossem do mesmo tipo e com o mesmo valor.
Gabarito: Letra C

2. (FCC / TST - 2012) Considere o programa abaixo escrito na linguagem PHP:

$v = array(10, 50, 2, 15, 35);

for($i=0;$i<count($v)-1;$i++){
if($v[$i] > $v[$i+l]){

$temp = $v[$i+1];

$v[$i+l] = $v[$i] ;

$v[$i] = $temp;

$í=-i;

}

}

for($i=0;$i<=count($v);$i ++){
echo " ".$v[$i];

}

O resultado a ser informado ao usuário após a execução do programa acima é:
a) íoo 70 30 20 4

b) 50 35 1510 2

c) 4 20 30 70 100

d) 2 1015 35 50

e) 10 50 2 15 35

Comentários:

Esse é um simples algoritmo de ordenação. Observem que há a declaração de uma array $v com cinco valores desordenados. Dentro de um loop de repetição que vai de 0 (índice do primeiro elemento do vetor) até 4 (índice do último elemento do vetor), é verificado se o elemento anterior é maior que o posterior e, caso seja, armazena-se o valor da variável posterior em uma variável temporária $temp, copia-se o valor da variável anterior na variável posterior,depois copia-se o valor da variável temporária na variável anterior e rearranja o array. Éum simples Bubble Sort, cujo resultado é 2 1015 35 50. Por fim, há um loop que escreve o resultado na tela.
Gabarito: Letra D

3. (FCC / MPE-AP - 2012) Analise os exemplos de criação de array em PHP.
I.

íidade = array("Paulo"=>32, "Pedro"=>3o, "Ana"=>34);

II.

sfamilia = array("Jorge"=>array("Angela","Iracema",
"Bia"),"Pedro"=>array("Ana"));

III.

$nome[o] ="Paulo";

$nome[i] ="Pedro";

$nome[2] ="Ana";

IV.

$idade['Paulo'j = "32";

$idade['Pedro'] = "30";

$idade['Ana'] = "34";

Representam exemplos corretos de criação de array os itens a) I, II, III e IV.
b) III e IV, apenas.

/ 121

/

c) I e II, apenas.

d) I, III e IV, apenas.

e) II, III e IV, apenas.

Comentários:

Primeiro, lembremos que - em PHP - o índice do array pode ser tanto um valor numérico quando um texto. Portanto, pode haver um array $vetor[o] = "João" ou $vetor["João"] = o.
Vetor I: Correto, trata-se de um array associativo em que $idade["Paulo"] = 32,
$idade["Pedro"] =
30 e $idade["Ana"] = 34. Percebam que os índices/chaves desse vetor são "Paulo",
"Pedro" e "Ana"
que estão associados por meio do operador => aos valores numéricos 32, 30 e 34.

Vetor II: Correto, trata-se de um array multidimensional em que o primeiro elemento
"Jorge" é um vetor com os valores "Angela", "Iracema" e "Bia" e o segundo elemento "Pedro" também é um vetor com o valor "Ana".
Vetor III: Correto, trata-se de um array numérico em que o primeiro elemento é
"Paulo", o segundo é "Pedro" e o terceiro é "Ana".
Vetor IV: Correto, trata-se de um vetor associativo em que o primeiro elemento é
"32", o segundo é "30" e o terceiro é "34".
Gabarito: Letra A

4. (FCC / MPE-AP - 2012) Marcos está desenvolvendo uma aplicação web PHP
utilizando o
WAMPServer. Como está utilizando um banco de dados MySQL, escolheu uma função para enviar uma consulta ou comando SQL (por exemplo, os comandos select, insert ou delete)para o banco de dados ativo. A função correta escolhida foi:
a) mysql_fetch_array.

b) mysqLquery.

c) mysql_update.

d) mysql_execute_stmt.

e) mysql_stmt_start.

Comentários:

Pessoal, é impossível sabertodas as funções do PHP, ainda mais com as extensões (cerca de 5000)!Então essa era uma questão em que se necessitava de um conhecimento mais aprofundado,
mas nada extremamente complicado. Bastava ver que a única opção mais condizente com um banco de dados era aquela que tinha o nome "query". Essa função envia uma consulta/comando MySQL.
Gabarito: Letra B

5. (FCC / TRE-SP - 2012) Na linguagem PHP é possível utilizar o protocolo SOAP por meio de classes desenvolvidas especificamente para esse protocolo. A classe que fornece acesso cliente aos servidores SOAP é chamada de:
a) PHPAccess.

b) WSDLClient.

c) SoapConnect.

d) SoapClient.

e) SoapAccess.

Comentários:

Mais uma questão que exige saber funções específicas. Caso vocês não saibam, eu recomendo que tentem ir sempre no mais lógico. A questão pede a classe que fornece acesso cliente aos servidoresSOAP, portanto - na minha opinião - o item mais condizente é o SoapClient. Essa função fornece acesso cliente a servidores SOAP 1.1 e 1.2, podendo ser usada em Modo WSDL e Não-WSDL.
Gabarito: Letra D

6. (FCC / TRE-SP - 2012) A linguagem PHP permite a instalação de extensões que podem aumentar sua gama de funcionalidades. Uma das funcionalidades extras que podem ser adicionadas se refere a manipulação de arquivos XML. A extensão que possui várias classes que podem ser instanciadas para a leitura e gravação de arquivos XML é chamada:
a) DOM.

b) XML-RPC.

c) Ctype.

d) SCA.

e) YAZ.

Comentários:

Mais uma questão que exige saber funções específicas, porém essa era mais complicada.
O bom senso diria para ir na Letra B, no entanto a extensão que possui diversas classes para leitura e gravação de arquivos XML. Ela permite manipular documentos XML por meio da API DOM.
Gabarito: Letra A

7. (FCC / TRE-AP - 2011) Em relação a PHP e JSP é correto afirmar:

a) Em JSP o conceito de classes e objetos não leva em conta os princípios de proteção de dados tanto nas propriedades quanto nos métodos.
b) A flexibilidade do PHP permite-lhe que a avaliação de uma variável seja o nome de outra variável ou mesmo de uma função.
c) Em PHP os objetos possuem métodos e propriedades privados e devem ser instanciados para serem usados.
d) Em JSP pode-se chamar o construtor do objeto pai em qualquer parte do código e não há tratamento de exceções nos métodos nativos.
e) Em JSP os objetos são destruídos ao final da execução do script.

Comentários:

Vamos nos ater aos itens sobre PHP! (b) Sim, PHP é bastante flexível nesse sentido,
isto é, uma variável pode receber o nome de outra variável ou o nome de uma função - são as chamadas variáveis variáveis; (c) Sim! No entanto, o gabarito diz que é errado! Eu não encontrei nenhum erro nessa questão. Observem que não foi dito que os objetos sempre possuem métodos e propriedades privados. De fato, o mais comum é ter métodos públicos e propriedades privadas - mas isso não é obrigatório.
Gabarito: Letra B

8. (FCC / TRT14 - 2011) Na PHP 5, é uma função usada para a busca por um padrão em um nome de arquivo:
a) fscanf.

b) fpassthru.

c) fseek.

d) fputs.

e) fnmatch.

Comentários:

Mais uma questão que exige saber funções específicas. O bom senso diria para ir na
Letra E, na medida em que ela traz a palavra "match". Apenas por curiosidade: fscanf() lê dados de um arquivo;fpassthru() lê dados de um arquivo até o fim do arquivo e escreve o resultado no buffer de saída;fseek() posiciona o ponteiro em um arquivo; fputs() escreve em um arquivo; e fnmatch()
compara o nome em um arquivo com um padrão.
Gabarito: Letra E

/ 121

/

9. (CESPE / MPE-RN -2010) Na linguagem PHP, a função fputs:

a) busca por um padrão em um nome de arquivo.

b) é um nome alternativo para a função fwrite.

c) interpreta o conteúdo de um arquivo de acordo com um determinado formato.

d) cria um link físico.

e) posiciona o ponteiro em um arquivo.

Comentários:

Mais uma questão que exige saber funções específicas: (a) Errado. Quem faz isso é a função fnmatch(); (b) Correto. É um nome alternativo para a função fwrite(); (c) Errado. Quem faz isso é a função fscanf(); (d) Errado. Quem faz isso é a função link(); (e) Errado. Quem faz isso é a função fseek().
Gabarito: Letra B

Io.(FCC/TCE-SP-2oIo) NÃO se trata de uma característica do PHP:

a) portábil.

b) baseado no servidor.

c) gratuito e com código aberto.

d) embutido no HTML.

e) baseado no cliente.

Comentários:

Bem, em primeiro lugar, uma observação: "Portábil", FCC? Pelo amor de Deus! Segundo,
vamos à avalição dos itens: (a) Sim, ele é independente de plataformas. Similar ao Java, éWORA (Write
Once, Run Anywhere); (b) Sim, é uma linguagem Server-side, isto é, o cliente envia a requisição,que é processada no servidor e retorna a resposta; (c) Sim, é uma linguagem Free e
Open-source;

(d) Sim, o PHP vai inserido em tags HTML; (e) Não, é uma linguagem Server-side e, não, Client-side.

Gabarito: Letra E

11. (CESPE /TRE-BA- 2015) Para o recebimento dos dados de um formulário HTML,
enviados por meio do método GET, para uma página PHP, deve-se utilizar:
a) $_GET["nome_text"]

b) $GET["nome_text"]

c) _GET$["nome_text"]

d) _$GET["nome_text"]

/ 121

/

e) _$_GET["nome_text"]

Comentários:

Para recebimento de dados em formulário HTML, utilizando GET,
deve-se utilizar

$_GET["nome_text"].

Por exemplo: caso o usuário entre em: http://example.com/?name=Sou+TRE, o resultado da execução de echo $_GET["name"], será "Sou TRE".
Gabarito: Letra A

i2.(CESPE / CPRM -2013) A validação de uma data em PHP pode ser realizada pela função:

a) getdate.

b) checkdate.

c) setdate.

d) isdate.

e) mktime.

Comentários:

getdate() recupera uma data; checkdate() verifica/valida uma data; setdate() modifica o valor de uma data; isdate() não faz parte das funções do PHP; mktime() obtém um timestamp Unix para uma data. A função checkdate valida uma data do calendário Gregoriano. Sua assinatura é a seguinte: checkdate(month,day,year);
Gabarito: Letra B

i3.(CESPE / TRE-MS - 2015) Em uma função, escrita na linguagem de programação PHP, a passagem de parâmetros por referência é feita por meio da utilização do caractere:
a) !

b) °/o c) &
d) @

e) ?

Comentários:

Lembram-se de que a sintaxe da Linguagem PHP é fortemente influenciada pela sintaxe de
C/C++
e Perl. Em C, a passagem de parâmetros por referência é feita por meio da utilização do caractere

Nas funções PHP, a passagem por valor é o padrão. Caso você necessite passar um parâmetro por referência, utilize o caractere &. Veja no exemplo abaixo:
<?php function foo(&$var)
$var++;

$a=5;
foo($a);

// $a vale 6 aqui.

Gabarito: Letra C

í^.fCESPE/TRE-MT-2015) Um servidor Web que interpreta páginas em PHP é denominado:

a) IIS.

b) JSTL.

c) NetBeans.

d) Apache.

e) Netscape.

Comentários:

Bem, essa é uma questão extremamente mal formulada. Primeiro, JSTL é uma biblioteca de tagsJSP, NetBeans é uma IDE de desenvolvimento de software e Netscape é um navegador web.Sobram, portanto, IIS e Apache. No entanto, ambos são Servidores Web capazes de interpretar páginas em PHP! No entanto, o gabarito oficial é Letra D.
Gabarito: Letra D

15. (CESGRANRIO / PETROBRÁS - 2015) O envio de e-mails, por meio de programas PHP, é responsabilidade da função:
a) email.

b) mail.

c) &mail.

d) ismail.

e) &email.

Comentários:

/ 121

/

Questão decoreba que não avalia conhecimento! A função responsável pelo envio de e-mails é a função mail(). Repare que o examinadortenta confundir colocando simbolos, em PHP os nomes de variáveis é que são precedidas por símbolos ($), os nomes funções não (os parâmetros podem ser precedidos por & para indicar passagem por referência). Agora colocar e-mail como alternativa foi maldade rs. Veja um exemplo abaixo retirado da documentação.
mail('caffeinated@example.com', 'My Subject', $message);

Gabarito: Letra B

I6.(CESPE/TJ-RO-2O15) Em PHP,

a) os operadores aritméticos restringem-se a soma, subtração, multiplicação e divisão.

b) as variáveis necessitam da sua definição de tipo no início do programa.

c) operações aritméticas entre variáveis numéricas e variáveis alfanuméricas, por exemplo 6divido por 3, resultam em mensagem de erro.

d) o único conjunto de comandos condicionais utilizado é o if...endif.

e) as variáveis são definidas com o símbolo antes do nome da variável.

Comentários:

(a) Não, basta lembrar dos operadores Negação e Módulo; (b) Não, PHP é linguagem de tipagem dinâmica e fraca, isto é, permite declaração de variáveis em tempo de execução e permitem que as variáveis mudem de tipo; (c) Não, PHP realiza uma conversão implícita de tipos,portanto essa operação resultará no número 2 (64-3); (d) Não, lf... elseif... else e Switch; (e)Sim, para definir uma variável, utiliza-se o símbolo "$" antes de seu nome. Por exemplo: $variavel = 10.
Gabarito: Letra E

17. (FCC / MPE-MA- 2015) Em PHP, uma variável NÃO pode receber o nome inválido:

a) $cod_empregado b) sbaseisalario c) ídata-nascimento d) $depto_i_nome e) sdescricao
Comentários:

Em PHP, uma variável possui um nome válido caso se inicie com uma letra ou underscore, seguido de qualquer número de letras, algarismos ou underscores. Portanto, todas estão corretas,exceto

$data-nascimento, na medida em que possui um traço (que é diferente de underscore).

/ 121

/

Gabarito: Letra C

i8.(FCC / TJ-PE - 2015) NÃO é uma afirmativa correta sobre a função PHP:

a) session_start() = Inicializa os dados da sessão.

b) session_destroy() = Cancela o registro de uma variável global da sessão.

c) session_unset() = Libera todas as variáveis da sessão.

d) session_commit() = O mesmo que session_write_ close().

e) session_write_close() = Escreve os dados da sessão e a encerra.

Comentários:

A função session_destroy() destrói todos os dados registrados em uma sessão!

Gabarito: Letra B

íg.íFCC / TRT19 - 2015) Utilizando a data 01/07/2009 e o comando PHP:

echo $data = date("d/m/y");

a data será exibida no formato a) 01/07/09.
b) 01/07/2009.

c) oi/Jul/09.

d) oi/Jul/2009.

e) Wed, oi/Jul/2009

Comentários:

Sinceramente, galera! É um absurdo cobrarem uma questão como essa... isso não avalia conhecimento de ninguém! Enfim, "d" é o dia de 01 a 31; "m" é o mês de 01 a 12;e "y" é o ano em dois dígitos.
Gabarito: Letra A

2o.(FEPESE / JUCESC - 2013) A função fopen ( ), utilizada em um script PHP, que recebe o argumento de modo igual a "a+", abre um arquivo existente para:
a) leitura e gravação e coloca o ponteiro no final do arquivo, depois de todos os dados.

b) leitura e gravação, deleta todo o conteúdo e coloca o ponteiro no início do arquivo.

c) leitura e gravação e coloca o ponteiro no início do arquivo, antes de qualquer dado.

d) somente gravação e coloca o ponteiro no final do arquivo, depois de todos os dados.

e) somente gravação, deleta todo o conteúdo e coloca o ponteiro no início do arquivo.

Comentários:

O argumento "a+" abre o arquivo para leitura e escrita; coloca o ponteiro no final do arquivo e, se o arquivo não existir, tenta criá-lo.
Gabarito: Letra A

2i.(MPE-RS / MPE-RS - 2015) Um conteúdo será considerado como um código PHP
pelo interpretador se estiver dentro do par de tags:
a) <php> </php>

b) <?php ?>

c) <?php php?>

d) <?> </?>

e) <script language - PHP> ?>

Comentários:

Essa é fácil: começa com "<?php" e termina com "?>".

Gabarito: Letra B

22.(FCC/ TRT 23 - 2015) A expressão PHP $x && $y representa um exemplo de utilização de operador:
a) de atribuição.

b) aritmético.

c) lógico.

d) de comparação.

e) de incremento e decremento.

Comentários:

Operador "&&" é um operador lógico. O resultado é verdadeiro se ambas as variáveis forem verdadeiras, caso contrário será falso.
Gabarito: Letra C

23. (IBFC - Prefeitura de divinópolis - 2018) Dado o loop PHP:
for ($x = o; $x <= "5"; $x++)

A variável $x assumirá os valores:

a) í, 3 e 5.

b) o, í, 2, 3 e 4.

c) i, 2, 3,405.

d) o, 2 e 4.

e) o, 1, 2, 3, 4 e 5.

Comentários:

Questão bastante simples: é um laço de repetição em que os valores variam de 0 a 5.
Portanto, a variável $x assume os valores o, 1, 2, 3, 4 e 5.
Gabarito: Letra E

24.(FGV / BANESTES - 2021) HTML, DHTML, JavaScript e PHP são linguagens utilizadas no desenvolvimento de sites da World Wide Web. A seu respeito é correto afirmar que:
a) o código de uma aplicação JavaScript deve ser interpretado pelo servidor HTTP ao passo que o código de uma aplicação PHP deve ser interpretado pelo cliente HTTP.
b) o código de uma aplicação JavaScript deve ser interpretado pelo cliente HTTP ao passo que o código de uma aplicação PHP deve ser interpretado pelo servidor HTTP.
c) tanto o código de uma aplicação JavaScript como o código de uma aplicação PHP
devem ser executados pelo cliente HTTP.
d) tanto o código de uma aplicação JavaScript como o código de uma aplicação PHP
devem ser executados pelo servidor HTTP.
e) o código de uma página HTML deve ser interpretado pelo cliente HTTP ao passo que o código de uma página DHTML deve ser interpretado pelo servidor HTTP.
Comentários:

Como já foi dito, JavaScript é client-side e PHP é server-side.

Gabarito: Letra B

25. (IF-RJ / BIO-RIO - 2015) Considere o seguinte script encontrado em uma página PHP.

<?php

Sidade - array("Paulo"=>"4o", "Pedro"=>"62", "Ana"=>"43", "Marcos"=>"i8");

arsort($idade);

foreach($idade as $x => $x_valor) {
echo $x." = ". $x_valor."

}

?>

Ao executar o script será exibido na página:

a) Ana = 43 Marcos = 18 Paulo = 40 Pedro = 62

b) Marcos = 18 Paulo = 40 Ana = 43 Pedro = 62

c) o = 62 1 = 43 2 = 40 3 = 18

d) Pedro = 62 Paulo = 40 Marcos = 18 Ana = 43

e) Pedro - 62 Ana = 43 Paulo = 40 Marcos = 18

Comentários:

Questão sobre arrays e o método arsort. Como esse é um array com índices associativos, vimos na aula que o asort que ordena o array em ordem crescente dos valores, mantendo o índice. Já o arsort,o r é de reverse, ordena os valores na ordem inversa, ou seja, decrescente.

Gabarito: Letra E

26.(IF-RJ / BIO-RIO - 2015) Considere o código PHP a seguir:

<?php

£ nomes =array ("Zen ai de"," M a rcelo"," B iu n 0");

I

Sclength=count($ nomes};

fo r( $x=0;S c length; $ x-*-+)

{

echo $ nomes [3>x]:
echo

}

?>

O comando que deve ser utilizado na lacuna I para colocar os nomes em ordem alfabética crescente é:
a) order($nomes) ascending;

b) rsort($nomes);

c) index($nomes) order by asc;

d) sort(ínomes);

e) krsort(snomes);

Comentários:

Esse é um array do tipo indexado, com índices numéricos. Portanto o método é o sort simples.

Gabarito: Letra D

27.OF-RJ / BIO-RIO - 2015) Considere um formulário criado na página de site desenvolvido comPHP para permitir que os usuários façam upload de arquivos:

«fornfi action="ijpload.php" mettiod="post' enctype="mutüpart/fonri-data">

<label fo r="file"> F ile name:<Jlabel >

<inputtype-üle"name="file" id="file7><br/>

<input type="submit" value="Fazer Upload"/*

No arquivo upload.php, as instruções utilizadas para se obter o nome e o tipo do arquivo, caso não ocorra erro são, respectivamente,
a) $_DUMP["file"] e $_DUMP ["type"]

b) $_FILES["file"]["name"] e $_FILES["file"]["type"]

c) $_POST["file"] e $_ POST["type"]

d) $_FILES["file"] e s.FILES ["type"]

e) $_REQUEST["file"]["name"] e $_REQUEST["file"]["type"]

Comentários:

A variável superglobal que guarda os arquivos é o $_FILES. Perceba que o nome do input do arquivo é file. Ele que será o índice passado para o $_FILES. Agora o nome do arquivo e seu tipo estão dentro do objeto file. Por isso é preciso acessar com dois índices.$_FILES["file"]["name"] e

$_FILES["file"]["type"].

Gabarito: Letra B

28.(TJ-PE / IBFC - 2017) Para acessar bases de dados MySQL, por meio do PHP, é necessário antes estabelecer uma conexão. Para isso, deve ser utilizado o comando:
a) mysqL&connect ou mysql_&pconnect b) mysql_&&connect ou mysql_&&pconnect c) mysql&_connect ou mysql&_pconnect d) mysql&&_connect ou mysql&&_pconnect e) mysql_connect ou mysql_pconnect
Comentários:

O comando de acesso a uma base de dados MySQL é mysql_connect ou mysql_pconnect. Adiferença entre os dois é que no segundo, a conexão é persistente. Essas funções estão depreciadas nas versões mais recentes, o uso agora é unificado na função mysqli_connect() e para que a conexão seja persistente utiliza-se o parâmetro p: como prefixo do host.
Gabarito: Letra E

2g.(FCC / TCE-SP - 2010) Uma função PHP em execução terminará imediatamente, retornando seu argumento como valor, se for chamada, na função, a instrução:
a) this b) null c) return d) this.value e) this.return
Comentários:

O comando return encerra a execução de uma função retornando o argumento como valor.

Gabarito: Letra C

30. (FCC / TRT 3 - 2009) Dados os operadores "e" lógico: "and", "&&" e e os operadores "ou"lógico: "or", "||" e "|", a ordem de precedência no momento do PHP avaliar as expressões será na sequência:
a) and, &&, &, or, || e |.

b) or, II, I, and, && e &.

c) and, or, &&, ||, & e |.

d) or, and, ||, &&, | e &.

e) &, &&, and, |, || e or.

Comentários:

Essa questão foi anulada, mas podemos aproveitá-la para avaliar como se dá a ordem de precedência em PHP!
PRECEDÊNCIA DOS OPERADORES
CLONENEW

[

**

++ - - [INT] (FLOAT) (STRINGJ [ARRAY] [OBJECT] [BOOL] @

*/ah

+ -.

<< »

<<=>>=

== 1==== !==<><=>

&

A

I

&&

II

??

= += -= *= **= /= = o/o= 8= | = A= «= »=
AND

XOR
OR

Ou seja, a única opção onde alguma ordem é respeitada é a letra D, que está na ordem CRESCENTE
de precedência. A questão acabou ficando mal feita, mas ao menos revisamos como se dá a ordem de avaliação de operadores em PHP!
Gabarito: Letra D

31. (FCC / TRF 3 - 2016) Cookie é um arquivo texto que pode ser armazenado no computador do usuário, normalmente com informações de sua navegação no site, para ser recuperado posteriormente pelo servidor. Em PHP, um cookie criado pela instrução setcookie("ck","abcde",
time() + 3600); poderá ser recuperado utilizando a instrução:

a) $_ISSET["ck"J

b) load_cookie ("ck")

c) get_cookie("ck")

d) $_GETCOOKIE["ck"]

e) $_COOKIE["ck"]

Comentários:

A variável superglobal $_COOKIE["ck"] recupera cookies armazenados no cliente.

Gabarito: Letra E

32. (FGV/ TJ-PI - 2015) Analise o código PHP mostrado a seguir.

<?php function f($arg)
I

íargoi = 343 + 20/2 + 911;

$argo2 = 38 - (5 * 11);

$argRetorno = $argoi - $argo2;

Sargoi = 343;

$argo2 = 38;
f($argoi);
echo $argoi;

?>

A saída produzida pela execução desse código é:

a) -17

b) 38

c) 343

d) 1264

e) 1281

Comentários:

A passagem padrão de argumentos no PHP é por valor, ou seja, o valor da variável passada não é alterado. Logo, o valor continua sendo 343.
Gabarito: Letra C

33. (FGV/TJ-PI-2015) Uma String recebida do campo nome de um formulário HTML enviado por meio do método POST para um site deve ser codificada para UTF-8. A forma correta de realizar essa operação, utilizando a linguagem PHP, é:
a) ínome = utf8_encode( $_POST['nome'])

b) $nome: utf8

c) decode($nome)

d) $nome = string( $_POST['nome'])

e) parseHTML($nome, utf8( $_POST['nome'])

Comentários:

Para resolver essa questão, precisamos saber qual é a forma de ler um campo do método POST. Já sabemos que a variável superglobal $_POST guarda os valores passados, para recuperar basta colocar o nome do campo, logo, recuperamos o campo nome dessa forma: $_POST['nome'].Isso jé eliminam as letras b e c. Infelizmente era necessário saber que a função é a utf8_encode.
Gabarito: Letra A

3Zf.(IESES / IFC-SC - 2015) Em um código PHP 5.6.2, qual das alternativas a seguir atribuiria o valor10 à variável $var?

a) $var = (100 > 10 :100 ? 10);

b) $var = (100 > 10 ? 10 :100);

c) $var = (100 > 10 :10 ? 100);

d) $var = (100 > 10 ? 100 :10);

Comentários:

O'?' é o operadorternário do PHP. Sua sintaxe é (expi ? exp2 : exp3). Caso a expi seja verdadeira o retorno é exp2, caso seja falsa, o retorno é exp3. Os itens A e C estão com sintaxe errada. Vamos analisar os restantes:
(b) 100 > 10 ? verdade; Logo retorna 10. Correto.

(c) 100 > 10 ? verdade; Logo retorna 100. Incorreto.

Gabarito: Letra B

35. (FGV/ TJ-PI - 2015) Analise o código PHP mostrado a seguir.

<?php

$lista = range(0,20);

for (Si = 0; $i <=20; $i++)

{

$p€'S- randfO^O};

$aiiK = $lista[$ij;

$lfcta[$I] = $lista($po5];

$ lista[Ípos] = $auX;

}

Ao final da execução desse código, os valores na variável ílista estarão:

a) ordenados de forma crescente, segundo o método de ordenação Quicksort;

b) ordenados de forma crescente, segundo o método de ordenação em bolha;

c) embaralhados, não sendo possível prever a ordem dos valores;

d) removidos da variável, devido a um erro no código;

e) duplicados, devido a um erro no código.

Comentários:

Primeiramente, a variável slista recebe um array cujos valores são os números de o à
20 (retorno da função range). Em seguida, executamos uma for com a variável $i também recebendo valores de o a 20.
Ao entrar no for, a variável $pos sempre receberá um valor aleatório entre o e 20
(função rand). A

$aux receberá o valor da $Iista[0], ou seja, o. E $Iista[o] = $1 ista[$pos], quer dizer que receberá um valor aleatório entre o e 20. E ao final $lista[$pos] - $aux, saux == 0 nesse momento, ou seja, a posição aleatória receberá o valor na ordem do loop.
Ufa, para mim isso virou uma bagunça total entre o e 20 rs, não podemos saber quais valores estão em cada posição.
Gabarito: Letra C

36.(CESPE /TRE-BA - 2017) A respeito da declaração de variáveis na linguagem de programaçãoPHP, assinale a opção correta.

x

/ 121

/

a) Uma variável é composta pelo nome dessa variável seguido do sinal $ no final.

b) Um nome de variável pode começar com um número.

c) Os tipos de variáveis existentes são somente local e global.

d) Diferentemente das linguagens em que o programador deve declarar o nome e o tipo da variável antes de usá-la, o PHP converte automaticamente a variável para o tipo de dado correto.
e) Os nomes das variáveis no PHP não diferenciam maiusculas de minúsculas, ou seja,
eles são case insentivive.
Comentários:

(a) Errado, uma variável é composta pelo sinal $ no início e o nome da variável; (b)
Errado, um nome de variável sempre começa com uma letra ou sublinhado, seguido por letras,números ou sublinhados - a expressão regular é [a-zA-Z_\x7f-\xff][a-zA-Zo-g_\x7f-\xff]*;(c) Errado, seria melhor dizer que existem os escopos: Global, Local ou Estático; (d) Correto, PHP é fracamente tipada, ou seja, durante a execução do programa pode-se alterar o tipo de dados de uma variável;
(e) Errado, PHP é case-sensitive.

PHP Version 5.3.0

Syslein
Duild Dato
Compilei
ArcMtecwre

Configure
Comniand

Server AF'I

Virtual Diroctory
Support

ConNguration F ito
(php.Hil) Palti

Loaded

Conflgut Jtion File

Sceti mH toi jddüicnal ini Hlei
AddWonnl Inl IHe»
parted

PHP API

PHP Extenskm
Zend Extemion

Zentf Extcmion
Build

PHP Exteniton
B*nld

Debug Üuíld
'hreed Snfety

Zentl Uemory
Manjger

Zend UuhM:/r*
Support iP.-ü Suppott
ReyÍ!»t<rted PHP
Streatni

Registered Strcaw
Sockel Trampod»

Regist»r»d Strafttn
Füton

Window» riT 6 1 butld 2600 (Wodm «P Protwsícnai Semce Pedi 3) i£86

Jun 29 2009 Z1 23 30

MSVCÍ iVteua C** 6 01
xM

cscntf noioço cocégur* fi eneoie-snapshci-Dwld -drsafcte iaÇ' -eeabie deènjç-peck" php-adkoracte'inslentcl»efli10.»dk ifcâred* ~—wíb-
oUQ^O pbp-sdksorecle^neiantcbent 10>sdk irteved" --wah'C-00***-*D íjvchsdk *oroci®
unstontctoiKl 1 Jdk shared -wflh-ench&nE*share<S

Apache 2 0 rtandler totolÉM
C tWHDOWS

C u«tmptEmtopeche<Apeche2 2 m

<r ji ^i inonel j'_ NdAP1220090GSTSVC6

API2W9O626 TS VCS

ãõ

HUM

MbM
diwtded enaiMO
php Fe gloti dM*. http tp ÜP campres» iib phar tcp udp ccrr.wrt ccn< itnrg rot 1J stmo touppw ífnrtq lc c iSrwis itnp tegs ccn«ed corwmod dechur* Xiifc *
Gabarito: Letra D

37. (CESPE/ABIN - 2010) A habilitação da característica de thread safety no painel de informações do ambiente de runtime PHP depende fundamentalmente do suporte que o sistema operacional oferta, e não, das características do zend engine.
Comentários:

Um servidor web deve lidar com diversas requisições de usuários, e para tal, pode criar um novo processo para cada nova requisição ou apenas um processo com diversas threads, uma para cada requisição. Historicamente, sistemas baseados em Unix utilizam processos para lidar com
/ 121

/

concorrência. Já quando se trata de Windows, a maioria dos Webservers irá tratar diferentes cliente sem diferentes threads.
No PHP, para que não haja conflitos entre as threads, ou seja, para que ele seja thread safe, se faz necessário um sistema de proteção para que cada thread mantenha acesso apenas às suas variáveis. Esse sistema é chamado de Zend Thread Safety ou ZTS, que depende do Zend Engine.
Gabarito: Letra E

38.(CESPE / ABIN - 2010) Considere que determinada aplicação web a ser desenvolvida em
PHP
deva ser integrada aos sistemas de controle de acesso já presentes nos ambientes de desenvolvimento e produção da organização. Nesse caso, se esses ambientes forem embasados em Kerberos ou em RADIUS (remote authentication dial in user service), o programador poderá obter êxito na integração por meio do uso de extensões providas pela biblioteca PECL(PHP
extension community library), tais como os packages KADM5 e RADIUS.

Comentários:

Correta. RADIUS (Remote Authentication Dial In User Service) é um protocolo de rede que fornece gerenciamento centralizado de Autenticação, Autorização e Contabilização para usuários que se conectam a e utilizam um serviço de rede. Kerberos é um protocolo de autenticação, que foi concebido para fornecer uma robusta autenticação para aplicações cliente-servidor através de criptografia de chave secreta.
Uma das formas de acessar servidores que utilizam o Kerberos é utilizando o KADM5
(Kerberos
Administration 5). Tanto o KADM5 quanto o RADIUS podem ser instalados pelo repositório de extensões PECL.
Gabarito: Correto

39.(CESPE / ABIN - 2010) O arquivo de configuração do PHP, de nome php.ini, será lido apenas no momento da inicialização (startup) do servidor HTTP associado ao referido IDE, que, no caso específico, é o Apache 2.2.11.
Comentários:

Correta. O arquivo de configuração, php.ini, é lido quando o PHP inicia. Para as versões de módulo de servidor, isso acontece apenas quando o servidorweb for iniciado. Vale notarque para as versõesCGI e CLI, isso acontece a cada invocação. O servidor HTTP é, realmente, o Apache
2.1.11, como podemos ver na imagem fornecida na questão no item Loaded Configuration File.
Gabarito: Correto

/ 121

/

4O.(CESPE / ABIN - 2010) Para que possa depurar os scripts PHP que construirá, o programador não necessita instalar depuradores externos, uma vez que a distribuição padrão de PHPvem acompanhada de depurador.
Comentários:

Errada. Como a questão é de 2010, na época o PHP não vinha com depurador,
necessitando desta forma de algum depurador externo (XDebug, por exemplo) em conjunto com algumaIDE
(Netbeans, Eclipse, PHPStorm, etc). Porém, a partir da versão 5.6 do PHP,
ele vem com um depurador próprio, o phpdbg que é um depurador interativo. Então se a questão cair novamente a resposta muda, beleza?! Fiquem atentos!
Gabarito: Errado

4i.(CESPE / ABIN - 2010) O acesso otimizado ao sistema gerenciador de banco de dados
(SGBD)
em uso nos ambientes de desenvolvimento e produção da organização pode ser obtido por meio da extensão PDO (PHP data objects), desde que seja habilitado o driver PDO específico do SGBDem uso, uma vez que a PDO não provê abstração completa do banco de dados, mas apenas uma camada de abstração para acesso aos dados, que não reescreve SQL nem emula funcionalidades de um SGBD.
Comentários:

O PDO (PHP Data Object) realiza uma abstração do banco de dados fornecendo uma biblioteca limpa e consistente, que unifica as características das extensões que acessam os bancos de dados.Porém, o PDO possui também algumas desvantagens, por exemplo, não efetua a leitura e tradução das instruções SQL, é apenas realizada uma fusão dos métodos mandados para as extensões respectivas. Principais características do PDO:
Flexibilidade - Como o PDO carrega o driver específico do banco de dados em tempo de execução,não é preciso reconfigurar o PHP sempre que um banco de dados diferente for usado.

Desempenho - O PDO está escrito em C e compilado no PHP, o que lhe garante um aumento considerável no desempenho em relação a soluções escritas em PHP.
Consistência de código - No PDO não existe a inconsistência de código, pois é oferecida apenas uma interface unificada que é está disponível para qualquer banco de dados.
Características de orientação de objetos - Possui recursos de orientação de objetos, o que resulta em uma comunicação mais poderosa e eficiente com banco de dados.
Gabarito: Correto

/ 121

/

42.(CESPE / ABIN - 2010) Caso o programador deseje criar, gerenciar e distribuir internamente à organização um ou mais packages que contenham módulos ou extensões porele desenvolvidos,é correto o uso da técnica de channels, que é embasada em arquitetura orientada a serviços(SOA), por meio da utilização de XML e REST (representational state transfer).

Comentários:

A questão mistura muitos conceitos causando uma confusão e, aparentemente, parece estarerrada por falar de um técnica do SOA (channels) e terminar falando de REST. Bem, um dos princípios doSOA é o reuso logo, se um programador desenvolveu um pacote de funcionalidade é interessante que este fique disponível para toda a organização, assim, caso alguém sinta a necessidade de alguma funcionalidade já coberta por este pacote, basta consumi-lo. Uma das formas de consumo é através de channels implementados em REST que é um forma de consumo para webservices mais simples que o SOA.
Gabarito: Correto

43.(CESPE / ABIN - 2010) Para instalar extensões do repositório PEAR (PHP
extension and application repository'), é correto o uso do Pyrus, uma versão refatorada do instaladorPEAR,
capaz de prover maior segurança aos processos, permitindo o gerenciamento e a distribuição de packages.
Comentários:

O PEAR (PHP Extension and Application Repository) é um repositório de diversas extensões doPHP, escritas em PHP. Um dos gerenciadores de pacotes PHP que suportava pacotes PEAR
era o pyrus descontinuado em 2011 devido a popularidade de um outro gerenciador de pacotes, oComposer. Vale lembrar que se utilizam gerenciadores de pacotes devido a facilidade com que eles integram as diversas dependências entre os pacotes, facilitando a vida do programador que não tem que ficar instalando as dependências dos pacotes uma a uma.
Gabarito: Correto

44.(CESPE / ABIN - 2010) Ao se escreverem scripts PHP, deve-se empregar indentação com espaços em branco, sem uso de tabs; atribuições em arrays devem ser alinhadas;comentários podem adotar o estilo C ou estilo C++, mas comentários em estilo PERL devem ser evitados.
Comentários:

Correta. Segundo a PSR (PHP Standard Recommendations), mais especificamente a PSR 2, ou
Guia de estilo de codificação (Coding Style Guide), que aborda como deve ser feita a formatação do código para facilitar a leitura por outros desenvolvedores, algumas das indicações são:
/ 121

/

- Devemos usar 4 espaços para indentação, não tabs.

- Não devemos fixar um número de caracteres por linha, mas é bom que uma linha tenha menos de80 caracteres.

- A abertura de colchetes de classes e métodos devem vir na próxima linha.
class Foo

{

public saMemberVar = 'aMemberVar Member Variable';
public $aFuncName = 'aMemberFunc';

function aMemberFuncO {
prinflnside 'aMemberFuncO'1;

}

- A abertura de colchetes de estruturas de controle deve vir na mesma linha com um espaço em branco.
for ($i = 1; $i <= 10; $i++) {
echo $i;

Comentários podem ser feitos com // (Tal como C e C++), # ou /* ... */ (Para blocos de comentário)
// comentário
## comentário

/* Comentário

Multi linhas

*/

Arrays em PHP são atribuídos da seguinte forma:

<?php

$cars = array("Volvo", "BMW", "Toyota");

?>

Sobre os comentários no estile PEARL, na documentação oficial do PHP não há menção alguma sobre evitar comentários com # (cerquilha, estilo PEARL), assim a questão está errada,porém o
CESPE considerou correta.

Gabarito: Correto

45.(CESPE / ABIN - 2010) Scripts de teste funcional devem conter a extensão .phpt, conforme prescreve o padrão de distribuição de módulos PHP; os diversos artefatos de teste relacionados a um módulo desenvolvido devem ser armazenados em subdiretório de nome tests, dentro do diretório do módulo ou package; dados de configuração específicos do ambiente de teste do desenvolvedor devem ser armazenados no arquivo de nome config.php.dist.
Comentários:

Na página oficial do PHP Assurance Quality Team, não há quaisquer das restrições impostas para realização de testes descritas no enunciado da questão. Um teste phpt é um pequeno script usado pelo php-src e equipes de Garantia de Qualidade (QA) para testar as funcionalidades doPHP, e ele pode ser usado com novos lançamentos para certificar-se de que eles continuem funcionando como nas versões anteriores, ou para ajudar a encontrar erros em versões atuais.
Gabarito: Errado

46.(CESPE / ABIN - 2010) Se o pedido http://localhost:8o8o/teste.php?nome=joao for aplicado de forma bem sucedida ao script apresentado a seguir, então, após o processamento do pedido, a saída de dados para o usuário deverá conter a stríng joao e um arquivo de nome joao.txt,contendo a palavra joao, existirá no computador onde se encontra o serviço HTTP
associado ao referido pedido.
<h tml Xbody >< ?php

$ponteiro fopen ( $_REQUEST['nome'].'.txt');
fwrite($ponteiro,$nome);

fclose($ponteiro);

echo $_GET['nome'];

?></body></html>

Comentários:

Pessoal, a questão está ERRADA, mas o CESPE anulou. Vamos analisar: trata-se de uma requisição do tipo GET. Vejamos a constituição da requisição:
http://localhost:8o8o/

URL para onde é mandada a requisição teste.php?
Script que será executado

?nome=joao

Variável nome com valor joao

Vamos analisar linha a linha:

$ponteiro = fopen ( $_REQUEST['nome'].'.txt']);

Cria um arquivo com o nome passado na URL através da variável nome(http://localhost:8o8o/teste.php?nome=joao) e extensão ".txt", porém, faltou especificar o modo é de escrita (poderíamos usar 'r+', 'w', 'w+', 'a', 'a+').
MODO DESCRIÇÃO

ABRE SOMENTE PARA LEITURA; COLOCA 0 PONTEIRO DO ARQUIVO NO COMEÇO DO
ARQUIVO.

ABRE PARA LEITURA E ESCRITA; COLOCA 0 PONTEIRO DO ARQUIVO NO COMEÇO DO
ARQUIVO.

ABRE SOMENTE PARA ESCRITA; COLOCA 0 PONTEIRO DO ARQUIVO NO COMEÇO 00
'W ARQUIVO E REDUZ 0 COMPRIMENTO 00 ARQUIVO PARA ZERO. SE 0 ARQUIVO NÃO

EXISTIR, TENTA CRIÁ-LO.
ABRE PARA LEITURA E ESCRITA; COLOCA 0 PONTEIRO DO ARQUIVO NO COMEÇO
DO

'W+' ARQUIVO E REDUZ 0 COMPRIMENTO 00 ARQUIVO PARA ZERO. SE 0 ARQUIVO NÃO

EXISTIR, TENTA CRIÁ-LO.
ABRE SOMENTE PARA ESCRITA; COLOCA 0 PONTEIRO 00 ARQUIVO NO FINAL 00

ARQUIVO. SE 0 ARQUIVO NÃO EXISTIR, TENTA CRIÁ-LO.

ABRE PARA LEITURA E ESCRITA; COLOCA 0 PONTEIRO DO ARQUIVO NO FINAL DO
ARQUIVO. SE 0 ARQUIVO NÃO EXISTIR, TENTA CRIÃ-LO.
CRIA E ABRE 0 ARQUIVO SOMENTE PARA ESCRITA; COLOCA 0 PONTEIRO NO COMEÇO

DO ARQUIVO. SE 0 ARQUIVO JÁ EXISTIR, A CHAMADA AFOPEN [] FALHARÁ,

'X' RETORNANDO FALSE E GERANDO UM ERRO DE NÍVEL E.WARNING. SE 0 ARQUIVO NÃO
EXISTIR, TENTA CRIÃ-LO. ISTO É EQUIVALENTE A ESPECIFICAR AS FLAGS

O_EXCL | O.CREAT PARA A CHAMADA DE SISTEMA 0PENÍ2).

CRIA E ABRE 0 ARQUIVO PARA LEITURA E ESCRITA; COLOCA 0 PONTEIRO NO COMEÇO
DO ARQUIVO. SE 0 ARQUIVO JÁ EXISTIR, A CHAMADA AFOPEN[] FALHARÁ,

'X+' RETORNANDO FALSE E GERANDO UM ERRO DE NÍVEL E_WARNING. SE 0 ARQUIVO NÃO
EXISTIR, TENTA CRIÃ-LO. ISTO É EQUIVALENTE A ESPECIFICAR AS FLAGS

O_EXCL | O-CREAT PARA A CHAMADA DE SISTEMA OPEN[2],

fwrite($ponteiro,$nome);

Escreve no arquivo criado o valor da variável $nome (no caso joao).
fclose($ponteiro);

Fecha o arquivo recem criado.
echo $_GET['nome'];

Imprime para usuário o valor da variável nome passado na requisição do tipo GET.

/ 121

/

Vale notar que as variáveis $_GET, $_POST e $_REQUEST são ditas 'superglobais', ou globais automáticas. Isto significa que elas estão disponíveis em todos escopos pelo script. Não há necessidade de fazer global svariable; para acessá-las dentro de uma função ou método.Pessoal,
embora o $_REQUEST trate tanto requisições POST quanto GET é aconselhável utilizar utilizar
$_GET para requisições GET e $_POST para requisições POST não só por questões de performance,
estilo e boa práticas. As variáveis $_REQUEST são providas para o script PHP via mecanismos de entradas GET, POST, e COOKIE e, portanto, poderiam ser modificadas por um usuário remoto e não podem ser confiadas.
Gabarito: Letra A

47.(CESPE / ABIN - 2010) Sabendo-se que a função array_multisort é capaz de ordenar múltiplos arrays na plataforma PHP, então a saída de dados gerada pela execução bem sucedida do script abaixo produzirá o resultado indicado em seguida.
<?php

$arl array(10, 100,

$ar2 arrayll, 3, 2,
array_multisort($arl,
va r_dump($a rl);

va r_dump($a r2);

?>

100, 0) ;

4) ;

$ar2) ;

Comentários:

Pessoal, esta questão trata de como a função array_multisort funciona. Ela é usada para ordenar vários arrays de uma vez ou apenas um array multi-dimensional de acordo com uma das dimensões.Os arrays dados são tratados como colunas de uma tabela a ser classificada pelas linhas - isso lembra a funcionalidade da cláusula ORDER BY da SQL.
O primeiro array é o principal na ordenação. As linhas (valores) no primeiro array servem de base para a ordenação do próximo, e assim por diante. A estrutura de argumentos dessa função não é muito normal, mas bastante flexível. O primeiro argumento de todos deve ser um array.Subsequentemente, cada argumento pode ser um array ou um dos sinais de classificação da lista a seguir.
Sinais de ordem de classificação:

SORT_ASC - classifica na ordem crescente
SORT_DESC - classifica na ordem decrescente

Sinais de tipos de ordenação:

SORT_REGULAR - compara os elementos normalmente
SORT_NUMERIC - compara os elementos como itens numéricos

SORT_STRING - compara os elementos como strings

Não podem existir dois sinais de ordenação do mesmo tipo especificados para um mesmo array. Os sinais de ordenação especificados depois de um array se aplicam apenas para esse array - a eles são atribuídos por padrão os valores SORT_ASC e SORT_REGULAR antes de cada novo argumento do tipo array.
Realizando o algoritimo na primera array, a segunda "acompanha"
com os índices correspondentes, como linhas de uma tabela (lembrando que o PHP utiliza o algoritmoQuicksort para ordenação de arrays).
1B Iteração

Array 1 Array 2

10 1

2a Iteração

Array 1 Array 2

10 1

0 4

3a Iteração

Array 1 Array 2

0 4

10 1

0 4

Logo, a afirmação está correta! Para fins de ilustração, vejamos outros exemplos da função array_multisort.
Exemplo i:

<?php

$ari - array("io", íoo, íoo, "a");

$ar2 = array(i, 3, "2", 1);
array_multisort($ari, $ar2);

?>

Saída: "10 // 100,100 e 1, i,"2",

Exemplo 2:

<?php

$ar = array(array ("10", 100,100, "a"), array (1, 3, "2", 1));
array_multisort($ar[o], SORT_ASC, SORT_STRING,

$ar[i], SORT_NUMERIC, SORT_DESC);

?>

Gabarito: Correto

48.(CESPE / ABIN - 2010) A execução bem sucedida do script apresentado abaixo produz como saída o valor 900.
<h tml Xbody >< ?php

$num=*14; Sdeslocado $num >> 2;

$scrrBF$des locado; $valorl=10; $valor2«20; $valor3=30;

$soma+«$valorl+$valor2;$soma*- $valor3;

$soma%-100;
echo $soma;

?></body></html>

Comentários:

Errada. Pessoal, vamos resolver linha a linha:

Linha i: snum = 14; sdeslocado = snum » 2;

O operador >> desloca snum de 2 bits para esquerda isso na prática corresponde a dividir por 4,vejamos: snum em binário é 1110, logo 1110 » 2 fica 11, então sdeslocado assume o valor 11 em binário, ou seja, 3. Assim terminamos a primeira linha com:
$num - 14 e sdeslocado - 3

Linha 2: $soma=$deslocado;$valori=io;$valor2=2o;$valor3=3o;

Aqui não temos nada demais a não ser atribuição de valores a variáveis. Terminamos a linha com:
$soma=3, $valon=io, $valor2=2o e $valor3=3o

Linha 3: $soma+=$valori+$valor2;$soma*=$valor3;

Nada demais, vejamos: $soma+=$valon+$valor2 equivale a ssoma = ssoma + svalon + $valor2
= 3

+ 10 + 20 - 33; $soma*=$valor3 equivale a ssoma = ssoma * $valor3 = 33 * 30 =
990; Assim terminamos a linha 3 com:
ssoma = 990

Linha 4: $soma°/o=ioo;

Aqui estamos utilizando o operador resto da divisão inteira, logo: $soma°/o=ioo equivale a ssoma =Ssoma % 100 - 990 % 100 = 90. Assim terminamos a linha 4 com:

ssoma = 90

Linha 5: echo ssoma;

Termina imprimindo o valor da variável ssoma que é igual a 90 e não 900.

Gabarito: Errado

49-(CESPE/ABIN - 2010) Se o pedido http://localhost/teste.php?nome=joao for aplicado deforma bem sucedida ao script apresentado abaixo, então a saída de dados deverá conter a string Você
/

deve preencher os campos. É correto afirmar, ainda, que uma conexão de socket foi estabelecida entre dois processos que se executam no mesmo computador onde se encontra o serviço HTTP associado ao referido pedido, sendo uma extremidade da conexão associada à porta 8o e a outra, a uma porta cujo número não se pode determinar pelas informações apresentadas.
<h tml >< bo dy > < ? ph p if (empty ($nome) OR empty ($email)) {echo " Você deve preencher os campos";

} else {

echo "olá $nome";

}

?></body></html>

Comentários:

Pessoal, vamos analisar as duas afirmativas da questão. Primeiro vamos entender o que a cláusula if testa. A entrada na cláusula if está condicionada a verificação das variáveis ínome e íemail, se ao menos uma estiver vazia então será impresso "Você deve preencher os campos". Se ambas não forem vazias então será escrito "Olá ínome", onde ínome será substituído pelo valor da variável.
Observando a URL da requisição http://localhost/teste.php?nome=joao, percebemos que se trata de uma requisição do tipo GET com apenas a variável $nome=joao, não há a passagem da variável email, logo, será impresso a string "Você deve preencher os campos".
Agora vamos a segunda afirmação que fala da porta do socket. Como podemos perceber pela própria URL, estamos realizando requisições para o endereço de localhost (ou 127.0.0.1- loopback),
ou seja, a conexão socket foi estabelecida entre dois processos do mesmo computador.
Por se tratar de uma requisição HTTP então a porta é de fato a 80.
Gabarito: Correto

5o.(CESPE / ABIN - 2010) Sabendo-se que a função natsort() opera com o conceito de ordenação natural, na qual as strings alfanuméricas são ordenadas da forma que um ser humano ordenaria,enquanto a função asort() opera com o conceito de ordenação classicamente usado em algoritmos de ordenação de strings, na ciência da computação, então a execução bem sucedida do script PHP apresentado abaixo produzirá, na saída, a primeira ocorrência da string imgi2.png antes da primeira ocorrência da string img2.png e a segunda ocorrência da string imgi2.png depois da segunda ocorrência da string img2.png.
/ 121

/

(Profs. Paolla Ramos e Raphael L

<?php

$A1~ $array2" array("imgl2.png", "imgio.png".
img2.png", "imgl.png");

asort($A1) ;
print_r($Al);

natsort($array2);
print_r($array2);

?>

Comentários:

Correta. Bom primeiro precisamos entender como natsort() e asort() ordenam. O
algoritmo de ordenação utilizado em natsort() ordena conforme um ser humano ordena, então, o resultado de natsort() sobre o array $Ai, tem como resultado:
$Ai= ["imgi.png", "img2.png", "imgio.png","imgi2.png"]

Agora o algoritmo de ordenação utilizado em asort(), compara as strings caractere por caractere,de forma a preservar a ordem de cada um dos caracteres que compõem as strings.
Assim, asort()
sobre o array $array2, tem como resultado:

$array2 = ["imgi.png", "imgio.png", "imgi2.png", "img2.png"]

Agora vamos a saída do script PHP. Como a ordem de execução é do asort($Ai), seguida da impressão do array $Ai e depois do natsort($array2) e a impressão do array $array2, temos:
["imgi.png", "imgio.png", "imgi2.png", "img2.png"]

["imgi.png", "img2.png", "imgio.png", "imgi2.png"]

Logo, a primeira ocorrência de imgi2.png ocorre antes da primeira ocorrência de img2.png e a segunda ocorrência de imgi2.png ocorre depois da segunda ocorrência de img2.png.
Gabarito: Errado

5i.(CESPE / ABIN - 2010) Uma sessão PHP é criada ou recuperada automaticamente durante a execução do script.
Comentários:

Errada. Uma sessão web é bem parecida com a sessão de um PC, que ao iniciar, temos que colocar usuário e senha, assim seu computador pode saber quem está usando a máquina e guardar os registros com segurança. Em um site ou sistema web, a sessão é importante quando se quer mais segurança na página ou quando se querter um controle de usuário.
Também alguns programadores se utilizam deste recurso para guardar informações e ou montar um carrinho de compras de um site de vendas, pois assim vão armazenando-se os itens ou produtos e só no final é que os dados são jogados no banco de dados.
Nota: A variável de sessão PHP é usada para armazenar informações sobre, ou alterar as configurações do sistema ou site para uma sessão de usuário. As variáveis de sessão armazenam informações sobre um único usuário e estão disponíveis para todas as páginas em um único aplicativo.
No código apresentado não há em momento algum a utilização da variável $_SESSION,
logo, não será possível recuperara sessão.
Gabarito: Errado

52.(CESPE / ABIN - 2010) A senha do usuário que está no banco de dados não foi criptografada com um hash, fato que torna a aplicação vulnerável a ataques de dicionário.
Comentários:

Pessoal, essa questão ao meu ver é polêmica. De fato, não há elementos que nos permitam afirmar que a senha está ou não criptografada no banco de dados. Para isso precisaríamos ter ciência se os valores salvos na coluna "senha" foram submetidos a alguma função de hash (MD5,SHA256, etc).
Contudo é muito provável que não esteja criptografada pois não é aplicada nenhuma função de hash sobre a senha no código PHP fornecido.
Quanto a ataques de dicionário não tem mistério, é usar SENHAS FORTES. Como sabemos que muitas vezes os usuários, mesmo conscientes, negligenciam isso podemos implementar mecanismos extras como autenticação de dois fatores (2FA), bloqueio de conta após um certo número de tentativas falhas, entre outros.
Gabarito: Errado

53.(CESPE / ABIN - 2010) O banco de dados MySQL é usado pelo script, mas a conexão com o banco deveria ter sido encerrada ou devolvida ao pool ao final do script,fato que não se concretiza.
Comentários:

É fácil verificar que o banco é o MySQL, pois o conector usado é o conecta_mysql.inc. E sim, a conexão com o banco deveria ter sido encerrada com um mysql_free_result($r),isso evita que memória fique alocada para consultas que já passaram.
/ 121

/

Gabarito: Correto

54. (CESPE / ABIN - 2010) O pedido HTTP que pode ser atendido por esse script não poderá conter cookies de nomes nu e su, além de estar sujeito a ataques de SQL injection.
Comentários:

Pessoal, esta questão está bem confusa. Primeiro os cookies foram criados sem estabelecer um tempo de validade, assim, eles vão expirar ao fim da sessão, ou seja, não adianta nada setar os cookies, pois em um novo acesso o usuário terá que colocar as credenciais de acesso novamente e conforme a lógica de login os cookies nu e su serão sobrescritos.
Quanto a sujeição à ataques de SQL injection, é uma boa práctica validar os dados dos campos usuário e senha, que são utilizados para montar uma consulta SQL. Poderíamos usar um caractere de escapamento e fazer outras buscas além do nome do usuário e de sua senha. Existem formas de fazer isso utilizando a função htmlspecialchars() e a mysql_real_escape_string();
Gabarito: Errado

55. (CESPE / ABIN - 2010) Os softwares de servidores web, ao aderirem à arquitetura de sistemas operacionais, empregam modelo de memória virtual, que atua como um cache de memória e contém parte das instruções e dados executados por um script em determinado instante de tempo. Assim, o script não precisa estar armazenado simultaneamente na memória principal e no disco; com isso, a memória total disponível para um script ou programa pode exceder o tamanho da memória principal do sistema.
Comentários:

Quem emprega o modelo de memória virtual é o sistema operacional, a memória utilizada é transparente para o software. Além disso cache e memória virtual são coisas distintas.Memória cache ou simplesmente cache é usado para armazenar dados acessados com frequência, a fim de acessar rapidamente os dados sempre que for necessário.
Ambos são conceitualmente a mesma coisa, porém diferem principalmente em matéria de execução, que resulta em diferentes aspectos, como velocidade e controle de mecanismo. Memória virtual é usada para ocultar a informação da memória física real do sistema. Estende-se a memória disponível do computador, armazenando as partes inativas do conteúdo RAM em um disco.
Memória virtual cria uma ilusão de que um usuário tem um ou mais espaços de endereços contíguos que começam com endereço zero.
Gabarito: Errado

56.(CESPE/ ABIN-2010) O formato JSON (javascript object notation) permite representar objetos e classes como estruturas de dados e arrays associativos, sendo possível seu uso em combinação com Ajax e PHP, por meio de bibliotecas diversas, como DOJO.
Comentários:

JSON (JavaScript Object Notation - Notação de Objetos JavaScript) é uma formatação leve de troca de dados. Para seres humanos, éfácil de lere escrever. Para máquinas, é fácil de interpretar e gerar.Está baseado em um subconjunto da linguagem de programação JavaScript, Standard ECMA-262
3a Edição - Dezembro -1999.

JSON é em formato texto e completamente independente de linguagem, pois usa convenções que são familiares às linguagens C, C++, C#, Java, JavaScript, Perl, Python e muitas outras. Estas propriedades fazem com que JSON seja um formato ideal de troca de dados.
Já o DOJO é uma biblioteca de JavaScript modular de código aberto (ou mais especificamente o kit de ferramentas do JavaScript), projetado para facilitar o rápido desenvolvimento de aplicativos e sites da plataforma baseados em JavaScript / Ajax. Entre os módulos disponibilizados há o dojo/json que trata de json (parsing, serialization, etc).
Gabarito: Correto

57.(CESPE / ABIN - 2010) Arrays associativos, usados em PHP e em outras linguagens de script,podem ser implementados de forma eficiente, do ponto de vista de consumo de memória,
por meio do uso de tabelas de dispersão. Para garantir eficiência, essas tabelas precisam ser totalmente livres de colisão, tal que, na implementação de métodos de busca, as pesquisas sejam executadas em tempo constante, independentemente do valor pesquisado.
Comentários:

Pessoal, tabelas de dispersão nada mais são que os famosos hash (plural hashes). Ela é uma estrutura de dados especial, que associa chaves de pesquisa a valores. Seu objetivo é,a partir de uma chave simples, fazer uma busca rápida e obter o valor desejado. Estas tabelas utilizam funções de espalhamento, que nada mais são que funções que geram a partir de uma chave um determinado índice que facilita a busca subsequente.
O ideal para a função de espalhamento é que sejam sempre fornecidos índices únicos para as chaves de entrada. A função perfeita seria a que, para quaisquer entradas A e B, sendo Adiferente de B,
fornecesse saídas diferentes. Quando as entradas A e B são diferentes e, passando pela função de espalhamento, geram a mesma saída, acontece o que chamamos de colisão.
Na prática, funções de espalhamento perfeitas ou quase perfeitas são encontradas apenas onde a colisão é intolerável (por exemplo, nas funções de dispersão da criptografia), ou quando x53
/ 121

/

conhecemos previamente o conteúdo da tabela armazenada. Nas tabelas de dispersão comuns a colisão é apenas indesejável, diminuindo o desempenho do sistema.
Muitos programas funcionam sem que seu responsável suspeite que a função de espalhamento seja ruim e esteja atrapalhando o desempenho. Por causa das colisões, muitas tabelas de dispersão são aliadas com alguma outra estrutura de dados, tal como uma lista encadeada ou até mesmo com árvores balanceadas. Em outras oportunidades a colisão é solucionada dentro da própria tabela.
Gabarito: Errado

58.(CESPE / ABIN - 2010) Estruturas de dados padronizadas, como listas ligadas duplamente encadeadas, pilhas, filas, filas de prioridade e arrays numéricos de tamanho fixo, são disponíveis em PHP por meio da extensão SPL {standard PHP library).
Comentários:

Essa é fácil! A maioria das linguagens de alto nível orientadas a objeto já tem em suas bibliotecas padrão, implementações para diversos problemas conhecidos na computação. A SPL é aStandard
PHP Library e fornece uma coleção de interfaces e classes que servem para resolver problemas padrões.
Gabarito: Correto

5g.(CESPE / ABIN -2010) Algoritmos recursivos normal mente têm menor tempo de resposta que seus equivalentes iterativos, mas as linguagens PHP e Javascript, por serem linguagens de script,não permitem nem necessitam de recursividade.

Comentários:

Primeiramente, algoritmos recursivos são classicamente mais custosos que os iterativos e estão suscetíveis a diversos problemas como o famoso stackoverflow (estouro da pilha de memória).Além disso PHP e javascript permitem sim o uso da recursividade.

Gabarito: Errado

6o.(FUND / CIG - 2020) Qual dos trechos de código abaixo, em linguagem PHP 5.5, é executado sem erros e, adicionalmente, pode ser considerado o mais seguro para fazer uma consulta em uma tabela de usuários em um banco de dados relacional PostgreSQL?
a) ínome = "João"; $sql = "SELECT nome, sobrenome, senha FROM tb_usuario WHERE
nome=$nome;"; sresultado - pg_query($conn, $sql);

/ 121

/

b) $nome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, senha FROM
tb_usuario
WHERE nome='$nome;'"; sresultado - pg_secure_query($conn, $sql);

c) ínome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, senha FROM
tb_usuario
WHERE nome=$i;"; sresultado = pg_query_params($conn, $sql, array($nome));

d) ínome - $_GET["nome"j; $sql = "SELECT nome, sobrenome,
senha WHERE
nome='$nome';"; $resultado = pg_query($conn, $sql);

e) ínome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, encrypt(senha) FROM
tb_usuario WHERE nome=$nome;"; $resultado = pg_query_params($conn, $sql);

Comentários:

Tem questões pessoal que a Banca deveria responder judicialmente por fazer algo que não avalia nenhum conhecimento. Mas vamos lá..
(a) O valor de "ínome" deveria vir da requisição, esse é o erro; (b) Não existe
"pg_secure_query".
Além disso, ao usar o "ínome", estou apenas interpolando strings para montar minha query, o que é inseguro; (c) Correto; (d) Só faltou o FROM; (e) A senha já é armazenada em formato de hash, não há necessidade da função encrypt. Além disso, essa função é do MySQL, não existe no PostgreSQL
Gabarito: Letra C

6i.(CESPE / MPE-AP - 2021) No desenvolvimento de um sistema em PHP, o desenvolvedor precisa validar se o endereço bob@mpap.mp.br é ou não um email válido. A partir dessa situação hipotética, assinale a opção em que o código apresentado é o correto para o desenvolvedor realizar a referida validação, tendo como referência que a variável a sertestada é $email.
a) <?php if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { echo "Invalid email format";}
else {
echo "Valid email format";} ?>

b) <?php if (!preg_match("/A[a-zA-Z-' ]*$ @./", íemail)) {echo "Invalid email format";}
else {
echo "Valid email format";} ?>

c) <?php if (emailspecialchars($email)) {echo "Valid email format";} else {echo "Invalid email format";} ?>
d) <?php if (ctype_alnum ($email)) {echo "Valid email format";} else {echo "Invalid email format";} ?>
e) <?php if (strncasecmp ($email, 7A[a-zA-Z-' ]*$ @./")) {echo "Valid email format";}
else {
echo "Invalid email format";} ?>

x

/ 121

/

Comentários:

Existem várias formas de validar um e-mail em PHP, dentre elas temos a utilização doFILTER-VALIDATE-EMAIL

Gabarito: Letra A

62.(QUADRIX/ CRM 4 - 2021) Considerando o trecho de código acima, julgue o item.

<?php
IncludeCpages/footer.php');

?>

O construtor include() está incluindo o arquivo pages/footer.php. Caso seja utilizado o construtor require() ao invés do construtor include() e o arquivo footer.php não seja encontrado no diretório pages, será apresentado um warning, indicando que o arquivo não foi encontrado,mas permitindo ainda a execução do script.

Comentários:

O construtor include () avisa caso tenhamos um erro, mas é somente isso. Já o require () gera um faltai error.
Gabarito: Errado

63.(QUADRIX / CRM 4 - 2021) Na linguagem PHP, a função Itrimfjé utilizada para retirar os espaços em branco no início e no final de uma string.
Comentários:

A função ltrim() retira espaços em branco no inicio da string.

Gabarito: Errado

64.(APICE / DPE-PB - 2021) O PHP (um acrônimo recursivo para PHP: Hypertext
Preprocessor) é uma linguagem de script open source de uso geral, muito utilizada, e especialmente adequada para o desenvolvimento web e que pode ser embutida dentro do HTML.
Comentários:

Perfeito! O PHP (um acrônimo recursivo para PHP: Hypertext Preprocessor) é uma linguagem descript open source de uso geral, muito utilizada, e especialmente adequada para o desenvolvimento web e que pode ser embutida dentro do HTML.
Gabarito: Correto

65.(PS CONCURSOS / PREFEITURA DE SC - 2021) Analise o código abaixo e responda, a qual linguagem de programação melhor se enquadra essa sintaxe:
Svl = 40;

Sv2 - 20;

if ( $vl > $v2 ) {

echo variável M.$vl. " e maior que a variável ".Sv2;
}

Alternativas:

a) ASP

b) PASCAL

c) JAVA

d) C#

e) PHP

Comentários:

Exato! Temos um código PHP.

Gabarito: Letra E

66. (CESPE / MINISTÉRIO DA ECONOMIA - 2020) Uma expressão lambda é usada principalmente para definira implementação procedural de uma interface associativa.
Comentários:

Uma expressão Lambda é uma função anônima que você pode usar para criar delegados ou tipos de árvore de expressão.
Gabarito: Errado

67.(CESPE / TJ-AM - 2019) Após a configuração de um servidor Apache com módulo PHP,
uma forma de validar o seu funcionamento é criar uma página HTML e inserir a função phpinfo (),que mostra informações a respeito da configuração do PHP no servidor Apache.

Comentários:

Perfeito! Após a configuração de um servidor Apache com módulo PHP, uma forma de validar o seu funcionamento é criar uma página HTML e inserir a função phpinfo (), que mostra informações a respeito da configuração do PHP no servidor Apache.
Gabarito: Correto

68. (CESPE/TJ-AM - 2019) A função current () não retorna o valor armazenado onde o ponteiro atual aponta.
Comentários:

A função current () retorna o valor armazenado onde o ponteiro atual aponta.

Gabarito: Errado

69. (CESPE / TJ-AM - 2019) A linguagem PHP suporta o uso de operadores lógicos capazes de diversas comparações lógicas. O operador && considera que uma comparação será verdadeira se um ou ambos os argumentos forem verdadeiros.
Comentários:

O operador && representa o "AND", isto é, ambos devem ser verdadeiros. Já o || (Or)
- Um dos dois for verdadeiro.
Gabarito: Errado

70.(CESPE / MP-SC - 2014) PHP é uma linguagem de alto nível, logo o programador precisar acessar diretamente a memória para acionar os ponteiros em uma implementação.
Comentários:

PHP é alto nível e acessar ponteiro em memória é baixo nível.

Gabarito: Errado

71. (SELECON / EMGEPRON - 2021) A figura mostra um código em PHP.

/ 121

/

<!DOCTYPE html>

<html>

<body>

<?php

$m = 44;

$n - 27;

$p = 15;
echo ++$p;

if ($m « 44 or $n « 79) {
echo w EMGEPRON!";

}

else {

echo M MARINHA!";

}

?>

</body>

</html>

Após a execução, a saída está indicada na seguinte opção:

a) 16 MARINHA!

b) 15 MARINHA!

c) 16 EMGEPRON!

d) 15 EMGEPRON!

Comentários:

Ao executar o código, a saída será 16 EMPREPRON! O ++$a: realiza o pré-incremento,
assim,
incrementa $a em um, e então retorna $a. Logo, irá imprimir o número 16. Já o operador lógico fará o seguinte: $a or $b: Verdadeiro se $a ou $b são verdadeiros.
$m==zhzh: V

$n==79): F

Resultado Verdadeiro.

Assim imprime "ENGEPRON!";

Gabarito: Letra C

72. (APICE / DPE-PB - 2021) Existe a possibilidade dos valores do array em PHP serem outros arrays e árvores. Incluindo a biblioteca com a diretiva #include<Arrays>, é possível realizar a manipulação de arrays multidimensionais.
Comentários:

Não é preciso importar biblioteca para manipular arrays multidimensinais. Além disso,
imports em
PHP são feitos com "require", "include" ou suas variantes.

00 SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital)

Gabarito: Errado

73.(APICE / DPE-PB - 2021) Um array no PHP é tipo que relaciona valores a chaves.
Este tipo é otimizado para várias usos diferentes: ele pode ser tratado como um array,uma lista
(vetor), hashtable (que é uma implementação de mapa), dicionário, coleção, pilha ou fila.

Comentários:

Exato! Um array no PHP é tipo que relaciona valores a chaves. Este tipo é otimizado para vários usos diferentes: ele pode ser tratado como um array, uma lista (vetor), hashtable(que é uma implementação de mapa), dicionário, coleção, pilha ou fila.
Gabarito: Correto

74.(APICE / DPE-PB - 2021) Para definir uma classe no PHP, deve-se começar com a palavra-chave class, seguida do nome da classe e de um par de colchetes que englobam as definições de propriedades e métodos pertencentes à classe.
Comentários:

Perfeito! Para definir uma classe no PHP, deve-se começar com a palavra-chave class,
seguida do nome da classe e de um par de colchetes que englobam as definições de propriedades e métodos pertencentes à classe.
Gabarito: Correto

75.(APICE / DPE-PB - 2021) Quando PHP interpreta um arquivo, uma procura pelas tags de abertura e fechamento, <?php e ?>, é realizada. Estas tags indicam para iniciar ou parar a interpretação do código entre elas.
Comentários:

Perfeito! Quando PHP interpreta um arquivo, uma procura pelas tags de abertura e fechamento,
<?php e?>, é realizada. Estas tags indicam para iniciar ou parara interpretação do código entre elas.
Gabarito: Correto

76.(CIGA-SC - 2020) Para responder à questão, considere o código apresentado pela
Figura 7
abaixo, escrito em PHP 5.5:

<?php dass Fundonario {public $nome;

public Ssituacao;
public Stipo;

function construct($nome) {

$this->nome = $nome;

>

>

dass FundonarioAtivo extends Fundonario {
function construct($nome) {

parent:: construct(Snome);

$this->situacao "ativo*;

>

>

dass Fundonariolnativo extends Fundonario {

function Fundonariolnativo($nome) {

parent:: construct(Snome);

$this->situacao "inativo";

>

}

$fal new FuncionarioAtivo("João");

$fa2 = new FuncionarioAtivo("Joáo");

$fi = new FuncionarioInativo("Joáo");

?>

Analise as seguintes expressões lógicas escritas em PHP 5.5, caso fossem avaliadas logo após a execução do código apresentado anteriormente:
1. $fai===$fi

2. $fai==$fi

3. $fai===$fa2

4. $fai==$fa2

A alternativa que apresenta o resultado correto das expressões é:

a) TRUE - FALSE - FALSE - FALSE

b) TRUE - TRUE - FALSE - FALSE

c) FALSE-TRUE-TRUE-TRUE

d) FALSE-FALSE-FALSE-TRUE

e) FALSE-FALSE-TRUE-TRUE

Comentários:

Pessoal, como falamos anteriormente quando utilizamos == vamos comprar só o valor e não o tipo.Se utilizamos 0 === estamos comparando o valor e o tipo. Logo:

1. $fai===$fi: FALSE

2. $fai==$fi: FALSE

3. $fai===$fa2: FALSE

4. $fai==$fa2: TRUE

Gabarito: Letra D

77. (Prefeitura de São Paulo - 2020) Analise o trecho do código PHP a seguir.

$x -10;

if ($x == '10') {
echo"SIM";

} else {

echo "NÃO";

}

Ao ser executado, esse código apresentará a mensagem:

a) "SIM", pois o operador "==" compara apenas o valor e não o tipo.

b) "SIM", visto que o operador "==" é de atribuição, e seu resultado é sempre verdadeiro.

c) "NÃO", pois os tipos das variáveis são diferentes e não podem ser comparados.

d) NÃO", pois cadeias de caracteres devem ser delimitadas por aspas duplas, caso contrário apenas o primeiro caractere é considerado.
e) "NÃO", pois a comparação de variáveis com tipos diferentes sempre retorna "falso".

Comentários:

Ao executar o código, teremos a mensagem SIM, porque o operador == vai comprar só o valore não o tipo. Seria NÃO, ao invés de SIM, se fosse if ($x === '10') { porque nesse caso,estaremos comparando o valor e o tipo.
Gabarito: Letra A

78.(UFMT - UFMT - 2021) Um conceito muito importante em programação orientada a objetos é o de exceções. Exceções podem serconceituadas como ocorrências de programação tidas como inválidas durante o processamento e que paralisam o programa até que sejam resolvidas.
Em PHP, exceções são objetos especiais e derivam da classe Exception, possuindo métodos específicos de retorno. Selecione, a seguir, a alternativa que lista apenas métodos presentes na referida classe Exception do PHP:
a) getMessage(), getCode(), getTraceAsString().

b) getLine(), getStackTraceStringO, getFile().

c) getPrevious(), getTrace(), getSuppressed().

d) try(), catch(), finaIly().

e) getStackTraceStringO, getCode(), getMessage().

Comentários:

Falou da classe exception, conforme vimos é só lembrar dos métodos: getMessage(),
getCode(),
getTraceAsStringO

Gabarito: Letra A

79.(UFMT - UFMT - 2021) O Hypertext Preprocessor (PHP) é uma linguagem de script usada no desenvolvimento web. Sobre o PHP, marque V para as afirmativas verdadeiras e F para as falsas
() Possui tag que indica final do código PHP.
() Trata-se de uma linguagem open source.
() Elimina o uso de códigos HTML e CSS.

() O código é executado apenas no cliente.
Assinale a sequência correta.

a) V,V,F,F

b) F,F,V,V

c) F,V,F,V

d) V,F,V,F

Comentários:

Organizando então o que vimos ao longo da aula sobre PHP, temos: (V) Possui tag que indica final do código PHP; (V) Trata-se de uma linguagem open source; (F) Elimina o uso de códigos HTML eCSS. (Não faz o menor sentido dizer isso); (F) O código é executado apenas no cliente. (PHP é executado do lado servidor).
Gabarito: Letra A

8o.(CONSULPLAN / Prefeitura de Colômbia-SP - 2021) Comando do PHP (Personal Home Page)
"adiciona um parâmetro a um procedimento armazenado local ou remoto quando utilizado com o Microsoft SQL Server". A afirmativa se refere a:
a) mssqljnit b) mssql_bind c) mssql_execute d) mssql_fetch_row
Comentários:

Estou trazendo esse tipo de questão pessoal, porque realmente não tem como sair fora,
as bancas podem cobrar esse tipo de coisa. O parâmetro em questão é o mssql_bind
Gabarito: Letra B

8i.(CONSULPLAN / Prefeitura de Colômbia-SP - 2021) Considerando as funções do PHP para manipulação de documentos em PDF, uma delas "preenche o caminho atual e o desenha no documento". Trata-se de:
a) pdf_fill b) pdf_stroke c) pdf_fill_stroke d) pdf_filLtextblock
Comentários:

Para preencher o caminho atual de desenha no documento, temos a função: pdf_fiIl_stroke

Gabarito: Letra C

82.(CESPE / PGDF - 2021) PHP é uma linguagem de script projetada para desenvolvimento web,mas que também pode ser usada para programação de uso geral.

Comentários:

Perfeito! Exatamento o que vimos na aula. PHP é uma linguagem de script projetada para desenvolvimento web, mas que também pode ser usada para programação de uso geral
Gabarito: Correto

83.(OBJETIVA / Prefeitura de Santa Maria-RS - 2021) Conforme BONATTI, sobre tecnologias e linguagens utilizadas na construção de websites, numerar a 2a coluna de acordo com a ia e,após, assinalara alternativa que apresenta a sequência CORRETA:

i)CSS.

(2) PHP.

(3) HTML.

( ) É uma linguagem de programação open source, que é interpretada pelo servidor, muito utilizada para o desenvolvimento de aplicações voltadas para a internet.
( ) Serve para promover o acabamento visual das páginas web. Pode ser compartilhado entre várias páginas, permitindo, assim, uma padronização visual muito simplificada e lógica.
/ 121

/

( ) É uma linguagem de marcação, que é interpretada pelo browser para dar formatação e posicionamento ao conteúdo do website.
a) i-2-3

b) 3-2-1

c) 2 - 3 -1

d) 2-1-3

e) 3-i-2

Comentários:

Pessoal, questão simples não é verdade, só para nos lembrar alguns fundamentos: (PHP)
É uma linguagem de programação open source, que é interpretada pelo servidor, muito utilizada para o desenvolvimento de aplicações voltadas para a internet; (CSS) Serve para promover o acabamento visual das páginas web. Pode ser compartilhado entre várias páginas,permitindo, assim, uma padronização visual muito simplificada e lógica; (HTML) É uma linguagem de marcação, que é interpretada pelo browser para dar formatação e posicionamento ao conteúdo do website
Gabarito: Letra D
84.(OBJETIVA / Prefeitura de Santa Maria-RS - 2021) Considere o seguinte código escrito na linguagem PHP.
<?php function inversa($x) { if ($x==o) { throw new Exceptionf exception ');
} return i/$x;

} try { echo inversa(o); echo " try catch (Exception $e) { echo " catch
"; echo $e-

>getMessage();} finally { echo " finally";}

Ao se executar esse código, será impressa na tela a seguinte sequência de palavras:

a) try catch exception finally b) try catch finally c) catch exception finally d) catch exception e) finally catch exception
Comentários:

Temos no caso uma exceção (exception) dentro de um try tempos uma interrupção e continua no catch até o finally. Logo, echo inversa(o); Vai lançar a exceção dentro dolFe ir direto para a cláusula catch sem imprimir nada.
echo " catch " -> Imprime catch echo $e->getMessage(); -> Imprime ' exception ' e echo " finally-
> Imprime " finally". Assim, será impressa na tela a sequência: catch exception finally

/ 121

/

Gabarito: Letra C

85.(OBJETIVA / Prefeitura de Santa Maria-RS - 2021) A forma correta de se declarar uma constante na linguagem PHP é:
a) constant "XPTO" = "alguma coisa";

b) constant $XPTO = "alguma coisa";

c) constant("XPTO","alguma coisa");

d) declare("XPTO","alguma coisa");

e) define("XPTO","alguma coisa");

Comentários:

A função define() é a opção mais conhecida do PHP para criar constantes. Utilizamos essa função quando precisamos declarar uma constante com escopo global, isto é, fora do escopo de uma classe. Basta então utilizar: define ("XPTO", "alguma coisa")
Gabarito: Letra E

86. (CESPE / FUNPRESPJUD - 2021) Quando enviamos um arquivo através de um formulário para o PHP, ele cria a super global $_FILES, no mesmo estilo das super globais $_GET e $_POST.Cada campo do tipo file é colocado em um array dentro de $_FILES.

Comentários:

Foi literalmente o que vimos na aula. Lembre-se então que quando enviamos um arquivo através de um formulário para o PHP, ele cria a super global $_FILES, no mesmo estilo das super globais
$_GET e $_POST. Cada campo do tipo file é colocado em um array dentro de $_FILES

Gabarito: Errado

87.(UFSC / UFSC - 2016) Considere o seguinte fragmento de código presente em uma página de uma aplicação escrita em PHP:
<p<?php if (sdestaque): ?class="destaque"<?php endif;»Parágrafo.</p>

O fragmento gerará qual código HTML, caso o valor da variável "sdestaque" seja verdadeiro(true), quando a página for requisitada por um navegador?

a) <p class="destaque">Parágrafo.</p>

b) <p>Parágrafo.</p>

c) Parágrafo.

d) <p class="$destaque">Parágrafo</p>

e) <px/p>

Comentários:

O código PHP em questão, se for compilado com sdestaque = true, vai ter como saída: <p class="destaque">Parágrafo.</p>
Gabarito: Letra A

88. (FGV / TJ-TO - 2022) Num script PHP, a função que permite verificar se um cookie está definido é:
a) active()

b) cookie_value()

c) exists()

d) isset()

e) status()

Comentários:

Para permitir a verificação de cookie utiliza-se a função isset () no PHP.

Gabarito: Letra D

89. (FGV / TJ-TO - 2022) Numa página web, um script PHP deve ser localizado entre as tags:

a) <?php ?>

b) <php php>

c) <?php> <?>

d) <scriptPHP scriptPHP>

e) <.php ,php>

Comentários:

No PHP, conforme estudamos um script dever estar localizado entre as tags: <?php ?>

Gabarito: Letra A

9O.(FCC/TJ-SC-2O2i) Considere o método abaixo, em uma classe PHP chamada Cliente,
public function setNome($Nome) {

$this->Nome = $Nome;

A partir de outra classe, um objeto na classe Cliente foi instanciado por meio da instrução $cli =new Cliente;. Para chamar o método acima e passar o nome 'Paulo' como parâmetro,
utiliza-se a instrução:
a) $cli::setNome('Paulo');

b) $cli->setNome('Paulo');

c) $cli.nome('Paulo');

d) $cli->send.setNome('Paulo');

e) $cli.setNome('Paulo');

Comentários:

Para chamar o método, passando o nome 'Paulo', utiliza-se a instrução $cli->setNome('Paulo');

Gabarito: Letra B

gi.fVUNESP / PREF. ILHABELA - 2020) Analise o trecho de código PHP a seguir.

$x = 10;

if ($x == '10') {
echo"SIM";

} else {

echo "NÃO";

Ao ser executado, esse código apresentará a mensagem:

a) "SIM", pois o operador "==" compara apenas o valor e não o tipo.

b) "SIM", visto que o operador "==" é de atribuição, e seu resultado é sempre verdadeiro.

c) "NÃO", pois os tipos das variáveis são diferentes e não podem ser comparados.

d) NÃO", pois cadeias de caracteres devem ser delimitadas por aspas duplas, caso contrário apenas o primeiro caractere é considerado.
e) "NÃO", pois a comparação de variáveis com tipos diferentes sempre retorna "falso".

Comentários:

A mensagem a ser apresentada será "SIM", pois o operador compara apenas o valor e não o tipo.
Gabarito: Letra A

92.(FUNDATEC / CIGA-SC - 2020) Qual dos trechos de código abaixo, em linguagem PHP
5.5, é executado sem erros e, adicionalmente, pode ser considerado o mais seguro para fazer uma consulta em uma tabela de usuários em um banco de dados relacional PostgreSQL?
a) $nome = "João"; $sql = "SELECT nome, sobrenome, senha FROM tb_usuario
WHERE
nome=$nome;"; $resultado = pg_query($conn, $sql);

b) $nome = $_GET["nome"]; $sql - "SELECT nome, sobrenome, senha FROM
tb_usuario
WHERE nome='$nome;'"; $resultado = pg_secure_query($conn, $sql);

c) $nome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, senha FROM
tb_usuario
WHERE nome=$i;"; $resultado = pg_query_params($conn, $sql, array($nome));

d) $nome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, senha
WHERE
nome='$nome';"; sresultado = pg_query($conn, $sql);

e) $nome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, encrypt(senha) FROM
tb_usuario WHERE nome=$nome;"; íresultado = pg_query_params($conn, $sql);

Comentários:

(a) Errado. O valor de "snome" deveria vir da requisição; (b) Errado. Não existe
"pg_secure_query".
Além disso, ao usar o "$nome", estou apenas interpolando strings para montar minha query, o que é inseguro; (c) Correto; (d) Errado. Faltou o "FROM"; (e) Errado. A senha já é armazenada em formato de hash, não há necessidade da função encrypt. Além disso, essa função é doMySQL, não existe no PostgreSQL.
Gabarito: Letra C

93.(CESPE / TCE-SP 2015) Em PHP é possível usar uma variável sem declarar seu tipo,
que será decidido, também, durante a execução do programa.
Comentários:

Em PHP, é possível usar uma variável sem declarar seu tipo, que será decidido,
também, durante a execução do programa.
Gabarito: Correto

94.(CESPE / TCE-SP 2015) PHP é uma linguagem de programação de scripts, interpretada,
de baixo nível, open-source, gratuita, server-side, dinamicamente/fracamente tipada,estruturada e orientada a objetos, portável, robusta e eficiente utilizada para desenvolvimento web.
Comentários:

Perfeito! PHP é uma linguagem de programação de scripts, interpretada, de baixo nível, open-source, gratuita, server-side, dinamicamente/fracamente tipada, estruturada e orientada a objetos,portável, robusta e eficiente utilizada para desenvolvimento web

Gabarito: Correto

95.(CESPE / TJ-AM - 2019) A linguagem PHP suporta o uso de operadores lógicos capazes de diversas comparações lógicas. O operador && considera que uma comparação será verdadeira se um ou ambos os argumentos forem verdadeiros.
Comentários:

O operador && representa o "AND", isto é, ambos devem ser verdadeiros. Já o || (Or)
= Um dos dois for verdadeiro.
Gabarito: Errado

96. (CESPE /TJ-AM - 2019) Após a configuração de um servidor Apache com módulo
PHP, uma forma de validar o seu funcionamento é criar uma página HTML e inserir a função phpinfo (),que mostra informações a respeito da configuração do PHP no servidor Apache.

Comentários:

Perfeito! Após a configuração de um servidor Apache com módulo PHP, uma forma de validar o seu funcionamento é criar uma página HTML e inserir a função phpinfo (), que mostra informações a respeito da configuração do PHP no servidor Apache.
Gabarito: Correto

97. (CESPE / MINISTÉRIO DA ECONOMIA - 2020) Após a configuração de um servidor Apache com módulo PHP, uma forma de validar o seu funcionamento é criar uma página HTML e inserir a função phpinfo ( ), que mostra informações a respeito da configuração do PHP no servidorApache.

Comentários:

Uma expressão Lambda é uma função anônima que você pode usar para criar delegados ou tipos de árvore de expressão.
Gabarito: Errado x
/ 121

/

98. (ADMTEC / PREFEITURA DE RIO LARGO - 2019) Analise o código abaixo e responda, a qual linguagem de programação melhor se enquadra essa sintaxe:
<?

Svl = 40;

Sv2 - 20;

if ( Svl > Sv2 ) {

echo variável ".Svl." é maior que a variável ".Sv2;
}

?>

a) ASP

b) PASCAL

c) JAVA

d) C#

e) PHP

Comentários:

Exato! Temos um código PHP.

Gabarito: Letra E

99. (QUADRIX / CRM 4 - 2021) Na linguagem PHP, a função Itrimfj é utilizada para retirar os espaços em branco no início e no final de uma string.
Comentários:

Pessoal, a função ltrim() retira espaços em branco no inicio da string.

Gabarito: Errado

100. (QUADRIX / CRM 4 - 2021) Considerando o trecho de código acima, julgue o item.

<?php
IncludeCpages/footer.php');

?>

O construtor include() está incluindo o arquivo pages/footer.php. Caso seja utilizado o construtor require() ao invés do construtor include() e o arquivo footer.php não seja encontrado no diretório pages, será apresentado um waming, indicando que o arquivo não foi encontrado, mas permitindo ainda a execução do script.
Comentários:

Pessoal, o construtor include () avisa caso tenhamos um erro, mas é somente isso. Já o require ()gera um faltai error.

Gabarito: Errado íoi. (CESPE / MPE-AP - 2021) No desenvolvimento de um sistema em PHP, o desenvolvedor precisa validar se o endereço bob@mpap.mp.br é ou não um email válido. Apartir dessa situação hipotética, assinale a opção em que o código apresentado é o correto para o desenvolvedor realizar a referida validação, tendo como referência que a variável a ser testada é $email.
a) <?php if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { echo "Invalid email format";}
else {
echo "Valid email format";} ?>

b) <?php if (!preg_match("/A[a-zA-Z-' ]*$ @./", semail)) {echo "Invalid email format";}
else {
echo "Valid email format";} ?>

c) <?php if (emailspecialchars($email)) {echo "Valid email format";} else {echo "Invalid email format";} ?>
d) <?php if (ctype_alnum (íemail)) {echo "Valid email format";} else {echo "Invalid email format";} ?>
e) <?php if (strncasecmp ($email, 7A[a-zA-Z-' ]*$ @./")) {echo "Valid email format";}
else {
echo "Invalid email format";} ?>

Comentários:

Existem várias formas de validar um e-mail em PHP, dentre elas temos a utilização doFILTER-VALIDATE-EMAIL.

Gabarito: Letra A

102. (CESPE/MEC-2015)

<?php if (isset($_REQUEST['emai1'])) {
$admin_emai1 = "admin@prova.com";

$email = $_REQUEST['emai1'];

$subject = $_REQUEST['subject'];

$comment = $_REQUEST['comment'];

/ 121

/

mail($admi n_emai1₃ "$subject", $comment ₃ "From:".

$email);

echo "Obrigado";

}

else {

<form method="post">

Email: <input name="email" type="text" /xbr />
Assunto: cinput name="subject" type="text" /xbr />
Mensagem:<br />

<textarea name="comment" rows="15"
cols="40"x/textarea><br />

<input type="submit" value="Submit" />

</form>

<?php

}

De acordo com o trecho de código apresentado, julgue o item subsequente.
O trecho de código semail = $_REQUEST['email']; indica que a variável semail recebe como parâmetro o email do administrador do portal prova.com.
Comentários:

O correto seria receber o e-mail do usuário e não do administrador. O email do adm é estático via código: $admin_email = "admin@prova.com"
Gabarito: Errado

103. (CESPE / MEC - 2015) De acordo com o trecho de código apresentado, julgue o item subsequente.
x

/ 121

/

<?php if (isset($_REQUEST[*email'])) {
$admin_email - "admin@prova.com";

$email « $_REQUEST(*email'] ;
Ssubject = $_REQUEST['subject'];

$comment = $_REQUEST['comment'];

mail($admin_emailf "$subject", $comment, "From:".

$email);

echo "Obrigado";

)

else (

?>

<form method-"post">

Email: <input name="email" type="text" /xbr />
Assunto: <input name="subject" type="text" /xbr />
Mensagem:<br />

<textarea name-"comment" rows-"15"
cols-"40"x/textarea><br />

<input type-"submit" value-"Submit" />

</form>

<?php

)

?>

O código apresentado é um exemplo de formulário para enviar email em PHP e está sintaticamente correto.
Comentários:

Perfeito! Trata-se de um formulário em PHP para envio de e-mail e está correto.

Gabarito: Correto

104. (CESPE / ANATEL - 2014) Em PHP 6, a passagem de variáveis entre páginas, por meio do uso de sessões, está limitada a informações fornecidas pelo usuário em uma página.
Comentários:

Não existe PHP 6 ou versão 6 do PHP, existe versão 5 do PHP e versão 7 do PHP.

Gabarito: Errado

105. (CESPE/ANATEL-2014) A utilização do PHPatendea mais de uma finalidade:
gerarscripts no lado servidor, que é o uso mais comum da linguagem; gerar scripts em linha de comando,caso em que é necessário apenas o interpretador; e escrever aplicações para desktop,
situação em que é necessária a extensão PHP-GTK.
Comentários:

Perfeito! A utilização do PHP atende a mais de uma finalidade: gerar scripts no lado servidor, que é o uso mais comum da linguagem; gerar scripts em linha de comando, caso em que é necessário apenas o interpretador; e escrever aplicações para desktop, situação em que é necessária a extensão PHP-GTK.
Gabarito: Correto

106. (CESPE/ANATEL - 2014) O script PHP abaixo está correto e exibe o número 9
como saída. <

?php function soma($b==5, $c==4){ return $b+$c;} echo soma(); ? >

Comentários:

O script está errado. O correto é utilizar o = para atribuição e não o == que serve para comparação.
Gabarito: Errado

107. (CESPE / ANATEL - 2014) Existem três tipos de operadores em PHP: os unários,
que operam em apenas uma sentença; os binários, que retornam o valorde acordo com a operação realizada em duas sentenças; e os ternários, que entre dois valores selecionam um, a depender de um terceiro.
Comentários:

Perfeito! No PHP temos três tipos de operadores em PHP: os unários, que operam em apenas uma sentença; os binários, que retornam o valorde acordo com a operação realizada em duas sentenças;e os ternários, que entre dois valores selecionam um, a depender de um terceiro.

Gabarito: Correto

108. (CESPE / ANATEL - 2014) No que se refere à linguagem PHP, julgue os itens subsecutivos.
$_4dias, sãripãev e $margem_são variáveis válidas no PHP.

Comentários:

Nenhum problema com as respectivas variáveis: $_4dias, sãripãev e $margem_

Gabarito: Correto

109. (CESPE / STM - 2018) O comando INCLUDE interromperá a execução do script assim que ocorrer um erro, enquanto o comando REQUIRE continuará a executar o código após o erro.
x

/ 121

/

Comentários:

Como o nome do comando sugere, o require requer que o arquivo seja incluso. Já o include não faz essa exigência.
Gabarito: Errado no. (CESPE / SEDF - 2017) AngularJS, Ajax, JQuery, Less e PHP são tecnologias para desenvolvimento web front-end.
Comentários:

Pessoal, conforme vimos PHP é back-end e server side.

Gabarito: Errado

111. (CESPE / TCE-PA - 2016) As instruções echo e print, do PHP 5, são utilizadas para viabilizar a saída de dados na tela.
Comentários:

Exatamente! As instruções echo e print, do PHP 5, são utilizadas para viabilizar a saída de dados na tela.
Gabarito: Correto

112. (CESPE / TCE-PA - 2016) Em PHP 5, a função count é utilizada para retornar o número de elementos de um array.
Comentários:

Perfeito! Em PHP 5, a função count é utilizada para retornar o número de elementos de um array.

Gabarito: Correto

113. (CESPE / MPU - 2013) O código da linguagem PHP é interpretado em um servidor web,enquanto o código da linguagem Java é interpretado pela própria máquina.

Comentários:

Pessoal, ambos são interpretados do lado servidor.

Gabarito: Errado

114. (CESPE /TRT10 - 2013) No código abaixo, o teste da condição retornará verdadeiro.

<?php if (2 === 2.0)
echo "2 é igual a 2.0";

?>

Comentários:

Pessoal, quando comparamos com === comparamos os valores e os tipos de dados. O "2"
é do tipo integer enquanto que o "2.0" é do tipo float. Logo, retorna false.
Gabarito: Errado

115. (CESPE /TRT10 - 2013) Ao ser corretamente executado, o trecho de código abaixo avalia se o conteúdo da variável van é diferente do conteúdo de var2; caso a avaliação seja verdadeira,será emitida mensagem de que os valores são diferentes.

<?php if ($van <> $var2)
echo "$van é diferente de $var2";

?>

Comentários:

Perfeito! O trecho de código abaixo avalia se o conteúdo da variável van é diferente do conteúdo de var2; caso a avaliação seja verdadeira, será emitida mensagem de que os valores são diferentes.
Gabarito: Correto

116. (CESPE / TCDF - 2014) Zend Framework é uma biblioteca PHP para desenvolvedores que permite utilizar ferramentas controladas de acesso às informações de transação, de modo a padronizar-se o processo de desenvolvimento para que a interface seja estruturada por tags personalizadas.
Comentários:

ZEND é um framework e não uma biblioteca PHP.

Gabarito: Errado

117. (CESPE / EBSERH - 2018) Julgue o item que se segue a respeito das características da linguagem PHP e de compiladores.
O código PHP

< ?php

$txt "Viva1;

print H $txt a vida \nM;
print 1 $txt a vida *;

?>

apresenta o resultado a seguir.

Viva a vida

$txt a vida

Comentários:

Perfeito! Ao ser compilado o referido código, apresentará Viva a vida na primeira linha e $txt a vida na segunda linha.
Gabarito: Errado

118. (CESPE / EBSERH - 2018) Na linguagem PHP, o comando explode() permite descarregar os buffers de saída de qualquer backend que o PHP esteja usando, como, por exemplo,um CGI
ou um servidor web.

Comentários:

O comando explode () divide uma string principal em partes menores com base em um caractere divisor, que pode ser um ponto e vírgula ou qualquer outro caractere ou string.
Gabarito: Errado

119. (CESPE / EBSERH - 2018) PHP consiste de uma linguagem compilada para código nativo e gera um bytecode que é interpretado por uma máquina virtual implantada em cada cliente onde o código será executado.
Comentários:

O PHP conforme vimos é uma linguagem interpretada e não uma linguagem compilada.

Gabarito: Errado

120. (CESPE / EBSERH - 2018) O comando a seguir concatena corretamente caracteres em
PHP.

$final = "abc". "efg";

Comentários:

Exato! Para concatenar, utiliza-se o operador (.) Logo, o comando sfinal = "abc".
"efg"; concatena corretamente.
Gabarito: Correto

121. (QUADRIX/ CRBM 4 - 2021) Considerando o trecho de código acima, julgue o item.

<?php
IncludeCpages/footer.php');

?>

O construtor include() está incluindo o arquivo pages/footer.php. Caso seja utilizado o construtor require() ao invés do construtor include() e o arquivo footer.php não seja encontrado no diretório pages, será apresentado um waming, indicando que o arquivo não foi encontrado,mas permitindo ainda a execução do script.

Comentários:

A diferença aqui é que o require() vai gerarem erro fatal, enquanto o include vai só avisar caso exista um erro.
Gabarito: Errado

122. (QUADRIX / CRBM 4 - 2021) Na linguagem PHP, a função Itrim() é utilizada para retirar os espaços em branco no início e no final de uma string.
Comentários:

Pessoal, a função Itrim () é utilizada para retirar os espaços em branco somente do início da string e não do final.
Gabarito: Errado

123. (QUADRIX / CRQ 4 Região - 2018) Em programas PHP, os comentários podem ser usados utilizando-se os caracteres "#", "//" ou 7* */", sendo que estes últimos delimitam textos que podem se estender em mais de uma linha.
Comentários:

/ 121

/

Perfeito! Nos programas PHP, os comentários podem ser usados utilizando-se os caracteres
"#",
"II" ou "I* */", sendo que estes últimos delimitam textos que podem se estender em mais de uma linha.
Gabarito: Correto

124. (QUADRIX / CRQ 4 Região - 2018) A linguagem PHP é baseada emscr/ptde uso livre(open source) e adequada para o desenvolvimento web, pois pode ser embutida em códigos
HTML.

Comentários:

Perfeito! A linguagem PHP é baseada emscr/ptde uso livre (open source) e adequada para o desenvolvimento web, pois pode ser embutida em códigos HTML.
Gabarito: Correto

125. (QUADRIX / CRN 9 - 2018) Uma das utilidades do safe_mode é a proteção dos scripts PHPcontra acessos remotos.

Comentários:

Perfeito! A proteção dos scriptos é uma das utilidades do fase_mode nos scripts PHP
contra acessos remotos.
Gabarito: Errado

126. (QUADRIX / CRN 9 - 2018) A PHP é considerada como uma linguagem de programação totalmente insegura, visto que ela não pode ser utilizada em aplicações que estejam relacionadas a informações relevantes, como as confidenciais e as bancárias.
Comentários:

Tudo errado. PHP é considerada como uma linguagem de programação totalmente segura,
visto que ela pode ser utilizada em aplicações que estejam relacionadas a informações relevantes, como as confidenciais e as bancárias.
Gabarito: Errado

127. (QUADRIX / CRN 9 - 2018) Ao desabilitar a diretiva register_globals, a
PHP somente interpretará variáveis inicializadas.
Comentários:

/ 121

/

Exato! Essa é o objetivo por retirar (desabilitar) o register_globals, para que o PHP interprete somente variáveis inicializadas.
Gabarito: Correto

128. (QUADRIX / CRN 9 - 2018) O ponto e vírgula, na linguagem de programação PHP, é usado no término de uma declaração.
Comentários:

Perfeito! Conforme vimos o ponto e vírgula, na linguagem de programação PHP,
é usado no término de uma declaração.
Gabarito: Correto

129. (QUADRIX / CRO-AC- 2019) No PHP, para cada necessidade, deve ser criado um procedimento, já que os procedimentos não podem ser reaproveitados em outras situações.
Comentários:

Obviamente que pode! Existe o reaproveitamento.

Gabarito: Errado

130. (QUADRIX / CRESC-SC- 2019) O código $Cad_Especialidade['Pesq Area'] =
'Social', em
PHP, representa o armazenamento do elemento ('Social') em uma variável do tipo array,
em que $Cad_Especialidade é a chave de pesquisa associada ao elemento armazenado.
Comentários:

Pessoal, $Cad_Especialidade é o nome do array; logo, a chave do array, de pesquisa, é o nome 'Pesq
Area'.

Gabarito: Errado

131. (QUADRIX / CRESC-SC- 2019) Na declaração de uma função, na linguagem
PHP, as variáveis enviadas por referência devem ser identificadas pelo símbolo &
Comentários:

Perfeito! Na declaração de uma função, na linguagem PHP, as variáveis enviadas por referência devem ser identificadas pelo símbolo &.
Gabarito: Correto

132. (QUADRIX / CRO-AC- 2019) Uma função no PHP, mesmo sendo uma função isolada, tem como característica principal a retenção de informações, ou seja, a função armazena informações para serem usadas no futuro.
Comentários:

Uma função em PHP é um trecho de código que pode ser chamado (invocado) de qualquer parte do código para executar uma tarefa qualquer e retornar algum valor. Ou seja,você pode chamar quantas vezes forem necessárias a função. Você pode passar zero ou mais parâmetros para uma função, e poderá retornar apenas um valor.
Gabarito: Errado

133. (QUADRIX / CRO-AC- 2019) No PHP, para cada necessidade, deve ser criado um procedimento, já que os procedimentos não podem ser reaproveitados em outras situações.
Comentários:

No PHP, por definição, não existem produceres, existem functions.

Gabarito: Errado

134. (QUADRIX / CRM-PR - 2019) Considerando o programa abaixo, julgue o próximo item.

<!D0CTYPE html>

<html>

<body>

<?php for ($x = 0; $x <= 10; $x++) {
echo "The number is: $x <br>";

}

?>

</body>

</html>

A saída do programa resultará em uma linha no navegador do cliente, contendo a frase:
The number is: 0123 4 5 678 910.
Comentários:

A saída será:

/ 121

/

The number is: o
The number is: 1
The number is: 2
The number is: 3

Gabarito: Errado

135. (QUADRIX / CRM-PR - 2019) Considerando o programa abaixo, julgue o próximo item.

<!D0CTYPE html>

<html>

<body>

<?php for ($x = 0; $x <= 10; $x++) {
echo "The number is: $x <br>";

}

?>

</body>

</html>

O comando de repetição for incrementa a variável x com valores de 0 a 10.

Comentários:

Perfeito! O comando de repetição for incrementa a variável x com valores de o a 10.

Gabarito: Correto

136. (QUADRIX / CRM-PR - 2019) Considerando o programa abaixo, julgue o próximo item.

<!D0CTYPE html>

<html>

<body>

<?php for ($x = 0; $x <= 10; $x++) {
echo "The number is: $x <br>";

}

?>

</body>

</html>

O programa deve ser executado em um servidor web com PHP instalado e seu resultado aparecerá no browser do cliente que o acessar.
00 SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital)

Comentários:

Perfeito! O programa deve ser executado em um servidor web com PHP instalado e seu resultado aparecerá no browser do cliente que o acessar.
Gabarito: Correto

137. (QUADRIX/CRM-PR - 2016) Considerando um programa em PHP com os seguintes valores nas variáveis: a=6 b=5 c=4- Qual será a saída do trecho de código abaixo:
<?php if($a<$b){
echo "Marte";

} elseíf ($b > $c) {
echo "Terra";

} elseif ($b = $c) {

echo "Júpiter / Vénus";

} else {

echo "Mercúrio";

}

?>

a) MARTE.

b) TERRA.

c) JÚPITER.

d) VÉNUS.

e) MERCÚRIO.

Comentários:

Somente um dos blocos será executado, ou seja, somente o bloco verdadeiro, ou seja, b
(6) é maior que c (4), logo a saída será: TERRA.
Gabarito: Letra B

138. (QUADRIX / CFP - 2016) Sobre PHP é correto afirmar que:

a) as variáveis começam com um sinal #, seguido do nome da variável.

b) possui comandos obrigatórios para declarar variáveis antes que elas recebam um valor.

c) o operador de concatenação (.) é usado para juntar dois valores string.

d) não converte automaticamente a variável para o tipo de dado correto, dependendo do valor recebido.
e) tem apenas dois diferentes escopos de variáveis: local e global.

Comentários:

Sobre PHP, é correto afirmar que o operador de concatenação (.) é usado para juntar dois valores string.
Gabarito: Letra C

139. (FCC/TRE-BA-2015) Para conectar uma aplicação PHP5 orientada a objetos aos principais servidores de banco de dados, abstraindo o acesso de forma que, para se mudar de servidor,seja necessário alterar apenas a string de conexão, deve-se utilizar a biblioteca:

a) PHPDbc b) Detector c) Whoops d) PDO
e) ObjectODBC

Comentários:

Pessoal, para realizar a conexão de uma aplicação PHP5 orientada a objetos aos principais servidores de banco de dados, basta utilizar a biblioteca PDO. Exemplo:
$con = new PDO("mysql:host=localhost;dbname=exercicio", "root", "senha");

Lembre-se: A Biblioteca PDO fornece uma camada de abstração em relação a conexão com o banco de dados, considerando que PDO efetua conexão com diversos banco de dados,modificando apenas a string de conexão.
Gabarito: Letra D

140. (FCC / TRE-RR - 2015) Considere o seguinte script encontrado em uma página PHP.

<?php

$idade » array("Paulo">"40" , "Pedro"«>"62"t

**Ana" = >"43", "Marcos"«>"18") ;

arsort($idade);

foreach($idade as $x => $x_valor) {
echo $x . " " . $x_valor . * *;

}

?>

Ao executar o script será exibido na página:

a) Ana = 43 Marcos = 18 Paulo = 40 Pedro = 62

b) Marcos = 18 Paulo = 40 Ana = 43 Pedro = 62

c) o = 62 1 = 43 2 = 40 3 = 18

d) Pedro = 62 Paulo = 40 Marcos = 18 Ana = 43

e) Pedro = 62 Ana = 43 Paulo = 40 Marcos = 18

Comentários:

Quando executamos o referido script teremos na saída o valor atribuído a Pedro (62),
a Ana (43), a
Paulo (40) e a Marcos (18) com ordenação de valor (arsort) do maior para o menor.

Gabarito: Letra E

/ 121

/

LISTA DE QUESTõES - DIVERSAS BANCAS

í. (FCC -TST - 2012) Considere a linguagem de programação PHP e seus operadores. A execução da sentença:
a) (A != B) retorna falso (false), considerando as variáveis A e B inicializadas com os valores 3 e
6,
respectivamente.

b) (A %- B) atribui o valor 3 (três) para a variável A, considerando as variáveis A
e B inicializadas com os valores 10 e 3, respectivamente.
c) (A . = B) concatena o conteúdo das variáveis A e B e armazena o conteúdo em A.

d) !(A -- B) retorna falso (false), considerando as variáveis A e B inicializadas com os valores 3 e6, respectivamente.

e) (A = = = B) compara somente os tipos das variáveis A e B.

2. (FCC / TST - 2012) Considere o programa abaixo escrito na linguagem PHP:

$v = array(10, 50, 2, 15, 35);

for($i=0;$i <count($v)-1;$i++){
if($v[$i] > $v[$i+l]){

$temp = $v[$i+1];

$v[$i+l] = $v[$i];

$v[$i] = $temp;

$í=-i;

}

}

for($i=0;$i<=count($v);$i ++){
echo " ".$v[$i];

}

O resultado a ser informado ao usuário após a execução do programa acima é:

a) 100 70 30 20 4

b) 50 35 1510 2

c) 4 20 30 70 100

d) 2 10 15 35 50

e) 10 50 2 15 35

3. (FCC / MPE-AP - 2012) Analise os exemplos de criação de array em PHP.
I.

$ idade = array("Paulo"=>32, "Pedro"=>3O, "Ana"=>34);

II.

$familia = array("Jorge"=>array("Angela","Iracema",
"Bia"),"Pedro"=>array("Ana"));

III.

$nome[o] ="Paulo";

$nome[i] ="Pedro";

$nome[2] ="Ana";

IV.

$idade['Paulo'] = "32";

$idade['Pedro'] = "30";

$idade['Ana'] = "34";

Representam exemplos corretos de criação de array os itens a) I, II, III e IV.
b) III e IV, apenas.

c) I e II, apenas.

d) I, III e IV, apenas.

e) II, III e IV, apenas.

4. (FCC / MPE-AP - 2012) Marcos está desenvolvendo uma aplicação web PHP
utilizando o
WAMPServer. Como está utilizando um banco de dados MySQL, escolheu uma função para enviar uma consulta ou comando SQL (por exemplo, os comandos select, insert ou delete)para o banco de dados ativo. A função correta escolhida foi:
a) mysql_fetch_array.

b) mysqLquery.

c) mysql_update.

d) mysql_execute_stmt.

e) mysql_stmt_start.

5. (FCC / TRE-SP - 2012) Na linguagem PHP é possível utilizar o protocolo SOAP por meio de classes desenvolvidas especificamente para esse protocolo. A classe que fornece acesso cliente aos servidores SOAP é chamada de:
a) PHPAccess.

b) WSDLClient.

c) SoapConnect.

d) SoapClient.

e) SoapAccess.

6. (FCC / TRE-SP - 2012) A linguagem PHP permite a instalação de extensões que podem aumentar sua gama de funcionalidades. Uma das funcionalidades extras que podem ser adicionadas se refere a manipulação de arquivos XML. A extensão que possui várias classes que podem ser instanciadas para a leitura e gravação de arquivos XML é chamada:
a) DOM.

b) XML-RPC.

c) Ctype.

d) SCA.

e) YAZ.

7. (FCC / TRE-AP - 2011) Em relação a PHP e JSP é correto afirmar:

a) Em JSP o conceito de classes e objetos não leva em conta os princípios de proteção de dados tanto nas propriedades quanto nos métodos.
b) A flexibilidade do PHP permite-lhe que a avaliação de uma variável seja o nome de outra variável ou mesmo de uma função.
c) Em PHP os objetos possuem métodos e propriedades privados e devem ser instanciados para serem usados.
d) Em JSP pode-se chamar o construtor do objeto pai em qualquer parte do código e não há tratamento de exceções nos métodos nativos.
e) Em JSP os objetos são destruídos ao final da execução do script.

8. (FCC / TRT14 - 2011) Na PHP 5, é uma função usada para a busca por um padrão em um nome de arquivo:
a) fscanf.

b) fpassthru.

c) fseek.
djfputs.

e) fnmatch.

9. (CESPE / MPE-RN -2010) Na linguagem PHP, a função fputs:

a) busca por um padrão em um nome de arquivo.

b) é um nome alternativo para a função fwrite.

c) interpreta o conteúdo de um arquivo de acordo com um determinado formato.

d) cria um link físico.

e) posiciona o ponteiro em um arquivo.

/ 121

/

io.(FCC/TCE-SP-2Oio) NÃO se trata de uma característica do PHP:

a) portábil.

b) baseado no servidor.

c) gratuito e com código aberto.

d) embutido no HTML.

e) baseado no cliente.

n.(CESPE /TRE-BA- 2015) Para o recebimento dos dados de um formulário HTML, enviados por meio do método GET, para uma página PHP, deve-se utilizar:
a) $_GET["nome_text"]

b) $GET["nome_text"]

c) _GET$["nome_text"]

d) _$GET["nome_text"]

e) _$_GET["nome_text"]

12. (CESPE / CPRM -2013) A validação de uma data em PHP pode ser realizada pela função:

a) getdate.

b) checkdate.

c) setdate.

d) isdate.

e) mktime.

13. (CESPE / TRE-MS - 2015) Em uma função, escrita na linguagem de programação PHP, a passagem de parâmetros por referência é feita por meio da utilização do caractere:
a) !

b) °/o c) &
d) @

e) ?

iZj.(CESPE /TRE-MT-2015) Um servidor Web que interpreta páginas em PHP é denominado:

a) IIS.

b) JSTL.

c) NetBeans.

d) Apache.

e) Netscape.

/ 121

/

15. (CESGRANRIO / PETROBRÁS - 2015) O envio de e-mails, por meio de programas PHP, é responsabilidade da função:
a) email.

b) mail.

c) &mail.

d) ismail.

e) &email.

16. (CESPE / TJ-RO - 2015) Em PHP,

a) os operadores aritméticos restringem-se a soma, subtração, multiplicação e divisão.

b) as variáveis necessitam da sua definição de tipo no início do programa.

c) operações aritméticas entre variáveis numéricas e variáveis alfanuméricas, por exemplo 6divido por 3, resultam em mensagem de erro.

d) o único conjunto de comandos condicionais utilizado é o if...endif.

e) as variáveis são definidas com o símbolo antes do nome da variável.

17. (FCC / MPE-MA- 2015) Em PHP, uma variável NÃO pode receber o nome inválido:

a) $cod_empregado b) íbaseisalario c) $data-nascimento d) $depto_i_nome e) $descricao
18. (FCC / TJ-PE - 2015) NÃO é uma afirmativa correta sobre a função PHP:

a) session_start() = Inicializa os dados da sessão.

b) session_destroy() = Cancela o registro de uma variável global da sessão.

c) session_unset() = Libera todas as variáveis da sessão.

d) session_commit() = O mesmo que session_write_ close().

e) session_write_close() = Escreve os dados da sessão e a encerra.

19. (FCC / TRT19 - 2015) Utilizando a data 01/07/2009 e o comando PHP:
echo $data = date("d/m/y");

a data será exibida no formato a) 01/07/09.
b) 01/07/2009.

c) oi/Jul/09.

d) oi/Jul/2009.

e) Wed, oi/Jul/2009

20. (FEPESE / JUCESC - 2013) A função fopen ( ), utilizada em um script PHP, que recebe o argumento de modo igual a "a+", abre um arquivo existente para:
a) leitura e gravação e coloca o ponteiro no final do arquivo, depois de todos os dados.

b) leitura e gravação, deleta todo o conteúdo e coloca o ponteiro no início do arquivo.

c) leitura e gravação e coloca o ponteiro no início do arquivo, antes de qualquer dado.

d) somente gravação e coloca o ponteiro no final do arquivo, depois de todos os dados.

e) somente gravação, deleta todo o conteúdo e coloca o ponteiro no início do arquivo.

21. (MPE-RS / MPE-RS - 2015) Um conteúdo será considerado como um código PHP pelo interpretador se estiver dentro do par de tags:
a) <php> </php>

b) <?php ?>

c) <?php php?>

d) <?> </?>

e) <script language = PHP> ?>

22. (FCC/ TRT 23 - 2015) A expressão PHP $x && $y representa um exemplo de utilização de operador:
a) de atribuição.

b) aritmético.

c) lógico.

d) de comparação.

e) de incremento e decremento.

23. (IBFC - Prefeitura de divinópolis - 2018) Dado o loop PHP:
for ($x = o; $x <= "5"; $x++)

A variável $x assumirá os valores:

a) 1, 3 e 5.

b) o, 1, 2, 3 e 4.

c) 1, 2, 3, 4e5-

d) o, 2 e 4.

e) o, 1, 2, 3, 4 e 5.

24.(FGV / BANESTES - 2021) HTML, DHTML, JavaScript e PHP são linguagens utilizadas no desenvolvimento de sites da World Wide Web. A seu respeito é correto afirmar que:
/ 121

/

a) o código de uma aplicação JavaScript deve ser interpretado pelo servidor HTTP ao passo que o código de uma aplicação PHP deve ser interpretado pelo cliente HTTP.
b) o código de uma aplicação JavaScript deve ser interpretado pelo cliente HTTP ao passo que o código de uma aplicação PHP deve ser interpretado pelo servidor HTTP.
c) tanto o código de uma aplicação JavaScript como o código de uma aplicação PHP
devem ser executados pelo cliente HTTP.
d) tanto o código de uma aplicação JavaScript como o código de uma aplicação PHP
devem ser executados pelo servidor HTTP.
e) o código de uma página HTML deve ser interpretado pelo cliente HTTP ao passo que o código de uma página DHTML deve ser interpretado pelo servidor HTTP.
25. (IF-RJ / BIO-RIO - 2015) Considere o seguinte script encontrado em uma página PHP.

<?php

$idade = array("Paulo"=>"4o", "Pedro"=>"62", "Ana"=>"zh3", "Marcos"=>"i8");
arsort($idade);

foreach($idade as $x => $x_valor) {
echo $x ." = ". $x_valor."

}

?>

Ao executar o script será exibido na página:

a) Ana = 43 Marcos = 18 Paulo = 40 Pedro = 62

b) Marcos = 18 Paulo = 40 Ana = 43 Pedro = 62

c) o = 62 1 = 43 2 = 40 3 = 18

d) Pedro = 62 Paulo = 40 Marcos = 18 Ana = 43

e) Pedro = 62 Ana = 43 Paulo = 40 Marcos = 18

26.(IF-RJ / BIO-RIO - 2015) Considere o código PHP a seguir:

/ 121

/

<?php

£ nomes =array ("Zen ai de"," M a rcelo"," B iu n o");

I

Sclength=count($ nomes};

fo r( Jx=O; length; $ x-*-+)

{

echo $ nomes [$x]:
echo

}

?>

O comando que deve ser utilizado na lacuna I para colocar os nomes em ordem alfabética crescente é:
a) order($nomes) ascending;

b) rsort($nomes);

c) index($nomes) order by asc;

d) sort($nomes);

e) krsort($nomes);

27. (IF-RJ / BIO-RIO - 2015) Considere um formulário criado na página de site desenvolvido com
PHP para permitir que os usuários façam upload de arquivos:

«fornfi action="upload.php" mettiod="post' enctype="muttipart/fonn-data">

<label fo r="file"> F ile name:<Jlabel >

<inputtype-üle"name="file" id="file7><br/>

<inputtype="submit" value="Fazer Upload"/*

No arquivo upload.php, as instruções utilizadas para se obter o nome e o tipo do arquivo, caso não ocorra erro são, respectivamente,
a) $_DUMP["file"] e $_DUMP ["type"]

b) $_FILES["file"]["name"] e $_FILES["file"]["type"]

c) $_POST["file"] e $_ POST["type"]

d) $_FILES["file"] e $_FILES ["type"]

e) $_REQUEST["file"]["name"] e $_REQUEST["file"]["type"]

28.(TJ-PE / IBFC - 2017) Para acessar bases de dados MySQL, por meio do PHP, é necessário antes estabelecer uma conexão. Para isso, deve ser utilizado o comando:
a) mysqL&connect ou mysql_&pconnect b) mysql_&&connect ou mysql_&&pconnect
/ 121

/

c) mysql&_connect ou mysql&_pconnect d) mysql&&_connect ou mysql&&_pconnect e) mysql_connect ou mysql_pconnect
29. (FCC / TCE-SP - 2010) Uma função PHP em execução terminará imediatamente,
retornando seu argumento como valor, se for chamada, na função, a instrução:
a) this b) null c) return d) this.value e) this.return
30. (FCC / TRT 3 - 2009) Dados os operadores "e" lógico: "and", "&&" e e os operadores "ou"lógico: "or", "||" e "|", a ordem de precedência no momento do PHP avaliar as expressões será na sequência:
a) and, &&, &, or, || e |.

b) or, II, I, and, && e &.

c) and, or, &&, ||, & e |.

d) or, and, ||, &&, | e &.

e) &, &&, and, |, || e or.

31. (FCC / TRF 3 - 2016) Cookie é um arquivo texto que pode ser armazenado no computador do usuário, normalmente com informações de sua navegação no site, para ser recuperado posteriormente pelo servidor. Em PHP, um cookie criado pela instrução setcookie("ck","abcde",
time() + 3600); poderá ser recuperado utilizando a instrução:

a) $_ISSET["ck"]

b) load_cookie ("ck")

c) get_cookie("ck")

d) $_GETCOOKIE["ck"]

e) $_COOKIE["ck"]

32. (FGV/TJ-PI - 2015) Analise o código PHP mostrado a seguir.

<?php function f($arg)
$argoi = 343 + 20/2 + 911;

$argo2 = 38 - (5 * 11);
sargRetorno = $argoi - $argo2;

$argoi = 343;

$argo2 - 38;
f($argoi);
echo $argoi;

A saída produzida pela execução desse código é:

a) -17

b) 38

c) 343

d) 1264

e) 1281

33. (FGV/TJ-PI - 2015) Uma String recebida do campo nome de um formulário HTML
enviado por meio do método POST para um site deve ser codificada para UTF-8. A forma correta de realizar essa operação, utilizando a linguagem PHP, é:
a) snome - utf8_encode( $_POST['nome'])

b) snome: utf8

c) decode(snome)

d) snome - string( $_POST['nome'])

e) parseHTML($nome, utf8( $_POST['nome'])

34. (1 ES ES / IFC-SC - 2015) Em um código PHP 5.6.2, qual das alternativas a seguir atribuiria o valor10 à variável svar?

a) svar = (100 > 10 :100 ? 10);

b) svar = (100 > 10 ? 10 :100);

c) svar = (100 > 10 :10 ? 100);

d) svar = (100 > 10 ? 100 :10);

35. (FGV/ TJ-PI - 2015) Analise o código PHP mostrado a seguir.

<?php

$lista = range(0,20);

for (Si = 0; $i <=20; $i++)

{

$pos- randfO^O};

$aiiK = $lista[$ij;

$lfcta[$I] = $lista($po5];

$ lista[Ípos] = $auX;

}

Ao final da execução desse código, os valores na variável slista estarão:

a) ordenados de forma crescente, segundo o método de ordenação Quicksort;

b) ordenados de forma crescente, segundo o método de ordenação em bolha;

c) embaralhados, não sendo possível prever a ordem dos valores;

d) removidos da variável, devido a um erro no código;

e) duplicados, devido a um erro no código.

36. (CESPE / TRE-BA - 2017) A respeito da declaração de variáveis na linguagem de programaçãoPHP, assinale a opção correta.

a) Uma variável é composta pelo nome dessa variável seguido do sinal $ no final.

b) Um nome de variável pode começar com um número.

c) Os tipos de variáveis existentes são somente local e global.

d) Diferentemente das linguagens em que o programador deve declarar o nome e o tipo da variável antes de usá-la, o PHP converte automaticamente a variável para o tipo de dado correto.
e) Os nomes das variáveis no PHP não diferenciam maiúsculas de minúsculas, ou seja,
eles são case insentivive.
37. (CESPE / ABIN - 2010) A habilitação da característica de thread safety no painel de informações do ambiente de runtime PHP depende fundamentalmente do suporte que o sistema operacional oferta, e não, das características do zend engine.
/ 121

/

38.(CESPE / ABIN - 2010) Considere que determinada aplicação web a ser desenvolvida em
PHP
deva ser integrada aos sistemas de controle de acesso já presentes nos ambientes de desenvolvimento e produção da organização. Nesse caso, se esses ambientes forem embasados em Kerberos ou em RADIUS (remote authentication dial in user service), o programador poderá obter êxito na integração por meio do uso de extensões providas pela biblioteca PECL(PHP
extension community library), tais como os packages KADM5 e RADIUS.

3g.(CESPE / ABIN - 2010) O arquivo de configuração do PHP, de nome php.íni, será lido apenas no momento da inicialização (startup) do servidor HTTP associado ao referido IDE, que, no caso específico, é o Apache 2.2.11.
40. (CESPE / ABIN - 2010) Para que possa depurar os scripts PHP que construirá, o programador não necessita instalar depuradores externos, uma vez que a distribuição padrão de PHPvem acompanhada de depurador.
41. (CESPE / ABIN - 2010) O acesso otimizado ao sistema gerenciador de banco de dados (SGBD)em uso nos ambientes de desenvolvimento e produção da organização pode ser obtido por meio da extensão PDO (PHP data objects), desde que seja habilitado o driver PDO específico do SGBDem uso, uma vez que a PDO não provê abstração completa do banco de dados, mas apenas uma camada de abstração para acesso aos dados, que não reescreve SQL nem emula funcionalidades de um SGBD.
42. (CESPE / ABIN - 2010) Caso o programador deseje criar, gerenciar e distribuir internamente à organização um ou mais packages que contenham módulos ou extensões porele desenvolvidos,é correto o uso da técnica de channels, que é embasada em arquitetura orientada a serviços(SOA), por meio da utilização de XML e REST (representational state transfer).

43. (CESPE / ABIN - 2010) Para instalar extensões do repositório PEAR (PHP
extension and application repository), é correto o uso do Pyrus, uma versão refatorada do instaladorPEAR,
capaz de prover maior segurança aos processos, permitindo o gerenciamento e a distribuição de packages.
44. (CESPE / ABIN - 2010) Ao se escreverem scripts PHP, deve-se empregar indentação com espaços em branco, sem uso de tabs; atribuições em arrays devem ser alinhadas;comentários podem adotar o estilo C ou estilo C++, mas comentários em estilo PERL devem ser evitados.
45. (CESPE / ABIN - 2010) Scripts de teste funcional devem conter a extensão .phpt,
conforme prescreve o padrão de distribuição de módulos PHP; os diversos artefatos de teste relacionados a um módulo desenvolvido devem ser armazenados em subdiretório de nome tests,dentro do diretório do módulo ou package; dados de configuração específicos do ambiente de teste do desenvolvedor devem ser armazenados no arquivo de nome config.php.dist.
46. (CESPE / ABIN - 2010) Se o pedido http://localhost:8o8o/teste.php?nome=joao for aplicado de forma bem sucedida ao script apresentado a seguir, então, após o processamento do pedido, a saída de dados para o usuário deverá conter a string joao e um arquivo de nome joao.txt,contendo a palavra joao, existirá no computador onde se encontra o serviço HTTP
associado ao referido pedido.
<h tml Xbody >< ?php

$ponteiro fopen ( $_REQUEST['nome'].'.txt');
fwrite($ponteiro,$nome);

fclose($ponteiro);

echo $_GET['nome'];

?></body></html>

47.(CESPE / ABIN - 2010) Sabendo-se que a função array_multisort é capaz de ordenar múltiplos arrays na plataforma PHP, então a saída de dados gerada pela execução bem sucedida do script abaixo produzirá o resultado indicado em seguida.
<?php

$arl * array(10, 100, 100, 0) ;

$ar2 * array(l, 3, 2, 4);
array_multisort ($arl, $ar2);
va r_dump ($a rl);

va r_dunip ($a r2 );

?>

48.(CESPE / ABIN - 2010) A execução bem sucedida do script apresentado abaixo produz como saída o valor 900.
< h tml >< bo dy > < ?ph p

$num=14; $deslocado $num >> 2;

$scrrHF$des locado; $valorl=10; $valor2®20; $valor3=30;

$soma+«$valorl+$valor2;$soma*- $valor3;

$soma% = 100;
echo $soma;

?></body></html>

4g.(CESPE / ABIN - 2010) Se o pedido http://localhost/teste.php?nome=joao for aplicado de forma bem sucedida ao script apresentado abaixo, então a saída de dados deverá conter a string Você deve preencher os campos. É correto afirmar, ainda, que uma conexão de socket foi estabelecida entre dois processos que se executam no mesmo computador onde se encontra o serviço HTTP associado ao referido pedido, sendo uma extremidade da conexão associada à porta 80 e a outra, a uma porta cujo número não se pode determinar pelas informações apresentadas.
/ 121

/

<h tml >< bo dy > < ? ph p if (empty ($nome) OR empty ($email)) {echo " Você deve preencher os campos";

} else {

echo "olá $nome";

}

?></body></html>

50. (CESPE / ABIN - 2010) Sabendo-se que a função natsort() opera com o conceito de ordenação natural, na qual as strings alfanuméricas são ordenadas da forma que um ser humano ordenaria,enquanto a função asort() opera com o conceito de ordenação classicamente usado em algoritmos de ordenação de strings, na ciência da computação, então a execução bem sucedida do script PHP apresentado abaixo produzirá, na saída, a primeira ocorrência da string imgi2.png antes da primeira ocorrência da string img2.png e a segunda ocorrência da string imgi2.png depois da segunda ocorrência da string img2.png.
<?php

$A1~ $array2" array("imgl2.png", "imglO.png",
"img2.png", "inigl .png") ;

asort($A1);
print_r($Al);

natsort($array2);
print_r($array2);

?>

51. (CESPE / ABIN - 2010) Uma sessão PHP é criada ou recuperada automaticamente durante a execução do script.
52. (CESPE / ABIN - 2010) A senha do usuário que está no banco de dados não foi criptografada com um hash, fato que torna a aplicação vulnerável a ataques de dicionário.
53. (CESPE / ABIN - 2010) O banco de dados MySQL é usado pelo script, mas a conexão com o banco deveria ter sido encerrada ou devolvida ao pool ao final do script,fato que não se concretiza.
54. (CESPE / ABIN - 2010) O pedido HTTP que pode ser atendido por esse script não poderá conter cookies de nomes nu e su, além de estar sujeito a ataques de SQL injection.
55. (CESPE / ABIN - 2010) Os softwares de servidores web, ao aderirem à arquitetura de sistemas operacionais, empregam modelo de memória virtual, que atua como um cache de memória e contém parte das instruções e dados executados por um script em determinado instante de tempo. Assim, o script não precisa estar armazenado simultaneamente na memória principal e no disco; com isso, a memória total disponível para um script ou programa pode exceder o tamanho da memória principal do sistema.
56. (CESPE/ ABIN-2010) O formato JSON (javascript object notatíon) permite representar objetos e classes como estruturas de dados e arrays associativos, sendo possível seu uso em combinação com Ajax e PHP, por meio de bibliotecas diversas, como DOJO.
57. (CESPE / ABIN - 2010) Arrays associativos, usados em PHP e em outras linguagens de script,podem ser implementados de forma eficiente, do ponto de vista de consumo de memória,
por meio do uso de tabelas de dispersão. Para garantir eficiência, essas tabelas precisam ser totalmente livres de colisão, tal que, na implementação de métodos de busca, as pesquisas sejam executadas em tempo constante, independentemente do valor pesquisado.
58. (CESPE / ABIN - 2010) Estruturas de dados padronizadas, como listas ligadas duplamente encadeadas, pilhas, filas, filas de prioridade e arrays numéricos de tamanho fixo, são disponíveis em PHP por meio da extensão SPL (standard PHP library).
59-(CESPE / ABIN-2010) Algoritmos recursivos normal mente têm menor tempo de resposta que seus equivalentes iterativos, mas as linguagens PHP e Javascript, por serem linguagens de script,não permitem nem necessitam de recursividade.

6o.(FUND / CIG - 2020) Qual dos trechos de código abaixo, em linguagem PHP 5.5, é executado sem erros e, adicionalmente, pode ser considerado o mais seguro para fazer uma consulta em uma tabela de usuários em um banco de dados relacional PostgreSQL?
a) $nome = "João"; $sql = "SELECT nome, sobrenome, senha FROM tb_usuario
WHERE
nome=$nome;"; $resultado = pg_query($conn, $sql);

b) $nome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, senha FROM
tb_usuario
WHERE nome='$nome;"'; sresultado - pg_secure_query($conn, $sql);

c) ínome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, senha FROM
tb_usuario
WHERE nome=$i;"; $resultado - pg_query_params($conn, $sql, array($nome));

d) ínome = $_GET["nome"]; $sql = "SELECT nome, sobrenome,
senha WHERE
nome='$nome';"; íresultado - pg_query($conn, $sql);

e) ínome = $_GET["nome"]; $sql = "SELECT nome, sobrenome, encrypt(senha) FROM
tb_usuario WHERE nome=ínome;"; $resultado = pg_query_params($conn, $sql);

6i.(CESPE / MPE-AP - 2021) No desenvolvimento de um sistema em PHP, o desenvolvedor precisa validar se o endereço bob@mpap.mp.br é ou não um email válido. A partir dessa situação hipotética, assinale a opção em que o código apresentado é o correto para o desenvolvedor realizar a referida validação, tendo como referência que a variável a sertestada é $email.
/ 121

/

a) <?php if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { echo "Invalid email format";}
else {
echo "Valid email format";} ?>

b) <?php if (!preg_match("/A[a-zA-Z-' ]*$ íemail)) {echo "Invalid email format";}
else {
echo "Valid email format";} ?>

c) <?php if (emailspecialchars($email)) {echo "Valid email format";} else {echo "Invalid email format";} ?>
d) <?php if (ctype_alnum (semail)) {echo "Valid email format";} else {echo "Invalid email format";} ?>
e) <?php if (strncasecmp ($email, 7A[a-zA-Z-' ]*$ @./")) {echo "Valid email format";}
else {
echo "Invalid email format";} ?>

62. (QUADRIX/ CRM 4 - 2021) Considerando o trecho de código acima, julgue o item.

<?php
IncludeCpages/footer.php');

?>

O construtor include() está incluindo o arquivo pages/footer.php. Caso seja utilizado o construtor require() ao invés do construtor include() e o arquivo footer.php não seja encontrado no diretório pages, será apresentado um warning, indicando que o arquivo não foi encontrado,mas permitindo ainda a execução do script.

63. (QUADRIX / CRM 4 - 2021) Na linguagem PHP, a função Itrimfjé utilizada para retirar os espaços em branco no início e no final de uma string.
64. (APICE / DPE-PB - 2021) O PHP (um acrônimo recursivo para PHP: Hypertext
Preprocessor) é uma linguagem de script open source de uso geral, muito utilizada, e especialmente adequada para o desenvolvimento web e que pode ser embutida dentro do HTML.
65. (PS CONCURSOS / PREFEITURA DE SC - 2021) Analise o código abaixo e responda, a qual linguagem de programação melhor se enquadra essa sintaxe:
Svl = 40;

Sv2 - 20;

if ( $vl > $v2 ) {

echo "A variável M.$vl. " e maior que a variável ".Sv2;
}

Alternativas:

a) ASP

b) PASCAL

c) JAVA

d) C#

e) PHP

66. (CESPE / MINISTÉRIO DA ECONOMIA - 2020) Uma expressão lambda é usada principalmente para definira implementação procedural de uma interface associativa.
67. (CESPE / TJ-AM - 2019) Após a configuração de um servidor Apache com módulo PHP,
uma forma de validar o seu funcionamento é criar uma página HTML e inserir a função phpinfo (),que mostra informações a respeito da configuração do PHP no servidor Apache.

68. (CESPE/TJ-AM - 2019) A função current () não retorna o valor armazenado onde o ponteiro atual aponta.
69. (CESPE / TJ-AM - 2019) A linguagem PHP suporta o uso de operadores lógicos capazes de diversas comparações lógicas. O operador && considera que uma comparação será verdadeira se um ou ambos os argumentos forem verdadeiros.
70. (CESPE / MP-SC - 2014) PHP é uma linguagem de alto nível, logo o programador precisar acessar diretamente a memória para acionar os ponteiros em uma implementação.
71. (SELECON / EMGEPRON - 2021) A figura mostra um código em PHP.

<!DOCTYPE html>

<html>

<body>

<?php

$m = 44;

$n - 27;

$p = 15;
echo ++$p;

if ($m « 44 or $n « 79) {
echo w EMGEPRON!";

}

else {

echo M MARINHA!";

}

?>

</body>

</html>

Após a execução, a saída está indicada na seguinte opção:

a) 16 MARINHA!

b) 15 MARINHA!

c) 16 EMGEPRON!

d) 15 EMGEPRON!

72. (APICE/ DPE-PB - 2021) Existe a possibilidade dos valores do array em PHP serem outros arrays e árvores. Incluindo a biblioteca com a diretiva #include<Arrays>, é possível realizar a manipulação de arrays multidimensionais.
73. (APICE / DPE-PB - 2021) Um array no PHP é tipo que relaciona valores a chaves.
Este tipo é otimizado para várias usos diferentes: ele pode ser tratado como um array,uma lista
(vetor), hashtable (que é uma implementação de mapa), dicionário, coleção, pilha ou fila.

74. (APICE / DPE-PB - 2021) Para definir uma classe no PHP, deve-se começar com a palavra-chave class, seguida do nome da classe e de um par de colchetes que englobam as definições de propriedades e métodos pertencentes à classe.
75. (APICE / DPE-PB - 2021) Quando PHP interpreta um arquivo, uma procura pelas tags de abertura e fechamento, <?php e ?>, é realizada. Estas tags indicam para iniciar ou parar a interpretação do código entre elas.
76. (CIGA-SC - 2020) Para responder à questão, considere o código apresentado pela
Figura 7
abaixo, escrito em PHP 5.5:

/ 121

/

<?php dass Fundonario {public $nome;

public Ssituacao;
public Stipo;

function construct($nome) {

$this->nome = $nome;

>

>

dass FundonarioAtivo extends Fundonario {
function construct($nome) {

parent:: construct(Snome);

$this->situacao "ativo*;

>

>

dass Fundonariolnativo extends Fundonario {

function Funcionariolnativo($nome) {

parent:: construct(Snome);

$this->situacao "inativo";

>

}

$fal new FuncionarioAtivo("João");

$fa2 = new FuncionarioAtivo("João");

$fi = new FuncionarioInativo("Joáo");

?>

Analise as seguintes expressões lógicas escritas em PHP 5.5, caso fossem avaliadas logo após a execução do código apresentado anteriormente:
1. $fai===$fi

2. $fai==$fi

3. $fai===$fa2

4. $fai==$fa2

A alternativa que apresenta o resultado correto das expressões é:

a) TRUE - FALSE - FALSE - FALSE

b) TRUE - TRUE - FALSE - FALSE

c) FALSE-TRUE-TRUE-TRUE

d) FALSE-FALSE-FALSE-TRUE

e) FALSE-FALSE-TRUE-TRUE

77. (Prefeitura de São Paulo - 2020) Analise o trecho do código PHP a seguir.

$x = 10;

if ($x == '10') {
echo"SIM";

} else {

echo"NÃO";

}

Ao ser executado, esse código apresentará a mensagem:

a) "SIM", pois o operador "==" compara apenas o valor e não o tipo.

b) "SIM", visto que o operador "==" é de atribuição, e seu resultado é sempre verdadeiro.

c) "NÃO", pois os tipos das variáveis são diferentes e não podem ser comparados.

d) NÃO", pois cadeias de caracteres devem ser delimitadas por aspas duplas, caso contrário apenas o primeiro caractere é considerado.
e) "NÃO", pois a comparação de variáveis com tipos diferentes sempre retorna "falso".

78. (UFMT - UFMT - 2021) Um conceito muito importante em programação orientada a objetos é o de exceções. Exceções podem ser conceituadas como ocorrências de programação tidas como inválidas durante o processamento e que paralisam o programa até que sejam resolvidas.
Em PHP, exceções são objetos especiais e derivam da classe Exception, possuindo métodos específicos de retorno. Selecione, a seguir, a alternativa que lista apenas métodos presentes na referida classe Exception do PHP:
a) getMessage(), getCode(), getTraceAsString().

b) getLineO, getStackTraceStringO, getFile().

c) getPrevious(), getTrace(), getSuppressed().

d) try(), catch(), finaIly().

e) getStackTraceStringO, getCode(), getMessage().

79. (UFMT - UFMT - 2021) O Hypertext Preprocessor (PHP) é uma linguagem de script usada no desenvolvimento web. Sobre o PHP, marque V para as afirmativas verdadeiras e F para as falsas
() Possui tag que indica final do código PHP.
() Trata-se de uma linguagem open source.
() Elimina o uso de códigos HTML e CSS.

() O código é executado apenas no cliente.
Assinale a sequência correta.

a) V,V,F,F

b) F,F,V,V

c) F,V,F,V

d) V,F,V,F

8o.(CONSULPLAN / Prefeitura de Colômbia-SP - 2021) Comando do PHP (Personal Home Page)
"adiciona um parâmetro a um procedimento armazenado local ou remoto quando utilizado com o Microsoft SQL Server". A afirmativa se refere a:
a) mssqljnit b) mssql_bind c) mssql_execute d) mssql_fetch_row
81. (CONSULPLAN / Prefeitura de Colômbia-SP - 2021) Considerando as funções do PHP para manipulação de documentos em PDF, uma delas "preenche o caminho atual e o desenha no documento". Trata-se de:
a) pdf_fiII

b) pdf_stroke c) pdf_fill_stroke d) pdf_fill_textblock
82. (CESPE / PGDF - 2021) PHP é uma linguagem de script projetada para desenvolvimento web,mas que também pode ser usada para programação de uso geral.

83. (OBJETIVA / Prefeitura de Santa Maria-RS - 2021) Conforme BONATTI, sobre tecnologias e linguagens utilizadas na construção de websites, numerar a 2a coluna de acordo com a ia e,após, assinalara alternativa que apresenta a sequência CORRETA:

i)CSS.

(2) PHP.

(3) HTML.

( ) É uma linguagem de programação open source, que é interpretada pelo servidor,
muito utilizada para o desenvolvimento de aplicações voltadas para a internet.
( ) Serve para promover o acabamento visual das páginas web. Pode ser compartilhado entre várias páginas, permitindo, assim, uma padronização visual muito simplificada e lógica.
( ) É uma linguagem de marcação, que é interpretada pelo browser para dar formatação e posicionamento ao conteúdo do website.
a) i-2-3

b) 3-2-1

c) 2 - 3 -1

d) 2-1-3

e) 3-i-2

84. (OBJETIVA / Prefeitura de Santa Maria-RS - 2021) Considere o seguinte código escrito na linguagem PHP.
<?php function inversa($x) { if ($x==o) { throw new Exceptionf exception'); }
return i/$x;

} try { echo inversa(o); echo " try catch (Exception $e) { echo
" catch echo $e-

>getMessage();} finally { echo " finally";}

Ao se executar esse código, será impressa na tela a seguinte sequência de palavras:

a) try catch exception finally b) try catch finally c) catch exception finally d) catch exception e) finally catch exception
85. (OBJETIVA / Prefeitura de Santa Maria-RS - 2021) A forma correta de se declarar uma constante na linguagem PHP é:
a) constant "XPTO" = "alguma coisa";

b) constant $XPTO = "alguma coisa";

c) constant("XPTO","alguma coisa");

d) declare("XPTO","alguma coisa");

e) define("XPTO","alguma coisa");

86. (CESPE / FUNPRESPJUD - 2021) Quando enviamos um arquivo através de um formulário para o PHP, ele cria a super global $_FILES, no mesmo estilo das super globais $_GET e $_POST.Cada campo do tipo file é colocado em um array dentro de $_FILES.

87. (UFSC / UFSC - 2016) Considere o seguinte fragmento de código presente em uma página de uma aplicação escrita em PHP:
<p<?php if ($destaque): ?class="destaque"<?php endif;»Parágrafo.</p>

O fragmento gerará qual código HTML, caso o valor da variável "$destaque" seja verdadeiro(true), quando a página for requisitada por um navegador?

a) <p class="destaque">Parágrafo.</p>

b) <p>Parágrafo.</p>

c) Parágrafo.

d) <p class="$destaque">Parágrafo</p>

e) <px/p>

88. (FGV / TJ-TO - 2022) Num script PHP, a função que permite verificar se um cookie está definido é:
a) active()

b) cookie_value()

c) exists()

d) isset()

e) status()

89. (FGV / TJ-TO - 2022) Numa página web, um script PHP deve ser localizado entre as tags:

a) <?php ?>

b) <php php>

c) <?php> <?>

d) <scriptPHP scriptPHP>

e) <.php ,php>

90. (FCC/TJ-SC-2O2i) Considere o método abaixo, em uma classe PHP chamada Cliente.
publicfunction setNome($Nome) {

$this->Nome = $Nome;

A partir de outra classe, um objeto na classe Cliente foi instanciado por meio da instrução $cli =new Cliente;. Para chamar o método acima e passar o nome 'Paulo' como parâmetro,
utiliza-se a instrução:
a) $cli::setNome('Paulo');

b) $cli->setNome('Paulo');

c) $cli.nome('Paulo');

d) $cli->send.setNome('Paulo');

e) $cli.setNome('Paulo');

91. (VUNESP / PREF. ILHABELA - 2020) Analise o trecho de código PHP a seguir.

$x = 10;

if ($x == '10') {
echo"SIM";

} else {

echo "NÃO";

}

Ao ser executado, esse código apresentará a mensagem:

a) "SIM", pois o operador "==" compara apenas o valor e não o tipo.

b) "SIM", visto que o operador "==" é de atribuição, e seu resultado é sempre verdadeiro.

c) "NÃO", pois os tipos das variáveis são diferentes e não podem ser comparados.

d) NÃO", pois cadeias de caracteres devem ser delimitadas por aspas duplas, caso contrário apenas o primeiro caractere é considerado.
e) "NÃO", pois a comparação de variáveis com tipos diferentes sempre retorna "falso".

g2.(FUNDATEC / CIGA-SC - 2020) Qual dos trechos de código abaixo, em linguagem PHP
5.5, é executado sem erros e, adicionalmente, pode ser considerado o mais seguro para fazer uma consulta em uma tabela de usuários em um banco de dados relacional PostgreSQL?
a) $nome = "João"; $sql - "SELECT nome, sobrenome, senha FROM tb_usuario
WHERE
nome=$nome;"; sresultado = pg_query($conn, ssql);

b) ínome = $_GET["nome"]; ssql = "SELECT nome, sobrenome, senha FROM
tb_usuario
WHERE nome='$nome;'"; sresultado = pg_secure_query($conn, ssql);

c) ínome = $_GET["nome"]; ssql = "SELECT nome, sobrenome, senha FROM
tb_usuario
WHERE nome=$i;"; sresultado = pg_query_params($conn, ssql, array(snome));

d) snome = $_GET["nome"]; ssql = "SELECT nome, sobrenome, senha
WHERE
nome='$nome';"; sresultado = pg_query($conn, ssql);

e) snome = $_GET["nome"]; ssql = "SELECT nome, sobrenome, encrypt(senha) FROM
tb_usuario WHERE nome=$nome;"; sresultado = pg_query_params($conn, ssql);

93. (CESPE / TCE-SP 2015) Em PHP é possível usar uma variável sem declarar seu tipo,
que será decidido, também, durante a execução do programa.
94. (CESPE / TCE-SP 2015) PHP é uma linguagem de programação de scripts, interpretada,
de baixo nível, open-source, gratuita, server-side, dinamicamente/fracamente tipada,estruturada e orientada a objetos, portável, robusta e eficiente utilizada para desenvolvimento web.
95. (CESPE / TJ-AM - 2019) A linguagem PHP suporta o uso de operadores lógicos capazes de diversas comparações lógicas. O operador && considera que uma comparação será verdadeira se um ou ambos os argumentos forem verdadeiros.
96. (CESPE /TJ-AM - 2019) Após a configuração de um servidor Apache com módulo
PHP, uma forma de validar o seu funcionamento é criar uma página HTML e inserir a função phpinfo (),que mostra informações a respeito da configuração do PHP no servidor Apache.

97. (CESPE / MINISTÉRIO DA ECONOMIA - 2020) Após a configuração de um servidor Apache com módulo PHP, uma forma de validar o seu funcionamento é criar uma página HTML e inserir a função phpinfo ( ), que mostra informações a respeito da configuração do PHP no servidorApache.

98. (ADMTEC / PREFEITURA DE RIO LARGO - 2019) Analise o código abaixo e responda, a qual linguagem de programação melhor se enquadra essa sintaxe:
<?

Svl = 40;

Sv2 * 20;

if ( $vl > $v2 ) {

echo "A variável *.Svl." é maior que a variável ".$v2;
}

?>

a) ASP

b) PASCAL

c) JAVA

d) C#

e) PHP

99. (QUADRIX / CRM 4 - 2021) Na linguagem PHP, a função Itrimfj é utilizada para retirar os espaços em branco no início e no final de uma string.
100. (QUADRIX / CRM 4 - 2021) Considerando o trecho de código acima, julgue o item.

<?php
IncludeCpages/footer.php');

?>

O construtor include() está incluindo o arquivo pages/footer.php. Caso seja utilizado o construtor require() ao invés do construtor include() e o arquivo footer.php não seja encontrado no diretório pages, será apresentado um warning, indicando que o arquivo não foi encontrado, mas permitindo ainda a execução do script.
101. (CESPE / MPE-AP - 2021) No desenvolvimento de um sistema em PHP, o desenvolvedor precisa validar se o endereço bob@mpap.mp.br é ou não um email válido. Apartir dessa situação hipotética, assinale a opção em que o código apresentado é o correto para o desenvolvedor realizar a referida validação, tendo como referência que a variável a ser testada é $email.
a) <?php if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { echo "Invalid email format";}
else {
echo "Valid email format";} ?>

b) <?php if (!preg_match("/A[a-zA-Z-' ]*$ @./", $email)) {echo "Invalid email format";}
else {
echo "Valid email format";} ?>

c) <?php if (emailspecialchars($email)) {echo "Valid email format";} else {echo "Invalid email format";} ?>
d) <?php if (ctype_alnum ($email)) {echo "Valid email format";} else {echo "Invalid email format";} ?>
e) <?php if (strncasecmp ($email, 7A[a-zA-Z-' ]*$ @./")) íecho "Valid email format";} else {
echo "Invalid email format";} ?>

102. (CESPE/MEC-2015)

<?php if (isset($_REQUEST['emai1'])) {
$admin_emai1 = "admin@prova.com";

$email = $_REQUEST['email'];

$subject = $_REQUEST['subject'];

$comment = $_REQUEST['comment'];

mai1($admin_emai1, "$subject", $comment, "From:".

$emai1);

echo "Obrigado";

}

else {

<form method="post">

Email: <input name="email" type="text" /xbr />
Assunto: cinput name="subject" type="text" /xbr />
Mensagem:<br />

<textarea name="comment" rows="15"
cols="40"x/textarea><br />

<input type="submit" value="Submit" />

</form>

<?php

}

De acordo com o trecho de código apresentado, julgue o item subseguente.
O trecho de código semail = $_REQUEST['email']; indica que a variável $email recebe como parâmetro o email do administrador do portal prova.com.
103. (CESPE / MEC - 2015) De acordo com o trecho de código apresentado, julgue o item subsequente.
00 SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software -
2023 (Pós-Edital)

(Profs. Paolla Ramos e Raphael L

<?php if (isset($_REQUEST[*email'])) {
$admin_email - "admin@prova.com";

$email « $_REQUEST(*email'] ;
Ssubject = $_REQUEST['subject'];

$comment = $_REQUEST['comment'];

mail($admin_emailf "$subject", $comment, "From:".

$email);

echo "Obrigado";

}

else (

?>

<form method-"post">

Email: <input name="email" type="text" /xbr />
Assunto: <input name="subject" type="text" /xbr />
Mensagem:<br />

<textarea name-"comment" rows-"15"
cols-"40"x/textarea><br />

<input type-"submit" value-"Submit" />

</form>

<?php

?>

O código apresentado é um exemplo de formulário para enviar email em PHP e está sintaticamente correto.
104. (CESPE / ANATEL - 2014) Em PHP 6, a passagem de variáveis entre páginas, por meio do uso de sessões, está limitada a informações fornecidas pelo usuário em uma página.
105. (CESPE / ANATEL - 2014) A utilização do PHP atende a mais de uma finalidade: gerar scripts no lado servidor, que é o uso mais comum da linguagem; gerar scripts em linha de comando,caso em que é necessário apenas o interpretador; e escrever aplicações para desktop,
situação em que é necessária a extensão PHP-GTK.
106. (CESPE/ANATEL - 2014) O script PHP abaixo está correto e exibe o número 9
como saída. <

?php function soma($b==5, $c==4){ return $b+$c;} echo soma(); ? >

107. (CESPE / ANATEL - 2014) Existem três tipos de operadores em PHP: os unários, que operam em apenas uma sentença; os binários, que retornam o valorde acordo com a operação realizada em duas sentenças; e os ternários, que entre dois valores selecionam um, a depender de um terceiro.
108. (CESPE / ANATEL - 2014) No que se refere à linguagem PHP, julgue os itens subsecutivos.

$_4dias, $ãripãev e $margem_são variáveis válidas no PHP.

109. (CESPE / STM - 2018) O comando INCLUDE interromperá a execução do script assim que ocorrer um erro, enquanto o comando REQUIRE continuará a executar o código após o erro.
110. (CESPE / SEDF - 2017) AngularJS, Ajax, JQuery, Less e PHP são tecnologias para desenvolvimento web front-end.
111. (CESPE / TCE-PA - 2016) As instruções echo e print, do PHP 5, são utilizadas para viabilizar a saída de dados na tela.
112. (CESPE / TCE-PA - 2016) Em PHP 5, a função count é utilizada para retornar o número de elementos de um ctrray.
113. (CESPE / MPU - 2013) O código da linguagem PHP é interpretado em um servidor web,enquanto o código da linguagem Java é interpretado pela própria máquina.

114. (CESPE / TRT10 - 2013) No código abaixo, o teste da condição retornará verdadeiro.

<?php if (2 === 2.0)
echo "2 é igual a 2.0";

?>

115. (CESPE /TRT10 - 2013) Ao ser corretamente executado, o trecho de código abaixo avalia se o conteúdo da variável van é diferente do conteúdo de var2; caso a avaliação seja verdadeira,será emitida mensagem de que os valores são diferentes.

<?php if ($van <> $var2)
echo "$van é diferente de $var2";

?>

116. (CESPE / TCDF - 2014) Zend Framework é uma biblioteca PHP para desenvolvedores que permite utilizar ferramentas controladas de acesso às informações de transação, de modo a padronizar-se o processo de desenvolvimento para que a interface seja estruturada por tags personalizadas.
117. (CESPE / EBSERH - 2018) Julgue o item que se segue a respeito das características da linguagem PHP e de compiladores.
O código PHP

< ?php

$txt ,Viva';

print H $txt a vida \nM;
print 1 $txt a vida *;

?>

apresenta o resultado a seguir.

Viva a vida

$txt a vida

118. (CESPE / EBSERH - 2018) Na linguagem PHP, o comando explode() permite descarregar os buffers de saída de qualquer backend que o PHP esteja usando, como, por exemplo,um CGI
ou um servidor web.

119. (CESPE / EBSERH - 2018) PHP consiste de uma linguagem compilada para código nativo e gera um bytecode que é interpretado por uma máquina virtual implantada em cada cliente onde o código será executado.
120. (CESPE / EBSERH - 2018) O comando a seguir concatena corretamente caracteres em PHP.ífinal = "abc". "efg";

121. (QUADRIX/ CRBM 4 - 2021) Considerando o trecho de código acima, julgue o item.

<?php
IncludeCpages/footer.php');

?>

O construtor include() está incluindo o arquivo pages/footer.php. Caso seja utilizado o construtor require() ao invés do construtor include() e o arquivo footer.php não seja encontrado no diretório pages, será apresentado um waming, indicando que o arquivo não foi encontrado,mas permitindo ainda a execução do script.

122. (QUADRIX / CRBM 4 - 2021) Na linguagem PHP, a função Itrim() é utilizada para retirar os espaços em branco no início e no final de uma string.
123. (QUADRIX / CRQ 4 Região - 2018) Em programas PHP, os comentários podem ser usados utilizando-se os caracteres "II" ou 7* */", sendo que estes últimos delimitam textos que podem se estender em mais de uma linha.
124. (QUADRIX / CRQ 4 Região - 2018) A linguagem PHP é baseada em script de uso livre(open source) e adequada para o desenvolvimento web, pois pode ser embutida em códigos
HTML.

125. (QUADRIX / CRN 9 - 2018) Uma das utilidades do safe_mode é a proteção dos scripts PHPcontra acessos remotos.

126. (QUADRIX / CRN 9 - 2018) A PHP é considerada como uma linguagem de programação totalmente insegura, visto que ela não pode ser utilizada em aplicações que estejam relacionadas a informações relevantes, como as confidenciais e as bancárias.
127. (QUADRIX / CRN 9 - 2018) Ao desabilitar a diretiva register_globals,
a PHP somente interpretará variáveis inicializadas.
128. (QUADRIX / CRN 9 - 2018) O ponto e vírgula, na linguagem de programação
PHP, é usado no término de uma declaração.
129. (QUADRIX / CRO-AC- 2019) No PHP, para cada necessidade, deve ser criado um procedimento, já que os procedimentos não podem ser reaproveitados em outras situações.
130. (QUADRIX / CRESC-SC- 2019) O código $Cad_Especialidade['Pesq Area'] = 'Social',
em
PHP, representa o armazenamento do elemento ('Social') em uma variável do tipo array,
em que $Cad_Especialidade é a chave de pesquisa associada ao elemento armazenado.
131. (QUADRIX / CRESC-SC- 2019) Na declaração de uma função, na linguagem
PHP, as variáveis enviadas por referência devem ser identificadas pelo símbolo &
132. (QUADRIX / CRO-AC- 2019) Uma função no PHP, mesmo sendo uma função isolada,
tem como característica principal a retenção de informações, ou seja, a função armazena informações para serem usadas no futuro.
133. (QUADRIX / CRO-AC- 2019) No PHP, para cada necessidade, deve ser criado um procedimento, já que os procedimentos não podem ser reaproveitados em outras situações.
134. (QUADRIX / CRM-PR - 2019) Considerando o programa abaixo, julgue o próximo item.

<!D0CTYPE html>

<html>

<body>

<?php for ($x = 0; $x <= 10; $x++) {
echo "The number is: $x <br>";

}

?>

</body>

</html>

A saída do programa resultará em uma linha no navegador do cliente, contendo a frase:
The number is: o 12 3 4 5 6 7 8 910.
135- (QUADRIX / CRM-PR - 2019) Considerando 0 programa abaixo, julgue 0 próximo item.

OO SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital) x 116

Z 121

/

<!D0CTYPE html>

<html>

<body>

<?php for ($x = 0; $x <= 10; $x++) {
echo "The number is: $x <br>";

}

?>

</body>

</html>

O comando de repetição for incrementa a variável x com valores de o a io.

136. (QUADRIX / CRM-PR - 2019) Considerando o programa abaixo, julgue o próximo item.

<!D0CTYPE html>

<html>

<body>

<?php for ($x = 0; $x <= 10; $x++) {
echo "The number is: $x <br>";

}

?>

</body>

</html>

O programa deve ser executado em um servidor web com PHP instalado e seu resultado aparecerá no browser do cliente que o acessar.
137. (QUADRIX/CRM-PR - 2016) Considerando um programa em PHP com os seguintes valores nas variáveis: a=6 b=5 0=4. Qual será a saída do trecho de código abaixo:
<?php if($a<$b){
echo "Marte";

} elserf ($b > $c) {
echo 'Terra";

} elseif ($b == $c){

echo "Júpiter / Vénus";

} else {

echo "Mercúrio";

}

?>

a) MARTE.

00 SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software -
2023 (Pós-Edital)

b) TERRA.

c) JÚPITER.

d) VÉNUS.

e) MERCÚRIO.

138. (QUADRIX / CFP - 2016) Sobre PHP é correto afirmar que:

a) as variáveis começam com um sinal #, seguido do nome da variável.

b) possui comandos obrigatórios para declarar variáveis antes que elas recebam um valor.

c) o operador de concatenação (.) é usado para juntar dois valores string.

d) não converte automaticamente a variável para o tipo de dado correto, dependendo do valor recebido.
e) tem apenas dois diferentes escopos de variáveis: local e global.

139. (FCC / TRE-BA - 2015) Para conectar uma aplicação PHP5 orientada a objetos aos principais servidores de banco de dados, abstraindo o acesso de forma que, para se mudar de servidor,seja necessário alterar apenas a string de conexão, deve-se utilizar a biblioteca:

a) PHPDbc b) Detector c) Whoops d) PDO
e) ObjectODBC

140. (FCC / TRE-RR - 2015) Considere o seguinte scrípt encontrado em uma página PHP.

<?php

$idade » array("Paulo">"40" , "Pedro"«>"62"t

**Ana" = >"43", "Marcos"«>"18") ;

arsort($idade);

foreach($idade as $x => $x_valor) {
echo $x . " " . $x_valor . * *;

}

?>

Ao executar o script será exibido na página:

a) Ana = 43 Marcos = 18 Paulo = 40 Pedro = 62

b) Marcos = 18 Paulo - 40 Ana = 43 Pedro = 62

c) o - 62 1 - 43 2 = 40 3 = 18

d) Pedro = 62 Paulo = 40 Marcos = 18 Ana = 43

e) Pedro = 62 Ana = 43 Paulo = 40 Marcos = 18

GABARITo - DIVERSAS BANCAS

1. LETRA C 41. ERRADO
81. LETRA C

2. LETRA D 42. CORRETO
82. CORRETO

3- LETRA A 43- CORRETO
83- LETRA D

4- LETRA B 44. CORRETO
84. LETRAC

5- LETRA D 45- CORRETO
85. LETRA E

6. LETRA A 46. ERRADO
86. ERRADO

7- LETRA B 47- LETRA A
87. LETRA A

8. LETRA E 48. CORRETO
88. LETRA D

9- LETRA B 49- ERRADO
89- LETRA A

10. LETRA E 50. CORRETO
90. LETRA B

íi. LETRA A 51- ERRADO
91. LETRA A

12. LETRA B 52. ERRADO
92. LETRA C

13- LETRAC 53- ERRADO
93- CORRETO

14- LETRA D 54- CORRETO
94- CORRETO

x5- LETRA B 55- ERRADO
95- ERRADO

16. LETRA E 56. ERRADO
96. CORRETO

17- LETRAC 57- CORRETO
97- ERRADO

i8. LETRA B 58. ERRADO
98. LETRA E

19. LETRA A 59- CORRETO
99- ERRADO

20. LETRA A 60. LETRA C
100. ERRADO

21. LETRA B 61. LETRA A
101. LETRA A

22. LETRAC 62. ERRADO
102. ERRADO

23- LETRA E 63- ERRADO
103. CORRETO

24. LETRA B 64. CORRETO
104. ERRADO

25- LETRA E 65. LETRA E
105. CORRETO

26. LETRA D 66. ERRADO
106. ERRADO

27- LETRA B 67. CORRETO
107. CORRETO

28. LETRA E 68. ERRADO
108. CORRETO

29. LETRA C 69. ERRADO
109. ERRADO

30. LETRA E 70. ERRADO
110. ERRADO

3i- LETRA D 71- LETRAC
111. CORRETO

32. LETRA E 72. ERRADO
112. CORRETO

33- LETRAC 73- CORRETO
113. ERRADO

34- LETRA A 74- CORRETO
114. ERRADO

35- LETRA B 75- CORRETO
115. CORRETO

36. LETRA C 76. LETRA D
116. CORRETO

37- LETRA D 77- LETRA A
117. ERRADO

38. LETRA E 78. LETRA C
118. ERRADO

39- CORRETO 79- LETRA C
119. CORRETO

40. CORRETO 80. LETRA B
120. ERRADO

121. CORRETO 128. CORRETO 135-
CORRETO

122. ERRADO 129. ERRADO
136. CORRETO

123- CORRETO 130. ERRADO 137-
LETRA B

124. CORRETO 131. CORRETO 138.
LETRA C

125. CORRETO 132. ERRADO
139- LETRA D

126. ERRADO 133- ERRADO
140. LETRA E

127. CORRETO 134- ERRADO

