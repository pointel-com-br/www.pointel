# Engenharia de Software e Sistemas - Padrões de Projeto - Comportamentais

Índice

1 Chain of Responsability

2 Command

3 Interpreter

4 Iterator

5 Mediator

6 Memento

7 Observer

8 State

9 Strategy

10 Template Method

11 Visitor

Chain of Responsability

Esse padrão evita o acoplamento do remetente de uma requisição ao seu receptor ao dar a mais de um objeto a chance de lidar com a requisição.
Esse padrão de projeto deve ser utilizado quando se deseja emitir uma solicitação para um dentre vários objetos, sem especificar explicitamente o receptor ou quando mais de um objeto é capaz de lidar com a requisição e ele não for conhecido a priori. Esse padrão também é comumente utilizado quando um conjunto de objetos que podem lidar com uma requisição forem especificados dinamicamente.
Esse padrão acaba com estruturas de decisão ao criar uma cadeia de objetos em que se passa a responsabilidade até encontrar aquele que pode respondê-la. Consideremos a hipótese de uma loja virtual que permite pagamento online por meio de diversos bancos. Dado um parâmetro, deve-se identificar qual banco deve ser utilizado para o pagamento. Esse problema pode ser resolvido com outros padrões, mas o Chain of Responsability fornece uma solução com fraco acoplamento.
Assim, cada elemento da cadeia pode implementar a requisição da maneira que quiserem. Assim, não há uma associação direta entre o remetente e o receptor que irá lidar com a requisição.

Command

Esse padrão encapsula a requisição de um objeto, portanto permitindo que se parametrize os clientes com diferentes requisições.
Esse padrão de projeto deve ser utilizado quando se deseja parametrizar objetos para realizar alguma execução ou também para especificar, enfileirar e executar requisições a qualquer momento. Ele também é utilizado para suportar mudanças de log de maneira que possa ser reaplicado no caso de uma queda no sistema. Entenderam? Considerem a hipótese de um interruptor que ligue ou desligue uma lâmpada.
Esse interruptor encapsula uma requisição, de tal modo que se possa utilizá-lo para diferentes dispositivos. Em outras palavras, se eu retirar um interruptor de uma lâmpada, conectar adequadamente aos fios de um computador, é possível ligar/desligar o computador com o mesmo interruptor. Logo, o interruptor tem sua interface encapsulada, logo pode ser utilizado em qualquer dispositivo que tenha uma interface Ligar/Desligar.
Imaginem agora uma classe que faz diversas conexões a um banco de dados. Não é recomendável que ela tenha um método que se conecte diretamente ao banco, portanto encapsula-se essa conexão, diminuindo a dependência.

Interpreter

Esse padrão, dada uma linguagem, define uma representação para sua gramática em conjunto com um interpretador que utiliza a representação para interpretar sentenças na linguagem.
Esse padrão de projeto deve ser utilizado quando houver uma linguagem para interpretar e quando se puder representar declarações nessa linguagem como árvores sintáticas abstratas. Ele funciona bem quando a gramática é simples, permitindo um fácil gerenciamento e quando a eficiência não é um fator crítico de sucesso. Basta lembrar do Java, que é uma linguagem interpretada.
O que isso quer dizer esse negócio de interpretada, professor? Bem, isso significa que o código fonte é compilado em um bytecode, que é então posteriormente interpretado por um interpretador. Dessa forma, esse padrão de projeto é utilizado nos casos em que é possível definir uma linguagem com uma gramática que possa ser, posteriormente, interpretada.

Iterator

Esse padrão fornece uma maneira de acessar elementos de um objeto agregado sequencialmente sem expor sua representação interna.
Esse padrão de projeto deve ser utilizado quando se deseja acessar o conteúdo de um objeto agregado sem expor a sua representação interna e para fornecer uma interface uniforme para diferentes estruturas de agregação. Ele também é recomendado para suportar múltiplos acessos a objetos agregados. Entendido? Vamos ver um exemplo!
Considerem a hipótese de se desejar percorrer sequencialmente quatro coleções distintas (Lista, Arrays, Map e Set) de objetos bastante complexos. Em uma situação normal, deve-se conhecer a representação interna de cada uma dessas coleções. O Iterator permite que se percorra todas essas coleções sem precisar saber detalhes de seu funcionamento.

Mediator

Esse padrão define um objeto que encapsula a forma como um conjunto de objetos interagem, promovendo um fraco acoplamento ao evitar que objetos se refiram aos outros explicitamente.
Esse padrão de projeto deve ser utilizado quando um conjunto de objetos se comunicar de maneira bem definida, porém complexa e quando o reúso de um objeto for difícil por referenciar e se comunicar com muitos outros objetos. Ademais, ele é utilizado quando um comportamento distribuído entre diversas classes puder ser customizado sem a criação de muitas subclasses.
Considerem a hipótese de um software complexo com grandes quantidades de classes, de tal modo que a lógica de processamento está distribuída entre elas. Todo mundo sabe que, há cada manutenção ou refatoração, o desenho do software pode se tornar mais complexo e a comunicação entre as classes pode ser mais difícil de ler entender.
Logo, o Padrão Mediator permite que a comunicação entre objetos seja encapsulada em um outro objeto mediador. Assim, não haverá mais uma comunicação direta entre as classes, reduzindo o acoplamento, garantindo que todos fiquem mais livres para serem modificados e diminuindo a complexidade de comunicação entre objetos.

Memento

Esse padrão captura e externaliza o estado interno de um objeto, sem violar seu encapsulamento, de maneira que o objeto possa ser restaurado posteriormente.
Esse padrão de projeto deve ser utilizado quando uma parte do estado de um objeto precisar ser armazenada, de forma que possa ser recuperada posteriormente. Ele é utilizado, também, para evitar que uma interface direta para obter um estado exponha detalhes de implementação e quebrem o encapsulamento do objeto. Considerem a hipótese de um editor de texto que guarde o estado interno do objeto.
Em outras palavras, o que o usuário está digitando, aí ele deleta uma palavra, mas se arrepende e deseja voltar ao estado anterior. Bem, o memento oferece uma maneira de desfazer ações sem ter acesso ao que estava sendo escrito, ele apenas retorna o estado anterior, mas sem olhar o que estava escrito. Logo, o Padrão Memento permite a captura e externalização do estado interno de um objeto, sem violar seu encapsulamento.
Ele captura o que estava escrito e mostra ao usuário, mas sem acesso direto ao que estava escrito. Assim, pode-se cancelar operações e desfazer alterações para retornar ao estado anterior.

Observer

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.Esse padrão de projeto deve ser utilizado quando uma mudança em um objeto requisitar mudanças em outros objetos e não se souber quantos objetos necessitam ser modificados. Ele também é utilizado quando uma abstração possuir dois aspectos, sendo um dependente do outro. Além disso, sua utilização é recomendada quando um objeto for capaz de notificar outros sem assumir quem são. Certinho?
Considerem a hipótese de uma tabela de classificação do campeonato brasileiro com um gráfico de pizza informando vitórias, empates e derrotas de um determinado time, assim como um gráfico com a variação de posição do time do campeonato. Aí chega o domingão, ocorrem 10 jogos e o estagiário altera a tabela com os novos dados. E agora? Tem que atualizar os gráficos um a um? Os gráficos ficarão desatualizados? Não haverá nem uma notificação de novos dados?
Ele cria uma dependência dos gráficos em relação à tabela de modo que, quando a tabela muda de estado, os gráficos são atualizados automaticamente.

State

Esse padrão permite a um objeto alterar o seu comportamento quando o seu estado interno for modificado.
Esse padrão de projeto deve ser utilizado quando o comportamento de um objeto depender de seu estado e ele deve mudar este comportamento em tempo de execução de acordo com este estado. Ademais, é recomendado quando operações tiverem declarações condicionais grandes que dependam do estado do objeto. Considerem a hipótese do jogo Super Mario Bros! Lembram-se de quando ele conseguia uma flor de fogo?
Se ele estivesse pequeno, ele ficava grande e pegando fogo! Se ele estivesse grande, ele ficava pegando fogo! Se já estivesse pegando fogo, ganhava 1000 pontos! Se tivesse com uma capa de voo, perdia a capa e ficava pegando fogo! Logo, notem que o estado futuro depende de seu estado atual e o estado futuro é decidido em tempo de execução, isto é, durante o jogo. Esse padrão elimina a necessidade de condicionais complexos. Por que?
Porque pode haver dezenas ou centenas de estados possíveis. A grande vantagem é que esta solução torna mais simples adicionar estados e suas transições.

Strategy

Esse padrão define uma família de algoritmos, encapsula cada um e faz deles intercambiáveis.
Esse padrão de projeto deve ser utilizado quando várias classes relacionadas diferirem apenas em seus comportamentos e que houver necessidade de diferentes variantes de um algoritmo. Ele também é utilizado quando uma classe definir muitos comportamentos e eles aparecerem como declarações condicionais em suas operações. Considerem a hipótese de uma escola querer organizar os meninos e as meninas por ordem de idade.
Há uma família de algoritmos capaz de realizar essa operação (BubbleSort, QuickSort, Heapsort, etc). Uma maneira de realizar essa operação é por meio de operadores condicionais (if- else), mas isso pode ser trabalhoso em grandes quantidades. Uma boa estratégia seria encapsular os algoritmos de ordenação, de modo que se possa trocar de algoritmo sempre que quiser. Basta chamar o método OrdenaAluno com os parâmetros sexoAluno e algoritmoOrdenacao.
Assim, é possível chamar o método ordenaAluno(menino, bubbleSort) ou ordenaAluno(menina, mergeSort), etc, diminuindo o acoplamento.

Template Method

Esse padrão define o esqueleto de um algoritmo dentro de uma operação, deixando alguns passos a serem preenchidos pelas subclasses.
Esse padrão de projeto deve ser utilizado quando se deseja implementar a parte invariante de um algoritmo e deixar que as subclasses implementem o comportamento variável. Ele também é recomendado quando comportamentos comuns entre subclasses forem fatorados e localizados em uma classe comum, para evitar duplicação de código. Considerem a hipótese de uma franquia de McDonald's fabricando um sanduíche.
Bem, o cliente pode pedir para colocar mais queijo, tirar os picles, adicionar ketchup, não colocar sal, entre outras opções. No entanto, observem que operações como: abrir o pão, posicionar o hambúrguer no meio e fechar o pão são operações que sempre irão ocorrer. Logo, esse esqueleto de algoritmo jamais irá mudar. Já as opções de condimentos, verduras, etc podem ser modificadas de acordo com o gosto do cliente.
Sendo assim, a parte invariável será implementada na classe abstrata e a parte variável será implementada pelas classes filhas de acordo com as necessidades do usuário.

Visitor

Esse padrão representa uma operação a ser realizada sobre elementos de uma estrutura de objetos e permite definir uma operação sem mudar as classes dos elementos sobre os quais opera.
Esse padrão deve ser utilizado quando muitas operações distintas e não relacionadas precisarem ser executadas sobre uma estrutura de objetos e se quer evitar a poluição das classes com essas operações. Ademais, são recomendadas quando as classes que definem a estrutura do objeto raramente forem modificadas. Considerem a hipótese de uma compra em um supermercado. O carrinho de compras é a estrutura de dados que contém um conjunto de elementos.
Ao finalizar a compra, deve-se passar a responsabilidade para o caixa (Visitor). A partir deste momento, ele estará no comando, porque ele que realizará a soma dos preços, pesará as frutas, verduras, vegetais, etc (entre outras operações). Logo, algumas operações se aplicam a alguns elementos, mas não se aplicam a outros, isto é, uma cerveja já possui um valor, mas uma maça precisa ser pesada. No entanto, ambas fazem parte da mesma estrutura de dados.

