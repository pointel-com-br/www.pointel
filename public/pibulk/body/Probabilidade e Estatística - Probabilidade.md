# Probabilidade e Estatística - Probabilidade

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Introdução - Probabilidade

2) Noções Iniciais sobre Probabilidade

3) Definição Clássica de Probabilidade

4) Combinações de Eventos

5) Axiomas de Probabilidade

6) Probabilidade Condicional

7) Questões Comentadas - Definição Clássica de Probabilidade - Cebraspe

8) Questões Comentadas - Combinações de Eventos e Probabilidade - Cebraspe

9) Questões Comentadas - Probabilidade Condicional - Cebraspe

10) Lista de Questões - Definição Clássica de Probabilidade - Cebraspe

11) Lista de Questões - Combinações de Eventos e Probabilidade - Cebraspe

12) Lista de Questões - Probabilidade Condicional - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Olá, amigos! Tudo certo até aqui com Estatística?

Nesta aula, vamos estudar a Teoria da Probabilidade. Além de ser um tópico muito frequente nas provas de concursos, ela também é a base para todo o estudo de Estatística Inferencial.
A matéria não é complicada, mas é preciso entender bem um assunto antes de passar para o próximo,porque ela é bem encadeada. Então, vamos com bastante calma!

Te espero!

Luana Brandão

Não me conhece? Sou Doutora em Engenharia de Produção, pela Universidade
Federal Fluminense, e
Auditora Fiscal da SEFAZ-RJ. Quero muito te ajudar com Estatística, para você conseguir a tão sonhada aprovação!
Se tiver alguma dúvida, entre em contato comigo!

M professoraluanabrandao@gmail.com
@professoraluanabrandao

"Determinação, coragem e autoconfiança são fatores decisivos para o sucesso."

Dalai Lama

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

PRoBABILIDADE

Conceitos Iniciais

A Teoria da Probabilidade é o ramo da Estatística que estuda experimentos e fenômenos aleatórios, cujos resultados são incertos. Como exemplo, podemos citar:
* lançamentos de dados ou moedas;

* seleções feitas ao acaso (ou aleatoriamente), como de uma carta no baralho, de uma pessoa ou peça dentro de um grupo, etc.;
* fenômenos naturais, como chuva em determinado dia.

Embora os resultados sejam incertos, se tais experimentos ou fenômenos são repetidos muitas vezes, é possível encontrar certo padrão em seus resultados. Se lançarmos uma moeda comum muitas vezes esperamos que, em torno de metade das vezes, a face superior seja cara e, na outra metade, coroa.
Porém, para encontrar tal padrão, é necessário que os experimentos/fenômenos possam ser repetidos indefinidamente, sob condições inalteradas.
Um exemplo em que essa condição não é atendida é o lançamento de uma moeda próximo a um bueiro. Em algum lançamento, é possível que a moeda caia no bueiro, não sendo mais possível repetir o experimento.Para esse tipo de situação, não podemos utilizar todos os conceitos da
Teoria da Probabilidade que estudaremos aqui.
ESQUEMATIZANDO

Os Experimentos/Fenômenos aleatórios:

i) Podem ser repetidos indefinidamente, sob condições inalteradas;

ii) Apresentam resultado incerto, porém com um padrão conhecido.

Espaço Amostrai

O Espaço Amostrai de um experimento/fenômeno aleatório é o conjunto de todos os resultados possíveis.Também podemos chamar o Espaço Amostrai de Universo, e ele pode ser representado como U ou ÍT.

No lançamento de uma moeda, por exemplo, o Espaço Amostrai é o conjunto:

UM = {CARA, COROA}

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para o lançamento de um dado (com 6 faces), o Espaço Amostrai é o conjunto:

UD = {1, 2, 3, 4, 5, 6}

Se o experimento for o lançamento de 2 moedas, o Espaço Amostrai é dado por:

U₂M = {(CARA, CARA), (CARA, COROA), (COROA, CARA), (COROA, COROA)}

Podemos, ainda, chamar cada resultado possível de ponto amostrai. No lançamento de 2
moedas que acabamos de ver, por exemplo, há 4 pontos amostrais.
I«** IX

i (2017 - Secretaria de Educação/MG) Em Teoria das Probabilidades, um conceito importante ao se trabalhar
= com experimentos aleatórios é o conceito de Espaço Amostrai. Assinale a alternativa que indica o correto i
= significado deste conceito.
i

I

I

: a) Conjunto de todos os resultados possíveis do experimento j b) Tamanho total da amostra i

I

: c) Proporção entre o tamanho da amostra tomada e o tamanho total da população i
I

I

d) Intervalono qualas probabilidades somadas ultrapassam 0,5
i

I

: e) Somatória dos todos os possíveis resultados de um experimento i
I

i Comentários:

I

I

: O Espaço Amostrai de um experimento é o conjunto de todos os seus resultados possíveis.
i

I

: Gabarito: A

L

Evento

Um evento é todo e qualquer subconjunto do Espaço Amostrai.

Por exemplo, no lançamento de 2 moedas, podemos chamar de evento A aquele em que ambas as moedas apresentam o mesmo resultado para a face superior. Portanto, o evento A é o subconjunto:
A = {(CARA, CARA), (COROA, COROA)}

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Observamos que o evento A apresenta 2 elementos (ou 2 pontos amostrais).
Denotamos o número de elementos do evento A por n(A). Nesse exemplo, temos:
n(A) = 2

Considerando como exemplo o lançamento de 2 dados, podemos chamar de evento B aquele em que a soma das faces superiores dos dois dados é igual a 12. O evento B é, portanto, o subconjunto:
B = {(6,6)}

Ou seja, temos n(B) = 1. Nesse caso, dizemos que o evento é simples ou elementar.

E se disséssemos que o evento C corresponde ao subconjunto em que a soma das faces superiores dos dois dados é igual a 13? Nesse caso, não há elemento algum do Espaço Amostrai que atenda a esse requisito (a soma máxima é 12). Por isso, esse evento é um conjunto vazio (simbolizamos o conjunto vazio por 0):
C = 0

Como não há elemento algum no subconjunto, temos n(C) = 0. Dizemos que esse evento é impossível!

Podemos ter, ainda, um evento que corresponda a todo o Espaço Amostrai. Por exemplo,
considerando o lançamento de um único dado, podemos chamar de evento D aquele em que o número indicado na face superior é menor que 7. Assim, o evento D corresponde ao subconjunto:
D = {1,2,3,4,5,6}= UD

Como ambos os conjuntos (evento D e Espaço Amostrai UD) são iguais, o número de elementos de ambos os conjuntos também é igual: n(D) = n(UD). Dizemos que esse evento é certo!
Evento simples ou elementar -> n(B) = 1
Evento impossível: C = 0 -> n(C) = 0
Evento certo: D = U -> n(D) = n(U)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (2017 - Instituto de Previdência de João Pessoa) Sobre as afirmações a seguir, assinale a única correta no i que diz respeito ao espaço amostrai.
I

I

i a) Se Q é um espaço amostrai do experimento, todo subconjunto A contido em Q será chamado de evento, i i Q é o evento certo, <|) o evento impossível. Se o evento w pertence a Q, o evento {w} é dito elementar b) Se Q é um espaço amostrai do experimento, todo subconjunto A contido em Q será chamado de subespaço i i amostrai, 0 é o evento certo, <|) o evento vazio. Se o evento oJ pertence a Q,o evento {w} é dito elementar ;

I

I

: c) Se Q é um espaço amostrai do experimento, todo subconjunto A contido em Q será chamado de evento, i
= 0 é o evento vazio, <|) o evento neutro. Se o evento w pertence a 0 o evento {oJ} é dito elementar.

I

d) Se 0 é um espaço de probabilidades do experimento, todo subconjunto A contido em
Q será chamado de i i evento, Qéo evento certo, <|> o evento vazio. Se o evento oJ pertence a 0, o evento {w} é dito único.
= e) Se 0 é um espaço de probabilidades do experimento, todo subconjunto A contido em 0 será chamado de i
= evento, Qéo evento certo, <|> o evento vazio. Se o evento oJ pertence a Q, o evento {GJ} é dito unitário.
I

I

i Comentários:

i) Podemos denotar por 0 um Espaço Amostrai (não um espaço de probabilidades, como descrito nas i j alternativas "d" e "e");
I

I

: ii) Todo subconjunto do Espaço Amostrai é chamado de evento (não de subespaço amostrai, como descrito i
= na alternativa "b");
i

I

; iii) O evento igual ao Espaço Amostrai (Q) é dito certo (não vazio, como descrito na alternativa
"c");

I

I

iv) O evento que corresponde ao conjunto vazio (<|)) é dito impossível (não neutro,
como descrito na i

= alternativa "c");

i

= v) O evento com um único elemento, como é o caso de B = {(6, 6)} que vimos anteriormente, é dito j
; elementar.

I

: Logo, a única afirmação correta é a alternativa A.

; Gabarito: A

L

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DEFINIçõES DE PRoBABILIDADE

A probabilidade representa as chances de um evento ocorrer. Agora, veremos como ela pode ser calculada.
A principal definição é a clássica, que veremos primeiro. Porém, em alguns casos, ela não pode ser utilizada,sendo necessário recorrer à definição frequentista de probabilidade, que veremos em seguida.

Definição Clássica

Sendo U o Espaço Amostrai, a probabilidade de ocorrer o evento A é, pela definição clássica:

PU) = n((7)

Ou seja, a probabilidade de um evento é a razão entre o número de elementos do
Evento, n(zl), e o número de elementos do Espaço Amostrai, n(Lf).
Por exemplo, no lançamento de 2 moedas, o Espaço Amostrai (U2M) é:

U₂M = {(CARA, CARA), (CARA, COROA), (COROA, CARA), (COROA, COROA)}

E o número de elementos desse Espaço Amostrai é:

n(U2M) = 4

O evento em que ambas as moedas fornecem o mesmo resultado, que vamos chamar de A, é o subconjunto:
A = {(CARA, CARA), (COROA, COROA)}

E o número de elementos do evento A é:

n(A) = 2

Portanto, a probabilidade de o evento A ocorrer é:

PQ4) =

n(X)

Também podemos dizer que a probabilidade é a razão entre o número de casos favoráveis ao evento e o número de casos totais:
p número de casos favoráveis número de casos totais
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ES(CLARECENDO!

Para utilizar a definição clássica, há uma condição crucial: todos os elementos do Espaço
Amostrai devem ser igualmente prováveis.

Se isso não for verdade, não podemos utilizar a definição clássica de probabilidade.

Por exemplo, se tivermos uma moeda viciada, em que a probabilidade de cair CARAé maior que a probabilidade de cair COROA, não poderemos utilizar a definição clássica.
I«** IX

(FGV/2019 - Prefeitura de Angra dos Reis/RJ) Uma pesquisa feita com os alunos de uma sala mostrou que
7 alunos torcem pelo Flamengo, 6 pelo Vasco, 5 pelo Fluminense, 4 pelo Botafogo e 3
não torcem por time nenhum. Escolhendo ao acaso um dos alunos dessa turma, a probabilidade de que ele seja torcedor do Vasco é de
Comentários:

A probabilidade de escolher um torcedor do Vasco equivale à razão entre o número de torcedores do Vasco(casos favoráveis) e o número de alunos (casos totais):

número de casos favoráveis n(V)

P =

O número total de alunos é de:

número de casos totais n(lT)

n([/) = 7 + 6 + 5 + 4 + 3 = 25

O número de torcedores do Vasco é n(V) = 6. Logo, a probabilidade desejada é:

P = — = 0,24 = 24%

Gabarito: D.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= (VUNESP/2020 - PM/SP) Em um pote, há 60 balas, todas de mesmo tamanho e formato, embaladas
I

; individualmente. Desse total, 25 são balas de leite com recheio de chocolate, 15
são balas de café sem

= recheio, e as demais são balas de frutas também com recheio de chocolate.
Retirando-se aleatoriamente

= uma bala desse pote, a probabilidade de que ela tenha recheio de chocolate é de

I

i Comentários:

A probabilidade de escolher uma bala com recheio de chocolate é a razão entre o número de balas com
= recheio de chocolate (casos favoráveis) e o número de balas no total (casos totais):

I

: nfcasos favoráveis) n(RC)

; nfcasos totais) n(U)

= O enunciado informa que há 60 balas, logo, n(U) = 60.

: As balas com recheio de chocolate são as balas de leite e as balas de frutas, ou seja, todas as balas exceto as i balas de café. Sabendo que há 15 balas de café, o número de balas com recheio de chocolate é:
n(RC) = 60 - 15 = 45

: Logo, a probabilidade desejada é:

i 4-5 _ 3

! P ~ 6Õ~ 4

i Gabarito: B.

i (FCC/2017 - Secretaria da Administração/BA) Uma sala de aula com 40 alunos fez uma pesquisa sobre a
= ocorrência de dengue no contexto familiar. A pesquisa consistia em tabular, no universo de 120 pessoas, se
= cada aluno e seus respectivos pais e mães já tiveram dengue, ou não. As respostas estão tabuladas abaixo.
Alunos
Pais de alunos
Mães de alunos

Teve dengue

Não teve dengue

= Sorteando-se ao acaso uma das 120 pessoas pesquisadas, a probabilidade de que ela tenha respondido na
= pesquisa que já teve dengue é igual a

: a) 2,5%.

b) 2,3%.

j c) 7,8%.

d) 3,8%.

í e) 1,4%.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

i Comentários:

I

a

A probabilidade é a razão entre o número de casos favoráveis e o número de casos totais:

I

i casos favoráveis nÇD')
: casos totais nÇU')

= Os casos favoráveis correspondem às pessoas que tiveram dengue. A tabela mostra que o número de pessoas que tiveram dengue é:
n(D) = 1 + 2 = 3

= O enunciado informa que, no total, 120 pessoas participaram da pesquisa: n(U) = 120.
i Assim, a probabilidade desejada é:

j Gabarito: A.

I

PW = ifõ = = 2'5%

i

I

i (CESPE/2018 - EBSERH) Uma pesquisa revelou característica da população de uma pequena comunidade
= composta apenas por casais e seus filhos. Todos os casais dessa comunidade são elementos do conjunto A U
= B U C, em que

I

A = {casais com pelo menos um filho com mais de 20 anos de idade};

i B = {casais com pelo menos um filho com menos de 10 anos de idade};

: C = {casais com pelo menos 4 filhos}.

I

I

: Considerando que n(P) indique a quantidade de elementos de um conjunto P, suponha que nÇA) = 18; j
= n(B) = 20; n(C) = 25; n(A n B) = 13; n(A n C) = 11; n(B A C) = 12 e n(A A B A C) = 8. O diagrama i i a seguir mostra essas quantidades de elementos.i

Com base nas informações e no diagrama precedentes, julgue o item a seguir.

Se um casal dessa comunidade for escolhido ao acaso, então a probabilidade de ele ter menos de 4 filhos será superior a 0,3.
Comentários:

A probabilidade é a razão entre o número de casos favoráveis e o número de casos totais:

casos favoráveis rifE)

casos totais nÇU')

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= Os casos favoráveis correspondem ao número de casais com menos de 4 filhos.
Sabendo que C representa =I

; os casais com pelo menos 4 filhos, então os casais com menos de 4 filhos são aqueles que não estão em C, ;
: conforme indicado abaixo:

= Assim, o número de casos favoráveis é:

: E o número de casos totais é:

= Logo, a probabilidade é:

n(E) = 2 + 5 + 3 = 10

n(U) = 2 + 5 + 3 + 3 + 8 + 4+10 = 35

j P = 35"°'286

= Ou seja, é inferior a 0,3.

i Gabarito: Errado.

; (FGV/2022-PC/RJ) Treze cadeiras numeradas consecutivamente de 1 a 13 formam uma fila. Quatro pessoas i devem sentar-se nelas e o número da cadeira em que cada uma deve se sentar será decidido por sorteio, i
= Para as três primeiraspessoas foram sorteados os números 3, 8 e 11 e será feito osorteio para a últimaj
= cadeira a ser ocupada.A probabilidade de que aquarta pessoa NÃO sesenteao lado de nenhumapessoa já i i sentada é:
i j a) 1/2j b) 1/4j c) 2/5
d) 7/10
j e) 4/13

I

i Comentários:

I

I

: O enunciado informa que há 13 cadeiras e que três pessoas ocupam as cadeiras 3, 8
e 11; e pede a ;

= probabilidade de a quarta pessoa não se sentar ao lado de ninguém.
;

A probabilidade é a razão entre o número de eventos favoráveis e o número total de eventos possíveis:

: eventos favoráveis n(A)
í

: eventos possíveis n(lT)
=

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Os eventos possíveis correspondem às 13 - 3 = 10 cadeiras restantes:

n(t/) = 10

E os eventos favoráveis correspondem às cadeiras que não estão ao lado de ninguém sentado, ilustradas a seguir, em que P representa uma pessoa sentada e X representa uma cadeira ao lado de uma pessoa sentada:
X P X

1 2 3 4 5

X P

6 7 8

X X P

9 10 11

X

12 13

Podemos observar que há 4 cadeiras que não estão ao lado de ninguém sentado (eventos favoráveis):
nQ4) = 4

E a probabilidade é a razão:

Gabarito: C

nÇA) 4 2

P = n(lT) = ÍÕ = 5

Para resolver diversas questões de probabilidade, envolvendo a definição clássica, será necessário utilizar as técnicas de análise combinatória, para calcular o número de elementos do evento e/ou o número de elementos do Espaço Amostrai.
EXEMPLIFICANDO

Vamos supor haja 5 peças amarelas e 6 peças verdes dentro de um saco e que teremos que retirar 2 peças sem olhar. Qual é a probabilidade de retirar 2 peças amarelas?
A probabilidade é a razão entre o número de casos favoráveis e o número de casos totais:

casos favoráveis n(A)
casos totais n(LT)

Os casos favoráveis são as maneiras de retirar 2 dentre as 5 peças amarelas. Como a ordem não importa, temos a combinação 2, dentre 5 elementos:
n(i4) — C₅ ₂ —

5!
(5—2)!x2!

5X4X3!

3!x2!

Os casos totais são as maneiras de retirar 2 peças, de um total de 11 peças (entre amarelas e verdes), também sem importância de ordem:
z77x ~ 11! 11X10X9! 11X10 --n
C = ---------- — =-- =- -=
2)!X2! 9!x2! 2

n 10Logo, a probabilidade de retirar 2 peças amarelas e: P

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E se a ordem importasse?

EXEMPLIFICANDO

Vamos supor, então, que há 5 mulheres e 6 homens, dos quais 2 serão escolhidos para ocupar a posição de presidente e vice-presidente do grupo.
Qual seria a probabilidade de escolher mulheres para ambos os cargos?
A probabilidade é calculada pela razão:

p casos favoráveis n(A}

casos totais n((7)
Os casos favoráveis são as maneiras de escolher 2 mulheres, dentre as 5, sendo que a ordem importa, por serem cargos distintos:
Os casos totais são as maneiras de escolher 2 pessoas, de um total de 11 (dentre mulheres e homens), também com importância de 1o1r!dem: 11X10X9! = 1X x 1Q = 11Q
n(L7) = 4112 =11'rz (11-2)1

Logo, a probabilidade de escolher 2 mulheres é:

P = — ¹⁰

110 55

Esse é o mesmo resultado que obtivemos antes!

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Quando estivermos escolhendo o mesmo número de elementos, com o mesmo critério em relação à importância da ordem, tanto nos casos favoráveis, quanto nos casos totais,não faz diferença se consideramos que a ordem importa ou não!

Se a ordem importa, temos o arranjo, tanto para os casos favoráveis, quanto para os totais.Para o nosso exemplo das 5 mulheres e 6 homens, a probabilidade de escolher 2
mulheres para cargos distintos foi calculada como:
5!

(5-2)!

11!

(11-2)!

Se a ordem não importa, temos a combinação, tanto para os casos favoráveis, quanto para os casos totais. Para o nosso exemplo das 5 peças amarelas e 6 peças verdes, a probabilidade de escolher 2 peças amarelas, sem importância de ordem, foi:
5!
(5—2)!x2!

ll!

(11—2)!x2!

5!

(5-2)!

11!

(11-2)!

Ou seja, o cálculo da probabilidade será o mesmo, independentemente de a ordem importar ou não!
I«** IX

(FGV/2019 - Prefeitura de Salvador/BA) Entre 6 deputados, 3 do Partido A e 3 do
Partido B, serão sorteados
2 para uma comissão. A probabilidade de os 2 deputados sorteados serem do Partido A é de:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

^Comentários:

A probabilidade é a razão entre o número de casos favoráveis e o número de casos totais:

I

: p nfcasos favoráveis) n(A)

: nfcasos totais) n(U)

iOs casos totais são as maneiras de escolher 2 deputados, dentre todos os 6 (sem importância de ordem):i 6!
6x5x4! 6x5

n(U) - C6:2 - ç6_2y x 2! - 4! x 2! - 2 _ 15

iOs casos favoráveis são as maneiras de escolher 2 deputados, dentre os 3 do Partido
A (também sem iimportância de ordem):
i . . 3!
3x2!
j - C3,2 - (3 _ 2)| x 2! - 1; x
2! - 3

I

ÍLogo, a probabilidade desejada é:

í 3

P ~ 15 ~ 5

ÍGabarito: D.

:(CESPE/2017 - PM-MA) Uma operação policial será realizada com uma equipe de seis agentes, que têm prenomes distintos, entre eles André, Bruno e Caio. Um agente será o coordenador da operação e outro, o jassistente deste; ambos ficarão na base móvel de operações nas proximidades do local de realização da ioperação. Nessa operação, um agente se infiltrará, disfarçado, entre os suspeitos, em reunião por estes imarcada em uma casa noturna, e outros três agentes, também disfarçados, entrarão na casa noturna para prestar apoio ao infiltrado, caso seja necessário. A respeito dessa situação hipotética, julgue o item seguinte.
Ê Se os dois agentes que ficarão na base móvel forem escolhidos aleatoriamente, a probabilidade de André e
= Bruno serem os escolhidos será superior a 30%.

I

: Comentários:

jPara calculara probabilidade, temos:

I

: casos favoráveis nQ4)

: casos totais n(U)

;Os casos totais correspondem a todas as maneiras de escolher um coordenador e um assistente, dentre 6jagentes. Considerando que os cargos são distintos, temos um arranjo de 2 elementos, dentre 6:

. z x

6! 6x5x4!

i n(U) = A6i2 = 2)1 = —— =
6 x 5 = 30

;Os casos favoráveis correspondem às maneiras de escolher André e Bruno como coordenador e assistente,iem qualquer ordem. Podemos ter André como coordenador e Bruno como assistente OU Bruno como
; coordenador e Bruno como assistente. Logo, há 2 possibilidades: n(A) = 2. Assim, a probabilidade é:
I 7 «

Que é inferior a 30%.

= Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FCC/2016 - Conselho Regional de Medicina/SP) Em dezembro serão vistoriados 10
estabelecimentos de saúde, sendo 2 hospitais, 1 pronto-socorro, 3 ambulatórios e 4 postos de saúde.Sorteando-se ao acaso a ordem de visita dos 10 estabelecimentos, a probabilidade de que os dois primeiros sejam postos de saúde é igual a a)2/15b) 4/25

c) 2/25

d) 3/20

e) 3/25

Comentários:

Para calcular a probabilidade de 2 postos de saúde serem os primeiros vistoriados
(evento A), utilizamos a definição clássica de probabilidade:
PQ4) =

n(X)

n(t/)

O Espaço Amostrai corresponde a todas as possibilidades de se ordenar 10 elementos:

n(t/) = P₁₀ = 10!

O evento A corresponde às possibilidades de se escolher 2 postos de saúde, dentre 4,
sendo a ordem relevante (arranjo), E de escolher a ordem dos demais 8 elementos(permutação). Pelo princípio multiplicativo (análise combinatória), temos:
4!

nQ4) = X4i2 x 8! = — x 8! = 4x3x8!

A probabilidade do evento A é, portanto:

z x nQ4) 4X3X8! 4X3 2 2

v 7 n([/) 10! 10x9 5x3 15

Gabarito: A

L.................... .

Probabilidade como Frequência Relativa ou Empírica

Agora, vamos supor que estejamos observando os resultados de um experimento, repetidos N vezes.

Sabendo que um evento específico ocorreu n vezes, de um total N repetições,
podemos calcular a frequência relativa (ou empírica) do evento, pela fórmula:
n- de observações do evento n

? n- total de repetições N

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vamos supor que estejamos observando os resultados de sucessivos lançamentos de uma moeda. Afrequência da face COROA será a razão entre o número de vezes em que obtemos COROA
e o número total de lançamentos efetuados:
n(C0R0A)

nÇLançamentos)

Para ilustrar esse experimento, utilizei o excel para gerar resultados aleatórios,
considerando que 0 (zero)
representa CARA e 1 representa para COROA.

Adotando esse procedimento para 100 células, ou seja, N = 100, obtive 48 vezes o número 1 (COROA), isto é,n = 48 (se você fizer esse procedimento, é bem possível que obtenha outro resultado).Portanto, temos a seguinte frequência relativa para COROA:

Esse resultado é próximo da probabilidade de 50% que conhecemos, porém diferente. Para
N = 1.000,
obtive 505 vezes o número 1, portanto:

1.000

50,5%

Agora, o resultado ficou mais próximo. Em um último teste, com N = 10.000, obtive n
= 5016:

5.016

10.000

50,16%

Observe que estamos nos aproximando cada vez mais do valor de 50%. Ou seja, não podemos dizer que a frequência é exatamente igual à probabilidade. Porém, quanto maior for o número de experimentos, mais a frequência relativa se aproxima da probabilidade.
INDO MAIS

FUNDO!

Para infinitas repetições, a probabilidade se torna igual à frequência relativa:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Essa definição de probabilidade pode ser utilizada para eventos que não são igualmente prováveis, em que a definição clássica não pode ser aplicada.
Por exemplo, para uma moeda não equilibrada, se verificamos, após muitos experimentos,
que obtemos 1
face COROA a cada 4 lançamentos, então a probabilidade de obter COROA é:

n 1

l«** IX

r f i (2019 - Prefeitura de Candói/PR) Em uma obra foram entregues 8 milheiros de tijolos maciços.Sabe-se que,
durante o transporte, em média 100 tijolos são danificados. Qual é a probabilidade de, ao acaso,
selecionar

= um tijolo, e ele estar danificado?
í a) 0,00125%

b) 0,01257o j c) 0,1257o d) 1,257o í e) 12,57o i Comentários:
I

I

: Para resolver essa questão, devemos calcular a probabilidade a partir da frequência relativa observada:
í n 100 1
=

í P = ^« = ãõõõ=8Õ = °'0125 = 1'25%
í

Li .G...a..b..a..r..i.t.o..:...D..

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

CoMBINAçõES DE EVENToS

Nessa seção, veremos formas de combinar eventos. Para esse estudo, pode ser bastante proveitoso utilizar o Diagrama de Venn, ilustrado abaixo para dois eventos A e B quaisquer, dentro de um EspaçoAmostrai (U).

Teorema da União

A união do evento A com o evento B, que representamos como AuB, é um novo evento,
em que estão incluídos tanto os elementos de A quanto os elementos de B.
Dizemos que, para ocorrer o evento união, pode ocorrer o evento A ou o evento B (ou ambos). A união corresponde a toda a região cinza indicada no diagrama abaixo.
Por exemplo, considerando o lançamento de um dado, se o evento A representa os resultados menores que4 e o evento B representa os resultados maiores que 3, então a união dos eventos corresponde aos valores menores que 4 ou maiores que 3.
Temos, portanto, os seguintes subconjuntos:

A = {1, 2, 3}

B = {4, 5, 6}

Au B = {1, 2, 3, 4, 5, 6}

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TOME

NOTA!

Quando a união de eventos corresponde a todo o Espaço Amostrai, dizemos que tais eventos são exaustivos.
Eventos A e B Exaustivos: Au B = U

No exemplo que acabamos de ver, a união corresponde à soma dos elementos de A e os elementos de B.

Agora vamos supor que o evento C corresponda aos resultados menores que 5 e o evento
D, aos resultados maiores que 3:
C = {1, 2, 3, 4}

D = {4, 5, 6}

Cu D = {1,2, 3, 4, 5, 6}

Nesse caso, somamos os elementos de C e os elementos de D, mas com atenção para não duplicar os elementos que constam em C e em D (nesse exemplo, o número 4).
Os elementos que constam em ambos os eventos pertencem à interseção desses eventos, a qual representamos como C n D, e corresponde à região cinza indicada no diagrama abaixo.
Nesse último exemplo, temos:

C n D = {4}

No exemplo anterior, em que A = {1, 2, 3} e B = {4, 5, 6}, não havia elementos que pertencessem tanto ao evento A, quanto ao evento B, ou seja, a interseção é um conjunto vazio:
A n B = 0

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TOME

NOTA!

Para calcular o número de elementos na união de C e D, sem duplicarmos os elementos da interseção,somamos os elementos de ambos os eventos e subtraímos os elementos da interseção, para que não sejam somados duas vezes:
n(C U D) = n(C) + n(D)-n(C n £>)

Dividindo todos esses termos por n(U), obtemos a fórmula da probabilidade da União:

n(C U D) n(C) , n(D) n(C n D)

n(I7) ~ n((7) + n((7) n(I7)

P(C U D) = P(C) + P(D)-P(C n D)

Por exemplo, sendo C = {1, 2, 3, 4}, D = {4, 5, 6} e C n D = {4}, as probabilidades dos eventos C, D e da interseção, considerando o Espaço Amostrai U = {1, 2, 3, 4, 5, 6}, são, respectivamente:
P(C) =

n(C) 4

P(D) =

n(D) _ 3

, , n(C n D) 1

p(Cnr>) =

n((7) 6' n(I7) " 6' n(jT)

Com base nessas probabilidades, podemos calcular a probabilidade da união:

ᶻ ˣ ᶻ ˣ ᶻ ˣ ᶻ ,4316P U D) P(C
P(£>) (CnD) - + 1

6 6 6 6

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para eventos mutuamente excludentes, isto é, que não possuem elementos em sua interseção, como no caso de A = {1, 2, 3} e B = {4, 5, 6}, a probabilidade da interseção é zero:
P(A n B) =

n(A n B)

n(B)

n(B)

Portanto, a probabilidade da união de eventos mutuamente excludentes pode ser calculada como:

P(A uB) = P(A) + P(B) - P(A n B)

1 1 1

P(A U B) = P(A) + P(B)

Para o exemplo em que A = {1, 2, 3}, B = {4, 5, 6}, as probabilidades dos eventos A e B,
considerando o Espaço
Amostrai U = {1, 2, 3, 4, 5, 6}, são, respectivamente:

PG4) =

nÇA)
n(LT)

3 _ 1

P(B) =

6 _ 2'

n(B) _ 3 1

n(B) " 6 2

Como são eventos mutuamente excludentes, a probabilidade da união é:

PQ4UB) = PQ4) + P(B) = j + |= 1

Eventos A e B Mutuamente Excludentes: P(A n B) = P(0) = 0
Probabilidade da União (caso geral): P(C u D) = P(C) + P(D) - P(C n D)
Probabilidade da Uniãc de Eventos Excludentes: P(A u B) = P(A) + P(B)

r.................................................*

i

: (FGV/2018 - ALE/RO) Dois eventos A e B ocorrem, respectivamente, com 40% e 30% de probabilidade. A :í probabilidade de que A ocorra ou B ocorra é 50%. Assim, a probabilidade de que A e B ocorram é igual a
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

í a) 10%

b) 20%

; c) 30%

d) 40%

í e) 50%

i Comentários:

A probabilidade de A OU B ocorrer corresponde à união desses eventos, dada por:

P(A U B) = P(A) + P(B) - P(A n B)

; O enunciado informa que:

* p(A) = 40%
i * P(B) = 30%

í * PQ4 U B) = 50%

I

: Substituindo esses valores na equação da união, temos:

50% = 40% + 30% - P(A n B)

P(A n B) = 70% - 50% = 20%

j Gabarito: B

I

i (CESPE/2018 - BNB) Um tabuleiro quadrado e quadriculado, semelhante a um tabuleiro de xadrez, com 12
; linhas e 12 colunas, e, portanto, com 12 x 12 = 144 quadradinhos pintados: 54, na cor azul; 30, na cor
: marrom; 40, na cor amarela; e 20, na cor verde. A cada quadradinho é associado um cartão com dois
; números, que indicam a posição do quadradinho no tabuleiro; o primeiro número corresponde ao número da linha, e o segundo corresponde ao número da coluna. Por exemplo, o cartão com os números 5,10
= corresponde ao quadradinho posicionado na linha 5 e na coluna 10. Esses cartões estão em uma urna, da qual podem ser retirados aleatoriamente.

A respeito desse tabuleiro e desses cartões, julgue o item a seguir.

I A probabilidade de retirar dessa caixa, de maneira aleatória, um cartão correspondente a um quadrado
; pintado na cor amarela ou na cor verde é superior a 0,44.

; Comentários:

A probabilidade de retirar um cartão da cor amarela ou na cor verde corresponde à probabilidade da união desses eventos.

: Considerando que não há interseção entre esses eventos (não existem quadrados amarelos E verdes), então
= a probabilidade da união é dada por:

P(A U 7) = PQ4) + P(V)

= Sabendo que há 40 quadrados amarelos e 144 quadrados no total, a probabilidade de retirar um quadrado
: amarelo é:

í z x n(A)
40 10

í v 7 n(B)
144 36

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= Considerando que há 20 quadrados verdes, a probabilidade de retirar um cartão verde é:

i , n(V)
20 5

i v 7 n(t/)
144 36

A probabilidade de retirar um cartão amarelo ou verde é, então:

i z x 10 5
15 5

I P(AUl,) = 36 + 36 = 36 = Í2S(W2

= Ou seja, é inferior a 0,44.
I

j Gabarito: Errado.

i (FCC/2019 -Secretaria de Estado da Fazenda/BA) Uma sala contém 20 homens e 30 mulheres em que todos
= são funcionários de uma empresa. Verifica-se que metade desses homens e metade dessas mulheres possuem nível superior. Escolhendo aleatoriamente uma pessoa dessa sala para realizar uma tarefa, a
; probabilidade de ela ser mulher ou possuir nível superior é igual a a) 2/3.
b) 3/10.

i c) 5/6.
d) 3/4.

| e) 4/5.

i Comentários:

I

: Essa questão envolve a união entre os eventos ser mulher (M) com possuir nível superior (S), cuja
; probabilidade é calculada por:

P(M U S) = P(M) + P(S) - P(M n S)

A questão informa que o número de mulheres é:

I

n(M) = 30

Sabendo que além dessas 30 mulheres, há 20 homens, então o total de pessoas é:

n(U) = 30 + 20 = 50

Logo, a probabilidade de escolher uma mulher é:

P(M) =

n(M) 30

n(I7) 50

A questão informa que metade de todas as pessoas possui nível superior. Logo o número de pessoas com nível superior é:
z > 50
n(S) = — = 25

Assim, a probabilidade de escolher uma pessoa com nível superior é:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= Por fim, o sabemos que metade das 30 mulheres possui nível superior. Então o número de mulheres com
: nível superior (interseção entre os eventos) é:

I

:

i n(M n S) = — = 15

; Logo, a probabilidade associada à interseção dos eventos é:
i r x n(MnS) 15

: P(MUS) = = —

ziÇíTj 50

; Substituindo os valores que calculamos na equação da probabilidade da união, temos:

z x 30 25 15 40 4

: P(MuS)- — + — - —- —

Lj .G...a..b..a..r.i.t..o E.

União de Três Eventos

A união de 3 eventos, A, B e C, pode ser representada pelo seguinte Diagrama de Venn:

Podemos observar que há diversos elementos que se repetiriam se simplesmente somássemos os elementos de A, de B e de C para encontrar a união dos três eventos. Na verdade, estaríamos somando duas vezes os elementos das interseções, 2 a 2, e três vezes os elementos da interseção de todos os conjuntos.
Porém, ao subtrairmos os elementos da interseção 2 a 2, estaríamos deixando de fora os elementos da interseção de todos os três eventos. Por isso, precisamos somádos novamente.
Assim, a união de 3 eventos é dada por:

n(A u B u C) = n(A) + n(B) + n(C)-n(71 nB)-n(B n C)-n(4 nC) + n(A nfínC)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Dividindo todos os termos por n(U), obtemos a fórmula da probabilidade da união de 3 eventos:

n(A u B u C) n(X) n(B) n(C) n(A n B) n(B n C) n(A n C) n(A nB n C)

n(B) n(B) + n(B) + n(B) n(B) n(B) n(B) + n(B)

P(A U B U C) = P(A) + P(B) + P(Q- P(X n B)-P(B n 0- P(A A C) + P(A A B A 0

Em vez de decorar a fórmula, pode ser mais simples utilizar o diagrama de Venn para encontrar o número de elementos da união n(A U B U C) e depois dividir o resultado por n(B).
EXEMPLIFICANDO

Vamos considerar as seguintes informações, a respeito das probabilidades de 3 eventos:

* P(A) = 1/2

* P(B)= 5/8

* P(A A B) = 1/4

* P(A n C) = 5/16

* P(B A C) = 3/8

* P(A n B n C) = 3/16

* P(A U B U C) = 1

Com essas informações, podemos calcular P(C). Para isso, vamos primeiro utilizar a fórmula da probabilidade da união e substituir as informações do enunciado:
P(AoBoC) = P(A) + P(B) + P(C) - P(AnB) - P(BnC) - P(AnC) + P(AnB nC)

1 = 1 + 5 + W) 1

8+10-4-5-6+3

2.

16 8 ' 16

1 = P(C) +

P(0 = 1 -- = -

8 8

Alternativamente, podemos utilizar o diagrama de Venn, e preencher os valores fornecidos, começando pela interseção de 3 eventos.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O valor de x corresponde à probabilidade dos elementos da interseção de A e B, A n
B, que não estão na interseção de todos os 3 eventos, A n B n C, isto é, a diferença entre P(A n B)eP(An Bn C):
x = PQ4Z n B)A - P(/l n BZ n C)\ = - - — = —4-3 — = —

4 lo lo lo

O valor de y corresponde à probabilidade dos elementos da interseção de A e C, A n
C, que não estão na interseção de todos os 3 eventos, A n B n C, isto é, a diferença entre P(A n C) e P(A n B n C):
x = P(A n C) - P(A n B n C) =

lo 16 16

O valor de z corresponde à probabilidade dos elementos da interseção de B e C, B n
C, que não estão na interseção de todos os 3 eventos, A n B n C, isto é, a diferença entre P(B n C) e P(A n B n C):
x = P(B n C) - P(A n B n C) = -

Inserindo esses valores no diagrama de Venn, temos:

/ a ,/í/16\ b \

13/16/

\ / 2/16 \/ 3/16 )

C j

C \

O valor de a corresponde à probabilidade dos elementos de A que não pertencem a qualquer interseção:
z 112 3

P(A) — x — y — P(A <1 B P\ C) = — — — — — — —

2 16 16 16

8-6 2

16 16

O valor de b corresponde à probabilidade dos elementos de B que não pertencem a qualquer interseção:
b = P(B) -x-z-PÇAHB nc)

5 13 3

8 16 _ 16 _ 16

10-7 3

16 "16

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, o valor de c pode ser calculado como a diferença entre a probabilidade da união dos 3
eventos e todos os demais campos. Para facilitar, em vez de subtrair todos os campos separadamente, podemos3 3subtrair P(A), b = — z = —:

' " 16 16

c = P(A U B U C) - PQ4) -b-z=l

13 3

2 16 _ 16

16-8-6 2

16 16

l«** IX

..
.......................................................... * «

i (FCC/2018 - SEPLAG de Recife/PE) Em um censo realizado em uma cidade em que são consumidos somente i i os sabonetes de marca X, YeZ, verifica-se que:i

; I. 40% consomem X.

i II. 40% consomem Y.
;

i III. 47% consomem Z.
;

;

: IV. 15% consomem X e Y.

I

I

: V. 5% consomem X e Z.
;

I

i VI. 10% consomem Y e Z.
;

= VII. qualquer elemento da população consome pelo menos uma marca de sabonete.
i

I

:Então, escolhendo aleatoriamente um elemento dessa população, a probabilidade de ele consumir uma e i
; somente uma marca de sabonete é igual a a) 79%.;

b) 70%.

; c) 60%.

d) 80%.

e) 76%.

I

I

; Comentários:

I

í Como toda a população consome alguma marca, então vamos aplicar a fórmula da probabilidade da união, i
: que vimos, para calcular a interseção de todos os eventos:

P(Xu Y u Z) = P(X) + P(Y) + P(Z) - P(X n Y) - P(X n Z)- P(Y nZ) + P(X n Y n Z) = 100%
40% + 40% + 47% - 15% - 5% - 10% + P(X n Y n Z) = 100%

P(X n Y n Z) = 100% - 97% = 3%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, vamos utilizar o diagrama de Venn.

Começamos preenchendo P(X n Y n Z). Em seguida, inserimos as interseções dois a dois,
subtraindo-se o valor de P(X n Y n Z). Por fim, inserimos os valores correspondentes a cada marca, individualmente,subtraindo-se todas as interseções.

Portanto, a probabilidade de o elemento consumir apenas uma marca é:

23% + 18% + 35% = 76%

Gabarito: E

Teorema do Evento Complementar

O complementar de um evento corresponde a todos os elementos do Espaço Amostrai que não pertencem a tal evento, como representado abaixo (a região em cinza corresponde ao complementar de A).
No exemplo do lançamento de um dado, em que C = {1, 2, 3, 4}, o evento complementar de C, indicado por
C, corresponde ao seguinte subconjunto:

C = {5,6}

Por definição, o número de elementos do evento somado ao número de elementos do complementar é igual ao total de elementos:
n(C) + n(C) = n(t/)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Dividindo toda a equação por n(U~), podemos calcular a probabilidade do evento complementar:

n(C) n(C) n(í/)

n(t/) + n(t/) n(í/)

P(C) + P(C) = 1

P(C) = 1 - P(C)

Para o exemplo do lançamento do dado, em que C = {1, 2, 3, 4} e o Espaço Amostrai é U = {1,2, 3,4, 5,6},a probabilidade do evento C é:

4 2

6 3

Pelo Teorema do Evento Complementar, a probabilidade do seu complementar é:

P(C) = l-P(C) = i-| = |

De fato, sabemos que o evento complementar é C = {5,6}. Pela definição clássica de probabilidade,
temos:

P(C) =

n(C) _ 2 1

n(i7) _ 6 3

Que é justamente o resultado que encontramos aplicando o Teorema do Evento Complementar.

I«** IX

r f i (2019 - Prefeitura de Palhoça/SC) Uma urna tem dez bolas vermelhas, três azuis e duas pretas. Qual é i
; probabilidade de sortearmos uma bola que não seja da cor vermelha?
j a) 33,33%

b) 45,66%

; c) 38,23%
;

d) 25,45%

i Comentários:

i A probabilidade do evento complementar é:
i

P(Ã) = 1-PQ4)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A probabilidade de sortear uma bola vermelha, sabendo que há 10 bolas vermelhas e 15 bolas no total, é:
Assim, a probabilidade de não sortear uma bola vermelha é:

15 - 10

=

| = 33,33%

Gabarito: A

(CESPE/2018 - BNB) Um tabuleiro quadrado e quadriculado, semelhante a um tabuleiro de xadrez, com 12linhas e 12 colunas, e, portanto, com 12 x 12 = 144 quadradinhos pintados: 54, na cor azul; 30, na cor marrom; 40, na cor amarela; e 20, na cor verde. A cada quadradinho é associado um cartão com dois números, que indicam a posição do quadradinho no tabuleiro; o primeiro número corresponde ao número da linha, e o segundo corresponde ao número da coluna. Por exemplo, o cartão com os números 5,10corresponde ao quadradinho posicionado na linha 5 e na coluna 10. Esses cartões estão em uma urna, da qual podem ser retirados aleatoriamente.
A respeito desse tabuleiro e desses cartões, julgue o item a seguir.

A probabilidade de retirar dessa caixa, de maneira aleatória, um cartão correspondente a um quadrado que não tenha sido pintado na cor marrom é inferior a 0,72.
Comentários:

A probabilidade de retirar um cartão que não seja marrom pode ser calculada pelo teorema do evento complementar:
P(M) = 1 - P(M)

A probabilidade de retirar um cartão marrom é a razão entre o número de cartões marrons e o número de cartões no total:
O enunciado informa que há:

-144 quadrados, logo, n(U) = 144; e

- 30 quadrados marrons, logo n(M) = 30

P(M) =

n(M)

n(I7)

Assim, a probabilidade de retirar um cartão marrom é:

r . 30 15

P(M) = = —

V 7 144 72

A probabilidade de retirar um cartão não marrom é complementar:

15 72 - 15 57

P(M) = 1 - — = — = — = 0,79

72 72 72

Que é superior a 0,72.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Complementar da União e da Interseção

O Teorema do Evento Complementar PQ4) = 1 - P(A) pode ser aplicado, mesmo quando o evento A for resultado de uma combinação de eventos, seja a união seja a interseção.
O complementar da união está representado pela região cinza indicada no diagrama abaixo:

Pelo Teorema que acabamos de ver, a probabilidade do complementar da união é dada por:

P(AUB) = 1 - P(A U B)

Já o complementar da interseção está representado pela região cinza indicada a seguir:

Pelo Teorema que acabamos de ver, a probabilidade do complementar da interseção é:

p(A n B) = l - P(A n B)

As seguintes relações também são importantes:

Item. 1. Á n B = Au B então P(Â n B) = P(T4 U B) = 1 - P(4 U B)

A interseção entre o complementar de A e o complementar de B é igual ao complementar da união do evento A com o evento B, como ilustrado a seguir.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

De fato, a situação do tipo "nem A nem B" significa a interseção dos complementares:

não A E não B

Essa situação implica que não temos qualquer elemento de A ou B, ou seja, o complementar da união.

E já sabemos calcular a probabilidade do complementar da união:

P(Ã OB) = P(TÜB) = 1 - P(A U B)

Por exemplo, em um lançamento do dado, em que o Espaço Amostrai é U = {1, 2, 3,
4, 5, 6}, vamos supor que o evento A corresponda a todos os números pares: A = {2, 4, 6} e o evento Bcorresponda aos números menores que 4: B = {1, 2, 3}.
A união dos eventos é A U B = {1, 2, 3, 4, 6} e sua probabilidade é:

P(A U B)

n(A U B) 5

n(B) 6

Aplicando a fórmula, podemos calcular a probabilidade de não ocorrer A nem B (não A E não B):

- - , 5 1

P(A n B) = 1 - P(A U B) = 1 - - = -

6 6

De fato, podemos observar que o elemento que não pertence ao evento A e nem ao evento B éÃ n B = [5],cuja probabilidade é:

P(A n B)

n(A n B) 1

Que é justamente o resultado que obtivemos aplicando a fórmula P(A n B) = 1 — P(A U B).

Item. 2. A U B = A n B então Pfd U B) = P(4 n B) = 1- P(Â A B)

A união do complementar de A com o complementar de B é igual ao complementar da interseção de A e B,
como ilustrado abaixo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vamos supor que em um restaurante haja x pessoas que estejam comendo e bebendo, c pessoas que estejam só comendo e b pessoas que estejam só bebendo.
Primeiro, pedimos que as pessoas que não estejam comendo se levantem (as b pessoas que estão somente bebendo se levantarão). Em seguida, pedimos que as pessoas que não estejam bebendo também se levantem(as c pessoas que estão somente comendo se levantarão).

Ao final, estarão em pé as c pessoas que estavam somente comendo e as b pessoas que estavam somente bebendo, isto é, todos menos as x pessoas que estavam fazendo as duas coisas(complementar da interseção)

- essas pessoas permanecerão sentadas.

Considerando o exemplo anterior do lançamento do dado, em que A = {2, 4, 6} e B =
{1, 2, 3}, a interseção dos eventos é A Cl B = {2} e sua probabilidade é:
P(A n B)

n(A n B) 1

n(í7) 6

Aplicando a fórmula que acabamos de ver, podemos calcular a probabilidade de não ocorrer o evento A OUnão ocorrer o evento B, que equivale à probabilidade de não ocorrer a interseção AhB:

1 5

P(AUB) = P(Aí)B) = l-P(Aí)B) = l- - = -

6 6

De fato, os elementos que não pertencem ao conjunto A são A = {1,3,5} e os elementos que não pertencem ao conjunto B são B = {4, 5,6}.
A união desses dois eventos complementares é ÂUB = {1,3,4,5,6}, que contém todos os elementos exceto a interseção A n B = {2}. E a probabilidade dessa união A U B é:
P(A U B)

n(A U B) 5

n(B) 6

Que é justamente o resultado que obtivemos aplicando a fórmula P(A U B) = 1 — P(A n B).

Esses casos podem ser extrapolados para diversos eventos. Para três eventos A, B e C, temos:

A n B n C = A U B U C P(A n B n C) = P(A U B U C) = 1 - P(A UBüC)

A u B u C = ÂnBnC P(Ã u B u C) = P(AnBn C) = 1 - P(A n B n C)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ESQUEMATIZANDO

Probabilidade Complementar: P(A) = 1 - P(A)

Interseção dos complementares = complementar da união:

P(Ã n B) = P(TÜB) = 1- P(A U B)

União dos complementares = complementar da interseção:

P(Ã UB) = P(TnB) = 1- P(A n B)

HORAM

i (FGV/2017 - SEPOG/RO) A probabilidade de que certo evento A ocorra é de 20%, a probabilidade de que o i
= evento B ocorra é de 30% e a probabilidade de que A e B ocorram é de 10%.
Assim, a probabilidade de que i

= nem A nem B ocorra é igual a:

a) 30%

b) 40%

; c) 50%

d) 60%

i e) 70%

i Comentários:

I

A probabilidade de que nem A nem B ocorra corresponde à interseção dos complementares, que, por sua i
= vez, equivale ao complementar da união:
j

P(ÃOB) = PQTÜB) = 1 - P(A U B)

: E a probabilidade da união é dada por:

: O enunciado informa que:

* P(A) = 20%
i * P(B) = 30%

i * P(A n B) = io%

P(A U B) = P(A) + P(B) - P(A n B)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Substituindo esses valores na equação da união, temos:

PQ4 U B) = 20% + 30% - 10% = 40%

O complementar da união, que a questão exige, é, portanto:

P(TÜB) = 1 - P(A U B) = 100% - 40% = 60%

Gabarito: D

i (2019 - Fundação Santo André/SP) Considere: Num campeonato de futebol descobriu-se que dos 1000torcedores, 440 torciam para o time A, 320 torciam para o time B.

I

Ao escolher uma pessoa no estádio, ao acaso, assinale a alternativa correta quanto à probabilidade dessa

: pessoa não torcer para nenhum desses times.
a) 24%

b) 76%

í c) 27%

d) 32%

i Comentários:

I

A interseção dos complementares (não A e não B) equivale ao complementar da união:

P(ÃOB) = PQTÜB) = 1 - P(A U B)

= Nesse caso, os eventos são mutuamente excludentes (A n B = 0), pois, ninguém torce para mais de um time. Por isso, a probabilidade da união é dada por:
í P(A U B) = PQ4) + P(B)

A probabilidade de uma pessoa torcer para A é a razão entre o número de torcedores de A, que é n(A)
= 440,

: e o número total de torcedores, que é n(U) = 1000. Logo:

nQ4) 440

P(71) =

n(t/) " 1000

A probabilidade de uma pessoa torcer para B é a razão entre o número de torcedores de B, que é n(B) = 320,e o número total de torcedores:

, n(B) 320

P®=írô = iõõõ = 32%

: Portanto, a probabilidade da união é:
I

P(A U B) = PQ4) + P(B) = 44% + 32% = 76%

= Dessa forma a probabilidade de uma pessoa não torcer para A e nem para B é:
I

P(A n B) = 1 - P(A UB) = 100% - 76% = 24%

i Gabarito: A

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= (CESPE/2013 - CBM/CE) Uma pessoa que possua sangue classificado como O- é considerada doadora
; universal pelo fato de seu sangue poder, em tese, ser ministrado a qualquer pessoa de qualquer tipo
; sanguíneo. A pessoa que possua sangue classificado como AB+ é considerada receptora universal pelo fato de poder receber, em tese, sangue proveniente de doador de qualquer tipo sanguíneo. Dentro de um mesmo
= grupo sanguíneo, os de fator Rh- podem doar aos de fator Rh+. O sangue 0+ pode ser doado para qualquer
= pessoa que possua sangue com fator Rh+. A tabela abaixo apresenta a distribuição do tipo sanguíneo e do
; fator Rh de membros de uma corporação.

Fator Rh

Rh+
Rh
Total grupo sanguíneo
A B AB O

12 15 18 21

16 11 6 1

28 26 24 22

Total

= Tendo como referência essas informações e a tabela acima, julgue o item que se segue.

= Escolhendo-se aleatoriamente um membro dessa corporação, a probabilidade de ele não ser nem receptor
= universal nem doador universal é superior à probabilidade de um membro dessa mesma corporação ter o
; fator Rh+.

Comentários:

I

A probabilidade de um membro não ser nem receptor universal (AB+) nem doador universal
(O.) corresponde à interseção dos complementares, que, por sua vez, equivale ao complementar da união desses eventos.
P(AB+ Cl 0_) = P(AB+ U 0_) = 1 - P(AB+ U CL)

A probabilidade de um membro ser receptor universal (AB+) é dada pela razão entre a proporção de receptores universais e o total. Pela tabela, observamos que n(AB+) = 18 e n(U) =Item. 100. Assim, a probabilidade de um membro ser receptor universal é:
P(AB+) =

n(AB+)

n(lT)

A probabilidade de um membro ser doador universal (O.) é dada pela razão entre a proporção de doadores universais e o total. Pela tabela, observamos que n(O-) = 1. Assim, a probabilidade de um membro ser doador universal é:
, , n(0_) 1

P(O_) = -^ = —=1%

n(U) 100

Considerando que não há interseção entre esses eventos (são eventos mutuamente exclusivos), então a probabilidade da união é dada por:
P(AB+ U CL) = P(AB+) + P(CL) = 18% + 1% = 19%

Assim, a probabilidade de a pessoa não ser doadora universal ou receptora universal é dada pelo Teorema do Evento Complementar:
I

P(AB+ U CL) = 1 - P(AB+ U CL) = 100% - 19% = 81%

Por outro lado, para calcular a probabilidade de uma pessoa ter Rh+, precisamos do número de pessoas comRh+: n(+) = 66. Logo, essa probabilidade é:

Í'(+) = T55 = 66%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Como 81% é maior que 66%, então a probabilidade de a pessoa não ser doadora ou receptora universal é,de fato, maior que a probabilidade de ela ter Rh+.

Gabarito: Certo.

(2018 - Conselho Regional de Medicina Veterinária/ES) Em uma pesquisa feita com 200
usuários de uma pasta de dente, verificou-se o seguinte:
- 76 usam a pasta de dente A

- 86 usam a pasta de dente B

-140 usam a pasta de dente C

- 68 usam a pasta de dente A e B

- 34 usam a pasta de dente A e C

- 48 usam a pasta de dente B e C

- 30 usam a pasta de dente A, B e C

Marque a probabilidade que, em um sorteio ao acaso de todos os usuários entrevistados,
é sorteado aquele que não utiliza nenhuma das três pastas apresentada.
a) 18%

b) 9%

c) 12%

d) 21%

e) 15%

Comentários:

A probabilidade de o sorteado não utilizar qualquer pasta, A, B e nem C, é:

P(Ã nBaC) = P(AUBU C) = 1 - P(7l U B U C)

Vimos na seção anterior que:

P(AuBuC) = P(A) + P(B) + P(C) - P(A n B) - P(B n C) - P(A n C) + P(A n B n C)

O enunciado informa que a pesquisa foi feita com 200 usuários e que:

- 76 usam a pasta de dente A, logo PQ4) = —
- 86 usam a pasta de dente B, logo P(B') = —

-140 usam a pasta de dente C, logo P(C) =

- 68 usam a pasta de dente A e B, logo P(A n B) = —

- 34 usam a pasta de dente A e C, logo P(A n C) = ~

- 48 usam a pasta de dente B e C, logo P(B n C) = —

- 30 usam a pasta de dente A, B e C, logo P(A A B A C) = — 30

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

„ x 76 86 140 68 34 48 30

P ÍX U B U C ) — 1 1 1

v 7 200 200 200 200 200 200 200

= Nota: se preferir, utilize o Diagrama de Venn para encontrar o número de elementos na união.
Depois, basta dividir pelo total (200) para encontrar a probabilidade da união. Assim:
P(A U B U C) = 1 - P(A U B U C)

Item. 182. 18

P(JÜBÜC) = 1- —= —=»

L; .G..a..b. .a..r.i.t.o. : B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

AXIoMAS DE PRoBABILIDADE

Os chamados axiomas são verdades tão básicas que dispensam qualquer demonstração. É a partir dessas verdades, que as propriedades e os teoremas são desenvolvidos. Em probabilidade, temos os Axiomas deKolmogorov. São eles:

Item. 1. PQ4) > 0

A probabilidade de qualquer evento é maior ou igual a 0, ou seja, não há probabilidade negativa.

Item. 2. P(17) = 1

A probabilidade associada a todo o Espaço Amostrai, ou seja, a todos os eventos possíveis, é igual a
1 (100%). Por exemplo, considerando o lançamento de um dado, qual é a probabilidade de ocorrer um dos resultados 1, 2, 3, 4, 5 ou 6? Como teremos algum desses resultados,certamente, então a probabilidade de ocorrer um desses eventos é 100% = 1.
Item. 3. Se A e B são mutuamente excludentes (X n B = 0), então a probabilidade da união desses eventos corresponde à soma das probabilidades dos eventos:
P(4 UB) = P(4) + P(B)

Com base nesses três axiomas, é possível deduzir as propriedades de probabilidade:

i) Evento impossível: Sendo A um evento impossível, a sua probabilidade é igual a zero:

Se A = 0, então P(Á) = 0

NA

PROVA!

Se um evento é impossível, então necessariamente a sua probabilidade é nula; mas o contrário não é necessariamente verdadeiro, ou seja, se a probabilidade de um evento é nula, não podemos concluir que tal evento é impossível.
Há eventos que são, em tese, possíveis, mas cuja probabilidade é nula. Por exemplo, ao lançarmos uma moeda infinitas vezes, é possível obter infinitas CARAs, mas a probabilidade disso é igual a zero.
Analogamente, se um evento é certo, então necessariamente a sua probabilidade é igual a
1, mas o contrário não é necessariamente verdadeiro, ou seja, se a probabilidade de um evento é igual a 1, não podemos concluir que tal evento é certo.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ii) Sendo A um evento qualquer, a sua probabilidade está entre 0 e 1:

0 < P(A) < 1

iii) Sendo A e B eventos quaisquer, a probabilidade de ocorrer A e não ocorrer B, que indicamos comoP(A - B) ou P(A \ B), é a diferença entre a probabilidade de A e a probabilidade da interseção:

P(A - B) = P(A) - P(A n B)

O evento A - B = A \ B está ilustrado a seguir:

iv) Se A e B são eventos tais que A implica B, isto é, A está contido em B (AÇ B), então a probabilidade de A é menor ou igual à probabilidade de B.
PQ4) < P(B)

Também são propriedades decorrentes dos Axiomas de Kolmogorov, a Probabilidade da União de eventos quaisquer e a Probabilidade do Evento Complementar:
P(A U B) = PQ4) + P(B) - P(A n B)

P(A) = 1 - PQ4)

ESQUEMATIZANDo

Axiomas

Item. 1. PQ4) > 0

Item. 2. P(B) = 1

Item. 3. Se A e B são mutuamente excludentes então P(A U B) = PQ4) + P(EP)

Propriedades i) Se A = 0, então PQ4) = 0
ii) 0 < P(X) < 1

iii) P(A - B) = PQ4\B) = P(X) - P(A n B)

iv) Se A Ç B, então PQ4) < P(EP)

V) P(A UB) = PQ4) + P(B) - P(A n B)

vi) P(Á) = 1 - P(A)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

HOftADf

(VUNESP/2016 - Prefeitura de Alumínio/SP -Adaptada) Uma moeda é viciada de modo que a probabilidade de sair cara é 4 vezes a de sair coroa.
A probabilidade de sair cara em um lançamento qualquer é a) 50%
b) 25%

c) 20%

d) 75%

e) 80%

Comentários:

Para calcular a probabilidade de sair CARA/COROA em um lançamento de uma moeda viciada, não podemos utilizar a definição clássica de probabilidade, pois os resultados não são equiprováveis.
Nesse caso, podemos calcular as probabilidades dos resultados utilizando o axioma P(U)
= 1, combinado com o dado do enunciado de que a probabilidade de sair CARA é 4 vezes maior que a probabilidade de sairCOROA.

Chamando a probabilidade de sair COROA de p, então a probabilidade de sair CARA é 4p. Logo:

P(lT) = 4p + p = 1

E a probabilidade de sair CARA é:

4p = - = 80%

Resposta: E

(FCC/2019 - SANASA/SP) O número de ocorrências diárias de um determinado evento foi registrado por um funcionário de uma empresa durante um longo período.
Esse trabalho permitiu, com o objetivo de análise, elaborar a distribuição de probabilidade conforme tabela abaixo, sabendo-se que o evento nunca ocorre mais que 5 vezes em um dia.
Número de ocorrências diárias
Probabilidade de ocorrência

0 1

0,20 p

2 3 4 5

2p 3p 2p P

A probabilidade de que em 1 dia o evento ocorra, pelo menos, uma vez, mas não mais que 3 vezes, é igual a
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 2/9

b) 1/3

c) 5/12

d) 4/5

e) 8/15

Comentários:

Primeiro, precisamos calcular o valor de p. Sabendo que a tabela corresponde a todo o
Espaço Amostrai,
uma vez que o evento nunca ocorre mais que 5 vezes no dia, temos:

0,20 + p + 2p + 3p + 2p + p = l
9p = 0,8

P~9Õ

A probabilidade de ocorrer pelo menos 1 vez e não mais de 3 vezes é:

8 8

P(l) + P(2) + P(3) = p + 2p + 3p = 6p = 6x — = —

Gabarito: E

(FCC/2017 - SABESP) Em um grupo de 100 pessoas, 80 possuem telefone celular, 50
possuem telefone fixo,
e 10 não possui telefone celular nem telefone fixo.

Sorteando-se ao acaso uma dessas 100 pessoas, a probabilidade de que ela tenha telefone fixo mas não tenha telefone celular é de a) 50%.
b) 5%.

c) 1%.

d) 20%.

e) 10%.

Comentários:

A questão informa que, de um total de 100 pessoas, 10 não possuem nem celular, nem fixo. Portanto, 90pessoas possuem celular ou fixo:

n(C) + n(F)-n(C A F) = 90

Além disso, o enunciado informa que n(C) = 80 e n(F) = 50. Substituindo esses valores, temos:

80 + 50-n(C A F) = 90
n(C A F) = 40

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ou seja, 40 pessoas possuem celular e fixo, conforme representado a seguir.

Portanto, o número de pessoas que têm fixo, mas não têm celular (evento F\C) é:

n(F\C) = n(F) - n(F n C) = 50 - 40 = 10

Sabendo que há n(U) = 100 pessoas no total, a probabilidade do evento F\C é:

, , n(F\C) 10

w^=^r=iõõ=10%

Gabarito: E

L..................................................... .

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

PRoBABILIDADE CoNDICIoNAL

A probabilidade condicional trabalha com a probabilidade de um evento ocorrer,
sabendo que outro já ocorreu.
Por exemplo, vamos supor que, em um auditório, existam enfermeiros e dentistas, tanto homens quanto mulheres. Podemos calcular a probabilidade de uma pessoa escolhida aleatoriamente ser enfermeiro,sabendo que é homem.

O fato de sabermos que a pessoa escolhida é homem corresponde a uma redução do universo de possibilidades - não estamos mais considerando todo o auditório, mas apenas os homens nesse auditório.Com esse "novo" universo, calculamos a probabilidade de esse homem ser enfermeiro.

Para ilustrar, vamos atribuir números a esse exemplo, conforme tabela abaixo:

Enfermeiros
Dentistas
Totais

Homens

Mulheres

Totais

Nesse caso, o "novo" universo são os 120 homens, ao invés de todas as 200 pessoas no auditório. Assim, a probabilidade de ser um enfermeiro pode ser calculado pela razão entre os casos favoráveis (número de enfermeiros) e os casos possíveis (número de homens), nesse "novo" universo:
p casos favoráveis nQ4)

casos possíveis n(U'')

_ 40 _ 1

P 12Õ ~ 3

O que fizemos foi dividir o número de enfermeiros e homens (interseção) pelo número de homens (evento que se sabe ter ocorrido).
n(E n H)

P =

n(fT)

Dividindo tanto o numerador quanto o denominador pelo número de elementos de todo o
Espaço Amostrai n(U), obtemos a fórmula da probabilidade de condicional do evento E, dado o evento H, indicada porP(E | H):

P(E|H) =

n(P n fí)
n((/)
n(H)

n(l7)

P(F n H)

PW

PÇE\H) = P(EnlT)

PW

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O evento que sabemos ter ocorrido (o evento "homem", no nosso exemplo) é chamado de evento a priori(ocorre antes). O outro evento é aquele cuja probabilidade queremos calcular (no nosso exemplo, o evento"enfermeiro"). Esse evento é chamado de evento a posteriori (ocorre depois).

É possível que a interseção dos eventos seja equivalente ao próprio evento a posteriori. Por exemplo,suponha que, dos 90 enfermeiros indicados na tabela, 10 tenham mais de vinte anos de profissão. Agora,vamos calcular a probabilidade de ter sorteado um enfermeiro com mais de vinte anos de profissão (X),sabendo que foi sorteado um enfermeiro. Essa probabilidade é dada por:

PCXIE) =

P(X n E)

P(F)

Ora, todos os enfermeiros com mais de vinte anos de profissão (X) pertencem ao grupo dos enfermeiros (E).Assim, a interseção X O E corresponde ao próprio evento X, logo:

P(X|E) =

P(X) n(X)

P(E) _ n(E)

10 1

P^ = 9Õ = 9

FIQUE

ATENTO!

Podemos efetuar as mesmas operações de combinação de eventos com a probabilidade condicional. Em especial, a probabilidade condicional complementar é:
P(Ê\H) = 1 — P(E\EE)

O complementar do evento E, dado H, é não E, dado H. Assim, o evento a priori, que sabemos que ocorreu, permanece como evento a priori.
Para o nosso exemplo, temos P(E|H) = -. Então, dado que foi selecionado um homem, a probabilidade de a pessoa selecionada não ser um enfermeiro, é:
P(Ê\H) = 1 — P(E\H~) = 1-^ = |

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

— PRATICAR! —

...................................... . 1

(VUNESP/2019 - Prefeitura da Estância Balneária de Peruíbe/SP) O gráfico a seguir apresenta dados referentes a homens e mulheres que se inscreveram para prestar um concurso para trabalhar em uma instituição pública. Entre os candidatos, alguns já tinham emprego.
- mulheres H homens

Um desses candidatos foi escolhido aleatoriamente. Sabendo-se que esse candidato não tem emprego, a probabilidade de que ele seja homem é:
a) 2/9

b) 4/9

c) 2/5

d) 1/5

e) 3/8

Comentários:

A questão pede a probabilidade de o candidato ser homem, dado que não tem emprego
(probabilidade condicional). Essa probabilidade pode ser calculada pela razão clássica entre os eventos favoráveis e os eventos totais, restringindo-os aos candidatos que não têm emprego (universo conhecido):
nÇHomens sem emprego}
n(Candidatos sem emprego}

Obs.: Se preferir, considere a definição de probabilidade condicional para calcular a probabilidade de o candidato ser homem (H), dado que não tem emprego (Ê):
P(H\E} =

P(H n E}

P&}

n(H n E}

Pelo gráfico, observamos que o número de homens sem emprego é:

n(H n E} = nÇHomens sem emprego} = 80

O gráfico informa também que o número de mulheres sem emprego é de 100. Logo, o número total de candidatos sem emprego é:
n(£) = nÇCandidatos sem emprego} = 80 + 100 = 180

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, a probabilidade desejada é:

Gabarito: B.

80 4

P(H\E) = —

180 9

I

Ii (CESPE/2018-ABIN) Como forma de melhorar a convivência, as famílias Turing, Russell e Gõdel disputaram,
; no parque da cidade, em um domingo à tarde, partidas de futebol e de vôlei. O quadro a seguir mostra os quantitativos de membros de cada família presentes no parque, distribuídos por gênero.
Família
Turing
Russell
Gõdel

Masculino

Feminino

A partir dessa tabela, julgue o item subsequente.

I

: Considere que, em eventual sorteio de brindes, um nome tenha sido retirado, ao acaso, do interior de uma
: urna que continha os nomes de todos os familiares presentes no evento. Nessa situação, sabendo-se que o
= sorteado não é uma mulher da família Gõdel, a probabilidade de ser uma mulher da família Russel será
= superior a 20%.

s i Comentários:
I

A questão indaga sobre probabilidade condicional. Podemos calcular essa probabilidade, utilizando a
= fórmula da probabilidade clássica, porém restringindo os casos considerados ao evento que sabemos ter
= ocorrido, no caso, o fato de não ser uma mulher da família Gõdel:

casos favoráveis nQ4)

casos possíveis n(U')

Obs.: Se preferir, considere a definição de probabilidade condicional para calcular a probabilidade de o sorteado ser uma mulher da família Russel (Mr), dado que não é uma mulher da Gõdel (MG):
P(Mr n MG)

P(MR\M(f) =

Perceba que a interseção entre as mulheres da família Russel e as pessoas que não são mulheres da famíliaGõdel, Mr n Mg, equivale exatamente às mulheres da família Russel, MR, logo:

P(M«) _ n(A^)

P(Mr|MG) =

= Ou seja, sabendo que o sorteado não é uma mulher da família Gõdel, então os casos possíveis correspondem
; a todos os familiares exceto as mulheres dessa família:

n(M7) = n(U') = 5 + 7 + 6 + 54-5 = 28

: Os casos favoráveis correspondem ao número de mulheres da família Russel:
i n(MR) = n(A) = 5

= Logo, a probabilidade é dada por:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ou seja, é inferior a 20%.

Gabarito: Errado.

(FCC/2018 - Banrisul/RS) Em uma empresa com 400 funcionários, 30% ganham acima de 5
Salários Mínimos
(S.M.). O quadro de funcionários dessa empresa é formado por 180 homens e 220
mulheres, sendo que 160
mulheres ganham no máximo 5 S.M. Escolhendo aleatoriamente 1 funcionário dessa empresa e verificando que é homem, a probabilidade de ele ganhar mais do que 5 S.M. é igual a a) 1/2.
b) 3/20.

c) 1/3.

d) 3/11.

e) 3/10.

Comentários:

A probabilidade de a pessoa ganhar mais que 5SM, dado que é homem, pode ser calculada como:

A questão informa que n(H) = 180, que representa o "novo Universo".

Também é informado que 30% dos funcionários ganham mais que 5SM: n(G) = 30% x 400 = 120.

Sabendo que 160 mulheres ganham menos que 5SM, então 220 - 160 = 60 mulheres ganham mais que 5SM.Então, o número de homens que ganham mais que 5SM é:

n(G OH) = n(G) - n(G n/f) = 120 - 60 = 60

Portanto:

Gabarito: C

(FGV/2022 - SEFAZ/ES) As probabilidades de dois eventos A e B são P[A] = 0,5, P[B]
= 0,8. A probabilidade condicional de A ocorrer dado que B ocorre é P[A| B] = 0,6. Assim, a probabilidade de que A ou B ocorram é igual a a) 0,56
b) 0,60

c) 0,76

d) 0,82

e) 0,94

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)
ívivw. estrategiaconcursos. com. br

Comentários:

O enunciado informa a probabilidade dos eventos A e B, bem como a probabilidade condicional de A, dadoB, a qual corresponde à razão entre a probabilidade da interseção e a probabilidade do evento a priori, no caso,o evento B:
PÇA\B) =

p(A n B)

P(B)

Sabendo que P(B) = 0,8 e que PQ41B) = 0,6, podemos calcular a probabilidade da interseção:

P(A n B)

P(A\B) =

0,8

= 0,6

P(A n B) = 0,6 x 0,8 = 0,48

Conhecendo as probabilidades P(A) = 0,5, P(B) = 0,8 e P(A n B) = 0,48,
podemos calcular a probabilidade da união (A OU B):
P(A \JB) = P(A) + P(B) - P(A n B) = 0,5 + 0,8 - 0,48 = 0,82

Gabarito: D

Teorema da Multiplicação

O Teorema da Multiplicação pode ser visto como uma forma diferente de escrever a fórmula da probabilidade condicional. Como vimos, a probabilidade condicional é:
P(BM) =

P(A O B)

P(^4)

O Teorema da Multiplicação fornece a probabilidade da interseção, a partir da probabilidade condicional:
P(A n B) = P(B|4) x PQ4)

Ou seja, a probabilidade da interseção de dois eventos é o produto da probabilidade condicional pela probabilidade do evento a priori.
Para o nosso exemplo anterior, vimos que a probabilidade de ter sido selecionado um enfermeiro, sabendo que foi homem é:
P(E|H) = |

Assim, conhecendo a probabilidade de selecionar um homem (evento a priori),
podemos calcular a probabilidade de selecionar um enfermeiro homem (interseção).
Para isso, vejamos novamente a tabela desse exemplo:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Enfermeiros
Dentistas
Totais

Homens

Mulheres

Totais

A probabilidade de selecionar um homem (evento a priori) é, pela definição clássica:

P(H) =

n(H')
n(U)

120 3

2ÕÕ 5

Agora, podemos calcular a probabilidade da interseção P(E n H), pelo Teorema da Multiplicação:

P(E nH) = P(E\H) x P(H) = | x | = |

De fato, aplicando a definição clássica de probabilidade para calcular a interseção, a partir da tabela, temos:
P(E n ET)

n(E n H)

n(I7)

40 _ 1

200 _ 5

Observe que podemos aplicar o Teorema da Multiplicação, invertendo-se os eventos a priori e a posteriori.Se, em vez de P(E|H), conhecêssemos P(H\E), poderíamos calcular a probabilidade da interseçãoP(E O ET) como:

P(E O H) = P(H\E) x P(E)

Já conhecemos a probabilidade da interseção, mas vamos efetuar os cálculos com essa inversão?

A probabilidade condicional de a pessoa selecionada ser homem, dado que é enfermeiro
(homem ou mulher)
é, pela tabela:

z , „ casos favoráveis 40 4

P(Ji\E) =

casos possíveis 90 9

E a probabilidade de selecionar um enfermeiro é, pela tabela (definição clássica):

„

P(F} =

n(E) 90 9

=----------------= —

v 7 n(t/) 200 20

Com P(H\E') e PÇE'), podemos calcular a probabilidade da interseção P(E n ET),
aplicando-se o Teorema da
Multiplicação:

P(E C\ H} = P(H\E) x P(F) = x |

Que é o resultado que obtivemos antes!

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para 3 eventos, a interseção é dada por:

P(A n B n C) = P(i4) x P(B|4) x P(C|t4 n B)

Ou seja, é a probabilidade do evento a priori (A), multiplicada pela probabilidade condicional do primeiro evento a posteriori (B|A), multiplicada pela probabilidade condicional do segundo evento a posteriori(C|AAB).

I«** IX

(VUNESP/2016 - Prefeitura de Alumínio/SP - Adaptada) Um estudante resolve uma prova com apenas questões em forma de testes de múltipla escolha, com 4 alternativas cada teste. Ele sabe 75% da matéria da prova. Quando ele sabe a matéria da questão ele acerta e, quando não sabe, escolhe a alternativa ao acaso.
A probabilidade de o aluno acertar uma questão qualquer por acaso é igual a a) 6,25%
b) 8,5%

c) 15%

d) 17,25%

e) 18,75%

Comentários:

A probabilidade de o aluno acertar uma questão qualquer por acaso corresponde à interseção dos eventos"não saber a matéria" (que podemos chamar de S) E "acertar a questão" (que podemos chamar de A) é:

P(SnX)

Considerando que a probabilidade de o aluno acertar a questão depende do evento saber ou não a matéria,a probabilidade da interseção é dada por:

P(5n/1) = P(S)xP(2l|S)

O enunciado informa que:

* O aluno sabe 75% da matéria da prova: P(S) = 0,75

Logo, o aluno não sabe o restante da matéria (evento complementar):

P(S) = 1 - P(S) = 1 - 0,75 = 0,25

* O aluno escolhe a alternativa ao acaso, se ele não souber a matéria.

Havendo 4 alternativas, a probabilidade de o aluno acertar a questão, dado que não sabe a matéria é:
PUIS) = - = 0,25

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= Substituindo esses valores na fórmula da probabilidade da interseção, obtemos a probabilidade de o aluno
; acertar uma questão qualquer por acaso:

P(sn7l) = 0,25 x 0,25 = 0,0625 = 6,25%

E

; Gabarito: A

i (VUNESP/2019 - Prefeitura de Campinas/SP) Ao operar em um turno de trabalho, uma linha de produção
= se interrompe totalmente se uma máquina Ml falhar. Para diminuir o risco de interrupção, ligou-se ao i sistema uma máquina M2 programada para entrar imediatamente em funcionamento caso Ml falhe,
Ii fazendo com que o sistema prossiga. A probabilidade de Ml falhar é de 1/20 e a probabilidade de M2 falhar
: é também de 1/20. A probabilidade de que o sistema não se interrompa durante um turno de trabalho após
= a inclusão de M2 é de j a) 99,75%
b) 95%

j c) 99%

d) 90,25%

; e) 97,5%

i Comentários:

I

A probabilidade de o sistema não se interromper pode ser calculada pelo complementar de ele se
= interromper:

P(7) = 1 - P(7)

= Para o sistema se interromper, é necessário que a máquina Ml falhe E que a máquina M2 falhe. Logo, temos i a interseção desses eventos:
P(7) = P(F1) xP(F2|Fl)

i Representamos a falha da M2 como F21 Fl, pois a máquina atua somente se a Ml falhar.

= O enunciado informa que a probabilidade de tanto uma quanto outra falhar é de 1/20:

| í,(') = ^X2Í = 4ÕÕ = 0'0025

i Assim, a probabilidade de o sistema não interromper é complementar:

P(7") = 1 - P(7) = 1 - 0,0025 = 0,9975 = 99,75%

Gabarito: A.

i (FGV/2018 - ALE/RO) Uma urna I contém inicialmente 4 bolas azuis e 6 bolas vermelhas; nessa ocasião, a
; urna II contém 5 bolas azuis e 4 bolas vermelhas, e a urna III, 2 azuis e 7 vermelhas. Uma bola é sorteada da
; urna I e colocada na urna II. Em seguida, uma bola é sorteada da urna II e colocada na urna III.
Por fim, uma bola é sorteada da urna III. A probabilidade de que a bola sorteada da urna III seja azul é igual a j a) 0,166
b) 0,182

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

í c) 0,254

d) 0,352

; e) 0,368

i Comentários:

A probabilidade de retirar uma bola azul da urna III depende de qual bola é retirada da urna II,
que, por sua

= vez, depende de qual bola é retirada da urna I, conforme ilustrado abaixo:

2 bolas azuis

:
7 + 1 bolas vermelhas

= Na figura, temos as quantidades de bolas nas urnas, para cada caso, o que nos permite calcular a
; probabilidade de retirar uma bola azul ou vermelha, em cada etapa.

K

; Para encontrar a probabilidade de tirar uma bola azul, precisamos da interseção dos eventos subsequentes
= (retirada da urna 1, da urna 2 e da urna 3) e da união das possibilidades alternativas (isto é, dos diferentes
; caminhos).

K

A probabilidade do primeiro caminho (superior) é dada por:

P(A1 n >12 n >13) = PQ41) x P(A2)A1) x P(A3|>12) = 0,4 x 0,6 x 0,3 = 0,072

A probabilidade do segundo caminho é:

P(A1 n 72 n >13) = PQ41) x P(V2\A1) x PQ43|72) = 0,4 x 0,4 x 0,2 = 0,032

A probabilidade do terceiro caminho é dada por:

P(V1 n A2 n >13) = P(71) x P(>12|71) x PQ43|>12) = 0,6 x 0,5 x 0,3 = 0,09

A probabilidade do quarto caminho (inferior) é dada por:

i P(71 n 72 n >13) = P(71) x P(72|71) x P(A3172) = 0,6 x 0,5 x 0,2 = 0,06

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= E a probabilidade de retirar uma bola azul, considerando todas essas possibilidades
(mutuamente exclusivas) =I

: é, pelo princípio aditivo:
;

P(A3) = P(A1 n A2 n >13) + PQ41 n 72 n >13) + P(71 n >12 n >13) + P(7l n 72 n >13)

; PQ43) = 0,072 + 0,032 + 0,09 + 0,06 = 0,254
;

; Gabarito: C

6666666669999933333333338881111111111

Independência de Eventos

Eventos independentes são aqueles que não influenciam uns nos outros. Por exemplo, o resultado do lançamento de um dado em nada influencia o resultado de outro lançamento.
Como fica a probabilidade condicional desses eventos, então?

Vamos supor que o resultado de um lançamento de um dado tenha sido o número 3: A =
{3}. Sabendo disso, qual é a probabilidade de um novo lançamento do dado ser B = {4}?
Bem, o resultado do 1Q lançamento (evento A) em nada influencia o 2g lançamento (evento B).Portanto, a probabilidade de o 25 lançamento ser 4 é a mesma (P = 1/6),
independentemente do resultado do 1Q lançamento.
Isso quer dizer que, sendo A e B eventos independentes, a probabilidade condicional de
B, sabendo que o evento A ocorreu, é igual à probabilidade de B (e vice-versa):
P(B|>1) = P(B)

Vamos a mais uma pergunta: sabendo que o resultado do 1Q lançamento foi A
= {3}, qual é a probabilidade de não sair 4 no 2Q lançamento (evento B)?
Sabendo que a probabilidade de sair 4 no 25 lançamento é a mesma, independente do resultado do15 lançamento, então a probabilidade de não sair 4 também é independente do 15 lançamento.

De forma geral, se A e B são independentes, então os complementares também são independentes. Isso implica nas seguintes igualdades:
i. P(B|4) = P(B)

Por exemplo, a probabilidade de sair 4 no 25 lançamento (evento B), dado que o resultado do 15lançamento não foi 3 (evento Ã), é a mesma (P = 1/6), independentemente do resultado do 1Qlançamento.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ii. = P(B)

Por exemplo, a probabilidade de não sair 4 no 2? lançamento (evento B), dado que o resultado do l9lançamento foi 3 (evento A), é a mesma (P = 5/6), independentemente do resultado do l9lançamento.

iii. P(B|À) = P(5)

Por exemplo, a probabilidade de não sair 4 no 29 lançamento (evento B), dado que o resultado do l9lançamento não foi 3 (evento Ã), é a mesma (P = 5/6), independentemente do resultado do l9lançamento.

E como fica o teorema da multiplicação para eventos independentes?

Bem, para eventos quaisquer, temos:

P(A ClB) = P(B\Á).P(Á)

Considerando que, para eventos independentes, temos P(B|X) = P(B), então a interseção de eventos independentes é calculada como:
P(A n B) = P(P) x P(Á)

Por exemplo, a probabilidade de obter 3 no l9 lançamento (evento A), com probabilidade P(A) = 1/6 E de obter 4 no 29 lançamento (evento B), com probabilidade P(B) = 1/6, é:
P(A n B) = P(B) x P(A) = = ±

6 6 36

Essa relação entre a interseção de eventos independentes e o produto das probabilidades é uma propriedade de "ida e volta".
Em outras palavras, se soubermos que A e B são independentes, podemos concluir que
P(A nB) = P(A) x P(By, e, se soubermos que P(A nB) = P(7l) x P(B),
podemos concluir que A e B são independentes.
Por exemplo, mesmo sem conhecer os eventos, se soubermos que P(Á) = -,P(B} = - e P(A n B) = —,

6 6 36

podemos concluir que A e B são independentes.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (CESPE/2015 - Telebras) Nas chamadas de suporte de uma empresa de telecomunicações,
o funcionário i

; Pedro resolve o problema do cliente em duas de cada três vezes em que é solicitado, enquanto Marcos i
= resolve em três de cada quatro chamadas.

I

A partir dessa situação hipotética, julgue o item seguinte, considerando que os funcionários sejam ;
= suficientemente experientes para que a tentativa de resolução do problema de qualquer chamada não esteja ;
= subordinada a tentativas anteriores.
j

I

i Se Pedro não resolver o problema de um cliente, considerando-se que nenhuma informação a respeito da i tentativa é repassada a Marcos, a probabilidade de que este também não resolva o referido problema será j
= inferior a 20%.

i i Comentários:
I

I

A questão pede a probabilidade de Marcos não resolver o problema, dado que Pedro não o resolveu

= (probabilidade condicional), que podemos representar por P(/?m|7?p).
;

I

I

: O item esclarece que nenhuma informação a respeito da tentativa é repassada a Marcos, indicando que são i i eventos independentes. Para esses eventos, a probabilidade condicional é igual à probabilidade não
= condicional:

i j =PTO

; O enunciado informa que Marcos resolve o problema em 3 de 4 ligações, logo a probabilidade de Marcos ;
= resolver é 3/4 e a probabilidade de Marcos não resolver é o complementar:

I

I

i PG^) = l-| = i=25%
i

= Que é superior a 20%.
j

I

i Gabarito: Errado.

I

I

I

I

i (CESPE/2019 - TJ/AM) Em um espaço de probabilidades, as probabilidades de ocorrerem os eventos i
= independentesA e B são,respectiva mente, P(A) = 0,3 e P(B) = 0,5.
i i Nesse caso, P(AAB) =0,15.;

i Comentários:

I

í Sendo A e B eventos independentes, a probabilidade da interseção é o produto das probabilidades:

PQánB) = P(A) xP(B)

= Sendo P(A) = 0,3 e P(B) = 0,5, então:
=

P(A n B) = 0,3 x 0,5 = 0,15

= Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FGV/2019 - Prefeitura de Angra dos Reis/RJ) Peter é um ótimo lançador de dardos. A
cada lançamento, a probabilidade de Peter acertar o alvo é de 90% e independe de Peter ter acertado ou não o alvo em lançamentos anteriores. Após fazer dois lançamentos em sequência, a probabilidade dePeter ter acertado o alvo nos dois lançamentos é de a) 180%
b) 90%

c) 81%

d) 72%

e) 160%

Comentários:

O enunciado informa que os lançamentos são eventos independentes. Portanto, a probabilidade de acertar os dois lançamentos, que corresponde à interseção dos eventos (Ai E A₂) é o produto das probabilidades:
P(7l1n^2)=P(241)xP(712)

A probabilidade de acerto é 90%, ou seja, PÇA^) = P(7l₂) = 90%. Logo, a probabilidade da interseção é:
P(A± n Â2) = 90% x 90% = 81%

Gabarito: C

(FGV/2018 - ALE/RO) A urna A tem dois cartões vermelhos e três amarelos e, a urna B, três cartões vermelhos e dois amarelos. Retira-se, aleatoriamente, um cartão de cada urna. Aprobabilidade de os dois cartões retirados serem amarelos é
Comentários:

A probabilidade de retirar 2 cartões amarelos, isto é, retirar um cartão amarelo da urna A E um cartão amarelo da urna B, corresponde à interseção desses eventos. Considerando que esses eventos (que podemos chamar por A e B) são independentes, então a interseção é dada pelo produto das probabilidades:
P(Aí)B) = P(A) x P(B)

Considerando que há 3 cartões amarelos, de um total de 5 cartões, na urna A, a probabilidade de retirar um cartão de A é: P(Á) = -
Considerando que há 2 cartões amarelos, de um total de 5 cartões, na urna B, a probabilidade de retirar um cartão de A é: P(B) = |
Assim, a probabilidade de retirar 2 cartões amarelos é:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Gabarito: A.

P(A n B)

3 2 _ 6

5 X5 "25

(FGV/2019 - DPE/RJ - Adaptada) A partir dos axiomas da Teoria das Probabilidades,
algumas proposições podem ser estabelecidas. Para quaisquer eventos não vazios, julgue as seguintes proposições.
I) P(A U B) < PQ4) + P(B) - PQ4). P(B)

II) Se P(A n B) = PQ4). P(B) -» P(Ã n B) = PQ4). P(B)

Comentários:

Em relação ao item I, a probabilidade da união é dada por:

P(A U B) = P(Á) + P(B) - P(A n B)

Se A e B fossem independentes, teríamos P(A n B) = PQ4) x P(£P). Porém, essa não é uma condição dada pelo enunciado. Logo, é possível que os eventos sejam dependentes e, consequentemente, termos:
P(Aí)B) ¥= P(A) x P(B)

Pontue-se que não é possível afirmar qual das duas probabilidades P(A n B) ou PQ4) x P(B) é maior.

Sabendo que a probabilidade da interseção pode ser diferente do produto das probabilidades, então a probabilidade da união pode ser diferente de:
P(A UB) * P(A) + P(B) - P(A) x P(B)

Logo, o item I está errado.

Em relação ao item II, o item informa que:

P(Aí)B) = P(Á) x P(B)

Isso nos permite concluir que A e B são eventos independentes.
Consequentemente, os eventos complementares também são independentes. Logo, a interseção dos eventos complementares é o produto:
P(ÂíTB) = P(Â) x P(B)

Assim, o item II está correto.

Resposta: item I errado; item II certo.

FIQUE

ATENTO!

Algumas questões pedem a probabilidade da forma "pelo menos um", ou da união de diversos eventos, em que será mais simples calcular a probabilidade complementar.
Vejamos algumas questões desse estilo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

(CESPE/2015 - DEPEN) Considerando que, entre a população carcerária de um presídio, a probabilidade de um detento contrair tuberculose seja igual a 0,01; que dois detentos sejam selecionados aleatoriamente dessa população carcerária; e que as ocorrências de tuberculose entre esses detentos sejam eventos independentes, julgue o próximo item.
A probabilidade de pelo menos um detento na amostra contrair tuberculose será superior a 0,01 e inferior a0,03.

Comentários:

A probabilidade de pelo menos um detento, dentre os 2 detentos da amostra, contrair tuberculose pode ser calculada como o complementar da probabilidade de nenhum dos 2 detentos contrair a doença.
A probabilidade de um detento qualquer não contrair a doença é o complementar da probabilidade de ele contraí-la:
P(Õ) = 1 - P(D) = 1 - 0,01 = 0,99

A probabilidade de nenhum dos 2 detentos contrair a doença é a interseção da probabilidade de cada um não a contrair. Como os eventos são independentes, basta multiplicar as probabilidades:
Pnenhum = PÍP) X P(D) = 0,99 X 0,99 = 0,98

Assim, a probabilidade de pelo menos um dos 2 detentos contrair a doença é o complementar:

Ppelo menos 1 1 ^nenhum — 1 0,98 0,02
Esse resultado é, de fato, superior a 0,01 e inferior a 0,03.

Gabarito: Certo

(FGV/2021 - FEMPAR) Suponha que cada dose de certa vacina, ao ser aplicada em uma população específica,garanta a imunização contra uma doença, de metade daqueles que não estão imunizados.
Inicialmente, toda essa população estava não imunizada e todos os seus indivíduos foram submetidos a duas doses consecutivas dessa vacina. Sorteando-se, ao acaso, um indivíduo dessa população, a probabilidade de que esteja imunizado contra a doença é de a) 100%
b) 87,5%

c) 75%

d) 50%

e) 25%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Segundo o enunciado, quando uma dose de vacina é aplicada em uma população não imunizada, metade ficará imunizada. Em outras palavras, há uma probabilidade de 50% de uma pessoa não imunizada se tornar imunizada com uma dose de vacina. E a questão afirma que foram aplicadas 2 doses em uma população inicialmente não imunizada.
Vamos calcular a probabilidade de uma pessoa estar imunizada pelo seu complemento, qual seja de não estar imunizada:
P(imunizado) = 1 — P(não imunizado')

Para isso, é necessário que ela não tenha sido imunizada na primeira dose, com probabilidade de 50%, E não ter sido imunizada na segunda dose, também com probabilidade de 50%. Assim, temos a interseção de eventos independentes, cuja probabilidade é dada pelo produto:
P(não imunizado) = 0,5 x 0,5 = 0,25

E a probabilidade complementará:

Gabarito: C

P(imunizado) = 1 — 0,25 = 0,75 = 75%

Independência de Três Eventos

Quando há três eventos independentes, a situação é um pouco diferente de quando há apenas dois eventos.Se os eventos A, B e C são independentes, então temos todas as situações a seguir:

P(A nB) = P(A).P(B)

P(A C\ C) = P(A).P(C)

P(B n C) = P(B).P(C)

P(A n B n C) = P(A). P(B).P(C)

Dessa forma, os três eventos são considerados independentes somente se todos forem independentes entre si, tanto quando comparados dois a dois, quanto para todos os 3.
Ou seja, se os eventos são independentes, então podemos concluir que:

P(A n B n C) = P(A). P(B).P(C)

Por exemplo, lançando-se 3 moedas equilibradas, e sendo os eventos A = {CARA na 1-
moeda}, B =

{COROA na 2^ moeda} e C = {CARA na 3? moeda}, então a probabilidade P(A n B n C) é dada por:

P(A n B n C) = P(A) x P(B) x P(C) = |x|x| = i

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Porém, o contrário não é verdadeiro, ou seja, não podemos concluir que os eventos são independentes a partir desta identidade somente.
Por exemplo, sem conhecer os eventos A, B e C, mas sabendo que:

PW=l' PCC)=|' PUnBnC)=j não podemos, com base apenas nessas informações, concluir que A, B e C são independentes.
Além disso, é possível que todos os eventos sejam independentes 2 a 2, porém os 3
eventos não serem independentes. Ou seja, sabendo que A e B são independentes, B e C são independentes,A e C são independentes, ainda assim, não podemos concluir que os 3 eventos são independentes.
Também é possível que A e B sejam independentes e que B e C sejam independentes.
Com base nessas informações, não podemos concluir que A e C são independentes.
Por exemplo, suponha que o l9e29 lançamentos serão de moedas equilibradas. Suponha que, se o resultado do l9 lançamento for CARA, o 39 lançamento será de uma moeda desequilibrada; caso contrário, o 39 lançamento será de uma moeda equilibrada.
Suponha os mesmos eventos A = {CARA na 1-}, B = {COROA na 29} e C = {CARA na 39}.

Nesse exemplo, os eventos A e B são independentes (2 lançamentos separados) e os eventos B e Csão independentes, pois o resultado do 29 lançamento em nada influencia no resultado do 39lançamento. Porém, os eventos A e C não são independentes, pois o resultado do l9
lançamento afeta o resultado do 39 lançamento.
Generalizando, para n eventos independentes, vale a relação:

P(4i n 42 n ... n 4n) = P(AJ x p(42) x ... x PQ4„)

Porém, o contrário não é verdadeiro, ou seja, não podemos concluir que os eventos são independentes, a partir dessa igualdade.
I«** IX

..
.....................................* i i (VUNESP/2019 - Prefeitura de Cerquilho/SP) Em uma prova de múltipla escolha de língua chinesa, cada í
= uma das 5 questões tem 4 alternativas. A probabilidade de uma pessoa acertar todas as questões, sem =
= conhecer a língua, e escolhendo, aleatoriamente, uma alternativa em cada questão, é
=

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

A probabilidade de acertar todas as questões, escolhendo aleatoriamente as respostas, corresponde à interseção de acertar cada uma das questões.
Sabendo que há 4 alternativas, a probabilidade de acertar uma questão é:

PW = i

Assim, a probabilidade de acertar as 5 questões, considerando que são eventos independentes, é o produto:
P^i ná2 ná3 ná4nÂ5) = PQ4) x P(A) x P(A) x PQ4) x P(X) = Jx Jx
=

Gabarito: A.

(VUNESP/2018 - UNICAMP/SP) Dentre os bebedores de cerveja, sabe-se que 1/3 preferem a marca A. Se três deles são escolhidos ao acaso, a probabilidade de que nenhum deles preferem a marca A é
Comentários:

Sabendo que - dos bebedores preferem a marca A, então a probabilidade de escolher um bebedor que não prefira é complementar:
Considerando que a escolha de um bebedor independe da escolha de outro, então,
escolhendo 3 bebedores ao acaso, a probabilidade de que nenhum dos 3 bebedores prefira a marca A corresponde à interseção dos eventos (produto das probabilidades):
2 2 2 8

PxPxP=-x-x-=—

3 3 3 27

Gabarito: C.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FGV/2017 - TJ/AL) Os eventos A, B e C de um espaço amostrai são tais que A é independente de B, e B é independente de C. Sabe-se ainda que os três têm probabilidade não nula de ocorrência.
Com tais informações, é correto afirmar que:

a) A é independente de C;

b) A, B e C são mutuamente independentes;

c) A e C são mutuamente exclusivos;

d) B é independente do complementar de C;

e) P(i4).P(B).P(C) = P(A n B\C).

Comentários:

Sabendo que A é independente de B e que B é independente de C, não podemos afirmar nada a respeito da dependência entre A e C, muito menos a respeito da dependência dos 3 eventos. Por esses motivos, as alternativas A e B estão incorretas.
Por outro lado, podemos afirmar que os complementares dos eventos apresentam a mesma relação de independência dos respectivos eventos. Logo, a afirmativa D está correta.
Em relação à alternativa C, se 2 eventos são mutuamente exclusivos, a sua interseção é nula. Como o enunciado não menciona a respeito da interseção, não podemos saber se os eventos são mutuamente exclusivos, ou não. Logo, a alternativa C está incorreta.
Em relação à alternativa E, pela definição de probabilidade condicional, temos:

z x P(ÂnBnC)
P(AnB|C)= —

Como não sabemos se A, B e C são independentes e considerando que o enunciado não forneceu elementos que nos permitem calcular P(A C\ B ílC), não podemos calcular PQ4 nB|C).Logo, a alternativa E está incorreta.
Gabarito: D

Teorema da Probabilidade Total

O Teorema da Probabilidade Total permite calcular a probabilidade de um evento B,
quando conhecemos as probabilidades condicionais desse evento.
Por exemplo, suponha que, em um banco, o nível de inadimplência dos pagadores do grupo A (melhores pagadores) seja 1%; o nível de inadimplência dos pagadores do grupo B seja 5%; e o nível de inadimplência dos pagadores do grupo C seja de 10%.
Além disso, suponha que o grupo A represente 50% dos pagadores; o grupo B represente
30%; e o grupo C
represente 20%. Com base nesses valores, podemos calcular a probabilidade total de inadimplência, ou seja,a probabilidade de inadimplência de um cliente qualquer, sem saber a que grupo ele pertence.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para isso, consideramos que a probabilidade do evento I (inadimplência) está "espalhada"
nos três grupos,
ou seja, temos os inadimplentes do grupo A, os inadimplentes do grupo B e os inadimplentes do grupo C,como representado a seguir.

A B

I

C

_ J

Portanto, a probabilidade total de inadimplência é a soma dos inadimplentes de cada grupo, ou seja, a soma das interseções de I com os grupos A, B e C:
P(Z) = P(I n 71) + P(Z n B) + P(I n C)

Pelo Teorema da Multiplicação, substituímos as interseções pelos produtos das probabilidades:

P(Z) = P(Z|t4) x P(Á) + P(Z|B) x P(Z3) + P(Z|C) x P(C)

Nesse exemplo, temos P(A) = 0,5, P(B) = 0,3, P(C) = 0,2, P(l | A) = 0,01, P(l | B) = 0,05 e P(11C)
= 0,1. Logo, a probabilidade de um cliente qualquer ser inadimplente é:
P(Z) = 0,5 x 0,01 + 0,3 x 0,05 + 0,2 x 0,1

P(Z) = 0,005 + 0,015 + 0,02 = 0,04 = 4%

Essa relação vale para qualquer número de eventos. Havendo apenas 2 eventos a priori,
como se fossem apenas 2 classificações de clientes, A e Ã, a probabilidade total P(Z) é dada por:
P(Z) = P(Z|21) x P(4) + P(Z|21) x P(4)

Generalizando, com n eventos At e conhecendo P(I\Ai), temos P(Z) dado por:

P(Z) = PCZI^i) x P(^i) + P(Z|712). PQ42) + - + P(Z|21n). P(4n)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (CESPE/2015 - Departamento Penitenciário Nacional - Área 4) As probabilidades dos eventos aleatórios A
; = "o infrator é submetido a uma pena alternativa" e B = "o infrator reincide na delinquência" são i
= representadas, respectivamente, por P(A) e P(B). Os eventos complementares de A e B são denominados, ;i respectivamente, por Ã e B. Considerando que P(A) = 0,4, e que as probabilidades condicionais
P(B\Ã) = i

= 0,3 e P(B|i4) = 0,1, julgue o item a seguir.

í P(B) < 0,2.

I

I

i Comentários:

A questão trata da probabilidade total de B, dada por:

P(B) = x P(Á) + P(B|Â) x P(Â)

= O enunciado informa que PQ4) = 0,4; P(B|Â) = 0,1 e P(B|Â) = 0,3.

I

Ademais, sabendo que P(Á) = 0,4, o seu complementar é:
i

PQ4) = 1 - PQ4) = 1 - 0,4 = 0,6

I

; Substituindo esses valores, temos:
i

P(B) = 0,1 x 0,4 + 0,3 x 0,6 = 0,04 + 0,18 = 0,22

= Esse resultado é maior que 0,2: P(B) > 0,2.
;

j Gabarito: Errado.

I

: (FGV/2019 - DPE/RJ) 10% das lâmpadas fabricadas pela empresa A queimam antes de 1000h de ;

I

: funcionamento. Das fabricadas pelaempresa B, 5% queima antes de 1000h de funcionamento.
Das i

; fabricadas pela empresa C, 1% queima antes de 1000h de funcionamento. Em uma grande loja de varejo, i
= 20% das lâmpadas em estoque são da marca A, 30% são da marca B e 50% são da marca C. Uma lâmpada é i
= escolhida ao acasodo estoquedessa loja.
i

I

I

A probabilidade de que ela não queime antes de 1000h de funcionamento é igual a.
i i a) 0,76
b) 0,84
í c) 0,92

d) 0,96

j e) 0,98

i Comentários:

A questão trabalha com o Teorema da Probabilidade Total, pois informa as probabilidades de durabilidade, i
= condicionadas aos fabricantes, e pede a probabilidade de durabilidade, não condicionada.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= A probabilidade de a lâmpada não queimar antes de 1000h é complementar à probabilidade de ela queimar
= antes de 1000h:

E

; O enunciado informa que:
I

P(Q) = 1-P(Q)

i * 10% das lâmpadas fabricadas por A queimam antes de 1000h: P(Q| A) = 0,1;

j * 5% das lâmpadas fabricadas por B queimam antes de 1000h: P(Q| B) = 0,05;
I

i * 1%das lâmpadas fabricadas por C queimam antes de lOOOh: P(Q| C) = 0,01;
i * 20% das lâmpadas são fabricadas por A: P(A) = 0,2;

i * 30% das lâmpadas são fabricadas por B: P(B) = 0,3;
i * 50% das lâmpadas são fabricadas por C: P(C) = 0,5.

= Pelo Teorema da Probabilidade Total, temos:

P(Q) = P(Q|21) x PQ4) + P(Q|B) x P(B) + P(Ç|C) x P(C)

= Substituindo os valores fornecidos, temos:

P(Ç) = 0,1 x 0,2 + 0,05 x 0,3 + 0,01 x 0,5 = 0,02 + 0,015 + 0,005 = 0,04

= Portanto, a probabilidade de a lâmpada não queimar é complementar:

P(Ç) = l-P(Q) = 1-0,04 = 0,96

; Gabarito: D

i (FCC/2016 - Analista Judiciário do TRT 11^ Região) Um determinado órgão público recebe mensalmente
= processos que devem ser analisados por 2 analistas: A e B. Sabe-se que esses dois analistas recebem a mesma i proporção de processos para a análise. Sabe-se que 20% de todos os processos encaminhados para A são
= analisados no mês de recebimento e que 10% são indeferidos. Sabe-se também que 40%
dos processos

= encaminhados para B são analisados no mês de recebimento e que 20% são indeferidos.

I

i Um processo recebido em determinado mês é selecionado ao acaso. A probabilidade de ele ser deferido
: naquele mesmo mês é igual a a) 0,245
b) 0,350

; c) 0,500

d) 0,420

í e) 0,250

i Comentários:

I

: Pela probabilidade total, a probabilidade de um processo ser deferido no mesmo mês é:

P(D) = P(D\Á) xP(A) + P(D\B) xP(B)

= Sabemos que P(A) = P(B). Como P(A) + P(B) = 1, então P(A) = P(B) = 0,5.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Além disso, sabemos que a probabilidade de o processo ser deferido no mesmo mês é o complementar de ele ser indeferido no mesmo mês.
O enunciado informa que:

* 20% dos processos de A são analisados no mês e 10% deles são indeferidos. Ou seja, 90% dos processos analisados no mês por A são deferidos:
P(D\A~) = 0,2 x 0,9 = 0,18

* 40% dos processos de B são analisados no mês e 20% deles são indeferidos. Ou seja, 80% dos processos analisados no mês por B são deferidos:
P(D\B) = 0,4 x 0,8 = 0,32

Inserindo esses valores no Teorema da Probabilidade Total, temos:

P(£>) = 0,18 x 0,5 + 0,32 x 0,5 = 0,09 + 0,16 = 0,25

Gabarito: E

Teorema de Bayes

O Teorema de Bayes é usado quando conhecemos as probabilidades condicionais da forma
P(B | A), e queremos calcular a probabilidade condicional da forma P(A| B), isto é, invertendo-se os eventos a priori e a posteriori.
No exemplo da inadimplência que vimos antes, conhecemos as probabilidades de inadimplência para cada grupo, isto é, com a inadimplência sendo o evento a posteriori e os grupos A, B e C sendo os eventos a priori:
* P(l|A) = 0,01

* P(l|B) = 0,05

* P(l|C) = 0,l.

Mas, podemos calcular a probabilidade de um cliente pertencer a um dos grupos (por exemplo ao grupo A),
sabendo que ele foi inadimplente, ou seja, tendo a inadimplência como evento a priori:

* P(A|I) = ?

Para isso, vamos utilizar a fórmula da probabilidade condicional:

P(A n /)

P(A\P) =

Pelo Teorema da Multiplicação, podemos escrever o numerador em função da probabilidade condicionalP(l | A), que conhecemos, isto é, com o evento inadimplência a posteriori:

P(A nl) = x P(A)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Pelo Teorema da Probabilidade Total, podemos escrever o denominador como:

P(Z) = P(J|Â) x P(Á) + P(Z|B) x P(B) + P(Z|C) x P(C)

Assim, a fórmula do Teorema de Bayes para é:

P(4|/) =

P(/|í4)xP(í4)

P(/|4)xP(i4)+P(/|B)xP(B)+P(/|C)xP(C)

Para o nosso exemplo, já calculamos o denominador, que corresponde à probabilidade de um cliente ser inadimplente, pela probabilidade total:
P(Z) = P(X).P(/|?1) + P(S).P(7|fí) + P(C).P(7|C) = 0,04

Também sabemos que P(l | A) = 0,01 e P(A) = 0,5, portanto, a probabilidade de um cliente inadimplente ser do grupo A é:
P(A\D =

0,01 x 0,5
ÕÕ4

0,005

0,04

- = 0,125 = 12,5%
O

De maneira geral, com n eventos At e conhecendo as probabilidades P(B\Ai),
então a probabilidade de algum evento Am, condicionada ao evento B é:
PWAJ.PÇAJ + P(B|42).P(42) + - + PWAJ.PIM

HORA»

: (FGV/2019 - DPE/RJ) A abrangência do atendimento da Defensoria Pública depende da condição econômica i
I do cidadão e também do tipo de causa envolvida. Sabe-se que 80% das demandas surgem em função da i I
; hipossuficiência econômica, e os outros 20% devem-se a causas no âmbito criminal. Entre aqueles que não i dispõem de recursos, 90% têm suas necessidades atendidas, enquanto entre os envolvidos em ações i
= criminais, só 40% são beneficiados com a gratuidade.
i

= Suponha que um indivíduo do cadastro dos que procuram a Defensoria seja sorteado ao acaso, verificando- j
= se tratar-se de alguém atendido gratuitamente.
i

I

I

: Então, a probabilidade de que o sorteado seja um dos que procuraram a Defensoria por causa de questões i
= criminais é igual a:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

A questão trabalha com o Teorema de Bayes, pois informa as probabilidades de gratuidade condicionadas aos tipos de situação e pergunta pela probabilidade do tipo de situação, condicionada à gratuidade, isto é,inverte os eventos a priori e a posteriori.

O enunciado informa que:

* 80% das demandas surgem por hipossuficiência econômica: P(H) = 0,8;

* Os outros 20% das demandas surgem por causas criminais: P(C) = 0,2;

* 90% das demandas de hipossuficiência econômica conseguem gratuidade: P(G | H) = 0,9

* 40% das demandas por causas criminais conseguem gratuidade: P(G | C) = 0,4

Assim, a probabilidade de a demanda ser por causas criminais, sabendo que conseguiu gratuidade, P(C|G),é dada pela fórmula de Bayes:

P(C|G) =

P(G|C)xP(C)

P(G|C) x P(C) + P(G|H) x P(W)

Substituindo os valores do enunciado, temos:

0,4 x 0,2

0,08

0,08 _ 1

Gabarito: A

P(C|G) =

0,4 x 0,2 + 0,9 x 0,8

0,08 + 0,72

Õ8Õ_ 1Õ

(FCC/2018 - Analista Judiciário do TRT 14? Região) Uma cidade sede do interior possui três varas trabalhistas. A 1§ Vara comporta 50% das ações trabalhistas, a 25 Vara comporta 30% e a 35 Vara as 20%restantes. As porcentagens de ações trabalhistas oriundas da atividade agropecuária são
3%, 4% e 5% para a 15, 2^ e 35 Varas, respectivamente. Escolhe-se uma ação trabalhista aleatoriamente e constata-se ser originária da atividade agropecuária. A probabilidade dessa ação ser da1? Vara trabalhista é,
aproximadamente:

a) 0,5312.

b) 0,3332.

c) 0,1241.

d) 0,4909.

e) 0,4054.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado fornece as proporções das ações de atividade agropecuária para cada uma das varas (ou seja,tendo as ações de atividade agropecuária como probabilidade a posteriori) e exige a probabilidade uma ação de ser da 1? Vara, sabendo que ela trata atividade agropecuária (ou seja, tendo as ações de atividade agropecuária como evento a priori).
Pelo Teorema de Bayes, P(Vi| A) é dado por:

PGTOxPÇVi)

PCViM) =

PGW x PCVJ + P(4|7 ) x P(V ) + P(A|Vs) x P(V )

A questão informa que:

2 2 3

I

: * A Vara comporta 50% das ações: P(Vi) =0,5;

: * A 2ã Vara comporta 30% das ações: P(V₂) =0,3;
i * A 3? Vara comporta 20% das ações: P(73) =0,2;

I

j * As percentagens das ações de atividade agropecuária para as Varas 1, 2 e 3 são,
respectivamente, 3%,

; 4% e 5%: P^lVi) = 0,03, PQ4|V₂~) = 0,04 e PQ4|V₃) = 0,05.

: Substituindo esses valores na fórmula do Teorema de Bayes, temos:

i z x 0,03 x 0,5
0,015 0,015

í v 11 7 0,03 x 0,5 + 0,04 x 0,3 + 0,05 x 0,2 0,015 +
0,012 + 0,01 0,037

I

i Gabarito: E.

I

: (CESPE/2019 -TJ/AM) Se Carlos estiver presente na aula ministrada pela professora Paula, a probabilidade de ele aprender o conteúdo abordado é de 80%; se ele estiver ausente, essa probabilidade cai para0%. Em

= 25% das aulas da professora Paula, Carlos está ausente.

= Com relação a essa situação hipotética, julgue o item seguinte.

= Se Carlos não aprendeu o conteúdo ministrado na aula da professora Paula, então a probabilidade de ele ter j estado presente na aula é inferior a 50%.
I

i Comentários:

= O enunciado informa que:

I

i * Se Carlos estiver presente na aula, a probabilidade de aprender o conteúdo é de
80%: P(Ap\P) = 0,8,

= em que Ap corresponde ao aprendizado e P corresponde à presença;

I

i * Se Carlos estiver ausente, a probabilidade de aprender é 0%: PQ4p|P) = 0, em que P corresponde à não presença, isto é, à ausência;
j * Carlos está ausente em 25%: P(P) = 0,25.

= Para calcular a probabilidade de Carlos ter estado presente, sabendo que ele não aprendeu o conteúdo, isto i é, PÇP\Ap), em que Ap corresponde ao não aprendizado, utilizamos a fórmula de Bayes:
p(PMp) =

P(Âp|P) X P(P)

P(Ãp\P) X P(P) + P(Ap\P) X P(P)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= Sabemos que a probabilidade de Carlos aprender, dado que esteve presente, é P(Av\P)
= 0,8. Assim, a =I

; probabilidade de Carlos não aprender, dado que esteve presente, corresponde à probabilidade do evento ;i complementar:

P(Ãp\P) = 1 - PQ4p|P) = 1 - 0,8 = 0,2

i Sabemos ainda que a probabilidade de Carlos não estar presente é P(P) = 0,25.
Logo, a probabilidade de i

= Carlos estar presente corresponde à probabilidade do evento complementar:

P(P) = 1 - P(P) = 1 - 0,25 = 0,75

= Por fim, sabemos que a probabilidade de Carlos aprender, dado que não esteve presente, é P(Ap\P) = 0. i
= Logo, a probabilidade de Carlos não aprender, dado que não esteve presente, é complementar:

PG4p|P) = 1 - P(Ap\P) = 1-0 = 1

= Substituindo esses valores na fórmula de Bayes, temos:
i í z x 0,2 x 0,750,15 0,15
i

P(P|7lp) - Q 2 x Q ?5 + x x Q 25 - Q 15 + 0 25 - — - 37,5%
;

I

: Ou seja, a probabilidade de Carlos estar presente, sabendo que ele não aprendeu é inferior a 50%

I

I

Ê Gabarito: Certo.

ESQUEMATIZANDO

Probabilidade Condicional

Probabilidade Condicional: P(B1^4) = P(^n5')

P(A)

Teorema da Multiplicação: P(A nB) = P(B\A) x P(A)

Teorema da Probabilidade Total: P(/) = PÇl\Ay) x PÇA) + P(7|fí) x P(B)

Teorema de Bayes: PQ4|7)

P(JftA) P(I\A)XP(A)

P(T) ~ P(/|A)XP(J4)+P(/|B)XP(B)

Independência

A e B independentes «-» P(A nB) = P(71) x P(B)

A, B e C independentes -> P(A A B O C) = P(A) x PÇB) x P(C)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Resumo da Aula

Definição clássica de probabilidade

PQ4) =

número de casos favoráveis número de casos totais n(A)
n(lT)

Probabilidade da União - caso geral

P(A uB) = P(A) + P(B) - P(A n B)

Probabilidade da União - eventos mutuamente excludentes: P(A n B) = 0

P(AuB) = P(A) + P(B)

Teorema do Evento Complementar

Vale também para combinação de eventos (união e interseção) e para probabilidades condicionais

PQ4) = 1 - P(4)

Axiomas/Propriedades de Probabilidade

P(B) = 1

0 < P(X) < 1

Probabilidade Condicional - quando sabemos que o evento A ocorreu

P(B|4) =

P(A n B)

P(4)

P(A nB) = P(B|4) x PQ4)

Eventos Independentes - o resultado de um não influencia o resultado do outro

P(B|X) = P(B)

P(Aí}B) = P(B) x P(Á)

Teorema da Probabilidade Total: probabilidade do todo, a partir das probabilidades condicionais

P(Z) = P(Z|^4) x P(A) + P(Z|B) x P(B) + P(Z|C) x P(C)

Teorema de Bayes: quando a questão inverte os eventos a priori e a posteriori pçA\n =
P(I\A) x P(A)

P(I\A) x P(A) + P(7|B) x P(B) + P(7|C) x P(C)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Definições de Probabilidade

Item. 1. (Cebraspe/2022 - DPE/RO) Um lote contendo 100 componentes foi testado por
Item. 1.000 horas. Nesse período, 4 componentes falharam. A partir das informações anteriores, assinale a opção que corresponde à taxa de falha do teste em questão.
a) 20%

b) 8%

c) 4%

d) 16%

e) 10%

Comentários:

Essa questão pede a probabilidade de falha. A probabilidade clássica é a razão entre o número de casos favoráveis e o número total de casos possíveis. Considerando que 4componentes falharam (casos favoráveis), dentre 100 componentes (total de casos), a probabilidade de falha é:
casos favoráveis n(F} 4

P = = —= = 0,04 = 4%

casos totais n(LF) 100

Gabarito: C.

Item. 2. (Cebraspe/2020 - ME) O setor de gestão de pessoas de determinada empresa realiza regularmente a análise de pedidos de férias e de licenças dos seus funcionários. Os pedidos são feitos em processos, em que o funcionário solicita apenas férias, apenas licença ou ambos (férias e licença).Em determinado dia,
30 processos foram analisados, nos quais constavam 15 pedidos de férias e 23 pedidos de licenças.
Com base nessa situação hipotética, julgue o item que se segue.
Se todos os processos foram analisados individualmente nesse dia, então a probabilidade de um processo específico ter sido o primeiro a ser analisado é superior a —.
Comentários:

A probabilidade é a razão entre o número de casos favoráveis e o número total de casos possíveis. Sabendo que existem 30 processos no total, a probabilidade de selecionar 1 processo específico é:
casos favoráveis 1

P = = ^ = 0,03

casos totais 30

Que é inferior a — = 0,10.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Gabarito: Errado

Item. 3. (Cebraspe/2021 - CBM/AL) Os professores João, Carlos e Luis ministrarão um curso de primeiros socorros em que serão ensinados os seguintes procedimentos.
I. fazer massagem cardíaca

II. desengasgar

III. estancar sangramentos

IV. amenizar queimaduras

V. desafogar

VI. cuidar de fraturas

Cada professor ensinará exatamente dois procedimentos, e o mesmo professor que ensinar o procedimento desafogar ensinará também o procedimento desengasgar. Considerando essa situação hipotética, julgue o próximo item.
Selecionando-se ao acaso o professor que ensinará o procedimento fazer massagem cardíaca, a probabilidade de Luis ser o escolhido é maior do que 40%.
Comentários:

O enunciado informa que há 3 professores para ministrar dois procedimentos cada. A
probabilidade de Luis ser escolhido para ministrar um procedimento específico é a razão entre o número de casos favoráveis (1professor: Luis) e o número total de casos (3 professores):

casos favoráveis n(A) 1

P =------------= - - 0,33 = 33%

casos totais n(U) 3

Que é menor do que 40%

Gabarito: Errado

Item. 4. (Cebraspe/2021 - CBM/AL) Os professores João, Carlos e Luis ministrarão um curso de primeiros socorros em que serão ensinados os seguintes procedimentos.
I. fazer massagem cardíaca

II. desengasgar

III. estancar sangramentos

IV. amenizar queimaduras

V. desafogar

VI. cuidar de fraturas

Cada professor ensinará exatamente dois procedimentos, e o mesmo professor que ensinar o procedimento desafogar ensinará também o procedimento desengasgar. Considerando essa situação hipotética, julgue o próximo item.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Se Carlos ensinar o procedimento cuidar de fraturas, então, selecionando-se ao acaso os professores que ensinarão os outros procedimentos, a chance de que João ensine o procedimento desafogar é maior do que45%.

Comentários:

O enunciado informa que cada um dos 3 professores irá ensinar 2 procedimentos, sendo que o professor que ensinar o procedimento desafogartambém irá ensinar desengasgar. Considerando queCarlos irá ensinar o procedimento cuidar de faturas, ele ensinará algum outro procedimento diferente de desafogar e desengasgar. Assim, o procedimento de desafogar será ensinado por João ouLuis (2 possibilidades). A
probabilidade de ser João é:

casos favoráveis n(A} 1

P =------------J-——.---------= = - = 0,5 = 50%

casos totais n(U) 2

Que é maior do que 45%

Gabarito: Certo

Item. 5. (Cebraspe/2021 - CBM/AL) Em determinado dia, em uma região atendida por uma unidade do corpo de bombeiros, ocorreram 16 acidentes, que resultaram em 48 vítimas, socorridas pelos bombeiros nos próprios locais de acidente. Entre essas vítimas, 4 vieram a óbito no momento do atendimento, e as demais sobreviveram. Com base nessa situação hipotética, julgue o item a seguir.
Considere que os nomes das 48 vítimas tenham sido anotados individualmente em rascunhos pelos bombeiros que as atenderam nos locais de acidente. Considere também que, ao final do dia, determinado bombeiro tenha sido responsável por registrar em relatório o nome de cada vítima,escolhendo cada nome aleatoriamente a partir desses rascunhos. Considere, por fim, que este bombeiro tenha registrado os nomes de metade das vítimas e que todas essas vítimas já registradas sejam sobreviventes. Nesse caso, a probabilidade de o vigésimo quinto registro deste bombeiro ser de uma vítima que veio a óbito é igual a -.
Comentários:

Esse item informa que 4 vítimas faleceram, dentre 48 no total, e que já foram selecionadas 24 vítimas que não faleceram, logo, restaram 24 vítimas para serem selecionadas, das quais 4faleceram. Assim, a probabilidade de a próxima vítima selecionada ter falecido, corresponde à razão entre as 4 vítimas que faleceram (casos favoráveis) e as 24 vítimas disponíveis para seleção (casos totais):
casos favoráveis nÇF') 4 1

casos totais nÇU') 24 6

Gabarito: Certo

Item. 6. (Cebraspe/2018 - PGE/PE) A União tem, hoje, 138 estatais sob sua gestão,
entre elas o Banco do
Brasil S.A., a PETROBRAS e a CAIXA. Dessas 138, somente três devem permanecer sob a gestão da União;
as demais serão privatizadas. Considerando essa afirmação, julgue o próximo item.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Supondo-se que a PETROBRAS e o Banco do Brasil S.A. sejam estatais já escolhidas para permanecerem sob a gestão da União, se a terceira estatal for escolhida ao acaso, a chance de aCAIXA ser privatizada será superior a 99%.
Comentários:

A probabilidade é, por definição:

casos favoráveis n(E')

casos totais n(U)

Considerando que há 138 estatais, e que o destino de 2 delas já foi decidido, então restam 136 estatais cujo destino será definido ao acaso. Logo, n(U) = 136.
Dessas 136 estatais, 1 será mantida sob gestão da União e, consequentemente, 135 serão privatizadas. Ou seja, n(E) = 135.
Assim, a probabilidade de uma estatal ser privatizada, nessas condições, é:

= 777 = 99,26%

Que é superior a 99%.

Gabarito: Certo.

Item. 7. (Cebraspe/2018 - PF) Em um aeroporto, 30 passageiros que desembarcaram de determinado voo e que estiveram nos países A, B ou C, nos quais ocorre uma epidemia infecciosa, foram selecionados para ser examinados. Constatou-se que exatamente 25 dos passageiros selecionados estiveram em A ou em B,nenhum desses 25 passageiros esteve em C e 6 desses 25 passageiros estiveram em A e em B.

Com referência a essa situação hipotética, julgue o item que se segue.

Se 2 dos 30 passageiros selecionados forem escolhidos ao acaso, então a probabilidade de esses 2passageiros terem estado em 2 desses países é inferior a 1/30.

Comentários:

Para calculara probabilidade,temos:

casos favoráveis n(E')

casos totais n(U)

O enunciado informa que nenhum dos passageiros que estiveram em A ou em B esteve em
C. Assim, somente visitaram 2 países aqueles que foram para A e para B, ou seja, 6 passageiros.
Portanto, os casos favoráveis correspondem às diferentes maneiras de escolher, sem importância de ordem,2 passageiros dentre os 6 que visitaram 2 países (combinação de 2, dentre 6):

z , 6! 6x5x4! 6x5

- C6,2 - (6 2)! X 2! 4! x 2! 2 15

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Os casos totais correspondem às diferentes maneiras de escolher 2 passageiros,
dentre o total de passageiros. Como há 30 passageiros, no total, então temos a combinação de 2, dentre 30 elementos:
n 30! 30 x 29 x 28!

n(t7) - C30,2 - (30 _ 2)j x 2! - —28! x 2!—

30 x 29

15 x 29

Assim, a probabilidade de selecionar 2 passageiros que estiveram em dois países é:

15 1

P " 15 x 29 " 29

Que é superior a 1/30.

Gabarito: Errado

Item. 8. (Cebraspe/2018 - PF) Os indivíduos Sl, S2, S3 e S4, suspeitos da prática de um ilícito penal, foram interrogados, isoladamente, nessa mesma ordem. No depoimento, com relação à responsabilização pela prática do ilícito, Sl disse que S2 mentiria; S2 disse que S3 mentiria; S3 disse que S4 mentiria.
A partir dessa situação, julgue o item a seguir.

Considerando que a conclusão ao final do interrogatório tenha sido a de que apenas dois deles mentiram,mas que não fora possível identificá-los, escolhendo-se ao acaso dois entre os quatro para novos depoimentos, a probabilidade de apenas um deles ter mentido no primeiro interrogatório é superior a0,5.

Comentários:

Para calculara probabilidade,temos:

casos favoráveis n(E')

casos totais n(U)

O total de casos corresponde a todas as maneiras de escolher e suspeitos, dentre 4,
sem importância de ordem (combinação de 2, dentre 4 elementos):
4! 4x3x2! 4x3

w(íl) - C4;2 - (4_2)! x 2! - 2! x 2! - 2 - 6

Os casos favoráveis correspondem às maneiras de escolher 1 mentiroso e 1 sincero,
de um total de 2
mentirosos e de 2 sinceros. Assim, há 2 possibilidades de escolher o mentiroso e 2 possibilidades de escolher o sincero. Pelo princípio multiplicativo, temos:
n(E) = 2x2 = 4

A probabilidade é então:

Que é superior a 0,5.

Gabarito: Certo.

4 2

P = : - = 0,666

: 6 "

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 9. (Cebraspe/2017 - PM-MA) Determinado laboratório de análises clínicas está sendo investigado por emitir laudos falsos de um exame constituído por 7 indicadores, correspondentes à concentração de 4compostos na corrente sanguínea, obtidos da seguinte forma: uma medição da concentração de cada um dos compostos A, B, C e D, e 3 medições, por 3 diferentes técnicas, da concentração do composto E.Os laudos verdadeiros de 7 pacientes (chamados pacientes-fonte), com prenomes distintos, entre elesAmanda, Bárbara, Carlos e Daniel, eram usados para compor laudos falsos para os demais pacientes.
Para dificultar a ação da autoridade policial, na montagem de um laudo falso, o laboratório tomava o cuidado de, no conjunto de 7 medições que constituíam cada laudo falsificado, usar apenas uma medição de cada paciente-fonte, ou seja, de nunca usar 2 ou mais medições de um mesmo paciente-fonte.
Com referência a essa situação hipotética, julgue o item seguinte.

Caso o laboratório escolhesse aleatoriamente, entre os dados dos 7
pacientes-fonte, aqueles que seriam usados nas medições referentes ao composto E, a probabilidade de serem usados os dados de Amanda,Bárbara e Carlos seria inferior a 3%.

Comentários:

Para calculara probabilidade, temos:

casos favoráveis n(E')

casos totais n(lT)

Os casos totais correspondem a todas as maneiras de escolher 3 pacientes-fonte, dentre
7, sem que a ordem importe, pois todos serão utilizados para as medições do composto E. Logo, temos a combinação de 3elementos, dentre 7:

n(L/) = C7i3

Os casos favoráveis correspondem às maneiras de escolher Amanda, Bárbara e Carlos como os 3 pacientes-fonte, em qualquer ordem. Ou seja, n(E) = 1.

Assim, a probabilidade dessa escolha é:

P = — = 2,86%

Que é inferior a 3%.

Gabarito: Certo.

Item. 10. (Cebraspe/2019 - Prefeitura de São Cristóvão/SE) A sorte de ganhar ou perder,
num jogo de azar,
não depende da habilidade do jogador, mas exclusivamente das probabilidades dos resultados. Um dos jogos mais populares no Brasil é a Mega Sena, que funciona da seguinte forma: de 60bolas, numeradas de 1 a 60, dentro de um globo, são sorteadas seis bolas. À medida que uma bola é retirada, ela não volta para dentro do globo. O jogador pode apostar de 6 a 15 números distintos por volante e receberá o prêmio
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

se acertar os seis números sorteados. Também são premiados os acertadores de 5 números ou de 4números.

A partir dessas informações, julgue o item que se segue.

A probabilidade de a primeira bola sorteada ser um número múltiplo de 8 é de 10%.

Comentários:

A probabilidade é, por definição:

casos favoráveis n(E')

casos totais n(U)

O total de casos corresponde ao número total de bolas, ou seja, n(U) = 60.

O número de casos favoráveis corresponde à quantidade de múltiplos de 8, entre 1 e 60:

T = 7'5

Assim, há 7 múltiplos de 8 entre 1 e 60: n(E) = 7. Assim, a probabilidade é:

P = ^- = 11,67%

Assim, a probabilidade não é de 10%.

Gabarito: Errado.

Item. 11. (Cebraspe/2019 - Prefeitura de São Cristóvão/SE) A sorte de ganhar ou perder,
num jogo de azar,
não depende da habilidade do jogador, mas exclusivamente das probabilidades dos resultados. Um dos jogos mais populares no Brasil é a Mega Sena, que funciona da seguinte forma: de 60bolas, numeradas de 1 a 60, dentro de um globo, são sorteadas seis bolas. À medida que uma bola é retirada, ela não volta para dentro do globo. O jogador pode apostar de 6 a 15 números distintos por volante e receberá o prêmio se acertar os seis números sorteados. Também são premiados os acertadores de 5 números ou de 4números. A partir dessas informações, julgue o item que se segue.

A probabilidade de se acertar os 6 números sorteados na Mega Sena com a aposta de um volante com 6números é igual a 541/601.

Comentários:

A probabilidade é, por definição:

casos favoráveis nfA')
casos totais n(U)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para acertar os 6 números com uma aposta de 6 números, há somente uma possibilidade. Logo, n(A) =
1.

O número de casos totais corresponde à quantidade de maneiras distintas de escolher 6
números, dentre
60, sem que a ordem importe. Assim, temos a combinação de 6 elementos, dentre 60:

60! 60!

C60'6 (60 - 6)! x 6! 54! x 6!

Logo, a probabilidade de acertar os 6 números é (lembre-se de que a divisão por uma fração equivale à multiplicação pelo inverso dessa fração):
1 d 54! x 6! 54! x 6!

P ~ 60! 1 X 60! " 60!

54! x 6!

Ou seja, a probabilidade é 6! vezes maior do que a probabilidade descrita no item.

Gabarito: Errado

Item. 12. (Cebraspe/2019 - Prefeitura de São Cristóvão/SE) A sorte de ganhar ou perder,
num jogo de azar,
não depende da habilidade do jogador, mas exclusivamente das probabilidades dos resultados. Um dos jogos mais populares no Brasil é a Mega Sena, que funciona da seguinte forma: de 60bolas, numeradas de 1 a 60, dentro de um globo, são sorteadas seis bolas. À medida que uma bola é retirada, ela não volta para dentro do globo. O jogador pode apostar de 6 a 15 números distintos por volante e receberá o prêmio se acertar os seis números sorteados. Também são premiados os acertadores de 5 números ou de 4números.

A partir dessas informações, julgue o item que se segue.

Se p for a probabilidade de se acertar na Mega Sena com a aposta de um volante com
6 números distintos,
então, apostando-se 8 números, a probabilidade de acerto será igual a 28p.

Comentários:

Vimos que, para acertar os 6 números, com uma aposta de 6 números, há somente 1
possibilidade. Para acertar os 6 números, com uma aposta de 8 números, corresponde à quantidade de maneiras de escolher corretamente 6, dentre 8 números. Sabendo que a ordem não importa, tem-se a combinação de 6elementos, dentre 8:

8! 8 x 7 x 6! 8 x 7

Cs'6 " (8-6)! x 6! " 2! x 6! " 2 28

Logo, a probabilidade de se acertar os 6 números com uma aposta de 8 números é 28
vezes mais provável do que com uma aposta de 6 números.
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 13. (Cebraspe/2018 - BNB) Um tabuleiro quadrado e quadriculado, semelhante a um tabuleiro de xadrez, com 12 linhas e 12 colunas, e, portanto, com 12 x 12 = 144 quadradinhos pintados: 54, na cor azul;30, na cor marrom; 40, na cor amarela; e 20, na cor verde. A cada quadradinho é associado um cartão com dois números, que indicam a posição do quadradinho no tabuleiro; o primeiro número corresponde ao número da linha, e o segundo corresponde ao número da coluna. Por exemplo, o cartão com os números5,10 corresponde ao quadradinho posicionado na linha 5 e na coluna 10. Esses cartões estão em uma urna,da qual podem ser retirados aleatoriamente.

A respeito desse tabuleiro e desses cartões, julgue o item a seguir.

A probabilidade de retirar dessa caixa, de maneira aleatória, um cartão correspondente a um quadrado pintado na cor azul é superior a 1/3.
Comentários:

A probabilidade de um evento é dada por:

z x casos favoráveis n(Á)

P(Á) = = -77K

total de casos n(U)

O total de casos corresponde a todos os 144 quadrados, logo, n(U) = 144.
Os casos favoráveis correspondem aos quadrados azuis, logo n(A) = 54.
Assim, a probabilidade de retirar um cartão de cor azul é:

54 3

PM)=Ü4 = 8 = 0'375

Que é superior a - = 0,33

Gabarito: Certo.

Item. 14. (Cebraspe/2021 - SEED/PR) A tabela a seguir mostra o valor unitário por ação de determinada empresa na bolsa de valores ao longo de dez dias úteis.
Dia

Valor da abertura (em R$)
100,00

90,00

110,00

121,00

120,00

144,00

160,00

194,00

180,00

160,00

Valor do fechamento (em R$)
90,00

110,00

121,00

120,00

144,00

160,00

194,00

180,00

160,00

140,00

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Caso uma pessoa compre ações dessa empresa pelo valor de abertura (VA) e faça a revenda total dessas ações, ao final do mesmo dia, pelo valor de fechamento (VF), o lucro ou o prejuízo percentual diário (LP)poderá ser calculado pela seguinte fórmula, de modo que LP > 0 indica lucro e LP < 0 indica prejuízo.
VF — VA

Ainda considerando as informações do texto 6A3-I, suponha que uma pessoa tenha decidido investir nas ações daquela empresa em um único dia entre aqueles 10 dias úteis. Suponha, também, que a escolha da data do investimento tenha sido tomada aleatoriamente e que tenha ocorrido antes do primeiro dia listado na tabela. Nessas condições, a probabilidade de essa pessoa ter um lucro superior a 20% é de a) 10%
b) 20%

c) 30%

d) 40%

e) 50%

Comentários:

A probabilidade de a pessoa ter um lucro superior a 20%, entre o valor de fechamento e o de abertura de um único dia, em um desses 10 dias indicados na tabela, corresponde à razão entre o número de dias em qcie o lucro diário superou 20% e o número total de dias (no caso, 10).
Para sabermos o número de dias em que o lucro superou 20%, precisamos calcular o lucro diário, conforme tabela a seguir, mas sem perder tempo calculando o percentual do prejuízo:
Dia

1°

2°

Valor da abertura (em R$)

100,00

90,00

Valor do fechamento (em R$)

90,00

110,00

Lucro

Prejuízo
110 - 90

LP= go ~ 22%

39 110,00

121,00

121 - 110

LP= no =10%

49 121,00

59 120,00

69 144,00

120,00

144,00

160,00

Prejuízo
144-120

LP= 12Q

160 - 144

=20%

79 160,00

194,00

LP = = 11%

194-160

LP= 160 = 21%

194,00

180,00

160,00

180,00

160,00

140,00

Prejuízo
Prejuízo
Prejuízo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Portanto, o número de dias em que o lucro foi superior a 20% foi 2 (2^ e 7Q dias):

p casos favoráveis casos totais
Gabarito: B

Item. 15. (Cebraspe/2022 - PC/PB)

Residência
João Pessoa

Outras cidades da Paraíba
Outros Estados

Homem

Mulher

A tabela acima mostra os resultados de uma pesquisa feita em um Shopping Center em João Pessoa sobre o local de residência de seus frequentadores, na qual foram entrevistadas 240 pessoas. Todas as fichas das240 pessoas entrevistadas foram colocadas em um fichário. Nessa situação, se uma das fichas for retirada aleatoriamente do fichário, a probabilidade da ficha corresponder a uma mulher residente na Paraíba é a) inferior a 0,35
b) superior a 0,36 e inferior a 0,42

c) superior a 0,56

d) superior a 0,43 e inferior a 0,49

e) superior a 0,50 e inferior a 0,55

Comentários:

Essa questão pede de selecionar aleatoriamente uma mulher residente na Paraíba. O
enunciado informou que há um total de 240 fichas, que é o número de casos totais n([7) = 240.
E os casos favoráveis correspondem às mulheres residentes na Paraíba. Segundo a tabela,
há 83 mulheres de João Pessoa (capital da Paraíba) e 30 mulheres de outras cidades da Paraíba, logo,o número de casos favoráveis é:
Portanto, a probabilidade desejada é:

nQ4) = 83 + 30 = 113

casos favoráveis n(X) 113

casos totais 240

Que é superior a 0,43 e inferior a 0,49.

Gabarito: D

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 16. (Cebraspe/2022 - PETROBRAS) O item a seguir é apresentada uma situação hipotética seguida de uma assertiva a ser julgada a respeito de probabilidade e estatística.
De 10 contêineres, numerados de 1 a 10, deseja-se inspecionar ao acaso três deles.
Sabendo que existem cargas irregulares nos contêineres 2, 5 e 7 e que a probabilidade de escolherem qualquer trio de contêineres é a mesma, então a probabilidade de a equipe de inspeção escolher os contêineres problemáticos é superior a 1%.
Comentários:

A questão informa que serão selecionados 3 contêineres, dentre 10, e pede a probabilidade de selecionar 3contêineres específicos.

casos favoráveis n(A)
casos totais n(U)

Nessa situação, há um único evento favorável nQ4) = 1; e o total de eventos corresponde às possibilidades de selecionar quaisquer 3 elementos, dentre 10 (combinação):
10! 10x9x8x7!

nÇU) - C10j3 - (1Q _ 3)j x 3! - 7! x 3!

E a probabilidade é:

10 x 9 x 8

= 10 x 3 x 4 = 120

3x2x1

P =

Que é inferior a 1% = —.

Gabarito: Errado.

Item. 17. (Cebraspe/2021 - PC/DF) Luís, Fernando, Paulo, Carlos e Marcos, suspeitos de terem praticado determinado crime, foram convocados para depor. Na delegacia, ocorreram os eventos descritos a seguir.
* Marcos e Carlos preferiram ficar em silêncio.

* Fernando afirmou que o culpado era Marcos ou Carlos.

* Luís afirmou que o culpado era Fernando ou Carlos.

* Paulo afirmou que o culpado era Marcos ou Fernando.

Considerando que exatamente dois deles são culpados e que, em 2021, todos eles terão mais de quinze anos de idade, julgue o item a seguir.
Se dois desses acusados forem aleatoriamente escolhidos para uma acareação, a probabilidade de serem os dois culpados é igual a 1/10.
Comentários:

A questão informa que há 2 culpados dentre os 5 suspeitos e pede a probabilidade de,
ao selecionar 2
suspeitos, escolher os 2 culpados.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nessa situação, há um único caso favorável, qual seja a seleção dos 2 suspeitos.

casos favoráveis = 1

E os casos possíveis corresponde à seleção de 2 suspeitos quaisquer dentre todos os 5 (combinação):

5x4

casos possíveis = C₅>2

—— = 5x2 = 10

E a probabilidade é a razão entre esses resultados:

casos favoráveis 1

casos possíveis 10

Gabarito: Certo

Item. 18. (Cebraspe/2021 - PM/TO) Cinco pessoas (Arnaldo, Bernardo, Cláudio,
Diógenes e Ernesto),
suspeitas de determinada contravenção, são chamadas para acareação por uma autoridade policial.Exatamente dois deles são culpados, e as seguintes declarações foram feitas durante o depoimento:

I. Arnaldo disse que os culpados não foram Ernesto nem Bernardo;

II. Bernardo disse que os culpados não foram Arnaldo nem Cláudio;

III. Cláudio disse que os culpados não foram Bernardo nem Diógenes.

Se 3 pessoas forem aleatoriamente escolhidas entre os 5 suspeitos, então a probabilidade de os dois culpados serem escolhidos será igual a a) 1/10
b) 3/10

c) 2/15

d) 13/20

e) 11/15

Comentários:

A questão informa que há 2 culpados dentre os 5 suspeitos e pede a probabilidade de,
ao selecionar 3
suspeitos, escolher os 2 culpados. Os casos favoráveis correspondem à seleção dos 2
culpados e de mais um suspeito, dentre os 3 que restaram:
casos favoráveis = 3

E os casos possíveis corresponde à seleção de 3 pessoas quaisquer dentre todos os 5 suspeitos
(combinação):

5! 5x4x3! 5x4

™sos possíveis = C„ = (5_3)!x3, = 2!x3, = — = 5 x 2 = 10
E a probabilidade é a razão entre esses resultados:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

casos favoráveis 3

casos possíveis 10

Gabarito: B.

Item. 19. (Cebraspe/2022 - UNB) Em uma viagem de turismo, um grupo com 18 passageiros,
acompanhados de um guia turístico, serão transportados do aeroporto até o hotel em um micro-ônibus. Desses passageiros, 12 são membros da mesma família, constituída por 5 crianças e 7 adultos,sendo Paulo um dos adultos. Durante o trajeto, o guia turístico escolherá, por meio de sorteio aleatório, quatro passageiros do grupo e, a cada um deles, entregará um brinde.
Considerando essa situação hipotética, julgue o item a seguir.

A probabilidade de Paulo ser um dos sorteados é superior a 0,2.

Comentários:

O enunciado informa que serão sorteadas 4 pessoas, dentre 18, e o item pede a probabilidade de Paulo ser um dos sorteados:
casos favoráveis n(A)

casos totais n(U)

Os casos totais correspondem às maneiras de sortear 4 pessoas, dentre 18, ou seja, à combinação de 4elementos, dentre 18:

18! 18x17x16x15x14! 18x17x16x15

n{U) - C18i4 - Q8 4 X4! 14! x 4! -
4 x 3 x 2 x 1

Não vamos fazer esse cálculo agora, para evitarmos cálculos desnecessários.

E os casos favoráveis correspondem às maneiras de sortear Paulo e outras 3 pessoas quaisquer, dentre as 17que restaram. Logo, temos a combinação de 3 elementos, dentre 17:

r 17! 17x16x15x14! 17x16x15

níA) - C17>3 - (17_3)!x3! - 14! x 3!
- 3x2x1

E a probabilidade buscada é a razão entre os casos favoráveis, nQ4), e os casos totais, n(L/):
17 x 16 x 15 lT^x jXx jX

p = ^.= 32£2 =
=±_1X± = 2_0222

n(U} 18x17x16x15 18 x j/xXx X 18 18

4x3x2 4xZxZ 4

Que é superior a 0,2.

Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 20. (Cebraspe/2022 - UNB) Em uma viagem de turismo, um grupo com 18 passageiros,
acompanhados de um guia turístico, serão transportados do aeroporto até o hotel em um micro-ônibus. Desses passageiros, 12 são membros da mesma família, constituída por 5 crianças e 7 adultos,sendo Paulo um dos adultos. Durante o trajeto, o guia turístico escolherá, por meio de sorteio aleatório, quatro passageiros do grupo e, a cada um deles, entregará um brinde. Considerando essa situação hipotética, julgue o item a seguir.
A probabilidade de os quatro sorteados não serem da família de Paulo é superior a 1/200.

Comentários:

O enunciado informa que há 18 passageiros, dos quais 12 são da família de
Paulo. Para calcular a probabilidade de os 4 sorteados não serem da família, devemos calcular o número de maneiras de selecionar4 membros, dentre os 6 que não são da família (eventos favoráveis):

6! 6x5x4!

n^) - CA4 - (6-4)! x4! _ 2! x 4!

6x5

= —^—=3 x 5 = 15

E os eventos possíveis correspondem à seleção de 4 pessoas, dentre todas as 18:

3 4

18! 18x17x16x15x14! 1#5< 17 x>6 x 15

nÇU) - C18i4 - (18_4)| x4! - 14! x 4!
- 1

n(t/) = 3 x 17 x 4 x 15 = 204 x 15

E a probabilidade corresponde à razão entre os eventos favoráveis e os eventos possíveis:

n(Â) 15 1

P ~ n(U') ~ 204 x 15 ~ 204

Que é inferior a 1/200 (o denominador é maior).

Gabarito: Errado

Item. 21. (Cebraspe/2022 - PC/PB) Um levantamento identificou que, em um hospital infantil, os pacientes seguiam a seguinte distribuição por idade.
Idade (anos)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com relação à distribuição de frequência da idade dos pacientes apresentada no texto acima, assinale a opção correta.
a) Se forem escolhidas duas crianças aleatoriamente para fazerem um exame clínico, a probabilidade de as duas crianças terem 2 anos de idade é de 8,0%.
b) Caso seja escolhida aleatoriamente uma criança para fazer um exame clínico, a probabilidade de ela ter 3anos ou mais é de 60,0%.

c) Se todas as crianças com quatro anos ou mais estiverem brincando no jardim do hospital no momento que foi escolhida aleatoriamente uma criança com 3 anos para também ir ao jardim, a chance de uma criança específica ser a escolhida é de 26,9%.
d) Caso uma criança seja escolhida aleatoriamente para fazer um exame clínico e, no dia seguinte, mais uma criança seja escolhida aleatoriamente para fazer este mesmo exame, a probabilidade de a mesma criança ser escolhida nos dois dias é de 3,3%.
e) Se forem escolhidas quatro crianças aleatoriamente para fazer um exame clínico, a probabilidade de nenhuma delas ter 3 anos ou mais é de 14,1%.
Comentários:

Para resolver essa questão, precisamos calcular as probabilidades indicadas em cada alternativa, com base no gráfico. Segundo este, há 10 crianças de 1 ano, 9 crianças de 2 anos, 7 crianças de 3 anos, 3crianças de 4
anos e 1 criança de 5 anos, totalizando 30 crianças ao todo.

Em relação à alternativa A, a probabilidade de 2 crianças escolhidas terem
2 anos é a razão entre a combinação de 2 elementos, dentre as 9 crianças de 2 anos (eventos favoráveis), e a combinação de 2elementos, dentre todas as 30 crianças (todos os eventos possíveis):

p eventos favoráveis C92
eventos possíveis C302

Calculando as combinações em separado, temos:

9! 9x8x7!

Cg'2 " (9 - 2)! x 2! " 7! x 2!

30! 30 x 29 x 28!

C30'2 " (30 - 2)! x 2! " 28! x 2!

E a probabilidade corresponde à razão entre esses resultados:

9x8

—— = 9 x 4 = 36

30 x 29

----- - ----- = 15 x 29 = 435

Embora seja próximo, a alternativa A afirmou a probabilidade é 8,0% (e não 8,3%) e por isso está incorreta.
Em relação à alternativa B, a probabilidade de 1 criança escolhida ter 3 anos ou mais é a razão entre o número de crianças com 3 ou mais anos de idade (eventos favoráveis) e o número total de crianças (total de eventos possíveis):
eventos favoráveis

P =

eventos possíveis

7 + 3 + 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E não 60%, como indicado na alternativa B, logo, ela está incorreta.

Em relação à alternativa C, a probabilidade de selecionar uma criança específica,
dentre as crianças com 3
anos, é a razão entre 1 (eventos favoráveis: a criança específica) e o número total de crianças com 3 anos(total de eventos possíveis):

eventos favoráveis 1

P = = - = 14,3%

eventos possíveis 7

E não 26,9%, como indicado na alternativa C, e por isso ela está incorreta.

A alternativa D informa que uma criança será escolhida para fazer um exame e que, no dia seguinte, mais uma criança será escolhida para fazer o mesmo exame. Com essa redação, entendemos que outra criança será escolhida no dia seguinte, ou seja, não escolheríamos a mesma criança em ambos os dias. Por isso, a alternativa D está incorreta.
Em relação à alternativa E, a probabilidade de, dentre 4 crianças selecionadas, nenhuma ter 3 anos ou mais corresponde à razão entre a combinação 4 crianças dentre aquelas com 1 ou 2 anos (eventos favoráveis) e a combinação de 4 crianças dentre todas as 30 crianças. Sabendo que há 19 crianças com 1 ou 2 anos,temos:

p eventos favoráveis C19j4

eventos possíveis C30 4

Calculando as combinações em separado, temos:

19! 19x18x17x16x15! 19x18x17x16

Cl9'4 " (19-4)! x 4! " 15! x 4! "
4!

Vamos deixar para fazer as contas depois:

30! 30 x 29 x 28 x 27 x 26! 30 x 29 x 28 x 27

= =
=

30,4 (30 - 4)!x4! 26! x 4!
4!

E a razão é:

19 x 18 x 17 x 16

Cl9,4 4! 19 x 18 x 17 x 16

r

L30,4

30 x 29 x 28 x 27 ~ 30 x 29 x 28 x 27

4!

19 x Itfx 17 x 16C4 19x17x4 1292

P = = = — 14
1%

5^x29x2í^/279 5 x 29 x 7 x 9 9135

Que é o resultado indicado na alternativa E.

Gabarito: E

Item. 22. (Cebraspe/2021 - CBM/TO) Considere que em um plantão estejam trabalhando 10
bombeiros, 4
mulheres e 6 homens, e que 3 dessas pessoas devam ser escolhidas ao acaso para atender a uma ocorrência. Nessa situação, a probabilidade de que sejam escolhidas para o atendimento exatamente 2mulheres é de

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 30%

b) 15%

c) 10%

d) 50%

Comentários:

O enunciado informa que há 4 mulheres e 6 homens (total de 10 pessoas) e que serão selecionadas 3
pessoas; e pede a probabilidade de escolher exatamente 2 mulheres.

As possibilidades de escolher exatamente 2 mulheres (eventos favoráveis)
corresponde à seleção de 2
mulheres dentre as 4 (combinação) E à seleção de 1 homem dentre os 6. Pelo princípio multiplicativo,devemos multiplicar esses resultados:

casos favoráveis = C42 x 6

4! 4x3x2! 4x3

C<'2 " (4 - 2)! x 2! " 2! x 2! " 2 " 6

casos favoráveis = 6 x 6 = 36

E os casos possíveis correspondem à seleção de quaisquer 3 pessoas, dentre os 10:

10! 10x9x8x7! 10x9x8

CaS0S p0SS,'FeÍS = C'« = (10-3)! x 3! = 7!x3! =
3x2x1 = 10 x 3 x 4 = 120

E a probabilidade é a razão entre esses resultados:

casos favoráveis 36 3

Gabarito: A

P = c-a--s-o--s-Lp=oTs^sí=ve-^is= 30%

120 10

Item. 23. (Cebraspe/2021 - ALE/CE) Uma urna contém 10 bolas idênticas, exceto pela cor: duas bolas são da cor azul e as outras 8 bolas são da cor vermelha. As bolas encontram-se misturadas,aleatoriamente,
dentro da urna. Retirando-se, simultaneamente e aleatoriamente, cinco bolas da urna, a probabilidade de a amostra contemplar, exatamente, 1 bola da cor azul e 4 bolas da cor vermelha é igual a e) 3.125
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

O enunciado informa que há 2 bolas azuis e 8 bolas vermelhas (total de 10 bolas) e que serão selecionadas
5 bolas; e pede a probabilidade de escolher exatamente 1 bola azul e 4 bolas vermelhas.

Os eventos favoráveis correspondem à seleção de 4 bolas, dentre as 8 vermelhas
(combinação) E à seleção de 1 bola dentre as 2 azuis. Pelo princípio multiplicativo, devemos multiplicar esses resultados:
casos favoráveis = C8,4 x 2

8! 8x7x6x5x41 8fx 7 xXx 5

Cs'4 " (8 - 4)! x 4! " 4! X 4! ~ 4Ó< ZxZx 1 " 2 x 7 x 5

casos favoráveis =2x7x5x2

Não vamos fazer essa conta agora. E os casos possíveis correspondem à seleção de quaisquer 5 bolas,
dentre os 10:
10! 10x9x8x7x6x5! lXx 9 x Qfx 7 xíf casos possíveis = C10.5 = (10_5),x5, =--------------------------------- 5^= yx#x2-xyxl

Cio,5 = 2x9x2x7
E a probabilidade é a razão entre esses resultados:

casos favoráveis 2 x 7 x 5 x 2 5

casos possíveis 2 x 9 x 2 x 7 9

Gabarito: C

Item. 24. (Cebraspe/2022 - TELEBRAS)

Amostragem Aleatória Simples
I Com reposição

II Sem reposição

Tamanho da amostra

Suponha que determinada população de tamanho N = 100 seja constituída pelos elementos xi, xioo-Para a realização de um levantamento amostrai sobre essa população, cogitam-se duas possibilidades mostradas no quadro anterior, ambas pelo método de amostragem aleatória simples. Se o tipo I for o escolhido, então a amostragem será com reposição com n = 6. No entanto, se o escolhido for o tipo II,então a amostra será sem reposição com n = 5. Com base nessas informações, julgue o item que se segue.
Se o tipo II for aplicado, a probabilidade de que a amostra seja formada pelos elementos x8, x27, x70, x77, x9g é igual a *
Comentários:

Essa questão informa que há 100 elementos, dos quais 5 serão selecionados sem reposição, e pede a probabilidade de determinados 5 elementos serem selecionados:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

casos favoráveis n(A)

P =

casos totais n(U)

Os eventos favoráveis correspondem à escolha dos 5 elementos definidos, n(A) = 1.

Os eventos possíveis correspondem à escolha de 5 elementos quaisquer, dentre 100 (combinação):

n(t/) — C100j5

Sendo uma outra forma de representar a combinação de 5 elementos dentre 100.

Logo, a probabilidade é a razão entre 1 e a combinação

-i

Gabarito: Certo.

Item. 25. (Cebraspe/2021 - CBM/AL) Determinado dado tetraédrico (dado em formato de tetraedro regular),com vértices numerados de 1 a 4, foi lançado 21 vezes, de modo que o resultado do lançamento desse dado correspondia ao vértice voltado para cima. A tabela seguinte mostra a frequência com que se obteve cada resultado.
Resultado Quantidade de Lançamentos

1 2

2 5

3 5

4 9

Com base nessa situação hipotética, julgue o item a seguir.

A frequência percentual do resultado 3 é superior a 25%.

Comentários:

Essa questão trabalha com a definição frequentista (ou frequencista) de probabilidade, definida como a razão entre o número de observações do evento e o número total de repetições.
Nessa questão, o número de observações da face 3 é igual a 5 e o número total de repetições (no caso,lançamentos) é 21:

Que é inferior a 25%.

Gabarito: Errado.

n- total de repetições zi

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)
ívivw. estrategiaconcursos. com. br

Combinações de Eventos

Item. 1. (Cebraspe/2021 - MJ/SP) Ao procurar ativos para realizar operações de day trade em uma lista de
260 ações negociadas em bolsa de valores, um investidor classificou 120 ações como de boa liquidez(elevado volume de negócios realizados diariamente) e 130 ações como de bom nível de volatilidade(muitas variações de preço para cima ou para baixo ao longo do dia); 45 ações ele não classificou em nenhuma dessas classes. Tendo em vista essa situação hipotética, julgue o item seguinte.
Selecionando-se ao acaso uma das ações da lista analisada pelo investidor, a probabilidade de que essa ação tenha bom nível de volatilidade é maior que a probabilidade de ela não ter bom nível de volatilidade.
Comentários:

A probabilidade é a razão entre o número de eventos favoráveis e o número total de eventos possíveis. Oenunciado informa que existem 130 ações com bom nível de volatilidade e 260 ações no total. Assim, a probabilidade de selecionar uma ação com bom nível de volatilidade é:
n((J) 260 2

E a probabilidade de selecionar uma ação que não tenha bom nível de volatilidade é complementar:

Logo, essas probabilidades são iguais.
Gabarito: Errado

Item. 2. (Cebraspe/2021 - SERPRO) Em um curral, há doze bezerros, entre os quais apenas três sofrem de diarreia virai bovina, sendo os demais saudáveis. Dois bezerros desse curral serão escolhidos aleatoriamente. Nessa situação hipotética, a probabilidade de se escolher pelo menos um bezerro que sofra de diarreia virai bovina é igual a
0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

O enunciado informa que há 12 bezerros, dos quais 3 são doentes, e que serão selecionados 2
bezerros.

A probabilidade de escolher pelo menos um doente pode ser calculada pela probabilidade do evento complementar, qual seja de que todos os 2 bezerros escolhidos sejam saudáveis:
Pípelo menos um doente) = 1 — Pítodos saudáveis)

A probabilidade é a razão entre os eventos favoráveis e o total de eventos possíveis:

nítodos saudáveis)

Pítodos saudáveis) =

n(JJ)

O total de eventos possíveis corresponde a todas as maneiras de selecionar 2 bezerros,
dentre 12, sabendo que a ordem da escolha não importa (combinação):
12! 12x11x10! 12x11

Cl2-2 (12-2)! x 2! 10! x 2! 2 - 6 x 11 - 66

E os eventos favoráveis corresponde a escolha de 2 bezerros saudáveis. Sabendo que dos
12 bezerros, 3 são doentes, o número total de bezerros saudáveis é 12 - 3 = 9:
9! 9x8x7! 9x8

Cg'2 " (9 - 2)! x 2! " 7! x 2! " 2 " 9 x 4 " 36

E a probabilidade do evento complementar é a razão entre esses resultados:

36 6

Pítodos saudáveis) = — = —

66 11

E a probabilidade de encontrar pelo menos um doente é complementar:

6 11 6 5

Pípelo menos um doente) = 1 — Pítodos saudáveis) = ~YÍ = —ií— = ii

Gabarito: E

Item. 3. (Cebraspe/2021 - SERPRO) Suponha que sejam gerados 5 números válidos de CPF
para serem atribuídos a 5 indivíduos distintos. Com base nessas informações, julgue o item a seguir.
Suponha que, logo após a atribuição dos CPFs aos indivíduos, são escolhidos aleatoriamente 2 desses CPFs e separados 3 desses indivíduos. Nessa situação, a probabilidade de pelo menos um dosCPFs escolhidos pertencer a um dos indivíduos separados é igual a 3/5.
Comentários:

O enunciado informa que 5 CPFs serão distribuídos a 5 indivíduos e que serão selecionados 2 CPFs e 3indivíduos. A questão pede a probabilidade de pelo menos um CPF pertencer a um indivíduo separado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para isso, vamos calcular a probabilidade do evento complementar, qual seja de que nenhum dos CPFs pertença a um indivíduo selecionado:
P(pelo menos um) = 1 — P (nenhum)

Sabemos que a probabilidade é a razão entre os eventos favoráveis e o total de eventos possíveis:

n(nenhum)

P (nenhum) =------------ t—t--------

n(U)

O total de eventos possíveis corresponde a todas as maneiras de selecionar 2 CPFs E
3 indivíduos. Como a ordem não importa temos a combinação de 2 elementos dentre 5, multiplicada pela combinação de 3
elementos dentre 5:

n((/) — C5 2 x C5 3

Calculando as combinações em separado, temos1 * 3:

C5,2

5!

(5 - 2)! x 2!

5!

5x4x3!
3! x 2!

5x4x3!

5x4

—=10

5x4

^5,3 (5 — 3)! x 3!

E o total de eventos possíveis corresponde ao produto:

2! x 3!

—=10

n(U) = 10 x 10 = 100

E os eventos favoráveis são aqueles em que nenhum dos CPFs escolhidos pertence a um indivíduo escolhido.Em outras palavras, escolhemos 2 CPFs, dentre 5, e os 3 indivíduos já estarão definidos, pois são aqueles dosCPFs não escolhidos:

5!
n(nentam) = C5-2 = (5_2),x2, - -37737

5x4x3! 5x4

= 10

Portanto, a probabilidade do evento complementar é a razão:

n (nenhum) 10 1

P {nenhum) =----------T777\-----—

n(U) ÍÕ

E a probabilidade buscada é:

P(pelo menos um) = 1 — P (nenhum) =

Que é diferente de -.

1 9

1 _iõ 1Õ

Gabarito: Errado

1 Aqui, vale lembrar que a combinação de k elementos, dentre n é igual à combinação (n - k)
elementos, dentre n:

^n,k — Cn,(n-k)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 4. (Cebraspe/2021 - ALE/CE) Considere um experimento aleatório cujo espaço amostrai seja representado por fl e, ainda, dois eventos aleatórios A e B, tais que A c B c fi.Se as probabilidades de ocorrência dos eventos A e B forem P(A) = 0,2 e P(B) = 0,3, então P(AUB) é igual a a) 0,06
b) 0,1

c) 0,2

d) 0,3

e) 0,5

Comentários:

O enunciado informa que o evento A está contido no evento B, conforme ilustrado a seguir.

Desse modo, a união dos eventos A e B corresponde ao próprio evento B, cuja probabilidade é 0,3:
P(A U B) = P(B) = 0,3

Gabarito: D

Item. 5. (Cebraspe/2022 - PETROBRAS) Considerando dois eventos aleatórios A e B, tais que P(A U B) =
P(i4) > 0, P(A n B) = P(JT) > 0 e P(.4) + = 1, julgue o item que se segue.
Se Ac denota o evento complementar de A, então é correto afirmar que Ac = B.
Comentários:

O enunciado informa que a probabilidade da união dos eventos A e B equivale à probabilidade do evento A;e que a probabilidade da interseção dos eventos equivale à probabilidade do evento B.
Para que isso seja possível, é necessário que o evento B esteja contido no evento A, conforme ilustrado a seguir:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabemos que o evento complementar corresponde a todos os demais eventos. Ou seja, o complementar do evento A corresponde a todos os demais eventos, exceto o evento A, conforme indicado em cinza na figura a seguir:
Podemos observar que o complementar de A é bem diferente de B.

Gabarito: Errado

Item. 6. (Cebraspe/2021 - Pref. Aracaju) Considere dois eventos A e B contidos em determinado espaço amostrai tal que A £ B. Se as probabilidades de ocorrências desses eventos e de seus eventos complementares forem P(A') = 0, 3, P(B) = 0,7, P(A) = 0,7 e P(B) = 0, 3, então a) P(4 UB) = 1
b) P(4 0B) = 0,21

c) P(4 U B) = 0,3

d) P(A n B) = 0,3

e) P(4 n B) = 0,4

Comentários:

A questão informa que A está contido em B, sendo P(A) = 0,3 e P(B) = 0,7, conforme ilustrado a seguir:
Em relação à alternativa A, a união dos eventos A e B corresponde ao próprio evento B:

P(A UB) = P(B) = 0,7

Logo, a alternativa A está incorreta.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação à alternativa B, a interseção dos eventos A e B corresponde ao próprio evento A:

P(A n B) = PQ4) = 0,3

Em relação à alternativa C, o evento A corresponde a toda região fora de A, indicada em cinza na ilustração a seguir, ao lado esquerdo; e o evento B corresponde a toda região fora de B,indicada em cinza na ilustração a seguir, ao lado direito.
Podemos observar que a união de ambas as regiões corresponde à própria região indicada à esquerda, qual seja o evento A, cuja probabilidade é 0,7, conforme indicado no enunciado:
P(Ã U B) = P(Á) = 0,7

Portanto, a alternativa C está incorreta.

A alternativa D trabalha com a interseção entre os eventos A, indicada em verde na figura abaixo, e B,
indicada em cinza na mesma figura.

Podemos observar que não há interseção entre essas regiões, logo a sua probabilidade é nula:

P(A n B) = 0

A alternativa E trabalha com a interseção entre o evento A, indicada em cinza na figura da esquerda, e o evento B, indicada em azul na figura da direita:
A
F

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos observar que a interseção corresponde a região que pertence a B, mas não pertence a A, que corresponde à diferença entre a probabilidade de B e a probabilidade de A:
P(4 nB) = P(B\X) = P(B) - P(A n B) = P(B) - PQ4) = 0,7 - 0,3 = 0,4

Logo, a alternativa E está correta.

Gabarito: E

Item. 7. (Cebraspe/2020 - TJ/PA) Se íí representar um espaço amostrai de determinado experimento aleatório, 4cíl e Bcíl forem dois eventos com P(4) = 0,4 e P(JP) = 0,8e se A e B forem,
respectivamente, os eventos complementares de A e B, então a) P(4 0 B) > 0, 2
b) P(A U B) + P(A n B) < 1

c) P(A n A n 71) = 0, 064

d) 0,2 < P(4 0B) < 0,4

e) P(Ã n B) + P(Ã n B) > 0,7

Comentários:

O enunciado informa que P(A) = 0,4 e que P(B) = 0,8.

Considerando que a união desses eventos tem probabilidade no máximo igual a
1, podemos calcular a probabilidade mínima da interseção:
P(A U B) = P(2l) + P(B) - P(A n B) < 1
0,4 + 0,8 - P(A n B) < 1

1,2 - P(A n B) < 1

0,2 < P(A n B)

Por outro lado, a união desses eventos é no mínimo igual ao maior evento, no caso,
o evento B. Nessa situação, o evento A estaria totalmente contido no evento B e a interseção seria igual ao próprio evento A:
P(A U B) = PQ4) + P(B) - P(4 n B) > P(B)
PQ4) > P(A n B)

Sabendo que P(A) = 0,4, a probabilidade máxima da interseção é:

PQ4 n B) < 0,4

Ou seja, a probabilidade da interseção é no mínimo igual a 0,2 e no máximo igual a
0,4 e assim concluímos que a alternativa D está correta.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação à alternativa A, vamos calcular as probabilidades dos eventos complementares:

PQ4) = 1 - P(Â) = 1 - 0,4 = 0,6

P(B) = 1 - P(B) = 1 - 0,8 = 0,2

Portanto, a interseção entre esses eventos é no máximo igual ao evento menor, no caso, o evento B:

PÇÃ n Ã) < P(5)

PÇÃ OB) < 0,2

Portanto, a alternativa A está incorreta.

Em relação à alternativa B, vamos reorganizar a fórmula da união:

PÇA UB) = PÇA) + P(B) - P(Â n B)
PÇA U B) + PÇA n B) = P(A) + P(B)
PÇA U B) + PÇA n B) = 0,4 + 0,8 = 1,2

E assim concluímos que a alternativa B está incorreta.

Em relação à alternativa C, a interseção de um evento com ele mesmo é igual ao próprio evento:

PÇA n A n 21) = PÇA) = 0,4

Logo, a alternativa C está incorreta.

Em relação à alternativa E, a interseção do complementar do evento A com o evento B
corresponde ao evento B/A, conforme ilustrado a seguir:
PÇA OB) = PÇB/A) = PÇB) - PÇA n B)

Ademais, a interseção dos complementares corresponde ao complementar da união:

PÇA n B) = 1 - PÇA U B)

Assim, a soma de ambas as probabilidades é:

PÇÃ n B) + PÇÃ nB) = PÇB) - PÇA UB) + 1 - PÇA U B)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

p(A n B) + p(4 nB) = P(B) + l - [Pd n B) + p(a U B)J

Vimos que P(A U B) + P(A ílB) = 1,2, logo:

P(Ã n B) + P(Ã nB) = 0,8 + 1- 1,2 = 0,6

Que é menor que 0,7, logo a alternativa E está incorreta.

Gabarito: D

Item. 8. (Cebraspe/2021 - PF) Considere os seguintes conjuntos:

p =
Pl =
p2 =

p3 =

{todos os policiais federais em efetivo exercício no país}

{policiais federais em efetivo exercício no país e que têm até 1 ano de experiência no exercício do cargo}
{policiais federais em efetivo exercício no país e que têm até 2 anos de experiência no exercício do cargo}
{policiais federais em efetivo exercício no país e que têm até 3 anos de experiência no exercício do cargo}
e, assim, sucessivamente. Com base nessas informações, julgue o item que se segue.

Escolhendo-se aleatoriamente um integrante do conjunto P, a probabilidade de ele ter entre dois e três anos n(p p )
de experiência no exercício do cargo é dada por , em que n(X) indica o número de elementos do conjunto X e P₂- P3 é 0 conjunto formado pelos indivíduos que estão em P₂, mas não estão em P₃.
Comentários:

Pela tabela, observamos que P₂ é 0 conjunto dos policiais com experiência de até 2
anos e que P₃ é 0
conjunto de policiais com experiência de até 3 anos. Assim, 0 conjunto de policiais com experiência entre 2e 3 anos corresponde à diferença entre os conjuntos P₃ e P₂:

P₃ — P₂ = {policiais com experiência entre 2 e 3 anos}

E a probabilidade de selecionar aleatoriamente um integrante desse conjunto é a razão entre 0 número de policiais que pertencem a esse conjunto e 0 número total de policiais:
Prob = n(P3~P2)
n(P)

Assim, a probabilidade indicada no item está incorreta, tanto em relação ao numerador
(inversão de P₂ e
P₃), quanto em relação ao denominador.

Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Probabilidade Condicional

Item. 1. (Cebraspe/2022 - PETROBRAS) No que diz respeito aos conceitos e cálculos utilizados em probabilidade e estatística, julgue o item a seguir.
Considere que, em uma sala de provas de um concurso, ao se selecionar aleatoriamente um candidato para acompanhar a abertura do envelope de provas, a probabilidade de ele ter estudado em escola particular é0,32 e a probabilidade de ele ter estudado em escola particular e ser um candidato forte à aprovação é 0,24.Nessa situação, se o candidato selecionado estudou em escola particular, então a probabilidade de ele ser um candidato forte à aprovação é 0,75.
Comentários:

Essa questão pede a probabilidade condicional de um candidato ser forte dado que estudou em escola particular, que corresponde à razão entre a probabilidade da interseção dos eventos e a probabilidade de o candidato ter estudado em escola particular (evento a priori):
P(F n P)

P(F|P) =

P(P)

O enunciado informa que a probabilidade de o candidato ter estudado em escolar particular é P(P) = 0,32e a probabilidade de o candidato ter estudado em escola particular e ser forte é P(F
n P) = 0,24. Logo, a probabilidade condicional é:
Gabarito: Certo

P(F|P) =

P(F n P)

P(P)

0,24 3

Õ32 4

Item. 2. (Cebraspe/2022 - UNB) Em uma viagem de turismo, um grupo com 18 passageiros,
acompanhados de um guia turístico, serão transportados do aeroporto até o hotel em um micro-ônibus. Desses passageiros, 12 são membros da mesma família, constituída por 5 crianças e 7 adultos,sendo Paulo um dos adultos. Durante o trajeto, o guia turístico escolherá, por meio de sorteio aleatório, quatro passageiros do grupo e, a cada um deles, entregará um brinde. Considerando essa situação hipotética, julgue o item a seguir.
Se os quatro brindes forem entregues a membros da família de Paulo, então a probabilidade de os sorteados serem as crianças é inferior a 0,01.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A questão pede a probabilidade condicional de os 4 sorteados serem crianças (Cr), dado que são da família de Paulo (Pa):
P(Cr|Pa) =

P(Cr Cl Pa)
P(Pa)

Mas essa probabilidade pode ser calculada pela definição clássica de probabilidade, como a razão entre os eventos favoráveis e os eventos possíveis, mas restringindo o Universo ao sorteio da família dePaulo:

, „ eventos favoráveis
P(Cr) = —

eventos possíveis n(Cr)n(U')

Assim, os eventos possíveis correspondem ao sorteio de 4 membros, dentre os 12 da família de Paulo:

12! 12x11x10x9x8!

n(í7 ) - C12)4 - Q2 _4)| x4! - 8! x 4!j—

12 x 11 x 10 x 9

11 x 4 x 9 = 396

4 x 3 x 2 x 1

E os eventos favoráveis corresponde à seleção de 4 dentre as 5 crianças da família de Paulo:

5x4!

«(Cr) = C5,4 = (5_4),x4! =' 1! x 4! _ 5

E a probabilidade buscada corresponde à razão entre esses resultados:

Que é superior a 0,01 = 1%. Para termos 1% com esse denominador, o numerador precisaria ser 3,96.

Gabarito: Errado

Item. 3. (Cebraspe/2018 - ABIN) A tabela abaixo mostra dados de sobrevivência (em dias) de uma coorte de animais acometidos por uma doença aguda. Na primeira coluna, t corresponde aos dias, sendo t = 0o dia em que a contagem começou a ser feita; vt, na segunda coluna, é a quantidade de animais vivos no início do dia t; dt, na terceira coluna, indica quantos animais morreram no decorrer do dia t.
r n <

0 10 000 500

i 9.500 700

2 8.800 800

1 8000 8<M)

4 7.200 1 080

5 6.120 720

6 5400 1 350

7 4.050 1 350

8 2.700 1.200

9 1.500 1.500

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com referência a essas informações, julgue o item que se segue.

Se um animal que estivesse vivo no início do dia t = 4 fosse escolhido ao acaso, a probabilidade de ele morrer nesse dia seria igual a 15%.
Comentários:

A questão indaga sobre probabilidade condicional. Podemos calcular essa probabilidade, utilizando a fórmula da probabilidade clássica, porém restringindo os casos considerados ao evento que sabemos ter ocorrido, no caso, o fato de o animal estar vivo no início do dia t = 4:
casos favoráveis nÇA)

casos possíveis nflf')

Os casos totais correspondem aos animais vivos no início do dia t = 4. Pela tabela,
observamos que n(U') = v₄

= 7.200.

Os casos favoráveis correspondem aos animais que morreram no dia t = 4. Pela tabela,
observamos que n(A)

= d₄ = 1.080.

Assim, a probabilidade é:

1080

P = 7200 = 15%

Gabarito: Certo.

Item. 4. (Cebraspe/2018 - ABIN) A tabela abaixo mostra dados de sobrevivência (em dias) de uma coorte de animais acometidos por uma doença aguda. Na primeira coluna, t corresponde aos dias, sendo t = 0o dia em que a contagem começou a ser feita; vt, na segunda coluna, é a quantidade de animais vivos no início do dia t; dt, na terceira coluna, indica quantos animais morreram no decorrer do dia t.
r n

0 10 000

i 9.500

2 8.800

1 8000

4 7.200

5 6.120

6 5400

7 4.050

8 2.700

9 1.500

8<M)

1 080

1 350

1 350

1.200

1.500

Com referência a essas informações, julgue o item que se segue.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Se um animal que estivesse vivo no início do dia t = 3 fosse escolhido ao acaso, a probabilidade de ele ter morrido até o dia t = 6 seria superior a 50%.
Comentários:

A questão indaga sobre probabilidade condicional. Podemos calcular essa probabilidade, utilizando a fórmula da probabilidade clássica, porém restringindo os casos considerados ao evento que sabemos ter ocorrido, no caso, o fato de o animal estar vivo no início do dia t = 3:
casos favoráveis nÇA)

casos possíveis nflf')

Os casos totais correspondem aos animais vivos no início do dia t = 3. Pela tabela,
observamos que n(U') = v₃

= 8.000.

Os casos favoráveis correspondem aos animais que morreram desde o dia t = 3 até o dia t = 6 (inclusive).Esse número corresponde à diferença entre a quantidade de animais vivos no início do dia t = 3 (v₃ = 8.000)e a quantidade de vivos no início do dia t = 7 (v₇ = 4.050):

n(A) = V7 - v₃ = 8000 - 4050 = 3950

Assim, a probabilidade é:

Ou seja, é inferior a 50%.

Gabarito: Errado.

3950

P = 8ÕÕÕ = 49'375%

Item. 5. (Cebraspe/2018 - ABIN) A tabela abaixo mostra dados de sobrevivência (em dias) de uma coorte de animais acometidos por uma doença aguda. Na primeira coluna, t corresponde aos dias, sendo t = 0o dia em que a contagem começou a ser feita; vt, na segunda coluna, é a quantidade de animais vivos no início do dia t; dt, na terceira coluna, indica quantos animais morreram no decorrer do dia t.
r n

0 10 000

i 9.500

2 8.800

1 8000

4 7.200

5 6.120

6 5400

7 4.050

8 2.700

9 1.500

8<M>

1 080

1 350

1 350

1.200

1.500

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com referência a essas informações, julgue o item que se segue.

Se um animal que estivesse vivo no início do dia t = 4 fosse escolhido ao acaso, a probabilidade de ele ter chegado vivo no dia t = 7 seria superior a 60%.
Comentários:

A questão indaga sobre probabilidade condicional. Podemos calcular essa probabilidade, utilizando a fórmula da probabilidade clássica, porém restringindo os casos considerados ao evento que sabemos ter ocorrido, no caso, o fato de o animal estar vivo no início do dia t = 4:
casos favoráveis nÇA)

casos possíveis nflf')

Os casos totais correspondem aos animais vivos no início do dia t = 4. Pela tabela,
observamos que n(U') = v₄

= 7.200.

Os casos favoráveis correspondem

= V7 = 4.050.

Assim, a probabilidade é:

Ou seja, é inferior a 60%.

Gabarito: Errado.

aos animais vivos no início do dia t = 7. Pela tabela, observamos que n(A)

4050

P = 72ÕÕ=56'25%

Item. 6. (Cebraspe/2018 - PF) O resultado de uma pesquisa acerca da satisfação de 200
papiloscopistas, no que diz respeito às tarefas por eles executadas de identificação de vítimas e de descobertas de crimes de falsificação, foi o seguinte:
* 30 papiloscopistas sentem-se igualmente satisfeitos ao executar qualquer uma dessas tarefas;

* 180 papiloscopistas sentem-se satisfeitos ao executar pelo menos uma dessas tarefas.

Considerando que todos os 200 papiloscopistas responderam à pesquisa, julgue o item seguinte.

A probabilidade de que um papiloscopista, escolhido ao acaso, tenha se dito igualmente satisfeito ao executar qualquer uma entre as duas tarefas mencionadas, dado que se sente satisfeito ao executar pelo menos uma das duas tarefas, é inferior a 0,15.
Comentários:

A questão indaga sobre probabilidade condicional. Podemos calcular essa probabilidade, utilizando a fórmula da probabilidade clássica, porém restringindo os casos considerados ao evento que sabemos ter ocorrido:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

casos favoráveis n(A')

casos possíveis nflf')

Sabemos que o papiloscopista escolhido se sente satisfeito com pelo menos uma das tarefas, ou seja, n(U')
= 180.

Os casos favoráveis correspondem aos papiloscopistas igualmente satisfeitos em qualquer das duas tarefas,logo, n(A) = 30.

Assim, a probabilidade condicional é dada por:

Que é superior a 0,15.

18Õ

- = 0,1666...

Gabarito: Errado.

Item. 7. (Cebraspe/2018 - ABIN) Considerando os conceitos associados a probabilidade e estatística, julgue o item.
A probabilidade de se obter um número menor que 5 no lançamento de um dado, sabendo que o dado não é defeituoso e que o resultado é um número ímpar, é igual a 2/3.
Comentários:

A questão indaga sobre probabilidade condicional. Podemos calcular essa probabilidade, utilizando a fórmula da probabilidade clássica, porém restringindo os casos considerados ao evento que sabemos ter ocorrido:
casos favoráveis nÇA)

casos possíveis nflf')

No caso, sabemos que o resultado do lançamento do dado é um número ímpar. Assim,
tanto os casos favoráveis, quanto os casos totais, levarão tal fato em consideração.
Ou seja, os casos totais são todos os números ímpares do dado: {1, 3, 5}. Logo, n(U') = 3.
Os casos favoráveis são os números ímpares menores que 5: {1, 3}. Logo, n(A) = 2.

Substituindo esses valores, obtemos:

Gabarito: Certo.

Item. 8. (Cebraspe/2022 - FUNPRESP-EXE) A seguir, são apresentadas informações obtidas a partir de uma pesquisa realizada com 1.000 pessoas.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

* 480 possuem plano de previdência privada;

* 650 possuem aplicações em outros tipos de produtos financeiros;

* 320 não possuem aplicação em nenhum produto financeiro.

Com base nessa situação hipotética, julgue o item seguinte.

Se uma pessoa escolhida ao acaso entre as que participaram da pesquisa possui plano de previdência privada, então a probabilidade de ela possuir também aplicação em outros produtos financeiros é superior a 90%.
Comentários:

O primeiro passo para resolver essa questão é calcular o número de pessoas que estão na interseção, entre aquelas que possuem previdência privada e aquelas que possuem outros tipos de produtos financeiros.
O enunciado informa que, das 1000 pessoas, 320 não possuem aplicação alguma. Logo, o número de pessoas que possuem alguma aplicação, previdência privada (Pr) e/ou outros tipos de produtos (Ou) é:
nÇPr U Ou) = 1000 — 320 = 680

Sabendo que 480 possuem previdência privada e 650 possuem outros produtos, a interseção corresponde à soma desses valores, subtraída do total da união:
n(Pr U Ou) = n(Pr) + n(0u) — n(Pr O Ou)
n^Pr O Ou) = n(Pr) + n(0u) — n^Pr U Ou)
nÇPr n Ou) = 480 + 650 — 680 = 450

Logo, 450 pessoas possuem tanto previdência privada quanto outros produtos. O item pede a probabilidade de uma pessoa possuir outros produtos financeiros, dado que possui previdência privada,que corresponde à razão entre a probabilidade da interseção e a probabilidade do evento a priori (no caso, possuir previdência privada):
P(0u\Pr) = p^

P(Pr n Ou)

Sabendo que a probabilidade é a razão entre os eventos favoráveis e o total de eventos, temos:

n^Pr n Ou) n(Pr n Ou)

P(0u\Pr) =

P(Pr n Ou)
P(Pr)

n(JJ)

n(Pr) n(Pr)

n(JJ) u{0)

n(Pr n Ou)
n(Pr)

Sabendo que na interseção há n(Pr n Ou) = 450 pessoas e que o número de pessoas com previdência privada é n(Pr) = 480, temos:
Que é superior a 90%.

Gabarito: Certo.

P(0u\Pr) =

nÇPr n Ou)
n(Pr)

48Õ

— = 0,9375 = 93,75%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 9. (Cebraspe/2021 - IBGE) Considere que, quando Carlos, agente de pesquisas por telefone, realiza uma chamada telefônica, a chance de que a sua chamada não seja atendida seja de 20%e que, se a chamada for atendida, a chance de que ele obtenha respostas verdadeiras seja de 60%. Nessa situação, a probabilidade de Carlos obter respostas verdadeiras em uma dada chamada telefônica é igual a a) 12%
b) 48%

c) 60%

d) 80%

e) 88%

Comentários:

Essa questão informa a probabilidade de Carlos obter uma resposta verdadeira, dado que foi atendido e pede a probabilidade de ele obter uma resposta verdadeira. Vale notar que ele só obterá uma resposta verdadeira se ele for atendido.
Assim, a questão trabalha com o teorema da multiplicação, em que a probabilidade da interseção pode ser calculada a partir da probabilidade condicional1:
P(7nX) = P(7|4) x PQ4)

O enunciado informa que a probabilidade de Carlos obter uma resposta verdadeira, dado que é atendido éP(V |>1) = 60%; e que a probabilidade de não ser atendido é PQ4) = 20%, ou seja,
a probabilidade de ser atendido é complementar:
P(A) = 1 - P(Á) = 100% - 20% = 80%

Logo, a probabilidade de Carlos receber uma resposta verdadeira (e ser atendido) é:

p(y n Á) = 60% x 80% = 48%

Gabarito: B

Item. 10. (Cebraspe/2021 - BANESE) Considerando que A e B sejam eventos aleatórios independentes e queP(A) = 0,8 e P(B) = 0,2, julgue o próximo item.

FQ4|B)
P(5|Â)

1 O Teorema da Multiplicação é basicamente um rearranjo da definição da probabilidade condicional:

P(7nyl)

WM) = p(x) p(v nA) = p<YiA) x P(A)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Essa questão fornece as probabilidades dos eventos A e B, e pede a razão entre as probabilidades condicionais. Sabendo que a probabilidade condicional é a razão entre a probabilidade da interseção e a probabilidade do evento a priori, temos:
P(A n B) 1

PQ4|B) P(B) P(B) P(B) P{A}

P(B |A) " P(A n B) 1 " PfB)

PQ4) P(A) P(A)

Sabendo que P(A) = 0,8 e P(B) = 0,2, temos:

PG4|B) P(A) 0,8

P(B|?1) P(B) 0^2 4

Gabarito: Certo

Item. 11. (Cebraspe/2021 - BANESE) Considerando dois eventos aleatórios A e B, tais que P(A|B) =
P(B\A) = 0, 5 e P(A U B) = 0, 8, julgue o seguinte item.

PQ4) > P(B).

Comentários:

O enunciado fornece as probabilidades condicionais e pede para compararmos as probabilidades dos eventos. Sabendo que a probabilidade condicional de A dado B é P(54|B) = -, temos:
Reorganizando essa fórmula, temos:

P(X|fí) =

z PÇ4nB)

P(A n B) 1

P(B) 3

P(B) = ———- = 3. P(A n B)

Similarmente, sabendo que a probabilidade condicional de B dado A é P(B|X) = 0,5, temos:

P(A n B)

p(s|i4) = ^G4T = 0'5

z P(/lnB)

PG4) = 05 =2.P(XnB)

Como P(B) — 3. P(A A B) e P(Á) = 2.P(A A B), temos que P(JP) > P(A) e não o contrário.

Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 12. (Cebraspe/2021 - BANESE) Considerando dois eventos aleatórios A e B, tais que
PÇA|B) =

PÇB\A) = 0, 5 e PÇA U B) = 0, 8, julgue o seguinte item.

PÇA A B) = 0,2.

Comentários:

O enunciado fornece as probabilidades condicionais e a probabilidade da união, e pede a probabilidade da interseção. Da questão anterior, vimos que P(B') = 3. PÇA A B) e PÇÁ) = 2. PÇA A B).
Agora, vamos utilizar a fórmula da probabilidade da união:

PÇA U B) = PQ4) + P(B) - PÇA A B)

PÇA U B) = 3. PÇA A B) + 2. PÇA A B) - PÇA A B) = 4. PÇA A B)

Sabendo que essa probabilidade é igual a 0,8, temos:

4.PÇA A B) = 0,8

PÇA A B) = 0,2

Gabarito: Certo

Item. 13. (Cebraspe/2022 - PETROBRAS) Considerando dois eventos aleatórios A e B, tais que PÇA U B) =
PfA) > 0, PÇA A B) = PÇB) > 0 e P(>1) + PÇBÇ) = 1, julgue o item que se segue.

São eventos independentes.

Comentários:

O enunciado informa que a união dos eventos A e B corresponde ao evento A; e que a interseção dos eventos corresponde ao evento B. Para que isso seja possível, é necessário que o evento Besteja contido no evento
A, conforme ilustrado a seguir:

O item pergunta se os eventos são independentes. Por definição, para eventos independentes, vale:

PÇA\BÇ) = PÇA), se A e B forem independentes

No entanto, essa equação é falsa pelo fato de o evento B estar contido no evento A.
Desse modo, dado que ocorreu o evento B, temos certeza de que ocorre o evento A:
PQ4|B) = 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E sabemos que a probabilidade P(A) é menor que 1, já que P(B) > 0.

Assim, concluímos que P(A|B) =# P(Á) e, consequentemente, que os eventos não são independentes.

Gabarito: Errado

Item. 14. (Cebraspe/2021 - BANESE) Considerando que A e B sejam eventos aleatórios independentes e que
P(i4) = 0,8 e P(B) = 0,2 julgue o próximo item.

P(A n B) = 0.

Comentários:

Sabendo que os eventos A e B são independentes, podemos concluir que a probabilidade da interseção equivale ao produto das probabilidades:
P(A n B) = x P(B)

Considerando que P(A) = 0,8 e P(B) = 0,2, temos:

P(A n B) = 0,8 x 0,2 = 0,16

Que é diferente de zero.

Gabarito: Errado

Item. 15. (Cebraspe/2018 - IJSN/ES) Considerando os conceitos associados a probabilidade e estatística,julgue o item.

Com base no espaço amostrai S = {1, 2, 3, 4} é correto afirmar que os eventos A = {2 ,4} e B = {1,
4}, não são independentes.
Comentários:

Para dois eventos (A e B) independentes, temos necessariamente:

P(A n B) = P(i4) x P(B)

Vamos calcular a probabilidade desses três elementos. Sendo A = {2, 4} e S = {1, 2, 3, 4}, então
P(A) é:

z nQ4) 2 1

~ N(S) ~4~2

Sendo B = {1, 4}, então P(B) é:

Portanto, o lado direito da primeira equação é:

P(B) =

n(B)
MS)

2 _ 1

4 " 2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

PQ4)xP(B) =|x| =

Por outro lado, a interseção de Ae Bé:4 CiB = {4}. Logo:

P(A n B)

Ou seja, temos P(A n B) = PQ4) x P(B). Portanto, os eventos A e B são independentes.

Gabarito: Errado.

Item. 16. (Cebraspe/2021 - SEDUC/AL) O próximo item apresenta uma situação hipotética a ser julgada,acerca de problemas matemáticos envolvendo situações em uma escola.

No primeiro andar de uma escola, todas as 10 salas de aula possuem as portas do mesmo lado e em sequência. Três alunos distraídos, mexendo em seus celulares, estão indo em direção a suas respectivas salas de aula, porém, como estão distraídos, eles podem entrar em qualquer uma das salas, de forma independente. Nessa situação hipotética, a probabilidade de os três alunos entrarem exatamente na mesma sala é de 1%.
Comentários:

A questão informa que há 10 portas e pede a probabilidade de 3 alunos entrarem aleatoriamente na mesma porta.
Vamos imaginar que o primeiro aluno selecione uma porta qualquer. Sabendo que há 10 portas, a probabilidade de o segundo aluno selecionar a mesma porta é^; e a probabilidade de o terceiro aluno selecionar a mesma porta é também —.
K 10

Considerando que são eventos independentes, a probabilidade da interseção é o produto:

1 1 _ 1

1%

iõx iõ - lõõ

Gabarito: Certo

Item. 17. (Cebraspe/2018 - IJSN/ES) Considerando os conceitos associados a probabilidade e estatística,julgue o item. Considere que de uma urna contendo 2 bolas azuis e 6 bolas brancas retira-se ao acaso uma bola, anota-se sua cor e repõe-se a bola na urna. Em seguida retira-se novamente uma bola da urna e anota-se sua cor.
Nessas condições, a probabilidade das duas bolas retiradas serem azuis é %.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A probabilidade de retirar uma bola azul, considerando que há 2 bolas azuis e 6
bolas brancas, ou seja, 8
bolas, no total, é dada por:

nQ4)

PG4) =

n((7)

2 _ 1

8 " 4

A probabilidade de retirar 2 bolas azuis (isto é, a primeira E a segunda) corresponde à interseção desses eventos independentes (uma vez que as bolas retiradas são repostas). Logo,devemos multiplicar as respectivas probabilidades. Como as bolas selecionadas são repostas, a probabilidade de retirar a primeira bola azul é igual à de tirar a segunda bola azul, então, temos:
Gabarito: Errado.

Item. 18. (Cebraspe/2021 - MJ/SP) Em um jogo de cara e coroa disputado com uma moeda não viciada, um pai criou a seguinte regra, visando aumentar as chances de sua filha vencer a disputa: a moeda seria lançada certa quantidade de vezes, n, definida previamente, e o pai só sairia vencedor caso a moeda apontasse cara em todos os n lançamentos. Tendo como referência essa situação hipotética, julgue o item que se segue.
Se n = 2, a probabilidade de vitória da filha será de 75%.

Comentários:

A vitória da filha pode ser calculada como o complementar da vitória do pai:

P(filha) = 1 — P(pai)

Por sua vez, a vitória do pai corresponde à probabilidade de obter CARA nos n = 2
lançamentos, isto é, à interseção de 2 eventos independentes, dada pelo produto das probabilidades:
z x 111

P(pai) =-x-=-= 0,25

Logo, a vitória da filha é:

P(filhd) = 1 - 0,25 = 0,75 = 75%

Gabarito: Certo

Item. 19. (Cebraspe/2021 - MJ/SP) Em um jogo de cara e coroa disputado com uma moeda não viciada, um pai criou a seguinte regra, visando aumentar as chances de sua filha vencer a disputa: a moeda seria lançada certa quantidade de vezes, n, definida previamente, e o pai só sairia vencedor caso a moeda apontasse cara em todos os n lançamentos. Tendo como referência essa situação hipotética, julgue o item que se segue.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

10 é o menor número de lançamentos que asseguraria à filha chance de vencer de pelo menos 95%.

Comentários:

Nessa questão, também vamos calcular a vitória da filha como complementar da vitória do pai. Para que a probabilidade de a filha vencer seja de pelo menos 95%, a probabilidade de o pai vencer deve ser menor que100% - 95% = 5%.

A probabilidade de o pai ganhar em n lançamentos corresponde à probabilidade de obter CARA nos n lançamentos, isto é, à interseção de n eventos independentes (produto das probabilidades):
1 1 1 /l\n

(2 X 2 X 2 X U

í nvezes
Vejamos qual é o menor valor de n para o qual essa probabilidade é menor que 5%:

* Para n = 1, temos Q) = | = 50%

* Para n = 2, temos Q) = 4 = 25%

* Para n = 3, temos Q) = ^ = 12,5%

/1\4 1

* Para n = 4, temos (-) = — = 6,25%

\2/ 16

* Para n = 5, temos Q) =^=3,125%

Portanto, 5 (e não 10) é o menor número de lançamentos para o qual a probabilidade de o pai vencer é inferior a 5% e, portanto, a probabilidade de a filha vencer é superior a 95%.
Gabarito: Errado

Item. 20. (Cebraspe/2022 - PC/PB) Na enfermaria de um hospital estavam internados 32
pacientes. Destes,

8 apresentavam pneumonia, 6 tinham diagnóstico de asma, 10 estavam com gripe, 6 tinham câncer no pulmão e os demais aguardavam atendimento. Coincidentemente, em cada grupo a quantidade de homens e mulheres era a mesma. Considerando essa situação hipotética, assinale a opção correta.
a) Foram escolhidos aleatoriamente 3 pacientes dentre aqueles com gripe para responder uma pesquisa. Aprobabilidade de todos eles serem mulheres é de 50%.

b) Se selecionado um paciente aleatoriamente para a realização de um exame, a probabilidade de ele estar com asma ou ser um dos que têm câncer no pulmão é de 18,75%.
c) 4 pacientes serão escolhidos aleatoriamente para receber uma visita especial. A
chance deste grupo ser composto por um homem com pneumonia, uma mulher com asma, uma mulher com gripe e um homem que tem câncer no pulmão é de 0,12%.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

d) Sabe-se que a proporção de diagnóstico de asma nos pacientes que chegam ao hospital é a mesma daquela dos pacientes já diagnosticados que estavam na enfermaria. Assim, a probabilidade dos dois pacientes que aguardam atendimento receberem diagnóstico de asma é de 20%.
e) A cada dia, durante os próximos 4 dias, um paciente será escolhido aleatoriamente para receber uma sobremesa especial no almoço. A chance dos quatro pacientes sorteados serem mulheres é de 6,25%.
Comentários:

Essa questão informa que há 32 pacientes, dos quais 8 estavam internados com pneumonia, 6 com asma, 10com gripe, 6 com câncer e os outros 2 aguardavam atendimento. Ademais, a questão informa que, em cada grupo, a quantidade de homens e mulheres é a mesma.
As alternativas pedem para calcularmos as probabilidades, seguindo a definição clássica, exceto as alternativas D e E, que exigem conhecimento a respeito da interseção de eventos independentes. Então vamos primeiro a elas.
A alternativa D pede a probabilidade de os 2 pacientes aguardando atendimento terem asma, sabendo que as proporções dos que aguardam o atendimento é a mesma dos que estão internados. Dos30 internados, 6
têm asma, logo a probabilidade de um paciente ter asma é:

Que é 20%, como indicado na alternativa. No entanto, a probabilidade de os
2 pacientes terem asma corresponde ao produto das probabilidades (interseção de eventos independentes):
P = 0,2 x 0,2 = 0,04 = 4%

Logo, a alternativa D está incorreta.

Já a alternativa E afirma que ao longo dos próximos 4 dias 1 pessoa será escolhida e pede a probabilidade de todas as 4 serem mulheres. A probabilidade de uma mulher ser sorteada em um dia é de 50% = 0,5, uma vez que metade dos pacientes são mulheres. E a probabilidade de 4 serem mulheres é o produto das probabilidades (interseção de eventos independentes):
P = 0,5 x 0,5 x 0,5 x 0,5 = 0,0625 = 6,25%

Portanto, a alternativa E está correta.

Agora vejamos as demais alternativas. A alternativa A informa que 3 pacientes serão escolhidos, dentre os
10 pacientes com gripe, e pede a probabilidade de todos eles serem mulheres. Essa probabilidade é a razão entre a combinação de 3 pacientes, dentre as 5 mulheres com gripe (eventos favoráveis), e a combinação de3 pacientes dentre todos os 10 pacientes com gripe (todos os eventos possíveis):

p eventos favoráveis C53
eventos possíveis C10 3

Vamos calcular as combinações em separado:

5! 5x4x3! 5x4

Cs'3 ~ (5 - 3)! x 3! 2! x 3! 2 " 5 x 2 " 10

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

10! 10x9x8x7! 10x9x8

— -—-—- = 10 x 3 x 4 = 120

E a razão é:

10,3 (10 — 3)! x 3! 7! x 3!

3x2x1

p — ^*5,3 _
10 1

r

L10,3

120 ~ 12

Que é diferente de 50% e por isso a alternativa A está incorreta.

Em relação à alternativa B, a probabilidade de um paciente estar com asma ou ter câncer é a razão entre o número de pacientes com asma ou com câncer (6 + 6 = 12) e o número total de pacientes (32):
P = H = | = °'375 = 37'5%

Que é diferente de 18,75%, logo a alternativa B está errada.

Por fim, a alternativa C afirma que 4 pacientes serão escolhidos e pede a probabilidade de que sejam escolhidos um homem com pneumonia, uma mulher com asma, uma mulher com gripe e um homem com câncer. Sabendo que há 4 homens com pneumonia, 3 mulheres com asma, 5 mulheres com gripe e 3 homens com câncer de pulmão, o número de eventos favoráveis é o produto (princípio multiplicativo):
eventos favoráveis = 4x3x5x3 = 180

E o total de eventos possíveis corresponde à combinação de 4 pacientes, dentre todos os 32:

eventos possíveis = C3íi = & _ 4), x 4, =

32! 32 x 31 x 30 x 29 x 28!

4 1 n

32 x 31 x 30 x 29 Xx 31 x^0x29

eventos possíveis = —-—-—-—-— = —;— = 4x31x 10 x 29 = 35960

4x3x2x1 Xx/x/xl

E a probabilidade é a razão:

Logo, a alternativa C está incorreta.

Gabarito: E

P = 3596ÕS0'005 = a5%

Item. 21. (Cebraspe/2022 - DPE/RO) A confiabilidade mensura a capacidade que um sistema,
produto ou serviço possui de se comportar da forma esperada, podendo estar associada a diversas áreas de gestão,inclusive gestão da qualidade. As informações apresentadas na seguinte tabela referem-se a determinado processo produtivo dividido em 3 etapas A, B e C.
Etapa
A
B
C

Confiabilidade
0,95

0,80

0,50

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com base nas informações apresentadas, assinale a opção que mostra a confiabilidade desse processo produtivo.
a) 0,95

b) 0,50

c) 0,45

d) 0,38

e) 0,80

Comentários:

Para que todo o processo se comporte bem, é necessário que todas as etapas se comportem bem. Portanto,a probabilidade de que o processo se comporte bem (confiabilidade) corresponde à interseção dos eventos.Considerando que os eventos são independentes, a probabilidade da interseção é o produto das probabilidades:
P(A n B n C) = P(A) x P(B) x P(C) = 0,95 x 0,80 x 0,50 = 0,38

Gabarito: D

Item. 22. (Cebraspe/2021 - ALE/CE) A probabilidade de um jogador acertar determinado alvo em cada rodada de um jogo é igual a 0,6. Na tabela abaixo, por exemplo, em determinada partida, esse jogador acertou o alvo pela primeira vez na quarta rodada.
rodiada

1 2 3 4 5

X X X / /

6 7 8

X / X

9 10

X /

Caso esse mesmo jogador inicie outra partida, considerando-se que haja independência mútua entre duas rodadas, a probabilidade de ele acertar o alvo, pela primeira vez, na terceira rodada é igual a a) 0,096
b) 0,16

c) 0,33

d) 0,60

e) 0,76

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A questão informa a probabilidade de um jogador acertar o alvo em cada rodada e pede a probabilidade de ele acertar pela primeira vez na 3- rodada. Para isso, é necessário que o jogador erre na 1- e na rodada,e acerte na 3?.

Sabendo que são eventos independentes, a probabilidade da interseção corresponde ao produto:

p — pçerro^ x P(erro) x P(acerto)

O enunciado informa que a probabilidade de acerto é P(acerto) = 0,6. Sabendo que a probabilidade do erro é complementar, temos:
Assim, a probabilidade buscada é:

Gabarito: A

P(erro) = 1 — P(acerto) = 1 — 0,6 = 0,4

P = 0,4 x 0,4 x 0,6 = 0,096

Item. 23. (Cebraspe/2021 - COREN/SE) Um ambulatório funciona diariamente nos períodos matutino e vespertino, sendo registradas, diariamente, as ocorrências de incidentes durante o seu funcionamento.Para essa situação hipotética, considere que

A = "ocorrência diária de incidentes no período matutino" e
B = "ocorrência diária de incidentes no período vespertino".

Se A e B forem dois eventos aleatórios independentes cujas probabilidades sejam P(A) = 0,5 e P(B) =
0,5,
então a probabilidade de ocorrência diária de incidentes nesse ambulatório, representada como o eventoA U B, será igual a a) l b) 0
c) 0,25

d) 0,75

Comentários:

O enunciado informa a probabilidade dos eventos A e B, afirma que são eventos independentes e pede a probabilidade da união:
P(A U B) = P(A) + P(B) - P(A n B)

Sendo os eventos independentes, a probabilidade da interseção é o produto das probabilidades:

P(A n B) = P(A) x P(B) = 0,5 x 0,5 = 0,25

Logo, a probabilidade da união é dada por:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

P(A UB) = 0,5 + 0,5 - 0,25 = 0,75

Gabarito: D

Item. 24. (Cebraspe/2022 - TELEBRAS) Julgue o item que se segue, a respeito de contagem,
probabilidade e estatística.
Considere que seja preciso comprar duas peças pi e p2 para um projeto de satélite.
Considere ainda que a probabilidade de ter a peça pi no estoque na distribuidora é de 1/3 e a probabilidade de ter a peça p2 no estoque na mesma distribuidora é de 3/5. Nesse caso, a probabilidade de que pelo menos uma das peças esteja no estoque é de 11/15.
Comentários:

A probabilidade de haver pelo menos uma das peças corresponde à união dos eventos,
cuja probabilidade é calculada como:
PQ4i U Â2) = PUO + P(X2) - PÇÁ! n A2)

Em que PÇAJ = | e P(A₂) = |

Considerando que esses eventos são independentes, a probabilidade da interseção é o produto:

PQ4i D A2) — P(Ai) x PÇAJ — g x — 5

Logo, a probabilidade da união é dada por:

Gabarito: Certo

5 9 3 11

15 + 15 _ 15 15

Item. 25. (Cebraspe/2021 - ADAPAR) A tabela a seguir apresenta a porcentagem de lotes de carnes produzidos por cada estado da região Sul do Brasil em 2019, em relação ao total dos lotes produzidos nessa região durante esse período.
Estado da Região Sul
Paraná

Rio Grande do Sul
Santa Catarina porcentagem de lotes de carne produzidos50%

42%

8%

Por razões sanitárias, nesse mesmo ano, foram descartados 2,5% dos lotes produzidos no Paraná, 3%
dos lotes produzidos no Rio Grande do Sul e 3,5% dos lotes produzidos em Santa Catarina.
Nessa situação hipotética, a probabilidade de se selecionar aleatoriamente um lote de carne produzido nessa região que tenha sido descartado no referido ano é de
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 0,0168

b) 0,0279

c) 0,09

d) 0,91

e) 0,9721

Comentários:

Essa questão trabalha com o Teorema da Probabilidade Total, em que desejamos calcular a probabilidade total do evento (no caso, do descarte), conhecendo as probabilidades condicionais desse evento, isto é, a probabilidade do descarte de cada Estado:
P(£>) = P(D|X) x P(A) + P(£>|B) x P(B) + P(£>|C) x P(C)

Em que as probabilidades condicionais do descarte para cada Estado são:

* Paraná: P(£>M) = 2,5% = 0,025

* Rio Grande do Sul: P(D|£?) = 3% = 0,03

* Santa Catarina: P(D|C) = 3,5% = 0,035

E as probabilidades associadas a cada Estado são:

* Paraná: PQ4) = 50% = 0,5

* Rio Grande do Sul: P(B) = 42% = 0,42

* Santa Catarina: P(C) = 8% = 0,08

Substituindo esses valores na fórmula da probabilidade total, temos:

P(£») = 0,025 x 0,5 + 0,03 x 0,42 + 0,035 x 0,08

P(£>) = 0,0125 + 0,0126 + 0,0028 = 0,0279

Gabarito: B

Item. 26. (Cebraspe/2019 - TJ/AM) Se Carlos estiver presente na aula ministrada pela professora Paula, a probabilidade de ele aprender o conteúdo abordado é de 80%; se ele estiver ausente,essa probabilidade cai para 0%. Em 25% das aulas da professora Paula, Carlos está ausente.
Com relação a essa situação hipotética, julgue o item seguinte.

A probabilidade de Carlos não aprender o conteúdo ministrado pela professora Paula é inferior a
25%.

Comentários:

O enunciado informa que:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

* Se Carlos estiver presente na aula, a probabilidade de aprender o conteúdo é de 80%: P(Ap\P')
=

0,8, em que Ap corresponde ao aprendizado e P corresponde à presença;

* Se Carlos estiver ausente, a probabilidade de aprender é 0%: P(Ap\Py) = 0, em que P
corresponde à não presença, isto é, à ausência;
* Carlos está ausente em 25%: P(P) = 0,25.

Para calcular a probabilidade de Carlos não aprender o conteúdo, utilizamos a fórmula da ProbabilidadeTotal:

P(Ãp) = P(Ãp\P) x P(P) + P(Ãp\P) x P(P)

Sabemos que P(Ap\P) = 0,8, logo o seu complementar é:

P(Ãp\P) = 1 - P(Ap\P) = 1 - 0,8 = 0,2

Sabemos ainda que P(P) = 0,25, logo o seu complementar é:

P(P) = 1 - P(P) = 1 - 0,25 = 0,75

Por fim, sabemos que P(Ap\P~) = 0, logo o seu complementar é:

P(Ãp\P) = 1 - PQ4p|P) = 1-0 = 1

Substituindo esses valores na fórmula da Probabilidade Total, temos:

P(Ãp) = 0,2 x 0,75 + 1 x 0,25 = 0,15 + 0,25 = 0,4

Ou seja, a probabilidade de Carlos não aprender é superior a 25%.

Gabarito: Errado

Item. 27. (Cebraspe/2019 - TJ/AM) Se Carlos estiver presente na aula ministrada pela professora Paula, a probabilidade de ele aprender o conteúdo abordado é de 80%; se ele estiver ausente,essa probabilidade cai para 0%. Em 25% das aulas da professora Paula, Carlos está ausente.
Com relação a essa situação hipotética, julgue o item seguinte.

O evento "Carlos não aprendeu o conteúdo ministrado pela professora Paula, dado que estava ausente na aula." é evento certo, isto é, a probabilidade de esse evento ocorrer é igual a 1.
Comentários:

O enunciado informa que se Carlos estiver ausente, a probabilidade de aprender é 0%,
o que podemos representar porP(zlp|P) = 0, em quezlp corresponde ao aprendizado e P corresponde à não presença, isto é, à ausência. Assim, o seu complementar é:
P(Ãp\P) = 1 - PQ4p|P) = 1-0 = 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ou seja, a probabilidade de Carlos não aprender o conteúdo, dado que estava ausente é igual a 1. Assim,esse evento é chamado evento certo.

Gabarito: Certo.

Item. 28. (Cebraspe/2022 - PETROBRAS) O item a seguir é apresentada uma situação hipotética seguida de uma assertiva a ser julgada a respeito de probabilidade e estatística.
Uma empresa faz toda a produção do seu único produto em duas fábricas distintas A e
B, que produzem,
respectivamente, 75% e 25% da produção total. Na fábrica A, 5% da produção passa por um processo de controle de qualidade, enquanto, na fábrica B, a produção que passa pelo controle de qualidade é de 10%.Nessa situação, escolhendo-se um produto ao acaso dentre os que passaram por controle de qualidade, após todas as etapas da produção, a probabilidade desse item ter sido produzido na fábrica B é inferior a 30%.
Comentários:

Essa questão trabalha com o Teorema de Bayes, em que conhecemos as probabilidades condicionais doControle de qualidade para as fábricas A e B [P(C|Â) e P(C|B)j; e precisamos da probabilidade condicional da fábrica B, sabendo que a peça passou pelo Controle de qualidade [P(B|C)], ou seja,há uma inversão dos eventos a priori e a posteriori.
A fórmula de Bayes é dada por2:

O enunciado informa que:

P(C|B)xP(B)

" P(C|2l)xP(Â) + P(C|B)xP(B)

* A fábrica A é responsável por 75% da produção: PQ4) = 0,75;

* A fábrica B é responsável por 25% da produção: P(B) = 0,25;

* 5% da produção da fábrica A passa pelo controle de qualidade: P(C|>1) = 0,05

* 10% da produção da fábrica B passa pelo controle de qualidade: P(C|B) = 0,1

Logo, a probabilidade de um item ter vindo da fábrica B, dado que passou pelo controle de qualidade é:
P(B|C) =

Que é superior a 30%

Gabarito: Errado

0,1 x 0,25

0,05 x 0,75 + 0,1 x 0,25

0,025

0,0375 + 0,025

0,025

0,0625

- = 40%

2 A fórmula do Teorema de Bayes decorre da fórmula da probabilidade condicional, em que o numerador P(B n C) é dado pelo Teorema da Multiplicação e o denominador P(C) é dado pelo Teorema da Probabilidade Total:
P(B|C) =

P(B n C)

P(C)

P(C|S) xP(B)
P(C|4) x P(4) + P(C|B) x P(B)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Aula

Item. 29. (Cebraspe/2022 - TELEBRAS) Julgue o item que se segue, a respeito de contagem,
probabilidade e estatística.
Considere que o lançamento de um satélite no centro de lançamento de Alcântara esteja previsto para o dia
5 de abril, e que, naquela região, chove apenas 10 dias durante esse mês.
Considere ainda que a meteorologia prevê chuva para o dia do lançamento e que, quando efetivamente chove, a meteorologia prevê corretamente a chuva em 90% das vezes, e, quando não chove, ela prevê incorretamente chuva 10%das vezes. Nessa situação, a probabilidade de chover no dia do lançamento do satélite é inferior a
80%.

Comentários:

Aqui, essa questão também trabalha com o Teorema de Bayes, pois o enunciado informa a probabilidade de a meteorologia prever chuva, nos dias de chuva e de não chuva, e pede a probabilidade de chover, dado que a meteorologia previu chuva, caracterizando a inversão dos eventos a priori e a posteriori.
Na fórmula, vamos representar a previsão de chuva como Pc, a ocorrência de chuva como Cea não ocorrência de chuva como C:
P(Pc|C) xP(C)

P(ClPc) p(pc|C) x p(c) + p(pc|c) x P(C)

O item informa que:

* Quando chove, a meteorologia prevê chuva em 90% das vezes: P(Pc|C) = 0,9

* Quando não chove, a meteorologia prevê chuva em 10% das vezes: P(Pc|C) = 0,1

* Nessa região, chove 10 dias no mês de abril (com 30 dias).
Logo a probabilidade de chuva é:

E a probabilidade de não chover é complementar:

Substituindo esses dados na fórmula de Bayes, temos:

P(C|Pc) =

0,9 xi
0,9 x | + 0,1 x |

Multiplicando todos os termos por 3:

Que é superior a 80%.

Gabarito: Errado

0,0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)
www. estra tegiaconcursos. com. br

Item. 30. (Cebraspe/2021 - SEDUC) O próximo item apresenta uma situação hipotética a ser julgada, acerca de problemas matemáticos envolvendo situações em uma escola.
O professor de biologia leva uma turma de alunos para uma viagem de pesquisa. A
manhã do dia de saída para a viagem encontra-se nublada no destino da viagem, e sabe-se que manhãs nubladas acontecem em40% dos dias ali. Além disso, nesse local, 50% dos dias em que chove começam nublados, contudo, no mês em que acontece a viagem, costuma chover pouco — exatamente 20% dos dias são chuvosos. Nessa situação hipotética, a chance de chover durante o dia da viagem é de 12,5%.
Comentários:

Essa questão também trabalha com o Teorema de Bayes, caracterizada pela inversão dos eventos a priori e a posteriori. Isso porque o enunciado informa que 50% dos dias de chuva começam nublados, que corresponde à probabilidade de o dia ter começado nublado, dado que choveu; e pede a probabilidade de chover, dado que o dia começou nublado. Vamos representar o dia nublado por N e a chuva por C. O item informa que:
* 50% dos dias de chuva começam nublados: P(7V|C) = 0,5

* As manhãs nubladas acontecem em 40% dos dias: P(N) = 0,4

* 20% dos dias são chuvosos: P(C) = 0,2

A diferença dessa questão em relação às anteriores é que não precisamos utilizar o Teorema daProbabilidade Total para calcular o denominador, pois o enunciado já forneceu a probabilidade de o dia amanhecer nublado:
( . = P(C n = P(N|C)XP(C)

1 1 } PW P(7V|C) x P(C) + P(7V|C) x P(C)

P(C|N) =

Que é diferente de 12,5%.

Gabarito: Errado

P(2V|C) x P(C)

W)

0,5 x 0,2

Õ4

Item. 31. (Cebraspe/2018 - ABIN) Considerando os conceitos associados a probabilidade e estatística, julgue o item.
Considere que as bolas de uma urna tenham sido divididas em duas caixas, sendo que a caixa I ficou com 3bolas brancas e 1 bola preta, enquanto a caixa II ficou com 3 bolas brancas e 3
bolas pretas. Em seguida, uma caixa foi escolhida e dela foi sorteada uma bola. Sabendo que a cor da bola sorteada era branca, a probabilidade de ter vindo da caixa I é de 3/8.
Comentários:

Essa questão pode ser resolvida pela fórmula de Bayes, pois são fornecidos elementos para calcularmos a probabilidade da cor da bola (branca ou preta), a partir da caixa (I ou II) e indaga-se a respeito da
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

probabilidade da caixa, a partir da cor da bola constatada. Ou seja, há uma inversão dos eventos a priori(anterior) e a posteriori (posterior).

Mais precisamente, indaga-se sobre a probabilidade de a bola sorteada ter vindo da caixa I, sabendo que ela é branca, que podemos representar por P(7|77).
Para isso, o enunciado informa que:

* Na caixa I, há 3 bolas brancas e 1 bola preta, ou seja, há 3 bolas brancas e 4 bolas no total. Portanto,dado que a bola saiu da caixa I, a probabilidade de ela ser branca é P(7?|7) =

* Na caixa II, há 3 bolas brancas e 3 bolas pretas, ou seja, há 3 bolas brancas e 6 bolas no total. Portanto,
3 1

dado que a bola saiu da caixa II, a probabilidade de ela ser branca é P(7?|77) = - =

6 2

* Uma caixa foi escolhida aleatoriamente, logo, a probabilidade de ter sido a caixa I é P(7) =
- e de ter sido a caixa II é PÇII) = j.
Substituindo essas informações na fórmula de Bayes, temos:

P(7?|7) x P(7)

P(B\I)x P(P) + P(B\Il)x P(II)

3 1 3 3

Gabarito: Errado.

P1 x(711|Bj)2=---------- - —2--2 = —-— =2—.

4x2 + 2X2 8+ 4 "ã-

z , A 3 8 3

p('|B) = ãx5 = 5

-—3 | 3

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Definições de Probabilidade

Item. 1. (Cebraspe/2022 - DPE/RO) Um lote contendo 100 componentes foi testado por
Item. 1.000 horas. Nesse período, 4 componentes falharam. A partir das informações anteriores, assinale a opção que corresponde à taxa de falha do teste em questão.
a) 20%

b) 8%

c) 4%

d) 16%

e) 10%

Item. 2. (Cebraspe/2020 - ME) O setor de gestão de pessoas de determinada empresa realiza regularmente a análise de pedidos de férias e de licenças dos seus funcionários. Os pedidos são feitos em processos, em que o funcionário solicita apenas férias, apenas licença ou ambos (férias e licença).Em determinado dia,
30 processos foram analisados, nos quais constavam 15 pedidos de férias e 23 pedidos de licenças.
Com base nessa situação hipotética, julgue o item que se segue.
Se todos os processos foram analisados individualmente nesse dia, então a probabilidade de um processo
Item. 3. (Cebraspe/2021 - CBM/AL) Os professores João, Carlos e Luis ministrarão um curso de primeiros socorros em que serão ensinados os seguintes procedimentos.
I. fazer massagem cardíaca

II. desengasgar

III. estancar sangramentos

IV. amenizar queimaduras

V. desafogar

VI. cuidar de fraturas

Cada professor ensinará exatamente dois procedimentos, e o mesmo professor que ensinar o procedimento desafogar ensinará também o procedimento desengasgar. Considerando essa situação hipotética, julgue o próximo item.
Selecionando-se ao acaso o professor que ensinará o procedimento fazer massagem cardíaca, a probabilidade de Luis ser o escolhido é maior do que 40%.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 4. (Cebraspe/2021 - CBM/AL) Os professores João, Carlos e Luis ministrarão um curso de primeiros socorros em que serão ensinados os seguintes procedimentos.
I. fazer massagem cardíaca

II. desengasgar

III. estancar sangramentos

IV. amenizar queimaduras

V. desafogar

VI. cuidar de fraturas

Cada professor ensinará exatamente dois procedimentos, e o mesmo professor que ensinar o procedimento desafogar ensinará também o procedimento desengasgar. Considerando essa situação hipotética, julgue o próximo item.
Se Carlos ensinar o procedimento cuidar de fraturas, então, selecionando-se ao acaso os professores que ensinarão os outros procedimentos, a chance de que João ensine o procedimento desafogar é maior do que45%.

Item. 5. (Cebraspe/2021 - CBM/AL) Em determinado dia, em uma região atendida por uma unidade do corpo de bombeiros, ocorreram 16 acidentes, que resultaram em 48 vítimas, socorridas pelos bombeiros nos próprios locais de acidente. Entre essas vítimas, 4 vieram a óbito no momento do atendimento, e as demais sobreviveram.
Com base nessa situação hipotética, julgue o item a seguir.

Considere que os nomes das 48 vítimas tenham sido anotados individualmente em rascunhos pelos bombeiros que as atenderam nos locais de acidente. Considere também que, ao final do dia, determinado bombeiro tenha sido responsável por registrar em relatório o nome de cada vítima,escolhendo cada nome aleatoriamente a partir desses rascunhos. Considere, por fim, que este bombeiro tenha registrado os nomes de metade das vítimas e que todas essas vítimas já registradas sejam sobreviventes. Nesse caso, a probabilidade de o vigésimo quinto registro deste bombeiro ser de uma vítima que veio a óbito é igual a -.
Item. 6. (Cebraspe/2018 - PGE/PE) A União tem, hoje, 138 estatais sob sua gestão,
entre elas o Banco do
Brasil S.A., a PETROBRAS e a CAIXA. Dessas 138, somente três devem permanecer sob a gestão da União;
as demais serão privatizadas.

Considerando essa afirmação, julgue o próximo item.

Supondo-se que a PETROBRAS e o Banco do Brasil S.A. sejam estatais já escolhidas para permanecerem sob a gestão da União, se a terceira estatal for escolhida ao acaso, a chance de aCAIXA ser privatizada será superior a 99%.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 7. (Cebraspe/2018 - PF) Em um aeroporto, 30 passageiros que desembarcaram de determinado voo e que estiveram nos países A, B ou C, nos quais ocorre uma epidemia infecciosa, foram selecionados para ser examinados. Constatou-se que exatamente 25 dos passageiros selecionados estiveram em A ou em B,nenhum desses 25 passageiros esteve em C e 6 desses 25 passageiros estiveram em A e em B. Com referência a essa situação hipotética, julgue o item que se segue.
Se 2 dos 30 passageiros selecionados forem escolhidos ao acaso, então a probabilidade de esses 2passageiros terem estado em 2 desses países é inferior a 1/30.

Item. 8. (Cebraspe/2018 - PF) Os indivíduos Sl, S2, S3 e S4, suspeitos da prática de um ilícito penal, foram interrogados, isoladamente, nessa mesma ordem. No depoimento, com relação à responsabilização pela prática do ilícito, Sl disse que S2 mentiria; S2 disse que S3 mentiria; S3 disse queS4 mentiria. A partir dessa situação, julgue o item a seguir.
Considerando que a conclusão ao final do interrogatório tenha sido a de que apenas dois deles mentiram,mas que não fora possível identificá-los, escolhendo-se ao acaso dois entre os quatro para novos depoimentos, a probabilidade de apenas um deles ter mentido no primeiro interrogatório é superior a0,5.

Item. 9. (Cebraspe/2017 - PM-MA) Determinado laboratório de análises clínicas está sendo investigado por emitir laudos falsos de um exame constituído por 7 indicadores, correspondentes à concentração de 4compostos na corrente sanguínea, obtidos da seguinte forma: uma medição da concentração de cada um dos compostos A, B, C e D, e 3 medições, por 3 diferentes técnicas, da concentração do composto E.Os laudos verdadeiros de 7 pacientes (chamados pacientes-fonte), com prenomes distintos, entre elesAmanda, Bárbara, Carlos e Daniel, eram usados para compor laudos falsos para os demais pacientes.
Para dificultar a ação da autoridade policial, na montagem de um laudo falso, o laboratório tomava o cuidado de, no conjunto de 7 medições que constituíam cada laudo falsificado, usar apenas uma medição de cada paciente-fonte, ou seja, de nunca usar 2 ou mais medições de um mesmo paciente-fonte.
Com referência a essa situação hipotética, julgue o item seguinte.

Caso o laboratório escolhesse aleatoriamente, entre os dados dos 7
pacientes-fonte, aqueles que seriam usados nas medições referentes ao composto E, a probabilidade de serem usados os dados de Amanda,Bárbara e Carlos seria inferior a 3%.

Item. 10. (Cebraspe/2019 - Prefeitura de São Cristóvão/SE) A sorte de ganhar ou perder,
num jogo de azar,
não depende da habilidade do jogador, mas exclusivamente das probabilidades dos resultados. Um dos jogos mais populares no Brasil é a Mega Sena, que funciona da seguinte forma: de 60bolas, numeradas de 1 a 60, dentro de um globo, são sorteadas seis bolas. À medida que uma bola é retirada, ela não volta para dentro do globo. O jogador pode apostar de 6 a 15 números distintos por volante e receberá o prêmio se acertar os seis números sorteados. Também são premiados os acertadores de 5 números ou de 4números. A partir dessas informações, julgue o item que se segue.

A probabilidade de a primeira bola sorteada ser um número múltiplo de 8 é de 10%.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 11. (Cebraspe/2019 - Prefeitura de São Cristóvão/SE) A sorte de ganhar ou perder,
num jogo de azar,
não depende da habilidade do jogador, mas exclusivamente das probabilidades dos resultados. Um dos jogos mais populares no Brasil é a Mega Sena, que funciona da seguinte forma: de 60bolas, numeradas de 1 a 60, dentro de um globo, são sorteadas seis bolas. À medida que uma bola é retirada, ela não volta para dentro do globo. O jogador pode apostar de 6 a 15 números distintos por volante e receberá o prêmio se acertar os seis números sorteados. Também são premiados os acertadores de 5 números ou de 4números.

A partir dessas informações, julgue o item que se segue.

A probabilidade de se acertar os 6 números sorteados na Mega Sena com a aposta de um volante com 6números é igual a 541/601.

Item. 12. (Cebraspe/2019 - Prefeitura de São Cristóvão/SE) A sorte de ganhar ou perder,
num jogo de azar,
não depende da habilidade do jogador, mas exclusivamente das probabilidades dos resultados. Um dos jogos mais populares no Brasil é a Mega Sena, que funciona da seguinte forma: de 60bolas, numeradas de 1 a 60, dentro de um globo, são sorteadas seis bolas. À medida que uma bola é retirada, ela não volta para dentro do globo. O jogador pode apostar de 6 a 15 números distintos por volante e receberá o prêmio se acertar os seis números sorteados. Também são premiados os acertadores de 5 números ou de 4números.

A partir dessas informações, julgue o item que se segue.

Se p for a probabilidade de se acertar na Mega Sena com a aposta de um volante com
6 números distintos,
então, apostando-se 8 números, a probabilidade de acerto será igual a 28p.

Item. 13. (Cebraspe/2018 - BNB) Um tabuleiro quadrado e quadriculado, semelhante a um tabuleiro de xadrez, com 12 linhas e 12 colunas, e, portanto, com 12 x 12 = 144 quadradinhos pintados: 54, na cor azul;30, na cor marrom; 40, na cor amarela; e 20, na cor verde. A cada quadradinho é associado um cartão com dois números, que indicam a posição do quadradinho no tabuleiro; o primeiro número corresponde ao número da linha, e o segundo corresponde ao número da coluna. Por exemplo, o cartão com os números5,10 corresponde ao quadradinho posicionado na linha 5 e na coluna 10. Esses cartões estão em uma urna,da qual podem ser retirados aleatoriamente.

A respeito desse tabuleiro e desses cartões, julgue o item a seguir.

A probabilidade de retirar dessa caixa, de maneira aleatória, um cartão correspondente a um quadrado pintado na cor azul é superior a 1/3.
Item. 14. (Cebraspe/2021 - SEED/PR) A tabela a seguir mostra o valor unitário por ação de determinada empresa na bolsa de valores ao longo de dez dias úteis.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Dia

Valor da abertura (em R$)
100,00

90,00

110,00

121,00

120,00

144,00

160,00

194,00

180,00

160,00

Valor do fechamento (em R$)
90,00

110,00

121,00

120,00

144,00

160,00

194,00

180,00

160,00

140,00

Caso uma pessoa compre ações dessa empresa pelo valor de abertura (VA) e faça a revenda total dessas ações, ao final do mesmo dia, pelo valor de fechamento (VF), o lucro ou o prejuízo percentual diário (LP)poderá ser calculado pela seguinte fórmula, de modo que LP > 0 indica lucro e LP < 0 indica prejuízo.
VF — VA

Ainda considerando as informações do texto 6A3-I, suponha que uma pessoa tenha decidido investir nas ações daquela empresa em um único dia entre aqueles 10 dias úteis. Suponha, também, que a escolha da data do investimento tenha sido tomada aleatoriamente e que tenha ocorrido antes do primeiro dia listado na tabela. Nessas condições, a probabilidade de essa pessoa ter um lucro superior a 20% é de a) 10%
b) 20%

c) 30%

d) 40%

e) 50%

Item. 15. (Cebraspe/2022 - PC/PB)

Residência
João Pessoa

Outras cidades da Paraíba
Outros Estados

Homem

Mulher

A tabela acima mostra os resultados de uma pesquisa feita em um Shopping Center em João Pessoa sobre o local de residência de seus frequentadores, na qual foram entrevistadas 240 pessoas. Todas as fichas das240 pessoas entrevistadas foram colocadas em um fichário. Nessa situação, se uma das fichas for retirada aleatoriamente do fichário, a probabilidade da ficha corresponder a uma mulher residente na Paraíba é a) inferior a 0,35
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

b) superior a 0,36 e inferior a 0,42

c) superior a 0,56

d) superior a 0,43 e inferior a 0,49

e) superior a 0,50 e inferior a 0,55

Item. 16. (Cebraspe/2022 - PETROBRAS) O item a seguir é apresentada uma situação hipotética seguida de uma assertiva a ser julgada a respeito de probabilidade e estatística.
De 10 contêineres, numerados de 1 a 10, deseja-se inspecionar ao acaso três deles.
Sabendo que existem cargas irregulares nos contêineres 2, 5 e 7 e que a probabilidade de escolherem qualquer trio de contêineres é a mesma, então a probabilidade de a equipe de inspeção escolher os contêineres problemáticos é superior a 1%.
Item. 17. (Cebraspe/2021 - PC/DF) Luís, Fernando, Paulo, Carlos e Marcos, suspeitos de terem praticado determinado crime, foram convocados para depor. Na delegacia, ocorreram os eventos descritos a seguir.
* Marcos e Carlos preferiram ficar em silêncio.

* Fernando afirmou que o culpado era Marcos ou Carlos.

* Luís afirmou que o culpado era Fernando ou Carlos.

* Paulo afirmou que o culpado era Marcos ou Fernando.

Considerando que exatamente dois deles são culpados e que, em 2021, todos eles terão mais de quinze anos de idade, julgue o item a seguir.
Se dois desses acusados forem aleatoriamente escolhidos para uma acareação, a probabilidade de serem os dois culpados é igual a 1/10.
Item. 18. (Cebraspe/2021 - PM/TO) Cinco pessoas (Arnaldo, Bernardo, Cláudio,
Diógenes e Ernesto),
suspeitas de determinada contravenção, são chamadas para acareação por uma autoridade policial.Exatamente dois deles são culpados, e as seguintes declarações foram feitas durante o depoimento:

I. Arnaldo disse que os culpados não foram Ernesto nem Bernardo;

II. Bernardo disse que os culpados não foram Arnaldo nem Cláudio;

III. Cláudio disse que os culpados não foram Bernardo nem Diógenes.

Se 3 pessoas forem aleatoriamente escolhidas entre os 5 suspeitos, então a probabilidade de os dois culpados serem escolhidos será igual a a) 1/10
b) 3/10

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) 2/15

d) 13/20

e) 11/15

Item. 19. (Cebraspe/2022 - UNB) Em uma viagem de turismo, um grupo com 18 passageiros,
acompanhados de um guia turístico, serão transportados do aeroporto até o hotel em um micro-ônibus. Desses passageiros, 12 são membros da mesma família, constituída por 5 crianças e 7 adultos,sendo Paulo um dos adultos. Durante o trajeto, o guia turístico escolherá, por meio de sorteio aleatório, quatro passageiros do grupo e, a cada um deles, entregará um brinde. Considerando essa situação hipotética, julgue o item a seguir.
A probabilidade de Paulo ser um dos sorteados é superior a 0,2.

Item. 20. (Cebraspe/2022 - UNB) Em uma viagem de turismo, um grupo com 18 passageiros,
acompanhados de um guia turístico, serão transportados do aeroporto até o hotel em um micro-ônibus. Desses passageiros, 12 são membros da mesma família, constituída por 5 crianças e 7 adultos,sendo Paulo um dos adultos. Durante o trajeto, o guia turístico escolherá, por meio de sorteio aleatório, quatro passageiros do grupo e, a cada um deles, entregará um brinde. Considerando essa situação hipotética, julgue o item a seguir.
A probabilidade de os quatro sorteados não serem da família de Paulo é superior a 1/200.

Item. 21. (Cebraspe/2022 - PC/PB) Um levantamento identificou que, em um hospital infantil, os pacientes seguiam a seguinte distribuição por idade.
Com relação à distribuição de frequência da idade dos pacientes apresentada no texto acima, assinale a opção correta.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) Se forem escolhidas duas crianças aleatoriamente para fazerem um exame clínico, a probabilidade de as duas crianças terem 2 anos de idade é de 8,0%.
b) Caso seja escolhida aleatoriamente uma criança para fazer um exame clínico, a probabilidade de ela ter 3anos ou mais é de 60,0%.

c) Se todas as crianças com quatro anos ou mais estiverem brincando no jardim do hospital no momento que foi escolhida aleatoriamente uma criança com 3 anos para também ir ao jardim, a chance de uma criança específica ser a escolhida é de 26,9%.
d) Caso uma criança seja escolhida aleatoriamente para fazer um exame clínico e, no dia seguinte, mais uma criança seja escolhida aleatoriamente para fazer este mesmo exame, a probabilidade de a mesma criança ser escolhida nos dois dias é de 3,3%.
e) Se forem escolhidas quatro crianças aleatoriamente para fazer um exame clínico, a probabilidade de nenhuma delas ter 3 anos ou mais é de 14,1%.
Item. 22. (Cebraspe/2021 - CBM/TO) Considere que em um plantão estejam trabalhando 10
bombeiros, 4
mulheres e 6 homens, e que 3 dessas pessoas devam ser escolhidas ao acaso para atender a uma ocorrência. Nessa situação, a probabilidade de que sejam escolhidas para o atendimento exatamente 2mulheres é de a) 30%
b) 15%

c) 10%

d) 50%

Item. 23. (Cebraspe/2021 - ALE/CE) Uma urna contém 10 bolas idênticas, exceto pela cor: duas bolas são da cor azul e as outras 8 bolas são da cor vermelha. As bolas encontram-se misturadas,aleatoriamente,
dentro da urna. Retirando-se, simultaneamente e aleatoriamente, cinco bolas da urna, a probabilidade de a amostra contemplar, exatamente, 1 bola da cor azul e 4 bolas da cor vermelha é igual a e) 3.125
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 24. (Cebraspe/2022 - TELEBRAS)

Amostragem Aleatória Simples
I Com reposição

II Sem reposição

Tamanho da amostra

Suponha que determinada população de tamanho N = 100 seja constituída pelos elementos xi, xioo.Para a realização de um levantamento amostrai sobre essa população, cogitam-se duas possibilidades mostradas no quadro anterior, ambas pelo método de amostragem aleatória simples. Se o tipo I for o escolhido, então a amostragem será com reposição com n = 6. No entanto, se o escolhido for o tipo II,então a amostra será sem reposição com n = 5. Com base nessas informações, julgue o item que se segue.
Se o tipo II for aplicado, a probabilidade de que a amostra seja formada pelos elementos x8, x27, x70, x77, x9g é igual a *
Item. 25. (Cebraspe/2021 - CBM/AL) Determinado dado tetraédrico (dado em formato de tetraedro regular),com vértices numerados de 1 a 4, foi lançado 21 vezes, de modo que o resultado do lançamento desse dado correspondia ao vértice voltado para cima. A tabela seguinte mostra a frequência com que se obteve cada resultado.
Resultado

Quantidade de Lançamentos

Com base nessa situação hipotética, julgue o item a seguir.

A frequência percentual do resultado 3 é superior a 25%.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. LETRA C 10. ERRADO
Item. 19. CERTO

Item. 2. ERRADO 11. ERRADO
Item. 20. ERRADO

Item. 3. ERRADO 12. CERTO
Item. 21. LETRA E

Item. 4. CERTO 13. CERTO
Item. 22. LETRA A

Item. 5. CERTO 14. LETRA B
Item. 23. LETRA C

Item. 6. CERTO 15. LETRA D
Item. 24. CERTO

Item. 7. ERRADO 16. ERRADO
Item. 25. ERRADO

Item. 8. CERTO 17. CERTO

Item. 9. CERTO 18. LETRA B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Combinações de Eventos

Item. 1. (Cebraspe/2021 - MJ/SP) Ao procurar ativos para realizar operações de day trade em uma lista de
260 ações negociadas em bolsa de valores, um investidor classificou 120 ações como de boa liquidez(elevado volume de negócios realizados diariamente) e 130 ações como de bom nível de volatilidade(muitas variações de preço para cima ou para baixo ao longo do dia); 45 ações ele não classificou em nenhuma dessas classes. Tendo em vista essa situação hipotética, julgue o item seguinte.
Selecionando-se ao acaso uma das ações da lista analisada pelo investidor, a probabilidade de que essa ação tenha bom nível de volatilidade é maior que a probabilidade de ela não ter bom nível de volatilidade.
Item. 2. (Cebraspe/2021 - SERPRO) Em um curral, há doze bezerros, entre os quais apenas três sofrem de diarreia virai bovina, sendo os demais saudáveis. Dois bezerros desse curral serão escolhidos aleatoriamente. Nessa situação hipotética, a probabilidade de se escolher pelo menos um bezerro que sofra de diarreia virai bovina é igual a
Item. 3. (Cebraspe/2021 - SERPRO) Suponha que sejam gerados 5 números válidos de CPF
para serem atribuídos a 5 indivíduos distintos. Com base nessas informações, julgue o item a seguir.
Suponha que, logo após a atribuição dos CPFs aos indivíduos, são escolhidos aleatoriamente 2 desses CPFs e separados 3 desses indivíduos. Nessa situação, a probabilidade de pelo menos um dosCPFs escolhidos pertencer a um dos indivíduos separados é igual a 3/5.
Item. 4. (Cebraspe/2021 - ALE/CE) Considere um experimento aleatório cujo espaço amostrai seja representado por Í1 e, ainda, dois eventos aleatórios A e B, tais que A c B c fi.Se as probabilidades de ocorrência dos eventos A e B forem P(A) = 0,2 e P(B) = 0,3, então P(AUB) é igual a
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 0,06

b) 0,1

c) 0,2

d) 0,3

e) 0,5

Item. 5. (Cebraspe/2022 - PETROBRAS) Considerando dois eventos aleatórios A e B, tais que P(A U B~) =P(A) > 0, P(A Ci B) = P(B) > 0 e P(A) + P(JP) = 1, julgue o item que se segue.

Se Ac denota o evento complementar de A, então é correto afirmar que Ac = B.

Item. 6. (Cebraspe/2021 - Pref. Aracaju) Considere dois eventos A e B contidos em determinado espaço amostrai tal que A B. Se as probabilidades de ocorrências desses eventos e de seus eventos complementares forem P(A') = 0, 3, P(B) = 0,7, P(A) = 0,7 e P(B~) = 0, 3, então a) P(4 U B) = 1
b)PQ4ClB) = 0,21

c) P(Ã U B) = 0, 3

d) P(A n B) = 0, 3

e) P(4 n B) = 0,4

Item. 7. (Cebraspe/2020 - TJ/PA) Se íí representar um espaço amostrai de determinado experimento aleatório, A c Í2 e B c íl forem dois eventos com P(4) = 0,4 eP(JP) = 0,8 e se A e B forem,
respectivamente, os eventos complementares de A e B, então a) P(4 0 B) > 0, 2
b) P(A UB) + P(4 n B) < 1

c) P(A n A n 21) = 0, 064

d) 0,2 < P(4 0B) < 0,4

e) P(Ã n B) + P(Ã n B) > 0,7

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 8. (Cebraspe/2021 - PF) Considere os seguintes conjuntos:

p =

Pl =

p2 =
p3 =

{todos os policiais federais em efetivo exercício no país}

{policiais federais em efetivo exercício no país e que têm até 1 ano de experiência no exercício do cargo}
{policiais federais em efetivo exercício no país e que têm até 2 anos de experiência no exercício do cargo}
{policiais federais em efetivo exercício no país e que têm até 3 anos de experiência no exercício do cargo}
e, assim, sucessivamente. Com base nessas informações, julgue o item que se segue.

Escolhendo-se aleatoriamente um integrante do conjunto P, a probabilidade de ele ter entre dois e três anos n(p p )
de experiência no exercício do cargo é dada por , em que n(X) indica o número de elementos do conjunto X e P₂-P3 é 0 conjunto formado pelos indivíduos que estão em P₂, mas não estão em P₃.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. ERRADO 4. LETRA D
Item. 7. LETRA D

Item. 2. LETRA E 5. ERRADO
Item. 8. ERRADO

Item. 3. ERRADO 6. LETRA E

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Probabilidade Condicional

Item. 1. (Cebraspe/2022 - PETROBRAS) No que diz respeito aos conceitos e cálculos utilizados em probabilidade e estatística, julgue o item a seguir.
Considere que, em uma sala de provas de um concurso, ao se selecionar aleatoriamente um candidato para acompanhar a abertura do envelope de provas, a probabilidade de ele ter estudado em escola particular é0,32 e a probabilidade de ele ter estudado em escola particular e ser um candidato forte à aprovação é 0,24.Nessa situação, se o candidato selecionado estudou em escola particular, então a probabilidade de ele ser um candidato forte à aprovação é 0,75.
Item. 2. (Cebraspe/2022 - UNB) Em uma viagem de turismo, um grupo com 18 passageiros,
acompanhados de um guia turístico, serão transportados do aeroporto até o hotel em um micro-ônibus. Desses passageiros, 12 são membros da mesma família, constituída por 5 crianças e 7 adultos,sendo Paulo um dos adultos. Durante o trajeto, o guia turístico escolherá, por meio de sorteio aleatório, quatro passageiros do grupo e, a cada um deles, entregará um brinde. Considerando essa situação hipotética, julgue o item a seguir.
Se os quatro brindes forem entregues a membros da família de Paulo, então a probabilidade de os sorteados serem as crianças é inferior a 0,01.
Item. 3. (Cebraspe/2018 - ABIN) A tabela abaixo mostra dados de sobrevivência (em dias) de uma coorte de animais acometidos por uma doença aguda. Na primeira coluna, t corresponde aos dias, sendo t = 0o dia em que a contagem começou a ser feita; vt, na segunda coluna, é a quantidade de animais vivos no início do dia t; dt, na terceira coluna, indica quantos animais morreram no decorrer do dia t.
t n

0 10 000

1 9.500

2 8.800

3 8000

4 7.200

5 6.120

6 5400

7 4.050

8 2.700

9 1.500

XíM)
1 080

1.350

1.350

1.200

1.500

Com referência a essas informações, julgue o item que se segue.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Se um animal que estivesse vivo no início do dia t = 4 fosse escolhido ao acaso, a probabilidade de ele morrer nesse dia seria igual a 15%.
Item. 4. (Cebraspe/2018 - ABIN) A tabela abaixo mostra dados de sobrevivência (em dias) de uma coorte de animais acometidos por uma doença aguda. Na primeira coluna, t corresponde aos dias, sendo t = 0o dia em que a contagem começou a ser feita; vt, na segunda coluna, é a quantidade de animais vivos no início do dia t; dt, na terceira coluna, indica quantos animais morreram no decorrer do dia t.
r n

0 10.000

i 9.500

2 8.800

3 8000

4 7.200

5 6.120

6 5400

7 4.050

8 2.700

9 1.500

1 080

1.350

1350

1.200

1.500

Com referência a essas informações, julgue o item que se segue.

Se um animal que estivesse vivo no início do dia t = 3 fosse escolhido ao acaso, a probabilidade de ele ter morrido até o dia t = 6 seria superior a 50%.
Item. 5. (Cebraspe/2018 - ABIN) A tabela abaixo mostra dados de sobrevivência (em dias) de uma coorte de animais acometidos por uma doença aguda. Na primeira coluna, t corresponde aos dias, sendo t = 0o dia em que a contagem começou a ser feita; vt, na segunda coluna, é a quantidade de animais vivos no início do dia t; dt, na terceira coluna, indica quantos animais morreram no decorrer do dia t.
t n

0 10000

1 9.500

2 8.800

3 8000

4 7.200

5 6.120

6 5400

7 4.050

8 2.700

9 1.500

1 080

1.350

1 350

1.200

1.500

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com referência a essas informações, julgue o item que se segue.

Se um animal que estivesse vivo no início do dia t = 4 fosse escolhido ao acaso, a probabilidade de ele ter chegado vivo no dia t = 7 seria superior a 60%.
Item. 6. (Cebraspe/2018 - PF) O resultado de uma pesquisa acerca da satisfação de 200
papiloscopistas, no que diz respeito às tarefas por eles executadas de identificação de vítimas e de descobertas de crimes de falsificação, foi o seguinte:
* 30 papiloscopistas sentem-se igualmente satisfeitos ao executar qualquer uma dessas tarefas;

* 180 papiloscopistas sentem-se satisfeitos ao executar pelo menos uma dessas tarefas.

Considerando que todos os 200 papiloscopistas responderam à pesquisa, julgue o item seguinte.

A probabilidade de que um papiloscopista, escolhido ao acaso, tenha se dito igualmente satisfeito ao executar qualquer uma entre as duas tarefas mencionadas, dado que se sente satisfeito ao executar pelo menos uma das duas tarefas, é inferior a 0,15.
Item. 7. (Cebraspe/2018 - ABIN) Considerando os conceitos associados a probabilidade e estatística, julgue o item.
A probabilidade de se obter um número menor que 5 no lançamento de um dado, sabendo que o dado não é defeituoso e que o resultado é um número ímpar, é igual a 2/3.
Item. 8. (Cebraspe/2022 - FUNPRESP-EXE) A seguir, são apresentadas informações obtidas a partir de uma pesquisa realizada com 1.000 pessoas.
* 480 possuem plano de previdência privada;

* 650 possuem aplicações em outros tipos de produtos financeiros;

* 320 não possuem aplicação em nenhum produto financeiro.

Com base nessa situação hipotética, julgue o item seguinte.

Se uma pessoa escolhida ao acaso entre as que participaram da pesquisa possui plano de previdência privada, então a probabilidade de ela possuir também aplicação em outros produtos financeiros é superior a 90%.
Item. 9. (Cebraspe/2021 - IBGE) Considere que, quando Carlos, agente de pesquisas por telefone, realiza uma chamada telefônica, a chance de que a sua chamada não seja atendida seja de 20%e que, se a chamada for atendida, a chance de que ele obtenha respostas verdadeiras seja de 60%. Nessa situação, a probabilidade de Carlos obter respostas verdadeiras em uma dada chamada telefônica é igual a
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 12%

b) 48%

c) 60%

d) 80%

e) 88%

Item. 10. (Cebraspe/2021 - BANESE) Considerando que A e B sejam eventos aleatórios independentes e queP(A) = 0,8 e P(B) = 0,2, julgue o próximo item.

Item. 11. (Cebraspe/2021 - BANESE) Considerando dois eventos aleatórios A e B, tais que
P(A|B) = -,

P(B\A) = 0, 5 e P(A U B) = 0, 8, julgue o seguinte item.

PQ4) > P(B).

Item. 12. (Cebraspe/2021 - BANESE) Considerando dois eventos aleatórios A e B, tais que
PQ4|B) = -,
P(B|i4) = 0, 5 e P(A U B) = 0, 8, julgue o seguinte item.

P(A n B) = 0,2.

Item. 13. (Cebraspe/2022 - PETROBRAS) Considerando dois eventos aleatórios A e B, tais que P(A UB) =P(i4) > 0, P(A n B) = P(B) > 0 e PQ4) + P(B) = 1, julgue o item que se segue.

São eventos independentes.

Item. 14. (Cebraspe/2021 - BANESE) Considerando que A e B sejam eventos aleatórios independentes e queP(i4) = 0,8 e P(B) = 0,2 julgue o próximo item.

P(A n B) = 0.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 15. (Cebraspe/2018 - IJSN/ES) Considerando os conceitos associados a probabilidade e estatística,julgue o item.

Com base no espaço amostrai S = {1, 2, 3, 4} é correto afirmar que os eventos A = {2 ,4} e B = {1,
4}, não são independentes.
Item. 16. (Cebraspe/2021 - SEDUC/AL) O próximo item apresenta uma situação hipotética a ser julgada,acerca de problemas matemáticos envolvendo situações em uma escola.

No primeiro andar de uma escola, todas as 10 salas de aula possuem as portas do mesmo lado e em sequência. Três alunos distraídos, mexendo em seus celulares, estão indo em direção a suas respectivas salas de aula, porém, como estão distraídos, eles podem entrar em qualquer uma das salas, de forma independente. Nessa situação hipotética, a probabilidade de os três alunos entrarem exatamente na mesma sala é de 1%.
Item. 17. (Cebraspe/2018 - IJSN/ES) Considerando os conceitos associados a probabilidade e estatística,julgue o item. Considere que de uma urna contendo 2 bolas azuis e 6 bolas brancas retira-se ao acaso uma bola, anota-se sua cor e repõe-se a bola na urna. Em seguida retira-se novamente uma bola da urna e anota-se sua cor.
Nessas condições, a probabilidade das duas bolas retiradas serem azuis é %.

Item. 18. (Cebraspe/2021 - MJ/SP) Em um jogo de cara e coroa disputado com uma moeda não viciada, um pai criou a seguinte regra, visando aumentar as chances de sua filha vencer a disputa: a moeda seria lançada certa quantidade de vezes, n, definida previamente, e o pai só sairia vencedor caso a moeda apontasse cara em todos os n lançamentos. Tendo como referência essa situação hipotética, julgue o item que se segue.
Se n = 2, a probabilidade de vitória da filha será de 75%.

Item. 19. (Cebraspe/2021 - MJ/SP) Em um jogo de cara e coroa disputado com uma moeda não viciada, um pai criou a seguinte regra, visando aumentar as chances de sua filha vencer a disputa: a moeda seria lançada certa quantidade de vezes, n, definida previamente, e o pai só sairia vencedor caso a moeda apontasse cara em todos os n lançamentos. Tendo como referência essa situação hipotética, julgue o item que se segue.
10 é o menor número de lançamentos que asseguraria à filha chance de vencer de pelo menos 95%.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 20. (Cebraspe/2022 - PC/PB) Na enfermaria de um hospital estavam internados 32
pacientes. Destes,

8 apresentavam pneumonia, 6 tinham diagnóstico de asma, 10 estavam com gripe, 6 tinham câncer no pulmão e os demais aguardavam atendimento. Coincidentemente, em cada grupo a quantidade de homens e mulheres era a mesma. Considerando essa situação hipotética, assinale a opção correta.
a) Foram escolhidos aleatoriamente 3 pacientes dentre aqueles com gripe para responder uma pesquisa. Aprobabilidade de todos eles serem mulheres é de 50%.

b) Se selecionado um paciente aleatoriamente para a realização de um exame, a probabilidade de ele estar com asma ou ser um dos que têm câncer no pulmão é de 18,75%.
c) 4 pacientes serão escolhidos aleatoriamente para receber uma visita especial. A
chance deste grupo ser composto por um homem com pneumonia, uma mulher com asma, uma mulher com gripe e um homem que tem câncer no pulmão é de 0,12%.
d) Sabe-se que a proporção de diagnóstico de asma nos pacientes que chegam ao hospital é a mesma daquela dos pacientes já diagnosticados que estavam na enfermaria. Assim, a probabilidade dos dois pacientes que aguardam atendimento receberem diagnóstico de asma é de 20%.
e) A cada dia, durante os próximos 4 dias, um paciente será escolhido aleatoriamente para receber uma sobremesa especial no almoço. A chance dos quatro pacientes sorteados serem mulheres é de 6,25%.
Item. 21. (Cebraspe/2022 - DPE/RO) A confiabilidade mensura a capacidade que um sistema,
produto ou serviço possui de se comportar da forma esperada, podendo estar associada a diversas áreas de gestão,inclusive gestão da qualidade. As informações apresentadas na seguinte tabela referem-se a determinado processo produtivo dividido em 3 etapas A, B e C.
Etapa
A
B
C

Confiabilidade
0,95

0,80

0,50

Com base nas informações apresentadas, assinale a opção que mostra a confiabilidade desse processo produtivo.
a) 0,95

b) 0,50

c) 0,45

d) 0,38

e) 0,80

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 22. (Cebraspe/2021 - ALE/CE) A probabilidade de um jogador acertar determinado alvo em cada rodada de um jogo é igual a 0,6. Na tabela abaixo, por exemplo, em determinada partida, esse jogador acertou o alvo pela primeira vez na quarta rodada.
roclada

1 2 3 4 5

X X X / /

6 7 8

X / X

9 10

X /

Caso esse mesmo jogador inicie outra partida, considerando-se que haja independência mútua entre duas rodadas, a probabilidade de ele acertar o alvo, pela primeira vez, na terceira rodada é igual a a) 0,096
b) 0,16

c) 0,33

d) 0,60

e) 0,76

Item. 23. (Cebraspe/2021 - COREN/SE) Um ambulatório funciona diariamente nos períodos matutino e vespertino, sendo registradas, diariamente, as ocorrências de incidentes durante o seu funcionamento.Para essa situação hipotética, considere que

A = "ocorrência diária de incidentes no período matutino" e
B = "ocorrência diária de incidentes no período vespertino".

Se A e B forem dois eventos aleatórios independentes cujas probabilidades sejam P(A) = 0,5 e P(B) =
0,5,
então a probabilidade de ocorrência diária de incidentes nesse ambulatório, representada como o eventoA U B, será igual a a) l b) 0
c) 0,25

d) 0,75

Item. 24. (Cebraspe/2022 - TELEBRAS) Julgue o item que se segue, a respeito de contagem,
probabilidade e estatística.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considere que seja preciso comprar duas peças pi e P2 para um projeto de satélite.
Considere ainda que a probabilidade de ter a peça pi no estoque na distribuidora é de 1/3 e a probabilidade de ter a peça P2 no estoque na mesma distribuidora é de 3/5. Nesse caso, a probabilidade de que pelo menos uma das peças esteja no estoque é de 11/15.
Item. 25. (Cebraspe/2021 - ADAPAR) A tabela a seguir apresenta a porcentagem de lotes de carnes produzidos por cada estado da região Sul do Brasil em 2019, em relação ao total dos lotes produzidos nessa região durante esse período.
Estado da Região Sul
Paraná

Rio Grande do Sul
Santa Catarina porcentagem de lotes de carne produzidos50%

42%

8%

Por razões sanitárias, nesse mesmo ano, foram descartados 2,5% dos lotes produzidos no Paraná, 3%
dos lotes produzidos no Rio Grande do Sul e 3,5% dos lotes produzidos em Santa Catarina.
Nessa situação hipotética, a probabilidade de se selecionar aleatoriamente um lote de carne produzido nessa região que tenha sido descartado no referido ano é de a) 0,0168
b) 0,0279

c) 0,09

d) 0,91

e) 0,9721

Item. 26. (Cebraspe/2019 - TJ/AM) Se Carlos estiver presente na aula ministrada pela professora Paula, a probabilidade de ele aprender o conteúdo abordado é de 80%; se ele estiver ausente,essa probabilidade cai para 0%. Em 25% das aulas da professora Paula, Carlos está ausente.
Com relação a essa situação hipotética, julgue o item seguinte.

A probabilidade de Carlos não aprender o conteúdo ministrado pela professora Paula é inferior a
25%.

Item. 27. (Cebraspe/2019 - TJ/AM) Se Carlos estiver presente na aula ministrada pela professora Paula, a probabilidade de ele aprender o conteúdo abordado é de 80%; se ele estiver ausente,essa probabilidade cai para 0%. Em 25% das aulas da professora Paula, Carlos está ausente.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com relação a essa situação hipotética, julgue o item seguinte.

O evento "Carlos não aprendeu o conteúdo ministrado pela professora Paula, dado que estava ausente na aula." é evento certo, isto é, a probabilidade de esse evento ocorrer é igual a 1.
Item. 28. (Cebraspe/2022 - PETROBRAS) O item a seguir é apresentada uma situação hipotética seguida de uma assertiva a ser julgada a respeito de probabilidade e estatística.
Uma empresa faz toda a produção do seu único produto em duas fábricas distintas A e
B, que produzem,
respectivamente, 75% e 25% da produção total. Na fábrica A, 5% da produção passa por um processo de controle de qualidade, enquanto, na fábrica B, a produção que passa pelo controle de qualidade é de 10%.Nessa situação, escolhendo-se um produto ao acaso dentre os que passaram por controle de qualidade, após todas as etapas da produção, a probabilidade desse item ter sido produzido na fábrica B é inferior a 30%.
Item. 29. (Cebraspe/2022 - TELEBRAS) Julgue o item que se segue, a respeito de contagem,
probabilidade e estatística.
Considere que o lançamento de um satélite no centro de lançamento de Alcântara esteja previsto para o dia
5 de abril, e que, naquela região, chove apenas 10 dias durante esse mês.
Considere ainda que a meteorologia prevê chuva para o dia do lançamento e que, quando efetivamente chove, a meteorologia prevê corretamente a chuva em 90% das vezes, e, quando não chove, ela prevê incorretamente chuva 10%das vezes. Nessa situação, a probabilidade de chover no dia do lançamento do satélite é inferior a
80%.

Item. 30. (Cebraspe/2021 - SEDUC) O próximo item apresenta uma situação hipotética a ser julgada, acerca de problemas matemáticos envolvendo situações em uma escola.
O professor de biologia leva uma turma de alunos para uma viagem de pesquisa. A
manhã do dia de saída para a viagem encontra-se nublada no destino da viagem, e sabe-se que manhãs nubladas acontecem em40% dos dias ali. Além disso, nesse local, 50% dos dias em que chove começam nublados, contudo, no mês em que acontece a viagem, costuma chover pouco — exatamente 20% dos dias são chuvosos. Nessa situação hipotética, a chance de chover durante o dia da viagem é de 12,5%.
Item. 31. (Cebraspe/2018 - ABIN) Considerando os conceitos associados a probabilidade e estatística, julgue o item.
Considere que as bolas de uma urna tenham sido divididas em duas caixas, sendo que a caixa I ficou com 3bolas brancas e 1 bola preta, enquanto a caixa II ficou com 3 bolas brancas e 3
bolas pretas. Em seguida, uma caixa foi escolhida e dela foi sorteada uma bola. Sabendo que a cor da bola sorteada era branca, a probabilidade de ter vindo da caixa I é de 3/8.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. CERTO 12. CERTO
Item. 23. LETRA D

Item. 2. ERRADO 13. ERRADO
Item. 24. CERTO

Item. 3. CERTO 14. ERRADO
Item. 25. LETRA B

Item. 4. ERRADO 15. ERRADO
Item. 26. ERRADO

Item. 5. ERRADO 16. CERTO
Item. 27. CERTO

Item. 6. ERRADO 17. ERRADO
Item. 28. ERRADO

Item. 7. CERTO 18. CERTO
Item. 29. ERRADO

Item. 8. CERTO 19. ERRADO
Item. 30. ERRADO

Item. 9. LETRA B 20. LETRA E
Item. 31. ERRADO

Item. 10. CERTO 21. LETRA D

Item. 11. ERRADO 22. LETRA A

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

