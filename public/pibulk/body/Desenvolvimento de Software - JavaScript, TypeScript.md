# Desenvolvimento de Software - JavaScript, TypeScript

Índice

1) JavaScript - Teoria

2) JavaScript - Questões Comentadas

3) JavaScript - Lista de Questões

4) JavaScript Moderno (Ecma 2021) - Teoria

5) JavaScript Moderno (Ecma 2021) - Questões Comentadas

6) JavaScript Moderno (Ecma 2021) - Lista de Questões

7) TypeScript - Teoria

8) TypeScript - Questões Comentadas

9) TypeScript - Lista de Questões

Conceitos Básicos

JAVASCRIPT

INCIDÊNCIA EM PROVA: ALTÍSSIMA

A tecnologia Javascript nasceu a partir de um contexto maior, logo inicialmente eu vou precisar fazer uma grande contextualização, para que o assunto faça sentido para vocês. Alinguagem de marcação HTML, surgiu na década de 1990 e destina-se a estruturar uma página web, não sendo empregada para adicionar estilos ou apresentação visual aos elementos que constituem a página,sendo tais tarefas função das folhas de estilo em cascata.

Ela também não possui funcionalidades que permitam adicionar interatividade avançada à página, sendo tal tarefa função das linguagens de programação. Então grave o seguinte:
A linguagem HTML não é empregada para adicionar estilos ou apresentação visual aos elementos que constituem a página, sendo tais tarefas função das folhas de estilo em cascata. Ela também não possui funcionalidades que permitam adicionar interatividade avançada à página, sendo tal tarefa função das linguagens de programação.
PROFESSOR, MAS A AULA NÃO É SOBRE JAVASCRIPT, ECMA, TYPESCRIPT, JQUERY E AJAX?

Calma jovem, lembre-se que estamos contextualizando. Como assim, professor? O Javascript foi criado pela Netscape em parceria com a Sun Microsystems, com a finalidade de fornecer um x y 79
/

meio de adicionar interatividade a uma página web. A primeira versão, denominada
JavaScript í.o, foi lançada em 1995 e implementada em março de 1996 no navegador NetscapeNavigator 2.0
quando o mercado era dominado pela Netscape.

Logo a seguir, veio a época da chamada guerra dos browsers, cujos efeitos nocivos se fazem sentir até os dias atuais. Para não fugir à regra, a Microsoft, em resposta à Netscape,criou a linguagem
JScript baseada em Visual Basic cuja primeira versão denominada JScript 1.0 e foi lançada com o navegador Internet Explorer 3.0. Não há como fazer funcionar um formulário HTML com o uso de elementos HTML.
A HTML limita-se a criar os rótulos e campos de um formulário para serem preenchidos pelo usuário e nada mais. Com HTML, não conseguimos processar os dados nem mesmo enviá-los ao servidor ou a outra máquina qualquer. Para cumprir essas tarefas, é necessário utilizar um programa que consiga manipular e processar os dados. Entendido?
Um desenvolvedor web moderno deve saber três linguagens de programação: HTML, para definir o conteúdo das páginas; CSS para especificar o layout das páginas; e Javascript para programar o comportamento das páginas. Trata-se de uma linguagem extremamente abrangente,funcionando em computadores, servidores, laptops, tablets, smartphones, entre outros1.

Existe um conceito muito importante chamado Document Object Model (DOM), que é uma especificação W3C para representar e interagir com objetos em HTML, XHTML e XML. Pois é, a primeira grande vantagem do Javascript é a sua capacidade de manipular o DOM dePáginas
HTML por meio de diversos métodos. Ele torna possível criar, alterar, deletar e copiar vários elementos HTML.
Como ele faz isso? Ele é capaz de modificar valores de atributos de um Documento
HTML.
Ademais, ele é capaz de modificar Folhas de Estilos do CSS. Incrível, não? Ele também é bastante utilizado para validar entradas de dados do usuário. Como assim, professor?Eventualmente, um formulário pede sua Data de Nascimento! Ele é capaz de receber seus dados e verificar se está no formato correto (dd/mm/aaaa).
Podemos dizer que HTML é para conteúdo; CSS é para apresentação; e
Javascript é para Interatividade! Professor, ouvi dizer que Javascript faz parte da Plataforma Java! Ouviu errado! O primeiro é uma linguagem de scripts de propósito específico, dinamicamente tipada, baseada em protótipos, com escopo de função, que não precisa ser compilada. Osegundo é uma linguagem de programação de propósito geral,
estaticamente tipada, baseada em classes, com escopo de bloco, que precisa ser compilada.
1 Javascript é a linguagem de script padrão de todos os navegadores modernos e do HTML5. Apesar disso, ela não é utilizada apenas em Páginas HTML.
y 79

/

IMPORTANTE

JAVASCRIPT É UMA LINGUAGEM DE USO ESPECÍFICO! ELA FOI DESENVOLVIDA PARA APRIMORAR A
EXPERIÊNCIA DOS
USUÁRIOS NOS NAVEGADORES. ELA NUNCA FOI UMA LINGUAGEM DE PROPÓSITO GERAL (EX: JAVA,
CAPAZ DE CRIAR
APLICAÇÕES INTEIRAS]. NO ENTANTO, RECENTEMENTE 0 JAVASCRIPT TEM SE ENVEREDADO PARA ESSE
PROPÓSITO, POR
MEIO DAS JSLIBS. PERCEBA: 'JSLIBS IS A STANDALONE JAVASCRIPT DEVELOPMENT RUNTIME
ENVIRONMENT FOR USING
JAVASCRIPT AS A GENERAL-PURPOSE SCRIPTING LANGUAGE"!

Há uma frase em inglês que eu acredito que defina bem a diferença entre ambas as linguagens:
"Java and Javascript are as similar as Car and Carpet". Isso quer dizer que as linguagens são completamente diferentes e uma das poucas coisas em comum é o prefixo do seu nome(Java), e só! Captaram a mensagem? Pois é, não caiam em pegadinha de banca alguma agora.
JavaScript é uma linguagem client-side (desenvolvida para rodar no lado do cliente), i.e., a interpretação e o funcionamento da linguagem dependem de funcionalidades hospedadas no navegador do usuário (ele contém um interpretador JavaScript). Com oJavaScript, pode-se manipular conteúdo e apresentação; manipular o navegador; interagir com formulários; e interagir com outras linguagens dinâmicas.
Por fim, um detalhe interessante: JavaScript é baseado em ECMAScript.
Professor, o que é
ECMAScript? É uma especificação para linguagens de scripts que é implementada pelo
JavaScript,
entre outras linguagens (vamos ver mais sobre ela ainda nessa aula). Ela se encontra na Versão 2021
e trouxe a maior mudança para a linguagem JavaScript desde a sua criação, há cerca de 20 anos.

O principal objetivo da nova versão especificação foi tornar a linguagem mais flexível,
enxuta e fácil de se aprender e trabalhar, tornando-a mais próxima a outras linguagens orientadas a objeto, como Java e Python. Dentre as principais mudanças, temos: criação de novos tipos de dados(Map, WeakMap, Set, WeakSet); novas maneiras de iterar objetos e coleções;
declaração de variáveis com let e const.
Além dessas, temos: modularização e estrutura de classes; geradores e símbolos;
operadores rest e spread. Nos últimos anos, o JavaScript ganhou muita força na comunidade de desenvolvedores através do "grande boom" do ecossistema das tecnologias Node.js e npm. Desde então, a flexibilidade da linguagem tem sido usada a favor não somente do lado do cliente, mas também do lado do servidor.
Galera, isso era algo impensável até alguns anos atrás. Tudo isso fez com que não somente a comunidade, mas também grandes empresas de tecnologia como o Facebook, reconhecessem a força da linguagem e finalmente a levasse a sério. Esse interesse na linguagem se refletiu na criação de uma imensa diversidade de bibliotecas e frameworks, como: ReactJS, Angular2,Meteor,
Electron, etc;

x y 79
/

Para escrever código Javascript, não há necessidade de instalar um software especial.Escrevemos com um editor de textos simples e visualizamos o resultado em um navegador.Arquivos escritos com o uso dessa linguagem devem ser separados com a extensão .js e são criados para serem executados dentro de um Arquivo HTML. O código deve sempre vir entre as tags <script> e </script>:
<script>

function minhaFuncao() {

document.getElementById("demo").innerHTML = "Minha primeira função iavaScript!";

}

</script>

Existem três maneiras de inserir Javascript em HTML:

Externo: escrever o script em um arquivo externo com extensão .js e inserir com um link na tag

<script> dentro da seção <body> ou <head> do documento

<!DOCTYPE html>

<html>

<body>

<script src="meuScript.js"></script>

</body>

</html>

Incorporado: também conhecida como interna, insere-se o script na seção <head> do documento.
<!DOCTYPE html>

<html>

<head>

<script>

function myFunction() {

Document.getElementById("demo").innerHTML = "Parágrafo modificado.";

}

</script>

</head>

<body>

<hl>A Web Page</hl>

<p id="demo">Um Parágrafo</p>

cbutton type="button" onclick="myFunction()">Experimente!</button>

</body>

</html>

Inline: insere-se o script diretamente na seção <body> do documento. Não é recomendada, pelo princípio da separação das camadas.
<!DOCTYPE html>

<html>

<body>

<hl>Uma Página Web</hl>

<p id="demo">Um Parágrafo</p>

cbutton type="button" onclick="myFunction()">Experimente!</button>

<script>

function myFunctionO {

document.getElementById("demo").innerHTML = "Parágrafo Modificado.";

}

</script>

</body>

</html>

As modernas práticas de desenvolvimento preconizam o uso de scripts externos a serem linkados ao documento. Cria-se um ou mais arquivos contendo os scripts e gravados com a extensão .js e usa-se o elemento script na seção head do documento para linká-lo à página. Essa técnica permite linkar o script a várias páginas do site, facilitando a manutenção.
Inserir script inline é uma prática que pertence ao passado e deve ser evitada pelo desenvolvedor comprometido com os Padrões Web. Ao escrevermos scripts dentro da marcação y 79
/

HTML, estaremos misturando as camadas de marcação e comportamento,
dificultando a manutenção e o entendimento dos códigos. Entendido até agora?
JS: CASE SENSITIVE E COMENTÁRIOS

O Javascript é sensível ao tamanho da caixa (Case-Sensitive). Portanto, os nomes de variáveis,funções e demais identificadores são diferenciados quando escritos com letras maiúsculas ou minúsculas. Por exemplo: as variáveis total, Total, toTal e TOTAL são diferentes. Ométodo write() deve serescrito em minúscula, pois escrever Write() ou WRITEQ causará um erro no script.
Comentários são pequenos textos que o desenvolvedor insere ao longo do script com a finalidade de facilitar o entendimento e a manutenção do código. A linguagem Javascript admite doistipos de marcadores para comentários: comentários de linha única e comentários de múltiplas linhas. Abaixo, podemos ver como funcionam cada uma.
Comentários de linha única:

// Modifica o cabeçalho:

document.getElementByld("meuHeader").innerHTML = "Minha primeira página";

// Modifica o Parágrafo:

document.getElementByld("myP").innerHTML = "Meu primeiro parágrafo.";

Comentários de múltiplas linhas:

/*

O código abaixo modificará o cabeçalho com id = "meuHeader"
e o parágrafo com id = "meuParagrafo"
em minha página web:

*/

document.getElementByld("meuHeader").innerHTML = "Minha primeira página";

document.getElementByld("meuParagrafo").innerHTML = "Meu primeiro parágrafo.";

JS: DECLARAÇÕES

Um script consiste em uma série de instruções escritas segundo uma sintaxe própria e rígida. As instruções determinam a realização de tarefas com a finalidade de obter um resultado final. Cada uma das instruções de um script constitui uma declaração independente e existem duas sintaxes para separar as declarações. Separe-as com ponto-e-vírgula ou coloque cada declaração em uma linha separada.
a = 5;

b = 6;

c = a + b;

É o mesmo que...

a = 5; b = 6; c = a + b;

y 79

/

A sintaxe determina que o ponto-e-vírgula seja obrigatório para separar declarações em uma mesma linha e facultativo para separar declarações em linhas diferentes, contudo é uma boa prática usar ponto-e-vírgula para separar declarações em linhas diferentes. Estou passando rapidamente por esses aspectos, porque isso não é nada diferente da maioria das linguagens de programação.
JS: ESPAÇO EM BRANCO E QUEBRAS DE UNHA

Quebras de linhas e espaços em branco, quando inseridos entre nomes de variáveis, nomes de funções, números e entidades similares da linguagem, são ignorados na sintaxeJavascript. Contudo, para strings e expressões regulares, tais espaçamentos são considerados.No exemplo abaixo, ignoram-se os espaços extras fora da string! Se for dentro da string, não se ignoram os espaços.
var person = "Diego";

var person-'Diego";

Nesse exemplo, quebra-se a linha de código dentro de uma string:

document.getElementByld.("demo".innerHTML = "Oi \
Diego! '';

Na terminologia Javascript, a palavra literal designa qualquer dado - valor fixo (não variável) -que se insere no código do script. Podem ser de diversos tipos, tais como: inteiros
(Ex: 250),
decimais (Ex: 3.1415), booleanos (Ex: true e false), strings2 (Ex: "Edson Arantes do
Nascimento"),
arrays (Ex: frutas = ["laranja", "pera", "goiaba", "morango"]) e objetos (Ex: Carro).

JS: VETORES (ARRAYS)

Os literais arrays, na sintaxe Javascript, são os conjuntos de zero ou mais valores,
separados por vírgula e envolvidos por colchetes ([ ]). Os valores contidos em um array recebem umÍndice sequencial começando com zero. A sintaxe é:
var nome-array = [iteml, item2, ...]

Um exemplo concreto seria:

var carros = ["Volks", "Ford",

Mas essa não é a única maneira de se criar um vetor, podemos também utilizar o operador new.
var carros = new Array("Volks", "Ford", "BMW");

2 Strings podem vir com aspas simples ou duplas.

y 79

/

JS: SAÍDA DE DADOS

Professor, como eu faço para manipular os elementos HTML? Para acessar, devemos utilizar o método document.getElementByld(id). O atributo id deve ser usado para identificar o elementoHTML e innerHTML deve ser usado para se referir ao conteúdo do elemento. Observem a tag
<script> no exemplo abaixo! Ela busca pelo elemento HTML cujo id="demo".

<!DOCTYPE html>

<html>

<body>

<hl>Minha primeira Página Web</hl>

<p>Meu primeiro parágrafo</p>

<p id="demo''></p>

<script>

document.getElementByld.("demo").innerHTML = "Parágrafo modificado";

</script>

</body>

</html>

Trata-se do elemento <p>. Ele pega o conteúdo interno desse elemento e modifica o valor de seu atributo id para ''Parágrafo modificado". É possível também escrever diretamente no DocumentoHTML por meio do método writef). É recomendável utilizá-lo apenas para realizar testes,
na medida em que ele sobrescreve todos os elementos HTML. Bacana?
<!DOCTYPE html>

<html>

<body>

<hl>Minha primeira Página Web</hl>

<p>Meu primeiro parágrafo.</p>

<script>

document.write("Meu segundo parágrafo");

</script>

</body>

</html>

JS: EVENTOS

O Javascript é bastante utilizado com eventos. Como assim, professor? Um evento é uma ação capaz de disparar uma reação. Clicar em um link ou colocar o ponteiro do mouse sobre um elemento podem ser considerados eventos. Ao clicar em um link, desencadeamos uma reação que poderá ser a de abrir uma nova página. Ao colocar o ponteiro do mouse sobre um elemento,podemos alterar sua opacidade.

x y 79
/

Eventos são bastante utilizados em Javascript e viabilizam a interatividade em uma página web. Na verdade, eventos viabilizam a própria existência do Javascript. Sem eles, não teríamos como fazer funcionar os scripts. Há uma gama imensa de possibilidades de eventos3! Ele permite a execução de funções quando eventos são detectados. Vamos ver como ele funciona:
<button onclick='getElementByld("demo")*innerHTML=Date()'>The Time is?</button>

No exemplo acima, quando o usuário clicar no botão, será informada a data e hora atual. Oresultado é mostrado abaixo:

Result:

| Thetimeis? |

Mon Aug 18 2014 15:42:02 GMT-0300 (Hora oficial do Brasil)

Observem que o Javascript modifica o conteúdo do elemento com id-"demo".

Por fim, vamos falar rapidamente do Unobstrusive JavaScript. Antes do CSS,
colocavam-se elementos de apresentação dentro dos elementos HTML. O CSS veio e mudou esse paradigma,separando a apresentação da estruturação, em um arquivo separado. Da mesma forma, antes doJavaScript, colocavam-se eventos e outros elementos de integração dentro dos elementos
HTML.
O Unobstrusive JavaScript veio e mudou esse paradigma, separando a integração da estruturação,em um arquivo separado.

Dessa forma, é possível separar o comportamento da marcação, reutilizar código,
realizar melhoria contínua, melhorou a detecção do código JavaScript e o suporte a cache. Dessa forma,desenvolvedores podem escrever códigos mais fáceis de manter e depurar.

Há uma biblioteca JavaScript que ajuda a criar interfaces de usuário ricas e responsivas relacionadas a um modelo de dados subjacente: chama-se Knockout! Ele permite associar facilmente elementos DOM com um modelo de dados usando uma sintaxe concisa e legível.Ademais, quando qualquer coisa muda o estado de seu modelo de dados, a interface de usuário é atualizada automaticamente.
Ele permite também configurar implicitamente cadeias de relacionamentos entre dados do modelo para transformá-los e combiná-los; e é capaz de gerar rapidamente sofisticadas interfaces de usuário aninhadas em função de seu modelo de dados. Galera, ele implementa o padrãoMVC, é livre, bem documentado, pequeno, leve e suportado pelos navegadores mais populares.
3 Eventos podem ser disparados pelo usuário (Ex: onclick - usuário clica em um elemento qualquer da página) ou independente de interferência do usuário (Ex: onload - quando um documento é carregado).
y 79

/

Eu sei, isso é tudo muito abstrato. Vamos ver um exemplo para vocês entenderem melhor: imagine um carrinho de compras de uma página de e-commerce (Ex: Netshoes). Quando o usuário deleta um item do carrinho, você tem que remover o item do modelo de dados (back-end), remover o elemento HTML associado no carrinho de compras (front-end), além de atualizar o preço total.
Podemos escrever event handlers e event listeners para rastrear essas dependências ou simplesmente podemos utilizaro Knockout. Ele fornece uma maneira simples e conveniente para gerenciar esse tipo complexo de interface orientada a dados. Em vez de rastrear mudanças no estado do modelo de dados manualmente, cada elemento do HTML automaticamente atualiza oDOM.

Apesar de ter muitas similaridades com tecnologias como jQuery, Prototype, MooTools e
Ajax, seu objeto não é apresentar animações, manipular eventos ou criar funcionalidades assíncronas. Seu foco principal está em projetar interfaces de usuário escaláveis e orientadas a dados,em que eu posso manipular modelo de dados e visão sem perda de referências. Chega de plug-ins...
Galera, assim como outras linguagens de programação, a imensa maioria das questões deJavaScript pergunta sobre tags e é inviável passar na aula dezenas e dezenas de tags. Logo, não vou passá-las aqui antes, vou passá-las durante os exercícios. Dessa forma, vocês aprendem na prática e descobrem quais são as mais frequentes. Bacana?
(BANESTES - 2021) Considere o código javascript a seguir:

let txt =

function funcao(value, index, array) {
if (index % 2 == 0) {txt += value};

}

function xpto (x) {
x.forEach(funcao);
return txt;

}

alert (xpto([0, 1, 1, 2, 3, 5]));

A execução desse código provoca a exibição de:
a) 011235

b) 013

c) 125

d) 532110

e) null

Comentários: pessoal, estamos utilizando na execução do código o index, então este é concatenado através do método forEach em cada elemento do array. Toda vez que invocamos a função, essa recebe um valor como parâmetro, o índice e a lista. Oprimeiro elemento que temos é:

value = o;
index = o;

array = [o,i,i,2,3,5]

if(o % 2 == o){ Zero dividido por 2 = o txt += 0 Temos a string txt concatenada com 0
No próximo elemento, chamamos a função de novo:

value = í;
index = í;

array = [0,1,1,2,3,51

if(i % 2 == o){ ¥2 = 0.5, logo não entremos na seleção, já que a divisão é diferente de zero.

Próximo elemento:

value = í;
index = 2;

array = [0,1,1,2,3,51

if(2 % 2 == o){ 2/2, 0 resto da divisão por 2 = 0, logo txt += 1 (a string txt é concatenada com 1,
ficando: 01
Quando realizamos de novo com index = 3, teremos: 013. Logo, a Letra B é a correta (Letra B).

(BANESTES - 2021) Considere o código javascript a seguir:

document.getElementByld('demo').innerHTML = Date()

Numa página web na qual esse código seja aplicado, o elemento que é compatível com a estrutura do comando para receber a data corrente é:
a) <p "demo">H</p>

b) <p class="demo">H</p>

c) <p id="demo">H</p>

d) <p js="demo">H</p>

e) <p onclick="demo">H</p>

Comentários: para receber a data corrente devemos passar o parâmetro recebido no GET:

document.getElementByld('demo').innerHTML = Date()

então 0 correto é:

<p id="demo">H</p>

(Letra C).

x y 79
/

QUESTõES CoMENTADAS - JS

í. (ESAF/CGU - 2012) Variáveis Javascript contêm:

a) um identificador, escopo e um tipo de dados específico.

b) um contextualizador, localizador e um tipo de dados específico.

c) um identificador, parâmetro e um tipo de escopo.

d) um delimitador, escopo e um referenciador.

e) um identificador, extensão e um ponteiro.

Comentários:

Em JavaScript, as variáveis têm identificador, escopo e tipo. Qual a pegadinha? A
pegadinha é que o tipo não é obrigatório - JavaScript é fracamente tipada.
Gabarito: Letra A

2. (FGV / SENADO - 2008) Em relação ao JavaScript, não é correto afirmar que:

a) é uma linguagem script que só pode ser usada em páginas HTML.

b) proporciona aos desenvolvedores de páginas web uma linguagem de programação.

c) é uma linguagem interpretada.

d) pode ser usada para criar cookies.

e) pode adicionar interatividade nas páginas html.

Comentários:

(a) Errado, ela pode ser utilizada com outras linguagens; (b) Correto, é mais uma alternativa para os desenvolvedores; (c) Correto, Javascript é uma linguagem de script e interpretada; (d) Correto,pode criar, ler e deletar cookies; (e) Correto, ele ajuda bastante a melhorar a interatividade das páginas HTML.
Gabarito: Letra A

3. (FGV / DPE-RO - 2015) As linguagens de programação utilizadas em programação frontend e back-end são, respectivamente:
a) Javascript e Java;

b) PHP e Javascript;

c) Python e Javascript;

d) PHP e Java;

e) C++ePHP.

Comentários:

Grosso modo, o front-end trata da interface de interação com o usuário e o back-end trata das regras de negócio do sistema. Portanto, vamos julgar: (a) Front-end e Back-end; (b)Back-end e
Front-end; (c) Back-end e Front-end; (d) Back-end e Back-end; (e) Back-end e Back-end.

Gabarito: Letra A

4. (CONSULPLAN /TRF 2-2017) Brendan Eich desenvolveu a primeira versão do JavaScript para o browser Mozilla, em 1995. A ideia era que a linguagem tivesse uma sintaxe parecida com Java,utilizando até mesmo alguns objetos e métodos com nomes iguais. Dessa forma,
a sintaxe correta para a inicialização de um array em Javascript corresponde à questão:
a) var array = [16, 34, 36, 42, 50, 58].

b) lnt[ ] array = [16, 34, 36, 42, 50, 58].

c) int array[ ] = [16, 34, 36, 42, 50, 58].

d) var array = int[16, 34, 36, 42, 50, 58].

Comentários:

Para declarar arrays explicitamente, a sintaxe utilizada é var nome_do_array = [item_i, item_2,

Gabarito: Letra A

5. (CONSUPLAN/ TRF2 - 2017) Em javascript, eventos são chamadas de código que ocorrem quando o usuário ou o browser executam determinadas ações. Existem eventos para quando o usuário clicar em algum lugar, para quando mover o ponteiro do mouse sobre uma região ou quando o ponteiro do mouse sairdessa região. Os eventos que compreendem carregamento de janela e alteração em um campo são representados respectivamente pelos comandos:
a) onload e onclick b) onload e onchange c) onchange e onreload d) onclick e onexchange
Comentários:

PROPRIEDADES | DESCRIÇÃO

onload onclick onchange
Indica o carregamento da janela.
Indica um clique em algum objeto.

Indica alteração em um campo de um objeto.

x y 79
/

onreload onexchange
Não existe.
Não existe.

Conforme a tabela acima, Onload indica o carregamento da janela e Onclick indica um clique em algum objeto.
Gabarito: Letra B

6. (FGV/ IBGE - 2016) Uma página contém o seguinte código JavaScript:

function teste() {
var letras = [] ;
grupolnicial: {

letras.push('A');

letras.push('B');
break grupolnicial;
letras.push('C');

}

letras.push('D');

letras.push('E');
return letras.join;

}

O resultado esperado é:

a) A,B

b) A,B,C

c) A,B,D,E

d) A,B,C,D,E

e) D,E

Comentários:

O comando break termina a execução do escopo atual e o código continua a ser executado em seu escopo mais externo. Nesse caso, a linha letras.push('C'); não será executada.
Gabarito: Letra C

7. (FGV / IBGE - 2016) Um website foi programado para exibir o nome do usuário no canto da tela através do seguinte código HTML:
<p id="cliente">usuário</p>

Considerando que o nome está armazenado na variável "meuNome", a sintaxe correta emJavascript para trocar a palavra "usuário" pelo conteúdo da variável é:

/ 79

/

a) document.getElementByld(cliente).innerHTML - "meuNome"

b) document.getElement("cliente").innerHTML = meuNome c) document.getElementByName(cliente).innerHTML = meuNome d) document.getElementByld("cliente").innerHTML = meuNome e) document.getElementByld(meuNome).innerHTML = "cliente"
Comentários:

Para obtermos uma referência a partir de um id, utilizamos o método getElementByld do objeto document e, para acessar seu conteúdo html, usamos a propriedade innerHTML. Como o valor que queremos está na variável meuNome, o correto será:
document.getElementByld("cliente").innerHTML = meuNome (Sem as aspas!)

Gabarito: Letra D

8. (FGV / IBGE - 2016) Para a produção de um website responsivo com grande quantidade de textos e imagens, as técnicas mais eficientes se baseiam na aplicação de:
a) grades fixas e dimensionadas em unidades absolutas, imagens dimensionadas em unidades absolutas e posicionadas de modo fluido, e JavaScript para alterar as regras de estilo com base na resolução de tela b) grades fluidas e dimensionadas em unidades absolutas, imagens flexíveis limitadas por elementos de contenção e posicionadas em unidades absolutas, e JavaScript para alterar as regras de estilo com base na resolução de tela c) grades fluidas e proporcionais, imagens flexíveis limitadas por elementos de contenção e dimensionadas em unidades relativas, e media queries para alterar as regras de estilo com base na resolução de tela d) grades fixas e proporcionais, imagens fixas e dimensionadas porJavascript, e media queries para alterar as regras de estilo com base na resolução de tela e) grades fluidas, imagens flexíveis limitadas por elementos de contenção, e JavaScript para posicionar todo o conteúdo de acordo com a resolução de tela.
Comentários:

Um website responsivo deve adaptar-se a qualquer tamanho de tela, desde um monitor de muitas polegadas até um celular. Para isso, podemos destacar algumas propriedades de um website
/ 79

/

responsivo. Grades (divs e outros elementos) fluidas e proporcionais, distribuindo o conteúdo de acordo com o tamanho da tela.
Imagens de tamanho relativo para que não fiquem nem muito pequenas e ilegíveis, e nem muito grandes e ultrapassem o tamanho da tela. Media queries! que permitem o uso de diferentes regras de estilo para cada tamanho de tela.
Gabarito: Letra C

9. (FGV / IBGE - 2016) Com a introdução do HTML5, diversas novas APIs Javascript
(Application
Programming Interfaces) foram disponibilizadas, aumentando consideravelmente a quantidade de recursos disponíveis para a produção de páginas web. São APIs exclusivas do HTML5:
a) múltiplas colunas de texto, transformações 2D/3D e RWD (Responsive Web Design).

b) armazenamento em nuvem, suporte a telas de toque e SSL (Secure Sockets Layer)

c) acesso a câmeras em dispositivos móveis, suporte a streaming de vídeo e SSE
(Streaming
SIMD Extensions)

d) armazenamento local, geolocalização e SSE (Server-Sent Events)

e) redimensionamento dinâmico de imagens, detecção de resolução de tela e RWD
(Responsive
Web Display)

Comentários:

Diversas APIs foram disponibilizadas com o HTML5, dentre elas. Armazenamento local, onde possível armazenar variáveis no navegador; Geolocalizalção, para localização do cliente; e SSE(Server-Sent Events), onde é possível que a página receba atualizações de eventos do servidor.

Gabarito: Letra D

io.(FGV/TCM-SP -2015) Em Javascript, considere o trecho de código a seguir:

/ 79

/

fimction base (x)

{

return funaticm produto4y}

{

retum x * y;

}

I

var f = base (2} ;
var g = base(-l) ;

Após as duas atribuições, supondo que os valores de f e g não mudem, a avaliação da expressão f(2) + g(-i) produzirá o valor:
a) 5;

b) 4;

c) 3;

d) 2;

e) í.

Comentários:

Podemos pensar da seguinte maneira: f = base(2) retorna a função produto(y) {return
2*y;}, logo f(y) = 2*y e f(2) = 4. De forma análoga temos:
g = base(-i) retorna a função produto(y) {return -i*y}, logo g(y) = -y e g(-i) = 1.
Com isso concluímos facilmente que f(2) + g(i) = 5.

Gabarito: Letra A

n.(IESES / IFC-SC - 2015) Analise as afirmativas a seguir sobre o JavaScript 1.8 e assinale a alternativa correta:
I. A maneira mais comum de se declarar uma classe em JavaScript com o nome "Cachorro"
seria da seguinte forma: class Cachorro { }

II. A maneira mais comum de se instanciar um objeto em JavaScript a partir da classe
"Cachorro" seria da seguinte forma: Cachorro cachorro = new Cachorro;

y 79

/

III. Tanto comentários de uma linha com barras duplas (//...) quanto comentários em blocos com barra e asterisco (/* ... */) são suportados em JavaScript.
a) As afirmativas I, II e III são verdadeiras.

b) Somente a afirmativa I é verdadeira.

c) Somente as afirmativas I e III são verdadeiras.

d) Somente a afirmativa III é verdadeira

Comentários:

(I) Errado, a diretriz class não existe no JavaScript. A maneira mais comum seria var
Cachorro =
function() {}; (II) Errado, a declaração de qualquer tipo é realizada utilizando var.
A maneira mais comum seria var cachorro = new Cachorro(); (III) Correto, o item está perfeito - ambos são suportados.
Gabarito: Letra D

i2.(IESES / IFSC-2015) Uma determinada linha de código JavaScript 1.8 se lê da seguinte forma:
var novoCachorro = new Cachorro();

Assinale a alternativa que apresenta um trecho de código que deve ser inserido antes da linha demonstrada, de forma que o código seja sintática e semanticamente válido:
a) function(e) {e.class(Cachorro);}

b) var Cachorro = function() { }

c) class Cachorro {function(e) {e.instanceof(Cachorro);}}

d) class Cachorro { }

Comentários:

A linha apresentada no enunciado mostra uma instanciação da classe Cachorro. Para que isso seja possível, precisamos que a classe seja declarada. A maneira correta de declarar uma classe emJavascript é var Cachorro = function() {}.

Gabarito: Letra B

13.OESES / IFSC-2015) Observe o código javascript abaixo:

/ 79

/

<script type="text/java5cript">

var cidades = ["Sao Paulo". "Criciúma", "Curitiba", "ItajaP, "Rio do Sul", "Erechim"];
forjvar i = 0; i < cidades de ngth; i++}[

str = cidades[i];
if(strlength == S){

document.write(str);

docum ent .wrrte("<b r>");

}

}

<7script>

O resultado da execução desse script é:

a) Criciúma, Curitiba b) Criciúma, Curitiba c) São Paulo Criciúma Curitiba Itajaí Rio do Sul Erechim d) Criciúma Curitiba
Comentários:

O script acima simplesmente percorre todos os itens do Array cidades e escreve no documento aqueles em que otamanho do item é igual a 8. Vale notar que eletambém adiciona uma quebra de linha (<br>) entre cada escrita.
Gabarito: Letra A

i4.(FGV/TCE-SE-20i5) Em um programa Javascript, encontra-se o seguinte comando:

var x = 3 + "4";

Após a execução deste comando, a variável x conterá:

a) a cadeia "34";

b) número 34;

c) a cadeia "7";

d) número 7;

e) o mesmo de antes da execução do comando, devido a um erro referente à conversão de tipos

Comentários:

Em JavaScript, o operador + é utilizado para concatenação de strings e, se algum dos operandos for uma string, ele irá converter qualquer outro operando em string. Isso se chama conversão implícita.
Gabarito: Letra A

/ 79

/

i5.(FGV/TCE-SP-20i5) Em uma página HTML, é declarado o seguinte formulário:

cfonn id-"dados'r action-^script.php"

method=llFaST">

cinput type- " s ubmi t" name-11S ubrii t"

value= " ENVI AR11 / >
cinput type=11 h 1dden" id="tamanho11

name=" TAMANHO"

value=" "7>

</fonn>

O valor do campo TAMANHO deverá ser preenchido por uma função Javascript, que terá acesso a ele através do construtor:
a) document.getElementByld("dados").tamanho.value;

b) document.getElementByld("hidden").value;

c) document.getElementByld("tamanho").value;

d) document.getElementByld("input").tamanho, value;

e) document.getElementByld("form").tamanho.value.

Comentários:

Para obtermos uma instância de um objeto a partir de seu id, utilizamos o método document. getElementByld("id")
e, para acessar seu valor, utilizamos o atributo value. Logo, para acessarmos o valor do campoTAMANHO utilizamos document.getElementByld("tamanho").value;.
Gabarito: Letra C

i6.(NUCEPE / SEFAZ-PI - 2015) Laços são importantes construções em linguagens de programação. Qual tipo de laço (loop) NÃO possui suporte em JavaScript?
a) For.

b) For/in.

c) Repeat/until.

d) While.

e) Do/while.

/ 79

Comentários:

A sintaxe do JavaScript não suporta laços do tipo Repeat/until. Todos das outras alternativas são suportados. Podemos ver alguns exemplos de utilização dos laços abaixo:
for (int a=0; a<10; a++) { ... }
for (element in array) { ... }
while (a == true) { ... }

do { ... } while (a < 10);

Gabarito: Letra C

17. (MPE-RS / MPE-RS -2015) Dado o código HTML abaixo:

<!DOCTYPE html>

<html>

<body>

<p>UM</p>

<p>DOIS</p>

<p>TRES</p>

<script type='rtext/javascript">
window.onload = function() {

}

</script>

</body>

</html>

Quais dos comandos Javascript listados abaixo podem ser colocados no espaço indicado pelos pontos para que a página, ao ser carregada, altere somente a cor do texto "UM" para azul?
1. document.getElementsByTagName("p")[o].style.color = "#ooooFF";

2. document.getElementsByTagName("p")[o].color = "#ooooFF";

3. document.getElementsByTagName("p").item(o).style.color = "#ooooFF";

a) Apenas 1.

b) Apenas 2.

c) Apenas 3.

d) Apenas 1 e 3.

e) í, 2 e3.

Comentários:

O método document.getElementsByTagName("p") retorna uma coleção de objetos do tipoHTMLCollection. Para acessarmos o primeiro elemento da coleção, podemos utilizar tanto a sintaxe de acesso por índices, [o], quanto o método item(o). Uma vez que obtivermos o objeto, para mudar sua cor é necessário acessar primeiro o atributo style e depois o atributo color,.style.color.

Gabarito: Letra D

i8.(MPE-RS / MPE-RS - 2015) Dado o código Javascript abaixo:

<script type='rteKt7javascript''>
var numeros =

["UnT/Llois"/1 res","Quatro"];

numeros.pop();

nu m e ros. pus h (" Dez");
numeros.shiftO;

d oc u me nt. wri te (n um ei os) ;

</script>

Quando o bloco for inserido no corpo de uma página HTML e executado no navegador, o que será exibido na tela?
a) Dois,Tres,Dez b) Quatro,Dez,Dois,Tres c) Dois,Tres,Dez,Um d) Dez,Dois,Tres e) Um,Dois,Tres,Dez,Dez
Comentários:

Vejamos a função de cada método utilizado:

pop() remove o último item do array ("Quatro");
o Resultado: "Um", "Dois", "Tres".

push() adiciona um item ao final do array (Dez); e o Resultado: "Um", "Dois", "Tres", "Dez".
shift() remove o primeiro element do array (Um).

/ 79

/

Resultado: "Dois", "Tres", "Dez".

Gabarito: Letra A

i9.(MPE-RS / MPE-RS -2015) Dado o código Javascript abaixo:

<script type="text/javascript">
function Aluno() {

var nome = "Ze";

var dados = {

idade : 18,

peso : 75

};

this.qetDados = function() {

return dados;

};

}

var x = new Aluno();
var y = x.qetDados();

document.write(x.nome + " ");
document.write(y.idade + " ");
y.idade += 2;
document.write(x.getDados(). idade);

</script>

Quando o bloco for inserido no corpo de uma página HTML e executado no navegador, o que será exibido na tela?
a) undefined undefined 20

b) undefined 18 20

c) Ze 18 18

d) Ze 18 20

e) undefined 18 18

Comentários:

Vamos analisar as linhas onde há escrita:

document.write(x.nome + "");

- O objeto x, da classe Aluno, não possui a propriedade nome (sua variável dados,
sim), portanto essa linha imprime undefined.
document.write(y.idade + "");

- Até aqui é bem simples: y tem o valor de dados, dentro de x. Portanto y.idade é igual a 18.
document.write(x.getDados(). idade);

- Aqui está a verdadeira questão, o fato de mudar o valor de y.idade afetará o valor de x.dados.idade? A resposta é sim, e vamos ver o porque.
Para isso, precisamos separar em dois casos de atribuição com o operador =:

1) Com valores primitivos, o operdor = funciona por valor. Vejamos um exemplo:
var name = "Carlos"; varfirstName = name;

name = "Carla";

console.log(name); // "Carla"
console.log(firstName); // "Carlos"

Nesse caso, a variável firstName recebe uma cópia de name, portanto alterar o valor de name não irá alterar o valor de firstName.
2) Com objetos, o operador = funciona por referência. Vejamos um exemplo:

var myName = {firstName: "Carlos"}; var identity = myName;
myName.firstName = "Carla";
console.log(myName.firstName); // "Carla"
console.Iog(identity.firstName); // "Carla"

Nesse caso, a variável firstName recebe uma referência de name, portanto alterar o valor de name irá alterar o valor de firstName.
Voltando para nossa questão, como se trata de um objeto, a atribuição é feita por referência, ou seja, quando alteramos o valor de y.idade também alteramos o valor de x.getDados().idade.
Gabarito: Letra B

2o.(MPE-RS / MPE-RS -2015) Quais são os valores de saída do código Javascript abaixo?

y 79

/

Cscript ty pe="text/j avascri pt " >

<!—

vai x = 1;
whiile (x < 20)

{

if (x == 5){
break;

}

x = x + 1;

document.write( x + "<br />");

}

//->

</sc npt>

a) 2-3-A-5

b) 2-3-4

c) 1-2-3-4-5

d) 1-2-3-4

e) 0-1-2-3-4

Comentários:

Pelo loop principal, while (x < 20), a variável x percorreria os valores de 1 a 19, porém quando x chega a 5 o código sai do loop devido ao comando break. Logo, os valores de x são 1, 2,3 e 4. Como o valor de x é incrementado antes da impressão, os valores impressos são 2, 3, 4 e 5. Vale ressaltar que as linhas <!—e // -> não alteram em nada o código. Além disso, como há uma impressão da tag <br />,a saída seria como os números linha a linha, e não lado a lado.

Gabarito: Letra A

21. (MPE-RS / MPE-RS - 2015) Dado o seguinte código JSON com Javascript:

var text = '{ "employees"' : [' 4-

'{ "firstName':"Johnn , nlastNamen:"Doe" +

'{ "firstNamen:"Arma" , "lastNamé":'SmittT +
'{ ,,firstNamen:1,Peter'' , " lastNamé" :'Jones" } ]}';

É correto afirmar que o código apresentado acima:

a) concatena três string formando uma classe e atribui dados a ela.

b) concatena três objetos formando uma classe e atribui dados a ela.

c) divide um objeto em três strings e atribui dados a elas.

d) concatena três arrays em um objeto e atribui dados a ele.

y 79

/

e) cria um array com três objetos e atribui ciados a eles

Comentários:

ENTRADA SAÍDA

var text = '{"employees" : [' +

'{ "firstName":"3ohn", "lastName":"Doe" }/ +

'{ "firstName":"Anna", "lastName":"Smith" },' +

'{ "firstName":"Peter", "lastName":"Jones" } ]}';

{"employees" : [

{ "firstName":"3ohn", "lastName":"Doe" },

{ "firstName":"Anna", "lastName":"Smith" },

{ "firstName":"Peter", "lastName":"Jones" }

]}

Analisando a entrada com syntax highlighting, podemos ver facilmente que se trata de uma concatenação de três strings, porém não forma uma classe, e sim um array employees com três objetos que possuem os atributos firstName e lastName.
Vale notar que a variável text é apenas uma string, e que para que seja transformada no que a banca queria seria necessário usar JSON.parse(text) para obter-se o array.
Gabarito: Letra E

22. (UFG / AL-GO - 2015) Leia o trecho em Javacript a seguir:

Qual é a saída da execução desse trecho de código Javascript?
a) 123

b) 456

c) 156

d) 423

Comentários:

Para responder essa questão, precisamos entender como funcionam os índices de arrays.
Quando o índice é um objeto, o JavaScript irá primeiro converter o índice para uma string,e depois utilizá-
lo. Vejamos um exemplo:

00 SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital) 28

var a = {};

var b = [1, 2, 3];

a [b] = ' oi ' ;

No exemplo, a[b] retorna 'oi', a[[i, 2, 3]] retorna 'oi' e a[i, 2, 3] retorna 'oi'.
Isso porque todos os argumentos quando transformados em string retornam a mesma coisa: b.toStringO = '1, 2, 3', [1, 2,
3].toString() = '1, 2, 3' e '1, 2, 3'.toString() = '1, 2, 3'.

No código da questão acima, b.toStringO = '[object Object]' e c.toStringO - '[object
Object]', logo para o array a, os índices b e c são iguais, como podemos ver no output do console abaixo:
> a[b] = 123;

> a

< {[object Obj ect] : 123}

> a[c] = 456;

> a

< {[obj ect Obj ect]: 456}

Logo, chamar a[b] ou a[c] seria o mesmo que chamar a['[object Object]'] e portanto ambos retornariam 456 ao final do código.
Gabarito: Letra B

23. (FGV / BANESTES -2021) Considere o código javascript a seguir:

let txt =

function funcao(value, index, array) {
if (index % 2 == 0) {txt += value};

}

function xpto (x) {
x.forEach(funcao);
return txt;

}

alert (xpto([0, 1, 1, 2, 3, 5]));

A execução desse código provoca a exibição de:
a) 011235

b) 013

c) 125

/ 79

/

d) 532110

e) null

Comentários:

Pessoal, estamos utilizando na execução do código o index, então este é concatenado através do método forEach em cada elemento do array. Toda vez que invocamos a função, essa recebe um valor como parâmetro, o índice e a lista. O primeiro elemento que temos é:
value = 0;
index = o;

array = [0,1,1,2,3,5]

if(o % 2 == o){ Zero dividido por 2 = 0

txt += o Temos a string txt concatenada com 0

No próximo elemento, chamamos a função de novo:

value = i;
index = 1;

array = [0,1,1,2,3,5]

if(i % 2 == o){ ¥2 = 0.5, logo não entremos na seleção, já que a divisão é diferente de zero.

Próximo elemento:

value = 1;

index = 2;

array = [o,i,i,2,3,5]

if(2 % 2 == o){ 2/2, o resto da divisão por 2 = 0, logo txt += 1 (a string txt é concatenada com 1,ficando: 01

Quando realizamos de novo com index = 3, teremos: 013. Logo, a Letra B é a correta.

Gabarito: Letra B

24.(FGV / BANESTES -2021) Considere o código javascript a seguir:

document.getElementByld('demo').innerHTML = Date()

Numa página web na qual esse código seja aplicado, o elemento que é compatível com a estrutura do comando para receber a data corrente é:
a) <p "demo">H</p>

/ 79

/

b) <p class="demo">H</p>

c) <p id="demo">H</p>

d) <p js="demo">H</p>

e) <p onclick=,,demo">H</p>

Comentários:

Galera, para receber a data corrente devemos passar o parâmetro recebido no GET:

document.getElementByld('demo').innerHTML = Date()

Então, o correto é:

<p id="demo">H</p>

Gabarito: Letra C

25. (CESPE / PGDF - 2021) Julgue o item a seguir, referente a linguagem de scripts.

<input type='text' id='a' value=,5l>

<br>

<input type-^text1 id='b' value^Z^

<br>

<input type-^text1 idstc' >

<sGript>
document.getElementByld(1c1).values(document-

getElejnentByld (* a *) * value+document . getElement
Byld(1b*).value);

</script>

</html>

Em um navegador Internet com JavaScript habilitado, esse código apresentará o resultado a seguir

Comentários:

Pessoal, os inputs são texto e valores, teremos então os textos sendo concatenados e três inputs de valores, como o terceiro input é vazio, concatena-se com os anteriores, 5 e 2, por isso apresenta texto 52. Mas tem uma indução a erro na questão, que é apresentar o resultado em forma de tabela,todavia a banca desconsiderou esse fato e entendeu como certa a apresentação dos respectivos resultados (5,2, 52) em formato de tabela.
x y 79
/

Gabarito: Correto

26.(CESPE / SEED-PR - 2021) resultado = (x for x in [5.-2])

Assinale a opção que apresenta o resultado da execução do código CoofeeScript precedente.
a) 5,5

b) 5,4,3,2

c) 2,2,2,2,2

d) 5,3,1

e) 4,3

Comentários:

CoofeeScript é uma linguagem compilada do JS, então o que aprendemos com JS se aplica aqui,ok?

Temos de forma bem simples um array, onde o resultado é equivalente a (x para todo x dentro do intervalo de (5 a 2), logo termos: 5,4,3,2, dentro do intervalo 582. Simples, não é verdade?
Gabarito: Letra B

27. (CESPE / SEED-PR - 2021) JavaScript trabalha com números usando os operadores aritméticos fornecidos pela própria linguagem. No entanto, a linguagem aceita operações matemáticas mais complexas por meio de um conjunto de funções e constantes definidas como propriedades do objeto Math.
Comentários:

Perfeito! O objeto Math define as funções e constante para operações dentro da linguagem JS.

Gabarito: Correto

28.(CESPE / SEED-PR - 2021) A opção Match.ceil () apresenta a função que permite realizar, emJS, a operação matemática de arredondar para cima o número 1,17, obtendo-se o valor 2.

Comentários:

Perfeito! Quando utilizamos o Match.ceil arredondamos para cima o valor do número 1.17,resultando em 2. Se fosse utilizado o Match.round () teríamos o arredondamento para o inteiro mais próximo, ou seja, 2.0.
Gabarito: Correto

29.(CESPE / ME - 2020) Nos padrões web, as camadas deverão ser separadas de acordo com o objetivo para o qual elas foram desenvolvidas. Criar páginas em camadas lógicas é uma boa prática: xHTML, folhas de estilo CSS e JavaScript são voltadas, respectivamente, para as camadas de conteúdo, de apresentação visual do conteúdo e de comportamento dos elementos.
Comentários:

Pessoal, não é objeto dessa aula tratar de xHTML e CSS, porém a questão abordou,
logo temos que xHTML é responsável pelo conteúdo, CSS pela apresentação do conteúdo e o JScuidará da interação ou comportamento do conteúdo da página web. Dito isso, é uma boa prática utilizar xHTML, CSS e JS nas respectivas funções apresentadas.
Gabarito: Correto

30. (CESPE / TJ-AM - 2019) JavaScript é uma linguagem de programação orientada ao desenvolvimento da interface para aplicações web, cujo código-fonte é compilado pelo servidor antes de sua execução.
Comentários:

JS é uma linguagem interpretada, assim como PHP e Python. Exemplo de linguagem compilada seria o C++.
Gabarito: Errado

31. (CESPE / SLU-DF - 2019) Uma função JavaScript é um bloco de código utilizado para executar tarefas repetidas e é definida pela palavra-chave public seguida por um nome seguido por parênteses ().
Comentários:

Pessoal, quando apresentamos a função JS em código para execução de tarefas repetidas
(loop),
demonstramos a estrutura:

<script>

function minhaFuncao() {

document.getElementByld("demo").innerHTML = "Minha primeira função JavaScript!";

}

</script>

/ 79

Ou seja, a função se inicia pelo function e não pela palavra public, com argumento
(no exemplo temos minhaFuncao), seguido de parenteses.
Gabarito: Errado

32.(CESPE / SLU-DF - 2019) O JSX (JavaScript Syntax Extension) é de uso obrigatório no React e permite inserir a interface do usuário no código JavaScript.
Comentários:

O React (também denominado React. js ou ReactJS) é uma biblioteca JavaScript de código aberto com foco em criar interfaces de usuário (frontend) em páginas web. É mantido peloFacebook,
Instagram, outras empresas e uma comunidade de desenvolvedores individuais. Dito isso,
qual o problema da questão: O JSX (JavaScript Syntax Extension) NÃO é de uso obrigatório noReact, ou seja, o React NÃO requer o uso do JavaScript Syntax Extension. Dificilmente vocês verão uma questão escrito "é obrigatório" e estará correta.
Gabarito: Errado

33. (FCC / TRT11 - 2005) Em JavaScript, para declarar nomes de identificadores válidos utiliza-se:
a) somente número no primeiro caractere.

b) somente letra ou underscore no primeiro caractere.

c) qualquer tipo de caractere a partir do segundo caractere.

d) espaço entre caracteres a partir do segundo caractere.

e) uma palavra reservada do JavaScript

Comentários:

Para declarar nomes de identificadores, utiliza-se apenas letra ou underscore no primeiro caractere.
Gabarito: Letra B

34. (FCC / TRE-SE - 2007) O cliente JavaScript, quando se soltar um botão do mouse pressionado,invocará o evento:

a) MouseOver.

b) MouseDown.

c) MouseUp.

d) MouseMove.

e) MouseOut.

Comentários:

/ 79

/

PROPRIEDADES DESCRIÇÃO

onmouseover onmousedown onmouseup onmousemove onmouseout
O ponteiro é movido a um elemento ou a seus filhos.

O usuário pressiona 0 botão do mouse em um elemento.
O usuário solta 0 botão sobre um elemento.

O ponteiro se move quando se está sobre um elemento.

O usuário retira 0 ponteiro de um elemento ou de seus filhos.

Gabarito: Letra C

35. (FCC / MPE-SE - 2008) Uma função embutida na linguagem JavaScript que calcula o conteúdo de uma string denomina-se:
a) string.

b) eval.

c) number.

d) parselnt.

e) parseFloat

Comentários:

"The eval() function evaluates or executes an argument. If the argument is an expression, eval()evaluates the expression. If the argument is one or more JavaScript statements, eval()
executes the statements". Portanto, ela avalia e executa códigos dentro de uma string e apresenta o resultado,como podemos ver abaixo:

var x = 10;
var y = 20;

var a = eval("x

* y") + "<br>";

var b = eval("2 + 2") + "<br>";
var c = eval("x + 17") + "<br>"

var res = a + b + c;

O Resultado será: 200, 4 e 27.

Gabarito: Letra B

36.(FCC / TRT-i - 2014) O trecho de programa a seguir foi elaborado na linguagem
HTML com
JavaScript e será aberto por um navegador que as suporte.

<html>

<body>

<hi>Página Principal</hi>

/ 79

/

<form>
comando y

</form>

</body>

</html>

Página Principal

Nova Página

O comando que deve ser colocado no lugar do comando y, de modo que, ao se pressionar o botão Nova Página, seja aberta a página Pi.html, é:
a) <input type = "button" text="Nova Página" click="window.location='Pi.html'">

b) <input type="button" text="Nova Página" onclick = "window.location='Pi.html'">

c) <input type="onbutton" text="Nova Página" onclick = "window.location='Pi.html'">

d) <inputtype="button" value="Nova Página" onclick = "window.location='Pi.html'">

e) <input type="onbutton" value="Nova Página" click = "window.location='Pi.html'">

Comentários:

Bem, basta saber usar a tag <input>! Ela serve para receber dados. O
atributo com valor type="button" especifica um botão cujo nome é value="Nova Página" e o evento onclick ="window.location='Pi.html"' leva o usuário que clica nesse botão à página Pi.html

Gabarito: Letra D

37.(FCC / TRT-18 - 2008) Na linguagem JavaScript, os métodos de interface com o usuário que fazem parte do objeto window são apenas os denominados:
a) select, submit e confirm.

b) open, alert e write.

c) click, select e write.

d) open, submit e close.

e) alert, confirm e prompt.

Comentários:

Trata-se da última opção: alert, confirm e prompt.

/ 79

/

MÉTODOS DESCRIÇÃO

alertO
confirm ()
prompt ()

Exibe uma janela de alerta com um Botão Ok.

Exibe uma janela de diálogo com uma mensagem e os botões Ok e Cancel.
Exibe uma janela de diálogo à espera de uma entrada do usuário.

Gabarito: Letra E

38.(FCC / DPE-SP - 2010) As tecnologias Web utilizam linguagem de scripting JavaScript,
linguagem de scripting ASP e applets Java para incluir aplicações, respectivamente, no lado:

a) servidor, cliente e servidor.

b) cliente, servidor e cliente.

c) servidor, servidor e cliente.

d) cliente, cliente e servidor.

e) cliente, cliente e cliente.

Comentários:

JavaScript e Applets rodam no cliente e Scripting ASP roda no servidor.

Gabarito: Letra B

39.(FCC /TRT-20 - 2010) No JavaScript, a caixa de mensagem "Confirm":

a) permite que o usuário insira um nome e/ou um número dentro da caixa de texto.

b) Exibe apenas uma informação para o usuário.

c) Permite que o usuário insira um nome dentro da caixa de texto.

d) Permite que o usuário insira um número dentro da caixa de texto.

e) Solicita uma confirmação do usuário, positiva ou negativa.

Comentários:

A página em www.w3schools.com diz:

Press a button!

OK Cancelar

As caixas de diálogo de confirmação visam apenas exibir uma mensagem e pedir uma confirmação positiva ou negativa
Gabarito: Letra E

x y 79
/

/fO.(FCC -TRT-20 - 2010) É um método do objeto History:

a) Case.

b) Left.

c) Open.

d) Forward e) Hostname
Comentários:

O objeto History contém as URLs visitadas por um usuário.

MÉTODOS DESCRIÇÃO

back() Carrega a URL anterior do histórico.
forward() Carrega a próxima URL do histórico.

go() Carrega uma URL específica do histórico.

Gabarito: Letra D

y 79

/

LISTA DE QUESTõES - JS

í. (ESAF/CGU - 2012) Variáveis Javascript contêm:

a) um identificador, escopo e um tipo de dados específico.

b) um contextualizador, localizador e um tipo de dados específico.

c) um identificador, parâmetro e um tipo de escopo.

d) um delimitador, escopo e um referenciador.

e) um identificador, extensão e um ponteiro.

2. (FGV / SENADO - 2008) Em relação ao JavaScript, não é correto afirmar que:

a) é uma linguagem script que só pode ser usada em páginas HTML.

b) proporciona aos desenvolvedores de páginas web uma linguagem de programação.

c) é uma linguagem interpretada.

d) pode ser usada para criar cookies.

e) pode adicionar interatividade nas páginas html.

3. (FGV / DPE-RO - 2015) As linguagens de programação utilizadas em programação frontend e back-end são, respectivamente:
a) Javascript e Java;

b) PHP e Javascript;

c) Python e Javascript;

d) PHP e Java;

e) C++e PHP.

4. (CONSULPLAN /TRF 2-2017) Brendan Eich desenvolveu a primeira versão do JavaScript para o browser Mozilla, em 1995. A ideia era que a linguagem tivesse uma sintaxe parecida com Java,utilizando até mesmo alguns objetos e métodos com nomes iguais. Dessa forma,
a sintaxe correta para a inicialização de um array em Javascript corresponde à questão:
a) var array = [16, 34, 36, 42, 50, 58].

b) lnt[ ] array = [16, 34, 36, 42, 50, 58].

c) int array[ ] = [16, 34, 36, 42, 50, 58].

d) var array = int[i6, 34, 36, 42, 50, 58].

5. (CONSUPLAN/ TRF2 - 2017) Em javascript, eventos são chamadas de código que ocorrem quando o usuário ou o browser executam determinadas ações. Existem eventos para quando o usuário clicar em algum lugar, para quando mover o ponteiro do mouse sobre uma região ou quando o ponteiro do mouse sairdessa região. Os eventos que compreendem carregamento de janela e alteração em um campo são representados respectivamente pelos comandos:
y 79

/

a) onload e onclick b) onload e onchange c) onchange e onreload d) onclick e onexchange
6. (FGV / IBGE - 2016) Uma página contém o seguinte código JavaScript:

function teste() {
var letras = [] ;
grupolnicial: {

letras.push('A');

letras.push('B');
break grupolnicial;
letras.push('C');

}

letras.push('D');

letras.push('E');
return letras.join;

}

O resultado esperado é:

a) A,B

b) A,B,C

c) A,B,D,E

d) A,B,C,D,E

e) D,E

7. (FGV / IBGE - 2016) Um website foi programado para exibir o nome do usuário no canto da tela através do seguinte código HTML:
<p id="cliente">usuário</p>

Considerando que o nome está armazenado na variável "meuNome", a sintaxe correta emJavascript para trocar a palavra "usuário" pelo conteúdo da variável é:

a) document.getElementByld(cliente).innerHTML = "meuNome"

b) document.getElement("cliente").innerHTML = meuNome c) document.getElementByName(cliente).innerHTML = meuNome d) document.getElementByld("cliente").innerHTML - meuNome e) document.getElementByld(meuNome).innerHTML = "cliente"
8. (FGV / IBGE - 2016) Para a produção de um website responsivo com grande quantidade de textos e imagens, as técnicas mais eficientes se baseiam na aplicação de:
y 79

/

a) grades fixas e dimensionadas em unidades absolutas, imagens dimensionadas em unidades absolutas e posicionadas de modo fluido, e JavaScript para alterar as regras de estilo com base na resolução de tela b) grades fluidas e dimensionadas em unidades absolutas, imagens flexíveis limitadas por elementos de contenção e posicionadas em unidades absolutas, e JavaScript para alterar as regras de estilo com base na resolução de tela c) grades fluidas e proporcionais, imagens flexíveis limitadas por elementos de contenção e dimensionadas em unidades relativas, e media queries para alterar as regras de estilo com base na resolução de tela d) grades fixas e proporcionais, imagens fixas e dimensionadas porJavascript, e media queries para alterar as regras de estilo com base na resolução de tela e) grades fluidas, imagens flexíveis limitadas por elementos de contenção, e JavaScript para posicionartodo o conteúdo de acordo com a resolução de tela.
9. (FGV / IBGE - 2016) Com a introdução do HTML5, diversas novas APIs Javascript
(Application
Programming Interfaces) foram disponibilizadas, aumentando consideravelmente a quantidade de recursos disponíveis para a produção de páginas web. São APIs exclusivas do HTML5:
a) múltiplas colunas de texto, transformações 2D/3D e RWD (Responsive Web Design).

b) armazenamento em nuvem, suporte a telas de toque e SSL (Secure Sockets Layer)

c) acesso a câmeras em dispositivos móveis, suporte a streaming de vídeo e SSE
(Streaming
SIMD Extensions)

d) armazenamento local, geolocalização e SSE (Server-Sent Events)

e) redimensionamento dinâmico de imagens, detecção de resolução de tela e RWD
(Responsive
Web Display)

10. (FGV/TCM-SP -2015) Em Javascript, considere o trecho de código a seguir:

/ 79

/

fimction base (x)

{

return funaticm produto4y}

{

retum x * y;

}

I

var f = base (2} ;
var g = base(-l) ;

Após as duas atribuições, supondo que os valores de f e g não mudem, a avaliação da expressão f(2) + g(-i) produzirá o valor:
a) 5;

b) 4;

c) 3;

d) 2;

e) í.

n.(IESES / IFC-SC - 2015) Analise as afirmativas a seguir sobre o JavaScript 1.8 e assinale a alternativa correta:
I. A maneira mais comum de se declarar uma classe em JavaScript com o nome "Cachorro"
seria da seguinte forma: class Cachorro { }

II. A maneira mais comum de se instanciar um objeto em JavaScript a partir da classe
"Cachorro" seria da seguinte forma: Cachorro cachorro = new Cachorro;

III. Tanto comentários de uma linha com barras duplas (//...) quanto comentários em blocos com barra e asterisco (/* ... */) são suportados em JavaScript.
a) As afirmativas I, II e III são verdadeiras.

b) Somente a afirmativa I é verdadeira.

c) Somente as afirmativas I e III são verdadeiras.

d) Somente a afirmativa III é verdadeira i2.(IESES / IFSC -2015) Uma determinada linha de código JavaScript 1.8 se lê da seguinte forma:
var novoCachorro = new Cachorro();

/ 79

/

Assinale a alternativa que apresenta um trecho de código que deve ser inserido antes da linha demonstrada, de forma que o código seja sintática e semanticamente válido:
a) function(e) {e.class(Cachorro);}

b) var Cachorro = function() { }

c) class Cachorro {function(e) {e.instanceof(Cachorro);}}

d) class Cachorro { }

i3.(IESES/IFSC-20i5) Observe o código javascript abaixo:

<script type="text/javascripl">

var cidades = [São Paulo". "Criciúma", "Curitiba", "ItajaP, "Rio do Sul", "Erechim"];
forjvar i = 0; i < cidades de ngth; i++}[

str = cidades[i];
if(strlength == S){

document.write(str);

docum ent wrrte("<b r>");

}

}

<7script>

O resultado da execução desse script é:

a) Criciúma, Curitiba b) Criciúma, Curitiba c) São Paulo Criciúma Curitiba Itajaí Rio do Sul Erechim d) Criciúma Curitiba
14. (FGV/TCE-SE-20i5) E m um programa Javascript, encontra-se o seguinte comando:

var x = 3 + "4";

Após a execução deste comando, a variável x conterá:

a) a cadeia "34";

b) número 34;

c) a cadeia "7";

d) número 7;

e) o mesmo de antes da execução do comando, devido a um erro referente à conversão detipos

15. (FGV/TCE-SP-2O15) Em uma página HTML, é declarado o seguinte formulário:

y 79

/

<form id—"dados" action-"script.php"

method="POST">

<input type -11 s libmi t" n ame-113 ubmi t"

value= " ENVI AR" / >

<input type=" h 1dden" id="tamanho"

name=" TAMANHO"

value=" "7>

</f orm>

O valor do campo TAMANHO deverá ser preenchido por uma função Javascript, que terá acesso a ele através do construtor:
a) document.getElementByld("dados").tamanho.value;

b) document.getElementByld("hidden").value;

c) document.getElementByld("tamanho").value;

d) document.getElementByld("input").tamanho.value;

e) document.getElementByld("form").tamanho.value.

16. (NUCEPE / SEFAZ-PI - 2015) Laços são importantes construções em linguagens de programação. Qual tipo de laço (loop) NÃO possui suporte em JavaScript?
a) For.

b) For/in.

c) Repeat/until.

d) While.

e) Do/while.

17. (MPE-RS / MPE-RS -2015) Dado o código HTML abaixo:

<!DOCTYPE html>

<html>

<body>

<p>UM</p>

<p>DOIS</p>

<p>TRES</p>

<script type='rtext/javascript">
window.onloâd = function() {

}

</script>

</body>

</html>

Quais dos comandos Javascript listados abaixo podem ser colocados no espaço indicado pelos pontos para que a página, ao ser carregada, altere somente a cor do texto "UM" para azul?
í. document.getElementsByTagName("p")[o].style.color = "#ooooFF";

2. document.getElementsByTagName("p")[o].color = "#ooooFF";

3. document.getElementsByTagName("p").item(o).style.color = "#ooooFF";

a) Apenas 1.

b) Apenas 2.

c) Apenas 3.

d) Apenas 1 e 3.

e) 1, 2e3.

i8.(MPE-RS / MPE-RS -2015) Dado o código Javascript abaixo:

<script type='rteKt7javascript''>
var numeros =

["UnT/Dois"/1 res","Quatro"];

numeros.pop();

nu m e ros. pus h ('1 Dez");
numeros.shift();

d oc u me nt. wri te (n um ei os) ;

</script>

y 79

/

Quando o bloco for inserido no corpo de uma página HTML e executado no navegador, o que será exibido na tela?
a) Dois,Tres,Dez b) Quatro,Dez,Dois,Tres c) Dois,Tres,Dez,Um d) Dez,Dois,Tres e) Um,Dois,Tres,Dez,Dez
19. (MPE-RS / MPE-RS -2015) Dado o código Javascript abaixo:

<script type="text/javascript">
function Aluno() {

var nome = "Ze";

var dados = {

idade : 18,

peso : 75

};

this.qetDados = function() {

return dados;

};

}

var x = new Aluno();
var y = x.qetDados();

document.write(x.nome + " ");
document.write(y.idade + " ");
y.idade += 2;
document.write(x.getDados(). idade);

</script>

Quando o bloco for inserido no corpo de uma página HTML e executado no navegador, o que será exibido na tela?
a) undefined undefined 20

b) undefined 18 20

c) Ze 18 18

d) Ze 18 20

e) undefined 18 18

20.(MPE-RS / MPE-RS-2015) Quais são os valores de saída do código Javascript abaixo?

/ 79

/

Cscript ty pe="text/j avascri pt " >

<!—

vai x = 1;
whiile (x < 20)

{

if (x == 5){
break;

}

x = x + 1;

document.write( x + "<br />");

}

//->

</sc npt>

a) 2-3-4-5

b) 2-3-4

c) 1-2-3-4-5

d) 1-2-3-4

e) 0-1-2-3-4

2i.(MPE-RS / MPE-RS -2015) Dado o seguinte código JSON com Javascript:

var text = '{ "employees"' : [' 4-

'{ "firstName":Tohn" , "Ia st Name":'Doe" +

'{ "firstN ame": "Anua" , ,rlastName":,,Smith" +

'{ "firstNameVPeter" , "lastName':'Jonesn } ]}';

É correto afirmar que o código apresentado acima:

a) concatena três string formando uma classe e atribui dados a ela.

b) concatena três objetos formando uma classe e atribui dados a ela.

c) divide um objeto em três strings e atribui dados a elas.

d) concatena três arrays em um objeto e atribui dados a ele.

e) cria um array com três objetos e atribui dados a eles

22. (UFG / AL-GO - 2015) Leia o trecho em Javacript a seguir:

y 79

/

Qual é a saída da execução desse trecho de código Javascript?
a) 123

b) 456

c) 156

d) 423

23. (FGV / BANESTES -2021) Considere o código javascript a seguir:

let txt =

function funcao(value, índex, array) {
if (índex % 2 == 0) {txt += value};

' }

function xpto (x) {
x.forEach(funcao);
return txt;

}

alert (xpto([0, 1, 1, 2, 3, 5]));

A execução desse código provoca a exibição de:
a) 011235

b) 013

c) 125

d) 532110

e) null

24. (FGV / BANESTES -2021) Considere o código javascript a seguir:

y 79

/

document.getElementByld('demo').innerHTML = Date()

Numa página web na qual esse código seja aplicado, o elemento que é compatível com a estrutura do comando para receber a data corrente é:
a) <p "demo">H</p>

b) <p class="demo">H</p>

c) <p id="demo">H</p>

d) <p js="demo">H</p>

e) <p onclick=udemo">H</p>

25. (CESPE / PGDF 2021) Julgue o item a seguir, referente a linguagem de scripts.

<input type='text' id='a' value=,5l>

<br>

<input type-^text1 id='b' value^Z^

<br>

<input type-^text1 idstc' >

<script>
document.getElementByld(1c1).values(document-

getElejnentByld (* a *) * value+document . getElement
Byld(1b*).value);

</script>

</html>

Em um navegador Internet com JavaScript habilitado, esse código apresentará o resultado a seguir

26.(CESPE / SEED-PR - 2021) resultado = (x for x in [5.-2])

Assinale a opção que apresenta o resultado da execução do código CoofeeScript precedente.
a) 5,5

b) 5,4,3,2

c) 2,2,2,2,2

d) 5,3,i e) 4,3
27. (CESPE / SEED-PR - 2021) JavaScript trabalha com números usando os operadores aritméticos fornecidos pela própria linguagem. No entanto, a linguagem aceita operações matemáticas
/ 79

mais complexas por meio de um conjunto de funções e constantes definidas como propriedades do objeto Math.
28. (CESPE / SEED-PR - 2021) A opção Match.ceil () apresenta a função que permite realizar, emJS, a operação matemática de arredondar para cima o número 1,17, obtendo-se o valor 2.

29. (CESPE / ME - 2020) Nos padrões web, as camadas deverão ser separadas de acordo com o objetivo para o qual elas foram desenvolvidas. Criar páginas em camadas lógicas é uma boa prática: xHTML, folhas de estilo CSS e JavaScript são voltadas, respectivamente, para as camadas de conteúdo, de apresentação visual do conteúdo e de comportamento dos elementos.
30. (CESPE / TJ-AM - 2019) JavaScript é uma linguagem de programação orientada ao desenvolvimento da interface para aplicações web, cujo código-fonte é compilado pelo servidor antes de sua execução.
31. (CESPE / SLU-DF - 2019) Uma função JavaScript é um bloco de código utilizado para executar tarefas repetidas e é definida pela palavra-chave public seguida por um nome seguido por parênteses ().
32. (CESPE / SLU-DF - 2019) O JSX (JavaScript Syntax Extension) é de uso obrigatório no React e permite inserir a interface do usuário no código JavaScript.
33. (FCC / TRT11 - 2005) Em JavaScript, para declarar nomes de identificadores válidos utiliza-se:

a) somente número no primeiro caractere.

b) somente letra ou underscore no primeiro caractere.

c) qualquertipo de caractere a partir do segundo caractere.

d) espaço entre caracteres a partir do segundo caractere.

e) uma palavra reservada do JavaScript

34. (FCC /TRE-SE - 2007) O cliente JavaScript, quando se soltar um botão do mouse pressionado,invocará o evento:

a) MouseOver.

b) MouseDown.

c) MouseUp.

d) MouseMove.

e) MouseOut.

35. (FCC / MPE-SE - 2008) Uma função embutida na linguagem JavaScript que calcula o conteúdo de uma string denomina-se:
a) string.

b) eval.

/ 79

/

c) number.

d) parselnt.

e) parseFloat

36.(FCC / TRT-i - 2014) O trecho de programa a seguir foi elaborado na linguagem HTML com
JavaScript e será aberto por um navegador que as suporte.

<html>

<body>

<hi>Página Principal</hi>

<form>
comando y

</form>

</body>

</html>

Página Principal

Nova Página

O comando que deve ser colocado no lugar do comando y, de modo que, ao se pressionar o botão Nova Página, seja aberta a página Pi.html, é:
a) <input type = "button" text="Nova Página" click="window.location='Pi.html'">

b) <inputtype="button" text="Nova Página" onclick = "window.location='Pi.html'">

c) <input type="onbutton" text="Nova Página" onclick = "window.location='Pi.html'">

d) <inputtype="button" value="Nova Página" onclick = "window.location='Pi.html'">

e) <input type="onbutton" value="Nova Página" click = "window.location='Pi.html'">

37.(FCC / TRT-18 - 2008) Na linguagem JavaScript, os métodos de interface com o usuário que fazem parte do objeto window são apenas os denominados:
a) select, submit e confirm.

b) open, alert e write.

c) click, select e write.

d) open, submit e close.

e) alert, confirm e prompt.

38.(FCC / DPE-SP - 2010) As tecnologias Web utilizam linguagem de scripting JavaScript,
linguagem de scripting ASP e applets Java para incluir aplicações, respectivamente, no lado:

x y 79
/

a) servidor, cliente e servidor.

b) cliente, servidor e cliente.

c) servidor, servidor e cliente.

d) cliente, cliente e servidor.

e) cliente, cliente e cliente.

3g.(FCC /TRT-2O - 2010) No JavaScript, a caixa de mensagem "Confirm":

a) permite que o usuário insira um nome e/ou um número dentro da caixa de texto.

b) Exibe apenas uma informação para o usuário.

c) Permite que o usuário insira um nome dentro da caixa de texto.

d) Permite que o usuário insira um número dentro da caixa de texto.

e) Solicita uma confirmação do usuário, positiva ou negativa.

Z|O.(FCC -TRT-20 - 2010) É um método do objeto History:

a) Case.

b) Left.

c) Open.

d) Forward e) Hostname
GABARITo - JS

1. LETRA A 15- LETRA C
29. ERRADO

2. LETRA A i6. LETRA C
30. ERRADO

3- LETRA A 17- LETRA D
3i- ERRADO

4- LETRA A i8. LETRA A
32. ERRADO

5- LETRA B 19- LETRA B
33- LETRA B

6. LETRA C 20. LETRA A
34- LETRA C

7- LETRA D 21. LETRA E
35- LETRA B

8. LETRA C 22. LETRA B
36. LETRA D

9- LETRA D 23- LETRA B
37- LETRA E

10. LETRA A 24. LETRA C
38. LETRA B

íi. LETRA D 25- CORRETO
39- LETRA E

12. LETRA B 26. LETRA B
40. LETRA D

13- LETRA A 27- CORRETO

14- LETRA A 28. CORRETO

x53

y 79

/

Conceitos Básicos

ECMA 2021

INCIDÊNCIA EM PROVA: BAIXA

ECMA é o padrão de definição da linguagem ECMAScript 2021, sendo a décima segunda especificação da linguagem ECMAScript, que teve início em 1996. Atualmente é uma das linguagens de programação de propósito geral mais utilizada, tendo em vista que já foi incorporada a maioria dos navegadores web, servidores e aplicativos. E 0 que tem haver ECMA comJavascript,
Professor?

JavaScript

É o mesmo que ECMAScript?
ECMAScript é baseado em várias tecnologias originárias, sendo as mais conhecidas
JavaScript
(Netscape) e JScript (Microsoft). A linguagem foi inventada por Brendan Eich na Netscape e apareceu pela primeira vez no Navegador navegador 2.0. Ele apareceu em todos os navegadores subsequentes da Netscape e em todos os navegadores da Microsoft começando com oInternet
Explorer3.o.

O desenvolvimento da especificação de linguagem ECMAScript começou em novembro de 1996 e a primeira edição da Ecma foi adotada pela Assembleia Geral da Ecma em junho de 1997.ECMAScript é uma linguagem de programação orientada a objetos para realizar cálculos e manipular objetos computacionais dentro de um ambiente host.
Através de uma interface de usuário, a linguagem de ECMAscript consegue ser um mecanismo simples para expor funcionalidades para o ambiente de programação. Lembre-se que qualquer y 79
/

linguagem de script se destina ao uso por programadores profissionais e não profissionais, para automatizar rotinas.
O ECMAScript foi originalmente projetado para ser uma linguagem de script para automatização na Web, fornecendo um mecanismo para animar as páginas da Web em navegadores e para executar scripts do lado servidor como parte de uma arquitetura cliente-servidor baseada naWeb.

ECMAScript atualmente é usado para fornecer recursos de script para uma variedade de ambientes de host. O uso do ECMAScript foi evoluindo com o tempo, e hoje vai além do script simples no ambiente web, sendo empregado para todo o espectro de tarefas de programação em muitos ambientes e escalas diferentes. À medida que o uso do ECMAScript se expandiu, os recursos e facilidades que oferece também se expandiram.
Mas professor por que precisa existir Javascript e ECMAScript ?

Só você pensar o seguinte: Imagina o caos que seria cada navegador com sua própria linguagem,meio o que acontece hoje com a web3, mas isso é outro assunto. A ideia da web é funcionar para todos e para isso precisamos de uma linguagem que permeie comportamento comuns a todos os navegadores. Para manter um padrão, a Netscape enviou o JavaScript à ECMA, que é a associação que cuida do ECMAScript.
Já que o nome JavaScript pertencia à Sun, registrou-se então um novo nome um padrão universal era o ECMAScript. Foi assim então que surgiu o nome ECMAScript.Porém, como o nome JavaScript sempre foi mais famoso, continuamos chamando a linguagem assim até hoje.
x y 79
/

Galera, agora vamos começar a falar de termos mais técnicos! O documento do
ECMAScript continuou evoluindo (ECMA - 262). Em 2015 foi lançado o ECMAScript 6, ECMAScript 7,8, 9, etc.
Todo ano então temos uma nova versão sendo lançada.

A nova versão 2021 traz muitas novas características, o que não considero razoável apresentar todas aqui, pelo simples fato que não existe uma cobrança pesada ao ponto de referenciar o esforço de vocês de aprendertodo o ECMA 262. Então vamos as principais características, porém que quiser dar uma olhada na especificação completa, só acessar: https://tc39.eS/ecma262/#sec-intro.Vamos então verificar o principal aspecto do ECMAScript 2021:
ES: SYMBOL

O tipo Symbol é o conjunto de todos os valores não String que podem ser usados como chave de uma propriedadeObject. Cada valor de símbolo possível é único e imutável.

ESPECIFICAÇÃO | DESCRIÇÃO

Um método que retorna o Asynclterator padrão para um objeto. Chamado pela

@@ASYNCITERATOR

semântica da declaração for-await-of.

@@HASINSTANCE

@@ISCONCATSPREADABLE

Um método que determina se um objeto construtor reconhece um objeto como uma das instâncias do construtor. Chamado pela semântica do operador instanceof.
Uma propriedade com valor booleano quez se true, indica que um objeto deve ser nivelado para seus elementos de matriz por Array.prototype.concat.
@@ITERATOR

Um método que retorna o Iterator padrão para um objeto. Chamado pela semântica da instrução for-of.
@@MATCH

Um método de expressão regular que corresponde à expressão regularem relação a uma string. Chamado pelo método String.prototype.match.
@@MATCHALL

@@REPLACE

Um método de expressão regular que retorna um iterador, que gera correspondências da expressão regular com uma string. Chamado pelo métodoString. prototype.matchAII.

Um método de expressão regular que substitui as substrings correspondentes de uma string. Chamado pelo método String.prototype.replace.
@@SEARCH

Um método de expressão regular que retorna o índice em uma string que corresponde à expressão regular. Chamado pelo método String.prototype.search.
@@SPECIES

Uma propriedade com valor de função que é a função construtora usada para criar objetos derivados.
@@SPLIT

Um método de expressão regular que divide uma string nos índices que correspondem à expressão regular. Chamado pelo método String.prototype.split.
x y 79
/

Um método que converte um objeto em um valor primitivo corres
Chamado pela operação abstrata ToPrimitive.

Uma propriedade com valor de String que é usada na criação da descrição de strir padrão de um objeto. Acessado pelo método interno Object.prototype.toString
Uma propriedade com valor de objeto cujos nomes de propriedade próprios herdados são nomes de propriedade que são excluídos das associações c ambiente do objeto associado.
Professor, se eu entendo e lógica e indexação do Javascript, eu vou entender a do ECMAScript? Sim,
existe a mesma finalidade e a mesma estrutura, por isso as questões como veremos, estão 99%
orientadas ao Javascript. O que você precisa guardar é que o escopo da finalidade de ambos...

(UNIPAMPA-2013) ECMAScript é considerada uma versão anterior do JavaScript.

Comentários: conforme vimos, o ECMAScript é uma especificação formal de uma linguagem de script.
Javascript é a implementação mais popular do ECMAScript (Errado).
(COREN - 2018) Em relação ao JavaScript (versão ECMAScript 2015 ou superior), é correto afirmar que para adicionar o array (arr2) ao final do array existente (arn),era utilizada a instrução "Array.prototype.push.apply(arn, arr2);" e atualmente,após a especificação ES2015, passa a ser "arri.push(...arr2);".
Comentários: a simplificação apresentada diz respeito ao ECMAScript, e faz com que a instrução de adição de array, utilize o arn.pus (...arr2), sem o prototype, logo a questão está perfeita (Correto).
(COREN -2018) No ECMAScript, os tipos de dados primitivos são: bool, number, String,
Symbol e closures.

Comentários: os tipos primitivos são no ECMAScript: string, number, null, undefined, boolean e symbol (Errado).
x y 79
/

QUESTõES CoMENTADAS - ECMASCRIPT

í. (UFC / CCV - 2018) O que acontece quando executamos o código abaixo em um navegador com suporte à ECMAScript versão ES6 ou superior?
<'DOCTYPE html>

<html>

<body>

<scrípt>

let teste — 200,
tf < teste > 100){

let teste = 1;

}

console, logt testei;

</script>

</body>

</html>

a) O valor da variável teste será sempre 200.

b) Será exibido no console do navegador o valor 1.

c) Será exibido dentro da janela navegador o valor 1.

d) A instrução let introduz um escopo de bloco a variável teste.

e) A declaração da variável teste utilizando let funcionaria da mesma forma se utilizássemos var.
Comentários:

O erro da alternativa A) está em dizer que "teste" sempre será 200, o que é incorreto, visto que se invocarmos um console.log(teste) dentro do if teremos que teste é = 1. Isso acontece porque existe uma nova declaração da variável teste dentro do if, e quando chamamos uma variável dentro de um bloco de código 0 Javascript sempre "pegará" a variável que estiver mais perto do bloco. A B eC estão erradas porque não será exibido nem dentro do console e nem dentro da janela o valor 1. AD é nossa resposta correta, porque a instrução let é que introduz um escopo de bloco a variável teste no código e a E está errada, porque se utilizássemos var não seria o mesmo de utilizar let, são instruções distintas, let cria uma variável com escopo de bloco.
Gabarito: Letra D

2. (UFC / CCV - 2018) O que acontece quando executamos o código abaixo em um navegador com suporte à ECMAScript versão ES6 ou superior?
/ 79

<'DOCTYPE httnl>

<body>

<soipT>

var ponto = [1,3],

segmento — [ponto, [5,5]],

tríangnto = [...segmento,[],$]];
console fogtmangulo lengrhi

</scnpr>

</body>

</hrml>

a) A variável triângulo terá o comprimento i.

b) A variável triângulo terá o comprimento 2.

c) A variável triângulo terá o comprimento 3.

d) A variável triângulo terá o comprimento 4.

e) A variável triângulo terá o comprimento 6.

Comentários:

Questão de raciocínio lógico! Vejamos um triângulo tem três lados, e temos as variáveis: ponto(1,3), segmento [ponto, [5,5]] e segmento [ 1,8]], agora vamos de frente para trás,
se length é o comprimento para o triângulo (triângulo.length), então: triângulo, concatena segmento, que concatena ponto, logo recebemos 3 de length.
Gabarito: Letra C

3. (UFC / CCV - 2018) O que acontece quando executamos o código abaixo em um navegador com suporte à ECMAScript versão ES6 ou superior?
<!DOCTYPE litml-*

<body>

<p id="deiuo,,x/p>

<script>

obj = { na me: "Joao", age: 20, city: "Fortaleza" };

A-ar myJSON = JSON.strmgify(obj);

document. getElementById( "demo") .innerHTA IL = myJSON;

</script>

</body>

a) Será exibido na janela do navegador o seguinte texto: [object Object],

b) Será exibido no console do navegador o seguinte texto: [object Object].

c) Será exibido na janela do navegador o seguinte texto: Joao, 20, Fortaleza.

d) Será exibido na janela do navegador o seguinte texto:
{"name":"Joao","age":2o,"city":"Fortaleza"}.

e) Será exibido no console do navegador o seguinte texto:
{"name":"Joao","age":2o,"city":"Fortaleza"}.

Comentários:

Ao compilar o código, teremos os elementos:
{"name":"Joao","age":2o,"city":"Fortaleza"} na janela do navegador e não no console.
Gabarito: Letra D

4. (COVED / UFPE - 2019) Considere a execução do código JavaScript abaixo,
compatível com o
ECMAScript 6, e a respectiva numeração das linhas de código na coluna à esquerda, e assinale a alternativa correta.
y 79

/

1 var a 5;

2 var b = 10;

3 xf (a —- 5) (

4 let a 4;

5 var b - 1;

6 console.log(a);

7 console.log(b);

8 )

9 console.log(a);

10 console.log(b);

Após a execução do código, desconsiderando os caracteres de quebra de linha da função console.Iog(), o console apresentará:
a) as saídas: 4,1,5 e 1

b) as saídas: 4,1,4 e 1

c) as saídas: 4,1,4 e 10

d) uma mensagem de erro referente a linha 3

e) uma mensagem de erro referente a linha 4

Comentários:

Pessoal, vamos linha a linha:

Primeiro, iniciamos as variáveis e atribuímos os valores 5 e 10 (linha 1 e 2).
Depois usamos a condição (IF e colocamos == que é um operadorde igualdade, ou seja, verifica se a realmente é igual5, com objetivo de inicializar o laço condicional. Em seguida temos o let, let transforma a variável como escopo de bloco. Ex:
let escopoBloco = 'Pedro';
console.log (escopoBloco); // Pedro

Logo: console.log(a); // 4 console.log(b); //1 console.log(a); // 5 console.log(b); //1

Gabarito: Letra A

5. (UFPR / COREN - 2018) Em relação ao JavaScript (versão ECMAScript 2015 ou superior), é correto afirmar:
a) A expressão "varfunc = x=>x *x;" define a variável x apontando para a função func que calcula a raiz quadrada de x.
b) Template literais ou template strings são literais string que permitem expressões embutidas,nas quais os textos são delimitados por aspas simples e as expressões indicadas e delimitadas por #{expressãoj.
c) Para adicionar o array (arr2) ao final do array existente (arn), era utilizada a instrução"Array.prototype.push.apply(arn, arr2);" e atualmente, após a especificação ES2015,
passa a ser "arn.push(...arr2);".
d) No ECMAScript 6, os tipos de dados primitivos são: bool, number, String, Symbol e closures.

e) A função focus do objeto Window, quando o script é executado nos navegadores da web,remove o foco da janela atual.

Comentários:

(a) Errado. Para definir a variável x precisaria ser var func = function (x) {return x*x e não var func =x => x*x; (b) Errado. Template Literal é delimitado por acento grave (")
e a interpolação de expressão é feita com ${}; (c) Correto. Pessoal algumas questões você vão ter que descobrir as erradas e ir excluindo, é humamente improvável que alguém soubesse no detalhe a especificaçãoES2015 aplicada a instrução Array.prototype.push.apply(am, arr2); neste caso vale a regra: se a questão não tem erro, provavelmente ela é a correta; (d) Errado. No ECMAScript 6, os tipos de dados primitivos são: string, number, undefined, null, boolean, symbol; (e) Errado. Ao contrário, a função focus adiciona foco e não remove o foco da janela atual.
Gabarito: Letra C

y 79

/

LISTA DE QUESTõES - ECMASCRIPT

í. (UFC / CCV - 2018) O que acontece quando executamos o código abaixo em um navegador com suporte à ECMAScript versão ES6 ou superior?
<'DOCTYPE html>

<html>

<body>

<scrípt>

let teste — 200,
tf < teste > 100){

let teste = 1;

}

console, logt testei;

</script>

</body>

</html>

a) O valor da variável teste será sempre 200.

b) Será exibido no console do navegador o valor 1.

c) Será exibido dentro da janela navegador o valor 1.

d) A instrução let introduz um escopo de bloco a variável teste.

e) A declaração da variável teste utilizando let funcionaria da mesma forma se utilizássemos var.
2. (UFC / CCV - 2018) O que acontece quando executamos o código abaixo em um navegador com suporte à ECMAScript versão ES6 ou superior?
/ 79

<'DOCTYPE httnl>

<body>

<soipT>

var ponto = [1,3],

segmento — [ponto, [5,5]],

tríangnto = [...Segmento,[],$]];
console fogtmangulo lengrhi

</scnpr>

</body>

</hrml>

a) A variável triângulo terá o comprimento i.

b) A variável triângulo terá o comprimento 2.

c) A variável triângulo terá o comprimento 3.

d) A variável triângulo terá o comprimento 4.

e) A variável triângulo terá o comprimento 6.

3. (UFC / CCV - 2018) O que acontece quando executamos o código abaixo em um navegador com suporte à ECMAScript versão ES6 ou superior?
<!DOCTYPE litml-*

<html>

<body>

<p id="deiuo,,x/p>

<script>

obj = { na me: "Joao", age: 20, city: "Fortaleza" };

A-ar myJSON = JSON.strmgify(obj);

document. getElementById( "demo") .innerHTA IL = myJSON;

</script>

</body>

a) Será exibido na janela do navegador o seguinte texto: [object Object],

b) Será exibido no console do navegador o seguinte texto: [object Object].

c) Será exibido na janela do navegador o seguinte texto: Joao, 20, Fortaleza.

d) Será exibido na janela do navegador o seguinte texto:
{"name":"Joao","age":2O,"city":"Fortaleza"}.

y 79

/

e) Será exibido no console do

{"name":"Joao"/"age":2o,"city":"Fortaleza"}.

navegador o seguinte texto:

4. (COVED / UFPE - 2019) Considere a execução do código JavaScript abaixo,
compatível com o
ECMAScript 6, e a respectiva numeração das linhas de código na coluna à esquerda, e assinale a alternativa correta.
1 var a 5;

2 var b = 10;

3 if (a === 5) (

4 let a - 4;

5 var b 1;

6 console.log(a);

7 console.log(b);

8 )

9 console.log(a);

10 console.log(b);

Após a execução do código, desconsiderando os caracteres de quebra de linha da função console.Iog(), o console apresentará:
a) as saídas: 4,1,5 e 1

b) as saídas: 4,1,4 e 1

c) as saídas: 4,1,4 e 10

d) uma mensagem de erro referente a linha 3

e) uma mensagem de erro referente a linha 4

5. (UFPR / COREN - 2018) Em relação ao JavaScript (versão ECMAScript 2015 ou superior), é correto afirmar:
a) A expressão "varfunc = x => x * x;" define a variável x apontando para a função func que calcula a raiz quadrada de x.
b) Template literais ou template strings são literais string que permitem expressões embutidas,nas quais os textos são delimitados por aspas simples e as expressões indicadas e delimitadas por#{expressão}.
c) Para adicionar o array (arr2) ao final do array existente (arn), era utilizada a instrução"Array.prototype.push.apply(arn, arr2);" e atualmente, após a especificação ES2015,
passa a ser "arri.push(...arr2);".
d) No ECMAScript 6, os tipos de dados primitivos são: bool, number, String, Symbol e closures.

e) A função focus do objeto Window, quando o script é executado nos navegadores da web,remove o foco da janela atual.

y 79

/

GABARITo - ECMASCRIPT

1. LETRA D

2. LETRA C

3. LETRA D

4. LETRA A

5. LETRA C

/ 79

/

Conceitos Básicos

TYPESCRIPT

INCIDÊNCIA EM PROVA: BAIXA

TYPESCRIPT é uma evolução do Javascript proposta pela Microsoft, que tem como principal característica a tipagem forte, sendo compilado para javascript, open-source e utilizado em vários frameworks web.
Diante das limitações que o Javascript possui, Anders Hejlsberg, que também participou da criação do C#, do Delphi, do Turbo Pascale da plataforma .NET, desenvolveu o Typescript. Que até então não suportava a programação 00. Importante destacar que no momento da compilação oTypescript se torna Javascript, a razão disso é que o Typescript foi construído em cima do Javascript.Isso facilita a vida dos navegadores que não precisam entender outra linguagem, somente o javascript. Professor, e quais são as diferenças do JS para o TS?
TS

TypeScript

Anote ai! Ouviu TypeScript, pensou: Estático, Tipagem forte, Orientado a objetos, Genérico,Namespaces e Decorators. A característica mais marcante do TypeScript é sem dúvida é sua tipagem forte, motivo pelo qual leva no seu nome: type (tipagem). Temos o aspecto daOrientação a Objetos que é muito importante do ponto de vista estrutural da linguagem, sendo um paradigma que facilita a adoção da mesma.
O JavaScript, na maior parte do seu projeto de linguagem, não é tipado e a inferência de tipo só vai até certo ponto, o que abre caminho para utilização de TypeScript, a fim de suprir essa deficiência.
Vejamos um exemplo de código escrito em TypeScript e depois em Javascript:

y 79

/

CONDIÇÃO DE APROVAÇÃO EM TYPESCRIPT

type Result = "aprovado" | "reprovado"

function verify(result: Resultado) {
if (result === "aprovado") {

console.log("Aprovado")

} else {

console.log("Reprovado")

}

}

CONDIÇÃO DE APROVAÇÃO EM JAVASCRIPT

function verify(result) {

if (result === "aprovado") {
console.log("Aprovado")

} else {

console.log("Reprovado")

}

}

Pessoal, a diferença nesse exemplo é bem simples, com TypeScripttemos adição de sintaxe natural para fornecimento de types (tipos). No typescript, uma string é uma sequencia de caracteres,considerado objeto. Um objeto em typescript é declarado com {}, enquanto que um array é [ ]

TIPOS MAIS EMPREGADOS NO TYPESCRIPT

NUMBER: É para todo e qualquertipo de número, seja ele ponto flutuante ou inteiro.

STRING: Representa uma string costumeiramente conhecida em outras linguagens de programação.

BOOLEAN: Representa um valor booleano: true ou false.

ANY: A tradução de Any é qualquer e, como sua tradução sugere, é um tipo que pode ser modificado para qualqueroutro tipo presente na linguagem, seja string, number, boolean ou qualquer outra coisa.
ARRAY: Representa o tipo Array dentro da linguagem. É válido informar que podemos criar arrays de duas formas dentro do TypeScript.
Importante: Para indicar a raiz de arquivos Typescript basta encontrarmos arquivos do tipo tsconfig.json e a linguagem Typescript não aceita heranças múltiplas.
(CCV- 2019) Sobre TypeScript, assinale a alternativa correta.

a) Toda função deve possuir um nome.

b) TypeScript é um subconjunto de JavaScript.

c) Em um enum não é possível misturar membros de tipos baseados em string e number.

y 79

/

d) Em uma classe TypeScript é possível utilizar herança múltipla por meio da palavra chave extends.
e) A presença de um arquivo tsconfig.json em um diretório indica que o diretório é a raiz de um projeto TypeScript.
Comentários: (a) Errado. Função não precisa necessariamente ter nome, é possível invocar uma função anônimas; (b) Errado.Como vimos, Typescript é uma linguagem e não um subconjunto de JS; (c) Errado. É possível sim misturar strings, number e boolean, que são tipos em typescript em uma enum; (d) Errado. Não se utiliza herança múltipla emTypescript pela adoção ao paradigma orientado a objeto, logo não cabe herança múltipla conforme vimos;(e) Correto. A presença de um arquivo tsconfig.json em um diretório indica que o diretório é a raiz de um projeto TypeScript(Letra E).

x y 79
/

í. (CESGRANRIO / BB - 2021) Considere o fragmento de código TypeScript a seguir.
const a=<T extends {b:string}> (obj:T)=>{<códigoremovido>};

Com relação ao código apresentado acima, a(o)

a) função a() retorna um objeto do tipo string.

b) variável a é uma lista de objetos do tipo string.

c) variável a é um dicionário cujas chaves são objetos do tipo string.

d) objeto que for passado para a função a() deve ter um campo b do tipo string.

e) valor retornado pela função a() é um objeto que estende um objeto do tipo string.

Comentários:

No typescript, string é uma sequência de caracteres, considerado objeto, um objeto em typescript é declarado com {}, enquanto que um array é [ ].
Gabarito: Letra D

2. (CESGRANRIO / BB - 2021) Considere o código HTML a seguir.

<ldoctype html>

<html lang="pt-br">

<head>

<script src="scrípt.js"x/script>

</head>

<body>

<f orm>

Texto: <input type='text' name='texto* id='ídTexto' class='classe-input'
value=*Texto inicial'xbr>

<input type='submit' value='Envia*>

</form>

</body>

</html>

Considere, também, o arquivo TypeScript script.ts, listado a seguir, que irá gerar o arquivo script.js no mesmo diretório do arquivo HTML, apresentado acima.
onload = (event) => {

const texto = document.querySelector('???') as HTMLInputElement;
console.log('Texto inicial: texto.value);

Que texto o programador deverá utilizar no lugar de ???, no código do arquivo
TypeScript script.ts,
para exibir o valor do campo HTML input na console?

a) #classe-input b) #idTexto c) #texto d) .idTexto e) .texto
Comentários:

No lugar de ??? basta utilizar o #idTexto, a fim de buscar o atributo id no código do arquivoTypeScript script.ts, a partir do campo HTML input.

Gabarito: Letra B

3. (FCC / MPE-PB - 2018) Considere o fragmento de código TypeScript abaixo.

interface CriaArrayString {
(índice: number): string;

)

var nomes: CriaArrayString;

nomes = ["Ana", "Pedro", "Mariana");
document.body.ínnerHTXL nomes[1];

Ao executar esse código:

a) ocorrerá um erro na linha que contém o comando [indice: number]: string;

b) será exibido na tela o nome Pedro.

c) ocorrerá um erro na linha que contém o comando var nomes: CriaArrayString;

d) será exibido na tela o nome Ana.

e) ocorrerá um erro na linha que contém o comando document.body.innerHTML = nomesfi];

Comentários:

Quando for executado o nome Pedro será exibido na tela, porque ao definir o array coms as strings nome = ["Ana", " Pedro", " Mariana".] e invocar o nome [1], devemos lembrar que um array começa em o, logo:
Nome [0] = Ana
Nome [1] = Pedro
Nome [2] = Mariana

Gabarito: Letra B

/ 79

4. (UFC / CCV - 2019) Para o desenvolvimento de aplicações Web, qual item abaixo contém apenas frameworks/bibliotecas/plataformas que foram desenvolvidas ou que dependem deJavaScript ou TypeScript:

a) Node.js, CSS, Java.

b) React, Node.js, Scala.

c) Angular, React, Vue.js.

d) Angular, Node.js, Java.

e) Java AWT, Angular, Scala.

Comentários:

Os frameworks que utilizam tanto JS como TS são Angular, React e Vue, respectivamente todos podemos inclusive ser escritos como AngularJS, ReactJS e VueJS.
Gabarito: Letra C

5. (CVV / UFC - 2019) Sobre TypeScript, assinale a alternativa correta.

a) Toda função deve possuir um nome.

b) TypeScript é um subconjunto de JavaScript.

c) Em um enum não é possível misturar membros de tipos baseados em string e number.

d) Em uma classe TypeScript é possível utilizar herança múltipla por meio da palavra chave extends.
e) A presença de um arquivo tsconfig.json em um diretório indica que o diretório é a raiz de um projeto TypeScript.
Comentários:

(a) Errado. Não necessariamente toda função deve possuir nome, é possível aplicar funções anônimas por exemplo, com arrow functions, por exemplo; (b) Errado.Typescript não é subconjunto do Javascript; (c) Errado. É possível misturar tanto strings, numbers ou boolean, que são os únicos tipos em typescript, em uma "enum"; (d) Errado. Typescript não utiliza herança múltipla conforme estudamos; (e) Correto. A presença de um arquivo tsconfig.json em um diretório indica que o diretório é a raiz de um projeto TypeScript.
Gabarito: Letra E

6. (FCC / MPE-PE - 2018) Considere o fragmento de código TypeScript abaixo.

x y 79
/

interface CriaArrayString {
(Índice: number]: string;

}

var nomes: CriaArrayString;

nomes = ("Ana", "Pedro", "Mariana");
document.body.innerHTML nomes(1];

Ao executar esse código:

a) ocorrerá um erro na linha que contém o comando [indice: number]: string;

b) será exibido na tela o nome Pedro.

c) Ocorrerá um erro na linha que contém o comando var nomes: CriaArrayString;

d) Será exibido na tela o nome Ana.

e) Ocorrerá um erro na linha que contém o comando document.body.innerHTML = nomesfi];

Comentários:

(a) Errado. Não existe motivo para ocorre um erro no comando: [indice:
number]: string; (b)
Correto. Será exibido Pedro; (c) Errado. Não existe motivo para ocorre um erro na linha var nomes:CriaArrayString; (d) Errado. Será exibido Pedro e não Ana; (e) Errado. Também não existe erro no comando document.body.innerHTML = nomesfi];
Gabarito: Letra B

/ 79

/

LISTA DE QUESTõES - TYPESCRIPT

í. (CESGRANRIO / BB - 2021) Considere o fragmento de código TypeScript a seguir.
const a=<T extends {b:string}> (obj:T)=>{<códigoremovido>};

Com relação ao código apresentado acima, a(o)

a) função a() retorna um objeto do tipo string.

b) variável a é uma lista de objetos do tipo string.

c) variável a é um dicionário cujas chaves são objetos do tipo string.

d) objeto que for passado para a função a() deve ter um campo b do tipo string.

e) valor retornado pela função a() é um objeto que estende um objeto do tipo string.

2. (CESGRANRIO / BB - 2021) Considere o código HTML a seguir.

<ldoctype html>

<html lang="pt-br">

<head>

<script src="scrípt.js"x/script>

</head>

<body>

<f orm>

Texto: <input type='text' name='texto* id='ídTexto' class='classe-input'
value=*Texto inicial'xbr>

<input type='submit' value='Envia*>

</form>

</body>

</html>

Considere, também, o arquivo TypeScript script.ts, listado a seguir, que irá gerar o arquivo script.js no mesmo diretório do arquivo HTML, apresentado acima.
onload = (event) => {

const texto = document.querySelector('???') as HTMLInputElement;
console.log('Texto inicial: texto.value);

};

Que texto o programador deverá utilizar no lugar de ???, no código do arquivo
TypeScript script.ts,
para exibir o valor do campo HTML input na console?

a) #classe-input b) #idTexto c) #texto d) .idTexto x
/ 79

e) .texto

3. (FCC / MPE-PB - 2018) Considere o fragmento de código TypeScript abaixo.

interface CriaArrayString {
(índice: number): string,-

)

var nomes: CriaArrayString;

nomes = ["Ana", "Pedro", "Mariana");
document.body.ínnerHTXL nomes[1];

Ao executar esse código:

a) ocorrerá um erro na linha que contém o comando [indice: number]: string;

b) será exibido na tela o nome Pedro.

c) ocorrerá um erro na linha que contém o comando var nomes: CriaArrayString;

d) será exibido na tela o nome Ana.

e) ocorrerá um erro na linha que contém o comando document.body.innerHTML = nomes[ij;

4. (UFC / CCV - 2019) Para o desenvolvimento de aplicações Web, qual item abaixo contém apenas frameworks/bibliotecas/plataformas que foram desenvolvidas ou que dependem deJavaScript ou TypeScript:

a) Node.js, CSS, Java.

b) React, Node.js, Scala.

c) Angular, React, Vue.js.

d) Angular, Node.js, Java.

e) Java AWT, Angular, Scala.

5. (CVV/ UFC - 2019) Sobre TypeScript, assinale a alternativa correta.

a) Toda função deve possuir um nome.

b) TypeScript é um subconjunto de JavaScript.

c) Em um enum não é possível misturar membros de tipos baseados em string e number.

d) Em uma classe TypeScript é possível utilizar herança múltipla por meio da palavra chave extends.
e) A presença de um arquivo tsconfig.json em um diretório indica que o diretório é a raiz de um projeto TypeScript.
6. (FCC / MPE-PE - 2018) Considere o fragmento de código TypeScript abaixo.

x76

/ 79

interface CriaArrayString {
(Índice: number): string;

}

var nomes: CriaArrayString;

nomes = ("Ana", "Pedro", "Mariana");
document.body.innerHTML nomes(1) ;

Ao executar esse código:

a) ocorrerá um erro na linha que contém o comando [indice: number]: string;

b) será exibido na tela o nome Pedro.

c) Ocorrerá um erro na linha que contém o comando var nomes: CriaArrayString;

d) Será exibido na tela o nome Ana.

e) Ocorrerá um erro na linha que contém o comando document.body.innerHTML = nomesfi];

x y 79
/

GABARITo - TYPESCRIPT

1. LETRA D

2. LETRA B

3. LETRA B

4. LETRA C

5. LETRA E

6. LETRA B

