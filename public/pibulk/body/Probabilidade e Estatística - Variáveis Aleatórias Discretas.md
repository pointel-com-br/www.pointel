# Probabilidade e Estatística - Variáveis Aleatórias Discretas

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Introdução - Variáveis Aleatórias Discretas

2) Noções Iniciais sobre Variáveis Aleatórias Discretas

3) Variável Aleatória Discreta

4) Medidas de Tendência Central

5) Função de Distribuição Acumulada

6) Variância e Desvio Padrão

7) Covariância e Correlação

8) Variância da Soma e da Diferença

9) Coeficiente de Variação e Variância Relativa

10) Questões Comentadas - Noções de Variáveis Aleatórias Discretas - Cebraspe

11) Lista de Questões - Noções de Variáveis Aleatórias Discretas - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Olá, amigo(a)! Espero que estejam ficando mais à vontade com Estatística!

Nesta aula, vamos estudar Variáveis Aleatórias Discretas. Veremos algumas definições e suas propriedades que são moderadamente cobradas nas provas de concursos e te ajudam a entender melhor a aula deDistribuições Discretas de probabilidade.

Vamos lá?

Luana Brandão

Quer me conhecer um pouquinho? Sou Doutora em Engenharia de Produção, pela
Universidade Federal
Fluminense, e Auditora Fiscal da SEFAZ-RJ. Tornei-me professora de Estatística do
Estratégia, para ajudá-lo(a)
na sua trajetória rumo à aprovação!

Se tiver alguma dúvida, entre em contato comigo!

M professoraluanabrandao@gmail.com

IS)@professoraluanabrandao

"O sucesso é a soma de pequenos esforços repetidos dia após dia."

Robert Collier

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

VARIÁVEIS ALEATóRIAS DISCRETAS

Conceitos Iniciais

Introdução à Estatística Inferencial

Com esta aula, estamos iniciando os estudos em Estatística Inferencial ou Inferência
Estatística, que é o ramo da Estatística que nos ajuda a tirar conclusões a respeito de um todo (que chamamos de população) a partir das observações feitas em uma parte dessa população (que chamamos de amostra).A inferência é uma técnica importante, pois normalmente não é possível conhecer a informação exata (por exemplo,altura, idade, salário, etc.) para toda a população.

Por exemplo, para conhecer a altura média dos brasileiros, os órgãos responsáveis por essa estatística NÃOverificam a altura de TODOS os brasileiros para conhecer exatamente a sua média. Em vez disso, é selecionada uma amostra de brasileiros, a partir da qual são feitas as medições necessárias. Por fim, com base nessas medições da amostra, são feitos os cálculos necessários para tirar conclusões a respeito da altura média da população de brasileiros.
Vamos destacar os seguintes conceitos do processo que acabamos de descrever:

* A característica numérica da população que se deseja conhecer (no nosso exemplo, a altura média da população de brasileiros) é chamada de parâmetro populacional;
* A medida correspondente feita na amostra (no caso, a altura média dos brasileiros da amostra selecionada) é chamada de parâmetro de estimativa ou estatística da amostra;
* As conclusões a respeito da população feitas a partir da amostra são chamadas de inferência.

As etapas desse processo de inferência estão representadas abaixo:

Selecionar uma amostra Calcular a estatística da amostra
Inferir o parâmetro populacional ixi * xr*ix X12 * * 2
Hoje, vamos começar a estudar a base que permeia o processo.

A inferência do parâmetro populacional não é uma informação exata, a qual seria obtida somente se toda a população fosse verificada. Como os cálculos são feitos a partir de uma amostra,somente, os resultados vão depender da amostra selecionada. Ou melhor, vão variar de acordo com a amostra. Por isso, dizemos que as medidas obtidas a partir da amostra são variáveis aleatórias!
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Variáveis Aleatórias

A definição de variável aleatória, ou simplesmente v.a., é uma função que associa um número real a cada ponto amostrai, isto é, a cada elemento do Espaço Amostrai.
Com isso, passamos a ter uma caracterização numérica do resultado de um experimento ou fenômeno aleatório.
Quando utilizamos o número 0 (zero) para representar a face CARA e o número 1 para representar a faceCOROA, criamos justamente uma variável aleatória! Outro exemplo de variável aleatória é atribuir o número indicado na face superior do dado {1,2,3,4,5,6} ao resultado do seu lançamento (o que é bastante comum).
Assim como os resultados dos experimentos e fenômenos que representam, os valores das variáveis aleatórias também são incertos (variáveis que apresentam valores certos não são variáveis aleatórias).Apesar dessa incerteza, os resultados das variáveis aleatórias apresentam certo padrão,
o que torna possível lhes atribuir probabilidades.
Por exemplo, se denotarmos a variável que representa o lançamento de uma moeda equilibrada por X, então a probabilidade de termos X = 0 (o que equivale à probabilidade de obtermos a face CARA) é:
resultados favoráveis (CARA) 1

resultados possíveis (CARA, COROA) 2

Note que mudamos um pouco a forma que escrevemos a probabilidade, pois agora estamos associando-a a uma variável aleatória e não mais a um evento. Por isso, em vez de escrevê-la comoP(A), para representar o evento A, estamos utilizando a forma P(X = 0). Alternativamente, podemos utilizar a forma P(0).
Similarmente, a probabilidade de termos X = 1 (face COROA) é:

P(X = 1)

resultados favoráveis (COROA) 1

resultados possíveis (CARA, COROA) 2

Se denotarmos a variável que representa o resultado do lançamento de um dado equilibrado por Y, então a probabilidade de termos Y = 1 é:
p(Y = 1) =

„ s resultados favoráveis 1 = -

resultados possíveis 6

A probabilidade de qualquer outro resultado do dado é a mesma:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nesses dois exemplos, as variáveis aleatórias são discretas, pois a quantidade de valores que elas podem assumir é enumerável (isto é, contável). No caso da moeda, há 2 possíveis resultados;para o dado, há 6
possíveis resultados. Normalmente, os valores possíveis de uma variável discreta são números racionais.
O conjunto dos números racionais (Q) engloba os números inteiros e decimais (finitos ou infinitos com dízima periódica), ou seja, todos os números que podem ser descritos em forma de fração.
Não estão englobados os números irracionais (II), isto é, os números infinitos sem dízima periódica, como as constantes n = 3,1415... e o número neperiano e = 2,718...
Juntos, os racionais e irracionais formam o conjunto dos números reais (IR).

Por outro lado, há variáveis aleatórias contínuas, cujos resultados não são enumeráveis. Essas podem assumir quaisquer valores dentro de um intervalo (ou conjunto de intervalos),finito ou infinito. Por exemplo, suponha que a variável Z represente a quantidade de água que um brasileiro ingere em um dia.Assim, Z pode assumir qualquer valor maior ou igual a 0L.

Para variáveis contínuas, não atribuímos probabilidades aos seus resultados. Ou seja,
não calculamos a probabilidade de um brasileiro beber exatamente 2L de água em um dia, isto é,exatamente 2,000000...
litros, nem um milésimo de litro a mais nem a menos. Essa probabilidade é sempre nula.

No entanto, podemos atribuir probabilidades a um intervalo, por exemplo, entre 1,95L e
2,05L e mensurar os resultados obtidos.
Para variáveis contínuas, há infinitos valores possíveis. Porém, não é essa a característica que distingue os dois tipos de variável aleatória. Isso porque as variáveis discretas também podem assumir um número infinito de valores, desde que tais valores sejam enumeráveis.
Por exemplo, suponha que uma variável aleatória represente o número de carros que chegam em um pedágio. Essa variável poderá assumir os valores 1, 2, 3,... Não há um limite para a variável, pois sempre será possível chegar mais um carro. Portanto, há infinitos valores possíveis. Entretanto, esses valores são enumeráveis (contáveis), pois nunca aparecerá meio carro, ou qualquer outra parcela de carro.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em resumo, as Variáveis Aleatórias Discretas e Contínuas possuem as seguintes características:

Variáveis Aleatórias
Discretas

* Quantidade de valores possíveis é enumerável (finito ou não)

* Atribuímos probabilidades a resultados específicos

Variáveis Aleatórias
Contínuas

* Assumem qualquer valor dentro de um intervalo

* Os resultados possíveis são infinitos e não enumeráveis

* Não atribuímos probabilidade a resultados específicos, apenas a intervalos l«** IX
r**.................. *

t i (CESPE/2005 - Secretaria de Educação/MG) A identificação do tipo de variável é um requisito importante i
= para a escolha do teste estatístico mais adequado. Acerca das variáveis, julgue o seguinte item.
;

I

I

: Os valores das variáveis quantitativas discretas não podem ser contados, mas apenas mensurados.

; Comentários:

I

i Os valores das variáveis discretas podem ser contados, enquanto os valores das variáveis contínuas não i podem ser contados, apenas mensurados.j

I

; Gabarito: Errado.

I

I

I

I

; (2017 - SEDUC/MT) Sobre as variáveis serem discretas ou contínuas, analise as afirmativas abaixo, dê valores j
= Verdadeiro (V) ou Falso (F).
;

() A contagem do número de alunos dentro de uma sala de aula só pode ser uma variável discreta, pois é j
: um número inteiro racional e positivo.

I

: () A contagem da quilometragem de um corredor em uma pista circular é uma variável contínua, pois este i
= valor pode assumir qualquer valor dentro do intervalo real, no caso múltiplos de n (pi).
;

= () O caso do termômetro analógico (de mercúrio), a variável representada nele é uma variável discreta, pois i
= aceita todos os valores intermediários entre duas temperaturas a e b.
i

= Assinale a alternativa que traga, de cima para baixo, a sequência correta.
j a) V, V, F
b) V, V, V

c) V, F, V

d) F, F, V
j e) F, V, F

: Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I: Em relação ao primeiro item, o número de alunos dentro de uma sala é, de fato,
uma variável discreta, pois =I

; os alunos podem ser enumerados. O número de alunos é um número racional e positivo. Portanto, a ;
; afirmativa é verdadeira.

I

: Em relação ao segundo item, a distância percorrida por um corredor é uma variável contínua, pois pode i i assumir quaisquer valores reais, dentro de determinado intervalo, inclusive valores múltiplos de n, por se i tratar de uma circunferência. Portanto, a afirmativa é verdadeira.i

: Em relação ao terceiro item, por aceitar todos os valores intermediários entre quaisquer duas temperaturas, j i os resultados de um termômetro analógico correspondem uma variável contínua. Portanto,a afirmativa é i i falsa.
i

= Assim, a sequência correta é V, V, F.

I

: Gabarito: A

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

VARIÁVEL ALEATóRIA DISCRETA

Aqui, trataremos apenas de variáveis aleatórias discretas. Como já sabemos, para essas variáveis, podemos atribuir probabilidades a resultados específicos. É possível calcular a probabilidade de a face superior do dado lançado ser especificamente igual a 1, por exemplo.
Ou seja, sendo x um resultado possível para a variável X (no nosso exemplo, temos x
= 1), então podemos calcular a probabilidade de a variável X assumir tal resultado, isto é, X = x:
P(X = x)

No lançamento de um dado, a probabilidade de obter a face X = 1 (ou qualquer outra face) é:

P(X = 1) = 7

Agora, vamos supor que tenhamos testado um medicamento em uma amostra de 100 pessoas,
das quais 80
pessoas apresentaram melhora em seu quadro. Então, podemos representar os resultados obtidos pela variável Y e dizer que Y = 1 representa o resultado de melhora e Y = 0 representa o resultado em que não houve melhora. Assim, a probabilidade de ter Y = 1 é:
p(zy = !) = —- =800,8

Em outras palavras, podemos definir a probabilidade dessa variável como:

P(y = y)

n(Y = y)

n(t/)

Em que n(Y = y) representa a frequência do resultado Y = y (nesse exemplo,
calculamos a probabilidade de Y = 1); e n(t/) representa a quantidade de todos os resultados possíveis.
Se estivéssemos observando os resultados em uma amostra, n(Y = y) representaria o número de vezes em que foi observado o resultado y; e n(t/) representaria o número total de observações da amostra, chamado de tamanho amostrai.
Chamamos essa função que atribui uma probabilidade a um resultado de uma variável aleatória discreta de função de probabilidade.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por se tratar de uma probabilidade, essa função satisfaz aos axiomas de probabilidade: P > 0 e
P(lT) = 1-

TOME

NOTA!

i) P(X = x) > 0, pois não há probabilidade negativa;

ii) Somatório das probabilidades de todos os possíveis resultados é igual a 1, pois a probabilidade de todo o Espaço Amostrai é P(U) = 1.
Vimos que para o lançamento de um dado, a probabilidade de todos os resultados é:

P(X = 1) = P(X = 2) = P(X = 3) = P(X = 4) = P(X = 5) = P(X = 6) = -

O que atende à primeira condição, por se tratar de um valor positivo. Para verificar a segunda condição,
somamos as probabilidades de todos os resultados:

P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4) + = 5) + P(X = 6) =

1111116

T+T+T+T+T+T=T=1

No exemplo dos medicamentos, observamos que a frequência de pessoas que apresentaram melhora foiP(Y = 1) = 0,8. Então, para que o somatório de todos os possíveis resultados seja
P(U) = 1, a frequência de pessoas que não apresentaram melhora é:
P(Y = 0) = 1 - P(Y = 1) = 1 - 0,8 = 0,2

Assim, observamos que esse exemplo também atende às 2 condições da função de probabilidade, isto é,todos os valores y apresentam valores de probabilidade não negativos, P(Y =
y) > 0, e a soma das probabilidades de todos os possíveis valores é P(U) = 1.
Em vez de apresentar resultados fixos, como os que acabamos de ver, a função de probabilidade P(X = x)
também pode ser definida como uma função do valor de x, como no exemplo a seguir.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

EXEMPLIFICANDO

A função de probabilidade pode ser definida como:

P(x = 0 = Para x = 1, 2, 3, 4,...

2 2

Ou seja, para x = 1, temos: P(x = 1) = = -

2 2

Para x = 2, temos: P(x = 2) = p = -

2 2

Para x = 3, temos: P(x = 3) = -? = —

' v J 33 27

Para esse exemplo, podemos observar que os valores de probabilidade são positivos.

Para verificar a segunda propriedade, devemos observar que se trata de uma Progressão Geométrica infinita,
1 2

com razão q = - e termo inicial A± = cuja soma é dada por:

2 2

Algumas questões fornecem a função de probabilidade com uma incógnita, que você deve calcular utilizando essas propriedades.
EXEMPLIFICANDO

Vamos supor a seguinte função de probabilidade, para um valor de k que ainda não conhecemos:
P(X = %) = 7 para x = 1, 2, 3 e 4

K.

Ou seja, as probabilidades deX = l, X = 2, X = 3eX = 4 são:

P(X = 1)=1, P(X = 2)=^, P(X = 3)=|, P(Jf = 4) = |

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para descobrir o valor de k, devemos considerar que o somatório de todas as probabilidades é igual a 1:
P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4) = 1

12 3 4

k + k + k + k

1 + 2 + 3 + 4 10

k k 1

k = 10

Agora, podemos conhecer todas as probabilidades:

m = 3)=^, P(X = 4) 1Õ

l«** IX

(2014 - Fundação João Pinheiro/MG) A fórmula P(x) = 3k/x representa a distribuição de probabilidade de uma variável aleatória, para x = 1,7,9. Portanto P(1 < x < 7) é igual a a) 27/237
b) 23/63

c) 1/3

d) 216/237

e) 210/23

Comentários:

Sabendo que a x pode assumir 1, 7 ou 9, a soma dessas probabilidades deve ser igual a 1:

P(x = 1) + P(x = 7) + P(x = 9) = 1

3k 3k 3k

~ + ~ + ~9= 1

Sabendo que o MMC é 1 x 7 x 9 = 63, temos:

3k x 63 + 3k x 9 + 3k x 7 3k x (63 + 9 + 7) 3k x (79)

63 63 _ 63 _ 1

3k x 79 = 63

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

: Portanto, a probabilidade de x é:

:

z x 3k 63

pçx = x)= — = —-

:
X 79.x

; Agora, podemos calcular o valor de P(1 < X < 7):

P(1 < X < 7) = P(X = 1) + P(X = 7)

i ;'iYz x 63 63
" —

, , 63 9

I pU = 7) = 7977=79

A soma será, portanto:

P(ᶻ1 < X < 7) =— + — = —

x 63 972

i
V " " 7 79 7979

= Multiplicando o numerador e o denominador desse resultado por 3, obtemos a resposta:

s z x 72 216
* P(1 < x < 7) = —
=----------------

v J 79 237

Gabarito: D

O conjunto dos pares (x,P(X = %)), isto é, o valor da variável e sua respectiva probabilidade, é chamado de distribuição de probabilidade da variável.
Uma forma de representá-la é por meio de uma tabela, relacionando o valor da variável com a sua probabilidade. A seguir, apresentamos a distribuição de probabilidade para o lançamento de um dado equilibrado, em forma de tabela.
PÇX = Xi)

P(X = Xi) 1

i

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Também é possível utilizar um gráfico de barras, com os valores da variável no eixo das abcissas (eixo horizontal) e os respectivos valores de probabilidade no eixo das ordenadas (eixo vertical).
Por exemplo, vamos supor um dado viciado (não equilibrado), com a distribuição de probabilidades apresentada no gráfico a seguir:
Distribuição de Probabilidades
Dado Viciado

Podemos observar que a distribuição de probabilidades de cada face do dado viciado, representada no gráfico acima, corresponde à distribuição representada na tabela abaixo:
Xt

P(X = Xí)

i

PÇX = Xi)

5% = 0,05

10% = 0,10

15% = 0,15

20% = 0,20

25% = 0,25

25% = 0,25

Pontue-se que o gráfico de barras é diferente do histograma, ilustrado abaixo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O histograma apresenta uma distribuição de frequências para variáveis contínuas, como faixas de altura de uma população, por exemplo; enquanto o gráfico de barras representa variáveis discretas.
Por isso, não há espaço entre as barras de um histograma, enquanto há espaço em um gráfico de barras.
FIQUE

ATENTO!

Dizemos que duas ou mais variáveis aleatórias são independentes e identicamente distribuídas (i.i.d. ou IID) se todas as variáveis forem mutuamente independentes entre si e tiverem a mesma distribuição de probabilidade, isto é, mesmos (%;,?(%;)).
Vamos supor, por exemplo, uma variável Y com a seguinte distribuição de probabilidades:

yt i
P(Y = yj

L

P(X = yò

0,05

0,10

0,15

0,20

0,25

0,25

Podemos observar que a variável X referente ao dado viciado e esta variável Y
apresentam os mesmos resultados possíveis {1, 2, 3, 4, 5, 6} e as mesmas probabilidades associadas a cada resultado possível: P(l) =
0,05; P(2) = 0,10; P(3) = 0,15; P(4) = 0,20; P(5) = 0,25 e P(6) = 0,25.

Portanto, podemos dizer que X e Y apresentam a mesma distribuição de probabilidade.

Assim, se X e Y forem independentes, concluímos que essas variáveis são independentes e identicamente distribuídas (i.i.d.).
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (CESPE/2015 - Telecomunicações Brasileiras S.A.) Considerando que Yi, Y₂, Yn,
... sejam variáveis i

; aleatórias independentes que satisfazem P(Yj = j) = P(Yj = -j) = 1/2 para j = 1,
2,..., julgue 0 item que se segue. j
I

I

: As variáveis aleatórias Yi, Y₂,..., Yn,... são identicamente distribuídas.
i

I

I

i Comentários:

= Para Yi, temos:

p(Yi = 1) = P(Yi = -1) = 1/2

I

I

i ParaY₂, temos:

i

P(Y2 = 2) = P(Yi = -2) = 1/2

I

jO que segueindefinidamente. Para um Ynqualquer, temos:
i

P(Yn = n) = P(Yn = -n) = 1/2

= Ou seja, os valores de probabilidade são os mesmos, mas os valores que a variável assume (que normalmente i
= chamamos de x, mas 0 enunciado chamou de j), não são os mesmos. Portanto, as variáveis não são i
; identicamente distribuídas.
j

: Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

MEDIDAS DE TENDÊNCIA CENTRAL

Neste tópico, veremos três medidas de tendência central relevantes para distribuições de probabilidade,quais sejam a esperança, a moda e a mediana. O objetivo dessas medidas é resumir a posição central das variáveis aleatórias, no intuito de facilitar a análise dos seus resultados.
Esperança Matemática

A esperança matemática de uma variável corresponde ao seu valor médio, podendo ser chamada também de expectância, valor esperado ou média.
Para ilustrar esse conceito, vamos supor que Maria enfrente trânsito de sua casa até o trabalho. Depois de algum tempo fazendo esse trajeto, Maria terá alguma noção de quanto tempo ela costuma levar para chegar no trabalho, isto é, uma média do tempo que ela leva.
Essa noção de quanto tempo se "costuma" ou se "espera" levar é justamente a esperança da variável. Neste último exemplo, a esperança corresponde ao tempo médio que a pessoa leva de casa ao trabalho; e no exemplo da altura dos brasileiros, a esperança corresponde à média de altura dos brasileiros.
Sendo X uma variável aleatória, a sua esperança é indicada por £(X) ou nx.

Para os exemplos dos lançamentos de moedas ou dados, em que os resultados são equiprováveis, a esperança corresponde à média aritmética dos resultados. Assim, para o lançamento de uma moeda, com faces 0 e 1, temos:
z x 0 + 1

E(X) = = 0,5

Para o lançamento de um dado, com faces de 1 a 6, temos:

1+2+3+4+5+6 21

£(K) = - = — = 3,5
6 6

Contudo, no caso geral, para qualquer variável aleatória discreta, a esperança é calculada multiplicando-se cada valor da variável pela sua respectiva probabilidade, e, em seguida, somando-se todos os resultados.
TOME

NOTA!

E(X) = £x.P(X = x)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Aplicando essa fórmula geral1 para a variável que representa o

P(X = 0) = | e P(X = 1) = |, temos:

lançamento de uma moeda, em que

Para o lançamento de um dado, em que todas as probabilidades são de -, temos:

! i ! i ! i

E(Y^ — lx — + 2x — + 3x — + 4x — + 5x — + 6x —
6 6 6 6 6 6

1+2+3+4+5+6 21

E(O= -6

= - = 3,5

Podemos efetuar esse mesmo cálculo, a partir da tabela de distribuição de probabilidade, criando uma coluna com o produto de x£ e P(%£). Assim, a esperança corresponderá à soma de todas as linhas dessa nova coluna.
Xi-POi)

v lx1/ =1/

v6 2 X 6V =6 2/

3 6 3 x V6 =

3 *6

4 v6

4xV6 = V6

Soma das

5 x

6 6 x 6

6 6

= 5/

= %⁶

Colunas

1 E(X) = 3, 5

1A rigor, representamos o somatório junto a um índice i:

n

E(X) = ^Xt.PÇX = xt)

i=l

Esse índice deixa claro que estamos somando para os diferentes valores de i, desde i = 1 até i = n,
ou seja, para

^1, ^2> >

Porém, nesta aula, daremos preferência à notação sem o índice, no intuito de simplificar a fórmula visualmente.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

NA

PROVA!

Algumas questões fornecem uma tabela com vários cenários e estratégias possíveis, com os resultados e as probabilidades correspondentes; e pedem para você indicar a que resulta no maior valor esperado.
No exemplo a seguir, temos 3 possíveis estratégias de negócio e os lucros associados a cada uma delas, considerando 3 possíveis cenários. A probabilidade de cada cenário também consta na tabela.
Cenário 1 (30%)

Cenário 2 (50%)

Cenário 3 (20%)

Estratégia 1

R$ 1000,00

R$ 600,00

R$ -100,00

Estratégia 2

R$ 800,00

R$ 500,00

R$ 200,00

Estratégia 3

R$ 500,00

R$ 500,00

R$ 500,00

Para escolher a estratégia associada ao maior lucro esperado, vamos calcular a esperança de cada estratégia, multiplicando o lucro de cada cenário pela respectiva probabilidade:
F(l) = 1000 x 30% + 600 x 50% - 100 x 20% = 300 + 300 - 20 = 580

£(2) = 800 x 30% + 500 x 50% + 200 x 20% = 240 + 250 + 40 = 530

F(3) = 500 x 30% + 500 x 50% + 500 x 20% = 150 + 250 + 100 = 500

Assim, podemos concluir que a Estratégia 1 resulta no maior lucro esperado.

i«** IX

(2017 - Secretaria de Saúde/RO) Uma variável aleatória discreta X tem valores possíveis
0, 1, 2 e 3 com probabilidades respectivamente iguais a 0,2, 0,4, 0,3 e 0,1. A média de X é igual a a) 1,0.
b) 1,3.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) 1,5.

d) 1,8.

e) 1,9.

Comentários:

Vamos inserir as informações do enunciado na tabela de distribuição de probabilidade a seguir:

X P(x) x.P(x)

0 0,2 0 x 0,2 = 0

1 0,4 1 x 0,4 = 0,4

2 0,3 2 X 0,3 = 0,6

3 0,1 3 X 0,1 = 0,3

Assim, a esperança é a soma da última coluna:

E(X) = 0 + 0,4 + 0,6 + 0,3 = 1,3

Gabarito: B.

(VUNESP/2019 - Prefeitura de Campinas/SP) Sabe-se que as probabilidades de um carro transportar 1, 2,3, 4 ou 5 pessoas são de 0,05, 0,20, 0,40, 0,25 e 0,10, respectivamente. Se em uma cidade chegaram 400carros, a estimativa de pessoas que chegaram é de a) 1400.
b) 1600.

c) 1260.

d) 2000.

e) 1320

Comentários:

A estimativa do número de pessoas transportadas por carro corresponde à esperança dessa distribuição.Inserindo as informações do enunciado na tabela de distribuição, temos:

X P(x) x.P(x)

1 0,05 1 x 0,05 = 0,05

2 0,20 2 x 0,2 = 0,4

3 0,40 3 x 0,4 = 1,2

4 0,25 4 x 0,25 = 1

5 0,10 5 x 0,1 = 0,5

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, a esperança é a soma da última coluna:

= 0,05 + 0,40 + 1,20 + 1,00 + 0,50 = 3,15

Logo, são transportadas, em média, 3,15 pessoas por carro. Sabendo que chegam
400 carros, então a estimativa de pessoas é de:
400x3,15 = 1260

Gabarito: C

(FGV/2022 - PC/AM) Suponha que X, uma variável aleatória discreta, assuma a seguinte distribuição de probabilidade:
X Proba(X)

0 0

1 1/4

2 1/4

3 K

O valor de K e o valor esperado de X são, respectivamente:

a) 0 e 3/4

b) 1/4 e 3/2

c) 1/2 e 3/4

d) 1/2 e 3/2

e) 1/2 e 9/4

Comentários:

Para resolver essa questão, o primeiro passo é calcular o valor de K,
considerando que a soma das probabilidades dos possíveis resultados é igual a 1 (probabilidade de todo o Espaço Amostrai):
P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3) = 1

1 1

0+-+-+K=l

4 4

1 1

E para calcular a esperança, somamos os produtos dos valores de x com as respectivas probabilidades

Gabarito: E

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

00551155220001199000- -EEvveertrotonrMurilo Vieira

I= (CESPE/2010 - Agência Brasileira de Inteligência) Sabendo que X é variável aleatória discreta que pode
; assumir valores inteiros não negativos, julgue o próximo item.
I

A média de X é não negativa.

i Comentários:

A média da variável é a soma dos produtos dos resultados pelas respectivas probabilidades:

j E(X) = \x.P(X = x)

i Sabemos que a probabilidade é sempre maior ou igual a zero (condição necessária).
Então, se os valores da

= variável são não negativos, o produto de ambos será sempre maior ou igual a zero
(não negativo).

= Consequentemente, a média, que corresponde à soma desses valores será maior ou igual a zero.

I

: Gabarito: Certo.

i (CESPE/2015 - Telecomunicações Brasileiras S.A.) Considerando que Yi, Y₂, ..., Yn,
... sejam variáveis

; aleatórias independentes que satisfazem P(Yj = j) = P(Yj = -j) = 1/2 para j = 1, 2,..., julgue 0
item que se segue.

: O valor esperado para a variável aleatória Yj é nulo para todo número natural positivo j i Comentários:
= Para ilustrar 0 cálculo da esperança para Yj, vamos primeiro calcular a esperança para j = 1 e j
= 2.

I

: Sabemos que para Yi, temos P(Yi = 1) = P(Yi = -1) = %. Logo, a esperança de Yi é:

E(Yi) = -1 x 1/2 + 1 x 1/2 = -1/2 + % = 0

I

: Para Y₂, temos P(Y₂ = 2) = P(Yi = -2) = %, então a esperança dessa variável é:

E(Y2) = -2 x y2 + 2 x y2 = -1 + 1 = 0

; Ou seja, para um Yj qualquer, temos P(Yj = j) = P(Yj = -j) = 1/₂ e sua esperança é dada por:

E(Yj) = -j x 1/₂ + j x y₂ = 0

: Logo, a esperança é nula para qualquer j = 1, 2, ...

: Gabarito: Certo.

0666666699999333333333333888811111111

Propriedades da Esperança

Nesta seção, veremos propriedades da esperança. Vale adiantar que essas propriedades valem também para a esperança de variáveis aleatórias contínuas.
Nos enunciados abaixo, consideramos X e Y variáveis aleatórias e k uma constante real qualquer.

i) E(fc.X) = fc.E(X)

De acordo com essa propriedade, a esperança de uma variável aleatória X, cujos valores foram multiplicados por uma constante k, é igual a k vezes a esperança da variável aleatória X.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos considerar, como exemplo, um grupo de funcionários com salários distintos, de modo que a média seja R$ 5.000. Segundo essa propriedade, se os salários de todos os funcionários forem dobrados, então a média também será dobrada (passará para R$ 10.000).
Mas vamos confirmar isso!

Digamos que os funcionários tenham os seguintes valores de salário, em mil reais:

X = {1, 2, 2, 2, 3, 5, 7, 7, 10, 11}

Sorteando um desses 10 funcionários ao acaso, o valor esperado do salário do funcionário sorteado pode ser calculado pela média aritmética de todos os 10 salários:
z , 1 + 2 + 2 + 2 + 3 + 5 + 7 + 7 + 10 + 11 50

E® = 10 = Tõ"5

Duplicando os salários de todos os funcionários, temos:

Y = 2.X = {2, 4, 4, 4, 6, 10, 14, 14, 20, 22}

Nesse caso, o valor esperado será:

2 + 4 + 4 + 4 + 6 + 10 + 14 + 14 + 20 + 22 100

Em = 10 = 7T = 1Ü

Também podemos multiplicar uma variável por uma constante e representar a distribuição resultante utilizando a tabela de distribuição de probabilidade.
Para ilustrar, vamos considerar o mesmo exemplo dos salários. Considerando que há 10
elementos no total, a tabela de distribuição para X é:

X P(X = x)

1 1/10

2 3/10

3 1/10

5 1/10

7 2/10

10 1/10

11 1/10

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E a média (ou esperança) pode ser calculada como:

EW =

Etf) = 5

Para obter a tabela de distribuição de Y = 2X, duplicamos os valores da primeira coluna
(referentes aos elementos da distribuição) e mantemos as mesmas probabilidades:

y P(Y = y)

2 1/10

4 3/10

6 1/10

10 1/10

14 2/10

20 1/10

22 1/10

Calculando a esperança de Y, observamos que ela é o dobro da esperança de X:

F(K) = 2 x — + 4 x - + 6 x - + 10 x — + 14 x — + 20 x — + 22 x —

10 10 10 10 10 10 10

E(X) _l i_22i_2 i_12_i_22_i_22_i_2£ — 122

K) K) K) K) K) K) 10 10

A mesma propriedade vale quando dividimos a variável pela constante, isto é:

„ (X\ E(X)

\k) k

Ou seja, se cada salário fosse dividido por 2, então a média também seria divida por
2: passaria de R$ 5.000
para R$ 2.500.

Na verdade, essa é a mesma propriedade da multiplicação, pois ao invés de pensarmos que estamos dividindo por 2, podemos pensar que estamos multiplicando por k =-.
ii) E(X + fc) = E(X) + k

A esperança de uma variável aleatória X, sendo esta somada a uma constante k, é igual a k mais a esperança deX.
Ou seja, se todos os funcionários do nosso exemplo, cuja média salarial era de R$
5.000, tiverem um aumento de R$ 2.000, então a média desse grupo passará para R$ 7.000, segundo essa propriedade.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vamos verificar essa propriedade novamente. Sabendo que os salários originais eram X =
{1, 2, 2, 2, 3, 5, 7,
7, 10, 11}, então, com um aumento de 2 mil reais, eles passarão a ser:

Y = X + 2 = {3, 4, 4, 4, 5, 7, 9, 9, 12, 13}

Assim, a esperança será:

3 + 4 + 4 + 4 + 5 + 7 + 9 + 9 + 12 + 13 70

Em= lõ
=iõ=7

A mesma propriedade vale quando subtraímos a variável pela constante, isto é:

E(X -k) = E(X) - k

Ou seja, se cada funcionário recebesse uma redução de R$ 2.000 do seu salário, então a média também seria reduzida em R$ 2.000: passaria de R$ 5.000 para R$ 3.000.
Na verdade, essa é a mesma propriedade da adição, pois ao invés de pensarmos que estamos subtraindo 2,podemos pensar que estamos somando k = -2.

iii) E(X + V) = E(X) + E(V)

Por essa propriedade, temos que a esperança da soma de duas variáveis, X e Y, é igual à soma da esperança de X com a esperança de Y.
Digamos que um grupo de homens receba um salário médio E(X) = 5.000; e que um grupo de mulheres receba, em média, E(Y) = 4.000. Ao selecionar uma mulher e um homem, o valor do salário somado será, em média:
E(X + Y) = E(X) + E(Y) = 5.000 + 4.000 = 9.000

Para verificar essa propriedade, vamos utilizar um exemplo menor, pois envolve encontrar todas as possíveis combinações dos elementos dos dois grupos e somá-los. Suponha, então, o experimento de lançamento de duas moedas (Xi e X₂), com faces representadas por 0 e 1.
Ao lançarmos ambas as moedas, temos os seguintes valores possíveis:

(Xi,X₂) = {(0,0), (0,1), (1,0), (1,1)}

Ao somarmos esses valores, temos:

Xi + X₂ = {(0 + 0), (0 + 1), (1 + 0), (1 + 1)} = {0,1,1,2}

A média é então:

E(%l+X2)

0+1+1+2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabendo que o valor esperado dos dois lançamentos é E(Xi) = E(X₂) = então confirmamos que, de fato:

E(Xx + X2) = EQQ + E(X2) =| + |=1

A mesma propriedade vale para a subtração de variáveis:

E(Xi - X2) = E(Xi) - E(X2)

iv) E(fc) = k

Ou seja, o valor esperado de uma constante é igual à própria constante.

Digamos que em um grupo de funcionários, o salário individual de todos seja igual a k = 5 mil reais.Selecionando um funcionário ao acaso, qual será o salário esperado? Certamente, 5 mil reais.

Também podemos obter esse resultado, a partir da fórmula da esperança. Sendo k = 5,
então para um grupo de n funcionários, a esperança é:
E(fc) =

n x 5

-------- = 5

TL

v) Se X e Y são independentes, então E(X. V) = E(X). E(K)

Se X e Y são variáveis aleatórias independentes, então a esperança do produto de X e
Y é igual ao produto da esperança de X com a esperança de Y.
Supondo novamente o lançamento das duas moedas, em que (Xi,X₂) = {(0,0), (0,1), (1,0),
(1,1)}. Assim, o produto Xi x X₂ corresponde ao conjunto:
XixX₂ = {0,0,0,!}

A média de Xi x X₂ é, portanto:

E(Xx x X2) =

0 + 0 + 0 + 1 1

4 4

Sabendo que o valor esperado dos dois lançamentos é E(Xi) = E(X₂) = -, então, confirmamos que, de fato:
E(XÍ x X2) = E(XJ x E(X2) = | x | = 4

No entanto, para isso é essencial que as variáveis X e Y sejam independentes (como é o caso de lançamentos distintos).
Por outro lado, é possível verificar a identidade E(X.Y) = E(X).E(Y) e as variáveis não serem independentes.Ou seja, se as variáveis são independentes, então podemos concluir que E(X.Y) =
E(X).E(Y); mas se E(X.Y) =
E(X).E(Y), não sabemos se as variáveis são ou não independentes.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

i) E(fcX) = k. E(X)

ii) E(X ± k) = E(X) ± k iii) E(X ± K) = E(X) ± E(¥)
iv) E(k) = k v) Se X e Y forem independentes, então E(X x F) = E(X) x E(Y)
Essas propriedades podem ser utilizadas conjuntamente e para qualquer número de variáveis aleatórias. Por exemplo, sendo X, Y e Z variáveis aleatórias, então:
e(3.X + ^- 2.Z + l) = E(3.X) + eQ -E(2.Z) + E(1)

(Y \ E (Y 1

3.Z + --2.Z + 1J = 3.E(X)+-^.-2.E(Z) + l l«** IX
......................................................... * «

i (2016 - Instituto Federal de Educação/BA -Adaptada) Sendo X uma variável aleatória,
com média p, então i

= a esperança matemática da função Y = a + bX, com a eb E R, é i
= a) E(Y) = a + b b) E(Y) = a j c) E(Y) = bp d) E(Y) = a + bp e) E(Y) = a2
i

I

I

i Comentários:

I

i Pelas propriedades da esperança, temos E(Y) = E(a + bx) = a +b.E(X). Como p = E(X), temos:
i

E(Y) = a + b.p

I

:

; Gabarito: D.

I

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= (FGV/2017 - IBGE - Adaptada) Para o caso de variáveis aleatórias quaisquer, existem diversas propriedades =Ique se aplicam diretamente à esperança matemática. Dentre essas propriedades está:
;

a) E(X.Y) = E(X).E(Y)

b) E(X+a) = a
;

í c) E(X±Y) = E(X) ± E(Y)

d) E(a.X)= E(X), sendo a uma constante qualquer
;

I

I

i Comentários:

: Em relação à alternativa A, podemos afirmar que E(X.Y) = E(X).E(Y) somente se X e
Y forem independentes. ;

= Como o enunciado não menciona que X e Y são independentes, então a alternativa A está incorreta.

I

: Em relação à alternativa B, temos a seguinte propriedade da esperança:
i

E(X + a) = E(X) + a

I

: Portanto, a alternativa B está incorreta.
i

I

I

: Em relação à alternativa C, temos de fato a seguinte propriedade, para quaisquer variáveis aleatórias X e Y: j
; E(X +Y) = E(X) +
E(Y) ;

E(X - Y) = E(X) - E(Y)

I

I

: Portanto, a alternativa C está correta. Em relação à alternativa D, sabemos que:
E(a.X) = a.E(X). Portanto, a j

= alternativa D está incorreta.
i

I

: Resposta: C.

Moda

A moda de uma variável aleatória é o seu valor mais provável, isto é, o valor com maior probabilidade.
No exemplo de lançamento de duas moedas, Xi e X₂, a soma das variáveis resulta no seguinte conjunto de resultados possíveis:
X = Xi + X₂={0,1,1,2}.

Assim, a probabilidade de cada resultado é:

Como a probabilidade de X = 1 é maior que as demais, então concluímos que a moda dessa variável é X
= 1.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

No gráfico de barras que representa a distribuição de probabilidades de uma variável,
a moda pode ser identificada visualmente, pois estará associada à coluna mais alta, como representado abaixo.
X = X, + x2

A moda é um valor da variável aleatória e não a sua probabilidade. Assim, no gráfico de barras, a moda estará no eixo horizontal.
Se estivermos lidando com uma amostra, a moda, chamada de moda amostrai, corresponde ao valor da variável obtido com maior frequência.
É possível haver mais de uma moda, quando a maior probabilidade estiver associada a mais de um resultado.
No exemplo anterior do dado viciado, tanto a face 5 quanto a face 6 apresentavam a maior probabilidade,de 25%.

Distribuição de Probabilidades
Dado Viciado

Com 2 modas, a distribuição é chamada bimodal.

Uma distribuição trimodal apresenta 3 modas e uma distribuição multimodal apresenta múltiplas modas.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por outro lado, também é possível que uma distribuição não tenha moda, o que ocorre todos os resultados da variável são equiprováveis, como é o caso do lançamento de uma moeda equilibrada e de um dado equilibrado, como ilustrado abaixo.
Distribuição de Probabilidades
Dado Equilibrado

Nessa situação, a distribuição é dita amodal.

Propriedades da Moda

Nesta seção, veremos propriedades da moda, sendo X uma variável aleatória e k uma constante real.

i) MoÇk.X) = k.Mo(X)

Quando uma variável X é multiplicada por uma constante k, a sua moda é igual k vezes a moda de X.Considerando o exemplo dos salários dos funcionários, se os salários dobram, a nova moda também será o dobro da moda anterior.
Para ilustrar, vamos considerar novamente os seguintes valores de salário, em mil reais:

X = {1, 2, 2, 2, 3, 5, 7, 7, 10, 11}

Podemos observar que a moda é igual a 2 mil reais. Duplicando os salários de todos os funcionários,
temos:

2.X = {2, 4, 4, 4, 6, 10, 14, 14, 20, 22}

E a nova moda é igual a 4 mil reais, que é o dobro da moda anterior.

A mesma propriedade vale quando dividimos a variável pela constante, isto é:

Mo(À)

k

Ou seja, se cada salário fosse dividido por 2, então a moda também seria dividida por 2: passaria de 2 mil reais para mil reais.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ii) Mo(X + k) = Mo(X) + k

Quando somamos uma constante k a uma variável X, a sua moda é acrescida da mesma constante k.

Em relação ao exemplo dos salários dos funcionários, se há um aumento de 3 mil reais no salário, a moda também terá esse mesmo aumento: passará de 2 mil reais para 5 mil reais.
Para ilustrar, sabendo que os salários originais eram X = {1, 2, 2, 2, 3, 5, 7, 7,
10, 11}, com um aumento de 3
mil reais, eles passarão a ser:

X + 2 = {4, 5, 5, 5, 6, 8, 10, 10, 13, 14}

Podemos observar que a nova moda é, de fato, de 5 mil reais.

A mesma propriedade vale quando subtraímos a variável pela constante, isto é:

Mo(X - k) = Mo® - k

Ou seja, se cada funcionário recebesse uma redução de mil reais do seu salário, então a moda também seria reduzida em mil reais: passaria de 2 mil reais para mil reais.
RESUMINDO

i) Mo(k.X) = k.Mo(X)

ii) Mo(X±k) = Mo(X)±k

HORA IX

: (FCC/2018 - Prefeitura de Macapá/AP - Adaptada) A medida de tendência central que representa o valor i
= com maior frequência na distribuição de uma amostra é a i
I

I

; a) média amostrai.
i

I

I

b) variância.
;

: c) amplitude total.

I

I

d) mediana.
;

I

I

: e) moda amostrai.

I

: Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A moda de uma amostra é o valor obtido com maior frequência.

Gabarito: E.

(CESPE/2015 - Agente do Departamento Penitenciário Nacional)

quantidade diária de incidentes (IV)
total frequência relativa
0,1

0,2

0,5

0,0

0,2

= Considerando os dados da tabela mostrada, que apresenta a distribuição populacional da quantidade diária j de incidentes (N) em determinada penitenciária, julgue o item que se segue.i

A moda da distribuição de N é igual a 4, pois esse valor representa a maior quantidade diária de incidentes i que pode ser registrada nessa penitenciária.;

i Comentários:

A moda é o valor com maior frequência relativa, que é igual a 0,5.
i

= Essa frequência está associada a N = 2, então a moda é N = 2.
;

I

I

j Gabarito: Errado.

I

; (CESPE/2018 - Departamento de Polícia Federal)

Àr (quantidade diária de drogas apreendidas, em kg)
dia

1 2 3 4 5

10 22 18 22 28

; Tendo em vista que, diariamente, a Polícia Federal apreende uma quantidade X, em kg, de drogas em
=
determinado aeroporto do Brasil, e considerando os dados hipotéticos da tabela precedente, que apresenta i
= os valores observados da variável X em uma amostra aleatória de 5 dias de apreensões no citado aeroporto, j
= julgue o próximo item.
;

I

A moda da distribuição dos valores X registrados na amostra foi igual a 22 kg.

i Comentários:

I

I

A moda de uma amostra é o valor obtido com maior frequência. No caso, foram apreendidos 22kg em 2 dias, i
; enquanto as demais quantidades foram apreendidas em um único dia somente.
i

I

: Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Mediana

A mediana de uma variável é o valor que divide a distribuição em duas partes com mesma probabilidade,de modo que a probabilidade dos valores menores ou iguais à mediana é igual a 50% e a probabilidade dos valores maiores ou iguais à mediana é igual a 50%.
Para ilustrar, o gráfico replicado a seguir representa a distribuição de probabilidades do dado viciado que vimos anteriormente.
Distribuição de Probabilidades
Dado Viciado

Podemos observarque a mediana está entre X = 4e X = 5, pois a probabilidade associada aos valores menores ou iguais a 4 é de 50% e a probabilidade associada aos valores maiores ou iguais a 5 é igual a 50%.
Por convenção, quando a mediana está entre 2 valores, consideramos a média aritmética desses valores:
Agora, vamos considerar o exemplo em que somamos os resultados do lançamento de duas moedas,conforme o gráfico replicado a seguir:

X = X, + x2

Neste caso, temos 25% menor que 1 e 75% menor ou igual a 1; por outro lado, também temos 25% maior que a e 75% maior ou igual a 1. Ainda assim, a mediana será igual a 1. Afinal,não faz sentido ela ser igual a
0 e nem igual a 2.

Então, vamos ajustar a definição: a probabilidade dos valores menores ou iguais à mediana é de pelo menos
50%; e a probabilidade dos valores são maiores ou iguais à mediana também é de pelo menos 50%.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Propriedades da Mediana

As propriedades da mediana que veremos nesta seção são as mesmas das propriedades da moda que vimos anteriormente.
i) MdÇk.X') = k.Md(X)

Quando uma variável X é multiplicada por uma constante k, a sua mediana é igual k vezes a mediana de X.
Considerando o exemplo dos salários dos funcionários, se os salários dobram, a nova mediana também será o dobro da mediana anterior.
Para ilustrar, vamos considerar o mesmo exemplo dos salários, mas agora vamos analisar a tabela de distribuição de probabilidade da variável X = {1, 2, 2, 2, 3, 5, 7, 7, 10,11}:
X P(X = x)

1 10%

2 30%

3 10%

5 10%

7 20%

10 10%

11 10%

Podemos observar que a mediana está entre 3 e 5, pois 50% dos valores são menores ou iguais a 3 e 50%dos valores são maiores ou iguais a 5, de modo que a mediana é, por convenção:

3 + 5

Md(X) =-^—= 4

Duplicando os salários de todos os funcionários, temos s seguinte tabela de distribuição de probabilidade:
2.X

P(X = x)
10%

30%

10%

10%

20%

10%

10%

Agora, a mediana está entre 6 e 10, pois 50% dos valores são menores ou iguais a 6
e 50% dos valores são maiores ou iguais a 10, de modo que a nova mediana é:
6 + 10

Md(2.X) = —-— = 8

Que é o dobro da mediana anterior.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A mesma propriedade vale quando dividimos a variável pela constante, isto é:

fX\ MdÇX)

Ou seja, se cada salário fosse dividido por 2, então a mediana também seria dividida por 2: passaria de 4 mil reais para 2 mil reais.
ii) Md(X + k) = Md(X) + k

Quando somamos uma constante k a uma variável X, a sua mediana é acrescida da mesma constante k.

Em relação ao exemplo dos salários dos funcionários, se há um aumento de 3 mil reais no salário, a mediana também terá esse mesmo aumento: passará de 4 mil reais para 7 mil reais. Vejamos:
X + 3

P(X = x)
10%

30%

10%

10%

20%

10%

10%

E a nova mediana está entre 6 e 8:

Md(X + 3) =

6 + 8

= 7

A mesma propriedade vale quando subtraímos a variável pela constante, isto é:

MoÇX - k) = Mo(X) - k

Ou seja, se cada funcionário recebesse uma redução de mil reais do seu salário, então a mediana também seria reduzida em mil reais: passaria de 4 mil reais para 3 mil reais.
i) Md(k.X) = k.Md(X)

ii) Md(X ± k) = Md(X) ± k

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

..................... . f i (CESPE/2020 - ME) Considerando que R representa uma variável quantitativa cuja média, mediana e
: variância são, respectivamente, iguais a 70, 80 e 100, e que U = — — 7, julgue o próximo item, acerca das
= variáveis U e R.

A mediana de U é negativa.

i Comentários:

'
R

= De acordo com as propriedades da mediana que vimos, a mediana de U = — — 7 é dada por:

, R
Md(R')

í Mdm=-0~7=—-7

: O enunciado informa que a mediana de R é Md(R) = 80, logo a mediana de U é:
i Md(Jf)= — — 7 = 8 —7 = 1

Ou seja, a mediana é positiva.

jL.G...a..b..a..r..i.t.o. : Errado.
a

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

FUNçÃo DE DISTRIBUIçÃo ACUMULADA

A função de distribuição acumulada de uma variável aleatória (ou simplesmente f.d.a ou função de distribuição) apresenta a probabilidade acumulada de todos os valores menores ou iguais a determinado valor x.
TOME

NOTA!

F(x) = P(X < x)

Ou seja, equivale à soma de todas as probabilidades menores ou iguais ao valor x.

Por exemplo, no experimento de lançar um dado, a probabilidade de cada uma das faces, numeradas dela
6, é -. Assim, o valor da função de distribuição acumulada para X = 1 equivale à probabilidade de X
= 1, uma vez que não há valor menor:
F(l) = P(X < 1) = P(X = 1) = -

Para X = 2, a f.d.a. corresponde à soma das probabilidades de X = 1 e de X = 2:

F(2) = P(X < 2) = P(X = 1) + P(X = 2)

Para X = 3, temos a soma das probabilidades de X = 1, X = 2 e X = 3:

F(3) = P(X < 3) = P(X = 1) + P(X = 2) + P(X = 3)

E assim sucessivamente.

Alternativamente, podemos somar a probabilidade no ponto x à função de distribuição acumulada no ponto anterior. Dessa forma, a função de distribuição acumulada para X = 3 é calculada como:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para X = 4, temos:

F(4) = P(X < 4) = P(X = 4) + F(3) = ^ + | = ^

6 6 6

E assim por diante.

Também podemos calcular os valores da f.d.a., incluindo uma nova coluna na tabela da distribuição de probabilidade. Para preenchê-la, basta somarmos o valor da função acumulada acima (valor de X anterior),com o valor da probabilidade da linha em questão (valor de X atual), como ilustrado pelas setas para F(3).
X P(X = x)

1 v6

2 v6

F(x) = P(X < x)

v6

3 % + /—76

4 V6 ——í V6

5 v6 %

6 v6 %

Algumas questões de prova apresentariam essa f.d.a. da seguinte forma:

F(x) = <

r 0,se x < 1 A

-*-/g,se 1 < x < 2

V3 <se 2 < x < 3
I/2,se 3 < x < 4

2/3,se 4 < x < 5

^/g,se 5 < x < 6

v l,se x > 6 )

Também podemos calculara função de distribuição acumulada para uma amostra, chamada de distribuição amostrai ou empírica acumulada. Nessa situação, substituímos as probabilidades pelas frequências relativas observadas na amostra.
De maneira geral, a função acumulada de uma variável aleatória X (discreta ou contínua) apresenta as seguintes características:
i) Fé não decrescente, porque as probabilidades são sempre somadas.

ii) Por ser uma probabilidade, a f.d.a. também assume valores somente entre 0 e 1:

0 < F(x) < 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

FIQUE

ATENTO!

A função de distribuição acumulada F(x) é definida em toda a reta real, ou seja, ela pode ser calculada para qualquer valor de x.
Isso significa que a função de distribuição não assume valores apenas nos pontos dos possíveis resultados da variável. Utilizando o mesmo exemplo do dado, podemos calcular o valor da função de distribuição em outros pontos diferentes de X = 1, X = 2, X = 3,..., X = 6.
Por exemplo, para X = 0,5, a f.d.a. corresponde à soma das probabilidades de todos os valores menores ou iguais a 0,5. Como o menor valor possível é X = 1, então a probabilidade acumulada até X = 0,5 é nula:
F(0,5) = P(X < 0,5) = 0

De forma geral, podemos dizer que, para os valores de x menores que o menor valor possível da variável (no exemplo do dado, para x < 1), o valor da f.d.a. é F(x) = 0.
Para X = 8,1, a f.d.a. corresponde à soma das probabilidades de todos os valores menores ou iguais a 8,1.Como o maior valor possível é X = 6, então a probabilidade acumulada até X = 8,1 é igual à probabilidade acumulada até X = 6, isto é, à probabilidade de todo o Espaço Amostrai:
F(8,l) = P(X < 8,1) = P(X < 6) = 1

De forma geral, podemos dizer que, para os valores de x maiores ou iguais ao maior valor possível da variável (no caso do dado, para x > 6), o valor da f.d.a. é F(x) = 1-
Para X = 4,7, a f.d.a. corresponde à soma das probabilidades de todos os valores menores ou iguais a 4,7.Como as faces do dado são valores inteiros, a probabilidade acumulada até X = 4,7 é igual à probabilidade acumulada até X = 4:
F(4,5) = P(X < 4,5) = P(X < 4) = -

Similarmente, para X = 5,3, a f.d.a. corresponde à probabilidade acumulada até X = 5:

F(5,3) = P(X < 5,3) = P(X < 5) = f

A f.d.a. pode ser calculada para qualquer valor de x, mas os seus valores serão alterados somente nos pontos dos possíveis resultados da variável.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para o nosso exemplo do dado, os valores da f.d.a. serão alterados somente para X =
1, X = 2, X = 3,X = 6.
Veja, no gráfico abaixo, como a f.d.a. dá saltos para esses valores de x.

O tamanho de cada "salto" no gráfico da f.d.a. corresponde à probabilidade em cada ponto x. Nesse exemplo, os "saltos" são todos iguais, pois os valores de X são todos equiprováveis.
Para o exemplo do dado viciado, temos a seguinte f.d.a.:

y = y)

i 0,05

2 0,10

3 0,15

4 0,20

5 0,25

6 0,25

F(y) = P(Y < y)

0,05

0,15

0,30

0,50

0,75

1,00

Assim, o gráfico da f.d.a. para o dado viciado é:

1,0

0,9

0,8

0,7

0,6

0,5

0,4

0,3

0,2

0,1

0 1 2 3
4 5 6
*

Observe que os "saltos" apresentam tamanhos diferentes, uma vez que as probabilidades não são todas iguais.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabendo que esses "saltos" representam as diferenças da função acumulada em cada ponto,
é possível percorrer o caminho inverso, ou seja, calcular a probabilidade P(X = x) de cada ponto, pela diferença entre o valor da f.d.a. no ponto e o valor da f.d.a. no ponto anterior.
Por exemplo, para um dado equilibrado, a probabilidade da face X = 4 pode ser calculada pela diferença entre os valores da f.d.a. nos pontos X = 4 e X = 3:
P(X = 4) = F(4) - F(3) = 7 - I

6 6 6

Para o nosso exemplo do dado viciado, temos:

P(Y = 4) = F(4) - F(3) = 0,5 - 0,3 = 0,2

É possível calcular, ainda, a probabilidade de um intervalo de valores, a partir da f.d.a. Para o nosso exemplo do dado equilibrado, a probabilidade do intervalo P(2 < X < 5) pode ser calculada pela diferença entre a f.d.a. para x = 5 e a f.d.a. para x = 2:
P(2 < X < 5) = F(5) - F(2) = | - f = |

6 6 6

Mas, para isso, é importante verificar se a igualdade está ou não contemplada em cada extremo do intervalo.A diferença entre a f.d.a. no ponto X = 5 e a f.d.a. no ponto X = 2 fornece a probabilidade de a face do dado ser maior que 2 e menor ou igual a 5.
F(5) - F(2) = P(X < 5) - P(X < 2) = P(2 < X < 5)

Isso porque, no ponto X = 5, a f.d.a. contempla a probabilidade para todo valor menor ou igual a 5 e no pontoX = 2, ela contempla a probabilidade para todo valor menor ou igual a 2. Logo,
quando subtraímos esta da primeira, teremos a probabilidade de todo valor menor ou igual a 5 e maior que 2.
TOME

NOTA!

De maneira geral, para a < b, temos:

F(b) - F(a) = P(a < X < h)

Se precisarmos de um intervalo de uma forma diferente, precisaremos adaptá-lo para que fique dessa forma.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

FIQUE

ATENTO!

Se o extremo inferior estiver contemplado no intervalo, ou seja, se o intervalo for:

P(a < X < Z?)

fazemos a adaptação buscando um valor menor que a como novo extremo inferior, o qual não estará contemplado no novo intervalo.
No exemplo do dado, se a face 2 estiver contemplada no intervalo, ou seja, se o intervalo for 2 < X < 5, então fazemos a adaptação, subtraindo 1 unidade do extremo inferior,o qual será 2-1 = 1:
P(2 < X < 5) = P(1 < X < 5) = F(5) - F(l)

P(2 <X < 5) = - -- = -

6 6 6

Por outro lado, se extremo superior não estiver contemplado no intervalo, ou seja, se o intervalo for a < X < b, então fazemos a adaptação buscando um valor menor que b como novo extremo superior, o qual estará contemplado no novo intervalo.
Por exemplo, se a face 5 não estiver contemplada, ou seja, se o intervalo for 2 <
X < 5,
fazemos a adaptação, subtraindo 1 unidade do extremo superior, o qual será 5-1 = 4:

P(2 < x < 5) = P(2 < x < 4) = F(4) - F(2)

P(2 <%< 5) =--- = -

6 6 6

Se o intervalo for da forma a < x < b, faremos as duas adaptações, ou seja,
buscamos um valor menor que a e um valor menor que b:
P(2 < x < 5) = P(1 < X < 4) = F(4) - F(l) = - - 1 = -

6 6 6

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

vm. estrategiaconcursos. com.br l«** IX
(FGV/2018 - ALERO) Uma variável aleatória discreta X tem função de probabilidade dada por:

X

P(x)

-2

0,1

-1

0,2

0,3

0,4

= Se F(x) representa a função de distribuição de X, V x real, então F(-0,8) é igual a a) 0,3.
b) 0,4.

í c) 0,5.

d) 0,6.

e) 1,0.

I

i Comentários:

I

A função acumulada F(-0,8) corresponde à probabilidade P(X < -0,8), que nesse caso é igual à soma das
; probabilidades P(X = -2) + P(X = -1):

F(-0,8) = P(X < -0,8) = P(X = -2) + P(X = -1) = 0,1 + 0,2 = 0,3

= Gabarito: A

I

: (FGV/2015 - TJ/RO) A função distribuição de probabilidade acumulada da variável "número de anos de ;
= experiência de magistrados" de um dado tribunal é dada por:

í AnosfX) 0 5 10
15 25 35 É

: F[x) 0 5,30 0,48
0,69 0,SÓ 1 :

= Então, a probabilidade de que um magistrado escolhido ao acaso tenha experiência maior do que cinco anos i i e menor ou igual a 15 anos é igual a:i a) 0,39.
b) 0,45.
;

c) 0,48.

d) 0,57.

i e) 0,61.

I

: Comentários:

= A probabilidade de P(5 < X < 15) é igual à diferença entre os valores da função acumulada F(15) - F(5), uma =i vez que o intervalo não precisa ser adaptado, pois o extremo superior está contemplado e o inferior, não: i
P(5 < X < 15) = P(X < 15) - P(X < 5) = F(15) - F(5) = 0,69 - 0,30 = 0,39

= Gabarito: A

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= (FGV/2017 - MPE/BA) Considere a variável aleatória do tipo discreta(X), relativa às fases de andamento de
: um processo podendo assumir apenas três valores numéricos 1, 2 ou 3, conforme o mesmo esteja em
= conhecimento, liquidação ou execução, respectivamente. Se F(.) é a função distribuição acumulada
= correspondente, com F(l, 17) = 0,15 e F(2,76) = 0,45. Então é verdadeiro que

: a) P(X > 1,9) = 0,75 e P(X < 2,5) = 0,60.

b) P(X < 2,70) < 0,45 e P(X > 1,5) = 0,85.

j c) P(X = 1) = 0,15 e P(X = 2) = 0,30.
d) P(X = 3) = 0,55 e E(X) = 2,70.

j e) P(l,44 < X < 3) = 0,85 e Mo(X) = 3.

I

i Comentários:

: O enunciado informa que há apenas três valores possíveis: X = 1, X = 2 ou X = 3.

: Para conhecermos as probabilidades de cada valor, o enunciado informa os valores que a função de distribuição acumulada assume:
F(l,17) = P(X < 1,17) = 0,15.

O único valor menor ou igual a 1,17 é o valor X = 1. Ou seja:

P(X < 1,17) = P(X = 1) = 0,15

j Assim, concluímos que:

P(X = 1) = 0,15

j * F(2,76) = P(X < 2,76) = 0,45.

= Os valores menores ou iguais a 2,76 são X = 1 e X = 2, ou seja:

P(X < 2,76) = P(X = 1) + P(X = 2) = 0,45

i Sabemos que P(X = 1) = 0,15, logo:

P(X < 2,76) = 0,15 + P(X = 2) = 0,45

P(X = 2) = 0,30

E

j Isso nos permite concluir que a alternativa C está correta, mas vejamos as demais alternativas.

: Em relação à alternativa A, o valor de P(X > 1,79) pode ser calculado como:

P(X > 1,79) = 1 - P(X < 1,79) = 1 - P(X = 1) = 1 - 0,15 = 0,85

= E o valor de P(X < 2,5) é:

P(X < 2,5) = P(X = 1) + P(X = 2) = 0,15 + 0,30 = 0,45

j Logo, a alternativa A está incorreta.

I

: Em relação à alternativa B, o valor de P(X < 2,70) é:

P(X < 2,70) = P(X = 1) + P(X = 2) = 0,15 + 0,30 = 0,45
í Ou seja, P(X < 2,70) = 0,45 (não < 0,45).

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= E o valor de P(X > 1,5) pode ser calculado como:

P(X > 1,5) = 1 - P(X < 1,5) = 1 - P(X = 1) = 1 - 0,15 = 0,85

I

I

A segunda parte está correta, mas a alternativa B está incorreta, porque a primeira parte é falsa.

I

: Em relação à alternativa D, o valor de P(X = 3) é:
i

P(X = 3) = 1 - P(X = 1) - P(X = 2) = 1 - 0,15 - 0,30 = 0,55

: E o valor da esperança é:
i

E(X) = 1x0,15 + 2x0,30 + 3x0,55 = 0,15 + 0,60 + 1,65 = 2,40

A primeira parte está correta, mas a alternativa D está incorreta, porque a segunda parte é falsa.

I

: Em relação à alternativa E, o valor de P(l,44 < X < 3) é:
i

P(l,44 < X < 3) = P(X = 2) = 0,30

= E a moda de X (valor com maior probabilidade) é, de fato, Mo(X) = 3.

I

A segunda parte está correta, mas a alternativa E está incorreta, porque a primeira parte é falsa.

I

I

; Gabarito: C

Quartis e Mediana

A partir da função de distribuição acumulada, podemos calcular a mediana da distribuição. A mediana é,assim como a esperança e a moda, uma medida de tendência central, mas também uma medida separatriz,ou seja, que separa a distribuição em partes iguais.

Ela divide a distribuição em 2 partes iguais, de forma que 50% das observações fiquem abaixo dessa medida e 50% das observações fiquem acima. Portanto, a mediana é o valor de X para o qual a f.d.a. é igual a 50%.
TOME

NOTA!

FÇ.XMediana) 50% — 0, 5

Outras medidas separatrizes são os quartis da distribuição (0.1, Q2 e Q3), os quais dividem a distribuição em
4 partes iguais.

O primeiro quartil (Ql) deixa 25% das observações abaixo e 75%, acima; o segundo quartil (Q2) deixa 50%das observações abaixo e 50%, acima; e o terceiro quartil (Q3) deixa 75% das observações abaixo e 25%,acima. Note que a mediana equivale ao segundo quartil!

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, os valores da f.d.a. no primeiro, no segundo e no terceiro quartis são:

F(xq1) = 25% = 0,25

F(xq2) = F(xMed) = 50% = 0,5

F(xQ3) = 75% = 0,75

Para as variáveis discretas, pode não ser possível encontrar valores para x que separem a distribuição exatamente nesses percentuais. Nesses casos, devemos encontrar os valores de X para os quais a f.d.a.apresenta valores maiores (ou iguais) a esses percentuais:

F(xQ1) > 25%

F(xQ2) = F(xMed) > 50%

F(xQ3) > 75%

Para ilustrar, replicamos a tabela com os valores da f.d.a. (em percentual) para o lançamento do dado:
X F(x) = P(X < x)
1 16,7%

2 33,3%

3 50%

4 66,7%

5 83,3%

6 100%

Podemos observar que não há um valor de X para o qual a f.d.a. é exatamente igual a 25%. Por isso,escolhemos a probabilidade imediatamente superior, qual seja, de 33,3%, associada a X =
Item. 2. Com isso,
concluímos que o primeiro quartil é:

Xqi = 2

Também observamos que não há um valor de X para o qual a f.d.a. seja exatamente igual a 75%. Aprobabilidade imediatamente superior é de 83,3%, associada a X = 5. Logo, o terceiro quartil é

Xq3 = 5

Em relação à mediana, podemos observar que a f.d.a. para X = 3 é exatamente F(3) =
50%. Isso significa que xMed = 3 é um possível valor para a mediana. Entretanto, esse não é o único valor.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Lembra que a função acumulada é definida para qualquer valor de x? Pois é! Para todos os valores de x que pertencem ao intervalo [3,4)x, temos F(x) = 50%.
Sendo assim, podemos dizer que quaisquer desses valores são a mediana, inclusive o próprio 4. Entretanto,por convenção, normalmente consideramos o valor médio desse intervalo como a mediana:

3 + 4

Além dos quartis, há outros quantis, que dividem a distribuição em partes iguais, como os decis, que dividem em 10 partes iguais, e os percentis, que dividem em 100 partes iguais.
Calculamos esses quantis da mesma forma, a partir da função de distribuição acumulada.

I«** IX

(CESPE/2015 - Agente do Departamento Penitenciário Nacional)

Quantidade diária de incidentes (N)
Total

Frequência relativa
0,1

0,2

0,5

0,0

0,2

i Considerando os dados da tabela mostrada, que apresenta a distribuição populacional da quantidade diária de incidentes (N) em determinada penitenciária, julgue o item que se segue.

: O segundo quartil da distribuição das quantidades diárias de incidentes registradas nessa penitenciária é igual a 2.

; Comentários:

: A mediana é calculada a partir da função de distribuição acumulada, cuja tabela consta a seguir:

1 Utilizamos o parêntesis, ou o colchete voltado para fora, para indicar que o intervalo é aberto naquele extremo, o que significa que o extremo não está incluído no intervalo.
Utilizamos o colchete voltado para dentro para indicar que o intervalo é fechado naquele extremo, o que significa que o extremo está incluído.
Assim, a expressão [3,4) equivale a [3,4[ e representa o intervalo 3 < X < 4.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

X P(x)

0 0,1

1 0,2

2 0,5

3 0,0

4 0,2

F(x)
0,1

0,3

0,8

0,8

= Nesse exemplo, não temos nem um valor de X para o qual o valor de F(x) seja exatamente igual a
0,5. O valor

= imediatamente superior a 0,5 é de 0,8, o qual está associado ao valor X = 2.
Logo, o segundo quartil (ou i mediana) é xMed = 2.
= Gabarito: Certo.

I

i (FCC/2014 - TRT 19- Região) Seja F(x) a função de distribuição da variável X que representa o número de trabalhadores por domicílio em uma determinada população. Se:
= então, o número médio de trabalhadores por domicílio subtraído do número mediano de trabalhadores por domicílio é igual a j a) 0,15
b) 0,10

i c) 0,25

d) -0,15

í e) -0,50

i Comentários:

I

A média (ou valor esperado) de trabalhadores por domicílio é dada pela fórmula:

j F(X)=^xí.P(xí)

:
i

; Para aplicá-la, precisamos dos valores de probabilidade, a serem calculados a partir dos valores da função de distribuição acumulada:
P(X = 0) = F(0) = 0,10

j P(X = 1) = F(l) - F(0) = 0,25
- 0,10 =0,15

j P(X = 2) = F(2) - F(l) = 0,50
- 0,25 =0,25

j P(X = 3) = F(3) - F(2) = 0,80
- 0,50 =0,30

i p(X = 4) = F(4) - F(3) = 1 - 0,8 = 0,20

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, a média é dada por:

E(X) = 0 x P(X = 0) + 1 x P(X = 1) + 2 x P(X = 2) + 3 x P(X = 3) + 4 x P(X = 4)

£(%) = 1 x 0,15 + 2 x 0,25 + 3 x 0,30 + 4 x 0,20

F(X) = 0,15 + 0,50 + 0,90 + 0,80 = 2,35

A mediana é calculada a partir da função de distribuição acumulada. Pelo enunciado,
podemos observar que
F(x) = 50% para x G [2,3). Por convenção, temos:

A diferença entre a média e a mediana é:

Gabarito: D

F(x) — xM = 2,35 - 2,5 = -0,15

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

VARIÂNCIA E DESVIo PADRÃo

Nesta seção, veremos medidas de dispersão (ou variabilidade), que representam o quanto os elementos desviam em relação à média.
Variância

O desvio de um elemento x em relação à média /z é a diferença entre os seus valores:

Desvio = x - ju

Entretanto, ao somar os desvios de todos os elementos do conjunto, os desvios positivos (x > /z) anulam os desvios negativos (x < jiz), de modo que o resultado seria zero, tendo vista a própria definição de média.
Para ilustrar, vamos supor o seguinte conjunto de números {1, 1, 1, 1, 3, 7, 7}. A média desse conjunto é:
14-1 + 1 + 1 + 3 + 7 + 7 21

/z = - = — = 3

7 7

A soma dos desvios em relação à média é:

Soma Desvios = (1 — 3) + (1 - 3) + (1 - 3) + (1 - 3) + (3 — 3) + (7 — 3) + (7 — 3)

Soma Desvios = — 2 — 2 — 2 — 2 + 0 + 4 + 4 = 0
Assim, para que possamos somar os desvios, precisamos elevá-los ao quadrado antes.

Desvio quadrado = (x — ^tz)2

A variância é, portanto, definida como a média do quadrado dos desvios. Assim, em um conjunto de elementos, somamos o quadrado de todos os desvios e dividimos pela quantidade N de elementos, para obtermos a variância, que pode ser indicada como cr2:
=2 S(X - /Z)2

Para o nosso exemplo, temos:

(1 - 3)2 + (1 - 3)2 + (1 - 3)2 + (1 - 3)2 + (3 - 3)2 + (7 - 3)2 + (7 - 3)2

(—2)2 + (—2)2 + (—2)2 + (—2)2 + (O)2 + (4)2 + (4)2 _4 + 4 + 4 + 4 + 0 + 16 + 16_48

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação aos elementos repetidos, podemos multiplicá-los pela sua frequência.

Em outras palavras, podemos calcular a variância, somando os produtos dos desvios quadrados multiplicados pela sua frequência relativa:
a2 = (1 - S)2 x | + (3 - 3)2 x | + (7 - 3)2 x | = (-2)2 x | + (O)2 x | + (4)2 x |

, 4 2 16 + 32 48
a2 = 4x-+0 + 16x- =--------------- ----- = —

7 7 7 7

Genericamente, essa segunda forma de obter a variância pode ser representada pela seguinte fórmula, em que fr é a frequência relativa:
Y (x - /z)2 x fr

Para uma variável aleatória, a variância é calculada de maneira similar, porém, em vez da frequência relativa,utilizamos a probabilidade para cada valor x.

TOME

NOTA!

tr2 = £(x - fi)2 x P(x)

A variância da variável aleatória X pode ser denotada também por V(X) ou Var(X).

Vamos, então, calcular a variância para o nosso exemplo do dado equilibrado, em que os valores da variável são {1,2,3,4,5,6} com probabilidade P(X = x) = - para todos os elementos e média /z = 3,5.
1 1 1 1 1
1 135

= 6,25 x — + 2,25 x — + 0,25 x — + 0,25 x — + 2,25 x — + 6,25 x — = 17,5x — = ——
6 6 6 6 6
6 6 12

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

INDO MAIS

FUNDO!

A esperança de uma variável X é a soma dos produtos de cada valor de X pela sua probabilidade:
E(X) = £xxP(X = x)

Se substituirmos x por (x — /z)2, obtemos justamente a fórmula da variância:

E(X - ^2 = £(x - /z)2 x P(X = x)

Por isso, dizemos que a variância de uma variável aleatória é a esperança dos quadrados dos desvios:
a2 = E(X - ii)2

A variância também pode ser calculada da seguinte forma:

TOME

NOTA!

ff2 = E(X2) - n2

Considerando que /z = E(X), podemos escrever essa fórmula como:

o2 = E(X2) - [E(X)J2

O termo E(X2) representa a esperança dos valores da variável aleatória X, elevados ao quadrado, isto é, o produto de x2 pela sua probabilidade:
E(X2) = y x2 x P(X = x)

Vamos calcular a variância para o exemplo do lançamento do dado, utilizando a segunda fórmula:
a2 = E(X2) - /a2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O primeiro termo dessa fórmula é:

E(X2) = y X2 X P(X = x)

E(X2) = (1)2.1+ (2)2.1+ (3)2.1+ (4)2.i+ (5)2.i+ (6)2.1

6 6 6 6 6 6

z 1 1 1 1 1 1 91

E(X2) = i +4 +9 + 16 -+ 25.- + 36.- = —-

6 6 6 6 6 6 6

O segundo termo dessa fórmula (em fração) é:

A variância é dada pela diferença:

2 91 49 182 147 35

° 12" 12

Para essa segunda forma de cálculo, podemos utilizar, como apoio, a tabela de distribuição de probabilidade,com os valores de x e P(X = x), acrescentando duas colunas, uma com o valor da variável ao quadrado, x2,e outra com o produto x2. P(X = x).

A soma da última coluna será o resultado de E(X2>).

X P(X = x) X2

x2.P(X = x)

v

1 v6 1 4 6

2 v6 4 /ó

3 v 9 %

4 v6 16

2 /6

5 v6 25 %

6 v 36 3%

£(X2) = 6

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para calcular a variância, seguimos os seguintes passos:

i) Calcular a média: jU = E(X) = 2áXi.P(Xi);

ii) Elevar a média ao quadrado: jU2;

iii) Elevar os valores de X ao quadrado e multiplicá-los pela probabilidade: x2.P(X = x);

iv) Somar os resultados do passo iii para calcular F(X2) = Yá(Xi)2 P(%i);

v) Calcular a variância pela diferença (iv) - (ii): cr2 = E(X2) — p2.

Cuidado para não esquecer o último passo. Ou seja, não pense que o resultado do passo iv, E(X2), é a variância.
INDO MAIS

FUNDO!

Chamamos F(X2) de segundo momento (ou momento de segunda ordem) da variável aleatória. Também podemos chamar a variância de segundo momento central (ou momento central de segunda ordem) da variável aleatória.
I«** IX

í (2017 - DPE/PR)

Tabela - Distribuição da variável aleatória X

X P(X)

1 0,42

2 0,25

3 0,18

4 0,08

5 0,07

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Seja X uma variável aleatória discreta, sua esperança e variância são respectivamente:

a) Esperança = 2,00 e Variância = 2,13.

b) Esperança = 2,13 e Variância = 1,53

d) Esperança = 1,00 e Variância = 1,53

e) Esperança = 2,13 e Variância = 2,53

Comentários:

Vamos utilizar novamente a tabela de distribuição de probabilidade fornecida para calcular os valores de
/x = E(X) = YiXi-PÇXi) e de F(X2) = Sí(%í)2.P(xí):

X P(x) x.P(x) X2 x2.P(x)

1 0,42 0,42 1 0,42

2 0,25 0,50 4 1,00

3 0,18 0,54 9 1,62

4 0,08 0,32 16 1,28

5 0,07 0,35 25 1,75

Total 1,00 2,13 - 6,07

i Portanto, temos = EQO = 2,13, então, /z2 = 4,54; e E(X2) = 6,07.
I

: Assim, a variância é:

<j2 = E(X2) - /z2 = 6,07 - 4,54 = 1,53

j Gabarito: B

(VUNESP/2014 - TJ/PA) Em uma locadora de automóveis a demanda diária é uma variável aleatória com a seguinte distribuição de probabilidades:
Automóveis X; 0 1 2 3 4 5

Probabilidade 0,10 0,10 0,30 0,30 0,10 0,10

A variância da demanda diária é:
a) 1,85.

b) 1,5.

c) 1,25.

d) 1,0.

e) 0,85

Comentários:

A variância pode ser calculada como:

K(X) = E(X2) - [£(X)J2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vamos utilizar a tabela para calcular o valor de E(X):

Xi
P(Xi)
Xi.PÍXi)

E

0,1

0x0,1 =0

0,1

1x0,1 =0,1

0,3

2x0,3=0,6

0,3

3x0,3=0,9

0,1

4x0,1 =0,4

0,1

5x0,1 =0,5

; Sabendo que E(X) é a soma de Xj.P(Xj), temos:

E (X) = 0 x 0,1 + 1 x 0,1 + 2 x 0,3 + 3 x 0,3 + 4 x 0,1 + 5 x 0,1

i £(X) = 0 + 0,1 + 0,6 + 0,9 + 0,4 + 0,5 = 2,5

: Logo, o quadrado de E(X) é:

Í [F(X)]2 = (2,5)2 = 6,25

= Agora, vamos calcular E(X2\.

X 0 1 2 3 4

(X)2 0^0 1²=1 22=4 3²=9 42=16
52=25

P(X) 0,1 0,1 0,3 0,3 0,1
0,1
(X)2.P(X) 0x0,1 =0 1x0,1 =0,1 4x0,3=1,2 9x0,3=2,7 16x0,1=1,6 25x0,1=2,5

: Sabendo que E(X2) é a soma de Xj2.P(Xj), temos:

F(X2) = 02 x 0,1 + l2 x 0,1 + 22 x 0,3 + 32 x 0,3 + 42 x 0,1 + 52 x 0,1

£(X2) = 0 x 0,1 + 1 x 0,1 + 4 x 0,3 + 9 x 0,3 + 16 x 0,1 + 25 x 0,1

F(X2) = 0 + 0,1 + 1,2 + 2,7 + 1,6 + 2,5 = 8,1

: Assim, a variância é:

; Gabarito: A

V(X) = 8,1 - 6,25 = 1,85

i (2019 - IF-PA) Uma variável aleatória discreta Z tem função de probabilidade dada por:

Z _2 -1 0 1 2

P(Z) 0.3 0.1 0.2 0.3 0.5

I

i Pode-se afirmar que a variância da variável aleatória Z é igual a:

Í a) 2,64

b) 3,00

í c) 3,24

d) 4,64

Í e) 2,84

i Comentários:

I

í Vamos utilizar a tabela de distribuição de probabilidade fornecida para calcular os valores de = E(Z) =
i TãZt. P(zí) e de F(Z2) = ^i(Zi)2.P(Zj). Atente-se que a tabela abaixo está em um formato diferente
= daquele que vimos antes (está transposta), para acompanhar a tabela do enunciado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

z -2 -1 0 1 2 Total

P(Z)

0,3

0,1

0,2

0,3

0,5 1

Z.P(Z)

-0,6

-0,1 0

0,3

1 0,6

z2 4 1 0 1 4 -

z2.P(Z)

1,2

0,1

0 0,3

2 3,6

Portanto, temos = E(Z) = 0,6, então, [i2 = 0,36; e E(Z2) = 3,6.
Assim, a variância é:

a2 = F(Z2) - n2 = 3,6 - 0,36 = 3,24

Gabarito: C

(FGV/2022 - SEFAZ/AM) Uma variável aleatória X tem a seguinte função de probabilidade,
sendo k uma constante:
A variância de X é igual a:
a) 1,8

b) 2,0

Í c) 2,2

d) 2,4

e) 2,6

X

p(x)

-2,0

0,2

-1,0

0,1

0,0

0,4

1,0 2

0,1 k i Comentários:
: Para calcular a variância, precisamos do valor de k e da esperança.

= Sabendo que a soma das probabilidades é igual a 1, o valor de k é dado por:

0,2 + 0,1 + 0,4 + 0,1 + /c = 1

k = 1 - 0,8 = 0,2

= Assim, a esperança é:

£(%) = (-2) x 0,2 + (-1) x 0,1 + 0 x 0,4 + 1 x 0,1 + 2 x 0,2

í
= -0,4 - 0,1 + 0 + 0,1 + 0,4 = 0

; Agora, precisamos calcular os desvios de cada valor de x em relação à média (que será igual ao próprio valor da variável) e elevar cada desvio ao quadrado.

: Em seguida, multiplicamos cada quadrado pela respectiva probabilidade e somamos todos os resultados:I

i
VOO =\[X - E(X)]2 x P(X = x)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Esses cálculos constam na tabela a seguir:

X -2,0 -1,0 0,0 1,0 2

P(x) 0,2 0,1 0,4 0,1 0,2

x-E(X) -2 -1 0 1 2

[x-E(X)]2 4 1 0 1 4

[x-E(X)]Lp(x) 0,8 0,1 0 0,1 0,8

A variância é a soma dos resultados da última linha:

= 0,8 + 0,1 + 0 + 0,1 + 0,8 = 1,8

Gabarito: A

(2012 - Empresa de Pesquisa Energética) Sejam X e Y variáveis aleatórias independentes.
Sabendo-se que:

E (X) = 2; E(X2Y) = 8; E(XY2) = 6 e E ((XY)2) = 24, conclui-se que o valor da variância de Y, Var
(Y), é a) 48
b) 24

c) 10

d) 3

e) 2

Comentários:

Sendo X e Y variáveis independentes, então vale a propriedade multiplicativa da esperança:

E(XY) = E(X).E(Y)

Sabendo que E(X) = 2 e que E(XY2) = 6, então:

E(X.Y2) = E(X).E(Y2) = 2,E(Y2) = 6
E(Y2) = 3

Considerando esse resultado e sabendo que E((XY)2) = 24, então:

E((XY)2) = E(X2.Y2) = E(X2).E(Y2) = E(X2).3 = 24
E(X2) = 8

Considerando esse resultado e sabendo que E(X2Y) = 8, então:

E(X2Y) = E(X2).E(Y) = 8.E(Y) = 8
E(Y) = 1

Sabendo que E(Y2) = 3 e E(Y) = 1, podemos calcular a variância, por:

VAR (Y) = E(Y2) - [E(Y)]2 = 3-1 = 2

Gabarito: E

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Desvio Padrão

Ao utilizarmos os quadrados dos desvios, perdemos um pouco a noção da grandeza dos resultados. Se estivermos interessados na altura dos brasileiros, por exemplo, a média adulta masculina seria algo em torno de 173cm e a variância, 400cm2, por exemplo. Analisando somente esses números, não entendemos muito bem o que 400cm2 querem dizer.
Por isso, existe o conceito do desvio padrão, que representamos por o, D(X) ou DP(X),
definido como a raiz quadrada da variância:
Nesse exemplo hipotético, o desvio padrão seria de:

cr = V400 = 20cm

Ora, esse resultado é bem mais palatável - ele indica que uma boa parcela da população adulta masculina tem altura entre 153cm e 193cm. Agora, o quanto uma "boa parcela" representa depende de alguns fatores.Então, aguarde cenas dos próximos capítulos!

7 35

Para o nosso exemplo da moeda equilibrada, em que calculamos a variância o = —, o desvio padrão é a raiz quadrada desse valor:
Variância e Desvio Padrão Amostrais

Podemos calcular a variância e o desvio padrão a partir de amostras, isto é, utilizar os dados obtidos em amostras para estimar a variância ou o desvio padrão da população de interesse.
Para isso, considerando uma amostra de tamanho n (isto é, com n observações), primeiro calculamos a média da amostra, que denotamos por x:
n

Para calcular a estimativa da variância, que denotamos por s2, dividimos a soma do quadrado dos desvios
£(x — x)2 porn - 1:

E(x-x)2

n-1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Observe que essa fórmula é bastante similar à variância populacional, com a seguinte diferença: no cálculo da variância populacional, dividimos pelo total da população N e, no cálculo da variância amostrai (isto é,para estimar a variância, a partir dos dados da amostra), dividimos por n — 1.

Vamos supor que o conjunto que vimos anteriormente, {1,1,1,1, 3, 7, 7}, represente os números observados em uma amostra, obtidos a partir de determinada população. Assim, para estimar a variância da população,a partir dessa amostra, utilizamos a fórmula:

7 H%-%)* 2

s =---------n--—--- i1—

Já calculamos a média desse conjunto: x = 3. Então a estimativa da variância é:

Çz =

(1 - 3)2 + (1 - 3)2 + (1 - 3)2 + (1 - 3)2 + (3 - 3)2 + (7 - 3)2 + (7 - 3)2

(—2)2 + (—2)2 + (—2)2 + (—2)2 + (O)2 + (4)2 + (4)2

4 _l_ 4 _l_ 4 _l_ 4 _l_ 0 + 16 + 16 48

l«** IX

(FCC/2015 - SEFAZ/PI - Adaptada) Julgue a seguinte afirmativa:

= As amostras I e II dadas abaixo possuem a mesma variância amostrai igual a 10.

B

í Amostra 1:1 3 5 7 9 Amostra II: 1113 15 17 19

I

; Comentários:

I

: Para calcular a variância amostrai da Amostra I, primeiro calculamos a média da amostra:

I

= 1 + 3 + 5 + 7 + 9

%i =------- =
= — = 5

n 5

= Logo, a variância amostrai da Amostra I é dada por:

: S(X-X)2

n — 1

s

, (1 - 5)2 + (3 - 5)2 + (5 - 5)2 + (7 - 5)2 + (9 - 5)2 *
16 + 4 + 0 + 4 + 16

Sl 4

..

— = 10

; Para calcular a variância amostrai da Amostra II, começamos pelo cálculo da média:

I

i £% 11 + 13 + 15 + 17 + 19

: n 5

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

* 05152001900 - Everton
Murilo Vieira

A variância amostrai da Amostrai II é, portanto, dada por:

(11 - 15)2 + (13 - 15)2 + (15 - 15)2 + (17 - 15)2 + (19 - 15)2

= 4

9 16 + 4 + 0 + 4 + 16 40

= 4 =4=10

Portanto, as amostras I e II possuem a mesma variância amostrai, igual a 10.

Resposta: Certo.

Propriedades

Agora, veremos as propriedades da variância e do desvio padrão, que são aplicáveis tanto a variáveis aleatórias discretas, quanto a variáveis contínuas.
Nos enunciados a seguir, consideramos X e Y variáveis aleatórias e k uma constante real qualquer,

i) V(X + fc) = V(X)

Quando somamos uma constante k a uma variável X, a variância de X não se altera.

Por exemplo, para k = 2 e V(X) = —, a variância de X + 2 será:

z- *\ Z . 35

V(X + 2) = V(X) = —

INDO MAIS

FUNDO!

Vamos entender o porquê disso, com base no exemplo do dado. Sabendo que a média é

/z = 3,5, vamos replicar o início do cálculo da variância, pela primeira fórmula:

V(X) = Z(* - ^)2 x P(X = x)

V(X) = (1 - 3,5)2.i +O(2 - 3,5)2.| + (3o - 3,5)2.| + (4 -o3,5)2.| + (5 - 3,o5)2.i + (6 - 3,5)2.|
o

V(X) = (-2,5)2 i + (-1,5)2 j + (-0,5)2.i + (0,5)2.| + (1,5)2.| + (2,5)2 j

6 6 6 6 6 6

Agora, vamos supor que Y represente um dado igualmente equilibrado, cujas faces variam de Y = 3 até Y = 8. Ou seja, somamos k = 2 às faces do dado X:
Y = X + 2 = {3, 4, 5, 6, 7, 8}

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A média (ou esperança) de Y será:

E (r) = 3x- + 4x-+5x-+6x-+7x- + 8x- = — = 5,5

6 6 6 6 6 66

E a variância será calculada como:

V(Y') = (3 - 5,5)2.i +o(4 - 5,5)2.i + (o5 - 5,5)2.| + (6 -o5,5)2.| + (7 - 5o,5)2.| + (8 - 5,5)2.i o
7(7) = (-2,5)2 i+ (-1,5)2 (-0,5)2.|+ (0,5)2.|+ (1,5)2
(2,5)2 j

6 6 6 6 6 6

Observe que os desvios y — E(Y) são exatamente os mesmos de x — EÇX),
e as probabilidades P(Y = y) são as mesmas de P(X = x). Como o cálculo é o mesmo, o resultado, isto é, a variância, será igual.
Isso acontece porque, ao somarmos a constante k = 2 aos valores de X, a média também sofre esse mesmo acréscimo (essa é uma propriedade da esperança):
£(7) = E(X + 2) = £(%) + 2

Consequentemente, os desvios y — E(Y) são iguais aos x — E(X\.

y - EÇY') = (x + 2) - [E(X) - 2] = x + 2 - £(X) - 2 = x - £(X)

Por isso, as variâncias são iguais!

Essa propriedade vale também quando subtraímos uma constante k (trata-se da mesma propriedade, pois podemos considerar que estamos somando -fc):
V(X - k) = 7(X)

Então, para esse mesmo exemplo de 7(X) = —/ a variância de X - 4 será:

* 35

V(X - 4) = 7(X) = —

Por ser a raiz quadrada da variância, que não se altera, o desvio padrão também permanece o mesmo:

D(X + fc) = D(X)

D(X — fc) = D(X)

ii) 7(/í.X) =/<2.7(X)

Quando multiplicamos uma variável por uma constante, a variância é multiplicada pelo quadrado dessa constante.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por exemplo, para k = 2 e V(X) = — a variância de 2.X será:

7(2. X) = 22.7(X) =

T

INDO MAIS

FUNDO!

Vamos, novamente, entender o porquê disso, mas agora vamos supor que Y represente os valores de X multiplicados por 3:
Y = 3.X

Pelas propriedades da esperança, a média de Y será multiplicada por 3:

F(y) = F(3.X) = 3 x F(X)

E os desvios serão multiplicados por 3:

y - E(T) = (3. x) - [3. F(X)] = 3. [x - F(X)]

Ao elevarmos esses desvios ao quadrado, os resultados serão multiplicados por (3)2:

(y - F(n)2 = (3. [x - E(X)])2 = (3)2. ([x - E(X)])2

Por isso, a variância é multiplicada pelo quadrado da constante!

Essa propriedade também vale para a divisão por uma constante k (podemos considerar que estamos multiplicando por^):
Não importa se k é positivo ou negativo, pois o seu quadrado será sempre positivo.

Por exemplo, para Y = a variância de X é dividida por (—2)2 = 4. Sendo V(X) = —, teremos:

(-2)2

1 35 35

412 T

Como o desvio padrão é a raiz quadrada da variância, o desvio padrão do produto k.X, é:

D(k.X~) = yjVÇk.X) = y/k2.V(X) = \k\.DÇX)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Como a raiz de um número é sempre um número positivo, então a raiz de k2 é o módulo de k, denotado por |/c|:
O módulo de k, \k|, é uma "versão positiva" do número k, ou seja:

k, se k > 0 |

—k,se k < Oj
Por exemplo, se k = 3, então |k| = 3 e se k = -3, então |/c| = 3.

Portanto:

D(k.X) = k.DÇX), para k > 0
D(k.X) = -k.D(X), para k < 0

D®=^,para„0

Dg) = _T,parak<o

Por exemplo, para Y = 3.X, o desvio padrão será:

E para Y = x

2'

o desvio padrão será:

D(Y) = D(3.X) = 3.D(X)

D(y)=D(2L)=

iii) V(fc) = 0

A variância de uma constante qualquer é zero. Por exemplo, a variância da constante k = 3 é:

V(3) = 0

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

INDO MAIS

FUNDO!

Pelas propriedades da esperança, a média de uma constante k:

/j. = E(k) = k

Assim, o desvio k — /z será:

desvio = k — /j. = k — k = 0

Por isso, a variância será 0.

Consequentemente, a variância e o desvio padrão de uma constante são iguais a zero: D(k) = 0

iv) Se X e Y são independentes, então V(X + F) = V(X) + V(F)

Somente se X e Y forem variáveis aleatórias independentes, poderemos concluir que a variância da soma das variáveis é igual à soma das variâncias (propriedade aditiva).
EXEMPLIFICANDO

Vamos supor que X represente os resultados do lançamento de um dado normal
(equilibrado, com faces de 1 a 6) e que Y represente os resultados do lançamento do dado equilibrado com faces de 3 a 8. Assim, se lançarmos os dois dados ao mesmo tempo,qual será a variância da distribuição da soma dos resultados?
Já calculamos as variâncias de X e Y em exercícios anteriores:

7(y) = = ||

Sendo X e Y variáveis independentes, pois um lançamento não influencia no outro, a variância da distribuição de X + Y, é:
v(x) + 7(y) = — + — =

V 7 12 12

? 35 _ 35

12 " 6

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Além disso, se X e Y forem independentes, a variância da diferença X - Y também é a soma das variâncias:
v(x - r) = v(x) + v(K)

Para variáveis independentes, temos V(X ± K) = 7(X) + VÇY'), porém o contrário não é necessariamente verdadeiro. Ou seja, é possível verificar que V(X ±Y~) = V(X)+ V(Y') e as variáveis não serem independentes.
i) V(X ± k) = V(X)

ii) V(fc.X) = k2.V(X)

iii) V(fc) = 0

iv) Se X e Y forem independentes, então V(X ± F) = V(X) + V(K)

l«** IX

..................................................................... ........................... f i (2016 - Instituto Federal de Educação/BA - Adaptada) Sendo X uma variável aleatória,com variância cr2, i

= então a variância da função Y = a + bX, com a e b G R, é j a) V(Y) = b2
b) V(Y) = a + b i c) V(Y) = o2
d) V(Y) = b2o2

i e) V(Y) = a2 + b2

I

i Comentários:

I

: Pelas propriedades da variância, temos:
i

V(Y) = V(a + bx) = b2.V(X)

I

I

i Como a variância de X é V(X) = cr2, então a variância de Y é:
i

V(Y) = b2c>2

i

:

; Gabarito: D.

I

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= (FGV/2017 - IBGE - Adaptada) Para o caso de variáveis aleatórias quaisquer, existem diversas propriedades =Ique se aplicam diretamente à esperança matemática e ao momento central de segunda ordem. Dentre essas ;
= propriedades está:

a) Var(X) > E(X2)

b) Var(X±Y) = Var(X) ± Var(Y)

: c) DP(a) = 0, sendo a uma constante qualquer
;

I

d) Var(a.X) = a.Var(X), sendo a uma constante positiva i
: e) DP(a.X) = a.DP(X), sendo a uma constante qualquer
;

I

i Comentários:

I

: Em relação à alternativa A, podemos calcular a variância como:
i

Var(X) = E(X2) - [E(X)]2

I

: Como [E(X)]2 > 0 para qualquer variável X, então, temos:
i

Var(X)< E(X2)

: Portanto, a alternativa A está incorreta. Em relação à alternativa B, se X e Y forem independentes, então i podemos afirmar que:i

Var(X± Y) = Var(X) + Var(Y)

I

: Logo, a alternativa B está incorreta por 2 motivos:
i

I

i) Não pode considerar a propriedade aditiva da variância, Var(X ± Y) = Var(X) +
Var(Y), pois o enunciado não ;

: afirmou que X e Y são independentes.
j

I

: ii) Ainda que X e Y fossem independentes, a variância da diferença de X e Y
seria igual à soma das variâncias: i i Var(X - Y) = Var(X) + Var(Y)i

: Em relação à alternativa C, sabemos que a variância e o desvio padrão de uma constante "a"
qualquer são j iguais a zero.
i

DP(a) = 0

= Portanto, a alternativa C está correta. Em relação à alternativa D, sabemos que para uma constante "a" i
: qualquer:

Var(a.X) = a2.Var(X)

= Portanto, a alternativa D está incorreta. Em relação à alternativa E, sabemos que para uma constante "a" i
; qualquer, temos:

DP(a.X) = | a | .DP(X)

I

I

: Assim, sendo a uma constante positiva então:

DP(a.X) = a.DP(X)

I

I

: Sendo a uma constante negativa então:

DP(a.X) = -a.DP(X)

I

i Portanto, temos equações distintas para constantes positivas e negativas, logo a alternativa E está incorreta, iI

I

: Resposta: C.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

CoVARIÂNCIA E CoRRELAçÃo

As medidas que estudaremos nesta seção representam a relação entre duas variáveis aleatórias. Variáveis relacionadas são aquelas em que o resultado de uma influencia o resultado de outra,ou seja, essas variáveis não são independentes.
Por exemplo, a altura de uma criança é dependente da altura de seus pais; o volume de água em uma caixa d'água se tem relção com o seu peso; a demanda de certo produto varia de acordo com o seu preço.
Há variáveis fortemente relacionadas, como o volume e o peso de água, e outras nem tanto, como a altura dos pais e a altura dos filhos. Também existem variáveis que se relacionam em um mesmo sentido (quanto mais altos são os pais, mais altos os filhos tendem a ser) e variáveis que se relacionam em sentidos opostos(quanto maior o preço, menor a demanda).

No gráfico abaixo, ilustramos um exemplo hipotético de duas variáveis que se relacionam no mesmo sentido,
como a altura dos pais e a altura dos filhos.

1,55

Altura dos Pais X Altura dos Filhos

1,45 * s-

* *

1,4 *

* *

1,35 *

13 *

1,25 *

1,2

1,65 1,7 1,75 1,8 1,85 1,9 1,95 2 2,05

No gráfico a seguir, ilustramos um exemplo hipotético de duas variáveis que se relacionam em sentidos opostos, como o preço de um produto e a quantidade adquirida.
Preço X Quantidade Comprada

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A covariância e a correlação caracterizam tanto a força da relação entre duas variáveis, quanto a sua orientação (se variam no mesmo sentido ou em sentidos opostos).
A covariância entre duas variáveis aleatórias X e Y, representada por Cov(X, y), é, por definição:

Cov(x, y) = E[(X - (y - nYy\

Nessa expressão, corresponde à média (esperança) da variável X, e [iY corresponde à média de Y.
A covariância também pode ser calculada como:

TOME

NOTA!

Cov(x, y) = e(x. y) - e(x). E(y)

Nessa fórmula, E(X. K) corresponde ao seguinte:

E(X- y) = y x. y. p(x, y)

Ou seja, multiplicamos os possíveis valores das variáveis pelas probabilidades correspondentes.
Se os valores forem igualmente prováveis, podemos calcular E(X. y) como:

E(X.y)

Zx.y

N

Por exemplo, vamos considerar uma parte dos dados hipotéticos do gráfico Preço X
Quantidade Comprada,
conforme indicado na tabela abaixo.

Para calcular a covariância, podemos criar uma nova coluna com o produto das duas variáveis, o que permitirá calcular E(X.Y).
i ii iii iv
Total

X: Preço

1,50

2,00

3,00

5,00

11,50

Y: Qtdade

X.Y

Como esses valores são igualmente prováveis, o valor de E(X.Y) pode ser calculado como:

, x Sx.y 165

e(X y) = == —= 41'25

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, calculamos E(X) e E(Y), isto é, a média de X e de Y:

A covariância será, portanto:

Cov(X,y) = 41,25 - 2,875 x 19,25 = -14

Nesse caso, obtivemos uma covariância negativa. Isso ocorreu porque as variáveis se relacionam em sentidos opostos (relação negativa), isto é, quando uma aumenta, a outra diminui, em média.
Quando a covariância das variáveis é positiva, elas variam no mesmo sentido (relação positiva), isto é,quando uma aumenta, a outra também aumenta, em média.

Para calcular a covariância, podemos seguir os seguintes passos:

i) Multiplicar os valores de X e Y;

ii) Somar os produtos X.Y e dividir por N para obter E(X. Y) =

iii) Calcular as médias E(X) = — e E(Y) = — e multiplicá-las;

iv) Subtrair o resultado de ii pelo resultado de iii para obter a covariância.

Entretanto, a força da relação entre duas variáveis é difícil de interpretar a partir da covariância. Em relação ao nosso exemplo, uma covariância de -14 indica uma forte relação negativa ou uma fraca relação?
Para isso, há o conceito de correlação (ou coeficiente de correlação), indicado por p,
em que dividimos a covariância pelo desvio padrão de ambas as variáveis.
TOME

NOTA!

p(x, v) =Cov(X,Y)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para calcular o desvio padrão (populacional) para as variáveis do nosso exemplo, vamos utilizar a seguinte fórmula da variância:
V(X) = E(X2) - [E(X)]2

Para isso, vamos criar uma coluna com os valores de X2 e Y2:

i ii iii iv
Total

X: Preço

1,50

2,00

3,00

5,00

11,50

Y: Qtdade

X2

2,25

40,25

Y2

1929

Os valores de FQY2) e E(Y2} são, portanto:

, S%2 40,25

E(X2) =

£(y2) = y

N

y v2 1929

« —= 482'25

Sabendo que EÇX2) = 10,06 e que E(X) = 2,875, então a variância de X é:

E o desvio padrão de X é:

ax = yi8Õ = 1,34

Em relação a Y, sabendo que E(Y2') = 482,25 e que E(Y) = 19,25, então a variância e desvio padrão são:7(r) = E(Y2) - [E(y)]2 = 482,25 - [19,25]2 = 482,25 - 370,56 = 111,69

ay s V111-69 = 10,57

Portanto, o coeficiente de correlação para o nosso exemplo é:

p(X,Y) =

Cov(X, K) -14

1,34 x 10,57

-0,99

Com base nesse valor, podemos concluir que a relação negativa entre as variáveis é muito forte, pois o valor do coeficiente de correlação é próximo de -1.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vamos com

TUDoI

A fórmula do coeficiente de correlação também pode ser representada como:

Em que o numerador é igual à covariância multiplicada por n e o denominador é igual ao produto dos desvios padrão, também multiplicado por n.
Vamos verificar isso! A covariância pode ser representada como:

Cov(X,Y) = E(X.Y) -E(X).E(Y) - x.y = ;(2x.y - n.x.y)

E os desvios padrão são a raiz quadrada da variância:

a* = = JE(X2) - [E(X)]2 = - % = pEx2-n.x)

= 7F(r2) - [£(D]2 = J^-y = J;(Sy2-n.y)

Dividindo a covariância pelo produto dos desvios padrão, obtemos a fórmula acima!

O coeficiente de correlação mede a força e a orientação com que duas variáveis se relacionam linearmente,
podendo assumir valores no intervalo [-1,1].

Assim, como para a covariância, valores positivos do coeficiente de correlação indicam uma relação entre as variáveis no mesmo sentido (relação positiva) e valores negativos indicam relação em sentidos opostos(relação negativa).

Além disso, quando p = 1, há uma correlação linear perfeita positiva, ou seja, as variáveis apresentam uma relação linear entre si da forma Y = aX + b, sendo a e b reais e a > 0. É o caso do volume de água e do peso da caixa d'água.
Quando p = —1, há uma correlação linear perfeita negativa, ou seja, as variáveis apresentam uma relação linear entre si da forma Y = aX + b, sendo a e b reais e a < 0. Um exemplo dessa relação seria o peso da caixa d'água e o seu espaço disponível.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vejamos agora qual valor a covariância assume quando as variáveis são independentes. Sendo X

variáveis independentes, sabemos que:

£(x.y) = £(x).E(y)
Portanto, a covariância de duas variáveis independentes é:

CovÇx, y) = e(x. y) - £(%). E(y) = £(%). £(y) - e(x). F(y) = o

Consequentemente, o valor do coeficiente de correlação para variáveis independentes também é p =

Porém, é possível ter Cov = 0, p = 0 e as variáveis não serem independentes.

Existe uma exceção para essa regra!

Para variáveis binárias, isto é, que assumem apenas 2 valores, a covariância nula implica na independência dessas variáveis! Em outras palavras, se a covariância entre 2variáveis binárias for nula, podemos garantir que essas variáveis são independentes.
ESQUEMATIZANDO

Cov(X,y) = E(X.Y) - E(X).E(T)

p(X,Y) ⁼ c_o^npE

Gx-ryy

Variáveis X e Y Independentes -> CovÇX, K) = 0, p(X, 7) = 0

Cov(X, 7) > 0, p(X, y) > 0 «-» Relação positiva (XeY variam no mesmo sentido)
Cov(X, y) < 0, p(X, y) < 0 <-* Relação negativa (X e Y variam em sentidos opostos)
p(X, y) = 1 <-> relação linear perfeita positiva ^>Y = aX + b,a> 0

p(X, y) = —1 <-> relação linear perfeita negativa ^Y = aX + b, a < 0

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (2018 - UFRGS) A análise depermite estudar a relação entre dois conjuntos de valores e i quantificar o quanto um está relacionado com o outro, no sentido de determinar a intensidade e a direção j dessa relação. Isto é, essa análise indica se, e com que intensidade, os valores de uma variável aumentam ou i diminuem enquanto os valores da outra variável aumentam ou diminuem.;

= Assinale a alternativa que completa corretamente a lacuna do texto acima.

i a) correlação i
I

I

b)dispersão i
= c) classificação

I

d) agrupamento i
I

i e) regressão i
; Comentários:

I

: O conceito que estuda a relação entre duas variáveis, representando tanto a força dessa relação quanto o i seu sentido, é a correlação.i

: Gabarito: A

I

(2015 - PC/GO) Com o intuito de avaliar possíveis correlações entre variáveis, um gráfico de dispersão pode j ser um aliado na tomada de decisão. Esse gráfico, elaborado no eixo cartesiano, plota resultados das i variáveis estudadas a fim de representá-las conjuntamente. Sejam x e y variáveis referentes a "tempo de i experiência" e "tempo de execução de tarefa", respectivamente, e analisando o gráfico de dispersão j apresentado, assinale a alternativa correta.i

* * * * w * * * **

8 10 12 14

Tempo de experiência (anos)

a) É observada uma correlação positiva perfeita entre as variáveis.

b) É observada uma correlação positiva entre as variáveis.

c) É observada uma correlação nula entre as variáveis.

I

d) É observada uma correlação negativa entre as variáveis.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= e) É observada uma correlação negativa perfeita entre as variáveis..

i Comentários:

I

: Pelo gráfico, observamos que as variáveis se relacionam em um mesmo sentido,
portanto a correlação é

= positiva. Porém, essa relação não é perfeitamente linear, por isso a correlação não é perfeita.

= Gabarito: B

I

; (FCC/2015 - SEFAZ/PI - Adaptada) Julgue as seguintes afirmações:

; I - Se r é o coeficiente de correlação linear entre duas variáveis, então -1 < r < 1.

: II - Se duas variáveis X e Y apresentam correlação linear inversa, o coeficiente de correlação linear entre elas i será um número negativo menor do que -1.
j Comentários:

: Em relação à afirmação I, o coeficiente de correlação varia entre [-1,1]. Portanto, a afirmação I
está correta.

: Em relação à afirmação II, se X e Y se relacionam de forma inversa, então o coeficiente de correlação é
= negativo. Porém, como o menor valor para o coeficiente é -1, o coeficiente será um valor negativo maior ou igual a -1, não menor do que -1. Portanto, a afirmação II está incorreta.
Ê Resposta: I - Certo; II - Errado.

(CESPE/2016 - TCE/PR) Se satisfação no trabalho e saúde no trabalho forem indicadores com variâncias populacionais iguais a 8 e 2, respectivamente, e se a covariância populacional entre esses indicadores for igual a 3, então a correlação populacional entre satisfação no trabalho e saúde no trabalho será igual a a) 0,8125.
b) 1.

c) 0,1875.

d) 0,30.

e) 0,75.

Comentários:

Sabendo que V(X) = 8, V(Y) = 2 e Cov(X,Y) = 3, então a correlação é dada por:

Cov(X, 7)

Gabarito: E

p(U)

Ox.ffy i (2018 - FUNPAPA) Um pesquisador suspeita que existe uma correlação entre o número de promessas que
; um candidato político faz e o número de promessas que são cumpridas uma vez que o candidato é eleito.
= Ele acompanha vários políticos proeminentes e registra as promessas feitas (X) e as promessas mantidas (Y).
= Utilizando os seguintes dados sumarizados, calcule o coeficiente de correlação entre as promessas feitas e
= as promessas mantidas e assinale a alternativa correta.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

=280. =2S, yV[=Mí'. £*'-12400 e Í>? = 140.

1-L T-L í-l l-l a) O coeficiente de correlação entre as promessas feitas e as promessas mantidas indicam uma correlação forte e positiva.
b) O coeficiente de correlação entre as promessas feitas e as promessas mantidas indicam uma correlação fraca e negativa.
c) O coeficiente de correlação entre as promessas feitas e as promessas mantidas indicam uma correlação forte e negativa.
d) O coeficiente de correlação entre as promessas feitas e as promessas mantidas indicam uma correlação fraca e positiva.
e) O coeficiente de correlação entre as promessas feitas e as promessas mantidas indicam uma correlação r « 0,5.
Comentários:

O coeficiente de correlação é calculado por:

A covariância pode ser calculada por:

z , Cov(X,y)

P(x,y) = —-—- ox.oy

CovÇx, y) = e(x. y) - £(%). E(y)

O enunciado informa que E x.y = 940 e n = 7, logo:

. x Xx.y 940

n 7

O valor de E(X) pode ser calculado a partir da informação de que E x = 280, logo:

. . E% 280
F(X) = — = —

n 7

O valor de E(Y) pode ser calculado a partir da informação de que Ey = 28, logo:

Assim, o valor da covariância é:

£(y) = ^- = — = 4

n 7

z x 940 280 940 1120 180

Cov(X,y) =—-------------- — x4 = — = s 25,7

7 7 7 7 7

Para calcular o coeficiente de correlação, vamos primeiro calcular a variância de X utilizando fórmula:
a seguinte

O enunciado informa que E x2 = 12400, logo:

K(X) = E(X2) - [£Q0]2

12400

Sabendo que E(X) = — = 40, então a variância de X é:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= E o desvio padrão de X é:

z x 12400 , 12400 11200 1200

Vtf) = —------------ 40i) 2 = — — = ——

7 7 7 7

I

: O enunciado informa que £ y2 = 140, logo:

:

s f(y )=±±2_ = = 20
: n

I

: Sabendo que E(Y) = 4, então a variância de Y é:

7(y) = 20 - 42 = 20 - 16 = 4

: E o desvio padrão de Y é:
I

= Assim, o coeficiente de correlação é:

0% = V4 = 2

i z x Cov(X,K) -25,7

i p(X, y) =---------- ------- - =
= -0,98
13,1 x 2

= Como -0,98 é muito próximo de -1, há uma correlação forte e negativa.

I

i Gabarito: C

L...

A

Propriedades

Veremos agora propriedades da covariância e da correlação, que valem tanto para variáveis discretas,quanto para variáveis contínuas. Nesta seção, deduziremos algumas propriedades para que você possa escolher se prefere deduzi-las ou memorizá-las.
A seguir, consideramos X, Y e Z variáveis aleatórias e k uma constante real qualquer.

i) Cov(X,Y') = Cov(Y,X)

A covariância é considerada uma medida simétrica, pois não importa qual é a variável que aparece primeiro.De fato, a fórmula da covariância é composta por produtos e, por isso, a ordem das variáveis é indiferente:
Cov(X,Y) = EÇX.Y)-EÇX\E(Y) = E(K. X) - E(Y). E(X) = Cov(Y,X)

Pelo mesmo motivo, o coeficiente de correlação também é simétrico:

p(X,V) =p(K,X)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Afinal, ele é a razão entre a covariância e o produto dos desvios padrão:

ii) Cov(X,X) = V(X)

A covariância de uma mesma variável é igual à sua variância.

Por exemplo, sendo X uma variável aleatória com variância V(X) = 4, então a covariância dessa variável com ela mesma é igual à própria variância: Cov(X,X) = 4.
ESCLARECENDO!

Podemos obter esse resultado, pela fórmula da covariância:

Cov(x,y) = - F(x).E(r)

Assim, o valor de Cov(X,X) é:

Cov(X,X) = E(X.X) - E(X}.E{X} = E(X2) - [E(X]]2

Essa é exatamente a fórmula da variância!

Dessa forma, o coeficiente de correlação de uma mesma variável é:

p(X,X) = 1

Ou seja, não importa qual é a variável, o seu coeficiente de correlação com ela mesma é igual a 1.

iii) Cov(k,X) = 0

A covariância de uma constante e uma variável é igual a zero.

Ou seja, a covariância de uma variável X com uma constante k = 5, por exemplo, é
Cov(X,5) = 0. Essa propriedade vale para qualquer variável X e qualquer constante k.
0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

/ 125

/

ví.-

W ES<CLARECENDO!

Vejamos o porquê desse resultado. Pela fórmula da covariância, temos:

Cov(k,Xy) = E(k.X} - E(k).E(X)

Sabemos que Eík.X) = k.E(X) e F(/c) = k. Substituindo esses resultados, temos:

Cov(k,X') = k.E(X) - k.E(X) = 0

Como a covariância Cov(k,X) = 0, então a correlação também é igual a 0: p(fc,X) = 0

iv) Cov(X + a,Y + b) = Cov(X, F)

A covariância não se altera quando somamos ou subtraímos constantes às variáveis. Por exemplo, sendoCov(X,Y) = 6, então a covariância entre a variável X + 5 e a variável Y - 4 será a igual:

Cov(X + 5, Y - 4) = Cov(X,Y) = 6

Podemos verificar essa propriedade, pela fórmula de covariância:

Cov(X + a,Y + b) = E[(X + a). (Y + h)J - E(X + a). E(Y + Z?)

Aplicando a distributiva na primeira expressão, temos:

Cov(X + a,Y + &) = E(X. Y + b.X + a. Y + a. b~) — E(X + à).E(Y + h)

Pelas propriedades da esperança, temos:

Cov(X + a,Y + b) = E(X. F) + b. E(X) + a.E(Y) + a.b - [F(X) + a], [£(F) + b]

Aplicando a distributiva no segundo termo:

= E(X. F) + b. E(X) + a. Eífi + a. b. ~[EÇX). E(Y} + b. E(X) + a. E(Y) + a. b]

= E(X. F) + b. E(X) + a. E(Y} + a. b. -EÇX). E(Y) - b.E(X) ~ a.E(Y~) -a.b
CovÇX + a,Y + b) = E(X. F) - E(X). £(F)

Essa é justamente a fórmula da covariância Cov(X, y)l

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Dessa forma, o coeficiente de correlação também não se altera quando somamos ou subtraímos constantes às variáveis:
p(X±a,Y±b) = p(X.Y)

v) Cov(X + Y,Z) = Cov(X, Z) + CovÇY, Z}

A covariância da soma de variáveis aleatórias X + Y e uma outra variável Z é igual à soma da covariância entreX e Z com a covariância entre Y e Z.

Por exemplo, vamos supor que a covariância entre as variáveis X e Z seja Cov(X, Z)
= 1 e que a covariância entre as variáveis Y e Z seja Cov(Y, Z) = 2. Supondo que a variável S represente a soma S = X + Y, então podemos calcular a covariância entre S e Z:
Cov(S,Z) = Cov(X + Y, Z) = Cov(X,Z) + Cov(Y,Z) = 1 + 2 = 3

INDO MAIS

FUNDO!

Novamente, podemos verificar essa propriedade, pela fórmula de covariância:

Cov(X + Y,Z) = E[(X + Y).Z] - E(X + Y).E(Z)

Aplicando a distributiva na primeira expressão, temos:

Cov(X + Y,Z) = E(X.Z + Y.Z) - E(X + r).E(Z)

Pela propriedade aditiva da esperança, temos:

Cov(x + y,z) = Etx.z) + F(r.z) - [e (x) + eçy)].e(z)

Aplicando a distributiva no segundo termo:

Cov(X + Z,Z) = E(X.Z~) + F(Z.Z) - [E(X).E(Z) + £(Z).£(Z)]

Cov(X + Y,Z) = E(X. Z) + E(Y. Z) -E(X). E(Z) - E(Y\E(Z)

Reorganizando esses termos:

Cov(X + Y,Z) = EÇX.Z) - E(X').E(Z') + F(Z.Z) - E(Y).E(Z)

Cov(x + r,z) = Cov(x,z) + cov(y,z)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A mesma propriedade pode ser aplicada para a subtração de variáveis:

Cov(x - y,z) = cov(x,z) - cov(y,z)

Ou seja, para o nosso exemplo em que Cov(X,Z) = 1 e seja Cov(Y,Z) = 2, supondo D = X - Y, então a covariância entre D e Z é:
Cov(D,Z) = Cov(X - Y, Z) = Cov(X,Z) - Cov(Y,Z) = 1 - 2 = -1

vi) Cov(kX,Y') = Cov(X,kY) = k.Cov(X,Y)

A covariância de duas variáveis aleatórias, sendo qualquer uma delas multiplicada por uma constante, é igual ao produto da constante pela covariância das variáveis.
Considerando que a covariância entre X e Y é Cov(X, Y) = 6 e supondo W = 5.Y, a covariância entre X
e W será:
Cov(X, W) = Cov(X, 5.Y) = 5.Cov(X, Y) = 5 x 6 = 30

E se definíssemos a variável H = 5.X, então a covariância entre H e Y seria:

Cov(H, Y) = Cov(5.X, Y) = 5.Cov(X, Y) = 30

Teríamos o mesmo resultado! Ou seja, não importa qual é a variável que está sendo multiplicada pela constante, pois o resultado será o mesmo: a covariância será multiplicada pela constante.
O mesmo vale para quando estamos dividindo por uma constante k (pois é o mesmo que multiplicar pela
1 Yconstante - Por exemplo, para G = -, a variância entre X e G será:
k 3

Essa propriedade também pode ser verificada, a partir da fórmula da covariância e das propriedades da esperança.
Cov(k.X,Y) = E(k.X.Y) - E(k.X).E(Y)
Cov(k.X,Y) = k.EÇX.Y) -k.E(X\E(Y) = k.[E(X.Y) - £(X).£(Y)]

Cov(k.XfY) = k.Cov(X,Y)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos deduzir que, se ambas as variáveis estiverem multiplicadas pela constante, então a covariância será multiplicada pelo quadrado da constante:
Cov(k.X,k. V) = k.k.Cov(X,Y) = k2.Cov(X,Y)

Por exemplo, sendo W = 5.Y e H = 5.X, a covariância entre H e W é:

Cov(H, W) = Cov(5.X, 5.Y) = 5 x 5.Cov(X,Y) = 25 x 6 = 150

E se as constantes forem diferentes, teremos:

CovÇk. X, l. y) = k. I. Cov(X, y)

Y

Por exemplo, para G = - e H = 5.X, a covariância entre H e G é:

Cov(H,G) = Covfs.X,^ = S.^.Cov(X,Y) = 5.|.6 = 10

E como fica o coeficiente de correlação?

Se as variáveis estiverem multiplicadas por duas constantes quaisquer, k e l, o coeficiente de correlação se manterá o mesmo se as constantes tiverem o mesmo sinal (kl > 0) e terá sinal contrário se as constantes tiverem sinais diferentes (kl < 0):
p(k.X, l. y) = p(X, y), se kl > 0

p(fc.X,Z.y) = -p(X,y), se kl < 0

Assim, o coeficiente de correlação não varia, em módulo, ao multiplicarmos as variáveis aleatórias por constantes reais.
W ESCLARECENDO!

Para obter o coeficiente de correlação, dividimos a covariância pelos desvios padrão:

p(fc.xj.y)

CovÇk.X^.Y) _ k.l.Cov(X,Y')

°kX-°lX akX-alX

Pelas propriedades do desvio padrão, sabemos que okx — \k\.Gx e ai.Y - \l\-W

p(k.X,l.Y) k.l.CovÇX,Y) Cov(X,Y)

|k|.<TX.|Z|.(TK \kl\ (Tx-^X

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabemos que

^x-^x

— pÇx, Y), logo:

L-J

pÇk.X.l.Y) =-^xPÇX,Y)

Assim, se o produto das constantes for positivo, kl > 0, o que ocorre quando as constantes possuem o mesmo sinal, então teremos kl = \kl\ e o mesmo valor para o coeficiente de correlação:
p(/c.xj.r) =kl ^xp(x,r) = i.p(x,n

Se o produto das constantes for negativo, kl < 0, o que ocorre quando as constantes possuem sinal contrário, então teremos kl = — \kl\ e o coeficiente de correlação terá sinal contrário:
pC/c.xj.y) =-^-xp(x,y) = -I.p(x,r)

Por exemplo, sendo A = 5.X e B = -.Y, o produto entre os coeficientes k = 5 e I = - é positivo:

1 5

5.- = -> 0

3 3

Portanto, o coeficiente de correlação entre X e Y se mantém o mesmo:

p(Â,B) = p(5.x,|.r) = p(x,r)

Similarmente, se tivermos C = -5.X e D = — |.Y, o produto também será positivo:

1 5

-5X-3=3>O

Logo, o coeficiente de correlação também se mantém o mesmo:

Porém, se tivermos A = 5.X e D = — |.Y, o produto entre os coeficientes é negativo:

1 5

5X-3=-3<O

Por isso, o coeficiente de correlação terá sinal oposto:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Se houver apenas uma constante k multiplicando uma das variáveis, temos um caso específico dessa propriedade, para l = 1. Nesse caso, o coeficiente de correlação será o mesmo se k> 0 e terá sinal contrário se k < 0:
p(k.X,Y} = p(X,Y), se k > 0

p(k.X,Y) = —p(X,Y), sek <0

Propriedades da Covariância i) Simetria: Cov(X,Y) = Cov(Y,X)
ii) Mesma variável: Cov(X,X) = Var(X)

iii) Com uma constante: Cov(k,X) = 0

iv) Soma/Subtração de uma constante: Cov(X ± a,Y ± Z?) = Cov(X, K)

v) Soma/Subtração de variáveis: Cov(X ±Y,Z) = Cov(X,Z) ± Cov(Y, Z)

vi) Produto de constantes: Cov(k.X, l. K) = k. I. Cov(X, K)

HORAM

í (FGV/2015 - Prefeitura de Recife/PE) Uma variável aleatória X tem média igual a 2
e desvio padrão igual a i 2. Se Y = 6 - 2X, então a média de Y, a variância de Y e o coeficiente de correlação entre X e Y valem,
= respectivamente,
a) -2, 4el.

b) -2, 16 e 1.

c) 2,16 e -1.

d) 10, 2 e -1.

e) 2, 4 e -1.

: Comentários:

= Pelas propriedades da esperança, temos:

E(Y) = E(6 - 2X) = 6 - 2.E(X)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

: O enunciado informa que a média de X é E(X) = 2, logo:

E(Y) = 6-2.2 = 2

I

: Pela propriedade da variância, temos:

V(Y) = V(6 - 2X) = (-2)2.V(X) = 4.V(X)

= O enunciado informa que o desvio padrão de X é DP(X) = 2. Assim, a variância é V(X) = 22 = 4:

V(Y) = 4.4 = 16

I

; Como Y = 6 - 2X, o coeficiente de correlação de X e Y é:

i p(X,D=p(X,6-2X)

: Sabemos que a soma de constantes não altera o coeficiente de correlação, logo:
i p(X,Y} = p(X,-2X)

Aqui, temos uma constante negativa multiplicando uma das variáveis: k = -2 < 0. Logo, o coeficiente de
= correlação terá sinal contrário:

= Sabemos que p(X,X) = 1, logo:

p(V) = -p(xj)

j p(XJ) = -l

= Gabarito: C

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

VARIÂNCIA DA SoMA E DA DIFERENçA

No caso geral, a variância da soma é dada pela seguinte fórmula:

v(x + y) = + y(y) + 2. Cov(x, y)

Por exemplo, vamos supor que a variância de X é V(X) = 3, que a variância de Y é
V(Y) = 4 e a covariância entre X e Y é Cov(X,Y) = 1. Então, a variância da soma das variáveis S = X + Y será:
V(S) = V(X + Y) = V(X) + V(Y) + 2.Cov(X,Y) = 3 + 4 + 2x1 = 9

Para a subtração das variáveis, temos:

v(x - y) = + y(y) - 2. Cov(x, y)
Para o mesmo exemplo, sendo D = X - Y, a variância de D será:

V(D) = V(X - Y) = V(X) + V(Y) - 2.Cov(X,Y) = 3 + 4 - 2x1 = 5

^^ACORDE!

Tanto na fórmula da variância da soma V(X + Y), quanto na fórmula da variância da subtração V(X - Y), iremos somar as variâncias de X e Y.
A diferença entre as duas fórmulas está no sinal da covariância, que é multiplicada por 2. Para a variância da soma, somamos o dobro da covariância e para a variância da subtração, subtraímos o dobro da covariância entre as variáveis.
Para ajudar a lembrar, observe a similaridade das fórmulas acima com os produtos notáveis:

(x + y)2 = x2 + y2 + 2. x. y
(x — y)2 = x2 + y2 — 2. x. y

Para variáveis independentes X, Y, temos Cov(X,Y) = 0 e, portanto, a variância da soma será igual à variância da diferença (propriedade aditiva da variância):
v(x + y) = v(x) + iz(y) + 2. Cov(x, y) = + y(y)

v(x - y) = y(x) + y(y) - 2. cov(x, y) = + y(y)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por exemplo, se X e Y forem independentes, com V(X) = 3 e V(Y) = 4, então a variância da soma e da diferença serão iguais a:
V(X + Y) = V(X - Y) = V(X) + V(Y) = 7

INDO MAIS

FUNDO!

Se as variáveis forem multiplicadas por constantes reais quaisquer k, l:
V(k. X + l.Y} = V(k. X) + V(l. Y) + 2. Cov(k. X, l. K)

Sabemos que:

V(k.X} = k2.V(X}

V(l.Y} = l2.V(Y}
CovÇk.X,l.Y} = k. I. Cov(X,Y)

Então:

V(k. X+l.Y) = k2. V(X) + l2. V(K) + 2. k.l. Cov(X, F)

Analogamente, temos:

V(k. X-l.Y} = k2. F(X) + l2. V(F) -2. k.l. Cov(X, F)

Perceba que a similaridade com os produtos notáveis se mantém:

(k.x + l.y)2 = k2.x2 + l2.y2 + 2. (/c. l}.x.y

(k.x — l.y}2 = k2.x2 + l2.y2 — 2. (/c. V).x.y

E se houver mais de 2 variáveis? A variância da soma de 3 variáveis, por exemplo, é:

V(X + Y + Z} = V(X) + V(Y} + 7(Z) + 2[Cov(X,Y) + Cov(X,Z) + Cov(Y,Z}]

Ou seja, precisamos somar as variâncias com o dobro das covariâncias entre todas as variáveis. É importante notar que consideramos a covariância entre duas variáveis uma única vez, em razão da sua simetria, isto é,Cov(X,Y) = Cov(Y,X).

Para n variáveis X₁,X₂, —,Xn, podemos representara variância da soma SÍ=I^Í como:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (2016 - IBGE) Se duas variáveis aleatórias, X e Y, têm correlação linear negativa, então:
i

; a) Quanto menor for o valor de X, menor será o valor de Y.
j b) A soma dos valores esperados de X e Y é menor do que o valor esperado de X + Y.;

I

I

: c) O produto dos valores esperados de X e Y é menor do que o valor esperado do produto X.Y.

d) A soma das variâncias de X e Y é igual ou menor do que as variâncias de X + Y.

i e) A soma das variâncias de X e Y é estritamente maior do que a variância de X + Y.
;

I

I

i Comentários:

A questão informa que a correlação linear entre X e Y é negativa.
;

I

: Em relação à alternativa A, como a covariância é negativa, então X e Y se relacionam em sentidos opostos, i
; Assim, quanto menor for o valor de X, maior será o valor de Y (em média).

: Portanto: alternativa A incorreta.

I

: Em relação à alternativa B, a soma dos valores esperados E(X) + E(Y) é igual ao valor esperado E(X+Y), para i
= quaisquer variáveis Xe Y.

: Portanto: alternativa B incorreta.
i

I

: Em relação à alternativa C, o valor de E(X.Y) pode ser calculado a partir da covariância:
i

Cov(X,Y) = E(X.Y) - E(X).E(Y)

E(X.Y) = Cov(X,Y) + E(X).E(Y)

I

i Como a correlação entre X e Y é negativa, então Cov(X,Y) < 0. Dessa forma:
i

; E(X.Y) <
E(X).E(Y) ;

I

: Ou seja, o produto dos valores esperados E(X).E(Y) é maior que o valor esperado do produto
E(X.Y).

= Portanto: alternativa C incorreta.

: Em relação às alternativas D e E, a variância de X + Y é:

V(X + Y) = V(X) + V(Y) + 2.Cov(X,Y)

= Como Cov(X,Y) < 0, então:

j V(X + Y) < V(X) +
V(Y) j

I

: Ou seja, A soma das variâncias de V(X) + V(Y) é maior que a V(X + Y).
;

= Portanto: alternativa D incorreta e alternativa E correta.

I

I

; Gabarito: E.

I

I

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FGV/2015 - TJ/RO) Seja X = número de anos de condenação e Y = nível de renda do condenado (mil reais).São fornecidas ainda as seguintes informações:

Var(X) = 25; Var (Y) = 16 e Var (X+Y) = 21

Assim sendo, a correlação entre X e Y é igual a:
a) 0,20

b) 0,25

c) 0,50

d) -0,50

e) -0,10

Comentários:

A correlação é dada por:

z Cov(X,Y)

p(X,Y) = -

ox.oy

O valor de Cov(X,Y) pode ser obtido pela fórmula da variância da soma:

V(X + Y) = V(X) + V(Y) + 2.Cov(X,Y)

O enunciado informa que V(X + Y) = 21, V(X) = 25 e V(Y) = 16, logo:

21 = 25 + 16 + 2.Cov(X,Y)

2.Cov(X,Y) = 21 - 25 - 16 = -20

Cov(X,Y) = -10

Os valores dos desvios padrão são a raiz quadrada das variâncias. Sendo V(X) = 25,
então:

ax = V25 = 5

Sendo V(Y) = 16, então:

oY = Vl6 = 4

Portanto, 0 coeficiente de correlação é:

p(X,Y) =

Gabarito: D

Cov(X, 7)

Ox.ay

-10

5x4

-0,5

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

CoEFICIENTE DE VARIAçÃo E VARIÂNCIA RELATIVA

A definição de coeficiente de variação (também chamado de desvio padrão relativo ou, ainda, de coeficiente de variabilidade), Cv, é:
Podemos dizer que esse parâmetro representa uma normalização do desvio padrão pela média, para permitir a comparação da dispersão de variáveis com médias distintas.
Por exemplo, vamos supor que a variável aleatória X apresente média [ix = 100 e desvio padrão ox = 20;e que a variável aleatória Y apresente média = 10 e desvio padrão aY = 5.

Nesse caso, não poderíamos afirmar que a dispersão de X é maior que a de Y, só porque ax > oY- Para efetuarmos essa comparação, precisamos do Coeficiente de Variação. Para esse exemplo, temos:
Portanto, concluímos que a dispersão de Y é maior do que a de X, porque CVY > CVX-

Como a média e o desvio padrão consideram a mesma unidade de medida (a mesma dos elementos da variável aleatória), o coeficiente de variação é adimensional, isto é, não possui unidade de medida, sendo apenas um número.
A variância relativa, VR, também apresenta o mesmo objetivo, qual seja, de permitir comparações entre variáveis com médias distintas.
A variância relativa é definida como o quadrado do coeficiente de variação:

Ou seja, a variância relativa é o quociente entre a variância e o quadrado da média.

Para o nosso exemplo, em que CVx = 0,2, a variância relativa de X é:

VR = (Cvy = (0,2)2 = 0,04

0,0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)
www. estra tegiaconcursos. com. br l«** IX
i (2015 - Analista de Planejamento e Orçamento) O coeficiente de correlação de duas variáveis aleatórias x i
= e y é igual 0,7, ou seja: 6 (x , y) = 0,7. O coeficiente de variabilidade de x é 0,3 - por yx =0,3. O coeficiente de j
= variabilidade de y é 0,5 - yy =0,5. Com essas informações sobre as variáveis x e y, pode-se, corretamente, i
; afirmar que:

i

= a) àmedida que x cresce, em média y decresce.
j b) a variabilidade absoluta de x é maior que a variabilidade absoluta de y.i

I

I

: c) o desvio-padrão de x é 30% menor do que sua média.
;

d) o desvio-padrão de y é 50% de sua média.

I

: e) o desvio-padrão de y é 50% maior do que sua média.
i

I

i Comentários:

A questão informa que o coeficiente de correlação entre X e Y é 0,7: p(X,Y) = 0,7;
que o coeficiente de i

: variabilidade (ou de variação) de X é 0,3:

: CVx = — = 0,3
:

= E que o coeficiente de variabilidade (ou de variação) de Y é 0,5:
i

(7y

: CVy= — = 0,5
:

= Em relação à alternativa A, como o coeficiente de correlação é positivo, à medida que x cresce, em média, y i também cresce.i

: Portanto, a alternativa A está incorreta.
i

= Em relação à alternativa B, não é possível calcular as médias /xx e fiY com as informações fornecidas, assim, ;
= não é possível afirmar algo sobre as variabilidades absolutas (isto é, os desvios padrão ou as variâncias) das i
= variáveis.

i

I

I

: Portanto, a alternativa B está incorreta.
i

I

: Em relação à alternativa C, podemos afirmar que o desvio padrão de X é 30% da sua média:

I

I

: (jx = 0,3 X [lx

:

= Portanto, a alternativa C está incorreta.
=

= Em relação às alternativas D e E, podemos afirmar que o desvio padrão de Y é 50% da sua média:

I

I

: Oy — 0,5 X fly
:

í Portanto, a alternativa D está correta e a alternativa E está incorreta.
=

I

I

: Gabarito: D.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Resumo

Função de Distribuição Acumulada: F(x) = P(X < x)

Esperança Matemática (média): F(X) = £x. P(X = x)

* E(kX~) = k.E(X)

* E(X + k) = E(X) + k

* E(X ±Y) = E(X) ± F(F)

* E(k) = k

* Se X e Y forem independentes, então E(X x F) = F(X) x F(Y)

Moda: valor de X com maior probabilidade

Mediana: divide a distribuição em duas partes iguais, F(xMed) = 0,5

Variância: V(X) = EU - f)2 x P(X =

* V(X + k) = 7(X)

* V(k.X) = k2.7(X)

* V(k) = 0

* Se X e Y forem independentes, então V(X ± Y) = V(X) + 7(Y)

Desvio Padrão: o = x'V(X)

Covariância: Cov(X, Y) = F(X. F) - F(X).F(Y)

Correlação: p(X, Y) = Cov(x,r'>

(TX-CTy

* Se X e Y forem independentes, então Cov(X, K) = 0, p(X, Y) =

Variância da Soma e da Diferença

V(X + F) = F(X) + V(F) + 2. Cov(X, F)

V(X — F) = F(X) + V(F) - 2. Cov(X, F)

Coeficiente de Variação: Q = "

Variância Relativa: VR = (Cv)2 =

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Noções de variáveis discretas

Item. 1. (CEBRASPE/2022 - PETROBRÁS) Considerando que a função de distribuição de probabilidade de uma variável aleatória discreta X seja dada por
(P(X = -l) = 2a)
J P(X = 0) = a [

(p(X = +1) = 2a)

Julgue o item que se segue.

P(|X| > 0) < 0,6

Comentários:

O enunciado fornece a função de distribuição da variável, em função de uma constante a. Para encontrar o valor dessa constante, devemos considerar que a soma das probabilidades de todos os possíveis valores da variável deve ser igual a 1:
2a + a + 2a = 5a = 1

a = - = 0,2

Logo, P(X = -1) = 0,4; P(X = 0) = 0,2 e P(X = +1) = 0,4.

O item pede a probabilidade de o módulo de X ser maior que 0, isto é, de o valor absoluto de
X, desconsiderando-
se o sinal ser maior que zero. Para isso, X pode ser maior que zero ou menor que zero:

P(|X| > 0) = P(X < 0) + P(X > 0)

Como a variável assume apenas os valores -1, 0 e +1, essa probabilidade é igual a:

P(|X| > 0) = P(X = +1) + P(X = -1) = 0,4 + 0,4 = 0,8

Que é maior que 0,6.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 2. (CEBRASPE/2022 - PETROBRÁS) Considerando que a função de distribuição de probabilidade de uma variável aleatória discreta X seja dada por
(P(X = -l) = 2a)
J P(X = 0) = a [
(P(X = +1) = 2a)

Julgue o item que se segue.

O valor esperado da distribuição de X é igual a zero.

Comentários:

Para calcular o valor esperado da distribuição, multiplicamos cada possível valor da variável pela sua probabilidade e somamos todos os produtos. Considerando que a variável assume apenas os valores X = -1, X =0 e X = +1, temos

£(%) = -1 x P(X = -1) + 0 x P(X = 0) + 1 x P(X = 1)

£(%) = -p(x = -1) + P(X = 1)

Pela função de distribuição de probabilidade dada no enunciado, observamos que
P(X = -1) = 2a e

P(X = 1) = 2a, logo:

= —2a + 2a = 0

De fato, o valor esperado é igual a zero.

Gabarito: Certo

Item. 3. (CEBRASPE/2022 - PETROBRÁS) Considerando que a função de distribuição de probabilidade de uma variável aleatória discreta X seja dada por
(P(X = -l) = 2a)
J P(X = 0) = a [

(p(X = +1) = 2a)

Julgue o item que se segue.

O desvio padrão de X é igual a 2 Vã

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O desvio padrão é a raiz quadrada da variância, que por sua vez é definida como:

W) = - E(X))2 x p(Xí)
Na questão anterior, vimos que FQO = 0, logo:

= (—l)2 x 2a + O2 x a + l2 x 2a = 2a + 0 + 2a = 4a

E o desvio padrão é a raiz quadrada desse resultado:

= y/V(X) = Jíã = 2Vã

Gabarito: Certo

Item. 4. (CEBRASPE/2022 - FUNPRESP-EXE) O item a seguir é apresentada uma situação hipotética seguida de uma assertiva a ser julgada a respeito de Estatística e Econometria.
Caso X e Y sejam variáveis aleatórias com média p, desvio padrão o e coeficiente de correlação p, a variável aleatória U = X - Y terá média igual a 0 e variância igual a 2o.
Comentários:

O enunciado informa que a média de ambas as variáveis é E(X) = p e E(Y) = p.
Pelas propriedades da esperança,
a média de U = X - Y é:

E(U) = E(X - Y) = E(X) - E(Y) = p - p = 0

Ademais, o enunciado informa que o desvio padrão das variáveis é igual a o, logo a variância é V(X) = o2 e V(Y) =o2. A variância da diferença é dada por:

V(U) = V(X - Y) = V(X) + V(Y) -2.Cov(X,Y) = o2 + o2 - 2.Cov(X,Y)

O enunciado forneceu o coeficiente de correlação entre as variáveis p, que consiste na razão entre a covariância e o produto dos desvios padrão:
Covçx, r) Covçx, r)

P = =

<jx x ay cr x o

Cov(X,Y) = p x cr2
Substituindo esse resultado na fórmula da variância de U, temos:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

V([/) = 2. o2 — 2.p.a2 = 2. cr2(l - p)

Que é diferente de 2o.

Gabarito: Errado.

Item. 5. (CEBRASPE/2022 - FUNPRESP-EXE) A respeito de estatística e da linguagem de programação
R, julgue o item a seguir.
A covariância e a correlação são conceitos estatísticos idênticos e medem a relação linear entre duas variáveis.
Comentários:

A covariância e a correlação medem a relação linear entre duas variáveis, mas não são iguais. Para calcular a correlação, dividimos a covariância pelo produto dos desvios padrão:
p(U) =

Covçx, r)
(Ty X Oy

Gabarito: Errado.

Item. 6. (CEBRASPE/2022 - TCE/SC) Considerando uma sequência de variáveis aleatórias {Xk}, em queP(Xk = —0,2k) = P(Xk = 0,2fc) = 0,5, para k E {1,2,...}, julgue o item a seguir,
com relação à soma Sn =
Sfc=i xk.

O valor esperado de Sn é igual a zero.

Comentários:

Para avaliarmos essa alternativa, vamos primeiro calcular os resultados possíveis para alguns valores de k.
Para k = 1, temos:

PQLl = -0,2x) = P(Xx = -0,2) = 0,5
P(Xx = 021) = P(X1 = 0,2) = 0,5

O valor esperado dessa variável é:

FQQ = -0,2 x 0,5 + 0,2 x 0,5 = 0

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para k = 2, temos:

P(X2 = —0,22) = P(X2 = -0,04) = 0,5

P(X2 = 0,22) = P(X2 = 0,04) = 0,5

O valor esperado dessa variável é:

P(X₂) = -0,04 x 0,5 + 0,04 x 0,5 = 0

Portanto, o valor esperado de cada variável é igual a zero. Pelas propriedades da esperança, temos que o valor esperado da soma é igual à soma dos valores esperados:
n y E(Xk) = 0 + 0 + 0 + *** = 0
Assim, concluímos que o valor esperado da soma, de fato, é igual a zero.

Gabarito: Certo

Item. 7. (CEBRASPE/2021 - TC/DF) Uma amostra aleatória simples, sem reposição, de tamanho 100, será retirada de uma população constituída por 1.000 indivíduos, com o objetivo de se estimar a média p das idades desses 1.000 indivíduos. Essa amostra é representada por um conjunto de variáveis aleatórias Xi,...,Xioo, e o estimador da média populacional p é dado pela seguinte expressão.

Se, no plano amostrai em apreço, (xi,..., xwo) representa uma possível realização de
Xi,..., Xwo e se P(Xi= xi,...

, Xwo = xwo) denota sua probabilidade de ocorrência, é correto afirmar que P(Xi = xi,..., Xioo =
xwo) = 0,1.

Comentários:

Essa questão informa que 100 indivíduos serão extraídos, sem reposição, de uma população de 1000 indivíduos,no total. Para analisar o item, precisamos da probabilidade de extrair o primeiro indivíduo da população em primeiro lugar, o segundo indivíduo da população em segundo lugar, e assim sucessivamente até o centésimo indivíduo da população ser extraído em centésimo lugar.
A probabilidade é a razão entre o número de eventos favoráveis e o número de eventos possíveis:

nfeventos favoráveis') n(A)

nfeventos possíveis) n(U)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O número de eventos possíveis corresponde ao arranjo de 100 elementos, dentre 1000,
por se tratar de uma seleção em que a ordem a importa:
z x 1000!

n(í/) — -^íooo.ioo — 100! — X 999 X
X

E o número de eventos possíveis é igual a 1, pois existe apenas uma possibilidade de selecionarmos primeiro o primeiro elemento, depois o segundo,...
P ~ 1000 x 999 x ...102 x 101

Como o denominador é muito superior a 10, essa probabilidade é muito inferior a — = 0,1.

Gabarito: Errado.

Item. 8. (CEBRASPE/2021 - PGDF) A tabela a seguir apresenta o número anual de irregularidades detectadas por auditores conforme o tempo de experiência desses auditores na atividade de auditoria. A última coluna foi obtida utilizando-se a reta ajustada pelo método dos mínimos quadrados.
Auditor

Totais

Tempo
(T anos)

N2 de irreg detec(N)
TxN

T2

1003

N2

(T - T)2

96,04

23,04

3,24

10,24

174,24

306,8

(N - N)2

(N - N)2

0,052441

0,022201

0,488601

0,048841

0,003721

0,615805

Caso necessário, use as seguintes aproximações: 15341/2 = 39,2 e 2301/2 = 15,2.
Considerando essas informações, julgue o próximo item.

O coeficiente de correlação linear entre as variáveis T — tempo de experiência do auditor na atividade — e N —número anual de irregularidades detectadas pelo auditor — é superior a 0,75.

Comentários:

O coeficiente de correlação entre duas variáveis X e Y pode ser calculado como:

£x.y - n.x.y

VS*2 — n.x2 x y/Xy2 — n.y2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nessa questão estamos trabalhando com as variáveis T e N. Pela tabela, obtemos as seguintes informações:
* £x.y = £T.N = 531

* x- = T = — E=T—59= 11,8

n 5

_ jrv EN 35„

7 n 5

* £x2 =XT2 = 1003

* Ey2 = E/V2 = 291

Substituindo esses dados na fórmula:

531-5x11,8x7 531 - 59 x7

P 71003 - 5 x 11,82 x V291 - 5 x 72 71003 " 5 x
139,24 x V291 - 5 x 49

531-413 118

P ~ V1003 - 696,2 x V291 - 245 " V3Õ6^ x V46

Agora, devemos observar os resultados fornecidos no enunciado V1534 = 39,2 e V230 = 15,2 e notar que
1534 é 5 vezes 306,8 e 230 também é 5 vezes 46. Então, vamos multiplicar o numerador e o denominador por
5 (o que equivale multiplicar por n tanto o numerador quanto o denominador da fórmula do coeficiente de correlação acima):
5 118 118 x 5 590

v/5 x V5 V306,8 x V46 ^306,8 x 5 x V46 x 5 V1534 x V230

590 590

P 39,2 x 15,2 595,84 " '

Que, de fato, é superior a 0,75.

Gabarito: Certo

Item. 9. (CESPE/2021 - PC/SE) Considere duas variáveis aleatórias, X e Y, tais que P(X > 0) = 1,
P (X < 1) = 1/10,

P (X < 11Y > 1) = 3/10, Var(X) = Var(Y) = 1, e Cov(X, Y) = 0. Com base nessas informações, julgue o item a seguir.
X e Y são independentes.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado informa que a covariância entre as variáveis é igual a zero, mas isso não significa que as variáveis sejam independentes. Em outras palavras, se as variáveis são independentes, a covariância entre elas é necessariamente igual a zero; mas o contrário não é verdadeiro, ou seja, é possível que a covariância entre duas variáveis seja igual a zero, mesmo que as variáveis sejam dependentes.
Inclusive, vale observar a probabilidade condicional P(X<l|Y>l)ea não condicional
P (X < 1) fornecida. Para eventos independentes, essas probabilidades deveriam ser iguais. No entanto, o enunciado informa que P (X <1 | Y > 1) = 1/10 e que P (X < 1) = 3/10. Assim, confirmamos que as variáveis não são independentes.
Gabarito: Errado.

Item. 10. (CESPE/2021 - PC/SE) Considere duas variáveis aleatórias, X e Y, tais que P(X > 0) = 1,
P (X < 1) = 1/10,

P (X < 11Y > 1) = 3/10, Var(X) = Var(Y) = 1, e Cov(X, Y) = 0. Com base nessas informações, julgue o item a seguir.
Var(X - Y) = 2

Comentários:

A variância da diferença entre duas variáveis é dada por:

Var(X - Y) = Var(X) + Var(Y) ~ 2. Cov(X, y)
O enunciado informa que Var(X) = 1, Var(Y) = 1 e Cov(X,Y) = 0, logo:

Var(X — y) = 1 + 1 — 0 = 2

Gabarito: Certo.

Item. 11. (CESPE/2020 - ME) Considerando que R representa uma variável quantitativa cuja média,
mediana e variância são, respectivamente, iguais a 70, 80 e 100, e que U = — — 7, julgue o próximo item, acerca das variáveis U e R.
A correlação linear entre as variáveis U e R é igual a zero.

Comentários:

y^

Este item pede o coeficiente de correlação entre Re U = — - 7:

p(R, U) = p

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Pelas propriedades do coeficiente de correlação, quando somamos ou subtraímos uma constante a uma variável, o coeficiente de correlação não se altera:
p(R,U)=p

Quando dividimos uma variável por uma constante, o módulo do coeficiente (seu valor absoluto) não se altera.Se a variável for negativa, o coeficiente é multiplicado por -1; senão, ele permanece o mesmo.
Como estamos dividindo por uma constante positiva, então:

p(R, IP) = p(R, /?)

E o coeficiente de correlação de uma mesma variável é igual a 1, e não zero.

Gabarito: Errado

Item. 12. (CESPE/2020 - ME) Considerando que R representa uma variável quantitativa cuja média,
mediana e variância são, respectivamente, iguais a 70, 80 e 100, e que U = — —7, julgue o próximo item, acerca das variáveis U e R.
A variável U possui média nula.

Comentários:

y^

De acordo com as propriedades da esperança, a média de U = — - 7 é dada por:

z . R E(R)

E^=-0-7"-7

O enunciado informa que a média de R é E(R) = 70, logo a média de U é:

£([/)= —-7 = 7-7 = 0

Logo, de fato, a variável U possui média nula.

Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 13. (CESPE/2020 - SEFAZ-DF) A partir de uma amostra aleatória simples de tamanho n, sabe-se que a média aritmética de uma variável X foi igual a 3.
Considerando que os valores possíveis para a variável X sejam -1 e +4, julgue o item que se segue.

A distribuição da variável X é simétrica em torno da sua média.

Comentários:

O enunciado informa que a média (ou esperança) da variável é E(X) = 3 e que os possíveis valores da variável sãoX = -1 e X = 4.

Com base nessas informações, podemos calcular a distribuição de probabilidade da variável.
Sabendo que a soma das probabilidades dos possíveis valores da variável deve ser igual a 1:

P(X = -1) + P(X = 4) = 1

Vamos chamar de p a probabilidade P(X = -1), logo:

p(X = 4) = 1 - p

A esperança é a soma dos produtos dos valores da variável pelas respectivas probabilidades:

E(X) = x x p(x)

E(X) = -1 x P + 4 x (1 — p) = — p + 4 - 4p = 4 - 5p

E sabemos que a esperança é igual a 3, logo:

F(X) = 4 - 5p = 3
5p = 4 — 3 = 1

p=l=0,2

Portanto, a probabilidade deX = -1 é igual a 0,2 e a probabilidade de X = 4é igual a 1 -0,2 = 0,8.
Assim, concluímos que a variável não é simétrica.
Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 14. (CESPE/2020 - ME - Adaptada)

A
P(A)

-1

20%

70%

10%

B
P(B)

-1

20%

60%

20%

Considerando que as tabelas precedentes mostram as variáveis categorizadas A e B, que foram codificadas em três níveis numéricos de resposta: -1, 0,1, julgue o item que se segue.
A média da variável A é negativa.

Comentários:

A média (ou esperança) da variável corresponde ao produto dos seus valores pelas respectivas probabilidades:
EQO = x x p(x)

Pela tabela fornecida, observamos que A assume os valores -1, 0 e 1, com probabilidades P(A = -1) = 20% = 0,2;P(A = 0) = 70% = 0,7 e P(A = 1) = 10% = 0,1, logo:

E(A) = -1 x 0,2 + 0 x 0,7 + 1 x 0,1 = -0,2 + 0,1 = -0,1

Que, de fato, é negativo.

Gabarito: Certo

Item. 15. (CESPE/2020 - ME - Adaptada)

A
P(A)

-1

20%

70%

10%

B
P(B)

-1

20%

60%

20%

Considerando que as tabelas precedentes mostram as variáveis categorizadas A e B, que foram codificadas em três níveis numéricos de resposta: -1, 0,1, julgue o item que se segue.
As modas e as medianas das variáveis A e B são iguais a zero.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A moda é o valor com maior probabilidade da distribuição. Para A, o valor com maior probabilidade é A = 0 (com probabilidade de 70%); e para B, o valor mais provável é B = 0 (com probabilidade de 60%). Portanto, as modas das variáveis, de fato, são iguais a zero.
Já em relação à mediana, a probabilidade dos valores menores ou iguais à mediana é de pelo menos 50%; e a probabilidade dos valores são maiores ou iguais à mediana também é de pelo menos 50%.
Em relação à variável A, a probabilidade dos valores menores ou iguais a 0 (no caso,
-1 e 0) é igual a 90%; e a probabilidade dos valores maiores ou iguais a 0 (no caso, 0 e 1) é igual a 80%.Assim, concluímos que a mediana de A, de fato, é igual a zero.
Em relação à variável B, a probabilidade dos valores menores ou iguais a 0 (no caso,
-1 e 0) é igual a 80%; e a probabilidade dos valores maiores ou iguais a 0 (no caso, 0 e 1) também é igual a80%. Assim, concluímos que a mediana de B também é igual a zero.
Gabarito: Certo

Item. 16. (CEBRASPE/2018 - ABIN - Adaptada) Julgue o item que se segue. Se
X e Y forem variáveis independentes e tiverem distribuição com médias px e respectivamente,e variâncias ax2 e aY2,
respectivamente, então a soma X + Y terá média px + pY e variância ox2 + crY2.

Comentários:

Pelas propriedades de esperança e variância, temos:

E(X + Y) = E(X) + E(Y) = /zx4-My

Se X e Y forem independentes, então V(X + Y) = V(X) + V(Y) = ax2 + aY2

Gabarito: Certo.

Item. 17. (CEBRASPE/2016 - TCE/PR) A quantidade de parcelas (X) escolhida por um cliente para o pagamento de determinado serviço é uma variável aleatória discreta com função de probabilidade,para P(X = K) 7-k / 21

, para k G {1, 2,..., 6} e P(X = K) = 0, para K £ {1,2,...6}.

No que se refere a essa variável aleatória, assinale a opção correta.

a) A esperança E(3X - 8) é igual a zero.

b) P(X< 2) >0,5

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) P(X2 = 1) = 4/49

d) A esperança de X é igual ou superior a 3.

e) A variância da variável aleatória X é igual ou superior a 3.

Comentários:

Vamos utilizar a tabela de distribuição para calcular as probabilidades de cada valor e a esperança da variável aleatória:
X

Total

P(x)

(7-1J/21 = 6/21
(7-2J/21 = 5/21
(7-3J/21 = 4/21
(7-4J/21 = 3/21
(7-5J/21 = 2/21
(7-6J/21 = 1/21
21/21 = 1

x.P(x)

6/21

10/21

12/21

12/21

10/21

6/21

56/21 = 8/3

Em relação à alternativa B, temos:

P(X< 2) = P(X=1) = 6/21

Como 6/21 < 0,5, a alternativa B está errada.

Em relação à alternativa C, sabemos que se X2 = 1, então X = 1 ou X = -1, ou seja:

P(X2 = 1) = P(X = 1) + P(X = -1)

Como P(X = -1) = 0, então:

P(X2 = 1) = P(X = 1) = 6/21

Portanto, a alternativa C está errada.

Em relação à alternativa D, como E(X) = 8/3 = 2,666... < 3, a alternativa D está errada.Em relação à alternativa A, temos:

E(3X- 8) = 3E(X)- 8 = 8-8 = 0.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Portanto a alternativa A está correta. Vejamos, porém, a alternativa faltante.
Em relação à alternativa E, temos:

V(X) = E(X2) — [E(X)]2

Vamos utilizar novamente a tabela para calcular E(X2):

X X2

1 1

2 4

3 9

4 16

5 25

6 36

Total

P(x)

6/21

5/21

4/21

3/21

2/21

1/21

x2.P(x)

6/21

20/21

36/21

46/21

50/21

36/21

194/21

Assim, a variância é:

7(X) = £(X2)- [F(X)]2 = —

194 64

9"

582 - 448

-6^ 2427

Como 2,127 < 3, então a alternativa D está errada.

Gabarito: A

Item. 18. (CEBRASPE/2015 - TELEBRAS) Considerando que Yi, Y₂, ..., Yn, ...
sejam variáveis aleatórias independentes que satisfazem P(Yj = j) = P(Yj = -j) = 1/2 para j = 1, 2,..., julgue o item que se segue.
O conjunto de valores que a variável aleatória Yi + Y₂ + Y₃ pode assumir é igual a {-6, -4, -2, 0,
2, 4, 6}.

Comentários:

Os valores que Yi pode assumir são Yi = 1 e Yi = -1; os valores que Y₂ pode assumir são Y₂ = 2 e Y₂ = -2; e os valores que Y3 pode assumir são Y3 = 3 e Y3 = -3.
Portanto, os valores que Yi + Y₂ + Y₃ corresponde aos resultados possíveis de ±1 ±
2 ± 3. Pelo princípio multiplicativao 0 número de possibilidades, não necessariamente distintas é:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

2 x 2 x 2 = 8 possibilidades

São elas:

1 + 2 + 3 = 6,

1 + 2 - 3 = 0,

1 - 2 + 3 = 2,

-1-2-3 =-6;

-1-2 +3 = 0;

-1 + 2 - 3 = -2;

-1 + 2 + 3 = 4, 1 - 2 - 3 = -4.

Assim, os possíveis resultados são {-6, -4, -2, 0, 2, 4, 6}.

Gabarito: Certo.

Item. 19. (CEBRASPE/2015 - TELEBRAS) Um vendedor de certo tipo de equipamento de telecomunicações pode visitar, em um dia, um ou dois clientes, com probabilidades de 1/3 e 2/3,respectivamente. De cada contato pode resultar a venda de um equipamento por R$ 50.000, com probabilidade de 1/10 ou nenhuma venda,com probabilidade de 9/10.

Considerando que V seja a variável aleatória que indica o valor total de vendas diárias desse vendedor, em milhares de reais, julgue o item que se segue.
Se p representar a função de probabilidade de V, então p(0) = 0,84.

Comentários:

A probabilidade de não realizar qualquer venda, P(0), é a soma da probabilidade de ele não vender, dado que ele visitou 1 cliente, indicada por P(01VI), e de ele não vender, dado que ele visitou 2 clientes, indicada porP(01V2) (união de eventos excludentes):

P(0) = P(0|71). P(V1) + P(0|V2).P(V2)

As probabilidades de VI e V2 são dadas no enunciado: P(V1) = 1/3 e P(V2) = 2/3.

A probabilidade de ele não vender, tendo realizado uma visita, é 9/10, portanto, P(0| VI) = 9/10.

A probabilidade de ele não vender, tendo realizado 2 visitas, corresponde a ele não vender na primeira visita E
não vender na segunda visita (interseção de eventos). Portanto:

P(0|72)

9 9 _ 81

iõx 1Õ _ 1ÕÕ

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Dessa forma, temos para P(0):

, 9 1 81 2 3 54

o) - + +

Gabarito: Certo.

Item. 20. (CEBRASPE/2015 - TELEBRAS) Um vendedor de certo tipo de equipamento de telecomunicações pode visitar, em um dia, um ou dois clientes, com probabilidades de 1/3 e 2/3,respectivamente. De cada contato pode resultar a venda de um equipamento por R$ 50.000, com probabilidade de 1/10 ou nenhuma venda,com probabilidade de 9/10.

Considerando que V seja a variável aleatória que indica o valor total de vendas diárias desse vendedor, em milhares de reais, julgue o item que se segue.
A probabilidade de esse vendedor fechar exatamente uma venda em um dado dia é superior a 0,09.

Comentários:

A probabilidade de vender um equipamento, indicado por P(S), é função da probabilidade de ele vender um equipamento, dado que ele visitou 1 cliente, P(S | VI), e de ele vender um equipamento, dado que ele visitou 2clientes, P(S| V2):

P(S) = P(S|K1).P(V1) + P(S|V2).P(V2)

A probabilidade de uma venda para cada contato é 1/10, portanto, P(S | VI) = 1/10.

A probabilidade de venda, considerando que ele visitou 2 clientes, corresponde a ele realizar a venda para o primeiro cliente E não realizar para o segundo; OU ele não realizar a venda para o primeiro cliente E realizar para o segundo. Portanto, temos:
Dessa forma, temos para P(S):

P(S|72)

1ÕX

9 9

TÕ+1Õ

x 1Õ _;

ÍÕÕ

Que é superior a 0,09.

Gabarito: Certo.

1 18 2 46

— + ------ X — : =------- —

3 100 3 300

0,153

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 21. (CEBRASPE/2015 - TELEBRAS) Um vendedor de certo tipo de equipamento de telecomunicações pode visitar, em um dia, um ou dois clientes, com probabilidades de 1/3 e 2/3,respectivamente. De cada contato pode resultar a venda de um equipamento por R$ 50.000, com probabilidade de 1/10 ou nenhuma venda,com probabilidade de 9/10. Considerando que V seja a variável aleatória que indica o valor total de vendas diárias desse vendedor, em milhares de reais, julgue o item que se segue.
O valor esperado da variável aleatória V é maior que 5 e indica, em milhares, o valor total esperado de vendas em cada dia.
Comentários:

Considerando que o vendedor visita até 2 clientes e que, para cada cliente, pode realizar até 1 venda, no valor de 50 mil reais, então o valor esperado de V, que representa o valor esperado de vendas diárias, em milhares de reais, é:
£(%) = \x.P(X = x)

= 0 x P(0) + 1 x 50 x P(l) + 2 x 50 x P(2) = 50 x P(l) + 100 x P(2)

A probabilidade de realizar exatamente 1 venda é a soma da probabilidade de ele vender um equipamento,dado que ele visitou 1 cliente, P(11 Cl), com a probabilidade de ele vender um equipamento, dado que ele visitou2 clientes, P(1|C2):

P(l) = P(1|C1).P(C1) + P(1|C2).P(C2)

A probabilidade de uma venda para cada contato é 1/10, portanto, P(11 Cl) = 1/10. A
probabilidade de venda,
considerando que ele visitou 2 clientes, corresponde a ele realizar a venda para o primeiro cliente E não realizar para o segundo; OU ele não realizar a venda para o primeiro cliente E realizar para o segundo.Portanto, temos:

P(l|C2) = ^x

9 9 1 18

x

10 1Õ 1Õ 1ÕÕ

Dessa forma, temos para P(l):

P(l) =

18 2 _ 46

1ÕÕX 3 - 3ÕÕ

A probabilidade de ele realizar exatamente 2 vendas é igual à probabilidade de ele visitar 2 clientes E efetuar a venda para os dois:
P(2) = P(2|C2) x P(C2)
112 2

_ 1Õ X 1Õ X 3 _ 3ÕÕ

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A esperança de V é, portanto:

46 2 46 d- 4
E(X) = 0 x P(0) + 50 x P(l) + 100 x P(2) = 50 x — + 100 x — = ——

300 300 6

— = 8,333 ...

Gabarito: Certo.

Item. 22. (CEBRASPE/2015 - TELEBRAS) Roberto comprou, por R$ 2.800,00, rodas de liga leve para seu carro, e,ao estacionar no shopping, ficou indeciso sobre onde deixar o carro, pois, caso o coloque no estacionamento público, correrá o risco de lhe roubarem as rodas, ao passo que, caso o coloque no estacionamento privado,terá de pagar R$ 70,00, com a garantia de que eventuais prejuízos serão ressarcidos pela empresa administradora.
Considerando que p seja a probabilidade de as rodas serem roubadas no estacionamento público, que X
seja a variável aleatória que representa o prejuízo, em reais, ao deixar o carro no estacionamento público, e queY seja a variável aleatória que representa o valor, em reais, desembolsado por Roberto ao deixar o carro no estacionamento pago, julgue o item subsequente.
O conjunto de valores possíveis para a variável aleatória X é X(W) = {2.800, 70, 0}.

Comentários:

O enunciado informa que X representa o prejuízo ao deixar o carro no estacionamento público. Oestacionamento público é gratuito, porém, há o risco de roubo das rodas. Se não roubarem, o prejuízo é zero;se roubarem, o prejuízo é R$ 2.800. Assim, temos X = {2.800, 0}.

Gabarito: Errado

Item. 23. {CEBRASPE/2015 - TELEBRAS) Roberto comprou, por R$ 2.800,00, rodas de liga leve para seu carro, e,ao estacionar no shopping, ficou indeciso sobre onde deixar o carro, pois, caso o coloque no estacionamento público, correrá o risco de lhe roubarem as rodas, ao passo que, caso o coloque no estacionamento privado,terá de pagar R$ 70,00, com a garantia de que eventuais prejuízos serão ressarcidos pela empresa administradora.
Considerando que p seja a probabilidade de as rodas serem roubadas no estacionamento público, que X
seja a variável aleatória que representa o prejuízo, em reais, ao deixar o carro no estacionamento público, e queY seja a variável aleatória que representa o valor, em reais, desembolsado por Roberto ao deixar o carro no estacionamento pago, julgue o item subsequente.
Supondo-se que Roberto tome sua decisão escolhendo aleatoriamente entre suas opções, se p = 0,05, então o valor esperado para o prejuízo/valor desembolsado por Roberto será inferior a R$ 100,00.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Sabendo que p = 0,05, a esperança de X (prejuízo do estacionamento público) é:

£(%) = \x.P(X = x)

F(X) = 2800 x p + 0 x (1 - p) = 2800 x p = 2800 x 0,05 = 140

Sabemos também que Y (desembolso no estacionamento privado) assume somente o valor
{70}, isto é, Y = 70.
Por ser uma constante, temos E(Y) = 70.

Supondo aleatória a escolha entre o estacionamento público e o privado, então são alternativas equiprováveis,isto é, há 50% de chance de escolher o público e 50% de escolher o privado. O
valor esperado dessa situação é dado por:
E(0,5.X + 0,5. r) = 0,5. + 0,5. E(Y) = 0,5 x 140 + 0,5 x 70 = 70 + 35 = 105

Tal valor é superior a 100, não inferior.

Gabarito: Errado.

Item. 24. (CEBRASPE/2015 - TELEBRAS) Roberto comprou, por R$ 2.800,00, rodas de liga leve para seu carro, e,ao estacionar no shopping, ficou indeciso sobre onde deixar o carro, pois, caso o coloque no estacionamento público, correrá o risco de lhe roubarem as rodas, ao passo que, caso o coloque no estacionamento privado,terá de pagar R$ 70,00, com a garantia de que eventuais prejuízos serão ressarcidos pela empresa administradora.
Considerando que p seja a probabilidade de as rodas serem roubadas no estacionamento público, que X
seja a variável aleatória que representa o prejuízo, em reais, ao deixar o carro no estacionamento público, e queY seja a variável aleatória que representa o valor, em reais, desembolsado por Roberto ao deixar o carro no estacionamento pago, julgue o item subsequente.
Se Roberto tomar sua decisão escolhendo aquela cuja variável aleatória correspondente tenha menor valor esperado, então será mais vantajoso para ele deixar o carro no estacionamento pago apenas se p >0,025.

Comentários:

Sabendo que X pode assumir os valores {2800,0}, então considerando que a probabilidade de roubo é p, então a probabilidade de não haver roubo é 1 - p (uma vez que a soma das probabilidades de todos os resultados possíveis é 100%). O valor esperado para X é, portanto:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

£(%) = \x.P(X = x)

£(%) = 2800 xp + 0 x (1 - p) = 2800p

Além disso, sabemos que Y, que representa o desembolso no estacionamento privado,
assume o valor {70}, isto é, Y = 70. Por ser uma constante, temos E(Y) = 70.
Por representarem valores de prejuízo/desembolso, então, será mais vantajoso ele pagar o estacionamento se:
£(%) > F(r)
2800p > 70

70 1

P > 2800 _ 4Õ

p > 0,025

Gabarito: Certo.

Item. 25. (CEBRASPE/2015 - Departamento Penitenciário Nacional)

%

ano

Dado que a participação dos presidiários em cursos de qualificação profissional é um aspecto importante para a reintegração do egresso do sistema prisional à sociedade, foram realizados levantamentos estatísticos, nos anos de 2001 a 2009, a respeito do valor da educação e do trabalho em ambientes prisionais. Cada um desses levantamentos, cujos resultados são apresentados no gráfico, produziu uma estimativa anual do percentualP de indivíduos que participaram de um curso de qualificação profissional de curta duração, mas que não receberam o diploma por motivos diversos.
Em 2001, 69,4% dos presidiários que participaram de um curso de qualificação profissional não receberam o diploma. No ano seguinte, 2002, esse percentual foi reduzido para 61,5%, caindo, em 2009, para30,9%.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A partir das informações e do gráfico apresentados, julgue o item que se segue.

O coeficiente de variação do percentual P é negativo, pois o gráfico de dispersão entre ano e percentual P mostra uma tendência de redução deste último ao longo do tempo.
Comentários:

O coeficiente de variação de P é:

Como todos os valores são positivos, então a média é positiva. Como o desvio padrão é sempre positivo, então o coeficiente de variação é positivo.
Gabarito: Errado.

Item. 26. (CEBRASPE/2013 - MPU) Considere uma máquina fabril cuja operação tenha se iniciado às 8 h da quarta-feira do dia 2/1/2003 e haja se estendido durante cinco dias úteis por semana, sem feriados,de 8 h às
18 h. Considere, ainda, que essa máquina tenha produzido 400 peças, das quais 380 sejam aproveitáveis, até parar por quebra de um componente às 10 h do dia 12/2/2003.
Com base nessas informações, julgue o item seguinte.

Variáveis aleatórias não possuem valores firmes, pois seus valores variam sob a influência de fatores casuais.Assim, conhecer uma variável aleatória não significa conhecer seu valor numérico nem enumerar seus valores possíveis, mas sim considerar as probabilidades de a variável assumir cada valor possível de saída de um experimento a ela associado.
Comentários:

De fato, as variáveis aleatórias representam os resultados de experimentos aleatórios e,
por isso, não possuem valor certo. Conhecer uma variável implica em conhecer os valores possíveis e a probabilidade de a variável assumir cada valor. Com essas informações, podemos calcular todas as medidas que aprendemos.
Gabarito: Certo.

Item. 27. (CESPE/2011 - SEDUC-AM) Para orientar os investimentos em educação em certo município,
um analista foi contratado para criar um ranking das escolas públicas desse município.Para cada escola, as variáveis disponíveis são a quantidade de turmas, a quantidade de alunos, a quantidade de professores, a nota da Prova Brasil e a área do terreno.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A partir dessa situação, julgue o item.

Considere que as áreas de todas as escolas desse município sejam distintas e que cada escola tenha obtido uma nota diferente na prova Brasil. Nessa situação, os modelos de probabilidade para variáveis aleatórias discretas são adequados para representar a distribuição de todas as variáveis analisadas por esse analista.
Comentários:

Essa questão pergunta basicamente se as variáveis quantidade de turmas, quantidade de alunos, quantidade de professores, nota da Prova Brasil e área do terreno são variáveis aleatórias discretas. No entanto, área do terreno é uma variável contínua e não discreta. Logo, os modelos para as variáveis aleatórias discretas não são adequados para representar essa variável.
Gabarito: Errado.

Item. 28. (CESPE/2011 - EBC) Julgue o item a seguir, considerando dois eventos A e B, de um mesmo espaço amostrai S, tais que P(A) > 0 e P(B) > 0.
Considere que IA e IB sejam, respectivamente, as variáveis indicadoras referentes aos eventos A e B, de modo que, por exemplo, lA = 1 se o evento A ocorre e lA = 0 se o evento A não ocorre. Nesse caso, a covariância nula entre as variáveis aleatórias lA e IB não garante que os eventos A e B sejam independentes.
Comentários:

Via de regra, o fato de a covariância entre duas variáveis ser nula não implica na independência entre as variáveis. No entanto, se as variáveis forem binárias, isto é, assumirem apenas 2valores possíveis, como é o caso de A e B, a covariância nula garante a independência das variáveis.
Gabarito: Errado.

Item. 29. (CESPE/2010 - ABIN) Sabendo que X é uma variável aleatória discreta, 0 < p < 1 e k,
número natural,
julgue o item abaixo.

P(X < fc) = (1 — p)k é uma função de probabilidade acumulada.

Comentários:

Sendo k um número natural, ele pode assumir os valores {0,1, 2, 3...}. Para k = 0,
a função apresentada assume o valor:
P(X < 0) = (1 - p)° = 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para k = 1, temos:

P(X< 1) = (1-p)1 = 1-p

Para k = 2, temos:

P(X < 1) = (1 - p)2

Conforme k aumenta, os valores da função diminuem. Portanto, essa função não é uma função de probabilidade acumulada.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Noções de variáveis discretas

Item. 1. (CEBRASPE/2022 - PETROBRÁS) Considerando que a função de distribuição de probabilidade de uma variável aleatória discreta X seja dada por
ÍP(X = -1) = 2a

] P(X = 0) = a *
(p(X = +1) = 2a

Julgue o item que se segue.

P(|X| > 0) < 0,6

Item. 2. (CEBRASPE/2022 - PETROBRÁS) Considerando que a função de distribuição de probabilidade de uma variável aleatória discreta X seja dada por
ÍP(X = -1) = 2a

] = 0) = a *

(p(X = +1) = 2a

Julgue o item que se segue.

O valor esperado da distribuição de X é igual a zero.

Item. 3. (CEBRASPE/2022 - PETROBRÁS) Considerando que a função de distribuição de probabilidade de uma variável aleatória discreta X seja dada por
ÍP(X = -1) = 2a

] P(X = 0) = a *
(p(X = +1) = 2a

Julgue o item que se segue.

O desvio padrão de X é igual a 2 Vã

Item. 4. (CEBRASPE/2022 - FUNPRESP-EXE) O item a seguir é apresentada uma situação hipotética seguida de uma assertiva a ser julgada a respeito de Estatística e Econometria.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Caso X e Y sejam variáveis aleatórias com média p, desvio padrão o e coeficiente de correlação p, a variável aleatória U = X - Y terá média igual a 0 e variância igual a 2o.
Item. 5. (CEBRASPE/2022 - FUNPRESP-EXE) A respeito de estatística e da linguagem de programação R,julgue o item a seguir.

A covariância e a correlação são conceitos estatísticos idênticos e medem a relação linear entre duas variáveis.
Item. 6. (CEBRASPE/2022 - TCE/SC) Considerando uma sequência de variáveis aleatórias
{Xk}, em que
P(Xk = —0,2k) = P(Xk = 0,2k) = 0,5, para k E {1,2,...}, julgue o item a seguir, com relação à somaSn = Yk=lXk.

O valor esperado de Sn é igual a zero.

Item. 7. (CEBRASPE/2021 - TC/DF) Uma amostra aleatória simples, sem reposição, de tamanho 100, será retirada de uma população constituída por 1.000 indivíduos, com o objetivo de se estimar a média p das idades desses 1.000 indivíduos. Essa amostra é representada por um conjunto de variáveis aleatóriasXi,...,
Xioo, e o estimador da média populacional p é dado pela seguinte expressão.

Se, no plano amostrai em apreço, (xi,..., xioo) representa uma possível realização de
Xi,..., Xioo e se P(Xi = xi,

..., Xioo = Xioo) denota sua probabilidade de ocorrência, é correto afirmar que P(Xi = xi,..., Xwo
= Xioo) = 0,1.

Item. 8. (CEBRASPE/2021 - PGDF) A tabela a seguir apresenta o número anual de irregularidades detectadas por auditores conforme o tempo de experiência desses auditores na atividade de auditoria. A última coluna foi obtida utilizando-se a reta ajustada pelo método dos mínimos quadrados.
Auditor

Tempo
(T anos)

N5 de irreg detec(IXI)
Tx N

T2 N2

(T - T)2

(N - N}2

(n - Ny2

1 2

2 7

3 10

4 15

5 25

Totais 59

3 6

5 35

7 70

8 120

12 300

35 531

1003

96,04

23,04

3,24

10,24

174,24

306,8

16 0,052441

4 0,022201

0 0,488601

1 0,048841

25 0,003721

46 0,615805

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Caso necessário, use as seguintes aproximações: 15341/2 = 39,2 e 2301/z = 15,2.
Considerando essas informações, julgue o próximo item.
O coeficiente de correlação linear entre as variáveis T — tempo de experiência do auditor na atividade — eN — número anual de irregularidades detectadas pelo auditor — é superior a 0,75.

Item. 9. (CESPE/2021 - PC/SE) Considere duas variáveis aleatórias, X e Y, tais que P(X > 0) = 1,
P (X < 1) =

1/10, P (X < 11Y > 1) = 3/10, Var(X) = Var(Y) = 1, e Cov(X, Y) = 0. Com base nessas informações, julgue o item a seguir.
X e Y são independentes.

Item. 10. (CESPE/2021 - PC/SE) Considere duas variáveis aleatórias, X e Y, tais que P(X > 0) = 1,
P (X < 1) =

1/10, P (X < 11Y > 1) = 3/10, Var(X) = Var(Y) = 1, e Cov(X, Y) = 0. Com base nessas informações, julgue o item a seguir.
Var(X-Y) = 2

Item. 11. (CESPE/2020 - ME) Considerando que R representa uma variável quantitativa cuja média,
mediana yy e variância são, respectivamente, iguais a 70, 80 e 100, e que U = — — 7, julgue o próximo item,acerca das variáveis U e R.
A correlação linear entre as variáveis U e R é igual a zero.

Item. 12. (CESPE/2020 - ME) Considerando que R representa uma variável quantitativa cuja média,
mediana yy e variância são, respectivamente, iguais a 70, 80 e 100, e que U = — — 7, julgue o próximo item,acerca das variáveis U e R.
A variável U possui média nula.

Item. 13. (CESPE/2020 - SEFAZ-DF) A partir de uma amostra aleatória simples de tamanho n, sabe-se que a média aritmética de uma variável X foi igual a 3.
Considerando que os valores possíveis para a variável X sejam -1 e +4, julgue o item que se segue.

A distribuição da variável X é simétrica em torno da sua média.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 14. (CESPE/2020 - ME - Adaptada)

A
P(A)

-1

20%

70%

10%

B
P(B)

-1

20%

60%

20%

Considerando que as tabelas precedentes mostram as variáveis categorizadas AeB, que foram codificadas em três níveis numéricos de resposta: -1, 0,1, julgue o item que se segue.
A média da variável A é negativa.

Item. 15. (CESPE/2020 - ME - Adaptada)

A
P(A)

-1

20%

70%

10%

B
P(B)

-1

20%

60%

20%

Considerando que as tabelas precedentes mostram as variáveis categorizadas AeB, que foram codificadas em três níveis numéricos de resposta: -1, 0,1, julgue o item que se segue.
As modas e as medianas das variáveis AeB são iguais a zero.

Item. 16. (CEBRASPE/2018 - ABIN - Adaptada) Julgue o item que se segue. Se X e Y
forem variáveis independentes e tiverem distribuição com médias px e pY, respectivamente, e variâncias ax2 e oy2,respectivamente, então a soma X + Y terá média px + pY e variância ax2 + aY2.

Item. 17. (CEBRASPE/2016 - TCE/PR) A quantidade de parcelas (X) escolhida por um cliente para o pagamento de determinado serviço é uma variável aleatória discreta com função de probabilidade, paraP(X = K) 7-k / 21, para k G {1, 2,..., 6} e P(X = K) = 0, para K £ {1,2,...6}.

No que se refere a essa variável aleatória, assinale a opção correta.

a) A esperança E(3X - 8) é igual a zero.

b) P(X< 2) >0,5

c) P(X2 = 1) = 4/49

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

d) A esperança de X é igual ou superior a 3.

e) A variância da variável aleatória X é igual ou superior a 3.

Item. 18. (CEBRASPE/2015 - TELEBRAS) Considerando que Yi, Y₂, Yn, ... sejam variáveis aleatórias independentes que satisfazem P(Yj = j) = P(Yj = -j) = 1/2 para j = 1, 2,..., julgue o item que se segue.
O conjunto de valores que a variável aleatória Yi + Y₂ + Y₃ pode assumir é igual a {-6, -4, -2, 0,
2, 4, 6}.

Item. 19. (CEBRASPE/2015 - TELEBRAS) Um vendedor de certo tipo de equipamento de telecomunicações pode visitar, em um dia, um ou dois clientes, com probabilidades de 1/3 e 2/3,respectivamente. De cada contato pode resultar a venda de um equipamento por R$ 50.000, com probabilidade de 1/10 ou nenhuma venda, com probabilidade de 9/10.
Considerando que V seja a variável aleatória que indica o valor total de vendas diárias desse vendedor, em milhares de reais, julgue o item que se segue.
Se p representar a função de probabilidade de V, então p(0) = 0,84.

Item. 20. (CEBRASPE/2015 - TELEBRAS) Um vendedor de certo tipo de equipamento de telecomunicações pode visitar, em um dia, um ou dois clientes, com probabilidades de 1/3 e 2/3,respectivamente. De cada contato pode resultar a venda de um equipamento por R$ 50.000, com probabilidade de 1/10 ou nenhuma venda, com probabilidade de 9/10.
Considerando que V seja a variável aleatória que indica o valor total de vendas diárias desse vendedor, em milhares de reais, julgue o item que se segue.
A probabilidade de esse vendedor fechar exatamente uma venda em um dado dia é superior a 0,09.

Item. 21. (CEBRASPE/2015 - TELEBRAS) Um vendedor de certo tipo de equipamento de telecomunicações pode visitar, em um dia, um ou dois clientes, com probabilidades de 1/3 e 2/3,respectivamente. De cada contato pode resultar a venda de um equipamento por R$ 50.000, com probabilidade de 1/10 ou nenhuma venda, com probabilidade de 9/10.
Considerando que V seja a variável aleatória que indica o valor total de vendas diárias desse vendedor, em milhares de reais, julgue o item que se segue.
O valor esperado da variável aleatória V é maior que 5 e indica, em milhares, o valor total esperado de vendas em cada dia.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 22. (CEBRASPE/2015 - TELEBRAS) Roberto comprou, por R$ 2.800,00, rodas de liga leve para seu carro,e, ao estacionar no shopping, ficou indeciso sobre onde deixar o carro, pois, caso o coloque no estacionamento público, correrá o risco de lhe roubarem as rodas, ao passo que, caso o coloque no estacionamento privado, terá de pagar R$ 70,00, com a garantia de que eventuais prejuízos serão ressarcidos pela empresa administradora.
Considerando que p seja a probabilidade de as rodas serem roubadas no estacionamento público, que Xseja a variável aleatória que representa o prejuízo, em reais, ao deixar o carro no estacionamento público,e que Y seja a variável aleatória que representa o valor, em reais, desembolsado por
Roberto ao deixar o carro no estacionamento pago, julgue o item subsequente.
O conjunto de valores possíveis para a variável aleatória X é X(W) = {2.800, 70, 0}.

Item. 23. (CEBRASPE/2015 - TELEBRAS) Roberto comprou, por R$ 2.800,00, rodas de liga leve para seu carro,e, ao estacionar no shopping, ficou indeciso sobre onde deixar o carro, pois,
caso o coloque no estacionamento público, correrá o risco de lhe roubarem as rodas, ao passo que, caso o coloque no estacionamento privado, terá de pagar R$ 70,00, com a garantia de que eventuais prejuízos serão ressarcidos pela empresa administradora.
Considerando que p seja a probabilidade de as rodas serem roubadas no estacionamento público, que Xseja a variável aleatória que representa o prejuízo, em reais, ao deixar o carro no estacionamento público,e que Y seja a variável aleatória que representa o valor, em reais, desembolsado por
Roberto ao deixar o carro no estacionamento pago, julgue o item subsequente.
Supondo-se que Roberto tome sua decisão escolhendo aleatoriamente entre suas opções, se p = 0,05, então o valor esperado para o prejuízo/valor desembolsado por Roberto será inferior a R$ 100,00.
Item. 24. (CEBRASPE/2015 - TELEBRAS) Roberto comprou, por R$ 2.800,00, rodas de liga leve para seu carro,e, ao estacionar no shopping, ficou indeciso sobre onde deixar o carro, pois,
caso o coloque no estacionamento público, correrá o risco de lhe roubarem as rodas, ao passo que, caso o coloque no estacionamento privado, terá de pagar R$ 70,00, com a garantia de que eventuais prejuízos serão ressarcidos pela empresa administradora.
Considerando que p seja a probabilidade de as rodas serem roubadas no estacionamento público, que Xseja a variável aleatória que representa o prejuízo, em reais, ao deixar o carro no estacionamento público,e que Y seja a variável aleatória que representa o valor, em reais, desembolsado por
Roberto ao deixar o carro no estacionamento pago, julgue o item subsequente.
Se Roberto tomar sua decisão escolhendo aquela cuja variável aleatória correspondente tenha menor valor esperado, então será mais vantajoso para ele deixar o carro no estacionamento pago apenas se p >0,025.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 25. (CEBRASPE/2015 - Departamento Penitenciário Nacional)

2002 2004 2006 2008

ano

Dado que a participação dos presidiários em cursos de qualificação profissional é um aspecto importante para a reintegração do egresso do sistema prisional à sociedade, foram realizados levantamentos estatísticos, nos anos de 2001 a 2009, a respeito do valor da educação e do trabalho em ambientes prisionais. Cada um desses levantamentos, cujos resultados são apresentados no gráfico,produziu uma estimativa anual do percentual P de indivíduos que participaram de um curso de qualificação profissional de curta duração, mas que não receberam o diploma por motivos diversos.
Em 2001, 69,4% dos presidiários que participaram de um curso de qualificação profissional não receberam o diploma. No ano seguinte, 2002, esse percentual foi reduzido para 61,5%, caindo, em 2009, para30,9%.

A partir das informações e do gráfico apresentados, julgue o item que se segue.

O coeficiente de variação do percentual P é negativo, pois o gráfico de dispersão entre ano e percentual Pmostra uma tendência de redução deste último ao longo do tempo.

Item. 26. (CEBRASPE/2013 - MPU) Considere uma máquina fabril cuja operação tenha se iniciado às 8 h da quarta-feira do dia 2/1/2003 e haja se estendido durante cinco dias úteis por semana,sem feriados, de 8
h às 18 h.

Considere, ainda, que essa máquina tenha produzido 400 peças, das quais 380 sejam aproveitáveis, até parar por quebra de um componente às 10 h do dia 12/2/2003.
Com base nessas informações, julgue o item seguinte.

Variáveis aleatórias não possuem valores firmes, pois seus valores variam sob a influência de fatores casuais.Assim, conhecer uma variável aleatória não significa conhecer seu valor numérico nem enumerar seus valores possíveis, mas sim considerar as probabilidades de a variável assumir cada valor possível de saída de um experimento a ela associado.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 27. (CESPE/2011 - SEDUC-AM) Para orientar os investimentos em educação em certo município, um analista foi contratado para criar um ranking das escolas públicas desse município.Para cada escola, as variáveis disponíveis são a quantidade de turmas, a quantidade de alunos, a quantidade de professores, a nota da Prova Brasil e a área do terreno.
A partir dessa situação, julgue o item.

Considere que as áreas de todas as escolas desse município sejam distintas e que cada escola tenha obtido uma nota diferente na prova Brasil. Nessa situação, os modelos de probabilidade para variáveis aleatórias discretas são adequados para representar a distribuição de todas as variáveis analisadas por esse analista.
Item. 28. (CESPE/2011 - EBC) Julgue o item a seguir, considerando dois eventos A e B, de um mesmo espaço amostrai S, tais que P(A) > 0 e P(B) > 0.
Considere que IA e IB sejam, respectivamente, as variáveis indicadoras referentes aos eventos A e B, de modo que, por exemplo, IA = 1 se o evento A ocorre e IA = 0 se o evento A não ocorre. Nesse caso, a covariância nula entre as variáveis aleatórias IA e IB não garante que os eventos A e B sejam independentes.
Item. 29. (CESPE/2010 - ABIN) Sabendo que X é uma variável aleatória discreta, 0 < p < 1 e k,
número natural,
julgue o item abaixo.

P(X < k) = (1 — p)k é uma função de probabilidade acumulada.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. ERRADO 11. ERRADO
Item. 21. CERTO

Item. 2. CERTO 12. CERTO
Item. 22. ERRADO

Item. 3. CERTO 13. ERRADO
Item. 23. ERRADO

Item. 4. ERRADO 14. CERTO
Item. 24. CERTO

Item. 5. ERRADO 15. CERTO
Item. 25. ERRADO

Item. 6. CERTO 16. CERTO
Item. 26. CERTO

Item. 7. ERRADO 17. LETRA A
Item. 27. ERRADO

Item. 8. CERTO 18. CERTO
Item. 28. ERRADO

Item. 9. ERRADO 19. CERTO
Item. 29. ERRADO

Item. 10. CERTO 20. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

