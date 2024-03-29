# Probabilidade e Estatística - Testes de Hipótese

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Introdução - Testes de Hipóteses

2) Conceitos Fundamentais

3) Tipos de Erros

4) Testes de Hipóteses para a Média

5) Testes de Hipóteses para Proporções

6) P-Valor

7) Questões Comentadas - Conceitos Fundamentais - Cebraspe ...

8) Questões Comentadas - Tipos de Erros - Cebraspe

9) Questões Comentadas - Testes para a Média - Cebraspe

10) Questões Comentadas - Testes para Proporções - Cebraspe ...

11) Questões Comentadas - P-Valor - Cebraspe

12) Lista de Questões - Conceitos Fundamentais - Cebraspe

13) Lista de Questões - Tipos de Erros - Cebraspe

14) Lista de Questões - Testes para a Média - Cebraspe

15) Lista de Questões - Testes para Proporções - Cebraspe

16) Lista de Questões - P-Valor - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Olá, amigo(a)!

Chegamos à cereja do bolo da Estatística Inferencial! Os testes de hipóteses são muito queridos pelas bancas porque reúnem o conhecimento de quase toda a Estatística Inferencial e ainda exigem atenção especial na hora da conclusão.
Preparado(a)?!

Luana Brandão

Doutora em Engenharia de Produção (UFF)
Auditora Fiscal da SEFAZ-RJ

Se tiver alguma dúvida, entre em contato comigo!

M professoraluan abran dao@gm ail. com
@professoraluanabrandao

"A direção é mais importante do que o velocidade."

Edson Marques

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

VARIÁVEIS ALEATóRIAS CoNTÍNUAS

As Variáveis Aleatórias podem ser classificadas em variáveis discretas ou contínuas. Os possíveis resultados que uma variável discreta pode assumir são contáveis (ou enumeráveis). Por exemplo,para a variável que representa o lançamento de uma moeda, há 2 possíveis resultados; para o lançamento de um dado, há 6possíveis resultados.

Por outro lado, para variáveis aleatórias contínuas, os resultados não são enumeráveis.
Essas podem assumir quaisquer valores dentro de um intervalo (ou conjunto de intervalos). Por exemplo, a quantidade de água que uma pessoa ingere por dia pode assumir qualquer valor não negativo. São exemplos desse tipo de variável: peso, comprimento, área, volume, distância, tempo etc.
Não é possível contar o resultado de uma variável contínua, apenas mensurar (medir) o seu valor. Por exemplo, não contamos a quantidade de água que uma pessoa ingere por dia,apenas medimos essa quantidade.
Conceitos Fundamentais

Vamos considerar um exemplo de variável contínua: a altura de uma pessoa, que pode assumir qualquer valor positivo. Podemos encontrar valores como 1,70 ou 1,83, ou podemos melhorar a precisão da medição e encontrar 1,704 ou 1,829. Aumentando ainda mais a precisão, podemos encontrar 1,7043 ou 1,8291...
Considerando que podemos sempre acrescentar mais uma casa decimal na medida,
há infinitos valores possíveis para a altura. E isso vale para qualquer variável contínua.
Dessa forma, a probabilidade de uma variável assumir exatamente um valor específico (por exemplo,exatamente 1,82908) é minúscula. Na verdade, essa probabilidade é zero!

Por isso, para variáveis contínuas, associamos as probabilidades a um intervalo de valores (ou conjunto de intervalos). Ou seja, podemos calcular a probabilidade de a altura estar entre, por exemplo, 1,82 e 1,83 ou entre 1,80 e 1,90.
Assim, em vez de termos uma função de probabilidade da forma /(%) = P(X
= x), como no caso de variáveis discretas, para as variáveis contínuas, temos uma função densidade de probabilidade ou simplesmente f.d.p. (não é f!#%# da p#%@, hein!)
Por exemplo, podemos ter a seguinte função densidade de probabilidade (f.d.p.) para uma variável aleatória contínua que assume valores no intervalo entre 0 e 1:
f(x) = 12x2(l — x), se x E [0,1]

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O gráfico dessa f.d.p. é da forma:

TOME

NOTA!

Uma função densidade de probabilidade qualquer satisfaz às seguintes condições:

i) Uma probabilidade qualquer nunca é negativa, logo:

/(*) > o

Obs.: Quando /(%) = 0 em determinado intervalo, a probabilidade associada a esse intervalo será zero.
ii) A probabilidade associada a todo o Espaço Amostrai, isto é, ao conjunto de todos os resultados possíveis da variável, é igual a 100% = 1.
E como se calcula a probabilidade?

A probabilidade associada a um intervalo de valores corresponde à área da região abaixo da f.d.p., nesse intervalo.
Para o exemplo anterior, a probabilidade de x pertencer ao intervalo de 0,4 a 0,6
corresponde à área da região indicada pela seta na figura a seguir:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabendo que a probabilidade de todo o Espaço Amostrai é igual a 1, então a área da região abaixo de toda a f.d.p. é igual a 1.
Dependendo do formato da f.d.p., será possível calcular a sua área, utilizando as fórmulas de geometria básica:
Área Retângulo = Base x Altura

A

Altura

Área Triângulo = BasexAltura

Área Trapézio = {Base Maior+Base Menor)x Altura

Base Menor

Base Maior

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

INDO MAIS

FUNDO!

Se não for possível utilizar as fórmulas de geometria básica para calcular a área da f.d.p.,precisaremos calcular a integral1 dessa função. Por isso, veremos agora um breve resumo das operações mais comuns envolvendo integral.
Para uma potência qualquer de x (exceto para n = -1), a integral é dada por2:

-.71+1

f xn. dx - —-

J n+l

Por exemplo:

[ x2.dx = - = -

2 + 1 3

y — 2 + 1 1
f %-2. dx = = —

J -2+1 -1

Pontue-se que:

i) Quando houver uma multiplicação ou divisão por uma constante, basta multiplicar ou dividir o resultado da integral pela constante:
rn+i f a.xn. dx = a.-----------
J n+l

Por exemplo, f 3x4. dx = 3. y, r X7 j 1 X8

J 10 10 8

1 A ideia da integral consiste na separação da área a ser calculada em retângulos muito estreitos,
como ilustrado a seguir,
de modo que a área da região seja aproximada à soma das áreas dos retângulos.

Quanto mais estreitos forem os retângulos, mais precisa será essa aproximação.

No limite, quando a largura dos retângulos tende a zero, a soma das suas áreas será igual à área da região sob a função, que é justamente a definição de integral da função.
2 O termo dx indica que estamos integrando em relação à variável X.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ii) Se a integral for somente de uma constante, teremos:

f a. dx = a. x

Isso porque se considera que a constante está multiplicada por x° = 1. Logo, o resultado x°+i da integral é —- = x
° o+i

Por exemplo, f dx = f 1. dx = x, f 3.dx = 3x iii) A integral de uma potência de x na base e (constante neperiana e =2,718) é ela mesma:
f ex dx = ex

Além disso, quando há uma soma ou subtração de uma constante no expoente com base e, a integral também permanece a mesma expressão:
Por exemplo: J g(x+4) e(x+4), J e(x 3) dx — e(x 3)

iv) A integral de uma soma (ou subtração) de expressões equivale à soma (ou subtração) das integrais de cada expressão.
Por exemplo: f (x4 + 3x2 - x + 2). dx = f x4dx + J 3x2dx - f x.dx + f 2.dx

O resultado da integral, chamado de integrando, pode ser indicado por F(x).

Para calcular a área sob a função em determinado intervalo, precisaremos calcular a integral definida nesse intervalo, se não for possível utilizar as fórmulas de geometria básica. Para um intervalo (a,b)qualquer:

Assim, depois de calcularmos o integrando F(x), aplicamos no ponto x = b (limite superior do intervalo) e subtraímos o integrando no ponto x = a (limite inferior do intervalo).
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por exemplo, vamos calcular a probabilidade associada ao intervalo (0,5; 0,6) para /(%) = 3x2:

Para isso, precisamos calcular a integral de f(x) = 3x2 definida no intervalo (0,5;
0,6). O primeiro passo, é calcular o resultado da integral, independentemente do intervalo (isto é, o integrando):
r

F(x) = I 3x2. dx = 3 x -—- = 3 x — = x3

J 2 + 1 3

Agora, aplicamos o resultado F(x) = x3 nos pontos x = 0, 5 e x = 0,6:

F(0,5) = 0, 53 = 0,125

F(0,6) = 0,63 = 0,216

Por fim, subtraímos esses valores:

P(0, 5 < X < 0,6) = 0,216 - 0,125 = 0,091 = 9,1%

A seguir, representamos o integrando F(x) = x3 e seus valores para x = 0,5 e para x = 0,6. A sua diferença corresponde à área da f.d.p. /(x) = 3x2 no intervalo entre x = 0,5 e x =0,6 e, consequentemente, à probabilidade associada a tal intervalo.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Atenção! Devemos aplicar o resultado da integral F(x), no ponto b e, em seguida, no ponto a, para então subtrair os resultados F(&) - F(a).
Não podemos calcular a diferença b — a e, em seguida, aplicar essa diferença no integrando F(b — a), o que corresponderia, no exemplo anterior, a F(0,6 — 0,5) = (0,6 - 0,5)3 = 0,l3 = 0,001.
Os resultados são muito diferentes!

Para variáveis contínuas, não importa se definimos um intervalo com sinal "<" (menor que)
ou "<" (menor ou igual).

Como a probabilidade de ser igual a um valor específico é zero, então ambos os sinais correspondem à mesma probabilidade.
P(a < X < &) = P(a < X < h) = P(a < X < Z?) = P(a < X < &)

Isso também vale para os sinais ">" e ">".

Vimos que a probabilidade associada a todo o Espaço Amostrai é igual a 1, certo?
Então, para uma f.d.p. cujo valor mínimo é xt e o valor máximo é x$, a integral definida nesse intervalo é igual a 1, ou seja:
p(s) = Çf(xydx = i

Se a f.d.p. apresentar uma função para toda a reta real, então temos = —oo e xs =
oo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

PROVA!

É possível que uma variável tenha uma função para um intervalo e outra função para outro intervalo, conforme exemplo da Banca CEBRASPE abaixo.
|x, se 0 < x < 1

4 6

0, caso contrário J

Essa f.d.p. apresenta uma função para o intervalo de 0 a 1 e outra função para o intervalo de 1 a 3, como ilustrado abaixo.
Nesse caso, se for necessário integrar em relação a um intervalo que envolva ambas as funções, como o intervalo de 0,5 a 1,5, teremos que separar a integral em duas.
Primeiro, integramos a função -x, no intervalo de 0,5 a 1 e depois integramos a função x 5
------ E -, no intervalo dela 1,5. Em seguida, devemos somar os resultados dessas integrais,

4 6

para encontrar a probabilidade associada a todo o intervalo de 0,5 a 1,5.

P(0,5 < x < 1,5) = 5 (|x) dx + +1) dx

HORA»

(VUNESP/2014 - TJ-PA) Uma variável aleatória contínua tem uma função de probabilidade dada porf(x) =
= K.x, válida apenas no intervalo 1< x < 2. Fora desse intervalo f(x) = 0. De acordo com isso o valor de K é:a) 1/3

; b) 2/3

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) 1/2

d) l e) 2
Comentários:

Para resolver essa questão, devemos considerar que a probabilidade de todo o Espaço
Amostrai é igual a 1.
Para isso, podemos integrar a função f(x) ou, como essa função é uma reta3, basta calcularmos a área delimitada por essa função, indicada abaixo.
Podemos observar que essa região é um trapézio, cuja área é dada por:

(B + Z?) x /i

A= 2

A altura h do trapézio corresponde à amplitude do intervalo:

h = 2- 1 = 1

A base menor b corresponde ao valor da função para x = 1. Como f(x) = K.x, então:

b = f(l) = K.l = K
A base maior corresponde ao valor da função para x = 2:

B = f(2) = K.2 = 2K

Substituindo esses valores na fórmula da área, temos:

(2K + /C) x 1

2 =1

3K = 2

Gabarito: B.

3 Podemos concluir que a função f(x) = K.x é uma reta, pois x está elevado ao expoente 1 (f(x) =
K.x1). Se x estivesse elevado a 0,
ou seja, se a função fosse da forma f(x) = K.x0 = K, então, teríamos uma reta paralela ao eixo X.

Se o expoente fosse igual a 2 ou superior, teríamos uma curva e precisaríamos integrar a função para calcular a probabilidade associada.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FCC/2018 - Analista Judiciário do TRT da 14? Região) Os sinistros de uma companhia de seguros (em R$milhões) são modelados por uma variável aleatória contínua X com função densidade de probabilidade dada por:
/(X) = (1+X)3' X>0

A probabilidade de um sinistro, aleatoriamente escolhido, exceder R$ 1,5 milhões é a) 0,1536.
b) 0,128.

c) 0,84.

d) 0,16.

e) 0,8464.

; Comentários:

A probabilidade de o sinistro exceder 1,5 milhões P(X > 1,5) pode ser calculada como o complementar da
= probabilidade de ele não exceder tal valor:

P(X > 1,5) = 1 - P(X < 1,5)

Para calcular a probabilidade P(X < 1,5), primeiro calculamos a integral da função:

(1 + o-3

(i+xr2

FM = !(i7^dx = f

2 x (1 + x) 3. dx = 2 x —-—

7 -3 + 1

= 2XL-=2^

F(x) = -(i+xr = -^4^

: Agora, aplicamos os limites, com x > 0, conforme enunciado:

P(X < 1,5) = P(0 <X < 1,5) = F(l,5) - F(0)

f(1'5) = -(ü+F'0'16
f(w = -ÕTÕF=-1

= 4Logo:

P(X < 1,5) = F(l,5) - F(0) = -0,16 - (-1) = 1 - 0,16 = 0,84

Então, a probabilidade de exceder esse valor é complementar:

P(X > 1,5) = 1-P(X< 1,5) = 1 - 0,84 = 0,16

Gabarito: D.

4 Observe que a integral aplicada no extremo inferior do intervalo, F(0), foi diferente de zero,
nesse caso.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ii (FCC/2009 - Analista Judiciário do TJ/AP) Se X é uma variável aleatória contínua com função densidade de
; probabilidade dada por:
I

= í^(l - x2), se 0 < x < 1|

(O, caso contrário)

Então o valor de k deve ser i Comentários:
: Para encontrar o valor de K, precisamos considerar que a probabilidade de todo o
Espaço Amostrai é igual a

Item. 1. Para isso, precisamos integrar a f.d.p.:

I

i F(x) = J k(l — x2

)dx = f (k — k. x2)dx = j k.dx — J k. x2dx

= Calculando as integrais em separado, temos:

i J k. dx = k x x í Logo:
Ç x2+1 x2

I k.x2dx = k x-—- = kx —
J 2 + 1 3

F(x) = kxx — kx —

Como 0 < x < 1, então aplicamos esse resultado em x = 0 e em x = 1:

P(0 < X < 1) = f f(x).dx = F(l) — F(0)

:
JloO

i z l3 O3 k Z.k i P(0 < X < 1) = k x 1 - k x —- - k x 0 - k x —- = k - - = ——
-
o o o o
I

: Essa probabilidade de todo o Espaço Amostrai precisa ser igual a 1:

, A 2.À:

; P(O<X<1)= — =1

í fc = 1,5

Gabarito: B.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TIPoS DE ERRoS

0 nível de significância a corresponde à probabilidade de rejeitarmos a hipótese nula, sendo ela verdadeira.
Mos essa situação não é desejável, certo? No mundo ideal, gostaríamos de aceitar a hipótese nula quando ela for verdadeira e rejeitá-la quando ela for falsa.
Realmente, essa situação de rejeitar a hipótese nula quando ela é verdadeira é um erro, chamado de erro tipo I. Essa situação pode ser chamada de falso positivo.
Normalmente, o nível de significância é pré-definido, mas ele pode diminuir quando o tamanho da amostra aumenta, sem alterar os limites da Região de Não Rejeição. Também é possível diminuir o nível de significância, sem alterar o tamanho da amostra, aumentando a Região de Não Rejeição.
Por outro lado, existe a possibilidade de não rejeitar a hipótese nula quando ela é falsa, que também é um erro, chamado de erro tipo II, que pode ser chamada de falso negativo.
A probabilidade desse erro é indicada como fi.

TOME

NOTA!

Erro tipo I (probabilidade a): rejeitar Ho dado que Ho é verdadeira
Erro tipo II (probabilidade f>): não rejeitar Ho dado que Ho é falsa

Os erros correspondem aos respectivos eventos, ou seja, o erro tipo I é o evento de rejeitar a hipótese nula quando esta é verdadeira e o erro tipo II é o evento de não rejeitar a hipótese nula quando esta é falsa. As probabilidades desses eventos são, respectivamente, a (isto é, o nível de significância) e f>.
Nós vamos conviver com esses erros, ok? Sempre que o resultado estiver na Região de
Não Rejeição, vamos decidir não rejeitar a hipótese nula e sempre que o resultado estiver na RegiãoCrítica, vamos rejeitar a hipótese nula. Seguiremos essa regra, mesmo sabendo que existe um risco (/? e a,respectivamente), de estarmos tomando a decisão errada.
Nos gráficos que construímos para os testes de hipóteses, que têm como premissa a hipótese nula, podemos identificar a região de rejeição, cuja probabilidade é a.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considerando o exemplo em que a hipótese nula é Ho\ ft = 2 e que vamos rejeitá-la se a média amostrai observada forX < 1,9 (e não a rejeitar, caso contrário), a probabilidade do erro tipoI corresponde à região à esquerda do limite crítico L= 1,9:
E onde fica a região de f>? Ela não existe!

O erro tipo II é a probabilidade de aceitar a hipótese nula, sendo ela falsa. Ou seja, para visualizá-lo,precisamos do gráfico construído com o verdadeiro parâmetro populacional, que é distinto do parâmetro indicado na hipótese nula, já que estamos considerando que essa hipótese é falsa.
A distribuição verdadeira segue a mesma distribuição da hipótese nula, porém com um parâmetro diferente. Apenas com base nessa distribuição verdadeira podemos visualizar a região do erro tipoII.

Para ilustrar, vamos voltar ao nosso exemplo, em que rejeitamos a hipótese nula Ho-.
p. = 2 se X < 1,9 e não a rejeitamos se X > 1,9. Vamos supor que a verdadeira média populacional seja g. = 1,5. (Essa informação não costuma estar disponível na realidade; mas, algumas questões de prova a fornecem).
A região indicada por /3 corresponde à probabilidade de obter um resultado na Região de Não Rejeição, no caso X > 1,9, considerando que a média verdadeira é /z = 1,5:
M = 1.5 L: 1,9

Para que o valor de /3 possa ser calculado, a questão também pode fornecer duas possibilidades para o parâmetro, por exemplo, Ho: p. = 2 e H^. p. = 1,5.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nessa situação, embora não conheçamos o verdadeiro parâmetro, sabemos que, se a hipótese nula for falsa,então a distribuição terá o parâmetro indicado na hipótese alternativa (n = 1,5).
Assim, podemos calcular a probabilidade do erro tipo II /?, com base na distribuição com o parâmetro indicado na hipótese alternativa.
Os erros nao são complementares: cc + z*/1

Eles pressupõem distribuições distintas e por isso pertencem a Espaços Amostrais diferentes. A rigor, a sua soma pode até ser maior que 1!
Os complementares dos erros correspondem a decisões corretas.

O complementar do erro tipo I corresponde à não rejeição da hipótese nula quando ela é verdadeira e tem probabilidade igual a 1 — a, chamada nível de confiança.
O complementar do erro tipo II corresponde à rejeição da hipótese nula quando ela é falsa e tem probabilidade igual a 1 — /?, chamada poder do teste.
ESQUEMATIZANDO

Vida real

Hipótese nula verdadeira
Hipótese nula falsa
Resultado do teste
RNR

RC
RNR
RC

Decisão
Aceitar
Rejeitar
Aceitar
Rejeitar

Conclusão
Decisão correta
Erro tipo I

Erro tipo II
Decisão correta

Probabilidade

1-a

◦
p

1-p

Conceitos associados
Nível de Confiança
Nível de Significância

-

Poder do teste

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Quando as probabilidades dos erros tipo I e II são mínimas (mais precisamente, quando a sua a combinação linear a. a + b./3 é mínima, sendo a e b são constantes positivas), temos o chamado teste ótimo.
Para esse teste, utilizamos a razão de verossimilhanças (RV):

RV = ^

Pi

Em que p é a função de verossimilhança, ou seja, o produto das funções de probabilidade f, aplicadas para cada resultado da amostra:
p = LÇe.Xi) = = ftO.xJ xf(0,x2) x ... x/(0,xn)

Enquanto p₀ considera o parâmetro 0O indicado na hipótese nula, p±
considera o parâmetro indicado na hipótese alternativa.
O teste irá rejeitar a hipótese nula quando a razão de verossimilhanças for menor do que uma constante k; não rejeitar a hipótese nula quando a razão for maior do que a constante; e será inconclusivo quando a razão for igual à constante:
— < k -> rejeitar Hn., — > k não rejeitar H^, — = k -> inconclusivo
Pi Pi Pi

De modo geral, um teste ótimo irá rejeitar a hipótese nula quando a razão for pequena e não irá rejeitá-la quando a razão for grande.
I«** IX

i (FCC/2019- Secretaria de Manaus/AM) De um estudo, obtiveram-se informações de uma amostra aleatória i
= extraída de uma população. Em um teste de hipóteses, foram formuladas as hipóteses Ho (hipótese nula) e ;
: H| (hipótese alternativa) para analisar um parâmetro da população com base nos dados da amostra.
O nível de significância deste teste corresponde à probabilidade de j
; a) não rejeitar Ho, dado que Ho é falsa.
;

b) rejeitar Ho, dado que Ho é falsa c) rejeitar Ho, dado que Ho é verdadeira j
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

d) não rejeitar Ho, independente de Ho ser falsa ou verdadeira e) rejeitar Ho, independente de Ho ser falsa ou verdadeira
Comentários:

O nível de significância (a), ou seja, a probabilidade do erro tipo I, corresponde à probabilidade de rejeitar a hipótese nula, sendo ela verdadeira.
Gabarito: C

(FGV/2013 - TJ-AM) A respeito do erro do tipo I, assinale a afirmativa correta.

a) é a probabilidade de se rejeitar a hipótese nula quando a mesma é verdadeira.

b) é a probabilidade de se rejeitar a hipótese nula quando a mesma é falsa.

c) é o nível de significância de um teste de hipóteses.

d) é o evento de rejeitar a hipótese nula quando esta é verdadeira.

e) é o evento de não rejeitar a hipótese nula quando esta é falsa.

Comentários:

O erro tipo I é o evento de rejeitar a hipótese nula quando ela é verdadeira, como indicado na alternativa D,que é diferente da sua probabilidade.

As alternativas A e C confundem o evento erro tipo I com a sua probabilidade. Tanto a probabilidade de se rejeitar a hipótese nula, quanto o nível de significância a corresponde à probabilidade do erro tipo I.
A alternativa B define o poder do teste, que é a probabilidade de se rejeitar a hipótese nula, sendo ela falsa,igual a 1 — /?.

Já a alternativa E define o erro tipo II, que é o evento de não rejeitar a hipótese nula, sendo ela falsa.
Gabarito: D

(2018 - HCPA/RS) Considere as afirmações abaixo em relação ao erro em pesquisa.
I - O erro tipo I acontece quando a hipótese nula é rejeitada incorretamente.

II - Alfa define a probabilidade aceitável de falsos-positivos em um teste de hipótese.
III - O erro tipo II é igual a 1 menos alfa.

IV - O poder do estudo é igual a 1 menos beta.
Quais estão corretas?

a) Apenas I

b) Apenas IV

c) Apenas le II

d) Apenas I, II e IV

e) Apenas II, III e IV

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação à afirmação I, o erro tipo I corresponde à rejeição da hipótese nula sendo ela verdadeira.Portanto, a afirmação I está correta.

Em relação à afirmação II, a representa a probabilidade do erro tipo I, definida como aceitável. Considerando que um resultado positivo do teste é a rejeição da hipótese nula, a representa"falsos-positivos". Portanto,
a afirmação II está correta.

Em relação à afirmação III, a probabilidade do erro tipo II (/?) não é complementar de a. Portanto, a afirmação III está incorreta.
Em relação à afirmação IV, o poder do teste é dado por 1 — /?, portanto a afirmação IV está correta.
Gabarito: D

Função Potência

A função potência é a função que representa o poder do teste (1 — (3), o qual corresponde à probabilidade de rejeitar a hipótese nula, sendo ela falsa. Ela é descrita em função do parâmetro verdadeiro podendo ser denotada por 7r:
^Ol)

Quanto maior a diferença entre o parâmetro descrito na hipótese nula n₀ e o parâmetro verdadeiro maior será o poder do teste.
Para visualizar isso, vamos considerar o mesmo exemplo em que a hipótese nula é n₀ =
2, a qual será rejeitada se a média amostrai observada for X < 1,9. A seguir, temos duas curvas, a curva laranja supõe que o parâmetro verdadeiro seja = 1, 5, como vimos antes, e a curva verde supõe que o parâmetro verdadeiro seja Mi = 1,3.
Observe que a região correspondente a /S (X > 1,9) relativa à curva verde é muito menor do que em relação à curva laranja. Consequentemente, o poder do teste 1 — /? é muito maior se o parâmetro verdadeiro for
= 1,3 do que se for = 1,5.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nos testes unilaterais à esquerda, a hipótese alternativa indica um parâmetro menor do que o parâmetro da hipótese nula (como no exemplo que acabamos de ver, Ha\ // < 2). Nesse tipo de situação, quanto menor for o verdadeiro parâmetro, maior o poder do teste. Assim, a função potência é estritamente decrescente,
isto é, ela apenas decresce:

Teste à Esquerda

Nos testes unilaterais à direita, a hipótese alternativa indica um parâmetro maior do que o parâmetro da hipótese nula (por exemplo, Ha\/z > 2). Nesse tipo de situação, quanto maior for o verdadeiro parâmetro,maior o poder do teste. Assim, a função potência é estritamente crescente, isto é, ela apenas cresce:
Teste à Direita

Por fim, no teste bilateral, o parâmetro verdadeiro pode ser menor ou maior do que o parâmetro indicado na hipótese nula (por exemplo, #= 2). Nesses casos, se o parâmetro verdadeiro for inferior, então quanto menor o verdadeiro parâmetro, maior o poder do teste; e se o parâmetro verdadeiro for superior,então quanto maior o verdadeiro parâmetro, maior o poder do teste. Logo, a função potência é decrescente para < n₀ e crescente para > [/₀, como ilustrado abaixo:
Teste Bilateral

►

Portanto, em testes bilaterais, a função potência não é estritamente monótona, isto é,
ela não apresenta um único sentido (crescente ou decrescente).
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Além da diferença entre os parâmetros, o poder do teste também é afetado por outros 2 fatores:

o Tamanho da amostra n: quanto maior o tamanho da amostra, maior o poder do teste;

o Nível de significância a: quanto maior o nível de significância, maior o poder do teste.

O aumento de cada um desses dois fatores diminui a região de não rejeição. Assim, a probabilidade de não rejeitar a hipótese nula sendo ela falsa (/3) se torna menor e, consequentemente, o poder do teste (1 — /?)se torna maior.

Para o nosso exemplo, em que a hipótese alternativa é < 2, o aumento do tamanho da amostra n e/ou do nível de significância a permitiriam rejeitar a hipótese nula para X < 1,95, por exemplo, em vez de X < 1,9.Observe na figura abaixo como essa mudança reduz a região associada a /? e,
consequentemente, aumenta o poder do teste 1 — /?.
1,9 1,95

No exemplo acima, o poder do teste aumentou mesmo sem alterarmos o parâmetro verdadeiro [2₁. Ou seja,o poder do novo teste é maior para todos os valores de Neste caso, dizemos que o teste é mais poderoso.
A figura a seguir1 representa duas funções de poder de um teste bilateral,
em que o parâmetro da hipótese nula é ju = 60.
1 Figura obtida na apresentação de Estatística Aplicada II da Prof. Lilian
M. Lima Cunha, disponível no site https://edisciplinas.usp.br/pluginfile.php/1928095/mod_resource/content/0/a ula8-2016.pdf
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A curva azul representa a função para uma amostra de tamanho n = 25 e a curva vermelha, para uma amostra de tamanho n = 100.
Podemos verificar que o poder do teste para n = 100 é maior do que para n = 25
para qualquer valor do parâmetro verdadeiro n₁.
Assim, dizemos que o teste para n = 100 é mais poderoso do que para n = 25.

Na figura anterior, também podemos observar que ambas as funções assumem o menor valor
(ambas a 5%)
para = 60, isto é, quando a hipótese nula é verdadeira. Esse valor corresponde ao nível de significância a, também chamado de tamanho do teste.
Já, o teste uniformemente mais poderoso (UMP) é aquele que maximiza o poder do teste
(minimiza /?) para testar determinada hipótese nula HO:6E0O frente à determinada hipótese alternativa H^.OeQ^considerando determinado nível de significância a (ou tamanho a).

O teste UMP atende às seguintes condições:

* a probabilidade de rejeitar a hipótese nula, quando ela é falsa, é maior do que a de qualquer outro teste, com o mesmo nível de significância a.
Sendo Y* o teste UMP e Y qualquer outro teste com o mesmo nível de significância, temos:

7Ty*(0) > 7Ty(0), V 9 E 01

* a probabilidade de rejeitar a hipótese nula, quando ela é verdadeira, é, no máximo2, igual a a:
swpgE&onY*(0) = a

Os testes UMP só existem em situações especiais, por exemplo, para distribuições da família exponencial.
Função potência

Função do poder do teste (1 — (3), que varia com o parâmetro verdadeiro

O poder do teste aumenta com o aumento dos seguintes fatores:

* Diferença entre o parâmetro verdadeiro e o parâmetro da hipótese nula;

* Tamanho amostrai n;

* Nível de significância a (ou tamanho do teste).

2 O termo "sup" representa supremo, sendo definido como o menor limite superior de um conjunto de dados.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

HOKADE

r......... ......... .....

í (CESPE/2019 - TJ-AM) A respeito dos testes de hipóteses, julgue o próximo item.

I

: O poder de um teste estatístico varia conforme o tamanho amostrai.

; Comentários:

= O poder do teste, que representa a probabilidade de rejeitar a hipótese nula,
quando ela é falsa, dado por

1 — /?, aumenta conforme o tamanho da amostra aumenta, conforme o nível de significância a aumenta,
: e conforme a diferença entre o valor do parâmetro observado 0 e o valor do parâmetro para a hipótese nula
= Oo aumenta.

: Portanto, a afirmativa está correta.

: Gabarito: Certa

; (FGV/2019 - DPE-RJ - Adaptada) A respeito da formulação, execução, decisão e critérios de avaliação de testes de hipóteses, julgue as afirmativas a seguir:
; I - Em testes bilaterais, envolvendo a distribuição normal, a função potência é estritamente monótona.

: II - Um teste é uniformemente mais poderoso para dado nível de significância se esse nível minimiza a
: probabilidade do erro do Tipo II para valores compatíveis com Ho.

; Comentários:

: Em relação à primeira afirmativa, a função potência para testes bilaterais decresce para valores menores que a média e cresce para valores maiores que a média.
= Portanto, a função não é estritamente monótona e a afirmativa está incorreta.

: Em relação à segunda afirmativa, o teste é considerando uniformemente mais poderoso,
para determinado

: nível de significância (a), quando maximizar o poder do teste (ou minimizar o erro tipo II) para testar a
; hipótese nula frente à hipótese alternativa.

i Logo, o item II está correto.

Resposta: Item I errado; Item II certo.

: (FGV/2022 - PC/AM) Em relação ao poder de um teste de hipóteses, NÃO é possível afirmar que

: a) é definido como a probabilidade de se rejeitar a hipótese nula, quando essa é falsa.

b) é igual à unidade deduzida da probabilidade de erro do tipo II.

: c) quanto maior o tamanho da amostra, maior o poder do teste de hipóteses.

d) é afetado pelo verdadeiro valor do parâmetro que é testado.

: e) independe do nível de significância fixado pelo pesquisador.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

A questão pede a alternativa INCORRETA a respeito do poder do teste.

Em relação à alternativa A, o poder do teste corresponde à probabilidade de rejeitar a hipótese nula, sendo ela falsa. Logo, a alternativa A está correta.
Em relação à alternativa B, o poder do teste é o complementar da probabilidade do erro tipo II. Ou seja,sendo /3 a probabilidade do erro tipo II, o poder do teste é 1 — /?. Logo, a alternativa B está correta.
Em relação à alternativa C, quanto maior o tamanho da amostra (mantendo as demais características constantes), maior o poder do teste, de fato. Afinal, o poder do teste corresponde a uma decisão correta e quanto maior o tamanho da amostra, mais precisa é a estimativa e,consequentemente, maior a probabilidade de tomar uma decisão correta. Logo, a alternativa C está correta.
Em relação à alternativa D, a função do poder do teste (chamada função potência) é dependente do valor verdadeiro do parâmetro: quanto maior a diferença entre o parâmetro verdadeiro e o parâmetro indicado na hipótese nula, maior o poder do teste. Logo, a alternativa D está correta.
Em relação à alternativa E, o nível de significância também influencia o poder do teste - quanto maior o nível de significância, maior o poder do teste. Afinal, o nível de significância está associado à região crítica e,consequentemente, à probabilidade de rejeição da hipótese nula. Logo, a alternativa E está incorreta.
Gabarito: E

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TESTES DE HIPóTESES PARA A MÉDIA

Nessa seção, veremos os testes de hipóteses para a média de populações, que podem ter a variância conhecida ou não. Essas duas situações estão associadas a distribuições distintas de probabilidade: no primeiro caso, utilizamos a distribuição normal e, no segundo, a distribuição de t-Student.
Teste para Média com Variância Conhecida

Quando a população tiver variância conhecida cr2 e distribuição normal, a média amostrai X também terá distribuição normal. Se a população apresentar outra distribuição, mas o tamanho da amostra for suficientemente grande, também podemos aproximar a distribuição da média amostrai a uma normal(Teorema Central do Limite). Assim, utilizamos a seguinte transformação entre a normal e a normal padrão:
valor na distribuição — média da distribuição z —
desvio padrão da distribuição

Os testes que levam em consideração uma distribuição normal (ainda que seja por aproximação) são chamados de Testes Z.
Para calcular os limites das regiões RC e RNR, partimos de um nível de confiança 1 — a fornecido
(ou do nível de significância cr) e do tipo de teste (bilateral, unilateral à esquerda ou unilateral à direita). Com essas informações, calculamos o valor dez que corresponde ao limite entre a região de não rejeição e a região crítica, que podemos chamar de zc (z crítico).
No caso do teste bilateral, haverá dois valores de zc (um à esquerda e outro à direita). Como as regiões críticas de cada lado são do mesmo tamanho, então, pela simetria da curva normal padrão, os valores críticos serão iguais em módulo (ou seja, terão o mesmo valor absoluto), porém um será negativo e outro positivo.
Por exemplo, vamos supor que o nível de confiança desejado seja 1 — a =
90% (ou seja, nível de significância a = 10%) em um teste bilateral, conforme ilustrado a seguir.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Precisamos dos valores que delimitam 5% da distribuição abaixo de LINF e 5% acima de
LSUP. Pela simetria da normal padrão, o limite superior estará associado a um valor crítico da normal padrão zc e o limite inferior a -zc.
A seguir, temos um excerto da tabela normal que apresenta as probabilidades P(0 < Z
< z), isto é, as probabilidades entre 0 e o valor de z indicado na tabela, conforme ilustrado na figura a seguir.
0 t

0,00 0,01 0,02 0,03 0,04 0,05
0,06 0,07 0,08 0,09

0,4332 0,4345 0,4357 0,4370 0,4382 0,4394 0,4406
0,4418 0,4429 0,4441

0,4452 0,4463 0,4474 0,4484 0,4495 0,4505 0,4515
0,4525 0,4535 0,4545

0,4554 0,4564 0,4573 0,4582 0,4591 0,4599 0,4608
0,4616 0,4625 0,4633

0,4641 0,4649 0,4656 0,4664 0,4671 0,4678 0,4686
0,4693 0,4699 0,4706

0,4713 0,4719 0,4726 0,4732 0,4738 0,4744 0,4750
0,4756 0,4761 0,4767

0,4772 0,4778 0,4783 0,4788 0,4793 0,4798 0,4803
0,4808 0,4812 0,4817

Sabendo que a curva normal é simétrica, o lado direito da curva normal tem probabilidade P(Z > 0) = 50%.Então, para que 5% da distribuição seja superior a zc, precisamos buscar o valor de zc que delimite uma probabilidade de 50% - 5% = 45% entre 0 e zc:
P(0 < Z < zc) = P(Z > 0) - P(Z > zc) = 50% - 5% = 45% = 0,45

Pela tabela anterior, observamos que o valor mais próximo é zc = 1,64, pois P(0 <
Z < 1,64) = 0,4495.
Portanto, o limite superior será calculado considerando zc = 1,64 e o limite inferior, zc =
-1,64.

Além do valor de zc, para utilizar a fórmula da transformação, precisamos da média e do desvio padrão da distribuição.
Como nos testes de hipóteses consideramos a hipótese nula como premissa, o valor da média da distribuição é o valor da média populacional n indicada na hipótese nula.
Ademais, sabendo que vamos extrair uma amostra e calcular a sua média amostrai X para realizar o teste,o desvio padrão que vamos utilizar é o desvio padrão da média amostrai, dado pela razão entre o desvio padrão populacional e a raiz quadrada do tamanho da amostra:
cr

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Pronto! Conhecendo zc, o desvio padrão populacional cr e o parâmetro jU
indicado na hipótese nula,
podemos calcular os limites para a média amostrai Lx entre a RC e a
RNR, utilizando a fórmula da transformação:
Sendo o limite superior calculado com um valor positivo de zc e o limite inferior, com um valor negativo.Reorganizando essa expressão, obtemos a fórmula para calcular os limites:

—i u + z X<-7=

r —r c vn

Vamos supor que o desvio padrão populacional seja cr = 1 e que o tamanho da amostra seja n = 16. Assim,o desvio padrão da média amostrai é:

o _ 1 _ 1

Então, supondo que o parâmetro a ser testado seja = 2, em um teste bilateral, com nível de significância de 10% (vimos que, para esse caso, temos zc = 1,64) o limite superior para a média amostrai será:
LSUP = 2 + 1,64 x - = 2 + 0,41 = 2,41

E o limite inferior será:

Linf = 2 — 1,64 x - = 2 - 0,41 = 1,59

Para esse exemplo, iremos rejeitar a hipótese inicial de [i = 2, caso a média amostrai seja X < 1,59 ou se
X > 2,41.

A razão zt = calculada com base na média amostrai x observada no teste pode ser chamada estatística do teste.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Outra forma de decidir se vamos rejeitar ou não a hipótese nula é comparar a estatística do teste (também chamado de escore reduzido observado) com o valor crítico da normal padrão zc, em vez de comparar X e os limites superior/inferior estabelecidos, como fizemos anteriormente.
Assim, a hipótese nula será rejeitada se a estatística do teste for maior que o limite crítico superior zc ou menor que o limite crítico inferior — zc. Como esses limites possuem o mesmo valor absoluto, basta comparar o valor absoluto da estatística com o valor crítico absoluto zc e rejeitar a hipótese nula se a estatística for superior.
Vamos supor que, no exemplo acima, tenhamos observado X = 1,55. Como 1,55
< 1,59, sabemos que vamos rejeitar a hipótese nula, porque o resultado do teste é inferior ao limite mínimo estipulado.
Alternativamente, podemos concluir quanto à hipótese nula, comparando a estatística do teste ao valor crítico zc. A estatística do teste é calculada, utilizando a fórmula da transformação para o valor observado
— 1

X = 1,55, sabendo que a média é /z = 2 e que o desvio padrão da média amostrai é o* = -:

X — LI 1,55-2= ---- = -0,45 x 4 = -1,8

Zt~ rr =

Como o valor absoluto da estatística é superior ao valor crítico |zt| > zc, rejeitamos a hipótese inicial.
I«** IX

(2019 - Instituto Federal de Educação, Ciência e Tecnologia da Paraíba) Um atleta,
querendo levantar dinheiro para participar de campeonatos, compra uma máquina de empacotar biscoitos caseiros em embalagens de 300g. Para aferir se a máquina está embalando corretamente o atleta tomou uma amostra de 1500 embalagens, que apresentou uma média de 285g e desvio padrão de 15g. Com os resultados do experimento realizado pelo atleta proporcionam evidências suficientes para concluir que a máquina não está trabalhando conforme o esperado. Nível de confiança de 99%. Sabendo que F(z) é a função de distribuição acumulada da normal padrão, onde F(l,3) = 0,90, F(l,64) = 0,95, F(l,96) = 0,975, F(2,58) = 0,995
Observando o problema acima, responda, qual teste deve ser realizado e quais os valores críticos?

a) Teste bilateral e valores críticos 1,96 e -1,96

b) Teste bilateral e valores críticos 1,3 e -1,3

c) Teste unilateral à esquerda e valor crítico igual a 2,33

d) Teste unilateral à direita e valor crítico igual a 2,33

e) Teste bilateral e valores críticos 2,58 e -2,58

Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nesse caso, a máquina precisa empacotar corretamente, nem a mais (senão, o atleta terá prejuízo), nem a menos (senão, o cliente será lesado). Portanto, o teste deve ser bilateral.
Para um nível de confiança 1 - a = 99%, isto é, nível de significância de a = 1%,
a área á direita do limite superior (e à esquerda do limite inferior) deve ser a= 0,5%, como ilustrado a seguir.
Considerando que a tabela padrão apresentada apresenta a função de distribuição acumulada, precisamos do valor de z que corresponde a uma probabilidade acumulada F(z) = P(Z < z) = 0,5% + 99% = 99,5%.
Pela tabela, vemos que esse valor é z = 2,58, pois F(2,58) = 0,995.
Portanto, os valores críticos, na curva normal padrão, são -2,58 e 2,58.
Gabarito: E.

(VUNESP/2019 - TJ-SP) Um teste de hipóteses consistirá em testar, ao nível de significância de 5%, se a vida média p das lâmpadas produzidas por uma indústria é igual a 2 000 horas, em face da hipótese alternativa de p ser diferente de 2 000 horas. A população das vidas das lâmpadas produzidas é normalmente distribuída, de tamanho infinito e variância conhecida. Com base em uma amostra aleatória de 100 lâmpadas da população que apresentou uma vida média de 2 050 horas, foi realizado o teste.Seja z o valor do escore da distribuição normal padrão (Z) tal que a probabilidade P(|Z| < z) = 95%. O valor do escore reduzido encontrado, por meio dos dados da amostra, para comparar com o valor de z foi igual a 2,5.
O desvio padrão populacional é de a) 500 horas b) 400 horas c) 280 horas d) 100 horas e) 200 horas
Comentários:

O enunciado apresenta os seguintes dados:

o Média /.i = 2000 (hipótese nula a ser testada);

o Tamanho da amostra n = 100;

o Valor observado x = 2050; e o Escore reduzido encontrado (estatística do teste): z = 2,5.
Para calcular o desvio padrão populacional o, com base nesses dados, devemos utilizar a transformação entre a normal e a normal padrão:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Substituindo os dados fornecidos, temos

Gabarito: E

(2018 - Economista da Secretaria de Estado de Saúde/DF) O preenchimento automático de garrafas de água de uma determinada marca segue o modelo de distribuição normal com média p = 500 ml e desvio padrão de 20 mL. Em uma amostra de 4 garrafas, foi encontrado o volume médio de 485 mL.
Aplicando-se o teste de hipótese:

Ho\p = 500 ml

H±: p < 500 ml

Com base na amostra obtida, a conclusão do teste é que se rejeita Ho com a) 1% de significância b) 3% de significância, mas não com 1% de significância c) 5% de significância, mas não com 3% de significância d) 7% de significância, mas não com 10% de significância e) 7% de significância, mas não com 5% de significância
Considere os seguintes valores da tabela normal padrão fornecida na prova: P(z<2,43) =
99%; P(z<l,88) =
97%, P(z<l,64) = 95%, P(z<l,48) = 93% e P(z<l,28) = 90%.

Comentários:

O enunciado informa que a hipótese nula é p = 500 ml e a hipótese alternativa é p
< 500 ml, portanto,
trata-se de um teste para a média, unilateral à esquerda.

Sendo assim, vamos rejeitar a hipótese nula se a média amostrai observada for inferior ao limite mínimo calculado para o nível de significância buscado.
Como as alternativas mencionam diversos níveis de significância distintos, será menos trabalhoso calcular a estatística do teste e compará-la ao valor crítico zc.
O enunciado forneceu os seguintes dados:

o Média indicada na hipótese nula: p = 500;

o Desvio padrão populacional cr = 20;

o Tamanho da amostra n = 4; e o Valor observado x = 485.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

: Com base nessas informações, podemos calcular a estatística do teste:

í X -
jU

: Zt =

: Primeiro, vamos calcular o desvio padrão da média amostrai:

; o- 20

: °x = ~j=
= ~j= = = 10

Vn V4 Z

i

: Então, o valor de z para a média amostrai encontrada x = 485 (estatística do teste) é:

485 - 500 -15

Zt ~ iõ _ 1õ" 1'5

A hipótese nula será rejeitada se o módulo | zt| = 1,5 for maior do que o valor crítico (em módulo)
Zc.

= Pelos valores da tabela normal padrão fornecidos, observamos que a estatística do teste |zt| =
1,5 está entre í z = 1,64 e z = 1,48.
Sendo P(Z < 1,64) = 95%, temos a seguinte situação:

Como a estatística do teste (em módulo) é menor do que o valor crítico ao nível de
5% de significância, não rejeitamos a hipótese a esse nível. Também não iremos rejeitar a hipótese nula para um nível menor de significância, porque isso implicaria em um valor crítico ainda maior.
Sendo P(Z < 1,48) = 93%, temos:

Como a estatística do teste (em módulo) é maior do que o valor crítico ao nível de
5% de significância,
rejeitamos a hipótese a esse nível. Também iremos rejeitar a hipótese nula para um nível maior de significância, porque isso implicaria em um valor crítico ainda menor.
Gabarito: E.

(FGV/2022 - TJDFT) Deseja-se testar a média populacional p, sendo as hipóteses:

Ho-. p = 600 e H₁:p>600

Suponha que o tamanho da amostra seja n = 100, a variância seja conhecida e igual a o2 = 400 e a probabilidade de ocorrer o erro do tipo I, 2,5%.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O poder do teste, quando a média, sob a hipótese alternativa, for /z = 608 é, aproximadamente:
a) 82,3%;

b) 87,2%;

c) 92,2%;

d) 97,7%;

e) 100%.

Para resolver essa questão, considere a tabela normal padrão P(Z > Zo) fornecida na prova, parcialmente replicada a seguir.
Probabilidade da distribuição normal padrão acumulada na cauda superior - Prob(Z>Zo)
Segunda decimal de Zo

0,00 0,01 0,02 0,03 0,04 0,05
0,06 0,07 0,08 0,09

1,00

1,20

1,30

1,40

1,50

1,60

1,70

1,80

1,90

2,00

0,1587 0,1562 0,1539 0,1515 0,1492 0,1469 0,1446
0,1423 0,1401 0,1379

0,1357 0,1335 0,1314 0,1292 0,1271 0,1251 0,1230
0,1210 0,1190 0,1170

0,1151 0,1131 0,1112 0,1093 0,1075 0,1056 0,1038
0,1020 0,1003 0,0985

0,0968 0,0951 0,0934 0,0918 0,0901 0,0885 0,0869
0,0853 0,0838 0,0823

0,0808 0,0793 0,0778 0,0764 0,0749 0,0735 0,0721
0,0708 0,0694 0,0681

0,0668 0,0655 0,0643 0,0630 0,0618 0,0606 0,0594
0,0582 0,0571 0,0559

0,0548 0,0537 0,0526 0,0516 0,0505 0,0495 0,0485
0,0475 0,0465 0,0455

0,0446 0,0436 0,0427 0,0418 0,0409 0,0401 0,0392
0,0384 0,0375 0,0367

0,0359 0,0351 0,0344 0,0336 0,0329 0,0322 0,0314
0,0307 0,0301 0,0294

0,0287 0,0281 0,0274 0,0268 0,0262 0,0256 0,0250
0,0244 0,0239 0,0233

0,0228 0,0222 0,0217 0,0212 0,0207 0,0202 0,0197
0,0192 0,0188 0,0183

; Comentários:

= Essa questão trabalha pede o poder do teste. O primeiro passo é calcularmos o limite da região crítica,
= considerando o parâmetro indicado na hipótese nula /z, sabendo que se trata de um teste unilateral à direita
; (limite crítico superior somente):

cr

: L = ^ + z.—

Vn

: Para isso, o enunciado informa que:

= * O parâmetro indicado na hipótese nula é jiz = 600;
I

i * A variância da população é o2 = 400, logo o desvio padrão é o = v/400 = 20;
i * O tamanho da amostra é n = 100, logo a raiz quadrada é y/n = 10.

= Para obtermos o valor de z, o enunciado informa que a probabilidade de ocorrer o erro tipo I (nível de
: significância) é a = 2,5% = 0,025. Assim, precisamos do valor de Zo tal que P(Z > Zo) = 0,025:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Pela tabela, observamos que Zo = 1,96 = 2. Agora, podemos encontrar o limite superior:

L = 600 + 2 x — = 600 + 4 = 604

O poder do teste corresponde à probabilidade de rejeitar a hipótese nula (ou seja, de observarmos um resultado maior que esse limite), considerando que o parâmetro verdadeiro é /i = 608 (hipótese nula falsa).
Para isso, utilizamos a fórmula da transformação para L = 604, considerando o parâmetro verdadeiro:

604- 608 —4

Assim, o poder do teste é 1 — /3 = P(Z > -2), ilustrada a seguir:

Pela simetria da normal padrão, temos:

P(Z < -2) = P(Z > 2)

Pela tabela observamos que /? = P(Z > 2) = 0,0228.
Logo, o poder do teste é:

1 - £ = 1 - 0,0228 = 0,9772 = 97,7%

Gabarito: D

Teste para Média com Variância Desconhecida

Quando a variância da população for desconhecida, precisamos estimá-la pela variância amostrai.

O estimador não tendencioso para a variância (variância amostrai) é:

7 — - xy

Em que n é o tamanho da amostra.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Alternativamente, podemos calcular o estimador não tendencioso para a variância como:

Que decorre da fórmula da variância populacional 7(X) = E(X2~) — /j2.

Como dividimos por n, na fórmula da variância populacional, e por n — 1, na fórmula da variância amostrai, precisamos multiplicar a fórmula da variância populacional por n e dividir por n — 1, para obter a variância amostrai.
Esse estimador vale para populações infinitas OU amostras extraídas com reposição.

Caso a população seja finita de tamanho N, e a amostra seja extraída sem reposição, é necessário aplicar o fator de correção, multiplicando a fórmula da variância amostrai por^—j-.
N—n

Com a estimativa para a variância populacional, calculamos a estimativa para a variância da média amostrai
(basta substituir cr2 por s2, na fórmula da variância da média amostrai, que conhecemos):

E o desvio padrão da média amostrai será (a raiz quadrada):

s

=

Vn

Quando a população seguir distribuição normal (ou quando o tamanho da amostra permitir essa aproximação), mas com variância desconhecida, utilizamos a distribuição t-Student, que é similar à normal,porém mais achatada no centro e com caudas mais largas, ou seja, apresenta maior variabilidade.

Por ser baseado nessa distribuição de t-Student, esse teste pode ser chamado de teste T.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabendo que a média da distribuição é o parâmetro p indicado na hipótese nula, a estatística do teste, que corresponde à transformação da média amostrai observada x para a distribuição padronizada, é:
t x~ii x~n

Essa estatística deve ser comparada ao valor crítico tabelado tc, considerando o nível de significância desejado, o tipo de teste (bilateral, unilateral à esquerda ou unilateral à direita) e n — 1 graus de liberdade.
Alternativamente, podemos utilizar a fórmula da transformação para calcular os limites das regiões RC/RNR,considerando o valor crítico tc.

Reorganizando a expressão acima, obtemos a fórmula para os limites críticos:

Por exemplo, suponha o mesmo nível de confiança 1 — a = 90% do nosso exemplo anterior, um teste bilateral e uma amostra de tamanho n = 5.
Nessa situação, precisamos do valor de t, considerando n — 1 = 4 graus de liberdade.

A seguir, temos parte da tabela de t-Student, que apresenta os valores de t para os quais as probabilidades
P(T < t) constam na primeira linha, considerando os graus de liberdade indicados na primeira coluna:
n <0,55 <0.60 <0,70 <0,80 <0,90
<0,95 <0,975

<0,99

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

Se a probabilidade associada ao intervalo de confiança é de 90%, então a probabilidade associada aos valores acima e abaixo desse intervalo é de 5%, como ilustrado abaixo.
Logo, a probabilidade associada aos valores menores que tc é:

P(T < tc) = 5% + 90% = 95%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, devemos buscar o valor de t com 4 graus de liberdade, para o qual P(T < t₄) = 0,95.
Pela tabela acima, temos tc = 2,1318 = 2,13.

Agora, vejamos os demais parâmetros para calcular os limites do intervalo.

Vamos supor que a variância amostrai observada seja s2 = 0,0125. Nesse caso, a variância da média amostrai será estimada por:
0,0125

—-— = 0,0025

E o desvio padrão da média amostrai será estimado pela sua raiz quadrada:

= V0,0025 = 0,05

Portanto, supondo que a média populacional indicada na hipótese nula seja pi = 1, os limites superior e inferior serão, respectivamente:
LSUP — jU + t x sx — 1 + 2,13 x 0,05 — 1 + 0,1065 — 1,165

LINF — jti — txsx= 1 — 2,13 x 0,05 = 1 — 0,1065 = 0,8935

HORADt í (FGV/2022 - TCU) Assuma que o valor anual gasto para pagamento de pessoal em municípios de uma certa i
: região do Brasil possui distribuição normal com parâmetros desconhecidos. Em uma amostra de 16 j
: municípios, observou-se um gasto médio de R$ 1.000.000,00 ao ano com desvio padrão amostrai igual a R$ j
= 500.000,00. Gostaríamos de testar se o gasto médio para pagamento de pessoal desses municípios é ;
: estatisticamente diferente de R$ 750.000,00.
j

= O teste a ser usado e o valor da sua estatística de teste são, respectivamente:

: a) teste T e a estatística de teste é igual a 2;
=

b) teste Z e a estatística deteste é igual a 1/2;

= c) teste T e a estatística deteste é igual a 1/2;
j d) teste F e a estatística deteste é igual a 1/2;
= e) teste Z e a estatística deteste é igual a 2;

: Comentários:

= O enunciado informa que a população segue distribuição normal com parâmetros desconhecidos, ou seja, ;tanto a média quanto a variância da população são desconhecidas.

= Assim, temos um teste para a média com variância desconhecida, em que devemos utilizar a distribuição de ;t-Student (teste T).

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para isso, o enunciado fornece os seguintes dados:

* Tamanho da amostra n = 16;

* Gasto médio observado na amostra x = 1.000.000; e

* Desvio padrão amostrai s = 500.000.

Ademais, o enunciado informa que o objetivo do teste é verificar se a média é estatisticamente diferente de
Item. 750.000. Ou seja, /z = 750.000 corresponde à hipótese nula e 750.000
corresponde à hipótese alternatica.ao parâmetro da hipótese nula.
Assim, a estatística do teste é dada por:

x-/z 1.000.000 - 750.000 250.000 250.000

Ü TT- 500.000 500.000 125.000 2

Vn 7Í6 4

Já temos a resposta da questão, mas vale reforçar que, para decidirmos se rejeitamos ou não a hipótese nula, comparamos essa estatística do teste ao valor tabelado da distribuição de t-Student com n — 1 = 15graus de liberdade.

Gabarito: A

(FCC/2018 - TCE-RS) Uma população, referente aos comprimentos de certo cabo, é normalmente distribuída, de tamanho infinito e com variância desconhecida. Deseja-se verificar se há indícios de que a média // dessa população seja diferente de 100 cm. Para isso foi retirada uma amostra aleatória de tamanho9, que apresentou uma média igual a x, em cm, e um desvio padrão igual a 6 cm.
Foram formuladas as hipóteses Ho: // = 100cm (hipótese nula) e H^. // #= 100cm (hipótese alternativa), e o nível de significância considerado foi de 5%. Para testar a hipótese nula, utilizou- se o teste t de Student.
A tabela abaixo fornece valores de t₀j02s > 0, que representa o quantil da distribuição t de Student para n graus de liberdade, em que t₀i02s > 0 é o quantil da distribuição t deStudent tal que a probabilidade
P(t > to,025) = 0,025. Verificou-se que 0 valor que foi encontrado para x foi 0
menor valor tal que Ho não é rejeitada.
Dados:

Graus de Liberdade to,025
2,36

2,31

2,26

Então, x é igual a:

a) 95,48 cm b) 94,88 cm c) 95,28 cm d) 94,60 cm e) 95,38 cm
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A questão pede o valor de x, que é o menor valor para o qual a hipótese nula não é rejeitada, ou seja, o limite inferior da Região de Não Rejeição, calculado como:
s x = u - t x = u - t x —
Vn

Para isso, o enunciado apresenta os seguintes dados:

* Média da população (parâmetro sendo testado): // = 100 cm

* Desvio padrão amostrai: s = 6

* Tamanho da amostra: n = 9

Com base nessas informações, primeiro calculamos o valor do desvio padrão da média amostrai:

s 6 6

O valor crítico t deve ser obtido para n — 1 = 8 graus de liberdade. Pela tabela fornecida, observamos que t = 2,31. Logo, o valor mínimo é:
x = 100 - 2,31 x 2 = 100 - 4,62 = 95,38

Gabarito: E

Comparação das Médias de duas populações

O objetivo desse teste é comparar as médias de duas populações X₁ e X₂ independentes,
para verificar se as médias são iguais, isto é, correspondem à mesma população, ou não.
Vamos indicar as médias das duas populações X₁ e X₂ como ^e fi₂, respectivamente.

A hipótese nula é de que as médias são iguais (ou seja, de que se trata da mesma população):

Ho' Ui = H2

Isso é o mesmo que afirmar que a diferença entre as médias é nula:

Ho- Hi ~ H2 = 0

Por exemplo, uma empresa que tenha recebido 2 lotes de peças do seu fornecedor pode estar interessada em verificar se esses lotes são da mesma população. Para isso, a empresa irá extrair uma amostra de cada lote e calcular as médias amostrais, que indicamos por x{ e x^.
Nos testes bilaterais, estamos interessados em verificar se as médias das populações são iguais ou diferentes. Assim, as hipóteses nula e alternativa são as seguintes:
f//0: ? í#o: Hi ~ H2 = 0)

/z₂J kHi: Hi ~ H2 Oj

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nessa situação, vamos rejeitar a hipótese nula se a média amostrai da primeira população for muito menor do que a da segunda (xjj « xjj); ou se a média amostrai da primeira população for muito maior do que a da segunda população (x^ » xjf).
Por que estamos falando em muito maior ou muito menor? Porque a rejeição é a decisão forte. Assim,rejeitamos a hipótese nula se realmente tivermos forte indício de que ela seja falsa,
isto é, se o resultado do teste estiver na região crítica.
Nesse caso, a empresa cria um intervalo, como (—0,5; 0,5), para a diferença entre as médias amostrais de cada lote. Assim, se a empresa encontrar xf — x^< —0,5 ou xf — xf > 0,5, ela irá rejeitar os lotes.
Em outra situação, pode ser um problema para a empresa apenas se a média do primeiro lote for menor que a do segundo lote. Nessa situação, deve ser conduzido o teste unilateral à esquerda,cujas hipóteses nula e alternativa são as seguintes:
fH0: pr = ? (Ho: Pi ~ P2 = 0)
(Hi: < /z2J v^i: Pi ~ P2 < 0j

Nesse caso, a rejeição irá ocorrer apenas se a média amostrai da primeira população for muito menor do que a da segunda população (xf « x^).
Por exemplo, a empresa pode decidir rejeitar os lotes apenas sexf — x^< -0,5.

Por outro lado, pode ser um problema para a empresa apenas se a média do primeiro lote for maior que a do segundo lote. Assim, deve ser conduzido 0 teste unilateral à direita, cujas hipóteses nula e alternativa são as seguintes:
fH0: AÍ = ^2) (? (Ho: Pi ~ P2 = 0)

(Hi: > /z2J v^i: Pi ~ P2 > 0j

Nessa situação, a rejeição irá ocorrer apenas se a média amostrai da primeira população for muito maior do que a da segunda população (xf » xf).
Por exemplo, a empresa pode decidir rejeitar os lotes apenas sexf — x^> 0,5.

Se as populações X₁ e X₂ seguirem distribuições normais (ou se as amostras forem grandes 0 suficiente para que as médias amostrais sigam distribuições), com variâncias conhecidas, V(Xf) = of eV(X₂) = °2 > então a diferença das médias amostrais xf — xf também seguirá distribuição normal. Assim,utilizamos a seguinte transformação para a normal padrão:
valor da distribuição — média da distribuição z —
desvio padrão da distribuição

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O valor da distribuição é a diferença entre as médias amostrais:

valor da distribuição = x1— x2

A média da distribuição é a diferença entre as médias populacionais:

média da distribuição = Mi — M2

Como consideramos a hipótese nula, em que — /z₂ = 0/ então a média da distribuição é igual a zero:

média da distribuição = 0

A variância da diferença das médias amostrais — x₂ é dada pela soma das variâncias,
uma vez que as populações são independentes1:
- x₂) = K(xx) + V(x₂)

E a variância da média amostrai é a razão entre a variância populacional e 0 tamanho amostrai,
então:

7(Xi) oí

VX) =

1 nx

V(W =

7(X2) tf n2 n2
Em que Hi é 0 tamanho da amostra extraída da primeira população X₁ e n₂ é 0
tamanho da amostra extraída da segunda população X₂. Assim, a variância da diferença V(x\ — x^) é a soma, já que as amostras são independentes:
7(xi - x₂) = —+ —

Hl n2

Assim, 0 desvio padrão da distribuição é a raiz quadrada dessa variância:

desvio padrão da distribuição = = -JVÇx-^ - x₂) =

1 Quando as variáveis não são necessariamente independentes, as variâncias da soma e da diferença são dadas respectivamente por:
+ X2) = V(XJ + V(X2) + 2. CovÇXlfX2)
VÇX± - X2) = V(XJ + V(X2) - 2. CovÇX1,X2)

Em que CovÇX1,X2>) é a covariância entre as variáveis.

Pontue-se que, para variáveis independentes, a covariância é nula. Por esse motivo, a variância tanto da soma quanto da diferença de variáveis independentes equivale à soma das variâncias.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Dessa forma, considerando a hipótese nula, = 0, o valor da estatística do teste corresponde à transformação da diferença das médias amostrais x^ — x^ para a normal padrão:
X*Vl" 'V' Á2

'V 'V

Gxr-x2

2 2

^l + a2

5 ni n2

Essa estatística deve ser comparada ao valor crítico tabelado zc, considerando o nível de significância desejado e o tipo de teste (bilateral, unilateral à esquerda ou unilateral à direita).
Alternativamente, pode-se verificar se o resultado observado da diferença x±
- x₂ respeita o limite estipulado (ou os limites, no teste bilateral), considerando o valor crítico tabelado zc.
Para calcular os limites da diferença, podemos reorganizar a fórmula acima, isolando a diferença x^
— x^:

Assim, os limites da diferença terão o mesmo valor absoluto, apenas com sinais diferentes.

EXEMPLIFICANDO

Vamos considerar que a variância da primeira população seja c2 = 3 e da segunda população cr₂2 = 1; e que seja extraída uma amostra de tamanho nx = 18 da primeira população e outra de tamanho n₂ = 12 da segunda população.
A variância da média amostrai da primeira população é:

E da segunda população é:

A variância da diferença é a soma:

7(%I-XT) = 7(%z) + V(x^ = i + = ^ = _3_ 1

12 4

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E o desvio padrão da distribuição é a raiz quadrada desse resultado:

= y/V(xí-XÍ) =

Agora, vamos supor um nível de confiança 1 — a = 95% em um teste bilateral, em que zc = ±1,96 (pela tabela normal padrão).
Então, o valor limite para a diferença em módulo, é:

LD = zcx Oxí-xi = 1,96 x | = 0,98

Note que não precisamos conhecer as médias populacionais /.Q e fi₂, uma vez que a hipótese nula é de que a diferença seja nula.
FIQUE

ATENTO!

Se a questão fornecer os desvios padrão amostrais, -= e será necessário elevá-los ao

2 2

quadrado para obter as respectivas variâncias amostrais, — e —.

ni n2

Somente então, você poderá calcular a variância da diferença e, em seguida, obter o desvio padrão da diferença, pela sua raiz quadrada:
+

Não some os desvios padrão!

Oj | ^2

Se as populações seguirem distribuições normais (ou aproximadamente normais) com variâncias desconhecidas, utilizamos fórmulas similares, mas considerando a variância amostrai, no lugar da variância populacional; e a distribuição de t-Student, no lugar da distribuição normal:
xr-x2

^XÍ~X2

xr-x2

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

í (FGV/2019 - DPE-RJ) Suponha que para estimar e testar a diferença entre as médias de duas populações i
: cujas características são independentes sejam extraídas duas amostras. Os tamanhos de amostra são n = 36 ;
: e m = 64, para X e Y, respectivamente. Como resultado da seleção, chega-se a X =
20 e Y = 17. Além disso, j

= sabe-se que as variâncias populacionais são = 100-
i

: Em módulo, a estatística amostrai para fins de estimação e inferência é:
j

= a)

b)

c)

36/35

1,44

1,60

d) 0,48

e) 1,05

Comentários:

: O enunciado forneceu os seguintes dados:

: * Variâncias populacionais: = aY = 100;

I

: * Tamanhos das amostras nx = 36 enY = 64;

i * Valores observados: x = 20 e y = 17.

I

: Assim, as variâncias das médias amostrais são dadas por:

: (j3

: 7(%) = —

: nx

: v(y) =

í ny

100 25

~36

100 25

64 "16

= E a variância da diferença é a soma, já que as populações são independentes:

: 25
25 400 + 225 625
i V(x -y) = V(x) + V(y) = — + — =

= E o desvio padrão da diferença é a raiz quadrada:

Cx-y = ^V(x-y) =

144 144

|ó25 25

j 144 _ 12

Assim, a estatística do teste é a razão:

x — y 20-17 12

Gabarito: B.

Z =-------- -- = = 3 x — = 1,44

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ESQUEMATIZANDO

Testes para a Média

Variância conhecida:

Estatística do teste: z = °x Limites da Região Crítica: L =
p ± zc x-^=

Variância desconhecida:

Estatística do teste: t = Limites da Região Crítica: L
= [i + tc x-^=

Comparação de 2 populações:

Estatística do teste: z = Limites da Região Crítica: L = z x

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TESTES DE HIPóTESES PARA PRoPoRçõES

É possível utilizar o teste de hipóteses para proporções, aplicável para populações que seguem distribuições de Bernoulli (isto é, em que cada elemento é categorizado em sucesso ou fracasso),com proporção p desconhecida. Esse tipo de teste de hipóteses é bastante cobrado em provas.
Teste para a Proporção de uma População

Para iniciar o teste para a proporção, é feita uma suposição a respeito da proporção populacional p (hipótese nula), a qual será testada a partir da proporção amostrai observada p.
A estatística do teste também pode ser calculada utilizando-se a fórmula da transformação para a curva normal padrão para uma amostra suficientemente grande (isto é, uma aproximação que pode ser feita considerando-se o Teorema do Limite Central):
valor da distribuição — média da distribuição z —
desvio padrão da distribuição

O valor da distribuição corresponde à proporção p observada na amostra.
A média da distribuição é o parâmetro indicado na hipótese nula p.

Para calcular o desvio padrão da distribuição, precisamos da variância populacional, dada por:

7(p) = p.q

Em que q = 1 — p. Considerando que a variância da proporção amostrai corresponde à variância da proporção populacional dividida pelo tamanho da amostra, então a variância da proporção amostrai é dada por:
Em que n é o tamanho da amostra. Por fim, o desvio padrão da distribuição é a raiz quadrada:

Portanto, a estatística do teste é dada por:

z = ^ = ^fH

n

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por exemplo, vamos considerar uma grande empresa que alega ter o mesmo número de homens e mulheres dentre os seus colaboradores, ou seja, que a proporção de homens seja de 50% (hipótese nula):
H0:p = 0,5

Para testar essa hipótese, é extraída uma amostra de 100 colaboradores, dos quais 55 são homens. Aproporção encontrada na amostra é de:

p=lõõ=0'55

Para calcular a estatística desse teste, vamos primeiro calcular a variância da proporção amostrai. Sendo p =0,5 e, portanto, q = 1 — p = 0,5, a variância da proporção amostrai é a razão entre a variância populacional e o tamanho da amostra:
z x p. q 0,5 x 0,5

y(p) = ^-1 = = 0,0025

n 100

E o desvio padrão da proporção amostrai é a raiz quadrada:

o-p = = V°<0025 = 0,05

A estatística da amostra é dada por:

p —p 0,55 - 0,5 0,05

<jp 0,05 0,05

Também podemos utilizar essa mesma fórmula da transformação para calcular o limite da
Região Crítica (ou os limites, no caso do teste bilateral), considerando o valor crítico zc,para o nível de confiança (ou significância) desejado e o tipo de teste (bilateral ou unilateral). Reorganizando a fórmula para isolar o valor do limite para a proporção amostrai L:
L = p + z x

Nessa fórmula, o valor de z será positivo para obter um limite superior para a proporção amostrai e negativo para obter um limite inferior para a proporção amostrai.
Essas fórmulas pressupõem uma população infinita ou amostras extraídas com reposição. Caso a população seja finita e as amostras extraídas sem reposição, então será necessário aplicar o fator de correção para população finita. Para isso, devemos multiplicar a variância amostrai por j-:
N — n

N — 1

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TV—7l

0 teste para proporções também pode ser utilizado quando classificamos a população em

2 categorias, que podem ser representadas por sinais "+" e e desejamos fazer o teste para avaliar hipóteses formuladas a respeito da proporção desses sinais.
É comum chamar a estatística desse teste de escore reduzido.

HORAM

(CESPE/2018-ABIN) Em uma fábrica de ferragens, o departamento de controle de qualidade realizou testes na linha de produção de parafusos. Os testes ocorreram em dois campos: comprimento dos parafusos e frequência com que esse comprimento fugia da medida padrão. Historicamente, o comprimento médio desses parafusos é 3 cm, e o desvio padrão observado é 0,3 cm. Foram avaliadosItem. 10.000 parafusos durante uma semana. Desses, 1.000 fugiram às especificações técnicas da gerência: o comprimento do parafuso deveria variar de 2,4 cm a 3,6 cm. O chefe da linha de produção, porém, insiste em afirmar que, em média,4% da produção de parafusos fogem às especificações. O departamento de controle de qualidade assume que os comprimentos dos parafusos têm distribuição normal.
A partir dessa situação hipotética, julgue os itens subsequentes, considerando que 0(1)
= 0,841, 0(1,65) =
0,95, 0(2) = 0,975 e 0(2,5) = 0,994, em que O(z) é a função distribuição normal padronizada acumulada, e que 0,002 seja valor aproximado para
Com base nos dados apresentados, pode-se rejeitar, com significância de 5%, a afirmação do chefe da linha de Produção.
Comentários:

O enunciado informa que o chefe da linha de Produção afirma que 4% dos parafusos fogem às especificações:
H₀:p = 0,04

Considerando-se a hipótese nula (p = 0,04 e, portanto, q = 1 — p = 0,96), a variância da proporção da amostra extraída, de tamanho n = 10.000, é:
0,04 x 0,96

10.000

0,0384

10.000

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I: Logo, o desvio padrão da proporção amostrai, raiz quadrada da variância
(considerando a aproximação iI

: í

: indicada no enunciado * = 0,002) é:

Item. 10.000 '

i ffp = = J

10.000

: Agora, vamos calcular o valor de z, considerando o nível de significância a = 5% (logo, o nível de confiança
= é 1 — a = 95%). Note que o problema é a proporção de defeito superar a proporção indicada (se a

= proporção de defeito for menor, será ainda melhor para a empresa). Assim, temos um teste unilateral à direita, em que a hipótese alternativa é:

s

I

i Ou seja, precisamos do valor de z cuja função de distribuição acumulada é P(Z <
zc) = 0,95. Pela tabela i fornecida na questão, observamos que o valor crítico é zc = 1,65, pois P(Z <1,65) = 0,95. Portanto, a i proporção amostrai máxima para que a hipótese nula não seja rejeitada é:
L = p + zx<j^ = 0,04 + 1,65 x 0,002 = 0,04 + 0,0033 = 0,0433

= Porém, na amostra extraída pelo departamento de controle, observou-se que, de n =
Item. 10.000 parafusos, 1.000

; fugiam à especificação, ou seja, a proporção observada foi de:

1.000

j - 10.000 _ 0,1

: Por ser muito superior ao limite máximo da proporção amostrai aceitável, a hipótese nula deve ser rejeitada.

Ê Gabarito: Certo.

A

Teste para 2 Proporções

Existem testes de hipóteses cujo objetivo é comparar as proporções de 2 populações e
X₂ independentes,
considerando a mesma característica. Por exemplo, podemos verificar se a proporção de homens, dentre os colaboradores, de uma empresa A é a mesma proporção de outra empresa B.
A hipótese nula é de que as proporções sejam iguais, ou seja, pT = p₂. Já a hipótese alternativa depende do tipo do teste. Para testes bilaterais, temos as seguintes hipóteses nula e alternativa:
ítt0: Pi = Pz] (Ho- p1-p2 = 0]

{H1-.p1 -p2 #= 0)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para testes unilaterais à esquerda, temos as seguintes hipóteses nula e alternativa:

í#o: Pi = Pz] p₁-p₂ = Oj

{H1:p1<p2) lH1:p1-p2 < 0)

E para testes unilaterais à direita, temos as seguintes hipóteses nula e alternativa:

(Ho: p± = p2] (Ho: Pr - p2 = Oj

{H1:p1>p2) {H1:p1-p2>0)

Aproximando-se as proporções amostrais a distribuições normais (Teorema Central do Limite), então a diferença entre as proporções também seguirá distribuição normal. Dessa forma, a estatística do teste será calculada pela mesma transformação para a normal padrão:
valor da distribuição — média da distribuição z —
desvio padrão da distribuição

O valor da distribuição corresponde à diferença entre as proporções amostrais:

valor da distribuição = pi — pi

A média da distribuição é a diferença entre as proporções populacionais:

média da distribuição = Pr —p₂

Como consideramos a hipótese nula, em que Pr—p₂= 0, então a média da distribuição é igual a zero:
média da distribuição = 0

A variância da diferença das médias amostrais V(pi — p₂) é dada pela soma das variâncias,
uma vez que as populações são independentes:
V(pi - Pz) = V(.Pi) + ^(Pz)

A variância da média amostrai é a razão entre a variância populacional e o tamanho amostrai. Considerando,ainda, que a variância populacional é 7(p) = p. q, em que q = 1 — p:

Pi-Qi p-q p2.q2 p.q n2 n2
Em que HX é o tamanho da amostra extraída da primeira população e n₂ é o tamanho da amostra extraída da segunda população X₂. Assim, a variância da diferença V(p^ — p^) é a soma:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

E o desvio padrão da distribuição é a raiz quadrada da variância:

desvio padrão da distribuição = o^-p., = V^(Pi P2) =

p.Q , p-q

Ul P2

Dessa forma, considerando a hipótese nula, pr — p = Q, o valor da estatística do teste é:

z = P1-P2 P1-P2

aPl-P2 «1 n

Para ilustrar, vamos considerar a nossa empresa (A), que alegou que a proporção de homens é de 50%, bem como uma segunda empresa (B) com a mesma alegação. Para testar tais alegações,aplicaremos 0 teste comparando essas duas populações. Para isso, extraímos uma amostra de 200colaboradores de cada empresa, tendo encontrado 110 homens da empresa A e 90 homens da empresa B.
A variância dessa distribuição Víp^ — p₂) é dada por:

E 0 desvio padrão é a raiz quadrada:

= V0'0025 = °-05

A diferença entre as proporções amostrais observadas é:

110 90

P'-f'2=2ÕÕ-2ÕÕ = 0'55-0'45 = 0'1

Portanto, a estatística desse teste é:

Pi ~ P2 0,1

z = = ——— = 2

^Pi~ P2 0,05

Esse valor pode ser comparado ao valor crítico zc, obtido com base no nível de confiança (ou significância)desejado e 0 tipo de teste (bilateral ou unilateral). Também podemos utilizar essa mesma fórmula para calcular os limites para as diferenças das proporções. Reorganizando a fórmula, para isolar a diferença p^ —
temos:

PT - x ari_r2

Para estipular um limite superior, 0 valor crítico zc será positivo e para estipular um limite inferior, 0 valor crítico zc será negativo.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

P-VALoR

O p-valor, também denominado nível descritivo ou probabilidade de significância, é uma outra forma de analisar o resultado do teste de hipóteses, para decidirmos se vamos aceitar ou rejeitar a hipótese nula, em vez do nível de significância a.
O p-valor é a probabilidade de obter um valor mais extremo ou igual ao resultado observado, considerando a hipótese nula como verdadeira. Em seguida, comparamos o p-valor com o nível de significância a para decidir se vamos rejeitar ou não a hipótese nula.
Vamos supor que estejamos testando a hipótese nula Ho-, /j. = 2 em um teste unilateral à esquerda e que a média amostrai observada tenha sidoX = 1,85.
Sabendo que o p-valor é a probabilidade de obter um valor mais extremo ou igual,
neste caso, ele é a probabilidade de obter um valor igual ou inferior a X = 1,85, pelo fato de a região crítica estar à esquerda:
p-valor

X = 1,85 M = 2

Se o p-valor for menor que o nível de significância a, então o resultado do teste está na região crítica e a hipótese nula deve ser rejeitada. Caso contrário, a hipótese nula não é rejeitada.
TOME

NOTA!

p-valor < a Rejeitar HQ

p-valor > a Não Rejeitar Ho

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Essa análise é chamada de análise da significância estatística e pode ser realizada para qualquer tipo de teste de hipóteses.
Quando p < a, ou seja, quando a hipótese é rejeitada, dizemos que o resultado é estatisticamente significante ou que há significância estatística (ou, ainda, evidência estatística).
Para calcular o p-valor do resultado observado (no caso, X = 1,85), primeiro calculamos a estatística do teste. Tratando-se de um teste para a média de uma população normal com variância conhecida (Teste Z),fazemos:

x — /z z = 7V^n"
No nosso exemplo, temos x = 1,85 e /z = 2. Supondo que a variância populacional é cr = 1 e que o tamanho da amostra seja n = 100, a estatística do teste é:
x —/z 1,85-2 —0,15 —0,15

z = = i = "X" = "õT" = _1'5

7 VTõõ 10

Agora, para calcular o p-valor, recorremos à tabela normal padrão. A tabela inserida parcialmente a seguir apresenta a probabilidade P(0 < Z < z), como ilustrado no gráfico anterior à tabela.
z 0,00 0,01 0,02 0,03 0,04 0,05
0,06 0,07 0,08 0,09

1,4

1,5

1,6

0,4192 0,4207 0,4222 0,4236 0,4251 0,4265 0,4279
0,4292 0,4306 0,4319

0,4332 0,4345 0,4357 0,4370 0,4382 0,4394 0,4406
0,4418 0,4429 0,4441

0,4452 0,4463 0,4474 0,4484 0,4495 0,4505 0,4515
0,4525 0,4535 0,4545

Podemos observar que P(0 < Z < 1,5) = 0,4332. Pela simetria da normal padrão, temos:

P(—1,5 < Z < 0) = 0,4332

E a probabilidade de P(Z < —1,5) é dada pela diferença:

P(Z < -1,5) = P(Z < 0) - P(-l,5 < Z < 0) = 0,5 - 0,4332 = 0,0668

p = 6,68%

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, se o nível de significância for a = 5%, teremosp > ae, então, não rejeitaremos a hipótese nula:
Porém, se o nível de significância for a = 10%, teremos p < a,e devemos rejeitar a hipótese nula.

Essa regra de rejeição da hipótese nula se p < a ou não, caso contrário, vale para todos os tipos de teste(bilateral, unilateral à esquerda ou unilateral à direita). A diferença está na região associada ao p-valor.
Para o teste unilateral à direita, o p-valor é a probabilidade de se observar um valor maior que o resultado observado, porque a região crítica está à direita:
E para o teste bilateral, o p-valor se refere aos dois extremos.

Considerando o mesmo exemplo em que a estatística do teste foi zt =
-1,5, o p-valor é a soma das probabilidades P(Z < —1,5) e P(Z > 1,5):
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considerando a simetria da distribuição normal, as probabilidades P(Z < -zt)
e P(Z > zt) são iguais e,
assim, o p-valor em um teste bilateral considerando será o dobro do p-valor em um teste unilateral, para essa distribuição.
HORAM

i (2019 - Prefeitura de Cruzeiro do Sul/AC - Adaptada) Com relação a Testes de
Hipóteses realizados sobre i

; uma amostra que nos auxiliam a aceitar ou rejeitar uma hipótese estatística, julgue a afirmativa a seguir.

: Se um teste de hipótese tiver valor-p associado igual a 0,02, podemos rejeitar a hipótese nula com nível de i
; significância a 5%, mas não a rejeitaríamos a um nível de significância de 0,1%.
;

; Comentários:

I

A hipótese nula deve ser rejeitada se p-valor < nível de significância a.

I

i Sendo p-valor = 0,02 = 2%, então se a = 5%, teremos:

; p-valor < a
;

I

j Nesse caso, rejeitamos a hipótese nula.

I

I

: E se a = 0,1%, teremos:
j

: p-valor > a
;

I

j Nessa situação, não rejeitamos a hipótese nula. Portanto, a afirmativa está correta.

I

I

Ê Resposta: Certo.

I

I

i (CESPE/2017-TCE/PE) Para avaliar se a proporção p de itens defeituosos enviados por um fornecedor estava i
; acima do valor pactuado de 0,025, um analista, a partir de uma amostra aleatória de itens enviada por esse i j fornecedor, testou a hipótese nula H₀-.p < 0,025 contra a hipótese alternativa H^.p > 0,025, utilizando i i nível de significância a = 1%.

A respeito dessa situação hipotética, julgue o seguinte item.
;

I

j Caso o P-valor do teste efetuado pelo analista seja igual a 0,005, é correto concluir que a afirmação proposta i
= na hipótese nula seja verdadeira.

I

i Comentários:

I

j Para sabermos se devemos rejeitar ou não a hipótese nula, devemos comparar o p-valor e o nível de i
= significância a.
j

I

I

: O enunciado informa que a = 1% e o item informa que p-valor = 0,005 = 0,5%. Ou seja, temos:

I

I

: p-valor < a i
I

I

: Portanto, devemos rejeitar a hipótese nula, isto é, concluir que ela é falsa.

I

: Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

(FGV/2019 - DPE-RJ - Adaptada) A respeito da formulação, execução, decisão e critérios de avaliação de testes de hipóteses, julgue as afirmativas a seguir:
O p-valor de um teste é o maior valor para o nível de significância a partir do qual a hipótese nula não poderá ser rejeitada.
Comentários:

O item afirma que o p-valor é o maior valor para o nível de significância.

Porém, o p-valor é a probabilidade de obter um resultado tão ou mais extremo que o valor observado no teste. Ou seja, ele não define limite algum. Por isso, o item está errado.
Resposta: Errado.

(2019 - Instituto de Desenvolvimento Agropecuário/AM - Adaptada) Sobre testes de significância, julgue a afirmativa abaixo.
Em testes de hipóteses estatísticos, diz-se que há significância estatística ou que o resultado é estatisticamente significante quando o p-valor observado é menor que o nível de significância definido para o estudo.
Comentários:

O teste é dito estatisticamente significante quando p-valor < a, isto é, quando rejeitamos a hipótese nula,com base no p-valor calculado.

Resposta: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Conceitos Fundamentais

Item. 1. (Cebraspe/2019 - TJ-AM) A respeito dos testes de hipóteses, julgue o próximo item.

Sendo a o nível de significância de um teste estatístico, seu valor será sempre constante em 0,05.

Comentários:

O valor de a, isto é, o nível de significância, equivale à probabilidade de se rejeitar a hipótese nula, sendo ela verdadeira. Como uma probabilidade, a pode assumir qualquer valor entre 0 e 1, embora seja normalmente abaixo de 10%
Gabarito: Errado.

Item. 2. (CESPE/2011 - STM) Acerca dos conceitos de estatística e dos parâmetros estatísticos,
julgue o item seguinte.
A estatística descritiva permite testar hipóteses a respeito da população de interesse.

Comentários:

O teste de hipóteses pertence à Estatística Inferencial (ou Dedutiva), e não à Estatística
Descritiva.

Gabarito: Errado.

Item. 3. (CESPE/2011 - STM) Acerca dos conceitos de estatística e dos parâmetros estatísticos,
julgue o item seguinte.
Em estatística, parâmetro pode ser uma quantidade desconhecida da população-alvo,
à qual não se tem acesso diretamente, mas que se deseja estimar ou a respeito da qual se deseja avaliar hipóteses.
Comentários:

De fato, parâmetro é uma quantidade desconhecida da população sendo estudada, que se deseja estimar(estimação intervalar) ou avaliar hipóteses (teste de hipóteses).

Gabarito: Certo.

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 4. (Cebraspe/2015 - Telebras) Com relação às técnicas de amostragem estatística,
julgue o próximo item.
Considerando as informações colecionadas em uma amostra, a metodologia do teste de hipóteses tem o objetivo de determinar a possibilidade de a hipótese nula ser verdadeira, uma vez que é indissolúvel a relação entre a declaração da hipótese nula e a especificação da hipótese alternativa, sendo esta necessariamente verdadeira caso a hipótese nula seja falsa.
Comentários:

O objetivo do teste de hipóteses é, de fato, decidir se a hipótese nula é verdadeira ou falsa. Se a hipótese nula for considerada falsa, então a hipótese alternativa será necessariamente verdadeira.
Gabarito: Certo.

Item. 5. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.Um teste t de Student foi aplicado com a hipótese nula Ho: PA = pp e a hipótese alternativa Hi: pA
> pp, em que PA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

As hipóteses do teste t de Student aplicado são simples.

Comentários:

A hipótese alternativa do teste é pA > pp, que é uma hipótese composta, uma vez que não especifica os parâmetros.
Gabarito: Errado

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (Cebraspe/2015-Telebras)

valor esperado, p
(em kg)

desvio padrão a

(em kg)

Japão 100 15

Taiwan 110 20

Um varejista de motocicletas e acessórios encontrou uma caixa de parafusos especiais de origem desconhecida para um modelo da marca Honda. Esses parafusos são produzidos apenas noJapão e
Taiwan. As características da resistência à tração X dos parafusos são apresentadas na tabela. Uma amostra de 20 parafusos da caixa foi testada e encontrou-se a resistência à tração média x.
Considere o teste a respeito da procedência dos parafusos constituído das seguintes hipóteses. Ho: os parafusos procedem do Japão: p = 100; e Hi: os parafusos procedem de Taiwan: p = 110. A regra da decisão do teste é não rejeitar Ho se x < xc, em que xc é um valor a ser encontrado; e rejeitar Ho no caso contrário.A respeito dessa situação, julgue o item subsequente.

O teste descrito é um teste de hipóteses composto.

Comentários:

Hipóteses compostas são aquelas que não especificam o parâmetro, por exemplo, p < 100
ou p > 100,
enquanto as hipóteses simples são aquelas que especificam, por exemplo, /z = 100.
Nessa questão, tanto a hipótese nula quanto a hipótese alternativa especificam o parâmetro, portanto,ambas são hipóteses simples.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Tipos de Erros

Item. 1. (Cebraspe/2018 - IJSN-ES) Considerando os conceitos associados a probabilidade e estatística,julgue o item.

A hipótese nula (Ho) é a afirmação feita acerca do valor de um parâmetro populacional e o erro tipo I ocorre quando a hipótese nula é falsa e não é rejeitada.
Comentários:

A hipótese nula, de fato, trás uma afirmação acerca do valor de um parâmetro populacional, mas o erro tipoI (com probabilidade a) ocorre quando rejeitamos a hipótese nula sendo ela verdadeira.
O evento de não rejeitar a hipótese sendo ela falsa é o erro tipo II (com probabilidade /?).
Gabarito: Errado.

Item. 2. (Cebraspe/2016 - TCE-PAM) Uma amostra aleatória, com n = 16 observações independentes e identicamente distribuídas (IID), foi obtida a partir de uma população infinita, com média e desvio padrão desconhecidos e distribuição normal. Tendo essa informação como referência inicial,julgue o seguinte item.
A potência de um teste de hipóteses corresponde à probabilidade de se rejeitar a hipótese nula, dado que a hipótese nula é correta.
Comentários:

A potência do teste, 1 - /?, corresponde à probabilidade de rejeitar a hipótese nula dado que ela é falsa.Gabarito: Errado.

Item. 3. (Cebraspe/2016 - TCE-PR) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0. Considerando que a amostra {0,1,1, 0, 0,1,
0,1, 0,1,1, 0, 0,1,
1, 0,1,1,1,1} foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

O poder do teste pode ser facilmente calculado pelo complementar do erro tipo II (/3).

Comentários:

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

De fato, o poder do teste é 1 - /3, isto é, o complementar da probabilidade do erro tipo II.

Gabarito: Certo.

Item. 4. (CESPE/2011 - STM) Julgue os itens que se seguem, acerca de definições da teoria estatística.
O erro do tipo II de um teste de hipóteses ocorre quando se rejeita uma hipótese nula que é verdadeira.
Comentários:

O erro tipo II corresponde à situação em que se rejeita a hipótese nula, sendo ela falsa.

Gabarito: Errado.

Item. 5. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.Um teste t de Student foi aplicado com a hipótese nula Ho: |JA = |ip e a hipótese alternativa Hi:
pA > pp, em que PA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

A função poder do teste, n(pA - pp), assume o valor n(0) = 0,03.

Comentários:

O poder do teste é o complementar do erro tipo II, 1 —/?, e corresponde à probabilidade de rejeitar a hipótese nula, sendo ela falsa. Para calculá-lo, precisamos da distribuição do verdadeiro parâmetro pA - pp,o que não foi dado no enunciado.

Ademais, sendo pA - pp = 0, como descrito no item, concluímos que a hipótese nula é verdadeira. Nessa situação, a probabilidade de rejeitar a hipótese nula sendo ela falsa é nula, pois sabemos que a hipótese nula não é falsa.
Gabarito: Errado.

Item. 6. (Cebraspe/2013 - FUB) No que se refere a testes de hipóteses, julgue o item subsecutivo.

O poder de um teste tende a diminuir à medida que o nível de significância decresce.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Quando o nível de significância a diminui, a região crítica diminui, assim como a probabilidade de rejeitar a hipótese nula. Dessa forma, o poder do teste também diminui.
Gabarito: Certo.

Item. 7. (Cebraspe/2013 - FUB) No que se refere a testes de hipóteses, julgue o item subsecutivo.

O tamanho amostrai influencia o poder do teste e o nível de significância.

Comentários:

O tamanho amostrai influencia o poder do teste, mas não o nível de significância do teste, que precisa estar previamente definido.
Gabarito: Errado.

Item. 8. (CESPE/2012 - ANAC) Consoante a teoria de testes de hipóteses, julgue os próximos itens.
Em um teste de hipóteses para se comparar duas médias amostrais, o tamanho amostrai é um fator importante, pois, à medida que o tamanho da amostra aumenta, a probabilidade do erro de tipo I (nível de significância do teste) tende a diminuir.
Comentários:

O tamanho da amostra não influencia no nível de significância do teste;
este precisa estar previamente definido.
Gabarito: Errado.

Item. 9. (CESPE/2010 - FUB - Estatístico) Julgue o próximo item, referente à inferência estatística.
No teste de hipóteses Ho: p. = /j.o contra Hi: /z =# /z₀, em que os dados são provenientes de uma distribuição normal com variância conhecida, se a probabilidade de ocorrência do erro tipo I (a)for 5%, a probabilidade de ocorrer o erro tipo II (/3) é igual a 20%.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para obter o valor de fí, precisamos conhecer o verdadeiro parâmetro, o qual não foi fornecido. Logo, não é possível afirmar que /3 = 20% a partir dos dados do enunciado.
Gabarito: Errado.

Item. 10. (Cebraspe/2020 - TJ-PA) O teste de hipóteses se assemelha ao julgamento de um crime. Em um julgamento, há um réu, que inicialmente se presume inocente. As provas contra o réu são, então,apresentadas, e, se os jurados acham que são convincentes, sem dúvida alguma, o réu é considerado culpado. A presunção de inocência é vencida. Michael Barrow. Estatística para economia,contabilidade e administração. São Paulo: Ática, 2007, p. 199 (com adaptações).
João foi julgado culpado pelo crime de assassinato e condenado a cumprir pena de 20 anos de reclusão.Após 10 anos de prisão, André, o verdadeiro culpado pelo delito pelo qual João fora condenado,
confessou o ilícito e apresentou provas irrefutáveis de que é o verdadeiro culpado,exclusivamente. Considerando a situação hipotética apresentada e o fragmento de texto anterior, julgue os itens que se seguem.
I Pode-se considerar que a culpa de João seja uma hipótese alternativa.

II No julgamento, ocorreu um erro conhecido nos testes de hipótese como erro do tipo I.

III Se a hipótese nula fosse admitida pelos jurados como verdadeira e fosse efetivamente
João o culpado pelo crime, o erro cometido teria sido o chamado erro do tipo II.
Assinale a opção correta a) Apenas o item I está certo.
b) Apenas o item II está certo.

c) Apenas os itens I e III estão certos.

d) Apenas os itens II e III estão certos.

e) Todos os itens estão certos.

Comentários:

O enunciado traça um paralelo entre o teste de hipóteses e o julgamento de um réu, pontuando que inicialmente presume-se que o réu é inocente, sendo este considerado culpado apenas se as provas forem fortes o suficiente. Com base nessa premissa, podemos considerar a inocência do réu como hipótese nula, a qual será rejeitada apenas se houver evidência estatística (isto é, se o resultado estiver na região crítica).
Em seguida, o enunciado afirma que João foi julgado culpado por um crime e cumpriu pena por isso. Porém,na verdade, André era exclusivamente culpado por esse crime (ou seja, João era inocente, na realidade).
Agora, vamos analisar os itens.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação ao item I, de fato, consideramos a culpa de um réu como hipótese alternativa (a qual será aceita somente se houver fortes evidências). Logo, o item I está correto.
Em relação ao item II, vimos que João foi considerado culpado injustamente, ou seja,
a hipótese nula foi rejeitada, sendo ela verdadeira. Essa é a definição do erro tipo I, logo, o item II está correto.
Em relação ao item III, se a hipótese nula fosse admitida como verdadeira, então João teria sido absolvido.Se João fosse o real culpado pelo crime, ele teria sido considerado inocente injustamente, ou seja, a hipótese nula não seria rejeitada, sendo ela falsa. Essa é a definição do erro tipo II, logo, o item IIIestá correto.

Gabarito: E

Item. 11. (Cebraspe/2017 - TCE-PE) Para avaliar se a proporção p de itens defeituosos enviados por um fornecedor estava acima do valor pactuado de 0,025, um analista, a partir de uma amostra aleatória de itens enviada por esse fornecedor, testou a hipótese nula Ho: p < 0,025 contra a hipótese alternativa Hi: p
> 0,025, utilizando nível de significância a = 1%. A respeito dessa situação hipotética, julgue o seguinte item.
O nível de significância representa a probabilidade de se aceitar a hipótese Ho: p <
0,025 quando, na verdade,
a proporção p for superior a 0,025.

Comentários:

O nível de significância representa a probabilidade de rejeitar a hipótese nula (Ho: p
< 0,025) quando ela é verdadeira. A probabilidade de aceitar a hipótese nula quando ela é falsa,como descrito no item, é a probabilidade do erro tipo II (/3).
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Testes para a Média

Item. 1. (Cebraspe/2019 - TJ-AM) Um pesquisador deseja comparar a diferença entre as médias de duas amostras independentes oriundas de uma ou duas populações gaussianas. Considerando essa situação hipotética, julgue o próximo item.
Para que qualquer teste possa ser realizado, as amostras devem ter distribuição normal.

Comentários:

Os testes de hipóteses para a média podem considerar a distribuição normal,
quando a variância populacional é conhecida, ou a distribuição de t-Student, quando a variância populacional é desconhecida,caso em que ela é estimada a partir da amostra. Logo, não há necessidade de as amostras terem distribuição normal.
Gabarito: Errado.

Item. 2. (Cebraspe/2019 - TJ-AM) Um pesquisador deseja comparar a diferença entre as médias de duas amostras independentes oriundas de uma ou duas populações gaussianas. Considerando essa situação hipotética, julgue o próximo item.
Para que a referida comparação seja efetuada, é necessário que ambas as amostras tenham N > 30.

Comentários:

Para amostras de tamanho n > 30, podemos aproximar a distribuição da média amostrai a uma distribuição normal, independentemente da distribuição da população. Porém, nesse caso, isso não é uma condição necessária para o teste.
Inclusive, como as populações são normais (gaussianas), a média da amostra
(independentemente do seu tamanho) seguirá distribuição normal se a variância populacional for conhecida ou distribuição de t-Student se a variância populacional for desconhecida, estimada a partir da variância amostrai.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 3. (Cebraspe/2019 - TJ-AM) Um pesquisador deseja comparar a diferença entre as médias de duas amostras independentes oriundas de uma ou duas populações gaussianas. Considerando essa situação hipotética, julgue o próximo item.
Caso o pesquisador realize um teste t de Student e encontre um valor de p = 0,95,
considerando-se a = 0,05,
será correto concluir que ambas as amostras provêm da mesma população.

Comentários:

Caso o p-valor do teste seja p = 0,95, então, para um nível de significância a =
0,05, então temos p > a e, por isso, não rejeitamos a hipótese nula de que as médias das populações são iguais, =jU₂- Com isso, conclui-
se que se trata da mesma população.

Gabarito: Certo.

Item. 4. (Cebraspe/2016 - FUNPRESP)

O gráfico ilustra cinco possibilidades de fundos de investimento com suas respectivas rentabilidades.Considerando que as probabilidades de investimento para os fundos A, B, C e D sejam,
respectivamente,
P(A) = 0,182; P(B) = 0,454; P(C) = 0,091; e P(D) = 0,182, julgue o item abaixo.

Se os cinco fundos de investimento representarem uma amostra de todos os fundos de investimento disponíveis no mercado financeiro, então o teste Z com 4 graus de liberdade poderá ser utilizado para verificar se a rentabilidade média de todos os fundos é maior que um valor especificado, considerando-se que os dados seguem uma distribuição normal.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

No teste Z, que considera a distribuição normal, não há que se falar em graus de liberdade. Ademais, não sendo conhecida a variância populacional, deve-se utilizar a distribuição t-Student,ainda que a distribuição da população seja normal.
Gabarito: Errado.

Item. 5. (Cebraspe/2013 - ANCINE) Em relação aos métodos de inferência estatística, julgue o item subsequente.
Em um teste de hipóteses para a média de uma distribuição (Ho: p = po), a razão x-p0
em que o denota o desvio padrão populacional, x é a média x amostrai e n representa o tamanho de uma amostra, segue uma distribuição normal padrão, desde que a distribuição populacional seja normal.
Comentários:

A média amostrai segue distribuição normal se a população seguir distribuição normal,
mas também se a população não seguir essa distribuição e a amostra for grande suficiente.
Gabarito: Errado.

Item. 6. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.
Um teste t de Student foi aplicado com a hipótese nula Ho: PA = pp e a hipótese alternativa Hi: pA
> pp, em que pA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

Caso fosse calculado um intervalo de confiança bilateral para pA- pp, com coeficiente de confiança 95%, tal intervalo conteria o valor zero.
Comentários:

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em um teste bilateral, o nível de significância seria a= 0,025 de cada lado. Assim,
sendo o resultado do teste t tal que p-valor = P(T > t) = 0,03, então o resultado está na região de não rejeição, como ilustrado abaixo:
Isso significa que o intervalo de confiança bilateral construído a partir do resultado do teste, para o mesmo nível de confiança, conteria a hipótese nula, qual seja, o valor pA - pp = 0.
Gabarito: Certo

Item. 7. (Cebraspe/2015 -Telebras) Um analista da TELEBRAS, a fim de verificar o tempo durante o qual um grupo de consumidores ficou sem o serviço de Internet do qual eram usuários,selecionou uma amostra de 10 consumidores críticos. Os dados coletados, em minutos, referentes a esses consumidores foram listados na tabela seguinte.
consumidor tempo (cm minutos)
C| c2

8 2

c3 C4 c5

3 5 7

Q c7 C8

7 10 9

c9 C]o

4 5

Com base nessa situação hipotética, julgue o item subsequente.

Para verificar se o tempo médio sem Internet é igual a 5 minutos, o analista deverá realizar um teste com 8graus de liberdade.

Comentários:

Sendo desconhecida a variância da população, deve-se utilizar a distribuição de t-Student com n - 1 graus de liberdade. Como a amostra tem tamanho n = 10, então o teste terá 9 graus de liberdade (não 8).
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 8. (Cebraspe/2015 - FUB - Estatístico) O tempo, X, de carregamento de um celular segue uma distribuição normal com média e variância desconhecidas. Foi coletada uma amostra de tamanho igual a10, em que a média amostrai é de 58 minutos e o desvio padrão da amostra é de 5 minutos. O
fabricante do celular, para testar se a média de carregamento é de 50 minutos, aplica um teste t de Student com a hipótese nula Ho: px = 50 contra a hipótese alternativa de Hi: px.^ 50.
Considerando a situação hipotética descrita, julgue os itens a seguir.

58 ^7S, 58 H—em que za é o a-quantil da distribuição Normal.
Comentários:

O enunciado informa que a variância da população é desconhecida, sendo fornecida o desvio padrão da amostra. Nessa situação, precisamos utilizar a distribuição de t-Student para construir o intervalo de confiança, e não a distribuição normal, como descrito no item. Por esse motivo, o item está errado.
Gabarito: Errado.

Item. 9. (Cebraspe/2015 - FUB - Estatístico) O tempo, X, de carregamento de um celular segue uma distribuição normal com média e variância desconhecidas. Foi coletada uma amostra de tamanho igual a
10, em que a média amostrai é de 58 minutos e o desvio padrão da amostra é de 5 minutos. O
fabricante do celular, para testar se a média de carregamento é de 50 minutos, aplica um teste t de Student com a hipótese nula Ho: px = 50 contra a hipótese alternativa de Hi: px.^ 50.
Considerando a situação hipotética descrita, julgue os itens a seguir.

O teste t de Student realizado pelo fabricante é inválido, pois a amostra não é suficientemente grande.
Comentários:

Não há tamanho mínimo para realizar o teste t de Student. Na verdade, a situação é justamente o contrário:caso o fabricante utilizasse a distribuição normal, o teste seria inválido pelo fato de a amostra não ser grande o suficiente.
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 10. (Cebraspe/2016 - TCE-PR) Em um teste estatístico para a média populacional fi com nível de significância a = 5% a hipótese nula Ho deverá ser rejeitada se X > 30 ou X < 10,em que X denota a média amostrai. Supondo que a variância populacional seja conhecida e que o tamanho da amostra seja igual a 10, assinale a opção correta.
a) A hipótese alternativa do teste é Hi: X #= 20.

b) O teste é bilateral.

c) Sob a hipótese nula, P(X > 30) = 0,05

d) Trata-se de um teste t de Student com 10 graus de liberdade.

e) A hipótese nula desse teste é Ho: p. = 10 ou = 30

Comentários:

O enunciado não descreve a hipótese nula, mas diz que ela será rejeitada se a média amostrai observada for
X > 30 ou X < 10, considerando um nível de significância a = 5%.

Em relação à alternativa A, a hipótese nula e alternativa se referem ao parâmetro populacional, no caso Ju, e não a X. Por isso, a alternativa A está incorreta.
Em relação à alternativa B, como a hipótese nula será rejeitada tanto para valores muito pequenos de X(X < 10) quanto para valores muito grandes (X > 30), então podemos concluir que o teste é bilateral(alternativa B correta).

Em relação à alternativa C, por se tratar de um teste bilateral, o nível de significância é dividido em ambas as regiões críticas:
Logo, a probabilidade P(X > 30) = 0,025. Por isso, a alternativa C está incorreta.

Em relação à alternativa D, como a variância populacional é conhecida, utiliza-se a distribuição normal, não a de t-Student (alternativa incorreta).
Em relação à alternativa E, a hipótese nula não pode ser /z = 10 ou = 30, pois isso não permitiria rejeitar a hipótese nula para X > 30 ou X < 10, a um nível de significância a = 5%.
Gabarito: B.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 11. (Cebraspe/2018 - PF) O tempo gasto (em dias) na preparação para determinada operação policial é uma variável aleatória X que segue distribuição normal com média M, desconhecida, e desvio padrão igual a 3 dias. A observação de uma amostra aleatória de 100 outras operações policiais semelhantes a essa produziu uma média amostrai igual a 10 dias.
Com referência a essas informações, julgue o item que segue, sabendo que P(Z > 2) =
0,025, em que Z
denota uma variável aleatória normal padrão.

Considerando-se o teste da hipótese nula Ho: M < 9,5 dias contra a hipótese alternativa Hi: M > 9,5 dias,adotando-se o nível de significância igual a 1%, não haveria evidências estatísticas contra a hipótese Ho.
Comentários:

O enunciado informa que a população segue distribuição normal, com desvio padrão <7 =
3 dias; que em uma amostra de tamanho n = 100 operações, a média amostrai encontrada foi x = 10.Sabendo que a média amostrai segue distribuição normal e que a hipótese nula é de que a média seja menor ou igual a M = 9,5,então a estatística do teste é:

x — M 10 -9,5 0,5 0,5

Z _ ~ 3 J 1,67

Vn VTõõ 10

Como o teste é unilateral à direita, precisamos comparar o nível de significância fornecido a = 1% com a probabilidade P(Z > 1,67), que corresponde ao p-valor do teste. O enunciado não forneceu essa probabilidade, mas informou que P(Z > 2) = 0,025 = 2,5%. Com isso, concluímos que o p-valor é maior que2,5%:

P(Z > 1,67) > 2,5%

Como o p-valor é maior que o nível de significância a = 1%, então não rejeitamos a hipótese nula, ou seja,concluímos que não há evidência estatística contra a hipótese nula.

Gabarito: Certo.

Item. 12. (Cebraspe/2016 - TCE-PR) A respeito de uma amostra de tamanho n = 10,
com os valores amostrados {0,10, 0,06, 0,10, 0,12, 0,08, 0,10, 0,05, 0,15, 0,14, 0,11}, extraídos de determinada população,julgue o item seguinte.

Para um teste Z ou t de Student bilateral (com pelo menos 9 graus de liberdade),
uma estatística do teste menor que 1,5 é considerada não significativa para o nível de significância de 5%.
Comentários:

Em um teste bilateral, com nível de significância a = 5%, temos as seguintes regiões críticas e de não rejeição:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sabemos que para esse teste temos zc = 1,96, pois P(Z < 1,96) = 0,975. Ou seja, o resultado de 1,5 está na região de não rejeição, para uma distribuição normal.
Já a distribuição de t-Student tem maior variabilidade, sendo mais achatada no centro.
Consequentemente,
é preciso de um intervalo ainda maior para conter um nível de confiança de 1 - a =
95%. Ou seja, os valores da tabela de t-Student superam os valores da tabela normal para um mesmo nível de confiança/significância.Assim, o resultado de 1,5 também está na região de não rejeição para a distribuição de t-Student.

Assim, para uma estatística de 1,5 não rejeitamos a hipótese nula e, por isso, ela é chamada de não significativa.
Gabarito: Certo.

Item. 13. (Cebraspe/2016 - TCE-PR) A respeito de uma amostra de tamanho n = 10,
com os valores amostrados {0,10, 0,06, 0,10, 0,12, 0,08, 0,10, 0,05, 0,15, 0,14, 0,11}, extraídos de determinada população,julgue o item seguinte.

Dado que a variância populacional é desconhecida e os dados seguem uma distribuição normal, é correto afirmar que o teste t para a média populacional possui 10 graus de liberdade.
Comentários:

Sendo a variância populacional desconhecida, utilizamos a distribuição de t-Student com n - 1 graus de liberdade, em que n é o tamanho da amostra. Assim, para n = 10, o teste possui n -1 = 9 graus de liberdade.
Gabarito: Errado.

Item. 14. (Cebraspe/2014 - TJ-SE) Com o propósito de produzir inferências acerca da proporção populacional
(p) de pessoas satisfeitas com determinado serviço oferecido pelo judiciário brasileiro,
foi considerada uma pequena amostra de 30 pessoas, tendo cada uma de responder 1, para o caso de estar satisfeita,ou
0, para o caso de não estar satisfeita. Os dados da amostra estão registrados a seguir.

000110100000100010001100010001

Com base nessas informações, julgue os itens seguintes.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A estatística do teste para verificar se p é igual a 0,5 possui 29 graus de liberdade.

Comentários:

Em um teste para proporções, utilizamos a aproximação para a distribuição normal (e não à distribuição de t-Student). Logo, não há que se falar em graus de liberdade.
Gabarito: Errado.

Item. 15. (CESPE/2011 - ECT)

/ 1 2 3

X 10 15 8

Y 80 90 60

4 5

10 9

85 80

6 7

5 6

50 60

8 9

7 11

65 110

Vx=93, y.r= 945, £y= 780, £^ = 64.150

A fim de planejar o orçamento de uma grande empresa para o próximo ano, um analista selecionou uma amostra aleatória de 10 produtos (i) das empresas filiais e anotou as despesas (X) e os faturamentos (Y)totais decorrentes desses produtos (em R$ milhões). Os resultados por ele obtidos são mostrados na tabela acima.
Com base nessas informações, julgue o item subsecutivo.

Considerando-se X~N(/z, 4), em que /.t representa a média populacional da variável X,
ao se testar a hipótese nula Ho: jiz = R$ 10 milhões contra a hipótese alternativa Hi: /z < R$ 10 milhões,é correto afirmar que o valor da estatística do teste z foi negativo.
Comentários:

Pela tabela, podemos calcular o valor da média amostrai para X observada:

2% 93

% = — = — = 9,3

n 10

Considerando que a população segue distribuição normal com variância conhecida, a média amostrai segue distribuição normal e devemos utilizar a estatística z:
x — /z z = 7^"
Vn

Como jiz = 10 e x < /z, então a estatística z é negativa.

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 16. (CESPE/2011 - ECT)

/ 1 2 3

X 10 15 8

Y 80 90 60

4 5

10 9

85 80

6 7

5 6

50 60

8 9

7 11

65 110

Vx=93, y.r= 945, £y= 780, £^ = 64.150

A fim de planejar o orçamento de uma grande empresa para o próximo ano, um analista selecionou uma amostra aleatória de 10 produtos (i) das empresas filiais e anotou as despesas (X) e os faturamentos (Y)totais decorrentes desses produtos (em R$ milhões). Os resultados por ele obtidos são mostrados na tabela acima.
Com base nessas informações, julgue o item subsecutivo.

Considere o teste de hipóteses Ho: jU = R$ 10 milhões versus Hi: jiz < R$ 10
milhões, em que jU representa a média populacional da variável X, e suponha que X segue uma distribuição normal com desvio padrão igual a R$2 milhões. Com base nessas informações, considerando-se o nível de significância igual a 5%, é correto afirmar que a hipótese nula não seria rejeitada.
Comentários:

Considerando que a população segue distribuição normal com variância conhecida, a média amostrai segue distribuição normal e devemos utilizar a estatística z:
x — /z z = 7^"
Vn

No caso, temos x = 9,3, jU = 10, o = 2 e n = 10, o valor da estatística é:

VTÕ

Pela distribuição normal, temos P(Z < -1,11) = 0,1335, que é superior a 5%. Logo, de fato, não rejeitamos a hipótese nula.
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 17. (CESPE/2011 - ECT)

/ 1 2 3

X 10 15 8

Y 80 90 60

4 5

10 9

85 80

6 7

5 6

50 60

8 9

7 11

65 110

Vx=93, y.r= 945, £y= 780, £^ = 64.150

A fim de planejar o orçamento de uma grande empresa para o próximo ano, um analista selecionou uma amostra aleatória de 10 produtos (i) das empresas filiais e anotou as despesas (X) e os faturamentos (Y)totais decorrentes desses produtos (em R$ milhões). Os resultados por ele obtidos são mostrados na tabela acima.
Com base nessas informações, julgue o item subsecutivo.

Considere um teste de hipóteses acerca da média da variável X. Nesse caso, se todos os demais momentos da distribuição X forem desconhecidos, então a estatística apropriada para esse teste segue uma distribuição t com 9 graus de liberdade.
Comentários:

O item supõe que os demais momentos da distribuição X são desconhecidos, o que significa que a variância(segundo momento central) é desconhecida. Nesse caso, utilizamos a distribuição t de Student com n
- 1 =

10 - 1 = 9 graus de liberdade.

Gabarito: Certo.

Item. 18. (Cebraspe/2015-Telebras)

Japão
Taiwan valor esperado, p(em kg)

desvio padrão a
(em kg)

Um varejista de motocicletas e acessórios encontrou uma caixa de parafusos especiais de origem desconhecida para um modelo da marca Honda. Esses parafusos são produzidos apenas noJapão e
Taiwan. As características da resistência à tração X dos parafusos são apresentadas na tabela. Uma amostra de 20 parafusos da caixa foi testada e encontrou-se a resistência à tração média x.
Considere o teste a respeito da procedência dos parafusos constituído das seguintes hipóteses. Ho: os parafusos procedem do Japão: p = 100; e Hi: os parafusos procedem de Taiwan: p = 110. A regra da decisão
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

do teste é não rejeitar Ho se x < xc, em que xc é um valor a ser encontrado; e rejeitar Ho no caso contrário.A respeito dessa situação, julgue o item subsequente.

O valor crítico xc para o qual vale P(erro tipo I) = P(erro tipo II) é dado por —.

Comentários:

l()0Xc X 110

O enunciado informa que a hipótese nula é H₀:/j. = 100 e a hipótese alternativa é
H^. /x = 110. A hipótese é rejeitada se o resultado do teste for superior a um valor crítico xc, definido de tal forma que a probabilidade do erro tipo I (a) seja igual à probabilidade do erro tipo II (fí), conforme ilustrado abaixo, em que a curva verde representa a hipótese nula e a curva laranja representa a hipótese alternativa:
A probabilidade do erro tipo I pode ser calculada a partir da transformação para a normal padrão do valor xc, considerando a média [i₀ = 100, um desvio padrão populacional o₀ = 15 e uma amostra de tamanho n = 20:
xc — fio xc — 100

z° = 2o_ = 15

Vn V2Õ

Como xc > fio, conforme ilustrado no gráfico, o valor de z₀ é positivo; e a probabilidade do erro tipo I é dada por:
a = P(Z > z₀}

E a probabilidade do erro tipo II pode ser calculada pela transformação para a normal padrão do mesmo valor xc, considerando a média = 110, um desvio padrão populacional = 20e a mesma amostra de tamanho n = 20:
xc — Pi xc — 110

Zl = = 20

Vn V2Õ

Como xc < conforme ilustrado no gráfico, o valor de z± é negativo; e a probabilidade do erro tipo II é dada por:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

/? = P(Z < zj

Para que ambas as probabilidades sejam iguais, temos a seguinte igualdade, ilustrada no gráfico abaixo:
a = P

Pela simetria da normal padrão, temos:

zi = ~zo xc — 110 xc — 100
20 15

V2Õ V2Õ

xc — 110 100 — xc

20 = 15

Que é o resultado descrito no item.

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Testes para a Proporção

Item. 1. (CESPE/2006 - DETRAN-PA) Uma instituição fez dois levantamentos amostrais em um município para avaliar o uso de cinto de segurança pelos condutores de veículos de passeio. O primeiro levantamento envolveu 400 motoristas, dos quais apenas 220 eram usuários do cinto de segurança. Em função desse resultado, foram realizadas campanhas a favor do uso do cinto de segurança. Alguns meses após essas campanhas, realizou-se o segundo levantamento. Dos 100 condutores de veículos de passeio observados no segundo levantamento, 80 eram usuários do cinto de segurança. Com 95% de confiança para o percentual populacional de condutores usuários de cinto de segurança, as margens de erro das duas pesquisas foram, respectivamente, iguais a 5% e 8%.
Para o segundo levantamento, deseja-se testar a hipótese nula Ho: p > 0,9 versus a hipótese alternativaHA : p < 0,9. Nesse caso, a estatística do teste é igual a.

a) 10/3

b) 5/2

c) -5/2.

d) -10/3

Comentários:

Essa questão trata de um teste para proporções, cuja a estatística do teste é dada por:

p — p z = ~^=
PM

\ n

O enunciado informa que, na segunda pesquisa, foram consultados n = 100 motoristas,
dos quais 80 eram

80usuários do cinto de segurança. Logo, a proporção encontrada na amostra foi p =
= 0,8. A hipótese nula presume p = 0,9 (logo, q = 1 - p = 0,1). Assim, a estatística do teste é dada por:
0,8 - 0,9 -0,1 -0,1 10 10

Z |0,9 x 0,1 R/Õ9 ^2 0,1 X °'3 3

J 100 J100 10

Gabarito: D

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 2. (Cebraspe/2016 - TCE-PR) Por meio de uma pesquisa, estimou-se que, em uma população, o percentual p de famílias endividadas era de 57%. Esse resultado foi observado com base em uma amostra aleatória simples de 600 famílias.
Nessa situação, considerando a hipótese nula Ho: p > 60%, a hipótese alternativa Hi: p < 60% e P(Z
< 2) =
0,977, em que Z representa a distribuição normal padrão, bem como sabendo que o teste se baseia na aproximação normal, assinale a opção correta, a respeito desse teste de hipóteses.
a) O erro do tipo II representa a probabilidade de se rejeitar a hipótese nula, uma vez que, na realidade, p =60%.

b) Com nível de significância a = 2,3%, a regra de decisão do teste é rejeitar a hipótese nula caso o percentual de famílias endividadas na amostra seja inferior a 56%.
c) Trata-se de um teste unilateral à direita.

d) A estatística do teste foi igual ou superior a 1.

e) A hipótese nula deve ser rejeitada caso a probabilidade de ocorrência de erro do tipo I seja igual ou inferior a 0,01.
Comentários:

Essa questão trata de um teste para proporções em que consideramos a aproximação da distribuição binomial para a normal (Teorema Central do Limite). Assim, a estatística do teste é dada por:
p — p z= |
pxq

\ n

A hipótese nula é Ho: p > 60% e a hipótese alternativa Hi: p < 60%, logo temos um teste unilateral à esquerda(alternativa C incorreta).

O enunciado informa que:

* A proporção observada é p = 0,57

* A proporção indicada na hipótese nula é p = 0,6 (logo, q = 1 — p = 0,4)

* O tamanho amostrai é n = 600
Substituindo esses valores, temos:

0,57 - 0,6 -0,03 -0,03 -0,03

Z /0,6 x 0,4 /Õ24 V0,0004 0,02
V 600 \ 600

Logo, a estatística do teste é inferior a 1 (alternativa D incorreta).

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação à alternativa A, o erro tipo II corresponde ao evento de se não rejeitar a hipótese nula sendo ela falsa. O erro descrito na alternativa (rejeitar a hipótese nula sendo ela verdadeira é o erro tipo I). Por isso, a alternativa A está incorreta.
Em relação à alternativa E, a rejeição ou não da hipótese nula depende do nível de significância desejado,não sendo possível decidir quanto à rejeição ou não da hipótese nula sem esse valor.
Logo, a alternativa E
está incorreta.

A alternativa B define um nível de significância cr = 2,3%. O enunciado informa que
P(Z < 2) = 0,977. Logo, o complementar é:
P(Z > 2) = 1 - P(Z < 2) = 1 - 0,977 = 0,023

Pela simetria da normal padrão, temos:

P(Z <-2) = P(Z > 2) = 0,023

Como se trata de um teste unilateral à esquerda, o valor crítico é zc = -2. Então,
a proporção limite é dada por:
= Pc ~ 0,6

|0,6 x 0,4

A/ 600

pc — 0,6 = — 2 x 0,02 = —0,04

Pc = 0,56

Logo, a regra de decisão será, de fato, rejeitar a hipótese nula caso a proporção amostrai observada seja inferior a 56%.
Gabarito: B

Item. 3. (Cebraspe/2016 - TCE-PR) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0. Considerando que a amostra {0,1,1, 0, 0,1,
0,1, 0,1,1, 0, 0,1,
1, 0,1,1,1,1} foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

Uma vez que a amostra é menor que 30, a estatística do teste segue uma distribuição t de Student.

Comentários:

Em testes para proporções, a estatística do teste é dada por:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

z= I

p — p pxq
\ n

Em que consideramos a aproximação da proporção amostrai a uma distribuição normal. A
distribuição de t-
Student é utilizada para populações normais com variância desconhecida.

Gabarito: Errado.

Item. 4. (Cebraspe/2016 - TCE-PR) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0. Considerando que a amostra {0,1,1, 0, 0,1,
0,1, 0,1,1, 0, 0,1,
1, 0,1,1,1,1} foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

A estatística do teste para testar a hipótese Ho: P = 0,5 contra Hi: P #= 05, em que P representa a proporção de empresas cujo CNPJ está regular, é maior que 2.
Comentários:

Em testes para proporções, a estatística do teste é dada por:

A proporção amostrai observada é:

p =

n

-0=0'6

Então, considerando a hipótese nula, p = 0,5 (logo, q = 1 - p = 0,5), a estatística é:

z = .

0,6 - 0,5

0,5 x 0,5

2Õ

Que é inferior a 2.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

p-valor

Item. 1. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.Um teste t de Student foi aplicado com a hipótese nula Ho: PA = pp e a hipótese alternativa Hi: pA
> pp, em que PA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

A hipótese Ho deve ser rejeitada, o que indica que pA > pp.

Comentários:

Sendo o p-valor = 0,03 e o nível de significância a = 0,05, temos p < a, o que significa que a hipótese nula deve ser rejeitada. Assim, consideramos como verdadeira a hipótese alternativa em que pA > pp.
Gabarito: Certo

Item. 2. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.Um teste t de Student foi aplicado com a hipótese nula Ho: pA = pp e a hipótese alternativa Hi: pA
> pp, em que pA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

Se a hipótese alternativa fosse H^. p.A * ilp, a hipótese nula não seria rejeitada.

Comentários:

Se a hipótese alternativa fosse Hr\o teste seria bilateral, em que o nível de significância seria a=0,025 de cada lado. Assim, se o resultado do teste fosse t tal que p-valor = P(T >
t) = 0,03, então o resultado do teste estaria na região de não rejeição, como ilustrado abaixo:
0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Assim, a hipótese nula não seria rejeitada.

Gabarito: Certo

Item. 3. (Cebraspe/2017 - TCE-PE) Para avaliar se a proporção p de itens defeituosos enviados por um fornecedor estava acima do valor pactuado de 0,025, um analista, a partir de uma amostra aleatória de itens enviada por esse fornecedor, testou a hipótese nula Ho: p < 0,025 contra a hipótese alternativa Hi: p
> 0,025, utilizando nível de significância a = 1%. A respeito dessa situação hipotética, julgue o seguinte item.
Caso o P-valor do teste efetuado pelo analista seja igual a 0,005, é correto concluir que a afirmação proposta na hipótese nula seja verdadeira.
Comentários:

Caso o p-valor do teste seja p = 0,005 e o nível de significância seja a = 0,01,
então temos p < cr e então devemos rejeitar a hipótese nula (ou seja, concluir que a hipótese nula é falsa).
Gabarito: Errado.

Item. 4. (Cebraspe/2014 - TJ-SE) Com o propósito de produzir inferências acerca da proporção populacional
(p) de pessoas satisfeitas com determinado serviço oferecido pelo judiciário brasileiro,
foi considerada uma pequena amostra de 30 pessoas, tendo cada uma de responder 1, para o caso de estar satisfeita,ou
0, para o caso de não estar satisfeita. Os dados da amostra estão registrados a seguir.

000110100000100010001100010001

Com base nessas informações, julgue os itens seguintes.

Caso o p-valor do teste Ho: p = 0,5 versus Hi: p * 0,5 seja igual a 0,0295, então,
se a hipótese alternativa fosse alterada para Hi: p < 0,5, o teste seria significativo ao nível de significância de 2%.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O item informa que o p-valor observado, considerando-se um teste bilateral foi p =
0,0295. Caso o teste fosse unilateral, teríamos p-valor = 0,0295/2 = 0,015. Para um nível de significância a =0,02, teríamos a > p —
valor. Nesse caso, devemos rejeitar a hipótese nula, o que chamamos de teste significativo (ou evidência estatística).
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Conceitos Fundamentais

Item. 1. (Cebraspe/2019 - TJ-AM) A respeito dos testes de hipóteses, julgue o próximo item.

Sendo a o nível de significância de um teste estatístico, seu valor será sempre constante em 0,05.

Item. 2. (CESPE/2011 - STM) Acerca dos conceitos de estatística e dos parâmetros estatísticos,
julgue o item seguinte.
A estatística descritiva permite testar hipóteses a respeito da população de interesse.

Item. 3. (CESPE/2011 - STM) Acerca dos conceitos de estatística e dos parâmetros estatísticos,
julgue o item seguinte.
Em estatística, parâmetro pode ser uma quantidade desconhecida da população-alvo,
à qual não se tem acesso diretamente, mas que se deseja estimar ou a respeito da qual se deseja avaliar hipóteses.
Item. 4. (Cebraspe/2015 - Telebras) Com relação às técnicas de amostragem estatística,
julgue o próximo item.
Considerando as informações colecionadas em uma amostra, a metodologia do teste de hipóteses tem o objetivo de determinar a possibilidade de a hipótese nula ser verdadeira, uma vez que é indissolúvel a relação entre a declaração da hipótese nula e a especificação da hipótese alternativa, sendo esta necessariamente verdadeira caso a hipótese nula seja falsa.
Item. 5. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.Um teste t de Student foi aplicado com a hipótese nula Ho: PA = pp e a hipótese alternativa Hi: pA
> pp, em que PA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

As hipóteses do teste t de Student aplicado são simples.

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (Cebraspe/2015-Telebras)

valor esperado, p
(em kg)

desvio padrão a

(em kg)

Japão 100 15

Taiwan 110 20

Um varejista de motocicletas e acessórios encontrou uma caixa de parafusos especiais de origem desconhecida para um modelo da marca Honda. Esses parafusos são produzidos apenas noJapão e
Taiwan. As características da resistência à tração X dos parafusos são apresentadas na tabela. Uma amostra de 20 parafusos da caixa foi testada e encontrou-se a resistência à tração média x.
Considere o teste a respeito da procedência dos parafusos constituído das seguintes hipóteses. Ho: os parafusos procedem do Japão: p = 100; e Hi: os parafusos procedem de Taiwan: p = 110. A regra da decisão do teste é não rejeitar Ho se x < xc, em que xc é um valor a ser encontrado; e rejeitar Ho no caso contrário.A respeito dessa situação, julgue o item subsequente.

O teste descrito é um teste de hipóteses composto.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. ERRADO

Item. 2. ERRADO

Item. 3. CERTO

Item. 4. CERTO

Item. 5. ERRADO

Item. 6. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Tipos de Erros

Item. 1. (Cebraspe/2018 - IJSN-ES) Considerando os conceitos associados a probabilidade e estatística,julgue o item.

A hipótese nula (Ho) é a afirmação feita acerca do valor de um parâmetro populacional e o erro tipo I ocorre quando a hipótese nula é falsa e não é rejeitada.
Item. 2. (Cebraspe/2016 - TCE-PAM) Uma amostra aleatória, com n = 16 observações independentes e identicamente distribuídas (IID), foi obtida a partir de uma população infinita, com média e desvio padrão desconhecidos e distribuição normal. Tendo essa informação como referência inicial,julgue o seguinte item.
A potência de um teste de hipóteses corresponde à probabilidade de se rejeitar a hipótese nula, dado que a hipótese nula é correta.
Item. 3. (Cebraspe/2016 - TCE-PR) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0. Considerando que a amostra {0,1,1, 0, 0,1,
0,1, 0,1,1, 0, 0,1,
1, 0,1,1,1,1} foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

O poder do teste pode ser facilmente calculado pelo complementar do erro tipo II (/3).

Item. 4. (CESPE/2011 - STM) Julgue os itens que se seguem, acerca de definições da teoria estatística.
O erro do tipo II de um teste de hipóteses ocorre quando se rejeita uma hipótese nula que é verdadeira.
Item. 5. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.
Um teste t de Student foi aplicado com a hipótese nula Ho: PA = pp e a hipótese alternativa Hi: pA
> pp, em que PA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

A função poder do teste, n(pA - pP), assume o valor n(0) = 0,03.

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 6. (Cebraspe/2013 - FUB) No que se refere a testes de hipóteses, julgue o item subsecutivo.

O poder de um teste tende a diminuir à medida que o nível de significância decresce.

Item. 7. (Cebraspe/2013 - FUB) No que se refere a testes de hipóteses, julgue o item subsecutivo.

O tamanho amostrai influencia o poder do teste e o nível de significância.

Item. 8. (CESPE/2012 - ANAC) Consoante a teoria de testes de hipóteses, julgue os próximos itens.
Em um teste de hipóteses para se comparar duas médias amostrais, o tamanho amostrai é um fator importante, pois, à medida que o tamanho da amostra aumenta, a probabilidade do erro de tipo I (nível de significância do teste) tende a diminuir.
Item. 9. (CESPE/2010 - FUB) Julgue o próximo item, referente à inferência estatística.

No teste de hipóteses Ho: p. = /z₀ contra Hi: /z =# ^₀, em que os dados são provenientes de uma distribuição normal com variância conhecida, se a probabilidade de ocorrência do erro tipo I (a)for 5%, a probabilidade de ocorrer o erro tipo II (/3) é igual a 20%.
Item. 10. (Cebraspe/2020 - TJ-PA) O teste de hipóteses se assemelha ao julgamento de um crime. Em um julgamento, há um réu, que inicialmente se presume inocente. As provas contra o réu são, então,apresentadas, e, se os jurados acham que são convincentes, sem dúvida alguma, o réu é considerado culpado. A presunção de inocência é vencida. Michael Barrow. Estatística para economia,contabilidade e administração. São Paulo: Ática, 2007, p. 199 (com adaptações).
João foi julgado culpado pelo crime de assassinato e condenado a cumprir pena de 20 anos de reclusão.Após 10 anos de prisão, André, o verdadeiro culpado pelo delito pelo qual João fora condenado,
confessou o ilícito e apresentou provas irrefutáveis de que é o verdadeiro culpado,exclusivamente. Considerando a situação hipotética apresentada e o fragmento de texto anterior, julgue os itens que se seguem.
I Pode-se considerar que a culpa de João seja uma hipótese alternativa.

II No julgamento, ocorreu um erro conhecido nos testes de hipótese como erro do tipo I.

III Se a hipótese nula fosse admitida pelos jurados como verdadeira e fosse efetivamente
João o culpado pelo crime, o erro cometido teria sido o chamado erro do tipo II.
Assinale a opção correta a) Apenas o item I está certo.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

b) Apenas o item II está certo.

c) Apenas os itens I e III estão certos.

d) Apenas os itens II e III estão certos.

e) Todos os itens estão certos.

Item. 11. (Cebraspe/2017 - TCE-PE) Para avaliar se a proporção p de itens defeituosos enviados por um fornecedor estava acima do valor pactuado de 0,025, um analista, a partir de uma amostra aleatória de itens enviada por esse fornecedor, testou a hipótese nula Ho: p < 0,025 contra a hipótese alternativa Hi: p
> 0,025, utilizando nível de significância a = 1%. A respeito dessa situação hipotética, julgue o seguinte item.
O nível de significância representa a probabilidade de se aceitar a hipótese Ho: p <
0,025 quando, na verdade,
a proporção p for superior a 0,025.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. ERRADO 5. ERRADO
Item. 9. ERRADO

Item. 2. ERRADO 6. CERTO
Item. 10. LETRA E

Item. 3. CERTO 7. ERRADO
Item. 11. ERRADO

Item. 4. ERRADO 8. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Testes para a Média

Item. 1. (Cebraspe/2019 - TJ-AM) Um pesquisador deseja comparar a diferença entre as médias de duas amostras independentes oriundas de uma ou duas populações gaussianas. Considerando essa situação hipotética, julgue o próximo item.
Para que qualquer teste possa ser realizado, as amostras devem ter distribuição normal.

Item. 2. (Cebraspe/2019 - TJ-AM) Um pesquisador deseja comparar a diferença entre as médias de duas amostras independentes oriundas de uma ou duas populações gaussianas. Considerando essa situação hipotética, julgue o próximo item.
Para que a referida comparação seja efetuada, é necessário que ambas as amostras tenham N > 30.

Item. 3. (Cebraspe/2019 - TJ-AM) Um pesquisador deseja comparar a diferença entre as médias de duas amostras independentes oriundas de uma ou duas populações gaussianas. Considerando essa situação hipotética, julgue o próximo item.
Caso o pesquisador realize um teste t de Student e encontre um valor de p = 0,95,
considerando-se a = 0,05,
será correto concluir que ambas as amostras provêm da mesma população.

Item. 4. (Cebraspe/2016 - FUNPRESP)

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O gráfico ilustra cinco possibilidades de fundos de investimento com suas respectivas rentabilidades.Considerando que as probabilidades de investimento para os fundos A, B, C e D sejam,
respectivamente,
P(A) = 0,182; P(B) = 0,454; P(C) = 0,091; e P(D) = 0,182, julgue o item abaixo.

Se os cinco fundos de investimento representarem uma amostra de todos os fundos de investimento disponíveis no mercado financeiro, então o teste Z com 4 graus de liberdade poderá ser utilizado para verificar se a rentabilidade média de todos os fundos é maior que um valor especificado, considerando-se que os dados seguem uma distribuição normal.
Item. 5. (Cebraspe/2013 - ANCINE) Em relação aos métodos de inferência estatística, julgue o item subsequente.
Em um teste de hipóteses para a média de uma distribuição (Ho: p = po), a razão

, = x-^0

em que o denota o desvio padrão populacional, x é a média x amostrai e n representa o tamanho de uma amostra, segue uma distribuição normal padrão, desde que a distribuição populacional seja normal.
Item. 6. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.Um teste t de Student foi aplicado com a hipótese nula Ho: PA = pp e a hipótese alternativa Hi: pA
> pp, em que pA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

Caso fosse calculado um intervalo de confiança bilateral para pA- pp, com coeficiente de confiança 95%, tal intervalo conteria o valor zero.
Item. 7. (Cebraspe/2015-Telebras) Um analista da TELEBRAS, a fim de verificar o tempo durante o qual um grupo de consumidores ficou sem o serviço de Internet do qual eram usuários,selecionou uma amostra de 10 consumidores críticos. Os dados coletados, em minutos, referentes a esses consumidores foram listados na tabela seguinte.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

consumidor tempo (cm minutos)
Cl c2

8 2

c3 c4 c5

3 5 7

Q ^8

7 10 9

c9 C|0

4 5

Com base nessa situação hipotética, julgue o item subsequente.

Para verificar se o tempo médio sem Internet é igual a 5 minutos, o analista deverá realizar um teste com 8graus de liberdade.

Item. 8. (Cebraspe/2015 - FUB - Estatístico) O tempo, X, de carregamento de um celular segue uma distribuição normal com média e variância desconhecidas. Foi coletada uma amostra de tamanho igual a10, em que a média amostrai é de 58 minutos e o desvio padrão da amostra é de 5 minutos. O
fabricante do celular, para testar se a média de carregamento é de 50 minutos, aplica um teste t de Student com a hipótese nula Ho: px = 50 contra a hipótese alternativa de Hi: px.^ 50.
Considerando a situação hipotética descrita, julgue os itens a seguir.

distribuição Normal.

58 ^7S, 58 H—em que za é o a-quantil da

Item. 9. (Cebraspe/2015 - FUB - Estatístico) O tempo, X, de carregamento de um celular segue uma distribuição normal com média e variância desconhecidas. Foi coletada uma amostra de tamanho igual a
10, em que a média amostrai é de 58 minutos e o desvio padrão da amostra é de 5 minutos. O
fabricante do celular, para testar se a média de carregamento é de 50 minutos, aplica um teste t de Student com a hipótese nula Ho: px = 50 contra a hipótese alternativa de Hi: px.^ 50.
Considerando a situação hipotética descrita, julgue os itens a seguir.

O teste t de Student realizado pelo fabricante é inválido, pois a amostra não é suficientemente grande.
Item. 10. (Cebraspe/2016 - TCE-PR) Em um teste estatístico para a média populacional g com nível de significância a = 5% a hipótese nula Ho deverá ser rejeitada se X > 30 ou X <10, em que X denota a média amostrai. Supondo que a variância populacional seja conhecida e que o tamanho da amostra seja igual a 10, assinale a opção correta.
a) A hipótese alternativa do teste é Hi: X =# 20.

b) O teste é bilateral.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) Sob a hipótese nula, P(X > 30) = 0,05

d) Trata-se de um teste t de Student com 10 graus de liberdade.

e) A hipótese nula desse teste é Ho: p. = 10 ou = 30

Item. 11. (Cebraspe/2018 - PF) O tempo gasto (em dias) na preparação para determinada operação policial é uma variável aleatória X que segue distribuição normal com média M, desconhecida, e desvio padrão igual a 3 dias. A observação de uma amostra aleatória de 100 outras operações policiais semelhantes a essa produziu uma média amostrai igual a 10 dias.
Com referência a essas informações, julgue o item que segue, sabendo que P(Z > 2) =
0,025, em que Z
denota uma variável aleatória normal padrão.

Considerando-se o teste da hipótese nula Ho: M < 9,5 dias contra a hipótese alternativa Hi: M > 9,5 dias,adotando-se o nível de significância igual a 1%, não haveria evidências estatísticas contra a hipótese Ho.
Item. 12. (Cebraspe/2016 - TCE-PR) A respeito de uma amostra de tamanho n = 10,
com os valores amostrados {0,10, 0,06, 0,10, 0,12, 0,08, 0,10, 0,05, 0,15, 0,14, 0,11}, extraídos de determinada população,julgue o item seguinte.

Para um teste Z ou t de Student bilateral (com pelo menos 9 graus de liberdade),
uma estatística do teste menor que 1,5 é considerada não significativa para o nível de significância de 5%.
Item. 13. (Cebraspe/2016 - TCE-PR) A respeito de uma amostra de tamanho n = 10,
com os valores amostrados {0,10, 0,06, 0,10, 0,12, 0,08, 0,10, 0,05, 0,15, 0,14, 0,11}, extraídos de determinada população,julgue o item seguinte.

Dado que a variância populacional é desconhecida e os dados seguem uma distribuição normal, é correto afirmar que o teste t para a média populacional possui 10 graus de liberdade.
Item. 14. (Cebraspe/2014 - TJ-SE) Com o propósito de produzir inferências acerca da proporção populacional
(p) de pessoas satisfeitas com determinado serviço oferecido pelo judiciário brasileiro,
foi considerada uma pequena amostra de 30 pessoas, tendo cada uma de responder 1, para o caso de estar satisfeita,ou
0, para o caso de não estar satisfeita. Os dados da amostra estão registrados a seguir.

000110100000100010001100010001

Com base nessas informações, julgue os itens seguintes.

A estatística do teste para verificar se p é igual a 0,5 possui 29 graus de liberdade.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 15. (CESPE/2011 - ECT)

/ 1 2 3

X 10 15 8

Y 80 90 60

4 5

10 9

85 80

6 7

5 6

50 60

8 9

7 11

65 110

Vx=93, y.r= 945, £y= 780, £^ = 64.150

A fim de planejar o orçamento de uma grande empresa para o próximo ano, um analista selecionou uma amostra aleatória de 10 produtos (i) das empresas filiais e anotou as despesas (X) e os faturamentos (Y)totais decorrentes desses produtos (em R$ milhões). Os resultados por ele obtidos são mostrados na tabela acima.
Com base nessas informações, julgue o item subsecutivo.

Considerando-se X~N(/z, 4), em que representa a média populacional da variável X, ao se testar a hipótese nula Ho: jU = R$ 10 milhões contra a hipótese alternativa Hi: /z < R$ 10 milhões,é correto afirmar que o valor da estatística do teste z foi negativo.
Item. 16. (CESPE/2011 - ECT)

/ 1 2 3

X 10 15 8

Y 80 90 60

4 5

10 9

85 80

6 7

5 6

50 60

8 9

7 11

65 110

Vx=93, y.r= 945, £y= 780, £^ = 64.150

A fim de planejar o orçamento de uma grande empresa para o próximo ano, um analista selecionou uma amostra aleatória de 10 produtos (i) das empresas filiais e anotou as despesas (X) e os faturamentos (Y)totais decorrentes desses produtos (em R$ milhões). Os resultados por ele obtidos são mostrados na tabela acima.
Com base nessas informações, julgue o item subsecutivo.

Considere o teste de hipóteses Ho: /z = R$ 10 milhões versus Hi: /z < R$ 10
milhões, em que /z representa a média populacional da variável X, e suponha que X segue uma distribuição normal com desvio padrão igual a R$2 milhões. Com base nessas informações, considerando-se o nível de significância igual a 5%, é correto afirmar que a hipótese nula não seria rejeitada.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 17. (CESPE/2011 - ECT)

/ 1 2 3

X 10 15 8

Y 80 90 60

4 5

10 9

85 80

6 7

5 6

50 60

8 9

7 11

65 110

Vx=93, y.r= 945, £y= 780, £^ = 64.150

A fim de planejar o orçamento de uma grande empresa para o próximo ano, um analista selecionou uma amostra aleatória de 10 produtos (i) das empresas filiais e anotou as despesas (X) e os faturamentos (Y)totais decorrentes desses produtos (em R$ milhões). Os resultados por ele obtidos são mostrados na tabela acima.
Com base nessas informações, julgue o item subsecutivo.

Considere um teste de hipóteses acerca da média da variável X. Nesse caso, se todos os demais momentos da distribuição X forem desconhecidos, então a estatística apropriada para esse teste segue uma distribuição t com 9 graus de liberdade.
Item. 18. (Cebraspe/2015-Telebras)

Japão
Taiwan valor esperado, p(em kg)

desvio padrão a
(em kg)

Um varejista de motocicletas e acessórios encontrou uma caixa de parafusos especiais de origem desconhecida para um modelo da marca Honda. Esses parafusos são produzidos apenas noJapão e
Taiwan. As características da resistência à tração X dos parafusos são apresentadas na tabela. Uma amostra de 20 parafusos da caixa foi testada e encontrou-se a resistência à tração média x.
Considere o teste a respeito da procedência dos parafusos constituído das seguintes hipóteses. Ho: os parafusos procedem do Japão: p = 100; e Hi: os parafusos procedem de Taiwan: p = 110. A regra da decisão do teste é não rejeitar Ho se x < xc, em que xc é um valor a ser encontrado; e rejeitar Ho no caso contrário.A respeito dessa situação, julgue o item subsequente.

l()0Xc X 110

O valor crítico xc para o qual vale P(erro tipo I) = P(erro tipo II) é dado por-------------------
= — -- .

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. ERRADO

Item. 2. ERRADO

Item. 3. CERTO

Item. 4. ERRADO

Item. 5. ERRADO

Item. 6. CERTO

Item. 7. ERRADO

Item. 8. ERRADO

Item. 9. ERRADO

Item. 10. LETRA B

Item. 11. CERTO

Item. 12. CERTO

Item. 13. ERRADO

Item. 14. ERRADO

Item. 15. CERTO

Item. 16. CERTO

Item. 17. CERTO

Item. 18. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Testes para a Proporção

Item. 1. (CESPE/2006 - DETRAN-PA) Uma instituição fez dois levantamentos amostrais em um município para avaliar o uso de cinto de segurança pelos condutores de veículos de passeio. O primeiro levantamento envolveu 400 motoristas, dos quais apenas 220 eram usuários do cinto de segurança. Em função desse resultado, foram realizadas campanhas a favor do uso do cinto de segurança. Alguns meses após essas campanhas, realizou-se o segundo levantamento. Dos 100 condutores de veículos de passeio observados no segundo levantamento, 80 eram usuários do cinto de segurança. Com 95% de confiança para o percentual populacional de condutores usuários de cinto de segurança, as margens de erro das duas pesquisas foram, respectivamente, iguais a 5% e 8%.
Para o segundo levantamento, deseja-se testar a hipótese nula Ho: p > 0,9 versus a hipótese alternativaHA : p < 0,9. Nesse caso, a estatística do teste é igual a.

a) 10/3

b) 5/2

c) -5/2.

d) -10/3

Item. 2. (Cebraspe/2016 - TCE-PR) Por meio de uma pesquisa, estimou-se que, em uma população, o percentual p de famílias endividadas era de 57%. Esse resultado foi observado com base em uma amostra aleatória simples de 600 famílias.
Nessa situação, considerando a hipótese nula Ho: p > 60%, a hipótese alternativa Hi: p < 60% e P(Z
< 2) =
0,977, em que Z representa a distribuição normal padrão, bem como sabendo que o teste se baseia na aproximação normal, assinale a opção correta, a respeito desse teste de hipóteses.
a) O erro do tipo II representa a probabilidade de se rejeitar a hipótese nula, uma vez que, na realidade, p =60%.

b) Com nível de significância a = 2,3%, a regra de decisão do teste é rejeitar a hipótese nula caso o percentual de famílias endividadas na amostra seja inferior a 56%.
c) Trata-se de um teste unilateral à direita.

d) A estatística do teste foi igual ou superior a 1.

e) A hipótese nula deve ser rejeitada caso a probabilidade de ocorrência de erro do tipo I seja igual ou inferior a 0,01.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 3. (Cebraspe/2016 - TCE-PR) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0. Considerando que a amostra {0,1,1, 0, 0,1,
0,1, 0,1,1, 0, 0,1,
1, 0,1,1,1,1} foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

Uma vez que a amostra é menor que 30, a estatística do teste segue uma distribuição t de Student.

Item. 4. (Cebraspe/2016 - TCE-PR) Em estudo acerca da situação do CNPJ das empresas de determinado município, as empresas que estavam com o CNPJ regular foram representadas por 1, ao passo que as comCNPJ irregular foram representadas por 0. Considerando que a amostra {0,1,1, 0, 0,1,
0,1, 0,1,1, 0, 0,1,
1, 0,1,1,1,1} foi extraída para realizar um teste de hipóteses, julgue o item subsequente.

A estatística do teste para testar a hipótese Ho: P = 0,5 contra Hi: P #= 05, em que P representa a proporção de empresas cujo CNPJ está regular, é maior que 2.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. LETRA D

Item. 2. LETRA B

Item. 3. ERRADO

Item. 4. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

p-valor

Item. 1. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.Um teste t de Student foi aplicado com a hipótese nula Ho: |iA = |ip e a hipótese alternativa Hi: pA > pp, em que PA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

A hipótese Ho deve ser rejeitada, o que indica que pA > pp.

Item. 2. (Cebraspe/2015 - FUB - Estatístico) Alunos de um departamento de uma universidade estudaram por dois livros diferentes, A e P. Foram retiradas amostras aleatórias simples dos que estudaram pelo livroA e dos que estudaram pelo livro P, tendo sido observadas as notas dos alunos em um exame padronizado.Um teste t de Student foi aplicado com a hipótese nula Ho: pA = pp e a hipótese alternativa Hi: pA > pp, em que pA e pp representam, respectivamente, as médias populacionais das notas dos alunos, no exame padronizado, que estudaram pelo livro A e pelo livro P. O valor p obtido foi 0,03.
A partir da situação apresentada, julgue os itens subsequentes, considerando o nível de significância de0,05.

Se a hipótese alternativa fosse H^. p.A * ilp, a hipótese nula não seria rejeitada.

Item. 3. (Cebraspe/2017 - TCE-PE) Para avaliar se a proporção p de itens defeituosos enviados por um fornecedor estava acima do valor pactuado de 0,025, um analista, a partir de uma amostra aleatória de itens enviada por esse fornecedor, testou a hipótese nula Ho: p < 0,025 contra a hipótese alternativa Hi: p
> 0,025, utilizando nível de significância a = 1%. A respeito dessa situação hipotética, julgue o seguinte item.
Caso o P-valor do teste efetuado pelo analista seja igual a 0,005, é correto concluir que a afirmação proposta na hipótese nula seja verdadeira.
Item. 4. (Cebraspe/2014 - TJ-SE) Com o propósito de produzir inferências acerca da proporção populacional
(p) de pessoas satisfeitas com determinado serviço oferecido pelo judiciário brasileiro, foi considerada
0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

uma pequena amostra de 30 pessoas, tendo cada uma de responder 1, para o caso de estar satisfeita, ou0, para o caso de não estar satisfeita. Os dados da amostra estão registrados a seguir.

000110100000100010001100010001

Com base nessas informações, julgue os itens seguintes.

Caso o p-valor do teste Ho: p = 0,5 versus Hi: p * 0,5 seja igual a 0,0295, então,
se a hipótese alternativa fosse alterada para Hi: p < 0,5, o teste seria significativo ao nível de significância de 2%.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. CERTO

Item. 2. CERTO

Item. 3. ERRADO

Item. 4. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

