# Engenharia de Software e Sistemas - Arquitetura. Padrões de projeto. Padrões GRASP. SOLID

Índice

1) Padrões de Projeto

2) Padrões de Projeto - Padrões Criacionais.

3) Padrões de Projeto - Padrões Estruturais.

4) Padrões de Projeto - Padrões Comportamentais.

5) Resumo - Padrões de Projeto

6) Questões Comentadas - Padrões de Projeto - CESPE

7) Questões Comentadas - Padrões de Projeto - FCC

8) Questões Comentadas - Padrões de Projeto - FGV

9) Questões Comentadas - Padrões de Projeto - Diversas.

10) Lista de Questões - Padrões de Projeto - CESPE

11) Lista de Questões - Padrões de Projeto - FCC

12) Lista de Questões - Padrões de Projeto - FGV

13) Lista de Questões - Padrões de Projeto - Diversas.

14) Padrões de Projeto - GRASP - Teoria

15) Padrões de Projeto - GRASP - Questões Comentadas - CEBRASPE

16) Padrões de Projeto - GRASP - Lista de Questões- CEBRASPE

17) Princípios SOLID - Teoria

18) Princípios SOLID - Questões Comentadas.

19) Princípios SOLID - Lista de Questões.

PADRõES DE PRoJETo - GANG oF FoUR (GOF)

Conceitos Básicos

INCIDÊNCIA EM PROVA: BAIXA

Pessoal, vamos iniciar pelo básico! O que é um Padrão? É um modelo testado ou documentado para se alcançar um determinado objetivo. O autor Christopher Alexander afirma que cada padrão descreve um problema que ocorre repetidas vezes em nosso ambiente e o núcleo de sua solução, de tal forma que ela pode ser usada diversas vezes sem que seja realizada da mesma maneira. E o que seriam Padrões de Projeto (do inglês, Design Patterns)?
Respondo: são descrições de objetos que se comunicam e classes que são customizadas para resolver um problema genérico em um contexto específico. Esses padrões nomeiam, abstraem e identificam aspectos comuns em uma estrutura e os torna úteis para que sejam realizados. Como é isso, professor? Suponham que haja uma fábrica de software que desenvolve diversos sistemas para as mais variadas áreas de negócio.
Sabe-se que, mesmo em áreas aparentemente distintas ou contrastantes, grande parte dos problemas já possuem uma solução conhecida, formalmente documentada e exaustivamente testada, uma vez que se tratam de problemas recorrentes. Portanto, não há necessidade de se resolver o problema do início se já existe uma solução adequada. Assim sendo, os padrões de projeto são modelos para solucionar problemas gerais de projeto em um contexto particular.
Poxa, professor... o engenheiro de software que inventou isso era genial, né?! Qual é,
pessoal! Mais uma vez, nós "roubamos" isso de outras engenharias. Em meados de 1977, um sujeito chamadoChristopher Alexander (arquiteto, matemático e urbanista austríaco) estudava como melhorar o projeto de edifícios. Ao se cansar de observar repetidos problemas, ele lançou um manifesto com o registro de diversos padrões de projeto recorrentes na engenharia civil.
Esse manifesto continha algumas regras e figuras que descreviam métodos para a construção de projetos práticos, seguros e atrativos em quaisquer escalas, desde regiões inteiras a cidades,vizinhanças, jardins, edifícios, salas, entre outros. Cada padrão foi testado no mundo real, sendo revisado por diversos arquitetos e engenheiros. Alexander fez uma importante declaração a respeito de padrões de projeto de arquitetura:
"Cada padrão descreve um problema que ocorre repetidas vezes em nosso ambiente e,
então,
descreve 0 núcleo da solução para aquele problema, de tal maneira que pode-se usar essa solução milhões de vezes sem nunca fazê-la da mesma forma duas vezes".
Bem, isso chamou a atenção de programadores que estavam de saco cheio de ter que refazer várias partes do código para cada projeto. Foi então que, em 1994, quatro engenheiros de software,conhecidos como The Gang of Four (GoF), resolveram compilar um conjunto de bibliotecas de

SERPRO (Analista - Especialização: Tecnologia) Engenharia de software - 2023
(Pós-Edital)

soluções para problemas comuns de codificação e lançaram um livro clássico com 23
Padrões de Projeto de Software.
Esse livro se tornou um clássico best-seller da literatura orientada a objetos e é recomendado na nossa bibliografia, não obstante ser de leitura extremamente técnica. Concernente aos padrões de projeto, os autores desse livro dizem: "São descrições de objetos que se comunicam e classes que são customizadas para resolver um problema genérico de design em um contexto específico".Professor, que contexto específico é esse? Bem, o contexto é inerente a área de negócio!

Cada um adapta o padrão genérico ao seu ambiente específico para resolver um mesmo problema. Os padrões de projeto abstraem e identificam os aspectos-chave de uma estrutura de projeto comum para torná-la reutilizável. Entre as vantagens dos padrões de projeto, podemos mencionar que é possível aprender com a experiência de outros, identificando problemas comuns de engenharia de software e utilizando soluções testadas e bem documentadas.
É possível utilizar soluções com nomes que facilitam a comunicação,
compreensão e documentação. Eles facilitam o reúso de soluções arquiteturais bem-sucedidas e permitem desenvolver softwares de melhorqualidade. Padrões capturam a estrutura estática e a colaboração dinâmica entre objetos participantes no projeto de sistemas. Eles utilizam conceitos de orientação a objetos para construir código reutilizável, eficiente, de alta coesão e baixo acoplamento.
Então há apenas benefícios em se utilizar padrões de projetos? Claro que não! Muitas vezes, as tentativas de se escrever um código que esteja em conformidade com um determinado padrão de projeto aumentam desnecessariamente a complexidade do código. Em outras palavras, a tentativa de simplificar pode acabar complicando a implementação. Ademais, estudos mostram que grande parte dos padrões podem ser simplificados ou eliminados. Como, professor? utilizando-
Se recursos diretos das próprias linguagens de programação, como em
LISP e DYLAN. Portanto, os Design Patterns podem ser simplesmente um indicativo de que algumas linguagens de programação falham em oferecer determinadas características. Cada padrão de projeto é organizado segundo quatro elementos: Nome, Problema, Solução e
Consequências. Nome simplesmente identifica o padrão; Problema descreve a condição em que ele deve ser aplicado; Solução descreve como resolvê-lo; e Consequência descreve os impactos.
Por fim, algumas observações importantes! Esses 23 Design Patterns somente podem ser utilizados em projetos de tecnologia da informação? Claro, eles são padrões de projeto de software. Esses 23Design Patterns somente podem ser utilizados em projetos orientados a objetos?
Sim, também.
Pessoal, Padrões GOF somente com Orientação a Objetos! Padrões de Projeto, em geral,
podem usarqualquerparadigma ou linguagem!
SERPRO (Analista - Especialização: Tecnologia) Engenharia de software - 2023
(Pós-Edital)

Propósito

Criação Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter lemplate Method
Os 23 Padrões de Projeto podem ser classificados quanto aos seus propósitos em três tipos: PadrõesCriacionais, Padrões Estruturais e Padrões Comportamentais. Infelizmente,
vocês têm que decorar como se classificam todos os padrões de projeto. A tabela acima apresenta todos os padrões de acordo com seus respectivos propósitos. Os Padrões Criacionais abstraem o processo de criação de objetos a partir da instanciação de classes.
Já os Padrões Estruturais tratam da forma como classes e objetos estão organizados para formar estruturas maiores. Por fim, Padrões Comportamentais se preocupam com os algoritmos e responsabilidades dos objetos, que ocorrem em tempo de execução. Pessoal... quando eu estudei esse assunto na minha vida de concurseiro, utilizei de um mnemónico maneiríssimo criado peloProf. Rogério Araújo para memorizar:

PAPPO&6 PÊ CfílAÇÃO

A FÁÊRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO. A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO
ÚNICO,
A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO. A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO
ÚNICO.

A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO.
A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO.
A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO.
A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO.

A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO.
A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO.
A FÁSRICA ASSTRATA CONSTRÓI UM PROTÓTIPO ÚNIICO.
A FÁÊRICA ASSTRATA CONSTRÓI UM PROTÓTIPO

PWPOtS Ê6TRUTURAI5

A PONTÊ APAPTAPAÊ COMPOSTA PÊ PÊCORA^ÓÊS NA
FA.C.H..A.P..A..P.A..P..A..O..P..Ê.S.O..M..O.S..C.A...S.Ê..A..P.R..O.X..IM..A<R.

A PONTÊ APAPTAPA Ê COMPOSTA PÊ PÊCORAÓÕÊSNA FACHAPAPARA O PÊSO MOSCA SÊ APROXI o#

A PONTÊ APAPTAPA Ê COMPOSTA PÊ PÊCORAÓÕÊSNA FACHAPAPARA O PÊSO MOSCA SÊ APROX .

A PONTÊ APAPTAPA Ê COMPOSTA PÊ PÊCORAÓÕÊSNA FACHAPAPARA O PÊSO MOSCA SÊ APROXIM^ '

A PONTÊ APAPTAPAÊ COMPOSTA PÊ PÊCORACÕÊS NA FACHAPA PARA O PÊSO MOSCA SÊ APROXIMA 'J

A PONTÊ APAPTAPAÊ COMPOSTA PÊ PÊCORACÕÊS NA FACHAPA PARA O PÊSO MOSCA SÊ APROXIMAR. | |

Explicação: A fábrica (Factory Method') abstrata (Abstract Factory) constrói (Builder) um protótipo(Prototype) único (Singleton). A ponte (Bridge) adaptada (Adapter) é composta
(Composite) de decorações (Decorator) na fachada (Façade) para o peso-mosca (Flyweight) se aproximar(Proxy). E
não tem frase para 0 último? Não, porque não é necessária! Se não é um padrão criacional ou estrutural, é um padrão comportamental.
SERPRO (Analista - Especialização: Tecnologia) Engenharia de software - 2023
(Pós-Edital)

Padrões Criacionais

INCIDÊNCIA EM PROVA: ALTÍSSIMA

Abstract Facto ry

Esse padrão fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
Esse padrão de projeto deve ser utilizado quando o sistema for configurado como uma família de produtos, que - uma vez relacionados - são projetados para serem utilizados em conjunto. OAbstract Factory busca assegurar essa restrição, revelando apenas suas interfaces e,
não, suas implementações. Considerem a hipótese de se visualizar a globo.com de um desktop ou de um smartphone. Evidentemente, são duas interfaces gráficas diferentes (Clássica e Mobile).
Apesar de serem distintas, existem muitas similaridades. Logo, é útil aproveitar todo código em comum e implementar com as classes concretas apenas as diferenças. Assim, o usuário interage apenas com a interface provida pelo padrão Abstract Factory. Em tempo de execução,ela descobre, a partir de algum parâmetro fornecido, se o acesso parte de um smartphone ou desktop e instancia apenas a classe concreta específica que renderizará a interface gráfica pretendida.
Galera, todos os padrões do tipo Factory encapsulam a criação de objetos. O padrão
Factory
Method, por exemplo, deixa as subclasses decidirem quais objetos criar.

Builder

Esse padrão separa a construção de um objeto complexo da sua representação, deforma que o mesmo processo de construção possa criar diferentes tipos de representações.
Esse padrão de projeto deve ser utilizado quando o algoritmo para criação de um objeto complexo for independente das partes que compõem o objeto e independente de como ele é montado.Ademais, o processo de construção deve permitir diferentes representações para o objeto que será construído. Esse padrão é bastante parecido com o Abstract Factory. A diferença é que não se constrói uma família de objetos de uma única vez, mas partes do objeto passo-a-passo!
No exemplo anterior, havia duas famílias de objetos compostas de várias partes (botões,
barra de rolagem, caixas de seleção, ícones, etc), que compunham a interface de um website em um smartphone ou desktop. Ao se descobrir de que dispositivo se tratava, instanciava-se a interface completa do smartphone ou desktop. Agora suponham que um tablete seja capaz de reunir simultaneamente elementos de ambas as interfaces gráficas.
O Builder é capaz de coordenar a construção da interface gráfica do tablete ao instanciar partes dessas interfaces. Logo, ele pode criar diferentes representações de suas interfaces gráficas ao instanciar, por exemplo, um botão da interface do smartphone, a barra de rolagem da interface do desktop, caixas de seleção da interface do smartphone e ícones da interface do desktop. Ele possui uma classe que coordena a construção desses objetos até a criação da representação final.
Factory Method

Esse padrão define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.
Esse padrão de projeto deve ser utilizado quando uma classe não puder antecipar qual objeto ela deve criar. Deve ser usado, também, quando uma classe quer que suas subclasses especifiquem os objetos que ela criar. Por fim, deve ser usado para delegar responsabilidades a diversas outras subclasses. Considerem a hipótese de se visualizar as características de um carro de uma concessionária.
No entanto, sabe-se que em uma concessionária há diversos modelos de carro. Então,
pode-se criar uma classe abstrata base para representar todos os carros e especializá-la em subclasses que representem cada tipo de carro (Corsa, Celta, Cruze, Camaro, etc). No entanto, o problema surge quando se quer criar um objeto, uma vez que - de alguma forma - precisa-se identificar qual objeto se deseja criar.
O Factory Method cria objetos concretos que implementam a classe base e especializam cada objeto, sendo definidos, pelo usuário, em tempo de execução, qual carro deverá ser instanciado. É bom destacar que ele - conforme especificado - contém diversos elementos, tais como: Creator, ConcreteCreator, Product e ConcreteProduct.
Prototype

Esse padrão especifica os tipos de objetos para criar usando uma instância como protótipo e cria novos objetos copiando este protótipo.
Esse padrão de projeto deve ser utilizado quando um sistema possuir componentes cujo estado inicial tenha poucas variações. É oportuno disponibilizar um conjunto pré-estabelecido de protótipos que dão origem aos objetos que compõem o sistema. Dessa forma, basta modificar os atributos que forem diferentes e adaptar o objeto para o uso pretendido. Considerem a hipótese de se preencher os dados de todas as pessoas de uma família.
Considerem também que cada objeto Pessoa contenha centenas de atributos, tais como:
Nome,
Idade, Endereço, Telefone Residencial, Nacionalidade, Classe Social, etc. Vamos supor que sejam preenchidos todos os atributos do objeto Pessoa referente ao pai, mas ainda falta preencher os dados da mãe e filhos. Logo, sabe-se que atributos como Endereço, TelefoneResidencial,
Nacionalidade, etc provavelmente serão idênticos para todos os membros da família.

Logo, ao invés de se criar objeto para cada membro e preenchê-los um a um integralmente, pode-se clonar o objeto pai já preenchido e modificar apenas os atributos diferentes, como
Nome, Idade,
etc. Entre outros benefícios, temos: acrescenta e remove produtos em tempo de execução;
reduz o número de subclasses; configura dinamicamente uma aplicação com classes; especifica novos objetos pela variação de valores; e especifica novos objetos pela variação da estrutura. Bacana?
Singleton

Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
Esse padrão de projeto deve ser utilizado quando houver a necessidade de existir exatamente uma instância de uma classe e ela deverá ser acessível aos clientes a partir de um ponto de acesso conhecido. Vamos considerar a hipótese de um sistema que trabalhe com diversas conexões com o banco de dados em uma mesma execução. Imaginem a perda de desempenho ao se instanciar a classe de conexão com o banco de dados várias vezes.
O Padrão Singleton garante que só haverá uma instância de conexão com o banco de dados e,assim, assegura que-durante a execução-a classe será instanciada apenas uma única vez.

Padrões Estruturais

INCIDÊNCIA EM PROVA: ALTÍSSIMA

Adapter

Esse padrão converte a interface de uma classe em outra interface que normalmente não poderiam trabalhar juntas por serem incompatíveis.
Esse padrão de projeto deve ser utilizado quando se quer usar uma classe e sua interface não é compatível com aquela de que você necessita. Deve ser usado, também, quando se quer criar classes reusáveis que cooperem com classes que não têm necessariamente interfaces compatíveis.Essa classe funciona como um adaptador de tomada. Frequentemente, quer se utilizar uma tomada de três pinos, porém a tomada disponível só permite dois pinos.
Usa-se, então, um adaptador que converte a interface de uma das tomadas permitindo que se faça a conexão normalmente. Ela permite que um objeto cliente utilize serviços de outros objetos com interfaces diferentes. Considerem a hipótese de um objeto que contenha dados de um formulário de Vistos de Imigração do sistema da polícia federal, como Data deNascimento (no formato DD:MM:AAAA).
Porém, esse objeto deve se comunicar com outro objeto do sistema da embaixada americana, que adota o formato MM:DD:AAAA. Nesse caso, um Adapter seria extremamente oportuno!
Bridge

Esse padrão desacopla uma interface de sua implementação, deforma que ambas possam variar independentemente.
Esse padrão de projeto deve ser utilizado quando se deseja evitar um vínculo permanente entre uma abstração e sua implementação. Ele é recomendado também quando se quer evitar que mudanças na implementação de uma abstração causem impacto nos clientes, isto é, seu código não deve ter que ser recompilado. O Bridge fornece um nível de abstração maior que o Adapter, na medida em que permite variações independentes da interface e da implementação.
Ele provê alto nível de desacoplamento de componentes, fazendo uma ponte entre as hierarquias de classes relacionadas. Esse padrão de projeto é um pouco complicado de se entender,portanto prestem atenção! Considerem a hipótese de um conjunto de janelas gráficas que funcionem em diversas plataformas (Windows, Linux, Mac, etc). Professor, por que não usar oAdapter? De fato, ele poderia adaptar interfaces para cada uma das plataformas.

No entanto, há dezenas de tipos de janelas gráficas (Diálogo, Aviso, Erro, etc),
tornando a utilização inviável para grandes quantidades. Uma ideia melhor seria criar uma interface para plataformas e outra para janelas. A primeira conteria os elementos comuns das plataformas e teria classes concretas específicas para implementarjanelas em Linux, Mac, etc; e a segunda conteria elementos comuns das janelas e teria classes concretas específicas para implementarjanelas Aviso, Erro, etc.
Logo, ao chamar um método da classe concreta da interface de janelas, ela realizará chamadas aos métodos concretos da interface de plataformas. Assim, caso se queira adicionar mais tipos de janelas ou mais plataformas, não haverá impacto no cliente, não haverá recompilação de código nem vínculo entre interfaces de um e implementações de outros. O desacoplamento permite que se modifique o código da interface sem alterar a implementação das janelas e vice-versa.
Notem que, assim, pode-se combinar as interfaces e implementações de quaisquer maneiras possíveis - essa é vantagem do padrão Bridge. Esse padrão nos lembra do padrão bridge.
Composite

Esse padrão compõe objetos em estruturas de árvore para representar hierarquias parte-todo,permitindo aos clientes tratarem objetos individuais e composições de objetos uniformemente.

Esse padrão de projeto deve ser utilizado quando se deseja representar hierarquias parte-todo de objetos e quando se deseja que os clientes ignorem a diferença entre composições de objetos e objetos individuais. Assim, eles tratarão todos os objetos em uma estrutura composta uniformemente. Considerem a hipótese de uma interface gráfica composta de vários objetos. Em muitos casos, esses objetos são compostos de outros objetos. Exemplo de implementação:
Por meio de uma árvore de forma transparente para o cliente - ele não precisa saber de nada disso.Assim, ele não deve diferenciar objetos individuais (folhas) de objetos compostos (nós).

Decorator

Esse padrão anexa responsabilidades adicionais a um objeto dinamicamente. Fornece uma alternativa flexível em relação à herança para estender funcionalidades.
Esse padrão de projeto deve ser utilizado quando se quer adicionar responsabilidades a objetos individuais dinâmica e transparentemente, isto é, sem afetar outros objetos. Também é utilizado quando extensões por subclasses forem impraticáveis, tendo em vista o possível número de extensões independentes. Considerem a hipótese de um Subway! Usando-se herança, cria-se uma classe abstrata sanduíche e várias classes concretas para implementá-la.
No entanto, há sanduíches com almôndega, sem queijo, com tomate, sem cebola,
etc. É
customizável, portanto é completamente inviável construir classes concretas para cada tipo de sanduíche, devido a gigantesca quantidade de combinações. O Padrão Decorator sugere que o objeto sanduíche anexe diversas responsabilidades dinamicamente. Dessa forma, em tempo de execução, à medida que se adicione um novo ingrediente, cria-se mais uma responsabilidade.
Ao contrário da herança, que aplica funcionalidades a todos os seus objetos, o
Decorator aplica funcionalidades apenas a um objeto específico.
Façade

Esse padrão oferece uma interface unificada para um conjunto de interfaces em um subsistema,
definindo uma interface de alto nível que facilita a utilização do subsistema.

O Padrão de Projeto Façade (também é um dos mais importantes) deve ser utilizado quando se desejarfornecer uma interface simples para um subsistema complexo ou também quando se deseja dividirem camadas os subsistemas. É também utilizando quando existem diversas dependências entre clientes e as classes de implementação de uma abstração. Considerem a hipótese de um banco com um sistema legado de informações de crédito muito complexo.
Esse sistema deve interagir com um sistema de banco de dados recém implementado e moderno.Para que ele acesse o sistema legado, pode-se utilizar o padrão Façade, uma vez que ele facilita a utilização por meio de uma interface de alto nível e, dessa forma, não há necessidade de se interagir diretamente com o sistema complexo.
Flyweight

Esse padrão utiliza compartilhamento para suportar eficientemente grandes quantidades de objetos de baixa granularidade.
Esse padrão de projeto deve ser utilizado quando uma aplicação usa grande número de objetos e os custos de armazenamento forem altos. Deve ser utilizado, também, quando muitos grupos de objetos puderem ser substituídos por relativamente poucos objetos compartilhados, uma vez que os estados extrínsicos forem removidos. Considerem a hipótese de um texto escrito noMicrosoft Word, em que cada caractere seja um objeto que contenha posição, formato e tamanho,
isso poderia ocupar toda memória disponível no sistema, mas percebam que vários caracteres se repetem diversas vezes (Ex: letra A) e eles são exatamente iguais, muda-se somente a posição (ex:
200 ocorrências da letra A em várias posições). Logo, cada caractere deve possuir uma referência para um objeto Flyweight, que deverá ser compartilhado por todas as instâncias do mesmo caractere do documento, exceto a posição que será variável.
Dessa forma, em vez de armazenarem 800 objetos com três atributos, armazenam-se 800
objetos com um atributo e ponteiro para o objeto Flyweight.
Proxy

Esse padrão provê um substituto ou ponto através do qual um objeto pode controlar o acesso a outro objeto.
Esse padrão de projeto deve ser utilizado quando houver uma necessidade de uma referência mais versátil ou sofisticada para um objeto do que um simples ponteiro. Por exemplo,proxies virtuais criam objetos caros por demanda e proxies de proteção controlam o acesso ao objeto original.Considerem a hipótese de um sistema que acesse um banco de dados por meio de uma classe de conexão.
No entanto, por medidas de segurança, vamos supor que se deseja que esse sistema não tenha acesso direto ao banco de dados referido. Dessa forma, o usuário se conectará aoProxy (isto é, a classe substituta ou suplente) e o Proxy que irá se conectar ao banco de dados.Claro, tudo isso ocorrendo de maneira transparente para o usuário.
SERPRO (Analista - Especialização: Tecnologia) Engenharia de software - 2023
(Pós-Edital)

Padrões Comportamentais

INCIDÊNCIA EM PROVA: MÉDIA

Chain of Responsability

Esse padrão evita o acoplamento do remetente de uma requisição ao seu receptor ao dar a mais de um objeto a chance de lidar com a requisição.
Esse padrão de projeto deve ser utilizado quando se deseja emitir uma solicitação para um dentre vários objetos, sem especificar explicitamente o receptor ou quando mais de um objeto é capaz de lidar com a requisição e ele não for conhecido a priori. Esse padrão também é comumente utilizado quando um conjunto de objetos que podem lidar com uma requisição forem especificados dinamicamente.
Esse padrão acaba com estruturas de decisão ao criar uma cadeia de objetos em que se passa a responsabilidade até encontraraquele que pode respondê-la. Consideremos a hipótese de uma loja virtual que permite pagamento online por meio de diversos bancos. Dado um parâmetro,deve-se identificar qual banco deve ser utilizado para o pagamento. Esse problema pode ser resolvido com outros padrões, mas o Chain of Responsability fornece uma solução com fraco acoplamento.
Assim, cada elemento da cadeia pode implementar a requisição da maneira que quiserem.
Assim,
não há uma associação direta entre o remetente e o receptor que irá lidar com a requisição.

Command

Esse padrão encapsula a requisição de um objeto, portanto permitindo que se parametrize os clientes com diferentes requisições.
Esse padrão de projeto deve ser utilizado quando se deseja parametrizar objetos para realizar alguma execução ou também para especificar, enfileirar e executar requisições a qualquer momento. Ele também é utilizado para suportar mudanças de log de maneira que possa ser reaplicado no caso de uma queda no sistema. Entenderam? Considerem a hipótese de um interruptor que ligue ou desligue uma lâmpada.
Esse interruptor encapsula uma requisição, de tal modo que se possa utilizá-lo para diferentes dispositivos. Em outras palavras, se eu retirar um interruptor de uma lâmpada, conectar adequadamente aos fios de um computador, é possível ligar/desligar o computador com o mesmo interruptor. Logo, o interruptortem sua interface encapsulada, logo pode ser utilizado em qualquer dispositivo que tenha uma interface Ligar/Desligar.
Imaginem agora uma classe que faz diversas conexões a um banco de dados.
Não é recomendável que ela tenha um método que se conecte diretamente ao banco, portanto encapsula-se essa conexão, diminuindo a dependência.
Interpreter

Esse padrão, dada uma linguagem, define uma representação para sua gramática em conjunto com um interpretador que utiliza a representação para interpretar sentenças na linguagem.
Esse padrão de projeto deve ser utilizado quando houver uma linguagem para interpretar e quando se puder representar declarações nessa linguagem como árvores sintáticas abstratas. Ele funciona bem quando a gramática é simples, permitindo um fácil gerenciamento e quando a eficiência não é um fator crítico de sucesso. Basta lembrar do Java, que é uma linguagem interpretada.
O que isso quer dizer esse negócio de interpretada, professor? Bem, isso significa que o código fonte é compilado em um bytecode, que é então posteriormente interpretado por um interpretador.Dessa forma, esse padrão de projeto é utilizado nos casos em que é possível definir uma linguagem com uma gramática que possa ser, posteriormente, interpretada.
Iterator

Esse padrão fornece uma maneira de acessar elementos de um objeto agregado sequencialmente sem expor sua representação interna.
Esse padrão de projeto deve ser utilizado quando se deseja acessar o conteúdo de um objeto agregado sem expor a sua representação interna e para fornecer uma interface uniforme para diferentes estruturas de agregação. Ele também é recomendado para suportar múltiplos acessos a objetos agregados. Entendido? Vamos ver um exemplo!
Considerem a hipótese de se desejar percorrer sequencialmente quatro coleções distintas
(Lista,
Arrays, Map e Set) de objetos bastante complexos. Em uma situação normal, deve-se conhecer a representação interna de cada uma dessas coleções. O Iterator permite que se percorra todas essas coleções sem precisar saber detalhes de seu funcionamento.
Mediator

Esse padrão define um objeto que encapsula a forma como um conjunto de objetos interagem,promovendo um fraco acoplamento ao evitar que objetos se refiram aos outros explicitamente.

Esse padrão de projeto deve ser utilizado quando um conjunto de objetos se comunicar de maneira bem definida, porém complexa e quando o reúso de um objeto for difícil por referenciar e se comunicar com muitos outros objetos. Ademais, ele é utilizado quando um comportamento distribuído entre diversas classes puder ser customizado sem a criação de muitas subclasses.
Considerem a hipótese de um software complexo com grandes quantidades de classes, de tal modo que a lógica de processamento está distribuída entre elas. Todo mundo sabe que,há cada manutenção ou refatoração, o desenho do software pode se tomar mais complexo e a comunicação entre as classes pode ser mais difícil de ler entender.
Logo, o Padrão Mediator permite que a comunicação entre objetos seja encapsulada em um outro objeto mediador. Assim, não haverá mais uma comunicação direta entre as classes,reduzindo o acoplamento, garantindo que todos fiquem mais livres para serem modificados e diminuindo a complexidade de comunicação entre objetos.
Memento

Esse padrão captura e externaliza o estado interno de um objeto, sem violar seu encapsulamento,
de maneira que o objeto possa ser restaurado posteriormente.

Esse padrão de projeto deve ser utilizado quando uma parte do estado de um objeto precisar ser armazenada, de forma que possa ser recuperada posteriormente. Ele é utilizado,também,
para evitar que uma interface direta para obter um estado exponha detalhes de implementação e quebrem o encapsulamento do objeto. Considerem a hipótese de um editor de texto que guarde o estado interno do objeto.
Em outras palavras, o que o usuário está digitando, aí ele deleta uma palavra, mas se arrepende e deseja voltar ao estado anterior. Bem, o memento oferece uma maneira de desfazer ações sem ter acesso ao que estava sendo escrito, ele apenas retorna o estado anterior, mas sem olhar o que estava escrito. Logo, o Padrão Memento permite a captura e externalização do estado interno de um objeto, sem violar seu encapsulamento.
Ele captura o que estava escrito e mostra ao usuário, mas sem acesso direto ao que estava escrito.
Assim, pode-se cancelar operações e desfazer alterações para retornar ao estado anterior.

Observer

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.
Esse padrão de projeto deve ser utilizado quando uma mudança em um objeto requisitar mudanças em outros objetos e não se souber quantos objetos necessitam ser modificados. Ele também é utilizado quando uma abstração possuir dois aspectos, sendo um dependente do outro. Além disso, sua utilização é recomendada quando um objeto for capaz de notificar outros sem assumir quem são. Certinho?
Considerem a hipótese de uma tabela de classificação do campeonato brasileiro com um gráfico de pizza informando vitórias, empates e derrotas de um determinado time, assim como um gráfico com a variação de posição do time do campeonato. Aí chega o domingão, ocorrem 10jogos e o estagiário altera a tabela com os novos dados. E agora? Tem que atualizar os gráficos um a um? Os gráficos ficarão desatualizados? Não haverá nem uma notificação de novos dados?
Ele cria uma dependência dos gráficos em relação à tabela de modo que, quando a tabela muda de estado, os gráficos são atualizados automaticamente.
State

Esse padrão permite a um objeto alterar o seu comportamento quando o seu estado interno for modificado.
Esse padrão de projeto deve ser utilizado quando o comportamento de um objeto depender de seu estado e ele deve mudar este comportamento em tempo de execução de acordo com este estado.Ademais, é recomendado quando operações tiverem declarações condicionais grandes que dependam do estado do objeto. Considerem a hipótese do jogo Super Mario Bros'.Lembram-se de quando ele conseguia uma flor de fogo?
Se ele estivesse pequeno, ele ficava grande e pegando fogo! Se ele estivesse grande, ele ficava pegando fogo! Se já estivesse pegando fogo, ganhava 1000 pontos! Se tivesse com uma capa de voo, perdia a capa e ficava pegando fogo! Logo, notem que o estado futuro depende de seu estado atual e o estado futuro é decidido em tempo de execução, isto é, durante o jogo.Esse padrão elimina a necessidade de condicionais complexos. Porque?
Porque pode haver dezenas ou centenas de estados possíveis. A grande vantagem é que esta solução torna mais simples adicionar estados e suas transições.
Strategy

Esse padrão define uma família de algoritmos, encapsula cada um efaz deles intercambiáveis.

Esse padrão de projeto deve ser utilizado quando várias classes relacionadas diferirem apenas em seus comportamentos e que houver necessidade de diferentes variantes de um algoritmo. Ele também é utilizado quando uma classe definir muitos comportamentos e eles aparecerem como declarações condicionais em suas operações. Considerem a hipótese de uma escola querer organizar os meninos e as meninas por ordem de idade.
Há uma família de algoritmos capaz de realizar essa operação (BubbleSort,
QuickSort,
Heapsort, etc). Uma maneira de realizar essa operação é por meio de operadores condicionais (if-else), mas isso pode sertrabalhoso em grandes quantidades. Uma boa estratégia seria encapsular os algoritmos de ordenação, de modo que se possa trocar de algoritmo sempre que quiser. Basta chamar o método OrdenaAluno com os parâmetros sexoAluno e algoritmoOrdenacao.
Assim, é possível chamar o método ordenaAluno(menino, bubbleSort) ou ordenaAluno(menina,mergeSort), etc, diminuindo o acoplamento.

Template Method

Esse padrão define o esqueleto de um algoritmo dentro de uma operação, deixando alguns passos a serem preenchidos pelas subclasses.
Esse padrão de projeto deve ser utilizado quando se deseja implementar a parte invariante de um algoritmo e deixar que as subclasses implementem o comportamento variável. Ele também é recomendado quando comportamentos comuns entre subclasses forem fatorados e localizados em uma classe comum, para evitar duplicação de código. Considerem a hipótese de uma franquia de McDonald's fabricando um sanduíche.
Bem, o cliente pode pedir para colocar mais queijo, tirar os picles, adicionar ketchup, não colocar sal, entre outras opções. No entanto, observem que operações como:abrir o pão,
posicionar o hambúrguer no meio e fechar o pão são operações que sempre irão ocorrer.
Logo, esse esqueleto de algoritmo jamais irá mudar. Já as opções de condimentos, verduras, etc podem ser modificadas de acordo com o gosto do cliente.
Sendo assim, a parte invariável será implementada na classe abstrata e a parte variável será implementada pelas classes filhas de acordo com as necessidades do usuário.
Visitor

Esse padrão representa uma operação a ser realizada sobre elementos de uma estrutura de objetos e permite definir uma operação sem mudar as classes dos elementos sobre os quais opera.
Esse padrão deve ser utilizado quando muitas operações distintas e não relacionadas precisarem ser executadas sobre uma estrutura de objetos e se quer evitar a poluição das classes com essas operações. Ademais, são recomendadas quando as classes que definem a estrutura do objeto raramente forem modificadas. Considerem a hipótese de uma compra em um supermercado. Ocarrinho de compras é a estrutura de dados que contém um conjunto de elementos.

Ao finalizar a compra, deve-se passar a responsabilidade para o caixa
(Visitor). A partir deste momento, ele estará no comando, porque ele que realizará a soma dos preços, pesará as frutas,verduras, vegetais, etc (entre outras operações). Logo, algumas operações se aplicam a alguns elementos, mas não se aplicam a outros, isto é, uma cerveja já possui um valor, mas uma maça precisa ser pesada. No entanto, ambas fazem parte da mesma estrutura de dados.
Galera, vou ser bem sincero com vocês: esse assunto é muuuuuuuuuuuuito chato - e também é muito decoreba! Então, vou explicar o que eu recomendo para o estudo dessa aula —fiz uma análise estatístico rápida e cheguei a algumas conclusões! Primeiro de tudo, decore as frases porque cerca de 15% das questões de prova exigem apenas saber qual Padrão de ProjetoGOF
pertence a qual categoria.

Vocês matam 15% das questões apenas decorando aquelas duas frases, certinho? Segundo,
se você estiver sem tempo, ignore a categoria comportamental, visto a distribuição de questões segue a tabela mostrada acima - e ela é a que tem mais padrões. Por fim, dos 23 Padrões deProjeto, seis correspondem à 55% das questões de prova (dos 85% restantes, isto é, sem as questões de categorias). São eles, em ordem:
Pessoal, se vocês estiverem com o tempo muito apertado, estudem apenas esses acima! Do mesmo modo, podemos afirmar que, dos 23 Padrões deProjeto, onze correspondem à 15% das questões de prova: Decorator, Flyweight, Proxy, Chain ofResponsability, Interpreter, Mediator, Memento,
State, Strategy e Template Method. Os seis padrões restantes, estão no meio termo e correspondem a 30%das questões de prova.

| FALOU EM...
| ...PROVAVELMENTE SERÁ:

Criarfamílias de objetos relacionados...
ABSTRACTFACTORY

Construção de um objeto complexo com diferentes representações...
BUILDER

Deixar subclasses decidirem...
FACTORY METHOD

Criar uma instância prototípica...
PROTOTYPE

Apenas uma instância com um ponto global a ela...
SINGLETON

SERPRO (Analista - Especialização: Tecnologia) Engenharia de software - 2023
(Pós-Edital)

Converte uma interface em outra, por serem incompatíveis...
ADAPTER

Desacoplar interface da implementação...
BRIDGE

Estruturas de árvore em hierarquia parte-todo...
COMPOSITE

Anexa responsabilidades adicionais dinamicamente...
DECORATOR

Interface unificada de alto nível para simplificar outra complexa...
FAÇADE

Compartilhamento para suportar grandes quantidades de objetos...
FLYWEIGHT

Prover substituto para controlar um objeto
PROXY

Evitar o acoplamento dando oportunidade a outros objetos...
CHAIN OF RESPONSABILITY

Encapsula requisição de objetos...
COMMAND

Representação de uma gramática...
INTERPRETER

Interface única para acessar coleções sequencialmente...
ITERATOR

Encapsula a forma como objetos interagem...
MEDIATOR

Captura o estado interno de um objeto...
MEMENTO

Quando objeto mudar de estado, notifica os dependentes...
OBSERVER

Altera comportamentos quando modificar o estado interno...
STATE

Família de algoritmos...
STRATEGY

Esqueleto de algoritmos...
TEMPLATEMETHOD

Operação a ser realizada sobre uma estrutura de objetos...
VISITOR

RESUMo

Propósito

Criação Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Medi ator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

PADRÕES
CRIACIONAIS

BUILDER
ABSTRACTFACTORY

PROTOTYPE
SINGLETON
FACTORYMETHOD

DESCRIÇÃO

Esse padrão separa a construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes tipos de representações.
Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
Esse padrão especifica os tipos de objetos para criar usando uma instância como protótipo e cria novos objetos copiando este protótipo.
Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
Esse padrão define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.
PADRÕES
ESTRUTURAIS

ADAPTER

DESCRIÇÃO

Esse padrão converte a interface de uma classe em outra interface que normalmente não poderiam trabalhar juntas por serem incompatíveis.
BRIDGE

Esse padrão desacopla uma interface de sua implementação, de forma que ambas possam variar independentemente.
COMPOSITE

Esse padrão compõe objetos em estruturas de árvore para representar hierarquias parte-todo,permitindo aos clientes tratarem objetos individuais e composições de objetos uniformemente.
DECORATOR

FACADE

FLYWEIGHT

PROXY

Esse padrão anexa responsabilidades adicionais a um objeto dinamicamente. Fornece uma alternativa flexível em relação à herança para estenderfuncionalidades.
Esse padrão oferece uma interface unificada para um conjunto de interfaces em um subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.
Esse padrão utiliza compartilhamento para suportar eficientemente grandes quantidades de objetos de baixa granularidade.
Esse padrão provê um substituto ou ponto através do qual um objeto pode controlar o acesso a outro objeto.
PADRÕES
COMPORTAMENTAIS

CHAINOF
RESPONSABILITY

COMMAND

DESCRIÇÃO

Esse padrão evita o acoplamento do remetente de uma requisição ao seu receptor ao dar a mais de um objeto a chance de lidar com a requisição.
Esse padrão encapsula a requisição de um objeto, portanto permitindo que se parametrize os clientes com diferentes requisições.
ITERATOR

Esse padrão fornece uma maneira de acessar elementos de um objeto agregado sequencialmente sem expor sua representação interna.
MEDIATOR

MEMENTO

Esse padrão define um objeto que encapsula a forma como um conjunto de objetos interagem, promovendo um fraco acoplamento ao evitar que objetos se refiram aos outros explicitamente.
Esse padrão captura e externaliza o estado interno de um objeto, sem violar seu encapsulamento, de maneira que o objeto possa ser restaurado posteriormente.
OBSERVER

STATE

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.
Esse padrão permite a um objeto alterar o seu comportamento quando o seu estado interno for modificado.
STRATEGY

Esse padrão define uma família de algoritmos, encapsula cada um e faz deles intercambiáveis.

VISITOR

INTERPRETER

Esse padrão representa uma operação a ser realizada sobre elementos de uma estrutura de objetos e permite definir uma operação sem mudar as classes dos elementos sobre os quais opera.
Esse padrão, dada uma linguagem, define uma representação para sua gramática em conjunto com um interpretador que utiliza a representação para interpretar sentenças na linguagem.
TEMPLATEMETHOD

Esse padrão define o esqueleto de um algoritmo dentro de uma operação, deixando alguns passos a serem preenchidos pelas subclasses.
PAPPO&6 PÊ CRIAÇÃO

A FÁ&MCA A&6TRATA CONSTRÓIUM PROTÓTIPO ÚNICO, A
FÁ&RICAASSTRATACONSTRÓIUMPROTÓTIPOÚN
A FÁ&MCA A&STFATA CONSTRÓIUM PROTÓTIPO ÚNICO, A
FÁ&FICAA&STFATACONSTRÓIUMPROTÓTIPOÚN
A FÁ&WCA ASSTRATA CONSTRÓIUM PROTÓTIPO ÚNICO, A FÁ&KCAA&6TFATACONSTRÓIUMPROTÓTIPOÚN
A FÁSRICAASSTRATA CONSTRÓIUM PROTÓTIPO ÚNICO, A
FÁSRICAASSTRATACONSTRÓIUMPROTÓTIPOÚN
A FÁSRICAASSTRATA CONSTRÓIUM PROTÓTIPO ÚNICO, A
FÁSRICAASSTRATACONSTRÓIUMPROTÓTIPOÚN
A FÁSRICAASSTRATA CONSTRÓIUM PROTÓTIPO ÚNICO, A FÁSRICAASSTRATACONSTRÓIUMPROTÓTIPO

PAPRÕÊ5 Ê5TRUTURAI5

A PONTS APAPTAPAS CO^FOSVA PS PSCORAÓÕSS NA FACHAPAPARA O PSSO SMSOASCPRAOXIMAR,
A PONTS APAPTAPAS COMPOSTA PS PSCORAÓÕSS NA FACHAPAPARA O PSSO SMSOASCPRAOXI o#

A PONTS APAPTAPAS COMPOSTA PS PSCORAÓÕSS NA FACHAPAPARA O PSSO 5M5OSACPAROX

A PONTS APAPTAPAS COMPOSTA PS PSCORAÓÕSS NA FACHAPAPARA O PSSO SMÉOASPCPAOXIM^' %-*

A PONTS APAPTAPAÉ COMPOSTA PS PSCORAÓÕSS NA FACHAPAPARA O PSSO 5M6OSACPAPOXIMA 'J

A PONTS APAPTAPAS COMPOSTA PS PSCORAÓÕSS NA FACHAPAPARA O PSSO MOSCA AO

©I PARA MAIS DICAS: WWW.INSTAGRAM.COM/PROFESSORDIEGOCARVALHO

QUESTõES CoMENTADAS - CESPE

í. (CESPE IBANRISUL- 2022) Entre os padrões definidos pelo GRASP, destacam-se baixa coesão e alto acoplamento.
Comentários:

A questão inverteu os conceitos: entre os padrões definidos pelo GRASP, destacam-se a alta coesão e o baixo acoplamento.
Gabarito: Errado

2. (CESPE / BANRISUL - 2022) O objetivo do padrão Singleton é especificar os tipos de objetos a partir de uma instância de protótipo.
Comentários:

Na verdade, o objetivo desse padrão é garantir que exista apenas uma única instância de uma determinada classe. Isso é conseguido assegurando que todas as solicitações para instanciar objetos dessa classe sejam direcionadas para a mesma instância. A questão trata do padrãoPrototype!

Gabarito: Errado

3. (CESPE / BANRISUL - 2022) Por meio do padrão Facade, é possível construir uma interface comum e simplificada para um sistema ou subsistema.
Comentários:

Perfeito! Esse padrão oferece uma maneira simples e direta de acessar os recursos internos de um sistema ou subsistema, provendo uma única interface para o usuário, a qual fornece acesso a todos os recursos necessários. Dessa maneira, o usuário não precisa interagir diretamente com os subsistemas, facilitando e acelerando o processo.
Gabarito: Correto

4. (CESPE / BANRISUL - 2022) O padrão de comportamento Command permite representar comandos como objetos, sem a necessidade de saber como a operação é executada.
Comentários:

Perfeito! Esse padrão permite representar comandos como objetos, sem a necessidade de saber como a operação é executada. Ele é usado para encapsular todos os detalhes de uma operação,
como parâmetros, contexto e estado, em um objeto. Isso permite que os clientes criem,armazenem e reutilizem objetos comandos para executar operações específicas. Dessa forma,
os clientes não precisam saber como a operação é executada, pois isso é encapsulado pelo objeto de comando.
Gabarito: Correto

5. (CESPE / BANRISUL - 2022) O padrão GRASP de Expert é utilizado para atribuir uma responsabilidade à classe que possui a informação necessária para atender essa mesma responsabilidade.
Comentários:

Perfeito! Trata-se de uma técnica de design orientado a objetos que visa melhorar a estrutura e a modularidade do código ao atribuir responsabilidades específicas a classes que possuem conhecimento sobre esse assunto. O objetivo é que a classe especializada possa lidar com as tarefas complexas, permitindo que o código seja mais limpo e desacoplado. Isso ajuda a aumentar a manutenibilidade, simplificar a depuração e melhorar a escalabilidade.
Gabarito: Correto

6. (CESPE / Petrobrás - 2022) Os três principais padrões de projeto (design patterns)
são os criacionais, os estruturais e os comportamentais; os padrões criacionais aumentam a flexibilidade e a reutilização de código porque oferecem diversas alternativas de criação de objetos.
Comentários:

Perfeito! Os Padrões de Projeto podem ser classificados em Padrões Criacionais,
Padrões
Estruturais e Padrões Comportamentais. Ademais, os Padrões Criacionais abstraem o processo de criação de objetos a partir da instanciação de classes, logo aumenta-se a flexibilidade e a reutilização de código, concedendo mais alternativas para se criar objetos.
Gabarito: Correto

7. (CESPE / Petrobrás - 2022) Design patterns é um conjunto de soluções generalistas para problemas recorrentes durante o desenvolvimento de um software; trata-se de um framework ou código pronto, e não de uma definição de alto nível de como um problema comum pode ser solucionado.
Comentários:

Os padrões de projetos são descrições de objetos que se comunicam e classes que são customizadas para resolver um problema genérico em um contexto específico. Desse modo, de fato, os padrões de projeto são um conjunto de soluções generalistas para problemas recorrentes durante o desenvolvimento de um software. Entretanto, eles não são um framework, e - sim - eles são uma definição de alto nível de como um problema comum pode ser solucionado.
Gabarito: Errado

8. (CESPE / TJ-RJ - 2021) A coleção GoF (Gang of Four) é formada por padrões orientados a objetos, separados em categorias. A categoria padrões estruturais é responsável por:
a) estabelecer um design de objetos reutilizáveis.

b) fornecer maneiras eficientes para criar objetos.

c) descrever como os objetos são colocados juntos.

d) descrever como os objetos interagem.

e) distribuir responsabilidades entre os objetos.

Comentários:

Os padrões estruturais no GoF são responsáveis tratam das associações entre as classes e os objetos, ou seja, tratam do relacionamento entre eles. Em suma, busca descrever como os objetos são colocados juntos.
Gabarito: Letra C

4. (CESPE / TCE-PR - 2016) Um projeto fundamentado em padrões emprega um conjunto de soluções comprovadas de maneira conceituai para a construção da aplicação em conformidade com seu escopo.
Comentários:

Na verdade, são soluções comprovadas de maneira factual/prática e, não, conceituai.

Gabarito: Errado

5. (CESPE/TCU-2015) Nos padrões de projeto (design patterns) estruturais,
utilizam-se técnicas que valorizam um forte acoplamento entre as classes para favorecer o aprendizado e a portabilidade das aplicações.
Comentários:

Opa... eles valorizam o fraco/baixo acoplamento.

Gabarito: Errado

6. (CESPE / INPI - 2013) O padrão bridge, além de converter a interface de uma classe existente em outra interface esperada pelos clientes, permite que algumas classes com interfaces diferentes funcionem conjuntamente.
Comentários:

ADAPTER Esse padrão converte a interface de uma classe em outra interface que normalmente poderiam trabalhar juntas por serem incompatíveis.
BRIDGE Esse padrão desacopla uma interface de sua implementação, de forma que ambas variar independentemente.
Converte a interface de uma classe existente em outra interface? Opa, isso é Adapter!

Gabarito: Errado

7. (CESPE / INPI - 2013) Design patterns não se aplicam, exclusivamente, ao Java, podendo ser empregados em projetos que utilizam linguagem C#.
Comentários:

Padrões de Projeto se aplicam a qualquer linguagem de programação e qualquer paradigma.

Gabarito: Correto

8. (CESPE / ANTT- 2013) Em programação orientada a objetos, o padrão de projeto denominadoIterator define uma forma de acesso sequencial aos elementos de um objeto agregado, sem expor sua representação interna.
Comentários:

ITERATOR Esse padrão fornece uma maneira de acessar elementos de um objeto agre sequencialmente sem expor sua representação interna.
Acesso sequencial aos elementos de um objeto agregado? Opa, isso é Iterator!

Gabarito: Correto

9. (CESPE / ANTT - 2013) Em programação orientada a objetos, o padrão de projeto denominadoSingleton define uma classe que possui apenas uma instância e provê um ponto de acesso local a ela.
Comentários:

SINGLETON Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de global a ela.
Classe que possui apenas uma instância? Opa, isso é Singleton! No entanto, ele diz que é um ponto de acesso local'. Opa... não, é um ponto de acesso global!
Gabarito: Errado io.(CESPE / TCE-RO - 2013) Uma das aplicabilidades do padrão Iterator é a representação de hierarquias do tipo todo-parte de objetos, de modo que a aplicação seja capaz de ignorar a diferença entre composições de objetos e objetos individuais, haja vista que todos os objetos tratados no padrão têm comportamento uniforme.
Comentários:

Esse padrão compõe objetos em estruturas de árvore para representar hierarquias parte-todo,

COMPOSITE permitindo aos clientes tratarem objetos individuais e composições de objetos uniformemente.
ITERATOR

Esse padrão fornece uma maneira de acessar elementos de um objeto agregado sequencialmente sem expor sua representação interna.
Representação de hierarquias do tipo todo-parte? Comportamento uniforme? Opa, isso é Composite!

Gabarito: Errado n.(CESPE / TCO-RO - 2013) O padrão Adapter será mais apropriado que o Façade quando for necessário fornecer uma interface unificada para um conjunto de interfaces em um subsistema.
Comentários:

FACADE Esse padrão oferece uma interface unificada para um conjunto de interfaces em subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.
ADAPTER Esse Padrão converte a interface de uma classe em outra interface que normalmente não poderiam trabalhar juntas por serem incompatíveis.
Interface unificada para um conjunto de interfaces em um subsistema? Opa, isso é Façade,
logo ele é mais indicado!
Gabarito: Errado i2.(CESPE / TCE-RO - 2013) O uso do padrão Builder tem a vantagem de permitir acesso controlado à instância de uma classe, uma vez que ele encapsula a classe, criando um ponto global único de acesso.
Comentários:

Esse padrão separa a construção de um objeto complexo da sua representação, de forma que0 mesmo processo de construção possa criar diferentes tipos de representações.

Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
Ponto global único de acesso? Opa, isso é Singleton!

Gabarito: Errado i3.(CESPE / TCE-RO - 2013) Os padrões estruturais, tais como o Bridge e o Proxy,abstraem o processo de instanciação, ajudando a tornar um sistema independente de como os seus objetos são criados. Já os padrões de criação, como Prototype e o Builder, se preocupam com a forma como as classes e os objetos são criados para formar estruturas compostas maiores.
Comentários:

Os Padrões Criacionais abstraem o processo de criação de objetos a partir da instanciação de classes. Já os Padrões Estruturais tratam da forma como classes e objetos estão organizados para formar estruturas maiores. Por fim, Padrões Comportamentais se preocupam com os algoritmos e responsabilidades dos objetos, que ocorrem em tempo de execução.
A questão inverteu os conceitos! Os padrões estruturais tratam da forma como as classes e objetos são organizados (a banca usou o termo "criados", que não é o mais correto) para formar estruturas maiores e os padrões criacionais abstraem o processo de instanciação.
Gabarito: Errado i4.(CESPE/ MPOG-2013) O padrão de comportamento e encadeamento de atendentes(chain of responsibility) evita acoplamento entre solicitantes e atendentes, permitindo que mais de um objeto tenha chance de tratar a solicitação.
Comentários:

CHAIN OF
RESPONSABILITY

Esse padrão evita 0 acoplamento do remetente de uma requisição ao seu receptor ao dar a mais de um objeto a chance de lidar com a requisição.
Evita o acoplamento entre solicitantes e atendentes? É Chain of Responsability!

Gabarito: Correto i5.(CESPE / MPOG - 2013) Para um problema recorrente no desenvolvimento de sistemas,normalmente, um padrão de projeto descreve uma solução geral, que não pode ser reutilizada.

Comentários:

São soluções gerais para problemas recorrentes e, portanto, podem ser reutilizadas.

Gabarito: Errado i6.(CESPE / MPOG - 2013) Padrões de projeto envolvem combinações de classes e algoritmos associados que cumprem com propósitos comuns de projeto.
Comentários:

Perfeito! Eles resolvem problemas comuns ou recorrentes.

Gabarito: Correto i7.(CESPE / MPE-PI - 2012) O padrão de projeto conhecido como façade é indicado para a definição de uma interface de nível mais alto que torne mais fácil a comunicação entre os subsistemas de um sistema complexo.
Comentários:

FAÇADE Esse padrão oferece uma interface unificada para um conjunto de interfaces em subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.
Definição de uma interface de nível mais alto que tome mais fácil a comunicação? Opa, isso é
Façade.

Gabarito: Correto i8.(CESPE / BASA-2012) O padrão mediator define um objeto que encapsula como um conjunto de objetos interage. Esse padrão torna desnecessário que cada objeto armazene referências para todos os objetos com os quais interage e pode ser usado quando objetos se comunicam de forma definida, mas complexa.
Comentários:

Esse padrão define um objeto que encapsula a forma como um conjunto de objetos

MEDIATOR interagem, promovendo um fraco acoplamento ao evitar que objetos se refiram aos outros explicitamente.
Encapsula a forma como um conjunto de objetos interagem? Opa, isso é Mediator! O
restante da descrição também está certo.
Gabarito: Correto ig.(CESPE / BASA - 2012) O padrão adapter define uma família de algoritmos,permite o encapsulamento de algoritmos e possibilita a substituição desses algoritmos. Os algoritmos podem variar independentemente dos seus clientes. Esse padrão pode ser usado quando várias classes relacionadas diferirem apenas nos seus comportamentos.
Comentários:

STRATEGY Esse padrão define uma família de algoritmos, encapsula cada um e faz deles intercambiáveis.
Família de algoritmos? Opa, isso é Strategy!

Gabarito: Errado

2O.(CESPE / MEC - 2011) O padrão Singleton garante que uma classe tenha somente uma instância, fornecendo, assim, um ponto global de acesso a essa instância.
Comentários:

SINGLETON Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de global a ela.
Perfeito! Ele realmente garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
Gabarito: Correto

21. (CESPE / MEC - 2011) O padrão Prototype pode ser usado no desenvolvimento de programas escritos com a linguagem PHP 5.0, atuando como padrão estrutural que permite construirtanto classes quanto objetos.
Comentários:

Propósito

Criação Estrutura Comportamento

Builder
Abstract Factory

Prototype
Singlenton
Factory Method

Adapter
Bridge
Composite
Decorator
Facade
Flyweight
Proxy

Chain of Responsibility
Command

Iterator
Mediator
Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Prototype é um padrão criacional e, não, estrutural.

Gabarito: Errado

22.(CESPE / MEC - 2011) Os padrões de projeto são úteis tanto na fase de planejamento da arquitetura quanto na de desenvolvimento e codificação.
Comentários:

Perfeito! Ele é útil na fase de planejamento (Padrão de Projeto), mas também é útil na fase de codificação.
Gabarito: Correto

23. (CESPE / MEC - 2011) O padrão Abstract Factory é corretamente aplicável, quando necessário,para fornecer uma biblioteca de classes e não revelar suas interfaces.

Comentários:

ABSTRACTFACTORY Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou sem especificar suas classes concretas.
A questão está errada, porque deve-se revelar apenas suas interfaces e, não, suas classes concretas.Não sei se não entraram com recurso ou se a banca não quis trocar o gabarito, mas no gabarito oficial veio como verdadeiro.
Gabarito: Correto

24.(CESPE/TRT-RN-2oIo) OS padrões de projeto podem ser definidos como soluções já testadas para problemas que ocorrem frequentemente durante o projeto de software.
Comentários:

Padrões de Projeto são descrições de objetos que se comunicam e classes que são customizadas para resolver um problema genérico em um contexto específico. Esses padrões nomeiam,abstraem e identificam aspectos comuns em uma estrutura e os torna úteis para que sejam realizados.
Gabarito: Correto

25.(CESPE/TRT-RN-2oIo) OS padrões de projeto podem ser definidos como soluções já testadas para problemas que ocorrem frequentemente durante o projeto de software.
Comentários:

Apenas a definição! Fácil, fácil, né?! Padrões de Projeto são descrições de objetos que se comunicam e classes que são customizadas para resolver um problema genérico em um contexto específico. Esses padrões nomeiam, abstraem e identificam aspectos comuns em uma estrutura e os torna úteis para que sejam realizados.
Gabarito: Correto

26.(CESPE / ANAC - 2009) O uso de padrões de projeto somente pode ser aplicado a projetos que implementam o paradigma de programação orientada a objetos.
Comentários:

Não caiam nessa pegadinha! Padrões GOF somente podem ser aplicados a projetos orientados a objetos. No entanto, padrões de projeto (sem especificar quais) podem ser usados com qualquer paradigma.
Gabarito: Errado

27.(CESPE / TCU - 2009) Caso seja verificado no desenvolvimento de um sistema forte acoplamento entre as classes, recomenda-se o uso do padrão de comportamentoFactory
Method, que evita o acoplamento do remetente de uma solicitação ao seu receptor, dando a mais de um objeto a oportunidade de tratar uma solicitação, mesmo nos casos em que o conjunto de objetos não seja conhecido a priori ou seja definido dinamicamente.
Comentários:

Propósito

Criação Estrutura Comportamento

Builder
Abstract Factory

Prototype
Singlenton
Factory Method

Adapter
Bridge
Composite
Decorator
Facade
Flyweight
Proxy

Chain of Responsibility
Command

Iterator
Mediator
Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Padrão de Comportamento Factory Method? Espera aí: "A fábrica abstrata constrói Opa,Factory Method é um padrão criacional! Ademais, a descrição se trata do padrão Chain ofResponsability!

Gabarito: Errado

28.(CESPE / TCU - 2009) No desenvolvimento de um sistema estruturado em subsistemas para facilitar o acesso e minimizar a comunicação e dependências entre os subsistemas, o padrão de criação Factory Method, que fornece uma interface para a criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas, é mais indicado que o padrão de criação Prototype.
Comentários:

ABSTRACTFACTORY
FACTORY METHOD

Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
Esse padrão define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.
Fornece uma interface para a criação de famílias de objetos? Opa, isso é Abstract
Factory - não confundam com Factory Method! Um aluno já me perguntou sobre o início da questão, mas cuidado: no início, fala-se de um sistema estruturado, mas isso nada tem a ver com paradigma estruturado - é estruturado, no sentido de organizado.
Gabarito: Errado

2g.(CESPE / TCU - 2009) Se, no desenvolvimento de uma aplicação que leia documentos do tipo txt e seja capaz de converter o documento em vários formatos distintos, houver a necessidade de facilitar acréscimos de novos tipos de conversão, será mais indicado o uso do padrão de estrutura Adapter que o uso do padrão de estrutura Bridge, pois o padrão Adapter separa a construção de um objeto complexo de sua representação para criar representações diferentes com o mesmo processo.
Comentários:

BUILDER Esse padrão separa a construção de um objeto complexo da sua representação,
de forma o mesmo processo de construção possa criar diferentes tipos de representações.
Separa a construção de um objeto complexo de sua representação? Opa, isso é Builder!

Gabarito: Errado

3o.(CESPE / TCE-RN - 2009) O template method se aplica primariamente às classes, sendo um padrão de projeto com finalidade comportamental, ou seja, caracterizado pela maneira como as classes interagem e distribuem responsabilidades.
Comentários:

TEMPLATE METHOD Esse padrão define 0 esqueleto de um algoritmo dentro de uma operação, deixando alg passos a serem preenchidos pelas subclasses.
Questão perfeita! Alguns métodos se aplicam primariamente às classes, como: Template
Method,
Interpreter, Adapter e Factory Method. O restante se aplica primariamente a objetos.

Gabarito: Correto

3i.(CESPE / STJ - 2008) Os padrões de projeto podem ser usados no projeto orientado a objetos para apoiar o reúso de software. Esses padrões frequentemente empregam a herança e o polimorfismo para prover generalidade. Abstract factory, strategy e template method são padrões de projeto que podem ser empregados nos frameworks orientados a objetos para facilitar a adaptação dos frameworks.
Comentários:

A questão está toda correta! A única dúvida que poderia gerar seria em relação a última parte,porém esses três padrões têm o intuito - sim - de adaptar frameworks.

Gabarito: Correto

32.(CESPE/TJ-DF-2oo8) O padrão de projeto orientado a objetos denominado singleton exprime o fenômeno recorrente na análise que é a existência de muitas aplicações nas quais há um objeto que é a única instância de sua classe.
Comentários:

SINGLETON Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de global a ela.
Gabarito: Correto

33. (CESPE / SERPRO - 2008) Adapter é um padrão estrutural utilizado para compatibilizar interfaces de modo que elas possam interagir.
Comentários:

Propósito

Criação Estrutura Comportamento

Builder
Abstract Factory
Prototype
Singlenton
Factory Method

Adapter
Bridge
Composite
Decorator
Facade
Flyweight
Proxy

Chain of Responsibility
Command

Iterator

Mediator
Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Estrutural? Lembrem-se do mnemónico: "A Ponte Adaptada portanto é estrutural.
Compatibilizar interfaces de modo que elas possam interagir? Opa, isso é Adapter!

Gabarito: Correto

34. (CESPE / SERPRO - 2008) O Singleton é um padrão que garante que uma classe tenha apenas uma instância.
Comentários:

SINGLETON Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de global a ela.
Classe com apenas uma instância? Opa, isso é Singleton!

Gabarito: Correto

35. (CESPE /SERPRO - 2008) Alguns padrões de criação como o Prototype, o Proxy e o Façade não são adequados para a programação orientada a objetos.
Comentários:

Como é? Não faz nenhum sentido! Eles são adequados, sim...

Gabarito: Errado

36.(CESPE / STF - 2008) A figura acima, adaptada de java.sun.com, ilustra a arquitetura de uma aplicação web desenvolvida na plataforma J2EE, tendo sido alguns de seus módulos nomeados de A até I. Considere que uma aplicação com a arquitetura mostrada tenha sido instalada em um servidor de aplicação JBoss 4.0 ou superior, por meio do deploy de um arquivo com nome aplicação.war, e se encontrem pleno funcionamento. Conforme a nomenclatura proposta peloGoF (Gang of Four) book, o nome dado ao módulo F sugere que esse módulo implementa um padrão da categoria comportamental, enquanto o nome do módulo C sugere que ele implementa um padrão da categoria estrutural.
HTTP Request

A

* do Front Controüer -----------------------------------
Applicabon

Controfier

Dispatcher

▼

Cornniand

►

Composrte
Víew

!►

c Víew Helper Facade

Service Locator

HTTP Response

◄—

Comentários:

Propósito

Criação Estrutura Comportamento

Builder
Abstract Factory

Prototype
Singlenton
Factory Method

Adapter
Bridge
Composite
Decorator
Facade
Flyweight
Proxy

Chain of Responsibility
Command

Iterator
Mediator
Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

F é Command! Command é comportamental? Sim. C é Composite! Composite é estrutural? Sim.

Gabarito: Correto

37.(CESPE/TST-2OO7) Um dos mecanismos da orientação a objetos para reutilização de software é a identificação e documentação de padrões de projeto (design patterns), que são modelos particulares de classes e de objetos comunicantes que se repetem de um projeto para outro e que podem assim ser padronizados.
Comentários:

Perfeita definição de Design Pattern!

Gabarito: Correto

38.(CESPE / DATAPREV - 2006) As seguintes situações justificam o uso do padrão AbstractFactory: o sistema deve ser independente de como os objetos são criados; o sistema deve poder ser configurado com diferentes famílias de classes; é necessário garantir que certas classes sejam usadas em conjunto.
Comentários:

ABSTRACTFACTORY Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou sem especificar suas classes concretas.
Família de classes/objetos? Opa, Abstract Factory!

Gabarito: Correto

39-(CESPE / DATAPREV - 2006) As seguintes situações justificam o uso do padrão
Adapter: é necessário um objeto local que se faça passar por um objeto localizado em outro espaço de endereçamento; é necessário controlar o acesso a um objeto; um objeto persistente deve ser carregado em memória somente quando for referenciado.
Comentários:

PROXY Esse padrão provê um substituto ou ponto através do qual um objeto pode controlar 0a outro objeto.

Controlar 0 acesso a um objeto? Proxy!

Gabarito: Errado

4O.(CESPE / DATAPREV-2006) As seguintes situações justificam o uso do padrão Command: um conjunto de objetos se comunica de forma definida porém complexa, o que resulta em interdependências difíceis de serem entendidas; o reúso está sendo dificultado pois cada objeto se comunica com vários outros objetos.
Comentários:

MEDIATOR

Esse padrão define um objeto que encapsula a forma como um conjunto de objetos interagem, promovendo um fraco acoplamento ao evitar que objetos se refiram aos outros explicitamente.
Forma bem definida, porém complexa? Mediator!

Gabarito: Errado

4i.(CESPE / DATAPREV - 2006) As seguintes situações justificam o uso do padrão
Strategy: é necessário configurar uma classe com uma variedade de comportamentos; uma classe usa diferentes variações de um algoritmo; o método de uma classe tem muitos enunciados condicionais pois a classe tem comportamentos variados.
Comentários:

STRATEGY Esse padrão define uma família de algoritmos, encapsula cada um e faz deles intercambiáveis.
Variações de algoritmo? Strategy!

Gabarito: Correto

42.(CESPE / DATAPREV - 2006) Quanto aos padrões de projeto orientados a objetos, assinale a opção correta.
a) O Facade pode ser usado quando se deseja prover uma interface simples para um subsistema complexo; existem muitas dependências entre clientes e as classes que implementam uma abstração.
b) Pode-se usar o Decorator quando um sistema deve ser configurado com uma entre várias famílias de produtos; uma família de produtos relacionados foi projetada para ser usada em conjunto.
c) O Adapter pode ser usado quando objetos se comunicam de forma definida, mas complexa;as interdependências entre os objetos são difíceis de entender; o reúso está sendo dificultado,pois um objeto se comunica com vários outros.

d) Pode-se usar o Builder quando o comportamento de um objeto muda em tempo de execução e depende do seu estado; as operações têm múltiplos enunciados condicionais que dependem do estado do objeto.
Comentários:

(a) Correto; (b) Errado, trata-se do Abstract Factory; (c) Errado, trata-se do
Mediator; (d) Errado,
trata-se do State.

Gabarito: Letra A

QUESTõES CoMENTADAS - FCC

4. (FCC / Prefeitura de Teresina-PI - 2016) Dentre os tipos de Padrões de
Projeto (Design
Patterns) o que se caracteriza por definir uma interface para a criação de um objeto e que permite que a subclasse decida qual classe instanciar é denominado a) Factory Method.
b) Builder.

c) Prototype.

d) Abstract Factory.

e) Composite.

Comentários:

FACTORY METHOD Esse padrão define uma interface para criarum objeto, mas deixa as subclasses decidirem qual classe instanciar.
O padrão onde se permite o adiamento da instanciação é o: Factory Method.

Gabarito: Letra A

5. (FCC/TRE-PB-2015) Um técnico deseja usar um padrão de projeto de criação que permita que as subclasses da aplicação possam variar. Este padrão deverá ser focado no processo de instanciação e encapsular a criação de objetos, deixando as subclasses decidirem quais objetos criar e garantindo assim, baixo acoplamento. Para conseguir o que deseja, o técnico selecionou o padrão de projeto que possui uma classe abstrata Creator que define um método especifico para criação de objetos. Trata-se do padrão:
a) Prototype.

b) Adapter.

c) Factory Method.

d) Composite.

e) Façade.

Comentários:

FACTORY METHOD Esse padrão define uma interface para criarum objeto, mas deixa as subclasses decidirem qual classe instanciar.
Mais uma vez cobrando Factory Method! Já alertamos o fato para vocês outras vezes,
mas a FCC
repete muito item! Vale muito a pena fazer muitas questões, de novo, e de novo ©

6. (FCC / TRT13 - 2014) Angela pretende utilizar alguns design patterns em seu projeto Java e,após algumas pesquisas, encontrou o que buscava em Singleton e Prototype cujos objetivos são,respectivamente:

I. Encapsular a escolha das classes concretas a serem utilizadas na criação dos objetos de diversas famílias.
II. Permitir a criação de uma única instância de uma classe e fornecer um modo para recuperá-la.

III. Possibilitar o reaproveitamento de objetos.

IV. Possibilitar a criação de novos objetos a partir da cópia de objetos existentes.

Está correto o que consta APENAS em a) I e II.
b) I e III.

c) lie III.

d) lie IV

e) III e IV.

Comentários:

Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
Esse padrão especifica os tipos de objetos para criar usando uma instância como protótipo e cria novos objetos copiando este protótipo.
Os itens que correspondem ao Singleton e Prototype são (II) e (IV).

Gabarito: Letra D

7. (FCC / DPE-SP-2013) Um design pattern descreve uma solução geral comprovada e reutilizável para um problema recorrente no desenvolvimento de sistemas de software orientados a objetos. Padrões de projeto ajudam a reconhecer e implementar boas soluções para problemas comuns. Dois dos principais design patterns utilizados atualmente são descritos a seguir:
I. Visa garantir que uma classe só tenha uma única instância e prover um ponto de acesso global a ela.
II. Visa definir uma dependência um-para-muitos entre objetos para que quando um objeto mudar de estado os seus dependentes sejam notificados e atualizados automaticamente.
Os design patterns descritos em I e II são, respectivamente:

a) Singleton e Observer.

b) Facade e Adapter.

c) Composite e Adapter.

d) Singleton e Command.

e) Facade e Observer.

Comentários:

SINGLETON

Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
(I) Ponto de acesso global? Singleton!

OBSERVER

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.
(II) Dependentes notificados automaticamente? Observer.

Gabarito: Letra A

8. (FCC / TRT15 - 2013) Os padrões Gang of Four (GoF) organizam um conjunto de padrões de projeto (design patterns) em três grupos: de criação, estruturais e comportamentais. Três destes padrões são descritos a seguir:
I. Em situações em que classes precisam trabalhar juntas, mas isto não está sendo possível porque suas interfaces são incompatíveis, pode-se utilizar este design pattern que permite converter a interface de uma classe em outra interface esperada pelos clientes de forma que classes com interfaces incompatíveis possam interagir.
II. Este design pattern pode ser utilizado quando se deseja definir uma dependência um-para-muitos entre objetos de modo que quando um objeto muda o estado, todos seus dependentes são notificados e atualizados.
III. Em situações em que se deseja acessar o conteúdo de uma coleção sem expor sua representação interna utiliza-se este design pattern que permite prover uma interface única para varrer coleções diferentes.
Os padrões descritos nos itens I, II e III são, respectivamente,

a) Adapter, Facade e Strategy.

b) Prototype, Composite e Command.

c) Abstract Factory, Observere Iterator.

d) Adapter, Observer e Iterator.

e) Abstract Factory, Composite e Command.

Comentários:

Esse padrão converte a interface de uma classe em outra interface que normalmente não

ADAPTER poderiam trabalhar juntas por serem incompatíveis.

(I) Interfaces incompatíveis? Adapter!

OBSERVER

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.
(II) Quando um objeto muda o estado, todos os seus dependentes são notificados e atualizados?
Observer!

ITERATOR

Esse padrão fornece uma maneira de acessar elementos de um objeto agregado sequencialmente sem expor sua representação interna.
(III) Deseja acessar o conteúdo de uma coleção? Iterator.

Gabarito: Letra D

9. (FCC / AL-RN - 2013) Analise as seguintes afirmações:

I. Fornece uma interface para a criação de uma família de objetos relacionados ou dependentes sem fornecer os detalhes de implementação das classes concretas.
II. Converte uma interface de uma classe existente em outra interface esperada pelos clientes.Permite que algumas classes com interfaces diferentes trabalhem em conjunto.

III. Separa uma implementação de sua abstração, de forma que ambas possam variar independentemente.
IV. Separa a construção de um objeto complexo de sua representação, de modo que o mesmo processo possa criar representações diferentes.
Tratam, respectivamente, dos design patterns:

a) Builder - Adapter - Bridge - Abstract Factory.

b) Abstract Factory - Adapter - Bridge - Builder.

c) Bridge - Adapter - Builder - Abstract Factory.

d) Adapter - Builder - Abstract Factory - Bridge.

e) Builder - Bridge - Abs tract Factory - Adapter.

Comentários:

ABSTRACTFACTORY Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
(I) Trata-se do Abstract Factory.

ADAPTER Esse padrão converte a interface de uma classe em outra interface que normalmente poderiam trabalhar juntas por serem incompatíveis.
(II) Trata-se do Adapter.

BRIDGE Esse padrão desacopla uma interface de sua implementação, de forma que ambas possa m variar independentemente.
(III) Trata-se do Bridge.

BUILDER Esse padrão separa a construção de um objeto complexo da sua representação,
de forma o mesmo processo de construção possa criar diferentes tipos de representações.
(IV) Trata-se do Builder.

Gabarito: Letra B

io.(FCC /TCE-PR-2011) OS design patterns:

a) são projetos de arquitetura para um domínio específico de aplicação e sempre trazem componentes predefinidos que envolvem código de programação.
b) consistem em conjuntos de classes que um usuário instancia para utilizar seus métodos. Após a chamada ao método, o controle do fluxo da aplicação retorna para o usuário.
c) são de uso exclusivo em processos de desenvolvimento de soluções orientado a objetos, já que os objetos são a mais adequada abstração para o reúso.
d) são aplicações propriamente ditas, normalmente construídas pela integração de diversos frameworks.
e) podem ser modelados utilizando-se a linguagem UML que fornece um meio eficiente de modelar padrões de projeto representando-os como colaborações.
Comentários:

(a) Errado. Domínio específico? Não, trata-se de domínio genérico! Sempre trazem código?
Também não; (b) Errado. Design Patterns não consistem em conjuntos de classes! Aliás, quem falou em orientação a objetos? A questão se refere a Design Patterns em geral; (c) Errado.Galera, lembrem-
se de que Padrões de Projeto (GOF) são orientados a objetos, mas a questão não especificou - ela disse bem genericamente; (d) Errado. Aplicações, não! São modelos, descrições,etc. Galera,
padrões de projeto são muito mais abstratos do que aplicações; (e) Correto. Pode-se utilizar aLinguagem UML. Ademais, é possível representá-los de diversas maneiras,
inclusive com colaborações.
Gabarito: Letra E

li. (FCC / TRT24 - 2011) Considere:

I. Fornecer uma interface para criação de famílias de objetos relacionados ou dependentes, sem especificar suas classes concretas. Possibilitar o adiamento da instanciação para as subclasses.
II. Garantira existência de apenas uma instância de uma classe, mantendo um ponto global de acesso ao seu objeto.
III. Possibilitar o armazenamento do estado interno de um objeto em um determinado momento, para que seja possível retorná-lo a este estado, caso necessário.
I, II e III são, respectivamente, objetivos dos Design Patterns intitulados:

a) Interpreter, Iteratore Memento.

b) Command, Singleton e Iterator.

c) Factory Method, Singleton e Memento.

d) Iterator, Factory Method e Flyweight.

e) Singleton, Flyweight e Command.

Comentários:

FACTORY METHOD Esse padrão define uma interface para criarum objeto, mas deixa as subclasses decidirem qual classe instanciar.
(I) Na minha opinião, houve confusão da FCC! Factory Method fornece uma interface para criar um objeto, possibilitando o adiamento da instanciação para as subclasses. Já oAbstract Factory fornece uma interface para criar uma família de objetos, relacionados ou dependentes, sem especificar suas classes concretas. Ou seja, a FCC misturou ambas as definições, no entanto considerou como Factory Method;
SINGLETON Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de global a ela.
(II) Ponto global de acesso? Ficou fácil: Singleton;

MEMENTO Esse padrão captura e externaliza o estado interno de um objeto,
sem violar encapsulamento, de maneira que o objeto possa ser restaurado posteriormente.
(III) Armazenar estado interno de um objeto para retornar, se necessário? Ficou fácil: Memento.

Gabarito: Letra C

12.(FCC /TRE-RN - 2011) Na engenharia de software, os padrões de projetos comportamentais tratam das interações e divisões de responsabilidades entre as classes ou objetos. São exemplos típicos dessa família:
a) Command, Factory Method e Prototype.

b) Builder, Prototype e Singleton.

c) Chain of Responsability, Interpreter e Iterator.

d) Adapter, Bridge e Façade.

e) Abstract Factory, Builder e Composite.

Comentários:

Propósito

Criação Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

(a) Errado. Factory Method e Prototype são Criacionais; (b) Errado. Todos são
Criacionais; (c)
Correto. Todos são Comportamentais; (d) Errado. Todos são Estruturais; (e)
Errado. Todos são
Criacionais.

Gabarito: Letra C

13. (FCC / TRT4 - 2011) O catálogo de padrões de projeto (Design Patterns) do GoF contém:

a) 20 padrões e está basicamente dividido em duas seções: Structural e Behavioral.

b) 21 padrões e está basicamente dividido em duas seções: Creational e Behavioral.

c) 23 padrões e está basicamente dividido em duas seções: Structural e Behavioral.

d) 23 padrões e está, basicamente, dividido em três seções: Creational, Structural e Behavioral.

e) 24 padrões e está basicamente dividido em três seções: Creational, Spectral e Behavioral.

Comentários:

Propósito

Criação Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

23 Padrões de Projeto, dividido em Criacional, Estrutural e Comportamental.

Gabarito: Letra D

14.(FCC / TRT14 - 2011) No contexto dos padrões de projeto:

I. Oferecer uma interface simples para uma coleção de classes.

II. Desacoplar uma abstração de sua implementação para que ambas possam variar independentemente.
Correspondem respectivamente a:

a) Façade e Bridge.

b) Adapter e Façade.

c) Composite e Bridge.

d) Façade e Composite.

e) Bridge e Adapter.

Comentários:

Esse padrão oferece uma interface unificada para um conjunto de interfaces em um subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.
Esse padrão desacopla uma interface de sua implementação, de forma que ambas possam variar independentemente.
Quem oferece uma interface simples para uma coleção de classes é o Façade e quem desacopla uma abstração de sua implementação para que ambas possam várias independentemente é oBridge.

Gabarito: Letra A

15. (FCC / TRF4 - 2010) Sobre os design patterns, é correto afirmar:

a) Padrões e linguagens de padrões são maneiras de implementar sistemas orientados a objetos por meio da captação da experiência de programadores. Os padrões, apesar de abstratos,sempre incluem algum código de programação.

b) São aplicações, propriamente ditas, dedicadas aos domínios de aplicações específicos,
tais como sistemas de telecomunicações ou financeiros.
c) Não são complexos e necessita-se de um tempo mínimo para aprender a usá-los.

d) O princípio geral de englobamento de experiência em um padrão é aplicável apenas à abordagem de projeto de software orientado a objetos.
e) O padrão é uma descrição de conhecimento e experiência acumulados, uma solução comprovada para um problema comum.
Comentários:

(a) Sempre incluem algum código de programação? Não; (b) Padrões de Projeto não são aplicações propriamente ditas; (c) Afirmar que não são complexos é perigoso! Há padrões bastante complicados; (d) De novo, não! Padrões de Projeto não se limitam a orientação a objetos; (e) É isso mesmo! Questão perfeita!
i6.(FCC / TJ-PI - 2009) Os padrões de projeto, quando aplicados ao desenvolvimento de aplicações,fornecem meios de descrever soluções comuns para problemas comuns, resultando em redução de tempo gasto com 0 desenvolvimento e melhoria da qualidade da aplicação.
Analise:

I. É o responsável pela especificação dos tipos de objetos a serem criados usando uma
"instância"
prototípica e pela criação de novos objetos copiando este protótipo.

II. Define uma interface de nível mais alto que torna o subsistema mais fácil de usar e fornece uma interface única para um subsistema com diversas interfaces; compõe o grupo de padrões estruturais.
III. Integrante do grupo de padrões comportamentais, ele provê uma forma de acessar sequencialmente os elementos de um agregado de objetos, sem expor a representação interna desse agregado.
IV. As consequências do uso deste padrão é que o encapsulamento é mantido, já que objetos usam sua própria informação para cumprir responsabilidades; leva ao fraco acoplamento entre
' objetos e à alta coesão, uma vez que objetos fazem tudo que é relacionado à sua própria informação.
As afirmações correspondem, respectivamente, aos padrões a) Command, Iterator, Singleton e Expert.
b) Controller, Expert, Singleton e Prototype.

c) Command, Singleton, Controller e Façade.

d) Prototype, Façade, Iterator e Expert.

e) Adapter, Façade, Command e Iterator.

Comentários:

PROTOTYPE

Esse padrão especifica os tipos de objetos para criar usando uma instância como e cria novos objetos copiando este protótipo.
(I) Instância prototípica? Trata-se do Prototype!

FAÇADE Esse padrão oferece uma interface unificada para um conjunto de interfaces em subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.
(II) Interface de nível mais alto? Trata-se do Façade.

ITERATOR Esse padrão fornece uma maneira de acessar elementos de um objeto agregado sequencialmente sem expor sua representação interna.
(III) Provê forma de acessar sequencialmente? Trata-se do Iterator.

(IV) Expert? Isso é Padrão GRASP e, não, GOF (é outro assunto!).

Gabarito: Letra D

17. (FCC / Infraero - 2009) As associações entre classes e objetos são tratadas pelos Padrões deProjeto de Software (Design Patterns) da família de Padrões:

a) GoF Estruturais.

b) GRASP Comportamentais.

c) GRASP Estruturais.

d) GoF de Criação.

e) GoF Comportamentais.

Comentários:

A associação entre classes e objetos é tratada por Padrões GoF Estruturais.

Gabarito: Letra A

QUESTõES CoMENTADAS - FG V

4. (FGV / AL-Caruaru - 2015) O catálogo denominado Padrões GoF ('Gang of
Four') define soluções reutilizáveis para problemas frequentes em projetos de sistemas de software.Essas soluções estão organizadas em três famílias conforme o propósito de cada solução. Os padrões de projetos denominados Interpreter, Prototype e Flyweight que fazem parte desse catálogo,pertencem, respectivamente, às seguintes famílias:

a) padrão comportamental, padrão de criação e padrão estrutural.

b) padrão estrutural, padrão comportamental e padrão de criação.

c) padrão comportamental, padrão estrutural e padrão de criação.

d) padrão estrutural, padrão de criação e padrão comportamental.

e) padrão de criação, padrão comportamental e padrão estrutural.

Comentários:

PA&POÍ-S PE CRKÃO

A FÁSRICA AÉSTRATA CONSTRÓI UM PROTÓTIPO ÚNICO,

A FÁÉRICA ASSTRATA CONSTRÓI

UM PROTÓTIPO ÚNICO,

A FÁSRICA ASSTRATA CONSTRÓI UM
A FÁÉRICA ASSTRATA CONSTRÓI UM
A FÁÉRICA ASSTRATA CONSTRÓI UM
A FÁÉRICA AÉSTRATA CONSTRÓI UM
A FÁÉRICA AÉSTRATA CONSTRÓI UM

PROTÓTIPO ÚNICO,
PROTÓTIPO ÚNICO,
PROTÓTIPO ÚNICO,
PROTÓTIPO ÚNICO,
PROTÓTIPO ÚNICO,

A FÁÉRICA AÉSTRATA CONSTRÓI
A FÁSRICA ASSTRATA CONSTRÓI
A FÁSRICA ASSTRATA CONSTRÓI
A FÁÉRICA AÉSTRATA CONSTRÓI
A FÁSRICA ASSTRATA CONSTRÓI

UM PROTÓTIPO ÚNICO,
UM PROTÓTIPO ÚNICO,
UM PROTÓTIPO ÚNICO,
UM PROTÓTIPO ÚNICO,
UM PROTÓTIPO

A PONTÉ
AA rPVONNTTpÉ

PAPPOtS ESTRUTURAIS

APAPTAPA É COMPOSTA PÉ PÉCORACÕÉS NA FACHAPA PARA O PÉSO MOSCA SÉ APROXIMAR.
APAPTAAl/PAAriAIÉ/ACtOCMGPWOISFTVASTPAÉ PÉCOURt^ACCOÕRÉASÇOt^S NA FFAACCHHAAUPAAPPAARRAA
OOPÉkSt^OSO MMOOSSCCAA SSpÉ AAPPRROOXXII o*

A PONTÉ APAPTAPA É COMPOSTA PÉ PÉCORAfÕÉS NAFACHAPA PARA O PÉSO MOSCA SÉ
APROX

A PONTÉ APAPTAPA É COMPOSTA PÉ PÉCORACÕÉS NAFACHAPA PARA O PÉSO MOSCA SÉ
APROXIM^* w

A PONTÉ-----A--P--A--P--T--A--P--A----É--- ' COMPOSTA PÉ PÉCORAfÕÉS ' NA FACHAPA
-P--A--R---A----------------OSÉPO ---M-----OS--C--A-- --S--É-
-------A---P-R-----OX--I-MA 'J

A PONTÉ

APAPTAPA

É COMPOSTA PÉ PÉCORAÇÕÉS

NA FACHAPA PARA O PÉSO

MOSCA

SÉ APROXIMAR. | |

Vocês decoraram as frases? Interpreter não está nas frases, então é um Diagrama
Comportamental;
Prototype está na primeira frase, então é um Diagrama de Criação; Flyweight está na segunda frase, então é um Padrão de Estrutural.
Gabarito: Letra A

5. (FGV/AL-MA-2013) Com relação ao tema Padrões de Projeto, conforme descritos porGamma et AlIi, sobre o padrão Prototype, analise as afirmativas a seguir.
I. Apresenta como benefícios adicionais a adição e a remoção de produtos em tempo de execução.
II. Apresenta como benefícios adicionais a especificação de novos objetos pela variação de seus valores e/ou de sua estrutura.
III. Apresenta como benefícios adicionais a redução da necessidade de criação de subclasses.

Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente a afirmativa II estiver correta.

c) se somente a afirmativa III estiver correta.

d) se somente as afirmativas I e II estiverem corretas.

e) se todas as afirmativas estiverem corretas.

Comentários:

Todas as alternativas estão corretas - tratam de benefícios ou vantagens corretas.

Gabarito: Letra E

6. (FGV / Senado Federal - 2008) Considera as seguintes assertivas sobre as vantagens do uso de padrões de software (software patterns):
I. Padrões de projeto proporcionam um vocabulário comum de projeto,
facilitando comunicação, documentação e aprendizado dos sistemas de software.
II. Padrões de projeto auxiliam no desenvolvimento de software por meio da reutilização do projeto de soluções computacionais já testadas e aprovadas.
III. Uma biblioteca de padrões pode ajudar a melhorar e padronizar o desenvolvimento de software.
As assertivas corretas são:

a) somente II.

b) somente I e II.

c) somente I e III.

d) somente II e III.

e) I, lie III.

Comentários:

(I) Correto, eles possuem um jargão próprio comum a todos: nome, problema,
solução e consequências; (II) Correto, grande parte dos problemas já possuem uma solução conhecida,formalmente documentada e exaustivamente testada, uma vez que se tratam de problemas recorrentes; (III) Correto. Imaginem que, em uma equipe de programadores, todos utilizam um determinado padrão de projeto, mas cada um à sua maneira. Não seria melhor ter uma biblioteca de padrões afim de padronizar e melhorar o desenvolvimento de software?
Gabarito: Letra E

QUESTõES CoMENTADAS - DIvERSAS BANCAS

4. (IBFC / Prefeitura de Divinópolis-MG - 2018) Os padrões de projetos (Design
Patterns) são compostos basicamente por 4 elementos essenciais que são:
a) Nome do software + Problema a ser resolvido + Solução dada pelo padrão + Tempo de desenvolvimento b) Nome do padrão + Problema a ser resolvido + Solução dada pelo padrão + Consequências c) Nome do software + Problema a ser resolvido + Planejamento das atividades + Consequências d) Nome do padrão + Problema a ser resolvido + Planejamento das atividades + Tempo de desenvolvimento
Comentários:

O template padrão de um padrão de projeto é: (1) Nome do Padrão; (2) Problema a ser resolvido;
(3) Solução dada pelo padrão; (4) Tempo de Desenvolvimento.

Gabarito: Letra B

5. (IBFC / EBSERH - 2017) Os Padrões de Projeto de software são organizados em três famílias conforme a "Gangue dos Quatro" (Gang of Four). Dos "Padrões de Criação" abaixo,identifique qual deles não pertence a essa família especificamente:
(1) Abstract Factory

(2) Builder

(3) Factory Method

(4) Prototype

(5) Proxy a) somente o 1 não pertence a essa família especificamente.
b) somente o 2 não pertence a essa família especificamente.

c) somente o 3 não pertence a essa família especificamente.

d) somente o 4 não pertence a essa família especificamente.

e) somente o 5 não pertence a essa família especificamente.

Comentários:

CriaçJão

Propósito

Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

(i) Abstract Factory é um padrão de criação; (2) Builder é um padrão de criação; (3)
Factory Method é um padrão de criação; (4) Prototype é um padrão de criação; (5) Proxy é um padrão estrutural.
Gabarito: Letra E

6. (IBFC / EBSERH - 2017) Erich Hamma, Richard Helm, Ralph Johson e John Vlissdes,
mais conhecidos como "Gang of Four", coletaram originalmente 23 Design Pattems(Padrões de
Projeto) e organizaram em 3 grupos denominados:

a) Startup Standards (Padrões de Inicialização) - Intermediate Patterns (Padrões
Intermediários)

- Finishing Standards (Padrões de Fiinalização).

b) Interaction patterns (Padrões de Interação) - Beta Standards (Padrões Beta)
- Finishing
Standards (Padrões de Finalização).

c) Creational Patterns (Padrões de Criação) - Structural Patterns (Padrões
Estruturais) -
Behavioral Patterns (Padrões Comportamentais).

d) Users Patterns (Padrões de Usuários) - Creational Patterns (Padrões de Criação) -
Interaction patterns (Padrões de Interação).
e) Alpha Standards (Padrões Alfa) - Beta Standards (Padrões Beta) - Patterns Gamma
(Padrões
Gama).

Comentários:

CriaçJão

Propósito

Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Os tipos de padrão são: Padrões de Criação (Creational Patterns), Padrões Estruturais
(Structural
Patterns) e Padrões Comportamentais (Behavioral Patterns).

Gabarito: Letra C

7. (ESAF / CGU - 2012) O padrão de projeto singleton é usado para restringir:

a) a instanciação de uma classe para objetos simples.

b) a instanciação de uma classe para apenas um objeto.

c) a quantidade de classes.

d) as relações entre classes e objetos.

e) classes de atributos complexos.

Comentários:

SINGLETON Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
Ele restringe a instanciação de uma classe para apenas um objeto ou instância.

Gabarito: Letra B

8. (FEMPERJ /TCE-RJ -2012) Padrões de Projeto descrevem soluções para problemas recorrentes no desenvolvimento de sistemas de software orientados a objetos. Um padrão de projeto estabelece um nome e define o problema, a solução, quando aplicar esta solução e suas consequências. Um dos padrões de projeto mais utilizados é o padrão Adapter(adaptador), que tem como função:
a) garantir a existência de apenas uma instância de uma classe, mantendo um ponto global de acesso ao seu objeto.
b) adicionar dinamicamente um comportamento a um objeto existente sem alterar o código das classes existentes.
c) fornecer uma interface para a criação de famílias de objetos correlatos ou dependentes sem a necessidade de especificar a classe concreta destes objetos.
d) definir novas operações sem alterar as classes dos elementos sobre os quais ele opera.

e) permitir que classes com interfaces incompatíveis possam interagir.

Comentários:

SINGLETON

Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
(a) Errado, trata-se do Singleton.

Esse padrão anexa responsabilidades adicionais a um objeto dinamicamente. Fornece uma

DECORATOR alternativa flexível em relação à herança para estenderfuncionalidades.

(b) Errado, trata-se do Decorator.

ABSTRACT FACTORY

Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
(c) Errado, trata-se do Abstract Factory.

VISITOR

Esse padrão representa uma operação a ser realizada sobre elementos de uma estrutura objetos e permite definir uma operação sem mudar as classes dos elementos sobre os qu opera.
(d) Errado, trata-se do Visitor.

Esse padrão converte a interface de uma classe em outra interface que normalmente não

ADAPTER poderiam trabalhar juntas por serem incompatíveis.

(e) Correto, trata-se do Adapter.

Gabarito: Letra E

9- (ESAF/ATRFB-2012) OS padrões de projeto (Design Patterns) são classificados nas categorias:

a) Situacional. Estrutural. Complementar.

b) Criacional. Evolutiva. Contingencial.

c) Compartimentai. Vinculada. Comportamental.

d) Criacional. Step-by-step. Orientada a requisitos.

e) Criacional. Estrutural. Comportamental.

Comentários:

Propósito

Criação Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Classifica-se em Criacional, Estrutural ou Comportamental.

Gabarito: Letra E

io.(ESAF / CGU - 2008) Ao longo das últimas décadas, a engenharia de software fez progressos significativos no campo de padrões de projeto - arquiteturas comprovadas para construir software orientado a objetos flexível e fácil de manter. Com relação ao padrão Facade,é correto afirmar que:
a) Fornece um objeto representante ou um marcador de outro objeto para controlar o acesso ao mesmo.
b) Define o esqueleto de um algoritmo em uma operação, postergando a definição de alguns passos para subclasses.
c) Define uma interface para criar um objeto, mas deixas as subclasses decidirem qual classe a ser instanciada.
d) Fornece uma interface unificada para um conjunto de interfaces em um sistema.

e) Define uma dependência "um para muitos" entre objetos, de modo que, quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados.
Comentários:

Esse padrão provê um substituto ou ponto através do qual um objeto pode controlar o acesso

PROXY a outro objeto.

(a) Errado. Trata-se do Proxy.

TEMPLATE METHOD

Esse padrão define o esqueleto de um algoritmo dentro de uma operação, deixando alguns passos a serem preenchidos pelas subclasses.
(b) Errado. Trata-se do Template Method.

FACTORYMETHOD

Esse padrão define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.
(c) Errado. Trata-se do Factory Method.

Esse padrão oferece uma interface unificada para um conjunto de interfaces em um

FACADE subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.

(d) Correto. Trata-se do Façade.

OBSERVER

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.
(e) Errado. Trata-se do Observer.

Gabarito: Letra D

ii.(ESAF / CGU - 2008) Quanto à finalidade, os padrões de projeto podem ser classificados em padrões de criação, padrões de estutura ou padrões comportamentais. Correspondem à categoria de padrões estruturais:
a) Facade, Prototype e Proxy.

b) Adapter, Composite e Proxy.

c) Adapter, Factory Method e Template Method.

d) Builder, Template Method e Strategy.

e) Adapter, Bridge e Singleton.

Comentários:

Propósito

Criação Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Trata-se do Adapter, Composite e Proxy.

Gabarito: Letra B

12. (ESAF / AFRFB - 2005) Analise as seguintes afirmações relacionadas a padrões de projetos:

I. O padrão Builder separa a construção de um objeto complexo de sua representação,
de modo a que o mesmo processo de construção possa criar diferentes representações.
II. O método Abstract Factory fornece uma interface para a criação de uma família de objetos relacionados ou dependentes sem especificar suas classes completas.
III. O padrão Bridge define uma interface para criar um objeto, mas deixa as subclasses decidirem que classe será instanciada. O Bridge permite a uma classe postergar a instanciação das subclasses.
IV. O Chain of responsability usa compartilhamento para suportar grandes quantidades de objetos e define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados.
Indique a opção que contenha todas as afirmações verdadeiras.

a) I e III.

b) lie III.

c) III e IV.

d) I e II.

e) lie IV.

Comentários:

BUILDER

Esse padrão separa a construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes tipos de representações.
(I) Contrução de um objeto complexo?Trata-se do Builder!

ABSTRACTFACTORY

Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
(II) Interface para a criação de uma família de objetos relacionados? Abstract Factory!
Observem que ele diz completa, em vez de concreta! Nesse contexto, os termos são sinônimos, isto é, a classe concreta é completa, na medida em que contém todas as implementações de seus métodos,por outro lado uma classe abstrata seria incompleta.
FACTORY METHOD

Esse padrão define uma interface para criarum objeto, mas deixa as subclasses decidirem qual classe instanciar.
(III) Interface para criar objeto deixando a decisão para subclasses? Factory Method!

Esse padrão utiliza compartilhamento para suportar eficientemente grandes quantidades de

FLYWEIGHT objetos de baixa granularidade.

OBSERVER

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.
(IV) A questão misturou Flyweight com Observer.

Gabarito: Letra D

QUESTõES CoMENTADAS - CESPE

í. (CESPE IBANRISUL- 2022) Entre os padrões definidos pelo GRASP, destacam-se baixa coesão e alto acoplamento.
2. (CESPE / BANRISUL - 2022) O objetivo do padrão Singleton é especificar os tipos de objetos a partir de uma instância de protótipo.
3. (CESPE / BANRISUL - 2022) Por meio do padrão Facade, é possível construir uma interface comum e simplificada para um sistema ou subsistema.
4. (CESPE / BANRISUL - 2022) O padrão de comportamento Command permite representar comandos como objetos, sem a necessidade de saber como a operação é executada.
5. (CESPE / BANRISUL - 2022) O padrão GRASP de Expert é utilizado para atribuir uma responsabilidade à classe que possui a informação necessária para atender essa mesma responsabilidade.
6. (CESPE / Petrobrás - 2022) Os três principais padrões de projeto (design patterns) são os criacionais, os estruturais e os comportamentais; os padrões criacionais aumentam a flexibilidade e a reutilização de código porque oferecem diversas alternativas de criação de objetos.
7. (CESPE / Petrobrás - 2022) Design patterns é um conjunto de soluções generalistas para problemas recorrentes durante o desenvolvimento de um software; trata-se de um framework ou código pronto, e não de uma definição de alto nível de como um problema comum pode ser solucionado.
8. (CESPE / TJ-RJ - 2021) A coleção GoF (Gang of Four) é formada por padrões orientados a objetos, separados em categorias. A categoria padrões estruturais é responsável por:
a) estabelecer um design de objetos reutilizáveis.

b) fornecer maneiras eficientes para criar objetos.

c) descrever como os objetos são colocados juntos.

d) descrever como os objetos interagem.

e) distribuir responsabilidades entre os objetos.

4. (CESPE / TCE-PR - 2016) Um projeto fundamentado em padrões emprega um conjunto de soluções comprovadas de maneira conceituai para a construção da aplicação em conformidade com seu escopo.
5. (CESPE / TCU - 2015) Nos padrões de projeto (design patterns) estruturais,
utilizam-se técnicas que valorizam um forte acoplamento entre as classes para favorecer o aprendizado e a portabilidade das aplicações.
6. (CESPE / INPI - 2013) O padrão bridge, além de converter a interface de uma classe existente em outra interface esperada pelos clientes, permite que algumas classes com interfaces diferentes funcionem conjuntamente.
7. (CESPE / INPI - 2013) Design patterns não se aplicam, exclusivamente, ao Java,
podendo ser empregados em projetos que utilizam linguagem C#.
8. (CESPE/ANTT-2013) Em programação orientada a objetos, o padrão de projeto denominadoIterator define uma forma de acesso sequencial aos elementos de um objeto agregado, sem expor sua representação interna.
9. (CESPE / ANTT- 2013) Em programação orientada a objetos, o padrão de projeto denominadoSingleton define uma classe que possui apenas uma instância e provê um ponto de acesso local a ela.
10. (CESPE / TCE-RO - 2013) Uma das aplicabilidades do padrão Iterator é a representação de hierarquias do tipo todo-parte de objetos, de modo que a aplicação seja capaz de ignorar a diferença entre composições de objetos e objetos individuais, haja vista que todos os objetos tratados no padrão têm comportamento uniforme.
11. (CESPE / TCO-RO - 2013) O padrão Adapter será mais apropriado que o Façade quando for necessário fornecer uma interface unificada para um conjunto de interfaces em um subsistema.
12. (CESPE / TCE-RO - 2013) O uso do padrão Builder tem a vantagem de permitir acesso controlado à instância de uma classe, uma vez que ele encapsula a classe, criando um ponto global único de acesso.
13. (CESPE / TCE-RO - 2013) Os padrões estruturais, tais como o Bridge e o Proxy,
abstraem o processo de instanciação, ajudando a tornar um sistema independente de como os seus objetos são criados. Já os padrões de criação, como Prototype e o Builder, se preocupam com a forma como as classes e os objetos são criados para formar estruturas compostas maiores.
14. (CESPE / MPOG -2013) O padrão de comportamento e encadeamento de atendentes (chain of responsibility) evita acoplamento entre solicitantes e atendentes, permitindo que mais de um objeto tenha chance de tratar a solicitação.
15. (CESPE / MPOG - 2013) Para um problema recorrente no desenvolvimento de sistemas,normalmente, um padrão de projeto descreve uma solução geral, que não pode ser reutilizada.

16. (CESPE / MPOG - 2013) Padrões de projeto envolvem combinações de classes e algoritmos associados que cumprem com propósitos comuns de projeto.
17. (CESPE / MPE-PI - 2012) O padrão de projeto conhecido como façade é indicado para a definição de uma interface de nível mais alto que torne mais fácil a comunicação entre os subsistemas de um sistema complexo.
18. (CESPE / BASA-2012) O padrão mediator define um objeto que encapsula como um conjunto de objetos interage. Esse padrão torna desnecessário que cada objeto armazene referências para todos os objetos com os quais interage e pode ser usado quando objetos se comunicam de forma definida, mas complexa.
19. (CESPE / BASA - 2012) O padrão adapter define uma família de algoritmos, permite o encapsulamento de algoritmos e possibilita a substituição desses algoritmos. Os algoritmos podem variar independentemente dos seus clientes. Esse padrão pode ser usado quando várias classes relacionadas diferirem apenas nos seus comportamentos.
20. (CESPE / MEC - 2011) O padrão Singleton garante que uma classe tenha somente uma instância, fornecendo, assim, um ponto global de acesso a essa instância.
21. (CESPE / MEC - 2011) O padrão Prototype pode ser usado no desenvolvimento de programas escritos com a linguagem PHP 5.0, atuando como padrão estrutural que permite construirtanto classes quanto objetos.
22. (CESPE / MEC - 2011) Os padrões de projeto são úteis tanto na fase de planejamento da arquitetura quanto na de desenvolvimento e codificação.
23. (CESPE / MEC - 2011) O padrão Abstract Factory é corretamente aplicável, quando necessário,para fornecer uma biblioteca de classes e não revelar suas interfaces.

24. (CESPE/TRT-RN-2010) Os padrões de projeto podem ser definidos como soluções já testadas para problemas que ocorrem frequentemente durante o projeto de software.
25. (CESPE /TRT-RN - 2010) Os padrões de projeto podem ser definidos como soluções já testadas para problemas que ocorrem frequentemente durante o projeto de software.
26. (CESPE / ANAC - 2009) O uso de padrões de projeto somente pode ser aplicado a projetos que implementam o paradigma de programação orientada a objetos.
27. (CESPE / TCU - 2009) Caso seja verificado no desenvolvimento de um sistema forte acoplamento entre as classes, recomenda-se o uso do padrão de comportamentoFactory
Method, que evita o acoplamento do remetente de uma solicitação ao seu receptor, dando a mais de um objeto a oportunidade de tratar uma solicitação, mesmo nos casos em que o conjunto de objetos não seja conhecido a priori ou seja definido dinamicamente.
28.(CESPE / TCU - 2009) No desenvolvimento de um sistema estruturado em subsistemas para facilitar o acesso e minimizar a comunicação e dependências entre os subsistemas, o padrão de criação Factory Method, que fornece uma interface para a criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas, é mais indicado que o padrão de criação Prototype.
2g.(CESPE / TCU - 2009) Se, no desenvolvimento de uma aplicação que leia documentos do tipo txt e seja capaz de converter o documento em vários formatos distintos, houver a necessidade de facilitar acréscimos de novos tipos de conversão, será mais indicado o uso do padrão de estrutura Adapter que o uso do padrão de estrutura Bridge, pois o padrão Adapter separa a construção de um objeto complexo de sua representação para criar representações diferentes com o mesmo processo.
30. (CESPE / TCE-RN - 2009) O template method se aplica primariamente às classes,
sendo um padrão de projeto com finalidade comportamental, ou seja, caracterizado pela maneira como as classes interagem e distribuem responsabilidades.
31. (CESPE / STJ - 2008) Os padrões de projeto podem ser usados no projeto orientado a objetos para apoiar o reúso de software. Esses padrões frequentemente empregam a herança e o polimorfismo para prover generalidade. Abstract factory, strategy e template method são padrões de projeto que podem ser empregados nos frameworks orientados a objetos para facilitar a adaptação dos frameworks.
32. (CESPE/TJ-DF-2008) O padrão de projeto orientado a objetos denominado singleton exprime ofenômeno recorrente na análise que é a existência de muitas aplicações nas quais há um objeto que é a única instância de sua classe.
33. (CESPE / SERPRO - 2008) Adapter é um padrão estrutural utilizado para compatibilizar interfaces de modo que elas possam interagir.
34-(CESPE / SERPRO -2008) O Singleton é um padrão que garante que uma classe tenha apenas uma instância.
35. (CESPE / SERPRO - 2008) Alguns padrões de criação como o Prototype, o Proxy e o Façade não são adequados para a programação orientada a objetos.
36. (CESPE / STF - 2008) A figura acima, adaptada de java.sun.com, ilustra a arquitetura de uma aplicação web desenvolvida na plataforma J2EE, tendo sido alguns de seus módulos nomeados de A até I. Considere que uma aplicação com a arquitetura mostrada tenha sido instalada em um servidor de aplicação JBoss 4.0 ou superior, por meio do deploy de um arquivo com nome aplicação.war, e se encontrem pleno funcionamento. Conforme a nomenclatura proposta peloGoF (Gang of Four) book, o nome dado ao módulo F sugere que esse módulo implementa um padrão da categoria comportamental, enquanto implementa um padrão da categoria estrutural.
o nome do módulo C sugere que ele

HTTP Request

A

* do Front Controfler ------------------- Applicabon

Controlar

Dispatcher

▼

Co mm and

Composrte
Víew

Service Locator

HTTP Response

◄—

37.(CESPE/TST-2OO7) Um dos mecanismos da orientação a objetos para reutilização de software é a identificação e documentação de padrões de projeto (design patterns), que são modelos particulares de classes e de objetos comunicantes que se repetem de um projeto para outro e que podem assim ser padronizados.
38.(CESPE / DATAPREV - 2006) As seguintes situações justificam o uso do padrão AbstractFactory: o sistema deve ser independente de como os objetos são criados; o sistema deve poder ser configurado com diferentes famílias de classes; é necessário garantir que certas classes sejam usadas em conjunto.
39-(CESPE / DATAPREV - 2006) As seguintes situações justificam o uso do padrão
Adapter: é necessário um objeto local que se faça passar por um objeto localizado em outro espaço de endereçamento; é necessário controlar o acesso a um objeto; um objeto persistente deve ser carregado em memória somente quando for referenciado.
/fO.(CESPE / DATAPREV-2006) As seguintes situações justificam o uso do padrão Command:
um conjunto de objetos se comunica de forma definida porém complexa, o que resulta em interdependências difíceis de serem entendidas; o reúso está sendo dificultado pois cada objeto se comunica com vários outros objetos.
4i.(CESPE / DATAPREV - 2006) As seguintes situações justificam o uso do padrão
Strategy: é necessário configurar uma classe com uma variedade de comportamentos; uma classe usa diferentes variações de um algoritmo; o método de uma classe tem muitos enunciados condicionais pois a classe tem comportamentos variados.
42.(CESPE / DATAPREV - 2006) Quanto aos padrões de projeto orientados a objetos, assinale a opção correta.
a) O Facade pode ser usado quando se deseja prover uma interface simples para um subsistema complexo; existem muitas dependências entre clientes e as classes que implementam uma abstração.
b) Pode-se usar o Decorator quando um sistema deve ser configurado com uma entre várias famílias de produtos; uma família de produtos relacionados foi projetada para ser usada em conjunto.
c) O Adapter pode ser usado quando objetos se comunicam de forma definida, mas complexa;as interdependências entre os objetos são difíceis de entender; o reúso está sendo dificultado,pois um objeto se comunica com vários outros.

d) Pode-se usar o Builder quando o comportamento de um objeto muda em tempo de execução e depende do seu estado; as operações têm múltiplos enunciados condicionais que dependem do estado do objeto.
GABARITo

1. ERRADO

2. ERRADO

3. CORRETO

4. CORRETO

5. CORRETO

6. CORRETO

7. ERRADO

8. LETRA C

g. ERRADO
io. ERRADO
li. ERRADO

12. CORRETO

13. CORRETO

14. ERRADO

15. ERRADO

16. ERRADO

17. ERRADO

18. ERRADO

19. CORRETO

20. ERRADO

21. CORRETO

22. CORRETO

23. CORRETO

24. ERRADO

25. CORRETO

26. ERRADO

27. CORRETO

28. CORRETO

29. CORRETO

30. CORRETO

31. ERRADO

32. ERRADO

33. ERRADO

34. ERRADO

35. CORRETO

36. CORRETO

37. CORRETO

38. CORRETO

39. CORRETO

40. ERRADO

41. CORRETO

42. CORRETO

43. CORRETO

44. ERRADO

45. ERRADO

46. CORRETO

47. LETRA A

QUESTõES CoMENTADAS - FCC

í. (FCC / Prefeitura de Teresina-PI - 2016) Dentre os tipos de Padrões de
Projeto (Design
Patterns) o que se caracteriza por definir uma interface para a criação de um objeto e que permite que a subclasse decida qual classe instanciar é denominado a) Factory Method.
b) Builder.

c) Prototype.

d) Abstract Factory.

e) Composite.

2. (FCC/TRE-PB-2015) Um técnico deseja usar um padrão de projeto de criação que permita que as subclasses da aplicação possam variar. Este padrão deverá ser focado no processo de instanciação e encapsular a criação de objetos, deixando as subclasses decidirem quais objetos criar e garantindo assim, baixo acoplamento. Para conseguir o que deseja, o técnico selecionou o padrão de projeto que possui uma classe abstrata Creator que define um método especifico para criação de objetos. Trata-se do padrão:
a) Prototype.

b) Adapter.

c) Factory Method.

d) Composite.

e) Façade.

3. (FCC / TRT13 - 2014) Angela pretende utilizar alguns design patterns em seu projeto Java e,após algumas pesquisas, encontrou o que buscava em Singleton e Prototype cujos objetivos são,respectivamente:

I. Encapsular a escolha das classes concretas a serem utilizadas na criação dos objetos de diversas famílias.
II. Permitir a criação de uma única instância de uma classe e fornecer um modo para recuperá-la.

III. Possibilitar o reaproveitamento de objetos.

IV. Possibilitar a criação de novos objetos a partir da cópia de objetos existentes.

Está correto o que consta APENAS em a) I e II.
b) I e III.

c) lie III.

d) II e IV

e) III e IV.

4. (FCC/DPE-SP-2013) Um design pattern descreve uma solução geral comprovada e reutilizável para um problema recorrente no desenvolvimento de sistemas de software orientados a objetos. Padrões de projeto ajudam a reconhecer e implementar boas soluções para problemas comuns. Dois dos principais design patterns utilizados atualmente são descritos a seguir:
I. Visa garantir que uma classe só tenha uma única instância e prover um ponto de acesso global a ela.
II. Visa definir uma dependência um-para-muitos entre objetos para que quando um objeto mudar de estado os seus dependentes sejam notificados e atualizados automaticamente.
Os design patterns descritos em I e II são, respectivamente:

a) Singleton e Observer.

b) Facade e Adapter.

c) Composite e Adapter.

d) Singleton e Command.

e) Facade e Observer.

5. (FCC / TRT15 - 2013) Os padrões Gang of Four (GoF) organizam um conjunto de padrões de projeto (design patterns) em três grupos: de criação, estruturais e comportamentais.Três destes padrões são descritos a seguir:
I. Em situações em que classes precisam trabalhar juntas, mas isto não está sendo possível porque suas interfaces são incompatíveis, pode-se utilizar este design pattern que permite converter a interface de uma classe em outra interface esperada pelos clientes de forma que classes com interfaces incompatíveis possam interagir.
II. Este design pattern pode ser utilizado quando se deseja definir uma dependência um-para-muitos entre objetos de modo que quando um objeto muda o estado, todos seus dependentes são notificados e atualizados.
III. Em situações em que se deseja acessar o conteúdo de uma coleção sem expor sua representação interna utiliza-se este design pattern que permite prover uma interface única para varrer coleções diferentes.
Os padrões descritos nos itens I, II e III são, respectivamente,

a) Adapter, Facade e Strategy.

b) Prototype, Composite e Command.

c) Abstract Factory, Observere Iterator.

d) Adapter, Observer e Iterator.

e) Abstract Factory, Composite e Command.

6. (FCC / AL-RN - 2013) Analise as seguintes afirmações:

I. Fornece uma interface para a criação de uma família de objetos relacionados ou dependentes sem fornecer os detalhes de implementação das classes concretas.
II. Converte uma interface de uma classe existente em outra interface esperada pelos clientes.Permite que algumas classes com interfaces diferentes trabalhem em conjunto.

III. Separa uma implementação de sua abstração, de forma que ambas possam variar independentemente.
IV. Separa a construção de um objeto complexo de sua representação, de modo que o mesmo processo possa criar representações diferentes.
Tratam, respectivamente, dos design patterns:

a) Builder - Adapter - Bridge - Abstract Factory.

b) Abstract Factory - Adapter - Bridge - Builder.

c) Bridge - Adapter - Builder - Abstract Factory.

d) Adapter - Builder - Abstract Factory - Bridge.

e) Builder - Bridge - Abs tract Factory - Adapter.

7. (FCC / TCE-PR - 2011) Os design patterns:

a) são projetos de arquitetura para um domínio específico de aplicação e sempre trazem componentes predefinidos que envolvem código de programação.
b) consistem em conjuntos de classes que um usuário instancia para utilizar seus métodos. Após a chamada ao método, o controle do fluxo da aplicação retorna para o usuário.
c) são de uso exclusivo em processos de desenvolvimento de soluções orientado a objetos, já que os objetos são a mais adequada abstração para o reúso.
d) são aplicações propriamente ditas, normalmente construídas pela integração de diversos frameworks.
e) podem ser modelados utilizando-se a linguagem UML que fornece um meio eficiente de modelar padrões de projeto representando-os como colaborações.
8. (FCC/TRT24-2011) Considere:

I. Fornecer uma interface para criação de famílias de objetos relacionados ou dependentes, sem especificar suas classes concretas. Possibilitar o adiamento da instanciação para as subclasses.
II. Garantir a existência de apenas uma instância de uma classe, mantendo um ponto global de acesso ao seu objeto.
III. Possibilitar o armazenamento do estado interno de um objeto em um determinado momento, para que seja possível retorná-lo a este estado, caso necessário.
I, II e III são, respectivamente, objetivos dos Design Patterns intitulados:

a) Interpreter, Iteratore Memento.

b) Command, Singleton e Iterator.

c) Factory Method, Singleton e Memento.

d) Iterator, Factory Method e Flyweight.

e) Singleton, Flyweight e Command.

9. (FCC / TRE-RN - 2011) Na engenharia de software, os padrões de projetos comportamentais tratam das interações e divisões de responsabilidades entre as classes ou objetos. São exemplos típicos dessa família:
a) Command, Factory Method e Prototype.

b) Builder, Prototype e Singleton.

c) Chain of Responsability, Interpreter e Iterator.

d) Adapter, Bridge e Façade.

e) Abstract Factory, Builder e Composite.

10. (FCC /TRT4-2011) O catálogo de padrões de projeto (Design Patterns) do GoF contém:

a) 20 padrões e está basicamente dividido em duas seções: Structural e Behavioral.

b) 21 padrões e está basicamente dividido em duas seções: Creational e Behavioral.

c) 23 padrões e está basicamente dividido em duas seções: Structural e Behavioral.

d) 23 padrões e está, basicamente, dividido em três seções: Creational, Structural e Behavioral.

11. (FCC / TRT14 - 2011) No contexto dos padrões de projeto:

I. Oferecer uma interface simples para uma coleção de classes.

II. Desacoplar uma abstração de sua implementação para que ambas possam variar independentemente.
Correspondem respectivamente a:

a) Façade e Bridge.

b) Adapter e Façade.

c) Composite e Bridge.

d) Façade e Composite.

e) Bridge e Adapter.

12. (FCC / TRFZj - 2010) Sobre os design patterns, é correto afirmar:

a) Padrões e linguagens de padrões são maneiras de implementarsistemas orientados a objetos por meio da captação da experiência de programadores. Os padrões, apesar de abstratos,sempre incluem algum código de programação.

b) São aplicações, propriamente ditas, dedicadas aos domínios de aplicações específicos,
tais como sistemas de telecomunicações ou financeiros.
c) Não são complexos e necessita-se de um tempo mínimo para aprender a usá-los.

d) O princípio geral de englobamento de experiência em um padrão é aplicável apenas à abordagem de projeto de software orientado a objetos.
e) O padrão é uma descrição de conhecimento e experiência acumulados, uma solução comprovada para um problema comum.
13. (FCC / TJ-PI - 2009) Os padrões de projeto, quando aplicados ao desenvolvimento de aplicações,fornecem meios de descrever soluções comuns para problemas comuns, resultando em redução de tempo gasto com 0 desenvolvimento e melhoria da qualidade da aplicação.
Analise:

I. É o responsável pela especificação dos tipos de objetos a serem criados usando uma
"instância"
prototípica e pela criação de novos objetos copiando este protótipo.

II. Define uma interface de nível mais alto que torna o subsistema mais fácil de usar e fornece uma interface única para um subsistema com diversas interfaces; compõe o grupo de padrões estruturais.
III. Integrante do grupo de padrões comportamentais, ele provê uma forma de acessar sequencialmente os elementos de um agregado de objetos, sem expor a representação interna desse agregado.
IV. As consequências do uso deste padrão é que o encapsulamento é mantido, já que objetos usam sua própria informação para cumprir responsabilidades; leva ao fraco acoplamento entre objetos e à alta coesão, uma vez que objetos fazem tudo que é relacionado à sua própria informação.
As afirmações correspondem, respectivamente, aos padrões a) Command, Iterator, Singleton e Expert.
b) Controller, Expert, Singleton e Prototype.

c) Command, Singleton, Controller e Façade.

d) Prototype, Façade, Iterator e Expert.

e) Adapter, Façade, Command e Iterator.

14. (FCC / Infraero - 2009) As associações entre classes e objetos são tratadas pelos Padrões de
Projeto de Software (Design Patterns) da família de Padrões:

a) GoF Estruturais.

b) GRASP Comportamentais.

c) GRASP Estruturais.

d) GoF de Criação.

e) GoF Comportamentais.

GABARITo

1. LETRA A

2. LETRA C

3. LETRA D

4. LETRA A

5. LETRA D

6. LETRA B

7. LETRA E

8. LETRA C

9. LETRA C

10. LETRA D

11. LETRA A

12. LETRA E

13. LETRA D

14. LETRA A

QUESTõES CoMENTADAS - FC V

í. (FGV / AL-Caruaru - 2015) O catálogo denominado Padrões GoF ('Gang of
Four') define soluções reutilizáveis para problemas frequentes em projetos de sistemas de software.Essas soluções estão organizadas em três famílias conforme o propósito de cada solução. Os padrões de projetos denominados Interpreter, Prototype e Flyweight que fazem parte desse catálogo,pertencem, respectivamente, às seguintes famílias:

a) padrão comportamental, padrão de criação e padrão estrutural.

b) padrão estrutural, padrão comportamental e padrão de criação.

c) padrão comportamental, padrão estrutural e padrão de criação.

d) padrão estrutural, padrão de criação e padrão comportamental.

e) padrão de criação, padrão comportamental e padrão estrutural.

2. (FGV/AL-MA-2013) Com relação ao tema Padrões de Projeto, conforme descritos porGamma et AlIi, sobre o padrão Prototype, analise as afirmativas a seguir.
I. Apresenta como benefícios adicionais a adição e a remoção de produtos em tempo de execução.
II. Apresenta como benefícios adicionais a especificação de novos objetos pela variação de seus valores e/ou de sua estrutura.
III. Apresenta como benefícios adicionais a redução da necessidade de criação de subclasses.

Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente a afirmativa II estiver correta.

c) se somente a afirmativa III estiver correta.

d) se somente as afirmativas I e II estiverem corretas.

e) se todas as afirmativas estiverem corretas.

3. (FGV / Senado Federal - 2008) Considera as seguintes assertivas sobre as vantagens do uso de padrões de software (software patterns):
I. Padrões de projeto proporcionam um vocabulário comum de projeto,
facilitando comunicação, documentação e aprendizado dos sistemas de software.
II. Padrões de projeto auxiliam no desenvolvimento de software por meio da reutilização do projeto de soluções computacionais já testadas e aprovadas.
III. Uma biblioteca de padrões pode ajudar a melhorar e padronizar o desenvolvimento de software.
As assertivas corretas são:

a) somente II.

b) somente I e II.

c) somente I e III.

d) somente II e III.

e) I, lie III.

GABARITo

1. LETRA A

2. LETRA E

3. LETRA E

QUESTõES CoMENTADAS - DIVERSAS BANCAS

í. (IBFC / Prefeitura de Divinópolis-MG - 2018) Os padrões de projetos (Design
Patterns) são compostos basicamente por 4 elementos essenciais que são:
a) Nome do software + Problema a ser resolvido + Solução dada pelo padrão + Tempo de desenvolvimento b) Nome do padrão + Problema a ser resolvido + Solução dada pelo padrão + Consequências c) Nome do software + Problema a ser resolvido + Planejamento das atividades + Consequências d) Nome do padrão + Problema a ser resolvido + Planejamento das atividades + Tempo de desenvolvimento
Comentários:

O template padrão de um padrão de projeto é: (1) Nome do Padrão; (2) Problema a ser resolvido;

(3) Solução dada pelo padrão; (4) Tempo de Desenvolvimento.

Gabarito: Letra B

2. (IBFC / EBSERH - 2017) Os Padrões de Projeto de software são organizados em três famílias conforme a "Gangue dos Quatro" (Gang of Four). Dos "Padrões de Criação" abaixo,identifique qual deles não pertence a essa família especificamente:
(1) Abstract Factory

(2) Builder

(3) Factory Method

(4) Prototype

(5) Proxy a) somente o 1 não pertence a essa família especificamente.
b) somente o 2 não pertence a essa família especificamente.

c) somente o 3 não pertence a essa família especificamente.

d) somente o 4 não pertence a essa família especificamente.

e) somente o 5 não pertence a essa família especificamente.

Comentários:

CriaçJão

Propósito

Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

(i) Abstract Factory é um padrão de criação; (2) Builder é um padrão de criação; (3)
Factory Method é um padrão de criação; (4) Prototype é um padrão de criação; (5) Proxy é um padrão estrutural.
Gabarito: Letra E

3. (IBFC / EBSERH - 2017) Erich Hamma, Richard Helm, Ralph Johson e John Vlissdes,
mais conhecidos como "Gang of Four", coletaram originalmente 23 Design Pattems(Padrões de
Projeto) e organizaram em 3 grupos denominados:

a) Startup Standards (Padrões de Inicialização) - Intermediate Patterns (Padrões
Intermediários)

- Finishing Standards (Padrões de Fiinalização).

b) Interaction patterns (Padrões de Interação) - Beta Standards (Padrões Beta)
- Finishing
Standards (Padrões de Finalização).

c) Creational Patterns (Padrões de Criação) - Structural Patterns (Padrões
Estruturais) -
Behavioral Patterns (Padrões Comportamentais).

d) Users Patterns (Padrões de Usuários) - Creational Patterns (Padrões de Criação) -
Interaction patterns (Padrões de Interação).
e) Alpha Standards (Padrões Alfa) - Beta Standards (Padrões Beta) - Patterns Gamma
(Padrões
Gama).

Comentários:

CriaçJão

Propósito

Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Os tipos de padrão são: Padrões de Criação (Creational Patterns), Padrões Estruturais
(Structural
Patterns) e Padrões Comportamentais (Behavioral Patterns).

Gabarito: Letra C

4. (ESAF / CGU - 2012) O padrão de projeto singleton é usado para restringir:

a) a instanciação de uma classe para objetos simples.

b) a instanciação de uma classe para apenas um objeto.

c) a quantidade de classes.

d) as relações entre classes e objetos.

e) classes de atributos complexos.

Comentários:

SINGLETON Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
Ele restringe a instanciação de uma classe para apenas um objeto ou instância.

Gabarito: Letra B

5. (FEMPERJ /TCE-RJ -2012) Padrões de Projeto descrevem soluções para problemas recorrentes no desenvolvimento de sistemas de software orientados a objetos. Um padrão de projeto estabelece um nome e define o problema, a solução, quando aplicar esta solução e suas consequências. Um dos padrões de projeto mais utilizados é o padrão Adapter(adaptador), que tem como função:
a) garantir a existência de apenas uma instância de uma classe, mantendo um ponto global de acesso ao seu objeto.
b) adicionar dinamicamente um comportamento a um objeto existente sem alterar o código das classes existentes.
c) fornecer uma interface para a criação de famílias de objetos correlatos ou dependentes sem a necessidade de especificar a classe concreta destes objetos.
d) definir novas operações sem alterar as classes dos elementos sobre os quais ele opera.

e) permitir que classes com interfaces incompatíveis possam interagir.

Comentários:

SINGLETON

Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.
(a) Errado, trata-se do Singleton.

Esse padrão anexa responsabilidades adicionais a um objeto dinamicamente. Fornece uma

DECORATOR alternativa flexível em relação à herança para estenderfuncionalidades.

(b) Errado, trata-se do Decorator.

ABSTRACT FACTORY

Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
(c) Errado, trata-se do Abstract Factory.

VISITOR

Esse padrão representa uma operação a ser realizada sobre elementos de uma estrutura objetos e permite definir uma operação sem mudar as classes dos elementos sobre os qu opera.
(d) Errado, trata-se do Visitor.

Esse padrão converte a interface de uma classe em outra interface que normalmente não

ADAPTER poderiam trabalhar juntas por serem incompatíveis.

(e) Correto, trata-se do Adapter.

Gabarito: Letra E

6. (ESAF/ATRFB-2012) OS padrões de projeto (Design Patterns) são classificados nas categorias:

a) Situacional. Estrutural. Complementar.

b) Criacional. Evolutiva. Contingencial.

c) Compartimentai. Vinculada. Comportamental.

d) Criacional. Step-by-step. Orientada a requisitos.

e) Criacional. Estrutural. Comportamental.

Comentários:

Propósito

Criação Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Classifica-se em Criacional, Estrutural ou Comportamental.

Gabarito: Letra E

7. (ESAF/CGU-2008) Ao longo das últimas décadas, a engenharia de software fez progressos significativos no campo de padrões de projeto - arquiteturas comprovadas para construir software orientado a objetos flexível e fácil de manter. Com relação ao padrão Facade,é correto afirmar que:
a) Fornece um objeto representante ou um marcador de outro objeto para controlar o acesso ao mesmo.
b) Define o esqueleto de um algoritmo em uma operação, postergando a definição de alguns passos para subclasses.
c) Define uma interface para criar um objeto, mas deixas as subclasses decidirem qual classe a ser instanciada.
d) Fornece uma interface unificada para um conjunto de interfaces em um sistema.

e) Define uma dependência "um para muitos" entre objetos, de modo que, quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados.
Comentários:

Esse padrão provê um substituto ou ponto através do qual um objeto pode controlar o acesso

PROXY a outro objeto.

(a) Errado. Trata-se do Proxy.

TEMPLATE METHOD

Esse padrão define o esqueleto de um algoritmo dentro de uma operação, deixando alguns passos a serem preenchidos pelas subclasses.
(b) Errado. Trata-se do Template Method.

FACTORYMETHOD

Esse padrão define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.
(c) Errado. Trata-se do Factory Method.

Esse padrão oferece uma interface unificada para um conjunto de interfaces em um

FACADE subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.

(d) Correto. Trata-se do Façade.

OBSERVER

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.
(e) Errado. Trata-se do Observer.

Gabarito: Letra D

8. (ESAF / CGU - 2008) Quanto à finalidade, os padrões de projeto podem ser classificados em padrões de criação, padrões de estutura ou padrões comportamentais. Correspondem à categoria de padrões estruturais:
a) Facade, Prototype e Proxy.

b) Adapter, Composite e Proxy.

c) Adapter, Factory Method e Template Method.

d) Builder, Template Method e Strategy.

e) Adapter, Bridge e Singleton.

Comentários:

Propósito

Criação Estrutura Comportamento

Builder Adapter Chain of Responsibility
Abstract Factory Bridge Command

Prototype Composite Iterator

Singlenton Decorator Mediator

Factory Method Facade
Flyweight

Proxy

Memento
Observer
State
Strategy
Visitor
Interpreter

Template Method

Trata-se do Adapter, Composite e Proxy.

Gabarito: Letra B

9. (ESAF / AFRFB - 2005) Analise as seguintes afirmações relacionadas a padrões de projetos:

I. O padrão Builder separa a construção de um objeto complexo de sua representação,
de modo a que o mesmo processo de construção possa criar diferentes representações.
II. O método Abstract Factory fornece uma interface para a criação de uma família de objetos relacionados ou dependentes sem especificar suas classes completas.
III. O padrão Bridge define uma interface para criar um objeto, mas deixa as subclasses decidirem que classe será instanciada. O Bridge permite a uma classe postergar a instanciação das subclasses.
IV. O Chain of responsability usa compartilhamento para suportar grandes quantidades de objetos e define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados.
Indique a opção que contenha todas as afirmações verdadeiras.

a) I e III.

b) lie III.

c) III e IV.

d) I e II.

e) lie IV.

Comentários:

BUILDER

Esse padrão separa a construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes tipos de representações.
(I) Contrução de um objeto complexo?Trata-se do Builder!

ABSTRACTFACTORY

Esse padrão fornece uma interface para criarfamílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
(II) Interface para a criação de uma família de objetos relacionados? Abstract Factory!
Observem que ele diz completa, em vez de concreta! Nesse contexto, os termos são sinônimos, isto é, a classe concreta é completa, na medida em que contém todas as implementações de seus métodos,por outro lado uma classe abstrata seria incompleta.
FACTORY METHOD

Esse padrão define uma interface para criarum objeto, mas deixa as subclasses decidirem qual classe instanciar.
(III) Interface para criar objeto deixando a decisão para subclasses? Factory Method!

Esse padrão utiliza compartilhamento para suportar eficientemente grandes quantidades de

FLYWEIGHT objetos de baixa granularidade.

OBSERVER

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.
(IV) A questão misturou Flyweight com Observer.

Gabarito: Letra D

GABARITo

1. LETRAB

2. LETRAE

3. LETRAC

4. LETRAB

5. LETRAE

6. LETRAE

7. LETRAD

8. LETRAB

9. LETRAD

GRASP

O GRASP, acrônimo de General Responsability Assignment Software Patterns (ou Principies),
consiste em um conjunto de práticas que descrevem os princípios fundamentais de atribuição de responsabilidade a objetos, expressas na forma de padrões. Ele ajuda a compreender melhor a utilização da orientação a objetos em projetos complexos.
A qualidade de um projeto orientado a objetos está fortemente relacionada à distribuição de responsabilidades, que podem ser divididas em Responsabilidade de Conhecimento(Knowing) e
Responsabilidade de Realização (Doing). A primeira refere-se à distribuição das características do sistema entre as classes e a segunda à distribuição do comportamento do sistema entre as classes.
As Responsabilidades do Tipo Realização são realizadas por um único método ou uma coleção de métodos trabalhando em conjunto. Já as Responsabilidades do Tipo Conhecimento são inferidas a partir do modelo conceituai, i.e., são atributos e relacionamentos. Lembram-se daUML? Pois é,
os Diagramas de Interação são bastante utilizados para representar responsabilidades.

Galera, para ser bem sincero com vocês, eu considero Padrões GRASP mais como uma filosofia de projeto do que como um conjunto de padrão de projeto. Eles descrevem princípios fundamentais de desenho orientado a objetos e definição de responsabilidades,expressos em padrões. Vocês sabem o que significa o verbo To Grasp? Significa tomar,agarrar, apreender,
captar, aferrar, pegar de súbito.

Esse nome foi escolhido com o intuito de sugerir a importância de agarrar ou captar esses princípios para desenhar projetos de software orientados a objetos da melhor forma possível. OsPadrões de Projeto GOF exploram soluções de projeto mais específicas, já os Padrões de Projeto
GRASP refletem práticas mais pontuais da aplicação de técnicas orientadas a objetos.

O Padrão GRASP é composto de cinco Padrões Básicos e quatro Padrões
Avançados. Os
Padrões Básicos são: Information Expert, Creator, High Cohesion, Low Coupling e
Controller. Já os Padrões Avançados são: Polymorphism, Pure Fabrication, Indirection e ProtectedVariations.
Assim como os Padrões de Projeto (GOF), para resolver a grande maioria das questões,
basta conhecer a descrição básica.
\iAC>.

lawTOK

llMP^cnoNl

CoJRJKIÇ FRoTEonet?

/ccNT£òL£<

*

Expert:

Também conhecido como Information Expert, esse padrão é utilizado para determinar para quem delegar as responsabilidades. Essas responsabilidades incluem métodos, campos calculados,etc.
Deve-se atribuir a responsabilidade ao especialista da informação, isto é., a classe que possui a informação necessária para satisfazer essa responsabilidade.
C reator:

A criação de objetos é uma das atividades mais comuns em sistemas orientados a objetos. Esse padrão é responsável por criar objetos de classes, sendo uma propriedade fundamental do relacionamento entre objetos em determinadas classes, i.e., possui a responsabilidade unívoca pela criação de uma nova instância de uma classe.
High Cohesion:

Esse padrão busca manter objetos apropriadamente focados, gerenciáveis e compreensíveis.Geralmente é utilizado para suportar o baixo acoplamento, enfatizando que as responsabilidades de um dado elemento são fortemente relacionadas e altamente focadas. Eu sempre decorei assim:"Coesão é a divisão de responsabilidades".

Low Coupling:

Esse padrão é responsável por ditar como atribuir responsabilidades para apoiar baixa dependência entre classes, como suportar mudanças em uma classe que tenham baixo impacto em outras classes, e maior potencial de reúso. O acoplamento está sempre associado à coesão.Eu sempre decorei assim: "Acoplamento é a dependência entre as partes".

Controller:

Esse padrão tem o objetivo de atribuir a responsabilidade de lidar com eventos de sistema a uma classe que não implemente elementos gráficos, e represente um sistema completo ou um cenário de caso de uso. Um objeto Controller não é uma interface com o usuário, trata-se -na verdade -
de um objeto responsável por receber e tratar eventos do sistema.

Polymorphism:

Esse padrão atribui a responsabilidade de definir a variação de comportamentos baseado em tipos aos tipos em que essas variações ocorrem. Isso ocorre por meio de operações polimórficas. Em outras palavras, não se deve utilizar a lógica condicional para decidir qual comportamento será realizado, mas utilizar os próprios tipos. Galera, é o polimorfismo comum à orientação a objetos.
Pure Fabrication:

Esse padrão apresenta uma classe que não representa um conceito real, mas artificial,
no domínio de problema, sendo utilizada para atingir baixo acoplamento, alta coesão e o potencial reúso. Em outras palavras, ela atribui um conjunto altamente coesivo de responsabilidade a uma classe artificial que não representa um conceito do domínio do problema.
Indirection:

Esse padrão atribui responsabilidade a um objeto intermediário para mediar as mensagens entre outros componentes ou serviços para que não sejam diretamente acoplados. Ele cria uma camada de indireção entre os dois componentes que não mais dependem um do outro,i.e., ambos dependem da indireção. Um exemplo é o Componente Controller no MVC - ele faz a mediação entre Model e View.
Protected Variations:

Esse padrão identifica pontos de variação ou instabilidades potenciais e atribui responsabilidades para criar uma interface estável em volta desses pontos. Dessa forma, ela protege elementos das variações de outros elementos (objetos, sistemas, subsistemas) ao envolver o foco de instabilidade em uma interface e usando o polimorfismo para criar várias implementações desta interface.
QUESTõES CoMENTADAS - CRASP - CEBRASPE

1. (CESPE - 2013 - TCE/RO - Analista de Informática) O padrão Pure Fabrication objetiva designar a responsabilidade unívoca pela criação de uma nova instância de uma classe.
Comentários:

Creator:

A criação de objetos é uma das atividades mais comuns em sistemas orientados a objetos. Esse padrão é responsável por criar objetos de classes, sendo uma propriedade fundamental do relacionamento entre objetos em determinadas classes, i.e., possui a responsabilidade unívoca pela criação de uma nova instância de uma classe.
Conforme vimos em aula, a questão trata do Padrão Creator! Gabarito: E

2. (CESPE - 2013 - TCE/RO - Analista de Informática) Nos casos em que a solução oferecida pelo padrão Expert violar a alta coesão e o baixo acoplamento, o padrão adequado a ser aplicado será o Creator, que atribui um conjunto altamente coesivo de responsabilidades a uma classe artificial que não representa um conceito do domínio do problema.
Comentários:

Pure Fabrication:

Esse padrão apresenta uma classe que não representa um conceito real, mas artificial,
no domínio de problema, sendo utilizada para atingir baixo acoplamento, alta coesão e o potencial reúso. Em outras palavras, ela atribui um conjunto altamente coesivo de responsabilidade a uma classe artificial que não representa um conceito do domínio do problema.
Conforme vimos em aula, a questão trata do Padrão Padrão Pure Fabrication! Gabarito: E

3. (CESPE - 2013 - TCE/RO - Analista de Informática) O padrão Indirection é utilizado para atribuir responsabilidades à classe que tiver a informação necessária para satisfazer a responsabilidade.
Comentários:

Expert:

Também conhecido como Information Expert, esse padrão é utilizado para determinar para quem delegar as responsabilidades. Essas responsabilidades incluem métodos, campos calculados, etc.Deve-se atribuir a responsabilidade ao especialista da informação, isto é., a classe que possui a informação necessária para satisfazer essa responsabilidade.
Conforme vimos em aula, a questão trata do Padrão Expert! Gabarito: E

4. (CESPE - 2013 - TCE/RO - Analista de Informática) O padrão Don't Talk to
Strangers é utilizado para fortalecer o polimorfismo, realizado pelo padrão Polymorphism. O objetivo de ambos os padrões é substituir um componente sem afetar outro componente, embora o primeiro implemente o polimorfismo em nível de classe e o segundo lide com alternativas embasadas no tipo de componente.
Comentários:

Protected Variations:

Esse padrão identifica pontos de variação ou instabilidades potenciais e atribui responsabilidades para criar uma interface estável em volta desses pontos. Dessa forma, ela protege elementos das variações de outros elementos (objetos, sistemas, subsistemas) ao envolver o foco de instabilidade em uma interface e usando o polimorfismo para criar várias implementações desta interface.
Polymorphism:

Esse padrão atribui a responsabilidade de definir a variação de comportamentos baseado em tipos aos tipos em que essas variações ocorrem. Isso ocorre por meio de operações polimórficas. Em outras palavras, não se deve utilizar a lógica condicional para decidir qual comportamento será realizado, mas utilizar os próprios tipos. Galera, é o polimorfismo comum à orientação a objetos.
Galera, além de ser o nome de uma música do grande Ronnie James Dio, Don't Talk to
Strangers é o nome da versão original do Padrão Protected Variations. No entanto,quem lida com alternativas embasadas no tipo de componente é o Padrão Don't Talk to Strangers (ouProtected
Variations). Quem liga com o polimorfismo em nível de classe é o Padrão Polymorphism.
Gabarito:
E

5. (CESPE - 2013 - CNJ - Analista Judiciário - Análise de Sistemas) Os padrões:
Controller;
Polimorfismo; e Information Expert, são considerados do tipo GRASP porque cada um embute uma forma de atribuição de responsabilidades a objetos. No caso do Controller,a responsabilidade é concernente ao tratamento de eventos. No caso do Polimorfismo, a responsabilidade é concernente à variação de comportamento, conforme o tipo do objeto. No caso do Information Expert, a responsabilidade concerne à disponibilidade de informações que permitem o desempenho de uma responsabilidade.
Comentários:

Questão mais perfeita, impossível! Tudo correto! Gabarito: C

6. (CESPE - 2010 - MPU - Desenvolvimento de Sistemas) GRASP (general responsibility assignment software patterns) consiste em um conjunto de sete padrões básicos para atribuir responsabilidades em projeto orientado a objetos: information expert,creator,
controller, low coupling, high cohesion, polymorphism e pure fabrication.

Comentários:

O Padrão GRASP é composto de cinco Padrões Básicos e quatro Padrões Avançados. Os
Padrões
Básicos são: Information Expert, Creator, High Cohesion, Low Coupling e Controller. Já os Padrões

Avançados são: Polymorphism, Pure Fabrication, Indirection e Protected Variations.
Assim como os Padrões de Projeto (GOF), para resolver a grande maioria das questões,basta conhecer a descrição básica.
\^AI> SXs iQoS

\ tx-peKT-

I CRE/VOK

/ LoJ CoJHJMG

PòLyrWH is/^

EM

IN^Í^CTToNI

FfSoFGQreb

— X/VJVM lONl <

.

Conforme vimos em aula, temos cinco padrões básicos! Gabarito: E

7. (CESPE - 2005 - SERPRO - Desenvolvimento de Sistemas) No polimorfismo, que é um tipo de padrão GRASP, um mesmo método pode apresentar várias formas.
Comentários:

Polymorphism:

Esse padrão atribui a responsabilidade de definir a variação de comportamentos baseado em tipos aos tipos em que essas variações ocorrem. Isso ocorre por meio de operações polimórficas. Em outras palavras, não se deve utilizar a lógica condicional para decidir qual comportamento será realizado, mas utilizar os próprios tipos. Galera, é o polimorfismo comum à orientação a objetos.
Conforme vimos em aula, está perfeito! Gabarito: C

8. (CESPE - 2008 - SERPRO - Analista - Desenvolvimento de Sistemas) Expert é um padrão que apresenta uma interface para várias funcionalidades de uma API de maneira simples e fácil de usar.
9.

Comentários:

Bem, essa descrição se aproxima mais do Padrão Protected Variations ou, no caso dos
Padrões de
Projeto GOF, se aproxima mais do Padrão Façade! Gabarito: E

10.(CESPE - 2010 - SERPRO - Analista de Sistemas) Os padrões GRASP (general responsibility assignment software patterns) consistem em modelos de distribuição de responsabilidades a classes e objetos em implementações orientadas a objetos. Os principais exemplos de padrões GRASP são: Information Expert, Creator, Visitor,
Controller, Iterator, Low Coupling, High Cohesion, Polymorphism, State, Strategy,
Pure
Fabrication, Indirection, Proxy e Protected Variations.

Comentários:

\^AI> SXs iQoS

\ tx-peKT- Pbc/MÇXpj-iis^

I CRE/VOK EM

li\fíx"^cnobJ

/ LoJ CoJHJMÇ FfSoFGcrcb

JV

""""

Conforme vimos em aula, não existe Padrão GRASP Visitor, Iterator, State,
Strategy e Proxy -
todos esses são Padrões GOF! Gabarito: E

11 .(CESPE - 2014 - SUFRAMA - Analista de Sistemas) Enquanto os padrões GRASP refletem práticas mais pontuais da aplicação de técnicas orientadas a objetos, os padrões de projeto GoF (Gang of Four) exploram soluções mais específicas. Dessa forma, não há, noGRASP, um padrão que ajude a solucionar, por exemplo, a definição de qual classe deve ser a responsável por lidar com um evento de determinada interface.
Comentários:

Esse nome foi escolhido com o intuito de sugerir a importância de agarrar ou captar esses princípios para desenhar projetos de software orientados a objetos da melhor forma possível. OsPadrões de Projeto GOF exploram soluções de projeto mais específicas, já os Padrões de
Projeto
GRASP refletem práticas mais pontuais da aplicação de técnicas orientadas a objetos.

Controller:

Esse padrão tem o objetivo de atribuir a responsabilidade de lidar com eventos de sistema a uma classe que não implemente elementos gráficos, e represente um sistema completo ou um cenário de caso de uso. Um objeto Controller não é uma interface com o usuário,mas é um objeto responsável por receber e tratar eventos do sistema.
Claro que há! Conforme vimos em aula, trata-se do Padrão Controller. Gabarito: E

12.(CESPE - 2014 - SUFRAMA - Analista de Sistemas) Em um cenário em que é necessário minimizar dependências e maximizar o reúso, bem como atribuir uma responsabilidade para que o acoplamento mantenha-se fraco, o padrão Expert é mais adequado que o padrão Low Coupling.
Comentários:

Low Coupling:

Esse padrão é responsável por ditar como atribuir responsabilidades para apoiar baixa dependência entre classes, como suportar mudanças em uma classe que tenham baixo impacto em outras classes, e maior potencial de reúso. O acoplamento está sempre associado à coesão.Eu sempre decorei assim: "Acoplamento é a dependência entre as partes".

Conforme vimos em aula, o Padrão Low Coupling é o mais adequado! Gabarito: E

13.(CESPE - 2017 - SE/DF - Analista de Sistemas) No padrão GRASP, a alta coesão (high cohesion) serve para mensurar quão fortemente uma classe está conectada a outras classes.
Comentários:

Low Coupling:

Esse padrão é responsável por ditar como atribuir responsabilidades para apoiar baixa dependência entre classes, como suportar mudanças em uma classe que tenham baixo impacto em outras classes, e maior potencial de reúso. O acoplamento está sempre associado à coesão.Eu sempre decorei assim: "Acoplamento é a dependência entre as partes".

Não confundam esses dois padrões! Coesão trata de divisão de responsabilidades e
Acoplamento trata da dependência entre partes/componentes. A questão trata do segudo caso:Acoplamento.
Gabarito: E

LISTA DE QUESTõES - GRASP - MULTIBANCAS

1. (CESPE - 2013 - TCE/RO - Analista de Informática) O padrão Pure Fabrication objetiva designar a responsabilidade unívoca pela criação de uma nova instância de uma classe.
2. (CESPE - 2013 - TCE/RO - Analista de Informática) Nos casos em que a solução oferecida pelo padrão Expert violar a alta coesão e o baixo acoplamento, o padrão adequado a ser aplicado será o Creator, que atribui um conjunto altamente coesivo de responsabilidades a uma classe artificial que não representa um conceito do domínio do problema.
3. (CESPE - 2013 - TCE/RO - Analista de Informática) O padrão Indirection é utilizado para atribuir responsabilidades à classe que tiver a informação necessária para satisfazer a responsabilidade.
4. (CESPE - 2013 - TCE/RO - Analista de Informática) O padrão Don't Talk to
Strangers é utilizado para fortalecer o polimorfismo, realizado pelo padrão Polymorphism. O objetivo de ambos os padrões é substituir um componente sem afetar outro componente, embora o primeiro implemente o polimorfismo em nível de classe e o segundo lide com alternativas embasadas no tipo de componente.
5. (CESPE - 2013 - CNJ - Analista Judiciário - Análise de Sistemas) Os padrões:
Controller;
Polimorfismo; e Information Expert, são considerados do tipo GRASP porque cada um embute uma forma de atribuição de responsabilidades a objetos. No caso do Controller,a responsabilidade é concernente ao tratamento de eventos. No caso do Polimorfismo, a responsabilidade é concernente à variação de comportamento, conforme o tipo do objeto. No caso do Information Expert, a responsabilidade concerne à disponibilidade de informações que permitem o desempenho de uma responsabilidade.
6. (CESPE - 2010 - MPU - Desenvolvimento de Sistemas) GRASP (general responsibility assignment software patterns) consiste em um conjunto de sete padrões básicos para atribuir responsabilidades em projeto orientado a objetos: information expert,creator,
controller, low coupling, high cohesion, polymorphism e pure fabrication.

7. (CESPE - 2005 - SERPRO - Desenvolvimento de Sistemas) No polimorfismo, que é um tipo de padrão GRASP, um mesmo método pode apresentar várias formas.
8. (CESPE - 2008 - SERPRO - Analista - Desenvolvimento de Sistemas) Expert é um padrão que apresenta uma interface para várias funcionalidades de uma API de maneira simples e fácil de usar.
9. (CESPE - 2010 - SERPRO - Analista de Sistemas) Os padrões GRASP (general responsibility assignment software patterns) consistem em modelos de distribuição de responsabilidades a classes e objetos em implementações orientadas a objetos. Os principais exemplos de padrões GRASP são: Information Expert, Creator,Visitor,
Controller, Iterator, Low Coupling, High Cohesion, Polymorphism, State, Strategy,
Pure
Fabrication, Indirection, Proxy e Protected Variations.

10. (CESPE - 2014 - SUFRAMA - Analista de Sistemas) Enquanto os padrões GRASP refletem práticas mais pontuais da aplicação de técnicas orientadas a objetos, os padrões de projeto GoF (Gang of Four) exploram soluções mais específicas. Dessa forma, não há, noGRASP, um padrão que ajude a solucionar, por exemplo, a definição de qual classe deve ser a responsável por lidar com um evento de determinada interface.
11. (CESPE - 2014 - SUFRAMA - Analista de Sistemas) Em um cenário em que é necessário minimizar dependências e maximizar o reúso, bem como atribuir uma responsabilidade para que o acoplamento mantenha-se fraco, o padrão Expert é mais adequado que o padrão Low Coupling.
12. (CESPE - 2017 - SE/DF - Analista de Sistemas) No padrão GRASP, a alta coesão
(high cohesion) serve para mensurar quão fortemente uma classe está conectada a outras classes.
GABARITo

GABARITO

1. E 5. C
9. E

2. E 6. E
10. E

3. E 7. C
11. E

4. E 8. E
12. E

Conceitos Básicos

PRINCÍPIoS SOLID

PrinCípios SOLID

Trata-se de um conjunto de princípios de design criados para tornar o software mais fácil de manter, entender, sustentar, escalar e estender por meio do desenvolvimento de classes fracamente acopladas. Os cinco princípios são: Princípio de Responsabilidade Única, PrincípioAberto-Fechado, Princípio de Substituição de Liskov, Princípio de Segregação de Interface e
Princípio de Inversão de Dependência.

Escrever um código que satisfaça os requisitos atuais, e que também possa satisfazer requisitos futuros facilmente, deve ser o objetivo de qualquer desenvolvedor-evoluir com o tempo é o único fator que pode manter o código-fonte. Princípios SOLID são cinco princípios de design de código orientado a objeto para tornar o código mais entendível, claro, flexível,conciso e tolerante a mudanças; e para aumentar a adesão do código aos princípios da orientação a objetos.
SOLID é um acrônimo para cada um dos cinco princípios que fazem parte desse grupo:

Single Responsability Principie;

Open/Closed Principie

Liskov Substitution Principie

Interface Segregation Principie

Dependency Inversion Principie

Esses cinco princípios de desenvolvimento de software são diretrizes a serem seguidas ao criar software para facilitar o dimensionamento e a manutenção. Veja bem, alguns desses princípios podem parecer semelhantes, mas não visam o mesmo objetivo. Para simplificar o acompanhamento, usarei a palavra "Classe", mas observe que ela também pode se aplicar a uma função, método ou módulo.
Responsabilidade Única

I am a chef,
a gardener,
a painter

& driver

I am a gardener
I am a painter
X Single Responsibility

UMA CLASSE DEVER TER UMA ÚNICA RESPONSABILIDADE

Se uma classe tiver muitas responsabilidades, aumenta a probabilidade de ocorrerem bugs,
uma vez que alterar uma de suas responsabilidades pode afetar as outras sem que você saiba. Para resolver esse problema, temos o Princípio da Responsabilidade Única. O objetivo desse princípio é separar comportamentos para que, se surgirem bugs como resultado de sua alteração, isso não afete outros comportamentos não relacionados.
Na imagem, temos um robô que tem muitas responsabilidades: ele é chef,
jardineiro, pintor e motorista - o ideal é que tivéssemos um robô para cada uma dessas responsabilidades.
Aberto-Fechado

CLASSES DEVEM SER ABERTAS PARA EXTENSÃO, MAS FECHADAS PARA MODIFICAÇÃO

Alterar o comportamento atual de uma classe afetará todos os sistemas que usam essa classe. Se você deseja que a classe execute mais funções, a abordagem ideal é adicionar às funções que já existem e, não, alterá-las. Aberto para extensão significa que, ao receber uma nova requisição, é possível adicionar um novo comportamento. Fechado para modificação significa que, para introduzir um novo comportamento (extensão), não é necessário modificar o código existente.
O objetivo desse princípio é estender o comportamento de uma classe sem alterar o comportamento existente dela. Isso evita a ocorrência de bugs onde quer que a classe esteja sendo usada. Na imagem à esquerda, observem que tínhamos um robô que cortava,teve seu comportamento modificado e que agora passou a pintar; na imagem à direita, tínhamos um robô que cortava, foi estendido e agora aprendeu também a pintar.
Substituição de Liskov

Hi, Tm Sam.
I make coffee i i
<

Hey Eden, Sam is not here ríght now.Can you make me coffee?
X Liskov Substitution

SE S É UM SUBTIPO DE T, ENTÃO OBJETOS DO TIPO T EM UM PROGRAMA PODEM SER SUBSTITUÍDOS
POR OBJETOS DO TIPO S SEM ALTERAR AS PROPRIEDADES DESEJÁVEIS DESSE PROGRAMA

Quando uma classe-filha não pode executar as mesmas ações que sua classe-pai, isso pode causar bugs. Se você tiver uma classe e criar outra classe a partir dela, ela se tornará pai e a nova classe se tornará filha. A classe-filha deve ser capaz de fazer tudo o que a classe-pai pode fazer. Este processo é chamado de Herança. A classe-filha deve ser capaz de processar as mesmas solicitações e entregar o mesmo resultado que a classe-pai ou pode entregar um resultado do mesmo tipo.
O objetivo desse princípio é reforçara consistência para que a classe-pai ou sua classe-filha possam ser usadas da mesma maneira sem erros. A imagem à esquerda mostra que a classe-pai entrega café (pode ser qualquer tipo de café). É aceitável que a classe-filha entregue cappuccino por ser um tipo específico de café, mas não é aceitável entregar água. Se a classe-filha não atender a esses requisitos, isso significa que a classe-filha foi alterada completamente e viola esse princípio.
Já a imagem à direita mostra que Eden (que é filho de Sam) também faz café
(cappuccino), já que ele pode executar as mesmas ações que sua classe-pai (Sam).
Segregação de Interface

X Interface Segregation

CLIENTES NÃO DEVEM SER FORÇADOS A DEPENDER DE MÉTODOS QUE NÃO UTILIZAM

Quando uma classe é obrigada a executar ações que não são úteis, trata-se de um desperdício e pode produzir bugs inesperados se a classe não tiver a capacidade de executar essas ações. Uma classe deve executar apenas as ações necessárias para cumprir seu papel. Qualquer outra ação deve ser removida completamente ou movida para outro lugar se puder ser utilizada por outra classe no futuro. Entendido?
O objetivo desse princípio é dividir um conjunto de ações em conjuntos menores para que uma classe execute apenas o conjunto de ações de que necessita. Na imagem à esquerda,temos dois robôs: um com antena e outro sem antena. E todos os robôs possuem três ações: girar,rodar os braços e balançaras antenas. Ora, se o segundo robô não possui antena, como ele conseguirá executar a terceira função? Ele não conseguirá, logo essa ação é inútil!
Já na imagem à direita, também temos dois robôs: um com antena e outro sem antena.
No entanto,
temos uma divisão de ações: ações para robôs que podem girar; ações para robôs que podem rodar os braços; e ações para robôs que podem balançar as antenas. Logo, nenhum robô possui uma função inútil que não podem executar e que são apenas um desperdício capaz de produzir bugs inesperados. Bacana?
Inversão de Dependência

I cut pizza with any tool given to me
-------------------

X Dependency Inversion

MÓDULOS DE ALTO NÍVEL NÃO DEVEM DEPENDER DE MÓDULOS DE BAIXO NÍVEL: AMBOS DEVEM
DEPENDER DA ABSTRAÇÃO.

AS ABSTRAÇÕES NÃO DEVEM DEPENDER DE DETALHES: DETALHES DEVEM DEPENDER DE
ABSTRAÇÕES.

Em primeiro lugar, vamos definir os termos usados aqui de forma mais simples:

Módulo/Classe de Alto Nível: classe que executa uma ação com uma ferramenta;

Módulo/Classe de Baixo Nível: ferramenta necessária para executar uma ação;

Abstração: representa uma interface que conecta as duas classes;

Detalhes: como a ferramenta funciona .

Este princípio diz que uma classe não deve serfundida com a ferramenta que usa para executar uma ação. Em vez disso, ele deve ser fundido à interface que permitirá que a ferramenta se conecte à classe. Também diz que tanto a classe quanto a interface não devem saber como a ferramenta funciona. No entanto, a ferramenta precisa atender à especificação da interface. Oobjetivo desse princípio é reduzira dependência de uma classe de alto nível na classe de baixo nível, introduzindo uma interface.
Na imagem à esquerda, temos um robô que possui um braço exclusivamente para cortar pizzas; já na imagem à direita, temos um robô que possui um braço que pode ser adaptado para diversas ações - inclusive cortar pizza. Note que eu posso adaptar uma outra ferramenta no braço do robô para que ele possa realizar outra ação. Logo, temos uma inversão: as classes de alto nível deixam de depender das classes de baixo nível e passam a depender apenas da abstração (interface).
Para finalizar, vamos falar um pouquinho sobre coesão e acoplamento. A
implementação de qualquer classe deve ser coesa, isto é, toda classe deve implementar uma única funcionalidade ou serviço. Especificamente, todos os métodos e atributos de uma classe devem estar voltados para a implementação do mesmo serviço. Uma outra forma de explicar coesão é afirmando que toda classe deve ter uma única responsabilidade no sistema.
Dito de outra forma, deve existir um único motivo para modificar uma classe. Ok? Bem,
a coesão tem algumas vantagens: facilita a implementação de uma classe, bem como o seu entendimento e manutenção; facilita a alocação de um único responsável por manter uma classe; e facilita o reuso e teste de uma classe, pois é mais simples reusar e testar uma classe coesa do que uma classe com várias responsabilidades.
Já o acoplamento é a força da conexão entre duas classes. Trata-se da medida em que as partes de um programa estão interconectadas entre si. Pode-se dizer que se refere à quantidade de dependência entre os elementos de um programa. Quanto menor o acoplamento, melhor será a reutilização de código e a manutenção do programa. Na tabela seguinte, veremos um conjunto de propriedades de projeto relacionadas a cada um dos princípios:
PRINCÍPIOS SoLID DESCRIÇÃO
PROPRIEDADES

Uma classe deve ter um, e somente um, motivo para mudar.

Objetos ou entidades devem estar abertos para extensão, mas fechados para modificação.
Uma classe derivada deve ser substituível por sua classe base.

Uma classe não deve serforçada a implementar interfaces e métodos que não irá utilizar.
Dependa de abstrações e, não, de implementações.

Coesão

Extensibilidade

Extensibilidade

Coesão

Acoplamento í. (FGV/ Senado Federal -2022) Os princípios de Orientação a Objetos e Design deCódigo são guiados pelos conceitos do acrônimo SOLID, em que cada letra descreve um princípio.Assinale a opção que indica o princípio que tem a preocupação com a falta de coesão e alto acoplamento:
a) Princípio da Substituição de Liskov.

b) Princípio da Segregação de Interface.

c) Princípio Aberto-fechado.

d) Princípio da Responsabilidade Única.

e) Princípio da Inversão de Dependência.

Comentários:

Estamos em busca do princípio que se preocupa com a falta de coesão e com o alto acoplamento.A falta de coesão indica que uma classe tem mais de uma atribuição, quando deveria ter apenas uma; o alto acoplamento indica que uma classe depende bastante de outras classes. Qual é 0princípio que busca inibir a falta de coesão? Responsabilidade Única e Segregação de
Interface.
Qual é a 0 princípio que busca inibir o alto acoplamento? Inversão de Dependência.
Logo, temos três respostas corretas e, por essa razão, a questão foi anulada.
Gabarito: Anulada

2. (CESPE / BANRISUL - 2022) Os princípios de programação orientada a objetos que correspondem aos princípios SOLID são: criador (creator), especialista na informação(information expert), controlador (controller), polimorfismo (polymorphism), fabricação pura(pure fabrication).

Comentários:

Os Princípios SOLID são:

[S] - Single Responsiblity Principie (Princípio da Responsabilidade Única)

[0] - Open-Closed Principie (Princípio Aberto-Fechado)

[L] - LiskovSubstitution Principie (Princípio da Substituição de Liskov)

[I] - Interface Segregation Principie (Princípio da Segregação da Interface)

[D] -Dependency Inversion Principie (Princípio da Inversão da Dependência)

Gabarito: Errado

0 0

www- estratégia concursos. com.br

3- (AOCP / PRODEB - 2018) Com base no modelo SOLID utilizado como referência para padrões de projeto e princípios arquiteturais, um dos seus princípios denominados de LSP(Liskov Substitution Principie) diz respeito ao fato de que:

a) uma classe deve ter apenas uma razão para mudar, sendo coesa.

b) os objetos devem ser substituíveis com instâncias de seus tipos base, sem prejudicar o funcionamento do software.
c) todo o processo de desenvolvimento de software deve ser baseado em abstrações, já que elas pouco mudam.
d) deve-se utilizar o conceito de herança o máximo possível, estendendo para todo e qualquer atributo que possua alguma semelhança.
e) os módulos devem ser enxutos tendo poucos comportamentos.

Comentários:

(a) Errado, isso é o Princípio de Responsabilidade Única; (b) Correto; (c) Errado,
isso é o Princípio de Inversão de Dependência; (d) Errado, deve-se evitar herança o máximo possível para evitar o acoplamento e devemos priorizara composição ou interface; (e) Errado, essa descrição não está relacionada ao LSP.
Gabarito: Letra B

4. (AOCP / PRODEB - 2018) Em relação aos padrões de projeto de software e princípios arquiteturais, em programação orientada a objetos, existe um princípio denominado deSOLID. Ele, por sua vez, é composto por 05 princípios de acordo com as suas iniciais, sendo eles:
a) S (Single responsibility principie) - O (Openclosed principie) - L
(Liskov substitution principie) -1 (Interface segregation principie) e D (Dependency inversion principie).
b) S (Solid principie) - O (Open principie) - L (Library principie) -1 (Integration principie) - D(Double principie).

c) S (Security closed principie) - O (Open extend principie) - L (Liskov include principie) - I(Interface duplication principie) - D (Duplicate structure principie).

d) S (Single closed principie) - O (Open-closed principie) - L (Library exclusive principie) - I(Integration case principie) - D (Dependency inversion principie).

e) S (Security basic principie) - O (Open extern principie) - L (Liskov include principie) - I(Interface duplication principie) - D (Duplicate segregation principie).

Comentários:

Ele é composto por 05 princípios de acordo com as suas iniciais, sendo eles:

[S] - Single Responsiblity Principie (Princípio da Responsabilidade Única)

[0] - Open-Closed Principie (Princípio Aberto-Fechado)

[L] -LiskovSubstitution Principie (Princípio da Substituição de Liskov)

[I] - Interface Segregation Principie (Princípio da Segregação da Interface)

[D] -Dependency Inversion Principie (Princípio da Inversão da Dependência)

Gabarito: Letra A

5. (CESPE / BANRISUL - 2022) O princípio da segregação de interface dos padrões SOLID
define que uma classe deve possuir somente uma operação para ser executada.

Comentários:

Na verdade, a descrição trata do Princípio da Responsabilidade Única. O Princípio da
Segregação de Interface define que uma classe não deve serforçada a implementar interfaces e métodos que não irá utilizar.
Gabarito: Errado

6. (FUNDEP / UFJF - 2022) No contexto dos princípios SOLID, analise as afirmativas a seguir.

I. O princípio de inversão de dependência estabelece que uma classe deve depender de implementações abstratas e não concretas, sempre que possível.
II. O princípio aberto/fechado estabelece que uma classe deve estarfechada para extensões,mas aberta para modificações.

III. O princípio da responsabilidade única é uma aplicação da propriedade de coesão,
por propor que toda classe deve ter uma única finalidade.
Está(ão) correta(s) a(s) afirmativa(s):

a) I, apenas.

b) II, apenas.

c) III, apenas.

d) I e III, apenas.

e) II e III, apenas.

Comentários:

(I) Correto; (II) Errado, ele estabelece que uma classe deve estar aberta para extensões, mas fechada para modificações - a questão inverteu os conceitos; (III) Correto.
7- (FCC / TRE-PR - 2017) Os princípios SOLID reúnem cinco boas práticas para projetosOrientados a Objetos-OO. O princípio S, que se refere ao Single Responsability
Principle-SRP
ou Princípio de Responsabilidade Única, indica que uma classe deve ter uma e, apenas uma,razão para mudar. Considere a classe Java abaixo.

public class UrnaEleitoral {

public void AdicionarCandidato(String nome, int numero, int partido) { }
public decimal CalcularTotalVotosCandidato() { }

public void CadastrarPartidos() { }
public void CadastrarEleitores() { }
public void CadastrarMesarios() { }

}

Com base no princípio SRP e nas boas práticas para projetos 00, é correto afirmar:

a) O SRP visa aumentar o acoplamento entre classes e separar responsabilidades como forma de melhorar o código da aplicação 00 sendo desenvolvida.
b) A classe UrnaEleitoral tem acoplamento baixo, ou seja, tem um número pequeno de dependências e, portanto, fica mais sujeita a mudanças em decorrência de alterações em outras classes.
c) Uma classe com mais de um motivo para mudar possui mais de uma responsabilidade e apresentando dificuldade de manutenção, mas, poroutro lado, tem maiorfacilidade de reúso e de coesão.
d) A classe UrnaEleitoral apresenta uma quebra do SRP, uma vez que possui responsabilidades que deveriam ser de componentes distintos do software.
e) Em um projeto com várias classes seguindo o padrão da classe UrnaEleitoral fica mais fácil manter a coesão em um nível mais alto ou em nível de componentes, poiso software fica com uma divisão clara de camadas.
Comentários:

(a) Errado, ele visa reduzir o acoplamento entre classes; (b) Errado, é possível notar que há vários métodos relativos a domínios diferentes de urna, tais como Candidato, Partidos,Eleitores e
Mesários. Logo, ela tem muitas dependências, portanto alto acoplamento; (c)
Errado, se ela possui mais de uma responsabilidade, ela tem menos facilidade de reúso e menor coesão;(d)
Correto, note que ela tem cinco métodos, portanto tem cinco responsabilidades diferentes -quando deveria ter apenas uma; (e) Errado, fica mais difícil de manter visto que ela tem diversas responsabilidades.
Gabarito: Letra D

8. (IESES / CREA-SC - 2017) Assinale a alternativa correta:

a) SOLID é um acróstico e, cada letra está relacionada a um princípio para programação e design orientado a objetos de autoria de Robert C. Martin. O Acrostico é formado pela inicial de Sistema, Objeto, Lógica, Informação e, Disign.
b) SOLID é um acróstico e, cada letra está relacionada a um princípio para programação e design orientado a objetos de autoria de Robert C. Martin.
c) SOLID é um acróstico formado pelas iniciais de SPR, OCP, LSP, ISP e DIP. É um conjunto consistente de princípios para modelagem matemática e computacional de sólidos tridimensionais. A modelagem sólida distingue-se das áreas relacionadas de modelagem geométrica e computação gráfica por sua ênfase na fidelidade física.
d) Em programação Orientada a Objetos é um conjunto consistente de princípios para modelagem matemática e computacional de sólidos tridimensionais. A modelagem sólida distingue-se das áreas relacionadas de modelagem geométrica e computação gráfica por sua ênfase na fidelidade física.
Comentários:

Em primeiro lugar, um acróstico é uma palavra formada pelas primeiras letras de cada linha conforme podemos ver a seguir:
[S] - Single Responsiblity Principie (Princípio da Responsabilidade Única)

[0] - Open-Closed Principie (Princípio Aberto-Fechado)

[L] -LiskovSubstitution Principie (Princípio da Substituição de Liskov)

[I] - Interface Segregation Principie (Princípio da Segregação da Interface)

[D] -Dependency Inversion Principie (Princípio da Inversão da Dependência)

(a) Errado, ele é formado pela inicial de Single, Open, Liskov, Interface e
Dependency; (b)
Correto; (c) Errado, não tem nenhuma relação com modelagem matemática e computacional de sólidos tridimensionais; (d) Errado, não tem nenhuma relação com modelagem matemática e computacional de sólidos tridimensionais.
Gabarito: Letra B

LISTA DE QUESTõES

í. (FGV/ Senado Federal -2022) Os princípios de Orientação a Objetos e Design de
Código são guiados pelos conceitos do acrônimo SOLID, em que cada letra descreve um princípio.Assinale a opção que indica o princípio que tem a preocupação com a falta de coesão e alto acoplamento:
a) Princípio da Substituição de Liskov.

b) Princípio da Segregação de Interface.

c) Princípio Aberto-fechado.

d) Princípio da Responsabilidade Única.

e) Princípio da Inversão de Dependência.

2. (CESPE / BANRISUL - 2022) Os princípios de programação orientada a objetos que correspondem aos princípios SOLID são: criador (creator), especialista na informação(information expert), controlador (controller), polimorfismo (polymorphism), fabricação pura(pure fabrication).

3. (AOCP / PRODEB - 2018) Com base no modelo SOLID utilizado como referência para padrões de projeto e princípios arquiteturais, um dos seus princípios denominados de LSP(Liskov Substitution Principie) diz respeito ao fato de que:

a) uma classe deve ter apenas uma razão para mudar, sendo coesa.

b) os objetos devem ser substituíveis com instâncias de seus tipos base, sem prejudicar o funcionamento do software.
c) todo o processo de desenvolvimento de software deve ser baseado em abstrações, já que elas pouco mudam.
d) deve-se utilizar o conceito de herança o máximo possível, estendendo para todo e qualquer atributo que possua alguma semelhança.
e) os módulos devem ser enxutos tendo poucos comportamentos.

4. (AOCP / PRODEB - 2018) Em relação aos padrões de projeto de software e princípios arquiteturais, em programação orientada a objetos, existe um princípio denominado deSOLID. Ele, por sua vez, é composto por 05 princípios de acordo com as suas iniciais, sendo eles:
a) S (Single responsibility principie) - O (Openclosed principie) - L
(Liskov substitution principie) -1 (Interface segregation principie) e D (Dependency inversion principie).
b) S (Solid principie) - O (Open principie) - L (Library principie) -1 (Integration principie) - D(Double principie).

c) S (Security closed principie) - O (Open extend principie) - L (Liskov include principie) - I(Interface duplication principie) - D (Duplicate structure principie).

d) S (Single closed principie) - O (Open-closed principie) - L (Library exclusive principie) - I(Integration case principie) - D (Dependency inversion principie).

e) S (Security basic principie) - O (Open extern principie) - L (Liskov include principie) - I(Interface duplication principie) - D (Duplicate segregation principie).

5. (CESPE / BANRISUL - 2022) O princípio da segregação de interface dos padrões
SOLID
define que uma classe deve possuir somente uma operação para ser executada.

6. (FUNDEP / UFJF - 2022) No contexto dos princípios SOLID, analise as afirmativas a seguir.

I. O princípio de inversão de dependência estabelece que uma classe deve depender de implementações abstratas e não concretas, sempre que possível.
II. O princípio aberto/fechado estabelece que uma classe deve estarfechada para extensões,mas aberta para modificações.

III. O princípio da responsabilidade única é uma aplicação da propriedade de coesão,
por propor que toda classe deve ter uma única finalidade.
Está(ão) correta(s) a(s) afirmativa(s):

a) I, apenas.

b) II, apenas.

c) III, apenas.

d) I e III, apenas.

e) II e III, apenas.

7. (FCC / TRE-PR - 2017) Os princípios SOLID reúnem cinco boas práticas para projetosOrientados a Objetos-OO. O princípio S, que se refere ao Single Responsability
Principle-SRP
ou Princípio de Responsabilidade Única, indica que uma classe deve ter uma e, apenas uma,razão para mudar. Considere a classe Java abaixo.

public class UrnaEleitoral {

public void AdicionarCandidato(String nome, int numero, int partido) { }
public decimal CalcularTotalVotosCandidato() { }

public void CadastrarPartidos() { }
public void CadastrarEleitores() { }
public void CadastrarMesarios() { }

}

Com base no princípio SRP e nas boas práticas para projetos 00, é correto afirmar:

a) O SRP visa aumentar o acoplamento entre classes e separar responsabilidades como forma de melhorar o código da aplicação 00 sendo desenvolvida.
b) A classe UrnaEleitoral tem acoplamento baixo, ou seja, tem um número pequeno de dependências e, portanto, fica mais sujeita a mudanças em decorrência de alterações em outras classes.
c) Uma classe com mais de um motivo para mudar possui mais de uma responsabilidade e apresentando dificuldade de manutenção, mas, por outro lado, tem maiorfacilidade de reúso e de coesão.
d) A classe UrnaEleitoral apresenta uma quebra do SRP, uma vez que possui responsabilidades que deveriam ser de componentes distintos do software.
e) Em um projeto com várias classes seguindo o padrão da classe UrnaEleitoral fica mais fácil manter a coesão em um nível mais alto ou em nível de componentes, poiso software fica com uma divisão clara de camadas.
8. (IESES / CREA-SC - 2017) Assinale a alternativa correta:

a) SOLID é um acróstico e, cada letra está relacionada a um princípio para programação e design orientado a objetos de autoria de Robert C. Martin. O Acrostico é formado pela inicial de Sistema, Objeto, Lógica, Informação e, Disign.
b) SOLID é um acróstico e, cada letra está relacionada a um princípio para programação e design orientado a objetos de autoria de Robert C. Martin.
c) SOLID é um acróstico formado pelas iniciais de SPR, OCP, LSP, ISP e DIP. É um conjunto consistente de princípios para modelagem matemática e computacional de sólidos tridimensionais. A modelagem sólida distingue-se das áreas relacionadas de modelagem geométrica e computação gráfica por sua ênfase na fidelidade física.
d) Em programação Orientada a Objetos é um conjunto consistente de princípios para modelagem matemática e computacional de sólidos tridimensionais. A modelagem sólida distingue-se das áreas relacionadas de modelagem geométrica e computação gráfica por sua ênfase na fidelidade física.
GABARITo

1. ANULADA

2. ERRADO

3. LETRA B

4. LETRA A

5. ERRADO

6. LETRA D

7. LETRA D

8. LETRA B

