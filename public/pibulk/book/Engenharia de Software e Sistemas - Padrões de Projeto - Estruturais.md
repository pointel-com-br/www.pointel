# Engenharia de Software e Sistemas - Padrões de Projeto - Estruturais

Índice

1 Adapter

2 Bridge

3 Composite

4 Decorator

5 Façade

6 Flyweight

7 Proxy

Adapter

Esse padrão converte a interface de uma classe em outra interface que normalmente não poderiam trabalhar juntas por serem incompatíveis.
Esse padrão de projeto deve ser utilizado quando se quer usar uma classe e sua interface não é compatível com aquela de que você necessita. Deve ser usado, também, quando se quer criar classes reusáveis que cooperem com classes que não têm necessariamente interfaces compatíveis. Essa classe funciona como um adaptador de tomada. Frequentemente, quer se utilizar uma tomada de três pinos, porém a tomada disponível só permite dois pinos.
Usa-se, então, um adaptador que converte a interface de uma das tomadas permitindo que se faça a conexão normalmente. Ela permite que um objeto cliente utilize serviços de outros objetos com interfaces diferentes. Considerem a hipótese de um objeto que contenha dados de um formulário de Vistos de Imigração do sistema da polícia federal, como Data de Nascimento (no formato DD:MM:AAAA).
Porém, esse objeto deve se comunicar com outro objeto do sistema da embaixada americana, que adota o formato MM:DD:AAAA. Nesse caso, um Adapter seria extremamente oportuno!

Bridge

Esse padrão desacopla uma interface de sua implementação, de forma que ambas possam variar independentemente.
Esse padrão de projeto deve ser utilizado quando se deseja evitar um vínculo permanente entre uma abstração e sua implementação. Ele é recomendado também quando se quer evitar que mudanças na implementação de uma abstração causem impacto nos clientes, isto é, seu código não deve ter que ser recompilado. O Bridge fornece um nível de abstração maior que o Adapter, na medida em que permite variações independentes da interface e da implementação.
Ele provê alto nível de desacoplamento de componentes, fazendo uma ponte entre as hierarquias de classes relacionadas. Esse padrão de projeto é um pouco complicado de se entender, portanto prestem atenção! Considerem a hipótese de um conjunto de janelas gráficas que funcionem em diversas plataformas (Windows, Linux, Mac, etc). Professor, por que não usar o Adapter? De fato, ele poderia adaptar interfaces para cada uma das plataformas.
No entanto, há dezenas de tipos de janelas gráficas (Diálogo, Aviso, Erro, etc), tornando a utilização inviável para grandes quantidades. Uma ideia melhor seria criar uma interface para plataformas e outra para janelas. A primeira conteria os elementos comuns das plataformas e teria classes concretas específicas para implementar janelas em Linux, Mac, etc; e a segunda conteria elementos comuns das janelas e teria classes concretas específicas para implementar janelas Aviso, Erro, etc.
Logo, ao chamar um método da classe concreta da interface de janelas, ela realizará chamadas aos métodos concretos da interface de plataformas. Assim, caso se queira adicionar mais tipos de janelas ou mais plataformas, não haverá impacto no cliente, não haverá recompilação de código nem vínculo entre interfaces de um e implementações de outros. O desacoplamento permite que se modifique o código da interface sem alterar a implementação das janelas e vice-versa.
Notem que, assim, pode-se combinar as interfaces e implementações de quaisquer maneiras possíveis - essa é vantagem do padrão Bridge. Esse padrão nos lembra do padrão bridge.

Composite

Esse padrão compõe objetos em estruturas de árvore para representar hierarquias parte-todo, permitindo aos clientes tratarem objetos individuais e composições de objetos uniformemente.
Esse padrão de projeto deve ser utilizado quando se deseja representar hierarquias parte-todo de objetos e quando se deseja que os clientes ignorem a diferença entre composições de objetos e objetos individuais. Assim, eles tratarão todos os objetos em uma estrutura composta uniformemente. Considerem a hipótese de uma interface gráfica composta de vários objetos. Em muitos casos, esses objetos são compostos de outros objetos. Exemplo de implementação:
Por meio de uma árvore de forma transparente para o cliente - ele não precisa saber de nada disso. Assim, ele não deve diferenciar objetos individuais (folhas) de objetos compostos (nós).

Decorator

Esse padrão anexa responsabilidades adicionais a um objeto dinamicamente. Fornece uma alternativa flexível em relação à herança para estender funcionalidades.
Esse padrão de projeto deve ser utilizado quando se quer adicionar responsabilidades a objetos individuais dinâmica e transparentemente, isto é, sem afetar outros objetos. Também é utilizado quando extensões por subclasses forem impraticáveis, tendo em vista o possível número de extensões independentes. Considerem a hipótese de um Subway! Usando-se herança, cria-se uma classe abstrata sanduíche e várias classes concretas para implementá-la.
No entanto, há sanduíches com almôndega, sem queijo, com tomate, sem cebola, etc. É customizável, portanto é completamente inviável construir classes concretas para cada tipo de sanduíche, devido a gigantesca quantidade de combinações. O Padrão Decorator sugere que o objeto sanduíche anexe diversas responsabilidades dinamicamente. Dessa forma, em tempo de execução, à medida que se adicione um novo ingrediente, cria-se mais uma responsabilidade.
Ao contrário da herança, que aplica funcionalidades a todos os seus objetos, o Decorator aplica funcionalidades apenas a um objeto específico.

Façade

Esse padrão oferece uma interface unificada para um conjunto de interfaces em um subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.
O Padrão de Projeto Façade (também é um dos mais importantes) deve ser utilizado quando se desejar fornecer uma interface simples para um subsistema complexo ou também quando se deseja dividir em camadas os subsistemas. É também utilizando quando existem diversas dependências entre clientes e as classes de implementação de uma abstração. Considerem a hipótese de um banco com um sistema legado de informações de crédito muito complexo.
Esse sistema deve interagir com um sistema de banco de dados recém implementado e moderno. Para que ele acesse o sistema legado, pode-se utilizar o padrão Façade, uma vez que ele facilita a utilização por meio de uma interface de alto nível e, dessa forma, não há necessidade de se interagir diretamente com o sistema complexo.

Flyweight

Esse padrão utiliza compartilhamento para suportar eficientemente grandes quantidades de objetos de baixa granularidade.
Esse padrão de projeto deve ser utilizado quando uma aplicação usa grande número de objetos e os custos de armazenamento forem altos. Deve ser utilizado, também, quando muitos grupos de objetos puderem ser substituídos por relativamente poucos objetos compartilhados, uma vez que os estados extrínsicos forem removidos. Considerem a hipótese de um texto escrito no Microsoft Word, em que cada caractere seja um objeto que contenha posição, formato e tamanho.
Isso poderia ocupar toda memória disponível no sistema, mas percebam que vários caracteres se repetem diversas vezes (Ex: letra A) e eles são exatamente iguais, muda-se somente a posição (ex: 200 ocorrências da letra A em várias posições). Logo, cada caractere deve possuir uma referência para um objeto Flyweight, que deverá ser compartilhado por todas as instâncias do mesmo caractere do documento, exceto a posição que será variável.
Dessa forma, em vez de armazenarem 800 objetos com três atributos, armazenam-se 800 objetos com um atributo e ponteiro para o objeto Flyweight.

Proxy

Esse padrão provê um substituto ou ponto através do qual um objeto pode controlar o acesso a outro objeto.
Esse padrão de projeto deve ser utilizado quando houver uma necessidade de uma referência mais versátil ou sofisticada para um objeto do que um simples ponteiro. Por exemplo, proxies virtuais criam objetos caros por demanda e proxies de proteção controlam o acesso ao objeto original. Considerem a hipótese de um sistema que acesse um banco de dados por meio de uma classe de conexão.
No entanto, por medidas de segurança, vamos supor que se deseja que esse sistema não tenha acesso direto ao banco de dados referido. Dessa forma, o usuário se conectará ao Proxy (isto é, a classe substituta ou suplente) e o Proxy que irá se conectar ao banco de dados. Claro, tudo isso ocorrendo de maneira transparente para o usuário.

