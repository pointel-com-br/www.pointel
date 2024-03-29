# Engenharia de Software e Sistemas - Padrões de Projeto - Criacionais

Índice

1 Abstract Factory

2 Builder

3 Factory Method

4 Prototype

5 Singleton

Abstract Factory

Esse padrão fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
Esse padrão de projeto deve ser utilizado quando o sistema for configurado como uma família de produtos, que - uma vez relacionados - são projetados para serem utilizados em conjunto. O Abstract Factory busca assegurar essa restrição, revelando apenas suas interfaces e, não, suas implementações. Considerem a hipótese de se visualizar a globo.com de um desktop ou de um smartphone. Evidentemente, são duas interfaces gráficas diferentes (Clássica e Mobile).
Apesar de serem distintas, existem muitas similaridades. Logo, é útil aproveitar todo código em comum e implementar com as classes concretas apenas as diferenças. Assim, o usuário interage apenas com a interface provida pelo padrão Abstract Factory. Em tempo de execução, ela descobre, a partir de algum parâmetro fornecido, se o acesso parte de um smartphone ou desktop e instancia apenas a classe concreta específica que renderizará a interface gráfica pretendida.
Galera, todos os padrões do tipo Factory encapsulam a criação de objetos. O padrão Factory Method, por exemplo, deixa as subclasses decidirem quais objetos criar.

Builder

Esse padrão separa a construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes tipos de representações.
Esse padrão de projeto deve ser utilizado quando o algoritmo para criação de um objeto complexo for independente das partes que compõem o objeto e independente de como ele é montado. Ademais, o processo de construção deve permitir diferentes representações para o objeto que será construído. Esse padrão é bastante parecido com o Abstract Factory. A diferença é que não se constrói uma família de objetos de uma única vez, mas partes do objeto passo-a-passo!
No exemplo anterior, havia duas famílias de objetos compostas de várias partes (botões, barra de rolagem, caixas de seleção, ícones, etc), que compunham a interface de um website em um smartphone ou desktop. Ao se descobrir de que dispositivo se tratava, instanciava-se a interface completa do smartphone ou desktop. Agora suponham que um tablete seja capaz de reunir simultaneamente elementos de ambas as interfaces gráficas.
O Builder é capaz de coordenar a construção da interface gráfica do tablete ao instanciar partes dessas interfaces. Logo, ele pode criar diferentes representações de suas interfaces gráficas ao instanciar, por exemplo, um botão da interface do smartphone, a barra de rolagem da interface do desktop, caixas de seleção da interface do smartphone e ícones da interface do desktop. Ele possui uma classe que coordena a construção desses objetos até a criação da representação final.

Factory Method

Esse padrão define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.
Esse padrão de projeto deve ser utilizado quando uma classe não puder antecipar qual objeto ela deve criar. Deve ser usado, também, quando uma classe quer que suas subclasses especifiquem os objetos que ela criar. Por fim, deve ser usado para delegar responsabilidades a diversas outras subclasses. Considerem a hipótese de se visualizar as características de um carro de uma concessionária.
No entanto, sabe-se que em uma concessionária há diversos modelos de carro. Então, pode-se criar uma classe abstrata base para representar todos os carros e especializá-la em subclasses que representem cada tipo de carro (Corsa, Celta, Cruze, Camaro, etc). No entanto, o problema surge quando se quer criar um objeto, uma vez que - de alguma forma - precisa-se identificar qual objeto se deseja criar.
O Factory Method cria objetos concretos que implementam a classe base e especializam cada objeto, sendo definidos, pelo usuário, em tempo de execução, qual carro deverá ser instanciado. É bom destacar que ele - conforme especificado - contém diversos elementos, tais como: Creator, ConcreteCreator, Product e ConcreteProduct.

Prototype

Esse padrão especifica os tipos de objetos para criar usando uma instância como protótipo e cria novos objetos copiando este protótipo.
Esse padrão de projeto deve ser utilizado quando um sistema possuir componentes cujo estado inicial tenha poucas variações. É oportuno disponibilizar um conjunto pré-estabelecido de protótipos que dão origem aos objetos que compõem o sistema. Dessa forma, basta modificar os atributos que forem diferentes e adaptar o objeto para o uso pretendido. Considerem a hipótese de se preencher os dados de todas as pessoas de uma família.
Considerem também que cada objeto Pessoa contenha centenas de atributos, tais como: Nome, Idade, Endereço, Telefone Residencial, Nacionalidade, Classe Social, etc. Vamos supor que sejam preenchidos todos os atributos do objeto Pessoa referente ao pai, mas ainda falta preencher os dados da mãe e filhos. Logo, sabe-se que atributos como Endereço, Telefone Residencial, Nacionalidade, etc provavelmente serão idênticos para todos os membros da família.
Logo, ao invés de se criar objeto para cada membro e preenchê-los um a um integralmente, pode- se clonar o objeto pai já preenchido e modificar apenas os atributos diferentes, como Nome, Idade, etc. Entre outros benefícios, temos: acrescenta e remove produtos em tempo de execução; reduz o número de subclasses; configura dinamicamente uma aplicação com classes; especifica novos objetos pela variação de valores; e especifica novos objetos pela variação da estrutura. Bacana?

Singleton

Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
Esse padrão de projeto deve ser utilizado quando houver a necessidade de existir exatamente uma instância de uma classe e ela deverá ser acessível aos clientes a partir de um ponto de acesso conhecido. Vamos considerar a hipótese de um sistema que trabalhe com diversas conexões com o banco de dados em uma mesma execução. Imaginem a perda de desempenho ao se instanciar a classe de conexão com o banco de dados várias vezes.
O Padrão Singleton garante que só haverá uma instância de conexão com o banco de dados e, assim, assegura que - durante a execução - a classe será instanciada apenas uma única vez.

