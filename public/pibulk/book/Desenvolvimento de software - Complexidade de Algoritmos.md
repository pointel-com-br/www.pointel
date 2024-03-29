# Desenvolvimento de software - Complexidade de Algoritmos

Galera, por que estudamos a complexidade de algoritmos? Para determinar o custo computacional (tempo, espaço, etc) para execução de algoritmos. Em outras palavras, ela classifica problemas computacionais de acordo com sua dificuldade inerente. E importante entender isso para posteriormente estudarmos a complexidade de métodos de ordenação e métodos de pesquisa.

Nosso estudo aqui será bastante superficial por duas razões: primeiro, concursos cobram pouco e, quando cobram, querem saber as complexidades dos métodos de ordenação mais conhecidos; segundo, essa é uma disciplina absurdamente complexa que envolve Análise Assintótica, Cálculo Diferencial, Análise Polinomial (Linear, Exponencial, etc). Logo, vamos nos ater ao que cai em concurso público!

Só uma pausa: passei dias sem dormir na minha graduação por conta dessa disciplina! Na UnB, ela era ministrada pelo Instituto de Matemática e era considerada a disciplina mais difícil do curso :-(. Continuando: lá em cima eu falei sobre custo computacional! Ora, para que eu escolha um algoritmo, eu preciso definir algum parâmetro.

Podemos começar com Tempo! Um algoritmo que realiza uma tarefa em 20 minutos é melhor do que um algoritmo que realiza uma tarefa em 20 dias? Não é uma boa estratégia, porque depende do computador que eu estou utilizando (e todo o hardware correspondente), depende das otimizações realizadas pelo compilador, entre outras variáveis.

Vamos analisar, então, Espaço! Um algoritmo que utiliza 20Mb de RAM é melhor do que um algoritmo que utiliza 20Gb? Seguem os mesmos argumentos utilizados para o Tempo, ou seja, não é uma boa opção! E agora, o que faremos? Galera, eu tenho uma sugestão: investigar a quantidade de vezes que operações são executadas na execução do algoritmo!

Essa estratégia independe do computador (e hardware associado), do compilador, da linguagem de programação, das condições de implementação, entre outros fatores - ela depende apenas da qualidade inerente do algoritmo implementado. Utilizam-se algumas simplificações matemáticas para se ter uma ideia do comportamento do algoritmo. Prosseguindo...

Dada uma entrada de dados de tamanho N, podemos calcular o custo computacional de um algoritmo em seu pior caso, médio caso e melhor caso! Como assim, professor? Para entender isso, vamos utilizar a metáfora de um jogo de baralho! Imaginem que eu estou jogando contra vocês. Vocês embaralham e me entregam 5 cartas, eu embaralho novamente e lhes entrego 5 cartas.

Quem joga baralho sabe que uma boa alternativa para grande parte dos jogos é ordenar as cartas em ordem crescente de modo a encontrar mais facilmente a melhor carta para jogar. Agora observem... vocês receberam as seguintes cartas (nessa ordem): 4, 5, 6, 7, 8. Já eu recebi as seguintes cartas (também nessa ordem): 8, 7, 6, 5, 4 - nós queremos analisar a complexidade de ordenação dessas cartas.

Ora, convenhamos que vocês possuem o melhor caso, porque vocês deram a sorte de as cartas recebidas já estarem ordenadas. Já eu peguei o pior caso, porque as cartas estão ordenadas na ordem inversa. Por fim, o caso médio ocorre caso as cartas recebidas estejam em uma ordem aleatória. Com isso, espero que vocês tenham entendido o sentido de pior, médio e melhor casos.

Vamos partir agora para o estudo da Notação Big-O (ou Notação Assintótica)! Isso é simplesmente uma forma de representar o comportamento assintótico de uma função. No nosso contexto, ela busca expressar a quantidade de operações primitivas executadas como função do tamanho da entrada de dados. Vamos ver isso melhor!

A Notação Big-O é a representação relativa da complexidade de um algoritmo. É relativa porque só se pode comparar maçãs com maçãs, isto é, você não pode comparar um algoritmo de multiplicação aritmética com um algoritmo de ordenação de inteiros. É uma representação porque reduz a comparação entre algoritmos a uma simples variável por meio de observações e suposições.

E trata da complexidade porque se é necessário 1 segundo para ordenar 10.000 elementos, quanto tempo levará para ordenar 1.000.000? A complexidade, nesse exemplo particular, é a medida relativa para alguma coisa. Vamos ver isso por meio de um exemplo: soma de dois inteiros! A soma é uma operação ou um problema, e o método para resolver esse problema é chamado algoritmo!

Vamos supor que no algoritmo de somar (mostrado acima), a operação mais cara seja a adição. Observem que se somarmos dois números de 100 dígitos, teremos que fazer 100 adições. Se somarmos dois números de 10.000 dígitos, teremos que fazer 10.000 adições. Perceberam o padrão? A complexidade (aqui, número de operações) é diretamente proporcional ao número n de dígitos, i.e., O(n).

Quando dizemos que um algoritmo é O(n2), estamos querendo dizer que esse algoritmo é da ordem de grandeza quadrática! Ele basicamente serve para te dizer quão rápido uma função cresce, por exemplo: um algoritmo O(n) é melhor do que um algoritmo O(n2), porque ela cresce mais lentamente! Abaixo vemos uma lista das classes de funções mais comuns em ordem crescente de crescimento:

Nome - Notação

Constante - 0 de ( 1 )

Logarítmica - O de ( log n )

Polilogarítmica - O de [ ( log n ) c ]

Linear - O de ( n )

Linear Logarítmica - O de ( n log n )

Quadrática - O de ( n elevado a 2 )

Cúbica - O de ( n elevador a 3 )

Polinomial - O de ( n elevado a c )

Exponencial - O de ( c elevado a n )

Fatorial - O de ( n ! )

Quando dizemos que o Shellsort é um algoritmo O(n2), estamos querendo dizer que a complexidade (nesse caso, o número de operações) para ordenar um conjunto de n dados com o Algoritmo Shellsort é proporcional ao quadrado do número de elementos no conjunto! Grosso modo, para ordenar 20 números, é necessário realizar 400 operações (sem entrar em detalhes sobre a operação em si, nem sobre as simplificações matemáticas que são realizadas).

Entender como se chega a esses valores para cada método de ordenação e pesquisa é extremamente complexo! Galera, apesar de eu nunca ter visto isso em prova, é bom que vocês saibam que existem outras notações! Utiliza-se Notação Big-O (O) para pior caso; Notação Big- Ômega para melhor caso (Q); e Notação Big-Theta (0) para caso médio.

Como na prática utiliza-se Big-O para tudo, o que eu recomendo (infelizmente, porque eu sei que vocês têm zilhões de coisas para decorar) é memorizar o pior caso dos principais métodos. Dessa forma, é possível responder a maioria das questões de prova sobre esse tema. Eventualmente, as questões pedem também caso médio e melhor caso, mas é menos comum. Bacana? :-)

Por último, uma pergunta muito frequente: Professor, já vi questões cobrando Logaritmo na Base 10, Logaritmo na Base 2, Logaritmo Neperiano, etc... isso não está errado? Galera, suponha que um algoritmo levou um tempo 0(log1O n). Você também poderia dizer que levou um tempo 0(lg n) (ou seja, 0(log2 n)). Você pode utilizar qualquer base.

Sempre que a base do logaritmo é uma constante, não importa a base que usamos na notação assintótica. Por que não? Porque, para a notação assintótica, isso é completamente irrelevante. Beleza? Então, não se prendam a base do logaritmo, qualquer uma pode ser utilizada na representação de complexidade assintótica de algoritmos.
