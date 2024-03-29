# Engenharia de Software e Sistemas - Padrões de Projeto

Pessoal, vamos iniciar pelo básico! O que é um Padrão? É um modelo testado ou documentado para se alcançar um determinado objetivo. O autor Christopher Alexander afirma que cada padrão descreve um problema que ocorre repetidas vezes em nosso ambiente e o núcleo de sua solução, de tal forma que ela pode ser usada diversas vezes sem que seja realizada da mesma maneira. E o que seriam Padrões de Projeto (do inglês, Design Patterns)?
Respondo: são descrições de objetos que se comunicam e classes que são customizadas para resolver um problema genérico em um contexto específico. Esses padrões nomeiam, abstraem e identificam aspectos comuns em uma estrutura e os torna úteis para que sejam realizados. Como é isso, professor? Suponham que haja uma fábrica de software que desenvolve diversos sistemas para as mais variadas áreas de negócio.

Sabe-se que, mesmo em áreas aparentemente distintas ou contrastantes, grande parte dos problemas já possuem uma solução conhecida, formalmente documentada e exaustivamente testada, uma vez que se tratam de problemas recorrentes. Portanto, não há necessidade de se resolver o problema do início se já existe uma solução adequada. Assim sendo, os padrões de projeto são modelos para solucionar problemas gerais de projeto em um contexto particular.
Poxa, professor... o engenheiro de software que inventou isso era genial, né?! Qual é, pessoal! Mais uma vez, nós "roubamos" isso de outras engenharias. Em meados de 1977, um sujeito chamado Christopher Alexander (arquiteto, matemático e urbanista austríaco) estudava como melhorar o projeto de edifícios. Ao se cansar de observar repetidos problemas, ele lançou um manifesto com o registro de diversos padrões de projeto recorrentes na engenharia civil.

Esse manifesto continha algumas regras e figuras que descreviam métodos para a construção de projetos práticos, seguros e atrativos em quaisquer escalas, desde regiões inteiras a cidades, vizinhanças, jardins, edifícios, salas, entre outros. Cada padrão foi testado no mundo real, sendo revisado por diversos arquitetos e engenheiros. Alexander fez uma importante declaração a respeito de padrões de projeto de arquitetura:
"Cada padrão descreve um problema que ocorre repetidas vezes em nosso ambiente e, então, descreve o núcleo da solução para aquele problema, de tal maneira que pode-se usar essa solução milhões de vezes sem nunca fazê-la da mesma forma duas vezes".
Bem, isso chamou a atenção de programadores que estavam de saco cheio de ter que refazer várias partes do código para cada projeto. Foi então que, em 1994, quatro engenheiros de software, conhecidos como The Gang of Four (GoF), resolveram compilar um conjunto de bibliotecas de soluções para problemas comuns de codificação e lançaram um livro clássico com 23 Padrões de Projeto de Software.

Esse livro se tornou um clássico best-seller da literatura orientada a objetos e é recomendado na nossa bibliografia, não obstante ser de leitura extremamente técnica. Concernente aos padrões de projeto, os autores desse livro dizem: "São descrições de objetos que se comunicam e classes que são customizadas para resolver um problema genérico de design em um contexto específico". Professor, que contexto específico é esse? Bem, o contexto é inerente a área de negócio!
Cada um adapta o padrão genérico ao seu ambiente específico para resolver um mesmo problema. Os padrões de projeto abstraem e identificam os aspectos-chave de uma estrutura de projeto comum para torná-la reutilizável. Entre as vantagens dos padrões de projeto, podemos mencionar que é possível aprender com a experiência de outros, identificando problemas comuns de engenharia de software e utilizando soluções testadas e bem documentadas.

É possível utilizar soluções com nomes que facilitam a comunicação, compreensão e documentação. Eles facilitam o reúso de soluções arquiteturais bem-sucedidas e permitem desenvolver softwares de melhor qualidade. Padrões capturam a estrutura estática e a colaboração dinâmica entre objetos participantes no projeto de sistemas. Eles utilizam conceitos de orientação a objetos para construir código reutilizável, eficiente, de alta coesão e baixo acoplamento.

Então há apenas benefícios em se utilizar padrões de projetos? Claro que não! Muitas vezes, as tentativas de se escrever um código que esteja em conformidade com um determinado padrão de projeto aumentam desnecessariamente a complexidade do código. Em outras palavras, a tentativa de simplificar pode acabar complicando a implementação. Ademais, estudos mostram que grande parte dos padrões podem ser simplificados ou eliminados. Como, professor? utilizando-se recursos diretos das próprias linguagens de programação, como em LISP e DYLAN. Portanto, os Design Patterns podem ser simplesmente um indicativo de que algumas linguagens de programação falham em oferecer determinadas características. Cada padrão de projeto é organizado segundo quatro elementos: Nome, Problema, Solução e
Consequências. Nome simplesmente identifica o padrão; Problema descreve a condição em que ele deve ser aplicado; Solução descreve como resolvê-lo; e Consequência descreve os impactos.

Por fim, algumas observações importantes! Esses 23 Design Patterns somente podem ser utilizados em projetos de tecnologia da informação? Claro, eles são padrões de projeto de software. Esses 23 Design Patterns somente podem ser utilizados em projetos orientados a objetos? Sim, também. Pessoal, Padrões GOF somente com Orientação a Objetos! Padrões de Projeto, em geral, podem usar qualquer paradigma ou linguagem!
Os 23 Padrões de Projeto podem ser classificados quanto aos seus propósitos em três tipos: Padrões Criacionais, Padrões Estruturais e Padrões Comportamentais. Infelizmente, vocês têm que decorar como se classificam todos os padrões de projeto. A tabela acima apresenta todos os padrões de acordo com seus respectivos propósitos. Os Padrões Criacionais abstraem o processo de criação de objetos a partir da instanciação de classes.

Já os Padrões Estruturais tratam da forma como classes e objetos estão organizados para formar estruturas maiores. Por fim, Padrões Comportamentais se preocupam com os algoritmos e responsabilidades dos objetos, que ocorrem em tempo de execução.
Explicação: A fábrica (Factory Method) abstrata (Abstract Factory) constrói (Builder) um protótipo (Prototype) único (Singleton). A ponte (Bridge) adaptada (Adapter) é composta (Composite) de decorações (Decorator) na fachada (Façade) para o peso-mosca (Flyweight) se aproximar (Proxy). E não tem frase para o último? Não, porque não é necessária! Se não é um padrão criacional ou estrutural, é um padrão comportamental.
Vamos dar uma olhada em cada um deles:

Galera, vou ser bem sincero com vocês: esse assunto é muuuuuuuuuuuuito chato - e também é muito decoreba! Então, vou explicar o que eu recomendo para o estudo dessa aula - fiz uma análise estatístico rápida e cheguei a algumas conclusões! Primeiro de tudo, decore as frases porque cerca de 15% das questões de prova exigem apenas saber qual Padrão de Projeto GOF pertence a qual categoria.
Vocês matam 15% das questões apenas decorando aquelas duas frases, certinho? Segundo, se você estiver sem tempo, ignore a categoria comportamental, visto a distribuição de questões segue a tabela mostrada acima - e ela é a que tem mais padrões. Por fim, dos 23 Padrões de Projeto, seis correspondem à 55% das questões de prova (dos 85% restantes, isto é, sem as questões de categorias). São eles, em ordem:

1. Adapter

2. Singleton

3. Façade

4. Abstract Factory

5. Iterator

6. Bridge

Pessoal, se vocês estiverem com o tempo muito apertado, estudem apenas esses acima! Do mesmo modo, podemos afirmar que, dos 23 Padrões de Projeto, onze correspondem à 15% das questões de prova: Decorator, Flyweight, Proxy, Chain of Responsability, Interpreter, Mediator, Memento, State, Strategy e Template Method. Os seis padrões restantes, estão no meio termo e correspondem a 30% das questões de prova.

FALOU EM.

Criar famílias de objetos relacionados...

PROVAVELMENTE SERÁ.

ABSTRACT FACTORY.

FALOU EM.

Construção de um objeto complexo com diferentes representações...

PROVAVELMENTE SERÁ.

BUILDER.

FALOU EM.

Deixar subclasses decidirem...

PROVAVELMENTE SERÁ.

FACTORY METHOD.

FALOU EM.

Criar uma instância prototípica...

PROVAVELMENTE SERÁ.

PROTOTYPE.

FALOU EM.

Apenas uma instância com um ponto global a ela...

PROVAVELMENTE SERÁ.

SINGLETON.

FALOU EM.

Converte uma interface em outra, por serem incompatíveis...

PROVAVELMENTE SERÁ.

ADAPTER.

FALOU EM.

Desacoplar interface da implementação...

PROVAVELMENTE SERÁ.

BRIDGE.

FALOU EM.

Estruturas de árvore em hierarquia parte-todo...

PROVAVELMENTE SERÁ.

COMPOSITE.

FALOU EM.

Anexa responsabilidades adicionais dinamicamente...

PROVAVELMENTE SERÁ.

DECORATOR.

FALOU EM.

Interface unificada de alto nível para simplificar outra complexa...

PROVAVELMENTE SERÁ.

FAÇADE.

FALOU EM.

Compartilhamento para suportar grandes quantidades de objetos...

PROVAVELMENTE SERÁ.

FLYWEIGHT.

FALOU EM.

Prover substituto para controlar um objeto.

PROVAVELMENTE SERÁ.

PROXY.

FALOU EM.

Evitar o acoplamento dando oportunidade a outros objetos...

PROVAVELMENTE SERÁ.

CHAIN OF RESPONSABILITY.

FALOU EM.

Encapsula requisição de objetos...

PROVAVELMENTE SERÁ.

COMMAND.

FALOU EM.

Representação de uma gramática...

PROVAVELMENTE SERÁ.

INTERPRETER.

FALOU EM.

Interface única para acessar coleções sequencialmente...

PROVAVELMENTE SERÁ.

ITERATOR.

FALOU EM.

Encapsula a forma como objetos interagem...

PROVAVELMENTE SERÁ.

MEDIATOR.

FALOU EM.

Captura o estado interno de um objeto...

PROVAVELMENTE SERÁ.

MEMENTO.

FALOU EM.

Quando objeto mudar de estado, notifica os dependentes...

PROVAVELMENTE SERÁ.

OBSERVER.

FALOU EM.

Altera comportamentos quando modificar o estado interno...

PROVAVELMENTE SERÁ.

STATE.

FALOU EM.

Família de algoritmos...

PROVAVELMENTE SERÁ.

STRATEGY.

FALOU EM.

Esqueleto de algoritmos...

PROVAVELMENTE SERÁ.

TEMPLATE METHOD.

FALOU EM.

Operação a ser realizada sobre uma estrutura de objetos...

PROVAVELMENTE SERÁ.

VISITOR.

PADRÕES CRIACIONAIS.

DESCRIÇÃO.

BUILDER.

Esse padrão separa a construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes tipos de representações.

ABSTRACT FACTORY.

Esse padrão fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.

PROTOTYPE.

Esse padrão especifica os tipos de objetos para criar usando uma instância como protótipo e cria novos objetos copiando este protótipo.

SINGLETON.

Esse padrão garante que uma classe tenha apenas uma instância e provê um ponto de acesso global a ela.

FACTORY METHOD.

Esse padrão define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.

PADRÕES ESTRUTURAIS.

DESCRIÇÃO.

ADAPTER.

Esse padrão converte a interface de uma classe em outra interface que normalmente não poderiam trabalhar juntas por serem incompatíveis.

BRIDGE.

Esse padrão desacopla uma interface de sua implementação, de forma que ambas possam variar independentemente.

COMPOSITE.

Esse padrão compõe objetos em estruturas de árvore para representar hierarquias parte-todo, permitindo aos clientes tratarem objetos individuais e composições de objetos uniformemente.

DECORATOR.

Esse padrão anexa responsabilidades adicionais a um objeto dinamicamente. Fornece uma alternativa flexível em relação à herança para estender funcionalidades.

FAÇADE.

Esse padrão oferece uma interface unificada para um conjunto de interfaces em um subsistema, definindo uma interface de alto nível que facilita a utilização do subsistema.

FLYWEIGHT.

Esse padrão utiliza compartilhamento para suportar eficientemente grandes quantidades de objetos de baixa granularidade.

PROXY.

Esse padrão provê um substituto ou ponto através do qual um objeto pode controlar o acesso a outro objeto.

PADRÕES COMPORTAMENTAIS.

DESCRIÇÃO.

CHAIN OF RESONSABILITY.

Esse padrão evita o acoplamento do remetente de uma requisição ao seu receptor ao dar a mais de um objeto a chance de lidar com a requisição.

COMMAND.

Esse padrão encapsula a requisição de um objeto, portanto permitindo que se parametrize os clientes com diferentes requisições.

ITERATOR.

Esse padrão fornece uma maneira de acessar elementos de um objeto agregado sequencialmente sem expor sua representação interna.

MEDIATOR.

Esse padrão define um objeto que encapsula a forma como um conjunto de objetos interagem, promovendo um fraco acoplamento ao evitar que objetos se refiram aos outros explicitamente.

MEMENTO.

Esse padrão captura e externaliza o estado interno de um objeto, sem violar seu encapsulamento, de maneira que o objeto possa ser restaurado posteriormente.

OBSERVER.

Esse padrão define uma dependência um-para-muitos entre objetos para que, quando um objeto mudar de estado, os seus dependentes sejam notificados e atualizados automaticamente.

STATE.

Esse padrão permite a um objeto alterar o seu comportamento quando o seu estado interno for modificado.

STRATEGY.

Esse padrão define uma família de algoritmos, encapsula cada um e faz deles intercambiáveis.

VISITOR.

Esse padrão representa uma operação a ser realizada sobre elementos de uma estrutura de objetos e permite definir uma operação sem mudar as classes dos elementos sobre os quais opera.

INTERPRETER.

Esse padrão, dada uma linguagem, define uma representação para sua gramática em conjunto com um interpretador que utiliza a representação para interpretar sentenças na linguagem.

TEMPlATE METHOD.

Esse padrão define o esqueleto de um algoritmo dentro de uma operação, deixando alguns passos a serem preenchidos pelas subclasses.

