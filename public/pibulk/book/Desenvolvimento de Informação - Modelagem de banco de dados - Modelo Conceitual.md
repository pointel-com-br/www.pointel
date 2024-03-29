# Desenvolvimento de Informação - Modelagem de banco de dados - Modelo Conceitual

Índice

1) Modelagem Conceituai de Dados.

2) Modelo Entidade Relacionamento - ER

3) Relacionamentos.

4) Entidade Forte x Entidade Fraca

5) Outras Representações Conceituais.

6) Questões Comentadas - Administração de Dados, Projetos de Banco de Dados e Modelagem Conceituai
- CE 46

7) Questões Comentadas - Administração de Dados, Projetos de Banco de Dados e Modelagem Conceituai
- CE 67

8) Lista de Questões - Administração de Dados, Projetos de Banco de Dados e Modelagem Conceituai -
CEBR 101

9) Lista de Questões - Administração de Dados, Projetos de Banco de Dados e Modelagem Conceituai -
CESG 113

10) Lista de Questões - Administração de Dados, Projetos de Banco de Dados e Modelagem Conceituai -
CEBR 142

MoDELAGEM CoNCEITUAL DE DADoS (MoDELo DE

ENTIDADES E RELACIoNAMENToS)

PRoJETo DE BANCo DE DADoS

O desenvolvimento de uma aplicação de banco de dados é uma tarefa complexa que envolve várias etapas, entre elas o projeto de um esquema de banco de dados. Oesquema é a forma do bolo. Ele estabelece a definição dos objetos que serão armazenados em um banco de dados. Uma tabela, por exemplo, é descrita em função dos seus atributos e outras restrições de integridades.
Esquema Instância

Para evoluir dentro do processo de definição de um banco de dados, as necessidades dos usuários desempenham um papel fundamental. Essas necessidades vão estabelecer os requisitos do nosso esquema de banco de dados. Visando capturar de forma consistente as funcionalidades esperadas pelos usuários devemos definir um esquema conceituai de dados.
Nesta aula, nosso foco será na definição de um esquema que esteja em um nível de abstração que possa ser entendido pelos usuários do sistema. Utilizamos um esquema conceituai para representar as informações percebidas pelo usuário, retirando do modelo as informações técnicas envolvidas. Desta forma, é possível debater e evoluir o modelo com as pessoas que vão de fato utilizar os dados armazenados.
Essas ações levam a construção de um projeto de banco de dados mais robusto e adequado para a organização. O projetista de banco de dados precisa interagir com os usuários da aplicação para entender suas demandas. Essas demandas vão dar origem um diagrama que representa as informações de forma simples, em alto nível.
Esse diagrama geralmente utiliza notações gráficas para representar as entidades,
relacionamentos e atributos que serão armazenados em um banco de dados. Esse tipo de construção consegue estabelecer uma semântica para os dados. Partindo dessa representação do modelo de dados podemos refinar o diagrama, diminuído a abstração do modelo.
Uma abstração similar pode ser observada quando pensamos na construção de uma casa ou prédio. Para entender melhor os requisitos do cliente, um arquiteto pode se utilizar de uma planta baixa ou de uma simulação em três dimensões, ambas são abstrações ou representações da casa. Assim, o futuro morador pode decidir sobre a disposição dos móveis em um ambiente, cores e tamanhos.
CASA PLANTA BAIXA 3D

Perceba que a casa real é uma implementação do modelo abstrato descrito na planta baixo ou no modelo em três dimensões. Essa ideia também vale para bancos de dados, o banco de dados será a implementação de um modelo abstrato que apresenta os requisitos e as definições necessárias. Para chegarmos no nível de implementação precisamos começar no nível conceituai dos modelos de dados, definindo um esquema conceituai.
Perceba que no modelo de dados conceituai os queremos definir quais dados serão armazenados. Neste momento, pouco importa como os dados serão armazenados fisicamente. Por isso, podemos dizer que os modelos de dados conceituais são independentes de hardware e software. Eles não estão associados a um SGBD específico e possuem o mais alto nível de abstração.
Depois de estabelecermos um modelo conceituai, podemos incorporar mais informações a respeito das restrições e tipos de dados presentes em cada entidade ou relacionamento.Assim, reduziremos o nível de abstração do modelo, definindo um modelo lógico ou de implementação para os dados. A relação ou tabela é a estrutura básica que define um modelo lógico, mais especificamente um modelo lógico relacional.
Nesta etapa já é possível termos detalhes suficientes para estruturarmos nosso banco de dados. Podemos, portanto, utilizar a linguagem SQL para definição das tabelas. O comandoSQL é recebido pelo SGBD que se encarrega de criar a estrutura física para armazenamento dos dados. Ao final da execução dos comandos SQL temos um esquema físico de banco de dados.
O fluxo do projeto de banco de dados possui algumas etapas mais importantes que aparecem com frequência em provas de concursos: projeto (ou modelagem) conceituai,projeto lógico e projeto físico. A figura a seguir apresenta um fluxo simplificado para construção de um projeto de banco de dados. Peço que preste atenção nos elementos ao lado direito da figura. Tente observar as etapas que acabamos de descrever.
ESQUEMATIZANDO

Especificação da Esquema conceituai transação de alto nível (em um modelo de dados de alto nível)
Programas de aplicação

Figura 1 - Projeto de banco de dados

Perceba que cada projeto gera como resultado um esquema. Nesta aula nosso foco será entender as possíveis estruturas notacionais para definição de um esquema conceituai. Omodelo entidade-relacionamento (ER) será o primeiro a ser estudado, em seguida veremos algumas notações alternativas para representação gráfica do modelo conceituai.
É importante perceber que essa representação utiliza elementos gráficos para apresentar uma semântica simples e de entendimento rápido. Para que essa interação com o diagrama seja feita a contento é preciso entender os componentes que se fazem presentes na elaboração do esquema de dados usando a modelagem conceituai.
A sequência do processo, seguido para o desenvolvimento de um projeto de banco de dados, nos apresenta o projeto lógico que, de forma prática, está associado ao modelo relacional. Perceba que neste nível existe uma dependência de um tipo específico deSGBD. Esse assunto será visto em outra aula. Vejamos uma questão sobre o assunto.

(Ministério da Economia - Especialista em Gestão de Projetos - 2020)

Com relação às informações contidas no modelo conceituai precedente, julgue o próximo item.
O modelo em tela, da forma como está apresentado, não poderá ser implementado,porque, além de ser um modelo conceituai, contém um relacionamento n:n.

Comentários: O modelo em questão apresenta uma estrutura abstrata e conceituai. Para que seja implementado é necessário baixar o nível do modelo para um modelo lógico, pois precisamos de detalhes como tipos de dados e restrições de integridade para que o SGBD crie (implemente) o modelo.
Gabarito: CERTO

Antes de falarmos um pouco mais sobre a modelo entidade relacionamento, queria que você voltasse os olhos para a figura anterior e percebesse que ao lado esquerdo temos uma sequência de ações que acontecessem em paralelo ao projeto de banco de dados. Essas ações vão descrever as funcionalidades do sistema. Gostaria de falar um pouco sobre a análise funcional, que pode ser vista como o um processo simplificado de engenharia de software. Vamos, então, dar continuidade a nossa explicação focando nossa atenção nos conceitos de análise funcional.
ANÁLISE FUNCIoNAL

Ainda sobre a figura vista anteriormente, podemos observar que, em paralelo com a especificação de requisitos de dados, é útil determinar os requisitos funcionais da aplicação. Os requisitos funcionais estão ligados ao processo de engenharia de software e vão definir as funcionalidades do sistema. Eles consistem em operações (ou transações)definidas pelos usuários que serão aplicadas ao banco de dados.

No projeto de desenvolvimento de um sistema, é comum usar diagrama de fluxo de dados,
diagrama de sequência, cenários e outras técnicas para especificar os requisitos funcionais.Neste sentido, o ciclo de vida de um sistema de informação pode ser denominado de ciclo de vida macro, este inclui as fases de análise de viabilidade, levantamento e análise de requisitos, projeto, implementação, validação e teste de aceitação e implantação, operação e manutenção.
Estudo da viabilidade
Engenharia de requisitos(Análise)

Modelagem do sistema(Desenho)

Codificação e Teste(Desenvolvi mento)
Implantação Avaliação

2J

MANUTENÇÃO

l Jl 1

Figura 2 - Ciclo de vida de um sistema de informação.

Já as atividades do ciclo de vida micro, que focalizam o sistema de banco de dados,
incluem:

1. Definição do sistema. O escopo do sistema de banco de dados, seus usuários e suas aplicações são definidos. As interfaces para diversas categorias de usuários, as restrições do tempo de resposta e as necessidades de armazenamento são identificadas.
2. Projeto de banco de dados. Um projeto lógico e físico completo do sistema de banco de dados no SGBD escolhido é preparado.
3. Implementação do banco de dados. Isso compreende o processo de especificar as definições de banco de dados conceituais, externas e internas,crias os arquivos de banco de dados (vazios) e implementar as aplicações de software.
4. Carga ou conversão de dados. O banco de dados é preenchido ou pela carga dos dados diretamente ou pela conversão de arquivos existentes para o formato do sistema de banco de dados.
5. Conversão de aplicação. Quais quer aplicação de software de um sistema anterior são convertidas para o novo sistema.
6. Teste e validação. O novo sistema é testado e validado. O teste e a validação dos programas exigem várias técnicas que normalmente são abordadas pela engenharia de software.
7. Operação. O sistema de banco de dado e suas aplicações são colocados em operação. Normalmente, os sistemas antigos e os novos são operados em paralelo por um período.
8. Monitoramento e manutenção. Durante a fase operacional, o sistema é constantemente monitorado e mantido. O crescimento e a expansão podem ocorrer no conteúdo de dados e nas aplicações. Importantes modificações podem ser necessárias de tempos em tempos.
As fases de projeto e implementação de um grande banco de dados podem ser visualizadas na figura abaixo:
Conteúdo, estrutura e restrições de dados
Aplicações de banco de dados
Fase 1: Levantamento e análise de requisitos
Fase 2: Projeto conceituai do banco de dados
Fase 3: Escolha do SGBD
Fase 4: Mapeamento do modelo de dados(projeto lógico)

Fase 5: Projeto físico
Fase 6: Implementação e ajuste do sistema
Requisitos de dados
Projeto do esquema conceituai
(independente do SGBD)

Instruções DDL
Instruções SDL

Requisitos de processamento
Projeto de transação e aplicação(independente do SGBD)

Implementação de transação e aplicação
Figura 3 - Fases do projeto e implementação de banco de dados

A fase de escolha de um SGBD deve considerar alguns aspectos relacionados ao custo de aquisição do software, manutenção, aquisição de hardware, criação ou conversão de dados, pessoal, treinamento e operacional.
Contudo, quando estamos analisando o problema do ponto de vista do sistema de informação, muitas vezes existe a necessidade de uma linguagem comum para comunicar os requisitos e demais ações que são feitas durante as fases da elaboração de um sistema.Para tentar apresentar um pouco do que seria essa linguagem vamos mostrar nas próximas linhas o conceito de UML.
UML- ÜNIFIED MODELING LANGUAGE

A necessidade de um técnica-padrão que visa cobrir todas as etapas de desenvolvimento de um sistema de informação. O espectro que vai da análise de requisitos, passando pela modelagem, projeto, implementação até chegar à implantação. Um destas técnicas é conhecida como UML - Unified Modeling Laguage. Ela oferece um mecanismo na forma de notação diagramática e sintaxe de linguagem associada para cobrir todo o ciclo de vida.
A UML combina conceitos comumente aceitos de muitos métodos e metodologias orientados a objetos (O-O). Ela é genérica independente de linguagem e plataforma. AUML
tem muitos tipos diagramas que podem ser divididos em duas categorias:

Diagramas estruturais. Estes descrevem os relacionamentos estruturais ou estáticos entre objetos de esquema, objetos de dados componentes de software.Incluem os diagramas de classes, de objetos, de componentes e de implementação.
Diagramas comportamentais. Sua finalidade é descrever o comportamento ou relacionamento dinâmico entre componentes. Incluem diagramas de caso de uso,de sequência, de colaboração, de estados e de atividades.

Pense que um sistema tem aspectos estáticos e dinâmicos, esses dois tipos de diagrama descrevem essas características. Vamos dar um exemplo de cada um dos tipos de diagrama apenas para ajudar você na fixação do conteúdo. O Diagrama deClasses oferece um ótimo exemplo do tipo de diagrama estrutural e fornece um conjunto inicial de elementos de notação que todos os outros diagramas de estrutura usam. O propósito do diagrama de classes é mostrar os tipos que estão sendo modelados no sistema.
Uma classe é representada na forma de um retângulo, contendo duas linhas que separam
3 partes. A primeira contém no nome da classe, a segunda os atributos da classe e a última os métodos. Vejamos uma figura que ajude a entender melhor esses conceitos:
Concurseiro nome: String concursoAlvo: String identidade: Integer dataDeNascimento: Date getConcursoAlvo(): String getldadeQ: Integer
Observe a classe acima, temos a classe Concurseiro com os atributos nome, concursoAlvo,
indentidade e dataDeNascimento. Veja que cada atributo tem um tipo de dado associado.
Por fim, o retângulo mostra as operações que podem ser executadas com os dados desta classe, conhecidos como métodos.
O diagrama comportamental que usaremos como exemplo é o diagrama de Casos de Uso.
O diagrama de casos de uso tem o objetivo de auxiliar a comunicação entre os analistas e o cliente. Ele descreve um cenário que mostra as funcionalidades do sistema do ponto de vista do usuário. O cliente deve ver no diagrama de casos de uso as principais funcionalidades de seu sistema.
O diagrama de Caso de Uso é representado por atores, casos de uso e relacionamentos entre estes elementos. Um ator é representado por um boneco e um rótulo com o nome do ator. Um ator é um usuário do sistema, que pode ser um usuário humano ou um outro sistema computacional. Um caso de uso é representado por uma elipse e um rótulo com o nome do caso de uso. Um caso de uso define uma grande função do sistema. Os relacionamentos ajudam a descrever casos de uso. A figura abaixo descreve um diagrama de caso de uso. Nela temos os atores Paciente, Secretária, Doutor e Balconista que fazem acesso a diferentes macrofuncionalidades do sistema, ou seja, os casos de uso.
Figura 4 - Diagrama de caso de uso

Antes de você pergunte o que são os termos «include» e «extends» na figura acima,deixa eu tentar explicar de uma forma bem simples. O «include» afirma que um caso de uso depende do outro, tente observar na figura, para marcar uma consulta é necessário ter os dados do paciente. Já o «extends» incluí uma funcionalidade extra que não é obrigatória, por exemplo, adiar pagamento é uma possibilidade na ação de pagar conta.
ADMINISTRAçÃo DE DADoS

Você deve se lembrar da diferença entre o administrador de banco de dados e o administrador de dados que vimos em uma aula anterior do nosso curso. O nosso objetivo agora é olhar para a administração dos dados de forma mais sistêmica. A atividade de administração de dados traz em seu cerne a preocupação em tornar claro o entendimento das informações que estão sendo armazenadas, caracterizado pelo bom entendimento do negócio da organização, pelo projeto adequado das bases de dados,pelo compartilhamento de informações e pela integração entre os sistemas de informação.
A implantação de uma política de Administração de Dados (AD) visa minimizar riscos quanto à complexidade da informação armazenada. O resultado da análise do atual cenário,benchmarking e boas práticas tem por objetivo é suprir as necessidades de informação proveniente dos sistemas de informação. Esse processo envolve diversas perspectivas ou ações:
Modelagem de dados corporativos - analisa a modelagem de dados quando aplicada aos requisitos de dados globais ou totais de uma empresa, em vez de ser aplicada ao conjunto menor de requisitos que devem ser atendidos por um único sistema de informações. Éimportante ter em mente que os modelos de dados corporativos são necessários e devem ser modelados e documentados em todos os níveis de abstração. Assim, o desenvolvimento de um modelo de dados corporativos pode ser abordado em função de seis princípios:
1. Desenvolver o modelo "top-down".

2. Dar primazia ao core business.

3. Cobrir toda a organização

4. Tentar prever o futuro no seu modelo.

5. Desenvolver cooperativamente;

6. Obtenha consenso, não perfeição.

Definição de dados e nomenclatura - essas ações visão a definição de dados chave e os padrões de nomenclatura usados pelos gerenciadores ou projetistas de dados.
Metadados - mais uma vez no curso temos o conceito de "dados sobre dados" que são usados de forma especial na estruturação de qualquer modelo de dados.
Qualidade de dados - você deve ter uma visão clara dessa importante área. Observamos que os dados de baixa qualidade podem afetar um negócio. Devemos, portanto, procurar entender as causas associadas aos dados de baixa qualidade e usarmos técnicas para melhorar a qualidade deles.
Acessibilidade de dados - essa perspectiva pode ser relacionada à segurança de dados,
proteção do banco de dados contra usuários não autorizados, integridade de dados,proteção do banco de dados contra usuários autorizados e recuperação de dados, trazendo o banco de dados a um estado consistente utilizável após uma falha.
Gerenciamento de dados mestre - Os dados mestres são os dados globais padronizados e utilizados por toda a empresa. Eles evitam que os dados sejam armazenados em bases de dados distintas.
Todos esses fatores estão associados a governança de dados, definida como a orquestração formal de pessoas, processos e tecnologia para permitir que uma organização aproveite os dados como um ativo corporativo.
O administrador de dados, também conhecido como projetista de dados, tem um trabalho de natureza estratégica em relação os dados corporativos. Sua principal preocupação é entender as necessidades de informações e contribuir para a disponibilidade dos dados.Perceba que o objetivo do AD envolve planejar e controlar o gerenciamento dos dados corporativo. Vejamos uma questão que aborda esse tema.
PRESTE MAIS

ATENÇAO!

(Questão/CESPE/BASA)

O dicionário de dados é uma das principais ferramentas para a administração dos dados corporativos. Por meio da engenharia reversa, pode-se armazenar os modelos de dados,as estruturas de dados, seus relacionamentos e toda a documentação necessária para garantir facilidade na localização e manipulação dos dados. Acerca dos papéis do administrador de dados (AD) e dos dicionários de dados, julgue os itens a seguir.
Enquanto o AD se preocupa com o gerenciamento dos dados como patrimônio da empresa, o administrador de banco de dados (ABD) é responsável pelo gerenciamento físico e dos acessos ao banco de dados.
Comentário: Lembre-se o administrador de dados (AD) atua para: (1) obter um melhor conhecimento do contexto de negócio;
(2) projetar adequadamente a base de dados; (3) permitir o compartilhamento dos dados e a integração dos sistemas; e (4)contribuir para a unificação da visão que a empresa tem dos dados.

Gabarito: C.

A partir do próximo tópico, vamos nos preocupar com a construção de um modelo de dados conceituai utilizando o diagrama entidade relacionamento. Veja que essa etapa do projeto de banco de dados é tipicamente uma atividade realizada pelo administrador de dados. Vamos em frente!
MoDELo ENTIDADE RELACIoNAMENTo - ER

Na fase de projeto de banco de dados, é importante usar um modelo de dados conceituai de alto nível com as seguintes características:
1. Expressividade. O modelo de dados deve ser expressivo o suficiente para distinguir diferentes tipos de dados, relacionamentos e restrições.
2. Simplicidade e compreensão. O modelo deve ser simples o suficiente para que usuários típicos não especialista compreendam e usem seus conceitos.
3. Minimalismo. O modelo deve ter um pequeno número de conceitos básicos, que são distintos e não sobrepostos.
4. Representação diagramática. O modelo deverá ter uma notação diagramática para exibir um esquema conceituai que seja fácil de interpretar.
5. Formalidade. Um esquema conceituai expresso no modelo de dado deve representar uma especificação não ambígua forma dos dados (precisão e não ambiguidade).
Você vai perceber que o modelo conceituai se encaixa como uma luva nestas características. A modelagem conceituai é uma fase crucial no planejamento de uma aplicação de banco de dados. Ela vai permitir a descrição de um modelo de dados associados a um contexto de negócio ou requisitos de um processo em alto nível de abstração. Ou seja, essa descrição tende a ser simples, com poucos elementos diagramáticos.
Uma abordagem tradicional de modelagem de dados engloba as estruturas e restrições do banco de dados. Os elementos diagramáticos são responsáveis por descrever essas estruturas e restrições aos usuários de negócio. As estruturas representam entidades e atributos cujos valores são interpretações de objetos do mundo real e suas propriedades.
Imagine um carro. Ele tem alguns atributos que podem ser definidos para cada instância de carro. Ou, de forma mais simples, para todos os carros que você pensar, será possível definir características como cor, marca, modelo e peso. A figura abaixo apresenta atributos associados a entidade carro.
Atributos
Marca
Color
Modelo
Peso

Neste sentido, queremos apresentar os conceitos ou elementos presentes no modelo
Entidade-Relacionamento (ER). Este é um modelo de dados conceituai de alto nível extremamente popular. A modelagem ER foi proposta por Peter Chen, em março de 1976,no artigo The Entity-Relationship Model: Toward the unified view of data. A
literatura especializada afirma que o modelo tem como embasamento a formalização do óbvio. Oesquema a seguir descreve as características básicas do modelo ER.

Figura 1 - Conceitos básicos do modelo Entidade-Relacionamento.

A abordagem é composta por uma técnica de diagramação e um conjunto de conceitos. A
técnica é um meio de representação dos próprios conceitos por ela manipulados:
entidades, relacionamentos e atributos. Cada um deles é representando por uma figura geométrica. Entidade são definidas por retângulos, relacionamentos são denotados por losango1 e atributos são referenciados por meio de elipses. Vamos agora entender a definição de cada um desses elementos.
ENTIDADES

Entidades são objetos do "mundo real" sobre os quais se deseja manter informações no banco de dados. Cada entidade de ser a representação abstrata de um objeto. Atributos são as propriedades que descrevem essas entidades. Relacionamentos são as associações entre entidades. Cada tipo entidade que participa de um tipo relacionamento executa um papel no relacionamento.
De posse dos conceitos que vimos até aqui vamos tentar analisar a primeira questão do
CESPE desta nossa aula.

1 A forma correta é losango. Esta palavra entrou na língua portuguesa através do francês losange. É uma palavra grave, isto é, com acento tónico na penúltima sílaba. Em geral, as palavras graves não levam acento gráfico.
HORA DE

PRATICAR!

(Ano: 2016 Banca: CESPE Órgão: TCE-PA Prova: Auditor de Controle Externo - Área
Informática - Analista de Suporte)

i-0 número

Considerando a figura apresentada, que ilustra o modelo de um banco de dados hipotético, julgue o item que se segue.
[1] A figura expõe um modelo lógico, uma vez que ele contém detalhes de implementação e é independente de um sistema gerenciador de banco de dados (SGBD).
Comentário: Analisando a figura acima podemos verificar que o diagrama apresenta características gráficas com alto nível de abstração. Esse tipo de modelo é conhecido como conceituai. Perceba que a assertiva diz que esse é um modelo lógico, o que não é verdade. Por isso podemos afirmar que a afirmação está incorreta.
Gostaria ainda de aproveitar o diagrama para fazer um comentário a respeito da notação dos atributos. Percebam que os atributos, associados a cada uma das entidades, estão representados por bolas e os nomes ou descrição deles aparecem fora da mesma. Essa é uma das notações alternativas para representação dos atributos.
Gabarito: E.

Agora vamos voltar a teoria sobre o assunto. A figura abaixo foi retirada do artigo original do Peter Chen. Apresenta um diagrama simples do modelo entidade-relacionamento.
The Entily-Relaticnship Model

ENTITY SET RELATIONSHIP
SET

ÉNTITY SET

Figura 2 - Figura do artigo original do Peter Chen

Nesse diagrama, podemos observar a presença das entidades EMPREGADO e PROJETO,
e do relacionamento trabalha-no-projeto. Na figura, é possível visualizar também o termo conjunto (set) de Entidade e de Relacionamento. Quando vamos definir uma entidade,geralmente, usamos uma instância do mundo real. Por exemplo, o funcionário
Thiago
Cavalcanti com o CPF 045034045-12. Essa instância vai ser usada para definir um Tipo deEntidade, neste caso, FUNCIONÁRIO.

O termo conjunto tentar expor o conceito de que a entidade FUNCIONÁRIO, por exemplo,
deve ser uma descrição de um conjunto de funcionários de uma empresa em um determinado momento do tempo. Você se lembra do conceito de instância? O entity set vai representar o conjunto de instâncias da entidade empregado.
Esse termo contribui para a formalização do modelo. Ele descreve, basicamente, o conjunto de objetos do mesmo tipo que são instanciados para cada tipo de entidade ou relacionamento. Perceba que o tipo representa a descrição da entidade funcionário (em termos de restrições e atributos), enquanto o conjunto trata das instâncias. Em nosso estudo não vamos nos preocupar muito com esse rigor. Usaremos a palavra entidade para definir uma abstração que representa um objeto sobre o qual queremos armazenar informações na nossa base de dados.
A entidades individuais que fazem parte de um conjunto são denominadas extensão de um conjunto de entidades. Assim, todos os funcionários de uma empresa são uma extensão do conjunto de entidades funcionários. Uma entidade pode ser concreta, como uma pessoa ou um livro, ou pode ser abstrata, como um feriado ou um conceito.
O mais importante da figura acima é observar que o modelo define um retângulo para representação de uma entidade e um losango para representação de um relacionamento.Temos ainda os atributos, que, embora não estejam desenhados na figura, são representados por uma elipse. Para finalizar, utilizamos linhas para fazer a ligação entre os elementos dos modelos.
Vejamos um exemplo de duas entidades (cliente e empréstimo) com seus respectivos atributos na figura abaixo.
Qcodclientej) ^teiefone^

'X

cliente

<f$az >

-emp—réstimo

<homé^> \ 'jdade?

Cdatanascimentq';

C codern préstim o Á ÇvalorJ

ATRIBUToS

Figura 3 - Diagrama entidade relacionamento

Já sabemos que os atributos são representados por elipses e que eles apresentam as propriedades ou características das entidades ou dos relacionamentos. É importante saber que os atributos também podem ser representados por círculos, ou ainda não serem representados para não sobrecarregar o diagrama.
Até aqui tratamos apenas dos elementos gráficos básicos do modelo, vamos,
então,
observar quais são as classificações de cada um dos elementos e como essa classificação influencia ou altera a representação gráfica de cada elemento. Começaremos pelos atributos, que podem ser:
Identificador ou Não Identificador

Toda entidade, normalmente, possui um conjunto de um ou mais atributos que são usados para identificar univocamente cada instância da entidade. Cada atributo que compõe esse conjunto é denominado atributo-chave ou identificador. Na notação padrão do diagramaER o nome aparece sublinhado dentro da elipse. Quando o diagrama utiliza círculos para representar os atributos, o círculo aparece preenchido conforme observamos na figura a seguir:
código nome endereço
PRATELEIRA

—O capacidade

—* número do corredor

—* número da prateleira

Figura 4 - Exemplo de identificadores simples e composto

Perceba que, se o conjunto de atributos identificadores for composto por apenas um atributo, denominamos ele de identificador simples. Por outro lado, se o conjunto possuir dois ou mais atributos, como na entidade prateleira da figura acima, denominamos esse conjunto de identificador composto. Resumindo:
Identificador de entidade

Conjunto de um ou mais atributos cujos valores servem para distinguir uma ocorrência da entidade das demais ocorrências da mesma entidade.
Pode ser simples ou composto.

Figura 5 - Identificador de entidade.

Existem algumas entidades que não possuem atributos suficientes para que cada uma das suas instâncias seja identificada de forma unívoca. Falaremos sobre esse tipo de entidade, denominada entidade fraca, a seguir ... por enquanto, lembre-se que essa exceção existe. Agora, perceba que eu falei que a entidade fraca não possui atributos suficientes, logo, ela pode ter um atributo que fará parte da chave, mas que não a compõe totalmente. Esse atributo é de é denominado chave parcial e a notação gráfica é descrita abaixo:
ATRIBUTO CHAVE PARCIAL (ENTIDADES FRACAS)

Figura 6 - Notação gráfica para chove parcial.

Simples ou Compostos

Quando classificamos os atributos em relação a sua estrutura, podemos dividi-los em simples e compostos. Simples são aqueles atributos considerados atômicos ou indivisíveis.Em outras palavras, eles não são divididos em subpartes. Os compostos podem ser divididos em partes menores, essas partes representam atributos básicos com significados independentes.
Um exemplo de atributo simples seria CPF, um valor único e indivisível. Por outro lado,como representante dos atributos compostos podemos apresentar o endereço. Perceba que um endereço pode ser dividido em várias partes: nome da rua, número, complemento,CEP, bairro, cidade e país.

Monovalorados ou Multivalorados

Monovalorados são atributos que possuem apenas um valor para uma instância da entidade (exemplo: Idade). Multivalorados possuem mais de um valor para dada elemento de uma entidade. Perceba que esses valores estão associados ao mesmo domínio. (Exemplo: Telefones (88787981, 34141242, 46578741)).
Quando o projetista julgar necessário, ele pode impor limites inferiores e superiores para um determinado atributo multivalorado. Por exemplo, um banco pode limitar o número de telefones armazenados para um único cliente. Essa restrição não fica explícita na modelagem conceituai.
Armazenados ou Derivados

Atributos armazenados definem aqueles atributos que efetivamente são gravados no banco de dados. Já os atributos derivados são os atributos que podem ser obtidos a partir de um dado armazenado (exemplo: calcular a idade utilizando a data de nascimento).
Obrigatórios ou Opcionais

Atributos cujo valor seja exigido em todas as instâncias da entidade são denominados obrigatórios. Caso não seja, eles são denominados opcionais. Todos os atributos, no geral, são considerados obrigatórios e monovalorados. Essas propriedades podem ser descritas por dois valores entre parênteses (1,1). O primeiro valor refere-se à obrigatoriedade do atributo, já o segundo ao fato de só termos um valor no máximo.Vamos dar outro exemplo para você entender melhor... observe a figura abaixo:
CLIENTE

Í telefone (0, n)
O código

O nome

Figura 7 - Exemplo de atributo não obrigatório e multivalorado.

Na figura acima, telefone possui cardinalidade mínima 0, o que denota que ele é opcional.O atributo possui ainda cardinalidade máxima n o que significa que ele é multivalorado. Já os atributos código e nome são considerados obrigatórios e monovalorados, perceba que a notação (1,1) é omitida dos diagramas.
Descritivos, nominativos e referenciais

Uma outra forma de definir os atributos é quanto a finalidade ou função relacionada a uma entidade, estes podem ser classificados e identificados como:
Atributos descritivos: atributo que seja capaz de demonstrar, ou representar,características formadoras, ou pertencentes, a um objeto. (Ex: Data de nascimento, idade,
sexo.)

Atributos Nominativos: atributo que além de cumprirem a função de descritivos, também servem como definidores de nomes ou rótulos de identificação aos objetos aos quais pertencem. Perceba que todo atributo nominativo também é descritivo. (Ex: código do...,matrícula, número.)

Atributos Referenciais: atributo que não pertencem propriamente a entidade onde estão,
mas fazem algum tipo de referência dessa entidade com outra entidade. (Ex: Imagine uma entidade PRODUTO como um atributo ID_FABRICANTE).
Antes de continuar, gostaria de apresentar um rápido resumo dessas características vistas até aqui:
Figura 8 - Atributos no modelo entidade relacionamento.

Seguimos a nossa jornada através dos atributos. Nosso objetivo agora é entender o que são valores nulos e tratar de uma composição especial dos atributos: os atributos complexos.
Atributos nulos

Em alguns casos, uma entidade em particular pode não ter um valor aplicável para um atributo. Por exemplo, o atributo Numero_apartamento de um endereço só se aplica a endereços que estão em prédios de apartamento, e não a outros tipos de residências,como casas. De modo semelhante, um atributo Formacao_academica só se aplica a pessoas com esse tipo de formação.
Para tais situações, foi criado um valor especial, chamado NULO (NULL). Um endereço de uma casa teria NULL para seu atributo Numero_apartamento, e uma pessoa sem formação acadêmica teria NULL para Formacao_academica. NULL também pode ser usado quando não conhecemos o valor de um atributo para determinada entidade.
Resumindo, usamos o atributo nulo quando o valor para o atributo em questão é não aplicável ou desconhecido.
Atributos complexos

Em geral, os atributos compostos e multivalorados podem ser aninhados arbitrariamente.
Podemos representar o aninhamento arbitrário ao agrupar componentes de um atributo composto entre parênteses () e separá-los com vírgulas, e ao exibir os atributos multivalorados entre chaves {}. Esses atributos são chamados de atributos complexos.Vejamos um exemplo:

{Endereço_telefone({Telefone(Codigo_area,

Numero_telefone)},Endereco(Logradouro

(Numero, Rua, Numero_apartamento), Cidade, Estado, Cep))}

Vejam a seguir as representações gráficas dos atributos no modelo entidade-relacionamento. Observe que o segundo tipo se refere a atributo chave. Esse tipo de atributo é caraterizado pela linha é usada para sublinhar o atributo dentro da elipse. A ideia é que ele sirva como referência para encontramos uma instância específica de um conjunto de entidades.
CPF é um bom exemplo de chave. Se você me informar seu número de CPF e eu tiver acesso à base de dados da receita, eu conseguirei obter diversas informações a seu respeito. Neste caso CPF é um atributo monovalorado, simples e armazenado.
HORA DE

PRATICAR!

(Ministério da Economia - Especialista em Gestão de Projetos - 2020)

Com relação às informações contidas no modelo conceituai precedente, julgue o próximo item.
O modelo em questão apresenta um erro de construção, porque existem atributos declarados com nomes idênticos, o que impossibilita transformá-lo em um modelo lógico.
Comentários: Não existe nenhum erro no modelo em questão. É perfeitamente possível que,
em entidades distintas, existam atributos com o mesmo nome.
Gabarito: ERRADO

(Ministério da Economia - Especialista em Gestão de Projetos - 2020)

Com relação às informações contidas no modelo conceituai precedente, julgue o próximo item.
No tipo de modelo apresentado, é permitido que atributos sejam declarados tanto em entidade quanto em relacionamento.
Comentários: Os atributos são descrições ou características dos objetos e dos relacionamentos em um modelo conceituai. Logo,podemos incorporar ou associar os atributos às entidades e aos relacionamentos.

Gabarito: CERTO

Agora vamos tratar dos relacionamentos que são usados para associações entre as entidades. No diagrama ER, os relacionamentos são representados por losangos. Observe a figura abaixo, ela representa um relacionamento entra duas entidades.
Figura 1 - Exemplo de relacionamento.

Perceba que cada departamento pode ter várias pessoas. Cada par que relaciona uma instância de pessoa a um departamento específico é denominado ocorrência.
Eles podem ser classificados das seguintes formas:

Quanto ao grau que representa o número de entidades que participam desse relacionamento. Podendo ser unário, binário, ternário ..
Quanto à razão de cardinalidade quando, analisando um relacionamento binário,
podemos especificar o número máximo de instâncias de cada entidade presente no relacionamento, este valor é definido como razão de cardinalidade. Podendo receber os seguintes valores: 1:1, 1:N, N:1 e M:N.
A cardinalidade pode ser visualizada no diagrama conforme a figura abaixo. O diagrama apresenta entre parênteses dois números naturais. O primeiro representa a cardinalidade mínima e o segundo a cardinalidade máxima. Perceba que se o primeiro número for zero teremos um relacionamento opcional, caso seja maior ou igual que um teremos um relacionamento obrigatório.
"Uma editora pode publicar N livros.

Um livro é obrigatoriamente publicado por no máximo 1 editora."

Vamos agora fazer mais uma questão sobre o assunto:

HORA DE

PRATICAR!

Ministério da Economia - Especialista em Gestão de Projetos - 2020)

Com relação às informações contidas no modelo conceituai precedente, julgue o próximo item.
Um PAÍS pode, ou não, tributar um SERVIÇO.

Comentários: A cardinalidade mínima do relacionamento é zero, desta forma, é possível existir um país que não tribute determinado serviço.
Gabarito: CERTO

(Ministério da Economia - Especialista em Gestão de Projetos - 2020)

Com relação às informações contidas no modelo conceituai precedente, julgue o próximo item.
Todos os serviços, independentemente do tipo de cada um deles, são tributados por todos os países
Comentários: Perceba que essa é uma questão de interpretação da cardinalidade mínima do relacionamento. Para todos os serviços serem tributados o relacionamento deveria ser obrigatório, quando na realidade é opcional.Assim, cada serviços pode ou não ser tributado dependendo da legislação tributária do país em questão. Logo, temos uma alternativa errada.
Gabarito: ERRADO.

(Ano: 2017 Banca: CESPE Órgão: TRE-PE Prova: Analista Judiciário - Análise de Sistemas)
Assinale a opção que corresponde ao tipo de restrição de integridade expressa no próprio diagrama de entidades e relacionamentos no modelo relacional.
a) dependência b) enumeração c) normas de aceitação d) cardinalidade e) repetição
Comentário: Observe que, pelas definições que acabamos de explicar a alternativa que se adequa melhor a nossa questão está na letra D.
Gabarito: D.

AUToRRELACIoNAMENTo oU RELACIoNAMENTo RECURSIvo.

Outra situação importante que podemos encontrar em um modelo conceituai é o autorrelacionamento. Neste caso o diagrama representa um relacionamento entre uma entidade e ela mesma. Ou seja, quando um tipo entidade participa mais de uma vez de um relacionamento em papeis diferentes. O papel de entidade em relacionamento é a função que uma instância da entidade cumpre dentro de uma instância do relacionamento. Vejamos um exemplo de papeis em um autorrelacionamento:
Figura 2 - Autorrelacionamento com papeis.

Um outro exemplo desta afirmação é o relacionamento gerencia do tipo de entidade empregado. Para entender melhor está situação vamos fazer uma questão do CESPE sobre o assunto:
HORA DE

PRATICAR!

(Ano: 2016 Banca: CESPE Órgão: TRE-PI Prova: Analista Judiciário - Análise de Sistemas)
Considere que existe uma entidade PESSOA com um relacionamento denominado
CASAMENTO que pode associar diversas ocorrências na mesma entidade PESSOA. De acordo com as propriedades do diagrama entidade-relacionamento, o conceito desse relacionamento (CASAMENTO) pode ser definido como a) generalização.
b) relacionamento binário.

c) autorrelacionamento.

d) entidade associativa.

e) especialização.

Comentário: Observamos que CASAMENTO é um relacionamento que envolve duas ocorrências da entidade PESSOA. Para facilitar o entendimento, em geral costumamos identificar o papel de cada entidade no relacionamento (para o exemplo, marido e esposa). Veja a figura abaixo para fixar ainda mais o conteúdo em questão:
Após essa rápida análise, podemos assinalar o gabarito na alternativa C.

Gabarito: C.

Agora vamos fazer mais um esquema para descrever os relacionamentos

Figura 3 - Resumo dos relacionamentos

ENTIDADE FoRTE X ENTIDADE FRACA

Vamos agora tratar de entidade fraca e forte.

Uma entidade fraca não possui entre seus próprios atributos um conjunto que possa ser definido como chave primária. São identificadas por estarem relacionadas a entidades específicas de outro tipo entidade conhecidas como entidade forte. Geralmente um atributo da entidade forte faz parte da chave primária da entidade fraca.
Obs.: Veja que a entidade fraca pode ter um atributo-chave, que vai fazer parte da chave primária no modelo relacional (veremos isso na próxima aula) contudo para compor a sua chave primária, que consegue identificar univocamente uma instância da entidade, você precisa da ajuda de um ou mais atributos da entidade forte.
Entidade forte ou identificador/proprietária. Pode definida como uma entidade que consegue especificar sua chave primária dentro do conjunto dos seus atributos. Uma observação importante é que chamamos o tipo relacionamento entre a entidade fraca e seu tipo proprietário de relacionamento identificador.
Vejamos um exemplo de entidade fraca e relacionamento identificador. O exemplo abaixo mostra que o conjunto de entidades Ementa só existe se existirem Disciplinas, portanto,a participação no relacionamento Possui é obrigatória.
Figura 1 - Relacionamento identificador e entidade fraca

Antes de darmos continuidade ao nosso assunto, vamos ver como a FCC já cobrou esse assunto em provas anteriores.
HORA DE

PRATICAR!

BANCA: FCC ANO: 2015 ÓRGÃO: TRT - 15^ REGIÃO (CAMPINAS-SP) PROVA: TÉCNICO
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

O modelo E-R utiliza alguns conceitos básicos como entidades, atributos e relacionamentos. Os atributos podem ser classificados em obrigatórios, opcionais,
monovalorados, multivalorados, simples ou compostos. Nesse contexto, uma entidade chamada Empregado possui os atributos ID, Nome, TelefonesContato, CNH e Endereço.Os atributos TelefonesContato e Endereço são classificados, respectivamente, em

A monovalorado e multivalorado.
B simples e multivalorado.

C multivalorado e composto.
D obrigatório e opcional.

E composto e multivalorado.

Comentário: Essa questão está avaliando o entendimento de atributos em modelos ER. A questão fala de dois atributos específicos: TelefonesContato e Endereço.
Começando pelo TelefonesContato, imagine uma lista de telefones pertencentes a uma determinada pessoa: 6134432323,6134564343, 6132423234. Veja que eles são um conjunto de valores do mesmo tipo. Esse tipo de atributo é conhecido como multivalorado.
O outro atributo é o Endereço, pense no endereço da sua casa. Ele geralmente é composto de um nome de rua, número, bairro,cidade e cep. Veja que o atributo possui uma sequência de valores de tipos diferentes, por isso chamamos ele de composto.
Considerando os dois parágrafos anteriores temos multivalorado e composto como resposta para a questão. Gabarito: C.
MELHoRIAS No MoDELo E-R

Os diagramas ER discutidos até agora representam os conceitos básicos de um esquema de banco de dados. No entanto, alguns aspectos de um banco de dados, tais como herança entre os vários tipos de entidade não podem ser expressos utilizando o modelo básico ER. Estes aspectos podem ser expressos através de uma evolução do modelo ER. Os diagramas resultantes são conhecidos como diagramas ER estendido e o modelo é chamado de modelo EER.
O modelo básico ER pode representar os aplicativos de banco de dados tradicionais, tais como a aplicação de processamento de dados típico de uma organização. Por outro lado,o modelo EER é usado para representar as aplicações novas e complexas de banco de dados, tais como telecomunicações, Sistemas de Informação Geográfica (GIS), etc. Esta seção discute os recursos dos modelos ER estendido, incluindo especialização,generalização e agregação e sua representação utilizando EER diagramas.

ESPECIALIZAçÃo E GENERALIZAçÃo

Em algumas situações, um tipo de entidade pode ser visto como agrupamentos de outras entidades, de tal maneira as entidades de nível inferior possuem todas as características da entidade de nível superior. Por exemplo, o tipo de entidade BOOK (livro)pode ser classificado em três tipos, a saber, TEXTBOOK, LANGUAGE_BOOK, e NOVEL. Estes tipos de entidade são descritos por um conjunto de atributos que inclui todos os atributos do tipo de entidade livro e um conjunto adicional de atributos que os diferenciam uns dos outros.
Estes atributos adicionais são também conhecidos como atributos locais ou específicos.

Por exemplo, o tipo de entidade TEXTBOOK pode ter o atributo adicional Assunto (por exemplo, Computação, Matemática, Ciências, etc.), LANGUAGE_BOOK pode ter o atributoIdioma (por exemplo, francês, alemão, japonês, etc.), e a entidade do tipo NOVEL
(romance)
pode ter um atributo TIPO (Ficção, Mistério, Fantasia, etc.). Este processo de definir os subgrupos de um determinado tipo de entidade é chamado especialização.
O tipo de entidade que contém os atributos comuns é conhecido como superclasse,
e o tipo de entidade que é um subconjunto da superclasse, é conhecida como a sua subclasse. Por exemplo, o tipo de entidade livro é uma superclasse e os tipos de entidadeTEXTBOOK, LANGUAGE_BOOK e NOVEL são suas subclasses. Este processo de refinar os tipos de entidade de nível superior (superclasse) em tipos de entidade de nível inferior(subclasse), acrescentando alguns recursos adicionais para cada um deles é uma abordagem de projeto top-down.
O processo de design também pode seguir uma abordagem bottom-up no qual vários tipos de entidade de nível mais baixo são combinados com base em características comuns para formar os tipos de entidade de nível superior. Por exemplo, o designer de banco de dados pode identificar primeiro o tipo de entidade TEXTBOOK e em seguida os tiposLANGUAGE_BOOK e NOVEL e, por fim, combinar os atributos comuns destes tipos de entidades para formar uma entidade de nível superior BOOK. Este processo é conhecido como generalização.
«MJ

fh^TOME

NOTA!

Em termos simples, a generalização é o inverso da especialização.

As duas abordagens são diferentes em termos de partida e ponto final.
Especialidade começa com um único tipo de entidade de nível mais alto e termina com um conjunto de tipos de entidades de nível inferior que têm alguns atributos adicionais que as distinguem umas das outras.
Generalização, por outro lado, inicia-se com a identificação de um número de tipos de entidade de nível mais baixo e termina com o agrupamento dos atributos comuns para formar um único tipo de entidade de nível mais alto. Generalização representa as semelhanças entre os tipos de entidade de nível inferior. No entanto, suprime as suas diferenças.
Especialização e generalização podem ser representadas graficamente, com a ajuda de um diagrama ERE em que a superclasse está ligada por uma linha a um círculo, que por sua vez está ligado por uma linha a cada subclasse que foi definida. O símbolo em forma de 'u'em cada linha que liga uma subclasse ao círculo indica que a subclasse é um subconjunto da superclasse. O círculo pode ser vazio ou pode conter um símbolo "d" (para disjunção) ou"o" (para sobreposição). Vejam a figura abaixo para esclarecer a nossa explicação.

Antes de falarmos mais detalhes sobre disjunção e sobreposição vamos definir o que vem a ser atributo de herança. Como discutido anteriormente, os tipos de entidade de nível superior e de nível inferior são criados com base em seus atributos. O tipo de entidade de nível superior (ou superclasse) tem os atributos que são comuns a todos os seus tipos de entidade de nível mais baixo (ou subclasses). Esses atributos comuns da superclasse são herdados por todas as suas subclasses. Esta propriedade é conhecida como atributo de herança.
DISJUNçÃo E SoBREPoSIçÃo

Dois tipos de restrições, denominados, disjunção e sobreposição, podem ser aplicados a uma especialização. Estas restrições determinam se uma instância de entidade de nível superior pode ou não pertencer a mais de um tipo de entidade de nível mais baixo dentro de uma única especialização.
Restrição de disjunção: Esta restrição define que a mesma instância de entidades de nível superior não pode pertencer a mais de um tipo de entidade de nível inferior. Isto é,a subclasses de qualquer superclasse deve ser separada. Por exemplo, uma entidade do tipoBOOK pode pertencer a um TEXTBOOK ou NOVEL, mas não ambos. Uma especialização definida por um atributo em que na definição deste atributo ele possua um valor único implica em uma restrição de disjunção. A restrição de disjunção é representada por um símbolo "d" escrito em um círculo num diagrama ERE como mostrado na figura.
Restrição de sobreposição: Esta restrição estabelece que a mesma instância de entidades de nível superior pode pertencer a mais de um tipo de entidade de nível inferior. Isto é, as subclasses de qualquer superclasse não precisam ser separadas e as entidades podem se sobrepor uma à outra.
Em termos de diagrama ERE, a restrição de sobreposição é representada por um símbolo
'o' escrito em um círculo que une à superclasse com suas subclasses. Por exemplo, os tipos de entidade PLAYER e POLITICIAN mostram uma restrição de sobreposição, uma celebridade pode ser um jogador bem como um político (ver figura). Da mesma forma, uma entidade do tipo BOOK pode pertencer a ambos TEXTBOOK e LANGUAGE_BOOK, desde que o livro sobre idioma também possa ser um livro prescrito em uma disciplina.
(Ano: 2016 Banca: CESPE Órgão: TRE-PI Prova: Técnico Judiciário - Operação de
Computadores)

Acerca do modelo entidade-relacionamento estendido, assinale a opção correta.

a) Uma restrição de disjunção pode ser aplicada a uma especialização, na qual deve ser especificado que as subclasses da especialização devem ser mutuamente exclusivas.
b) A generalização é o resultado da separação de um tipo-entidade de nível mais alto
—
superclasse — e forma vários tipos-entidades de nível mais baixo — subclasse.

c) Uma entidade, que é membro de uma subclasse, nem sempre herda todos os atributos da entidade como um membro da superclasse.
d) O modelo em questão incorpora conceitos de modelagem entidade-relacionamento,
herança, encapsulamento e polimorfismo.

e) A simbologia do referido modelo é a mesma do modelo entidade-relacionamento, não havendo novas representações.
Comentário. Observem que essa questão trata do assunto que acabamos de estudar. A restrição de disjunção afirma que uma instância de entidade só pode ser especializada para apenas um dos subtipos. Já a sobreposição permite que uma instância possua as características de mais de uma classe filha. Analisando as alternativas acima podemos afirmar que o gabarito se encontra na alternativa A.
Gabarito: A

RESTRIçÃo PARTICIPAçÃo

A última restrição que pode ser aplicado a generalização ou especialização, é a restrição participação ou integralidade. Ela determina se uma entidade no conjunto de entidades de nível superior deve ou não pertencera, pelo menos, um dos conjuntos de entidades de nível inferior. A restrição de participação pode ser total ou parcial.
Especialização Total: Especifica que cada entidade de nível superior deve pertencer a,
pelo menos um, dos tipos de entidade de nível inferior na especialização. A Figura (a)
mostra a especialização total do tipo de entidade BOOK. Aqui, cada entidade livro deve pertencer a um ou outro TEXTBOOK ou LANGUAGE BOOK ou NOVEL. A especialização total é representada por linhas duplas que ligam a superclasse com o círculo.
Especialização parcial: Ela permite que algumas das instâncias de tipo de entidade de nível superior não pertencerem a qualquer um dos tipos de entidade de nível inferior.A
figura (b) mostra a especialização parcial do tipo de entidade BOOK, como todos os livros não necessariamente pertencem às categorias TEXTBOOK ou LANGUAGE BOOK, alguns podem pertencer à categoria NOVEL, por exemplo.
ACREGAçÃo/ENTIDADE ASSoCIATIvA

Os diagramas ER discutidos até agora representam as relações entre duas ou mais entidades. Um diagrama de ER não pode representar os relacionamentos entre relacionamentos. No entanto, em algumas situações, é necessário utilizar algum artifício para representar uma relação entre os relacionamentos. A melhor forma de representar estes tipos de situações é por meio da agregação. O processo através do qual podemos tratar os relacionamentos como entidades de nível superior é conhecido como agregação.
Por exemplo, em um banco de dados de livros (BOOK), o relacionamento ESCREVE, entre as entidades autor e livros, pode ser tratado como uma entidade de nível superior chamadaESCREVE (WRITES). O relacionamento ESCREVE e as entidades autor e livros são agregados em um único tipo de entidade para mostrar o fato de que uma vez que o autor escreveu um livro só então que ele poderá ser publicado.
O tipo de relacionamento PUBLISHED_BY pode ser mostrado entre o tipo de entidade editor e ESCREVE como mostrado na figura abaixo. O tipo de relacionamento PUBLISHED_BY é um relacionamento muitos-para-um. Isso implica que um livro escrito por um grupo de autores pode ser publicado por uma única editora; no entanto, um editor pode imprimir muitos livros escritos por diferentes autores.
HORA DE

PRATICAR!

(Ministério da Economia - Especialista em Gestão de Projetos - 2020)

Com relação às informações contidas no modelo conceituai precedente, julgue o próximo item.
A entidade SERVIÇO é um exemplo clássico de entidade associativa ou entidade fraca.

Comentários: No modelo em questão não temos nenhuma entidade fraca ou associativa.

Gabarito: ERRADO

(BANCA: CESPE ANO: 2010 ÓRGÃO: INMETRO PROVA: PESQUISADOR - GOVERNANÇA
DE TI)

Considerando a figura acima, que ilustra um modelo conceituai, assinale a opção correta.
A As entidades pessoa física e pessoa jurídica são exemplos de generalização/especialização, conceito que envolve a ideia de herança de propriedades.Herdar propriedades significa que cada ocorrência da entidade especializada possui, além de suas propriedades (atributos, relacionamentos e generalizações ou especializações),também as propriedades de ocorrência da entidade genérica correspondente.

B A cardinalidade do relacionamento entre filial e cliente define que pode existirfilial sem clientes, e ainda, que os clientes podem existir sem estar vinculados a nenhuma filial.
C Telefone é exemplo de atributo opcional.

D No modelo apresentado, entidades, relacionamentos, cardinalidade e identificadores estão corretos e consistentes.
E As entidades cliente, pessoa física e pessoa jurídica apresentam relacionamento do tipo ternário ou de grau maior, que são modelados usando-se uma entidade associada, por meio de relacionamentos binários, a cada uma das entidades que participam do relacionamento ternário.
Comentário. Primeiramente gostaria de fazer um comentário sobre o diagrama da questão. Quando apresentamos esse tipo de notação, os círculos pretos representam atributos chave das entidades e os círculos brancos representam atributos não chave.Outro ponto é a presença da restrição estrutural definindo os valores mínimos e máximos de cada entidade no relacionamento.Feito as considerações vamos analisar as alternativas, começando pela letra A que é a nossa resposta. Vejam que o examinador que saber se você entende que, quando temos especializações dentro de um diagrama conceituai, as entidades que são subclasses herdam os atributos e relacionamentos das suas superclasses.
A letra B faz uma leitura errada do relacionamento entre cliente e filial. O correto seria dizer que uma filial atende a zero até n clientes e um cliente é atendido por uma e apenas uma filial.
Para responder a alternativa C precisamos entender o que significar o " (l,n) " ao lado do atributo telefone da entidade cliente.Podemos dizer que ele representa um atributo multivalorado, pois um cliente pode ter mais de um telefone e obrigatório, pois cada cliente precisa ter, no mínimo, um telefone.
Na alternativa D temos que encontrar um erro no diagrama. Precisamos verificar que o nome filial está grafado como chave primária da entidade filial, o que não faz sentido. Portanto o diagrama não está 100% correto.
Por fim, a alternativa E, as entidades listadas não representam um relacionamento ternário, é sim uma relação de generalização/especialização.
Gabarito: A.

OUTRAS REPRESENTAçõES CoNCEITUAIS

Apresentaremos abaixo outras opções de notações conceituais que estão presentes na maioria das ferramentas de modelagem. Optei por mantê-las aqui apenas para que você possa usar como fonte de consulta rápida quando estiver resolvendo questões sobre modelagem conceituai.
NoTAçÃo DE BARkER

Nós usamos o termo notação de Barker (Barker Notation) para a notação conceituai discutida no tratamento clássico de Richard Barker (1990). Essa notação tem sua origem no final da década de 1980 no CACI no Reino Unido, a notação foi adotada mais tarde pelaOracle Corporation em suas ferramentas de projeto (CASE - Computer-Aided
Software
Engineering).

A Oracle agora suporta UML - Unified Modeling Language - como uma alternativa para a notação Barker ER, embora para aplicações de banco de dados, muitos projetistas ainda preferem a notação Barker em vez de UML. A Embarcadero adicionou suporte básico para a notação Barker em seu produto EA/Studio. Embora existam dezenas de dialetosER,
consideramos a notação Barker pode ser uma das melhores notações de ER, pois tem com amplo apoio na indústria.
As convenções básicas estão ilustradas na figura abaixo. Tipos de entidade são mostrados como retângulos de cantos arredondados com seu nome em letras maiúsculas. Os atributos são escritos abaixo do nome do tipo de entidade. Algumas informações de restrição podem aparecer antes de um nome de atributo. Um indica que o atributo é a chave primária da entidade, ou um componente da chave.
/ \

EMPREGADO

## * NumEmp

* NomeEmp o FoneEmp
\ 7

Figura 1 - Entidade na notação de Barker

O "*" ou ponto escuro indica que o atributo é obrigatório (ou seja, cada instância na população banco de dados do tipo de entidade deve ter um valor não nulo registrado para este atributo). Um "o" indica que o atributo é opcional. Alguns projetistas utilizam um ponto para indicar que o atributo não é parte do identificador ou da chave. Outra característica é que os nomes dos atributos não podem se repetir na mesma entidade.
Relações são restritas a relacionamentos binários (sem unários,
ternários ou relacionamentos mais longos) e são descritos por linhas, que podem ser contínuas ou tracejadas, com um nome que representa o papel da entidade no relacionamento. Esta colocação de nome supera o problema de ambiguidade na descrição do relacionamento.Assim, ambas as leituras da direita para a esquerda ou em sentido inverso podem ser exibidas e descritas em uma relação binária, cada qual em uma das extremidades da linha.Isso faz com que a notação Barker seja superior a UML para verbalizar relacionamentos.
Vejam um exemplo na figura abaixo:

Figura 2 - Notação de Barker

Na figura acima podemos observar uma linha tracejada e uma linha contínua.
Os relacionamentos são classificados da seguinte forma:
1. Relacionamento Obrigatório: Um relacionamento obrigatório especifica que cada instância de uma entidade deve estar relacionada a outra instância. Isso é representado por uma linha reta. Veja o caso entre times e jogadores. Cada jogador deve ser membro de um time. E um time deve ter pelo menos um jogador.
2. Relacionamento Opcional: Um relacionamento opcional especifica que cada instância de uma entidade pode estar relacionada a outra instância. Isso é representado por uma linha tracejada. Nesta situação, uma confederação pode organizar uma ou várias ligas,contudo, uma liga deve ser organizada (OBRIGATORIAMENTE) por uma confederação associadas a mesmas.
Uma coisa interessante da notação de Barker é a leitura das cardinalidades mínima e máxima. Perceba na figura abaixo:
Cada PEDIDO deve ser feito por um e apenas um COSUMIDOR

Talvez não tenha ficado tão claro ainda. Vamos ver um exemplo com um relacionamento de cardinalidade máxima N (muitos). O que eu quero que você perceba, é que,diferentemente da cardinalidade mínima do modelo E-R tradicional, na notação de Barker a obrigatoriedade e a cardinalidade máxima estão de lados opostos da figura.
Cada CONSUMIDOR pode ser o solicitante de um ou mais PEDIDOS

A figura acima apresenta um relacionamento com uma cardinalidade opcional e com múltiplos valores. Portanto, uma linha tracejada é desenhada do lado da entidade consumidor e a sentença de relação "é solicitante de" que descreve o papel é escrita abaixo desta linha. Um pé de galinha é desenhado ao lado da entidade PEDIDO para mostrar a relação de múltiplos valores. Já um pedido deve (linha contínua) ser solicitado por um e apenas um consumidor.
A notação de Barker apareceu muito pouco em provas de concursos. Use o texto acima como referência para seus estudos. Vamos em frente!
NoTAçÃo DE PÉ-DE-CALINHA

Outras notações podem ser usadas para representar modelos conceituais, uma das opções mais conhecidas é muito usada para representar relacionamento entre entidades.Conhecida no português como diagrama pé-de-galinha ou, no inglês, crows feet notation.
Apresentamos a seguir uma explicação gráfica dos principais elementos desta notação.

Uma entidade

Uma linha representa um relacionamento. O
texto contem um verbo que descreve.

Um relacionamento do tipo um e exatamente um ou muito (um ou mais)
Um relacionamento do tipo zero ou um para muitos (zero ou mais)
Um relacionamento do tipo muitos pra muitos,
sendo em ambos os lados obrigatórios (um ou mais)
HORA DE

PRATICAR!

(BANCA: FCC ANO: 2015 ÓRGÃO: TRT - 15^ REGIÃO (CAMPINAS-SP) PROVA: TÉCNICO
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO)

Para representar o relacionamento entre entidades no modelo E-R, várias notações foram criadas, como a da Engenharia da Informação, criada por James Martin. Com relação a esta notação, considere o relacionamento abaixo.
Departamento Empregado

Neste relacionamento,

A podem haver departamentos cadastrados sem nenhum empregado relacionado a ele.
B todo departamento cadastrado deverá ter, obrigatoriamente, pelo menos, um empregado.
C um mesmo empregado pode estar associado a muitos departamentos.
D somente dois departamentos poderão ser cadastrados.

E somente três empregados poderão ser relacionados a cada departamento.

Comentário. Vamos aproveitar a questão para falar de outra notação conceituai. A abordagem de
Engenharia da Informação (El)
ou sistemas de informação começou com o trabalho de Clive Finkelstein na Austrália e do CACI no
Reino Unido, mais tarde foi adaptada por James Martin. James ficou conhecido como responsável pelo sucesso e propagação da notação. Existem diferentes versões de notações para El, sem um padrão único. De uma forma ou outra, a El é suportada por muitas ferramentas de modelagem de dados e é uma das notações mais populares para o projeto de banco de dados.
A notação de El é semelhante à notação de Barker, ela apresenta a frequência máxima de um papel através da marcação na extremidade da linha do relacionamento. Mas, ao contrário da notação Barker, a notação da El apresenta também a possibilidade de configuração opcional/obrigatória. O elemento gráfico mais próximo da entidade representa o número máximo de elementos:apenas um no caso da barra vertical (|) ou vários ( > ou <). O outro elemento gráfico representa a obrigação (|) ou opção (o).Veja a figura abaixo.

IE

n:1

both roles optional

1:n:

both roles optional n:1
first role mandatory

1:n first role mandatory
1:1

first role mandatory m n first role mandatory
Vejam que pela figura acima podemos inferir do diagrama da questão que pode haver departamento cadastrado sem nenhum empregado associado a ele. Ou ainda, cada departamento possui de zero até n empregados. Agora, por outro lado, cada empregado participa de um e apenas um departamento. Não existe a opção de um empregado existir sem um departamento relacionado. Sendo assim confirmamos nossa resposta na alternativa A.
Gabarito: A

NoTAçÃo IDEFIX

Vamos aproveitar para apresentar outra notação bastante utilizada em provas de concursos:
a notação IDEF1X. Embora aplicada no nível conceituai, incorpora em suas raízes muitas características de projeto de banco de dados (modelagem lógica). Sua diagramação dependente de conceitos como chaves e dependências de identificação. Seus elementos podem ser divididos em entidades, relacionamentos, atributos e subtipos/supertipos.
Abaixo temos um exemplo de duas entidades independentes, um relacionamento entre elas e uma descrição dos espaços onde devem aparecer os atributos chaves e os demais atributos em uma entidade.
I
I

Entidades Independentes

Atributos - chave primária
Demais atributos

A figura a seguir mostra como os elementos são definidos para construção de diagramas na notação IDEF1X. Observem que as entidades podem ser segmentadas em independentes e dependentes. Esse conceito se baseia no fato da existência de uma entidade depender da existência de outra (s) entidade (s). Uma entidade dependente precisa de outra entidade independente para existir. Uma entidade independente,representada por um retângulo, é aquela que possui existência e identificador
(chave)
próprio, isto é, não composto por qualquer outro identificador de outra entidade.

Já uma entidade dependente, representada por um retângulo com os cantos arredondados,
pode ser dependente de identificador ou dependentes de existência. A dependência de identificador significa que uma entidade necessita para formar sua própria chave identificadora, da chave de outra entidade. Já a dependência de existência implica que,para que uma ocorrência de uma entidade filha exista, deverá existir, relacionada a ela, obrigatoriamente, uma ocorrência de entidade pai.
Veja que existe uma sutileza aqui. Para resolver essa diferença vamos observar algumas figuras.
Entity-A

Key-Attribute-A

Relation ;hip Name

<

Entity-B

Key-Attribute-A (FK)

Key-Attribute-B

y

Parent Entity

Identifying Relationship

**Child Entity

Na figura ao lado, a entidade A "empresta"
sua chave primária para a entidade B. Logo,
temos um relacionamento identificador, e,
logicamente uma dependência de identificador.
Observe que nessa situação a linha que liga as duas entidades é contínua. Isso demonstra a obrigatoriedade do relacionamento.
Assim, neste exemplo, a chave primária da entidade pai participa da chave primária da entidade filha!
Uma entidade pai em um relacionamento não identificado mandatório pode ser uma entidade independente de identificador (como mostrado na entidade A da figura) ou uma entidade dependente de identificador dependendo dos outros relacionamentos (que não aparece na figura).
A entidade filha em um relacionamento não identificado mandatório será sempre uma entidade independente de identificador ao menos que a entidade seja também uma entidade filha em algum outro relacionamento identificador.
Neste caso, a chave primaria da entidade pai não participa da chave primaria da entidade filha,mas é um atributo obrigatório!

Entity-A

Key-Attribute-A

Relationship Naine i i
Entity-B

*Parent Entity

Mandatory Non-Identifying
Relationship

**Child Entity

Entity-A

Key-Attribute-A

Relationship Name ii ii
Entity-B

*Parent Entity

Optional Non-Identifying
Relationship

**Child Entity

Para finalizar vamos apesentar o relacionamento opcional não identificado.Neste caso, a chave primária da entidade pai não participa da chave primária da entidade filha e é um atributo opcional.
Dentro de cada entidade pode aparecer os atributos. Os atributos chave aparecem acima da linha que corta o desenho horizontalmente e os demais atributos aparecem abaixo dessa linha. Podemos colocar após a definição do nome dos atributos os termos (FK), (PK),(AKn), (O). Os três primeiros se referem,
respectivamente, a chave estrangeira, chave primária e chave alternativas. O 'n' representa uma numeração atribuída a chave alternativa.
O último termo (O) representa que o atributo em questão é opcional. Vejam a figura abaixo com o exemplo desta nomenclatura.
Empioyee empNr empName ssn (AK1)sex fax (O)WdgNr (FK)
roomNr (FK)

Room

'SldgNr (FK)
roomNr ste phoneNr (O)V 7

Na primeira figura apresentamos também a notação de cardinalidade dos relacionamentos e se eles são identificadores ou não. Por fim, abaixo temos uma figura que mostra como o comportamento de herança é descrito. Vejam que temos dois conceitos. O fato de ser uma herança completa ou incompleta, que diz respeito ao fato de todos os elementos terem uma especialização. Outro ponto é ser exclusivo ou inclusivo, neste caso analisamos se é permitido ou não que uma entidade tenha mais de uma especialização dentro das possibilidades.
Exclusiva

Inclusiva

Com isso terminamos nosso estudo de modelagem conceituai, a modelagem conceituai juntamente com o projeto lógico e físico são as principais etapas de um projeto de banco de dados. Veremos os aspectos do projeto lógico quando tratarmos do modelo relacional.
QUESTõES CoMENTADAS CESPE

< , HORA DE

PRATICAR!

1. CEBRASPE (CESPE) - Auditor de Finanças e Controle de Arrecadação da Fazenda
Estadual (SEFAZ AL) /2020

Com relação a banco de dados, julgue o item seguinte.

Com base no diagrama a seguir, é correto afirmar que um item na entidade Ambiente pode não relacionar-se com nenhum item na entidade Setor ou pode relacionar-se com vários itens nesta entidade, enquanto um item na entidade Setor pode relacionar-se somente com um item na entidade Ambiente.

Comentário: Essa questão trata da cardinalidade descrita pelos valore entre parênteses na figura acima. Primeiro vamos analisar a cardinalidade do relacionamento POSSU/ partindo da entidade Ambiente. É importante atentar para algo que confunde muitos candidatos: a cardinalidade sempre está do lado oposto da entidade, devendo ser encontrada da seguinte forma:
Daí tiramos que uma instância da entidade Ambiente deve relacionar-se com um e somente um elemento na entidade Setor. Agora, vamos analisar partindo da entidade Setor:
Um item da entidade Setor pode relacionar-se com nenhum ou com vários itens da entidade Ambiente. Agora, vamos corrigir a assertiva:
Com base no diagrama a seguir, é correto afirmar que um item na entidade Ambiente deve relacionar-se com um e somente um item na entidade Setor, enquanto um item na entidade Setor pode relacionar-se somente com nenhum ou vários itens na entidade Ambiente. Concluímos, assim, que a assertiva está errada.
Gabarito: Errado

HORA DE

PRATICAR!

2. CEBRASPE (CESPE) - Ana Min (MPE CE)/MPE CE/Ciências da Computação/2020

Considerando o diagrama entidade- relacionamento precedente e os múltiplos aspectos que a modelagem de dados oferece ao analista para examinar os dados no contexto de uma aplicação de software, julgue o item subsecutivo.
No diagrama apresentado, a modalidade obrigatória que conecta transportador e transporta indica que, para todo alimento fabricado, é necessária uma ação de transporte.
Comentário: Essa questão reforça a importância de entender as notações complementares à notação ER. Neste caso, temos que lembrar que relembrar da notação pé-de-galinha.
A questão pediu para analisarmos a cardinalidade do relacionamento transporta partindo de alimento. Lembre-se que temos que olhar para o símbolo oposto à entidade que estamos analisando:
Note que um alimento fabricado pode ser transportado por nenhum ou vários transportadores. Dessa forma, não é necessária uma ação de transporte para todo alimento fabricado. Concluímos, assim, que a assertiva está errada.
Gabarito: Errado

« PRATICAR!

3. CEBRASPE (CESPE) - Ana Min (MPE CE)/MPE CE/Ciências da Computação/2020

Considerando o diagrama entidade- relacionamento precedente e os múltiplos aspectos que a modelagem de dados oferece ao analista para examinar os dados no contexto de uma aplicação de software, julgue o item subsecutivo.
A cardinalidade e a modalidade apresentada para a entidade fabricante mostram que obrigatoriamente um fabricante inicializa a ação de solicitação de distribuição,contratação de transporte e produção de alimento, o que caracteriza uma relação 1 *
n.

Comentário: Vamos analisar os relacionamentos que a entidade fabricante participa.
Lembre-se que temos que olhar para o símbolo oposto à entidade que estamos analisando.
Relacionamento autoriza

Otransportad

Um distribuidor é autorizado obrigatoriamente por um fabricante, enquanto um

| fabricante autoriza um ou vários distribuidores. Como é de costume representar a cardinalidade apenas pelos valores máximos, desprende-se que o relacionamento é do tipo 1:N.
Relacionamento produz

O transporta*

Um alimento é produzido obrigatoriamente por um fabricante, enquanto um fabricante produz um ou vários alimentos. A cardinalidade do relacionamento também é 1 :N.
Relacionamento contrata

Um transportador é contratado obrigatoriamente por um fabricante, enquanto um fabricante contrata nenhum ou vários transportadores. A cardinalidade do relacionamento, mais uma vez, é 1:N.
Perceba que, em todos os relacionamentos, a presença do fabricante é obrigatória: um distribuidor é autorizado obrigatoriamente por um fabricante; um alimento é obrigatoriamente produzido por um fabricante; e um transportador é obrigatoriamente contratado por um fabricante. Em todos os casos, o relacionamento é 1:N. Concluímos, assim, que a assertiva está correta.
Gabarito: Certo

. . HORA DE

PRATICAR!

4. CEBRASPE (CESPE) - Ass Min (MPC TCE-PA)/TCE-PA/lnformática/2019

As seguintes informações foram extraídas de um diagrama de entidades-
relacionamento no contexto de um banco de dados relacional.

De acordo com as informações do texto 9A1-I, assinale a opção correta, com relação à leitura das regras do negócio representadas no modelo apresentado.
a) Ao realizar uma reserva, o cliente pode escolher um ou vários trechos de voo.
Existem várias opções de aeronaves para o trecho reservado.

b) Ao realizar uma reserva, o cliente pode escolher um ou vários trechos de voo, mas existe apenas uma aeronave alocada para o trecho reservado.
c) Ao realizar uma reserva, o cliente pode escolher apenas um trecho de voo, mas existem várias opções de aeronaves para o trecho reservado.
d) Um trecho de voo está relacionado a apenas uma reserva.

e) Ao realizar uma reserva, o cliente recebe um único número de assento, válido para todos os trechos que forem reservados.
Comentário: A questão acima apresenta um diagrama de entidades-relacionamento no contexto de um banco de dados. Vamos analisar cada uma das alternativas da questão:
a) Errado. A primeira parte está correta, o cliente pode escolher um ou vários trechos de voo. Porém, analisando os relacionamentos entre as entidades, não existem várias opções de aeronaves para o trecho reservado.
b) Correto. Conforme vimos na LETRA A. A primeira parte está correta e a segunda também.
c) Errado. O cliente pode escolher um ou vários trechos de voo. E não existem várias opções de aeronaves para o trecho reservado.
í d) Errado. Temos um relacionamento um para muitos. Um trecho de voo está relacionado a muitas reservas.
e) Errado. Ao realizar uma reserva, o cliente recebe um único número de reserva. O
número do assento está relacionado a reserva do trecho, o cliente irá receber um número de assento para cada trecho escolhido.
Assim, podemos encontrar nossa resposta na alternativa B.

Gabarito: B

HORA DE

PRATICAR!

5. CEBRASPE (CESPE) - Tec (EBSERH)/EBSERH/lnformática/2018

Tendo como referência o modelo lógico precedente, julgue o item a seguir.

A partir do modelo apresentado, infere-se que um hospital pode estar vinculado a várias universidades, pois a tabela Hospital apresenta cardinalidade (0, n).
Comentário: Um modelo lógico é um modelo de dados que representa a estrutura de dados de um banco de dados conforme vista pelo usuário do SGBD. Lembremos também que a cardinalidade expressa o comportamento (número de ocorrências)de uma entidade associada a uma ocorrência da entidade em apreço através do relacionamento A cardinalidade é expressa como Número (Mínimo, Máximo) pode ser mínima ou máxima:
* Máxima: informa a quantidade máxima de ocorrências de determinada entidade,
associada a uma ocorrência da entidade em apreço, usando o relacionamento;

* Mínima: informa a quantidade mínima de ocorrências de determinada entidade,
associada a uma ocorrência da entidade em apreço, usando o relacionamento.

Além disto, a cardinalidade é representada no lado oposto. Pela figura acima, (0,n)
faz referência a Universidade, e (1,1) faz referência a Hospital, o que já nos permite concluir que O ITEM ESTÁ ERRADO, pois a cardinalidade de Hospital é (1,1).
O modelo apresentado nos permite concluir que:

* Uma ocorrência de Universidade pode estar associada a várias ocorrências de
Hospital (determinada Universidade pode possuir vários Hospitais) e pode ainda não ter nenhuma correspondência;
Uma ocorrência de Hospital está associada a apenas uma ocorrência de Universidade

{determinado Hospital está vinculado a apenas uma Universidade). Aqui vemos,
portanto, OUTRO ERRO no item.

Gabarito: Errado

6. CEBRASPE (CESPE) - APF/PF/2018

Considerando o modelo entidade-relacionamento (ER) precedente, julgue o seguinte item, relativo a banco de dados.
Conforme o modelo ER em questão, um tipo de produto pode estar associado a somente 1 produto e cada produto possui um preço e uma descrição.
Comentário: Temos que lembrar que a leitura da cardinalidade do relacionamento entre duas entidades é feita de forma "cruzada", neste caso, cada produto está associado a um tipo de produto e cada tipo de produto pode estar associado a vários produtos. Logo, temos uma alternativa incorreta.
Gabarito: Errado

7. CEBRASPE (CESPE) - Ana Min (MPE PI)/MPE Pl/Tecnologia da lnformação/2018

Tendo em vista que, ao se desenvolver um sistema de vendas e compras para um cliente, devem-se descrever os produtos, as entradas, as saídas, o controle de estoque e o lucro das vendas, julgue o item subsequente, relativo à modelagem de dados para a aplicação descrita.
No sistema implementado, o cliente terá de cadastrar cada produto nos módulos de vendas e compras, pois a redundância será controlada pelo usuário, e não pela modelagem do banco de dados.
Comentário: A intenção de criar qualquer sistema computacional é, geralmente,
automatizar e facilitar uma determinada atividade do negócio. A modelagem de dados serve justamente para evitar a redundância dos dados, mantendo a unicidade dos dados para que não haja dados conflitantes no sistema. Uma possível correção para a assertiva seria:
"No sistema implementado, o cliente não terá de cadastrar cada produto nos módulos de vendas e compras, pois a redundância será tratada na fase da modelagem do banco de dados"
Logo, temos uma alternativa incorreta.

Gabarito: Errado

F PRATICAR!

8. CEBRASPE (CESPE) - AFA (SEFAZ RS)/SEFAZ RS/2018

No modelo entidade-relacionamento, as propriedades particulares que descrevem uma entidade são denominadas a) valores.
b) atributos.

c) chaves primárias.

d) relacionamentos.

e) instâncias.

Comentário: A questão trata dos conceitos básicos do modelo entidade-relacionamento. Os atributos caracterizam uma entidade, por exemplo, uma entidade
"Pessoa" e alguns atributos como nome, CPF, Identidade, Endereço, Data de nascimento. Consegue perceber que esses atributos estão descrevendo uma pessoa?Desta forma, já podemos marcar nossa resposta na alternativa B, mas vamos analisar as alternativas:
a) Valores são as instâncias ou os dados que serão efetivamente preenchidos para cada atributo. Por exemplo, o atributo data de nascimento pode conter o valor"05/10/1995".

c) Chaves primárias identificam unicamente uma instância numa determinada entidade ou relacionamento.
d) Relacionamentos associam uma ou mais entidades de acordo com a realidade que se quer modelar.
e) Instâncias são ocorrências em uma determinada estrutura de banco de dados,
podemos ter instância do banco de dados, de uma tabela ou de um atributo desta tabela.
Gabarito: B

HORA DE

PRATICAR!

9. CEBRASPE (CESPE) - Tec (FUB)/FUB/Tecnologia da lnformação/2018

Julgue o item seguinte, a respeito dos conceitos de modelagem de dados e níveis de abstração.
No modelo de entidade-relacionamento, uma entidade se caracteriza por um objeto do mundo real que possui um conjunto de propriedades; os valores de um subconjunto dessas propriedades podem identificar de maneira única a entidade.
Comentário: No geral, todas as entidades possuem um conjunto de atributos identificadores que conseguem identificar univocamente cada instância da mesma.Esse conjunto de atributos é chamado de chave primária por alguns autores. Logo,
temos uma afirmativa correta.

Gabarito: Certo

F PRATICAR!

10. CEBRASPE (CESPE) - Tec (FUB)/FUB/Tecnologia da lnformação/2018

Julgue o item seguinte, a respeito dos conceitos de modelagem de dados e níveis de abstração.
Na cardinalidade de mapeamento entre o conjunto de entidades X e Y de uma associação um-para-um, uma entidade em X é associada, no máximo, a uma entidade em Y, e uma entidade em Y é associada, no máximo, a uma entidade em X.
Comentário: Certo!! Na cardinalidade 1-1 cada elemento dos conjuntos de entidades que participam do relacionamento só pode estar associado a um elemento da outra entidade. Lembre-se do relacionamento entre armário e funcionário. Cada funcionário tem apenas um armário e cada armário é possuído por apenas um empregado. Afinal,você não vai querer compartilhar um local onde você guarda sua roupa de academia que você fez antes de ir pro trabalho com outra pessoal. :)
Gabarito: Certo h^F^
« PRATICAR!

11. Ano: 2018 Banca: CESPE Órgão: STJ Cargo: Técnico Judiciário - Suporte
Técnico

Acerca de banco de dados, julgue os itens que se seguem.

75 Em um diagrama MER, a entidade representa uma coisa concreta do mundo real,
enquanto as coisas abstratas são representadas pelo relacionamento entre as entidades.
Comentário: Os nomes ou as coisas do mundo real ou imaginário são sempre entidades no modelo entidade-relacionamento. O que representa os relacionamentos são os verbos ou ações associadas a cada entidade. Desta forma, temos a afirmação acima como incorreta.
Gabarito: Errado

« PRATICAR!

12. Ano: 2018 Banca: CESPE Órgão: STJ Cargo: Técnico
Judiciário -
Desenvolvimento de Sistemas Questão: 64 e 65

Julgue os itens a seguir, referentes à modelagem de dados.

64 Generalização é o processo de definição de um tipo de entidade a partir de duas ou mais entidades que possuem atributos em comum — por exemplo, as entidades carro e ônibus podem ser generalizadas na superclasse veículo.
Comentário: Sabemos que quando pensamos em um modelo de dados, uma possível hierarquia entre os dados pode ser construída de forma que a entidade pai tenha os atributos comuns as suas respectivas entidades filhas. A esse conceito dar-se o nome de generalização, que é justamente o mesmo conceito descrito na questão. Logo, a alternativa está correta.
Gabarito: Certo

F PRATICAR!

13. Ano: 2018 Banca: CESPE Órgão: TCM-BA Cargo: Auditor de Contas Questão:

A respeito de entidades, relacionamentos e tipos de chave, assinale a opção correta.
A Uma entidade fraca não possui seus próprios atributos chave.

B Toda relação deve possuir somente uma chave primária de atributo único.

C Um identificador ou chave é usado para determinar exclusivamente uma instância de um relacionamento entre entidades.
D A abordagem entidade-relacionamento permite somente relacionamentos binários e dos tipos 1:1 e 1:n.
E Uma entidade forte existe no banco de dados e possui atributos que a identificam sem que ela precise estar associada a outra entidade identificadora.
Comentário: Vejam que essa questão apresenta um conceito associado ao modelo entidade-relacionamento. Uma entidade forte significa que possui atributos suficientes para identificar de forma unívoca cada instancia ou elemento de um conjunto de entidade. Logo, podemos marcar a resposta na alternativa E. Vamos agora procurar os erros das demais alternativas.
A) Uma entidade pode ter um atributo que seja chave, contudo, ele sozinho não consegue identificar um elemento da entidade. Para compor a chave ele precisa de um atributo que vai ser definido na entidade forte a ele associada. Sendo assim, temos uma alternativa incorreta.
B) A chave primária de uma relação pode ser classificada em simples, quando possuir apenas um atributo, ou composta, quando tiver dois ou mais atributos. Sendo assim,temos mais uma alternativa incorreta.

C) Uma instância de relacionamento é uma associação entre entidades, que inclui exatamente uma entidade de cada tipo de entidade participante. A identificação do relacionamento é feita pela associação entre as chaves das entidades participantes do relacionamento.
D) Os relacionamentos binários admitem cardinalidade máxima 1:1, 1:N e N:M. Logo temos mais uma afirmação errada.
Gabarito: E.

F PRATICAR!

14. Ano: 2018 Banca: CESPE Órgão: STM Cargo: Programação de Sistemas
Questão: 61 a 65

Acerca dos conceitos de normalização de dados e dos modelos de dados, julgue os itens subsequentes.
63 O modelo conceituai, que reflete uma estrutura simplificada do banco de dados, é responsável por registrar como os dados estão armazenados no sistema de gerenciamento de banco de dados (SGBD).
64 Comparativamente aos usados pelos usuários leigos, os modelos de dados utilizados por programadores são considerados menos abstratos, pois contêm mais detalhes de como as informações estão organizadas internamente no banco de dados.
Comentário: Vamos comentar cada uma das alternativas acima.

63. Quem descrever como os dados são armazenados no sistema de gerenciamento de banco de dados é o modelo físico, ele o faz descrevendo o modo como os dados são salvos em meios de armazenamentos, como discos e fitas, sendo exigido a definição tanto dos dispositivos de armazenamento físico como dos métodos de acesso (físico) necessários para se chegar aos dados nesse dispositivos, o que o torna dependente tanto de software como de hardware. Novamente, temos mais uma alternativa incorreta.
64. Essa alternativa está correta. Quando descemos na hierarquia dos modelos de dado, aumentamos o nível detalhamento.
Gabarito: Errado Certo h^F^
P PRATICAR!

15. BANCA: CESPE ANO: 2014 ÓRGÃO: ANATEL PROVA: ANALISTA
ADMINISTRATIVO - DESENVOLVIMENTO DE SISTEMAS DE INFORMAÇÃO

Com base nos modelos de banco de dados, julgue os itens subsequentes.

[89] São empregados no projeto de aplicações de um banco de dados o modelo entidade-relacionamento (MER), que é um modelo representacional, e suas variações.
[90] O modelo de dados físico é considerado de baixo nível, o que significa que somente os sistemas gerenciadores de banco de dados conseguem interpretá-lo.
Comentário: Vimos ao longo da nossa aula que os modelos considerados representacionais, de implementação ou lógicos são os modelos em rede, hierárquico e relacional. Alternativa 89 está incorreta.
Os modelos de dados físicos definem a forma como os dados são armazenados nos discos. Não podemos restringir o seu entendimento ao SGBD, outros componentes,como o sistema operacional, devem ser capazes de ler ou interpretar os dados. Sendo assim, a alternativa 90 também está errada.
Gabarito: Errado Errado.

HORA DE

PRATICAR!

16. Ano: 2015 Banca: CESPE Órgão: TRE-PI Cargo: Operação de computadores -
Questão 40

De acordo com a notação para diagramas entidade-relacionamento, assinale a opção que descreve a representação acima disposta.
A entidade, atributo, atributo composto e atributo derivado

B relacionamento, atributo, atributo fraco e atributo multivalorado

C entidade fraca, atributo-chave, atributo multivalorado e atributo derivado
D entidade, atributo-chave, atributo multivalorado e atributo derivado

E entidade forte, atributo, atributo composto e atributo fraco

Comentários: Essa questão nos ajuda a relembrar a notação gráfica definida pelo modelo entidade-relacionamento. Os símbolos acima representam, respectivamente:
1. Uma entidade fraca, que significa que a instâncias dessas entidades não conseguem existir dentro do modelo sem a existência de uma instância na entidade pai, conhecida também como forte, proprietária ou identificadora.
2. Um atributo-chave, neste caso, todos os atributos que são caracterizados com essa linha sublinhada abaixo do seu nome fazem parte da chave da entidade. Quando apenas um atributo for sublinhado a chave é conhecida como simples. Caso mais de um atributo seja sublinhado a chave é dita composta.
3. As elipses concêntricas representam um atributo multivalorado. Neste contexto você pode ter várias instâncias de atributos associadas a uma única instância da entidade. O caso clássico de atributo multivalorado é telefone.
4. Um atributo derivado, ele pode ser calculado a partir de um ou mais atributos armazenados na base de dados. Desta forma, ele não precisa ser gravado na base de dados.
Após analisar cada uma das representações podemos encontrar nossa resposta na alternativa C.
Gabarito: C.

F PRATICAR!

17. Ano: 2015 Banca: CESPE Órgão: TRE-PI Cargo: Operação de computadores -
Questão 41

Acerca do modelo entidade-relacionamento estendido, assinale a opção correta.

A Uma restrição de disjunção pode ser aplicada a uma especialização, na qual deve ser especificado que as subclasses da especialização devem ser mutuamente exclusivas.
B A generalização é o resultado da separação de um tipo-entidade de nível mais alto

— superclasse — e forma vários tipos-entidades de nível mais baixo — subclasse.

C Uma entidade, que é membro de uma subclasse, nem sempre herda todos os atributos da entidade como um membro da superclasse.
D O modelo em questão incorpora conceitos de modelagem entidade-relacionamento,
herança, encapsulamento e polimorfismo.

E A simbologia do referido modelo é a mesma do modelo entidade-relacionamento,
não havendo novas representações.

Comentários: Vimos durante a aula que temos duas opções para herança no modelo entidade-relacionamento estendido. A disjunção, onde as entidades são mutuamente exclusivas e a sobreposição, esta restrição especifica que a mesma instância de entidades de nível superior pode pertencer a mais de um tipo de entidade de nível inferior.
L

J

Gabarito: A.

h^F^

« PRATICAR!

18. Ano: 2015 Banca: CESPE Órgão: TRE-PI - Questão 57

Considere que existe uma entidade PESSOA com um relacionamento denominado
CASAMENTO que pode associar diversas ocorrências na mesma entidade PESSOA.

De acordo com as propriedades do diagrama entidade-relacionamento, o conceito desse relacionamento (CASAMENTO) pode ser definido como
A generalização.

B relacionamento binário.
C autorrelacionamento.

D entidade associativa.
E especialização.

Comentários: Vamos analisar o conceito associado a cada uma das alternativas.

i Generalização se refere ao processo funcionalmente inverso da especialização no qual se identificam as características comuns que passarão a caracterizar uma nova superclasse que generaliza as entidades-tipo originais.
Relacionamento binário trata do relacionamento entre duas entidades.

Auto relacionamento trata do relacionamento de uma entidade com ela mesma, o exemplo clássico é o relacionamento gerencia entre um empregado e outro. Também se refere ao contexto da resposta da nossa questão
Por fim, entidade associativa que substitui a associação entre relacionamentos, a qual não é prevista pelo modelo ER, é um relacionamento que passa a ser tratado como entidade, permitindo o uso de relacionamento opcional.
Gabarito: C

PRATICAR!

19. BANCA: CESPE ANO: 2015 ÓRGÃO: MPOG PROVA: ANALISTA - ANALISTA EM
TECNOLOGIA DA INFORMAÇÃO

A respeito de modelo entidade-relacionamento e normalização, julgue os itens subsequentes.
[113] Em relações normalizadas, na primeira forma normal, toda tupla em toda relação contém apenas um único valor, do tipo apropriado, em cada posição de atributo.
[114] Sabendo que, nos relacionamentos ternários, a cardinalidade refere-se a pares de entidades, em um relacionamento ternário R entre três entidades A, B e C, a cardinalidade máxima de A e B dentro de R indica quantas ocorrências de C podem estar associadas a um par de ocorrências de A e B.
Comentário: A primeira forma normal diz que todo atributo deve ser atômico. Ou de outra forma, nenhum atributo pode ser composto ou multivalorado. A partir dessa definição podemos definir que em toda tupla cada um dos seus atributos deve ter apenas um valor de um tipo apropriado. A alternativa 113 está correta. Aproveitando para dizer que a primeira forma normal é parte da definição do modelo relacional. Ou seja, se eu disser que uma tabela do modelo relacional ela está automaticamente na primeira forma normal.
\n\n\n. estrategiaconcursos. com.br

Uma propriedade importante de um relacionamento é de quantas ocorrências de uma entidade podem estar associadas a uma determinada ocorrência através do relacionamento. Esta propriedade é chamada de Cardinalidade. Num relacionamento ternário a cardinalidade é definida pelo relacionamento de uma entidade com as demais conjuntamente. Vejam a figura abaixo:
Gabarito: Certo Certo.

HORA DE

PRATICAR!

20. BANCA: CESPE ANO: 2015 ÓRGÃO: TRE-GO PROVA: TÉCNICO DO
JUDICIÁRIO - PROGRAMAÇÃO DE SISTEMAS

Julgue os seguintes itens, a respeito da modelagem de dados.

[65] Considere a seguinte situação hipotética. Em um banco de dados referente a um curso, um aluno pode estar em mais de um curso ao mesmo tempo. Além disso, na tabela de cursos realizados por aluno, estão presentes as chaves estrangeiras aluno e curso. Nessa situação, tanto o código do curso como o código do aluno são chaves primárias nas tabelas curso e aluno, respectivamente.
[66] Ao se excluir uma tupla de um banco de dados, pode-se violar a integridade referencial desse banco por uma chave primária.
[67] Um conjunto de entidades que não possuem atributos suficientes para formar uma chave primária é definido como um conjunto de entidades fortes.
[68] Uma chave primária identifica um único valor de uma tupla no banco de dados e não possui mais de um atributo na tabela.
Comentário. Analisando a alternativa 65 podemos observar que trata de uma narrativa consistente e, portanto, correta.
Na questão 66 temos um erro ao disser que a exclusão de uma linha pode violar a integridade referencial por meio da chave primária, o certo seria dizer que pode existir uma violação de integridade por meio da chave estrangeira. Em outras palavras podemos pensar da seguinte forma: eu só posso excluir uma linha da tabela A se não existir nenhuma referência a ela em outra tabela X. Essa referência é feita por meio de uma chave estrangeira, presente na outra tabela X.
Na questão 67 o erro é atribuir a entidade forte o conceito de entidade fraca.

A alternativa 68 trata da chave primária de uma tabela. Essa pode ser definida sobre um ou vários atributos. Quando definida sobre mais de um atributo é necessário que a informação contida no conjunto de atributos da chave seja única para cada linha da tabela. Sendo assim podemos assinalar a alternativa como incorreta.
Gabarito: Certo Errado Errado Errado.

F PRATICAR!

21. BANCA: CESPE ANO: 2015 ÓRGÃO: STJ PROVA: TÉCNICO JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

A respeito da modelagem de dados e da qualidade de software, julgue os itens subsecutivos.
[84] O relacionamento no modelo entidade-relacionamento é uma associação intuitiva entre entidades, cujo número de entidades envolvidas é conhecido como hierarquia.
[86] Entidade-relacionamento é uma modelagem semântica cujo modelo resultante é estendido, e as entidades, nesse modelo, são definidas como um ente que pode ser distintamente identificado.
Comentário. A alternativa 84 foge de qualquer definição saudável ou característica do modelo entidade-relacionamento. Um modelo entidade-relacionamento é um modelo de dados para descrever os dados, informações de um domínio de negócio ou seus processos, de forma abstrata. Os principais componentes do modelo ER são as entidades e os relacionamentos que podem existir entre eles. Foi desenvolvido porPeter Chen e publicado em um artigo em 1976.

A questão 86, embora com um texto rebuscado, diz, basicamente, que o modelo ER
utiliza elementos com significados específicos para representar seus conceitos,
por exemplo, um retângulo representa uma entidade. O modelo carece de detalhes que são inseridos quando saímos da modelagem conceituai para um modelo lógico.Quanto nós analisamos uma modelagem conceituai cada entidade define algum objeto ou aspecto do mundo real que possui um escopo específico dentro do projeto. Cada entidade é única dentro do modelo.
Gabarito: [84] Errado [86] Certo.

22. Ano: 2016 Banca: CESPE Órgão: TCE-PA Prova: Auditor de Controle Externo -
Área Informática - Analista de Suporte

Considerando a figura apresentada, que ilustra o modelo de um banco de dados hipotético, julgue o item que se segue.
[1] A figura expõe um modelo lógico, uma vez que ele contém detalhes de implementação e é independente de um sistema gerenciador de banco de dados(SGBD).

Comentário: Analisando a figura acima podemos verificar que o diagrama apresenta características gráficas com alto nível de abstração. Esse tipo de modelo é conhecido como conceituai. Perceba que a assertiva diz que esse é um modelo lógico, o que não é verdade. Por isso podemos afirmar que a afirmação está incorreta.
Gostaria ainda de aproveitar o diagrama para fazer um comentário a respeito da notação dos atributos. Percebam que os atributos, associados a cada uma das entidades, estão representados por bolas e os nomes ou descrição deles aparecem fora da mesma. Essa é uma das notações alternativas para representação dos atributos.
Gabarito: Errado.

HORA DE

PRATICAR!

23. Ano: 2017 Banca: CESPE Órgão: TRE-PE Prova: Analista Judiciário - Análise de
Sistemas

Assinale a opção que corresponde ao tipo de restrição de integridade expressa no próprio diagrama de entidades e relacionamentos no modelo relacional.
a) dependência b) enumeração c) normas de aceitação d) cardinalidade e) repetição
Comentário: Observe que, pelas definições que acabamos de explicar a alternativa que se adequa melhor a nossa questão está na letra D.
Gabarito: D.

F PRATICAR!

24. Ano: 2016 Banca: CESPE Órgão: TRE-PI Prova: Analista Judiciário - Análise de
Sistemas

Considere que existe uma entidade PESSOA com um relacionamento denominado
CASAMENTO que pode associar diversas ocorrências na mesma entidade PESSOA.
De acordo com as propriedades do diagrama entidade-relacionamento, o conceito desse relacionamento (CASAMENTO) pode ser definido como a) generalização.
b) relacionamento binário.

c) autorrelacionamento.

d) entidade associativa.

e) especialização.

Gabarito: C.

25. Ano: 2016 Banca: CESPE Órgão: TRE-PI Prova: Técnico Judiciário - Operação de Computadores
Acerca do modelo entidade-relacionamento estendido, assinale a opção correta.

a) Uma restrição de disjunção pode ser aplicada a uma especialização, na qual deve ser especificado que as subclasses da especialização devem ser mutuamente exclusivas.
b) A generalização é o resultado da separação de um tipo-entidade de nível mais alto

— superclasse — e forma vários tipos-entidades de nível mais baixo — subclasse.

c) Uma entidade, que é membro de uma subclasse, nem sempre herda todos os atributos da entidade como um membro da superclasse.
d) O modelo em questão incorpora conceitos de modelagem entidade-relacionamento,
herança, encapsulamento e polimorfismo.

e) A simbologia do referido modelo é a mesma do modelo entidade-relacionamento,
não havendo novas representações.

Comentário. Observem que essa questão trata do assunto que acabamos de estudar.
A restrição de disjunção afirma que uma instância de entidade só pode ser especializada para apenas um dos subtipos. Já a sobreposição permite que uma instância possua as características de mais de uma classe filha. Analisando as alternativas acima podemos afirmar que o gabarito se encontra na alternativa A.
Gabarito: A

HORA DE

PRATICAR!

26. BANCA: CESPE ANO: 2010 ÓRGÃO: INMETRO PROVA: PESQUISADOR -
GOVERNANÇA DE TI

Considerando a figura acima, que ilustra um modelo conceituai, assinale a opção correta.
A As entidades pessoa física e pessoa jurídica são exemplos de generalização/especialização, conceito que envolve a ideia de herança de propriedades. Herdar propriedades significa que cada ocorrência da entidade especializada possui, além de suas propriedades (atributos, relacionamentos e generalizações ou especializações), também as propriedades de ocorrência da entidade genérica correspondente.
B A cardinalidade do relacionamento entre filial e cliente define que pode existir filial sem clientes, e ainda, que os clientes podem existir sem estar vinculados a nenhuma filial.
C Telefone é exemplo de atributo opcional.

D No modelo apresentado, entidades, relacionamentos, cardinalidade e identificadores estão corretos e consistentes.
E As entidades cliente, pessoa física e pessoa jurídica apresentam relacionamento do tipo ternário ou de grau maior, que são modelados usando-se uma entidade associada,por meio de relacionamentos binários, a cada uma das entidades que participam do relacionamento ternário.
Comentário. Primeiramente gostaria de fazer um comentário sobre o diagrama da questão. Quando apresentamos esse tipo de notação, os círculos pretos representam atributos chave das entidades e os círculos brancos representam atributos não chave.Outro ponto é a presença da restrição estrutural definindo os valores mínimos e máximos de cada entidade no relacionamento.
Feito as considerações vamos analisar as alternativas, começando pela letra A que é a nossa resposta. Vejam que o examinador que saber se você entende que, quando temos especializações dentro de um diagrama conceituai, as entidades que são subclasses herdam os atributos e relacionamentos das suas superclasses.
A letra B faz uma leitura errada do relacionamento entre cliente e filial. O correto seria dizer que uma filial atende a zero até n clientes e um cliente é atendido por uma e apenas uma filial.
Para responder a alternativa C precisamos entender o que significar o " (1 ,n) " ao lado do atributo telefone da entidade cliente. Podemos dizer que ele representa um atributo multivalorado, pois um cliente pode ter mais de um telefone e obrigatório, pois cada cliente precisa ter, no mínimo, um telefone.
Na alternativa D temos que encontrar um erro no diagrama. Precisamos verificar que o nome filial está grafado como chave primária da entidade filial, o que não faz sentido.Portanto o diagrama não está 100% correto.

Por fim, a alternativa E, as entidades listadas não representam um relacionamento ternário, é sim uma relação de generalização/especialização.
Gabarito: A.

QUESTõES CoMENTADAS CESCRANRIO.

1. CESGRANRIO - Técnico (UNIRIO)/Tecnologia da lnformação/2019

A empresa que irá administrar o estacionamento de um clube decidiu desenvolver um sistema de informação específico para isso. Apenas os sócios poderão ter acesso ao estacionamento.Assim sendo, o sócio que tiver interesse em usar o estacionamento terá de procurar o balcão da empresa para se registrar no sistema. No ato do registro, serão informados o nome do sócio e a sua matrícula no clube, além de ser gerado, automaticamente, o número do cartão de acesso ao estacionamento e a data de validade desse cartão. Cada cartão só poderá ser usado por um único sócio. Após ser cadastrado no sistema, um sócio poderá registrar os dados (placa, modelo e cor) dos veículos que ele irá estacionar. Um veículo só pode ser registrado por um único sócio. Ocadastramento dos veículos é obrigatório, pois uma câmera de vídeo irá capturar os caracteres das placas para verificar se eles estão devidamente cadastrados. Caso não o estejam, a cancela que dá acesso ao estacionamento não será aberta. Após a saída de um veículo, o sistema irá registrar o período em que ele ficou no estacionamento. Esse registro irá conter a data e a hora de entrada, a data e a hora de saída, e o valor a ser pago pela estadia. No final do mês, será gerado um boleto para cada sócio que utilizou o estacionamento durante o mês em questão. O boleto terá um número de código de barra, a data de vencimento e o valor a ser pago. Quando o boleto for pago, será inserido no sistema um registro de pagamento, que irá informar o número do banco em que o boleto foi pago e a data do pagamento.
Qual diagrama de classes conceituais representa adequadamente os conceitos envolvidos no negócio descrito acima e as relações entre esses conceitos?
Comentário:

Essa é uma questão que verificar o seu entendimento sobre cardinalidade. Perceba que:

1. Cada cartão de acesso está associado a 1 sócio e cada sócio possui apenas 1 cartão de acesso.

2. Cada sócio pode registrar zero ou mais veículos, mas cada veículo só pode pertencer a 1 sócio.

3. Cada veículo pode ter zero ou várias estadias, mas cada estadia deve ser associada a apenas 1veículo.

4. Todos os meses os sócios pagarão seus respectivos boletos, mas cada boleto só pode pertencer a1 sócio.

5. Todo boleto possui zero ou 1 pagamento. Veja que o pagamento só é registrado depois que é feito. Logo, até o pagamento o boleto não estará associado a nenhum pagamento.
A partir destas descrições, chegamos na resposta correta na alternativa D.

Gabarito: D

2. CESGRANRIO - Técnico (UNIRIO)/Tecnologia da lnformação/2019

A Figura a seguir representa um diagrama E-R.

Seja x uma instância de K, y uma instância de L e z uma instância de M. A
cardinalidade máxima exibida logo abaixo da entidade L significa que
A um par (x,z) pode estar associado a muitas instâncias de L.
B a entidade L possui muitas instâncias que participam de R.

C uma instância de K pode estar associada a muitas instâncias L.

D uma instância de M pode estar associada a, no máximo, uma instância de L.
E a relação R possui muitas instâncias de L.

Comentário. A questão demonstra um relacionamento com 3 entidades (ternário).
Neste caso,
devemos avaliar as cardinalidades através de pares de relacionamento. Assim,
neste caso, as entidades K e M (em pares) podem ser relacionar com 1 ou muitas entidades de L,conforme mencionado na Letra A.
Vamos comentar as demais alternativas:

b) ERRADA. A entidade L pode possuir 1 ou muitas instâncias participantes de R.

c) ERRADA. Em tese, estaria certo se o relacionamento não fosse ternário.
Todavia, a entidade IVI possui um relacionamento obrigatório (1,1). Assim, uma instância de K e M (em conjunto) só poderia se associar a instâncias de L.
d) ERRADA. A questão inverteu os relacionados. De M para L, é 1 ou muitas, como vimos.
Por outro lado, de L para M, é 1 e apenas l(relacionamento obrigatório).
e) ERRADA. Pode possuir 1 ou muitas.

Gabarito: A.

3. CESGRANRIO - Analista (UNIRIO)/Tecnologia da lnformação/2019

O diagrama E-R, exibido pela Figura abaixo, representa o modelo conceituai de um banco de dados.

Suponha que os elementos do conjunto T a seguir sejam instâncias da entidade de mesmo nome,presente no diagrama E-R acima.

T={tl,t2,t3,t4,t5}

Quais conjuntos completam esse banco de dados de modo que as regras definidas no modelo E-Rnão sejam violadas?

A K={kl,k2,k3,k4,k5,k6}

L={kl,k2,k3,k4,k5,k6}
M={}

S={(tl,kl),(t2,kl),(t3,kl),(t4,kl)}
B K={kl,k2,k3,k4,k5,k6}

L={kl,k2,k3,k4}

M={k4,k5,k6}
S={}

C K={kl,k2,k3,k4,k5,k6}

L={kl,k2,k3,k4}

M={k4,k5,k6}
S={(tl,kl),(t2,k2),(t4,k6)}

D K={kl,k2,k3,k4,k5,k6}
L={kl,k2}
M={k3,k4,k5,k6}

S={(t2,kl),(t3,kl),(t4,kl),(t4,k6)}
E K={kl,k2,k3,k4,k5,k6}
L={kl,k2}

M={k4,k5,k6}
S={(tl,k6),(t2,k5),(t3,k4),(t4,k3),(t5,k2)}

Comentário. Para resolver essa questão temos que olhar para as regras descritas do modelo:

1. Cardinalidade: Cada instância da entidade K deve estar associada a zero ou várias instâncias da entidade de T. Já cada instância da entidade T pode estar associa a no mínimo zero e no máximo uma instância de K.
2. Herança, que é descrita como uma generalização total e exclusiva, ou seja, todos os elementos da classe pai devem pertencer ale apenas uma das classes filhas.
De posse dessas informações, podemos observar que o conjunto das instâncias de T foi informado.Pelas regras acima, cada elemento de T pode aparecer no máximo 1 vez no relacionamento S. Por outro lado, cada elemento de K pode aparecer várias vezes. Assim, analisando a letraA, percebemos que os relacionamentos presentes em S estão corretos.
A K={kl,k2,k3,k4,k5,k6}

L={kl,k2,k3,k4,k5,k6}
M={}

S={(tl,kl),(t2,kl),(t3,kl),(t4,kl)}

Agora vamos analisar a lista de elementos presentes em K. Cada elemento de K deve estar presente em L ou M, mas nunca nos dois ao mesmo tempo. Se observarmos a letra A, todos os elementos de
K pertencem a pertencem L, e nenhuma M. Isso é perfeitamente possível. Logo, a nossa resposta já está na alternativa A. Vamos entender os problemas presentes nas demais alternativas:
b) k4 apare em L e M. Isso não pode acontecer pois a especialização é exclusiva.

c) Mais uma vez, k4 apare em L e M. Isso não pode acontecer pois a especialização é exclusiva.

d) t4 está associado a dois elementos de K (kl e k6) o que não é possível pois a cardinalidade máxima é 1.
e) k3 não aparece nem em L nem em M o que não é possível pois a especialização é total

Gabarito: A

4. CESGRANRIO - Analista (UNIRIO)/Tecnologia da lnformação/2019

Em qual diagrama E-R a relação R define uma função de E em F?

Comentário. Função é uma relação entre dois conjuntos A e B, não vazios, de forma que todo elemento de A tem um elemento correspondente em B e um elemento de A só possui um único correspondente no conjunto B. ("lei do cada" e "lei do todo"). Tendo então uma função Y =X2, podemos enxergar isso como:

Então, para encontrarmos o diagrama, temos que achar uma relação onde que todo elemento de Etem um elemento correspondente em F e um elemento de E só possui um único correspondente no conjunto F.
Então temos que definir uma cardinalidade que corresponda com essa condição da função.

* A cardinalidade de E->F tem que ser de no mínimo 1 e no máximo 1
correspondente, o que gerará: [1,1]
* E a cardinalidade de F-> E tem que ser de no mínimo 1 e no máximo 1 ou n correspondente, o que gerará: [1, (1 ou n) ]
A única opção que satisfaz as duas condições é o diagrama:

E (M)

▼

ÍMÍ F

Gabarito: D

HORA DE

PRATICAR!

5. CESGRANRIO - Analista de Sistemas Júnior (TRANSPETRO)/ Processos de Negócio/2018

A Figura a seguir exibe um modelo E-R composto por duas entidades e uma relação.

Qual diagrama de Venn contém uma relação que atende às regras de multiplicidade definidas no modelo E-R acima?
Comentário. O relacionamento R apresentado na questão tem cardinalidade 1:N.
Analisando a figura, temos duas regras que devem ser respeitadas:
* uma instância da entidade El pode se relacionar com uma ou várias instâncias da entidade E2;
e

* uma instância da entidade E2 pode se relacionar com nenhuma ou no máximo uma instância deEl.

Vamos analisar as alternativas:

a) ERRADA. Note que bl se relaciona com mais de uma instância de El, violando a regra 2.

b) ERRADA. Note que b2 se relaciona com mais de uma instância de El, violando a regra 2.

c) ERRADA. Note que a4 não se relaciona com nenhuma instância de El, violando a regra 1.

d) CORRETA. Para cada instância de El e E2, as regras 1 e 2 são respeitadas.

e) ERRADA. Note que bl se relaciona com mais de uma instância de El, violando a regra 2.

Gabarito: D

6. CESGRANRIO - Escriturário (BB)/"Sem Área"/2018

Um banco de dados possui um modelo conceituai cuja descrição é feita pelo diagrama E-R a seguir.

A-{ai,a2,a3,a4,a5,a6}
Al={a2,a₃,a₄}

A2={ai,a₅,a₆}

C={ci,c₂}
D={di,d2,d3,d₄}

Oe elementos desses conjuntos representam instâncias das entidades presentes no diagrama
E-R do banco de dados em questão.
As relações que completam o estado desse banco de dados, sem que nenhuma regra de cardinalidade ou generalização seja violada, são
A Rl={(ai,ci),(a₂,ci)}
R2={}

B Rl={}

R2={}

C Rl={(ai,Ci),(ai,C2)}
R2={(a2,di),(a5,d2),(a6,d4)}

D Rl={(ci,a5),(ci,a2),(c2,a5),(c2,a2)}

R2={(a5,di),(a6,d2),(a5,d3),(a5,d4)}

E Rl={(a5,ci),(a2,Ci),(a5,C2),(a2,C2)}

R2={(a5,di),(a6,d2),(a5,d3),(a5,d4),(a6,d4)}

Comentário.

Nesta questão temos que olhara para a cardinalidade. O primeiro ponto é que o relacionamento deC com A é obrigatório, ou seja, RI não pode ser um conjunto vazio e deve apresentar pelo menos 1
relacionamento para as instâncias cl e c2. Isso anula as alternativas A e B. A letra
A não apresenta relacionamento par a c2, enquanto a letra B não apresenta nenhum relacionamento.
O segundo ponto a ser observado é que apenas as instâncias de A2 podem ser relacionar com a entidade D. Ou seja, não pode haver relacionamento a2, a3 e a4 com os elementos deD. Isso tornar incorreta a alternativa C, que tenta relacionar a2 a dl.
Por fim, não podemos ter elementos de D associados a mais de um elemento de A2. Perceba que na letra E, d4 está associado a a5 e a6, o que não é possível.
Assim, chegamos a nossa resposta na alternativa D. Verifique as regras acima nestes relacionamentos. Perceba que todas as regras são respeitadas.
Gabarito: D.

7. CESGRANRIO - Profissional (LIQUIGÁS)/Analista de Sistemas/Júnior TI/2018/Edital 02

Os conjuntos a seguir representam um banco de dados relacional.

P={pl,p2,p3}

Q={ql,q2,q3 }

R={rl,r2,r3,r4 }
Tl={(pl,ql),(pl,q2),(pl,q3)}
T2={}
T3={(ql,rl),(q2,r3),(q3,r4)}

Qual modelo E-R define regras de cardinalidade compatíveis com esse banco de dados?

Comentário. Vamos analisar cada alternativa e identificar inconsistências no modelo E-R
que não devem existir neste banco de dados.
a) CORRETO. O que podemos inferir de acordo com o que nos foi dado na questão: O relacionamento
TI existe entre as entidades P e Q. Temos a instância pl se relacionando com três instâncias de Q

(ql, q2, q3). Podemos concluir, com certeza, que a entidade P se relaciona no máximo com Ninstâncias de Q.e no mínimo com 0 (zero), porque existem instâncias de P que não estão relacionadas com Q. A entidade Q pode se relacionar no mínimo com uma instância de P,cardinalidade mínima
1.

O relacionamento T2 não é obrigatório, então possui cardinalidade mínima 0.

E, no relacionamento T3, a entidade R pode se relacionar ou não com a entidade Q,
ou seja,
cardinalidade mínima 0, porque a instância r_2 não se relaciona com a entidade Q. A
entidade Q
possui relacionamento obrigatório com R, cardinalidade mínima 1.

b) ERRADO. Podemos eliminar esta alternativa porque não existe o relacionamento T3
entre P e R.
A entidade P pode se relacionar ou não com a entidade Q, temos um relacionamento opcional, então a cardinalidade mínima é 0.
c) ERRADO. Também eliminamos esta alternativa porque não existe o relacionamento T3
entre P e

R. A cardinalidade mínima de Q. em relação a P é 1, porque todas as instâncias de
Q estão relacionadas a alguma instância de P. E, a cardinalidade mínima de R em relação aQéO, porque r_2
não está relacionada com a entidade Q.

d) ERRADO. No relacionamento Tl, existem instâncias de P que não estão relacionadas com instâncias de Q, por isso a cardinalidade mínima é 0.
e) ERRADO. No relacionamento Tl, Q tem que estar relacionada no mínimo com uma instância deP (cardinalidade mínima 1), porque todos as instâncias de Q estão relacionadas a alguma instância de P. E, no relacionamento T3, como r_2 não está relacionada com alguma instância deQ, a cardinalidade mínima de R em relação a QéO.
Gabarito: A.

8. CESGRANRIO - Profissional (LIQUIGÁS)/Arquiteto de Soluções/Júnior TI/2018/Edital 02

O modelo de Entidades e Relacionamentos (ER) é bastante utilizado na modelagem conceituai de bancos de dados. Além de utilizar entidades e seus relacionamentos para descrição dos dados, o modelo ER inclui também alguns atributos que descrevem as características de cada entidade.
Já um relacionamento também pode ter atributos

A se as cardinalidades máximas forem lxN, independentemente das cardinalidades mínimas.
B se as cardinalidades máximas forem NxN, independentemente das cardinalidades mínimas.

C se as cardinalidades mínimas do relacionamento forem maiores que zero,
independentemente das cardinalidades máximas.
D somente se estiver participando de uma entidade associativa.
E independentemente das cardinalidades do relacionamento.

Comentário.

Sabemos que a existência de atributos no relacionamento independe da cardinalidade.
Logo, temos a nossa resposta na alternativa E.
Gabarito: E.

HORA DE

PRATICAR!

9. BANCA: CESGRANRIO ANO: 2014 ORGAO: PETROBRAS PROVA: TÉCNICO - TÉCNICO DE
INFORMÁTICA

O diagrama a seguir apresenta um modelo de entidades e relacionamentos segundo a notação daEngenharia de Informação.

Coleção Item Coleção
A notação equivalente em IDEF1X é

Comentário. Veja que o losango representa um relacionamento opcional e a bola preta representa zero, um ou vários. A linha tracejada representa um relacionamento não identificador.Isso acontece quando temos duas entidades independentes ou representadas por retângulos.
Curiosidade: A notação IDEF1X (Integrated DEFinition for Information Modelling) foi desenvolvida no final da década de 70 para a força aérea norte-americana. Esta metodologia faz parte de um conjunto de técnicas (IDEF) para a modelagem completa de um sistema, incluindo modelagem de processos, dados, simulação e descrição de procedimentos. A metodologia IDEF1X é um padrão do birô federal de processamento de informações norte-americano (padrão FIPS 184) e de uso público e livre.
Gabarito: A

HORA DE

PRATICAR!

10.Ano: 2016 Banca: CESGRANRIO Órgão: IBGE Prova: Supervisor de Pesquisas - Tecnologia de
Informação e Comunicação

A KWX é uma empresa do varejo que atua exclusivamente na Web. Ela está desenvolvendo um sistema de informação para registrar os pedidos de seus clientes e controlar todo o processo de entrega de mercadorias. Um pedido é entregue por uma das transportadoras conveniadas com a empresa. Quando o novo sistema estiver em funcionamento, todas elas serão devidamente cadastradas, tendo em vista melhorar a gestão de entregas pelo setor responsável. Ocusto de transporte varia de transportadora para transportadora, além de levar em conta o endereço de entrega de um pedido. Visando a reduzir o tempo de entrega, a diretoria de vendas determinou que a definição da transportadora tem de ser feita até 48h após um pedido ter sido inserido no sistema.
No ato do recebimento de um pedido, o cliente irá conferir se todos os produtos comprados estão corretos e se não houve avarias durante o transporte. Caso esteja tudo em ordem, o cliente irá assinar o recibo de entrega, pondo a data em que ela foi feita. Essa informação será posteriormente inserida no sistema por um funcionário do setor de entregas. Caso o cliente encontre algum problema, ele poderá recusar o recebimento dos produtos, informando o motivo pelo qual a entrega foi recusada. O motivo da devolução deve ser assinalado no próprio documento de entrega, que contém uma lista de motivos extraída do sistema. Um motivo possui código e descrição.
O sistema deve, também, atender a alguns requisitos adicionais. São eles:

* o cliente deve informar o endereço de entrega no momento em que inserir um pedido;

* um pedido possui um número e a data em que foi realizado;

* uma transportadora precisa ter registrados o número do CNPJ, o nome e o endereço.

Qual diagrama E-R descreve adequadamente os elementos envolvidos no negócio da empresa KWX?

b)

e)

Comentário: A chave para responder à questão está na frase: "Um pedido é entregue por uma das transportadoras conveniadas com a empresa." Veja que se cada pedido possui apenas uma transportadora, logo precisamos compor uma agregação entre as entidades pedido e transportadora. Essa entidade associativa "entregue" vai agora poder se relacionar com a entidadeMotivo de forma parcial, caso exista algum motivo para a não aceitação da entrega.

Veja que agora precisamos alocar os atributos nas suas respectivas entidades ou relacionamentos.Assim temos:

Pedido (número, datalnclusão, endereçoEntrega)
Transportadora (CNPJ, enderço, nome)

Entrega (dataEntrega, custoTransporte)
Motivo (código, descrição)

A última etapa é verificar a cardinalidade dos relacionamentos. Primeiro, cada pedido ao ser feito ainda não possui uma transportadora associada, contudo para ser entregue ele tem que ter uma transportadora e apenas uma, assim temos para a cardinalidade mínima e máxima os valores (0,1).Já uma transportadora pode não ter transportado nenhum pedido, ou fazer várias entregas. Neste caso, temos uma cardinalidade (0,n). O outro relacionamento entre Entrega eMotivo pode ser descrito da seguinte forma: se a entrega for aceita não temos motivo, entretanto se ela for negada,temos 1 e apenas 1 motivo (0,1). Por outro lado, um motivo pode estar associado a várias entregas diferentes. Por exemplo, produto quebrado pode ser o motivo de devolução de várias entregas distintas (0,n).
Após compilar todas essas informações acima, podemos marcar nossa resposta na alternativa C.

Gabarito: C

11. Ano: 2016 Banca: CESGRANRIO Órgão: UNIRIO Prova: Técnico em Tecnologia da Informação

Considere as Tabelas a seguir para responder a questão.

Essas Tabelas fazem parte do esquema de um banco de dados usado por uma associação de criadores de cães para organizar informações sobre os torneios que ela promove.
CREATE TABLE CAO (

COD NUMRERC5) NOT NULL,

NOME VARCRAR2(30) NOT NULL,

RACA VARCRAR2(50) NOT NULL,

NOME- PAI VARCRAR2(50) r

NOME 'PROPR VARCRAR2(50) NOT NULL,
CONSTRAINT CAO PK PRIMARY KEY (COD)

)

CREATE TABLE COMPETICAO (

COD NUMBER(5) NOT NULL,

DESCR VARCRAR2(50) NOT NULL,
CONSTRAINT COMPETICAO_PK PRIMARY KEY (COD)

)

CREATE TABLE ARBITRO (

COD NUMBER(5) NOT NULL,

NOME VARCHAR2(50) NOT NULL,
CONSTRAINT ARBITRO_PK PRIMARY KEY (COD)

)

CREATE TABLE
COD_CAO
COD_COMP
COLOCACAO

PARTICIPACAO (

NUMBER(5)
NUMBERfS)
NÜMBER(4)

NOT NULLf
NOT NULL,
NOT NULL,

CONSTRAINT PARTICIPACAO PK PRIMARY KEY
(COD-CAO,COD_COMP),

CONSTRAINT PARTIClPACAO_FK1 FOREIGN KEY (COD_CAO)

REFERENCES CAO (COD),

CONSTRAINT PARTIClPACAO_FK2 FOREIGN KEY (COD_COMP)
REFERENCES COMPETICAO (COD)

CREATE TABLE AVALIACAO

COD_CAO
COD_COMP
COD_ARBTR
NOTA ARBTR

NUMBERÍ5)
NUMBERÍ5)
NUMBER(5)
NUMBER(3f1)

NOT NULLj
NOT NULL,
NOT NULL,
NOT NULL,

CONSTRAINT AVALIACAO PK PRIMARY KEY

(COD CAO,COD COMPjCOD ARBTR),

CONSTRAINT AVALIACAO_FK1
REFERENCES CAO (COD),
CONSTRAINT AVALIACAO_FK2
REFERENCES COMPETICAO
CONSTRAINT AVALIACAO FK3

REFERENCES ARBITRO (COD)

FOREIGN KEY (COD- CAO)

FOREIGN KEY (COD- COMP)
(COD) ,

FOREIGN KEY (COD ARBTR)

Observações:

* A Tabela CAO contém os dados dos cães inscritos na referida associação. A coluna
NOME_PAI
indica o nome do pai de um cão, a coluna RACA indica a raça do mesmo, e a coluna NOME_PROPR
indica o nome do seu proprietário. As demais colunas são autoexplicativas.

* A Tabela COMPETICAO contém informações sobre as competições patrocinadas pela associação.Suas colunas são autoexplicativas.

* A Tabela PARTICIPACAO informa as competições das quais participaram os cães registrados na associação. Cada linha dessa tabela indica a colocação obtida por um cão em uma determinada competição. Suas colunas são autoexplicativas.
* A Tabela ARBITRO contém os dados dos árbitros que julgam os cães que participam de competições. Suas colunas são autoexplicativas.
* Cada linha da Tabela AVALIACAO representa a nota atribuída a um cão, por um determinado árbitro em uma determinada competição. Suas colunas são autoexplicativas.
Qual diagrama E-R contém um modelo conceituai compatível com as tabelas do banco de dados da associação de criadores de cães?
a)

b)

e)

Comentário: Essa é mais uma questão que nos remete a existência de uma entidade associativa,desta vez um cão pode participar de várias competições e cada competição pode ter vários cães.Essa participação pode ser avaliada por vários árbitros diferentes. Em uma competição os árbitros devem avaliar diversos cães. Veja que a colocação é um atributo associado a participação, já a nota,que deve ser atribuída por um árbitro torna-se um atributo do relacionamento avaliação.

Outra informação relevante é que o nome do pai é o único atributo do código SQL que pode ser nulo. Na representação conceituai o examinador optou por representar tal falto colando um "(0,1)"ao lado do atributo.

Analisando o texto e as alternativas, podemos encontrar nossa resposta na alternativa
C. Veja que as demais alternativa, ou o diagrama não expressa semanticamente o contexto descrito no enunciado, ou possui a cardinalidade denotada incorretamente, como é o caso da alternativa E.
Gabarito: C

HORA DE

PRATICAR!

12. Ano: 2016 Banca: CESGRANRIO Órgão: UNIRIO Prova: Técnico em Tecnologia da Informação

Uma empresa que atua no ramo de entrega de encomendas precisa de um sistema de informação para controlar sua principal atividade. Durante o levantamento dos requisitos desse sistema, as seguintes informações sobre o pagamento de entregas foram fornecidas por um funcionário da empresa:
*Uma entrega é identificada internamente por um código. Além disso, é necessário registrar o peso e as dimensões do objeto a ser entregue, o endereço de entrega e o custo da operação de entrega;
* Uma entrega pode ser paga através de cartão de crédito, cartão de débito ou boleto bancário.Visando a atender às demandas de seus clientes, uma entrega pode ser paga usando-se qualquer combinação desses três meios de pagamento;
* Em relação a um pagamento com cartão de crédito, o sistema deve registrar a data de pagamento,o valor pago, o número do cartão, sua data de validade e a instituição que o emitiu;

* Em relação a um pagamento com cartão de débito, o sistema deve registrar a data de pagamento,o valor pago, o número do banco e os números da agência e da conta corrente às quais o cartão está vinculado;
* Em relação a um pagamento com boleto bancário, o sistema deve registrar a data de pagamento,o valor pago e o número do código de barras do boleto;

* Cada pagamento registrado se refere a uma única entrega

* Não há entrega registrada no sistema que não tenha, pelo menos, um pagamento associado a ela.
Qual diagrama E-R representa corretamente os elementos e as regras presentes na descrição dos requisitos listados acima, sem que haja perda de informações ou redundância de dados,além de observar as boas práticas de modelagem conceituai de dados?
c)

e)

Comentário: Após ler o enunciado da questão, podemos observar que o Pagamento possui 3subtipos: Boleto, Cartão de Crédito e Cartão de Débito. Vejam que essas 4
entidades serão organizadas em uma estrutura de generalização/especialização. Nela, os atributos data e valor estão associados à entidade pai, e os outros atributos, específicos de cada entidade filha,devem ser associados de acordo com o texto do enunciado.
Em seguida, podemos observar que a existência de um pagamento deve estar relacionada como uma Entrega. Desta forma, devemos criar a entidade entrega e um relacionamento total ou obrigatório em ambos os lados do relacionamento. Uma entrega pode ser associada a vários pagamentos, e um pagamento pode ser associado a uma e somente uma entrega.
Dito isto, podemos marcar nossa resposta na alternativa C.

Gabarito: C

HORA DE

PRATICAR!

13. Ano: 2014 Banca: CESGRANRIO Órgão: Petrobras Prova: Técnico(a) de Exploração de Petróleo
Júnior - Informática

ALUNO (cpf : string , nome : string , endereço : string, telefone : string)
MATRICULA (cpf : string , cod-cad : string)

CADEIRA (cod-cad : string, nome : string , créditos : number)

A representação do esquema relacional acima, segundo um diagrama de entidades e relacionamentos, deve representar ALUNO, MATRICULA e CADEIRA, respectivamente, como a) entidade, relacionamento nxm e entidade b) entidade, relacionamento lxn e entidade c) entidade, entidade e atributo d) entidade, entidade e relacionamento nxm e) entidade, atributo e entidade
Comentário: Vejam que essa questão pede para fazer uma engenharia reversa, partir do modelo relacional e chegar ao modelo entidade relacionamento. De cara, podemos observar que as relaçõesALUNO e CADEIRA são entidades do modelo. A próxima etapa é perceber que a relação MATRICULA
possui as chaves das duas relações. Neste caso, temos um relacionamento n:m. Logo, nossa resposta está na alternativa A.
Gabarito: A

CAIU

na prova!

14. Ano: 2014 Banca: CESGRANRIO Órgão: CEFET-RJ Prova: Analista de Tecnologia da Informação

Uma das características do Modelo de Entidade e Relacionamentos é que a) cada domínio de possíveis valores possui um atributo.
b) dois conjuntos de entidades são sempre disjuntos.

c) toda chave candidata é uma chave primária.

d) todos os atributos em determinado conjunto de atributos têm o mesmo conjunto de entidades.

e) um conjunto de relacionamentos pode ser considerado um conjunto de n-tuplas.

Comentário: Vamos analisar cada uma das alternativas acima. Primeiramente, o domínio restringe os valores possíveis de um atributo. A alternativa a) fala algo que se opõe a esse conceito, logo está errada.
Dois conjuntos de entidades, ou de valores armazenados em uma entidade específica,
podem ser iguais, disjuntos ou sobrepostos. Logo, a alternativa B, também está incorreta.
A chave primária é um conceito que vai aparecer de verdade no modelo relacional.
Quando falamos do modelo entidade relacionamento estamos falando de chave ou atributo identificador. Ainda assim, uma relação pode ter várias chaves candidatas e uma delas é escolhida para ser chave primária da relação. Logo, a afirmação da alternativa c) não é válida.
Na alternativa d) temos mais uma troca de conceitos, na realidade todas as entidades em um determinado conjunto de entidades têm o mesmo conjunto de atributos.
Por fim, nossa reposta, um conjunto de relacionamentos pode ser considerado um conjunto de n-tuplas. Ou, em outras palavras, o conjunto de relacionamento é formado pelas diversas instâncias deste relacionamento. Sendo assim, nossa resposta está na alternativa E.
Gabarito: E

HORA DE

PRATICAR!

15. Ano: 2014 Banca: CESGRANRIO Órgão: Banco da Amazônia Prova: Técnico Científico - Banco de
Dados

Para responder à questão, tenha como referência o diagrama de entidades e relacionamentos,apresentado abaixo, que representa parte do modelo de dados de uma instituição financeira.

Movimento

Conta

<-------------------------------- >

seq_movimento data_hora_movimento credito_debito valor numero-documento ti po_docu mento dep_origem historico
<saldo >

Contato_Cliente id_telefone telefone tipO—telefone
A

Cliente id_cliente
-|- nome_diente i datajnicio data fim
Endereco_Cliente f \
id_endereco inicio_validade_endereco fim_validade_endereco logradouro numero complemento cep bairro cidade
\/estado

Que representação gráfica do modelo ER proposta pela notação IDEF1X representa relacionamento existente entre Conta e Cliente?
Comentário: Temos que observar que a questão trata especificamente da ligação entre as duas entidades ou do relacionamento entre elas. Observe que os cantos arredondados da entidade Conta,e os canto retos da entidade Cliente são reflexos diretos do diagrama original. Fato é que conta é uma entidade dependente da entidade independente cliente.
Vejam agora que temos um pé de galinha em ambos os lados do diagrama original. Logo,
estamos falando de um relacionamento n:n, que no modelo IDEF1X é designado por uma bola fechada. Veja na figura abaixo:
1 zero, one or more

1p one or more

1n-m exactlv n from n to m lzzero or one reference to note (n) where
(n) cardmaliry is speciíied

Sendo assim, podemos marcar nossa resposta na alternativa B.

Gabarito: B

16. Ano: 2014 Banca: CESGRANRIO Órgão: Banco da Amazônia Prova: Técnico Científico - Banco de
Dados

Para responder à questão, tenha como referência o diagrama de entidades e relacionamentos,apresentado abaixo, que representa parte do modelo de dados de uma instituição financeira.

Movimento

Conta seq_movimento data_hora_movimento creditO—debito valor numero-documento tipo—documento dep_origem historico k saldo >
Endereco Cliente

( x id_endereco inicio_validade_endereco fim_validade_endereco logradouro numero complemento cep bairro cidade estado
Sendo feita a transformação desse modelo de dados em um modelo diretamente equivalente a um modelo relacional, de maneira a manter o número mínimo de Tabelas necessárias, e sendo feita a migração das chaves para constituir as chaves externas, sem o uso de chaves substitutas, quantos campos serão adicionados ao modelo?
a) 7

b) 8

c) 9

d) 11

e) 13

Comentário: Devemos lembrar que no caso da entidade Conta, esta representa uma entidade fraca,devido sua forma arredondada, neste caso, ela irá herdar as chaves primárias das outras tabelas e estas chaves irão compor sua chave primária, sendo assim a entidade Conta terá como chave primária os atributos:
(id_conta, id_agencia, codigo_tipo_conta) 3 atributos sendo 2 atributos FK

A entidade Movimento terá a chave estrangeira através da composição da chave primária da entidade Conta, vejamos:
Movimento (id_movimento, id_conta, id_agencia, codigo_tipo_conta)

4 atributos chave sendo 3 chaves FK

Agora vamos analisar as demais entidades:

Endereco_Cliente (id cliente) -1 atributo FK
Contato_Cliente (id cliente) -1 atributo FK

Falta apenas avaliarmos o relacionamento entre Conta e Cliente.
Conta_Cliente (id_conta, id_agencia, codigo_tipo_conta, id cliente)

4 atributos FK

Logo, as chaves externas são:

2 Conta + 3 Movimento + 1 Endereco_Cliente + 4 Conta_Cliente +

1 Contato_Cliente = 11 chaves externas.

Desta forma, nossa resposta encontra-se na alternativa D.

Gabarito: D

17. Ano: 2014 Banca: CESGRANRIO Órgão: Banco da Amazônia Prova: Técnico Científico - Análise de Sistemas
A federação de futebol de um estado brasileiro resolveu criar uma nova forma de vender ingressos para os jogos do seu campeonato estadual. Lotes de cartões com chip, semelhantes a cartões de crédito, serão enviados para lojas credenciadas. O torcedor que queira comprar ingressos para os jogos terá de se cadastrar, antecipadamente, na federação e dirigir- -se a uma das lojas para adquirir um desses cartões e carregá-lo com ingressos para os jogos a que desejar comparecer.A entrada nos estádios será feita mediante a apresentação do cartão contendo os ingressos que o torcedor comprou. Cada torcedor poderá possuir um único cartão. O controle será feito pelo número do CPFdo torcedor. Um cartão terá um número, que o identificará. Esse número será gravado no chip pelo fabricante dos cartões, e registrado no sistema da federação, antes que o cartão seja enviado para uma loja credenciada.
Qual diagrama E-R descreve, adequadamente, as regras de negócio apresentadas acima, além de observar os preceitos de um bom modelo conceituai de dados?
c)

e)

Comentário: A primeira informação importante, no meu ponto de vista, para resolver a questão é que o torcedor carrega o cartão com ingressos para os jogos. Outro ponto importante é que esse cartão pode estar carregado com 0 ou vários jogos, representados pelo ingresso do jogo. Cada ingresso, logicamente, dá direito a entrar em 1 e apenas 1 jogo e só poderá estar associado a um cartão.
De posse desse cartão, o torcedor consegue entrar em diversos jogos, mas veja que o relacionamento entre cartão e torcedor é 1:1. Lembre-se que cada torcedor tem 1 cartão e cada cartão só pode pertencer a um torcedor, o número do CPF do torcedor nos ajuda nesta unicidade.Lembrando ainda que, um torcedor pode ou não ter um cartão, e um cartão pode estar associado ou não a um torcedor. Assim, temos uma restrição de participação parcial,que nos leva uma cardinalidade mínima de 0 nos dois lados do relacionamento.
Depois desta descrição, podemos marcar nossa resposta na alternativa D. Agora vamos verifica o que está errado nas demais alternativa.
Na alternativa a), não existe o relacionamento carrega e a cardinalidade torcedor cartão é (0,1), pois"Cada torcedor poderá possuir um único cartão"

Já na letra b), o erro, mais uma vez, está na cardinalidade cartão-torcedor(l,l) e também na cardinalidade ingresso-cartão(0,n). Verifique a cardinalidade correta na alternativa D.
Seguindo para a letra c), a cardinalidade n sinaliza a criação de um atributo de chave estrangeira(referencial) no modelo relacional. Não é preciso representá-lo na Entidade Ingresso pelo atributo numcartão.
Por fim, na alternativa e) não deveria existir o relacionamento carrega, pois o mesmo não é descrito no enunciado.
Gabarito: D

18. Ano: 2014 Banca: CESGRANRIO Órgão: FINEP Prova: Analista - Desenvolvimento de Sistemas

Um país irá leiloar blocos de exploração de petróleo e precisa de um sistema de informação para controlar o registro dos consórcios que participarão dos leilões, os lances que serão realizados e o vencedor de cada leilão. Todos os consórcios que irão disputar os leilões terão que ser previamente cadastrados no sistema. Um consórcio é formado por uma ou mais empresas.
O objeto de cada leilão é um bloco de exploração. Os consórcios poderão registrar vários lances para cada bloco disputado. Os lances, entretanto, terão de ser maiores ou iguais a um valor mínimo, que será fixado, para cada bloco, antes de cada leilão.
Além de atender aos requisitos acima, o sistema de informação em questão deve responder às seguintes questões:
* Qual é o nome do consórcio vencedor?

* Quais são as empresas que integram um determinado consórcio?

* Qual é o país de origem de uma determinada empresa?

* Qual é o nome de uma determinada área de exploração? Onde ela está localizada?

* Qual é o código de um determinado bloco de exploração? Onde ele está localizado? A
que área de exploração ele pertence?
Qual diagrama E-R atende a todos os requisitos descritos acima?

a)

b)

c)

Comentário: Observem que o ponto crucial para responder a essa questão é o fato de uma empresa está localizada em apenas um país. Logo, não existe a necessidade de construirmos o relacionamento localizada. Com isso eliminamos as alternativas a), b) e e).Agora, entre as alternativas c) e d), verificamos que a letra d) não possuí a entidade consórcio.Ficamos, portanto,
com a nossa resposta na alternativa c) que consegue responder plenamente as perguntas listas e reflete a descrição do enunciado.
Gabarito: C

LISTA DE QUESTõES - CEBRASPE

1. CEBRASPE (CESPE) - Auditor de Finanças e Controle de Arrecadação da Fazenda
Estadual (SEFAZ AL)/2020

Com relação a banco de dados, julgue o item seguinte.

Com base no diagrama a seguir, é correto afirmar que um item na entidade Ambiente pode não relacionar-se com nenhum item na entidade Setor ou pode relacionar-se com vários itens nesta entidade, enquanto um item na entidade Setor pode relacionar-se somente com um item na entidade Ambiente.

1. CEBRASPE (CESPE) - Ana Min (MPE CE)/MPE CE/Ciências da Computação/2020

Considerando o diagrama entidade- relacionamento precedente e os múltiplos aspectos que a modelagem de dados oferece ao analista para examinar os dados no contexto de uma aplicação de software, julgue o item subsecutivo.
No diagrama apresentado, a modalidade obrigatória que conecta transportador e transporta indica que, para todo alimento fabricado, é necessária uma ação de transporte.
2. CEBRASPE (CESPE) - Ana Min (MPE CE)/MPE CE/Ciências da Computação/2020

Considerando o diagrama entidade- relacionamento precedente e os múltiplos aspectos que a modelagem de dados oferece ao analista para examinar os dados no contexto de uma aplicação de software, julgue o item subsecutivo.
A cardinalidade e a modalidade apresentada para a entidade fabricante mostram que obrigatoriamente um fabricante inicializa a ação de solicitação de distribuição,contratação de transporte e produção de alimento, o que caracteriza uma relação 1 x n.
3. CEBRASPE (CESPE) -Ass Min (MPC TCE-PA)/TCE-PA/lnformática/2019

As seguintes informações foram extraídas de um diagrama de entidades-
relacionamento no contexto de um banco de dados relacional.

De acordo com as informações do texto 9A1-I, assinale a opção correta, com relação à leitura das regras do negócio representadas no modelo apresentado.
a) Ao realizar uma reserva, o cliente pode escolher um ou vários trechos de voo.
Existem várias opções de aeronaves para o trecho reservado.

b) Ao realizar uma reserva, o cliente pode escolher um ou vários trechos de voo, mas existe apenas uma aeronave alocada para o trecho reservado.
c) Ao realizar uma reserva, o cliente pode escolher apenas um trecho de voo, mas existem várias opções de aeronaves para o trecho reservado.
d) Um trecho de voo está relacionado a apenas uma reserva.

e) Ao realizar uma reserva, o cliente recebe um único número de assento, válido para todos os trechos que forem reservados.
4. CEBRASPE (CESPE) - Tec (EBSERH)/EBSERH/lnformática/2018

Tendo como referência o modelo lógico precedente, julgue o item a seguir.

A partir do modelo apresentado, infere-se que um hospital pode estar vinculado a várias universidades, pois a tabela Hospital apresenta cardinalidade (0, n).
5. CEBRASPE (CESPE) - APF/PF/2018

Considerando o modelo entidade-relacionamento (ER) precedente, julgue o seguinte item, relativo a banco de dados.
Conforme o modelo ER em questão, um tipo de produto pode estar associado a somente 1 produto e cada produto possui um preço e uma descrição.
6. CEBRASPE (CESPE) - Ana Min (MPE PI)/MPE Pl/Tecnologia da lnformação/2018

Tendo em vista que, ao se desenvolver um sistema de vendas e compras para um cliente, devem-se descrever os produtos, as entradas, as saídas, o controle de estoque e o lucro das vendas, julgue o item subsequente, relativo à modelagem de dados para a aplicação descrita.
No sistema implementado, o cliente terá de cadastrar cada produto nos módulos de vendas e compras, pois a redundância será controlada pelo usuário, e não pela modelagem do banco de dados.
7. CEBRASPE (CESPE) - AFA (SEFAZ RS)/SEFAZ RS/2018

No modelo entidade-relacionamento, as propriedades particulares que descrevem uma entidade são denominadas a) valores.
b) atributos.

c) chaves primárias.

d) relacionamentos.

e) instâncias.

8. CEBRASPE (CESPE) - Tec (FUB)/FUB/Tecnologia da lnformação/2018

Julgue o item seguinte, a respeito dos conceitos de modelagem de dados e níveis de abstração.
No modelo de entidade-relacionamento, uma entidade se caracteriza por um objeto do mundo real que possui um conjunto de propriedades; os valores de um subconjunto dessas propriedades podem identificar de maneira única a entidade.
9. CEBRASPE (CESPE) - Tec (FUB)/FUB/Tecnologia da lnformação/2018

Julgue o item seguinte, a respeito dos conceitos de modelagem de dados e níveis de abstração.
Na cardinalidade de mapeamento entre o conjunto de entidades X e Y de uma associação um-para-um, uma entidade em X é associada, no máximo, a uma entidade em Y, e uma entidade em Y é associada, no máximo, a uma entidade em X.
10. Ano: 2018 Banca: CESPE Órgão: STJ Cargo: Técnico Judiciário - Suporte
Técnico

Acerca de banco de dados, julgue os itens que se seguem.

75 Em um diagrama MER, a entidade representa uma coisa concreta do mundo real,
enquanto as coisas abstratas são representadas pelo relacionamento entre as entidades.
11. Ano: 2018 Banca: CESPE Órgão: STJ Cargo: Técnico
Judiciário -
Desenvolvimento de Sistemas Questão: 64 e 65

Julgue os itens a seguir, referentes à modelagem de dados.

64 Generalização é o processo de definição de um tipo de entidade a partir de duas ou mais entidades que possuem atributos em comum — por exemplo, as entidades carro e ônibus podem ser generalizadas na superclasse veículo.
12. Ano: 2018 Banca: CESPE Órgão: TCM-BA Cargo: Auditor de Contas Questão:

A respeito de entidades, relacionamentos e tipos de chave, assinale a opção correta.
A Uma entidade fraca não possui seus próprios atributos chave.

B Toda relação deve possuir somente uma chave primária de atributo único.

C Um identificador ou chave é usado para determinar exclusivamente uma instância de um relacionamento entre entidades.
D A abordagem entidade-relacionamento permite somente relacionamentos binários e dos tipos 1:1 e 1:n.
E Uma entidade forte existe no banco de dados e possui atributos que a identificam sem que ela precise estar associada a outra entidade identificadora.
13. Ano: 2018 Banca: CESPE Órgão: STM Cargo: Programação de Sistemas
Questão: 61 a 65

Acerca dos conceitos de normalização de dados e dos modelos de dados, julgue os itens subsequentes.
63 O modelo conceituai, que reflete uma estrutura simplificada do banco de dados, é responsável por registrar como os dados estão armazenados no sistema de gerenciamento de banco de dados (SGBD).
64 Comparativamente aos usados pelos usuários leigos, os modelos de dados utilizados por programadores são considerados menos abstratos, pois contêm mais detalhes de como as informações estão organizadas internamente no banco de dados.
14. BANCA: CESPE ANO: 2014 ÓRGÃO: ANATEL PROVA: ANALISTA
ADMINISTRATIVO - DESENVOLVIMENTO DE SISTEMAS DE INFORMAÇÃO

Com base nos modelos de banco de dados, julgue os itens subsequentes.

[89] São empregados no projeto de aplicações de um banco de dados o modelo entidade-relacionamento (MER), que é um modelo representacional, e suas variações.
[90] O modelo de dados físico é considerado de baixo nível, o que significa que somente os sistemas gerenciadores de banco de dados conseguem interpretá-lo.
15. Ano: 2015 Banca: CESPE Órgão: TRE-PI Cargo: Operação de computadores -
Questão 40

De acordo com a notação para diagramas entidade-relacionamento, assinale a opção que descreve a representação acima disposta.
A entidade, atributo, atributo composto e atributo derivado

B relacionamento, atributo, atributo fraco e atributo multivalorado

C entidade fraca, atributo-chave, atributo multivalorado e atributo derivado
D entidade, atributo-chave, atributo multivalorado e atributo derivado

E entidade forte, atributo, atributo composto e atributo fraco

16. Ano: 2015 Banca: CESPE Órgão: TRE-PI Cargo: Operação de computadores -
Questão 41

Acerca do modelo entidade-relacionamento estendido, assinale a opção correta.

A Uma restrição de disjunção pode ser aplicada a uma especialização, na qual deve ser especificado que as subclasses da especialização devem ser mutuamente exclusivas.
B A generalização é o resultado da separação de um tipo-entidade de nível mais alto

— superclasse — e forma vários tipos-entidades de nível mais baixo — subclasse.

C Uma entidade, que é membro de uma subclasse, nem sempre herda todos os atributos da entidade como um membro da superclasse.
D O modelo em questão incorpora conceitos de modelagem entidade-relacionamento,
herança, encapsulamento e polimorfismo.

E A simbologia do referido modelo é a mesma do modelo entidade-relacionamento,
não havendo novas representações.

17. Ano: 2015 Banca: CESPE Órgão: TRE-PI - Questão 57

Considere que existe uma entidade PESSOA com um relacionamento denominado
CASAMENTO que pode associar diversas ocorrências na mesma entidade PESSOA.
De acordo com as propriedades do diagrama entidade-relacionamento, o conceito desse relacionamento (CASAMENTO) pode ser definido como
A generalização.

B relacionamento binário.
C autorrelacionamento.

D entidade associativa.
E especialização.

18. BANCA: CESPE ANO: 2015 ÓRGÃO: MPOG PROVA: ANALISTA - ANALISTA EM
TECNOLOGIA DA INFORMAÇÃO

A respeito de modelo entidade-relacionamento e normalização, julgue os itens subsequentes.
[113] Em relações normalizadas, na primeira forma normal, toda tupla em toda relação contém apenas um único valor, do tipo apropriado, em cada posição de atributo.
[114] Sabendo que, nos relacionamentos ternários, a cardinalidade refere-se a pares de entidades, em um relacionamento ternário R entre três entidades A, B e C, a cardinalidade máxima de A e B dentro de R indica quantas ocorrências de C podem estar associadas a um par de ocorrências de A e B.
19. BANCA: CESPE ANO: 2015 ÓRGÃO: TRE-GO PROVA: TÉCNICO DO
JUDICIÁRIO - PROGRAMAÇÃO DE SISTEMAS

Julgue os seguintes itens, a respeito da modelagem de dados.

[65] Considere a seguinte situação hipotética. Em um banco de dados referente a um curso, um aluno pode estar em mais de um curso ao mesmo tempo. Além disso, na tabela de cursos realizados por aluno, estão presentes as chaves estrangeiras aluno e curso. Nessa situação, tanto o código do curso como o código do aluno são chaves primárias nas tabelas curso e aluno, respectivamente.
[66] Ao se excluir uma tupla de um banco de dados, pode-se violar a integridade referencial desse banco por uma chave primária.
[67] Um conjunto de entidades que não possuem atributos suficientes para formar uma chave primária é definido como um conjunto de entidades fortes.
[68] Uma chave primária identifica um único valor de uma tupla no banco de dados e não possui mais de um atributo na tabela.
20. BANCA: CESPE ANO: 2015 ÓRGÃO: STJ PROVA: TÉCNICO JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

A respeito da modelagem de dados e da qualidade de software, julgue os itens subsecutivos.
[84] O relacionamento no modelo entidade-relacionamento é uma associação intuitiva entre entidades, cujo número de entidades envolvidas é conhecido como hierarquia.
[86] Entidade-relacionamento é uma modelagem semântica cujo modelo resultante é estendido, e as entidades, nesse modelo, são definidas como um ente que pode ser distintamente identificado.
21. Ano: 2016 Banca: CESPE Órgão: TCE-PA Prova: Auditor de Controle Externo -
Área Informática - Analista de Suporte

Considerando a figura apresentada, que ilustra o modelo de um banco de dados hipotético, julgue o item que se segue.
[1] A figura expõe um modelo lógico, uma vez que ele contém detalhes de implementação e é independente de um sistema gerenciador de banco de dados(SGBD).

22. Ano: 2017 Banca: CESPE Órgão: TRE-PE Prova: Analista Judiciário - Análise de
Sistemas

Assinale a opção que corresponde ao tipo de restrição de integridade expressa no próprio diagrama de entidades e relacionamentos no modelo relacional.
a) dependência b) enumeração c) normas de aceitação d) cardinalidade e) repetição
23. Ano: 2016 Banca: CESPE Órgão: TRE-PI Prova: Analista Judiciário - Análise de
Sistemas

Considere que existe uma entidade PESSOA com um relacionamento denominado
CASAMENTO que pode associar diversas ocorrências na mesma entidade PESSOA.
De acordo com as propriedades do diagrama entidade-relacionamento, o conceito desse relacionamento (CASAMENTO) pode ser definido como a) generalização.
b) relacionamento binário.

c) autorrelacionamento.

d) entidade associativa.

e) especialização.

24. Ano: 2016 Banca: CESPE Órgão: TRE-PI Prova: Técnico Judiciário - Operação de Computadores
Acerca do modelo entidade-relacionamento estendido, assinale a opção correta.

a) Uma restrição de disjunção pode ser aplicada a uma especialização, na qual deve ser especificado que as subclasses da especialização devem ser mutuamente exclusivas.
b) A generalização é o resultado da separação de um tipo-entidade de nível mais alto

— superclasse — e forma vários tipos-entidades de nível mais baixo — subclasse.

c) Uma entidade, que é membro de uma subclasse, nem sempre herda todos os atributos da entidade como um membro da superclasse.
d) O modelo em questão incorpora conceitos de modelagem entidade-relacionamento,
herança, encapsulamento e polimorfismo.

e) A simbologia do referido modelo é a mesma do modelo entidade-relacionamento,
não havendo novas representações.

25. BANCA: CESPE ANO: 2010 ÓRGÃO: INMETRO PROVA: PESQUISADOR -
GOVERNANÇA DE TI

A As entidades pessoa física e pessoa jurídica são exemplos de generalização/especialização, conceito que envolve a ideia de herança de propriedades. Herdar propriedades significa que cada ocorrência da entidade especializada possui, além de suas propriedades (atributos, relacionamentos e generalizações ou especializações), também as propriedades de ocorrência da entidade genérica correspondente.
B A cardinalidade do relacionamento entre filial e cliente define que pode existir filial sem clientes, e ainda, que os clientes podem existir sem estar vinculados a nenhuma filial.
C Telefone é exemplo de atributo opcional.

D No modelo apresentado, entidades, relacionamentos, cardinalidade e identificadores estão corretos e consistentes.
E As entidades cliente, pessoa física e pessoa jurídica apresentam relacionamento do tipo ternário ou de grau maior, que são modelados usando-se uma entidade associada,por meio de relacionamentos binários, a cada uma das entidades que participam do relacionamento ternário.
GABARITo

GABARITO

1. Errado

2. Errado

3. Certo

4. B

5. Errado

6. Errado

7. Errado

8. B

9. Certo

10. Certo

11. E

12. C

13. E

14. E C

15. E E

16. C

17. A

18. C

19. CC

20. C E E E

21. E C

22. E

23. D

24. C

25. A

26. A

LISTA DE QUESTõES - CESCRANRIO.

1. CESGRANRIO - Técnico (UNIRIO)/Tecnologia da lnformação/2019

A empresa que irá administrar o estacionamento de um clube decidiu desenvolver um sistema de informação específico para isso. Apenas os sócios poderão ter acesso ao estacionamento.Assim sendo, o sócio que tiver interesse em usar o estacionamento terá de procurar o balcão da empresa para se registrar no sistema. No ato do registro, serão informados o nome do sócio e a sua matrícula no clube, além de ser gerado, automaticamente, o número do cartão de acesso ao estacionamento e a data de validade desse cartão. Cada cartão só poderá ser usado por um único sócio. Após ser cadastrado no sistema, um sócio poderá registrar os dados (placa, modelo e cor) dos veículos que ele irá estacionar. Um veículo só pode ser registrado por um único sócio. Ocadastramento dos veículos é obrigatório, pois uma câmera de vídeo irá capturar os caracteres das placas para verificar se eles estão devidamente cadastrados. Caso não o estejam, a cancela que dá acesso ao estacionamento não será aberta. Após a saída de um veículo, o sistema irá registrar o período em que ele ficou no estacionamento. Esse registro irá conter a data e a hora de entrada, a data e a hora de saída, e o valor a ser pago pela estadia. No final do mês, será gerado um boleto para cada sócio que utilizou o estacionamento durante o mês em questão. O boleto terá um número de código de barra, a data de vencimento e o valor a ser pago. Quando o boleto for pago, será inserido no sistema um registro de pagamento, que irá informar o número do banco em que o boleto foi pago e a data do pagamento.
Qual diagrama de classes conceituais representa adequadamente os conceitos envolvidos no negócio descrito acima e as relações entre esses conceitos?
2. CESGRANRIO - Técnico (UNIRIO)/Tecnologia da lnformação/2019

A Figura a seguir representa um diagrama E-R.

Seja x uma instância de K, y uma instância de L e z uma instância de M. A
cardinalidade máxima exibida logo abaixo da entidade L significa que
A um par (x,z) pode estar associado a muitas instâncias de L.
B a entidade L possui muitas instâncias que participam de R.

C uma instância de K pode estar associada a muitas instâncias L.

D uma instância de M pode estar associada a, no máximo, uma instância de L.
E a relação R possui muitas instâncias de L.

3. CESGRANRIO - Analista (UNIRIOJ/Tecnologia da lnformação/2019

O diagrama E-R, exibido pela Figura abaixo, representa o modelo conceituai de um banco de dados.

Suponha que os elementos do conjunto T a seguir sejam instâncias da entidade de mesmo nome,presente no diagrama E-R acima.

T={tl,t2,t3,t4,t5}

Quais conjuntos completam esse banco de dados de modo que as regras definidas no modelo E-Rnão sejam violadas?

A K={kl,k2,k3,k4,k5,k6}

L={kl,k2,k3,k4,k5,k6}
M={}

S={(tl,kl),(t2,kl),(t3,kl),(t4,kl)}

B K={kl,k2,k3,k4,k5,k6}

L={kl,k2,k3,k4}

M={k4,k5,k6}
S={}

C K={kl,k2,k3,k4,k5,k6}

L={kl,k2,k3,k4}

M={k4,k5,k6}
S={(tl,kl),(t2,k2),(t4,k6)}

D K={kl,k2,k3,k4,k5,k6}
L={kl,k2}
M={k3,k4,k5,k6}

S={(t2,kl),(t3,kl),(t4,kl),(t4,k6)}
E K={kl,k2,k3,k4,k5,k6}
L={kl,k2}

M={k4,k5,k6}

4. CESGRANRIO - Analista (UNIRIO)/Tecnologia da lnformação/2019

Em qual diagrama E-R a relação R define uma função de E em F?

5. CESGRANRIO - Analista de Sistemas Júnior (TRANSPETRO)/ Processos de Negócio/2018

A Figura a seguir exibe um modelo E-R composto por duas entidades e uma relação.

Qual diagrama de Venn contém uma relação que atende às regras de multiplicidade definidas no modelo E-R acima?
6. CESGRANRIO - Escriturário (BB)/"Sem Área"/2018

Um banco de dados possui um modelo conceituai cuja descrição é feita pelo diagrama E-R a seguir.

Admita-se que o estado desse banco de dados seja definido, em parte, pelos seguintes conjuntos:

A-{ai,a2,a3,a4,a5,a6}
Al={a2,a3,a₄}

A2={ai,a₅,a₆}

C={Cl,C₂}

D={di,d₂,d₃,d₄}

Os elementos desses conjuntos representam instâncias das entidades presentes no diagrama
E-R do banco de dados em questão.
As relações que completam o estado desse banco de dados, sem que nenhuma regra de cardinalidade ou generalização seja violada, são
A Rl={(ai,ci),(a₂,ci)}
R2={}

B Rl={}

R2={}

C Rl={(ai,ci),(ai,c₂)}
R2={(a2,di),(a5,d2),(a6,d4)}

D Rl={(ci,a5),(ci,a2),(c2,a5),(c2,a2)}

R2={(a5,di),(a6,d2),(a5,d3),(a5,d4)}

E Rl={(as,ci),(a2,ci),(a5,c2),(a2,c2)}

R2={(a5,di),(a6,d2),(a5,d3),(a5,d4),(a6,d4)}

7. CESGRANRIO - Profissional (LIQUIGÁS)/Analista de Sistemas/Júnior TI/2018/Edital 02

Os conjuntos a seguir representam um banco de dados relacional.

P={pl,p2,p3}

Q={ql,q2,q3 }

R={rl,r2,r3,r4}
Tl={(pl,ql),(pl,q2),(pl,q3)}
T2={}
T3={(ql,rl),(q2,r3),(q3,r4)}

Qual modelo E-R define regras de cardinalidade compatíveis com esse banco de dados?

8. CESGRANRIO - Profissional (LIQUIGÁS)/Arquiteto de Soluções/Júnior TI/2018/EditaI 02

O modelo de Entidades e Relacionamentos (ER) é bastante utilizado na modelagem conceituai de bancos de dados. Além de utilizar entidades e seus relacionamentos para descrição dos dados, o modelo ER inclui também alguns atributos que descrevem as características de cada entidade.
Já um relacionamento também pode ter atributos

A se as cardinalidades máximas forem lxN, independentemente das cardinalidades mínimas.
B se as cardinalidades máximas forem NxN, independentemente das cardinalidades mínimas.

C.se as cardinalidades mínimas do relacionamento forem maiores que zero,
independentemente das cardinalidades máximas.
D somente se estiver participando de uma entidade associativa.
E independentemente das cardinalidades do relacionamento.

Comentário.

Sabemos que a existência de atributos no relacionamento independe da cardinalidade.
Logo, temos a nossa resposta na alternativa E.
Gabarito: E.

9. BANCA: CESGRANRIO ANO: 2014 ORGAO: PETROBRAS PROVA: TÉCNICO - TÉCNICO DE
INFORMÁTICA

O diagrama a seguir apresenta um modelo de entidades e relacionamentos segundo a notação daEngenharia de Informação.

Coleção Item Coleção
A notação equivalente em IDEF1X é

HORA DE

PRATICAR!

lO.Ano: 2016 Banca: CESGRANRIO Órgão: IBGE Prova: Supervisor de Pesquisas - Tecnologia de
Informação e Comunicação

A KWX é uma empresa do varejo que atua exclusivamente na Web. Ela está desenvolvendo um sistema de informação para registrar os pedidos de seus clientes e controlar todo o processo de entrega de mercadorias. Um pedido é entregue por uma das transportadoras conveniadas com a empresa. Quando o novo sistema estiver em funcionamento, todas elas serão devidamente cadastradas, tendo em vista melhorar a gestão de entregas pelo setor responsável. Ocusto de transporte varia de transportadora para transportadora, além de levar em conta o endereço de entrega de um pedido. Visando a reduzir o tempo de entrega, a diretoria de vendas determinou que a definição da transportadora tem de ser feita até 48h após um pedido ter sido inserido no sistema.
No ato do recebimento de um pedido, o cliente irá conferir se todos os produtos comprados estão corretos e se não houve avarias durante o transporte. Caso esteja tudo em ordem, o cliente irá assinar o recibo de entrega, pondo a data em que ela foi feita. Essa informação será posteriormente inserida no sistema por um funcionário do setor de entregas. Caso o cliente encontre algum problema, ele poderá recusar o recebimento dos produtos, informando o motivo pelo qual a entrega foi recusada. O motivo da devolução deve ser assinalado no próprio documento de entrega, que contém uma lista de motivos extraída do sistema. Um motivo possui código e descrição.
O sistema deve, também, atender a alguns requisitos adicionais. São eles:

* o cliente deve informar o endereço de entrega no momento em que inserir um pedido;

* um pedido possui um número e a data em que foi realizado;

* uma transportadora precisa ter registrados o número do CNPJ, o nome e o endereço.

Qual diagrama E-R descreve adequadamente os elementos envolvidos no negócio da empresa KWX?

c)

HORA DE

PRATICAR!

11. Ano: 2016 Banca: CESGRANRIO Órgão: UNIRIO Prova: Técnico em Tecnologia da Informação

Considere as Tabelas a seguir para responder a questão.

Essas Tabelas fazem parte do esquema de um banco de dados usado por uma associação de criadores de cães para organizar informações sobre os torneios que ela promove.
CREATE TABLE CAO (

COD NUMRERC5) NOT NULL,

NOME VARCRAR2(30) NOT NULL,

RACA VARCRAR2(50) NOT NULL,

NOME- PAI VARCRAR2(50) r

NOME 'PROPR VARCRAR2(50) NOT NULL,
CONSTRAINT CAO PK PRIMARY KEY (COD)

)

CREATE TABLE COMPETICAO (

COD NUMBER(5) NOT NULL,

DESCR VARCRAR2(50) NOT NULL,
CONSTRAINT COMPETICAO_PK PRIMARY KEY (COD)

)

CREATE TABLE ARBITRO (

COD NUMBER(5) NOT NULL,

NOME VARCHAR2(50) NOT NULL,
CONSTRAINT ARBITRO_PK PRIMARY KEY (COD)

)

CREATE TABLE
COD_CAO
COD_COMP
COLOCACAO

PARTICIPACAO (

NUMBER(5)
NUMBERfS)
NÜMBER(4)

NOT NULLf
NOT NULL,
NOT NULL,

CONSTRAINT PARTICIPACAO PK PRIMARY KEY
(COD-CAO,COD_COMP),

CONSTRAINT PARTIClPACAO_FK1 FOREIGN KEY (COD_CAO)

REFERENCES CAO (COD),

CONSTRAINT PARTIClPACAO_FK2 FOREIGN KEY (COD_COMP)
REFERENCES COMPETICAO (COD)

CREATE TABLE AVALIACAO

COD_CAO
COD_COMP
COD_ARBTR
NOTA ARBTR

NUMBERÍ5)
NUMBERÍ5)
NUMBER(5)
NUMBER(3f1)

NOT NULLj
NOT NULL,
NOT NULL,
NOT NULL,

CONSTRAINT AVALIACAO PK PRIMARY KEY

(COD CAO,COD COMPjCOD ARBTR),

CONSTRAINT AVALIACAO_FK1
REFERENCES CAO (COD),
CONSTRAINT AVALIACAO_FK2
REFERENCES COMPETICAO
CONSTRAINT AVALIACAO FK3

REFERENCES ARBITRO (COD)

FOREIGN KEY (COD- CAO)

FOREIGN KEY (COD- COMP)
(COD) ,

FOREIGN KEY (COD ARBTR)

Observações:

* A Tabela CAO contém os dados dos cães inscritos na referida associação. A coluna
NOME_PAI
indica o nome do pai de um cão, a coluna RACA indica a raça do mesmo, e a coluna NOME_PROPR
indica o nome do seu proprietário. As demais colunas são autoexplicativas.

* A Tabela COMPETICAO contém informações sobre as competições patrocinadas pela associação.Suas colunas são autoexplicativas.

* A Tabela PARTICIPACAO informa as competições das quais participaram os cães registrados na associação. Cada linha dessa tabela indica a colocação obtida por um cão em uma determinada competição. Suas colunas são autoexplicativas.
* A Tabela ARBITRO contém os dados dos árbitros que julgam os cães que participam de competições. Suas colunas são autoexplicativas.
* Cada linha da Tabela AVALIACAO representa a nota atribuída a um cão, por um determinado árbitro em uma determinada competição. Suas colunas são autoexplicativas.
Qual diagrama E-R contém um modelo conceituai compatível com as tabelas do banco de dados da associação de criadores de cães?
a)

b)

e)

HORA DE

PRATICAR!

12. Ano: 2016 Banca: CESGRANRIO Órgão: UNIRIO Prova: Técnico em Tecnologia da Informação

Uma empresa que atua no ramo de entrega de encomendas precisa de um sistema de informação para controlar sua principal atividade. Durante o levantamento dos requisitos desse sistema, as seguintes informações sobre o pagamento de entregas foram fornecidas por um funcionário da empresa:
* Uma entrega é identificada internamente por um código. Além disso, é necessário registrar o peso e as dimensões do objeto a ser entregue, o endereço de entrega e o custo da operação de entrega;
* Uma entrega pode ser paga através de cartão de crédito, cartão de débito ou boleto bancário.Visando a atender às demandas de seus clientes, uma entrega pode ser paga usando-se qualquer combinação desses três meios de pagamento;
* Em relação a um pagamento com cartão de crédito, o sistema deve registrar a data de pagamento,o valor pago, o número do cartão, sua data de validade e a instituição que o emitiu;

* Em relação a um pagamento com cartão de débito, o sistema deve registrar a data de pagamento,o valor pago, o número do banco e os números da agência e da conta corrente às quais o cartão está vinculado;
* Em relação a um pagamento com boleto bancário, o sistema deve registrar a data de pagamento,o valor pago e o número do código de barras do boleto;

* Cada pagamento registrado se refere a uma única entrega

* Não há entrega registrada no sistema que não tenha, pelo menos, um pagamento associado a ela.

Qual diagrama E-R representa corretamente os elementos e as regras presentes na descrição dos requisitos listados acima, sem que haja perda de informações ou redundância de dados,além de observar as boas práticas de modelagem conceituai de dados?
b)

e)

13. Ano: 2014 Banca: CESGRANRIO Órgão: Petrobras Prova: Técnico(a) de Exploração de Petróleo
Júnior - Informática

ALUNO (cpf: string, nome : string, endereço : string, telefone : string)
MATRICULA (cpf : string , cod-cad : string)

CADEIRA (cod-cad : string, nome : string , créditos : number)

A representação do esquema relacional acima, segundo um diagrama de entidades e relacionamentos, deve representar ALUNO, MATRICULA e CADEIRA, respectivamente, como a) entidade, relacionamento nxm e entidade b) entidade, relacionamento lxn e entidade c) entidade, entidade e atributo d) entidade, entidade e relacionamento nxm e) entidade, atributo e entidade
14. Ano: 2014 Banca: CESGRANRIO Órgão: CEFET-RJ Prova: Analista de Tecnologia da Informação

Uma das características do Modelo de Entidade e Relacionamentos é que a) cada domínio de possíveis valores possui um atributo.
b) dois conjuntos de entidades são sempre disjuntos.

c) toda chave candidata é uma chave primária.

d) todos os atributos em determinado conjunto de atributos têm o mesmo conjunto de entidades.

e) um conjunto de relacionamentos pode ser considerado um conjunto de n-tuplas.

HORA DE

PRATICAR!

15. Ano: 2014 Banca: CESGRANRIO Órgão: Banco da Amazônia Prova: Técnico Científico - Banco de
Dados

Para responder à questão, tenha como referência o diagrama de entidades e relacionamentos,apresentado abaixo, que representa parte do modelo de dados de uma instituição financeira.

Movimento

Conta

<-------------------------------- >

seq_movimento data_hora_movimento credito_debito valor numero-documento ti po_docu mento dep_origem historico
Vsaldo J

Contato_Cliente id_telefone telefone tipO—telefone
A

Cliente id_cliente
-|- nome_cliente i datajnicio data fim
EnderecO-Cliente

\
id_endereco inicio_validade_endereco fim_validade_endereco logradouro numero complemento cep bairro cidade k_e_s_ta_d_o z
Que representação gráfica do modelo ER proposta pela notação IDEF1X representa relacionamento existente entre Conta e Cliente?
3 PRATICAR!

16. Ano: 2014 Banca: CESGRANRIO Órgão: Banco da Amazônia Prova: Técnico Científico - Banco de
Dados

Para responder à questão, tenha como referência o diagrama de entidades e relacionamentos,apresentado abaixo, que representa parte do modelo de dados de uma instituição financeira.

Movimento

Conta seq_movimento data_hora_movimento creditO—debito valor numero-documento tipo—documento dep_origem historico k_sald_o >
Endereco Cliente id_endereco inicio_validade_endereco fim_validade_endereco logradouro numero complemento cep bairro cidade k_e_sta_do_ z
Sendo feita a transformação desse modelo de dados em um modelo diretamente equivalente a um modelo relacional, de maneira a manter o número mínimo de Tabelas necessárias, e sendo feita a migração das chaves para constituir as chaves externas, sem o uso de chaves substitutas, quantos campos serão adicionados ao modelo?
a) 7

b) 8

c) 9

d) 11

e) 13

HORA DE

PRATICAR!

17. Ano: 2014 Banca: CESGRANRIO Órgão: Banco da Amazônia Prova: Técnico Científico - Análise de Sistemas
A federação de futebol de um estado brasileiro resolveu criar uma nova forma de vender ingressos para os jogos do seu campeonato estadual. Lotes de cartões com chip, semelhantes a cartões de crédito, serão enviados para lojas credenciadas. O torcedor que queira comprar ingressos para os jogos terá de se cadastrar, antecipadamente, na federação e dirigir- -se a uma das lojas para adquirir um desses cartões e carregá-lo com ingressos para os jogos a que desejar comparecer.A entrada nos estádios será feita mediante a apresentação do cartão contendo os ingressos que o torcedor comprou. Cada torcedor poderá possuir um único cartão. O controle será feito pelo número do CPFdo torcedor. Um cartão terá um número, que o identificará. Esse número será gravado no chip pelo fabricante dos cartões, e registrado no sistema da federação, antes que o cartão seja enviado para uma loja credenciada.
Qual diagrama E-R descreve, adequadamente, as regras de negócio apresentadas acima, além de observar os preceitos de um bom modelo conceituai de dados?
a)

c)

e)

HORA DE

PRATICAR!

18. Ano: 2014 Banca: CESGRANRIO Órgão: FINEP Prova: Analista - Desenvolvimento de Sistemas

Um país irá leiloar blocos de exploração de petróleo e precisa de um sistema de informação para controlar o registro dos consórcios que participarão dos leilões, os lances que serão realizados e o vencedor de cada leilão. Todos os consórcios que irão disputar os leilões terão que ser previamente cadastrados no sistema. Um consórcio é formado por uma ou mais empresas.
O objeto de cada leilão é um bloco de exploração. Os consórcios poderão registrar vários lances para cada bloco disputado. Os lances, entretanto, terão de ser maiores ou iguais a um valor mínimo, que será fixado, para cada bloco, antes de cada leilão.
Além de atender aos requisitos acima, o sistema de informação em questão deve responder às seguintes questões:
* Qual é o nome do consórcio vencedor?

* Quais são as empresas que integram um determinado consórcio?

* Qual é o país de origem de uma determinada empresa?

* Qual é o nome de uma determinada área de exploração? Onde ela está localizada?

* Qual é o código de um determinado bloco de exploração? Onde ele está localizado? A
que área de exploração ele pertence?
Qual diagrama E-R atende a todos os requisitos descritos acima?

c)

GABARITo

1. D

2. A

3. A

4. D

5. D

6. D

8. E

9. A

io. c

11. C

12. C

13. A

14. E

15. B

16. D

17. D

18. C

LISTA DE QUESTõES - CEBRASPE

1. CEBRASPE (CESPE) - Auditor de Finanças e Controle de Arrecadação da Fazenda
Estadual (SEFAZ AL)/2020

Com relação a banco de dados, julgue o item seguinte.

Com base no diagrama a seguir, é correto afirmar que um item na entidade Ambiente pode não relacionar-se com nenhum item na entidade Setor ou pode relacionar-se com vários itens nesta entidade, enquanto um item na entidade Setor pode relacionar-se somente com um item na entidade Ambiente.

1. CEBRASPE (CESPE) - Ana Min (MPE CE)/MPE CE/Ciências da Computação/2020

Considerando o diagrama entidade- relacionamento precedente e os múltiplos aspectos que a modelagem de dados oferece ao analista para examinar os dados no contexto de uma aplicação de software, julgue o item subsecutivo.
No diagrama apresentado, a modalidade obrigatória que conecta transportador e transporta indica que, para todo alimento fabricado, é necessária uma ação de transporte.
2. CEBRASPE (CESPE) - Ana Min (MPE CE)/MPE CE/Ciências da Computação/2020

Considerando o diagrama entidade- relacionamento precedente e os múltiplos aspectos que a modelagem de dados oferece ao analista para examinar os dados no contexto de uma aplicação de software, julgue o item subsecutivo.
A cardinalidade e a modalidade apresentada para a entidade fabricante mostram que obrigatoriamente um fabricante inicializa a ação de solicitação de distribuição,contratação de transporte e produção de alimento, o que caracteriza uma relação 1 x n.
3. CEBRASPE (CESPE) -Ass Min (MPC TCE-PA)/TCE-PA/lnformática/2019

As seguintes informações foram extraídas de um diagrama de entidades-
relacionamento no contexto de um banco de dados relacional.

De acordo com as informações do texto 9A1-I, assinale a opção correta, com relação à leitura das regras do negócio representadas no modelo apresentado.
a) Ao realizar uma reserva, o cliente pode escolher um ou vários trechos de voo.
Existem várias opções de aeronaves para o trecho reservado.

b) Ao realizar uma reserva, o cliente pode escolher um ou vários trechos de voo, mas existe apenas uma aeronave alocada para o trecho reservado.
c) Ao realizar uma reserva, o cliente pode escolher apenas um trecho de voo, mas existem várias opções de aeronaves para o trecho reservado.
d) Um trecho de voo está relacionado a apenas uma reserva.

e) Ao realizar uma reserva, o cliente recebe um único número de assento, válido para todos os trechos que forem reservados.
4. CEBRASPE (CESPE) - Tec (EBSERH)/EBSERH/lnformática/2018

Tendo como referência o modelo lógico precedente, julgue o item a seguir.

A partir do modelo apresentado, infere-se que um hospital pode estar vinculado a várias universidades, pois a tabela Hospital apresenta cardinalidade (0, n).
5. CEBRASPE (CESPE) - APF/PF/2018

Considerando o modelo entidade-relacionamento (ER) precedente, julgue o seguinte item, relativo a banco de dados.
Conforme o modelo ER em questão, um tipo de produto pode estar associado a somente 1 produto e cada produto possui um preço e uma descrição.
6. CEBRASPE (CESPE) - Ana Min (MPE PI)/MPE Pl/Tecnologia da lnformação/2018

Tendo em vista que, ao se desenvolver um sistema de vendas e compras para um cliente, devem-se descrever os produtos, as entradas, as saídas, o controle de estoque e o lucro das vendas, julgue o item subsequente, relativo à modelagem de dados para a aplicação descrita.
No sistema implementado, o cliente terá de cadastrar cada produto nos módulos de vendas e compras, pois a redundância será controlada pelo usuário, e não pela modelagem do banco de dados.
7. CEBRASPE (CESPE) - AFA (SEFAZ RS)/SEFAZ RS/2018

No modelo entidade-relacionamento, as propriedades particulares que descrevem uma entidade são denominadas a) valores.
b) atributos.

c) chaves primárias.

d) relacionamentos.

e) instâncias.

8. CEBRASPE (CESPE) - Tec (FUB)/FUB/Tecnologia da lnformação/2018

Julgue o item seguinte, a respeito dos conceitos de modelagem de dados e níveis de abstração.
No modelo de entidade-relacionamento, uma entidade se caracteriza por um objeto do mundo real que possui um conjunto de propriedades; os valores de um subconjunto dessas propriedades podem identificar de maneira única a entidade.
9. CEBRASPE (CESPE) - Tec (FUB)/FUB/Tecnologia da lnformação/2018

Julgue o item seguinte, a respeito dos conceitos de modelagem de dados e níveis de abstração.
Na cardinalidade de mapeamento entre o conjunto de entidades X e Y de uma associação um-para-um, uma entidade em X é associada, no máximo, a uma entidade em Y, e uma entidade em Y é associada, no máximo, a uma entidade em X.
10. Ano: 2018 Banca: CESPE Órgão: STJ Cargo: Técnico Judiciário - Suporte
Técnico

Acerca de banco de dados, julgue os itens que se seguem.

75 Em um diagrama MER, a entidade representa uma coisa concreta do mundo real,
enquanto as coisas abstratas são representadas pelo relacionamento entre as entidades.
11. Ano: 2018 Banca: CESPE Órgão: STJ Cargo: Técnico
Judiciário -
Desenvolvimento de Sistemas Questão: 64 e 65

Julgue os itens a seguir, referentes à modelagem de dados.

64 Generalização é o processo de definição de um tipo de entidade a partir de duas ou mais entidades que possuem atributos em comum — por exemplo, as entidades carro e ônibus podem ser generalizadas na superclasse veículo.
12. Ano: 2018 Banca: CESPE Órgão: TCM-BA Cargo: Auditor de Contas Questão:

A respeito de entidades, relacionamentos e tipos de chave, assinale a opção correta.
A Uma entidade fraca não possui seus próprios atributos chave.

B Toda relação deve possuir somente uma chave primária de atributo único.

C Um identificador ou chave é usado para determinar exclusivamente uma instância de um relacionamento entre entidades.
D A abordagem entidade-relacionamento permite somente relacionamentos binários e dos tipos 1:1 e 1:n.
E Uma entidade forte existe no banco de dados e possui atributos que a identificam sem que ela precise estar associada a outra entidade identificadora.
13. Ano: 2018 Banca: CESPE Órgão: STM Cargo: Programação de Sistemas
Questão: 61 a 65

Acerca dos conceitos de normalização de dados e dos modelos de dados, julgue os itens subsequentes.
63 O modelo conceituai, que reflete uma estrutura simplificada do banco de dados, é responsável por registrar como os dados estão armazenados no sistema de gerenciamento de banco de dados (SGBD).
64 Comparativamente aos usados pelos usuários leigos, os modelos de dados utilizados por programadores são considerados menos abstratos, pois contêm mais detalhes de como as informações estão organizadas internamente no banco de dados.
14. BANCA: CESPE ANO: 2014 ÓRGÃO: ANATEL PROVA: ANALISTA
ADMINISTRATIVO - DESENVOLVIMENTO DE SISTEMAS DE INFORMAÇÃO

Com base nos modelos de banco de dados, julgue os itens subsequentes.

[89] São empregados no projeto de aplicações de um banco de dados o modelo entidade-relacionamento (MER), que é um modelo representacional, e suas variações.
[90] O modelo de dados físico é considerado de baixo nível, o que significa que somente os sistemas gerenciadores de banco de dados conseguem interpretá-lo.
15. Ano: 2015 Banca: CESPE Órgão: TRE-PI Cargo: Operação de computadores -
Questão 40

De acordo com a notação para diagramas entidade-relacionamento, assinale a opção que descreve a representação acima disposta.
A entidade, atributo, atributo composto e atributo derivado

B relacionamento, atributo, atributo fraco e atributo multivalorado

C entidade fraca, atributo-chave, atributo multivalorado e atributo derivado
D entidade, atributo-chave, atributo multivalorado e atributo derivado

E entidade forte, atributo, atributo composto e atributo fraco

16. Ano: 2015 Banca: CESPE Órgão: TRE-PI Cargo: Operação de computadores -
Questão 41

Acerca do modelo entidade-relacionamento estendido, assinale a opção correta.

A Uma restrição de disjunção pode ser aplicada a uma especialização, na qual deve ser especificado que as subclasses da especialização devem ser mutuamente exclusivas.
B A generalização é o resultado da separação de um tipo-entidade de nível mais alto

— superclasse — e forma vários tipos-entidades de nível mais baixo — subclasse.

C Uma entidade, que é membro de uma subclasse, nem sempre herda todos os atributos da entidade como um membro da superclasse.
D O modelo em questão incorpora conceitos de modelagem entidade-relacionamento,
herança, encapsulamento e polimorfismo.

E A simbologia do referido modelo é a mesma do modelo entidade-relacionamento,
não havendo novas representações.

17. Ano: 2015 Banca: CESPE Órgão: TRE-PI - Questão 57

Considere que existe uma entidade PESSOA com um relacionamento denominado
CASAMENTO que pode associar diversas ocorrências na mesma entidade PESSOA.
De acordo com as propriedades do diagrama entidade-relacionamento, o conceito desse relacionamento (CASAMENTO) pode ser definido como
A generalização.

B relacionamento binário.
C autorrelacionamento.

D entidade associativa.
E especialização.

18. BANCA: CESPE ANO: 2015 ÓRGÃO: MPOG PROVA: ANALISTA - ANALISTA EM
TECNOLOGIA DA INFORMAÇÃO

A respeito de modelo entidade-relacionamento e normalização, julgue os itens subsequentes.
[113] Em relações normalizadas, na primeira forma normal, toda tupla em toda relação contém apenas um único valor, do tipo apropriado, em cada posição de atributo.
[114] Sabendo que, nos relacionamentos ternários, a cardinalidade refere-se a pares de entidades, em um relacionamento ternário R entre três entidades A, B e C, a cardinalidade máxima de A e B dentro de R indica quantas ocorrências de C podem estar associadas a um par de ocorrências de A e B.
19. BANCA: CESPE ANO: 2015 ÓRGÃO: TRE-GO PROVA: TÉCNICO DO
JUDICIÁRIO - PROGRAMAÇÃO DE SISTEMAS

Julgue os seguintes itens, a respeito da modelagem de dados.

[65] Considere a seguinte situação hipotética. Em um banco de dados referente a um curso, um aluno pode estar em mais de um curso ao mesmo tempo. Além disso, na tabela de cursos realizados por aluno, estão presentes as chaves estrangeiras aluno e curso. Nessa situação, tanto o código do curso como o código do aluno são chaves primárias nas tabelas curso e aluno, respectivamente.
[66] Ao se excluir uma tupla de um banco de dados, pode-se violar a integridade referencial desse banco por uma chave primária.
[67] Um conjunto de entidades que não possuem atributos suficientes para formar uma chave primária é definido como um conjunto de entidades fortes.
[68] Uma chave primária identifica um único valor de uma tupla no banco de dados e não possui mais de um atributo na tabela.
20. BANCA: CESPE ANO: 2015 ÓRGÃO: STJ PROVA: TÉCNICO JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

A respeito da modelagem de dados e da qualidade de software, julgue os itens subsecutivos.
[84] O relacionamento no modelo entidade-relacionamento é uma associação intuitiva entre entidades, cujo número de entidades envolvidas é conhecido como hierarquia.
[86] Entidade-relacionamento é uma modelagem semântica cujo modelo resultante é estendido, e as entidades, nesse modelo, são definidas como um ente que pode ser distintamente identificado.
21. Ano: 2016 Banca: CESPE Órgão: TCE-PA Prova: Auditor de Controle Externo -
Área Informática - Analista de Suporte

Considerando a figura apresentada, que ilustra o modelo de um banco de dados hipotético, julgue o item que se segue.
[1] A figura expõe um modelo lógico, uma vez que ele contém detalhes de implementação e é independente de um sistema gerenciador de banco de dados(SGBD).

22. Ano: 2017 Banca: CESPE Órgão: TRE-PE Prova: Analista Judiciário - Análise de
Sistemas

Assinale a opção que corresponde ao tipo de restrição de integridade expressa no próprio diagrama de entidades e relacionamentos no modelo relacional.
a) dependência b) enumeração c) normas de aceitação d) cardinalidade e) repetição
23. Ano: 2016 Banca: CESPE Órgão: TRE-PI Prova: Analista Judiciário - Análise de
Sistemas

Considere que existe uma entidade PESSOA com um relacionamento denominado
CASAMENTO que pode associar diversas ocorrências na mesma entidade PESSOA.
De acordo com as propriedades do diagrama entidade-relacionamento, o conceito desse relacionamento (CASAMENTO) pode ser definido como a) generalização.
b) relacionamento binário.

c) autorrelacionamento.

d) entidade associativa.

e) especialização.

24. Ano: 2016 Banca: CESPE Órgão: TRE-PI Prova: Técnico Judiciário - Operação de Computadores
Acerca do modelo entidade-relacionamento estendido, assinale a opção correta.

a) Uma restrição de disjunção pode ser aplicada a uma especialização, na qual deve ser especificado que as subclasses da especialização devem ser mutuamente exclusivas.
b) A generalização é o resultado da separação de um tipo-entidade de nível mais alto

— superclasse — e forma vários tipos-entidades de nível mais baixo — subclasse.

c) Uma entidade, que é membro de uma subclasse, nem sempre herda todos os atributos da entidade como um membro da superclasse.
d) O modelo em questão incorpora conceitos de modelagem entidade-relacionamento,
herança, encapsulamento e polimorfismo.

e) A simbologia do referido modelo é a mesma do modelo entidade-relacionamento,
não havendo novas representações.

25. BANCA: CESPE ANO: 2010 ÓRGÃO: INMETRO PROVA: PESQUISADOR -
GOVERNANÇA DE TI

A As entidades pessoa física e pessoa jurídica são exemplos de generalização/especialização, conceito que envolve a ideia de herança de propriedades. Herdar propriedades significa que cada ocorrência da entidade especializada possui, além de suas propriedades (atributos, relacionamentos e generalizações ou especializações), também as propriedades de ocorrência da entidade genérica correspondente.
B A cardinalidade do relacionamento entre filial e cliente define que pode existir filial sem clientes, e ainda, que os clientes podem existir sem estar vinculados a nenhuma filial.
C Telefone é exemplo de atributo opcional.

D No modelo apresentado, entidades, relacionamentos, cardinalidade e identificadores estão corretos e consistentes.
E As entidades cliente, pessoa física e pessoa jurídica apresentam relacionamento do tipo ternário ou de grau maior, que são modelados usando-se uma entidade associada,por meio de relacionamentos binários, a cada uma das entidades que participam do relacionamento ternário.
GABARITo

GABARITO

1. Errado

2. Errado

3. Certo

4. B

5. Errado

6. Errado

7. Errado

8. B

9. Certo

10. Certo

11. E

12. C

13. E

14. E C

15. E E

16. C

17. A

18. C

19. CC

20. C E E E

21. E C

22. E

23. D

24. C

25. A

26. A

