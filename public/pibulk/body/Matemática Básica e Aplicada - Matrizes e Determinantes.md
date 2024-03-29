# Matemática Básica e Aplicada - Matrizes e Determinantes

SERPRO - Raciocínio Lógico - 2023

(Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Matrizes

2) Determinantes

3) Questões Comentadas - Matrizes - Cebraspe

4) Questões Comentadas - Determinantes - Cebraspe

5) Lista de Questões - Matrizes - Cebraspe

6) Lista de Questões - Determinantes - Cebraspe

MATRIZES

Matrizes

Introdução às matrizes

Podemos representar uma matriz tanto com colchetes "[ ]" quanto com parênteses "()".
Matriz de dimensão m x n: m linhas e n colunas.

Elemento a^i o primeiro índice representa a linha e o segundo índice representa a coluna.

Representação de uma matriz pela lei de formação

Cada elemento da matriz deve ser calculado por meio de uma fórmula apresentada.

Tipos de matrizes

Matriz linha: apresenta apenas uma linha. Dimensão da forma 1 x n.

Matriz coluna: apresenta apenas uma coluna. Dimensão da forma m x 1.

Matriz quadrada: apresenta o mesmo número de linhas e de colunas. Dimensão da forma n X n.

y/?' 3

Diagonal Secundária

/'+/ = n+1

''7.

Diagonal Principal
'=/

Matriz Retangular: número de linhas é diferente do número de colunas.

Matriz Diagonal: matriz quadrada em que todos os elementos que não pertencem à diagonal principal são iguais a zero.
Matriz Triangular: matriz quadrada em que todos os elementos acima ou abaixo de sua diagonal principal são nulos.
* Matriz Triangular Superior: todos os elementos abaixo da diagonal principal são nulos.

* Matriz Triangular Inferior: todos os elementos acima da diagonal principal são nulos.

Matriz Identidade: elementos da diagonal principal são iguais a 1 e os elementos fora da diagonal principal são zero.
Matriz Nula: todos os elementos são iguais a zero. É comum representar uma matriz nula quadrada pela letra 0 acrescida de um índice que indica a ordem da matriz. Ex: 0₃ -» matriz nula quadrada de ordem 3.
Operações com matrizes

Igualdade entre matrizes: duas matrizes são iguais quando apresentam a mesma dimensão mxn e seus elementos são idênticos e estão nas mesmas posições.
Adição e subtração de matrizes: é necessário que as matrizes tenham a mesma dimensão mxn. Para realizar a operação, basta somar/subtrair os termos que estão na mesma posição.
Multiplicação da matriz por um número real: multiplicar todos os elementos da matriz pelo número real.
Multiplicação de matrizes

Item. 1. Verificar se o número de colunas da primeira matriz é igual ao número de linhas da segunda. Se essa igualdade não se verificar, não é possível realizar o produto das matrizes.
Item. 2. Obter o esquema geral da matriz-produto, que apresenta a seguinte dimensão:

Número de linhas da primeira x Número de colunas da segunda

Colunas da 1a = Linhas da 2a

A2X3 B3X4

Produto: Linhas da 1a e Colunas da 2a

C2X4

Item. 3. Obter os elementos da matriz resultante a partir das linhas da primeira matriz e das colunas da segunda matriz.
O elemento cíy- da matriz-produto C é obtido por meio da linha í da primeira matriz e da coluna j da segunda matriz.
Propriedades da multiplicação de matrizes

A propriedade comutativa não vale para matrizes: AB #= BA.

Propriedade associativa entre matrizes: (AB)C = A(BC)

Propriedade associativa entre matrizes e um número real: cc(AB) = (aA)B = A(aB)

Propriedade distributiva: A(B + C) = AB + AC; (B + C)A = BA + CA

Elemento neutro da multiplicação de matrizes: AI = IA = A

Traço de uma matriz quadrada

O traço de uma matriz quadrada é a soma dos elementos da sua diagonal principal. Se A é uma matriz quadrada, então o seu traço é representado por tr(A).
* tr Q4 + B) = tr(A) + tr(B)

* tr (A — B) = tr(A) — tr(B)

* tr(aA) = a tr(A)

* tr (AB) = tr(BA)

Matriz oposta

A matriz oposta de A é —A.

Matriz transposta, simétrica e antissimétrica

A transposta de uma matriz A (notação: AÈ) corresponde à matriz cujas linhas foram transformadas em colunas.
(yf)* = A
(a A)1 = a A1

(AB)1 = BtAt

(A + By = At + Bt

Matriz Simétrica: a matriz é igual a sua transposta -» A = At

* É quadrada; e

* Os elementos simétricos com relação à diagonal principal são iguais.
Matriz antissimétrica: AL = —A

* É quadrada;

* A diagonal principal é nula; e

* Os elementos simétricos com relação à diagonal principal são opostos.

Matriz inversa

A inversa de uma matriz A (notação: T4_1) é aquela matriz que, quando multiplicada pela matriz A,
tem como resultado a matriz identidade:
AA-1 = A~tA = In

Uma matriz que não possui inversa é denominada singular.

Propriedades:

(X-1)-1 = A

(X-1)t = (A*)-1

(aA)~r = -A-1

a

(AB)"1 = B~rA~r

ÇABCy1 = C~1B~1A~1

Matriz inversa como análogo da divisão: pode-se multiplicar ambos os lados de uma equação matricial pela inversa de uma matriz (X-1) e, na sequência, usar a propriedade X 1T4 = I.
Matriz ortogonal

Uma matriz A é dita ortogonal quando a sua inversa é igual a sua transposta:

A é ortogonal < > = At

Introdução às matrizes

Noção básica

A ideia básica de uma matriz é representar uma tabela de um modo mais formal, com uma "linguagem matemática".
Suponha, por exemplo, que um concurseiro quer organizar em uma matriz quantas horas ele pretende estudar em cada dia da semana das próximas quatro semanas. Considere também que:
* As linhas representam os dias da semana: a primeira linha corresponde à segunda-feira, a segunda linha corresponde à terça-feira, e assim sucessivamente até a sétima linha, que corresponde ao domingo.
* As colunas representam as semanas: a primeira coluna corresponde à primeira semana, a segunda coluna corresponde à segunda semana, a terceira coluna corresponde à terceira semana e, por fim,a quarta coluna corresponde à quarta semana.

Nesse caso, o concurseiro pode representar a sua matriz do seguinte modo:

1° linha (segunda)
2a linha (terça)
3a linha (quarta)

4a linha (quinta)

5a linha (sexta)
6a linha (sábado)
7a linha (domingo)

I

3 4

4 3

5 4

5 4

6 5

9 II

9 8

I I

5 6'

4 3

4 3

3 3

3 4

9 8

9 9-

Note que o elemento que está na 6a linha e na 2? coluna representa o número de horas que concurseiro planeja estudar no sábado da segunda semana: 11 horas.
2a coluna (2a semana)

1 I

'3 2 5 6'

4 r I 4 3

5 2 4 3

5 2 3 3

6 ! 3 4

6a linha (sábado)

9—(lí) 9 8

L9 8 9 9-

Podemos representar uma matriz tanto com colchetes "[ ]" quanto com parênteses "()". Portanto, a matriz em questão também pode ser representada da seguinte maneira:
/3 4 5 6\

4 3 4 3

5 4 4 3

5 4 3 3

6 5 3 4

9 11 9 8

\g 8 g g/

Dimensão de uma matriz

Podemos dizer que uma matriz de dimensão m X n (lê-se: matriz de dimensão m por n) é uma matriz formada por elementos (ou entradas) distribuídos em m linhas e n colunas.
No exemplo que acabamos de mostrar, temos uma matriz composta por 7 linhas e por 4 colunas.
Portanto,
trata-se de uma matriz 7X4 (matriz 7 por 4). Vejamos mais quatro exemplos:

11 V3 7/9

6 5 2

8 1 3 -

' 5 11/12 i

-V7 4 4

é uma matriz 3x3;

531 . e uma matriz 2x4;

2 3 '

5 7

11 13

17 19-

é uma matriz 4x2;

r5]

-1-

é uma matriz 3x1.

FIQUE

ATENTO!

A ordem correta é l\P de LINHAS x de COLUNAS

Representação genérica dos elementos de uma matriz

Cada elemento de uma matriz apresenta uma determinada localização dentro dela. Essa localização é dada pela linha e pela coluna do elemento.
Considere a seguinte matriz A:

-3 4 5 6-

4 3 4 3

5 4 4 3

A = 5 4 3 3

6 5 3 4

9 11 9 8

Lç 8 9 9-1

Genericamente, um elemento dessa matriz A pode ser representado por aí7-, em que i representa a linha em que esse elemento se encontra e j representa a sua coluna.
FIQUE

ATENTO!

O primeiro índice representa a linha e o segundo índice representa a coluna.

Linha

Coluna

Por exemplo, o elemento a42 é aquele que está na linha 4 e na coluna 2. Portanto, a42 = 4.

2a coluna

6'

9-

O elemento a24, por sua vez, é aquele que está na linha 2 e na coluna 4. Portanto, a24 = 3.

4a coluna

I

4 5$'

---- 4-©

4 4 3

4 3 3

5 3 4

11 9 8

8 9 9-

Representação genérica de uma matriz

Uma matriz A de dimensão mxn, isto é, uma matriz A com m linhas e n colunas, pode ser representada genericamente das seguintes formas:
Anmxn

A = (d^

mxn an aí₂ ^ln
A = a21 a22 a2n

Aml dm2 CLmn

Representação de uma matriz pela lei de formação

Podemos representar uma matriz por meio de uma lei de formação. Nesse caso, cada elemento da matriz deve ser calculado por meio de uma fórmula apresentada.
Considere por exemplo, a seguinte matriz:

A = tal que aÜ = i+J2

Note que a matriz A é 3x3, isto é, possui 3 linhas e 3 colunas.

'all a12 a13~

a21 a22 a23

.a31 a32 a33.

Para obter a matriz, devemos calcular cada um de seus elementos por meio da lei de formação apresentada, dada por = i + j2.
Portanto, a matriz A é dada por:

Vamos a um exercício.

an = 1 + l2 = 2

a12 = 1 + 22 = 5

a13 '= 1 + 32 : = 10

a21 = 2 + l2 = 3

₀₋₂₂ = 2 + 22 = 6

a23 = 2 + 32 = 11
a31 : = 3 + l2 : = 4
a32 : = 3 + 22 : = 7

a33 = 3 + 32 = = 12

'2 5 10

A = 3 6 11

Item. .4 7 12.

(DNIT/2013) Os elementos de uma matriz X₃x2 , isto é, com três linhas e duas colunas, são dados por:
f(i + ;)2,se i = j li2 + j2, sei j
Em que representa o elemento da matriz >l₃x2 localizado na linha i e coluna j.
Então, a soma dos elementos da primeira coluna de >l3x2 é igual a:
a) 17

b) 15

c) 12

d) 19

e) 13

Comentários:

Como a matriz A apresenta 3 linhas e 2 colunas, podemos representá-la genericamente do seguinte modo:
a12~

A = a21 a22

.a31 a32.

A questão pede a soma dos elementos da primeira coluna de A:

+ d2i + (Z3i

Para allr temos i = j. Logo, a±1 = (1 + l)2 = 4.
Para a21, temos i + j. Logo, n21 = l2 + 22 = 5.
Para a31, temos i + j. Logo, a31 = 32 + l2 = 10.

A questão pede a soma dos elementos da primeira coluna de A é:

4 + 5 + 10 = 19

Gabarito: Letra D.

Tipos de matrizes

Matriz linha

É uma matriz com apenas uma linha, ou seja, tem dimensão da forma 1 xn. Exemplos:

* [5 4 1] é uma matriz linha de dimensão 1x3.

* [3 | V4 y 7 2 1 42 y] é uma matriz linha de dimensão 1x9.

Matriz coluna

É uma matriz com apenas uma coluna, ou seja, tem dimensão da forma m x 1. Exemplos:

-4

Vó é uma matriz coluna de dimensão 3 x 1.
53.

é uma matriz coluna de dimensão 5x1.

Matriz quadrada

É uma matriz que apresenta o mesmo número de linhas e de colunas, ou seja, tem dimensão da forma n x n. Exemplos:
.70%

é uma matriz quadrada de dimensão 2x2.

f 7 53

4 -8

Lll 4%

3 '

22 é uma matriz quadrada de dimensão 3x3.
1.

Quando uma matriz quadrada apresenta dimensão n x n, dizemos que essa matriz quadrada apresenta ordem n. Nos dois exemplos anteriores, temos uma matriz quadrada de ordem 2 e uma matriz quadrada de ordem 3, respectivamente.
Diagonais da matriz quadrada

Uma matriz quadrada apresenta duas diagonais: a diagonal principal e a diagonal secundária.

A diagonal principal é composta pelos elementos em que o número da linha é igual ao número da coluna,isto é, i = j.

8 9

11 2%

V7 3 '''7^

Para o exemplo em questão, os elementos da diagonal principal são air = 5, a22 = 15 e a33 = 7.

Já a diagonal secundária é composta por elementos cuja soma da linha e da coluna (i + j) é igual à ordem da matriz (n) acrescida de uma unidade, isto é:
i + j = n+1

' 5 8

11 ^5''2%

MT- 3 7

Para 0 exemplo em questão, os elementos da diagonal secundária são a13 = 9, a22 = 15 e a31 = V7.

Matriz retangular

Uma matriz é retangular quando o número de linhas é diferente do número de colunas. Exemplos:
' 3 11

33 -11

Item. .13 6 -

í° 11

1-9 50%

é uma matriz retangular de dimensão 3x2.

4] ' uma matriz retangular de dimensão 2x3.
lle

Matriz diagonal

A matriz diagonal é uma matriz quadrada em que todos os elementos que não pertencem à diagonal principal são iguais a zero. Exemplos:
4 0 0

0-2 0

Item. .0 0 7

Matriz triangular

Uma matriz triangular é uma matriz quadrada em que todos os elementos acima ou abaixo de sua diagonal principal são nulos.
Matriz triangular superior

Quando todos os elementos abaixo da diagonal principal forem nulos, temos uma matriz triangular superior. Exemplo:
8 5 7 1

0 9 14

0 0 5 2

0 0 0 1

Matriz triangular inferior

Quando todos os elementos acima da diagonal principal forem nulos, temos uma matriz triangular inferior.
Exemplo:

8 0 0 0

2 9 0 0

3 9 5 0

15 13

Matriz identidade ou matriz unidade

A matriz identidade (ou matriz unidade) é uma matriz quadrada cujos elementos da diagonal principal são iguais a 1 e os elementos fora da diagonal principal são zero. Exemplo:
10 0 0

0 10 0

0 0 10

Lo o o iJ

A representação desse tipo de matriz é dada pela letra I acrescida de um índice que indica a ordem da matriz.Isso significa que 7₃ é uma matriz identidade de ordem 3:

1 0 0

h — 0 1 0

0 0 1

Matriz nula

Matriz nula é a matriz que apresenta todos seus elementos iguais a zero. Exemplos:

0 é uma matriz nula de dimensão 2x3.

0 0

0 0

Item. .0 0

0 é uma matriz nula quadrada de ordem 3.
0.

É comum representar uma matriz nula quadrada pela letra O acrescida de um índice que indica a ordem da matriz. Isso significa que O₃ é uma matriz nula quadrada de ordem 3.
Operações com matrizes

Igualdade entre matrizes

Duas matrizes são iguais quando:

* Apresentam a mesma dimensão m x n;

* Seus elementos são idênticos e estão nas mesmas posições.

Por exemplo, as duas matrizes abaixo são iguais, pois apresentam a dimensão 3x3, bem como seus elementos são idênticos e estão nas mesmas posições:
3/4 11 -3

7 42 -4

_v/2 5 -1

3/4 11 -3

= 7 42 -4

_V2 5 -1

Observe agora a suposta igualdade:

3/4

ii -3

42 -4

??

r*-!

3/4

11 -3

X -4

. y 5 -1 tV2 5 -1.

Note que a igualdade só se verifica se x = 42 e y = v/2. Caso contrário, as duas matrizes não serão iguais.
(Pref. N Horizonte/2019) O valor de x + y que determina a igualdade entre as matrizes
[7 x-y -101 ' 7 -13 2x'

Ll5 8 24 J —3x 8 3y.

a) 5.

b) 3.

! c)-5.

d) -8.

í e) -13.

; Comentários:

: Note que as duas matrizes apresentam a mesma dimensão 2x3. Para que elas sejam iguais, seus elementos devem ser idênticos e devem estar nas mesmas posições. Para tanto, devemos ter:
x — y = —13

2x = -10

-3x = 15

3y = 24

A partir da segunda e da quarta equação, podemos obter os valores de x e de y.

2x = -10 -> x = -5

3y = 24 -> y = 8

O valor de x + y é:

O gabarito, portanto, é letra B.

(-5) + 8 = 3

Observe que as outras equações se verificam para x = — 5 e y = 8, pois, caso contrário, as matrizes não seriam iguais.
x-y= (-5)-8 = -13

—3x = -3 x (-5) = 15

Gabarito: Letra B.

Adição e subtração de matrizes

Para somar ou subtrair matrizes, é necessário que elas tenham a mesma dimensão. Note, portanto, que não é possível somarmos uma matriz de dimensão 3x5 com uma matriz de dimensão 4x3.
Feita essa observação, deve-se entender que a soma entre duas matrizes é feita somando os termos que estão na mesma posição.
Para a subtração, seguimos a mesma ideia, subtraindo os elementos de uma matriz dos elementos de mesma posição da outra matriz.
Suponha, por exemplo, que temos duas matrizes A e B dadas por:

A soma A + B é dada por:

= [5 + (-3)

L -4 + 2

-2 + 3

1 + 1

2 1 1

—2 2 12

3 + (-2)1

5 + 7 J

Já a subtração A — B é dada por:

r5-(-3) -2-3 3-(-2)1

1-4-2 1-1 5-7-1

= í 8 "5 5 1

1-6 0 -2J

Multiplicação da matriz por um número real

Para multiplicarmos uma matriz por um número real qualquer, basta multiplicar todos os elementos dessa matriz pelo número real. Considere, por exemplo, a seguinte matriz A:
Ao multiplicar a matriz A por 2, obtemos a seguinte matriz:

2A = 2 x

-3 2 5

1 3 -1

. 7 -3 VzJ

2A =

2 x (-3) 2x2 2x5

2x1 2x3 2 x (-1)

2x7 2 x (-3) 2 x V2

Multiplicação de matrizes

2A =

-6 4 10

2 6 -2

Item. .14 -6 2V2.

Pessoal, atenção redobrada com a multiplicação de matrizes. Essa é a parte que costuma gerar mais confusão entre os alunos.
Para multiplicar duas matrizes, devemos seguir os seguintes passos:

Item. 1. Verificar se 0 número de colunas da primeira matriz é igual ao número de linhas da segunda. Se essa igualdade não se verificar, não é possível realizar o produto das matrizes.
Item. 2. Obter 0 esquema geral da matriz-produto, que apresenta a seguinte dimensão:

Número de linhas da primeira x Número de colunas da segunda

Item. 3. Obter os elementos da matriz resultante a partir das linhas da primeira matriz e das colunas da segunda matriz.
Professor, não entendi nadai!

Calma, caro aluno! Vamos resolver um exemplo.
Considere as matrizes A e B, dadas por:

100 200 450 200'

B = 400 150 150 450

Item. .250 300 100 700.

Vamos calcular o produto A x B.

Item. 1. Verificar se o número de colunas da primeira matriz é igual ao número de linhas da segunda. Se essa igualdade não se verificar, não é possível realizar o produto das matrizes;
Note que a matriz A tem dimensão 2 x 3, e a matriz B tem dimensão 3x4. Observe,
portanto, que o número de colunas da matriz A é igual ao número de linhas da matriz B. Logo, é possível realizar o produto das matrizes 42x3 e B3x4.
Item. 2. Obter o esquema geral da matriz-produto, que apresenta a seguinte dimensão:

Número de linhas da primeira x Número de colunas da segunda

A matriz A tem dimensão 2 x 3, e a matriz B tem dimensão 3x4. Logo, a matriz-produto apresenta a dimensão 2x4. Temos o seguinte esquema geral:
C = AxB = [( ) ( )

L( ) ( )

( ) ( )i

( ) ( )J

Ou então, de maneira mais formal, poderíamos escrever:

cí4

C24

Lembre-se: o elemento q7- está na linha i e na coluna j da matriz C.
Uma maneira prática de memorizar os passos 1 e 2 é a seguinte:

Item. 3. Obter os elementos da matriz resultante a partir das linhas da primeira matriz e das colunas da segunda matriz.
Temos a seguinte matriz-produto:

C=AxB= cn

.C21

C12 C13 C14

C22 C23 C24

Obtenção de

—> Primeira linha da primeira matiz, primeira coluna da segunda matriz

Para determinar o elemento da primeira linha e da primeira coluna da matriz-produto (cn), devemos utilizar a primeira linha da primeira matriz e a primeira coluna da segunda matriz.
100 200 450 200'

B = 400 150 150 450

Item. .250 300 100 700.

Para obter o elemento c11; realiza-se a seguinte operação:

Cn = 3 x 100 + 2 x 400 + 1 x 250 = 1350

Vamos colocar esse novo elemento na nossa matriz-produto:

C = A x B = 1350

- ( )

( ) ( ) ( )1

( ) ( ) ( )J

Obtenção de C^

C₁₂ Primeira linha da primeira matiz, segunda coluna da segunda matriz

Para determinar o elemento da primeira linha e da segunda coluna da matriz-produto (c₁₂), devemos utilizar a primeira linha da primeira matriz e a segunda coluna da segunda matriz.
100 200 450 200'

B = 400 150 150 450

Item. .250 300 100 700.

Para obter o elemento c₁₂, realiza-se a seguinte operação:

c12 = 3 x 200 + 2 x 150 + 1 x 300 = 1200

Vamos colocar esse novo elemento na nossa matriz-produto:

C=AxB= 1350

.( )

1200

( )

( ) ( )1

( ) ( )J

Obtenção de 643

Cj3 Primeira linha da primeira matiz, terceira coluna da segunda matriz

Para determinar o elemento da primeira linha e da terceira coluna da matriz-produto (c₁₃), devemos utilizar a primeira linha da primeira matriz e a terceira coluna da segunda matriz.
100 200 450 200'

B = 400 150 150 450

Item. .250 300 100 700.

Para obter o elemento c₁₃, realiza-se a seguinte operação:

c13 = 3 x 450 + 2 x 150 + 1 x 100 = 1750

Vamos colocar esse novo elemento na nossa matriz-produto:

C =AxB 1350

.( )

1200
( )

1750 ( )'

( ) ( ).

Obtenção de

C₄₄ —> Primeira linha da primeira matiz, quarta coluna da segunda matriz

Para determinar o elemento da primeira linha e da quarta coluna da matriz-produto (c₁₄), devemos utilizar a primeira linha da primeira matriz e a quarta coluna da segunda matriz.
100 200 450 200

B = 400 150 150 450

Item. .250 300 100 700.

Para obter o elemento c₁₄, realiza-se a seguinte operação:

c14 = 3 x 200 + 2 x 450 + 1 x 700 = 2200

Vamos colocar esse novo elemento na nossa matriz-produto:

C =AxB = 1350

.( )

1200 1750 2200

( ) ( ) ( )

Obtenção de C₂j

C₂₁ Segunda linha da primeira matiz, primeira coluna da segunda matriz

Para determinar 0 elemento da segunda linha e da primeira coluna da matriz-produto (c₂₁), devemos utilizar a segunda linha da primeira matriz e a primeira coluna da segunda matriz.
100 200 450 200'

B = 400 150 150 450

Item. .250 300 100 700.

Para obter 0 elemento c₂₁, realiza-se a seguinte operação:

c21 = 1 x 100 + 3 x 400 + 3 x 250 = 2050

Vamos colocar esse novo elemento na nossa matriz-produto:

C=AxB= 1350

2050

1200
( )

1750 2200
( ) ( )

Obtenção de C₂₂

C₂₂ -> Segunda linha da primeira matiz, segunda coluna da segunda matriz

Para determinar 0 elemento da segunda linha e da segunda coluna da matriz-produto (c₂₂), devemos utilizar a segunda linha da primeira matriz e a segunda coluna da segunda matriz.
100 200 450 200'

B = 400 150 150 450

Item. .250 300 100 700.

Para obter 0 elemento c₂₂, realiza-se a segeinte operaçã0:

c22 = 1 x 200 + 3 x 150 + 3 x 300 = 1550

Vamos colocar esse novo elemento na nossa matriz-produto:

1350 1200 1750 2200

2050 1550 ( ) ( ) .

Obtenção de C23

C23 —> Segunda linha da primeira matiz, terceira coluna da segunda matriz

Para determinar 0 elemento da segunda linha e da terceira coluna da matriz-produto (c₂₃), devemos utilizar a segunda linha da primeira matriz e a terceira coluna da segunda matriz.
100 200 450 200'

B = 400 150 150 450

Item. .250 300 100 700.

Para obter 0 elemento c₂₃, realiza-se a seguinte operação:

c23 = 1 x 450 + 3 x 150 + 3 x 100 = 1200

Vamos colocar esse novo elemento na nossa matriz-produto:

C = AxB = ri350
2050

1200

1550

1750 2200

1200 ( )

Obtenção de C24

C24 -> Segunda linha da primeira matiz, quarta coluna da segunda matriz

Para determinar 0 elemento da segunda linha e da quarta coluna da matriz-produto (c₂₄), devemos utilizar a segunda linha da primeira matriz e a quarta coluna da segunda matriz.
100 200 450 200

B = 400 150 150 450

Item. .250 300 100 700.

Para obter 0 elemento c₂₄, realiza-se a seguinte operação:

c24 = 1 x 200 + 3 x 450 + 3 x 700 = 3650

Vamos colocar esse novo elemento na nossa matriz-produto:

C =AxB rl350
1.2050

1200

1550

1750 22001

1200 3650-1

Pronto! Acabamos de realizar 0 produto das matrizes A e B.

3 2

Ll 3 3-I

.250

AxB = C

200'

700.

rl350
Í2050

1200 1750 22001

1550 1200 365oJ

Professor... você levou QUATRO PÁGINAS poro calcular os oito elementos!!

Calma, caro aluno. Levamos quatro páginas porque fizemos passo a passo. Em resumo, o que você precisa saber é o seguinte:
ATENÇÃO

DECORE!

O elemento da linha i e da coluna j da matriz-produto C é obtido por meio da linha i da primeira matriz e da coluna j da segunda matriz.
6'! ] -> Linha1 da primeira matriz e coluna 1 dasegundamatriz;
c₁₂ -> Linha 1 da primeira matriz e coluna 2 dasegundamatriz;
c₁₃ -> Linha 1 da primeira matriz e coluna 3 dasegundamatriz;
c₁₄ -> Linha 1 da primeira matriz e coluna 4 dasegundamatriz;
c₂₁ -> Linha 2 da primeira matriz e coluna 1 dasegundamatriz;
c₂₂ -> Linha 2 da primeira matriz e coluna 2 dasegundamatriz;
c₂₃ -> Linha 2 da primeira matriz e coluna 3 dasegundamatriz;
c₂₄ -> Linha 2 da primeira matriz e coluna 4 dasegundamatriz.

Na hora da prova, ao se deparar com o seguinte produto:

I-Q 7 1 1

Q x

*J

100 200 450 200

400 150 150 450

Item. .250 300 100 700.

Você deve realizar as contas assim:

r( 3.100+ 2.400 + 1.250)

[(1.100 + 3.400 + 3.250)

(3.200 + 2.150 + 1.300)

(1.200 + 3.150 + 3.300)

(3.450 + 2.150 + 1.100)

(1.450 + 3.150 + 3.100)

(3.200 + 2.450 + 1.700)1

(1.200 + 3.450 + 3.700)]

rl350
1.2050

1200

1550

1750

1200

22001

3650-1

'i

(MPE SC/2022) Seja A = || *].

A soma dos elementos da matriz A2 é:

b) 12;

c) 15;

d) 23;

Comentários:

Note que a matriz 42 é:

Á2 = A x A

M 1]

= [2.2+ 1.3

Item. 1.3.2 + 1.3

I

Item. 2.1 + 1.11

Item. 3.1 + 1. lJ

I

: Logo, a soma dos elementos da matriz 4 2 é:

Gabarito: Letra D.

7 3

Item. 1.9 4-1

7 + 3 + 94-4

= 23

(Pref. SJC/2019) Sobre as matrizes Amxn eBpxqé correto afirmar que existe a operação:

a) A + B, se n = p b) B - A, se n = p c) A B, se m = q d) B A, se m = q e) A 4- B, se n = p
Comentários:

Vamos analisar cada alternativa.

a) ERRADO. Temos a soma das duas matrizes, que só é possível se elas apresentarem a mesma dimensão.
Para tanto, deveríamos ter m = p e n = q.

b) ERRADO. Temos uma subtração de matrizes, que só é possível se elas apresentarem a mesma dimensão.
Para tanto, deveríamos ter m = p e n = q.

c) ERRADO. Temos uma multiplicação de matrizes, que só é possível se o número de colunas da primeira (n)
: for igual ao número de linhas da segunda (p). Para tanto, deveríamos ter n = p.

d) CERTO. Temos uma multiplicação de matrizes, que só é possível se o número de colunas da primeira
(q)

: for igual ao número de linhas da segunda (m). Esse é o caso apresentado na alternativa, em que m
= q.

: e) ERRADO. Não existe divisão de matrizes.

j Gabarito: Letra D.

(Pref. Dois Córregos/2019) O produto das matrizesriI5 3

L4 2 6

r

0 , nessa ordem
1.

a) não existe, pois elas têm os números de linhas diferentes, assim como os números de colunas.

b) não existe, pois o número de linhas da primeira matriz do produto é diferente do número de colunas da segunda matriz.
c) existe, e é igual a [0

d) existe, e é igual a e) existe, e é igual a [10 ^ ].
Comentários:

Lembre-se que, multiplicar duas matrizes, devemos seguir os seguintes passos:

Item. 1. Verificar se o número de colunas da primeira matriz é igual ao número de linhas da segunda. Se essa igualdade não se verificar, não é possível realizar o produto das matrizes.
Item. 2. Obter o esquema geral da matriz-produto, que apresenta a seguinte dimensão:

Número de linhas da primeira X Número de colunas da segunda

Item. 3. Obter os elementos da matriz resultante a partir das linhas da primeira matriz e das colunas da segunda matriz.
Note que a primeira matriz apresenta dimensão 2 x 3, e a segunda matriz apresenta dimensão 3x2. Isso significa que:
Item. 1. O número de colunas da primeira matriz (3) é igual ao número de linhas da segunda (3) e,
portanto, o produto existe.
Item. 2. A matriz-produto apresenta dimensão 2x2.

Temos, então, que a matriz-produto apresenta o seguinte esquema geral:

[() ()1

Lo ol

Vamos agora para o terceiro passo:

Item. 3. Obter os elementos da matriz resultante a partir das linhas da primeira matriz e das colunas da segunda matriz.
1 5 0

4 2 1

(1.0 + 5.2 + 3.0)

.(4.0 + 2.2 + 6.0)

(1.1+ 5.0+ 3.1)

(4.1 + 2.0+ 6.1).

b.G..a..b...a..r.i.t.o L..e..tra D.

Propriedades da multiplicação de matrizes

A propriedade comutativa não vale para matrizes

Antes de apresentarmos as propriedades da multiplicação de matrizes, vamos mostrar uma propriedade que não pode ser utilizada para matrizes.
Na álgebra comum, a propriedade comutativa para a multiplicação de números nos diz que "a ordem dos fatores não altera o produto". Isso significa que:
150 x 311 = 311 x 150

Para o caso das matrizes, essa propriedade não ocorre. O produto da matriz A pela matriz B é diferente do produto da matriz B pela matriz A (a não ser que a igualdade ocorra por uma grande coincidência).Isso significa que:
AB + BA

INDO MAIS

FUNDO!

Perceba que em alguns casos o produto AB existe e o produto BA não existe.

Considere a matriz ^2x3 de ordem 2 x 3 e a matriz B3x4 de ordem 3x4.

Note que o produto AB existe, pois 0 número de colunas de A é igual ao número de linhas defí.
Colunas da 1a = Linhas da 2a

A2X3 B3X4

Produto: Linhas da 1a e Colunas da 2a

Por outro lado, o produto BA não é possível, pois 0 número de colunas de B não é igual ao número de linhas de A.
Colunas da 1a Linhas da 2a

B3X4 A2X3

O produto BA não é possível!

Propriedade associativa

Propriedade associativa entre matrizes

Na álgebra comum, a propriedade associativa para a multiplicação de números nos diz que podemos agrupar números que estão sendo multiplicados da forma que nos for conveniente.
Por exemplo, ao realizar a multiplicação 2x3x5, podemos realizar de duas maneiras:

* (2 x 3) x 5; ou

* 2 x (3 x 5).
Isso significa que:

(2 x 3) x 5 = 2 x (3 x 5)

Para a multiplicação de matrizes, temos a mesma propriedade.

Para o caso em que é possível o produto das matrizes A, B e C, nessa ordem, podemos realizar o produto
ABC de duas formas:

* Realizar o produto AB e depois multiplicar pela matriz C; ou

* Realizar o produto BC e depois realizar o produto de A com o resultado BC.

Em linguagem matemática, temos:

(AB~)C = A(BC~)

Propriedade associativa entre matrizes e um número real

Se a for um número real e A e B forem matrizes em que o produto AB é possível, então:

aíAB) = (aA)B = A(aB)

Exemplo:

3Q4B) = (34)B = X(3B)

Propriedade distributiva

Propriedade distributiva pela esquerda

Na álgebra comum, a propriedade distributiva pela esquerda ocorre quando realizamos a seguinte operação:
2 x (3 + 5) = 2 x 3 + 2 x 5

Temos a mesma propriedade quando realizamos a operação contrária, conhecida por "colocar o número em evidência":
2 x 3 + 2 x 5 = 2 x (3 + 5)

Para matrizes, é válida a propriedade distributiva pela esquerda:

A(B + C) =AB + AC

A mesma propriedade ocorre quando "colocamos uma matriz em evidência":

AB + AC = A(B + C)

Propriedade distributiva pela direita

Na álgebra comum, a propriedade distributiva pela direita ocorre quando realizamos a seguinte operação:(3 + 5) x 2 = 3 x 2 + 5 x 2

Temos a mesma propriedade quando realizamos a operação contrária, conhecida por "colocar o número em evidência":
3 x 2 + 5 x 2 = (3 + 5) x 2

Para matrizes, é válida a propriedade distributiva pela direita:

(B + C)A = BA + CA

A mesma propriedade ocorre quando "colocamos uma matriz em evidência":

BA + CA = (B + C)A

FIQUE

ATENTO!

Vimos no tópico anterior que, para a álgebra, é válida a propriedade comutativa. Portanto,
2 pode comutar com (3 + 5):

2 x (3 + 5) = (3 + 5) x 2

Note, porém, que a multiplicação de matrizes não goza da propriedade comutativa.

Portanto, A não comuta com (B + C):

A(B + C) + (B + C)4

Isso porque A(B + C) é igual a AB + AC. Já (B + C)A é igual a BA + CA.

Elemento neutro da multiplicação de matrizes

Quanto temos uma matriz quadrada de ordem n (Anxn), a multiplicação dessa matriz pela matriz identidade de ordem n (In) corresponde à própria matriz original:
AI = IA = A

Exemplo:

3 7 2

5 4 1

3 1 4

1 0 0

0 10

0 0 1.

1 0 0

X 0 10

0 0 1.

3 7 2

X 5 4 1

3 1 4

3 7 2

= 5 4 1

3 1 4

3 7 2

= 5 4 1

3 1 4

Traço de uma matriz quadrada

0 traço de uma matriz quadrada é a soma dos elementos da sua diagonal principal. Se A é uma matriz quadrada, então o seu traço é representado por tr(A).
Exemplo:

7 2'

4 1

1 4.

tr(A) = 3 + 4 + 4 = 11

Propriedades do traço de uma matriz

Considere as matrizes quadradas de mesma ordem A e B e o número real a. 0 traço de uma matriz apresenta as seguintes propriedades:
* tr (4 + fi) = trQ4) + tr(fi)

* tr (A — B) = tr(A) — tr(B)

* trÇaA) = a x tr(4)

* tr (AB) = trÇBA)

Matriz oposta

Dada uma matriz A, a sua matriz oposta é — A.

Exemplo:

3 -7 6 '

A = -5 3 1

3 1 --4.

Oposta de A:

-A =

-3 -(-7) -6

-(- 5) -3 -1

-3 -1 -(-4)

-A =

-3 7 -6

5 -3 -1

.-3 -1 4

Matriz transposta, simétrica e antissimétrica

Matriz transposta

A transposta de uma matriz A corresponde à matriz cujas linhas foram transformadas em colunas.

* A primeira linha de A se torna a primeira coluna de A1-;

* A segunda linha de A se torna a segunda coluna de A^,

* A terceira linha de A se torna a terceira coluna de

* Etc.

A representação da matriz transposta é simbolizada por AT ou Xt. Exemplos:

0 -9

1 5

Item. .4 1 .

' 3 -7

A = -5 3

6 3 -5 3

1 -> AÈ = -7 3 1

3 1 -4

Propriedades da matriz transposta

A matriz transposta goza das seguintes propriedades:

. 6 1 -4

* A transposta da transposta corresponde à matriz original:

(A^ = A

* Transposta do produto de uma matriz por um número real:

(cM/ = a A1

* Transposta do produto de matrizes:

(7lB)t = BlAl

* Transposta da soma:

Matriz simétrica

(A + B)t = At + Bt

Uma matriz A é dita simétrica quando ela é igual a sua transposta:

A = A{

Exemplo:

3 -5

A = -5 3

3 3 -5 3

1 -> A¹ = -5 3 1

3 1 -4. . 3 1 -4.

Uma matriz é simétrica quando:

* É quadrada; e

* Os elementos simétricos com relação à diagonal principal são iguais.

Veja mais atentamente o exemplo anterior:

Matriz antissimétrica

Uma matriz A é dita antissimétrica quando:

AL = -A

Exemplo:

0 5 -3

A = -5 0 1

3 -1 0

-> A1 =

0 -5 3

5 0 -1

-3 1 0

Uma matriz é antissimétrica quando:

* É quadrada;

* A diagonal principal é nula; e

* Os elementos simétricos com relação à diagonal principal são opostos

Veja mais atentamente o exemplo anterior:

'2

(SEDF/2017) Considerando a matriz A = 4

.0

0 10'

10 20 , julgue o próximo item.
2 40.

Se B = 1

y x -7'
0 z

10 0 .

e a matriz A + B for simétrica, então x + y + z = 0.

Comentários:

Primeiramente, vamos determinar .4 + B.

'2 0 10' 0 X —7"

A + B =

4 10 20 +

Item. .0 2 40.

1 0 z y 10 0 .
2 + 0

4 + 1

Item. .0 + y

0 + x

10 + 0

2 + 10

x

10 - 7'

20 + z

40 + 0.

5 10

y 12

20 + z

Para uma matriz ser simétrica, ela deve ser quadrada e os elementos simétricos com relação à diagonal principal devem ser iguais.
Observe novamente a matriz A + B:

Para ela ser simétrica, devemos ter:

Logo, x+y+z=5+3+ (-8) = 0.

L Gabarito: CERTO.

x 3

5 "10^20 + z
Ly 12 40. *

x = 5 x = 5

y = 3 -> y = 3
120 + z = 12 z = —8

(AFRFB/2014) A matriz quadrada A, definida genericamente por A = a^, é dada por ari = 0; a12 = —
4;
a13 = 2;a21 = x; a22 = 0; a23 = (1 — z);a31 = y; a32 = 2z e, por último,
a33 = 0. Desse modo, para que a matriz A seja uma matriz antissimétrica, os valores de a21, a23, a31 e a32 deverão ser,respectivamente,
iguais a:

a) 4; -2; -2; -2.

b) 4; -2; 2; -2.

c) 4; 2; -2; -2.

d) -4; -2; 2; -2.

e) -4; -2; -2; -2.

Comentários:

Vamos montar a matriz em questão.

'all a12 a13~

a21 a22 a23

.a31 a32 a33.

0 -4 2 '

A = X 0 1 — z y 2z 0
Para uma matriz ser antissimétrica, ela deve ser quadrada, a diagonal principal deve ser nula, e os elementos simétricos com relação à diagonal principal devem ser opostos.
Observe novamente a matriz A:

Para ela ser antissimétrica, devemos ter:

Portanto, x = 4,y = —2, e:

^-4 2 '

x i - z y 2z
( x = -(-4)

| y = -2

2z. = —(1 — z)

2z = —(1 — z)

2z = —1 + z

2z — z = —1

z = — 1

Obtidos os valores de x, y e z, temos a seguinte matriz A:

0 -4 2 '

A = X 0 1 — z y 2z 0
2'

0.

Logo, os valores de a21, a23, a31 e a32 deverão ser, respectivamente, iguais a 4,2, —2, —2.

Gabarito: Letra C.

Matriz inversa

Definição

A inversa de uma matriz A (notação: A-1) é aquela matriz que, quando multiplicada pela matriz A tem como resultado a matriz identidade:
A A-1 = A-1 A = In

Uma matriz que não possui inversa é denominada singular.

A não possui inversa <-> A é singular

Caso o assunto determinantes faça parte do seu edital, veremos que uma matriz é inversível (possui inversa)quando o seu determinante é diferente de zero. Caso contrário, isto é, caso a matriz tenha determinante zero, ela é singular (não possui inversa).
Vamos a um exemplo que pode ser cobrado em prova:

Seja A = ri 3i j. Determine a matriz inversa de A.

Considere, genericamente, que A 1 = [a Nesse caso:

Lc aJ

ío 2I

AA~1 = I2

bi ri 0]

lJ

Realizando o produto de matrizes, temos:

rla + 3c lb + 3dj 1

ha + 2c 0b + 2dJ_ 1-0lJ

rla + 3c lb + 3dj -í1 °1

I. 2c 2d J lJ

Como as duas matrizes são iguais, seus elementos são iguais:

la + 3c = 1
lb + 3d = 0
2c = 0

2d = 1

rla + 3c = 1

lb + 3d = 0

< c = 0

Sabemos que c = 0. Temos que:

la + 3c = 1

Sabemos que d = |. Temos que:

b = ~2

1(2 + 0 — 1

a = l lb + 3d = 0
b = —3d

Portanto, a matriz inversa A 1 = ía

Lc (2-1

Vamos resolver dois exercícios:

é dada por:

1 —3/2

0 1/2 .

.......................................... ..................................... i í (ANPEC/2018) Classifique a afirmação abaixo segundo a sua veracidade:
= Se uma matriz tem inversa, então ela é singular.

= Comentários:

: Uma matriz é singular quando ela não possui inversa.
i Gabarito: ERRADO.

(MPE SP/2019) A inversa da matriz [2 é:
0,5 0,2

a) . 1 0,33

b) r 3 -5]

.-1 2 J

3 5

c)l

-1 2-

d) r 3 -n

[-5 21

r0,33 0,2

e) . 1 0,5

Comentários:

Considere, genericamente, que A 1 = [a + Nesse caso:

te ai

AA-1 = 12

í2 5]x[a

Ll 3J Lc dl Lo

Realizando o produto de matrizes, temos:

[2a + 5c 2h + 5dj í1 °1
Lia + 3c lb + 3di ~ Lo iJ

Como as duas matrizes são iguais, seus elementos são iguais:

2a + 5c = 1

2b + 5d = 0

la + 3c = 0

lb + 3d = 1

Multiplicando a terceira equação por —2 e somando com a primeira, temos:

* 2a + 5c = 1

-2a - 6c = 0

—c = 1

Portanto, c = —1.

Da terceira equação, temos:

a + 3c = 0
a — 3 = 0

a = 3

Multiplicando a quarta equação por —2 e somando com a segunda, temos:

2b + 5d = 0

—2b — 6d = —2

-d = -2

Portanto, d = 2.

Da quarta equação, temos:

lZ? + 3d = 1

b + 6 = 1

h = -5

Logo, a matriz inversa X-1 = j é:

Gabarito: Letra B.

Propriedades da matriz inversa

Inversa da inversa

A matriz inversa da inversa de A é a própria matriz A:

(A-1)-1 = A

Inversa da transposta X Transposta da inversa

A matriz inversa da transposta de A é igual a matriz transposta da inversa de A:

(A-1^ = (A1)-1

Inversa do produto de uma matriz por um número real

Considerando uma matriz A inversível e um número real a, temos:

= —J4_1

a

Exemplo:

(3?!)-1 = I^T1

Inversa do produto de matrizes

Considerando duas matrizes A e B inversíveis, a inversa do produto AB é:

Q4B)-1 = B 'A '

Para mais termos, segue-se a mesma lógica:

(ABCy1 = C~1B~1A~1

Matriz inversa como análogo da divisão

Pessoal, a primeira coisa que devemos saber é que não existe a operação de divisão para matrizes.
Feita essa observação, vamos entender o porquê de a matriz inversa ser o análogo da divisão.
Considere que, em um problema de álgebra, você chegue na seguinte equação:

3x = 9

O que você faz para obter o valor de x? Ao "jogar o 3 para o outro lado da equação", na verdade você está dividindo ambos os lados da equação por 3:
3% _ 9

x = 3

Agora vamos para um problema de matrizes. Suponha que você tenha as matrizes quadradas AeB e que você queira determinar uma matriz X em que:
AX = B

Note que não podemos dividir ambos os lados da equação matricial por A, pois não existe a operação de divisão para matrizes. Observe, porém, que podemos multiplicar ambos os lados da equação por A 1pela esquerda (caso a matriz A seja inversível, isto é, caso ela não seja singular). Assim:
A~'AX = A'B

Note que, por definição de matriz inversa, A_1A = I. Portanto:

IX = A-1B

A matriz identidade 7 é o elemento neutro da multiplicação de matrizes e, por isso, IX = X. Logo,
ficamos com:
X = A^B

Isso significa que a matriz X que queremos determinar é o produto da inversa de A pela matriz B.

(SEFAZ MG/2005) A, B e C são matrizes quadradas de mesma ordem, não singulares e diferentes da matriz identidade. A matriz C é igual ao produto AZ B, onde Z é também uma matriz quadrada. A matriz Z,portanto, é igual a:

a) A~1BC

b) AC^B-1

cJ/T1 C B-1

d) AB C-1

e) C~1B-1A-1

Comentários:

ESTA É

DIFÍCIL!

Note que todas as matrizes são quadradas, de mesma ordem e admitem inversa (pois não são singulares).
A matriz C é igual ao produto AZB. Logo:

AZB = C

Ao multiplicar ambos os lados da equação por A 1 pela esquerda, temos:

A~rAZB = A-1C
(A^AjZB = A-1C
(T)ZB = A~1C
ZB = A-1C

Ao multiplicar ambos os lados da equação por B 1 pela direita, temos:

ZBB'1 =

ZÇBB-1) = A^CB1

Z(C) = A~1CB~Í

Z = A~1CB~1

Portanto, a matriz Z é igual a A~XCB~\

Gabarito: Letra C.

i (Pref Paulínia/2021) Considere a equação matricial j42X 1B 1 = AC, onde A, B, C
e X são matrizes i quadradas invertíveis e de mesma ordem.
A solução X é igual a
;

Ía).4B_1C-1

i bjAC^C-1
Í

: c) CA~rB
:

d)4-1BC
:

[^B^C^A

= Comentários:

= Sabemos que todas as matrizes quadradas são inversíveis e de mesma ordem. Note que:

^X^B-1 = i4C

AAX~rB~r = AC

Ao multiplicar ambos os lados da equação por .4-1, pela esquerda, temos:

= A-1AAX~1B~1 = A_1AC
=
(A~1A)AX~1B~1 = (A~1A)C

(I)AX~1B~1 = (I)C

í AX~1B~1 = C
!

Ao multiplicar ambos os lados da equação novamente por >4_1, pela esquerda, temos:

A~1AX~1B~1 = A~1C

(A-1A)X~1B~1 = A~1C !

(OX^B-1 = A^C

; X-1B~1=A~1C
=

Ao multiplicar ambos os lados da equação por X, pela esquerda, temos:

XX-1B-1 = XA~*C
(XX-^B-1 = XA^C
(TiB-1 = XA~rC
B'1 =XA~1C

Logo:

XA^C = B-1

Ao multiplicar ambos os lados da equação por C_1, pela direita, temos:

XA^C C-1 = B-1 C'1
XA_1(C C^1) = B-1 C-1
XA-^I) = B-1 C~1

XA-1 = B-1 C-1

Finalmente, ao multiplicar ambos os lados da equação por A, pela direita, temos:

XA~rA = B-1 C_1A
XÇA^A) = B'1 C_1A
X(I) = B-1 C^A

X = B1 C'A

Gabarito: Letra E.

Matriz ortogonal

Uma matriz A é dita ortogonal quando a sua inversa é igual a sua transposta:

A é ortogonal -o A-1 = A1-

Sabemos que, pela definição de matriz inversa:

A-1 A = AA-1 = I

Quando a matriz A é ortogonal, uma vez que A 1 = A(, temos:

A1 A =AAt = I

r...................................................................................................

í (TRANSPETRO/2018) A inversa de uma matriz ortogonal é igual à sua
I

A) adjunta

: B) adjunta transposta

= c) cofatora d) cofatora transposta
= e) transposta

; Comentários:

: Uma matriz é ortogonal quando a sua inversa é igual a sua transposta.

j Gabarito: Letra E.

r...................................................................................................

(ANPEC/1998) Uma matriz A, quadrada de dimensão n é dita ortogonal quando ALA = A A1- = In , onde o superescrito t denota transposição e In é a identidade de dimensão n. Considere uma matriz ortogonal A de ordem n. Classifique como certo ou errado a afirmação (sobre A) abaixo:
Sua inversa e sua transposta são também matrizes ortogonais.

Comentários:

ESTA É

DIFÍCIL!

Note que a matriz A é ortogonal. Isso significa que:

Devemos responder duas perguntas:

i * A matriz A 1 é ortogonal?

: * A matriz A1 é ortogonal?
;

; Para que i4_1 seja ortogonal, devemos ter que a sua inversa Q4-1)-1 seja igual a sua transposta
C4_1)f.

I

A única informação que temos ao certo é que A-1 = A(. Fazendo a transposta em ambos os lados da i

: equação, temos:

: Qr1)* = (A*?
:

: Como (Ay = A, temos:
;

j = A
!

: Observe que>l = Q4-1)-1. Logo:

: OT1/ = G4"1)"1
j i Portanto, é verdade que é ortogonal, pois a sua inversa Q4-1)-1 é igual a sua transposta i
I
I

: Como A-1 é ortogonal, AÈ também é. Sabemos, pelos dados do problema, que 4_1 = Af. Como já obtemos i que = G4-1)-1, basta substituir 4-1 por 4^;

j OT1/ = Gr1)"1
j

(Ay = (Ay1

= Portanto, também é verdade que A* é ortogonal, pois a sua inversa (Xí)_1 é igual a sua transposta
; Gabarito: CERTO.

DETERMINANTES

Determinantes

Noção básica e representação

Um determinante é um número calculado a partir de uma matriz quadrada. Representado por duas barras"| |".
Determinante de matriz de ordem 1
O determinante de uma matriz de ordem 1 é o próprio elemento da matriz.

Determinante de matriz de ordem 2

= lc dl detX = ad — bc

(Produto dos elementos da diagonal principal) — (Produto dos elementos da diagonal secundária)

Determinante de matriz de ordem 3

Regra de Sarrus

Parte Negativa Parte Positiva deti4 = [«n«22a33 + a12a23a31 + a13a21a32J " ta13a22a31 + alla23a32 + a12a21a33l
Obtenção do determinante de matrizes de qualquer ordem

|l\/lenor complementa

O menor complementar de um elemento de uma matriz A é o determinante Dy da matriz obtida eliminando-se a linha i e a coluna / da matriz A
|Cofator ou complemento algébrico|

O cofator do elemento ay de uma matriz A é um número representado por Ay calculado do seguinte modo:
At] = (-l)'+^y peorema de Laplace|
O determinante de uma matriz A é a soma dos produtos dos elementos de uma fila qualquer (linha ou coluna) pelos seus respectivos cofatores.
Item. 1. Escolher uma fila (linha ou coluna), preferencialmente a que tiver mais zeros;

Item. 2. Realizar o produto de cada elemento da fila pelo seu respectivo cofator; e

Item. 3. Somar os produtos obtidos.

Propriedades dos determinantes

* Teorema de Binet: det(AB) = det A x det#

* Determinante da matriz inversa: det A-1 = — det A

* Determinante da matriz transposta: detAf = det A

* Multiplicação de uma fila por uma constante: ao multiplicar uma fila (linha ou coluna) de uma matriz por uma constante k, o determinante dessa nova matriz também fica multiplicado por k.
* Multiplicação da matriz por uma constante: det(Zo4) = kn det A

* Determinante de matriz triangular ou de matriz diagonal: o determinante é o produto dos elementos da diagonal principal.
* Fila nula: uma matriz que apresenta uma fila (linha ou coluna) cujos elementos são todos zero apresenta determinante zero.
* Filas paralelas iguais: uma matriz com filas paralelas iguais (linhas ou colunas) apresenta determinante zero.
* Filas paralelas proporcionais: uma matriz com filas paralelas proporcionais (linhas ou colunas)
apresenta determinante zero.

* Troca de filas paralelas: ao trocarmos uma fila (linha ou coluna) de lugar com outra fila paralela, o determinante muda de sinal.
* Combinação linear de filas: quando uma matriz apresenta uma fila (linha ou coluna) que é combinação linear de outras filas, o seu determinante é zero.
Teorema de Jacobi

Ao multiplicar uma fila por qualquer número e somar esse resultado a uma outra fila paralela qualquer, o valor do determinante não se altera. Em outras palavras, podemos trocar uma fila qualquer por uma combinação linear que contenha a fila original.
Regra de Chió

* Fazer com que o elemento alr seja igual a 1;

* Zerar todos os elementos da primeira linha, à exceção de allr fazendo uso da primeira coluna;

* Feita a operação anterior, o determinante em questão é igual ao menor complementar D^;

* Repita o processo, se necessário, para reduzir a ordem do determinante mais uma vez.

Matriz inversa

A é inversível < > det A =# 0
A é singular < > det A = 0

A=\a ;i-'>1

Lc dJ detx L—c a J

Noção básica e representação

Pessoal, a aplicação prática de determinantes surge quando estudamos sistemas lineares, que será visto na sequência, caso faça parte do seu edital.
Nesse momento, deve-se entender que um determinante é um número calculado a partir de uma matriz quadrada.
Considere uma matriz A dada por A =

r 4 3i j. Seu determinante, como veremos adiante, é o número 11.
A representação do determinante de A pode ser feita de duas formas:

* detX = 11; ou

I 4

1-1

FIQUE

ATENTO!

Vimos na seção de matrizes que podemos representá-las tanto com colchetes "[ ]" quanto com parênteses "()". A matriz A, portanto, pode ser representada dessas duas formas:
Já o determinante da matriz A é representado por duas barras "| |", e o seu cálculo corresponde a um número.
det4 = 3| = 11

Determinante de matriz de ordem 1

Uma matriz quadrada de ordem 1 é uma matriz que apresenta uma única linha e uma única coluna.Exemplo:

AlXl = [7]

O determinante de uma matriz de ordem 1 é o próprio elemento da matriz. Exemplos:

* A - [3] -> detX = 3;

* B - [V5] -> detF = V5;

* C - [-2] -> detC = —2.

Determinante de matriz de ordem 2

Para calcular o determinante de uma matriz quadrada de ordem 2, devemos realizar a seguinte operação:(Produto dos elementos da diagonal principal) - (Produto dos elementos da diagonal secundária)

Considere a matriz de ordem 2 genérica, dada por A = j. Seu determinante é dado por:

detd = ad- bc

Vamos a um exemplo numérico:

detX = [4 x 2] - [3 x (-1)]

= 8 - (-3)

= 11

(Pref. N Horizonte/2019) O número real que verifica se o valor do determinante da matriz

= a 18 é:

í a) 54.

b) 36.

j c) 27.

d) 9.

! e)3.

= Comentários:

: O determinante da matriz em questão é dado pela seguinte operação:

; (Produto dos elementos da diagonal principal) - (Produto dos elementos da diagonal secundária)
= Para que o valor do determinante seja igual a 18, devemos ter:

: (x2 x 2x) - (4 x 9) = 18

j 2x3 - 36 = 18

í 2x3 =54

j x3 = 27

: X3 = 33

: X = 3

; Gabarito: Letra E.

Determinante de matriz de ordem 3

Para calcular o determinante de uma matriz quadrada
Considere a matriz A:

de ordem 3, vamos utilizar a regra de Sarrus.

Para aplicar a regra de Sarrus, devemos repetir as duas primeiras colunas da matriz após a terceira coluna:
4 2 2

3 -1 -1

-5 -3 -3

Nesse momento, vamos dividir o cálculo em 2:

* Parte positiva;

* Parte negativa.

A parte positiva é obtida por meio das diagonais para a direita. Para obtê-la, multiplicamos os elementos dessas diagonais e somamos os valores.
[4. (—1). 1 + 2.4. (-5) +(-2). 3. (-3)]

= [(-4) + (-40) + 18]

= -26

A parte negativa é obtida por meio das diagonais para a esquerda. Para obtê-la,
multiplicamos os elementos dessas diagonais e somamos os valores.
[(—2). (—1). (—5) + 4.4. (-3)+ 2. 3.1]

= [(-10) + (-48) + 6]

= -52

Para obter o determinante, tomamos a parte positiva e subtraímos a parte negativa.

det A = (Parte positiva) — (Parte negativa)

= (-26) - (-52)

= -26 + 52

= 26

De modo genérico, temos a seguinte representação da regra de Sarrus:

FIQUE

ATENTO!

r

(CRM PR/2014) Qual deve ser o valor de X para que o determinante seja 0,5?

13 5

2X6

0 11

a) 0,5

b) l c) 1,5
d) 2

e) 2,5

Comentários:

Vamos aplicar a regra de Sarrus no determinante em primeiras colunas da matriz após a terceira coluna:
13 5

2X6

0 11

questão. Primeiramente, devemos repetir as duas
1 3

2 X
0 1

Em seguida devemos calcular a parte positiva e a parte negativa para, na sequência, realizar a subtração:
Parte Negativa Parte Positiva

[1.X. 1 + 3. 6.0 + 5. 2.1] - [5.X. 0 + 1. 6.1 + 3.2.1]

= [X + 10] - [6 + 6]

= X-2

Portanto, o determinante em questão é X — 2. O valor de X para que o determinante seja igual a 0,5
é:

X - 2 = 0,5

X = 2,5

Gabarito: Letra E.

Obtenção do determinante de matrizes de qualquer ordem

Para que possamos calcular o determinante de matrizes de ordem superiores a 3, devemos compreender primeiramente os conceitos de menor complementar e de cofator (ou complemento algébrico).
Menor complementar

Considere uma matriz A de ordem maior ou igual a 2.

O menor complementar de um elemento qualquer dessa matriz A é o determinante Djj da matriz resultante ao se eliminar a linha e a coluna em que esse elemento se encontra.
ATENÇÃO

DECORE!

Em outras palavras, o menor complementar de um elemento a.-j de uma matriz A é o determinante da matriz obtida eliminando-se a linha i e a coluna / da matriz A.
Professor, não entendi noda!

Calma, amigo. Essas coisas só se entendem com um exemplo mesmo!
Considere a seguinte matriz A:

Para calcular o menor complementar do elemento a₁₂, isto é, para obter calcular o determinante D₁₂,

precisamos eliminar a linha e a coluna do elemento a₁₂.

Note que a₁₂ = 2, e esse elemento está na primeira linha e na segunda coluna da matriz A.

z i

A = 3 — 1 4
L-5 — lJ

Logo, o determinante D12 correspondente ao menor complementar de a12 é:

D₁₂ = [3 x 1] - [4 x (-5)]

D₁₂ = 3 - (-20)

(MPOG/2005) O menor complementar de um elemento genérico Xj,- de uma matriz X é o determinante que se obtém suprimindo a linha e a coluna em que esse elemento se localiza. Uma matriz Y = ytj ,de terceira ordem, é a matriz resultante da soma das matrizes A = (aij) e B = (bij).Sabendo-se que (aÍ7)

= (i + j)2 e que btj = i2, então o menor complementar do elemento y23 é igual a:

A)0

b) -8

c) -80

d) 8

e) 80

Comentários:

A matriz Y é a soma as matrizes A e B.

Os elementos da matriz A são dados por = (i + j)2. Logo:

ail = (1 + l)2 = 4 ; a12 = (1 + 2)2 = 9; a13 = (1 + 3)2 = 16

a21 = (2 + l)2 = 9 ; a22 = (2 + 2)2 = 16 ; a23 = (2 + 3)2 = 25

a31 = (3 + l)2 = 16; a32 = (3 + 2)2 = 25 ; a33 = (3 + 3)2 = 9

Portanto, a matriz A é dada por:

' 4 9 16'

A = 9 16 25

Item. .16 25 36.

Os elementos da matriz B são dados por bjj = i2. Logo:

b±i = l2 = 1; b12 = l2 = 1; ò13 = l2 =1

/?2i = 22 = 4; b22 = 22 = 4; b23 = 22 =4

b31 = 32 = 9; b32 = 32 = 9; b33 = 32 =9

Portanto, a matriz B é dado por:

A matriz Y é a soma das matrizes A e B:

1 1 1

B = 4 4 4

Item. .9 9 9.

'4 9 16

1 1 1

Y = A + B =

9 16 25

Item. .16 25 36.

+ 4 4 4

Item. .9 9 9.

' 5 10 17'

Y = 13 20 29

Item. .25 34 45.

......................... ........................ i í Perceba que o elemento y₂₃ é igual a 29. O menor complementar de y₂₃ é o determinante da matriz que
: se obtém eliminando a linha 2 e a coluna 3:

' 5 10 1 7'

13 20 2 9

L25 34 4 5]

i

Logo, o determinante Z)23 correspondente ao menor complementar de y23 é:

I 5 10

Gabarito: Letra C.

125 34l

= [5 x 34] - [10 x 25]

= -80

I

Cofator ou complemento algébrico

Considere uma matriz A de ordem maior ou igual a 2.

O cofator de um elemento aLj dessa matriz A é um número representado por A^ calculado do seguinte modo:
= (-1)™DV

Onde Djj é 0 menor complementar do elemento a^.

Utilizando como exemplo a mesma matriz:

Temos que 0 cofator do elemento a12 é dado por:

-^12 = (—1)1+2^12

Do item anterior, já obtemos que 0 menor complementar D₁₂ é igual a 23. Logo:

rl12 = (-D3 x 23
Â₁₂ = (-1) x 23

= -23

Portanto, 0 cofator do elemento a17 é .412 = -23.

Teorema de Laplace

O Teorema de Laplace serve para obtermos o determinante de qualquer matriz quadrada de ordem maior ou igual a 2.
Vamos conceituar o teorema:

TOME

NOTA!

O determinante de uma matriz A é a soma dos produtos dos elementos de uma fila qualquer
(linha ou coluna) pelos seus respectivos cofatores.

Vejamos o teorema com mais detalhes. Em resumo, ele consiste em seguir 3 passos:

Item. 1. Escolher uma fila (linha ou coluna), preferencialmente a que tiver mais zeros;

Item. 2. Realizar o produto de cada elemento da fila pelo seu respectivo cofator; e

Item. 3. Somar os produtos obtidos.

Vamos realizar um exemplo para que tudo fique mais claro.

EXEMPLIFICANDO

3 2 3 1

Calcule o determinante de A = -1

2 0 8

-1 0 6

2 4 0 3

Note que temos uma matriz quadrada de ordem 4. Seu determinante não pode ser obtido pela regra de
Sarrus. Nesse caso, devemos seguir os três passos do Teorema de Laplace.

Item. 1. Escolher uma fila (linha ou coluna), preferencialmente a que tiver mais zeros:

Vamos escolher a terceira coluna, pois ela apresenta três zeros.

3 2 3 1

4 = -1 2 0 8

5-106

Item. .2 4 0 3.

Item. 2. Realizar o produto de cada elemento da fila pelo seu respectivo cofator

Lembre-se que o cofator é definido como = (—l)l+JDij. Devemos, portanto, calcular os seguintes produtos:
^13-^13 a23-^23 a33-^33 a43^43

Cálculo de a13j413

a13-^13 — 3 X >113

= 3 x (-1)1+3D13

-3——2—I F -4

-1 2 ) 8

5 -1 1 ) 6

2 4 3

-1 2 8

-1 6

2 4 3

-1 2 8

Aplicando a regra de Sarrus em 5 -1

2 4

6 obtém-se 197.

Logo:

-1

= 3 5

2 8

-1 6

4 3

3 x 197

= 591

Cálculo de «23^23

Note que 0 elemento a23 é zero, de modo que 0 produto a237423 será zero:

<^23^23 = 0 x í4₂₃ = 0

Cálculo de a33A33

Note que 0 elemento a33 é zero, de modo que 0 produto a33A33 será zero:

a33^33 = 0 x t4₃₃ = 0

Cálculo de a44A43

Note que 0 elemento a43 é zero, de modo que 0 produto a437443 será zero:

<^43-^43 = 0 X 4₄₃ = 0

Item. 3. Somar os produtos obtidos

Por fim, para obter o determinante, soma-se os produtos obtidos:

det>l = <131^31 + <^32-^32 + a33-^33 + d43A43

= 591 + 0 + 0 + 0

= 591

Logo, determinante de A é 591.

Destaca-se a importância de se selecionar a fila (linha ou coluna) com o maior número de zeros. Caso tivéssemos selecionado outra fileira, 0 trabalho teria sido muito maior, pois teríamos que calcular mais determinantes de ordem 3. Vejamos:
EXEMPLIFICANDO

3 2 3 1

Calcule o determinante de A = -1

2 0 8

-1 0 6

2 4 0 3

Item. 1. Escolher uma fila (linha ou coluna), preferencialmente a que tiver mais zeros

Vamos supor que tenhamos escolhido a segunda linha, que não é a fila que apresenta mais zeros.

3 2 3 1

-12 0 8

5-106

2 4 0 3.

Item. 2. Realizar o produto de cada elemento da fila pelo seu respectivo cofator; e

Item. 3. Somar os produtos obtidos.

Nesse caso, 0 determinante seria calculado da seguinte forma:

det.4 = «21^21 + ^22^22 + ^23-^23 + ^24^24

(-1). (-1)2+1D21 + 2. (-1)2+2D22 + 0. (-1)2+3O23 + 8. (—1)2+4D24

— ^21 + 2^22 + 8Z?24

2 3 1

-1 0 6 + 2

4 0 3

3 3 1

5 0 6 + 8

2 0 3

3 2 3

5 -1 0

2 4 0

......................... ........................ i

Aplicando a regra de Sarrus para os três determinantes, obtém-se 81, —9 e 66, respectivamente.
Portanto:

detX = 81 + 2 x (-9) + 8 x 66

: = 81 - 18 + 528
:

=591
i

: Note que chegamos no mesmo resultado, porém foram necessárias 3 aplicações da regra de Sarrus.

Vamos resolver um problema de concurso público.

(SEFAZ-RS/2014) O determinante da matriz a) -32
b) -26

c) 14

d) 16

e) 28

Comentários:

1 2

A = 2 3

2 -3

2 1

1 Ol

1 4-1

Devemos calcular um determinante de ordem 4. Para tanto, faremos uso do Teorema de Laplace.

Item. 1. Escolher uma fila (linha ou coluna), preferencialmente a que tiver mais zeros;

Selecionaremos a quarta coluna, pois ela é a fila que mais apresenta zeros.

1 2 1 0

A = 2 3 1 0

2 -3 2 1

2 1 1 4

Item. 2. Realizar o produto de cada elemento da fila pelo seu respectivo cofator; e

Item. 3. Somar os produtos obtidos.

O determinante de A é dado por:

det.4 = íll4-di4 + 0124-^24 3" ®34-'^34 3" O442I44

= 0. .di4 + O.2I24 3" l--^34 3" 4VI44

= 2I34 + AA₄₄

= (—1)3+4D34 + 4 x (—1)4+4D44

= (-1)7D34 + 4x(-1)8D44

— " D34 + 4D44

Vamos aplicar a regra de Sarrus no primeiro determinante D₃₄

Parte Negativa Parte Positiva

D₃₄ = [1.3.1 + 2.1.2 + 1.2.1] - [1. 3.2 + 1.1.1 + 2.2.1]

£>34 = [3 + 4 + 2] — [6 + 1 + 4]

D34 = 9 - 11

£>34 = —2

Vamos agora aplicar a regra de Sarrus no segundo determinante £>₄₄:

Parte Negativa Parte Positiva

£>₄₄ = [1.3. 2 + 2.1. 2 + 1.2. (-3)] - [1. 3.2 + 1.1. (-3) + 2. 2.2]

D₄₄ = [6 + 4 - 6] - [6 - 3 + 8]

n44 = 4 - 11

£>44 = —7

Voltando ao cálculo do determinante de A, temos:

1 2 1 1 2 1

detX = — 2 3 1 + 4 2 3 1

2 1 1 2 -3 2

= —(—2) + 4 x (—7)

= 2-28

= -26

Gabarito: Letra B.

Propriedades dos determinantes

Teorema de Binet

O teorema de Binet nos diz que o determinante do produto de duas matrizes é igual ao produto dos determinantes das duas matrizes.
detQ4fí) = detX x detF
Esse teorema também pode ser aplicado para mais matrizes:

det(zlFC) = detzl x detfí x detC

r

(MPE-RS/2010) Considere as matrizes M = ³

1 2 2

2 eP = 5 3

1 -

4 4

Sendo Q o produto das matrizes M e P, nessa ordem, ou seja, Q = MP, o determinante da matriz Q é igual a:
a'à b) —
' 240

d) —

' 540

e) —

Comentários:

Note que a questão pede o determinante da matriz MP. Não é necessário calcular o produto das matrizes,pois, pelo Teorema de Binet, sabemos que:

det(MP) = detM x detP

O determinante da matriz M é dado por:

detM =

1 1 5-6 1

12 1Õ 60 60

O determinante da matriz P é dado por:

detP = 3

2 2 1 2 3-4 1

4_3=2_3= 6 6

Logo, o determinante de Q = MP é dado por:

det(MP) = detM x detP

L.G..a. .b..a..r..i.to...:..L..e..t.r..a...C. .

Determinante da matriz inversa

36Õ

0 determinante da matriz inversa é o inverso do determinante da matriz original.

detA 1 =

det A

INDO MAIS

FUNDO!

Essa propriedade é uma consequência do Teorema de Binet.

Pela definição de matriz inversa, temos que:

Logo, o determinante do produto é:

AA-1 = I

det(AA_1) = det/

Veremos mais adiante que o determinante de uma matriz diagonal é o produto dos elementos da diagonal. No caso da matriz identidade, esse produto será 1 x 1 x ... x 1 = 1. Portanto, det / = 1.
n vezes
(matriz de ordem rí)

Além disso, pelo Teorema de Binet, temos que det(A 1A) = det A x det A 1. Logo:

det(AA 1) = det/
detA x detA 1 = 1

detA 1 =

detA

Determinante da matriz transposta

O determinante da matriz transposta é igual ao determinante da matriz original.

detXt = detA

(TRT 11/2017) Se A é uma matriz quadrada de ordem 2 tal que Ari inversa da matriz transposta de A é igual a a) -0,20
b) -0,40

c) -0,25

d) -0,50

Comentários:

A questão pergunta pelo determinante da inversa da transposta.

A^> AÇ (A^-1

: transposta inversa da transposta
= O determinante da matriz A é dado por:

= 3Ji

, então o determinante da detA =
1 3I

2 ll i s
= [1 x 1] - [3 x 2]

= 1-6

= -5

Lembre-se que det A( = det A. Logo, o determinante da inversa da transposta é:

detO^)-1 = -——-

detCA4)

Gabarito: Letra A.

detA

= z5

= -0,2

Multiplicação de uma fila por uma constante

Ao multiplicar uma fila (linha ou coluna) de uma matriz por uma constante k, o determinante dessa nova matriz também fica multiplicado por k.
EXEMPLIFICANDO

Exemplo: considere a seguinte matriz A.

detX = 3x3 — 2x1 = 7

Multiplicando uma das filas de A por 5, obtemos uma nova matriz, que chamaremos de A'. Observe que o determinante de A' fica multiplicado por 5. Veja:
5x2]

5 x 3J

detTl' = 2 x 15 - 10 x 1

= 45-10

= 35

Uma consequência interessante dessa propriedade é realizar a operação inversa, removendo um fator comum de dentro do determinante. Veja:
|2 10| _ |2 5 x 2| = 5 x I3 2|

ll 15l ll 5 x 3I ll 3l

Multiplicação da matriz por uma constante

Ao multiplicar uma matriz de ordem n por uma constante k, 0 determinante dessa nova matriz fica multiplicado por kn.
det(/o4) = kn det4

Exemplo: considere a seguinte matriz A = , cujo determinante é 7.

A matriz 3A é dada por:

sHxi II

= O determinante de 3A = ] é:

det34 = [9 x 9] - [6 x 3] = 63

: Note que o novo determinante é 9 vezes o determinante original, isto é:

i det(3>l) = 32 det4
;

INDO MAIS

FUNDO!

Note que, ao multiplicar uma matriz de ordem n por uma constante k, na verdade estamos multiplicando cada uma das suas n linhas (ou colunas) por k. Por isso, o novo determinante acaba sendo multiplicado por:
/c x /c x ... x k = kn n vezes

(MPE SC/2022) Seja A uma matriz 4x4 cujo determinante é igual a 2.

= O determinante da matriz 3A é igual a:

: a) 6;

b) 12;

= c) 24;

d) 64;

: e) 162.

= Comentários:

: Sabemos que, ao multiplicar uma matriz de ordem n por uma constante k, o determinante dessa nova

; matriz fica multiplicado por kn.

: det(/o4) = kn det4

: Como a matriz A é de ordem n = 4, temos:

: det(3>l) = 34 det4

j det(3X) = 81 x 2

j det(3X) = 162

: Gabarito: Letra E.

í (Pref. Gramado/2019) Considerando que a Matriz A seja quadrada de ordem 2 e que tenha determinante i igual a 2, o determinante da matriz 3.4 é:
b) 6.

c) 9.

d) 18

Comentários:

A matriz A apresenta ordem n = 2 e determinante det4 = 2.
Temos que:

det34 = 3n detX

= 32 x 2

= 9x2

= 18

Gabarito: Letra E.

í (MPOG/2008) Uma matriz X de quinta ordem possui determinante igual a 10. A matriz
B é obtida i

: multiplicando-se todos os elementos da matriz X por 10. Desse modo, o determinante da matriz B é igual a: ;
Í a) 10"6

i b) 105
c) IO10

d) 106

Comentários:

A matriz X apresenta ordem n = 5 e determinante detX = 10.

A matriz B é obtida multiplicando-se todos os elementos da matriz X por 10. Logo:

B = 10X

O determinante da matriz B é:

:LGabarito: Letra D.

detfí = det 10X

= 10ndetX

= 105 x 10

= 106

*

Determinante de matriz triangular ou de matriz diagonal

O determinante de uma matriz triangular ou de uma matriz diagonal é o produto dos elementos da diagonal principal. Exemplos:
3 2 8

0 2 2

0 0 1

0 0 0

8 = 3x2x1x3 = 18

3 0 0

1 5 0

5 7 3

= 3x5x2 = 30

1 0 0

0 2 0

0 0 5

0 0 0

0 = 1x2x5x3 = 30

* det/4 =

10 0 0

0 10 0

0 0 10

0 0 0 1

=lxlxlxl=l

(IF Baiano/2019) Seja í4₃x3 uma matriz que pode ser decomposta como o produto de outras duas matrizes
L3x3 e U3x3, onde L é uma matriz triangular inferior, com ZX1
triangular superior, tal que A = L.U

e U, uma matriz

/5 2 /^ll 0

₃ 1 4 =| hl ^22

\1 1 3/ V31 ^32

Calcule o determinante da matriz U.

a) det U = —13

b) det U = -9

c) det U = —2

d) det U = 3

e) det U = 5

Comentários:

Note que A = LU. Pelo Teorema de Binet, temos:

0 \ /Wh u12 Wi3\

0 I. I 0 u22 u23 I

Z33/ V 0 0 W33/

detTl = det LU

det>l = detL x detí/

Isolando det U, ficamos com:

det 4

detL = det U

det.4

det U =

detl

Como L é uma matriz triangular inferior, deu determinante é o produto dos elementos da diagonal principal.
det L — Zn X ^22 ^33

=1x1x1

= 1

A é uma matriz 3x3 conhecida. Para obter o seu determinante, podemos utilizar a regra de Sarrus.

Logo:

Parte Negativa Parte Positiva det 4 = [5.1.3 + 2.4.1 + 1.3.1] - [1.1.1 + 5.4.1 + 2.3.3]
= [15+ 8 +3]-[1 + 20 +18]

= 26-39

= -13

det .4

Gabarito: Letra A.

det U =

detl

Fila nula

Uma matriz que apresenta uma fila (linha ou coluna) cujos elementos são todos zero apresenta determinante zero. Exemplos:
3 ol = 0

1 4 -3

0 0 0 0

5 VTT 7T

3 2 0 1

-1 2

5 -1

0 8 = 0

2 4 0 3

Filas paralelas iguais

Uma matriz com filas paralelas iguais (linhas ou colunas) apresenta determinante zero. Exemplos:

1 li

3 3l 0

4 4 4

4 4 4

5 VTT7T

1 2 1

1 2 1

1 -1 1

1 4 1

= 0

8 — 0u

Filas paralelas proporcionais

Uma matriz com filas paralelas proporcionais (linhas ou colunas) apresenta determinante zero.
Exemplos:

1 3

3 9

0,5

= 0, pois a segunda coluna é 3 vezes a primeira coluna.

1,5 =0, pois a primeira linha é o dobro da segunda linha.

4 2

1 2

2 -1

3 4

20 1

5 8

10 6

15 3

= 0, pois a terceira coluna é 5 vezes a primeira coluna.

Troca de filas paralelas

Ao trocarmos uma fila (linha ou coluna) de lugar com outra fila paralela, o determinante muda de sinal,
3 2 3 3 3 2

-1 2 3 = 20 -1 3 2

5 -1 1 5 1 -1

Professor, e se trocarmos as filas de novo?

Nesse caso, o sinal muda novamente!

J 4 2 7

r i 2 5

l 2 -1 1

H 3 4 4

3 4

2 -1

1 2

4 2

4 3

1 6 = 271

5 1

7 1

a b c

(MPE SC/2022) Considere as matrizes A = d e f lg h kl eB =
2a c 3b
2d f 3e
2g k 3h

Sendo det(Al e det(B) os determinantes das matrizes Ae B, respectivamente, tem-se que:

a) detQ4) = 6 x detÇB);

b) det(A) = -6 x det(B\,

c) det(B) = 6 x det(A);

d) det(B) = —6 x det(A\,
e) detQ4) = det(B).
Comentários:

Sabemos que, ao multiplicar uma fila (linha ou coluna) de uma matriz por uma constante k, o determinante dessa nova matriz também fica multiplicado por k.
Uma consequência interessante dessa propriedade é realizar a operação inversa, removendo um fator comum de dentro do determinante.
Veja que:

det(B) =

2a c 3b

2d f 3e zg k 3h a c 3b det(fí) = 2 x d f 3e
9 k 3h a c b det(B) = 2 x 3 x d f e g k h a c b det(B) = 6 x a c b d f e g k h
X

Note que x = d f e g k h estão trocadas.
é muito parecido com det(X). A diferença é que a segunda e a terceira coluna

Sabemos que ao trocarmos uma fila muda de sinal. Logo:
(linha ou coluna) de lugar com outra fila paralela, o determinante

Portanto:

a c b d f e = x g & &
a b c d e f g h k det(4)
= — X

detQ4) = —x x = — detQ4)
Consequentemente, temos que det(B) é dado por:

a c b det(fí) = 6 x d f e g k h
X

det(B) = —6 x det (71)

Gabarito: Letra D.

Combinação linear de filas

Primeiramente, vamos entender o que é uma combinação linear.

Podemos dizer a primeira linha de uma matriz, por exemplo, é combinação linear de outras linhas L₂,
L₃

e L₄ quando existem valores reais a, b e c tais que:

Li = aL2 + bL3 + CL4

Exemplo: considere a matriz A abaixo:

2 1

7 5

13 8

Note que a terceira linha L₃ = [6 13 8] é uma combinação linear da primeira linha = [1
2 1] e da segunda linha L2 = [3 5 7], pois L3 = 3Lr + L2.
Vejamos:

3L4 + L2

= 3[1 2 1] + [3 7 5]

= [3 6 3] + [3 7 5]

= [6 13 8]

= L3

Também podemos ter combinações lineares com colunas. Considere a seguinte matriz B:

' 4 2 7 11

B = 1 2 5 9

2 1 1 3

Note que a quarta coluna C₄ =

. 3 4 4 12.

9 é combinação linear da segunda coluna C

3 2

2 e da terceira coluna

5 pois C

1 ' 4

= 2C2

+ C3.

Vejamos:

2C2 + C3

-4-

-7-

-8-

-4-

Entendida a ideia de combinação linear entre linhas e entre colunas, devemos saber que quando uma matriz apresenta uma fila (linha ou coluna) que é combinação linear de outras filas, o seu determinante é zero.
Nos exemplos em questão, a matriz A e a matriz B apresentam determinantes nulos.

' 5

(TJ PR/2009) Calcule 0 determinante de A = -1

-1 -2 1

2 -3 1

-4 —6 3

a) 11

b) -11

c) 0

d) 5

Comentários:

. 1 3 4 -2.

E aí, concurseiro? Vai aplicar 0 Teorema de Laplace nesse determinante 4x4? Negativo!
Note que a linha 1 é a soma da linha 3 com a linha 4, isto é, L± = L3 + L4.

5-1-2 1

L 1 3 4 —2j

Como temos uma linha que é combinação linear de outras duas, 0 determinante é zero.

Gabarito: Letra C

Teorema de Jacobi

O Teorema de Jacobi é uma ferramenta poderosíssima. Isso porque esse teorema nos permite manipular os determinantes de modo a aplicar as propriedades vistas até então.
Esse teorema nos diz que ao multiplicar uma fila por qualquer número e somar esse resultado a uma outra fila paralela qualquer, o valor do determinante não se altera.
Em outras palavras, podemos trocar uma fila qualquer por uma combinação linear que contenha a fila original.
Vejamos um exemplo:

1 2 1 2

Calcule o determinante da matriz A = 4

8 1 3

7 1 2

1 2 1 3

Note que temos um determinante de ordem 4. Poderíamos aplicar o Teorema de Laplace diretamente para resolver o problema, porém note que seria bastante trabalhosa a resolução, visto que não temos uma fileira com três zeros.
Para resolver o determinante, vamos fazer "surgir alguns zeros" com o Teorema de Jacobi. Lembre-se que ao multiplicar uma fila por qualquer número e somar esse resultado a uma outra fila paralela qualquer, o valor do determinante não se altera.
Primeiramente, vamos multiplicar a primeira coluna (Cx) por (—2) e somar à segunda coluna (C₂).
Em outras palavras, vamos substituir C2 por C2 + Ç-2)C1.

Para facilitar a comunicação, vamos descrever essa substituição assim: C₂ <- C₂ — 2Cr.

X(-2)

n

1 2 1 2 1 0 1 2

4 8 1 3 C2<-C2-2C1 4 0 1 3

3 7 1 2 3 1 1 2

1 2 1 3 1 0 1 3

Note também que podemos substituir C₄ por C₄ + (-2)C₃, isto é, podemos realizar a operação
C4 <— C4 — 3C3.

X(-2)

ÍX

1 0 1 2 1 0 1 0

4 0 1 3 C4—2C3 4 0 1 1

3 1 1 2 3 1 1 0

1 0 1 3 1 0 1 1

Observe que 0 determinante da matriz original corresponde a

1 0 10

4 0 11

3 110

1 0 11

Note que agora podemos aplicar o Teorema de Laplace com mais facilidade. Ao selecionar a segunda coluna, temos que o determinante é dado por:
detX = 0 x 412 + 0 x 422 + 1 x 432 + 0 x 442

= 1 x 432

= (-1)3+2D32

1 ( ) 1 0

(-1)5 4 ( 1 1 1

1 ( > 1 1

4 11

Vamos aplicar a regra de Sarrus no determinante.

Parte Negativa Parte Positiva

D₃₂ = [1.1.1 + 1.1.1 + 0.4.1] - [0.1.1 + 1.1.1 + 1.4.1]

O32 = 2 - 5

D32 — "3

1 1

Note que det4 = — 4 1

1 1

1 . Portanto:

detX = -(-3)

det4 = 3

Regra de Chió

A Regra de Chió é uma regra que permite com que um determinante tenha a sua ordem reduzida. Trata-se de uma aplicação do Teorema de Jacobi.
Vamos ver a aplicação da regra na prática. Considere o determinante abaixo:

3 2 12

4 8 13

3 7 12

12 2 3

O primeiro passo e fazer com que o elemento arí seja igual a 1. Realizando a operação Cx — 2C3,temos:

X(-2)

3 2 1 2

4 8 1 3

3 7 1 2

1 2 2 3

Cl<-Ci-2C₃

1 2 1 2

2 8 1 3

1 7 1 2

-3 2 2 3

A partir desse momento, devemos zerar todos os elementos da primeira linha, à exceção do elemento allz fazendo uso da primeira coluna.
Para tanto, vamos realizar as seguintes substituições, nessa ordem:

* C₂ <- C₂ — 2C^;

* <- C3 — Clz' e

* <— C₄ — 2CX.

1 0 1 0 1 0 1 2 1 0 0
2 1 0 0 0

4 0 1 1 C2*— C2 —2C\ 2 4 1 3 C3<-C3-Ci 2 4 -1
3 C4<—C4—2C\ 2 4 -1 -1

3 1 1 0 1 5 1 2 1 5 0
2 1 5 0 0

1 0 1 1 -3 8 2 3 -3 8 5
3 -3 8 5 9

Ficamos com:

1 0 0 0

2 4 -1 -1

1 5 0 0

-3 8 5 9

Ao aplicar o Teorema de Laplace na primeira linha, temos:

det?l — @11^11 + ^12^12 "1" ^13^13 "1" ^14^14

Como na Regra de Chió temos o sempre o elemento axl = 1 e os demais elementos da primeira linha iguais a zero, ficamos com det>l = Dri\
det.4 = 1^4 ii + 0í412 + 0X13 + OX14

detzl = Atl detX = (—l)1+1Dn deti4 =
detd =

4 -1 -1

5 0 0

8 5 9

Veja, portanto, que a Regra de Chió reduziu a ordem do seguinte determinante:
determinante de 4 para 3, pois tínhamos 0

3 2 1 2

4 8 1 3

3 7 1 2

1 2 2 3

Esse determinante foi reduzido a:

4 -1 -1

5 0 0

8 5 9

Poderíamos continuar utilizando a Regra de Chió para reduzir a ordem do determinante de 3 para 2.Porém, como já temos um determinante de ordem 3, podemos aplicar a regra de Sarrus.

Parte Negativa Parte Positiva

[4.0.9 + (-1). 0.8 + (-1). 5. 5] - [(-1). 0.8 + 4. 0. 5 + (-1). 5.9]

= [0 + 0 - 25J - [0 + 0 - 45]

= -25 + 45

= 20

Em resumo, a Regra de Chió consiste nos seguintes passos:

* Fazer com que o elemento atl seja igual a 1;

* Zerar todos os elementos da primeira linha, à exceção de au, fazendo uso da primeira coluna;

* Feita a operação anterior, o determinante em questão é igual ao menor complementar D₁X;

* Repita o processo, se necessário, para reduzir a ordem do determinante mais uma vez.

Nesse momento, vamos resolver uma questão que já fizemos por Teorema de Laplace, dessa vez por meio da Regra de Chió.
(SEFAZ-RS/2014) O determinante da matriz

A

a) —32

b) -26

c) 14

d) 16

e) 28

Comentários:

1 2 1 0

2 3 1 0 é

2 -3 2 1

2 1 1 4

Temos um determinante de ordem 4. Dessa vez, vamos utilizar a Regra de Chió.

Fazer com que o elemento a, , seja igual a 1

Note que o elemento atl já é igual a 1.

Zerar todos os elementos da primeira linha, à exceção de a!i, fazendo uso da primeira coluna

Para tanto, vamos realizar as seguintes substituições, nessa ordem:
C2 C*2 — 2Q; e

C3 C3 Q-

1 2 1 0

2 3 1 0

2 -3 2 1

2 1 1 4

C2*~ ^2~ 2Ci

1 0 1 0

2 -1 1 0

2 -7 2 1

2 -3 1 4

C3<-C3-Ci

1 0 0 0

2 -1 -1 0

2 -7 0 1

2 -3 -1 4

Observe que o determinante ficou reduzido a:

1 0 0 0

2 -1 -1 0

2 -7 0 1

2 -3 -1 4

Feita a operação anterior, o determinante em questão é igual ao menor complementar Dn detX =
detzl =

«------ 9—9

-1 -1 0

-7 0 1

-3 -1 4

-1 -1 0

-7 0 1

-3 -1 4

deM = [(-1). 0.4 + (-1). 1. (-3) + 0. (-7). (-1)] - [0. 0. (-3) + (-1). 1. (-1) + (-1). (-7). 4]

detÂ = [0 + 3 + 0] - [0 + 1 + 28]

det4 = 3-29

detTl = -26

O determinante da matriz A, portanto, é igual a -26.

Gabarito: Letra B.

Matriz inversa

No tópico de matrizes, definimos que a inversa de uma matriz A é aquela matriz que, quando multiplicada pela matriz A, tem como resultado a matriz identidade:
A A-1 = A-1 A = ln

Agora que sabemos como calcular determinantes, você precisa saber que uma matriz A é inversível (ou invertível) quando o determinante é diferente de zero, isto é:
A é inversível <-> det A #= 0

Vimos também que uma matriz que não é inversível é denominada singular. Nesse caso:

A é singular <-> det A = 0

Para uma matriz 2x2, temos uma fórmula para encontrar a matriz inversa. Considerando uma matriz
= lc 1' e'a adm'te inversa quando det A í Oe sua inversa é:

det A L—c a J

—xíd ad — bc !—c
Vamos resolver dois exercícios sobre matriz inversa:

'2

(SEDF/2017) Considerando a matriz A = 4

.0

0 10'

10 20 , julgue o próximo item.
2 40.

A matriz A é inversível.

Comentários:

Vamos calcular o determinante de A. Se o valor for diferente de zero, então a matriz é inversível.
Aplicando a regra de Sarrus, temos:

Parte Negativa Parte Positiva det A = [2.10.40 + 0. 20.0 + 10.4.2] - [10.10. 0 + 2. 20.2 + 0.4.40]
detA = [800 + 0 + 80] - [0 + 80 + 0]

detA = 880 - 80

det4 = 800

Como o determinante é diferente de zero, trata-se de uma matriz inversível.

Gabarito: CERTO.

(MPE SP/2019) A inversa da matriz é:
0,5 0,2

a) . 1 0,33

b) r 3 -5]

--1 2 J

3 5

ᶜ'l -1 2-

d) r 3 -n

[-5 21

r0,33 0,2

e) . 1 0,5

Comentários:

Resolvermos essa questão no capítulo sobre matrizes. Dessa vez, vamos utilizar a fórmula apresentada.Temos que a inversa de uma matriz A = j é dada por:

— xíd ~b]
detX L—c a J

A matriz em questão é B =

A inversa de B é:

*J ,J e seu determinante é:

detfí = [2 x 3] - [5 x 1] = 1

Gabarito: Letra B.

Para finalizar a parte teórica de determinantes, vamos resolver uma questão que envolve diversas propriedades aprendidas.
(Pref. Gov. Celso Ramos/2017) Considere as proposições:

-2

-2

I) 0

1/2

-7

H) 0

7 13

1 5

0 2_1

0 0

n 13

5 6

0 0

-21

= -3

= 0

21 -8

-4 -3

2 -3

III) A matriz A =

\1O

-3

-11

-2

-7 '6)/

é singular, isto é, não possui inversa.

IV) O conjunto solução da igual a —2.
x 1 -2

equação 3 2 -1

4 1 x

+ -2 2

1 4

= 0 possui dois elementos cujo produto é

Está(ão) CORRETA(S) a(s) proposição(ões):

a)Apenas as alternativas I e II estão corretas.

b)Apenas II e IV.

c)Apenas a alternativa II está correta.

d) Apenas I, III e IV.

e)Apenas II, III e IV.
Comentários:

Vamos analisar cada proposição individualmente.

I) ERRADA.

Veja que o determinante apresentado de assemelha muito a uma matriz triangular superior, exceto pelo elemento a₂₁ = —2:
-2 7 13 -21

-2 15 8

0 0 2'1 11

0 0 0 3

Para resolver transformar esse determinante em um determinante de matriz triangular,
podemos aplicar o

Teorema de Jacobi realizando a substituição L2 <- L2 — Lr.

-2 7 13 -21 -2 7 13 -21

-2 1 5 8 ^2*"^2 —^1 0 -6 -8 29

0 0 2-1 11 0 0 2-1 11

0 0 0 3 0 0 0 3

O determinante resultante corresponde ao determinante de uma matriz triangular superior.

Logo, o item está errado, pois o determinante em questão é 18.

II) CERTO.

Trata-se de um determinante que apresenta uma fila nula. Portanto, o determinante é nulo.

1/2 n 13 25

-7 5 6 3

0 0 0 0

21 -8 -4 -3

III) CERTO.

Para a matriz em questão ser singular, o determinante deve ser zero.

Note que temos uma fila é combinação linear de outras duas, pois L3 =
(—2)£1 + L2. Portanto, o determinante de 4 é nulo e, consequentemente, trata-se de uma matriz singular.
IV) CERTO.

Parte Negativa Parte Positiva

= [x.2.x + l.(-l).4 + (-2).3.1] - [(—2).2.4 + x. (—1). 1 + 1.3.x]

= [2x2 - 4 - 6] - [-16 - x + 3x]

= [2x2 - 10] - [2x - 16]

= 2x2 — 2x + 6

Agora vamos calcular o determinante .

1-2 2| 4:

I 1 4l l"? 2| = [(-2) x 4] - [2 x 1] =-10
Portanto, a equação requerida é:

x

(2x2 - 2x + 6) + (-10) = 0
2x2 — 2x - 4 = 0

Da teoria de equações do segundo grau, sabemos que o produto das raízes é Logo:

c —4

x x x = - = = —2

2 a 2

O item, portanto, está correto.

Por fim, temos que apenas os itens II, III e IV estão certos.
Gabarito: Letra E.

QUESTõES CoMENTADAS - CEBRASPE

Matrizes

'I

Texto para as próximas questões

Um importante algoritmo para a resolução de problemas que envolvem matrizes
(por exemplo, resolução de sistemas lineares, cálculo da matriz inversa, determinantes etc.)consiste em efetuar operações elementares sobre as linhas da matriz. Essas operações incluem multiplicação de uma linha da matriz por um número não nulo; adição a uma linha de um múltiplo de outra linha; permutação de linhas. Com relação a essas operações, considere a matriz B obtida da matriz A =
1 0

2 -1

2 -1

-2\

—2 depois de efetuada a seguinte

-1/

sequência de operações elementares: substituição da linha 3 pela linha 3 menos a linha
2; substituição da linha 2 pela linha 2 menos duas vezes a linha 1. Com base nessas informações, julgue o item que se segue,acerca da matriz B.

Item. 1. (CESPE/CBM DF/2011) Na linha 3 da matriz B, há apenas um elemento nulo.

Item. 2. (CESPE/CBM DF/2011) A soma dos elementos da linha 2 da matriz B é igual a 1.

Comentários:

Vamos obter a matriz B por meio das operações propostas. Primeiramente, temos:

* Substituição da linha 3 pela linha 3 menos a linha 2.

-1

-l-(-l) -1 - (-2)7

* Substituição da linha 2 pela linha 2 menos duas vezes a linha 1.

í 1 0 -2

B = 2 - 2 x (1) -1 - 2 x (0) -2 - 2 x (-2)

\ 0 0 1

Questão 01

Veja que na linha 3 da matriz B há dois elementos nulos. O gabarito, portanto, é ERRADO.

Questão 02

A soma dos elementos da linha 2 da matriz B é:

O gabarito, portanto, é CERTO.
Gabarito: 01 - ERRADO. 02 - CERTO.

0 + (-1) + 2 = 1

Item. 3. (CESPE/PC-DF/2013) Considere que a empresa X tenha disponibilizado um aparelho celular a um empregado que viajou em missão de 30 dias corridos. O custo do minuto de cada ligação, para qualquer telefone, é de R$ 0,15. Nessa situação, considerando que a empresa tenha estabelecido limite de R$200,00
e que, após ultrapassado esse limite, o empregado arcará com as despesas, julgue o item a seguir.

Considere que, em uma nova missão, o preço das ligações tenha passado a depender da localidade,
mesma cidade ou cidade distinta da de origem da ligação, e do tipo de telefone para o qual a ligação tenha sido feita, celular, fixo ou rádio. As tabelas abaixo mostram quantas ligações de cada tipo foram feitas e o valor de cada uma:
celular fixo rádio mesma cidade 6 3 1
cidade distinta 7 1 3

Tabela I: número de ligações realizadas por tipo de telefone mesma cidade cidade distinta celular
0.20

0,50

fixo

0,15

0,30

rádio

0.20

0.20

Tabela II: preço de cada ligação, em reais

Nessas condições, se A = [7 1 3],or a matriz formada pelos dados da tabela 'B =

0,20

0,15

0,20

0,50

0,30

0,20

for a matriz formada pelos dados da tabela II, então a soma de todas as entradas da matriz A x B
será igual ao valor total das ligações efetuadas.
Comentários:

O preço total a ser pago seria dado pelo seguinte:

Mesma cidade: 6 x 0,20 + 3 x 0,15 + 1 x 0,20 = 1,85

Cidades diferentes: 7 x 0,5 + 1 x 0,30 + 3 x 0,20 = 4,40

Total: 1,85 + 4,40 = /?$ 6,85

Porém, na multiplicação de matrizes, vamos ter o seguinte resultado:

r O 1 i 0,20 0,50'

r

L7/ 1 1

37-X1

0,15 0,30

.0,20 0,20.

6 x 0,20 + 3 x 0,15 + 1 x 0,20

Item. .7 x 0,20 + 1 x 0,15 + 3 x 0,20

6 x 0,5 + 3 x 0,30 + 1 x 0,20

7 x 0,5 + 1 x 0,30 + 3 x 0,20.

1,85 4,10

.2,15 4,40.

Vemos que apenas a diagonal principal possui valores condizentes com o anterior,
enquanto a diagonal secundária corresponde a cobranças cruzadas, isto é, cobrar o preço de ligações de mesma cidade para ligações em cidades diferentes, e vice e versa.
Assim, o valor total das ligações efetuadas será o traço da matriz, isto é, a soma dos elementos da diagonal principal. Não se trata da soma de todos os elementos da matriz.
Gabarito: ERRADO.

Item. 4. (CESPE/SEDF/2017) Considerando a matriz A =

2 0

4 10

0 2

20 , julgue o próximo item.

Se C = [Cí;], 1 < i, j <3, tal que C = A2 , então C23 - C22 > 500.
Comentários:

Temos que:

C = 42

= AxA

'2 0 10' '2 0 10'

4 10 20 X 4 10 20

Item. .0 2 40. .0 2 40.

A questão pergunta pela subtração de dois elementos da matriz C: C₂₃ — C₂₂. Note que não precisamos obter a matriz inteira. Lembre-se que:
0 elemento da linha i e da coluna j da matriz-produto C é obtido por meio da linha i da primeira matriz e da coluna j da segunda matriz.
Para obter o elemento ^22/ faremos uso da segunda linha da segunda matriz.
primeira matriz e da segunda coluna da

'2 0 10'

4 10 20 X

Item. .0 2 40.

'2 0 10'

4 10 20

Item. .0 2 40.

C22 = 4 x 0 + 10 x 10 + 20 x 2 = 140

Para obter o elemento C₂₃, faremos uso da segunda linha da primeira matriz e da terceira coluna da segunda matriz.
'2 0 10'

4 10 20 X

Item. .0 2 40.

'2 0 10

4 10 20

Item. .0 2 40.

C23 = 4 x 10 + 10 x 20 + 20 x 40 = 1.040

Portanto, C23 — C22 = 1040 — 140 = 900. Trata-se de um número maior do que 500.
Gabarito: CERTO.

Item. 5. (CESPE/IBAMA/2013) Julgue o item subsequente, relacionado a problemas aritméticos,
geométricos e matriciais.
Considere que A e B sejam matrizes distintas, de ordem 2x2, com entradas reais e, em cada matriz, três das quatro entradas sejam iguais a zero. Além disso,considere também que
AxA=BxB=AxB = O, em que O é a matriz nula, isto é, a matriz em que todas as entradas são iguais a zero. Nesse caso, necessariamente, A = O ou B = O.
Comentários:

Temos duas matrizes A e B de ordem 2 em que ao menos três dos quatro elementos
(entradas) é igual a zero. Além disso, 0 é a matriz nula (de ordem 2).
Em resumo, a questão pergunta o seguinte:

íAA = 0

Se IBB = 0, então necessariamente A ou B é a matriz nula?

{AB = 0

Pessoal, para responder a essa pergunta, devemos utilizar um contraexemplo.

Considere Â = [° J] e B = [°

AA = í°

Io lI I=r0l.0 + 1.0 0.1 + 1. 01l-í° 01

Lo oJHLo oJ

Lo. o + o.o 0.1+ 0.0-1

I lo 0-I

BB = í° 21 í° 2l lo oJ lo oJ
ro. 0 + 2.0 0.2 + 2.01l-í° °1

Lo. o + o.o 0.2 + 0.0-1 I lo o-l r0.0 + 1.0 0.2 + l.Ol lo oJ lo oJI -1Lo. o + o.o 0.2 + 0.0-1 I lo O-l
Note que encontramos duas matrizes A e B que desmentem a afirmação do enunciado,
pois temos

AA = BB = AB = O com A e B diferentes da matriz nula. O gabarito, portanto, é ERRADO.
Gabarito: ERRADO.

QUESTõES CoMENTADAS - CEBRASPE

Determinantes l.(CESPE/IFF/2018) Considere que k seja um número real e que o determinante da matriz B =
igual a 27. Nesse caso, se A =

r3 — li j então o determinante da matriz B — A, será igual a:
a) 30.

b)0.

c) 3.

d) 6.

e) 10.

Comentários:

O determinante de B é dado pelo produto dos termos da diagonal principal menos o produto dos termos da diagonal secundária:
detB = I³ ᵏˡ

Logo, a matriz B é dada por:

A matriz B — A é:

27 = [3 x 9] - [k x 3]

27 = 27 - 3k k = 0
;[3 01 r3 -11

L3 9J 1-9 6 j

-3 0 — (—1)1

-9 9-6 1

0 1

L-6 3J

Novamente, para calcular det(B - >1), devemos realizar produto dos termos da diagonal principal e subtrair0 produto dos termos da diagonal secundária:

Gabarito: Letra D.

det(B-^) = |_°₆ 1|

det(B - 4) = [0 x 3] - [1 x (-6)]

det(B - 21) = 0 - (-6)
det(B - X) = 6

2.(CESPE/SEDUC AL/2018) Julgue o item que se seguem, relativos a matrizes e sistemas lineares.

Se a é um número real e se o determinante da matriz P =

então a = - 2 ou a = 1.

for igual a zero,

Comentários:

A matriz P é dada por:

la 1 1 [ 2x0 2 x (-1)

lo a-li + [2 x (-1) 2x1 .

rcz + 0

lo - 2

1-2

d — 1 + 2

ti + 1

Temos que:

detP = 0

[ax(a + l)]-[(-l)x(-2)] = 0

a2 + a — 2 = 0

Note que as raízes dessa equação do segundo grau em a são de fato —2 e 1, pois:

(—2)2 + (-2) -2 = 0

l2 + 1 - 2 = 0

Logo, se detP = 0, devemos ter a = -2 ou a = 1.
Gabarito: CERTO.

3.(CESPE/ABIN/2010) Considerando a matriz A = I 2
julgue o item a seguir.

O determinante de A é igual a - 1.

A 2

\3 4

e os vetores X = %

\x

Comentários:

Aplicando a regra de Sarrus no determinante de A, temos:

detX = [1.0.5 + 2.2.3 + 2.2.4] - [2.0.3 + 1.2.4 + 2.2.5]

= [0 + 12 + 16] - [0 + 8 + 20]

= 28-28

= 0

Gabarito: ERRADO.

2 0

Item. 4. (CESPE/SEDF/2017) Considerando a matriz >1=4 10

0 2

20 , julgue o próximo item.

Se B = então o determinante de B é maior que 200.
Comentários:

Pessoal, para resolver esse problema, podemos obter a matriz B e calcular o seu determinante diretamente pela regra de Sarrus.
Ocorre que, na prova que cobrou essa questão, houve a necessidade de calcular o determinante de A. Então,para responder ao item, vamos obter det(X) e em seguida obteremos o det(B) a partir de det(+l).

Aplicando a regra de Sarrus no determinante de A, temos:

Parte Negativa Parte Positiva detzl = [2.10.40 + 0. 20.0 + 10.4.2] - [10.10. 0 + 2. 20.2 + 0.4.40]
detTl = [800 + 0 + 80] - [0 + 80 + 0]

detX = 880 - 80

detzl = 800

Sabemos que, ao multiplicar uma matriz de ordem n por uma constante k, o determinante dessa nova matriz fica multiplicado por kn.
det(L4) = kn det4

Logo:

detfí = det^->l^

Portanto, o determinante de B é menor do que 200.

Gabarito: ERRADO.

= - x 800
O

= 100

1 1

5.(CESPE/SEDUC CE/2013/Adaptada) Considerando a matriz A = 1 0

1 0

a:

a) -16

b) 0.

c) 16.

d) 20.

e) 81.

Comentários:

Temos que:

det(X4) = det(4 xAxAxA)

Pelo Teorema de Binet, temos:

0 , o determinante de A4 é igual
2.

detQ44) = (det yl) x (det/l) x (detX) x (det.4)
detQ44) = (det X)4

Portanto, para obter o determinante de A4, precisamos obter o determiante de A e elevar à quarta potência.Aplicando a regra de Sarrus no determinante de A, temos:

Parte Negativa Parte Positiva detX = [1.0. 2 + 1.0.1 + 0.1. 0] - [0. 0.1 + 1. 0. 0 + 1.1.2]
= [0 + 0 + 0] - [0 + 0 + 2]

= -2

Logo:

detQ44) = (det/l)4

= (-2)4

= 16

Gabarito: Letra C.

Item. 6. (CESPE/MS/2008) Se uma matriz quadrada A = ((/,-/) tem dimensão 3 x 3 e é tal que (ai;) = 1,
se i < j e (a.y) = i — j, se i > j, então o determinante de A é um número estritamente positivo.Comentários:

Temos uma matriz quadrada A de ordem 3:

Temos que:

'all a12 a13~

a21 a22 a23

.a31 a32 a33.

f 1 ;se i <j ttlJ ~ (i — j; se i > j
Portanto, se o número da coluna j for maior ou igual do que o número da linha i,
o elemento é 1. Caso contrário, o elemento éi — j. Nesse caso, a matriz A é:
1 1'

1 1

3-2 1.

1 1]

1 1

1 1J

Note que a matriz A apresenta duas fileiras iguais (linhas 1 e 2, assim como colunas
2 e 3). Portanto, o seu determinante é zero.
Logo, é errado afirmar que o determinante de A é estritamente positivo.

Gabarito: ERRADO.

Texto para as próximas questões

2 -1 5 3 0 0' 1 0 0'

Considerando as matrizes A = 10 4 = 3 0 0 eC = 0 10
, julgue os itens a seguir.

Item. .2 2 0. .3 0 0. .0 0 5.

Item. 7. (CESPE/SEDU-ES/2012) Como [det B]2 = det B, então det B = 1.

Item. 8. (CESPE/SEDU-ES/2012) É correto afirmar que det[.A x B x C] = detB

Item. 9. (CESPE/SEDU-ES/2012) detTl2 = 196.

Comentários:

Questão 07

Lembre-se que se uma fila (linha ou coluna) de uma matriz é formada apenas por zeros, seu determinante é nulo. Isso significa que detB = 0 e (detfí)2 = O2 = 0.
O gabarito, portanto, é ERRADO.

Questão 08

Aplicando o teorema de Binet, temos:

det[zl x B x C] = det>l x detfí x detC

Como detF = 0, ficamos com:

det[>l x B x C] = det.4 x 0 x det C

det[zl x B x C] = 0

Logo, o gabarito da questão é CERTO, pois det[4 x B x C] = detB = 0.

Questão 09

Temos que det>l2 = det(71 x >1). Pelo teorema de Binet:

det(X x 4) = detd x detX

= (detX)2

Note, portanto, que detX2 = (det/l)2.

Vamos calcular o determinante de A. Pela regra de Sarrus:

Parte Negativa Parte Positiva det?l = [2. 0. 0 + (-1). 4. 2 + 5.1. 2] - [5. 0.2 + 2.4.2 + (-1). 1. 0]
det4 = [0 - 8 + 10] - [0 + 16 + 0]

deti4 = —14

Logo:

O gabarito, portanto, é CERTO.

det/l2 = (det.4)2

= (-14)2 = 196

Gabarito: 07 - ERRADO. 08 - CERTO. 09 - CERTO.

Item. 10. (CESPE/PETROBRAS/2008) Se A é uma matriz quadrada invertível, então a) det[/l x Xt] = [detd]2, em que A1 é a matriz transposta da matriz A.
b) det [TI + 4] = 2 x detd.

c) det4 + dety4t = 0.

d) det [4 + 4_1] = 0.

e) detX = det.4-1.

Comentários:

Vamos comentar cada alternativa.

a) det [d x d*] = [detd]2, em que A1 é a matriz transposta da matriz A. CORRETO.

Pelo teorema de Binet, temos que:

det(d x >19 = detd x detd*

Note que 0 determinante da matriz transposta de A é igual ao determinante de A, isto é, detd = detd*.Logo:

det(d x dr) = det d x det d

= (detd)2

b) det [d + d] = 2 x detd. ERRADO.

Sabemos que, ao multiplicar uma matriz de ordem n por uma constante k, 0 determinante dessa nova matriz fica multiplicado por kn.
det(fcd) = kn detd

Se a matriz A tiver ordem n, temos que:

det[d + d] = det 2d

= 2n detd c) detd + detd* = 0. ERRADO.
Note que 0 determinante da matriz transposta de A é igual ao determinante de A, isto é, detd = detd*.Logo:

detd + detdr = detd + detd

= 2 detd d) det [d + d1] = 0. ERRADO.
Essa propriedade que envolve a soma de uma matriz A com a sua inversa não existe.
Para tanto, podemos apresentar um contraexemplo.
Suponha d = I₂, ou seja, que A é uma matriz identidade de ordem 2.

A inversa da matriz identidade é a própria matriz identidade, isto é, d 1 = I₂. Nesse caso:

d + d"1 = 2I2

O determinante de d + d 1 é, portanto:

det(d + d = det2/n

= 22 det/n

= 22 x 1

= 4

e)deti4 = det d1. ERRADO.

O determinante da inversa de A é o inverso do determinante de A, isto é:

Gabarito: Letra A.

detd 1 =

det d

Item. 11. (CESPE/PETROBRAS/2008) Considere que A = (a seja uma matriz invertível,
B = A 1 seja a vc a'
inversa de A e C = (

tem-se que a) det d = detB.
b) det C = 2 x det A

c) det [X x B] = 1.

vc + 2a a + 2a)

\ Nesse caso, é correto afirmar que, para toda matriz A, invertível,

d) det [d + B] = 2 X det A

e) det [X x B_1] = 1.

Comentários:

Vamos comentar cada uma as alternativas.

a) det d = det B. ERRADO.

Como B é a inversa de A, a alternativa está afirmando que detd = detd \ Essa propriedade é falsa, pois o determinante da inversa de A é o inverso do determinante de A, isto é:
bjdetf = 2 x det A. ERRADO.

detd 1 =

detd

Não existe essa relação entre as matrizes A e C. Para provar que a alternativa é falsa, vamos mostrar um contraexemplo.
Considere que A é a matriz identidade, com a = d = leb = c = 0.

[a bl í1 °1

1-0 lJ

Nesse caso, a matriz C seria:

r a b i _ í 1 0 1 -í1 °1

te + 2a d + 2ai Lo+ 2.1 l + 2.lJ 1.2 3-1

Note que, para esse exemplo:

* detX = [1.1] - [0.0] = 1

* detC = [1.3] - [0.2] = 3

Portanto, é errado dizer que det C = 2 det A

c) det [4 x B] = 1. CERTO.

Como B é a inversa de A, a alternativa está afirmando que det(4 X-1) = 1. Essa relação é verdadeira, pois,pelo teorema de Binet:

det(44 = det A x det .4 1

= det A x -—-

det 4

= 1

d) det [4 + B] = 2 x det A. ERRADO.

Essa propriedade não existe. B é a inversa de A, de modo que não se pode afirmar que det(4 + X-1) = 2 det A

Para provar que a alternativa é falsa, vamos mostrar um contraexemplo.

Considere que A é a matriz identidade, com a = d = leb = c = 0.

Temos que:

det4 = [1.1] - [0.0]

det4 = 1

A inversa da matriz identidade é a própria matriz identidade, isto é, A 1 = I₂. Nesse caso:

4 + 4'1 = 2/2

O determinante de A + A~1 é, portanto:

det(4 + A-1) = det(27₂)

= 22 det/2

= 22 x 1

= 4

Logo, perceba que, para o contraexemplo apresentado, det(A + 4_1) 2 x det A

e) det [i4 x F_1] = 1. ERRADO.

Como B é a inversa de A, B_1 é a própria matriz A, pois:

B"1 = G4"1)-1 = A

Portanto, a alternativa afirma que det(4 x 4) = 1. Não se pode afirmar isso para qualquer matriz A. Pelo teorema de Binet, sabemos que:
det(4 x 4) = detzl x det 4
det(4 x X) = (det yl)2

Gabarito: Letra C.

Item. 12. (CESPE/IFF/2018) Considere que A, B e C sejam matrizes quadradas, de mesma dimensão e com entradas reais. Assinale a opção correta a respeito das propriedades dessas matrizes,assumindo que det (X) é o determinante da matriz X e X1 é a matriz transporta da matriz X.
a) Se a matriz A for antissimétrica, isto é, se AÈ = —A, então det(4) = 0.

b) Se A não for matriz nula e se AB = AC, então B = C.

c) Se (4 + B)2 = (B — A)2, então AB = —BA.

d) SeAB * BA, então det(AB) #= det(BA).

e) det(2A) = 2det(A).

Comentários:

Vamos analisar cada alternativa.

a) Se a matriz A for antissimétrica, isto é, se A1 = —A, então det(4) = 0. ERRADO.

Uma matriz é antissimétrica quando A1 = —A. Em outras palavras, uma matriz é antissimétrica quando a diagonal principal deve ser nula e os elementos simétricos com relação à diagonal principal são opostos.
Podemos verificar que a afirmação é falsa com um contraexemplo. Note que a matriz abaixo é antissimétrica e o determinante é diferente de zero:
detX = [0.0] - [(—1). 1]

= 0 - (-1)

= 1

b) Se A não for matriz nula e se AB = AC, então B = C. ERRADO.

Essa relação só é válida se A for uma matriz inversível. Isso porque, se a matriz for inversível, podemos multiplicar ambos os lados da equação AB = AC porX-1 pela esquerda:
A~1AB = A-1 AC
(A^A^B = (A^AIC
IB = IC

B = C

Vamos mostrar que a afirmação é falsa com um contraexemplo. Considere A =

Logo, temos um caso em que A não é a matriz nula, AB = AC e B é diferente de C.

c) Se (i4 + B)2 = (B - A)2, então AB = -BA. CERTO.

Vamos desenvolver a igualdade:

(4 + B)2 = (B — 4)2

(X + B)Q4 + B) = (B - 4)(B - 4)

A.A + AB+ BA + B.B = B.B-BA-AB+A.A

Simplificando os termos comuns, ficamos com:

AB + BA = -BA - AB
AB + AB = -BA - BA
2AB = -2BA

AB = -BA

d)SeAB * BA, então det(AB) #= det(BA). ERRADO.

Para mostrar que essa alternativa está errada, vamos mostrar um contraexemplo. Considere A =

Note que, para esse contraexemplo, AB BA e det(AB) = det(BA).

e) det(2A) = 2det(A). ERRADO.

Sabemos que, ao multiplicar uma matriz de ordem n por uma constante k, o determinante dessa nova matriz fica multiplicado por kn. Logo:
det(2A) = 2n detA

Gabarito: Letra C.

13.(CESPE/CBM DF/2011) Um importante algoritmo para a resolução de problemas que envolvem matrizes(por exemplo, resolução de sistemas lineares, cálculo da matriz inversa, determinantes etc.)
consiste em efetuar operações elementares sobre as linhas da matriz. Essas operações incluem multiplicação de uma linha da matriz por um número não nulo; adição a uma linha de um múltiplo de outra linha;permutação de linhas.
/I 0

2 _1

\2 -1

Com relação a essas operações, considere a matriz B obtida da matriz
-2\

—2 depois de efetuada a seguinte sequência de operações elementares: substituição da

-1/

linha 3 pela linha 3 menos a linha 2; substituição da linha 2 pela linha 2 menos duas vezes a linha
Item. 1. Com base nessas informações, julgue o item que se segue, acerca da matriz B.
O determinante da matriz A é igual ao determinante da matriz B.

Comentários:

A matriz B é obtida a partir da matriz A após as seguintes operações:

* Substituição da linha 3 pela linha 3 menos a linha 2, isto é, L₃ <- L₃ + (—l)i₂;

* Substituição da linha 2 pela linha 2 menos duas vezes a linha 1, isto é, L₂ L₂ + (-2)Ir

Note que essas duas alterações, pelo Teorema de Jacobi, não alteram o valor do determinante. Logo, os determinantes das matrizes Ae B são iguais.
Lembre-se que o Teorema de Jacobi nos diz que:

Ao multiplicar uma fila por qualquer número e somar esse resultado a uma outra fila paralela qualquer, o valor do determinante não se altera.
Gabarito: CERTO.

14.(CESPE/SEDUC AL/2018) Julgue o item que se seguem, relativos a matrizes e sistemas lineares.
Se P for uma matriz simétrica, então P será inversível.

Comentários:

Uma matriz é inversível quando o seu determinante é diferente de zero.

Não há correlação entre o fato de uma matriz ser simétrica com o fato de ela apresentar determinante diferente de zero.
Para mostrar que a afirmação está errada, pode-se usar como contraexemplo a matriz P =

Note que trata-se de uma matriz simétrica, pois = P = Veja, porém,
que detP = 0 e, portanto,
essa matriz não é inversível.

Gabarito: ERRADO

Item. 15. (CESPE/Pref. São Cristóvão/2019) Para a matriz A =

consequentemente, A é uma matriz inversível.
Comentários:

1 0 -1

1 1 1

0 0 1

1 0 0

1 , tem-se que detíA) = —1 e,

Temos um determinante de ordem 4. Para calculá-lo, vamos usar a regra de Chió.

Fazer com que o elemento seja igual a 1

Note que o elemento alt já é igual a 1.

Zerar todos os elementos da primeira linha, à exceção de allf fazendo uso da primeira coluna

Para tanto, vamos realizar as seguintes substituições, nessa ordem:

* <— C_> + C]

* C4 <— C4 — C4

1 0 -1 1

1 1 1 1

0 0 1 1

1 0 0 1

C3<-C3+Ci

1 0 0 1

1 1 2 1

0 0 1 1

1 0 1 1

C4«—C4 —

1 0 0 0

1 1 2 0

0 0 1 1

1 0 1 0

Observe que 0 determinante ficou reduzido a:

deti4 =

10 0 0

112 0

0 0 11

10 10

Feita a operação anterior, o determinante em questão é igual ao menor complementar deti4 =
deti4 =

detTl =

10 0 0

112 0

0 0 11

10 10

1 2

0 1

0 1

-.000

12 0

0 0 11

.010

Podemos agora calcular 0 determinante de A pela regra de Sarrus. Observe, porém, que é mais conveniente aplicar 0 Teorema de Laplace na primeira coluna, pois 0 determinante fica reduzido a DX1.
detd — cZii-dn -I- (721-^21 d- ^31^31

= 1^4n + O.X21 + 0.2l₃₁

= A±1

= Dn

:—2" -e

) 1 i

1 0

1 1

li ol

= [1.0]-[1.1]

= -1

Temos, portanto, que det/l = -1. Além disso, a matriz A é inversível, pois o seu determinante é diferente de zero.
Gabarito: CERTO.

LISTA DE QUESTõES - CEBRASPE

Matrizes

'I

Texto para as próximas questões

Um importante algoritmo para a resolução de problemas que envolvem matrizes
(por exemplo, resolução de sistemas lineares, cálculo da matriz inversa, determinantes etc.)consiste em efetuar operações elementares sobre as linhas da matriz. Essas operações incluem multiplicação de uma linha da matriz por um número não nulo; adição a uma linha de um múltiplo de outra linha; permutação de linhas. Com relação a essas operações, considere a matriz B obtida da matriz A =
0 -2\

-1 —2 depois de efetuada a seguinte

-1 -1/

sequência de operações elementares: substituição da linha 3 pela linha 3 menos a linha
2; substituição da linha 2 pela linha 2 menos duas vezes a linha 1. Com base nessas informações, julgue o item que se segue,acerca da matriz B.

Item. 1. (CESPE/CBM DF/2011) Na linha 3 da matriz B, há apenas um elemento nulo.

Item. 2. (CESPE/CBM DF/2011) A soma dos elementos da linha 2 da matriz B é igual a 1.

Item. 3. (CESPE/PC-DF/2013) Considere que a empresa X tenha disponibilizado um aparelho celular a um empregado que viajou em missão de 30 dias corridos. O custo do minuto de cada ligação, para qualquer telefone, é de R$ 0,15. Nessa situação, considerando que a empresa tenha estabelecido limite de R$200,00
e que, após ultrapassado esse limite, o empregado arcará com as despesas, julgue o item a seguir.

Considere que, em uma nova missão, o preço das ligações tenha passado a depender da localidade,
mesma cidade ou cidade distinta da de origem da ligação, e do tipo de telefone para o qual a ligação tenha sido feita, celular, fixo ou rádio. As tabelas abaixo mostram quantas ligações de cada tipo foram feitas e o valor de cada uma:
celular fixo rádio mesma cidade 6 3 1
cidade distinta 7 1 3

Tabela I: número de ligações realizadas por tipo de telefone mesma cidade cidade distinta celular
0.20

0.50

Oto

0.15

0.30

rádio

0.20

0,20

Tabela II: preço de cada ligação, em reais

Nessas condições, se A = [7 1 3],or a matriz formada pelos dados da tabela 'B =

0,20

0,15

0,20

0,50

0,30

0,20

for a matriz formada pelos dados da tabela II, então a soma de todas as entradas da matriz A x B
será igual ao valor total das ligações efetuadas.
2 0

Item. 4. (CESPE/SEDF/2017) Considerando a matriz >1=4 10

0 2

20 , julgue o próximo item.

Se C = [Cí;], 1 < i, j <3, tal que C = A2 , então C23

- £22 > 500.

Item. 5. (CESPE/IBAMA/2013) Julgue o item subsequente, relacionado a problemas aritméticos,
geométricos e matriciais.
Considere que A e B sejam matrizes distintas, de ordem 2x2, com entradas reais e, em cada matriz, três das quatro entradas sejam iguais a zero. Além disso,considere também que
AxA=BxB=AxB = O, em que O é a matriz nula, isto é, a matriz em que todas as entradas são iguais a zero. Nesse caso, necessariamente, A = O ou B = O.
GABARITo - CEBRASPE

Matrizes

Item. 1. ERRADO

Item. 2. CERTO

Item. 3. ERRADO

Item. 4. CERTO

Item. 5. ERRADO

LISTA DE QUESTõES - CEBRASPE

Determinantes l.(CESPE/IFF/2018) Considere que k seja um número real e que o determinante da matriz B =
igual a 27. Nesse caso, se A =

r3 — li j então o determinante da matriz B — A, será igual a:

a) 30.

b) 0.

c) 3.

d) 6.

e) 10.

2.(CESPE/SEDUC AL/2018) Julgue o item que se seguem, relativos a matrizes e sistemas lineares.

Se a é um número real e se o determinante da matriz P =

então a = - 2 ou a = 1.

a zero,

/I 2

3.(CESPE/ABIN/2010) Considerando a matriz A = I 2 0

\3 4

/X

e os vetores X = x

\x julgue o item a seguir.
O determinante de A é igual a - 1.

Item. 4. (CESPE/SEDF/2017) Considerando a matriz A =

2 0

4 10

0 2

20 , julgue o próximo item.

Se B = |J4, então o determinante de B é maior que 200.

5.(CESPE/SEDUC CE/2013/Adaptada) Considerando a matriz A =

a:

a) -16

b) 0.

c) 16.

d) 20.

e) 81.

1 1 0

1 0 0 , o determinante de 41 é igual

1 0 2

Item. 6. (CESPE/MS/2008) Se uma matriz quadrada A = (g.y) tem dimensão 3 x 3 e é tal que (ai;) = 1, se i < / e (ctí7) = i — j, se i > j, então o determinante de A é um número estritamente positivo.
Texto para as próximas questões

2 -1 5 3 0 0' 1 0 0'

Considerando as matrizes A = 10 4 = 3 0 0 eC = 0 10
, julgue os itens a seguir.

Item. .2 2 0. .3 0 0. .0 0 5.

Item. 7. (CESPE/SEDU-ES/2012) Como [det B]2 = det B, então det B = 1.

Item. 8. (CESPE/SEDU-ES/2012) É correto afirmar que det[.A x B x C] = det B
Item. 9. (CESPE/SEDU-ES/2012) det212 = 196.

10.(CESPE/PETROBRAS/2008) Se A é uma matriz quadrada invertível, então a) det[21 x Xt] = [det A]2, em que AL é a matriz transposta da matriz A.
b) det [21 + 4] = 2 x det A

c) det A + dety4t = 0.

d) det [21 + 2T1] = 0.

e) det 21 = det.4-1.

Item. 11. (CESPE/PETROBRAS/2008) Considere que A = (^ seja uma matriz invertível,
B = A 1 seja a inversa de A e C = ( \ Nesse caso, é correto afirmar que, para toda matrizA, invertível,

vc + 2a d + 2a)

tem-se que a) det 21 = detB.
b) det C = 2 x det2l.

c) det [X x B] = 1.

d) det [4 + B] = 2 x det A

e) det [X x B_1] = 1.

Item. 12. (CESPE/IFF/2018) Considere que A, B e C sejam matrizes quadradas, de mesma dimensão e com entradas reais. Assinale a opção correta a respeito das propriedades dessas matrizes,assumindo que det (X) é o determinante da matriz X e X1 é a matriz transporta da matriz X.
a) Se a matriz A for antissimétrica, isto é, se A[ = -A, então det(X) = 0.

b) Se A não for matriz nula e se AB = AC, então B = C.

c) Se (A + B)2 = (B — A)2, então AB = —BA.

d) SeAB * BA, então det(AB) #= det(BA).

e) det(2A) = 2det(A).

13.(CESPE/CBM DF/2011) Um importante algoritmo para a resolução de problemas que envolvem matrizes(por exemplo, resolução de sistemas lineares, cálculo da matriz inversa, determinantes etc.) consiste em efetuar operações elementares sobre as linhas da matriz. Essas operações incluem multiplicação de uma linha da matriz por um número não nulo; adição a uma linha de um múltiplo de outra linha;permutação de linhas.
/I 0

2 _1

\2 -1

Com relação a essas operações, considere a matriz B obtida da matriz
—2 depois de efetuada a seguinte sequência de operações elementares: substituição da

-1/

linha 3 pela linha 3 menos a linha 2; substituição da linha 2 pela linha 2 menos duas vezes a linha
Item. 1. Com base nessas informações, julgue o item que se segue, acerca da matriz B.
O determinante da matriz A é igual ao determinante da matriz B.

14.(CESPE/SEDUC AL/2018) Julgue o item que se seguem, relativos a matrizes e sistemas lineares.
Se P for uma matriz simétrica, então P será inversível.

Item. 15. (CESPE/Pref. São Cristóvão/2019) Para a matriz A =

consequentemente, A é uma matriz inversível.

1 0 -1

1 1 1

0 0 1

1 0 0

1 , tem-se que det(A) = —1 e,

GABARITo - CEBRASPE

Determinantes

Item. 1. LETRA D

Item. 2. CERTO

Item. 3. ERRADO

Item. 4. ERRADO

Item. 5. LETRA C

Item. 6. ERRADO

Item. 7. ERRADO

Item. 8. CERTO

Item. 9. CERTO

Item. 10. LETRA A

Item. 11. LETRA C

Item. 12. LETRA C

Item. 13. CERTO

Item. 14. ERRADO

Item. 15. CERTO

