# Arquitetura de Software - SOLID

O SOLID é um acrônimo que representa cinco princípios da programação orientada a objetos e design de software. Esses princípios, formulados por Robert C. Martin, são diretrizes para criar sistemas de software flexíveis, extensíveis e de fácil manutenção. Aqui estão os cinco princípios SOLID:

1. Princípio da Responsabilidade Única (Single Responsibility Principle - SRP): Uma classe deve ter uma única responsabilidade e motivo para mudar. Isso significa que uma classe deve ter apenas uma única funcionalidade ou responsabilidade, evitando que ela se torne muito grande ou complexa. Isso facilita a manutenção, reutilização e testabilidade do código.

2. Princípio Aberto/Fechado (Open/Closed Principle - OCP): As entidades de software (classes, módulos, etc.) devem estar abertas para extensão, mas fechadas para modificação. Isso significa que o código existente não deve ser modificado quando novos recursos ou comportamentos precisarem ser adicionados. Em vez disso, deve ser possível estender o código existente por meio de herança, implementação de interfaces ou outros mecanismos.

3. Princípio da Substituição de Liskov (Liskov Substitution Principle - LSP): As subclasses devem ser substituíveis por suas classes base sem afetar a integridade do sistema. Isso significa que uma classe derivada deve ser capaz de ser usada em qualquer lugar onde sua classe base é esperada, sem causar problemas de comportamento ou violar as precondições e pós-condições.

4. Princípio da Segregação de Interface (Interface Segregation Principle - ISP): Os clientes não devem ser forçados a depender de interfaces que não utilizam. Esse princípio sugere que as interfaces devem ser coesas e específicas para os clientes que as utilizam. Evite interfaces "gordas" que forçam os clientes a implementar métodos que não precisam.

5. Princípio da Inversão de Dependência (Dependency Inversion Principle - DIP): Dependa de abstrações, não de implementações concretas. Esse princípio incentiva a dependência em interfaces ou classes abstratas em vez de depender de classes concretas. Isso promove a flexibilidade, o desacoplamento e a reutilização de código.

Esses princípios SOLID são diretrizes importantes para criar um código modular, flexível e de fácil manutenção. Eles promovem a coesão, o baixo acoplamento e a extensibilidade em sistemas de software orientados a objetos. Ao seguir esses princípios, você pode melhorar a qualidade do software, facilitar a evolução do sistema e tornar o código mais resiliente a mudanças.

Escrever um código que satisfaça os requisitos atuais, e que também possa satisfazer requisitos futuros facilmente, deve ser o objetivo de qualquer desenvolvedor - evoluir com o tempo é o único fator que pode manter o código-fonte. Princípios SOLID são cinco princípios de design de código orientado a objeto para tornar o código mais entendível, claro, flexível, conciso e tolerante a mudanças; e para aumentar a adesão do código aos princípios da orientação a objetos.
SOLID é um acrônimo para cada um dos cinco princípios que fazem parte desse grupo:

§ Single Responsability Principle

§ Open/Closed Principle

§ Liskov Substitution Principle

§ Interface Segregation Principle

§ Dependency Inversion Principle

Esses cinco princípios de desenvolvimento de software são diretrizes a serem seguidas ao criar software para facilitar o dimensionamento e a manutenção. Veja bem, alguns desses princípios podem parecer semelhantes, mas não visam o mesmo objetivo. Para simplificar o acompanhamento, usarei a palavra "Classe", mas observe que ela também pode se aplicar a uma função, método ou módulo.

Índice

1 Responsabilidade Única

2 Aberto-Fechado

3 Substituição de Liskov

4 Segregação de Interface

5 Inversão de Dependência

Responsabilidade Única

Uma classe dever ter uma única responsabilidade.
Se uma classe tiver muitas responsabilidades, aumenta a probabilidade de ocorrerem bugs, uma vez que alterar uma de suas responsabilidades pode afetar as outras sem que você saiba. Para resolver esse problema, temos o Princípio da Responsabilidade Única. O objetivo desse princípio é separar comportamentos para que, se surgirem bugs como resultado de sua alteração, isso não afete outros comportamentos não relacionados.
Na imagem, temos um robô que tem muitas responsabilidades: ele é chef, jardineiro, pintor e motorista - o ideal é que tivéssemos um robô para cada uma dessas responsabilidades.

Aberto-Fechado

Classes devem ser abertas para extensão, mas fechadas para modificação.
Alterar o comportamento atual de uma classe afetará todos os sistemas que usam essa classe. Se você deseja que a classe execute mais funções, a abordagem ideal é adicionar às funções que já existem e, não, alterá-las. Aberto para extensão significa que, ao receber uma nova requisição, é possível adicionar um novo comportamento. Fechado para modificação significa que, para introduzir um novo comportamento (extensão), não é necessário modificar o código existente.
O objetivo desse princípio é estender o comportamento de uma classe sem alterar o comportamento existente dela. Isso evita a ocorrência de bugs onde quer que a classe esteja sendo usada. Na imagem à esquerda, observem que tínhamos um robô que cortava, teve seu comportamento modificado e que agora passou a pintar; na imagem à direita, tínhamos um robô que cortava, foi estendido e agora aprendeu também a pintar.

Substituição de Liskov

Se S é um subtipo de T, então objetos do tipo T em um programa podem ser substituídos por objetos do tipo S sem alterar as propriedades desejáveis desse programa.
Quando uma classe-filha não pode executar as mesmas ações que sua classe-pai, isso pode causar bugs. Se você tiver uma classe e criar outra classe a partir dela, ela se tornará pai e a nova classe se tornará filha. A classe-filha deve ser capaz de fazer tudo o que a classe-pai pode fazer. Este processo é chamado de Herança. A classe-filha deve ser capaz de processar as mesmas solicitações e entregar o mesmo resultado que a classe-pai ou pode entregar um resultado do mesmo tipo.
O objetivo desse princípio é reforçar a consistência para que a classe-pai ou sua classe-filha possam ser usadas da mesma maneira sem erros. A imagem à esquerda mostra que a classe-pai entrega café (pode ser qualquer tipo de café). É aceitável que a classe-filha entregue cappuccino por ser um tipo específico de café, mas não é aceitável entregar água. Se a classe-filha não atender a esses requisitos, isso significa que a classe-filha foi alterada completamente e viola esse princípio.
Já a imagem à direita mostra que Eden (que é filho de Sam) também faz café (cappuccino), já que ele pode executar as mesmas ações que sua classe-pai (Sam).

Segregação de Interface

Clientes não devem ser forçados a depender de métodos que não utilizam.
Quando uma classe é obrigada a executar ações que não são úteis, trata-se de um desperdício e pode produzir bugs inesperados se a classe não tiver a capacidade de executar essas ações. Uma classe deve executar apenas as ações necessárias para cumprir seu papel. Qualquer outra ação deve ser removida completamente ou movida para outro lugar se puder ser utilizada por outra classe no futuro. Entendido?
O objetivo desse princípio é dividir um conjunto de ações em conjuntos menores para que uma classe execute apenas o conjunto de ações de que necessita. Na imagem à esquerda, temos dois robôs: um com antena e outro sem antena. E todos os robôs possuem três ações: girar, rodar os braços e balançar as antenas. Ora, se o segundo robô não possui antena, como ele conseguirá executar a terceira função? Ele não conseguirá, logo essa ação é inútil!
Já na imagem à direita, também temos dois robôs: um com antena e outro sem antena. No entanto, temos uma divisão de ações: ações para robôs que podem girar; ações para robôs que podem rodar os braços; e ações para robôs que podem balançar as antenas. Logo, nenhum robô possui uma função inútil que não podem executar e que são apenas um desperdício capaz de produzir bugs inesperados. Bacana?

Inversão de Dependência

Módulos de alto nível não devem depender de módulos de baixo nível: ambos devem depender da abstração.
As abstrações não devem depender de detalhes: detalhes devem depender de abstrações.
Em primeiro lugar, vamos definir os termos usados aqui de forma mais simples:

§ Módulo/Classe de Alto Nível: classe que executa uma ação com uma ferramenta;

§ Módulo/Classe de Baixo Nível: ferramenta necessária para executar uma ação;

§ Abstração: representa uma interface que conecta as duas classes;

§ Detalhes: como a ferramenta funciona;

Este princípio diz que uma classe não deve ser fundida com a ferramenta que usa para executar uma ação. Em vez disso, ele deve ser fundido à interface que permitirá que a ferramenta se conecte à classe. Também diz que tanto a classe quanto a interface não devem saber como a ferramenta funciona. No entanto, a ferramenta precisa atender à especificação da interface. O objetivo desse princípio é reduzir a dependência de uma classe de alto nível na classe de baixo nível, introduzindo uma interface.
Na imagem à esquerda, temos um robô que possui um braço exclusivamente para cortar pizzas; já na imagem à direita, temos um robô que possui um braço que pode ser adaptado para diversas ações - inclusive cortar pizza. Note que eu posso adaptar uma outra ferramenta no braço do robô para que ele possa realizar outra ação. Logo, temos uma inversão: as classes de alto nível deixam de depender das classes de baixo nível e passam a depender apenas da abstração (interface).

Para finalizar, vamos falar um pouquinho sobre coesão e acoplamento. A implementação de qualquer classe deve ser coesa, isto é, toda classe deve implementar uma única funcionalidade ou serviço. Especificamente, todos os métodos e atributos de uma classe devem estar voltados para a implementação do mesmo serviço. Uma outra forma de explicar coesão é afirmando que toda classe deve ter uma única responsabilidade no sistema.
Dito de outra forma, deve existir um único motivo para modificar uma classe. Ok? Bem, a coesão tem algumas vantagens: facilita a implementação de uma classe, bem como o seu entendimento e manutenção; facilita a alocação de um único responsável por manter uma classe; e facilita o reuso e teste de uma classe, pois é mais simples reusar e testar uma classe coesa do que uma classe com várias responsabilidades.

Já o acoplamento é a força da conexão entre duas classes. Trata-se da medida em que as partes de um programa estão interconectadas entre si. Pode-se dizer que se refere à quantidade de dependência entre os elementos de um programa. Quanto menor o acoplamento, melhor será a reutilização de código e a manutenção do programa. Na tabela seguinte, veremos um conjunto de propriedades de projeto relacionadas a cada um dos princípios:

PRINCÍPIO SOLID

RESPONSABILIDADE ÚNICA

DESCRIÇÃO

Uma classe deve ter um, e somente um, motivo para mudar.

PROPRIEDADES

Coesão

PRINCÍPIO SOLID

ABERTO/FECHADO

DESCRIÇÃO

Objetos ou entidades devem estar abertos para extensão, mas fechados para modificação.

PROPRIEDADES

Extensibilidade

PRINCÍPIO SOLID

SUBSTITUIÇÃO DE LISKOV

DESCRIÇÃO

Uma classe derivada deve ser substituível por sua classe base.

PROPRIEDADES

Extensibilidade

PRINCÍPIO SOLID

SEGREGAÇÃO DE INTERFACE

DESCRIÇÃO

Uma classe não deve ser forçada a implementar interfaces e métodos que não irá utilizar.

PROPRIEDADES

Coesão

PRINCÍPIO SOLID

INVERSÃO DE DEPENDÊNCIA

DESCRIÇÃO

Dependa de abstrações e, não, de implementações.

PROPRIEDADES

Acoplamento

