# Probabilidade e Estatística - Estimação Intervalar

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Distribuição Amostrai

2) Estimação Intervalar

3) Questões Comentadas - Distribuição Amostrai - Cebraspe

4) Questões Comentadas - Estimação Intervalar - Cebraspe

5) Lista de Questões - Distribuição Amostrai - Cebraspe

6) Lista de Questões - Estimação Intervalar - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

DISTRIBUIçÃo AMoSTRAL

Nesta seção, estudaremos a distribuição de probabilidade dos principais estimadores, chamada deDistribuição Amostral. Vale ressaltar que os estimadores são variáveis aleatórias e por isso apresentam distribuições de probabilidade.
Inicialmente, é importante pontuar que a distribuição dos elementos de uma amostra aleatória qualquer segue a mesma distribuição populacional.
Por exemplo, vamos considerar uma moeda com 2 faces, que vamos chamar de face 0 e face 1. Tratando-se de uma moeda equilibrada, a probabilidade de cada face é de - = 0,5 e a esperança e variância são,respectivamente:

£(%) = \x.P(X = x)

£(%) = 0 x 0,5 + 1 x 0,5 = 0,5

y(X) = - ^y.pçx = x)

, 1 o 1 0,25 + 0,25

7(X) = (0 - 0,5)2 x - + (i - 0,5)2 x - = = 0,25

Agora, suponha que vamos extrair uma amostra aleatórias de tamanho 3, ou seja, vamos lançar a moeda 3vezes. Podemos representar essa amostra porX1(X2,X3.

Considerando que os possíveis resultados das amostras são os mesmos da população (0 ou
1) e com as mesmas probabilidades de - = 0,5 para cada face, então temos:
E(XJ = E(X2) = E(X3) = 0 x 0,5 + 1 x 0,5 = 0,5

, 1 , 1 0,25 + 0,25

V(XJ = 7(X₂) = V(xy = (0 - 0,5)2 x - + (1 - 0,5)2 x - =
= 0,25

Ou seja, a esperança e a variância de cada amostra são iguais às da população:

E® = F(X) =
7(Xf) = V(X) = a2

Na verdade, toda a distribuição de probabilidade da amostra é igual à distribuição de probabilidade da população (as esperanças e as variâncias são iguais como consequência desse fato).
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Quando as variáveis X1,X2,X3, ...Xn, que representam os elementos da amostra,
são independentes, dizemos que elas independentes e identicamente distribuídas (i.i.d.), isto é, são independentes e apresentam a mesma distribuição (igual à da população).
Isso ocorre quando a população é infinita (ou muito grande em comparação com o tamanho da amostra) ou quando a amostra é extraída com reposição.
I«** IX

i (FGV/2021 - FunSaúde/CE - Adaptada) Se Xi, X2, ... Xn é uma amostra aleatória simples extraída de uma população infinita com determinada distribuição de probabilidades f(x), avalie se as afirmativas a seguir
= estão corretas.

; I. Xi, X2,... Xn são independentes.

= II. Xi, X2,... Xn são identicamente distribuídos.

; III. Nem sempre cada Xi, i = 1,..., n, tem distribuição f(x).

: Está correto 0 que se afirma em

: a) I, apenas.

b) I e II, apenas.

= c) I e III, apenas.

d) II e III, apenas.
í e) I, II e III.

; Comentários:

: Essa questão trabalha com os conceitos fundamentais envolvendo distribuição amostrai.

= Sendo a população infinita, então os elementos da amostra (que 0 enunciado chamou de Xi, X2,... Xn) são
: variáveis aleatórias independentes que apresentam a mesma distribuição da população.

: Assim, as afirmativas I e II estão corretas, enquanto a afirmativa III está incorreta, pois cada variável Xi
: apresenta a mesma distribuição f(x) da população (sempre).

Gabarito: B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, estudaremos a distribuição dos estimadores mais utilizados, quais sejam, a média,
a proporção e a variância amostrais.
Distribuição Amostrai da Média

Para estimarmos a média da população p, utilizamos como estimador a média amostrai X.

Sendo ...,Xn os valores observados da amostra, a média amostrai é a razão entre a soma dos valores observados, XT + X₂ H 1- Xn, e o número de elementos observados, n:
X = x1+x2+-+xn n
Assim como os demais estimadores, a média amostrai é uma variável aleatória, uma vez que X varia de acordo com os valores observados da amostra X1,X2, ,Xn.
Vamos ao exemplo da moeda lançada 3 vezes. Se o resultado for {0, 0,1}, a média amostrai será:

_ 0+0+1 1

% = = 5S0'33

Se o resultado for {0,1,1}, por exemplo, a média amostrai será:

0+1+1 2

% = = 5S0'67

E qual seria a esperança desse estimador? Bem, sabendo que as faces possíveis são 0 e 1, cada uma com 50%de chance, esperamos que as médias desse experimento estejam em torno de 0,5.

Ou seja, a esperança da média amostrai é igual à média populacional?

= n

E quanto à variância? A variância da média amostrai é dada por:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para o exemplo dos 3 lançamentos da moeda, em que V(X) = 0,25 e n = 3, a variância da média amostrai é:
A variância da média amostrai é menor do que a variância populacional V(X).

ESCLARECENDO!

Isso ocorre porque a média das observações X tende a ser um valor bem mais próximo da média populacional do que as observações individuais da amostra Xt. Afinal, no cálculo da média amostrai, os valores acima da média compensam os valores abaixo da média.
Em outras palavras, as médias amostrais X variam menos do que as observações individuais X,. Lembrando que as observações individuais da amostra seguem a mesma distribuição da população, então concluímos que a variância da média amostrai 7(X) é menor do que a variância da população V(X).
Além disso, quanto maior o tamanho da amostra n, menor será a variância da média amostrai.

O desvio padrão (raiz quadrada da variância) de um estimador pode ser chamado de erro padrão.

O erro padrão (ou desvio padrão) da média amostrai é dado por:

FP(X) = =

Ou seja, o erro padrão (ou desvio padrão) da média amostrai pode ser calculado como a raiz quadrada da variância da média amostrai y/vÇX'), ou como a razão entre o desvio padrão populacional e a raiz do número de elementos da amostra
Vn

Também podemos denotar o erro padrão (ou desvio padrão) da média amostrai por <7y.

Para o nosso exemplo, o erro padrão da média amostrai pode ser calculado como:

FP(X) = JvÕÕ =

0,25

T"

0,29

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

INDO MAIS

FUNDO!

As fórmulas da esperança e variância podem ser obtidas pelas respectivas propriedades.

Sendo X = Xl+Xz+ +%n, a esperança E(X) é dada por:

£(%) =E ^i+x2+ -+xn^ = E^ + E

+ - + £(v)

E(X)=if(X1)+Í£'(X2) + - + Í£(Xn)

Vimos que a esperança amostrai é igual à esperança populacional, E(Xt) = EÇX') =

E(X) — - u + - u + —F-u = nx-x u. = u n n n n
Considerando que as variáveis X₁,X₂, —>Xn são independentes, a variância V(X) é:

vm = v (x-+x;+-+x") = v g) + v g) + - + v (J)

7(X) = ^V(X±) +^V(X2) + + ±V(Xn)

Sabendo que a variância amostrai é igual à variância populacional, V(Xj) = 7(X) = cr2:
2.

F(X) =

nz nz nz

= nx4xo2=- n

A variância dos elementos da amostra X, é igual à variância populacional V(Xt) = cr2. O

- a2

que é diferente é a variância da média amostrai, V(X~) =

Se a variância da população não for conhecida, ela precisa ser estimada a partir da amostra (variância amostrai):
₇ = SC^-x)2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nessa situação, a estimativa para a variância da média amostrai será:

s

VW = - n

(CESPE/2016 - TCE/PA) Uma amostra aleatória, com n = 16 observações independentes e identicamente distribuídas (IID), foi obtida a partir de uma população infinita, com média e desvio padrão desconhecidos e distribuição normal. Tendo essa informação como referência inicial, julgue o seguinte item.
Para essa amostra aleatória simples, o valor esperado da média amostrai é igual à média populacional.
Comentários:

De fato, o valor esperado da média amostrai (para uma amostra aleatória) é igual à média populacional.Gabarito: Certo.

(2019 - UEPA) Considere uma amostra aleatória X₁,X₂,...,Xn de uma população normal de média /z e
XX X

variância a2 = 9. Então, a média e a variância de Xn = 11 n, são, respectivamente,

a ue\ 3-

n b) . \ M-e9-
n n x 9
c) "e?

.V n d) Me-.
Comentários:

A média (ou esperança) e a variância da média amostrai são, respectivamente:

F(X) = M

V(X) 9y(X) = =

n n

Gabarito: C.

(VUNESP/2015 -TJ-SP) Resultados de uma pesquisa declaram que o desvio padrão da média amostrai é 32.Sabendo que o desvio padrão populacional é 192, então o tamanho da amostra que foi utilizada no estudo foi a) 6.
b) 25.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) 36.

Comentários:

: O desvio padrão (ou erro padrão) da média amostrai pode ser calculado como a razão entre o desvio padrão j da população e a raiz do número de elementos da amostra:
<7

i = ~j=
í

: O enunciado informa que o desvio padrão da média amostrai é <7^ = 32 e o desvio padrão populacional é j
: cr = 192. Logo:

32= —

Vn

I

I

V" = 3T = 6

n = (6)2 = 36

Gabarito: C.

(FCC/2012-TRE-SP) Uma variável aleatória U tem distribuição uniforme contínua no intervalo [a, 3a]. Sabe-se que U tem média 12. Uma amostra aleatória simples de tamanho n, com reposição, é selecionada da distribuição de U e sabe-se que a variância da média dessa amostra é 0,1. Nessas condições, o valor de n é a) 80.
b) 100.

c) 120.

d) 140.

e) 150.

Comentários:

O que essa questão exige, em relação à matéria que acabamos de estudar, é a fórmula do desvio padrão da média amostrai:
<7

°x — I—

Assim, podemos escrever o tamanho amostrai como:

°x

Ou seja, o tamanho amostrai é a razão entre a variância populacional cr2
(quadrado do desvio padrão populacional cr) e a variância da média amostrai crj (quadrado do desvio padrão da média amostrai ox\
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado informa que a variância da média amostrai é crf = 0,1.

Pronto! A matéria desta aula acabou. Agora, para calcular a variância populacional,
precisamos saber calcular a média e a variância da distribuição contínua uniforme.
A média (esperança) dessa distribuição é igual à média aritmética dos limites do intervalo, a e b. Sabendo que a = a, b = 3.a e E(X) = 12, conforme dados do enunciado, temos:
z x a + b
EW = —

12=- = - = 2a a + 3a 4a a = 6Ou seja, a = 6 e b = 3x6 = 18. Então, a variância é dada por:

z x (b-a)2 (18-6)2 (12)2
y(X) = = -—= ₁₂

12 12 12

Voltando à nossa fórmula para encontrar o tamanho amostrai, temos:

a2 12

n = —= —= Í2°

0,1

Gabarito: C

Fator de Correção para População Finita

Os resultados da variância e do desvio padrão da média amostrai são válidos para variáveis Ài,X₂, ...,Xn independentes, ou seja, quando a população é infinita ou quando as amostras são extraídas com reposição.
Quando isso não ocorre, ou seja, quando a população é finita e as amostras são extraídas sem reposição,
precisamos fazer um ajuste.

Sendo n o tamanho da amostra e N o tamanho da população, precisamos multiplicar a variância da média amostrai, pelo fator de correção de população finita
Af—n

N-n

N—l

Observe que o fator de correção é menor do que 1, pois N — n < N - 1. Assim, o ajuste diminui a variância da média amostrai.
Sabendo que o erro (ou desvio) padrão é a raiz quadrada da variância, podemos ajustá-lo para populações finitas e amostras extraídas sem reposição, multiplicando-o pela raiz quadrada do fator de correção:
la2 N -- n xAz n N--1
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Distribuição da Média Amostrai e a Curva Normal

Quando a população segue distribuição normal (ou gaussiana) com variância conhecida, a média amostrai também seguirá distribuição normal.
Como vimos anteriormente, a esperança, a variância e o desvio (ou erro) padrão da média amostrai são:
F(X) = M

cr2

VW = — n

EPW =

y/n

Assim, para calcular as probabilidades envolvendo a média amostrai, nessa situação,
utilizamos a seguinte transformação para a normal padrão:
x — fl

Z = ^T~

\!n

Por exemplo, vamos supor uma população com média /z = 20 e desvio padrão cr = 2.
Para calcular a probabilidade de a média de uma amostra de tamanho n = 16 ser maior que x = 21, fazemos:
21-20 1

Z = 2 = 7 = 2

VTó 4

Assim, a probabilidade P(X > 21) é igual à probabilidade P(Z > 2), que pode ser obtida a partir da tabela normal padrão.
De modo equivalente, podemos dizer que a seguinte variável segue distribuição normal padrão (ou reduzida), isto é, com média igual a 0 e desvio padrão igual a 1, que representamos como N(0,l):
Z =

y/n

Ainda que a população não siga distribuição normal com variância conhecida, pelo Teorema Central do

Limite, é possível aproximar a distribuição da média amostrai a uma normal, também com média £(X) = [i,
^.2 (J

variância V(X) = — e desvio padrão (ou erro padrão) EP(X) = -?=, quando o tamanho da amostra n for grande o bastante.
A possibilidade de tal aproximação depende do tamanho da amostra e da distribuição da população.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Quanto maior o tamanho da amostra e quanto mais simétrica for a distribuição da população, melhor será a aproximação. Usualmente, considera-se que para uma amostra grande, com n > 30, a aproximação será satisfatória, para qualquer distribuição populacional.
HORAM

r....... ... ......... ......... . ...........

(CESPE/2014 - ANATEL) Com base no teorema limite central, julgue o item abaixo.

Sendo uma amostra aleatória simples retirada de uma distribuição X com média p. e variância 1, a distribuição da média amostrai dessa amostra, X, converge para uma distribuição normal de média np e variância 1, à medida que n aumenta.
Comentários:

A distribuição da média amostrai X converge para uma distribuição normal à medida que n aumenta. Porém,a média dessa distribuição é E(X) = p e variância V(X) = Sabendo que 7(X) = 1, a variância da média amostrai é V(X) = - (e não 1).
n

Gabarito: Errado.

(CESPE 2018/PF) O tempo gasto (em dias) na preparação para determinada operação policial é uma variável aleatória X que segue distribuição normal com média M, desconhecida, e desvio padrão igual a 3 dias. Aobservação de uma amostra aleatória de 100 outras operações policiais semelhantes a essa produziu uma média amostrai igual a 10 dias. Com referência a essas informações, julgue o item que se segue, sabendo queP(Z > 2) = 0,025, em que Z denota uma variável aleatória normal padrão.
O erro padrão da média amostrai foi inferior a 0,5 dia.

Comentários:

O erro padrão da média amostrai é:

£P(X) =

Xn

Em que n é o tamanho da amostra (n

Gabarito: Certo.

= 100); e cr é o desvio padrão amostrai (cr = 3), logo:
3 3

EP(X} = -= = — = 0,3

VTÕÕ 10

(CESPE/2019 - Analista Judiciário TJ) Um pesquisador deseja comparar a diferença entre as médias de duas amostras independentes oriundas de uma ou duas populações gaussianas.Considerando essa situação hipotética, julgue o próximo item.
Para que a referida comparação seja efetuada, é necessário que ambas as amostras tenham N > 30.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

: Comentários:

: Quando a população segue uma distribuição normal (ou gaussiana), a média amostrai também seguirá uma ;
: distribuição normal, independentemente do tamanho da amostra. Logo, o item está errado.

= Para fins de complementação, se a amostra for grande o suficiente (normalmente,
consideramos isso para ;

= n > 30), a média amostrai seguirá aproximadamente uma distribuição normal, mesmo que a população não j
= siga distribuição normal.
j Gabarito: Errado.

= (FCC 2015/SEFAZ-PI) Instrução: Para responder à questão utilize, dentre as informações dadas a seguir, as ;
; que julgar apropriadas. Se Z tem distribuição normal padrão, então:

í P(Z < 0,4) = 0,655; P(Z < 1,2) = 0,885; P(Z < 1,6) = 0,945; P(Z < 1,8) = 0,964; P(Z < 2) = 0,977.

= Uma auditoria feita em uma grande empresa considerou uma amostra aleatória de 64
contas a receber. Se ;

: a população de onde essa amostra provém é infinita e tem distribuição normal com desvio padrão igual a R$ j
= 200,00 e média igual a R$ 950,00, a probabilidade da variável aleatória média amostrai, usualmente ;
; denotada por X, estar situada entre R$ 980,00 e R$ 1.000,00 é dada por
;

: a) 18,47o b) 9,27o j c) 28,57o d)47,77o í e) 86,27o
; Comentários:

: O enunciado informa que a população segue distribuição normal, logo, a média amostrai também terá =
: distribuição normal. Assim, utilizamos a seguinte transformação para a normal padrão:

í X-ii i i = —ÕJí íVn í

: Sabemos que o tamanho da amostra é n = 64, logo, Vn = 8; que a média populacional é jU = 950 e que o :
: desvio padrão populacional é cr = 200. Substituindo esses valores, a transformação para Xinf =
980 é:

980 -950 8 6

í _ 2ÕÕ " 30 X 2ÕÕ" 5 _ 1,2

Í

í 8
í

: Para Xsup = 1000, temos:
j

1000 - 950 8

í Z* ~ 2ÕÕ _ 50 X 2ÕÕ_ 2

j i 8í

= Ou seja, a probabilidade desejada corresponde a P(l,2 < Z < 2), que pode ser calculada pelos dados =
= fornecidos no enunciado:

P(l,2 < Z < 2) = P(Z < 2) - P(Z < 1,2) = 0,977 - 0,885 = 0,092 = 9,2%

: Gabarito: B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Distribuição Amostrai da Proporção

Agora, vamos trabalhar com uma população em que determinada característica está presente em uma proporção p dessa população, por exemplo, 15% da população apresenta olhos azuis; 20%da população está doente, 1% da produção apresenta defeito, etc.
Um elemento qualquer da população X pode apresentar a característica estudada,
o que chamamos de sucesso (X = 1), ou não, o que chamamos de fracasso (X = 0). A probabilidade de sucesso é p e a probabilidade de fracasso é q = 1 — p.
Essa população apresenta uma distribuição de Bernoulli, com parâmetro p.

Sendo essa proporção populacional desconhecida, precisamos estimá-la a partir da proporção de sucessos encontrados na amostra, que indicamos por p.
Considerando que cada observação Xt da amostra será Xt = 0 ou Xt = 1 (assim como para a população),então a proporção de sucessos na amostra pode ser calculada como:

x1+x2+-+xn n
Vamos supor que queremos estimar a proporção de defeitos em uma produção de medicamentos. Para isso,extraímos uma amostra de 10 medicamentos, que apresentou o seguinte resultado, em que
0 representa um item não defeituoso e 1 representa um item defeituoso:
{0, 0, 1, 0, 0, 0,1, 0, 0, 0}

Logo, a proporção encontrada nessa amostra é:

0 + 0 + 1 + 0 + 0 + 0 + 1 + 0 + 0 + 0 2

Note que o estimador p é calculado da mesma forma que a média amostra X que vimos anteriormente.Logo, a esperança de p é calculada da mesma forma que para X, utilizando p no lugar de //:

F(p) = p

Ou seja, a esperança do estimador é igual à proporção populacional.

Em outras palavras, a proporção amostrai tende à proporção populacional.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A variância de p também é calculada de forma análoga à de X:

Sabendo que a população segue distribuição de Bernoulli, temos 7(p) = p. q, então:

E o erro padrão (ou desvio padrão) para p, raiz quadrada da sua variância é dado por:

Se a proporção populacional p for desconhecida, utilizamos a proporção amostrai p para estimar a variância populacional.
A estimativa da variância populacional é dada por:

7(p) = p.q

Em que q = 1 - p. E a estimativa da variância do estimador p é:

Para o nosso exemplo, em que encontramos p = 0,2 (logo, q = 1 — p = 0,8). A
estimativa da variância da proporção populacional é:
y(p) = p.q = 0,2 x 0,8 = 0,16

E a estimativa da variância da proporção amostrai é:

z x p.q 0,2 x 0,8

V(p) = í-1 = ——— = 0,016

n 10

Logo, a estimativa para o erro padrão (ou desvio padrão) da proporção amostrai é:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considerando que cada elemento da população segue distribuição de Bernoulli,
então o número de elementos com o atributo sucesso encontrados em uma amostra de tamanho n segue uma distribuição binomial, com parâmetros n e p. Para o nosso exemplo, temos uma distribuição binomial com n = 10 e proporção estimada p = 0,2.
Porém, também é possível aproximar, pelo Teorema Central do Limite, a distribuição da proporção amostrai
T) (] I T) O

a uma normal, com média £(p) = p, variância 7(p) = desvio (ou erro)
padrão FP(p) = I—, quando o tamanho da amostra n for suficientemente grande.
Assim, para calcular as probabilidades envolvendo a proporção amostrai, utilizamos a transformação para a normal padrão:
p — p

Por exemplo, supondo que a proporção de sucesso de uma população seja p = 0,5 (e proporção de fracasso q = 1 — p = 0,5), vamos calcular a probabilidade de observar uma proporção maior que p = 0,6 em uma amostra de tamanho n = 25:
0,6- 0,5 0,1 0,1

Z |0,5 x 0,5 0,1 1

\ 25 5

Assim, a probabilidade P(p > 0,6) é aproximadamente igual à probabilidade P(Z
> 1), que pode ser calculada pela tabela da normal padrão.
Se a população for finita e a amostra for extraída sem reposição, será necessário aplicar o fator de correção para população finita, multiplicando a variância da proporção amostrai por
N — n

N — 1

E o erro (ou desvio) padrão do estimador, com a correção para população finita, é igual à raiz quadrada:
£P(p) =

N — TL
N — 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

r"...............................................................

(CESPE 2016/TCE-PA) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as com CNPJ irregular foram representadas por 0.
Considerando que a amostra {0, 1, 1, 0, 0,1, 0,1, 0, 1,1, 0, 0,1,1, 0,1,1,1, 1} foi extraída para realizar um teste de hipóteses, julgue o item subsequente.
A estimativa pontual da proporção de empresas da amostra com CNPJ regular é superior a 50%.

Comentários:

O estimador da proporção p pode ser calculado pela soma dos valores dos elementos,
dividida pelo número de elementos na amostra:
A X1+X2 + - + Xn p =
n

0+1+1+0+0+1+0+1+0+1+1+0+0+1+1+0+1+1+1+1 12

P " 20
_ 2Õ

Logo, a proporção é de 60%.

Gabarito: Certo

(CESPE/2019 - TJ-AM) Para estimar a proporção de menores infratores reincidentes em determinado município, foi realizado um levantamento estatístico. Da população-alvo desse estudo, constituída por
Item. 10.050 menores infratores, foi retirada uma amostra aleatória simples sem reposição, composta por 201indivíduos. Nessa amostra foram encontrados 67 reincidentes. Com relação a essa situação hipotética, julgue o seguinte item.
A estimativa do erro padrão da proporção amostrai foi inferior a 0,04.

Comentários:

O erro padrão da proporção é dada pela relação:

EP™ =

A questão nos diz que a amostra é composta por 201 indivíduos, sendo 67 deles reincidentes. Assim, temos
67 1 2

n = 201 e p = ~ = " Logo, Q — 1 — P — Logo, o erro padrão é:

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Estimador para a media: X =--------------------

n

Esperança: E(X) = //; Variância: V(X) =

Estimador para a proporção: p = %1+Ã2+ +Xn

Esperança: £(p) = p; Variância: 7(p) =

Distribuição Amostrai da Variância

Quando a variância da população é desconhecida, precisamos estimá-la a partir da amostra, assim como fizemos com a média e a proporção.
O estimador da variância que utilizamos para uma amostra de tamanho n é:

n-1

Utilizamos esse estimador, com a divisão por n — 1, porque a sua esperança é igual à variância populacional,como veremos posteriormente, o que não ocorre com o estimador com a divisão por n.

EXEMPLIFICANDO

Vamos supor que a variância da altura de determinado grupo de adultos seja desconhecida,assim como a sua média. Para estimar esses parâmetros, obtemos a seguinte amostra de
5 pessoas:

{1,65; 1,75; 1,8; 1,85; 1,95}

Primeiro, precisamos calcular a média da amostra:

1,65 + 1,75+1,8+1,85+1,95 9 .Á — — — —
1.0

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Agora, calculamos o estimador da variância, somando os desvios em relação à média,
elevados ao quadrado, e dividindo o somatório por n — 1:

2 _ S(xf-x)2

n-1

2 (l,65-1,8)2 + (l,75-1,8)2+(l,8-1,8)2 + (l,85-1,8)2+(l,95-1,8)2

(—O,15)2 + (—O,O5)2 + (O)2+(O,O5)2 + (O,15)2

0,0225+0,0025+0,0025+0,0225 0,05 Q|25

4 4 '

INDO MAIS

FUNDO!

Uma maneira alternativa de calcular a variância populacional é:

cr2 = E(X2) - [£(X)]2

Para a variância amostrai, também podemos utilizar uma fórmula similar a essa, mas com as devidas adaptações. No lugar de EÇX), utilizamos a média amostrai X; e, no lugar deE(X2), utilizamos X2, que é a média dos valores elevados ao quadrado:

n

Para o exemplo anterior, teríamos:

yy _ (l,65)2 + (l,75)2 + (l,8)2+(l,85)2+(l,95)2 _

= 16,25 - 3,25

Por fim, fazemos um ajuste. Para calcular a variância populacional, dividimos por n e para a variância amostrai, dividimos por n — 1.
Logo, precisamos multiplicar o resultado por para obter a variância amostrai:

S2 = [X2 _ (X)2] x

Para o nosso exemplo, em que X2 = 3,25, X = 1,8 e n = 5, a variância amostrai pode ser calculada como:
s2 = [3,25 - (1,8)2] x | = [3,25 - 3,24] x | = = 0,0125

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para a variância amostrai, a sua esperança é igual à variância populacional,
analogamente ao que ocorreu com os demais estimadores. A sua variância e erro padrão são dados por:
Se a variância populacional cr2 for desconhecida, utilizamos, no lugar de cr2, a própria estimativa s2 para estimar a média F(s2), a variância 7(s2) e o erro padrão EPÇs2).
Para o nosso exemplo, em que calculamos s2 = 0,0125, para a amostra com n = 5
observações, o erro padrão de s2 pode ser estimado como:
FP(s2)

Se a população seguir uma distribuição normal, então o estimador s2, multiplicado pelo fator ^-=-, segue uma distribuição qui-quadrado com n — 1 graus de liberdade:
Em outras palavras, 0 estimador s2 é uma variável com distribuição qui-quadrado, com n — 1 graus de liberdade, multiplicada por^—<
Vamos supor que, para uma população normal, a variância populacional seja cr2 = 1, e que vamos extrair amostras de tamanho n = 5. Nesse caso, a variância amostrai s2 terá a seguinte distribuição:
Ou seja, a variância amostrai seguirá uma distribuição qui-quadrado com n— 1
= 4 graus de liberdade,
dividida por 4.

A seguir, consta a tabela da distribuição qui-quadrado com 4 graus de liberdade, que apresenta os valores de probabilidade P(X2 <x) e os respectivos valores de x. Como a variância amostrai segue essa distribuição, dividida por 4, criamos uma terceira coluna, dividindo os valores de x por 4.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

P(X42 < x)

X
X/A:

0,005

0,21

0,05

0,01

0,30

0,07

0,025

0,48

0,12

0,05

0,71

0,18

0,1

1,06

0,27

0,25

1,92

0,48

0,5

3,36

0,84

0,75

5,39

1,35

0,9

7,78

1,94

0,95

9,49

2,37

0,975

11,14

2,79

0,99

13,28

3,32

0,995

14,86

3,72

Por exemplo, a probabilidade de a variância amostrai observada ser inferior a 0,48 é:

P(s2 < 0,48) = 0,25

A partir desse resultado, podemos calcular a esperança e a variância do estimador. A

esperança é dada por:

F[s2] =E[(^I).X2_1] =

Considerando que a média de uma distribuição qui-quadrado com k graus de liberdade é igual a k, então fazendo k = n - 1, temos:
F[X2_J = k = n-l

Substituindo no resultado anterior, temos:

^[s2] = =

Esse é o resultado que vimos no início da seção. A variância do estimador é:

Considerando que a variância de uma distribuição qui-quadrado com k graus de liberdade é igual a 2k, então fazendo k = n — 1, temos:
7[X2_J = 2.fc = 2.(n-l)

Substituindo no resultado anterior, temos:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vale acrescentar que uma população normal depende dos dois parâmetros, variância e média, os quais são independentes. Consequentemente, os estimadores correspondentes também serão independentes.
I«** IX

(FGV/2016 - IBGE) Suponha que uma amostra de tamanho n = 5 é extraída de uma população normal, com média desconhecida, obtendo as seguintes observações:
Xi=3,X2=5,X3 = 6, X4=9eXs=12

São dados ainda os seguintes valores, retirados da tabela da distribuição qui-quadrado:

. P(/2 < 5) = 0,713

. P(xl < 12,5) = 0,986

* P(Zs > 5) = 0,854

. P(xl > 12,5) = 0,971

Se a população tem variância verdadeira a2 = 4, em nova amostra (n = 5), a probabilidade de se observar uma variância amostrai maior do que a anterior é de:
a) 0,014

b) 0,029

c) 0,146

d) 0,287

e) 0,713

Comentários:

Para resolver essa questão, vamos primeiro calcular a variância amostrai obtida nessa primeira amostra:
2 M-*)2

S =

Para isso, precisamos da média amostrai:

n — 1

3 + 5 + 6 + 9 + 12 35

X ~ 5 " T " 7

Agora, podemos calcular a variância dessa primeira amostra:

, (3 - 7)2 + (5 - 7)2 + (6 - 7)2 + (9 - 7)2 + (12 - 7)2

Sl _ 4

, (—4)2 + (—2)2 + (-1)2 + (2)2 + (5)2 16 + 4 + 1 + 4 +
25 50

si = ; =
; = -r = 12,5

4 4 4

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= Para calcular a probabilidade de a variância amostrai ser s2 > 12,5, consideramos que esse estimador segue =
: uma distribuição qui-quadrado com n - 1 graus de liberdade, multiplicada por
=

I
I

: Sabendo que a variância populacional é cr2 = 4 e que o tamanho da amostra é n = 5, então:
;

s2 = (5êi)-x5-i = x2

= Portanto, a variância amostrai segue a mesma distribuição de X₄. A probabilidade de s2 > 12,5 é,
portanto: i

P(s2 > 12,5) = P(X42 > 12,5)

= O enunciado informa que P(X₄ < 12,5) = 0,986. A probabilidade P(X₄ > 12,5) é complementar:

P(X42 > 12,5) = 1 - P(X42 < 12,5) = 1 - 0,986 = 0,014

j Gabarito: A

Distribuições para Amostragem Estratificada

Para uma amostragem estratificada, com k estratos, a média amostrai será calculada como:

Í = 1

Nessa expressão, Nj é 0 tamanho década estrato; Né 0 tamanho total da população; exL, a média amostrai observada para cada estrato. Ou seja, calculamos a média xj para cada estrato i, multiplicamos pelo tamanho do estrato Nt e dividimos pelo tamanho total N.
Para ilustrar, vamos supor uma população dividida em 3 estratos, com os seguintes tamanhos Ni e os seguintes valores de média amostrai xj para cada estrato i:
Estrato Ni

1 50

2 30

3 20

rii xt

5 2

3 3

2 4

A média amostrai para toda a população corresponde às médias amostrais dos estratos,
ponderadas pelos respectivos tamanhos dos estratos:
— 50 x 2 + 30 x 3 + 20 x 4

X = 50 + 30 + 20

100 + 90 + 80

1ÕÕ

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A razão entre o tamanho do estrato e o tamanho total da população N pode ser chamada de peso do estrato (W[). Nessa situação, para calcular a média amostrai, basta multiplicar a média de cada estrato pelo respectivo peso e somar todos os resultados:
k x = ^Wixxl i=l
Podemos calcular, ainda, a variância da média amostrai:

Pelas propriedades da variância, temos:

=È Gf

Em que a variância da média amostrai de cada estrato V(X) é calculada pela razão entre a variância populacional do estrato e o tamanho da amostra do estrato:
VtxJ

nt

Em uma amostragem proporcional, o tamanho amostrai do estrato pode ser calculado pela razão entre o tamanho do estrato populacional e o tamanho total da população,multiplicada pelo tamanho total da amostra:

AQ

Hj = —.n

1 N

Vamos supor as seguintes variâncias para os estratos da população, que vimos anteriormente:

Estrato Ni nj

1 50 5 4

2 30 3 2

3 20 2 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

As variâncias das médias amostrais dos estratos são dadas por:

V(%T) = ^ = 5 = 0,8

Ui

V(x£ =

n2

5=0,5

«3

E a variância da média amostrai global é dada por:

V(X) =

Z-A f50Ã2

=(iõõ) x0'8+

k i=l x 0,67 +
/ 20 \2

K1ÕÕ7 X °'5 = °'25 X °'8 + 0,09 X °'67 + 0,04 X °'5 = °'28

A variância da média de uma amostra estratificada proporcional é menor ou igual do que a variância da média de uma amostra aleatória simples (AAS). Afinal, a amostragem estratificada proporcional é mais precisa do que a AAS1.
1A variância da média de uma AAS é a razão entre a variância da população como um todo e 0 tamanho da amostra; e a variância de toda a população é maior (ou igual) às variâncias dos estratos ponderadas pelos respectivos tamanhos:
v^AAS) = -x vm > - x v k i=l
A expressão à direita corresponde justamente à variância da média amostrai global em uma amostragem estratificada proporcional. Sabendo que V(XFst) = Y>í=i (^) que y(X) = e que, na alocação proporcional, = ^-.n, então:
VÇXEP)

i=l

VÜQ.N

Ni.n

Nj VÜQ

N n

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sendo a variância populacional de cada estrato desconhecida, precisamos estimá-la a partir da variância amostrai de cada estrato sjL Substituindo, na fórmula acima, V(X) por s| e V(xi) por temos:
h=l

Em que a estimativa da variância da média amostrai para cada estrato sf., considerando uma amostra de tamanho nL para esse estrato, com a correção para população finita, é dada por:
Vamos supor que as estimativas da variância para cada estrato sejam:

Estrato Ni

1 50

2 30

3 20

rii

Sxi

1,5

Assim, as variâncias das médias amostrais para cada estrato, com o fator de correção, são:

2/'50 - 5^ = 0,367

5* .50 - V

_ x'5 ^30 — 3' ) = 0,466

3 \30 — 1,

'20 — 2^
2* .20 - lJ

E a variância da média amostrai global é dada por:

= 0,474

2 / 30 \

x0'367+(lõõ)

x 0,474

s? = 0,25 x 0,367 + 0,09 x 0,466 + 0,04 x 0,474 = 0,092 + 0,042 + 0,019 = 0,153

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

(CESPE/2018 - STM) Um estudo acerca do tempo (x, em anos) de guarda de autos findos em determinada seção judiciária considerou uma amostragem aleatória estratificada. A população consiste de uma listagem de autos findos, que foi segmentada em quatro estratos, segundo a classe de cada processo (as classes foram estabelecidas por resolução de autoridade judiciária.)
A tabela a seguir mostra os tamanhos populacionais (TV) e amostrais (n), a média amostrai (x) e a variância amostrai dos tempos (s2) correspondentes a cada estrato.
Estratos Tamanhos Populacionais (N) Tamanhos Amostra (n) | rq

A 30.000 300
20 3

B 40.000 400
15 16

C 50.000 500
10 5

D 80.000 800
5 8

Total 200.000 2.000

I

I

: Considerando que o objetivo do estudo seja estimar o tempo médio populacional (em anos) de guarda dos j
= autos findos, julgue os itens a seguir.
;

; (CESPE/2018 - STM) A estimativa do tempo médio populacional da guarda dos autos findos é maior ou igual j
= a 12 anos.
;

: Comentários:

: Em uma amostra aleatória por estratificação, a média amostrai é dada por:
;

Í = 1

Em que k é a quantidade de estratos; Nt o tamanho de cada estrato; e xt a média de cada estrato.
Pelos dados de TV e x fornecidos na tabela, temos:

_ TVyj x Xyi d- TVg x Xg 4" N(j x 4" TVp x xp

30000 x 20 + 40000 x 15 + 50000 x 10 4- 80000 x 5

X ~ 200000

I

Gabarito: Errado.

60 4- 60 4- 50 4- 40

X =

I

10,5

I

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(CESPE/2018 - STM) Combinando-se todos os estratos envolvidos, a estimativa da variância do tempo médio amostrai da guarda dos autos findos é inferior a 0,005 ano2.
Comentários:

Em uma amostragem estratificada, a estimativa da variância da média amostrai é dada por:
k i=l
«A x sf.

nJ

Em que =

4, pVi-nj-

y Pelos valores apresentados na tabela, temos:

S- 3 ( <30000 — 300^

300 1 30000 - 1 /

= 0,0099

S- 16 I

<40000 - 400^

= 0,0396

S- —

400' 1 40000 - 1 /

₅ | <50000 - 500^

500 1k 50000 - 1 7

= 0,0099

I

I

I

: Além disso, temos que:

S%-

₈ | <80000 — 800^

800 1 80000 - 1 /

= 0,0099

(NA\2 ( 30000 \2

(« ) = (zõõõõõ) = °'0225

(Nb\2 ( 40000 \2

( N ) = (zõõõõõ) = °'04

íNc\2 ( 50000 \2

U) = (zõõõõõ) = °'0625

/TVM2 / 80000 \2

U =(2Õõõõõ) =0'16

I

I

: Portanto:

X Sxh h=l s2 = (0,0225 0,0099 + 0,04 * 0,0396 + 0,0625 0,0099 + 0,16 0,0099)
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ESTIMAçÃo INTERVALAR

Após obtermos uma estimativa para o parâmetro populacional desejado (estimação pontual), calculamos um intervalo associado a esse parâmetro. Ou seja, na estimação intervalar (ou estimação por intervalos), a estimativa deixa de ser um ponto (isto é, um valor único) e passa a ser um intervalo. Esse intervalo, chamado intervalo de confiança, fornece uma noção da precisão da estimativa.
O intervalo de confiança é construído em torno da estimativa pontual 9, da forma (O
— E;0 + F), que também pode ser indicado como 0 ± E. Esse intervalo indica que o parâmetro populacional 9 deve estar entre o limite inferior, 9 - E, e o limite superior 9 + E. O valor E corresponde à metade da amplitude do intervalo, podendo ser chamado de margem de erro, erro de precisão, erro máximo.
Como assim o parâmetro "deve" estar no intervalo? É possível que o parâmetro 9 esteja fora desse intervalo?Por se tratar de um intervalo construído em torno de uma variável aleatória, sim! Em
Inferência Estatística,
sempre convivemos com um nível de dúvida. Mas, felizmente, é possível dimensionar esse nível de dúvida.
Assim, atribuímos ao intervalo um nível (ou grau) de confiança 1 — a, indicado em forma percentual, por exemplo, 95%. A interpretação desse nível é a seguinte: repetindo o procedimento para a construção do intervalo muitas vezes, em (1 — <z)% (por exemplo, 95%) dessas vezes, o intervalo construído incluirá o parâmetro populacional.
Ou seja, o nível de confiança é uma probabilidade. Porém, não se trata da probabilidade de o parâmetro populacional pertencer ao intervalo, uma vez que o parâmetro populacional é fixo (embora seja desconhecido). O nível de confiança representa a probabilidade de o intervalo, o qual é construído a partir de variáveis aleatórias, incluir o parâmetro populacional.
Quanto maior o nível de confiança (1 — a), ou seja, quanto maior for a probabilidade de o intervalo incluir o parâmetro populacional, maior será o tamanho do intervalo, se mantivermos as demais características iguais. Logo, maior será a margem de erro (isto é, a semi-amplitude do intervalo).
Se, para isso, a margem de erro não puder aumentar, então teremos que aumentar o tamanho da amostra.Ou seja, para termos uma estimativa mais precisa (com menor margem de erro e/ou com maior nível de confiança), teremos que investigar um número maior de elementos. Veremos as fórmulas dessas relações adiante, mas é importante entender essa lógica por trás delas.
E o valor de a? a, chamado de nível de significância, é o complementar do nível de confiança e corresponde à probabilidade de o intervalo de confiança não englobar o parâmetro populacional.
Nas próximas seções, veremos como construir o intervalo de confiança para os parâmetros populacionais(média, proporção e variância), a partir dos respectivos estimadores.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (CESPE/2019 -TJ/AM) Acerca de métodos usuais de estimação intervalar, julgue o item subsecutivo.
Um i intervalo de confiança de 95% descreve a probabilidade de um parâmetro estar entre dois valores numéricos ;
: na próxima amostra não aleatória a ser coletada.

; Comentários:

: Existem alguns erros neste item. A estimação, de modo geral, trabalha com amostras aleatórias já coletadas, jAlém disso, não se trata da probabilidade de o parâmetro estar entre dois valores, mas sim de os dois valores ;
i englobarem o parâmetro.

; Gabarito: Errado.

; (CESPE/2019 - TJ/AM) Acerca de métodos usuais de estimação intervalar, julgue o item subsecutivo.
É :
possível calcular intervalos de confiança para a estimativa da média de uma distribuição normal, ;

= representativa de uma amostra aleatória.
;

: Comentários:

= De fato, é possível calcular intervalos de confiança para a média, a partir de uma amostra aleatória.
: Gabarito: Certo.

= (FGV/2019 - DPE-RJ - Adaptada) Para a aplicação de técnica de estimação por intervalos, há uma série de j
= requisitos e recomendações. Sobre essas condições, julgue os seguintes.

= I - A amplitude do intervalo varia positivamente com o grau de confiança e o tamanho da amostra.

; II - A ideia da técnica é a da construção de um intervalo ao qual seja possível associar uma probabilidade, j
= justamente aquela de que o parâmetro de interesse esteja nele contido.

: III - É inquestionável que, antes da seleção da amostra, o grau de confiança é a probabilidade de o intervalo j
= teórico conter de fato o verdadeiro valor do parâmetro de interesse.
;

: Comentários:

: Em relação ao item I, quanto maior o nível de confiança, maior será a amplitude do intervalo,
logo essas j

: grandezas, de fato, variam no mesmo sentido. Porém, quanto maior o tamanho da amostra, menor será a j
: amplitude do intervalo. Logo, essas grandezas variam em sentidos opostos e o item I está errado.

: Em relação ao item II, não se trata de uma probabilidade de o parâmetro de interesse (que é fixo)
estar j

= contido no intervalo construído, mas sim de o intervalo construído conter o parâmetro de interesse, logo o ;
: item II está errado.

= Em relação ao item III, o grau de confiança (1 — a), de fato, representa a probabilidade de o intervalo conter ;
: o parâmetro de interesse.
j

: Resposta: Itens I e II Errados; Item III Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Intervalo de Confiança para a Média

Para estimarmos a média populacional, utilizamos a média amostrai como estimador. Porém, para construirmos um intervalo de confiança em torno desse estimador, é necessário saber se a variância populacional é conhecida ou não.
População com Variância Conhecida

Se a população tiver variância conhecida cr2 e distribuição normal (ou se apresentar outra distribuição, mas o tamanho da amostra for suficientemente grande), a média amostrai X terá distribuição normal.
Assim, consideramos a curva normal para construir um intervalo que delimite uma probabilidade de 1 — a em torno de X. Ou seja, devemos encontrar os valores de X que delimitam uma área sob a curva normal,correspondente a 1 - a:

Para encontrar os limites, devemos utilizar a tabela normal padrão e a transformação para a distribuição normal padrão Z (com média 0 e desvio padrão igual a 1):
valor procurado — média da distribuição z =
desvio padrão da distribuição

No caso, os valores procurados são X=X+EeX=X- E; a média da distribuição é X; e o desvio padrão da distribuição é o erro padrão de X:
EP(X) =

\n

Substituindo esses valores na fórmula da transformação, encontramos a expressão do erro:

X + E-X E

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O intervalo de confiança X + E é, portanto:

Esses limites podem ser chamados de valores críticos.

E qual é o valor de z? Depende do nível de confiança.

Por exemplo, suponha um nível de confiança de 95%. Para que toda a região delimitada pelo intervalo X + Edelimite uma área de 1 — a = 95%, então a área entre a média X e o limite superior X ± E deve ser a metade (47,5%). Considerando a transformação para a normal padrão, temos P(0 < Z < z) = 0,475.
z 0,05 0,06 0,07

1,8

1,9

0,4678 0,4686 0,4693

0,4744 0,475 0,4756

0,4798 0,4803 0,4808

Pela tabela da normal padrão, temos z = 1,96. Assim, se o nível de confiança for de 95%, o intervalo será:
X ± 1,96.-7=

Agora podemos entender melhor o raciocínio que vimos no início desta seção: quanto maior o nível de confiança (maior valor de z), maior será a margem de erro E = z.-^= e,consequentemente, maior o tamanho do intervalo X ± E, mantendo as demais características constantes.
E quanto maior o tamanho da amostra n, menor será a margem de erro E = z.-^= e,
consequentemente,

Vn menor o tamanho do intervalo X ± E, mantendo as demais características constantes.
Além disso, quanto maior a variabilidade da população (maior desvio padrão cr), maior será a margem de erro E = z.-^= e, consequentemente, maior o tamanho do intervalo X + E,mantendo as demais características constantes.
Para exemplificar, vamos supor uma população com média desconhecida e variância igual cr2 = 9 (portanto,desvio padrão cr = Võ2 = V9 = 3), sendo extraída uma amostra de 36 indivíduos.
Considerando um nível de 1 — a = 95% de confiança (em que z = 1,96), a margem de erro é dada por:
0-3 3 1,96

E = 1,96.-= = 1,96.-= = 1,96.- = —- = 0,98

Vn V36 6 2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Supondo que a média amostrai tenha sidoX = 10, o intervalo de confiança é:

X + E = 10 + 0,98 = 10,98

X - E = 10 - 0,98 = 9,02

(9,02; 10,98)

A probabilidade associada aos valores não incluídos no intervalo de confiança é complementar (igual a a).
Por se tratar de uma distribuição simétrica, a probabilidade associada aos valores superiores ao intervalo é aI2 e aos valores inferiores é também a
₇₂ / 1_ ₐ 72

X — E x X+E

Por isso, é comum utilizar a notação zay para indicar 0 limite do intervalo na distribuição normal padrão (no nosso exemplo, temos za^ = 1,96).
Tamanho Amostrai

A questão pode fornecer, além do nível de confiança (1 — a), 0 valor do erro máximo tolerado (E) e indague a respeito do tamanho necessário da amostra n. Para isso, podemos utilizar a mesma fórmula do erro que vimos há pouco:
(7

E = z —

Vn

Reorganizando essa fórmula, temos:

Podemos observar que, quanto maior 0 nível de confiança desejado (z), maior será 0
tamanho amostrai; e quanto maior 0 erro máximo (E), menor será 0 tamanho amostrai.
Pontue-se que 0 erro máximo também pode ser chamado de distância máxima (ou diferença máxima) entre a estimativa e 0 parâmetro populacional com probabilidade 1 - a.
Ademais, em vez de fornecer 0 erro máximo, a questão pode fornecer a amplitude do intervalo de confiança,que corresponde ao dobro do erro máximo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

No exemplo que vimos anteriormente, obtivemos uma margem de erro de E = 0,98, com uma amostra de n = 36. Vamos supor que o erro máximo tolerável seja a metade, ou seja, E = 0,49.Considerando que os demais valores permaneçam constantes, ou seja, z = 1,96 e cr = 3, o tamanho da nova amostra n₂,necessário para obter a margem de erro desejada é:

=(4)Mw6Xõ^9

= (4 x 3)2 = (12)2 = 144

Note que o tamanho da amostra quadruplicou para que a margem de erro fosse reduzida à metade,
mantendo o nível de confiança, para a mesma população (portanto, o mesmo desvio padrão).

Na verdade, poderíamos verificar que isso aconteceria, sem conhecer os dados do problema. Vejamos: a amostra inicial é dada por:
=(4)2

E a nova amostra necessária para que o erro se reduza à metade é:

n2 = = 4.

1 r 1

íll

Pontue-se que tais fórmulas pressupõem uma população infinita ou amostras extraídas com reposição. Caso a população seja finita e as amostras extraídas sem reposição, será necessário aplicar o fator de correção para população finita.
|n-h

Para isso, devemos multiplicar a fórmula do erro pelo fator

\ N-l'

o que influencia no tamanho da amostra:

a |N — n

HORAtX

í (CESPE 2020/TJ-PA) Uma equipe de engenheiros da qualidade, com vistas a estimar vida útil de determinado i
: equipamento, utilizou uma amostra contendo 225 unidades e obteve uma média de 1.200
horas de duração, j

= com desvio padrão de 150 horas.

: Considerando-se, para um nível de confiança de 95%, z = 1,96, é correto afirmar que a verdadeira duração j
= média do equipamento, em horas, estará em um intervalo entre
;

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) 1.190,00 e 1.210,00.

b) 1.185,20 e 1.214,80.

c) 1.177,50 e 1.222,50.

d) 1.180,40 e 1.219,60.

e) 1.174,20 e 1.225,80.

Comentários:

Vamos listar as informações do enunciado:

* Média amostrai: X = 1.200

* Nível de confiança: z = 1,96

* Desvio padrão da população: cr = 150

* Tamanho da amostra: n = 225

Agora, substituímos esses dados na fórmula do intervalo de confiança para a média:

cr

X±?x —

Vn

1200 ± 1,96 x-=

V225

1200 ± 1,96 x —

1200 ± 1,96 x 10

1200 ± 19,6

Logo, o intervalo é (1200 - 19,6 = 1180,4; 1200 + 19,6 = 1219,6)

Gabarito: D.

(FGV/2022 - TJDFT) Uma grande amostra foi selecionada para estimar o tempo médio de tramitação de um tipo particular de ação em uma comarca. Essa amostra demonstrou que o intervalo bilateral de 95% de confiança para o tempo médio de tramitação estava entre 8 e 10 anos.
Com o objetivo de aumentar a precisão dessa estimativa, um estatístico resolveu diminuir a confiança para85%. O novo intervalo de confiança passou a ser, aproximadamente, igual a:

a) 9 ± 0,26

b) 9 ± 0,34

c) 9 ± 0,72

d) 9 ± 0,88

e) 9 ± 1,44

Nessa prova, foi fornecida a tabela normal padrão da forma P(Z > Zo), parcialmente replicada a seguir.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Zo

1,00

1,10

1,20

1,30

1,40

1,50

1,60

1,70

1,80

1,90

2,00

Segunda decimal de Zo

0,00 0,01 0,02 0,03 0,04 0,05
0,06 0,07 0,08 0,09

0,1587 0,1562 0,1539 0,1515 0,1492 0,1469
0,1446 0,1423 0,1401 0,1379

0,1357 0,1335 0,1314 0,1292 0,1271 0,1251
0,1230 0,1210 0,1190 0,1170

0,1151 0,1131 0,1112 0,1093 0,1075 0,1056
0,1038 0,1020 0,1003 0,0985

0,0968 0,0951 0,0934 0,0918 0,0901 0,0885
0,0869 0,0853 0,0838 0,0823

0,0808 0,0793 0,0778 0,0764 0,0749 0,0735
0,0721 0,0708 0,0694 0,0681

0,0668 0,0655 0,0643 0,0630 0,0618 0,0606
0,0594 0,0582 0,0571 0,0559

0,0548 0,0537 0,0526 0,0516 0,0505 0,0495
0,0485 0,0475 0,0465 0,0455

0,0446 0,0436 0,0427 0,0418 0,0409 0,0401
0,0392 0,0384 0,0375 0,0367

0,0359 0,0351 0,0344 0,0336 0,0329 0,0322
0,0314 0,0307 0,0301 0,0294

0,0287 0,0281 0,0274 0,0268 0,0262 0,0256
0,0250 0,0244 0,0239 0,0233

0,0228 0,0222 0,0217 0,0212 0,0207 0,0202
0,0197 0,0192 0,0188 0,0183

Comentários:

A questão informa que, para um nível de 95% de confiança, o intervalo para estimar a média foi (8; 10), ou seja, 9 ± 1. O erro portanto é dado por:
: E = Z^°/o-~P = 1
:

:
\TL

: E a questão pede 0 novo intervalo, quando reduzimos o nível de confiança para 85%, sabendo que os demais ;parâmetros continuarão os mesmos.

= Assim, precisamos comparar 0 valor de z para 95% de confiança e 0 valor de z para 85% de confiança.
A prova apresenta a tabela normal da forma P(Z > Zo). Para um nível de 1 - a =
95% de confiança, resta j

CZ (X

i - = 2,5% abaixo do limite inferior do intervalo e - = 2,5% acima do limite superior do intervalo.
:

: Logo, precisamos do valor de Zo associado a uma probabilidade P(Z > Zo) = 2,5% = 0,025. Pela tabela fornecida, j temos que Zo = 1,96 = 2.;

i Para um nível de 1 — a = 85% de confiança, temos = 7,5% abaixo do limite inferior e | = 7,5% acima i do limite superior do intervalo.
: Logo, precisamos do valor de Zo associado a uma probabilidade P(Z > Zo) = 7,5% = 0,075. Pela tabela fornecida, ;temos que Zo = 1,44.

: Agora, vamos calcular a razão entre os valores de z:

1,44

: = —- = 0,72
:

: z95%
:

= Considerando que 0 erro é diretamente proporcional ao valor de z, a razão entre os erros segue essa mesma =
: proporção:

^*85%

==
P%5%

i

= °'72

: Sabendo que 0 erro a 95% de confiança é igual a 1, então 0 erro a 85% de confiança é:

; ^85% — 0,72 x £950/0 = 0,72 x 1 = 0,72

i Logo, 0 intervalo de confiança é da forma 9 ± 0,72.
i Gabarito: C

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FCC/2014 - TRT/MA) Para responder às questões use, dentre as informações dadas abaixo,
as que julgar apropriadas.
Se Z tem distribuição normal padrão, então: P(Z<0,25)=0,599,
P(Z<0,80)=0,84, P(Z<l)=0,841,
P(Z<l,96)=0,975, P(Z<3,09)=0,999

Considere Xi, X2, ...Xn uma amostra aleatória simples, com reposição, da distribuição da variável X, que tem distribuição normal com média p e variância 36. Seja X a média amostrai dessa amostra.
O valor de n para que a distância entre X e p seja, no máximo, igual a 0,49, com probabilidade de 95% é igual a:
a) 256

b) 225

c) 400

d) 144

e) 576

Comentários:

Ao dizer que a distância entre a média amostrai (estimativa) e a média populacional (parâmetro populacional) seja no máximo igual a 0,49 com probabilidade de 95%, a questão forneceu0 erro máximo
E = 0,49 e 0 nível de confiança de 95%.

Para que 95% da distribuição esteja no intervalo (X — E;X + E), 2,5% da distribuição estará acima desse intervalo e 2,5% abaixo:
Assim, precisamos do valor de z cuja probabilidade P(Z < z) seja igual a 2,5% + 95% = 97,5%.
Pelos valores fornecidas observamos que z = 1,96.

Sabendo que a variância é cr2 = 36, ou seja, 0 desvio padrão éa = = v/36
= 6, podemos calcular 0
tamanho amostrai:

«=(4)2

Gabarito: E.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FGV/2022 - MPE/SC) O tempo, em horas diárias, que homens com idades entre os 40 e
50 anos acessam redes sociais segue uma distribuição Normal com média 2,5 e desvio padrão 1,5. Para o mesmo grupo etário de mulheres, esse tempo segue também uma distribuição Normal com média 3 e desvio padrão 1. Serão retiradas duas amostras casuais e independentes, uma de homens e outra de mulheres.
O tamanho mínimo da amostra da população das mulheres que se pretende com probabilidade pelo menos0,95 e cuja diferença em valor absoluto entre a média amostrai e a média populacional não exceda 0,1 é,aproximadamente:

a) 20;

b) 100;

c) 250;

d) 385;

e) 500.

Comentários:

Essa questão também trabalha com o tamanho amostrai, para um intervalo de confiança para a média, com variância conhecida:
n=G-ff)

Em que z é o valor da tabela normal padrão associado ao nível de confiança desejado;
E é a margem de erro e cr é o desvio padrão.
A^questão pede o tamanho mínimo para o tempo das mulheres, em que o desvio padrão é cr = 1.O enunciado informa, ainda, que a probabilidade do intervalo (nível de confiança) é de 95%, logo, z
= 1,96.

Ademais, a questão informa que a diferença máxima entre a média amostrai e a média populacional, que corresponde à margem de erro, é E = 0,1. Substituindo esses dados na fórmula, temos:
/1,96 \2 z n = (-5Y-1) = (19,6)2 = 384,16
Logo, o menor tamanho amostrai, isto é, o menor número inteiro maior que o valor calculado, é 385.
Gabarito: D

(CESPE 2016/TCE-PA) Considerando uma população finita em que a média da variável de interesse seja desconhecida, julgue o item a seguir.
Se uma amostra aleatória simples, sem reposição, for obtida de uma população finita constituída por N = 45indivíduos, o fator de correção para população finita não será considerado na definição do tamanho da amostra para a estimação da média.
Comentários:

Quando uma população é finita e a amostra é extraída sem reposição, utilizamos, sim,
um ajuste na equação,
chamado fator de correção, que influencia o cálculo do tamanho amostrai.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

População com Variância Desconhecida

Sendo a variância populacional desconhecida, precisamos estimá-la, a partir da variância amostrai(estimador não tendencioso para a variância):

2 IXxQG-*)2

ˢ ⁼ n —i—1

Esse estimador vale para populações infinitas OU amostras extraídas com reposição.

Caso a população seja finita de tamanho TV E a amostra seja extraída sem reposição,
é necessário aplicar o fator de correção, multiplicando a variância amostrai por j-:
TV—n

2 Sr=1(^-^)2 N — n s* =-------------- z x ——-
Com a estimativa para a variância populacional, calculamos a variância da média amostrai X, de forma análoga à que vimos anteriormente, substituindo a variância populacional cr2 pela variância amostrai s2:
s2

VW = - n

E o desvio padrão (ou erro padrão) da média amostrai será a raiz quadrada:

EP(X) = =

O método para a construção do intervalo de confiança será similar ao que vimos antes,
porém utilizaremos a distribuição de t-Student, quando a população seguir distribuição normal (ou quando o tamanho da amostra permitir essa aproximação) com variância desconhecida.
Essa distribuição é similar à normal, também com formato de sino, porém mais achatada no centro e com caudas mais largas, ou seja, apresenta maior variabilidade.
F ESE(SCLARECENDO!

Precisamos utilizar uma outra distribuição, que não a distribuição normal, porque agora a variância deixou de ser um valor fixo e passou a ser também uma estimativa, o que justifica o uso de uma distribuição com maior variabilidade do que a normal.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para isso, também será necessário encontrar os valores deX + EeX — E que delimitam uma probabilidade de 1 - a, considerando a distribuição de t-Student.
A distribuição de t-Student também possui uma tabela para a distribuição padrão, com média igual a 0 e desvio padrão igual a 1. Assim, para encontrar os limites X + E eX — E, utilizamos a seguinte transformação,similar à transformação para a normal padrão:

valor procurado — média da distribuição desvio padrão da distribuição
No caso, os valores procurados são X = X + EeX = X- E; a média da distribuição é
X; e o desvio padrão da distribuição é EPÇX) = -j=:
X + E E

Vn Vn

Reorganizando essa expressão, obtemos a fórmula do erro:

Ou seja, o erro é calculado assim como fizemos para a população com variância conhecida, apenas substituindo a variável da normal padrão z pela variável de t-Student t e o desvio padrão da população o pela sua estimativa s.
O intervalo de confiança é da forma X + E = (X — t.-^=;X + t.-7=).

\ Vn Vn/

O valor de t depende do nível de confiança, assim como o valor de z, mas também do número de graus de liberdade da distribuição, igual ao tamanho da amostra menos 1:
n- de graus de liberdade = n — 1

Por exemplo, para uma amostra de tamanho n = 5, precisamos buscar o valor de t considerando n - 1 = 4graus de liberdade.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Abaixo, inserimos parte da tabela de t-Student, que apresenta os valores de t para os quais as probabilidades
P(T < t) constam na primeira linha, considerando os graus de liberdade indicados na primeira coluna:
n <0,55 <0,60 <0,70 <0,80 <0,90 <0,95
<0,975

<0.99

<0,995

1 0,1584

2 0,1421

3 0,1366

4 0,1338

5 0,1322

0,3249

0,2887

0,2767

0,2707

0,2672

0,7265

0,6172

0,5844

0,5686

0,5594

1,3764

1,0607

0,9785

0,9410

0,9195

3,0777

1,8856

1,6377

1,5332

1,4759

6,3138

2,9200

2,3534

2,1318

2,0150

12,7062

4,3027

3,1824

2,7764

2,5706

31,8205

6,9646

4,5407

3,7469

3,3649

63,6567

9,9248

5,8409

4,6041

4,0321

Supondo que o nível de confiança seja 1 — a = 95%, então a probabilidade associada aos valores acima e abaixo desse intervalo é - = 2,5%.
Ou seja, a probabilidade associada aos valores abaixo do valor crítico superior é:

P(X < X + E) = 95% + 2,5% = 97,5%

Assim, devemos buscar o valor de t para o qual P(T < t) = 0,975, considerando n —
1 = 4 graus de liberdade. Pela tabela acima, temos t = 2,7764 = 2,78. Logo, o intervalo será da seguinte forma:
X± 2,78.-p v5
Vamos supor que a variância amostrai observada seja s2 = 0,0125. Nesse caso, o desvio padrão é dado por:
s = 7s2= 70,0125

Portanto, a margem de erro para esse exemplo é:

s V0,0125 ,-----------

E = 2,78. — = 2,78. y—=— = 2,78 x ^0,0025 = 2,78 x 0,05 = 0,139

\5 \5

Vamos supor que a média observada dessa amostra tenha sidoX = 1,8. Assim, o intervalo de confiança é:
X + E = 1,8 + 0,139 = 1,939

X — E = 1,8 - 0,139 = 1,661

(1,661; 1,939)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

; (FCC/2019 - SEFAZ-BA) Para obter um intervalo de confiança de 90% para a média p de uma população i
; normalmente distribuída, de tamanho infinito e variância desconhecida, extraiu-se uma amostra aleatória ;de tamanho 9 dessa população, obtendo-se uma média amostrai igual a 15 e variância igual a 16.

= Considerou-se a distribuição t de Student para o teste unicaudal tal que a probabilidade P(t - to) = 0,05, com ;
: n graus de liberdade.
j

= Com base nos dados da amostra, esse intervalo é igual a

:
Dados:

n 7 8 9 10 11

tₒ,O₅ 1,90 1,86 1,83 1,81 1,80

a) (12,56; 17,44)

b) (13,76; 16,24)

c) (12,47; 17,53)

d) (12,59; 17,41)

e) (12,52; 17,48)

Comentários:

Essa questão trabalha com um intervalo de confiança para a média de uma população de tamanho infinito
(não precisamos do fator de correção) com variância desconhecida, dado por:

X + E = (x -t.-^=;X + t.-^\

V Vn vn/

Pelo enunciado, sabemos que o tamanho amostrai é n = 9. Logo, temos n — 1 = 8 graus de liberdade.
Pela tabela fornecida, para 8 de graus de liberdade, observamos que t = 1,86.

Considerando que a variância amostrai observada é s2 = 16, logo s = = Vl6 =
4, o erro é dado por:

s 4

E = t.— = 1,86 x - = 2,48

V7v 3

Assim, o intervalo de confiança para a média X = 15 é:

X-E = 15-2,48 = 12,52

X + E = 15 + 2,48 = 17,48

(12,52; 17,48)

Gabarito: E.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FGV/2022 - TJDFT) Em um modelo de simulação de uma fila com apenas um servidor para atendimento,foram realizadas 9 replicações para determinar o número médio de pessoas em fila. Os resultados obtidos para cada replicação estão no quadro a seguir.
Replicação

Média de pessoas na fila
3,8

3,5

4,5

1,4

5 6

2 1,5

1,1

3,2

2,5

Média
2,61

Desvio padrão
1,20

Variância
1,44

O intervalo bilateral de confiança de 95% para a média é, aproximadamente:
a) (1,83; 3,39)

b) (1,73; 3,50)

c) (1,69; 3,53)

d) (0,33; 4,83)

e) (0,04; 5,12)

Nessa prova, foi fornecida a tabela de t-Student da forma P(T > to), parcialmente replicada a seguir.
Grau de liberdade

Área da cauda superior

0,1 0,05 0,025 0,01 0,005

3,078 6,314 12,706 31,821 63,657

1,886 2,920 4,303 6,965 9,925

1,638 2,353 3,182 4,541 5,841

1,533 2,132 2,776 3,747 4,604

1,476 2,015 2,571 3,365 4,032

1,440 1,943 2,447 3,143 3,707

1,415 1,895 2,365 2,998 3,499

1,397 1,860 2,306 2,896 3,355

1,383 1,833 2,262 2,821 3,250

1,372 1,812 2,228 2,764 3,169

; Comentários:

: Essa questão trabalha com um intervalo de confiança para a média, com variância desconhecida:

s

: X±t.—

yn

:

: Em que s é a estimativa para o desvio padrão. Pela tabela fornecida na questão,
temos X = 2,61 es = 1,20.
I

Ademais, o enunciado informa que n = 9 (logo, y/n = VÕ = 3).

: Um intervalo com 95% de confiança deixa 2,5% abaixo do limite inferior e 2,5%
acima do limite superior.

: Logo, precisamos do valor de to associada a uma probabilidade P(T > to) = 2,5% = 0,025.

= Pela tabela de t-Student fornecida, observamos que, para n -1 = 8 graus de liberdade e 0,025 de área da
; cauda superior, temos to = 2,306 = 2,3. Substituindo esses dados na fórmula do intervalo de confiança:
1,2

: 2,61 ± 2,3. — = 2,61 ± 2,3 x 0,4 = 2,61 ± 0,92 = (1,69; 3,53)

L: .G..a..b...a..r.i.t.o...:..C...

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Intervalo de Confiança para a Proporção

Para estimar a proporção populacional p, utilizamos a proporção observada na amostra p.

Para viabilizar os cálculos, as questões consideram a aproximação da distribuição desse estimador a uma normal. Assim, devemos encontrar os valores limites que delimitam uma área sob a curva normal,correspondente a 1 - a:

A variância da proporção amostrai é dada por:

Sendo q = 1 - p. 0 desvio padrão (erro padrão do estimador) é, portanto:

W) = =

Sabendo que a média da distribuição é a proporção amostrai p, então a transformação para a normal padrão de p + E é:
valor procurado — média desvio padrão p + E —p E
Reorganizando essa expressão, obtemos a fórmula do erro do intervalo de confiança:

\ n

E o intervalo de confiança será p ± E

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Vamos supor que tenhamos estimado a proporção amostrai de defeito em p = 0,2 (logo,
q = 1 — p = 0,8),
considerando uma amostra de n = 100 peças.

Nesse caso, o desvio padrão (ou erro padrão) é dado por:

EP(p) =

,2 x 0,8 VÕ46 0,4

----------- = = — = 0,04
100 VTõõ 10

Considerando um nível de confiança de 95% (z = 1,96), a margem de erro será:

E = z.

Então, o intervalo de confiança para a proporção será:

p — z.

(0,12; 0,28)

Tamanho Amostrai

Também podemos determinar o tamanho amostrai, para um dado nível de confiança (1 — a)
e um valor de erro máximo E. Reorganizando a fórmula do erro que acabamos de ver, temos:
Vamos supor que o erro máximo tolerável seja E = 0,04, mantendo os demais parâmetros iguais aos do exemplo anterior (z = 1,96 e p = 0,2). Nesse caso, o tamanho da amostra n₂ será:
x 0,2 x 0,8 = (49)2 x 0,16 = 2401 x 0,16 = 384

TOME

NOTA!

Para calcular o tamanho máximo da amostra n, utilizamos p = q = 0,5, pois essa é a proporção que maximiza a variância da proporção amostrai.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, mesmo sem conhecer a proporção amostrai, é possível determinar um valor seguro para o tamanho amostrai, considerando p = q = 0, 5 na fórmula do tamanho amostrai.
Supondo z = 1,96 e um erro máximo tolerável E = 0,04, o valor seguro para o tamanho amostrai n„, sendo desconhecida a proporção amostrai, é:
n* =

\0,ü4/

x °'5 x °'5 = C49)2 x 0,25 = 2401 x 0,25 s 600

Quanto mais próximo de p = q = 0,5, maior será o tamanho amostrai. Por exemplo, o tamanho amostrai para p = 0,4 (e q = 1 — p = 0,6) é maior do que para p = 0,3 (e q = 1 — p = 0,7).
Ademais, como multiplicamos essas duas proporções no cálculo do tamanho amostrai, não importa qual proporção assume o maior ou o menor valor. Assim, o tamanho da amostra para p = 0,4(q = 1 — p = 0,6)
é igual ao tamanho da amostra para p = 0,6 (q = 1 - p = 0,4).

Essas fórmulas valem para uma população infinita OU amostras extraídas com reposição.

Caso a população seja finita E as amostras extraídas sem reposição, será necessário aplicar o fator de correção para população finita. Para isso, devemos multiplicar a fórmula do erro pelo fator o tamanho amostrai:
-N---n-- , o que afte*ta

N-l' M

N — TL

N-l

HORAtX

Í(CESPE 2018/PF) Determinado órgão governamental estimou que a probabilidade p de um ex-condenado i jvoltar a ser condenado por algum crime no prazo de 5 anos, contados a partir da data da libertação, seja j igual a 0,25. Essa estimativa foi obtida com base em um levantamento por amostragem aleatória simples de ;Item. 1.875 processos judiciais, aplicando-se o método da máxima verossimilhança a partir da distribuição de j jBernoulli.
jSabendo que P(Z < 2) = 0,975, em que Z representa a distribuição normal padrão,
julgue o item que se segue, j iem relação a essa situação hipotética.;

A estimativa intervalar 0,25 ± 0,05 representa o intervalo de 95% de confiança do parâmetro populacionalP-

jComentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O intervalo de confiança para a proporção é dado por:

p+E=p+zx

O enunciado informa que

;* A proporção amostrai ép = 0,25, logo q = 1 — p = 0,75
I

;* O tamanho da amostra é n = 1.875

* O valor de z para 95% de confiança é z = 2

Substituindo esses dados na fórmula do erro do intervalo, temos:

0,1875

= 2x —= 2x0,01 = 0,02

Assim, o intervalo de confiança é:

p + E = 0,25 ± 0,02

Gabarito: Errado.

(2019/FMS) Uma pesquisa tem como finalidade conhecer a proporção de pessoas em Teresina que teriam interesse em frequentar uma nova franquia de lanchonete vinda do exterior. Oempreendedor diz que só vale a pena a instalação da franquia, se pelo menos 10% da população tivesse interesse em frequentar o estabelecimento.
Supondo que a proporção máxima da população não será maior que 30%, qual tamanho de amostra(aproximado) tal que a diferença entre a proporção populacional e proporção amostrai não tenha um erro maior que três pontos percentuais, com uma confiança de 95%. Obs.: zY= 1,96.
a) 897

b) 683

c) 700

d) 300

e) 654

Comentários:

O tamanho amostrai para a construção de um intervalo de confiança para a proporção é dado por:

;O enunciado informa que z = 1,96 e E = 0,03.

Ademais, informa que a proporção máxima p é de 30%. Essa é a proporção que deve ser utilizada, por ser a imais próxima de 50%, para maximizar o tamanho amostrai.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sendo p = 0,3, logo q = 1 — p = 0,7, temos:

Gabarito: A.

/1,96\2

n=te)x °'3 x °'7 3 897

(FGV/2022 - MPE/SC) Uma empresa recebeu um lote muito grande, milhões de peças de refugo, e deseja saber quantas peças deverá examinar para estimar a proporção de itens defeituosos, de modo que o erro de estimação seja no máximo 2%. Será empregada uma seleção aleatória de itens onde cada um será classificado como defeituoso ou não defeituoso. Deseja-se extrair uma amostra aleatória de tamanho n.
Tendo como padrão um grau de confiança de 95%, o tamanho da amostra necessário para garantir o processo é:
a) 189;

b) 384;

c) 600;

d) 1681;

e) 2401.

Comentários:

Essa questão também trabalha com o tamanho amostrai, para a estimação de proporções:

:Em que z é o valor da tabela normal padrão associado ao nível de confiança desejado; E é a margem de erro
(ou erro máximo de estimação); p é a estimativa para a proporção de sucesso e q é a estimativa para a proporção de fracasso, sendo q = 1 — p.
;O enunciado informa que o erro máximo éE = 2% = 0,02; e que o grau de confiança é de 95%, logo,
z=l,96.

A questão não informa a estimativa para a proporção de sucesso, logo, devemos considerar aquela que imaximiza o tamanho da amostra, qual seja p = q = 0,5. Substituindo esses dados na fórmula, temos:
j n = (-2—) x 0,5
x 0,5 = (98)2 x 0,25 = 2401

Gabarito: E

k...................... . .................................... .

Intervalo de Confiança para a Variância

O estimador da variância s2 (variância amostrai), multiplicado pelo fator se8ue uma distribuição qui-quadrado com n— 1 graus de liberdade:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Como essa distribuição é assimétrica, utilizaremos a tabela da distribuição qui-quadrado para encontrar tanto o limite superior X$UP quanto o limite inferior XfNF do intervalo de confiança:
r2 < (n ~ s2 <S X2

A-INF y g-2 J -^SUP

Isolando cr2 nessa expressão, temos:

(n — l).s2

^INF

Ou seja, para calcular o limite inferior, dividimos pelo valor crítico superior da tabela XjUP, e para calcular o limite superior dividimos pelo valor crítico inferior da tabela X2NF.
Isso porque X$UP é maior que X2NF. Assim, quando dividimos por X2UP, obtemos um valor menor (limite inferior) do que quando dividimos por X2NF (limite superior).
Assim, o intervalo de confiança para a variância é da forma:

/ (n-l).s2

\ %SUP

(n-l).s2

Os valores XFUP e X2NF são obtidos a partir da tabela da distribuição qui-quadrado, dependendo do nível de confiança 1 — a desejado:
Observamos que o valor X2NF deixa da distribuição abaixo e o valor X$UP
deixa da distribuição acima,
assim como vimos para os outros intervalos de confiança. A diferença é que agora não estamos mais lidando com uma distribuição simétrica:
P(X2 < X2NF) = -2
P(X2 <X2UP) = 1-^

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Os valores da tabela da distribuição qui-quadrado também dependem do número de graus de liberdade,igual ao tamanho da amostra menos 1.

número de graus de liberdade = n — 1

Para uma amostra de tamanho n = 5, por exemplo, devemos utilizar os valores da tabela da distribuição qui-quadrado com n -1 = 4 graus de liberdade.

A tabela a seguir apresenta os valores de x que delimitam as probabilidades P(X2 <
x) da distribuição qui-
quadrado com 4 graus de liberdade indicadas na primeira linha:

P(X42 < x) 0,005 0,01 0,025 0,05 0,1 0,25 0,5 0,75
0,9 0,95 0,975 0,99 0,995

X 0,21 0,30 0,48 0,71 1,06 1,92 3,36 5,39
7,78 9,49 11,14 13,28 14,86

Para um nível de confiança de 1 — a = 95%, temos:

Pela tabela acima, observamos que o valor de x que delimita uma probabilidade P(X2
< x) = 0,025, que corresponde ao limite inferior, é x = X2NF = 0,48; e o valor de x que delimita uma probabilidadeP(X2 < x) = 0,975, que corresponde ao limite superior, é x = X2UP = 11,14.

Considerando que a variância amostrai é s2 = 0,0125, os limites do intervalo de confiança são:

(n-l).s2 4 x 0,0125 0,05

= = = = 0,004

X2UP 11,14 11,14

(n-l).s2 4 x 0,0125 0,05

2 = = — 0 104

E o intervalo é:

X nf 0,48 0,48 -

(0,004; 0,104)

Caso a questão forneça a soma dos quadrados EQQ — X)2, em vez da estimativa para a variância s2,
podemos utilizá-lo diretamente no cálculo do intervalo de confiança.

IC =

(n — l).s2\

JQNF /

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabendo que s2 X(xt-x)2 , o intervalo de confiança pode ser calculado como:

n-1

Y^-xy W.-xy

1C

^INF

HORA»

í (FGV/2019 - DPE-RJ) Com o objetivo de produzir uma estimativa por intervalo para a variância populacional,
: realiza-se uma amostra de tamanho n = 4, obtendo-se, após a extração, os seguintes resultados:

= Xi = 6, X2= 3, X3 = 11 e X4 = 12

: Informações adicionais:

: P (X24 < 0,75 ) = 0,05 P (X23 < 0,40 ) = 0,05
í P (X24 < 10,8 ) = 0,95 P (X23 < 9 ) = 0,95

= Então, sobre o resultado da estimação, e considerando-se um grau de confiança de
90%, tem-se que:

; a) 5 < o2 <72;

b) 8 < o2 < 180;

; c) 6 < o2 < 135;
d) 4 < o2 < 22;

b) 6 < o2 < 24.

= Comentários:

: O intervalo de confiança para a variância é dado por:

: /(n-l).s2 (n —l).s2\

I ^2 1
I

\ ^SUP ^INF /

= Primeiro, precisamos calcular a estimativa para variância s2 (variância amostrai):

? S^-x)2

n — 1

: Para isso, precisamos da média amostrai:

= IX; 6 + 3 + 11 + 12

* X = =—± =
= — = 8

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Logo, o estimador da variância é:

, (6 — 8)2 + (3 — 8)2 + (11 — 8)2 + (12 — 8)2 (-2)2 + (-5)2 +
(3)2 + (4)2

s =
=

4 — 1 3

, 4 + 25 + 9 + 16 54

i = § = T=18

O enunciado informa que o tamanho da amostra é n = 4, logo, o número de graus de liberdade é n - 1
= 3.

Sabendo que o intervalo de confiança é de 1 - a = 90% = 0,9, precisamos dos valores da tabela que delimitam as probabilidades P(X2 < XfNF) = ~ = 0,05 e P(X2 < X/yP) = 1 — ^ = 0,95.
O enunciado informa que P(X32 < 0,40) = 0,05, logo XfNF = 0,4; e P(X3 < 0,9) = 0,95, logo XFup
= 9.

Assim, os limites inferior e superior são:

Gabarito: C.

ESQUEMATIZANDO

Estimação Intervalar

Intervalo para a Média - Variância conhecida (distribuição normal):

o- (
oAMargem de Erro: E z.^=; Tamanho amostrai: n = \Z-~j

Intervalo para a Média - Variância desconhecida (distribuição t-Student):
Margem de Erro: E = Tamanho Amostrai: n =

Intervalo para a Proporção:

Margem de Erro: E = Tamanho Amostrai: n

Intervalo para a Variância:

/ (n-l).s2
X %SUP

(n-l).s2\

XHIF /

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Estimadores

RESUMo DA AULA

Erro Padrão é o desvio padrão (raiz quadrada da
=> Média amostrai X: E(X) = p, 7(X) = EP(X) =

=> Proporção amostrai p: E(p) = p,V(p) = ™,EP(p) =

variância) do estimador

=> Estimador da variância amostrai: s2 = —l------------

n-1

Propriedades dos Estimadores

=> Suficiente (contempla todas as informações para estimar o parâmetro populacional)

=> Não Tendencioso (esperança do estimador é igual ao parâmetro populacional)

=> Eficiente (menor variância possível)

=> Consistente (estimativas convergem com o aumento do tamanho amostrai)

Métodos de Estimação

—

=> Método dos Momentos: Resulta em X como estimador para a média; e em cr2

estimador para a variância (a2 é tendencioso)

— yrx-—Jõ2

= como n
Método da Máxima Verossimilhança: Resulta em p como estimador para a proporção; para uma
— 2 — x)2

população normal, em X como estimador da média e o = como estimador para a variância
(cr2 é tendencioso)

=> Método dos Mínimos Quadrados: Resulta em X como estimador para a média;
e em p como estimador para a proporção
Estimação Intervalar

Erro depende do nível de confiança desejado e do tamanho da amostra

Erro do Intervalo E

(metade da amplitude)

Intervalo de confiança para população com variância conhecida: X ± z.-^=

y/n

Intervalo de confiança para população com variância desconhecida: X + t

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Distribuição Amostrai

Item. 1. (Cebraspe 2013/Telebras) Acerca da estatística Q2 = - -^)2
em que X = Xl+^+Xn e

X₁,X₂, — ,Xn representa uma amostra aleatória simples retirada de uma distribuição normal, com média3 e variância igual a 4, julgue o item a seguir.

Q2 eX são independentes.

Comentários:

Podemos observar que Q2 é o numerador para o cálculo da variância e que X é a média amostrai. Oenunciado informa que a população segue distribuição normal, que depende dos parâmetros variância (cr2)e média (^), os quais são independentes (pois não apresentam relação entre si). Logo, os respectivos estimadores também são independentes entre si.
Gabarito: Certo.

Item. 2. (Cebraspe 2013/Telebras) Acerca da estatística Q2 = - -^)2
em que X = Xl+^+Xn e

X₁,X₂, — ,Xn representa uma amostra aleatória simples retirada de uma distribuição normal, com média3 e variância igual a 4, julgue o item a seguir.

Q2

A distribuição amostrai da estatística e qui-quadrado, com n -1 graus de liberdade.

Comentários:

Sendo s2 a distribuição amostrai, a seguinte estatística segue distribuição qui-quadrado, com n -1 graus de liberdade:
Sabemos que a variância amostrai é dada por:

s =

2 SJU*,--<?2

n — 1 n — 1

Sabendo que a variância populacional é d2 = 4, então a estatística que segue distribuição qui-quadrado com n -1 graus de liberdade é:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Que é diferente da estatística descrita no item.

Gabarito: Errado.

Item. 3. (Cebraspe 2019/TJ-AM) Em determinado município brasileiro, realizou-se um levantamento para estimar o percentual P de pessoas que conhecem o programa justiça itinerante. Para esse propósito,foram selecionados 1.000 domicílios por amostragem aleatória simples de um conjunto de 10 mil domicílios.Nos domicílios selecionados, foram entrevistados todos os residentes maiores de idade, que totalizaram 3.000pessoas entrevistadas, entre as quais 2.250 afirmaram conhecer o programa justiça itinerante.

De acordo com essa situação hipotética, julgue o seguinte item.

O número médio de pessoas maiores de idade por domicílio foi igual a 3 pessoas por domicílio; e o erro padrão do estimador do percentual P é inversamente proporcional a 3V1.000.
Comentários:

Como foram entrevistadas 3000 pessoas em 1000 domicílios, a média de pessoas maiores de idade por domicílio é igual a:
3000

—— = 3 pessoas por domicilio.

1000

Por outro lado, o erro padrão da proporção é igual a:

EP = t em que p é a proporção amostrai e n o tamanho da amostra.
Sendo a amostra do número de pessoas de tamanho igual a 3000, o número de pessoas que conhecem o programa igual a 2250, então p = 2250/3000 e
2250 750

3000 X 3000

3000

750 „ 750 1

1000 * 1000 X 9000

750 1 1

EP = x , = 0,75 x —,

1000 V9ÕÕÕ 3VTÕÕÕ

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

o que mostra que o erro é inversamente proporcional a 3V1000.

Gabarito: Certo.

Item. 4. (Cebraspe 2019/TJ-AM) Para avaliar a satisfação dos servidores públicos de certo tribunal no ambiente de trabalho, realizou-se uma pesquisa. Os servidores foram classificados em três grupos, de acordo com o nível do cargo ocupado. Na tabela seguinte, k é um índice que se refere ao grupo de servidores, e Nk denota o tamanho populacional de servidores pertencentes ao grupo k.
De cada grupo k foi retirada uma amostra aleatória simples sem reposição de tamanho nk, pk representa a proporção de servidores amostrados do grupo k que se mostraram satisfeitos no ambiente de trabalho.
A partir das informações e da tabela apresentadas, julgue o próximo item.

Com relação ao grupo k = 2, o erro padrão da estimativa da proporção dos servidores satisfeitos no ambiente de trabalho foi inferior a 0,1.
Comentários:

O erro padrão para a proporção é dada pela relação:

EP =

Para k = 2, temos p2 = 0,8 e n2 = 20, de modo que:

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 5. (Cebraspe 2019/TJ-AM) Em determinado município brasileiro, realizou-se um levantamento para estimar o percentual P de pessoas que conhecem o programa justiça itinerante. Para esse propósito,foram selecionados 1.000 domicílios por amostragem aleatória simples de um conjunto de 10 mil domicílios.Nos domicílios selecionados, foram entrevistados todos os residentes maiores de idade, que totalizaram 3.000pessoas entrevistadas, entre as quais 2.250 afirmaram conhecer o programa justiça itinerante.

De acordo com essa situação hipotética, julgue o seguinte item.

A estimativa do percentual de pessoas que conhecem o programa justiça itinerante foi inferior a
60%.

Comentários:

Após selecionados os domicílios, foram entrevistados todos os residentes maiores de idade, que totalizaram
Item. 3.000 pessoas. Nesse grupo, o número de participantes que conhecia o programa justiça itinerante foi de
Item. 2.250 pessoas.

Dessa forma, a estimativa de pessoas que conhecem o programa é de:

2250

3000

0,75 = 75%

Gabarito: Errado.

Item. 6. (Cebraspe 2019/TJ-AM) Para estimar a proporção de menores infratores reincidentes em determinado município, foi realizado um levantamento estatístico. Da população-alvo desse estudo,constituída por 10.050 menores infratores, foi retirada uma amostra aleatória simples sem reposição,composta por 201 indivíduos. Nessa amostra foram encontrados 67 reincidentes.

Com relação a essa situação hipotética, julgue o seguinte item.

Se a amostragem fosse com reposição, a estimativa da variância da proporção amostrai teria sido superior a0,001.

Comentários:

O Teorema Central do Limite nos garante que a variância da proporção amostrai, na amostragem com reposição, tem distribuição aproximadamente normal, sendo calculada pela relação:
Var(p) = P(1~P)

n

Em que p é a proporção amostrai e n é o tamanho da amostra.
Como a amostra tem tamanho n = 201 e p = 67/201 = 1/3, então:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Var(p) = p(l-p)

n

Var(p) =

1 2

3 x 3

Var(p) =

1809

Var(p) = 0,0011

Gabarito: Certo.

Item. 7. (Cebraspe 2018/PF) Determinado órgão governamental estimou que a probabilidade p de um ex-condenado voltar a ser condenado por algum crime no prazo de 5 anos, contados a partir da data da libertação, seja igual a 0,25. Essa estimativa foi obtida com base em um levantamento por amostragem aleatória simples de 1.875 processos judiciais, aplicando-se o método da máxima verossimilhança a partir da distribuição de Bernoulli.
Sabendo que P(Z < 2) = 0,975, em que Z representa a distribuição normal padrão,
julgue o item que se segue, em relação a essa situação hipotética.
O erro padrão da estimativa da probabilidade p foi igual a 0,01.

Comentários:

O estimador de máxima verossimilhança para a proporção populacional é justamente a proporção amostrai.A variância da estimativa de p é dada por:

n

Em que p é a proporção amostrai de casos de interesse (0,25) e q = 1 - p = 0,75.
Além disso, n é o tamanho da amostra, que é de 1.875 processos.
„ 25 x 0,75

S 1.875

Dividindo numerador e denominador por 75:

0,25 x 0,01

Dividindo numerador e denominador por 25:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

s2 = 0,01 x 0,01

O desvio padrão é a raiz quadrada da variância:

s = 0,01

Gabarito: Certo.

Item. 8. (Cebraspe 2018/PF) Uma pesquisa realizada com passageiros estrangeiros que se encontravam em determinado aeroporto durante um grande evento esportivo no país teve como finalidade investigar a sensação de segurança nos voos internacionais. Foram entrevistados 1.000 passageiros,alocando-se a amostra de acordo com o continente de origem de cada um — África, América do Norte (AN), América doSul (AS), Ásia/Oceania (A/O) ou Europa. Na tabela seguinte, N é o tamanho populacional de passageiros em voos internacionais no período de interesse da pesquisa; n é o tamanho da amostra por origem; Pé o percentual dos passageiros entrevistados que se manifestaram satisfeitos no que se refere à sensação de segurança.
Origem N n P

África 100.000 100 80

AN 300.000 300 70

AS 100.000 100 90

A/O 300.000 300 80

Europa 200.000 200 80

Total 1.000.000 1.000

rppop

Em cada grupo de origem, os passageiros entrevistados foram selecionados por amostragem aleatória simples. A última linha da tabela mostra o total populacional no período da pesquisa,o tamanho total da amostra e Ppop representa o percentual populacional de passageiros satisfeitos.
A partir dessas informações, julgue o item.

Considerando o referido desenho amostrai, estima-se que o percentual populacional Ppop seja inferior a 79%.
Comentários:

A proporção amostrai (p) nos dá a estimativa da proporção populacional (p).

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Origem N n P(%)
n x P

África 100.000 100 80% 80

AN 300.000 300 70% 210

AS 100.000 100 90% 90

A/O 300.000 300 80% 240

Europa 200.000 200 80% 160

total 1.000.000 1.000

Logo:

1.000

78%.

De fato, a estimativa é inferior a 79%.

Gabarito: Certo.

Item. 9. (Cebraspe 2018/STM) Em um tribunal, entre os processos que aguardam julgamento, foi selecionada aleatoriamente uma amostra contendo 30 processos. Para cada processo da amostra que estivesse há mais de 5 anos aguardando julgamento, foi atribuído o valor 1; para cada um dos outros, foi atribuído o valor 0. Os dados da amostra são os seguintes:
110010110111101110101010111011

A proporção populacional de processos que aguardam julgamento há mais de 5 anos foi denotada por p;a proporção amostrai de processos que aguardam julgamento há mais de 5 anos foi representada por p

A variância da proporção amostrai p sob a hipótese nula Ho: p = 0,5 é menor que
0,1.

Comentários:

A variância da proporção amostrai é dada por:

Na fórmula acima, temos:

i) p é a proporção populacional de casos favoráveis. A questão disse que p = 0,5;

ii) q é a proporção populacional de casos desfavoráveis, q = 1 — p = 0,5;

iii) né o tamanho da amostra (n = 30).

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

0,5 x 0,5

" 30

0,25

_-3Õ"

s 0,00833

Gabarito: Certo.

Item. 10. (Cebraspe 2018/STM) Em um tribunal, entre os processos que aguardam julgamento, foi selecionada aleatoriamente uma amostra contendo 30 processos. Para cada processo da amostra que estivesse há mais de 5 anos aguardando julgamento, foi atribuído o valor 1; para cada um dos outros, foi atribuído o valor 0. Os dados da amostra são os seguintes:
110010110111101110101010111011

A proporção populacional de processos que aguardam julgamento há mais de 5 anos foi denotada por p;a proporção amostrai de processos que aguardam julgamento há mais de 5 anos foi representada por p

Estima-se que, nesse tribunal, p > 60%.

Comentários:

Na amostra de tamanho 30, há 20 casos favoráveis, ou seja, 20 valores iguais a "1".
Portanto, a proporção amostrai fica:

P = só - 66,67%

Como é comum usarmos a proporção amostrai para estimar a proporção populacional,
pode-se dizer que a estimativa é superior a 60%.
Gabarito: Certo.

Item. 11. (Cebraspe 2018/EBSERH) Xlf X2, X10 representa uma amostra aleatória simples retirada de uma distribuição normal com média p e variância cr2, ambas desconhecidas. Considerando que fie a representam os respectivos estimadores de máxima verossimilhança desses parâmetros populacionais, julgue o item subsecutivo.
A razão segue uma distribuição normal padrão.

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Pode-se mostrar que o estimador de máxima verossimilhança para a média de uma distribuição normalJV(p, cr2) é igual a

— X, + X2 +

fi = X = = Média amostrai

Para concluir a questão, precisamos de duas informações adicionais:

Item. 1. a distribuição da média amostrai de uma distribuição normal com média p e variância cr2 é dada por
Item. 2. para uma variável aleatória X com distribuição normal com média p e variância cr2, a transformação:
X-p

Z = -

a

Juntando as duas informações, chegamos à transformação:

cr

Vn

Gabarito: Errado.

Item. 12. (Cebraspe 2016/TCE-PA) Uma amostra aleatória simples Xlt X2, Xn foi retirada de uma população normal com média e desvio padrão iguais a 10. Julgue o próximo item, a respeito da média amostrai X = |A'1 + X2+. . . +Xn]/n.
A variância de X é igual a 100.

Comentários:

O desvio padrão populacional vale 10, isso é:

a = 10

A variância é igual ao quadrado do desvio padrão:

o2 = 100

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A média amostrai tem variância igual à populacional, dividida por n, em que n é o tamanho da amostra.
Logo, esse valor não é igual a 100.

Gabarito: Errado.

Item. 13. (Cebraspe 2016/TCE-PA) Uma amostra aleatória simples Xlt X2, Xn foi retirada de uma população normal com média e desvio padrão iguais a 10. Julgue o próximo item, a respeito da média amostrai X = |A'1 + X2+... +Xn]/n.
A média amostrai segue uma distribuição t de Student com n — 1 graus de liberdade.

Comentários:

O enunciado garantiu que a distribuição original é normal. Deste modo, a média aritmética X dependerá de uma soma de n variáveis normais, independentes e identicamente distribuídas.Será, também, uma variável normal (e não t de Student).
Gabarito: Errado.

Item. 14. (Cebraspe 2016/TCE-PA) Uma amostra aleatória simples Xlt X2, Xn foi retirada de uma população normal com média e desvio padrão iguais a 10. Julgue o próximo item, a respeito da média amostrai X = |A'1 + X2+... +Xn]/n.
P(X - 10 > 0) < 0,5

Comentários:

O exercício pediu a seguinte probabilidade:

P(X - 10 > 0)

= P(X > 10)

Sabemos que X é normal com média 10.

A média amostrai X, por sua vez, também é normal com média 10. Ou seja, seu comportamento é simétrico ao redor de 10. Isto significa que a chance de termos valores maiores que 10 é igual à chance de valores menores que 10, ambas valendo 50%.
P(X > 10) = 0,5

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O item afirmou que a probabilidade seria menor ou igual a 0,5. Como vimos, ela é justamente igual, o que torna o item correto.
Gabarito: Certo.

Item. 15. (Cebraspe 2016/TCE-PA) Considere um processo de amostragem de uma população finita cuja variável de interesse seja binária e assuma valor 0 ou 1, sendo a proporção de indivíduos com valor1 igual a p = 0,3. Considere, ainda, que a probabilidade de cada indivíduo ser sorteado seja a mesma para todos os indivíduos da amostragem e que, após cada sorteio, haja reposição do indivíduo selecionado na amostragem. A partir dessas informações, julgue o item subsequente.
Se, dessa população, for coletada uma amostra aleatória de tamanho n = 1, a probabilidade de um indivíduo apresentar valor 1 é igual a 0,5.
Comentários:

Como na população temos 30% de casos iguais a 1 (ou seja, a população tem 30% de casos favoráveis), então a chance de a extração resultar em caso favorável é justamente de 30%.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Estimação Intervalar

Item. 1. (Cebraspe 2020/TJ-PA) Para determinado experimento, uma equipe de pesquisadores gerou 20amostras de tamanho n = 25 de uma distribuição normal, com média p = 5 e desvio padrão o = 3. Para cada amostra, foi montado um intervalo de confiança com coeficiente de 0,95 (ou 95%). Com base nessas informações, julgue os itens que se seguem.
I. Os intervalos de confiança terão a forma ± 1,176, em que /?, é a média da amostra i.

II. Para todos os intervalos de confiança, /?, + £> p > - £, sendo £ a margem de erro do estimador.
III. Se o tamanho da amostra fosse maior, mantendo-se fixos os valores do desvio padrão e do nível de confiança, haveria uma redução da margem de erro £.
Assinale a opção correta.

a) Apenas o item II está certo.

b) Apenas os itens I e II estão certos.

c) Apenas os itens I e III estão certos.

d) Apenas os itens II e III estão certos.

e) Todos os itens estão certos.

Comentários:

Vamos analisar as afirmativas:

Item I - Certo. Vamos usar a fórmula do intervalo de confiança (IC) para uma amostra menor ou igual a 30:
X ± ^a/2 x "1=

Vn

X -> média amostrai

Za/t ^o,o25 = 1-96 -» escore associado ao nível de confiança (1 — a)
cr = 3 -> desvio padrão n = 25 tamanho da amostra
Pi ± 1,96 x -

Pi ±1,176

Item II - Errado. O enunciado nos diz que o intervalo de confiança é de 95%, sendo assim 5% estará fora desse intervalo, logo, não é verdadeiro o que se afirma em II.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item III - Certo. Quanto maior o tamanho da amostra, menor a margem de erro.

Gabarito: C.

Item. 2. (Cebraspe 2020/TJ-PA). Ao analisar uma amostra aleatória simples composta de
324 elementos,
um pesquisador obteve, para os parâmetros média amostrai e variância amostrai, os valores 175 e 81,respectivamente.

Nesse caso, um intervalo de 95% de confiança de p é dado por a) (166,18; 183,82).
b) (174,02; 175,98).

c) (174,51; 175,49).

d) (163,35; 186,65).

e) (174,1775; 175,8225).

Comentários:

Vamos listar as informações do enunciado:

Média amostrai -> X = 175

Escore associado ao nível de confiança -> z = 1,96

Desvio padrão -> a = V81 = 9

Tamanho da amostra -> n = 324

Agora, podemos apenas aplicar na fórmula do intervalo de confiança para a média:

cr
X±zx —

fn

175 ± 1,96 x-=

V324

175 ± 1,96

175 ± 1,96 x 0,5

175 ±0,98

175 ±0,98

Logo, o intervalo é (175 - 0,98 = 174,02; 175 + 0,98 = 175,98).

Gabarito: B.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 3. (Cebraspe 2020/TJ-PA). A respeito dos intervalos de confiança, julgue os próximos itens.

I. Um intervalo de confiança tem mais valor do que uma estimativa pontual única, pois uma estimativa pontual não fornece nenhuma informação sobre o grau de precisão da estimativa.
II. Um intervalo de confiança poderá ser reduzido se o nível de confiança for menor e o valor da variância populacional for maior.
III. No cálculo de um intervalo de confiança para a média, deve-se utilizar a distribuição t em lugar da distribuição normal quando a variância populacional é desconhecida e o número de observações é inferior a 30.
Assinale a opção correta.

a) Apenas o item II está certo.

b) Apenas os itens I e II estão certos.

c) Apenas os itens I e III estão certos.

d) Apenas os itens II e III estão certos.

e) Todos os itens estão certos.

Comentários:

Item I - Correto. Uma estimativa pontual não nos dá um parâmetro para definir o quão precisa é a estimativa.Quando temos um intervalo de confiança, quanto maior a amostra, menor é o erro e maior é a precisão.
Item II - Errado. Quanto maior o nível de confiança, menor será a margem de erro e,
consequentemente,
menor será o intervalo de confiança.

Item III - Certo. Para n < 30 e com variância populacional desconhecida utiliza-se t-Student. Se aumentar a amostra com variância desconhecida, ou dada a variância independentemente do tamanho da amostra utiliza-se a distribuição normal.
Gabarito: C.

Item. 4. (Cebraspe 2020/TJ PA) Na construção de um intervalo de confiança para a média, conhecida a variância, considerando o intervalo na forma [x + E; x — E], sendo x o valor do estimador da média e E a semi-amplitude do intervalo de confiança ou, como é mais popularmente conhecida, a margem de erro do intervalo de confiança. Considere que, para uma determinada peça automotiva, um lote de100 peças tenha apresentado espessura média de 4,561 polegada, com desvio padrão de 1,125polegada. Um intervalo de confiança de 95% para a média apresentou limite superior de 4,7815 e limite inferior de4,3405. Nessa situação, a margem de erro do intervalo é de, aproximadamente,

a)E = 0,4410.

b)E = 0,3436.

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

C) E = 0,2205.
d) c = 0,1125.

e) £ = 0,1103.

Comentários:

Vamos listar as informações do enunciado:

Za/₂ -> escore associado ao nível de confiança (1 - a)

nível de confiança de 95% na tabela normal -> Z0025 = 1,96

Desvio padrão -> a = 1,125

Tamanho da amostra -> n = 100

Agora, podemos apenas aplicar na fórmula da margem do erro no intervalo de confiança para a média:

£ = 0,2205

Gabarito: C.

Item. 5. (Cebraspe 2020/TJ-PA) Tabela da distribuição T fornecida.

Em uma amostra aleatória de 20 municípios Paraenses, considerando-se os dados da Secretaria de
Estado de Segurança Pública e Defesa Social relativos ao crime de lesão corporal, a média é igual a 87 e o desvio padrão igual a 101,9419.
Considerando-se, para 19 graus de liberdade, o coeficiente a = 2,093 e utilizando-se o valor aproximado4,4721 para a raiz quadrada de 20, com o auxílio da distribuição t, um intervalo de 95% de confiança para a média deverá ter a) Limite inferior de, aproximadamente, 38,78.
b) Limite superior de, aproximadamente, 143,12.

c) Amplitude 2c = 93,45.

d) Limite inferior de 39,29 e limite superior de 142,18.

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

e) Limite superior de, aproximadamente, 134,71.

Comentários:

Vamos listar as informações do enunciado:

Média amostrai -> X = 87

t -> valor crítico associado ao nível de confiança da distribuição t — student t = 2,093 -> para 95% de confiança
Desvio padrão -> a = 101,9419

Tamanho da amostra -> n = 20 => V2Õ = 4,4721

Agora, podemos apenas aplicar na fórmula do intervalo de confiança para a média:

cr

X + tx —

fn

87 ± 2,093 x

87 ± 2,093 x

101,9419

V2Õ

101,9419

4,4721

87 ± 2,093 x 22,7950

87 ±47,71

Logo, o intervalo é (87 - 47,71 = 39,29; 87 + 47,71 = 134,71)

Gabarito: E.

Item. 6. (Cebraspe 2018/EBSERH) Uma amostra aleatória simples Yl, Y2, Y25 foi retirada de uma distribuição normal com média nula e variância o2, desconhecida. Considerando que P(x2 < 13) =P(X2 > 41)

= 0,025, em que x2 representa a distribuição qui-quadrado com 25 graus de liberdade,
e que S2 = Yt=i rf,

julgue o item a seguir.

[S2/41;S2/13] representa um intervalo de 95% de confiança para a variância o2.

Comentários:

Vamos calcular o intervalo de confiança para o2 com nível 100(1 — a)%.
Assim, determinaremos se a afirmativa é verdadeira:
IC = (o2,1 — a)

S2 S2

Ql-a/2 Qa/2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado nos informou que n = 25.
Sendo a = 0,05, temos:

( S2 S2

/C = (o2,1 — 0,95) = I —------------ ,----------

\Vo,975 VO,025

Qo,975 = 41

@0,025 = 13

Então:

^(-^24 — @0,975) = 0,975, ou seja, P(X24 < @0,975) = 0,025

Logo,

IC = (o2,1-0,95)

Gabarito: Certo.

Item. 7. (Cebraspe 2018/PF) O tempo gasto (em dias) na preparação para determinada operação policial é uma variável aleatória X que segue distribuição normal com média M, desconhecida, e desvio padrão igual a 3 dias. A observação de uma amostra aleatória de 100 outras operações policiais semelhantes a essa produziu uma média amostrai igual a 10 dias.
Com referência a essas informações, julgue o item que se segue, sabendo que P(Z > 2) = 0,025, em que Zdenota uma variável aleatória normal padrão.

A expressão 10 dias ± 6 dias corresponde a um intervalo de 95% de confiança para a média populacional M.
Comentários:

Vamos listar as informações do enunciado:

Média amostrai -> X = 10

Escore associado ao nível de confiança -> z = 2
Desvio padrão -> a = 3

Tamanho da amostra -> n = 100

Agora, podemos apenas aplicar na fórmula do intervalo de confiança para a média:

cr

X±z x —

y/n

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

10 ±2 x

VTõõ

10 ± 2 x 0,3

10 ±0,6

Logo, o intervalo é (10 — 0,6 = 9,4; 10 + 0,6 = 10,6)

Gabarito: Errado.

Item. 8. (Cebraspe 2016/TCE-PA) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0.

Considerando que a amostra

{0,1,1, 0, 0,1, 0,1, 0,1,1, 0, 0,1,1, 0,1,1,1,1}

Foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

Uma vez que a amostra é menor que 30, a estatística do teste utilizada segue uma distribuição t de
Student.

Comentários:

Pelo enunciado, sabemos que a população segue distribuição de Bernoulli (0 ou 1).
Nessa situação, utilizamos a proporção amostrai, p, para estimar a proporção populacional, e consideramos a distribuição normal para estimar o seu intervalo.
Gabarito: Errado.

Item. 9. (Cebraspe 2016/TCE-PA) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0.

Considerando que a amostra

{0,1,1, 0, 0,1, 0,1, 0,1,1, 0, 0,1,1, 0,1,1,1,1}

Foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sendo P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Z representa a variável normal padronizada, e P(t2o
> 2,086) = 0,025 e P(ti9 > 1,729) = 0,05, em que t2o e tig possuem distribuição t de Student com,respectivamente, 20 e 19 graus de liberdade, o erro utilizado para a construção do intervalo de confiança é menor que 15%, se considerado um nível de significância de 5%.
Comentários:

O erro máximo no intervalo de confiança de uma distribuição de proporção é dado por:

Vamos aos dados do problema:

p = 0,6 -> proporção amostrai de 12 empresas regulares em 20

q = 1 — p = 0,4

n = 20 -» tamanho da amostra

Zo = 1,96 -> nível de confiança de 95% na tabela normal

0,6 x 0,4

1,96 x

1,96 x V0,012

1,96 x 0,109

0,213 ou 21,3%

Gabarito: Errado.

Item. 10. (Cebraspe 2016/TCE-PR) A partir de um levantamento estatístico por amostragem aleatória simples em que se entrevistaram 2.400 trabalhadores, uma seguradora constatou que 60% deles acreditam que poderão manter seu atual padrão de vida na aposentadoria.
Considerando que P( | Z | <3)=0,99, em que Z representa a distribuição normal padrão,
assinale a opção correspondente ao intervalo de 99% de confiança para o percentual populacional de trabalhadores que acreditam que poderão manter seu atual padrão de vida na aposentadoria.
a) 60,0% ± 1,0%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

b) 60,0% ± 1,5%

c) 60,0% ± 3,0%

d) 60,0% ± 0,2%

e) 60,0% ± 0,4%

Comentários:

O intervalo de confiança de uma distribuição de proporção é dado por:

P i Zo x

Vamos aos dados do problema:

p = 0,6 -> proporção amostrai q = 1 — p = 0,4
n = 2.400 -> tamanho da amostra

Zo = 3 -> nível de confiança de 99% na tabela normal

0,6 + 3 x

I 0,24

J 2.400

0,6 ± 3 x 70,0001

0,6 ± 3 x 0,01

0,6 ± 0,03

60% ± 3%

Gabarito: C.

Item. 11. (Cebraspe 2016/TCE-PA) Suponha que o tribunal de contas de determinado estado disponha de 30dias para analisar as contas de 800 contratos firmados pela administração. Considerando que essa análise é necessária para que a administração pública possa programar o orçamento do próximo ano e que o resultado da análise deve ser a aprovação ou rejeição das contas, julgue o item a seguir. Sempre que
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

necessário, utilize que P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Z
representa a variável normal padronizada.
Se forem aprovados 90% dos contratos de uma amostra composta de 100 contratos, o erro amostrai será superior a 10%.
Comentários:

A questão trata sobre o erro amostrai da proporção:

O enunciado não nos dá o nível de confiança, portanto, não é possível calcular o erro sem ele. Porém, para deixar evidente que a questão está errada, vamos adotar o nível de confiança de 95%,o escore normal padrão seria de 1,96, valor informado na questão. Então, fica:
e = 1,96

e = 1,96 x 70,0009

e = 1,96 x 0,03

e = 0,0579 ou 5,79%

Logo, temos um erro amostrai inferior a 10%.

Gabarito: Errado.

Item. 12. (Cebraspe 2016/TCE-PA) Suponha que o tribunal de contas de determinado estado disponha de 30dias para analisar as contas de 800 contratos firmados pela administração. Considerando que essa análise é necessária para que a administração pública possa programar o orçamento do próximo ano e que o resultado da análise deve ser a aprovação ou rejeição das contas, julgue o item a seguir. Sempre que necessário, utilize que P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Zrepresenta a variável normal padronizada.
Considerando-se que, no ano anterior ao da análise em questão, 80% dos contratos tenham sido aprovados e que 0,615 seja o valor aproximado de 1,962x0,8x0,2, é correto afirmar que a quantidade de contratos de uma amostra com nível de 95% de confiança para a média populacional e erro amostrai de 5% é inferior a160.

Comentários:

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

/ 102

/

Vamos listar os dados da questão:

p = 0,8 -> proporção amostrai de contas aprovadas no ano anterior q = 1 — p = 0,2
n -» tamanho da amostra

Zo -» escore normal associado ao nível de significãncia 5% -> Zo = 1,96

Temos que o erro amostrai é dado por:

Gabarito: Errado.

Item. 13. (Cebraspe 2016/TCE-PA) A respeito de uma amostra de tamanho n = 10, com os valores amostrados
{0,10, 0,06, 0,10, 0,12, 0,08, 0,10, 0,05, 0,15, 0,14, 0,11}, extraídos de determinada população, julgue o item seguinte.
Por um intervalo de confiança frequentista igual a (-0,11, 0,32), entende-se que a probabilidade de o parâmetro médio ser superior a -0,11 e inferior a 0,32 é igual ao nível de confiança y-
Comentários:

A probabilidade de que o parâmetro dado no enunciado esteja no intervalo construído
(-0,11, 0,32) é ou 0
ou 1. Pela abordagem frequentista, 95% dos intervalos de confiança conteriam o verdadeiro valor do parâmetro (a média populacional).
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 14. (Cebraspe 2016/TCE-PA) Uma amostra aleatória, com n = 16 observações independentes e identicamente distribuídas (IID), foi obtida a partir de uma população infinita, com média e desvio padrão desconhecidos e distribuição normal.
Tendo essa informação como referência inicial, julgue o seguinte item.

Se a média amostrai for igual a 3,2 e a variância amostrai, igual a 4,0, o estimador de máxima verossimilhança para a média populacional será igual a 1,6.
Comentários:

Sabendo que a população segue distribuição normal, então o estimador de máxima verossimilhança para a média populacional é igual à média amostrai. Sabendo que a média amostrai é igual a3,2, então o estimador de máxima verossimilhança para a média populacional é 3,2.
Gabarito: Errado.

Item. 15. (Cebraspe 2016/TCE-PA) Uma amostra aleatória, com n = 16 observações independentes e identicamente distribuídas (IID), foi obtida a partir de uma população infinita, com média e desvio padrão desconhecidos e distribuição normal.
Tendo essa informação como referência inicial, julgue o seguinte item.

Em um intervalo de 95% de confiança para a média populacional em questão, caso se aumente o tamanho da amostra em 100 vezes (passando a 1.600 observações), a largura total do intervalo de confiança será reduzida à metade.
Comentários:

A questão trata da amplitude do intervalo de confiança. Pela fórmula, podemos determinar se a afirmativa da questão está correta. Vamos analisar:
cr

X = 2 x t0 x —

Vn t₀ -> é o escore de distribuição T associado a 95% de confiança,o -> desvio padrão da população n -» tamanho da amostra
Aumentando o tamanho da amostra em 100 vezes, na fórmula ficará Vl00 = 10. Logo,
concluímos que A
será dividido por 10 e não por 2.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 16. (Cebraspe 2015/TELEBRAS) Para estimar a porcentagem de eleitores que votariam a favor de um candidato presidencial, foi escolhida uma amostra aleatória de 200 pessoas. Dessa amostra, uma avaliação indicou que 60 eleitores votariam no referido candidato. Considerando que 0(1,645) =0,95 e que 0(1,96)

= 0,975 em que a função O representa a função distribuição acumulada da distribuição normal padronizada, julgue o seguinte item.
A estimativa pontual para o parâmetro p — proporção de eleitores na população favorável ao candidato —é superior a 25%.

Comentários:

A estimativa pontual para a proporção populacional é a proporção amostrai. 0
enunciado informa que a amostra tem tamanho n = 200, dos quais 60 são favoráveis ao candidato. Assim, a proporção de eleitores favoráveis ao candidato encontrada na amostra foi de:
Que é superior a 25%.

Gabarito: Certo

Item. 17. (Cebraspe 2015/TELEBRAS) Para estimar a porcentagem de eleitores que votariam a favor de um candidato presidencial, foi escolhida uma amostra aleatória de 200 pessoas. Dessa amostra, uma avaliação indicou que 60 eleitores votariam no referido candidato. Considerando que 0(1,645) =0,95 e que 0(1,96)

= 0,975 em que a função O representa a função distribuição acumulada da distribuição normal padronizada, julgue o seguinte item.
O erro máximo provável do intervalo de confiança é inferior a 0,07.

Comentários:

Vamos listar as informações do enunciado:

p = —— = 0,3 -> proporção amostrai q = Çl-p) = 0f7
Za/2 valor crítico da distrubuição normal associado ao nível de significància a valor crítico associado ao nível de significància 5% -> Zo 025 = 1.96
Tamanho da amostra -> n = 200

Agora, podemos apenas aplicar na fórmula da margem do erro no intervalo de confiança:

0,0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

www. estra tegiaconcursos. com. br

05152001900- Evertorn Murilo Vieira

£ = 1,96 x lo,3 x 0,7
J 200

£ = 1,96 x 70,00105

£ = 1,96 x 0,0324

£ = 0,063

Gabarito: Certo.

Item. 18. (Cebraspe 2015/FUB) Em uma faculdade, o administrador universitário supõe que os alunos admitidos no primeiro semestre — grupo P — obtenham um índice de rendimento acadêmico(IRA,
número que varia entre 0 e 5) em média maior do que o índice dos alunos admitidos no segundo semestre
— grupo S.

Considerando que tenha sido selecionada uma amostra aleatória simples de 1.000
estudantes do grupo P
e uma amostra aleatória simples de 1.000 alunos do grupo S, julgue o item seguinte.

Considere que o intervalo de 95% de confiança para a diferença entre as médias dos dois grupos seja igual a(0,1, 1,2). Nesse caso, de acordo com o paradigma frequentista, existe uma probabilidade de 95% de que a verdadeira diferença entre as médias populacionais dos IRAs seja superior a 0,1 e inferior a 1,2
Comentários:

A probabilidade de que o parâmetro dado no enunciado esteja no intervalo construído
(0,1; 1,2) é ou 0 ou

Item. 1. Pela abordagem frequentista, 95% dos intervalos de confiança conteriam o verdadeiro valor do parâmetro(média).

Gabarito: Errado.

Item. 19. (Cebraspe 2015/FUB) O tempo, X, de carregamento de um celular segue uma distribuição normal com média e variância desconhecidas. Foi coletada uma amostra de tamanho igual a 10,em que a média amostrai é de 58 minutos e o desvio padrão da amostra é de 5 minutos. O fabricante do celular, para testar se a média de carregamento é de 50 minutos, aplica um teste t de Student com a hipótese nula Ho-. fix =
50 contra a hipótese alternativa de H₁ : Mx * 50

Considerando a situação hipotética descrita, julgue o item a seguir.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O intervalo de 95% de confiança para é igual a (58 — 5*^75,58 + 5*^75)
em que za é o a-quantil da distribuição Normal.
Comentários:

Para n < 30 e com variância populacional e média desconhecidas utiliza-se T-Student e não uma distribuição normal.
Gabarito: Errado.

Item. 20. (Cebraspe 2015/TELEBRAS)

dados errados

Gráfico I

dados corretos rendaGráfico 11

Um analista coletou os dados a respeito da renda, do consumo e do número de filhos de uma amostra aleatória de 100 famílias. Em 21 dessas famílias, não há filhos, em 26 delas, há apenas um filho,em outras
43, há dois filhos, e em 10 delas, há três filhos. A média da renda das 100 famílias é R$
5.389,00, e o desvio padrão é R$ 2.709,00.
Com base nessas informações, o analista elaborou um gráfico da relação entre renda e consumo (gráficoI). No entanto, posteriormente o analista verificou a existência de erro nesse gráfico,
o que o levou a elaborar um segundo gráfico com os dados corretos (gráfico II).
Considerando que Z siga uma distribuição normal padrão, P(Z < 1,9600) = 0,975, e que
T siga uma distribuição t com 99 graus de liberdade, P(T < 1,9840) = 0,975, julgue o próximo item acerca da situação hipotética e dos gráficos apresentados, arredondando os valores encontrados ao inteiro mais próximo quando for o caso.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considerando-se que a variável renda siga uma distribuição normal com média e variância desconhecidas, é correto afirmar que o intervalo de confiança bilateral para a média de renda na população com nível de confiança de 95% é [4.858, 5.920].
Comentários:

Vamos listar os dados do enunciado:

X = 5.389,00 -> média amostrai t₀ = 1,9840 escore da distribuição T associado a 95% de confiança,s = 2.709 -> desvio padrão amostrai n = 100 -» tamanho da amostra
A variância populacional é desconhecida, então usamos a usamos a distribuição T.

s

X + to x ——

y/n

2.709

5.389,00 ± 1,9840 x-==

VTÕÕ

5.389,00 ± 1,9840 x 270,9

5.389,00 ± 537,46

Logo, temos o intervalo (5.389,00 — 537,46 = 4.851,54 ; 5.389,00 + 537,46 = 5.926,46).

Gabarito: Errado.

Item. 21. (Cebraspe 2015/TELEBRAS) Com relação às técnicas de amostragem estatística,
julgue o próximo item.
Situação hipotética: Pouco antes de uma eleição municipal para prefeito, um instituto de pesquisa declarou que um dos candidatos tinha 52% das intenções de votos, com possibilidade de erro de dois pontos percentuais para mais ou para menos. Assertiva: Nesse caso, o erro destacado corresponde a erro de medição, que é típico ou representativo da tabulação dos dados.
Comentários:

O erro destacado não corresponde a erro de medição e sim a variabilidade normal de uma amostra para outra, erro amostrai.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 22. (Cebraspe 2015/TELEBRAS) Para estimar a porcentagem de eleitores que votariam a favor de um candidato presidencial, foi escolhida uma amostra aleatória de 200 pessoas. Dessa amostra, uma avaliação indicou que 60 eleitores votariam no referido candidato. Considerando que (D (1,645) = 0,95 e que<D (1,96)

= 0,975 em que a função <D representa a função distribuição acumulada da distribuição normal padronizada, julgue o seguinte item.
Um intervalo de confiança (IC) de 95% é dado por IC = [ 0,3 — £,0,3 + £] em que e =

Comentários:

Vamos listas os dados da questão:

p = —— = 0,3 -> proporção amostrai n = 200 -» tamanho da amostra
Za/₂ -> valor crítico da distrubuição normal associado ao nível de significància a valor crítico associado ao nível de significància 5% -» Z0 025 = 1,96 =(0,975)

O intervalo de confiança para a proporção amostrai é dado por:

Logo:

|o,3 x 0,7

6 =

J 200

o^Co^s)

Gabarito: Errado.

Item. 23. (Cebraspe 2014/ANATEL) Julgue o item que se segue, relativo a conceitos de amostragem.

Para se calcular o tamanho de uma amostra a ser retirada de uma população qualquer,
é necessário conhecer o valor da variância populacional da variável de interesse.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para se calcular o tamanho de uma amostra, se o valor da variância populacional for desconhecido, pode-se utilizar o desvio padrão amostrai.
Gabarito: Errado.

Item. 24. (Cebraspe 2014/ANATEL) Julgue o item que se segue, relativo a conceitos de amostragem.

Considere que o intervalo simétrico de 95% de confiança para a média de uma distribuição normal seja obtido a partir de uma amostra aleatória simples. Nesse caso, para que a amplitude desse intervalo seja igual ao dobro do desvio padrão dessa distribuição, é preciso que o tamanho da amostra seja inferior a 10unidades.

Comentários:

Temos que o intervalo de confiança de 95% para uma distribuição normal é dado por:

X± 1,96x4=

Assim, temos que a amplitude desse intervalo será:

2 x 1,96 x 4=

Vn

Logo:

2 x 1,96 x — = 2cr

Vn
1,96 = Vn n = 1,962 < 10
Gabarito: Certo.

Item. 25. (Cebraspe 2014/ANATEL) Com relação a conceitos de intervalos de confiança e planos amostrais,julgue o item subsequente.

Considere que, para a avaliação da qualidade do sinal de conexão com a
Internet que chega a certo município, tenha sido observada uma amostra aleatória simples de velocidades de conexão em alguns pontos desse município, tendo sido o intervalo de 95% de confiança para a velocidade média de conexão(em MB por segundo) igual a [1,5; 3,4], Nessa situação, supondo-se que a velocidade média seja constante,não sofrendo variação ao longo do tempo, é correto afirmar que a velocidade média real de conexão nesse município está no intervalo [1,5; 3,4] com probabilidade 0 ou 1.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

A probabilidade de que o parâmetro dado no enunciado esteja no intervalo construído [1,5; 3,4] é ou
0 ou

Item. 1. Pela abordagem frequentista, 95% dos intervalos de confiança conteriam o verdadeiro valor do parâmetro(velocidade média real).

Gabarito: Certo.

Item. 26. (Cebraspe 2014/ANATEL) Julgue o item que se segue, relativo a conceitos de amostragem.

Suponha que, conforme uma pesquisa de satisfação acerca de planos de serviços de telefonia celular, 30%dos usuários estejam satisfeitos com suas operadoras. Nesse cenário, supondo-se que o tamanho da amostra seja de 900 usuários e a amostragem, do tipo aleatória simples, o erro amostrai dessa pesquisa é inferior a0,02.

Comentários:

Essa questão se refere ao erro padrão da distribuição amostrai, isto é, à raiz quadrada da variância da distribuição amostrai como erro amostrai.
Para a distribuição amostrai da proporção, o erro padrão é dado por:

EP(p) =

Em que:

p = 0,3 -» Sucesso q = 0,7 -> Fracasso (1 — p)
n = 900 -» tamanho da amostra

Assim:

EP(p) =

0,3 x 0,7

0,21

9ÕÕ

Que é inferior a 0,02.

Gabarito: Certo.

EP(p) =

30 10 30 300

EP(p) = 0,015

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 27. (Cebraspe 2013/ANTT) De acordo com determinada pesquisa, o tempo médio de espera de um passageiro em uma rodoviária, desde a chegada ao terminal até o embarque no ônibus, é de 20 minutos.O desvio padrão dos tempos de espera é, também, de 20 minutos e o tamanho da amostra dessa pesquisa é n = 900. Considerando que a pesquisa tenha sido feita por amostragem aleatória simples, julgue o item a seguir.
Com 95% de confiança, a estimativa intervalar do tempo médio de espera de um passageiro na população equivale a 20 minutos ± 20 minutos.
Comentários:

Vamos listar os dados do enunciado:

X = 20 -» média amostrai z = 1,96 escore associado ao nível de confiança de 95% da tabela normal.
a = 20 -> desvio padrão n = 900 -» tamanho da amostra
O intervalo de confiança é dado por:

a
X ± z x —

Xn

20 ± 1,96 x

VÕÕÕ

20 ±1,96 x —

20 ± 1,96 x -

20 ± 1,31

Logo, a estimativa do tempo médio de espera é de 20 minutos ± 1,31 minutos.

Gabarito: Errado.

Item. 28. (CESPE 2011/CBM-DF) Pesquisadores desenvolveram um novo dispositivo para medir a velocidade de uma aeronave e, em um oratório especial, submeteram uma amostra aleatória de 36réplicas da aeronave (amostra A) a um teste de operação, medindo a temperatura mínima necessária para o bom funcionamento de cada réplica.
Considerando essa situação, julgue o item que se segue, acerca de inferência estatística.

Considere que o intervalo de confiança de 95% para a média da temperatura mínima de operação do novo dispositivo tenha sido [-47 2C; -45 QC]. Nessa situação, se o nível de confiança aumentar de 95% para 99%, a amplitude do intervalo de confiança de 99% será inferior a 2 °C.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Para 95% de confiança, o intervalo teve amplitude de 2Q C. Se aumentamos o nível de confiança, ou seja, se quisermos uma "garantia" maior de que estamos acertando a média, precisaremos de uma amplitude maior.Logo, a nova amplitude será maior que 2^C.

Para quem preferir pensar por meio de fórmulas, a amplitude do intervalo de confiança é dada por:

Â = 2 x ZQ x s%

Em que Zo é o escore da normal padrão que delimita o nível de confiança desejado.
Quanto maior o nível de confiança, maior Zo e, por tabela, maior a amplitude.
Gabarito: Errado.

Item. 29. (CESPE 2010/Oficial Técnico de Inteligência) O tempo de duração de determinado aparelho eletrônico segue uma distribuição normal com média desconhecida /i e desvio padrão o =400 horas.
Um estudo feito com uma amostra de n = 1.600 aparelhos produziu um tempo médio de duração igual a 5.000 horas.
Com base nessas informações, e considerando que Z0025 = 1,96, em que Zaé definido por </>(Za) =1 — a e 0 representa a função de distribuição acumulada da distribuição normal padrão, julgue o próximo item.
Considerando que a e n sejam valores constantes, se o nível de confiança aumentar, o comprimento do intervalo de confiança diminuirá.
Comentários:

A amplitude do intervalo de confiança é dada por:

a

2 x Zo x —

Vn

Em que:

* Zo é o quantil da normal padrão correspondente ao nível de confiança adotado;

* cr é o desvio padrão da população;

* n é o tamanho da amostra.

Se o nível de confiança aumentar, estamos aumentando o valor de Zo. Logo, a amplitude do intervalo de confiança também aumentará.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Distribuição Amostrai

Item. 1. (Cebraspe 2013/Telebras) Acerca da estatística Q2 = - -^)2
em que X = Xl+^+Xn e

X₁,X₂, — ,Xn representa uma amostra aleatória simples retirada de uma distribuição normal, com média3 e variância igual a 4, julgue o item a seguir.

Q2 eX são independentes.

Item. 2. (Cebraspe 2013/Telebras) Acerca da estatística Q2 = Yj=i(Xj - -^)2
em que X = Xl+ +Xn e

X₁,X₂, ...,Xn representa uma amostra aleatória simples retirada de uma distribuição normal, com média3 e variância igual a 4, julgue o item a seguir.

Q2

A distribuição amostrai da estatística e qui-quadrado, com n -1 graus de liberdade.

Item. 3. (Cebraspe 2019/TJ-AM) Em determinado município brasileiro, realizou-se um levantamento para estimar o percentual P de pessoas que conhecem o programa justiça itinerante. Para esse propósito,foram selecionados 1.000 domicílios por amostragem aleatória simples de um conjunto de 10 mil domicílios.Nos domicílios selecionados, foram entrevistados todos os residentes maiores de idade, que totalizaram 3.000pessoas entrevistadas, entre as quais 2.250 afirmaram conhecer o programa justiça itinerante.

De acordo com essa situação hipotética, julgue o seguinte item.

O número médio de pessoas maiores de idade por domicílio foi igual a 3 pessoas por domicílio; e o erro padrão do estimador do percentual P é inversamente proporcional a 3V1.000.
Item. 4. (Cebraspe 2019/TJ-AM) Para avaliar a satisfação dos servidores públicos de certo tribunal no ambiente de trabalho, realizou-se uma pesquisa. Os servidores foram classificados em três grupos, de acordo com o nível do cargo ocupado. Na tabela seguinte, k é um índice que se refere ao grupo de servidores, e Nk denota o tamanho populacional de servidores pertencentes ao grupo k.
I 1 500 50 0,7

II 2 300 20 0,8

3 200 10 0,9

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

De cada grupo k foi retirada uma amostra aleatória simples sem reposição de tamanho nk; pk representa a proporção de servidores amostrados do grupo k que se mostraram satisfeitos no ambiente de trabalho.
A partir das informações e da tabela apresentadas, julgue o próximo item.

Com relação ao grupo k = 2, o erro padrão da estimativa da proporção dos servidores satisfeitos no ambiente de trabalho foi inferior a 0,1.
Item. 5. (Cebraspe 2019/TJ-AM) Em determinado município brasileiro, realizou-se um levantamento para estimar o percentual P de pessoas que conhecem o programa justiça itinerante. Para esse propósito,foram selecionados 1.000 domicílios por amostragem aleatória simples de um conjunto de 10 mil domicílios.Nos domicílios selecionados, foram entrevistados todos os residentes maiores de idade, que totalizaram 3.000pessoas entrevistadas, entre as quais 2.250 afirmaram conhecer o programa justiça itinerante.

De acordo com essa situação hipotética, julgue o seguinte item.

A estimativa do percentual de pessoas que conhecem o programa justiça itinerante foi inferior a
60%.

Item. 6. (Cebraspe 2019/TJ-AM) Para estimar a proporção de menores infratores reincidentes em determinado município, foi realizado um levantamento estatístico. Da população-alvo desse estudo,constituída por 10.050 menores infratores, foi retirada uma amostra aleatória simples sem reposição,composta por 201 indivíduos. Nessa amostra foram encontrados 67 reincidentes.

Com relação a essa situação hipotética, julgue o seguinte item.

Se a amostragem fosse com reposição, a estimativa da variância da proporção amostrai teria sido superior a0,001.

Item. 7. (Cebraspe 2018/PF) Determinado órgão governamental estimou que a probabilidade p de um ex-condenado voltar a ser condenado por algum crime no prazo de 5 anos, contados a partir da data da libertação, seja igual a 0,25. Essa estimativa foi obtida com base em um levantamento por amostragem aleatória simples de 1.875 processos judiciais, aplicando-se o método da máxima verossimilhança a partir da distribuição de Bernoulli.
Sabendo que P(Z < 2) = 0,975, em que Z representa a distribuição normal padrão,
julgue o item que se segue, em relação a essa situação hipotética.
O erro padrão da estimativa da probabilidade p foi igual a 0,01.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 8. (Cebraspe 2018/PF) Uma pesquisa realizada com passageiros estrangeiros que se encontravam em determinado aeroporto durante um grande evento esportivo no país teve como finalidade investigar a sensação de segurança nos voos internacionais. Foram entrevistados 1.000 passageiros,alocando-se a amostra de acordo com o continente de origem de cada um — África, América do Norte (AN), América doSul (AS), Ásia/Oceania (A/O) ou Europa. Na tabela seguinte, N é o tamanho populacional de passageiros em voos internacionais no período de interesse da pesquisa; n é o tamanho da amostra por origem; Pé o percentual dos passageiros entrevistados que se manifestaram satisfeitos no que se refere à sensação de segurança.
Origem N n P

África 100.000 100 80

AN 300.000 300 70

AS 100.000 100 90

A/O 300.000 300 80

Europa 200.000 200 80

Total 1.000.000 1.000

p pop
Em cada grupo de origem, os passageiros entrevistados foram selecionados por amostragem aleatória simples. A última linha da tabela mostra o total populacional no período da pesquisa,o tamanho total da amostra e Ppop representa o percentual populacional de passageiros satisfeitos.
A partir dessas informações, julgue o item.

Considerando o referido desenho amostrai, estima-se que o percentual populacional Ppop seja inferior a 79%.
Item. 9. (Cebraspe 2018/STM) Em um tribunal, entre os processos que aguardam julgamento, foi selecionada aleatoriamente uma amostra contendo 30 processos. Para cada processo da amostra que estivesse há mais de 5 anos aguardando julgamento, foi atribuído o valor 1; para cada um dos outros, foi atribuído o valor 0. Os dados da amostra são os seguintes:
110010110111101110101010111011

A proporção populacional de processos que aguardam julgamento há mais de 5 anos foi denotada por p;a proporção amostrai de processos que aguardam julgamento há mais de 5 anos foi representada por p

A variância da proporção amostrai p sob a hipótese nula Ho: p = 0,5 é menor que 0,1.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 10. (Cebraspe 2018/STM) Em um tribunal, entre os processos que aguardam julgamento, foi selecionada aleatoriamente uma amostra contendo 30 processos. Para cada processo da amostra que estivesse há mais de 5 anos aguardando julgamento, foi atribuído o valor 1; para cada um dos outros, foi atribuído o valor 0. Os dados da amostra são os seguintes:
110010110111101110101010111011

A proporção populacional de processos que aguardam julgamento há mais de 5 anos foi denotada por p;a proporção amostrai de processos que aguardam julgamento há mais de 5 anos foi representada por p

Estima-se que, nesse tribunal, p > 60%.

Item. 11. (Cebraspe 2018/EBSERH) Xlf X2, X10 representa uma amostra aleatória simples retirada de uma distribuição normal com média p e variância cr2, ambas desconhecidas. Considerando que fie a representam os respectivos estimadores de máxima verossimilhança desses parâmetros populacionais, julgue o item subsecutivo.
A razão segue uma distribuição normal padrão.

Item. 12. (Cebraspe 2016/TCE-PA) Uma amostra aleatória simples Xlt X2, Xn foi retirada de uma população normal com média e desvio padrão iguais a 10. Julgue o próximo item, a respeito da média amostrai X = [Xt + X2+... +Xn]/n.
A variância de X é igual a 100.

Item. 13. (Cebraspe 2016/TCE-PA) Uma amostra aleatória simples Xlf X2, Xn foi retirada de uma população normal com média e desvio padrão iguais a 10. Julgue o próximo item, a respeito da média amostrai X = |A'1 + X2+... +Xn]/n.
A média amostrai segue uma distribuição t de Student com n — 1 graus de liberdade.

Item. 14. (Cebraspe 2016/TCE-PA) Uma amostra aleatória simples Xlf X2, Xn foi retirada de uma população normal com média e desvio padrão iguais a 10. Julgue o próximo item, a respeito da média amostrai X = |A'1 + X2+... +Xn]/n.
P(X - 10 > 0) < 0,5

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 15. (Cebraspe 2016/TCE-PA) Considere um processo de amostragem de uma população finita cuja variável de interesse seja binária e assuma valor 0 ou 1, sendo a proporção de indivíduos com valor1 igual a p = 03- Considere, ainda, que a probabilidade de cada indivíduo ser sorteado seja a mesma para todos os indivíduos da amostragem e que, após cada sorteio, haja reposição do indivíduo selecionado na amostragem. A partir dessas informações, julgue o item subsequente.
Se, dessa população, for coletada uma amostra aleatória de tamanho n = l,a probabilidade de um indivíduo apresentar valor 1 é igual a 0,5.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. CERTO 6. CERTO
Item. 11. ERRADO

Item. 2. ERRADO 7. CERTO
Item. 12. ERRADO

Item. 3. CERTO 8. CERTO
Item. 13. ERRADO

Item. 4. CERTO 9. CERTO
Item. 14. CERTO

Item. 5. ERRADO 10. CERTO
Item. 15. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Estimação Intervalar

Item. 1. (Cebraspe 2020/TJ-PA) Para determinado experimento, uma equipe de pesquisadores gerou 20amostras de tamanho n = 25 de uma distribuição normal, com média n = 5 e desvio padrão o = 3. Para cada amostra, foi montado um intervalo de confiança com coeficiente de 0,95 (ou 95%). Com base nessas informações, julgue os itens que se seguem.
I. Os intervalos de confiança terão a forma /?É ± 1,176, em que /?, é a média da amostra i.

II. Para todos os intervalos de confiança, /?, + £> fi > Pt - £, sendo £ a margem de erro do estimador.
III. Se o tamanho da amostra fosse maior, mantendo-se fixos os valores do desvio padrão e do nível de confiança, haveria uma redução da margem de erro £.
Assinale a opção correta.

a) Apenas o item II está certo.

b) Apenas os itens I e II estão certos.

c) Apenas os itens I e III estão certos.

d) Apenas os itens II e III estão certos.

e) Todos os itens estão certos.

Item. 2. (Cebraspe 2020/TJ-PA). Ao analisar uma amostra aleatória simples composta de
324 elementos,
um pesquisador obteve, para os parâmetros média amostrai e variância amostrai, os valores 175 e 81,respectivamente.

Nesse caso, um intervalo de 95% de confiança de p é dado por a) (166,18; 183,82).
b) (174,02; 175,98).

c) (174,51; 175,49).

d) (163,35; 186,65).

e) (174,1775; 175,8225).

Item. 3. (Cebraspe 2020/TJ-PA). A respeito dos intervalos de confiança, julgue os próximos itens.

I. Um intervalo de confiança tem mais valor do que uma estimativa pontual única, pois uma estimativa pontual não fornece nenhuma informação sobre o grau de precisão da estimativa.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

II. Um intervalo de confiança poderá ser reduzido se o nível de confiança for menor e o valor da variância populacional for maior.
III. No cálculo de um intervalo de confiança para a média, deve-se utilizar a distribuição t em lugar da distribuição normal quando a variância populacional é desconhecida e o número de observações é inferior a 30.
Assinale a opção correta.

a) Apenas o item II está certo.

b) Apenas os itens I e II estão certos.

c) Apenas os itens I e III estão certos.

d) Apenas os itens II e III estão certos.

e) Todos os itens estão certos.

Item. 4. (Cebraspe 2020/TJ PA) Na construção de um intervalo de confiança para a média, conhecida a variância, considerando o intervalo na forma [x + E; x — E], sendo x o valor do estimador da média e E a semi-amplitude do intervalo de confiança ou, como é mais popularmente conhecida, a margem de erro do intervalo de confiança. Considere que, para uma determinada peça automotiva, um lote de100 peças tenha apresentado espessura média de 4,561 polegada, com desvio padrão de 1,125polegada. Um intervalo de confiança de 95% para a média apresentou limite superior de 4,7815 e limite inferior de4,3405. Nessa situação, a margem de erro do intervalo é de, aproximadamente,

a) E = 0,4410.

b) E = 0,3436.
C)E = 0,2205.
d) E = 0,1125.

e) E = 0,1103.

Item. 5. (Cebraspe 2020/TJ-PA) Tabela da distribuição T fornecida.

Em uma amostra aleatória de 20 municípios Paraenses, considerando-se os dados da Secretaria de
Estado de Segurança Pública e Defesa Social relativos ao crime de lesão corporal, a média é igual a 87 e o desvio padrão igual a 101,9419.
Considerando-se, para 19 graus de liberdade, o coeficiente a = 2,093 e utilizando-se o valor aproximado4,4721 para a raiz quadrada de 20, com o auxílio da distribuição t, um intervalo de 95% de confiança para a média deverá ter
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) Limite inferior de, aproximadamente, 38,78.

b) Limite superior de, aproximadamente, 143,12.

c) Amplitude 2c = 93,45.

d) Limite inferior de 39,29 e limite superior de 142,18.

e) Limite superior de, aproximadamente, 134,71.

Item. 6. (Cebraspe 2018/EBSERH) Uma amostra aleatória simples Yl, Y2, Y25 foi retirada de uma distribuição normal com média nula e variância a2, desconhecida. Considerando que P(xz < 13) =P(X2 > 41)

= 0,025, em que x2 representa a distribuição qui-quadrado com 25 graus de liberdade,
e que S2 = Yt=i rf,

julgue o item a seguir.

[S2/41;S2/13] representa um intervalo de 95% de confiança para a variância o2.

Item. 7. (Cebraspe 2018/PF) O tempo gasto (em dias) na preparação para determinada operação policial é uma variável aleatória X que segue distribuição normal com média M, desconhecida, e desvio padrão igual a 3 dias. A observação de uma amostra aleatória de 100 outras operações policiais semelhantes a essa produziu uma média amostrai igual a 10 dias.
Com referência a essas informações, julgue o item que se segue, sabendo que P(Z > 2) = 0,025, em que Zdenota uma variável aleatória normal padrão.

A expressão 10 dias ± 6 dias corresponde a um intervalo de 95% de confiança para a média populacional M.
Item. 8. (Cebraspe 2016/TCE-PA) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0.

Considerando que a amostra

{0,1,1, 0, 0,1, 0,1, 0,1,1, 0, 0,1,1, 0,1,1,1,1}

Foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

Uma vez que a amostra é menor que 30, a estatística do teste utilizada segue uma distribuição t de
Student.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 9. (Cebraspe 2016/TCE-PA) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0.

Considerando que a amostra

{0,1,1, 0, 0,1, 0,1, 0,1,1, 0, 0,1,1, 0,1,1,1,1}

Foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

Sendo P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Z representa a variável normal padronizada, e P(t2o
> 2,086) = 0,025 e P(ti9 > 1,729) = 0,05, em que t2o e tig possuem distribuição t de Student com,respectivamente, 20 e 19 graus de liberdade, o erro utilizado para a construção do intervalo de confiança é menor que 15%, se considerado um nível de significância de 5%.
Item. 10. (Cebraspe 2016/TCE-PR) A partir de um levantamento estatístico por amostragem aleatória simples em que se entrevistaram 2.400 trabalhadores, uma seguradora constatou que 60% deles acreditam que poderão manter seu atual padrão de vida na aposentadoria.
Considerando que P( | Z | <3)=0,99, em que Z representa a distribuição normal padrão,
assinale a opção correspondente ao intervalo de 99% de confiança para o percentual populacional de trabalhadores que acreditam que poderão manter seu atual padrão de vida na aposentadoria.
a) 60,0% ± 1,0%

b) 60,0% ± 1,5%

c) 60,0% ± 3,0%

d) 60,0% ± 0,2%

e) 60,0% ± 0,4%

Item. 11. (Cebraspe 2016/TCE-PA) Suponha que o tribunal de contas de determinado estado disponha de 30dias para analisar as contas de 800 contratos firmados pela administração. Considerando que essa análise é necessária para que a administração pública possa programar o orçamento do próximo ano e que o resultado da análise deve ser a aprovação ou rejeição das contas, julgue o item a seguir. Sempre que necessário, utilize que P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Zrepresenta a variável normal padronizada.
Se forem aprovados 90% dos contratos de uma amostra composta de 100 contratos, o erro amostrai será superior a 10%.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 12. (Cebraspe 2016/TCE-PA) Suponha que o tribunal de contas de determinado estado disponha de 30dias para analisar as contas de 800 contratos firmados pela administração. Considerando que essa análise é necessária para que a administração pública possa programar o orçamento do próximo ano e que o resultado da análise deve ser a aprovação ou rejeição das contas, julgue o item a seguir. Sempre que necessário, utilize que P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Zrepresenta a variável normal padronizada.
Considerando-se que, no ano anterior ao da análise em questão, 80% dos contratos tenham sido aprovados e que 0,615 seja o valor aproximado de 1,962x0,8x0,2, é correto afirmar que a quantidade de contratos de uma amostra com nível de 95% de confiança para a média populacional e erro amostrai de 5% é inferior a
160.

Item. 13. (Cebraspe 2016/TCE-PA) A respeito de uma amostra de tamanho n = 10, com os valores amostrados
{0,10, 0,06, 0,10, 0,12, 0,08, 0,10, 0,05, 0,15, 0,14, 0,11), extraídos de determinada população, julgue o item seguinte.
Por um intervalo de confiança frequentista igual a (-0,11, 0,32), entende-se que a probabilidade de o parâmetro médio ser superior a -0,11 e inferior a 0,32 é igual ao nível de confiança y-
Item. 14. (Cebraspe 2016/TCE-PA) Uma amostra aleatória, com n = 16 observações independentes e identicamente distribuídas (IID), foi obtida a partir de uma população infinita, com média e desvio padrão desconhecidos e distribuição normal.
Tendo essa informação como referência inicial, julgue o seguinte item.

Se a média amostrai for igual a 3,2 e a variância amostrai, igual a 4,0, o estimador de máxima verossimilhança para a média populacional será igual a 1,6.
Item. 15. (Cebraspe 2016/TCE-PA) Uma amostra aleatória, com n = 16 observações independentes e identicamente distribuídas (IID), foi obtida a partir de uma população infinita, com média e desvio padrão desconhecidos e distribuição normal.
Tendo essa informação como referência inicial, julgue o seguinte item.

Em um intervalo de 95% de confiança para a média populacional em questão, caso se aumente o tamanho da amostra em 100 vezes (passando a 1.600 observações), a largura total do intervalo de confiança será reduzida à metade.
Item. 16. (Cebraspe 2015/TELEBRAS) Para estimar a porcentagem de eleitores que votariam a favor de um candidato presidencial, foi escolhida uma amostra aleatória de 200 pessoas. Dessa amostra, uma avaliação
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

indicou que 60 eleitores votariam no referido candidato. Considerando que 0(1,645) =
0,95 e que 0(1,96)

= 0,975 em que a função O representa a função distribuição acumulada da distribuição normal padronizada, julgue o seguinte item.
A estimativa pontual para o parâmetro p — proporção de eleitores na população favorável ao candidato —é superior a 25%.

Item. 17. (Cebraspe 2015/TELEBRAS) Para estimar a porcentagem de eleitores que votariam a favor de um candidato presidencial, foi escolhida uma amostra aleatória de 200 pessoas. Dessa amostra, uma avaliação indicou que 60 eleitores votariam no referido candidato. Considerando que 0(1,645) =0,95 e que 0(1,96)

= 0,975 em que a função O representa a função distribuição acumulada da distribuição normal padronizada, julgue o seguinte item.
0 erro máximo provável do intervalo de confiança é inferior a 0,07.

Item. 18. (Cebraspe 2015/FUB) Em uma faculdade, o administrador universitário supõe que os alunos admitidos no primeiro semestre — grupo P — obtenham um índice de rendimento acadêmico(IRA,
número que varia entre 0 e 5) em média maior do que o índice dos alunos admitidos no segundo semestre
— grupo S.

Considerando que tenha sido selecionada uma amostra aleatória simples de 1.000
estudantes do grupo P
e uma amostra aleatória simples de 1.000 alunos do grupo S, julgue o item seguinte.

Considere que o intervalo de 95% de confiança para a diferença entre as médias dos dois grupos seja igual a(0,1, 1,2). Nesse caso, de acordo com o paradigma frequentista, existe uma probabilidade de 95% de que a verdadeira diferença entre as médias populacionais dos IRAs seja superior a 0,1 e inferior a 1,2
Item. 19. (Cebraspe 2015/FUB) O tempo, X, de carregamento de um celular segue uma distribuição normal com média e variância desconhecidas. Foi coletada uma amostra de tamanho igual a 10,em que a média amostrai é de 58 minutos e o desvio padrão da amostra é de 5 minutos. O fabricante do celular, para testar se a média de carregamento é de 50 minutos, aplica um teste t de Student com a hipótese nula Ho-. fix =
50 contra a hipótese alternativa de H₁ : Mx * 50

Considerando a situação hipotética descrita, julgue o item a seguir.

O intervalo de 95% de confiança para [ix é igual a (58 — 5*^í75 , 58 + *^75) em que za é o a-quantil da distribuição Normal.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 20. (Cebraspe 2015/TELEBRAS)

dados errados

Gráfico I

dados corretos rendaGráfico II

Um analista coletou os dados a respeito da renda, do consumo e do número de filhos de uma amostra aleatória de 100 famílias. Em 21 dessas famílias, não há filhos, em 26 delas, há apenas um filho,em outras
43, há dois filhos, e em 10 delas, há três filhos. A média da renda das 100 famílias é R$
5.389,00, e o desvio padrão é R$ 2.709,00.
Com base nessas informações, o analista elaborou um gráfico da relação entre renda e consumo (gráficoI). No entanto, posteriormente o analista verificou a existência de erro nesse gráfico,
o que o levou a elaborar um segundo gráfico com os dados corretos (gráfico II).
Considerando que Z siga uma distribuição normal padrão, P(Z < 1,9600) = 0,975, e que
T siga uma distribuição t com 99 graus de liberdade, P(T < 1,9840) = 0,975, julgue o próximo item acerca da situação hipotética e dos gráficos apresentados, arredondando os valores encontrados ao inteiro mais próximo quando for o caso.
Considerando-se que a variável renda siga uma distribuição normal com média e variância desconhecidas, é correto afirmar que o intervalo de confiança bilateral para a média de renda na população com nível de confiança de 95% é [4.858, 5.920].
Item. 21. (Cebraspe 2015/TELEBRAS) Com relação às técnicas de amostragem estatística,
julgue o próximo item.
Situação hipotética: Pouco antes de uma eleição municipal para prefeito, um instituto de pesquisa declarou que um dos candidatos tinha 52% das intenções de votos, com possibilidade de erro de dois pontos percentuais para mais ou para menos. Assertiva: Nesse caso, o erro destacado corresponde a erro de medição, que é típico ou representativo da tabulação dos dados.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 22. (Cebraspe 2015/TELEBRAS) Para estimar a porcentagem de eleitores que votariam a favor de um candidato presidencial, foi escolhida uma amostra aleatória de 200 pessoas. Dessa amostra, uma avaliação indicou que 60 eleitores votariam no referido candidato. Considerando que (D (1,645) = 0,95 e que<D (1,96)

= 0,975 em que a função <D representa a função distribuição acumulada da distribuição normal padronizada, julgue o seguinte item.
Um intervalo de confiança (IC) de 95% é dado por IC = [ 0,3 — £,0,3 + £ ] em que e =
(0,95).

Item. 23. (Cebraspe 2014/ANATEL) Julgue o item que se segue, relativo a conceitos de amostragem.

Para se calcular o tamanho de uma amostra a ser retirada de uma população qualquer,
é necessário conhecer o valor da variância populacional da variável de interesse.
Item. 24. (Cebraspe 2014/ANATEL) Julgue o item que se segue, relativo a conceitos de amostragem.

Considere que o intervalo simétrico de 95% de confiança para a média de uma distribuição normal seja obtido a partir de uma amostra aleatória simples. Nesse caso, para que a amplitude desse intervalo seja igual ao dobro do desvio padrão dessa distribuição, é preciso que o tamanho da amostra seja inferior a 10unidades.

Item. 25. (Cebraspe 2014/ANATEL) Com relação a conceitos de intervalos de confiança e planos amostrais,julgue o item subsequente.

Considere que, para a avaliação da qualidade do sinal de conexão com a
Internet que chega a certo município, tenha sido observada uma amostra aleatória simples de velocidades de conexão em alguns pontos desse município, tendo sido o intervalo de 95% de confiança para a velocidade média de conexão(em MB por segundo) igual a [1,5; 3,4], Nessa situação, supondo-se que a velocidade média seja constante,não sofrendo variação ao longo do tempo, é correto afirmar que a velocidade média real de conexão nesse município está no intervalo [1,5; 3,4] com probabilidade 0 ou 1.
Item. 26. (Cebraspe 2014/ANATEL) Julgue o item que se segue, relativo a conceitos de amostragem.

Suponha que, conforme uma pesquisa de satisfação acerca de planos de serviços de telefonia celular, 30%dos usuários estejam satisfeitos com suas operadoras. Nesse cenário, supondo-se que o tamanho da amostra seja de 900 usuários e a amostragem, do tipo aleatória simples, o erro amostrai dessa pesquisa é inferior a0,02.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

/ 102

/

Item. 27. (Cebraspe 2013/ANTT) De acordo com determinada pesquisa, o tempo médio de espera de um passageiro em uma rodoviária, desde a chegada ao terminal até o embarque no ônibus, é de 20 minutos.O desvio padrão dos tempos de espera é, também, de 20 minutos e o tamanho da amostra dessa pesquisa é n = 900. Considerando que a pesquisa tenha sido feita por amostragem aleatória simples, julgue o item a seguir.
Com 95% de confiança, a estimativa intervalar do tempo médio de espera de um passageiro na população equivale a 20 minutos ± 20 minutos.
Item. 28. (CESPE 2011/CBM-DF) Pesquisadores desenvolveram um novo dispositivo para medir a velocidade de uma aeronave e, em um oratório especial, submeteram uma amostra aleatória de 36réplicas da aeronave (amostra A) a um teste de operação, medindo a temperatura mínima necessária para o bom funcionamento de cada réplica.
Considerando essa situação, julgue o item que se segue, acerca de inferência estatística.

Considere que o intervalo de confiança de 95% para a média da temperatura mínima de operação do novo dispositivo tenha sido [-47 ^C; -45 QC]. Nessa situação, se o nível de confiança aumentar de 95% para 99%, a amplitude do intervalo de confiança de 99% será inferior a 2 QC.
Item. 29. (CESPE 2010/Oficial Técnico de Inteligência) O tempo de duração de determinado aparelho eletrônico segue uma distribuição normal com média desconhecida /i e desvio padrão o =400 horas.
Um estudo feito com uma amostra de n = 1.600 aparelhos produziu um tempo médio de duração igual a 5.000 horas.
Com base nessas informações, e considerando que Z₀,025 = 1,96, em que Zaé definido por </>(Za) =1 — a e 0 representa a função de distribuição acumulada da distribuição normal padrão, julgue o próximo item.
Considerando que a e n sejam valores constantes, se o nível de confiança aumentar, o comprimento do intervalo de confiança diminuirá.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. LETRA C 11. ERRADO
Item. 21. ERRADO

Item. 2. LETRA B 12. ERRADO
Item. 22. ERRADO

Item. 3. LETRA C 13. ERRADO
Item. 23. ERRADO

Item. 4. LETRA C 14. ERRADO
Item. 24. CERTO

Item. 5. LETRA E 15. ERRADO
Item. 25. CERTO

Item. 6. CERTO 16. CERTO
Item. 26. CERTO

Item. 7. ERRADO 17. CERTO
Item. 27. ERRADO

Item. 8. ERRADO 18. ERRADO
Item. 28. ERRADO

Item. 9. ERRADO 19. ERRADO
Item. 29. ERRADO

Item. 10. LETRA C 20. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

