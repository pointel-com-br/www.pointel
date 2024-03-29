# Análise e desenvolvimento de software - Estrutura de Dados

A estrutura de dados é um componente fundamental no desenvolvimento de software, pois ela define a forma como os dados são organizados, armazenados e manipulados em um programa. A escolha correta da estrutura de dados pode impactar significativamente o desempenho, a eficiência e a escalabilidade de um sistema.

Existem várias estruturas de dados com diferentes características e propósitos, cada uma adequada para determinadas situações. Algumas das estruturas de dados mais comuns incluem:

1. Array (vetor): É uma estrutura de dados simples e estática que armazena elementos em uma sequência contígua de memória. Os elementos podem ser acessados através de índices. Os arrays possuem acesso rápido aos elementos, mas possuem tamanho fixo.

2. Lista: É uma estrutura de dados dinâmica que armazena uma sequência de elementos. Existem dois tipos principais de listas: lista ligada (linked list) e lista duplamente ligada (doubly linked list). As listas podem ser facilmente expandidas ou reduzidas, mas o acesso aos elementos pode ser mais lento em comparação com os arrays.

3. Pilha (stack): É uma estrutura de dados baseada no princípio Last-In-First-Out (LIFO), onde o último elemento inserido é o primeiro a ser removido. As operações fundamentais em uma pilha são a inserção (push) e a remoção (pop) de elementos.

4. Fila (queue): É uma estrutura de dados baseada no princípio First-In-First-Out (FIFO), onde o primeiro elemento inserido é o primeiro a ser removido. As operações fundamentais em uma fila são a inserção (enqueue) e a remoção (dequeue) de elementos.

5. Árvore (tree): É uma estrutura de dados hierárquica composta por nós interconectados. Cada nó pode ter um ou mais nós filhos, formando uma estrutura de árvore. As árvores são amplamente utilizadas em algoritmos de busca e estruturas de dados mais complexas, como árvores binárias, árvores de busca binária e árvores balanceadas.

6. Grafo (graph): É uma estrutura de dados que consiste em um conjunto de vértices (nós) conectados por arestas. Os grafos são usados para representar relações entre objetos e são usados em problemas de roteamento, redes sociais, sistemas de recomendação, entre outros.

Essas são apenas algumas das estruturas de dados comumente utilizadas no desenvolvimento de software. Cada estrutura de dados tem suas características e aplicações específicas. A escolha correta da estrutura de dados depende das necessidades do sistema, dos requisitos de desempenho e da natureza dos dados a serem manipulados.

Além disso, é importante ter em mente que muitas linguagens de programação oferecem implementações nativas de estruturas de dados, facilitando a sua utilização. No entanto, em alguns casos, pode ser necessário implementar uma estrutura de dados personalizada, adaptada às necessidades específicas do sistema em questão.

Pessoal, um programa pode ser visto como uma especificação formal da solução de um problema. Wirth expressa esse conceito por meio de uma equação:

PROGRAMA = ALGORITMO + ESTRUTURA DE DADOS

Nosso foco aqui é em Estruturas de Dados! Na evolução do mundo computacional, um fator extremamente importante trata da forma de armazenar informações. De nada adianta o enorme desenvolvimento de hardware e software se a forma de armazenamento e tratamento de dados não evoluir harmonicamente. E é por isso que as estruturas de dados são tão fundamentais.
As estruturas de dados, na maioria dos casos, baseiam-se nos tipos de armazenamento vistos dia a dia, i.e., nada mais são do que a transformação de uma forma de armazenamento já conhecida e utilizada no mundo real adaptada para o mundo computacional. Por isso, cada tipo de estrutura de dados possui vantagens e desvantagens e cada uma tem sua área de atuação otimizada.

Bem, não vou enrolar muito explicando o que é uma Estrutura de Dados! A melhor forma de saber é vendo exemplos. Antes disso, eu gostaria de falar sobre um conceito importante: Dados Homogêneos e Heterogêneos. Os primeiros são aqueles que possuem só um tipo básico de dados (Ex: Inteiros); os segundos são aqueles que possuem mais de um tipo básico de dados (Ex: Inteiros + Caracteres). Os tipos básicos de dados também são chamados de tipos primitivos.

Entenderam? Existem estruturas de dados que tratam de dados homogêneos, i.e., todos os dados são apenas de um tipo básico, tais como Vetores! Ora, em um vetor, todos os elementos são do mesmo tipo. Existem estruturas de dados que tratam de dados heterogêneos, i.e., os dados são de tipos básicos diferentes, tais como Listas! Ora, em uma lista, todos os elementos são, em geral, de tipos básicos diferentes.
Além dessa classificação, existe outra também importante: Estruturas Lineares e Estruturas Não- Lineares. As Estruturas Lineares são aquelas em que cada elemento pode ter um único predecessor (exceto o primeiro elemento) e um único sucessor (exceto o último elemento). Como exemplo, podemos citar Listas, Pilhas, Filas, Arranjos, entre outros.

Já as Estruturas Não-Lineares são aquelas em que cada elemento pode ter mais de um predecessor e/ou mais de um sucessor. Como exemplo, podemos citar Árvores, Grafos e Tabelas de Dispersão. Essa é uma classificação muito importante e muito simples de entender. Pessoal, vocês perceberão que esse assunto é cobrado de maneira superficial na maioria das questões, mas algumas são nível doutorado!
Por fim, vamos falar sobre Tipos Abstratos de Dados (TAD). Podemos defini-lo como um modelo matemático (v,o), em que v é um conjunto de valores e o é um conjunto de operações que podem ser realizadas sobre valores. Eu sei, essa definição é horrível de entender! Para compreender esse conceito, basta lembrar de abstração, i.e., apresentar interfaces e esconder detalhes.

Os Tipos Abstratos de Dados são simplesmente um modelo para um certo tipo de estrutura de dados. Como assim, professor? Quando eu falo em pilha, eu estou falando de um tipo abstrato de dados que tem duas operações com comportamentos bem definidos e conhecidos: push (para inserir elementos na pilha); e pop (para retirar elementos da pilha).
E a implementação dessas operações? Isso não importa! Aliás, não importa implementação nem paradigma nem linguagem de programação. Não importa se a pilha é implementada com um paradigma orientado a objetos ou com um paradigma estruturado; não importa se a pilha é implementada em Java ou Pascal; não importa como é a implementação interna - isso serve para outras estruturas.

Podemos concluir, portanto, que um tipo abstrato de dados contém um modelo que contém valores e operações associadas, de forma que essas operações sejam precisamente independentes de uma implementação particular. Em geral, um TAD é especificado por meio de uma especificação algébrica que, em geral, contém três partes: Especificação Sintática, Semântica e de Restrições.
A Especificação Sintática define o nome do tipo, suas operações e o tipo dos argumentos das operações, definindo a assinatura do TAD. A Especificação Semântica descreve propriedades e efeitos das operações de forma independente de uma implementação específica. E a Especificação de Restrições estabelece as condições que devem ser satisfeitas antes e depois da aplicação das operações.

Em outras palavras, o nível semântico trata do comportamento de um tipo abstrato de dados; e o nível sintático trata da apresentação de um tipo abstrato de dados. Podemos dizer, então, que o TAD encapsula uma estrutura de dados com características semelhantes - podendo ser formado por outros TADs -, e esconde a efetiva implementação dessa estrutura de quem a manipula.

Índice

1 Vetores e Matrizes

2 Lista Encadeada

3 Pilhas

4 Filas

5 Árvore

6 Grafos

Vetores e Matrizes

Um Vetor é uma estrutura de dados linear que necessita de somente um índice para que seus elementos sejam indexados. É uma estrutura homogênea, portanto armazena somente uma lista de valores do mesmo tipo. Ele pode ser estático ou dinâmico, com dados armazenados em posições contíguas de memória e permite o acesso direto ou aleatório a seus elementos.
Observem que, diferentemente das listas, filas e pilhas, ele vem praticamente embutido em qualquer linguagem de programação. E a Matriz, professor? Não muda muita coisa! Trata-se de um arranjo bidimensional ou multidimensional de alocação estática e sequencial. Ela necessita de um índice para referenciar a linha e outro para referenciar a coluna para que seus elementos sejam endereçados.
Da mesma forma que um vetor, uma matriz também pode ter tamanhos variados, todos os elementos são do mesmo tipo, cada célula contém somente um valor e os tamanhos dos valores são os mesmos. Os elementos ocupam posições contíguas na memória. A alocação dos elementos pode ser feita colocando os elementos linha-por-linha ou coluna-por-coluna.

Lista Encadeada

Também conhecida como Lista Encadeada Linear, Lista Ligada Linear ou Linked List, trata-se de uma estrutura de dados dinâmica formada por uma sequência encadeada de elementos chamados nós, que contêm dois campos: campo de informação e campo de endereço. O primeiro armazena o real elemento da lista e o segundo contém o endereço do próximo nó da lista.
Esse endereço, que é usado para acessar determinado nó, é conhecido como ponteiro. A lista ligada inteira é acessada a partir de um ponteiro externo que aponta para o primeiro nó na lista, i.e., contém o endereço do primeiro nó1. Por ponteiro "externo", entendemos aquele que não está incluído dentro de um nó. Em vez disso, seu valor pode ser acessado diretamente, por referência a uma variável.
O campo do próximo endereço do último nó na lista contém um valor especial, conhecido como NULL, que não é um endereço válido. Esse ponteiro nulo é usado para indicar o final de uma lista. Uma lista é chamada Lista Vazia ou Lista Nula caso não tenha nós ou tenha apenas um nó sentinela. O valor do ponteiro externo para esta lista é o ponteiro nulo. Uma lista pode ser inicializada com uma lista vazia.
Suponha que seja feita uma mudança na estrutura de uma lista linear, de modo que o campo próximo no último nó contenha um ponteiro de volta para o primeiro nó, em vez de um ponteiro nulo. Esse tipo de lista é chamado Lista Circular (ou Fechada2), i.e., a partir de qualquer ponto, é possível atingir qualquer outro ponto da lista. Certinho, até agora?
Observe que uma Lista Circular não tem um primeiro ou último nó natural. Precisamos, portanto, estabelecer um primeiro e um último nó por convenção. Uma convenção útil é permitir que o ponteiro externo para a lista circular aponte para o último nó, e que o nó seguinte se torne o primeiro nó. Assim podemos incluir ou remover um elemento convenientemente a partir do início ou do final de uma lista.
Embora uma lista circularmente ligada tenha vantagens sobre uma lista linear, ela ainda apresenta várias deficiências. Não se pode atravessar uma lista desse tipo no sentido contrário nem um nó pode ser eliminado de uma lista circularmente ligada sem se ter um ponteiro para o nó antecessor. Nos casos em que tais recursos são necessários, a estrutura de dados adequada é uma lista duplamente ligada.
Cada nó numa lista desse tipo contém dois ponteiros, um para seu predecessor e outro para seu sucessor. Na realidade, no contexto de listas duplamente ligadas, os termos predecessor e sucessor não fazem sentido porque a lista é totalmente simétrica. As listas duplamente ligadas podem ser lineares ou circulares e podem conter ou não um nó de cabeçalho.
Podemos considerar os nós numa lista duplamente ligada como consistindo em três campos: um campo info que contém as informações armazenadas no nó, e os campos left e right, que contêm ponteiros para os nós em ambos os lados. Dado um ponteiro para um elemento, pode-se acessar os elementos adjacentes e, dado um ponteiro para o último elemento, pode-se percorrer a lista em ordem inversa.
Existem cinco operações básicas sobre uma lista encadeada: Criação, em que se cria a lista na memória; Busca, em que se pesquisa nós na lista; Inclusão, em que se insere novos nós na lista em uma determinada posição; Remoção, em que se elimina um elemento da lista; e, por fim, Destruição, em que se destrói a lista junto com todos os seus nós.
Pilhas e Filas são subespécies de Listas. No entanto, cuidado na hora de responder questões! De maneira genérica, Pilhas e Filas podem ser implementadas como Listas. No entanto, elas possuem características particulares de uma lista genérica. Ok?
Precisamos falar um pouco sobre Fragmentação! O que é isso, professor? Galera, falou em fragmentação, lembrem-se de desperdício de espaço disponível de memória. O fenômeno no qual existem vários blocos disponíveis pequenos e não-contíguos é chamado fragmentação externa porque o espaço disponível é desperdiçado fora dos blocos alocados.
Esse fenômeno é o oposto da fragmentação interna, no qual o espaço disponível é desperdiçado dentro dos blocos alocados, como apresenta a imagem abaixo. Sistemas Operacionais possuem uma estrutura de dados que armazena informações sobre áreas ou blocos livres (geralmente uma lista ou tabela). Uma lista encadeada elimina o problema da fragmentação externa. Por que?
Porque mantém os arquivos, cada um, como uma lista encadeada de blocos de disco. Dessa forma, uma parte de cada bloco é usada como ponteiro para o próximo bloco e o restante do bloco é usado para dados. Uma vantagem desse tipo de alocação é que o tamanho do arquivo não precisa ser conhecido antes de sua criação, já que cada bloco terá um ponteiro para o próximo bloco.
Galera... e o acesso a uma lista? A Lista é uma estrutura de acesso sequencial, i.e., é preciso percorrer nó por nó para acessar um dado específico. Logo, é proporcional ao número de elementos - Acesso O(n). E os Vetores? Eles são uma estrutura de acesso direto, i.e., pode-se acessar um elemento diretamente. Portanto, não precisa percorrer elemento por elemento ( Acesso O ( 1 ) ).

Pilhas

A Pilha é um conjunto ordenado de itens no qual novos itens podem ser inseridos e eliminados em uma extremidade chamada topo. Novos itens podem ser colocados no topo da pilha (tornando-se o novo primeiro elemento) ou os itens que estiverem no topo da pilha poderão ser removidos (tornando-se o elemento mais abaixo o novo primeiro elemento).
Também conhecida como Lista LIFO (Last In First Out), basta lembrar de uma pilha de pratos esperando para serem lavados, i.e., o último a entrar é o primeiro a sair. A ordem em que os pratos são retirados da pilha é o oposto da ordem em que eles são colocados sobre a pilha e, como consequência, apenas o prato do topo da pilha está acessível.
As Pilhas oferecem três operações básicas: push, que insere um novo elemento no topo da pilha; pop, que remove um elemento do topo da pilha; e top (também conhecida como check), que acessa e consulta o elemento do topo da pilha. Pilhas podem ser implementadas por meio de Vetores (Pilha Sequencial - Alocação Estática de Memória) ou Listas (Pilha Encadeada - Alocação Dinâmica de Memória).

Filas

Uma fila é um conjunto ordenado de itens a partir do qual podem-se eliminar itens numa extremidade (chamada início da fila) e no qual podem-se inserir itens na outra extremidade (chamada final da fila). Também conhecida como Lista FIFO (First In First Out), basta lembrar de uma fila de pessoas esperando para serem atendidas em um banco, i.e., o primeiro a entrar é o primeiro a sair.
Quando um elemento é colocado na fila, ele ocupa seu lugar no fim da fila, como um aluno recém-chegado que ocupa o final da fileira. O elemento retirado da fila é sempre aquele que está no início da fila, como o aluno que se encontra no começo da fileira e que esperou mais tempo. As operações básicas são Enqueue (Enfileirar) e Dequeue (Desenfileirar). As Filas possuem início (ou cabeça) e fim (ou cauda).
É bom salientar outro conceito importante: Deque (Double Ended Queue)! É também conhecida como Filas Duplamente Encadeadas e permite a eliminação e inserção de itens em ambas as extremidades. Ademais, elas permitem algum tipo de priorização, visto que é possível inserir elementos de ambos os lados. Assim sendo, é comum em sistemas distribuídos!
Sistemas distribuídos sempre necessitam que algum tipo de processamento seja mais rápido, por ser mais prioritário naquele momento, deixando outros tipos mais lentos ou em fila de espera, por não requerem tanta pressa. Ele pode ser entendido como uma extensão da estrutura de dados Fila. Agora uma pergunta: Qual a diferença entre uma lista duplamente encadeada e um deque?
Pessoal, um deque gerencia elementos como um vetor, fornece acesso aleatório e tem quase a mesma interface que um vetor. Ele se diferencia de uma lista duplamente encadeada, entre outras coisas, por essa não fornecer acesso aleatório aos elementos, i.e., para acessar o quinto elemento, você deve navegar pelos quatro primeiros elementos - logo a lista é mais lenta nesse sentido. Bacana?

Árvore

Uma árvore é uma estrutura de dados hierárquica (não-linear) composta por um conjunto finito de elementos com um único elemento raiz, com zero ou mais sub-árvores ligadas a esse elemento raiz. Como mostra a imagem abaixo, há uma única raiz, em amarelo. Há também nós folhas, em vermelho e seus pais, em verde. Observem ainda os conceitos de Altura, Grau e Nível de uma árvore.
O Grau informa a quantidade de filhos de um determinado nó! A Raiz tem Nível 0 (excepcionalmente, alguns autores consideram que tem Nível 1) e o nível de qualquer outro nó na árvore é um nível a mais que o nível de seu pai. Por fim, a Altura é a distância entre a raiz e seu descendente mais afastado. Dessas informações, podemos concluir que toda folha tem Grau 0.
Existe um tipo particular de árvore chamado: Árvore Binária! O que é isso? É uma estrutura de dados hierárquica em que todos os nós têm grau 0, 1 ou 2. Já uma Árvore Estritamente Binária é aquela em que todos os nós têm grau 0 ou 2. E uma Árvore Binária Completa é aquela em que todas as folhas estão no mesmo nível, como mostram as imagens abaixo.
Uma Árvore Binária Completa com x folhas conterá sempre (2x - 1) nós. Observem a imagem acima e façam as contas: 2*8 - 1 = 15 nós! Uma árvore binária completa de altura h e nível n contém (2h-1) ou (2n+1-1) nós e usa-se (2n), para calcular a quantidade de nós em determinado nível. Na imagem acima, há uma árvore de h = 4 e n = 3; logo, existem 23+1 -1 = 15 nós no total; e no Nível 3, existe 23 = 8 nós.
Vamos falar um pouco agora sobre Árvore de Busca Binária! Trata-se de uma Uma estrutura de dados vinculada, baseada em nós, onde cada nó contém uma chave e duas subárvores à esquerda e a direita. Para todos nós, a chave da subárvore esquerda deve ser menor que a chave desse nó, e a chave da subárvore direita deve ser maior. Beleza?
Todas estas subárvores devem qualificar-se como árvores binárias de busca. O pior caso de tempo de complexidade para a pesquisa em uma árvore binária de busca é a altura da árvore, isso pode ser tão pequeno como O(log n) para uma árvore com n elementos. Galera, abaixo nós vamos ver como árvores podem ser representadas e o conceito de árvore binária de busca ficará mais clara!
Como representamos árvores? Podemos representar uma árvore como um conjunto de parênteses aninhados. Nessa notação, (P (F1)(F2)) significa que P, F1, F2 são nós e que F1, F2, são filhos do pai P. Ao transcrever isso para o desenho hierárquico de uma árvore, lemos da esquerda para a direita. Agora suponhamos que F1 tem dois filhos N1 e N2. Logo, reescrevemos a subárvore de F1 como (F1 (N1)(N2)).
Podemos, então, substituir F1 por (F1(N1)(N2)). Ao final, ficará (P(F1(N1)(N2))(F2)). E assim por diante. Temos então que o primeiro elemento é a raiz e sempre que tivermos um parêntese, teremos uma nova subárvore. Vamos exemplificar: (12(10(9(8))(11))(14(13)(15))). Como ficaria, professor? Sabemos que 12 será a raiz dessa árvore e, a partir daí, criamos a árvore da esquerda para direita.
Observem o parêntese após o 12! Notem que ele só é fechado após o 11: (12(10(9(8))(11)). Isso significa que tudo que está em vermelho é subárvore da esquerda da raiz 12 - e o restante (14(13)(15)) é subárvore da direita da raiz 12. Observem o parêntese após o 10! Notem que ele só é fechado após o 8: 10(9(8)). Isso significa que tudo que está em amarelo é subárvore da esquerda da raiz 10.
E o restante (11) é subárvore da direita da raiz 10. Observem o parêntese após o 9! Notem que ele só é fechado após o 8: 9(8). Isso significa que tudo que está em verde é subárvore da esquerda da raiz 9 - e o restante... que restante, professor? Pois é, não tem restante! Logo, 9 não tem subárvore da direita. Vejam abaixo como ficou e vamos analisar o outro lado.
A subárvore da direita da raiz 12 tem raiz 14 e tem dois filhos: na esquerda, 13 e na direita 15. Fim! Galera, eu sei que parece complicado, mas leiam e pratiquem umas três vezes - de preferência no papel - que vocês internalizam tranquilamente esse conteúdo. É chatinho, mas não é difícil! Vejam abaixo como ficou o resultado final e vamos seguir em frente...
Bem, pessoal! Dito isso, vamos analisar agora como ficaria para remover um nó desta árvore. Existem três possibilidades para realizar essa operação: (1) remover um nó que não tem filhos; (2) remover um nó que tem apenas um filho; (3) e remover um nó que tenha dois filhos. O primeiro caso é muito simples: basta retirar o nó desejado e ponto final. Vejamos como fica:
No segundo caso, basta retirar o nó da árvore e conectar seu único filho (e sua subárvore, se houver) diretamente ao pai do nó removido. Vejamos:
Já o último caso, nós podemos utilizar duas estratégias. Você pode escolher qual deseja utilizar em uma situação específica. Vejamos:
Por fim, como seria a representação por parênteses aninhados? Na primeira estratégia, temos: (13(10(9(8))(11))(14(15))); na segunda, temos (11(10(9(8)))(14(13)(15))).
Galera, em uma Árvore de Busca Binária, podemos fazer três percursos: pré-ordem, in-ordem e pós-ordem (esses prefixos são em relação a raiz). É interessante notar que, quando se faz um percurso em ordem em uma árvore binária de busca, os valores dos nós aparecem em ordem crescente. A operação "Percorre" tem como objetivo percorrer a árvore numa dada ordem, enumerando os seus nós.

Quando um nó é enumerado, diz-se que ele foi "visitado". Vamos ver agora esses três percursos:

§ Pré-Ordem (ou Profundidade): visita a raiz; percorre a subárvore esquerda em pré-ordem; percorre a subárvore direita em pré-ordem

§ In-Ordem (ou Simétrica): percorre a subárvore esquerda em in-ordem; visita a raiz; percorre a subárvore direita em in-ordem.

§ Pós-Ordem: percorre a subárvore esquerda em pós-ordem; percorre a subárvore direita em pós-ordem; visita a raiz.

Agora vamos falar um pouquinho sobre três tipos especiais e árvores: Árvore B, Árvore B+ e Árvore AVL. E aí, eu preciso bastante da atenção de vocês agora! Eu coloco esse assunto porque os editais pedem apenas Árvore e não especificam a profundidade do assunto. Com exceção da CESGRANRIO, é raro outras bancas cobrarem esse assunto na profundidade que veremos agora.
É um assunto mais difícil e que cai pouco em prova, portanto só recomendo seguir caso queiram realmente cercar todas as possibilidades. Galera, época de faculdade, segundo semestre, disciplina de Estrutura de Dados! O trabalho final da disciplina era construir um compactador! Isso mesmo! Uma espécie de WinZip, WinRar, etc. E a estrutura usada para compactar arquivos de índices era uma Árvore B.
Uma árvore B é uma maneira de armazenar grandes quantidades de dados de tal forma que você pode procurá-los e recuperá-los muito rapidamente. As árvores B são a base da maioria dos bancos de dados modernos. Como eles funcionam é um bocado complicado, mas eu vou contar uma historinha que talvez os ajude a entender melhor! Vamo lá...
Imagine que você está procurando um par de novos fones de ouvido. Você tem algumas abordagens. Certo? Você poderia ir a todas as lojas do mundo até encontrar o produto que você procura. Como você pode imaginar, esta seria uma maneira horrível de fazer compras. Em vez disso, você poderia ir em uma FNAC, porque você sabe que eles vendem eletrônicos.
Uma vez que chegou à FNAC, você pode observar cada uma das descrições de corredor para ver onde os fones de ouvido são armazenados. Depois de encontrar o corredor correto, você pode escolher os fones de ouvido que você deseja. Ponto final! Observe como o objetivo desse processo é restringir o foco de uma pesquisa cada vez mais...
É assim que funcionam as Árvores B! Ao organizar os dados de forma específica, podemos aproveitá-las para que não desperdicemos nosso tempo buscando dados que tenham chance zero de armazenar os dados que estamos procurando. E a árvore já é construída de maneira a organizar os dados da melhor forma possível. Bacana, pessoal?
E qual a diferença de uma Árvore B para uma Árvore B+? Galera, a principal diferença é que, em uma Árvore B, as chaves e os dados podem ser armazenados tanto nos nós internos da árvore quanto nas folhas da árvore, enquanto que em uma Árvore B+ as chaves podem ser armazenadas em qualquer nó, mas os dados só podem ser armazenados nas folhas.
Por fim, vamos falar um pouco sobre Árvores AVL! Uma Árvore AVL (Adelson-Vesky e Landis) é uma Árvore Binária de Busca em que, para qualquer nó, a altura das subárvores da esquerda e da direita não podem ter uma diferença maior do que 1, portanto uma Árvore AVL é uma Árvore Binária de Busca autobalanceável. Calma que nós vamos ver isso em mais detalhes...
Observem o Nó 3: a altura da subárvore da esquerda é 2 e da subárvore da direita também é 2. Vejamos agora o Nó 1: a altura da subárvore da esquerda é 1 e da subárvore da direita também é 1. E o Nó 5: a altura da subárvore da esquerda é 1 e da subárvore da direita é 0 (visto que ela não existe). Vocês podem ver todos os nós e não encontrarão subárvore da esquerda e direita com diferença maior que 1.
Uma Árvore AVL mantém seu equilíbrio de altura executando operações de rotação se algum dos nós violar a propriedade da diferença maior que 1. Exemplo 1: para a seguinte árvore, a propriedade da árvore AVL é violada no Nó 5, porque a subárvore esquerda possui altura 2, mas a subárvore da direita tem altura 0, então eles diferem em 2. Entenderam?
Essa diferença de 2 é construída nos dois ramos esquerdos - Ramo 5-4 e Ramo 4-3. Concordam? Se a diferença de 2 for construída por dois ramos esquerdos, chamamos esse caso de um Caso Esquerdo- Esquerdo (Genial, né?). Neste caso, realizamos uma rotação à direita no Ramo 5-4 como mostrado na imagem abaixo de forma a rebalancear a árvore.
Já na imagem abaixo, a Árvore AVL tem sua propriedade violada no Nó 8. A altura da subárvore esquerda é maior do que a altura da subárvore direita em 2. Essa diferença de 2 é construída por um ramo esquerdo (Ramo 8-4) e um ramo direito (Ramo 4-6), logo é um Caso Esquerdo-Direito. Para restaurar o equilíbrio de altura, executamos uma rotação esquerda seguida de uma rotação direita. Vejam...
Então, galera, caso a árvore não esteja balanceada, é necessário seu balanceamento através de rotações. No Caso Esquerda-Esquerda, basta fazer uma rotação simples para direita no nó desbalanceado. No caso Esquerda-Direita, temos que fazer uma rotação dupla, i.e., faz-se uma rotação para esquerda no nó filho e uma rotação para direita no nó desbalanceado.
No caso Direita-Direita, basta fazer uma rotação simples para a esquerda no nó desbalanceado. No caso Direita-Esquerda, temos que fazer uma rotação dupla, i.e., faz-se uma rotação para direita no nó filho, seguida de uma rotação para esquerda no nó desbalanceado. Bacana? Vocês entenderão isso melhor nos exercícios. Vamos ver agora a complexidade logarítmica dessas estruturas.

ÁRVORE BINÁRIA DE BUSCA

ALGORITMO

Espaço

CASO MÉDIO

O ( n )

PIOR CASO

O ( n )

ALGORITMO

Busca

CASO MÉDIO

O ( log n )

PIOR CASO

O ( n )

ALGORITMO

Inserção

CASO MÉDIO

O ( log n )

PIOR CASO

O ( n )

ALGORITMO

Remoção

CASO MÉDIO

O ( log n )

PIOR CASO

O ( n )

ÁRVORE B / ÁRVORE AVL

ALGORITMO

Espaço

CASO MÉDIO

O ( n )

PIOR CASO

O ( n )

ALGORITMO

Busca

CASO MÉDIO

O ( log n )

PIOR CASO

O ( log n )

ALGORITMO

Inserção

CASO MÉDIO

O ( log n )

PIOR CASO

O ( log n )

ALGORITMO

Remoção

CASO MÉDIO

O ( log n )

PIOR CASO

O ( log n )

Grafos

Fiz uma disciplina na faculdade chamada Teoria dos Grafos! Aquilo era absurdamente complexo, mas para concursos a teoria é beeeem mais tranquila e muito rara de cair. Portanto fiquem tranquilos, bacana? Uma definição de grafo afirma que ele é uma estrutura de dados que consiste em um conjunto de nós (ou vértices) e um conjunto de arcos (ou arestas).
Em outras palavras, podemos dizer que é simplesmente um conjunto de pontos e linhas que conectam vários pontos. Ou também que é uma representação abstrata de um conjunto de objetos e das relações existentes entre eles. Uma grande variedade de estruturas do mundo real podem ser representadas abstratamente através de grafos. Professor, pode me passar um exemplo? Claro!
Vejam só como se trata de um conceito bastante abrangente! O Facebook pode ser considerado um grafo (pessoas se interligam através de amizades); um mapa rodoviário pode ser considerado um grafo (cidades se relacionam através de estradas); as eliminatórias de um campeonato de futebol também podem ser consideradas um grafo (times jogam entre si para ganhar o campeonato).
Abaixo temos um exemplo de um grafo que eu desenhei e que nos ajudará a entender melhor a terminologia utilizada. Seguem as premissas:

Ø N = {A, B, C, D, E, F}
Ø G = {(A,B), (B,A), (B,C), (B,D), (C,C), (D,A), (D,C), (E,F)}

§ Nó, Nodo ou Vértice: Qualquer elemento de um conjunto N.

§ Aresta ou Arco: Qualquer elemento de um conjunto A.

§ Nós Adjacentes (Relação de Adjacência): São aqueles nós ligados por um arco (Ex: A é adjacente a D).

§ Arco Incidente (Relação de Incidência): São aqueles arcos que levam a um nó (Ex: (C,D) é incidente em D).

§ Grau: É a quantidade de arcos que partem ou chegam em/de um nó.

§ Caminho: Sequência de arcos que levam de um nó a outro (Ex: AàC <(A,B), (B,D), (D,C)>).

§ Circuito ou Ciclo:É o caminho que leva ao mesmo nó do qual saiu (Ex: <(A,B), (B,D), (D,A)>).

§ Laço: É o circuito de um único arco (<(C,C)>).

§ Ordem: É a quantidade de vértices totais do grafo.

Vamos ver agora alguns conceitos importantes! Um grafo pode ser dirigido - também chamado direcionado, orientado ou dígrafo -, se as arestas tiverem uma direção (imagem da esquerda), ou não dirigido, se as arestas não tiverem direção (imagem central). Se as arestas tiverem associado um peso ou custo, o grafo passa a ser chamado ponderado, valorado ou pesado (imagem da direita).
Um grafo simples é aquele que não contém laços. Um grafo vazio é aquele que contém exclusivamente vértices (não contém arcos). Um grafo misto é aquele que possui arestas dirigidas e não-dirigidas. Um grafo trivial é aquele que possui somente um vértice. Um grafo é denso se contém muitos arcos em relação ao número de vértices e esparso se contém poucos arcos. Como assim, professor?
Um grafo é denso se o seu número de arcos é da mesma ordem que o quadrado do número de vértices; e é esparso se o número de arcos for da mesma ordem que o número de vértices. Um grafo é regular se todos os vértices têm o mesmo grau; e é completo se todo vértice é adjacente a todos os outros vértices (o grafo ao lado é regular e completo).
Um grafo é dito conexo ou conectado quando existir pelo menos um caminho entre cada par de vértices. Caso contrário, ele será dito desconexo, isto é, se há pelo menos um par de vértices que não esteja ligado a nenhuma cadeia (caminho). Vejam a imagem do grafo que eu desenhei lá em cima! Ele é conexo ou desconexo? Ele é desconexo, há um par de vértices (E,F) que não está ligado a nenhum caminho.
Se o grafo for direcionado/orientado, um grafo é dito fortemente conexo se existir um caminho de A à B e de B à A, para cada par (A,B) de vértices de um grafo. Em outras palavras, o grafo é fortemente conexo se cada par de vértices participa de um circuito. Isto significa que cada vértice pode ser alcançável partindo-se de qualquer outro vértice do grafo.
Galera, existem outras maneiras de representar um grafo. Uma das maneiras mais comuns é por meio de uma Matriz de Adjacências. A definição precisa das entradas da matriz varia de acordo com as propriedades do grafo que se deseja representar, porém de forma geral o valor aij guarda informações sobre como os vértices vi e vj estão relacionados (isto é, informações sobre a adjacência de vi e vj).
Para representar um grafo não direcionado, simples e sem pesos, basta que as entradas aij da Matriz A contenham 1 se vi e vj são adjacentes e 0, caso contrário. Se as arestas do grafo tiverem pesos, aij pode conter, ao invés de 1 quando houver uma aresta entre vi e vj, o peso dessa mesma aresta.
Vamos entender? O elemento A11 = 1, significando que o Nó 1 tem adjacência com o Nó 1 (ele mesmo, basta ver a figura); o elemento A12 = 1, significando que o Nó 1 tem adjacência com o Nó 2; elemento A13 = 0, significando que o Nó 1 não tem adjacência com o Nó 3; o elemento A14 = 0, significando que o Nó 1 não tem adjacência com o Nó 4.
O elemento A15 = 1, significando que o Nó 1 tem adjacência com o Nó 5; o elemento A16 = 0, significando que o Nó 1 não tem adjacência com o Nó 3. Galera, agora ficou Fácil de entender, concordam? Lembrando que, se fosse um grafo ponderado, bastaria colocar o peso, em vez de colocar 1 na Matriz de Adjacências. Existem só mais alguns detalhes.
Em grafos não direcionados, as matrizes de adjacência são simétricas ao longo da diagonal principal - isto é, a entrada aij é igual à entrada aji. Matrizes de Adjacência de grafos direcionados, no entanto, não são assim. Num dígrafo sem pesos, a entrada aij da matriz é 1 se há um arco de vi para vj e 0, caso contrário. Há outra maneira de representar também chamada Lista de Adjacências.
Se o grafo é não direcionado, cada entrada é um conjunto de dois nós contendo as duas extremidades da aresta correspondente; se ele for dirigido, cada entrada é uma tupla de dois nós, um indicando o nó de origem e o outro denotando o nó destino do arco correspondente. É bem simples, para cada nó, eu escrevo suas adjacências. No exemplo anterior: Nó 1 = 1, 2, 5; Nó 2 = 1, 3, 5; e assim por diante.
Professor, qual é melhor? Cara, cada representação tem suas vantagens e desvantagens! É fácil encontrar todos os vértices adjacentes a um vértice dada em uma representação lista de adjacência; você simplesmente lê a sua lista de adjacência. Com uma matriz de adjacência em vez disso se tem que pesquisar mais de uma linha inteira, gastando tempo O ( n ).
Se, pelo contrário, deseja realizar um teste de vizinhança em dois vértices (isto é, determinar se eles têm uma aresta entre eles), uma matriz de adjacência proporciona isso na hora. No entanto, este teste de vizinhança em uma lista de adjacências requer tempo proporcional ao número de arestas associado com os dois vértices. Há diversos outros aspectos também a considerar, como tamanho.
Pensem comigo! Para um grafo com uma Matriz de Adjacência esparsa (não densa), uma representação de Lista de Adjacências do grafo ocupa menos espaço, porque ele não usa nenhum espaço para representar as arestas que não estão presentes. Lembram-se da lista? Nós só representamos os nós adjacentes, em contraste com a Matriz de Adjacência. No entanto, quanto mais denso, isso pode mudar.

