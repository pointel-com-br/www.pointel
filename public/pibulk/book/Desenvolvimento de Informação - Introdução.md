# Desenvolvimento de Informação - Introdução

Índice

1) Conceitos Básicos de Banco de Dados.

2) Características da Abordagem de BD

3) Personagem do Ecossistema de BD

4) Evolução História dos SGBD's

5) Classificação dos SGBD's.

6) Modelos de Dados e Arquitetura em 3 Esquemas - Instâncias x Esquemas.

7) Modelo de Dados.

8) Arquitetura 3 Esquemas.

9) Ambiente do Sistema de Banco de Dados.

10) Questões Comentadas - Conceitos Básicos de Banco de Dados - CEBRASPE

11) Questões Comentadas - Conceitos Básicos de Banco de Dados - CESGRANRIO

12) Lista de Questões - Conceitos Básicos de Banco de Dados - CEBRASPE

13) Lista de Questões - Conceitos Básicos de Banco de Dados - CESGRANRIO

CoNCEIToS DE BANCo DE DADoS

CoNCEIToS BÁSICoS

Antes de adentrar nos conceitos de banco de dados gostaria de voltar um pouco no tempo. Preciso que você conheça os sistemas de arquivo. Você deve ter acesso a um sistema de arquivo do computador ou dispositivo que você está usando para ter acesso a esse conteúdo. Agora imagine a seguinte situação: você trabalha em uma empresa e a lista de clientes está armazenada em um arquivo do Excel.
Você e todos os demais funcionários do setor de vendas (isso mesmo, na nossa história você trabalha no setor de vendas!!) fazem acesso ao mesmo arquivo para incluir e atualizar dados dos clientes.Quando o arquivo começa a ficar sem controle vocês resolvem criar cópias do mesmo para que cada vendedor possa ter seu próprio cadastro. Perceba que a solução do problema de acesso simultâneo nos leva a outro problema: redundância de dados. Várias cópias sem um controle centralizado e automatizado podem ainda ter inconsistência entre os dados armazenados.
Para resolver o problema da redundância não controlada, você e seus colegas de trabalho ouvem falar de uma solução robusta para o problema de armazenamento de dados. Essa solução passa por manter apenas uma cópia dos dados em um banco de dados e usar um sistema gerenciador para controlar o acesso concorrente. Perceba que neste
OfAHcOKm momento a redundância, caso exista, passa a ser controlada por um sistema, de forma automática.Neste sentido, podemos definir os dois tipos de redundância que podem existir entre arquivos ou conjuntos de dados.
ESCLARECENDO! Há dois tipos de redundância de dados:
Redundância controlada de dados: Acontece quando o software tem conhecimento da múltipla representação da informação e garante a sincronização entre as diversas representações.
Redundância não controlada: Acontece quando a responsabilidade pela manutenção da sincronia entre as diversas representações de uma informação está com o usuário e não com o software.
No universo tecnológico o que aconteceu em um passado recente teve como motivação a mesma lógica do problema do cadastro de clientes da sua empresa se vendas (Isso mesmo, você ainda está trabalhando lá!). Aplicativos empresariais faziam acesso a arquivos sem um elemento central para controlar o processo, isso criava o caos pois não tínhamos controle da redundância. Eis que surge o
Sistema de Gerenciamento de Banco de Dados (SGBD) para atuar como um guardião do banco de dados, que substituiu a abordagem de arquivos. Vejamos uma figura para esclarecer esses contextos:
Sistema de arquivos Sistema de Banco de Dados

Dados
(arquivos)

Aplicativos

Figura 1 - Sistemas de arquivos e sistema de banco de dados

A figura mostra dois sistemas. O primeiro representa a estrutura de um sistema de arquivos onde os dados são acessados diretamente pelos aplicativos. Na segunda temos um sistema de banco de dados no qual o SGBD aparece entre os dados e os aplicativos.
Perceba que do lado esquerdo não temos o SGBD, já do lado direito existe o elemento.
Para entender como e por que esse camarada apareceu aí vamos compreender os conceitos elementares para o entendimento do assunto. Em qualquer ciência, o entendimento completo do seu conteúdo deve se basear nos conceitos fundamentais. Nossa aula começa focada nesses conceitos.
E o primeiro conceito que preciso que você armazene é o de banco de dados, neste instante, você seria capaz de responder a seguinte pergunta:
O que é banco de dados?

Você já consegue definir esse termo e suas principais características? Se você ainda não tem o entendimento perfeito do que seria um banco de dados, nosso objetivo agora é construir o conceito.Uma forma tradicional de definir banco de dados é começar entendendo o significado das palavras que compõe o termo: Banco e dados.
Banco tem diversas definições possíveis no dicionário da língua portuguesa. Dentre elas a que melhor se encaixa no nosso contexto é um conjunto organizado e categorizado de objetos, por exemplo, podemos ter um banco de fotografias ou um banco de leite.
Dados são fatos conhecidos que podem ser registrados e possuem um significado implícito. Esse conceito, porém, é um pouco amplo e abstrato para nosso intuito. Quando reduzimos o escopo à tecnologia da informação, temos um conceito mais adequado para dado. Ele é a representação física de um evento no tempo e espaço que não agrega fundamento ou significado para quem o sente ou recebe. É, basicamente, um registro!
Imagine que eu fale para você por "32260436, cinco, aprovado, Thiago". Você vai pensar, o professor está ficando louco! Mas em um banco de dados, esses registros são armazenados e chamados de dados. Para representarem uma informação eles precisam de um contexto associado. Se pensarmos em uma agenda telefônica o número "32260436" pode ser o telefone de Thiago. Aprovado pode ser a sua situação no seu próximo concurso e cinco seria a colocação no referido certame.
Agora que temos o entendimento dos termos vamos partir para a definição do banco de dados.
De forma simples e direta: um Banco de dados é uma coleção de dados relacionados. Vejam que essa definição não estabelece a necessidade dos dados serem armazenados em formato digital.Alguns livros trazem o exemplo de uma agenda telefônica de papel como um exemplo bastante didático do conceito de banco de dados.
Esta definição, porém, é considerada muito simplista para alguns autores por não contextualizar o termo. O Navathe, por exemplo, cita três propriedades implícitas que contribuem para o entendimento do termo banco de dados (BD).Primeiramente, o BD
representa algum aspecto do mundo real, às vezes chamado de minimundo ou de universo de discurso (UoD- Universe of Discourse). As mudanças no minimundo devem ser refletidas no banco de dados.
A segunda característica implícita diz que a coleção de dados é logicamente coerente com algum significado inerente. Uma variedade aleatória de dados não pode ser chamada de banco de dados.Um banco de dados pode armazenar as informações de uma empresa, uma faculdade ou um órgão do setor público. Veja que essas informações estão dentro de um contexto, sendo,logicamente coerente.
A terceira propriedade afirma que um banco de dados é construído e populado com dados para uma finalidade específica. Ele possui um grupo de usuários bem definido e algumas aplicações,previamente concebidas, sobre as quais esses usuários interessados fazem acesso aos dados. Não adianta você criar um repositório sem propósito! Ele tem que atender alguma necessidade de acesso ao conjunto dos dados.
Vamos voltar ao nosso exemplo físico da agenda telefônica, você consegue visualizar as propriedades definidas pelo Navathe neste banco de dados. Qual o aspecto do mundo real que ela representa? Os dados estão logicamente relacionados? Possuem uma finalidade específica?Acredito que sim! Tente responder a essas perguntas mentalmente antes de seguir em frente.

EXEMPLIFICANDO

Respondendo ... a agenda telefônica descreve um aspecto do mundo real, por exemplo, a agenda que seu pai armazena os contatos dos amigos e familiares. Esses dados são logicamente relacionados,geralmente, em ordem alfabética, cada letre apresenta os contatos com números de telefone, endereço e outras informações. Por fim, existe um propósito para a existência da agenda: todos da casa podem ter um acesso rápido aos contatos familiares. Seu Zacarias (painho) possui até hoje uma agenda telefônica ao lado aparelho ... funciona muito bem!
Okl! As três propriedades definidas pelo Navathe começam a estruturar os conceitos na sua cabeça.Vamos consolidar o conceito de banco de dados apresentado mais algumas definições presentes na literatura:
nqut

O banco de dados, por si só, pode ser considerado como o equivalente eletrônico de um armário de arquivamento; ou seja, ele é um repositório ou recipiente para uma coleção de arquivos de dados computadorizados. - C JDate

Banco de dados é um conjunto de dados integrados que tem por objetivo atender a uma comunidade de usuários - Carlos Heuser.
Banco de dados é um conjunto de dados estruturados que são confiáveis, coerentes e compartilhados por usuários que têm necessidades de informações diferentes.-
Silberchatz

Acho que você já entendeu o conceito de banco de dados! Na lista acima, você conheceu todas as definições que podem aparecer na sua prova. :)
Vamos agora entender a diferença entre banco de dados, sistemas de gerenciamento de banco de dados (SGBD) e sistemas de banco de dados (SBD). São três conceitos diferentes para os autores dos livros teóricos sobre o assunto. Para entender essas diferenças peço que você observe a figura a seguir:
Figura 2 - Visão geral do relacionamento entre banco de dados e SGBD

Seguindo o fluxo de acesso aos dados, podemos observar que os usuários e programadores se comunicam com o sistema de banco de dados. Este, por sua vez, faz acesso ao sistema de gerenciamento do banco de dados. O SGDB usa as informações presentes nos bancos de dados,representados pelos cilindros da figura acima, para ter acesso aos dados armazenados.

Um Sistema de Gerenciamento de Banco de Dados (SGBD) é um conjunto de programas que permitem armazenar, modificar e extrair informações de um banco de dados. Seu principal objetivo é proporcionar um ambiente tanto conveniente quanto eficiente para a recuperação e armazenamento das informações do banco de dados.
Contudo, os SGBDs não se restringem apenas a manipulação dos dados. Eles fornecem uma variedade de programas com diferentes funcionalidades.
k

Gontrole dle t ransaçõe s á k
1Ajuste/

1runninj 7

F

á k íÇiGBt i
1 F

seguranç a cle acesstD
ontrole d mcorrênc
Reícuperaçe30

4 '3pós falhe3

Figura 3 - Principais funcionalidades de um SGBD.

A figura acima apresenta algumas funcionalidades dos SGBDs. Cada espaço está preenchido com alguma funcionalidade que faz parte do escopo de um software de SGBD. Não se preocupe se você não tiver ideia do que está presente em cada espaço, ao longo desta aula ou do nosso curso, quando você começar a entender melhor o assunto, você perceberá a presença deles dentro do contexto de um SGBD. Vamos em frente!
Outro aspecto interessante sobre banco de dados são as descrições ou definições dos objetos, pense em uma tabela do modelo relacional. Para termos acesso a uma tabela precisamos conhecer sua estrutura, começando pelo seu nome e das suas colunas. Essa tarefa envolve especificar os tipos,estruturas e restrições dos dados a serem armazenados.

A definição ou informação descritiva do banco de dados também é armazenada pelo SGBD
numa estrutura conhecida como catálogo ou dicionário de dados, que armazena os chamados de metadados dos objetos. Os metadados carregam consigo um significado. Uma coluna de uma tabela pode ser definida por um tipo de dados, inteiro, uma restrição, not null.
É possível ainda fazer o compartilhamento dos dados entre diversos usuários e programas,possibilitando o acesso ao banco de dados de forma simultânea. Outras funções importantes também são providas como proteção do sistema contra defeitos de hardware e software,feitos por meio de redundância ou replicação, e proteção de segurança contra acesso não autorizados ou maliciosos.
Outros aspectos interessantes estão relacionados com o controle de transações,
recuperação após falha, otimização de consultas ou do próprio SGBD, auditoria por meio de logs de sistema, enfim,
são várias as funcionalidades providas pelos softwares presentes em um SGBD. Vamos agora definir o próximo conceito: sistema de banco de dados!
O sistema de banco de dados (SBD) é considerado a união entre o banco de dados e o sistema de gerenciamento de banco de dados. Em outras palavras, consiste em uma coleção de dados inter-relacionados e de um conjunto de programas para acessá-los. Partindo da figura que apresentamos anteriormente conseguimos construir a seguinte fórmula:
SBD = BD + SGBD + (Programa de aplicação/consulta)

Antes de continuarmos construindo nosso arcabouço teórico sobre o assunto vamos resolver algumas questões de provas passadas.
1. Gestor da Informação (Curitiba)/2019

O principal objetivo de um Sistema Gerenciador de Banco de Dados (SGBD) é:

a) criar a infraestrutura para a construção de um data warehouse.

b) armazenar e recuperar os dados de forma conveniente e eficiente.

c) organizar os dados para suportar operações de OLAP.

d) possibilitar a armazenagem distribuída dos dados.

e) facilitar a implementação de tecnologias de armazenagem em nuvem.

Comentário: Vejam que, pelas definições acima apresentada um SGBD é definido como um sistema cujo objetivo é armazenar e recuperar dados de forma eficiente. Analisando as demais alternativas, elas não fazem sentido para definirem o principal objetivo do SGBD. Vamos deixar para apresentar os conceitos referente as palavras "data warehouse", OLAP e computação na nuvem em outro momento, para não atrapalhar seu processo de aprendizado.
Mas professor, eu queria aprender agora ... ok! Então vamos nessa.

Data Warehouse (DW) é um repositório de dados utilizado para guardar dados analíticos.
OLAP
é um conjunto de ferramentas e definições que permitem acessar e trabalhar com os dados noDW.

O armazenamento distribuído dos dados é uma possibilidade dentre das funções do SGBD,
mas não é seu principal objetivo.
A computação em nuvem é o fornecimento de serviços de computação, incluindo servidores,
armazenamento, bancos de dados, rede, software, análise e inteligência, pela
Internet ("a nuvem") para oferecer inovações mais rápidas, recursos flexíveis e economias de escala.Você normalmente paga apenas pelos serviços de nuvem que usa, ajudando a reduzir os custos operacionais, a executar sua infraestrutura com mais eficiência e a escalonar conforme as necessidades da sua empresa mudam.
Assim, reforçando a nossa resposta encontra-se na alternativa B.

Gabarito: B.

2. Ano: 2019 - Prefeitura de Jataí - GO - Analista de Tecnologia da Informação

Com relação aos conceitos e às definições de banco de dados, assinale a alternativa correta.

A Um banco de dados não é formado por um conjunto de arquivos, mas sim por um conjunto de dados com as mesmas características.
B Um banco de dados é um conjunto de dados organizados, com o objetivo de armazenamento persistente dos dados, que possui mecanismos de manipulação e recuperação de informações.
C Um banco de dados é um conjunto integrado de dados não relacionados logicamente.

D A melhor definição para banco de dados é que ele é uma representação estática, visto que os dados não podem sofrer alterações temporais.
E O banco de dados é uma estrutura de compartilhamento parcial, ou seja, os dados existentes em um banco de dados não podem ser compartilhados por várias pessoas; apenas uma pessoa por vez pode ter acesso ao banco de dados.
Comentário: Vamos comentar cada uma das alternativas. (A) Todo banco de dados digital,
em última instância, é formado por um conjunto de arquivos. (B) Perfeita a definição!!Perceba que ele disse que o banco de dados é o conjunto de dados organizados e que possui mecanismos de manipulação, esses são parte do SGBD que possui outras funcionalidades além da manipulação dos dados, como backup e controle de acesso. (C) O banco de dados é um conjunto logicamente relacionados. (D) O banco de dados possui uma representação dinâmica, tanto os dados, quanto os modelos podem ser ajustados para se adaptarem a mudanças no minimundo que eles descrevem. (E) Os dados do banco de dados são compartilhados entre diferentes grupos de usuários. No geral, cada grupo possui a visão de apenas parte do banco de dados.
Gabarito: B

3. Ano: 2016 Órgão: TCE-SC Prova: Auditor Fiscal de Controle Externo - Informática

Com relação aos bancos de dados relacionais, julgue o próximo item.

O catálogo de um sistema de gerenciamento de banco de dados relacional armazena a descrição da estrutura do banco de dados e contém informações a respeito de cada arquivo,do tipo e formato de armazenamento de cada item de dado e das restrições relativas aos dados.
Comentário: Perceba que a definição acima está de acordo com o termo dicionários de dados,catálogo de dados ou metadados presentes em um sistema de banco de dados. Lembre-se que essa separação entre a descrição dos dados e os dados propriamente dito é uma das características relevantes que foram apresentadas na evolução de sistemas de arquivos para a l abordagem de banco de dados. Sendo assim, podemos afirmar que a questão está correta!
Gabarito: C.

4. Ano: 2010 Órgão: Banco da Amazônia Prova: Técnico Científico - Tecnologia da Informação

O dicionário de dados é uma das principais ferramentas para a administração dos dados corporativos. Por meio da engenharia reversa, pode-se armazenar os modelos de dados, as estruturas de dados, seus relacionamentos e toda a documentação necessária para garantir facilidade na localização e manipulação dos dados. Acerca dos papéis do administrador de dados (AD) e dos dicionários de dados, julgue os itens a seguir.
[1] O dicionário de dados é considerado um subconjunto das funções de um catálogo de sistema.
[2] O catálogo do sistema é um repositório com função de armazenar as definições dos esquemas dos bancos de dados.
Comentário: É importante lembrar que existe uma hierarquia entre os objetos ou elementos em um dicionário de dados. Um dicionário de dados possui a descrição dos esquemas ou catálogo de sistemas. Cada catálogo deve conter a descrição dos objetos que fazem parte do contexto de um sistema, como tabelas, visões e domínios. Dentro das definições das tabelas temos as descrições dos atributos e restrições de integridades dos dados.
Assim, ao analisar as alternativas acima, podemos inferir que a alternativa
[1] encontra-se incorreta, já a afirmação [2] está certa!
Gabarito: E C.

CARACTERÍSTICAS DA ABoRDAGEM DE BD

Segundo Navathe, são quatro, as principais características da abordagem de banco de dados que a fazem sobressair em relação às abordagens de processamento de arquivo.
Natureza de autodescrição de um sistema de banco de dados
Isolamento entre programas e dados, abstração de dados
Suporte a múltiplas visões de dados

Compartilhamento de dados e processamento de transação multiusuário.

Esses esforços visam reduzir a redundância o que implica em reduzir o desperdício no espaço de armazenamento e os esforços para manter os dados comuns ou duplicados atualizados. Tudo realizado por meio de um único repositório!
Vejam que a lista acima pode ser caracterizada como uma enumeração e, como eu sempre digo,listas fazem parte do rol de questões de prova de concurso. Seja qual for a matéria,
sempre gaste um pouco do seu tempo lendo, mais de uma vez, cada uma das listas pertencentes aos assuntos. Averdade é: não importa o grau de relevância dentro do assunto, um examinador preguiçoso sempre está propício a utilizar deste artifício ao elaborar uma questão.
A primeira característica listada pelo Navathe é conhecida por nós como catálogo do SGBD,dicionário de dados ou metadados. Esta propriedade permite ao SGBD gravar as definições das suas estruturas e restrições. E, quais são as descrições que podem ser gravadas? Descrição de tabelas,tamanho do campo, tipo dos dados, propriedade de ser nulo ou não, valores default,
restrições de integridade, entre outros. Para facilitar sua visualização pense numa definição de uma tabela emSQL1. Veja o exemplo a seguir e observe algumas dessas descrições.

CREATE TABLE EMPREGADO (
ID_EMPREGADO INT PRIMARY KEY,
FK_ID_SUPERVISOR INT,

PRIMEIR0_N0ME VARCHAR2 (100 ) NOT NULL,
ULTIM0_N0ME VARCHAR2 (100) NOT NULL,
EMAIL VARCHAR2(100) NOT NULL,
DATA_NASC_FUNC DATE NOT NULL,
DATA_INICIO_FUN DATE DEFAULT SYSDATE,
DATA_FIM_FUN DATE DEFAULT NULL,

CONSTRAINT FK_SUP FOREIGN KEY EMPREGADO (ID_EMPREGADO)

);

1 SQL é uma linguagem declarativa usada para enviar comandos aos sistemas de gerenciamento de banco de dados.Esses comandos permitem a criação de tabelas e a manipulação dos dados armazenados. Na criação da tabela podemos observar a definição dos tipos de dados (VARCHAR2, DATE, NUMBER), bem como das restrições de integridade (NOT NULL, DEFAULT).
A próxima característica é uma decorrência da anterior. A partir do momento em que temos um dicionário de dados, é possível excluir da estrutura dos programas a definição dos dados presentes nos mesmos. Agora isolados, dados e aplicações, criam um conceito chamado independência de dados do programa. Este só é possível por conta da abstração de dados. A abstração de dados permite a criação de diferentes níveis de modelos. Cada modelo revela a estrutura dos dados de uma forma específica.
O suporte a múltiplas visões parte do princípio de que diferentes usuários têm diferentes necessidades sobre os dados. Se pensarmos em SQL, uma VIEW representa um subconjunto de informações referentes a uma ou mais tabelas (ou até a nenhuma tabela). Do ponto de vista mais abstrato, uma visão é a parte do banco de dados ao qual um usuário ou grupo de usuários tem acesso. Porém, existe a possibilidade dessa visão conter um dado virtual que é derivado das informações armazenadas. Imagine, por exemplo, a idade calculada a partir da data de nascimento.
Quando falamos de suporte a múltiplos usuários queremos, basicamente, permitir que diferentes usuários acessem o banco de dados ao mesmo tempo. Para garantir que isso ocorra é preciso que oSGBD forneça um mecanismo de controle de concorrência. As transações efetuadas devem levar o sistema a um estado válido (C), não ter conhecimento umas das outras (I), serem executadas sempre por completo (ou não serem executadas) (A) e, uma vez gravadas na base, devem persistir ao longo do tempo (D).
Você dever estar se perguntando, o que são essas letras ao lado das características das transações citadas anteriormente? Elas se referem às características de uma transação: atomicidade,consistência, isolamento e durabilidade. Elas formam uma sigla conhecida como ACID e são bastante conhecidas dentro do modelo de dados relacional/transacional.
ESQUEMATIZANDO

Acabamos de tratar das características que o Navathe utiliza para diferenciar sistemas de arquivo dos sistemas de banco de dados. Vamos agora listar as características descritas peloDate e pelo
Silberschatz. Date chama de benefícios da abordagem de banco de dados. Quais sejam:

1. O dado pode ser compartilhado

2. A redundância pode ser reduzida

3. Inconsistências podem ser evitadas

4. Pode-se utilizar o suporte a transações

5. A integridade pode ser mantida

6. A segurança pode ser aperfeiçoada

7. Requisitos conflitantes podem ser balanceados

8. Padrões podem ser utilizados

Já Abraham Silberschatz trata das desvantagens de se utilizar um sistema de arquivo:

1. Redundância e inconsistência dos dados

2. Dificuldade de acesso a dados

3. Isolamento dos dados

4. Problemas de integridade

5. Problemas de atomicidade

6. Anomalias de acesso concorrente

7. Problemas de segurança

Lembrem-se, não precisamos decorar todas essas listas, apenas tomar conhecimento da sua existência, pois fazem parte do contexto. Elas procuram sempre expor as características que diferenciam os sistemas de arquivos dos sistemas de banco de dados.
Vejamos mais algumas questões que tratam do assunto.

HORA DE

PRATICAR!

1. Ano: 2019 - CREA-TO - Analista de Sistemas

No que diz respeito a banco de dados, julgue o item.

Em um banco de dados, é necessária a abstração dos dados, de tal forma que o usuário não se importe com a forma como eles estão armazenados.
Comentário: Quando falamos em abstração dos dados, estamos retirando dos usuários a visão do armazenamento físico e da sua complexidade. A divisão dos discos rígidos em setores e a organização dos arquivos nos SGBDs são abstraídas por meio dos diversos níveis de modelos de dados.
Gabarito: C

2. Ano: 2018 Órgão: TCE-PB Cargo: Auditor de Constas Públicas Questão: 97

A respeito de SGBDs, assinale a opção correta.

A Um SGBD, por definição, não é flexível, dada a dificuldade de mudar a estrutura dos dados quando os requisitos mudam.
B Um SGBD é um software que não prevê as funções de definição, recuperação e alteração de dados, sendo essa tarefa a função básica de um sistema de banco de dados.
C A consistência de dados é o princípio que determina a manutenção de determinado dado em vários arquivos diferentes.
D Conforme o princípio da atomicidade, caso ocorra erro em determinada transação, todo o conjunto a ela relacionado será desfeito até o retorno ao estado inicial, como se a transação nunca tivesse sido executada.
E O controle de concorrência é o princípio que garante e permite a manipulação, no mesmo momento, de um mesmo dado por mais de uma pessoa ou um sistema.
Comentário: Vamos analisar as alternativas acima. Elas são relevantes para consolidar nosso conhecimento sobre o assunto. Começando pela alternativa A, o erro aparece quando o examinador afirmar que os SGBDs não são flexíveis. Lembre-se que um SGBD veio solucionar um problema de replicação dos dados em diversos arquivos distintos. Agora, com uma fonte única dos dados, as alterações dos mesmos são centralizadas.
Já a alternativa B nos remonta as funcionalidades do SGBD. O que podemos fazer com tal sistema? É possível, primariamente, armazenar e manipular dados, para tal, é necessário descrever as estruturas das tabelas. Todos os SGBDs possuem estrutura para construção do banco de dados, usando uma linguagem como SQL. Sendo assim, a alternativa B também está incorreta.
As próximas duas alternativas tratam das propriedades das transações, mais especificamente da consistência, que tem por objetivo levar o banco de dados de um estado válido para outro estado consistente, e da atomicidade, que parte do princípio que uma transação é composta por vários comandos de modificação da base de dados e que estes comandos devem ser executados em conjunto completamente ou não serem executados. Desta forma, para garantir a atomicidade, caso uma transação falhe todas as operações já efetivadas precisam ser desfeitas. Desta forma, a alternativa C está incorreta e a alternativa D é a nossa resposta.
Por fim, o controle de concorrência é um mecanismo que permite que apenas um usuário consiga modificar um dado do sistema em um determinado momento. É importante entender que é possível várias pessoas terem acesso aos dados para leitura. Como se todos estivessem lendo um livro. Contudo, na hora de escrever, só existe uma caneta e, se alguma pessoa estiver de posse da caneta, apenas ela poderá fazer alterações na base.
Gabarito: D.

3. Ano: 2019 - UFPB - Analista de Tecnologia da Informação

Os bancos de dados estão implícitos na vida da sociedade moderna. Assinale a alternativa queNÃO apresenta uma implicação adicional do uso de banco de dados.

A Economias de escalas.

B Disponibilidade de informações atualizadas.
C Desenvolvimento de novos dispositivos.

D Flexibilidade.

E Tempo reduzido para o desenvolvimento de aplicações.

Comentário: Se pensarmos em dispositivos como componente de hardware, percebemos que a utilização de um banco de dados não auxilia no desenvolvimento de um novo dispositivo. As demais alternativas apresentam benefícios da utilização da abordagem de banco de dados.A
economia de escala refere-se a possibilidade expansão da quantidade de usuários do banco a um custo relativamente baixo. As informações centralizadas com redundância controlada permitem a disponibilização atualizadas das mesmas. Quando você pensa no desenvolvimento de um novo sistema, o fato das informações estarem isoladas das aplicações facilita a vida dos desenvolvedores, reduzindo o tempo para construção das aplicações. Reforçando,temos nossa resposta na alternativa C.
Gabarito: C

4. ANO: 2014 ÓRGÃO: TJ-AP PROVA: ANALISTA JUDICIÁRIO - BANCO DE DADOS - DBA

A redundância controlada de dados em um sistema de banco de dados ocorre quando

A um programa está ciente da múltipla representação de uma dada informação e garante o sincronismo entre as diversas representações.
B a responsabilidade pela manutenção do sincronismo entre as múltiplas representações de uma dada informação é compartilhada entre o programa e o usuário.
C os dados mais importantes são duplicados a cada backup do sistema, visando aumentar a garantia da recuperação da informação em caso de problemas.
D a responsabilidade pela manutenção do sincronismo entre as múltiplas representações de uma dada informação é do usuário.
E um programa está ciente da múltipla representação de uma dada informação, mas não garante o sincronismo entre as diversas representações.
Comentário: Nesta questão vamos entender o que está sendo cobrado antes de avaliarmos as alternativas. Em primeiro lugar, precisamos lembrar que o SGBD vai controlar a redundância dentro do banco de dados. Esse controle é feito quando diferentes usuários compartilham a mesma informação.
Suponha uma tabela de endereços de clientes em um banco comercial. Todos os setores do banco podem fazer uso desta informação. A área de investimento pode mandar o extrato das suas aplicações, o setor de cartão de crédito pode enviar sua fatura e o relacionamento com o cliente pode te enviar um cartão de feliz aniversário. A importância deste ponto único de contato é verificada quando a cliente muda de endereço, a atualização da tabela vai ser efetiva para os diferentes usuários da informação.
Agora vamos analisar as alternativas, ao ler cada uma delas, podemos observar que no
SGBD
um programa deve estar ciente da múltipla representação de uma dada informação e garantir o sincronismo entre as diversas representações. Essa descrição é a presentes na alternativa Aque é a nossa resposta.

Gabarito: A.

5. CETREDE - Fiscal Ambiental (Pref ltaitinga)/2019

Antigamente, os bancos de dados eram manuais. Atualmente com a difusão tecnológica a grande maioria dos bancos de dados são digitais. Eles compõem um conjunto estruturado de dados que obedecem a um modelo de dados e são armazenados em formato digital - em um hardware (geralmente, um servidor da rede - storage). NÃO é vantagem de um banco de dados,
a) maior volume de dados armazenado.

b) ocupar maior espaço físico.

c) maior velocidade de acesso aos dados.

d) permite o compartilhamento de informações.

e) persistência dos dados: depois de muitos anos, ainda podem ser acessados.

Comentário: Sabemos que um banco de dados é uma coleção de dados sobre pessoas, coisas,
lugares. Esses dados se relacionam entre si de forma que geram informação, ou seja,
algo que tenha sentido para seus usuários. No passado, os bancos de dados eram manuais. Lembrem-se do exemplo da lista telefônica do Seu Zacarias.

Com o passar do tempo, a tecnologia foi avançando e foram surgindo bancos de dados digitais,que armazenam os dados em máquinas. Hoje em dia, a grande maioria das empresas em geral utilizam um sistema que registra de forma digital as suas operações.
Vamos analisar cada uma das alternativas:

a) ERRADA. Essa é uma vantagem de um banco de dados digital. Ele consegue armazenar um volume muito maior do que os bancos de dados manuais, que utilizavam papéis ou outros meios para armazenar as informações de forma manual.
b) CORRETA. Essa não é uma vantagem dos bancos de dados digitais. Na verdade, eles ocupam um espaço físico menor. Isso ocorre porque a organização dos dados nos arquivos de banco de dados é mais eficiente, e porque a redundância dos dados é reduzida.
c) ERRADA. Essa é uma vantagem dos bancos de dados digitais. Através de linguagens de consulta, o poder de processamento dos computadores permite acessar os dados de forma muito mais rápida que uma busca realizada manualmente.
d) ERRADA. Essa é outra vantagem dos bancos de dados. Com a internet, por exemplo, é possível compartilhar informações com outros usuários em qualquer lugar do mundo por meio de bancos de dados distribuídos.
i e) ERRADA. Mais uma vantagem dos bancos de dados. Um caderno, por exemplo, pode ter suas páginas deterioradas com o tempo ou a tinta da caneta pode apagar. As mídias digitais,entretanto, permitem que a informação esteja acessível por quanto tempo for necessário.Claro que, para isso, devem ser utilizadas técnicas de backup e redundância dos dados.

Desta forma, podemos encontrar a nossa resposta para essa questão na alternativa B.

Gabarito: B.

PERSoNAGEM Do ECoSSISTEMA DE BD

Quando tratamos de grandes organizações, as atividades relacionadas a banco de dados devem ser compartilhadas entre diferentes pessoas. Trataremos agora dos dois principais papéis dentro desse processo: o administrador de banco de dados (DBA) e o administrador de dados (AD).
Só para termos uma ideia, algumas empresas do setor bancário chegam a ter algumas dezenas deADs dentro da organização. O Bradesco tem por volta de 40 ADs. Vamos então começar falando um pouco sobre esse perfil de trabalhador especializado em banco de dados.
O AD é a pessoa que toma as decisões estratégicas e de normas com relação aos dados da empresa.
Os administradores de dados também podem ser conhecidos por projetista de dados. Suas tarefas são realizadas principalmente antes do banco de dados ser realmente implementado e/ou populado.
Eles são responsáveis por identificar os dados a serem armazenados e escolher estruturas apropriadas para representar esses dados. Para isso precisam se comunicar com todos os potenciais usuários a fim de entender suas necessidades e criar um projeto que as atenda suas necessidades.Eles definem então visões para cada grupo de usuários. Podemos listar ainda como atribuições doAD:

* Padronizar os nomes dos objetos criados no BD

* Gerenciar e auxiliar na definição das regras de integridade

* Controlar a existência de informações redundantes

* Trabalhar de forma corporativa nos modelos de dados da organização

Falaremos agora do DBA - Database Administrator, ou, da pessoa que fornece o suporte técnico necessário para implementar as decisões. Assim, o DBA é responsável pelo controle geral do sistema em um nível técnico. Tem como recurso primário o banco de dados e como recursos secundários oSGBD e os softwares relacionados.

O DBA é o responsável por autorizar o acesso ao banco de dados, coordenar e monitorar seu uso,adquirir recursos de software e hardware conforme a necessidade e por resolver problemas tais como falhas de segurança ou demora no tempo de resposta do sistema. Segundo o Date uma lista de atividades associadas ao DBA contém as seguintes tarefas:
* Definir o esquema conceituai1 (às vezes conhecido como lógico)

* Definir o esquema interno

* Contatar com os usuários

* Definir restrições de segurança e integridade

1 Esse esquema conceituai é estabelecido no âmbito da arquitetura em três esquemas.
Veremos que ele não tem relação com o modelo de dados conceituai. Uma outra informação importante é que segundo oCJ Date o Administrador de Dados também pode ser responsável pela criação do modelo conceituai.

* Monitorar o desempenho e responder a requisitos de mudanças.

* Definir normas de descarga e recarga (dumping)2
Vejamos algumas questões rápida sobre o assunto:

x/ HORA DE

« PRATICAR!

1. Ano: 2019 - CRN - 3- Região (SP e MS) - Assistente Técnico

No que se refere aos conceitos gerais de banco de dados, assinale a alternativa correta.

A Os dados, independentes ou não, de um banco de dados formam necessariamente uma informação.
B Os projetistas, também conhecidos como administradores do banco de dados
(database administrators), são os usuários iniciantes ou paramétricos do sistema.
C Um banco de dados não representa um aspecto do mundo real.

D Uma planilha do Microsoft Excel ou uma lista de contatos (nome, telefone e e-mail)
de uma agenda configuram um banco de dados.
E A edição ou a alteração dos dados de um banco de dados é muito onerosa ao administrador,o que torna comum a prática de sua total exclusão.

Comentário: Vamos comentar cada uma das alternativas. (A) Dados e informações são conceitos distintos. A informação precisa de contexto e significado, já o dado é apenas um fato registro (bruto). (B) Os projetistas são conhecidos como administradores de dados. (C)Todo banco de dados deve descrever alguma coisa do mundo real, podendo ser concreto ou abstrato. (D) Falamos sobre isso no início da nossa aula. A lista telefônica do seuZacarias é considerada um banco de dados, mesmo não sendo digital. (E) Fazer alterações no banco de dados nem sempre é onerosa, alguns fatores podem permitir uma alteração rápida do registro.
Gabarito: D

2. Ano: 2018 Órgão: EBSERH Prova: Analista de Tecnologia da Informação

Com relação a banco de dados, julgue o item seguinte.

Após um banco de dados ser criado, o administrador executa uma série de tarefas para dar permissão de acesso aos usuários que necessitam ler e gravar informações na base de dados.A responsabilidade de gerir os acessos ao banco de dados é do sistema gerenciador de banco de dados (SGBD).
2 Carga e recarga ou dumping é uma outra forma de definir backup de banco de dados.

Comentário: Observe que neste texto podemos verificar explicitamente o benefício do sistema de gerenciamento de banco de dados. O administrador de banco de dados vai atribuir aos diversos usuários as permissões compatíveis com suas necessidades. Contudo, quem vai gerenciar o acesso, no sentido de autorizar o usuário a acessar o banco de dados e visualizar os dados, é o próprio SGBD. Desta forma, temos uma alternativa correta.
Gabarito: C.

3. ANO: 2010 ÓRGÃO: TCE-SP PROVA: AGENTE DA FISCALIZAÇÃO FINANCEIRA - PRODUÇÃO E
BANCO DE DADOS

Considerando que os dados constituem um dos bens mais valiosos de uma empresa, é necessário que haja um papel que tenha a responsabilidade central pelos dados,principalmente entendendo as necessidades empresariais nos altos níveis da organização.
Tal papel é mais adequadamente desempenhado pela
A administração de banco de dados.
B administração de dados.

C alta administração da organização.
D análise de sistemas.

E gerência de sistemas.

Comentário: Percebam que a questão trata da padronização dos dados corporativos. Entender a organização e sua relação com as informações de forma a gerenciar os dados de maneira eficiente é reponsabilidade da equipe de administração de dados. Hoje em dia um termo muito utilizado para os dados que permeiam vários setores das empresas ou órgãos públicos é o conceito de dados mestres. Eles são armazenados em um repositório central e distribuídos aos diversos usuários.
Gabarito: B.

Você precisa entender que são dois os principais papeis presentes no trabalho diário de organização e manutenção de banco de dados. O administrador de dados que cuida do contexto estratégico dos dados, sua preocupação está em saber quais os dados serão armazenados em um banco de dados,quem são as pessoas que precisam dos mesmos e ainda, procurar padronizar os nomes dos atributos e outros objetos para que dados redundantes não sejam armazenados.
O outro indivíduo importante neste processo é o administrador de banco de dados. Nessa função encontramos todo o suporte técnico necessário para as atividades diárias de um sistema de banco de dados. O DBA distribui as permissões de acesso aos dados, criar os objetos que vão armazenar os dados, faz ajustes para que eles funcionem de forma adequada.
EVoLUçÃo HISTóRICA DoS SCBDS

É interessante conhecer a evolução dos modelos de dados até os bancos de dados NoSQL.
Afinal,
quando começamos a tratar as informações em sistemas como elas eram armazenadas? Apreocupação com o armazenamento dos dados começa na década de 1960. Até então os computadores funcionavam como grandes calculadoras. Veja a figura abaixo para conhecer um pouco mais sobre os modelos de armazenamento de dados. Perceba que os aspectos semânticos vão sendo aprimorados até os modelos semântico.
*Endereçando problemas de Big Data

* Menos semântica nos modelos de dados

* Baseado em modelos sem esquema e chave valor

* Mais adaptado para armazenamento de uma grandes quantidade de dados esparsos i
Figura 1 - Evolução histórica dos modelos de dados.

Os primeiros sistemas de gerenciamento de banco de dados são implementados no final da década de 1960. Charles Bachmann desenvolveu o primeiro SGBD chamado Integrated Data Store (IDS)
1 * Também vale para o modelo hierárquico.

enquanto trabalhava na Honeywell em 1964. Esse sistema usava o modelo de rede onde as relações de dados são representadas como um grafo bidirecional. A principal vantagem de um modelo de banco de dados em rede é o suporte ao relacionamento muitos-para-muitos. O resultado é um acesso mais rápido aos dados, pesquisa e navegação.
Contudo, o primeiro SGBD que obteve sucesso comercial foi desenvolvido pela
IBM chamado
Information Management System (IMS). Ele usava o modelo hierárquico no qual as relações entre os dados são representadas como uma árvore. Por incrível que pareça, o IMS ainda está em uso hoje no sistema de reservas SABRE da IBM na American Airlines.
A estrutura hierárquica é usada para ordenar fisicamente os registros no armazenamento. É possível acessar os registros navegando para baixo na estrutura de dados usando ponteiros. Vamos tentar a presentar um exemplo para retirar um pouco da abstração do conceito.
A figura abaixo descreve um banco de dados de Estudante, cada estudante pode se matricular em vária disciplinas ... Neste caso, os estudantes têm um relacionamento de 1-N com disciplina ... Ou seja, se diferentes alunos cursarem a mesma disciplina, elas serão cadastradas várias vezes no banco de dados, uma para cada aluno.
Figura 2 - Modelo de banco de dados hierárquico.

Esses dois modelos, em rede e hierárquico, apresentavam problemas sérios, entre eles:

* O acesso ao banco de dados feito através de operações com o ponteiro de baixo nível.
* Detalhes de armazenamento dependiam do tipo de dados a serem armazenados.

* Para adicionar um campo no banco era necessário reescrever o esquema subjacente de acesso/modificação, em outras palavras o modelo de dados físico.
* Ênfase nos registros a serem processados, não na estrutura global.

* O usuário deveria conhecer a estrutura física da BD, para fim de consulta das informações.
Vejamos algumas questões recentes sobre o assunto:

HORA DE

PRATICAR!

1. Analista (Pref Vila Velha)/Desenvolvimento/2020

Uma das estruturas de bancos de dados é a que tem o formato conhecido por "árvore".
Nessas estruturas, cada registro tem apenas um possuidor. Esse modelo é chamado:
a) hierárquico.

b) indexado.

c) block chain.

d) relacional.

e) sequencial.

Comentário: No modelo hierárquico, cada registro é definido como um nó numa estrutura em árvore, onde cada nó-pai pode ter vários filhos, mas cada nó-filho só pode ter um pai. Ou seja,percebemos um relacionamento 1-N.

Esse tipo de banco de dados permite que as referências entre os registros sejam automaticamente construídas por conta das ligações (links) presentes entre eles. Por outro lado, relações complexas são difíceis de se representar no modelo.
Desta forma, temos o gabarito da questão na alternativa A.

Gabarito: A.

2. Ano: 2019 Órgão: MPC-PA - Analista Ministerial - Tecnologia da Informação

Assinale a opção que apresenta o modelo de dados caracterizado por organizar os dados em uma estrutura do tipo árvore, na qual cada registro tem um único "pai" e é classificado em uma ordem específica.
A híbrido
B de rede

C relacional
D hierárquico

E orientado a objetos

Comentário: O modelo hierárquico organiza dados em uma estrutura de árvore, nele cada registro tem um único "pai" ou raiz. Registros "irmãos" são classificados em uma ordem específica. Essa ordem é usada como a ordem física para armazenar o banco de dados.Este modelo é bom para descrever muitas relações do mundo real. Contudo, possui limitações para descrever relacionamentos N-N entre os elementos de dados. Esse modelo foi usado principalmente pelos Sistemas de Gestão de Informações da IBM nos anos 60 e 70, mas são raramente vistos hoje devido a certas ineficiências operacionais.
Curiosidade: O modelo hierárquico foi implementado em um esforço conjunto da IBM e
North
American Rockwell em 1965. A IBM teve o Information Management System IMS (DL/1),
largamente utilizado durante as décadas de 1970 e início da década de 1980

Gabarito: D

3. Administrador de Rede (CM Piracicaba)/2019

Sobre o modelo hierárquico de bancos de dados, é correto afirmar que a) um registro não pode ser pai de mais de um registro filho.
b) um registro pai pode ter relacionamento com, no máximo, 3 registros filhos.

c) um registro do tipo raiz só pode ter relacionamento com um único registro filho.

d) um registro do tipo raiz não participa como registro filho em qualquer relacionamento.

e) o campo de um registro filho admite apenas tipos de dados inteiros.

Comentário: Vamos comentar cada uma das alternativas. (A) Um registro pode ser pai de vários registros, mas cada registro só pode ter um pai. (B) Mais uma vez, um registro pai pode ter relacionamento com vários filhos, não há limitação. (C) O registro raiz é o pai de todos ... logo,ele terá relacionamento com vários filhos. (D) Essa é a nossa resposta!! (E) Campos podem ter outros valores além de inteiros, por exemplo, valores textuais.
Gabarito:

Modelo Relacional

No geral, os primeiros SGBDs eram muito complexos e inflexíveis, o que tornou cada vez mais difícil o trabalho, quando era necessária a adição de novos aplicativos ou a reorganização dos dados. Para resolver esses e outros problemas Edgar (Ted) Codd, conhecido com o pai do modelo relacional,trabalhando no laboratório da IBM em San Jose propôs no artigo "A Relational Model of
Data for
Large Shared Data Banks" a definição do modelo relacional.

Figura 3 - Elementos básicos do modelo relacional

A ideia de Codd era usar conceitos matemáticos da teoria dos conjuntos e da lógica de primeira ordem para definir objetos de dados conhecidos como relações. As relações podem ser vistas como tabelas compostas por linhas. O modelo chamou as linhas de tuplas. As tuplas são constituídas por um conjunto de atributos cada um definido dentro de um conjunto de valores possíveis(domínio).
Perceba que todos os dados são armazenados em uma estrutura predefinida, com tipos de dados e tamanhos bem estabelecidos.
Segundo Codd, o modelo fornece um meio de descrição de dados apresentando apenas a sua estrutura natural - isto é, sem sobreposição de qualquer estrutura adicional para efeitos de representação física dos dados. Perceba a grande sacada de Codd!! Ele construiu um modelo que abstraia a representação física dos dados!! Quando você descreve uma relação, você não se importa com a forma de acesso aos dados quando estes estiverem armazenados.
Essa ideia trouxe uma simplicidade estrutural ao modelo. Assim, ele forneceu uma base para uma linguagem de dados de alto nível que permite obter a independência máxima entre dados e programas com a representação de um lado e a estrutura física da máquina do outro.
Em outras palavras, o modelo relacional teve suas bases estabelecidas na independência de dados e, na forma de acesso aos dados definida por uma linguagem clara e ampla. Em vez de processar um registro de cada vez, um programador pode usar o idioma para especificar operações individuais que seriam realizados em todo o conjunto de dados.
Devido à natureza técnica do artigo e a relativa complicação matemática presente no texto, o significado e proposição do artigo não foram prontamente identificados. Entretanto, Codd levou aIBM a montar um grupo de pesquisa conhecido como System R (Sistema R) para tentar avançar sobre o assunto.
O projeto do Sistema R era criar um sistema de banco de dados relacional o qual eventualmente se tornaria um produto. Os primeiros protótipos foram utilizados por muitas organizações,tais como na Sloan School of Management (renomada escola de negócios norte-americana). Novas versões foram testadas com empresas de aviação para rastreamento de manufaturas em estoque.
Eventualmente, o Sistema R evoluiu para SQL/DS, o qual posteriormente tornou-se o DB2. Alinguagem criada pelo grupo do Sistema R foi a Structured Query Language (SQL) ou linguagem de consulta estruturada. Esta linguagem tornou-se um padrão na indústria para bancos de dados relacionais e, hoje em dia, é um padrão ISO (International Organization forStandardization). A
linguagem SQL era originalmente conhecida como SEQUEL (Structured English QUEry Language).
Depois teve seu nome modificado para SQL por problemas de patentes.

Vejamos uma questão simples sobre bancos de dados relacionais que já conseguimos resolver com essa pequena introdução ao assunto ...
HORA DE

PRATICAR!

4. FAEPESUL - Assistente (CRC SC)/Suporte em lnformática/2019

A definição correta para banco de dados relacionais é:

a) Um sistema que serve para criar uma relação de confiança, para acesso à internet.

b) Um sistema que serve para armazenar arquivos dentro do computador.

c) Um banco de dados que modela os dados de forma que eles sejam percebidos pelo usuário como tabelas.
d) Um banco de dados onde cada informação é armazenada na forma de objetos.

e) Um banco de dados que não possui tabelas.

Comentário: As tabelas ou relações dos bancos de dados relacionais são formadas por linhas ou tuplas, que indicam cada registro da tabela, e colunas ou atributos, que identificam os campos da tabela. Cada atributo possui um domínio associado a ele, ou seja, um conjunto de valores que ele pode assumir. Assim, podemos marcar nossa resposta na alternativa C.
Gabarito: C.

Em meados da década de 80, tornou-se óbvio que existiam várias áreas onde bancos de dados relacionais não eram aplicáveis, por causa dos tipos de dados envolvidos. Estas áreas incluíam medicina, multimídia e física nuclear, todas com necessidades de flexibilidade para definir como os dados seriam representados e acessados.
Este fato levou ao início de pesquisas em bancos de dados orientados a objetos, nos quais os usuários poderiam definir seus próprios métodos de acesso aos dados e como estes seriam representados e acessados. Ao mesmo tempo, linguagens de programação orientadas a objetos(Object Oriented Programming - POO), tais como C++, começaram a surgir na indústria.

No início de 1990, temos a aparição do primeiro Sistema de Gerenciamento de Banco de
Dados
Orientado a Objetos (SGBDOO), através da companhia Objectivity. Isso permitiu que usuários e organizações criassem bancos de dados para armazenar resultados de pesquisas como o CERN(maior laboratório que trabalha com partículas em pesquisas de física nuclear -
europeu) e SLAC
(Centro de Aceleração Nuclear - norte-americano), para mapeamento de rede de provedores de telecomunicações e para armazenar registros médicos de pacientes em hospitais,consultórios e laboratórios.
A evolução nos levou aos SGBDs orientados a objetos, mas a praticidade nos trouxe de volta para o modelo objeto-relacional, pois a grande maioria das empresas continuou utilizando os bancos de dados relacionais. Contudo esse modelo começou a apresentar outra lista de problemas ou desafios:
1. Dados na ordem de dezenas ou centenas de TB (terabytes) - abordagem de cluster é cara.
2. Poder de crescimento elástico horizontal - controle de transação ACID torna inviável com a elasticidade.
3. Fácil distribuição dos dados e/ou processamento - SGBD paralelos são caros.

4. Tipos de dados variados, complexos e/ou semiestruturados - modelo de dados objeto-
relacional não resolve todos os requisitos.

Tivemos então o surgimento de um novo movimento no mercado em busca de uma solução que superasse tais problemas: o movimento NoSQL. Este teve sua origem em junho de 2009,para nomear um encontro promovido por Johan Oskarsson e Eric Evans, que teve como objetivo discutir o surgimento crescente de soluções open source de armazenamento de dados distribuídos não relacionais.
Podemos considerar NoSQL uma nova onda de SGBDs, pois propõe algumas alternativas ao modelo relacional, porém com uma grande diferença histórica: o movimento NoSQL não tem como objetivo invalidar ou promover a total substituição do modelo relacional, e sim o fim do modelo relacional como bala de prata, como a única solução correta ou válida. Inclusive, é importante entender queNoSQL não significa "no SQL" (não ao SQL), mas sim "not only SQL" (não só SQL).

Curiosidade: Ao que tudo indico o termo NoSQL foi criado em 1998 por Cario Strozzi para nomear seu projeto open source, que tinha como objetivo ser uma implementação mais leve de um banco de dados relacional, porém sua principal característica era não expor a interface SQL. Portanto é bem irônico usar o termo NoSQL, criado para nomear um banco de dados relacional, para classificar soluções de armazenamento de dados não relacionais.
Juntamente com NoSQL surge o conceito de Big Data. A definição mais tradicional usa a equação dos cinco Vs. Nela, Big Data = volume + variedade + velocidade + veracidade + valor, de dados. Cada característica desta é associada aos dados armazenados. É possível justificar cada uma delas.Vejamos:

NA

PROVA!

Volume porque além dos dados gerados pelos sistemas transacionais, temos a imensidão de dados gerados pelos objetos na Internet das Coisas, como sensores e câmeras, e os dados gerados nas mídias sociais por meio de PCs, smartphones e tablets.
Variedade porque estamos tratando tanto de dados textuais estruturados como não estruturados como fotos, vídeos, e-mails e tuites.
Velocidade porque os dados são gerados muito rapidamente e os sistemas devem ter capacidade de receberem esses dados. Muitas vezes precisamos responder aos eventos quase que em tempo real, ou seja, estamos falando de geração e tratamento de dados em fluxo massivos.
O ponto de vista da veracidade também deve ser considerado, pois não adianta muita coisa lidar com a combinação "volume + velocidade + variedade" se não houver dados confiáveis. Énecessário que haja processos que garantam a consistência dos dados.
O último V, valor, considera que informação é poder, informação é patrimônio.
A combinação
"volume + velocidade + variedade + veracidade", além de todo e qualquer outro aspecto que caracteriza uma solução de Big Data, se mostrará inviável se o resultado não trouxer benefícios significativos e que compensem o investimento.
O que acontece agora? Diante destas definições, importantes à implementação de
SGBDs que suportem a estratégia definida pelo Big Data podemos sugerir diferentes soluções. Bancos do tipoNoSQL são mais flexíveis, sendo inclusive compatíveis com um grupo de premissas que
"compete"
com as propriedades ACID dos SGBDs tradicionais: a BASE (BAsically Available,
Soft state,
Eventually consistency - Basicamente disponível, estado leve, eventualmente consistente).

Exemplos de bancos de dado NoSQL são o Cassandra, o MongoDB, o HBase, o CouchDB e o Redis.
Mas, quando o assunto é Big Data, apenas um banco de dados do tipo não basta. É
necessário também contar com ferramentas que permitam o tratamento correto do volume de dados.Neste ponto, o Hadoop é, de longe, a principal referência.
O Hadoop é uma plataforma open source desenvolvida especialmente para processamento e análise de grandes volumes de dados, sejam eles estruturados ou não estruturados. Pode-se dizer que o projeto teve início em meados de 2003, quando o Google criou um modelo de programação que distribui o processamento a ser realizado entre vários computadores para ajudar o seu mecanismo de busca a ficar mais rápido e livre das necessidades de servidores poderosos (e caros). Esta tecnologia recebeu o nome de MapReduce.
Vamos ficando por aqui, isso é o que nos interessa para o contexto histórico.
Apresentamos acima uma figura com uma evolução dos modelos de dados ao longo do tempo e logo em seguida um resumo com as principais características de cada tipo de modelos de dados.
TOME

NOTA!

Modelos de dados hierárquicos

*1968 - Primero modelo de dados a ser reconhecido. Usa estruturas de árvores onde cada registro é considerado uma coleção de campos ou atributos. Exemplo: IMS.
i

Modelo de dados relacional

* Década de 1970 - Sucessor dos modelos de dados legados. Baseia-se no conceito de relações, tuplas e atributos. Tem fundamentação na teoria dos conjuntos.
* Década de 1980 - Os SGBDs começam a ser melhorados devido a grande aceitação do mercado.
Network Database Model

---

Modelo de dados em Rede

*1969 - Eliminou o conceito de hierarquia,
permitindo que um mesmo registro estivesse envolvido em várias associações. Ex: IDS.
Modelo Entidade Relacionamento.

* É um modelo conceituai de alto-nível, ou seja, é projetado para ser compreensível aos usuários comuns.
* Formado por um conjunto de objetos chamados de entidades e pelo conjunto dos relacionamentos entre esses objetos.
Modelo Orientado a Objeta '

Hi

Modelos de dados semântico

* Modelos de dados orientado a objetos - são mais adequados para tratamento de objetos complexos e dinâmicos.. Um objeto estará associado a um estado e um comportamento.
* Modelo de dados objeto relacional

Modelo de dados NoSQL.

* Década de 90 - Surgem as primeiras alternativas aos modelos relacionais baseados em documentos, chave-valor e colunar.

* Anos 2000 - As bases de dados NoSQL começam a ser reconhecidas devido ao alto poder de performance e escalabilidade
Figura 4 - Diferentes tipos de modelos de dados.

Vamos agora fazer algumas questões sobre o assunto.

HORA DE

PRATICAR!

5. ANO: 2014 ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - BANCO DE DADOS

Acerca de bancos de dados semiestruturados e bancos de dados NOSQL, julgue os itens subsecutivos.
[86] Bancos de dados NOSQL orientados a documentos são apropriados para o armazenamento de dados semiestruturados.
[87] Para garantir a eficiência das consultas a bancos de dados semiestruturados, é fundamental a adoção de técnica de indexação que leve em consideração, além das informações, as propriedades estruturais dos dados.
[88] Devido à escalabilidade esperada para os bancos de dados NOSQL, a implementação desses bancos utiliza modelos de armazenamento de dados totalmente distintos dos utilizados em sistemas relacionais.
Comentário: Vimos que um dos desafios que os banco de dados NoSQL tenta resolver tem relação com os tipos de dados variados, complexos e/ou semiestruturados. Assim podemos considerar a alternativa 86 como correta.
A questão 87 envolve alguns conceitos interessantes. Começa falando sobre dados semiestruturados, por exemplo, XML ou JSON. Consultas em bancos de dados semiestruturados consideram tanto a estrutura quanto os valores. Outra questão é a criação de índice sobre um conjunto de dados semiestruturados. Para avaliar se um índice deve ou não ser criado é importante usar as informações sobre a estrutura dos dados e os valores armazenados. Neste caso, considerando a necessidade de um espaço maior para armazenamento e do custo de manutenção, a criação do índice deve melhorar a performance para ser de fato implementado. Logo, a assertiva está correta.
A alternativa 88 vai exigir conhecimento sobre os modelos de armazenamento utilizados por bancos de dados NoSQL. Quando tratamos de bases de dados NoSQL podemos classificá-las em quatro diferentes tipos, são eles:
Chave/valor (Key/Value): conhecidos como tabelas de hash distribuídas. Armazenam objetos indexados por chaves, e facilita a busca por esses objetos a partir de suas chaves.
Orientados a Documentos: os documentos dos bancos são coleções de atributos e valores onde um atributo pode ser multivalorado. Em geral, os bancos de dados orientados a documento não possuem esquema, ou seja, os documentos armazenados não precisam possuir uma estrutura em comum. Essa característica faz deles boas opções para o armazenamento de dados semiestruturados.
Colunar: Bancos relacionais normalmente guardam os registros das tabelas contiguamente no disco. Ou seja, um registro ou tupla seguida da outra. Por exemplo, caso se queira guardar id,nome e endereço de usuários em um banco de dados relacional, os registros seriam:

Idl, Nomel, Endereçol;
Id2, Nome2, Endereço2.

Essa estrutura torna a escrita muito rápida, pois todos os dados de um registro são colocados no disco com uma única escrita no banco. Também é eficiente caso se queira ler registros inteiros. Mas para situações em que se quer ler algumas poucas colunas de muitos registros(conhecido como família de colunas), essa estrutura relacional (organizada em forma de tabelas) é pouco eficiente, pois muitos blocos do disco terão de ser lidos.
Para esses casos em que se quer otimizar a leitura de dados estruturados verticalmente,bancos de dados de famílias de colunas são mais interessantes, pois eles guardam os dados contiguamente por coluna.
O exemplo anterior em um banco de dados dessa categoria ficaria:
Idl, Id2; Nomel, Nome2; Endereçol, Endereço2.

Os bancos de dados de famílias de colunas são mais interessantes para processamento analítico online (OLAP). BigTable é uma implementação da Google dessa categoria de bancos de dados.
Orientado a Grafos: diferente de outros bancos de dados NoSQL, esse está diretamente relacionado a um modelo de dados estabelecido, o modelo de grafos. A ideia desse modelo é representar os dados e/ou o esquema dos dados como grafos dirigidos, ou como estruturas que generalizem a noção de grafos. O modelo de grafos é aplicável quando "informações sobre a interconectividade ou a topologia dos dados são mais importantes, ou tão importante quanto os dados propriamente ditos". Possui três componentes básicos: os nós (são os vértices do grafo), os relacionamentos (são as arestas) e as propriedades (ou atributos)dos nós e relacionamentos.
Agora vamos voltar a questão, precisamos responder a seguinte pergunta: nenhum dos modelos acima tem relação com bancos de dados relacionais? Ou ainda, não é possível criar estruturas em SGBDs relacionais que representem esses conceitos?
Embora NoSQL apresentes diferentes sistemas de armazenamento que vieram para suprir necessidades em demandas onde os bancos de dados tradicionais (relacionais) são ineficazes.Muitas dessas bases tradicionais apresentam características muito interessantes como alta performance, escalabilidade, replicação, suporte à dados estruturados e sub colunas. Essas características são utilizadas pelas bases de dados NoSQL.
Para finalizar vamos fazer apenas um comentário sobre escalabilidade: A escalabilidade em um banco de dados relacional pode ocorrer de duas formas: horizontal e vertical.A forma horizontal ocorre pela utilização de mais equipamentos e particiona a estrutura de dados de acordo com critérios estabelecidos. A forma vertical ocorre pelo aumento da capacidade do equipamento em que o sistema gerenciador de banco de dados está instalado. Bases de dadosNoSQL têm como um de seus motivadores o baixo custo para realizar uma escalabilidade horizontal, o que torna possível o uso de equipamentos mais acessíveis. Além disso,proporciona um modelo de particionamento nativo (Sharding).

Gabarito: C C E.

6. ANO: 2017 ÓRGÃO: TST PROVA: TÉCNICO JUDICIÁRIO - PROGRAMAÇÃO

[57] Considere que um determinado tipo de banco de dados organiza os dados na forma de uma pirâmide, onde o registro principal no topo da pirâmide é chamado registro raiz. Os registros são organizados como pai e filho onde um registro filho sempre tem apenas um registro pai ao qual ele está ligado, como em uma árvore familiar normal. Em contrapartida,um registro pai pode ter mais de um registro filho a ele ligado.

Trata-se do Banco de Dados a) hierárquico.
b) relacional.

c) orientado a objeto.

d) objeto-relacional.

e) de rede.

sold

Figura 5 - Um exemplo de um modelo de dados hierárquico.

Já o modelo de dados de rede representa dados usando o link entre os registros. O
registro pai é chamado de Registro Proprietário, e o registro filho é chamada de Registro deMembro.
Se os registros Proprietário e Membro estiverem relacionados com o relacionamento muitos-
para-muitos, eles estão conectados através do registro do conector que é conhecido como
Set.
Agora vejamos um modelo semelhante ao visto acima, agora com as características do modelo em rede:
Figura 6 - Um modelo de dados em rede.

Temos ainda o conceito de modelo relacional foi dado por E. F. Codd, em 1970, em seu documento histórico sobre o modelo de dados relacionais. No modelo relacional, os dados são representados em uma forma tabular denominada, relação (tabela), e estão associados a relacionamentos. Portanto, o nome desse modelo é o modelo de dados relacional. Cada entidade é convertida em relação e a associação é tratada através de chaves primárias e estrangeiras. Cada ocorrência da entidade é conhecida como tupla (registro) e a característica de uma entidade é chamada de atributo (coluna). É muito fácil representar a relação muitos-para-muitos usando o modelo de dados relacionais. O modelo relacional é amplamente utilizado em todo o mundo, hoje em dia, para armazenar dados. Vejamos agora um exemplo de um banco de dados relacional de uma livraria on-line.
BOOK

ISBN Book title Category Price Copyrigjit date Year
Page cmint P ID
001-354-921-1 Ransack Novel 22 2005 2006
200 POOl

001-987-760-9 c+- Textbook 25 2004 2005
800 POOl

PUBLISHER

PJD Pname Address State Phone EmailJD

POOl

Hills
Publications

12, Park street,
Atlaiita

Geórgia

71340

H_pub@hi 1 ls-c ora

REV1EW

RJ D ISBN Ratmg
A002 001-987-760-9 6.0

A006 001-354-921-1 7.5

A008 001-987-760-9 7.2

Figura 7 - Um exemplo de banco de dados relacional.

Gabarito: A

CLASSIFICAçÃo DoS SCBDS

Depois de estudar a evolução dos modelos de dados, podemos agora entender as diversas classificações dos SGBDs. A primeira classificação que devemos saber é quanto ao modelo de dados.Desta forma temos os seguintes tipos:

EXEMPLIFICANDO

TIPo EXEMPLo
OBSERVAçÃo
HIERÁRQUICo IMS (IBM), SYSTEM 2K, TDMS

EM REDE
RELACIoNAL

ORIENTADo A
oBJEToS

ORIENTADo A

DOCUMENTOS

CoLUNAR
CHAVE-VALoR

ORIENTADo A
GRAFoS

IDMs, DMS1100, IMAGE, VAX-

SCBDESUPRA

SQL SERVER, DB2, ORACLE,
PoSTGRES, MYSQL, SQLITE,
MICRoSoFT ACCESS

VERSANT, OBJECT SToRE, DB4o,
MATISSE.

MoNCoDB, CoUCHDB,

COUCHBASE

HBASE, ACCUMULo

REDIS, CASSANDRA, DYNAMoDB,
MEMCHACHE

NEo4J, JANUSGRAPH, DGRAPH,
GIRAPH, TICERGRAPH

SISTEMAS DE BANCoS DE

DADOS LEGADOS

NoSQL

Uma informação importante é que vários desses SGBDs pode se encaixar em mais de um tipo de modelo de dados. Uma lista completa por tipo de banco de dados pode ser vista no site: https://db-engines.com/en/ranking. Esse site apresenta uma lista atualizada dos bancos de dados mais utilizados no mercado.
Outro critério usado para classificar SGBDs é o número de usuários suportados pelo sistema.Sistemas monousuário admitem apenas um usuário de cada vez, e são usados principalmente comPCs. Sistemas multiusuário, que incluem a maioria dos SGBDs, admitem múltiplos usuários simultaneamente.
O terceiro critério é o número de locais sobre os quais o banco de dados está distribuído. Um SGBD
é centralizado se os dados estiverem armazenados em um único computador. Um
SGBD
centralizado pode atender a vários usuários, mas o SGBD e o banco de dados residem integralmente em um único computador. Um SGBD distribuído (SGBDD) pode ter o banco de dados real e o software de SGBD distribuídos por vários locais, conectados por uma rede de computadores.
Os SGBDDs homogêneos usam o mesmo software de SGBD em todos os locais, ao passo que SGBDDs heterogêneos podem usar um software de SGBD diferente em cada local.
Um outro critério de classificação é quanto ao custo para aquisição do produto. Temos os SGBDs livre, ou de código aberto, e os SGBDs pagos ou de código fechado.
Resumindo temos que o SGBD pode ser:

MONOUSUÁRIO
CENTRALIZADO
HOMOGÊNEO
PAGO

OU MULTIUSUÁRIOS
ou DISTRÍBUIDO
ou HETEROGÊNEO
ou GRATUÍTO

MoDELo DE DADoS E ARQUITETURA EM TRÊS ESQUEMAS

INSTÂNCIAS X ESQUEMAS

Antes de adentrar no estudo dos modelos de dados queria que você entendesse a diferença entre esquema e instância. O esquema é a definição da estrutura do modelo e a instância se refere aos dados armazenados em um esquema em um momento do tempo.
Para descrever os modelos utilizamos os elementos fornecidos por cada um deles e construímos esquemas. Conhecido com o projeto geral do banco de dados, o esquema é basicamente a descrição do banco, conhecido também como a intenção ou conotação. Baseado nesse esquema é possível criar uma instância do BD. Essa coleção de dados armazenados no banco de dados em um determinado instante é o próprio banco de dados, também denominada de extensão.
Esquema Instância

- Projeto de banco de dados

- Intenção

- Conotação

- Descrição

- Fotografia (snapshot)

- Extensão

| | Estado

- Ocorrências

Quando trata de uma instância de banco de dados, o Date faz uma distinção interessante sobre os valores que estão armazenados. Ele divide os dados armazenados em campo, registro e arquivo. Afigura abaixo nos ajuda a consolidar essa ideia:

Banco de dados armazenado

Outros arquivos armazenados
Arquivo armazenado de "peças n?da nome corda peso da peça da peça peça peça
Duas ocorrências

P1 Porca Vermelho

\ \ u

12.0

do tipo de registrow Ocorrências de campos armazenados armazenado "peça'
I

HW

P2 Pino | Verde | 17.0

n? da nome cor da peso da peça da peça peça peça
Figura 1 - Campo, registro e arguivos armazenados

Um campo é a menor unidade de dados armazenado, veja na figura os diversos atributos de peças,cada um possui um valor específico. Já um registro pode ser visto como uma coleção de campos armazenados e relacionados entre si. Cada ocorrência de peça representa um registro.Por fim, um arquivo armazenado é o conjunto de todas as ocorrências de um único tipo de registro.
Esse assunto já foi cobrado em provas anteriores ... vejamos:

HORA DE

PRATICAR!

1. Ano: 2019 Prefeitura de São Roque do Canaã - ES - Técnico em Processamento de Dados

A coleção de informações armazenadas de um banco de dados é chamada de:
A Parâmetros.

B Instância.
C Esquema.
D Arquitetura.

E Projeto.

Comentário: Perceba que a coleção de informações de um banco de dados em um considerada uma instância, fotografia, extensão, estado ou ocorrências. Assim temos a nossa resposta na alternativa B.
Gabarito: B

MoDELo DE DADoS

Um modelo de dados fornece um significado necessário para permitir a abstração dos dados,ocultando detalhes de armazenamento. Pode ser visto como uma coleção de conceitos que são usados para descrever a estrutura de um banco de dados. Cada modelo deve definir uma coleção de ferramentas conceituais para as seguintes tarefas:
(1) descrição de dados

(2) relacionamentos entre eles

(3) a semântica dos dados

(4) restrições de consistência.

Boa parte dos modelos também dá suporte a operações, algumas dessas operações podem representar o aspecto dinâmico ou comportamento de uma aplicação de banco de dados.
Os modelos de dados podem ser divididos em três categorias de acordo com os tipos de conceitos usados para descrever a estrutura do banco de dados. No nível mais alto temos os modelos de dados conceituais que apresentam os dados da forma como os usuários finais percebem. Em um nível intermediário está a classe de modelos de dados lógicos ou representacionais que fornece um entendimento aos envolvidos no processo de desenvolvimento do BD, mas já introduz informações sobre a forma pela qual os dados são armazenados dentro de um computador. Oúltimo nível apresenta os modelos de dados físicos ou de baixo nível. Observem na figura a seguir:
Figura 1 - Categorias de modelos de dados.

Antes de continuarmos gostaria de apresentar para você uma figura que mostra a existência de uma evolução ou um refinamento nos modelos de dados. Esse refinamento reduz o nível de abstração permitindo a implementação da estrutura de dados no disco rígido ou em outro dispositivo físico. Opasso a passo do projeto de banco de dados será visto em outro momento neste curso.

Modelo Lógico

S Leva em conta algumas limitações e implementa recursos como adequação de padrão e nomenclatura, define as chaves primárias e estrangeiras,normalização, integridade referencial, entre outras.
S Define-se o tipo de SGBD (Ex.:
Relacional)

Nível de abstração cresce de baixo para cima! Quanto mais abstrato, menos complexidade
Modelo Conceituai.

Mais alto nível

Usado para envolver o cliente, foco em aspectos do negócio e não da tecnologia.
São mais fáceis de compreender
Não temos a definiçãodo SGBD
Diagrama de Entidade e
Relacionamento

Modelo Físico.

Leva-se em conta as limitações impostas pelo SGBD escolhido.Nível mais baixo de abstração,
Descreve o modo como os dados são salvos em meios de armazenamentos
Figura 2 - Resumo sobre os modelos de dados.

Após conhecermos a divisão de modelo de dados, vamos mudar nosso foco para outra classificação presente no contexto de banco de dados. Silberschatz apresenta um conceito de níveis de abstração.O nível de abstração mais baixo ou físico descreve como os dados realmente são armazenados. Este nível descreve em detalhes estruturas de dados complexas.
O próximo nível de abstração descreve que dados estão armazenados no banco de dados e que relações existem entre eles. O nível lógico descreve o banco de dados inteiro em termos de um pequeno número de estruturas relativamente simples. Embora a implementação das estruturas simples no nível lógico possa envolver estruturas complexas em nível físico, o usuário do nível lógico não precisa tomar ciência desta complexidade.
O nível de abstração mais alto descreve apenas parte do banco de dados. Muitos usuários de sistema de banco de dos não precisam de todas as informações armazenadas. Em vez disso, eles precisam apenas de uma parte do banco de dados. O nível de visão (v/ei/i/) existe para simplificar sua interação com o sistema, que pode fornecer muitas visões para o mesmo banco de dados.
A hierarquia de níveis de abstração de dados pode ser vista na figura abaixo:

Figura 3 - Os 3 níveis de abstração: Visão, lógico e físico.

ARQUITETURA TRÊS ESQUEMAS

O American National Standards Institute (ANSI) através do Standards Planning and
Requirements
Committee (SPARC) estabeleceu um padrão para o desenvolvimento de tecnologias de base de dados, definindo uma arquitetura de três níveis independentes: interno, conceituai e externo.
Essa arquitetura tem por objetivo separar o usuário da aplicação do banco de dados físico. Possuem,logicamente, os esquemas definidos em três níveis distintos. Vamos definir cada um deles e em seguida apresentar uma figura que servirá de base para uma explicação mais detalhada.
WST( MAIS

ATENÇAO! (*) Nível interno - (também conhecido como nível de armazenamento) é o mais próximo do meio de armazenamento físico - ou seja, é aquele que se ocupa do modo como os dados são fisicamente armazenados dentro do sistema.
(*) Nível conceituai - (também conhecido como nível lógico de comunidade, ou às vezes apenas nível lógico, sem qualificação) é um nível "indireto" entre os outros dois.
(*) Nível externo ou visão - (também conhecido como nível lógico do usuário) é o mais próximo dos usuários - ou seja, é aquele que se ocupa do modo como os dados são vistos por usuários individuais.
Usuário A1 Usuário A2 Usuário B1 Usuário B2 Usuário B3

* Interface com o usuário

Figura 1 - Arquitetura detalhada do sistema

Olhando para a figura anterior percebemos que diferentes grupos de usuários acessam visões externas distintas. A figura mostra dois grupos de usuários A e B acessando suas respectivas visões externa por meio de uma sublinguagem de dados (DSL). Toda DSL é dividida em pelo menos duas sublinguagens: uma linguagem de definição de dados (DDL) que dar suporte à criação de objetos no banco de dados; e a linguagem de manipulação de dado (DML) que permite o processamento ou manipulação dos objetos.
O nível externo é o nível de usuário individuais. Uma visão externa representa o conteúdo visto por um determinado usuário. Pense que para esse usuário o banco de dados é composto apenas pela parte que ele enxerga (sabe nada inocente!:)). Muitas vezes, um usuário tem acesso a apenas alguns atributos de uma tabela ou arquivo. Essa composição de atributos que não compreende a totalidade das colunas é conhecida como registro externo. Cada visão externa é definida como um esquema externo e descrita por meio de uma DDL externa.
A visão conceituai representa todo o conteúdo do banco de dados também em um nível de abstração razoável quando compara do o nível interno. A visão conceituai consiste em várias ocorrências de cada um dos tipos de registros conceituais. Um esquema conceituai é usado para descrever cada um dos registros para tal usa uma linguagem de definição conhecida comoDDL
conceituai.

A visão interna é uma representação de baixo nível do banco de dados inteiro. Ela é formada por várias ocorrências dos registros internos1. No nível interno deverá haver referência a representações de campos armazenados, sequências de registros armazenados, índices,esquemas de hashing, ponteiros ou outros detalhes de armazenamento e acesso. Para tal, vamos usar um esquema interno usando uma DDL interna.
Veja na tabela abaixo que, embora os termos nível, registros, esquemas e DDL
apareceram várias vezes na explicação acima, eles seguem a lógica do "Jícada um no seu quadradojí".
Nível Registros Esquemas
DDL
Externo Externo Externo
Externo
Conceituai Conceituai Conceituai
Conceituai
Interno Interno Interno
Interno

Neste momento vamos falar dos mapeamentos externo/conceitual e conceitual/interno eles são a chave para a independência de dados que veremos a seguir. Observe que os três esquemas representam descrições dos dados. Se cada um dos níveis usar sua própria linguagem para descrição e manipulação dos dados, é necessário fazer um mapeamento entre esses níveis.
Uma consulta feita por um usuário no nível externo precisará ser convertida em uma linguagem aceita pelo nível conceituai. A mesma lógica vale para os processos de transformação de requisições e os resultados obtidos entre os níveis conceituai e interno. Segundo o CJ Date:
1 Registro interno é o termo ANSI/SPARC que representa a construção que temos chamado de registro armazenado
O mapeamento conceitual/interno define a correspondência entre a visão conceituai e interno, ele especifica o modo como os registros e campos conceituais são representados no nível interno.
Um mapeamento externo/conceitual define a correspondência entre uma visão externa específica e a visão conceituai.
É possível ainda criar um mapeamento externo/externo quando criamos um esquema externo a partir de outro.
Falta falar sobre um último tópico desta seção ... a independência dos dados que nada mais é do que a capacidade de alterar o esquema em um nível dos sistemas de banco de dados sem alterar o esquema no nível mais alto ou, em outras palavras a habilidade de modificar a definição de um esquema em um nível sem afetar a definição do esquema em um nível mais alto.
Segundo Navathe é possível definir dois tipos de independência de dados:

fKHM

ATENTO!

1. Independência lógica de dados - a capacidade de alterar o esquema conceituai sem ter de alterar os esquemas externos ou os aplicativos.
2. Independência física de dados - a capacidade de alterar o esquema interno sem ter de alterar o esquema conceituai.
Se a estrutura do banco de dados armazenado for alterada - isto é, se for efetuada uma mudança na definição do banco de dados armazenado - o mapeamento conceitual/interno terá de ser alterado de acordo, a fim de que o esquema conceituai possa permanecer invariável. Em outras palavras, os efeitos dessas mudanças devem ser isolados abaixo do nível conceituai, a fim de preservar a independência de dados física.
Apresentamos a seguir uma figura que descreve os níveis da arquitetura em três esquemas.Observem que pela definição de independência de dados é necessário a existência de um nível superior ao esquema alterado. Desta forma só temos o conceito para os níveis conceituai e interno da figura.
Usuários finais

Nível externo

Visão externa
Visão externa armazenado
Figura 2 - Níveis da arquitetura em 3 esquemas.

De uma forma simples, cada um dos níveis possui uma função dentro das suas respectivas abstrações. O nível de visão do usuário determina a parte em que o usuário tem acesso. O nível conceituai identifica os dados armazenados e suas relações. Por fim, o nível interno é o nível mais baixo de abstração, define a maneira como os dados estão armazenados. Vejamos mais algumas questões sobre o assunto:
HORA DE

PRATICAR!

1. SUGEP - Técnico (UFRPEJ/Tecnologia da lnformação/Sistemas/2019

O padrão de ANSI/SPARC para arquitetura de SGBD define uma arquitetura em três níveis.
São eles:
a) nível interno, nível de usuário e nível físico.

b) nível interno, nível externo e nível conceituai.

c) nível externo, nível de tabelas e nível físico.

d) nível conceituai, nível de usuário e nível de arquivos.

e) nível de tabelas, nível de arquivos e nível de visão.

Comentário: Acabamos de falar da arquitetura em três esquemas ANSI/SPARC que tem como objetivo separar a aplicação do banco de dados físico. Nessa arquitetura, temos uma divisão dos esquemas em três níveis:
i Interno: nesse nível está o esquema interno do banco de dados. Esse esquema contém a descrição da estrutura física, ou seja, informações detalhadas sobre como os dados são armazenados no hardware, definições das estruturas, índices, caminhos de acesso.
Conceituai: nesse nível está o esquema conceituai, onde é descrita a estrutura do banco de dados para uma comunidade de usuários. Esse esquema não traz detalhes físicos, o foco é descrever quais dados do banco são armazenados, como eles se relacionam e as restrições existentes.
Externo: nesse nível existem uma série de esquemas externos ou visões do usuário. Cada uma dessas visões descreve uma parte do banco que interessa a um determinado usuário (ou grupo de usuários), ocultando todo o restante dos dados.
Assim, temos nossa resposta na alternativa B.

Gabarito: B

2. Ano: 2016 Órgão: TRE-PI Prova: Analista Judiciário - Análise de Sistemas

A respeito das características de um SGBD e das atividades de administração de banco de dados, assinale a opção correta.
a) Para fins práticos, é necessário distinguir diferentes cardinalidades máximas, que podem ser maiores ou iguais a zero.
b) A característica autodescritiva de um banco de dados define que o banco de dados contém o próprio dado assim como uma descrição desses dados e suas restrições. Essas descrições e restrições estão armazenadas no catálogo (dicionário) do SGBD.
c) A independência física de dados consiste na habilidade de modificar o esquema conceituai sem a necessidade de reescrever os programas aplicativos. As modificações no nível conceituai são necessárias quando a estrutura lógica do banco de dados é alterada.
d) Na linguagem SQL, os comandos DDL GRANT e ROLLBACK permitem a implementação de um controle de acesso discricionário, criando e retirando permissões no banco de dados.
e) A coleção das informações armazenadas em um banco de dados, em determinado momento, corresponde ao esquema do banco de dados.
Comentário: Observe que a descrição presente na alternativa B está perfeitamente adequada.Tente encontrar os erros das demais alternativas. Apenas por curiosidade, na alternativa
D, a linguagem SQL possui algumas subdivisões dos comandos. Os comandos GRANT e REVOKEserver para implementação do controle de acesso discricionário. O ROLLBACK, juntamente com o COMMIT e SAVEPOINT servem para controle de transações.
Outro ponto importante, é que, na alternativa A, a cardinalidade máxima tem que ser obrigatoriamente maior ou igual a 1. A justificativa para isso será dada na próxima aula.
Gabarito: B.

3. Ano: 2014 Órgão: TJ-CE Prova: Analista Judiciário - Ciências Computação

Considerando o sistema gerenciador de banco de dados (SGBD), assinale a opção correta acerca de bancos de dados.
a) Enquanto a DDL (Data Definition Language) é utilizada para definir a estrutura do banco de dados, a SDL (Storage Definition Language) é utilizada para especificar o esquema conceituai e seus mapeamentos com o esquema interno.
b) A informação armazenada no catálogo do SGBD é denominada metamodelo.

c) Na independência de dados do programa, propriedade do SGBD, a estrutura dos arquivos de dados é armazenada no catálogo separadamente dos programas de acesso.
d) Na arquitetura de três esquemas de um banco de dados, o nível conceituai é responsável por descrever de forma detalhada as estruturas de armazenamento físico,incluindo os relacionamentos entre as tabelas.
e) Na arquitetura de três esquemas, a capacidade de alterar o esquema interno sem ter de alterar o esquema conceituai consiste na independência lógica de dados.
Comentário: Nesta questão, tão importante quanto saber que a alternativa C está correta, e esse assunto nós já vimos no início da aula, é entender porque as outras estão erradas. Perceba primeiramente que, se formos teoricamente precisos deveríamos trocas SGBD porSDB.
(lembra?!, SGBD + DB = SBD) A questão é que alguns autores falam da abordagem de sistemas de gerenciamento de banco de dados. Assim, essa acaba sendo a menos errada das alternativas.
Na alternativa A, o examinador sugere que SDL, é utilizada para descrever um esquema conceituai. Vejam que SDL está relacionada com armazenamento, e, quando existe de forma separada em uma linguagem, é utilizada para definir os detalhes do nível interno.
Na alternativa B, no lugar de meta modelo, o correto seria metadados.
Na alternativa D, o nível descrito é o nível interno.

Por fim, a alternativa E trata de independência física e não lógica como descrito no texto.

Gabarito: C.

4. Ano: 2016 Órgão: TCE-PA Prova: Auditor de Controle Externo - Área Informática - Analista de
Sistema

Julgue o item subsequente, no que se refere a sistemas de gerenciamento de bancos de dados
(SGBD).

Independência lógica de dados refere-se à capacidade de alterar o esquema conceituai sem a necessidade de alterar os esquemas externos ou os programas de aplicação.
Comentário: Lembre-se que a independência lógica ou conceituai atual no nível intermediário da arquitetura em 3 esquemas. Ela está relacionada ao fato de que modificações nesta camada da arquitetura não gera necessidade de alteração nos esquemas externos ou programas de aplicação. Desta forma, a alternativa encontra-se correta.
Gabarito: C.

5. Ano: 2016 Órgão: TCE-PA Prova: Auditor de Controle Externo - Área Informática -
Administrador de Banco de Dados

Com relação a sistemas gerenciadores de bancos de dados (SGBD), julgue o próximo item.

No nível conceituai da arquitetura de três camadas de banco de dados, cada esquema externo descreve a parte do banco que interessa a determinado grupo de usuários e oculta desse grupo o restante do banco de dados.
Comentário: Perceba que essa questão apresenta uma casca de banana das mais malvadas.
Ele mistura o nível conceituai da arquitetura em três esquemas com o nível externo.
Sabemos que os esquemas externos estão associados as diferentes visões dos grupos de usuários.Tal fato reflete os interesses distintos de cada grupo quanto ao acesso as informações do banco de dados. Assim, podemos marcar nosso gabarito como errado.
Gabarito: E.

6. ANO: 2010 ÓRGÃO: TCE-SP PROVA: AGENTE DA FISCALIZAÇÃO FINANCEIRA - CONHECIMENTOS
BÁSICOS

As três visões da arquitetura básica de um SGBD, pela ordem, desde a mais próxima do usuário até a mais distante, são:
A externa, conceituai e interna.
B externa, interna e conceituai.
C conceituai, interna e externa.
D conceituai, externa e interna.
E interna, conceituai e externa.

Comentário. Ao analisar as alternativas temos que ter em mente duas informações relevantes de enunciados. Primeiro é solicitado as três visões da arquitetura, desta forma podemos concluir que o examinador está se referindo a arquitetura em três esquemas.A outra informação é que a questão pede para você colocar em ordem crescente, da mais próxima do usuário até a mais distante. Com essas duas informações podemos relembrar dos conceitos vistos anteriormente e descrever a seguinte ordem: externa, conceituai e interna.
Gabarito: A.

AMBIENTE Do SISTEMA DE BANCo DE DADoS

A figura a seguir apresenta, de forma simplificada, os componentes típicos de um SGBD.
Perceba que temos uma divisão em duas partes. A parte superior mostra os usuários e a forma de interação deles com o SGBD. Cada tipo de usuário possui a sua interface de relacionamento.
A parte inferior ilustra os detalhes internos do SGBD, eles são responsáveis pelo armazenamento dos dados e processamento das transações dos usuários. Vejam que o banco de dados e o catálogo do SGBD estão representados por um cilindro, representando o fato de serem armazenados permanentemente. Os discos rígidos representam uma das diversas possibilidades de armazenamento não volátil ou permanente dos dados.
Usuários: DBAs Usuários casuais
Programadores Usuários

Figura 1 - Ambiente do sistema de banco de dados.

Nas próximas linhas vou descrever um pouco dos componentes da figura acima. Os conceitos podem ser úteis para que você entenda um pouco da "caixa preta" por trás de um SGBD.
O acesso aos discos rígidos é controlado pelo sistema operacional ou pelo próprio
SGBD. O controle vai escalonar as operações de leitura e escrita sobre o disco. Quando consideramos a execução de uma transação sobre o banco de dados, o intervalo de tempo gasto na transferência de dados entre a memória e o disco é considerado um gargalo no processamento. Para otimizar o processo alguns
SGBDs podem contar com um módulo de gerenciamento de buffer que planeja a troca de dados entre a memória principal e o disco.
Outro módulo, o gerenciador de dados armazenados, controla o acesso às informações do
SGBD
que estão armazenadas, seja no catálogo de dados ou no bando de dados. Ele utiliza os serviços básicos do sistema operacional para executar operações de entrada/saída (leitura/escrita)de baixo nível entre o disco e a memória principal.
Observa-se, na parte superior da figura, as interfaces para os diferentes usuários do sistema. De um lado temos os usuários casuais que trabalham com interfaces interativas para formular consultas.Logo em seguida, visualizamos os programadores de aplicação que usam uma linguagem de programação hospedeira para ter acesso aos dados. Por fim, temos os usuários paramétricos que inserem valores para os parâmetros predefinidos pelas transações.
No parágrafo anterior, falamos apenas das manipulações de dados que podem ser feitas sobre as bases de dados. Essas operações incluem consultas, inserções, deleções e atualizações das informações armazenadas. Contudo, é necessário, antes de manipularmos os dados, construir as estruturas do banco de dados. A linguagem de definição de dados ou data definition language é utilizada pelo DBA para descrever os objetos presentes na base de dados. Uma tabela do modelo relacional é um exemplo de objeto que podemos criar por meio de uma instrução DDL em nossa base de dados.
Quando o DBA digita uma instrução ou comando DDL, essa é enviada ao compilador DDL.
Um compilador transforma o código fonte (da linguagem de programação) em um código em que o computador entenda. O compilador da DDL processa as definições de esquema especificadas e armazena as descrições de esquema (metadados) no catálogo do SGBD. Esse fluxo pode ser observado no lado esquerdo da figura anterior.
Outra função do DBA é o ajuste fino ou tuning do sistema de gerenciamento de banco de dados,bem como a configuração de parâmetros que são feitos por meio dos comandos privilegiados.Apenas para exemplificar, um comando presente na maioria dos SGBDs é o REORG, serve para reorganizar uma tabela ou índice na estrutura física do banco de dados.
Os usuários casuais interagem usando alguma interface de consulta interativa. Essas consultas são analisadas e validadas pela exatidão da sintaxe da consulta, os nomes de arquivos e elementos de dados, e assim por diante, por um compilador de consulta. Essa consulta interna está sujeita a melhorias feitas pelo otimizador de consultas, que se preocupa com o rearranjo e a possível reordenação de operações, com a eliminação de redundâncias e uso dos algoritmos e índices corretos durante a execução.
Ele consulta o catálogo do sistema em busca de informações estatísticas e outras informações físicas sobre os dados armazenados, gerando um código executável. Este por sua vez realiza as operações necessárias para a consulta e faz chamadas ao processador em tempo de execução (falaremos mais sobre ele logo mais).
Os programadores de aplicação escrevem programas em linguagens hospedeiras, como Java e
C#,
que são submetidas a um pré-compilador. Este extrai os comandos DML do programa de aplicação.Para entender melhor como funciona essa divisão vamos partir para um exemplo prático. No exemplo abaixo temos um código Java com um comando SQL. O comentário (//) no código delimita o início da instrução SQL dentro do código Java.
public boolean verificarUsuario(String login, String senha){
String sql = "";

Connection conn = conectarBD();

//INSTRUÇÃO SQL

sql += "select nome from usuários sql +="where login =» + »'" + login +sql += " and senha = " + »"»* + senha +
try{

Statement st = conn.createStatement();
ResultSet rs = st.executeQuery(sql);
if(rs.next()){

result = true;

nome = rs.getString("nome");}

}catch (Exception e) { }

return result; }

Figura 2 - Exemplo de código em Java guefaz acesso a uma tabela de nome usuários. Primeiramente criamos uma conexão com o banco,depois um objeto Statment e executamos a consulta passando o código SQL paro o método executeQuery da classe Stament. O resultado é gravado em uma instância da classe ResultSet.
Observem que o comando select. Ele está escrito na linguagem SQL considerada uma DML.
Esses comandos são enviados ao compilador DML para serem compilados em código objeto com acesso ao banco de dados. O restante do programa é enviado ao compilador da linguagem hospedeira. Os códigos objetos para os comandos DML e o restante do programa são ligados ('linkados')formando uma transação programada ou compilada.
As transações programadas são executadas repetidas vezes pelos usuários paramétricos, que apenas fornecem os parâmetros para as transações. No nosso exemplo anterior, as informações necessárias são login e senha. Cada execução é considerada uma transação separada. Outro exemplo de transação é o saque no caixa eletrônico, no qual o número da conta e o valor são fornecidos como parâmetros.
Na parte inferior da figura temos o processador de banco de dados em tempo de execução (PBDTE).
Ele é responsável por executar os comandos privilegiados, os planos de consulta executáveis e as transações programadas. Para isso são utilizadas informações e dados estatísticos do catálogo do sistema. O PBDTE também trabalho com o gerenciador de dados armazenados.
Os sistemas de controle de concorrência, backup e recuperação são apresentados como um módulo da figura. Eles são integrados ao processador de banco de dados em tempo de execução para fins de gerenciamento de transações. Você precisa ter em mente que esses controles são necessários para o perfeito funcionamento do SGBD. O backup é utilizado durante a recuperação caso alguma falha aconteça. A concorrência entre transações deve existir dentro de limites bem definidos para evitar que o banco de dados entre em um estado inconsistente.
Afigura apresentada não pretende descrever um SGBD específico nem esgotar suas funcionalidades.Nossa ideia foi ilustrar os módulos básicos de um SGBD e estruturar seu raciocínio.
Lembre-se que um SGBD é um sistema informatizado. Para executar todas as suas tarefas sua implementação é dividida em diferentes módulos. O SGBD interage ainda com o sistema operacional quando o acesso ao disco rígido é necessário. Vamos fazer uma questão que trata do assunto.
HORA DE

PRATICAR!

1. Ano: 2010 Órgão: BADESC Cargo: Analista de Sistemas

Os objetivos dos compiladores DDL, DML e DCL são, respectivamente:

A) criar os objetos do banco de dados, manipular (recuperação, inserção, remoção e alteração)de dados nos objetos criados pela DDL e fornecer privilégio de acesso às informações.

B) fornecer privilégio de acesso às informações, criar os objetos do banco de dados e manipular(recuperação, inserção, remoção e alteração) de dados nos objetos criados pela DDL.

C) manipular (recuperação, inserção, remoção e alteração) de dados nos objetos criados pelaDML, criar os objetos do banco de dados e fornecer privilégio de acesso às informações.

D) fornecer privilégio de acesso às informações, manipular (recuperação, inserção,
remoção e alteração) de dados nos objetos criados pela DDL e criar os objetos do banco de dados.
E) criar os objetos do banco de dados, fornecer privilégio de acesso às informações e manipular(recuperação, inserção, remoção e alteração) de dados nos objetos criados pela DDL.

Comentário: Vimos que o compilador DDL permite que o DBA emita comandos para a criação dos objetos do banco de dados, esses vão fornecer informações sobre as estruturas das tabelas como atributos e restrições. O compilador DML é responsável por transformar o códigoSQL
para manipulação dos dados armazenados.

Por fim, temos o Data Control Language - DCL, essa parte da linguagem SQL vai permitir aos administradores de banco de dados a distribuição de privilégios de acesso sobre a base de dados. Com essa informação, podemos marcar tranquilamente a resposta na alternativa A.
Gabarito: A.

Espero que você tenha entendido nossa proposta de apresentar o ambiente do SGBD.
Acabamos aqui o nosso primeiro conjunto de assuntos teóricos envolvidos na introdução dos sistemas de bancos de dados.
QUESTõES CoMENTADAS CoMPLEMENTARES

1. CEBRASPE (CESPE) - Analista Judiciário (TJ PA)/Análise de Sistema/Suporte/2020

O administrador de dados e o administrador do banco de dados exercem funções-chave na administração de banco de dados. Ao responsável pelas decisões estratégicas e de normas com relação aos dados da empresa cabe também a) definir o esquema interno.
b) definir o esquema conceituai.

c) manter contato com os usuários.

d) definir normas de descarga e recarga.

e) responder a requisitos de mudanças.

Comentário: Comentário: O administrador de dados (DA, do inglês Data Administrator) cuida do planejamento dos dados. Ele documenta, padroniza e modela como os dados de uso comum de uma organização serão armazenados e gerenciados, sempre visando atender as necessidades estratégicas. É o DA que é responsável pelas normas com relação aos dados da empresa. Por exemplo, ele define um padrão para os nomes dos atributos e das tabelas.
Mas ... a questão fala do esquema conceituai... e esse esquema, conforme comentado ao longo da aula, é definido no nível conceituai da arquitetura em 3 esquemas. Como eu sei disso? Pelo contexto da questão que foi tirada do livro do CJ Date. Vejamos o que o DATE fala sobre esse tópico:
Cabe ao administrador de dados decidir quais informações devem ser mantidas no banco de dados - em outras palavras, identificar as entidades de interesse para a empresa e identificar as informações a serem registradas sobre essas entidades. Normalmente, esse processo é referenciado como projeto lógico - às vezes, conceituai - de banco de dados. Uma vez que o administrador de dados tenha definido o conteúdo do banco de dados em um nível abstrato,o DBA então criará o esquema conceituai correspondente, usando a DDL conceituai.

Eita professor! Nem o Date sabe o que está falando! Ele disse que o DBA criará o esquema conceituai! Calma ... o Date ainda complementa ... Devemos acrescentar que, na prática,as coisas raramente serão definidas do modo exato como sugerem as observações anteriores.Em alguns casos, o administrador de dados criará o esquema conceituai diretamente. Em outros,o DBA criará o projeto lógico.

As demais atividades são executadas apenas pelo DBA. Logo, temos a resposta na alternativaB.

Gabarito: B.

2. CEBRASPE (CESPE) - Analista Judiciário (TJ PA)/Análise de Sistema/Suporte/2020

Um sistema de banco de dados proporciona a empresas o controle centralizado de todos os seus dados. O funcionamento do banco de dados baseia-se em unidades lógicas de trabalho conhecidas como a) entidades.
b) ocorrências.

c) registros.

d) tabelas.

e) transações.

Comentário: Uma transação é uma unidade lógica de trabalho que executa um conjunto de operações no banco de dados. Essas operações podem inserir, remover, modificar ou recuperar dados nas tabelas. Ao final da transação, é possível confirmar as alterações realizadas (através do comando COMMIT) ou descartar as alterações (comando ROLLBACK).
Por exemplo: um sistema de uma instituição financeira pode ter uma transação chamada
TRANSFERÊNCIA. Essa transação executa duas operações: primeiro, ela remove o valor que se quer transferir do saldo da conta de origem; depois, ela adiciona esse mesmo valor no saldo da conta de destino. Vamos ver os conceitos trazidos pelas demais alternativas:
a) entidades. - ERRADA. Esse é um conceito associado ao modelo entidade-relacionamento.
As entidades representam as "coisas" do mundo real que queremos modelar. Por exemplo:
uma loja pode ter o interesse de armazenar informações dos seus clientes e dos seus produtos.Cliente e Produto são entidades do modelo.

b) ocorrências. - ERRADA. Uma ocorrência é uma linha da tabela (também chamada de registro).
c) registros. - ERRADA. Um registro é uma linha da tabela (também chamado de ocorrência).

d) tabelas. - ERRADA. As tabelas são estruturas compostas por linhas e colunas. São utilizadas para armazenar dados nos bancos relacionais.
Concluímos, assim, que o gabarito é letra E.

Gabarito: E.

3. CEBRASPE (CESPE) - Assistente Judiciário (TJ AM)/Suporte ao Usuário de lnformática/2019

Acerca de sistema gerenciador de banco de dados, do tuning e da segurança em banco de dados,julgue o item subsequente.

Uma das vantagens de utilizar sistema gerenciador de banco de dados é o fato de ele realizar o controle da redundância de dados, o que impede a ocorrência de inconsistências entre os arquivos.
Comentário: Às vezes, há motivos comerciais ou técnicos plausíveis para manter várias cópias i i distintas dos mesmos dados (redundância controlada). Na prática, às vezes é necessário usar a redundância controlada para melhorar o desempenho das consultas.
Gabarito: Certo

4. Ano: 2019 Banca: CESPE Órgão: SEFAZ-RS Prova: Auditor Assunto: Banco de Dados

As funções de um sistema de gerenciamento de banco de dados (SGBD) incluem

A gerenciar o becape e a recuperação dos dados, bem como o escalonamento de processos no processador por meio do banco de dados.
B gerenciar o sistema de arquivos e a segurança do banco de dados.

C gerenciar a entrada e saída de dispositivos, linguagens de acesso ao banco de dados e interfaces de programação de aplicações.
D gerenciar a integridade de dados, o dicionário e o armazenamento de dados, bem como a memória do computador enquanto o SGBD estiver em execução.
E transformar e apresentar dados, controlar o acesso de multiusuário e prover interfaces de comunicação do banco de dados.
Comentário: Dentre as alternativas acima a única que apresentam funções exclusivas do
SGBD
é a alternativa E. As demais alternativas tratam de aspectos associados aos sistemas operacionais1: A) escalonamento de processos, B) gerenciamento do sistema de arquivos, C)gerenciamento da entrada e saída, D) Gerenciamento de memória.

Um Sistema de Gerenciamento de Banco de Dados (SGBD) é um conjunto de componentes que dão suporte à criação, utilização e à manutenção de bancos de dados. Inicialmente, um SGBDproporcionava armazenamento e recuperação eficientes dos dados. Devido às exigências do mercado e à inovação dos produtos, os SGBDs evoluíram e hoje fornecem uma ampla gama de recursos para a aquisição, armazenamento, disseminação, manutenção, recuperação e formatação de dados.
Gabarito: E

1 Sistema operacional (SO) é o conjunto de programas que gerenciam recursos, processadores,armazenamento, dispositivos de entrada e saída e dados da máquina e seus periféricos.
O sistema faz a comunicação entre o hardware e os demais softwares, criando uma plataforma comum a todos os programas utilizados. São exemplos de SO: Dos, Unix, Linux, Mac OS, OS-2, Windows NT.
5. CEBRASPE (CESPE) - Assistente Judiciário (TJ AM)/Programador/2019

Julgue o próximo item, relativos a sistema gerenciador de banco de dados (SGBD).

Na arquitetura ANSI/SPARC de um SGBD, o nível interno trata do armazenamento físico dos dados, o nível externo trata do modo como os dados são visualizados por usuários individuais, e o nível conceituai oferece uma visão comunitária dos dados.
Comentário: O objetivo da arquitetura de três esquemas é separar as aplicações do usuário do banco de dados físico. Nessa arquitetura, os esquemas podem ser definidos nos três níveis a seguir:
1. O nível interno tem um esquema interno, que descreve a estrutura do armazenamento físico do banco de dados. O esquema interno usa um modelo de dados físico e descreve os detalhes completos do armazenamento de dados e caminhos de acesso para o banco de dados.
2. O nível conceituai tem um esquema conceituai, que descreve a estrutura do banco de dados inteiro para uma comunidade de usuários. O esquema conceituai oculta os detalhes das estruturas de armazenamento físico e se concentra na descrição de entidades, tipos de dados,relacionamentos, operações do usuário e restrições.

3. O nível externo ou de visão inclui uma série de esquemas externos ou visões do usuário.Cada esquema externo descreve a parte do banco de dados em que um grupo de usuários em particular está interessado e oculta o restante do banco de dados do grupo de usuários.
Desta forma temos uma afirmação correta.

Gabarito: Correta.

6. Ano: 2018 Banca: CESPE Órgão: EBSERH Prova: Analista de Tecnologia da Informação

Com relação a banco de dados, julgue o item seguinte.

Após um banco de dados ser criado, o administrador executa uma série de tarefas para dar permissão de acesso aos usuários que necessitam ler e gravar informações na base de dados.A responsabilidade de gerir os acessos ao banco de dados é do sistema gerenciador de banco de dados (SGBD).
Comentário: Observe que neste texto podemos verificar explicitamente o benefício do sistema de gerenciamento de banco de dados. O administrador de banco de dados vai atribuir aos diversos usuários as permissões compatíveis com suas necessidades. Contudo, quem vai gerenciar o acesso, no sentido de autorizar o usuário a acessar o banco de dados e visualizar os dados, é o próprio SGBD. Desta forma, temos uma alternativa correta.
Gabarito: C

7. Ano: 2018 Banca: CESPE Órgão: STM Prova: Técnico Judiciário - Programação de Sistemas

Acerca dos conceitos de normalização de dados e dos modelos de dados,
julgue o item subsequente.
Comparativamente aos usados pelos usuários leigos, os modelos de dados utilizados por programadores são considerados menos abstratos, pois contêm mais detalhes de como as informações estão organizadas internamente no banco de dados.
Comentário: Os usuários leigos, por terem um conhecimento mais limitado a respeito da tecnologia de banco de dados, devem ter uma visão mais abstrata dos dados quando comparados com os programadores. Estes, por terem conhecimento e formação específica podem ter mais detalhes da estrutura de armazenamento dos dados.
Gabarito: C

8. Ano: 2018 Banca: CESPE Órgão: CGM de João Pessoa - PB Prova: Auditor Municipal de Controle
Interno - Desenvolvimento de Sistemas

A respeito de bancos de dados, julgue o item a seguir.

Nos bancos de dados construídos sob a concepção do modelo hierárquico, os dados são estruturados em hierarquia ou árvores cujos nós contêm ocorrências de registros, e cada registro consiste em uma coleção de atributos.
Comentário: Um banco de dados hierárquico consiste em uma coleção de registros que são conectados uns aos outros por meio de ligações. Um registro é uma coleção de campos,cada qual contendo apenas um valor de dados. Uma ligação é uma associação entre exatamente dois registros. O modelo hierárquico difere do modelo de rede na organização de registros como coleção de árvores em vez de como grafos arbitrários.
Um diagrama com estrutura de árvore é um esquema para um banco de dados hierárquico.
Tal diagrama consiste em dois componentes básicos: retângulos, que correspondem a tipos de registro, e linhas, que correspondem a ligações. O diagrama com estrutura de árvore serve para os mesmos propósitos que um diagrama entidade-relacionamento; a saber, ele especifica a estrutura lógica geral do banco de dados.
Após essa rápida reflexão teórica sobre o assunto, podemos marcar nossa reposta como correta.
Gabarito: C

9. Ano: 2018 Banca: CESPE Órgão: CGM de João Pessoa - PB Prova: Auditor Municipal de Controle
Interno - Desenvolvimento de Sistemas

A respeito de bancos de dados, julgue o item a seguir.

Um banco de dados é uma coleção de dados que são organizados de forma randômica, sem significado implícito e de tamanho variável, e projetados para atender a uma proposta específica de alta complexidade, de acordo com o interesse dos usuários.
Comentário: Essa questão procura contrapor as propriedades listas pelo Navathe. Um banco de dados precisa representar algum aspecto do mundo real, ser logicamente coerente com algum significado inerente e possuir um grupo de usuários. Enfim, um banco de dados possui
[1] alguma fonte da qual o dado é derivado,

[2] algum grau de interação com eventos no mundo real e

[3] um público que está ativamente interessado em seu conteúdo.

Logo, a afirmação da questão está incoerente, portanto, incorreta.

Gabarito: E

10. Ano: 2018 Banca: CESPE Órgão: TCE-PB Prova: Auditor de Contas Públicas - Demais Áreas

A respeito de SGBDs, assinale a opção correta.

a) Um SGBD, por definição, não é flexível, dada a dificuldade de mudar a estrutura dos dados quando os requisitos mudam.
b) Um SGBD é um software que não prevê as funções de definição, recuperação e alteração de dados, sendo essa tarefa a função básica de um sistema de banco de dados.
c) A consistência de dados é o princípio que determina a manutenção de determinado dado em vários arquivos diferentes.
d) Conforme o princípio da atomicidade, caso ocorra erro em determinada transação, todo o conjunto a ela relacionado será desfeito até o retorno ao estado inicial, como se a transação nunca tivesse sido executada.
e) O controle de concorrência é o princípio que garante e permite a manipulação, no mesmo momento, de um mesmo dado por mais de uma pessoa ou um sistema.
Comentário: Vamos analisar as alternativas acima. Elas são relevantes para consolidar nosso conhecimento sobre o assunto. Começando pela alternativa A, o erro aparece quando o examinador afirmar que os SGBDs não são flexíveis. Lembre-se que um SGBD veio solucionar um problema de replicação dos dados em diversos arquivos distintos. Agora, com uma fonte única dos dados, as alterações dos mesmos são centralizadas.
Já a alternativa B nos remonta as funcionalidades do SGBD. O que podemos fazer com tal sistema? É possível, primariamente, armazenar e manipular dados, para tal, é necessário descrever as estruturas das tabelas. Todos os SGBDs possuem estrutura para construção do banco de dados, usando uma linguagem como SQL. Sendo assim, a alternativa B também está incorreta.
As próximas duas alternativas tratam das propriedades das transações, mais especificamente da consistência, que tem por objetivo levar o banco de dados de um estado válido para outro estado consistente, e da atomicidade, que parte do princípio que uma transação é composta por vários comandos de modificação da base de dados e que estes comandos devem ser executados em conjunto completamente ou não serem executados. Desta forma, para garantir a atomicidade, caso uma transação falhe todas as operações já efetivadas precisam ser desfeitas. Desta forma, a alternativa C está incorreta e a alternativa D é a nossa resposta.
Por fim, o controle de concorrência é um mecanismo que permite que apenas um usuário consiga modificar um dado do sistema em um determinado momento. É importante entender que é possível várias pessoas terem acesso aos dados para leitura. Como se todos estivessem lendo um livro. Contudo, na hora de escrever, só existe uma caneta e, se alguma pessoa estiver de posse da caneta, apenas ela poderá fazer alterações na base.
Gabarito: D.

ll.CESPE - Analista Ministerial (MPE Pl)/Tecnologia da lnformação/2018

Tendo em vista que, ao se desenvolver um sistema de vendas e compras para um cliente,
devem-se descrever os produtos, as entradas, as saídas, o controle de estoque e o lucro das vendas, julgue o item subsequente, relativo à modelagem de dados para a aplicação descrita.
No sistema implementado, o cliente terá de cadastrar cada produto nos módulos de vendas e compras, pois a redundância será controlada pelo usuário, e não pela modelagem do banco de dados.
Comentário: A intenção de criar qualquer sistema computacional é, via de regra,
automatizar e facilitar uma determinada atividade do negócio. A modelagem de dados serve justamente para evitar a redundância dos dados, mantendo a unicidade dos dados para que não haja dados conflitantes no sistema. A assertiva está incorreta e uma possível correção para a mesma seria:
"No sistema implementado, o cliente não terá de cadastrar cada produto nos módulos de vendas e compras, pois a redundância será tratada na fase da modelagem do banco de dados"
Gabarito: E.

12. Ano: 2016 Banca: CESPE Órgão: TCE-SC Prova: Auditor Fiscal de Controle Externo - Informática

Com relação aos bancos de dados relacionais, julgue o próximo item.

O catálogo de um sistema de gerenciamento de banco de dados relacional armazena a descrição da estrutura do banco de dados e contém informações a respeito de cada arquivo,do tipo e formato de armazenamento de cada item de dado e das restrições relativas aos dados.
Comentário: Perceba que a definição acima está de acordo com o termo dicionários de dados,catálogo de dados ou metadados presentes em um sistema de banco de dados. Lembre-se que essa separação entre a descrição dos dados e os dados propriamente dito é uma das características relevantes que foram apresentadas na evolução de sistemas de arquivos para a abordagem de banco de dados. Sendo assim, podemos afirmar que a questão está correta!
Gabarito: C.

13. CESPE - Técnico (FUB)/Tecnologia da lnformação/2016

Acerca dos conceitos de bancos de dados, julgue o item seguinte.

Uma solução para evitar a redundância controlada de informações é o uso do compartilhamento de dados; dessa forma, cada informação é armazenada uma única vez.
Comentário: Lembrando da nossa qual que existe dois tipos de redundâncias:

* Redundância controlada de dados: Acontece quando o software tem conhecimento da múltipla representação da informação e garante a sincronização entre as diversas representações.
* Redundância não controlada: Acontece quando a responsabilidade pela manutenção da sincronia entre as diversas representações de uma informação está com o usuário e não com o software.
A solução para redundância não controlada é o compartilhamento de dados, ou seja,
todos os usuários acessam a mesma fonte de dados.
Uma forma de corrigir a afirmação seria: "Uma solução para evitar a redundância não I
controlada de informações é o uso do compartilhamento de dados; dessa forma, cada informação é armazenada uma única vez."
Da forma com está escrito na questão, o item pode ser assinalado como INCORRETO.

Gabarito: E

14. CESPE - Técnico Judiciário (STM)/Apoio Especializado/Programação de Sistemas/2018

Acerca dos conceitos de normalização de dados e dos modelos de dados,
julgue o item subsequente.
O modelo conceituai, que reflete uma estrutura simplificada do banco de dados, é responsável por registrar como os dados estão armazenados no sistema de gerenciamento de banco de dados (SGBD.)
Comentário: Vejamos uma lista das características presentes nos diferentes níveis de modelos de dados:
Modelo Conceituai

* É uma descrição de banco de dados de forma independente de implementação num sistema de gerenciamento.
* Registra quais dados podem aparecer no banco, mas não registra COMO estes dados estão armazenados no SGBD. (Veja que o modelo registra o que e não como, logo a alternativa está incorreta.)
* Oferecem conceitos que são próximos ao modo como muitos usuários percebem os dados.

* Os modelos de dados conceituais utilizam conceitos como entidades,
atributos e relacionamentos.
Modelo Lógico

* Também conhecidos como modelos de dados representativos ou de implementação

* Mostram os dados usando estruturas de registro e, portanto, às vezes são denominados modelos de dados baseados em registro.
Modelo Físico

* Descrevem o armazenamento dos dados como arquivos no computador, com informações como formatos de registro, ordenações de registro e caminhos de acesso.
* Um índice é um exemplo de um caminho que permite o acesso direto aos dados usando um termo de índice ou uma palavra-chave.
Assim, podemos marcar a afirmação como incorreta.

Gabarito: E.

15. CESPE - Analista de Gestão Educacional (SEDF)/Tecnologia da lnformação/2017

Julgue o item seguinte, a respeito de estruturas em programação e de arquiteturas de bancos de dados.
O esquema do nível externo de uma arquitetura de três esquemas oculta os detalhes das estruturas de armazenamento físico e se concentra na descrição de entidades, tipos de dados,conexões, operações de usuários e restrições.

Comentário: Segundo o Elmarsi, os níveis da arquitetura em 3 esquemas podem ser descritos da seguinte forma:
1. O nível interno tem um esquema interno, que descreve a estrutura do armazenamento físico do banco de dados. O esquema interno usa um modelo de dados físico e descreve os detalhes completos do armazenamento de dados e caminhos de acesso para o banco de dados.
2. O nível conceituai tem um esquema conceituai, que descreve a estrutura do banco de dados inteiro para uma comunidade de usuários. O esquema conceituai oculta os detalhes das estruturas de armazenamento físico e se concentra na descrição de entidades, tipos de dados,relacionamentos, operações do usuário e restrições. Normalmente, um modelo de dados representativo é usado para descrever o esquema conceituai quando um sistema de banco de dados é implementado. Esse esquema conceituai de implementação costuma estar baseado em um projeto de esquema conceituai em um modelo de dados de alto nível.
3. O nível externo ou de visão inclui uma série de esquemas externos ou visões do usuário.
Cada esquema externo descreve a parte do banco de dados em que um grupo de usuários em particular está interessado e oculta o restante do banco de dados do grupo de usuários. Como no nível anterior, cada esquema externo é comumente implementado usando um modelo de dados representativo, possivelmente baseado em um projeto de esquema externo em um modelo de dados de alto nível.
O texto da questão mistura os níveis conceituai e externo, logo, temos uma alternativa
I incorreta.

Gabarito: E

16. CESPE - Técnico Judiciário (TRE BA)/Apoio Especializado/Operação de Computadores/2017

Na modelagem de dados, a capacidade de modificar a definição dos esquemas em determinado nível, sem afetar o esquema do nível superior, é denominada a) integridade de domínio.
b) esquema.

c) especialização total.

d) independência de dados.

e) cardinalidade.

Comentário: A arquitetura de três esquemas pode ser usada para explicar melhor o conceito de independência de dados, que pode ser definida como a capacidade de alterar o esquema em um nível do sistema de banco de dados sem ter de alterar o esquema no nível mais alto.Podemos definir dois tipos de independência de dados:

1. Independência lógica de dados é a capacidade de alterar o esquema conceituai sem ter de alterar os esquemas externos ou os programas de aplicação. Podemos alterar o esquema conceituai para expandir o banco de dados (acrescentando um tipo de registro ou item de dado), para alterar restrições ou para reduzir o banco de dados (removendo um tipo de registro ou item de dado). No último caso, esquemas externos que se referem apenas aos dados restantes não seriam afetados.
2. Independência física de dados é a capacidade de alterar o esquema interno sem ter de alterar o esquema conceituai. Logo, os esquemas externos também não precisam ser alterados. Mudanças no esquema interno podem ser necessárias porque alguns arquivos físicos foram reorganizados — por exemplo, ao criar estruturas de acesso adicionais —para melhorar o desempenho da recuperação ou atualização.
Logo, temos nossa resposta na alternativa D.

Gabarito: D

17.CESPE - Técnico Judiciário (TRT 7- Região)/Apoio Especializado/Tecnologia da lnformação/2017
Acerca da arquitetura de três esquemas para bancos de dados, assinale a opção correta.

a) Uma alteração no esquema interno da arquitetura implica alterar também o esquema externo.
b) Na arquitetura de três esquemas, os níveis são definidos como interno, intermediário e externo.
c) No nível interno da arquitetura, são descritos os caminhos de acesso para o banco de dados.

d) Em um SGBD embasado nessa arquitetura, todos os grupos de usuários utilizam o mesmo esquema externo.
—————————————————————————————————————————--—q

I Comentário: Vamos comentar cada uma das alternativas acima:

a) Errada. Pela definição de independência de dados uma alteração no esquema interno da arquitetura não implica em alterar o esquema conceituai nem o esquema externo.
b) Errada. Os três níveis da arquitetura em 3 esquemas são interno, conceituai e externo.

c) Essa é a nossa resposta. O esquema interno usa um modelo de dados físico e descreve os detalhes completos do armazenamento de dados e caminhos de acesso para o banco de dados.
d) Errada. Cada esquema externo descreve a parte do banco de dados em que um grupo de usuários em particular está interessado e oculta o restante do banco de dados do grupo de usuários.
Gabarito: C.

18. CESPE - Técnico Judiciário (TRE TO)/Apoio Especializado/Programação de Sistemas/2017

A respeito da arquitetura de três esquemas para banco de dados, assinale a opção correta.

a) Uma das desvantagens da arquitetura de três esquemas é a impossibilidade de aplicar a independência de dados.
b) Um dos objetivos da arquitetura de três esquemas é aproximar o banco de dados físico das aplicações.
c) O nível conceituai serve para descrever a estrutura do banco de dados para um conjunto de usuários.
d) Mapeamentos são as transformações que dados brutos armazenados sofrem para se tornar informações inteligíveis.
e) O nível interno inclui uma série de visões do usuário utilizadas para descrever partes do banco de dados.
í Comentário: Vamos analisar cada uma das alternativas:

a) Errado. Uma das características da arquitetura em 3 esquemas é justamente a independência de dados que pode ser classificada em independência lógica e independência física.
b) Errado. Um dos objetivos da arquitetura é abstrair a complexidade dos dados no nível físico para as aplicações.
c) Certo! O nível conceituai descreve um esquema conceituai para uma comunidade de usuários.
d) Errado. Os processos de transformação de requisições e os resultados entre os níveis são chamados de mapeamentos.
e) Errado. Cada esquema externo descreve a parte do banco de dados em que um grupo de usuários em particular.
Assim, temos a nossa resposta na alternativa C.

Gabarito: C

Aula Thiago Cavalcanti)

19.CESPE - Auditor de Controle Externo (TCE-PA)/lnformática/Administrador de Banco de
Dados/2016

Com relação a sistemas gerenciadores de bancos de dados (SGBD), julgue o próximo item.

No nível conceituai da arquitetura de três camadas de banco de dados, cada esquema externo descreve a parte do banco que interessa a determinado grupo de usuários e oculta desse grupo o restante do banco de dados.
Comentário: O nível externo ou de visão inclui uma série de esquemas externos ou visões do usuário. Cada esquema externo descreve a parte do banco de dados em que um grupo de usuários em particular está interessado e oculta o restante do banco de dados do grupo de usuários.
Gabarito: E

20.CESPE - Auditor de Controle Externo (TCE-PA)/lnformática/Analista de Sistema/2016

Julgue o item subsequente, no que se refere a sistemas de gerenciamento de bancos de dados(SGBD).

Independência lógica de dados refere-se à capacidade de alterar o esquema conceituai sem a necessidade de alterar os esquemas externos ou os programas de aplicação.
Comentário: Independência lógica de dados é a capacidade de alterar o esquema conceituai sem ter de alterar os esquemas externos ou os programas de aplicação. Podemos alterar o esquema conceituai para expandir o banco de dados (acrescentando um tipo de registro ou item de dado), para alterar restrições ou para reduzir o banco de dados (removendo um tipo de registro ou item de dado).
Gabarito: C

21.CESPE - Técnico (FUB)/Tecnologia da lnformação/2016

Acerca dos conceitos de bancos de dados, julgue o item seguinte.

Em um projeto de banco de dados, a modelagem conceituai define quais dados vão aparecer no banco de dados, mas sem considerar a sua implementação.
Comentário: Exatamente, um modelo conceituai é um modelo de dados abstrato,
que descreve a estrutura de um banco de dados de forma independente de um SGBD particular.Somente o modelo físico que dependerá de sua implementação. Portanto, gabarito CERTO.

Gabarito: C

22. BANCA: CESPE ANO: 2014 ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - SUPORTE E
INFRAESTRUTURA

Julgue os itens a seguir, relativos à administração de banco de dados e ao sistema de gerenciamento de banco de dados (SGBD).
[69] Os dados físicos de um banco de dados podem ser acessados diretamente por meio de qualquer sistema, sem a necessidade de utilização do SGBD.
[70] Uma das atribuições do administrador de banco de dados é definir a estratégia que determinará como será feito o becape do banco de dados.
Comentário: Aproveitaremos essa questão para fazer um comentário técnico e prático sobre o assunto em cada uma das alternativas.
Na assertiva 69 diz que o acesso aos bancos de dados pode ser feito fisicamente sem a necessidade de um SGBD. Essa afirmação é falsa, se você lembrar das conexões que são feitas aos bancos, você precisa passar as informações de endereço (IP ou URL), porta, schema e um driver ou conector, que vai permitir uma comunicação correta entre o sistema e o banco de dados, além da autenticação do usuário. Sendo, portanto, incorreta a alternativa.
A alternativa 70 faz menção a uma das tarefas técnicas executadas pelo DBA. É
necessário definir um roteiro ou procedimento de backup do banco de dados. Neste são definidos a periodicidade, o tipo de backup, a mídia de armazenamento e outras especificidades.Essa é uma das tarefas mais importantes feitas pelo DBA. Sendo assim, a alternativa está correta.
Gabarito: E C.

23. BANCA: CESPE ANO: 2013 ÓRGÃO: MC PROVA: ANALISTA DE NÍVEL SUPERIOR - TECNOLOGIA
DA INFORMAÇÃO

Julgue os itens a seguir, acerca dos fundamentos e das finalidades do banco de dados.

[51] Atualmente, os bancos de dados são utilizados para armazenar e processar dados de caracteres em geral, não apresentando recursos para tratar dados multimídias, como filmes e fotografias.
[52] Uma característica fundamental do banco de dados e dos antigos sistemas de arquivos é o inter-relacionamento dos dados, sem redundâncias ou duplicação de dados.
[53] Para definir e manter os dados em um banco é necessário o uso de sistemas de aplicação,
o que caracteriza a dependência de dados, que é um fundamento do banco de dados.

Comentário: Vamos analisar as alternativas acima.

Começando pelo item 51. Veja que a questão sugere que existe uma limitação nos tipos de dados armazenados em bancos de dados. Sabemos que todos os SGBDs comerciais que implementam SQL possuem o tipo de dados BLOB - Binary Large Object. Nele é possível gravar qualquer informação em formato binário como arquivos multimídias. Falaremos mais sobre tipos de dados na aula sobre SQL. Podemos então marcar a alternativas como incorreta.
Observem que a alternativa 52 tenta comparar os sistemas de arquivos com os bancos de dados colocando uma das suas principais diferenças como uma similaridade entre eles. Adiminuição da redundância e da duplicação ocorre primordialmente com a evolução dos sistemas de arquivo para os sistemas de bancos de dados. Sendo assim, alternativa também está incorreta.
Vimos que por estarem isolados, dados e aplicações, criam um conceito chamado independência de dados do programa. Este só é possível por conta da abstração de dados. Aabstração de dados permite a criação de diferentes níveis de modelos. Falaremos mais sobre os níveis de abstração quando apresentarmos os modelos de dados. Mas, por enquanto, o nosso conhecimento já é suficiente para analisarmos a questão 53 como errada.
Gabarito: E E E

24. BANCA: CESPE ANO: 2014 ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - SUPORTE E
INFRAESTRUTURA

Julgue os itens a seguir, relativos à administração de banco de dados e ao sistema de gerenciamento de banco de dados (SGBD).
[71] Um SGBD deve gerenciar o acesso múltiplo aos dados de uma tabela sem ocasionar perda da integridade dessas informações.
Comentário: Vejam que o SGBD possui como uma das suas características fazer o controle de concorrência entre diferentes usuários ou transações que acessam uma mesma tabela, ou um conjunto de dados no modelo relacional. Isso é importante para garantir a integridade dos registros e a consistência das transações executadas. Desta forma, podemos marcar a alternativa como correta!
Gabarito: C.

25. BANCA: CESPE ANO: 2015 ÓRGÃO: MPOG PROVA: ANALISTA - ANALISTA EM TECNOLOGIA DA
INFORMAÇÃO

Acerca de sistema de gerenciamento de banco de dados (SGBD), julgue os seguintes itens.

Aula Thiago Cavalcanti)

[115] Os dados armazenados em um SGBD são acessados por um único usuário de cada vez,sendo impedido o acesso concorrente aos dados.

[116] O SGBD proporciona um conjunto de programas que permite o acesso aos dados sem exposição dos detalhes de representação e armazenamento de dados, por meio de uma visão abstrata dos dados, conhecida como independência de dados.
Comentário: Vimos na nossa aula que uma das características de SGBDs é o suporte a usuários simultâneos. O SGBD faz o controle de concorrência entre transações que tentam acessar a mesma tabela ao mesmo tempo. A alternativa 115 está incorreta.
Uma das características que já conhecemos é independência entre dados e programas. Vimos que a partir do momento em que temos um dicionário de dados, é possível excluir da estrutura dos programas a definição dos dados presentes nos mesmos. Agora isolados,dados e aplicações, criam um conceito chamado independência de dados do programa. Este só é possível por conta da abstração de dados. A abstração de dados permite a criação de diferentes níveis de modelos. Por isso a alternativa 116 está correta.
Gabarito: E C.

26. BANCA: CESPE ANO: 2015 ÓRGÃO: DEPEN PROVA: AGENTE PENITENCIÁRIO FEDERAL -
TECNOLOGIA DA INFORMAÇÃO

No que diz respeito a linguagens de programação e banco de dados, julgue os itens a seguir.

[101] Os níveis interno, externo e conceituai da arquitetura de um banco de dados são responsáveis, respectivamente, por gerenciar o modo como os dados serão armazenados fisicamente, por gerenciar o modo como os dados serão vistos pelos usuários e por representar todo o conteúdo de informações do banco de dados.
Comentário: Falamos sobre a arquitetura três esquemas: interno, conceituai e externo.Observem que a alternativa acima está correta. Vá se acostumando com os termos e conceitos:

O nível externo é o nível do usuário. Cada grupo de usuários pode ter uma visão externa separada (ou visão, para resumir) de um banco de dados customizado para as necessidades específicas do grupo.
O esquema conceituai define um banco de dados de uma empresa que pode ser bastante grande, com centenas de tipos de entidade e relacionamentos. O esquema conceituai representa o banco de dados inteiro.
O esquema interno representa a visão do armazenamento do banco de dados. O esquema interno define arquivos, grupos de dados em um dispositivo de armazenamento como um disco rígido.
Gabarito: C.

27. BANCA: CESPE ANO: 2013 ÓRGÃO: MC PROVA: ANALISTA DE NÍVEL SUPERIOR - TECNOLOGIA
DA INFORMAÇÃO

Julgue os itens subsequentes, quanto à administração de banco de dados.

[58] O administrador do banco de dados não deve gerenciar a utilização do espaço em disco nos servidores, pois sua função limita-se à utilização de ferramentas de gerenciamento com o objetivo de garantir a disponibilidade dos serviços de banco.
[59] A administração de banco de dados abrange a definição e a alteração de esquema,
que,
em alguns casos, são tarefas importantes para melhorar o desempenho do banco de dados.

Comentário: Nesta questão tratamos mais uma vez das funções do administrador de banco de dados. Responsável pelo suporte técnico as atividades do SGBD, uma das suas atividades envolve monitorar o crescimento das bases de dados em disco ou no conjunto de discos. Essa ação está relacionada ao controle da capacidade de armazenamento do banco de dados.Quando o espaço disponível se aproxima de zero ele deve trabalhar para alocar mais espaço.Esse serviço faz parte da garantia de disponibilidade do banco de dados. Sendo assim,
a alternativa 58, pode ser considerar errada.
O ajuste fino ou tuning dos esquemas de banco de dados são de reponsabilidade do DBA. Esses ajustes ajudam a melhorar o desempenho do banco de dados. Temos a alternativa 59 como correta.
Gabarito: E C.

28. BANCA: CESPE ANO: 2013 ÓRGÃO: ANTT PROVA: ANALISTA ADMINISTRATIVO -
INFRAESTRUTURA DE TI

No que diz respeito às funções do administrador de dados e à elaboração e implantação de projeto de banco de dados, julgue os itens que se seguem.
[89] Uma das funções do administrador de dados é padronizar os dados, documentando as definições e descrições dos itens de dados.
Comentário: Vimos que uma das funções do administrador de dados é trabalhar com os dados e sua organização de forma global. Ele tem a responsabilidade de padronizar valores e definir domínios que sejam coerentes com o negócio. Podemos avaliar a alternativa 89 como correta,pois está de acordo com nosso conhecimento.

Gabarito: C E C.

0 0

29. Ano: 2010 Banca: CESPE Órgão: Banco da Amazônia Prova: Técnico Científico - Tecnologia da
Informação

O dicionário de dados é uma das principais ferramentas para a administração dos dados corporativos. Por meio da engenharia reversa, pode-se armazenar os modelos de dados, as estruturas de dados, seus relacionamentos e toda a documentação necessária para garantir facilidade na localização e manipulação dos dados. Acerca dos papéis do administrador de dados (AD) e dos dicionários de dados, julgue os itens a seguir.
[1] O dicionário de dados é considerado um subconjunto das funções de um catálogo de sistema.
[2] O catálogo do sistema é um repositório com função de armazenar as definições dos esquemas dos bancos de dados.
Comentário: É importante lembrar que existe uma hierarquia entre os objetos ou elementos em um dicionário de dados. Um dicionário de dados possui a descrição dos esquemas ou catálogo de sistemas. Cada catálogo deve conter a descrição dos objetos que fazem parte do contexto de um sistema, como tabelas, visões e domínios. Dentro das definições das tabelas temos as descrições dos atributos e restrições de integridades dos dados.
Assim, ao analisar as alternativas acima, podemos inferir que a alternativa
[1] encontra-se incorreta, já a afirmação [2] está certa!
Gabarito: E C.

QUESTõES CoMENTADAS

QUESTõES CoMENTADAS CESCRANRIO.

1. BANCA: CESGRANRIO ANO: 2012 ÓRGÃO: LIQUIGÁS PROVA: PROFISSIONAL DE TECNOLOGIA
DA INFORMAÇÃO - ADMINISTRADOR DE BANCO DE DADOS

A arquitetura ANSI/SPARC de um Sistema Gerenciador de Banco de Dados (SGBD) divide-se nos níveis
A externo, conceituai e interno
B externo, lógico e recuperador
C interno, indexador e lógico

D físico, conceituai e lógico

E físico, indexador e recuperador

Comentário: Questão água com açúcar, quais seriam os níveis da arquitetura ANSI/SPARC?
Externo,
Conceituai e Interno! Observem a figura a seguir para relembrar os níveis envolvidos.

USUÃRIOS
FINAIS

Logo, podemos marcar nossa resposta na alternativa A.

Gabarito: A.

HORA DE

PRATICAR!

2. BANCA: CESGRANRIO ANO: 2010 ÓRGÃO: ELETROBRAS PROVA: ANALISTA DE SISTEMAS -
ENGENHARIA DE SOFTWARE

Um Modelo de Dados corresponde a uma descrição formal da estrutura de um banco de dados.
Com relação à Modelagem de Dados, relacione os modelos, apresentados na coluna da esquerda,
à respectiva característica, entre as indicadas na coluna da direita.

Modelo de Dados

I - Conceituai

II - Lógico

III - Físico

Característica

P - Representa a estrutura de dados, conforme vista pelo usuário do SGBD.
Q - Utiliza as técnicas de mode­
lagem baseadas em Rede,
Hierárquico e Relacional.

R - Trata dos aspectos de imple­
mentação do SGBD.

S - É abstrato, independente de um SGBD particular.
Estão corretas as associações
A I - P, II - Q, III-R.

B I -Q, II - R, III -S.

Cl-S, ll-P, lll-R.

Dl-S, ll-R, lll-Q.

E I - S, II - P, III -Q.

Comentário: Veja que a questão trata dos níveis de modelo. Os três modelos definidos pela questão são conceituai, lógico e físico. O modelo conceituai apresenta aos usuários dos sistemas uma modelagem que esconde detalhes de implementação por meio da abstração e muitas vezes restringe o escopo do banco de dados a apenas as entidades que fazem parte do contexto do usuário. Observem também que o fato ser abstrato e independente de um SGBD particular é uma característica do modelo de dados conceituai.
O modelo lógico, segundo Carlos Heuser, é modelo de dados que representa a estrutura de dados de um banco de dados conforme vista pelo usuário do SGBD. O modelo lógico nos traz à lembrança dos modelos baseados em registros em Rede, Hierárquico e Relacional. O modelo relacional ainda é o mais usado dentro do mercado de banco de dados. Por fim, temos o modelo físico que trata de detalhes das estruturas de armazenamento das informações dentro dos storages.
Vejam que pelo exposto, nossa resposta encontra-se na alternativa C.

Gabarito: C.

< > HORA DE

== PRATICAR!

3. Ano: 2014 Banca: CESGRANRIO Órgão: Banco da Amazônia Prova: Técnico Científico - Banco de Dados
Na arquitetura ANSI/SPARC de banco de dados, o nível conceituai a) define a estrutura de armazenamento do banco de dados.
b) define a estrutura do banco de dados para uma comunidade de usuários.

c) descreve a parte do banco de dados em que um grupo de usuários está interessado,
escondendo as outras partes.
d) descreve os caminhos de acesso para a base de dados.

e) inclui um número de visões de usuário.

Comentário: Vejamos o que está a cargo do nível conceituai da arquitetura em 3
esquemas. Esse nível de abstração descreve quais dados estão armazenados de fato no banco de dados e as relações que existem entre eles. Neste ponto, o banco de dados inteiro é descrito em termos de um pequeno número de estruturas relativamente simples. Embora as implementações de estruturas simples no nível conceituai possam envolver complexas estruturas de nível físico, o usuário do nível conceituai não precisa se preocupar com isso. Sua abstração é usada por administradores de banco de dados,que podem decidir quais informações devem ser mantidas no BD.

Segundo o Date, livro muito usado como referencia para as questões da CESGRANRIO, o nível conceituai, também conhecido como nível lógico de comunidade é um nível indireto entre os níveis
Logo, temos nossa resposta na alternativa B. Tente observar as outras alternativas e associar, se possível, a um dos outros níveis descritos na figura.
Gabarito: B

4. Ano: 2014 Banca: CESGRANRIO Órgão: EPE Prova: Analista de Gestão Corporativa -
Tecnologia da Informação

Um dicionário de dados utilizado por um desenvolvedor tem como função a) visualizar a estrutura de dados b) identificar significados e conteúdo dos dados c) servir como um inventário dos dados contidos em uma base de dados d) explicitar os modelos de entidades e relacionamentos e) controlar o histórico do acesso a dados pelos usuários
Comentário: O SGBD deve fornecer uma função de dicionário de dados. Este pode ser considerado um banco de dados isolado que contém os dados sobre os dados, também chamados de metadados ou descritores. Em outras palavras, ele contém definições de outros objetos do sistema. Em particular, todos os vários esquemas e todas as diversas restrições de segurança e integridade estarão armazenados, tanto na forma de fonte quanto de objeto, no dicionário. Podemos perceber que ele possui uma descrição detalhada dos dados, sendo assim, é possível dizer que ele serve como um inventário dos dados contidos em uma base de dados.
Gabarito: C

5. Ano: 2014 Banca: CESGRANRIO Órgão: EPE Prova: Analista de Gestão Corporativa -
Tecnologia da Informação

O responsável por um SGBD relacional que apoiava vários sistemas percebeu que havia problemas de desempenho e resolveu criar alguns índices novos. Nenhuma aplicação precisou ser alterada, mas todas se beneficiaram dessa alteração.
Isso é um exemplo de que tipo de independência de dados fornecida pelos SGBD?

a) Lógica b) Relacional c) Conceituai d) Externa e) Física
Comentário: O mapeamento conceitual/interno define a correspondência entre a visão conceituai e o banco de dados armazenado. Ele especifica o modo como os registros e campos conceituais são representados no nível interno. Se a estrutura do banco de dados armazenado for alterada - isto é,se for efetuada uma mudança na definição dos dados armazenados - o mapeamento conceitual/interno terá de ser alterado de acordo, a fim de quer o esquema conceituai possa permanecer invariável.
É de reponsabilidade do DBA, ou possivelmente do SGBD, administrar tais alterações.
Pode dizer que, os efeitos das mudanças devem ser isolados abaixo do nível conceituai, a fim de preservar a independência dos dados física. Logo, a resposta está na alternativa E.
Gabarito: E

< > HORA DE

== PRATICAR!

6. Ano: 2014 Banca: CESGRANRIO Órgão: IBGE Prova: Supervisor de Pesquisas - Tecnologia de
Informação e Comunicação

Segundo a classificação de categorias de modelos de dados, o modelo de dados relacional deve ser entendido como a) conceituai b) externo c) físico d) interno e) representacional
Comentário: O modelo lógico ou relacional pode ser classificado como um modelo representacional ou de implementação. Podemos relembrar disto olhando para a figura abaixo. Vejam que no nível conceituai temos os modelos entidade-relacionamento.
Esquemas
Conceituais

-õ
Conceituais

Alto nível i 7
" A

raiiem---la* DUIIG».

Esquemas \

Lógicos

Esquemas
Físicos

Representativos
Implementação

Físicos
Baixo nível

À

Logo, podemos marcar nossa resposta na alternativa E.

Gabarito: E.

7. Ano: 2014 Banca: CESGRANRIO Órgão: IBGE Prova: Supervisor de Pesquisas - Tecnologia de
Informação e Comunicação

SQL é uma linguagem dedicada à operação de Bancos de Dados relacionais,
padronizada internacionalmente, e que pode ser encontrada nos principais SGBD modernos.
Os principais comandos da sua linguagem de manipulação de dados (DML) são:

a) ALTER, CREATE e DROP

b) CREATE, DELETE, READ e UPDATE

c) CREATE, DESTROY, FIND e INCLUDE

d) SELECT, DELETE, INSERT e UPDATE

e) SELECT, JOIN, PROJECT e RENAME

Comentário: Os comandos DML (Data Manipulation Language) ou linguagem de manipulação de dados que nos permite inserir, alterar e remover dados de uma tabela. Sendo assim,temos os seguintes comandos: SELECT, DELETE, INSERT e UPDATE.
Gabarito: D.

8. Ano: 2014 Banca: CESGRANRIO Órgão: IBGE Prova: Supervisor de Pesquisas - Tecnologia de
Informação e Comunicação

O modelo relacional tornou-se o padrão estabelecido do mercado. Outros modelos anteriores ao modelo relacional, porém, podem ser encontrados em sistemas usados no passado e,algumas vezes,
encontrados como sistemas legados nas empresas.

Dois desses modelos são os a) em rede e XML
b) hierárquico e em rede c) hierárquico e XML
d) orientado a objetos e em rede e) orientado a objetos e XML
Comentário: Segundo o Navathe, dois modelos de dados antigos, importantes historicamente,
agora conhecidos como modelos de dados legados, são os modelos em rede e os modelos hierárquicos. Omodelo em rede representa os dados como tipos de registros e um tipo relacionamento 1:N,

limitado, chamado tipo conjunto. Esse modelo também foi conhecido como CODADYL DBTG. Já o modelo hierárquico representa os dados como estruturas de árvores hierárquicas.Vejam que,
diante da afirmação acima, só podemos marcar nossa resposta na alternativa B.

Gabarito: B.

9. Ano: 2013 Banca: CESGRANRIO Órgão: IBGE Prova: Analista - Suporte Operacional

A independência de dados é uma das propriedades dos SGBDs relacionais. Ela é atingida por meio do uso de três níveis de abstração de dados, representados usualmente na forma dos esquemas a) lógico, relacional e externo b) lógico, conceituai e externo c) físico, conceituai e externo d) físico, externo e de aplicação e) físico, lógico e de aplicação
Comentário: O sistema de banco de dados deve garantir uma visão totalmente abstrata do banco de dados para o usuário, ou seja, para o usuário do banco de dados pouco importa qual unidade de armazenamento está sendo usada para guardar seus dados, contanto que os mesmos estejam disponíveis no momento necessário. Esta abstração se dá em três níveis:
Nível físico: é o nível mais baixo de abstração, em que define efetivamente de que maneira os dados estão armazenados.
Nível conceituai: define quais os dados que estão armazenados e qual o relacionamento entre eles.
Nível externo ou de visão do usuário: as partes do banco de dados que o usuário tem acesso de acordo com a necessidade individual de cada usuário ou grupo de usuários.
Sendo assim, nossa resposta está na alternativa C.

Gabarito: C.

10. Ano: 2013 Banca: CESGRANRIO Órgão: IBGE Prova: Tecnologista - Geoprocessamento

O Sistema Gerenciador de Banco de Dados (SGBD) NÃO apresenta a seguinte característica:

a) Procurar armazenar os dados, buscando o melhor aproveitamento da memória e visando a recuperá-los de modo eficiente.
b) Poder decidir se possui informações suficientes ou não para responder a uma consulta aos dados.
c) Saber qual a estrutura interna e de inter-relacionamento entre os dados,
de modo a gerir eficientemente o seu armazenamento.
d) Descrever as informações a respeito dos dados armazenados — projeção cartográfica,
data de criação, fontes de dados e autoria — conhecidas como metadados.
e) Permitir a inserção de mapas de uma determinada localidade que contenham nomes ou representações gráficas distintos para as mesmas entidades geográficas.
Comentário: Um fato importante é que os sistemas de informação geográfico usam os chamados banco de dados geográfico, tais bancos são muito parecidos como os relacionais, exceto pelo fato de suportar dados geométricos em suas tabelas. Sendo assim, a alternativa E não se refere a uma característica dos SGBDs.
Gabarito: E

11. Ano: 2012 Banca: CESGRANRIO Órgão: EPE Prova: Analista de Gestão Corporativa -
Tecnologia da Informação

Em uma empresa, a coleção de metadados para prover consistência entre itens de dados através de diferentes tabelas, padronizando definições semânticas e de representação de elementos de dados e melhorando o controle do compartilhamento das informações através das aplicações, é denominada a) Diagrama de entidade relacionamento b) Dicionário de dados c) Modelo conceituai de dados d) Modelo físico de dados e) Diagrama de fluxo de dados
Comentário: Um dicionário de dados (do inglês data dictionary) é uma coleção de metadados que contêm definições e representações de elementos de dados. Logo, nossa resposta encontra-se na alternativa B.
Gabarito: B

12. Ano: 2012 Banca: CESGRANRIO Órgão: Petrobras Prova: Analista de Sistemas Júnior -
lnfraestrutura-2012

Quais as propriedades ACID das transações que um SGDB relacional multiusuário deve garantir?

a) Armazenamento, Consistência, Independência e Durabilidade b) Armazenamento, Consistência, Isolamento e Determinação c) Atomicidade, Consistência, Isolamento e Durabilidade d) Atomicidade, Confiabilidade, Isolamento e Durabilidade e) Atomicidade, Confiabilidade, Independência e Determinação
Comentário: Essa questão é clássica, trata das propriedades de uma transação. A sigla
ACID refere-
se respectivamente a Atomicidade, Consistência, Isolamento e Durabilidade.

Gabarito: C.

13. Ano: 2012 Banca: CESGRANRIO Órgão: Chesf Prova: Técnico em Eletrônica

A arquitetura de um Banco de Dados ANSI/SPARC possui três níveis. O primeiro desses níveis é responsável pelo armazenamento de dados, o segundo serve de interface entre o primeiro e o terceiro nível, o qual, por seu turno, é responsável pela visualização dos dados pelo usuário.
Esses três níveis são denominados, respectivamente, de a) físico, externo e conceituai b) físico, conceituai e externo c) externo, físico e conceituai d) conceituai, externo e físico e) conceituai, físico e externo
Comentário: Veja que já fizemos uma questão bem parecida com está anteriormente. A
arquitetura
ANSI/SPARC, que data de 1975, define níveis de abstração para um sistema de gestão de bancos de dados: o nível interno (ou físico), que define a maneira pela qual são armazenados os dados e os métodos para acessá-los; o nível conceituai, também chamado de MCD (Modelo Conceituai dosDados) ou MLD (Modelo Lógico dos Dados), que define a disposição das informações no banco de dados; e o nível externo, que define as visualizações dos usuários.
Gabarito: B.

LISTA DE QUESTõES - CEBRASPE

1. CEBRASPE (CESPE) - Analista Judiciário (TJ PA)/Análise de Sistema/Suporte/2020

O administrador de dados e o administrador do banco de dados exercem funções-chave na administração de banco de dados. Ao responsável pelas decisões estratégicas e de normas com relação aos dados da empresa cabe também a) definir o esquema interno.
b) definir o esquema conceituai.

c) manter contato com os usuários.

d) definir normas de descarga e recarga.

e) responder a requisitos de mudanças.

2. CEBRASPE (CESPE) - Analista Judiciário (TJ PA)/Análise de Sistema/Suporte/2020

Um sistema de banco de dados proporciona a empresas o controle centralizado de todos os seus dados. O funcionamento do banco de dados baseia-se em unidades lógicas de trabalho conhecidas como a) entidades.
b) ocorrências.

c) registros.

d) tabelas.

e) transações.

3. CEBRASPE (CESPE) - Assistente Judiciário (TJ AM)/Suporte ao Usuário de lnformática/2019

Acerca de sistema gerenciador de banco de dados, do tuning e da segurança em banco de dados,julgue o item subsequente.

Uma das vantagens de utilizar sistema gerenciador de banco de dados é o fato de ele realizar o controle da redundância de dados, o que impede a ocorrência de inconsistências entre os arquivos.
4. Ano: 2019 Banca: CESPE Órgão: SEFAZ-RS Prova: Auditor Assunto: Banco de Dados

As funções de um sistema de gerenciamento de banco de dados (SGBD) incluem

A gerenciar o becape e a recuperação dos dados, bem como o escalonamento de processos no processador por meio do banco de dados.
B gerenciar o sistema de arquivos e a segurança do banco de dados.

C gerenciar a entrada e saída de dispositivos, linguagens de acesso ao banco de dados e interfaces de programação de aplicações.
D gerenciar a integridade de dados, o dicionário e o armazenamento de dados, bem como a memória do computador enquanto o SGBD estiver em execução.
E transformar e apresentar dados, controlar o acesso de multiusuário e prover interfaces de comunicação do banco de dados.
5. CEBRASPE (CESPE) - Assistente Judiciário (TJ AM)/Programador/2019

Julgue o próximo item, relativos a sistema gerenciador de banco de dados (SGBD).

Na arquitetura ANSI/SPARC de um SGBD, o nível interno trata do armazenamento físico dos dados, o nível externo trata do modo como os dados são visualizados por usuários individuais, e o nível conceituai oferece uma visão comunitária dos dados.
6. Ano: 2018 Banca: CESPE Órgão: EBSERH Prova: Analista de Tecnologia da Informação

Com relação a banco de dados, julgue o item seguinte.

Após um banco de dados ser criado, o administrador executa uma série de tarefas para dar permissão de acesso aos usuários que necessitam ler e gravar informações na base de dados.A responsabilidade de gerir os acessos ao banco de dados é do sistema gerenciador de banco de dados (SGBD).
7. Ano: 2018 Banca: CESPE Órgão: STM Prova: Técnico Judiciário - Programação de Sistemas

Acerca dos conceitos de normalização de dados e dos modelos de dados,
julgue o item subsequente.
Comparativamente aos usados pelos usuários leigos, os modelos de dados utilizados por programadores são considerados menos abstratos, pois contêm mais detalhes de como as informações estão organizadas internamente no banco de dados.
8. Ano: 2018 Banca: CESPE Órgão: CGM de João Pessoa - PB Prova: Auditor Municipal de Controle
Interno - Desenvolvimento de Sistemas

A respeito de bancos de dados, julgue o item a seguir.

Nos bancos de dados construídos sob a concepção do modelo hierárquico, os dados são estruturados em hierarquia ou árvores cujos nós contêm ocorrências de registros, e cada registro consiste em uma coleção de atributos.
9. Ano: 2018 Banca: CESPE Órgão: CGM de João Pessoa - PB Prova: Auditor Municipal de Controle
Interno - Desenvolvimento de Sistemas

A respeito de bancos de dados, julgue o item a seguir.

Um banco de dados é uma coleção de dados que são organizados de forma randômica, sem significado implícito e de tamanho variável, e projetados para atender a uma proposta específica de alta complexidade, de acordo com o interesse dos usuários.
10. Ano: 2018 Banca: CESPE Órgão: TCE-PB Prova: Auditor de Contas Públicas - Demais Áreas

A respeito de SGBDs, assinale a opção correta.

a) Um SGBD, por definição, não é flexível, dada a dificuldade de mudar a estrutura dos dados quando os requisitos mudam.
b) Um SGBD é um software que não prevê as funções de definição, recuperação e alteração de dados, sendo essa tarefa a função básica de um sistema de banco de dados.
c) A consistência de dados é o princípio que determina a manutenção de determinado dado em vários arquivos diferentes.
d) Conforme o princípio da atomicidade, caso ocorra erro em determinada transação, todo o conjunto a ela relacionado será desfeito até o retorno ao estado inicial, como se a transação nunca tivesse sido executada.
e) O controle de concorrência é o princípio que garante e permite a manipulação, no mesmo momento, de um mesmo dado por mais de uma pessoa ou um sistema.
11. CESPE - Analista Ministerial (MPE Pl)/Tecnologia da lnformação/2018

Tendo em vista que, ao se desenvolver um sistema de vendas e compras para um cliente,
devem-se descrever os produtos, as entradas, as saídas, o controle de estoque e o lucro das vendas, julgue o item subsequente, relativo à modelagem de dados para a aplicação descrita.
No sistema implementado, o cliente terá de cadastrar cada produto nos módulos de vendas e compras, pois a redundância será controlada pelo usuário, e não pela modelagem do banco de dados.
12. Ano: 2016 Banca: CESPE Órgão: TCE-SC Prova: Auditor Fiscal de Controle Externo - Informática

Com relação aos bancos de dados relacionais, julgue o próximo item.

O catálogo de um sistema de gerenciamento de banco de dados relacional armazena a descrição da estrutura do banco de dados e contém informações a respeito de cada arquivo,do tipo e formato de armazenamento de cada item de dado e das restrições relativas aos dados.
13. CESPE - Técnico (FUB)/Tecnologia da lnformação/2016

Acerca dos conceitos de bancos de dados, julgue o item seguinte.

Uma solução para evitar a redundância controlada de informações é o uso do compartilhamento de dados; dessa forma, cada informação é armazenada uma única vez.
14. CESPE - Técnico Judiciário (STM)/Apoio Especializado/Programação de Sistemas/2018

Acerca dos conceitos de normalização de dados e dos modelos de dados,
julgue o item subsequente.
O modelo conceituai, que reflete uma estrutura simplificada do banco de dados, é responsável por registrar como os dados estão armazenados no sistema de gerenciamento de banco de dados (SGBD.)
15. CESPE - Analista de Gestão Educacional (SEDF)/Tecnologia da lnformação/2017

Julgue o item seguinte, a respeito de estruturas em programação e de arquiteturas de bancos de dados.
O esquema do nível externo de uma arquitetura de três esquemas oculta os detalhes das estruturas de armazenamento físico e se concentra na descrição de entidades, tipos de dados,conexões, operações de usuários e restrições.

16. CESPE - Técnico Judiciário (TRE BA)/Apoio Especializado/Operação de Computadores/2017

Na modelagem de dados, a capacidade de modificar a definição dos esquemas em determinado nível, sem afetar o esquema do nível superior, é denominada a) integridade de domínio.
b) esquema.

c) especialização total.

d) independência de dados.

e) cardinalidade.

17. CESPE - Técnico Judiciário (TRT 7^ Região)/Apoio Especializado/Tecnologia da lnformação/2017
Acerca da arquitetura de três esquemas para bancos de dados, assinale a opção correta.

a) Uma alteração no esquema interno da arquitetura implica alterar também o esquema externo.
b) Na arquitetura de três esquemas, os níveis são definidos como interno,
intermediário e externo.
c) No nível interno da arquitetura, são descritos os caminhos de acesso para o banco de dados.

d) Em um SGBD embasado nessa arquitetura, todos os grupos de usuários utilizam o mesmo esquema externo.
18. CESPE - Técnico Judiciário (TRE TO)/Apoio Especializado/Programação de Sistemas/2017

A respeito da arquitetura de três esquemas para banco de dados, assinale a opção correta.

a) Uma das desvantagens da arquitetura de três esquemas é a impossibilidade de aplicar a independência de dados.
b) Um dos objetivos da arquitetura de três esquemas é aproximar o banco de dados físico das aplicações.
c) O nível conceituai serve para descrever a estrutura do banco de dados para um conjunto de usuários.
d) Mapeamentos são as transformações que dados brutos armazenados sofrem para se tornar informações inteligíveis.
e) O nível interno inclui uma série de visões do usuário utilizadas para descrever partes do banco de dados.
19. CESPE - Auditor de Controle Externo (TCE-PA)/lnformática/Administrador de Banco de
Dados/2016

Com relação a sistemas gerenciadores de bancos de dados (SGBD), julgue o próximo item.

No nível conceituai da arquitetura de três camadas de banco de dados, cada esquema externo descreve a parte do banco que interessa a determinado grupo de usuários e oculta desse grupo o restante do banco de dados.
20. CESPE - Auditor de Controle Externo (TCE-PA)/lnformática/Analista de Sistema/2016

Julgue o item subsequente, no que se refere a sistemas de gerenciamento de bancos de dados(SGBD).

Independência lógica de dados refere-se à capacidade de alterar o esquema conceituai sem a necessidade de alterar os esquemas externos ou os programas de aplicação.
21. CESPE - Técnico (FUB)/Tecnologia da lnformação/2016

Acerca dos conceitos de bancos de dados, julgue o item seguinte.

Em um projeto de banco de dados, a modelagem conceituai define quais dados vão aparecer no banco de dados, mas sem considerar a sua implementação.
22. BANCA: CESPE ANO: 2014 ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - SUPORTE E
INFRAESTRUTURA

Julgue os itens a seguir, relativos à administração de banco de dados e ao sistema de gerenciamento de banco de dados (SGBD).
[69] Os dados físicos de um banco de dados podem ser acessados diretamente por meio de qualquer sistema, sem a necessidade de utilização do SGBD.
[70] Uma das atribuições do administrador de banco de dados é definir a estratégia que determinará como será feito o becape do banco de dados.
23. BANCA: CESPE ANO: 2013 ÓRGÃO: MC PROVA: ANALISTA DE NÍVEL SUPERIOR - TECNOLOGIA
DA INFORMAÇÃO

Julgue os itens a seguir, acerca dos fundamentos e das finalidades do banco de dados.

[51] Atualmente, os bancos de dados são utilizados para armazenar e processar dados de caracteres em geral, não apresentando recursos para tratar dados multimídias, como filmes e fotografias.
[52] Uma característica fundamental do banco de dados e dos antigos sistemas de arquivos é o inter-relacionamento dos dados, sem redundâncias ou duplicação de dados.
[53] Para definir e manter os dados em um banco é necessário o uso de sistemas de aplicação,
o que caracteriza a dependência de dados, que é um fundamento do banco de dados.

24. BANCA: CESPE ANO: 2014 ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - SUPORTE E
INFRAESTRUTURA

Julgue os itens a seguir, relativos à administração de banco de dados e ao sistema de gerenciamento de banco de dados (SGBD).
[71] Um SGBD deve gerenciar o acesso múltiplo aos dados de uma tabela sem ocasionar perda da integridade dessas informações.
25. BANCA: CESPE ANO: 2015 ÓRGÃO: MPOG PROVA: ANALISTA - ANALISTA EM TECNOLOGIA DA
INFORMAÇÃO

Acerca de sistema de gerenciamento de banco de dados (SGBD), julgue os seguintes itens.

[115] Os dados armazenados em um SGBD são acessados por um único usuário de cada vez,sendo impedido o acesso concorrente aos dados.

[116] O SGBD proporciona um conjunto de programas que permite o acesso aos dados sem exposição dos detalhes de representação e armazenamento de dados, por meio de uma visão abstrata dos dados, conhecida como independência de dados.
26. BANCA: CESPE ANO: 2015 ÓRGÃO: DEPEN PROVA: AGENTE PENITENCIÁRIO FEDERAL -
TECNOLOGIA DA INFORMAÇÃO

No que diz respeito a linguagens de programação e banco de dados, julgue os itens a seguir.

[101] Os níveis interno, externo e conceituai da arquitetura de um banco de dados são responsáveis, respectivamente, por gerenciar o modo como os dados serão armazenados fisicamente, por gerenciar o modo como os dados serão vistos pelos usuários e por representar todo o conteúdo de informações do banco de dados.
27. BANCA: CESPE ANO: 2013 ÓRGÃO: MC PROVA: ANALISTA DE NÍVEL SUPERIOR - TECNOLOGIA
DA INFORMAÇÃO

Julgue os itens subsequentes, quanto à administração de banco de dados.

[58] O administrador do banco de dados não deve gerenciar a utilização do espaço em disco nos servidores, pois sua função limita-se à utilização de ferramentas de gerenciamento com o objetivo de garantir a disponibilidade dos serviços de banco.
[59] A administração de banco de dados abrange a definição e a alteração de esquema,
que,
em alguns casos, são tarefas importantes para melhorar o desempenho do banco de dados.

28. BANCA: CESPE ANO: 2013 ÓRGÃO: ANTT PROVA: ANALISTA ADMINISTRATIVO -
INFRAESTRUTURA DE TI

No que diz respeito às funções do administrador de dados e à elaboração e implantação de projeto de banco de dados, julgue os itens que se seguem.
[89] Uma das funções do administrador de dados é padronizar os dados, documentando as definições e descrições dos itens de dados.
29. Ano: 2010 Banca: CESPE Órgão: Banco da Amazônia Prova: Técnico Científico - Tecnologia da
Informação

O dicionário de dados é uma das principais ferramentas para a administração dos dados corporativos. Por meio da engenharia reversa, pode-se armazenar os modelos de dados, as estruturas de dados, seus relacionamentos e toda a documentação necessária para garantir facilidade na localização e manipulação dos dados. Acerca dos papéis do administrador de dados (AD) e dos dicionários de dados, julgue os itens a seguir.
[1] O dicionário de dados é considerado um subconjunto das funções de um catálogo de sistema.
[2] O catálogo do sistema é um repositório com função de armazenar as definições dos esquemas dos bancos de dados.
GABARITo

1. B

2. E

3. Certo

4. E

5. Certo

6. Certo

7. Certo

8. Certo

9. Errado

10. D

11. Errado

12. Certo

13. Errado

14. Errado

15. Errado

16. D

17. C

18. C

19. Errado

20. Certo

21. Certo

22. Errado Certo

23. Errado Errado Errado

24. Certo

25. Errado Certo

26. Certo

27. Errado Certo

28. Certo

29. Errado Certo

LISTA DE QUESTõES - CESGRANRIO

1. BANCA: CESGRANRIO ANO: 2012 ÓRGÃO: LIQUIGÁS PROVA: PROFISSIONAL DE TECNOLOGIA
DA INFORMAÇÃO - ADMINISTRADOR DE BANCO DE DADOS

A arquitetura ANSI/SPARC de um Sistema Gerenciador de Banco de Dados (SGBD) divide-se nos níveis
A externo, conceituai e interno
B externo, lógico e recuperador
C interno, indexador e lógico

D físico, conceituai e lógico

E físico, indexador e recuperador

2. BANCA: CESGRANRIO ANO: 2010 ÓRGÃO: ELETROBRAS PROVA: ANALISTA DE SISTEMAS -
ENGENHARIA DE SOFTWARE

Um Modelo de Dados corresponde a uma descrição formal da estrutura de um banco de dados.
Com relação à Modelagem de Dados, relacione os modelos, apresentados na coluna da esquerda,
à respectiva característica, entre as indicadas na coluna da direita.

Modelo de Dados
I - Conceituai

II - Lógico
III - Físico

Característica

P - Representa a estrutura de dados, conforme vista pelo usuário do SGBD.
Q - Utiliza as técnicas de mode­
lagem baseadas em Rede,
Hierárquico e Relacional.

R - Trata dos aspectos de imple­

mentação do SGBD.

S - É abstrato, independente de um SGBD particular.
Estão corretas as associações
Al-P, ll-Q, III-R.

Bl-Q, ll-R, lll-S.

Cl-S, ll-P, lll-R.

D I - S, II - R, III-Q.

E I - S, ll-P, III -Q.

3. Ano: 2014 Banca: CESGRANRIO Órgão: Banco da Amazônia Prova: Técnico Científico - Banco de Dados
Na arquitetura ANSI/SPARC de banco de dados, o nível conceituai a) define a estrutura de armazenamento do banco de dados.
b) define a estrutura do banco de dados para uma comunidade de usuários.

c) descreve a parte do banco de dados em que um grupo de usuários está interessado, escondendo as outras partes.
d) descreve os caminhos de acesso para a base de dados.

e) inclui um número de visões de usuário.

4. Ano: 2014 Banca: CESGRANRIO Órgão: EPE Prova: Analista de Gestão Corporativa -
Tecnologia da Informação

Um dicionário de dados utilizado por um desenvolvedor tem como função a) visualizar a estrutura de dados b) identificar significados e conteúdo dos dados c) servir como um inventário dos dados contidos em uma base de dados d) explicitar os modelos de entidades e relacionamentos e) controlar o histórico do acesso a dados pelos usuários
5. Ano: 2014 Banca: CESGRANRIO Órgão: EPE Prova: Analista de Gestão Corporativa -
Tecnologia da Informação

O responsável por um SGBD relacional que apoiava vários sistemas percebeu que havia problemas de desempenho e resolveu criar alguns índices novos. Nenhuma aplicação precisou ser alterada, mas todas se beneficiaram dessa alteração.
Isso é um exemplo de que tipo de independência de dados fornecida pelos SGBD?

a) Lógica b) Relacional c) Conceituai d) Externa e) Física
6. Ano: 2014 Banca: CESGRANRIO Órgão: IBGE Prova: Supervisor de Pesquisas - Tecnologia de
Informação e Comunicação

Segundo a classificação de categorias de modelos de dados, o modelo de dados relacional deve ser entendido como a) conceituai b) externo c) físico d) interno e) representacional
7. Ano: 2014 Banca: CESGRANRIO Órgão: IBGE Prova: Supervisor de Pesquisas - Tecnologia de
Informação e Comunicação

SQL é uma linguagem dedicada à operação de Bancos de Dados relacionais,
padronizada internacionalmente, e que pode ser encontrada nos principais SGBD modernos.
Os principais comandos da sua linguagem de manipulação de dados (DML) são:

a) ALTER, CREATE e DROP

b) CREATE, DELETE, READ e UPDATE

c) CREATE, DESTROY, FIND e INCLUDE

d) SELECT, DELETE, INSERT e UPDATE

e) SELECT, JOIN, PROJECT e RENAME

8. Ano: 2014 Banca: CESGRANRIO Órgão: IBGE Prova: Supervisor de Pesquisas - Tecnologia de
Informação e Comunicação

O modelo relacional tornou-se o padrão estabelecido do mercado. Outros modelos anteriores ao modelo relacional, porém, podem ser encontrados em sistemas usados no passado e,algumas vezes,
encontrados como sistemas legados nas empresas.

Dois desses modelos são os a) em rede e XML
b) hierárquico e em rede c) hierárquico e XML
d) orientado a objetos e em rede e) orientado a objetos e XML
9. Ano: 2013 Banca: CESGRANRIO Órgão: IBGE Prova: Analista - Suporte Operacional

A independência de dados é uma das propriedades dos SGBDs relacionais. Ela é atingida por meio do uso de três níveis de abstração de dados, representados usualmente na forma dos esquemas a) lógico, relacional e externo b) lógico, conceituai e externo c) físico, conceituai e externo d) físico, externo e de aplicação e) físico, lógico e de aplicação
10. Ano: 2013 Banca: CESGRANRIO Órgão: IBGE Prova: Tecnologista - Geoprocessamento

O Sistema Gerenciador de Banco de Dados (SGBD) NÃO apresenta a seguinte característica:

a) Procurar armazenar os dados, buscando o melhor aproveitamento da memória e visando a recuperá-los de modo eficiente.
b) Poder decidir se possui informações suficientes ou não para responder a uma consulta aos dados.
c) Saber qual a estrutura interna e de inter-relacionamento entre os dados, de modo a gerir eficientemente o seu armazenamento.
d) Descrever as informações a respeito dos dados armazenados — projeção cartográfica, data de criação, fontes de dados e autoria — conhecidas como metadados.
e) Permitir a inserção de mapas de uma determinada localidade que contenham nomes ou representações gráficas distintos para as mesmas entidades geográficas.
11. Ano: 2012 Banca: CESGRANRIO Órgão: EPE Prova: Analista de Gestão Corporativa -
Tecnologia da Informação

Em uma empresa, a coleção de metadados para prover consistência entre itens de dados através de diferentes tabelas, padronizando definições semânticas e de representação de elementos de dados e melhorando o controle do compartilhamento das informações através das aplicações, é denominada a) Diagrama de entidade relacionamento b) Dicionário de dados c) Modelo conceituai de dados d) Modelo físico de dados e) Diagrama de fluxo de dados
12. Ano: 2012 Banca: CESGRANRIO Órgão: Petrobras Prova: Analista de Sistemas Júnior -
lnfraestrutura-2012

Quais as propriedades ACID das transações que um SGDB relacional multiusuário deve garantir?

a) Armazenamento, Consistência, Independência e Durabilidade b) Armazenamento, Consistência, Isolamento e Determinação c) Atomicidade, Consistência, Isolamento e Durabilidade d) Atomicidade, Confiabilidade, Isolamento e Durabilidade e) Atomicidade, Confiabilidade, Independência e Determinação
13. Ano: 2012 Banca: CESGRANRIO Órgão: Chesf Prova: Técnico em Eletrônica

A arquitetura de um Banco de Dados ANSI/SPARC possui três níveis. O primeiro desses níveis é responsável pelo armazenamento de dados, o segundo serve de interface entre o primeiro e o terceiro nível, o qual, por seu turno, é responsável pela visualização dos dados pelo usuário.
Esses três níveis são denominados, respectivamente, de a) físico, externo e conceituai b) físico, conceituai e externo c) externo, físico e conceituai d) conceituai, externo e físico e) conceituai, físico e externo
GABARITo

1. A

2. C

3. B

4. C

5. E

6. E

7. D

8. B

9. C

10. E

11. B

12. C

13. B

