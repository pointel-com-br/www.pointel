# Matemática Básica e Aplicada - Sistemas Lineares

SERPRO - Raciocínio Lógico - 2023

(Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

12 de Maio de 2023

Índice

.1..)..S..i.s..t.e..m...a..s...L..in..e..a..r..e..s

.2..)..E..q..u..a..ç..ã..o...L..i.n..e..a..r

.3..)..S..i.s..t.e..m...a...L..i.n..e..a..r.........................................................
Item. ...1 0

.4..)..S..i.s..t.e..m...a..s...L..in..e..a..r..e..s..E...q..u..i.v.a..l.e..n..t.e..s................
Item. ..................1 7

.5..)..C..l.a..s..s..i.f.ic..a..ç..ã..o...d..e...u..m....S..i.s..t.e..m...a...L..i.n..e..a..r.......
Item. ....................2 2

.6..)..S..i.s..t.e..m...a...L..i.n..e..a..r..H..o..m...o..g..ê..n..e..o.............................
Item. ............2 5

.7..)..S..o..l.u..ç..ã..o...d..e...u..m....S..i.s..t.e..m...a...L..i.n..e..a..r.....................
Item. ..............2 6

.8..)..D..i.s..c..u..s..s.ã..o...d..e...u..m....S...i.s.t.e..m...a...L..i.n..e..a..r................
Item. ................5 1

.9..)..Q...u..e..s.t.õ..e..s...C...o..m...e..n..t.a..d..a..s...-..S..o..l.u..ç..ã..o...d..e...u..m..
..S..i.s..t.e..m...a...L..i.n..e..a..r..-..C...e..b..r.a..s..p..e...................................
Item. ..........................................6 1

.1..0..)..Q...u..e..s.t.õ..e..s...C...o..m...e..n..t.a..d..a..s...-..D..i.s..c..u..s..s.ã..o...d..e.
..u..m....S...i.s.t.e..m...a...L..i.n..e..a..r..-...C..e..b..r.a..s..p..e...........................
Item. .............................................6 4

.1..1..)..L..i.s.t.a...d..e...Q...u..e..s..t.õ..e..s...-..S..o..l.u..ç..ã..o...d..e...u..m....S..i.s
..t.e..m...a...L..i.n..e..a..r..-..C...e..b..r.a..s..p..e...........................................
Item. ........................................7 9

.1..2..)..L..i.s.t.a...d..e...Q...u..e..s..t.õ..e..s...-..D...is..c..u..s..s..ã..o...d..e...u..m....
S..i.s..t.e..m...a...L..in..e..a..r...-..C..e..b..r..a..s.p..e......................................
Item. ..........................................8 1

APRESENTAÇÃO DA AULA

Fala, pessoal!

Hoje trataremos sobre sistemas lineares. Antes de começar esse PDF, é necessário que você já tenha uma base de matrizes e determinantes.
Ressalto desde já que o assunto dessa aula não costuma ser muito cobrado em provas de concurso público.
Usualmente procuro colocar questões ao longo da teoria. Para o aprendizado da matéria de sistemas lineares, existe a necessidade de uma base teórica que não costuma ser cobrada diretamente nas questões, motivo pelo qual essa aula apresenta alguns trechos de teoria sem muitas questões.
Como de costume, vamos exibir um resumo logo no início do tópico para que você tenha uma visão geral do conteúdo antes mesmo de iniciar o assunto.
Conte comigo nessa caminhada =)

Prof. Eduardo Mocellin.
@edu.mocellin

SISTEMAS LINEARES

Sistemas lineares

Equação linear

Equações lineares são da forma 𝒂𝟏𝒙𝟏 + 𝒂𝟐𝒙𝟐 + 𝒂𝟑𝒙𝟑 + ⋯ + 𝒂𝒏𝒙𝒏 = 𝒃.

* 𝒙𝟏, 𝒙𝟐, 𝒙𝟑, ..., 𝒙𝒏 são incógnitas;

* 𝒂𝟏, 𝒂𝟐, 𝒂𝟑, ... ,𝒂𝒏 são os coeficientes;

* 𝒃 é o termo independente.

Uma solução de uma equação linear é um conjunto ordenado de números reais que torna a equação verdadeira.
Sistema linear

Um sistema linear é um conjunto de equações lineares.

A solução de um sistema linear deve tornar verdadeira todas as equações que compõem o sistema.

Representação matricial de um sistema linear:

𝑨𝑿 = 𝑩

*𝑨: Matriz dos coeficientes ou matriz incompleta do sistema;

* 𝑿: Matriz das incógnitas;

* 𝑩: Matriz dos termos independentes.

* [𝑨|𝑩]: Matriz completa do sistema.

𝟑𝒙 + 𝟒𝒚 + 𝟏𝒛 = 𝟑

𝟑 𝟒 𝟏 𝒙 𝟑

{𝟏𝒙 + (−𝟏)𝒚 + 𝟏𝒛 = 𝟏

𝟏𝒙 + 𝟑𝒚 + 𝟎𝒛 = 𝟐

→ [𝟏 −𝟏 𝟏] × [𝒚] = [𝟏]

𝟏 𝟑 𝟎 𝒛 𝟐

𝟑 𝟒 𝟏 𝟑
[𝑨|𝑩] = [𝟏 −𝟏 𝟏 𝟏]

𝟏 𝟑 𝟎 𝟐

Sistemas lineares equivalentes

Dois sistemas lineares são equivalentes quando apresentam as mesmas soluções.

Uma equação L₁ é combinação linear de outras equações L₂ e L₃ quando existem valores reais 𝒂 e 𝒃 tais que:
L1 = 𝒂L2 + 𝒃L3

Em um sistema linear, ao substituir uma determinada equação por uma combinação linear dela com outra equação, temos um sistema linear equivalente.
Em um sistema linear, quando uma determinada equação corresponde a uma combinação linear de outras equações do sistema, podemos eliminar essa equação do sistema.
Classificação de um sistema linear

Se um sistema linear apresenta mais de uma solução, então ele apresenta infinitas soluções.

Sistema linear homogêneo

Um sistema linear homogêneo é aquele em que os termos independentes de todas as equações são iguais a zero. Sempre admite a solução em que todas as variáveis são zero (solução trivial).
3𝑥 + 1𝑦 + 𝑧 = 𝟎

{2𝑥 + 4𝑦 + 2𝑧 = 𝟎
3𝑥 + 2𝑦 + 4𝑧 = 𝟎

Solução de um sistema linear

* Solução por substituição: consiste em isolar uma variável em uma equação e substituir em outra equação.
* Solução por eliminação de variável: consiste em eliminar variáveis por meio de uma combinação linear conveniente das equações do sistema linear.
* Solução pela soma das equações do sistema: existem casos em que a solução do sistema linear é obtida de modo mais rápido realizando a soma de todas as equações do sistema.
* Solução por matriz inversa: a matriz das incógnitas (𝑿) é obtida pelo produto da matriz inversa dos coeficientes pela matriz dos termos independentes: 𝑿 = 𝑨−𝟏𝑩.
Teorema de Cramer

Só pode ser utilizado quando o número de equações do sistema linear (𝒏) é igual ao número de incógnitas. Nesse caso, a matriz dos coeficientes (𝑨) do sistema linear será quadrada,de dimensão 𝒏 × 𝒏.
Seja 𝐷 = det 𝐴.

01) Se 𝐷 ≠ 0, o sistema é possível e determinado (SPD), apresentando solução única.

02) Sendo 𝐷 ≠ 0, a solução única (𝛼₁, 𝛼₂, ... , 𝛼𝑛) do sistema linear é tal que:

𝛼𝑖

= 𝐷𝑖

𝐷

Onde 𝐷𝑖 é o determinante da matriz que se obtém a partir de 𝐴𝑛×𝑛 substinuindo a coluna 𝑖 pela matriz
𝐵𝑛×1.

Método do==2d4a97== escalonamento

O método consiste em obter um sistema equivalente ao sistema original em que o número de variáveis explícitas diminui de equação para equação. Em outras palavras, o número de coeficientes nulos aumenta de equação para equação.
2𝑥 + 𝑦 + 𝑧 = 4

{2𝑥 + 4𝑦 + 4𝑧 = 22 → {
2𝑥 + 4𝑦 + 3𝑧 = 10

2𝑥 + 𝑦 + 𝑧 = 4

3𝑦 + 3𝑧 = 18

−𝑧 = −12

Para obter o sistema escalonado, devemos seguir os seguintes passos:

* Colocar como 1ª equação uma que apresente a 1ª incógnita;

* Anular a 1ª incógnita de todas as equações (exceto da 1ª) fazendo uso da 1ª equação;

* Anular a 2ª incógnita de todas as equações (exceto da 1ª e da 2ª) fazendo uso da 2ª equação;

* Anular a 3ª incógnita de todas as equações (exceto da 1ª, da 2ª e da 3ª) fazendo uso da 3ª equação;
* E assim sucessivamente, até que tenhamos usado todas as equações.

Posto e nulidade de uma matriz

O posto de uma matriz é o número de linhas não nulas de uma matriz escalonada. A representação do posto de uma matriz 𝐴 é dada por 𝜌(𝐴).
A nulidade de uma matriz é dada por 𝑛𝑢𝑙𝑙(𝐴) = (Nº 𝑐𝑜𝑙𝑢𝑛𝑎𝑠) − 𝜌(𝐴)

Discussão de um sistema linear

Discussão por Teorema de Cramer

Para fins de discussão do sistema linear, o Teorema de Cramer tem serventia quando obtemos 𝑫 ≠ 𝟎
ou quando o sistema é homogêneo.
Discussão pelo Método do Escalonamento

Passo 1: Escalonar o sistema linear.

Passo 2: Analisar o sistema linear escalonado.

* Se obtivermos uma equação da forma 𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 + 𝟎𝒘 = 𝒃, com 𝒃 ≠ 𝟎, temos um sistema impossível (SI);
* Caso contrário, temos duas possibilidades:

▸ Se o número de equações for igual ao número de incógnitas, temos um sistema possível e determinado (SPD).
▸ Se o número de equações for menor do que o número de incógnitas, temos um sistema possível e indeterminado (SPI).
No escalonamento, se obtivermos uma equação da forma 𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 + 𝟎𝒘 = 𝟎, devemos eliminar essa equação do sistema linear, pois essa equação é uma combinação linear das outras.
Equação linear

Definição

Nesse momento, vamos mostrar a representação genérica de uma equação linear.
Basicamente, uma equação linear é uma equação da seguinte forma:
𝒂𝟏𝒙𝟏 + 𝒂𝟐𝒙𝟐 + 𝒂𝟑𝒙𝟑 + ⋯ + 𝒂𝒏𝒙𝒏 = 𝒃

Em que 𝒙𝟏, 𝒙𝟐, 𝒙𝟑, ..., 𝒙𝒏 são incógnitas.

Os números reais 𝒂𝟏, 𝒂𝟐, 𝒂𝟑, ... ,𝒂𝒏 são os coeficientes da equação e 𝒃 é denominado termo independente.
Exemplos de equações lineares:

==2d4a97==

Equação linear Incógnitas Coeficientes
Termo independente

𝟓𝒙 + 𝟑𝒚 = 𝟐 𝒙 , 𝒚
𝟓 , 𝟑 𝟐

𝟐𝒙 + 𝟎𝒚 + 𝟑𝒛 + 𝟏𝒘 = 𝟎 𝒙, 𝒚, 𝒛, 𝒘
𝟐, 𝟎, 𝟑, 𝟏 0

𝟓𝟐𝒙𝟏 + √𝟑𝒙𝟐 + 𝟏𝒙𝟑 = 𝝅 𝒙𝟏, 𝒙𝟐, 𝒙𝟑
𝟓𝟐, √𝟑, 𝟏 𝝅

As equações a seguir não são equações lineares.

* 3√𝒙 + 2𝑦 + 𝑧 = 3

* 3𝑥 + 2𝒚𝟐 + 𝑧 = 1;

* 5𝑥 + 𝐥𝐨𝐠 𝒚 + 𝒛𝒘 = 0;

* 𝑥 + 𝑦 + 𝐜𝐨𝐬 𝒛 = 3.

Note que a principal restrição de uma equação linear está na incógnita. Não se pode ter incógnitas da forma √𝒙, 𝒚𝟐 , 𝐥𝐨𝐠 𝒚, 𝐜𝐨𝐬 𝒛, por exemplo, bem como não se pode ter produto entre incógnitas (𝒛𝒘).
Já os coeficientes e o termo independente podem ser quaisquer números reais: 5², √3, 𝜋,
etc.

Solução de uma equação linear

Uma solução de uma equação linear é um conjunto ordenado de números reais que torna a equação verdadeira.
Vamos a um exemplo. Considere a seguinte equação linear:

3𝑥 + 2𝑦 + 𝑧 = 7

Note que o conjunto ordenado (𝒙, 𝒚, 𝒛) = (𝟏, 𝟎, 𝟒) é uma solução, pois:

3𝒙 + 2𝒚 + 𝒛 = 7

Item. 3. 𝟏 + 2. 𝟎 + 𝟒 = 7

7 = 7

(VERDADEIRO)

Podemos ter infinitas soluções para a equação linear em questão. Observe que o conjunto ordenado
(𝒙, 𝒚, 𝒛) = (𝟎, 𝟎, 𝟕) também é uma solução, pois:

3𝒙 + 2𝒚 + 𝒛 = 7

Item. 3. 𝟎 + 2. 𝟎 + 𝟕 = 7

7 = 7

(VERDADEIRO)

Vejamos agora o conjunto ordenado (𝒙, 𝒚, 𝒛) = (𝟓, 𝟓, 𝟓):

3𝒙 + 2𝒚 + 𝒛 = 7

Item. 3. 𝟓 + 2. 𝟓 + 𝟓 = 7

30 = 7

(FALSO)

Note que (𝟓, 𝟓, 𝟓) não é solução da equação linear, pois esse conjunto ordenado não tornou a equação linear verdadeira.
Sistema linear

Definição

Um sistema linear nada mais é do que um conjunto de equações lineares. A seguir, temos um sistema linear,pois trata-se de um conjunto de equações lineares:

2𝑥 + 𝑦 + 𝑧 = 1

{3𝑥 + 3𝑦 + 𝑧 = 3

𝑥 + 2𝑦 + 𝑧 = 2

Agora observe o seguinte sistema de equações:

𝑥 + 𝑦 + 𝑧 = 1

{ 𝟐𝒚 = 1

𝒙𝟐𝒚 = 3

Esse sistema de equações não é linear, pois contém equações que não são lineares.

Solução de um sistema linear

Assim como as equações lineares, um sistema linear também apresenta solução. A diferença é que a solução do sistema linear deve tornar verdadeira todas as equações que compõem o sistema.
Considere, por exemplo, o seguinte sistema linear de equações:

𝑥 + 𝑦 + 𝑧 = 6

{3𝑥 + 𝑦 + 3𝑧 = 16
0𝑥 + 𝑦 + 𝑧 = 3

Note que (𝒙, 𝒚, 𝒛) = (𝟑, 𝟏, 𝟐) é solução do sistema linear, pois essa solução torna verdadeira as três equações. Vejamos:
Primeira equação 𝒙 + 𝒚 + 𝒛 = 6
𝟑 + 𝟏 + 𝟐 = 6
6 = 6
(VERDADEIRO)

Segunda equação

3𝒙 + 𝒚 + 3𝒛 = 16

Item. 3. 𝟑 + 𝟏 + 3. 𝟐 = 16

16 = 16

(VERDADEIRO)

Terceira equação

0𝒙 + 𝒚 + 𝒛 = 3

Item. 0. 𝟑 + 𝟏 + 𝟐 = 3

3 = 3

(VERDADEIRO)

Agora observe o que acontece com (𝒙, 𝒚, 𝒛) = (𝟐, 𝟐, 𝟐):

Primeira equação 𝒙 + 𝒚 + 𝒛 = 6
𝟐 + 𝟐 + 𝟐 = 6
6 = 6
(VERDADEIRO)

Segunda equação

3𝒙 + 𝒚 + 3𝒛 = 16

Item. 3. 𝟐 + 𝟐 + 3. 𝟐 = 16

14 = 16

(FALSO)

Terceira equação

0𝒙 + 𝒚 + 𝒛 = 3

Item. 0. 𝟐 + 𝟐 + 𝟐 = 3

4 = 3

(FALSO)

Como (𝒙, 𝒚, 𝒛) = (𝟐, 𝟐, 𝟐) satisfaz apenas uma equação do sistema, (𝟐, 𝟐, 𝟐) não é solução do sistema linear.
Veremos mais adiante que um sistema linear pode apresentar uma solução única, infinitas soluções ou então nenhuma solução.
Representação na forma matricial

Considere o seguinte sistema linear com três equações:

𝟐𝒙 + 𝟐𝒚 + 𝟏𝒛 = 𝟐

{𝟏𝒙 + 𝟑𝒚 + 𝟐𝒛 = 𝟏

𝟑𝒙 + 𝟏𝒚 + 𝟒𝒛 = 𝟒

Esse sistema linear também pode ser representado por meio da equação matricial 𝑨𝑿 = 𝑩:

𝟐 𝟐 𝟏 𝒙 𝟐

[𝟏 𝟑 𝟐] × [𝒚] = [𝟏]

⏟𝟑 𝟏 𝟒¸

𝑴𝒂𝒕𝒓𝒊𝒛 𝑨

⏟𝒛

𝑴𝒂𝒕𝒓𝒊𝒛 𝑿

⏟𝟒

𝑴𝒂𝒕𝒓𝒊𝒛 𝑩

𝑨𝑿 = 𝑩

Como assim, professor? Como que apareceu uma equação matricial?

Para compreender melhor a representação matricial, vamos desenvolvê-la.
Do lado esquerdo, temos o seguinte produto:

𝟐 𝟐 𝟏

[𝟏 𝟑 𝟐]

𝟑 𝟏 𝟒 ₃×₃

𝒙

× [𝒚]

𝒛 3×1

Trata-se da multiplicação de uma matriz 3 × 3 por uma matriz 3 × 1. Note que o produto é possível e que o resultado desse produto é uma matriz 3 × 1.
Logo, 𝐴𝑋 é:

𝟐 𝟐 𝟏

𝐴𝑋 = [𝟏 𝟑 𝟐]

𝒙

× [𝒚]

𝟑 𝟏 𝟒 3×3 𝒛 3×1

𝟐𝒙 + 𝟐𝒚 + 𝟏𝒛

𝐴𝑋 = [𝟏𝒙 + 𝟑𝒚 + 𝟐𝒛]

𝟑𝒙 + 𝟏𝒚 + 𝟒𝒛 3×1

Do outro lado da equação, temos uma matriz 𝐵, que também apresenta dimensão 3 × 1:

Assim, temos:

𝐵 = [𝟏]

𝟒 3×1

𝐴𝑋 = 𝐵

𝟐 𝟐 𝟏

[𝟏 𝟑 𝟐]

𝟑 𝟏 𝟒 ₃×₃

𝒙

× [𝒚]

𝒛

3×1

= [𝟏]

𝟒 3×1

𝟐𝒙 + 𝟐𝒚 + 𝟏𝒛
[𝟏𝒙 + 𝟑𝒚 + 𝟐𝒛]

𝟑𝒙 + 𝟏𝒚 + 𝟒𝒛 3×1

= [𝟏]

𝟒 3×1

Agora temos a igualdade de duas matrizes 3 × 1. Para as matrizes serem iguais, todos os elementos de mesma posição devem ser iguais:
𝟐𝒙 + 𝟐𝒚 + 𝟏𝒛 = 𝟐

{𝟏𝒙 + 𝟑𝒚 + 𝟐𝒛 = 𝟏

𝟑𝒙 + 𝟏𝒚 + 𝟒𝒛 = 𝟒

Veja que voltamos ao nosso sistema linear!

Logo, podemos representar um sistema linear tanto por meio de um conjunto de equações quanto por meio de uma equação matricial do tipo 𝑨𝑿 = 𝑩.
Vejamos alguns exemplos de representação matricial:

Representação por conjunto de equações Representação matricial 𝑨𝑿 = 𝑩

{𝟓𝒙 + 𝟑𝒚 = 𝟎

==2d4a97==

𝟓 𝟑 𝒙 𝟎

] × [ ] = [ ]

𝟏𝒙 + 𝟏𝒚 = 𝟏

𝟐𝒙 + 𝟑𝒚 = 𝟐

𝟏 𝟏 𝒚 𝟏

𝟐 𝟑 𝒙 𝟐

{𝟏𝒙 + 𝟐𝒚 = 𝟏

𝟒𝒙 + 𝟔𝒚 = 𝟒

𝟑𝒙 + 𝟒𝒚 + 𝟏𝒛 = 𝟑

[𝟏 𝟐] × [𝒚] = [𝟏]

𝟒 𝟔 𝟒

𝟑 𝟒 𝟏 𝒙 𝟑

{𝟏𝒙 + (−𝟏)𝒚 + 𝟏𝒛 = 𝟏

𝟏𝒙 + 𝟑𝒚 + 𝟎𝒛 = 𝟐

𝟑𝒙 + 𝟐𝒚 + 𝟏𝒛 = 𝟑

𝟏𝒙 + 𝟑𝒚 + (−𝟏)𝒛 = 𝟏

[𝟏 −𝟏 𝟏] × [𝒚] = [𝟏]

𝟏 𝟑 𝟎 𝒛 𝟐

𝟑 𝟐 𝟏 𝒙 𝟑

𝟏 𝟑 −𝟏 𝒚 𝟏

{ 𝟏𝒙 + 𝟑𝒚 + 𝟎𝒛 = 𝟐

𝟔𝒙 + 𝟒𝒚 + 𝟐𝒛 = 𝟔

[

𝟏 𝟑 𝟎

𝟔 𝟒 𝟐

] × [

𝒛

] = [ ]

Um ponto muito importante ao realizar a representação matricial é ordenar corretamente os coeficientes,as variáveis e os termos independentes.

Suponha, por exemplo, que temos o seguinte sistema:

𝒙 + 𝟑𝒚 + 𝒛 = 𝟓

{ 𝒛 − 𝟐𝒙 = 𝟏

𝟐𝒚 + 𝒛 + 𝟑 = 0

Devemos colocar os termos independentes no lado direito da equação. Nesse caso, a última equação deve ser modificada:
𝒙 + 𝟑𝒚 + 𝒛 = 𝟓

{ 𝒛 − 𝟐𝒙 = 𝟏

𝟐𝒚 + 𝒛 = −𝟑

Além disso, devemos ordenar as variáveis da forma correta:

𝒙 + 𝟑𝒚 + 𝒛 = 𝟓

{ −𝟐𝒙 + 𝒛 = 𝟏

𝟐𝒚 + 𝒛 = −𝟑

Por fim, quanto aos coeficientes, deve-se entender que:

* Variáveis que aparecem em outras equações e não aprecem em uma determinada equação devem ser representadas com um coeficiente 0;
* Variáveis que supostamente não apresentam coeficiente na verdade têm coeficiente 1.

Ficamos com:

𝟏𝒙 + 𝟑𝒚 + 𝟏𝒛 = 𝟓

{ −𝟐𝒙 + 𝟎𝒚 + 𝟏𝒛 = 𝟏

𝟎𝒙 + 𝟐𝒚 + 𝟏𝒛 = −𝟑

Portanto, o sistema original apresenta a seguinte forma matricial 𝑨𝑿 = 𝑩:

𝟏 𝟑 𝟏 𝒙 𝟓

[−𝟐 𝟎 𝟏] × [𝒚] = [ 𝟏 ]

𝟎 𝟐 𝟏 𝒛 −𝟑

Importante destacar que a matriz 𝑨 é conhecida por matriz dos coeficientes ou também matriz incompleta do sistema. Já a matriz 𝑿 é a matriz das incógnitas e a matriz 𝑩 é a matriz dos termos independentes.
Por fim, você deve saber que a matriz completa do sistema é a matriz formada pela matriz incompleta
(𝑨)
concatenada com a matriz dos termos independentes (𝑩). Para o exemplo anterior, a matriz completa é dada por:
𝟏 𝟑 𝟏 𝟓
[𝑨|𝑩] = [−𝟐 𝟎 𝟏 𝟏 ]

𝟎 𝟐 𝟏 −𝟑

O esquema a seguir resume o que vimos sobre a representação matricial de um sistema linear.

Representação matricial de um sistema linear:

𝑨𝑿 = 𝑩

*𝑨: Matriz dos coeficientes ou matriz incompleta do sistema;

* 𝑿: Matriz das incógnitas;

* 𝑩: Matriz dos termos independentes;

* [𝑨|𝑩]: Matriz completa do sistema.

𝟑𝒙 + 𝟒𝒚 + 𝟏𝒛 = 𝟑

𝟑 𝟒 𝟏 𝒙 𝟑

{𝟏𝒙 + (−𝟏)𝒚 + 𝟏𝒛 = 𝟏

𝟏𝒙 + 𝟑𝒚 + 𝟎𝒛 = 𝟐

→ [𝟏 −𝟏 𝟏] × [𝒚] = [𝟏]

𝟏 𝟑 𝟎 𝒛 𝟐

𝟑 𝟒 𝟏 𝟑

[𝑨|𝑩] = [𝟏 −𝟏 𝟏 𝟏]

𝟏 𝟑 𝟎 𝟐

(SEDUC AM/2014) Considere o sistema linear de três equações e duas incógnitas a seguir:

𝑥 + 2𝑦 = 3

{3𝑥 + 4𝑦 = 5
5𝑥 + 6𝑦 = 7

Esse sistema escrito na forma matricial é:

1 2 3

a) [3 4] [𝑥 𝑦] = [5]

5 6 7

b) [1 3 4] [𝑥] = [3 5 7]

2 4 6 𝑦

1 2 3

c) [𝑥 𝑦] [3 4] = [5]

5 6 7

1 2 𝑥 3

d) [3 4] [𝑦] = [5]

5 6

1 3 4

3 𝑥 e) [2 4 6] [5] = [𝑦]
Comentários:

A representação de um sistema linear com 𝟑 equações e 𝟐 incógnitas na forma matricial é dado por
𝑨𝑿 = 𝑩, em que:

* 𝑨 é a matriz dos coeficientes, da forma 3 × 2;

* 𝑿 é a matriz das incógnitas, da forma 2 × 1; e

* 𝑩 é a matriz dos termos independentes, da forma 3 × 1.

Para o sistema:

Temos:

𝑥 + 2𝑦 = 3

{3𝑥 + 4𝑦 = 5
5𝑥 + 6𝑦 = 7

𝟏𝒙 + 𝟐𝒚 = 𝟑

→ {𝟑𝒙 + 𝟒𝒚 = 𝟓

𝟓𝒙 + 𝟔𝒚 = 𝟕

𝑨𝑿 = 𝑩

𝟏 𝟐 𝒙 𝟑

[𝟑 𝟒] [𝒚] = [𝟓]

𝟓 𝟔 𝟕

Gabarito: Letra D.

Sistemas lineares equivalentes

O entendimento do que são sistemas equivalentes será bastante útil adiante, quando estudarmos a solução de um sistema linear e a discussão de um sistema linear. Vamos à definição:
Definição

Dois sistemas lineares são equivalentes quando apresentam as mesmas soluções.

Exemplo: considere os sistemas lineares 𝑆₁ e 𝑆₂.

𝑆₁

𝑥 + 3𝑦 = 7

{5𝑥 + 𝑦 = 7

𝑆₂

{ 𝑥 + 3𝑦 = 7

14𝑦 = −28

Ainda veremos como obter as soluções de um sistema linear. Nesse momento, você deve acreditar em mim:ambos os sistemas admitem uma única solução dada por (𝑥, 𝑦) = (1, 2).

Assim, como ambos os sistemas apresentam as mesmas soluções (no caso, uma solução única), eles são equivalentes.
Podemos representar a equivalência entre dois sistemas por meio de um til " ~ ". Portanto:

𝑥 + 3𝑦 = 7

{

5𝑥 + 𝑦 = 7

𝑥 + 3𝑦 = 7

~ { 14𝑦 = −28

A equivalência entre dois sistemas também pode ser representada por meio da matriz completa do sistema:
1 3 7 1 3 7

[ ] ~ [ ]

5 1 7 0 −14 28

Combinação linear de equações

Na aula de determinantes, tratamos do conceito de combinação linear. Vamos recapitular a ideia,
aplicando o conceito para equações lineares.
Podemos dizer que uma equação L₁ é combinação linear de outras equações L₂ e L₃
quando existem valores reais 𝒂 e 𝒃 tais que:
L₁ = 𝒂L₂ + 𝒃L₃

Vejamos um exemplo:

Exemplo 1. Considere as três equações abaixo:

𝑥 + 𝑦 + 𝑧 = 5
2𝑥 + 𝑦 + 3𝑧 = 3

3𝑥 + 2𝑦 + 4𝑧 = 8

Note que a terceira equação (L₃) é combinação linear da primeira (L₁) com a segunda
(L₂), pois

L₃ = 𝟏L₁ + 𝟏L₂.

Nem sempre é fácil identificar uma combinação linear. Vejamos um outro exemplo:

Exemplo 2. Considere as três equações abaixo:

𝑥 − 𝑦 + 𝑧 = −1
2𝑥 + 𝑦 + 𝑧 = 3

5𝑥 + 1𝑦 + 3𝑧 = 5

Temos que a primeira equação (L₁) é combinação linear da segunda (L₂) e da terceira
(L₃), pois

L₁ = (−𝟐)L₂ + 𝟏L₃. Veja:

(−𝟐)𝑳𝟐 −𝟒𝒙 − 𝟐𝒚 − 𝟐𝒛 = −6

𝟏𝑳𝟑 𝟓𝒙 + 𝟏𝒚 + 𝟑𝒛 = 5
(−𝟐)𝑳𝟐 + 𝟏𝑳𝟑 𝒙 − 𝒚 + 𝒛 = −1

Obtenção de sistemas lineares equivalentes

Uma propriedade importante dos sistemas lineares diz respeito à combinação linear de equações.

Em um sistema linear, ao substituir uma determinada equação por uma combinação linear dela com outra equação, temos um sistema linear equivalente.
Considere o seguinte sistema linear:

𝑥 + 3𝑦 = 7

{

5𝑥 + 𝑦 = 7

Ao substituir a segunda equação (𝑳𝟐) pela combinação linear 𝟏𝑳𝟐 + (−𝟓)𝑳𝟏, obtemos um novo sistema linear que é equivalente ao primeiro.
Como 𝟏L₂ + (−𝟓)L₁ corresponde a −𝟏𝟒𝒚 = −𝟐𝟖, ficamos com:

𝑥 + 3𝑦 = 7

{

5𝑥 + 𝑦 = 7

𝑥 + 3𝑦 = 7

~ { 14𝑦 = −28

Para facilitar a comunicação, a substituição de 𝑳𝟐 por 𝑳𝟐 + (−𝟓)𝑳𝟏 será denotada da seguinte forma:
𝑳𝟐 ← 𝟏𝑳𝟐 + (−𝟓)𝑳𝟏

A propriedade aprendida é válida quando substituímos a equação por uma combinação linear de equações que contenha a equação original. Para o exemplo apresentado:
==2d4a97==

𝑳𝟐 ← 1𝑳𝟐 + (−5)L₁

Vamos a um outro exemplo. Considere o seguinte sistema linear:

𝑥 + 𝑦 + 𝑧 = 3

{𝑥 + 2𝑦 + 2𝑧 = 4
2𝑥 + 4𝑦 + 𝑧 = 5

Ao substituir a segunda equação (L₂) pela combinação linear 𝟏L₂ + (−𝟏)L₁, obtemos um novo sistema linear que é equivalente ao primeiro.
𝑥 + 𝑦 + 𝑧 = 3

{𝑥 + 2𝑦 + 2𝑧 = 4 ~ {
2𝑥 + 4𝑦 + 𝑧 = 5

𝑥 + 𝑦 + 𝑧 = 3

𝒚 + 𝒛 = 𝟏
2𝑥 + 4𝑦 + 𝑧 = 5

Remoção de equações do sistema linear

Em um sistema linear, quando uma determinada equação corresponde a uma combinação linear de outras equações do sistema, podemos eliminar essa equação do sistema.
Exemplo: considere o seguinte sistema.

𝒙 + 𝒚 + 𝒛 = 𝟓

{ 𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝟑𝒙 + 𝟐𝒚 + 𝟒𝒛 = 𝟖

Temos que a terceira equação é uma combinação linear da primeira com a segunda, pois 𝑳𝟑 = 𝟏𝑳𝟏
+ 𝟏𝑳𝟐.
Logo, podemos eliminar a terceira equação. Isso significa que temos a seguinte equivalência:

𝒙 + 𝒚 + 𝒛 = 𝟓

{ 𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝟑𝒙 + 𝟐𝒚 + 𝟒𝒛 = 𝟖

~ { 𝒙 + 𝒚 + 𝒛 = 𝟓

𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

A ideia por trás dessa remoção de uma equação é que, em um sistema linear, uma equação que é combinação linear de outras contém uma informação desnecessária. No caso apresentado, a informação 𝟑𝒙 + 𝟐𝒚 + 𝟒𝒛 = 𝟖 já está contida, implicitamente, nas outras duas equações.
Há uma situação análoga em que se pode eliminar uma equação do sistema linear:

Já sabemos que, em um sistema linear, ao substituir uma determinada equação por uma combinação linear dela com outra equação, temos um sistema linear equivalente.
Se nessa substituição obtivermos uma equação no seguinte formato:

0𝑥 + 0𝑦 + 0𝑧 + 0𝑤 = 0

Podemos remover essa equação do sistema linear.

Vamos utilizar o mesmo sistema linear como exemplo:

𝒙 + 𝒚 + 𝒛 = 𝟓

{ 𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝟑𝒙 + 𝟐𝒚 + 𝟒𝒛 = 𝟖

Ao substituirmos 𝑳𝟑 por 𝑳𝟑 + (−1)L₁, temos o seguinte sistema linear equivalente:

𝒙 + 𝒚 + 𝒛 = 𝟓

{ 𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝟑𝒙 + 𝟐𝒚 + 𝟒𝒛 = 𝟖

𝑥 + 𝑦 + 𝑧 = 5

~ { 2𝑥 + 𝑦 + 3𝑧 = 3

𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

Ao substituirmos novamente 𝑳𝟑 por 𝑳𝟑 + (−1)L₂, temos:

𝑥 + 𝑦 + 𝑧 = 5

{ 2𝑥 + 𝑦 + 3𝑧 = 3

𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝑥 + 𝑦 + 𝑧 = 5

~ { 2𝑥 + 𝑦 + 3𝑧 = 3

𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 = 𝟎

Note que obtivemos uma equação no formato 𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 = 𝟎. Logo, podemos eliminar essa equação.
𝑥 + 𝑦 + 𝑧 = 5

{ 2𝑥 + 𝑦 + 3𝑧 = 3 ~ {

𝒙 + 𝒚 + 𝒛 = 𝟓

𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 = 𝟎

𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

Portanto, temos que o sistema linear original é equivalente ao novo sistema linear obtido, isto é:

𝒙 + 𝒚 + 𝒛 = 𝟓

{ 𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝟑𝒙 + 𝟐𝒚 + 𝟒𝒛 = 𝟖

~ { 𝒙 + 𝒚 + 𝒛 = 𝟓

𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

Classificação de um sistema linear

Um sistema linear pode ser classificado de três formas:

* Sistema Possível e Determinado (SPD): o sistema apresenta uma única solução;

* Sistema Possível e Indeterminado (SPI): o sistema apresenta infinitas soluções; e

* Sistema Impossível (SI): ocorre quando o sistema não apresenta solução.

Sistema Linear

Possível

Possível
Determinado
(SPD)

Possível
Indeterminado
(SPI)

Solução única

Infinitas soluções

Impossível (SI) Sem solução

A seguir, vamos entender essas três classificações com maiores detalhes. O procedimento de como realizar essa classificação será visto no tópico de discussão de um sistema linear.
Um sistema linear pode apresentar solução única, infinitas soluções ou nenhuma solução.

Se um sistema linear apresenta mais de uma solução, então ele apresenta infinitas soluções.
Não existe a possibilidade de ele apresentar "apenas duas soluções", "apenas três soluções", etc.
Sistema possível e determinado (SPD)

Um sistema possível e determinado (SPD) é aquele que admite uma única solução.

Um exemplo de sistema possível e determinado é o seguinte:

x + y + z = 6

{2𝑥 + 𝑦 + 3𝑧 = 14

𝑥 + 2𝑦 + 𝑧 = 7

Isso porque ele admite uma única solução: (𝑥, 𝑦, 𝑧) = (6, 14, 7).
Para um sistema ser possível e determinado, devemos ter:

* Um número de equações igual ao número d==2d4a97==

e incógnitas;

* Essas equações não podem ser combinações lineares umas das outras (pois, nesse caso,
podemos eliminar equações); e
* Essas equações não podem se contradizer.

Sistema possível e indeterminado (SPI)

Um sistema possível e determinado (SPD) é aquele que admite infinitas soluções.

Podemos tomar como exemplo o sistema que vimos recentemente:

𝒙 + 𝒚 + 𝒛 = 𝟓

{ 𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝟑𝒙 + 𝟐𝒚 + 𝟒𝒛 = 𝟖

Lembre-se que ele é equivalente a um sistema com duas equações:

𝒙 + 𝒚 + 𝒛 = 𝟓

{ 𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝟑𝒙 + 𝟐𝒚 + 𝟒𝒛 = 𝟖

~ { 𝒙 + 𝒚 + 𝒛 = 𝟓

𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

Veja que (𝒙, 𝒚, 𝒛) = (𝟎, 𝟔, −𝟏), bem como (−𝟒, 𝟖, 𝟏) e (−𝟐, 𝟕 𝟎) são soluções do sistema linear.
Solução (𝒙, 𝒚, 𝒛) Teste em 𝒙 + 𝒚 + 𝒛 = 𝟓
Teste em 𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑
(𝟎, 𝟔, −𝟏) 0 + 6 + (−1) = 5 → 𝑶𝑲 2.0 + 6 +
Item. 3. (−1) = 3 → 𝑶𝑲

(−𝟒, 𝟖, 𝟏) (−4) + 8 + 1 = 5 → 𝑶𝑲 2. (−4) +
8 + 3.1 = 3 → 𝑶𝑲

(−𝟐, 𝟕, 𝟎) (−2) + 7 + 0 = 5 → 𝑶𝑲 2. (−2) +
7 + 3.0 = 3 → 𝑶𝑲

Além dessas três soluções, temos infinitas outras. Logo, o sistema é possível e indeterminado.

Sistema impossível (SI)

O sistema impossível ocorre quando o sistema não apresenta solução.
Exemplo:

𝑥 + 𝑦 + 𝑧 = 5

{𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟑

𝟐𝒙 + 𝒚 + 𝟑𝒛 = 𝟒

Observe o que a segunda e a terceira equação estão nos dizendo: em uma equação,
temos que
"𝟐𝒙 + 𝒚 + 𝟑𝒛" é igual a 3 e, na outra, temos que essa mesma soma é igual a 4.

Ora, não é possível encontrar uma solução (𝑥, 𝑦, 𝑧) cuja soma " 𝟐𝒙 + 𝒚 + 𝟑𝒛" seja igual a 3
e a 4 ao mesmo tempo. Logo, o sistema é impossível.
Sistema linear homogêneo

Um sistema linear homogêneo é aquele em que os termos independentes de todas as equações são iguais a zero.
Exemplo:

3𝑥 + 1𝑦 + 𝑧 = 𝟎

{2𝑥 + 4𝑦 + 2𝑧 = 𝟎
3𝑥 + 2𝑦 + 4𝑧 = 𝟎

Observe que (𝒙, 𝒚, 𝒛) = (𝟎, 𝟎, 𝟎) é solução desse sistema.

Um sistema linear homogêneo é sempre possível, pois sempre admite a solução em que todas as variáveis são zero (denominada solução trivial).
* Se o sistema linear homogêneo admitir somente a solução trivial, então ele é um
Sistema Possível e
Determinado (SPD);

* Caso ele admita outras soluções, então ele admite infinitas soluções e é um Sistema Possível eIndeterminado (SPI).

Sistema Linear
Homogêneo

Sempre é
Possível

Possível e
Determiando

(SPD)

Possível e

Solução única
(trivial)

Indeterminado
(SPI)

Infinitas soluções

(inclui a trivial)

(ANPEC/2001) Julgue o item a seguir como certo ou errado.

Um sistema homogêneo de equações lineares sempre tem solução.

Comentários:

Um sistema homogêneo de equações lineares, ou seja, um sistema linear homogêneo, é sempre possível,
isto é, sempre admite ao menos uma solução, a solução trivial.

Gabarito: CERTO.

Solução de um sistema linear

Pessoal, até o momento o estudo foi mais voltado para a construção de uma base teórica. A partir de agora,temos que redobrar a atenção.

Solução por substituição

A solução por substituição consiste em isolar uma variável em uma equação e substituir em outra equação.Veja o próximo exemplo:

𝟑𝒙 + 𝟐𝒚 = 𝟐

Encontre a solução do seguinte sistema linear: { 𝟐𝒙 + 𝒚 = 𝟒 .

A partir da segunda equação, podemos isolar 𝑦:

2𝑥 + 𝑦 = 4

𝒚 = 𝟒 − 𝟐𝒙

Substituindo esse 𝒚 na primeira equação, temos:

3𝑥 + 2𝒚 = 2

3𝑥 + 2. (𝟒 − 𝟐𝒙) = 2

3𝑥 − 8 − 4𝑥 = 2

−𝑥 + 8 = 2

−𝑥 = −6

𝒙 = 𝟔

Como 𝒚 = 𝟒 − 𝟐𝒙, temos:

𝑦 = 4 − 2𝒙 𝑦 = 4 − 2. 𝟔
𝒚 = −𝟖

Logo, a solução do sistema em questão é (𝒙, 𝒚) = (𝟔, −𝟖).

(SEFAZ AM/2022) 𝑥 e 𝑦 são tais que 4𝑥 + 5𝑦 = 80 e 6𝑥 + 7𝑦 = 116. O valor de 2𝑥 + 3𝑦 é:

a) 38

b) 40

c) 42

d) 44

e) 46

Comentários:

Vamos resolver o sistema linear por substituição. Temos o seguinte sistema linear:

{ 4𝑥 + 5𝑦 = 80
6𝑥 + 7𝑦 = 116

A partir da primeira equação, podemos isolar 𝑥:

4𝑥 + 5𝑦 = 80

4𝑥 = 80 − 5𝑦

𝟖𝟎 − 𝟓𝒚 𝒙 =
Substituindo o valor de 𝑥 na segunda equação, temos:

6𝑥 + 7𝑦 = 116

80 − 5𝑦

6 × (

3 × (

80 − 5𝑦

) + 7𝑦 = 116

) + 7𝑦 = 116

3 × (40 − 2,5𝑦) + 7𝑦 = 116

120 − 7,5𝑦 + 7𝑦 = 116

−0,5𝑦 = 116 − 120

−0,5𝑦 = −4

−4

𝑦 =

−0,5

𝒚 = 𝟖

Substituindo o valor de 𝑦 em 𝒙 =

𝟖𝟎−𝟓𝒚

, temos:

𝑥 =

80 − 5𝑦 𝑥 =
80 − 5 × 8

80 − 40

𝑥 =

𝑥 =

𝒙 = 𝟏𝟎

Logo, o valor procurado é:

Gabarito: Letra D.

2𝑥 + 3𝑦

= 2 × 10 + 3 × 8

= 20 + 24

= 44

Solução por eliminação de variável

Consiste em eliminar variáveis por meio de uma combinação linear conveniente das equações do sistema linear.
Trata-se de uma solução não muito metodológica, uma vez que não há uma clareza do passo a passo a ser seguido.
Veremos, mais adiante, que o método do escalonamento é uma versão procedimental do que aprenderemos nesse tópico.
Vejamos dois exemplos:

𝟑𝒙 + 𝟐𝒚 = 𝟐

Encontre a solução do seguinte sistema linear: {𝟐𝒙 − 𝟐𝒚 = 𝟑

Ao realizar a soma das duas primeiras equações, isto é, a combinação linear 𝑳𝟏 + 𝑳𝟐, elimina-se a variável 𝑦:
𝑳𝟏 3𝑥 + 2𝑦 = 2

𝑳𝟐 2𝑥 − 2𝑦 = 3

𝑳𝟏 + 𝑳𝟐 𝟓𝒙 = 𝟓

Dividindo ambos os lados da equação por 5, ficamos com:

𝒙 = 𝟏

Para obter 𝑦, podemos substituir o valor de 𝒙 em qualquer uma das equações do sistema linear.
Vamos substituir na primeira:
3𝒙 + 2𝑦 = 2

Item. 3. 𝟏 + 2𝑦 = 2

2𝑦 = 2 − 3

2𝑦 = −1

𝒚 = −

Logo, a solução do sistema em questão é (

𝒙, 𝒚)

= (𝟏, − 𝟏 .

𝒙 + 𝟐𝒚 + 𝒛 = 𝟓

Encontre a solução do seguinte sistema linear: {𝟐𝒙 + 𝟐𝒚 + 𝟑𝒛 = 𝟗

𝒙 + 𝒚 + 𝒛 = 𝟑

Ao realizar a combinação linear 𝑳𝟏 + (−𝟏)𝑳𝟑, elimina-se as variáveis 𝑥 e 𝑧:

𝑳𝟏 𝑥 + 2𝑦 + 𝑧 = 5
(−𝟏)𝑳𝟑 −𝑥 − 𝑦 − 𝑧 = −3

𝑳𝟏 + (−𝟏)𝑳𝟑 𝒚 = 𝟐

Ao realizar a combinação linear 𝑳𝟐 + (−𝟐)𝑳𝟑, elimina-se as variáveis 𝑥 e 𝑦:

𝑳𝟐 2𝑥 + 2𝑦 + 3𝑧 = 9
(−𝟐)𝑳𝟑 −2𝑥 − 2𝑦 − 2𝑧 = −6

𝑳𝟏 + (−𝟏)𝑳𝟑 𝒛 = 𝟑

Temos, portanto, que 𝒚 = 𝟐 e 𝒛 = 𝟑. Para obter 𝑥, podemos substituir esses valores em qualquer uma das equações do sistema linear. Vamos substituir na terceira:
𝑥 + 𝒚 + 𝒛 = 3

𝑥 + 𝟐 + 𝟑 = 3

𝒙 = −𝟐

==2d4a97==

Portanto, a solução do sistema linear é (𝒙, 𝒚, 𝒛) = (−𝟐, 𝟐, 𝟑).

Solução pela soma das equações do sistema

Pessoal, existem casos em que a solução do sistema linear é obtida de modo mais rápido realizando a soma de todas as equações do sistema. Vejamos um exemplo:
𝒙 + 𝒚 = 𝟑

Encontre a solução do seguinte sistema linear: {𝒙 + 𝒛 = 𝟒

𝒚 + 𝒛 = 𝟓

Somando todas as equações do sistema, isto é, realizando a combinação linear 𝑳𝟏 + 𝑳𝟐 + 𝑳𝟑,
temos:

𝑳𝟏

𝑳𝟐

𝑳𝟑

𝑥 + 𝑦 = 3

𝑥 + 𝑧 = 4

𝑦 + 𝑧 = 5

𝑳𝟏 + 𝑳𝟐 + 𝑳𝟑 2𝑥 + 2𝑦 + 2𝑧 = 12

Ficamos com:

2(𝑥 + 𝑦 + 𝑧) = 12

𝒙 + 𝒚 + 𝒛 = 𝟔

A partir dessa informação, podemos subtrair cada equação do sistema linear de 𝒙 + 𝒚 + 𝒛 = 𝟔.

𝒙 + 𝒚 + 𝒛 = 𝟔
(−𝟏)𝑳𝟏 −𝑥 − 𝑦 = −3

𝒛 = 𝟑

𝒙 + 𝒚 + 𝒛 = 𝟔
(−𝟏)𝑳𝟐 −𝑥 + − 𝑧 = −4

𝒚 = 𝟐

𝒙 + 𝒚 + 𝒛 = 𝟔

(−𝟏)𝑳𝟑 − 𝑦 − 𝑧 = −5

𝒙 = 𝟏

Portanto, a solução do sistema linear é (𝒙, 𝒚, 𝒛) = (𝟏, 𝟐, 𝟑).

(MPE SC/2022) No sistema o valor de 𝑎 é:a) -1;

b) 1;

c) 2;

d) 3;

e) 4.

Comentários:

3𝑎 + 𝑏 + 𝑐 + 𝑑 = 16

{ 𝑎 + 3𝑏 + 𝑐 + 𝑑 = 6

𝑎 + 𝑏 + 3𝑐 + 𝑑 = 14

𝑎 + 𝑏 + 𝑐 + 3𝑑 = 12

Ao somar todas as equações do sistema linear, temos:

3𝑎 + 𝑏 + 𝑐 + 𝑑 = 16

𝑎 + 3𝑏 + 𝑐 + 𝑑 = 6

𝑎 + 𝑏 + 3𝑐 + 𝑑 = 14

𝑎 + 𝑏 + 𝑐 + 3𝑑 = 12
6𝑎 + 6𝑏 + 6𝑐 + 6𝑑 = 48

Ficamos com:

6(𝑎 + 𝑏 + 𝑐 + 𝑑) = 48

𝒂 + 𝒃 + 𝒄 + 𝒅 = 𝟖

A partir dessa informação, podemos subtrair 𝒂 + 𝒃 + 𝒄 + 𝒅 = 𝟖 da primeira equação do sistema linear.
3𝑎 + 𝑏 + 𝑐 + 𝑑 = 16

−𝒂 − 𝒃 − 𝒄 − 𝒅 = −𝟖

𝟐𝒂 = 𝟖

Logo, dividindo os dois lados da equação por 2, temos 𝒂 = 𝟒.

Gabarito: Letra E.

(TCE TO/2022) Considere o sistema:

O valor de 𝑥 é:
a) 3/2;

b) 5/2;

c) 7/2;

d) 9/2;

e) 11/2.

Comentários:

𝑥 + 𝑦 + 5𝑧 = 0

{𝑥 + 5𝑦 + 𝑧 = 14
5𝑥 + 𝑦 + z = 28

Ao somar todas as equações do sistema linear, temos:

𝑥 + 𝑦 + 5𝑧 = 0

𝑥 + 5𝑦 + 𝑧 = 14
5𝑥 + 𝑦 + 𝑧 = 28

7𝑥 + 7𝑦 + 7𝑧 = 42

Ficamos com:

7(𝑥 + 𝑦 + 𝑧) = 42

𝑥 + 𝑦 + 𝑧 =

𝑥 + 𝑦 + 𝑧 = 6

A partir dessa informação, podemos subtrair 𝒙 + 𝒚 + 𝒛 = 𝟔 da terceira equação do sistema linear.
5𝑥 + 𝑦 + 𝑧 = 28

−𝒙 − 𝒚 − 𝒛 = −𝟔

𝟒𝒙 = 𝟐𝟐

Portanto:

Gabarito: Letra E.

Solução por matriz inversa 𝑥 =
𝑥 =

Considere um sistema linear cujo número de equações (𝒏) é igual ao número de incógnitas. Note que,
nesse caso, a matriz dos coeficientes (𝑨) do sistema linear será quadrada, de dimensão 𝒏 × 𝒏.
O sistema pode ser escrito na forma matricial do seguinte modo:

𝑨𝒏×𝒏𝑿𝒏×𝟏 = 𝑩𝒏×𝟏

Supondo que 𝐝𝐞𝐭 𝑨 ≠ 𝟎, você deve se lembrar da aula de determinantes que a matriz 𝑨 possui inversa. Ao multiplicar ambos os lados da equação por 𝐴−¹ pela esquerda, temos:
𝑨−𝟏𝑨𝑿 = 𝑨−𝟏𝑩

Pela definição de matriz inversa, temos que 𝑨−𝟏𝑨 = 𝑰. Logo:

𝑰𝑿 = 𝑨−𝟏𝑩

Como a matriz identidade é o elemento neutro da multiplicação de matrizes, ficamos com:

𝑿 = 𝑨−𝟏𝑩

Veja, portanto, que a matriz das incógnitas (𝑿) é obtida pelo produto da matriz inversa dos coeficientes pela matriz dos termos independentes.
Vamos resolver um exemplo.

𝟑𝒙 + 𝟐𝒚 = 𝟐

Encontre a solução do seguinte sistema linear: {𝟐𝒙 − 𝟐𝒚 = 𝟑

No sistema linear apresentado, a matriz dos coeficientes é dada por

3 2

𝐴 = [ ] e matriz dos termos

2 −2

independentes é

𝐵 = [

]. Note que a matriz 𝐴 é inversível, pois:

det 𝐴 = [3 × (−2)] − [2 × 2] = −10

Da aula sobre determinantes, você deve se lembrar que, para uma matriz 𝒂 𝒃
𝐴 = [𝒄 𝒅], a sua inversa é dada por 𝐴−¹ = 1
det 𝐴

[ 𝒅 −𝒃]. Logo, para o nosso caso:

−𝒄 𝒂

𝐴−1 = 1

−2 −2

−10

[ ]

−2 3

A matriz dos coeficientes 𝑿 do sistema linear em questão é:

𝑿 = 𝑨−𝟏𝑩

𝑥 1

−𝟐 −𝟐 𝟐

[𝑦] = −10 [−𝟐 𝟑 ] [𝟑]

= − 1 [(−𝟐). 𝟐 + (−𝟐). 𝟑]
10 (−𝟐). 𝟐 + 𝟑. 𝟑

= − 1 [−10]

10 5

− . (−10)

= [ 1

− . 5

] = [−1/2]

𝑥

Veja que

1 ], isto é, 𝑥 = 1 e 𝑦 = − 1

( ) 𝟏 .

[𝑦] = [

−1/2

. Portanto, a solução do sistema linear é 𝒙, 𝒚
= (𝟏, − )

𝑥

(PETROBRAS/2008) A matriz 𝑋 = [𝑦], solução do sistema de equações lineares

{2𝑥 + 3𝑦 = 185
3𝑥 + 2𝑦 = 190

pode ser expressa na forma 𝑋 = 𝑃𝐵, em que 𝐵 = [195] é a matriz dos termos constantes do sistema, 𝑃 é uma matriz constante, quadrada, de dimensão 2 × 2. Nesse caso, assinale a opção correspondente à matriz
𝑃.

3 − 2

a) [⁵ ⁵

5 5

1 2

b) [⁵ ⁵

5 5

2 3

c) [⁵ ⁵

5 5

− 2 3

d) [ ⁵ ⁵ ]

3 − 2

5 5

− 1 2

e) [ ⁵ ⁵ ]

2 − 1

5 5

Comentários:

Considerando o sistema apresentado:

{2𝑥 + 3𝑦 = 185
3𝑥 + 2𝑦 = 190

Temos que a matriz dos coeficientes é 𝑨 = [2 3]. Como det 𝐴 ≠ 0, então a matriz 𝑨 é inversível.
3 2

det 𝐴 = [2.2] − [3.3] = 4 − 9 = −5

O sistema linear pode ser representado na sua forma matricial por:

𝑨𝑿 = 𝑩

Como a matriz 𝐴 é inversível, podemos multiplicar ambos os lados da equação por 𝐴−¹ pela esquerda:
𝑨−𝟏𝑨𝑿 = 𝑨−𝟏𝑩

𝑰𝑿 = 𝑨−𝟏𝑩

𝑿 = 𝑨−𝟏𝑩

Comparando 𝑿 = 𝑨−𝟏𝑩 a equação matricial apresentada no enunciado, dada por 𝑿 = 𝑷𝑩,
temos que

𝑷 = 𝑨−𝟏.

Para uma matriz 𝒂 𝒃 1
𝐴 = [ ], a sua inversa é dada por 𝐴 =

[ 𝒅 −𝒃]. Logo, para o nosso caso:

𝒄 𝒅 det 𝐴
−𝒄 𝒂

1 1 2 3

−1 1

2 −3

− × 2 − × (−3) −

5 5 5 5

𝐴 =

− 2

Portanto, 𝑃 = 𝐴−¹ = [ ⁵

−5 [−3 2

5 ]

] = [ 1

−

× (−3) − × 2

] = [ ]

−

5 5

Gabarito: Letra D.

3 − 2

5 5

Teorema de Cramer

Primeiramente, deve-se entender que o Teorema de Cramer só pode ser utilizado quando o número de equações do sistema linear (𝒏) é igual ao número de incógnitas. Nesse caso, a matriz dos coeficientes (𝑨)do sistema linear será quadrada, de dimensão 𝒏 × 𝒏.

Considere, então, um sistema linear escrito na forma matricial:

𝑨𝒏×𝒏𝑿𝒏×𝟏 = 𝑩𝒏×𝟏

Vamos chamar de 𝑫 o determinante da matriz dos coeficientes (𝑨). Ou seja:

𝐷 = det 𝐴

O Teorema de Cramer nos diz duas coisas:

01) Se 𝐷 ≠ 0, o sistema é possível e determinado (SPD), apresentando solução única.

02) Sendo 𝐷 ≠ 0, a solução única (𝛼₁, 𝛼₂, ... 𝛼𝑛) do sistema linear é tal que:

𝛼𝑖

= 𝐷𝑖

𝐷

Onde 𝐷𝑖 é o determinante da matriz que se obtém a partir de 𝐴𝑛×𝑛 substinuindo a coluna 𝑖 pela matriz 𝐵𝑛×1.
Professor, não entendi nada!

Calma, concurseiro. O entendimento só virá com o desenvolvimento do próximo exemplo. Ao acompanhá-
lo, o Teorema de Cramer fica mais claro.

𝒙 + 𝟐𝒚 + 𝒛 = 𝟓

Encontre a solução do seguinte sistema linear {𝟐𝒙 + 𝟐𝒚 + 𝟑𝒛 = 𝟗 pelo Teorema de Cramer.

𝒙 + 𝒚 + 𝒛 = 𝟑

Ao representar o sistema linear na sua forma matricial, temos 𝐴𝑋 = 𝐵, sendo:

1 2 1

𝑥 5

𝐴 = [2 2 3] 𝑋 = [𝑦] 𝐵 = [9]

1 1 1

𝑧 3

Primeiro, devemos obter o determinante da matriz 𝐴:

1 2 1

𝐷 = det 𝐴 = |2 2 3|

1 1 1

Aplicando a Regra de Sarrus, ficamos com:

1 2 1 1 2

|2 2 3| 2 2

1 1 1 1 1

Parte Negativa Parte Positiva

𝐷 = [𝟏. 𝟐. 𝟏 + 𝟐. 𝟑. 𝟏 + 𝟏. 𝟐. 𝟏] − [𝟏. 𝟐. 𝟏 + 𝟏. 𝟑. 𝟏 + 𝟐. 𝟐. 𝟏]

𝐷 = 10 − 9

𝐷 = 1

Como 𝐷 ≠ 0, o sistema é possível e determinado (SPD), sendo possível aplicar o teorema.

Obtenção de 𝒙

Para obter 𝑥, vamos utilizar a seguinte relação:

𝑥 =

𝐷𝑥

𝐷

Já temos o valor do determinante 𝐷. Nesse momento, devemos obter 𝐷𝑥.

𝐷𝑥 é o determinante da matriz que se obtém a partir da matriz 𝐴 substituindo a coluna dos coeficientes da variável 𝒙 pela matriz 𝐵.
Coeficientes de 𝒙

𝟏 𝟐 𝟏 𝟓

𝐴 = [𝟐 𝟐 𝟑] 𝐵 = [𝟗]

𝟏 𝟏 𝟏 𝟑

Aplicando a Regra de Sarrus, ficamos com:

𝟓 𝟐 𝟏

𝐷𝑥 = |𝟗 𝟐 𝟑|

𝟑 𝟏 𝟏

5 2 1 5 2

|9 2 3| 9 2

3 1 1 3 1

Logo:

Parte Negativa Parte Positiva

𝐷𝑥 = [𝟓. 𝟐. 𝟏 + 𝟐. 𝟑. 𝟑 + 𝟏. 𝟗. 𝟏] − [𝟏. 𝟐. 𝟑 + 𝟓. 𝟑. 𝟏 + 𝟐. 𝟗. 𝟏]

𝐷𝑥 = 37 − 39

𝐷𝑥 = −2

𝑥 =

𝐷𝑥 −2

=

𝐷 1

𝑥 = −2

Obtenção de 𝒚

𝐷𝑦 é o determinante da matriz que se obtém a partir da matriz 𝐴 substituindo a coluna dos coeficientes da variável 𝒚 pela matriz 𝐵.
Coeficientes de 𝒚

𝟏 𝟐 𝟏 𝟓

𝐴 = [𝟐 𝟐 𝟑] 𝐵 = [𝟗]

𝟏 𝟏 𝟏 𝟑

Aplicando a Regra de Sarrus, ficamos com:

𝟏 𝟓 𝟏

𝐷𝑦 = |𝟐 𝟗 𝟑|

𝟏 𝟑 𝟏

1 5 1 1 5

|2 9 3| 2 9

1 3 1 1 3

Logo:

Parte Negativa Parte Positiva

𝐷𝑦 = [𝟏. 𝟗. 𝟏 + 𝟓. 𝟑. 𝟏 + 𝟏. 𝟐. 𝟑] − [𝟏. 𝟗. 𝟏 + 𝟏. 𝟑. 𝟑 + 𝟓. 𝟐. 𝟏]

𝐷𝑦 = 30 − 28

𝐷𝑦 = 2

𝑦 =

𝐷𝑦 2

=

𝐷 1

𝑦 = 2

Obtenção de 𝒛

𝐷𝑧 é o determinante da matriz que se obtém a partir da matriz 𝐴 substituindo a coluna dos coeficientes da variável 𝒛 pela matriz 𝐵.
Coeficientes de 𝒛

𝟏 𝟐 𝟏 𝟓

𝐴 = [𝟐 𝟐 𝟑] 𝐵 = [𝟗]

𝟏 𝟏 𝟏 𝟑

Aplicando a Regra de Sarrus, ficamos com:

𝟏 𝟐 𝟓

𝐷𝑧 = |𝟐 𝟐 𝟗|

𝟏 𝟏 𝟑

1 2 5 1 2

|2 2 9| 2 2

1 1 3 1 1

Logo:

Parte Negativa Parte Positiva

𝐷𝑧 = [𝟏. 𝟐. 𝟑 + 𝟐. 𝟗. 𝟏 + 𝟓. 𝟐. 𝟏] − [𝟓. 𝟐. 𝟏 + 𝟏. 𝟗. 𝟏 + 𝟐. 𝟐. 𝟑]

𝐷𝑧 = 34 − 31

𝐷𝑧 = 3

𝑧 =

𝐷𝑧 3

=

𝐷 1

𝑧 = 3

Portanto, a solução do sistema linear é (𝒙, 𝒚, 𝒛) = (𝟏, 𝟐, 𝟑).

(AFRFB/2012) Considere o sistema de equações lineares dado por:

𝑥 + 𝑦 + 𝑧 = 0

{ 𝑥 − 𝑦 + 𝑟𝑧 = 2

𝑟𝑥 + 2𝑦 + 𝑧 = −1

Sabendo-se que o sistema tem solução única para 𝑟 ≠ 0 e 𝑟 ≠ 1, então o valor de 𝑥 é igual a a)
𝑟

−2

b)

𝑟 c)
𝑟

−1

d)

𝑟 e) 2𝑟
Comentários:

Vamos resolver essa questão com o Teorema de Cramer.

Note que as variáveis do sistema são 𝑥, 𝑦 e 𝑧, sendo 𝑟 uma constante.

Ao representar o sistema linear na sua forma matricial, temos 𝐴𝑋 = 𝐵, sendo:

1 1 1 𝑥 0

𝐴 = [1 −1 𝑟] 𝑋 = [𝑦] 𝐵 = [ 2 ]

𝑟 2 1 𝑧 −1

Primeiro, devemos obter o determinante da matriz 𝐴:

1 1 1

𝐷 = det 𝐴 = |1 −1 𝑟|

𝑟 2 1

Aplicando a Regra de Sarrus, ficamos com:

1 1 1 1 1

|1 −1 𝑟| 1 −1

𝑟 2 1 𝑟 2

Parte Negativa Parte Positiva

𝐷 = [𝟏. (−𝟏). 𝟏 + 𝟏. 𝒓. 𝒓 + 𝟏. 𝟏. 𝟐] − [𝟏. (−𝟏). 𝒓 + 𝟏. 𝒓. 𝟐 + 𝟏. 𝟏. 𝟏]

𝐷 = [𝑟² + 1] − [𝑟 + 1]

𝐷 = 𝑟² − 𝑟

𝐷 = 𝑟(𝑟 − 1)

O enunciado pede a solução para 𝑟 ≠ 0 e 𝑟 ≠ 1. Note que, para esse caso, 𝑫 será diferente de zero.Portanto, podemos aplicar o Teorema de Cramer.

Para obter 𝑥, vamos utilizar a seguinte relação:

𝑥 =

𝐷𝑥

𝐷

𝐷𝑥 é o determinante da matriz que se obtém a partir da matriz 𝐴 substituindo a coluna dos coeficientes da variável 𝒙 pela matriz 𝐵.
Coeficientes de 𝒙

𝟏 𝟏 𝟏 𝟎

𝐴 = [𝟏 −𝟏 𝒓] 𝐵 = [ 𝟐 ]

𝒓 𝟐 𝟏 −𝟏

𝟎 𝟏 𝟏

𝐷𝑥 = | 𝟐 −𝟏 𝒓|

−𝟏 𝟐 𝟏

Aplicando a Regra de Sarrus, ficamos com:

0 1 1 0 1

| 2 −1 𝑟|

−1 2 1

2 −1

−1 2

Parte Negativa Parte Positiva

𝐷𝑥 = [𝟎. (−𝟏). 𝟏 + 𝟏. 𝒓. (−𝟏) + 𝟏. 𝟐. 𝟐] − [𝟏. (−𝟏). (−𝟏) + 𝟎. 𝒓. 𝟐 + 𝟏. 𝟐. 𝟏]

Logo:

𝐷𝑥 = [−𝑟 + 4] − [3]

𝐷𝑥 = 1 − 𝑟 𝑥 =
𝐷𝑥

𝐷

1 − 𝑟

=

𝑟(𝑟 − 1)

−(𝑟 − 1)

=

𝑟(𝑟 − 1)

Simplificando (𝑟 − 1), obtemos:

Gabarito: Letra D.

Método do escalonamento

−1

𝑥 =

𝑟

O método do escalonamento, também conhecido por Eliminação Gaussiana, sem dúvidas é o melhor meio para se resolver sistemas lineares.
Esse método nos traz um passo a passo, uma "receita de bolo". Não é necessário ter uma "sacada" para resolver o sistema. Além disso, não precisamos resolver determinantes, como acontece no Teorema deCramer.

O método consiste em obter um sistema equivalente ao sistema original em que o número de variáveis explícitas diminui de equação para equação. Em outras palavras, o número de coeficientes nulos aumenta de equação para equação.
Considere o seguinte sistema:

2𝑥 + 𝑦 + 𝑧 = 4

{2𝑥 + 4𝑦 + 4𝑧 = 22
2𝑥 + 4𝑦 + 3𝑧 = 10

A ideia do método do escalonamento é chegar no seguinte sistema equivalente:

2𝑥 + 𝑦 + 𝑧 = 4

{ 3𝑦 + 3𝑧 = 18

−𝑧 = −12

Dizemos que este sistema é um sistema escalonado porque o número de variáveis explícitas diminui de equação para equação. Note que na primeira equação temos 3 variáveis explícitas, na segunda equação temos 2 variáveis e, na última equação, temos apenas uma variável explícita.
Veja como o sistema escalonado é interessante: a partir da última equação, obtemos o valor de 𝒛. Na penúltima equação conseguimos obter o valor de 𝒚, pois já temos o valor de 𝑧. Por fim, na primeira equação,conseguimos obter o valor de 𝒙, pois já temos 𝑦 e 𝑧.

Ok, professor. Mas como obtenho esse sistema escalonado?

Para obter o sistema escalonado, devemos seguir os seguintes passos:

* Colocar como 1ª equação uma que apresente a 1ª incógnita;

* Anular a 1ª incógnita de todas as equações (exceto da 1ª) fazendo uso da 1ª equação;

* Anular a 2ª incógnita de todas as equações (exceto da 1ª e da 2ª) fazendo uso da 2ª equação;
* Anular a 3ª incógnita de todas as equações (exceto da 1ª, da 2ª e da 3ª) fazendo uso da 3ª equação;
* E assim sucessivamente, até que tenhamos usado todas as equações.

Vamos aprender na prática.

𝟐𝒙 + 𝒚 + 𝒛 = 𝟒

Encontre a solução do seguinte sistema linear {𝟐𝒙 + 𝟒𝒚 + 𝟒𝒛 = 𝟐𝟐 pelo método do escalonamento.
𝟐𝒙 + 𝟒𝒚 + 𝟑𝒛 = 𝟏𝟎

* Note que a 1ª equação já apresenta a 1ª incógnita (𝒙).

* Devemos, agora, eliminar a 1ª incógnita (𝒙) de todas as equações (exceto da 1ª)
fazendo uso da 1ª equação.
Temos o seguinte sistema linear:

2𝑥 + 𝑦 + 𝑧 = 4

{2𝑥 + 4𝑦 + 4𝑧 = 22
2𝑥 + 4𝑦 + 3𝑧 = 10

Fazendo L₂ ← 𝟏L₂ + (−𝟏)L₁, obtemos um sistema linear equivalente:

2𝑥 + 𝑦 + 𝑧 = 4

~ { 3𝑦 + 3𝑧 = 18
2𝑥 + 4𝑦 + 3𝑧 = 10

Fazendo L₃ ← 𝟏L₃ + (−𝟏)L₁, obtemos um sistema linear equivalente:

2𝑥 + 𝑦 + 𝑧 = 4

~ { 3𝑦 + 3𝑧 = 18
3𝑦 + 2𝑧 = 6

* Devemos, agora, eliminar a 2ª incógnita (𝒚) de todas as equações (exceto da 1ª e da 2ª) fazendo uso da2ª equação.

Fazendo L₃ ← 𝟏L₃ + (−𝟏)L₂, obtemos um sistema linear equivalente:

2𝑥 + 𝑦 + 𝑧 = 4

~ { 3𝑦 + 3𝑧 = 18

− 1𝑧 = −12

Observe que obtemos um sistema escalonado. Nesse momento, devemos parar o escalonamento e obter a solução a partir da última equação.
Da segunda equação, temos:

−1𝑧 = −12

𝒛 = 𝟏𝟐

3𝑦 + 3𝒛 = 18

3𝑦 + 3. 𝟏𝟐 = 18

3𝑦 = −18

𝒚 = −𝟔

Da primeira equação, temos:

2𝑥 + 𝒚 + 𝒛 = 4

2𝑥 + (−𝟔) + 𝟏𝟐 = 4

2𝑥 + 6 = 4

2𝑥 = −2

𝒙 = −𝟏

Portanto, a solução do sistema linear é (𝒙, 𝒚, 𝒛) = (−𝟏, −𝟔, 𝟏𝟐).

Observe que, no problema anterior, obtivemos a seguinte sequência de sistemas equivalentes:

𝟐𝒙 + 𝒚 + 𝒛 = 𝟒

{𝟐𝒙 + 𝟒𝒚 + 𝟒𝒛 = 𝟐𝟐 L2←𝟏L2+(−𝟏)L1 {

𝟐𝒙 + 𝟒𝒚 + 𝟑𝒛 = 𝟏𝟎

2𝑥 + 𝑦 + 𝑧 = 4

L3←𝟏L3+(−𝟏)L1

3𝑦 + 3𝑧 = 18 ~ {

2𝑥 + 4𝑦 + 3𝑧 = 10

2𝑥 + 𝑦 + 𝑧 = 4

3𝑦 + 3𝑧 = 18

3𝑦 + 2𝑧 = 6

L3←𝟏L3+(−𝟏)L2

~ {

2𝑥 + 𝑦 + 𝑧 = 4

3𝑦 + 3𝑧 = 18

− 1𝑧 = −12

Uma outra forma de escalonar o sistema é utilizando a matriz completa do sistema [𝐴|𝐵].

𝟐 𝟏 𝟏 𝟒

L2←𝟏L2+(−𝟏)L1

2 1 1 4

L3←𝟏L3+(−𝟏)L1

2 1 1 4

[𝟐 𝟒 𝟒 𝟐𝟐] ~

𝟐 𝟒 𝟑 𝟏𝟎

[0 3 3 18] ~

2 4 3 10

[0 3 3 18]

0 3 2 6

L3←𝟏L3+(−𝟏)L2

~

2 1 1 4

[0 3 3 18 ]

0 0 −1 −12

Dê preferência ao escalonamento por meio da matriz completa do sistema. Isso porque ela traz maior agilidade no escalonamento, pois não é necessário escrever diversas vezes as incógnitas 𝑥, 𝑦 e 𝑧.
Para evitar trabalhar com frações na hora de escalonar um sistema, um recurso interessante é alterar a ordem das equações. Veremos isso na resolução do primeiro exercício a seguir.
(Pref. Rezende/2019) O valor de 𝑥 no sistema linear a seguir é:

2𝑥 + 𝑦 + 3𝑧 = 19

{ 𝑥 + 2𝑦 + 𝑧 = 12
3𝑥 − 𝑦 + 𝑧 = 7

a) 1

b) 2

c) 3

d) 4

Comentários:

Vamos resolver essa questão pelo método do escalonamento, fazendo uso da matriz completa do sistema.
Inicialmente, temos:

2𝑥 + 𝑦 + 3𝑧 = 19

{ 𝑥 + 2𝑦 + 𝑧 = 12
3𝑥 − 𝑦 + 𝑧 = 7

Note que, para iniciar o escalonamento, teríamos que fazer L₂ ← 𝟏L₂ + (−

) L para eliminar a incógnita 𝑥 da segunda equação. Para evitar trabalhar com números fracionários, vamos trocar a primeira e a segunda equação de lugar:
𝑥 + 2𝑦 + 𝑧 = 12

{2𝑥 + 𝑦 + 3𝑧 = 19
3𝑥 − 𝑦 + 𝑧 = 7

A matriz completa do sistema é:

1 2 1 12

[2 1 3 19]

3 −1 1 7

* Note que a 1ª equação já apresenta a 1ª incógnita (𝒙).

* Devemos, agora, eliminar a 1ª incógnita (𝒙) de todas as equações (exceto da 1ª)
fazendo uso da 1ª equação.
Fazendo L₂ ← 𝟏L₂ + (−𝟐)L₁, obtemos um sistema linear equivalente:

1 2 1 12

~ [0 −3 1 −5]

3 −1 1 7

Fazendo L₃ ← 𝟏L₃ + (−𝟑)L₁, obtemos um sistema linear equivalente:

1 2 1 12

~ [0 −3 1 −5 ]

0 −7 −2 −29

* Devemos, agora, eliminar a 2ª incógnita (𝒚) de todas as equações (exceto da 1ª e da 2ª) fazendo uso da2ª equação.

Fazendo L₃ ← 𝟏L₃ + (−

) L , obtemos um sistema linear equivalente:

1 2 1 12

0 −3 1 −5

~ [ 13

0 0 −

52]

−

Note, portanto, que obtivemos o seguinte sistema equivalente:

𝑥 + 2𝑦 + 𝑧 = 12

{ − 3𝑦 + 𝑧 = −5

Da última equação, temos:

13 52

− 𝑧 = −

3 3

13 52

− 𝑧 = −

3 3

13𝑧 = 52

𝒛 = 𝟒

05152001900 - Everton Murilo Vieira

Da segunda equação, temos:

−3𝑦 + 𝑧 = −5

−3𝑦 + 4 = −5

−3𝑦 = −9

𝒚 = 𝟑

Da primeira equação, temos:

Portanto, o valor de 𝑥 é 2.

Gabarito: Letra B.

𝑥 + 2𝑦 + 𝑧 = 12

𝑥 + 2.3 + 4 = 12

𝑥 = 12 − 4 − 6

𝒙 = 𝟐

(Pref. Caxias do Sul/2019) Dado o sistema de equações lineares abaixo:

2𝑥₁ + 2𝑥₂ + 𝑥₃ = 8

𝑌 = { 3𝑥₁ + 2𝑥₂ + 𝑥₃ = 10
2𝑥₁ + 2𝑥₂ + 2𝑥₃ = 16

O conjunto solução S com base na ordem de 𝑆 = (𝑥₂, 𝑥₁, 𝑥₃) é:

a) 𝑆 = (𝑥₂, 𝑥₁, 𝑥₃) = (2, −2, 8).

b) 𝑆 = (𝑥₂, 𝑥₁, 𝑥₃) = (−2, 2, 8).

c) 𝑆 = (𝑥₂, 𝑥₁, 𝑥₃) = (8, −2, 2).

d) 𝑆 = (𝑥₂, 𝑥₁, 𝑥₃) = (2, 8, 2).

e) 𝑆 = (𝑥₂, 𝑥₁, 𝑥₃) = (2, 2, 8).

Comentários:

Vamos resolver essa questão pelo método do escalonamento, fazendo uso da matriz completa do sistema.
2 2 1 8

L2←𝟏L2+(− )L1

2 2 1 8

L ←𝟏L +(−𝟏)L

2 2 1 8

𝟐 2 2

[3 2 1 10] ~

2 2 2 16

[0 −1 −1/2 −2] ~

2 2 2 16

[0 −1 −1/2 −2]

0 0 1 8

Veja que a última operação já eliminou a variável 𝑥₁ e 𝑥₂ da terceira equação.
Ficamos com o seguinte sistema escalonado:

05152001900 - Everton Murilo Vieira

Aula 18

Da última equação, temos:
Da segunda equação, temos:

Da primeira equação, temos

2𝑥₁ + 2𝑥₂ + 𝑥₃ = 8

{ − 1𝑥₂ − 2 𝑥₃ = −2

1𝑥₃ = 8

𝒙𝟑 = 𝟖

−1𝑥₂ − 2 𝒙𝟑 = −2

−𝑥₂ − 2 . 8 = −2

−𝑥₂ − 4 = −2

−𝑥₂ = 4 − 2

−𝑥₂ = 2

𝒙𝟐 = −𝟐

2𝑥₁ + 2𝒙𝟐 + 𝒙𝟑 = 8

2𝑥₁ + 2. (−2) + 8 = 8

2𝑥₁ = 4

𝒙𝟏 = 𝟐

Muita atenção nesse momento. A questão pergunta pela solução 𝑆 = (𝒙𝟐, 𝒙𝟏, 𝑥₃).
O gabarito, portanto, é letra B: 𝑆 = (𝒙𝟐, 𝒙𝟏, 𝑥₃) = (−𝟐, 𝟐, 8).

Gabarito: Letra B.

Posto e nulidade de uma matriz

O posto de uma matriz é o número de linhas não nulas de uma matriz escalonada. A representação do posto de uma matriz 𝐴 é dada por 𝜌(𝐴).
A nulidade de uma matriz é dada pela diferença entre o número de colunas e o posto da matriz:

𝑛𝑢𝑙𝑙(𝐴) = (Nº colunas) − 𝜌(𝐴)

Exemplo: se, ao escalonarmos uma matriz 𝐴, obtivermos o seguinte resultado:

𝟏 𝟒 𝟐 𝟏 𝟑
F𝟎 𝟏 𝟑 𝟐 𝟒1

𝟎 𝟎 𝟏 𝟏 𝟐
I𝟎 𝟎 𝟎 𝟎 𝟎I
[𝟎 𝟎 𝟎 𝟎 𝟎]

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Aula 18

Temos que:

* O posto dessa matriz é 𝝆(𝑨) = 𝟑.

* A nulidade dessa matriz é 𝑛𝑢𝑙𝑙 (𝐴) = 5 − 3 = 2.

O posto da matriz também é conhecido por característica da matriz.

(ABIN/2010) Considerando a matriz

E os vetores:

Julgue o item a seguir.
A matriz 𝐴 tem posto 2.
Comentários:

Vamos escalonar a matriz 𝐴, dada por:

Fazendo L₂ ← 𝟏L₂ + (−𝟐)L₁, obtemos:

Fazendo L₃ ← 𝟏L₃ + (−𝟑)L₁, obtemos:

1 2 2

𝐴 = (2 0 2)

3 4 5

𝑥₁

𝑥 = (𝑥2)

𝑥₃

𝑏₁

𝑏 = (𝑏₂)

𝑏₃

1 2 2

(2 0 2)

3 4 5

1 2 2

(0 −4 −2)

3 4 5

1 2 2

(0 −4 −2)

0 −2 −1

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Aula 18

Fazendo L₃ ← 𝟏L₃ + (−

) L , obtemos:

𝟏 𝟐 𝟐
(𝟎 −𝟒 −𝟐)

𝟎 𝟎 𝟎

O posto de uma matriz é o número de linhas não nulas de uma matriz escalonada. Logo, o posto de 𝐴
é 2.

Gabarito: CERTO.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Aula 18

Discussão de um sistema linear

Vimos que um sistema linear pode ser classificado de três formas:

* Sistema Possível e Determinado (SPD): o sistema apresenta uma única solução;

* Sistema Possível e Indeterminado (SPI): o sistema apresenta infinitas soluções; e

* Sistema Impossível (SI): ocorre quando o sistema não apresenta solução.

A discussão de um sistema linear trata justamente dessa classificação, de modo a determinar se o sistema linear é SPD, SPI ou SI.
Discussão por Teorema de Cramer

Vimos que é possível obter a solução de um sistema linear por meio do Teorema de Cramer:

𝑥 =

𝐷𝑥

𝑫

; 𝑦 =

𝐷𝑦

𝑫

; 𝑧 =

𝐷𝑧

𝑫

Lembre-se de que a condição para aplicar o teorema é 𝑫 ≠ 𝟎, isto é, o determinante da matriz dos coeficientes (matriz incompleta do sistema) deve ser diferente de zero. Nesse caso, o sistema é possível e determinado (SPD), apresentando solução única.
Por outro lado, quando 𝑫 = 𝟎, podemos ter um sistema possível indeterminado (SPI) ou um sistema impossível (SI).
Teorema de Cramer

D ≠ 0 D = 0

Sistema Possível e
Determinado (SPD)

Sistema Possível e
Indeterminado (SPI)

Sistema Impossível (SI)

Um caso interessante ocorre quando temos um sistema linear homogêneo. Lembre-se de que esse sistema sempre admite solução, a solução trivial. Nesse caso, esse sistema não pode ser impossível, de modo que,se 𝐷 = 0, necessariamente ele é possível e indeterminado (SPI).

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Aula 18

Sistema Linear Homogêneo

D ≠ 0 D = 0

Sistema Possível e Determinado (SPD) Sistema Possível e Indeterminado (SPI)

Admite somente a solução trivial Admite a solução trivial e infinitas outras

Professor, quando 𝐷 = 0 e o sistema não é homogêneo, como vou diferenciar o SPI do SI?

Excelente pergunta! Nesse caso, o Teorema de Cramer nos deixa na mão. Devemos utilizar o Método do
Escalonamento, que será visto no próximo tópico.

Para fins de discussão do sistema linear, o Teorema de Cramer tem serventia quando obtemos 𝑫 ≠ 𝟎 ou quando o sistema é homogêneo.
No caso em que 𝑫 = 𝟎 e o sistema não é homogêneo, ficamos na dúvida entre SPI e SI.
Para sanar essa questão, deve-se utilizar o Método do Escalonamento.

(Pref. SJC/2019) Considere o sistema linear S, representado da seguinte forma matricial:

𝑎 𝑏 𝑥 0

O sistema S é:

a) impossível se 𝑎𝑑 − 𝑏𝑐 = 0

b) impossível se 𝑎𝑑 − 𝑏𝑐 ≠ 0

𝑆 = (

𝑐 𝑑

) . (𝑦) = ( )

c) possível e determinado se 𝑎𝑑 − 𝑏𝑐 = 0

d) possível e determinado se 𝑎𝑑 − 𝑏𝑐 ≠ 0

e) possível e indeterminado se 𝑎𝑑 − 𝑏𝑐 ≠ 0

Comentários:

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

Observe que o sistema linear em questão é homogêneo, pois os termos independentes são nulos.
Nesse caso, sendo 𝐷 o determinante da matriz dos coeficientes:

* Se 𝐷 ≠ 0, temos um sistema possível e determinado (SPD);

* Se 𝐷 = 0, temos um sistema possível e indeterminado (SPI).

O determinante da matriz dos coeficientes é:

𝑎 𝑏

Logo:

𝐷 = |𝑐 𝑑| = 𝑎𝑑 − 𝑏𝑐

* Se 𝑎𝑑 − 𝑏𝑐 ≠ 0, temos um sistema possível e determinado (SPD);

* Se 𝑎𝑑 − 𝑏𝑐 = 0, temos um sistema possível e indeterminado (SPI).

==2d4a97==

O gabarito, portanto, é letra D.
Gabarito: Letra D.

(TRANSPETRO/2018) Sistemas lineares homogêneos possuem, pelo menos, uma solução e, portanto, nunca serão considerados impossíveis. O sistema linear dado abaixo possui infinitas soluções.
𝑥 + 𝑦 + 𝑧 = 0

{ 𝑥 + 𝛼𝑦 + 𝑧 = 0

𝛼𝑥 + 𝛼𝑦 + 2𝑧 = 0

Qual o maior valor possível para 𝛼?

a) 0

b) 1

c) 2

d) 3

e) 4

Comentários:

Temos um sistema linear homogêneo com infinitas soluções. Logo, além de homogêneo, o sistema é possível e indeterminado (SPI).
1 1 1

Portanto, devemos ter 𝐷 = 0, ou seja, |1 𝛼 1| = 0.

𝛼 𝛼 2

Aplicando a Regra de Sarrus no determinante 𝐷, temos:

1 1 1 1 1

|1 𝛼 1| 1 𝛼 𝛼 𝛼 2 𝛼 𝛼
Parte Negativa Parte Positiva

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

𝐷 = [𝟏. 𝜶. 𝟐 + 𝟏. 𝟏. 𝜶 + 𝟏. 𝟏. 𝜶] − [𝟏. 𝜶. 𝜶 + 𝟏. 𝟏. 𝜶 + 𝟏. 𝟏. 𝟐]

𝐷 = [4𝛼] − [𝛼² + 𝛼 + 2]

𝐷 = −𝛼² + 3𝛼 − 2

Como 𝐷 = 0, temos:

−𝛼² + 3𝛼 − 2 = 0

𝛼² − 3𝛼 + 2 = 0

Aplicando a Fórmula de Bhaskara:

∆= 𝑏² − 4𝑎𝑐

∆= (−3)² − 4.1.2

∆ = 1

𝛼 =

−𝑏 ± √∆
2𝑎 𝛼 =
−(−3) ± √1

2.1

3 ± 1

𝛼 =

𝜶𝟏 = 𝟐 ; 𝜶𝟐 = 𝟏

Logo, o maior valor possível para 𝜶 é 2.
Gabarito: Letra C.

Antes de passar para o próximo tópico, é necessário esclarecer um ponto para aqueles que estudaram essa matéria em outras fontes.
Alguns professores, especialmente relacionados a concursos públicos, ensinam de modo equivocado (ERRADO) que se pode usar Teorema de Cramer para diferenciar um SPI de um SI. Eles dizem que, uma vez que 𝐷 = 0, o SPI ocorre quando:
𝐷 = 𝐷𝑥 = 𝐷𝑦 = 𝐷𝑧 = ⋯ = 0

O contraexemplo a seguir mostra que esse bizu está errado:

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

1𝑥 + 1𝑦 + 1𝑧 = 1

{2𝑥 + 2𝑦 + 2𝑧 = 2
3𝑥 + 3𝑦 + 3𝑧 = 𝟕

Note que o sistema apresentado é impossível (SI). Isso porque, ao multiplicar a primeira equação por 3, obtém-se:
3𝑥 + 3𝑦 + 3𝑧 = 𝟑

Essa equação contradiz a última equação do sistema, pois 3𝑥 + 3𝑦 + 3𝑧 não pode ser igual a 𝟑 e a 𝟕 ao mesmo tempo.
Observe, porém, que todos os determinantes são zero, pois apresentam filas paralelas iguais:
1 1 1

𝟏 1 1

1 𝟏 1

1 1 𝟏

𝐷 = |2 2 2| 𝐷𝑥 = |𝟐 2 2| 𝐷𝑦 = |2 𝟐 2| 𝐷𝑧 = |2 2
𝟐|

3 3 3

𝟕 3 3

3 𝟕 3

3 3 𝟕

Segundo o bizu errado, teríamos um SPI, pois 𝐷 = 𝐷𝑥 = 𝐷𝑦 = 𝐷𝑧 = 0.

Discussão pelo Método do Escalonamento

Podemos classificar um sistema linear em SPD, SPI e SI de maneira inequívoca por meio do escalonamento.Para tanto, deve-se seguir os seguintes passos:

Passo 1: Escalonar o sistema linear.

Passo 2: Analisar o sistema linear escalonado.

* Se obtivermos uma equação da forma 𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 + 𝟎𝒘 = 𝒃, com 𝒃 ≠
𝟎, temos um sistema impossível (SI);
* Caso contrário, temos duas possibilidades:

o Se o número de equações for igual ao número de incógnitas, temos um sistema possível e determinado (SPD).
o Se o número de equações for menor do que o número de incógnitas, temos um sistema possível e indeterminado (SPI).
SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

No escalonamento, se obtivermos uma equação da forma 𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 + 𝟎𝒘 = 𝟎,
devemos eliminar essa equação do sistema linear, pois essa equação é uma combinação linear das outras.
Vamos realizar três exemplos para que não reste dúvida quanto ao método.

𝒙 + 𝟐𝒚 + 𝒛 = 𝟐

Classifique o sistema linear { 𝟐𝒙 + 𝟑𝒚 + 𝒛 = 𝟑 .

𝟒𝒙 + 𝟕𝒚 + 𝟑𝒛 = 𝟖

Vamos escalonar o sistema fazendo uso da matriz completa do sistema.

1 2 1 2

L2←𝟏L2+(−𝟐)L1

1 2 1 2

L3←𝟏L3+(−𝟒)L1

1 2 1 2

[2 3 1 3] ~

4 7 3 8

[0 −1 −1 −1] ~

4 7 3 8

[0 −1 −1 −1]

0 −1 −1 0

L3←𝟏L3+(−𝟏)L2

~

1 2 1 2

[0 −1 −1 −1]

𝟎 𝟎 𝟎 𝟏

A última equação do sistema escalonado, dada por 𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 = 𝟏, indica que estamos diante de um sistema impossível (SI).
𝒙 + 𝟐𝒚 + 𝒛 = 𝟏

Classifique o sistema linear { 𝒙 + 𝟑𝒚 + 𝟐𝒛 = 𝟐 .

𝟒𝒙 + 𝟗𝒚 + 𝟓𝒛 = 𝟓

Vamos escalonar o sistema fazendo uso da matriz completa do sistema.

1 2 1 1

L2←𝟏L2+(−𝟏)L1

1 2 1 1

L3←𝟏L3+(−𝟒)L1

1 2 1 1

[1 3 2 2] ~

4 9 5 5

[0 1 1 1] ~

4 9 5 5

[0 1 1 1]

0 1 1 1

L3←𝟏L3+(−𝟏)L2

~

1 2 1 1

[0 1 1 1]

𝟎 𝟎 𝟎 𝟎

A última equação do sistema escalonado, dada por 𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 = 𝟎, deve ser eliminada. O
sistema linear em questão é equivalente a:
SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

1 2 1 1

1 2 1 1

[0 1 1 1] ~ [ ]

𝟎 𝟎 𝟎 𝟎

0 1 1 1

Explicitando as variáveis, o sistema linear original equivale a:

{𝑥 + 2𝑦 + 𝑧 = 1

𝑦 + 𝑧 = 1

Veja que o sistema anterior é escalonado, pois o número de incógnitas diminui de equação para equação.
Trata-se de um sistema escalonado cujo número de equações (2) é menor do que o número de incógnitas

(3). Logo, temos um sistema possível e indeterminado (SPI).

𝒙 − 𝒚 + 𝒛 = 𝟏

Classifique o sistema linear { 𝒙 + 𝟑𝒚 + 𝟐𝒛 = 𝟐 .

𝟐𝒙 + 𝟑𝒚 + 𝟏𝒛 = 𝟑

Vamos escalonar o sistema fazendo uso da matriz completa do sistema.

1 −1 1 1

L2←𝟏L2+(−𝟏)L1

1 −1 1 1

L3←𝟏L3+(−𝟐)L1

1 −1 1 1

[1 3 2 2] ~

2 3 1 3

[0 4 1 1] ~

2 3 1 3

[0 4 1 1]

0 5 −1 1

L ←𝟏L +(−𝟓 L

~

1 −1 1 1

𝟎 4 1 1

[ 1 1]

𝟎 𝟎 − −

4 4

Explicitando as variáveis, o sistema linear original equivale a:

𝑥 − 𝑦 + 𝑧 = 1

4𝑦 + 𝑧 = 1

{ 1 1

− 𝑧 = −

4 4

Veja que o sistema acima é escalonado, pois o número de incógnitas diminui de equação para equação.

Trata-se de um sistema escalonado cujo número de equações (3) é igual ao número de incógnitas (3).
Logo, temos um sistema possível e determinado (SPD).

Vamos praticar o que aprendemos nessa seção.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

(STN/2013) Dado o sistema de equações lineares

{2𝑥 + 4𝑦 = 6
3𝑥 + 6𝑦 = 9

É correto afirmar que:

a) o sistema não possui solução.

b) o sistema possui uma única solução.

c) 𝑥 = 1 e 𝑦 = 2 é uma solução do sistema.

d) o sistema é homogêneo.

e) o sistema possui mais de uma solução.

Comentários:

Vamos escalonar o sistema fazendo uso da matriz completa do sistema. Temos:

[2 4 6

Realizando L₂ = 𝟏L₂ + (−

3 6 ]

) L , ficamos com:

~ [2 4 6]

𝟎 𝟎 𝟎

A última equação do sistema escalonado, dada por 𝟎𝒙 + 𝟎𝒚 = 𝟎, pode ser eliminada. O sistema linear em questão é equivalente a:
~[2 4 6]

Explicitando as variáveis, o sistema linear original equivale a:

{𝑥 + 2𝑦 = 6

Trata-se de um sistema escalonado cujo número de equações (1) é menor do que o número de incógnitas
(2). Logo, temos um sistema possível e indeterminado (SPI). Isso significa que o sistema possui mais de uma solução, isto é, possui infinitas soluções. O gabarito, portanto, é letra E.
Gabarito: Letra E.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

(CGU/2008) Considerando o sistema de equações lineares

{ 𝑥₁ − 𝑥₂ = 2
2𝑥₁ + 𝑝𝑥₂ = 𝑞 pode-se corretamente afirmar que a) se 𝑝 = −2 e 𝑞 ≠ 4, então o sistema é impossível.
b) se 𝑝 ≠ −2 e 𝑞 = 4, então o sistema é possível e indeterminado.

c) se 𝑝 = −2, então o sistema é possível e determinado.

d) se 𝑝 = −2 e 𝑞 ≠ 4, então o sistema é possível e indeterminado.

e) se 𝑝 = 2 e 𝑞 = 4, então o sistema é impossível.

Comentários:

Essa questão é um excelente resumo do que vimos quanto à discussão de um sistema linear.
Inicialmente, vamos utilizar o Teorema de Cramer.

O determinante 𝐷 da matriz dos coeficientes é:

1 −1

𝐷 = | |

2 𝑝

𝐷 = [1 × 𝑝] − [(−1) × 2]

𝐷 = 𝑝 − (−2)

𝑫 = 𝒑 + 𝟐

Pelo Teorema de Cramer, sabemos que o sistema é possível e determinado (SPD) quando 𝑫 ≠ 𝟎, isto é,
quando:

𝑝 + 2 ≠ 0

𝒑 ≠ −𝟐

Para o caso em que 𝑫 = 𝟎, isto é, quando 𝒑 = −𝟐, podemos ter tanto um sistema possível e indeterminado
(SPI) quanto um sistema impossível (SI).

Para saber o que acontece para o caso em que 𝒑 = −𝟐, devemos escalonar o sistema. Temos:

{ 𝑥₁ − 𝑥₂ = 2
2𝑥₁ − 𝟐𝑥₂ = 𝑞

Na forma matricial:

[1 −1 2]

2 −2 𝑞

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

Realizando L₂ = 𝟏L₂ + (−𝟐)L₁, temos:

~ [1 −1 2 ]

0 0 𝑞 − 4

Note que:

* Se (𝑞 − 4) for diferente de zero, isto é, se 𝒒 ≠ 𝟒, teremos um sistema impossível (SI), pois haverá uma equação da forma 𝟎𝒙𝟏 + 𝟎𝒙𝟐 = (𝒒 − 𝟒) com (𝒒 − 𝟒) ≠ 𝟎.
* Por outro lado, se 𝒒 = 𝟒, ficamos com:

~ [1 −1 2]

𝟎 𝟎 𝟎

A última equação do sistema escalonado, dada por 𝟎𝒙𝟏 + 𝟎𝒙𝟐 = 𝟎, pode ser eliminada. O
sistema linear em questão é equivalente a:
~[1 −1 2]

Explicitando as variáveis, o sistema linear original equivale a:

{𝑥₁ − 𝑥₂ = 2

Trata-se de um sistema escalonado cujo número de equações (1) é menor do que o número de incógnitas

(2). Logo, temos um sistema possível e indeterminado (SPI).

Em resumo, temos o seguinte:

* 𝑝 ≠ −2 → Sistema Possível e Determinado (SPD);

* 𝑝 = −2 e 𝑞 ≠ 4 → Sistema Impossível (SI);

* 𝑝 = −2 e 𝑞 = 4 → Sistema Possível e Indeterminado (SPI).

O gabarito, portanto, é letra A.
Gabarito: Letra A.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

QUESTÕES COMENTADAS - CEBRASPE

Solução de um sistema linear

(CESPE/IFF/2018) Considere que 𝑨 = (𝒂𝒊𝒋) seja uma matriz quadrada de dimensão 𝒏 × 𝒏 e de entradas reais; que 𝑩 = (𝒃𝒊) seja uma matriz coluna, de dimensão 𝒏 × 𝟏 e de entradas reais, e que 𝑿= (𝒙𝒊) seja a matriz das incógnitas, uma matriz coluna de dimensão 𝒏 × 𝟏. Nesse caso, para se resolver o sistema matricial 𝑨𝑿 = 𝑩, o método indicado é o denominado a) método de diferenças finitas.
b) método de quadratura de Gauss.

c) método de Simpson.

d) método de elementos de contorno.

e) método de eliminação de Gauss.

Comentários:

Para resolver um sistema linear, pode-se utilizar o método do escalonamento, também conhecido por
Eliminação Gaussiana ou método de eliminação de Gauss.
Gabarito: Letra E.

Texto para as próximas questões 𝑥 − 𝑦 − 𝑧 = 0
Considerando o sistema linear {

2𝑥 + 3𝑦 + 2𝑧 = 2

−𝑥 + 2𝑦 − 2𝑧 = −11

, julgue os itens que se segue.

(CESPE/SGA AC/2008) 𝒚 > 𝒙.

(CESPE/SGA AC/2008) Todas as soluções do sistema são números naturais.
(CESPE/SGA AC/2008) 𝒛 = 𝒙 + |𝒚|

Comentários:

Antes de resolver os itens da questão, vamos escalonar a matriz completa do sistema e obter a solução.
1 −1 −1 0

[ 2 3 2 2

L2←𝟏L2+(−𝟐)L1

] ~

1 −1 −1 0

[ 0 5 4 2

L3←𝟏L3+𝟏L1

] ~

1 −1 −1 0

[0 5 4 2 ]

−1 2 −2 −11

−1 2 −2 −11

0 1 −3 −11

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

L3←𝟏L3+(− )L1

1 −1 −1 0

~ 𝟓 0 5 4 2

[ 19

0 0 −

57]

−

Logo, temos o seguinte sistema linear equivalente:

𝑥 − 𝑦 − 𝑧 = 0

5𝑦 + 4𝑧 = 2

{ 19 57

− 𝑧 = −

5 5

Da terceira equação, temos:

19 57

− ==2d4a97== 𝑧 = −

5 5

𝑧 =

𝒛 = 𝟑

Da segunda equação, temos:

5𝑦 + 4𝒛 = 2

5𝑦 + 4 × 3 = 2

5𝑦 = 2 − 12

5𝑦 = −10

𝒚 = −𝟐

Da primeira equação, temos:

𝑥 − 𝒚 − 𝒛 = 0

𝑥 = 𝑦 + 𝑧 𝑥 = −2 + 3
𝒙 = 𝟏

Portanto, a solução do sistema é (𝑥, 𝑦, 𝑧) = (1, −2, 3). Vamos analisar os itens.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

Questão 02

Item ERRADO. 𝑦 > 𝑥 é uma afirmação falsa, pois, −𝟐 não é maior do que 1.

Questão 03

Item ERRADO. 𝑦 não é um número natural, pois 𝑦 = −2.

Questão 04

Item CERTO. Temos que a expressão é uma igualdade verdadeira, pois 𝑧 = 3 e 𝑥 + |𝑦| também é igual a 3.
𝑧 = 𝑥 + |𝑦|
3 = 1 + |−2|

3 = 1 + 2

3 = 3

Gabarito: 02 - ERRADO. 03 - ERRADO. 04 - CERTO.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

QUESTÕES COMENTADAS - CEBRASPE

Discussão de um sistema linear

(CESPE/Pref. São Cristóvão/2019) Com relação a sistemas lineares e análise combinatória, julgue o item.
Para todo sistema linear da forma 𝑨𝑿 = 𝑩, em que 𝑨 é uma matriz quadrada 𝒎 × 𝒎, 𝑿 e 𝑩 são matrizes colunas 𝒎 × 𝟏, e 𝒅𝒆𝒕(𝑨) = 𝟎, o sistema não tem solução.
Comentários:

Temos um sistema linear na forma matricial 𝑨𝒎×𝒎𝑿𝒎×𝟏 = 𝑩𝒎×𝟏, sendo:

* 𝑨: Matriz dos coeficientes ou matriz incompleta do sistema;

* 𝑿: Matriz das incógnitas;

* 𝑩: Matriz dos termos independentes.

Segundo o Teorema de Cramer, quando 𝐷 = 0, isto é, quando 𝐝𝐞𝐭 𝑨 = 𝟎, podemos ter:

* Sistema Possível e Indeterminado (SPI): apresenta infinitas soluções;

* Sistema Impossível (SI): não apresenta solução.

Portanto, não se pode afirmar que o sistema não tem solução, pois ele pode ser SPI e,
consequentemente,

pode apresentar infinitas soluções.
Gabarito: ERRADO.

𝒂 − 𝟏 𝒂 − 𝟏 𝒂 − 𝟏

(CESPE/SEDUC CE/2009/Adaptada) Acerca da matriz 𝑨 = [𝒂 − 𝟏 𝟏 𝟐

𝒂 − 𝟏 𝟏 −𝟐

], em que 𝒂 é um número real, julgue o item a seguir.
𝒙 𝟎

Se 𝒂 ≠ 𝟏, então a equação matricial 𝑨𝑿 = 𝑶, em que 𝑿 = [𝒚] e 𝑶 = [𝟎] é a matriz nula de ordem 𝟑 × 𝟏,
𝒛 𝟎

tem uma única solução.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

Comentários:

Observe que a equação matricial 𝐴𝑋 = 𝑶 representa um sistema linear homogêneo, pois se trata de um sistema linear em que todos os termos independentes são nulos.
Pelo Teorema de Cramer, sabemos que se 𝐷 ≠ 0, isto é, se 𝐝𝐞𝐭 𝑨 ≠ 𝟎, o sistema linear homogêneo apresenta solução única, a solução trivial.
Aplicando a Regra de Sarrus no determinante da matriz 𝐴, temos:

𝑎 − 1 𝑎 − 1 𝑎 − 1

|𝑎 − 1 1 2

𝑎 − 1 1 −2

𝑎 − 1 𝑎 − 1

| 𝑎 − 1 1

𝑎 − 1 1

Parte Negativa Parte Positiva det 𝐴 = [(−𝟐). (𝒂 − 𝟏) + 𝟐(𝒂 − 𝟏)𝟐 + (𝒂 − 𝟏)𝟐] − [(𝒂 − 𝟏)𝟐 + 𝟐(𝒂 − 𝟏) + (−𝟐). (𝒂− 𝟏)𝟐]
det 𝐴 = [3(𝑎 − 1)² − 2(𝑎 − 1)] − [−(𝑎 − 1)² + 2(𝑎 − 1)]

det 𝐴 = 4(𝑎 − 1)² − 4(𝑎 − 1)

Para termos solução única, devemos ter 𝐝𝐞𝐭 𝑨 ≠ 𝟎.

4(𝑎 − 1)² − 4(𝑎 − 1) ≠ 0

4(𝑎 − 1)² ≠ 4(𝑎 − 1)
(𝑎 − 1)² ≠ (𝑎 − 1)

A igualdade ocorre com 𝑎 = 1. Portanto, devemos ter 𝒂 ≠ 𝟏. Simplificando ambos os lados por (𝑎
− 1),
temos:

(𝑎 − 1) ≠ 1

𝒂 ≠ 𝟐

Logo, para que tenhamos solução única, é necessário que 𝒂 seja diferente de 1 e também que 𝒂 seja diferente de 2.
Portanto, é errado dizer que se 𝑎 ≠ 1, então a equação matricial 𝐴𝑋 = 𝑂 tem uma única solução.

Gabarito: ERRADO.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

𝟓𝒙 + 𝟓𝒚 + 𝟓𝒛 = 𝟑. 𝟎𝟎𝟎

(CESPE/SEDUC AL/2013/Adaptada) O sistema { 𝟓𝒙 + 𝟒𝒚 + 𝟒𝒛 = 𝟏. 𝟎𝟔𝟎

𝟔𝒙 + 𝟓𝒚 + 𝟓𝒛 = 𝟏. 𝟐𝟔𝟎

é impossível.

Comentários:

Vamos escalonar o sistema fazendo uso da matriz completa do sistema.

5 5 5 3000

L ←𝟏L +(−𝟏)L

5 5 5 3000

L3←𝟏L3+(−

)L1

5 5 5 3000

2 2 1

[5 4 4 1060] ~

6 5 5 1260

[0 −1 −1 −1940] ~

6 5 5 1260

[0 −1 −1 −1940]

0 −1 −1 −2340

L3←𝟏L3+(−𝟏)L2

~

5 5 5 3000

[0 −1 −1 −1940]

𝟎 𝟎 𝟎 −𝟒𝟎𝟎

A última equação do sistema escalonado, dada por 𝟎𝒙 + 𝟎𝒚 + 𝟎𝒛 = −𝟒𝟎𝟎, indica que estamos diante de um sistema impossível (SI).
Gabarito: CERTO.

𝟓𝒙 + 𝟓𝒚 + 𝟓𝒛 = 𝟑𝟎𝟎𝟎

(CESPE/SEDUC AL/2013/Adaptada) O sistema {𝟓𝒙 + 𝟒𝒚 + 𝟒𝒛 = 𝟏. 𝟎𝟔𝟎 é possível e indeterminado.
𝟒𝒙 + 𝟓𝒚 + 𝟐𝒛 = 𝟏. 𝟏𝟒𝟎

Comentários:

Vamos escalonar o sistema fazendo uso da matriz completa do sistema.

5 5 5 3000

L ←𝟏L +(−𝟏)L

5 5 5 3000

L3←𝟏L3+(−

)L1

5 5 5 3000

2 2 1

[5 4 4 1060] ~

4 5 2 1140

[0 −1 −1 −1940] ~

4 5 2 1140

[0 −1 −1 −1940]

0 1 −2 −1260

L3←𝟏L3+𝟏L2

~

5 5 5 3000

[0 −1 −1 −1940]

0 0 −3 −3200

Explicitando as variáveis, o sistema linear original equivale a:

5𝑥 + 5𝑦 + 5𝑧 = 3000

{ −𝑦 − 𝑧 = 1

−3𝑧 = −3200

Veja que o sistema acima é escalonado, pois o número de incógnitas diminui de equação para equação.

Trata-se de um sistema escalonado cujo número de equações (3) é igual ao número de incógnitas (3).
Logo, temos um sistema possível e determinado (SPD).

Gabarito: ERRADO.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

(CESPE/IFF/2018) Considere o sistema S de m equações lineares e n incógnitas, mostrado abaixo.

𝒂𝟏𝟏𝒙𝟏 + 𝒂𝟏𝟐𝒙𝟐 + ... + 𝒂𝟏𝒏𝒙𝒏 = 𝒃𝟏

𝒂𝟐𝟏𝒙𝟏 + 𝒂𝟐𝟐𝒙𝟐 + ... + 𝒂𝟐𝒏𝒙𝒏 = 𝒃𝟐

𝒂𝒎𝟏𝒙𝟏 + 𝒂𝒎𝟐𝒙𝟐 + ... + 𝒂𝒎𝒏𝒙𝒏 = 𝒃𝒎

Nesse sistema, 𝒙𝟏, 𝒙𝟐, ... , 𝒙𝒏 são as incógnitas, os coeficientes 𝒂𝐢𝐣 e os 𝒃𝒊 são números reais, para
𝟏 ≤ 𝒊 ≤ 𝒎 e 𝟏 ≤ 𝒋 ≤ 𝒏. A respeito das propriedades e das soluções do sistema
S, assinale a opção correta.
a) Considere que 𝑚 = 𝑛 e que 𝐴 = (𝑎𝑖𝑗) — a matriz dos coeficientes de S — seja tal que 𝑑𝑒𝑡(𝐴) = 0.Nesse caso, S não possui solução.

b) Se 𝛼 = (𝛼₁, 𝛼₂, ... , 𝛼𝑛) e 𝛽 = (𝛽₁ , 𝛽₂, ... , 𝛽𝑛) são soluções de S e se r é um número real qualquer, então 𝛼 + 𝛽 = (𝛼₁ + 𝛽₁, 𝛼₂ + 𝛽₂, ... , 𝛼𝑛 + 𝛽𝑛) e 𝑟𝛼 = (𝑟𝛼₁, 𝑟𝛼₂, ... , 𝑟𝛼𝑛) são também soluções de S.
c) Se 𝑚 < 𝑛, então S possui infinitas soluções.

d) Se 𝑚 = 𝑛 e se o sistema homogêneo associado a S — isto é, o sistema com os mesmos coeficientes 𝑎𝑖𝑗 apenas considerando todos os 𝑏𝑖 = 0 — tiver solução única, então o sistema S também terá solução única.
e) Se 𝑚 > 𝑛, então S não possui solução.

Comentários:

Veja que a questão apresenta um sistema linear genérico com 𝒎 equações e 𝒏 incógnitas. Vamos comentar cada alternativa.
a) Considere que 𝒎 = 𝒏 e que 𝑨 = (𝒂𝒊𝒋) — a matriz dos coeficientes de S — seja tal que 𝒅𝒆𝒕(𝑨) = 𝟎.Nesse caso, S não possui solução. ERRADO.

A alternativa afirma que, se o número de equações for igual ao número de incógnitas
(𝑚 = 𝑛) e se o determinante da matriz dos coeficientes for zero (det 𝐴 = 0), então o sistema não possui soluções.
Essa afirmativa está errada porque, de acordo com o Teorema de Cramer, se 𝐷 = 0, isto é, se det 𝐴
= 0,
podemos ter tanto um sistema possível indeterminado (SPI) quanto um sistema impossível
(SI). No primeiro caso, temos infinitas soluções.
SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

b) Se 𝜶 = (𝜶𝟏, 𝜶𝟐, ... , 𝜶𝒏) e 𝜷 = (𝜷𝟏 , 𝜷𝟐, ... , 𝜷𝒏) são soluções de S e se r é um número real qualquer,então 𝜶 + 𝜷 = (𝜶𝟏 + 𝜷𝟏, 𝜶𝟐 + 𝜷𝟐, ... , 𝜶𝒏 + 𝜷𝒏) e 𝒓𝜶 = (𝒓𝜶𝟏, 𝒓𝜶𝟐, ... ,
𝒓𝜶𝒏) são também soluções de

S. ERRADO.

A alternativa afirma três coisas sobre o sistema linear genérico apresentado:

* O sistema admite ao menos duas soluções e, portanto, admite infinitas soluções. Isso significa que estamos diante de um Sistema Possível Indeterminado (SPI).
* A soma das duas soluções de um SPI gera necessariamente uma nova solução do sistema;
e

* A multiplicação de uma solução do SPI por uma constante 𝒓 qualquer também é solução do sistema.
Para mostrar que as afirmações estão erradas, vamos mostrar um contraexemplo. Considere o seguinte

Sistema Possível e Indeterminado (SPI) de uma única equação:

{𝑥1 + 𝑥2 = 1

Note que (𝑥₁, 𝑥₂) = (1, 0) é solução do sistema e que (𝑥₁, 𝑥₂) = (0, 1) também é. Note, porém,
que:

* (1 + 0, 0 + 1) = (1, 1) não é solução do sistema, pois 1 + 1 ≠ 1; e

* 5. (1, 0) = (5, 0) não é solução do sistema, pois 5 + 0 ≠ 1.

A alternativa, portanto, está ERRADA.

c) Se 𝒎 < 𝒏, então S possui infinitas soluções. ERRADO.

Vimos que a questão apresenta um sistema linear genérico com 𝒎 equações e 𝒏 incógnitas.

A alternativa afirma que se o número de equações é menor do que o número de incógnitas (𝑚 < 𝑛),
então o sistema apresenta infinitas soluções.
Trata-se de uma afirmação ERRADA, pois o sistema pode ter um número de equações menor do que o número de incógnitas e ser um Sistema Impossível (SI) (sem solução).
Veja o seguinte contraexemplo:

{ 𝑥 + 𝑦 + 𝑧 = 1
2𝑥 + 2𝑦 + 2𝑧 = 3

Note que o número de equações é menor do que o número de incógnitas e o sistema é impossível. Isso porque, ao multiplicar a primeira equação por 2, obtém-se:
2𝑥 + 2𝑦 + 2𝑧 = 2

Essa equação contradiz a segunda equação do sistema, pois 2𝑥 + 2𝑦 + 2𝑧 não pode ser igual a 2 e a 3 ao mesmo tempo.
SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

d) Se 𝒎 = 𝒏 e se o sistema homogêneo associado a S — isto é, o sistema com os mesmos coeficientes 𝒂𝒊𝒋 apenas considerando todos os 𝒃𝒊 = 𝟎 — tiver solução única, então o sistema S também terá solução única.CERTO.

Se 𝑚 = 𝑛, o sistema tem o mesmo número de equações e de incógnitas. Nesse caso, a matriz dos coeficientes (𝑨) é quadrada.
O sistema original 𝑆 pode ser descrito na forma matricial por:

𝑨𝑿 = 𝑩

O sistema homogêneo associado é dado por:

𝑨𝑿 = 𝑶

Em que 𝑂 é a matriz nula de ordem 𝑛 × 1.

Se o sistema homogêneo associado tiver solução única, esse sistema homogêneo é um Sistema Possível e
Determinado (SPD). Pelo Teorema de Cramer, temos que 𝑫 = 𝐝𝐞𝐭 𝑨 ≠ 𝟎.

Como a matriz dos coeficientes (𝑨) é a mesma para o sistema original, esse sistema também será possível e determinado (SPD), pois 𝑫 = 𝐝𝐞𝐭 𝑨 ≠ 𝟎. Logo, o sistema original também terá solução única.
e) Se 𝒎 > 𝒏, então S não possui solução. ERRADO.

Vimos que a questão apresenta um sistema linear genérico com 𝒎 equações e 𝒏 incógnitas.

A alternativa afirma que se o número de equações é maior do que o número de incógnitas (𝑚 > 𝑛),
então o sistema não possui solução, ou seja, o sistema é impossível (SI).
Trata-se de uma afirmação ERRADA, pois nesse caso podemos ter um sistema possível e determinado
(SPD),
um sistema possível e indeterminado (SPI) ou até mesmo um sistema impossível (SI).

Veja o seguinte contraexemplo:

𝑥 + 𝑦 = 1

{2𝑥 + 2𝑦 = 2
3𝑥 + 3𝑦 = 3

Note que temos um número de equações (3) maior do que o número de incógnitas (2). Note, porém, que ao escalonar o sistema ficamos com:
𝑥 + 𝑦 = 1

{0𝑥 + 0𝑦 = 0 ~ {𝑥 + 𝑦 = 1
0𝑥 + 0𝑦 = 0

Note, portanto, que esse sistema é possível e indeterminado (SPI), admitindo infinitas soluções.

Gabarito: Letra D.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

(CESPE/SEDUC AL/2018) Julgue o item que se segue, relativos a matrizes e sistemas lineares.

Um sistema linear escrito na forma matricial 𝑷𝑿 = − 𝑿, em que 𝑷 é uma matriz 𝒏 × 𝒏 de coeficientes constantes e 𝑿 é a matriz das incógnitas, 𝒏 × 𝟏, tem solução única se, e somente se, a matriz𝑷 + 𝑰 for inversível (𝑰 é a matriz identidade 𝒏 × 𝒏).
Comentários:

Sabe-se que um sistema linear pode ser escrito na forma matricial 𝑨𝑿 = 𝑩, sendo:

* 𝑨: Matriz dos coeficientes ou matriz incompleta do sistema;

* 𝑿: Matriz das incógnitas;

* 𝑩: Matriz dos termos independentes.

==2d4a97==

O problema propõe a forma matricial 𝑃𝑋 = −𝑋. Vamos organizar essa equação matricial:

𝑃𝑋 = −𝑋

𝑃𝑋 + 𝑋 = 𝑂

Colocando a matriz 𝑋 em evidência:

(𝑷 + 𝑰)𝑿 = 𝑶

Comparando a expressão acima com a forma tradicional 𝑨𝑿 = 𝑩, temos que:

* (𝑷 + 𝑰) é a matriz dos coeficientes;

* 𝑿 é a matriz das incógnitas;

* 𝑶, que é a matriz nula, é a matriz dos termos independentes.

Para o sistema ter solução única, ele deve ser um sistema possível e determinado (SPD). Sabemos,
pelo
Teorema de Cramer, que isso ocorre quando o determinante da matriz dos coeficientes é diferente de zero.Isso significa que 𝐝𝐞𝐭(𝑷 + 𝑰) é diferente de zero.

Sabemos que uma matriz é inversível se, e somente se, essa matriz tem determinante diferente de zero.Logo, a matriz 𝑷 + 𝑰 deve ser inversível.

Gabarito: CERTO.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

(CESPE/Pref. São Luís/2017) Um sistema linear de 4 equações e 4 incógnitas pode ser escrito na forma matricial como 𝑨𝑿 = 𝑩, em que 𝑨 é a matriz, de ordem 𝟒 × 𝟒, dos coeficientes da equação; 𝑿é a matriz coluna, de ordem 𝟒 × 𝟏, das incógnitas da equação e 𝑩 é a matriz coluna, de ordem 𝟒 × 𝟏, dos termos independentes da equação.
Com referência a essas informações, assinale a opção correta.

a) Se 𝑋₁, 𝑋₂ e 𝑋₃ forem matrizes, de ordem 4 × 1, que são soluções distintas da referida equação matricial,então o determinante de 𝐴 será igual a zero.

b) Se a matriz 𝐴 tiver exatamente duas linhas iguais, então o sistema terá exatamente duas soluções distintas.
c) Se todos os elementos da matriz 𝐵 forem iguais a zero e o determinante de 𝐴 for igual a zero,
então o sistema não terá solução.
d) Se uma matriz 𝐶, de ordem 4 × 1, possuir dois elementos positivos e dois negativos e for tal que 𝐴𝐶 =
𝐵, então o determinante de 𝐴 será diferente de zero.

e) Se o determinante da matriz 𝐴 for igual a zero, então 𝐴 terá pelo menos duas linhas iguais.

Comentários:

Vamos avaliar todas as alternativas da questão.

a) Se 𝑿𝟏, 𝑿𝟐 e 𝑿𝟑 forem matrizes, de ordem 𝟒 × 𝟏, que são soluções distintas da referida equação matricial, então o determinante de 𝑨 será igual a zero. CERTO.
Se o sistema linear 𝐴𝑋 = 𝐵 apresenta mais de uma solução, então ele apresenta infinitas soluções e é classificado como Sistema Possível e Indeterminado (SPI).
Sabemos, pelo Teorema de Cramer, que este é um caso em que 𝐷 = 0, isto é, det 𝐴 =
Item. 0. O gabarito,
portanto, é letra A.

b) Se a matriz 𝑨 tiver exatamente duas linhas iguais, então o sistema terá exatamente duas soluções distintas. ERRADO.
Um sistema linear pode apresentar solução única, infinitas soluções ou nenhuma solução.

c) Se todos os elementos da matriz 𝑩 forem iguais a zero e o determinante de 𝑨 for igual a zero,
então o sistema não terá solução. ERRADO.
SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

Se todos os elementos da matriz B forem iguais a zero, temos um Sistema Linear Homogêneo. Nesse caso,se det 𝐴 = 0, isto é, 𝐷 = 0, o sistema apresenta infinitas soluções.

d) Se uma matriz 𝑪, de ordem 𝟒 × 𝟏, possuir dois elementos positivos e dois negativos e for tal que 𝑨𝑪 =
𝑩, então o determinante de 𝑨 será diferente de zero. ERRADO.

A alternativa apresenta uma solução para o sistema 𝐴𝑋 = 𝐵, dada pela matriz 𝑪. O
fato dessa solução apresentar dois elementos positivos e dois elementos negativos em nada influencia o determinante da matriz 𝑨. Como há a garantia de que temos uma solução, esse sistema pode ser:
* Possível e Determinado (SPD): apresenta solução única. Nesse caso, 𝐷 = det 𝐴 ≠ 0;

* Possível e Indeterminado (SPI): apresenta infinitas soluções, dentre elas a matriz 𝐶. Nesse caso,
𝐷 = det 𝐴 = 0.

Como o sistema pode ser SPI, então não necessariamente o determinante de 𝐴 será diferente de zero.

e) Se o determinante da matriz 𝑨 for igual a zero, então 𝑨 terá pelo menos duas linhas iguais.
ERRADO.

Da aula de determinantes, sabemos que existem muitas formas de uma matriz 𝑨 ter determinante zero.
Esse determinante zero pode ocorrer, por exemplo, por conta de filas iguais (linhas ou colunas),
de filas proporcionais ou também de filas que são combinações lineares de outras.
Logo, é errado dizer que se o determinante da matriz 𝐴 for igual a zero, necessariamente há linhas iguais.
Gabarito: Letra A.

(CESPE/CGE MG/2009) Em um concurso estadual, foram aprovados x candidatos, que serão distribuídos para trabalharem em y cidades do estado. Na hipótese de serem encaminhados 2 candidatos para cada cidade, sobrarão 70 candidatos para serem distribuídos. Entretanto, no caso de serem encaminhados 3candidatos para cada cidade, será necessário convocar mais 40 candidatos classificados nesse concurso.
Para determinação dos valores 𝒙 e 𝒚, obtém-se um sistema linear de duas equações com incógnitas 𝒙 e 𝒚.A ele está associada uma matriz 𝑴, formada pelos coeficientes das variáveis das suas equações.
Assinale a opção correta a respeito da solução desse sistema.
a) A matriz 𝑀 tem determinante diferente de zero.

b) O sistema é homogêneo.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

c) O sistema é compatível e indeterminado.

d) A matriz 𝑀 é não-inversível.

e) A matriz 𝑀 não pode ser transformada por meio de operações elementares sobre suas linhas na matriz identidade 2 por 2.
Comentários:

Vamos descrever o problema por meio de equações:

"Na hipótese de serem encaminhados 2 candidatos para cada cidade, sobrarão 70 candidatos para serem distribuídos"
Isso significa que, se tivéssemos 𝑥 − 70 candidatos, poderíamos encaminhar 2 para cada cidade.
Logo:

𝑦 =

𝑥 − 70

2𝑦 = 𝑥 − 70

𝒙 − 𝟐𝒚 = 𝟕𝟎

"...no caso de serem encaminhados 3 candidatos para cada cidade, será necessário convocar mais 40
candidatos classificados nesse concurso."

Isso significa que, se tivéssemos 𝑥 + 40 candidatos, poderíamos encaminhar 3 para cada cidade.
Logo:

𝑦 =

𝑥 + 40

3𝑦 = 𝑥 + 40

𝒙 − 𝟑𝒚 = −𝟒𝟎

O sistema linear obtido para se determinar 𝑥 e 𝑦 é:

{ 𝑥 − 2𝑦 = 70

𝑥 − 3𝑦 = −40

Na forma matricial, podemos escrever:

[1 −2 𝑥 70

] [𝑦] = [ ]

1 −3 −40

Vamos analisar as alternativas.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

a) A matriz 𝑴 tem determinante diferente de zero. CERTO.

Como  é a matriz dos coeficientes, então:

1 −2

det  = | |

1 −3

= [1 × (−3)] − [(−2) × 1]

= −3 − (−2)

= −1

Portanto, o determinante de  é diferente de zero. Logo, o gabarito é letra A.

b) O sistema é homogêneo. ERRADO.

O sistema não é homogêneo, pois a matriz dos termos independentes, [ 70 ], não é nula.

−40

c) O sistema é compatível e indeterminado. ERRADO.

O sistema é possível e determinado, pois 𝐷 = det  ≠ 0.

d) A matriz 𝑴 é não-inversível. ERRADO.

A matriz  apresenta determinante diferente de zero. Portanto, ela é inversível.

e) A matriz 𝑴 não pode ser transformada por meio de operações elementares sobre suas linhas na matriz identidade 𝟐 por 𝟐. ERRADO.
Temos a matriz  

Se fizermos L₂ = (−1)L₂ + L₁, ficamos com:

Fazendo L₁ = L₁ + 2L₂, ficamos com:

1 −2

]

1 −3

1 −2

0 1 ]

1 0

[ ]

0 1

Portanto, a matriz  pode ser transformada na matriz identidade 2 por 2.

Gabarito: Letra A.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

(CESPE/PETROBRAS/2008/Adaptada) Considerando que A seja a matriz formada pelos coeficientes do 𝒂𝒙 + 𝒃𝒚 = 𝝁 𝒙 𝝁 sistema {𝒄𝒙 + 𝒅𝒚 = 𝒗, que 𝑾 = (𝒚) e que, 𝒁 = (𝒗) assinale a opção correta.
a) Se as componentes de 𝑍 forem nulas e o determinante de 𝐴 for igual a zero, então o sistema terá infinitas soluções.
b) O sistema pode ser representado matricialmente por 𝐴𝑍 = 𝑊.

c) O determinante de 𝐴 é igual a 𝑎𝑑 + 𝑏𝑐.

d) A substituição dos elementos 𝑐 e 𝑑, da segunda linha 𝐴, por 2𝑎 e 2𝑏, respectivamente, o determinante da nova matriz será igual a 4𝑎𝑏.
Comentários:

Temos que a matriz dos coeficientes é dada por independentes e 𝑾 é a matriz das incógnitas.Vamos analisar as alternativas.

𝑎 𝑏

𝐴 = [𝑐 𝑑]. Além disso, 𝒁 é a matriz dos termos a) Se as componentes de 𝒁 forem nulas e o determinante de 𝑨 for igual a zero,então o sistema terá infinitas soluções. CERTO.
Se as componentes de 𝑍 forem nulas, temos um sistema homogêneo. Nesse caso, se 𝐷 = det 𝐴 = 0,
temos um sistema possível e indeterminado (SPI), que admite infinitas soluções. O gabarito, portanto, é letra A.
b) O sistema pode ser representado matricialmente por 𝑨𝒁 = 𝑾. ERRADO.

O sistema pode ser representado por 𝐴𝑊 = 𝑍, pois 𝒁 é a matriz dos coeficientes, que deve estar na equação sem multiplicar outra matriz.
c) O determinante de 𝑨 é igual a 𝒂𝒅 + 𝒃𝒄. ERRADO.

O determinante de 𝐴 é 𝑎𝑑 − 𝑏𝑐.

d) A substituição dos elementos 𝒄 e 𝒅, da segunda linha 𝑨, por 𝟐𝒂 e 𝟐𝒃, respectivamente, o determinante da nova matriz será igual a 𝟒𝒂𝒃. ERRADO.
Nesse caso, o determinante seria zero, pois teríamos duas linhas proporcionais:

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

| 𝑎 𝑏 | = [𝑎. 2𝑏] − [𝑏. 2𝑎] = 2𝑎𝑏 − 2𝑎𝑏 = 0
2𝑎 2𝑏

Gabarito: Letra A.

Texto para as próximas questões 𝑎𝑥 + 2𝑦 + 𝑧 = 0
{𝑥 + 𝑎²𝑦 + 3𝑧 = 0
2𝑥 + 3𝑦 + 5𝑧 = 0

Considerando o sistema homogêneo de equações lineares apresentado acima, em que a é uma constante real, julgue os itens que se segue.
(CESPE/INPE/2008) Para 𝒂 = −𝟏, a única solução do sistema é 𝒙 = 𝒚 = 𝒛 = 𝟎.

(CESPE/INPE/2008) Independentemente do valor de a, o sistema tem apenas a solução 𝒙 = 𝒚 = 𝒛 = 𝟎.Comentários:

Note que estamos diante de um sistema linear homogêneo, pois todos os termos independentes são zero.
Nesse caso, segundo o Teorema de Cramer, temos:

𝑎 2 1

Vamos calcular o determinante da matriz dos coeficientes, isto é, o determinante 𝐷 = |1 𝑎²
3|.

2 3 5

𝑎 2 1 𝑎 2

|1 𝑎² 3| 1 𝑎²

2 3 5 2 3

Parte Negativa Parte Positiva

𝐷 = [𝒂. 𝒂𝟐. 𝟓 + 𝟐. 𝟑. 𝟐 + 𝟏. 𝟏. 𝟑] − [𝟏. 𝒂𝟐. 𝟐 + 𝒂. 𝟑. 𝟑 + 𝟐. 𝟏. 𝟓]

𝐷 = [5𝑎³ + 12 + 3] − [2𝑎² + 9𝑎 + 10]

𝐷 = 5𝑎³ − 2𝑎² − 9𝑎 + 5

Vamos analisar as alternativas.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

Questão 10

Se 𝑎 = −1, o determinante da matriz dos coeficientes é:

𝐷 = 5𝑎³ − 2𝑎² − 9𝑎 + 5

𝐷 = 5(−1)³ − 2(−1)² − 9. (−1) + 5

𝐷 = −5 − 2 + 9 + 5

𝐷 = 7

Como 𝐷 ≠ 0, o sistema é possível e determinado (SPD), admitindo solução única. Como estamos lidando com um sistema homogêneo, a solução única é a solução trivial, dada por 𝑥 = 𝑦 = 𝑧 =Item. 0. O gabarito,
portanto, é CERTO.

Questão 11

Quando 𝐷 = 0, isto é, quando:

5𝑎³ − 2𝑎² − 9𝑎 + 5 = 0

O sistema linear em questão é possível e indeterminado (SPI). Nesse caso, o sistema admite infinitas soluções, dentre as quais a solução trivial 𝑥 = 𝑦 = 𝑧 = 0. O gabarito, portanto, é ERRADO.
Observação: necessariamente existe um valor real de 𝑎 que é raiz daquela equação, pois todo polinômio de grau ímpar admite solução real. O assunto polinômios não faz parte dessa aula. Caso faça parte do seu edital,o tema será visto em outra aula.

Gabarito: 10 - CERTO. 11 - ERRADO.

(CESPE/PM DF/2007) Julgue o seguinte item com relação a geometria do plano cartesiano, modelos periódicos e modelos lineares.
Considere o seguinte sistema de equações lineares homogêneo.

𝒙 + 𝒂𝒚 − 𝟐𝒛 = 𝟎

{ 𝒂𝒙 + 𝒚 + 𝒛 = 𝟎

𝒙 − 𝒚 − 𝒛 = 𝟎

Nesse caso, é correto afirmar que, se 𝒂 = −𝟏 ou se 𝒂 = −𝟐, então esse sistema só admite a solução 𝒙 = 𝒚 = 𝒛 = 𝟎.Comentários:

Note que estamos diante de um sistema linear homogêneo, pois todos os termos independentes são zero.
Nesse caso, segundo o Teorema de Cramer, temos:

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

1 𝑎 −2

Vamos calcular o determinante da matriz dos coeficientes, isto é, o determinante 𝐷 = |𝑎 1
1 |.

1 −1 −1

1 𝑎 −2 1 𝑎

|𝑎 1 1 | 𝑎 1

1 −1 −1 1 −1

Parte Negativa Parte Positiva

𝐷 = [𝟏. 𝟏. (−𝟏) + 𝒂. 𝟏. 𝟏 + (−𝟐). 𝒂. (−𝟏)] − [(−𝟐). 𝟏. 𝟏 + 𝟏. 𝟏. (−𝟏) + 𝒂. 𝒂.
(−𝟏)]

𝐷 = [−1 + 𝑎 + 2𝑎] − [−2 − 1 − 𝑎²]

𝐷 = 3𝑎 + 2 + 𝑎²

𝐷 = 𝑎² + 3𝑎 + 2

Note que, para 𝒂 = −𝟏 e para 𝒂 = −𝟐, temos 𝑫 = 𝟎:

𝒂 = −𝟏

→ 𝐷 = (−1)² + 3. (−1) + 2

𝐷 = 1 − 3 + 2

𝐷 = 0

𝒂 = −𝟐

→ 𝐷 = (−2)² + 3. (−2) + 2

𝐷 = 4 − 6 + 2

𝐷 = 0

Portanto, para 𝒂 = −𝟏 e para 𝒂 = −𝟐, o sistema é possível e indeterminado (SPI),
admitindo infinitas soluções. O gabarito, portanto, é ERRADO.
Gabarito: ERRADO.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

LISTA DE QUESTÕES - CEBRASPE

Solução de um sistema linear

(CESPE/IFF/2018) Considere que 𝑨 = (𝒂𝒊𝒋) seja uma matriz quadrada de dimensão 𝒏 × 𝒏 e de entradas reais; que 𝑩 = (𝒃𝒊) seja uma matriz coluna, de dimensão 𝒏 × 𝟏 e de entradas reais, e que 𝑿= (𝒙𝒊) seja a matriz das incógnitas, uma matriz coluna de dimensão 𝒏 × 𝟏. Nesse caso, para se resolver o sistema matricial 𝑨𝑿 = 𝑩, o método indicado é o denominado a) método de diferenças finitas.
b) método de quadratura de Gauss.

c) método de Simpson.

d) método de elementos de contorno.

e) método de eliminação de Gauss.

Texto para as próximas questões 𝑥 − 𝑦 − 𝑧 = 0
Considerando o sistema linear {

2𝑥 + 3𝑦 + 2𝑧 = 2

−𝑥 + 2𝑦 − 2𝑧 = −11

, julgue os itens que se segue.

(CESPE/SGA AC/2008) 𝒚 > 𝒙.

(CESPE/SGA AC/2008) Todas as soluções do sistema são números naturais.
(CESPE/SGA AC/2008) 𝒛 = 𝒙 + |𝒚|

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

GABARITO - CEBRASPE

Solução de um sistema linear

LETRA E
ERRADO
ERRADO
CERTO

==2d4a97==

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

LISTA DE QUESTÕES - CEBRASPE

Discussão de um sistema linear

(CESPE/Pref. São Cristóvão/2019) Com relação a sistemas lineares e análise combinatória, julgue o item.
Para todo sistema linear da forma 𝑨𝑿 = 𝑩, em que 𝑨 é uma matriz quadrada 𝒎 × 𝒎, 𝑿 e 𝑩 são matrizes colunas 𝒎 × 𝟏, e 𝒅𝒆𝒕(𝑨) = 𝟎, o sistema não tem solução.
𝒂 − 𝟏 𝒂 − 𝟏 𝒂 − 𝟏

(CESPE/SEDUC CE/2009/Adaptada) Acerca da matriz 𝑨 = [𝒂 − 𝟏 𝟏 𝟐

𝒂 − 𝟏 𝟏 −𝟐

], em que 𝒂 é um número real, julgue o item a seguir.
𝒙 𝟎

Se 𝒂 ≠ 𝟏, então a equação matricial 𝑨𝑿 = 𝑶, em que 𝑿 = [𝒚] e 𝑶 = [𝟎] é a matriz nula de ordem 𝟑 × 𝟏,
𝒛 𝟎

tem uma única solução.

𝟓𝒙 + 𝟓𝒚 + 𝟓𝒛 = 𝟑. 𝟎𝟎𝟎

(CESPE/SEDUC AL/2013/Adaptada) O sistema { 𝟓𝒙 + 𝟒𝒚 + 𝟒𝒛 = 𝟏. 𝟎𝟔𝟎

𝟔𝒙 + 𝟓𝒚 + 𝟓𝒛 = 𝟏. 𝟐𝟔𝟎

é impossível.

𝟓𝒙 + 𝟓𝒚 + 𝟓𝒛 = 𝟑𝟎𝟎𝟎

(CESPE/SEDUC AL/2013/Adaptada) O sistema {𝟓𝒙 + 𝟒𝒚 + 𝟒𝒛 = 𝟏. 𝟎𝟔𝟎 é possível e indeterminado.
𝟒𝒙 + 𝟓𝒚 + 𝟐𝒛 = 𝟏. 𝟏𝟒𝟎

(CESPE/IFF/2018) Considere o sistema S de m equações lineares e n incógnitas, mostrado abaixo.

𝒂𝟏𝟏𝒙𝟏 + 𝒂𝟏𝟐𝒙𝟐 + ... + 𝒂𝟏𝒏𝒙𝒏 = 𝒃𝟏

𝒂𝟐𝟏𝒙𝟏 + 𝒂𝟐𝟐𝒙𝟐 + ... + 𝒂𝟐𝒏𝒙𝒏 = 𝒃𝟐

𝒂𝒎𝟏𝒙𝟏 + 𝒂𝒎𝟐𝒙𝟐 + ... + 𝒂𝒎𝒏𝒙𝒏 = 𝒃𝒎

Nesse sistema, 𝒙𝟏, 𝒙𝟐, ... , 𝒙𝒏 são as incógnitas, os coeficientes 𝒂𝐢𝐣 e os 𝒃𝒊 são números reais, para
𝟏 ≤ 𝒊 ≤ 𝒎 e 𝟏 ≤ 𝒋 ≤ 𝒏. A respeito das propriedades e das soluções do sistema
S, assinale a opção correta.
a) Considere que 𝑚 = 𝑛 e que 𝐴 = (𝑎𝑖𝑗) — a matriz dos coeficientes de S — seja tal que 𝑑𝑒𝑡(𝐴) = 0.Nesse caso, S não possui solução.

b) Se 𝛼 = (𝛼₁, 𝛼₂, ... , 𝛼𝑛) e 𝛽 = (𝛽₁ , 𝛽₂, ... , 𝛽𝑛) são soluções de S e se r é um número real qualquer, então 𝛼 + 𝛽 = (𝛼₁ + 𝛽₁, 𝛼₂ + 𝛽₂, ... , 𝛼𝑛 + 𝛽𝑛) e 𝑟𝛼 = (𝑟𝛼₁, 𝑟𝛼₂, ... , 𝑟𝛼𝑛) são também soluções de S.
c) Se 𝑚 < 𝑛, então S possui infinitas soluções.

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

d) Se 𝑚 = 𝑛 e se o sistema homogêneo associado a S — isto é, o sistema com os mesmos coeficientes 𝑎𝑖𝑗 apenas considerando todos os 𝑏𝑖 = 0 — tiver solução única, então o sistema S também terá solução única.
e) Se 𝑚 > 𝑛, então S não possui solução.

(CESPE/SEDUC AL/2018) Julgue o item que se segue, relativos a matrizes e sistemas lineares.

Um sistema linear escrito na forma matricial 𝑷𝑿 = − 𝑿, em que 𝑷 é uma matriz 𝒏 × 𝒏 de coeficientes constantes e 𝑿 é a matriz das incógnitas, 𝒏 × 𝟏, tem solução única se, e somente se, a matriz𝑷 + 𝑰 for inversível (𝑰 é a matriz identidade 𝒏 × 𝒏).
(CESPE/Pref. São Luís/2017) Um sistema linear de 4 equações e 4 incógnitas pode ser escrito na forma matricial como 𝑨𝑿 = 𝑩, em que 𝑨 é a matriz, de ordem 𝟒 × 𝟒, dos coeficientes da equação; 𝑿é a matriz

==2d4a97==

coluna, de ordem 𝟒 × 𝟏, das incógnitas da equação e 𝑩 é a matriz coluna, de ordem 𝟒 × 𝟏, dos termos independentes da equação.
Com referência a essas informações, assinale a opção correta.

a) Se 𝑋₁, 𝑋₂ e 𝑋₃ forem matrizes, de ordem 4 × 1, que são soluções distintas da referida equação matricial,então o determinante de 𝐴 será igual a zero.

b) Se a matriz 𝐴 tiver exatamente duas linhas iguais, então o sistema terá exatamente duas soluções distintas.
c) Se todos os elementos da matriz 𝐵 forem iguais a zero e o determinante de 𝐴 for igual a zero,
então o sistema não terá solução.
d) Se uma matriz 𝐶, de ordem 4 × 1, possuir dois elementos positivos e dois negativos e for tal que 𝐴𝐶 =
𝐵, então o determinante de 𝐴 será diferente de zero.

e) Se o determinante da matriz 𝐴 for igual a zero, então 𝐴 terá pelo menos duas linhas iguais.

(CESPE/CGE MG/2009) Em um concurso estadual, foram aprovados x candidatos, que serão distribuídos para trabalharem em y cidades do estado. Na hipótese de serem encaminhados 2 candidatos para cada cidade, sobrarão 70 candidatos para serem distribuídos. Entretanto, no caso de serem encaminhados 3candidatos para cada cidade, será necessário convocar mais 40 candidatos classificados nesse concurso.
Para determinação dos valores 𝒙 e 𝒚, obtém-se um sistema linear de duas equações com incógnitas 𝒙 e 𝒚.A ele está associada uma matriz 𝑴, formada pelos coeficientes das variáveis das suas equações.
Assinale a opção correta a respeito da solução desse sistema.
a) A matriz 𝑀 tem determinante diferente de zero.

b) O sistema é homogêneo.

c) O sistema é compatível e indeterminado.

d) A matriz 𝑀 é não-inversível.

e) A matriz 𝑀 não pode ser transformada por meio de operações elementares sobre suas linhas na matriz identidade 2 por 2.
SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

(CESPE/PETROBRAS/2008/Adaptada) Considerando que A seja a matriz formada pelos coeficientes do 𝒂𝒙 + 𝒃𝒚 = 𝝁 𝒙 𝝁 sistema {𝒄𝒙 + 𝒅𝒚 = 𝒗, que 𝑾 = (𝒚) e que, 𝒁 = (𝒗) assinale a opção correta.
a) Se as componentes de 𝑍 forem nulas e o determinante de 𝐴 for igual a zero, então o sistema terá infinitas soluções.
b) O sistema pode ser representado matricialmente por 𝐴𝑍 = 𝑊.

c) O determinante de 𝐴 é igual a 𝑎𝑑 + 𝑏𝑐.

d) A substituição dos elementos 𝑐 e 𝑑, da segunda linha 𝐴, por 2𝑎 e 2𝑏, respectivamente, o determinante da nova matriz será igual a 4𝑎𝑏.
Texto para as próximas questões 𝑎𝑥 + 2𝑦 + 𝑧 = 0
{𝑥 + 𝑎²𝑦 + 3𝑧 = 0
2𝑥 + 3𝑦 + 5𝑧 = 0

Considerando o sistema homogêneo de equações lineares apresentado acima, em que a é uma constante real, julgue os itens que se segue.
(CESPE/INPE/2008) Para 𝒂 = −𝟏, a única solução do sistema é 𝒙 = 𝒚 = 𝒛 = 𝟎.

(CESPE/INPE/2008) Independentemente do valor de a, o sistema tem apenas a solução 𝒙 = 𝒚 = 𝒛 = 𝟎.
(CESPE/PM DF/2007) Julgue o seguinte item com relação a geometria do plano cartesiano, modelos periódicos e modelos lineares.
Considere o seguinte sistema de equações lineares homogêneo.

𝒙 + 𝒂𝒚 − 𝟐𝒛 = 𝟎

{ 𝒂𝒙 + 𝒚 + 𝒛 = 𝟎

𝒙 − 𝒚 − 𝒛 = 𝟎

Nesse caso, é correto afirmar que, se 𝒂 = −𝟏 ou se 𝒂 = −𝟐, então esse sistema só admite a solução 𝒙 = 𝒚 = 𝒛 = 𝟎.
SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

Equipe Exatas Estratégia Concursos
Aula 18

GABARITO - CEBRASPE

Discussão de um sistema linear

ERRADO
ERRADO
CERTO
ERRADO

LETRA D
CERTO
LETRA A
LETRA A

LETRA A
CERTO
ERRADO
ERRADO

SERPRO - Raciocínio Lógico - 2023 (Pós-Edital)

www.estrategiaconcursos.com.br

05152001900 - Everton Murilo Vieira

