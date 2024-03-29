# Probabilidade e Estatística - Distribuições Discretas de Probabilidade

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Introdução - Distribuições Discretas de Probabilidade

2) Distribuição Uniforme

3) Distribuição de Bernoulli

4) Distribuição Binomial

5) Distribuição Geométrica

6) Distribuição Hipergeométrica

7) Distribuição de Poisson

8) Distribuição Binomial Negativa

9) Questões Comentadas - Distribuição Uniforme - Cebraspe

10) Questões Comentadas - Distribuição de Bernoulli - Cebraspe

11) Questões Comentadas - Distribuição Binomial - Cebraspe

12) Questões Comentadas - Distribuição Geométrica - Cebraspe ...

13) Questões Comentadas - Distribuição de Poisson - Cebraspe ...

14) Lista de Questões - Distribuição Uniforme - Cebraspe

15) Lista de Questões - Distribuição de Bernoulli - Cebraspe

16) Lista de Questões - Distribuição Binomial - Cebraspe

17) Lista de Questões - Distribuição Geométrica - Cebraspe

18) Lista de Questões - Distribuição de Poisson - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Olá, concurseiro(a)! Estão aproveitando o curso?

Agora, vamos estudar Distribuições Discretas: aquelas distribuições especiais, como a distribuição binomial,que caem bastante em prova. Os conceitos envolvidos são aqueles que vimos na aula de variáveis discretas,mas aqui eles são utilizados de maneira diferente. Então, mesmo que você não esteja muito seguro com a aula passada, vem comigo, para aprender a resolver questões de distribuições discretas
Até já!

Luana Brandão

Posso te falar um pouquinho sobre mim? Sou Doutora em Engenharia de Produção, pela
Universidade Federal
Fluminense, e Auditora Fiscal da SEFAZ-RJ. Sou professora de Estatística do Estratégia,
porque quero muito ajudá-lo(a) em sua trajetória rumo à aprovação!
Se tiver alguma dúvida, entre em contato comigo!

M professoraluanabrandao@gmail.com
@professoraluanabrandao

"Quando pensar em desistir, lembre-se da causa pela qual você começou."

Elias Lima da Silva

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçõES DISCRETAS DE PRoBABILIDADE

Nesta aula, veremos algumas distribuições específicas de probabilidade, chamadas de
Distribuições Teóricas ou Distribuições Especiais, que, por serem muito comuns, merecem atenção especial.
Distribuições Uniformes

Distribuições uniformes são aquelas cujos possíveis resultados são equiprováveis, como o lançamento de uma moeda equilibrada ou de um dado equilibrado; ou o sorteio de um elemento quando as probabilidades de todos os elementos serem sorteados forem iguais.
Para distribuições uniformes, havendo um total de N elementos, a probabilidade de cada valor x é dada por:
Por exemplo, a probabilidade de cada face da moeda é P = - e do dado é P =-.

2 6

Visualmente, no gráfico de uma distribuição uniforme, as barras apresentam o mesmo tamanho, como representado abaixo, para o exemplo do dado:
Distribuição Uniforme
Dado Equilibrado

Vamos calcular a esperança dessa distribuição. A fórmula geral da esperança é:

F(X) = ^x.P(x)

Como P(X = x) = para uma distribuição uniforme, então a esperança dessa distribuição é:

E (X) =

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ou seja, a esperança da distribuição uniforme corresponde à média aritmética dos valores da variável. Para o exemplo do dado, a esperança é:
1+2+3+4+5+6 21 7

Em= 6 = T=2

O próximo passo é calcular a variância dessa distribuição. A fórmula da variância é:

K(X) = E(X2) - [E(X)]2

Sabemos calcular E(X), então basta elevá-la ao quadrado para calcular [E(X)]2. Já o valor de E(X2) é definido como:
E(X2) = ^%2.P(%)

Como P(x) = - para uma distribuição uniforme, então, para essa distribuição, temos:

Ou seja, PQY2) é a média aritmética dos valores da variável elevados ao quadrado.

Para o exemplo do dado, o valor de E(X2) é:

z l2 + 22 + 32 + 42 + 52 + 62 1 + 4 + 9 + 16 +
25 + 36 91

6 = 6 = T

Logo, a variância será a diferença:

2 91 49 182 - 147 35

12 " 12

A maioria das distribuições teóricas conhecidas fazem parte da chamada família exponencial (ex.: binomial, geométrica, hipergeométrica, de Poisson;exponencial,
Normal). Uma família é um conjunto de distribuições que apresentam características semelhantes. Para a família exponencial, a função de probabilidade pode ser descrita de forma similar.
A distribuição uniforme é uma distribuição discreta importante que não pertence à família exponencial.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

r

,

i (2008 - TJ/RO) Uma urna contém dez bolas, cada uma gravada com um número diferente, de 1 a 10.
Uma bola é retirada da urna aleatoriamente e X é o número marcado nesta bola. X é uma variável aleatória cujo(a)
I

I

i a) desvio padrão é 10.

b) primeiro quartil é 0,25.

: c) média é 5.

d) distribuição de probabilidades é uniforme.

I

i e) distribuição de probabilidades é assimétrica.
I

; Comentários:

I

: Sabendo que todas as bolas possuem a mesma probabilidade de serem sorteadas, então elas seguem distribuição uniforme. Com isso, já sabemos a resposta da questão (D), mas vejamos as demais alternativas.
: Em relação à alternativa C, a média é:

I

s

"=E®=—
1+2+3+4+5+6+7+8+9+ 10 55

1707 " lõ

5,5

Portanto, a alternativa C está incorreta.

= Em relação à alternativa A, o desvio padrão é a raiz da variância, dada por:

7(X) = E(X2) - [£W]2

i Para distribuições uniformes, o valor de FGV2) é dado por:

I

7 £x2

£(JÍ '=—

I

B

„ 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100

fOf2) = 10

= Sabendo que [£(X)]2 = (5,5)2 = 30,25, a variância é:

hT = 38'5

I

j E o desvio padrão é a raiz quadrada:
I

: Assim, a alternativa A está incorreta.

I

7(X) = E(X2) - /z2 = 38,5 - 30,25 = 8,25

B

o = = V^25 - 2,87

: Em relação à alternativa B, sabemos que a probabilidade associada a cada valor é:

B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, a função de distribuição acumulada aumenta em 10% para cada unidade:

X P(x)

1 10%

2 10%

3 10%

4 10%

5 10%

6 10%

7 10%

8 10%

9 10%

10 10%

F(x)

10%

20%

30%

40%

50%

60%

70%

80%

90%

100%

= Observamos que não existe um valor de X = x que corresponda a F(x) = 25%
exatamente. O valor superior a

= 25% mais próximo é F(x) = 30%, associado a X = 3. Portanto, o primeiro quartil é X = 3.
i Assim, a alternativa B está incorreta.

; Em relação à alternativa D, no gráfico de uma distribuição uniforme, todas as barras apresentam o mesmo tamanho. Logo, a distribuição não é assimétrica.
; Gabarito: D

L..............................
..

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçÃo DE BERNoULLI

Uma variável aleatória discreta X com Distribuição de Bernoulli assume apenas 2 valores possíveis, 0 ou 1,em um experimento realizado uma única vez. Esse experimento é chamado de Ensaio de
Bernoulli ou
Experimento de Bernoulli.

Um exemplo clássico dessa distribuição é o lançamento de uma moeda.

Chamamos os resultados possíveis de sucesso (em que a variável assume o valor X = 1) ou fracasso (em que a variável assume o valor X = 0). Se estivermos interessados na face CARA, esta representaria o sucesso eCOROA representaria o fracasso (ou o contrário, se estivéssemos interessados na outra face).

Nesse exemplo, não faz muita diferença qual face corresponde ao sucesso ou ao fracasso, porque a probabilidade de ambas é a mesma: 50%.
Agora, vamos considerar que estamos torcendo para que o resultado do lançamento de um dado seja um múltiplo de 3. Nesse caso, os resultados 3 e 6 correspondem ao sucesso e os demais resultados correspondem ao fracasso.
Assim, teríamos 2 resultados de sucesso (em que X = 1) e 4 resultados de fracasso (em que X = 0).
Logo, as probabilidades seriam as seguintes:
z x 2 1P(X ) = - =
6 3

4 2

P(X = 0) = - = -

6 3

Normalmente, indicamos a probabilidade de sucesso como p e a probabilidade de fracasso como q.

p = P(X = 1)

q = P(X = 0)

Para esse exemplo, temos p = | e q = |.

Outro exemplo de uma distribuição de Bernoulli é associar o sucesso a apenas uma das faces do dado, por exemplo, a face 3. Nesse caso, temos 1 resultado de sucesso (X = 1) e 5 resultados de fracasso (X =0):

p = PÇX = 1) = j

Q = P(X = 0) = f

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Como há apenas 2 resultados possíveis, as probabilidades de sucesso e de fracasso são complementares,
isto é, a soma dessas 2 probabilidades é igual a 1:

p + q = l q = l-p
A probabilidade de sucesso p é a única informação necessária para caracterizar uma distribuição deBernoulli, uma vez que a probabilidade de fracasso é calculada a partir dela. Por isso, podemos indicar que uma variável X segue distribuição de Bernoulli como X~Ber(p).
Esse dado que caracteriza uma distribuição de probabilidade é chamado de parâmetro.

Um mesmo experimento pode estar associado a variáveis aleatórias com distribuições distintas de probabilidade, dependendo de como você o analisa.
O lançamento de um dado, por exemplo, pode estar associado a uma variável uniforme,
com 6 valores equiprováveis; ou a distribuições de Bernoulli com parâmetros distintos;dentre outras distribuições possíveis.

Agora, vamos calcular a esperança da distribuição de Bernoulli. A fórmula geral da esperança é:

£(X) = ^\.P(X = x)

EGO = 0xq + lxp

£(X) = P

Para calcular a variância, primeiro calculamos EtX2'):

E(X2') = ^x2.P(X = x)

£(X2) = O2 x q + l2 x p
E(X2) = p

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Logo, a variância é:

K(X) = E(X2) - [£(X)]2

V(X) = p - p2 = p(l — p)

V(X) = p. q

Para o exemplo do dado, em que o sucesso corresponde a uma face múltipla de 3,
vimos que p = - e q =

Nesse caso, a esperança e a variância são:

F(X) = p

V(X) = p.q

12 2

~ 3 X 3 " 9

Para o exemplo em que o sucesso corresponde a uma face específica do dado, vimos que p = - e q =

Nesse caso, a esperança e a variância são:

F(X) = p

W) = p.q

1 JL

6 6 36

ESQUEMATIZANDO

Distribuição de Bernoulli (p)

1 experimento: Ensaio de Bernoulli

2 resultados possíveis: sucesso (X = 1) ou fracasso (X = 0)
Probabilidade de sucesso: P[X = 1] = p

Probabilidade de fracasso: P[X = 0] = q = 1 — p

Esperança: = p; Variância: 7(X) = P Q

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (2017 - SES/DF) Considere o lançamento de um dado cúbico honesto cujas faces são numeradas de 1 a 6, i
; após o qual é observado se o número da face voltada para cima é múltiplo de 3.
Tendo em vista que um j

= experimento como esse pode apresentar apenas dois resultados possíveis
(sucesso ou falha), é correto i

; afirmar que tal experiência denomina-se distribuição

= a) de Bernoulli.

b) hipergeométrica.
i

I

I

: c) de Poisson.
;

d) normal.
;

I

: e) qui-quadrado.

i

I

i Comentários:

A distribuição que trabalha com apenas 2 resultados possíveis (sucesso ou fracasso) para 1 ensaio
(no caso, ;

1 lançamento do dado) é a distribuição de Bernoulli.
i

I

I

; Gabarito: A.

I

i (CESPE/2016 - TCE/PA) Se as variáveis aleatórias X e Y seguem distribuições de Bernoulli, tais que:
P[X = 1] = P[Y = 0] = 0,9

I

: Então a média de Y é superior a 0,5.
i

I

i Comentários:

I

I

A questão indaga sobre a média (esperança) de Y.

I

: O enunciado informa que Y segue distribuição de Bernoulli, com probabilidade de fracasso de:
i

P(Y = 0) = q = 0,9

= Logo, a probabilidade de sucesso é complementar:

i p + q = 1

i

: p = 1 - 0,9 = 0,1
j

: Assim, a esperança de Y é:

F(r) = p = o,i

= Que é inferior a 0,5.

I

I

: Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçÃo BINoMIAL

Quando repetimos um mesmo Ensaio de Bernoulli (isto é, o experimento com 2 resultados possíveis),
damos origem à Distribuição Binomial.

Para termos uma distribuição binomial, é necessário que a probabilidade de sucesso de cada repetição seja a mesma (afinal, estamos repetindo um mesmo Ensaio de Bernoulli).
Além disso, as repetições precisam ser independentes, isto é, o resultado de um experimento não pode afetar o resultado de outro.
Os parâmetros dessa distribuição (os dados que a caracterizam) são o número n de repetições e a probabilidade de sucesso p. Por isso, podemos indicar que uma variável X segue distribuição binomial comoX~B(n,p).

A Distribuição Binomial pode ser considerada a soma de n variáveis com Distribuição de
Bernoulli independentes, com mesmo parâmetro p.

Também é possível formar uma distribuição binomial pela soma de outras distribuições binomiais, com mesmo parâmetro p.
Por exemplo, sendo nx = 3 o número de repetições da variável X e nY = 4 o número de repetições da variável Y, então a soma das variáveis S = X + Y terá distribuição binomial com o seguinte número de repetições:
ns = nx + nY = 4 + 3 = 7

Um exemplo de distribuição binomial é o lançamento de um dado n = 3 vezes, em que o sucesso, corresponde à face 6 e o fracasso corresponde às demais faces.
Cada um desses lançamentos corresponde a um Ensaio de Bernoulli, em que podemos obter,
em cada um deles, sucesso (XBer = 1) ou fracasso (XBer = 0), ou seja, 2 resultados possíveis.
Assim, o número de possíveis resultados para os 3 lançamentos é (princípio multiplicativo de combinatória):
2x2x2=8

As 8 possibilidades são:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A variável X com distribuição binomial representa o número de sucessos obtidos em todos os n lançamentos.
Sabendo que cada sucesso terá valor 1 e que cada fracasso terá valor 0, então o número de sucessos pode ser calculado pela soma dos resultados dos Ensaios.
Para o nosso exemplo dos 3 lançamentos, a variável binomial pode assumir os seguintes valores:

* X = 0 (nenhum sucesso): {(0,0,0)}

* X = 1 (1 sucesso): {0,0,1), (0,1,0), (1,0,0)}

* X = 2 (2 sucessos): {(0,1,1), (1,0,1), (1,1,0)}

* X = 3 (3 sucessos): {(1,1,1)}

De maneira geral, a variável binomial pode assumir qualquer valor entre 0 e n.

Agora, vamos calcular a probabilidade de cada valor dessa variável binomial.
A probabilidade de obter a face 6 (sucesso) em um único lançamento é:

E a probabilidade de não obter a face 6 (fracasso) em um único lançamento é complementar:

,=1-p=-

Logo, a probabilidade de ter fracasso nos n = 3 lançamentos (0 sucesso: X = 0)
corresponde à interseção de n = 3 fracassos. Por serem eventos independentes, a interseção é o produto das probabilidades:
z A 5 5 5

p(X = 0) = qxqxq=-x-x- =

6 6 6

Generalizando, para n repetições, a probabilidade de ter 0 sucesso (n fracassos) é:

P(X = 0) = q x q x ... x q = qn

'------------ --—i 1

n vezes

Similarmente, a probabilidade de obter somente sucessos (nenhum fracasso) nos n = 3
lançamentos (X = 3)
corresponde à interseção desses eventos independentes, dada pelo produto:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Generalizando, para n repetições, a probabilidade de ter n sucessos (0 fracassos) é:

P(X = ri) = p x p x ... x p = pn n vezes
Já, a probabilidade de obter exatamente 1 sucesso (2 fracassos) é igual à probabilidade de obter 1 sucesso no primeiro experimento OU 1 sucesso no segundo experimento OU 1 sucesso no terceiro experimento:
p(x = 1) = P({l,0,0} U {0,1,0} U {0,0,1})

Como são eventos mutuamente excludentes, a probabilidade da união desses eventos é a soma dessas probabilidades:
P(X = 1) = P({l,0,0} U {0,1,0} U {0,0,1}) = P({l,0,0}) + P({0,l,0}) + P({0,0,l})

Agora, vamos calcular essas probabilidades para o nosso exemplo:

P({l,0,0}) =

P({0,l,0}) =

P({0,0,l}) =

1 5 5 25

px(/x(7= x x =

5 1 5 25

Qxpx(7= x x =

5 5 1 25

QxQxP=-x-x- = -

Como as probabilidades são todas iguais, em vez de somá-las, basta MULTIPLICAR o resultado por 3:

z > 25 75

P(X = l) = 3xpxqxq = 3x —— = ——

zlo zló

E a probabilidade de obter exatamente 2 sucessos (1 fracasso) é igual à probabilidade de obter 1 fracasso no primeiro OU no segundo OU no terceiro experimento:
P({0,l,l}) = qxpxp

=6X6X6= 216

P({l,0,l}) = p x q xp

15 1

=6X6X6=

P({l,l,0}) = p xp x q

—11_5

xs _ y 5 —

6 6 6 216

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Esses eventos também são mutuamente excludentes, então a probabilidade da união também corresponde à soma das probabilidades. Como elas são iguais, podemos multiplicar o resultado por 3:
Generalizando, para n repetições, vamos calcular a probabilidade de obter k sucessos, digamos, nas primeiras k tentativas e, portanto, n — k fracassos nas demais tentativas:
pxpx ...xpxqxqx ...x q = pkx qn~k i r i '------------ Y
k vezes n — k vezes

Porém, a ordem não precisa ser exatamente essa. Podemos obter k sucessos em quaisquer k tentativas. Por isso, devemos multiplicar esse resultado pelo número de maneiras de reorganizar os resultados de sucesso e fracasso.
Para isso, podemos simplesmente "escolher" quais serão as tentativas que resultarão em k sucessos, pois as outras n — k tentativas serão, necessariamente, fracassos.
O número de maneiras de "escolher" k tentativas, dentre n tentativas no total,
corresponde à combinação de k elementos, dentre n:
n!

(n-/c)!xk!

Logo, a probabilidade de ter exatamente k sucessos (e, portanto, n — k fracassos) é o produto da probabilidade pk x qn~k com a combinação Cnk.
TOME

NOTA!

p(x = /c) = cnkxpkxqn k

A combinação Cnk também pode ser indicado por Ck ou por

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos calcular também a probabilidade de um intervalo ou de múltiplos valores da variável binomial.
Por exemplo, vamos primeiro calcular a probabilidade de obter 1 OU 2 sucessos, em 3
lançamentos de uma moeda (com p = q = 0,5). Como são eventos mutuamente exclusivos,
devemos somar as probabilidades:

P(X = 1 U X = 2) = P(X = 1) + P(X = 2)

A probabilidade de obter 1 sucesso é:

P(X = 1) = C3;1 x O^1 x 0,52 = 3 x 0,5 x 0,25 = 0,375

A probabilidade de obter 2 sucessos é:

P(X = 2) = C3;2 x 0,52 x O^1 = 3 x 0,25 x 0,5 = 0,375

Então, a probabilidade de obter 1 OU 2 sucessos é:

P(X = 1 U X = 2) = 0,375 + 0,375 = 0,75

Agora, vamos calcular a probabilidade de obter pelo menos um sucesso.

Em geral, para calcular a probabilidade de "pelo menos um", é mais fácil calcular a probabilidade complementar, isto é, a probabilidade de nenhum:
P(X > 1) = 1 - P(X = 0)

A probabilidade de obter 0 sucesso é:

P(X = 0) = C3,o x 0,53 x 0,5° = 1 x 0,125 x 1 = 0,125

Logo, a probabilidade de obter pelo menos um sucesso é o complemento:

P(X > 1) = 1 - 0,125 = 0,875

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Também podemos nos referir a uma distribuição binomial como uma amostra de tamanho n de uma população que segue uma Distribuição de Bernoulli.
Por exemplo, vamos supor uma população de peças, das quais 20% delas são defeituosas.
Nesse caso, a seleção de uma única peça corresponde a um Ensaio de Bernoulli, pois há 2 resultados possíveis: sucesso(peça defeituosa) ou fracasso (peça não defeituosa).

A probabilidade de sucesso desse experimento equivale à proporção de peças defeituosas na população:
p = 20% = 0,2

E a probabilidade de fracasso é complementar: q = 1 - p = 0,8

Suponha que vamos selecionar uma amostra de n = 5 peças ao acaso. O número de peças defeituosas encontradas na amostra segue uma distribuição binomial com parâmetros n = 5 e p = 0,2.
Assim, a probabilidade de obter k = 3 peças defeituosas (portanto, n — k = 2 peças não defeituosas)
é:

PÇX = k) = Cnik xpkx qn~k
P(X = 3) = C5,3 x 0,23 x 0,82

A combinação de 3 elementos, dentre 5, é:

r — 5_! — 5_x4x3!

— 5_x4

— 1 n

5,3 (5-3)!x3! 2! x 3! 2

Logo, a probabilidade de obter 3 é igual a:

FIQUE

ATENTO!

Para que as seleções sejam independentes (condição necessária para termos uma distribuição binomial), isto é, para que o resultado de uma não influencie no resultado da outra, a proporção de peças defeituosas não pode ser alterada a cada extração.
Para que essa condição seja satisfeita, temos duas alternativas:

* A seleção das peças é feita com reposição, isto é, a peça selecionada é devolvida; ou

* A população é infinita (ou grande o suficiente, em comparação com o tamanho da amostra, para permitir tal aproximação).
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

r i
(2020 - Universidade do Estado do Pará - Adaptada) Julgue as seguintes afirmações:

I. As distribuições de Bernoulli e Binomial apresentam as mesmas características e,
portanto, os mesmos parâmetros.
II. Repetições independentes de um ensaio de Bernoulli, com a mesma probabilidade de ocorrência de"sucesso", dão origem ao modelo Binomial;

Comentários:

Em relação à afirmativa I, o parâmetro de uma distribuição de Bernoulli é a probabilidade de sucesso p; e os parâmetros de uma distribuição binomial são a probabilidade de sucesso p e o número de repetições n.
Portanto, a afirmativa I está errada.

Em relação à afirmativa II, o modelo Binomial realmente consiste em repetições independentes de um ensaio de Bernoulli, com a mesma probabilidade de sucesso p. Logo, a afirmativa II está certa.
Gabarito: I - Errado; II - Certo.

(CESPE/2016 - Auditor de Controle Externo TCE/PA) Considere um processo de amostragem de uma população finita cuja variável de interesse seja binária e assuma valor 0 ou 1, sendo a proporção de indivíduos com valor 1 igual a p = 0,3.
Considere, ainda, que a probabilidade de cada indivíduo ser sorteado seja a mesma para todos os indivíduos da amostragem e que, após cada sorteio, haja reposição do indivíduo selecionado na amostragem.
A partir dessas informações, julgue o item subsequente.

Se for coletada uma amostra de tamanho n = 20, o número total de observações sorteadas com valor 1 terá distribuição binomial com parâmetros n e p.
Comentários:

A variável binária corresponde a uma distribuição de Bernoulli.

Coletando uma amostra de tamanho n, então o número de observações com o atributo sucesso corresponde a uma variável binomial, com parâmetros n e p.
Gabarito: Certo.

(CESPE/2016 - TCE/PA) Se as variáveis aleatórias X e Y seguem distribuições de Bernoulli, tais que

P[X = 1] = P[Y = 0] = 0,9

então X + Y segue uma distribuição binomial com parâmetros n = 2 e p = 0,3, se X
e Y forem variáveis aleatórias independentes.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A distribuição binomial é caracterizada por repetições independentes de Ensaios de
Bernoulli, com o mesmo parâmetro p.
O enunciado informa que:

* P[X = 1] = 0,9, ou seja, a probabilidade de sucesso de X é px = 0,9.

* P[Y = 0] = 0,9, ou seja, a probabilidade de fracasso de Y é qv = 0,9.
Portanto, a probabilidade de sucesso de Y é: pY = 1-0,9 = 0,1
Como px #= pv, então X + Y não segue uma distribuição binomial.

Gabarito: Errado.

(2018 - Câmara de Goiânia) Considere uma variável aleatória X com distribuição binomial e parâmetros p =1/3 e n = 4. Qual é a probabilidade de X = 2?

a) 4/81

b) 1/9

c) 2/9

d) 8/27

Comentários:

A probabilidade P(X = k) de uma distribuição binomial é dada por:

P(X = fc) = Cn>k.pk.(l-p)n-k

Para p = 1/3, n = 4 e k = 2, temos:

P(X = 2}=JL A2 f2\2=4x3 1 4 = _8_

1 2I.2IA37 \3/ 2 '9'9 27

Gabarito: D

(2016 - ANAC) Em um determinado município, 70% da população é favorável a um certo projeto. Se uma amostra aleatória de cinco pessoas dessa população for selecionada, então a probabilidade de exatamente três pessoas serem favoráveis ao projeto é igual a a) 40,58%
b) 35,79%

c) 42,37%

d) 30,87%

e) 37,46%

Comentários:

Considerando que a pessoa pode ser favorável ou não (não há outra possibilidade) e que o resultado da seleção de uma pessoa não afeta o de outra, então temos uma distribuição binomial.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabemos que:

* a proporção de pessoas favoráveis é p = 70% = 0,7 (logo, q = 1 - p = 0,3); e

* serão selecionadas n = 5 pessoas.

Então, a probabilidade de selecionar k = 3 pessoas favoráveis, P(X = 3), é dada por:

P(X = fc) = Cn,k xpkx qn~k
P(X = 3) = C53 x (0,7)3 x (0,3)2

A combinação de 3 elementos, dentre 5, é:

r — 5_! — 5_x4x3!

— 5_x4

— 1 n

5,3 (5 — 3)! x 3! 2! x 3! 2

Assim, P(X = 3) é:

P(X = 3) = 10 x 0,343 x 0,09 = 0,3087 = 30,87%

Gabarito: D

(FGV/2018 - ALE/RO) Uma moeda é lançada quatro vezes. A probabilidade de saírem mais caras do que coroas é de
Comentários:

Para saírem mais caras do que coroas em 4 lançamentos de uma moeda, é necessário que saiam 3 OU 4caras. Assim, temos uma distribuição binomial com n = 4 e p = % (e também q = %).

A probabilidade de saírem k = 4 caras (4 sucessos e 0 fracasso) é:

= /c) = Cnk x pk x qn~k

A probabilidade de saírem k = 3 caras (3 sucessos e 1 fracasso) é:

P(X = 3)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Portanto, a probabilidade de obter 3 OU 4 caras, sabendo que são eventos mutuamente exclusivos, é:

Gabarito: B.

(VUNESP/2019 - TJ/SP) Em uma eleição, sabe-se que 40% dos eleitores são favoráveis ao candidato X e o restante ao candidato Y. Extraindo uma amostra aleatória, com reposição, de tamanho 3da população de eleitores, obtém-se que a probabilidade de que no máximo 1 eleitor da amostra seja favorável ao candidatoX é igual a a) 35,2%
b) 64,8%

c) 36,0%

d) 43,2%.

e) 78,4%

Comentários:

O enunciado informa que 40% dos eleitores são favoráveis a X (sucesso) e que os demais são favoráveis a Y(fracasso), ou seja, a seleção de uma pessoa ao acaso segue distribuição de Bernoulli.

Logo, a seleção de 3 pessoas com reposição (seleções independentes) configura uma distribuição binomial com n = 3ep = 0,4(q = l- p = 0,6).
Nessa distribuição, a probabilidade de encontrar k sucessos é dada por:

P(X = fc) = cnk xpkx qn~k

A probabilidade de obter no máximo 1 eleitor favorável corresponde a obter 0 ou 1 sucesso:

p = P(X = 0) + P(X = 1)

Para k = 0, temos:

P(X = 0) = C3,o x 0,4° x 0,63 = 1 x 1 x 0,36 = 0,216

Para k = 1, temos:

P(X = 1) = C3jl x 0,4x x 0,62 = 3 x 0,4 x 0,36 = 0,432

Assim, a probabilidade desejada é:

P(X = 0 U X = 1) = 0,216 + 0,432 = 0, 648 = 64,8%

Gabarito: B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Esperança e Variância

E quanto à esperança dessa distribuição?

Vamos considerar o experimento de lançar uma moeda 100 vezes. Quantos resultados "CARA"
você espera?
50, certo? Qual é a intuição por trás desse valor?

Se a probabilidade de sucesso é p e se estamos realizando esse experimento n vezes,
espera-se que o número de sucessos obtidos mantenha essa proporção. Ou seja, o valor esperado é:
E(X) = n x p

Para o exemplo dos 3 lançamentos de uma moeda, temos p = - e n = 3. Então, o número de vezes que esperamos obter a face CARA é:
z x 13E(X) = nxp = 3x- =l,5

Mas esse valor não é inteiro!

Tudo bem! Algumas vezes obteremos mais CARAS, outras vezes menos, de modo que, em média, obteremos1,5 CARA.

E a variância da distribuição binomial? A sua fórmula é:

V(X) = nxp x q

Para esse mesmo exemplo, com q = |, a variância é:

z x 1137 =nxpxq=3x-x-=-= 0,75

L L 4

E o desvio padrão é a raiz quadrada da variância:

DP(X) = Jn xpxq

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

INDO MAIS

FUNDO!

A combinação de k elementos, dentre n, é igual à combinação de n — k elementos, dentre

Cn,k Cn,n-k-

Ou seja, o número de maneiras de obter 0 sucesso é igual ao de obter n sucessos; o número de maneiras de obter 1 sucesso é igual ao de obter n — 1 sucessos; etc.
Assim, se tivermos p = q, a probabilidade de obter 0 sucesso será igual à probabilidade de obter n sucessos; a probabilidade de obter 1 sucesso será igual à de n — 1 sucessos etc.
Portanto, temos uma distribuição simétrica se p = q, isto é, se p = q = 0, 5, conforme ilustrado a seguir.
Quando a probabilidade de sucesso for maior p > 0,5, teremos uma distribuição assimétrica negativa, conforme ilustrado a seguir.
Analogamente, quando a probabilidade de sucesso for menor p < 0,5, teremos uma distribuição assimétrica positiva, conforme ilustrado a seguir.
Apesar de a distribuição binomial ser assimétrica sempre que p #= 0,5, sempre que o produto n x p for um número inteiro, esse será o valor da média, da mediana e da moda!
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ESQUEMATIZANDO

Distribuição Binomial (n,p)

n Ensaios de Bernoulli independentes, com probabilidade de sucesso p
P(X = k) = Cnk.pk.qn~k

Esperança: = n.p; Variância: 7(X) = n.p.q

Observe que:

* A esperança da binomial é igual a n vezes a esperança da Bernoulli; e

* A variância da binomial é igual a n vezes a variância da Bernoulli.

^(.^Binomial) ~ E (X Bernoulli)

V(XBinomial) ~ Bernoulli)

HORA»

i (2019 - Universidade Federal do Acre) Seja X uma variável aleatória com distribuição binomial de i
; parâmetros n e p. Então, pode-se dizer que a variância de X é dado por.

: a) n
:

I

b) n.p ic)n.p(l-p).j d) n.p2
í e) n.p2(l-p)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

A variância de uma variável com distribuição binomial é dada por:

V(X) = n.p.q = n.p. (1 — p)

Gabarito: C

(CESPE/2013 - TRT 17? Região) Em toda distribuição binomial, a média será menor que a variância.

Comentários:

Em uma distribuição binomial, a média é E(X) = n.p e a variância V(X) = n.p.q.
Como q < 1 (por ser uma probabilidade), então:

V(X) = n.p.q <n.p.l = E(X)

Portanto, a média é sempre maior que a variância.

Gabarito: Errado.

(2016 - IBGE) Quando um pesquisador vai a campo e aborda pessoas na rua para serem entrevistadas, o número de pessoas que aceita responder à pesquisa segue uma distribuição binomial.
Se o valor esperado dessa distribuição é 8, e sua variância é 1,6, então a probabilidade de uma pessoa aceitar responder à pesquisa é de a) 1,6%
b) 16%

c) 20%

d) 50%

e) 80%

Comentários:

O enunciado informa que o valor esperado de uma variável com distribuição binomial é E(X) = 8.
Sabendo que, para uma distribuição binomial, temos E(X) = n.p, então:

EQO = n.p = 8

n = -

p

O enunciado informa, ainda, que a variância é V(X) = 1,6.
Sabemos que:

Então:

V (X) = n.p.q = n.p.(l — p) = n.p — n. p2

V(X) = n.p — n.p2 = 1,6

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

g

Considerando que n = -, temos:

p

Gabarito: E.

8 8

= -.p--.p2 = 1,6

p p

8 — 8. p = 1,6

8.p = 6,4

p = 0,8 = 80%

; (FCC/2014 - Auditor Fiscal da SEFAZ/RJ) Sabe-se que:

: I. X é uma variável aleatória com distribuição binomial com média 2p e variância (2p-2p2).

: II. Y é uma variável aleatória com distribuição binomial com média 5p e variância (5p-5p2).I

i III. A probabilidade de X ser inferior a 2 é igual a 15/16.

I

: Nessas condições, a probabilidade de Y ser superior a 3 é igual a a) 3/1.024
b) 1/64

c) 5/512

d) 15/1.024

e) 7/512

i Comentários:

I

i Sendo X uma variável com distribuição binomial, com média 2p, então:

E(X) = nx.p = 2p i nx = 2
= O enunciado informa que a probabilidade de X ser inferior a 2 é P(X < 2) = 15/16, isto é:

P(X < 2) = P(X = 0) + P(X = 1) = 15/16

I

i Sabendo que a probabilidade da distribuição binomial é P(X = k) = Cn>k. pk. qn~k, então para n =
2,

P(X = 0) = C2j0.p°. q2 = 1 x 1 x q2 = q2 = (1 - p)2

P(X = 1) = C2jl. p1. q1 = 2. p. q = 2. p. (1 - p)

; Sabendo que a soma dessas probabilidades é igual a 15/16, então:

: (1-p)2 +2.p.(l-p) =^|

: 16

= 2 _
2 7 15

: 1 — 2p + p + 2.p — 2p =—

= ,

: P 16

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

: , 15

:
P2 = 1----------------- = ---------

: 16 16

: Extraindo a raiz de ambos os lados da equação, sabendo que p > 0, temos:

: 1

j P = í

= Sabendo que, para Y, temos E(Y) = 5.p, então o número n de repetições de Y é:

E(Y) = nY.p = 5p

I

nY = 5

A probabilidade de Y ser superior a 3 corresponde à probabilidade de Y ser igual 4 OU igual a 5:

P(Y > 3) = P(Y = 4) + P(Y = 5)

= Sabendo que p = % (logo q = 1 - p = %) e nY = 5, temos:

3? 1 3 15

PÇ.Y = 4) = C₅,₄ x (i

/lx5

P(Y = 5) = C₅,₅ x (J x

Assim, a probabilidade de Y ser superior a 3 é:

X

z) =SX4Í

3\° 1

-) = 1 X -r

.4/ 45

x - =

x 1 =

1024

1024

pfyZ > 31 =X--------1-5 1-

1 16 1

v 7 1024 1024 1.024 64

Gabarito: B

I

; (FGV/2022 - TCU) A média e a variância de uma distribuição binomial são,
respectivamente, 20 e 4. O

: número de ensaios (n) dessa distribuição é:

a) 20

b) 22
i c) 25

d) 50

í e) 100

; Comentários:

i Segundo o enunciado, a média de uma distribuição binomial é igual a 20 e a variância é igual a 4:

E(X) = nxp = 20

= V(X) = nxp x q = 4

A fórmula da variância é igual à da esperança, multiplicada por q:

I

: V(JO ={nx px q = E(X) x q

: Sabendo que E(X) = 20 e que V(X) = 4, podemos calcular a probabilidade de fracasso:

y(X) = 20 x q = 4

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A probabilidade de sucesso é complementar:

B

4 1

q ~ 2Õ~ 5

B

;
1 4

| P=1-'=1-5=5

; Sabendo que EQO = n x p = 20, podemos calcular o número n de ensaios:

B

£(%) = n x - = 20

Gabarito: C

20 5 100

n = -7- = 20 x - = —— = 25
4 4 4

a

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçÃo GEoMÉTRICA

Assim como a distribuição binomial, a distribuição geométrica também se baseia em
Ensaios de Bernoulli independentes com a mesma probabilidade de sucesso p.
Porém, a variável com distribuição geométrica corresponde ao número de ensaios até o primeiro sucesso.
Por exemplo, suponha que iremos lançar um dado até obter a face 6, que será o nosso sucesso. Essa distribuição estuda, nesse caso, o número de lançamentos que teremos que efetuar até obtermos essa face pela primeira vez.
Assim, se o valor da variável forX = 1, teremos realizado 1 ensaio (ou tentativa)
até a obtenção do primeiro sucesso; se o valor for X = 2, teremos realizado 2 ensaios até a obtenção do primeiro sucesso,...
De maneira geral, X = k corresponde à realização de k ensaios até o primeiro sucesso.

Portanto, a probabilidade P(X = k), equivale à probabilidade de se obter, nesta ordem,
k — 1 fracassos e,
na /c-ésima tentativa, 1 sucesso. Ou seja, temos a interseção desses eventos independentes.

Assim, considerando que a probabilidade de cada fracasso é q e a probabilidade do sucesso é p, então a probabilidade P(X = k) é o produto das probabilidades:
P(X = k) = q.q.q.qq.p

' 1 1

k — 1 fracassos

TOME

NOTA!

P(X = k) = qk \p

Por exemplo, sabendo que a probabilidade de obtermos uma determinada face do dado
(sucesso) é p = -,

e que a probabilidade de não a obter (fracasso) é q = -, então a probabilidade de efetuarmos k = 3
lançamentos do dado até obtermos o primeiro sucesso (ou seja, obtermos fracasso nas 2
primeiras tentativas e sucesso na 3^) é:
P(X = 3)

/5\2 1 25

\6/ X 6 216

Observe que, conhecendo p (e, portanto, q = 1 —p), podemos calcular a probabilidade de qualquer valor de X, isto é, toda a distribuição de probabilidade da variável. Portanto, o único parâmetro da distribuição geométrica é a probabilidade de sucesso p e, assim, representamos essa distribuição por X~Geo(p).
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

É importante pontuar que é sempre possível ter que realizar o experimento mais uma vez até obter o primeiro sucesso. Por exemplo, no lançamento de um dado, com p = l/g, seria possível termos que lançar o dado 10 vezes até obter a face desejada? Sim! A probabilidade dessa situação seria:
P(X = 10) = (I) x| = 3,2%

E 50 vezes? Seria possível? Pode ser improvável, mas possível é, com a seguinte probabilidade:

P(X = 50) = q49.p = 0,0018%

Ou seja, não há limite para a variável com distribuição geométrica - ela é uma variável discreta, mas infinita.A variável pode assumir qualquer valor no intervalo [1, oo) - ela não pode ser menor que um, pois, no mínimo, faremos 1 lançamento para obter 1 sucesso.
Para calcular a probabilidade de a variável assumir um número maior ou igual a k, pela probabilidade complementar:
P(X > fc) = 1 - P(X < fc)

A probabilidade P(X < /c) pode ser calculada pela soma:

P(X < fc) = P(X = 1) + P(X = 2) + + P(X = /c - 1)

Por exemplo, a probabilidade de precisar de pelo menos 3 tentativas até obter determinada face do dado (sucesso) pode ser calculada como:
P(X > 3) = 1 - P(X = 1) - P(X = 2)

A probabilidade de obter sucesso na 1- tentativa é:

P(X = 1) = Q

A probabilidade de obter sucesso na 2^ tentativa é:

0 1 i

X - =

6 6

P(X = 2) = (|)Ixl =

_5_

Assim, a probabilidade de precisar de pelo menos 3 tentativas é:

P(X > 3) = 1 -1 - - = = -

6 36 36 36

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Esperança e Variância

Vamos deixar a nossa imaginação fluir! No caso da moeda, sabendo que há 50% de chance de o resultado ser CARA, quantas vezes você espera lançar a moeda até obter a face CARA? 2, certo?(Se a sua intuição não concorda comigo, não se preocupe!)
De modo geral, para uma variável geométrica com probabilidade de sucesso p, temos:

E a variância é:

Para o exemplo do dado, o número esperado de lançamentos até obter determinada face, com p i ,
= - e:

E(X) = -

p z , 1 6
E(X) = y = 1 x - = 6

E a variância, sabendo que q = 1—p = -,é:

vm=4

V(X) = —f X (7) = 5 x 6 = 30

G) 6 u

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

INDO MAIS

FUNDO!

É possível parametrizar a variável geométrica de uma outra maneira: a variável Y pode corresponder ao número de fracassos até o primeiro sucesso.
Ou seja, sendo Y = 3 temos 3 fracassos até o primeiro sucesso (obtido na 4? tentativa).

Com essa parametrização a variável pode assumir os valores Y =
{0,1,2,3,...incluindo o valor zero, uma vez que é possível obter sucesso na 1- tentativa.
Nessa situação, a probabilidade de Y = k é calculada como:

P(Y = k) = qk.p

Ou seja, elevamos a probabilidade de fracasso a k, e não a k - 1, como antes.
Com essa parametrização, a variância é a mesma!

E(n = A

Mas a esperança é um pouco diferente:

£(y) = -

p

Como as probabilidades dessa parametrização são q vezes as probabilidades da outra, a esperança dessa parametrização corresponde à esperança da outra parametrização,multiplicada por q.

9<!>P

ESQUEMATIZANDO

Distribuição Geométrica (p)

Número de Ensaios de Bernoulli até o primeiro sucesso

P(X = k~) = qk^.p

Esperança: E(X) = Variância: 7(X) =

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

r i
(2018 - IPM) Marque a alternativa correta em relação ao modelo probabilístico que mais se adequa ao seguinte caso: lançamento de uma moeda honesta, contando o número de casos até a realização da primeira coroa:
a) Poisson.

b) Geométrica.

c) Hipergeométrica.

d) Uniforme Discreta.

e) Pareto.

Comentários:

Ensaios sucessivos e independentes de Bernoulli até o primeiro sucesso caracterizam a distribuição geométrica.
Gabarito: B

(2018 - IPM) Sabe-se que a distribuição geométrica pode ser interpretada como uma sequência de ensaios de Bernoulli, independentes, até a ocorrência do primeiro sucesso. Assinale a alternativa que indica corretamente a média e a variância, respectivamente, de uma distribuição geométrica cujo parâmetro é p =0,64 e tendo como parametrização o número de ensaios de Bernoulli até se obter um sucesso.
a) 1,56; 0,78

b) 1,56; 0,88

c) 0,56; 0,88

d) 0,56; 0,78

e) 1,56; 0,68

Comentários:

A média de uma distribuição geométrica, com p = 0,64, é dada por:

Mp = F(EX()X=) - = - = ^r = 1,56

p 0,64

E, sabendo que q = 1 - 0,64= 0,36, a variância é:

2 =JL =

Gabarito: B

0,36

p2 (0,64)2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FGV/2017 - Prefeitura de Salvador) Abel tem uma moeda que dá "cara" com probabilidade
1/2 e Breno tem uma moeda que dá "cara" com probabilidade 1/3. Abel e Breno lançam suas respectivas moedas,alternadamente. O primeiro que obtiver "cara", ganha. Abel é o primeiro a lançar, e os lançamentos são todos independentes.
A probabilidade de Abel ganhar no seu terceiro lançamento é de:

Comentários:

A probabilidade de Abel, que é o primeiro a lançar, ganhar em seu 39 lançamento corresponde a ele obterCARA exatamente em seu 3- lançamento E Breno obter COROA em seus l9 e 29 lançamentos.

O enunciado informou que a probabilidade de Abel obter CARA (sucesso) é p = -, logo a probabilidade de obter COROA (fracasso) é complementar q = 1 — p = -.
Assim, a probabilidade de Abel obter CARA (sucesso) exatamente no 39 lançamento corresponde a uma distribuição geométrica com k = 3:
P(X = k) = qk_1.p

PW=P(X = 3) = (/2.p = y x- = -

0 enunciado informou que a probabilidade de Breno obter CARA (sucesso) é p = -, logo a probabilidade de obter COROA (fracasso) é complementar q = 1 — p = -.
Assim, a probabilidade de Breno obter COROA no l9 E 29 lançamentos é:

2 2 4

= Q.g = - X - = -

Portanto, a probabilidade de Abel ganhar no 3g lançamento corresponde à interseção desses 2
eventos

(produto das probabilidades):

14 1 1

P(4) x P(fi) = x^ = = _

8 9 2 x 9 18

Gabarito: E

(CESPE/2016 - TCE/PA) Considere que Y seja uma variável aleatória geométrica que representa o número de erros cometidos por um atendente no preenchimento de formulários e que a função de probabilidade deY seja definida por P(Y = k) = 0,9 x (0,l)k, em que k = 0,1, 2,... A partir dessas informações, julgue o item que se segue.
O desvio padrão da variável Y é inferior a 1.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Observa-se que a questão apresenta a segunda forma de parametrização da distribuição geométrica, da forma: P(Y = k) = qk.p, com k = 0, 1, 2,..., sendo q = 0,1 e p = 0,9.
A variância (que não se altera com o tipo de parametrização) é dada por:

q 0,1 0,1 10

~p*~ (0,9)2 Õ81 _ 81
O desvio padrão, raiz quadrada da variância, é dado por:

i a = = — =
0,35 i

Ê Gabarito: Certo.

I

I

I

I

i (CESPE/2019-TJ-AM/Analista Judiciário) É igual a 3/4 a probabilidade de determinado advogado conseguir decisão favorável a si em cada petição protocolada por ele na vara cível de certo tribunal. O plano desse i
= advogado é protocolar, sequencialmente, 12 petições nessa vara cível durante o ano de 2020.
Favoráveis ou

= não, as decisões do tribunal para petições são emitidas na mesma ordem cronológica em que são i
I

: protocoladas e são sempre independentes entre si.
i

I

I

A partir dessa situação hipotética, julgue os próximos itens, considerando as variáveis aleatórias
X e Y, em j que X = quantidade de decisões emitidas pelo tribunal até que ocorra a primeira decisão não favorável ao i i advogado, e Y = quantidade de decisões emitidas pelo tribunal favoráveis ao advogado.i

I

: Espera-se que a primeira decisão desfavorável ao advogado ocorra somente depois de,
pelo menos, quatro i decisões favoráveis a ele.i i Comentários:
= Note que a questão pede o número de decisões favoráveis (fracasso) até a primeira decisão desfavorável ;
= (sucesso). Para essa parametrização, o valor esperado da distribuição geométrica é:
i

E(X) = -

P

A probabilidade de fracasso (decisão favorável) é q = %, conforme enunciado.
i

I

I

: Assim, a probabilidade de sucesso (decisão desfavorável) é complementar: p = 1 - q = %.
;

= Logo, a esperança é:
i

3/

£(X) = j-4 = 3

j
/4 j

= Ou seja, espera-se que haja 3 decisões favoráveis até a primeira decisão desfavorável.

I

: Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Propriedades

Existem 2 propriedades da distribuição geométrica que são moderadamente cobradas nas provas:

i) P(X > t + s|X > s) = P(X > t)

Essa propriedade afirma que, sabendo que já houve s ou mais tentativas, então a probabilidade de haver mais que t tentativas a mais, até o primeiro sucesso, é igual à probabilidade de haver mais que t tentativas,até o primeiro sucesso, independentemente das tentativas anteriores.

Por exemplo, sabendo que eu já lancei a moeda mais que s = 10 vezes e não obtive
CARA (sucesso), então qual é a probabilidade de eu precisar lançar a moeda mais que t = 4 vezes a mais até obter CARA? É igual à probabilidade de eu ter que lançar a moeda mais que t = 4 vezes até obter CARA!
Essa propriedade está associada à "falta de memória" ou "falta de desgaste" da distribuição geométrica. Ela afirma que não importa quantas tentativas já foram feitas, as probabilidades dos próximos resultados se mantêm as mesmas.
P(X=fc)

ü) P(X>fc) = p

Essa propriedade também decorre de uma probabilidade condicional, mas "disfarçada".

Considerando que X = k pode ser considerado o resultado da interseção entre X = k e
X > k, então a fração à esquerda da igualdade pode ser escrita como:
P(X = /c)

P(X > /c)

P(X = knX > k)
P(X > k)

= P(X = k\X > k)

Ou seja, podemos reescrever essa propriedade da seguinte forma:

= k\X>k) =p

Essa expressão significa o seguinte: sabendo que eu vou precisar de pelo menos k tentativas até o primeiro sucesso (isso porque já foram feitas k - 1 tentativas sem sucesso), então a probabilidade de obter sucesso na fc-ésima tentativa é igual a p.
Ora, p é a probabilidade de obter sucesso em uma tentativa qualquer! Inclusive, na
/c-ésima tentativa! Ou seja, temos mais uma propriedade associada à falta de memória (ou de desgaste) da distribuição geométrica.
Mas, reorganizando a expressão original dessa segunda propriedade, temos:

P(X > fc) =

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com isso, podemos calcular P(X > k) facilmente, em vez de fazer P(X > fc) = 1 —
P(X < k), o que pode ser trabalhoso, dependendo do valor de k.
Por exemplo, para calcular a probabilidade de serem necessárias pelo menos 3 tentativas até obter determinada face do dado pela primeira vez, sendo p = - e q = -, primeiro calculamos a probabilidade de
6 6

precisar de k = 3 tentativas:

P(X = 3)

Assim, a probabilidade de precisar de pelo menos 3 tentativas é obtida dividindo esse resultado por p = -:
z A P(X = 3)

P(X > 3) = —-------------- -

p r \ 216 25 25
p(x>3)=^ = —x6 = -

Este é exatamente o resultado que obtivemos calculando P(X > 3) = 1 — P(X = 1) — P(X = 2)1

De maneira geral, sabendo que P(X = k) = qk x. p, então podemos escrever a fórmula como:

P(X >k) =

P(X = k)

P

qk 1.p p
P(X >k) = q1*-1

HORA»

i (FGV/2019 - DPE/RJ) Para que as pessoas que aguardam atendimento em uma repartição pública fiquem i
; acomodadas com relativo conforto, é necessário que o recinto seja dimensionado à razão de um metro i quadrado de espaço para cada cidadão em espera.i

I

I

: Se o número de pessoas que comparece, por dia, tem distribuição geométrica, com parâmetro p = 0,2, é =í correto afirmar que:
i

: a) em função da distribuição do número de pessoas, o tamanho médio ideal do recinto deve ser de 16 metros =
= quadrados;

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

b) a probabilidade de que uma sala de espera com 4 metros quadrados não seja confortável em certo dia é(0,2).(0,8)4;

c) a probabilidade de que uma sala com 3 metros quadrados fique subutilizada em certo dia é igual a
0,448;

d) considerando uma sala de espera que tem 20 metros quadrados e o fato de que 18
pessoas já estão aguardando, a probabilidade de que atinja sua lotação exata é igual a 0,16;
e) a distribuição de probabilidade do tamanho (A) de sala ideal, a cada dia, é dada por P(A = x) =(0,2)2.(0,8)2x para X = 1,2,3,....

Comentários:

Sabendo que X é uma variável que segue uma distribuição geométrica com parâmetro p =
0,2 e que o recinto deve ter lm2 para cada cidadão, então:
Em relação à alternativa A, o tamanho médio ideal corresponde à média E(X):

. 1 1

= FQO = - = — = 5

P 0,2

Sabendo que uma sala de 5 m2 atende, em média, esse é o tamanho ideal. Logo, alternativa A está incorreta.
Em relação à alternativa B, a probabilidade de uma sala com 4m2 não ser adequada é igual à probabilidade de chegarem mais que 4 pessoas, ou seja, X > 5:
z , P(X = fc)

P(X > k) = = q

P

P(X > 5) = (0,8)4

fc-i

A" alternativa forneceu a resposta para P(X = 5) = (0,8)4.0,2. Entretanto,
essa é apenas uma das possibilidades de a sala não ser adequada. Portanto, a alternativa B está incorreta.
Em relação à alternativa C, para que uma sala de 3m2 fique subutilizada, é necessário ter X < 3:

P(X < 3) = P(X = 1) + P(X = 2) = p + q.p = 0,2 + 0,8 x 0,2 = 0,2 + 0,16 = 0,36

Em relação à alternativa D, sabendo que há 18 pessoas aguardando, então a probabilidade de atingir a lotação de 20m2 é igual à probabilidade de chegarem 2 pessoas a mais, que é igual à probabilidade de chegarem X = 2 pessoas (propriedade da falta de memória):
P(X = 2) = 0,8 x 0,2 = 0,16

A distribuição de probabilidade do tamanho da sala é igual à distribuição de probabilidade das pessoas que chegam, dada por:
P(X = k) = (0,8)fcl x 0,2 para k = {1,2,3,...}

Gabarito: D.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçÃo HIPERCEoMÉTRICA

A Distribuição Hipergeométrica considera uma população de elementos com dois possíveis atributos(sucesso ou fracasso), isto é, uma população com distribuição de Bernoulli, da qual será selecionada uma amostra de alguns elementos, assim como a distribuição binomial.
Porém, diferentemente desta, na distribuição hipergeométrica, a população é finita e a amostra é extraída sem reposição, ou seja, as extrações não são independentes.
Vamos chamar o tamanho da amostra de n e o tamanho da população de N. Dessa população, S elementos possuem o atributo sucesso e, consequentemente, N — S elementos possuem o atributo fracasso.
Esses três parâmetros N,S,n caracterizam a distribuição geométrica e, assim, podemos representá-la como
X~Hgeo(N,S,n).

Por exemplo, vamos supor que haja N = 10 peças, no total, das quais S = 4 peças sejam defeituosas(sucesso), logo, haverá N-S = 10-4 = 6 peças não defeituosas (fracasso).

Se formos extrair n = 3 peças sem reposição, então o número de peças defeituosas
(sucesso) encontradas na amostra seguirá uma Distribuição Hipergeométrica.
A probabilidade de haver k elementos com o atributo sucesso na amostra (e,
consequentemente n — k com o atributo fracasso) é dada por:
P(X = fc)

Vamos entender essa fórmula. Pela definição clássica de probabilidade, temos:

PQ4) =

número de casos favoráveis número total de casos n(A)
n(lT)

No denominador, constam todas as maneiras de selecionarmos n elementos, dentre N (sem importância de ordem), ou seja, temos a combinação de n elementos, dentre N:
No numerador, temos, de um lado, a quantidade de maneiras de selecionar k elementos com o atributo sucesso, dentre S elementos, no total.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ademais, temos a quantidade de maneiras de selecionar n — k elementos com o atributo fracasso, dentre
N — S, no total.

Em seguida, multiplicamos esses dois resultados para obter o número de casos favoráveis (princípio multiplicativo):
)

EXEMPLIFICANDO

Suponha que haja N = 10 peças, no total, das quais S = 4 peças sejam defeituosas. Se retirarmos n = 3 peças sem reposição, a probabilidade de encontrar k = 2 defeituosas é:
P(X = fc)

Vamos calcular cada combinação separadamente. No denominador, temos todas as maneiras de escolher n = 3 peças, dentre N = 10 peças, no total:
JV\ _ /10\ _ io!

Jl/~ \ 3 / (10—3)13!

10x9x8x7!

7!x3!

10x9x8
3x2x1

= 10 X 3 X 4 = 120

No numerador, temos, de um lado, a quantidade de maneiras de escolher k = 2

defeituosas, dentre S = 4 defeituosas, no total:

(4—2)!2!

4X3X2!

2!x2!

Ademais, temos a quantidade de maneiras de escolher n — k = 3 — 2 = 1 peça não defeituosa, dentre N — S = 10 — 4 = 6 não defeituosas, na população:
(N - = /6\ = 6! 6X5! ,

Vn - fc/ \1/ ~ (6-1)11! " 5!xl!

Pelo princípio multiplicativo, o numerador é:

x 6 = 36

Assim, a probabilidade de retirar k = 2 defeituosas é:

P(X = 2) = — = — = 30%

7 120 10

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em vez de aplicarmos essa fórmula, podemos calcular as probabilidades a cada extração.
Para o nosso exemplo, podemos calcular a probabilidade de encontrar k = 2 peças defeituosas, em uma amostra de tamanho n = 3, da seguinte forma:
i) Pt: Probabilidade de retirarmos a primeira peça não defeituosa. Sabendo que há JV — S =
peças não defeituosas dentre N = 10 peças no total, então:

ii) Pa: Probabilidade de retirarmos a segunda peça defeituosa, dado que a primeira peça foi não defeituosa. Sabendo que há S = 4 peças defeituosas dentre 9 peças no total, então:
iii) Píí£: Probabilidade de retirarmos a terceira peça defeituosa, dado que foi retirada uma peça não defeituosa e outra defeituosa. Sabendo que restam 3 peças defeituosas dentre 8peças no total, então:
Como todos os 3 eventos ocorrem (interseção), então pela Teoria da
Probabilidade, multiplicamos as 3
probabilidades.

Porém, considerando que a ordem das extrações não precisa ser essa, devemos multiplicar o resultado pela quantidade de maneiras de "escolher" qual será a extração da peça defeituosa1. Como há3 peças, no total,
das quais 1 é não defeituosa, temos 3 possibilidades:

3! 3x2!

(3 - 1)! x 1! 2! x 1!

Assim, a probabilidade de encontrar k = 2 peças defeituosas, é:

1 Se preferir, você pode raciocinar que devemos multiplicar as probabilidades pelo número de maneiras de reordenar as extrações,o que corresponde à permutação das 3 peças, com repetição de 2 peças defeituosas:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Esse raciocínio pode ser aplicado para qualquer valor de X, porém, é necessário se atentar ao fato de que a ordem das extrações não importa e, por isso, as probabilidades calculadas devem ser multiplicadas pela combinação correspondente. Além disso, para uma amostra grande, essa segunda maneira de calcular pode se tornar bastante trabalhosa.
INDO MAIS

FUNDO!

Agora, vamos ver quais são os limites mínimos e máximos da variável hipergeométrica.

Limite Superior: maior número possível de sucessos na amostra

Se o número total de sucessos existentes S for maior que o tamanho da amostra n, ou seja, se n < S, então o valor máximo que X pode assumir é n.
Por exemplo, se houver S = 4 peças defeituosas (sucesso) e o tamanho da amostra for de n = 3, então o valor máximo de peças defeituosas selecionadas será n = 3.
Caso contrário, ou seja, se o tamanho da amostra n for maior do que o número total de sucessos S, então o valor máximo que X pode assumir é S.
Por exemplo, havendo S = 4 peças defeituosas e o tamanho da amostra for n = 8 então o valor máximo de peças defeituosas que podem ser selecionadas será S = 4.
Logo, o limite superior da variável é o menor valor entre n e S:

k < min {n, 5}

Limite Inferior: menor número possível de sucessos na amostra

Se o número total de fracassos existentes, N - S, foi maior que o tamanho da amostra n,ou seja, se n < N — S, então todas as peças selecionadas podem ter o atributo fracasso e,portanto, o número mínimo que X pode assumir é 0.

Por exemplo, vamos supor que haja N = 10 peças e 5 = 4 peças defeituosas (sucesso),
logo, N-S = 6 peças não defeituosas (fracasso). Se o tamanho da amostra for de n =
peças, então todas as peças selecionadas podem ser não defeituosas (fracasso), ou seja,
é possível obter X = 0 sucessos.
Caso contrário, ou seja, se o tamanho da amostra n for maior que o número total de fracassos existentes, então o número máximo de fracassos será o total de fracassos existentes, N — S. Assim, o número mínimo de sucessos será a diferença entre o tamanho da amostra n e o máximo de fracassos N — S:
n — (N — S~)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por exemplo, supondo as mesmas N-S = 6 peças não defeituosas (fracasso), mas uma amostra de tamanho n = 8 peças, então o número máximo de peças não defeituosas(fracasso) que podem ser selecionadas é o número total existente, isto é, N-S = 6.

Assim, o número mínimo de peças defeituosas (sucesso) que podem ser selecionadas é a diferença entre o tamanho da amostra e esse limite:
n — (N — S) = 8- 6 = 2

Pontue-se que essa diferença será negativa na primeira situação, em que há mais fracassos existentes do que elementos na amostra. Para o nosso exemplo com a amostra de tamanho n = 3 peças, essa diferença será:
n — (N - S) = 3 - 6 = -3

Dessa forma, o limite inferior da variável é o maior valor entre 0 e n — (W — S).

k > max{0, n- (N - $)}

Portanto, os limites da variável são:

max {0, n - (N - $)} < k < min {n, $}

Esperança e Variância

Em relação ao valor esperado, vamos voltar ao nosso exemplo, em que S = 4 peças são defeituosas, de um total de N = 10 peças. Ou seja, a proporção de peças defeituosas é:
Então, se eu selecionar 5 peças (metade da população), espero que 2 sejam defeituosas
(metade da amostra),
certo? Ou seja, espero que a proporção de defeito (sucesso) na amostra seja a mesma de toda a população.
Isso significa que a esperança é dada pela seguinte fórmula:

E(X) = n.p

Em que p é a proporção de sucessos na população:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para o nosso exemplo com N = 10 peças no total, das quais S = 4 peças são defeituosas, a proporção de sucessos na população é:
S 4

P = ÃÍ = TÕ = 0'4

Considerando que vamos retirar uma amostra de n = 3 peças, o valor esperado é:

£(%) = n.p = 3 x 0,4 = 1,2

Observe que a esperança da distribuição hipergeométrica é a mesma da distribuição binomial (associada a seleções independentes)!
A variância, entretanto, fica um pouco diferente:

V(X) =

Em que q = 1 - p.

Para o nosso exemplo, com N = 10 e S = 4, a proporção de fracassos na amostra é:

q = 1 - p = 1 — 0,4 = 0,6

Então, sendo n = 3, a variância da variável é:

z x N — n 10-3
7V(X) = = 3 x 0,4 x 0,6 x = 3 x 0,24 x - = 0, x 7 = 0,56

Observe que a variância da distribuição hipergeométrica é igual à da distribuição binomial, n. p.
q, "corrigida"

/V—n pelo fator Esse fator é chamado fator de correção para população finita.
Esse fator é sempre menor que 1 (pois N - n < N - 1), logo, o fator de correção diminui a variância da distribuição.
Ele se aproxima de 1 quando o tamanho da população N é muito maior que o tamanho da amostra n. Nessa situação, a distribuição hipergeométrica pode ser aproximada à distribuição binomial.
É por esse motivo que podemos utilizar a distribuição binomial, mesmo para amostras extraídas com reposição, quando a população é suficientemente grande.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ESQUEMATIZANDO

Distribuição Hipergeométrica (N,S,ri)

Extrações sem reposição de elementos com 2 atributos

P(X = fc)

Esperança: £(X) = n.p; Variância: V(X) = n.p.q^^

HORA»

r*

: (FCC/2015 - DPE/SP -Adaptada) Julgue o item a seguir:

A distribuição hipergeométrica é adequada quando consideramos extrações casuais feitas sem reposição de
= uma população dividida segundo dois extratos.

i Comentários:

I

A distribuição hipergeométrica estuda as extrações, sem reposição, de uma população com 2 atributos

= (sucesso ou fracasso).

Resposta: Certo.

E

i (FCC/2015 - TRT 3- Região - Adaptada) Julgue o item a seguir:

A distribuição hipergeométrica é uma distribuição de probabilidade discreta que depende de 3
parâmetros.

I

i Comentários:

I

: A distribuição hipergeométrica depende dos parâmetros N (total da população), S
(total de elementos com í o atributo sucesso) e n (número de extrações).
= Resposta: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= (FGV/2022 - TJDFT) A Vara Cível de determinada comarca realiza 200 audiências por mês. No mês passado,
: em 120 audiências o autor era assistido pela Defensoria Pública e, nas outras 80
audiências restantes, o demandante esteve representado por advogado particular.

: Sorteiam-se, aleatoriamente e sem reposição, 80 audiências desse último mês. O número mais provável de
; audiências em que atuam os defensores públicos é de:

a) 48

b) 49

c) 50

d) 51

e) 52

j Comentários:

: Nessa questão, a população de 200 audiências é segregada em assistência por
Defensoria Pública (sucesso)

= e por advogado particular (fracasso).

: Considerando que uma amostra de 80 audiências é extraída sem reposição, concluímos que as extrações são i dependentes, o que caracteriza uma distribuição hipergeométrica.
A média (ou esperança) dessa distribuição é dada por:

I

i
E(X) = n x p

A probabilidade de sucesso é a razão entre o número de audiências em que o autor é assistido pela
= Defensoria Pública (120) e o número total de audiências no mês (200):

= 120

P ~ 2ÕÕ " °'6

= Sabendo que o tamanho da amostra é n = 80, a esperança é:

E(X) = 80 x 0,6 = 48

j Gabarito: A

; (2013 - TRE/MG) Em uma população finita de tamanho N, onde existem k indivíduos com uma característica de interesse, ao se selecionar uma amostra aleatória de tamanho n sem reposição, o número de indivíduos
; com a característica na amostra (R) é uma variável aleatória com distribuição hipergeométrica. A

; probabilidade de se ter exatamente r indivíduos na amostra com a característica de interesse é dada por pr = , onde max (0, n - N + k) = r = min (k, n).
Analise:

I. Para N = 100, k = 20, n = 10 e r = 3, E(R) = 2 e Var(R) = 144/99.

! II. Para N = 100, k = 20, n = 5 e r = 3, E(R) = 1 e Var(R) = 8/10.

í III. Para N = 10000, k = 2000, n = 100 e r = 3, E(R) = 20 e Var(R) = 15,84.
IV. Para N = 10000, k = 1000, n = 100 e r = 3, E(R) = 10 e Var(R) « 9.

i V. Para N = 10000, k = 2000, n = 10 e r = 0, P(R = 0) « 0,1074.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Estão corretas apenas as alternativas a) I e II.
b) II e IV.

s e) II, III, IV eV
s

Comentários:

Em relação à afirmativa I, o total de elementos da população é N = 100, o número de sucessos da população(que chamamos de S) é k = 20, então a proporção de sucessos é:

p ~ lõõ _ 0,2

Sendo n = 10 o tamanho da amostra, então a esperança é:

= n.p = 10x0,2 = 2

Sabendo que a proporção de fracassos é q = 1 - p = 0,8, então a variância é:

_ N — n 90 144

VW = n.p.q.-^—^ = 10 x 0,2 x 0,8 x — = —

Portanto, a afirmativa I está correta.

Em relação à afirmativa II, o total de elementos e o número de sucessos da população são os mesmos, assim p = — = 0,2eq = l- p = 0,8.
r 100 M

Agora, a amostra tem tamanho n = 5, então a esperança é:

s

£(%) = n.p = 5 x 0,2 = 1

E a variância é:

z x N — n 95 76

V(X) = n.p. q.—- = 5 x 0,2 x 0,8 x — = — = 0,7676 ...

Portanto, a afirmativa II está errada.

Em relação à afirmativa III, o total de elementos da população é N = 10.000 e o número de sucessos da população é k (ou S) = 2.000. Assim, a proporção de sucessos é:
2.000

P ~ 10.000 _ 0,2

E a proporção de fracassos é q = 1 - p = 0,8. Sendo o tamanho da amostra n = 100, então, a esperança é:
I

E(X) = n.p = 100 x 0,2 = 20

E a variância é:

I

z „ N — n 9900 16 x 1100

= n.p.q.jj—^ = 100 x 0,2 x 0,8x —

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

* 05152001900 - Everton
Murilo Vieira

Portanto, a afirmativa III está correta.

Em relação à afirmativa IV, o total de elementos é N = 10.000 e o número de sucessos da população é fc(ouS) = 1.000. Assim, a proporção de sucessos é:
1.000

P ~ 10.000 _ 0,1

E q = 1 - p = 0,9. Sendo o tamanho da amostra n = 100, a esperança é:

£(%) = n.p = 100 x 0,1 = 10

E a variância é:

z x N — n

9900 9 x 1100

= 100 x 0,1 X 0.9 x — =

= 8,91 = 9

Portanto, a afirmativa IV está correta.

Em relação à afirmativa V, temos N = 10.000, k (ou S) = 2.000 e n = 10.

Para calcular o valor exato da probabilidade de não obter sucesso na amostra P(R = 0), faríamos:

O que é bastante trabalhoso. Porém, como o tamanho da amostra n = 10 é muito menor que o tamanho da população N = 10.000, podemos aproximar essa distribuição a uma binomial. A proporção de sucessos na amostra é:
2.000

P = 10.000

E de fracassos é q = 1 - p = 0,8. Assim, a probabilidade de não obter sucessos na amostra é aproximadamente:
P(X=0) = q10 = (0,8)10 = 0,1074

Portanto, a afirmativa V está correta.

Gabarito: D.

L

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçÃo DE PoISSoN

A Distribuição de Poisson descreve a probabilidade de ocorrências aleatórias em determinado intervalo,
como o tempo, mas com uma taxa média constante.

O número de ligações recebidas por hora ou o número de clientes que comparecem diariamente em um estabelecimento são exemplos em que podemos aplicar a distribuição de Poisson.
Nessas situações, a probabilidade de o evento ocorrer em um instante específico
(determinado segundo, por exemplo) é tão baixa, que não é possível ocorrer mais de um evento ao mesmo tempo.Por isso, dizemos que a probabilidade de ocorrência p em uma distribuição de Poisson é muito pequena (tende a zero).
Por outro lado, o tamanho da amostra n, que corresponde ao "número de instantes" no intervalo desejado,como uma hora ou um dia, é muito grande (tende a infinito). Essa é outra característica importante da distribuição de Poisson.
Além disso, as ocorrências devem ser independentes uma das outras e devem assumir apenas números inteiros (não é possível receber meia ligação ou chegar meio cliente), assim como na distribuição binomial.Na verdade, a distribuição de Poisson é desenvolvida a partir da distribuição binomial,
considerando que o tamanho da amostra n tende ao infinito e a probabilidade de sucesso p tende a zero.
A Distribuição de Poisson também pode ser utilizada como uma aproximação da distribuição binomial,quando o tamanho da amostra n for muito grande e probabilidade de sucesso p for muito pequena. Nesses casos, o cálculo das probabilidades pela distribuição binomial pode se tornar muito trabalhoso.
IMAGINA?!

Vamos supor que uma indústria farmacêutica apresenta defeito em p = 1% dos medicamentos e que a amostra a ser verificada contém n = 400 medicamentos.
Como calcularíamos a probabilidade de encontrar 5 medicamentos defeituosos, utilizando a distribuição binomial?
P(X = 100) = C400;5 x 0,015 x 0,99395

Que seria extremamente trabalhoso.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em uma distribuição binomial, a média (ou esperança) é:

E(XBi) =n.p

Na distribuição de Poisson, denotamos essa média por A (chamamos essa letra de lambda), que é o único parâmetro da distribuição. Assim, nos referimos à distribuição de Poisson como X~Po(A).
A = n.p

Para o nosso exemplo, em que a probabilidade de defeito é p = 1% = 0,01 e a amostra contém n = 400medicamentos, o valor de A é:

Â = n.p = 400 x 0,01 = 4

Dessa forma, a média (ou esperança) da distribuição de Poisson é igual ao parâmetro
A, que representa o número médio de ocorrências (taxa de ocorrência) em determinado intervalo:
E(X) = A

Essa taxa de ocorrência deve ser constante no intervalo considerado (assim como a probabilidade de sucesso da distribuição binomial deve ser a mesma para todos os ensaios).
Na distribuição binomial, a média (ou esperança) é:

= n.p.q

Considerando que p tende a 0, então q = 1 — p tende a 1.

Desse modo, a variância da distribuição de Poisson é dada por:

V(X) = n.p

Como definimos A = n.p, a variância também é igual ao parâmetro:

V(X) = A

A probabilidade de ocorrerem k eventos no intervalo determinado, na distribuição de Poisson, é dada por:
P(X = k) = ^-

Em que e = 2,718 (número neperiano).

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

EXEMPLIFICANDO

Vamos supor o exemplo inicial da indústria farmacêutica, que produz p = 1% de medicamentos defeituosos e que será extraída uma amostra com n = 400 peças.
Vimos que o parâmetro da distribuição de Poisson é A = 400 x 1% = 4, que equivale à sua média e variância.
Com base no parâmetro, podemos calcular a probabilidade de haver, por exemplo, k = 1

medicamento com defeito na amostra:

pçx = k) =

e~À Ak

O-A /I1

P(X = l)=^ = 4.e-4

Se essa fosse uma questão de prova, a banca poderia apresentar a resposta dessa forma,
ou então informar que e-4 = 0,018. Assim, seria possível calcular:

P(X = 1) = 4 x 0,018 = 0,072.

Poderíamos calcular, ainda, a probabilidade de encontrar mais de 1 medicamento com defeito, que pode ser calculada pelo seu complemento:
P(X > 1) = 1 - P(X < 1) = 1 - P(X = 0) - P(X = 1)

Como já temos P(X = 1), precisamos calcular P(X = 0):

Logo:

P(X > 1) = 1 - e"4 - 4. e'4 = 1 - 5. e-4 = 1 - 5 x 0,018 = 1 - 0,09 = 0,91

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sim, você precisa memorizar a fórmula da probabilidade de Poisson, mas eu vou tentar te ajudar. Você precisa preencher os 5 espaços indicados abaixo:
pçx=k) =LJ

No 1Q espaço, você preenche o e:

P(x = k) = e'"ly

Agora, você vai preencher o lambda A (para lembrar, chame-o de L) no 2Q e 3Q espaços. No
25 espaço (acima do e), acrescente um sinal de menos (-):

P(X = k) =

Nos últimos espaços, preencha o k. No último espaço (denominador), acrescente o fatorial
(!):

p(x = k) =

Pronto! Então, não se esqueça da sequência ELK, de colocar um no expoente e um "!"
no denominador.

Assim como para a distribuição binomial, o valor de X = k, varia entre 0 e o tamanho da amostra n
->

Ressalte-se, ainda, que o coeficiente de assimetria e de curtose b₂ para essa distribuição são:

Sabendo que 2 > 0, então esses coeficientes são positivos.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ESQUEMATIZANDO

Distribuição de Poisson (2)

Aproximação da Distribuição Binomial para n -> oo ep -> 0

PÇX = k) =

Esperança: E(X) = A; Variância: V(X) = A

— PRATICAR! —

i (2011 - Transpetro) Uma distribuição discreta de probabilidade que fornece a frequência de ocorrência de :
= certos tipos de eventos aleatórios, podendo ser usada como aproximação da distribuição binomial,

= corresponde à distribuição

I

: a) geométrica j

I

b) hipergeométrica i
= c) normal d) uniforme

: e) de Poisson
;

I

I

i Comentários:

A distribuição que se aproxima à distribuição binomial, para n muito grande, com parâmetro À, isto é, a taxa i
= (ou frequência) de ocorrência é a distribuição de Poisson.
;

i Gabarito: E

I

I

I

I

i (2019 - IDAM) Sobre a distribuição de Poisson P(X=k; À) que representa a distribuição de frequências da ;
= variável aleatória X, analise as afirmativas abaixo, dê valores Verdadeiro (V) ou Falso (F).
;

I

i () P(X = k;X) = lim Binomial (X = k; N,p = -)
i i ( ) A distribuição de Poisson é útil na modelagem de processos de natureza binomial onde o evento tem =
= probabilidade de ocorrência (binomial), p, pequena (ou seja, tendendo a zero), porém o valor esperado da j
= variável aleatória fica finito devido a ser grande a quantidade da amostragem (testes).
i

I

I

: () O parâmetro À corresponde ao mesmo tempo ao valor esperado e à variância da distribuição de Poisson, =
= P(X=k; À).
í

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assinale a alternativa que apresenta a sequência correta de cima para baixo.

a) F, F, F

b) F, V, V

c) V, F, V

d) V, V, V

Comentários:

Em relação à primeira afirmativa, sabemos que a distribuição de Poisson corresponde à distribuição binomial para n -> oo. Sabemos, ainda, que A = n.p, logo:
Portanto, a primeira afirmativa é verdadeira.

Em relação à segunda afirmativa, sabemos que a distribuição de Poisson é utilizada como aproximação da distribuição binomial para amostras grandes (n) e probabilidade pequena (p), tal que o produto n.p, isto é, a esperança da distribuição, é um valor finito. Portanto, a segunda afirmativa é verdadeira.
Na distribuição de Poisson, temos E(X) = Var(X) = A. Portanto, a terceira afirmativa é verdadeira.

Gabarito: D

(2019 - IF-PA - Adaptada) Se uma variável X tem distribuição de Poisson com parâmetro 0, tal queX~Poisson(0), pode-se afirmar que:

a) E(X) = 0 e Var(X) = 1/®

b) E(X)= 1-0 e Var(X)= 0

c) E(X) = ® e Var(X)= 0

d) E(X) = 0/2 e Var(X) = 02/12

e) E(X) = 0 e Var(X) = ®2/12

Comentários:

Na distribuição de Poisson, sabemos que E(X) = Var(X) = A. O enunciado chamou o parâmetro de A = 0,então:

E(X) = Var(X) = 0

Gabarito: C

(CESPE/2018-ABIN/Oficial Técnico) A quantidade diária de emails indesejados recebidos por um atendente é uma variável aleatória X que segue distribuição de Poisson com média e variância desconhecidas. Para estimá-las, retirou-se dessa distribuição uma amostra aleatória simples de tamanho quatro, cujos valores observados foram 10, 4, 2 e 4. Com relação a essa situação hipotética, julgue o seguinte item.
Se P (X = 0) representa a probabilidade de esse atendente não receber emails indesejados em determinado dia, estima-se que tal probabilidade seja nula.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Para a distribuição de Poisson, a probabilidade P(X = 0) é dada por:

Gabarito: Errado.

e À.A° e À.l m = 0) = ""õT" = ~1~ = e~À*°
(FCC/2014 - TRT 13? Região) Suponha que o número de processos trabalhistas que chegam, por dia, a um determinado tribunal regional do trabalho seja uma variável aleatória com distribuição de Poisson com média igual a À. Sabe-se que a probabilidade de chegarem 2 processos por dia é igual a oito vezes a probabilidade de não chegar nenhum. Nessas condições, a probabilidade de, em um determinado dia,chegarem pelo menos 2 processos é igual a

Dados: e-2 = 0,135; e~4 = 0,018
a) 0,91

b) 0,36

c) 0,93

d) 0,46

e) 0,85

Comentários:

O enunciado informa que a probabilidade de chegar 2 processos é 8 vezes a probabilidade de não chegar processo algum:
P(X = 2) = 8.P(X = 0)

Considerando P(X = k) = , então:

Substituindo esses resultados na equação, temos:

Dividindo ambos os lados da equação por e Â, temos:

Â2 = 16

Sabendo que Â é positivo (pois, Â = n. p, com n > 0 e p > 0), então:

Â = 4

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)
ívivw. estrategiaconcursos. com. br

I= Nessas condições, a probabilidade de chegarem pelo menos 2 processos é (com as aproximações fornecidas
; pelo enunciado):

P(X > 2) = 1 - P(X < 2) = 1 - [P(X = 0) + P(X = 1)]

i P(X = 0) = e"A = e"4 s 0,018

: g-4 41

i p(x = 1) = ' = 4.
e"4 = 0,072

i Portanto:

i Gabarito: A.

P(X > 2) = 1 - P(X < 2) = 1 - 0,018 - 0,072 = 1 - 0,09 = 0,91

Algumas questões informam a taxa de ocorrência A para determinado intervalo (por dia,
por exemplo), e pedem a probabilidade associada a um intervalo diferente (por semana, por exemplo).Nessa situação, é necessário calcular a taxa de ocorrência para o intervalo desejado, mantendo-se a proporção constante:
A₁ = n₁xp->p = —

«1

A2 = n2 x p = n2 x —

Hl

Em outras palavras, multiplicamos a taxa de ocorrência Ax fornecida pela razão entre o intervalo desejado e o intervalo fornecido —.
Vamos supor que o número de clientes que chegam em um estabelecimento siga uma distribuição de Poisson com média = 10 clientes por dia. Para calcular a probabilidade de chegarem100 clientes em uma semana, por exemplo, precisamos primeiro calcular o número médio de clientes que chegam em 1 semanaA₂, considerando que 1 semana = 5 dias úteis:

A = 10 x — = 50

Para calcular a probabilidade de chegar 1 cliente em uma hora, primeiro calculamos o número médio de clientes que chegam em 1 hora, considerando que 1 dia = 8 horas úteis: 1 * *
A₃ = 10 x-= 1,25

O

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos, ainda, calcular o tempo médio entre as ocorrências, dividindo o intervalo pela taxa de ocorrência:
n

Por exemplo, considerando que chegam em média Â = 10 clientes ao longo de 8 horas,
o tempo médio entre um cliente e outro é:
Por fim, é importante ressaltar que é possível somar variáveis com distribuição de Poisson.

Sendo Xx o parâmetro da distribuição da variável X e Ay o parâmetro da distribuição da variável Y, então a variável S = X + Y terá distribuição de Poisson com parâmetro:
As = A% + Ay

Por exemplo, suponha que a empresa X receba, em média, Àx = 5 novos clientes por mês e que a empresaY receba, em média, ÂY = 3 novos clientes por mês, de modo que ambos sigam distribuições de Poisson. Se essas empresas se juntarem, formando a empresa S, então, se as taxas de novos clientes permanecerem as mesmas, a nova empresa receberá a seguinte taxa de novos clientes por mês, que também seguirá uma distribuição de Poisson:
= ^-x + Ay = 5 + 3 = 8

Também podemos multiplicar esses parâmetros por constantes, que o resultado também seguirá uma distribuição de Poisson.
No nosso exemplo, havendo uma empresa Z que receba Az = 10 novos clientes por mês,
sendo que metade dela se juntará às demais empresas, então a nova empresa N formada receberá a seguinte taxa de novos clientes por mês, que também seguirá uma distribuição de Poisson:
An = Ax + Ay + 0,5. Az = 5 + 3 + 0,5 x 10 = 13

l«** IX

r f i (CESPE/2010 - MPU/Analista) Uma empresa possui um serviço de atendimento ao consumidor (SAC). i
: Diariamente, um atendente registra, em uma folha de papel, as chamadas recebidas.
Cada folha de registro i

= do atendente do SAC permite o registro de até 20 chamadas. O atendente efetua os registros de forma i
= sequencial, anotando, para cada chamada, se houve reclamação.
=

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

De acordo com os dados históricos, sabe-se que, a cada 20 chamadas, a probabilidade de se registrar exatamente uma reclamação é constante e igual a 0,05. Sabe-se também que o número médio diário de reclamações registradas pelo SAC é igual a 1.
Com base nessas informações e considerando 2,71 como valor aproximado para o número e, base do logaritmo natural, julgue o seguinte item.
Considere que o número de reclamações registradas pelo SAC, X(t), em um intervalo de tempo t, siga um processo de Poisson e que X(5) represente o número de reclamações registradas em um intervalo de 5 dias úteis. Nesse caso, a probabilidade de não haver reclamações registradas em um intervalo de 5 dias úteis é igual a e-5.
Comentários:

O enunciado informa que a média é de = 1 reclamação por dia. Assim, para um intervalo de 5 dias, a taxa de ocorrência é:
Para a distribuição de Poisson, a probabilidade P(X = 0), com Â = 5, é dada por:

e-À.Âk

Gabarito: Certo.

s

P(X = fc)

kl e 5.5o
P(X = 0)

0!

; (FGV/2022 - SEFAZ/AM) Suponha que o número de carros que chega a uma praça de pedágio siga uma distribuição Poisson, com uma média de 2 carros por minuto.

A probabilidade de que, num intervalo de 2 minutos, passe no máximo um carro é aproximadamente igual a í [use e'4 = 0,0183]í a) 0,09

b) 0,12

i c) 0,17

d) 0,20

í e) 0,22

; Comentários:

: O enunciado informa que a média é de 2 carros por minuto e pede a probabilidade associada a um tempo de 2 minutos. O primeiro passo é calcular a média de carros a cada 2 minutos:
Tl 2

: L = 1 X- = 2 x - = 4

í Hi

A probabilidade de passar no máximo um carro, ou seja, 0 ou 1 carro é a soma:
í P(X < 1) = P(X = 0) + P(X = 1)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A probabilidade da distribuição de Poisson é dada por:

P(x = fc) =

Para k = 0, sendo 2 = 4, temos:

e 4 0x) 4o x fc!
e 4 x 1

p(%= =

— =e-4

Para k = 1, temos:

E a soma é:

. e-4 x 41

PCx = 1) = —-—

e 4 x 4 ,

—; = 4.e"4

Sendo e 4 = 0,0183, temos:

Gabarito: A

P(X < 1) = e"4 + 4. e-4 = 5. e"4

P(X < 1) = 5 x 0,0183 = 0,0915 s 0,09

(FCC/2015 - TRT 3- Região) A comissão de erradicação do trabalho infantil de um determinado TribunalRegional do Trabalho analisa, por meio de seu canal de denúncias, casos de desrespeito à legislação que regula o trabalho de menores de 18 anos. Suponha que a variável X, que representa o número de denúncias mensais que são recebidas, tem distribuição de Poisson com média 9. Nessas condições,a probabilidade de serem recebidas 2 ou 3 denúncias em um período de 10 dias é igual a
Dados:

e1 = 0,37
e_2=Q,14
e-3 = 0,05

a) 0,450

b) 0,472

c) 0,230

d) 0,375

e) 0,250

Comentários:

Sabendo que a variável tem distribuição de Poisson, com média de 9 denúncias por mês,
ou seja, em um período n₁ = 30 dias, temos = 9, em um período de n₂ = 10 dias, temos:
Ademais, a probabilidade de receber X = 2 ou X = 3 denúncias corresponde a união dessas probabilidades.Como são eventos mutuamente exclusivos, a probabilidade da união corresponde à soma das probabilidades:
P(X = 2 OU X = 3) = P(X = 2) + P(X = 3)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= Pela fórmula de Poisson, temos:
=

e"3 32

; pçx = 2) = ' = 4,5 x
0,05 = 0,225 i

:
e-3 g3
:

; P(X = 3) = ' = 4,5 x 0,05
= 0,225 i i Logo:
i

P(X = 2 OU X = 3) = 0,225 + 0,225 = 0,45

; Gabarito: A.

I

; (CESPE/2018 - TCE-PA/Auditor de Controle Externo) O número de acidentes de trabalho em determinada ;
= obra pública no mês k segue uma distribuição de Poisson Wk com média igual a 1
acidente por mês. i

= Considerando uma amostra aleatória simples Wi, W₂,Wn, julgue 0 item a seguir, acerca da soma Wi +
W₂ i

+ ... + Wn.

: O total de acidentes segue distribuição de Poisson com média igual a n.
;

I

I

i Comentários:

A soma de variáveis com distribuição de Poisson também segue uma distribuição de Poisson. A média i

= (esperança) da distribuição Wi + W₂ + ... + wn pode ser calculada pela propriedade aditiva da esperança:
E(W1 + W2 + + Wn~) = E(WJ + E(W2) + - + E(Wn~)

; O enunciado informa que as médias são todas iguais a 1. Sabendo que há n variáveis W,, temos:

: E(W1 + W2 + - + Wn) = l + l + -+l = lxn = n
=

:
:

=
n vezes =

Ê Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçÃo BINoMIAL NEGATIVA

A distribuição binomial negativa ou distribuição de Pascal estuda o número de ensaios de Bernoulli necessários para se obter k sucessos.
Enquanto a binomial (original) estuda o número de sucessos (X = k) obtidos em n ensaios de Bernoulli, com n fixo; a binomial negativa estuda o número de ensaios(X = x)
necessários para se obter k sucessos, com k fixo.

Vamos utilizar um exemplo para ilustrar melhor essa diferença. Vamos supor que o ensaio de Bernoulli seja o lançamento de uma moeda, e que o sucesso corresponda à face CARA.
Se definirmos que vamos jogar a moeda 10 vezes para estudar quantos sucessos obtemos,
temos uma distribuição binomial (original); se definirmos que vamos jogar a moeda até obtermos 5sucessos, temos uma distribuição binomial negativa.
A probabilidade de realizarmos X = n ensaios para obter k sucessos é dada por:

p(X = %) = (* l)pk-qx k

Para o nosso exemplo de lançamento da moeda, a probabilidade de obter CARA (sucesso)
em um único lançamento é p = 0,5 e de obter COROA é q = 1 — p = 0,5. Assim, a probabilidade de obtermos k = 5sucessos em x = 8 lançamentos é:

= 8) = (| 1) 0,55.0,58"5 = Q 0,55.0,53

=(>8

A combinação (?) é igual a:

77^ 7! 7 x 6 x 5 x 4! 7x6x5

W (7-4)! x 4! " 3! x 4! " 3x2 ~ 7 x 5 ~ 35

Então, a probabilidade P(X = 8) é:

P(X = 8) = 35 x 0,58 = 0,137

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O que muda, em relação à fórmula da binomial (original), são os parâmetros da combinação: enquanto na binomial (original) a combinação é de Qj, na binomial negativa, a combinação é de Q
Para o nosso exemplo, em vez de termos a combinação Q) = como seria o caso para a distribuição binomial, temos a combinação (X = Q).
Essa diferença ocorre porque, na distribuição binomial negativa, a última tentativa será necessariamente o k-ésimo sucesso (para o nosso exemplo, a 8- tentativa será o 52 sucesso); caso contrário teríamos parado com as tentativas antes.
Por isso, precisamos escolher, dentre as demais x - 1 = 7 tentativas, quais serão os k — 1 = 4
sucessos.

Os parâmetros da distribuição binomial negativa são a probabilidade de sucesso p e o número de sucessos k. Assim, podemos representar essa distribuição como X~BN(p, k).
A variável com distribuição binomial negativa assume os valores x = k,k + 1, k + 2,...

Ela é no mínimo k (pois só é possível obter k sucessos, com no mínimo k tentativas)
e não tem limite superior
(é sempre possível ter que tentar mais uma vez até obter o k-ésimo sucesso). Para o nosso exemplo, em que k = 5, a variável pode assumir os valores x = 5,6,7,..., sem limite superior.
Também podemos utilizar a binomial negativa para calcular a probabilidade de extrairmos uma amostra de tamanho x, de uma população com 2 atributos (sucesso e fracasso), para encontrar k sucessos na amostra.
EXEMPLIFICANDO

Vamos supor que em uma fábrica, 20% das peças apresentem defeito. Para calcular a probabilidade de inspecionarmos exatamente x = 4 peças, para encontrar k =2 peças defeituosas, utilizamos a distribuição binomial negativa, com p = 20% = 0,2 e k = 2.
A probabilidade P(X = 4) é:

p(X = %) = (*_ ^pk.qx k

P(X = 4) = Q 0,22.0,82 = 3 x 0,04 x 0,64 = 7,68%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

No entanto, para utilizar essa distribuição, é necessário que as extrações sejam independentes (mesma condição necessária para a aplicação da distribuição binomial). Para isso, é necessário que a população seja infinita (ou muito grande em relação à amostra) ou que as extrações sejam feitas com reposição.
E quanto à esperança? Assim como para outras distribuições, esperamos que o resultado mantenha a proporção de sucessos. Por exemplo, no caso do lançamento de uma moeda, com p = 50%,esperamos ter que lançar 10 vezes para obter 5 caras.
Isso significa que o valor esperado é dado por:

Para o exemplo da fábrica, em que p = 0,2 e k = 2, esperamos que o número de peças inspecionadas seja:
E a variância é dada por:

Para o mesmo exemplo da fábrica, a proporção de peças não defeituosas (fracasso) é q
= 1 - p = 0,8. A
variância dessa distribuição é:

2 x 0,8

0,22

= 40

Pontue-se que a distribuição geométrica, que estuda o número de tentativas até o l9
sucesso, pode ser considerada um caso particular da binomial negativa, para k = 1.
Também podemos dizer que a binomial negativa corresponde à soma de k variáveis geométricas, com o mesmo parâmetro p.
De fato, para k = 1, temos = ~ e que são as fórmulas da esperança e da variância,respectivamente, da distribuição geométrica. E a probabilidade de X = x para k = 1 é:

P(X = x) = Q 1) pk. qx~k = (% Q 1) Pk-clX~k = P- ^X~k

Essa é justamente a probabilidade P(X = x) para a variável com distribuição geométrica.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

INDO MAIS

FUNDO!

Assim, como podemos parametrizar a distribuição geométrica pelo número de fracassos até o primeiro sucesso, também podemos parametrizar a binomial negativa como o número de fracassos até o /c-ésimo sucesso. Nesse caso, teríamos:
p(y = y) = pk. qy

Com essa parametrização temos y fracassos e k sucessos, logo, há y + k tentativas no total. Sabendo que a última tentativa será o /c-ésimo sucesso, precisamos escolher,dentre as demais y + k - 1 tentativas quais serão os k - 1 sucessos.
Para o exemplo do lançamento da moeda até obter k = 5 sucessos, sabemos que um total de x = 8 tentativas (parametrização anterior) corresponde a y = 3fracassos
(parametrização alternativa). A probabilidade de obter y = 3 fracassos é dada por:

P(Y = 3) = (5 + 3 ~ 0,55.0,53 = Q 0,55.0,53

Como era esperado, a probabilidade de obter y = 3 fracassos é igual à probabilidade de lançar a moeda um total de x = 8 vezes (parametrização anterior).
Com essa parametrização a variável pode assumir os valores Y = {0,1,2,3,...}, ou seja,
a partir de zero (afinal, é possível não obter fracasso algum).
ESQUEMATIZANDO

Distribuição Binomial Negativa (p,k)

Número de Ensaios de Bernoulli até o fc-ésimo sucesso p(X = fc) = Q i) pk-
Esperança: E(X) = Variância: V(JC) =

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (CESPE/2011 - STM) Se, em determinada fábrica, 10% das peças produzidas são defeituosas, então,
para fins i de controle de qualidade, uma distribuição binomial negativa deve ser usada na situação em que é retirada j
= uma amostra aleatória simples com reposição de 10 peças para se determinar a probabilidade de ocorrer
; exatamente 3 peças defeituosas nessa amostra.
i

; Comentários:

: Sabendo que será retirada uma amostra aleatória, com reposição, de n = 10 peças e que a probabilidade de i defeito é p = 10%, então temos uma distribuição binomial (original).
j Gabarito: Errado.

I

I

: (FGV/2019 - DPE/RJ - Adaptada) Uma amostra (Xi, X₂,..., Xn) de tamanho n, onde cada uma das variáveis X, ;
= é de Bernoulli, tipo 0 ou 1, todas com o mesmo parâmetro p, é extraída.
Considerando as distribuições exatas, ;

= é correto afirmar que:
i

I

I

: Se a extração da amostra só é encerrada quando Xk = 1, pela J-ésima vez, então K tem distribuição de Binomial j
= Negativa com parâmetros J e p.

I

I

i Comentários:

I

I

: Se a extração da amostra só é encerrada quando Xk = 1 (isto é, ocorre sucesso)
pela J-ésima vez, então a j

= variável tem distribuição binomial negativa. Os parâmetros são o número de sucessos desejados (J)
e a i

I

; probabilidade de sucesso de cada elemento p.
i

I

I

Ê Resposta: Certo.

I

i (CESPE/2018 - Analista Judiciário STM) A quantidade de clientes atendidos em cada minuto pelos ;
= empregados 1 e 2 em um balcão de atendimentos é expressa por T=Yi + Y₂, em que
Yi = quantidade de i

= clientes atendidos (por minuto) pelo empregado 1, e Y₂ = quantidade de clientes atendidos (por minuto) pelo i
= empregado 2.
;

= Considerando que, nessa situação hipotética, Yi e X₂ sejam variáveis aleatórias independentes, seguindo i
= uma mesma distribuição Y, cuja função de probabilidade é P(Y = y) = 0,1 x 0,9y,
para y = 0, 1, 2, ..., julgue o i

= seguinte item.
j

I

I

A somaTsegue uma distribuição binomial negativa.
i

I

I

i Comentários:

I

I

: Sabendo que as variáveis Y seguem distribuições geométricas com mesmo p, então a soma de k variáveis j
= com distribuição geométrica corresponde a uma distribuição binomial negativa (que estuda o número de i tentativas até o k-ésimo sucesso).i

I

I

: Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(CESPE/2018 - Analista Judiciário STM) A quantidade de clientes atendidos em cada minuto pelos empregados 1 e 2 em um balcão de atendimentos é expressa por T=Yi + Y₂, em que Yi= quantidade de clientes atendidos (por minuto) pelo empregado l,eY₂ = quantidade de clientes atendidos(por minuto) pelo empregado 2.
Considerando que, nessa situação hipotética, /i e Y₂ sejam variáveis aleatórias independentes, seguindo uma mesma distribuição Y, cuja função de probabilidade é P(/ = y) = 0,1 x o,9y,para y = 0, 1, 2,..., julgue o seguinte item.
Se E[T]=quantidade média de clientes atendidos em cada minuto por esses dois empregados, então
E[7]< 17.

Comentários:

A média de uma variável binomial negativa é dada por:

E(X) = ~

P

Pela função de probabilidade P(Y = y) = 0,1 x 0,9Y, concluímos que a probabilidade de sucesso é p = 0,1.Ademais, sabemos que a variável T consiste na soma de k = 2 variáveis geométricas, então:

Em = A = 20

L.G...a..b..a..r.i.t..o E. rrado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Resumo da Aula

Distribuição Uniforme: todos os valores são equiprováveis

Distribuição de Bernoulli (p): 1 Experimento (Ensaio) de Bernoulli

* 2 resultados possíveis: sucesso (X = 1) ou fracasso (X = 0)

* Probabilidade de sucesso: P[X = 1] = p

* Probabilidade de fracasso: P[X = 0] = q = 1 — p

E{X}=p- V(X) = p.q

Distribuição Binomial (n,p): Número de sucessos em n Ensaios de Bernoulli independentes

P(X = k) = Cn,k.pk.qn~k

E(X) = n.p; V(X) = n.p.q

Distribuição Geométrica (p): Número de Ensaios de Bernoulli até o primeiro sucesso

P(X = k} = q^kp q
F(X) =-;

p p

Distribuição Hipergeométrica (N,S,rí): Extrações sem reposição

P(X = k) = ©o

. . . . N — n
E(X) = n.p; V(X) = n.p.q _ ₁

Distribuição de Poisson (A): Aproximação da Binomial para n -> °oep -> 0

z x e"A.Ak
P(X = k) =

kl

E(X) = A; V(X) = A

Distribuição Binomial Negativa (p, k): Número de Ensaios até o fc-ésimo sucesso

P(x = k) = Q 2 i) Pk-qx~k

, „ k q.k

E(X)=~; y(x)=^

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Distribuição Uniforme

Item. 1. (CEBRASPE/2022 - TCE/SC) Considerando uma sequência de variáveis aleatórias {Xk}, em que
P(Xk = —0,2k) = P(Xk = 0,2k) = 0,5, para k G {1,2,...}, julgue o item a seguir, com relação à soma
Sn =

Xk segue distribuição uniforme discreta.

Comentários:

Em uma distribuição uniforme discreta, todos os resultados possíveis apresentam o mesmo resultado.Aqui, temos 2 resultados possíveis: —0,2k e 0,2k, cada um com probabilidade 0,5 (50%).

Por exemplo, para k = 1, temos:

P(Xx = —0.21) = P(Xx = -0,2) = 0,5

P(Xx = 0.21) = P(Xx = 0,2) = 0,5

Para k = 2, temos:

P(X2 = —0,22) = P(X2 = -0,04) = 0,5

P(X2 = 0,22) = P(X2 = 0,04) = 0,5

E assim por diante, para todos os valores de k.

Como todos os valores possíveis apresentam a mesma probabilidade, podemos concluir que, de fato, as variáveis seguem distribuições uniformes discretas.
Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Distribuição de Bernoulli

Item. 1. (CESPE/2011 - SEDUC-AM)

RG(*)

35805684

21355706

43674475

2305386

gênero

M
F
M
F

grau de instrução hiperatividade
N
N
S
N

98814652 M 4 N

(*) números Retidos gerados por computador.

A tabela acima contém um conjunto de dados formado por quatro variáveis: RG; gênero ( M =
masculino; F =
feminino); grau de instrução (1 = analfabeto; 2 = fundamental incompleto; 3 =
fundamental completo; 4 =
médio incompleto; 5 = médio completo ou superior); e hiperatividade (S = sim; N =
não). Com base nessa tabela, julgue o item seguinte.
Com relação à variável dicotômica hiperatividade, atribuindo-se valor 1 para uma categoria e 0 para a outra, a média dessa variável binária representa a frequência relativa de observações que receberam valor 1.
Comentários:

Considerando que os possíveis resultados para a variável são apenas 2, 0 (fracasso) ou
1 (sucesso), então essa variável segue uma distribuição de Bernoulli, cuja média (ou esperança) é dada por:
E(X) = p

Sabendo que p corresponde à probabilidade de sucesso (1), então a média, de fato,
corresponde à frequência relativa de observações com valor 1.
Gabarito: Certo.

Item. 2. (Cebraspe/2013 - MPU) As variáveis aleatórias X e Y seguem uma distribuição de Bernoulli com probabilidade de sucesso igual a 0,4. Considerando S = X + Y e que os eventos aleatórios A = [X =1] e B = [Y =
1] sejam mutuamente exclusivos, julgue o item subsequente.

É correto afirmar que P(A UB) = P(S = 1) = 0,8.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A probabilidade da união é dada por:

P(A U B) = P(A) + P(B) - P(A n B)

Pelo enunciado, temos A = [X = 1] e B = [Y = 1], logo:

P(A) = P[X = 1]

P(B) = P[F = 1]

É informado ainda que A e B são mutuamente exclusivos, logo:

P(A n B) = 0

Assim, a probabilidade da união corresponde a:

P(A U B) = P[X = 1] + P[Y = 1]

Considerando que X e Y seguem uma distribuição de Bernoulli com probabilidade de sucesso p = 0,4, então P[X
= 1] = 0,4 e P[Y = 1] = 0,4:

P(4 U B) = 0,4 + 0,4 = 0,8

Além disso, como S = X + Y, a probabilidade P(S = 1) corresponde à probabilidade deX = leY = 0oudeY = leX = 0. Como [X = 1] e [Y = 1] são eventos mutuamente exclusivos, então a probabilidade deX = leY = 0é igual à probabilidade de X = 1; e a probabilidade deY = leX = 0é igual à probabilidade de Y = 1, então:
P(S = 1) = P[X = 1] + P[Y = 1] = P(A U B)

Gabarito: Certo.

Item. 3. (Cebraspe/2016 - TCE-PA) Se as variáveis aleatórias X e Y seguem distribuições de
Bernoulli, tais que
P[X = 1] = P[Y = 0] = 0,9, então:

A média de Y é superior a 0,5.

Comentários:

A média de uma distribuição de Bernoulli é:

E(y) = p

Sabemos que a probabilidade de fracasso de Y é q = P[Y = 0] = 0,9. Logo a probabilidade de sucesso é p = 1 - q
= 1-0,9 = 0,1. Assim:

E(y) = 0,l

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 4. (Cebraspe/2016 - TCE-PA) Se as variáveis aleatórias X e Y seguem distribuições de
Bernoulli, tais que
P[X = 1] = P[Y = 0] = 0,9, então:

As variâncias de X e Y são iguais.

Comentários:

A variância de uma distribuição de Bernoulli é:

V(X) = p.</

Sabemos que a probabilidade de sucesso de X é p = P[X = 1] = 0,9, logo a probabilidade de fracasso é q = 1 - p =1-0,9 = 0,1:

V(X) = 0, 9 x 0,1 = 0,09

Já, a probabilidade de fracasso de Y é q = P[Y = 0] = 0,9, logo, a probabilidade de sucesso deYép = l- q = l-0,9 = 0,1:

V(Y) = 0,1 x 0,9 = 0, 09

Gabarito: Certo.

Item. 5. (Cebraspe/2016 - TCE-PA) Se as variáveis aleatórias X e Y seguem distribuições de
Bernoulli, tais que
P[X = 1] = P[Y = 0] = 0,9, então:

A distribuição X2 é Bernoulli com média igual a 0,81.

Comentários:

Vejamos como fica a distribuição de X2:

* X = 0 X2 = 0

* X = 1 X2 = 1

Assim, a probabilidade P(X2 = 0) corresponde à probabilidade de P(X = 0) e a probabilidade P(X2 = 1) corresponde à probabilidade P(X = 1):
P(X2 = 0) = P(X = 0) = 1 - 0,9 = 0,1
P(X2 = i) = = 1) = 0,9

Ou seja, temos uma distribuição de Bernoulli com probabilidade de sucesso p = 0,9.
Sabemos que a média (ou esperança) dessa distribuição é:

£(X) = p = 0, 9

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Gabarito: Errado.

Item. 6. (Cebraspe/2013 - STF) Pedro e João são os oficiais de justiça no plantão do fórum de determinado município. Em uma diligência distribuída a Pedro, X é a variável aleatória que representa o sucesso(X = 1) ou fracasso (X = 0) no cumprimento desse mandado. Analogamente, Y é a variável aleatória que representa o sucesso (Y = 1) ou fracasso (Y = 0) de uma diligência do oficial João.
Com base nessa situação hipotética e considerando a soma S = X + Y, e que P(X = 1) = P(Y = 1) = 0,6
e E(XY) =
0,5, julgue o item que se segue, acerca das variáveis aleatórias X, Y e S.

A média da distribuição S é igual a 1,2.

Comentários:

Conforme as propriedades da esperança, temos:

E(S) = E(X + y) = E(X) + E(Y)

Considerando que X e Y assumem apenas dois valores possíveis, sucesso (1)
ou fracasso (0), sendo a probabilidade de sucesso p = 0,6 e, portanto, a probabilidade de fracasso q = 1 - p= 0,4, então os valores de
E(X) e E(Y) são:

E(X) = E(Y) = 0x0,4 + 1x0,6 = 0,6

A média (ou esperança) de S é, portanto:

E(S) = 0,6 + 0,6 = 1, 2

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Distribuição Binomial

Item. 1. (Cebraspe/2022 - PETROBRAS) Julgue o item a seguir, relacionados a álgebra e a probabilidade.
Cada uma de três moedas não viciadas, quando lançada, apresenta como resultado "cara"
ou "coroa". Ao se lançar essas três moedas, uma de cada vez, a probabilidade de se obter "cara" em duas delas e "coroa" em uma delas é superior a 0,4.
Comentários:

O lançamento de moedas caracteriza uma distribuição binomial, pois os lançamentos são independentes uns dos outros. Sendo as moedas não viciadas (comuns), a probabilidade de obter CARA (que a gente pode considerar como sucesso) é:
P = |=0,5

A probabilidade de fracasso (que corresponde à COROA, no nosso caso) é q = 1 — - = 0,5.

Sabendo que serão lançadas n = 3 moedas, a probabilidade de obtermos k = 2 sucessos (isto é, 2
CARAS e 1
COROA) é:

PÇX = k) = Cnk xpkx qn~k

P(X = 2) = C32 x 0,52 x O^1 = 3 x 0,25 x 0,5 = 0,375

Que é inferior a 0,4.

Gabarito: Errado

Item. 2. (Cebraspe/2022 - FUNPRESP-EXE) Em uma empresa há 100 produtos em estoque,
todos de igual aparência, mas com qualidades distintas, que só são evidenciadas com testes específicos:40 são de alta qualidade, 35 são de média qualidade e 25 são de baixa qualidade.
Considerando essas informações e o procedimento de análise de uma amostra com 15
produtos, com reposição, julgue o item a seguir.
Espera-se que na amostra haja, em média, 6 produtos de alta qualidade.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado informa que há 40 produtos de alta qualidade, de um total de 100
produtos, dos quais 15 produtos serão extraídos com reposição. Devemos utilizar a distribuição binomial porque os produtos serão extraídos com reposição, logo as extrações são independentes.
Sabendo que há 40 produtos de alta qualidade, dentre 100, podemos calcular a probabilidade de sucesso:
Sabemos também que serão extraídos n = 15 produtos. Assim, a esperança da variável binomial é dada por:
E(X) = n x p = 15 x 0,4 = 6

De fato, espera-se que na amostra haja 6 produtos de alta qualidade.

Gabarito: Certo

Item. 3. (Cebraspe/2022 - FUNPRESP-EXE) Em uma empresa há 100 produtos em estoque,
todos de igual aparência, mas com qualidades distintas, que só são evidenciadas com testes específicos:40 são de alta qualidade, 35 são de média qualidade e 25 são de baixa qualidade.
Considerando essas informações e o procedimento de análise de uma amostra com 15
produtos, com reposição, julgue o item a seguir.
Espera-se que na amostra haja, em média, 4 produtos de baixa qualidade.

Comentários:

Essa questão pede o valor esperado de produtos de baixa qualidade, considerando que há
25 produtos desse tipo, de um total de 100 produtos. A probabilidade de sucesso é:
p = lõõ = 0'25

Sabendo que serão extraídos n = 15 produtos, com reposição (extrações independentes), a esperança da variável binomial é dada por:
£(X) = n x p = 15 x 0,25 = 3,75

Que é diferente de 4.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 4. (Cebraspe/2022 - PETROBRÁS) Considerando que a variável aleatória X segue uma distribuição binomial com parâmetros n = 10 e p = 0,1, julgue o item subsequente.
O valor esperado de X é igual a 1.

Comentários:

Para uma variável com distribuição binomial, o valor esperado é dado por:

E(X) = nxp

Sendo n = 10 e p = 0,1, temos:

£(%) = 10 x 0,1 = 1

Gabarito: Certo

Item. 5. (Cebraspe/2022 - PETROBRÁS) Considerando que a variável aleatória X segue uma distribuição binomial com parâmetros n = 10 e p = 0,1, julgue o item subsequente.
O desvio padrão da distribuição de X é igual ou superior a 0,9.

Comentários:

Para uma variável com distribuição binomial, a variância é dada por:

V (X) = n x p x q

Sendo p = 0,1, temos q = 1 - p = 0,9. Assim, sendo n = 10, a variância é:

7(X) = 10 x 0,1 x 0,9 = 0,9

O desvio padrão é a raiz quadrada:

0,95

Que, de fato, é superior a 0,9.

Gabarito: Certo

Item. 6. (Cebraspe/2022 - PETROBRÁS) Considerando que a variável aleatória X segue uma distribuição binomial com parâmetros n = 10 e p = 0,1, julgue o item subsequente.
P(X > 0) = 0,9.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Podemos calcular a probabilidade de X ser maior que 0 pela probabilidade complementar,
considerando que a variável binomial assume valores necessariamente maiores ou iguais a 0:
P(X > 0) = 1 - P(X = 0)

Sabendo que n = 10 e p = 0,1 (q = 1 - p = 0,9), a probabilidade de obtermos k = 0 sucessos é dada por:
P(X = /c) = CUik xpk x qn~k

P(X = 0) = C10j0 x 0,1° x O,910 = 1 x 1 x O,910 s 0,35

Que é diferente de 0,9.

Gabarito: Errado

Item. 7. (Cebraspe/2022 - TELEBRÁS) Considere um par (X, F) de variáveis aleatórias discretas, tais que
X~Binomial (lO,0 e Y~Binomial Sabendo que Cov(X, V) = -1,1,
julgue o seguinte item acerca da diferença Z = Y — X.
O valor esperado de Z é igual a 3.

Comentários:

Para calcular o valor esperado de Z, vamos primeiro calcular a esperança das variáveis X e Y.
Sabendo que a esperança de uma variável binomial é dada por nxp, temos:

£(X) = nxp = 10 x- = 5

£(/) = nxp = 10x- = 2

Pelas propriedades da esperança, a esperança da diferença corresponde à diferença das esperanças:

F(Z) = E(Y - X) = F(K) - F(X) = 2 - 5 = -3

Que é diferente de 3.

Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 8. (Cebraspe/2022 - TELEBRÁS) Considere um par (X, F) de variáveis aleatórias discretas, tais que
X~Binomial (lO,0 e Y~Binomial (lO,0.

Sabendo que Cov(X, F) = — 1,1, julgue o seguinte item acerca da diferença Z = Y — X.

Var[Z] = 6,3.

Comentários:

Para calcular a variância de Z, vamos antes calcular a variância das variáveis X e
Y. Sabendo que a esperança de uma variável binomial é dada por n x p x q, sendo q = 1 — p, temos:
z x 1 í 1\ 15

F(X) = n x p x q = 10 x - x ^1 — -J = 5 x - = - = 2,5

z X 1 ( 1\ 4 8

V(Y) = nxpxq = 10 x-x ^1 — -J = 2x- = -= 1,6

A variância da diferença é dada por:

7(Z) = V(Y - X) = 7(y) + V(X) - 2 x Cov(X, F)

Sabendo que Cov(X, F) = -1,1, temos:

7(Z) = 2,5 + 1,6 - 2 x (-1,1) = 4,1 + 2,2 = 6,3

Gabarito: Certo

Item. 9. (Cebraspe/2022 - TCE/SC) Suponha que uma amostra de tamanho n = 1 seja retirada de uma população X ~ BinomialÇm, p), em que m e p são parâmetros desconhecidos. Sabendo que m G {1,2} e que p G se a amostra aleatória simples for representada por Xlt considere a seguinte estatística para a estimação do par (m,p).
m = lep = -,

m = 2ep = -,

Com base nessas informações, julgue o próximo item.

seX1 = 0

se X± = 1 ou 2

Se jtí denota a média populacional desconhecida, então seu espaço paramétrico é representado pelo conjunto
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Segundo o enunciado, o parâmetro m da distribuição binomial (que normalmente chamamos de n) pode ser m = 1 ou m = 2; e que a probabilidade de sucesso pode ser p = - ou p =
Para cada parâmetro, temos duas possibilidades e não sabemos ao certo qual delas corresponde ao verdadeiro valor do parâmetro.
Sabendo que a média da distribuição binomial é o produto E(X) = m x p, as possibilidades para a média são:
m P E(X) = mxp

1 1 1

1 5 1 X 5 " 5

1 1 1

1 lx- = -

4 4 4

1 1 2

5 2 X 5 " 5

1 1 1

2 2x- = -

4 4 2

Logo, o espaço é representado pelo conjunto

Gabarito: Errado

Item. 10. (Cebraspe/2021 - COREN/CE) Suponha que 20% dos recursos administrativos impetrados contra determinada decisão administrativa em uma repartição pública sejam deferidos. Nessa situação, se 4 novos recursos administrativos forem distribuídos aleatoriamente para análise, a probabilidade de haver um único recurso deferido entre esses 4 recursos analisados é igual a a) 0,008
b) 0,1024

c) 0,25

d) 0,4096

Comentários:

O enunciado informa que a proporção de processos deferidos, que corresponde à probabilidade de sucesso, é p = 20% = 0,2. Logo, a probabilidade de fracasso é q = 1 - 0,2 = 0,8.
Sabendo que há n = 4 processos, a probabilidade de obtermos k = 1 sucesso (um único processo deferido) é:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

P(X = k) = Cn,k xpk xqn k

P(X = 1) = C41 x 0.21 x 0,83 = 4 x 0,2 x 0,512 = 0,4096

Gabarito: D

Item. 11. (Cebraspe/2021 - SERPRO) Considerando que o número X de erros registrados em determinado tipo de código computacional siga uma distribuição binomial com média igual a 4 e variância igual a 3, julgue o item a seguir.
É impossível haver registros de 18 erros nesse tipo de código computacional.

Comentários:

O enunciado informa que a média da variável binomial é:

E(JC) = n x p = 4

E que a variância é:

VÇX') = nxp x q = 3

Sabendo que o produto n x p é igual a 4, temos:

4 x q = 3

Sabendo que p = 1 — q, temos:

q=4

3 1

Substituindo esse resultado na fórmula da esperança, temos:

n x - = 4

n = 16

Como o limite máximo da variável é n = 16, de fato, é impossível observarmos k = 18 sucessos.

Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 12. (Cebraspe/2021 - SERPRO) Considerando que o número X de erros registrados em determinado tipo de código computacional siga uma distribuição binomial com média igual a 4 e variância igual a 3, julgue o item a seguir.
P(X = 0) = |

Comentários:

3 1

Na questão anterior, calculamos que a probabilidade de fracasso é q = -, a probabilidade de sucesso é p = - e
4 4

que n = 16. A probabilidade de obtermos k = 0 sucesso é dada por:

p(x = /c) = Cnk x pk x qn k

PCX = 0) = C16,0 x

Que é diferente de

Gabarito: Errado

Item. 13. (Cebraspe/2021 - SERPRO) Considerando que o número X de erros registrados em determinado tipo de código computacional siga uma distribuição binomial com média igual a 4 e variância igual a 3, julgue o item a seguir.
A mediana de X é igual a 4.

Comentários:

Sempre que o produto n x p for um número inteiro, a média, a mediana e a moda da distribuição binomial serão iguais a esse valor.
Aqui, temos n x p = 4, logo a mediana também é igual a 4.

Gabarito: Certo

Item. 14. (Cebraspe/2019 - TJ-AM) É igual a - a probabilidade de determinado advogado conseguir decisão favorável a si em cada petição protocolada por ele na vara cível de certo tribunal. O plano desse advogado é protocolar, sequencialmente, 12 petições nessa vara cível durante o ano de 2020.Favoráveis ou não, as decisões do tribunal para petições são emitidas na mesma ordem cronológica em que são protocoladas e são sempre independentes entre si.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A partir dessa situação hipotética, julgue o próximo item, considerando as variáveis aleatórias X
e Y, em que
X = quantidade de decisões emitidas pelo tribunal até que ocorra a primeira decisão não favorável ao advogado, e Y = quantidade de decisões emitidas pelo tribunal favoráveis ao advogado.
Espera-se que, ao longo de 2020, exatamente 9 decisões sejam favoráveis ao advogado.

Comentários:

Considerando que Y é a quantidade de decisões favoráveis, dentre n = 12 petições, sabendo que a probabilidade de a decisão ser favorável (sucesso) é p = - e que as decisões são independentes entre si,
podemos concluir que Y segue distribuição binomial. A esperança dessa distribuição é:

E(zXx) = nxp = 12x- = 9 3

Gabarito: Certo.

Item. 15. (Cebraspe/2019 - TJ/AM) É igual a - a probabilidade de determinado advogado conseguir decisão favorável a si em cada petição protocolada por ele na vara cível de certo tribunal. O plano desse advogado é protocolar, sequencialmente, 12 petições nessa vara cível durante o ano de 2020.Favoráveis ou não, as decisões do tribunal para petições são emitidas na mesma ordem cronológica em que são protocoladas e são sempre independentes entre si.
A partir dessa situação hipotética, julgue o próximo item, considerando as variáveis aleatórias X e
Y, em que
X = quantidade de decisões emitidas pelo tribunal até que ocorra a primeira decisão não favorável ao advogado, e Y = quantidade de decisões emitidas pelo tribunal favoráveis ao advogado.
A probabilidade do evento "Y é igual a 1" é superior a —.

Comentários:

Sabendo que Y segue distribuição binomial com n = 12 e probabilidade de sucesso p = -, logo, a probabilidade de fracasso é q = 1 — p = -. Assim, a probabilidade de obter k = 1 decisão favorável (sucesso) é:
P(y = fc) = Cnkxpkx qn~k
P(Y = 1) = C124 x d)' x (A)'1 = 12 x | x

Como o denominador 411 é maior do que o denominador indicado no item 410, então o resultado da fração
9é menor do que a fração indicada no item — E outras palavras, P(X = 1) é inferior a
—.

Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 16. (Cebraspe/2019 - TJ/AM) É igual a - a probabilidade de determinado advogado conseguir decisão favorável a si em cada petição protocolada por ele na vara cível de certo tribunal. O plano desse advogado é protocolar, sequencialmente, 12 petições nessa vara cível durante o ano de 2020.Favoráveis ou não, as decisões do tribunal para petições são emitidas na mesma ordem cronológica em que são protocoladas e são sempre independentes entre si.
A partir dessa situação hipotética, julgue o próximo item, considerando as variáveis aleatórias X e Y, em queX = quantidade de decisões emitidas pelo tribunal até que ocorra a primeira decisão não favorável ao advogado, e Y = quantidade de decisões emitidas pelo tribunal favoráveis ao advogado.
A probabilidade de Y ser inferior a 2 é superior a 1%.

Comentários:

Para que Y seja inferior a 2, então podemos ter Y = 0 ou Y = 1. Na questão anterior, calculamos a probabilidade de obtermos 1 sucesso:
z x 9

3 1

A probabilidade de observamos 0 sucesso, sabendo que n = 12, p = - e q = -, é dada por:

4 4

o 1\12 1 1

x 4/ - 1 x 1 x ^77 - ^77

Logo, a probabilidade de Y ser inferior a 2 é:

P(r < 2) = P(Y = 0) + P(Y = 1) =

Para que esse resultado seja superior a 1%, é necessário que 0 denominador seja inferior a 3700. No entanto,412 é muito superior a 3700. Para ilustrar, 46 = 4096, que já é superior a esse valor; e 412 é 0
quadrado disso!

Gabarito: Errado

Item. 17. (Cebraspe/2018 - BNB) Julgue o próximo item, relativos a análise combinatória e probabilidade.
Situação hipotética: Para cada um dos 16 itens da prova objetiva de informática de um concurso público, o candidato deverá marcar na folha de respostas se o item é certo ou errado. A condição para não desclassificação do candidato é que ele acerte o gabarito de pelo menos 10 desses itens.
Assertiva: Nesse caso, se 0 candidato marcar aleatoriamente todos os 16 itens, a probabilidade de ele não ser desclassificado é igual 7x3|xl3-
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considerando que as possíveis respostas são apenas 2, certo (sucesso) ou errado
(fracasso), e que há 16
questões, então temos uma distribuição binomial, com n = 16. Se o candidato marcar a resposta aleatoriamente,então a probabilidade de sucesso (acerto) é p =

Assim, a probabilidade de o candidato não ser desclassificado é igual à probabilidade de ele acertar 10 questões ou mais:
p = p(X = 10) + P(X = 11) + P(X = 12) + P(X = 13) + P(X = 14) + P(X = 15) + P(X = 16)

X (G.6,10 + Qe,ll + G.6,12 + G.6,13 + Qõ,14 + G.6,15 + 0.6,16)

16 16x15x14x13x12x11 16x15x14x13x12
16x15x14x13

X (

6 x 5 x 4 x 3 x 2

+

5 x 4 x 3 x 2

+

4x3x2

16 x 15 x 14 16 x 15 16

⁺ 3x2 ⁺ 2 ' h 1 + lóJ

X (4 x 14 x 13 x 11 + 2 x 14 x 13 x 12 + 2 x 5 x 14 x 13 + 16 x 5 x 7 + 8 x 15 + 17)

^_(7xl3xll + 7xl3x6 + 2,5x7xl3 + 2x5x7 + 15 + 2,125)

(7 x 13 x 19,5 + 70 + 17,125) (7 x 13 x 19,5 + 87,125)

213 213

7x11x13

Podemos observar que esse valor é superior a ——

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 18. (Cebraspe/2016 - TCE-PA) Se as variáveis aleatórias X e Y seguem distribuições de
Bernoulli, tais que
P[X = 1] = P[Y = 0] = 0,9, então:

X + Y segue uma distribuição binomial com parâmetros n = 2 e p = 0,3, se X e Y
forem variáveis aleatórias independentes.
Comentários:

Vimos que a distribuição binomial consiste na repetição de um mesmo experimento de
Bernoulli, com a mesma probabilidade de sucesso, p. Porém, a probabilidade de sucesso de X é p = 0,9 e a probabilidade de fracasso deYéq = 0,9 e, portanto, a probabilidade de sucesso deYép = l- q = l-0,9
= 0,1. Como a probabilidade de sucesso não é a mesma, não temos uma distribuição binomial.
Gabarito: Errado.

Item. 19. (Cebraspe/2015 - Telebrás) Um vendedor de certo tipo de equipamento de telecomunicações pode visitar, em um dia, um ou dois clientes, com probabilidades de 1/3 e 2/3,respectivamente. De cada contato pode resultar a venda de um equipamento por R$ 50.000, com probabilidade de 1/10 ou nenhuma venda,com probabilidade de 9/10. Considerando que V seja a variável aleatória que indica o valor total de vendas diárias desse vendedor, em milhares de reais, julgue o item que se segue.
Supondo-se que Xi seja a variável aleatória que indica o número de visitas do vendedor a clientes no i-ésimo dia do mês de novembro, que Yi = Xi - 1 e que Z = Y1 + Y2 + ... + Y30, é correto afirmar que Z será uma distribuição binomial de parâmetros n = 30 e p = 2/3.
Comentários:

O enunciado informa que Xi representa o número de clientes visitados em no dia i e que assume apenas dois valores possíveis (1 ou 2). Sabemos também que a probabilidade P(X = 1) = 1/3 e P(X = 2) = 2/3.
Dessa forma, Yi =Xi - 1 corresponde ao número de clientes visitados no dia, menos 1.
Assim, temos P(Y = 0) =
P(X = 1) = 1/3 e P(Y = 1) = P(X = 2) = 2/3. Portanto, Y segue distribuição de
Bernoulli, com probabilidade p = P(Y

= 1) = 2/3.

A questão informa, ainda, que Z corresponde à soma de 30 variáveis Y. Considerando que todas apresentam a mesma probabilidade p = 2/3, então Z segue uma distribuição binomial, com parâmetros n = 30 e p =2/3.

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 20. (Cebraspe/2015 - Telebrás) Nas chamadas de suporte de uma empresa de telecomunicações, o funcionário Pedro resolve o problema do cliente em duas de cada três vezes em que é solicitado, enquantoMarcos resolve em três de cada quatro chamadas.

A partir dessa situação hipotética, julgue o item seguinte, considerando que os funcionários sejam suficientemente experientes para que a tentativa de resolução do problema de qualquer chamada não esteja subordinada a tentativas anteriores.
A probabilidade de que Marcos consiga resolver o problema do cliente em exatamente três das quatro últimas chamadas em que foi solicitado é superior a 50%.
Comentários:

Considerando que há apenas dois resultados possíveis para cada chamada,
resolvida ou não, e que há 4
chamadas, então temos uma distribuição binomial com n = 4. Considerando que Marcos resolve 3 a cada 4chamadas, então a probabilidade de Marcos resolver (sucesso) é p = %. Logo, a probabilidade de Marcos não resolver (fracasso) éq = l- p = l- % = %.
Dessa forma, a probabilidade de Marcos resolver exatamente 3 de 4 chamadas é:

PCX = k) = Cn>k.pk.qn~k

4! 33

27 _ 27

P(X = 3)

Que é inferior a 0,5 = 50%

Gabarito: Errado.

ãTlJ X 43 x 41

4*_ 64 =

0,42

Item. 21. (Cebraspe/2013 - STF) Pedro e João são os oficiais de justiça no plantão do fórum de determinado município. Em uma diligência distribuída a Pedro, X é a variável aleatória que representa o sucesso(X = 1) ou fracasso (X = 0) no cumprimento desse mandado. Analogamente, Y é a variável aleatória que representa o sucesso (Y = 1) ou fracasso (Y = 0) de uma diligência do oficial João.
Com base nessa situação hipotética e considerando a soma S = X + Y, e que P(X = 1) = P(Y = 1) = 0,6
e E(XY) =
0,5, julgue o item que se segue, acerca das variáveis aleatórias X, Y e S.

A variável aleatória S segue uma distribuição binomial com parâmetros n = 2 e p = 0,6.

Comentários:

A distribuição binomial consiste na repetição de n experimentos de Bernoulli independentes. Assim, para que S
= X + Y siga a distribuição binomial, é necessário que X e Y sejam independentes.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Segundo as propriedades da esperança, temos que se as variáveis são independentes, então:

E(X. y) = E(X) x E(V)

Na questão anterior, calculamos E(X) = E(Y) = 0,6, logo:

E(X) x E(r) = 0, 6 x 0,6 = 0, 36

O enunciado informa que E(X.Y) = 0,5, logo E(X. K) #= E(X) x E(K) e,
consequentemente, as variáveis não são independentes.
Portanto, a soma S = X + Y não segue uma distribuição binomial.
Gabarito: Errado.

Item. 22. (CESPE/2012 - Câmara dos Deputados) Considere que, em um estudo realizado para avaliar a disponibilidade de 40 urnas eletrônicas para uso imediato, Y seja o número dessas urnas, que apresentavam problemas técnicos e que, historicamente, a probabilidade de uma urna apresentar defeito seja igual a 0,08.Considere, ainda, que as urnas sejam mutuamente independentes e que 0,036 e 0,039
sejam os valores aproximados, respectivamente, de O,9240 e 0,9239.
Com base nessas informações, julgue o item abaixo.

O número esperado de Y nesse lote é superior a 3 e menor ou igual a 4, enquanto o desvio padrão de Y se encontra dentro do intervalo [1,2],
Comentários:

Considerando que Y é o número de urnas que apresentam problemas e que, para cada urna há apenas 2resultados disponíveis (defeito ou não), então Y tem distribuição binomial com parâmetros p = 0,08 e n = 40. Ovalor esperado é então:

E(y) = np = 40 x 0,08 = 3,2

E a variância é, sendo q = l- p = l-0,08 = 0,92:

y(y) = npq = 40 x 0, 08 x 0,92 = 2,944

O desvio padrão, raiz quadrada da variância, é então:

o = JVÇX) = 72,944 = 1,7

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 23. (CESPE/2012 - SEDU-ES) Suponha que, em determinado país, 30% das crianças tenham algum tipo de dificuldade de aprendizagem.
Considerando que a população de crianças nesse país seja muito grande, tomando-se uma amostra aleatória de
10 crianças, a probabilidade de se encontrar nessa amostra exatamente três crianças com algum tipo de dificuldade de aprendizagem é superior a 0,15.
Comentários:

O número de crianças com dificuldade de aprendizagem encontrado em uma amostra de tamanho 10 segue distribuição binomial com parâmetros n = 10 e p = 0,3.
A probabilidade de encontrar exatamente 3 crianças com dificuldade, sendo q = 1 - p = 0,7, é:

Gabarito: Certo.

Item. 24. (CESPE/2011 - SEDUC-AM) Considere que a chegada e o atendimento de estudantes em determinada fila para matrícula em uma escola possam ser modelados segundo um passeio aleatório simples em tempo discreto t = 0,1, 2, 3 ... e que, em cada instante t, apenas dois eventos sejam possíveis: ou um novo estudante entra na fila com probabilidade p ou um estudante na fila é atendido com probabilidade 1 - p.Suponha, ainda,
que, no instante inicial t = 0, a quantidade de estudantes na fila não seja nula e grande o suficiente para que a fila não fique vazia em pouco tempo, e que, a cada instante t, no máximo um estudante pode ser atendido.
Com base nessa situação, julgue o item a seguir.

Na situação em que se consideram apenas os dois instantes iniciais, sendo t = 1 e t = 2, ep =
0,6, é mais provável que a fila não cresça.
Comentários:

A cada instante t, há apenas duas possibilidades, aluno entra na fila (sucesso) ou aluno atendido (fracasso).Considerando que a questão pede por 2 instantes, temos uma distribuição binomial com parâmetros p = 0,6 e n = 2.
A probabilidade de a fila não crescer é igual à probabilidade de um aluno entrar na fila e outro sair, nos dois instantes, dada por:
PÇX = k) = CnkPkqn~k

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

P(X = 1) = C210,610,4o = 2 x 0,6 x 0,4 = 0,48

Logo, a probabilidade de não crescer é menor do que a probabilidade de ela não crescer ou de ela crescer.
Gabarito: Errado.

Item. 25. (CESPE/2011 - EBC) Considerando uma sequência de lançamentos de Bernoulli, julgue o item subsecutivo.
Se, de uma urna em que há nA bolas da cor azul e nv bolas da cor vermelha,
forem retiradas, simultaneamente,
n bolas (n < nA + nv < °°) e o número X de bolas da cor azul for registrado,
então a distribuição de X seguirá uma distribuição binomial.
Comentários:

Considerando que a população é finita (nA + nv < °o) e que as bolas são retiradas simultaneamente, ou seja, sem reposição. Consequente, as extrações não serão independentes umas das outras e, por isso, X não seguirá uma distribuição binomial.
Gabarito: Errado.

Item. 26. (CESPE/2010 - ABIN) A respeito da distribuição binomial X com parâmetros n e p, em que n
> 1 e 0 < p

< 1, julgue o item subsequente.

Considere a seguinte situação hipotética. De uma urna que contém 15 bolas brancas e 1
bola vermelha serão retiradas aleatoriamente 12 bolas. Em cada retirada, será observada a cor da bola selecionada. Se branca, a bola não será devolvida à urna; se vermelha, a bola será devolvida à urna. Ao final do processo, será registrado o número X de vezes que a bola vermelha foi observada nessas doze retiradas. Em face dessa situação, é correto afirmar que X é uma variável aleatória com distribuição binomial com n = 12.
Comentários:

Como a população é de 16 bolas (finita) e que não há reposição de todas as bolas retiradas, as extrações não são independentes. Logo, X não segue uma distribuição binomial.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 27. (CESPE/2010 - ABIN) Considerando-se que Y siga uma distribuição binomial com parâmetros m e p e que X e Y sejam variáveis aleatórias independentes, é correto afirmar que a soma X + Y segue uma distribuição binomial com parâmetros (n + m) e p.
Comentários:

O enunciado informa que X segue distribuição binomial com parâmetros n
(número de ensaios de X) e p
(probabilidade de sucesso); que Y segue distribuição binomial com parâmetros m (número de ensaios de Y) e p(probabilidade de sucesso); e pergunta pela distribuição da soma das variáveis.

A soma de variáveis com distribuição binomial com mesma probabilidade de sucesso p corresponde a uma nova distribuição binomial, com o mesmo parâmetro p, em que o número de ensaios corresponde à soma dos números de ensaios.
Logo, a soma X + Y, de fato, segue distribuição binomial com parâmetros n + m e p.

Gabarito: Certo.

Item. 28. (CESPE/2010 - ANEEL) Um fabricante de impressoras possui três fornecedores — I, II e III
— de um certo circuito eletrônico. Para a produção de um lote de 100 impressoras, a fábrica dispõe de 50, 30 e 20circuitos fornecidos, respectivamente, por I, II e III.

As probabilidades de que um circuito fornecido por I, II ou III apresente defeito são, respectiva mente, iguais a 0,01, 0,03 e 0,05. Depois da produção do lote, m impressoras serão selecionadas aleatoriamente para testes de qualidade. Um indicador de qualidade da empresa é a razão f = n/m, em que n é o número observado de impressoras com defeitos no circuito.
Considerando as informações acima, julgue o item abaixo.

Dos circuitos disponíveis no estoque, o número esperado de circuitos defeituosos é menor ou igual a
2.

Comentários:

Do lote de 100 impressoras, o número esperado de peças defeituosas para cada fornecedor é:
I -> E(Xi) = ni.pi = 50.0,01 = 0,5

II- > E(X2) = n2.p2 = 30.0,03 = 0,9

III- > E(X3) = n3.p3 = 20.0,05 = 1

Logo, o total é:

1 + 11 + 111 = 0,5 + 0,9 + 1 = 2,4

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 29. (CESPE/2010 - PREVIC) Considerando que, a fim de verificar se o pagamento de determinado benefício estava de acordo com critérios definidos, um analista tenha selecionado uma amostra aleatória de 100pessoas, entre os 2.000 beneficiários existentes na base de dados, e considerando, ainda, que p representa a proporção populacional de benefícios corretamente pagos, julgue o próximo item.
Sabendo que a probabilidade de uma pessoa estar dentro dos critérios requeridos pelo benefício é 0,9, a probabilidade de exatamente 2 pessoas observadas na amostra estarem dentro dos critérios requeridos pelo benefício é superior a 0,10.
Comentários:

Podemos verificar a afirmativa utilizando uma distribuição binomial. Neste caso,
vamos considerar como
"probabilidade de sucesso" a probabilidade de uma pessoa estar dentro dos critérios requeridos e a negativa como probabilidade de fracasso. Portanto, p = 0,9 (probabilidade de sucesso, isto é,estar dentro dos critérios);
n é o número de ocorrências, ou seja, número de pessoas da amostra, portanto n =
100; e k é a quantidade de pessoas dentro dos critérios, neste caso k = 2. Logo:
P(X = /c) = Cn,k.pfe.qn-k
P(X = 2) = C100>2. (0,9)2. (0,l)98

Para facilitar a visualização, vamos considerar que 0,1 = 1/10 = 10-1:

100 x 99

P(X = 2) = 0,81 x 10-98 = 40 0 9,5 x 10"98 = 4 x 10-95

Esse valor é muito inferior a 0,10.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Distribuição Geométrica

Item. 1. (Cebraspe/2015 - Engenheiro Mecânico MEC) Considerando que a demanda diária por serviços de manutenção em certa instituição seja uma variável aleatória discreta N com função de probabilidade definida como P(N = n) = 0,8 x 0,2n, em que n = 0,1, 2, 3, b, julgue o próximo item.
A moda da distribuição N é igual ou superior a 1.

Comentários:

Vamos utilizar a tabela de distribuição para calcular a probabilidade de alguns valores da variável aleatória:
X P(x)

0 0,8x0,2°=0,8

1 0,8x0,2^0,8x0,2=0,16

2 0,8x0,22=0,8x0,04=0,032

3 0,8x0,23=0,8x0,008=0,0064

4 0,8x0,24=0,8x0,0016=0,00128

Veja que a probabilidade reduz conforme x aumenta. Portanto, a moda é x = 0.
Como 0 < 1, então o item está errado.

Gabarito: Errado.

Item. 2. (Cebraspe/2015 - Engenheiro Mecânico MEC) Considerando que a demanda diária por serviços de manutenção em certa instituição seja uma variável aleatória discreta N com função de probabilidade definida como P(N = n) = 0,8 x 0,2n, em que n = 0,1, 2, 3, b, julgue o próximo item.
A média da variável aleatória N é menor que 1.

Comentários:

Trata-se de uma variável com distribuição geométrica, com a parametrização alternativa, isto é, em que a variável representa o número de fracassos obtidos até o primeiro sucesso. Amédia (esperança) dessa distribuição é dada por:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Pela função de probabilidade fornecida pelo enunciado, observamos que p = 0,8 e q = 0,2, logo:

0,2

Em=^=°,25

Que é menor que 1.

Gabarito: Certo.

Item. 3. (Cebraspe/2015 - Engenheiro Mecânico MEC) Considerando que a demanda diária por serviços de manutenção em certa instituição seja uma variável aleatória discreta N com função de probabilidade definida como P(N = n) = 0,8 x 0,2n, em que n = 0,1, 2, 3, b, julgue o próximo item.
A probabilidade de X ser superior a 3 é inferior a 50%.

Comentários:

Considerando que X representa a quantidade de decisões até a ocorrência da primeira desfavorável, X apresenta distribuição geométrica. A probabilidade de X = k, para k = 1, 2, 3,..., é dada por:
P(X = k) = qk^.p

A probabilidade de fracasso (decisão favorável) é q = %, conforme enunciado. Assim, a probabilidade de sucesso(decisão desfavorável) é p = 1 - q = %.

A probabilidade de X > 3 é igual a:

P(X > 3) = 1 - P(X = 1) - P(X = 2) — P(X = 3)
P(X = 1) = p = i

P(X = ^ = ^ = 34X-4 = T6

/3\2 1 9
pa = 3) = ^.p = (₅) x-=-

Logo:

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 4. (Cebraspe/2016 - TCE/PA) Considere que Y seja uma variável aleatória que representa o número de erros cometidos por um atendente no preenchimento de formulários e que a função de probabilidade de Yseja definida por P(Y = fc) = 0,9 x (0, l)k, em que k = 0,1, 2,.... A partir dessas informações, julgue o item que se segue.
A distribuição Y é amodal

Comentários:

A moda de uma distribuição é X = 1, pois este valor está associado à maior probabilidade da distribuição. Como existe uma moda, a distribuição não é amodal (sem moda).
Gabarito: Errado.

Item. 5. (Cebraspe/2016 - TCE/PA) Considere que Y seja uma variável aleatória que representa o número de erros cometidos por um atendente no preenchimento de formulários e que a função de probabilidade de Yseja definida por P(Y = fc) = 0,9 x (0, l)k, em que k = 0,1, 2,.... A partir dessas informações, julgue o item que se segue.
P(Y > 2) = 0,01.

Comentários:

Sabemos que a probabilidade de todos os valores possíveis para Y é igual a 1:

P(Y > 2) = 1 - P(Y = 0) - P(Y = 1)

Pela função probabilidade apresentada, temos:

P(Y = 0) = 0,9 x (0,1)° = 0,9 x 1 = 0,9

P(Y = 1) = 0,9 x (04)1 = 0,9 x 0,1 = 0,09

Portanto:

P(Y > 2) = 1 - 0,9 - 0,09 = 0,01

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (Cebraspe/2016 - TCE/PA) Considere que Y seja uma variável aleatória geométrica que representa o número de erros cometidos por um atendente no preenchimento de formulários e que a função de probabilidade de Y seja definida por P(Y = k) = 0,9 x (0,l)k, em que k = 0,1,2,... A partir dessas informações,
julgue o item que se segue.

O desvio padrão da variável Y é inferior a 1.

Comentários:

Observa-se que a questão apresenta a segunda forma de parametrização da distribuição geométrica, da forma:P(Y = k) = qk.p, com k = 0, 1, 2,..., com q = 0,1 e p = 0,9.

A variância (que não se altera com o tipo de parametrização) é dada por:

q 0,1 0,1 10

(0,9)2 Õ81 _ 81

O desvio padrão, raiz quadrada da variância, é dado por:

, VTõ a = #(F) = — = 0,35
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Distribuição de Poisson

Item. 1. (CESPE/2010 - DETRAN-ES/Estatístico) Considerando que foi realizado estudo para modelar a distribuição da quantidade X de pontos acumulados por infrações de trânsito cometidas por um condutor de veículo de passeio ao longo de um ano, julgue o item a seguir, relativos a probabilidades e inferência estatística.
Nessa situação, caso X siga uma distribuição de Poisson com desvio padrão o, o coeficiente de variação de Xserá igual a

<7

Comentários:

O coeficiente de variação é a razão entre o desvio padrão e a média:

cr

Cy = ~

Sendo cr o desvio padrão, a variância será V(X) = o-2-

Na distribuição de Poisson, temos E(X) = V(X). Assim, n = E(X) = a2.

Substituindo na fórmula do coeficiente de variação, temos:

o 1

Gabarito: Certo.

Item. 2. (Cebraspe/2018 - PF/Papiloscopista) Em determinado município, o número diário X de registros de novos armamentos segue uma distribuição de Poisson, cuja função de probabilidade é expressa por e-M
P(X = k) = ——— em que k = 0,1,2,..., e M é um parâmetro.

dia

1 2 3 4 5

realização da variável X 6 8 0 4 2

Considerando que a tabela precedente mostra as realizações da variável aleatória X em uma amostra aleatória simples constituída por cinco dias, julgue o item que se segue.
Como a tabela não contempla uma realização do evento X = 7, é correto afirmar que P(X = 7) = 0.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Trata-se de uma distribuição de Poisson. A probabilidade de X = 7 é dada por:

P(X = /c)

e"ÂAk kl
6 ^7?

P(X = 7)=^-^0

Gabarito: Errado.

Item. 3. (CESPE/2011 - SEDUC-AM/Estatístico) Para orientar os investimentos em educação em certo município, um analista foi contratado para criar um ranking das escolas públicas desse município.Para cada escola, as variáveis disponíveis são a quantidade de turmas, a quantidade de alunos, a quantidade de professores, a nota da Prova Brasil e a área do terreno. A partir dessa situação, julgue o item subsequente.
Suponha que a distribuição da quantidade de turmas por escola siga uma distribuição de Poisson. Nessa situação, o modelo que descreve essa distribuição pode ser escrito como P(X = fc) =Ae~Ák, em que k > 0 e
A > 0 representa a média de turmas por escola.

Comentários:

Em uma distribuição de Poisson, a probabilidade de X = k é dada por:

e-ÂAk ppf=/I)=
Gabarito: Errado.

Item. 4. (CESPE/2010 - MPU/Analista) Uma empresa possui um serviço de atendimento ao consumidor
(SAC).
Diariamente, um atendente registra, em uma folha de papel, as chamadas recebidas. Cada folha de registro do atendente do SAC permite o registro de até 20 chamadas. O atendente efetua os registros de forma sequencial, anotando, para cada chamada, se houve reclamação. De acordo com os dados históricos,sabe-se que, a cada 20 chamadas, a probabilidade de se registrar exatamente uma reclamação é constante e igual a0,05. Sabe-se também que o número médio diário de reclamações registradas pelo SAC é igual a 1.

Com base nessas informações e considerando 2,71 como valor aproximado para o número e,
base do logaritmo natural, julgue o item.
Suponha que o número diário de reclamações registradas pelo SAC siga uma distribuição de Poisson. Nessa situação, a probabilidade de haver o registro de, no máximo, uma reclamação em determinado dia é superior a67%.

Coment®HRPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A probabilidade de haver no máximo 1 reclamação é igual a:

< 1) = P(X = 0) + P(X = 1)

Para a distribuição de Poisson, a probabilidade P(X = k):

P(X = k) =

Logo, com 2 = 1, temos:

e~\Xk kl
P(x = 0) =

0!

, . e'1!1

P(X = 1) =

Assim:

Gabarito: Certo.

Item. 5. (CESPE/2010 - MPU/Analista) Uma empresa possui um serviço de atendimento ao consumidor
(SAC).
Diariamente, um atendente registra, em uma folha de papel, as chamadas recebidas. Cada folha de registro do atendente do SAC permite o registro de até 20 chamadas. O atendente efetua os registros de forma sequencial, anotando, para cada chamada, se houve reclamação. De acordo com os dados históricos,sabe-se que, a cada 20 chamadas, a probabilidade de se registrar exatamente uma reclamação é constante e igual a0,05. Sabe-se também que o número médio diário de reclamações registradas pelo SAC é igual a 1.

Com base nessas informações e considerando 2,71 como valor aproximado para o número e,
base do logaritmo natural, julgue o item.
Suponha que o número de reclamações registradas pelo SAC, X(t), em um intervalo de tempo t, siga um processo de Poisson e que X(l) represente o número diário de reclamações registradas. Nessa situação, é correto afirmar que a variância de X(t) cresce linearmente com t.
Comentários:

Pelo enunciado, podemos afirmar que t representa o número de dias da análise.
Considerando que precisamos ajustar o valor de 2 de acordo com o número de dias da análise e que há uma reclamação por dia, temos 2 = t,ou seja, há t reclamações a cada t dias.

A variância em uma distribuição de Poisson é V(X) = 2, ou seja, V(X) =
t. Portanto, a variância cresce linearmente com t.
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (CESPE/2010 - TRE-ES/Analista Judiciário) Uma empresa iniciou suas atividades com R$ 30
mil de capital. O custo fixo mensal da empresa é de R$ 5 mil. As vendas de seus produtos ocorrem segundo um processo de Poisson, com taxa igual a R$ 1 mil por mês. A empresa fechará no momento que o seu capital for igual ou inferior a zero. Com base nessa situação, e considerando exp(- 6) = 0,0025, julgue o item seguinte.
A probabilidade de a empresa sobreviver além do sexto mês de funcionamento é inferior a 0,95.
Comentários:

A probabilidade de a empresa sobreviver além do sexto mês é o complementar da probabilidade de a empresa falir em até 6 meses. Considerando que o custo fixo mensal é de R$ 5.000, em 6meses, o custo fixo total terá sido de 6 x R$ 5.000 = R$ 30.000. Esse valor é igual ao capital inicial. Assim, a empresa irá falir(terá o seu capital igual a zero) nesse período apenas se não realizar venda durante 6 meses.
Considerando que a média de vendas é de R$ 1.000 por mês, então em 6 meses, a média de vendas é de
R$

Item. 6.000. Assim, a probabilidade P(X = 0), com A = 6, é:

P(X = k~)

e~66°

e~ÁAk kl
P(X = 0) = —— = e~6 = 0,0025

Logo, a probabilidade de a empresa sobreviver é:

P(X > 0) = 1 - = 0) = 0, 9975

Gabarito: Errado. 7

Item. 7. (Cebraspe/2013 - ANTT-DF/Área Estatística)

A figura acima apresenta um trecho de uma rodovia com três faixas de rolamento.
Considere que X(t)

represente o número de veículos que passam nesse trecho durante um intervalo de tempo de duração t
(em e f6minutos) e que X(t) siga um processo de Poisson com parâmetro 6t, ou seja, P(X(t) = x) = ———.
Suponha,

ainda, que, no intervalo t, cada veículo selecione aleatoriamente as faixas de rolamento 1, 2 e 3
com probabilidades 0,5; 0,3 e 0,2, respectivamente. Com base nessas informações, julgue o próximo item.
O número de veículos que passam nesse trecho pela faixa de rolamento 3 durante um intervalo de tempo de duração t (em minutos) segue um processo de Poisson com parâmetro l,2t.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

O número de veículos que passam nesse trecho segue uma distribuição de Poisson, com parâmetro Ax = 6t e média E(X) = A = 6t. Considerando que 20% desses veículos passam pela faixa 3, ou seja, X3 = 0,2.X, então,pelas propriedades da esperança, temos:

E(X₃) = E(0,2X) = 0, 2E(X) = 0, 2 x 6t = 1,2t

Sabendo que a média da distribuição de Poisson é igual ao seu parâmetro, então, AXs = 1,2t.
Gabarito: Certo.

Item. 8. (CESPE/2012 - CNJ/Analista Judiciário) A quantidade de chamadas que uma central telefônica recebe por hora é modelado por uma distribuição de Poisson, com parâmetro À = 12 chamadas por hora. Nesse caso,a probabilidade de a central telefônica receber:

menos de três chamadas em uma hora é igual a 85e-12.
Comentários:

A probabilidade de receber menos de 3 chamadas corresponde a:

< 3) = P(X = 0) + = 1) + P(X = 2)

Em uma distribuição de Poisson, a probabilidade de [X = k] é dada por:

e~ÁAk

Sendo A = 12, logo:

p,x=kl= k<

e_1212° e"12l 17

Kx = o)= 0, = t = e-12

e_12121
P(X = 1) = —-— = 12e-12

1!

e"12122 e_12.144

P(X = 2) = 2, =-------- - ------ = 72e-12

Portanto:

P(X < 3) = e"12 + 12e"12 + 72e"12 = 85e"12

Gabarito: Certo.

Item. 9. (CESPE/2012 - CNJ/Analista Judiciário) A quantidade de chamadas que uma central telefônica recebe por hora é modelado por uma distribuição de Poisson, com parâmetro À = 12 chamadas por hora. Nesse caso,a probabilidade de a central telefônica receber:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

exatamente duas chamadas em 20 minutos é igual a — e

6!

Comentários:

Em uma distribuição de Poisson, a probabilidade de [X = k] é dada por:

e-Â2k

P(X = fc)

kl

Pontue-se que a pergunta se refere a chamadas em 20 minutos, enquanto o parâmetro foi informado por hora,sendo 1 hr = 60 minutos = 3 x 20 minutos. Logo, o valor do parâmetro a cada 20 minutos é:

A = T = 4

Assim, a probabilidade de [X = 2] é:

P(X = 2) =

e-4 42

= 8e-4

Gabarito: Errado.

Item. 10. (Cebraspe/2013 - MC/Análises Técnicas) A quantidade diária de reclamações — X
— recebidas em uma central de atendimento ao consumidor segue uma distribuição de Poisson, em que P(X = 0) = 0,5.Nesse sentido, julgue o próximo item.
O valor esperado de X é igual a In2.

Comentários:

Para resolver essa questão, vamos encontrar o valor do parâmetro da distribuição, np = A, a partir da informação de que P(X = 0) = 0,5:
p(x = k)=^F

x e-Â2k e~*A° e~*. 1 j
= 0) = FF" = FF = e = °'5

Pela definição de logaritmo, podemos escrever e~Á = 0,5 como:

—A = loge 0,5

Sabendo que In é o logaritmo na base e, temos:

—A = ln 0,5

Como a questão trata de In 2, vamos representar 0,5 = % como 2 1 e aplicar a propriedade do logaritmo:
A = — ln(2_1) = —(—1 x ln 2) = ln 2

LogO, E()^RfifrôQ,êStatíStjCa e Probabilidade - 2023 (Pós-Edital)

Gabarito: Certo.

Item. 11. (CESPE/2012 - ANP/Especialista) A respeito da teoria básica de probabilidades, julgue o item subsequente.
Se uma variável aleatória de Poisson é tal que 2- P(X = 4) = P(X = 3), a média de X é 0,5.

Comentários:

Para resolver essa questão, vamos encontrar o valor do parâmetro da distribuição, np = A, a partir da informação de que 2.P(X = 4) = P(X = 3). A probabilidade de X = k em uma distribuição de Poisson é:
x e-Â2k p(x = k)=^r
Logo:

e_1Â3
P(X = 3) = —

e_Â24
p(x = 4) = —

Assim, 2.P(X = 4) = P(X = 3) corresponde a:

Dividindo ambos os lados por e~ÀA3, temos:

e~ÁA4 e~ÁA3

2 4! 3!

Â 1
4x36

6A = 12

A = 2

Como F(X) = A, a média é igual a 2.

Gabarito: Errado.

Item. 12. (Cebraspe/2020 - TJ-PA/Analista Judiciário) Uma amostra aleatória simples de tamanho 5 foi retirada de uma distribuição de Poisson com média igual a 5. Essa amostra é representada porXi, X₂, X₃, X₄, X₅, em que cada variável Xk denota o total de erros processuais registrados em certo cartório judicial no dia k, com k
= {1, 2, 3, 4, 5}. A respeito da quantidade semanal de erros processuais registrados nesse cartório
Y = Xi + X₂

+ X3 + X4 +X5, assinale a opção correta.

a) O coeficiente de variação de Y é igual a 1.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

b) E(Y) < 20

c) O desvio padrão de Y é igual a 5.

d) Para k = 1, 2, 3, 4, 5, tem-se que P(Y = 0) >= P(Xk = 0)

e) A média semanal de erros processuais, denotada por Y/5, segue uma distribuição normal.

Comentários:

Considerando que a média da distribuição de Poisson é Ax = 5 e sabendo que a soma de variáveis com distribuição de Poisson também apresenta distribuição de Poisson com parâmetro igual a soma dos parâmetros,temos:

AY = 5 + 5 + 5 + 5 + 5 = 25

Em relação à alternativa A, o coeficiente de variação de Y é dado por:

Em uma distribuição de Poisson, temos fiY = E(Y) = AY = 25. Também sabemos que
V(V) = AY = 25. Logo,
o desvio padrão é aY = ^V(Y) = V25 = 5. Assim, o coeficiente de variação é:

5 1

C,,"2S"5

Logo, a alternativa A está errada.

Em relação à alternativa B, vimos que E(Y) = AY = 25. Logo, a alternativa B está errada.

Em relação à alternativa C, vimos que aY = ^V(Y) = ^25 = 5. Logo, a alternativa C está correta.

Em relação à alternativa D, a probabilidade P(Y = 0) corresponde à probabilidade de todas as variáveis Xk serem iguais a zero (interseção), o que é bem menor que a probabilidade de uma única variável qualquer Xk ser igual a zero. Matematicamente, temos:
P(y = 0) = e"25

= 0) = e~5

Observa-se que e-25 < e~5, logo P(Y = 0) < P(Xk = 0). Logo, a alternativa D está errada.

Em relação à alternativa E, a média semanal de erros processuais segue distribuição de Poisson.
Logo, a alternativa E está errada.
Gabarito: C.

Item. 13. (Cebraspe/2013 - Analista Judiciário STF) As quantidades diárias de processos administrativos (A/)protocolados em certo órgão público seguem uma distribuição de Poisson com média igual a 5. Cada processo protoco!â£Hpft©n<^tftlA0Slefi^Siff«Rfèriiite9<^y:Ki^u para a B e, assim, a soma Y = ^=1Xh em que
1 se o processo segue para a superintendência A, e X, = 0 se o processo segue para B, representa o total diário de processos administrativos protocolados que se destinam para a superintendência A.
Com base nessa situação, julgue o seguinte item considerando que Xi, X₂,XN sejam variáveis aleatórias independentes, e que P(Xi = 1) = P(X₂ = 1) = ... = P(XN = 1) = 0,8.
A quantidade média diária de processos administrativos que se destinam para a superintendência A é igual a 4.
Comentários:

Considerando que as quantidades diárias de processos seguem uma distribuição de Poisson,
com média A = 5
e sabendo que a probabilidade de cada processo administrativo ser destinada à superintendência A é de 80%,então a média diária destinada a essa superintendência é:

Aa = 0,8 x 5 = 4

Gabarito: Certo

Item. 14. (Cebraspe/2013 - Analista Judiciário STF) As quantidades diárias de processos administrativos (A/)protocolados em certo órgão público seguem uma distribuição de Poisson com média igual a 5. Cada processo protocolado é encaminhado para a superintendência A ou para a B e, assim, a soma Y = Yí=i^í> em que X, =
1 se o processo segue para a superintendência A, e X, = 0 se o processo segue para B, representa o total diário de processos administrativos protocolados que se destinam para a superintendência A.
Com base nessa situação, julgue o seguinte item considerando que Xi, X₂,..., XN sejam variáveis aleatórias independentes, e que P(Xi = 1) = P(X₂ = 1) = ... = P(XN = 1) = 0,8.
O número diário de processos protocolados que são destinados à superintendência B segue uma distribuição de Poisson com média igual a 1.
Comentários:

Considerando que as quantidades diárias de processos seguem uma distribuição de Poisson,
com média A = 5
e sabendo que a probabilidade de cada processo administrativo ser destinada à superintendência B é 100% -80% = 20%, então a média diária destinada a essa superintendência é:

Aa = 0,2 x 5 = 1

Gabarito: Certo

Item. 15. (Cebraspe/2018 - Analista Administrativo EBSERH) O total diário - X - de pessoas recebidas em uma unidade de pronto atendimento (UPA) para atendimento ambulatorial, e o total diário - Y - de pessoas recebidas nessa mesma UPA para atendimento de urgência segue processos de Poisson homogêneos, <~nm
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edifal)
0 103

médias, respectivamente, iguais a 20 pacientes/dia e 10 pacientes/dia, e as variáveis aleatórias X e Y são independentes. Sabe-se que, em média, a necessidade de cuidados hospitalares atinge 10% dos pacientes do atendimento ambulatorial e 90% dos pacientes do atendimento de urgência.
A partir dessa situação hipotética, julgue o próximo item, considerando que o registro da necessidade de cuidados hospitalares seja feito no momento em que o paciente chegue à UPA e que Hseja a quantidade diária registrada de pacientes com necessidades de cuidados hospitalares.
Considerando a equivalência 1 dia=24 horas, então o tempo médio de chegada entre dois pacientes consecutivos para o atendimento de urgência nessa UPA é inferior a 3 horas.
Comentários:

Sabendo que Y representa o total diário de pessoas recebidas em uma UPA para atendimento de urgência, com média de 10 pacientes/dia, então a média de tempo entre dois pacientes é:
Como 2,4 é inferior a 3, então o item está certo.

Gabarito: Certo

Item. 16. (Cebraspe/2013 - Estatístico FUB) Tendo em vista que o número diário X de recursos administrativos protocolados em certa repartição pública segue uma distribuição de Poisson com taxa igual a InlOprocessos por dia, julgue o item que se segue.
O desvio padrão da distribuição de X é inferior a InlO processos por dia.

Comentários:

Sabendo que X segue uma distribuição de Poisson com média In 10 (À = In 10), então o desvio padrão é dado por:
a = y/V(X) =4Ã = VlnlO

Como ln 10 > 1, então o = Vln 10 < ln 10.

Gabarito: Certo

Item. 17. (Cebraspe/2013 - Estatístico FUB) Tendo em vista que o número diário X de recursos administrativos protocolados em certa repartição pública segue uma distribuição de Poisson com taxa igual a InlOprocessos por dia, - 2023 (Pós-Edital)
A distribuição do número diário de recursos administrativos apresenta coeficiente de variação igual a 1.
Comentários:

Sabendo que X segue uma distribuição de Poisson com média In 10 (À = In 10), então o coeficiente de variação é dado por:
r cr VÃ Vln 10

= jz = T = lnlO

Como Vln 10 < ln 10, então Cv < 1.

Gabarito: Errado.

Item. 18. (Cebraspe/2013 - Estatístico FUB) Tendo em vista que o número diário X de recursos administrativos protocolados em certa repartição pública segue uma distribuição de Poisson com taxa igual a lnlOprocessos por dia, julgue o item que se segue.
Em determinado dia, a probabilidade de não haver recurso protocolado é igual ou inferior a 0,1.

Comentários:

Sabendo que X segue uma distribuição de Poisson com média In 10 (À = In 10), então a probabilidade P(X = 0) é dada por:
P(X = 0) = e"Â = e_lnl°

Considerando a propriedade b~a = temos:

P(x = o) = e-lnlo = ;ilF

Pelas propriedades do logaritmo, temos &lo&>a = a, isto é, a base b elevada ao logaritmo (expoente) de a na base b é justamente igual a. Logo, elnl° = 10:
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 19. (Cebraspe/2013 - Estatístico FUB) Tendo em vista que o número diário X de recursos administrativos protocolados em certa repartição pública segue uma distribuição de Poisson com taxa igual a InlOprocessos por dia, julgue o item que se segue.
A distribuição de Poisson não possui memória, pois P(X = k | X > 1) = P(X = k - 1), em que k > 1.

Comentários:

A probabilidade condicional é calculada como:

P(X = k nx > 1) P(X = k)

pçx = kix>»= PÍXÍ1) =p(X£1)

Considerando que X segue distribuição de Poisson, então:

e-Â.Âk

/>(%=«= k!

Sabemos, ainda, que:

P(X > 1) = 1 - P(X < 1) = 1 - P(X = 0)
P(x = 0) = e~Á

Logo:

P(X > 1) = 1 - e~*

Então, a probabilidade condicional é dada por:

P(X = /c|X>l)=—

1 - e Á

e~Á.Ak kl (1 - e-A)
Por outro lado, P(X = k - 1) é dada por:

P(X = k- 1) (fc - 1)!

Logo, temos P(X = k\X > 1) =# P(X = k — 1).

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 20. (Cebraspe/2016 - Analista de Controle TCE/PR) Suponha que o número mensal X
de pessoas que sofrem algum tipo de acidente em um centro comercial siga uma distribuição de Poisson.Considerando que
P(X = 0) = 0,1 e InlO = 2,3, assinale a opção correta.

a) A distribuição X possui desvio padrão igual ou superior a 2.

b) P(X>l) = 0,9

c) 0,20 < P(X = 1) < 0,25

d) P(X<0) >0

e) A esperança de X é igual ou superior a 3.

Comentários:

Sabendo X segue uma distribuição de Poisson e que P(X = 0) = 0,1, então:

P(X = 0) = e~Á = 0,1

Então, pela propriedade b~a = Q) , então:

Pela definição de logaritmo, temos:

A = lnlO = 2,3

A esperança de X (alternativa e) é E(X) = A = 2,3 (portanto, a alternativa e está errada).
A variância de X (alternativa a) é V(X) = A = 2,3. O desvio padrão é, portanto:

a = y/VÕ) = ^

Esse valor é menor que 2, então a alternativa a está errada.
A probabilidade P(X = 1) (alternativa c) é dada por:

P(X = 1) = A. e~A = 2,3 x 0,1 = 0,23

Como 0,20 < 0,23 < 0,25, então a alternativa c está correta.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A probabilidade P(X > 1) (alternativa b) é igual a:

P(X > 1) = 1 - P(X=0) — P(X = 1) = 1 — 0,23 - 0,1 = 0,67

Portanto, a alternativa b está errada.

Em relação à alternativa d, a distribuição de Poisson vale para X = 0, 1, 2, ...,
n. Então P(X < 0) = 0 ou seja, a alternativa d está errada.
Gabarito: C

Item. 21. (Cebraspe/2015 - Estatístico FUB) Uma repartição pública recebe diariamente uma quantidade X de requerimentos administrativos e uma quantidade/de recursos administrativos.Essas quantidades seguem distribuições de Poisson com taxas, respectivamente, iguais a Inl5 requerimentos por dia e /n4recursos por dia.

Considerando que, nessa situação hipotética, as variáveis aleatórias X e Y
sejam independentes e que S = X+Y, julgue o seguinte item.
Em determinado dia, a probabilidade de não haver recebimento de requerimento administrativo nessa repartição será inferior a 0,08.
Comentários:

A probabilidade de não haver recebimento de requerimento é dada por:

P(X = 0) = e"Â = e~ln15

Considerando a propriedade b~a = ± bem como blogba = a, logo:

P(/ = 0) = e-'"ls=?A5 = i = 0,067

Gabarito: Certo

Item. 22. (Cebraspe/2015 - Estatístico FUB) Uma repartição pública recebe diariamente uma quantidade X de requerimentos administrativos e uma quantidade/de recursos administrativos.Essas quantidades seguem distribuições de Poisson com taxas, respectivamente, iguais a Inl5 requerimentos por dia e /n4recursos por dia.

Considerando que, nessa situação hipotética, as variáveis aleatórias
Xe/sejam independentes e que S = X + /, julgue o seguinte item.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A variância da distribuição de Y é igual a In4.

Comentários:

Sabemos que a para a distribuição de Poisson, temos E(Y) = V(Y) = Â. Portanto, V(Y) = In 4.

Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Distribuição Uniforme

Item. 1. (CEBRASPE/2022 - TCE/SC) Considerando uma sequência de variáveis aleatórias
{Xk}, em que
P(Xk = —0, 2fc) = P(Xk = 0,2fe) = 0, 5, para k E {1,2,...}, julgue o item a seguir, com relação à somaSn = Yk=íXk.

Xk segue distribuição uniforme discreta.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Distribuição de Bernoulli

Item. 1. (CESPE/2011 - SEDUC-AM)

RG(*)

35805684

21355706

43674475

2305386

gênero

M
F
M
F

grau de instrução hiperatividade
N
N
S
N

98814652 M 4 N

(*) números fictícios gerados por computador.

A tabela acima contém um conjunto de dados formado por quatro variáveis: RG; gênero ( M = masculino;
F = feminino); grau de instrução (1 = analfabeto; 2 = fundamental incompleto; 3 =
fundamental completo;
4 = médio incompleto; 5 = médio completo ou superior); e hiperatividade (S = sim; N
= não). Com base nessa tabela, julgue o item seguinte.
Com relação à variável dicotômica hiperatividade, atribuindo-se valor 1 para uma categoria e 0 para a outra,a média dessa variável binária representa a frequência relativa de observações que receberam valor
1.

Item. 2. (Cebraspe/2013 - MPU) As variáveis aleatórias X e Y seguem uma distribuição de Bernoulli com probabilidade de sucesso igual a 0,4. Considerando S = X + Y e que os eventos aleatórios A = [X =1] e B =
[Y = 1] sejam mutuamente exclusivos, julgue o item subsequente.

É correto afirmar que P(A U = P(S = 1) = 0,8.

Item. 3. (Cebraspe/2016 - TCE-PA) Se as variáveis aleatórias X e Y seguem distribuições de Bernoulli, tais que P[X = 1] = P[Y = 0] = 0,9, então:
A média de Y é superior a 0,5.

Item. 4. (Cebraspe/2016 - TCE-PA) Se as variáveis aleatórias X e Y seguem distribuições de Bernoulli, tais que P[X = 1] = P[Y = 0] = 0,9, então:
As variâncias de X e Y são iguais.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 5. (Cebraspe/2016 - TCE-PA) Se as variáveis aleatórias X e Y seguem distribuições de Bernoulli, tais que P[X = 1] = P[Y = 0] = 0,9, então:
A distribuição X2 é Bernoulli com média igual a 0,81.

Item. 6. (Cebraspe/2013 - STF) Pedro e João são os oficiais de justiça no plantão do fórum de determinado município. Em uma diligência distribuída a Pedro, X é a variável aleatória que representa o sucesso(X = 1)
ou fracasso (X = 0) no cumprimento desse mandado. Analogamente, Y é a variável aleatória que representa o sucesso (Y = 1) ou fracasso (Y = 0) de uma diligência do oficial João.
Com base nessa situação hipotética e considerando a soma S = X + Y, e que P(X = 1) = P(Y = 1) = 0,6
e E(XY)

= 0,5, julgue o item que se segue, acerca das variáveis aleatórias X, Y e S.

A média da distribuição S é igual a 1,2.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. CERTO

Item. 2. CERTO

Item. 3. ERRADO

Item. 4. CERTO

Item. 5. ERRADO

Item. 6. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Distribuição Binomial

Item. 1. (Cebraspe/2022 - PETROBRAS) Julgue o item a seguir, relacionados a álgebra e a probabilidade.
Cada uma de três moedas não viciadas, quando lançada, apresenta como resultado "cara"
ou "coroa". Ao se lançar essas três moedas, uma de cada vez, a probabilidade de se obter "cara" em duas delas e "coroa" em uma delas é superior a 0,4.
Item. 2. (Cebraspe/2022 - FUNPRESP-EXE) Em uma empresa há 100 produtos em estoque,
todos de igual aparência, mas com qualidades distintas, que só são evidenciadas com testes específicos:40 são de alta qualidade, 35 são de média qualidade e 25 são de baixa qualidade. Considerando essas informações e o procedimento de análise de uma amostra com 15 produtos, com reposição, julgue o item a seguir.
Espera-se que na amostra haja, em média, 6 produtos de alta qualidade.

Item. 3. (Cebraspe/2022 - FUNPRESP-EXE) Em uma empresa há 100 produtos em estoque,
todos de igual aparência, mas com qualidades distintas, que só são evidenciadas com testes específicos:40 são de alta qualidade, 35 são de média qualidade e 25 são de baixa qualidade. Considerando essas informações e o procedimento de análise de uma amostra com 15 produtos, com reposição, julgue o item a seguir.
Espera-se que na amostra haja, em média, 4 produtos de baixa qualidade.

Item. 4. (Cebraspe/2022 - PETROBRÁS) Considerando que a variável aleatória X segue uma distribuição binomial com parâmetros n = 10 e p = 0,1, julgue o item subsequente.
O valor esperado de X é igual a 1.

Item. 5. (Cebraspe/2022 - PETROBRÁS) Considerando que a variável aleatória X segue uma distribuição binomial com parâmetros n = 10 e p = 0,1, julgue o item subsequente.
O desvio padrão da distribuição de X é igual ou superior a 0,9.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (Cebraspe/2022 - PETROBRÁS) Considerando que a variável aleatória X segue uma distribuição binomial com parâmetros n = 10 e p = 0,1, julgue o item subsequente.
P(X > 0) = 0,9.

Item. 7. (Cebraspe/2022 - TELEBRÁS) Considere um par (X, Y) de variáveis aleatórias discretas, tais que
X~ Binomial (l0,0 e Y~Binomial (l0,0.

Sabendo que Cov(X, Y) = -1,1, julgue o seguinte item acerca da diferença Z = Y — X.

O valor esperado de Z é igual a 3.

Item. 8. (Cebraspe/2022 - TELEBRÁS) Considere um par (X, Y) de variáveis aleatórias discretas, tais que

X~Binomial (l0,0 e Y~Binomial (l0,0.

Sabendo que Cov(X, Y) = -1,1, julgue o seguinte item acerca da diferença Z = Y — X.

Var[Z] = 6,3.

Item. 9. (Cebraspe/2022 - TCE/SC) Suponha que uma amostra de tamanho n = 1 seja retirada de uma população X ~ BinomialÇm, p), em que m e p são parâmetros desconhecidos. Sabendo que m G {1,2}
e que p G se a amostra aleatória simples for representada por Xlt considere a seguinte estatística para a estimação do par (m,p).
m = lep = -,

m = 2ep = -,
Com base nessas informações, julgue o próximo item.

se Xr = 0

seX± = 1 ou 2

Se p denota a média populacional desconhecida, então seu espaço paramétrico é representado pelo conjunto
Item. 10. (Cebraspe/2021 - COREN/CE) Suponha que 20% dos recursos administrativos impetrados contra determinada decisão administrativa em uma repartição pública sejam deferidos. Nessa situação, se 4novos recursos administrativos forem distribuídos aleatoriamente para análise, a probabilidade de haver um único recurso deferido entre esses 4 recursos analisados é igual a
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 0,008

b) 0,1024

c) 0,25

d) 0,4096

Item. 11. (Cebraspe/2021 - SERPRO) Considerando que o número X de erros registrados em determinado tipo de código computacional siga uma distribuição binomial com média igual a 4 e variância igual a 3,julgue o item a seguir.

É impossível haver registros de 18 erros nesse tipo de código computacional.

Item. 12. (Cebraspe/2021 - SERPRO) Considerando que o número X de erros registrados em determinado tipo de código computacional siga uma distribuição binomial com média igual a 4 e variância igual a 3,julgue o item a seguir.

PÍX = 0) = 2.

Item. 13. (Cebraspe/2021 - SERPRO) Considerando que o número X de erros registrados em determinado tipo de código computacional siga uma distribuição binomial com média igual a 4 e variância igual a 3,julgue o item a seguir.

A mediana de X é igual a 4.

14.

(Cebraspe/2019 - TJ-AM) É igual a - a probabilidade de determinado advogado conseguir decisão favorável a si em cada petição protocolada por ele na vara cível de certo tribunal. O plano desse advogado é protocolar, sequencialmente, 12 petições nessa vara cível durante o ano de 2020. Favoráveis ou não, as decisões do tribunal para petições são emitidas na mesma ordem cronológica em que são protocoladas e são sempre independentes entre si. A partir dessa situação hipotética, julgue o próximo item,considerando as variáveis aleatórias X e Y, em que X = quantidade de decisões emitidas pelo tribunal até que ocorra a primeira decisão não favorável ao advogado, e Y = quantidade de decisões emitidas pelo tribunal favoráveis ao advogado.
Espera-se que, ao longo de 2020, exatamente 9 decisões sejam favoráveis ao advogado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 15. (Cebraspe/2019 - TJ/AM) É igual a - a probabilidade de determinado advogado conseguir decisão favorável a si em cada petição protocolada por ele na vara cível de certo tribunal. O plano desse advogado é protocolar, sequencialmente, 12 petições nessa vara cível durante o ano de 2020. Favoráveis ou não, as decisões do tribunal para petições são emitidas na mesma ordem cronológica em que são protocoladas e são sempre independentes entre si. A partir dessa situação hipotética, julgue o próximo item,considerando as variáveis aleatórias X e Y, em que X = quantidade de decisões emitidas pelo tribunal até que ocorra a primeira decisão não favorável ao advogado, e Y = quantidade de decisões emitidas pelo tribunal favoráveis ao advogado.
A probabilidade do evento "Y é igual a 1" é superior a —.

Item. 16. (Cebraspe/2019 - TJ/AM) É igual a - a probabilidade de determinado advogado conseguir decisão favorável a si em cada petição protocolada por ele na vara cível de certo tribunal. O plano desse advogado é protocolar, sequencialmente, 12 petições nessa vara cível durante o ano de 2020. Favoráveis ou não, as decisões do tribunal para petições são emitidas na mesma ordem cronológica em que são protocoladas e são sempre independentes entre si.
A partir dessa situação hipotética, julgue o próximo item, considerando as variáveis aleatórias X e Y, em que X = quantidade de decisões emitidas pelo tribunal até que ocorra a primeira decisão não favorável ao advogado, e Y = quantidade de decisões emitidas pelo tribunal favoráveis ao advogado.
A probabilidade de Y ser inferior a 2 é superior a 1%.

Item. 17. (Cebraspe/2018 - BNB) Julgue o próximo item, relativos a análise combinatória e probabilidade.
Situação hipotética: Para cada um dos 16 itens da prova objetiva de informática de um concurso público,o candidato deverá marcar na folha de respostas se o item é certo ou errado. A
condição para não desclassificação do candidato é que ele acerte o gabarito de pelo menos 10 desses itens.
Assertiva: Nesse caso, se o candidato marcar aleatoriamente todos os 16 itens, a probabilidade de ele não7x11x13

ser desclassificado é igual —.

Item. 18. (Cebraspe/2016 - TCE-PA) Se as variáveis aleatórias X e Y seguem distribuições de Bernoulli, tais que P[X = 1] = P[Y = 0] = 0,9, então:
X + Y segue uma distribuição binomial com parâmetros n = 2 e p = 0,3, se X e Y
forem variáveis aleatórias independentes.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 19. (Cebraspe/2015 - Telebrás) Um vendedor de certo tipo de equipamento de telecomunicações pode visitar, em um dia, um ou dois clientes, com probabilidades de 1/3 e 2/3, respectivamente. De cada contato pode resultar a venda de um equipamento por R$ 50.000, com probabilidade de 1/10 ou nenhuma venda,com probabilidade de 9/10. Considerando que V seja a variável aleatória que indica o valor total de vendas diárias desse vendedor, em milhares de reais, julgue o item que se segue.
Supondo-se que Xi seja a variável aleatória que indica o número de visitas do vendedor a clientes no i-ésimo dia do mês de novembro, que Yi = Xi - 1 e que Z = Y1 + Y2 + ... + Y30, é correto afirmar que Z será uma distribuição binomial de parâmetros n = 30 e p = 2/3.
Item. 20. (Cebraspe/2015 - Telebrás) Nas chamadas de suporte de uma empresa de telecomunicações, o funcionário Pedro resolve o problema do cliente em duas de cada três vezes em que é solicitado,enquanto
Marcos resolve em três de cada quatro chamadas.

A partir dessa situação hipotética, julgue o item seguinte, considerando que os funcionários sejam suficientemente experientes para que a tentativa de resolução do problema de qualquer chamada não esteja subordinada a tentativas anteriores.
A probabilidade de que Marcos consiga resolver o problema do cliente em exatamente três das quatro últimas chamadas em que foi solicitado é superior a 50%.
Item. 21. (Cebraspe/2013 - STF) Pedro e João são os oficiais de justiça no plantão do fórum de determinado município. Em uma diligência distribuída a Pedro, X é a variável aleatória que representa o sucesso(X = 1)
ou fracasso (X = 0) no cumprimento desse mandado. Analogamente, Y é a variável aleatória que representa o sucesso (Y = 1) ou fracasso (Y = 0) de uma diligência do oficial João.
Com base nessa situação hipotética e considerando a soma S = X + Y, e que P(X = 1) = P(Y = 1) = 0,6
e E(XY)

= 0,5, julgue o item que se segue, acerca das variáveis aleatórias X, Y e S.

A variável aleatória S segue uma distribuição binomial com parâmetros n = 2 e p = 0,6.

Item. 22. (CESPE/2012 - Câmara dos Deputados) Considere que, em um estudo realizado para avaliar a disponibilidade de 40 urnas eletrônicas para uso imediato, Y seja o número dessas urnas, que apresentavam problemas técnicos e que, historicamente, a probabilidade de uma urna apresentar defeito seja igual a 0,08. Considere, ainda, que as urnas sejam mutuamente independentes e que 0,036 e 0,039sejam os valores aproximados, respectivamente, de O,9240 e 0,9239. Com base nessas informações, julgue o item abaixo.
O número esperado de Y nesse lote é superior a 3 e menor ou igual a 4, enquanto o desvio padrão de Y se encontra dentro do intervalo [1,2],
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 23. (CESPE/2012 - SEDU-ES) Suponha que, em determinado país, 30% das crianças tenham algum tipo de dificuldade de aprendizagem.
Considerando que a população de crianças nesse país seja muito grande, tomando-se uma amostra aleatória de 10 crianças, a probabilidade de se encontrar nessa amostra exatamente três crianças com algum tipo de dificuldade de aprendizagem é superior a 0,15.
Item. 24. (CESPE/2011 - SEDUC-AM) Considere que a chegada e o atendimento de estudantes em determinada fila para matrícula em uma escola possam ser modelados segundo um passeio aleatório simples em tempo discreto t = 0,1, 2, 3 ... e que, em cada instante t, apenas dois eventos sejam possíveis:ou um novo estudante entra na fila com probabilidade p ou um estudante na fila é atendido com probabilidade 1 - p.
Suponha, ainda, que, no instante inicial t = 0, a quantidade de estudantes na fila não seja nula e grande o suficiente para que a fila não fique vazia em pouco tempo, e que, a cada instante t, no máximo um estudante pode ser atendido.
Com base nessa situação, julgue o item a seguir.

Na situação em que se consideram apenas os dois instantes iniciais, sendo t = 1 e t
= 2, ep = 0,6, é mais provável que a fila não cresça.
Item. 25. (CESPE/2011 - EBC) Considerando uma sequência de lançamentos de Bernoulli, julgue o item subsecutivo.
Se, de uma urna em que há nA bolas da cor azul e nv bolas da cor vermelha, forem retiradas,simultaneamente, n bolas (n < nA + nv < °°) e o número X de bolas da cor azul for registrado, então a distribuição de X seguirá uma distribuição binomial.
Item. 26. (CESPE/2010 - ABIN) A respeito da distribuição binomial X com parâmetros n e p, em que n
> 1 e 0

< p < 1, julgue o item subsequente.

Considere a seguinte situação hipotética. De uma urna que contém 15 bolas brancas e 1
bola vermelha serão retiradas aleatoriamente 12 bolas. Em cada retirada, será observada a cor da bola selecionada. Se branca, a bola não será devolvida à urna; se vermelha, a bola será devolvida à urna. Ao final do processo, será registrado o número X de vezes que a bola vermelha foi observada nessas doze retiradas. Em face dessa situação, é correto afirmar que X é uma variável aleatória com distribuição binomial com n = 12.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 27. (CESPE/2010 - ABIN) Considerando-se que Y siga uma distribuição binomial com parâmetros m e p e que X e Y sejam variáveis aleatórias independentes, é correto afirmar que a soma X+ Y segue uma distribuição binomial com parâmetros (n + m) e p.
Item. 28. (CESPE/2010 - ANEEL) Um fabricante de impressoras possui três fornecedores — I, II e III
— de um certo circuito eletrônico. Para a produção de um lote de 100 impressoras, a fábrica dispõe de 50, 30 e 20circuitos fornecidos, respectivamente, por I, II e III. As probabilidades de que um circuito fornecido por I,II ou III apresente defeito são, respectiva mente, iguais a 0,01, 0,03 e 0,05. Depois da produção do lote, m impressoras serão selecionadas aleatoriamente para testes de qualidade. Um indicador de qualidade da empresa é a razão f = n/m, em que n é o número observado de impressoras com defeitos no circuito.
Considerando as informações acima, julgue o item abaixo.

Dos circuitos disponíveis no estoque, o número esperado de circuitos defeituosos é menor ou igual a
2.

Item. 29. (CESPE/2010 - PREVIC) Considerando que, a fim de verificar se o pagamento de determinado benefício estava de acordo com critérios definidos, um analista tenha selecionado uma amostra aleatória de 100 pessoas, entre os 2.000 beneficiários existentes na base de dados, e considerando, ainda, que p representa a proporção populacional de benefícios corretamente pagos, julgue o próximo item.
Sabendo que a probabilidade de uma pessoa estar dentro dos critérios requeridos pelo benefício é 0,9, a probabilidade de exatamente 2 pessoas observadas na amostra estarem dentro dos critérios requeridos pelo benefício é superior a 0,10.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. ERRADO 11. CERTO
Item. 21. ERRADO

Item. 2. CERTO 12. ERRADO
Item. 22. CERTO

Item. 3. ERRADO 13. CERTO
Item. 23. CERTO

Item. 4. CERTO 14. CERTO
Item. 24. ERRADO

Item. 5. CERTO 15. ERRADO
Item. 25. ERRADO

Item. 6. ERRADO 16. ERRADO
Item. 26. ERRADO

Item. 7. ERRADO 17. ERRADO
Item. 27. CERTO

Item. 8. CERTO 18. ERRADO
Item. 28. ERRADO

Item. 9. ERRADO 19. CERTO
Item. 29. ERRADO

Item. 10. LETRA D 20. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Distribuição Geométrica

Item. 1. (Cebraspe/2015 - Engenheiro Mecânico MEC) Considerando que a demanda diária por serviços de manutenção em certa instituição seja uma variável aleatória discreta N com função de probabilidade definida como P(N = n) = 0,8 x 0,2n, em que n = 0,1, 2, 3, b, julgue o próximo item.
A moda da distribuição N é igual ou superior a 1.

Item. 2. (Cebraspe/2015 - Engenheiro Mecânico MEC) Considerando que a demanda diária por serviços de manutenção em certa instituição seja uma variável aleatória discreta N com função de probabilidade definida como P(N = n) = 0,8 x 0,2n, em que n = 0,1, 2, 3, b, julgue o próximo item.
A média da variável aleatória N é menor que 1.

Item. 3. (Cebraspe/2015 - Engenheiro Mecânico MEC) Considerando que a demanda diária por serviços de manutenção em certa instituição seja uma variável aleatória discreta N com função de probabilidade definida como P(N = n) = 0,8 x 0,2n, em que n = 0,1, 2, 3, JJ, julgue o próximo item.
A probabilidade de X ser superior a 3 é inferior a 50%.

Item. 4. (Cebraspe/2016 - TCE/PA) Considere que Y seja uma variável aleatória que representa o número de erros cometidos por um atendente no preenchimento de formulários e que a função de probabilidade de Y seja definida por P(Y = fc) = 0,9 x (0, l)k, em que k = 0,1, 2,.... Apartir dessas informações, julgue o item que se segue.
A distribuição Y é amodal

Item. 5. (Cebraspe/2016 - TCE/PA) Considere que Y seja uma variável aleatória que representa o número de erros cometidos por um atendente no preenchimento de formulários e que a função de probabilidade de Y seja definida por P(Y = fc) = 0,9 x (0, l)fc, em que k = 0,1, 2,.... Apartir dessas informações, julgue o item que se segue.
P(Y > 2) = 0,01.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (Cebraspe/2016 - TCE/PA) Considere que Y seja uma variável aleatória geométrica que representa o número de erros cometidos por um atendente no preenchimento de formulários e que a função de probabilidade de Y seja definida por P(Y = k) = 0,9 x (0,l)k, em que k = 0,1, 2,... A partir dessas informações,julgue o item que se segue.

O desvio padrão da variável Y é inferior a 1.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. ERRADO

Item. 2. CERTO

Item. 3. CERTO

Item. 4. ERRADO

Item. 5. CERTO

Item. 6. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Distribuição de Poisson

Item. 1. (CESPE/2010 - DETRAN-ES/Estatístico) Considerando que foi realizado estudo para modelar a distribuição da quantidade X de pontos acumulados por infrações de trânsito cometidas por um condutor de veículo de passeio ao longo de um ano, julgue o item a seguir, relativos a probabilidades e inferência estatística.
Nessa situação, caso X siga uma distribuição de Poisson com desvio padrão cr, o coeficiente de variação de Xserá igual a -.

Item. 2. (Cebraspe/2018 - PF/Papiloscopista) Em determinado município, o número diário
X de registros de novos armamentos segue uma distribuição de Poisson, cuja função de probabilidade é expressa por
P(X = k) = ——— em que k = 0,1,2,..., e M é um parâmetro.

dia

1 2 3 4 5

realização da variável X 6 8 0 4 2

Considerando que a tabela precedente mostra as realizações da variável aleatória X em uma amostra aleatória simples constituída por cinco dias, julgue o item que se segue.
Como a tabela não contempla uma realização do evento X = 7, é correto afirmar que P(X = 7) = 0.

Item. 3. (CESPE/2011 - SEDUC-AM/Estatístico) Para orientar os investimentos em educação em certo município, um analista foi contratado para criar um ranking das escolas públicas desse município. Para cada escola, as variáveis disponíveis são a quantidade de turmas, a quantidade de alunos, a quantidade de professores, a nota da Prova Brasil e a área do terreno. A partir dessa situação,julgue o item subsequente.
Suponha que a distribuição da quantidade de turmas por escola siga uma distribuição de
Poisson. Nessa situação, o modelo que descreve essa distribuição pode ser escrito como P(X = k) =Ae~Àk, em que k > 0
e Â > 0 representa a média de turmas por escola.

Item. 4. (CESPE/2010 - MPU/Analista) Uma empresa possui um serviço de atendimento ao consumidor

(SAC). Diariamente, um atendente registra, em uma folha de papel, as chamadas recebidas. Cada folha de registro do atendente do SAC permite o registro de até 20 chamadas. O atendente efetua os registros de forma sequencial, anotando, para cada chamada, se houve reclamação. De acordo com os dados
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

históricos, sabe-se que, a cada 20 chamadas, a probabilidade de se registrar exatamente uma reclamação é constante e igual a 0,05. Sabe-se também que o número médio diário de reclamações registradas peloSAC é igual a 1.

Com base nessas informações e considerando 2,71 como valor aproximado para o número e,
base do logaritmo natural, julgue o item.
Suponha que o número diário de reclamações registradas pelo SAC siga uma distribuição de Poisson. Nessa situação, a probabilidade de haver o registro de, no máximo, uma reclamação em determinado dia é superior a 67%.
Item. 5. (CESPE/2010 - MPU/Analista) Uma empresa possui um serviço de atendimento ao consumidor

(SAC). Diariamente, um atendente registra, em uma folha de papel, as chamadas recebidas. Cada folha de registro do atendente do SAC permite o registro de até 20 chamadas. O atendente efetua os registros de forma sequencial, anotando, para cada chamada, se houve reclamação. De acordo com os dados históricos, sabe-se que, a cada 20 chamadas, a probabilidade de se registrar exatamente uma reclamação é constante e igual a 0,05. Sabe-se também que o número médio diário de reclamações registradas peloSAC é igual a 1.

Com base nessas informações e considerando 2,71 como valor aproximado para o número e,
base do logaritmo natural, julgue o item.
Suponha que o número de reclamações registradas pelo SAC, X(t), em um intervalo de tempo t, siga um processo de Poisson e que X(l) represente o número diário de reclamações registradas.Nessa situação, é correto afirmar que a variância de X(t) cresce linearmente com t.
Item. 6. (CESPE/2010 - TRE-ES/Analista Judiciário) Uma empresa iniciou suas atividades com R$ 30
mil de capital. O custo fixo mensal da empresa é de R$ 5 mil. As vendas de seus produtos ocorrem segundo um processo de Poisson, com taxa igual a R$ 1 mil por mês. A empresa fechará no momento que o seu capital for igual ou inferior a zero. Com base nessa situação, e considerando exp(- 6) =0,0025, julgue o item seguinte.
A probabilidade de a empresa sobreviver além do sexto mês de funcionamento é inferior a 0,95.

Item. 7. (Cebraspe/2013 - ANTT-DF/Área Estatística)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A figura acima apresenta um trecho de uma rodovia com três faixas de rolamento.
Considere que X(t)
represente o número de veículos que passam nesse trecho durante um intervalo de tempo de duração t(em minutos) e que X(t) siga um processo de Poisson com parâmetro 6t, ou seja,
P(X(t) = x) = ———.

Suponha, ainda, que, no intervalo t, cada veículo selecione aleatoriamente as faixas de rolamento
1, 2 e 3
com probabilidades 0,5; 0,3 e 0,2, respectivamente. Com base nessas informações, julgue o próximo item.
O número de veículos que passam nesse trecho pela faixa de rolamento 3 durante um intervalo de tempo de duração t (em minutos) segue um processo de Poisson com parâmetro l,2t.
Item. 8. (CESPE/2012 - CNJ/Analista Judiciário) A quantidade de chamadas que uma central telefônica recebe por hora é modelado por uma distribuição de Poisson, com parâmetro À = 12 chamadas por hora.Nesse caso, a probabilidade de a central telefônica receber:

menos de três chamadas em uma hora é igual a 85e-12.

Item. 9. (CESPE/2012 - CNJ/Analista Judiciário) A quantidade de chamadas que uma central telefônica recebe por hora é modelado por uma distribuição de Poisson, com parâmetro À = 12 chamadas por hora.Nesse caso, a probabilidade de a central telefônica receber:

exatamente duas chamadas em 20 minutos é igual a —e . 6!

Item. 10. (Cebraspe/2013 - MC/Análises Técnicas) A quantidade diária de reclamações — X
— recebidas em uma central de atendimento ao consumidor segue uma distribuição de Poisson, em que P(X= 0) = 0,5.
Nesse sentido, julgue o próximo item.

O valor esperado de X é igual a In2.

Item. 11. (CESPE/2012 - ANP/Especialista) A respeito da teoria básica de probabilidades, julgue o item subsequente.
Se uma variável aleatória de Poisson é tal que 2- P(X = 4) = P(X = 3), a média de X é 0,5.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 12. (CESPE/2020 -TJ-PA/Analista Judiciário) Uma amostra aleatória simples de tamanho 5 foi retirada de uma distribuição de Poisson com média igual a 5. Essa amostra é representada por Xi, X₂, X₃, X₄,X₅, em que cada variável Xk denota o total de erros processuais registrados em certo cartório judicial no dia k,com k = {1, 2, 3, 4, 5}. A respeito da quantidade semanal de erros processuais registrados nesse cartório Y
= Xi + X2 + X3 + X4 +X5, assinale a opção correta.

a) O coeficiente de variação de Y é igual a 1.

b) E(Y) < 20

c) O desvio padrão de Y é igual a 5.

d) Para k = 1, 2, 3, 4, 5, tem-se que P(Y = 0) >= P(Xk = 0)

e) A média semanal de erros processuais, denotada por Y/5, segue uma distribuição normal.

Item. 13. (Cebraspe/2013 - Analista Judiciário STF) As quantidades diárias de processos administrativos (/V)protocolados em certo órgão público seguem uma distribuição de Poisson com média igual a 5. Cada processo protocolado é encaminhado para a superintendência A ou para a B e, assim, a soma Y = Yi=iXb em que Xi = 1 se o processo segue para a superintendência A, e Xi = 0 se o processo segue para B,representa o total diário de processos administrativos protocolados que se destinam para a superintendência A.
Com base nessa situação, julgue o seguinte item considerando que Xi, X₂,..., XN sejam variáveis aleatórias independentes, e que P(Xi = 1) = P(X₂ = 1) = ... = P(XN = 1) = 0,8.
A quantidade média diária de processos administrativos que se destinam para a superintendência A é igual a 4.
Item. 14. (Cebraspe/2013 - Analista Judiciário STF) As quantidades diárias de processos administrativos (N)protocolados em certo órgão público seguem uma distribuição de Poisson com média igual a 5. Cada processo protocolado é encaminhado para a superintendência A ou para a B e, assim, a soma Y = Yi=iXb em que Xi = 1 se o processo segue para a superintendência A, e Xi = 0 se o processo segue para B,representa o total diário de processos administrativos protocolados que se destinam para a superintendência A.
Com base nessa situação, julgue o seguinte item considerando que Xi, X₂,..., XN sejam variáveis aleatórias independentes, e que P(Xi = 1) = P(X₂ = 1) = ... = P(XN = 1) = 0,8.
O número diário de processos protocolados que são destinados à superintendência B segue uma distribuição de Poisson com média igual a 1.
Item. 15. (Cebraspe/2018 - Analista Administrativo EBSERH) O total diário - X - de pessoas recebidas em uma unidade de pronto atendimento (UPA) para atendimento ambulatorial, e o total diário -Y - de pessoas recebidas nessa mesma UPA para atendimento de urgência segue processos de Poisson homogêneos, com
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

médias, respectivamente, iguais a 20 pacientes/dia e 10 pacientes/dia, e as variáveis aleatórias X e Y são independentes. Sabe-se que, em média, a necessidade de cuidados hospitalares atinge 10% dos pacientes do atendimento ambulatorial e 90% dos pacientes do atendimento de urgência.
A partir dessa situação hipotética, julgue o próximo item, considerando que o registro da necessidade de cuidados hospitalares seja feito no momento em que o paciente chegue à UPA e que H seja a quantidade diária registrada de pacientes com necessidades de cuidados hospitalares.
Considerando a equivalência 1 dia=24 horas, então o tempo médio de chegada entre dois pacientes consecutivos para o atendimento de urgência nessa UPA é inferior a 3 horas.
Item. 16. (Cebraspe/2013 - Estatístico FUB) Tendo em vista que o número diário X de recursos administrativos protocolados em certa repartição pública segue uma distribuição dePoisson com taxa igual a InlO processos por dia, julgue o item que se segue.
O desvio padrão da distribuição de X é inferior a InlO processos por dia.

Item. 17. (Cebraspe/2013 - Estatístico FUB) Tendo em vista que o número diário X de recursos administrativos protocolados em certa repartição pública segue uma distribuição dePoisson com taxa igual a InlO processos por dia, julgue o item que se segue.
A distribuição do número diário de recursos administrativos apresenta coeficiente de variação igual a 1.
Item. 18. (Cebraspe/2013 - Estatístico FUB) Tendo em vista que o número diário X de recursos administrativos protocolados em certa repartição pública segue uma distribuição dePoisson com taxa igual a InlO processos por dia, julgue o item que se segue.
Em determinado dia, a probabilidade de não haver recurso protocolado é igual ou inferior a 0,1.

Item. 19. (Cebraspe/2013 - Estatístico FUB) Tendo em vista que o número diário X de recursos administrativos protocolados em certa repartição pública segue uma distribuição dePoisson com taxa igual a InlO processos por dia, julgue o item que se segue.
A distribuição de Poisson não possui memória, pois P(X = k | X > 1) = P(X = k - 1), em que k > 1.

Item. 20. (Cebraspe/2016 - Analista de Controle TCE/PR) Suponha que o número mensal X
de pessoas que sofrem algum tipo de acidente em um centro comercial siga uma distribuição de Poisson.Considerando que P(X = 0) = 0,1 e InlO = 2,3, assinale a opção correta.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) A distribuição X possui desvio padrão igual ou superior a 2.

b) P(X>1) = 0,9

c) 0,20 < P(X = 1) < 0,25

d) P(X<0) >0

e) A esperança de X é igual ou superior a 3.

Item. 21. (Cebraspe/2015 - Estatístico FUB) Uma repartição pública recebe diariamente uma quantidade X de requerimentos administrativos e uma quantidade Yde recursos administrativos.Essas quantidades seguem distribuições de Poisson com taxas,
respectivamente, iguais a /nl5 requerimentos por dia e In4 recursos por dia.
Considerando que, nessa situação hipotética, as variáveis aleatórias X e Y
sejam independentes e que S = X+Y, julgue o seguinte item.
Em determinado dia, a probabilidade de não haver recebimento de requerimento administrativo nessa repartição será inferior a 0,08.
Item. 22. (Cebraspe/2015 - Estatístico FUB) Uma repartição pública recebe diariamente uma quantidade X de requerimentos administrativos e uma quantidade Yde recursos administrativos.Essas quantidades seguem distribuições de Poisson com taxas,
respectivamente, iguais a /nl5 requerimentos por dia e In4 recursos por dia.
Considerando que, nessa situação hipotética, as variáveis aleatórias X e Y
sejam independentes e que S = X+Y, julgue o seguinte item.
A variância da distribuição de Y é igual a In4.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. CERTO 9. ERRADO
Item. 17. ERRADO

Item. 2. ERRADO 10. CERTO
Item. 18. CERTO

Item. 3. ERRADO 11. ERRADO
Item. 19. ERRADO

Item. 4. CERTO 12. LETRA C
Item. 20. LETRA C

Item. 5. CERTO 13. CERTO
Item. 21. CERTO

Item. 6. ERRADO 14. CERTO
Item. 22. CERTO

Item. 7. CERTO 15. CERTO

Item. 8. CERTO 16. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

