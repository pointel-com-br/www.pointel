# Raciocínio Lógico - Equivalências Lógicas

Índice

1) Equivalências Lógicas

2) Álgebra de Proposições

3) Questões Comentadas - Equivalências Lógicas - Cebraspe

4) Questões Comentadas - Introdução à Álgebra de Proposições - Cebraspe

5) Lista de Questões - Equivalências Lógicas - Cebraspe

6) Lista de Questões - Introdução à Álgebra de Proposições - Cebraspe

APRESENTAçÃo DA AULA

Fala, pessoal!

O principal assunto da aula de hoje é equivalências lógicas.

O entendimento da aula é muito importante, porém igualmente importante é que você DECORE as principais equivalências lógicas. Equivalências lógicas existem para serem usadas, e o uso delas requer que você tenha as principais fórmulas "no sangue".
Em seguida, será abordado álgebra de proposições. Nesse assunto, você deve focar nas propriedades comutativa, associativa e distributiva.
Como de costume, vamos exibir um resumo logo no início de cada tópico para que você tenha uma visão geral do conteúdo antes mesmo de iniciar o assunto.
Conte comigo nessa caminhada =)

Prof. Eduardo Mocellin.
(ÍS) @edu.mocellin

EQUIVALÊNCIAS LóGICAS

Equivalências lógicas

Duas proposições A e B são equivalentes quando todos os valores lógicos (V ou F) assumidos por elas são iguais para todas as combinações de valores lógicos atribuídos às proposições simples que as compõem.
Equivalências fundamentais p->q = ~q-»~p
Contrapositiva p-»q = ~pVq
Transformação da condicional em disjunção inclusiva pVq =~p->q
Transformação da disjunção inclusiva em condicional p«->q = (p->q)A(q->p)
Transformação da bicondicional em condicional/conjunção

Equivalências provenientes da negação de proposições
[Dupla negação da proposição simples|

~(~p) = p

[Negação da conjunção e da disjunção inclusiva (leis de De Morgan)|

Para negar "e": negar ambas as proposições e trocar por "ou".

~ (pA q) =~p V~q
Para negar "ou": negar ambas as proposições e trocar por "e".

~ (pVq) E~p A~q

[Negação da condicional|

(p->q) = pA~q

[Negação da disjunção exclusiva|

(pVq) = p«-»q

[Negação da bicondicional|

~(poq) = pYq

~(p<->q) = (~ p)«*q

~(p<^q) = p<->(~ q)

~(p<->q) = ( pA~q) V (qA~p)

Outras equivalências

|Equivalência do conectivo bicondicional|

p<H>q = (~p)<->(~q)

[Negação da conjunção para a forma condicional|

(pAq) = p->~q
(pAq) = q ->~p

|Conjunção de condicionais|

Quando o termo comum é o consequente, a equivalência apresenta uma disjunção inclusiva no antecedente.
(p^r)A(q^r) = (pVq)^r

Quanto o termo comum é o antecedente, a equivalência apresenta uma conjunção no consequente.

(p->q)A(p->r) = p->(qAr)

O que é uma equivalência lógica

Quando duas proposições apresentam a mesma tabela-verdade dizemos que as proposições são equivalentes.
A representação da equivalência lógica é dada pelo o símbolo <=> ou E. Se A é equivalente a B, podemos escrever de duas maneiras:
A <=> B

AEB

Observação: o símbolo de equivalência <=> é diferente do conectivo bicondicional <->

Informalmente, podemos dizer que duas proposições são equivalentes quando elas têm o mesmo significado. Exemplo:
a: "Eu moro em Taubaté."

b: "Não é verdade que eu não moro em Taubaté."
O conceito de equivalência lógica pode ser melhor detalhado assim:

TOME

NOTA!

Duas proposições A e B são equivalentes quando todos os valores lógicos (V ou F)
assumidos por elas são iguais para todas as combinações de valores lógicos atribuídos às proposições simples que as compõem.
Vejamos um exemplo:

Mostre que as proposições (p->q)A(q->p) e p<->q são equivalentes.

Para resolver esse problema, basta construirmos a tabela-verdade de ambas proposições. A
bicondicional já é conhecida por nós, então precisamos simplesmente confeccionar a tabela-verdade de (p->q)A(q-»p) e comparar com a bicondicional p<->q.
Passo 1: determinar o número de linhas da tabela-verdade.

Número de linhas = 2" = 22 = 4.

'i

Passo 2: desenhar o esquema da tabela-verdade.

Devemos determinar:

(p->q)A(q->p); (p->q); (q->p); p ; q

Podemos também incluir, de imediato, na nossa tabela a condicional p<->q, pois vamos compará-la com ai expressão que estamos querendo obter.:

Passo 3: atribuir V ou F às

Passo 4: obter o valor das demais proposições.

Para os condicionais, temos que eles só serão falsos nos casos em que o precedente é verdadeiro e o consequente é falso.
A conjunção (p->q)A(q-»p)
(q—>p) for verdadeiro.

i Para a bicondicional, já sabemos que ela será verdadeira quando p e q forem ambos verdadeiros ou ambos
: falsos.

p <7 p^q p^q

V V V V V V

V F F V F F

F V V F F F

F F V V V V

i Podemos perceber da análise da tabela-verdade acima que (p->q)A(q->p) e poq assumem os exatos
: mesmos valores lógicos para todas as possibilidades de p e q. Logo, as proposições são equivalentes. Veja:
Podemos escrever:

p-O-q <=> (p—>q)A(q—>p)

OU

p^>q = (p—»q )A(q—>p)

Equivalências fundamentais

Existem quatro equivalências fundamentais que devem ser entendidas e memorizadas. Dê especial atenção aos três primeiros casos que não só caem, mas despencam em provas de concurso público.
A primeira equivalência fundamental é conhecida como contrapositiva da condicional:

p->q = ~q->~p

A equivalência é realizada do seguinte modo:

1. Invertem-se as posições do antecedente e do consequente; e

2. Negam-se ambos os termos da condicional.

Como exemplo, sejam as proposições:

p: "Hoje choveu."

q: "João fez a barba."
A condicional dessas duas proposições pode ser escrita por:

p-»q: "Se [hoje choveu], então [João fez a barba]."

Observe que a frase seguinte é equivalente:

~q-»~p: "Se [João não fez a barba], então [não choveu]."

Um erro muito explorado pelas bancas é dizer que p->q seria equivalente a ~p-»~q. Isso porque é muito comum no dia-a-dia as pessoas cometerem esse erro.
Observe o exemplo acima: "se hoje choveu, então João fez a barba". Vamos supor que não choveu. O que podemos afirmar sobre barba de João? Absolutamente nada, ele pode tanto ter feito quanto não ter feito a barba.
Por outro lado, podemos afirmar sem dúvida que ~q-»~p, isto é, "se João não fez a barba,então hoje não choveu".

Em resumo: p->q não é equivalente a ~p->~q.

Mostre que são equivalentes p-»q e ~q-»~p.

Para mostrar a equivalência, montaremos a tabela-verdade de ~q->~p e compararemos com p-»q.

Passos 1, 2 e 3: determinar o número de linhas, desenhar o esquema e atribuir V ou
F às proposições simples de maneira alternada.
Vamos também incluir p->q para fins de comparação.

Para obter ~q->~p, basta observar que ela só será falsa quando ~q for verdadeiro ~p for falso.

Por fim, podemos incluir na assumidos por ~q-»~p.
Observe que os valores lógicos são exatamente iguais e, portanto, p->q e ~q->~p são equivalentes.

Vamos resolver dois exercícios envolvendo essa equivalência que acabamos de aprender.

(CBM AM/2022) Um antigo ditado diz: "Se há fumaça então há fogo".

Uma sentença logicamente equivalente é a) se há fogo então há fumaça.
b) se não há fumaça então não há fogo.

c) se não há fogo, então não há fumaça.

d) se não há fumaça pode haver fogo.

e) se há fogo então pode haver fumaça.

Comentários:

Sejam as proposições simples:

u: "Há fumaça."

o: "Há fogo."

A sentença original pode ser descrita por u->o:

u-»o: "Se [há fumaça], então [há fogo]".

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-»q
= ~q-»~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

u->o = ~o->~u

A proposição equivalente pode ser descrita por:

~o-»~u: "Se [não há fogo], então [não há fumaça]."

Gabarito: Letra C.

í (Pref. Bagé/2020) Uma proposição equivalente de "Se a prova está difícil, então
Antônio não será aprovado

: no concurso" é:

: a) A prova está difícil e Antônio não será aprovado no concurso.

b) Se Antônio for aprovado no concurso, então a prova não está difícil.

: c) A prova está fácil e Antônio foi aprovado no concurso.

d) A prova está fácil e Antônio não foi aprovado no concurso.

; e) A prova não está fácil e Antônio foi aprovado no concurso.

; Comentários:

= Sejam as proposições simples:

p: "A prova está difícil."

; a: "Antônio será aprovado no concurso."
A proposição original pode ser descrita por p->~a:

p-»~a: "Se [a prova está difícil], então [Antônio não será aprovado no concurso]."

= Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva:
p->q = ~q-»~p. Para

; aplicar essa equivalência, devemos realizar o seguinte procedimento:

: «^Invertem-se as posições do antecedente e do consequente; e i * Negam-se ambos os termos da condicional.
= Para o caso em questão, temos:

p->~a = ~(~a)->~p

= Como a dupla negação de a corresponde à própria proposição a, a condicional equivalente pode também ser descrita por a-»~p.
p->~a = a—>~p

: Logo, temos a seguinte proposição equivalente:

a->~p: "Se [Antônio for aprovado no concurso], então [a prova não está difícil]."

: Gabarito: Letra B.

INDO MAIS

FUNDO!

Na questão anterior definimos originalmente a seguinte sentença declarativa afirmativa:
a: "Antônio será aprovado."

A sua negação corresponde a:

~a: "Antônio não será aprovado."
A proposição original, nesse caso, foi descrita por p->~a.

Poderíamos ter resolvido a questão definindo originalmente uma sentença declarativa negativa. Isso em nada altera o gabarito. Poderíamos, portanto, ter definido a proposição a como:
a: "Antônio não será aprovado."
Nesse caso, a sua negação seria:

~a: "Antônio será aprovado."

A proposição original, a partir dessas novas definições, seria descrita por p->a.

A seguir, vamos resolver a mesma questão de outro modo. Compare com a resolução anterior.

í (Pref. Bagé/2020) Uma proposição equivalente de "Se a prova está difícil, então
Antônio não será aprovado

: no concurso" é:

= a) A prova está difícil e Antônio não será aprovado no concurso.

b) Se Antônio for aprovado no concurso, então a prova não está difícil.

: c) A prova está fácil e Antônio foi aprovado no concurso.

d) A prova está fácil e Antônio não foi aprovado no concurso.

: e) A prova não está fácil e Antônio foi aprovado no concurso.

; Comentários:

: Considere as proposições simples:

p: "A prova está difícil."

= a: "Antônio não será aprovado."

A proposição original é descrita por p-»a:

p->a: "Se [a prova está difícil], então [Antônio não será aprovado no concurso]."

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-»q
= ~q-»~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

p-»a = ~a->~p

Logo, temos a seguinte proposição equivalente:

~a->~p: "Se [Antônio for aprovado no concurso], então [a prova não está difícil]."

Gabarito: Letra B.

A segunda equivalência fundamental é a transformação da condicional em disjunção inclusiva:

p-»q = ~pVq

A equivalência é realizada do seguinte modo:

1. Nega-se o primeiro termo;

2. Troca-se a condicional (-») pela disjunção inclusiva (V); e

3. Mantém-se o segundo termo.

Como exemplo, considere novamente a seguinte condicional:

p-»q: "Se [hoje choveu], então [João fez a barba]."
Observe que a frase seguinte é equivalente:

~pVq: "[Hoje não choveu] ou [João fez a barba]."

Mostre que são equivalentes p-»q e ~pVq

Para mostrar a equivalência, montaremos a tabela-verdade de ~pVq e compararemos com p->q.

Passos 1, 2 e 3: determinar o número de linhas, desenhar o esquema e atribuir V ou
F às proposições simples de maneira alternada.
Vamos também incluir p->q para fins de comparação.

Passo 4: obter o valor das demais proposições.
Para obter ~p basta inverter o valor lógico de p.

Para obter ~pVq, basta observar que ela só será falsa quando ~p e q forem ambos falsos.

p 7 ~pVq

V V F V

V F F F

F V V V

F F V V

Por fim, podemos incluir na tabela a condicional p->q e comparar os valores lógicos assumidos por
~pVq.

Observe que os valores lógicos são exatamente iguais e, portanto, p->q e ~pVq são equivalentes.
p->q = ~pVq

Vamos resolver duas questões que utilizam essa equivalência.

r i (BANESTES/2021) A frase a seguir é um conhecido ditado popular:
"Se não tem cão então caça com gato"

: Uma frase logicamente equivalente é:

; a) Se tem cão então não caça com gato;

b) Se caça com gato então não tem cão;

= c) Tem cão ou caça com gato;

d) Tem cão e caça com gato;

= e) Tem cão ou não caça com gato.

; Comentários:

= Sejam as proposições simples:

c: "Tem cão."

g: "Caça com gato."

A proposição original pode ser descrita por ~c-»g:

~c->g: "Se [não tem cão], então [caça com gato]."

I

: As alternativas apresentam tanto condicionais (-») quanto uma disjunção inclusiva ("ou", V) como

; equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a condicional:
: * p->q = ~q->~p (contrapositiva)

; * p->q = ~p V q (transformação da condicional em disjunção inclusiva)

; Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento:

* Invertem-se as posições do antecedente e do consequente; e

: * Negam-se ambos os termos da condicional.

: Para o caso em questão, temos:

~c—>g = ~g—>~(~c)

A dupla negação de uma proposição corresponde à proposição original. Ficamos com:

: ~C"*g = ~g-»C

A proposição equivalente pode ser escrita por:

~g->c:"Se [não caça com gato], então [tem cão]."

Veja que essa equivalência não está nas alternativas apresentadas.

Vamos agora utilizar a segunda equivalência. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Nega-se o primeiro termo;

* Troca-se a condicional (-») pela disjunção inclusiva (V); e

* Mantém-se o segundo termo.

Para o caso em questão, temos:

~C-»g = ~(~c)Vg

A dupla negação de uma proposição corresponde à proposição original. Ficamos com:

~c->g = cVg

A proposição equivalente pode ser descrita por:

cVg: "[Tem cão] ou [caça com gato]."

Gabarito: Letra C.

(CM POA/2012) Se p e q são proposições, e o símbolo ~ denota negação, o símbolo V
denota o conetivo ou,
o símbolo A denota o conetivo e, símbolo -> denota o conetivo condicional, então a proposição (p-»~q) é equivalente à seguinte fórmula a) (~pA~q)
b) ~(pVq)

c) (~pAq)

d) (~pVq)

e) (~pV~q)
Comentários:

Note que a proposição original é uma condicional e, nas alternativas, as possíveis opções de equivalência são a conjunção ("e", A) e a disjunção inclusiva ("ou", A). Nesse caso, não devemos utilizar a equivalência contrapositiva, pois ela resulta em uma nova condicional. Devemos,portanto, aplicar a seguinte equivalência fundamental:
p-»q = ~pVq

A equivalência é realizada do seguinte modo:

* Nega-se o primeiro termo;

* Troca-se a condicional (-») pela disjunção inclusiva (V); e

* Mantém-se o segundo termo.

Aplicando essa equivalência para (p-»~q), temos:

p->(~q) = ~pV(~q)

A equivalência obtida corresponde à alternativa E: (~pV~q).
Gabarito: Letra E.

A terceira equivalência fundamental para sua prova é a transformação da disjunção em uma condicional:
pVq = ~p->q

A equivalência é realizada do seguinte modo:

1. Nega-se o primeiro termo;

2. Troca-se a disjunção inclusiva (V) pela condicional (->); e

3. Mantém-se o segundo termo.

Como exemplo, a disjunção inclusiva "[Pedro estuda] ou [trabalha]" é equivalente a "Se
[Pedro não estuda],

então [trabalha]".

INDO MAIS

FUNDO!

í Mostre que são equivalentes pVq e ~p-»q.

= Para demonstrar a equivalência, poderíamos estruturar a tabela-verdade de ~p-»q e comparar com PVq, i
; como feito nos exemplos anteriores. Contudo, existe uma outra forma.

Já vimos que uma equivalência da condicional corresponde a negar o primeiro termo e realizar uma disjunção inclusiva com o segundo termo. A equivalência que conhecemos é:
p->q = ~pVq

= Como as proposições p e q são arbitrárias (poderíamos ter chamado de r e s, por exemplo), podemos chamar ;
: a primeira proposição de (~p). Assim, continuamos com a mesma regra: negamos o primeiro termo e j realizamos uma disjunção inclusiva com o segundo termo.
(~P)->q = ~(~p)Vq

A dupla negação de uma proposição simples é equivalente à própria proposição simples,
isto é, ~(~p) = p.

Substituindo esse fato na equivalência acima, temos:

(~p)->q = pVq

Agora basta alterar a ordem da equivalência acima para chegarmos ao resultado que queremos:
pVq E~p->q

Vamos a um exercício.

í (Pref. Campinas/2019) Uma afirmação equivalente a: "Os cantadores da madrugada saíram hoje ou eu não
: ouço bem", é

; a) Os cantadores da madrugada não saíram hoje ou eu ouço bem.

b) Os cantadores da madrugada saíram hoje e eu ouço bem.

: c) Se os cantadores da madrugada saíram hoje, então eu não ouço bem.

d) Os cantadores da madrugada não saíram hoje e eu ouço bem.

: e) Se os cantadores da madrugada não saíram hoje, então eu não ouço bem.

; Comentários:

: Sejam as proposições simples:

m: "Os cantadores da madrugada saíram hoje."

o: "Eu ouço bem."

A afirmação original é dada pela disjunção inclusiva mV~o.

mV~o: "[Os cantadores da madrugada saíram hoje] ou [eu não ouço bem]."

: Sabemos que a disjunção apresenta uma equivalência fundamental dada por pVq = ~p-»q.
Isto é, deve-se

= realizar o seguinte procedimento:

i * Nega-se o primeiro termo;

: * Troca-se a disjunção inclusiva (V) pela condicional (->); e

: * Mantém-se o segundo termo.

Aplicando essa equivalência para proposição em questão, ficamos com:

mV~o = ~m-»~o

A equivalência obtida é descrita por:

~nw~o: "Se [os cantadores da madrugada não saíram hoje], então [eu não ouço bem]."
j Gabarito: Letra E.

DESPENCA NA

PROVA!

p-»q = ~ q-»~p p-»q = ~pVq pVq E~p->q
Apresentadas as três primeiras equivalências fundamentais, ressalto também que o resultado obtido com o exemplo do primeiro tópico é importante e deve ser memorizado:
peq E (p-*q)A(q->p)

Para exemplificar a equivalência, podemos dizer que a bicondicional "[Durmo] se e somente se [estou cansado]" é equivalente a "[Se (estou cansado), então (durmo)] e [se (durmo), então (estou cansado)]".
Os alunos costumam decorar essa equivalência com do seguinte modo: "uma forma equivalente à bicondicional é ir e voltar com a condicional".
ATENÇÃO

DECORE!

p<^q E (p->q)A(q-»p)

Mnemónico: Uma forma equivalente à bicondicional é ir e voltar com a condicional í (ISS RJ/2010) A proposição "um número inteiro é par se e somente se o seu quadrado for par" equivale
= logicamente à proposição:

: a) se um número inteiro for par, então o seu quadrado é par, e se um número inteiro não for par, então o
= seu quadrado não é par.

b) se um número inteiro for ímpar, então o seu quadrado é ímpar.

: c) se o quadrado de um número inteiro for ímpar, então o número é ímpar.

d) se um número inteiro for par, então o seu quadrado é par, e se o quadrado de um número inteiro não for par, então o número não é par.
: e) se um número inteiro for par, então o seu quadrado é par.

; Comentários:

Sejam as proposições:

p: "Um número inteiro é par."

q: "O quadrado de um número inteiro é par."

A proposição composta pode ser assim representada:

p<->q: "[Um número inteiro é par] se e somente se [o seu quadrado for par]."

A bicondicional é equivalente a:

P<H>q = (p->q)A(q->p)

Não temos alternativa que corresponda a essa última equivalência, porém, se realizarmos a contrapositiva de (q->p), encontramos:
poq = (p->q)A(~p->~q)

Esse resultado pode ser lido como:

(p-*q)A (~p-»~q): "[Se (um número inteiro for par), então (o seu quadrado é par)], e [se (um número inteiro não for par), então (o seu quadrado não é par)]."
Gabarito: Letra A

Equivalências provenientes da negação de proposições

FIQUE

ATENTO!

Antes de adentrarmos no assunto, é importante esclarecer que não se deve confundir equivalência com negação.
Ao se construir negação de uma proposição, constrói-se uma nova proposição com valores lógicos sempre opostos aos da proposição original.
Veremos mais adiante, por exemplo, que a negação de pAq é ~pV~q. Nesse caso:

* Não podemos dizer que pAq é equivalente a ~p V~q,

* Podemos dizer que ~(pAq) é equivalente a ~p V~q, isto é, ~(pAq) = ~p V~q.

Feitas estas considerações iniciais, passemos ao estudo das equivalências provenientes da negação de proposições.
Existem muitas maneiras de se expressar uma negação. A seguir serão apresentadas as formas mais comuns.
Dupla negação da proposição simples

Um resultado importante que pode ser obtido da tabela verdade é que a negação da negação de p sempre tem valor lógico igual a proposição p, ou seja, é equivalente a p.
~(~P) = P

A prova dessa equivalência corresponde à tabela-verdade abaixo.

Como exemplo, a dupla negação "Não é verdade que [Joãozinho não comeu o chocolate]" é equivalente a"Joãozinho comeu o chocolate".

ATENÇÃO

DECORE!

A negação da negação de p é equivalente a p.

~ (~P) = P

Negação da conjunção e da disjunção inclusiva (leis de De Morgan)

Negação da conjunção

Para realizar a negação conjunção pAq, deve-se seguir o seguinte procedimento:

1. Negam-se ambas as parcelas da conjunção;

2. Troca-se a conjunção (A) pela disjunção inclusiva (V).

Como resultado, podemos escrever que a negação de pAq, também conhecida por ~(pAq), é equivalente a
~p V~q:

~(pAq) =~p V~q

Como exemplo, sejam as proposições:

p: "Comi lasanha."

q: "Bebi refrigerante."
A conjunção dessas duas proposições pode ser escrita por:

pAq: "[Comi lasanha] e [bebi refrigerante]."

A negação dessa frase é:

~ (pAq) = ~p V~q: "[Não comi lasanha] ou [não bebi refrigerante]."

r

I

j Mostre que são equivalentes ~(pAq) e ~p V~q.

= Passos 1,2 e 3: determinar o número de linhas, estruturar a tabela-verdade e atribuir V ou F às proposições
= simples de maneira alternada.

= Para fins de comparação, vamos incluir ambas as proposições em uma mesma tabela.

p q ~p ~q pf\q ~(p^q) ~py~q

Passo 4: obter o valor das demais proposições.

~p e ~q são obtidos com a negação de p e q respectivamente.

P q ~P PAq ~(pAq) ~pV~q

V V F F

V F F V

F V V F

F F V V

A conjunção pAq só é verdadeira quando p e q são verdadeiras. Nos demais casos, será sempre falsa.

P q ~p ~q PAq ~(pAq) ~pV~q
V V F F V

V F F V F

F V V F F

F F V V F

A proposição — (PAq) é obtida pela negação de pAq.

P q ~p ~q pAq ~(pAq) ~pV~q

V V F F V F

V F F V F V

F V V F F V

F F V V F V

Finalmente, os valores lógicos da proposição ~pV~q são obtidos pela disjunção inclusiva de ~p e ~q, sendo falsa apenas quando ambas as proposições simples negadas forem falsas.
P q ~p ~q pAq ~(pAq) ~p\j~q
V V F F V F F

V F F V F V V

F V V F F V V

F F V V F V V

Observe que os valores lógicos assumidos por ~(pAq) e ~pV~q são iguais. Portanto, as proposições são equivalentes.
~ (pAq) =~p V~q

Negação da disjunção inclusiva

De modo semelhante à negação da conjunção, para negarmos a disjunção inclusiva pVq,
devemos seguir o seguinte procedimento:
1. Negam-se ambas as parcelas da disjunção inclusiva;

2. Troca-se a disjunção inclusiva (V) pela conjunção (A).

Como resultado disso, podemos escrever que a negação de pVq, também conhecida por ~(pVq), é equivalente a ~p A~q:
~ (pVq) = ~pA~q

Vejamos um exemplo:

pVq: "[Comi lasanha] ou [bebi refrigerante]."

A negação dessa frase seria:

~ (pVq) =~p A~q: "[Não comi lasanha] e [não bebi refrigerante]."
Essa equivalência pode ser facilmente constatada na tabela-verdade:

,*!v

"*DESPENCA NA

*V PROVA!

Para negar "e": negar ambas as proposições e trocar por "ou".

~ (pAq) =~p V~q

Para negar "ou": negar ambas as proposições e trocar por "e".

~ (pVq) =~p A~q

(SSP AM/2022) Considere a afirmação:

"Hoje é sexta-feira e amanhã não trabalharei".

A negação lógica dessa sentença é a) Hoje não é sexta-feira e amanhã trabalharei.
b) Hoje não é sexta-feira ou amanhã trabalharei.

c) Hoje não é sexta-feira, então amanhã trabalharei.

d) Hoje é sexta-feira e amanhã trabalharei.

e) Hoje é sexta-feira ou amanhã não trabalharei.

Comentários:

Sejam as proposições simples:

h: "Hoje é sexta-feira."

a: "Amanhã trabalharei."

A proposição original pode ser escrita pela conjunção hA~a:

hA~a:"[Hoje é sexta-feira] e [Amanhã não trabalharei]."

Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) =
~pV~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão,temos:

~(hA~a) = ~hV~(~a)

A dupla negação da proposição simples a corresponde à proposição original. Ficamos com:

~(hA~a) = ~hVa

Logo, a negação requerida pode ser descrita por:

~hVa: "[Hoje não é sexta-feira] ou [amanhã trabalharei]."

Gabarito: Letra B.

(SEMSA Manaus/2022) Considere a sentença:

"Paulo é torcedor do Nacional ou Débora não é torcedora do Fast".

A negação lógica dessa sentença é a) Paulo não é torcedor do Nacional ou Débora não é torcedora do Fast.
b) Paulo não é torcedor do Nacional ou Débora é torcedora do Fast.

c) Paulo não é torcedor do Nacional e Débora não é torcedora do Fast.

d) Paulo não é torcedor do Nacional e Débora é torcedora do Fast.

e) Paulo é torcedor do Nacional ou Débora é torcedora do Fast.

Comentários:

Sejam as proposições simples:

p: "Paulo é torcedor do Nacional."

d: "Débora é torcedora do Fast."

A sentença original pode ser descrita por pV~d:

pV~d: "[Paulo é torcedor do Nacional] ou [Débora não é torcedora do Fazt]."

Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(pVq) =
~pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da disjunção inclusiva;

* Troca-se a disjunção inclusiva (V) pela conjunção (A).

Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão,temos:

~(pV~d) = ~pA~(~d)

A dupla negação de d corresponde à proposição original. Ficamos com:

~(pV~d) = ~pAd

Logo, a negação requerida pode ser descrita por:

~pAd: "[Paulo não é torcedor do Nacional] e [Débora é torcedora do Fast]."

Gabarito: Letra D.

(TRT 9/2022) A negação da afirmação: "não ficou doente e vai ficar em casa" é:

a) Ficou doente e não vai ficar em casa.

b) Não ficou doente ou vai ficar em casa.

c) Ficou doente ou não vai ficar em casa.

d) Ficou doente ou vai ficar em casa.

e) Não ficou doente ou não vai ficar em casa.

Comentários:

Sejam as proposições simples:

d: "Ficou doente."

c: "Vai ficar em casa."

A proposição original pode ser escrita pela conjunção ~dAc:

~dAc:"[Não ficou doente] e [vai ficar em casa]."

Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) =
~pV~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão,temos:

~ (~dAc) = ~(~d)V~c

A dupla negação de c corresponde à proposição original. Ficamos com:

~(~dAc) = dV~c

Logo, a negação requerida pode ser descrita por:

dv~c: "[Ficou doente] ou [não vai ficar em casa]."

Gabarito: Letra C.

(SAAE/2018) Considere a afirmação:

Vou de tênis e visto um paletó, ou não faço sucesso.
Uma negação lógica dessa afirmação é:

a) Não vou de tênis ou não visto um paletó, e faço sucesso.

b) Vou de tênis e não visto um paletó, ou não faço sucesso.

c) Não vou de tênis ou visto um paletó, e faço sucesso.

d) Não vou de tênis e visto um paletó, ou não faço sucesso.

e) Vou de tênis ou visto um paletó ou faço sucesso

Comentário:

Sejam as proposições simples:

A afirmação do enunciado é dada por:

t: "Vou de tênis."
p: "Visto um paletó."
s: "Faço sucesso."

(tAp)V~s: "[(Vou de tênis) e (visto um paletó)], ou [não faço sucesso]."

A negação dessa frase é a negação de uma disjunção inclusiva ("ou", V) composta por dois termos: o termo
(tAp) e o termo ~s.

Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(pVq) =
~pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da disjunção inclusiva;

* Troca-se a disjunção inclusiva (V) pela conjunção (A).

Aplicando a equivalência em questão para negar (tAp)V~s, ficamos com:

~ [ (t Ap) V~s] = ~{tAp) A ~(~s)

Agora temos a negação da conjunção (tAp) e a dupla negação de s. Podemos novamente negar pAq por DeMorgan e, além disso, a dupla negação de s corresponde à proposição original s. Ficamos com:

(~tV~p)A|

(~tv~p) A s é a negação que estamos procurando e pode ser escrita assim:

(~tV~p) A s: "[(Não vou de tênis) ou (não visto um paletó)], e [faço sucesso]."

Gabarito: Letra A.

Negação da condicional

A negação de p-»q é realizada por meio da seguinte equivalência:

~ (p->q) = pA~q

A negação da condicional é realizada do seguinte modo:

1. Mantém-se o primeiro termo;

2. Troca-se a condicional (-») pela conjunção (A); e

3. Nega-se o segundo termo.

Como exemplo, considere a condicional:

p-»q: "Se [eu beber], então [dou gargalhadas]."
A negação dessa expressão pode ser escrita como:

~ (p->q) = pA~q: "[Eu bebo] e [não dou gargalhadas]."

INDO MAIS

FUNDO!

Mostre que ~(p—>q) é equivalente a pA~q.

Como não poderia deixar de ser, essa equivalência é obtida a partir da seguinte tabela-verdade:

p 9 ~<7 p/\~q P ^9 WWBI

V F F V F

V F v V F V

F v F V F

F F v F V F

Podemos obter o mesmo resultado de um outro modo, pois sabemos das equivalências fundamentais que:

p-»q = ~pVq

Se negarmos ambos os lados da equivalência anterior, obteremos:

~(p->q) E ~((~p)vq)

O lado direito dessa equivalência é a negação de uma disjunção. Utilizando a equivalência de De Morgan,obtemos:

~ÍP^q) = ~(~P)A~q i A negação da negação de uma proposição é a própria proposição original. Portanto:
~(p->q) E pA~q

Essa equivalência é muito importante e deve ser memorizada.

DESPENCA NA

PROVA!

~ (p->q) = pA~q

W APRESTE MAIS

ATENÇÃO!

Não confunda as seguintes equivalências p-»q = ~pVq
~(p-*q) E PA~q

(EPE/2022) A negação da afirmativa "Se João vai ao jogo, então o Flamengo perde" é a) João vai ao jogo e o Flamengo não perde.
b) João não vai ao jogo e o Flamengo perde.

c) João não vai ao jogo e o Flamengo não perde.

d) Se João não vai ao jogo, então o Flamengo perde.

e) Se João não vai ao jogo, então o Flamengo não perde.

Comentários:

Sejam as proposições simples:

j: "João vai ao jogo."

f: "O Flamengo perde."

A sentença original pode ser descrita por j-»f:

j—»f: "Se [João vai ao jogo], então [o Flamengo perde]".

i Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q)
= pA~q. Para aplicar essa i equivalência, devemos seguir o seguinte procedimento:
: * Mantém-se o primeiro termo;

: * Troca-se a condicional (->) pela conjunção (A); e i * Nega-se o segundo termo.
; Para o caso em questão, temos:

~(j—>f) = jA~f

: Logo, a negação pode ser descrita por:

jA~f: "[João vai ao jogo] e [o Flamengo não perde]."

: Gabarito: Letra A.

i (Pref. Panambi/2020) A negação da seguinte proposição composta: "Se estudo atentamente então serei
: nomeado em concurso público" é:

= a) Se não estudo atentamente, então não serei nomeado em concurso público.

b) Estudo atentamente e não serei nomeado em concurso público.

: c) Se não serei nomeado em concurso público, então não estudo atentamente.

d) Estudo atentamente ou serei nomeado em concurso público.

: e) Não estudo atentamente se, somente se não serei nomeado em concurso público.

; Comentários:

; Sejam as proposições simples:

e: "Estudo atentamente."

n: "Serei nomeado em concurso público."

A sentença original pode ser descrita por e->n:

e-»n: "Se [estudo atentamente] então [serei nomeado em concurso público]."

: Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q)
= pA~q. Para aplicar essa i equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

i * Troca-se a condicional (->) pela conjunção (A); e

: * Nega-se o segundo termo.

.

Aplicando para a condicional da questão, temos que a negação de e-»n é dada por:

~ (e-> n) = eA~n

Temos, portanto, a seguinte negação:

eA~n:" [Estudo atentamente] e [não serei nomeado em concurso público]."

Gabarito: Letra B.

Negação da disjunção exclusiva

A negação da disjunção exclusiva mais comum é equivalente a própria bicondicional.

~(pYq) E p<->q

Como exemplo, considere a disjunção exclusiva:

pVq: "Ou jogo bola, ou jogo sinuca."
A negação dessa expressão é dada pelo bicondicional abaixo:

~(pVq) E p<->q: "Jogo bola se e somente se jogo sinuca."

Mostre que são equivalentes ~(pVq) e p<->q.

Vamos colocar lado a lado as tabelas-verdade de poq e pVq.

pvq p++q

F V

V F

V F

F V

; Quando as proposições simples p e q têm o mesmo valor lógico, a disjunção exclusiva pVq é falsa. Nos demais
: casos, é verdadeira.

= Para a bicondicional poq ocorre exatamente o oposto: os casos em que ela é verdadeira são somente
= aqueles em que p e q são iguais.

: Isso significa que, ao negarmos a disjunção exclusiva, chegaremos à bicondicional. Veja:

PVq ~(pVq) P++P

F V V

V F F

V F F

F V V

Assim, temos:

~(pVq) E p«-»q

ATENÇÃO

DECORE!

A negação da disjunção exclusiva é equivalente a própria bicondicional.

~ (pVq) = p^q

Negação da bicondicional

São quatro as maneiras mais comuns de se negar a bicondicional. A primeira que vamos apresentar é que a negação da bicondicional é equivalente à disjunção exclusiva.
~(P<*q) = PYq

Mostre que ~ (p<->q) e pVq são equivalentes.

Essa relação pode ser provada portabela-verdade:

~(p++q) PYq

V F F

F V V

F V V

V F F

i Podemos também demonstrar a equivalência ~(p<->q) E (pVq) utilizando outra equivalência já conhecida, a
: negação da disjunção exclusiva:

~(pYq) E p<->q

: Podemos negar os dois lados desse resultado da seguinte forma:

~(~(pYq)) E ~(p<->q)

A proposição composta pVq é uma proposição assim como qualquer proposição simples, com a diferença que ela é resultado de uma composição de proposições simples por meio de um conectivo. Assim, continua válido o entendimento de que ao negar duas vezes uma proposição retornamos à proposição original.Logo:

PYq E ~(p<->q)

: Esse resultado pode ser escrito da seguinte forma, trocando os lados direito e esquerdo da equivalência
: anterior:

~(poq) = (pYq)

Podemos ainda negar a proposição bicondicional, negando apenas uma das suas proposições simples.
Veja:

~ (p<-»q) = (~p)<->q

~ (p<->q) = p<->(~q)

Lembre-se de que esses resultados também podem ser obtidos por tabela-verdade.

Cabe salientar que existe uma outra forma de negação da bicondicional utilizando apenas operadores de conjunção e disjunção:
~ (p<->q) = (pA~q) V (qA~p)

INDO MAIS

FUNDO!

Mostre que ~(p<->q) e (pA~q)V(qA~p) são equivalentes.

A utilização da tabela-verdade é a forma tradicional de se provar a equivalência. Vejamos, porém,
uma forma mais interessante de provar esta equivalência por meio de outras equivalências que já aprendemos.
Vamos utilizar uma equivalência fundamental já apresentada, que relaciona a bicondicional com duas condicionais:
P<->q =(p-»q)A(q-»p)

Se negarmos ambos os lados da equivalência teremos o seguinte:

~(p<^q) = ~((P->q)A(q-»p))

Veja-se que o lado direito da equivalência é a negação de uma conjunção, que pode ser reescrita utilizandoDe Morgan:

~ (p<-»q) = ~(p->q) v ~(q->p)

Agora devemos negar os dois condicionais, (p—>q) e (q—>p).

~ (P«*q) = (pA~ q) V (qA~p)

Finalmente chegamos à negação da bicondicional, utilizando apenas operadores de negação,
conjunção e disjunção inclusiva.
ATENÇÃO

DECORE!

As quatro formas mais comuns de negação da bicondicional são:

~ (p<->q) E pVq

~ (p«*q) E (~ p)<^q

~ (p«*q) E q)

~ (p<->q) E (pA~ q) V (qA~p)

Outras equivalências

Neste tópico, serão apresentadas outras equivalências que podem ser cobradas em prova, mas que apresentam menor incidência do que as ditas fundamentais.
Equivalência do conectivo bicondicional

Uma forma equivalente de se escrever a bicondicional é negar ambos os termos:

poq =

Para fins de exemplo, se considerarmos:

p<->q: "Hoje é dia 01/09 se e somente se hoje é o primeiro dia do mês de setembro."
Essa expressão é equivalente a:

~p<->~q: "Hoje não é dia 01/09 se e somente se hoje não é o primeiro dia do mês de setembro."
Verifiquemos na tabela-verdade:

^TACORDE!

Equivalência do bicondicional p<->q: negam-se p e q.

p<H>q = (~p)<->(~q)

Equivalência da negação do bicondicional ~(P<->q): nega-se apenas um dos termos.

~ (p<->q) = (~ p)<->q

~ (p<—>q) = po( q)

ATENÇÃO

DECORE!

Equivalência do bicondicional p<->q: nega-se tanto p quanto q.

p<->q E (~p)o(~q)

í (Pref. Vila Lângaro/2019) A negação da proposição "João passa no concurso público se e somente se João
: estuda" é:

: a) João não passa no concurso público se e somente se João não estudou.

b) João não passa no concurso público e João não estudou.

= c) João passa no concurso público e João estuda.

d) Ou João passa no concurso público ou João estuda.

= e) Se João passa no concurso público, então João estuda.

; Comentários:

A proposição composta original é uma bicondicional p<->q cujos termos são:

: p:" João passa no concurso público."
q:" João estuda."

= As principais formas de se negar a bicondicional são:

~ (p<-»q) E pVq

I

~ (p«*q) = (~ p)<->q

I

~ (p«*q) = P<H>(~ q)

~ (p<->q) E (pA~ q) V (qA~p)

I

A primeira forma apresentada corresponde à letra D:

pVq:" Ou [João passa no concurso público] ou [João estuda]."

= As demais formas apresentadas nas alternativas não correspondem à negação da bicondicional.
Especial atenção deve ser dada à alternativa A, que apresenta uma equivalência do bicondicional, não uma negação:
p<H>q E (~p)o(~q)

: Gabarito: Letra D.

Negações da conjunção para a forma condicional

Existem duas maneiras de se negar a conjunção de modo que ela adquira a forma condicional:

~(pAq) E p->~q

~(pAq) = q-»~p í Mostre que ~(pAq) = p-»~q são equivalentes.
: Utilizando a negação da conjunção por De Morgan:

~(pAq) = ~pV~q

: Chegamos a uma disjunção inclusiva, mas queremos encontrar uma condicional. Como proceder? Basta lembrar que existe uma equivalência fundamental que correlaciona a disjunção inclusiva com a condicional,que é dada por p V q = ~p->q. Essa equivalência nos diz basicamente que, para levar uma disjunção inclusiva para a condicional, devemos negar o primeiro termo e manter o segundo termo. Desse modo, vamos negar
: o primeiro termo e manter o segundo termo de ~p V~q.

~(pAq) E ~p V~q E ~(~p)-»~q

~(pAq) = ~(~p)->~q

A dupla negação de uma proposição é a própria proposição original. Assim, chegamos ao resultado

= pretendido:

~(pAq) E p->~q

Agora que sabemos que ~(pAq) E p-»~q, a prova da outra equivalência fica mais simples. Veja:

Mostre que ~(pAq) E q -» ~p são equivalentes.

Conhecemos a seguinte equivalência fundamental:

(i) . p->q E ~q ->~p

Essa equivalência nos mostra que uma condicional é equivalente à condicional resultante da negação das proposições originais, invertendo-se a posição do antecedente e do consequente.
Também conhecemos a seguinte equivalência:

(ii) . ~(pAq) = p-»~q

Utilizando-se a conclusão da equivalência (i) combinada à equivalência (ii), teremos:

~(pAq) E p—>~q = ~(~q) ->~p

A dupla negação ~(~q) equivale à proposição original q. Logo:

~(pAq) E q ->~p

ATENÇÃO

DECORE!

~(pAq) = p->~q

~(pAq) E q ->~p

(MRE/2016) Considere a sentença "Corro e não fico cansado". Uma sentença logicamente equivalente à negação da sentença dada é:
a) Se corro então fico cansado.

b) Se não corro então não fico cansado.

c) Não corro e fico cansado.

d) Corro e fico cansado.

e) Não corro ou não fico cansado.

Comentários:

Sejam as proposições simples:

c: "Corro."

f: "Fico cansado."
O enunciado apresenta a sentença cA~f e pede a negação ~(cA~f).

Observe que o enunciado requer a negação de uma conjunção e as alternativas apresentam condicionais("se...então"), conjunções ("e") e disjunção inclusiva ("ou"). Conhecemos três maneiras de se negar uma conjunção, sendo as duas últimas menos usuais:
(i) . ~(pAq) = ~pV~ q

(ii) . ~(PA q) E p->~ q

(iii) . ~(pAq) E q-> ~ p

Aplicando essas equivalências para o caso em questão, ficamos com:

(i) . ~(cA~f) = ~cV~(~f)

(ii) . ~(cA~f) = c^~(~f)

(iii) . ~(cA~f) = ~f-> ~c

Como uma dupla negação corresponde à proposição original, nossas equivalências ficam assim:

(i) . ~(cA~f) = ~cVf

(ii) . ~(cA~f) = c-»f
(iii). ~{cA~f) E ~f-> ~c

Observe que a equivalência (i). ~cVf: "[Não corro] ou [fico cansado]" não corresponde a nenhuma alternativa. Já a equivalência (ii) corresponde à letra A.
c-»f: "Se [corro], então [fico cansado]."

O gabarito, portanto, é a alternativa A.

Atenção! Poderíamos ter resolvido essa questão de uma outra maneira, sem precisar conhecer as"negações da conjunção para a forma condicional". Sejam as proposições simples:

c: "Corro."

f: "Fico cansado."

O enunciado apresenta a sentença cA~f e pede a negação ~(cA~f). Por De Morgan, temos:

~(cA~f) E ~c V ~(~f)

A dupla negação corresponde à proposição original. Logo, temos:

~(cA~f) = ~c V f

Veja que não temos como resposta ~cVf. Podemos transformar a disjunção inclusiva ~cVf em uma condicional utilizando a seguinte equivalência:
pVq = ~p-»q

Aplicando essa equivalência em ~c V f, que é negação de cA~f, ficamos com:

~(cA~f) E ~C V f E ~(~c)->f

A dupla negação de c corresponde à proposição simples c. Logo, ficamos com:

~(cA~f) E ~C V f E C—»f

Veja, portanto, que chegamos novamente na alternativa A:

c-»f: "Se [corro], então [fico cansado]."

Gabarito: Letra A.

Conjunção de condicionais

Existem duas equivalências que de vez em quando aparecem nas provas:

(p->r)A(q->r) = (pVq)->r

(p-»q)A(p-»r) = p^(qAr)

Quando o termo comum é o consequente, a equivalência apresenta uma disjunção inclusiva no antecedente.
(p—>r)A(q—>r) = (pVq)->r

Quanto o termo comum é o antecedente, a equivalência apresenta uma conjunção no consequente.
(p-»q)A(p->r) = p->(qAr)

Podemos verificar as duas equivalências por tabela-verdade:

j (SEFAZ-AL/2020) Considere as proposições:

= * Pl: "Se há carência de recursos tecnológicos no setor Alfa, então o trabalho dos servidores públicos que
: atuam nesse setor pode ficar prejudicado.".

= * P2: "Se há carência de recursos tecnológicos no setor Alfa, então os beneficiários dos serviços prestados por esse setor podem ser mal atendidos.".
A proposição P1AP2 é equivalente à proposição "Se há carência de recursos tecnológicos no setor Alfa, então
; o trabalho dos servidores públicos que atuam nesse setor pode ficar prejudicado e os beneficiários dos
: serviços prestados por esse setor podem ser mal atendidos.".

; Comentários:

: Considere as proposições simples:

; c: "Há carência de recursos tecnológicos no setor
Alfa."

t: "O trabalho dos servidores públicos que atuam nesse setor pode ficar prejudicado."

b: "Os beneficiários dos serviços prestados por esse setor podem ser mal atendidos."

A proposição Pl pode ser descrita por c->t e a proposição P2 pode ser descrita por c->b. Logo, a proposição
; P1AP2 pode ser descrita por:

(c->t)A(c->b)

: Devemos, portanto, avaliar se (c-»t)A(c-»b) é equivalente a:

; "Se [há carência de recursos tecnológicos no setor Alfa], então [(o trabalho dos servidores públicos que
Ê atuam nesse setor pode ficar prejudicado) e (os beneficiários dos serviços prestados por esse setor podem
: ser mal atendidos)]."

= Isto é, devemos avaliar se (c—>t)A(c—>b) é equivalente a c-»(tAb).

; Sabemos que essas duas proposições compostas são equivalentes, pois correspondem à seguinte
; equivalência estudada:

(p—>q)A(p—>r) = p->(qAr)

: O gabarito, portanto, é CERTO.

= Caso você não se lembre dessa equivalência na hora da prova, não se esqueça que
SEMPRE podemos

: recorrer à tabela-verdade para verificar se duas proposições são equivalentes. Isso porque, pela definição i de equivalências, temos que duas proposições A e B são equivalentes quando todos os valores lógicos (V ou
: F) assumidos por elas são iguais para todas as combinações de valores lógicos atribuídos às proposições j simples que as compõem.
Para o caso em questão, podemos montar a seguinte tabela-verdade:

Veja que ambas as proposições apresentam a mesma tabela-verdade e, portanto, são equivalentes.

Gabarito: CERTO.

(PF/2004) As proposições (PVQ)->S e (P->S)V(Q->S) possuem tabelas de valorações iguais.

Comentários:

A assertiva está ERRADA. A equivalência correta seria (P—>S)A(Q_—>S) = (PVQ)-»S.

Lembre-se que as equivalências mostradas nesse tópico são conjunções (A) de condicionais. Veja:

(p->r)A(q-»r) = (pVq)->r

(p—>q )A(p—>r) = p—>(qAr)

Para mostrar formalmente que (PVQ)->S e (P-»S)V(Q-»S) não possuem tabelas de valorações iguais, isto é,para mostrar que essas proposições não são equivalentes, podemos montar a seguinte tabela-verdade:

Gabarito: ERRADO.

Vamos agora praticar algumas questões gerais sobre o que aprendemos.

HORA DE

PRATICAR!

(CBM AM/2022) Gabriel comprou a camiseta do Nacional-AM, e guardou para uma ocasião especial. Certo dia, procurado em casa por um amigo, sua irmã disse:
"Vestiu a camiseta e foi ao jogo ou ao bar."

A negação lógica dessa sentença é:

a) Não vestiu a camiseta e foi ao jogo ou ao bar.

b) Vestiu a camiseta e não foi ao jogo ou ao bar.

c) Vestiu a camiseta e não foi ao jogo nem ao bar.

d) Não vestiu a camiseta ou foi ao jogo ou ao bar.

e) Não vestiu a camiseta ou não foi ao jogo nem ao bar.

Comentários:

Sejam as proposições simples:

v: "Vestiu a camiseta."

j: "Foi ao jogo."

b: "Foi ao bar."

A proposição original pode ser descrita pela conjunção entre v e (jvb), isto é, pode ser descrita por vA(jVb):
vA(jVb):"[Vestiu a camiseta] e [(foi ao jogo) ou (foi ao bar)]."

Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) =
~pV~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão,temos:

~ [vA(jVb)] E ~vV~(jVb)

Note que a parcela ~{jvb) também pode ser desenvolvida por De Morgan, e corresponde a
~jA~b. Portanto,
temos a seguinte equivalência:

~ [vA(jVb)] E ~vV(~jA~b)

Logo, a negação requerida pode ser descrita por:

~vV(~jA~b): "[Não vestiu a camiseta] ou [(não foi ao jogo) e (não foi ao bar)]."

Veja que essa negação é apresentada na alternativa E, que a representa a expressão "e não" por
"nem":

~vV(~jA~b): "[Não vestiu a camiseta] ou [(não foi ao jogo) (nem ao bar)]."

Gabarito: Letra E.

i (TJM SP/2021) Uma proposição equivalente a "Se acordei cedo e me alimentei, então tenho um dia
: produtivo" é a proposição:

= a) Não tenho um dia produtivo e não acordei cedo e não me alimentei.

b) Tenho um dia produtivo e não acordei cedo e não me alimentei.

= c) Se não tenho um dia produtivo, então não acordei cedo ou não me alimentei.

d) Se não tenho um dia produtivo, então não acordei cedo e não me alimentei.

= e) Se tenho um dia produtivo, então acordei cedo ou me alimentei.

; Comentários:

= Sejam as proposições simples:

c: "Acordei cedo."

a: "Me alimentei."

p: "Tenho um dia produtivo."

A proposição original pode ser descrita por cAa -» p.

cAa -> p:" Se [(acordei cedo) e (me alimentei)], então [tenho um dia produtivo]."

= Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva:
p-»q = ~q-»~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
: * Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

= Para o caso em questão, temos:

cAa -> p = ~p -* ~(cAa)

: O consequente obtido, ~(cAa), pode ainda ser desenvolvido por De Morgan. Nesse caso,
negam-se as duas

; parcelas e troca-se o "e" pelo "ou". Temos:

cAa -> p = ~p -» ~cV~a

: Ficamos com:

i ~p -> ~cV~a: "Se [não tenho um dia produtivo], então [(não acordei cedo) ou (não me alimentei)]."
= Gabarito: Letra C.

(DEPEN/2021) Com relação a lógica proposicional, julgue o item a seguir.

Considere as seguintes proposições p: "Paola é feliz";
q: "Paola pinta um quadro".

Assim, a proposição "Paola é feliz apenas se ela pinta um quadro" pode ser representada por ~(pA~q).
Comentários:

Sabemos que o conectivo "somente se" é do tipo condicional. Esse conectivo difere do
"se e somente se",

que é do tipo bicondicional.

Note que a proposição sugerida pelo enunciado é:

"[Paola é feliz] apenas se [ela pinta um quadro]"

O conectivo "apenas se" apresentado na questão corresponde ao condicional
"somente se". Logo, a proposição pode ser descrita por p-»q.
Veja que o enunciado sugere que a proposição composta pode ser representada por ~(pA~q). Podemos desenvolver essa negação por De Morgan. Para negar a conjunção "e", negam-se ambas as parcelas e troca-se o "e" pelo "ou". Ficamos com:

~(pA~q) = ~p V ~(~q)

A dupla negação de uma proposição simples corresponde à proposição original. Logo:

~(pA~q) = ~pVq

Nesse momento, você deve se lembrar da equivalência conhecida por
"transformação do condicional em disjunção inclusiva", dada por p-»q = ~pVq.
Conhecendo essa equivalência, observe que ~(pA~q) é equivalente a ~pVq que, por sua vez, é equivalente a p->q. Portanto:
~(pA~q) = p >q

Isso significa que a proposição p-»q, "Paola é feliz apenas se ela pinta um quadro", de fato pode ser representada por sua forma equivalente ~(pA~q). O gabarito, portanto, é CERTO.
Gabarito: CERTO.

ÁLGEBRA DE PROPOSIÇÕES

A álgebra de proposições trata do uso sequencial de equivalências lógicas e de outras propriedades para simplificar expressões.
O uso dessa ferramenta é interessante para resolver questões de um modo mais rápido.
Além disso, pode ser muito útil em questões mais diretas de equivalências lógicas, quando a banca tenta"esconder" a equivalência nas alternativas.
O mais importante é você conhecer as propriedades comutativa, associativa e distributiva e suas aplicações mais imediatas nas questões. Isso porque, via de regra, o conhecimento das demais propriedades não costuma ser cobrado e, além disso, é comum que as questões mais complexas de álgebra de proposições possam ser resolvidas por tabela-verdade.
FIQUE

ATENTO!

As três primeiras propriedades que serão apresentadas são as mais importantes para sua prova: comutativa, associativa e distributiva.
Questões mais complexas via de regra podem ser resolvidas por tabela-verdade. Nesses casos, a desenvoltura com álgebra de proposições seria apenas um "bônus" para que você resolva alguns problemas mais rapidamente.
Propriedade comutativa

Todos os conectivos, exceto o condicional "se...então", gozam da propriedade comutativa.
Isso quer dizer que é possível trocar a ordem dos componentes em uma proposição composta sem afetar o resultado da tabela-verdade:
pAq = qAp pVq = qVp pYq = qVp p<->q = q<->p
EXEMPLIFICANDO

Suponha que uma questão peça para você a negação da seguinte condicional:

p-*q: "Se eu correr, então chego a tempo."

Sabemos que essa condicional não goza da propriedade comutativa. A negação dessa condicional, pedida pela questão, pode ser encontrada pela seguinte equivalência:
(p—*q) E pA~q: "Corro e não chego a tempo.

Suponha agora que, dentre as alternativas da questão, você não encontre a proposição composta "Corro e não chego a tempo", porém encontre "Não chego a tempo e corro". Pode marcar essa alternativa sem medo!Isso porque, usando a propriedade comutativa, a conjunção obtida pA~q pode ser escrita como ~qAp:

(p-»q) E pA~q E ~qAp: "Não chego a tempo e corro.

TOME

NOTA!

Todos os conectivos exceto o condicional comutam:

pAq E qAp pVq E qVp pYq E qVp
P<->q E q<-»p

A condicional p->q não é comutativa. p-»q e q->p não são equivalentes.

A equivalência correta para a condicional é a contrapositiva:

p->q = ~q->~p

Essa propriedade é especialmente importante para questões de concurso público, pois muitas vezes a banca altera a ordem das proposições nas alternativas justamente para tentar esconder a resposta. Vamos a um exemplo.
(TJ SP/2015) Uma afirmação equivalente à afirmação: 'Se Marcondes é físico ou Isabela não é economista,então Natália não é advogada e Rui é médico', é:

a) Se Rui é médico ou Natália não é advogada, então Isa bela é economista e Marcondes não é físico.

b) Se Rui não é médico e Natália é advogada, então Isabela é economista ou Marcondes não é físico.

c) Se Marcondes não é físico e Isabela é economista, então Natália é advogada ou Rui não é médico.

d) Se Isabela é economista e Rui é médico, então Marcondes é físico e Natália não é advogada.

e) Se Rui não é médico ou Natália é advogada, então Isabela é economista e Marcondes não é físico.

Comentários:

Primeiramente, observe que a questão nos dá uma condicional e nos pede uma condicional equivalente. Isso significa que precisamos saber a contrapositiva:
Vamos dar nomes às proposições simples:

p-»q = ~q->~p m: "Marcondes é físico."i: "Isabela é economista."
n: "Natália é advogada."
r: "Rui é médico."

A proposição original do enunciado é dada por:

A contrapositiva equivalente é dada por:

(mV~i)-»(~nAr)

~(~nAr) ->~(mV~i)

As duas parcelas dessa condicional ainda podem ser melhor desenvolvidas por De Morgan:
para negar tanto a conjunção quanto a disjunção inclusiva, negam-se todas as parcelas e troca-se o operador ("e" para "ou" e vice-versa). Logo, podemos reescrever a expressão da seguinte forma:
(~(~n) V~r) -»(~ mA~(~i))

A dupla negação de uma proposição equivale à proposição original. Logo:

(n V~r) ->(~m A i)

Devemos, então, procurar pela seguinte frase:

II'Se [(Natália é advogada) ou (Rui não é médico)], então [(Marcondes não é físico) e (Isabela é economista)]"
i Veja que a letra E apresenta uma frase muito parecida. Essa alternativa utilizou a propriedade comutativa para o conectivo "e" e para o "ou" da nossa frase:
(n V~r) —»(~m A i) = (~r V n) —»(i A ~m)

"Se [(Rui não é médico) ou (Natália é advogada)], então [(Isabela é economista) e (Marcondes não é físiccj)]."
j Gabarito: Letra E.

Propriedade associativa

Na álgebra elementar, quando realizamos uma multiplicação, é comum ouvirmos a frase "a ordem dos fatores não altera o produto". Essa frase resume a propriedade associativa para a multiplicação.
Vamos supor que queremos realizar a multiplicação 3 x 5 x 7. Ela pode ser feita de duas formas:

* Multiplicamos 3 x 5 e depois multiplicamos esse resultado por 7, obtendo (3 x 5) x 7; ou

* Multiplicamos 3 pelo resultado da multiplicação de 5 x 7, obtendo 3 x (5 x 7).

Ou seja, na álgebra elementar, a propriedade associativa nos diz que em uma multiplicação de diversos termos, podemos realizar as operações de multiplicação na ordem que bem entendermos que o resultado será o mesmo:
(3 x 5) x 7 = 3 x (5x7)

O mesmo vale para a adição de termos:

(3 + 5) + 7 = 3 + (5 + 7)

Na álgebra de proposições temos algo muito semelhante. Dizemos que a conjunção "e" e a disjunção inclusiva "ou" gozam da propriedade associativa, sendo válidas as equivalências:
(pAq)Ar = pA(qAr)
(pVq)Vr = pV(qVr)

BrACORDE!

Observe que a propriedade associativa não mistura em uma mesma expressão o conectivo

"e" e o conectivo "ou"

Vamos a um exemplo que mostra uma utilidade para a propriedade associativa.

Mostre que pV(qV~p) é uma tautologia.

Lembre-se que uma tautologia ocorre quando a proposição em questão é sempre verdadeira.
Utilizando a propriedade comutativa em (qV~p), temos:

pV(~pVq)

Utilizando a propriedade associativa na expressão acima, temos:

(pV~p)Vq

(pV~p) é sempre verdadeiro, portanto, é uma tautologia. Logo, ficamos com:

tVq

Observe que a t V q é a disjunção inclusiva de um termo que é sempre verdade com a proposição q. Logo, se ao menos um dos termos é sempre verdadeiro (t), essa disjunção inclusiva é sempre verdadeira.Assim:

pV(qV~p) = t

Uma outra forma de se entender a propriedade associativa é perceber que, quando temos uma sequência de conjunções ou de disjunções inclusivas, podemos remover os parênteses.
í (TRT 1/2008) Proposições compostas são denominadas equivalentes quando possuem os mesmos valores i lógicos V ou F, para todas as possíveis valorações V ou F atribuídas às proposições simples que as compõem. :
= Assinale a opção correspondente à proposição equivalente a "-[[AA(-B)]->C]".

í a) AA(-B)A(-C)

b)(-A)V(-B)VC

í c) C-»[AA(--B)]

d) (-A)VBVC
j e) [(^A)AB]^«)

; Comentários:

A proposição original trata da negação de um condicional em que o antecedente da condicional é uma ;
= conjunção dada por [AA(~B)].

: Para negar uma condicional, utilizamos a equivalência ~ (p-> q) E pA~ q. Aplicando ao caso em questão, j
: devemos manter [AA(~B)j, trocar a condicional pela conjunção e negar C:

[AA(~B)J -> C E [AA(~B)JA(~C)

= Observe que, pela propriedade associativa, a ordem em que é executada a conjunção não importa. Logo, ;podemos escrever:

[AA(~B)J -» C E AA(~B)A(~C)

j Gabarito: Letra A.

Propriedade distributiva

Na álgebra elementar, a propriedade distributiva da multiplicação com relação à adição consiste em realizar a seguinte operação:
3x(5 + 7) = 3x5 + 3x7

Da mesma forma, podemos partir do lado direito da equação acima chegar ao lado esquerdo "colocando o número 3 em evidência":
3 x 5 + 3 x 7 = 3 x (5 + 7)

Na álgebra de proposições temos as seguintes propriedades distributivas:

* Do conectivo "e" com relação ao conectivo "ou";

* Do conectivo "ou" com relação ao conectivo "e".

Propriedade distributiva do "e" com relação ao "ou"

A propriedade distributiva do conectivo "e" em relação ao "ou" é dada pela equivalência abaixo. Perceba que nela "pA" é distribuído.
pA(qVr) = (pAq) V (pAr)

É importante também reconhecer a propriedade "de trás para frente". Isso significa que podemos colocar o termo "pA" em evidência.
(pAq)V(pAr) = pA(qVr)

Propriedade distributiva do "ou" com relação ao "e"

A propriedade distributiva do conectivo "ou" em relação ao "e" é dada pela equivalência abaixo. Perceba que nela "pV" é distribuído.
pV(qAr) = (pVq) A (pVr)

É importante também reconhecer a propriedade "de trás para frente". Isso significa que podemos colocar o termo "pv" em evidência.
(p\/jq) A (pVr) = pV(qA r)

(SEFAZ SC/2010) Na questão, considere a notação -X para a negação da proposição X.

Considere as proposições a e b e assinale a expressão que é logicamente equivalente a (a A b) V (a
A -b)

a) -a A-b b) -a V-b c) -a V b d) a V -b e) a
Comentários:

Por meio da propriedade distributiva, podemos colocar "aA" em evidência:

(aAb)V (aA~b) E aA (bv~b)

A expressão (bv~b) é uma tautologia. Logo, aA (bv~b) corresponde a:

aAt

Perceba que o valor da conjunção é determinado exclusivamente por a, uma vez que a outra parcela da conjunção é sempre verdadeira. Portanto:
(aAb)V(aA~b) E a

Gabarito: Letra E.

í (Pref. Alumínio/2016) Considere a afirmação: Sueli é professora e, pratica ginástica ou pratica corrida. Uma
: afirmação equivalente é

A) Sueli é professora e pratica ginástica e pratica corrida.

= B) Se Sueli é professora, então ela não pratica ginástica e não pratica corrida.

i C) Sueli é professora e pratica ginástica, ou é professora e pratica corrida.

: D) Se Sueli não pratica ginástica ou não pratica corrida, então ela é professora.

: E) Sueli pratica ginástica e pratica corrida, ou é professora.

; Comentários:

: Sejam as proposições simples:

= s: "Sueli é professora."
g: "Sueli pratica ginástica."

k: "Sueli pratica corrida."

; Na afirmação do enunciado, a vírgula após o "e" indica parênteses na proposição composta:

: "[Sueli é professora] e, [(pratica ginástica) ou (pratica corrida)]."
Logo, temos a seguinte representação:

sA(gVk)

Por meio da propriedade distributiva, podemos distribuir "sA":

sA(gVk) = (sAg)V(sAk)

Temos, portanto, a seguinte equivalência:

(sAg)V(sAk): "([Sueli é professora] e [pratica ginástica]), ou ([Sueli é professora] e [pratica corrida])"
Essa equivalência corresponde à alternativa C.

Gabarito: Letra C.

Quanto temos um condicional e queremos utilizar a álgebra de proposições para resolver alguma questão,é necessário transformar a condicional em disjunção inclusiva por meio da seguinte equivalência já conhecida:
p-»q = ~pVq

Lembre-se, também, que temos como transformar a negação da condicional em uma conjunção:
~(p->q) E pA~q

Vejamos um exemplo.

í (TCE-RO/2013) Com referência às proposições lógicas simples P, Q e R, julgue o próximo item.

= Se -R representa a negação de R, então as proposições PV[-(Q^R)] e (PVQ)A[PV(-R)] são equivalentes.
; Comentários:

i Note que poderíamos resolver essa questão comparando as tabelas-verdade das duas proposições. Nesse
; momento, vamos resolver o problema com álgebra de proposições.

A nossa estratégia será desenvolver PV[~(Q-»R)] para tentar chegar em (PVQ)A[PV(~R)].

: Veja que, para a negação da condicional (Q->R), podemos utilizar a equivalência
~(p-»q) = pA~q. Logo,

i PV[~(Q-»R)] corresponde a:

PV[QA~R]

Aplicando a propriedade distributiva em "PV", temos:

PV[QA~R] = [PVQ] A [PV~R]

í Note, portanto, que a partir de PV[~(Q->R)] chegamos em [PVQ]A[PV~R]. Logo,
as proposições são

: equivalentes.

; Gabarito: CERTO.

Propriedade da identidade, da absorção e da idempotência

FPRESTE MAIS

ATENÇÃO!

Trate as propriedades da identidade, da absorção e da idempotência como um "bônus"
que pode te ajudar em algumas questões mais difíceis. Não se apegue muito a essas propriedades, pois elas não costumam aparecer em prova.
Para melhor memorizar as propriedades da identidade e da absorção, podemos estabelecer uma analogia entre lógica de proposições e conjuntos.
Lógica de Proposições Conjuntos
Tautologia (í) Conjunto Universo (U)
Contradição (c) Conjunto Vazio (0)

Conjunção (A) Intersecção (A)
Disjunção Inclusiva (V) União (u)

Observada a analogia, vamos às propriedades.

Propriedade da identidade

Propriedade da identidade para a conjunção

Sendo t uma tautologia e c uma contradição, temos as seguintes equivalências:

pAt = p p A c = c
Note que p A t é equivalente a p porque se trata de uma conjunção em que um termo é sempre verdadeiro
(t). Isso significa que o valor de p A t é consequência somente do valor de p:

* Se p for verdadeiro, teremos V A V, que é uma conjunção verdadeira; e

* Se p for falso, teremos F A V, que é uma conjunção falsa.

Além disso, p A c é equivalente a c porque se trata de uma conjunção em que temos um termo sempre falso
(C).

Para fins de memorização, observe o análogo da teoria dos conjuntos:

Propriedade da identidade para a disjunção inclusiva

Sendo t uma tautologia e c uma contradição, temos as seguintes equivalências:

pVtEt pVc = p
Note que p V t é equivalente a t porque se trata de uma disjunção inclusiva em que temos um termo sempre verdadeiro (t).
Além disso, p V c é sempre equivalente a p porque se trata de uma disjunção inclusiva em que um termo é sempre falso (c). Isso significa que o valor de pVc é consequência somente do valor de p:
* Se p for verdadeiro, teremos V V F, que é uma disjunção verdadeira; e

* Se p for falso, teremos F V F, que é uma disjunção falsa.

Para fins de memorização, observe o análogo da teoria dos conjuntos:

i (ANPAD/2014) A proposição composta pA(qV(~p)) é logicamente equivalente à proposição
A)q

: B) pAq

Í C) pVq

: D) pA(~q)

: E) pV(~q)

= Comentários:

= Aplicado a propriedade distributiva em " pA", temos:

pA(qV~p) = (pAq) V (pA~p)

= (pA~p) é uma contradição. Logo, ficamos com:

(pAq) V c

A disjunção inclusiva de um termo com uma contradição corresponde ao próprio termo (propriedade da

; identidade para a disjunção inclusiva). Logo, temos:

(pAq)

; Gabarito: Letra B.

Propriedade da absorção

A propriedade da absorção é representada por duas equivalências:

pV(pAq) = p pA(pVq)sp
Para fins de memorização, observe o análogo da teoria dos conjuntos:

pV(pAç) = p

Essas equivalências são demonstráveis por tabela-verdade:

p q pAç pV(pAç)

M V V V

M F F V
F V F F

F F F F

P 9 pA(pVç)

M V V V
V F V V

F V V F

F F F F

í (SEFAZ-MS/2006) Representando por ~r a negação de uma proposição r, a negação de p
A (p V q) é

= equivalente a:

i a) ~p.

b) ~q.

: c) ~(p V q).

d) ~(P Aq).

= e) uma contradição.

= Comentários:

= Pela propriedade da absorção, sabemos que p A (p V q) = p. Logo, a negação pedida é ~p.

= Gabarito: Letra A.

Propriedade da idempotência

A propriedade da idempotência é representada por duas equivalências:

pAp = p pVp = p
O análogo à teoria dos corresponderia à intersecção de um conjunto com ele mesmo e à união de um conjunto com ele mesmo.
Essas equivalências são demonstráveis por tabela-verdade:

p P P^P

V V V

F F F

í (DPEN/2013) Considerando que, P, Qe R são proposições conhecidas, julgue o próximo item.
A Proposição -[(P -> Q) V Q] é equivalente à proposição P A (-Q), em que -P é a negação de P.

; Comentários:

= Primeiramente, vale perceber que essa questão pode ser resolvida por tabela-verdade, pois para duas
: proposições serem equivalentes basta que elas apresentem a mesma tabela-verdade.

= Dito isso, vamos resolver a questão por álgebra de proposições. A nossa estratégia será partir de i ~[(P-»Q)VQ] para chegar em PA(~Q).
: Vamos desenvolver ~[(P-»Q)VQ] por De Morgan, negando cada parcela da disjunção inclusiva e trocando
: "ou" por "e":

~(P—>Q)A—Q

= Para negar uma condicional, utilizamos a seguinte equivalência: ~(p-> q) = pA~ q.
Ficamos com:

[PA(~Q)]A(~Q)

Pela propriedade associativa, podemos escrever:

PA[(~Q)A(~Q)]

Observe que, pela propriedade idempotente, [(~Q)A(~Q)] apresenta sempre o valor lógico de (~Q). Isso porque Quando (~Q) é V, [(~Q)A(~Q)J é V, e quando (~Q) é F, [(~Q)A(~Q)] é F. Logo, nossa conjunção fica:
PA(~Q)

Gabarito: CERTO.

Equivalências lógicas x tautologia, contradição e contingência

Você se lembra que um dos métodos para descobrirmos se uma proposição composta é uma tautologia,
uma contradição ou uma contingência é utilizar equivalências lógicas ou álgebra de proposições?

Esse método costuma ser o mais rápido, porém requer o domínio das equivalências lógicas e das propriedades da álgebra de proposições.
Voltemos ao exemplo da aula de tautologia, contradição e contingência: queremos verificar se a proposição abaixo é uma tautologia:
((pAq) —> r) <-> (p—>(q—»r)) é uma tautologia?

Agora conhecemos a seguinte equivalência: (p—>q) = (~pVq). Aplicando essa equivalência a cada um dos lados da expressão bicondicional do nosso exemplo, tem-se que:
Lado esquerdo: ((pAq) -> r) = ~(pAq) V r
Lado direito: (p-> (q-> r)) = ~pV (q-> r)

Portanto, reescrevendo a bicondicional original ((pAq) -> r) <-> (p->(q-> r)), temos:

Prosseguindo, por De Morgan, a proposição composta ~(pAq), ao lado esquerdo da expressão, pode ser reescrita como (~pV~q). Já a condicional q-»r, ao lado direito, pode ser reescrita como seu equivalente
~qVr. Fazendo as devidas substituições na expressão obtida no passo anterior, ~(pAq) V
r<-> ~pV(q-> r),

teremos:

(~pV~q) V r <-> ~pV(~q V r)

Observe os dois lados da bicondicional. Eles são muito parecidos, exceto pelo uso dos parênteses que indicam uma ordem diferente de se executar o operador "ou". Utilizando a propriedade associativa do lado direito da bicondicional, podemos reescrever:
(~pV~q) V r <-> (~pV ~q) V r

Podemos concluir, portanto, que ambos os lados da expressão bicondicional são idênticos, e, por conseguinte, sempre assumirão o mesmo valor lógico. Isso significa que o nosso bicondicional sempre será verdadeiro e, portanto, é uma tautologia.
Pessoal, uma vez que se tem a prática com álgebra de proposições, a resolução de algumas questões de tautologia, contradição e contingência ficam mais rápidas. Observe, porém, que sempre é possível resolver esse tipo de questão por tabela-verdade ou pelo método da conclusão falsa.
Vamos resolver alguns exercícios do assunto utilizando equivalências lógicas.

l

HORA DE

PRATICAR!

: (STJ/2018) Considere as proposições PeQa seguir.

: P: Todo processo que tramita no tribunal A ou é enviado para tramitar no tribunal B ou no tribunal C.
; Q: Todo processo que tramita no tribunal C é enviado para tramitar no tribunal B.
A partir dessas proposições, julgue o item seguinte.

A proposição —P—>(P—>Q_), em que -P denota a negação da proposição P, é uma tautologia, isto é,
todos os

; elementos de sua tabela-verdade são V (verdadeiro).

; Comentários:

: Temos a proposição:

~P-> (P-»Q)

: Utilizando a equivalência p->q = ~pVq, temos:

~(~P)V(P—>Q)
PV(P—>Q)

: Novamente, utilizando a mesma equivalência para (P->Q):

PV(~PVQ)

Utilizando a propriedade associativa:

(PV~P)VQ

PV~P é uma tautologia, logo:

tVQ

í Observe que t V Q é a disjunção inclusiva de um termo que é sempre verdade com a proposição Q. Portanto, i
= como ao menos um dos termos é sempre verdadeiro (t), essa disjunção inclusiva é sempre verdadeira ;
: (propriedade da identidade para a disjunção inclusiva). Logo, trata-se de uma tautologia.

; Gabarito: CERTO.

(CBM AL/2017) A respeito de proposições lógicas, julgue o item a seguir.

Se P e Q forem proposições simples, então a proposição composta QV(Q->P) é uma tautologia.

Comentários:

Temos a seguinte proposição composta:

QV (Q -> P)

Utilizando a equivalência p->q = ~pVq para (Q-> P), temos:

QV(~QV P)

Pela propriedade associativa, podemos escrever:

(QV~Q)VP

QV~Q é uma tautologia. Portanto, ficamos com:

tVP

Observe que a t V P é a disjunção inclusiva de um termo que é sempre verdade com a proposição P. Portanto,como ao menos um dos termos é sempre verdadeiro (t), essa disjunção inclusiva é sempre verdadeira(propriedade da identidade para a disjunção inclusiva). Logo, trata-se de uma tautologia.

Gabarito: CERTO.

QUESTõES CoMENTADAS - CEBRASPE

Equivalências lógicas

Equivalências fundamentais l.(CESPE/PC DF/2021) Com relação a estruturas lógicas, lógica de argumentação e lógica proposicional,julgue o item subsequente.

A proposição "Se Paulo está mentindo, então Maria não está mentindo" é equivalente à proposição "SeMaria está mentindo, então Paulo não está mentindo".

Comentários:

Sejam as proposições simples:

p: "Paulo está mentindo."

m: "Maria está mentindo."
A proposição original pode ser descrita por p-»~m:

p->~m: "Se [Paulo está mentindo], então [Maria não está mentindo].

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-»q
= ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

p-»~m = ~(~m)-»~p

A dupla negação de m corresponde à proposição original. Logo, temos:

p->~m = m->~p

A proposição equivalente pode ser escrita por:

m-»~p: "Se [Maria está mentindo], então [Paulo não está mentindo]."

Gabarito: CERTO.

2.(CESPE/PM TO/2021) A proposição "Se André é culpado então Bruno não é suspeito" é equivalente à a) "Se Bruno é suspeito então André é inocente".
b) "Se Bruno não é suspeito então André é culpado".

c) "Se Bruno é suspeito então André não é inocente".

d) "Se André é inocente então Bruno é culpado".

e) "Se André não é culpado então Bruno é suspeito".

Comentários:

Sejam as proposições simples:

a: "André é culpado."

b: "Bruno é suspeito."
A proposição original pode ser descrita por a-»~b:

a-»~b: "Se [André é culpado], então [Bruno não é suspeito].

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p->q
= ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

a-»~b E ~(~b)-»~a

A dupla negação de b corresponde à proposição original. Logo, temos:

a->~b = b->~a

A proposição equivalente pode ser escrita por:

b-»~a: "Se [Bruno é suspeito], então [André não é culpado]."

Nessa questão, a banca utilizou "é inocente" como forma de se negar "é culpado".
Sabemos que a utilização de antônimos deve ser evitada, pois muitas vezes esse tipo de negação não abarca todas as possibilidades.Ocorre que o CESPE não costuma entrar nesse nível de detalhe, especialmente em questões envolvendo equivalências lógicas ou lógica de argumentação. Portanto, nesse tipo de questão, via de regra você pode negar usando antônimos, especialmente quando não há uma alternativa melhor.
Logo, a nossa proposição equivalente pode ser escrita por:

b-»~a: "Se [Bruno é suspeito], então [André é inocente]."

Gabarito: Letra A.

3.(CESPE/SEFAZ AL/2020) P: "Se o trabalho dos servidores públicos que atuam no setor Alfa fica prejudicado, então os servidores públicos que atuam nesse setor padecem.".
A proposição P é equivalente à proposição "Se os servidores públicos que atuam nesse setor não padecem,então o trabalho dos servidores públicos que atuam no setor Alfa não fica prejudicado."

Comentários:

Sejam as proposições simples:

a: "O trabalho dos servidores públicos que atuam no setor Alfa fica prejudicado."

p: "Os servidores públicos que atuam nesse setor padecem."
A proposição P pode ser descrita por a-»p:

a->p: "Se [o trabalho dos servidores públicos que atuam no setor Alfa fica prejudicado], então [os servidores públicos que atuam nesse setor padecem].
Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-»q
E ~q-»~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

a->p E ~p->~a

A proposição equivalente pode ser escrita por:

~ p-> ~a: "Se [os servidores públicos que atuam nesse setor não padecem], então [o trabalho dos servidores públicos que atuam no setor Alfa não fica prejudicado]."
Gabarito: CERTO.

4.(CESPE/TJ-SE/2014) Considerando que P seja a proposição "Se os seres humanos soubessem se comportar, haveria menos conflitos entre os povos", julgue o item seguinte.
A proposição P é logicamente equivalente à proposição "Se houvesse menos conflitos entre os povos,
os seres humanos saberiam se comportar".
Comentários:

Sejam as proposições simples:

h: "Os seres humanos sabem se comportar."

k: "Há menos conflitos entre os povos."

A proposição original pode ser descrita por uma condicional h->k na forma "Se p, q",
em que se omite o
"então".

h-»k: "Se [os seres humanos soubessem se comportar], [haveria menos conflitos entre os povos]."

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-»q
= ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

h->k = ~k-»~h

A proposição equivalente pode ser escrita por:

~k-»~h: "Se [não houvesse menos conflitos entre os povos], [os seres humanos não saberiam se comportar]."
Note que a questão nos trouxe o condicional k->h, isto é, inverteu a ordem do antecedente e do consequente sem negá-los. O gabarito, portanto, é ERRADO.
Gabarito: ERRADO.

5.(CESPE/EMAP/2018) Julgue o item seguinte, relativo à lógica proposicional e de argumentação.

A proposição "Se Sônia é baixa, então Sônia pratica ginástica olímpica." é logicamente equivalente à sentença "Se Sônia é alta, então Sônia não pratica ginástica olímpica."
Comentários:

Considere as proposições simples:

b: "Sônia é baixa."

g: "Sônia pratica ginástica olímpica."
A proposição original pode ser descrita por b-»g.

b->g: "Se [Sônia é baixa], então [Sônia pratica ginástica olímpica]."

Para essa questão, vamos considerar correta a negação b utilizando o antônimo "alta". Nesse caso,
temos:

~b: "Sônia é alta."

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-»q
E ~q-»~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

b->g = ~g -»~b

~g ->~b: "Se [Sônia não pratica ginástica olímpica], então [Sônia é alta]."

Note que a questão nos trouxe o condicional ~b->~g, isto é, realizou as negações das proposições simples sem inverter a ordem do antecedente e do consequente. O gabarito, portanto, é ERRADO.
Observação: A negação utilizando antônimos não é recomendada, pois muitas vezes esse tipo de negação não abarca todas as possibilidades. No exemplo da questão, Sônia poderia ter estatura mediana e, desse modo, não seria baixa. Ocorre que o CESPE não costuma entrar nesse nível de detalhe,especialmente em questões envolvendo equivalências lógicas ou lógica de argumentação. Portanto, nesse tipo de questão, via de regra você pode negar usando antônimos, pois a banca CESPE não costuma invalidar uma questão por causa disso.
Gabarito: ERRADO.

6.(CESPE/MDIC/2014) A proposição "Se o interessado der três passos, alugará a pouca distância uma loja por um valor baixo" é equivalente à proposição "Se o interessado não der três passos, não alugará a pouca distância uma loja por um valor baixo".
Comentários:

Sejam as proposições simples:

i: "O interessado dá três passos."

a: "O interessado aluga a pouca distância uma loja por um valor baixo."

A proposição P é uma condicional da forma "Se p, q", em que se omite o "então".
Trata-se da condicional i->a:
i-»a: "Se [o interessado der três passos], [alugará a pouca distância uma loja por um valor baixo]."
Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-»q
E ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

i->a = ~a->~i

A condicional equivalente pode ser escrita dessa forma:

~a-»~i: "Se [o interessado não alugar a pouca distância uma loja por um valor baixo], [o interessado não deu três passos]."
O enunciado apresentou como equivalente a proposição ~i->~a, ou seja, negou as parcelas da condicional sem trocar de lugar o antecedente e o consequente. O gabarito, portanto, é ERRADO.
Gabarito: ERRADO

7.(CESPE/ANVISA/2016) Considerando os símbolos normalmente usados para representar os conectivos lógicos, julgue os itens seguintes, relativos a lógica proposicional e à lógica de argumentação. Nesse sentido, considere, ainda, que as proposições lógicas simples sejam representadas por letras maiúsculas.
A sentença "Alberto é advogado, pois Bruno não é arquiteto" é logicamente equivalente à sentença"Bruno é arquiteto, pois Alberto não é advogado".

Comentários:

Sejam as proposições simples:

a: "Alberto é advogado."

b: "Bruno é arquiteto."

A questão apresenta um condicional da forma "q, pois p", em que se inverte o antecedente e o consequente. A condicional original pode ser descrita por ~b->a:
~b->a: "[Alberto é advogado], pois [Bruno não é arquiteto]."
Essa condicional ~b-*a pode ser descrita por meio do conectivo tradicional "Se p, então q":

~b-»a: "Se [Bruno não é arquiteto], então [Alberto é advogado]."

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p->q
= ~q-»~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

~b-»a = ~a->~(~b)

A dupla negação de b corresponde à proposição original. Logo, temos:

~b->a = ~a->b

A proposição equivalente pode ser escrita por:

~a-»b: "Se [Alberto não é advogado], então [Bruno é arquiteto]."
Podemos passar ~a-»b da forma "Se p, então q" para a forma "q, pois p":

~a->b: "[Bruno é arquiteto], pois [Alberto não é advogado]."
Note, portanto, que a equivalência apresentada pela questão está correta.

Gabarito: CERTO.

8.(CESPE/TRT17/2013) Considerando a proposição P: "Se estiver sob pressão dos corruptores ou diante de uma oportunidade com baixo risco de ser punido, aquele funcionário público será leniente com a fraude ou dela participará", julgue o item seguinte relativo à lógica sentenciai.
A proposição P é equivalente a "Se aquele funcionário público foi leniente com a fraude ou dela participou,então esteve sob pressão dos corruptores ou diante de uma oportunidade com baixo risco de ser punido".
Comentários:

Sejam as proposições simples:

a: "O funcionário público esteve sob pressão dos corruptores."

b:" O funcionário público esteve diante de uma oportunidade com baixo risco de ser punido."

c: "O funcionário público será leniente com a fraude."

d: "O funcionário público participará da fraude."
A proposição P original pode ser descrita por (aVb)->(cVd):

(aVb)-*(cVd): "Se [(estiver sob pressão dos corruptores) ou (diante de uma oportunidade com baixo risco de ser punido)], [(aquele funcionário público será leniente com a fraude) ou (dela participará)]."
Observe que a proposição a ser avaliada pode ser descrita por (cVd)->(aVb):

(cVd)-»(aVb): "Se [(aquele funcionário público foi leniente com a fraude) ou (dela participou)],
então

[(esteve sob pressão dos corruptores) ou (diante de uma oportunidade com baixo risco de ser punido)]".
Nota-se que a assertiva simplesmente inverteu a ordem da condicional sem negar as proposições, como deveria ser feito no caso da equivalência contrapositiva, dada por p->q = ~q-»~p.
Como a troca de posição ocorreu sem se negar as parcelas, as proposições não são equivalentes.

Gabarito: ERRADO.

9.(CESPE/CEF/2014) Considerando a proposição "Se Paulo não foi ao banco, ele está sem dinheiro",
julgue o item seguinte.
A proposição em apreço equivale à proposição "Paulo foi ao banco e está sem dinheiro".
Comentários:

Sejam as proposições simples:

b: "Paulo foi ao banco."

d: "Paulo está sem dinheiro."

A proposição original pode ser descrita por uma condicional ~b -* d na forma "Se p,
q", em que se omite o
"então".

~b -» d: "Se [Paulo não foi ao banco], [ele está sem dinheiro]"

Veja que a assertiva não apresenta uma condicional como equivalente. Logo, não se deve utilizar a equivalência contrapositiva, dada por p-»q = ~q-*~p.
Uma outra equivalência fundamental que se pode utilizar com o conectivo condicional é a seguinte: p-»q =
~pVq. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:

* Nega-se o primeiro termo;

* Troca-se a condicional (-») pela disjunção inclusiva (V); e

* Mantém-se o segundo termo.

Para o caso em questão, temos:

~b —> d = ~(~b)Vd

A dupla negação de b corresponde à proposição original. Logo, ficamos com:

~b -> d = bvd

Essa proposição equivalente pode ser descrita por:

bvd: "[Paulo foi ao banco] ou [ele está sem dinheiro]."

A assertiva erra ao inserir o conectivo "e" no lugar do conectivo "ou". O gabarito,
portanto, é ERRADO.
Gabarito: ERRADO.

10.(CESPE/TRE-G0/2015) P: Se L for um triângulo retângulo em que a medida da hipotenusa seja igual a c e os catetos meçam a e b, então c2 = a2 + b2.
Julgue o item que se segue, acerca de lógica proposicional.

A proposição P será equivalente à proposição (-R) V S, desde que R e S
sejam proposições convenientemente escolhidas.
Comentários:

Pessoal, a proposição P é uma condicional, e toda a condicional pode ser transformada em uma disjunção inclusiva por meio da equivalência p->q = ~pVq. Esse conhecimento já basta para marcarmos o gabarito como CERTO, pois bastaria escolher as proposições R e S de modo conveniente.
Para melhor explicar o raciocínio, vamos definir as proposições:

R: "L é um triângulo retângulo em que a medida da hipotenusa seja igual a c e os catetos meçam a e b."
S: "c2 = a2 + b2"

A proposição P é dada por R->S:

R-»S: "Se [Lfor um triângulo retângulo em que a medida da hipotenusa seja igual a c e os catetos meçam a e b], então [c2 = a2 + b2]."
Veja que a assertiva não apresenta uma condicional como equivalente. Logo, não se deve utilizar a equivalência contrapositiva, dada por p-»q = ~q-»~p.
Uma outra equivalência fundamental que se pode utilizar com o conectivo condicional é a seguinte:
p-»q = ~pVq. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:

* Nega-se o primeiro termo;

* Troca-se a condicional {-») pela disjunção inclusiva (V); e

* Mantém-se o segundo termo.

Para o caso em questão, temos:

P = R->S = ~ RV S

Gabarito: CERTO.

ll.(CESPE/PF/2018) P: "A nomeação do novo servidor público ocorre para reposição de vacância em área essencial, ou o candidato aprovado não será nomeado".
A proposição P é logicamente equivalente à proposição: "Se não for para reposição de vacância em área essencial, então o candidato aprovado não será nomeado".
Comentários:

Sejam as proposições simples:

n: "A nomeação do novo servidor público ocorre para reposição de vacância em área essencial."

a: "O candidato aprovado será nomeado."
A proposição original P pode ser escrita por nV~a:

nV~a: "[A nomeação do novo servidor público ocorre para reposição de vacância em área essencial],
ou [o candidato aprovado não será nomeado]."
Para transformar a disjunção inclusiva em uma condicional, podemos usar a equivalência pVq =~p-»q. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Nega-se o primeiro termo;

* Troca-se a disjunção inclusiva (V) pela condicional (->); e

* Mantém-se o segundo termo.

Para o caso em questão, temos:

nV~a = ~n->~a

A condicional equivalente obtida pode ser escrita como:

~n-»~a: "Se [não for para reposição de vacância em área essencial], então [o candidato aprovado não será nomeado]."
Gabarito: CERTO.

12.(CESPE/CAM DEP/2014) C: O candidato X me dará um agrado antes da eleição ou serei atingido por uma benfeitoria que ele fizer depois de eleito.
A proposição C é equivalente à seguinte proposição: "Se o candidato X não me der um agrado antes da eleição, serei atingido por uma benfeitoria que ele fizer após ser eleito".
Comentários:

Sejam as proposições simples:

a: "O candidato X me dará um agrado antes da eleição."

b: "Serei atingido por uma benfeitoria que o candidato X fizer depois de eleito."
A proposição original C é descrita por aVb:

aVb: "[O candidato X me dará um agrado antes da eleição] ou [serei atingido por uma benfeitoria que ele fizer depois de eleito]."
Para transformar a disjunção inclusiva em uma condicional, podemos usar a equivalência pVq = ~p-»q. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Nega-se o primeiro termo;

* Troca-se a disjunção inclusiva (V) pela condicional (->); e

* Mantém-se o segundo termo.

Para o caso em questão, temos:

aVb = ~a->b

Observe que a equivalência obtida pode ser descrita por:

~a-»b: "Se [o candidato X não me der um agrado antes da eleição], então [serei atingido por uma benfeitoria que ele fizer após ser eleito]."
A questão apresentou esse condicional na forma em que se omite o "então". O gabarito, portanto, é
CERTO.
Gabarito: CERTO.

Negação da conjunção e da disjunção inclusiva (leis de De Morgan)

13.(CESPE/MDIC/2014) A negação da proposição "A Brasil Central é uma das ruas mais movimentadas do centro da cidade e lá o preço dos aluguéis é alto" está corretamente expressa por "A Brasil Central não é uma das ruas mais movimentadas do centro da cidade ou lá o preço dos aluguéis não é alto".
Comentários:

Sejam as proposições simples:

m: "A Brasil Central é uma das ruas mais movimentadas do centro da cidade."

p: "Lá (na Brasil Central) o preço dos aluguéis é alto."
A proposição original pode ser descrita por mAp:

mAp:"[A Brasil Central é uma das ruas mais movimentadas do centro da cidade] e [lá o preço dos aluguéis é alto]."
Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) =
~pV~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão,temos:

~(mAp) = ~mV~p

Logo, a negação requerida pode ser descrita por:

~mV~p: "[A Brasil Central não é uma das ruas mais movimentadas do centro da cidade] ou [lá o preço dos aluguéis não é alto]".
Gabarito: CERTO.

14. (CESPE/SEFAZ-AL/2020) A negação da proposição "Os servidores públicos que atuam nesse setor padecem e os beneficiários dos serviços prestados por esse setor padecem." é corretamente expressa por"Os servidores públicos que atuam nesse setor não padecem e os beneficiários dos serviços prestados por esse setor não padecem."
Comentários:

Sejam as proposições simples:

s: "Os servidores públicos que atuam nesse setor padecem."

b: "Os beneficiários dos serviços prestados por esse setor padecem."
A proposição original pode ser escrita pela conjunção sAb:

sAb:"[Os servidores públicos que atuam nesse setor padecem] e [os beneficiários dos serviços prestados por esse setor padecem]."
Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) =
~pv~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão,temos:

~(sAb) = ~sV~b

Logo, a negação requerida pode ser descrita por:

~sV~b: "[Os servidores públicos que atuam nesse setor não padecem] ou [os beneficiários dos serviços prestados por esse setor não padecem]."
Perceba que a negação correta apresenta o conectivo "ou", não o conectivo "e", como presente na assertiva.O gabarito, portanto, é ERRADO.

Gabarito: ERRADO.

15.(CESPE/TRE MS/2013) A negação da proposição "Crescer além de certo porte é um ótimo negócio para empresários, mas um mau negócio para o mundo" é equivalente a a) Crescer além de certo porte não é um ótimo negócio para empresários ou não é um mau negócio para o mundo.
b) Não crescer além de certo porte é um ótimo negócio para empresários, mas um mau negócio para o mundo.
c) Não crescer além de certo porte não é um ótimo negócio para empresários, mas um mau negócio para o mundo.
d) Não crescer além de certo porte não é um ótimo negócio para empresários, nem um mau negócio para o mundo.
e) Crescer além de certo porte não é um ótimo negócio para empresários, nem um mau negócio para o mundo.
Comentário:

Sejam as proposições simples:

e: "Crescer além de certo porte é um ótimo negócio para empresários."

m: "Crescer além de certo porte é um mau negócio para o mundo."

Observe que na proposição original o conectivo "mas" corresponde a uma conjunção "e".
Isso significa que a proposição original pode ser descrita por eAm:
eAm: "[Crescer além de certo porte é um ótimo negócio para empresários], mas [um mau negócio para o mundo]."
Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) =
~pv~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão,temos:

~(eAm) = ~eV~m

Logo, a negação requerida pode ser descrita por:

~eV~m: "[Crescer além de certo porte não é um ótimo negócio para empresário] ou [não é um mau negócio para o mundo]."
Gabarito: Letra A.

16.(CESPE/SEFAZ-RS/2018) A negação da proposição "O IPTU, eu pago parcelado; o IPVA, eu pago em parcela única" pode ser escrita como a) "Eu pago o IPTU em parcela única ou pago o IPVA parcelado".
b) "Eu não pago o IPTU parcelado e não pago o IPVA em parcela única".

c) "Eu não pago o IPTU parcelado e pago o IPVA parcelado".

d) "Eu não pago o IPTU parcelado ou não pago o IPVA em parcela única".

e) "Eu pago o IPTU em parcela única e pago o IPVA parcelado".

Comentários:

Sejam as proposições simples:

u: "O IPTU, eu pago parcelado."

a: "O IPVA, eu pago em parcela única."

A proposição original da questão se trata da conjunção uAa, pois significa o seguinte:

uAa: "[O IPTU, eu pago parcelado] e [o IPVA, eu pago em parcela única]."

Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) =
~pV~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão,temos:

~(uAa) = ~uV~a

Logo, a negação requerida pode ser descrita por:

"[O IPTU eu não pago parcelado] ou [o IPVA eu não pago em parcela única]."

Esse resultado corresponde a alternativa D, que apresenta uma reescrita das proposições simples sem alteração de sentido.
Gabarito: Letra D.

17.(CESPE/SERPRO/2013) A negação da proposição "O síndico troca de carro ou reforma seu apartamento"
pode ser corretamente expressa por "O síndico não troca de carro nem reforma seu apartamento".

Comentários:

Sejam as proposições simples:

k: "O síndico troca de carro"

a: "O síndico reforma seu apartamento"
A proposição original pode ser descrita por kVa:

kVa: "[O síndico troca de carro] ou [reforma seu apartamento]."

Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(pVq) =
~pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da disjunção inclusiva;

* Troca-se a disjunção inclusiva (V) pela conjunção (A).

Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão,temos:

~(kVa) E ~kA~a

Logo, a negação requerida pode ser descrita por:

~kA~a: "[O síndico não troca de carro] e [não reforma seu apartamento]."

A equivalência sugerida pelo enunciado expressa a mesma frase anterior substituindo o conectivo "e" e a negação "não" pela palavra "nem".
~kA~a: "[O síndico não troca de carro] [nem reforma seu apartamento]."

Gabarito: CERTO.

18.(CESPE/PC MA/2018) A qualidade da educação dos jovens sobe ou a sensação de segurança da sociedade diminui.
Assinale a opção que apresenta uma proposição que constitui uma negação da proposição.

a) A qualidade da educação dos jovens não sobe e a sensação de segurança da sociedade não diminui.

b) A qualidade da educação dos jovens desce ou a sensação de segurança da sociedade aumenta.

c) A qualidade da educação dos jovens não sobe ou a sensação de segurança da sociedade não diminui.

d) A qualidade da educação dos jovens sobe e a sensação de segurança da sociedade diminui.

e) A qualidade da educação dos jovens diminui ou a sensação de segurança da sociedade sobe.

Comentário:

Sejam as proposições simples:

q: "A qualidade da educação dos jovens sobe."

s: "A sensação de segurança da sociedade diminui."
A proposição composta do enunciado é dada por:

qVs: "[A qualidade da educação dos jovens sobe] ou [a sensação de segurança da sociedade diminui]."

Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(pVq) E
~pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da disjunção inclusiva;

* Troca-se a disjunção inclusiva (V) pela conjunção (A).

Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão,temos:

~qA~s: "[A qualidade da educação dos jovens não sobe] e [a sensação de segurança da sociedade não diminui]."
O gabarito, portanto, é a alternativa A.

Observação: a palavra "desce" não é a negação de "sobe", bem como a palavra "aumenta"
não é a negação de "diminui".
Gabarito: Letra A.

19. (CESPE/MEC/2014) A negação da proposição "O candidato é pós-graduado ou sabe falar inglês"
pode ser corretamente expressa por "O candidato não é pós-graduado nem sabe falar inglês".
Comentários:

Sejam as proposições simples:

p:" O candidato é pós-graduado."

i: "O candidato sabe falar inglês."

A proposição composta original pode ser descrita por pVi:

pVi: "[O candidato é pós-graduado] ou [sabe falar inglês]."

Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(pVq) =
~pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da disjunção inclusiva;

* Troca-se a disjunção inclusiva (V) pela conjunção (A).

Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão,temos:

~(pVi) = ~p A ~i

Logo, a negação pode ser descrita por:

~p A ~i: "[O candidato não é pós-graduado] e [o candidato não sabe falar inglês]."

A equivalência sugerida pelo enunciado expressa a mesma frase anterior substituindo o conectivo "e" e a negação "não" pela palavra "nem".
~p A ~i: "[O candidato não é pós-graduado] [nem sabe falar inglês]."

Gabarito: CERTO.

20.(CESPE/DETRAN-DF/2009) Considerando que A, B e C sejam proposições, que os símbolos
V e A
representam os conectivos "ou" e "e", respectivamente, e que o símbolo - denota o modificador negação,julgue o item a seguir.

A proposição (AVB)A[(--A)A(--B)] é sempre falsa.
Comentários:

Veja que, para resolver a questão, poderíamos montar a tabela-verdade e verificar que a proposição em questão é sempre falsa.
Vamos agora resolver problema de um outro modo.

Devemos avaliar se (AVB)A[(~A)A(~B)] é sempre falsa.
Aplicando De Morgan "ao contrário" em [(~A)A(~B)], temos:

[(~A)A(~B)] = [~ (AVB)]

A proposição original fica:

(AVB)A[~ (AVB)]

Note que se trata da conjunção de um termo (AVB) com a sua negação. Essa conjunção apresenta, então,dois termos com valores lógicos sempre opostos. Temos, portanto, que o valor lógico da conjunção sempre será falso, ou seja, trata-se de uma contradição.
Gabarito: CERTO.

21.(CESPE/BNB/2018) Julgue o item que se segue, a respeito de lógica proposicional.

Se P e Q forem proposições simples, então a proposição -[PV(--Q)]o[(-'P)AQ] é uma tautologia.
Comentários:

Veja que, para resolver a questão, poderíamos montar a tabela-verdade e verificar que a proposição em questão é sempre verdadeira.
Note, porém, que existe uma outra forma de se resolver o problema.
Considere a proposição do enunciado:

—[PV(~Q)J <-> [(~P)AQ]

Vamos aplicar De Morgan no lado esquerdo da bicondicional:

[(—P)A ~(~Q)J ++ [(~P)AQ]

A dupla negação de Q corresponde à própria proposição Q. Nossa bicondicional fica:

[(~P)A Q] <-> [(-P)AQ]

Temos uma bicondicional com os dois termos que sempre assumem os mesmos valores lógicos. Isso significa que a bicondicional é sempre verdadeira e, portanto, trata-se de uma tautologia.
Gabarito: CERTO.

Negação da Condicional

22.(CESPE/PETROBRAS/2022) Acerca de lógica matemática, julgue o item a seguir.

A negativa da sentença composta "Se o preço está elevado, então a compra não será realizada." é "O
preço está elevado e a compra será realizada.".
Comentários:

Sejam as proposições simples:

p: "O preço está elevado."

r: "A compra será realizada."
A proposição composta original pode ser definida pela condicional p-»~r:

p-»~r: "Se [o preço está elevado], então [a compra não será realizada]."

Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (-») pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

~(p^~r) = pA~(~r)

A dupla negação de r corresponde à proposição original. Logo, temos:

~(p^~r) = pAr

Logo, a negação pode ser descrita por:

pAr: "[O preço está elevado] e [a compra será realizada]."

Gabarito: CERTO.

23.(CESPE/TC-DF/2021) Considerando que P e Q sejam, respectivamente, as proposições "Ausência de evidência de um crime não é evidência da ausência do crime." e "Se não há evidência, não há crime.",julgue a seguir.

A negação da proposição Q pode ser corretamente expressa por "Não há evidência, mas há crime.".

Comentários:

Sejam as proposições simples:

e: "Há evidência."

c: "Há crime."

A proposição composta Q pode ser definida pela condicional ~e-»~c:

~e-»~c: "Se [não há evidência], então [não há crime]."

Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (-») pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

~(~e—>~c) = ~e A~(~c)

A dupla negação de c corresponde à proposição original. Logo, temos:

~(~e-»~c) = ~e Ac

Logo, a negação pode ser descrita por:

~e Ac: "[Não há evidência] e [há crime]."

Sabemos que a conjunção "e" pode ser representada pela palavra "mas". Logo, a negação da condicional em questão também pode ser descrita por:
~e Ac: "[Não há evidência] mas [há crime]."

Gabarito: CERTO.

24.(CESPE/DEPEN/2021) Com relação a lógica proposicional, julgue o item a seguir.

Uma tautologia é uma proposição composta em que seu valor lógico será sempre verdadeiro,independentemente do valor lógico das proposições que a estruturam. Nesse sentido,
considerando-se p e q como proposições, a proposição composta pAq<^~(p->~q) é uma tautologia.
Comentários:

Devemos verificar se a bicondicional pAq<^~(p^~q) é uma tautologia.

Observe que a segunda parcela, dada por ~(p-»~q), é a negação de uma condicional.

Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (-») pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

A dupla negação da proposição simples q corresponde à proposição original. Logo, temos:

~(p->~q) = pAq

Substituindo na bicondicional a parcela ~(p-*~q) pelo equivalente pAq, ficamos com:

pAqopAq

Sabemos que, para a bicondicional ser verdadeira, ambas as parcelas devem apresentar o mesmo valor lógico.
Como a bicondicional em questão apresenta duas parcelas iguais, então essa bicondicional sempre apresentará o mesmo valor lógico nas duas parcelas. Consequentemente, a bicondicional em questão será sempre verdadeira. Logo, é correto afirmar que a bicondicional é uma tautologia.
Gabarito: CERTO.

25. (CESPE/ANVISA/2016) Julgue o seguinte item, relativo a raciocínio lógico, a princípios de contagem e probabilidade e a operações com conjuntos.
A sentença "Se João tem problemas cardíacos, então ele toma remédios que controlam a pressão." pode ser corretamente negada pela sentença "João tem problemas cardíacos e ele não toma remédios que controlam a pressão".
Comentários:

Sejam as proposições simples:

p: "João tem problemas cardíacos."

r: "João toma remédios que controlam a pressão."
A proposição composta original pode ser definida pela condicional p->r:

p-»r: "Se [João tem problemas cardíacos], então [ele toma remédios que controlam a pressão]."

Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (-») pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

~(p—>r) = pA~r

Logo, a negação pode ser descrita por:

pA~r: "[João tem problemas cardíacos] e [não toma remédios que controlam a pressão]."

Gabarito: CERTO.

26.(CESPE/EBSERH/2018) A respeito de lógica proposicional, julgue o item que se segue.

A negação da proposição "Se o fogo for desencadeado por curto-circuito no sistema elétrico, será recomendável iniciar o combate às chamas com extintor à base de espuma." é equivalente à proposição"O fogo foi desencadeado por curto-circuito no sistema elétrico e não será recomendável iniciar o combate às chamas com extintor à base de espuma."
Comentários:

Sejam as proposições simples:

f: "O fogo é desencadeado por curto-circuito no sistema elétrico."

r: "Será recomendável iniciar o combate às chamas com extintor à base de espuma."
A proposição original cuja negação se quer obter pode ser descrita por f-»r:

f-»r: "Se [o fogo for desencadeado por curto-circuito no sistema elétrico], [será recomendável iniciar o combate às chamas com extintor à base de espuma]."
A questão quer uma equivalência da negação da proposição original, ou seja,
quer uma expressão equivalente a ~(f"*r).
Para realizar a negação de uma condicional, usa-se a equivalência ~(p^q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (-») pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

~(f-> r) = fA~r

Logo, a negação pode ser descrita por:

fA~r: "[O fogo é desencadeado por curto-circuito no sistema elétrico] e [não será recomendável iniciar o combate às chamas com extintor à base de espuma].
Gabarito: CERTO.

27.(CESPE/MPOG/2015) Considerando a proposição P: "Se João se esforçar o bastante, então
João conseguirá o que desejar", julgue o item a seguir.
A negação da proposição P pode ser corretamente expressa por "João não se esforçou o bastante, mas,mesmo assim, conseguiu o que desejava".

Comentários:

Sejam as proposições simples:

e: "João se esforçou bastante."

d: "João conseguiu o que desejava."
A proposição composta original pode ser definida pela condicional e-»d:

e-*d: "Se [João se esforçar o bastante], então [João conseguirá o que desejar]."

Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (->) pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

~(e-»d) = eA~d

Logo, a negação pode ser descrita por:

eA~d: "[João se esforçou o bastante] e [não conseguiu o que desejava]".

A negação apresentada está errada, pois corresponde a ~eAd. Observe que a expressão
"mas, mesmo assim"
corresponde à conjunção "e".

~eAd: "[João não se esforçou o bastante], mas, mesmo assim, [conseguiu o que desejava]."

Gabarito: ERRADO.

28. (CESPE/COGE-CE/2019) Pl: Se os recursos foram aplicados em finalidade diversa da prevista ou se a obra foi superfaturada, então a prestação de contas da prefeitura não foi aprovada.
Assinale a opção correspondente à proposição equivalente à negação da proposição Pl.

a) "Os recursos foram aplicados em finalidade diversa da prevista ou a obra foi superfaturada, mas a prestação de contas da prefeitura foi aprovada".
b) "Os recursos foram aplicados em finalidade diversa da prevista e a obra foi superfaturada, mas a prestação de contas da prefeitura foi aprovada".
c) "Os recursos não foram aplicados em finalidade diversa da prevista e a obra não foi superfaturada, mas a prestação de contas da prefeitura foi aprovada".
d) "Se os recursos não foram aplicados em finalidade diversa da prevista e a obra não foi superfaturada,então a prestação de contas da prefeitura foi aprovada".

e) "Se a prestação de contas da prefeitura foi aprovada, então os recursos não foram aplicados em finalidade diversa da prevista e a obra não foi superfaturada".
Comentários:

Sejam as proposições simples:

a: "Os recursos foram aplicados em finalidade diversa da prevista."

s: "A obra foi superfaturada."

p: "A prestação de contas da prefeitura não foi aprovada."
A proposição Pl pode ser descrita por (aVs)->p:

(aVs)->p: "Se [(os recursos foram aplicados em finalidade diversa da prevista) ou (se a obra foi superfaturada)], então [a prestação de contas da prefeitura não foi aprovada]."
Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional {->) pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

~[(aVs)-»p] = (aVs) A ~p

Utilizando o conectivo "mas" para representar a conjunção, temos:

(aVs) A ~p: "[(Os recursos foram aplicados em finalidade diversa da prevista) ou (a obra foi superfaturada)], mas [a prestação de contas da prefeitura foi aprovada]".
Gabarito: Letra A.

Outras equivalências e negações

29.(CESPE/PETROBRAS/2022) Acerca de lógica matemática, julgue o item a seguir.
Dadas três proposições p, q e r, tem-se que pVq-»r é equivalente a (p->r)V(q->r).

Comentários:

Na teoria da aula, aprendemos duas equivalências relacionadas à conjunção de condicionais. Para resolver essa questão, teríamos que conhecer a seguinte equivalência:
(p->r)A(q->r) = (pVq)->r

Note que a questão sugere que (pVq)->r é equivalente a (p—>r)V(q—>r). O gabarito, portanto, é
ERRADO.

Outra forma de resolver o problema sem conhecer a equivalência supracitada é desenhar as tabelas-verdade de pVq->r e de (p—>r)V(q—>r). Como as tabelas-verdade não são iguais, as proposições compostas não são equivalentes.
Gabarito: ERRADO.

30. (CESPE/TCE-RS/2013) Com base na proposição P: "Quando o cliente vai ao banco solicitar um empréstimo, ou ele aceita as regras ditadas pelo banco, ou ele não obtém o dinheiro",julgue o item que se segue.
A negação da proposição "Ou o cliente aceita as regras ditadas pelo banco, ou o cliente não obtém o dinheiro" é logicamente equivalente a "O cliente aceita as regras ditadas pelo banco se, e somente se, o cliente não obtém o dinheiro"
Comentários:

Sejam as proposições simples:

p: "O cliente aceita as regras ditadas pelo banco."

q: "O cliente não obtém o dinheiro."

A proposição a ser negada é pVq. Sabemos que a negação da disjunção exclusiva é a bicondicional:

~(pYq) = p<->q

A bicondicional pode ser descrita por:

"[O cliente aceita as regras ditadas pelo banco] se, e somente se, [o cliente não obtém o dinheiro]."
Gabarito: CERTO.

31.(CESPE/PC-CE/2012) Considere as proposições:

Pl: Se se deixa dominar pela emoção ao tomar decisões, então o policial toma decisões ruins.
P2: Se não tem informações precisas ao tomar decisões, então o policial toma decisões ruins.

A proposição formada pela conjunção de Pl e P2 é logicamente equivalente à proposição
"Se se deixa dominar pela emoção ou não tem informações precisas ao tomar decisões, então o policial toma decisões ruins".
Comentários:

Sejam as proposições simples:

d: "O policial se deixa dominar pela emoção ao tomar decisões."

t: "O policial toma decisões ruins."

i: "O policial não tem informações precisas ao tomar decisões."

Definidas as proposições, Pl pode ser definida como d-»t e P2 pode ser definida por i-»t. Logo, a conjunção de Pl e P2 pode ser descrita por:
(d—>t)A(i—>t)

Devemos, portanto, avaliar se (d—»t)A(i—>t) é equivalente a:

"Se [(se deixa dominar pela emoção) ou (não tem informações precisas ao tomar decisões)], então [o policial toma decisões ruins]".
Isto é, devemos avaliar se (d->t)A(i-»t) é equivalente a (dvi)—>t. Sabemos que ambas as proposições são equivalentes, pois correspondem à seguinte equivalência:
(p-»r)A(q->r) = (pVq)->r

Caso você não se lembre dessa equivalência na hora da prova, não se esqueça que
SEMPRE podemos recorrer à tabela-verdade para verificar se duas proposições são equivalentes.
Veja que ambas as proposições apresentam a mesma tabela-verdade e, portanto, são equivalentes.

Gabarito: CERTO.

32.(CESPE/PRF/2012) Um jovem, visando ganhar um novo smartphone no dia das crianças,
apresentou à sua mãe a seguinte argumentação: "Mãe, se tenho 25 anos, moro com você e papai, dou despesas a vocês e dependo de mesada, então eu não ajo como um homem da minha idade. Se estou há 7 anos na faculdade e não tenho capacidade para assumir minhas responsabilidades, então não tenho um mínimo de maturidade. Se não ajo como um homem da minha idade, sou tratado como criança. Se não tenho um mínimo de maturidade, sou tratado como criança. Logo, se sou tratado como criança,mereço ganhar um novo smartphone no dia das crianças".
Com base nessa argumentação, julgue o item a seguir.

A proposição "Se não ajo como um homem da minha idade, sou tratado como criança, e se não tenho um mínimo de maturidade, sou tratado como criança" é equivalente a "Se não ajo como um homem da minha idade ou não tenho um mínimo de maturidade, sou tratado como criança"
Comentários:

Primeiro vamos definir as proposições:

a: "Não ajo como um homem da minha idade."

k: "Sou tratado como criança."

m: "Não tenho um mínimo de maturidade."

Note que a questão pergunta se (a-»k)A(m-»k) é equivalente a (aVm)-»k.
Sabemos que ambas as proposições são equivalentes, pois correspondem à seguinte equivalência:
(p-»r)A(q->r) = (pVq)->r

Caso você não se lembre dessa equivalência na hora da prova, não se esqueça que
SEMPRE podemos recorrer à tabela-verdade para verificar se duas proposições são equivalentes.
Gabarito: CERTO.

Questões com mais de uma equivalência

33.(CESPE/DEPEN/2021) Com relação a lógica proposicional, julgue o item a seguir.

Considere as seguintes proposições p: "Paola é feliz";
q: "Paola pinta um quadro".

Assim, a proposição "Paola é feliz apenas se ela pinta um quadro" pode ser representada por ~(pA~q).
Comentários:

Sabemos que o conectivo "somente se" é do tipo condicional. Esse conectivo difere do
"se e somente se",

que é do tipo bicondicional.

Note que a proposição sugerida pelo enunciado é:

"[Paola é feliz] apenas se [ela pinta um quadro]"

O conectivo "apenas se" apresentado na questão corresponde ao condicional
"somente se". Logo, a proposição pode ser descrita por p->q.
Veja que o enunciado sugere que a proposição composta pode ser representada por ~(pA~q). Podemos desenvolver essa negação por De Morgan. Para negar a conjunção "e", negam-se ambas as parcelas e troca-se o "e" pelo "ou". Ficamos com:

~(pA~q) = ~p V ~(~q)

A dupla negação de uma proposição simples corresponde à proposição original. Logo:

~(pA~q) = ~pVq

Nesse momento, você deve se lembrar da equivalência conhecida por
"transformação do condicional em disjunção inclusiva", dada por p->q = ~pVq.
Conhecendo essa equivalência, observe que ~(pA~q) é equivalente a ~pVq que, por sua vez, é equivalente a p->q. Portanto:
~(pA~q) E= p—>q

Isso significa que a proposição p->q, "Paola é feliz apenas se ela pinta um quadro", de fato pode ser representada por sua forma equivalente ~(pA~q). O gabarito, portanto, é CERTO.
Gabarito: CERTO.

34.(CESPE/PC DF/2021) A proposição "Se Marcos é culpado, então Paulo ou Carlos são inocentes."
equivale à proposição "Se Paulo ou Carlos são culpados, então Marcos é inocente.".
Comentários:

Nessa questão, a banca utilizou "é inocente" como forma de se negar "é culpado".
Sabemos que a utilização de antônimos deve ser evitada, pois muitas vezes esse tipo de negação não abarca todas as possibilidades.Ocorre que o CESPE não costuma entrar nesse nível de detalhe, especialmente em questões envolvendo equivalências lógicas ou lógica de argumentação. Portanto, nesse tipo de questão, via de regra você pode negar usando antônimos.
Considere as seguintes proposições simples:

m: "Marcos é inocente."
p: "Paulo é inocente."
c: "Carlos é inocente."

Vamos considerar que a negação dessas proposições simples são, respectivamente:

~m: "Marcos é culpado."

~p: "Paulo é culpado."

~c: "Carlos é culpado."

Note que a proposição original pode ser descrita por ~m-»pVc, pois pode ser escrita da seguinte maneira:
~m-»pVc: "Se [Marcos é culpado], então [(Paulo é inocente) ou (Carlos é inocente)]."

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-*q
E ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

~m->pVc = ~(pVc)-»~(~m)

A dupla negação de m corresponde à proposição original. Ficamos com:

~m->pVc E ~(pVc)->m

~(pVc) pode ser desenvolvida por De Morgan, correspondendo a ~pA~c. Ficamos com:

~m->pVc E ~pA~c ->m

Logo, temos a seguinte equivalência:

~pA~c -»m: "Se [(Paulo é culpado) e (Carlos é culpado)], então [Marcos é inocente]."
Essa proposição equivalente pode ser entendida da seguinte forma:

"Se [Paulo e Carlos são culpados], então [Marcos é inocente]."

Note que a assertiva está errada, pois ela apresenta a disjunção inclusiva
"ou" no antecedente da condicional, quando deveria apresentar a conjunção "e".
"Se [Paulo ou Carlos são culpados], então [Marcos é inocente]"

Gabarito: ERRADO.

35. (CESPE/CBM AL/2017) A respeito de proposições lógicas, julgue o item a seguir.
Considere que P e Q sejam as seguintes proposições:

P: Se a humanidade não diminuir a produção de material plástico ou não encontrar uma solução para o problema do lixo desse material, então o acúmulo de plástico no meio ambiente irá degradar a vida no planeta.
Q: A humanidade diminui a produção de material plástico e encontra uma solução para o problema do lixo desse material ou o acúmulo de plástico no meio ambiente degradará a vida no planeta.
Nesse caso, é correto afirmar que as proposições P e Q são equivalentes.
Comentários:

Sejam as proposições simples:

d: "A humanidade diminui a produção de material plástico."

s: "A humanidade encontra solução para o problema do lixo desse material."

a: "O acúmulo de plástico no meio ambiente degrada a vida no planeta."
A proposição P pode ser descrita por (~d V~s)-»a:

(~d V~s)-»a: "Se [(a humanidade não diminuir a produção de material plástico) ou (não encontrar uma solução para o problema do lixo desse material)], então [o acúmulo de plástico no meio ambiente irá degradar a vida no planeta].
A segunda proposição pode ser descrita por (d A s) V a:

(d A s) V a: "[A humanidade diminui a produção de material plástico] e [encontra uma solução para o problema do lixo desse material] ou [o acúmulo de plástico no meio ambiente degradará a vida no planeta]."
Devemos verificar se (~d V~s)-»a é equivalente a (d A s) V a.

Perceba que a primeira proposição é uma condicional e a segunda é uma disjunção inclusiva de (d A s) com a. Logo, não devemos usar a equivalência contrapositiva para a primeira proposição.
Uma equivalência fundamental que se pode utilizar com o conectivo condicional é a seguinte:
p-»q = ~pVq. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:

* Nega-se o primeiro termo;

* Troca-se a condicional (-») pela disjunção inclusiva (V); e

* Mantém-se o segundo termo.

Para o caso em questão, temos:

(~d V~s)—> a = (~d V~s) V a

Aplicando De Morgan para o termo ~(~d V~s ), temos:

(~d V~s )-» a = (~(~d )A~(~s )) V a

A dupla negação de uma proposição simples corresponde à proposição não negada. Logo:

(~d V~s)-> a = (d A s ) V a

Veja, portanto, que as proposições P e Qsão equivalentes.

Gabarito: CERTO.

36.(CESPE/PGE-PE/2019) Acerca da lógica sentenciai, julgue o item que se segue.

Se P, Q, R e S forem proposições simples, então as proposições PVR->QAS e
(~Q)V(~S)->(~P)A(~R) serão equivalentes
Comentários:

A questão pede a equivalência entre duas condicionais. Podemos então utilizar a equivalência contrapositiva em PVR->QAS. Para tanto, devemos negar ambas as parcelas e trocar de posição o antecedente com o consequente.
PVR->QAS = ~ (QAS)—> ~(PVR)

Aplicando De Morgan para ambos os lados da nova condicional obtida, obtemos:

PVR->QAS = (~Q)V(~S)-> (~P)A(~R)

Veja que, a partir de PVR->QAS, obtemos (~Q)V(~S)-»(~P)A(~R). Logo, essas proposições são equivalentes.
Gabarito: CERTO.

37. (CESPE/SERPRO/2013) Considerando que o símbolo lógico A corresponda à conjunção
"e"; V, à disjunção "ou"; —à condicional "se..., então"; <->, à bicondicional "se, e somente se";~ corresponda à negação "não"; P, Q e R sejam proposições simples; e S seja a seguinte proposição composta:[PA~(QVR)j—► [RA(P«->Q)j, julgue o próximo item.

A negação de S —S - pode ser corretamente expressa por [~PV(QVR)]A[(~R)V~(P<->Q)1-
Comentários:

A proposição S é dada por [PA~(QVR)J—>[RA(P«->Q)]. A pergunta pede a negação de S.

Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (->) pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

[PA-(QVR)] A ~[RA(P< >Q)]

O segundo termo é a negação de uma conjunção. Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) = ~pV~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Ficamos com:

[PA-(QVR)] A [(~R) V ~(P< >Q)]

Acabamos de obter a negação de S. Observe a negação sugerida pela assertiva:

[~PV(QVR)J A [(~R)V~(P<->Q)]

Podemos observar que a negação sugerida está errada, pois o primeiro termo, dado por
[~PV(QVR)j, é a negação de [PA~(QVR)j.
Gabarito: ERRADO.

38. (CESPE/TCE-ES/2012) Proposições são sentenças que podem ser julgadas como verdadeiras — V — ou falsas — F —, de forma que um julgamento exclui o outro, e são simbolizadas por letras maiusculas,como
P, Q, R e S. A partir de proposições conhecidas, novas proposições podem ser construídas usando-se símbolos especiais. Alguns desses símbolos são apresentados na tabela abaixo.
símbolo

A
V

—>

nome negação conjunção disjunção condicional notação
-p
PAQ
PVQ
P—>Q

leitura não PPeQ

P ou Q

se P, então Q

valor contrário ao de P: V, se P for F; ou F, se P forVV, se P e Q forem V; caso contrário, será F

F, se P e Q forem F; caso contrário, será V
F, se P for V e Q for F; caso contrário, será V

<—>

bicondicional

P<->Q

P se, e somente se, Q V, se P e Q tiverem os mesmos valores; caso contrário, será F

Considerando as definições acima e a proposição {(PVQ)—>[RA(~S)]}V[(PAS)< >(QAR)], julgue o item a seguir.
Essa proposição é logicamente equivalente à proposição {[(~R)VS]_>[( ~P)A(~Q)]}V[(PAS)< >(QAR)J.
Comentários:

Em um primeiro momento a questão parece ser mais difícil do que realmente é por conta do excesso do uso de parênteses, colchetes e chaves. Uma vez que conhecemos a ordem de precedência dos conectivos,podemos reescrever a primeira e a segunda proposição da seguinte maneira:

Primeira: (PVQ -» RA~S)V(PAS «-> QAR)

Segunda: (~RVS ->~PA~Q)V(PAS«->QAR)

Observe que o termo da direita da disjunção inclusiva "ou", dado por (PAS^QAR), é o mesmo para ambas as proposições.
Desse modo, para demonstrar a equivalência, vamos desenvolver o termo da esquerda (PVQ
-> RA~S) da primeira proposição e chegar no termo (~RVS PA—Q).
A equivalência clássica que envolve duas condicionais é a contrapositiva: p-*q
= ~q-»~p. Aplicando em

(PVQ -»RA~S), temos:

~ (RA~S) -> ~ (PVQ)

Utilizando as equivalências de De Morgan para os dois termos da condicional acima, temos:

~ R V~(~S) -> ~ PA~Q

A dupla negação~(~S) é equivalente a S. Ficamos com:

~ R V S —» ~ PA~Q

Finalmente, podemos constatar que os termos da esquerda de ambas as proposições são equivalentes e os termos da direita são iguais. Logo, as proposições são equivalentes.
Gabarito: CERTO.

39. (CESPE/SEFAZ-ES/2010) Considerando os símbolos lógicos - (negação), A (conjunção), V
(disjunção), ->
(condicional) e as proposições julgue o item que se segue.
S:(pA--q)V(-'pAr)-»qVr e
T :{{pA--q)V(--pAr))A(--qA--r)

As proposições compostas --S e T são equivalentes, ou seja, têm a mesma tabela-verdade,independentemente dos valores lógicos das proposições simples p, q, e r que as constituem.

Comentários:

Em um primeiro momento a questão parece ser complicada. Porém, se observarmos mais atentamente,podemos ver que parte das proposições S e T são iguais:

S:(pA~q)V(~pAr)->qVr

T :{{pA~q)V(~pAr))A(~qA~r)

Note que S é uma condicional em que o antecedente é (pA~q)V(~pAr). Vamos negar S,
como pede o enunciado, por meio da equivalência ~(p-> q) = pA~ q:
((pA~q)V(~pAr))A(~(qVr))

Podemos desenvolver ~(qVr) por De Morgan. A expressão de ~ S fica:

((pA~q)V(~pAr))A( ~qA~r)

Observe que, ao desenvolver ~ S, chegamos à proposição T. Logo, essas proposições são equivalentes.
Gabarito: CERTO.

Questões com mais de um item

Texto para as próximas questões

Considere as proposições lógicas P e Q, a seguir, a respeito de um condômino chamado Marcos.

P: "Se Marcos figura no quadro de associados e está com os pagamentos em dia, então ele tem direito a receber os benefícios providos pela associação de moradores de seu condomínio."-
Q: "Marcos não figura no quadro de associados, mas ele está com os pagamentos em dia."
Tendo como referência essas proposições, julgue os itens a seguir.

40. (CESPE/SEFAZ AL/2021) Considerando-se verdadeira a proposição P, é correto concluir que, se
Marcos não tem direito a receber os benefícios providos pela associação de moradores de seu condomínio,então,
necessariamente, ele não figura no quadro de associados nem está com os pagamentos em dia.

41. (CESPE/SEFAZ AL/2021) A proposição P é equivalente à proposição "Se Marcos não figura no quadro de associados ou não está com os pagamentos em dia, então ele não tem direito a receber os benefícios providos pela associação de moradores de seu condomínio.".
42. (CESPE/SEFAZ AL/2021) A proposição P é equivalente à proposição "Se Marcos tem direito a receber os benefícios providos pela associação de moradores de seu condomínio, então ele figura no quadro de associados e está com os pagamentos em dia.".
43. (CESPE/SEFAZ AL/2021) A proposição Q é uma negação da proposição "Se Marcos está com os pagamentos em dia, então ele figura no quadro de associados.".
Comentários:

Considere as seguintes proposições simples:

a: "Marcos figura no quadro de associados."

d: "Marcos está com os pagamentos em dia."

b: "Marcos tem direito a receber os benefícios providos pela associação de moradores de seu condomínio."Note que a proposição composta P pode ser descrita por aAd-»b.

aAd-»b: "Se [(Marcos figura no quadro de associados) e (está com os pagamentos em dia)], então [ele tem direito a receber os benefícios providos pela associação de moradores de seu condomínio]."
Além disso, a proposição composta Q é uma conjunção representada pela palavra
"mas", podendo ser descrita por ~aAd.
~aAd: "[Marcos não figura no quadro de associados], mas [ele está com os pagamentos em dia]."
Feitas essas observações, vamos avaliar os itens da questão.

Questão 40

Sabemos que a proposição composta P pode ser descrita por aAd-»b.

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p->q
= ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

aAd->b = ~b->~(aAd)

~(aAd) pode ser desenvolvida por De Morgan, correspondendo a ~aV~d. Ficamos com:

aAd-»b = ~b->~aV~d

Logo, considerando verdadeira a proposição P, é correto afirmar que:

~b-*~aV~d: "Se [Marcos não tem direito a receber os benefícios providos pela associação de moradores de seu condomínio], então [(ele não figura no quadro de associados) ou (não está com os pagamentos em dia)]."
Veja que o item da questão traz como equivalente à proposição P a seguinte proposição composta:
[Marcos não tem direito a receber os benefícios providos pela associação de moradores de seu condomínio], então, necessariamente, [(ele não figura no quadro de associados) (nem está com os pagamentos em dia)]
No item, temos uma condicional em que o consequente apresenta uma conjunção, pois
"nem" corresponde a "e não". Veja que essa condicional apresentada no item corresponde a ~b-»~aA~d, que é diferente da proposição equivalente ~b-»~aV~d.
~b-»~aA~d: "Se [Marcos não tem direito a receber os benefícios providos pela associação de moradores de seu condomínio], então [(ele não figura no quadro de associados) e (não está com os pagamentos em dia)]."
O gabarito, portanto, é ERRADO.

Questão 41

Sabemos que a proposição composta P pode ser descrita por aAd->b.

Note que o item apresenta como supostamente equivalente a P a proposição composta ~aV~d-»~b:

~aV~d-»~b: "Se [(Marcos não figura no quadro de associados) ou (não está com os pagamentos em dia)],
então [ele não tem direito a receber os benefícios providos pela associação de moradores de seu condomínio]."
Veja que ~aV~d-»~b não é equivalente a aAd->b, pois nesse caso negou-se o antecedente e o consequente sem invertê-los de posição. A equivalência seria corretamente executada se fosse utilizada a contrapositiva,em que:

* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

O gabarito, portanto, é ERRADO.

Questão 42

Sabemos que a proposição composta P pode ser descrita por aAd-*b.

Note que o item apresenta como equivalente a P a seguinte proposição composta b->aAd:

b-»aAd: "Se [Marcos tem direito a receber os benefícios providos pela associação de moradores de seu condomínio], então [(ele figura no quadro de associados) e (está com os pagamentos em dia)."
Veja que b-*aAd não é equivalente a aAd->b, pois nesse caso inverteu-se o antecedente e o consequente de posição sem negar ambas as parcelas. A equivalência seria corretamente executada se fosse utilizada a contrapositiva, em que:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

O gabarito, portanto, é ERRADO.

Questão 43

Sabemos que a proposição composta Q pode ser descrita por ~aAd. O item apresenta uma condicional como correspondente à negação de Q.
Para transformar a negação de uma conjunção para a condicional, podemos utilizar a seguinte equivalência:
~{pAq) = p->~q

Para realizar essa equivalência, note que:

* O primeiro termo da condicional é o primeiro termo da conjunção a ser negada;

* O segundo termo da condicional é a negação do segundo termo da conjunção.

Para o caso em questão, temos que a negação de ~aAd, dada por ~{~aAd), é:

~(~aAd) = ~a—»~d

Logo, a negação da proposição composta Q pode ser descrita por:

~a-»~d: "Se [Marcos não figura no quadro de associados], então [Marcos não está com os pagamentos em dia].
Aplicando a equivalência contrapositiva em ~a-»~d, obtemos d-»a, que é a equivalência apresentada no item:
d-»a: "Se [Marcos está com os pagamentos em dia], então [ele figura no quadro de associados]".
O gabarito, portanto, é CERTO.

Gabarito: 40 - ERRADO. 41 - ERRADO. 42 - ERRADO. 43 - CERTO.

Texto para as próximas questões

: Pl: Se a fiscalização foi deficiente, as falhas construtivas não foram corrigidas.

= P2: Se as falhas construtivas foram corrigidas, os mutuários não tiveram prejuízos.

: P3: A fiscalização foi deficiente.

= C: Os mutuários tiveram prejuízos.

: Considerando um argumento formado pelas proposições precedentes, em que C é a conclusão, e Pl a P3 são
= as premissas, julgue os itens a seguir.

44. (CESPE/PF/2021) A proposição Pl é equivalente a "Não é verdade que a fiscalização foi deficiente e que as falhas construtivas foram corrigidas".
45. (CESPE/PF/2021) Uma negação correta da proposição Pl pode ser expressa por: "Se a fiscalização não foi deficiente, as falhas construtivas foram corrigidas".
46.(CESPE/PF/2021) A proposição P2 é equivalente a "Se as falhas construtivas não foram corrigidas, os mutuários tiveram prejuízos".
Comentários:

Considere as seguintes proposições simples:

d: "A fiscalização foi deficiente."

c: "As falhas construtivas foram corrigidas."

p: "Os mutuários tiveram prejuízos."

Note que a proposição Pl corresponde à condicional d-»~c escrita na forma em que se omite o "então":d-»~c: "Se [a fiscalização foi deficiente], [as falhas construtivas não foram corrigidas]."

Além disso, a proposição P2 corresponde à condicional c-»~p escrita na forma em que se omite o
"então":
c->~p: "Se [as falhas construtivas foram corrigidas], [os mutuários não tiveram prejuízos]."

Feitas essas observações, vamos avaliar os itens da questão.

Questão 44

Note que o item apresenta a proposição ~(dAc) como equivalente à proposição Pl.

~(dAc): Não é verdade que [(a fiscalização foi deficiente) e (que as falhas construtivas foram corrigidas)]
Para transformar a negação de uma conjunção para a condicional, podemos utilizar a seguinte equivalência:
~(pAq) = p->~q

Para realizar essa equivalência, note que:

* O primeiro termo da condicional é o primeiro termo da conjunção a ser negada;

* O segundo termo da condicional é a negação do segundo termo da conjunção.

Para o caso em questão, temos que a negação de dAc, dada por ~(dAc), é:

~(dAc) = d-»~c

Logo, a proposição composta apresentada no item, dada por ~(dAc), é equivalente a Pl,
que é dada por d->~c.
O gabarito, portanto, é CERTO.

Questão 45

Note que o item apresenta a proposição ~d-»c como se fosse a negação da proposição Pl.

~d-»c: "Se [a fiscalização não foi deficiente], [as falhas construtivas foram corrigidas]."

Já vimos que Pl é dada por d-»~c. Observe, então, que a assertiva simplesmente negou ambas as parcelas da condicional original.
Sabemos que, na verdade, a negação de uma condicional é uma conjunção,
expressa pela seguinte equivalência: p-*q = pA~q. Para o caso em questão, a negação de Pl é dada por:
~(d->~c) = dA~(~c)

A dupla negação em c corresponde à proposição original, de modo que a negação de Pl é dada por:

~(d-»~c) = dAc

Logo, a negação correta é:

dAc: "(A fiscalização foi deficiente) e (as falhas construtivas foram corrigidas)"
O gabarito, portanto, é ERRADO.

Questão 46

Vimos que P2 é dada por c->~p.

Note que o item apresenta a proposição ~c-»p como se fosse equivalente à proposição P2.

~c-»p: "Se [as falhas construtivas não foram corrigidas], [os mutuários tiveram prejuízos]."

Veja que ~c-»p não é equivalente a c-»~p, pois nesse caso negou-se o antecedente e o consequente sem invertê-los de posição. A equivalência seria corretamente executada se fosse utilizada a contrapositiva, em que:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

O gabarito, portanto, é ERRADO.

Gabarito: 44 - CERTO. 45 - ERRADO. 46 - ERRADO.

Texto para as próximas questões

I

: Julgue os seguintes itens, considerando a proposição P: "Se o responsável pela indicação fizer sua parte e j
: seus aliados trabalharem duro, vencerão.".
;

47. (CESPE/MJSP/2021) A proposição P é equivalente a "Se não vencermos, o responsável pela indicação não terá feito sua parte ou seus aliados não terão trabalhado duro.".
48. (CESPE/MJSP/2021) A negação da proposição P pode ser expressa por "Se o responsável pela indicação não fizer sua parte ou seus aliados não trabalharem duro, não vencerão.".
Comentários:

Considere as seguintes proposições simples:

f: "O responsável pela indicação faz sua parte."

d: "Os aliados (do responsável pela indicação) trabalharam duro."

v: "(Eles) vencerão."

Note que a proposição P pode ser descrita pela condicional fAa->v na forma em que se omite o
"então".

fAa-»v: "Se [(o responsável pela indicação fizer sua parte) e (seus aliados trabalharem duro)],
[vencerão]."
Feitas essas observações, vamos avaliar os itens da questão.

Questão 47

Note que o item apresenta a proposição ~v-»~f V~a como equivalente à proposição P.

V~a: "Se [não vencermos], [(o responsável pela indicação não terá feito sua parte) ou (seus aliados não terão trabalhado duro)]."
Sabemos que equivalência fundamental envolvendo o conectivo condicional é a contrapositiva:p-»q = ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:

* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos que a proposição P é equivalente a:

fAa-»v = ~v-»~(fAa)

~(fAa) pode ser desenvolvida por De Morgan, correspondendo a ~f V~a. Ficamos com:

fAa->v = ~v->~f V~a

Logo, a proposição P, dada por fAa-»v, de fato é equivalente à proposição sugerida na assertiva, dada por
V~a. O gabarito, portanto, é CERTO.

Questão 48

Note que o item apresenta a proposição ~f V~a-»~v como sendo a negação de P.

~f V~a-»~v: Se [(o responsável pela indicação não fizer sua parte) ou (seus aliados não trabalharem duro)], [não vencerão]."
Já vimos que P é dada por fAa->v. Observe, então, que a assertiva simplesmente negou ambas as parcelas da condicional original, sendo a negação do antecedente, ~{fAa), negado por De Morgan,correspondendo a ~f V~a.
Sabemos que, na verdade, a negação de uma condicional é uma conjunção,
expressa pela seguinte equivalência: p-*q = pA~q. Para o caso em questão, a negação de P é dada por:
~{fAa-»v) = (fAa)A~v

Logo, a negação correta é:

(fAa)A~v: "(O responsável pela indicação faz sua parte) e (seus aliados trabalharam duro) e (não vencerão)"
O gabarito, portanto, é ERRADO.
Gabarito: 47 - CERTO. 48 - ERRADO.

Texto para as próximas questões

I

: Considerando a proposição P: "Se o servidor gosta do que faz, então o cidadão-cliente fica satisfeito", julgue =
= os itens a seguir.
;

49. (CESPE/SEFAZ DF/2020) A proposição P é logicamente equivalente à seguinte proposição: "Se o cidadão-cliente não fica satisfeito, então o servidor não gosta do que faz".
50. (CESPE/SEFAZ DF/2020) A proposição "O servidor não gosta do que faz, ou o cidadão-cliente não fica satisfeito" é uma maneira correta de negar a proposição P.
Comentários:

Sejam as proposições simples:

g: "O servidor gosta do que faz."

s:" O cidadão-cliente fica satisfeito."
A proposição composta P pode ser definida pela condicional g->s:

g-»s:"Se [o servidor gosta do que faz], então [o cidadão-cliente fica satisfeito]."
Vamos agora verificar as assertivas.

Questão 49

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p-»q
= ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

g->s = ~s-»~g

A proposição equivalente pode ser escrita por:

~s->~g:" Se [o cidadão-cliente não fica satisfeito], então [o servidor não gosta do que faz]."

O gabarito, portanto, é CERTO.

Questão 50

Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (-») pela conjunção (A); e

* Nega-se o segundo termo.

Para o caso em questão, temos:

(g->s) = gA~s

Logo, a negação pode ser descrita por:

gA~s: "[O servidor gosta do que faz] e [o cidadão-cliente não fica satisfeito]."
O gabarito, portanto, é ERRADO.

Gabarito: 49 - CERTO. 50 - ERRADO.

Texto para as próximas questões

= Considerando a proposição P: "Se João se esforçar o bastante, então João conseguirá o que desejar", julgue
: os itens a seguir.

51. (CESPE/MPOG/2015) A proposição "João não se esforça o bastante ou João conseguirá o que desejar"
é logicamente equivalente à proposição P.

52. (CESPE/MPOG/2015) A proposição "Se João não conseguiu o que desejava, então João não se esforçou o bastante" é logicamente equivalente à proposição P.
Comentários:

Sejam as proposições simples:

e: "João se esforça o bastante."

d: "João consegue o que deseja."
A proposição composta P pode ser definida pela condicional e-»d:

e-»d:"Se [João se esforçar o bastante], então [João conseguirá o que desejar]."
Vamos agora verificar as assertivas.

Questão 51

Veja que a assertiva não apresenta uma condicional como equivalente. Logo, não se deve utilizar a equivalência contrapositiva, dada por p-»q = ~q->~p.
Uma outra equivalência fundamental que se pode utilizar com o conectivo condicional é a seguinte:
p-»q = ~pVq. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:

* Nega-se o primeiro termo;

* Troca-se a condicional (-») pela disjunção inclusiva (V); e

* Mantém-se o segundo termo.

Para o caso em questão, temos:

e->d = ~eVd

Essa proposição equivalente pode ser descrita por:

~eVd: "[João não se esforça o bastante] ou [João conseguirá o que desejar]."
O gabarito, portanto, é CERTO.

Questão 52

Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p->q
= ~q->~p. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

e->d = ~d -»~e

A proposição equivalente pode ser escrita por:

~d ->~e:" Se [João não conseguiu o que desejava], então [João não se esforçou o bastante]."

Gabarito: 51 - CERTO. 52 - CERTO.

.

Texto para as próximas questões i Julgue os itens, considerando a proposição P a seguir.;

: P: "O bom jornalista não faz reportagem em benefício próprio nem deixa de fazer aquela que prejudique j
= seus interesses".

53. (CESPE/PF/2O18) A proposição P é logicamente equivalente à proposição: "Não é verdade que o bom jornalista faça reportagem em benefício próprio ou que deixe de fazer aquela que prejudique seus interesses".
54. (CESPE/PF/2018) A negação da proposição P está corretamente expressa por: "O bom jornalista faz reportagem em benefício próprio e deixa de fazer aquela que não prejudique seus interesses".
55. (CESPE/PF/2018) A negação da proposição P está corretamente expressa por: "Se o bom jornalista não faz reportagem em benefício próprio, então ele deixa de fazer aquela reportagem que prejudica seus interesses".
Comentários:

Sejam as proposições simples:

r: "O bom jornalista faz reportagem em benefício próprio."

p: "O bom jornalista deixa de fazer aquela que prejudique seus interesses."
Observe que "nem" corresponde a "e não". A proposição original P pode ser descrita por ~rA~p:

~rA~p: "[O bom jornalista não faz reportagem em benefício próprio] e [não deixa de fazer aquela que prejudique seus interesses]".
Vamos agora verificar as assertivas.

Questão 53

Veja que nova proposição apresentada pode ser descrita por ~ (rV p), uma vez que o termo "não é verdade que" nega a proposição composta como um todo:
~ (rV p): "Não é verdade que [(o bom jornalista faça reportagem em benefício próprio) ou (que deixe de fazer aquela que prejudique seus interesses)]."
Por De Morgan, conhecemos a equivalência ~(pVq) = ~pA~q. Aplicando essa equivalência ao caso, observe que as duas proposições compostas são equivalentes:
~(rV p) = ~rA~p

O gabarito, portanto, é CERTO.

Questão 54

A assertiva pede a negação de

Para realizar a negação de uma conjunção, usa-se a equivalência ~(pAq) E
~pv~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão,temos:

~rA~p = ~(~r)V~(~p)

A dupla negação corresponde à proposição original. Ficamos com:

~rA~p = rVp

Logo, a negação requerida pode ser descrita por:

rVp: "[O bom jornalista faz reportagem em benefício próprio] ou [deixa de fazer aquela que prejudique seus interesses]."
Perceba que a questão apresenta a negação de ~rA~p como rA~p ao invés de rVp.

rA~p: "[O bom jornalista faz reportagem em benefício próprio] e [deixa de fazer aquela que não prejudique seus interesses]."
O gabarito, portanto, é ERRADO.

Questão 55

A questão pede a negação de ~rA~p e pergunta se essa negação é uma determinada condicional. Para tanto,podemos utilizar a seguinte equivalência: ~(pAq) = p->~q. Para o caso em questão, temos:

~((~r)A(~p)) E (~r) -> ~(~q)

A dupla negação de uma proposição simples corresponde à proposição original.
Logo, a negação de

(~r)A(~p)é:

(~r) -> q

Em português, (~r) -» q corresponde à negação apresentada:

(~r) -> q: "Se [o bom jornalista não faz reportagem em benefício próprio], então [ele deixa de fazer aquela reportagem que prejudica seus interesses]."
O gabarito, portanto, é CERTO.

Gabarito: 53 - CERTO. 54 - ERRADO. 55 - CERTO.

*
* .

Texto para as próximas questões

: Considere a proposição P a seguir.
:

: P: Se não condenarmos a corrupção por ser imoral ou não a condenarmos por corroer a legitimidade da ;
; democracia, a condenaremos por motivos econômicos.
;

Ê Tendo como referência a proposição apresentada, julgue os itens seguintes.
;

56. (CESPE/TC-DF/2014) A proposição P é logicamente equivalente à proposição "Se não condenarmos a corrupção por motivos econômicos, a condenaremos por ser imoral e por corroer a legitimidade da democracia".
57. (CESPE/TC-DF/2014) A proposição P é logicamente equivalente à proposição
"Condenaremos a corrupção por ser imoral ou por corroer a legitimidade da democracia ou por motivos econômicos".
Comentários:

Sejam as proposições simples:

i: "Condenamos a corrupção por ser imoral"

d: "Condenamos a corrupção por corroer a legitimidade da democracia."

e: "Condenaremos a corrupção por motivos econômicos."

A proposição composta P é uma condicional escrita na forma na forma "Se p, q", em que se omite o "então".Em linguagem proposicional, podemos descrever P por (~i V~d) ->e.

(~i v~d) -»e: "Se [(não condenarmos a corrupção por ser imoral) ou (não a condenarmos por corroer a legitimidade da democracia)], [a condenaremos por motivos econômicos]."
Vamos agora verificar as assertivas.

Questão 56

Observe que a questão pede uma proposição equivalente à condicional (~i V~d) -»e e nos apresenta uma nova condicional para avaliarmos. Devemos, então, utilizar a equivalência contrapositiva p->q = ~q->~p.Para aplicar essa equivalência, devemos realizar o seguinte procedimento:

* Invertem-se as posições do antecedente e do consequente; e

* Negam-se ambos os termos da condicional.

Para o caso em questão, temos:

(~i V~d) -»e = ~e -» ~(~i V~d)

Podemos aplicar De Morgan no consequente da nova condicional obtida. Ficamos com:

~e -» ~(~i) A~(~d)

A dupla negação de uma proposição corresponde a proposição original. Logo:

~e —> i A d

Essa proposição equivalente obtida pode ser escrita como:

~e —> i A d: "Se [não condenarmos a corrupção por motivos econômicos], [(a condenaremos por ser imoral) e (por corroer a legitimidade da democracia)]."
O gabarito, portanto, é CERTO.

Questão 57

Observe que a questão pede uma proposição equivalente à condicional (~i V~d) -*e e nos apresenta uma disjunção inclusiva para avaliarmos. Nesse caso, vamos utilizar a equivalência p-»q E~pvq. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Nega-se o primeiro termo;

* Troca-se a condicional {->) pela disjunção inclusiva (V); e

* Mantém-se o segundo termo.

Para o caso em questão, temos:

(~i V~d) —>e = ~(~i v~d) V e

Podemos ainda desenvolver ~(~i V~d) por De Morgan:

(~i v~d) ->e =[~ (~i) A~ (-d)jve

A dupla negação de uma proposição corresponde à proposição original. Logo:

(~i V~d) -»e E [i A d] V e

Observe que a equivalência sugerida pelo enunciado é i V d V e, apresentando o conectivo "ou" no lugar do conectivo "e".
O gabarito, portanto, é ERRADO.
Gabarito: 56 - CERTO. 57 - ERRADO.

QUESTõES CoMENTADAS - CEBRASPE

Álgebra de proposições l.(CESPE/CBM AL/2021) Considerando os conectivos lógicos usuais, assumindo que as letras maiusculas representam proposições lógicas e considerando que o símbolo ~ representa a negação,julgue o item a seguir, relacionados à lógica proposicional.
A expressão ~(PA(~Q))«->(QV(~P)) é uma tautologia.
Comentários:

Devemos verificar se a bicondicional ~(PA(~Q))<->(QV(~P)) é uma tautologia.

Observe que a primeira parcela, dada por ~(PA(~Q)), é a negação de uma conjunção.
Para negar uma conjunção, podemos utilizar De Morgan: negam-se as duas proposições e troca-se o "e"pelo "ou". Ficamos com:
~(PA(~Q)) = ((~p)v~(~Q))

A dupla negação da proposição simples Q corresponde à proposição original. Logo, temos:

~(PA(~Q)) = ((~P)VQ)

Substituindo na bicondicional a parcela ~(PA(~Q)) pelo equivalente ((~P)VQ), ficamos com:

((~P)VQ)<->(QV(~P))

Pela propriedade comutativa, note que podemos trocar de posição as parcelas da disjunção inclusiva
(Qv(~P)), ficando com ((~P)VQ). Portanto, a bicondicional original pode ser reescrita da seguinte forma:
((~P)VQ)<->((~P)VQ)

Sabemos que, para a bicondicional ser verdadeira, ambas as parcelas devem apresentar o mesmo valor lógico.
Como a bicondicional em questão apresenta duas parcelas iguais, então essa bicondicional sempre apresentará o mesmo valor lógico nas duas parcelas. Consequentemente, a bicondicional em questão será sempre verdadeira. Logo, é correto afirmar que a bicondicional é uma tautologia.
Gabarito: CERTO.

2.(CESPE/EMAP/2018) Julgue o item seguinte, relativo à lógica proposicional e de argumentação.

Se P e Q são proposições lógicas simples, então a proposição composta S = [P->Q] <-> [QV(~P)J é uma tautologia, isto é, independentemente dos valores lógicos V ou F atribuídos a P e Q, o valor lógico de Sserá sempre V

Comentários:

Poderíamos resolver essa questão por tabela-verdade ou provando por absurdo. Observe, porém, que o lado direito da bicondicional [Qv(~P)j, pela propriedade comutativa, pode ser reescrito por:
[(~P)vQ]

Para transformar a disjunção inclusiva em uma condicional, podemos usar a equivalência pVq = ~p-»q. Para aplicar essa equivalência, devemos realizar o seguinte procedimento:
* Nega-se o primeiro termo;

* Troca-se a disjunção inclusiva (V) pela condicional (->); e

* Mantém-se o segundo termo.

Aplicando-se para o caso em questão, temos:

[~(~P)->Q]

A dupla negação corresponde à proposição original. Ficamos com:

[P->Q]

Observe então que o lado direito da bicondicional é a condicional acima, de modo que podemos reescrever a nossa bicondicional como:
[P->Q] o [P-»Q]

Como os dois lados da bicondicional sempre vão apresentar o mesmo valor, essa bicondicional é sempre verdadeira e, portanto, trata-se de uma tautologia.
Gabarito: CERTO.

3.(CESPE/BACEN/2013) Pl: O governo quer que a ferrovia seja construída, há necessidade de volumosos investimentos iniciais na construção e não haverá demanda suficiente por sua utilização nos primeiros anos de operação.
A negação da proposição Pl estará corretamente expressa por "O governo não quer que a ferrovia seja construída, não há necessidade de volumosos investimentos iniciais na construção ou haverá demanda suficiente por sua utilização nos primeiros anos de operação".
Comentários:

Sejam as proposições simples:

g:" O governo quer que a ferrovia seja construída."

i: "Há necessidade de volumosos investimentos iniciais na construção."

d: "Haverá demanda suficiente por sua utilização nos primeiros anos de operação."

Note que a proposição PI pode ser descrita por g A i A ~d. Observe, também, que a primeira conjunção tem o conectivo "e" omitido:
g A i A ~d: "[O governo quer que a ferrovia seja construída], [há necessidade de volumosos investimentos iniciais na construção] e [não haverá demanda suficiente por sua utilização nos primeiros anos de operação]."
A negação de PI pode ser pode ser desenvolvida por De Morgan, pois temos conjunções nessa proposição composta. Pela propriedade associativa, podemos separar a proposição PI em duas parcelas, sendo essa separação indiferente. Vamos então separar PI como (g A i) A ~d.
Para negar essa conjunção composta pelas parcelas (g A i) e ~d, devemos seguir o seguinte procedimento:
* Negam-se ambas as parcelas da conjunção;

* Troca-se a conjunção (A) pela disjunção inclusiva (V).

Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Temos:

~[(g A i) A ~d] = ~ (gAi)V~(~d)

A dupla negação corresponde à proposição original. Logo, ficamos com:

~[(g A i) A ~d] = ~(gAi)Vd

A parcela ~(gAi) pode ser desenvolvida novamente por De Morgan: negam-se as duas proposições e troca-se o "e" pelo "ou". Temos:

~[(g A i) A ~d] = (~gV~i) V d

Pela propriedade associativa, podemos remover os parênteses de [(g A i) A ~d] e de
(~gV~i) V d. Ficamos com:
~[g A i A ~d] = ~g V ~i V d

Podemos descrever a negação de PI proposição como:

~g V ~i V d: "[O governo não quer que a ferrovia seja construída] ou [não há necessidade de volumosos investimentos iniciais na construção] ou [haverá demanda suficiente por sua utilização nos primeiros anos de operação]."
A proposição que obtivemos difere da apresentada na assertiva somente pelo primeiro ou, que não é apresentado no item a ser julgado como certo errado. No lugar desse conectivo é apresentada uma vírgula.Veja:

"[O governo não quer que a ferrovia seja construída], [não há necessidade de volumosos investimentos iniciais na construção] ou [haverá demanda suficiente por sua utilização nos primeiros anos de operação]."
Nesse caso, a banca quis que a vírgula fosse interpretada como um "ou". Na proposição original Pl,
a vírgula funcionou como um conectivo "e" porque havia um conectivo "e" ao final da proposição composta. Já na negação, a banca entendeu que vírgula funcionou como um conectivo "ou" porque havia um conectivo "ou"ao final da proposição composta. O gabarito, portanto, é CERTO.

Gabarito: CERTO.

4.(CESPE/SEFAZ RS/2018) Se P, Q e R são proposições simples, então a proposição
-*[P->(Q->R)] é equivalente a a) (R^QH
b) (~P)-*[(~Q)-»(~R)].

c) (~P)AQAR

d) PAQA(~R).

e) (~P)->(Q->R)

Comentários:

Podemos desenvolver a proposição ~[P->(Q->R)] realizando a negação da condicional formada pelo antecedente P e pelo consequente (Q—>R).
Para realizar a negação de uma condicional, usa-se a equivalência ~(p-»q) =
pA~q. Para aplicar essa equivalência, devemos seguir o seguinte procedimento:
* Mantém-se o primeiro termo;

* Troca-se a condicional (-») pela conjunção (A); e

* Nega-se o segundo termo.

Aplicando essa equivalência em ~[P-»(Q->R)], devemos manter P, tocar a primeira condicional por uma conjunção e negar (Q->R):
~[P"> (Q->R)1 = PA[~(Q->R)1

A segunda parcela da conjunção obtida, ^(Q->R), também é a negação de uma condicional. Portanto,podemos aplicar a mesma equivalência nessa parcela:

~[P->(Q->R)] = PA[QA(~R)J

A equivalência obtida corresponde à alternativa D, que não apresenta os colchetes. Isso porque, pela propriedade associativa, podemos executar as conjunções em qualquer ordem.
Gabarito: Letra D.

5.(CESPE/PF/2018) As proposições P, Q e R a seguir referem-se a um ilícito penal envolvendo João,
Carlos,
Paulo e Maria:

P: "João e Carlos não são culpados".
Q: "Paulo não é mentiroso".

R: "Maria é inocente".

Considerando que ~X representa a negação da proposição X, julgue o item a seguir.

Independentemente de quem seja culpado, a proposição {P->(--Q)}-»{QV[(--Q)VR]}
será sempre verdadeira, isto é, será uma tautologia.
Comentários:

Primeiramente, vale notar que a construção da tabela-verdade é uma solução possível.
Veja que, de fato, a proposição em questão será sempre verdadeira, isto é, uma tautologia.
Vamos agora resolver de uma outra forma. Observe a proposição composta sugerida pelo enunciado:

{P-»(~Q)}->{QV[(~Q)VR]}

Podemos aplicar a propriedade associativa no consequente {QV[(~Q)VR]}, obtendo:

(QV~Q)VR

Observe que (QV~Q) é uma tautologia, pois se trata de uma disjunção inclusiva em que necessariamente uma das duas parcelas é verdadeira. Isso significa que o nosso consequente fica:
t V R

Observe que t V R é uma disjunção inclusiva com um dos termos sempre verdadeiro t.
Trata-se de uma tautologia. O nosso consequente fica:
t

Finalmente, a condicional fica:

O fato do consequente da condicional ser sempre verdadeiro garante que tal condicional é sempre verdadeira, pois o único caso em que uma condicional é falsa é quando o antecedente é V e o consequente é F. Temos, então, uma tautologia.
Caso não tivéssemos percebido isso, poderíamos continuar desenvolvendo a expressão. Utilizando a equivalência entre condicional e disjunção inclusiva, dada por p-»q = ~pVq, teríamos:
~{P-*(~Q)}vt

Novamente, observe que temos uma disjunção inclusiva com um dos termos sempre verdadeiro (t). Trata-se de uma tautologia.

Gabarito: CERTO.

6.(CESPE/PF/2018) As proposições P, Q e R a seguir referem-se a um ilícito penal envolvendo João,
Carlos,
Paulo e Maria:

P: "João e Carlos não são culpados".
Q: "Paulo não é mentiroso".

R: "Maria é inocente".

Considerando que ~X representa a negação da proposição X, julgue o item a seguir.
As proposições PA(~Q)-»(~R) e R->[QA(~P)J são equivalentes.

Comentários:

Primeiramente, vale notar que a construção da tabela-verdade é uma solução possível.
Veja que, ao colocar as duas proposições compostas em uma mesma tabela, percebe-se que elas não são equivalentes, pois seus valores são diferentes na primeira e na sétima linha.
p Q R ~P ~Q ~R PA~Q QA~P [PÁ-O]—>~R R >[QA~P]

V V V F F F F F V
F

V V F F V F F V
V

V V F V F V F F
F

V F V V V F V
V

V V V F F F V V
V

V V F V F V V
V

V V V F F F V F

V V V F F V V

Vamos agora resolver de outra forma.

A questão pergunta sobre a equivalência entre duas condicionais. Isso nos faz lembrar da contrapositiva p-*q = ~q->~p. Vamos aplicar essa equivalência na primeira proposição:
PA(~Q)-»(~R) = ~(~R) -> ~[PA(~Q)]

A dupla negação ~(~R) corresponde à proposição original R, logo:

PA(~Q)-»(~R) = R -> [PA(~Q)J

Aplicando De Morgan em ~[PA(~Q)], ficamos com:

PA(~Q)->(~R) = R —* [(~P)VQ]

Para melhor visualização, aplicaremos a propriedade comutativa em ~PVQ:

PA(~Q)—>(~R) = R -> [QV(~P)J

Perceba que a questão apresentou R -> [QA(~P)J como equivalente a PA(~Q)->(~R),
tornando a assertiva errada.
Gabarito: ERRADO.

7.(CESPE/TRE-GO/2015)

Q: Se L for um número natural divisível por 3 e por 5, então L será divisível por 15.
Julgue o item que se segue, acerca de lógica proposicional.

Se L for um número natural e se U, V e W forem as seguintes proposições:
U: " é divisível por 3";

V: "é divisível por 5";
W: "é divisível por 15";

então a proposição --Q, a negação de Q, poderá ser corretamente expressa por UAVA(--W).

Comentários:

Q é uma condicional que pode ser escrita do seguinte modo:

(UA V) W

Para resolver a questão, podemos construir a tabela-verdade da negação de (UA V) -> W
e comparar com

UAVA(-W).

Veja, na tabela abaixo, que de fato a negação da proposição sugerida pode ser expressa por UAVA(--W), pois elas apresentam a mesma tabela-verdade. O gabarito, portanto, é CERTO.
Uma outra forma de resolver é utilizando equivalências lógicas. Para negar Q, devemos negar a condicional acima. Assim, utilizaremos a equivalência ~(p-> q) = pA~ q.
~ [(UA V) —* W] = (UA V) A (~W)

Sabemos que, pela propriedade associativa, a ordem de execução das três conjunções do lado direito é indiferente. Logo, podemos representar:
~ [(UA V) -> W] = UA V A (~W)

Logo, ~ Q pode ser expressa por UA V A (~W).
Gabarito: CERTO.

8.(CESPE/TJ SE/2014) Julgue o próximo item, considerando os conectivos lógicos usuais A,
V, ->,<-> e que P, Q e R representam proposições lógicas simples.
A proposição [P->(QAR)]o-{[(-P)VQ]A[(-P)VR]} é uma tautologia.
Comentários:

Primeiramente, vale notar que a construção da tabela-verdade é uma solução possível.
Ocorre que essa não é a melhor forma de se resolver a questão, pois levaria mais tempo.
Vamos resolver o problema por álgebra de proposições.

Utilizando a equivalência p-»q = ~pVq, o lado direito da bicondicional, [P->(QAR)],
pode ser descrito por

-PV(QAR).

Já no lado esquerdo da bicondicional, dado por (~PVQ)A(~PVR), podemos colocar
"~PV" em evidência

(propriedade distributiva):

(-PVQ)A(-PVR) = -PV(QAR)

Veja, portanto, que tanto o lado direito quanto o lado esquerdo da bicondicional correspondem a ~PV(QAR).Temos uma bicondicional em que ambos os lados terão sempre o mesmo valor lógico. Como essa bicondicional será sempre verdadeira, temos uma tautologia.
Gabarito: CERTO.

9.(CESPE/AFT/2013)

p Q R S

V V V

V V F

V F V

V F F

F V V

F V F

F F V

F F F

A tabela acima corresponde ao início da construção da tabela-verdade da proposição S,
composta das proposições simples P, Q e R. Julgue o item seguinte a respeito da tabela-verdade de S.
Se S = (PAQ)V(PAR), então a última coluna da tabela-verdade de S conterá, de cima para baixo e na ordem em que aparecem, os seguintes elementos: V, F, V, V, F, V, F e F.
Comentários:

Pessoal, é claro que uma das formas de resolver a questão é construindo a tabela-verdade. Ocorre que, ao"bater o olho" em (PAQ)V(PAR), é importante que você já perceba que podemos colocar "PA" em evidência:
(PAQ)V(PAR) = PA(QVR)

Note, portanto, que temos uma conjunção entre P e (QVR). Para a conjunção ser verdadeira, tanto P quanto
(QVR) devem ser verdadeiras.

Analisando a assertiva, veja que ela sugere que a sexta linha é verdadeira: V, F, V, V, F, V, F e
F. Note que na sexta linha temos P falso, logo, a conjunção de P com (QVR) é falsa, não verdadeira.O gabarito, portanto, é
ERRADO.

Gabarito: ERRADO.

1O.(CESPE/CADE/2O14) Considerando os conectivos lógicos usuais e que as letras maiúsculas representem proposições lógicas simples, julgue o item seguinte acerca da lógica proposicional.
A proposição [(PVQ)A(RVS)] <-> [QA(RVS)]V[(PAR)V(PAS)J é uma tautologia.
Comentários:

ESTA É

DIFÍCIL!

Observe que temos quatro proposições simples nessa questão. Realizar a tabela-verdade resultaria em 16linhas e muitas colunas, sendo inviável gastar esse tempo com uma única questão em uma prova de certo e errado. A melhor solução para esse problema é utilizar álgebra de proposições.
Propriedade distributiva "colocando PA em evidência":

[(PVQ)A(RVS)] <-> [QAfRVSjJVtíMRJVÍPls)]
[(PVQ)A(RVS)] ++ [QA(RVS)]V[P/|(RVS)]

Aplicação da propriedade comutativa duas vezes:

[(PVQ)A(RVS)] ++ [QA(RVS)]V[PA(RVS)1

[(PVQ)A(RVS)] <-> [(RVS)AQ]V[(RVS)APJ

Propriedade distributiva colocando "(RVS)A" em evidência:

[(PVQ)A(RVS)] O [(RVS)AQ]V[(RVS)AP]

[(PVQ)A(RVS)] <-> [(RVS)A(QVP)]

Já podemos perceber que ambos os lados da bicondicional tem as mesmas proposições simples, bastando realizar a propriedade comutativa em alguns termos.
[(PVQ)A(RVS)] <-> [(RVS)A(QVP)]

[(PVQ)A(RVS)] O [(RVS)A(PVQ)]

[(PVQ)A(RVS)] ++ [(PVQ)A(

Como a bicondicional apresentada apresenta dois termos iguais, eles sempre apresentarão o mesmo valor lógico. Sendo assim, a bicondicional sempre será verdadeira, tratando-se de uma tautologia.
Gabarito: CERTO.

Equivalências lógicas

Equivalências fundamentais

1. (CESPE/PC DF/2021) Com relação a estruturas lógicas, lógica de argumentação e lógica proposicional,julgue o item subsequente.

A proposição "Se Paulo está mentindo, então Maria não está mentindo" é equivalente à proposição "SeMaria está mentindo, então Paulo não está mentindo".

2. (CESPE/PM TO/2021) A proposição "Se André é culpado então Bruno não é suspeito" é equivalente à a) "Se Bruno é suspeito então André é inocente".
b) "Se Bruno não é suspeito então André é culpado".

c) "Se Bruno é suspeito então André não é inocente".

d) "Se André é inocente então Bruno é culpado".

e) "Se André não é culpado então Bruno é suspeito".

3. (CESPE/SEFAZ AL/2020) P: "Se o trabalho dos servidores públicos que atuam no setor
Alfa fica prejudicado, então os servidores públicos que atuam nesse setor padecem.".
A proposição P é equivalente à proposição "Se os servidores públicos que atuam nesse setor não padecem,então o trabalho dos servidores públicos que atuam no setor Alfa não fica prejudicado."

4. (CESPE/TJ-SE/2014) Considerando que P seja a proposição "Se os seres humanos soubessem se comportar, haveria menos conflitos entre os povos", julgue o item seguinte.
A proposição P é logicamente equivalente à proposição "Se houvesse menos conflitos entre os povos,
os seres humanos saberiam se comportar".
5. (CESPE/EMAP/2018) Julgue o item seguinte, relativo à lógica proposicional e de argumentação.

A proposição "Se Sônia é baixa, então Sônia pratica ginástica olímpica." é logicamente equivalente à sentença "Se Sônia é alta, então Sônia não pratica ginástica olímpica."
0.0
www. estra tegiaconcursos. com. br

6.(CESPE/MDIC/2014) A proposição "Se o interessado der três passos, alugará a pouca distância uma loja por um valor baixo" é equivalente à proposição "Se o interessado não der três passos, não alugará a pouca distância uma loja por um valor baixo".
7.(CESPE/ANVISA/2016) Considerando os símbolos normalmente usados para representar os conectivos lógicos, julgue os itens seguintes, relativos a lógica proposicional e à lógica de argumentação. Nesse sentido, considere, ainda, que as proposições lógicas simples sejam representadas por letras maiúsculas.
A sentença "Alberto é advogado, pois Bruno não é arquiteto" é logicamente equivalente à sentença"Bruno é arquiteto, pois Alberto não é advogado".

8.(CESPE/TRT17/2013) Considerando a proposição P: "Se estiver sob pressão dos corruptores ou diante de uma oportunidade com baixo risco de ser punido, aquele funcionário público será leniente com a fraude ou dela participará", julgue o item seguinte relativo à lógica sentenciai.
A proposição P é equivalente a "Se aquele funcionário público foi leniente com a fraude ou dela participou,então esteve sob pressão dos corruptores ou diante de uma oportunidade com baixo risco de ser punido".
9.(CESPE/CEF/2014) Considerando a proposição "Se Paulo não foi ao banco, ele está sem dinheiro",
julgue o item seguinte.
A proposição em apreço equivale à proposição "Paulo foi ao banco e está sem dinheiro".

10.(CESPE/TRE-G0/2015) P: Se L for um triângulo retângulo em que a medida da hipotenusa seja igual a c e os catetos meçam a e b, então c2 = a2 + b2.
Julgue o item que se segue, acerca de lógica proposicional.

A proposição P será equivalente à proposição (--R) V S, desde que R e S
sejam proposições convenientemente escolhidas.
ll.(CESPE/PF/2018) P: "A nomeação do novo servidor público ocorre para reposição de vacância em área essencial, ou o candidato aprovado não será nomeado".
A proposição P é logicamente equivalente à proposição: "Se não for para reposição de vacância em área essencial, então o candidato aprovado não será nomeado".
12.(CESPE/CAM DEP/2014) C: O candidato X me dará um agrado antes da eleição ou serei atingido por uma benfeitoria que ele fizer depois de eleito.
A proposição C é equivalente à seguinte proposição: "Se o candidato X não me der um agrado antes da eleição, serei atingido por uma benfeitoria que ele fizer após ser eleito".
Negação da conjunção e da disjunção inclusiva (leis de De Morgan)

13.(CESPE/MDIC/2014) A negação da proposição "A Brasil Central é uma das ruas mais movimentadas do centro da cidade e lá o preço dos aluguéis é alto" está corretamente expressa por "A Brasil Central não é uma das ruas mais movimentadas do centro da cidade ou lá o preço dos aluguéis não é alto".
14. (CESPE/SEFAZ-AL/2020) A negação da proposição "Os servidores públicos que atuam nesse setor padecem e os beneficiários dos serviços prestados por esse setor padecem." é corretamente expressa por"Os servidores públicos que atuam nesse setor não padecem e os beneficiários dos serviços prestados por esse setor não padecem."
15.(CESPE/TRE MS/2013) A negação da proposição "Crescer além de certo porte é um ótimo negócio para empresários, mas um mau negócio para o mundo" é equivalente a a) Crescer além de certo porte não é um ótimo negócio para empresários ou não é um mau negócio para o mundo.
b) Não crescer além de certo porte é um ótimo negócio para empresários, mas um mau negócio para o mundo.
c) Não crescer além de certo porte não é um ótimo negócio para empresários, mas um mau negócio para o mundo.
d) Não crescer além de certo porte não é um ótimo negócio para empresários, nem um mau negócio para o mundo.
e) Crescer além de certo porte não é um ótimo negócio para empresários, nem um mau negócio para o mundo.
16. (CESPE/SEFAZ-RS/2018) A negação da proposição "O IPTU, eu pago parcelado; o IPVA,
eu pago em parcela única" pode ser escrita como a) "Eu pago o IPTU em parcela única ou pago o IPVA parcelado".
b) "Eu não pago o IPTU parcelado e não pago o IPVA em parcela única".

c) "Eu não pago o IPTU parcelado e pago o IPVA parcelado".

d) "Eu não pago o IPTU parcelado ou não pago o IPVA em parcela única".

e) "Eu pago o IPTU em parcela única e pago o IPVA parcelado".

17. (CESPE/SERPRO/2013) A negação da proposição "O síndico troca de carro ou reforma seu apartamento"pode ser corretamente expressa por "O síndico não troca de carro nem reforma seu apartamento".

18.(CESPE/PC MA/2018) A qualidade da educação dos jovens sobe ou a sensação de segurança da sociedade diminui.
Assinale a opção que apresenta uma proposição que constitui uma negação da proposição.

a) A qualidade da educação dos jovens não sobe e a sensação de segurança da sociedade não diminui.

b) A qualidade da educação dos jovens desce ou a sensação de segurança da sociedade aumenta.

c) A qualidade da educação dos jovens não sobe ou a sensação de segurança da sociedade não diminui.

d) A qualidade da educação dos jovens sobe e a sensação de segurança da sociedade diminui.

e) A qualidade da educação dos jovens diminui ou a sensação de segurança da sociedade sobe.

19. (CESPE/MEC/2014) A negação da proposição "O candidato é pós-graduado ou sabe falar inglês"
pode ser corretamente expressa por "O candidato não é pós-graduado nem sabe falar inglês".
20.(CESPE/DETRAN-DF/2009) Considerando que A, B e C sejam proposições, que os símbolos
V e A
representam os conectivos "ou" e "e", respectivamente, e que o símbolo - denota o modificador negação,julgue o item a seguir.

A proposição (AVB)A[(--A)A(--B)] é sempre falsa.

21.(CESPE/BNB/2018) Julgue o item que se segue, a respeito de lógica proposicional.

Se P e Q forem proposições simples, então a proposição -[PV(--Q)]o[(-'P)AQ] é uma tautologia.

Negação da Condicional

22.(CESPE/PETROBRAS/2022) Acerca de lógica matemática, julgue o item a seguir.

A negativa da sentença composta "Se o preço está elevado, então a compra não será realizada." é "O
preço está elevado e a compra será realizada.".
23.(CESPE/TC-DF/2O21) Considerando que P e Q sejam, respectivamente, as proposições
"Ausência de evidência de um crime não é evidência da ausência do crime." e "Se não há evidência,não há crime.",
julgue a seguir.

A negação da proposição Q pode ser corretamente expressa por "Não há evidência, mas há crime.".

24.(CESPE/DEPEN/2021) Com relação a lógica proposicional, julgue o item a seguir.

Uma tautologia é uma proposição composta em que seu valor lógico será sempre verdadeiro,independentemente do valor lógico das proposições que a estruturam. Nesse sentido,
considerando-se p e q como proposições, a proposição composta pAq<^~(p-»~q) é uma tautologia.
25. (CESPE/ANVISA/2016) Julgue o seguinte item, relativo a raciocínio lógico, a princípios de contagem e probabilidade e a operações com conjuntos.
A sentença "Se João tem problemas cardíacos, então ele toma remédios que controlam a pressão." pode ser corretamente negada pela sentença "João tem problemas cardíacos e ele não toma remédios que controlam a pressão".
26.(CESPE/EBSERH/2018) A respeito de lógica proposicional, julgue o item que se segue.

A negação da proposição "Se o fogo for desencadeado por curto-circuito no sistema elétrico, será recomendável iniciar o combate às chamas com extintor à base de espuma." é equivalente à proposição"O fogo foi desencadeado por curto-circuito no sistema elétrico e não será recomendável iniciar o combate às chamas com extintor à base de espuma."
27.(CESPE/MPOG/2015) Considerando a proposição P: "Se João se esforçar o bastante, então
João conseguirá o que desejar", julgue o item a seguir.
A negação da proposição P pode ser corretamente expressa por "João não se esforçou o bastante, mas,mesmo assim, conseguiu o que desejava".

28. (CESPE/COGE-CE/2019) Pl: Se os recursos foram aplicados em finalidade diversa da prevista ou se a obra foi superfaturada, então a prestação de contas da prefeitura não foi aprovada.
Assinale a opção correspondente à proposição equivalente à negação da proposição Pl.

a) "Os recursos foram aplicados em finalidade diversa da prevista ou a obra foi superfaturada, mas a prestação de contas da prefeitura foi aprovada".
b) "Os recursos foram aplicados em finalidade diversa da prevista e a obra foi superfaturada, mas a prestação de contas da prefeitura foi aprovada".
c) "Os recursos não foram aplicados em finalidade diversa da prevista e a obra não foi superfaturada, mas a prestação de contas da prefeitura foi aprovada".
d) "Se os recursos não foram aplicados em finalidade diversa da prevista e a obra não foi superfaturada,então a prestação de contas da prefeitura foi aprovada".

e) "Se a prestação de contas da prefeitura foi aprovada, então os recursos não foram aplicados em finalidade diversa da prevista e a obra não foi superfaturada".
Outras equivalências e negações

29.(CESPE/PETROBRAS/2022) Acerca de lógica matemática, julgue o item a seguir.
Dadas três proposições p, q e r, tem-se que pVq->r é equivalente a (p-»r)V(q-»r).

30. (CESPE/TCE-RS/2013) Com base na proposição P: "Quando o cliente vai ao banco solicitar um empréstimo, ou ele aceita as regras ditadas pelo banco, ou ele não obtém o dinheiro",julgue o item que se segue.
A negação da proposição "Ou o cliente aceita as regras ditadas pelo banco, ou o cliente não obtém o dinheiro" é logicamente equivalente a "O cliente aceita as regras ditadas pelo banco se, e somente se, o cliente não obtém o dinheiro"
31.(CESPE/PC-CE/2012) Considere as proposições:

Pl: Se se deixa dominar pela emoção ao tomar decisões, então o policial toma decisões ruins.
P2: Se não tem informações precisas ao tomar decisões, então o policial toma decisões ruins.

A proposição formada pela conjunção de Pl e P2 é logicamente equivalente à proposição
"Se se deixa dominar pela emoção ou não tem informações precisas ao tomar decisões, então o policial toma decisões ruins".
32.(CESPE/PRF/2012) Um jovem, visando ganhar um novo smartphone no dia das crianças,
apresentou à sua mãe a seguinte argumentação: "Mãe, se tenho 25 anos, moro com você e papai, dou despesas a vocês e dependo de mesada, então eu não ajo como um homem da minha idade. Se estou há 7 anos na faculdade e não tenho capacidade para assumir minhas responsabilidades, então não tenho um mínimo de maturidade. Se não ajo como um homem da minha idade, sou tratado como criança. Se não tenho um mínimo de maturidade, sou tratado como criança. Logo, se sou tratado como criança,mereço ganhar um novo smartphone no dia das crianças".
Com base nessa argumentação, julgue o item a seguir.

A proposição "Se não ajo como um homem da minha idade, sou tratado como criança, e se não tenho um mínimo de maturidade, sou tratado como criança" é equivalente a "Se não ajo como um homem da minha idade ou não tenho um mínimo de maturidade, sou tratado como criança"
Questões com mais de uma equivalência

33.(CESPE/DEPEN/2021) Com relação a lógica proposicional, julgue o item a seguir.

Considere as seguintes proposições p: "Paola é feliz";
q: "Paola pinta um quadro".

Assim, a proposição "Paola é feliz apenas se ela pinta um quadro" pode ser representada por
~(pA~q).

34.(CESPE/PC DF/2021) A proposição "Se Marcos é culpado, então Paulo ou Carlos são inocentes."
equivale à proposição "Se Paulo ou Carlos são culpados, então Marcos é inocente.".
35. (CESPE/CBM AL/2017) A respeito de proposições lógicas, julgue o item a seguir.
Considere que P e Q sejam as seguintes proposições:

P: Se a humanidade não diminuir a produção de material plástico ou não encontrar uma solução para o problema do lixo desse material, então o acúmulo de plástico no meio ambiente irá degradar a vida no planeta.
Q: A humanidade diminui a produção de material plástico e encontra uma solução para o problema do lixo desse material ou o acúmulo de plástico no meio ambiente degradará a vida no planeta.
Nesse caso, é correto afirmar que as proposições P e Q são equivalentes.

36.(CESPE/PGE-PE/2O19) Acerca da lógica sentenciai, julgue o item que se segue.

Se P, Q, R e S forem proposições simples, então as proposições PVR->QAS e
(~Q)V(~S)->(~P)A(~R) serão equivalentes
37.(CESPE/SERPRO/2013) Considerando que o símbolo lógico A corresponda à conjunção "e";
V, à disjunção "ou"; —>, à condicional "se..., então"; <->, à bicondicional "se, e somente se"; ~ corresponda à negação "não"; P, Q e R sejam proposições simples; e S seja a seguinte proposição composta:[PA~(QVR)]~► [RA(P«->Q)j, julgue o próximo item.

A negação de S —S - pode ser corretamente expressa por [~PV(QVR)]A[(~R)V~(P<^Q)j.

38. (CESPE/TCE-ES/2012) Proposições são sentenças que podem ser julgadas como verdadeiras — V — ou falsas — F —, de forma que um julgamento exclui o outro, e são simbolizadas por letras maiusculas,como
P, Q, R e S. A partir de proposições conhecidas, novas proposições podem ser construídas usando-se símbolos especiais. Alguns desses símbolos são apresentados na tabela abaixo.
símbolo

A
V

—>

nome negação conjunção disjunção condicional notação
-p
PAQ
PVQ
P—>Q

leitura não PPeQ

P ou Q

se P, então Q

valor contrário ao de P: V, se P for F; ou F, se P forVV, se P e Q forem V; caso contrário, será F

F, se P e Q forem F; caso contrário, será V
F, se P for V e Q for F; caso contrário, será V

<—>

bicondicional

P< >Q

P se, e somente se, Q V, se P e Q tiverem os mesmos valores; caso contrário, será F

Considerando as definições acima e a proposição {(PVQ)—>[RA(~S)]}V[(PAS)«->(QAR)], julgue o item a seguir.
Essa proposição é logicamente equivalente à proposição {[(~R)VS]_>[( ~P)A(~Q)]}V[(PAS)< >(QAR)].

39. (CESPE/SEFAZ-ES/2010) Considerando os símbolos lógicos - (negação), A (conjunção), V
(disjunção), -»
(condicional) e as proposições julgue o item que se segue.
S:(pA--q)V(--pAr)-»qVr e
T :{{pA--q)V(--pAr))A(-'qA--r)

As proposições compostas --S e T são equivalentes, ou seja, têm a mesma tabela-verdade,independentemente dos valores lógicos das proposições simples p, q, e r que as constituem.

Questões com mais de um item

Texto para as próximas questões

Considere as proposições lógicas P e Q, a seguir, a respeito de um condômino chamado Marcos.

P: "Se Marcos figura no quadro de associados e está com os pagamentos em dia, então ele tem direito a receber os benefícios providos pela associação de moradores de seu condomínio."-
Q: "Marcos não figura no quadro de associados, mas ele está com os pagamentos em dia."
Tendo como referência essas proposições, julgue os itens a seguir.

40. (CESPE/SEFAZ AL/2021) Considerando-se verdadeira a proposição P, é correto concluir que, se
Marcos não tem direito a receber os benefícios providos pela associação de moradores de seu condomínio,então,
necessariamente, ele não figura no quadro de associados nem está com os pagamentos em dia.

41. (CESPE/SEFAZ AL/2021) A proposição P é equivalente à proposição "Se Marcos não figura no quadro de associados ou não está com os pagamentos em dia, então ele não tem direito a receber os benefícios providos pela associação de moradores de seu condomínio.".
42. (CESPE/SEFAZ AL/2021) A proposição P é equivalente à proposição "Se Marcos tem direito a receber os benefícios providos pela associação de moradores de seu condomínio, então ele figura no quadro de associados e está com os pagamentos em dia.".
43. (CESPE/SEFAZ AL/2021) A proposição Q é uma negação da proposição "Se Marcos está com os pagamentos em dia, então ele figura no quadro de associados.".
Texto para as próximas questões

: Pl: Se a fiscalização foi deficiente, as falhas construtivas não foram corrigidas.

= P2: Se as falhas construtivas foram corrigidas, os mutuários não tiveram prejuízos.

: P3: A fiscalização foi deficiente.

= C: Os mutuários tiveram prejuízos.

: Considerando um argumento formado pelas proposições precedentes, em que C é a conclusão, e Pl a P3 são
= as premissas, julgue os itens a seguir.

44. (CESPE/PF/2021) A proposição Pl é equivalente a "Não é verdade que a fiscalização foi deficiente e que as falhas construtivas foram corrigidas".
45. (CESPE/PF/2021) Uma negação correta da proposição Pl pode ser expressa por: "Se a fiscalização não foi deficiente, as falhas construtivas foram corrigidas".
46.(CESPE/PF/2021) A proposição P2 é equivalente a "Se as falhas construtivas não foram corrigidas, os mutuários tiveram prejuízos".
* .

Texto para as próximas questões

: Julgue os seguintes itens, considerando a proposição P: "Se o responsável pela indicação fizer sua parte e j
L:
s..e..u..s...a..l.ia...d..o..s..t.r..a.b..a..l.h..a..re..md..u..r.o..,..v..e.n..c..e..r.ã..o...
."
I;

47. (CESPE/MJSP/2021) A proposição P é equivalente a "Se não vencermos, o responsável pela indicação não terá feito sua parte ou seus aliados não terão trabalhado duro.".
48. (CESPE/MJSP/2021) A negação da proposição P pode ser expressa por "Se o responsável pela indicação não fizer sua parte ou seus aliados não trabalharem duro, não vencerão.".
.

Texto para as próximas questões

I

I

: Considerando a proposição P: "Se o servidor gosta do que faz, então o cidadão-cliente fica satisfeito", julgue ;
: os itens a seguir.
;

49. (CESPE/SEFAZ DF/2020) A proposição P é logicamente equivalente à seguinte proposição: "Se o cidadão-cliente não fica satisfeito, então o servidor não gosta do que faz".
50. (CESPE/SEFAZ DF/2020) A proposição "O servidor não gosta do que faz, ou o cidadão-cliente não fica satisfeito" é uma maneira correta de negar a proposição P.
|

Texto para as próximas questões

: Considerando a proposição P: "Se João se esforçar o bastante, então João conseguirá o que desejar", julgue ;
= os itens a seguir.
;

51. (CESPE/MPOG/2015) A proposição "João não se esforça o bastante ou João conseguirá o que desejar"
é logicamente equivalente à proposição P.

52. (CESPE/MPOG/2015) A proposição "Se João não conseguiu o que desejava, então João não se esforçou o bastante" é logicamente equivalente à proposição P.
.

Texto para as próximas questões

= Julgue os itens, considerando a proposição P a seguir.

: P: "O bom jornalista não faz reportagem em benefício próprio nem deixa de fazer aquela que prejudique j
= seus interesses".

53. (CESPE/PF/2O18) A proposição P é logicamente equivalente à proposição: "Não é verdade que o bom jornalista faça reportagem em benefício próprio ou que deixe de fazer aquela que prejudique seus interesses".
54. (CESPE/PF/2018) A negação da proposição P está corretamente expressa por: "O bom jornalista faz reportagem em benefício próprio e deixa de fazer aquela que não prejudique seus interesses".
55. (CESPE/PF/2018) A negação da proposição P está corretamente expressa por: "Se o bom jornalista não faz reportagem em benefício próprio, então ele deixa de fazer aquela reportagem que prejudica seus interesses".
.

Texto para as próximas questões

I

I

: Considere a proposição P a seguir.
;

: P: Se não condenarmos a corrupção por ser imoral ou não a condenarmos por corroer a legitimidade da j
; democracia, a condenaremos por motivos econômicos.
;

: Tendo como referência a proposição apresentada, julgue os itens seguintes.
j

56. (CESPE/TC-DF/2014) A proposição P é logicamente equivalente à proposição "Se não condenarmos a corrupção por motivos econômicos, a condenaremos por ser imoral e por corroer a legitimidade da democracia".
57. (CESPE/TC-DF/2014) A proposição P é logicamente equivalente à proposição
"Condenaremos a corrupção por ser imoral ou por corroer a legitimidade da democracia ou por motivos econômicos".
GABARITo - CEBRASPE

Equivalências lógicas

1. CERTO 21.CERTO
41. ERRADO

2. LETRA A 22.CERTO
42. ERRADO

3. CERTO 23.CERTO
43. CERTO

4. ERRADO 24.CERTO
44. CERTO

5. ERRADO 25.CERTO
45. ERRADO

6. ERRADO 26.CERTO
46. ERRADO

7. CERTO 27. ERRADO
47. CERTO

8. ERRADO 28. LETRA A
48. ERRADO

9. ERRADO 29. ERRADO
49.CERTO

10.CERTO 30.CERTO
50. ERRADO

11. CERTO 31.CERTO
51. CERTO

12. CERTO 32.CERTO
52. CERTO

13. CERTO 33.CERTO
53.CERTO

14. ERRADO 34. ERRADO
54. ERRADO

15. LETRA A 35.CERTO
55.CERTO

16. LETRA D 36.CERTO
56. CERTO

17. CERTO 37. ERRADO
57. ERRADO

18. LETRA A 38.CERTO

19.CERTO 39.CERTO

20. CERTO 40. ERRADO

LISTA DE QUESTõES - CEBRASPE

Álgebra de proposições l.(CESPE/CBM AL/2021) Considerando os conectivos lógicos usuais, assumindo que as letras maiusculas representam proposições lógicas e considerando que o símbolo ~ representa a negação,julgue o item a seguir, relacionados à lógica proposicional.
A expressão ~(PA(~Q))«->(QV(~P)) é uma tautologia.

2.(CESPE/EMAP/2018) Julgue o item seguinte, relativo à lógica proposicional e de argumentação.

Se P e Q são proposições lógicas simples, então a proposição composta S = [P—*Q] <->
[QV(~P)J é uma tautologia, isto é, independentemente dos valores lógicos V ou F atribuídos a P e Q,o valor lógico de S
será sempre V

3.(CESPE/BACEN/2013) Pl: O governo quer que a ferrovia seja construída, há necessidade de volumosos investimentos iniciais na construção e não haverá demanda suficiente por sua utilização nos primeiros anos de operação.
A negação da proposição Pl estará corretamente expressa por "O governo não quer que a ferrovia seja construída, não há necessidade de volumosos investimentos iniciais na construção ou haverá demanda suficiente por sua utilização nos primeiros anos de operação".
4.(CESPE/SEFAZ-RS/2018) Se P, Q e R são proposições simples, então a proposição
--[P->(Q-»R)] é equivalente a a) (R^QH
b) (~P)-»[(~Q)-»(~R)].

c) (~P)AQAR

d) PAQA(~R).

e) (-PH(Q^R)

5. (CESPE/PF/2018) As proposições P, Q e R a seguir referem-se a um ilícito penal envolvendo João,
Carlos,
Paulo e Maria:

P: "João e Carlos não são culpados".
Q: "Paulo não é mentiroso".

R: "Maria é inocente".

Considerando que ~X representa a negação da proposição X, julgue o item a seguir.

Independentemente de quem seja culpado, a proposição {P->(--Q)}->{QV[(--Q)VR]}
será sempre verdadeira, isto é, será uma tautologia.
6. (CESPE/PF/2018) As proposições P, Q e R a seguir referem-se a um ilícito penal envolvendo João,
Carlos,
Paulo e Maria:

P: "João e Carlos não são culpados".
Q: "Paulo não é mentiroso".

R: "Maria é inocente".

Considerando que ~X representa a negação da proposição X, julgue o item a seguir.
As proposições PA(~Q)->(~R) e R->[QA(~P)] são equivalentes.

7. (CESPE/TRE-GO/2015)

Q: Se L for um número natural divisível por 3 e por 5, então L será divisível por 15.
Julgue o item que se segue, acerca de lógica proposicional.

Se L for um número natural e se U, V e W forem as seguintes proposições:

U: " é divisível por 3";
V: "é divisível por 5";
W: "é divisível por 15";

então a proposição --Q, a negação de Q, poderá ser corretamente expressa por UAVA(--W).

8. (CESPE/TJ SE/2014) Julgue o próximo item, considerando os conectivos lógicos usuais
-, A, V, ->,<-> e que P, Q e R representam proposições lógicas simples.
A proposição [P-»(QAR)]<->{[(--P)VQ]A[(-«P)VR]} é uma tautologia.

9.(CESPE/AFT/2O13)

p Q R S

V V V

V V F

V F V

V F F

F V V

F V F

F F V

F F F

A tabela acima corresponde ao início da construção da tabela-verdade da proposição S,
composta das proposições simples P, Qe R. Julgue o item seguinte a respeito da tabela-verdade de S.
Se S = (PAQ)V(PAR), então a última coluna da tabela-verdade de S conterá, de cima para baixo e na ordem em que aparecem, os seguintes elementos: V, F, V, V, F, V, F e F.
10. (CESPE/CADE/2014) Considerando os conectivos lógicos usuais e que as letras maiúsculas representem proposições lógicas simples, julgue o item seguinte acerca da lógica proposicional.
A proposição [(PVQ)A(RVS)] <-> [QA(RVS)]V[(PAR)V(PAS)J é uma tautologia.

GABARITo - CEBRASPE

Álgebra de proposições

1. CERTO

2. CERTO

3. CERTO

4. LETRA D

5. CERTO

6. ERRADO

7. CERTO

8. CERTO

9. ERRADO

10. CERTO

