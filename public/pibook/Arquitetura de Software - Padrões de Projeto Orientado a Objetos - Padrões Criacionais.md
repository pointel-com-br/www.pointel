# Arquitetura de Software - Padrões de Projeto Orientado a Objetos - Padrões Criacionais

Na arquitetura de software, os padrões de projeto orientados a objetos são soluções reutilizáveis para problemas comuns de design. Os padrões criacionais são um grupo de padrões de projeto que se concentram na criação de objetos de maneira eficiente e flexível. Eles fornecem abordagens para criar objetos de forma desacoplada e configurável, facilitando a manutenção e a extensibilidade do sistema.

Aqui estão alguns exemplos de padrões criacionais amplamente utilizados:

1. Factory Method (Método de Fábrica): O padrão Factory Method fornece uma interface para criar objetos, mas permite que as subclasses decidam qual classe concreta instanciar. Isso promove o desacoplamento entre o código cliente e as classes concretas, permitindo que o cliente seja independente das implementações específicas.

2. Abstract Factory (Fábrica Abstrata): O padrão Abstract Factory fornece uma interface para criar famílias de objetos relacionados sem especificar suas classes concretas. Ele permite que um cliente crie objetos relacionados sem se preocupar com as classes específicas envolvidas, promovendo a criação de famílias de objetos coesas e independentes.

3. Singleton: O padrão Singleton garante que uma classe tenha apenas uma única instância e fornece um ponto de acesso global para essa instância. Isso é útil quando é necessário ter uma única instância de uma classe em todo o sistema, como uma classe de configuração ou um gerenciador de log.

4. Builder (Construtor): O padrão Builder separa a construção de um objeto complexo da sua representação, permitindo que o mesmo processo de construção possa criar diferentes representações do objeto. Isso facilita a criação de objetos complexos passo a passo e permite que o código cliente tenha controle sobre o processo de construção.

5. Prototype (Protótipo): O padrão Prototype permite criar novos objetos a partir de um objeto existente, clonando-o e modificando-o conforme necessário. Isso é útil quando a criação de um objeto é complexa ou cara, e o sistema precisa criar várias variações desse objeto.

6. Object Pool (Piscina de Objetos): O padrão Object Pool mantém um conjunto de objetos pré-instantâneos e os gerencia para serem reutilizados quando necessário. Em vez de criar e destruir objetos repetidamente, o padrão Object Pool pode melhorar o desempenho ao reutilizar objetos existentes, especialmente quando a criação de objetos é custosa.

Esses são apenas alguns exemplos de padrões criacionais. Cada padrão aborda um aspecto específico da criação de objetos, como a flexibilidade, o desacoplamento, o controle de acesso e a reutilização. A escolha adequada dos padrões criacionais pode melhorar a flexibilidade, a extensibilidade e a eficiência do sistema.
