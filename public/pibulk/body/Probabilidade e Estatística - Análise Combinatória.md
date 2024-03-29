# Probabilidade e Estatística - Análise Combinatória

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Introdução Análise Combinatória

2) Princípios Fundamentais de Contagem

3) Fatorial de um Número Natural

4) Permutação

5) Outros Tipos de Permutação

6) Arranjo e Combinação

7) Questões Comentadas - Princípios de Contagem - Cebraspe

8) Questões Comentadas - Permutação - Cebraspe

9) Questões Comentadas - Arranjo e Combinação - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Olá, amigos! Como estão os estudos de Estatística?

Nesta aula, vamos estudar análise combinatória, que são ferramentas de contagem.

Como assim?Uma aula sobre contagem? 1, 2, 3,... ?

Sim e não! Sim, porque, de fato, você pode contar os eventos, simplesmente. Essa é uma boa estratégia quando há poucos eventos.
Mas, quando há muitos eventos, essa contagem se torna muito trabalhosa, você se perde no meio do caminho,... Então, a ideia dessas ferramentas é ajudá-lo a "contar" os eventos com eficiência!
Algumas questões de concursos cobram a análise combinatória, puramente; e outras cobram no cálculo de probabilidades. Então, esse é um assunto bem importante.Até já!

Luana Brandão

Posso te contar um pouquinho sobre a minha trajetória? Sou Doutora em Engenharia de
Produção, pela
Universidade Federal Fluminense, e Auditora Fiscal da SEFAZ-RJ. Sou professora de
Estatística do Estratégia porque quero muito te ajudar na sua trajetória, rumo à aprovação!
Se tiver alguma dúvida, entre em contato comigo!

M professoraluanabrandao@gmail.com
@professoraluanabrandao

"Lute e conquiste, supere seus medos. Acredite em seus sonhos."

Aislan Dlano

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ANÁLISE CoMBINATóRIA

Introdução

A Análise Combinatória, ou simplesmente combinatória, estuda técnicas de contagem, para que você não precise efetivamente contar todos os elementos.
Por exemplo, quantos números de 3 algarismos podemos formar com o conjunto {1, 3, 4},
sem repetir os algarismos, em um mesmo número?
Bem, as possibilidades são:

i) 134; ii) 143;
iii) 314;

iv) 341; v) 413; vi) 431.

Portanto, são 6 números distintos.

Para resolver esse problema, não precisamos de nenhuma técnica específica. Só precisamos raciocinar e contar todas as possibilidades.
Mas, e se o conjunto de algarismos fosse de todos os números de 1 a 9? Perderíamos muito tempo para relacionar todas as possibilidades, e talvez nos perderíamos em algum momento.
A análise combinatória facilita justamente a contagem das possibilidades, em conjuntos finitos.

Ela também permite efetuar contagens de subconjuntos com determinadas características. Por exemplo,poderíamos estar interessados apenas nos números pares ou nos números primos.

Princípios Fundamentais da Contagem

Nesta seção, veremos os princípios fundamentais de contagem, que você vai utilizar muito. Eles permeiam as ferramentas da análise combinatória e são requisitados em praticamente todas as questões sobre o assunto, desde as mais simples, até as mais complexas.
Princípio Multiplicativo

Esse princípio enuncia o seguinte:

i Se um evento A ocorre de m maneiras diferentes e se, para cada uma dessas maneiras, um i i outro evento B ocorre de n maneiras diferentes, então o número de maneiras diferentes de ;
a i
; ambos os eventos (A e B) ocorrerem émxn.
;

L......

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para ilustrar, vamos considerar que João precisa se vestir com uma calça e uma blusa e que ele tem 3 calças e 4 blusas. Nesse caso, o evento A corresponde a vestir uma calça, com m = 3possibilidades, e o evento B
corresponde a vestir uma blusa, com n = 4 possibilidades.

Segundo o princípio multiplicativo, o número de maneiras distintas de João se vestir é:

mxn=3x4=12

Calças Blusas
Possibilidades

Possibilidades

Calça 2 Blusa 1

Calças Blusas
Possibilidades

Observe que, para cada calça, há 4 possibilidades de blusas. Portanto, são 4 blusas possíveis para a calça 1;
4 blusas possíveis para a calça 2; e 4 blusas possíveis para a calça 3. Somando todas essas possibilidades,temos 4 + 4 + 4 = 3x4 = 12.

Obtemos o mesmo resultado se pensarmos que há 3 possibilidades de calça para cada blusa.

Podemos extrapolar esse princípio para qualquer número de eventos. Ou seja, se tivermos um terceiro evento C que ocorre de p maneiras diferentes, então o número de maneiras diferentes de os eventos A, B eC ocorrerem é m x n x p.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Utilizando o mesmo exemplo, considerando que João precisa utilizar um cinto e que ele tem p = 2 cintos distintos, então o número de maneiras distintas de João colocar uma calça, uma blusa e um cinto é:
mxnxp = 3x4x2 = 24

Generalizando para n eventos, com pi possibilidades para o evento Ai, P2 possibilidades para o evento A2,... e pn possibilidades para 0 evento An, então 0 número de maneiras de todos os n eventos ocorrerem é:
P(Ai e A2 e ... e An) = pix p2x ... x pn l«** IX
i (VUNESP/2019 - Prefeitura de dois Córregos/SP) Em um grupo de pessoas, há 12 homens e 13
mulheres.

= Com essas pessoas, uma dupla será aleatoriamente formada, com um homem e uma mulher, para participar de um concurso. O número total de possibilidades para a formação dessa dupla é a) 12.
b) 144.

c) 156.

d) 168.

; e) 288.

i Comentários:

I

: Havendo 12 homens e 13 mulheres, 0 número de possibilidades de selecionar um homem
E uma mulher é,

= pelo princípio multiplicativo:

12 x 13 = 156

I

: Gabarito: C

I

i (2019 - Prefeitura de Jacutinga/MG) Assinale a alternativa que contém a quantidade de vezes que é possível usar de maneiras diferentes duas blusas, três calças e quatro meias:

; a) 24 maneiras diferentes.

b) 28 maneiras diferentes.

: c) 32 maneiras diferentes.

d) 36 maneiras diferentes.

I

i Comentários:

: Há 2 blusas para cada uma das 3 calças.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Além disso, para cada possível combinação de uma blusa e uma calça, há 4 meias diferentes.
Logo, o número de alternativas é, pelo princípio multiplicativo:

2 x 3 x 4 = 24

Gabarito: A

(CESPE/2013 - TRT-ES) Os alunos de uma turma cursam 4 disciplinas que são ministradas por 4 professores diferentes. As avaliações finais dessas disciplinas serão realizadas em uma mesma semana, de segunda a sexta-feira, podendo ou não ocorrerem em um mesmo dia. A respeito dessas avaliações, julgue o item seguinte.
Se cada professor escolher o dia em que aplicará a avaliação final de sua disciplina de modo independente dos demais, haverá mais de 500 maneiras de se organizar o calendário dessas avaliações.
Comentários:

Vamos representar as escolhas dos 4 professores da seguinte forma:

Sabendo que há 5 dias disponíveis, então cada professor terá 5 possibilidades de escolha:

5 5 5 5

Pelo princípio multiplicativo, o número de maneiras de organizar o calendário para os 4 professores é:
Número de maneiras = 5x5x5x5 = 625
Ou seja, há mais de 500 maneiras de organizar.

Gabarito: Certo.

(FGV/2022 - PM-PB) Cada vértice de um quadrado ABCD deverá ser pintado com uma cor.
Há 5 cores diferentes disponíveis para essa tarefa. A única restrição é que os vértices que estejam em extremidades opostas de qualquer diagonal do quadrado (AC e BD) sejam pintados com cores diferentes. O número de maneiras diferentes de pintar os vértices desse quadrado é:
a) 18

b) 60

c) 120

d) 240

e) 400

Comentários:

A questão informa que temos 5 cores disponíveis para pintar 4 vértices de um quadrado:

A B

D C

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= No entanto, a cor do vértice A deve ser diferente da cor do vértice C; e a cor do vértice B deve ser diferente da cor do vértice D.
I

: Assim, há 5 possibilidades para o vértice A e 4 possibilidades para o vértice C.

: Similarmente, há 5 possibilidades para o vértice B e 4 possibilidades para o vértice D.

= Pelo princípio multiplicativo, o número total de possibilidades para todos os 4 vértices é:

5 x 5 x 4 x 4 = 400

I

; Gabarito: E

L

Contagem de Divisores

Com base no princípio multiplicativo, é possível calcular a quantidade de divisores de um número natural.O primeiro passo é fatorar o número natural em números primos. Por exemplo, vamos fatorar o número
60:

60 2

30 2

15 3

5 5

Assim, podemos representar o número 60, a partir dos seus divisores primos, da seguinte forma:

60 = 22 x 31 x 51

Agora é o pulo do goto: Todos os divisores de um número são formados pelo produto de um subconjunto dos seus divisores primos. Por exemplo, o número 15 é produto de 3 e 5 e pode ser representado como:
15 = 2o x 31 x 51

Assim, todos os divisores de 60, que indicamos como d₆₀, podem ser representados da seguinte forma:

d60 = 2X x 3y x 5Z, sendo x < 2,y < l,z < 1

Logo, as possibilidades para cada expoente são:

* x: 0, 1 ou 2 (3 possibilidades);

* y: 0 ou 1 (2 possibilidades);

* z: 0 ou 1 (2 possibilidades).

Pelo princípio multiplicativo, devemos multiplicar as possibilidades desses eventos para encontrar o número de possibilidades, no total:
3 x 2 x 2 = 12

Logo, há 12 divisores de 60.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

FIQUE

ATENTO!

Os expoentes dos divisores primos de 60 eram 2, 1 e 1, e os valores multiplicados para encontrar o número de divisores foram 3, 2 e 2.
Portanto, basta somar 1 a cada expoente e multiplicá-los:

Número de Divisores = (2 + 1) x (1 + 1) x (1 + 1) = 3 x 2 x 2

Isso porque o número de possibilidades que cada expoente pode assumir é igual ao seu valor, mais 1,
correspondente ao zero.

I«** IX

r t í (FCC/2016 - Companhia Metropolitana/SP) Uma tabela retangular de 12 linhas por 18 colunas possui i campos de preenchimento. Outras tabelas retangulares com combinações diferentes de linhas e colunas também possuem 216 campos de preenchimento. Observando-se que uma tabela de 12 linhas por 18
= colunas é diferente de uma tabela de 18 linhas por 12 colunas, o total de tabelas retangulares diferentes
= com 216 campos de preenchimento é igual a i a) 14
b) 12

c) 10

d) 16

e) 18

I

i Comentários:

I

: O enunciado pede a quantidade de tabelas distintas que podem ser formadas com 216 campos, de modo que uma tabela com A linhas e B colunas é diferente de uma tabela B linhas e A colunas.
: Essa quantidade corresponde ao número de maneiras de obter 216 pelo produto de 2 números inteiros:
1 x 216; 2 x 108; ; 108 x 2; 216 x 1

: Ou seja, ela corresponde ao número divisores de 216.

= Para isso, vamos primeiro fatorar 216 em números primos:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

216 2

108 2

54 2

27 3

9 3

3 3

216 = 23 x 33

Os divisores de 216 podem ser, portanto, representados da seguinte forma:

= 2* x 3y

Nesse caso, x pode assumir 3 + 1 = 4 possibilidades (0,1, 2 ou 3), assim como y.,
que também pode assumir as mesmas 3 + 1 = 4 possibilidades. Pelo princípio multiplicativo, o número total de possibilidades é:
4x4= 16

Gabarito: D.

Princípio Aditivo

Agora, veremos outro princípio fundamental de contagem, chamado de princípio aditivo:

r

|

i Se o evento A ocorre de m maneiras diferentes e o evento B ocorre de n maneiras diferentes, i i e se A e B são mutuamente exclusivos (ou seja, se um ocorrer o outro não ocorre), então ;
: o número de maneiras de ocorrer um dos eventos (A ou B) é m + n.
;

li

I

Para ilustrar esse princípio, vamos considerar que João precisa se calçar e que ele possui 3 opções de tênis e
2 opções de sapatos.

Nesse caso, o evento A corresponde a calçar um tênis, com m = 3 possibilidades, e o evento B corresponde a calçar um sapato, com n = 2 possibilidades. Esses eventos são mutuamente excludentes(João calçará um tênis ou um sapato; ele não pode calçar os dois). Assim, o número de maneiras de João se calçar é a soma:
m+n=3+2=5

Podemos generalizar esse princípio para qualquer número de eventos.

Havendo n eventos mutuamente exclusivos, com pi possibilidades para o evento Ai, p2
possibilidades para o evento A₂,... e pn possibilidades para o evento An, então o número de maneiras um dos n eventos ocorrer é:
P(Ai OU A2 OU ... OU An) = Pi + p2 + + pn

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

* Quando ambos ocorrem os eventos (A E B), multiplicamos as possibilidades;

* Quando ocorre somente um dos eventos (A OU B), somamos as possibilidades.

EXEMPLIFICANDO

Agora, vejamos um exemplo combinando esses dois princípios.
Vamos considerar que Maria precisa se vestir e se calçar, dispondo de:

* 4 vestidos;

* 2 saias;

* 3 blusas; e

* 5 sapatos.

Nesse caso, Maria irá colocar um vestido (evento A) OU um conjunto de saia (evento B) E
blusa (evento C). De uma forma ou de outra, irá colocar também um sapato (evento D).

Nessa situação, as possibilidades de Maria se vestir e se calçar são:

i) Os eventos B (saia) e C (blusa) são concomitantes - princípio multiplicativo:

2x3 = 6 possibilidades;

ii) Os eventos A (vestido) e (i) (saia e blusa) são excludentes - princípio aditivo:

4 + 6 = 10 possibilidades;

iii) Os eventos D (sapato) e (iii) (saia e blusa ou vestido) são concomitantes - princípio multiplicativo:
5 x 10 = 50 possibilidades.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (2017 - Conselho Regional de Educação Física/CE) Numa estante encontram-se 4 dicionários de inglês, 3 de i espanhol e 2 de francês.;

I

I

: De quantas maneiras uma pessoa pode escolher dois dicionários dessa estante e que sejam de idiomas i diferentes?
i

: a) 22

b) 24
j i c) 26j d) 28

I

i Comentários:

I

i Selecionando 2 dicionários de idiomas diferentes, podemos encontrar uma das seguintes opções:

; i) um livro de inglês e um de espanhol; ou

I

: ii) um livro de inglês e um de francês; ou

I

I

: iii) um livro espanhol e um de francês.
j

: Em cada opção, temos eventos concomitantes (ambos ocorrem), aplicando-se o princípio multiplicativo; i
= enquanto as opções i, ii e iii se excluem mutuamente (somente uma delas irá ocorrer), aplicando-se o i
= princípio aditivo entre elas.

I

;* para i (inglês e espanhol), temos 4 x 3 = 12 possibilidades;
i

:* para ii (inglês e francês), temos 4 x 2 = 8 possibilidades;
i

:* para iii (espanhol e francês), temos 3 x 2 = 6 possibilidades.
i

= E o total de maneiras de pegar dois dicionários de idiomas distintos é (princípio aditivo):
i

12 + 8 + 6 = 26

; Gabarito: C

I

I

I

I

i (CESPE/2013 -TRT-ES) Considerando que, na fruteira da casa de Pedro, haja 10 uvas,
2 maçãs, 3 laranjas, 4 j

= bananas e 1 abacaxi, julgue o próximo item.
;

I

I

i Se Pedro desejar comer apenas um tipo de fruta, a quantidade de maneiras de escolher frutas para comer ;
= será superior a 100.
i i Comentários:
I

I

: Se Pedro deseja comer apenas um tipo de fruta, ele poderá comer uvas OU maçãs OU
laranjas OU bananas =

= OU abacaxi.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I: i) Uvas: há 10 uvas, logo Pedro poderá comer 1, 2, 3, 4, 5, 6, 7, 8, 9 ou 10
uvas. Logo, há 10 maneiras de

I: escolher uvas para comer;

: ii) Maçãs: há 2 maçãs, logo há 2 maneiras de escolher maçãs para comer;

i iii) Laranjas: com 3 laranjas, há 3 maneiras de comer laranjas;

iv) Bananas: com 4 bananas, há 4 maneiras de comer bananas;

= v) Abacaxi: há 1 abacaxi, logo há 1 forma de comer abacaxi.

I

; Como Pedro irá escolher apenas uma dessas opções, então devemos aplicar o princípio aditivo:

Número de maneiras = 10 + 2 + 3 + 4 + 1 = 20

: Que é inferior a 100.

I

j Gabarito: Errado.

I

i (CESPE 2016/FUB) Em um intervalo para descanso, a assistente em administração Marta foi a uma lanchonete cujo cardápio oferecia 7 tipos diferentes de salgados, 4 tipos diferentes de bolos, 3espécies diferentes de tapioca, sucos de 3 sabores diferentes e 5 tipos diferentes de refrigerantes. Apartir dessa

= situação hipotética, julgue o item que se segue.

: Se Marta desejar fazer um lanche com apenas uma opção de comida e apenas uma bebida, ela terá mais de
= 100 maneiras distintas de organizar seu lanche.

I

i Comentários:

: Marta deseja escolher uma comida E uma bebida.

: Para comer, Marta pode escolher uma das 7 opções de salgado OU um dos 4 tipos de bolo OU uma das 3i espécies de tapioca. Pelo princípio aditivo, as opções de comida são:

í 7 + 4 + 3 = 14

I

: Para beber, Marta pode escolher uma das 3 opções de suco OU uma das 5 opções de refrigerante. Pelo
= princípio aditivo, as opções de bebida são:

3 + 5 = 8

i Pelo princípio multiplicativo, o número de maneiras de se escolher uma comida E uma bebida é:

14 x 8 = 112

= Logo, há mais de 100 maneiras.

Ê Gabarito: Certo.

Princípio da Casa dos Pombos

O princípio do pombal ou da casa dos pombos afirma que:

: Se n pombos devem se abrigar em m casas e se n > m, então pelo menos uma casa irá i

= conter mais de um pombo.
i

L

I

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por exemplo, podemos ter m = 4 casas. Nesse caso, se tivermos qualquer número de pombos maior do que
4, então pelo menos uma casa conterá mais de um pombo.

Por que pombos? Bem, os pombos são imprevisíveis. Eles podem resolver ficar todos juntos ou todos separados... Nesse sentido, eles representam eventos aleatórios, como a seleção de determinados elementos ao acaso. Porém, mesmo sendo imprevisíveis, é possível fazer algumas afirmações ou garantias.Para fazer essas afirmações, precisamos pensar no pior cenário possível.

Por exemplo, considerando um total de 4 casas, quantos pombos são necessários para garantir que haverá pelo menos 2 pombos em uma casa? Bem, é possível que, havendo apenas 2 pombos, ambos escolham a mesma casa. Porém, isso não pode ser garantido, pois também é possível que escolham casas distintas. Amesma situação ocorre com 3 e com 4 pombos, pois ainda é possível que todos escolham casas distintas.
Entretanto, com 5 pombos, necessariamente haverá pelo menos 2 pombos em uma casa. Como há somente4 casas, ainda que eles tentem se espalhar, o 5e pombo não terá alternativa e terá que ficar com algum outro pombo.
Também podemos encontrar o número de pombos necessários para garantir que haja pelo menos 3 pombos em uma mesma casa. No pior cenário, eles ficarão todos espalhados com 2 pombos por casa, antes de termos 3 pombos em uma mesma casa.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para que haja 2 pombos em cada uma das 4 casas, serão necessários 2x4 = 8 pombos.
Portanto, são necessários 8 + 1 = 9 pombos, para garantir que haverá pelo menos 3 pombos em uma casa.
Podemos mencionar outros exemplos, mais próximos à nossa realidade. Por exemplo, qual é o menor número de pessoas necessário para garantir que pelo menos 2 pessoas façam aniversário no mesmo mês?
Para garantir isso, precisamos pensar no pior cenário: aquele que em que os aniversariantes ficam todos"espalhados".

Assim, em um grupo de 12 pessoas, todas fariam aniversário em meses distintos. Porém,
em um grupo de
13 pessoas, como há somente 12 meses, então necessariamente alguém fará aniversário no mesmo mês que outra pessoa. Portanto, são necessárias 13 pessoas para garantir que pelo menos 2façam aniversário no mesmo mês.
a*»

II

Janeiro

*

T

Julho

*

IHI

Fevereiro f
Agosto

TII

Março

*

II

Setembro

TII

Abril

*

DII

Outubro

*

HII

Maio

*

nII

Novembro

TII

Junho

*

IIII

Dezembro

Por que a pergunta é pelo menor número de pessoas?

Note que, se houver mais do que 13 pessoas (ou seja, 14, 15,...), também poderemos garantir que pelo menos 2 pessoas farão aniversário no mesmo mês. Por isso, a questão se interessa pelo menor número de pessoas, para o qual temos a garantia desejada.
I«** IX

i (FCC/2017 - Analista Executivo da Secretaria de Gestão/MA) No setor administrativo de uma empresa, há
= quatro tipos de cargos: estagiários, técnicos, gerentes e diretores. Alguns funcionários desse setor comporão
= um grupo que será transferido para o setor financeiro da empresa. Compondo-se o grupo com funcionários
; escolhidos ao acaso, o número mínimo de funcionários que deverá compor o grupo para que se tenha certeza
= de que nele haverá quatro funcionários de um mesmo cargo é igual a

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 17

b) 15

c) 13

d) 16

e) 14

Comentários:

O pior cenário (ou seja, o cenário que exige o maior número de funcionários para garantir que 4 terão o mesmo cargo) é aquele em que os funcionários são todos de cargos diferentes. Assim,haverá 3 funcionários para cada um dos 4 tipos de cargo, antes de haver 4 funcionários de algum cargo.
Ou seja, haverá 3 x 4 = 12 funcionários distribuídos por todos os cargos, em 3
funcionários por cargo. Com o
13Q funcionário, necessariamente haverá 4 funcionários para algum cargo.

Gabarito: C

(CESPE/2013-TCE-RO) Considerando que, em uma pesquisa de rua, cada entrevistado responda sim ou não a cada uma de dez perguntas feitas pelos entrevistadores, julgue o item seguinte.
Será necessário entrevistar mais de mil pessoas para se garantir que duas pessoas respondam igualmente a todas as perguntas.
Comentários:

Para garantir que duas pessoas respondam igualmente a todas as perguntas, é necessário entrevistar um número de pessoas maior que o número de maneiras diferentes de responder ao questionário. Ou seja, essa questão combina o princípio dos pombos com o princípio multiplicativo.
Vamos representar as possibilidades de resposta para as 10 perguntas conforme abaixo:

Sabemos que há 2 respostas distintas possíveis para cada pergunta:

2 2 2 2 2 2 2 2 2 2

Pelo princípio multiplicativo, o número de maneiras distintas de responder às 10 perguntas é:

2x2x2x2x2x2x2x2x2x2 = 210 = 1024

Assim, precisamos entrevistar 1.025 pessoas para garantir que haverá pelo menos duas respostas iguais, ou seja, mais de 1.000 pessoas.
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

FAToRIAL DE UM NÚMERo NATURAL

Para resolvermos diversas questões de análise combinatória, utilizamos o chamado fatorial.

O fatorial de um número natural (0,1, 2, 3,...) é representado como:

n!

TOME

NOTA!

O fatorial representa o produto de todos os números inteiros positivos menores ou iguais àquele número, conforme indicado a seguir:
n! = n x (n — 1) x (n — 2) x ... x 2 x 1

Por exemplo:

21 = 2x1 = 2

3! = 3x2xl = 6

41=4x3x2x1 = 24

51 = 5x4x3x2x1 = 120

61 = 6x5x4x3x2x1 = 720

Note que podemos escrever o fatorial de um número natural em função do fatorial de qualquer outro número natural menor, por exemplo:
4! = 4 x 3x2x1 = 4x3!

3!

7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 7x6!

6!

7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 7x6x5!

5!

101 = 10x9x8Ix7x6x5x4x3x2x1 = 1I0x9x8x7x6!

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Esse tipo de mudança facilita o cálculo das divisões entre fatoriais (muito comuns em combinatória):
6! 6 x 5 x 4 x 3! 6x5 x4x3!/

3! 3!

= 6x5x4 = 120

10! 10 x 9 x 8 x 7!

7! 7!

15!

13!

10 x 9 x 8 x X

7K

z = 10 x 9 x 8 = 720

Nesses casos, aplicamos o fatorial antes de efetuar a divisão. Quando for necessário realizar a divisão antes, utilizaremos o parêntesis. Por exemplo:
Em —, calculamos os fatoriais antes: — = 6x5x4x3' = 6x5x4 = 120; já em f-)!,efetuamos a divisão entre parêntesis, antes do fatorial:

(|)l = 2! = 2xl = 2
Analogamente, em um produto, temos: 2 x 4! + (2 x 4)!

Em 2 x 4!, calculamos o fatorial de 4 antes da multiplicação:

2x41 = 2x4x3x2x1 = 48

Em (2 x 4) I, multiplicamos os fatores, antes de aplicar o fatorial:
(2 x4)! = 8! = 8 x 7 x 6x 5x4 x3 x 2 x 1 = 40.320

O mesmo vale para as demais operações:

2 + 4! + (2 + 4)!

Pois 2 + 4! = 2 + 4x3x2 xl = 26;e(2 + 4)! = 6! = 6x 5x 4 x3 x 2 x 1 = 720.

8-3! + (8-3)!

Pois 8-3! = 8-3 x 2 x 1 = 2; e (8 — 3)! = 5! = 5x4x3 x 2 x 1 = 120.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, vejamos dois casos especiais do fatorial. O fatorial de 1 pode ser entendido pela própria definição de fatorial. Como não há número inteiro positivo menor do que 1, apenas igual, então esse será o único fator:
1! = 1

O segundo caso especial é 0! Você pode considerar que o seguinte resultado é uma convenção:

0! = 1

KDOMMS
FUNDO!

Zl

Para entender o porquê dos resultados desses casos especiais, devemos observar que o fatorial de um número n pode ser escrito como o fatorial do número seguinte, (n +1)!,
dividido por esse número seguinte, n + 1.

Por exemplo, 4! pode ser representado como 5! dividido por 5.

S!=2«1«X2X1 =

5 ?

Similarmente, o fatorial de 1 pode ser representado como:

II — — — 2x1 _

' — 2 — 2 —

E o fatorial de 0 como:

i i l«** IX
i (2019 - Prefeitura de Jacutinga/MG) O fatorial de um número é extremamente utilizado na análise i
= combinatória. Dessa forma, analise as proposições a seguir:
;
i I. O fatorial n! de um número n G N é dado por n! = n x (n - 1) x (n - 2)... 3 x 2 x 1;

; II. 0! = 1;
j j III. 1! = 0.j

: Está(ão) CORRETA(S) a(s) proposição(ões):
j

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) II apenas.

b) I e II apenas.

c) II e III apenas.

d) I e III apenas.

Comentários:

A proposição I corresponde exatamente à definição de fatorial: n! = n x (n - 1) x (n - 2)... 3 x 2
x 1
A proposição II também está correta, pois 0! = 1.

A proposição III está incorreta, pois 1! = 1.

Ou seja, estão corretas apenas as proposições I e II.

Gabarito: B

(2018 - Prefeitura de Uruçuí/PI) A simplificação da expressão a seguir é:
a) 200

b) 198!

c) 38.800

d) 39.800

Comentários:

Podemos escrever 200! como 200! = 200 x 199 x 198!. Assim, temos:

200! 200 x 199 x 198!

=-----------— = 200 x 199 = 39.800

198! '

Gabarito: D

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

PERMUTAçÃo

Informalmente, podemos dizer que permutar significa trocar de lugar.

Ao trocar elementos de lugar, a ordem desses elementos se modifica. Por isso, podemos dizer que as técnicas de permutação permitem calcular as diferentes possibilidades de se ordenar elementos.
Permutação Simples

Na permutação simples, os elementos a serem ordenados são todos distintos entre si.

Digamos que 3 alunos (Ana, Beto e Caio), de um grupo de estudo, serão avaliados e,
em seguida, ranqueados de acordo com o resultado da sua avaliação. Supondo que não há empates, de quantas formas esses alunos podem ser ranqueados?
Como o exemplo é pequeno poderíamos relacionar e contar todas as possibilidades, mas vamos experimentar uma outra forma de resolver: encontrando o número de possibilidades para cada posição:
ie 22 32

Quais são os alunos que podem ficar em primeiro lugar? Qualquer um deles (Ana, Beto ou Caio) pode ficar em primeiro lugar. Portanto, temos 3 possibilidades para 0 primeiro lugar.
E para 0 segundo lugar? Bem, sabendo que alguém ficará em primeiro lugar, restarão 2
possibilidades para
0 segundo colocado.

E para 0 terceiro lugar, sabendo que alguém ficará em primeiro lugar e outro ficará em segundo lugar, restará apenas uma possibilidade para 0 terceiro lugar.
3 2 1

12 22 32

Como são eventos concomitantes, pois alguém ficará em primeiro lugar, outra pessoa ficará em segundo E
outra em terceiro, devemos multiplicar as possibilidades de cada evento, pelo princípio multiplicativo:
3x2x1

Poderíamos ter começado 0 raciocínio por qualquer posição, que 0 resultado seria 0 mesmo.

Como assim "sobrarão" 2 possibilidades para 0 2g colocado e 1 possibilidade para 0 3- colocado?

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vh-

F ES(CLARECENDO!

Para a 1? posição, todos os 3 alunos estão disponíveis:

Para cada uma dessas 3 possibilidades, teremos ordenações diferentes, dependendo do 25
e 3Q lugares. Por exemplo, mantendo Ana em 15 lugar, temos Ana, Beto e Caio ou Ana,
Caio e Beto.
Sabendo que não é possível que o mesmo aluno ocupe mais de uma posição, então há apenas 2 possibilidades para a 25 posição, uma vez que um dos alunos terá ocupado a 15.
Por isso, dizemos que o aluno da 15 posição "já foi escolhido" e assim sobrarão apenas 2alunos para a 25 posição:

3 2

1° 2? 35

Da mesma forma, só haverá 1 aluno que não terá ocupado nem a primeira nem a segunda posição, logo ele irá ocupar a terceira posição. Por isso, dizemos que, "após a escolha" do15 e do 25 colocados, sobrará apenas 1 aluno para a 35 posição:

3 2 1

15 25 35

Por fim, multiplicamos todas essas possibilidades (princípio multiplicativo) para encontrar a quantidade de maneiras de ordenar todos os 3 elementos.
E se houvesse 4 alunos? Quais seriam as possibilidades de ordenação? Nesse caso,
teríamos 4 possibilidades para 0 primeiro lugar; 3 para 0 segundo lugar; 2 para 0 terceiro e 1 para 0 quarto:
4 x 3 x 2 x 1

E para 10 alunos? Teríamos 10 possibilidades para 0 primeiro lugar, 9 para 0 segundo,
depois 8, depois 7...
até sobrar 1 possibilidade para 0 décimo lugar:

10x9x8x7x6x5x4x3x2x1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, a posição seguinte terá sempre uma possibilidade a menos do que a posição anterior.
Para n alunos, temos:

n x (n - 1) x (n - 2) x ... x 3 x 2 x 1
Lembrou de algo? Essa é a fórmula do fatorial!

Portanto, a permutação simples de n elementos distintos, que representamos como Pn,

que corresponde ao número de possibilidades de ordenar n elementos distintos, é:

Pn = n!

Reforçando, a permutação simples pode ser utilizada para calcular todas as possibilidades de se reordenar elementos, sejam letras de uma sigla (formando anagramas distintos), algarismos em um número (formando números distintos), etc., desde que os elementos sejam todos distintos.
I«** IX

r f í (FGV/2019 - Prefeitura de Salvador/BA) Trocando-se a ordem das letras da sigla PMSde todas as maneiras :
possíveis, obtêm-se os anagramas dessa sigla. O número desses anagramas é:
i j a) 16.j b) 12.
j c) 9.
j d) 8.
i e) 6.

i

I

i Comentários:

I

i Considerando que todas as 3 letras de PMS são distintas, o número de anagramas, ou seja, de formas de se i
= reordenar essas letras é a permutação de 3 elementos:

P₃ = 31 = 3x2x1 = 6

: Gabarito: E

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= (VUNESP/2018 - PM/SP) Em um armário, há 5 prateleiras e será preciso colocar 5
caixas, de cores distintas, =I

; cada uma em uma prateleira desse armário, sem que haja uma ordem específica. O
número total de maneiras ;

de colocar essas caixas nesse armário é j a) 25.j b) 60.:

; c) 95.
;

d) 120.

i e) 165.

I

i Comentários:

I

i Por se tratar de caixas distintas, a serem alocadas em determinada ordem, temos uma permutação de 5 i
: elementos:

i Gabarito: D.

P₅ = 51 = 5x4x3x2x1 = 120

i (CESPE 2018/EBSERH) Julgue o próximo item, a respeito de contagem.

I

: Se a enfermaria de um hospital possuir cinco leitos desocupados e se cinco pacientes forem ocupar esses i leitos, então haverá mais de 100 formas diferentes de fazer essa ocupação.

i Comentários:

I

I

: Considerando que temos 5 leitos para serem ocupados por 5 pacientes,
temos uma permutação de 5 i

: elementos:

P₅ = 51 = 5x4x3x2x1 = 120

= Logo, há mais de 100 formas de fazer essa ocupação.
i

I

Ê Gabarito: Certo.

I

I

I

I

i (CESPE 2016/CBM-DF) Para atender uma grave ocorrência, o comando do corpo de bombeiros acionou 15
i homens: 3 bombeiros militares condutores de viatura e 12 praças combatentes, que se deslocaram em três i
= viaturas: um caminhão e duas caminhonetes. Cada veículo transporta até 5 pessoas, todas sentadas,
;

= incluindo o motorista, e somente os condutores de viatura podem dirigir uma viatura. Com relação a essa i j situação, julgue o item seguinte.;

A quantidade de maneiras distintas de se distribuir os condutores de viatura para dirigir os veículos é superior =
j a 5.

I

I

i Comentários:

I

: Considerando que há 3 condutores para 3 veículos, a quantidade de maneiras de organizá-los corresponde i i a uma permutação de 3 elementos:i

P₃ = 31 = 3x2x1 = 6

: Logo, a quantidade de maneiras é superior a 5.
j

: Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Permutação Simples com Restrição

É possível que algumas questões de permutações imponham determinadas restrições. Nesses casos, nem todos os elementos poderão permutar livremente, o que exige mais atenção para resolver a questão.
Por exemplo, vamos considerar que há 8 elementos distintos a serem ordenados, por exemplo, os algarismos
{1, 2, 3, 4, 5, 6, 7, 8}. Vamos representar as opções de ordenação com os espaços abaixo.

Suponha que o número 1 esteja fixo na primeira posição e o número 8, na oitava posição:

1 8

Sendo assim, restarão os algarismos 2 a 7 (ou seja, um total de 6 algarismos) para serem ordenados nos 6espaços restantes. Dessa forma, teremos uma permutação de 6 elementos em 6 posições:

P₆ = 6! = 6x5x4x3x2x1 = 720

Poderíamos ter fixado quaisquer 2 algarismos em quaisquer 2 posições, que continuaríamos com a permutação dos 6 algarismos restantes, nos 6 espaços restantes. Portanto, o número de possibilidades de ordená-los seria o mesmo.
De modo geral, havendo n elementos, dos quais p estejam fixos em determinadas posições, fazemos a permutação de n - p elementos:
Pn-p = (n-p)l

Um exemplo sutilmente diferente seria se esses dois algarismos fossem posicionados nos extremos, mas sem fixar qual irá ocupar a primeira posição e qual irá ocupar a última posição.
Assim, poderíamos ter o número 1 na primeira posição e o número 8 na oitava; ou o número 8 na primeira posição e o número 1 na oitava:
1 8

8 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nesse caso, para cada uma das 720 possibilidades de permutar os algarismos de 2 a 7 nas posições intermediárias, calculadas anteriormente, há 2 possibilidades distintas de posicionar os extremos.
Pelo princípio multiplicativo, devemos multiplicar as possibilidades desses dois eventos:

2 x P₆ = 2 x 720 = 1440

Na verdade, essas 2 possibilidades de alocar esses 2 algarismos, 1 e 8,
nas 2 posições extremas correspondem à permutação desses 2 elementos.
Assim, podemos representar o número de maneiras de se ordenar os 8 algarismos, nessas condições,
como:

P2X P6

Em outras palavras, podemos tratar como duas permutações em separado: uma com os 2
elementos que ocuparão as posições extremas; e a outra com os 6 elementos que ocuparão as posições não extremas.
E para ordenar todos os 8 elementos, multiplicamos esses resultados (princípio multiplicativo).

Com isso, podemos resolver outros problemas que indiquem determinadas posições a certos elementos,
sem fixar a posição específica de cada um.

Por exemplo, vamos supor que os 3 primeiros algarismos tenham que ocupar as 3
primeiras posições, em qualquer ordem; e os demais algarismos, as demais posições, também em qualquer ordem:
Y V

1, 2 e 3 4, 5, 6, 7 e 8

Nesse caso, temos a permutação de 3 elementos nas 3 primeiras posições e de 5
elementos nas demais posições.
Pelo princípio multiplicativo, 0 número de ordenações possíveis é:

P3X Ps = 3! x 51 = 3x2x1x5x4x3x2x1 = 720

Agora, vamos supor que os algarismos ímpares tenham que ocupar posições ímpares e os algarismos pares,posições pares, como ilustrado abaixo:

I p 1 p 1 p 1 p

Também vamos resolver esse caso com 2 permutações em separado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação aos ímpares, temos 4 algarismos para 4 posições, logo, temos uma permutação de 4
elementos:

P₄ = 41=4x3x2x1 = 24

Em relação aos pares, temos 4 algarismos para 4 posições, logo, temos outra permutação de 4
elementos:
P₄ = 41=4x3x2x1 = 24

Pelo princípio multiplicativo, o número de maneiras de ordenar todos esses 8 algarismos é:

24 x 24 = 576

Em geral, havendo n elementos, dos quais p estejam designados a determinadas posições,
mas sem fixar a posição específica de cada um, fazemos a permutação de n - p elementos e multiplicamos pela permutação de p elementos:
Pn-pxPp=(n-p)!xp!

I«** IX

i (FCC/2019 - Analista Judiciário do TRF 3- Região) Em um concurso com 5 vagas, os candidatos aprovados i
= serão alocados, cada um, em um dos municípios A, B, C, D ou E. O primeiro colocado foi designado para o i i município A. O número de possíveis alocações dos outros candidatos aprovados é i i a) 30
b) 4
j j c) 120
d) 24
;

j e) 6
j i Comentários:

: Essa questão trabalha com a permutação de 5 elementos, com um deles fixo.
i

I

: Considerando que 1 dos candidatos está fixo no município A, restam 4 candidatos para serem alocados em ;
= 4 municípios (B, C, D ou E). Portanto:

P₄ = 4! =4x3x2x1 = 24

I

I

: Gabarito: D.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(CESPE 2018/BNB) Em um navio, serão transportados 10 animais, todos de espécies diferentes. Antes de serem colocados no navio, os animais deverão ser organizados em uma fila. Entre esses10 animais, há um camelo, um elefante e um leão. A respeito da organização dessa fila, julgue o item subsequente.
Existem 8! maneiras distintas de organizar essa fila de forma que o camelo fique na primeira posição e o elefante fique na sexta posição.
Comentários:

A questão pede para organizarmos uma fila de 10 animais, de forma que o camelo (C)
fique na primeira posição e o elefante (E), na sexta:
c E

Como esses elementos estão fixos em posições específicas, basta reordenarmos os demais elementos.

Logo, o número de maneira de organizarmos essa fila corresponde à permutação de 10 - 2 = 8
elementos:

Ps = 8!

Gabarito: Certo.

(CESPE 2018/BNB) Em um navio, serão transportados 10 animais, todos de espécies diferentes. Antes de serem colocados no navio, os animais deverão ser organizados em uma fila. Entre esses10 animais, há um camelo, um elefante e um leão.
A respeito da organização dessa fila, julgue o item subsequente.

Existem 3x7! maneiras distintas de organizar essa fila de forma que o elefante, o camelo e o leão fiquem nas três primeiras posições, não necessariamente nessa ordem.
Comentários:

Agora, desejamos organizar a fila de forma que os 3 animais (Elefante, Camelo e Leão)
fiquem nas 3 primeiras posições, em qualquer ordem. Consequentemente, os outros 10 - 3 = 7 animais ocuparão as outras 7posições, em qualquer ordem:

- #/

Elefante, Camelo, Leão Outros 7 animais

O número de formas de organizar os 3 animais corresponde a uma permutação de 3 elementos:

P3 = 3!

O número de formas de organizar os outros 7 animais equivale a uma permutação de 7 elementos:

P7 = 7!

Pelo princípio multiplicativo, multiplicamos esses resultados para obter o número de maneiras possíveis de organizar toda a fila:
Número de possibilidades = 3! x 7!

Esse resultado é diferente do valor informado no item, qual seja, 3 x 7!, logo, o item está errado. Aliás, como3! = 3 x 2, o nosso resultado é o dobro do que consta no item da questão.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vejamos mais uma ferramenta para resolver problemas de permutação simples com restrição.

Vamos supor que os algarismos 1 e 2 tenham que ficar sempre juntos, nessa ordem.

Nesse caso, tratamos esses 2 algarismos como elemento único, que podemos chamar de A.
Assim, em vez de 8 elementos {1, 2, 3, 4, 5, 6, 7 e 8}, ordenaremos apenas 7 elementos {A, 3, 4, 5, 6, 7 e 8}:
P₇ = 71 = 7x6x5x4x3x2x1 = 5.040

Portanto, a quantidade de maneiras de ordenar 8 elementos, de modo que 2 estejam sempre juntos em uma determinada ordem, corresponde à permutação de 7 elementos.
Se houvesse 3 elementos juntos em determinada ordem, {1, 2 e 3}, chamaríamos os 3
elementos de A, e calcularíamos a permutação dos outros 5 elementos acrescido do elemento A, o que corresponde à permutação de 6 elementos {A, 4, 5, 6, 7 e 8}.
De modo geral, havendo n elementos, dos quais j devam ficar juntos em determinada ordem, fazemos a permutação de n - j + 1 elementos:
Pn-j+l = (n-j+ 1)1

E se os elementos tivessem que ficar juntos, mas em qualquer ordem?

Nesse caso, o início da solução é similar, isto é, chamamos esses elementos de um único elemento, A, e fazemos a permutação do elemento A com os demais elementos.
Por exemplo, se os algarismos {1, 2 e 3} tivessem que ficar juntos, mas em qualquer ordem, dentre os 8algarismos, faríamos a permutação dos 6 elementos {A, 4, 5, 6, 7 e 8}:

P₆ = 6! = 6x5x4x3x2x1 = 720

Porém, para cada uma dessas 720 possibilidades de ordenar os elementos {A, 4, 5, 6,
7 e 8}, os algarismos

{1, 2 e 3} pode aparecer como:

... 1 2 3 ... ... 1 3 2 ...
... 2 1 3 ...

... 2 3 1... ... 3 1 2 ...
... 3 2 1...

Em outras palavras, para cada uma das possibilidades que calculamos anteriormente, temos diferentes formas de ordenar os 3 elementos.
Como calculamos as diferentes formas de ordenar 3 elementos? Pela permutação de 3 elementos!

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Logo, para calcular o número de maneiras de organizar todos os 8 elementos nessas condições, devemos multiplicar o resultado anterior pela permutação de 3 elementos (princípio multiplicativo):
P6x P3 = 6! x 3! = 720 x 6 = 4320

De modo geral, havendo n elementos, dos quais j elementos devem ficar juntos em qualquer ordem, fazemos a permutação de n - j + 1 elementos e multiplicamos pela permutação de j elementos:
Pn-j+ix Pj= (n-j + 1)! x j!

Na permutação simples com restrição, podemos (i) designar posições para determinados elementos ou (ii) determinar elementos a permanecerem juntos.
i) Quando designamos posições, devemos permutar os demais elementos.

i.a) Havendo p elementos fixos em determinadas posições, dentre n elementos no total,
devemos permutar n - p elementos:

Pn-p = (n-p)l i. b) Caso os p elementos possam ser reordenados dentre as posições designadas, devemos multiplicar o resultado anterior pela permutação de p elementos:
Pn-pX Pp = (n -p)! X p!

ii) Quando determinamos elementos devem permanecer juntos, devemos considerá-los como elementos único e permutar esse novo elemento junto aos demais.
ii. a) Havendo j elementos que deverão permanecer juntos em determinada ordem, dentre n elementos no total, devemos permutar os demais n - j elementos acrescidos de 1unidade, a qual corresponde ao conjunto dos j elementos:

Pn-j+1 = (n-j + 1)!

i.b) Se os j elementos, que deverão permanecer juntos, puderem ser reordenados entre si,devemos multiplicar o resultado anterior pela permutação de j elementos:

Pn-j+ix Pj = (n-j + 1)1 xj!

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (FGV/2017 - Prefeitura de Salvador/BA) Três casais vão ocupar seis cadeiras consecutivas de uma fila do i
= cinema, e os casais não querem sentar separados. Assinale a opção que indica o número de maneiras
;

diferentes em que esses três casais podem ocupar as seis cadeiras.
i i a) 6.
b) 12.

i c) 24.
j d) 36.
; e) 48.

I

i Comentários:

I

; Primeiro, vamos tratar cada casal como elemento único. Assim, temos a permutação de 3 elementos:

P₃ = 31 = 3x2x1 = 6

= Uma vez definida a ordem entre os casais, é necessário que cada casal decida a sua ordem.
i

: Assim, para cada uma dessas 6 possibilidades de ordem entre os casais, há P₂ = 2 possibilidades de cada um ;dos três casais se organizarem:

: 6x2x2x2=48
=

I

I

; Gabarito: E

I

I

I

I

i (CESPE 2018/BNB) Em um navio, serão transportados 10 animais, todos de espécies diferentes. Antes de i
; serem colocados no navio, os animais deverão ser organizados em uma fila. Entre esses 10 animais, há um =
; camelo, um elefante e um leão.
i

I

A respeito da organizaçãodessa fila, julgue o item subsequente.
i

I

: Existem 7x7! maneiras distintas de organizar essa fila de forma que o elefante, o camelo e o leão estejam ;
= sempre juntos, mantendo-se a seguinte ordem: leão na frente do camelo e camelo na frente do elefante. i

I

i Comentários:

= Para organizar uma fila de 10 animais, de modo que o leão, o camelo e o elefante apareçam sempre nessa j
= ordem, podemos tratá-lo como elemento único.
i

I

: Assim, o número de formas de organizar os outros 10 - 3 = 7 animais e mais esse trio corresponde a uma i
= permutação de 8 elementos:

P₈ = 8! = 8 x 7!

= Esse resultado é diferente de 7 x 7!, descrito no item.
i

I

: Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= (CESPE 2018/BNB) Julgue o próximo item, relativo a análise combinatória e probabilidade.

A quantidade de números naturais distintos, de cinco algarismos, que se pode formar com os algarismos 1, ;
= 2, 3, 4 e 5, de modo que 1 e 2 fiquem sempre juntos e em qualquer ordem, é inferior a 25.

I

i Comentários:

A quantidade de números que podem ser formados com os algarismos 1, 2, 3, 4 e 5
corresponde a uma j i permutação desses elementos. Para que os números 1 e 2 fiquem sempre juntos,podemos considerá-lo com i

; elemento único. Assim, temos uma permutação de 4 elementos:
i

P₄ = 4! = 4x3x2xl = 24

= Porém, para cada uma dessas 24 maneiras de organizar os algarismos 3, 4, 5 e o elemento 1-2,
podemos ter

1 primeiro e depois 2, ou 2 primeiro e depois 1. Logo, pelo princípio multiplicativo,
devemos multiplicar esse i i resultado pela permutação de 2 elementos P₂ = 2! = 2:;

: Quantidade de números possíveis = 24 x 2 =
48 i j Essa quantidade é superior a 25.i

; Gabarito: Errado.

............................................................... .............. a

Permutação com Repetição

Na permutação simples, todos os elementos são distintos.

Por exemplo, se houver 3 elementos {A, B, C}, há P3 = 3! = 3 x 2 x 1 = 6 possibilidades de ordená-los. São elas:i)ABC ii)ACB iii) B A C iv)BCA v)CAB vi) C B A

Agora, vamos supor que, em vez C, haja um segundo elemento A. Vamos escrever novamente as 6possibilidades descritas acima, porém substituindo C por um segundo A:

l)ABA II) A A B III) BAA IV) B A A V) A A B VI) ABA

Agora, a ordem descrita em I é igual à ordem em VI; a ordem em II é igual à ordem em V; e a ordem em III é igual à ordem em IV. Portanto, temos apenas 3 possibilidades distintas de ordenar os elementos {A,A, B}:

I) A B A II) A A B III) B A A

Ou seja, quando há elementos repetidos, 0 número de possibilidades distintas de ordenação diminui.

Mas, por quê? O que aconteceu?

Bem, a redução ocorreu porque na opção i da primeira permutação, os elementos A e C
estavam invertidos em relação à opção vi, enquanto todo o restante se manteve igual. Por isso, na segunda permutação, essas opções se tornaram uma única opção. O mesmo ocorreu com as opções ii e v; e com as opções iii e iv.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em outras palavras, precisamos dividir o resultado da primeira permutação pelo número de vezes em que Ae C trocam de posição.

E como calculamos a quantidade de maneiras em que elementos trocam de posição? Pela permutação!

Portanto, na permutação com repetição, dividimos a permutação simples pela permutação dos elementos repetidos. Indicamos essa permutação de 3 elementos com repetição de 2 elementos por P3:
, 3! 3x2! 3X/2!
Po = — = — = = ó = 3

3 P2 2! 2! /

Assim, se tivéssemos 5 elementos distintos para permutar, teríamos Ps = 51. Havendo 3
elementos iguais,

dentre esses 5, dividimos esse resultado pela permutação dos 3 elementos P3 = 3!:

p3 _ _

5! 5x4x3! 5x4x3!

Ps~p3~

= — =------ -- ----- = = 5 x 4 = 20

3! 3!

E se além de um elemento repetido, tivéssemos outro elemento repetido? Por exemplo, {A, A, B, B, B,
C, D}.

Vamos pensar em etapas: primeiro calculamos a permutação simples dos 7
elementos, como se fossem distintos: P7 = 7!. Em seguida, consideramos que 0 elemento A está repetido 2 vezes e dividimos pela permutação de 2 elementos: P2 = 2!. Por fim, consideramos que 0 elemento B está repetido 3 vezes e dividimos novamente pela permutação de 3 elementos: P3 = 3!:
p2.3 = P7

7 P2 X P3

7!

2! x 3!

7x6x5x4x3!

2x3! 7x3x5x4 = 420

Ou seja, na permutação com mais de um elemento repetido, dividimos a permutação simples pelas permutações dos elementos repetidos.
De modo geral, sendo n elementos totais, com mlfm₂, elementos distintos repetidos, a permutação desses elementos é dada por:
n!

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

(VUNESP/2019 - Prefeitura de Cerquilho/SP) Com as letras, A, B e C, é possível fazer seis agrupamentos diferentes de três letras: ABC, ACB, BAC, BCA, CAB, CBA. Se as três letras fossem A,A e B, só poderiam ser feitos três desses agrupamentos diferentes: AAB, ABA, BAA. Com as letras F, F, G eG, o número de agrupamentos diferentes de quatro letras é a) 6.
b) 8.

c) 10.

d) 12.

e) 16.

Comentários:

A quantidade de agrupamentos com as letras F, F, G e G corresponde à permutação de
4 elementos, com 2
repetições de F e 2 repetições de G:

,, 4! 4x3x2! 4x3

P ' = = = 6

4 2! x 2! 2! x 2! 2

Gabarito: A.

(FGV/2018-ALE-RO) Assinale a opção que indica o número de permutações das letras da palavra SUSSURRO
a) 1680

b) 1560

c) 1440

d) 1320

e) 1260

Comentários:

A palavra SUSSURRO contém 8 letras, sendo o S repetido 3 vezes, o U repetido 2 vezes e o R repetido
2 vezes.
Assim, temos a permutação de 8 elementos com repetição de 2, 2 e 3 elementos:

Gabarito: A

p2,2,3

r8 "

8!

2! x 2! x 3!

8x7x6x5x4x31

2x2x3! = 8x7x6x5 = 1680

(FCC/2015 - Professor da Secretaria de Educação/ES) O número de anagramas que podem ser obtidos utilizando as letras da palavra VITÓRIA, e que terminam com uma consoante é igual a
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

í a)2520

i b) 1080
; c) 840
d)5040

í e)1980

i Comentários:

i Na palavra VITÓRIA, há 7 letras:

1 2 3 4 5 6

i) Para terminar com uma consoante, há 3 possibilidades para essa posição, todas distintas:
i

I

I

1 2 3 4 5 6

= ii) As outras 6 letras podem permutar livremente pelas 6 posições restantes. Considerando que dessas i i 6, há 2 elementos repetidos (letra I), temos:i í ,6!í

: Pl = — = 6 x 5 x 4 x 3 = 360
;

:
:

= Pelo princípio multiplicativo, o número de possibilidades, no total, é:

3 x 360 = 1080

I

I

; Gabarito: B.

L.

Permutação Circular

Na permutação circular, considera-se que os elementos estão dispostos em um círculo.

No círculo, considera-se que não há posições fixas (primeiro lugar, segundo,
terceiro, ..., ou tampouco referências como acima, abaixo, à direita ou à esquerda).
A figura a seguir representa a mesma disposição daquela indicada na figura acima, como se tivéssemos girado o círculo 180Q, mantendo todos os elementos na mesma posição:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A disposição varia somente com a mudança da posição de algum elemento em relação aos demais. A figura abaixo representa uma disposição diferente, haja vista a troca dos elementos 2 e 3.
Para calcular a quantidade de disposições distintas, podemos fixar (qualquer)
um dos elementos, por exemplo, o elemento 1, em qualquer posição:
Agora sim, as posições de todos os outros elementos irão importar porque elas serão relativas ao elemento1 fixado. Portanto, calculamos a permutação simples para os demais elementos (no caso, os 7):

P₇ = 7! = 7x6x5x4x3x2xl = 5.040

Em geral, como fixamos um dos elementos, a permutação circular de n elementos,
indicada por PCn, é:

PCn = (n-1)!

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Permutação Circular com Restrições

É possível que uma permutação circular apresente restrições.

Por exemplo, suponha que haja 4 meninos (O) e 4 meninas (A) para se sentarem a uma mesa circular, de forma que todo menino esteja entre duas meninas (e, portanto, toda menina esteja entre dois meninos),como indicado abaixo.

Nesse tipo de situação, resolvemos o problema em 2 etapas: primeiro sentamos os meninos e, depois, as meninas (ou vice-versa). Para sentarmos os 4 meninos, há 4 posições possíveis:
Nessa primeira etapa, temos uma permutação circular, em que fixamos a posição de um deles e calculamos a permutação dos demais:
PCn = (n-l)!

PC₄ = 3! = 3 x 2 x 1 = 6

Na segunda etapa, vamos sentar as 4 meninas. Nesse caso, todas as posições são diferentes, pois já temos meninos sentados, de modo que a posição de todas as meninas importa.
Assim, temos a permutação simples de 4 elementos:

P₄ = 4! = 4x3x2x1 = 24

Portanto, para cada uma das 6 possibilidades de se posicionar os meninos, há 24
possibilidades de posicionar as meninas. Pelo princípio multiplicativo, devemos multiplicar as possibilidades desses eventos:
6 x 24 = 144

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

(2019 - Prefeitura de Ibiaçá/RS) O número máximo de maneiras distintas que um grupo de cinco amigos pode se sentar ao redor de uma mesa circular para realizar um lanche coletivo é:
a) 120

b) 50

c) 24

d) 12

e) l

Comentários:

A permutação circular de n = 5 elementos é dada por:

PCn = (n-1)!

PC₅ = 4! = 4 x 3 x 2 x 1 = 24

Gabarito: C

(2016 - Prefeitura de Ouricuri/PE) De quantas maneiras possíveis podemos dispor nove crianças em um círculo em que todas brincam de mãos dadas?
a) 9!

b) 8!

c) 7!

d) 6!

e) 5!

Comentários:

A permutação circular de n = 9 elementos é dada por:

PCn = (n — 1)1
PC9 = 8!

Gabarito: B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Bruno, Carlos, Davi, Eduardo e Flávio são amigos e jantam em uma churrascaria. Na mesa circular em que se encontram, há 5 cadeiras idênticas, equidistantes duas a duas, e 5 espaços entre cada par de cadeiras para os garçons servirem carnes: acém; costela; fraldinha; linguiça; e maminha. A figura acima ilustra uma possível configuração da mesa, com os 5 amigos e as 5 carnes do rodízio. Sabe-se que as carnes preferidas de Bruno são costela e acém e Davi prefere fraldinha.
Com base nessa situação hipotética, julgue o item a seguir.

O número possível de configurações da mesa, contando que os 5 amigos estejam sentados e as 5 carnes estejam entre cada par de cadeiras, é maior que 3.000.
Comentários:

Vamos resolver essa questão em 2 etapas. Primeiro, sentamos os 5 amigos e, em seguida, colocamos as 5carnes (ou vice-versa).

Para sentar os 5 amigos em uma mesa redonda, podemos sentar um amigo em qualquer posição e, em seguida, permutar os demais:
PC₅ = 4! = 4 x 3 x 2 x 1 = 24

Ao colocarmos as 5 carnes, a posição de todas elas importam, pois elas estarão entre amigos distintos.Portanto, temos a permutação simples de 5 elementos:

P₅ = 51 = 5x4x3x2x1 = 120

Portanto, para cada 24 possibilidades de sentar os amigos, há 120 possibilidades de colocar as carnes. Pelo princípio multiplicativo, as possibilidades desses eventos devem ser multiplicadas:
24 x 120 = 2.880

Como 2.880 é menor que 3.000, o item está errado.

Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

OUTRoS TIPoS DE PERMUTAçÃo

Nesta seção, veremos tipos de permutação mais complexos e menos frequentes nas provas de concursos,quais sejam, a permutação com elementos ordenados e a permutação caótica (ou desarranjo).

Permutação com Elementos Ordenados

Na permutação com elementos ordenados, determinados elementos devem seguir uma ordem definida,não podendo ser permutados livremente.

Vamos considerar o exemplo do grupo de estudo dos 3 alunos Ana, Beto e Caio. De quantas maneiras,podemos ordená-los, de acordo com as suas notas (sem empates), sabendo que a nota da
Ana foi maior do que a nota do Beto?
Para responder, vamos primeiro relacionar todas as possibilidades, ignorando essa restrição (sabemos que são P3 = 3! = 6 possibilidades):
i) Ana, Beto, Caio ii) Ana, Caio, Beto iii) Beto, Ana, Caio iv) Beto, Caio, Ana v) Caio, Ana, Beto vi) Caio, Beto, Ana
Agora vamos eliminar as possibilidades em que Beto está à frente de Ana (ordem incorreta):

i) Ana, Beto, Caio ii) Ana, Caio, Beto iii) Boto, Ana, Caio iv) Beto, Caio, Ana v) Caio, Ana, Beto vi) Caio, Beto, Ana
Claramente, há uma redução das ordenações possíveis, em relação à permutação simples. Mas por quê?

Na permutação simples, se mantivermos constantes as posições dos demais elementos,
haverá sempre uma opção em que Ana fica à frente de Beto e outra em que Beto ficará à frente deAna. Entretanto, apenas uma dessas opções atende à restrição de ordenação.
Por esse motivo, precisamos dividir 0 resultado pelo número de vezes em que os elementos ordenados trocam de posição.
Já sabemos como fazer isso! Dividindo a permutação simples pela permutação dos elementos ordenados!

Nesse exemplo, dividimos P3 por P₂:

P3 3! 3 x 2!

2! 2! " 3

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

De maneira geral, havendo n elementos, dos quais k elementos devem respeitar uma ordem específica, o número de possibilidades de ordená-los é:
Pn = n!

Pk kl

Esta fórmula é igual à da permutação com repetição!

FIQUE

ATENTO!

Na permutação com elementos ordenados, os elementos não devem ser necessariamente consecutivos.
No exemplo em que a ordenação foi Ana > Beto, aceitamos a opção ii (Ana, Caio, Beto),
sem que Ana e Beto estivessem em posições consecutivas.

Se o problema apontar que dois elementos estejam em determinada ordem e que sejam consecutivos, então será necessário tratá-lo como elemento único.
Em geral, havendo fci elementos que devam seguir uma ordem e outros k₂ elementos que devam seguir outra ordem, dividimos a permutação dos n elementos pela permutação de e de k₂ (o que também é similar à permutação com repetição):
Pn n!

fcilx/c₂!

Por exemplo, vamos supor a palavra ORDEM. O número de anagramas que podem ser formados de modo que as letras ORD estejam sempre nesta ordem, assim como as letras EM, corresponde a uma permutação de 5 elementos, de modo que 3 elementos sigam uma ordem e outros 2 elementos sigam uma ordem:
P₅ 5! 5x4x3!

P3 x P2 ~ 3! x 2! " 3! x 2 " 5 x 2 " 10

Para ilustrar, vejamos quais são essas 10 possibilidades:

i. ORDEM vi.
OERMD

ii. OREDM vii.
EORMD

iii. OERDM viii.
OEMRD

iv. EORDM ix.
EOMRD

V. OREMD X.
EMORD

Essa fórmula pode ser estendida para qualquer número de ordenações necessárias.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

................................f i (FCC/2014 - TRF 3? Região) Álvaro, Benedito, Cléber e outros dois amigos participam de uma corrida. Se
; apenas os cinco participaram dessa corrida, o número de possibilidades diferentes de maneira que Álvaro
= chegue antes que Benedito e este, por sua vez, chegue antes de Cléber é igual a:

j a) 20

b) 24

i c) 18

d) 22
i e) 26

s i Comentários:
I

: Há n = 5 elementos, dos quais k = 3 elementos estão ordenados: Álvaro > Benedito > Cléber.
Portanto, temos: i

^_ = n!
Pfe k!

P5 5!

5 4 20

?H= X =

Gabarito: A.

A

Permutação Caótica ou Desarranjo

Na permutação caótica ou desarranjo, considera-se que os elementos estão originalmente ordenados de certa maneira e que nenhum deles pode retornar para a sua posição original.
Vamos supor que 3 elementos {A, B, C} estejam originalmente posicionados nesta ordem, isto é, A em primeiro lugar, B em segundo lugar e C em terceiro lugar. Agora, vamos reordenar esses elementos, de modo que nenhum deles retorne à sua posição original.
Como o elemento A estava em primeiro lugar, ele poderá ocupar o 25 ou o 3Q lugar:

* A em 2^ lugar:A

o Como o elemento C estava em 35 lugar originalmente, ele terá que ocupar o 1Q lugar o Assim, resta a 3? posição para o elemento BPossível ordenação: C A B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

* A em 3e lugar:A

o Como o elemento B estava em 2Q lugar originalmente, ele terá que ocupar o 1Q lugar o Assim, resta a 2? posição para o elemento CPossível ordenação: B C A

Portanto, há 2 possibilidades de permutação caótica para esse exemplo.

Para calcular o número de possibilidades em uma permutação caótica (ou desarranjo) de n elementos, utiliza-se a seguinte fórmula:
Calma! Vamos juntos tentar digerir essa fórmula.

Observe que os denominadores das frações são fatoriais de 0 até n (total de elementos) e que os sinais das frações vão se alternando: quando o denominador é o fatorial de um número par, o sinal é positivo, quando o denominador é o fatorial de um número ímpar, o sinal é negativo.
Como não sabemos se n é par ou ímpar, utilizamos a expressão (—l)n. Assim, quando n é par, (—l)n = +1,e o sinal da fração é positivo; quando n é ímpar, (-l)n = —1, e o sinal da fração é negativo. Em outras palavras, não precisamos calcular uma função exponencial, apenas nos atentar para o sinal de n.
Ademais, considerando que 0! = 1 e que 1! = 1, os resultados da primeira e da segunda fração são:

Como o sinal da primeira fração é positivo e o da segunda é negativo, essas frações se anulam (1 - 1 = 0).Logo, podemos retirá-las da fórmula:

rl 1

D = n! x

1_ ... _l(—1)"1

ⁿ Í2! 3! n!

No nosso exemplo, tivemos n = 3, portanto:

1 3!

3!. 2! = 2

Que foi o resultado que obtivemos anteriormente.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (CESPE/2014 - TER-GO - Adaptada) As prestações de contas das campanhas dos 3 candidatos a governador de determinado estado foram analisadas por 3 servidores do TRE desse estado. Considerando que um
= servidor deve analisar exatamente prestação de contas e que, por coincidência, cada um dos 3
candidatos é i parente de um dos 3 servidores, julgue o item que se segue.
A quantidade de maneiras distintas de se distribuírem as prestações de contas entre os 3 servidores de modo que nenhum deles analise as contas de um parente é inferior a 5.
I

i Comentários:

; O enunciado informa que há 3 servidores que irão analisar as contas de 3
candidatos e que cada candidato

= é parente de um servidor:

Candidato A B C

Servidor a b c i Para que nenhum candidato seja avaliado pelo seu parente, devemos reordenar os candidatos de modo que
= nenhum deles retorne à posição original, indicada acima. Assim, temos uma permutação caótica (ou desarranjo) de 3 elementos.
: Como há poucos elementos, podemos contar as possibilidades, como fizemos anteriormente:

; - O candidato A pode ser analisado pelo servidor b:

Candidato A

Servidor a b c

- Nessa situação, o candidato C terá que ser analisado pelo servidor a;

- E restará o servidor c para o candidato B, resultando na seguinte possibilidade:

Candidato C A B

Servidor a b c

O candidato A pode ser analisado pelo servidor c:

Candidato A

Servidor a b c

- Nessa situação, o candidato B terá que ser analisado pelo servidor a;

- E restará o servidor b para o candidato C, resultando na seguinte possibilidade:

Candidato B c A

Servidor a b c

I

: Portanto, há 2 possibilidades.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= Alternativamente, podemos aplicar a fórmula de desarranjo que aprendemos:

rl 1 (-l)ni

Dn = n! x

1 1

-------- +...+------------

l_2! 3! n!

3! 3!

D4 = 3! x

.2!

_ 3!.

-------- =3-1 = 2

2! 3!

= Logo, o número de maneiras é inferior a 5.

I

Resposta: Certo.

i (FCC/2019 - Prefeitura de Recife/PE) Os quatro funcionários de uma repartição trabalham cada um em uma
= mesa, todos na mesma sala. O chefe da repartição determinou que os funcionários trocassem de mesa entre
= si. Os funcionários podem ser realocados na sala de modo que nenhum funcionário passe a ocupar a mesa que ocupava antes da realocação.
I

a

: a) de 4 maneiras diferentes.

I

i

: b) de 24 maneiras diferentes.

c) de 9 maneiras diferentes.

d) de 6 maneiras diferentes.

i e) de 12 maneiras diferentes.

Comentários:

Novamente, temos uma permutação caótica (ou desarranjo), mas agora com 4 elementos. Por haver uma maior quantidade de elementos, vamos direto para a fórmula:
r-i i

+ ...+ (---i-) ni

D4 = 4! x

Dn = n! x

1 1 1

.2! 3! + 4!.

l_2! 3! n!

41 41 41

2T3Í + 4! = 4X3-4 + 1 = 9

Gabarito: C
A

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ARRANJo E CoMBINAçÃo

As técnicas que veremos nesta seção (arranjo e combinação) trabalham com a seleção de um subconjunto dos elementos.
A ordem dos elementos selecionados será relevante para o arranjo, mas não para a combinação. Em outras palavras, selecionar os elementos A e B ou os elementos B e A são possibilidades distintas para o arranjo,porém equivalentes para a combinação.

Arranjo Simples

O arranjo de um conjunto finito de elementos é um subconjunto desses elementos, de tal maneira que a sua ordenação seja relevante.
Por exemplo, em um sorteio, em que o primeiro sorteado ganha um carro, e o segundo sorteado ganha uma bicicleta, a ordem, com certeza, será relevante. Em outras palavras, o cenário em que Ana é sorteada primeiro e Beto é sorteado depois será diferente daquele em que Beto é sorteado primeiro e Ana é sorteada depois.
Suponha que existam 6 pessoas em um sorteio, em que 3 delas serão sorteadas, não sendo possível sortear a mesma pessoa mais de uma vez. Considerando a ordem relevante, de quantas formas as3 pessoas poderão ser sorteadas?
Como a ordem importa, vamos sortear uma pessoa por vez, preenchendo os seguintes espaços com o número de possibilidades de cada sorteio:
12 3

Havendo 6 pessoas no total, há 6 possibilidades para sortearmos a primeira pessoa.
Assim, restarão 5 pessoas para o segundo sorteio. Em seguida, haverá 4 possibilidades para o terceiro e último sorteio:
6 5 4

12 3

Como os três sorteios irão ocorrer, pelo princípio multiplicativo, devemos multiplicar as possibilidades de cada evento. Dessa forma, o resultado desse arranjo é:
6x5x4

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E se houvesse 10 pessoas para 4 sorteios?

Para o primeiro sorteio, haveria 10 possibilidades; para o segundo, 9
possibilidades; para o terceiro, 8
possibilidades; e para o quarto, 7 possibilidades:

10 x 9 x 8 x 7

Parece um pouco a fórmula do fatorial, certo? Na verdade, é o início do fatorial do total de n elementos,
"estancado" após k fatores, sendo k o número de elementos sorteados.

E como fazemos para "estancar" um fatorial? Dividindo por um fatorial menor!

No caso de k = 4 sorteios para um conjunto de n = 10 pessoas, fazemos:

10! 10!

(10-4)! "TT

10x9x8x7x6!

------------- -- ------------- =10x9x8x7 = 5.040

6!

No caso geral, um arranjo sem reposição de k elementos, dentre n elementos distintos é:

. n!

n-k ~ (n-k)!

Outra notação possível para o arranjo é Ak.

Por exemplo, o número de maneiras de sortear 5 pessoas, dentre um total de 8, para prêmios distintos corresponde ao arranjo de 5 elementos, dentre 8:
8! 8! 8x7x6x5x4x3!

2485 = (8-5)! = 3! =---------------------------- 3! =8x7x6x5x4 = 6.720

Nem sempre a importância da ordem da seleção será fácil de visualizar. Vamos supor que, dentre um grupo de 10 funcionários de uma empresa, tivermos que selecionar 1 supervisor, 1 coordenador e 1 técnico.
Nesse caso, selecionar um funcionário como supervisor é diferente de selecionar esse mesmo funcionário como coordenador ou como técnico.
Imagine que a seleção desses cargos ocorre em uma sequência, por exemplo, primeiro supervisor, depois coordenador e depois técnico.
Assim, há diferença entre ser chamado primeiro, segundo ou terceiro. Logo, a ordem da seleção é, de fato,
importante, motivo pelo temos um arranjo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

FIQUE

ATENTO!

A fórmula de arranjo que acabamos de ver serve para casos sem reposição, ou seja, quando um mesmo elemento não puder ser selecionado mais de uma vez.
Caso haja reposição, o número de elementos disponíveis para cada sorteio é sempre o mesmo. Por exemplo, em uma seleção com reposição, cuja ordem importe, de 3elementos, dentre 6 elementos disponíveis no total, o número de possibilidades é:

6 x 6 x 6 = 63

De modo geral, o arranjo com reposição (ou repetição) de k elementos dentre n elementos no total é dado por:
An k = n x n x ... x n = nk k vezes
HORAM

(VUNESP/2019 - Prefeitura de Cerquilho/SP) Na bilheteria de um teatro há apenas 5
ingressos à venda para

I

a seção de uma peça. Se 4 amigos comprarem ingressos para essa seção, então o número total de posições distintas em que esses amigos poderão se acomodar no teatro é a) 120.
I

b) 80.

I

c) 60.

I

d) 20.

I

e) 5.

I

Comentários:

I

Temos uma seleção de 4 lugares, dentre 5 disponíveis, com importância de ordem, pois cada lugar é distinto
E

do outro. Assim, temos o arranjo de 4 elementos, dentre 5:

I

^5,4 = (5 _ 4)i = ^7 = Sx4x3x2xl = 120

: Gabarito: A.
I

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(VUNESP/2018 - PM/SP) Utilizando-se os algarismos 2, 3, 5, 6, 7 e 9, a quantidade de números múltiplos de5 e que tenham três algarismos distintos que podem ser formados é a) 25.
b) 20.

c) 15.

d) 10.

Comentários:

Para que o número formado pelos 6 algarismos indicados no enunciado seja múltiplo de
5, é necessário que o algarismo 5 seja o último algarismo. Assim, os diferentes números que podem ser formados com 3algarismos correspondem a um arranjo de 2 elementos, dentre 5:

5! 5x4x3!

(5-2)! _ 3! 5 x 4 = 20

Gabarito: B.

Ii (CESPE 2019/COGE-CE) Em determinado órgão, sete servidores foram designados para implantar novo
; programa de atendimento ao público. Um desses servidores será o coordenador do programa, outro será o
= subcoordenador, e os demais serão agentes operacionais.

: Nessa situação, a quantidade de maneiras distintas de distribuir esses sete servidores nessas funções é igual
: a a) 21.
b) 42.

c) 256.

d) 862.

e) 5.040.

Comentários:

Nessa questão, devemos definir o número de maneiras distintas de distribuir 7
servidores em funções distintas: 1 será coordenador, 1 será subcoordenador e os demais serão agentes. Note que, após a definição do coordenador e do subcoordenador, os que sobrarem serão necessariamente agentes. Por isso, não precisamos nos preocupar com eles, apenas com o coordenador o subcoordenador.
Para a escolha do coordenador, há 7 servidores, ou seja, 7 possibilidades:

Após a escolha do coordenador, restarão 6 possibilidades para o subcoordenador:

Como devemos escolher o coordenador E o subcoordenador, devemos multiplicar as possibilidades(princípio multiplicativo):

Número de Possibilidades = 7 x 6 = 42

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Alternativamente, poderíamos calcular o arranjo de 2 elementos, dentre 7:

Gabarito: B

i (CESPE 2020/TJ-PA) Em um sistema de acesso a uma rede de computadores, os usuários devem cadastrar
; uma senha de 6 dígitos, que deve ser formada da seguinte maneira:

I

: * os 2 primeiros dígitos devem ser letras minúsculas distintas, escolhidas entre as
26 letras do alfabeto;
I

: * os demais 4 dígitos da senha devem ser números inteiros entre 0 e 9, admitindo-se repetição.

I

: Nessa situação, a quantidade de senhas diferentes que podem ser formadas é igual a

: a) 3.674.

b) 5.690.

í c) 1.965.600.

d) 3.276.000.

j e) 6.500.000.

I

i Comentários:

= Nessa questão, temos os dois tipos de arranjo, com e sem reposição. Isso porque as letras devem ser distintas
= (não podem repetir) e os números podem ser repetir.

: Vamos representar a senha de 6 dígitos por 6 espaços:

= Os dois primeiros dígitos admitem as 26 letras do alfabeto, sem repetição. Logo,
temos 26 possibilidades

= para o primeiro espaço e 25 possibilidades para o segundo espaço (uma vez que a letra escolhida para o
: primeiro espaço não pode se repetir):

26 25

Os demais 4 dígitos admitem os 10 números (de 0 a 9), podendo haver repetição. Logo,
há 10 possibilidades para cada espaço:
26 25

10 10

10 10

Como a senha é formada por todos os 6 dígitos, então devemos multiplicar as possibilidades
(princípio multiplicativo):
Número de Senhas Possíveis = 26 x 25 x 10 x 10 x 10 x 10 = 6.500.000

Gabarito: E

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Combinação Simples

Assim como no caso do arranjo, a combinação é uma seleção de elementos de um conjunto finito. Entretanto, para a combinação, a ordem não importa.
Por exemplo, em um sorteio de participantes para um grupo de estudo, a ordem do sorteio de cada participante é irrelevante.
Nessa situação, algumas possibilidades distintas identificadas no arranjo são equivalentes na combinação.Consequentemente, a combinação de determinados elementos resulta em um número menor do que o arranjo dos mesmos elementos.
Menor, quanto?

Bem, todas as possibilidades de sorteio das mesmas pessoas, em que elas apenas mudam de lugar, são consideradas o mesmo resultado na combinação. Logo, precisamos dividir as possibilidades do arranjo pelo número de possibilidades em que os elementos selecionados trocam de posição, isto é,pela permutação dos elementos selecionados!
No caso de um sorteio de 3 pessoas, dividimos o número de possibilidades do arranjo por P₃:

r - ^6'3 - 6!

6'3 P3 (6-3)! 3!

De maneira geral, a combinação sem reposição de k elementos, de um total de n elementos, é dada por:
n!

(n-fc)!k!

Outras notações comuns para a combinação são ou l«** IX
..
.....................................* i i (FGV/2019 - Pref. Angra dos Reis/RJ) Maria possui em casa quatro tipos de frutas:banana, mamão, abacate 5

= e manga. Ela decidiu fazer uma vitamina com duas dessas frutas,
batendo-as juntas com leite no =

= liquidificador. O número de vitaminas diferentes que Maria poderá fazer é
=

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 3.

b) 4.

c) 5.

d) 6.

e) 12.

Comentários:

O número de vitaminas diferentes corresponde ao número de maneiras diferentes de Maria escolher 2, das4 frutas, sem que a ordem importe, logo, temos uma combinação de 2 elementos, dentre 4:

r' 4! 4! 4x3x2! 4x3 r

4,2 (4-2)! x2! 2! x2 2! x 2 " 2

Gabarito: D

(FGV/2022 - PC-RJ) Do grupo dos 6 novos policiais de uma delegacia, 2 deles serão escolhidos para um treinamento especial. O número de pares diferentes de policiais que podem ser enviados para o treinamento especial é:
a) 10

b) 12.

c) 15.

d) 16.

e) 18.

Comentários:

O número de pares de policiais que podem ser escolhidos, dentre 6, corresponde ao número de maneiras de escolher 2 elementos, dentre 6. Como a ordem dos escolhidos não importa,temos a combinação de 2
elementos dentre 6:

n!

^n,p (n —p)!xp!

6! 6x5x4! 6x5

Có'2 " (6 - 2)! x 2! 4! x 2! " 2 15

Gabarito: C

(CESPE 2018/BNB) Julgue o próximo item, relativo a análise combinatória e probabilidade.

Se 9 cidades forem interligadas por rodovias, de forma que entre quaisquer duas dessas cidades haja apenas uma rodovia interligando-as e essa rodovia não passe por nenhuma outra cidade, então essa malha viária será composta de 72 rodovias.
Comentários:

A ilustração a seguir representa as 9 cidades e 1 das rodovias possíveis.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Cidade 3 Cidade 6 j Cidade 9

Considerando que há exatamente 1 rodovia entre cada 2 cidades, então o número de rodovias é igual número de maneiras de selecionar 2 cidades, sem importância de ordem.
Sabendo que há 9 cidades, o número de maneiras de escolher 2 cidades é:

Gabarito: Errado.

9! 9!

(9 - 2)! x 2! 7! x 2!

9x8x7!
7! x 2!

9x8

2 36

9000000000000666666666666693333933388

É comum que a questão imponha restrições à seleção, da forma "pelo menos um".

Por exemplo, suponha um conjunto de 5 mulheres e de 4 homens. Quantos grupos distintos de 3 pessoas podem ser formados com pelo menos uma mulher?
Você pode resolver esse tipo de questão calculando todas as possibilidades de grupos,
desconsiderando-se a restrição imposta, e, em seguida, subtrair o número de possibilidades que não atendem à restrição.
Para o nosso exemplo, o número de maneiras possíveis de selecionar 3 pessoas, de um total de 4 + 5 = 9 pessoas, no total, é:
c — 9' -=---------- =---------=3x4x7 = 84 o .

9'3 (9-3)!x3! 6!x3! 3X2X1

Dentre essas possibilidades, não servem aquelas em que apenas homens são selecionados.
A quantidade de maneiras possíveis de selecionar 3 homens, dentre 4, é:

(4—3)!X3! I!x3!

Logo, o número de maneiras de formar grupos de 3 pessoas com pelo menos 1 mulher é:

84 - 4 = 80

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Casos Particulares de Combinação

Nessa seção, veremos alguns casos particulares da combinação simples. Você não precisa decorá-los, mas conhecê-los pode ajudar a resolver alguns problemas com mais rapidez.
i) Combinação de n elementos em n elementos (C„ n).

De quantas formas é possível selecionar 5 jogadores dentre 5 jogadores? Só uma, certo?
Selecionando todos os jogadores! De todo modo, vamos às contas:
n! n! n!

C = = = = 1

n,n (n — ri)\n\ (0)!n! lxn!

ii) Combinação de 0 elemento em n elementos ÇCn 0').

De quantas formas é possível selecionar 0 jogador dentre 5? Só uma também, certo? Não selecionando jogador algum! Vejamos como ficam as contas:
n! n!

Cn'° ~ (n-0)!0! ~ n! x 1 _ 1

iii) Combinação de 1 elemento em n elementos (Cn i).

Considerando 5 jogadores (A, B, C, D, E), quantas são as possibilidades de selecionar
1 jogador? 5, certo?
Podemos selecionar A, ou B, ou C, ou D ou E:

n! n

Cn-Í = (n —1)!1! = 1 = U

iv) Combinação de n — 1 elementos em n elementos

Considerando os 5 jogadores (A, B, C, D, E), quantas são as possibilidades de selecionar 4 jogadores?Podemos responder a essa pergunta, pensando em quem fica de fora em cada seleção.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ou seja, podemos selecionar todos exceto A; ou todos exceto B; ou todos exceto C; ou todos exceto D; ou todos exceto E. Assim, temos 5 possibilidades!
n n! n n

~ [n - (n — 1)]! (n - 1)! [n-n + 1]! ~i~n v) A combinação de k elementos em n é igual à combinação de n - k em n (Cn>k =
No item anterior, construímos o raciocínio de que selecionar 4 jogadores dentre 5 é o mesmo que deixar 1jogador. Além disso, o número de maneiras de deixar 1 jogador é o mesmo de selecionar 1 jogador.

Em outras palavras, de um total de 5 jogadores, o número de maneiras de selecionar 4
jogadores é o mesmo de selecionar 1 jogador.
Em geral, de um total de n elementos, selecionar k elementos é o mesmo que selecionar n — k elementos:
n!

Cn'k = (n-kW

n! n! n!

^Ti.n-k [n _ çn _ jyyy çn _ ^y [n _ n + /cji (n _ fcy k\(n — k)l

Vamos a mais um "facilitador de contas":

O somatório de todas as combinações possíveis de n elementos é 2"

Cn,0 + Cn,l + ^n,2 + H ^n,n-l + ^n,n = 2

Ou seja, o somatório de todas as possibilidades de combinações distintas de um total de n elementos, ou seja, a combinação com 0 elemento, as combinações com 1elemento,
combinações com 2 elementos, etc., até a combinação com n elementos, é igual a 2n.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

INDO MAIS

FUNDO!

Essa propriedade que acabamos de ver é um dos teoremas associados ao chamado
Triângulo de Pascal, que pode ser representado da seguinte forma:

G),o

Q,o G,i w 1 1

^2,0 ^2,1 ^2,2
12 1

£*3,0 £*3,1 ^3,2 ^3,3
13 3 1

£4,0 £4,1 C4,2 ^4,3 ^4,4
1 4 6 4 1

£5,0 ^S,! ^5,2 ^S,3 £5,4 ^5,5
1 5 10 10 5

O Triângulo de Pascal é formado por combinações Cnk, sendo n o número da linha e k o número da coluna, iniciando-se pela linha e coluna zero.
Os números Cnk podem ser chamados Números Binomiais ou Coeficientes Binomiais.

Para construir o Triângulo, somamos 2 elementos consecutivos (colunas k e k + 1) de uma mesma linha (n), para obter o elemento da linha abaixo (n + 1) na coluna k + 1:
13+^1

1 4 6 + ^, 1

1 5 10 10 5 1

Essa propriedade é chamada de Relação de Stifel e corresponde ao seguinte:

Cn,k + Gi,k+1 — Cn+l,k+l

Além disso, a soma dos elementos de uma coluna (k), desde o seu início (linha k) até alguma linha k + n, é igual ao elemento da linha seguinte (k + n + 1) e coluna seguinte(k + 1), conforme ilustrado abaixo para a coluna 1:

i[í
12 1

13 3 1

íUy 4 i

1 5 10 10 5 1

Essa propriedade é chamada de Teorema das Colunas e pode ser descrita como:

Ck,k d" Ck+l,k d" ^k+2,k d" d" Cfc+n,k ^k+n+l,k+l

A propriedade que vimos antes (Cn>0 d- Cn>1 + Cn<2 + —I- = 2n) é chamada deTeorema das Linhas, pois Cn>0 + Cnl + d- —E Cn>?J é a soma de todos os elementos de uma linha n.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

(2019 - Prefeitura de Colômbia/SP) Em uma pequena escola de música os estudantes são especializados em instrumentos conforme tabela a seguir:
Instrumentos
Guitarra
Contrabaixo
Bateria

Teclado

Número de estudantes

O número de bandas diferentes que poderão ser formadas com os estudantes desta escola de música com a seguinte constituição: 2 guitarristas, 1 contrabaixista, 1 baterista e 1 tecladista está compreendido entre:
a) 1e 300

b) 301e 400

c) 401 e 600

d) 601e 800

Comentários:

Para selecionar 2 guitarristas, dentre 6, temos:

n!

Cn'k = (n-kW

6! 6x5

Có'2 ~ (6-2)! 2! _ 2 _ 15

Para as demais combinações, basta conhecer o caso especial Cnl = n.

Para selecionar 1 contrabaixista, temos n = 2: C₂,i = 2.
Para selecionar 1 baterista, temos n = 4: C₄₁ = 4.

Para selecionar 1 tecladista, temos n = 3: C3jl = 3.

Como a banda terá todos esses instrumentistas, pelo princípio multiplicativo,
devemos multiplicar todas essas possibilidades:
Cguitarristas X Ccontrabaixistas X Cbateristas X Ctecladistas

15x2x4x3 = 360

Gabarito: B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= (CESPE 2018/PF) Para cumprimento de um mandado de busca e apreensão serão designados um delegado,
; 3 agentes (para a segurança da equipe na operação) e um escrivão. O efetivo do órgão que fará a operação
= conta com 4 delegados, entre eles o delegado Fonseca; 12 agentes, entre eles o agente Paulo; e 6 escrivães,
= entre eles o escrivão Estêvão.

: Em relação a essa situação hipotética, julgue o item a seguir.

= Considerando todo o efetivo do órgão responsável pela operação, há mais de 5.000 maneiras distintas de se
; formar uma equipe para dar cumprimento ao mandado.

!

i Comentários:

A questão pede o número de maneiras de escolher 1 delegado (dentre 4), 3 agentes
(dentre 12) e 1 escrivão i (dentre 6):
i - O número de formas de escolher 1 delegado, dentre 4, é igual a 4 - caso especial C₄₁ = 4;

i - O número de formas de escolher 3 agentes, dentre 12, é igual a:

12! 12x11x10

í C™ = *3T 3X2 =2X11X10 =

i - O número de formas de escolher 1 escrivão, dentre 6, é igual a 6 - caso especial C₆₁ = 6.

I

; Para formar toda a equipe, multiplicamos esses resultados (princípio multiplicativo):

Número de possibilidades = 4 x 220 x 6 = 5280

: Logo, há mais de 5.000 maneiras de formar a equipe.

I

: Gabarito: Certo.

i (FCC/2018 - Analista Judiciário do TRT 15? Região) Dez pastas diferentes devem ser guardadas em duas
; caixas diferentes. Se a única regra é que cada uma das caixas contenha pelo menos uma pasta,
então a quantidade de maneiras distintas como se pode guardar essas pastas nas caixas é j a)510
b) 1.022

j c) 126.

d) 2.048

i e)256

i Comentários:

= Como a ordem dentro das caixas não importa, utilizaremos combinação. Além disso, é importante notar que
= ao selecionarmos as pastas para uma das caixas, teremos definido as pastas que serão guardadas na outra
= caixa. Por isso, podemos pensar na combinação para uma das caixas apenas.

= Assim, podemos selecionar 1, 2, 3, 4, 5, 6, 7, 8 ou 9 pastas para a primeira caixa. Não podemos selecionar 10
= pastas porque não sobraria pastas para a segunda caixa, o que não é permitido
(cada caixa deve conter pelo

= menos 1 pasta). Pelo mesmo motivo, não podemos selecionar 0 pasta para a primeira caixa.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Devemos, portanto, calcular as possibilidades de combinação Cio,i, Cio,2, Cio,3, Cio,4, Cio,5,
Cio,6, Cio,7, Cio,s e
Cio,9. Esses eventos são mutuamente exclusivos (selecionamos 1 OU 2 OU 3 OU ... OU 9 pastas para a primeira caixa). Portanto, as possibilidades desses eventos devem ser somadas (princípio aditivo).
Para facilitar as contas, utilizaremos a propriedade de combinação que vimos:

Porém, não é exatamente essa soma que estamos buscando, pois não temos nem C10j0 nem
C1010. Por isso,
devemos subtrair os valores dessas combinações do resultado:

£10,1 + Qo,2 + G.0,3 + G.0,4 + £10,5 + Qo,6 + Qo,7 + Qo,8 + G.0,9 = 210 — Qo,O — ^10,10

Sabemos, ainda, que Cn0 = 1, logo, C10 0 = 1; e Cnn = 1, logo, C10jl0 = 1:

Cio.l + Cio,2 + Cio,3 + Cio,4 + Cio,5 + Cio,6 + ^10,7 + Ci0,8 + Ci0,9 = 1024 - 1 - 1 = 1022

Gabarito: B

Combinação Completa

Os problemas de combinação completa (ou combinação com repetição) envolvem um conjunto de n tipos de elementos diferentes, dos quais serão escolhidos k elementos iguais ou diferentes.Também podemos pensar que será selecionado um número k de objetos, iguais ou diferentes, dentre n tipos diferentes.
Por exemplo, escolher k = 3 potes de sorvete havendo um total de n = 5 marcas distintas (os potes podem ser de uma mesma marca ou de marcas distintas).
Observe que essa situação é diferente da escolha de 3 potes de sorvete dentre 5
potes, o que seria a combinação simples de 3 elementos, dentre 5 (Cs,3 = 10). Essa também seria a combinação para escolher 3marcas dentre 5 marcas.

Porém, no nosso exemplo atual, temos que escolher 3 potes dentre 5 marcas. O número de possibilidades é muito maior do que a combinação simples de 3 dentre 5 elementos.
Para calcular todas as possibilidades, vamos imaginar que cada marca de sorvete esteja em uma seção separada do congelador:
marca A marca B marca C marca D
marca E

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos escolher, por exemplo, 3 potes da marca A.

marca A marca B marca C marca D
marca E

Ou 2 potes da marca B e 1 da marca C:

marca A marca B marca C marca D
marca E

Ou, ainda, 1 da marca A, outro da D e outro da E:

Repare que podemos considerar esse problema como a permutação dos objetos (potes de sorvetes) e das divisórias que separam as diferentes marcas.
Nesse caso, temos 3 potes de sorvete e 4 divisórias - o número de divisórias é sempre o número de marcas menos 1. Assim, temos a permutação de 7 elementos, sendo 3 potes e 4 divisórias (elementos repetidos).
Portanto, a combinação completa de 3 objetos de 5 marcas, indicada por CR$, é igual à permutação de 7elementos, com repetição de 3 e 4 elementos:

7!

3! x 4!

7x6x5
3x2

De maneira geral, a combinação de p objetos de n tipos (ou marcas),
equivale à permutação de n — 1 divisórias com p objetos, ou seja, à permutação de n — 1 + p elementos, com repetição de n — 1 e p elementos:
f dV l,p (n—1+p)!

n ~ n—l+p ~ (n-i)!Xp!

Também devemos utilizar a combinação completa em problemas de distribuição de objetos entre pessoas(ou lugares). Por exemplo, a distribuição de 3 cestas básicas para 5 famílias segue o mesmo raciocínio.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A combinação completa de p objetos de n tipos também equivale à combinação simples de p elementos, dentre n — 1 + p elementos disponíveis:
p (n-l+p)! r

C n ~ (n-l)ixp! " C«-l+P-P

No nosso exemplo, a combinação completa de p = 3 potes de sorvete, havendo um total de n = 5 marcas distintas, corresponde à combinação de 3 elementos, dentre 5 - 1 +3 = 8
elementos no total.

I«** IX

i (FGV/2018 - ALE-RO) Helena entra em uma sorveteria que oferece sorvetes de 8 sabores diferentes.
Helena i deseja escolher uma casquinha com duas bolas de sorvete não necessariamente de sabores diferentes.A

; ordem em que as bolas forem colocadas na casquinha não fará a escolha de Helena ser diferente.

: O número de maneiras de Helena escolher sua casquinha é i j a) 64.
b) 56.

j c) 36.

d) 28.

i j e) 16.
I

I

i Comentários:

I

I

: Nessa questão, temos um exemplo de combinação com reposição (ou combinação completa). Trata-se de i
= uma combinação porque a ordem não importa, como a questão informa. E há reposição pelo fato de
Helena i poder escolher sabores não necessariamente diferentes. A fórmula da combinação completa é:
= (n-l + p)!
=

j n (n-l)!xp!
j

: Sabendo que há 8 sabores disponíveis (n = 8) e que Helena irá escolher 2 bolas de sorvete (p =
2):

i , (8 + 2-1)! 9!
9x8x7! 9x8 =

j 8 (8-1)! x 2! 7! x 2!
7! x 2 2 j

= Gabarito: C

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(2019 - Conselho Regional de Medicina/AC) O pai de 3 filhos, com idades diferentes, distribuiu 9
balas = I
idênticas entre eles, de forma que o mais velho recebeu o dobro de balas do caçula e o filho do meio recebeu mais balas que o caçula e menos balas que o mais velho. O filho caçula recebeu X balas e o filho do meio i recebeu Y balas.i

Com base nessa situação hipotética, julgue o item a seguir.
j

Se alguém deseja distribuir 9 balas idênticas entre 3 pessoas, sem qualquer critério de distribuição, com cada i uma delas recebendo pelo menos uma bala, então existem 28 maneiras de se fazer a distribuição.
Comentários:

s

Esse também é um caso de combinação completa, em que as balas correspondem aos objetos e as pessoas correspondem às seções.
Porém, o problema apontou para uma restrição: todas as pessoas receberão pelo menos uma bala.

Após distribuir uma bala por pessoa, totalizando 3 balas, sobrarão 9-3 = 6 balas a serem distribuídas, sem critério, para as 3 pessoas.
Portanto, temos a combinação completa de k = 6 objetos para n = 3 pessoas, ou seja, n - 1 = 2
divisórias:

rnP _ pn-l,p _ (n 1+p)!

n n"1+P (n-l)lxp!

Gabarito: Certo

8!

2! x 6!

8x7

; (CESPE 2018/SEFAZ-RS) Se 7 kg de feijão forem distribuídos para até quatro famílias, de modo que cada uma ;
delas receba um número inteiro de quilos, então, nesse caso, a quantidade de maneiras distintas de se i distribuírem esses 7 kg de feijão para essas famílias será igual a j j a) 30.
b) 120.

; c) 330.
;

d) 820.

í e) 1.320.

i Comentários:

I

: Podemos representar os quilos de feijão como 2Zle as 4 famílias como seções separadas por uma barra:

Família 1 Família 2 Família 3 Família

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado permite que alguma(s) família(s) fique sem quilos de feijão porque menciona que a distribuição será para "até" 4 famílias. Assim, há 7 quilos de feijão (p = 7) a serem distribuídos livremente para 4 famílias(n = 4).

Essa distribuição pode ser vista como a permutação dos 7 l le das 3 barras que separam as famílias, isto é,
uma permutação de 10 elementos, com repetição de 7 e de 3 elementos:

Gabarito: B.

10!

3! x 7!

10 x 9 x 8 x 7!

3! x 7!

10 x 9 x 8

—-—-— = 10 x 3 x 4 = 120

(FGV/2021 - Pref. Paulínia) Eva tem 9 maçãs indistinguíveis e deseja distribuí-las a 3
amigos de forma que cada um deles fique com, ao menos, 2 maçãs. O número de maneiras distintas de Eva distribuir as maçãs é a) 12
b) 10

c) 9

d) 8

e) 6

Comentários:

Essa questão trabalha com combinação completa, em que precisamos distribuir 9 maçãs para 3 amigos.Primeiro, distribuímos as maçãs obrigatórias, quais sejam, 2 para cada amigo. Após a distribuição das 6maçãs, restarão 3 a serem distribuídas livremente.

A figura a seguir ilustra uma forma de distribuir as 3 maçãs:

Amigo 1 Amigo 2 Amigo 3

A combinação completa, entre n = 3 amigos e p = 3 objetos, pode ser vista como a permutação dos 3objetos e das 2 barras que separam os amigos, que corresponde a permutação de 5
elementos no total, com repetição de 3 e de 2 elementos:
Gabarito: B

6666666666999933333333333311111111111

5!

3! x 2!

5x4x3!

3! x 2

5 x 2 = 10

Número de Soluções Inteiras de Equações

Os problemas de combinação completa, que acabamos de ver, podem ser analisados de outra perspectiva.
Vamos considerar o mesmo exemplo da compra de 3 potes de sorvete, dentre 5 marcas distintas.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos representá-lo por uma equação, em que xA representa a quantidade de potes de sorvete adquiridos da marca A; xB representa a quantidade de potes de sorvete da marca B;xc, a quantidade de potes da marca C; xD, a quantidade de potes da marca D; e xE, a quantidade de potes da marca E.
Sabendo que o total de potes de sorvete adquiridos é igual a 3, então a soma dos potes adquiridos de todas as marcas é igual a 3:
X^ + Xg + Xc + XD + XÊ = 3

Como os valores de x representam as quantidades de potes adquiridos de cada uma das
5 marcas, de modo que o total de potes seja igual a 3, o número de maneiras de escolher os 3 potes de sorvete corresponde ao número de maneiras de encontrar os valores de x que resolvem essa equação.
Ou seja, o problema de combinação completa, que vimos antes, corresponde ao número de soluções possíveis para essa equação.
Afinal, podemos representar os diferentes x,- por espaços entre os símbolos de^h6 os valores que eles assumem por , de forma que o total seja igual a 3. Um exemplo dessa representação é:
j i _r x£
Aqui, temos xA = 1, xB = 2, xc = 0, xD = 0, xE = 0. Outra opção seria:

i i i„ i y f
XB

r xD XB
Nesse exemplo, temos xA — 0,xB = 0,xc = 0, xD = 0 e xE = 3.

Ou seja, o número de maneiras de encontrar os possíveis valores de x, isto é, o número de soluções possíveis para a equação, corresponde a uma permutação de p = 3( com n - 1 = 4 símbolos de^^
7!

4! x 3!

Em outras palavras, a combinação completa CRf também indica o número de soluções possíveis para a equação xA + xB + xc + xD + xE = 3.
De modo geral, o número de soluções possíveis para a equação xx + x₂ 3 1- xn = p é:
pn-l,p rn-l+p
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O resultado da equação corresponde ao número de objetos: p

O número de variáveis corresponde ao número de seções: n

Mais precisamente, a combinação completa CR? indica o número de soluções inteiras e não-negativas possíveis para a referida equação.
Por que somente soluções inteiras e não-negativas?

Se pudéssemos escolher números negativos, poderíamos sempre diminuir uma unidade de uma variável e aumentar uma unidade de outra para manter a soma constante(no nosso exemplo, igual a 3).
Ou seja, poderíamos ter xA = 4 e xB = — 1 (e as demais variáveis nulas), xA =
5 e xB =

—2, xA = 6 e xB = —3, etc. O número de soluções seria infinita!

O mesmo vale para números decimais. Há infinitos números decimais entre quaisquer números inteiros. Por exemplo, entre 2 e 3, há 2,1; 2,11; 2,111; 2,1111;...
Portanto, se as incógnitas pudessem assumir quaisquer valores reais, sempre poderíamos aumentar uma incógnita um "pouquinho" e diminuir outra esse mesmo "pouquinho"e manter a soma constante.
Portanto, somente o conjunto das soluções inteiras e não-negativas da equação é um conjunto finito.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

FIQUE

ATENTO!

Como vimos, a princípio, são permitidas soluções nulas para algumas incógnitas.

Caso o problema traga alguma situação especial diferente dessa, como exigir que as soluções sejam positivas (ou seja, não permitir soluções nulas), precisamos fazer as adaptações necessárias.
Por exemplo, considere a seguinte equação, em que os valores de x precisam ser positivos:

xA + xB + xc + xD = 6, com x > 0
Nesse caso, precisamos primeiro distribuir 1 unidade para cada x.

Assim, sobrarão 6-4 = 2 unidades a serem livremente distribuídas, o que pode ser representado pela seguinte equação (em que x pode assumir valores nulos):
xA + xB + xc + xD = 2, com x > 0
Sabemos que o número de soluções possíveis para essa equação é:

DDATir ADI

r1

(CESPE/2011-SEDUC/AM) A equação Xi + X2 + X3 = 18 possui mais de 200 soluções inteiras e não negativas.
Comentários:

O número de soluções inteiras e não-negativas para essa equação é o número de combinações completas com p = 18 objetos em n = 3 seções, ou seja:
rnP pn~l>P

— n-l+p

O resultado (190) é inferior a 200.

Gabarito: Errado.

0,0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)
www. estra tegiaconcursos. com. br

(2015 - Prefeitura de Mangaratiba/RJ) Considerando o conjunto universo dos números inteiros não negativos, podemos afirmar que a equação x + y + z- 5 = 0:
a) possui uma única solução.

b) possui infinitas soluções.

c) possui 21 soluções.

d) possui 35 soluções.

e) possui 42 soluções.

Comentários:

Primeiro fazemos o seguinte ajuste na equação:

x + y + z = 5

O número de soluções inteiras e não-negativas para essa equação é o número de combinações completas com p = 5 objetos em n = 3 seções, ou seja:
Gabarito: C.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Princípios de Contagem

Item. 1. (CEBRASPE 2021/PC-DF) Um agente, com o objetivo de mensurar o risco de propagação da covid-19 em uma investigação na qual averiguava um possível descumprimento do artigo 268 do
Código Penal,
que define como crime de infração de medida sanitária "infringir determinação do poder público,destinada a impedir introdução ou propagação de doença contagiosa", obteve de uma testemunha as informações a seguir.
* Houve, no local investigado, uma festa, com aglomeração de moças e rapazes; não havia álcool em gel e ninguém estava usando máscaras.
* Cada rapaz cumprimentou exatamente uma vez a todos os outros rapazes com apertos de mão.

* Cada moça cumprimentou exatamente uma vez a todos os outros presentes com um aceno.

Considerando que são verdadeiras as informações prestadas pela testemunha da situação hipotética precedente, julgue o item a seguir.
Se, na festa, havia 20 moças e 18 rapazes, o número de cumprimentos entre moças e rapazes com acenos foi superior a 350.
Comentários:

A questão informa que as moças cumprimentaram todos, inclusive rapazes, com um aceno.
O item informa que havia 18 rapazes, logo, cada moça acenou para um rapaz 18 vezes.
Sabendo que havia 20 moças, o número de acenos entre moças e rapazes corresponde ao produto (princípio multiplicativo):
18x 20 = 360

Que é superior a 350.

Gabarito: Certo

Item. 2. (CEBRASPE 2021/PC-DF) Um agente, com o objetivo de mensurar o risco de propagação da covid-19 em uma investigação na qual averiguava um possível descumprimento do artigo 268 do
Código Penal,
que define como crime de infração de medida sanitária "infringir determinação do poder público,destinada a impedir introdução ou propagação de doença contagiosa", obteve de uma testemunha as informações a seguir.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

* Houve, no local investigado, uma festa, com aglomeração de moças e rapazes; não havia álcool em gel e ninguém estava usando máscaras.
* Cada rapaz cumprimentou exatamente uma vez a todos os outros rapazes com apertos de mão.

* Cada moça cumprimentou exatamente uma vez a todos os outros presentes com um aceno.

Considerando que são verdadeiras as informações prestadas pela testemunha da situação hipotética precedente, julgue o item a seguir.
Se na festa havia 20 moças, o número de cumprimentos com acenos entre moças foi superior a 200.

Comentários:

A questão informa que as moças cumprimentaram todos com um aceno. Considerando que havia 20 moças e que cada moça cumprimentou todas as outras 19 moças, então o número de acenos entre moças corresponde ao produto (princípio multiplicativo):
20 x 19 = 380

Que é superior a 200.

Gabarito: Certo

Item. 3. (CEBRASPE 2021/PM-AL) O próximo item apresenta uma situação hipotética seguida de uma assertiva, a ser julgada com base na matemática e em suas aplicações na atividade policial.
Um fugitivo tenta despistar policiais, realizando uma fuga entre três cidades (A, B e
C). Existem duas estradas ligando a cidade A à B e três estradas ligando a cidade B à C. Nessa situação hipotética, há 12 formas diferentes de o fugitivo ir da cidade A até a C, passando pela cidade B, voltando para a cidade A e passando novamente pela cidade B, sem repetir as estradas que usar para ir de A a C.
Comentários:

A questão informa que há 2 estradas entre as cidades A e B e 3 estradas entre B e C:

O enunciado pergunta o número de possibilidades de o fugitivo ir de A para B e de
B para C e, em seguida,
voltar de C para B e de B para A, sem repetir as estradas.

Em relação à ida, para ir de A para B, há 2 possibilidades; e para ir de B para C há 3
possibilidades. Para voltar sem repetir as estradas, restarão 2 possibilidades entre C e B e uma única estrada entre B e A.
Pelo princípio multiplicativo, o número de possibilidades é:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

2x3x2x1=12

Gabarito: Certo

Item. 4. (CEBRASPE 2021/PC-DF) Para ter acesso a um arquivo digital criptografado, um cibernauta deve testar uma senha de 8 dígitos composta pelos algarismos de 0 a 9, admitida a repetição. Ocibernauta teve a informação prévia de que o arquivo foi criado no dia 23/12/19 e que o dia, o mês e o ano da criação do arquivo, representados por dois algarismos cada, estão presentes na senha, mas aparecem em ordem aleatória.
Com base nessas informações, julgue o item a seguir.

Sem a informação de que o dia, o mês e o ano da criação do arquivo fazem parte da senha, a quantidade máxima de senhas a serem testadas pelo cibernauta seria de 108.
Comentários:

O item pergunta quantas possibilidades de senha de 8 dígitos podem ser formadas, com
10 algarismos (de 0
a 9), admitindo-se a repetição. A figura a seguir ilustra as possibilidades para cada dígito:

10 10 10

10 10

10 10 10

Pelo princípio multiplicativo, devemos multiplicar as possibilidades de cada dígito:

10 x 10 x 10 x 10 x 10 x 10 x 10 x 10 = 108

Gabarito: Certo

Item. 5. (CEBRASPE 2021/SEED-PR) As placas de veículos dentro do novo modelo aprovado pelo
MERCOSUL
possuem um padrão de letras e algarismos diferente do das antigas placas brasileiras. No Brasil, no caso dos automóveis, as placas no novo padrão terão 4 letras e 3 algarismos, seguindo-se a sequência LLLALAA
(sendo L letras e A algarismos).

Suponha que, para a escolha da combinação de letras e algarismos de uma placa no padrão MERCOSUL,
possam ser utilizados os algarismos de 0 a 9 e as 26 letras do alfabeto, podendo-se repetir algarismos e letras. Nesse caso, a alteração realizada no modelo de placa representará, em relação ao modelo anterior,um aumento no total de placas que poderão ser produzidas. Esse aumento será de a) 120%
b) 160%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) 210%

d) 260%

e) 330%

Comentários:

O enunciado apresenta as regras da placa nova e pergunta de quanto foi o aumento de placas possíveis em relação ao modelo antigo.
Para isso, a questão informa que o modelo novo possui 4 letras e 3 algarismos (da forma LLL ALAA) e que há26 possibilidades de letras e 10 possibilidades de algarismos (de 0 a 9), permitindo-se a repetição:
26 26 26

L L L

10 26

A L

10 10

A A

Pelo princípio multiplicativo, o número de possibilidades da placa nova é:

Aí = 26 x 26 x 26 x 10 x 26 x 10 x 10 = 264 x 103

Sabemos que a placa antiga é formada por 3 letras e 4 algarismos (LLL AAAA):

26 26 26

L L L

10 10

A A

10 10

A A

Pelo princípio multiplicativo, o número de possibilidades da placa antiga é:

A = 26 x 26 x 26 x 10 x 10 x 10 x 10 = 263 x 104

A razão entre o número de placas do modelo novo e o número de placas do modelo antigo é:

N 264 x 103 26

R ~ Ã ~ 263 x 104 1Õ _ 2,6

Isso significa que a quantidade de placas do modelo novo é 2,6 vezes a do modelo antigo. Em outras palavras,o aumento foi de 1,6 vezes (160%) a quantidade do modelo antigo.

Por exemplo, se houvesse 100 placas no modelo antigo, no novo, teríamos 260 placas, o que corresponde a um aumento de 260 - 100 = 160 placas, ou seja, 160% da quantidade do modelo antigo.
Gabarito: B.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (CEBRASPE 2019/Pref. São Cristóvão) Com relação a sistemas lineares e análise combinatória,julgue o item.

Situação hipotética: No jogo de basquete, cada um dos cinco jogadores de um time pode ocupar as seguintes posições: armador, ala armador, ala, libero e pivô. O elenco do time Alfa é formado por 2 armadores, 2 alas armadores, 3 alas, 2 líberos e 3 pivôs. Assertiva: Nessa situação, sabendo-se que em quadra jogam apenas 5jogadores por time e que os demais ficam no banco, é correto afirmar que existem 216
formas distintas de montar o time Alfa para iniciar a partida com exatamente um pivô, um armador e um ala.
Comentários:

A questão indaga sobre o número de possibilidades de formar um time exatamente com 1
pivô, 1 armador e 1 ala. A palavra exatamente indica que não haverá outro pivô, armador ou ala.Assim, os outros 2 jogadores
(uma vez que há um total de 5 jogadores) podem ser líberos ou alas armadores.

Outro ponto importante é que todas as posições são distintas. Ou seja, ainda que sejam selecionados 2líberos, por exemplo, o fato de escolhermos um para a posição e outro para a 5-
posição será diferente de escolher os mesmos líberos com as posições trocadas. Nesse caso, podemos representar as diferentes posições desse time da seguinte forma:
Pivô

Armad

Ala

Líbero/Ala Armad

Líbero/Ala Armad

Há 3 pivôs no time, logo, há 3 possibilidades para pivô:

Pivô

Armad

Ala

Líbero/Ala Armad

Líbero/Ala Armad

Há 2 armadores e 3 alas, logo, há 2 possibilidades para armador e 3 possibilidades para ala:

Pivô

Armad

Ala

Líbero/Ala Armad

Líbero/Ala Armad

Por fim, há 2 líberos e 2 alas armadores. Assim, há 4 possibilidades para uma das posições de líbero/ala armador e 3 possibilidades para a outra posição:
Pivô

Armad

Ala

Líbero/Ala Armad

Líbero/Ala Armad

Como devemos escolher os jogadores para todas essas vagas no time, aplicamos o princípio multiplicativo:
Número de formas: 3x2x3x4x3 = 216

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 7. (CEBRASPE 2018/IFF) Três pessoas entraram em uma sala de cinema onde restavam apenas 5assentos desocupados. Nesse caso, a quantidade de maneiras diferentes de essas pessoas ocuparem esses assentos é igual a a) 10.
b) 12.

c) 27.

d) 60.

e) 125.

Comentários:

A questão pede o número de maneiras em que 3 pessoas podem se sentar em 5 assentos.
Vamos representar a decisão das 3 pessoas da seguinte forma:
PI P2 P3

A primeira pessoa possui 5 opções de assentos, logo há 5 possibilidades distintas para ela:

PI P2 P3

A segunda pessoa tem 4 opções de assentos, uma vez que a pessoa anterior selecionou 1 assento:

5 4

PI P2 P3

Analogamente, a terceira pessoa tem 3 opções de assentos:

5 4 3

PI P2 P3

Como todas as pessoas devem se sentar, devemos multiplicar essas possibilidades (princípio multiplicativo):Número de possibilidades = 5x4x3 = 60

Gabarito: D.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 8. (CEBRASPE 2018/PF) Em um processo de coleta de fragmentos papilares para posterior identificação de criminosos, uma equipe de 15 papiloscopistas deverá se revezar nos horários de 8 h às 9h e de 9 h às 10 h.

Com relação a essa situação hipotética, julgue o item a seguir.

Se dois papiloscopistas forem escolhidos, um para atender no primeiro horário e outro no segundo horário,então a quantidade, distinta, de duplas que podem ser formadas para fazer esses atendimentos é superior a300.

Comentários:

Essa questão pede o número de maneiras de escolher um servidor para o primeiro horário e outro para o segundo horário. Vamos representar os horários da seguinte forma:
1° 2°

Há 15 servidores disponíveis para a escolha no l9 horário:

1° 2°

Após a escolha do servidor para l9 horário, restam 14 servidores para o 29 horário:

15 14

1° 2°

Como os servidores de ambos os horários precisam ser escolhidos, devemos multiplicar esses valores(princípio multiplicativo):

Número de possibilidades = 15 x 14 = 210

Logo o número de possibilidades de formar duplas para o atendimento é inferior a 300.

Gabarito: Errado.

Item. 9. (CEBRASPE 2018/PM-AL) A figura seguinte mostra a planta baixa de um condomínio. O terreno ocupado pelo condomínio é um quadrado de lados que mede 60 m. Nesse condomínio, as áreas indicadas por El, E2 e E3 correspondem aos locais onde estão construídos os prédios residenciais, e as regiões em branco correspondem às vias de livre circulação para pedestres e veículos.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A partir da figura e das informações precedentes, julgue o item a seguir, considerando que a área de E2seja igual a 200 m2.

Situação hipotética: Dois policiais devem ir do ponto A ao B, pelas vias de livre circulação, cada um deles fazendo um caminho diferente, sem passar duas vezes pelo mesmo local. Toda vez que os dois policiais chegarem ao ponto B, conta-se como realizado um trajeto. Assertiva: Nessa situação, a quantidade de trajetos distintos que os policiais poderão percorrer é inferior a 40.
Comentários:

Vejamos quantas são as possibilidades de ir de A até B:

*B >

E2 /ZZ

El

E3

Z íAZ

Assim, há 7 possibilidades de caminhos de A até B. Vamos representar a escolha dos 2
policiais conforme abaixo, uma vez que eles deverão escolher caminhos distintos:
1° 2°

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabemos que há 7 caminhos para o primeiro policial escolher:

1° 2°

Após a escolha do primeiro, restarão 6 caminhos possíveis para o segundo policial escolher:

7 6

1° 2°

Pelo princípio multiplicativo, devemos multiplicar essas possibilidades:

Número de possibilidades = 7 x 6 = 42
Logo, o número de possibilidades de escolha dos dois policiais é superior a 40.
Gabarito: Errado

Item. 10. (CEBRASPE 2017/PM-MA) Determinado laboratório de análises clínicas está sendo investigado por emitir laudos falsos de um exame constituído por 7 indicadores, correspondentes à concentração de 4compostos na corrente sanguínea, obtidos da seguinte forma: uma medição da concentração de cada um dos compostos A, B, C e D, e 3 medições, por 3 diferentes técnicas, da concentração do composto E.Os laudos verdadeiros de 7 pacientes (chamados pacientes-fonte), com prenomes distintos, entre elesAmanda, Bárbara, Carlos e Daniel, eram usados para compor laudos falsos para os demais pacientes.
Para dificultar a ação da autoridade policial, na montagem de um laudo falso, o laboratório tomava o cuidado de, no conjunto de 7 medições que constituíam cada laudo falsificado, usar apenas uma medição de cada paciente-fonte, ou seja, de nunca usar 2 ou mais medições de um mesmo paciente-fonte.Com referência a essa situação hipotética, julgue o item seguinte.
Se fosse adotada a estratégia de falsificar laudos seguindo-se a ordem sucessiva de medições referentes aos compostos A, B, C e D e, em seguida, as medições referentes ao composto E, a quantidade de laudos falsos distintos que poderiam ser gerados pelo laboratório seria superior a 800.
Comentários:

Considera-se que o laboratório produz laudos falsos, para um exame dos componentes A,
B, C, D e E, sendo que para o componente E, há 3 técnicas distintas, a partir de 7 pacientes-fonte distintos para cada laudo.
Para definir os pacientes-fonte de um laudo, é preciso selecionar o paciente-fonte para os componentes A,B, C e D, conforme representado a seguir. Uma vez definidos os pacientes-fonte desses
4 componentes, os outros 3 pacientes-fonte necessariamente serão utilizados para as 3 técnicas associadas ao componente E.
A B C D

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considerando que há 7 pacientes-fontes disponíveis, há 7 possibilidades para o componente A:

A B C D

Em seguida, definido o paciente-fonte do componente A, restarão 6 possibilidades para o componente
B:

7 6

A B C D

Aplicando o mesmo raciocínio, restarão 5 pacientes-fonte para o componente C e 4 para o componente
D:

7 6 5 4

A B C D

Pelo princípio multiplicativo, o número de laudos distintos é:

Número de laudos = 7x6x5x4 = 840
Assim, o número de laudos é superior a 800.

Gabarito: Certo.

Item. 11. (CEBRASPE 2017/PM-MA) Uma operação policial será realizada com uma equipe de seis agentes,que têm prenomes distintos, entre eles André, Bruno e Caio. Um agente será o coordenador da operação e outro, o assistente deste; ambos ficarão na base móvel de operações nas proximidades do local de realização da operação. Nessa operação, um agente se infiltrará, disfarçado, entre os suspeitos, em reunião por estes marcada em uma casa noturna, e outros três agentes, também disfarçados,entrarão na casa noturna para prestar apoio ao infiltrado, caso seja necessário.
A respeito dessa situação hipotética, julgue o item seguinte.

Há mais de 100 maneiras distintas de estruturar, com os seis agentes, a equipe que realizará a operação policial.
Comentários:

Para formar a equipe, é necessário definir o coordenador, o assistente e o infiltrado,
conforme representado abaixo:
Coord

Assist

Infilt

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabendo quais agentes ocuparão essas funções, os outros 3 agentes, necessariamente,
prestarão apoio ao infiltrado. Sabendo que há 6 agentes disponíveis, há 6 possibilidades para a função de coordenador:
Coord

Assist

Infilt

Uma vez definido o coordenador, restarão 5 agentes disponíveis para a escolha do assistente:

Coord

Assist

Infilt

Definidos o coordenador e o assistente, restarão 4 opções para a escolha do agente infiltrado:

Coord

Assist

Infilt

Como devemos escolher toda a equipe, devemos multiplicar esses valores (princípio multiplicativo):

Número de maneiras = 6x5x4 = 120
Logo, há mais de 100 maneiras de formar a equipe.

Gabarito: Certo.

Item. 12. (CEBRASPE 2015/MPOG) Determinado órgão público é composto por uma diretoria geral e quatro secretarias; cada secretaria é formada por três diretorias; cada diretoria tem quatro coordenações; cada coordenação é constituída por cinco divisões, com um chefe e sete funcionários subalternos em cada divisão.
A respeito desse órgão público, julgue o item seguinte, sabendo que cada executivo e cada funcionário subalterno só pode ocupar um cargo nesse órgão.
Se, entre onze servidores previamente selecionados, forem escolhidos: sete para compor determinada divisão, um para chefiar essa divisão, um para a chefia da coordenação correspondente,um para a diretoria e um para a secretaria, haverá menos de 8.000 maneiras distintas de se fazer essas escolhas.
Comentários:

Segundo o enunciado, temos 11 servidores para ocupar os cargos de chefia de uma secretaria (SE), uma diretoria (DR), uma coordenação (CO), uma divisão (DV) e a equipe de 7 membros da divisão. Note que, uma vez definidos os 4 cargos de chefia, os 7 servidores restantes ocuparão necessariamente a equipe de 7membros da divisão.

A escolha dos 4 cargos de chefia pode ser representada da seguinte forma:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

SE DR CO DV

Para a escolha do chefe da secretaria, há 11 servidores disponíveis:

SE DR CO DV

Após a definição do SE, restarão 10 possibilidades para a chefia da diretoria:

11 10

SE DR CO DV

Em seguida, restarão 9 possibilidades para a chefia da coordenação e, posteriormente, 8
possibilidades para a chefia da divisão:
11 10 9 8

SE DR CO DV

Pelo princípio multiplicativo, temos:

Número de maneiras = 11x10x9x8 = 7.920

Logo, há menos de 8.000 maneiras.

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Permutação

Item. 1. (CEBRASPE 2022/UNB) Em uma viagem de turismo, um grupo com 18 passageiros, acompanhados de um guia turístico, serão transportados do aeroporto até o hotel em um micro-ônibus. Desses passageiros, 12 são membros da mesma família, constituída por 5 crianças e 7 adultos,sendo Paulo um dos adultos. Durante o trajeto, o guia turístico escolherá, por meio de sorteio aleatório, quatro passageiros do grupo e, a cada um deles, entregará um brinde. Considerando essa situação hipotética, julgue o item a seguir.
Caso os quatro sorteados façam o trajeto entre o aeroporto e o hotel nos quatro primeiros assentos do micro-ônibus, então a quantidade de formas diferentes de eles se sentarem, nesses assentos, é igual a 24.
Comentários:

A quantidade de maneiras de 4 pessoas se sentarem em 4 assentos corresponde à permutação de 4
elementos:

Pn = n!

P₄ = 4! = 4x3x2x1 = 24

Que é igual a 24.

Gabarito: Certo.

Item. 2. (CEBRASPE/2022 - PC/PB) Uma quadrilha especializada em roubo a bancos é composta por 5homens: o chefe, o subchefe, o especialista em explosivos, o especialista em tecnologia e o especialista em armas. A polícia descobriu que a quadrilha faria um roubo e que seus membros estariam usando máscaras com cores diferentes (preta, cinza, azul, verde e marrom), mas não descobriu quem estaria usando qual máscara. Nesse caso, é possível distribuir as máscaras entre os membros da quadrilha de a) 5 formas distintas b) 120 formas distintas c) 10 formas distintas d) 25 formas distintas e) 32 formas distintas
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

A questão pede o número de maneiras de distribuir 5 máscaras distintas para 5
pessoas, sem restrições, o que corresponde à permutação simples de 5 elementos:
P₅ = 51 = 5x4x3x2x1 = 120

Gabarito: B

Item. 3. (CEBRASPE/2022 - SECONT/ES) Após análise realizada em determinada empresa, um auditor enumerou 15 procedimentos que devem ser realizados mensalmente por alguns funcionários para a melhoria da transparência e da eficiência da empresa.
Nessa enumeração, destaca-se o seguinte:

* os procedimentos 1 a 5 são independentes entre si e podem ser realizados em qualquer ordem,
mas não simultaneamente;

* o sexto procedimento somente pode ser realizado após a conclusão dos 5 primeiros;

* as execuções dos procedimentos de 7 até 15 só podem ser realizadas quando o procedimento anterior for concluído.
Com base nessas informações, julgue o item a seguir.

A quantidade de ordens distintas de realização dos procedimentos em determinado mês é superior a
200.

Comentários:

O enunciado informa que, a cada mês, 15 procedimentos devem ser realizados. Os 5 primeiros procedimentos podem ser realizados em qualquer ordem, enquanto os demais devem seguir uma ordem específica. Assim, o número de maneiras de ordenar os procedimentos corresponde à permutação dos 5primeiros procedimentos:

P₅ = 51 = 5x4x3x2x1 = 120

Que é menor que 200.

Gabarito: Errado

Item. 4. (CEBRASPE/2022 - POLITEC/RO) João, Paulo e mais outras 3 pessoas estavam em uma fila para,individualmente, depor sobre determinado delito. Nessa fila, João estava imediatamente após Paulo.

Nessa situação hipotética, a quantidade de possíveis ordens diferentes para os depoimentos é igual a
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 10

b) 12

c) 24

d) 48

e) 120

Comentários:

Para calcular o número de possíveis ordens de uma fila de 5 pessoas, em que João está imediatamente apósPaulo, devemos tratádos como elemento único. Assim, temos a permutação de 4 elementos
(3 pessoas e a dupla como elemento único):
P₄ = 4! = 4 x 3 x2 x 1 = 24

Gabarito: C

Item. 5. (CEBRASPE/2022 - SERES/PE) Uma agência de turismo oferece passeios consistentes na visita a 12pontos turísticos da cidade de Olinda-PE, entre os quais estão as praias do Bairro Novo e da Casa
Caiada,
que são as únicas praias da lista de pontos turísticos.

A partir dessas informações, assinale a opção que apresenta o número de maneiras possíveis de organizar roteiros de visitas aos 12 pontos turísticos, tal que, se uma praia é visitada, então a segunda praia deve ser o próximo ponto turístico a ser visitado.
a) 10!

b) 2 x 3 x 10!

c) 2 x 11!

d) 12 x 11 x 10 x ...x 4x 3

e) 12!

Comentários:

Precisamos calcular o número de maneiras de ordenar 12 pontos turísticos, de modo que
2 deles (praias)
estejam sempre juntos em qualquer ordem.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O primeiro passo é tratar as praias como elemento único. Assim, temos a permutação de
11 elementos (10
pontos turísticos e o as 2 praias como elemento único):

Pu = 11!

Para cada uma dessas possibilidades, há 2 maneiras de ordenar as praias (primeiro
Bairro Novo e depois Casa
Caiada ou primeiro Casa Caiada e depois Bairro Novo). Pelo princípio multiplicativo,
devemos multiplicar o resultado da permutação por 2:
n = 2 x 11!

Gabarito: C

Item. 6. (CEBRASPE/2022 - SEE/PE) As festas juninas são festas tradicionais que ocorrem em todo o país e possuem, além de muita comida e dança, brincadeiras e competições. Por isso, são ambientes excelentes para problemas de contagem e probabilidade e para estudos de fenômenos aleatórios. Com relação a esse tema, julgue o item que se segue.
Situação hipotética: Para determinada apresentação de dança de quadrilha, quatro homens e quatro mulheres devem ficar em fila, de modo que a primeira e a última pessoa da fila sejam mulheres. Assertiva:Nesse caso, há 8.640 formas distintas de organizar essa fila.

Comentários:

Precisamos calcular o número de maneiras de enfileirar 8 pessoas, sendo 4 mulheres e
4 homens, de modo que as extremidades sejam ocupadas por mulheres:
M M

Assim, há 4 possibilidades para a primeira posição e 3 possibilidades para a última posição. Em relação às posições centrais, em que não há restrições, temos a permutação de 6 elementos:
P₆ = 6! = 6 x 5x4x3 x2 x 1 = 720

Pelo princípio multiplicativo, o número de maneiras de organizar toda a fila
(eventos concomitantes) é o produto:
n = 4 x 3 x 720 = 8640

Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 7. (CEBRASPE/2022 - TELEBRAS) Julgue o item que se segue, a respeito de contagem,
probabilidade e estatística.
Considere que três amigos farão uma dinâmica de grupos e precisarão se sentar em uma roda com outras 5pessoas. Considere ainda que os três amigos fazem questão de ficarem juntos. Nessa situação, a roda poderá ser formada de 720 maneiras distintas, sem haver repetição das posições.
Comentários:

Essa questão trabalha com uma permutação circular, com restrições. A permutação circular de n elementos é dada por:
PCn = (n- 1)!

Isso porque consideramos que as posições em um círculo se modificam apenas quando a posição das pessoas em relação às outras se modificam. Em outras palavras, um simples giro da mesa não é considerado uma nova maneira de se organizar as pessoas. Assim, podemos imaginar em posicionar uma pessoa em qualquer lugar do círculo e permutar as outras n — 1.
A questão informa que 3 amigos irão se sentar com outras 5 pessoas em uma roda.
Como os amigos precisam ficar juntos, vamos considerá-los como um único elemento, por ora. Assim, temos a permutação circular de6 elementos (5 pessoas + amigos como elemento único):

PC₆ = 5! = 5 x 4 x 3 x 2 x 1 = 120

Como os 3 amigos ficarão juntos, mas em qualquer ordem, a forma de reordená-los corresponde à permutação de 3 elementos:
P₃ = 31 = 3x2x1 = 6

Pelo princípio multiplicativo, devemos multiplicar essas possibilidades:

n = 6 x 120 = 720

Gabarito: Certo.

Item. 8. (CEBRASPE/2022 - Pref. Maringá) Durante um treinamento de 10 servidores,
realizou-se uma dinâmica em que se dividiram os participantes em cinco duplas. Todos tiveram de sentar-se em uma mesa circular para realizar a atividade. Nessa situação hipotética, a quantidade de maneiras possíveis para que cada dupla sente-se à mesa sempre junta é igual a a) 24
b) 45

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) 768

d) 362.880

Comentários:

Precisamos sentar 5 duplas de servidores em uma mesa circular, de modo que cada dupla fique junta. Para isso, vamos primeiro tratar cada dupla como elemento único. Assim, temos uma permutação circular de 5elementos:

PC₅ = 4! = 4 x 3 x 2 x 1 = 24

Para cada possibilidade, há 2 possibilidades para cada uma das 5 duplas se organizar. Logo, devemos multiplicar o resultado por 2x2x2x2x2:
n = 24 x2x2x2x2x2 = 768

Gabarito: C

Item. 9. (CEBRASPE 2021/SERPRO) Suponha que sejam gerados 5 números válidos de CPF
para serem atribuídos a 5 indivíduos distintos. Com base nessas informações, julgue o item a seguir.
A quantidade de formas de se fazer a atribuição desses CPFs a esses indivíduos é maior que 100.

Comentários:

A quantidade de maneiras de distribuir 5 CPFs para 5 indivíduos corresponde à permutação de 5
elementos:

P₅ = 51 = 5x4x3x2x1 = 120

Que é maior que 100.

Gabarito: Certo.

Item. 10. (CEBRASPE 2021/CBM-TO) Determinado veículo de combate a incêndios, que tem seus assentos numerados, tem capacidade para transportar 5 soldados, incluindo-se o motorista. Se 5militares são designados para trabalhar com esse veículo e somente 2 deles podem dirigi-lo, então a quantidade de formas diferentes que eles podem ocupar os assentos do veículo é igual a a) 6
b) 10

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) 48

d) 120

Comentários:

Segundo o enunciado, há 5 pessoas para se sentarem em um veículo com 5 lugares distintos (numerados),mas apenas 2 podem dirigir. Assim, há 2 possibilidades para o motorista. Após a escolha do motorista, temos a permutação de 4 pessoas em 4 lugares:
Pelo princípio multiplicativo, temos:

2 xP₄ = 2 x4! = 2x4x3x2x1 = 48

Gabarito: C.

Item. 11. (CEBRASPE 2021/IBGE) Considere que a figura a seguir — que consiste de um retângulo maior subdividido em 45 retângulos menores, no qual estão destacados os pontos A, B e C; ao lado do retângulo maior estão indicadas as direções norte (N), sul (S), leste (L) e oeste (O) —representa um mapa, fora de escala, de parte de uma cidade onde será realizada uma pesquisa domiciliar.
M

záfex

As linhas retas representam as ruas, e os quarteirões são os retângulos menores, que medem 300
metros na direção oeste-leste e 60 metros na direção sul-norte. Durante os trabalhos, cada agente de pesquisas e mapeamento (APM), que sairá necessariamente do ponto A, somente pode caminhar nos sentidos oeste-leste ou sul-norte.

Tendo como referência o texto acima e observando-se a regra de que os deslocamentos apenas podem ser executados nos sentidos oeste-leste ou sul-norte, verifica-se que o número de caminhos distintos que podem ser percorridos por um APM para se deslocar do ponto A ao ponto C, passando pelo ponto B, é igual a
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 14

b) 49

c) 56

d) 735

e) 2.002

Comentários:

A questão informa que precisamos ir do ponto A ao ponto B e em seguida do ponto B
ao ponto C, utilizando as linhas verticais e horizontais.
Entre o ponto A e o ponto B, há 4 segmentos de reta verticais e 3 segmentos de reta horizontais. Isso significa que para irmos de um ponto a outro, precisamos efetuar 4 movimentos para cima e 3movimentos para a direita. Para ilustrar, vamos representar por N (Norte) o movimento para cima e por L(Leste) o movimento para a direita. Assim, a sequência N L N N L L N corresponde ao seguinte caminho:

T

A*

Em outras palavras, os diferentes caminhos podem ser representados por sequências com 4
Ns e 3 Ls em alguma ordem. Logo, a quantidade de caminhos diferentes entre A e B corresponde ao número de maneiras de reordenar 4 Ns e 3 Ls, que por sua vez corresponde à permutação de 7 elementos,com repetição de 4 e de 3elementos:
P?
P4 x P3

7!

4! x 3!

7x6x5x41 7x6x5

4! x 3! " 3x2x1 - 7 x 5 - 35

Com relação ao caminho entre B e C, há 5 segmentos de reta verticais e 2 segmentos de reta horizontais. Ou seja, esse caminho pode ser representado por sequências com 5 Ns e 2 Ls, de modo que a quantidade de caminhos diferentes corresponde a uma permutação de 7 elementos, com repetição de 5 e de 2elementos:

5„2P₇ 7! 7x6x5! 7x6

p ' = í = =
= = 7 v 3 = 21

7 P₅*P₂ 5! x 2! 5! x 2! 2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considerando que precisamos percorrer ambos os caminhos (de A até B E de
B até C), pelo princípio multiplicativo, precisamos multiplicar as possibilidades:
35x 21 = 735

Gabarito: D

Item. 12. (CEBRASPE 2018/PF) Os indivíduos Sl, S2, S3 e S4, suspeitos da prática de um ilícito penal, foram interrogados, isoladamente, nessa mesma ordem. No depoimento, com relação à responsabilização pela prática do ilícito, Sl disse que S2 mentiria; S2 disse que S3 mentiria; S3 disse queS4 mentiria. A partir dessa situação, julgue o item a seguir.
Se os quatro suspeitos tiverem nascido nos estados da Bahia, de Pernambuco, do Rio de
Janeiro e de São
Paulo, cada um em um estado diferente, e atualmente residirem nesses mesmos estados,
ainda que alguns deles possam ter se mudado de um estado para outro, a quantidade de possibilidades de naturalidade e residência dos acusados é inferior a 100.
Comentários:

A questão pede o número de maneiras de "alocar" os 4 suspeitos nos estados em que nasceram e nos estados em que residem. Sabendo que cada um dos 4 suspeitos nasceu em dos 4 estados,diferente do outro, temos uma permutação de 4 elementos:
P₄ = 4! = 4x 3 x2 x 1 = 24

Similarmente, sabendo que cada um dos 4 suspeitos reside em um dos 4 estados,
diferente do outro, temos outra permutação de 4 elementos:
P₄ = 4! = 4 x3 x 2 x 1 = 24

O número de possibilidades de naturalidade e residência é, portanto:

Número de possibilidades = 24 x 24 = 576
Logo o número de possibilidades é muito superior a 100.

Gabarito: Errado.

Item. 13. (CEBRASPE 2018/BNB) Julgue o próximo item, relativo à análise combinatória e probabilidade.
A quantidade de maneiras distintas de 5 meninos e 4 meninas serem organizados em fila única de forma que meninos e meninas sejam intercalados e 2 meninos ou 2 meninas nunca fiquem juntos é inferior a3.000.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Deseja-se formar uma fila com 5 meninos e 4 meninas, de modo que meninos (O) e meninas (A) fiquem intercalados:
OAOAOAOAO

Observe que necessariamente o primeiro da fila será um menino (O), pois há um menino a mais, de modo que, se começássemos com uma menina, teríamos meninos juntos (não intercalados) no final da fila.
O número de maneiras distintas de organizar os 5 meninos nessas posições corresponde à permutação de 5elementos:

P₅ = 5! = 5 x 4 x 3 x 2 = 120

O número de maneiras distintas de organizar as 4 meninas nessa posição, corresponde à permutação de 4elementos:

P₄ = 4! = 4 x 3 x2 x 1 = 24

Pelo princípio multiplicativo, devemos multiplicar essas possibilidades:

Número de maneiras = 120 x 24 = 2.880

Ejse número é inferior a 3.000.

Gabarito: Certo.

Item. 14. (CEBRASPE 2018/SEFAZ-RS) Sete pessoas se dirigem para formar uma fila em frente ao único caixa de atendimento individual em uma agência bancária. Dessas sete pessoas, quatro são idosos. Um servidor da agência deverá organizar a fila de modo que os idosos sejam atendidos antes dos demais.
Nessa situação, a quantidade de maneiras distintas de se organizar a fila é igual a a) 5.040.
b) 720.

c) 576.

d) 288.

e) 144.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Podemos representar a fila de 7 pessoas, sabendo que todos os 4 idosos deverão ser atendidos antes dos demais, da seguinte forma:
Y

4 idosos

Y

outras 3 pessoas

Para organizar os 4 idosos, temos uma permutação de 4 elementos:

P₄ = 4! = 4 x 3 x 2 x 1 = 24

Para organizar as outras 3 pessoas, temos uma permutação de 3 elementos:

P₃ = 3! = 3 x2x 1 = 6

Considerando que temos que organizar toda a fila, devemos multiplicar esses resultados (princípio multiplicativo):
Número de maneiras de organizar a fila = 24 x 6 = 144

Gabarito: E.

Item. 15. (CEBRASPE 2018/FUB) Considerando que 4 livros de matemática e 6 livros de física devam ser acomodados em uma estante, de modo que um fique ao lado do outro, julgue o item seguinte.
A quantidade de maneiras distintas de se acomodar esses livros na estante de forma que os livros de matemática fiquem todos à esquerda dos livros de física é igual a 720.
Comentários:

Precisamos acomodar 4 livros de matemática à esquerda de 6 livros de física:

k

Y

4 de matemática

V 7

6 de física

Para acomodar os 4 livros de matemática, temos uma permutação de 4 elementos:

= 4! = 4 x3 x 2 x 1 = 24

Para acomodar os 6 livros de física, temos uma permutação de 6 elementos:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

P₆ = 6! = 6 x 5x4x3 x2 x 1 = 720

Como devemos acomodar todos os dez livros, precisamos multiplicar esses resultados:

Número de possibilidades = 24 x 720
Logo, o número de maneiras de organizar a estante é muito superior a 720.
Gabarito: Errado.

Item. 16. (CEBRASPE 2017/PM-MA) Uma operação policial será realizada com uma equipe de seis agentes,que têm prenomes distintos, entre eles André, Bruno e Caio. Um agente será o coordenador da operação e outro, o assistente deste; ambos ficarão na base móvel de operações nas proximidades do local de realização da operação. Nessa operação, um agente se infiltrará, disfarçado, entre os suspeitos, em reunião por estes marcada em uma casa noturna, e outros três agentes, também disfarçados,entrarão na casa noturna para prestar apoio ao infiltrado, caso seja necessário. A respeito dessa situação hipotética,julgue o item seguinte.

A quantidade de maneiras distintas de formar a equipe, de modo que André, Bruno e
Caio sejam os agentes que prestarão apoio ao infiltrado, é inferior a 10.
Comentários:

Considerando que André, Bruno e Caio serão os agentes que prestarão apoio ao infiltrado, então será necessário definir o coordenador, o assistente e o infiltrado, isto é, as 3 funções distintas, dentre os 3 agentes que restaram. Assim, o número de maneiras distintas de formar a equipe corresponde ao número de formas de reordenar os 3 elementos, ou seja, à permutação de 3 elementos:
P₃ = 31 = 3x2x1 = 6

Logo, o número de maneiras distintas de formar a equipe é inferior a 10.

Gabarito: Certo.

Item. 17. (CEBRASPE 2016/CBM-DF) Para atender uma grave ocorrência, o comando do corpo de bombeiros acionou 15 homens: 3 bombeiros militares condutores de viatura e 12 praças combatentes,que se deslocaram em três viaturas: um caminhão e duas caminhonetes. Cada veículo transporta até 5 pessoas,todas sentadas, incluindo o motorista, e somente os condutores de viatura podem dirigir uma viatura.Com relação a essa situação, julgue o item seguinte.

Escolhidos o condutor da viatura e os 4 praças que seguirão em determinada viatura, a quantidade de maneiras distintas de eles ocuparem os assentos dessa viatura será inferior a 25.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Após a escolha do condutor e dos 4 praças que estarão em determinada viatura, a quantidade de maneiras distintas de eles ocuparem os assentos da viatura corresponde a uma permutação de 4elementos, uma vez que o condutor já está definido.
= 4! = 4 x3 x 2 x 1 = 24

Logo, a quantidade de maneiras é inferior a 25.

Gabarito: Certo.

Item. 18. (CEBRASPE 2016/CBM-DF) Para atender uma grave ocorrência, o comando do corpo de bombeiros acionou 15 homens: 3 bombeiros militares condutores de viatura e 12 praças combatentes,que se deslocaram em três viaturas: um caminhão e duas caminhonetes. Cada veículo transporta até 5 pessoas,todas sentadas, incluindo o motorista, e somente os condutores de viatura podem dirigir uma viatura.Com relação a essa situação, julgue o item seguinte.

A quantidade de maneiras distintas de serem distribuídos os 15 homens no interior das três viaturas é igual a 6 x 121.
Comentários:

Para distribuir os 15 homens no interior das 3 viaturas, é necessário distribuir os 3
condutores, E, em seguida,
os 12 praças.

Considerando que há 3 condutores para 3 veículos, a quantidade de maneiras de distribuí-los corresponde a uma permutação de 3 elementos:
P₃ = 31 = 3x2x1 = 6

Sabendo que cada veículo transporta até 5 pessoas, incluindo o motorista, então, me cada veículo, cabem 4não condutores. Logo, para os 3 veículos, há 3 x 4 = 12 posições para não condutores. Considerando que há
12 praças para 12 posições, a quantidade de maneiras distintas de distribuí-los corresponde à permutação de 12 elementos:
= 12!

Pelo princípio multiplicativo, devemos multiplicar esses resultados, por serem concomitantes:

Número de maneiras = 6 x 12!

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Arranjo e Combinação

Item. 1. (CEBRASPE 2022/FUNPRESP-EXE) A seguir, são apresentadas informações obtidas a partir de uma pesquisa realizada com 1.000 pessoas.
* 480 possuem plano de previdência privada;

* 650 possuem aplicações em outros tipos de produtos financeiros;

* 320 não possuem aplicação em nenhum produto financeiro.

Com base nessa situação hipotética, julgue o item seguinte.

Considere que, do grupo de 1.000 pessoas que participaram da pesquisa, será formada uma comissão composta por dois membros, um titular e um suplente, sendo escolhido primeiro o membro titular e, em seguida, o membro suplente. Nessa situação, é possível formar mais de um milhão de comissões distintas.
Comentários:

Nessa questão, temos 1000 pessoas, das quais 2 serão escolhidas para cargos diferentes na comissão.Considerando que a ordem importa, temos o arranjo de 2 elementos, dentre 1000:

^1000,2

1000!

(10-2)!

1000!

98!

1000 x 999 x 998!

----------- —— = 1000 x 999 = 999.000

Que é menor que 1.000.000.

Gabarito: Errado

Item. 2. (CEBRASPE 2022/UNB) Considerando que, na unidade de pronto-socorro de um hospital, quatro médicos façam atendimento aos pacientes e que haja a mesma probabilidade de esses pacientes serem atendidos por qualquer um desses médicos, julgue o item.
Se os amigos Jair, Ana e Patrícia estiverem em uma fila que tenha 12 pacientes,
então a quantidade de diferentes posições que esses três amigos poderão ocupar na fila é inferior a 1.200.
Comentários:

A questão pede o número de maneiras que os 3 amigos podem ocupar posições na fila.
Podemos entender essa questão como a seleção de 3 posições na fila para os diferentes amigos, isto é,com importância de ordem. Logo, temos o arranjo de 3 elementos, dentre 12:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

12!

(12-3)!

12! 12x11x10x9!

— = = 12 x 11 x 10 = 1320

Que é superior a 1200. Observe que não temos uma permutação dos 12
elementos, pois não estamos interessados nas posições das demais pessoas, apenas dos 3 amigos.
Gabarito: Errado

Item. 3. (CEBRASPE 2022/Telebras) João vai receber líquidos R$ 3.300,00 por salário, e decidiu que vai usar70% de sua renda com despesas pessoais e aplicar o restante. Dos recursos que destinará a aplicações,investirá 25% em ações de empresas listadas na bolsa brasileira, 25% em títulos de renda fixa, 25% em fundos de investimento imobiliário e o restante em ativos lastreados em dólar. Seus estudos indicaram dez empresas boas pagadoras de dividendos, com boa liquidez e cujas ações estão com bom preço. Com base nessa situação hipotética, julgue o item a seguir.
Se inicialmente João começar adquirindo ações de duas empresas dentre aquelas consideradas boas pagadoras de dividendos, com boa liquidez e cujas ações estão com bom preço, há mais de 50 maneiras deJoão escolher as duas que serão compradas.

Comentários:

O enunciado informa que há 10 empresas, das quais 2 serão selecionadas para João começar investindo.Como o investimento será nas duas empresas ao mesmo tempo, isto é, sem importância de ordem, temos a combinação de 2 elementos, dentre 10:
n!

^n,p (n — py. x p\

10! 10x9x8! 10x9

Cl0'2 " (10 - 2)! x 2! " 8! x 2! " 2 " 45

Que é menor que 50.

Gabarito: Errado.

Item. 4. (CEBRASPE 2022/UNB) Em uma viagem de turismo, um grupo com 18 passageiros, acompanhados de um guia turístico, serão transportados do aeroporto até o hotel em um micro-ônibus. Desses passageiros, 12 são membros da mesma família, constituída por 5 crianças e 7 adultos,sendo Paulo um dos adultos. Durante o trajeto, o guia turístico escolherá, por meio de sorteio aleatório, quatro passageiros do grupo e, a cada um deles, entregará um brinde. Considerando essa situação hipotética, julgue o item a seguir.
A quantidade de possibilidades distintas de o guia turístico escolher quatro pessoas diferentes do grupo de passageiros é superior a 3.000.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

O enunciado informa que há 18 passageiros, dos quais 4 serão escolhidos para receberem um brinde.

Considerando que não há diferença entre os brindes, ou seja, considerando que a ordem da seleção não importa, temos a combinação de 4 elementos, dentre 18:
18! 18x17x16x15x14! 18x17x16x15

Cl8'4 (18 —4)!x4!

14! x 4!

4 x 3 x 2 x 1

18 x 17 x l\x't5

= VSxXxl = 18 X 17 X 2 X 5 = 3060

Que é superior a 3000.

Gabarito: Certo.

Item. 5. (CEBRASPE 2022/Telebras) Uma empresa dispõe de dez funcionários, dos quais selecionará quatro para montar uma equipe para a realização de determinada tarefa, todos com igual função nessa tarefa.Márcio e Marcos são muito amigos e, quando trabalham juntos, costumam conversar demasiadamente,prejudicando a produtividade. Pedro e Paulo são desafetos, não trocam entre si nem mesmo as comunicações essenciais para o desempenho da tarefa, prejudicando também a produtividade.
No que se refere a essa situação hipotética, julgue o item que se segue.

Desconsiderando os riscos de prejuízos à produtividade, há mais de 250 maneiras de a equipe ser montada.
Comentários:

O item pede o número de possibilidades de escolher uma equipe de 4 funcionários,
dentre 10. Considerando que as tarefas serão iguais, ou seja, a ordem da seleção não importa, temos a combinação de 4 elementos dentre 10:
10!

Cl0'4 (10- 4)!x4!

10x9x8x7x6! 10x9x8x7

6! x 4! 4 x 3 x 2 x 1

10 x^X/g x 7

Ci1U04 = —7- = 10 x 3 x 7 = 210

' ^x/x/xl

Que é menor que 250.

Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (CEBRASPE/2022 - MP TCE/SC) Dada uma equipe de dez servidores, entre eles Alberto e
Bruna, W
é o conjunto de todas as listas que podem ser formadas com exatamente três servidores.

A partir das informações anteriores, e sabendo que, nessa hipótese, A é o conjunto de todas as listas em que consta o nome de Alberto e B, o conjunto daquelas em que consta o nome deBruna, julgue o item que se segue.
W contém mais de cem elementos.

Comentários:

O número de maneiras de selecionar 3 pessoas para compor uma lista, dentre
10 pessoas no total,
corresponde à combinação de 10 escolhe 3:

10!

Cl0'3 " (10 - 3)! x 3!

10 x 9 x 8 x 7!

7! x 3!

10 x 9 x 8

—-—-— = 10 x 3 x 4 = 120

Que é maior que 100.

Gabarito: Certo

Item. 7. (CEBRASPE/2022 - PC/RO) De um conjunto de 10 técnicos em necropsia, 4 serão selecionados para um treinamento especial.
Considerando essa hipótese, a quantidade de maneiras que esta delegação de 4 técnicos poderá ser formada é igual a a) 40
b) 210

c) 256

d) 5040

e) 10.000

Comentários:

O número de maneiras de selecionar 4 pessoas para formar uma comissão, dentre 10
pessoas no total,
corresponde à combinação de 10 escolhe 4:

10! 10x9x8x7x6! 10x9x8x7

C104 = - = =
= 10 x 3 x 7 = 210

10,4 (10 - 4)! x 4! 6! x 4! 4x3x2

Gabarito: B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 8. (CEBRASPE/2022 - BNB) Certo banco dispõe de uma equipe de 12 analistas de sistema, da qual fazem parte Antônio e Maria. Para atendimento de determinada demanda, o chefe do setor montará uma comissão com 5 analistas, todos com a mesma função.
Com base nessa situação hipotética, julgue o item seguinte.

Há mais de 800 maneiras de selecionar os analistas que comporão a comissão.

Comentários:

O número de maneiras de selecionar 5 analistas para compor a comissão, dentre 12 no total, corresponde à combinação de 12 escolhe 5:
12! 12x11x10x9x8x7! 12x11x10x9x8

Cl2'5 ~ (12 - 5)! x 5! 7! x 5! 5 x 4x 3 x 2
-11x9x8 -792

Que é menor que 800.

Gabarito: Errado

Item. 9. (CEBRASPE/2022 - BNB) Certo banco dispõe de uma equipe de 12 analistas de sistema, da qual fazem parte Antônio e Maria. Para atendimento de determinada demanda, o chefe do setor montará uma comissão com 5 analistas, todos com a mesma função.
Com base nessa situação hipotética, julgue o item seguinte.

O número de maneiras de montar comissões em que Antônio e Maria não participem juntos é superior a
600.

Comentários:

Para calcular o número de maneiras de montar uma comissão, sem que Antônio e Maria participem juntos,vamos subtrair, do total de comissões, aquelas em que Antônio e Maria participem juntos.

No item anterior, calculamos o total de comissões:

12!

Cl2'5 " (12 - 5)! x 5!

12 x 11 x 10 x 9 x 8 x 7!

7! x 5!

12 x 11 x 10 x 9 x 8

5 x 4 x 3 x 2

11 x 9 x 8 = 792

Para que Antônio e Maria participem juntos, é necessário escolher outros 3
membros para a comissão,
dentre os 10 analistas disponíveis, o que corresponde à combinação de 10 escolhe 3:

10!

=
10'3 (10 - 3)! x 3!

10 x 9 x 8 x 7!

7! x 3!

10 x 9 x 8

---------------- = 10 x 3 x 4 = 120

3x2

E o número de comissões que atendem à restrição é a diferença:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

n = 792 - 120 = 672

Que é superior a 600.

Gabarito: Certo

Item. 10. (CEBRASPE/2022 - BNB) Certo banco dispõe de uma equipe de 12 analistas de sistema, da qual fazem parte Antônio e Maria. Para atendimento de determinada demanda, o chefe do setor montará uma comissão com 5 analistas, todos com a mesma função.
Com base nessa situação hipotética, julgue o item seguinte.

Se o chefe decidir não convocar Antônio nem Maria, haverá mais de 250 maneiras de selecionar a comissão.
Comentários:

Agora, precisamos calcular o número de comissões possíveis sem Antônio e sem Maria.
Nessa situação,
precisamos escolher 5 analistas, dentre os outros 10:

10! 10x9x8x7x6x5! 10x9x8x7x6

Qo.s (10 _ 5)J x 5! -

5ri!rix 5!

— C/iqq5—x4x23xx92x2x7 —

Que é superior a 250.

Gabarito: Certo

Item. 11. (CEBRASPE 2022/Petrobrás) Uma empresa distribuidora de combustíveis atendia, ao término do ano de 2020, apenas 30 clientes. Após a implementação de medidas administrativas, a quantidade de novos clientes dessa empresa, no primeiro semestre de 2021 (contada sempre em relação ao mês anterior), aumentou em progressão geométrica. Na tabela a seguir, está registrada a quantidade total de clientes da empresa no final dos 4 primeiros meses de 2021.
Total de Clientes da Empresa

Meses Janeiro 2021 Fevereiro 2021 Março 2021 Abril 2021

Total de Clientes 32 36 44

Com base nessa situação hipotética e nos dados apresentados na tabela, julgue o item a seguir.

Supondo-se que, no final de março de 2021, três clientes devessem ter sido aleatoriamente escolhidos para responder a um questionário de avaliação da empresa, então a quantidade de formas diferentes de fazer essa escolha, de modo que, no grupo escolhido, houvesse pelo menos 2 clientes que tivessem ingressado na empresa antes de 2021, é inferior a 4.000.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O item pede o número de maneiras de selecionar 3 clientes ao final de março de
2021, de modo que pelo menos 2 clientes tenham ingressado antes de 2021, ou seja, de modo que 2 ou 3clientes tenham ingressado antes.
A tabela informa que há 44 clientes ao final de março de 2021 e o enunciado informa que havia 30 clientes ao final de 2020. Logo, o número de maneiras de selecionar 3 clientes, todos os quais tenham ingressado antes de 2021, corresponde à combinação de 3 elementos, dentre 30:
r 30! 30 x 29 x 28 x 27!

n(3) - 630,3 - (-30 _ 3)j x 3! - 27! x 3!

30 x 29 x 28

——-—— = 5 x 29 x 28 = 4060

3x2x1

Ademais, para selecionarmos exatamente 2 clientes que tenham ingressado antes de 2021,
multiplicamos o número de possibilidades de selecionar 2 clientes, dentre os 30 que ingressaram antes,pelo número de possibilidades de selecionar 1 cliente, dentre os 44 - 30 = 14 clientes que ingressaram ao longo de 2021.Portanto, primeiro temos a combinação de 2 elementos dentre 30:

630,2

30! 30 x 29 x 28!

(30 - 2)! x 2! 28! x 2!

30 x 29

----- - ----- = 15 x 29 = 435

E multiplicamos esse resultado pelas 14 maneiras de selecionar um cliente dentre os 14
novos:

n(2) = 14 x 435 = 6090

E 0 número de possibilidades associada a uma situação OU outra corresponde à soma das possibilidades:n(2 ou 3) = 6090 + 4060 = 10150

Que é superior a 4.000.

Gabarito: Errado

Item. 12. (CEBRASPE 2022/Petrobrás)

No plano cartesiano Oxy da figura precedente, estão marcados 8 pontos distintos no primeiro quadrante,cujas coordenadas são:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A = (1, a); B = (1, b); C = (1, c); D = (1, d)

E = (2, e); F = (2, f); G = (2, g); H = (2, h)

A partir dos dados apresentados, julgue o item subsequente.

O número de triângulos que se pode formar com vértices nos pontos dados é maior que 50.

Comentários:

Para formar um triângulo, precisamos de 3 vértices, sendo um dos vértices em uma das linhas e outros dois vértices na outra linha.
Vamos primeiro selecionar 1 vértice na primeira linha e 2 vértices na segunda linha.
Considerando que há 4
vértices na primeira linha, há 4 possibilidades de selecionarmos um vértice na primeira linha. Para selecionarmos 2 vértices da segunda linha, de um total de 4 vértices também, temos a combinação de 2elementos, dentre 4:

4! 4x3x2! 4x3 r

C4'2 (4-2)! x 2! 2! x 2! " 2 " 6

Pelo princípio multiplicativo, o número de maneiras de selecionarmos 1 vértice na primeira linha E 2 vértices na segunda linha é o produto dessas possibilidades:
4 x 6 = 24

Agora, devemos calcular o número de maneiras de selecionar 2 vértices na primeira linha e 1 vértice na segunda. Como ambas as linhas apresentam o mesmo número de vértices possíveis, também teremos 24possibilidades de selecionar o triângulo dessa forma.

Como são eventos mutuamente exclusivos, o número de possibilidades de selecionar o triângulo uma forma
OU de outra é a soma dessas possibilidades (princípio aditivo):

24 + 24 = 48

Que é menor que 50.

Gabarito: Errado

Item. 13. (CEBRASPE/2022 - BANRISUL) De acordo com o organograma do BANRISUL, existem sete diretorias ligadas diretamente à Presidência dessa instituição, entre as quais se incluem a DiretoriaAdministrativa e a Diretoria de Tecnologia da Informação e Inovação. Para aumentar a eficiência, 28funcionários foram enviados para o centro de treinamento da empresa, tendo sido quatro funcionários escolhidos por cada uma das sete diretorias.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com base na situação hipotética anterior, julgue o próximo item, relacionado aos 28 funcionários enviados para o centro de treinamento da empresa.
O número de maneiras diferentes de formar duas equipes com 14 funcionários cada, de modo que os quatro funcionários da Diretoria Administrativa estejam na mesma equipe, é inferior a ——.
Comentários:

2410

Para dividir os funcionários em duas equipes de 14 membros, podemos escolher os funcionários para uma das equipes, pois os que restarem formarão necessariamente a outra equipe.Considerando que 4
funcionários específicos devem estar na mesma equipe, precisamos escolher os outros 10
funcionários da equipe, dentre os 24 funcionários remanescentes:
24! 24! 24 x 23 x 22 x 21 x 20 x 19 x 18 x 17 x 16 x 15

C24'10 (24-10)! x 10! " 14! X 10! _
10!

2410

Agora, precisamos comparar esse resultado com No denominador, temos 10! em ambas as frações.

Ademais no numerador do nosso resultado temos o produto de 10 números, sendo um deles igual a 24 e os demais menores que 24. Assim, esse produto é necessariamente menor do que 2410, que corresponde ao produto de 10 números iguais a 24.
2410Portanto, de fato, o resultado é inferior a .

' ' (10!)

Gabarito: Certo

Item. 14. (CEBRASPE/2022 - SEE/PE) O triângulo aritmético, apresentado por Pascal em sua obra Traité duTriangle Arithmétique (1665), ilustrado a seguir, mostra uma tabela cuja primeira linha é formada com todos os elementos iguais a 1. A partir da segunda linha, os elementos são obtidos como soma de todos os elementos da linha precedente situados exatamente acima ou à esquerda do elemento desejado.
1 1 1

1 2 3

1 3 6

1 4 10

1 5 15

1 - -

1 1

4 5

10 15

20 35

35 70

- -

-

-

Com base nas informações e na tabela anteriores, julgue o item a seguir.

Na tabela, o elemento situado na décima coluna da sexta linha é maior que 2.000.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Essa tabela é uma forma alternativa de apresentar o triângulo de Pascal, que normalmente é apresentado da seguinte maneira:
G),o

G,o Cl,l

^2,0 C2,l C2t2

^3,1 £3,2 C33

£4,0 C44 £4,2 £*4,3 C4)4

£5,0 C54 Cs,2 C5 3 C5 4

1 1

12 1

13 3 1

1 4 6 4 1

1 5 10 10 5 1

As linhas da tabela correspondem às colunas do triângulo de Pascal, a partir do número 1. Considerando que as colunas do triângulo iniciam sempre uma linha depois da anterior, então, ao longo de uma mesma linha da tabela, há um aumento tanto no valor de n quanto no valor de k da combinação:
Q),o

Q,o

^2,0

£3,0

Q,o

C14

C24

C3,l
C44

Cs.i

C*2,2

^3,2

£4,2

C5,2

Q,2

^3,3

Cl,3

^5,3

Q,3

G,3

G,4

Q,4

Q,4
C*7,4
Cs,4

Assim, o elemento da linha i e coluna j representa a combinação Cnk, sendo n = i+j
— 2ek=j — 1. Essas subtrações são necessárias porque a tabela começa com n = 0 e k = 0.
Portanto, na linha i = 6 e coluna j = 10, temos:

n = 6 + 10 — 2 = 14

k = 10 - 1 = 9

O valor dessa combinação é:

14!

Cl4'9 " (14-9)! x 9!

14 x 13 x 12 x 11 x 10 x 9!

5! x 9!

14 x 13 x 12 x 11 x 10

5 x 4 x 3 x 2

14 x 13 x 11 = 2002

Gabarito: Certo

Item. 15. (CEBRASPE 2021/COREN-SE) Considere que, para realizar os procedimentos de vacinação, uma equipe tenha sido formada por três técnicos de enfermagem para exercer funções distintas. Um deles é responsável por registrar as informações do paciente nos sistemas; outro, por preparar a dose; e o terceiro,por aplicar.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considere ainda que um centro de saúde disponha de dez técnicos, todos igualmente hábeis nessas três funções. A propósito dessa situação hipotética, assinale a opção correspondente à quantidade de maneiras distintas que uma equipe pode ser formada.
a) 30.

b) 120.

c) 1.000.

d) 720.

Comentários:

A questão informa que há 10 profissionais, dos quais 3 serão selecionados para realizar funções distintas.
Como a ordem da seleção importa, devemos utilizar o arranjo de 3 elementos dentre 10:

n!

n'k = (n-k)!

?l10'3 _ (10-3)!

10!

10! 10x9x8x7!

— = = 10 x 9 x 8 = 720

Gabarito: D.

Item. 16. (CEBRASPE 2022/Telebras) Uma empresa dispõe de dez funcionários, dos quais selecionará quatro para montar uma equipe para a realização de determinada tarefa, todos com igual função nessa tarefa.Márcio e Marcos são muito amigos e, quando trabalham juntos, costumam conversar demasiadamente,prejudicando a produtividade. Pedro e Paulo são desafetos, não trocam entre si nem mesmo as comunicações essenciais para o desempenho da tarefa, prejudicando também a produtividade.No que se refere a essa situação hipotética, julgue o item que se segue.
Há 4! maneiras de montar uma equipe com a participação de Márcio, Marcos, Pedro e Paulo.

Comentários:

O enunciado informa que serão selecionados 4 funcionários para uma equipe. Como as tarefas serão as mesmas, então a ordem da seleção não importa. Logo, há uma única maneira de montar uma equipe Márcio,Marcos, Pedro e Paulo.

Se preferir, podemos calcular a combinação de 4 elementos, dentre 4:

4! 4!

C4'4 (4-4)! x 4! " 0! X 4! _ 1

Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 17. (CEBRASPE 2022/Telebras) Uma empresa dispõe de dez funcionários, dos quais selecionará quatro para montar uma equipe para a realização de determinada tarefa, todos com igual função nessa tarefa.Márcio e Marcos são muito amigos e, quando trabalham juntos, costumam conversar demasiadamente,prejudicando a produtividade. Pedro e Paulo são desafetos, não trocam entre si nem mesmo as comunicações essenciais para o desempenho da tarefa, prejudicando também a produtividade.No que se refere a essa situação hipotética, julgue o item que se segue.
O número de maneiras de se montar uma equipe em que Márcio e Marcos participem é inferior a 20.

Comentários:

O número de maneiras de montar uma equipe de 4 pessoas das quais partcipem Márcio e Marcos corresponde ao número de maneiras de escolher as outras 2 pessoas para compor a equipe. Considerando que há um total de 10 funcionários, restarão 8 pessoas disponíveis, ou seja, temos a combinação de 2elementos dentre 8:

c ~ 8!

8x7x6! 8x7

= —— = 4 x 7 = 28

(8 —2)!x2! 6! x 2!

Que é superior a 20.

Gabarito: Errado

Item. 18. (CEBRASPE 2021/IBGE)

Considere que os gráficos CA e CB apresentados representam, respectivamente, as quantidades mensais de clientes de dois mercados concorrentes A e B, desde o instante da sua inauguração simultânea, em t= 0,até os instantes em que esses mercados encerraram suas atividades,
respectivamente, nos instantes ÍA e ÍB, em que t é dado em meses. Considere, ainda, que C&(t) = 300t - 3t2 e que Cb(í)= 120t -12.

Tendo o texto acima como referência, suponha que 3 clientes do mercado A possam escolher, para retirar suas compras do mercado, qualquer um dos 5 caixas disponíveis, de forma a serem atendidos simultaneamente. Nessa situação, a quantidade de escolhas possíveis de caixas que esses clientes podem fazer é igual a a) 6
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

b) 10

c) 15

d) 60

e) 120

Comentários:

Apesar do enunciado parecer complexo, a questão é relativamente simples. Ela pede o número de maneiras de 3 clientes escolherem 5 caixas do mercado. Considerando que os clientes são diferentes entre si e,portanto, que a ordem da seleção importa, temos um arranjo de 3 elementos, dentre 5:

5! 5! 5 x 4 x 3 x 2!

Gabarito: D

Item. 19. (CEBRASPE 2021/MJ-SP) Em um jogo de cara e coroa disputado com uma moeda não viciada,
um pai criou a seguinte regra, visando aumentar as chances de sua filha vencer a disputa: a moeda seria lançada certa quantidade de vezes, n, definida previamente, e o pai só sairia vencedor caso a moeda apontasse cara em todos os n lançamentos. Tendo como referência essa situação hipotética, julgue o item que se segue.
Existem mais de 20 maneiras distintas de a moeda apontar cara exatamente duas vezes após cinco lançamentos.
Comentários:

O item informa que uma moeda será lançada 5 vezes e pede o número de maneiras de aparecer CARA em exatamente 2 vezes, logo, COROA nas demais vezes. Podemos pensar esse cálculo como a escolha de 2dentre 5 lançamentos, para que o resultado seja CARA:

r 5_! _5_x4x3! _5_x4

5,2 (5-2)!x2! 3! x 2! 2

=10

Alternativamente, podemos pensar na permutação de 3 elementos COROA e 2 elementos CARA,
o que nos levaria à permutação 5 com elementos, com repetição de 3 e de 2:
5!

3! x 2!

5x4x3!

3! x 2!

O que nos leva ao mesmo resultado, inferior a 20.

Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 20. (CEBRASPE 2021/CBM-AL) Em determinado dia, em uma região atendida por uma unidade do corpo de bombeiros, ocorreram 16 acidentes, que resultaram em 48 vítimas, socorridas pelos bombeiros nos próprios locais de acidente. Entre essas vítimas, 4 vieram a óbito no momento do atendimento, e as demais sobreviveram. Com base nessa situação hipotética, julgue o item a seguir.
Suponha que duas ambulâncias tenham comparecido a um dos locais de acidente para transportar quatro vítimas. Considerando-se que cada ambulância transporte no máximo duas vítimas e que todas as quatro vítimas devam ser transportadas, então a quantidade de formas diferentes de dispor as vítimas nas ambulâncias é inferior a seis.
Comentários:

O item informa que há 4 vítimas a serem transportadas em 2 ambulâncias. Note que,
após a escolha das vítimas para a primeira ambulância, as demais vítimas serão necessariamente transportadas pela segunda ambulância. Assim, o número de possibilidades de organizar as 4 vítimas nas 2ambulâncias corresponde ao número de maneiras de selecionar as 2 vítimas, dentre 4, para a primeira ambulância.
Como a ordem da escolha dessas vítimas não importa, pois a questão não mencionou diferenças entre os assentos de uma mesma ambulância, temos a combinação de 2 elementos, dentre 4:
4! 4x3x2!

C4'2 (4-2)! x 2! 2! x 2!

Que é igual a 6, e não inferior.

Gabarito: Errado.

Item. 21. (CEBRASPE 2021/CBM-AL) Os professores João, Carlos e Luis ministrarão um curso de primeiros socorros em que serão ensinados os seguintes procedimentos.
I. fazer massagem cardíaca

II. desengasgar

III. estancar sangramentos

IV. amenizar queimaduras

V. desafogar

VI. cuidar de fraturas

Cada professor ensinará exatamente dois procedimentos, e o mesmo professor que ensinar o procedimento desafogar ensinará também o procedimento desengasgar. Considerando essa situação hipotética, julgue o próximo item.
Existem mais de 20 maneiras diferentes de distribuir os procedimentos para os professores ensinarem.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A questão informa que há 3 professores e que cada professor irá ensinar 2
procedimentos, mas os procedimentos "desafogar" e "desengasgar" serão ensinados pelo mesmo professor.
Há 3 possibilidades para escolher o professor que irá ensinar esses dois procedimentos.
Assim, restarão 4
procedimentos e 2 professores. Note que, após a escolha dos procedimentos para o segundo professor, os demais procedimentos serão necessariamente ensinados pelo terceiro professor.
Logo, o número de maneiras de distribuir os 4 procedimentos pelos 2 professores é igual ao número de maneiras de escolher 2 procedimentos para o segundo professor:
4! 4x3x2! 4x3 r

C4'2 (4-2)! x 2! 2! x 2! " 2 " 6

Pelo princípio multiplicativo, devemos multiplicar essas possibilidades:

3 x 6 = 18

Que é menor que 20.

Gabarito: Errado.

Item. 22. (CEBRASPE 2021/CBM-AL) Aldo, produtor de uvas, dispõe de 10 trabalhadores para realizar a colheita do seu plantio. Na época adequada, para acelerar o processo de colheita, Aldo contratou mais 5trabalhadores, que se juntaram aos 10 já existentes.

Com base no texto acima, suponha que do grupo de 15 trabalhadores fosse constituída uma comissão de

3 membros e que exatamente um desses membros devesse ser escolhido entre os 5 trabalhadores novos.

Nessa situação, a quantidade de comissões distintas que podem ser formadas é igual a a) 25
b) 225

c) 450

d) 455

e) 1.350

Comentários:

A questão informa que há 10 trabalhadores antigos e 5 novos; e que será formada uma comissão de 3trabalhadores, dos quais exatamente 1 seja novo e, portanto, 2 sejam antigos. Para a escolha do trabalhador novo para a comissão, há 5 possibilidades. Para a escolha dos trabalhadores antigos,há 10 possibilidades,
das quais 2 serão escolhidas (sem importância de ordem):

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

10!

(10 - 2)! x 2!

10 x 9 x 8!

8! x 2!

10 x 9

= 45

Pelo princípio multiplicativo, temos:

5 x 45 = 225

Gabarito: B.

Item. 23. (CEBRASPE 2021/IBGE) Considere que, para realizar um conjunto de visitas domiciliares,
tenha sido selecionada, de um grupo de 10 APM, uma equipe composta por um supervisor, um coordenador e quatro coletores de informações. Se todos os APM do grupo forem igualmente hábeis para o desempenho de qualquer uma dessas funções, a equipe poderá ser formada de a) 151.200 maneiras distintas.
b) 6.300 maneiras distintas.

c) 720 maneiras distintas.

d) 210 maneiras distintas.

e) 70 maneiras distintas.

Comentários:

A questão informa que há 10 profissionais, dos quais serão selecionados 1 supervisor,
1 coordenador e 4
coletores. Para calcular de quantas maneiras podemos formar a equipe, devemos avaliar as possibilidades de cada cargo em separado.
Para selecionar 1 supervisor, há 10 possibilidades. Após a escolha do supervisor,
restarão 9 possibilidades para a seleção do coordenador. Após a escolha do coordenador, restarão 8 profissionais,dos quais 4 serão selecionados como coletores. Como a função desses 4 profissionais é a mesma, temos a combinação de 4elementos, dentre 8:

8! 8!

(8 - 4)! x 4! 4! x 4!

8x7x6x5x41 8 x 7 x 6 x 5

4! x 4! " 4 x 3 x 2 x 1

§<X 7 x òxx 5

4XÍ:'3Q< 2 x 1

2 x 7 x 5 = 70

Pelo princípio multiplicativo, devemos multiplicar todas essas possibilidades:

10 x 9 x 70 = 6300

Gabarito: B.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 24. (CEBRASPE 2021/SEDUC-AL) O próximo item apresenta uma situação hipotética a ser julgada,acerca de problemas matemáticos envolvendo situação de uma escola.

Um professor de educação física tem à sua disposição 12 alunos para formar a equipe de voleibol da escola.Desses alunos, dois são os líberos do time e os demais podem atuar em qualquer posição. Sabendo-se que,em uma equipe de voleibol, seis jogadores estão em quadra, sendo um deles,
necessariamente, o libero,
enquanto os demais ficam no banco de reservas, é correto afirmar que, na situação hipotética apresentada,é possível montar 252 combinações diferentes de times para estar em quadra.

Comentários:

O enunciado informa que há 12 alunos, dos quais 2 são líberos e os outros 10 atuam nas demais posições. Otime é formado com 6 alunos, dos quais 1 é libero. Assim, há 2 possibilidades para selecionar o libero.
Em relação aos demais alunos, considerando que a posição específica não importa, já que eles jogam em qualquer posição, temos a combinação de 5 alunos dentre 10 no total:
O número de maneiras de selecionar todo o time (o libero E os outros 5 jogadores)
corresponde ao produto das possibilidades (princípio multiplicativo):
2 x 252 = 504

Gabarito: Errado

Item. 25. (CEBRASPE 2021/PF) Para realizar uma operação de busca e apreensão, em duas localidades diferentes, devem ser deslocadas duas equipes, cada uma delas composta por 1 delegado, 1 escrivão e agentes. Tendo como base essas informações, julgue o item seguinte.
Se estiverem disponíveis, no momento de formação das equipes, exatamente, 2 delegados,
2 escrivães e 4
agentes, o número de maneiras distintas de se montar as duas equipes seria igual ao número de maneiras de se montar, escolhendo-se entre esses mesmos profissionais, uma única equipe para a realização de uma busca em uma única localidade.
Comentários:

O item informa que há 2 delegados, 2 escrivães e 4 agentes a serem selecionados para formar duas equipes,cada uma com 1 delegado, 1 escrivão e 2 agentes.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Note que, uma vez selecionados os membros para a primeira equipe, restarão 1 delegado,
1 escrivão e 2
agentes, os quais necessariamente farão parte da segunda equipe. Assim, o número de maneiras de se montar as duas equipes é igual ao número de maneiras de formar uma única equipe, neste caso.
Gabarito: Certo

Item. 26. (CEBRASPE 2021/PF) Para realizar uma operação de busca e apreensão, em duas localidades diferentes, devem ser deslocadas duas equipes, cada uma delas composta por 1 delegado, 1 escrivão e agentes. Tendo como base essas informações, julgue o item seguinte.
Se estiverem disponíveis, no momento de formação das equipes, exatamente, 2 delegados,
2 escrivães e 4
agentes, o número de maneiras distintas de se montar as duas equipes é igual a 4!.

Comentários:

Vamos calcular o número de maneiras de montar uma única equipe, já que a segunda equipe será formada com os profissionais não escolhidos para a primeira.
Sabendo que há 2 delegados, há 2 possibilidades para a escolha do delegado da primeira equipe.Similarmente, há 2 possibilidades para a escolha do escrivão da equipe. Considerando que há 4 agentes, o número de maneiras de selecionar 2 agentes (sem importância de ordem) é dado pela combinação:
4! 4x3x2! 4x3

C4'2 (4-2)! x 2! 2! x 2! " 2 " 6

Pelo princípio multiplicativo, o número de maneiras de escolher todos os membros da primeira equipe é:
2 x 2 x 6 = 24

Que é igual a 41 = 4x3x2x1 = 24.

Gabarito: Certo

Item. 27. (CEBRASPE 2021/PF) Para realizar uma operação de busca e apreensão, em duas localidades diferentes, devem ser deslocadas duas equipes, cada uma delas composta por 1 delegado, 1 escrivão e agentes. Tendo como base essas informações, julgue o item seguinte.
Se estiverem disponíveis, no momento de formação das equipes, 3 delegados, 4 escrivães e 6 agentes, o número de maneiras distintas de se montar as duas equipes é superior a 6.500.
Comentários:

Agora, o número de profissionais disponíveis é maior do que nos itens anteriores e,
por isso, precisamos pensar na escolha das 2 equipes.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabendo que há 3 delegados, há 3 possibilidades para a escolha do delegado da primeira equipe.Similarmente, há 4 possibilidades para a escolha do escrivão da primeira equipe.
Considerando que há 6
agentes, o número de maneiras de selecionar 2 agentes (sem importância de ordem) é dado pela combinação:
6! 6x5x4! 6x5

Có'2 " (6 - 2)! x 2! " 4! x 2! " 2 15

Pelo princípio multiplicativo, o número de maneiras de escolher todos os membros da primeira equipe é:
3 x 4 x 15 = 180

Após a escolha da primeira equipe, restarão 2 delegados, 3 escrivães e 4 agentes.
Assim, há 2 possibilidades para a escolha do delegado da segunda equipe; 3 possibilidades para a escolha do escrivão da segunda equipe; e para a escolha dos 2 agentes, temos a combinação:
4! 4x3x2! 4x3

C4-2 (4-2)! x 2! 2! x 2! " 2 " 6

Pelo princípio multiplicativo, o número de maneiras de escolher todos os membros da segunda equipe é:
2 x 3 x 6 = 36

E o número de maneiras de escolher os membros para ambas as equipes (uma E outra) é dada pelo produto das possibilidades (princípio multiplicativo):
180 x 36 = 6.480

Gabarito: Errado

Item. 28. (CEBRASPE 2021/PM-TO) Em um distrito policial, estão lotados 30 agentes para policiamento ostensivo. Acerca do tempo de serviço desses agentes como policiais, sabe-se que:
* 6 deles têm mais de 5 anos de serviço;

* 12 deles têm entre 2 e 10 anos de serviço;

* 16 deles têm menos de 2 anos de serviço.

Suponha que 3 policiais sejam escolhidos no grupo para cumprir determinada diligência.
Suponha, ainda,
que se deseje que, na função de policial, 1 desses agentes tenha mais de 2 anos de serviço, e os outros 2,menos de 2 anos de serviço. Nesse caso, a quantidade de formas diferentes de constituir esse grupo é a) inferior a 100.
b) superior a 100 e inferior a 400.

c) superior a 400 e inferior a 1.000

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

d) superior a 1.000 e inferior a 2.000

e) superior a 2.000

Comentários:

A questão pede o número de maneiras de selecionar 1 agente com mais de dois anos de serviço e 2 agentes com menos de dois anos de serviço. Pelos dados do enunciado, 16 agentes possuem menos de 2 anos. Logo,o número de maneiras de selecionar 2 agentes dentre eles é dado pela combinação:

16! 16x15x14! 16x15

Cl6'2 (16-2)! x 2! 14! x 2! 2 - 8 x 15 - 120

Agora, precisamos selecionar 1 agente com mais de dois anos. O enunciado informa que há 6 agentes com mais de cinco anos e 12 agentes com mais de dois anos e menos de dez anos. Essas duas categorias se referem a agentes com mais de dois anos, mas há uma interseção entre elas. Como há30 agentes no total,
dos quais 16 têm menos de dois anos, podemos concluir que a diferença está associada a agentes com mais de dois anos:
30 -16 = 14

Portanto, há 14 possibilidades para a escolha do agente com mais de dois anos. Pelo princípio multiplicativo,o número de maneiras de selecionar todos os 3 membros é dado pelo produto:

120 x 14 = 1680

Gabarito: D

Item. 29. (CEBRASPE 2021/PC-DF) Um agente, com o objetivo de mensurar o risco de propagação da covid-19 em uma investigação na qual averiguava um possível descumprimento do artigo 268 do
Código Penal,
que define como crime de infração de medida sanitária "infringir determinação do poder público,destinada a impedir introdução ou propagação de doença contagiosa", obteve de uma testemunha as informações a seguir.
* Houve, no local investigado, uma festa, com aglomeração de moças e rapazes; não havia álcool em gel e ninguém estava usando máscaras.
* Cada rapaz cumprimentou exatamente uma vez a todos os outros rapazes com apertos de mão.

* Cada moça cumprimentou exatamente uma vez a todos os outros presentes com um aceno.

Considerando que são verdadeiras as informações prestadas pela testemunha da situação hipotética precedente, julgue o item a seguir.
O número total de cumprimentos ocorridos na festa — acenos e apertos de mão — é proporcional ao número de pessoas presentes.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Para que o número total de cumprimentos T seja proporcional ao número de presentes N,
devemos ter, para uma constante k qualquer:
T = k.N

Vamos supor que haja x moças e y rapazes, sendo o total de pessoas N = x + y. O
número de acenos entre rapazes moças é, pelo princípio multiplicativo:
x.y

Considerando que os acenos não são recíprocos, ou seja, quando duas pessoas se acenam,
há 2 acenos,
então cada moça acena para todas as outras x — 1 moças:

x. (x — 1)

Em relação aos apertos de mão dos rapazes, esses sim são recíprocos, ou seja, quando duas pessoas se apertam as mãos, há 1 aperto de mão. Então, o número de apertos de mão corresponde à combinação de 2dentre o número total de rapazes:

y! y x (y - 1) x (y - 2)! y x (y - 1)

y'2 (y-2)! x2! (y — 2)! x 2! " 2

Assim, o número total de cumprimentos é dado por:

, y x (y-1)T = x.y + x. (x - 1) H------ ------

E esse total não pode ser descrito como o produto do total N = x + y por constante alguma, logo, essas grandezas não são proporcionais.
Gabarito: Errado

Item. 30. (CEBRASPE 2021/PC-DF) Para ter acesso a um arquivo digital criptografado, um cibernauta deve testar uma senha de 8 dígitos composta pelos algarismos de 0 a 9, admitida a repetição. Ocibernauta teve a informação prévia de que o arquivo foi criado no dia 23/12/19 e que o dia, o mês e o ano da criação do arquivo, representados por dois algarismos cada, estão presentes na senha, mas aparecem em ordem aleatória. Com base nessas informações, julgue o item a seguir.
O número máximo de possibilidades de senhas que o cibernauta deve testar é inferior a 5.000.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A questão informa que será escolhida uma senha de 8 dígitos, com os 10 algarismos de
0 a 9, de modo que estejam presentes os números 23, 12 e 19, em alguma ordem. Ou seja, é necessário escolher outros 2algarismos e alocar os números em alguma ordem:

23 12 19 Xi x2

Para calcular o número de possibilidades nessa situação, vamos continuar supondo a escolha de 2 algarismos distintos (Ai =# A₂), oU seja, começamos combinação de 2 elementos, dentre 10:
10! 10x9x8!

Cl0'2 (10 - 2)! x 2! 8! x 2 - 5 x 9 - 45

Agora, devemos permutar os elementos para formar as possibilidades de senha nesse caso:
23,12,19, X₁ e
X₂, a princípio do todos distintos. Logo, temos uma permutação de 5 elementos:

P₅ = 51 = 5x4x3x2x1 = 120

Pelo princípio multiplicativo, o número de senhas que podem ser formadas nessa situação é:

45 x 120 = 5400

Agora, vamos supor que os dois algarismos extras sejam iguais (AT = X₂).
Nessa situação, temos 10
possibilidades para a escolha do algarismo e o número de maneiras de organizar os elementos da senha corresponde a uma permutação 5 elementos com repetição de 2 elementos:
p2, _

5 V

ᵖ52. _

5! 5x4x3 x2 x 1

= 2!" 2xl -5X4X3 = 60

Pelo princípio multiplicativo, o número de possibilidades nesta situação é:

10 x 60 = 600

Agora, precisamos subtrair os casos em que escolhemos os algarismos extras, AT e X₂,
iguais às duplas. Por exemplo, as seguintes senhas são a mesma e foram contadas como possibilidades distintas:
23 12 19

23 12 1

1 9

9 19

O número de possibilidades em que temos essa situação, para cada uma das 3
duplas, corresponde à permutação de 4 elementos (23, 12, 19 e A₁X₂) com repetição de 2 elementos:
p2 _ _

4! 4x 3 x 2 x 1

P4 = 2! = 2X1 =4X3 = 12

Pelo princípio multiplicativo, o número total de possibilidades nessa situação é:

3 x 12 = 36

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E o número total de possibilidades de formar a senha é:

5400 + 600 - 36 = 5964

Que é superior a 5000.

Gabarito: Errado

Item. 31. (CEBRASPE 2021/SEDUC-AL) O próximo item apresenta uma situação hipotética a ser julgada,acerca de problemas matemáticos envolvendo situação de uma escola.

Um professor de matemática precisa distribuir 20 exercícios para 4 alunos, de tal forma que cada aluno receba no mínimo 3 exercícios. Nessa situação hipotética, há 165 maneiras distintas de o professor distribuir os exercícios.
Comentários:

O enunciado informa que há 20 exercícios a serem distribuídas para 4 alunos, de modo que cada aluno receba no mínimo 3 exercícios. Após a distribuição do número mínimo de exercícios para cada aluno (3x4= 12),restarão 8 exercícios a serem distribuídos livremente pelos 4 alunos. Em outras palavras, o primeiro aluno pode ficar com todos os 8 extras; ou o segundo aluno fica com 1 exercício extra e o quarto com 7 exercícios extras; etc. Aqui, os exercícios são considerados equivalentes, importando saber qual aluno vai ficar que quantidade de questões.
Essa é uma questão de combinação completa (ou combinação com repetição). Para resolvê-la, vamos representar os 4 alunos por seções e os 8 exercícios por objetos:
Aluno 1 Aluno 2 Aluno 3 Aluno 4

Na ilustração acima, o primeiro aluno ficou com 3 exercícios extras (além dos 3
obrigatórios), o segundo aluno ficou com 1 exercício extra e o quarto aluno ficou 4 exercícios extras.
Alternativamente, poderíamos ter:

Aluno 1 Aluno 2 Aluno 3 Aluno 4

Neste exemplo, o primeiro aluno ficou com 1 exercício extra, o segundo aluno ficou com 3 exercícios extras,o terceiro também ficou com 3 extras e o quarto ficou com 1 extra.

Assim, o número de maneiras de distribuir os 8 exercícios extras pelos 4 alunos
(combinação completa de n

= 4 elementos e p = 8 objetos) equivale ao número de maneiras de permutar os 8
exercícios com as 3

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

divisórias entre os alunos. Ou seja, temos uma permutação de 11 elementos no total,
dos quais 8 se repetem e 3 se repetem:
rr>V _ r>n-l,p _ (n 1 + p)l n-l+p (n_ 1)1 Xp!
rn8 _ p3,8 _

11 '

— 3! x 8!

11x10x9x8! 11x10x9

= 3! x 8! = 3X2X1 = 5 x 3 = 165

Gabarito: Certo

Item. 32. (CEBRASPE 2020/Ministério da Economia) O setor de gestão de pessoas de determinada empresa realiza regularmente a análise de pedidos de férias e de licenças dos seus funcionários. Os pedidos são feitos em processos, em que o funcionário solicita apenas férias, apenas licença ou ambos (férias e licença).Em determinado dia, 30 processos foram analisados, nos quais constavam 15 pedidos de férias e 23pedidos de licenças. Com base nessa situação hipotética, julgue o item que se segue.

Se 2 desses 30 processos forem aleatoriamente selecionados para auditoria, então a quantidade de pares de processos possíveis será superior a 400.
Comentários:

O enunciado informa que há 30 processos, dos quais 2 serão escolhidos aleatoriamente. O número de maneiras de selecionar esse par de processos corresponde à combinação de 2 elementos, dentre 30:
Que é superior a 400.

Gabarito: Certo

Item. 33. (CEBRASPE 2019/PGE-PE) No item a seguir, é apresentada uma situação hipotética, seguida de uma assertiva a ser julgada, a respeito de máximos e mínimos de funções, da regra de trapézio para cálculo aproximado de integrais e de análise combinatória.
Entre os 12 processos administrativos de determinado setor público, 5 se referem a adicional de periculosidade. Para agilidade na discussão e no julgamento, esses 12 processos serão agrupados em pares.Nesse caso, a quantidade de pares de processos distintos que podem ser formados de modo que pelo menos um dos processos se refira a adicional de periculosidade é igual a 35.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para encontrar o número de possibilidades de formar pares com pelo menos um processo de adicional de periculosidade, podemos calcular o número de formas de se escolher quaisquer 2processos e subtrair o número de formas de escolher 2 processos que não se referem a adicional de periculosidade.
O número de formas de escolher quaisquer 2 processos, dentre 12, é:

12! 12x11

Cl2'2 " 10! 2! " 2 " 66

O número de formas de escolher 2 processos que não se referem a adicional de periculosidade, sabendo que tais processos totalizam 12 - 5 = 7 processos, é:
7! 7x6

C?'2 " 5! 2! " 2 " 21

Logo, o número de formas de escolher 2 processos com pelo menos um processo de adicional de periculosidade é:
66-21 = 45

Nota: As 35 formas que o item mencionou correspondem ao número de formas de escolher 1 processos de periculosidade e 1 processo diferente, dado por 5 x 7 = 35. Esse valor deve ser somado (princípio aditivo) o
5' 5x4

número de formas de escolher ambos os processos de periculosidade, dado por C₅ ₂ = — = — = 10.

Gabarito: Errado.

Item. 34. (CEBRASPE 2019/PGE-PE) A União tem, hoje, 138 estatais sob sua gestão, entre elas o Banco doBrasil S.A., a PETROBRAS e a CAIXA. Dessas 138, somente três devem permanecer sob a gestão da União;
as demais serão privatizadas. Considerando essa afirmação, julgue o item.

Se todas as estatais tiverem a chance de ficar sob a gestão da União, então a quantidade de maneiras distintas de escolher as três empresas que não serão privatizadas será inferior a 230.000.
Comentários:

O número de formas de escolher 3 empresas que não serão privatizadas, dentre 138, é dado por:

Ci38,3 -

3! 135!

138! 138 x 137 x 136

- = = 23 x 137 x 136

3 X Z

Nem precisamos fazer essa conta. Basta notarmos que 137 e 136 são maiores que 100.
Logo, esse resultado é superior a 23 x 100 x 100 = 230.000.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 35. (CEBRASPE 2019/SEFAZ-RS) Os funcionários de uma repartição foram distribuídos em sete grupos de trabalhos, de modo que cada funcionário participa de exatamente dois grupos, e cada dois grupos têm exatamente um funcionário em comum. Nessa situação, o número de funcionários da repartição é igual a a) 7.
b) 14.

c) 21.

d) 28.

e) 35.

Comentários:

Sabendo que cada dois grupos apresenta um funcionário em comum, o número de funcionários corresponde ao número de pares de grupos formados. Sabendo que há 7 grupos, o número de maneira de escolher 2grupos é:

7! 7x6x5! 7x6

C?'2 " (7 - 2)! x 2! 5! x 2! " 2 21

Logo, há 21 funcionários.

Gabarito: C.

Item. 36. (CEBRASPE 2018/PF) Em um processo de coleta de fragmentos papilares para posterior identificação de criminosos, uma equipe de 15 papiloscopistas deverá se revezar nos horários de 8 h às 9h e de 9 h às 10 h. Com relação a essa situação hipotética, julgue o item a seguir.

Considere que uma dupla de papiloscopistas deve ser escolhida para atender no horário das 8 h. Nessa situação, a quantidade, distinta, de duplas que podem ser formadas para fazer esse atendimento é inferior a 110.
Comentários:

O número de formas de escolher 2 papiloscopistas, dentre 15, é:

15! 15x14x13! 15x14

Cl5'2 (15 - 2)! x 2! 13! x 2! 2 - 15 x 7 - 105

Logo, o número de duplas possíveis é inferior a 110.

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 37. (CEBRASPE 2018/ABIN) Como forma de melhorar a convivência, as famílias Turing, Russell e
Gõdel disputaram, no parque da cidade, em um domingo à tarde, partidas de futebol e de vôlei. O quadro a seguir mostra os quantitativos de membros de cada família presentes no parque, distribuídos por gênero.
FAMÍLIA MASCULINO FEMININO

Turing 5 7

Russell 6 5

Gõdel 5 9

A partir dessa tabela, julgue os itens subsequentes.

A quantidade de maneiras distintas de se formar um time de vôlei com seis integrantes, sendo três homens da família Turing e três mulheres da família Gõdel, é superior a 700.
Comentários:

Deseja-se formar um time com 3 homens da família Turing e 3 mulheres da família
Gõdel. Considerando que há 5 homens da família Turing, o número de maneiras de escolher os 3 homens do time é:
r — 5!

— 5x4x3!

— 5x4

=10

5,3 (5 — 3)! x 3! 2! x 3! 2

Considerando que há 9 mulheres na família Gõdel, o número de maneiras de escolher as
3 mulheres do time é:
9!

C9'3 (9 - 3)! x 3!

9 x 8 x 7 x 6!

6! x 3!

9x8x7
3x2x1

3 x 4 x 7 = 84

Sabendo que vamos precisar escolher os homens E as mulheres (são escolhas concomitantes), multiplicamos essas possibilidades (princípio multiplicativo):
Número de maneiras = 10 x 84 = 840
Logo, o número de maneiras de formar o time é superior a 700.

Gabarito: Certo.

Item. 38. (CEBRASPE 2018/PF) Para cumprimento de um mandado de busca e apreensão serão designados um delegado, 3 agentes (para a segurança da equipe na operação) e um escrivão. O efetivo do órgão que fará a operação conta com 4 delegados, entre eles o delegado Fonseca; 12 agentes,entre eles o agente
Paulo; e 6 escrivães, entre eles o escrivão Estêvão. Em relação a essa situação hipotética, julgue o item a seguir.
A quantidade de maneiras distintas de se escolher os três agentes para a operação de forma que um deles seja o agente Paulo é inferior a 80.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

A questão pede o número de maneiras de escolher 3 agentes, dentre 12, de forma que um deles seja o agente Paulo. Sabendo que Paulo já foi escolhido, restam 2 agentes a serem escolhidos dentre 11:
11! 11 x 10 x 9! 11 x 10

Cl1'2 (11 — 2)! x 2! 9! x 2! 2 - 11 x 5 - 55

Logo, há menos de 80 maneiras de fazer tal escolha.

Gabarito: Certo.

Item. 39. (CEBRASPE 2018/PF) Para cumprimento de um mandado de busca e apreensão serão designados um delegado, 3 agentes (para a segurança da equipe na operação) e um escrivão. O efetivo do órgão que fará a operação conta com 4 delegados, entre eles o delegado Fonseca; 12 agentes,entre eles o agente
Paulo; e 6 escrivães, entre eles o escrivão Estêvão.

Em relação a essa situação hipotética, julgue o item a seguir.

Se o delegado Fonseca e o escrivão Estêvão integrarem a equipe que dará cumprimento ao mandado, então essa equipe poderá ser formada de menos de 200 maneiras distintas.
Comentários:

O número de maneiras de formar a equipe, sabendo que o único delegado da equipe e o único escrivão da equipe já foram definidos, corresponde ao número de maneiras de escolher os 3 agentes.Considerando que há 12 agentes disponíveis, temos a combinação de 3 elementos dentre 12:
12!

Cl2'3 (12 - 3)! x 3!

12 x 11 x 10 x 9!

9! x 3!

12 x 11 x 10

——-—— = 2 x 11 x 10 = 220

3x2x1

Logo, há mais de 200 maneiras de escolher a equipe.

Gabarito: Errado.

Item. 40. (CEBRASPE 2018/PF) Para cumprimento de um mandado de busca e apreensão serão designados um delegado, 3 agentes (para a segurança da equipe na operação) e um escrivão. O efetivo do órgão que fará a operação conta com 4 delegados, entre eles o delegado Fonseca; 12 agentes,entre eles o agente
Paulo; e 6 escrivães, entre eles o escrivão Estêvão.

Em relação a essa situação hipotética, julgue o item a seguir.

Há mais de 2.000 maneiras distintas de se formar uma equipe que tenha o delegado
Fonseca ou o escrivão
Estêvão, mas não ambos.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Para formar uma equipe que tenha o delegado Fonseca ou o escrivão Estêvão, mas não ambos, precisamos considerar as duas situações possíveis.
Situação 1) Considerando que o delegado Fonseca faz parte da equipe, precisamos escolher os agentes e o escrivão, sabendo-se que o Estêvão não fará parte da equipe.
O número de formas de escolher 3 agentes, dentre 12, é igual a C12i3 =

12! 220

(12—3)!x3!

* O número de formas de escolher 1 escrivão, dentre 5 (já que Estêvão não é uma opção), é igual a
5.

Para formartoda a equipe com o delegado Fonseca, multiplicamos esses resultados (princípio multiplicativo):Número de Equipes com Fonseca = 220 x 5 = 1100

Situação 2) Considerando que o escrivão Estêvão faz parte da equipe,
precisamos escolher o delegado,
sabendo-se que Fonseca não fará parte da equipe, e os agentes.

* O número de formas de escolher 1 delegado, dentre 3 (já que Fonseca não é uma opção), é igual a
3.

* O número de formas de escolher 3 agentes, dentre 12, permanece a mesma: 220

Para formartoda a equipe com o escrivão Estêvão, multiplicamos esses resultados (princípio multiplicativo):
Número de Equipes com Estêvão = 3 x 220 = 660

Como são situação alternativas (a equipe terá Estêvão OU Fonseca), devemos somar essas possibilidades(princípio aditivo):

Número de possibilidades = 1100 + 660 = 1760
Logo, há menos de 2.000 maneiras de formar a equipe nessas condições.

Gabarito: Errado.

Item. 41. (CEBRASPE 2018/PF) Em um aeroporto, 30 passageiros que desembarcaram de determinado voo e que estiveram nos países A, B ou C, nos quais ocorre uma epidemia infecciosa, foram selecionados para ser examinados. Constatou-se que exatamente 25 dos passageiros selecionados estiveram em A ou em B,nenhum desses 25 passageiros esteve em C e 6 desses 25 passageiros estiveram em A e em B. Com referência a essa situação hipotética, julgue o item que se segue.
A quantidade de maneiras distintas de se escolher 2 dos 30 passageiros selecionados de modo que pelo menos um deles tenha estado em C é superior a 100.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Para encontrar o número de maneiras de selecionar 2 passageiros, de modo que pelo menos um tenha estado em C, podemos calcular o número de maneiras de selecionar 2 passageiros, dentre todos os 30, e subtrair o número de maneiras de selecionar 2 passageiros de modo que nenhum passageiro tenha estado em C. O número de maneiras de selecionar 2 passageiros, dentre 30, é igual a:
30!

Cso'2 " (30 - 2)! x 2!

30 x 29 x 28!

28! x 2!

30 x 29

---- - ---- = 15 x 29 = 435

Sabendo que há 25 passageiros que não estiveram em C, então o número de maneiras de selecionar 2passageiros que não estiveram em C corresponde à combinação de 2 elementos, dentre 25:

25!

C25'2 " (25 - 2)! x 2!

25 x 24 x 23!

23! x 2!

25 x 24

---- - ---- = 25 x 12 = 300

Logo, o número de possibilidades de selecionar 2 passageiros, de modo que pelo menos
1 tenha estado em
C é dado pela diferença:

435-300 = 135

Logo, a quantidade de maneiras é superior a 100.

Gabarito: Certo.

Item. 42. (CEBRASPE 2018/STJ) Considere as proposições P e Q a seguir.

P: Todo processo que tramita no tribunal A ou é enviado para tramitar no tribunal B ou no tribunal
C.
Q: Todo processo que tramita no tribunal C é enviado para tramitar no tribunal B.

A partir dessas proposições, julgue o item seguinte.

Se 10 processos que chegarem ao tribunal A em determinado dia forem separados de forma aleatória em dois grupos de 5 processos cada, um para ser encaminhado ao tribunal B, e outro,para o tribunal C, então essa separação poderá ser feita de, no máximo, 240 formas diferentes.
Comentários:

A questão informa que chegam 10 processos no tribunal, dos quais 5 serão encaminhados para A e 5 serão encaminhados para B, conforme representado a seguir:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ao selecionarmos os 5 processos para B, estaremos definindo os processos que serão encaminhados para C(e vice-versa). Logo, temos uma combinação de 5 elementos, dentre 10:

10! 10x9x8x7x6x5! 10x9x8x7x6

Cl0'5 = (10 - 5)! x 5! = 5! x 5! = 5x4x3x2xl
= 2x9x2x7 = 252

Logo, há mais de 240 formas diferentes de fazer essa separação.

Gabarito: Errado.

Item. 43. (CEBRASPE 2018/EMAP) No Porto de Itaqui, 16 contêineres serão embarcados em 2
navios: cada navio deverá levar exatamente 8 desses contêineres. Do total de contêineres, 8 estão carregados com frango congelado, 3, com carne bovina congelada e 5, com soja.
A partir dessas informações, julgue o item que se segue.

A quantidade de maneiras distintas de se embarcarem os 8 contêineres no primeiro navio, de forma que exatamente 7 deles estejam carregados com frango congelado, é inferior a 100.
Comentários:

No primeiro navio, são embarcados 8 contêineres, sem importância de ordem, dos quais,
exatamente 7 são de frango (nem mais, nem menos).
Sabendo que existem 8 contêineres de frango, no total, então a quantidade de maneiras distintas de selecionar os 7 contêineres de frango a serem embarcados no primeiro navio corresponde à combinação de7 elementos, dentre 8:

8! 8 x 7!

Cs'7 ~ (8 - 7)! x 7! " 1! x 7! _ 8

Além disso, o oitavo contêiner, que não será de frango, pode ser um dos 3
contêineres de carne bovina ou dos 5 contêineres de soja. Logo, há 8 possibilidades para o 85 contêiner.
Pelo princípio multiplicativo, temos:

Número de possibilidades = 8 x 8 = 64

Assim, o número de maneiras distintas de embarcar 8 contêineres, sendo 7 de frango, é inferior a
100.

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 44. (CEBRASPE 2018/EMAP) No Porto de Itaqui, 16 contêineres serão embarcados em 2
navios: cada navio deverá levar exatamente 8 desses contêineres. Do total de contêineres, 8 estão carregados com frango congelado, 3, com carne bovina congelada e 5, com soja.
A partir dessas informações, julgue o item que se segue.

A quantidade de maneiras distintas de se embarcarem, no primeiro navio, 4 contêineres de frango congelado e 4 de soja e, no segundo navio, 4 contêineres de frango congelado, 1 de soja e 3de carne bovina congelada é superior a 330.
Comentários:

Temos 16 contêineres a serem embarcados em 2 navios, cada um com 8
contêineres. Assim, ao selecionarmos os contêineres do primeiro navio, teremos definido os contêineres do segundo navio, por exclusão.
No primeiro navio, haverá 4 contêineres de frango, de um total de 8, e 4 de soja,
de um total de 5. Note que a ordem não é relevante. Assim, o número de maneiras de selecionar os 4 contêineres de frango, dentre 8,é:

8! 8x7x6x5x41 8 x 7 x 6 x 5

Cs'4 " (8-4)! x 4! " 4! x 4! " 4 x 3 x 2 x 1 - 2x7x5-70

O número de maneiras de selecionar 4 contêineres de soja, dentre 5, é:

5!

C5.4 - - 5

Pelo princípio multiplicativo, temos:

Número de maneiras = 70 x 5 = 350
Logo, há mais de 330 maneiras de selecionar os referidos contêineres.

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

