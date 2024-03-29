# Probabilidade e Estatística - Distribuições Aleatórias de Probabilidade

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Distribuição Normal

2) Questões Comentadas - Distribuição Normal - Cebraspe

3) Lista de Questões - Distribuição Normal - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçÃo NoRMAL

A distribuição normal, também chamada de gaussiana, é uma das distribuições contínuas mais importantes!A função densidade de probabilidade (f.d.p.) dessa distribuição é dada por:

f{x) = —e 2{ cr ) t X E (—00,00)

Essa f.d.p. é bastante complicada, não é? Mas não se preocupe! Você não vai precisar integrar ou derivar!
Observe que essa função depende apenas dos parâmetros /i (média) e c2 (variância),
que são parâmetros independentes.
No gráfico abaixo, temos uma f.d.p. com distribuição normal. Observe que a curva apresenta um formato de sino, que é uma característica de todas as variáveis normais.
As distribuições normais são simétricas, ou seja, tem-se:

Média = Mediana = Moda

Logo, o valor de /i divide a distribuição em duas partes iguais. Sabendo que a área total, sob toda a curva,corresponde à probabilidade de todo o Espaço Amostrai e, portanto, a 100%, então:

P(X > p) = P(X <p) = 50%

A probabilidade de um intervalo corresponde à área sob a f.d.p. limitada por esse intervalo. Assim, a igualdade acima pode ser ilustrada como no gráfico seguir:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

No exemplo do gráfico anterior, temos /z = 1, logo:

> 1) = P(X < 1) = 50%

Mas a simetria não implica somente nisso. A partir da média, toda a distribuição de probabilidades para os valores superiores é igual à distribuição para os valores inferiores.
Assim, para qualquer k real, a probabilidade de a variável ser maior do que jU + k é igual à probabilidade de ser menor do que n — k:
Em relação ao nosso exemplo, em que jU = 1, temos:

* Para k = 1: P(X > 2) = P(X < 0)

* Para k = 2: P(X > 3) = P(X < -1)

* Para k = 2,5: P(X > 3,5) = P(X < -1,5)

Similarmente, as probabilidades associadas aos intervalos entre a média e esses limites
/z + k e /z — k também são iguais, conforme equação abaixo e gráfico a seguir:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação ao nosso exemplo em que = 1, temos:

* Para/c = 1: P(1 < X < 2) = P(0 <X < 1)

* Para/c = 2:P(1 < X < 3) = P(-l <X< 1)

* Para k = 2,5: P(1 < X < 3,5) = P(-l,5 < X < 1)

Podemos observar, ainda, que a curva normal apresenta duas assintotas.

De modo geral, uma assintota ocorre quando uma curva se aproxima cada vez mais a uma reta, porém sem tocá-la. A curva normal se aproxima do eixo x (eixo das abcissas) tanto para x ->—oo, quanto para x -> +oo.
Por isso, dizemos que a curva normal é duplamente assintótica.

Além disso, existem dois pontos de inflexão na curva normal.

Pontos de inflexão são aqueles em que a concavidade da curva muda.

No início da curva normal, a concavidade está voltada para cima. No ponto (aproximado)
indicado pela seta da esquerda, a concavidade muda para baixo, e no ponto (aproximado) indicado pela seta da direita, a concavidade muda novamente para cima.
Esses pontos de inflexão ocorrem precisamente a 1 desvio padrão da média, ou seja, em p - o e em /z
+ o.

HORA IX

r i
(FGV/2010 - SEAD-AP - Adaptada) Em relação à distribuição normal, julgue as afirmativas a seguir.
I - A função de densidade de probabilidade é simétrica em relação à média.

II - O valor da mediana é igual ao valor da média.

III - A média de uma variável aleatória com distribuição normal pode ser negativa.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= Sabemos que a distribuição normal é simétrica em relação à média (logo, a afirmativa I está correta). Por ser =I
: simétrica, ela apresenta média = mediana (logo, a afirmativa II está correta).
;

I

I

A distribuição normal pode ter qualquer valor de média, inclusive negativa. Por exemplo, se estivermos i tratando do lucro das empresas que vão à falência, provavelmente, a média será negativa. Logo, a afirmativa i
; III está correta.
j

: Resposta: Todas corretas.

Distribuição Normal Padrão

Para calcular os valores de probabilidade, temos uma tabela que relaciona os valores de intervalo da variável aos respectivos valores de probabilidade.
Essa tabela, inserida abaixo, se refere a uma distribuição normal JV(0,1), isto é, com média n = 0 e variância o2 = 1, chamada de normal padrão ou reduzida, que denotamos por Z.
Pelo gráfico anterior à tabela, deduzimos que os seus valores correspondem à probabilidade entre a média
/x = 0 e o valor de z indicado. Assim, os campos da tabela informam a probabilidade P(0 < Z < z).

j *\

z

0,0

0,1

0,2

0,3

0,4

0,5

0,6

0,7

0,8

0,9

1,0

1,1

1,2

1,3

1,4

1,5

1,6

1,7

1,8

1,9

2,0

0,00 0,01 0,02 0,03 0,04 0,05 0,06
0,07 0,08 0,09

0,0000 0,0040 0,0080 0,0120 0,0160 0,0199 0,0239 0,0279
0,0319 0,0359

0,0398 0,0438 0,0478 0,0517 0,0557 0,0596 0,0636 0,0675
0,0714 0,0753

0,0793 0,0832 0,0871 0,0910 0,0948 0,0987 0,1026 0,1064
0,1103 0,1141

0,1179 0,1217 0,1255 0,1293 0,1331 0,1368 0,1406 0,1443
0,1480 0,1517

0,1554 0,1591 0,1628 0,1664 0,1700 0,1736 0,1772 0,1808
0,1844 0,1879

0,1915 0,1950 0,1985 0,2019 0,2054 0,2088 0,2123 0,2157
0,2190 0,2224

0,2257 0,2291 0,2324 0,2357 0,2389 0,2422 0,2454 0,2486
0,2517 0,2549

0,2580 0,2611 0,2642 0,2673 0,2704 0,2734 0,2764 0,2794
0,2823 0,2852

0,2881 0,2910 0,2939 0,2967 0,2995 0,3023 0,3051 0,3078
0,3106 0,3133

0,3159 0,3186 0,3212 0,3238 0,3264 0,3289 0,3315 0,3340
0,3365 0,3389

0,3413 0,3438 0,3461 0,3485 0,3508 0,3531 0,3554 0,3577
0,3599 0,3621

0,3643 0,3665 0,3686 0,3708 0,3729 0,3749 0,3770 0,3790
0,3810 0,3830

0,3849 0,3869 0,3888 0,3907 0,3925 0,3944 0,3962 0,3980
0,3997 0,4015

0,4032 0,4049 0,4066 0,4082 0,4099 0,4115 0,4131 0,4147
0,4162 0,4177

0,4192 0,4207 0,4222 0,4236 0,4251 0,4265 0,4279 0,4292
0,4306 0,4319

0,4332 0,4345 0,4357 0,4370 0,4382 0,4394 0,4406 0,4418
0,4429 0,4441

0,4452 0,4463 0,4474 0,4484 0,4495 0,4505 0,4515 0,4525
0,4535 0,4545

0,4554 0,4564 0,4573 0,4582 0,4591 0,4599 0,4608 0,4616
0,4625 0,4633

0,4641 0,4649 0,4656 0,4664 0,4671 0,4678 0,4686 0,4693
0,4699 0,4706

0,4713 0,4719 0,4726 0,4732 0,4738 0,4744 0,4750 0,4756
0,4761 0,4767

0,4772 0,4778 0,4783 0,4788 0,4793 0,4798 0,4803 0,4808
0,4812 0,4817

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Z (cont)
2,1

2,2

2,3

2,4

2,5

2,6

2,7

2,8

2,9

3,0

3,1

3,2

3,3

3,4

3,5

3,6

3,7

3,8

3,9

0,00 0,01 0,02 0,03 0,04 0,05 0,06
0,07 0,08 0,09

0,4821 0,4826 0,4830 0,4834 0,4838 0,4842 0,4846 0,4850
0,4854 0,4857

0,4861 0,4864 0,4868 0,4871 0,4875 0,4878 0,4881 0,4884
0,4887 0,4890

0,4893 0,4896 0,4898 0,4901 0,4904 0,4906 0,4909 0,4911
0,4913 0,4916

0,4918 0,4920 0,4922 0,4925 0,4927 0,4929 0,4931 0,4932
0,4934 0,4936

0,4938 0,4940 0,4941 0,4943 0,4945 0,4946 0,4948 0,4949
0,4951 0,4952

0,4953 0,4955 0,4956 0,4957 0,4959 0,4960 0,4961 0,4962
0,4963 0,4964

0,4965 0,4966 0,4967 0,4968 0,4969 0,4970 0,4971 0,4972
0,4973 0,4974

0,4974 0,4975 0,4976 0,4977 0,4977 0,4978 0,4979 0,4979
0,4980 0,4981

0,4981 0,4982 0,4982 0,4983 0,4984 0,4984 0,4985 0,4985
0,4986 0,4986

0,4987 0,4987 0,4987 0,4988 0,4988 0,4989 0,4989 0,4989
0,4990 0,4990

0,4990 0,4991 0,4991 0,4991 0,4992 0,4992 0,4992 0,4992
0,4993 0,4993

0,4993 0,4993 0,4994 0,4994 0,4994 0,4994 0,4994 0,4995
0,4995 0,4995

0,4995 0,4995 0,4995 0,4996 0,4996 0,4996 0,4996 0,4996
0,4996 0,4997

0,4997 0,4997 0,4997 0,4997 0,4997 0,4997 0,4997 0,4997
0,4997 0,4998

0,4998 0,4998 0,4998 0,4998 0,4998 0,4998 0,4998 0,4998
0,4998 0,4998

0,4998 0,4998 0,4999 0,4999 0,4999 0,4999 0,4999 0,4999
0,4999 0,4999

0,4999 0,4999 0,4999 0,4999 0,4999 0,4999 0,4999 0,4999
0,4999 0,4999

0,4999 0,4999 0,4999 0,4999 0,4999 0,4999 0,4999 0,4999
0,4999 0,4999

0,5000 0,5000 0,5000 0,5000 0,5000 0,5000 0,5000 0,5000
0,5000 0,5000

E quanto aos valores de z?

O valor de z começa a ser lido na primeira coluna (que apresenta as unidades e os décimos de z) e termina de ser lido na primeira linha (que apresenta os centésimos de z). Assim, a probabilidade P(0 < Z < z) é o valor que está no campo, cuja linha corresponda à unidade e ao décimo de z e cuja coluna corresponda ao centésimo de z.
Por exemplo, para encontrar o valor de P(0 < Z < 1,96), precisamos buscar o número que está na linha 1,9e na coluna 0,06, conforme indicado abaixo. Podemos observar que P(0 < Z < 1,96) = 0,475.

z 0,05 0,06 0,07

1,8

1,9

0,4678 0,4686 0,4693

0,4744 0,475 0,4756

0,4798 0,4803 0,4808

Também podemos fazer o caminho inverso, qual seja, encontrar o valor de z que corresponde à probabilidade desejada.
Vamos encontrar o valor de z tal que P(0 < Z < z) = 0,40, por exemplo. Para isso,
devemos buscar o valor
0,40 nos campos da tabela. Como não consta exatamente esse valor, somente 0,3997 e
0,4015, optamos pelo valor mais próximo, isto é, 0,3997.
Este se encontra na linha 1,2 e na coluna 0,08, conforme indicado a seguir. Logo, concluímos que z
= 1,28.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

z

1,1

1,2

1,3

0,07

0,3577

0,379

0,398

0,4147

0,08

0,3599

0,381

0,3997

0,4162

0,09

0,3621

0,383

0,4015

0,4177

Para resolver questões envolvendo a tabela normal padrão é importante lembrar que essa distribuição é simétrica, com média /j. = 0.
TOME

NOTA!

Supondo, por exemplo, z = 1,96, vimos que P(0 < Z < 1,96) = 0,475. Logo:

P(Z > 1,96) = 0,5 - P(0 < Z < 1,96) = 0,5 - 0,475 = 0,025

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

r P(0 < Z < 1,96)

K

T"

0,5

P(Z> 1,96)

P(-l, 96 < Z < 0) = P(0 < Z < 1,96) = 0,475

P(Z < -1,96) = P(Z > 1,96) = 0,5 - 0,475 = 0,025

A questão pode solicitar e/ou fornecer a probabilidade em módulo, da forma P(|Z| < z)
ou P(|Z| > z). Para resolvê-las, é importante lembrar que a probabilidade P(|Z| < z) corresponde a:
P(|Z| < z) = P(-z < Z < z) = P(-z < Z < 0) + P(0 < Z < z)

P(|Z| <z) = P(-z<Z<z)

Pela simetria da normal padrão, temos P(—z < Z < 0) = P(0 < Z < z), logo:

P(|Z| < z) = 2 x P(0 < Z < z)

Supondo, por exemplo, z = 1,96, vimos que P(0 < Z < 1,96) = 0,475. Logo:

P(|Z| < 1.96) = 2 x P(0 < Z < 1.96) = 2 x 0,475 = 0,95

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E a probabilidade P(|Z| > z) pode ser calculada pela fórmula da probabilidade complementar:

P(|Z|>z) = l-P(|Z|<z)

P(|Z| > z) = 1 - 2 x P(0 < Z < z)

Supondo, por exemplo, z = 1,96, vimos que P(0 < Z < 1,96) = 0,475. Logo:

P(|Z| > z) = 1 — 2 x P(0 <Z <z) = 1 - 2 x 0,475 = 1 - 0,95 = 0,05

Ou, também podemos calcular P(|Z| > z), aplicando-se o raciocínio análogo ao que fizemos anteriormente
P(|Z| > z) = P(Z < -z U Z > z) = P(Z < -z) + P(Z > z)

Pela simetria da normal padrão, temos P(Z < -z) = P(Z > z), logo:

P(|Z| < z) = 2 x P(Z > z)

Para z = 1,96, em que P(Z > 1,96) = 0,025, temos:

P(|Z| > z) = 2 x P(Z > z) = 2 x 0,025 = 0,05

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Existem, ainda, outros tipos de tabela para a distribuição normal padrão, que apresentam as probabilidades para outros intervalos, como por exemplo para a região indicada a seguir:
Esse tipo de tabela indica as probabilidades da forma P(—oo < z < z), que correspondem à função da distribuição normal acumulada.
Transformação entre Distribuições Normais

Mas, e se a média da distribuição for diferente de zero e/ou a variância for diferente de 1?

Para isso, fazemos uma transformação de uma distribuição normal qualquer para a distribuição normal padrão, conforme fórmula indicada abaixo:
x-/z

<r

Com essa transformação, encontramos os valores de z na distribuição normal padrão associados aos valores de x da distribuição normal de interesse, com média /z e desvio padrão o.
Vamos supor uma distribuição normal com média /z = 1 e desvio padrão cr
= 3, em que estamos interessados no valor de x = 7. A transformação desse valor para a distribuição normal padrão é:
Isso significa que os intervalos associados a z = 2 na distribuição normal padrão apresentam a mesma probabilidade daqueles associados a x = 7 na distribuição X, com média /z = 1 e desvio padrão cr =3.

Por exemplo:

> 7) = P(Z > 2)

Pela tabela da normal padrão, temos P(0 < Z < 2) = 0,4772, logo:

P(Z > 2) = 0,5 - 0,4772 = 0,0228

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Portanto, P(X > 7) = 0,0228 = 2,28%.

Analogamente, temos:

< 7) = P(Z < 2)

Sabemos que P(Z > 2) = 0,5 - 0,4772 = 0,0228, logo:

P(Z < 2) = 1 - P(Z > 2) = 1 - 0,0228 = 0,9772

Portanto, P(X < 7) = 0,9772.

Para encontrar intervalos envolvendo outros valores, por exemplo P(4 < X <
7), precisamos aplicar a transformação para ambos os valores. Para x = 4, temos:
Sabendo que a transformação para x = 7 é z = 2, então podemos concluir que:

P(4<X<7) = P(KZ<2)

A probabilidade P(1 < Z < 2) pode ser calculada como:

P(1 < Z < 2) = P(0 < Z < 2) - P(0 < Z < 1)

Pela tabela da distribuição normal, observamos que P(0 < Z < 1) = 0,3413 e que P(0 < Z < 2)=0,4772,
logo:

P(1 < Z < 2) = 0,4772 - 0,3413 = 0,1359

Assim, concluímos que P(4 < X < 7) = 0,1359 = 13,59%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Também podemos fazer o caminho inverso, encontrando o valor de x em uma distribuição com média /z e desvio padrão a, a partir de uma probabilidade desejada.
Para isso, primeiro encontramos o valor de z correspondente a essa probabilidade desejada, utilizando a tabela da normal padrão. Em seguida, aplicamos a fórmula da transformação.
Por exemplo, podemos calcular o valor de x para o qual a probabilidade de
P(X < x) = 0,8, para a distribuição normal com os mesmos parâmetros do exemplo anterior (/z = 1 e a = 3).
Considerando a simetria em torno de zero da normal padrão, temos que:

P(0 < Z < z) = P(Z < z) — 0,5

Assim, precisamos encontrar, na tabela normal padrão, o valor de z que corresponde a:

P(0 < Z < z) = 0,8 - 0,5 = 0,3

Pela tabela da distribuição normal padrão, observamos que esse valor é z = 0,84, pois
P(0<Z<0,84) = 0,2995,
que é o valor da tabela mais próximo de 0,3.

Substituindo os valores conhecidos na fórmula transformação (/i = 1, a = 3
e z = 0,84), podemos encontrar o valor de x, que delimita uma probabilidade P(X < x) = 0,8:
X — jlí z =
cr x — 1
0,84

x = 3 x 0,84 + 1 = 3,52

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, vamos calcular as probabilidades associadas a intervalos genéricos, em função do desvio padrão a.
Para calcular a probabilidade P(g - o < X < /z + c), utilizamos a seguinte transformação, para x =
/z + ff:

x — /z n + a — /z z = = z = = 1a ff

Para x = n - ff, temos:

x — // fi- ff - /.t z = = z = = —1
ff ff

Portanto:

P(n - ff < X < n + ff) = P(-l < Z < 1) = P(-l < Z < 0) + P(0 < Z < 1)

De maneira geral, quando os intervalos são da forma P(/z — k < X < p. + P), em que os extremos são equidistantes da média, basta fazermos a transformação para um dos extremos, pois o outro estará associado ao mesmo valor de z, porém multiplicado por -1.
Pela tabela da curva normal, temos P(0 < Z < 1) = 0,3413. Pela simetria da normal padrão, em torno da média 0, temos:
P(-l < Z < 0) = P(0 < Z < 1) = 0,3413

Logo:

P(-l < Z < 1) = P(-l < Z < 0) + P(0 < Z < 1) = 0,3413 + 0,3413 = 0,6826

P(/z - ti < X < /z + tr) = 68%

Ou seja, a probabilidade de uma variável normal qualquer se afastar da média (para cima ou para baixo) em até 1 desvio padrão é aproximadamente 68%, conforme ilustrado a seguir.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para P(/z — 2o < X < fi + 2o), temos:

Portanto:

x — n JU + 2<7 — /z z = = = 2
o o

PO - 2o < X < n + 2o) = P(—2 <Z < 2) = P(—2 < Z < 0) + P(0 < Z < 2)

Pela tabela, temos P(0 < Z < 2) = 0,4772. Considerando a simetria da normal padrão, temos:

P(—2 < Z < 0) = P(0 < Z < 2) = 0,4772

E a probabilidade desejada é:

P(-2 < Z < 2) = P(—2 < Z < 0) + P(0 < Z < 2) = 0,4772 + 0,4772 = 0,9544

P(li - 2o < X < n + 2o-) = 95%

Ou seja, a probabilidade de uma variável normal qualquer se afastar da média (para cima ou para baixo) em até 2 desvios padrão é aproximadamente 95%, como ilustrado abaixo.
Para P(/z — 3o < X < fi + 3o), obtemos, pela transformação, z = 3, logo:

P(jj. — 3o < X < n + 3o) = P(—3 < Z < 3) = P(—3 < Z < 0) + P(0 < Z < 3)

Pela tabela, temos P(0 < Z < 3) = 0,4987 e, pela simetria, P(—3 < Z < 0) = 0,4987, logo:

P(-3 < Z < 3) = P(—3 < Z < 0) + P(0 < Z < 3) = 0,4987 + 0,4987 = 0,9974

P(H - 3o < X < n + 3<r) = 99,7%

Ou seja, a probabilidade de uma variável normal qualquer se afastar da média (para cima ou para baixo) em até 3 desvios padrão é aproximadamente 99,7%, ilustrado abaixo.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Essas probabilidades (68% para fi ± a; 95% para fi±2a e 99,7% para fi ± 3a) compõem a chamada RegraEmpírica. Algumas questões (não muitas) exigem que você memorize essas probabilidades.

ESQUEMATIZANDO

Distribuição Normal: N(/t, cr2)

Simétrica, com formato de sino, definida em toda a reta real
Regra Empírica: 68% para g ± a; 95% para g ± 2a e 99,7% para /i±3a

X—[l

Transformação para a Normal Padrão N(0,l): Z =--------------

l«** IX

(FGV/2010 - SEAD-AP - Adaptada) Em relação à distribuição normal, julgue as afirmativas a seguir:

I - Se X tem distribuição normal com média // e variância cr2 então a variável Z = tem distribuição normal padrão.
II - A probabilidade de que uma variável Z que tenha distribuição normal padrão seja maior que 5 é aproximadamente igual a 0.
Comentários:

Em relação à afirmativa I, a transformação para a Normal Padrão é Z = ou seja, a divisão é pelo desvio d padrão, não pela variância. Por isso, a afirmativa I está incorreta.
Em relação à afirmativa II, a distribuição se concentra em 3 desvios-padrão para ambos os lados (mais de99% se encontram nesse intervalo). De fato, as tabelas da normal padrão, em geral,
fornecem valores até z=3,99 porque valores a probabilidade de Z ser maior que isso é praticamente nula.Logo, a afirmativa II está correta.
Resposta: I - incorreta, II - correta.

(VUNESP/2009 - CETESB) Para um determinado horário, considerando-se todos os dias de um período, ao se calcular a média de congestionamento de trânsito em km obtém-se o valor p. e desvio padrão cr.Considerando-se que os valores obtidos pela variável e suas respectivas probabilidades constituem uma distribuição normal, no intervalo de QÍ - a) até (ji + a), a percentagem dos dados contidos é cerca de
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

í a) 25%
b) 50%

; c) 68%

d) 94%

í e) 99%

i Comentários:

= Essa questão exige o conhecimento da Regra Empírica. Vimos que o intervalo de Qu —
cr) até (/./ + cr)

: concentra 68% da distribuição normal.

i Gabarito: C

; (CESPE/2016 - Analista da FUNPRESP-JUD) A simetria de Z implica que P(Z > 2) = 1 - P(Z < -2).

i Comentários:

A simetria da curva normal com média igual a zero implica na seguinte relação entre P(Z > 2) e P(Z
< -2):

P(Z > 2) = P(Z < -2)

= Essa relação está ilustrada no gráfico abaixo.

A relação descrita no enunciado iguala a probabilidade P(Z > 2) à probabilidade 1 - P(Z < —2). Esta i corresponde a toda a região indicada abaixo:
I

: Podemos observar que P(Z > 2) é bem menor que 50%, enquanto 1 — P(Z < —2) é bem maior que 50%,i ou seja:

P(Z > 2) ¥= 1 - P(Z < -2)

= Logo, o item está errado.

: Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I; (FGV/2022 - EPE) O salário médio dos funcionários de uma empresa é normalmente distribuído com média de R$ 2.500,00 e desvio padrão de R$ 1.500,00. A empresa divide os funcionários em 5classes, a saber: M,

= N, O, P e Q, onde "M" é a classe com melhor salário e "Q" a classe com menor salário.

: Se apenas 5% dos funcionários dessa empresa estão na classe "M", o menor valor do salário do funcionário
= para ele pertencer à classe "M" é

= [Considere que P(Z < 1,64) = 0,95.]
í a) 3900,00

b) 4170,00

í c) 4960,00

d) 5160,00

; e) 5350,00

i Comentários:

I

: O enunciado informa que os salários seguem distribuição normal com média p =
R$ 2.500,00 e desvio

= padrão o = R$1.500,00; e pede o valor do menor salário da classe M, associada aos
5% melhores salários,

= conforme ilustrado a seguir:

= Sabendo que 5% (ou 0,05) da distribuição é maior do que o valor buscado, então 95% (ou 0,95) da distribuição é menor e o enunciado informa justamente que P(Z < 1,64) = 0,95.
= Assim, devemos aplicar a transformação para z = 1,64, sabendo que a média é 2500
e o desvio padrão é j 1500:
I
x- p z =
o x- 2500
1,64 =

1500

x - 2500 = 1,64 x 1500 = 2460

x = 4960

Gabarito: C

i (VUNESP/2014 - EMPLASA) O tempo de vida da população de um determinado país tem distribuição normal
; com a média igual a 68 anos e o desvio padrão igual a 11.

I X—u

= Considere os valores da tabela e a fórmula Z =------------ :

:
cr

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

z

0,5

1,0

1,5

2,0

2,5

Distribuição normal reduzida
0,1915

0,3413

0,4332

0,4772

0,4938

A probabilidade de uma pessoa viver mais do que 90 anos é de a) 15,87%
b) 6,68%

c) 4,82%

d) 3,36%

e) 2,28%

Comentários:

Sendo p = 68 e cr = 11, temos a seguinte transformação para x = 90:

x — p z =
a

90 - 68 22

11 _ TT

Pela tabela, que apresenta a probabilidade P(0 < Z < z), temos:

P(0 < Z < 2) = 0,4772

Logo:

P(Z > 2) = 0,5 - P(0 < Z < 2) = 0,5 - 0,4772 = 0,0228

I

; Gabarito: E.

; (FCC/2015 - Auditor Fiscal da SEFAZ/PI) Se Z tem distribuição normal padrão, então:
P(Z < 0,4) = 0,655; P(Z

; < 1,2) = 0,885; P(Z < 1,6) = 0,945; P(Z < 1,8) = 0,964; P(Z < 2) = 0,977.
I

: O efeito do medicamento A é o de baixar a pressão arterial de indivíduos hipertensos. O tempo, em minutos,
decorrido entre a tomada do remédio e a diminuição da pressão é uma variável aleatória X com distribuição
= normal, tendo média p e desvio padrão o. Se o valor de p é de 56 min e o valor de o é de 10 min, a i probabilidade de X estar compreendido entre 52 min e 74 min é igual a a) 30,9%
b) 56,0%

í c) 61,9%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

d) 52,4%

e) 64,5%

Comentários:

A probabilidade de X estar entre 52 min e 74 min pode ser calculada a partir das transformações para x = 74min e para x = 52 min, considerando a média de 56 min e desvio padrão de 10 min.

Para x = 74, temos:

X — [1

z =

(J

74- 56 18

z ~ 10 _ 10 _ 1,8

A transformação para x = 52 é:

52 - 56 —4

z ~ io _ io _ 0,4

Então, a probabilidade de X estar compreendido entre 52 min e 74 min corresponde a:

P(52 < X < 74) = P(—0,4 < Z < 1,8)

Essa probabilidade pode ser calculada como:

P(—0,4 <Z < 1,8) = P(Z < 1,8) - P(Z < -0,4)

: P(Z < 1,8)

: Pela tabela observamos que P(Z < 1,8) = 0,964. Além disso, temos P(Z
< 0,4) = 0,655, logo, o seu i complementar é:
= Pela simetria da normal padrão, temos:

P(Z < -0,4) = P(Z > 0,4) = 0,345

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= Inserindo esses valores na equação acima, temos:
j

P(52 < X < 74) = P(Z < 1,8) - P(Z < -0,4) = 0,964 - 0,345 = 0,619

; Gabarito: C

L

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Distribuição Normal

Item. 1. (CESPE/2010 - INCA) Com relação a distribuições de probabilidade e seus parâmetros conceitos inerentes à estatística básica, julgue o item seguinte.
A distribuição Normal ou Gaussiana caracteriza-se por ter seus valores de média e desvio padrão independentes entre si.
Comentários:

Os parâmetros da distribuição normal são a média e o desvio padrão, sendo que um não interfere na definição do outro. Logo, são independentes entre si.
Gabarito: Certo.

Item. 2. (CEBRASPE/2018 - Oficial Técnico de Inteligência da ABIN) Em uma fábrica de ferragens, o departamento de controle de qualidade realizou testes na linha de produção de parafusos. Os testes ocorreram em dois campos: comprimento dos parafusos e frequência com que esse comprimento fugia da medida padrão. Historicamente, o comprimento médio desses parafusos é 3 cm, e o desvio padrão observado é 0,3 cm. Foram avaliados 10.000 parafusos durante uma semana. Desses, 1.000 fugiram às especificações técnicas da gerência: o comprimento do parafuso deveria variar de 2,4 cm a 3,6 cm. Ochefe da linha de produção, porém, insiste em afirmar que, em média, 4% da produção de parafusos fogem às especificações.O departamento de controle de qualidade assume que os comprimentos dos parafusos têm distribuição normal.
A partir dessa situação hipotética, julgue o item subsequente, considerando que 0(1) =
0,841, 0(1,65) = 0,95,
0(2) = 0,975 e 0(2,5) = 0,994, em que O(z) é a função distribuição normal padronizada acumulada, e que
0,002 seja valor aproximado para

Considere que o maior parafuso já encontrado na linha de produção tenha 3,75 cm de comprimento. Nesse caso, a probabilidade de que um parafuso escolhido aleatoriamente tenha comprimento maior que esse será superior a 1%.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para calcular a probabilidade de P(X > 3,75), utilizamos a transformação para x =
3,75, com média de 3cm =

3) e desvio padrão de 0,3cm (a = 0,3):

x — [d z =
a

3,75 - 3 0,75

="

Observamos, pela tabela, que P(Z < 2,5) = 0,994. Logo:

> 2,5) = 1 - P(Z < 2,5) = 1 - 0,994 = 0,006 = 0,6%

Esse valor é inferior a 1%.

Gabarito: Errado.

Item. 3. (CEBRASPE/2018 - Agente de Polícia Federal) O valor diário (em R$ mil)
apreendido de contrabando em determinada região do país é uma variável aleatória W que segue distribuição normal com média igual aR$ 10 mil e desvio padrão igual a R$4 mil. Nessa situação hipotética, julgue o próximo item.

P(W > R$ 10 mil) = 0,5.

Comentários:

Considerando que a distribuição normal é simétrica em torno da média, então:

P(W > ju) = 0,5

Como p = 10 mil, então:

P(V7 > 10 mil) = 0,5

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 4. (CEBRASPE/2018 - Agente de Polícia Federal) O valor diário (em R$ mil)
apreendido de contrabando em determinada região do país é uma variável aleatória W que segue distribuição normal com média igual aR$ 10 mil e desvio padrão igual a R$4 mil. Nessa situação hipotética, julgue o próximo item.

A razão segue distribuição normal padrão.

Comentários:

Sendo W uma variável com distribuição normal e média = 10 e desvio padrão <7 = 4
então a seguinte variável seguirá distribuição normal padrão:
W-p. HZ-10

Ou seja, W não segue distribuição normal padrão.

V4

Gabarito: Errado.

Item. 5. (CEBRASPE/2016 - TCE-PR) Se X for uma variável aleatória normal com média 0,8 e variância 0,4, e P(X
< x) representar a função de distribuição de probabilidade acumulada dessa variável X, para x G R,
então

XQ g a) A razão —— será uma variável aleatória normal padrão.0,4

b) O coeficiente de variação de X será inferior a 0,4

c) A moda de X será inferior a 0,6

d) P(X = 0,8) = P(X = 0,1)

e) P(X < 0,7) < P(X > 0,9)

Comentários:

Sendo X uma variável com distribuição normal e média jU = 0,8 e variância cr2 =
0,4 (portanto, desvio padrão

<7 = VÕ/4), então a seguinte variável seguirá distribuição normal padrão:

X-i2 X-0,8

— =

a

Q g

Ou seja, a razão q4 não é uma variável normal padrão e a alternativa A está incorreta.

O coeficiente de variação é a razão:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(7

Que é superior a 0,4, logo a alternativa B está incorreta.

A moda de uma distribuição normal é igual à média, no caso, = 0,8, que é superior a 0,6.

A probabilidade P(X = 0,8) é a mesma que P(X = 0,1), pois como a variável é contínua, a probabilidade de se observar um valor específico (qualquer valor que seja) é nula:
P(X = 0,8) = P(X = 0,1) = 0

Logo, a alternativa está correta.

Por fim, como a distribuição normal é simétrica, a probabilidade de a distribuição se distanciar da média em mais de 0,1 para ambos os lados é a mesma, ou seja:
Logo, a alternativa E está incorreta.

Gabarito: D.

Item. 6. (CEBRASPE/2013 - TRT-ES) Com relação à teoria de probabilidades, julgue o próximo item.

~0O ( X2\

Com base na distribuição Normal, é correto afirmar que J_oo exp I — — \ dx > 2.

Comentários:

A notação exp y) é uma alternativa à notação e (4). Ou seja, o enunciado está interessado no valor de:
Para isso, vejamos a f.d.p. da distribuição normal:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comparando as duas expressões, percebemos que temos = 0 e J = 1 (curva normal padrão):

/to = J^=e 2)

\2n

Sabemos que a área sob toda a curva é igual a 1, ou seja, a integral de —oo a °o é igual a 1:

= 1

pOO I

Vamos denotar por F o resultado desejado: F = J_m e' 2 dx. Como -to é uma constante, temos:
F = y/2n

Como n = 3,14 > 2, então a raiz V2zr = y/2 x 3,14 > 2, mais precisamente:

F = V2?r = 2,5

Gabarito: Certo.

Item. 7. (CEBRASPE/2015 - FUB) Em um estudo, determinou-se que a medida representada pela variável aleatória X segue a distribuição normal com média le variância 4 e que a função de densidade dessa variável é expressa por:
em quexé um número real. Com base nos dados desse estudo, julgue o itema seguir, considerando que 0(0,674) = 0,750,0(2,0) = 0,977 e 0(3,0) = 0,999, em queO(z) representa a função de distribuição acumulada da distribuição normal padrão.
É correto afirmar que P( | X | < 5) = 0,954.

Comentários:

A proba&itàpfte 2023 (Pós-Edital)

P( |XI < 5) = P(-5 < X < 5)

Sabendo que a média deXéjiz = lea variância é V(X) = 4, logo, o desvio padrão é a
= yjVÇX') = 2, então a transformação para a normal padrão para x = 5 é:
x - jU 5 — 1

E para x = -5 é:

Logo, a probabilidade desejada equivale a:

P(-5 < X < 5) = P(-3 < Z < 2) = P(Z < 2) - P(Z < -3)

Pelos valores fornecidos, observamos que P(Z < 2) = 0,977. Além disso, pela simetria da normal padrão, temos:P(Z < -3) = P(Z > 3)

Sabendo que P(Z < 3) = 0,999, então o seu complementar é:

P(Z < -3) = P(Z > 3) = 1 - P(Z < 3) = 1 - 0,999 = 0,001

Logo, a probabilidade desejada é:

P(-5 < X < 5) = P(Z < 2) - P(Z < -3) = 0,977 - 0,001 = 0,976

Portanto, o item está errado. O valor fornecido corresponde à probabilidade de P( | Z
| < 2), ou seja, de P(-2 < Z

<2).

Gabarito: Errado.

Item. 8. (CEBRASPE/2015 - FUB) Em um estudo, determinou-se que a medida representada pela variável aleatória X segue a distribuição normal com média le variância 4 e que a função de densidade dessa variável é expressa por:
¹ ™- ÊXP —

1 »

em quexé um número real. Com base nos dados desse estudo, julgue o itema seguir, considerando que 0(0,674) = 0,750,0(2,0) = 0,977 e 0(3,0) = 0,999, em queO(z) representa a função de distribui5gR^n^^tfi|^is^yjfigaeo^l(pg^isfitel)
A probabilidade de se observar o evento [X = 1] é igual a ^=.

Comentários:

Por se tratar de uma variável contínua, a probabilidade de se observar um valor específico, qualquer que seja,é igual a zero.

Gabarito: Errado.

Item. 9. (CEBRASPE/2015 - FUB) Em um estudo, determinou-se que a medida representada pela variável aleatória X segue a distribuição normal com média le variância 4 e que a função de densidade dessa variável é expressa por:
¹ ™- ÊXP —

2VS " »

em quexé um número real. Com base nos dados desse estudo, julgue o itema seguir, considerando que 0(0,674) = 0,750,0(2,0) = 0,977 e 0(3,0) = 0,999, em queO(z) representa a função de distribuição acumulada da distribuição normal padrão.
0 terceiro quartil da distribuição X é igual a 2,348.

Comentários:

0 terceiro quartil Q3 está associado à probabilidade de:

P(X < Q3) = 0,75

Pelos valores fornecidos, observamos que P(Z < 0,674) = 0,75.

Sabendo que a média deXéjiz = lea variância é V(X) = 4, logo, o desvio padrão é o
= yjV(X} = 2, então a transformação de z = 0,674 para X é:
x - jU

z =

(J

0,674

x — 1

x = 2 x 0,674 + 1 = 2,348

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Distribuição Normal

Item. 1. (CESPE/2010 - INCA) Com relação a distribuições de probabilidade e seus parâmetros conceitos inerentes à estatística básica, julgue o item seguinte.
A distribuição Normal ou Gaussiana caracteriza-se por ter seus valores de média e desvio padrão independentes entre si.
Item. 2. (Cebraspe/2018 - Oficial Técnico de Inteligência da ABIN) Em uma fábrica de ferragens, o departamento de controle de qualidade realizou testes na linha de produção de parafusos. Os testes ocorreram em dois campos: comprimento dos parafusos e frequência com que esse comprimento fugia da medida padrão. Historicamente, o comprimento médio desses parafusos é 3 cm, e o desvio padrão observado é 0,3 cm. Foram avaliados 10.000 parafusos durante uma semana. Desses, 1.000fugiram às especificações técnicas da gerência: o comprimento do parafuso deveria variar de 2,4 cm a 3,6 cm. Ochefe da linha de produção, porém, insiste em afirmar que, em média, 4% da produção de parafusos fogem às especificações. O departamento de controle de qualidade assume que os comprimentos dos parafusos têm distribuição normal.
A partir dessa situação hipotética, julgue o item subsequente, considerando que 0(1) =
0,841, 0(1,65) =
0,95, 0(2) = 0,975 e 0(2,5) = 0,994, em que O(z) é a função distribuição normal padronizada acumulada,
e que 0,002 seja valor aproximado para

0,0384

10.000'

Considere que o maior parafuso já encontrado na linha de produção tenha 3,75 cm de comprimento. Nesse caso, a probabilidade de que um parafuso escolhido aleatoriamente tenha comprimento maior que esse será superior a 1%.
Item. 3. (Cebraspe/2018 - Agente de Polícia Federal) O valor diário (em R$ mil)
apreendido de contrabando em determinada região do país é uma variável aleatória W que segue distribuição normal com média igual a R$ 10 mil e desvio padrão igual a R$ 4 mil. Nessa situação hipotética, julgue o próximo item.
P(W > R$ 10 mil) = 0,5.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

/ 33

/

Item. 4. (Cebraspe/2018 - Agente de Polícia Federal) O valor diário (em R$ mil)
apreendido de contrabando em determinada região do país é uma variável aleatória W que segue distribuição normal com média igual a R$ 10 mil e desvio padrão igual a R$ 4 mil. Nessa situação hipotética, julgue o próximo item.
A razão W^° segue distribuição normal padrão.

Item. 5. (Cebraspe/2016 - TCE-PR) Se X for uma variável aleatória normal com média
0,8 e variância 0,4, e
P(X < x) representar a função de distribuição de probabilidade acumulada dessa variável
X, para x E R,
então y Q g a) A razão —será uma variável aleatória normal padrão.
b) O coeficiente de variação de X será inferior a 0,4

c) A moda de X será inferior a 0,6

d) P(X = 0,8) = P(X = 0,1)

e) P(X < 0,7) < P(X > 0,9)

Item. 6. (Cebraspe/2013 - TRT-ES) Com relação à teoria de probabilidades, julgue o próximo item.

- QQ /

Com base na distribuição Normal, é correto afirmar que exp ( — — J dx > 2.

Item. 7. (Cebraspe/2015 - FUB) Em um estudo, determinou-se que a medida representada pela variável aleatória X segue a distribuição normal com média le variância 4 e que a função de densidade dessa variável é expressa por:
JW-

em quexé um número real. Com base nos dados desse estudo, julgue o itema seguir,
considerando que 0(0,674) = 0,750,0(2,0) = 0,977 e 0(3,0) = 0,999, em queO(z) representa a função de distribuição acumulada da distribuição normal padrão.
É correto afirmar que P( | X | < 5) = 0,954.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 8. (Cebraspe/2015 - FUB) Em um estudo, determinou-se que a medida representada pela variável aleatória X segue a distribuição normal com média le variância 4 e que a função de densidade dessa variável é expressa por:
JW- _*_«p _ fclZ

em quexé um número real. Com base nos dados desse estudo, julgue o itema seguir,
considerando que 0(0,674) = 0,750, 0(2,0) = 0,977 e 0(3,0) = 0,999, em que O(z)representa a função de distribuição acumulada da distribuição normal padrão.
A probabilidade de se observar o evento [X = 1] é igual a ^=-

Item. 9. (Cebraspe/2015 - FUB) Em um estudo, determinou-se que a medida representada pela variável aleatória X segue a distribuição normal com média le variância 4 e que a função de densidade dessa variável é expressa por:
JW- _*_«p _ fclZ

em quexé um número real. Com base nos dados desse estudo, julgue o itema seguir,
considerando que 0(0,674) = 0,750,0(2,0) = 0,977 e 0(3,0) = 0,999, em queO(z) representa a função de distribuição acumulada da distribuição normal padrão.
0 terceiro quartil da distribuição X é igual a 2,348.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. CERTO 4. ERRADO
Item. 7. ERRADO

Item. 2. ERRADO 5. LETRA D
Item. 8. ERRADO

Item. 3. CERTO 6. CERTO
Item. 9. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

