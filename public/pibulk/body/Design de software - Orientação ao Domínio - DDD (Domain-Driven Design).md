# Design de software - Orientação ao Domínio - DDD (Domain-Driven Design)

O Domain-Driven Design (DDD), ou Design Orientado ao Domínio, é uma abordagem de design de software que se concentra na modelagem do domínio do problema em questão. Ele visa criar um design que reflita de forma precisa e efetiva as regras e conceitos do negócio, com o objetivo de desenvolver sistemas que atendam às necessidades do domínio de forma eficiente e flexível.

O DDD enfatiza a colaboração estreita entre desenvolvedores e especialistas do domínio, como especialistas em negócios, analistas e outros stakeholders. O processo de design começa com a exploração do domínio, compreendendo os conceitos-chave, os processos de negócio e as regras que regem o sistema.

Alguns conceitos importantes no DDD incluem:

1. Entidades: São objetos que têm identidade única e podem ter um ciclo de vida. As entidades são modeladas com base em conceitos do domínio, e não apenas como estruturas de dados.

2. Agregados: São grupos de entidades e objetos de valor relacionados, tratados como uma unidade coesa. Os agregados são delimitados por uma raiz de agregado, que garante a consistência e a integridade das entidades relacionadas.

3. Objetos de Valor: São objetos que representam conceitos imutáveis e sem identidade própria. Eles encapsulam um conjunto de atributos e fornecem funcionalidades específicas.

4. Contexto Delimitado: O DDD preconiza a divisão do sistema em contextos delimitados, onde cada contexto é responsável por um subconjunto específico do domínio. Isso permite uma melhor compreensão e modelagem das regras de negócio e ajuda a evitar problemas de complexidade e dependências excessivas.

5. Linguagem Ubíqua: A linguagem ubíqua é uma linguagem compartilhada entre desenvolvedores e especialistas do domínio. Ela consiste em termos e conceitos que refletem o vocabulário do domínio de negócio. Uma linguagem ubíqua ajuda a melhorar a comunicação e o alinhamento entre os membros da equipe.

O DDD também promove o uso de padrões arquiteturais, como o padrão Repository para o acesso a dados, o padrão Service para a orquestração de operações e o padrão Factory para a criação de objetos complexos.

Ao aplicar o DDD, é essencial considerar a evolução contínua do design e a iteração com os especialistas do domínio. O objetivo é criar um modelo de domínio rico e expressivo, que seja uma representação fiel das regras e do comportamento do negócio.

O DDD é uma abordagem poderosa para o design de software em domínios complexos, onde a compreensão profunda e precisa do negócio é crucial para o sucesso do projeto. No entanto, é importante equilibrar o uso adequado dos conceitos do DDD com as necessidades e restrições do projeto, evitando complexidade desnecessária quando não é justificada.

Design Orientado ao Domínio (Domain-Driven Design - DDD)

Um domínio geralmente é mais extenso do que alguns objetos e, para torná-lo mais gerenciável, o DDD divide um domínio em subdomínios. O termo DDD 'domínio do problema' é usado para definir uma área funcional dentro de um contexto como uma organização ou departamento.
O desenvolvimento de software é mais frequentemente aplicado para automatizar processos que existem no mundo real ou fornecer soluções para problemas de negócios reais. Os processos de negócios sendo automatizados ou problemas do mundo real que o software é o domínio do software. Devemos entender desde o início que o software é originado e profundamente relacionado a este domínio.
Software é feito de código. Podemos ser tentados a gastar também muito tempo com o código e ver o software simplesmente como objetos e métodos. Considere a fabricação de carros como uma metáfora. Os trabalhadores envolvidos na fabricação de automóveis podem se especializar na produção de peças do carro, mas, ao fazê-lo, muitas vezes têm uma visão limitada do carro inteiro.
Eles começam a ver o carro como uma enorme coleção de peças que precisam se encaixar, mas um carro é muito mais do que isso. Um bom carro começa com uma visão. Começa com especificações cuidadosamente escritas. E continua com o Projeto. Muitos e muitos desenhos. Meses, talvez anos de tempo gasto em design, alterando-o e refinando-o até atingir perfeição, até que reflita a visão original. O processamento design não é tudo no papel. Muito disso inclui fazer modelos de o carro, e testá-los sob certas condições para ver se eles trabalhar. O design é modificado com base nos resultados do teste. O carro é enviado para produção eventualmente, e as peças são criadas e montadas juntas.
O desenvolvimento de software é semelhante. Não podemos simplesmente sentar e digitar o código. Podemos fazer isso e funciona bem para casos triviais. Mas não podemos criar software complexo como esse.
Para criar um bom software, você precisa saber do que se trata esse software. Você não pode criar um sistema de software bancário a menos que tenha um bom entendimento do que é o sistema bancário, é preciso entender o domínio do setor bancário. É possível criar um software bancário complexo sem um bom conhecimento de domínio?
Sem chance. Nunca. Quem conhece o banco? O arquiteto de software? Não. Ele apenas usa o banco para manter seu dinheiro seguro e disponível quando ele precisa. O analista de software? Na verdade, não. Ele sabe analisar um determinado tema, quando lhe são dados todos os ingredientes necessários. O desenvolvedor? Esqueça. Quem então? Os banqueiros, claro. O sistema bancário é muito bem compreendido pelas pessoas de dentro, por seus especialistas. Eles conhecem todos os detalhes, todas as armadilhas, todos os problemas possíveis.É por aqui que devemos sempre começar: o domínio. Quando iniciamos um projeto de software, devemos nos concentrar no domínio em que ele está operando. Todo o propósito do software é aprimorar um domínio específico. Para poder fazer isso, o software deve se encaixar harmoniosamente com o domínio para o qual foi criado. Caso contrário, ele introduzirá tensão no domínio, provocando mau funcionamento, danos e até mesmo o caos.
Como podemos fazer com que o software se encaixe harmoniosamente com o domínio? A melhor maneira de fazer isso é tornar o software um reflexo do domínio. O software precisa incorporar os conceitos e elementos centrais do domínio e realizar com precisão as relações entre eles. O software tem que modelar o domínio.
Alguém sem conhecimento de banco deve ser capaz de aprender muito apenas lendo o código em um modelo de domínio. Isso é essencial. O software que não tem suas raízes plantadas profundamente no domínio não reagirá bem às mudanças ao longo do tempo.
Então começamos com o domínio. Um domínio é algo deste mundo. Precisamos criar uma abstração do domínio. Aprendemos muito sobre um domínio enquanto conversamos com os especialistas do domínio. Mas esse conhecimento bruto não será facilmente transformado em construções de software, a menos que construamos uma abstração dele, um projeto em nossas mentes. No começo, o projeto está sempre incompleto.
Mas com o tempo, enquanto trabalhamos nisso, nós o melhoramos e ele se torna cada vez mais claro para nós. O que é essa abstração? É um modelo, um modelo do domínio. De acordo com Eric Evans, um modelo de domínio não é um diagrama específico; é a ideia que o diagrama pretende transmitir. Não é apenas o conhecimento na cabeça de um especialista de domínio; é uma abstração rigorosamente organizada e seletiva desse conhecimento. O modelo é nossa representação interna do domínio de destino e é muito necessário durante todo o processo de design e desenvolvimento.
Durante o processo de design, lembramos e fazemos muitas referências ao modelo. O mundo ao nosso redor é demais para nossas cabeças lidarem. Mesmo um domínio específico pode ser mais do que uma mente humana pode lidar ao mesmo tempo. Precisamos organizar a informação, sistematizá-la, dividi-la em pedaços menores, agrupar esses pedaços em módulos lógicos, pegar um de cada vez e lidar com isso. Precisamos até deixar algumas partes do domínio de fora. Um domínio contém informações demais para incluir tudo no modelo. E muito disso nem precisa ser considerado.
DDD pode ser visto por alguns como a volta da orientação a objetos. É verdade que o livro é um chamado às boas práticas de programação que já existem desde a época remota do SmallTalk.
Quando se fala em Orientação a Objetos pensa-se logo em classes, heranças, polimorfismo, encapsulamento. Mas a essência da Orientação a Objetos também tem elementos como:

· Alinhamento do código com o negócio: o contato dos desenvolvedores com os especialistas do domínio é algo essencial quando se faz DDD (o pessoal de métodos ágeis já sabe disso faz tempo);

· Favorecer reutilização: os blocos de construção, que veremos adiante, facilitam aproveitar um mesmo conceito de domínio ou um mesmo código em vários lugares;

· Mínimo de acoplamento: Com um modelo bem-feito, organizado, as várias partes de um sistema interagem sem que haja muita dependência entre módulos ou classes de objetos de conceitos distintos;

· Independência da Tecnologia: DDD não foca em tecnologia, mas sim em entender as regras de negócio e como elas devem estar refletidas no código e no modelo de domínio. Não que a tecnologia usada não seja importante, mas essa não é uma preocupação de DDD.

Para ter um software que atenda perfeitamente a um determinado domínio, é necessário que se estabeleça, em primeiro lugar, uma Linguagem Ubíqua, ou Linguagem comum, com termos bem definidos, que fazem parte do domínio do negócio e que são usados por todas as pessoas que fazem parte do processo de desenvolvimento de software. Nessa linguagem estão termos que fazem parte das conversas diárias entre especialistas de negócio e times de desenvolvimento. Todos devem usar os mesmos termos tanto na linguagem falada quanto no código.

Naked Objects

Naked Objects é um padrão de arquitetura usado na engenharia de software. É definida por três princípios:

· Toda a lógica de negócios deve ser encapsulada nos objetos de domínio. Este princípio não é exclusivo de objetos nus; é um forte compromisso com o encapsulamento.

· A interface do usuário deve ser uma representação direta dos objetos do domínio, com todas as ações do usuário consistindo em criar, recuperar ou invocar métodos nos objetos do domínio. Este princípio não é exclusivo de objetos nus: é uma interpretação de uma interface de usuário orientada a objetos.

· O recurso inovador do padrão de objeto nu surge combinando o 1º e 2º princípios em um 3º princípio:

A interface do usuário deve ser criada de forma totalmente automática a partir das definições dos objetos do domínio. Isso pode ser feito usando reflexão ou geração de código-fonte.
O padrão de Naked Objects foi descrito formalmente pela primeira vez na tese de doutorado de Richard Pawson que inclui investigação de antecedentes e inspirações para o padrão, incluindo, por exemplo, a interface de usuário mórfica.
O primeiro framework open source completo a ter implementado o padrão foi nomeado Naked Objects. Em 2021, Pawson anunciou que posteriormente aplicou o mesmo padrão ao paradigma de programação Functional Programming, como uma alternativa ao paradigma de programação orientada a objetos, criando uma variante da estrutura Naked Objects chamada Naked Functions.
O design orientado por domínio (DDD) concentra-se no que mais importa nos aplicativos corporativos: o domínio principal do negócio. Usando princípios orientados a objetos, você pode desenvolver um modelo de domínio que todos os membros da equipe — incluindo especialistas em negócios e técnicos — possam entender.
Mas se você já tentou criar um aplicativo orientado a domínio, saberá que aplicar os princípios DDD é mais fácil dizer do que fazer. Com a estrutura Naked Objects de software livre, você constrói seu aplicativo Java escrevendo apenas as classes de domínio principais, deixando que ele cuide do restante da infraestrutura.
O Naked Objects renderiza automaticamente seu objeto de domínio em um visualizador genérico - rich client ou HTML . Você pode usar sua integração com o Fitnesse para testar o desenvolvimento de seu aplicativo, história por história. E, uma vez desenvolvido, você pode implantar seu aplicativo em tempo de execução completo do Naked Objects ou em sua infraestrutura de aplicativo existente.

