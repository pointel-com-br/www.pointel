# Desenvolvimento de Software - Design de Software. DDD - Domain-Driven Design. Clean Code

Índice

1) DDD - Teoria

2) DDD - Questões Comentadas

3) DDD - Lista de Questões

4) Clean Code - Teoria

5) Clean Code - Questões Comentadas

6) Clean Code - Lista de Questões

DoMAIN-DRIvEN DESIGN - DDD

Conceitos Básicos

Design Orientado ao Domínio (Domain-Driven Design - DDD)

Um domínio geralmente é mais extenso do que alguns objetos e, para torná-lo mais gerenciável, oDDD divide um domínio em subdomínios. O termo DDD 'domínio do problema' é usado para definir uma área funcional dentro de um contexto como uma organização ou departamento.
O desenvolvimento de software é mais frequentemente aplicado para automatizar processos que existem no mundo real ou fornecer soluções para problemas de negócios reais. Os processos de negócios sendo automatizados ou problemas do mundo real que o software é o domínio do software. Devemos entender desde o início que o software é originado e profundamente relacionado a este domínio.
Software é feito de código. Podemos ser tentados a gastar também muito tempo com o código e ver o software simplesmente como objetos e métodos. Considere a fabricação de carros como uma metáfora. Os trabalhadores envolvidos na fabricação de automóveis podem se especializar na produção de peças do carro, mas, ao fazê-lo, muitas vezes têm uma visão limitada do carro inteiro.
Eles começam a ver o carro como uma enorme coleção de peças que precisam se encaixar, mas um carro é muito mais do que isso. Um bom carro começa com uma visão. Começa com especificações cuidadosamente escritas. E continua com o Projeto. Muitos e muitos desenhos. Meses,talvez anos de tempo gasto em design, alterando-o e refinando-o até atingir perfeição, até que reflita a visão original. O processamento design não é tudo no papel. Muito disso inclui fazer modelos de o carro,e testá-los sob certas condições para ver se eles trabalhar. O design é modificado com base nos resultados do teste. O carro é enviado para produção eventualmente, e as peças são criadas e montadas juntas.
O desenvolvimento de software é semelhante. Não podemos simplesmente sentar e digitar o código. Podemos fazer isso e funciona bem para casos triviais. Mas não podemos criar software complexo como esse.
Para criar um bom software, você precisa saber do que se trata esse software. Você não pode criar um sistema de software bancário a menos que tenha um bom entendimento do que é o sistema bancário, é preciso entender o domínio do setor bancário. É possível criar um software bancário complexo sem um bom conhecimento de domínio?
Sem chance. Nunca. Quem conhece o banco? O arquiteto de software? Não. Ele apenas usa o banco para manter seu dinheiro seguro e disponível quando ele precisa. O analista de software? Na verdade, não. Ele sabe analisar um determinado tema, quando lhe são dados todos os ingredientes
/ 60

/

necessários. O desenvolvedor? Esqueça. Quem então? Os banqueiros, claro. O sistema bancário é muito bem compreendido pelas pessoas de dentro, por seus especialistas. Eles conhecem todos os detalhes, todas as armadilhas, todos os problemas possíveis.
É por aqui que devemos sempre começar: o domínio. Quando iniciamos um projeto de software,devemos nos concentrar no domínio em que ele está operando. Todo o propósito do software é aprimorar um domínio específico. Para poder fazer isso, o software deve se encaixar harmoniosamente com o domínio para o qual foi criado. Caso contrário, ele introduzirá tensão no domínio, provocando mau funcionamento, danos e até mesmo o caos.
Como podemos fazer com que o software se encaixe harmoniosamente com o domínio? A
melhor maneira de fazer isso é tornar o software um reflexo do domínio. O software precisa incorporar os conceitos e elementos centrais do domínio e realizar com precisão as relações entre eles. O software tem que modelar o domínio.
Alguém sem conhecimento de banco deve ser capaz de aprender muito apenas lendo o código em um modelo de domínio. Isso é essencial. O software que não tem suas raízes plantadas profundamente no domínio não reagirá bem às mudanças ao longo do tempo.
Então começamos com o domínio. Um domínio é algo deste mundo. Precisamos criar uma abstração do domínio. Aprendemos muito sobre um domínio enquanto conversamos com os especialistas do domínio. Mas esse conhecimento bruto não será facilmente transformado em construções de software, a menos que construamos uma abstração dele, um projeto em nossas mentes. No começo,o projeto está sempre incompleto.

Mas com o tempo, enquanto trabalhamos nisso, nós o melhoramos e ele se torna cada vez mais claro para nós. O que é essa abstração? É um modelo, um modelo do domínio. De acordo com EricEvans, um modelo de domínio não é um diagrama específico; é a ideia que o diagrama pretende transmitir. Não é apenas o conhecimento na cabeça de um especialista de domínio; é uma abstração rigorosamente organizada e seletiva desse conhecimento. O modelo é nossa representação interna do domínio de destino e é muito necessário durante todo o processo de design e desenvolvimento.
Durante o processo de design, lembramos e fazemos muitas referências ao modelo. O
mundo ao nosso redor é demais para nossas cabeças lidarem. Mesmo um domínio específico pode ser mais do que uma mente humana pode lidar ao mesmo tempo. Precisamos organizar a informação,sistematizá-la, dividi-la em pedaços menores, agrupar esses pedaços em módulos lógicos,
pegar um de cada vez e lidar com isso. Precisamos até deixar algumas partes do domínio de fora. Um domínio contém informações demais para incluirtudo no modelo. E muito disso nem precisa ser considerado.
DDD pode ser visto por alguns como a volta da orientação a objetos. É verdade que o livro é um chamado às boas práticas de programação que já existem desde a época remota do SmalITalk.
/ 60

Quando se fala em Orientação a Objetos pensa-se logo em classes, heranças,
polimorfismo,
encapsulamento. Mas a essência da Orientação a Objetos também tem elementos como:

* Alinhamento do código com o negócio: o contato dos desenvolvedores com os especialistas do domínio é algo essencial quando se faz DDD (o pessoal de métodos ágeis já sabe disso faz tempo);
* Favorecer reutilização: os blocos de construção, que veremos adiante, facilitam aproveitar um mesmo conceito de domínio ou um mesmo código em vários lugares;
* Mínimo de acoplamento: Com um modelo bem-feito, organizado, as várias partes de um sistema interagem sem que haja muita dependência entre módulos ou classes de objetos de conceitos distintos;
* Independência da Tecnologia: DDD não foca em tecnologia, mas sim em entender as regras de negócio e como elas devem estar refletidas no código e no modelo de domínio. Não que a tecnologia usada não seja importante, mas essa não é uma preocupação de DDD.
Para ter um software que atenda perfeitamente a um determinado domínio, é necessário que se estabeleça, em primeiro lugar, uma Linguagem Ubíqua, ou Linguagem comum, com termos bem definidos, que fazem parte do domínio do negócio e que são usados por todas as pessoas que fazem parte do processo de desenvolvimento de software. Nessa linguagem estão termos que fazem parte das conversas diárias entre especialistas de negócio e times de desenvolvimento. Todos devem usar os mesmos termos tanto na linguagem falada quanto no código.
i (CESPE - TRE PE - 2017) O DDD (domain-driven design)

i a) consiste em uma técnica que trata os elementos de domínio e que garante segurança à aplicação i em uma programação orientada a objetos na medida em que esconde as propriedades desses i objetos.
i b) não tem como foco principal a tecnologia, mas o entendimento das regras de negócio e de como i elas devem estar refletidas no código e no modelo de domínio.
i c) prioriza a simplicidade do código, sendo descartados quaisquer usos de linguagem ubíqua que i fujam ao domínio da solução.
i d) constitui-se de vários tratadores e(ou) programas que processam os eventos para produzir i respostas e de um disparador que invoca os pequenos tratadores.
i e) define-se como uma interface de domínio normalmente especificada e um conjunto de operações
; que permite acesso a uma funcionalidade da aplicação.

i Comentários: Para ter um software que atenda perfeitamente a um determinado domínio, é i necessário que se estabeleça, em primeiro lugar, uma Linguagem Ubíqua. Nessa linguagem estão i termos que fazem parte das conversas diárias entre especialistas de negócio e times de
/ 60

/

i desenvolvimento. Todos devem usar os mesmos termos tanto na linguagem falada quanto no i i código. A alternativa a está errada, pois trata da Programação Orientada a Objetos.A alternativa b i i está correta, de fato, DDD foca em entender as regras de negócio e como elas devem estar refletidas i i no código e no modelo de domínio. A alternativa c também está errada! Ao contrário do que diz a i i questão, linguagem ubíqua é um conceito muito comum em DDD. Por fim, a alternativa d está i i incorreta, pois está citando o conceito de Programação Orientada a Eventos. E a alternativa e está i i incorreta porque DDD não se trata de uma interface de domínio normalmente e um conjunto de i operações. (Gabarito: Letra B)i

Naked Objects

Naked Objects é um padrão de arquitetura usado na engenharia de software. É definida por três princípios:
* Toda a lógica de negócios deve ser encapsulada nos objetos de domínio. Este princípio não é exclusivo de objetos nus; é um forte compromisso com o encapsulamento.
* A interface do usuário deve ser uma representação direta dos objetos do domínio,
com todas as ações do usuário consistindo em criar, recuperar ou invocar métodos nos objetos do domínio. Este princípio não é exclusivo de objetos nus: é uma interpretação de uma interface de usuário orientada a objetos.
* O recurso inovador do padrão de objeto nu surge combinando o Io e 2o princípios em um 3
0 princípio:

A interface do usuário deve ser criada de forma totalmente automática a partir das definições dos objetos do domínio. Isso pode ser feito usando reflexão ou geração de código-fonte.
O padrão de Naked Objects foi descrito formalmente pela primeira vez na tese de doutorado deRichard Pawson que inclui investigação de antecedentes e inspirações para o padrão,
incluindo, por exemplo, a interface de usuário mórfica.
O primeiro framework open source completo a ter implementado o padrão foi nomeado NakedObjects. Em 2021, Pawson anunciou que posteriormente aplicou o mesmo padrão ao paradigma de programação Functional Programming, como uma alternativa ao paradigma de programação orientada a objetos, criando uma variante da estrutura Naked Objects chamada Naked Functions.
O design orientado por domínio (DDD) concentra-se no que mais importa nos aplicativos corporativos: o domínio principal do negócio. Usando princípios orientados a objetos,você pode desenvolver um modelo de domínio que todos os membros da equipe - incluindo especialistas em negócios e técnicos - possam entender.
Mas se você já tentou criar um aplicativo orientado a domínio, saberá que aplicar os princípios DDDé mais fácil dizer do que fazer. Com a estrutura Naked Objects de software livre, você constrói seu

/ 60

/

aplicativo Java escrevendo apenas as classes de domínio principais, deixando que ele cuide do restante da infraestrutura.
O Naked Objects renderiza automaticamente seu objeto de domínio em um visualizador genérico
- rich client ou HTML. Você pode usar sua integração com o Fitnesse para testar o desenvolvimento de seu aplicativo, história por história. E, uma vez desenvolvido, você pode implantar seu aplicativo em tempo de execução completo do Naked Objects ou em sua infraestrutura de aplicativo existente.
/ 60

/

QUESTõES CoMENTADAS - DDD

1. (CESPE - DP DF - 2022) Quanto ao domain driven design (DDD), julgue o item a seguir.

O DDD permite o desenvolvimento de software com base no conhecimento e na modelagem do negócio.
Comentários:

Pessoal, DDD é um conjunto de princípios com foco em domínio, exploração de modelos de formas criativas e definir e falar a linguagem Ubíqua, baseado no contexto delimitado.Ademais, a questão do CESPE de 2017, do TRE-PE, nos diz o seguinte: o DDD não tem como foco principal a tecnologia,mas o entendimento das regras de negócio e de como elas devem estar refletidas no código e no modelo de domínio.
Gabarito: Correto

2. (CESPE - DP DF - 2022) Acerca de DDD (domain driven design), julgue o item a seguir.

O modelo é estático no DDD; caso ele se torne complexo, caberá aos desenvolvedores transferirem a abstração da complexidade para o software.
Comentários

Pessoal, o entendimento de um negócio é algo dinâmico e que precisa ser um processo contínuo.Dificilmente a primeira versão de uma especificação funcional é a que soluciona adequadamente o problema. Para o autor Evans, DDD é totalmente mutável, portanto, falar que o DDD é estático está errado!
Gabarito: Errado

3. (CESPE - DP DF - 2022) Acerca de DDD (domain driven design), julgue o item a seguir.

Devido a sua simplicidade, o DDD não permite a representação do modelo por meio de artefatos de software bem definidos.
Comentários:

Errado, normalmente, o DDD é utilizado para aplicações complexas e é muito fácil de entender. Por outro lado, difícil de aplicar.
Gabarito: Errado

/ 60

/

4. (CESPE - Telebras - 2022 - Adaptada) Acerca de aspectos diversos pertinentes a objetos de avaliação associados à análise de sistemas, julgue o item que se segue.
Com relação ao DDD (Domain Driven Design) é correto afirmar que ele traz como benefício o isolamento das regras de negócios da lógica de apresentação.
Comentários:

Pessoal, está correto! De fato, há o isolamento das regras de negócios da lógica de apresentação,que é a interface com o usuário. No DDD, os desenvolvedores devem ter um profundo conhecimento do domínio do sistema que eles desenvolvem. Esse conhecimento deve ser obtido por meio de conversas e discussões frequentes com especialistas no domínio (ou no negócio).Portanto, o design do sistema deve ser norteado para atender ao seu domínio. E não, por exemplo, para se moldar a uma determinada tecnologia de programação. Em suma, o design é dirigido pelo domínio,e não por frameworks, arquiteturas, linguagens de programação, etc. Pessoal, a questão original possui como gabarito errado, porém essa questão foi adaptada.
Gabarito: Correto

5. (CESPE - Ministério da Economial- 2020) Acerca de DDD (domain driven design),
julgue o item a seguir.
O bounded contexto é um limite conceituai do modelo, sendo considerado um delimitador de domínio.
Comentários:

Um bounded contexto é uma parte definida do software onde determinados termos,
definições e regras se aplicam de maneira consistente, explicou Eric Evans em sua palestra na DDDEurope no início de 2019.
Gabarito: Correto

6. (CESPE - Ministério da Economia- 2020) Acerca de DDD (domain driven design), julgue o item a seguir.
A modelagem e a implementação atuam de forma independente, tal que toda a elaboração do modelo deve preceder a implementação do código-fonte.
Comentários:

/ 60

/

Pessoal, na verdade, a modelagem e a implementação atuam de forma dependente ou conjunta.Usando uma linguagem ubíqua, implementação e modelagem usam uma única linguagem, DDD é uma metodologia ágil, em metodologia ágil, ocorrem iterações nas quais ocorre a modelagem e a implementação quase que em paralelo. Portanto, não ocorre de forma independente.
Gabarito: Errado

7. (CESPE-TJ-PA-2020) Assinale a opção que apresenta o padrão de arquitetura de software que,no âmbito DDD (domain driven design), é uma implementação do padrão para ajudar a prototipar, desenvolver e implantar rapidamente aplicativos orientados a domínio.
a) client/server architecture b) federal enterprise architecture c) service-oriented architecture d) Java persistence architecture e) naked object
Comentários:

Com a estrutura Naked Objects de software livre, você constrói seu aplicativo Java escrevendo apenas as classes de domínio principais, deixando que ele cuide do restante da infraestrutura. ONaked Objects renderiza automaticamente seu objeto de domínio em um visualizador genérico -rich client ou HTML .

Gabarito: Letra E

8. (CESPE - MPC PA- 2019) No Domain-Driven Design, a Ubiquitous Language é considerada a) uma linguagem de programação utilizada pelos desenvolvedores para escrever os códigos.
b) uma linguagem de modelagem utilizada pelos analistas para representar os processos de negócio.
c) uma linguagem do projeto de desenvolvimento de software utilizada para comunicação de todos os envolvidos no projeto.
d) uma linguagem de notação utilizada pelos arquitetos para representar as funcionalidades do software.
e) uma linguagem de semântica utilizada pelos especialistas para definir as especificações de negócio.
Comentários:

A linguagem ubíqua ou "linguagem onipresente" tem como objetivo viabilizar a comunicação entre desenvolvedores e especialistas de maneira mais natural, para que todos possam contribuir de forma satisfatória nas discussões sobre o domínio. Portanto, nosso gabarito é a letra c) Ubiquitous
/ 60

/

Language é considerada uma linguagem do projeto de desenvolvimento de software utilizada para comunicação de todos os envolvidos no projeto
Gabarito: Letra C

9. (CESPE - SLU DF- 2019) Julgue o próximo item, a respeito de domain-driven design, design patterns, emergent design, enterprise content management e REST.
No desenvolvimento embasado em domain-driven design, a definição da tecnologia a ser utilizada tem importância secundária no projeto.
Comentários:

Perfeito! Inicialmente você pensa que está errado quando a questão diz: "tem importância" ...porque na verdade, não é prioritário. Quando lê a questão inteira verifica que está correto!

Gabarito: Correto

10. (CESPE- MPE PI- 2018) Julgue o item subsequente, referente a Domain Driven Design e a Design
Patterns.

No Domain Driven Design, o projeto de software baseia sua reação em eventos externos e internos, tendo como premissa uma quantidade finita de estados que enfatizam a separação entre os modelos abstratos independentes de implementação e os específicos de implementação.
Comentários:

Na verdade, a questão trata sobre outro assunto. No desenvolvimento concorrente, o projeto de software baseia sua reação em eventos externos e internos, tendo como premissa uma quantidade finita de estados que enfatizam a separação entre os modelos abstratos independentes de implementação e os específicos de implementação.
Gabarito: Errado

11.(CESPE - STJ- 2018) Julgue o próximo item, relativo a model-view-
controller (MVC), proxy reverso e representational state transfer (REST).
O domain-driven design é parte das práticas do princípio lean da engenharia ágil voltada a arquiteturas que devem ser conduzidas por requisitos técnicos subjacentes do sistema, e não por planejamento especulativo para um futuro que pode mudar.
Comentários:

/ 60

/

Perfeita definição! De fato, 0 foco principal do DDD deve ser o domínio e domínios complexos devem estar baseados em um modelo. Ademais, o DDD procura reforçar conceitos e boas práticas relacionadas à 00 como alinhamento do código com o negócio; favorecer reutilização;mínimo de acoplamento; independência da tecnologia.
Gabarito: Correto

12. (IBFC-EMBASA-2017) Eric Evans, criador do DDD (Domain-Driven Design), afirma que,
no DDD,
foca-se numa linguagem que possa descrever sucintamente qualquer situação no domínio e descrever o que faremos para resolver ou que tipos de cálculos precisamos realizar. Essa linguagem pode ser compartilhada entre pessoas do negócio, especialistas de domínio,assim como os programadores que irão escrever o software, e isso chamamos de linguagem:
a) ecológica b) temporal c) ubíqua d) estética
Comentários:

Ubíqua, Ubíqua! Falamos diversas vezes! A linguagem ubíqua consiste de um conjunto de termos que devem ser plenamente entendidos tanto por especialistas no domínio (usuários do sistema)como por desenvolvedores (implementadores do sistema).

Gabarito: Letra C

13. (CESPE -TRE PE- 2017) 0 DDD (domain-driven design)

a) consiste em uma técnica que trata os elementos de domínio e que garante segurança à aplicação em uma programação orientada a objetos na medida em que esconde as propriedades desses objetos.
b) não tem como foco principal a tecnologia, mas o entendimento das regras de negócio e de como elas devem estar refletidas no código e no modelo de domínio.
c) prioriza a simplicidade do código, sendo descartados quaisquer usos de linguagem ubíqua que fujam ao domínio da solução.
d) constitui-se de vários tratadores e(ou) programas que processam os eventos para produzir respostas e de um disparador que invoca os pequenos tratadores.
e) define-se como uma interface de domínio normalmente especificada e um conjunto de operações que permite acesso a uma funcionalidade da aplicação.
Comentários:

/ 60

/

Para ter um software que atenda perfeitamente a um determinado domínio, é necessário que se estabeleça, em primeiro lugar, uma Linguagem Ubíqua. Nessa linguagem estão termos que fazem parte das conversas diárias entre especialistas de negócio e times de desenvolvimento.Todos devem usar os mesmos termos tanto na linguagem falada quanto no código. A alternativa a está errada,pois trata da Programação Orientada a Objetos. A alternativa b está correta, de fato,
DDD foca em entender as regras de negócio e como elas devem estar refletidas no código e no modelo de domínio. A alternativa c também está errada! Ao contrário do que diz a questão,linguagem ubíqua é um conceito muito comum em DDD. Por fim, a alternativa d está incorreta, pois está citando o conceito de Programação Orientada a Eventos. E a alternativa e está incorreta porqueDDD não se trata de uma interface de domínio normalmente e um conjunto de operações.
Gabarito: Letra B

14. (CESPE - TRT 8a Região - 2016) Assinale a opção correta com relação à modelagem orientada a domínio (DDD - domain driven design).
a) Fábricas são classes que contêm a lógica do negócio, mas que não pertencem a nenhuma entidade ou objeto de valores.
b) O uso de DDD será aplicável quando o software atender uma área de negócio muito específica e complexa.
c) DDD oferece uma série de conceitos e padrões que auxiliam o desenvolvedor no projeto da solução, exclusivamente no nível estratégico.
d) Capacidade de desenvolvimento iterativo e regras de negócio simples são requisitos básicos para a aplicação efetiva da modelagem DDD.
e) DDD utiliza os mesmos conceitos e premissas do processo de análise e projeto em orientação a objetos.
Comentários:

O DDD é uma abordagem para o desenvolvimento de software para necessidades complexas,conectando profundamente a implementação a um modelo em evolução dos principais conceitos de negócios. Assim, o uso de DDD será aplicável quando o software atender uma área de negócio muito específica e complexa
Gabarito: Letra B

15. (ESAF - ESAF- 2015) O Domain-Driven Design - DDD utiliza o conceito de divisão do sistema em camadas. As camadas desse modelo são:
a) aplicação, apresentação, sessão, transporte, rede, enlace e física.

b) de apresentação, de negócio e de dados.

c) do modelo, da visualização e de controle.

d) domínio de usuário, domínio de negócio e domínio de dados.

/ 60

/

e) interface com usuário, aplicação, domínio e infraestrutura.

Comentários:

Pessoal, vocês quase pensaram que estavam na aula errada? Redes? Haha. Não pessoal, as camadas do DDD são interface com usuário, aplicação, domínio e infraestrutura.
Gabarito: Letra E

16. (CESPE - STJ- 2015) Julgue o próximo item, relativo a Domain-Driven Design e design patterns.

Um dos princípios-chave do Domain-Driven Design é o uso de uma linguagem ubíqua com termos bem definidos, que integram o domínio do negócio e que são utilizados entre desenvolvedores especialistas de negócio.
Comentário:

Um dos princípios-chave do Domain-Driven Design é o uso de uma linguagem ubíqua,
perfeito,
termos bem definidos, que integram o domínio do negócio perfeito, e que são utilizados entre desenvolvedores especialistas de negócio perfeito! Questão correta pessoal!
Gabarito: Correto

17. (CESPE - STJ- 2015) Acerca de arquitetura de software e Domain-Driven Design,
julgue o seguinte item.
Domain-Driven Design pode ser aplicada ao processo de concepção arquitetural de um sistema de software, sendo que domain, em um software, designa o campo de ação, conhecimento e influência.
Comentários:

Perfeito! Domain ou domínio, em um software, designa o campo de ação,
conhecimento e influência.
Gabarito: Correto

18. (CESPE - MPOG- 2013) Com relação às metodologias ágeis de desenvolvimento, julgue os itens a seguir.
De acordo com os padrões de DDD (domain-driven design), ao se escrever um novo sistema para também interagir com um sistema legado (considerado um código de difícil manutenção),cria-
se uma camada entre os dois sistemas denominada camada anticorrupção.

/ 60

/

Comentários:

Correto, a Camada Anti-corrupção ocorre quando temos um sistema legado, com código muito bagunçado e uma interface complexa, e estamos escrevendo um sistema novo com o código razoavelmente bem feito, criamos uma camada entre esses dois sistemas. O nosso sistema novo e bem-feito falará com essa camada, que possui uma interface bem-feita.
Gabarito: Correto

LISTA DE QUESTõES - DDD

1. (CESPE - DP DF - 2022) Quanto ao domain driven design (DDD), julgue o item a seguir.

O DDD permite o desenvolvimento de software com base no conhecimento e na modelagem do negócio.
2. (CESPE - DP DF - 2022) Acerca de DDD (domain driven design), julgue o item a seguir.

O modelo é estático no DDD; caso ele se torne complexo, caberá aos desenvolvedores transferirem a abstração da complexidade para o software.
3. (CESPE - DP DF - 2022) Acerca de DDD (domain driven design), julgue o item a seguir.

Devido a sua simplicidade, o DDD não permite a representação do modelo por meio de artefatos de software bem definidos.
4. (CESPE - Telebras - 2022 - Adaptada) Acerca de aspectos diversos pertinentes a objetos de avaliação associados à análise de sistemas, julgue o item que se segue.
Com relação ao DDD (Domain Driven Design) é correto afirmar que ele traz como benefício o isolamento das regras de negócios da lógica de apresentação.
5. (CESPE - Ministério da Economial- 2020) Acerca de DDD (domain driven design), julgue o item a seguir.
O bounded contexto é um limite conceituai do modelo, sendo considerado um delimitador de domínio.
6. (CESPE - Ministério da Economia- 2020) Acerca de DDD (domain driven design), julgue o item a seguir.
A modelagem e a implementação atuam de forma independente, tal que toda a elaboração do modelo deve preceder a implementação do código-fonte.
7. (CESPE-TJ-PA-2020) Assinale a opção que apresenta o padrão de arquitetura de software que,no âmbito DDD (domain driven design), é uma implementação do padrão para ajudar a prototipar, desenvolver e implantar rapidamente aplicativos orientados a domínio.
a) client/server architecture b) federal enterprise architecture
/ 60

/

c) service-oriented architecture d) Java persistence architecture e) naked object
8. (CESPE - MPC PA- 2019) No Domain-Driven Design, a Ubiquitous Language é considerada a) uma linguagem de programação utilizada pelos desenvolvedores para escrever os códigos.
b) uma linguagem de modelagem utilizada pelos analistas para representar os processos de negócio.
c) uma linguagem do projeto de desenvolvimento de software utilizada para comunicação de todos os envolvidos no projeto.
d) uma linguagem de notação utilizada pelos arquitetos para representar as funcionalidades do software.
e) uma linguagem de semântica utilizada pelos especialistas para definir as especificações de negócio.
9. (CESPE - SLU DF- 2019) Julgue o próximo item, a respeito de domain-driven design, design patterns, emergent design, enterprise content management e REST.
No desenvolvimento embasado em domain-driven design, a definição da tecnologia a ser utilizada tem importância secundária no projeto.
10. (CESPE - MPE PI-2018) Julgue o item subsequente, referente a Domain Driven Design e a Design
Patterns.

No Domain Driven Design, o projeto de software baseia sua reação em eventos externos e internos, tendo como premissa uma quantidade finita de estados que enfatizam a separação entre os modelos abstratos independentes de implementação e os específicos de implementação.
11. (CESPE - STJ- 2018) Julgue o próximo item, relativo a model-view- controller (MVC), proxy reverso e representational state transfer (REST).
O domain-driven design é parte das práticas do princípio lean da engenharia ágil voltada a arquiteturas que devem ser conduzidas por requisitos técnicos subjacentes do sistema, e não por planejamento especulativo para um futuro que pode mudar.
12. (IBFC-EMBASA-2017) Eric Evans, criador do DDD (Domain-Driven Design), afirma que, no
DDD,
foca-se numa linguagem que possa descrever sucintamente qualquer situação no domínio e descrever o que faremos para resolver ou que tipos de cálculos precisamos realizar. Essa linguagem pode ser compartilhada entre pessoas do negócio, especialistas de domínio,assim como os programadores que irão escrever o software, e isso chamamos de linguagem:
/ 60

/

a) ecológica b) temporal c) ubíqua d) estética
13. (CESPE -TRE PE- 2017) O DDD (domain-driven design)

a) consiste em uma técnica que trata os elementos de domínio e que garante segurança à aplicação em uma programação orientada a objetos na medida em que esconde as propriedades desses objetos.
b) não tem como foco principal a tecnologia, mas o entendimento das regras de negócio e de como elas devem estar refletidas no código e no modelo de domínio.
c) prioriza a simplicidade do código, sendo descartados quaisquer usos de linguagem ubíqua que fujam ao domínio da solução.
d) constitui-se de vários tratadores e(ou) programas que processam os eventos para produzir respostas e de um disparador que invoca os pequenos tratadores.
e) define-se como uma interface de domínio normalmente especificada e um conjunto de operações que permite acesso a uma funcionalidade da aplicação.
14. (CESPE - TRT 8a Região - 2016) Assinale a opção correta com relação à modelagem orientada a domínio (DDD - domain driven design).
a) Fábricas são classes que contêm a lógica do negócio, mas que não pertencem a nenhuma entidade ou objeto de valores.
b) O uso de DDD será aplicável quando o software atender uma área de negócio muito específica e complexa.
c) DDD oferece uma série de conceitos e padrões que auxiliam o desenvolvedor no projeto da solução, exclusivamente no nível estratégico.
d) Capacidade de desenvolvimento iterativo e regras de negócio simples são requisitos básicos para a aplicação efetiva da modelagem DDD.
e) DDD utiliza os mesmos conceitos e premissas do processo de análise e projeto em orientação a objetos.
15. (ESAF - ESAF- 2015) O Domain-Driven Design - DDD utiliza o conceito de divisão do sistema em camadas. As camadas desse modelo são:
a) aplicação, apresentação, sessão, transporte, rede, enlace e física.

b) de apresentação, de negócio e de dados.

c) do modelo, da visualização e de controle.

d) domínio de usuário, domínio de negócio e domínio de dados.

e) interface com usuário, aplicação, domínio e infraestrutura.

/ 60

/

16. (CESPE - STJ- 2015) Julgue o próximo item, relativo a Domain-Driven Design e design patterns.

Um dos princípios-chave do Domain-Driven Design é o uso de uma linguagem ubíqua com termos bem definidos, que integram o domínio do negócio e que são utilizados entre desenvolvedores especialistas de negócio.
17. (CESPE - STJ- 2015) Acerca de arquitetura de software e Domain-Driven Design, julgue o seguinte item.
Domain-Driven Design pode ser aplicada ao processo de concepção arquitetural de um sistema de software, sendo que domain, em um software, designa o campo de ação, conhecimento e influência.
18. (CESPE - MPOG- 2013) Com relação às metodologias ágeis de desenvolvimento, julgue os itens a seguir.
De acordo com os padrões de DDD (domain-driven design), ao se escrever um novo sistema para também interagir com um sistema legado (considerado um código de difícil manutenção),cria-
se uma camada entre os dois sistemas denominada camada anticorrupção.

/ 60

/

GABARITo í. CORRETO
2. ERRADO

3. ERRADO

4. CORRETO

5. CORRETO

6. ERRADO

7. LETRA E

8. LETRA C

9. CORRETO

10. ERRADO

11. CORRETO

12. LETRA C

13. LETRA B

14. LETRA B

15. LETRA E

16. CORRETO

17. CORRETO

18. CORRETO

/ 60

/

Conceitos Básicos

KEEP
CALM

BECAUSE

ITS JUST
ATEST

KeepCalmAndPosters.com

CLEAN CoDE

O que é o Clean Code? Há muitas definições, mas algumas respostas e características encontradas são comuns, como por exemplo, a codificação deve ser simples e de fácil manutenção, não pode haver repetições de código, testes de unidade devem ser implementados, implementação de forma organizada, entre outros.
O Código Limpo é um conjunto de técnicas de programação que quando praticadas pelos desenvolvedores tem como objetivo garantir a legibilidade e qualidade do código produzido.
Escrever um código compreensível para outros colaboradores tornou-se crucial para melhorar a colaboração e a produtividade. O Código Limpo tornou-se uma das práticas de software mais relevantes e tem sido amplamente adotado como sinônimo de qualidade de código por desenvolvedores de software e organizações de desenvolvimento de software em todo o mundo. No entanto, muito pouco se sabe sobre se os desenvolvedores concordam com os princípios do Código Limpo e como eles os aplicam na prática.
Há inúmeras definições para Código Limpo, ao longo dessa parte da aula, vou apresentar as citações mais importantes de grandes programadores, os mais conhecidos, trazidos pelo livro Código Limpo1
Gosto do meu código elegante e eficiente. A lógica deve ser direta para dificultar o encobrimento de bugs. as dependências mínimas para facilitar a manutenção, o tratamento de erro completo de acordo com uma estratégia clara e o desempenho próximo do mais eficiente de modo a não incitar as pessoas a tornarem o código confuso com otimizações sorrateiras. O código limpo faz bem apenas uma coisa.2
Um código ruim incita o crescimento do caos num código. Quando outras pessoas alteram um código ruim, elas tendem a piorá-lo. Dave Thomas e Andy Hunt expressam isso de outra forma. Eles usam a metáfora das janelas quebradas. Uma construção com janelas quebradas parece que ninguém cuida dela. Dessa forma, outras pessoas deixam de se preocupar com ela também. Elas
Clean Code: A Handbook of Agile Software Craftsmanship

Bjarne Stroustrup, criador do C++ e autor do livro A linguagem de programação C++.

,.Z 60

/

permitem que as outras janelas se quebrem também. No final das contas, as próprias pessoas as quebram. Elas estragam a fachada com pichações e deixam acumular lixo. Uma única janela inicia o processo de degradação.
Para Bjarne um código limpo faz bem apenas uma coisa. Não é por acaso que há inúmeros princípios de desenvolvimento de software que podem ser resumidos a essa simples afirmação. Um código ruim tenta fazer coisas demais, ele está cheio de propósitos obscuros e ambíguos. O código limpo é centralizado. Cada função, cada classe, cada módulo expõe uma única tarefa que nunca sofre interferência de outros detalhes ou fica rodeada por eles.
Um código limpo é simples e direto. Ele é tão bem legível quanto uma prosa bem escrita. Ele jamais torna confuso o objetivo do desenvolvedor, em vez disso, ele está repleto de abstrações claras e linhas de controle objetivas.3
..
..
..
..
i i Além de seu criador, um desenvolvedor pode ler e melhorar um código limpo. Ele i tem testes de unidade e de aceitação, nomes significativos; ele oferece apenas uma iÊ maneira, e não várias, de se fazer uma tarefa; possui poucas dependências, as quais i i são explicitamente declaradas e oferecem um API mínimo e claro. O código deve ser iÊ inteligível já que dependendo da linguagem, nem toda informação necessária pode i i ser expressa no código em si.4
i

Eu poderia listar todas as qualidades que vejo em um código limpo, mas há uma predominante que leva a todas as outras. Um código limpo sempre parece que foi escrito por alguém que se importava. Não há nada de óbvio no que se pode fazer para torná-lo melhor. Tudo foi pensado pelo autor do código, e se tentar pensar em algumas melhoras, você voltará ao início, ou seja, apreciando o código deixado para você por alguém que se importa bastante com essa tarefa.5
Vejamos as palavras de Ron Jeffries6: nestes anos recentes, comecei, e quase finalizei, com as regras de Beck sobre código simples. Em ordem de prioridade, são:
1. Efetue todos os testes;

2. Sem duplicação de código;

3. Expressa todas as ideias do projeto que estão no sistema;

4. Minimiza o número de entidades, como classes, métodos funções e outras do tipo;

Grady Booch, autor do livro Object Oriented Analysis and Design with Applications
Dave Thomas, fundador da OTI, o pai da estratégia Eclipse

Michael Feathers, autor de Working Effectively with Legacy Code

Ron Jeffries autor de Extreme Programming Installed and Extreme Programming Adventures in C#

,.Z 60

/

Dessas quatro, Jeffries foca mais na de duplicação. Quando a mesma coisa é feita repetidas vezes, é sinal de que uma ideia em sua cabeça não está bem representada no código. Tento descobrir o que é e, então, expressar aquela ideia com mais clareza.
Expressividade, para Jeffries, são nomes significativos. Com ferramentas de programação modernas, como a Eclipse, renomear é bastante fácil. Entretanto, a expressividade vai além de nomes. Também se verifica se um método ou objeto faz mais de uma tarefa. Se for um objeto,provavelmente ele precisará ser dividido em dois ou mais. Se for um método, sempre usa-se a refatoração do Método de Extração nele, resultando em um método que expressa mais claramente sua função e em outros métodos que dizem como ela é feita.
Duplicação e expressividade levam ao que é considerado um código limpo, e melhorar um código ruim com apenas esses dois conceitos na mente pode fazer uma grande diferença. Redução de duplicação de código, alta expressividade e criação no início de abstrações simples. É isso que torna um código limpo.
r i
; Você sabe que está criando um código limpo quando cada rotina que você leia se :
Ê mostra como o que você esperava. Você pode chamar de código belo quando ele i i também faz parecer que a linguagem foi feita para o problema.7i

(CESPE - DP DF- 2022) A seguir, é apresentado um bom exemplo de código, de acordo com clean code.
int .a = 1;

if (

O == 1 )

a = Ol;

else

1 = 01;

Comentários: A questão diz que "é apresentado um bom exemplo de código". Dá uma olhada no código e me diga o que entendeu? Não há muita clareza não é mesmo? Acha que esse código tem
Ward Cunningham, criador do conceito de "WikiWiki", criador do Fit, co-criador da
Programação Extrema (eXtreme Programming). Incentivador dos Padrões de Projeto. Líder da Smalltalk e da 00. Pai de todos aqueles que se importam com o código.
consistência de expressão? Nomes significativos? Não né? Portanto essa questão está errada.(Gabarito: Errado)

Um código só está realmente limpo se ele for validado. Mas a questão é, como é possível manter um teste limpo? A resposta é simples, da mesma maneira que mantemos o nosso código limpo,com clareza, simplicidade e consistência de expressão.

Testes limpos seguem as regras do acrônimo FIRST (Fast, Indepedent, Repeatable,
Self-validation,
Timely).

* Rapidez: os testes devem ser rápidos para que possam ser executados diversas vezes;

* Independência: quando testes são dependentes, uma falha pode causar um efeito dominó dificultando a análise individual;
* Repetitividade: deve ser possível repetir o teste em qualquer ambiente;

* Auto validação: bons testes possuem como resultado respostas do tipo verdadeiro ou falso.
Caso contrário, a falha pode se tornar subjetiva;

* Pontualidade: os testes precisam ser escritos antes do código de produção, onde os testes serão aplicados. Caso contrário, o código pode ficar complexo demais para ser testado ou até pode ser que o código não possa ser testado.
r ..
..
..

>.l i (CESPE - TJ PA - 2020) O Clean Code deve considerar também o momento de teste do software em i i desenvolvimento. O Teste Limpo deve
I

I

i a) ser o mais completo possível, para que não seja necessário repeti-lo muitas vezes.
i b) ser específico para determinado ambiente.

i c) ser executado de forma que os testes sejam escritos antes que o código a ser testado esteja no ambiente de produção.
i d) produzir resultados com respostas o mais abertas possível, para garantir eficiência ao processo, i i e) contemplar todas as dependências possíveis, para garantir a eficácia do processo de testes.
i Comentários: Vamos analisar cada alternativa. A letra a está errada, porque, na verdade, os testes i i devem ser repetidos, e executados diversas vezes. Ao contrário do que diz a questão: " não seja i necessário repeti-lo muitas vezes". A letra b está incorreta, na verdade, o teste limpo deve ser feito i i para qualquer ambiente, não como diz a questão "ser específico para determinado ambiente". A i i letra C está correta, é exatamente o que preconiza as metodologias ágeis: TesteLimpo deve ser i i executado de forma que os testes sejam escritos antes que o código a ser testado esteja no ambiente i i de produção. A alternativa d também está errada, na verdade, o teste deve ser objetivo e não i i subjetivo. Por fim, a alternativa e está errada. Um teste limpo não deve contemplar todas as i i dependências. (Gabarito: Letra A)i

/ 60

/

3 R's da Arquitetura de software

O conceito do Clean Code é baseado nos 3 R's da Arquitetura de software, que são
Readability
(legibilidade), Reusability (reuso) e Refatoring (refatoração). Os 3 conceitos se complementam para a obtenção de um projeto sustentável à empresa.
A legibilidade prioriza a clareza na escolha de nomes, padronização k codificação, tendo como
Refactorability

Can modules be modified without breaking the system?
Reusability

Can modules be reused?
Are functions small?

Are side effects avoided?

Readability

Are variables named well?

Is the code consistently formatted?

Are functions documented?

principais características:

* Nomes de variáveis;

* Nomes de funções;

* Formatação;

* Níveis de aninhamento;

* Quantidade de linhas em funções;
* Quantidade de Argumentos k passados a uma função.
A reutilização diz respeito à criação de funcionalidades que possam ser reutilizadas dentro do sistema, priorizando fatores como:
* Um nível de abstração;

* Tamanho da função;

* Indentação;

* Níveis de aninhamento;

* Efeitos colaterais;

* Parâmetros de saída.

O refatoramento diz respeito à capacidade do sistema em permitir a otimização da estrutura sem que outras funcionalidades sejam afetadas. Nesta etapa são priorizados os seguintes fatores:
* Efeitos colaterais isolados;

* Testes constantes de funcionalidades;

* Refinamento sucessivo.

Readability (legibilidade) - Nomes Significativos

A partir desta introdução aos conceitos da Arquitetura de Software vamos aprofundar nossos conhecimentos sobre a legibilidade do código. Iniciaremos falando sobre a parte mais importante do seu código, nomes. Os nomes dizem muito sobre o desenvolvedor responsável, eles devem expressar as vontades de seu criador, os propósitos para que foi criado e todo o seu apreço pelo projeto. Dizer que os nomes devem demonstrar seu propósito é fácil. Escolher bons nomes leva tempo, mas economiza mais.
Nomes Significativos | Descrição
|

Cuide de seus nomes e troque-os quando encontrar melhores. O nome de uma variável, função ou classe deve responder a todas as grandes questões. Ele deve lhe dizer por que existe, o que faz e como é usado. Exemplo:
Use Nomes que Revelem seu
Propósito

Evite Informações Erradas

Faça Distinções Significativas int d;//tempo decorrido em dias
O nome d não revela nada. Melhores opções:
int elapsedTimelnDays;

int daysSinceCreation;

int daysSinceModification;
int fileAgelnDays;

Deve-se evitar passar dicas falsas que confundam o sentido do código. Devemos evitar palavras cujos significados podem se desviar daquele que desejamos. Por exemplo, hp,aix e sco seriam nomes ruins de variáveis, pois são nomes de plataformas Unix ou variantes. Mesmo se estiver programando uma hipotenusa e hp parecer uma boa abreviação, o nome pode ser mal interpretado.
Lembre-se que ao criar um objeto levamos em conta o nome dado àquela classe, não os comentários ou lista de métodos que ela contém.
As IDE's não possibilitam que dois elementos tenham o mesmo nome, isso implica ao desenvolvedor utilizar nomes semelhantes ou em sequência como: al, a2, a3, esta prática além de dificultar a leitura vai contra a regra anterior. Não há problemas em usar prefixos, porém sempre pensando em distinção significativa, devemos analisar os nomes para retirar trechos desnecessários como ambiguidades.Também devemos evitar palavras muito comuns ou vagas,
pois podem passar ao leitor vários significados e permitir

/ 60

/

Use Nomes Pronunciáveis

Use Nomes Passíveis de Busca

Evite Codificações

Evite Mapeamento Mental que ele entenda da forma que quiser dentro das possibilidades.
Exemplo de classe com nomes não pronunciáveis:
class DtaRcrdlO2 {

};

private Date genymdhms;
private Date modymdhms;

private final String pszqint - "102";

Exemplo com Nomes Pronunciáveis class Customer {
};

private Date generationTimestamp;
private Date modificationTimestamp;
private final String recordld = "102";

Nomes de uma só letra ou números possuem um problema em particular por não ser fácil localizá-los ao longo de um texto. Pode-se usar facilmente o grep paraMAX_CLASSES_PER_STUDENT, mas buscar o número 7
poderia ser mais complicado.

Nomes, definições de constantes e várias outras expressões que possuam tal número, usado para outros propósitos podem ser resultados da busca.
Codificar informações do escopo ou tipos em nomes simplesmente adiciona uma tarefa extra de decifração.
É uma sobrecarga mental desnecessária ao tentar resolver um problema. Nomes codificados raramente são pronunciáveis, além de ser fácil escrevê-los incorretamente.
Devemos evitar a tradução mental de nomes, atribuindo nomes de domínio ou de solução que sejam diretos e objetivos. Esta regra ressalta o problema em utilizar nomes com apenas uma letra, pois permite que seu leitor interprete de maneira livre, apenas levando em conta o conceito contido naquele trecho de código.
De maneira geral, desenvolvedores são muito espertos e provavelmente consigam mapear uma variável apenas pelo contexto do trecho, porém devemos pensar em todos os possíveis leitores. Uma diferença entre um programador esperto e um programador profissional é o entendimento sobre a clareza em que expressa seu código.
Classes e objetos devem ter nomes com substantivo(s),
como Cliente, PaginaWiki, Conta e AnaliseEndereco. Evite palavras como Gerente, Processador, Dados ou Info no nome de uma classe, que também não deve ser um verbo.
Os nomes de métodos devem ter verbos, como postarPagamento, excluirPagina ou salvar. Devem-se nomear métodos de acesso, alteração e autenticação segundo seus valores e adicionar os prefixos get, set ou is de acordo com o padrão javabean.*
Faça uma análise de palavras do domínio e coloque um padrão na utilização de conceitos. Por exemplo, é confuso utilizar pegar, recuperar e obter como métodos equivalentes em classes diferentes. Os ambientes de desenvolvimento, como o Eclipse ou IntelliJ, oferecem dicas relacionadas ao contexto como listas com métodos e nomes de variáveis que você pode chamar em determinado objeto.Mas devemos notar que a lista retornada não oferece os comentários sobre a função, então deve-se ter clareza na escolha dos nomes para que nesta etapa não seja necessário revisar trechos de código.
Lembre-se sempre de que serão programadores que lerão seu código, então utilize termos da área, nomes de padrões e termos matemáticos. Não é prudente utilizar um nome a partir do domínio do problema, pois seria um transtorno identificar o conceito do problema para saber o significado do nome.
Nomes como AccountVisitor ou JobQueue se expressam muito bem ao programador, então nomes técnicos,normalmente, são os mais adequados.

Há poucos nomes significativos por si só, portanto devemos utilizar nomes que tragam contexto ao leitor. Utilize nomes expressivos e que se complementam para formar uma linha de raciocínio, os nomes em uma classe devem se complementar e transmitir a ideia de seu desenvolvedor.
Em sistemas desenvolvidos no domínio da AZ, seria uma péssima ideia adicionar prefixos "AZ" em todas as classes.Este contexto adicionado vai contra as suas ferramentas,
pois a busca resultará um resultado enorme de todas as classes que tenham o prefixo.
/ 60

Nomes curtos geralmente são melhores, apenas precisam ser claros. Sempre revize seu código e melhore os nomes utilizados, gaste um tempo a mais com o objetivo de criar um código legível.
Para criar nomes que revelem seu propósito devemos seguir os seguintes conceitos:

* Nomes de variáveis devem informar seu conteúdo ou sua finalidade.

* Nomes de funções devem informar a atividade executada pela função.

* Nomes bons dispensam comentários, sempre troque comentários sobre variáveis por um nome que facilite o entendimento.
* Faça um bom uso do Naming Convention. Nomes de constantes no padrão SNAKE_CASE e demais nomes no padrão CamelCase.
/ 60

/

Reusability (Reuso) - Reutilização de funcionalidades

A primeira regra para funções é que elas devem ser pequenas. A segunda é que precisam ser mais espertas do que isso. De acordo com o autor do livro Clean Code, por cerca de quatro décadas criando funções de tamanhos variados. Essa experiência ensinou que, ao longo de muitas tentativas e erros, as funções devem ser muito pequenas.
Por outro lado, quando se trata de reutilização de funcionalidades, temos as seguintes diretrizes:

Reutilização de funcionalidades
Funções Devem ser pequenas

Blocos de endentação

Faça apenas uma coisa

Um nível de abstração por função

Descrição

O livro aconselha a construirfunções cada vez menores, pois são mais fáceis de realizar manutenção. A recomendação é:As funções devem ter no máximo 20 linhas.

É fortemente recomendado que blocos dentro de instruções if, else, while e outros devem ter apenas uma linha, possivelmente seja uma chamada de outra função.Esta recomendação mantém a função pequena e adiciona um valor significativo
Esta recomendação também implica que as funções não devem ser grandes e possuir vários níveis de aninhamento,ocasionando em um nível de indentação de no máximo dois blocos.
No SRP (Princípio de Responsabilidade Única) há uma regra sobre funções de uma única ação. Quando se tem mais de uma ação sendo executada dentro de uma única função pode-se gerar erros difíceis de serem encontrados e é mais propenso a erros. As funções devem fazer uma coisa e devem fazê-la bem.
No início do projeto pode-se realizar um mapeamento de ações que devem ser implementados e por meio desse mapeamento podemos decompor as ações em funções menores, pensando sempre em fazer apenas uma ação.
A fim de confirmar se nossa função tem uma responsabilidade, é necessário verificar se todas as instruções dentro da função estão no mesmo nível de abstração. O nível de abstração diz respeito aos conceitos implementados dentro da função, deve-se deixar bem claro
/ 60

/

o nível de importância sobre aquele trecho separando meros detalhes de conceitos extremamente importantes.
Regra decrescente

Use nomes descritivos

Como em uma narrativa, queremos que o código seja lido de cima para baixo e que cada próximo conceito passe a ideia de um contexto maior que se complementa a cada novo trecho. Cada parágrafo deve descrever o nível atual e fazer referência aos parágrafos consecutivos do próximo nível. Temos a orientação da leitura nas direções da esquerda para a direita e de cima para baixo, devemos facilitar aos usuários a leitura dessa forma padrão.
NOVAMENTE! Os nomes atribuídos às funções devem ses autoexplicativos e claros, devem transmitir ao leitor a ideia colocada pelo desenvolvedor dentro daquela função. Não tenha medo de criar nomes extensos para as funções, pois estes são melhores que nomes pequenos e enigmáticos e também poupa o trabalho de adicionar comentários de descrição sobre as funções. Lembre-se sempre das convenções de nomenclaturas, elas possibilitam a melhor leitura dos nomes.
Parâmetros de funções

Funções mônades comuns

Parâmetros lógicos

A quantidade ideal de parâmetros para uma função é de zero, seguida por um parâmetro, depois dois parâmetros e assim por diante. Deve-se, sempre que possível, evitar funções com três parâmetros, apenas com motivos muito especiais devemos ignorar essa regra. Esta regra é imposta por ser uma tarefa difícil complementar o nome da função com os nomes dos parâmetros.
As funções citadas no livro como mônades, são funções que possuem um único parâmetro. Elas são utilizadas quando,você está fazendo uma pergunta sobre aquele parâmetro,
como em boolean fileExists("Myfile"), ou você pode trabalhar sobre aquele parâmetro transformando-o em outro elemento ou retornando-o.
Mais conhecidos como flags, não passam de valores booleanos passados a uma função. Certamente é uma prática horrível, pois viola a regra de que a função deve ter apenas uma responsabilidade, caso o valor seja falso ela terá um comportamento, caso contrário será outro comportamento diferente. O ideal é que sejam divididas em duas funções que são responsáveis para cada estado da flag.
Funções díades possuem uma dificuldade maior na leitura em comparação com funções mônades. Há casos que dois parâmetros são necessários e devemos realizar uma análise sobre os parâmetros passados, filtrando a utilização apenas em casos que os parâmetros são valores independentes e necessários.
Devemos evitar ao máximo o uso desse tipo de funções,
além de ser consideravelmente mais difíceis de entender,
ainda possuem questões de ordenação e pausa que são mais recorrentes.
Efeitos colaterais são mentiras ocasionadas pelo contexto da função. Se sua função atende a regra de fazer apenas uma coisa, não teremos efeitos colaterais pois sabemos bem o que está sendo executado. Ações a mais em uma função podem fazer alterações desnecessárias aos parâmetros conhecidos, sejam os da função ou globais.
As funções devem fazer ou responder algo, nunca ambos.
Lembre-se de criar funcionalidades fazendo a separação entre a alteração de informações e retorno delas, efetuar as duas tarefas costuma gerar confusão.
Faça uma análise das funcionalidades implementadas e caso note a semelhança entre ações, transforme em uma só. Aduplicação no código pode passar despercebida e isso leva a maiores oportunidades para a omissão de erros.
A duplicação pode ser a raiz de todo o mal no software,
muitos princípios e práticas têm sido criados com a finalidade de controlá-la ou eliminá-la.Considere que a programação orientada a objeto serve para centralizar o código em classes-base que seriam redundantes em outro conceito.
*

i (CESPE - TJ AM - 2019) De acordo com Clean Code, julgue o item subsecutivo.

,.Z 60

i Independentemente da linguagem de programação, uma função deve executar todos os i i procedimentos que estão sintetizados no seu nome, gerando uma função com múltiplos passos.
i Comentários: Quando falamos sobre Reutilização de funcionalidades, vimos que funções devem ser ;
í pequenas, devem fazer apenas uma coisa. Portanto, essa questão está errada! (Gabarito: Errado) i x
,.Z 60

/

Refatoring (refatoração) - Otimização da estrutura

Nada pode sertão útil quanto um comentário bem colocado.
Porém nada pode ser tão prejudicial quanto comentários desnecessários e supérfluos, no máximo os comentários são um mal necessário.
O uso adequado de comentários compensa nosso fracasso em nos expressar no código, comentários são utilizados quando não encontramos outra forma de nos expressar adequadamente. Portanto, quando você estiver numa situação na qual precise criar um comentário, pense bem e veja se não há uma maneira melhor de se expressar através do código.
Ao utilizar comentários lembre-se de que as tecnologias estão em constante evolução e seus comentários podem se tornar antiquados ou desatualizados. Muitas das vezes os comentários mentem, quanto mais antigo e mais longe do trecho que ele descreve, mais provável que esteja errado.
Comentários Compensam um Código Ruim

Uma das motivações mais comuns para criar comentários é um código ruim. Temos ciência da bagunça que criamos e adicionamos um comentário com o pensamento de que o código será melhor, quando na verdade ainda temos um código ruim sendo poluído com comentários ruins.
Códigos claros e expressivos com poucos comentários são de longe superiores a um amontoado e complexo com muitos comentários. Ao invés de perder seu tempo criando comentários utilize para limpar e melhorar o código.
Explique-se no Código

Há vezes em que não é possível se expressar direito no código. Infelizmente muitos programadores assumiram que o código é um bom meio para se explicar.
//verifica se o funcionário é apto aos benefícios if ((employee.flags & HOURLY_FLAG) &&
(employee.age > 65))

if (employee. is EligibleFor FullBenefitsQ)

Passe algum tempo pensando em como ter expressividade no seu código, com certeza não será um tempo perdido. Muitas das vezes a mudança é apenas nomear as funções com o que você tem em mente para um comentário.
Comentários bons

Certos comentários são necessários ou benéficos. Entretanto tenha em mente que o único comentário verdadeiramente bom é aquele em que você encontrou uma forma de não o escrever.
Descrição

Às vezes nossos padrões de programação corporativa nos forçam a escrever certos comentários por questões legais.Então devemos adicionar um comentário padrão no cabeçalho dos arquivos, contendo as informações sobre direitos autorais da aplicação.
Sempre que possível coloque estes comentários em arquivos externos.
Às vezes precisamos fornecer informações básicas sobre uma funcionalidade, seja pelo valor ou pelo formato retornado pelas variáveis, caso o nome da função já informe o leitor, então deve-se ignorar o comentário, mas é aceitável criar um comentário informativo para esta situação.
Muitas vezes um comentário vai além de ser apenas informações úteis sobre a implementação, ele fornece a intenção por trás de uma decisão. O esclarecimento sobre a utilização de parâmetros também é aceitável.
As consequências da execução e manutenção de determinados trechos podem estar em comentários. Ocomentário pode auxiliar o leitor a identificar as consequências e permite uma ação prévia, como:
Wexecute apenas se tiver tempo disponível await browser.waitFor( 1000000000);
Os comentários podem elencar os próximos passos a fazer.
TODOs são tarefas que os programadores acham que devem ser efetuadas, mas por alguma razão não podem implementá-las no momento. Podem ser um lembrete
/ 60

/

sobre uma alteração que deve ser feita, um pedido para a verificação de outro membro.
Hoje em dia, a maioria das IDEs oferecem ferramentas e recursos para localizar os comentários TODO; portanto não é provável que fiquem perdidos no código. Revise regularmente seu código e elimine os comentários TODO.
Comentários Ruins

Quase todos os comentários caem nesta categoria, geralmente os comentários se tornam suporte ou desculpas para um código de baixa qualidade.
Tipo de comentário ruim | Descrição
|
Usar um comentário que não fará sentido ao leitor,
simplesmente é um comentário sobre as frustrações na

Murmúrio hora da codificação são tidos como murmúrios e não agregam valor ao projeto.
Comentários Enganadores

Às vezes, mesmo com as melhores intenções, o programador faz uma afirmação não muito clara em seus comentários. Uma pequena desinformação expressada em comentário pode dificultar a leitura e provocar erros futuros.
Comentários ruidosos

Por vezes os comentários não são nada além de chiados,
que dizem obviedades e não fornecem novas informações sobre o código. Estes comentários levam ao leitor a ignorá-los, com o tempo os olhos passam direto por eles e conforme a manutenção do código estes comentários passam a mentir.
Marcadores de Posição

Alguns programadores gostam de marcar uma posição determinada no arquivo fonte, como:
for(var i in itens){

/-./

}//for////

Raramente as junções por comentários fazem sentido em certas funções, mas de modo geral eles são aglomerações e devemos excluí-los. Tenha em mente que indicadores são
/ 60

/

chamativos no código, use-os esporadicamente para não se tornarem ruídos.
Código em comentários

Informações não-locais

Cabeçalhos de funções e fechamentos
Nunca, nunca mesmo, deixe código comentado no corpo de seu arquivo. Outros desenvolvedores que tiverem o contato com esse código não teriam coragem de excluir os comentários, pois passam a impressão de que estão lá por um motivo e são importantes demais para serem apagados.Essa prática tende a acumular comentários desnecessários e leva o leitor à uma confusão.
O comentário deve estar próximo ao código que ele descreve. Não forneça informações gerais do sistema no contexto de um comentário local. Considere por exemplo o comentário do Javadoc abaixo. Além de ser terrivelmente redundante, ele também fala sobre uma porta padrão que a função ainda não tem acesso.
É muito comum adicionarmos cabeçalhos em funções para passar alguma informação sobre a próxima função, porém funções curtas não requerem muita explicação. Um nome bem selecionado costuma ser melhor do que um comentário no cabeçalho.
Também são desnecessários os comentários de fechamento das ações e blocos, eles não contribuem em nenhum aspecto. Uma boa formatação substitui os comentários de fechamento.
Entretanto, há situações em que é recomendado fazer uso dos comentários, como:

* Legal Comments: copyright e authorship podem ser necessários e razoáveis de se colocar no início de cada arquivo.
* Informative Comments: por exemplo, explicando o formato aceito por uma expressão regular.
* Explanation of Intent: explicar a intenção por trás de uma decisão.

* Clarification: quando o código não puder ser modificado e algo obscuro necessitar ser explicado.
* Warning of Consequences: avisar os efeitos colaterais de se executar um método.Ex: Test case demorado.
/ 60

/

* TODO Comments: não é uma desculpa para deixar código ruim no sistema. Serve como um lembrete.
* Amplification: amplifica a importância de uma ação que caso contrário poderia parecer sem importância.
Formatação

Quando as pessoas olham nosso código desejamos que fiquem impressionadas com a clareza,consistência e a atenção aos detalhes presentes. Queremos passar toda a organização, o apreço e o profissionalismo que aplicamos na criação do projeto.
Você deve tomar conta para que seu código fique bem formatado, escolher uma série de regras simples que governem seu código e aplicá-las de forma consistente. Estas regras devem ser tomadas pela equipe, se for o caso, e todo o projeto deve girar em torno dessas regras.
O Objetivo da Formatação

A formatação do código é importante. Ela serve como uma comunicação e é a primeira regra para um desenvolvedor profissional. A funcionalidade que você cria tem grandes chances de ser modificada na próxima manutenção, mas a legibilidade do seu código terá um grande efeito sobre essas modificações, então se preocupe com a legibilidade. Seu estilo e disciplina sobrevivem, mesmo que seu código não.
Faça uma boa utilização das Naming Conventions, temos alguns padrões para as linguagens que facilitam a leitura.
Os principais padrões de Naming Conventions para o java são:

* CamelCase - Utilizado para nomearfunções e variáveis, este padrão remete que são utilizadas palavras compostas e faz a distinção por iniciais em maiúsculo. EX: daysInMonth.
* SNAKE_CASE - Utilizado para nomear constantes, este padrão é normalmente utilizado com todos os caracteres em maiúsculo e um para a separação das palavras compostas, como no exemplo a seguir:
Ruim:

const DAYS_IN_WEEK = 7;
const daysInMonth = 30;

const songs = ['Back In Black', 'Stairway to Heaven',
'Hey 3ude'];

const Artists = ['ACDC, ' Led Zeppelin', 'The Beatles'];

/ 60

/

function eraseDatabase() {}
function restore_database() {}

class animal {}
class Alpaca {}

Bom:

const DAYS_IN_WEEK = 7;
const DAYS_IN_MONTH = 30;

const SONGS = ['Back In Black', 'Stairway to Heaven',
'Hey Jude'];

const ARTISTS = ['ACDCj ' Led Zeppelin', 'The Beatles'];

function eraseDatabase() {}
function restoreDatabase() {}

class Animal {}
class Alpaca {}

Tipos de Formatação

Formatação Vertical

Espaçamento vertical entre conceitos
Descrição

O seu código-fonte deve ser de que tamanho? O Robert responde a essa questão, o número máximo deve ser de 500linhas. Há uma grande diversidade de tamanhos e algumas diferenças notáveis em estilo. No livro são elencados sete projetos diferentes: JUnit, FitNesse, testNG, Time andMoney, JDepend, Ant e Tomcat. As linhas verticais de todos eles atendem ao máximo de 500 linha e o mínimo encontrado foi um arquivo de 6 linhas.
A partir destes exemplos podemos dizer que é possível construir sistemas significativos a partir de códigos simples de 200 linhas, com um limite máximo de 500. Arquivos pequenos costumam ser mais fáceis de se entender.
Quase todo o código é lido da esquerda para a direita e de cima para baixo. Todas as linhas representam expressões e estruturas, cada grupo de linhas representa um pensamento completo. A cada pensamento escrito no código devemos separar por uma linha em branco, isso facilita a leitura e cria uma separação entre os conceitos.
/ 60

/

Continuidade Vertical

Distância vertical

Formatação horizontal

Se o espaçamento separa conceitos, então a continuidade vertical indica uma associação íntima entre o código. Assim,linhas de código que possuem relação dos conceitos devem aparecer verticalmente unidas. Note no exemplo acima que os elementos de um mesmo conceito estão próximos,enquanto outros possuem o espaçamento de 1 linha.

A equipe de desenvolvimento deve elaborar regras para a codificação. O livro cita algumas regras que são utilizadas como padrão sobre distância vertical, são:
declaração de variáveis: Deve ser o mais próximo do local onde serão utilizadas, como pretendemos criar funções pequenas as variáveis devem estar no topo.
Instância de variáveis: Deve ocorrer no início da classe. Há muita discussão sobre a posição das instâncias, em C++ é comum a regra da tesoura, na qual colocamos todas no final da classe. O Java a convenção é colocá-las no início da classe.
Funções dependentes: Se uma função chama outra, elas devem ficar verticalmente próximas e a que chamar deve ficar acima da função que é chamada. Essa recomendação permite que o leitor se localize no código por meio das funções, quando há uma chamada é esperado que a outra função esteja abaixo.
Afinidade conceituai: Quanto maior a afinidade entre as funcionalidades, menor deve ser a distância entre elas. Aafinidade conceituai pode ser definida por meio de funcionalidades que se complementam, mesmas tarefas básicas ou chamadas.
Após falarmos sobre o tamanho do arquivo e o espaçamento vertical, podemos entrar no debate sobre o tamanho horizontal do código. Qual deve ser o tamanho de uma linha? Novamente analisando os sete projetos citados no livro temos uma regularidade com cerca de 45caracteres, nestes projetos os desenvolvedores claramente preferem linhas curtas.
/ 60

/

É aceitável que o tamanho de uma linha seja de 100 a 120
caracteres, porém é totalmente desnecessário ter de rolar a tela para a direita para acessar informações.
Um arquivo é mais como uma hierarquia do que algo esquematizado. Há informações sobre o arquivo como um todo, às classes individuais, aos métodos dentro das classes e blocos de cada método.
Indentação

Regras de equipes

A fim de tornar visível a hierarquia desses escopos,
indentamos as linhas de nosso código de acordo com sua posição na hierarquia. Classes e instruções a nível do arquivo não necessitam de indentação, métodos dentro de uma classe são indentados um nível à direita e assim consecutivamente.
Os programadores dependem muito desse esquema de indentação, eles alinham visualmente na esquerda as linhas para ver em qual escopo elas estão. Esta técnica permite que escopos desnecessários ao leitor sejam pulados como as estruturas de if e while. Procuram mais a esquerda por novas declarações de métodos, novas variáveis e até novas classes.
A equipe de desenvolvedores deve escolher um único estilo de formatação para ser utilizado no projeto. O estilo deve ser consistente, não queremos que pensem que o código foi escrito por uma equipe em desacordo sobre as definições.
Lembre-se: um bom software é composto de uma série de documentos de fácil leitura. Eles também necessitam ter um estilo consistente e sutil. O leitor precisa confiar que a formatação sempre irá transmitir as mesmas informações.
Sugestões para criar um código que seja limpo, robusto, que trate erros com elegância e estilo:

Exceções Descrição

,.Z 60

/

Use exceções ao invés de retornar código de erro
É melhor lançar uma exceção quando um erro for encontrado, o código de chamada fica mais limpo e sua lógica não é ofuscada pelo tratamento de erro.
Crie primeiro sua estrutura try-
catch-finally

O bloco try funciona como uma transação que pode ser cancelada a qualquer momento e deve continuar no bloco catch. O bloco catch deve deixar seu programa num estado mais consistente sem se importar com o que aconteça no try. Por isso é recomendável que as funcionalidades que possuem a probabilidade de gerar erros sejam iniciadas por blocos try-catch, isso ajuda a definir o que o usuário deve esperar, independente do que ocorre no try.
Não passe ou retorne Null

Utilize Exceções não verificadas

Quando retornamos null estamos criando problemas para a execução, basta esquecer uma verificação e tudo irá por água abaixo.
Não passe null, a menos que esteja trabalhando com uma
API que espere receber null. Passando valores null a única certeza que temos é de que será lançada umaNulIPointerException. Na maioria das linguagens não há uma boa forma de lidar com valores nulos passados acidentalmente para uma chamada.
As exceções checadas surgiram com a primeira versão do java, de fato era uma ótima ideia carregar uma lista de exceções juntamente com a assinatura de um método.Desta maneira todas as assinaturas de exceções conhecidas pelo sistema serão notificadas ao usuário sempre que fossem necessárias.
O preço de se utilizar exceções checadas é a necessidade de assinalar ao Caller todas as vezes que for utilizar o método,assim poluindo a interface. Uma saída para o problema em utilizar exceções checadas é transformá-las em exceções não checadas por meio da RuntimeException.
r«*

: (CESPE - MPE CE - 2020) Julgue o seguinte item, relativo a métricas de qualidade de código, clean i i code e refactoring.
I

í Pela perspectiva do clean code, é recomendado usar exceções (try/catch, por exemplo)
em vez de j

: testar vários códigos de erros ou, ainda, retornar null.
i

,.Z 60

/

i Comentários: Pessoal, de acordo com o que vimos no conteúdo, algumas das recomendações são:i Crie primeiro sua estrutura try-catch-finally; Não passe ou retorne Null. (Gabarito: Correto)

Objetos e Estruturas de Dados

Os objetos expõem as ações e ocultam os dados. Isso facilita a adição de novos tipos de objetos sem precisar modificar as ações existentes e dificulta a inclusão de novas atividades em objetos existentes.
As estruturas de dados expõem os dados e não possuem ações significativas. Isso facilita a adição de novas ações às estruturas de dados existentes e dificulta a inclusão de novas estruturas de dados em funções existentes.
Em um dado sistema, às vezes, desejaremos flexibilidade para adicionar novos tipos de dados, e,portanto, optaremos por objetos. Em outras ocasiões, desejaremos querer flexibilidade para adicionar novas ações, e, portanto, optaremos por tipos de dados e procedimentos.
Bons desenvolvedores de software entendem essas questões sem preconceito e selecionam a abordagem que melhor se aplica no momento.
Pessoal, as bancas estão aprofundando cada vez mais na cobrança, veja a questão abaixo e estude com afinco os tópicos seguintes descritos na tabela - pode cair na sua prova, como já caiu em provas anteriores!
: (CESPE - TCE - PA - 2016) No contexto de clean code, o conceito de objetos é semelhante ao de i estruturas de dados, devendo os dados e as funções ficar expostos para permitir a inclusão de novos i i dados e de novas funções.
I

I

i Comentários: Pessoal, os objetos usam abstrações para esconder seus dados, e expõem as funções i i que operam em tais dados. As estruturas de dados expõem seus dados e não possuem funções i i significativas. Note a natureza complementar das duas definições. Elas são praticamente opostas i i (Gabarito: Errado)
Objetos e Estruturas de Dados | Descrição

Os objetos usam abstrações para esconder seus dados, e

Anti-simetria data/objeto expõem as funções que operam em tais dados. As estruturas de dados expõem seus dados e não possuem funções significativas.
/ 60

/

Note a natureza complementar das duas definições. Elas são praticamente opostas. Essa diferença pode parecer trivial,mas possui grandes implicações.

A lei de Demeter

Carrinhos de trem

Híbridos

Um módulo não deve enxergar o interior dos objetos que ele manipula. Os objetos escondem seus dados e expõem as operações. Isso significa que um objeto não deve expor sua estrutura interna por meio dos métodos acessores, pois isso seria expor, e não ocultar, sua estrutura interna. Mais precisamente, a Lei de Demeter diz que um método f de uma classe C só deve chamar os métodos de:
-C

- Um objeto criado por f

- Um objeto passado como parâmetro para f

- Um objeto dentro de uma instância da variável C

O método não deve chamar os métodos em objetos retornados por qualquer outra das funções permitidas. Em outras palavras, fale apenas com conhecidos, não com estranhos.
Esse tipo de código costuma ser chamador de carrinho de trem, pois parece com um monte de carrinhos de trem acoplados. Cadeias de chamadas como essa geralmente são consideradas descuidadas e devem ser evitadas. Na maioria das vezes é melhor dividi-las.
Estruturas híbridas ruins são metade objeto e metade estrutura de dados. Elas possuem funções que fazem algo significativo, e também variáveis ou métodos de acesso e de alteração públicos que, para todos os efeitos, tornam públicas as variáveis privadas, incitando outras funções externas a usarem tais variáveis da forma como um programa procedimental usaria uma estrutura de dados".
Esses híbridos dificultam tanto a adição de novas funções como de novas estruturas de dados. Eles são a pior coisa em ambas as condições. Evite criá-los. Eles indicam um modelo confuso cujos autores não tinham certeza - ou pior, não sabiam se precisavam se proteger de funções ou tipos.
Estruturas Ocultas

Objetos de transferência de dados

O Active Record

A mistura adicionada de diferentes níveis de detalhes é um pouco confusa. Pontos, barras, extensão de arquivos e objetos não devem ser misturadas entre si e nem com o código que os circunda.
A forma perfeita de uma estrutura de dados é uma classe com variáveis públicas e nenhuma função. Às vezes, chama-se isso de objeto de transferência de dados, ou DTO (sigla em inglês). Os DTOs são estruturas muitos úteis,especialmente para se comunicar com bancos de dados ou analisar sintaticamente de mensagens provenientes de sockets e assim por diante. Eles costumam se tornar os primeiros numa série de estágios de tradução que convertem dados brutos num banco de dados em objetos no código do aplicativo.
Os beans têm variáveis privadas manipuladas por métodos de escrita e leitura. O aparente encapsulamento dos beans parece fazer alguns puristas da 00 sentirem-se melhores,mas geralmente não oferece vantagem alguma.

Os Active Records são formas especiais de DTOS. Eles são estruturas de dados com variáveis públicas (ou acessadas por Beans); mas eles tipicamente possuem métodos de navegação, como save (salvar) e find (buscar). Esses ActiveRecords são traduções diretas das tabelas de bancos de dados ou de outras fontes de dados.
Infelizmente, costumamos encontrar desenvolvedores tentando tratar essas estruturas de dados como se fossem objetos, colocando métodos de regras de negócios neles.Isso é complicado, pois cria um híbrido entre uma estrutura de dados e um objeto. A solução, é claro, é tratar o RecordActive como uma estrutura de dados e criar objetos separados que contenham as regras de negócio e que ocultem seus dados internos (que provavelmente são apenas instâncias do Active Record).
/ 60

/

QUESTõES CoMENTADAS - CLEAN CoDE

1. (CESPE - DP DF- 2022) Julgue o próximo item, relativo à análise estática de código fonte.

A seguir, é apresentado um bom exemplo de código, de acordo com clean code.

int a = 1;

if ( o == 1 )

a = 01;

else

1 = 01;

Comentários

A questão diz que "é apresentado um bom exemplo de código". Dá uma olhada no código e me diga o que entendeu? Não há muita clareza não é mesmo? Acha que esse código tem consistência de expressão? Nomes significativos? Não né? Portanto essa questão está errada.
Gabarito: Errado

2. (CESPE -TJ PA - 2020) O Clean Code deve considerar também o momento de teste do software em desenvolvimento. O Teste Limpo deve
O texto acima refere-se a qual metodologia de análise e projeto de software?

a) ser o mais completo possível, para que não seja necessário repeti-lo muitas vezes.

b) ser específico para determinado ambiente.

c) ser executado de forma que os testes sejam escritos antes que o código a ser testado esteja no ambiente de produção.
d) produzir resultados com respostas o mais abertas possível, para garantir eficiência ao processo.
e) contemplar todas as dependências possíveis, para garantir a eficácia do processo de testes.

Comentários:

Vamos analisar cada alternativa. A letra a está errada, porque, na verdade, os testes devem ser repetidos, e executados diversas vezes. Ao contrário do que diz a questão: " não seja necessário repeti-lo muitas vezes". A letra b está incorreta, na verdade, o teste limpo deve ser feito para qualquer ambiente, não como diz a questão "ser específico para determinado ambiente". Aletra C
está correta, é exatamente o que preconiza as metodologias ágeis: Teste Limpo deve ser executado de forma que os testes sejam escritos antes que o código a ser testado esteja no ambiente de produção. A alternativa d também está errada, na verdade, o teste deve ser objetivo e não subjetivo.Por fim, a alternativa e está errada. Um teste limpo não deve contemplar todas as dependências.

Gabarito: Letra C

3. (CESPE - MPE CE - 2020) Julgue o seguinte item, relativo a métricas de qualidade de código,
clean code e refactoring.

Pela perspectiva do clean code, é recomendado usar exceções (try/catch, por exemplo) em vez de testar vários códigos de erros ou, ainda, retornar null.
Comentários: Pessoal, de acordo com o que vimos no conteúdo, algumas das recomendações são:Crie primeiro sua estrutura try-catch-finally; Não passe ou retorne Null.

Gabarito: Correto

4. (CESPE - TJ AM - 2019) De acordo com Clean Code, julgue o item subsecutivo.

Independentemente da linguagem de programação, uma função deve executar todos os procedimentos que estão sintetizados no seu nome, gerando uma função com múltiplos passos.
Comentários

Quando falamos sobre Reutilização de funcionalidades, vimos que funções devem ser pequenas,devem fazer apenas uma coisa. Portanto, essa questão está errada!

Gabarito: Errado

5. (CESPE - TJ AM- 2019) De acordo com Clean Code, julgue o item subsecutivo.

Comentários explicativos ou descritivos no código devem ser evitados, pois caracterizam um código ruim.
Comentários: Códigos com muitos comentários são tão ruidosos que, com o tempo, nossos olhos acabam ignorando todos. Então, o melhor não é comentar os códigos ruins e sim reescrevê-los.
Gabarito: Correto

6. (CESPE - TJ AM- 2019) De acordo com Clean Code, julgue o item subsecutivo.

Em códigos orientados a objeto, tanto objetos quanto estruturas de dados expõem seus dados internos e as funções que manipulam tais dados.
Comentários:

/ 60

/

Questão errada! Vocês se lembram do conceito de Encapsulamento? Aquela técnica que faz com que detalhes internos do funcionamento dos métodos de uma classe permaneça ocultos para os objetos. Por conta dessa técnica, o conhecimento a respeito da implementação interna da classe é desnecessário do ponto de vista do objeto, uma vez que isso passa a ser responsabilidade dos métodos internos da classe. Portanto, o que é apresentado pela questão não é o recomendado.
Gabarito: Errado

7. (CESPE - TRE PE - 2017) Acerca do clean code, assinale a opção correta.

a) Para se evitar a proliferação de funções curtas, recomenda-se o uso de uma função longa com muitas variáveis globais, cada qual com variáveis locais de pouco uso.
b) O uso de um código que contenha as letras I e O como variáveis é mais recomendado que o uso de um código cujas variáveis sejam contador e resultado, por exemplo.
c) Os atuais ambientes de programação permitem que um único arquivo de código-fonte seja desenvolvido em diferentes linguagens, embora o ideal seja que um código-fonte contenha apenas uma linguagem.
d) A fim de facilitar o entendimento do código pelos desenvolvedores,
recomenda-se utilizar gírias locais para nomear funções, sempre que possível.
e) Na análise léxica, o uso de uma mesma palavra para dois ou mais propósitos facilita a compilação de código, diminui o código e aumenta a velocidade dos objetos binários compilados.
Comentários:

Questão longa, vamos analisar cada alternativa. A está errada. Deve-se usar funções curtas. B está errada. Não é recomendado utilizar "letras", o ideal é utilizar NomesSignificativos, Nomes que
Revelem seu Propósito. A alternativa C está correta! Os atuais ambientes de programação permitem que um único arquivo de código-fonte seja desenvolvido em diferentes linguagens, embora o ideal seja que um código-fonte contenha apenas uma linguagem. Um software contendo apenas uma linguagem é muito mais limpo, facilitando a manutenção e o desenvolvimento. Aalternativa d também está incorreta. Métodos ou Funções devem ter nome de verbos, para assim,expressar quais são suas finalidades. Por fim, a alternativa e está incorreta: O Clean Code utiliza o conceito de DRY.DRY é o acrônimo para Don't repeat yourself (Não repita a si mesmo). É o conceito que diz que cada parte de conhecimento do sistema deve possuir apenas uma representação. Desta forma,evitando a ambiguidade do código, não deve existir duas partes do programa que desempenham a mesma função ou tenham o mesmo nome, ou seja, o famoso copiar e colar no código.
Gabarito: Letra C

8. (FCC - DPE RS- 2017) Considere os trechos de código em que // indica comentário. Aplica corretamente as regras de Clean Code o trecho de código:
a) Trecho 1:

/ 60

/

var a = (b + c)/d -10; // coloca o resultado em a b) Trecho 2:
//Valida se o cliente possui benefícios de acordo com a tabela de regras if ((cliente.Idade > 45 && cliente.Salario < enumValorSalarios.SalarioMinimo)
c) Trecho 3:

if (Ivisitante.EhAdulto && Ivisitante.EstaBloqueado) // lógica inversa return "Você não tem acesso por não ser adulto ou está bloqueado para ver este conteúdo";else return "Ótimo! Você poderá acessar este conteúdo.";
d) Trecho 4:

Reg regCPF = new Reg(@"A\d{3}\.\d{3}\.\d{3}-\d{2}$"); // 999.999.99
Reg regTelefone = new Reg(@"A\(\d{2}\)\d{4}-\d{4}$"); // (99)9999-9999

e) Trecho 5:

var textoContrato = RemoveHtml(contrato); //conforme ETC
EnviaContratoPorEmail(textoContrato);

textoContrato = textoContrato.FTC(".", ==","=").FTC("-",

Comentários:

Pessoal, os comentários das alternativas a, b e c e e não estão listados nas regras em que se deve realizar um comentário. A alternativa d apresenta comentários explicando o formato aceito por uma expressão regular, que consiste da regra Informative Comments.
Gabarito: Letra D

9. (CESPE - TCE-SC- 2016) A respeito da análise estática de código-fonte em Clean
Code e
SonarQube, julgue o item subsecutivo.

De acordo com as diretivas do Clean Code, o número de argumentos de uma função não deve ser igual ou superior a três, devido a sua influência no entendimento da função.
Comentários:

Pessoal, vamos relembrar as diretrizes do Clean Code no aspecto Reusabilidade? De acordo com a diretriz Parâmetros de funções, a quantidade ideal de parâmetros para uma função é de zero,seguida por um parâmetro, depois dois parâmetros e assim por diante. Deve-se,
sempre que possível, evitar funções com três parâmetros, apenas com motivos muito especiais devemos ignorar essa regra.
Gabarito: Correto

/ 60

/

10. (CESPE -TCE-PA- 2016) Acerca de análise estática de código-fonte, uma das práticas que verifica a qualidade do código e pode ser realizada antes da execução do software, julgue o próximo item.
De acordo com as práticas de clean code, comentários em um código-fonte servem para compensar um código mal escrito, devendo, portanto, ser evitados.
Comentários:

Alguns comentários são necessários ou benéficos. Mas o melhor é que você não precisa escrever.Uma das motivações mais comuns para criar comentários é um código ruim. Temos ciência da bagunça que criamos e adicionamos um comentário com o pensamento de que o código será melhor, quando na verdade ainda temos um código ruim sendo poluído com comentários ruins.Códigos claros e expressivos com poucos comentários são de longe superiores a um amontoado e complexo com muitos comentários. Ao invés de perder seu tempo criando comentários utilize para limpar e melhorar o código. Ou seja, reescreve o código! A questão está errada porque diz que comentários em um código-fonte servem para compensar um código mal escrito,devendo,
portanto, ser evitados.

Gabarito: Errado

11. (CESPE-TCE-PA-2016) Acerca de análise estática de código-fonte, uma das práticas que verifica a qualidade do código e pode ser realizada antes da execução do software, julgue o próximo item.
No contexto de clean code, o conceito de objetos é semelhante ao de estruturas de dados,devendo os dados e as funções ficar expostos para permitir a inclusão de novos dados e de novas funções.
Comentários:

Pessoal, os objetos usam abstrações para esconder seus dados, e expõem as funções que operam em tais dados. As estruturas de dados expõem seus dados e não possuem funções significativas.Note a natureza complementar das duas definições. Elas são praticamente opostas.

Gabarito: Errado

12. (CESPE-TCE-PA-2016) Acerca de análise estática de código-fonte, uma das práticas que verifica a qualidade do código e pode ser realizada antes da execução do software, julgue o próximo item.
As práticas de clean code recomendam que as funções tenham, no máximo, vinte linhas,
e até dois níveis de indentação.
/ 60

/

Comentários:

Funções Devem ser pequenas: O livro aconselha a construir funções cada vez menores, pois são mais fáceis de realizar manutenção. A recomendação é: As funções devem ter no máximo 20linhas.
Ademais, sobre blocos de endentação,é fortemente recomendado que blocos dentro de instruções if, else, while e outros devem ter apenas uma linha, possivelmente seja uma chamada de outra função. Esta recomendação mantém a função pequena e adiciona um valor significativo. Esta recomendação também implica que as funções não devem ser grandes e possuir vários níveis de aninhamento, ocasionando em um nível de endentação de no máximo dois blocos.
Gabarito: Correto

13. (CESPE -FUNPRESP-JUD- 2016) Julgue o próximo item, relativo a desenvolvimento e qualidade de software.
De acordo com Clean Code, argumentos em funções devem ser amplamente utilizados para melhorar a portabilidade do código e facilitar seu entendimento.
Comentários:

Pessoal, essa questão é batida! Vamos relembrar as diretrizes do Clean Code no aspectoReusabilidade? De acordo com a diretriz Parâmetros de funções, a quantidade ideal de parâmetros para uma função é de zero, seguida por um parâmetro, depois dois parâmetros e assim por diante.Deve-se, sempre que possível, evitar funções com três parâmetros, apenas com motivos muito especiais devemos ignorar essa regra.
Gabarito: Errado

14.(CESPE-STJ- 2015) A respeito de métricas de qualidade de código, código limpo e refatoração,julgue o item subsecutivo.

O uso de comentários é uma das técnicas de código limpo que, em conjunto com a refatoração de códigos, permite aumentar a produtividade de desenvolvimento de códigos.
Comentários:

Pessoal, de fato, comentários é uma das técnicas de código limpo e permite aumentar a produtividade de desenvolvimento de códigos desde que siga as diretrizes. Lembre-se:Nada pode ser tão útil quanto um comentário bem colocado. Porém nada pode ser tão prejudicial quanto comentários desnecessários e supérfluos, no máximo os comentários são um mal necessário.
Gabarito: Correto

/ 60

/

15. (CESPE - STJ- 2015) Julgue o próximo item, referente a criptografia, clean code e refatoração.

No contexto de clean code, as funções devem ter tamanho reduzido.

Comentários:

A primeira regra para funções é que elas devem ser pequenas. A segunda é que precisam ser mais espertas do que isso. (...) Enfim, as funções devem ser muito pequenas. Com todas essas afirmativas sobre o tamanho das funções, podemos fixar na mente que de fato, as funções devem ter tamanho reduzido.
Gabarito: Correto

16. (CESPE - TRE MT- 2015) Assinale a opção que apresenta instruções de elaboração corretas de acordo com a técnica Clean Code.
a) Os nomes utilizados devem ser pronunciáveis e devem ter sentido conhecido.

b) Os nomes de classes devem ser verbos no infinitivo e os de métodos devem ser substantivos.

c) Os nomes de funções e de métodos devem ser longos e descritivos.

d) Os parâmetros devem ser aglutinados em funções, e cada função deve ter, no máximo,
três parâmetros.
e) O comando return deve ser evitado, ao passo que continue e break devem ser priorizados,assim como o goto.

Comentários:

Os nomes utilizados devem ser pronunciáveis e devem ter sentido conhecido. Pessoal,
temos 13
diretrizes que informam sobre a necessidade de ter Nomes Significativos.
Portanto, com toda certeza, esse é o nosso gabarito.
Gabarito: Letra A

17. (CESPE -STF- 2013) A respeito do Clean Code e de integração contínua, julgue o item a seguir.

Os nomes de classes devem conter verbos, ao passo que os métodos devem ser indicados por substantivos.
Comentários:

Vejamos as diretrizes sobre nomes significativos: Classes e objetos devem ter nomes com substantivo(s), como Cliente, PaginaWiki, Conta e AnaliseEndereco. Evite palavras comoGerente,
Processador, Dados ou Info no nome de uma classe, que também não deve ser um verbo.
Por outro lado, os nomes de métodos devem ter verbos, como postarPagamento, excluirPagina ou salvar.
/ 60

/

Devem-se nomear métodos de acesso, alteração e autenticação segundo seus valores e adicionar os prefixos get, set ou is de acordo com o padrão javabean.*.
Gabarito: Errado

18. (CESPE - STF - 2013) Em relação a desenvolvimento orientado a testes, automação de testes com Selenium e SOAP Ui, julgue o item subsecutivo.
O desenvolvimento de sistemas mediante a utilização de CLEAN CODE baseia-se em um ciclo curto de repetições, em que o responsável pela codificação descreve testes automatizados que definem uma funcionalidade elicitada. Após se definir o teste, desenvolve-se o código que será validado pela equipe de teste e, posteriormente, refatorado.
Comentários:

A questão descreve TDD. Clean Code é um conjunto de técnicas de programação que quando praticadas pelos desenvolvedores tem como objetivo garantir a legibilidade e qualidade do código produzido
Gabarito: Errado

/ 60

/

LISTA DE QUESTõES - CLEAN CoDE

1. (CESPE - DP DF- 2022) Julgue o próximo item, relativo à análise estática de códigofonte.

A seguir, é apresentado um bom exemplo de código, de acordo com clean code.

int .a = 1;

if (

O == 1 )

a = Ol;

else

1 = 01;

2. (CESPE - TJ PA - 2020) O Clean Code deve considerar também o momento de teste do software em desenvolvimento. O Teste Limpo deve
O texto acima refere-se a qual metodologia de análise e projeto de software?

a) ser o mais completo possível, para que não seja necessário repeti-lo muitas vezes.

b) ser específico para determinado ambiente.

c) ser executado de forma que os testes sejam escritos antes que o código a ser testado esteja no ambiente de produção.
d) produzir resultados com respostas o mais abertas possível, para garantir eficiência ao processo.
e) contemplar todas as dependências possíveis, para garantir a eficácia do processo de testes.

3. (CESPE - MPE CE - 2020) Julgue o seguinte item, relativo a métricas de qualidade de código,
clean code e refactoring.

Pela perspectiva do clean code, é recomendado usar exceções (try/catch, por exemplo) em vez de testar vários códigos de erros ou, ainda, retornar null.
4. (CESPE - TJ AM - 2019) De acordo com Clean Code, julgue o item subsecutivo.

Independentemente da linguagem de programação, uma função deve executar todos os procedimentos que estão sintetizados no seu nome, gerando uma função com múltiplos passos.
5. (CESPE - TJ AM- 2019) De acordo com Clean Code, julgue o item subsecutivo.

Comentários explicativos ou descritivos no código devem ser evitados, pois caracterizam um código ruim.
/ 60

/

6. (CESPE - TJ AM- 2019) De acordo com Clean Code, julgue o item subsecutivo.

Em códigos orientados a objeto, tanto objetos quanto estruturas de dados expõem seus dados internos e as funções que manipulam tais dados.
7. (CESPE - TRE PE - 2017) Acerca do clean code, assinale a opção correta.

a) Para se evitar a proliferação de funções curtas, recomenda-se o uso de uma função longa com muitas variáveis globais, cada qual com variáveis locais de pouco uso.
b) O uso de um código que contenha as letras I e O como variáveis é mais recomendado que o uso de um código cujas variáveis sejam contador e resultado, por exemplo.
c) Os atuais ambientes de programação permitem que um único arquivo de código-fonte seja desenvolvido em diferentes linguagens, embora o ideal seja que um código-fonte contenha apenas uma linguagem.
d) A fim de facilitar o entendimento do código pelos desenvolvedores,
recomenda-se utilizar gírias locais para nomear funções, sempre que possível.
e) Na análise léxica, o uso de uma mesma palavra para dois ou mais propósitos facilita a compilação de código, diminui o código e aumenta a velocidade dos objetos binários compilados.
8. (FCC - DPE RS- 2017) Considere os trechos de código em que // indica comentário. Aplica corretamente as regras de Clean Code o trecho de código:
a) Trecho 1:

var a = (b + c)/d -10; // coloca o resultado em a b) Trecho 2:
//Valida se o cliente possui benefícios de acordo com a tabela de regras if ((cliente.Idade > 45 && cliente.Salario < enumValorSalarios.SalarioMinimo)
c) Trecho 3:

if ((visitante.EhAdulto && (visitante.EstaBloqueado) // lógica inversa return "Você não tem acesso por não ser adulto ou está bloqueado para ver este conteúdo";else return "Ótimo! Você poderá acessar este conteúdo.";
d) Trecho 4:

Reg regCPF = new Reg(@"A\d{3}\.\d{3}\.\d{3}-\d{2}$"); // 999.999.99
Reg regTelefone = new Reg(@"A\(\d{2}\)\d{4}-\d{4}$"); // (99)9999-9999

e) Trecho 5:

var textoContrato = RemoveHtml(contrato); //conforme ETC
EnviaContratoPorEmail(textoContrato);

x

,.Z 60

/

textoContrato = textoContrato.FTC(".", 11,11 ii ii ii_n)
11 11 11

9. (CESPE - TCE-SC- 2016) A respeito da análise estática de código-fonte em Clean
Code e
SonarQube, julgue o item subsecutivo.

De acordo com as diretivas do Clean Code, o número de argumentos de uma função não deve ser igual ou superior a três, devido a sua influência no entendimento da função.
10. (CESPE -TCE-PA- 2016) Acerca de análise estática de código-fonte, uma das práticas que verifica a qualidade do código e pode ser realizada antes da execução do software, julgue o próximo item.
De acordo com as práticas de clean code, comentários em um código-fonte servem para compensar um código mal escrito, devendo, portanto, ser evitados.
11. (CESPE-TCE-PA-2016) Acerca de análise estática de código-fonte, uma das práticas que verifica a qualidade do código e pode ser realizada antes da execução do software, julgue o próximo item.
No contexto de clean code, o conceito de objetos é semelhante ao de estruturas de dados,devendo os dados e as funções ficar expostos para permitir a inclusão de novos dados e de novas funções.
12. (CESPE-TCE-PA-2016) Acerca de análise estática de código-fonte, uma das práticas que verifica a qualidade do código e pode ser realizada antes da execução do software, julgue o próximo item.
As práticas de clean code recomendam que as funções tenham, no máximo, vinte linhas,
e até dois níveis de indentação.
13. (CESPE -FUNPRESP-JUD- 2016) Julgue o próximo item, relativo a desenvolvimento e qualidade de software.
De acordo com Clean Code, argumentos em funções devem ser amplamente utilizados para melhorar a portabilidade do código e facilitar seu entendimento.
14. (CESPE-STJ- 2015) A respeito de métricas de qualidade de código, código limpo e refatoração,julgue o item subsecutivo.

O uso de comentários é uma das técnicas de código limpo que, em conjunto com a refatoração de códigos, permite aumentar a produtividade de desenvolvimento de códigos.
/ 60

/

15. (CESPE - STJ- 2015) Julgue o próximo item, referente a criptografia, clean code e refatoração.

No contexto de clean code, as funções devem ter tamanho reduzido.

16. (CESPE - TRE MT- 2015) Assinale a opção que apresenta instruções de elaboração corretas de acordo com a técnica Clean Code.
a) Os nomes utilizados devem ser pronunciáveis e devem ter sentido conhecido.

b) Os nomes de classes devem ser verbos no infinitivo e os de métodos devem ser substantivos.

c) Os nomes de funções e de métodos devem ser longos e descritivos.

d) Os parâmetros devem ser aglutinados em funções, e cada função deve ter, no máximo,
três parâmetros.
e) O comando return deve ser evitado, ao passo que continue e break devem ser priorizados,assim como o goto.

17. (CESPE -STF- 2013) A respeito do Clean Code e de integração contínua, julgue o item a seguir.

Os nomes de classes devem conter verbos, ao passo que os métodos devem ser indicados por substantivos.
18. (CESPE - STF - 2013) Em relação a desenvolvimento orientado a testes, automação de testes com Selenium e SOAP Ui, julgue o item subsecutivo.
O desenvolvimento de sistemas mediante a utilização de CLEAN CODE baseia-se em um ciclo curto de repetições, em que o responsável pela codificação descreve testes automatizados que definem uma funcionalidade elicitada. Após se definir o teste, desenvolve-se o código que será validado pela equipe de teste e, posteriormente, refatorado
/ 60

/

GABARITo - CLEAN CoDE

1. ERRADO

2. LETRA C

3. CORRETO

4. ERRADO

5. CORRETO

6. ERRADO

7. LETRA C

8. LETRA D

9. CORRETO

10. ERRADO

11. ERRADO

12. CORRETO

13. ERRADO

14. CORRETO

15. CORRETO

16. LETRA A

17. ERRADO

18. ERRADO

/ 60

/

