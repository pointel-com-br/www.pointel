# Probabilidade e Estatística - Medidas de Variabilidade ou Dispersão

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Medidas de Dispersão

2) Amplitude Total

3) Amplitude Interquartílica

4) Desvios em Relação à Média Aritmética eMediana

5) Desvio Absoluto Médio

6) Variância

7) Desvio-Padrão

8) Coeficiente de Variação (ou DispersãoRelativa)

9) Variância Relativa

10) Questões Comentadas - Amplitude Total - Cebraspe

11) Questões Comentadas - Amplitude Interquartílica - Cebraspe

12) Questões Comentadas - Desvios em Relação à Média Aritmética eMediana -Cebraspe

13) Questões Comentadas - Desvio Absoluto Médio - Cebraspe

14) Questões Comentadas - Variância - Cebraspe

15) Questões Comentadas - Desvio-Padrão - Cebraspe

16) Questões Comentadas - Coeficiente de Variação (ou Dispersão Relativa) -Cebraspe

17) Lista de Questões - Amplitude Total - Cebraspe

18) Lista de Questões - Amplitude Interquartílica - Cebraspe

19) Lista de Questões - Desvios em Relação à Média Aritmética e Mediana -Cebraspe

20) Lista de Questões - Desvio Absoluto Médio - Cebraspe

21) Lista de Questões - Variância - Cebraspe

22) Lista de Questões - Desvio-Padrão - Cebraspe

23) Lista de Questões - Coeficiente de Variação (ou DispersãoRelativa) - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

MEDIDAS DE VARIABILIDADE

Nas aulas anteriores, estudamos mecanismos para encontrar valores (média, mediana e moda) que sintetizam o comportamento dos elementos de um conjunto de dados. Esses valores fornecem parâmetros significativos para uma análise dos dados, porém, também é importante identificarmos como variam ou como se diferenciam as características dos elementos de um conjunto.
Imagine, por exemplo, que você precise avaliar três grupos de alunos, cada um com cinco elementos, no que diz respeito ao domínio de uma determinada matéria. Os testes mostraram os seguintes resultados:
Grupos

A = 7,7,7,7,7

B = 5,6,7,8,9

C = 1,4,10,10,10

Para analisar esses dados, podemos, inicialmente, calcular a média aritmética dos três grupos. Concluímos,então, que todos possuem a mesma média aritmética (x = 7). Contudo, ao observarmos a variação dos dados, percebemos que os grupos se comportam de maneira diferente, apesar de todos possuírem a mesma média.
Grupo A

r> Média

*

*

*

X
I
X
I

0 1 2 3 4 5 6 7 8 9 10 11

Grupo B

í* Média i
X X * X X

0 1 2 3 4 5 6 7 8 9 10 11

Grupo C

[* Média

1 X

X

X X 1 X

0123456789 10 11

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nesse caso, a média, embora seja uma medida representativa do conjunto, não indica o grau de homogeneidade ou heterogeneidade existente entre os valores que compõem o conjunto.Desse modo,
precisamos recorrer a procedimentos matemáticos que possibilitem a compreensão da discrepância existente entre os valores do conjunto.
As medidas de dispersão (ou variabilidade) são justamente métricas que mostram a variação dos dados de um conjunto. Elas podem ser divididas em dois grupos:
a) medidas de dispersão absoluta:

amplitude total;
amplitude interquartílica;
desvio médio;

- variância; e desvio-padrão.
b) medidas de dispersão relativa:

coeficiente de variação (de Pearson); e variância relativa.
Nessa aula, aprenderemos a medir o grau de concentração ou dispersão dos dados em torno da média. Para isso, estudaremos as principais medidas de dispersão, que são: amplitude total,amplitude interquartílica,
desvio médio, variância, desvio padrão, coeficiente de variação e variância relativa.

HORA DE

PRATICAR!

í (COC-UFAC/UFAC/2019) Analise as seguintes assertivas:
I

: I. A moda e o desvio padrão são medidas de dispersão,

: II. O desvio médio e a média são medidas de dispersão,

; III. O coeficiente de variação e a variância são medidas de dispersão,

: IV. A moda, a média e o desvio padrão são medidas de posição.

= Pode-se afirmar que estão corretas:

: a) Apenas I. e II.

b) Apenas II. e III.

= c) Apenas III.

d) Apenas IV.

= e) Apenas I. e IV.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

; Comentários:

= As medidas de posição consistem em valores que representam a tendência de concentração dos dados
: observados. As medidas de posição mais importantes são as medidas de tendência central. Nesse grupo,
= encontram-se as medidas mais utilizadas: média aritmética, moda e mediana.

: Já as medidas de dispersão medem o grau de variabilidade dos elementos de uma distribuição. A
dispersão

= aumenta à proporção que o valor da medida de dispersão também aumenta. As principais medidas de dispersão são amplitude, desvio médio, variância, desvio padrão e coeficiente de variação.
j Gabarito: C.

: (VUNESP/MPE-SP/2016) Na estatística, são considerados medidas de dispersão:
I

: a) média e moda.

b) percentil e coeficiente de variação.

: c) amplitude total e percentil.

d) amplitude total e desvio padrão.

= e) variância e média.

; Comentários:

; As medidas de tendência central estudam o centro da amostra. As medidas de tendência central mais utilizadas são a média aritmética, a mediana e a moda.
: Por sua vez, as medidas de separatrizes dividem os dados em grupos com a mesma quantidade de elementos,
= sendo representadas pelos quartis, decis e percentis.

= Por fim, as medidas de dispersão têm a finalidade de identificar o quanto os dados estão dispersos em torno da média de uma amostra. São dadas pelos coeficientes de variação, desvio padrão, amplitude e variância,
j Gabarito: D.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

AMPLITUDE ToTAL

A amplitude total (ou simplesmente amplitude) é a diferença entre os valores extremos de um conjunto de observações, ou seja, a diferença entre o maior e o menor elemento desse conjunto:
%máx Xmín

Essa medida de dispersão chama atenção por ser extremamente simples e muito fácil de se calcular.Contudo, há uma certa restrição quanto ao seu uso por conta de sua grande instabilidade, vez que leva em consideração apenas os valores extremos da série.
Por exemplo, vamos comparar os conjuntos A e B da tabela a seguir:

Conjunto Média Amplitude total

A = 5,7,8,9,10,11,55 x = 15 At = 55 - 5 = 50

B = 12,13,14,15,16,17,18 x = 15 At = 18 - 12 = 6

Reparem que as médias aritméticas dos dois conjuntos são iguais a 15. Portanto, no que diz respeito a essa medida de posição, podemos considerá-los idênticos. Porém, ao calcularmos a amplitude total, verificamos que os valores do conjunto A apresentam um grau de dispersão bem maior que os do conjunto B.
Isso acontece porque, no cálculo da amplitude total, desconsideramos os valores da série que se encontram entre os extremos, o que pode conduzir a interpretações equivocadas. Com frequência, um valor discrepante pode afetar a medida de maneira acentuada. É o caso, por exemplo,do último valor (55)
do conjunto A, sensivelmente maior que seu antecessor (11), que elevou a magnitude da amplitude total para 50.
Além disso, a amplitude total também é sensível ao tamanho de amostra. Normalmente, a amplitude total tende a aumentar com o incremento do tamanho da amostra, ainda que não proporcionalmente. Ainda, a amplitude total pode apresentar muita variação de uma amostra para outra, ainda que extraídas de uma mesma população.
Apesar das limitações dessa medida, há situações em que ela pode ser aplicada de forma satisfatória. É o caso, por exemplo, da variação da temperatura em um dia. Também é o caso de quando uma compreensão rápida dos dados é mais relevante que a exatidão de um procedimento complexo.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Amplitude Total para dados não-agrupados

Para dados não agrupados, o cálculo da amplitude total pode ser expresso pela seguinte fórmula:

%máx Xmín em que xmá% é o maior elemento; e xmín é o menor elemento do conjunto.
EXEMPLIFICANDO

Calcular a amplitude total dos conjuntos apresentados a seguir:

A = 50,50,50,50,50,50,50

B = 47,48,49,50,51,52,53

C = 20,30,40,50,60,70,80

Aplicando a fórmula anterior para esses dados, obtemos os seguintes resultados:

X-máx -^mín = 50 - 50 = 0

Xmáx Xmin = 53 -47 = 6

X-máx -^mín = 80 - 20 = 60

Nesse caso, podemos observar que o conjunto A obteve uma amplitude total igual a 0, ou seja, uma dispersão nula. Então, significa que os valores não variam entre si. Oconjunto B, por sua vez, obteve uma amplitude igual a 6. Já a variável C teve uma amplitude total igual a 60.
Embora o valor da amplitude total seja diferente para os conjuntos A, B e C, todos possuem a mesma média aritmética (50). Independentemente da média, verificamos que o conjunto A possui elementos mais homogêneos do que os conjuntos B e C. E, também, que os elementos do conjuntoB são mais homogêneos do que os do conjunto C.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Amplitude Total para dados agrupados sem intervalos de classes

Para dados agrupados SEM intervalos de classe, a fórmula usada para a identificação da amplitude total é similar à adotada para dados não-agrupados. A única diferença consiste na identificação dos valores mínimo e máximo, que agora ocorre por meio de uma tabela de frequências.
EXEMPLIFICANDO

Calcular a amplitude total da tabela de frequências apresentada a seguir.

1 10

3 15

5 10

7 8

9 7

Nesse caso, como 1 e 9 são os valores mínimo e máximo da variável xz, temos o seguinte resultado:

X-máx X-rnín

At = 9 - 1 = 8

É importante ressaltar que esses valores foram selecionados independentemente da frequência associada a eles.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Amplitude Total para dados agrupados em classes

Para dados agrupados em intervalos de classe, podemos definir a amplitude total de duas formas:

1) pela diferença entre o limite superior da última classe (LSUp) e o limite inferior da primeira classe conforme expresso na fórmula a seguir:
2) pela diferença entre o ponto médio da última classe (PMÚU) e o ponto médio da primeira classe (PMprl),
conforme expresso na fórmula a seguir:

A = PMúlt - PMpri

EXEMPLIFICANDO

Calcular a amplitude total da distribuição de frequências apresentada a seguir:

Classes I PM{ I

1 l- 5 3 5

5l-9 7 10

9 H 13 11 15

13 1- 17 15 10

17 1- 21 19 5

Total 45

Pelo primeiro método, temos que o limite superior da última classe é 21,
enquanto o limite inferior da primeira classe é 1. Portanto, temos a seguinte amplitude:
A ~ LSup ~ hnf
A = 21 - 1 = 20

Pelo segundo método, temos que o ponto médio da última classe é 19,
enquanto o ponto médio da primeira classe é 3. Portanto, temos a seguinte amplitude:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A = PMült ~ PMpri

,4 = 19 — 3 = 16

Observe que a amplitude é menor pelo segundo método, porque os extremos da distribuição são desconsiderados.
HORA DE

PRATICAR!

i (COPEVE (UFAL)/Pref. Maceió/2012) Um registro em saúde epidemiológica apresenta os dados: 3, 4, 7, 8
= e 8. Se calcularmos 8-3 = 5, estaremos determinando:

j a) a amplitude total.

= b) o primeiro quartil.

; c) o desvio médio.

i d) a distância interquartílica.

; e) o terceiro quartil.

; Comentários:

A amplitude total (ou simplesmente amplitude) é a diferença entre os valores extremos de um conjunto de
= observações, ou seja, a diferença entre o maior e o menor elemento desse conjunto.

j Gabarito: A.

: (VUNESP/Pref. de São José dos Campos/2012) A diferença entre o maior e o menor valor em um conjunto j de dados é denominado (a)
= a) curva normal.

b) amplitude total.

= c) média.

d) média ponderada.

= e) moda.

; Comentários:

A diferença entre o maior e o menor valor em um conjunto de dados é denominada de amplitude (ou
: amplitude total).

j Gabarito: B.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Propriedades da Amplitude Total

Nesse tópico, estudaremos as principais propriedades da amplitude total:

1- Propriedade

* Somando-se (ou subtraindo-se) uma constante c a todos os valores de uma variável, a amplitude do conjunto não é alterada.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência {xn} = {3, 6, 8,9,10}, cuja amplitude total é:

4) -X-máx -^mín

A = 10 - 3 = 7

Se adicionarmos o número 5 a cada um dos termos da sequência, obteremos uma nova lista {yn} =
{xn + 5} = {8,11,13,14,15}, cuja amplitude total é:

A = 15 - 8 = 7

Logo, a adição do número 5 a cada um dos termos da sequência fez com que a amplitude permanecesse inalterada.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

2- Propriedade

* Multiplicando-se (ou dividindo-se) todos os valores de uma variável por uma constante c, a amplitude do conjunto fica multiplicada (ou dividida) por essa constante.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência {xn} = {8,11,13,14,15}, cuja amplitude total é:

xm(jX xmín
A - 15 - 8 - 7

Se multiplicarmos cada um dos termos da sequência por 5, obteremos uma nova lista {yn} —
(xn x 5} = {40,55,65,70, 75}, cuja amplitude total é:

A - 75 - 40 - 35

Logo, a multiplicação de cada um dos termos da sequência por 5 fez com que a amplitude total do conjunto também fosse multiplicada por 5.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

AMPLITUDE INTERQUARTÍLICA

Como já sabemos, denominamos de quartis os valores de uma série que a dividem em quatro partes iguais,isto é, quatro partes contendo o mesmo número de elementos (25%). A imagem a seguir mostra os quartis de uma distribuição hipotética:
Temos, então, 3 quartis (Çi, Q2 e Ç₃) para dividir uma série em quatro partes iguais:

* Çx: 0 primeiro quartil corresponde à separação dos primeiros 25% de elementos da série;

* Q₂ - o segundo quartil corresponde à separação de metade dos elementos da série, coincidindo com a mediana (Q₂ = Md);
* Q₃: o terceiro quartil corresponde à separação dos primeiros 75% de elementos da série, ou dos últimos 25% de elementos da série.
A amplitude interquartílica (ou distância interquartílica, ou intervalo interquartílico) é 0 resultado da subtração entre 0 terceiro quartil e 0 primeiro quartil:
AIQ — Ç3 — Qi

A amplitude semi-interquartílica (ou desvio quartílico) é definida como a metade desse valor, sendo calculada pela expressão apresentada a seguir:
Q3 ~ Qi

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

FIQUE

ATENTO!

Reparem que a fórmula da amplitude interquartílica (ou distância interquartílica)
é muito parecida com a fórmula da amplitude semi-interquartílico (ou desvio quartílico),podendo ser facilmente confundida.
HORA DE

PRATICAR!

í (AOCP/SUSIPE-PA/2018) Quartis são valores que dividem os dados de uma amostra em quatro grupos, i
; cada um deles contendo 1/4 do tamanho total da amostra. Em relação ao assunto, informe se é verdadeiro ;j (V) ou falso (F) o que se afirma a seguir e assinale a alternativa com a sequência correta.

; () O primeiro quartil Q1 tem 1/4 dos dados acima dele e 3/4 dos dados abaixo dele.

= () O terceiro quartil Q3 tem 3/4 dos dados abaixo dele e 1/4 dos dados acima dele.

; () O quartil Q3 é a própria mediana.

= () A distância interquartílica é dada por DIQ = Q3 - Ql.

í a) V-F-F-V.
í b)F-V-F-V.;

; c) F-V-V-V.

i d) V-V-F-V.:

e) F-V-F-F.

; Comentários:

= Vamos analisar cada assertiva:

: Item 1 - O primeiro quartil Ql tem 1/4 dos dados acima dele e 3/4 dos dados abaixo dele.
;

= Falso. O primeiro quartil (Ql) tem 1/4 (25%) dos dados abaixo dele e 3/4 (75%) acima dele.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item 2 - O terceiro quartil Q3 tem 3/4 dos dados abaixo dele e 1/4 dos dados acima dele.

Verdadeiro. De fato, o terceiro quartil (Q3) tem 3/4 (75%) dos dados abaixo dele e 1/4 (25%) acima dele
: Item 3 - O quartil Q3 é a própria mediana.

; Falso. A terceira assertiva é falsa, pois a mediana é equivalente ao segundo quartil (Q2).

: 4 - A distância interquartílica é dada por DIQ = Q₃ - Qx.

: Verdadeiro. Essa é a exata definição de distância interquartílica.

; Gabarito: B.

Propriedades da Amplitude Interquartílica

A seguir, veremos que a amplitude interquartílica e o desvio quartílico possuem as mesmas propriedades da amplitude total.
1- Propriedade

* Somando-se (ou subtraindo-se) uma constante c a todos os valores de uma variável, a amplitude interquartílica (e o desvio quartílico) do conjunto não é alterada.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência {xn} = {1,3, 5, 7,9,11,13},
cuja amplitude interquartílica é:
^IQ - Q3 ~ Ql

Aiq = 11 - 3 = 8

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Se adicionarmos o número 5 a cada um dos termos da sequência, iremos obter uma nova lista }yn} =
{xn + 5} = {6,8,10,12,14,16,18}, cuja amplitude interquartílica é:

^iq = Q3 ~ Qi
A!Q = 16 - 8 = 8

Logo, a adição do número 5 a cada um dos termos da sequência fez com que a amplitude interquartílica permanecesse inalterada.
Propriedade

* Multiplicando-se (ou dividindo-se) todos os valores de uma variável por uma constante c, a amplitude interquartílica (e o desvio quartílico) do conjunto fica multiplicada (ou dividida) por essa constante.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência {%„} — {1,3,5,7,9,11,13}, cuja amplitude interquartílica é:
^iq — Qz ~ Qi
AÍQ = 11-3 = 8

Se multiplicarmos cada um dos termos da sequência por 5, iremos obter uma nova lista {yn} —
[xn x 5} = [5,15,25,35,45,55,65}, cuja amplitude interquartílica é:

^iq — Q-3 ~ Qi

Aiq = 55 - 15 = 40

Logo, a multiplicação de cada um dos termos da sequência por 5
fez com que a amplitude interquartílica do conjunto também fosse multiplicada por 5.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DESVIoS EM RELAçÃo À MÉDIA ARITMÉTICA E MEDIANA

Antes de apresentarmos as fórmulas para o cálculo do desvio médio e da variância,
precisamos compreender qual o conceito de desvio em estatística. Um desvio é a distância entre qualquer observação do conjunto de dados e uma medida descritiva desse conjunto:
desvio = observação — medida

Em especial, destacamos os desvios em relação à média aritmética e em relação à mediana:

di = x — x (média)

ou di — x — Md (mediana)
É natural pensarmos que, quando os desvios em relação a uma medida descritiva são pequenos, as observações estão concentradas em torno dessa medida e, portanto, a variabilidade dos dados é pequena.Agora, quando os desvios são maiores, significa que as observações estão dispersas e,
portanto, a variabilidade dos dados é grande.
(VUNESP/TJ-SP/2015) Leia o texto a seguir para responder à questão. Uma pequena empresa que emprega apenas cinco funcionários paga os seguintes salários mensais (em mil reais):
0,9 1,2 1,4 1,5 2,0

Considerando-se a média dos salários, o valor do desvio do salário de quem ganha R$ 1.400,00
mensais é a) -1.000.
b) -400.

c) 0.

d) 200.

e) 400.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para responder a questão, primeiro teremos que calcular a média:

0,9 + 1,2 + 1,4 + 1,5 + 2

Então, o desvio em relação ao salário de R$ 1.400 é:

di = x
1400 - 1400 = 0

Gabarito: C.

(VUNESP/TJ-SP/2015) Leia o texto a seguir para responder à questão. Uma pequena empresa que emprega apenas cinco funcionários paga os seguintes salários mensais (em mil reais):
0,9 1,2 1,4 1,5 2,0

Somando-se os valores absolutos dos desvios individuais dos salários tomados em relação à média,encontra-se o valor de a) 1.400,00.
b) 1.200,00.

c) 1.000,00.

d) 800,00.

e) 0.

Comentários:

Como vimos na questão anterior, a média dos salários é:

0,9 + 1,2 + 1,4 + 1,5 + 2

X_ = 5

x = - => x = 1,4 mil

Agora, calcularemos os desvios para cada valor apresentado:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Valor Desvio Desvio absoluto
0,9 0,9 - 1,4 = -0,50 0,5

1,2 1,2 - 1,4 = -0,2 0,2

1,4 1,4 - 1,4 = 0 0

1,5 1,5 - 1,4 = 0,1 0,1

2 2 - 1,4 = 0,6 0,6

Total 1,4

Portanto, a soma dos desvios absolutos é 1,4 mil.

Gabarito: A.

Propriedades dos Desvios em Relação à Média Aritmética e
Mediana

Nesse tópico, revisaremos algumas propriedades importantes dos desvios sobre as quais discutimos quando estudamos sobre a média e a mediana.
1- Propriedade

* A soma algébrica dos desvios em relação à média é nula.

EXEMPLIFICANDO

Vamos tomar como exemplo a sequência {xn} = {1,2, 3,4, 5, 6, 7}, com média x = 4. O desvio em relação à média é a diferença entre cada elemento da sequência e a média aritmética. Como a sequência possui 7 elementos, teremos o mesmo número de desvios para calcular. Logo, basta encontrarmos a diferença entre cada elemento e a média:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, somaremos todos esses desvios:

d₄ = x₄ — x = 1 — 4 = —3
d₂ = x₂ — x = 2 — 4 = —2
d₃ = x₃ — x = 3 — 4 = —1

d₄ = x₄ — x= 4 — 4 =0

d₅ = x₅ — x= 5 — 4 =1

d₆ — x₆ — x— 6 — 4 =2

d₇ — x₇ — x— 7 — 4 =3

df - dx + d2 + d3 + ^4 "I" ^5 + d6 + ^7

7—1

i=l dt = (-3) + (-2) + (-1) + 0 + 1 + 2 + 3
^> = 0

i=l

Portanto, não importa qual a sequência de números, a soma dos desvios em relação à média é sempre igual a zero.
2- Propriedade

* A soma dos quadrados dos desvios da sequência de números {xj, em relação a um número a, é mínima se a for a média aritmética dos números.
EXEMPLIFICANDO

Novamente, vamos tomar como exemplo a sequência {xn} = {1,2,3,4, 5, 6, 7},
com média x = 4.
Já calculamos os desvios desses números em relação à média:

d₄ = x₄ — x = 1 — 4 = —3

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

d₂ = x₂ — x = 2 — 4 = — 2
d₃ = x₃ — x = 3 — 4 = —1

d₄ = x₄— x =4 — 4 =0

d₅ = x₅— x = 5 - 4 =1

d₆ — x₆— x —6 — 4 =2

d₇ — x₇— x —7 — 4 =3

Na propriedade anterior, vimos que a soma dos desvios é sempre igual a zero. Agora, calcularemos a soma dos quadrados desses desvios. Em outras palavras, vamos elevar cada um deles ao quadrado e somar todos os resultados:
i=l d[ = d( + d2 + cZ| + d4 + d| + dg + d7
^dt = (—3)2 + (—2)2 + (-1)2 + O2 + l2 + 22 + 32
Í=1

i=l

— 9 + 4 + 1 + 0 + 1 + 4 + 9

^dL = 28
í=i

A propriedade nos garante que, para essa sequência numérica, o valor 28 é o menor valor possível.Isto é, se encontrarmos os desvios em relação a outro número (diferente da média) e, em seguida,calcularmos a soma dos quadrados dos desvios, o valor obtido será maior que
Item. 28. Vamos ver o que acontece ao calcularmos o desvio em relação ao número 6:
di = x₄ — x = 1 — 6 = —5
d₂ = x₂ — x = 2 — 6= — 4
d₃ = x₃ — x = 3 — 6= — 3
d₄ = x₄ — x = 4 — 6= — 2
d₅ = x₅ — x = 5 — 6= — 1
d₆ = x₆ — x = 6 — 6 = 0

d₇ — x₇ — x — 7 — 6 = 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, calcularemos a soma dos quadrados desses números:

Como esperávamos, o resultado foi maior do que 28.

3- Propriedade

* A soma dos desvios absolutos de uma sequência de números, em relação a um número a, é mínima quando a é a mediana dos números.
EXEMPLIFICANDO

Vamos tomar como exemplo a série {xn} = {1,2, 3,4, 6,7,8,9}. Como o número de termos é par, a mediana será, por convenção, a média aritmética dos dois termos centrais:
O desvio em relação à mediana corresponde à diferença entre cada elemento da sequência e a mediana. Como são 8 números, temos a mesma quantidade de desvios para calcular. Logo, basta encontrarmos a diferença entre cada número e a mediana:
d-t = x± — Md = 1 — 5 = —4
d₂ = *2 — = 2 — 5 = —3
d₃ = %₃ — Md = 3 — 5 = —2

d₄ = x₄ — Md = 4 — 5 = — 1

d5 = x5 — Md = 6 —5 =1

d6 = x6 — Md = 7 —5 =2

d7 = x7 — Md = 8 —5 =3

d8 = x8 — Md = 9 —5 =4

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, precisamos somar os valores absolutos desses desvios:

i=l

= |dil + |d₂l + M3I + I^UI + 1^51 + l^ól + 1^71 + 1^81

£|d(l = 1-41 + |-3| + 1-21 + l-ll + |1| + |2| + |3| + |4|

i=l i=l
| di | — 4+3+2+1+1+2+3+4— 20

A propriedade garante que, ao calcularmos a soma dos desvios absolutos em relação à mediana, o menor valor que encontraremos para essa sequência será 20.
Há um detalhe importante que precisamos esclarecer. Como vimos anteriormente, quando o número de elementos do conjunto é ímpar, o valor da mediana é único e igual ao termo central.Porém, quando o número de elementos é par, a mediana pode ser qualquer valor entre os termos centrais, havendo infinitos valores possíveis para a mediana. Por convenção,contudo, adotamos a média aritmética dos valores centrais.
Certo, o que isso tem a ver com a propriedade que estamos estudando?
Significa dizer que, se calcularmos a soma dos desvios absolutos para qualquer valor entre 4 e 6,que são os termos centrais, o valor dos desvios absolutos em relação a mediana também será mínimo. A título exemplificativo, vamos calcular os desvios em relação ao valor 4,5:
di = — 4,5 = 1 — 4,5 = —3,5

d2 = x2 — 4,5 = 2 — 4,5 = —2,5

d3 = %3 — 4,5 = 3 — 4,5 = —1,5

d4 = x4 — 4,5 = 4 — 4,5 = —0,5

d₅ = x₅ — 4,5= 6 — 4,5 = 1,5

d₆ — x₆ — 4,5— 7 — 4,5 —2,5

d₇ — x₇ — 4,5— 8 — 4,5 —3,5

d₈ — x₈ — 4,5— 9 — 4,5 —4,5

Somando os valores absolutos desses desvios:

^JdJ = |dj + |d21 + |d31 + |d4| + |d5| + |d6| + |d7| + |d8|

i=i

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

^JdJ = 1-3,51 + |-2,5| + 1-1,5| + 1-0,5| + |1,5| + |2,5| + |3,5| + |4,5|

i=l i=l
\dt | = 3,5 + 2,5 + 1,5 + 0,5 + 1,5 + 2,5 + 3,5 + 4,5 = 20

Como havíamos previsto, o valor também foi igual ao valor mínimo, 20.

Por último, a propriedade também garante que, para qualquer valor fora do intervalo entre 4 e 6,encontraremos um valor maior que o mínimo. Por exemplo, vamos calcular os desvios em relação ao valor 7:
d₄ — x₄ —7 — 1 — 7— — 6

d₂ — x₂ —7 — 2 — 7 = — 5

d₃ = x₃ —7 = 3 — 7 = —4

d₄ = x₄ —7 = 4 — 7 = —3

d₅ = x₅ —7 = 6 — 7 = — 1

d₆ = %₆ — 7= 7 — 7 =0

d₇ = x₇ — 7= 8 — 7 =1

d₈ = x₈ — 7= 9 — 7 =2

Somando os valores absolutos desses desvios:

^JdJ = |dx | + |d21 + |d31 + |d4| + |d51 + |d6| + |d7| + |d8|

i=i

£|d(| = |-6| + |-5| + |-4| + |-3| + l-ll + |0| + |1| + |2|

i=l i=l j \di | — 6 + 5 + 4 + 3 + 1 + 0 + 1 + 2 — 22
Portanto, como havíamos previsto anteriormente, o valor foi maior que o mínimo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos resumir as propriedades dos desvios da seguinte forma:

l5) a soma dos desvios em relação à média aritmética é sempre nula;

2^) a soma dos quadrados dos desvios em relação à média aritmética é mínima; e

35) a soma dos módulos dos desvios em relação à mediana é mínima.

INDO MAIS

FUNDO!

Caso o número de elemento seja par, a soma dos módulos também será mínima se os desvios forem calculados em relação a um dos valores centrais. Isto é, também será mínima a soma dos módulos dos desvios calculados em relação a qualquer termo no intervalo os termos centrais.
Xn, Xn+l

- 2 21"

, em que xn e xn+1 são

2 2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

r i í (FCC/TRE-SP/2012) Dado um conjunto de observações, indicadas por Xt (i = 1,2,3,..., n), o desvio el da i

: i-ésima observação em relação a um valor «éef = Xt — ae |ej é o valor absoluto de ei. Considere as j j seguintes afirmações para qualquer conjunto de observações:
; I. O valor de X e,2 é mínimo se a for igual à média aritmética das observações.
i II. O valor de XleJ é mínimo se a for igual à mediana das observações.

= III. O valor de X e; é nulo se a for igual à moda das observações.

: IV. O valor de Xl^/I é nulo se a for igual à média aritmética das observações.

= Então, são corretas APENAS

: a) I e II.
:

b) I e III.
:

: c) II e III.
:

d) II e IV.

i

: e) II, III e IV.
:

; Comentários:

= Vamos analisar cada assertiva:

A sentença I é verdadeira, pois a soma dos quadrados dos desvios é mínima quando os desvios são calculados j i em relação à média aritmética.;

A sentença II também é verdadeira, pois a soma dos módulos dos desvios é mínima quando os desvios são j
= calculados em relação à mediana. Em qualquer situação, quando o desvio é calculado em relação à mediana, ;
: a soma dos desvios absolutas é mínima.

A sentença III é falsa, vez que a soma dos módulos dos desvios é nula se os desvios são calculados em relação ;
: à média. Somente seria verdadeira caso a moda fosse igual à média.

A sentença IV é falsa, pois a soma dos desvios absolutos em relação à média somente é nula quando todos j
: os desvios também são nulos, ou seja, se todos os números fossem iguais e não houvesse dispersão dos j dados.=

: Gabarito: A.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DESVIo ABSoLUTo MÉDIo

O desvio absoluto médio, ou simplesmente desvio médio, mede a dispersão entre os valores da distribuição e a média dos dados coletados. Para compreender essa medida, vamos supor que oEstratégia Concursos tenha realizado uma semana de revisão para estudantes da área fiscal, obtendo os seguintes números de visualizações:
semana Número de visualizações

Domingo 2.000
Segunda 4.000

Terça 5.200

Quarta 6.300

Quinta 5.400

Sexta
Sábado

Total

4.100

2.400
y ft = 29.400

Isso significa que a semana de revisão teve uma média diária de 4.200 visualizações.
Esse resultado, porém,
não retrata a realidade com fidedignidade, pois alguns dias tiveram mais visualizações do que a média;enquanto outros não. Por isso, é importante sabermos o quão distante a média está em relação aos valores reais por ela representados.
Para calculá-los, basta subtrairmos o valor da média de cada observação, conforme mostrado a seguir:
Dia da semana Número de visualizações Xi~ X
Domingo 2.000 2.000 - 4.200 = -2.200

Segunda 4.000 4.000 -4.200 = -200

Terça 5.200 5.200 - 4.200 = 1000

Quarta 6.300 6.300 -4.200 = 2.100

Quinta 5.400 5.400 -4.200 = 1.200

Sexta 4.100 4.100 -4.200 = -100

Sábado 2.400 2.400 - 4.200 = -1.800

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Total y ft = 29.400 0

Notem que, ao calcularmos o desvio médio, obtemos resultados positivos e negativos, que se anulam ao serem somados. Percebam que existem valores de observações que estão muito próximos da média,enquanto outros estão mais distantes.

Como a soma de todos os desvios médios é sempre igual a zero para qualquer conjunto de dados (l.s propriedade dos desvios), sabemos que — x) não nos fornecerá nenhuma informação relevante nem nos ajudará a compreender o que está acontecendo com essa variável.
Para superar essa dificuldade, podemos utilizar apenas os resultados positivos dos desvios calculados. Afórmula do cálculo do desvio médio se apresenta da seguinte maneira:

n em que Dm representa o desvio médio, 1%; — x| representa o módulo da diferença entre uma determinada observação e a média calculada, representa a frequência de um determinado valor para a variável da distribuição, e n representa o total de elementos formados pela distribuição.
O desvio médio é uma medida de dispersão mais robusta do que a amplitude total e a amplitude interquartílica, pois leva em consideração todos os valores do conjunto. O inconveniente dessa medida é a operação de módulo, que, por conta de suas características matemáticas, torna difícil o estudo de suas propriedades.
Desvio Médio para dados não-agrupados

O desvio absoluto médio (Dm), de um conjunto de n observações xlt , xn, é a média dos valores absolutos das diferenças entre as observações e a média. Isto é,
EHikz -x|

n

As barras verticais indicam a operação de módulo, que é responsável por transformar qualquer número negativo em um número positivo, isto é, retornar o valor absoluto.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

EXEMPLIFICANDO

Calcular o desvio médio do conjunto mostrado a seguir:

{1, 2, 3, 5, 9}

Iniciaremos pelo cálculo da média aritmética:

1+2+3+5+9 20

X~ 5 = _5"_ 4

Vamos montar uma tabela para facilitar o cálculo do desvio médio:

1 (1 - 4) = -3 3

2 (2 - 4) = -2 2

3 (3 - 4) = -1 1

5 (5 - 4) = 1 1

9 (9 - 4) = 5 5

-x| = 12

Aplicando a fórmula do desvio médio, temos:

Ef=1k-4|

n

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

HORA DE

PRATICAR!

(CESPE/ANATEL/2004)

meses

N

fev mar abr mai jun jul ago set out nov
A tabela acima mostra os números mensais de reclamações (N) feitas por usuários de telefonia fixa,registradas em uma central de atendimento, entre os meses de fevereiro a novembro de 2003.Considerando esses dados, julgue os itens que se seguem.

O maior desvio absoluto dos números mensais de reclamações registradas é superior a 45.

Comentários:

Iniciaremos pelo cálculo da média:

100 + 70 + 70 + 60 + 50 + 100 + 50 + 50 + 30 + 20 600

Agora, calcularemos o módulo (valor absoluto) de cada um dos desvios.

|dx| = |%! — x| = |100 - 60| = 40

|d2| = |x2 -x| = |70 - 60| = 10

|d3| = |x3-x| = |70 - 60| = 10

|d41 = |x4 — x| = 160 - 601 = 0

|d5| = |x5 -x| = |50 - 60| = 10

|d6| = |x6 — x| = |100 - 60| = 40

|d7| = |x7-x| = |50 - 60| = 10

|d8| = |x8-x| = |50 - 60| = 10

|d9| = |x9 — x| = |30 - 60| = 30
l^iol = l*io — x| = 120 — 601 = 40

O maior desvio absoluto é 40, portanto, o item está incorreto.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(CESPE/ANATEL/2004)

meses

N

fev mar abr mai jun jul ago set out nov
A tabela acima mostra os números mensais de reclamações (N) feitas por usuários de telefonia fixa,registradas em uma central de atendimento, entre os meses de fevereiro a novembro de 2003.Considerando esses dados, julgue os itens que se seguem.

O desvio médio absoluto da sequência formada pelos números mensais de reclamações é um valor entre 25e 35.

Comentários:

Para calcular o desvio absoluto médio, temos que encontrar a média dos valores absolutos (módulos) dos desvios.
40 + 10 + 10 + 0 + 10 + 40 + 10 + 10 + 30 + 40 _ 200

Dm ~ 1Õ
" 1Õ"

Dm = 20

Gabarito: Errado.

Desvio Médio para dados agrupados sem intervalo de classe

Quando os valores vierem dispostos em uma tabela de frequências, o desvio médio será calculado por meio da seguinte fórmula:
Em que m indica o número de grupos em que os dados estão organizados; e \xt — x|
representa o módulo da diferença entre uma determinada observação e a média calculada.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

EXEMPLIFICANDO

Durante uma pesquisa, o Estratégia Concursos registrou a quantidade de filhos de seus professores,obtendo a tabela de frequências apresentada a seguir. Vamos calcular o desvio médio dessa distribuição.
l\P de filhos por professor fi Xi^fi
* Pesquisa V = 2Q V x. x = 30
populacional >

Iniciaremos pelo cálculo da média aritmética:

_ 2 %i X fi x~ Zfi
= — = 1,50 filhos / professor

\J

Em seguida, adicionaremos uma nova coluna à tabela anterior, em que calcularemos os produtos dos desvios absolutos por suas respectivas frequências:
N2 de filhos por professor fi %í X |Xí - x| X /í
0 4 0 |0 - 1,5| x 4 = 6

1 8 8 |1 - 1,5| x 8 = 4

2 4 8 |2 - 1,5| x 4 = 2

3 2 6 |3 - 1,5| x 2 = 3

4 2 8 |4 — 1,5| x 2 = 5

* Pesquisa populacional
2>=20 XjX fi = 30 -x| xf = 20

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por fim, aplicando a fórmula do desvio médio, temos:

Y\Xi -x\ X /

D = -

m Yfi

= 2Õ_ 1

Desvio Médio para dados agrupados em classes

Se os dados estiverem agrupados em classe, deveremos adotar a mesma convenção que tomamos para o cálculo da média: vamos assumir que todos os valores coincidem com os pontos médios das suas respectivas classes.
EXEMPLIFICANDO

Durante uma pesquisa, o Estratégia Concursos registrou as estaturas de
40 alunos, obtendo a distribuição de frequências apresentada a seguir. Calcule o desvio médio dessa distribuição.
Frequência

Estaturas

(ft)

150 1- 154 4

154 H 158 9

158 R162 11

162 1- 166 8

166 1- 170 5

170 1- 174 3

* Pesquisa amostrai
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Inicialmente, construiremos uma tabela como a mostrada a seguir:

Estaturas

Frequência

(A) Xi Vfi Oi - X) |xÉ -x|
|Xj - x| X fí

150 H 154 4 152 608 -9
9 36

154 1- 158 9 156 1.404 -5
5 45

158 H 162 11 160 1.760 -1
1 11

162 1- 166 8 164 1.312 3
3 24

166 1- 170 5 168 840 7
7 35

170 1- 174 3 172 516 11
11 33

* Pesquisa amostrai
ZA = 40 xt x ft = 6.440
^|xz

— X| x = 184

Feito isso, podemos calcular a média da distribuição por meio da seguinte fórmula:

6.440

% = = !61 40

Conhecendo a média, completamos a tabela com as diferenças e os produtos necessários para o cálculo do desvio médio. Assim, aplicando a fórmula do desvio médio, temos:
4Õ"

4,6 cm

Portanto, o desvio médio para essa distribuição de estaturas é 4,6 cm.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

HORA DE

PRATICAR!

r................ .. ................ .. .................... .. .................... ..

(UEPA/SEFAZ-PA/2013) A tabela abaixo representa as estaturas dos jogadores de voleibol que disputaram a Liga Mundial de 2012.
ESTATURAS

(cm)

NÚMERO
DE
JOADORES

180 H 190 10

190 H 200 30

200 H 210 10

z

O desvio médio da estatura dos jogadores é:

a) 2

b) 4

c) 6

d) 8

e) 10

Comentários:

Vamos iniciar pelo cálculo da média. Para isso, construiremos uma coluna com os pontos médios e multiplicaremos cada um pela sua respectiva frequência. Da seguinte forma:
Estaturas fi Xi Xf X fi

180 1- 190 10 185 10 X 185 = 1.850

190 1- 200 30 195 30 X 195 = 5.850

200 1- 210 10 205 10 X 205 = 2.050

Total = 50 = 9.750

Portanto, a média é:

9.750

* = 50 =195

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em seguida, adicionaremos uma coluna para calcularmos os módulos dos desvios:

Estaturas I fi xf x, X fi
|xj-x|

180 1- 190 10 185 10 X 185 = 1.850 |185 - 195| = 10

190 1- 200 30 195 30 X 195 = 5.850 |195 - 195|= 0

200 1- 210 10 205 10 X 205 = 2.050 |205 - 195| = 10

Total ^/, = 50 ^x,- Xf,- = 9.750

Para calcular o desvio médio, devemos multiplicar cada desvio absoluto pela sua respectiva frequência.Depois, basta somar tudo e dividir por n.

Estaturas fi xf xf x ff
|Xí -x| |X( - x| x fi

180 l- 190 10 185 10 x 185 = 1.850 |185 - 195| =
10 10 x 10 = 100

190 1- 200 30 195 30 X 195 = 5.850 |195 - 195|=
0 0 X 30 = 0

200 F 210 10 205 10 x 205 = 2.050 |205 - 195| =
10 10 x 10 = 100

Total Z/<-5° y^XiXfi = 9.750

£|xf-x| Xfi = 200

Drtanto, o desvio médio é:

n _ Ekí -%| xf _ 200 _

Gabarito: B.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Propriedades do Desvio Médio

Nesse tópico, vamos aprender as principais propriedades do desvio médio.

1- Propriedade

* Somando-se (ou subtraindo-se) uma constante c a todos os valores de uma variável, o desvio médio do conjunto não é alterado.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência — [1,3, 5,7,9}, cuja desvio médio é:

|1 - 5| + |3 - 5| + |5 - 5| + |7 — 5| + |9 - 5|

4+2+0+2+4 12

5 T

Se adicionarmos o número 5 a cada um dos termos da sequência, iremos obter uma nova lista [yn] =
[xn + 5} = [6,8,10,12,14}, cujo desvio médio é:

|6 - 10| + |8 - 10| + |10 - 10| + |12 - 10| + |14 — 10|

4 + 2 + 0 + 2 + 4 12

5 "1F

Logo, a adição do número 5 a cada um dos termos da sequência fez com que o desvio médio permanecesse inalterado.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

2- Propriedade

* Multiplicando-se (ou dividindo-se) todos os valores de uma variável por uma constante c, o desvio médio do conjunto fica multiplicado (ou dividido) por essa constante.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência [xn] — [1,3, 5,7,9}, cujo desvio médio é:

|1 — 5| + |3 — 5| + |5 — 5| + |7 — 5| + |9 — 5|
r

4 + 2 + 0 + 2 + 4 12

Se multiplicarmos cada um dos termos da sequência por 5, iremos obter uma nova lista £yn} =
{xn x 5} = {5,15,25,35,45}, cujo desvio médio é:

|5 - 25| + 115 - 25| + |25 - 25| + |35 - 25| + |45 - 25|

20 + 10 + 0 + 10 + 20 60

Logo, a multiplicação de cada um dos termos da sequência por 5 fez com que o desvio médio do conjunto também fosse multiplicado por 5.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

VARIÂNCIA (CT2)

Existem outras formas de se eliminar o problema com os números negativos. Além da operação de módulo,podemos trabalhar com potências pares. A utilização de potências de expoente par, como o número dois,além de transformar números negativos em positivos, simplifica o cálculo.

A variância é determinada pela média dos quadrados dos desvios em relação à média aritmética. Por meio dessa medida de dispersão ou variabilidade, podemos avaliar o quanto os dados estão dispersos em relação à média aritmética. Nesse sentido, quanto maior a variância, maior a dispersão dos dados.
A variância leva em consideração a totalidade dos valores da variável em estudo, e não apenas os valores extremos, como faz a amplitude total. Por isso, essa medida de variabilidade é considerada muito estável.Além disso, a variância complementa as informações obtidas pelas medidas de tendência central.

Até o momento, as medidas que estudamos não sofriam nenhuma alteração quando o cálculo era realizado para uma amostra. Contudo, para a variância, devemos levar em consideração essa informação, pois há uma pequena diferença entre o cálculo da variância populacional e da variância amostrai.
A variância populacional é simbolizada pela letra grega cr (sigma), sendo calculada usando todos os elementos da população, pela seguinte fórmula:
,2 g=1(x,~M)2

n em que: xt é o valor de ordem i assumido pela variável; /z é a média populacional de x; cr2 é a variância populacional; enéo número de dados da população.
A variância amostrai é simbolizada pela letra s, sendo calculada a partir de uma amostra da população, pela seguinte fórmula:
em que: xt é o valor de ordem i assumido pela variável; x é a média amostrai de x; s2 é a variância amostrai;enéo número de dados da amostra.

Normalmente, uma população possui uma grande quantidade de elementos, o que inviabiliza a realização de um estudo aprofundado de suas medidas, chamadas de parâmetros populacionais.Nesse caso,
recorremos ao estudo de amostras representativas dessa população, buscando obter indícios do valor correto do parâmetro populacional desconhecido. Esse valor amostrai é denominado de estimador do parâmetro populacional.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em nosso caso, a variância populacional cumpre o papel de parâmetro populacional,
enquanto a variância amostrai atua como um estimador. Já vimos a variância populacional e a variância amostrai são representadas por símbolos diferentes: cr2 e s2. O mesmo acontece com a média populacional e a média amostrai, que também possuem símbolos diferentes: jU (parâmetro populacional) e x (estimador).
Reparem que, quando a variância representa uma descrição da amostra e não da população, caso mais frequente em estatística, o denominador das expressões deve ser n - 1, em vez de n.Isso ocorre porque a utilização do divisor (n — 1) resulta em uma melhor estimativa do parâmetro populacional.
Além disso, como a soma dos desvios em relação à média aritmética é sempre nula,
apenas (n - 1) dos desvios (%i - x) são independentes, vez que (n — 1) desvios determinam automaticamente o valor desconhecido. Para amostras grandes (n > 30), não há diferença significativa entre os resultados proporcionados pela utilização de qualquer dos dois divisores, nou (n- 1).
Em determinadas situações, a aplicação dessas fórmulas pode requerer um esforço considerável. É o caso do que acontece quando a média não é um número natural, situação em que a obtenção da soma dos quadrados dos desvios se torna muito trabalhosa. Por isso, é importante aprendermos outras fórmulas que podem nos ajudar no cálculo da variância.
Já ouviram dizer que a variância é igual à média dos quadrados menos o quadrado da média? Pois bem,essa é a fórmula que expressa a variância populacional:

em que x2 é a média dos quadrados; e (x)2 é o quadrado da média.

Como vimos, para encontrarmos a fórmula da variância amostrai, basta substituirmos n por (n — 1). Isso é equivalente a multiplicarmos a variância populacional por É exatamente o que faremos agora:
em que x2 é a média dos quadrados; (x)2 é o quadrado da média; enéo tamanho da amostra.

Por fim, é importante ressaltarmos que, por ser calculada a partir dos quadrados dos desvios, a variância é um número em unidade quadrada em relação à variável em questão, o que pode ser considerado um inconveniente. Por isso, essa medida tem pouca utilidade na estatística descritiva, mas é extremamente importante na inferência estatística e em combinações de amostras. Por exemplo, se os dados estiverem expressos em quilogramas (Kg), a variância estará expressa em quilogramas ao quadrado (Kg2).
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TOME

NOTA!

Símbolo da variância populacional:

Símbolo da variância amostrai:

FIQUE

ATENTO!

A variância de um conjunto é zero quando todos os elementos são iguais. Se todos os elementos são iguais, a média aritmética do conjunto coincide com o valor dos elementos e todos os desvios também são iguais a zero. Logo, a variância também é zero.
A variância é sempre maior ou igual a zero, isto é, sempre tem valor positivo.

Fórmula da variância populacional:

OU <72 = X2 — (x)2

Fórmula da variância amostrai:

s2 _ S"=l(Xi-x)2

n-1

OU S2 = [x2 - (x)2] X

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Variância para dados não-agrupados

Para dados não agrupados, a variância pode ser expressa por meio das seguintes fórmulas:

a) para populações

~ M)2

n ou (T2 n b) para amostras
A relação entre a variância amostrai (s2) e a variância populacional (o2) é dada por:

EXEMPLIFICANDO

Calcular a variância amostrai do conjunto de números mostrado a seguir:

[1,2,3,5,9}

Iniciaremos pelo cálculo da média aritmética:

1 + 2 + 3 + 5 + 9 20

Agora, vamos montar uma tabela para facilitar o cálculo da variância:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Xi I (Xí - x)2

1 (1 - 4)2 =9

2 (2 — 4)2 =4

3 (3 — 4)2 =1

5 (5 — 4)2 =1

9 (9 - 4)2 = 25

V (%Í - x)2 = 40

Por fim, aplicando a fórmula da variância amostrai, temos:

- x)2

n — 1

5-1

HORA DE

PRATICAR!

(VUNESP/TJ-SP/2015) Dados os valores de uma variável: 5, 10, 15, 20, 25, as variâncias amostrai e populacional são, respectivamente,
a) 14,7 e 15.

b) 125 e 250.

c) 62,5 e 50.

d) 29,4 e 30,8.

e) 83,3 e 85.

Comentários:

Vamos começar calculando a média:

5 + 10 + 15 + 20 + 25

Agora, vamos encontrar os desvios em relação à média:

d₁ = 5-15 = -10

d₂ = 10 - 15 = -5

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

d₃ = 15 - 15 = 0

d₄ = 20- 15 = 5

d₅ = 25 - 15 = 10

Para calcular a variância (populacional ou amostrai), precisamos calcular a soma dos quadrados dos desvios,isto é:

d? = (-10)2 + (—5)2 + O2 + 52 + 102
y d? = 250

Nesse momento, dividiremos esse valor por n para encontrar a variância populacional e por n — 1 para encontrar a variância amostrai:
£d? 250 250

s = = -—- = —— = 62,5 (variância amostrai)

n-1 5—1 4

, Ydl 250

cr2 = = —— = 50 (variância populacional)

n 5

Gabarito: C.

Variância para dados agrupados sem intervalos de classes

Quando os valores vierem dispostos em uma tabela de frequências, a variância será calculada por meio de uma das seguintes fórmulas:
a) para populações b) para amostras n — 1
ou s2 2=

n - 1

Em quen = Zí=i/i e% = t-1^ .

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

EXEMPLIFICANDO

Durante uma pesquisa, o Estratégia Concursos registrou a quantidade de filhos por professor,obtendo a tabela de frequências apresentada a seguir. Sendo assim,
calcule a variância amostrai dessa tabela.
l\P de filhos por professor fi XiXfi
* Pesquisa V y. = ₂0 V x< X £ = 30
populacional

Iniciaremos pelo cálculo da média aritmética:

_ £ XiXfi x= Yft
= — = 1,50 filhos / professor

\J

Em seguida, adicionaremos uma nova coluna à tabela anterior, em que calcularemos os produtos dos quadrados dos desvios por suas respectivas frequências:
l\P de filhos por professor fi X; X fi (xÉ - x)2 X fi
0 4 0 (0 - 1,5)2 x 4 = 9

1 8 8 (1 — 1,5)2 x8 = 2

2 4 8 (2 - 1,5)2 x 4 = 1

3 2 6 (3 - 1,5)2 x 2 = 4,5

4 2 8 (4- 1,5)2 x 2 = 12,5

* Pesquisa populacional
2/ = 2° Xj x f = 30 ^(xí-x)2x/í = 29

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por fim, aplicando a fórmula do desvio padrão amostrai, temos:

- %)2 X fj n — 1
— = 1,52

Variância para dados agrupados em classes

Para dados contínuos agrupados em classes, a variância é calculada por meio das seguintes expressões:
a) para populações b) para amostras
Observem que as fórmulas são praticamente iguais as apresentadas no subtópico anterior.
A diferença básica é que agora vamos utilizar o ponto médio das k classes.
EXEMPLIFICANDO

Durante uma pesquisa, o Estratégia Concursos registrou as estaturas de
40 alunos, obtendo a distribuição de frequências apresentada a seguir. Vamos calcular a variância amostrai dessa distribuição.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Estaturas

Frequência

(A)

150 b 154 4

154 b 158 9

158 b 162 11

162 b 166 8

166 b 170 5

170 b 174 3

* Pesquisa amostrai
Inicialmente, construiremos uma tabela como a mostrada a seguir:
Frequência

Estaturas

(A)

Xi *fi (Xf - x) (Xj - x)2 (Xj - X)2
X fi

150 b 154 4 152 608 -9
81 324

154 b 158 9 156 1.404 -5
25 225

158 b 162 11 160 1.760 -1
1 11

162 b 166 8 164 1.312 3
9 72

166 b 170 5 168 840 7
49 245

170 b 174 3 172 516 11
121 363

* Pesquisa populacional
^/< = 40 x, x ft = 6.440
£(xê-x)2 xfi = 1.240

Feito isso, podemos calcular a média da distribuição por meio da seguinte fórmula:

Conhecendo a média, completamos a tabela com as diferenças e os produtos necessários para o cálculo da variância. Agora, aplicando a fórmula da variância amostrai, temos:
~ x)2 x fi _ SXifci ~ 161)2 X fj n — 1 ~ 40-1
1.240

31,79 cm2

A variância amostrai das estaturas é 31, 79 cm2.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Propriedades do Variância

Nesse tópico, vamos aprender as principais propriedades da variância.

1- Propriedade

* Somando-se (ou subtraindo-se) uma constante c a todos os valores de uma variável, a variância do conjunto não é alterada.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência — [1,3, 5,7,9}, cuja variância é:

, (1 - 5)2 + (3 - 5)2 + (5 - 5)2 + (7 - 5)2 + (9 - 5)2

a = 5

16 + 4 + 0 + 4 + 16

tf 2 = - = 8

Se adicionarmos o número 5 a cada um dos termos da sequência, iremos obter uma nova lista £yn} =
[xn + 5} — [6,8,10,12,14}, cuja variância é:

, (6 - 10)2 + (8 - 10)2 + (10 - 10)2 + (12 - 10)2 + (14 - 10)2

16 + 4 + 0 + 4 + 16

tf2 = - = 8

Logo, a adição do número 5 a cada um dos termos da sequência fez com que a variância permanecesse inalterada.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

2- Propriedade

* Multiplicando-se (ou dividindo-se) todos os valores de uma variável por uma constante c, a variância do conjunto fica multiplicada (ou dividida) pelo QUADRADO dessa constante.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência {xn} = [1, 3, 5, 7,9], cuja variância é:

, (1 - 5)2 + (3 - 5)2 + (5 - 5)2 + (7 - 5)2 + (9 - 5)2

a = 5

„ 16 + 4 + 0 + 4 + 16

Se multiplicarmos cada um dos termos da sequência por 5, iremos obter uma nova lista {yn} =
{xn x 5} = {5,15,25,35,45}, cuja variância é:

, (5 - 25)2 + (15 - 25)2 + (25 - 25)2 + (35 - 25)2 + (45 - 25)2

a = 5

, 400 + 100 + 0 + 100 + 400

cr2 = - = 200

Logo, a multiplicação de cada um dos termos da sequência por 5 fez com que a variância do conjunto fosse multiplicada por 52 = 25.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DESVIo-PADRÃo (<T)

O desvio padrão (s ou oj é definido como sendo a raiz quadrada da média aritmética dos quadrados dos desvios e, dessa forma, é determinado pela raiz quadrada da variância. É uma das medidas de variabilidade mais utilizadas porque é capaz de apontar de forma mais precisa a dispersão dos valores em relação à média aritmética.
Valores muito próximos da média resultarão em um desvio-padrão pequeno, enquanto valores mais espalhados levarão a desvios maiores. Essa medida será sempre maior ou igual a zero. Ela será igual a zero quando todos os elementos do conjunto forem iguais.
O desvio padrão é utilizado para comparar a variabilidade de dois conjuntos de dados diferentes quando as médias forem aproximadamente iguais e quando as unidades de medidas para os dois conjuntos forem idênticas.
A fórmula para o cálculo do desvio padrão populacional é:

a =

A

- M)2

n

Para o desvio padrão amostrai, a fórmula é a seguinte:

s = 2"=i(Xí - x)2

A n — 1

Como vimos no tópico anterior, a utilização do divisor (n — 1) resulta em uma melhor estimativa do parâmetro populacional. Além disso, como a soma dos desvios em relação à média aritmética é sempre nula,apenas (n - 1) dos desvios (Xj — x) são independentes, uma vez que esses (n — 1)
desvios determinam automaticamente o valor desconhecido.
Por fim, o desvio-padrão é expresso nas mesmas unidades dos dados originais. Tanto o desvio padrão como a variância são usados como medidas de dispersão ou variabilidade. O uso de uma medida ou de outra dependerá da finalidade que se tiver em mente.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TOME

NOTA!

Símbolo do desvio-padrão populacional:

<7

Símbolo do desvio-padrão amostrai:

s

FIQUE

ATENTO!

O desvio-padrão será igual a zero quando todos os elementos forem iguais. Se todos os elementos forem iguais, a média aritmética do conjunto será igual ao valor dos elementos e todos os desvios também serão iguais a zero. Logo, o desvio-padrão também será zero.
O desvio-padrão é sempre maior ou igual a zero, isto é, sempre tem valor positivo.

Fórmula do desvio-padrão populacional:

Fórmula do desvio-padrão amostrai:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

HORA DE

PRATICAR!

r .

í (VUNESP/ARTESP/2018) Numa série composta por n dados, todos de mesmo valor x (x 0),
o valor do i desvio padrão 5 é:
b) s = 0

d) s = x e) s = 1
Comentários:

Como todos os dados são iguais, todos os desvios são nulos. Consequentemente, os quadrados dos desvios também são nulos. Logo, a variância e 0 desvio-padrão serão iguais a zero.
Gabarito: B.

(UFMT/Pref. de Cáceres-MT/2017) Um conjunto de dados sobre a plaquetopenia de pacientes com dengue tem variância igual a zero. Pode-se concluir que também vale zero a) a média.
b) 0 desvio padrão.

c) a mediana.

d) a moda.

Comentários:

O desvio-padrão é a raiz quadrada da variância. Nesse caso, como a variância é igual a zero, então 0 desvio-padrão vale:

o = Võ = 0.

Gabarito: B.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Desvio-padrão para dados não-agrupados

Para dados não agrupados, o desvio-padrão pode ser expresso por meio das seguintes fórmulas:

a) para populações

X? (xi - M)* 1 2 3

a =

A

b) para amostras

EXEMPLIFICANDO

Vamos calcular o desvio-padrão amostrai do conjunto de números mostrado a seguir:

(1,2,3,5,9}

Iniciaremos pelo cálculo da média aritmética:

1 + 2 + 3 + 5 + 9 20

x' = 5 = T = 4

Em seguida, montaremos uma tabela para facilitar o cálculo do desvio padrão:

Xj I (Xj - x)2

1 (1 - 4)2 =9

2 (2 - 4)2 =4

3 (3 - 4)2 =1

5 (5 - 4)2 -1

9 (9 — 4)2 = 25

V (Xi - x)2 = 40

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por fim, aplicando a fórmula do desvio padrão temos:

s, HORA DE

PRATICAR!

i (FCC/ARTESP/2017) O departamento de operações de uma autarquia do Estado fez um levantamento do
: número de acidentes em um determinado trecho de rodovia no ano de 2016, conforme tabela a seguir.

Mês

N° de Acidentes

Jan

Fev

Mar

Abr

Mai

Jun

Jul

Ago

Set

Out

Nov

Dez

; Os números indicam que há uma dispersão significativa, portanto, o desvio padrão para esta amostra é
; representado por a) 13,30.
b) 14,33.

c) 12,74.

d) 10,40.

: e) 11,50.

; Comentários:

Vamos iniciar calculando a média:

36 + 28 + 12 + 5 + 3 + 2 + 2 + 4 + 9 + 11 + 22 + 38

X =

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, vamos montar uma tabela para simplificar o cálculo da média dos quadrados:

Valor (x) X2

36 1.296

28 784

12 144

5 25

3 9

2 4

2 4

4 16

9 81

11 121

22 484

38 1.444

Total 4.412

= Portanto, a média dos quadrados é:

í 4.412

i x2 == 367,67

A variância populacional é dada pela diferença entre a média dos quadrados e o quadrado da média:

: cr2 = x2 — x2

a2 = 367,67 - (14,33)2

cr2 = 367,67 — 205,35

: a2 = 162,32

i Se multiplicarmos a variância populacional por^-y, encontraremos a variância amostrai:

= _ 12

s2 = 162,32 x —

: 11

: s2 = 162,32 x 1,09

s2 = 177,07

í s = Vl77,07

s = 13,30

: Gabarito: A.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(CESPE/Polícia Federal/2018)

X (quantidade diária de drogas apreendidas, em kg)
dia

1 2 3 4 5

10 22 18 22 28

Tendo em vista que, diariamente, a Polícia Federal apreende uma quantidade X, em kg,
de drogas em determinado aeroporto do Brasil, e considerando os dados hipotéticos da tabela precedente, que apresenta os valores observados da variável X em uma amostra aleatória de 5 dias de apreensões no citado aeroporto, julgue o próximo item.
O desvio padrão amostrai da variável Xfoi inferior a 7

Comentários:

Começaremos calculando a média:

Agora, vamos encontrar os desvios:

10 + 22 + 18 + 22 + 28

5 = 2°

dx = 10-20 = -10

d₂ = 22 - 20 = 2

d₃ = 18 - 20 = -2

d₄ = 22 - 20 = 2

d₅ = 28 - 20 = 8

Para calcular a variância (populacional ou amostrai), precisamos calcular a soma dos quadrados dos desvios,isto é:

df = (-10)2 + 22 + (—2)2 + 22 + 82

d? = 176

Nesse momento, dividiremos esse valor por n — 1 para encontrarmos a variância amostrai:

, £ d? 176 176

s2 = 1 =----------- = = 44

n-1 5-1 4

E, por fim, o desvio padrão é a raiz quadrada da variância:

s = V44

O enunciado diz que esse valor é menor do que 7kg. De fato, sabemos que 72 = 49, logo V44 < 7.

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Desvio-padrão para dados agrupados sem intervalo de Classe

Quando os valores vierem dispostos em uma tabela de frequências, o desvio-padrão será calculado por meio de uma das seguintes fórmulas:
a) para populações

S" i(rf? X A)

n b) para amostras yp
Em que n = £™ifi e x = — n

EXEMPLIFICANDO

Durante uma pesquisa, o Estratégia Concursos registrou a quantidade de filhos de seus professores,obtendo a tabela de frequências apresentada a seguir. Vamos calcular o desvio-padrão amostrai dessa distribuição.
N5 de filhos por professor fi XiXfl
'pe,squlsa, Ví =20 YX,X/, = 30
populacional «

Iniciaremos pelo cálculo da média aritmética:

x= sr, == — = 1,50 filhos / professor

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em seguida, adicionaremos uma nova coluna à tabela anterior, em que calcularemos os produtos dos quadrados dos desvios por suas respectivas frequências:
l\P de filhos por professor fi X; X fi (xÉ - X)2 X fí
0 4 0 (0 - 1,5)2 x 4 = 9

1 8 8 (1 — 1,5)2 x8 = 2

2 4 8 (2 - 1,5)2 x 4 = 1

3 2 6 (3 - 1,5)2 x 2 = 4,5

4 2 8 (4 - 1,5)2 x 2 = 12,5

* Pesquisa populacional
2/ = 2° ^ Xj x fi = 30 ^\xt - x)2 x = 29

Por fim, aplicando a fórmula do desvio padrão amostrai, temos:

SOí -x)2 *fi n — 1
s =

Desvio-padrão para dados agrupados em classes

Quando tivermos que calcular o desvio-padrão para dados agrupados em classes,
usaremos as mesmas fórmulas para dados sem intervalos de classes, utilizando para xt os pontos médios de cada classe, mas adotando os mesmos procedimentos.
EXEMPLIFICANDO

Durante uma pesquisa, o Estratégia Concursos registrou as estaturas de
40 alunos, obtendo a distribuição de frequências apresentada a seguir. Vamos calcular o desvio-padrão amostrai dessa distribuição.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Estaturas

Frequência
(/í)

150 H 154 4

154 1- 158 9

158 H 162 11

162 1- 166 8

166 I- 170 5

170 H 174 3

* Pesquisa amostrai S'< =40
Inicialmente, construiremos uma tabela como a mostrada a seguir:

Estaturas

Frequência
(A)

Xi^fi (Xí - x) Çxt - xY Çxt - xY x ft

150 1- 154 4 152 608 -9
81 324

154 1- 158 9 156 1.404 -5
25 225

158 1- 162 11 160 1.760 -1
1 11

162 1- 166 8 164 1.312 3
9 72

166 1- 170 5 168 840 7
49 245

170 1- 174 3 172 516 11
121 363

* Pesquisa 5

populacional

= 40 x A = 6 440
^OÍ-X)2 x/f = 1.240

Feito isso, podemos calcular a média da distribuição por meio da seguinte fórmula:

E PMi x fi 6.440

= —— = 161

X~ Xfi 40

Conhecendo a média, completamos a tabela com as diferenças e os produtos necessários para o cálculo do desvio padrão. Agora, aplicando a fórmula do desvio padrão amostrai, temos:
- x)2 xft_

1 1

- 161)2 x ft 1.240

40-1 " A 39

O desvio-padrão das estaturas é 5,64 cm. Vimos anteriormente que o desvio médio, para essa mesma distribuição, foi de 4,63 cm.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Propriedades do Desvio-padrão

Nesse tópico, vamos estudar as principais propriedades do desvio-padrão.

1- Propriedade

* Somando-se (ou subtraindo-se) uma constante c a todos os valores de uma variável, o desvio-padrão do conjunto não é alterado.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência — [1,3, 5,7,9}, cujo desvio-padrão é:

(1 - 5)2 + (3 - 5)2 + (5 - 5)2 + (7 - 5)2 + (9 - 5)2

/16 + 4 + 0 + 4 + 16 I—

a = J =2V2

Se adicionarmos o número 5 a cada um dos termos da sequência, iremos obter uma nova lista [yn] =
(xn + 5} = [6,8,10,12,14}, cujo desvio-padrão é:

(6 - 10)2 + (8 - 10)2 + (10 - 10)2 + (12 - 10)2 + (14 - 10)2

ll6 + 4 + 0 + 4 + 16

J 5

2V2

Logo, a adição do número 5 a cada um dos termos da sequência fez com que o desvio-padrão permanecesse inalterado.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

2- Propriedade

* Multiplicando-se (ou dividindo-se) todos os valores de uma variável por uma constante c, o desvio-padrão do conjunto fica multiplicado (ou dividido) por essa constante.
EXEMPLIFICANDO

Vamos tomar como exemplo a sequência {xn} = {1, 3, 5, 7,9}, cujo desvio-padrão é:

(1 - 5)2 + (3 - 5)2 + (5 - 5)2 + (7 - 5)2 + (9 - 5)2

16 + 4 + 0 + 4 + 16

cr = 2V2

Se multiplicarmos cada um dos termos da sequência por 5, iremos obter uma nova lista {yn} =
{xn x 5} = {5,15, 25, 35,45}, cujo desvio-padrão é:

1(5 - 25)2 + (15 - 25)2 + (25 - 25)2 + (35 - 25)2 + (45 - 25)2

J 5

I4OO + 100+ 0+ 100+ 400

J 5

Logo, a multiplicação de cada um dos termos da sequência por 5 fez com que o desvio-padrão do conjunto também fosse multiplicado por 5.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

CoEFICIENTE DE VARIAçÃo (oU DISPERSÃo RELATIVA)

O desvio-padrão pode ser utilizado para a comparação de duas ou mais séries de valores, no que diz respeito à variabilidade e dispersão, quando os conjuntos possuem a mesma média e estão expressos na mesma unidade de medida (p.ex., os dois conjuntos em centímetros). Porém, quando os conjuntos de dados estão expressos em unidades diferentes (p.ex., quilogramas e centímetros), precisamos de outra medida.
Para contornar essa limitação do desvio-padrão, podemos caracterizar a dispersão ou variabilidade dos dados de maneira relativa ao seu valor médio. Nesse sentido, o coeficiente de variação é uma medida de dispersão relativa que fornece a variação dos dados em relação à média, podendo ser calculado como:
a) para populações b) para amostras em que: cr é o desvio-padrão populacional; /z é a média populacional; s é o desvio-padrão amostrai; e x é a média amostrai.
O coeficiente de variação pode ser interpretado por meio de algumas regras empíricas:

a) a distribuição tem baixa dispersão se CV < 15%;

b) a distribuição tem média dispersão se 15% < CV < 30%; e c) a distribuição tem elevada dispersão se CV > 30%.
Além disso, quanto menor for o valor do coeficiente de variação, mais homogêneos serão os dados, ou seja,menor será a dispersão em torno da média. Por isso, podemos classificar as distribuições em homogêneas ou heterogêneas, da seguinte forma:
a) a distribuição é homogênea quando possui dispersão baixa ou média (CV < 30%);

b) a distribuição é heterogênea quando possui dispersão elevada (CV > 30%).

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

EXEMPLIFICANDO

Em uma empresa de tecnologia, o salário médio dos homens é de R$ 1800,00
com desvio-padrão de
R$ 810,00 e o salário médio das mulheres é de R$ 1500,00 com desvio padrão de R$ 705,00. Adispersão relativa dos salários dos homens é maior que a das mulheres?

Vamos identificar os dados do problema:

a) para os homens:

b) para as mulheres:

f/zH = 1800
í aH = 810

(HM = 1500

I = 705

Agora, vamos calcular os respectivos coeficientes de variação:

a) para os homens:

b) para as mulheres:

CV = — x 100

Ah

1800

45,0%

CV = — x 100

15ÕÕ

= 47,0%

Portanto, os salários das mulheres apresentam uma dispersão relativa maior que os salários dos homens. Além disso, as duas distribuições possuem uma alta dispersão (CV > 30%).
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

HORA DE

PRATICAR!

r i í (FCC/ALAP/2020) O número de empregados de uma empresa é igual a 200, sendo que 60% são homens e i
; o restante mulheres. Nesta empresa, a média aritmética dos salários da população formada pelos salários j j dos homens é igual a 5 mil reais, com um coeficiente de variação igual a 30%, e a média aritmética dos ;
; salários da população formada pelos salários das mulheres também é igual a 5 mil reais, porém com um :
= coeficiente de variação igual a 20%. Considerando a população formada por todos os 200 empregados da i j empresa, obtém-se que a variância, em mil reais ao quadrado, dos respectivos salários é igual a í a) 1,69
b) 1,75
j

: C) 1,30
:

d) 2,50

: e) 3,25
j

; Comentários:

; Para responder essa questão, encontraremos os dados considerando separadamente os homens e depois ;
: faremos o mesmo processo para as mulheres. Ao final, acharemos o que foi pedido para a população N = ;
: 200.
:

: Segundo a questão, a população tem tamanho igual a 200, isto é,N = 200. Dessa população de empregados, j temos que 60% são homens, ou seja:
60% x 200 = 120 homens.
;

= Consequentemente, o número de mulheres será:

200- 120 = 80 mulheres.

= De acordo com o enunciado, a média aritmética dos salários da população tem coeficiente de variação igual
: a 30%, isto é, CVhomens = 30%. Esse coeficiente é calculado por meio da seguinte fórmula:

: a

:

:
C^homens ~ ~
:

A questão nos informou que a média salarial dos homens é de 5 mil reais, ou seja,
jU = 5 (mil reais). Logo, j

= usando a fórmula acima, conseguiremos encontrar o desvio padrão "populacional" dos homens:

: nnn/ °homens
:

3« = —

^homens 30% X 5

& homens 1/^ (jTtil rcctís^

= Sabemos que a variância é o quadrado do desvio padrão, então:

= ^homens = (X5)2 = 2,25(mil reais}2

;

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Adotaremos o mesmo procedimento para as mulheres. A questão nos informou que a média salarial das mulheres é de 5 mil reais, ou seja, = 5 {mil reais). A única diferença é que o coeficiente de variação das mulheres é igual a 20%, CVmuiheres = 20%.
^mulheres — 1,00 {mil reais)

A variância é o quadrado do desvio padrão, então:

amuiheres = (l,00)2 = l,00{mil reais)2

Agora, consideraremos toda a população N = 200. A média populacional dos salários dos
200 empregados será 5 mil, já que tanto a média salarial dos homens quanto a média salarial das mulheres é igual é igual a 5mil reais. Portanto:

x = 5 {mil reais)

Agora, para encontrar a variância, vamos utilizar a fórmula clássica da variância:

2(%í - x)2

Buscaremos o termo Y{xí — n)2 para homens e mulheres, lembrando sempre que a média é igual a5 {mil reais), tanto para homens quanto para mulheres.

Calculando para os homens:

Y{xt-x)2

{Xi-fi)2 = 2,25 x 120 = 270

Calculando para as mulheres:

^mulheres

£{xí-x)2

{X[ — /z)2 = 1,00 X 80 = 80

Agora, substituiremos esses valores na variância de toda a população, considerando N = 200:

Y{Xj - X)2

Gabarito: B.

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

00551155220001199000- -EEvveertrotonrMurilo Vieira

(FCC/Metrô-SP/2019) Uma empresa possui 40 funcionários dos quais F1 são mulheres e F2
são homens.
Sabe-se que a média salarial das mulheres é de 8 salários mínimos, que a média salarial dos homens é de10 salários mínimos e que a média salarial de todos os 40 funcionários é de 8,6
salários mínimos. Se a variância dos salários dos funcionários do sexo masculino é igual a (F2 + 4)(salários mínimos)2, o coeficiente de variação desses funcionários do sexo masculino é igual a a) 32%.
b) 25%.

c) 36%.

d) 40%.

e) 15%

Comentários:

Conforme o enunciado, uma empresa possui um total de 40 funcionários, sendo um subtotal Fr de mulheres e um subtotal F₂ de homens. Logo,
Fx + F₂ = 40 (Equação 1)

De acordo com a questão, a média salarial das mulheres é 8, enquanto a média salarial dos homens é
10.

^mulheres $
X homens 10

X = 8,6

Calculando a média dos salários para homens e mulheres:

E (salário mulheres') = 8xF₁

E(salário homens)

^2

E(salário homens) = 10 x F₂

A média total pode ser calculada por meio da seguinte expressão:

E(salário mulheres) + E(salário homens)
x = Fi + F

8 x Fi + 10 x F₂

8,6 = 1 - -

Fi +

8,6 x F± + 8,6 x F2 = 8 x F1 + 10 x F2

0,6 x Fx = 1,4 x F2 (Equação 2)

Chegamos, portanto, a uma situação em que temos duas equações e duas incógnitas (Fx e F₂). Podemos isolar a variável Fx na Equação 2 e, em seguida, substituí-la na Equação 1, chegando ao valor deF₂.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

1,4 x F2

0,6

= Substituindo a variável F± na Equação 1, chegamos ao valor de F₂.

; Fi + F₂ = 40 (Equação 1)

\ (I) x F₂ + F₂ = 40

i Multiplicando todos os termos por 3, temos:

7 x F₂ + 3 x F₂ = 120

10 x F₂ = 120

= F2 = 12

: Portanto, o número de homens é 12.

: O enunciado também forneceu a variância, que é equivalente à expressão (F2+4). Isto é:
cr2 = F₂ + 4 = 12 + 4 = 16.

: Então, o desvio padrão será a raiz quadrada da variância:

cr = 4.

= O coeficiente de variação (CV) para os homens será:

: cr 4

i CV = = — =
40%

% homens

: Gabarito: D.

(FCC/TRT 205 Região/2016) Em uma associação de determinada carreira profissional é realizado um censo em que foram apurados os salários de todos os seus 320 associados em número de salários mínimos(S.M.).
O coeficiente de variação correspondente foi de 16% e a soma dos quadrados de todos os salários, em(S.M.)2, foi de 8.204,80. O desvio padrão dos salários destes associados é, em S.M., de a) 0,80
b) 0,64

c) 0,96

d) 0,40

e) 1,60

Comentários:

O coeficiente de variação foi informado na questão. Sabemos que ele é resultado da divisão entre o desvio padrão e a média, então:
16 _a

ÍÕÕ-^

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

100a

X= 16

A variância resulta da diferença entre a média dos quadrados e o quadrado da média. Vamos aplicar o valor da média na fórmula da variância:
cr2 = x2 — x2

2 8.204,80 /100a\2

° ~ 320 \ 16 )

2 8.204,80 10.000a2

~ 320 256

, 32.819,2 - 50.000a2
1280

1280a2 = 32.819,2 - 50.000a2

51280a2 = 32.819,2

2 32.819,2

67 " 51280

a2 = 0,64
a = 7o,64
a = 0,8

Gabarito: A.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

VARIÂNCIA RELATIVA

A variância relativa é uma medida de dispersão relativa que resulta do quociente entre a variância absoluta e o quadrado da média. É basicamente o quadrado do coeficiente de variação. Isto é:
a) para populações b) para amostras
VR = (

/ S\² s²

xJ X2

A variância relativa, assim como o coeficiente de variação, é uma medida adimensional,
ou seja, não tem uma unidade de medida. Repare que tanto o numerador (variância) quanto o denominador (quadrado da média) são expressos na mesma unidade de medida, de modo a se cancelarem no momento da divisão.
EXEMPLIFICANDO

Em uma empresa de tecnologia, o salário médio dos homens é de R$ 1800,00
com desvio-padrão de
R$ 810,00 e o salário médio das mulheres é de R$ 1500,00 com desvio padrão de R$ 705,00. Avariância relativa dos salários dos homens é maior que a das mulheres?

Vamos identificar os dados do problema:

a) para os homens:

(/j.H — 1800
t aH = 810

b) para as mulheres:

ÍMm = 1500
[ aM = 705

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, vamos calcular as respectivas variâncias relativas:

a) para os homens:

b) para as mulheres:

Portanto, os salários das mulheres apresentam uma variância relativa maior que os salários dos homens.
HORA DE

PRATICAR!

(FCC/SEFAZ-BA/2019) O coeficiente de variação de Pearson correspondente a uma população
PI com média aritmética igual a 20 e tamanho 20 é igual a 30%. Decide-se excluir de Pl, em um determinado momento, dois elementos iguais a 11 cada um, formando uma nova população P2. A variância relativa deP2 é igual a a) 10/147.
b) 4/49.

c) 16/147.

d) 8/49.

e) 4/441.

Comentários:

O coeficiente de variação de Pearson é a razão entre o desvio padrão e a média.

Oi

CVn = =

1 *1

= 20 x 0,3 = 6

Logo, a variância de P± é:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Como a variância é a média dos quadrados menos o quadrado das médias, temos:

ffl2=xF-®2

36 = xf — 202

36 = xf -400

X? = 436

Com isso, podemos calcular a soma dos termos:

Xi = 20 x X₁ = 20 x 20 = 400

7 = 1

De igual forma, temos:

^X? = 20 x X2 = 20 x 436 = 8.720

i=l

O enunciado afirma que dois elementos iguais a 11 serão retirados, formando uma nova população P₂- Dessa forma, as novas somas serão iguais a:
Assim, as novas médias são iguais a:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

De posse dessas informações, podemos calcular a nova variância absoluta:

a^=xl- ®2

cr2 = 471 - (21)2

o-2 = 471 - 441

a2 = 30

Finalmente, temos que a variância relativa é a razão entre a variância e o quadrado da média:

Simplificando por 3, temos:

Gabarito: A.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Amplitude Total

Item. 1. (CESPE/SEDF/2017) Um levantamento estatístico, feito em determinada região do país,
mostrou que jovens com idades entre 4 e 17 anos assistem à televisão, em média, durante 6 horas por dia. A tabela a seguir apresenta outras estatísticas produzidas por esse levantamento.
Distribuição dos tempos gastos assistindo televisão(7, em horas)

Io quartil 2

2o quartil 4

3o quartil 8

Io decil 1

9o decil 10

Tendo como referência essas informações, julgue o seguinte item.

A amplitude total dos tempos T é igual ou superior a 9 horas.

Comentários:

A amplitude é calculada pela diferença entre os valores máximos e mínimos da amostra.
Os valores do 9°
decil e do l.e decil foram informados na questão. Assim, para resolvermos a questão,
basta fazermos a subtração dos valores correspondentes ao 9.Q decil e l.Q decil:
10 - 1 = 9

Com isso, sabemos que a amplitude é de, no mínimo, 9.

Gabarito: Certo.

Item. 2. (CESPE/TCE-PA/2016)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

média amostrai desvio padrão amostrai primeiro quartil mediana terceiro quartil mínimo máximo
0,80

0,70

0,25

0,70

1,20

3,10

Um indicador de desempenho X permite avaliar a qualidade dos processos de governança de instituições públicas. A figura mostra, esquematicamente, a sua distribuição, obtida mediante estudo amostrai feito por determinada agência de pesquisa. A tabela apresenta estatísticas descritivas referentes a essa distribuição.
Com base nessas informações, julgue o item a seguir.

A amplitude total da amostra é inferior a 3.

Comentários:

A amplitude (ou amplitude total) é a diferença entre o valor máximo e o mínimo. Esses valores foram apresentados na tabela do enunciado. Então, aplicando esses dados na fórmula, temos:
Gabarito: Errado.

Item. 3. (CESPE/TCE-PA/2016)

A = 3,10 - 0 = 3,10

Número diário de denúncias registradas (X)
Frequência
Relativa

Total

0,3

0,1

0,2

0,1

0,3

1,0

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A tabela precedente apresenta a distribuição de frequências relativas da variável X,
que representa o número diário de denúncias registradas na ouvidoria de determinada instituição pública.A partir das informações dessa tabela, julgue o item seguinte.
A amplitude total da amostra é igual ou superior a 5.

Comentários:

A amplitude (ou amplitude total) é a diferença entre o valor máximo e o mínimo. Esses valores foram apresentados na tabela do enunciado. Então, aplicando esses dados na fórmula, temos:
A = 4 — 0 = 4

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Amplitude Interquartílica

Item. 1. (CESPE/SEE-DF/2017) Um levantamento estatístico, feito em determinada região do país,
mostrou que jovens com idades entre 4 e 17 anos assistem à televisão, em média, durante 6 horas por dia. A tabela a seguir apresenta outras estatísticas produzidas por esse levantamento.
Distribuição dos tempos gastos assistindo televisão(7, em horas)

Io quartil 2

2o quartil 4

3o quartil 8

Io decil 1

9o decil 10

Tendo como referência essas informações, julgue o seguinte item.

O desvio quartílico dos tempos T foi igual a 3.

Comentários:

O desvio quartílico é dado porQs2Ql, em que Q3 e Çi são o 35 e o 1^ quartis,
respectivamente. Aplicando os dados da tabela na fórmula, temos:
Q₃ ~ Qi _ 8 - 2 _
2 2

Gabarito: Certo.

Item. 2. (CESPE/TCE-PA/2016)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

média amostrai desvio padrão amostrai primeiro quartil mediana terceiro quartil mínimo máximo
0,80

0,70

0,25

0,70

1,20

3,10

Um indicador de desempenho X permite avaliar a qualidade dos processos de governança de instituições públicas. A figura mostra, esquematicamente, a sua distribuição, obtida mediante estudo amostrai feito por determinada agência de pesquisa. A tabela apresenta estatísticas descritivas referentes a essa distribuição.
Com base nessas informações, julgue o item a seguir.

O intervalo interquartílico da distribuição do indicador X é superior a 1,4.

Comentários:

O intervalo quartílico é dado pela distância entre o terceiro (Ç₃) e o primeiro quartil (Qi), isto é:
Q₃-Qi = 1,20 - 0,25 = 0,95

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Desvios em Relação à Média Aritmética e Mediana

Item. 1. (CESPE/ANATEL/2004)

meses

N

fev mar abr mai jun jul ago set out nov
A tabela acima mostra os números mensais de reclamações (N) feitas por usuários de telefonia fixa,registradas em uma central de atendimento, entre os meses de fevereiro a novembro de 2003.Considerando esses dados, julgue o item que se segue.

O maior desvio absoluto dos números mensais de reclamações registradas é superior a 45.

Comentários:

Iniciaremos calculando a média das reclamações:

100 + 70 + 70 + 60 + 50 + 100 + 50 + 50 + 30 + 20

X = iõ x _7õ"
x = 60

A partir daí, montamos uma tabela para calcular os desvios:

Reclamações
Ut)

Desvio em relação à média (x, - x)
100 100 - 60 = 40

70 70 - 60 = 10

60 60 - 60 = 0

50 50 - 60 = -10

30 30 - 60 = -30

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

20 20 - 60 = -40

Portanto, temos que o maior desvio absoluto é 40.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Desvio Absoluto Médio

Item. 1. (CESPE/ANATEL/2004)

meses

N

fev mar abr mai jun jul ago set out nov
A tabela acima mostra os números mensais de reclamações (N) feitas por usuários de telefonia fixa,registradas em uma central de atendimento, entre os meses de fevereiro a novembro de 2003.Considerando esses dados, julgue o item que se segue.

O desvio médio absoluto da sequência formada pelos números mensais de reclamações é um valor entre 25e 35

Comentários:

Iniciaremos calculando a média das reclamações:

100 + 70 + 70 + 60 + 50 + 100 + 50 + 50 + 30 + 20

X = iõ

*= W"

x = 60

A partir daí, montamos uma tabela para calcular os desvios:

Reclamações

Uí)

Frequências
(Â)

Desvio em relação à média (x, - x)
100 2 100 - 60 = 40

70 2 70 - 60 = 10

60 1 60 - 60 = 0

50 3 50 - 60 = -10

30 1 30 - 60 = -30

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

1 20 - 60 = -40

O desvio médio é dado pela média dos desvios absolutos, considerando a frequência:

2 x 40 + 2 x 10 + 1 x 0 + 3 x 10 + 1 x 30 llx 40

2+2+1+3+1+1

ÜT = 20

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Variância

Item. 1. (CESPE/PC RO/2022) Supondo-se que Tc seja uma variável que representa as temperaturas em grausCelsius observadas em amostras de certo objeto e sabendo-se que a variância amostrai da variável Tc é igual a 10, e que a temperatura na escala Fahrenheit é dada pela expressão
T F = 32 + — xTc,

é correto concluir que a variância amostrai da variável TF é igual a a) 18,0.
b) 32,4.

c) 50,0.

d) 324,0.

e) 1.056,4.

Comentários:

Nessa questão, precisamos relembrar as propriedades da variância: i) a variância de uma variável X somada a uma constante c é igual à variância da própria variável X; ii) ao multiplicar uma variável X por uma constante c, a nova variância será igual à variância de X multiplicada pelo quadrado da constante.
Sabendo disso, temos que:

Var(Tp) = Var ^32 + | x Tc^

/9\2

Var(TF') = y—J xVarÇTc}

Var(TF) =

Var(TF) =

/9\2

/81\

x 10

x 10

Gabarito: B.

Var(TF~) = 32,4

Item. 2. (CESPE/PETROBRAS/2022) O item a seguir é apresentada uma situação hipotética seguida de uma assertiva a ser julgada a respeito de probabilidade e estatística.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ao adicionar uma medição a mais, x21, a um conjunto com inicialmente 20 medições de uma dada grandeza,
{XlfX2, *** ,2C20}, a média aritmética do novo conjunto não se altera. Nesse caso, a variância a2
do conjunto inicial relaciona-se com a variância do novo conjunto na forma a^ = —a2.
Comentários:

A variância do conjunto é dada por:

Para um conjunto com 20 elementos, temos:

7 - nY

O" =

n

H=°ife - AÍ)2

o —

í=i

— [j.y = 20a2

A questão diz que, se adicionarmos mais um termo ao conjunto, a média não se altera,
logo, esse elemento
Xj é igual à média:

*21 = A

Assim, a variância do novo conjunto com 21 elementos é dada por:

E^ife - Aí)2 S^ife - fí)2 + fei - Aí)2

=

21 21

Agora, vamos substituir o valor de Sf=ife — A)2, que calculamos anteriormente:

- A)2 + fei - A)2 20a2 + (/Í — AÍ)2

a2 =

21 21

Gabarito: Certo.

2 20 2

^=21^

Item. 3. (CESPE/PETROBRAS/2022) No que diz respeito aos conceitos e cálculos utilizados em probabilidade e estatística, julgue o item a seguir.
Se, em determinada semana, as ações da PETROBRAS fecharam o pregão com as cotações,
em unidades monetária, iguais a 10,0; 9,0; 11,0; 12,0 e 8,0, respectivamente de segunda à sexta-feira, então a variância dessas cotações foi igual a 2,0.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A variância é determinada pela média dos quadrados dos desvios em relação à média aritmética. A variância populacional é dada por:
. 2F=iUí - ^)2

<j =

n em que: xt é o valor de ordem i assumido pela variável; /z é a média populacional de x; a2 é a variância populacional; enéo número de dados da população.
Vamos iniciar calculando a média do conjunto:

10 + 9 + 11 + 12 + 8 50

= T=W

Agora, vamos calcular os desvios em relação à média. Para isso, vamos escrever os dados em uma tabela para melhor compreensão:
Xi~H (Xt - [L)²

10 10 - 10 = 0 0

9 9 - 10 = -1 1

11 11 - 10 = 1 1

12 12 - 10 = 2 4

8 8- 10 = -2 4

Total 10

Calculando a variância, temos:

Gabarito: Certo.

Item. 4. (CESPE/PETROBRAS/2022)

X Frequência Relativa

0 0,23

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

1 0,22

2 0,50

3 0,05

Considerando que a tabela acima mostra a distribuição de frequências de uma variável x obtida com base em uma amostra aleatória simples de tamanho igual a n, julgue o item que se segue.
A variância amostrai de x é inferior a 0,7.

Comentários:

A variância amostrai é simbolizada pela letra s, sendo calculada a partir de uma amostra da população.Quando os valores vierem dispostos em uma tabela de frequências, a variância será calculada por meio da seguinte fórmula:
? - %)2 x /Í

em que x = L— n s = n — 1-i—
Então, vamos iniciar calculando a média. Para isso, consideraremos a frequência absoluta da tabela para uma amostra com n igual a 100.
fi XiXfi

0 23 0 x 23 = 0

1 22 1 x 22 = 22

2 50 2 x 50 = 100

3 5 3 x 5 = 15

J7í = 100 fi x xi = 137

Em seguida, adicionaremos uma nova coluna à tabela anterior, em que calcularemos os produtos dos quadrados dos desvios por suas respectivas frequências:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Portanto, a variância amostrai de x é SUPERIOR a 0,7

Gabarito: Errado.

Item. 5. (CESPE/TCE SC/2022) Julgue o item a seguir, considerando conceitos de estatística.

Com os seguintes dados, a variância da população é de 149,25.
36; 64; 18; 40; 35; 30; 41; 32

Comentários:

A variância é determinada pela média dos quadrados dos desvios em relação à média aritmética. A variância populacional é dada por:
7 - nY

O" =

n em que: é o valor de ordem i assumido pela variável; é a média populacional de x; cr2 é a variância populacional; e n é o número de dados da população.
Vamos iniciar calculando a média do conjunto:

36 + 64 + 18 + 40 + 35 + 30 + 41 + 32

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, vamos calcular os desvios em relação à média. Para isso, vamos escrever os dados em uma tabela para melhor compreensão:
Xi Xi-H (x, - M)2

36 36 - 37 = -1 1

64 64- 37 = Z1 729

18 18 - 37 = -19 361

40 40 - 37 = 3 9

35 35 - 37 = -2 4

30 30 - 37 = -7 49

41 41 - 37 = 4 16

32 32 - 37 = -5 25

Total 1194

Calculando a variância, temos:

Portanto, a questão está correta.

1194

149,25

Gabarito: Certo.

Item. 6. (CESPE/TJ RJ/2021) Considere que, em um estudo para avaliar a satisfação dos serviços de comunicação de dados oferecidos por uma operadora, no qual foram utilizadas duas variáveis, X e Y, observou-se que X
= 6Y + 24 e que o valor da variância de Y foi igual a 1. Nesse caso, o valor da variância de X é a) 30.
b) 60.

c) 6.

d) 24.

e) 36.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Temos no enunciado que X = 6Y + 24. Temos também que a variância de Y é igual a
1 cr2(Y) = 1.
Queremos saber quanto vale cr2(X). Assim, temos:

cr2(X) = a2(6Y + 24)

Uma das propriedades da variância diz que somando-se (ou subtraindo-se) uma constante c a todos os valores de uma variável, a variância do conjunto não é alterada. Assim, podemos desconsiderar a constante
Item. 24. Então, temos:

cr2(X) = a2(6Y + 24)
CT2(X) = cr2(6K)
a2(X) = 62<J2(Y)
a2(X) = 36a2 (Y)
a2(X) = 36 x 1 = 36

Gabarito: E.

Item. 7. (CESPE/MJ SP/2021) Acerca de planejamento de pesquisa estatística, julgue o item que se seguem.
A média do erro entre a média calculada e as observações reais em um conjunto de dados é conhecida como variância.
Comentários:

A variância é determinada pela média dos quadrados dos desvios/erros em relação à média aritmética. Por meio dessa medida de dispersão ou variabilidade, podemos avaliar o quanto os dados estão dispersos em relação à média aritmética. A variância populacional é simbolizada pela letra grega a(sigma), sendo calculada usando todos os elementos da população, pela seguinte fórmula:
7 2F=iUí - nY

n em que: xt é o valor de ordem i assumido pela variável; /i é a média populacional de x; cr2 é a variância populacional; e n é o número de dados da população.
Gabarito: Certo.

Item. 8. (CESPE/BANESE/2021) A respeito do conjunto de dados {11, 6, 28, 51,49, 32, 33}, julgue o item a seguir.
Esse conjunto de dados possui variância amostrai inferior a 300.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

A variância amostrai é simbolizada pela letra s, sendo calculada a partir de uma amostra da população, pela seguinte fórmula:
7 - %)2

s = n —- ;—1

em que: xt é o valor de ordem i assumido pela variável; x é a média amostrai de x; s2 é a variância amostrai;e n é o número de dados da amostra.

Então, vamos iniciar pelo cálculo da média:

11 + 6 + 28 + 51 + 49 + 32 + 33 210

= — = 30

X ~ 7

Agora, calculando a variância, temos:

, (11 - 30)2 + (6 - 30)2 + (28 - 30)2 + (51 - 30)2 + (49 - 30)2 + (32 - 30)2 + (33 -
30)2

s =

7-1

„ 361 + 576 + 4 + 441 + 361 + 4 + 9

, 1756

s =~T

s2 = 292,66

Gabarito: Certo.

Item. 9. (CESPE/BANESE/2021)

Média 5 10

Desvio padrão 2 2

Com base nas informações apresentadas na tabela precedente e considerando que a covariância entre as variáveis X e Y seja igual a 3, julgue o item que se segue.
A variância de X é igual a 4.

Comentários:

A variância corresponde ao desvio padrão elevado ao quadrado:
(o)-> desvio padrão

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

variância

Assim, basta elevarmos o desvio padrão de X ao quadrado para encontrarmos a variância:

o2 = 22 = 4

Gabarito: Certo.

Item. 10. (CESPE/SEDUC AL/2021) Com base em estatística, julgue o item a seguir.

Para um conjunto de dados x₁,x₂, —,xn quaisquer, a variância será sempre um número positivo.

Comentários:

A variância é sempre maior ou igual a zero, isto é, nunca terá valor negativo, mas também pode assumir valor nulo. A variância de um conjunto é zero quando todos os elementos são iguais.Se todos os elementos são iguais, a média aritmética do conjunto coincide com o valor dos elementos e todos os desvios também são iguais a zero. Logo, a variância também é zero.
Gabarito: Errado.

Item. 11. (CESPE/TCE-RJ/2021)

X Frequência Absoluta

0 5

1 10

2 20

3 15

Total 50

Considerando que a tabela precedente mostra a distribuição de frequências de uma variável quantitativaX, julgue o item a seguir.

A variância amostrai de X é superior a 0,89.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A variância amostrai é simbolizada pela letra s, sendo calculada a partir de uma amostra da população, pela seguinte fórmula:
7 - %)2

s = n —- ;—1

em que: xt é o valor de ordem i assumido pela variável; x é a média amostrai de x; s2 é a variância amostrai;e n é o número de dados da amostra.

Então, vamos iniciar calculando a média, para isso precisamos ponderar cada valor de x representado na tabela:
(0x5) + (lx 10) + (2 x 20) + (3 x 15) 95

X ~ 5 + 10 + 20 + 15 5Õ _ 1,9

Calculando a variância:

Gabarito: Certo.

, 5(0 - 1,9)2 + 10(1 - 1,9)2 + 20(2 - 1,9)2 + 15(3 - 1,9)2

=

50-1

9 18,5 + 8,1 + 0,2 + 18,15

s —

s 9= 44,95

s2 = 0,91

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Desvio-Padrão

Item. 1. (CESPE/FUB/2022) Uma universidade está fazendo um estudo para verificar a distribuição dos tempos que os alunos do curso de mestrado levam até a defesa da dissertação. Os dados a seguir mostram a função de probabilidade desses tempos, em meses.
Considerando essas informações, julgue o item subsequente.

Assumindo-se que E(X2) = 552, obtém-se um valor superior a 5 para o desvio padrão dos dados referentes ao tempo de defesa.
Comentários:

Para calcularmos a média aritmética, multiplicaremos cada valor de X (tempo de defesa)
por sua respectiva probabilidade. Em seguida, o resultado da soma desses produtos deve ser dividido pela soma das probabilidades. Vamos reescrever a tabela com os cálculos:
(X) (/) XX f

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

12 0,01 0,12

15 0,02 0,3

18 0,04 0,72

20 0,10 2

22 0,22 4,84

24 0,31 7,44

25 0,18 4,5

26 0,04 1,04

28 0,03 0,84

30 0,05 1,5

Total 1 23,3

Portanto, a média será dada por:

Agora, devemos lembrar que a variância pode ser calculada por meio da fórmula Var(X) = E(X2) —
[F(X)]2. Aplicando a expressão, temos:

Var(X) = E(X2) - [£(X)]2

Var(X) = 552 - (23,3)2

Var(X) = 552 - 542,89

Var(X) = 9,11

O desvio padrão é calculado pela raiz quadrada da variância. Portanto, temos:

s = vw s = 3,01
Gabarito: Errado.

Item. 2. (CESPE/MP TCE-SC/2022)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

X

Considerando a figura anterior, na qual é representada a distribuição de uma variável quantitativa discretaX, julgue o item a seguir.

O desvio padrão da variável X é superior a 2.

Comentários:

Primeiro, vamos traduzir os dados do gráfico para uma tabela e depois prosseguiremos com os cálculos necessários:
X Freq. relativa (fj)
^(xf-x)2 X/i

0 0,1 0 (0 -
1,6)2 x 0,1 = 0,256

1 0,5 0,5 (1 -
1,6)2 x 0,5 = 0,18

2 0,2 0,4 (2 -
1,6)2 x 0,2 = 0,032

3 0,1 0,3 (3 -
1,6)² x 0,1 = 0,196

4 0,1 0,4 (4 -
1,6)2 x 0,1 = 0,576

Total ^\x/- = l,6
^(%i -x)² xfi = 1,24
Calculando a média, temos:

Por fim, aplicando a fórmula do desvio padrão, temos:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

- %)2 X fj n
1^24 ,------

a= — = 7124 = 1,11

Gabarito: Errado.

Item. 3. (CESPE/PETROBRAS/2022)

Tabela A
Classes I Freq.
10-12 3

12-14 7

14-16 9

16-18 12

18-20 8

20-22 6

22-24 4

24-26 2

Tabela B
Classes 1 Freq

2-4 1

4-6 4

6-8 5

8-10 7

10-12 10

12-14 13

14-16 17

16-18 21

18-20 18

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

20-22 15

22-24 11

24-26 9

26-28 6

28-30 3

30-32 2

Com base nas tabelas de frequência A e B apresentadas anteriormente, julgue o item a seguir.

O desvio-padrão da série B é menor do que o desvio-padrão da série A.

Comentários:

Nessa questão, devemos ter em mente que o desvio-padrão sempre será igual ou inferior à metade da amplitude máxima da distribuição. Assim, analisando as duas tabelas, percebemos que os dados da tabela Aestão espalhados em uma amplitude de 26 — 10 = 16, enquanto os dados da tabela B
estão espalhados em uma amplitude de 32 — 2 = 30. Como os dados também se distribuem de forma quase simétrica em relação à metade da amplitude máxima, podemos afirmar que o desvio-padrão da série B é maior que o desvio-padrão da série A.

Gabarito: Errado.

Item. 4. (CESPE/PC PB/2022 - ADAPTADA)
Situação hipotética 17A4-I

Um padrão de referência possui concentração de 25 mg/mL da substância X. Um técnico, ao calibrar dois aparelhos que medem a concentração desta substância X, fez medidas durante 5 dias (amostra 1 no dia1,
amostra 2 no dia 2, e assim por diante) e encontrou os seguintes valores.

Aparelho A

Amostra

Concentração
(mg/ml)

1 21

2 22

3 21

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

4 20

5 21

Aparelho B

Amostra

Concentração
(mg/ml)

1 29

2 25

3 21

4 24

5 26

Considerando os dados obtidos na situação hipotética 17A4-I, os valores para a média e desvio-padrão dos aparelhos A e B são a) médiaA= 21 mg/mL; desvio-padrãoA= 0,71 mg/mL; médiaB= 25 mg/mL; desvio-padrãoB= 2,91 mg/mL;
b) médiaA= 21 mg/mL; desvio-padrãoA= 2 mg/mL; médiaB= 25 mg/mL; desvio-padrãoB= 10 mg/mL;

c) médiaA= 21 mg/mL; desvio-padrãoA= 0,63 mg/mL; médiaB= 24 mg/mL; desvio-padrãoB= 3,58 mg/mL;

d) médiaA= 21 mg/mL; desvio-padrãoA= 2 mg/mL; médiaB= 24 mg/mL; desvio-padrãoB= 4 mg/mL;

e) médiaA= 21 mg/mL; desvio-padrãoA= 0,71 mg/mL; médiaB= 24 mg/mL; desvio-padrãoB= 4 mg/mL;

Comentários:

Para a amostra A, temos:

a.l) média:

b.l) desvio padrão:

21 + 22 + 21 + 20 + 21 105

X* = 5 = 5 =21

7 S?=1(xí - x)2

G a ;

n — 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para a amostra B, temos:

a.2) média:

b.2) desvio padrão:

29 + 25 + 21 + 24 + 26 125

** = s = T = 25

2 2?=!^ - %)2

ff B =

n — 1

, (29 - 25)2 + (25 - 25)2 + (21 - 25)2 + (24 - 25)2 + (26 - 25)2

° B ~ 5^1

7 (4)2 + (O)2 + (—4)2 + (-1)2 + (l)2

° B~ 5-1

Na questão original, a banca informava que o desvio padrão de B era igual a 4, quando deveria ser de 2,91.
Gabarito: A.

Item. 5. (CESPE/PC RO/2022)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considere que a figura acima mostre a distribuição de frequências absolutas de uma variável. Nesse caso,a variância amostrai dessa variável é igual a a) 1,54.
b) 2,00.

c) 2,88.

d) 3,00.

e) 3,75.

Comentários:

Para calcular a média aritmética da distribuição, basta multiplicarmos cada valor por sua respectiva frequência e, em seguida, dividir o resultado pela soma das frequências:
Y Freq. (/J Y x f,

1 8 1x8 = 8

2 4 2x4 = 8

3 2 3x2 = 6

4 4 4x4= 16

5 8 5 x 8 = 40

TOTAL 26 78

Assim, a nossa média aritmética será:

Agora, vamos elevar o desvio ao quadrado e multiplicar pela respectiva frequência:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Y Freq. (/t) Y-Y (y - y)2 (y - y)2 x i 8 1 - 3 = -2 (-2)2 = 4 4x8 = 32
2 4 2 - 3 =-1 (-1)2 = 1 1x4 = 4

3 2 3-3 = 0 02 = 0 0x2 = 0

4 4 4-3 = 1 l2 = 1 1x4 = 4

5 8 5-3 = 2 22 = 4 4x8 = 32

TOTAL 26 72

De posse desses totais, podemos facilmente calcular o valor do desvio padrão amostrai por meio da expressão:
~ F)2 X fi 72

n-1 26-1

Gabarito: C.

Item. 6. (CESPE/COREN SE/2021) Considere que os tempos de espera X e de atendimento Y, ambos em minutos,
para determinado serviço ambulatorial se relacionem como Y = 2X - 1. Se o desvio padrão de X for igual a
2 minutos, então o desvio padrão de Y, em minutos, será igual a a) 2.
b) 5.

c) 3.

d) 4.

Comentários:

O enunciado nos informa que Y = 2X — 1. Também nos diz que o desvio padrão de X
é igual a 2 <j(X) = 2.
Queremos saber quanto vale cr(Y). Assim, temos:

o(Y) = cr(2X — 1)

Uma das propriedades da variância diz que somando-se (ou subtraindo-se) uma constante c a todos os valores de uma variável, a variância do conjunto não é alterada. Assim, podemos desconsiderar a constante(-1). Então, temos:

o(y) = cr(2X — 1)

o(r) = cr(2X)

a(Y) = 2(2)

a(y) = 2x2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

cr(Y) = 4

Gabarito: D.

Item. 7. (CESPE/PC SE/2021) Com base em uma amostra aleatória simples de tamanho n = 16
retirada de uma população normal com média desconhecida p e variância o-2 = 9, deseja-se testar a hipótese nula Ho: n =
0 contra a hipótese alternativa Hl-.p. #= 0 por meio da estatística y/nX/a, na qual
X denota a média amostrai.
Com respeito a esse teste de hipóteses, julgue o item a seguir, sabendo que o valor da média amostrai observado na amostra foi igual ale que, relativo a esse teste, o P-valor foi igual a 0,18.
O desvio padrão da média amostrai X é igual a 0,75.

Comentários:

O desvio padrão da média amostrai é expresso por:

cr

&X — !—

Vn

O enunciado nos informa que n = 16 e que a variância é igual a 9. Sabemos que o desvio padrão é a raiz quadrada da variância, então, substituindo na fórmula, temos:
a A/9

— /— — /-----

Vn Vl6

= 4 = °'75

Gabarito: Certo.

Item. 8. (CESPE/CBM AL/2021) Determinado dado tetraédrico (dado em formato de tetraedro regular), com vértices numerados de 1 a 4, foi lançado 21 vezes, de modo que o resultado do lançamento desse dado correspondia ao vértice voltado para cima. A tabela seguinte mostra a frequência com que se obteve cada resultado.
Resultado Quantidade de lançamentos

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

4 9

Com base nessa situação hipotética, julgue o item a seguir.

O desvio padrão dos resultados é superior a 1.

Comentários:

Vamos iniciar calculando a média do conjunto. Para isso, precisamos multiplicar cada resultado pela quantidade de lançamentos:
(1 x 2) + (2 x 5) + (3 x 5) + (4 x 9) 63

O desvio padrão é dado por:

= 2+5+5+9

21 " 3

em que n é a quantidade de lançamentos.

8+5+0+9

cr > 1

Portando, o desvio padrão é maior que 1.

Gabarito: Certo.

Item. 9. (CESPE/Pref. São Cristóvão/2019) A tabela seguinte mostra a distribuição das idades dos 30
alunos da turma A do quinto ano de uma escola de ensino fundamental.
Idade (em anos) 9 10 11 12 13

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Quantidade de estudantes
A partir dessa tabela, julgue o item.

O desvio padrão das idades é inferior a 1 ano.

Comentários:

Calculando a média:

9x6 + 10x22 + 11x0 + 12x1 + 13x0 + 14x1

* = 3Õ

X_ = lõ-

x = 10

Agora, calcularemos os desvios de cada idade em relação à média:

Idades

Ui)

Quantidade de
Estudantes

(A)

Desvio em relação à média(%i - x)

(Xi - x)2

9 6 9 - 10 = -1 1

10 22 10 - 10 = 0 0

11 0 11 - 10 = 1 1

12 1 12 - 10 = 2 4

13 0 13 - 10 = 3 9

14 1 14- 10 = 4 16

O desvio padrão é calculado por meio da seguinte fórmula:

Aplicando a fórmula, temos:

o = ZF=i(Xf - x)2 x

_ J n

1x6 +10 x 22+ 1x04-4x1 + 9x0 +16x1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Portanto, o desvio padrão é menor que 1:

Gabarito: Certo.

Item. 10. (CESPE/IFF/2018)

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

cm

Foram feitas dez medidas do comprimento da caneta mostrada na figura. Os valores dessas medidas estão expressos na tabela a seguir.
medida Si S2 s3 Si s5 S6 s7 s» Sg $10

comprimento (mm) 136 135 135 137 134 135 136 135 136 135

Com base nessas informações, é correto afirmar que o valor do desvio padrão, em mm, desse experimento é igual a a) 0,00.
b) 0,64.

c) 0,71.

d) 0,80.

e) 0,84.

Comentários:

Calculando a média:

134 + 5 x 135 + 3 x 136 + 137

1354

x = 135,4

O desvio padrão amostrai é dado pela fórmula apresentada a seguir. Repare que usamos (n — 1) no numerador pois se trata de uma amostra e não de toda a população:
Zp=i(xf - x)2 X fj n — 1
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Aplicando a fórmula, temos:

IXi^íXí - x)2 X fi

—*—

1(134 - 135,4)2 + 5 x (135 - 135,4)2 + 3 x (136 - 135,4)2 + (137 - 135,4)2

S=J '

^6,4

s = 0,84

Gabarito: E.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Coeficiente de Variação (ou Dispersão Relativa)

Item. 1. (CESPE/FUB/2022) A tabela de frequência a seguir mostra dados coletados em uma pesquisa para se verificar o número de disciplinas que os estudantes de determinada universidade estão cursando por semestre.
Disciplinas
Estudantes

Considerando essas informações, julgue o item seguinte.

Sabendo-se que a variância amostrai dos dados é igual a 2, conclui-se que o coeficiente de variação é maior que 50%.
Comentários:

O coeficiente de variação é expresso por:

CV = -x 100 (%)

Calculando a média, temos:

_ (2 x 10) + (3 x 15) + (4 x 40) + (5 x 35) + (6 x 28) + (7 x 10) + (8 x 4)

10 + 15 + 40 + 35 + 28 + 10 + 4

= 142 = 4,71

Sabemos também que o desvio padrão é igual a raiz quadrada da variância, logo, temos que:

V2

cv= — xl00(%)

CV = 30%

Gabarito: Errado.

Item. 2. (CESPE/TELEBRAS/2022) Com respeito ao conjunto de dados {0,0,1,1,1, 3}, julgue o item que se segue.
O coeficiente de variação é igual ou superior a 1,2.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O coeficiente de variação é uma medida que fornece a variação dos dados em relação à média, sendo calculado por meio da expressão:
Portanto, vamos calcular a média do conjunto:

0+0+1+1+1+3 6

" = 6 = 6 = 1

Sabemos que o desvio padrão da população é dado pela seguinte fórmula:

Oi - u)

Substituindo, podemos calcular o coeficiente de variação:

Gabarito: Errado.

Item. 3. (CESPE/TELEBRAS/2022 - ADAPTADA) Com respeito ao conjunto de dados {5a, 2a, 2a},
em que a representa uma constante não nula, julgue o próximo item.
O coeficiente de variação independe do valor da constante a.

Comentários:

Para a média, temos:

Para o desvio padrão, temos:

5a + 2a + 2a 9a

" =------5---- = T = 3a

= . EF=10i - ^)2

n

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(3a — 3a)2 + (2a — 3a)2 + (2a — 3a)2

(2a)2 + (-a)2 + (-a)2

° = 3

4a2 + a2 + a2 6a2

o = V2|a|

Substituindo, podemos calcular o coeficiente de variação:

CV =

Agora, devemos ficar atentos ao fato de que se a

-x 100 (%)

< 1, teremos:

Por outro lado, se a > 1, teremos:

CV =

V2|g| V2

—3a 3

V2|a| V2

CV = —— = —

3a 3

A questão original deu o gabarito como correto.

Gabarito: Errado.

Item. 4. (CESPE/SERPRO/2021) Considerando que o número X de erros registrados em determinado tipo de código computacional siga uma distribuição binomial com média igual a 4 e variância igual a 3, julgue o item a seguir.
O coeficiente de variação da distribuição de erros X é igual a 3.

Comentários:

O coeficiente de variação é dado pela razão entre o desvio padrão e a média. Sabemos que o desvio padrão é a raiz quadrada da variância, portanto, temos:
cr

V3

= — - 0,433

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 5. (CESPE/IPHAN/2018) Cinco municípios de um estado brasileiro possuem as seguintes quantidades de patrimônios históricos: {2, 3, 5, 3, 2}. Admitindo que a média e o desvio-padrão desse conjunto de valores sejam iguais a 3 e 1,2, respectivamente, julgue o item seguinte.
O coeficiente de variação é superior a 0,3 e inferior a 0,5.

Comentários:

O coeficiente de variação é dado pela razão entre o desvio padrão e a média.
Portanto, temos:

cr

Cv = T = 0,4

Gabarito: Certo.

Item. 6. (CESPE/TCE-PA/2016)

média amostrai desvio padrão amostrai primeiro quartil mediana terceiro quartil mínimo máximo
0,80

0,70

0,25

0,70

1,20

3,10

Um indicador de desempenho X permite avaliar a qualidade dos processos de governança de instituições públicas. A figura mostra, esquematicamente, a sua distribuição, obtida mediante estudo amostrai feito por determinada agência de pesquisa. A tabela apresenta estatísticas descritivas referentes a essa distribuição.
Com base nessas informações, julgue o item a seguir.

O coeficiente de variação da distribuição de X é inferior a 0,8.

Comentários:

O coeficiente de variação é dado pela razão entre o desvio padrão e a média. Portanto, temos:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Amplitude Total

Item. 1. (CESPE/SEDF/2017) Um levantamento estatístico, feito em determinada região do país,
mostrou que jovens com idades entre 4 e 17 anos assistem à televisão, em média, durante 6 horas por dia. A tabela a seguir apresenta outras estatísticas produzidas por esse levantamento.
Distribuição dos tempos gastos assistindo televisão(7, em horas)

Io quartil 2

2o quartil 4

3o quartil 8

Io decil 1

9o decil 10

Tendo como referência essas informações, julgue o seguinte item.

A amplitude total dos tempos T é igual ou superior a 9 horas.

Item. 2. (CESPE/TCE-PA/2016)

média amostrai desvio padrão amostrai primeiro quartil mediana terceiro quartil mínimo máximo
0,80

0,70

0,25

0,70

1,20

3,10

Um indicador de desempenho X permite avaliar a qualidade dos processos de governança de instituições públicas. A figura mostra, esquematicamente, a sua distribuição, obtida mediante estudo amostrai feito por determinada agência de pesquisa. A tabela apresenta estatísticas descritivas referentes a essa distribuição.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com base nessas informações, julgue o item a seguir.

A amplitude total da amostra é inferior a 3.

Item. 3. (CESPE/TCE-PA/2016)

Número diário de denúncias registradas (X)
Frequência
Relativa

Total

0,3

0,1

0,2

0,1

0,3

1,0

A tabela precedente apresenta a distribuição de frequências relativas da variável X,
que representa o número diário de denúncias registradas na ouvidoria de determinada instituição pública.A partir das informações dessa tabela, julgue o item seguinte.
A amplitude total da amostra é igual ou superior a 5.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo - CEBRASPE

Amplitude Total

Item. 1. CERTO 2. ERRADO
Item. 3. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Amplitude Interquartílica

Item. 1. (CESPE/SEE-DF/2017) Um levantamento estatístico, feito em determinada região do país,
mostrou que jovens com idades entre 4 e 17 anos assistem à televisão, em média, durante 6 horas por dia. A tabela a seguir apresenta outras estatísticas produzidas por esse levantamento.
Distribuição dos tempos gastos assistindo televisão(7, em horas)

Io quartil 2

2o quartil 4

3o quartil 8

Io decil 1

9o decil 10

Tendo como referência essas informações, julgue o seguinte item.

O desvio quartílico dos tempos T foi igual a 3.

Item. 2. (CESPE/TCE-PA/2016)

média amostrai desvio padrão amostrai primeiro quartil mediana terceiro quartil mínimo máximo
0,80

0,70

0,25

0,70

1,20

3,10

Um indicador de desempenho X permite avaliar a qualidade dos processos de governança de instituições públicas. A figura mostra, esquematicamente, a sua distribuição, obtida mediante estudo amostrai feito por determinada agência de pesquisa. A tabela apresenta estatísticas descritivas referentes a essa distribuição.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com base nessas informações, julgue o item a seguir.

O intervalo interquartílico da distribuição do indicador X é superior a 1,4.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo - CEBRASPE

Amplitude Interquartílica

Item. 1. CERTO 2. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Desvios em Relação à Média Aritmética e Mediana

Item. 1. (CESPE/ANATEL/2004)

meses

N

fev mar abr mai jun jul ago set out nov
A tabela acima mostra os números mensais de reclamações (N) feitas por usuários de telefonia fixa,registradas em uma central de atendimento, entre os meses de fevereiro a novembro de 2003.Considerando esses dados, julgue o item que se segue.

O maior desvio absoluto dos números mensais de reclamações registradas é superior a 45.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo - CEBRASPE

Desvios em Relação à Média Aritmética e Mediana

Item. 1. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Desvio Absoluto Médio

Item. 1. (CESPE/ANATEL/2004)

meses

N

fev mar abr mai jun jul ago set out nov
A tabela acima mostra os números mensais de reclamações (N) feitas por usuários de telefonia fixa,registradas em uma central de atendimento, entre os meses de fevereiro a novembro de 2003.Considerando esses dados, julgue o item que se segue.

O desvio médio absoluto da sequência formada pelos números mensais de reclamações é um valor entre 25e 35

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo - CEBRASPE

Desvio Absoluto Médio

Item. 1. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Variância

Item. 1. (CESPE/PC RO/2022) Supondo-se que Tc seja uma variável que representa as temperaturas em grausCelsius observadas em amostras de certo objeto e sabendo-se que a variância amostrai da variável Tc é igual a 10, e que a temperatura na escala Fahrenheit é dada pela expressão
T F = 32 + — xTc,

é correto concluir que a variância amostrai da variável TF é igual a a) 18,0.
b) 32,4.

c) 50,0.

d) 324,0.

e) 1.056,4.

Item. 2. (CESPE/PETROBRAS/2022) O item a seguir é apresentada uma situação hipotética seguida de uma assertiva a ser julgada a respeito de probabilidade e estatística.
Ao adicionar uma medição a mais, %₂i> a um conjunto com inicialmente 20 medições de uma dada grandeza,
{X1,X2, *** ,X20}, a média aritmética /z do novo conjunto não se altera. Nesse caso,
a variância cr2 do conjunto inicial relaciona-se com a variância do novo conjunto na forma = —a2.
Item. 3. (CESPE/PETROBRAS/2022) No que diz respeito aos conceitos e cálculos utilizados em probabilidade e estatística, julgue o item a seguir.
Se, em determinada semana, as ações da PETROBRAS fecharam o pregão com as cotações,
em unidades monetária, iguais a 10,0; 9,0; 11,0; 12,0 e 8,0, respectivamente de segunda à sexta-feira, então a variância dessas cotações foi igual a 2,0.
Item. 4. (CESPE/PETROBRAS/2022)

X Frequência Relativa

0 0,23

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

1 0,22

2 0,50

3 0,05

Considerando que a tabela acima mostra a distribuição de frequências de uma variável x obtida com base em uma amostra aleatória simples de tamanho igual a n, julgue o item que se segue.
A variância amostrai de x é inferior a 0,7.

Item. 5. (CESPE/TCE SC/2022) Julgue o item a seguir, considerando conceitos de estatística.

Com os seguintes dados, a variância da população é de 149,25.
36; 64; 18; 40; 35; 30; 41; 32

Item. 6. (CESPE/TJ RJ/2021) Considere que, em um estudo para avaliar a satisfação dos serviços de comunicação de dados oferecidos por uma operadora, no qual foram utilizadas duas variáveis, X e Y, observou-se que X
= 6Y + 24 e que o valor da variância de Y foi igual a 1. Nesse caso, o valor da variância de X é a) 30.
b) 60.

c) 6.

d) 24.

e) 36.

Item. 7. (CESPE/MJ SP/2021) Acerca de planejamento de pesquisa estatística, julgue o item que se seguem.
A média do erro entre a média calculada e as observações reais em um conjunto de dados é conhecida como variância.
Item. 8. (CESPE/BANESE/2021) A respeito do conjunto de dados {11, 6, 28, 51,49, 32, 33}, julgue o item a seguir.
Esse conjunto de dados possui variância amostrai inferior a 300.

Item. 9. (CESPE/BANESE/2021)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Média 5 10

Desvio padrão 2 2

Com base nas informações apresentadas na tabela precedente e considerando que a covariância entre as variáveis X e Y seja igual a 3, julgue o item que se segue.
A variância de X é igual a 4.

Item. 10. (CESPE/SEDUC AL/2021) Com base em estatística, julgue o item a seguir.

Para um conjunto de dados %i,x₂, — >*n quaisquer, a variância será sempre um número positivo.

Item. 11. (CESPE/TCE-RJ/2021)

X Frequência Absoluta

0 5

1 10

2 20

3 15

Total 50

Considerando que a tabela precedente mostra a distribuição de frequências de uma variável quantitativaX, julgue o item a seguir.

A variância amostrai de X é superior a 0,89.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo - CEBRASPE

Variância

Item. 1. LETRA B 5. CERTO
Item. 9. CERTO

Item. 2. CERTO 6. LETRA E
Item. 10. ERRADO

Item. 3. CERTO

Item. 4. ERRADO

Item. 7. CERTO

Item. 8. CERTO

Item. 11. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Desvio-Padrão

Item. 1. (CESPE/FUB/2022) Uma universidade está fazendo um estudo para verificar a distribuição dos tempos que os alunos do curso de mestrado levam até a defesa da dissertação. Os dados a seguir mostram a função de probabilidade desses tempos, em meses.
Tempo de Defesa (meses) Probabilidade

Considerando essas informações, julgue o item subsequente.

Assumindo-se que E(X2) = 552, obtém-se um valor superior a 5 para o desvio padrão dos dados referentes ao tempo de defesa.
Item. 2. (CESPE/MP TCE-SC/2022)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

X

Considerando a figura anterior, na qual é representada a distribuição de uma variável quantitativa discretaX, julgue o item a seguir.

O desvio padrão da variável X é superior a 2.

Item. 3. (CESPE/PETROBRAS/2022)

Tabela A
Classes I Freq.
10-12 3

12-14 7

14-16 9

16-18 12

18-20 8

20-22 6

22-24 4

24-26 2

Tabela B
Classes I Freq.
2-4 1

4-6 4

6-8 5

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

8-10 7

10-12 10

12-14 13

14-16 17

16-18 21

18-20 18

20-22 15

22-24 11

24-26 9

26-28 6

28-30 3

30-32 2

Com base nas tabelas de frequência A e B apresentadas anteriormente, julgue o item a seguir.

O desvio-padrão da série B é menor do que o desvio-padrão da série A.

Item. 4. (CESPE/PC PB/2022 - ADAPTADA)
Situação hipotética 17A4-I

Um padrão de referência possui concentração de 25 mg/mL da substância X. Um técnico, ao calibrar dois aparelhos que medem a concentração desta substância X, fez medidas durante 5 dias (amostra 1 no dia1,
amostra 2 no dia 2, e assim por diante) e encontrou os seguintes valores.

Aparelho A

Amostra

Concentração
(mg/ml)

1 21

2 22

3 21

4 20

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

5 21

Aparelho B

Amostra

Concentração
(mg/ml)

1 29

2 25

3 21

4 24

5 26

Considerando os dados obtidos na situação hipotética 17A4-I, os valores para a média e desvio-padrão dos aparelhos A e B são a) médiaA= 21 mg/mL; desvio-padrãoA= 0,71 mg/mL; médiaB= 25 mg/mL; desvio-padrãoB= 2,91 mg/mL;
b) médiaA= 21 mg/mL; desvio-padrãoA= 2 mg/mL; médiaB= 25 mg/mL; desvio-padrãoB= 10 mg/mL;

c) médiaA= 21 mg/mL; desvio-padrãoA= 0,63 mg/mL; médiaB= 24 mg/mL; desvio-padrãoB= 3,58 mg/mL;

d) médiaA= 21 mg/mL; desvio-padrãoA= 2 mg/mL; médiaB= 24 mg/mL; desvio-padrãoB= 4 mg/mL;

e) médiaA= 21 mg/mL; desvio-padrãoA= 0,71 mg/mL; médiaB= 24 mg/mL; desvio-padrãoB= 4 mg/mL;

Item. 5. (CESPE/PC RO/2022)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considere que a figura acima mostre a distribuição de frequências absolutas de uma variável. Nesse caso,a variância amostrai dessa variável é igual a a) 1,54.
b) 2,00.

c) 2,88.

d) 3,00.

e) 3,75.

Item. 6. (CESPE/COREN SE/2021) Considere que os tempos de espera X e de atendimento Y, ambos em minutos,
para determinado serviço ambulatorial se relacionem como Y = 2X - 1. Se o desvio padrão de X for igual a
2 minutos, então o desvio padrão de Y, em minutos, será igual a a) 2.
b) 5.

c) 3.

d) 4.

Item. 7. (CESPE/PC SE/2021) Com base em uma amostra aleatória simples de tamanho n = 16 retirada de uma população normal com média desconhecida p e variância o-2 = 9, deseja-se testar a hipótese nula Ho: n =
0 contra a hipótese alternativa Hl-.p. #= 0 por meio da estatística \~nX/<j, na qual
X denota a média amostrai.
Com respeito a esse teste de hipóteses, julgue o item a seguir, sabendo que o valor da média amostrai observado na amostra foi igual ale que, relativo a esse teste, o P-valor foi igual a 0,18.
O desvio padrão da média amostrai X é igual a 0,75.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 8. (CESPE/CBM AL/2021) Determinado dado tetraédrico (dado em formato de tetraedro regular), com vértices numerados de 1 a 4, foi lançado 21 vezes, de modo que o resultado do lançamento desse dado correspondia ao vértice voltado para cima. A tabela seguinte mostra a frequência com que se obteve cada resultado.
Resultado Quantidade de lançamentos

1 2

2 5

3 5

4 9

Com base nessa situação hipotética, julgue o item a seguir.

O desvio padrão dos resultados é superior a 1.

Item. 9. (CESPE/Pref. São Cristóvão/2019) A tabela seguinte mostra a distribuição das idades dos 30
alunos da turma A do quinto ano de uma escola de ensino fundamental.
Idade (em anos) 9 10 11 12 13

Quantidade de estudantes
6 22 0 1 0

A partir dessa tabela, julgue o item.

O desvio padrão das idades é inferior a 1 ano.

Item. 10. (CESPE/IFF/2018)

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

cm

Foram feitas dez medidas do comprimento da caneta mostrada na figura. Os valores dessas medidas estão expressos na tabela a seguir.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

medida comprimento (mm)
S2

S3

s4

s5

Se

S7

s8

s9

Sio

Com base nessas informações, é correto afirmar que o valor do desvio padrão, em mm, desse experimento é igual a a) 0,00.
b) 0,64.

c) 0,71.

d) 0,80.

e) 0,84.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo - CEBRASPE

Desvio-Padrão

Item. 1. ERRADO 5. LETRA C
Item. 9. CERTO

Item. 2. ERRADO 6. LETRA D
10.LETRA E

Item. 3. ERRADO 7. CERTO

Item. 4. LETRA A 8. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Coeficiente de Variação (ou Dispersão Relativa)

Item. 1. (CESPE/FUB/2022) A tabela de frequência a seguir mostra dados coletados em uma pesquisa para se verificar o número de disciplinas que os estudantes de determinada universidade estão cursando por semestre.
Disciplinas
Estudantes

Considerando essas informações, julgue o item seguinte.

Sabendo-se que a variância amostrai dos dados é igual a 2, conclui-se que o coeficiente de variação é maior que 50%.
Item. 2. (CESPE/TELEBRAS/2022) Com respeito ao conjunto de dados {0,0,1,1,1, 3}, julgue o item que se segue.
O coeficiente de variação é igual ou superior a 1,2.

Item. 3. (CESPE/TELEBRAS/2022 - ADAPTADA) Com respeito ao conjunto de dados {5a, 2a, 2a},
em que a representa uma constante não nula, julgue o próximo item.
O coeficiente de variação independe do valor da constante a.

Item. 4. (CESPE/SERPRO/2021) Considerando que o número X de erros registrados em determinado tipo de código computacional siga uma distribuição binomial com média igual a 4 e variância igual a 3, julgue o item a seguir.
O coeficiente de variação da distribuição de erros X é igual a 3.

Item. 5. (CESPE/IPHAN/2018) Cinco municípios de um estado brasileiro possuem as seguintes quantidades de patrimônios históricos: {2, 3, 5, 3, 2}. Admitindo que a média e o desvio-padrão desse conjunto de valores sejam iguais a 3 e 1,2, respectivamente, julgue o item seguinte.
O coeficiente de variação é superior a 0,3 e inferior a 0,5.

Item. 6. (CESPE/TCE-PA/2016)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

média amostrai desvio padrão amostrai primeiro quartil mediana terceiro quartil mínimo máximo
0,80

0,70

0,25

0,70

1,20

3,10

Um indicador de desempenho X permite avaliar a qualidade dos processos de governança de instituições públicas. A figura mostra, esquematicamente, a sua distribuição, obtida mediante estudo amostrai feito por determinada agência de pesquisa. A tabela apresenta estatísticas descritivas referentes a essa distribuição.
Com base nessas informações, julgue o item a seguir.

O coeficiente de variação da distribuição de X é inferior a 0,8.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo - CEBRASPE

Coeficiente de Variação (ou Dispersão Relativa)

Item. 1. ERRADO

Item. 2. ERRADO

Item. 3. ERRADO

Item. 4. ERRADO

Item. 5. CERTO

Item. 6. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

