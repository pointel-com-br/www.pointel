# Probabilidade e Estatística - Teoria da Amostragem

SERPRO - Estatística e Probabilidade -

2023 (Pós-Edital)

Autor:

Equipe Exatas Estratégia

Concursos

Índice

1) Introdução - Teoria da Amostragem

2) Noções Iniciais sobre a Teoria da Amostragem

3) Noções Iniciais sobre a Teoria da Amostragem

4) Tipos de Amostragem Probabilística

5) Tipos de Amostragem não Probabilística

6) Questões Comentadas - Conceitos Iniciais - Cebraspe

7) Questões Comentadas - Amostragem Probabilística - Cebraspe

8) Questões Comentadas - Amostragem Não Probabilística - Cebraspe

9) Lista de Questões - Conceitos Iniciais - Cebraspe

10) Lista de Questões - Amostragem Probabilística - Cebraspe

11) Lista de Questões - Amostragem Não Probabilística - Cebraspe

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Olá, concurseiro(a)!

Nessa aula, vamos fazer uma pausa nos cálculos!!! Não estou dizendo que você não vai precisar fazer conta alguma, mas elas são poucas e relativamente tranquilas!
Veremos alguns conceitos iniciais e diversos tipos de amostragem. Diversas questões sobre esse assunto descrevem um procedimento de amostragem e pedem para você indicar a que tipo ela se refere. Outras questões são mais genéricas e cobram alguns princípios envolvendo amostragem.
Então? Vamos lá?!

Luana Brandão

Doutora em Engenharia de Produção (UFF)
Auditora Fiscal da SEFAZ-RJ

Se tiver alguma dúvida, entre em contato comigo!

M professoraluanabrandao@gmail.com
@professoraluanabrandao

"O segredo de prosseguir é começar."

Mark Twain

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TEoRIA DA AMoSTRAGEM

Introdução

Nesta aula, veremos a Inferência Estatística (também chamada de Estatística Inferencial) na prática!
Esse ramo da estatística nos ajuda a tirar conclusões a respeito de um todo (que chamamos de população)
a partir das observações feitas em uma parte dessa população (que chamamos de amostra).

A inferência é uma técnica importante porque normalmente não é possível conhecer a informação exata
(por exemplo, altura, idade, salário, etc.) para toda a população (o que chamamos de censo).

Por exemplo, para conhecer a altura média dos brasileiros, não seria viável verificar a altura de todos os brasileiros para conhecer exatamente a sua média. Em vez disso, seleciona-se uma amostra de brasileiros, a partir da qual são feitas as medições necessárias.
Por fim, com base nessas medições da amostra, são feitos os cálculos necessários para tirar conclusões a respeito da altura média da população de brasileiros.
Vamos destacar os seguintes conceitos do processo que acabamos de descrever:

* A característica numérica da população que se deseja conhecer (no nosso exemplo, a altura média da população de brasileiros) é chamada parâmetro populacional;
* A medida correspondente feita na amostra (no caso, a altura média dos brasileiros da amostra selecionada) é chamada de parâmetro de estimativa ou estatística da amostra;
* As conclusões a respeito da população feitas a partir da amostra são chamadas de inferência.

As etapas desse processo de inferência estão representadas abaixo:

/------------------- X z X

Selecionar uma amostra

Calcular a estatística da amostra
*

Inferir o parâmetro populacional k y y k y
Nesta aula, veremos as maneiras de selecionar uma amostra, que éa 1- etapa da Inferência
Estatística.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

CoNCEIToS INICIAIS

A Teoria da Amostragem estuda a extração de amostras de uma dada população.

Uma população é um conjunto de elementos que apresenta pelo menos uma característica em comum;enquanto uma amostra é um subconjunto próprio dessa população. O termo próprio significa que o subconjunto não é vazio e não contém todos os elementos do conjunto original.
Nesse sentido, a amostra se distingue do censo, em que todos os elementos da população são examinados.Por não analisar todos os elementos, a amostragem não produz um resultado exato, sendo, portanto,recomendada quando o censo for inviável ou extremamente custoso.

A característica da população que se deseja estudar, descrita numericamente, é chamada de parâmetro populacional. São exemplos de parâmetro populacional, a média populacional, a variância populacional, a proporção populacional etc.
Por ser uma característica da população, o parâmetro populacional é fixo, não varia.

O parâmetro populacional é inferido a partir dos resultados encontrados na amostra, que chamamos de estimador (ou estimativa) do parâmetro populacional, parâmetro amostrai (ou de estimativa).
Um estimador é uma estatística da amostra, isto é, uma função dos dados observados,
que apresenta determinadas propriedades desejáveis. Assim, os estimadores são calculados após a extração das amostras.
Por exemplo, a média amostrai x é o estimador adequado para estimar a média populacional /z, sendo calculado pela razão entre o somatório dos elementos da amostra x, dividido pelo número de elementos da amostra n, ou seja, é uma função dos dados observados na amostra:
S x n
Como os valores dos elementos da amostra x variam, pois a cada extração podemos obter elementos diferentes, o estimador também varia. Ou seja, o estimador é uma variável aleatória.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Podemos representar o processo de amostragem como:

População

Parâmetro Populacional
(Valor Fixo)

Amostragem Aleatória

Inferência

Amostra

* '

Estimador
(Variável Aleatória)

-

A unidade passível de seleção é chamada de unidade amostrai. Por exemplo, se vamos verificar as condições socioeconômicas de uma população, podemos concentrar a pesquisa em indivíduos ou em famílias. No primeiro caso, selecionaríamos uma amostra de indivíduos (unidade amostrai =indivíduo); e, no segundo caso, selecionaríamos uma amostra de famílias (unidade amostrai = famílias).
A quantidade de elementos da amostra n pode ser chamada de tamanho amostrai; e a quantidade de elementos da população N, de tamanho populacional.
Também podemos adotar uma perspectiva diferente e considerar os elementos como área.
Nesse caso, as unidades amostrais são parcelas da área; o tamanho amostrai corresponde à área total da amostra a; e o tamanho populacional corresponde à área total da população A.
A razão entre o tamanho da amostra n e o tamanho da população N é chamada de fração amostrai ou fator amostrai ou intensidade amostrai e representa a proporção de elementos da população selecionados na amostra:
A razão inversa pode ser chamada de fração de seleção (ou fator de expansão) e corresponde ao número de indivíduos da população que cada indivíduo selecionado na amostra representa:
Esses parâmetros (unidade amostrai, fração amostrai etc.) são definidos no planejamento da amostragem,
também chamado de plano amostrai.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ATENÇÃO

DECORE!

Unidade amostrai: unidade passível de seleção (indivíduos, famílias, empresas etc.)

Fração ou intensidade amostrai (proporção entre seleção e população): / = "

Fração de seleção ou fator de expansão (n^ que cada selecionado representa): fs=~

— PRATICAR!

i (2017 - Conter) Entre os casos em que se recomenda a utilização de amostragem,
cita-se a situação em que :

= a) haja necessidade de alta precisão.
i b) as características da população sejam de fácil mensuração, mesmo com população que não seja pequena. ;
= c) a população seja muito pequena e a amostra fique relativamente grande.
;

d) a população seja muito pequena e suas características sejam totalmente desconhecidas.
i i e) a população seja numerosa e com características bastante homogêneas.;

; Comentários:

I

A amostragem não fornece uma informação exata, logo, quando houver necessidade de alta precisão, a i
= amostragem não é indicada. Portanto, a alternativa A está incorreta.
i

A amostragem é recomendada quando o censo for inviável ou extremamente custoso, logo não é necessária i quando a população é pequena ou quando a característica é de fácil mensuração. Logo, as alternativas B, C i
= e D estão incorretas.

I

A alternativa E está correta porque a amostragem é, de fato, indicada para uma população numerosa, i
I

I

quando há pelo menos uma característica em comum.

I

I

: Gabarito: E

I

i (2018 - Prefeitura de Raposa/MA) Dentro do contexto da Estatística, assinale a alternativa que preenche j
= corretamente a lacuna do texto abaixo:

I

:é um valor aproximado do parâmetro e é calculado com o uso da amostra. i
= a) Variável

I

: b) Estimativa
=

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) Atributo d) População
Comentários:

O valor calculado a partir da amostra que aproxima o parâmetro populacional é a estimativa (ou estatística).
Gabarito: B

(CESPE/2013 - PC/DF) Julgue o item abaixo, a respeito de técnicas de amostragem.

Em uma amostragem sistemática cuja fração de seleção seja igual a 3 e o tamanho resultante da amostra seja igual a 125.000 observações, o tamanho da população será superior a 300.000 elementos.
Comentários:

Essa questão informa a fração de seleção, que é a razão entre o tamanho da população e o tamanho da amostra, ou seja, é o número de pessoas da população que cada elemento da amostra representa:
Sendo fs = 3 en = 125.000, o tamanho da população é:

N = fsxn = 3x 125.000 = 375.000

Que é superior a 300.000

Gabarito: Certo

L.............

Tipos de Erros

Os erros do processo de amostragem podem ser amostrais ou não amostrais, de modo que o erro total da amostragem corresponde à soma de ambos os erros.
É importante não confundir erro com viés do estimador. O viés (ou vício ou tendência)
do estimador é a diferença entre o seu valor esperado e o verdadeiro valor do parâmetro. Assim, um estimador não viesado(ou não viciado ou ainda não tendencioso) é aquele cujo valor esperado equivale ao verdadeiro parâmetro populacional. Enquanto os erros amostrais são inevitáveis no processo de amostragem, como veremos a seguir, o viés do estimador pode e deve ser evitado.
Erros Amostrais

O erro amostrai (ou margem de erro) é definido como a diferença entre o estimador,
que vamos indicar como 6, e o parâmetro populacional sendo estimado, que vamos indicar como 6:
e = 9 — 9

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Os erros amostrais são intrínsecos ao plano amostrai e ocorrem pelo simples fato de os estimadores serem variáveis aleatórias.
Esses erros podem ser controlados e mensurados com base no plano amostrai e tendem a reduzir com o aumento do número de elementos na amostra. Por exemplo, uma estimativa baseada em uma amostra de100 elementos será mais precisa (ou seja, o erro será menor) do que se fosse baseada em uma amostra de apenas 20 elementos. No limite, caso toda a população fosse analisada (censo), o erro amostrai seria nulo.
Adotando-se uma perspectiva diferente, podemos fixar o erro amostrai máximo tolerado e,
com base nele,
calcular o tamanho da amostra necessário. Quanto menor o erro tolerado, maior será a amostra.

O tamanho da amostra adequado também pode variar de acordo com o tamanho da população
- quanto maior a população, maior a amostra. Quando a população é infinita (ou muito grande em relação à amostra),o cálculo do tamanho da amostra independe do tamanho da população.

A variabilidade da população também afeta o tamanho da amostra. Quanto mais diversos são os elementos da população, mais elementos são necessários para representá-la, ou seja, maior o tamanho da amostra.
NA

PROVA!

A fórmula de Slovin permite calcular um tamanho mínimo de amostra, quando não conhecemos o comportamento da população, utilizando apenas a margem de erro E e o tamanho da população N (o resultado deve ser aproximado para cima):
N

n = -

l+N.E2

Por exemplo, para uma população de tamanho N = 10.000 e um erro máximo tolerado

E = 0,1 e obter o tamanho mínimo da amostra:

10000 íoooo „„

n = -—— = = 99

l+10000X(0,l)2 1 + 100

Erros Não Amostrais

Já os erros não amostrais, (ou erros alheios à amostragem ou erros sistemáticos)
decorrem de falhas no processo de amostragem, não podendo ser medidos e nem totalmente controlados.
Esses erros não estão relacionados com a variabilidade dos estimadores e existiriam ainda que toda a população fosse analisada. Eles podem ocorrer em qualquer tipo de amostragem.Dentre os erros não amostrais, podemos citar erros de especificação, erros de cobertura, não resposta, erros nas respostas e erros de processamento.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A especificação incorreta da população ocorre quando o pesquisador não entende a população de interesse.Por exemplo, em uma pesquisa de preferências de alimentos para crianças, indagar apenas os pais pode produzir resultados incompletos, uma vez que as crianças podem ter alguma influência nas decisões dos pais.
O erro de cobertura, que também pode ser chamado de frame error, ocorre quando a amostra não representa bem a população de interesse, seja por deixar de fora determinados grupos de interesse ou incluir elementos que não estão no escopo da pesquisa. Por exemplo, se uma pesquisa atual voltada para a classe média utilizar como referência uma lista de telefones fixos, os resultados poderão ser inadequados,pois uma parcela significativa da população, que possui apenas telefones móveis, não estará representada na amostra.
A não resposta ocorre quando uma parcela significativa da amostra não responde à pesquisa, o que pode gerar resultados tendenciosos. Pesquisas de satisfação, por exemplo, podem representar as opiniões de uma pequena parcela de clientes: aqueles que se dispõem a responder a pesquisa.
Erros nas respostas dadas pelos entrevistados podem ocorrer quando as perguntas são inadequadas, sejam elas ambíguas, constrangedoras ou formuladas para o público errado (de modo que o entrevistado não saiba responder).
Por fim, os erros de processamento podem ocorrer em qualquer fase do processo de amostragem e estão associados a falhas humanas ou de softwares na codificação, digitação,transcrição, edição etc. das informações.
Considerando os erros não amostrais, podemos definir 3 tipos de população:

* População-alvo: população a respeito da qual se deseja obter informações.

* População referenciada: população constante em um sistema de referência (cadastro). A
população referenciada pode ser diferente da população-alvo, devido a falhas no sistema.
* População de pesquisa ou amostrada: população efetivamente coberta pela pesquisa, que pode conter unidades não previstas ou unidades que tenham sido perdidas.
Para ilustrar esses conceitos, vamos supor que uma escola deseje conhecer a opinião dos seus alunos atuais(população-alvo) e para isso enviará um e-mail, contendo uma pesquisa, para uma amostra dos alunos.

Havendo erros no cadastro, como falhas na atualização do cadastro de alunos atuais,
então a população referenciada, isto é, os alunos cujos e-mails estão corretamente cadastrados, será diferente da população-alvo.

A escola também pode decidir fazer um filtro, como enviar a pesquisa apenas para os alunos com mais de12 anos, o que torna a população referenciada diferente da população-alvo.

Se determinados alunos selecionados para a amostra não responderem o e-mail e/ou houver resposta de pessoas que não estavam cadastradas no sistema, então a população de pesquisa ou amostrada será diferente da população referenciada.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

ESQUEMATIZANDO

Tipos de Erros

Erros amostrais Erros não amostrais
(sistemáticos)

* São intrínsecos ao plano amostrai

* Podem ser controlados e mensurados

* Reduzem com o aumento do número de elementos na amostra
* Decorrem de falhas no processo de amostragem

* Não podem ser controlados ou medidos

* Existem ainda que toda a população seja analisada

HORA DE

: (FCC/2015 - CNMP- Adaptada) Julgue a seguinte afirmação.

= Em qualquer tipo de amostragem, a não resposta é uma fonte potencial de erro.
i

I

I

i Comentários:

I

A não resposta é um exemplo de erro não amostrai, o qual pode ocorrer em qualquer tipo de amostragem. ;I

: Resposta: Certo

I

I

I

I

i (CESPE/2014 - ANATEL) Em junho de 2014, o Brasil registrou 275,71 milhões de linhas ativas na telefonia i
= móvel e teledensidade de 136,06 acessos por 100 habitantes. Além disso, nesse mesmo mês, houve um ;
= acréscimo de 255,08 mil linhas na telefonia móvel: os acessos pré-pagos totalizaram
212,27 milhões (76,99% j do total) e os pós-pagos, 63,44 milhões (23,01% do total). A banda larga móvel totalizou 128,49 milhões de i
; acessos, dos quais 3,27 milhões eram terminais 4G. Considerando as informações apresentadas no texto ;
= acima e supondo que um analista pretenda elaborar um plano amostrai por meio de uma amostra aleatória i
= simples sem reposição das linhas ativas na telefonia móvel com o objetivo de estimar a proporção de ligações i
= não completas em junho de 2014, julgue o item a seguir.
j

I

I

: Nos erros não amostrais que o analista poderá identificar incluem-se os erros sistemáticos.
i

I

I

i Comentários:

I

I

: Erros sistemáticos são, de fato, erros não amostrais, quais sejam, aqueles decorrentes de falhas no processo j de amostragem.;

I

I

: Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TIPoS DE AMoSTRAGEM

Para que a estimativa da população seja confiável, precisamos que a amostra extraída seja representativa,isto é, que as proporções populacionais de interesse estejam refletidas na amostra.
Para isso, a extração da amostra precisa obedecer a determinados processos.
O processo de amostragem pode ser probabilístico ou não probabilístico.

A amostragem probabilística (ou estatística ou aleatória) segue métodos rigorosamente científicos, em que cada elemento possui uma probabilidade conhecida, maior que zero, de pertencer à amostra.
Já na amostragem não probabilística, há uma escolha deliberada dos elementos da amostra, a depender do pesquisador/entrevistador. Logo, não é possível calcular a probabilidade de seleção dos elementos.
A amostragem probabilística produz resultados mais confiáveis, permitindo a extrapolação dos resultados obtidos na amostra, para toda a população, com os parâmetros estatísticos adequados.
Além disso, é possível empregartécnicas que permitem compensarfalhas no processo de amostragem (erros não amostrais), como os métodos de expansão, que permitem generalizar os resultados encontrados na amostra. Essa técnica é empregada, por exemplo, para compensar a não resposta ou a inviabilidade de se analisar determinados elementos selecionados na amostra.
I«** IX

i (2020 - Câmara de Xaxim/SC - Adaptada) Julgue as afirmativas abaixo sobre amostragem.

i I - Pela amostragem probabilística, o julgamento é usado para selecionar os itens da amostra.
i

I

I

: II - Pela amostragem não probabilística, os itens da amostra são selecionados de modo que cada unidade de i
= amostragem tenha uma probabilidade conhecida de ser selecionada.
i

I

I

i Comentários:

I

I

: O tipo de amostragem que depende do julgamento do entrevistador é a amostragem não probabilística; e i
= o tipo de amostragem em que todos os elementos apresentam uma probabilidade conhecida (maior que i
: zero) é a amostragem probabilística (ou estatística).

: Resposta: ambas as afirmativas estão incorretas.

I

; (2017 - DEMAE) Na auditoria governamental, o método de amostragem é aplicado como forma de viabilizar
= a realização de ações de controle em situações nas quais o objeto alvo se apresenta em grandes quantidades i i e/ou distribui-se de maneira pulverizada. Os métodos de amostragem são classificados em:
= a) multivariado e univariado.
i

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= b) fatorial e não fatorial.
=

= c) estatístico e aleatório.
;

I

I

d)probabilístico e não probabilístico.
i

I

i Comentários:

= Os métodos de amostragem são classificados em probabilístico e não probabilístico.

; Gabarito: D.

Tipos de Amostragem Probabilística

Nesta seção, veremos tipos probabilísticos de amostragem, isto é,
aquelas que seguem métodos rigorosamente científicos, quais sejam, (1) a amostragem aleatória simples; (2)a amostragem sistemática;

(3) a amostragem por estratificação; (4) a amostragem por conglomerados; e (5) a amostragem múltipla.
Amostragem Aleatória Simples

Na Amostragem Aleatória Simples (AAS), também chamada de casual ou acidental, cada elemento da população tem a mesma probabilidade de ser selecionado.
Esse tipo de amostragem probabilística consiste basicamente em sortear os elementos que farão parte da amostra, sendo indicado para populações homogêneas, em que todos os elementos da população são similares para os objetivos da pesquisa.
A probabilidade de um elemento qualquer ser selecionado na amostra é calculada pela razão entre tamanho da amostra n e o tamanho da população N:
Por exemplo, para uma população com N = 100 pessoas e uma amostra de tamanho n = 20, a probabilidade de um elemento qualquer ser selecionado é:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O inverso dessa probabilidade de seleção de um elemento para a amostra é chamado de peso amostrai. Por exemplo, se a probabilidade de um elemento ser selecionado na amostra for p = 0,2, então o peso amostrai será w = — = 5.
Esse conceito transmite a ideia de quantas unidades da população estão representadas em cada elemento da amostra. Para esse exemplo, cada elemento da amostra representa5 elementos da população.

Uma AAS pode ser extraída com ou sem reposição (ou repetição), ou seja, os elementos selecionados para as amostras podem ser ou não repostos ao conjunto da população.
Se a população for infinita, as extrações com e sem reposição são equivalentes, pois a retirada de elementos da população não influencia em seu tamanho, que continua sendo infinito. Na prática, temos aproximadamente essa situação quando a população é muito grande quando comparada ao tamanho da amostra.
Por outro lado, se a população for finita (e não muito grande em relação ao tamanho da amostra), esses dois procedimentos (com ou sem reposição) produzem resultados distintos.
Quando a população é infinita (ou muito grande) OU quando as amostras são extraídas com reposição, as observações da amostra são independentes. Por outro lado, quando a população é finitaE as extrações são feitas com reposição, as observações da amostra são dependentes.
Sendo N o número de elementos da população e n o número de elementos da amostra,
então o número de amostras possíveis, extraídas com reposição, é dado por:
Nn = N x N x ...x N

1 T 1

n vezes

Isso porque há sempre N possibilidades para a seleção de cada elemento,
multiplicado pelo número de elementos selecionados n (princípio multiplicativo de análise combinatória).
Por exemplo, se a população for de 100 pessoas, então para cada extração há 100
possibilidades distintas.
Se a amostra for de 3 pessoas, então o número de amostras possíveis com reposição é:

100 x 100 x 100 = 1.000.000

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Nessa situação, a probabilidade de um elemento ser incluído na amostra, em qualquer extração, é sempre a mesma, igual a:
Por outro lado, se a amostra é extraída sem reposição, o número de amostras possíveis é:

7V!

(N—ny.nl

Ou seja, corresponde às possibilidades de escolher n elementos, dentre N, no total,
como se estivéssemos selecionando todos os elementos de uma só vez. A combinação também pode ser indicada como Cfi ou
Para a mesma população de 100 pessoas e a amostra de 3 pessoas, o número de amostras distintas possíveis sem reposição é:
100!

Cl00'3 " (100 - 3)! 3!

100 x 99 x 98 x 97!

97! x 3!

100 x 99 x 98

------- - — = 100 x 33 x 49 = 161.700

^ESCLARECENDO!

Quando as amostras são extraídas com reposição, as amostras são consideradas ordenadas, ou seja, selecionar (A,B,C) é diferente (C,A,B).
Quando as amostras são extraídas sem reposição, as amostras são consideradas não ordenadas, ou seja, (A,B,C) e (C,A,B) são consideradas a mesma possibilidade.
Para a AAS sem reposição, as probabilidades variam a cada extração:

* A probabilidade de um elemento ser selecionado na primeira extração é Px = -;

* A probabilidade de um elemento, dentre os N — 1 elementos não selecionados, ser selecionado na segunda extração é: P₂ —
* A probabilidade de um elemento, dentre os N — 2 elementos não selecionados, ser selecionado na terceira extração é: P₂ = ~~
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A AAS sem reposição é considerada mais eficiente do que a AAS com reposição, pois a seleção de um mesmo elemento mais de uma vez não traz novas informações para a pesquisa.
I«** IX

r................................... . ...........................................................

: (FCC/2007 - ANS - Adaptada) Com relação à teoria geral da amostragem, julgue o item a seguir.

= Na realização de amostragem aleatória simples, as unidades amostrais são selecionadas com probabilidade i igual.:

i Comentários:

I

I

: Na amostragem aleatória simples (AAS), todos os elementos possuem a mesma probabilidade de serem ;
= selecionados.

i

I

: Resposta: Certo

I

; (CESPE/2020 - TJ-PA) Muitos sorteios virtuais são realizados em uma plataforma que gera números de i
= maneira aleatória, sendo cada número sorteado apenas uma vez com a mesma probabilidade. Essa técnica i
= é denominada amostragem

: a) estratificada.

I

b) aleatória simples com repetição.
i

I

I

: c) sistemática.

i

I

d) aleatória simples sem repetição.
i

I

i e) por conglomerados.
i

I

I

; Comentários:

I

A técnica de amostragem em que todos os elementos apresentam a mesma probabilidade de serem ;
= selecionados é a amostragem aleatória simples (AAS).
;

: Como os elementos podem ser sorteados apenas uma vez, então os elementos selecionados não são i
= repostos. Logo, temos uma amostragem sem reposição (ou repetição).

; Gabarito: D

I

I

i (CESPE/2016 - TCE-PA) Suponha que o tribunal de contas de determinado estado disponha de 30 dias para i
= analisar as contas de 800 contratos firmados pela administração. Considerando que essa análise é necessária ;
= para que a administração pública possa programar o orçamento do próximo ano e que o resultado da análise i deve ser a aprovação ou rejeição das contas, julgue o item a seguir.
I

I

: Sempre que necessário, utilize que P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Z representa a variável =
= normal padronizada.
=

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

: Em uma amostra aleatória simples de 400 elementos, o peso amostrai de cada elemento será maior ou igual
= a 2.

= Comentários:

i O peso amostrai é o inverso da probabilidade um elemento ser incluído na amostra,
dada pela razão entre o tamanho da amostra e o tamanho da população. Sabendo que a população possui N = 800contas e a amostra terá tamanho n = 400, a probabilidade de um elemento ser selecionado é:
n 400 1

E o peso amostrai é o inverso:

P ~N ~ 8ÕÕ " 2

1 1

p 1 2

Gabarito: Certo

; (FGV/2019 - DPE-RJ - Adaptada) Sobre os desenhos mais utilizados para a seleção da amostra e suas
= características, julgue a seguinte afirmativa:

: A probabilidade "a priori" de seleção de um indivíduo numa AAS é diferente quando a amostra é sem ou com
= reposição.

i Comentários:

A probabilidade de um elemento ser selecionado em qualquer extração de uma AAS com reposição é P = ^,
= em que N é o tamanho da população.

= Em uma AAS sem reposição, a probabilidade se altera a cada extração. Antes da primeira extração (a priori),
; a probabilidade de um elemento ser selecionado é também P± =

: Logo, a probabilidade é a mesma.

Resposta: Errado i (FCC/2019 - Banrisul) Uma população consiste nos 6 primeiros números inteiros estritamente positivos, ou
= seja, {1, 2, 3, 4, 5, 6}. Seja m o número de amostras aleatórias possíveis de 2 elementos que podem ser
= extraídas da população com reposição e n.2 o número de amostras aleatórias possíveis de 2
elementos que podem ser extraídas da população sem reposição. O módulo de (m - nz) é igual a j a) 49
b) 24
j c) 26

d) 30

j e) 21

iIComentários:

: Se a população consiste em N = 6 elementos e a amostra consiste em n = 2
elementos, então o número de

: amostras possíveis extraídas com reposição é:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

: ni = NxN = 6x6 = 36

= E o número de amostras possíveis extraídas sem reposição é a combinação:
í _ N!

i

^N,n (N — n)!n!

í n 6!
6x5x4! 6x5 dr_

712 _ Có'2 " (6-2)! 2! _ 4! x 2 " 2 " 15

= Logo, a diferença — n₂ é:

Hi - n₂ = 36 — 15 = 21

i Como 21 é positivo, o módulo de 21 é ele mesmo: 1211 = 21.

i Gabarito: E

fa.aaa.aaaaaa

Amostragem Sistemática

A Amostragem Sistemática é também uma amostragem probabilística, que consiste em ordenar os elementos da população, seguindo qualquer critério (por exemplo, ordem alfabética), para que possam ser identificados pela respectiva posição.
Em seguida, as amostras são extraídas periodicamente, de x em x elementos (por exemplo, de 10 em 10elementos, de 25 em 25 elementos, etc.). Essa técnica é indicada para populações homogêneas e finitas e apresenta resultados similares à AAS, em termos de precisão.
Para definir as posições dos elementos a serem extraídos, denominadas pontos de extração ou pontos de coleta, primeiro calculamos a razão entre o tamanho da população e o tamanho da amostra:
TV

R = —

n

E utilizamos a parte inteira da razão, R. Os elementos serão então extraídos de R em
R elementos. Por exemplo, para uma população de N = 20 elementos e uma amostra de n = 5 elementos, a razão é:
Para definir a posição do primeiro elemento a ser extraído (e, consequentemente, dos demais elementos),pode-se sortear (selecionar aleatoriamente) um número de 1 a R. Vamos supor, para o nosso exemplo, que tenha sido sorteado o número 3, as extrações serão realizadas nos seguintes pontos:
i) 3;

ii) 3 + 4 = 7;

iii) 7 + 4 = 11;

iv) 11 + 4 = 15;

v) 15 + 4 = 19

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Os pontos de extração seguem uma Progressão Aritmética, com razão R. Assim, o ponto de extração do n-ésimo elemento selecionado pode ser calculado como:

An = Ai + (« - 1) x R

Para o nosso exemplo, tivemos R = 4 e Ar = 3. Assim, a posição do 59 elemento selecionado é:

A₅ = 3 + 4x4 = 19

Ou seja, o 52 elemento selecionado será o 195 elemento populacional, como vimos antes.

Esse procedimento pode ser visto como a divisão dos N = 20 elementos da população em n = 5 grupos de
R = 4 elementos cada, sendo selecionado o 39 elemento de cada grupo, como representado abaixo:

Também podemos visualizá-lo como a divisão dos TV = 20 elementos da população em R =
4 grupos de n = 5 elementos cada, sendo selecionado o 3Q grupo, do qual todos os membros serão analisados (como na amostragem de conglomerados que veremos posteriormente):
INDO MAIS

FUNDO!

Como as amostras são extraídas periodicamente, se houver uma periodicidade nos dados,
os elementos selecionados podem não ser uma boa representação de toda a população.

Por exemplo, vamos supor que o objetivo seja estimar a média anual de chuvas em determinada região, com base nos dados históricos. Se fizermos uma amostragem sistemática com intervalos de 12 meses, obteremos as informações de apenas 1 mês no ano. Como a quantidade de chuva é sazonal, a estimativa para o ano não será boa.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (FCC/2007 - ANS -Adaptada) Com relação à teoria geral da amostragem, julgue o item a seguir.

A amostragem sistemática é sempre menos precisa do que a amostragem aleatória simples.

i Comentários:

I

I

A amostragem sistemática é uma técnica probabilística, assim como a amostragem aleatória simples. Ambas i
; são similares em termos de precisão.

j Resposta: Errado.

I

I

; (FGV/2019 - DPE-RJ - Adaptada) Sobre os desenhos mais utilizados para a seleção da amostra e suas i
= características, julgue a seguinte afirmativa:
i

I

A amostragem sistemática tem como fragilidade o fato de que apenas a seleção do primeiro indivíduo é ;
; probabilística.

i

I

i Comentários:

I

I

A amostragem sistemática é totalmente probabilística, e não somente para a seleção do primeiro elemento, i

: Resposta: Errado

I

I

I

I

; (2021 - Prefeitura de Porto Alegre/RS)Assinale a alternativa que indica uma desvantagem da técnica de j
= amostragem sistemática.
i

I

i a) Não ser probabilística.
i

I

I

b) Exigir grandes tamanhos de amostragem.
;

I

: c) Podem ocorrer problemas se existir algum tipo de periodicidade oculta.
i d) Alta complexidade.;

: e) Erro elevado i

I

i Comentários:

I

I

A amostragem sistemática é probabilística (logo, a alternativa A está errada)
e pode ser aplicada para j

= qualquer tamanho de amostra (logo, a alternativa B está errada).
i

I

: Ela também não é complexa e não apresenta erro elevado (alternativas D e E erradas).
i

= Porém, se houver alguma periodicidade nos dados, a amostra selecionada pode não representar bem a ;população.
=

I

I

; Gabarito: C

I

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= (FGV/2022-TJDFT) Um Tribunal de Justiça deseja obter uma amostra de tamanho 3.000
de uma população =I
de 60.000 ações. Esse Tribunal possui um cadastro em que cada ação está associada,
sequencialmente, a um ;

: número (começando com o número 1 e terminando com o número 60.000). De posse do referido cadastro i
= e considerando o tamanho da amostra solicitada, o pesquisador utilizou o seguinte procedimento para a i
= seleção da amostra:

Item. 1. Determinou o intervalo de seleção da amostra dividindo o total da população pelo tamanho da amostra: ;60.000/3.000=20;

= 2. Elegeu aleatoriamente um número inteiro, entre [1, 20]. Essa foi a primeira ação selecionada;

I

i 3. A próxima ação selecionada foi definida pela soma do intervalo de seleção ao número selecionado na i i etapa 2.;

= E, assim, sucessivamente, foram determinados os próximos elementos,
acrescentando-se ao selecionado i

= anteriormente o intervalo de seleção da amostra. O número escolhido na etapa de número 2 foi 17; logo, a i
= primeira ação selecionada foi a de número 17; a seguinte, a de número 37, seguida da de número 57, e assim j
= sucessivamente.
;

I

: O milésimo elemento selecionado nessa amostra foi a ação de número:
i í a) 19.937;
b) 19.957;

i c) 19.977;

d) 19.997;

í e) 20.017.

: Comentários:

: O enunciado descreve a amostragem sistemática, em que primeiro calculamos a razão R
entre o número de j

= elementos da população e o número de elementos da amostra (aqui, temos
R = 20); e, em seguida, i i selecionamos aleatoriamente a posição do primeiro elemento (aqui, temos Ai = 17).;

A posição do n-ésimo elemento pode ser calculada, utilizando-se a fórmula da Progressão Aritmética:

i An = A₁ + (n - 1) x R
;

= Para A₁ = 17,n— 1000 e R = 20, temos:

>liooo = 17 + 999 x 20 = 17 + 19980 = 19997

; Gabarito: D

Amostragem por Estratificação

A amostragem por estratificação (ou estratificada) é aplicável para populações heterogêneas, isto é, que apresentam perfis distintos em relação ao objeto do levantamento.
Para aplicar a amostragem estratificada, a população deve ser segmentada em grupos, denominados estratos (ou subpopulações), de modo que os elementos de um mesmo estrato sejam homogêneos(similares entre si, com baixa variabilidade) e que os diferentes estratos sejam heterogêneos (diferentes,com alta variabilidade).

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A amostragem estratificada consiste em extrair uma amostra, utilizando uma técnica de probabilística, como a amostragem simples, de cada estrato.
O objetivo desse procedimento é obter estimativas mais precisas para populações com as citadas características. Quanto mais homogêneo forem os elementos dentro de cada estrato e mais heterogêneos forem os diferentes estratos, mais eficiente será o plano amostrai, ou seja, o erro amostrai será menor.
Por exemplo, para uma população de NT = 20 pessoas, sendo 10 homens e 10 mulheres,
temos um estrato para os 10 homens e outro para as 10 mulheres. Em seguida, sorteamos 2 elementos,por exemplo, do estrato dos homens e 2 elementos do estrato das mulheres, como ilustrado abaixo:
ffl m n n ÃL)A III <7 C)

Na figura, podemos observar que os elementos de um mesmo grupo são similares e que os grupos são diferentes entre si. Além disso, observamos que selecionamos apenas alguns elementos (no caso, 2) de cada estrato.
Mas os tamanhos dos estratos (também chamados de área) não precisam ser iguais,
como no exemplo acima. Vamos supor agora uma população de NT = 100 pessoas, das quais NAita = 10possuem alta renda,
NBaixa = 50 possuem baixa renda e NMédia = 40 são de classe média.

E como definimos o tamanho da amostra de cada estrato?

A amostra pode ser de mesmo tamanho para todos os estratos, o que chamamos de amostragem uniforme.

Para o nosso exemplo, em uma amostragem uniforme, poderíamos selecionar nAita = nBaixa
= nMédia = 3
elementos de cada estrato.

Alternativamente, a amostra pode ser proporcional ao tamanho do estrato,
o que chamamos de amostragem proporcional.
Para o nosso exemplo, podemos definir uma amostra total de nT = 10 pessoas, extraída proporcionalmente ao tamanho de cada estrato. Para isso, primeiro calculamos a proporção entre a amostra total desejada nTe a população total NT\

Esse percentual será o mesmo para todos os estratos. Assim, o tamanho da amostra para cada é:

nAlta = NAita x p = 10 X 0,1 = 1

^Baixa — NBaixa X p - 50 X 0,1 — 5

W-Média NMédia X p — 40 X 0,1 4

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Generalizando para um estrato x qualquer e substituindo p pela sua razão p = —, o tamanho da amostra nx pode ser calculado como:
Com uma pequena reorganização, podemos escrever a fórmula como:

Dessa forma, consideramos que a amostra do estrato x é a razão entre a população do estrato x e a população total, multiplicada pelo tamanho total da amostra.
Para o nosso exemplo, a amostra da população de baixa renda nBaixa pode ser vista como a razão entre o tamanho da população de baixa renda NBaixa = 50 e o tamanho da população total NT = 100, cujo resultado é NBaixa = 0,5, multiplicado pelo tamanho total da amostra n = 10:
Nt

^Baixa

W-Baixa ~ TIt X

t

10 x 0,5 = 5

O resultado é o mesmo, como era de se esperar. Então, por que estamos discutindo isso?

Bem, mudamos um pouquinho o ponto de vista da amostragem proporcional porque vamos utilizar esse segundo raciocínio para calcular o tamanho da amostra de um terceiro tipo de amostragem estratificada,que é a amostragem ótima (de Neyman).

Nesse tipo de amostragem, o tamanho amostrai de cada estrato depende tanto do tamanho populacional,quanto da sua variabilidade, medida pelo desvio padrão. Ou seja, para estratos com maior variabilidade as amostras são maiores para uma melhor representação das diferentes características.
Para calcular o tamanho da amostra por estrato, temos uma fórmula parecida com a que acabamos de ver para a amostragem proporcional, mas precisamos multiplicar o tamanho de cada estrato pelo respectivo desvio padrão:
— Tlj1 X NxxPx liNiXDt
Vamos supor que o desvio padrão da população de alta renda seja DAita = 4, da população de baixa renda sejaDBaixa = 2 e da população de classe média seja DMédia = 1.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Havendo NT = 100 pessoas no total, das quais NAita = 10 possuem alta renda, NBaixa = 50 possuem baixa renda e Niviédia = 40 são de classe média, vamos calcular o denominador da fração acima.Para isso, multiplicamos o tamanho populacional e o desvio padrão de cada estrato e somamos os produtos:
D Baixa) "I" (NMédia * Média)

i

^NL x Dt = (10 x 4) + (50 x 2) + (40 x 1) = 40 + 100 + 40 = 180

i

Considerando que a amostra total é de nT = 10 pessoas, então os tamanhos amostrais dos estratos são
, Mlta x ^Alta n .,

X ,T = 10 X

£lNlxDl

Baixa ^-T

NBaixa * ^Baixa

YiNiXDi

= 10

nMédia — nT

NMédia * ^Média

X

YíNíXDí

= 10

A amostragem ótima possui o menor erro amostrai, dentre as técnicas de amostragem estratificada,enquanto a amostragem uniforme possui o maior erro amostrai delas (a amostragem proporcional apresenta erro amostrai intermediário).
I«** IX

..............................................................................................i i (FCC/2013 - SEFAZ/SP - Adaptada) Julgue o item a seguir.
= Na amostragem aleatória estratificada, a população é dividida em estratos, usualmente, de acordo com os i
= valores ou categorias de uma variável, e, depois, uma amostragem aleatória simples é utilizada na seleção i de uma amostra de cada estrato.i

I

: Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

I= Na amostragem aleatória estratificada, a população é dividida em estratos, de acordo com algum critério
: (por exemplo, idade, sexo, etc.) e uma amostragem aleatória é utilizada para selecionar uma amostra de i cada estrato.Resposta: Certo i (FCC/2007 - ANS - Adaptada) Com relação à teoria geral da amostragem, julgue o item a seguir.
I

Amostragem estratificada consiste na divisão de uma população em grupos segundo alguma característica
: conhecida. Os estratos da população devem ser mutuamente exclusivos.

i Comentários:

I

: Na amostragem aleatória estratificada, a população é dividida em grupos,
chamados estratos, sem

= interseção entre eles (mutuamente exclusivos).

Resposta: Certo

; (FCC/2015 - CNMP- Adaptada) Julgue a afirmação a seguir.

: Na amostragem estratificada fica assegurado que cada extrato esteja representado na amostra global mas
= não fica assegurado que todas as unidades de estudo tenham a mesma probabilidade de serem selecionadas.

i Comentários:

I

: Na amostragem aleatória estratificada, cada extrato da população será representado na amostra, mas nem todos os elementos de toda a população possuem a mesma probabilidade de serem selecionados.

Resposta: Certo

(CESPE/2020 - TJ-PA) Um professor de educação física realizou uma pesquisa a respeito das alturas dos estudantes da instituição de ensino onde trabalha. A instituição possui 1.285estudantes, dos quais 535 são homens e 750 são mulheres. Para realizar essa pesquisa, foi selecionada uma amostra de257 estudantes pelo método de amostragem estratificada com alocação proporcional, considerando-se os estratos homem e mulher. Nessa situação, foram selecionados a) 107 homens e 150 mulheres b) 128 homens e 129 mulheres
I

c) 110 homens e 147 mulheres d) 150 homens e 107 mulheres
I

e) 129 homens e 128 mulheres

E

Comentários:

I

Para calcular o tamanho da amostra de cada estrato, em uma amostragem estratificada proporcional,primeiro calculamos a proporção do tamanho total da amostra em relação ao tamanho total da população:
1285

= 0,2

Essa é a proporção a ser mantida para ambos os estratos. Logo, o tamanho da amostra de cada estrato é:
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Homens P X N^omens 0,2 X 535 107

^Mulheres P X NMulheres X 750 150

Gabarito: A

i (CESPE/2020 - TJ-PA) Uma população é dividida nos estratos I, II e III. O estrato
I é composto por 400

= elementos; o II, por 600 elementos; e o III, por 1.000 elementos. Conforme um estudo piloto, os desvios
; padrão da variável de interesse nos estratos I, II e III são, respectivamente, 10, 20 e 8.

I

: Caso um pesquisador pretenda retirar uma amostra aleatória de 240 elementos dessa população utilizando
: a locação ótima de Neyman, os tamanhos das amostras a serem extraídas dos estratos
I, II e III devem ser,

= respectivamente,
a) 40, 30 e 170

b) 40, 120 e 80

í c) 48, 72 e 120

d) 79, 81 e 80

e) 50, 75 e 115

; Comentários:

I

: Essa questão trabalha com a alocação estratificada ótima, em que o tamanho amostrai do estrato x é:í
Nxx Dx

= O enunciado informa que:

i * O tamanho da população do estrato I é Ni = 400

i * O tamanho da população do estrato II é Nu = 600

i * O tamanho da população do estrato III é Nm = 1000
i * O desvio padrão da população do estrato I é Di = 10

i * O desvio padrão da população do estrato II é Dn = 20
i * O desvio padrão da população do estrato III é Dm = 8

I

Com essas informações, podemos calcular o denominador da fórmula, que corresponde ao somatório dos produtos dos tamanhos populacionais de cada estrato, multiplicados pelos respectivos desvios padrão:
xA = (Af, x D,) + (Nn x D„) + (NUI

i x £>///)
y Ni x Dt = (400 x 10) + (600 x 20) + (1000 x 8) = 4000 + 12000 + 8000 = 24000

= Considerando que o tamanho total da amostra é nT = 240, os tamanhos amostrais são:
i N,xD,
400 x 10 4000

: H.J = nT x =r—---------— = 240 x -777777777— =
77777- = 40

: 1 T £iNixDi

24000 100

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Ntt X Drr n,' =UtX XiNiXDi = 240
600 x 20 12000

x = = 120
24000 100

Mzz X ^IIl n A n

_1_0_0_0_x 8_ — _8_0_0_0_ — on n,u-nT
ˣ&N.xDl

- 240 x

24000 100

Gabarito: B

Amostragem por Conglomerados

Assim como a amostragem estratificada, a amostragem por conglomerados também é aplicável a populações heterogêneas, divididas em grupos. Além disso, utiliza-se uma técnica de amostragem probabilística, normalmente a AAS, para selecionar a amostra.
Porém, ao contrário da amostragem estratificada, na amostragem por conglomerados,
os grupos são homogêneos (similares entre si, com baixa variabilidade), enquanto os elementos de um mesmo grupo são heterogêneos (diferentes, com alta variabilidade). Assim, cada grupo, que chamamos de conglomerado ou cluster, pode ser considerado uma pequena representação de toda população.
Para estudar os salários dos colaboradores que trabalham em montadoras, por exemplo,
podemos agrupá-
los de acordo com suas empresas (elas formarão os conglomerados). As diferentes empresas apresentam características similares (homogêneas) e, dentro de cada empresa, os salários dos colaboradores são bem distintos (heterogêneas).
Analogamente ao que vimos para a amostragem estratificada, quanto mais heterogêneos forem os elementos dentro de cada conglomerado, e mais homogêneos forem os conglomerados, menor o erro amostrai, ou seja, mais eficiente o plano amostrai.
Outra diferença entre as duas técnicas de amostragem é que, na amostragem estratificada, aplica-se uma técnica de amostragem para selecionar alguns elementos de cada estrato. Por outro lado,na amostragem por conglomerados, aplica-se uma técnica de amostragem para selecionar alguns conglomerados, dos quais todos os elementos são analisados.
Para o nosso exemplo, selecionaríamos algumas empresas para analisar os salários de todos os seus colaboradores.
Consequentemente, enquanto na amostragem estratificada, cada indivíduo (no caso,
cada colaborador) é uma unidade amostrai, na amostragem por conglomerados, as unidades amostrais são os próprios conglomerados (no nosso exemplo, as empresas).
Assim, o tamanho da amostra, isto é, o número de unidades amostrais selecionadas, é o número de conglomerados selecionados.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A figura a seguir ilustra a amostragem por conglomerados, para uma população de 10
conglomerados, dos quais 2 são selecionados para a amostra (logo, o tamanho da amostra é igual a 2):
IWI IWI fll IWI

( fll IWI (li fll )

ffi ffi IWI ffi rwi rwi rwi rwi iwnwnwnwi

IWI fWl 1* IWI

IWI IWI IWI IWI

IWI 1* 1* IWI

iwi iwi IwI iwi

C * * * *]

xjWl IWI X

Na figura, podemos observar que os elementos de um mesmo grupo são diferentes entre si e que os grupos são similares. Além disso, observamos que 2 grupos são selecionados e todos os seus elementos são analisados.
Esse tipo de amostragem por conglomerados, em que analisamos todos os elementos dos conglomerados selecionados, é chamada de amostragem por conglomerados em um estágio.
Se não for possível analisar conglomerados inteiros, podemos subdividir os conglomerados selecionados em novos grupos, preservando as mesmas características de homogeneidade entre grupos e heterogeneidade dentro de cada grupo. Podemos efetuar essa subdivisão sucessivamente, até que todos os elementos de um grupo possam ser analisados. Essa técnica é chamada de amostragem por conglomerados em múltiplos estágios.
Vamos supor que o objetivo seja avaliar o desempenho de alunos do 99 ano nas escolas públicas do país.Para isso, podemos dividir toda a população de escolas de acordo com seus respectivos
Estados e selecionar alguns Estados para a amostra. Esse seria o l9 estágio da amostragem por conglomerados.
Como não é viável analisar as escolas públicas de um Estado inteiro,
podemos aplicar novamente a amostragem por conglomerados, subdividindo as escolas dos Estados selecionados no l9estágio, de acordo com seus Municípios. Em seguida, selecionamos alguns Municípios, dentre os Estados que haviam sido selecionados no l9 estágio, e avaliamos todas as escolas dos Municípios selecionados,que corresponde ao
29 estágio da amostragem por conglomerados.

Quando utilizamos a amostragem por conglomerados em dois estágios, teremos unidades amostrais primárias, aquelas selecionadas no primeiro estágio; e unidades amostrais secundárias, aquelas selecionadas no segundo estágio. Para o nosso exemplo, os Estados são as unidades amostrais primárias; e os Municípios, as secundárias.
Para utilizar a amostragem por conglomerado, deve haver uma lista dos conglomerados, não sendo necessária uma lista identificando todos os elementos da população, como nas demais técnicas de amostragem, e, por isso, tende a apresentar custos mais baixos.
Além disso, quando os custos de análise da amostra aumentarem conforme a distância entre os elementos(por exemplo, quando a análise exigir a presença física para a análise do elemento),
a amostragem por conglomerados tende a apresentar custos ainda menores do que as demais técnicas probabilísticas.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para ilustrar, vamos considerar novamente o nosso exemplo dos salários dos colaboradores. Poderíamos aplicar a amostragem por estratificação, dividindo a população nos diferentes grupos salariais e, em seguida,selecionando aleatoriamente elementos de cada grupo. Os elementos selecionados poderiam ser dos mais diversos países existentes, o que corresponderia a altos custos, caso a análise do elemento selecionado precisasse ser in loco. Já para a amostragem por conglomerados, podemos selecionar cidades específicas e efetuar as análises somente nesses locais., reduzindo os custos da pesquisa.
ESQUEMATIZANDO

Amostragem Estratificada Amostragem por Conglomerados

* Elementos homogêneos dentro de cada grupo
(estrato)

* Seleção de alguns elementos de cada grupo,
conforme o tipo de alocação (uniforme,
proporcional ou ótima)

* As unidades amostrais são os elementos

* Elementos heterogêneos dentro de cada grupo
(conglomerado)

* Seleção de alguns grupos, dos quais todos os elementos são analisados
* As unidades amostrais são os conglomerados

* Baixo custo, principalmente quando este aumenta com a distância
Ã(Ã)i |A Ã(Ã)Ã||Ã Ã(Ã)Ã(Ã)Ã i i

NA

PROVA!

Para comparar a variação dos elementos intragrupos com a variação entre os grupos,

utiliza-se o coeficiente de correlação intraconglomerados r, em que 0 < r < 1.

Quanto maior o coeficiente, menor a variação intragrupos (elementos de cada grupo mais homogêneos).
Para r = 0, toda a variância da população é explicada pela variância intragrupos e não há variância entre os grupos; para r = 1, toda a variância é explicada entre os grupos e não há variância intragrupos.
Em inventários florestais, recomenda-se a amostragem por estratificação para r > 0,4; e a amostragem por conglomerados, caso contrário.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (FCC/2007 - ANS -Adaptada) Com relação à teoria geral da amostragem, julgue o item a seguir.
i

= Em uma amostra por conglomerados, a população é dividida em subpopulações distintas.
j i Comentários:
I

I

: Naamostragem por conglomerados, os grupos (conglomerados) são compostos de elementos distintos i

: (heterogêneos).
j

: Resposta: Certo

I

I

; (2017 - CRP 7? Região - Adaptada) Em estudos numéricos, somente as amostragens probabilísticas i
= permitem a correta generalização para a população dos resultados amostrais. Considerando essa i
; informação, julgue a alternativa a seguir.

= Na amostragem aleatória por conglomerados, se os elementos mostrais são os alunos,
os conglomerados i podem ser as respectivas escolas.i

I

I

; Comentários:

: Na amostragem por conglomerados, a população é dividida em subgrupos formados por elementos ;
i heterogêneos, sendo os subgrupos homogêneos entre si, como ilustrado a seguir:

ffl ffl ffl «I

ffl ffl ffl ffl ffl ffl ffl ffl ffl ffl ffl ffl ffl ffl ffl ffl ffl ÍW) ffl «I
ffl ffl ffl ffl ffl ffl ffl ffl
: As escolas podem ser consideradas conglomerados (os retângulos ilustrados acima), pois são homogêneas i
= entre si, enquanto os alunos de cada escola são elementos heterogêneos (são de anos/idades distintos, por ;
= exemplo).
j

= Resposta: Certo.

I

I

I

I

; (FGV/2019 - DPE-RJ - Adaptada) Sobre os desenhos mais utilizados para a seleção da amostra e suas j
= características, julgue a seguinte afirmativa:
i

I

I

A amostra por conglomerados tem como principal restrição 0 custo de extração, que costuma ser elevado, i
I

I

; Comentários:

A amostragem por conglomerados tende a ser menos custosa, principalmente quando os custos da análise i
; aumentam com a distância entre os elementos selecionados.
i

I

I

i Resposta: Errado

L............................ .. .................

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Amostragem Múltipla

Na amostragem múltipla, as amostras são extraídas em etapas sucessivas e, dependendo dos resultados observados, as etapas posteriores podem ser dispensadas. Essa técnica é utilizada na inspeção por amostragem, isto é, quando é necessário tomar uma decisão sobre aceitar ou não um lote de produtos, com base na inspeção de apenas alguns elementos.
Por exemplo, vamos supor que uma empresa receba um lote de 1000 produtos do seu fornecedor, os quais devem atender a determinadas exigências de qualidade. Essa empresa irá aceitar o lote se essas exigências forem atendidas e rejeitá-lo, caso contrário. Se não for viável inspecionar todos os produtos do lote, a empresa poderá inspecionar apenas alguns itens e, com base nos resultados encontrados, decidir se irá aceitar ou rejeitar o lote.
A empresa poderia decidir realizar uma amostragem única, selecionando 50 elementos, por exemplo, para serem inspecionados. Alternativamente, a empresa pode utilizar uma amostragem dupla (que é um tipo de amostragem múltipla), optando por 2 amostras de 25 elementos, extraídas em etapas sucessivas (uma após a outra). A partir dos resultados da primeira amostra, a empresa irá decidir se vai aceitar o lote, rejeitá-lo ou extrair a segunda amostra.
Essa técnica pode ser estendida para múltiplas amostras sequenciais. No caso, a empresa pode optar pela extração sequencial de 5 amostras com 10 elementos cada. Após a análise de cada amostra, a empresa decide se irá aceitar o lote, rejeitá-lo ou extrair uma nova amostra.
O objetivo da amostragem múltipla é diminuir o número de elementos inspecionados a longo prazo,
reduzindo, assim, os custos de inspeção.

Um caso extremo dessa técnica é a amostragem sequencial, em que um único elemento é selecionado e inspecionado por vez, até que seja tomada a decisão de aceitar ou rejeitar o lote, com o objetivo de minimizar o número de elementos inspecionados a longo prazo.
I«** IX

i (FGV/2017 - IBGE) Dentre os métodos de amostragem probabilística, podem ser destacados os de amostras i i aleatórias simples, sistemáticas, por estratos, por cluster e múltipla.i

= Sobre cada um desses métodos, e nessa mesma ordem, poderiam ser associadas,
relativamente, as seguintes j

= palavras-chave ou expressões:
i

I

I

í a) equiprováveis, periodicidade, grupos homogêneos, grupos heterogêneos e sequencial;
=

: b) uniforme, sem cadastro, maior variância por grupo, menor variância por grupo e parada endógena;
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= c) uniforme, periodicidade, menor custo, maior custo e geométrica;

d) hipergeométrica, cadastral, grupos homogêneos, grupos heterogêneos e geométrica;

I

: e) equiprováveis, periodicidade, grupos heterogêneos, grupos homogêneos e "por etapas".

i Comentários:

I

: Na amostragem aleatória simples (AAS), a probabilidade de seleção de um elemento é a mesma para todos
= os elementos, ou seja, os elementos são equiprováveis.

= Na amostragem sistemática, os elementos são selecionados em períodos iguais, ou seja,
a seleção é

= periódica (periodicidade).

Ê Na amostragem por estratos, os grupos são compostos de elementos homogêneos; e na amostragem por i conglomerados ou cluster, os grupos são compostos de elementos heterogêneos.
: Na amostragem múltipla, as amostras são extraídas em etapas sequenciais.

j Gabarito: A

Resumo

Tipos de Amostragem Probabilística

Segue métodos científicos; probabilidade de qualquer elemento ser selecionado é maior que zero

* Amostragem Aleatória Simples: os elementos possuem a mesma probabilidade de seleção

* Amostragem Sistemática: elementos ordenados e selecionados periodicamente

* Amostragem Estratificada: divide população em grupos compostos de elementos similares; são selecionados alguns elementos de cada grupo (seguindo método probabilístico)
* Amostragem por Conglomerados: divide população em grupos compostos de elementos distintos; são selecionados alguns grupos (seguindo método probabilístico), dos quais todos os elementos são analisados
* Amostragem Múltipla: amostras extraídas em sequência; com base nos resultados de cada amostra, toma-se decisão de aceitar o lote, rejeitá-lo ou extrair nova amostra
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

TIPoS DE AMoSTRAGEM NÂo PRoBABILÍSTICA

Nesta seção, veremos tipos não probabilísticos de amostragem, quais sejam aqueles que envolvem uma escolha deliberada do pesquisador/entrevistador e não seguem métodos científicos rigorosos. Esses métodos são indicados quando os métodos probabilísticos não forem possíveis ou viáveis, por exemplo,quando a população alvo não for conhecida ou quando parte dela estiver inacessível.

Amostragem por Conveniência

A amostragem por conveniência, também chamada de amostragem por acessibilidade,
depende da conveniência do pesquisador, não havendo critérios científicos pré-definidos. A sua grande vantagem é a sua praticidade.
Um exemplo clássico desse método é a pesquisa em um local de grande circulação de pessoas, em que as pessoas selecionadas para a entrevista (ou seja, a amostra selecionada), são aquelas que passam perto do entrevistador e concordam com a entrevista.
Alguns chamariam essa seleção de aleatória, no sentido de incerto, imprevisível.

Porém, para que a seleção seja efetivamente aleatória, é necessário que todos os elementos tenham a mesma probabilidade de ser selecionado, o que não ocorre na amostragem por conveniência.
I«** IX

i (VUNESP/2018 - Prefeitura de Serrana/SP) De modo geral, as pesquisas sociais abrangem um universo de i
= elementos tão grande que se torna impossível considerá-los em sua totalidade. Por isso, nesse tipo de i
= pesquisa, é muito frequente o trabalho com os diversos tipos de amostragem. A amostragem por j
= acessibilidade ou por conveniência i
I

I

í a) é uma variação da amostragem aleatória simples.
i

: b) pode ser proporcional ou não proporcional.
=

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

= c) é destituída de qualquer rigor estatístico.
=

d) é o procedimento básico de amostragem científica.
;

I

I

: e) compara vários estratos de uma população.
i

I

i Comentários:

A amostragem por acessibilidade ou conveniência é uma amostragem não probabilística, sem qualquer j i critério científico pré-definido.
I

I

; Gabarito: C

Amostragem por Julgamento

Na amostragem por julgamento, a seleção dos elementos para a amostra é feita com base nos critérios definidos pelo entrevistador. Por exemplo, o entrevistador pode decidir selecionar pessoas com determinados aspectos visuais (como cor de pele ou altura), algum comportamento específico (pessoas que estejam se exercitando ou na frente de vitrine de alguma loja), frequência em determinados lugares (pessoas que estejam em determinada feira ou em algum parque), etc.
Enquanto na amostragem por conveniência não há qualquer critério pré-definido, sendo a seleção feita por simples conveniência do pesquisador, na amostragem por julgamento, existe um critério,mas ele é definido pelo próprio entrevistador.
Amostragem por Cotas

Na amostragem por cotas, as amostras seguem as mesmas proporções dos subgrupos da população, assim como a amostragem estratificada proporcional (tipo probabilístico de amostragem).Ou seja, essas proporções devem ser conhecidas pelo pesquisador.
Porém, diferentemente da amostragem estratificada, em que se aplica uma técnica probabilística para selecionar os elementos de cada estrato, na amostragem por cotas, utiliza-se um método não probabilístico.
I«** IX

r f í (FGV/2019 - DPE-RJ - Adaptada) Sobre os desenhos mais utilizados para a seleção da amostra e suas i
= características, julgue a seguinte afirmativa:
i

I

I

: A amostragem por cotas é uma forma de seleção estratificada, também apoiada em critérios probabilísticos. =
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Comentários:

Na amostragem por cotas, as amostras seguem as mesmas proporções da população, como na amostragem estratificada, porém, a amostragem por cotas não segue critérios probabilísticos.
Resposta: Errado.

(CESPE/2011 - FUB) Com relação às técnicas de amostragem de populações finitas, julgue o seguinte item.
As amostragens aleatórias simples, sistemática, estratificada e por cotas representam planos de amostragem probabilísticos.
Comentários:

As amostragens aleatória simples, sistemática e estratificada são probabilísticas,
mas a amostragem por cotas é não probabilística.
Gabarito: Errado.

(2021 - Prefeitura de Porto Alegre/RS) As técnicas de amostragem podem ser classificadas como amostras probabilísticas e amostras não probabilísticas. São, respectiva mente, uma técnica probabilística e uma técnica não probabilística:
a) Amostra aleatória simples e amostra sistemática.

b) Amostra por cotas e amostra por julgamento.

c) Amostra por conglomerado (cluster) e amostra por cotas.

d) Amostra aleatória simples e amostra por conglomerado (cluster).

e) Amostra por cotas e amostra por conveniência.

Comentários:

O enunciado pede uma amostragem probabilística primeiro e uma não probabilística depois.

Em relação à alternativa A, tanto a amostra aleatória simples quanto a amostra sistemática são probabilísticas, logo, a alternativa A está incorreta.
Em relação à alternativa B, tanto a amostra por cotas quanto a amostra por julgamento são não probabilísticas, logo a alternativa B está errada.
Em relação à alternativa C, a amostra por conglomerado é probabilística e a amostra por cotas é não probabilística, logo a alternativa C está certa.
Em relação à alternativa D, tanto a amostra aleatória simples quanto a amostra por conglomerado são probabilísticas, logo a alternativa D está errada.
Em relação à alternativa E, tanto a amostra por cotas quanto a amostra por conveniência são não probabilísticas, logo a alternativa E está errada.
Gabarito: C

L.................................................

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Amostragem por Tipicidade

A amostragem por tipicidade também é um tipo não probabilístico de amostragem,
aplicável a populações divididas em subgrupos. Porém, neste caso, o pesquisador seleciona elementos que ele considera representativos dos subgrupos da população. Logo, é necessário que o pesquisador tenha algum conhecimento prévio da população.
Por exemplo, para estudar os salários de um grupo de colaboradores, o pesquisador pode selecionar um funcionário que recebe 1 salário-mínimo, um funcionário que recebe 5 salários-mínimos e um que recebe 10salários-mínimos, para representar as diferenças salariais dessa população.

Amostragem por Voluntários

Na amostragem por voluntários, os próprios indivíduos da população se voluntariam para participar da pesquisa. Em outras palavras, em vez de o pesquisador selecionar o indivíduo, o próprio indivíduo decide participar voluntariamente da pesquisa. Isso é comum nas pesquisas pelas redes sociais sobre questões como política, religião etc.
Embora esse tipo de amostragem seja de fácil coleta e apresente baixo custo, os resultados não apresentam boa representatividade.
Amostragem por Bola de Neve

Na amostragem por bola de neve, o pesquisador seleciona alguns indivíduos iniciais e esses indivíduos convidam novos participantes, normalmente, dentre os seus conhecidos. Assim como uma bola de neve vai crescendo ao descer uma ladeira repleta de neve, a amostra selecionada com base nessa técnica também cresce conforme os indivíduos selecionados convidam novos participantes.
Esse processo apresenta baixo custo, pois são os próprios participantes que selecionam a amostra. Porém,essa característica leva a uma falta de controle sobre as características e o tamanho da amostra. Assim, a amostra pode não ser uma boa representação da população como um todo.
A amostragem por bola de neve é indicada para populações de baixa incidência, isto é, quando a característica que estiver sendo buscada for rara; ou de difícil acesso. Para estudar uma doença rara, por exemplo, o pesquisador dificilmente conhecerá toda a população para aplicar uma técnica aleatória de seleção dos indivíduos; ou mesmo terá informações para aplicar outras técnicas não probabilísticas mais elaboradas. Porém, ao selecionar alguns indivíduos com a doença, é bem possível que esses conheçam outras pessoas com a mesma doença e possam convidá-los a participar do estudo.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

l«** IX

i (FGV/2017 - IBGE) Dentre os métodos de amostragem não probabilística, podem ser destacados os i
= realizados por conveniência, por cotas, por julgamento, por tipicidade e as bolas de neve.
;

I

I

: Sobre cada um dos métodos, e nessa exata ordem, poderiam ser associadas às seguintes palavras-chave ou i i expressões:
i

= a) praticidade, efeito de estratificação, arbitragem, para um subgrupo e indicações técnicas;

b) proximidade, juízo de valor, para um subgrupo, avaliações em sequência e baixíssimo custo;

I

I

: c) baixo custo, arbitragem, seleção endógena, efeito cluster e para um subgrupo;
;

d) seleção endógena, para um subgrupo, indicações técnicas, efeito de estratificação e efeito cluster;

I

: e) proximidade, avaliações em sequência, baixíssimo custo, efeito de estratificação e longa duração.
I

i Comentários:

I

I

A amostragem por conveniência não segue critério específico, sendo utilizado por sua praticidade.

I

: Na amostragem por cotas, as amostras são proporcionais aos estratos da população.
i

I

I

: Na amostragem por julgamento, o pesquisador seleciona a amostra com base em seu julgamento,
arbítrio, j

: Na amostragem por tipicidade, o pesquisador seleciona elementos que ele entende representar os ;
= subgrupos da população.

I

I

: Na amostragem por bola de neve, a amostra é paulatinamente selecionada com base nas indicações dos j
= participantes.

i

I

: Logo, a alternativa A está correta.
i

I

I

: Gabarito: A.

L...................................................................................................
............................................................... 1

Resumo

Tipos de Amostragem Não Probabilística

Dependem de escolhas do pesquisador

* Amostragem por conveniência: a seleção da amostra não segue qualquer critério científico

* Amostragem por julgamento: o pesquisador arbitra os critérios para seleção da amostra

* Amostragem por cotas: o tamanho da amostra é proporcional aos estratos, mas a seleção da amostra não segue método probabilístico
* Amostragem por tipicidade: são selecionados elementos representativos das subpopulações

* Amostragem por voluntários: indivíduos decidem participar da pesquisa

* Amostragem por bola de neve: indivíduos selecionados convidam novos participantes

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Conceitos Iniciais

Item. 1. (Cebraspe/2014 - ANATEL) Em junho de 2014, o Brasil registrou 275,71 milhões de linhas ativas na telefonia móvel e teledensidade de 136,06 acessos por 100 habitantes. Além disso, nesse mesmo mês,houve um acréscimo de 255,08 mil linhas na telefonia móvel: os acessos pré-pagos totalizaram 212,27milhões (76,99% do total) e os pós-pagos, 63,44 milhões (23,01% do total). A banda larga móvel totalizou128,49 milhões de acessos, dos quais 3,27 milhões eram terminais 4G.

Considerando as informações apresentadas no texto acima e supondo que um analista pretenda elaborar um plano amostrai por meio de uma amostra aleatória simples sem reposição das linhas ativas na telefonia móvel com o objetivo de estimar a proporção de ligações não completas em junho de 2014, julgue o item a seguir.
Nos erros não amostrais que o analista poderá identificar incluem-se os erros sistemáticos.

Comentários:

Erros sistemáticos são, de fato, erros não amostrais, quais sejam, aqueles decorrentes de falhas no processo de amostragem.
Gabarito: Certo

Item. 2. (Cebraspe/2019 -TJ-AM) Em uma fila para atendimento, encontram-se 1.000
pessoas. Em ordem cronológica, cada pessoa recebe uma senha para atendimento numerada de 1 a 1.000. Para a estimação do tempo médio de espera na fila, registram-se os tempos de espera das pessoas cujas senhas são números múltiplos de 10, ou seja, 10, 20, 30, 40,..., 1.000.
Considerando que o coeficiente de correlação dos tempos de espera entre uma pessoa e outra nessa fila seja igual a 0,1, e que o desvio padrão populacional dos tempos de espera seja igual a 10 minutos,julgue o item que se segue.
Para a estimação do tempo médio de espera, a fração amostrai adotada na referida situação será superior a0,12.

Comentários:

A fração amostrai é a razão entre o tamanho amostrai e o tamanho populacional:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Sendo extraído um elemento para a amostra a cada de 10 elementos da população, então a razão entre o tamanho da amostra e o tamanho da população é de = 0,1.
No caso, o tamanho da população é N = 1000 e o tamanho da amostra será n = =
Item. 100. Assim, a fração amostrai é dada por:
100 1

f = = — =01

7 1000 10

Que é inferior a 0,12.

Gabarito: Errado.

Item. 3. (Cebraspe/2019 -TJ-AM) Em determinado município brasileiro, realizou-se um levantamento para estimar o percentual P de pessoas que conhecem o programa justiça itinerante. Para esse propósito,foram selecionados 1.000 domicílios por amostragem aleatória simples de um conjunto de 10 mil domicílios.Nos domicílios selecionados, foram entrevistados todos os residentes maiores de idade, que totalizaram 3.000pessoas entrevistadas, entre as quais 2.250 afirmaram conhecer o programa justiça itinerante.

De acordo com essa situação hipotética, julgue o seguinte item.

A fração amostrai do levantamento em tela foi superior a 0,5.

Comentários:

A fração amostrai é a razão entre o tamanho amostrai e o tamanho populacional:

O enunciado informa que foram selecionados 1.000 domicílios (n = 1.000), dentre 10.000
domicílios (N =
10.000). Logo, a fração é:

Item. 1.000 1

f = = — =01

1 10.000 10

Que é inferior a 0,5.

Gabarito: Errado.

Item. 4. (Cebraspe 2018/STM) Um estudo acerca do tempo (x, em anos) de guarda de autos findos em determinada seção judiciária considerou uma amostragem aleatória estratificada. Apopulação consiste de uma listagem de autos findos, que foi segmentada em quatro estratos, segundo a classe de cada processo (as classes foram estabelecidas por resolução de autoridade judiciária). A tabela a seguir mostra
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

os tamanhos populacionais (N) e amostrais (n), a média amostrai (x) e a variância amostrai dos tempos (s2)correspondentes a cada estrato.

Estratos

Tamanhos Populacionais (N)

Tamanhos Amostrais (n)

X s2

A 30.000

20 3

B 40.000

15 16

C 50.000

10 5

D 80.000 800
5 8

Total

200.000

Item. 2.000 - -

Considerando que o objetivo do estudo seja estimar o tempo médio populacional (em anos) de guarda dos autos findos, julgue o item a seguir.
A fração amostrai utilizada no estudo em tela foi igual ou superior a 10%.

Comentários:

A fração amostrai é a razão entre amostra total e a população total:

nT 2.000 1

= = = =

Jr Nt 200.000 100

Que é inferior a 10%.

Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

QUESTõES CoMENTADAS - CEBRASPE

Amostragem Probabilística

Item. 1. (Cebraspe/2016 - PC/PE) Para realizar um estudo a respeito da qualidade dos serviços oferecidos nas salas de UTI de hospitais particulares, uma empresa de fiscalização pretende coletar uma amostra mediante entrevistas a clientes de determinado hospital. A fim de obter uma amostra com base nas entrevistas de 10% dos 1000 clientes do hospital, a equipe de fiscalização decidiu realizar um sorteio para definir quais clientes participarão da entrevista.
Considerando a técnica utilizada pelo fiscal, assinale a opção que apresenta corretamente o tipo de amostra definida nessa situação hipotética.
a) amostra não probabilística b) amostra de conveniência c) amostra aleatória simples d) amostra semiprobabilística e) amostra aleatória estratificada
Comentários:

O enunciado informa que será realizado um sorteio para selecionar a amostra de clientes. Assim, a técnica utilizada é a amostragem aleatória simples (AAS).
Gabarito: C.

Item. 2. (Cebraspe/2018 - PF) Tendo em vista que a abordagem da população sobre o conjunto de unidades amostrais pode ser aleatória, sistemática ou mista, e que, entre esses arranjos estruturais, situam-se os processos de amostragem mais usuais em inventários florestais — amostragem aleatória simples,amostragem estratificada, amostragem sistemática, amostragem em dois estágios e amostragem em conglomerados —, julgue o item, relativo a esses processos de amostragem.
O processo de amostragem aleatória simples requer que todas as combinações possíveis de n unidades amostrais da população tenham igual chance de participar da amostra; que a área florestal a ser inventariada seja tratada como uma população única; e que a seleção das amostras possa ser realizada com ou sem reposição.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

No processo de amostragem aleatória simples (AAS):

o todos os elementos da população tenham a mesma chance de serem selecionados;

o a população é considerada homogênea (ou única); e o as amostras podem ser extraídas com ou sem reposição.
Gabarito: Certo.

Item. 3. (Cebraspe/2019 -TJ-AM) Em uma fila para atendimento, encontram-se 1.000
pessoas. Em ordem cronológica, cada pessoa recebe uma senha para atendimento numerada de 1 a 1.000. Para a estimação do tempo médio de espera na fila, registram-se os tempos de espera das pessoas cujas senhas são números múltiplos de 10, ou seja, 10, 20, 30, 40,..., 1.000.
Considerando que o coeficiente de correlação dos tempos de espera entre uma pessoa e outra nessa fila seja igual a 0,1, e que o desvio padrão populacional dos tempos de espera seja igual a 10 minutos,julgue o item que se segue.
A situação em tela descreve uma amostragem sistemática.

Comentários:

O enunciado informa que a amostra extraída para obtenção do tempo de espera é selecionada de 10 em 10elementos. Logo, trata-se de uma amostragem sistemática, com R = 10.

Gabarito: Certo.

Item. 4. (Cebraspe/2016 - TCE-PA) Suponha que o tribunal de contas de determinado estado disponha de
30 dias para analisar as contas de 800 contratos firmados pela administração.
Considerando que essa análise é necessária para que a administração pública possa programar o orçamento do próximo ano e que o resultado da análise deve ser a aprovação ou rejeição das contas, julgue o item a seguir.Sempre que necessário, utilize que P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Zrepresenta a variável normal padronizada.
Se a lista de contratos estiver ordenada pela data de assinatura, o resultado de uma amostra sistemática será similar ao de uma amostra selecionada por amostragem aleatória simples.
Comentários:

Se a população estiver ordenada, a amostragem sistemática terá, em geral, um resultado similar ao de uma amostragem aleatória simples, em termos de representatividade da população.
Gabarito: Certo

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 5. (Cebraspe/2015 - DEPEN) O diretor de um sistema penitenciário, com o propósito de estimar o percentual de detentos que possuem filhos, entregou a um analista um cadastro com os nomes de 500detentos da instituição para que esse profissional realizasse entrevistas com os indivíduos selecionados.
A partir dessa situação hipotética e dos múltiplos aspectos a ela relacionados, julgue o item, referente a técnicas de amostragem.
Se a lista de presos estiver em ordem alfabética, o emprego das técnicas de amostragem aleatória simples e de amostragem sistemática, para selecionar a amostra, produzirá praticamente os mesmos resultados.
Comentários:

Se a população estiver ordenada, a amostragem sistemática terá, em geral, um resultado similar ao de uma amostragem aleatória simples, em termos de representatividade da população.
Gabarito: Certo

Item. 6. (Cebraspe/2016 - TCE-PA) Considerando uma população finita em que a média da variável de interesse seja desconhecida, julgue o item a seguir.
Um processo de amostragem sistemática pode ser compreendido como um processo de amostragem por conglomerados.
Comentários:

Em uma amostragem sistemática, selecionamos os elementos a cada R elementos, a partir de um primeiro elementos selecionado Ai. Essa técnica pode ser vista como a divisão dos elementos da população em Rgrupos, dos quais um é selecionado para que todos os seus elementos sejam analisados,
que corresponde a uma amostragem por conglomerados.
Gabarito: Certo

Item. 7. (Cebraspe/2020 - TJ/PA) Uma população de 1.200 elementos possui um sistema de referências ordenado de 1 a 1.200. Com o propósito de se obter uma amostra de 300 elementos dessa população,dividiram-na em 300 grupos de 4 unidades populacionais, tendo sido a unidade
2 selecionada aleatoriamente entre as 4 primeiras unidades. Em seguida, foram selecionadas as segundas unidades dos299 grupos restantes, completando-se, assim, a amostra de 300 unidades populacionais.

Nesse caso, foi utilizada a amostragem a) por conglomerados em um estágio.
b) estratificada.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

c) sistemática.

d) aleatória simples.

e) por intervalos.

Comentários:

O enunciado informa que a população possui N = 1200 elementos ordenados e que a amostra possui n = 300elementos. Para isso, os N = 1200 elementos foram divididos em n = 300 grupos de 4
unidades (R = 1200/300

= 4) e sorteado um número de 1 a 4. No caso, o número sorteado foi o número 2.
Assim, em cada um dos n

= 300 grupos de 4 unidades, foi selecionado o 29 elemento. Ou seja, os elementos selecionados foram:
2, 6,10,14,...,

Esse é o procedimento da amostragem sistemática.

Gabarito: C

Item. 8. (Cebraspe/2020 - TJ-PA) O dono de um restaurante pretende selecionar 50 de seus clientes fidelizados para a degustação de uma nova receita que deseja incluir no cardápio. Ele possui um cadastro em que cada cliente fidelizado está numerado sequencialmente de 1 a 1.980. Para realizar a seleção, ele decidiu utilizar a técnica de amostragem sistemática.
Nessa situação, caso o intervalo de seleção da amostra seja igual a 39 e a primeira unidade populacional selecionada seja a 12.9, então a terceira unidade populacional selecionada será a a) 1179
b) 369

c) 909

d) 519.

e) 39

Comentários:

Em uma amostragem sistemática, calculamos o intervalo entre os elementos selecionados,
dividindo o total de elementos da população (no caso, 1980) pelo tamanho da amostra (no caso, 50):
N 1980

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Por isso, o enunciado informou que o intervalo será de R = 39. Em seguida, sorteamos o primeiro elemento a ser selecionado, escolhendo aleatoriamente um número entre 1 e 39. Oenunciado informou que o primeiro elemento é o 12Q cliente.
Assim, o segundo elemento será: 12 + 39 = 51; e o terceiro elemento será:

51 + 39 = 90

Gabarito: C

Item. 9. (Cebraspe/2020 - TJ-PA) Uma pesquisa foi realizada em uma população dividida em dois estratos,A e B. Uma amostra da população foi selecionada utilizando-se a técnica de amostragem estratificada proporcional, em que cada estrato possui um sistema de referências ordenadas.A seguir, são apresentadas as formas como as unidades populacionais de A e de B foram selecionadas,respectivamente,

o A primeira unidade populacional selecionada do estrato A foi a terceira. Em seguida,
cada unidade populacional foi selecionada a partir da primeira, adicionando-se 5 unidades. Dessa forma, a segunda unidade selecionada foi a oitava, e assim por diante, até a obtenção de 10 unidades populacionais.
o A primeira unidade populacional selecionada do estrato B foi a quarta.
Após, cada unidade populacional foi selecionada a partir da primeira, adicionando-se 6 unidades. Dessa forma, a segunda unidade selecionada foi a décima, e assim por diante, até a obtenção de 7 unidades populacionais.
A partir dessas informações, é correto afirmar que a) a população possui, no mínimo, 88 elementos.
b) a técnica de amostragem aleatória simples foi utilizada para selecionar a amostra de cada estrato.
c) a amostra possui, no mínimo, 92 unidades populacionais.

d) o estrato B possui mais unidades populacionais que o estrato A.

e) o intervalo de amostragem no estrato A possui amplitude maior que o intervalo de amostragem no estratoB.

Comentários:

O enunciado informa que a população é dividida em 2 estratos, sendo conduzida uma amostragem sistemática em cada estrato. Por isso, a alternativa B está incorreta.
Em relação ao estrato A, o enunciado informa que:

o O primeiro elemento selecionado está na posição A₁ = 3 da população;

o O intervalo é RA = 5;

o A amostra tem tamanho nA = 10.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Com base nessas informações, a posição do último (102) elemento selecionado nesse estrato é:

An = + (n - 1) x RA

X₁₀ = 3 + 9 x 5 = 48

Ou seja, o último elemento selecionado está na posição 48. Assim, concluímos que a população do estrato Apossui no mínimo 48 elementos.

Em relação ao estrato B, o enunciado informa que:

o O primeiro elemento selecionado está na posição B{ = 4 da população;

o O intervalo é RB = 6;

o A amostra tem tamanho nB = 7.

Com base nessas informações, a posição do último (72) elemento selecionado nesse estrato é:

B₇ = 4 + 6x6 = 40

Ou seja, o último elemento selecionado está na posição 40. Assim, concluímos que a população do estrato Bpossui no mínimo 40 elementos.

No total, há no mínimo 48 + 40 = 88 elementos. Por isso, a alternativa A está correta.

Como o número mínimo da população do estrato A é maior que o número mínimo da população do estratoB, concluímos que a alternativa D está incorreta. Como o intervalo do estrato A é RA
= 5 e do estrato B é
Rb = 6, a alternativa E está incorreta. Em relação à alternativa C, a amostra total possui nA + nB = 10 +
7 = 17 unidades, logo, a alternativa está incorreta.

Gabarito: A

Item. 10. (Cebraspe/2017 - SE/DF) Um estudo estatístico será realizado para avaliar a condição socioambiental de estudantes do 5.2 ano do ensino fundamental das escolas da rede pública do DF. Apartir de uma lista que contempla todas as turmas do 5.2 ano do ensino fundamental das escolas da rede pública do DF, serão selecionadas aleatoriamente 50 turmas. Em seguida, os entrevistadores aplicarão questionários para todos os estudantes matriculados nessas 50 turmas. Com base nessas informações,julgue o seguinte item.

A técnica de amostragem a ser empregada nesse estudo deverá ser a da amostragem aleatória estratificada,em que cada turma constitui um estrato de estudantes do 5.2 ano do ensino fundamental da rede pública do DF.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado informa que serão selecionadas aleatoriamente 50 turmas, das quais todos os estudantes serão analisados (responderão a questionários). Essa técnica é a amostragem por conglomerados, e não a amostragem estratificada.
Gabarito: Errado.

Item. 11. (Cebraspe/2020 - TJ-PA) Para realizar uma pesquisa a respeito da qualidade do ensino de matemática nas escolas públicas de um estado, selecionaram aleatoriamente uma escola de cada um dos municípios desse estado e aplicaram uma mesma prova de matemática a todos os estudantes do nono ano do ensino fundamental de cada uma dessas escolas.
Nesse caso, foi utilizada a amostragem a) sistemática.
b) aleatória simples.

c) por conglomerados em um estágio.

d) por conglomerados em dois estágios.

e) estratificada.

Comentários:

Para realizar uma pesquisa sobre a qualidade do ensino de um estado, foram analisados todos os estudantes do último ano das escolas selecionadas. Ou seja, são selecionados alguns grupos(escolhas) em que todos os elementos (alunos do último ano) são analisados. Portanto, temos a amostragem por conglomerados em um estágio.
Gabarito: C

Item. 12. (Cebraspe/2016 - TCE-PA) Considerando uma população finita em que a média da variável de interesse seja desconhecida, julgue o item a seguir.
Para uma amostra aleatória estratificada, quanto mais homogêneos forem os valores populacionais dentro de cada estrato, menor será o tamanho de amostra necessário para se obter determinado nível de precisão das estimativas da média populacional.
Comentários:

A amostragem aleatória estratificada é mais eficiente quanto maior for a homogeneidade dos elementos dentro de cada estrato. Isso significa que para um mesmo tamanho amostrai, a precisão será maior.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Alternativamente, para um mesmo nível de precisão, o tamanho amostrai poderá ser menor, para uma homogeneidade maior.
Gabarito: Certo.

Item. 13. (Cebraspe 2014/ANATEL) Em junho de 2014, o Brasil registrou 275,71 milhões de linhas ativas na telefonia móvel e teledensidade de 136,06 acessos por 100 habitantes. Além disso, nesse mesmo mês,houve um acréscimo de 255,08 mil linhas na telefonia móvel: os acessos pré-pagos totalizaram 212,27milhões (76,99% do total) e os pós-pagos, 63,44 milhões (23,01% do total). A banda larga móvel totalizou128,49 milhões de acessos, dos quais 3,27 milhões eram terminais 4G.

Considerando as informações apresentadas no texto acima e supondo que um analista pretenda elaborar um plano amostrai por meio de uma amostra aleatória simples sem reposição das linhas ativas na telefonia móvel com o objetivo de estimar a proporção de ligações não completas em junho de 2014, julgue o item a seguir.
Caso tenham sido registradas mais ligações incompletas no estrato pré-pago que no estrato pós-pago, o analista obterá, com o uso da estratificação proporcional, mais amostras de linhas pré-pagas que de linhas pós-pagas o que resultará em um aumento no viés da estimativa da proporção de ligações não completas para a população.
Comentários:

Caso haja mais ligações no estrato pré-pago que no estrato pós-pago, então, com o uso da estratificação proporcional, a amostra do estrato pré-pago deve, sim, ser maior do que a amostra do estrato pós-pago.Porém, essa escolha não resulta em um aumento do viés da estimativa. Na verdade, essa técnica é inclusive mais eficiente do que a amostragem estratificada uniforme, em que é o tamanho da amostra é o mesmo para todos os estratos.
Gabarito: Errado.

Item. 14. (Cebraspe/2015 - DEPEN) Uma amostra de vinte presídios foi selecionada para que fosse verificada a quantidade média de indivíduos por cela. A amostra foi estratificada por localização: capital (C)e interior
(I). A quantidade média de indivíduos por cela nas capitais é igual a 10, ao passo que a quantidade média de indivíduos por cela nas cidades do interior é igual a 15.
Considerando essa situação hipotética, julgue o item a seguir.

Se existem 50 presídios na capital e 100 presídios no interior, a alocação proporcional, nos estratos da amostra, será superior a 6 presídios na capital e superior a 12 presídios no interior.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado informa que serão selecionados n = 20 presídios na amostra. Considerando que existem 50presídios na capital e 100 presídios no interior (150 no total), então, na amostragem estratificada com alocação proporcional, a proporção a ser seguida em cada estrato é:
nT 20 2

Ã/7= 15Õ=15

Logo, o tamanho da amostra dos presídios da capital é:

Assim, o tamanho da amostra dos presídios da capital é superior a 6. Já, o tamanho da amostra dos presídios do interior é dado por:
2 200

m = pxN! = — xlQ0 = —— = 13,3

Assim, o tamanho da amostra dos presídios do interior é superior a 12.

Gabarito: Certo.

Item. 15. (Cebraspe/2013 - ANTT)

Estrato

Número total de caminhões no estrato(tamanho do estrato)

Número de caminhões observados na amostra(tamanho da amostra)

Média amostrai das idades dos caminhões do estrato
Desvio padrão amostrai das idades dos caminhões do estrato
A 10 mil

10 anos

10 anos

B 20 mil

1.000

20 anos

10 anos

Total

30 mil

Item. 1.500 - -

A tabela acima apresenta um levantamento estatístico por amostragem aleatória estratificada o qual foi realizado para se estimar a idade média da frota de caminhões em determinada região do país. Apopulação de caminhões foi divida em dois estratos A e B, dos quais foram selecionados — sem reposição
— 500 e 1.000 caminhões, respectivamente, perfazendo o total de 1,5 mil caminhões na amostra. Com base nessas informações e na tabela apresentada, julgue o seguinte item.
A amostragem sem reposição permite garantir que as unidades amostrais foram mutuamente independentes.
Comentários:

Na amostragem sem reposição, as extrações não são independentes uma das outras.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Gabarito: Errado

Item. 16. (Cebraspe/2013 - ANTT)

Estrato

Número total de caminhões no estrato(tamanho do estrato)

Número de caminhões observados na amostra(tamanho da amostra)

Média amostrai das idades dos caminhões do estrato
Desvio padrão amostrai das idades dos caminhões do estrato
A 10 mil

10 anos

10 anos

B 20 mil

1.000

20 anos

10 anos

Total

30 mil

Item. 1.500 - -

A tabela acima apresenta um levantamento estatístico por amostragem aleatória estratificada o qual foi realizado para se estimar a idade média da frota de caminhões em determinada região do país. Apopulação de caminhões foi divida em dois estratos A e B, dos quais foram selecionados — sem reposição
— 500 e 1.000 caminhões, respectivamente, perfazendo o total de 1,5 mil caminhões na amostra. Com base nessas informações e na tabela apresentada, julgue o seguinte item.
Os caminhões que constituem a amostra de cada estrato foram selecionados por amostragem aleatória simples.

Comentários:

O enunciado informa que são extraídas amostras sem reposição de cada estrato, ou seja,
que é um tipo de amostragem aleatória simples (AAS).
Gabarito: Certo

Item. 17. (Cebraspe/2013 - ANTT)

Estrato

Número total de caminhões no estrato(tamanho do estrato)

Número de caminhões observados na amostra(tamanho da amostra)

Média amostrai das idades dos caminhões do estrato
Desvio padrão amostrai das idades dos caminhões do estrato
A 10 mil

10 anos

10 anos

B 20 mil

1.000

20 anos

10 anos

Total

30 mil

Item. 1.500 - -

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A tabela acima apresenta um levantamento estatístico por amostragem aleatória estratificada o qual foi realizado para se estimar a idade média da frota de caminhões em determinada região do país. Apopulação de caminhões foi divida em dois estratos A e B, dos quais foram selecionados — sem reposição
— 500 e 1.000 caminhões, respectivamente, perfazendo o total de 1,5 mil caminhões na amostra. Com base nessas informações e na tabela apresentada, julgue o seguinte item.
A alocação da amostra nesse levantamento foi do tipo uniforme. Nesse caso, a probabilidade de seleção de um caminhão da população foi igual a 0,05.
Comentários:

Pela tabela, podemos observar que a proporção do tamanho da amostra em relação ao tamanho do estrato é a mesma para ambos os estratos (igual a 0,05). Assim, concluímos que a alocação foi proporcional, e não uniforme (em que o tamanho da amostra é sempre o mesmo, independentemente do tamanho do estrato).
Gabarito: Errado.

Item. 18. (Cebraspe/2013 - ANTT) Acerca da distribuição dos consumidores de determinado produto segundo suas preferências por marcas, sabe-se que, em determinada cidade, 20% dos consumidores preferem a marca A, 50%, a marca B e os 30% restantes, preferem a marca C. A marca A é importada e as marcas B e C são nacionais. Considere que os desvios padrão das rendas mensais dos consumidores que preferem as marcas A, B e C sejam, respectivamente, iguais a R$ 500,00, R$ 400,00 e 13xR$ 2.000,00.Uma amostragem aleatória estratificada de n=500 pessoas será retirada dessa população para estimar a renda média mensal dos consumidores desse produto dessa cidade.
Considerando que os três grupos de consumidores são os estratos da amostragem, julgue o item que se segue.
No caso da alocação proporcional ao tamanho dos estratos, a amostra deve consistir em
100 consumidores que preferem a marca A, 250 que preferem a marca B e 150 que preferem a marca C.
Comentários:

O enunciado informa que será selecionada uma amostra de tamanho n = 500 pessoas.
Considerando que
20% preferem a marca A, 50% preferem a marca B e 30% preferem a marca C, então,
para uma alocação proporcional, o número de elementos da amostra de cada estrato deverá seguir essa mesma proporção dos tamanhos populacionais dos estratos:
* A:20% x 500 = 100

* B: 50% x 500 = 250

* C: 30% x 500 = 150

Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 19. (CESPE 2007/TCU) Em auditoria, as técnicas de amostragem objetivam coletar e avaliar evidências numéricas das entidades administrativas no intuito de determinar e relatar o grau de adequação das informações obtidas. O método de amostragem probabilístico envolve a amostra aleatória simples, a estratificada e a amostra por conglomerados. Quanto a esse método, julgue o item abaixo.
Suponha-se que, em uma pesquisa, se pretenda estimar a proporção de beneficiários do crédito educativo que conseguem completar o curso superior. Suponha-se, ainda, que a metodologia de coleta de dados desse estudo seja feita por meio de questionários compulsórios e que estes sejam remetidos pelo correio. Nesse caso, a estratificação por curso, gênero ou localidade é relevante para o resultado da pesquisa, cujo método probabilístico é exemplo típico de amostra aleatória simples.
Comentários:

Sendo a estratificação relevante para o resultado da pesquisa, então o método probabilístico deverá ser a amostragem estratificada e não a amostragem aleatória simples.
Gabarito: Errado.

Item. 20. (CESPE 2010/MPU) Julgue o item a seguir, a respeito de amostragem por conglomerados,considerando uma população U = {1,..., 6} com conglomerados Cl = {1}, C2 = {2, 3} e C3 = {4, 5, 6}
e o vetor de dados associado D = (15,10, 4, 5, 8, 6).
Se dois dos três conglomerados — Cl, C2, C3 — da população U forem escolhidos em seguida para formar a amostra, as possíveis amostras serão: {1, 2, 3}, {1, 4, 5, 6}, {2, 3, 1}, {2, 3, 4, 5, 6}, {4, 5,6,1}, {4, 5, 6,1, 2, 3}.

Comentários:

Sendo apenas 2 dos 3 conglomerados forem selecionados, então não será possível formar a amostra {4, 5,6, 1, 2, 3}, que contém todos os elementos da população.

Gabarito: Errado.

Item. 21. (Cebraspe 2013/MPU) Julgue o item a seguir, a respeito de amostragem por conglomerados,considerando uma população U = {1,..., 6} com conglomerados Cl = {1}, C2 = {2, 3} e C3 = {4, 5, 6}
e o vetor de dados associado D = (15,10, 4, 5, 8, 6).
Se dois dos três conglomerados — Cl, C2, C3 — da população U forem escolhidos para formar a amostra, a média amostrai assume os seguintes possíveis valores: 29/3, 17/2 e 33/5, de modo que cada um desses valores ocorre com a mesma probabilidade, isto é, 1/3.
Comentários:

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

O enunciado informa que os valores associados aos elementos da população {1,
2, 3, 4, 5, 6} são,

respectivamente, (15, 10, 4, 5, 8, 6).

Caso sejam selecionados os conglomerados Cl = {1} e C2 = {2, 3}, associados aos valores (15,10, 4), a média amostrai será:
15 + 10 + 4 29

%1.2 - 3 - y

Caso sejam selecionados os conglomerados Cl = {1} e C3 = {4, 5, 6}, associados aos valores (15, 5, 8, 6), a média amostrai será:
15 + 5 + 8 + 6 34 17

%i,3 - —4 — - y - y

Caso sejam selecionados os conglomerados C2 = {2, 3} e C3 = {4, 5, 6}, associados aos valores (10,
4, 5, 8, 6),
a média amostrai será:

10 + 4 + 5 + 8 + 6 33

' 5 5

Assim, os possíveis valores são, de fato, 29/3,17/2 e 33/5, cada um com probabilidade de 1/3.

Gabarito: Certo.

Item. 22. (Cebraspe 2013/MPU) Julgue o item a seguir, a respeito de amostragem por conglomerados,considerando uma população U = {1,..., 6} com conglomerados Cl = {1}, C2 = {2, 3} e C3 = {4, 5, 6}
e o vetor de dados associado D = (15,10, 4, 5, 8, 6).
Na amostragem por conglomerados, a população é subdividida em grupos com tamanhos não necessariamente iguais. A amostra obtida consiste da união dos conglomerados escolhidos e geralmente 0tamanho dessa amostra é uma variável aleatória.

Comentários:

Na amostragem por conglomerados, a população é subdivida em grupos de elementos heterogêneos(chamados conglomerados), que não precisam ser de mesmo tamanho. Nesse tipo de amostragem, são analisados todos os elementos dos conglomerados selecionados, motivo pelo qual a amostra pode ser considerada uma união dos conglomerados escolhidos. O tamanho da amostra,então, dependerá dos conglomerados selecionados aleatoriamente e, por esse motivo, 0 tamanho da amostra pode ser considerado uma variável aleatória.
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 23. (CESPE 2011/TRE-ES) Julgue o item que se segue, referente às técnicas de amostragem e de inferência estatística.
Uma pesquisa de âmbito nacional para obter a intenção dos brasileiros na eleição para presidente daRepública pode ser feita com base em uma amostragem que considera pelo menos três estágios: por região,por estado e por município.

Comentários:

O item descreve uma amostragem por conglomerado, em que a população é dividida em grupos de elementos heterogêneos, sendo selecionados alguns grupos, dos quais todos os elementos são selecionados.Esse procedimento descreve a amostragem por conglomerado em um único estágio.
Caso seja inviável analisar todos os elementos do conglomerado, a amostragem pode ser feita em múltiplas etapas. Em uma segunda etapa, por exemplo, os conglomerados selecionados na primeira etapa são divididos em novos conglomerados, sendo selecionados alguns "sub-conglomerados". Esse procedimento é repetido até que todos os elementos dos grupos selecionados possam ser analisados.
Assim, o item descreve uma amostragem por conglomerados em 3 estágios.
Primeiro são selecionadas algumas regiões do Brasil; na segunda etapa, são selecionados alguns estados de cada uma das regiões selecionadas na etapa anterior; e, por fim, são selecionados alguns municípios de cada um dos estados selecionados na etapa anterior.
Gabarito: Certo.

Item. 24. (Cebraspe/2019 - TJ-AM) Para avaliar a satisfação dos servidores públicos de certo tribunal no ambiente de trabalho, realizou-se uma pesquisa. Os servidores foram classificados em três grupos, de acordo com o nível do cargo ocupado. Na tabela seguinte, k é um índice que se refere ao grupo de servidores, e NR denota o tamanho populacional de servidores pertencentes ao grupo k.
nível do cargo k Nk nk Pk

1 1 500 50 0,7

II 2 300 20 0,8

III 3 200 10 0,9

De cada grupo k foi retirada uma amostra aleatória simples sem reposição de tamanho nk; pk representa a proporção de servidores amostrados do grupo k que se mostraram satisfeitos no ambiente de trabalho.A partir das informações e da tabela apresentadas, julgue o próximo item.

O desenho amostrai empregado nessa pesquisa foi a amostragem aleatória estratificada com alocação proporcional aos tamanhos dos estratos.
Comentários:

Na amostragem aleatória estratificada com alocação proporcional, a proporção entre o tamanho da amostra e o tamanho da população é a mesma para todos os estratos.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Pela tabela, podemos observar que para o primeiro estrato, essa proporção é de:

Til 50 1

fl ~ N,~ 5ÕÕ " Tõ

Para o segundo estrato, a proporção é de:

nu 20 i fu ~ N,r ' 3ÕÕ~ 15
Como a proporção é diferente, então a amostragem não teve alocação proporcional.

Gabarito: Errado

Item. 25. (Cebraspe/2013 - SEFAZ-ES)

Estrato Tamanho do Estrato Tamanho da Amostra Desvio Padrão da

Variável de Interesse

1 50.000 100

2 100.000 200

A tabela acima descreve um processo de amostragem do tipo aleatória estratificada. Com base nessas informações, assinale a opção correta.
a) A fração amostrai no estrato 2 é superior à fração amostrai no estrato 1.

b) Com respeito ao tamanho da amostra retirada de cada estrato, o plano amostrai apresentado considera a alocação ótima de Neyman.
c) Na amostragem em tela, retira-se uma amostra aleatória simples de cada estrato.

d) O objetivo da estratificação é formar subgrupos heterogêneos, de modo a maximizar o desvio padrão da variável de interesse em cada estrato.
e) No plano amostrai apresentado, para o cálculo da estimativa da média populacional,
é necessário utilizar um fator de expansão para corrigir os vícios na estimação provocados pela estratificação.
Comentários:

Pela tabela, podemos observar que foi utilizada a amostragem estratificada com alocação proporcional, pois o tamanho da amostra corresponde a 0,2% do tamanho da população para ambos os estratos.
Em relação à alternativa A, a fração amostrai é a mesma para ambos os extratos (/ =
^ = 0,2%), logo a alternativa A está incorreta.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Em relação à alternativa B, pela tabela apresentada, concluímos que o plano amostrai considerou a alocação proporcional, e não com a alocação ótima de Neyman. Por isso, a alternativa B está errada.
Em relação à alternativa C, para selecionar a amostra de cada estrato, pode-se aplicar uma amostragem aleatória simples, logo a alternativa C está correta.
Em relação à alternativa D, na amostragem estratificada, a população é dividida em grupos compostos de elementos homogêneos (similares), de modo que o desvio padrão (isto é, a variabilidade)seja o menor possível, ao contrário do que afirma a alternativa.
Em relação à alternativa E, a amostragem estratificada é uma técnica probabilística de amostragem, não provocando, por si só, vícios na estimação.
Gabarito: C

Item. 26. (Cebraspe 2018/STM) Um estudo acerca do tempo (x, em anos) de guarda de autos findos em determinada seção judiciária considerou uma amostragem aleatória estratificada. Apopulação consiste de uma listagem de autos findos, que foi segmentada em quatro estratos, segundo a classe de cada processo (as classes foram estabelecidas por resolução de autoridade judiciária). A tabela a seguir mostra os tamanhos populacionais (N) e amostrais (n), a média amostrai (x) e a variância amostrai dos tempos (s2)correspondentes a cada estrato.

Estratos

Tamanhos Populacionais (N)

Tamanhos Amostrais (n)

X s2

A 30.000

20 3

B 40.000

15 16

C 50.000

10 5

D 80.000 800
5 8

Total

200.000

Item. 2.000 - -

Considerando que o objetivo do estudo seja estimar o tempo médio populacional (em anos) de guarda dos autos findos, julgue o item a seguir.
No desenho amostrai em tela há duas unidades amostrais: a primeira (unidade primária) corresponde à classe de cada processo, e a segunda (unidade secundária) refere-se a auto findo presente na listagem.
Comentários:

Unidades amostrais correspondem aos elementos a serem selecionados. Nesse caso, as unidades amostrais são os autos findos, logo, há 200.000 unidades amostrais no (e não 2).
Gabarito: Errado.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 27. (Cebraspe 2018/STM) Um estudo acerca do tempo (x, em anos) de guarda de autos findos em determinada seção judiciária considerou uma amostragem aleatória estratificada. Apopulação consiste de uma listagem de autos findos, que foi segmentada em quatro estratos, segundo a classe de cada processo (as classes foram estabelecidas por resolução de autoridade judiciária). A tabela a seguir mostra os tamanhos populacionais (N) e amostrais (n), a média amostrai (x) e a variância amostrai dos tempos (s2)correspondentes a cada estrato.

Estratos

Tamanhos Populacionais (N)

Tamanhos Amostrais (n)

X s²

A 30.000

20 3

B 40.000

15 16

C 50.000

10 5

D 80.000 800
5 8

Total

200.000

Item. 2.000 - -

Considerando que o objetivo do estudo seja estimar o tempo médio populacional (em anos) de guarda dos autos findos, julgue o item a seguir.
No estudo em questão foi aplicada uma amostragem aleatória estratificada com alocação proporcional ao tamanho dos estratos.
Comentários:

Na amostragem estratificada proporcional, a proporção entre a amostra e o tamanho populacional é mantida para todos os estratos.
A proporção entre a amostra total e a população total é:

nT 2.000

Ã/7 " 200.000

Essa proporção é mantida para todos os estratos:

nz 300 1

Item. 30.000 _ 100 _ 1/0

n/z 400 1

' 40.000 _ 100 _ 1/0

r nHI

^III

500 1

~ 50.000 " 100 _ 1/0

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

r 1VnIV 800 _ 1

-10/

J,v ~ NjV ~ 80.000 _ 100 _ °
Assim, concluímos que a amostragem estratificada segue a alocação proporcional.
Gabarito: Certo.

Item. 28. (Cebraspe 2018/ABIN) Um levantamento amostrai foi realizado para se estimar o valor médio mensal (em R$ mil) per capita gasto em segurança da informação. Como a população de interesse se organiza naturalmente em 50 grupos de pessoas (facilmente identificáveis), decidiu-se selecionar ao acaso5 desses grupos. Todas as pessoas de cada grupo (i = 1, 2, ... , 5) foram entrevistadas, e os resultados encontrados são mostrados no quadro a seguir, que mostra também a quantidade (ni) de pessoas em cada grupo e o valor mensal gasto em segurança da informação por cada grupo (yi, em R$ mil).
i ni Yi

1 10 5

2 20 2

3 30 1

4 20 4

5 20 8

total 100 20

A partir dessas informações, julgue o item que se segue, a respeito do estimador de razão y =
yi

=1

Os grupos de pessoas representam subpopulações que constituem uma partição da população. Assim, o levantamento amostrai em questão exemplifica uma amostragem aleatória estratificada, em que os grupos formam os estratos e cada pessoa presente em um estrato é uma unidade amostrai.
Comentários:

O enunciado informa que a população é dividida em 50 grupos, tendo sido selecionados
5 grupos, dos quais todos os membros são analisados. Essa técnica é a amostragem por conglomerados, e não a amostragem estratificada.
Gabarito: Errado.

Item. 29. (Cebraspe 2018/PF) Uma pesquisa realizada com passageiros estrangeiros que se encontravam em determinado aeroporto durante um grande evento esportivo no país teve como finalidade investigar a sensação de segurança nos voos internacionais. Foram entrevistados 1.000 passageiros,alocando-se a amostra de acordo com o continente de origem de cada um — África, América do Norte (AN), América doSul (AS), Ásia/Oceania (A/O) ou Europa. Na tabela seguinte, N é o tamanho populacional de passageiros em voos internacionais no período de interesse da pesquisa; n é o tamanho da amostra por origem; Pé o

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

percentual dos passageiros entrevistados que se manifestaram satisfeitos no que se refere à sensação de segurança.
origem
África

N
100.000

n P

100 80

AN 300.000 300 70

AS 100.000 100 90

A/O

300.000

300 80

Europa

200.000

200 80

Total

1.000.000

1.000

Ppop

Em cada grupo de origem, os passageiros entrevistados foram selecionados por amostragem aleatória simples. A última linha da tabela mostra o total populacional no período da pesquisa,o tamanho total da amostra e Ppop representa o percentual populacional de passageiros satisfeitos.
A partir dessas informações, julgue o item.

Na situação apresentada, o desenho amostrai é conhecido como amostragem aleatória por conglomerados,visto que a população de passageiros foi dividida por grupos de origem.

Comentários:

Podemos observar que a proporção entre o tamanho da amostra e o tamanho populacional é a mesma(0,1%) para todos os estratos. Com isso, concluímos que a amostragem é estratificada com alocação proporcional, e não amostragem por conglomerados, como descrito no item.
Gabarito: Errado.

Item. 30. (Cebraspe 2018/PF) Uma pesquisa realizada com passageiros estrangeiros que se encontravam em determinado aeroporto durante um grande evento esportivo no país teve como finalidade investigar a sensação de segurança nos voos internacionais. Foram entrevistados 1.000 passageiros,alocando-se a amostra de acordo com o continente de origem de cada um — África, América do Norte (AN), América doSul (AS), Ásia/Oceania (A/O) ou Europa. Na tabela seguinte, N é o tamanho populacional de passageiros em voos internacionais no período de interesse da pesquisa; n é o tamanho da amostra por origem; Pé o percentual dos passageiros entrevistados que se manifestaram satisfeitos no que se refere à sensação de segurança.
origem N n p

África

100.000

100 80

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

AN 300.000 300 70

AS 100.000 100 90

A/O

300.000

300 80

Europa

200.000

200 80

Total

1.000.000

1.000

Ppop

Em cada grupo de origem, os passageiros entrevistados foram selecionados por amostragem aleatória simples. A última linha da tabela mostra o total populacional no período da pesquisa,o tamanho total da amostra e Ppop representa o percentual populacional de passageiros satisfeitos.
A partir dessas informações, julgue o item.

Nessa pesquisa, cada grupo de origem representa uma unidade amostrai, da qual foi retirada uma amostra aleatória simples.
Comentários:

Uma unidade amostrai corresponde a cada elemento a ser selecionado. No caso,
a unidade amostrai corresponde a cada passageiro a ser analisado, e não a cada grupo, como ocorre na amostragem por conglomerados.
Gabarito: Errado.

Item. 31. (Cebraspe/2013 - CPRM)

Esquema de Amostragem para a área A

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Esquema de Amostragem para a área B

Considere que um estudo estatístico tenha sido realizado para determinar a concentração média de uma substância em duas diferentes áreas (A e B). Considere, ainda, que as figuras acima apresentam os esquemas amostrais para essas áreas, que foram divididas em uma malha regular de três por cinco quadrados, e que os pontos mostrados nas figuras representam os locais em que os dados foram coletados. Com base nessas informações, julgue o próximo item.
Considere que, no esquema da amostragem para a área B, a posição dos pontos dentro de cada quadrado da malha tenha sido escolhida aleatoriamente. Nessa situação, é correto afirmar que o plano amostrai para essa área ocorreu por conglomerados.
Comentários:

Na área B, podemos observar que foi selecionado um ponto aleatório para cada quadrado da malha. Isso corresponde à amostragem estratificada, em que é selecionada uma amostra de cada um dos grupos. Na amostragem por conglomerados, são selecionados alguns grupos, dos quais todos os elementos são analisados, o que não ocorre na área B.
Gabarito: Errado.

Item. 32. (Cebraspe/2013 - CPRM)

Esquema de Amostragem para a área A

Esquema de Amostragem para a área B

Considere que um estudo estatístico tenha sido realizado para determinar a concentração média de uma substância em duas diferentes áreas (A e B). Considere, ainda, que as figuras acima apresentam os esquemas amostrais para essas áreas, que foram divididas em uma malha regular de três por cinco
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

quadrados, e que os pontos mostrados nas figuras representam os locais em que os dados foram coletados. Com base nessas informações, julgue o próximo item.
O esquema amostrai para a área A caracteriza-se pela aplicação de uma malha regular com distribuição sistemática dos pontos de amostragem.
Comentários:

Na área A, é selecionado um ponto no mesmo local em cada um dos quadrados, como se tivéssemos selecionado o primeiro ponto e os demais pontos foram selecionados com a mesma periodicidade, o que corresponde à amostragem sistemática.
Gabarito: Certo.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Amostragem Não Probabilística

Item. 1. (CESPE/2011 - TER-ES) Julgue o item que se segue, referente às técnicas de amostragem e de inferência estatística.
No plano de amostragem por cotas, uma técnica probabilística, divide-se a população em classes de interesse e se seleciona uma quantidade de indivíduos de cada classe (quotas) para compor a amostra.
Comentários:

A amostragem por cotas não é uma técnica probabilística e, por esse motivo, o item está errado.

Gabarito: Errado.

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)
ívivw. estrategiaconcursos. com. br

Conceitos Iniciais

Item. 1. (Cebraspe/2014 - ANATEL) Em junho de 2014, o Brasil registrou 275,71 milhões de linhas ativas na telefonia móvel e teledensidade de 136,06 acessos por 100 habitantes. Além disso, nesse mesmo mês,houve um acréscimo de 255,08 mil linhas na telefonia móvel: os acessos pré-pagos totalizaram 212,27milhões (76,99% do total) e os pós-pagos, 63,44 milhões (23,01% do total). A banda larga móvel totalizou128,49 milhões de acessos, dos quais 3,27 milhões eram terminais 4G.

Considerando as informações apresentadas no texto acima e supondo que um analista pretenda elaborar um plano amostrai por meio de uma amostra aleatória simples sem reposição das linhas ativas na telefonia móvel com o objetivo de estimar a proporção de ligações não completas em junho de 2014, julgue o item a seguir.
Nos erros não amostrais que o analista poderá identificar incluem-se os erros sistemáticos.

Item. 2. (Cebraspe/2019 -TJ-AM) Em uma fila para atendimento, encontram-se 1.000
pessoas. Em ordem cronológica, cada pessoa recebe uma senha para atendimento numerada de 1 a 1.000. Para a estimação do tempo médio de espera na fila, registram-se os tempos de espera das pessoas cujas senhas são números múltiplos de 10, ou seja, 10, 20, 30, 40,..., 1.000.
Considerando que o coeficiente de correlação dos tempos de espera entre uma pessoa e outra nessa fila seja igual a 0,1, e que o desvio padrão populacional dos tempos de espera seja igual a 10 minutos,julgue o item que se segue.
Para a estimação do tempo médio de espera, a fração amostrai adotada na referida situação será superior a0,12.

Item. 3. (Cebraspe/2019 - TJ-AM) Em determinado município brasileiro, realizou-se um levantamento para estimar o percentual P de pessoas que conhecem o programa justiça itinerante. Para esse propósito,foram selecionados 1.000 domicílios por amostragem aleatória simples de um conjunto de 10 mil domicílios.Nos domicílios selecionados, foram entrevistados todos os residentes maiores de idade, que totalizaram 3.000pessoas entrevistadas, entre as quais 2.250 afirmaram conhecer o programa justiça itinerante.

De acordo com essa situação hipotética, julgue o seguinte item.

A fração amostrai do levantamento em tela foi superior a 0,5.

0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 4. (Cebraspe 2018/STM) Um estudo acerca do tempo (x, em anos) de guarda de autos findos em determinada seção judiciária considerou uma amostragem aleatória estratificada. Apopulação consiste de uma listagem de autos findos, que foi segmentada em quatro estratos, segundo a classe de cada processo (as classes foram estabelecidas por resolução de autoridade judiciária). A tabela a seguir mostra os tamanhos populacionais (N) e amostrais (n), a média amostrai (x) e a variância amostrai dos tempos (s2)correspondentes a cada estrato.

Estratos

Tamanhos Populacionais (N)

Tamanhos Amostrais (n)

X s²

A 30.000

20 3

B 40.000

15 16

C 50.000

10 5

D 80.000 800
5 8

Total

200.000

Item. 2.000 - -

Considerando que o objetivo do estudo seja estimar o tempo médio populacional (em anos) de guarda dos autos findos, julgue o item a seguir.
A fração amostrai utilizada no estudo em tela foi igual ou superior a 10%.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. CERTO

Item. 2. ERRADO

Item. 3. ERRADO

Item. 4. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Amostragem Probabilística

Item. 1. (Cebraspe/2016 - PC/PE) Para realizar um estudo a respeito da qualidade dos serviços oferecidos nas salas de UTI de hospitais particulares, uma empresa de fiscalização pretende coletar uma amostra mediante entrevistas a clientes de determinado hospital. A fim de obter uma amostra com base nas entrevistas de 10% dos 1000 clientes do hospital, a equipe de fiscalização decidiu realizar um sorteio para definir quais clientes participarão da entrevista.
Considerando a técnica utilizada pelo fiscal, assinale a opção que apresenta corretamente o tipo de amostra definida nessa situação hipotética.
a) amostra não probabilística b) amostra de conveniência c) amostra aleatória simples d) amostra semiprobabilística e) amostra aleatória estratificada
Item. 2. (Cebraspe/2018 - PF) Tendo em vista que a abordagem da população sobre o conjunto de unidades amostrais pode ser aleatória, sistemática ou mista, e que, entre esses arranjos estruturais, situam-se os processos de amostragem mais usuais em inventários florestais — amostragem aleatória simples,amostragem estratificada, amostragem sistemática, amostragem em dois estágios e amostragem em conglomerados —, julgue o item, relativo a esses processos de amostragem.
O processo de amostragem aleatória simples requer que todas as combinações possíveis de n unidades amostrais da população tenham igual chance de participar da amostra; que a área florestal a ser inventariada seja tratada como uma população única; e que a seleção das amostras possa ser realizada com ou sem reposição.
Item. 3. (Cebraspe/2019 -TJ-AM) Em uma fila para atendimento, encontram-se 1.000
pessoas. Em ordem cronológica, cada pessoa recebe uma senha para atendimento numerada de 1 a 1.000. Para a estimação do tempo médio de espera na fila, registram-se os tempos de espera das pessoas cujas senhas são números múltiplos de 10, ou seja, 10, 20, 30, 40,..., 1.000.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considerando que o coeficiente de correlação dos tempos de espera entre uma pessoa e outra nessa fila seja igual a 0,1, e que o desvio padrão populacional dos tempos de espera seja igual a 10 minutos,julgue o item que se segue.
A situação em tela descreve uma amostragem sistemática.

Item. 4. (Cebraspe/2016 - TCE-PA) Suponha que o tribunal de contas de determinado estado disponha de
30 dias para analisar as contas de 800 contratos firmados pela administração.
Considerando que essa análise é necessária para que a administração pública possa programar o orçamento do próximo ano e que o resultado da análise deve ser a aprovação ou rejeição das contas, julgue o item a seguir.Sempre que necessário, utilize que P(Z > 1,96) = 0,025 e P(Z > 1,645) = 0,05, em que Zrepresenta a variável normal padronizada.
Se a lista de contratos estiver ordenada pela data de assinatura, o resultado de uma amostra sistemática será similar ao de uma amostra selecionada por amostragem aleatória simples.
Item. 5. (Cebraspe/2015 - DEPEN) O diretor de um sistema penitenciário, com o propósito de estimar o percentual de detentos que possuem filhos, entregou a um analista um cadastro com os nomes de 500detentos da instituição para que esse profissional realizasse entrevistas com os indivíduos selecionados.
A partir dessa situação hipotética e dos múltiplos aspectos a ela relacionados, julgue o item, referente a técnicas de amostragem.
Se a lista de presos estiver em ordem alfabética, o emprego das técnicas de amostragem aleatória simples e de amostragem sistemática, para selecionar a amostra, produzirá praticamente os mesmos resultados.
Item. 6. (Cebraspe/2016 - TCE-PA) Considerando uma população finita em que a média da variável de interesse seja desconhecida, julgue o item a seguir.
Um processo de amostragem sistemática pode ser compreendido como um processo de amostragem por conglomerados.
Item. 7. (Cebraspe/2020 - TJ/PA) Uma população de 1.200 elementos possui um sistema de referências ordenado de 1 a 1.200. Com o propósito de se obter uma amostra de 300 elementos dessa população,dividiram-na em 300 grupos de 4 unidades populacionais, tendo sido a unidade
2 selecionada aleatoriamente entre as 4 primeiras unidades. Em seguida, foram selecionadas as segundas unidades dos299 grupos restantes, completando-se, assim, a amostra de 300 unidades populacionais.

Nesse caso, foi utilizada a amostragem

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

a) por conglomerados em um estágio.

b) estratificada.

c) sistemática.

d) aleatória simples.

e) por intervalos.

Item. 8. (Cebraspe/2020 - TJ-PA) O dono de um restaurante pretende selecionar 50 de seus clientes fidelizados para a degustação de uma nova receita que deseja incluir no cardápio. Ele possui um cadastro em que cada cliente fidelizado está numerado sequencialmente de 1 a 1.980. Para realizar a seleção, ele decidiu utilizar a técnica de amostragem sistemática.
Nessa situação, caso o intervalo de seleção da amostra seja igual a 39 e a primeira unidade populacional selecionada seja a 12.2, então a terceira unidade populacional selecionada será a a) 1172
b) 362

c) 902

d) 512.

e) 32

Item. 9. (Cebraspe/2020 - TJ-PA) Uma pesquisa foi realizada em uma população dividida em dois estratos,A e B. Uma amostra da população foi selecionada utilizando-se a técnica de amostragem estratificada proporcional, em que cada estrato possui um sistema de referências ordenadas.A seguir, são apresentadas as formas como as unidades populacionais de A e de B foram selecionadas,respectivamente,

o A primeira unidade populacional selecionada do estrato A foi a terceira. Em seguida,
cada unidade populacional foi selecionada a partir da primeira, adicionando-se 5 unidades. Dessa forma, a segunda unidade selecionada foi a oitava, e assim por diante, até a obtenção de 10 unidades populacionais.
o A primeira unidade populacional selecionada do estrato B foi a quarta.
Após, cada unidade populacional foi selecionada a partir da primeira, adicionando-se 6 unidades. Dessa forma, a segunda unidade selecionada foi a décima, e assim por diante, até a obtenção de 7 unidades populacionais.
A partir dessas informações, é correto afirmar que a) a população possui, no mínimo, 88 elementos.
0 0 SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

b) a técnica de amostragem aleatória simples foi utilizada para selecionar a amostra de cada estrato.
c) a amostra possui, no mínimo, 92 unidades populacionais.

d) o estrato B possui mais unidades populacionais que o estrato A.

e) o intervalo de amostragem no estrato A possui amplitude maior que o intervalo de amostragem no estratoB.

Item. 10. (Cebraspe/2017 - SE/DF) Um estudo estatístico será realizado para avaliar a condição socioambiental de estudantes do 5.2 ano do ensino fundamental das escolas da rede pública do DF. Apartir de uma lista que contempla todas as turmas do 5.2 ano do ensino fundamental das escolas da rede pública do DF, serão selecionadas aleatoriamente 50 turmas. Em seguida, os entrevistadores aplicarão questionários para todos os estudantes matriculados nessas 50 turmas. Com base nessas informações,julgue o seguinte item.

A técnica de amostragem a ser empregada nesse estudo deverá ser a da amostragem aleatória estratificada,em que cada turma constitui um estrato de estudantes do 5.2 ano do ensino fundamental da rede pública do DF.
Item. 11. (Cebraspe/2020 - TJ-PA) Para realizar uma pesquisa a respeito da qualidade do ensino de matemática nas escolas públicas de um estado, selecionaram aleatoriamente uma escola de cada um dos municípios desse estado e aplicaram uma mesma prova de matemática a todos os estudantes do nono ano do ensino fundamental de cada uma dessas escolas.
Nesse caso, foi utilizada a amostragem a) sistemática.
b) aleatória simples.

c) por conglomerados em um estágio.

d) por conglomerados em dois estágios.

e) estratificada.

Item. 12. (Cebraspe/2016 - TCE-PA) Considerando uma população finita em que a média da variável de interesse seja desconhecida, julgue o item a seguir.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Para uma amostra aleatória estratificada, quanto mais homogêneos forem os valores populacionais dentro de cada estrato, menor será o tamanho de amostra necessário para se obter determinado nível de precisão das estimativas da média populacional.
Item. 13. (Cebraspe 2014/ANATEL) Em junho de 2014, o Brasil registrou 275,71 milhões de linhas ativas na telefonia móvel e teledensidade de 136,06 acessos por 100 habitantes. Além disso, nesse mesmo mês,houve um acréscimo de 255,08 mil linhas na telefonia móvel: os acessos pré-pagos totalizaram 212,27milhões (76,99% do total) e os pós-pagos, 63,44 milhões (23,01% do total). A banda larga móvel totalizou128,49 milhões de acessos, dos quais 3,27 milhões eram terminais 4G.

Considerando as informações apresentadas no texto acima e supondo que um analista pretenda elaborar um plano amostrai por meio de uma amostra aleatória simples sem reposição das linhas ativas na telefonia móvel com o objetivo de estimar a proporção de ligações não completas em junho de 2014, julgue o item a seguir.
Caso tenham sido registradas mais ligações incompletas no estrato pré-pago que no estrato pós-pago, o analista obterá, com o uso da estratificação proporcional, mais amostras de linhas pré-pagas que de linhas pós-pagas o que resultará em um aumento no viés da estimativa da proporção de ligações não completas para a população.
Item. 14. (Cebraspe/2015 - DEPEN) Uma amostra de vinte presídios foi selecionada para que fosse verificada a quantidade média de indivíduos por cela. A amostra foi estratificada por localização: capital (C)e interior
(I). A quantidade média de indivíduos por cela nas capitais é igual a 10, ao passo que a quantidade média de indivíduos por cela nas cidades do interior é igual a 15.
Considerando essa situação hipotética, julgue o item a seguir.

Se existem 50 presídios na capital e 100 presídios no interior, a alocação proporcional, nos estratos da amostra, será superior a 6 presídios na capital e superior a 12 presídios no interior.
Item. 15. (CESPE/2013 - ANTT)

Estrato

Número total de caminhões no estrato(tamanho do estrato)

Número de caminhões observados na amostra(tamanho da amostra)

Média amostrai das idades dos caminhões do estrato
Desvio padrão amostrai das idades dos caminhões do estrato
A 10 mil

10 anos

10 anos

B 20 mil

1.000

20 anos

10 anos

Total

30 mil

Item. 1.500 - -

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A tabela acima apresenta um levantamento estatístico por amostragem aleatória estratificada o qual foi realizado para se estimar a idade média da frota de caminhões em determinada região do país. Apopulação de caminhões foi divida em dois estratos A e B, dos quais foram selecionados — sem reposição
— 500 e 1.000 caminhões, respectivamente, perfazendo o total de 1,5 mil caminhões na amostra. Com base nessas informações e na tabela apresentada, julgue o seguinte item.
A amostragem sem reposição permite garantir que as unidades amostrais foram mutuamente independentes.
Item. 16. (Cebraspe/2013 - ANTT)

Estrato

Número total de caminhões no estrato(tamanho do estrato)

Número de caminhões observados na amostra(tamanho da amostra)

Média amostrai das idades dos caminhões do estrato
Desvio padrão amostrai das idades dos caminhões do estrato
A 10 mil

10 anos

10 anos

B 20 mil

1.000

20 anos

10 anos

Total

30 mil

Item. 1.500 - -

A tabela acima apresenta um levantamento estatístico por amostragem aleatória estratificada o qual foi realizado para se estimar a idade média da frota de caminhões em determinada região do país. Apopulação de caminhões foi divida em dois estratos A e B, dos quais foram selecionados — sem reposição
— 500 e 1.000 caminhões, respectivamente, perfazendo o total de 1,5 mil caminhões na amostra. Com base nessas informações e na tabela apresentada, julgue o seguinte item.
Os caminhões que constituem a amostra de cada estrato foram selecionados por amostragem aleatória simples.
Item. 17. (Cebraspe/2013 - ANTT)

Estrato

Número total de caminhões no estrato(tamanho do estrato)

Número de caminhões observados na amostra(tamanho da amostra)

Média amostrai das idades dos caminhões do estrato
Desvio padrão amostrai das idades dos caminhões do estrato
A 10 mil

10 anos

10 anos

B 20 mil

1.000

20 anos

10 anos

Total

30 mil

Item. 1.500 - -

A tabela acima apresenta um levantamento estatístico por amostragem aleatória estratificada o qual foi realizado para se estimar a idade média da frota de caminhões em determinada região do país. Apopulação de caminhões foi divida em dois estratos A e B, dos quais foram selecionados — sem reposição
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

— 500 e 1.000 caminhões, respectivamente, perfazendo o total de 1,5 mil caminhões na amostra. Com base nessas informações e na tabela apresentada, julgue o seguinte item.
A alocação da amostra nesse levantamento foi do tipo uniforme. Nesse caso, a probabilidade de seleção de um caminhão da população foi igual a 0,05.
Item. 18. (Cebraspe/2013 - ANTT) Acerca da distribuição dos consumidores de determinado produto segundo suas preferências por marcas, sabe-se que, em determinada cidade, 20% dos consumidores preferem a marca A, 50%, a marca B e os 30% restantes, preferem a marca C. A marca A é importada e as marcas B e C são nacionais. Considere que os desvios padrão das rendas mensais dos consumidores que preferem as marcas A, B e C sejam, respectivamente, iguais a R$ 500,00, R$ 400,00 e 13xR$ 2.000,00.Uma amostragem aleatória estratificada de n=500 pessoas será retirada dessa população para estimar a renda média mensal dos consumidores desse produto dessa cidade.
Considerando que os três grupos de consumidores são os estratos da amostragem, julgue o item que se segue.
No caso da alocação proporcional ao tamanho dos estratos, a amostra deve consistir em
100 consumidores que preferem a marca A, 250 que preferem a marca B e 150 que preferem a marca C.
Item. 19. (CESPE 2007/TCU) Em auditoria, as técnicas de amostragem objetivam coletar e avaliar evidências numéricas das entidades administrativas no intuito de determinar e relatar o grau de adequação das informações obtidas. O método de amostragem probabilístico envolve a amostra aleatória simples, a estratificada e a amostra por conglomerados. Quanto a esse método, julgue o item abaixo.
Suponha-se que, em uma pesquisa, se pretenda estimar a proporção de beneficiários do crédito educativo que conseguem completar o curso superior. Suponha-se, ainda, que a metodologia de coleta de dados desse estudo seja feita por meio de questionários compulsórios e que estes sejam remetidos pelo correio. Nesse caso, a estratificação por curso, gênero ou localidade é relevante para o resultado da pesquisa, cujo método probabilístico é exemplo típico de amostra aleatória simples.
Item. 20. (CESPE 2010/MPU) Julgue o item a seguir, a respeito de amostragem por conglomerados,considerando uma população U = {1,..., 6} com conglomerados Cl = {1}, C2 = {2, 3} e C3 = {4, 5, 6}
e o vetor de dados associado D = (15,10, 4, 5, 8, 6).
Se dois dos três conglomerados — Cl, C2, C3 — da população U forem escolhidos em seguida para formar a amostra, as possíveis amostras serão: {1, 2, 3}, {1, 4, 5, 6}, {2, 3,1}, {2, 3, 4, 5, 6}, {4, 5, 6,1}, {4, 5, 6,1, 2, 3}.

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 21. (Cebraspe 2013/MPU) Julgue o item a seguir, a respeito de amostragem por conglomerados,considerando uma população U = {1,..., 6} com conglomerados Cl = {1}, C2 = {2, 3} e C3 = {4, 5, 6}
e o vetor de dados associado D = (15,10, 4, 5, 8, 6).
Se dois dos três conglomerados — Cl, C2, C3 — da população U forem escolhidos para formar a amostra, a média amostrai assume os seguintes possíveis valores: 29/3, 17/2 e 33/5, de modo que cada um desses valores ocorre com a mesma probabilidade, isto é, 1/3.
Item. 22. (Cebraspe 2013/MPU) Julgue o item a seguir, a respeito de amostragem por conglomerados,considerando uma população U = {1,..., 6} com conglomerados Cl = {1}, C2 = {2, 3} e C3 = {4, 5, 6}
e o vetor de dados associado D = (15,10, 4, 5, 8, 6).
Na amostragem por conglomerados, a população é subdividida em grupos com tamanhos não necessariamente iguais. A amostra obtida consiste da união dos conglomerados escolhidos e geralmente o tamanho dessa amostra é uma variável aleatória.
Item. 23. (CESPE 2011/TRE-ES) Julgue o item que se segue, referente às técnicas de amostragem e de inferência estatística.
Uma pesquisa de âmbito nacional para obter a intenção dos brasileiros na eleição para presidente daRepública pode ser feita com base em uma amostragem que considera pelo menos três estágios: por região,por estado e por município.

Item. 24. (Cebraspe/2019 - TJ-AM) Para avaliar a satisfação dos servidores públicos de certo tribunal no ambiente de trabalho, realizou-se uma pesquisa. Os servidores foram classificados em três grupos, de acordo com o nível do cargo ocupado. Na tabela seguinte, k é um índice que se refere ao grupo de servidores, e NR denota o tamanho populacional de servidores pertencentes ao grupo k.
nível do cargo k Nk nk Pk

1 1 500 50 0,7

II 2 300 20 0,8

III 3 200 10 0,9

De cada grupo k foi retirada uma amostra aleatória simples sem reposição de tamanho nk; pk representa a proporção de servidores amostrados do grupo k que se mostraram satisfeitos no ambiente de trabalho.A partir das informações e da tabela apresentadas, julgue o próximo item.

O desenho amostrai empregado nessa pesquisa foi a amostragem aleatória estratificada com alocação proporcional aos tamanhos dos estratos.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Item. 25. (Cebraspe/2013 - SEFAZ-ES)

Estrato Tamanho do Estrato Tamanho da Amostra Desvio Padrão da

Variável de Interesse

1 50.000 100

2 100.000 200

A tabela acima descreve um processo de amostragem do tipo aleatória estratificada. Com base nessas informações, assinale a opção correta.
a) A fração amostrai no estrato 2 é superior à fração amostrai no estrato 1.

b) Com respeito ao tamanho da amostra retirada de cada estrato, o plano amostrai apresentado considera a alocação ótima de Neyman.
c) Na amostragem em tela, retira-se uma amostra aleatória simples de cada estrato.

d) O objetivo da estratificação é formar subgrupos heterogêneos, de modo a maximizar o desvio padrão da variável de interesse em cada estrato.
e) No plano amostrai apresentado, para o cálculo da estimativa da média populacional,
é necessário utilizar um fator de expansão para corrigir os vícios na estimação provocados pela estratificação.
Item. 26. (Cebraspe 2018/STM) Um estudo acerca do tempo (x, em anos) de guarda de autos findos em determinada seção judiciária considerou uma amostragem aleatória estratificada. Apopulação consiste de uma listagem de autos findos, que foi segmentada em quatro estratos, segundo a classe de cada processo (as classes foram estabelecidas por resolução de autoridade judiciária). A tabela a seguir mostra os tamanhos populacionais (N) e amostrais (n), a média amostrai (x) e a variância amostrai dos tempos (s2)correspondentes a cada estrato.

Estratos

Tamanhos Populacionais (N)

Tamanhos Amostrais (n)

X s²

A 30.000

20 3

B 40.000

15 16

C 50.000

10 5

D 80.000 800
5 8

Total

200.000

Item. 2.000 - -

Considerando que o objetivo do estudo seja estimar o tempo médio populacional (em anos) de guarda dos autos findos, julgue o item a seguir.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

No desenho amostrai em tela há duas unidades amostrais: a primeira (unidade primária) corresponde à classe de cada processo, e a segunda (unidade secundária) refere-se a auto findo presente na listagem.
Item. 27. (Cebraspe 2018/STM) Um estudo acerca do tempo (x, em anos) de guarda de autos findos em determinada seção judiciária considerou uma amostragem aleatória estratificada. Apopulação consiste de uma listagem de autos findos, que foi segmentada em quatro estratos, segundo a classe de cada processo (as classes foram estabelecidas por resolução de autoridade judiciária). A tabela a seguir mostra os tamanhos populacionais (N) e amostrais (n), a média amostrai (x) e a variância amostrai dos tempos (s2)correspondentes a cada estrato.

Estratos

Tamanhos Populacionais (N)

Tamanhos Amostrais (n)

X s2

A 30.000

20 3

B 40.000

15 16

C 50.000

10 5

D 80.000 800
5 8

Total

200.000

Item. 2.000 - -

Considerando que o objetivo do estudo seja estimar o tempo médio populacional (em anos) de guarda dos autos findos, julgue o item a seguir.
No estudo em questão foi aplicada uma amostragem aleatória estratificada com alocação proporcional ao tamanho dos estratos.
Item. 28. (Cebraspe 2018/ABIN) Um levantamento amostrai foi realizado para se estimar o valor médio mensal (em R$ mil) per capita gasto em segurança da informação. Como a população de interesse se organiza naturalmente em 50 grupos de pessoas (facilmente identificáveis), decidiu-se selecionar ao acaso5 desses grupos. Todas as pessoas de cada grupo (i = 1, 2, ... , 5) foram entrevistadas, e os resultados encontrados são mostrados no quadro a seguir, que mostra também a quantidade (ni) de pessoas em cada grupo e o valor mensal gasto em segurança da informação por cada grupo (yi, em R$ mil).
i ni Yi

1 10 5

2 20 2

3 30 1

4 20 4

5 20 8

total 100 20

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

A partir dessas informações, julgue o item que se segue, a respeito do estimador de razão y =

Os grupos de pessoas representam subpopulações que constituem uma partição da população. Assim, o levantamento amostrai em questão exemplifica uma amostragem aleatória estratificada, em que os grupos formam os estratos e cada pessoa presente em um estrato é uma unidade amostrai.
Item. 29. (Cebraspe 2018/PF) Uma pesquisa realizada com passageiros estrangeiros que se encontravam em determinado aeroporto durante um grande evento esportivo no país teve como finalidade investigar a sensação de segurança nos voos internacionais. Foram entrevistados 1.000 passageiros,alocando-se a amostra de acordo com o continente de origem de cada um — África, América do Norte (AN), América doSul (AS), Ásia/Oceania (A/O) ou Europa. Na tabela seguinte, N é o tamanho populacional de passageiros em voos internacionais no período de interesse da pesquisa; n é o tamanho da amostra por origem; Pé o percentual dos passageiros entrevistados que se manifestaram satisfeitos no que se refere à sensação de segurança.
origem N n P

África

100.000

100 80

AN 300.000 300 70

AS 100.000 100 90

A/O

300.000

300 80

Europa

200.000

200 80

Total

1.000.000

1.000

Ppop

Em cada grupo de origem, os passageiros entrevistados foram selecionados por amostragem aleatória simples. A última linha da tabela mostra o total populacional no período da pesquisa,o tamanho total da amostra e Ppop representa o percentual populacional de passageiros satisfeitos.
A partir dessas informações, julgue o item.

Na situação apresentada, o desenho amostrai é conhecido como amostragem aleatória por conglomerados,visto que a população de passageiros foi dividida por grupos de origem.

Item. 30. (Cebraspe 2018/PF) Uma pesquisa realizada com passageiros estrangeiros que se encontravam em determinado aeroporto durante um grande evento esportivo no país teve como finalidade investigar a sensação de segurança nos voos internacionais. Foram entrevistados 1.000 passageiros,alocando-se a amostra de acordo com o continente de origem de cada um — África, América do Norte (AN), América doSul (AS), Ásia/Oceania (A/O) ou Europa. Na tabela seguinte, N é o tamanho populacional de passageiros
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

em voos internacionais no período de interesse da pesquisa; n é o tamanho da amostra por origem; P
é o percentual dos passageiros entrevistados que se manifestaram satisfeitos no que se refere à sensação de segurança.
origem
África

N
100.000

n P

100 80

AN 300.000 300 70

AS 100.000 100 90

A/O

300.000

300 80

Europa

200.000

200 80

Total

1.000.000

1.000

Ppop

Em cada grupo de origem, os passageiros entrevistados foram selecionados por amostragem aleatória simples. A última linha da tabela mostra o total populacional no período da pesquisa,o tamanho total da amostra e Ppop representa o percentual populacional de passageiros satisfeitos.
A partir dessas informações, julgue o item.

Nessa pesquisa, cada grupo de origem representa uma unidade amostrai, da qual foi retirada uma amostra aleatória simples.
Item. 31. (Cebraspe/2013 - CPRM)

Esquema de Amostragem para a área A

Esquema de Amostragem para a área B

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

Considere que um estudo estatístico tenha sido realizado para determinar a concentração média de uma substância em duas diferentes áreas (A e B). Considere, ainda, que as figuras acima apresentam os esquemas amostrais para essas áreas, que foram divididas em uma malha regular de três por cinco quadrados, e que os pontos mostrados nas figuras representam os locais em que os dados foram coletados. Com base nessas informações, julgue o próximo item.
Considere que, no esquema da amostragem para a área B, a posição dos pontos dentro de cada quadrado da malha tenha sido escolhida aleatoriamente. Nessa situação, é correto afirmar que o plano amostrai para essa área ocorreu por conglomerados.
Item. 32. (Cebraspe/2013 - CPRM)

Esquema de Amostragem para a área A

Esquema de Amostragem para a área B

Considere que um estudo estatístico tenha sido realizado para determinar a concentração média de uma substância em duas diferentes áreas (A e B). Considere, ainda, que as figuras acima apresentam os esquemas amostrais para essas áreas, que foram divididas em uma malha regular de três por cinco quadrados, e que os pontos mostrados nas figuras representam os locais em que os dados foram coletados. Com base nessas informações, julgue o próximo item.
O esquema amostrai para a área A caracteriza-se pela aplicação de uma malha regular com distribuição sistemática dos pontos de amostragem.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. LETRA C 12. CERTO
Item. 23. CERTO

Item. 2. CERTO 13. ERRADO
Item. 24. ERRADO

Item. 3. CERTO 14. CERTO
Item. 25. LETRA C

Item. 4. CERTO 15. ERRADO
Item. 26. ERRADO

Item. 5. CERTO 16. CERTO
Item. 27. CERTO

Item. 6. CERTO 17. ERRADO
Item. 28. ERRADO

Item. 7. LETRA C 18. CERTO
Item. 29. ERRADO

Item. 8. LETRA C 19. ERRADO
Item. 30. ERRADO

Item. 9. LETRA A 20. ERRADO
Item. 31. ERRADO

Item. 10. ERRADO 21. CERTO
Item. 32. CERTO

Item. 11. LETRA C 22. CERTO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

LISTA DE QUESTõES - CEBRASPE

Amostragem Não Probabilística

Item. 1. (CESPE/2011 - TER-ES) Julgue o item que se segue, referente às técnicas de amostragem e de inferência estatística.
No plano de amostragem por cotas, uma técnica probabilística, divide-se a população em classes de interesse e se seleciona uma quantidade de indivíduos de cada classe (quotas) para compor a amostra.
SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

GABARITo

Item. 1. ERRADO

SERPRO - Estatística e Probabilidade - 2023 (Pós-Edital)

