# Desenvolvimento de Software - Algoritmos

Índice

1) Métodos de Ordenação - Conceitos Básicos - Teoria

2) Métodos de Ordenação - Complexidade de Algoritmos - Teoria

3) Métodos de Ordenação - Pesquisa de Dados - Teoria

4) Métodos de Ordenação - Conceitos Básicos - Questões Comentadas

5) Métodos de Ordenação - Complexidade de Algoritmos - Questões Comentadas

6) Métodos de Ordenação - Pesquisa de Dados - Questões Comentadas

7) Métodos de Ordenação - Conceitos Básicos - Lista de Questões

8) Métodos de Ordenação - Complexidade de Algoritmos - Lista de Questões

9) Métodos de Ordenação - Pesquisa de Dados - Lista de Questões

MÉToDoS DE ORDENAçÃo ewveviSTA
WWW.VIDADEHIPSTEP.COM.8P

Métodos de Ordenação são algoritmos que têm o objetivo principal de posicionar os elementos de uma estrutura de dados em uma determinada ordem. Para que, professor? Ora, isso possibilita o acesso mais rápido e eficiente aos dados. Existem dezenas de métodos, todavia nessa aula veremos apenas os mais importantes: BubbleSort, QuickSort, InsertionSort,SelectionSort,
MergeSort, ShellSort e HeapSort.

Antes de iniciar, vamos falar sobre o conceito de Estabilidade! Um método estável é aquele em que os itens com chaves iguais mantêm-se com a posição inalterada durante o processo de ordenação, i.e., preserva-se a ordem relativa dos itens com chaves duplicadas ou iguais. MétodosEstáveis: Bubble, Insertion e Merge; Métodos Instáveis: Selection, Quick, Heap e Shell.
Vejamos um exemplo:
/ 49

/

Na imagem acima, foi colocado um sinal de aspas simples e duplas apenas para diferenciá-los,mas trata-se do mesmo número. Um algoritmo estável ordena todo o restante e não perde tempo trocando as posições de elementos que possuam chaves idênticas. Já um algoritmo instável ordena todos os elementos, inclusive aqueles que possuem chaves idênticas (sob algum outro critério).
x' 4

/ 49

/

Esse algoritmo é o primeiro método de ordenação aprendido na faculdade, porque ele é bastante simples e intuitivo. Nesse método, os elementos da lista são movidos para as posições adequadas de forma contínua. Se um elemento está inicialmente em uma posição i e, para que a lista fique ordenada, ele deve ocupar a posição j, então ele terá que passar por todas as posições entre i e j.
Em cada iteração do método, percorremos a lista a partir de seu início comparando cada elemento com seu sucessor, trocando-se de posição se houver necessidade. É possível mostrar que,se a lista tiver n elementos, após no máximo (n-1) iterações, a lista estará em ordem(crescente ou decrescente). Observem abaixo o código para a Ordenação em Bolha:
ALGORITMO BOLHA

ENTRADA: UM VETOR L COM N POSIÇÕES
SAÍDA: O VETOR L EM ORDEM CRESCENTE

PARA i = 1 até n-1

PARA j = 0 até n - 1 - i
SE L[j] > L[j + 1]

AUX = L[j] // SWAP
L[j] = L[j+1]

L[j+1] = AUX
FIM {BOLHA}

Melhor Caso Caso Médio Pior Caso

[Õ(nj | O(n²) | O(n²)
|

InsertionSort (Inserção)

Esse algoritmo, também conhecido como Inserção Direta, é bastante simples e apresenta um desempenho significativamente melhor que o BubbleSort, em termos absolutos. Além disso, ele é extremamente eficiente para listas que já estejam substancialmente ordenadas e listas com pequeno número de elementos. Observem abaixo o código para a Ordenação de Inserção:
ALGORITMO INSERÇÃO

ENTRADA: UM VETOR L COM N POSIÇÕES
SAÍDA: 0 VETOR L EM ORDEM CRESCENTE

PARA i = 1 até n-1
PIVO = L[i]

j = i - 1

ENQUANTO j 0 e L[j] > PIVO
L[j+1] = L[j]

j = j - 1

L[ j + 1] = PIVO
FIM {INSERÇÃO}

9 6 2 9 1

XI

6 9 2 9 1

x\

2 6 9 9 1

2 6 9 9 1

1 2 6 9 9

Nesse método, consideramos que a lista está dividida em parte esquerda, já ordenada, e parte direita, em possível desordem. Inicialmente, a parte esquerda contém apenas o primeiro elemento da lista. Cada iteração consiste em inserir o primeiro elemento da parte direta (pivô)na posição adequada da parte esquerda, de modo que a parte esquerda continue ordenada.
É fácil perceber que se a lista possui n elementos, após (n-1) inserções, ela estará ordenada. Para inserir o pivô, percorremos a parte esquerda, da direita para a esquerda, deslocando os elementos estritamente maiores que o pivô uma posição para direita. O pivô deve ser colocado imediatamente à esquerda do último elemento movido.
Melhor Caso Caso Médio Pior Caso

[Õ(nj |pÕ(rP)| P0(n2j
|

SelectionSort (Seleção)

9 6 2 $3 1

><

1 6 2 $) 9

A

1 2 6 $3 9

1 2 6 í 3 9

1 2 6 $3 9

/ 49

/

Esse algoritmo consiste em selecionar o menorl elemento de um vetor e trocá-lo (swap)
pelo item que estiver na primeira posição, i.e., inseri-lo no início do vetor. Essas duas operações são repetidas com os itens restantes até o último elemento. Tem como ponto forte o fato de que realiza poucas operações de swap. Seu desempenho costuma ser superior ao BubbleSort e inferior ao InsertionSort.
Assim como no InsertionSort, considera-se que a lista está dividida em parte esquerda, já ordenada, e parte direita, em possível desordem. Ademais, os elementos da parte esquerda são todos menores ou iguais aos elementos da parte direita. Cada iteração consiste em selecionar o menor elemento da parte direita (pivô) e trocá-lo com o primeiro elemento da parte direita.
Assim, a parte esquerda aumenta, visto que passa a incluir o pivô, e a parte direita diminui. Note que o pivô é maior que todos os demais elementos da parte esquerda, portanto a parte esquerda continua ordenada. Ademais, o pivô era o menor elemento da direita, logo todos os elementos da esquerda continuam sendo menores ou iguais aos elementos da direita. Inicialmente, a parte esquerda é vazia.
ALGORITMO SELEÇÃO

ENTRADA: UM VETOR L COM N POSIÇÕES
SAÍDA: O VETOR L EM ORDEM CRESCENTE

PARA i = 0 ate n - 2
MIN = i

PARA j = i + 1 até n - 1
SE L[j] < L[MIN]

MIN= j

TROCA(L [i], L[MIN])
FIM {SELEÇÃO}

Melhor Caso Caso Médio Pior Caso

HÕ(n2j IÕ(^jI P0(n2j
|

QuickSort (Troca)

1 A definição formal afirma que é o maior valor; a maioria das implementações utiliza o menor valor. As questões de prova cobram algumas vezes o maior, outras vezes o menor.
p

2 7 3 1 5 8 4 5

,m p

2 7 3 1 5 8 4 5

P V

2 3 7 1 5 8 4 5

nAi P

2 3 1 7 5 8 4 5

m i p
2 3 1 7 5 8 4 5

m i p
2 3 1 7 5 8 4 5

P

2 3 1 4 6 8 7 5

2 3 1 4 5 8 7 6

Esse algoritmo divide um conjunto de itens em conjuntos menores, que são ordenados de forma independente, e depois os resultados são combinados para produzir a solução de ordenação do conjunto maior. Trata-se, portanto, de um algoritmo do tipo Divisão-e-Conquista,i.e., repartindo os dados em subgrupos, dependendo de um elemento chamado pivô.
Talvez seja o método de ordenação mais utilizado! Isso ocorre porque quase sempre ele é significativamente mais rápido do que todos os demais métodos de ordenação baseados em comparação. Ademais, suas características fazem com que ele, assim como o MergeSort,possa ser facilmente paralelizado. Ele também pode ser adaptado para realizar ordenação externa(QuickSort Externo).

Neste método, a lista é dividida em parte esquerda e parte direita, sendo que os elementos da parte esquerda são todos menores que os elementos da parte direita. Essa fase do processo é chamada de partição. Em seguida, as duas partes são ordenadas recursivamente (usando o próprioQuickSort). A lista está, portanto, ordenada corretamente!

Uma estratégia para fazer a partição é escolher um valor como pivô e então colocar na parte esquerda os elementos menores ou iguais ao pivô e na parte direita os elementos maiores que o pivô - galera, a escolha do pivô é crítica! Em geral, utiliza-se como pivô o primeiro elemento da lista, a despeito de existirem maneiras de escolher um "melhor" pivô.
Esse algoritmo é um dos métodos mais rápidos de ordenação, apesar de às vezes partições desequilibradas poderem conduzir a uma ordenação lenta. A eficácia do método depende da escolha do pivô mais adequado ao conjunto de dados que se deseja ordenar.Alguns, por exemplo, utilizam a mediana de três elementos para otimizar o algoritmo.
Alguns autores consideram a divisão em três subconjuntos, sendo o terceiro contendo valores iguais ao pivô. O Melhor Caso ocorre quando o conjunto é dividido em subconjuntos de mesmo
/ 49

/

tamanho; o Pior Caso ocorre quando o pivô corresponde a um dos extremos (menor ou maior valor). Alguns o consideram um algoritmo frágil e não-estável, com baixa tolerância a erros.
PROCEDIMENTO PARTIÇÃO

ENTRADA: UM VETOR L E AS POSIÇÕES INICIO E FIM
SAÍDA:j, tal que L[INICIO]..L[j-1] < L[j] e

L[j+1 ] . . L [FIM] > L[j]

// j é a posição onde será colocado o pivô, como

// ilustrado na figura abaixo

PIVO = HINICIO], i = INICIO + 1, j = FIM
ENQUANTO i £ j

ENQUANTO i £ j e L[i] <> PIVO

i = i + 1

ENQUANTO L[j] > PIVO

j = j - 1
SE i £ j

TROCA(L[i],L[j])

i = i + 1, j = j - 1
TROCA(L[INICIO], L[j])
DEVOLVA j

FIM {PARTIÇÃO}

Melhor Caso Caso Médio Pior Caso

O(n log n) O(n log n) fÕ(n2j
|

ShellSort (Inserção)

Esse algoritmo é uma extensão ou refinamento do algoritmo do InsertionSort,
contornando o problema que ocorre quando o menor item de um vetor está na posição mais à direita.Ademais,
difere desse último pelo fato de, em vez de considerar o vetor a ser ordenado como um único segmento, ele considera vários segmentos e aplica o InsertionSort em cada um deles.
É o algoritmo mais eficiente dentre os de ordem quadrática. Nesse método, as comparações e as trocas são feitas conforme determinada distância (gap) entre dois elementos, de modo que, se gap = 6, há comparação entre o 1o e 7o elementos ou entre o 2o e8o elementos e assim sucessivamente, repetindo até que as últimas comparações e trocas tenham sido efetuadas e o gap tenha chegado a 1.
/ 49

/

ALGORITMO SHELLSORT

ENTRADA.- UM VETOR L COM N POSIÇÕES

SAÍDA.- O VETOR L EM ORDEM CRESCENTE

H = 1

ENQUANTO H < n FAÇA H = 3 * H + 1
FAÇA

H = H / 3 // divisão inteira

PARA i = H até n - 1 // Inserção adaptado para h-listas
PIVO = L[i]

j = i - H

ENQUANTO j £ 0 e L[j] > PIVO
L[j + H] = L[j]

j= j " H

L[j + H] = PIVO
ENQUANTO H > 1

FIM (SHELLSORT)

Melhor Caso Caso Médio Pior Caso

O(n log n) Depende do gap fÕ(n2j
|

Esse algoritmo é baseado na estratégia de resolução de problemas conhecida como divisão-e-conquista. Essa técnica consiste basicamente em decompor a instância a ser resolvida em instâncias menores do mesmo tipo de problema, resolver tais instâncias (em geral,recursivamente)
e por fim utilizar as soluções parciais para obter uma solução da instância original.

Naturalmente, nem todo problema pode ser resolvido através de divisão e conquista. Para que seja viável aplicar essa técnica a um problema, ele deve possuir duas propriedades estruturais. Oproblema deve ser decomponível, i.e., deve ser possível decompor qualquer instância não trivial do problema em instâncias menores do mesmo tipo de problema.
/ 49

/

Além disso, deve ser sempre possível utilizar as soluções obtidas com a resolução das instâncias menores para chegar a uma solução da instância original. No MergeSort, divide-se a lista em duas metades. Essas metades são ordenadas recursivamente (usando o próprio MergeSort)e depois são intercaladas. Abaixo segue uma possível solução:
ALGORITMO MERGESORT

ENTRADA: UM VETOR L E AS POSIÇÕES INICIO E FIM

SAÍDA: O VETOR L EM ORDEM CRESCENTE DA POSIÇÃO INICIO ATÉ
A POSIÇÃO FIM

SE inicio < fim meio = (inicio + fim)/2 // divisão inteiraSE inicio < meio

MERGESORT(L, inicio, meio)
SE meio + 1 < fim

MERGESORT (L, meio + 1, fim)
MERGE(L, inicio, meio, fim)

FIM {MERGESORT}

Melhor Caso Caso Médio Pior Caso

O(n log n) O(n log n) O(n log n)

estrutura.

Assim, ao final das inserções, os elementos podem ser sucessivamente removidos da raiz da heap,na ordem desejada.

Essa estrutura pode ser representada como uma árvore ou como um vetor.
Entenderam?
Inicialmente, insere-se os elementos da lista em um heap.

Em seguida, fazemos sucessivas remoções do menor elemento do heap, colocando os elementos removidos do heap de volta na lista - a lista estará então em ordem crescente.
O heapsort é um algoritmo de ordenação em que a sua estrutura auxiliar de armazenamento fora do arranjo de entrada é constante durante toda a sua execução.
/ 49

/

ALGORITMO HEAP SORT

ENTRADA: UM VETOR L COM N POSIÇÕES
SAÍDA: O VETOR L EM ORDEM CRESCENTE

inicialize um HBC H com n posições
PARA i = 0 até n - 1

INSERE-HBC(H, L[i] )

PARA i = 0 até n - 1
L[i] = REMOVE_MENOR(H)

FIM {HEAP SORT}

Melhor Caso Caso Médio Pior Caso

O(n log n) O(n log n) O(n log n)

Resumão de Complexidades

ALGORITMO MELHOR CASO CASO MÉDIO PIOR CASO

BubbleSort O(n) O(n2)
O(n2)

InsertionSort O(n) O(n2)
O(n2)

SelectionSort O(n2) O(n2) O(n2)
QuickSort O(n log n) O(n log n) O(n2)
ShellSort O(n log n) Depende do gap O(n2)
MergeSort O(n log n) O(n log n) O(n log n)
HeapSort O(n log n) O(n log n) O(n log n)
CoMPLEXIDADE DE ALGoRITMoS

Galera, por que estudamos a complexidade de algoritmos? Para determinar o custo computacional (tempo, espaço, etc) para execução de algoritmos. Em outras palavras, ela classifica problemas computacionais de acordo com sua dificuldade inerente. E importante entender isso para posteriormente estudarmos a complexidade de métodos de ordenação e métodos de pesquisa.
Nosso estudo aqui será bastante superficial por duas razões: primeiro, concursos cobram pouco e, quando cobram, querem saber as complexidades dos métodos de ordenação mais conhecidos;segundo, essa é uma disciplina absurdamente complexa que envolve Análise Assintótica,
Cálculo
Diferencial, Análise Polinomial (Linear, Exponencial, etc). Logo, vamos nos ater ao que cai em concurso público!
Só uma pausa: passei dias sem dormir na minha graduação por conta dessa disciplina!
Na UnB, ela era ministrada pelo Instituto de Matemática e era considerada a disciplina mais difícil do curso :-(.Continuando: lá em cima eu falei sobre custo computacional! Ora, para que eu escolha um algoritmo, eu preciso definir algum parâmetro.
Podemos começar com Tempo! Um algoritmo que realiza uma tarefa em 20 minutos é melhor do que um algoritmo que realiza uma tarefa em 20 dias? Não é uma boa estratégia, porque depende do computador que eu estou utilizando (e todo o hardware correspondente),depende das otimizações realizadas pelo compilador, entre outras variáveis.
Vamos analisar, então, Espaço! Um algoritmo que utiliza 20Mb de RAM é melhor do que um algoritmo que utiliza 20Gb? Seguem os mesmos argumentos utilizados para o Tempo,ou seja,
não é uma boa opção! E agora, o que faremos? Galera, eu tenho uma sugestão:
investigar a quantidade de vezes que operações são executadas na execução do algoritmo!
Essa estratégia independe do computador (e hardware associado), do compilador, da linguagem de programação, das condições de implementação, entre outros fatores - ela depende apenas da qualidade inerente do algoritmol implementado. Utilizam-se algumas simplificações matemáticas para se ter uma ideia do comportamento do algoritmo. Prosseguindo...
Dada uma entrada de dados de tamanho N, podemos calcular o custo computacional de um algoritmo em seu pior caso, médio caso e melhor caso! Como assim, professor? Para entender isso, vamos utilizar a metáfora de um jogo de baralho! Imaginem que eu estou jogando contra vocês. Vocês embaralham e me entregam 5 cartas, eu embaralho novamente e lhes entrego cartas.
Quem joga baralho sabe que uma boa alternativa para grande parte dos jogos é ordenar as cartas em ordem crescente de modo a encontrar mais facilmente a melhor carta para jogar. Agora observem... vocês receberam as seguintes cartas (nessa ordem): 4, 5, 6, 7, 8. Já eu recebi as
1 Pessoal, é claro que nossa visão sobre a complexidade dos algoritmos é teórica. Na prática,
depende de diversos outros fatores,
mas nosso foco é na visão analítica e, não, empírica.

/ 49

/

seguintes cartas (também nessa ordem): 8, 7, 6, 5, 4 - nós queremos analisar a complexidade de ordenação dessas cartas.
Ora, convenhamos que vocês possuem o melhor caso, porque vocês deram a sorte de as cartas recebidas já estarem ordenadas. Já eu peguei o pior caso, porque as cartas estão ordenadas na ordem inversa. Por fim, o caso médio ocorre caso as cartas recebidas estejam em uma ordem aleatória. Com isso, espero que vocês tenham entendido o sentido de pior, médio e melhor casos.
Vamos partir agora para o estudo da Notação Big-O (ou Notação
Assintótica)! Isso é simplesmente uma forma de representar o comportamento assintótico de uma função. No nosso contexto, ela busca expressar a quantidade de operações primitivas executadas como função do tamanho da entrada de dados. Vamos ver isso melhor!
A Notação Big-O é a representação relativa da complexidade de um algoritmo. É relativa porque só se pode comparar maçãs com maçãs, isto é, você não pode comparar um algoritmo de multiplicação aritmética com um algoritmo de ordenação de inteiros. É uma representação porque reduz a comparação entre algoritmos a uma simples variável por meio de observações e suposições.
E trata da complexidade porque se é necessário 1 segundo para ordenar
10.000 elementos,
quanto tempo levará para ordenar 1.000.000? A complexidade, nesse exemplo particular, é a medida relativa para alguma coisa. Vamos ver isso por meio de um exemplo: soma de dois inteiros!A soma é uma operação ou um problema, e o método para resolver esse problema é chamado algoritmo!
Transporte —> 1 1

Parcela 1 —> 1

10 1

Soma 1 10 0 0

Vamos supor que no algoritmo de somar (mostrado acima), a operação mais cara seja a adição.Observem que se somarmos dois números de 100 dígitos, teremos que fazer 100
adições. Se somarmos dois números de 10.000 dígitos, teremos que fazer 10.000 adições.Perceberam o padrão? A complexidade (aqui, número de operações) é diretamente proporcional ao número n de dígitos, i.e., O(n).
/ 49

/

Quando dizemos que um algoritmo é O(n2), estamos querendo dizer que esse algoritmo é da ordem de grandeza quadrática! Ele basicamente serve para te dizer quão rápido uma função cresce, por exemplo: um algoritmo O(n) é melhor do que um algoritmo O(n2), porque ela cresce mais lentamente! Abaixo vemos uma lista das classes de funções mais comuns em ordem crescente de crescimento:
Notação Nome

0(1) Constante

O(log n) Logarítmica
O[(log n)c] Polilogarítmica
O(n) Linear

O(n log n) -

O(n2) Quadrática

O(n3) Cúbica

O(nc) Polinomial

O(cn) Exponencial

O(n!) Fatorial

Quando dizemos que o Shellsort é um algoritmo O(n2), estamos querendo dizer que a complexidade (nesse caso, o número de operações) para ordenar um conjunto de n dados com oAlgoritmo Shellsort é proporcional ao quadrado do número de elementos no conjunto! Grosso modo, para ordenar 20 números, é necessário realizar 400 operações (sem entrar em detalhes sobre a operação em si, nem sobre as simplificações matemáticas que são realizadas).
Entender como se chega a esses valores para cada método de ordenação e pesquisa é extremamente complexo! Galera, apesar de eu nunca ter visto isso em prova, é bom que vocês saibam que existem outras notações! Utiliza-se Notação Big-O (O) para pior caso;Notação Big-
Ômega para melhor caso (Q); e Notação Big-Theta (0) para caso médio.

Como na prática utiliza-se Big-O para tudo, o que eu recomendo (infelizmente, porque eu sei que vocês têm zilhões de coisas para decorar) é memorizar o pior caso dos principais métodos. Dessa forma, é possível responder a maioria das questões de prova sobre esse tema.Eventualmente, as questões pedem também caso médio e melhor caso, mas é menos comum. Bacana? :-)
/ 49

/

Por último, uma pergunta muito frequente: Professor, já vi questões cobrando Logaritmo na Base10, Logaritmo na Base 2, Logaritmo Neperiano, etc... isso não está errado? Galera,
suponha que um algoritmo levou um tempo 0(log1O n). Você também poderia dizer que levou um tempo0(lg n) (ou seja, 0(log2 n)). Você pode utilizar qualquer base.
Sempre que a base do logaritmo é uma constante, não importa a base que usamos na notação assintótica. Por que não? Porque, para a notação assintótica, isso é completamente irrelevante.Beleza? Então, não se prendam a base do logaritmo, qualquer uma pode ser utilizada na representação de complexidade assintótica de algoritmos. Bacana? Exercícios...
/ 49

/

PESQUISA DE DADoS

Uma das tarefas de maior importância na computação é a pesquisa de informações contidas em coleções de dados. Em geral, desejamos que essa tarefa seja executada sem que haja a necessidade de inspecionar toda a coleção de dados. Existem algumas maneiras de realizar pesquisas, tais como: Pesquisa Sequencial, Pesquisa Binária, Tabelas de Dispersão(Hashing),
Árvores AVL, Árvores B e Árvores B+.

Busca Sequencial

Galera, imaginem que eu estou à procura de um valor X em um vetor L[
]! Para tal, posso inspecionar as posições sequenciais de L[ ] a partir da primeira posição: se eu encontrar X, minha busca tem êxito; se eu alcanço a última posição e não encontro X, concluímos que esse valor não ocorre no vetor L[ ]. Como é chamada essa busca em que eu inspeciono uma estrutura posição por posição? Sequencial ou Linear.
Considerando que o vetor L[ ] contém N elementos, ordenados ou não, é fácil verificar que a busca sequencial requer tempo linearmente proporcional ao tamanho do vetor, i.e., da ordemO(n). Por conta disso, é comum dizer que a busca sequencial é uma Busca Linear. Entenderam?Quanto maior o vetor, maior o tempo em média para buscar um elemento! Quanto mais ao final,mais demorado.
A Busca Sequencial é muito lenta para grandes quantidades de dados, mas aceitável para listas pequenas e que mudam constantemente. Observa-se que no Melhor Caso, X está na primeira posição, logo necessita apenas de uma comparação; no Pior Caso, X está na última posição, logo necessita de N comparações; e no Caso Médio, X é encontrado após (n+1 )/2 comparações.
A seguir, encontram-se dois algoritmos para realização de uma Busca Sequencial:
o primeiro ocorre de forma simples e o segundo ocorre de forma recursiva. Galera, para vetores de médio ou grande porte, o tempo de busca sequencial é considerado completamente inaceitável, dado que existem técnicas mais eficientes! Professor, me dá um exemplo? Claro, veremos adiante: BuscaBinária!

PROCEDIMENTO BUSCA SEQUENCIAL ( L , X , POS )

ENTRADA: UM VETOR L e UM VALOR X

SAÍDA: POS =1, SE X OCORRE NA POSIÇÃO i DE L // SUCESSO
POS = 0, CASO CONTRÁRIO.

POS - 0

PARA i = 1 até N
SE L[i] = X

POS = i
ESCAPE

//fim para
DEVOLVA POS

FIM (BUSCASEQUENCIAL}

*

PROCEDIMENTO BUSCA_SEQUENCIAL_REC ( L , N, X )

ENTRADA: UM VETOR L DE TAMANHO N e UM VALOR X
SAÍDA: i, SE X OCORRE NA POSIÇÃO i DE L // SUCESSO

0, CASO CONTRÁRIO.

SE N == 1

SE L[l] = X

DEVOLVA 1

SENÃO

DEVOLVA 0

SENÃO

SENÃO

SE L[N] = X

DEVOLVA N

BUSCASEQUENCIALREC ( L , N-l, X )

FIM {BUSCA SEQUENCIAL REC}

Busca Binária

A Busca Binária é um algoritmo de busca em vetores que segue o paradigma de divisão-e-conquista. Parte-se do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca, comparando o elemento chave com o elemento do meio do vetor. Possui complexidade da ordem de O(log2 n), em que N é o tamanho do vetor de busca.
Quando o Vetor L[ ] estiver em ordem crescente, podemos determinar se X ocorre em L[
] de forma mais rápida da seguinte forma: inspeciona-se a posição central do vetor! Se essa posição já contiver X, a busca para! Por que, professor? Porque nós já encontramos X! Se X for menor que esse elemento central, passamos a procurar X, recursivamente, no intervalo de L[ ] que se encontra à esquerda da posição central.
Se X for maior do que o elemento central, continuamos a procurar X, recursivamente,
no intervalo de L que está à direita da posição central. Se o intervalo se tornar vazio, a busca para, tendo sido malsucedida. Esse procedimento é conhecido como Busca Binária e, facilmente, pode-se adaptar a busca em ordem decrescente. Segue abaixo um possível algoritmo:
PROCEDIMENTO BUSCA_BINARIA

ENTRADA: UM VETOR L EM ORDEM CRESCENTE, UM VALOR X, E AS
POSIÇÕES INICIO E FIM.

SAÍDA: SIM, SE X OCORRE ENTRE AS POSIÇÕES INICIO E FIM DE
L; NÃO, CASO CONTRÁRIO.

SE INICIO > FIM
DEVOLVA NÃO E PARE

MEIO = (INICIO+FIM)/2 // DIVISÃO INTEIRA
SE X = L[MEIO]

DEVOLVA SIM E PARE
SE X < L[MEIO]

DEVOLVA BUSCA_BINARIA(L, X, INICIO, MEIO - 1)
SENÃO

DEVOLVA BUSCA_BINARIA(L, X, MEIO + 1, FIM)
FIM {BUSCA_BINARIA}

Na imagem abaixo, estamos à procura do valor 23! Em vermelho, encontra-se o elemento inicialL[0] = 2 e, em amarelo, encontra-se o elemento final L[N-1] = 57. Procuramos, então,
o elemento central! Como? Ele é o elemento de índice [0 + (N-1)]/2 = 7/2 = 3,5 = 3(Arredonda-se para baixo).
Ora, L[3] = 19! Encontramos? Não, 23>19! Sendo assim, L[0] = 19 e L[4] = 57.

Procuramos, então, o elemento central! Como? Ele é o elemento de índice [0 + (N-1)]/2
= 4/2 =

2. Ora, L[2] = 51! Encontramos? Não, 23<51! Sendo assim, L[0] = 19 e L[2] = 51.
Procuramos, então,
o elemento central! Como? Ele é o elemento de índice [0+ (N-1)]/2 = 2/2 = 1. Ora,
L[1] = 23!
Encontramos? Sim! Então, nossa busca obteve êxito e encontramos o que buscávamos.

/ 49

/

QUESTõES CoMENTADAS - MÉToDoS DE ORDENAçÃo -
MULTIBANCAS

1. (Instituto Cidades - 2012 - TCM-GO - Auditor de Controle Externo -
Informática) São exemplos de algoritmos de ordenação, exceto:
a) Bubble Sort b) Select Sort c) Shell Sort d) Busca Sequencial;
e) Quick Sort;

Comentários:

Conforme vimos em aula, a Busca Sequencial não é um algoritmo de ordenação! Na verdade, ele é um método de pesquisa sobre estruturas de dados. Gabarito: D
2. (FUMARC - 2012 - TJ-MG - Técnico Judiciário - Analista de Sistemas - I)
Quicksort divide um conjunto de itens em conjuntos menores, que são ordenados de forma independe, e depois os resultados são combinados para produzir a solução de ordenação do conjunto maior.
Comentários:

Conforme vimos em aula, está perfeito! Sendo um algoritmo do tipo Dividir Para
Conquistar, ele reparte o conjunto de dados em conjuntos menores, que são ordenados independentemente e depois combinados em uma solução maior. Gabarito: C
3. (CESPE - 2012 - MPE-PI - Analista Ministerial - Informática - Cargo
6) O heapsort é um algoritmo de ordenação em que a quantidade de elementos armazenada fora do arranjo de entrada é constante durante toda a sua execução.
Comentários:

Inicialmente, insere-se os elementos da lista em um heap. Em seguida, fazemos sucessivas remoções do menor elemento do heap, colocando os elementos removidos do heap de volta na lista - a lista estará então em ordem crescente. O heapsort é um algoritmo de ordenação em que a sua estrutura auxiliar de armazenamento fora do arranjo de entrada é constante durante toda a sua execução.
Essa questão é polêmica. O arranjo tem tamanho constante, mas a quantidade de elementos é variável. Diferente de outros algoritmos de ordenação que tem uma estrutura auxiliar de tamanho variável (assim como seus elementos), o Heap Sort tem uma estrutura auxiliar de tamanho fixo(porém a quantidade de elementos é variável). Como é dito por Neil Dale: "A heapsort is just as
/ 49

/

efficient in terms of space; only one array is used to store the data. The heap sort requires only constante extra space". No entanto, a questão foi dada como correta! Gabarito: C
4. (CESPE - 2010 - ABIN - Oficial Técnico de Inteligência - Área de Suporte a
Rede de Dados)
A eficácia do método de ordenação rápida (quicksort) depende da escolha do pivô mais adequado ao conjunto de dados que se deseja ordenar. A situação ótima ocorre quando o pivô escolhido é igual ao valor máximo ou ao valor mínimo do conjunto de dados.
Comentários:

Alguns autores consideram a divisão em três subconjuntos, sendo o terceiro contendo valores iguais ao pivô. O Melhor Caso ocorre quando o conjunto é dividido em subconjuntos de mesmo tamanho; o Pior Caso ocorre quando o pivô corresponde a um dos extremos (menor ou maior valor). Alguns o consideram um algoritmo frágil e não-estável, com baixa tolerância a erros.
Conforme vimos em aula, a questão se refere ao pior caso! Gabarito: E

5. (CESPE - 2010 - ABIN - Oficial Técnico de Inteligência - Área de Suporte a
Rede de Dados)
A estabilidade de um método de ordenação é importante quando o conjunto de dados já está parcialmente ordenado.
Comentários:

Na imagem acima, foi colocado um sinal de aspas simples e duplas apenas para diferenciá-los,mas trata-se do mesmo número. Um algoritmo estável ordena todo o restante e não perde tempo trocando as posições de elementos que possuam chaves idênticas. Já um algoritmo instável ordena todos os elementos, inclusive aqueles que possuem chaves idênticas (sob algum outro critério).
Conforme vimos em aula, a estabilidade é irrelevante com dados parcialmente ordenados ou não!A estabilidade é importante quando se deseja ordenar um conjunto de dados por mais de um critério (Ex: primeiro pelas chaves e segundo por índices). Se esse não for o caso(e a questão não disse que era!), a estabilidade "não fede nem cheira". O fato de os dados estarem parcialmente ordenados não fará diferença em termos de ordenação - ambos serão ordenados da mesma maneira. Gabarito: E
6. (CESPE - 2010 - Banco da Amazônia - Técnico Científico - Tecnologia da Informação -Administração de Dados) A classificação interna por inserção é um método que realiza a ordenação de um vetor por meio da inserção de cada elemento em sua posição correta dentro de um subvetor classificado.
Comentários:

Conforme vimos em aula, trata-se do InsertionSort! Gabarito: C

/ 49

/

7. (FCC - 2009 - TRT - 15a Região - Analista Judiciário - Tecnologia da Informação) São algoritmos de classificação por trocas apenas os métodos:
a) SelectionSort e InsertionSort.

b) MergeSort e BubbleSort.

c) QuickSort e SelectionSort.

d) BubbleSort e QuickSort.

e) InsertionSort e MergeSort.

Comentários:

Conforme vimos em aula, BubbleSort e QuickSort são métodos de troca;
InsertionSort é um método de Inserção; SelectionSort e HeapSort são métodos de Seleção; eMergeSort é um método de Intercalação. Gabarito: D
8. (CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - I) O tempo de pior caso do algoritmo QuickSort é de ordem menor que o tempo médio do algoritmo Bubblesort.
Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, está incorreto! São iguais: O(n2). Gabarito: E

9. (CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - II) O tempo médio doQuickSort é O(nlog2n), pois ele usa como estrutura básica uma árvore de prioridades.

Comentários:

, 49

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

cQuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, de fato, ele tem tempo médio O(n log n), mas ele usa como estrutura básica uma lista ou um vetor! Gabarito: E
10.(CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - III) O tempo médio doQuickSort é de ordem igual ao tempo médio do MergeSort.

Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, ambos têm tempo O(n log n). Gabarito: C

11 .(CESGRANRIO - 2012 - CMB - Analista de Sistemas - III) Em uma reunião de análise de desempenho de um sistema WEB, um programador apontou corretamente que a complexidade de tempo do algoritmo bubblesort, no pior caso, é:
a) 0(1)

x'

/ 49

/

b) O(log n)

c) O(n)

d) O(n log n)

e) O(n2)

Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, trata-se de O(n2)! Gabarito: E

12.(CESPE - 2010 - INMETRO - Analista de Sistemas) Se f é uma função de complexidade para um algoritmo F, então O(f) é considerada a complexidade assintótica ou o comportamento assintótico do algoritmo F. Assinale a opção que apresenta somente algoritmos que possuem complexidade assintótica quando f(n) = O(n log n).
a) HeapSort e BubbleSort b) QuickSort e InsertionSort c) MergeSort e BubbleSort d) InsertionSort e) HeapSort, QuickSort e MergeSort
Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

/ 49

/

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, trata-se da última opção. Vejam que ele não utilizou, nessa questão, oPior Caso. Gabarito: E

13.(FGV - 2013 - MPE/MS - Analista de Sistemas) Assinale a alternativa que indica o algoritmo de ordenação capaz de funcionar em tempo O(n) para alguns conjuntos de entrada.
a) Selectionsort (seleção)

b) Insertionsort (inserção)

c) Merge sort d) Quicksort e) Heapsort
Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, trata-se da segunda opção. Gabarito: B

14.(CESGRANRIO - 2010 - BACEN - Analista de Sistemas) Uma fábrica de software foi contratada para desenvolver um produto de análise de riscos. Em determinada funcionalidade desse software, é necessário realizar a ordenação de um conjunto formado por muitos números inteiros. Que algoritmo de ordenação oferece melhor complexidade de tempo (Big O notation) no pior caso?
a) Merge sort b) Insertion sort c) Bubble sort d) Quick sort e) Selection sort
Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, trata-se da primeira opção! Gabarito: A

15.(CESPE - 2011 - FUB - Analista de Sistemas) Os métodos de ordenação podem ser classificados como estáveis ou não estáveis. O método é estável se preserva a ordem relativa de dois valores idênticos. Alguns métodos eficientes como shellsort ou quicksort não são estáveis, enquanto alguns métodos pouco eficientes, como o método da bolha,são estáveis.

Comentários:

Métodos Estáveis: BubbleSort, InsertionSort e MergeSort; Métodos Instáveis:
SelectionSort,
QuickSort, HeapSort e ShellSort. Portanto, item perfeito! Gabarito: C

16.(CESPE - 2012 - BASA- Analista de Sistemas) O método de classificação
Shellsort iguala-
se ao método Quicksort em termos de complexidade temporal, porém é mais eficiente para quantidades pequenas a moderadas de dados.
Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

, 49

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Não, a complexidade temporal é completamente diferente! A complexidade que nós estudamos em aula se trata do comportamento do algoritmo em termos de custo - ela fornece uma resposta digamos que "genérica". Por que? Porque são ignorados constantes, parâmetros,etc - perceba que nós dizemos, por exemplo, que o algoritmo x tem complexidade O(n2). O que isso significa?Significa apenas que esse algoritmo tem um custo polinomial, mas nós sabemos que funções polinomiais têm o formato ax2 + bx + c. Onde está o a, bx, c? Nós ignoramos e ficamos apenas com o parâmetro mais importante. Além disso tudo, ainda temos que considerar que existe o pior caso, melhor caso e caso médio.
Para saber a complexidade temporal de um algoritmo de ordenação, nós temos que nos focar em diversos parâmetros. Além das constantes e parâmetros da função que representa a complexidade, nós temos que levar em consideração aspectos práticos (Por exemplo: o hardware em que será rodado o programa). Resumindo nosso papo: não há correlação direta entre complexidade de custo e complexidade temporal, logo eu não posso usar a função de um para calcular o outro. Gabarito: E
17.(CESPE - 2012 - BASA - Analista de Sistemas) O método de classificação
Quicksort é estável e executado em tempo linearmente dependente da quantidade de dados que estão sendo classificados.
Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, QuickSort é instável e não possui complexidade temporal linear!Gabarito: E

18.(CESPE - 2012 - BASA - Analista de Sistemas) No método de ordenamento denominado shellsort, as comparações e as trocas são feitas conforme determinada distância entre dois elementos, de modo que, uma distância igual a 6 seria a comparação entre o primeiro elemento e o sétimo, ou entre o segundo elemento e o oitavo, e assim sucessivamente,repetindo-se esse processo até que as últimas comparações e trocas tenham sido efetuadas e a distância tenha diminuído até chegar a 1.
Comentários:

É o algoritmo mais eficiente dentre os de ordem quadrática. Nesse método, as comparações e as trocas são feitas conforme determinada distância (gap) entre dois elementos, de modo que, se gap = 6, há comparação entre o 1° e 7o elementos ou entre o 2° e8o elementos e assim sucessivamente, repetindo até que as últimas comparações e trocas tenham sido efetuadas e o gap tenha chegado a 1.
Conforme vimos em aula, a questão descreveu perfeitamente o mecanismo de ordenação doShellsort. Gabarito: C

19.(FGV - 2008 - PETROBRÁS - Analista de Sistemas) Sobre o algoritmo de ordenação heapsort, assinale a afirmação correta.
a) Utiliza ordenação por árvore de decisão, ao invés de ordenação por comparação.

b) A estrutura de dados que utiliza, chamada heap, pode ser interpretada como uma árvore binária.
c) Seu desempenho de pior caso é pior do que o do algoritmo quicksort.

d) Seu desempenho de pior caso é o mesmo da ordenação por inserção.

e) Seu desempenho de pior caso é menor do que o da ordenação por intercalação.

Comentários:

(a) Utiliza ordenação por seleção; (b) Perfeito; (c) Não, é melhor que o QuickSort;
(d) Não, é melhor que o InsertionSort; (e) Não, é idêntico ao MergeSort. Gabarito: B
20.(CESGRANRIO-2009- BASA-Analista de Sistemas) Com relação aos algoritmos quicksort e mergsort, o tempo de execução para o:
a) pior caso do quicksort é (n lg n).

b) pior caso do mergesort é (n2).

x'"'

/ 49

/

c) pior caso do mergesort é (n lg n).

d) caso médio do mergesort é O(lg n).

e) caso médio do quicksort é O(n2).

Comentários:

Algoritmo Melhor Caso Caso Médio Pior Caso

BubbleSort

O(n)

O(n2)

O(n2)

InsertionSort

O(n)

O(n2)

O(n2)

SelectionSort

O(n2)

O(n2)

O(n2)

QuickSort

O(n log n)

O(n log n)

O(n2)

ShellSort

O(n log n)

Depende do gap

O(n2)

MergeSort

O(n log n)

O(n log n)

O(n log n)

HeapSort

O(n log n)

O(n log n)

O(n log n)

Conforme vimos em aula, trata-se da terceira opção. Gabarito: C

21 .(CESPE - 2009 - UNIPAMPA- Analista de Sistemas) O algoritmo quicksort, que divide uma instrução em quatro blocos diferentes de busca, é um exemplo de estrutura de ordenação de dados.
Comentários:

Conforme vimos em aula, são dois blocos diferentes de busca. Gabarito: E

22.(CESPE - 2013 - CPRM - Analista de Sistemas) No algoritmo de ordenação denominado quicksort, escolhe-se um ponto de referência, denominado pivô, e separam-se os elementos em dois grupos: à esquerda, ficam os elementos menores que o pivô, e à direita ficam os maiores. Repete-se esse processo para os grupos de elementos formados(esquerda e direita) até que todos os elementos estejam ordenados.

Comentários:

Esse algoritmo divide um conjunto de itens em conjuntos menores, que são ordenados de forma independente, e depois os resultados são combinados para produzir a solução de ordenação do conjunto maior. Trata-se, portanto, de um algoritmo do tipo Divisão-e-Conquista,i.e., repartindo os dados em subgrupos, dependendo de um elemento chamado pivô.
/ 49

/

Neste método, a lista é dividida em parte esquerda e parte direita, sendo que os elementos da parte esquerda são todos menores que os elementos da parte direita. Essa fase do processo é chamada de partição. Em seguida, as duas partes são ordenadas recursivamente (usando o próprioQuickSort). A lista está, portanto, ordenada corretamente!

Conforme vimos em aula, é exatamente assim! Gabarito: C

23.(CESPE - 2013 - MPU - Analista de Sistemas) Entre os algoritmos de ordenação e pesquisa bubble sort, quicksort e heapsort, o quicksort é considerado o mais eficiente, pois se caracteriza como um algoritmo de dividir-para-conquistar, utilizando operações de particionamento.
Comentários:

Conforme vimos em aula, o HeapSort é o mais eficiente no pior caso! Gabarito: E

24.(CESPE - 2013 -TRT/9 - Analista de Sistemas) No método Quicksort, o pivô é responsável pelo número de partições em que o vetor é dividido. Como o pivô não pode ser um elemento que esteja repetido no vetor, o Quicksort não funciona quando há elementos repetidos.
Comentários:

O pivô não é responsável pelo número de partições em que o vetor é dividido.
Ademais, ele pode sim ser um elemento que esteja repetido no vetor! Gabarito: E
25.(FCC - 2011 - TRT - 14a Região (RO e AC) - Analista Judiciário - Tecnologia da
Informação)
NÃO se trata de um método de ordenação (algoritmo):

a) inserção direta.

b) seleção direta.

c) inserção por meio de incrementos decrescentes.

d) direta em cadeias.

e) particionamento.

Comentários:

(a) Trata-se do InsertionSort; (b) Trata-se do SelectionSort; (c) Trata-se do ShellSort;
(d) Trata-se de um método de busca; (e) Trata-se do QuickSort. Portanto, é a quarta opção! Gabarito: D
26.(FCC - 2016 - TRT - 23a REGIÃO (MT) - Analista Judiciário -
Tecnologia da Informação)
Considere o método de ordenação abaixo.

/ 49

/

void ordena(int m, int x[]} {
int âux, j j. i;

for{i=Q;i<m-lji++) {
for(j =0 fji-1;j++)

if (x[j] > x[j+l] ) {
àux=x[j];

x[j]=x[ji+l] ;

X [ j| +1] =ãux;

}

}

}

Utilizando este algoritmo de ordenação, percorre-se a lista dada da esquerda para a direita,comparando pares de elementos consecutivos, trocando de lugar os que estão fora da ordem. Em cada troca, o maior elemento é deslocado uma posição para a direita.Trata-se de um algoritmo de ordenação:
a) Select Sort.

b) Insert Sort.

c) Bubble Sort.

d) Shell Sort.

e) Quick Sort.

Comentários:

O algoritmo realiza trocas de dois em dois, percorrendo todos os elementos. Como vimos, esse algoritmo é o Bubble Sort. Gabarito: C
, 49

QUESTõES CoMENTADAS - CoMPLEXIDADE DE

ALGoRITMoS - MULTIBANCAS

1. (VUNESP - 2012 - TJ/SP - Analista Judiciário - Tecnologia da Informação)
Considerando o conceito de Complexidade de Algoritmos, representado por O(função),assinale a alternativa que apresenta, de forma crescente, as complexidades de algoritmos.
a) O(2n); O(n3); O(n2); O(log2 n); O(n.log2 n).

b) O(n2); O(n3); O(2n); O(log2 n); O(n.log2 n).

c) O(n3); O(n2); O(2n); O(n.log2 n); O(log2 n).

d) O(log2 n); O(n.log2 n); O(n2); O(n3); O(2n).

e) O(n.log2 n); O(log2 n); O(2n); O(n3); O(n2).

Comentários:

Notação Nome

0(1) Constante

O(log n) Logarítmica

O[(log n)c] Polilogarítmica

O(n) Linear

O(n log n) -

O(n2) Quadrática

O(n3) Cúbica

O(nc) Polinomial

O(cn) Exponencial

O(n!) Fatorial

Conforme vimos em aula, basta consultar a tabelinha! Gabarito: D

2. (FCC - 2010 - TRT - 8a Região (PA e AP) - Analista Judiciário - Tecnologia da Informação)Numa competição de programação, ganhava mais pontos o time que apresentasse o algoritmo mais eficiente para resolver o pior caso de um determinado problema. Acomplexidade assintótica (notação Big O) dos algoritmos elaborados está ilustrada na tabela abaixo.
/ 49

/

Time
Branco
Amarelo
Azul
Verde
Vermelho

Complexidade

Ofn20)
Ofnlogn)
0(1)

O(ri)

O(2n)

O time que obteve a medalha de prata (2° algoritmo mais eficiente) é o:

a) Branco.

b) Amarelo.

c) Azul.

d) Verde.

e) Vermelho.

Comentários:

Notação Nome

0(1) Constante

O(log n) Logarítmica

O[(log n)c] Polilogarítmica

O(n) Linear

O(n log n) -

O(n2) Quadrática

O(n3) Cúbica

O(nc) Polinomial

O(cn) Exponencial

O(n!) Fatorial

Conforme vimos em aula, basta consultar a tabelinha! O primeiro é o time Azul (0(1))
e o segundo é o time Amarelo (O(n log n)). Gabarito: B
/ 49

/

QUESTõES CoMENTADAS - PESQUISA DE DADoS -
MULTIBANCAS

1. (CESPE - 2013 - TRT/MS - Analista de Sistemas) Considerando que se deseje efetuar uma pesquisa de um valor sobre a chave primária de uma tabela de um banco de dados com uma chave primária com um tipo de campo que receba um valor inteiro e que se possa fazer essa pesquisa utilizando-se a busca sequencial ou a busca binária,assinale a opção correta.
a) O método de busca binária requer, no máximo, ln(n) comparações para determinar o elemento pesquisado, em que n é o número de registros.
b) O método de busca binária será sempre mais rápido que o método de busca sequencial,independentemente de a tabela estar ordenada com base no elemento pesquisado.

c) O método de busca sequencial requererá, no máximo, n2 comparações para determinar o elemento pesquisado, em que n será o número de registros.
d) O método de busca binária sempre efetuará menos comparações que o método de pesquisa sequencial.
e) O método de busca sequencial efetuará menos comparações para encontrar o elemento pesquisado quando a tabela estiver ordenada em comparação à situação quando a tabela estiver desordenada.
Comentários:

A Busca Binária é um algoritmo de busca em vetores que segue o paradigma de divisão-e-conquista. Parte-se do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca, comparando o elemento chave com o elemento do meio do vetor. Possui complexidade da ordem de O(log2 n), em que N é o tamanho do vetor de busca.
a) Conforme vimos em aula, não é logaritmo neperiano (na verdade, é Base 2), mas a banca considerou correto mesmo assim.
A Busca Sequencial é muito lenta para grandes quantidades de dados, mas aceitável para listas pequenas e que mudam constantemente. Observa-se que no Melhor Caso, X está na primeira posição, logo necessita apenas de uma comparação; no Pior Caso, X está na última posição, logo necessita de N comparações; e no Caso Médio, X é encontrado após (n+1)/2 comparações.
b) Conforme vimos em aula, isso não ocorre sempre! Se compararmos o Melhor Caso da
Busca
Sequencial com o Pior Caso da Busca Binária, a primeira será mais rápida.

Considerando que o vetor L[ ] contém N elementos, ordenados ou não, é fácil verificar que a busca sequencial requer tempo linearmente proporcional ao tamanho do vetor, i.e., da ordemO(n). Por conta disso, é comum dizer que a busca sequencial é uma Busca Linear. Entenderam?Quanto maior o vetor, maior o tempo em média para buscar um elemento! Quanto mais ao final,mais demorado.
c) Conforme vimos em aula, ele possui complexidade da ordem de O(n).

A Busca Sequencial é muito lenta para grandes quantidades de dados, mas aceitável para listas pequenas e que mudam constantemente. Observa-se que no Melhor Caso, X está na primeira
/ 49

/

posição, logo necessita apenas de uma comparação; no Pior Caso, X está na última posição, logo necessita de N comparações; e no Caso Médio, X é encontrado após (n+1)/2 comparações.
d) Conforme vimos em aula, isso não ocorre sempre! Se compararmos o Melhor Caso da
Busca
Sequencial com o Pior Caso da Busca Binária, a primeira será mais rápida.

Considerando que o vetor L[ ] contém N elementos, ordenados ou não, é fácil verificar que a busca sequencial requer tempo linearmente proporcional ao tamanho do vetor, i.e., da ordemO(n). Por conta disso, é comum dizer que a busca sequencial é uma Busca Linear. Entenderam?Quanto maior o vetor, maior o tempo em média para buscar um elemento! Quanto mais ao final,mais demorado.
e) Conforme vimos em aula, não é necessário que a lista esteja ordenada. Logo, isso não fará diferença. Gabarito: A
2. (ESAF - 2001 - BACEN - Analista de Sistemas) Na pior hipótese, o número de comparações necessárias para pesquisar um elemento em um array de 2048 elementos pelo método de pesquisa binária será:
a) 8

b) 9

c) 10

d) 11

e) 12

Comentários:

A Busca Binária é um algoritmo de busca em vetores que segue o paradigma de divisão-e-conquista. Parte-se do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca, comparando o elemento chave com o elemento do meio do vetor. Possui complexidade da ordem de O(log2 n), em que N é o tamanho do vetor de busca.
Conforme vimos em aula, a complexidade da Busca Binária é O(log2 n), em que N é o tamanho do vetor de busca - no nosso caso, 2048! Quanto é Iog2 2048? 11! Por que,professor? Porque
211 = 2048! Gabarito: D

3. (CESPE - 2013 - TCE/RO - Analista de Sistemas) Considere uma tabela de um banco de dados com chave primária e tipo de campo que receba um valor inteiro. Ao se efetuar uma pesquisa de um valor sobre a chave primária dessa tabela, o método de busca binária requer, no máximo, lg(n) comparações para localizar o elemento pesquisado, em que n é o número de registros.
Comentários:

A Busca Binária é um algoritmo de busca em vetores que segue o paradigma de divisão-e-conquista. Parte-se do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do
/ 49

/

espaço de busca, comparando o elemento chave com o elemento do meio do vetor. Possui complexidade da ordem de O(log2 n), em que N é o tamanho do vetor de busca.
Conforme vimos em aula, de fato a complexidade da Busca Binária é O(log2 n). Gabarito: C

4. (FCC - 2016 - TRT - 14a Região (RO e AC) - Analista Judiciário - Tecnologia da Informação)Dada uma coleção de n elementos ordenados por ordem crescente, pretende-se saber se um determinado elemento x existe nessa coleção. Supondo que essa coleção está implementada como sendo um vetor a[0...n-1] de n elementos inteiros,utilizando-se um algoritmo de pesquisa binária, o número de vezes que a comparação x==a[i] será executada, no pior caso, é calculada por:
a) n/2.

b) n-1.

c) Vn.

d) Iog2(n).

e) n-=2.

Comentários:

A Busca Binária é um algoritmo de busca em vetores que segue o paradigma de divisão-e-conquista. Parte-se do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca, comparando o elemento chave com o elemento do meio do vetor. Possui complexidade da ordem de O(log2 n), em que N é o tamanho do vetor de busca. Gabarito: D
/ 49

/

LISTA DE QUESTõES - MÉToDoS DE ORDENAçÃo -
MULTIBANCAS

1. (Instituto Cidades - 2012 - TCM-GO - Auditor de Controle Externo -
Informática) São exemplos de algoritmos de ordenação, exceto:
a) Bubble Sort b) Select Sort c) Shell Sort d) Busca Sequencial;
e) Quick Sort;

2. (FUMARC - 2012 - TJ-MG - Técnico Judiciário - Analista de Sistemas - I)
Quicksort divide um conjunto de itens em conjuntos menores, que são ordenados de forma independe, e depois os resultados são combinados para produzir a solução de ordenação do conjunto maior.
3. (CESPE - 2012 - MPE-PI - Analista Ministerial - Informática - Cargo
6) O heapsort é um algoritmo de ordenação em que a quantidade de elementos armazenada fora do arranjo de entrada é constante durante toda a sua execução.
4. (CESPE - 2010 - ABIN - Oficial Técnico de Inteligência - Área de Suporte a
Rede de Dados)
A eficácia do método de ordenação rápida (quicksort) depende da escolha do pivô mais adequado ao conjunto de dados que se deseja ordenar. A situação ótima ocorre quando o pivô escolhido é igual ao valor máximo ou ao valor mínimo do conjunto de dados.
5. (CESPE - 2010 - ABIN - Oficial Técnico de Inteligência - Área de Suporte a
Rede de Dados)
A estabilidade de um método de ordenação é importante quando o conjunto de dados já está parcialmente ordenado.
6. (CESPE - 2010 - Banco da Amazônia - Técnico Científico - Tecnologia da Informação -Administração de Dados) A classificação interna por inserção é um método que realiza a ordenação de um vetor por meio da inserção de cada elemento em sua posição correta dentro de um subvetor classificado.
7. (FCC - 2009 - TRT - 15a Região - Analista Judiciário - Tecnologia da Informação) São algoritmos de classificação por trocas apenas os métodos:
a) SelectionSort e InsertionSort.

/ 49

/

b) MergeSort e BubbleSort.

c) QuickSort e SelectionSort.

d) BubbleSort e QuickSort.

e) InsertionSort e MergeSort.

8. (CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - I) O tempo de pior caso do algoritmo QuickSort é de ordem menor que o tempo médio do algoritmo Bubblesort.
9. (CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - II) O tempo médio doQuickSort é O(nlog2n), pois ele usa como estrutura básica uma árvore de prioridades.

10.(CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - III) O tempo médio doQuickSort é de ordem igual ao tempo médio do MergeSort.

11 .(CESGRANRIO - 2012 - CMB - Analista de Sistemas - III) Em uma reunião de análise de desempenho de um sistema WEB, um programador apontou corretamente que a complexidade de tempo do algoritmo bubblesort, no pior caso, é:
a) 0(1)

b) O(log n)

c) O(n)

d) O(n log n)

e) O(n2)

12. (CESPE - 2010 - INMETRO - Analista de Sistemas) Se f é uma função de complexidade para um algoritmo F, então O(f) é considerada a complexidade assintótica ou o comportamento assintótico do algoritmo F. Assinale a opção que apresenta somente algoritmos que possuem complexidade assintótica quando f(n) = O(n log n).
a) HeapSort e BubbleSort b) QuickSort e InsertionSort c) MergeSort e BubbleSort d) InsertionSort e) HeapSort, QuickSort e MergeSort
13.(FGV - 2013 - MPE/MS - Analista de Sistemas) Assinale a alternativa que indica o algoritmo de ordenação capaz de funcionar em tempo O(n) para alguns conjuntos de entrada.
a) Selectionsort (seleção)

b) Insertionsort (inserção)

/ 49

/

c) Merge sort d) Quicksort e) Heapsort
14.(CESGRANRIO - 2010 - BACEN - Analista de Sistemas) Uma fábrica de software foi contratada para desenvolver um produto de análise de riscos. Em determinada funcionalidade desse software, é necessário realizar a ordenação de um conjunto formado por muitos números inteiros. Que algoritmo de ordenação oferece melhor complexidade de tempo (Big O notation) no pior caso?
a) Merge sort b) Insertion sort c) Bubble sort d) Quick sort e) Selection sort
15.(CESPE - 2011 - FUB - Analista de Sistemas) Os métodos de ordenação podem ser classificados como estáveis ou não estáveis. O método é estável se preserva a ordem relativa de dois valores idênticos. Alguns métodos eficientes como shellsort ou quicksort não são estáveis, enquanto alguns métodos pouco eficientes, como o método da bolha,são estáveis.

16.(CESPE - 2012 - BASA- Analista de Sistemas) O método de classificação
Shellsort iguala-
se ao método Quicksort em termos de complexidade temporal, porém é mais eficiente para quantidades pequenas a moderadas de dados.
17.(CESPE - 2012 - BASA - Analista de Sistemas) O método de classificação
Quicksort é estável e executado em tempo linearmente dependente da quantidade de dados que estão sendo classificados.
18.(CESPE - 2012 - BASA - Analista de Sistemas) No método de ordenamento denominado shellsort, as comparações e as trocas são feitas conforme determinada distância entre dois elementos, de modo que, uma distância igual a 6 seria a comparação entre o primeiro elemento e o sétimo, ou entre o segundo elemento e o oitavo, e assim sucessivamente,repetindo-se esse processo até que as últimas comparações e trocas tenham sido efetuadas e a distância tenha diminuído até chegar a 1.
19.(FGV - 2008 - PETROBRÁS - Analista de Sistemas) Sobre o algoritmo de ordenação heapsort, assinale a afirmação correta.
a) Utiliza ordenação por árvore de decisão, ao invés de ordenação por comparação.

x'

/ 49

/

b) A estrutura de dados que utiliza, chamada heap, pode ser interpretada como uma árvore binária.
c) Seu desempenho de pior caso é pior do que o do algoritmo quicksort.

d) Seu desempenho de pior caso é o mesmo da ordenação por inserção.

e) Seu desempenho de pior caso é menor do que o da ordenação por intercalação.

20.(CESGRANRIO- 2009- BASA- Analista de Sistemas) Com relação aos algoritmos quicksort e mergsort, o tempo de execução para o:
a) pior caso do quicksort é (n lg n).

b) pior caso do mergesort é (n2).

c) pior caso do mergesort é (n lg n).

d) caso médio do mergesort é O(lg n).

e) caso médio do quicksort é O(n2).

21 .(CESPE - 2009 - UNIPAMPA- Analista de Sistemas) O algoritmo quicksort, que divide uma instrução em quatro blocos diferentes de busca, é um exemplo de estrutura de ordenação de dados.
22. (CESPE - 2013 - CPRM - Analista de Sistemas) No algoritmo de ordenação denominado quicksort, escolhe-se um ponto de referência, denominado pivô, e separam-se os elementos em dois grupos: à esquerda, ficam os elementos menores que o pivô, e à direita ficam os maiores. Repete-se esse processo para os grupos de elementos formados(esquerda e direita) até que todos os elementos estejam ordenados.

23.(CESPE - 2013 - MPU - Analista de Sistemas) Entre os algoritmos de ordenação e pesquisa bubble sort, quicksort e heapsort, o quicksort é considerado o mais eficiente, pois se caracteriza como um algoritmo de dividir-para-conquistar, utilizando operações de particionamento.
24.(CESPE - 2013 - TRT/9 - Analista de Sistemas) No método Quicksort, o pivô é responsável pelo número de partições em que o vetor é dividido. Como o pivô não pode ser um elemento que esteja repetido no vetor, o Quicksort não funciona quando há elementos repetidos.
25.(FCC - 2011 - TRT - 14a Região (RO e AC) - Analista Judiciário - Tecnologia da
Informação)
NÃO se trata de um método de ordenação (algoritmo):

a) inserção direta.

b) seleção direta.

c) inserção por meio de incrementos decrescentes.

/ 49

/

d) direta em cadeias.

e) particionamento.

26. (FCC - 2016 - TRT - 23a REGIÃO (MT) - Analista Judiciário - Tecnologia da Informação)
Considere o método de ordenação abaixo.

void ordena(int m, int x[]} {
int âux, j j. i;

for{i=Q;i<m-lji++) {
for(j =0}ji-1;j ++)

if (x[j] > xlj+1] ) {
aux=x[j];
x[j]=x[j+l] ;
x[j+l] =aux;

}

}

}

Utilizando este algoritmo de ordenação, percorre-se a lista dada da esquerda para a direita,comparando pares de elementos consecutivos, trocando de lugar os que estão fora da ordem. Em cada troca, o maior elemento é deslocado uma posição para a direita.Trata-se de um algoritmo de ordenação:
a) Select Sort.

b) Insert Sort.

c) Bubble Sort.

d) Shell Sort.

e) Quick Sort.

/ 49

/

GABARITo

GABARITO

1. D 10.C
19.B

2. C 11.E
20.C

3. C 12.E
21.E

4. E 13.B
22.C

5. E 14.A
23.E

6. C 15.C
24. E

7. D 16.E
25.D

8. E 17.E
26.C

9. E 18.C

SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023 (Pós-I

LISTA DE QUESTõES - CoMPLEXIDADE DE ALGoRITMoS -
MULTIBANCAS

1. (VUNESP - 2012 - TJ/SP - Analista Judiciário - Tecnologia da Informação)
Considerando o conceito de Complexidade de Algoritmos, representado por O(função),assinale a alternativa que apresenta, de forma crescente, as complexidades de algoritmos.
a) O(2n); O(n3); O(n2); O(log2 n); O(n.log2 n).

b) O(n2); O(n3); O(2n); O(log2 n); O(n.log2 n).

c) O(n3); O(n2); O(2n); O(n.log2 n); O(log2 n).

d) O(log2 n); O(n.log2 n); O(n2); O(n3); O(2n).

e) O(n.log2 n); O(log2 n); O(2n); O(n3); O(n2).

2. (FCC - 2010 - TRT - 8a Região (PA e AP) - Analista Judiciário - Tecnologia da Informação)Numa competição de programação, ganhava mais pontos o time que apresentasse o algoritmo mais eficiente para resolver o pior caso de um determinado problema. Acomplexidade assintótica (notação Big O) dos algoritmos elaborados está ilustrada na tabela abaixo.
Time
Branco
Amarelo
Azul
Verde
Vermelho

Complexidade
Oín20)
Ofnlogn)

0(1)

OfniJ

O(2n}

O time que obteve a medalha de prata (2o algoritmo mais eficiente) é o:

a) Branco.

b) Amarelo.

c) Azul.

d) Verde.

e) Vermelho.

SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital) x' 44

/ 49

/

GABARITo

GABARITO

1. D

2. B

/

LISTA DE QUESTõES - PESQUISA DE DADoS -
MULTIBANCAS

1. (CESPE - 2013 - TRT/MS - Analista de Sistemas) Considerando que se deseje efetuar uma pesquisa de um valor sobre a chave primária de uma tabela de um banco de dados com uma chave primária com um tipo de campo que receba um valor inteiro e que se possa fazer essa pesquisa utilizando-se a busca sequencial ou a busca binária,assinale a opção correta.
a) O método de busca binária requer, no máximo, ln(n) comparações para determinar o elemento pesquisado, em que n é o número de registros.
b) O método de busca binária será sempre mais rápido que o método de busca sequencial,independentemente de a tabela estar ordenada com base no elemento pesquisado.

c) O método de busca sequencial requererá, no máximo, n2 comparações para determinar o elemento pesquisado, em que n será o número de registros.
d) O método de busca binária sempre efetuará menos comparações que o método de pesquisa sequencial.
e) O método de busca sequencial efetuará menos comparações para encontrar o elemento pesquisado quando a tabela estiver ordenada em comparação à situação quando a tabela estiver desordenada.
2. (ESAF - 2001 - BACEN - Analista de Sistemas) Na pior hipótese, o número de comparações necessárias para pesquisar um elemento em um array de 2048 elementos pelo método de pesquisa binária será:
a) 8

b) 9

c) 10

d) 11

e) 12

3. (CESPE - 2013 - TCE/RO - Analista de Sistemas) Considere uma tabela de um banco de dados com chave primária e tipo de campo que receba um valor inteiro. Ao se efetuar uma pesquisa de um valor sobre a chave primária dessa tabela, o método de busca binária requer, no máximo, lg(n) comparações para localizar o elemento pesquisado, em que n é o número de registros.
4. (FCC - 2016 - TRT - 14a Região (RO e AC) - Analista Judiciário - Tecnologia da Informação)Dada uma coleção de n elementos ordenados por ordem crescente, pretende-se saber se um determinado elemento x existe nessa coleção. Supondo que essa coleção está implementada como sendo um vetor a[0...n-1] de n elementos inteiros, utilizando-se um
SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital) x' 46

/ 49

/

algoritmo de pesquisa binária, o número de vezes que a comparação x==a[i] será executada, no pior caso, é calculada por:
a) n/2.

b) n-1.

c) Vn.

d) Iog2(n).

e) n-=2.

I

GABARITo

GABARITO

1. A

2. D

3. C

4. D

