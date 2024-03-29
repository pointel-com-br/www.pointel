# Engenharia de Software e Sistemas - Arquitetura hexagonal

Índice

1) Arquitetura de Software

2) Arquitetura de Software - Coesão e Acoplamento

3) Arquitetura de Software - Arquitetura em Camadas.

4) Arquitetura de Software - Arquitetura MVC

5) Arquitetura de Software - Arquitetura Distribuída

6) Resumo - Arquitetura de Software

7) Questões Comentadas - Arquitetura de Software - CESPE

8) Questões Comentadas - Arquitetura de Software - FCC

9) Questões Comentadas - Arquitetura de Software - Diversas.

10) Lista de Questões - Arquitetura de Software - CESPE

11) Lista de Questões - Arquitetura de Software - FCC

12) Lista de Questões - Arquitetura de Software - Diversas.

13) Arquitetura Hexagonal

Conceitos Básicos

ARQUITETURA DE SoFTwARE

INCIDÊNCIA EM PROVA: BAIXA

Ao se considerar a arquitetura de um edifício, vários atributos diferentes vêm à mente. No nível mais simplista, pensamos na forma geral da estrutura física. No entanto, na realidade,arquitetura é muito mais do que isso. Ela é a maneira pela qual os vários componentes do edifício são integrados para formar um todo coeso. É o modo pelo qual o edifício se ajusta em seu ambiente e integra com outros edifícios da vizinhança.
É o grau com que o edifício atende seu propósito expresso e satisfaz às necessidades de seu proprietário. É o sentido estético da estrutura - o impacto visual do edifício - e a maneira pela qual as texturas, cores e materiais são combinados para criar a fachada e o "ambiente de moradia". Ela engloba também os detalhes - o projeto dos dispositivos de iluminação, o tipo de piso, o posicionamento de painéis, enfim, a lista é interminável.
E, finalmente, ela é arte. Mas arquitetura também é algo mais. É constituída por "milhares de decisões, tanto as grandes como as pequenas". Algumas dessas decisões são tomadas logo no início do projeto e podem ter um impacto profundo sobre todas as ações subsequentes. Outras são postergadas ao máximo, eliminando, portanto, restrições demasiadas que levariam a uma implementação inadequada do estilo da arquitetura. Mas o que dizer da arquitetura de software?
Alguns autores definem esse termo difícil de descrever da seguinte maneira:
"A arquitetura de software de um programa ou sistema computacional é a estrutura ou estruturas do sistema, que abrange os componentes de software, as propriedades externamente visíveis desses componentes e as relações entre eles". De outra forma, a arquitetura de software é a organização ou a estrutura dos componentes significativos do sistema de software que interagem por meio de interfaces.
A arquitetura não é o software operacional, mas - sim - uma representação que nos permite (1)analisar a efetividade do projeto no atendimento dos requisitos declarados, (2) considerar alternativas de arquitetura em um estágio quando realizar mudanças de projeto ainda é relativamente fácil e (3) reduzir os riscos associados à construção do software. Essa definição enfatiza o papel dos "componentes de software" em qualquer representação de arquitetura.
No contexto de projeto da arquitetura, um componente de software pode ser algo tão simples quanto um módulo de programa ou uma classe orientada a objetos, porém ele também pode ser estendido para abranger bancos de dados e "middleware" que possibilita a configuração de uma rede de clientes e servidores. As propriedades dos componentes são aquelas características necessárias para o entendimento de como eles interagem com outros componentes.
No nível da arquitetura, propriedades internas (por exemplo, detalhes de um algoritmo)
não são especificadas. As relações entre componentes podem sertão simples quanto a chamada procedural de um módulo a outro ou tão complexo quanto um protocolo de acesso a banco de dados. Uma arquitetura bem projetada deve ser capaz de atender aos requisitos funcionais e não-funcionais do sistema de software e ser suficientemente flexível para suportar requisitos voláteis.
Aarquitetura é importante, na medida em que ela permite uma comunicação efetiva entre as partes interessadas, abrangendo a compreensão, negociação e consenso. Além disso, permite decisões tempestivas, isto é, possibilita correção e validação do sistema antes da implementação.Por fim, permite uma abstração reutilizável do sistema em situações diferentes com características similares.
Uma forma de organizar a arquitetura de um sistema complexo em partes menores é por meio da utilização de camadas de software. Seguindo essa abordagem, cada camada corresponderá a um conjunto de funcionalidades de um sistema de software - sendo que as funcionalidades de alto nível dependerão das funcionalidades de baixo nível. A separação em camadas fornece um nível de abstração através do agrupamento lógico de subsistemas relacionados entre si.
Parte-se do princípio de que as camadas de abstração mais altas devem depender das camadas de abstração mais baixas - isso permite que software seja mais portável/modificável.Eventuais mudanças em uma camada mais baixa, que não afetem a sua interface, não implicarão mudanças nas camadas mais superiores; e mudanças em uma camada mais alta, que não impliquem a criação de um novo serviço em uma camada mais baixa, não afetarão as camadas mais inferiores.
A arquitetura em camadas permite melhor separação de responsabilidades;
decomposição de complexidade; encapsulamento de implementação; maior reúso e extensibilidade. No entanto,não são apenas benefícios! Elas podem penalizar o desempenho do sistema e aumentar o esforço ou complexidade de desenvolvimento do software. As camadas encapsulam bem algumas coisas,mas não todas. Isso, às vezes, resulta em alterações em cascata.

O exemplo clássico disto em uma aplicação corporativa em camadas é o acréscimo de um campo que precise ser mostrado na interface com o usuário e deva estar no banco de dados e assim deva também ser acrescentado a cada camada entre elas. Camadas extras podem prejudicar o desempenho. Em cada camada, os dados precisam, tipicamente, ser transformados de uma representação para outra.
O encapsulamento de uma função subjacente, no entanto, muitas vezes lhe dá ganhos de eficiência que mais do que compensam esse problema. Uma camada que controla transações pode ser otimizada e então tornará tudo mais rápido. Galera, camadas extras não necessariamente prejudicam o desempenho! Em geral, é isso que acontece! Porém, como foi dito, o encapsulamento de funções pode muitas vezes gerar ganhos de desempenho.
Esse assunto é polêmico e já caiu em prova, portanto vocês devem ter atenção! Bem,
acredito que isso seja suficiente para posteriormente entender melhor cada arquitetura.
(MPOG/ATI - 2015) Embora normalmente os sistemas desenvolvidos se baseiem em padrões de arquitetura, cada um deles tem arquitetura totalmente específica, em consequência dos seus requisitos.
Comentários: de fato, eu posso usar padrões de arquitetura, tais como uma arquitetura em camadas, uma arquitetura distribuída, uma arquitetura mainframe ou uma arquitetura orientada a serviços. Embora cada sistema tenha uma arquitetura baseada em seus requisitos, elas não são t otal mente específicas (Errado).
Coesão e Acoplamento

INCIDÊNCIA EM PROVA: MÉDIA

Bem, falemos brevemente sobre esses dois importantes princípios de engenharia de software:coesão e acoplamento! Eles são fundamentais no conceito de arquitetura de software. Logo,preciso que vocês decorem a seguinte frase como se fosse um mantra: Uma boa arquitetura de software deve ter componentes de projeto com baixo acoplamento e alta coesão. Como é?Acoplamento trata do nível de dependência entre módulos ou componentes de um software.

Já a Coesão trata do nível de responsabilidade de um módulo em relação a outros.
Professor, por que é bom ter baixo acoplamento? Porque se os módulos pouco dependem um do outro,modificações de um não afetam os outros, além de não prejudicar o reúso. Se esse princípio não for observado durante a construção da arquitetura de um sistema de software,pode haver problemas sérios de manutenção futura!
Professor, por que é bom ter alta coesão? Porque se os módulos têm responsabilidades claramente definidas, eles serão altamente reusáveis, independentes e simples de entender.
A Coesão está ligada ao princípio da responsabilidade única, que diz que uma classe deve ter uma e apenas uma responsabilidade e realizá-la de maneira satisfatória, isto é, a força funcional relativa de um módulo ou componente de software. O acoplamento está ligado ao grau de conexão entre módulos em uma estrutura de software. Eu apresento na tabela abaixo os vários tipos de acoplamento:
TIPO DE ACOPLAMENTO | DESCRIÇÃO

ACOPLAMENTO
POR CONTEÚDO

ACOPLAMENTO

Ocorre quando um módulo faz uso de estruturas de dados ou de controle mantidas no escopo de outro módulo.
Ocorre quando um conjunto de módulos acessa uma área global de dados.

COMUM

ACOPLAMENTO
POR CONTROLE

ACOPLAMENTO
POR DADOS

ACOPLAMENTO POR
CHAMADAS DE ROTINAS

ACOPLAMENTO POR USO DE

TIPOS

ACOPLAMENTO POR
INCLUSÃO OU IMPORTAÇÃO

ACOPLAMENTO EXTERNO

Ocorre quando módulos passam decisões de controle a outros módulos.

Ocorre quando apenas uma lista de dados simples é passada como parâmetro de um módulo para o outro, com uma correspondência um-para-um de itens.
Ocorre quando uma operação chama outra. Nesse nível de acoplamento, é comum e,
quase sempre, necessário. Entretanto, realmente aumenta a conectividade de um sistema.
Ocorre quando o Componente A usa um tipo de dados definido em um Componente B.
Se a definição de tipo mudar, todo componente que usa a definição também terá de ser alterado.
Ocorre quando um Componente A importa ou inclui um pacote ou o conteúdo do
Componente B.

Ocorre quando um componente se comunica ou colabora com componentes de infraestrutura. Embora seja necessário, deve-se limitar a um pequeno número de componentes em um sistema.
No contexto do projeto de componentes para sistemas orientados a objetos, coesão implica um componente ou classe encapsular apenas atributos e operações que estejam intimamente relacionados entre si e com a classe ou o componente em si. A comunicação e a colaboração são elementos essenciais de qualquer sistema orientado a objetos. Há, entretanto, o lado sinistro desse importante (e necessária) característica.
Como o volume de comunicação e colaboração aumenta (isto é, à medida que o grau de conexão entre as classes aumenta), a complexidade do sistema também cresce. E à medida que a complexidade aumenta, a dificuldade de implementação, testes e manutenção do software também aumentam. O acoplamento é uma medida qualitativa do grau com que as classes estão ligadas entre si.
Conforme as classes (e os componentes) se tornam mais interdependentes, o acoplamento aumenta - a ideia é tentar manter o acoplamento o mais baixo possível...
Arquitetura em Camadas

INCIDÊNCIA EM PROVA: ALTÍSSIMA

Inicialmente, os aplicativos eram combinados em uma única camada, incluindo
Banco de
Dados, Lógica do Aplicativo e Interface de Usuário. O aplicativo, em geral, era executado em um computador de grande porte, e os usuários o acessavam por meio de terminais burros que podiam apenas realizar a entrada e exibição de dados. Essa abordagem tem o benefício de ser mantida por um administrador central.
As arquiteturas de uma camada têm um grave empecilho: os usuários esperam interfaces gráficas que exigem muito mais podercomputacional do que o dos simplesterminais burros. Acomputação centralizada de tais interfaces exige muito mais poder computacional do que um único servidor tem disponível, e assim as arquiteturas de uma camada não consegue suportar milhares de usuários.Temos, então, a Arquitetura Cliente-Servidor de duas camadas.

Para explicá-la, precisamos passar alguns conceitos básicos. Bem, ela é organizada como um conjunto de serviços, além de servidores e clientes associados que os acessam e os usam. Compõem esse modelo: servidores, que oferecem serviços; clientes, que solicitam os serviços; e uma rede que permite aos clientes acessarem esses serviços.
O processamento da informação é dividido em módulo ou processos distintos,
sendo uma abordagem de computação que separa os processos em plataformas independentes que interagem, permitindo que os recursos sejam compartilhados enquanto se obtém o máximo de benefício de cada dispositivo diferente. Os principais componentes desse modelo são:
Oferecem serviços para outros subsistemas (Ex: Servidores de Impressão, Servidores
Arquivos, Servidor de Compilação, entre outros).

Solicitam os serviços oferecidos pelos servidores. Geralmente são independentes,
ser executados simultaneamente.

Permite aos clientes acessarem esses serviços - quando clientes e servidores podem executados em uma única máquina, não são necessários.
Clientes iniciam/terminam a comunicação com servidores,
solicitando/terminando serviços distribuídos. Eles não se comunicam com outros clientes diretamente, são responsáveis pela entrada e saída de dados e comunicação com o usuário e tornam a rede transparente ao usuário -em geral, são computadores pessoais conectados a uma rede. Já os servidores realizam uma execução contínua.
Eles recebem e respondem solicitações dos clientes, não se comunicam com outros servidores diretamente, prestam serviços distribuídos, atendem a diversos clientes simultaneamente - em geral, possuem um poder de processamento e armazenamento mais alto que de um cliente.Os clientes talvez precisem saber os nomes dos servidores e os serviços que eles fornecem, mas os servidores não precisam saber sobre os clientes.
Eles acessam os serviços pelo servidor por meio de chamadas remotas de procedimento usando,por exemplo, HTTP. Um cliente faz um pedido a um servidor e espera até receber uma resposta.

Cliente 1

Cliente 2 Cliente 3

Cliente 4

Internet

Servidor de
Catálogos

Catálogo do

Servidor de VídeosArquivos de

Servidor de
Fotografias
Fotografias

Servidor
Web

Info de

Acervo y^Videoclipe \DigitaHzadas/ \Filmes e Fotos,/

Essencialmente, um cliente faz um pedido a um servidor e espera até receber uma resposta. Aimagem acima mostra um exemplo de sistema baseado no modelo cliente-servidor.
Ele é multiusuário e baseado na Web, para fornecer um acervo de filmes e fotografias. Nesse sistema,vários servidores gerenciam e apresentam tipos diferentes de mídia. Os frames do vídeo precisam ser transmitidos rapidamente em sincronia, mas com uma resolução relativamente baixa.
Podem ser comprimidos em um repositório e, assim, o servidor pode cuidar da compressão/descompressão do vídeo. Fotografias devem estar em alta resolução,portanto devem ser mantidas em um servidor dedicado. O catálogo deve ser capaz de lidar com várias consultas e de fornecer links para Sistemas Web de informações com dados do filme e videoclipe,e um sistema de e-commerce que apoie a venda desses.

O programa cliente é simplesmente uma interface integrada com o usuário, construída com o uso de um navegador Web para esses serviços. A vantagem mais importante de um modelo cliente-servidor é que ele é uma arquitetura distribuída. O uso efetivo de sistemas em rede pode ser feito com muitos processadores distribuídos. É fácil adicionar um novo servidor e integrá-lo ao restante do sistema ou atualizar servidores de maneira transparente sem afetar outras partes do sistema.
As arquiteturas cliente-servidor de duas camadas podem ter duas formas:
Cliente-Magro ou
Cliente-Gordo. Como é isso, professor?

CLIENTE CLIENTE

MAGRO GORDO

No Modelo Cliente-Magro, todo processamento da aplicação e o gerenciamento de dados é realizado no servidor. O cliente é responsável somente por executar o software de apresentação,portanto é magro! No Modelo Cliente-Gordo, o servidor somente é responsável pelo gerenciamento de dados e o software do cliente implementa a lógica da aplicação e as interações com os usuários, portanto é gordo!
VANTAGENS DE CLIENTES

MAGROS

DESVANTAGENS DE CLIENTES

MAGROS

Baixo custo de administração; facilidade de proteção; baixo custo de hardware; menor custo para licenciamento de softwares; baixo consumo de energia; resistência a ambientes hosts; menor dissipação de calor para o ambiente; mais silencioso que umPC convencional; mais ágil para rodar planilhas complexas; entre outros.

Se o servidor der problema e não houver redundância, todos os clientes-magros ficarão inoperantes; necessita de maior largura de banda na rede em que é empregado; em geral, possui um pior tempo de resposta, uma vez que usam o servidor para qualquertransação; apresenta um apoio transacional menos robusto; etc.
VANTAGENS DE CLIENTES

GORDOS

DESVANTAGENS DE CLIENTES

GORDOS

Necessitam de requisitos mínimos para servidores; apresenta uma performance multimídia melhor; possui maior flexibilidade; algumas situações se beneficiam bastante, tais como jogos eletrônicos, em que se beneficiam por conta de sua alta capacidade de processamento e de hardware específico.
Não há um local central para atualizar e manter a lógica do negócio, uma vez que o código do aplicativo é executado em vários locais de cliente; é exigida uma grande confiança entre o servidor e os clientes por conta do banco de dados; não suporta bem o crescimento do número de clientes.
Comparada à arquitetura de uma camada, as arquiteturas de duas camadas separam fisicamente a interface do usuário da camada de gerenciamento de dados. Para implementar arquiteturas de duas camadas, não se pode mais ter terminais burros no lado do cliente; precisa-se de computadores que executem código de apresentação sofisticado (e, possivelmente, a lógica do aplicativo).
Sistemas Cliente-Servidor em duas camadas foram dominantes durante aproximadamente toda a década de noventa e são utilizados até hoje. Todavia, para minimizar o impacto de mudanças nas aplicações, decidiu-se separar a camada de negócio da camada de interface gráfica,gerando três camadas1: Camada de Apresentação, Camada Lógica do Negócio e Camada de
Acesso a Dados. Vejamos...
CAMADA DE
APRESENTAÇÃO

CAMADA DE

NEGÓCIO

CAMADA DE

DADOS

Também chamada de Camada de Interface, possui classes que contêm funcionalidades para visualização dos dados pelos usuários. Ela tem o objetivo de exibir informações ao usuário e traduzir ações do usuário em requisições às demais partes dos sistemas. O amplo uso da internet tornou as interfaces com base na web crescentemente populares.
Também chamada Camada Lógica ou de Aplicação, possui classes que implementam as regras de negócio no qual o sistema será implantado. Ela realiza cálculos com base nos dados armazenados ou nos dados de entrada, decidindo que parte da camada de acesso de serativada com base em requisições provenientes da camada de apresentação.
Possui classes que se comunicam com outros sistemas para realizar tarefas ou adquirir informações para o sistema. Tipicamente, essa camada é implementada utilizando algum mecanismo de armazenamento persistente. Pode haver uma subcamada dentro desta camada chamada Camada de Persistência ou Camada de Acesso.
Nessa arquitetura, a apresentação, o processamento de aplicações e o gerenciamento de dados são processos logicamente separados executados por processadores diferentes. Seu uso permite a otimização da transferência de informações entre o servidor web e o de banco de dados. As comunicações entre esses sistemas podem usar protocolos rápidos de comunicações de baixo nível.
Um middleware eficiente que apoia consultas de banco de dados em SQL (Structured Query
Language) é usado para cuidar da recuperação de informações do banco de dados. Em alguns casos, é adequado estender o modelo cliente-servidor de três camadas para uma variante com várias camadas, na qual servidores adicionais são incorporados ao sistema.
Esses sistemas podem ser usados quando as aplicações necessitam acessar e usar dados de bancos de dados diferentes. Nesse caso, um servidor de integração é colocado entre o servidor de aplicações e os servidores de banco de dados. O servidor de integração coleta os dados distribuídos e apresenta-os como se fossem provenientes de um único banco de dados. Um sistema de operações bancárias online é um exemplo de arquitetura cliente-servidor de três camadas.
O banco de dados de clientes fornece serviços de gerenciamento de dados; um servidor web fornece os serviços de aplicação, como recursos para transferir dinheiro, gerar extratos, pagar contas, etc; e uma interface gráfica amigável fornece a apresentação dos dados ao cliente. O
1 Galera, diz-se Arquitetura em Três Camadas, 3-Layers Architecture ou 3-tiers
Architecture. Apesar de muitas pessoas usarem os dois termos indiferentemente, eles não são iguais: Layers são camadas lógicas, isto é, pode haver três layers em uma única máquina e os Tiers são camadas físicas, isto é, pode haver apenas um tier por máquina. Entenderam? ;)
próprio computadorcom um browseré o cliente. Esse sistema é escalonável, pois é relativamente fácil adicionar novos servidores web quando o número de clientes aumenta.
O uso de uma arquitetura de três camadas, nesse caso, permite a otimização da transferência de informações entre o servidor web e o servidor de banco de dados. As comunicações entre esses sistemas podem usar protocolos de comunicações de baixo nível. Um middleware eficiente que apoia consultas de banco de dados é usado para cuidar da recuperação de informações do banco de dados.
A arquitetura de três camadas que distribuem o processamento de aplicações entre os clientes são mais escalonáveis. O tráfego de rede é reduzido em comparação com arquiteturas cliente-magro de duas camadas. O processamento de aplicações é mais volátil e pode ser facilmente atualizado, pois está no centro. O processamento pode ser distribuído entre os servidores de lógica de aplicações e de gerenciamento de dados, conseguindo respostas mais rápidas. Vamos resumir?
Bem, havia a arquitetura de uma camada (monolítica)! Nesse caso, um aplicativo era desenvolvido para ser usado em uma única máquina. Esse aplicativo abarcava toda a funcionalidade em um único módulo, isto é, a interface com usuário, lógica de aplicação e acesso a bancos de dados estavam presentes em um mesmo lugar. Logo, a necessidade de compartilhar a lógica de acesso a dados entre vários usuários fez surgir o modelo de arquitetura cliente-servidor em duas camadas.
Dessa forma, a base de dados foi colocada em uma máquina específica, separada das máquinas que executavam, de fato, as aplicações ou em uma mesma máquina, porém em processadores diferentes. Nessa arquitetura, os aplicativos eram instalados em estações clientes contendo toda a apresentação e lógica de aplicação. No entanto, quando havia alguma nova versão,tinha-se que reinstalar o software ou instalar a atualização em todas as (talvez milhares de) máquinas.
Esse problema fez surgir a Arquitetura Cliente-Servidor em Três Camadas. Essa abordagem retirava a lógica de negócio da máquina do cliente e a centralizava em um servidor chamadoServidor de Aplicação. Assim, o acesso ao Banco de Dados era feito seguindo regras de negócio contidas no Servidor de Aplicação, facilitando a atualização dos aplicativos. Contudo,atualizações na Camada de Apresentação precisavam ser distribuídas em todas as máquinas da rede.
Logo depois, surgiu uma nova abordagem: Arquitetura Cliente-Servidor em Quatro Camadas!
Ela surgiu com a ideia de retirar a Apresentação do cliente e centralizá-la em umServidor Web.
Assim, não havia necessidade de instalar o aplicativo na máquina do cliente, o acesso era feito por meio de um navegador. As camadas eram: Dados, Aplicação, Apresentação eCliente
(Navegador Web).

Grosso modo: um usuário faz uma requisição por meio de um Navegador (Camada do
Cliente), essa requisição é passada para um Servidor Web (Camada de Apresentação), que a processa e procura a regra de negócio correspondente no Servidor de Aplicação (Camada de Aplicação), que procura os dados no banco de dados (Camada de Dados).
Arquitetura MVC

INCIDÊNCIA EM PROVA: ALTÍSSIMA

O Model-View-Controller (MVC) é um padrão arquitetural de software para implementar interfaces de usuário. Ele divide uma aplicação de software em três partes interconectadas, de modo a separar representações internas de informação das formas em que a informação é apresentada para o usuário. Galera, esse é um assunto que pode ser bastante aprofundado, vou tentar simplificá-lo nessa aula.
Em uma linguagem bem simples e direta, ele é um padrão arquitetural de software que separa uma aplicação em três camadas. Você pode entendê-lo como uma forma de organizar o código de uma aplicação de forma que sua manutenção fique mais fácil. Trata-se da separação de responsabilidades, sendo uma maneira de quebrar uma aplicação (ou parte dela)em camadas:
Modelo, Visão e Controle.

O MVC promove a estrita separação de responsabilidade entre componentes de uma interface gráfica onde temos componentes responsáveis pela manutenção do estado da aplicação,denominado de Modelo, pela exibição de parte deste modelo para o usuário, ao que chamamos deVisão e pela coordenação entre atualizações no modelo e interações com o usuário,
feita através do Controlador.
Durante a década de setenta, surgiu a necessidade de criação de uma arquitetura para ser utilizada em projetos de interface visual na linguagem de programação Smalltalk. Aideia original era organizar o código, separar responsabilidades, aumentar a manutenibilidade,promover um baixo acoplamento e uma alta coesão, fomentar a reusabilidade do código e tornar o sistema escalável.
Passou um bocadinho de tempo e, com o surgimento da WWW, algumas pessoas pensaram em adaptar esse padrão arquitetural para o mundo web. Muitos frameworks de aplicação comerciais e não comerciais foram criados tendo como base esse modelo. Estes frameworks variam em suas interpretações, principalmente no modo que as responsabilidades MVC são divididas entre o cliente e servidor.
## CAMADA DE MODELO

Essa é a camada responsável pela representação dos dados, provendo meios de acesso(leitura/escrita). Cara, sempre que você pensar em manipulação de dados, (leitura,
escrita ou validação de dados1), pense na Camada de Modelo! Ela gerencia não só os dados, mas também os comportamentos fundamentais da aplicação - representados por regras de negócio (Sim,elas ficam na Camada de Modelo!).
A Camada de Modelo encapsula as principais funcionalidades e dados do sistema. Ela notifica suas visões e respectivos controladores quando surge alguma mudança em seu estado, isto é, ela é responsável pela manutenção do estado da aplicação. Estas notificações permitem que as visões produzam saídas atualizadas e que os controladores alterem o conjunto de comandos disponíveis.
## CAMADA DE CONTROLE

Essa é a camada responsável por receber todas as requisições do usuário.
Seus métodos -
chamados actions - são responsáveis por uma página, controlando qual modelo usar e qual visão será mostrada ao usuário. Ele é capaz de enviar comandos para o modelo atualizar o seu estado.Ele também pode enviar comandos para a respectiva visão para alterar a apresentação da visão do modelo.
A Camada de Controle atende às requisições do usuário e seleciona o modelo e a visão que o usuário usará para interagir com o modelo. O usuário interage com controladores - por meio de visões - que interpretam eventos e entradas enviadas (Jnput), mapeando ações do usuário em comandos que são enviados para o modelo e/ou para a visão para efetuar as alterações apropriadas(Output).

1 A validação ocorre na Camada de Modelo. Pode ocorrer na Camada de Visão? Sim, eu posso utilizar um JavaScript para fazer algumas validações de dados, mas isso é inseguro e se trata de uma violação do modelo. Logo, aceitem que validações ocorrem na camada de modelo.
Um controlador define o comportamento da aplicação, interpretando as ações do usuário e mapeando-as em chamadas do modelo. Em um cliente de aplicações web, essas ações do usuário poderiam ser cliques em botões ou seleções de menus. As ações realizadas pelo modelo poderiam ser ativar processos de negócio ou alterar o estado do modelo.
Vocês já pensaram no porquê de essa camada ter esse nome? Porque ela controla o fluxo da aplicação,
interpretando os dados de entrada e coordenando/orquestrando as manipulações do modelo e as interações com o usuário. Trata-se de uma camada intermediária entre a Visão e oModelo. Em geral, há um controlador para cada visão, apesar de poder existir várias controladoras para uma mesma visão.
tt CAMADA DE VISÃO

Essa é a camada responsável pela interação com o usuário, sendo responsável apenas pela exibição de dados. Trata-se de uma representação visual do modelo. Ela permite apresentar, de diversas formas diferentes, os dados para o usuário. A visão não sabe nada sobre o que a aplicação está fazendo atualmente, ela recebe instruções do controle, notifica o controle e recebe informações do modelo.
Prosseguindo com nossa linha de pensamento: geralmente, a visão contém formulários,
tabelas,
menus e botões para entrada e saída de dados. Além disso, existem diversas visões para cada modelo. Galera, agora um ponto importante que de vez em quando cai em prova e é importante saber bem para não confundir e acabar errando a questão por bobeira.
À primeira vista, a Arquitetura MVC parece não ter diferença alguma em relação à
Arquitetura em
Três-Camadas, com o Modelo substituindo a Camada de Dados, a Visão substituindo a
Camada de
Apresentação e o Controlador substituindo a Camada de Lógica de Negócio. No entanto,
essas duas arquiteturas são diferentes em relação a interação entre suas camadas.
Na Arquitetura em Três-Camadas, a comunicação entre camadas é rigidamente linear, isto é, aCamada de Apresentação e a Camada de Dados só se conversam bidirecionalmente com a
Camada de Lógica, mas nunca entre si. Já no MVC, a comunicação é triangular -existem diversas implementações diferentes dessa arquitetura, uma comunicação típica é apresentada na imagem a seguir.
Observem que a Visão pode tanto gerar eventos a serem tratados pelo Controle quanto obter os dados a serem exibidos diretamente do modelo. O Controle trata os eventos daVisão, mas também pode manipular diretamente o Modelo. Finalmente, o Modelo pode reagir diretamente tanto à Visão quanto ao Controle, mas também pode gerar eventos a serem tratados pela visão.
Essa última sentença é extremamente polêmica - vocês encontrarão muitos lugares dizendo que não é possível que a visão solicite diretamente o estado do modelo, mas é possível,sim! Vamos supor que você esteja comprando cursos no site do Estratégia! Colocou um no carrinho,colocou dois e colocou o terceiro. Você, então, clica no botão de listar os itens que estão no carrinho.
Nesse momento, a visão não precisa necessariamente fazer uma requisição para o controle, para que o controle peça a lista de itens para o modelo. Ora, ela pode pedir diretamente para o modelo!Fiquem ligados também que existem diversas visões para cada modelo. Na imagem abaixo,
podemos ver as possíveis interações na Arquitetura MVC!

Para quem quiser conhecer melhor, recomendo os seguintes artigos:

http://www.cfQigolo.com/2oo8/o1/mvc-model-view-controller-e-os-tres-macacos https://r.je/views-are-not-templates.html http://tableless.com.br/mvc-afinal-e-o-que
Por fim, não podemos confundir MVC com MVP (Model-View-Presenter). O O MVP
é uma evolução do MVC que se comunica bidirecionalmente com as outras camadas,evitando que o
Model tenha que se comunicar diretamente com a View sem passar pelo Controller e este último é fundamental para a interação com o usuário. O MVP desacopla as funções e torna a arquitetura ainda mais modular.
A camada Presenter é ciente de tudo o que ocorre nas outras duas camadas e deixa-as cientes do que ela está fazendo; a interação com usuário é feita primariamente pela View, e esta pode delegar ao Presenter determinadas tarefas; há uma relação um-para-um entre estas camadas. Nesta relação, há uma referência do View para o Presenter mas não o oposto.
Não devemos confundir também com o MVVM (Model-View-ViewModel). O MVVM é uma pequena evolução do MVP em um lado e um retrocesso em outro. Nele o ViewModel não está ciente do que ocorre no View, mas este está ciente do que ocorre no ViewModel (como noPadrão de Projeto Observer). No caso do Model, ambos estão cientes do que ocorre em cada um.
O nome se dá porque ele adiciona propriedades e operações ao Model para atenderas necessidades do View, portanto ele cria um novo modelo para a visualização. É possível associar várias Views para um ModelView. É comum que as Views sejam definidas de forma declarativa (HTML/CSS,XAML, etc.). O Data Binding é feito entre a View e o ViewModel.

Com esse padrão é possível reduzir a quantidade de código para manter. Algumas automações são possíveis portertodas as informações necessárias no ViewModel. ViewModel -é só um modelo mais adequado para uma visão específica (ou mais que uma). Pessoal, acredito que isso basta em relação a esses assuntos que só recentemente começaram a ser cobrados.
Arquitetura Distribuída

INCIDÊNCIA EM PROVA: BAIXA

Os sistemas de computação estão passando por uma evolução. Desde 1945, quando começou a era moderna dos computadores, até aproximadamente 1985, os computadores eram grandes e caros.Contudo, mais ou menos a partir de meados da década de 80, dois avanços tecnológicos começaram a mudar essa situação. O primeiro foi o desenvolvimento de microprocessadores de grande capacidade.
O segundo desenvolvimento foi a invenção de redes de computadores de alta velocidade. Nesse cenário, surgem os sistemas distribuídos, os quais são plataformas formadas por um conjunto de computadores independentes que se apresenta a seus usuários como um sistema único e coerente.Uma breve introdução histórica e agora podemos partir para o assunto: a arquitetura mainframe(Grande Porte) é conhecida por ser altamente centralizada.

Todo processamento ocorre no mainframe e há um bocado de terminal burro que o acessa.
Já a
Arquitetura Distribuída inverte essa concepção, na medida em que o processamento é dispersado através da organização e seus desktops e servidores. Professor,quais são as vantagens dessa abordagem? Cara, há ganhos de responsividade, escalabilidade,redundância,
disponibilidade, compartilhamento de recursos, controle e envolvimento do usuário, etc.

Componentes podem ser hospedados em diferentes plataformas e tecnologias, além de se comunicarem por meio de uma rede - sendo que cada nó tem sua responsabilidade específica no processamento de uma tarefa comum. Galera, o usuário nota que 0 processamento é distribuído?Não, é tudo transparente! Para ele, é como se tudo estivesse sendo executado como um único sistema.
Os computadores em um sistema distribuído podem estar fisicamente próximos e conectados por uma rede local ou podem estargeograficamente distantes e conectados por uma rede remota. Uma arquitetura distribuída pode consistir em uma série de configurações possíveis, como mainframes,computadores pessoais, estações de trabalho, minicomputadores e assim por diante. A meta da computação distribuída é fazer um trabalho de rede como um computador único.
Os sistemas de computação distribuída podem ser executados no hardware fornecido por muitos fornecedores e podem utilizar diversos componentes de software baseados em padrões. Esses sistemas são independentes do software subjacente. Eles podem ser executados em vários sistemas operacionais e podem utilizar vários protocolos de comunicação. Algum hardware pode utilizar Unix como o sistema operacional, enquanto outro hardware pode utilizar Windows.
Para comunicação entre máquinas, esse hardware pode utilizar SNA ou TCP/IP em Ethernet ouToken Ring. A imagem seguinte apresenta uma possível arquitetura distribuída descentralizada:

Esse sistema contém duas LANs conectadas entre si. Uma consiste em estações de trabalho UNIX(HP-UX, Solaris, AIX) de vários fabricantes (HP, Sun, IBM); já a outra consiste em
PCs executando vários sistemas operacionais (NT e 2000) em Token Ring. Há uma LAN conectada a um mainframe por meio de uma conexão SNA. Cliente/Servidor e P2P são exemplos famosos de arquitetura distribuída.
Galera, não confundam arquitetura distribuída com arquitetura paralela. No primeiro caso,processos são executados concorrentemente em máquinas diferentes dentro de uma rede; é uma arquitetura fracamente acoplada; é mais imprevisível devido ao uso de redes de computadores e suas falhas; apresenta controle e acesso descentralizado dos recursos. No segundo caso,processos são executados concorrentemente em uma mesma máquina;
Trata-se de uma arquitetura fortemente acoplada, que pode compartilhar hardware ou se comunicar através de um barra mento de alta velocidade; é mais previsível, porque falhas são menos comuns em barramentos de alta velocidade; apresenta controle e acesso centralizado dos recursos;utiliza melhoro poderde processamento; apresenta melhordesempenho e confiabilidade;
permite compartilhar dados e recursos; reutiliza serviços já disponíveis; atende mais usuários; etc.
Claro que nem tudo são flores - há também desvantagens: desenvolver, gerenciar e manter sistemas distribuídos; controlar o acesso concorrente a dados e a recursos compartilhados; evitar que falhas de máquinas ou da rede comprometam o funcionamento do sistema;garantir a segurança do sistema e o sigilo dos dados trocados entre máquinas; lidar com a heterogeneidade do ambiente; entre outros.
Um último conceito sobre esse assunto: Middleware. Um Middleware é uma camada de software que permite que elementos de aplicações interoperem através de redes de computadores -imaginem um software que padroniza interfaces de programação para que você não se preocupe se existem protocolos, arquiteturas, sistemas operacionais ou bancos de dados diferentes. Ele provê um modo para obter dados de um lugar para outro.
Além disso, é capaz de mascarar diferenças existentes entre sistemas operacionais,plataformas de hardware e protocolos de rede. O Middleware oculta do desenvolvedor da aplicação a complexidade do processo de transporte da rede. Os exemplos mais comuns são: RPC,RMI, CORBA, DCOM, etc. Quando utilizamos linguagens orientadas a objetos em arquiteturas distribuídas, chegamos ao conceito de objetos distribuídos e invocação remota.
Como o nome bem diz, objetos distribuídos são instâncias que podem ser acessadas remotamente e trazem para as aplicações distribuídas todas as vantagens da orientação a objetos: maior reusabilidade, segurança, padronização. Nas linguagens estruturadas, as funções remotas são utilizadas a partir de chamadas remotas, as famosas Remote Procedure Call (RPC). Os objetos não possuem funções, mas sim métodos, e não são "chamados", mas invocados.
Alguém consegue descobrir o nome similar ao RPC para objetos distribuídos? Trata-se do
Remote
Method Invocation (RMI). O RMI permite que um objeto executado em uma Java
Virtual
Machine (JVM) possa invocar métodos de outro objeto remoto, ou seja, executado em outra
JVM. RMI permite comunicação remota entre programas escritos na linguagem Java.
Professor,
quer dizer que, de uma máquina eu posso invocar um método de um objeto de outra máquina?

E se eu não tiver acesso ao código remoto? Para isso, utilizamos um recurso muito importante da orientação a objetos: interfaces. Desse modo, basta que o objeto que invoca o objeto distribuído tenha a interface com as assinaturas dos métodos remotos. Além da interface, existe um objeto local que implementa a interface remota, mas na verdade não faz nada além de repassar tudo ao objeto remoto (que também implementa a interface, obviamente).
O nome desse objeto local que implementa a interface remota é o proxy (qualquer semelhança com o padrão de projeto não é mera coincidência). Ah, professor, o senhor QUASE me enganou! Como pode um objeto num local saber onde está o objeto remoto, e como saber qual das classes que implementam a interface remota estão disponíveis para uso? Esse aluno vai passar! Meu querido,você tem toda razão...

Para saber qual objeto implementa o serviço da interface remota a ser invocado e onde ele se encontra, existe um serviço chamado Binder. Ele é responsável por transformar o nome de um serviço remoto que o objeto local quer invocar numa referência real de um objeto distribuído.Os servidores com os objetos distribuídos devem registrar os serviços no Binder para que os clientes possam acessá-los.
Basta que, antes, haja um contrato para que os nomes dos serviços sejam bem conhecidos por todos: clientes, servidores com objetos remotos e Binder. Os objetos remotos do lado do servidor são dois para cada objeto distribuído: skeleton e dispatcher. O skeleton implementa a interface remota, mas ainda não é quem faz o trabalho braçal (que pode ser uma classe "normal"que implementa a interface remota). Já o dispatcherfaz parte do arcabouço para receber as invocações remotas e chamar o skeleton certo.
Proxy (lado cliente), skeleton (lado servidor) e dispatcher (lado servidor) compõe o middleware de um sistema de objetos distribuídos. Em algumas implementações, o skeleton e dispatcher são unidos numa classe. Finalmente, o objeto distribuído, que vai realizar cálculos, acessar bancos de dados e tudo o que o cliente precisar, é acessado pelo Skeleton, que recebe os resultados e faz todo o caminho de volta.
RESUMo

ARQUITETURA DE SOFTWARE

A arquitetura de software de um programa ou sistema computacional é a estrutura ou estruturas do sistema, que abrange os componentes de software, as propriedades externamente visíveis desses componentes e as relações entre eles
COESÃO =

## DIVISÃO DE

ACOPLAMENTO =

## DEPENDÊNCIA DE COMPONENTES

TIPO DE ACOPLAMENTO | DESCRIÇÃO

ACOPLAMENTO
POR CONTEÚDO

ACOPLAMENTO

COMUM

ACOPLAMENTO
POR CONTROLE

ACOPLAMENTO
POR DADOS

ACOPLAMENTO POR
CHAMADAS DE ROTINAS

ACOPLAMENTO POR USO DE

TIPOS

ACOPLAMENTO POR
INCLUSÃO OU IMPORTAÇÃO

ACOPLAMENTO EXTERNO

Ocorre quando um módulo faz uso de estruturas de dados ou de controle mantidas no escopo de outro módulo.
Ocorre quando um conjunto de módulos acessa uma área global de dados.

Ocorre quando módulos passam decisões de controle a outros módulos.

Ocorre quando apenas uma lista de dados simples é passada como parâmetro de um módulo para o outro, com uma correspondência um-para-um de itens.
Ocorre quando uma operação chama outra. Nesse nível de acoplamento, é comum e,
quase sempre, necessário. Entretanto, realmente aumenta a conectividade de um sistema.
Ocorre quando o Componente A usa um tipo de dados definido em um Componente B.
Se a definição de tipo mudar, todo componente que usa a definição também terá de ser alterado.
Ocorre quando um Componente A importa ou inclui um pacote ou o conteúdo do
Componente B.

Ocorre quando um componente se comunica ou colabora com componentes de infraestrutura. Embora seja necessário, deve-se limitar a um pequeno número de componentes em um sistema.
O

Separação de responsabilidades

Decomposição de complexidade \_ * ... .

_\0 Arquitetura em Camadas

Encapsulamento de implementação J

organização ou a estrutura dos componentes signifiet ivos ob 9 st era que interagem por meio de interfaces
Maior reuso e extensibilidade /

programa e dados armazenados em uma única grande máquina -
não havia camadas ® Arquitetura Monolítica

Baixo Acoplamento aplicação rodava na máquina cliente que interagia com umSGBD (servidor de dados)

"fat client" continha toda a Arquitetura em duas camadas lógica de apresentação, )------------------------------------------------------------------
negócio e acesso a dados '

Camada de Apresentação

Camada da Lógica do Negócio \° Arquitetura em três camadas

Arquitetura de
Software

Arquitetura MVC controlador modelo
O comunicação triangular aplicações são conjuntos de serviçosMicrosserviços 0i1 implantações (deploys) independentes pode envolver tecnologias e
\ linguagens heterogêneas

Camada de Acesso a Dados /

browser como cliente universal
(camada de apresentação)

servidor web V
servidor de aplicação /

O Arquitetura Web não existe hierarquia ou exclusividade no fornecimento das informações trafegadas uma arquitetura P2P "pura" não possui servidor dedicado para o fornecimento de informações ou atendimento às requisições todo computador pode funcionar como cliente e/ou servidor ao mesmo tempo
CD hO
CD 00

SERVIDORES
CLIENTES

REDE

Oferecem serviços para outros subsistemas (Ex: Servidores de Impressão, Servidores de
Arquivos, Servidor de Compilação, entre outros).

Solicitam os serviços oferecidos pelos servidores. Geralmente são independentes, podendo ser executados simultaneamente.
Permite aos clientes acessarem esses serviços - quando clientes e servidores podem ser executados em uma única máquina, não são necessários.
Cliente 1 Cliente 2

Cliente 3

Cliente 4

Internet

: 1[ 1[
i

Servidor de X
Catálogos

Catálogo do

Servidor de VídeosArquivos de

Servidor de
Fotografias
Fotografias

Servidor
Web

Info de

Acervo \^Videoclipe J \JDigitalizadas\Filmes e Fotos/

VANTAGENS DE CLIENTES

MAGROS

DESVANTAGENS DE CLIENTES

MAGROS

Baixo custo de administração; facilidade de proteção; baixo custo de hardware; menor custo para licenciamento de softwares; baixo consumo de energia; resistência a ambientes hosts; menor dissipação de calor para o ambiente; mais silencioso que umPC convencional; mais ágil para rodar planilhas complexas; entre outros.

Se o servidor der problema e não houver redundância, todos os clientes-magros ficarão inoperantes; necessita de maior largura de banda na rede em que é empregado; em geral, possui um pior tempo de resposta, uma vez que usam o servidor para qualquertransação; apresenta um apoio transacional menos robusto; etc.
VANTAGENS DE CLIENTES

GORDOS

DESVANTAGENS DE CLIENTES

GORDOS

Necessitam de requisitos mínimos para servidores; apresenta uma performance multimídia melhor; possui maior flexibilidade; algumas situações se beneficiam bastante, tais como jogos eletrônicos, em que se beneficiam por conta de sua alta capacidade de processamento e de hardware específico.
Não há um local central para atualizar e manter a lógica do negócio, uma vez que o código do aplicativo é executado em vários locais de cliente; é exigida uma grande confiança entre o servidor e os clientes por conta do banco de dados; não suporta bem o crescimento do número de clientes.
CAMADA DE
APRESENTAÇÃO

Também chamada de Camada de Interface, possui classes que contêm funcionalidades pa visualização dos dados pelos usuários. Ela tem o objetivo de exibir informações ao usuário e
CAMADA DE

NEGÓCIO

CAMADA DE

DADOS

traduzirações do usuário em requisições às demais partes dos sistemas. O amplo uso da internet tornou as interfaces com base na web crescentemente populares.
Também chamada Camada Lógica ou de Aplicação, possui classes que implementam as regras de negócio no qual o sistema será implantado. Ela realiza cálculos com base nos dados armazenados ou nos dados de entrada, decidindo que parte da camada de acesso de ser ativada com base em requisições provenientes da camada de apresentação.
Possui classes que se comunicam com outros sistemas para realizar tarefas ou adquirir informações para o sistema. Tipicamente, essa camada é implementada utilizando algum mecanismo de armazenamento persistente. Pode haver uma subcamada dentro desta camada chamada Camada de Persistência ou Camada de Acesso.
MODEL

VIEW

CONTROLLER

Essa classe também é responsável por gerenciar e controlar a forma como os dados comportam por meio das funções, lógica e regras de negócios estabelecidas.
Essa camada é responsável por apresentaras informações de forma visual ao usuário. Em j desenvolvimento devem ser aplicados apenas recursos ligados a aparência como mensage botões ou telas.
Essa camada é responsável por intermediar as requisições enviadas pelo View com respostas fornecidas pelo Model, processando os dados que o usuário informou e repassar para outras camadas.
QUESTõES CoMENTADAS - CESPE

í. (CESPE / BNB - 2022) No padrão MVC, o componente de modelo gerencia as requisições dos usuários.
Comentários:

O Modelo é responsável por fornecer os dados para a view e para o controlador. Ele não gerencia as requisições dos usuários. O controlador é responsável por gerenciar as requisições dos usuários e, com base nas informações do modelo, ele processa as requisições e decide a ação a sertomada.
Gabarito: Errado

2. (CESPE / BNB - 2022) Na arquitetura em camadas, os componentes da camada mais interna opera o sistema operacional, ao passo que os da camada mais externa interagem com o usuário.
Comentários:

A arquitetura em camadas é uma abordagem de projeto de sistemas que divide o sistema em diferentes camadas, cada uma responsável por uma função específica. A camada mais interna opera diretamente o hardware e gerencia os recursos de sistema, como processamento,memória,
armazenamento e rede. Esta camada trabalha diretamente com o sistema operacional,
fornecendo o suporte necessário para o funcionamento do sistema. A camada mais externa contém os componentes responsáveis por interagir com o usuário e é responsável por criar a interface de usuário e executar a lógica de aplicativos e processos.
Gabarito: Correto

3. (CESPE / Petrobrás - 2022) Enquanto a arquitetura é responsável pela infraestrutura de alto nível do software, o design é responsável pelo software a nível de código, como, por exemplo, o que cada módulo está fazendo, o escopo das classes e os objetivos das funções.
Comentários:

A arquitetura de um software descreve a estrutura de nível mais alto de uma aplicação e identifica seus principais componentes. No projeto detalhado (design) detalha-se o projeto do software para cada componente identificado na arquitetura.
Gabarito: Correto

4. (CESPE/TJ-RJ - 2021) Na arquitetura MVC (Model-View-Controller), asfuncionalidades de cada segmento são mais bem descritas como:
a) o modelo encapsula as funcionalidades; o view gerencia as requisições dos usuários; o controlador prepara dados do modelo.
b) o modelo encapsula objetos de conteúdo; a visão solicita atualizações do modelo; o controlador seleciona o comportamento do modelo.
c) o modelo incorpora todos os estados; o view gerencia as requisições dos usuários; o controlador encapsula objetos de conteúdo.
d) o modelo encapsula objetos de conteúdo; o view seleciona o comportamento do modelo; o controlador solicita atualizações do modelo.
e) o modelo seleciona a resposta da visão; a visão apresenta a visão selecionada pelo controlador; o controlador encapsula objetos de conteúdo.
Comentários:

O MVC promove a estrita separação de responsabilidades entre componentes de uma interface gráfica. O Modelo é responsável pela representação dos dados, provendo meios de acesso(escrita/leitura), além disso ela encapsula as principais funcionalidades de dados do sistema. Acamada de Visão é responsável pela interação com o usuário, além disso, é possível que a camada de Visão solicite diretamente o estado (atualizações) do Modelo. Por fim, a camada deControle é responsável por receber todas as requisições do usuário, além disso, um controlador define o comportamento da aplicação e interpreta as ações do usuário.
i

Gabarito: Letra B

5- (CESPE / TJ-RJ - 2021) Em um ambiente cliente/servidor, a arquitetura que permite a mesma aplicação assumir tanto o papel de cliente quanto o de servidor é conhecida como arquiteturaC/S:

a) simples.

b) de dois níveis.

c) multinível.

d) de três camadas.

e) par-par.

Comentários:

A arquitetura par-a-par (ou peer-to-peer) trata-se do modelo não hierárquico de rede mais simples em que máquinas se comunicam diretamente, sem passar por nenhum servidordedicado, podendo compartilhar dados e recursos umas com as outras. Nesse tipo de rede, todas as máquinas oferecem e consomem recursos umas das outras, atuando ora como clientes, ora como servidoras.
Gabarito: Letra E

6. (CESPE / TELEBRÁS - 2021) Na arquitetura de software, a arquitetura cliente/servidor tem como vantagem uma maior facilidade de manutenção e segurança dos dados, e como desvantagens possíveis bloqueios no tráfego da rede, além de problemas de atualização da interface de aplicação.
Comentários:

Uma arquitetura cliente/servidor é formada por servidores, que oferecem serviços para outros subsistemas; pelos clientes, que solicitam os serviços oferecidos pelos servidores. Uma das vantagens desse modelo é a manutenção e a segurança dos dados, visto que os servidores podem ter um melhor controle sobre quem acessam os recursos. Já uma das desvantagens desse modelo é que os servidores podem ficar sobrecarregados com o excesso de solicitações pelos clientes,ocasionando bloqueios no tráfego da rede. Outro ponto é sobre a atualização da interface de aplicação, isso pode também paralisara rede.
Gabarito: Correto

7. (CESPE / TELEBRÁS - 2021) Por se tratar de uma arquitetura distribuída, o modelo cliente-servidor pressupõe facilidades para atualizar os servidores de forma transparente, sem que isso afete outras partes do sistema.
Comentários:

Perfeito! Como os servidores são centralizados, e em quantidade menor que os clientes,
há mais facilidade em se administrar as atualizações deles. Em suma, em um modelo cliente-servidor, uma de suas vantagens é a facilidade de manutenção dos servidores.
Gabarito: Correto

8. (CESPE / TRE-BA - 2017) Com referência às arquiteturas multicamadas de aplicações para o ambiente web, assinale a opção correta.
a) Se, na camada de dados, for realizada uma alteração no banco de dados, o restante das camadas também será afetado.
b) O modelo de três camadas recebe essa denominação caso um sistema cliente-servidor seja desenvolvido mantendo-se a camada de negócio do lado do cliente e as camadas de apresentação e dados no lado do servidor.
c) Cada camada é normalmente mantida em um servidor específico para tornar-se o mais escalonável e independente possível em relação a outras camadas, estando entre as suas principais características o eficiente armazenamento e a reutilização de recursos.
d) O objetivo das arquiteturas multicamadas consiste na junção de responsabilidades entre os componentes das aplicações web, de modo a atender aos requisitos funcionais e não funcionais esperados pela aplicação.
e) Na arquitetura de duas camadas — apresentação e armazenamento —, o computador que contiver a base de dados terá de ficar junto com os computadores que executarem as aplicações.
Comentários:

(a) Errado, uma alteração no banco de dados alteraria apenas as classes da camada de dados, mas o restante da arquitetura não seria afetado por essa alteração; (b) Errado,ela recebe essa denominação quando um sistema cliente-servidor é desenvolvido retirando-se a camada de negócio do lado do cliente; (c) Correto. Cada camada desta arquitetura é normalmente mantida em um servidor específico para tornar-se mais escalonável e independente das demais. Cada camada é auto-contida o suficiente de forma que a aplicação pode ser dividida em vários computadores em uma rede distribuída; (d) Errado, o objetivo consiste na separação de responsabilidades entre os componentes das aplicações web, de modo que tenham alta coesão; (e) Errado. Nesta estrutura, a base de dados é colocada em uma máquina específica, separada das máquinas que executavam as aplicações.
Gabarito: Correto

9. (CESPE / STJ - 2015) Na arquitetura em camadas MVC (modelo-visão-controlador), o modelo encapsula o estado de aplicação, a visão solicita atualização do modelo e o controlador gerencia a lógica de negócios.
Comentários:

A questão está errada! O modelo encapsula 0 estado da aplicação? Sim, isso é verdade.
A visão solicita atualização do modelo? Sim, vimos que ela faz isso por meio de eventos que notificam o controlador. O Controlador gerencia a lógica de negócios? Não, quem gerencia a lógica de negócios é o modelo.
Gabarito: Errado

10.(CESPE / MEC - 2015) O controlador gerencia as requisições dos usuários encapsulando as funcionalidades e prepara dados do modelo.
Comentários:

Servidor

I

O controlador gerencia as requisições dos usuários, o modelo encapsula funcionalidades e a visão prepara dados do modelo.
Gabarito: Errado

11. (CESPE / MEC - 2015) A visão encapsula objetos de conteúdo, solicita atualizações do modelo e seleciona o comportamento do modelo.
Comentários:

I
Servidor

L
I

O modelo encapsula objetos de conteúdo, a visão solicita atualizações do modelo e o controle seleciona o comportamento do modelo.
Gabarito: Errado i2.(CESPE / STJ - 2015) No padrão em camadas modelo-visão-controle (MVC), o controle é responsável por mudanças de estado da visão.
Comentários:

O controle é responsável por solicitar mudanças de estado, mas quem realiza a mudança é o modelo.
Gabarito: Errado

13. (CESPE / ANTAQ - 2014) O modelo MVC é um padrão de arquitetura que consiste na definição de camadas para a construção de softwares.
Comentários:

A questão foi extremamente rigorosa e considerou que o Modelo MVC não possui camadas.
Sendo bastante rigoroso, em uma definição acadêmica, ele trata de separação de responsabilidades e,não, de camadas exatamente. Essa é a única questão que eu já vi cobrando esse nível de detalhamento.
Gabarito: Errada i4.(CESPE / ANTAQ - 2014) O controller tem a responsabilidade de armazenar e buscar os dados que deverão ser exibidos pelo view.
Comentários:

Na verdade, essa é uma responsabilidade do modelo.

Gabarito: Errado i5.(CESPE / INPI - 2013) De acordo com os princípios da engenharia de software relacionados à independência funcional, os algoritmos devem ser construídos por módulos visando unicamente ao alto acoplamento e à baixa coesão, caso a interface entre os módulos dê-se pela passagem de dados.
Comentários:

Não, está invertido! Visa-se ao baixo acoplamento e à alta coesão!

Gabarito: Errado i6.(CESPE / STF - 2013) Quanto maior for o número de camadas, menor será o desempenho do software como um todo.
Comentários:

Esse é um assunto polêmico! Em geral, é isso que acontece, isto é, quanto mais camadas, mais overhead. No entanto, há casos em que isso não é válido! Portanto, essa questão caberia recurso.
Gabarito: Correto l-j. (CESPE / STF-2013) Cada camada tem comunicação (interface) com todas as demais camadas,tanto inferiores quanto superiores.

Comentários:

Na verdade, as camadas só possuem comunicação/interface com suas camadas adjacentes.

Gabarito: Errado

I8.(CESPE/STF-2O13) Em uma arquitetura em camadas, a camada de persistência é responsável por armazenar dados gerados pelas camadas superiores e pode utilizar um sistema gerenciador de banco de dados para evitar, entre outros aspectos, anomalias de acesso concorrente dos dados e problemas de integridade de dados.
Comentários:

Questão ótima! Persistência guarda os dados e, sim, pode utilizar um SGBD. Porque?
Porque ele é capaz de tratar concorrência de dados e problemas de integridade! Tudo certinho...
Gabarito: Correto

19.(CESPE / FUB - 2013) Aplicações cliente-servidor multicamadas são usualmente organizadas em três camadas principais: apresentação, lógica e periférico.
Comentários:

Na verdade, é apresentação, lógica e dados.

Gabarito: Errado

20.(CESPE/ FUB-2013) Entre as desvantagens de se executartodas as camadas de uma aplicação cliente-servidor no lado do servidor se destaca a dificuldade de atualização e correção da aplicação.
Comentários:

Primeiro, se todas as camadas de uma aplicação cliente-servidor são executados no servidor, então não é uma arquitetura cliente-servidor. Executar a maioria das camadas no lado do cliente é uma dificuldade de atualização e correção de aplicação, na medida em que é necessária fazer essa manutenção em todas as máquinas clientes.
Gabarito: Errado

2i. (CESPE / BACEN -2013) MVC (Model-View-Controller) é um modelo de arquitetura de software que separa, de um lado, a representação da informação e, de outro, a interação do usuário com a informação.
Comentários:

A camada de visão trata da representação da informação e a camada de controle trata da interação do usuário com a informação (modelo).
Gabarito: Correto

22. (CESPE /TCE-ES - 2013) No Padrão MVC, as regras do negócio que definem a forma de acesso e modificação dos dados são geridas pelo controlador.
Comentários:

Na verdade, essa é uma função do modelo.

Gabarito: Errado

23.(CESPE / Banco da Amazônia - 2012) De acordo com o princípio da coesão de classes, cada classe deve representar uma única entidade bem definida no domínio do problema. O grau de coesão diminui com o aumento contínuo de código de manutenção nas classes.
Comentários:

Uma classe deve ter uma única responsabilidade e executá-la de maneira satisfatória.
Além disso,
o grau de coesão tende a diminuir com o aumento contínuo de código de manutenção nas classes,mas isso não é regra.

Gabarito: Correto

24.(CESPE / Banco da Amazônia - 2012) O acoplamento de métodos expressa o fato de que qualquer método deve ser responsável somente por uma tarefa bem definida.
Comentários:

Acoplamento? Não! Na verdade, é a coesão!

Gabarito: Errado

25-(CESPE / CET - 2011) No padrão de desenvolvimento modelo-visualização-controlador
(MVC),
o controlador é o elemento responsável pela interpretação dos dados de entrada e pela manipulação do modelo, de acordo com esses dados.
Comentários:

Ele é responsável pelo fluxo da aplicação e, por isso, é o responsável pela interpretação dos dados de entrada e pela manipulação do modelo.
Gabarito: Correto

26.(CESPE / MEC - 2011) O modelo MVC pode ser usado para construir a arquitetura do software a partir de três elementos: modelo, visão e controle, sendo definidas no controle as regras de negócio que controlam o comportamento do software a partir de restrições do mundo real.
Comentários:

Regras de negócio ficam no modelo; o controlador só orquestra as solicitações vindas da visão para o modelo.
Gabarito: Errado

27. (CESPE / MEC - 2011) O controlador, no modelo MVC, realiza a comunicação entre as camadas de visão e modelo.
Comentários:

Perfeito! O controlador realmente realiza a comunicação entre as camadas de visão e modelo.

Gabarito: Correto

28. (CESPE / MEC - 2011) No MVC, o modelo representa o estado geral do sistema.

Comentários:

É realmente no modelo que se encontram os dados (estado) do sistema.

Gabarito: Correto

29. (CESPE / MEC - 2011) Apesar do seu amplo emprego em aplicações web, o MVC deve ser utilizado apenas em interfaces gráficas em função de sua arquitetura de componentes.
Comentários:

Quando ela começou nem existiam aplicações web. Ele é usado primariamente em interfaces gráficas, mas não se limita a isso!
Gabarito: Errado

3O.(CESPE / MEC - 2011) No MVC, é o modelo que permite apresentar, de diversas formas diferentes, os dados para o usuário.
Comentários:

Opa... essa é uma função da visão!

Gabarito: Errado

31. (CESPE / MEC - 2011) O controlador é o responsável pelas regras de negócio e pelos dados de uma aplicação no MVC.
Comentários:

Na verdade, essa é uma função do Modelo.

Gabarito: Errado

32.(CESPE / MEC - 2011) A independência dos componentes é um dos atributos que reflete a qualidade do projeto. O grau de independência pode ser medido a partir dos conceitos de acoplamento e coesão, os quais, idealmente, devem ser alto e baixo, respectivamente.
Comentários:

Na verdade, é o contrário! Devem ser baixo e alto, respectivamente.

Gabarito: Errado

33.(CESPE / MEC -2011) O termo cliente é usado para designar uma parte distinta de um sistema de computador que gerencia um conjunto de recursos relacionados e apresenta sua funcionalidade para usuários e aplicativos.
Comentários:

Na verdade, a questão trata de um serviço!

Gabarito: Errado

34-(CESPE / MEC - 2011) A arquitetura cliente/servidor proporciona a sincronização entre duas aplicações: uma aplicação permanece em estado de espera até que outra aplicação efetue uma solicitação de serviço.
Comentários:

Exato! A redação é meio complicada, mas o que essa questão quis dizer é: uma aplicação (servidor)fica em estado de espera aguardando solicitações e outra aplicação (cliente) efetua a solicitação de serviços.
Gabarito: Correto

35. (CESPE / MEC - 2011) A arquitetura cliente/servidor enseja o desenvolvimento de um sistema com, no máximo, duas camadas, quais sejam, cliente e servidor.
Comentários:

Na verdade, pode ter quantas camadas forem necessárias.

Gabarito: Errado

36.(CESPE / ABIN - 2010) Em sistemas de grande porte, um único requisito pode ser implementado por diversos componentes; cada componente, por sua vez,pode incluir elementos de vários requisitos, o que facilita o seu reúso, pois os componentes implementam,normalmente, uma única abstração do sistema.

Comentários:

Vocês se lembram da coesão e acoplamento? Um componente que inclui elementos de vários requisitos tem baixa coesão, reduzindo sua reusabilidade.
Gabarito: Errado

37. (CESPE / INMETRO - 2010) A coesão e o acoplamento são formas de se avaliar se a segmentação de um sistema em módulos ou em componentes foi eficiente. Acerca da aplicação desses princípios, assinale a opção correta.
a) O baixo acoplamento pode melhorar a manutebilidade dos sistemas, pois ele está associado à criação de módulos como se fossem caixas-pretas.
b) Os componentes ou os módulos devem apresentar baixa coesão e um alto grau de acoplamento.
c) Os componentes ou os módulos devem serfortemente coesos e fracamente acoplados.

d) Um benefício da alta coesão é permitir realizar a manutenção em um módulo sem se preocupar com os detalhes internos dos demais módulos.
e) A modularização do programa em partes especializadas pode aumentar a qualidade desses componentes, mas pode prejudicar o seu reaproveitamento em outros programas.
Comentários:

(a) Errado. Na verdade, essa é uma função da coesão e, não, do acoplamento; (b)
Errado. Os componentes ou os módulos devem apresentar alta coesão e baixo grau de acoplamento; (c)Correto. Essa é a regra geral: alta coesão e baixo acoplamento; (d) Errado. Esse é um benefício do baixo acoplamento; (e) Errado. Pelo contrário, quanto mais especializado, maior a coesão e maior a probabilidade de reaproveitamento em outros programas.
Gabarito: Correto

38.(CESPE / BASA - 2010) Nessa arquitetura (arquitetura multicamadas),
quando são consideradas três camadas, a primeira camada deve ser implementada por meio do servidor de aplicação.
Comentários:

Por lógica, a primeira camada seria a Camada de Usuário ou a Camada de Dados. A
Camada de
Aplicaçãojamais seria a primeira camada.

Gabarito: Errado

3g.(CESPE / BASA - 2010) Em arquitetura multicamadas, o servidor de aplicação nada mais é do que um programa que fica entre o aplicativo cliente e o sistema de gerenciamento de banco de dados.
Comentários:

É exatamente isso! Ele está entre a interface e os dados.

Gabarito: Correto

ZjO.(CESPE / BASA - 2010) Uma desvantagem dessa arquitetura (arquitetura multicamadas) é o aumento na manutenção da aplicação, pois alterações na camada de dados, por exemplo,acarretam mudanças em todas as demais camadas.

Comentários:

Não, a divisão em camadas reduz a manutenção da aplicação.

Gabarito: Errado

4i.(CESPE / BASA - 2010) Em uma arquitetura cliente-servidor, os clientes compartilham dos recursos gerenciados pelos servidores, os quais também podem, por sua vez, ser clientes de outros servidores.
Comentários:

Exato! Os servidores gerenciam seus recursos que são compartilhados pelas dezenas,
milhares,
milhões de clientes. Além disso, um servidor pode acabar sendo um cliente de outro servidor.

Gabarito: Correto

42.(CESPE / BASA - 2010) A Internet baseia-se na arquitetura cliente-servidor, na qual a parte cliente, executada no host local, solicita serviços de um programa aplicativo denominado servidor, que é executado em um host remoto.
Comentários:

Exato! A internet é isso: uma arquitetura cliente-servidor distribuída em que a parte cliente é executada no host local e solicita serviços de diversos servidores, que são executados em um host remoto.
Gabarito: Correto

43.(CESPE / BASA - 2010) A arquitetura cliente-servidor viabiliza o uso simultâneo de diferentes dispositivos computacionais, do seguinte modo: cada um deles realiza a tarefa para a qual é mais capacitado, havendo a possibilidade de uma máquina ser cliente em uma tarefa e servidor em outra.
Comentários:

Apesar de a redação da questão estar confusa ("tarefa para a qual é mais capacitado"), a questão está certa em afirmar que uma máquina pode ser cliente em uma aplicação e servidora em outra.
Gabarito: Correto

44-(CESPE I EMBASA - 2010) O MVC promove a estrita separação de responsabilidades entre os componentes de uma interface.
Comentários:

Essa questão foi anulada, porque ela não especificou qual tipo de interface.
Considerando tratar-se de interface gráfica, a questão seria correta.
Gabarito: Anulada

45.(CESPE / EMBASA - 2010) No MVC, a visão é responsável pela manutenção do estado da aplicação.
Comentários:

Na verdade, a questão trata da Camada de Modelo.

Gabarito: Errado

Zj6.(CESPE / EMBASA - 2010) O modelo no MVC tem como atribuição exibir a parte que é responsável pela manutenção da aplicação para o usuário.
Comentários:

Na verdade, essa atribuição é da camada de visão.

Gabarito: Errado

47. (CESPE/ EMBASA-2010) O controladoré responsável pela coordenação entre atualizações no modelo e interações com o usuário.
Comentários:

Essa é realmente uma das responsabilidades do controlador.

Gabarito: Correto

48.(CESPE / EMBASA- 2010) Por meio do MVC, é possível o desenvolvimento de aplicações em 3camadas para a Web.

Comentários:

Perfeito! Ela realmente permite o desenvolvimento de aplicações em três camadas para a web.

Gabarito: Correto

49.(CESPE / UNIPAMPA - 2009) Normalmente, a arquitetura em três camadas conta com as camadas de apresentação, de aplicação e de dados.
Comentários:

Exato! Arquitetura em Três Camadas: Apresentação, Aplicação e Dados.

Gabarito: Correto

50. (CESPE / UNIPAMPA - 2009) Em uma arquitetura em três camadas, na camada de aplicação,usualmente está um servidor de banco de dados que gerencia o conjunto de requisições.

Comentários:

Não, o Servidor de Banco de Dados usualmente se encontra na Camada de Dados.

Gabarito: Errado

51. (CESPE/ UNIPAMPA-2009) O uso de middlewares é comum em aplicações de n camadas.

Comentários:

Exato! Utilizam-se middlewares para realizar uma comunicação mais eficiente.

Gabarito: Correto

52. (CESPE / UNIPAMPA - 2009) Na camada de persistência dos dados em aplicações n camadas,podem ser utilizados o banco de dados orientado a objetos e o banco de dados relacionais.

Comentários:

É isso aí! É independente desse tipo de tecnologia.

Gabarito: Correto

53. (CESPE / UNIPAMPA - 2009) Nas aplicações cliente-servidor, em duas camadas, é simples acessarfontes de dados heterogêneas porque o legado de base de dados não precisa de drivers de conexões diferentes.
Comentários:

Na verdade, é necessário diversos drivers de conexões diferentes para acessar às bases de dados de fontes heterogêneas e não é simples! Em uma arquitetura cliente-servidor de três camadas,continua sendo necessário os drivers de conexões diferentes, porém é mais simples por haver uma camada responsável por gerenciar essas conexões.
Gabarito: Errado

54.(CESPE / ANTAQ - 2009) Os principais componentes da arquitetura cliente-servidor, que é um modelo de arquitetura para sistemas distribuídos, são o conjunto de servidores que oferecem serviços para outros subsistemas, como servidores de impressão e servidores de arquivos,o conjunto de clientes que solicitam os serviços oferecidos por servidores, e a rede que permite aos clientes acessarem esses serviços.
Comentários:

Perfeito, são clientes, servidores e uma rede que permite a comunicação.

Gabarito: Correto

55.(CESPE / BASA - 2009) Em arquiteturas cliente-servidor multicamadas, na maior parte das aplicações, o browser é adotado como cliente universal.
Comentários:

Sim, pessoal! Nessa arquitetura, o browser (navegador) geralmente é o cliente.

Gabarito: Correto

S6.(CESPE / ANAC - 2009) O framework modelo visão controlador (MVC - model view controller)é muito utilizado para projeto da GUI (graphical user interface) de programas orientados a objetos.
Comentários:

Perfeito! Foi nesse contexto que ele foi criado e com esse objetivo.

Gabarito: Correto

57-(CESPE / TCU - 2009) No MVC (model-view-controller), um padrão recomendado para aplicações interativas, uma aplicação é organizada em três módulos separados.Um para o modelo de aplicação com a representação de dados e lógica do negócio, o segundo com visões que fornecem apresentação dos dados e input do usuário e o terceiro para um controlador que despacha pedidos e controle de fluxo.
Comentários:

Perfeito! O MVC promove a estrita separação de responsabilidade entre componentes de uma interface gráfica onde temos componentes responsáveis pela manutenção do estado da aplicação,denominado de Modelo, pela exibição de parte deste modelo para o usuário, ao que chamamos deVisão e pela coordenação entre atualizações no modelo e interações com o usuário,
feita através do Controlador.
Gabarito: Correto

58.(CESPE/ANATEL-2oog) Uma das vantagens da arquitetura distribuída é o compartilhamento de recursos, que permite que sistemas, aplicativos e dispositivos periféricos,como discos,
impressoras, arquivos, estejam associados a diferentes computadores em uma rede.
Uma segunda vantagem é a concorrência, uma vez que vários processos podem operar ao mesmo tempo em diferentes computadores na rede. E, por fim, uma terceira vantagem é a proteção,pois o acesso é feito de forma centralizada.

Comentários:

Opa... o acesso é feito de forma descentralizada.

Gabarito: Errado

5g.(CESPE/ ANTAQ-2009) Uma das desvantagens da arquitetura distribuída é sua complexidade,
uma vez que é mais difícil compreender as propriedades emergentes dos sistemas que as dos sistemas centralizados.
Comentários:

É realmente complexo compreender e controlar as propriedades de sistemas distribuídos. Já imaginaram controlaras propriedades de concorrência e transação de um sistema que está distribuído?Pois é!

Gabarito: Correto

6o.(CESPE / INMETRO - 2009) Em uma arquitetura distribuída, middleware é definido como uma camada de software cujo objetivo é mascarar a heterogeneidade e fornecer um modelo de programação conveniente para os programadores de aplicativos. Como exemplos de middlewares é correto citar: Sun RPC, CORBA, RMI Java e DCOM da Microsoft.
Comentários:

Perfeito! Middleware é uma camada de software que permite que elementos de aplicações interoperem através de redes de computadores. Ele oculta do desenvolvedor da aplicação a complexidade do processo de transporte da rede. Os exemplos mais comuns são:RPC, RMI,
CORBA, DCOM, etc.

Gabarito: Correto

6i.(CESPE / IPEA-2008) Na arquitetura cliente-servidor com três camadas (three tier), a camada de apresentação, a camada de aplicação e o gerenciamento de dados ocorrem em diferentes máquinas. A camada de apresentação provê a interface do usuário e interage com o usuário,sendo máquinas clientes responsáveis pela sua execução. A camada de aplicação é responsável pela lógica da aplicação, sendo executada em servidores de aplicação. Essa camada pode interagir com um ou mais bancos de dados ou fontes de dados. Finalmente, o gerenciamento de dados ocorre em servidores de banco de dados, que processam as consultas da camada de aplicação e enviam os resultados.
Comentários:

Questão perfeita! Refere-se a Camadas Físicas (Tiers), portando cada camada está localizada em uma máquina.
Gabarito: Correto

62. (CESPE / STJ - 2008) A arquitetura de um sistema de software pode se basear em determinado estilo de arquitetura. Um estilo de arquitetura é um padrão de organização. No estilo cliente-servidor, o sistema é organizado como um conjunto de serviços, servidores e clientes associados que acessam e usam os serviços. Os principais componentes desse estilo são servidores que oferecem serviços e clientes que solicitam os serviços.
Comentários:

Exato! Trata-se de um conjunto de clientes e servidores que acessam e fornecem diversos serviços.

Gabarito: Correto

63.(CESPE / TJ-CE - 2008) A arquitetura MVC fornece uma maneira de dividir a funcionalidade envolvida na manutenção e apresentação dos dados de uma aplicação web.
Comentários:

O MVC promove a estrita separação de responsabilidade entre componentes de uma interface gráfica onde temos componentes responsáveis pela manutenção do estado da aplicação,denominado de Modelo, pela exibição de parte deste modelo para o usuário, ao que chamamos deVisão e pela coordenação entre atualizações no modelo e interações com o usuário,
feita através do Controlador
Gabarito: Correto

64.(CESPE / TJ-CE - 2008) A arquitetura MVC foi desenvolvida recentemente para mapear as tarefas complexas de saída do sistema do usuário.
Comentários:

Durante a década de setenta, surgiu a necessidade de criação de uma arquitetura para ser utilizada em projetos de interface visual na linguagem de programação Smalltalk. Aideia original era organizar o código, separar responsabilidades, aumentar a manutenibilidade,promover um baixo acoplamento e uma alta coesão, fomentar a reusabilidade do código e tornar o sistema escalável
Gabarito: Errado

65.(CESPE / TJ-CE - 2008) Na arquitetura MVC, um controlador define o comportamento da aplicação, já que este é o responsável por interpretar as ações do usuário e as relaciona com as chamadas do modelo.
Comentários:

Ele realmente interpreta ações do usuário e direciona para as chamadas do modelo.

Gabarito: Correto

66. (CESPE / TJ-CE - 2008) A arquitetura MVC não separa a informação de sua apresentação,porque, em sistemas web, informação e apresentação estão na mesma camada.

Comentários:

Ela separa a informação (Modelo) da apresentação (Visão).

Gabarito: Errado

67.(CESPE / TJ-CE - 2008) O desenvolvimento de sistemas web ocorre tipicamente em três camadas. A arquitetura MVC aumenta o escopo do desenvolvimento para, no máximo, quatro camadas, sendo a quarta camada o processamento dos dados do usuário.
Comentários:

Não, tipicamente temos três camadas. No entanto, realmente não há restrição de escopo para quatro camadas. Pode-se acrescentar outras camadas principalmente nas camadas de controle e visão.
Gabarito: Errado

68. (CESPE / IPEA - 2008) A arquitetura distribuída é caracterizada pelo compartilhamento de recursos computacionais e serviços por meio da comunicação direta e descentralizada entre os sistemas envolvidos e inclui, entre outras coisas, a troca de informações, ciclos de processamento e espaço de armazenamento em disco.
Comentários:

Ela se caracteriza por seu compartilhamento de recursos e serviços-além da comunicação direta e descentralizada entre os sistemas. Enfim, a questão está perfeita!
Gabarito: Correto

69. (CESPE / SERPRO - 2008) Uma arquitetura distribuída permite a divisão de uma mesma tarefa em diferentes processadores em uma mesma CPU. Essa característica aumenta a velocidade de processamento de uma informação.
Comentários:

Não se deve confundir Arquitetura Distribuída com Arquitetura Paralela. Observem que, no caso apresentado, não há uma rede de computadores - tudo ocorre em um uma mesma CPU!Logo, a questão trata de Arquitetura Paralela.
Gabarito: Errado

70.(CESPE /TCU - 2007) A arquitetura cliente-servidor tem por motivação sincronizar a execução de dois processos que devem cooperar um com outro. Assim, dadas duas entidades que queiram comunicar-se, uma deve iniciar a comunicação enquanto a outra aguarda pela requisição da entidade que inicia a comunicação.
Comentários:

Parece complicado, mas é simples! Uma entidade começa a comunicação e a outra aguarda a requisição da entidade iniciadora.
Gabarito: Correto

7i.(CESPE / DATAPREV - 2006) Uma arquitetura cliente/servidor caracteriza-se pela separação do cliente, o usuário que acessa ou demanda informações, do servidor. Um exemplo típico é um navegador que acessa páginas na Internet. É uma arquitetura que permite o acesso a serviços remotos através de rede de computadores, e que tem como principal deficiência a falta de escalabilidade.
Comentários:

Na verdade, um dos benefícios da arquitetura cliente/servidor é a escalabilidade.

Gabarito: Errado

72.(CESPE / DATAPREV - 2006) Arquiteturas cliente/servidor podem ser decompostas em mais de duas camadas. Uma configuração muito utilizada é aquela em que os clientes acessam informações por meio de servidores de aplicação, que por sua vez acessam servidores de banco de dados. Este tipo de arquitetura é conhecida como arquitetura em 3 camadas, ou three-tier.
Comentários:

Exato! O usuário utiliza um servidor de aplicação que acessa um servidor de banco de dados.

Gabarito: Correto

73.(CESPE/CENSIPAM-2Oo6) O padrão MVC organiza um software em modelo, visão e controle.
O modelo encapsula as principais funcionalidades e dados. As visões apresentam os dados aos usuários. Uma visão obtém os dados do modelo via funções disponibilizadas pelo modelo;só há uma visão para um modelo. Usuários interagem via controladoras que traduzem os eventos em solicitações ao modelo ou à visão; podem existir várias controladoras associadas a uma mesma visão.
Comentários:

Opa... pode haver várias visões para um modelo.

Gabarito: Errado

74.(CESPE / CENSIPAM - 2006) No padrão MVC, se um usuário modifica o modelo, as visões que dependem desse modelo refletem essas modificações, pois o modelo notifica as visões quando ocorre uma modificação nos seus dados. Portanto, é usado um mecanismo para propagação de modificações que mantém um registro dos componentes que dependem do modelo.
Comentários:

Mudanças em um modelo podem modificar as visões que dependem desse modelo, gerando uma rastreabilidade.
Gabarito: Correto

75.(CESPE / SEAD-PA - 2004) Em um modelo cliente-servidor em que o processamento é concentrado nos clientes e o armazenamento concentrado no servidor, observa-se uma baixa carga de tráfego na rede.
Comentários:

É um caso de Cliente-Gordo, em que o tráfego na rede é menor. No entanto nada garante que o tráfego na rede será baixo, ele pode ser altíssimo, porém é menor comparado ao Cliente-Magro.
Gabarito: Correto

76.(CESPE / SERPRO - 2004) Uma das vantagens da arquitetura cliente-servidor é que parte da carga de processamento é retirada do servidor e colocada nos vários clientes.
Comentários:

Essa é uma das grandes vantagens da arquitetura cliente-servidor. Ela retira uma parte do processamento dos serviços (desonerando o servidor) e transfere para os clientes.
Gabarito: Correto

77. (CESPEI STJ - 2004) As camadas da arquitetura cliente-servidor de três camadas são: camada de interface de usuário, camada de regras de negócio e camada de acesso ao banco de dados.
Comentários:

Esses nomes mudam bastante, mas a questão está certa!

Gabarito: Correto

78.(CESPE/ STJ -2004) Na arquitetura cliente-servidor multicamadas, uma alteração na camada de acesso aos dados não afeta a camada de interface de usuário, desde que essas camadas estejam na mesma máquina.
Comentários:

Na verdade, mesmo que essas camadas estejam na mesma máquina, uma alteração na camada de acesso aos dados não afeta a camada de interface de usuário.
Gabarito: Errado

79. (CESPE / STJ - 2004) A arquitetura cliente-servidor multicamadas possui a vantagem de que a camada de interface de usuário pode se comunicar diretamente com qualquer outra camada,ou seja, não existe hierarquia entre camadas.

Comentários:

Não, a camada de interface se comunica diretamente apenas com a camada de negócio.

Gabarito: Errado

80. (CESPE / TRE-RS - 2003) Aplicações com arquitetura cliente-servidor são assimétricas, no sentido de que o cliente e o servidor possuem papéis diferentes na arquitetura de comunicações.
Comentários:

Perfeito, eles possuem papéis distintos.

Gabarito: Correto

8i.(CESPE / TRE-RS - 2003) O servidor, por possuir normalmente um hardware mais robusto,sempre deve executara parte mais pesada do processamento.

Comentários:

Não! Por exemplo, quando se utiliza um cliente-gordo, a maior parte do processamento ocorre no cliente e, não, no servidor.
Gabarito: Errado

82.(CESPE / TRE-RS - 2003) Do ponto de vista das funcionalidades de usuários, o servidor não precisa necessariamente de uma interface de usuário.
Comentários:

Perfeito, percebam que foi dito "do ponto de vista das funcionalidades de usuários".
Uma vez que sejam executadas as funcionalidades esperadas, não há necessidade de uma interface de usuário.
Gabarito: Correto

QUESTõES CoMENTADAS - FCC

í. (FCC / TRF3 - 2019) Os conceitos alta coesão e baixo acoplamento, utilizados no processo de desenvolvimento de software, são princípios essenciais de:
a) Abstração.

b) Modularidade.

c) Incrementação.

d) Separação de Interesses.

e) Generalidade.

Comentários:

De acordo com Pressman: "Na modularidade 0 software é dividido em componentes separadamente especificados e localizáveis, algumas vezes denominados módulos, que são integrados para satisfazer os requisitos de um problema". Essa divisão em módulos facilita a compreensão e,consequentemente, reduz o custo necessário para se construir um software.

Como a coesão trata da divisão de responsabilidades e o acoplamento do nível de dependência entre os módulos, desejamos uma alta coesão e um baixo acoplamento em processo de modularização.
Gabarito: Letra B

2. (FCC/DPE-AM-2018)

Trecho 1:

public int pensaoAlimenticia(){

return Util.getFuncoes.getFuncoesData.calculaPensao(processo);

Trecho 2:

public int pensaoAlimenticia(){

return Util.calculaPensao(processo);

}

Em um sistema Orientado a Objetos bem desenvolvido, os princípios relativos a acoplamento e coesão devem ser respeitados. O código Java apresentando no trecho 1 mostra um exemplo de a) baixo acoplamento e o trecho 2 o corrige para alto acoplamento.
b) alta coesão e o trecho 2 o corrige para baixa coesão.

c) alto acoplamento e o trecho 2 o corrige para baixo acoplamento.

d) baixo acoplamento e o trecho 2 mostra um exemplo de baixa coesão.

e) baixa coesão e o trecho 2 mostra um exemplo de alto acoplamento.

Comentários:

O acoplamento trata do nível de dependência entre módulos ou componentesde um software.
Dito isso, podemos analisar os trechos de código:
O trecho ítrata da função pensãoAlimenticia(), em que há grande dependência de outros métodos no retorno; já no trecho 2, essa mesma função é construída, mas com menos dependência em relação ao trecho 1. Logo, há alto acoplamento no trecho 1 e baixo acoplamento no trecho 2.
Gabarito: Letra C

3. (FCC / TCM-GO - 2015 - Adaptada) Quanto à Arquitetura em 3 Camadas, é necessário um arranjo que possibilite a reutilização do código e facilite sua manutenção e seu aperfeiçoamento. Deve- se separar Apresentação, Regra de Negócio e Acesso a Dados.Busca-
se a decomposição de funcionalidades de forma a permitir aos desenvolvedores concentrarem-se em diferentes partes da aplicação durante a implementação.

Comentários:

Perfeito! Essa é uma situação bastante comum em uma arquitetura em três camadas.

Gabarito: Letra C

4. (FCC / CNMP - 2015) Há algumas variantes possíveis de arquitetura a serem utilizadas em um sistema de bancos de dados. Sobre essas variantes, é correto afirmar que:
a) na arquitetura de 3 camadas, não há uma camada específica para a aplicação.

b) a camada de apresentação da arquitetura de 2 camadas situa-se, usualmente, no servidor de banco de dados.
c) na arquitetura de 3 camadas, a camada de servidor de banco de dados é denominada cliente.

d) a arquitetura de 3 camadas é composta pelas camadas cliente, aplicação e servidor de banco de dados.
e) na arquitetura de 2 camadas não há necessidade de uso de um sistema gerenciadorde bancos de dados.
Comentários:

(a) Errado, é a camada intermediária; (b) Errado, fica na camada de apresentação; (c)
Errado, é chamada camada de dados; (d) Correto; (e) Errado, é claro que há necessidade.
Gabarito: Letra D

5. (FCC/TJ-AP-2014) Uma arquitetura muito comum em aplicações web é o Modelo
Arquitetural
3 Camadas:

I. Camada de Persistência.

II. Camada de Lógica de Negócio.

III. Camada de Apresentação.

Neste modelo, a correta associação dos componentes com as camadas é:

a) l-Servidor de Banco de Dados - ll-Servidor de Aplicação -1 ll-Máq ui na Cliente.

b) l-Servidor Web - ll-Servidor Cliente -1ll-Servidor de Aplicação.

c) l-Servidor Web - ll-Servidor de Banco de Dados - lll-Máquina Cliente.

d) l-Servidor de Banco de Dados - ll-Máquina Cliente - IIl-Servidor de Aplicação.

e) l-Máquina Cliente - ll-Servidor de Banco de Dados - lll-Servidor Web.

Comentários:

Servidor de Banco de Dados se associa com... Camada de Persistência;
Servidor de Aplicação se associa com... Camada de Lógica de Negócio;
Máquina Cliente se associa com... Camada de Apresentação.

Gabarito: Letra A

6. (FCC / TST - 2012) Uma arquitetura em camadas:

a) possui apenas 3 camadas, cada uma realizando operações que se tornam progressivamente mais próximas do conjunto de instruções da máquina.
b) tem, na camada mais interior, os componentes que implementam as operações de interface com o usuário.
c) pode ser combinada com uma arquitetura centrada nos dados em muitas aplicações de bancos de dados.
d) tem, como camada intermediária, o depósito de dados, também chamado de repositório ou quadro-negro.
e) tem, na camada mais externa, os componentes que realizam a interface com o sistema operacional.
Comentários:

(a) Errado. Não necessariamente possui três camadas - pode possuir 2, 3, 4, 5, etc;
(b) Errado.
Interface com o usuário é, em geral, na camada mais externa; (c) Correto. Não há nada que impeça isso; (d) Errado. O depósito de dados, em geral, fica na camada mais interna; (e)Errado. Interface com o sistema operacional, em geral, fica na camada mais interna.
Gabarito: Letra C

7. (FCC / TRF2 - 2012) São aspectos que podem caracterizar uma arquitetura cliente-servidor,estabelecida logicamente em 4 camadas:

I. A camada Cliente contém um navegador de Internet, caracterizado como cliente universal.

II. A camada de Lógica do Negócio se quebra em duas: camada de Aplicação e camada Web, em que o servidor Web representa a camada de Apresentação.
III. Na camada de Lógica do Negócio, o servidor de aplicação passa a utilizar middleware, para suporte a thin clients (PDA, celulares, smart cards, etc) e soluções baseadas em componentes,tais como, J2EE e .Net.

IV. Se, de um lado, a camada de Aplicação estabelece uma interface com a camada de
Dados,
do outro o faz com a camada Web e com os thin clients da camada Cliente.

Está correto o que consta em:

a) I e II, apenas.

b) III e IV, apenas.

c) I, II e III, apenas.

d) II, III e IV, apenas.

e) 1,11, III e IV.

Comentários:

(I) Correto. Na Arquitetura em 4 Camadas, a Camada Cliente contém um navegador,
caracterizado como cliente universal; (II) Errado. Camada de Lógica de Negócio é a Camada deAplicação e a
Camada Web não faz parte dela. Eu nunca ouvi falar nisso, mas a FCC disse que é correto! Adiferença entre a Arquitetura em 4 Camadas e 3 Camadas é que a Apresentação não fica mais no cliente e, sim, na Camada Web. (III) Errado. Imagino que o middleware à que a questão se refere é o Servidor Web, mas ele ficaria na Camada Web fazendo o meio-campo para suportar thin clients e, não, na Camada de Lógica de Negócio -a FCC discorda! (IV) Correto. A Camada deAplicação fica entre a Camada de Dados e a Camada Web.
Gabarito: Letra E

8. (FCC/TST-2012) No padrão MVC é possível definir grupos de componentes principais:
o Model
(Modelo), o View (Apresentação) e o Controller (Controle). Deve fazer parte do componente:

a) Controller, uma classe que contém um método com a finalidade de calcular o reajuste de salário dos funcionários.
b) View, uma classe que contém um método para persistir o salário reajustado de um funcionário.
c) Controller, as animações desenvolvidas em Flash.

d) View, as validações necessárias ao sistema, geralmente definidas através de um conjunto de comparações.
e) Model, as classes com métodos conhecidos como setters e getters e que representam tabelas do banco de dados.
Comentários:

(a) Errado, isso deve fazer parte do Model; (b) Errado, isso deve fazer parte do
Model; (c) Errado,
isso deve fazer parte da View; (d) Errado, isso deve fazer parte da Model; (e) Correto,
esses métodos de fato devem estar na Model.
Gabarito: Letra A

g. (FCC / MPE-AP - 2012) Em uma Aplicação Web desenvolvida utilizando o design pattern MVC,as páginas HTML e as classes com métodos que acessam o banco de dados e executam instruções SQL são representadas, respectivamente, nos componentes:
a) Presentation e Business.

b) View e Model.

c) Controller e Model.

d) Model e Business.

e) View e Business.

Comentários:

Páginas HTML são representadas na View; classes com métodos que acessam o banco de dados e executam instruções SQL são representadas na Model.
Gabarito: Letra B

io.(FCC / MPE-PE - 2012) O padrão de projeto utilizado em aplicações WEB que permite separar as páginas e classes da aplicação em três grupos (muitas vezes chamados de camadas)conhecidos como Apresentação, Controle e Modelo é denominado de:

a) 3-tier.

b) DAO.

c) MVC.

d) DTO.

e) DBO.

Comentários:

Só pode ser... MVC!

Gabarito: Letra C

n.(FCC / TRT-PE - 2012) O padrão de arquitetura MVC é um modelo de camadas que divide a aplicação em três componentes: Model (modelo), View (visualizador) e Controller(controlador).
As funções de cada um destes três componentes são apresentadas abaixo:

I. interpreta eventos de entrada e envia requisições para o modelo de dados; em seguida,processa os dados carregados a partir do modelo e envia para o visualizador.

II. encapsula o acesso aos dados e funções básicas da aplicação, fornecendo ao usuário procedimentos que executam tarefas específicas.
III. exibe para o usuário os dados fornecidos pelo controle e estabelece uma interface para interação entre o usuário e a aplicação.
A associação correta do componente do padrão MVC com sua função está expressa,respectivamente, em a) (I) Controller; (II) Model; (III) View;
b) (I) Model; (II) Controller; (III) View;

c) (I) View; (II) Model; (III) Controller;

d) (I) Controller; (II) View; (III) Model;

e) (I) Model; (II) View; (III) Controller;

Comentários:

(I) Quem faz essa orquestração de requisições é a Camada de Controle; (II) Acesso aos dados e funções básicas da aplicação são de responsabilidade da Camada de Modelo; (III)Exibição é sempre
Camada de Visão!

Gabarito: Letra A

12. (FCC / TJ-PE - 2012) Com relação à arquitetura MVC, considere:

I. O MODEL representa os dados da empresa e as regras de negócio que governam o acesso e atualização destes dados.
II. O VIEW acessa os dados da empresa através do MODEL e especifica como esses dados devem ser apresentados. É de responsabilidade do VIEW manter a consistência em sua apresentação,quando o MODEL é alterado.

III. O CONTROLLER traduz as interações do VIEW em ações a serem executadas pelo MODEL.
Com base na interação do usuário e no resultado das ações do MODEL, o CONTROLLER
responde selecionando uma VIEW adequada.

IV. Permite uma única VIEW para compartilhar o mesmo modelo de dados corporativos em um fluxo de comunicação sequencial.
Está correto o que se afirma em:

a) I, II, III e IV.

b) I, II e III, apenas.

c) II e III, apenas.

d) II, III e IV, apenas.

e) I e II, apenas.

Comentários:

(I) Correto, ele representa os dados e as regras de negócio; (II) Correto, a View acessa os dados por meio do Model. Essa parte gera dúvida, mas é responsabilidade da View - após ser notificada -atualizar a apresentação quando há modificação na Model; (III) Correto, essa é a função doController, ele orquestra as requisições entre Model e View; (IV) Errado, na verdade permite quantas views forem necessárias para um mesmo Model;
Gabarito: Letra B

13. (FCC / MPE-PE - 2012) O componente Controller do MVC:

a) Define o comportamento da aplicação, as ações do usuário para atualizar os componentes de dados e seleciona os componentes para exibir respostas de requisições.
b) Envia requisições do usuário para o controlador e recebe dados atualizados dos componentes de acesso a dados.
c) Responde às solicitações de queries e encapsula o estado da aplicação.

d) Notifica os componentes de apresentação das mudanças efetuadas nos dados e expõe a funcionalidade da aplicação.
e) É onde são concentradas todas as regras de negócio da aplicação e o acesso aos dados.

Comentários:

(a) Correto, ele define o comportamento da aplicação, as ações do usuário para atualizar os componentes de dados e seleciona os componentes para exibir respostas de requisições;(b) Errado,
essa responsabilidade é da View; (c) Errado, essa responsabilidade é do Model; (d)
Errado, essa responsabilidade é do Model; (e) Errado, essa responsabilidade é do Model;
Gabarito: Letra A

i4.(FCC /TRT-MT -2011) No projeto de arquitetura modelo-visão-controle (MVC), o controlador:

a) renderiza a interface de usuário a partir da visão, o modelo encapsula funcionalidades e objetos de conteúdo e a visão processa e responde a eventos e invoca alterações ao controlador.
b) encapsula funcionalidades e objetos de conteúdo, o modelo processa e responde a eventos e invoca alterações ao controlador e a visão renderiza a interface de usuário a partir do modelo.
c) encapsula funcionalidades e objetos de conteúdo, o modelo renderiza a interface de usuário a partir da visão e a visão processa e responde a eventos e invoca alterações ao controlador.
d) processa e responde a eventos e invoca alterações ao modelo, o modelo encapsula funcionalidades e objetos de conteúdo e a visão renderiza a interface de usuário a partir do modelo.
e) processa e responde a eventos e invoca alterações ao modelo, o modelo renderiza a interface de usuário a partir da visão e a visão encapsula funcionalidades e objetos de conteúdo.
Comentários:

O Controlador processa e responde a eventos e invoca alterações ao modelo, o modelo encapsula funcionalidades e objetos de conteúdo e a visão renderiza a interface de usuário a partir do modelo.
Gabarito: Letra D

15. (FCC/TRT-SE-2010) No desenvolvimento de sistemas, no âmbito das relações intermodulares entre as classes, diz-se que o programa está bem estruturado quando há:
a) maior coesão e maior acoplamento.

b) menor coesão e maior acoplamento.

c) menor coesão e menor acoplamento.

d) maior coesão e menor acoplamento.

e) apenas coesão ou apenas acoplamento.

Comentários:

Nosso mantra: alta coesão e baixo acoplamento!

Gabarito: Letra D

i6.(FCC /TCM-PA-2010) Extensão natural do conceito de ocultação de informações, que diz:
"um módulo deve executar uma única tarefa dentro do procedimento de software, exigindo pouca interação com procedimentos que são executados em outras partes de um programa", é o conceito de:
a) coesão.

b) enfileiramento.

c) acoplamento.

d) visibilidade.

e) recursividade.

Comentários:

Módulo deve executar uma única tarefa? Divisão de responsabilidades, isto é, coesão.

Gabarito: Letra A

17.(FCC/TRT-SE-2010) A arquitetura multicamadas divide-se em três camadas lógicas. São elas:

a) Apresentação, Negócio e Acesso a Dados.

b) Apresentação, Natureza e Acesso a Dados.

c) Apresentação, Negócio e Alteração.

d) Manipulação, Natureza e Acesso a Dados.

e) Manipulação, Negócio e Acesso a Dados.

Comentários:

Easy! Apresentação, Negócio e Acesso a Dados.

Gabarito: Letra A

i8.(FCC / METRÔ-SP - 2010) A arquitetura multicamadas divide-se em três camadas lógicas. São elas:
a) Apresentação, Negócio e Alteração.

b) Manipulação, Natureza e Acesso a Dados.

c) Manipulação, Negócio e Acesso a Dados.

d) Apresentação, Natureza e Acesso a Dados.

e) Apresentação, Negócio e Acesso a Dados.

Comentários:

Opa... Apresentação, Negócio e Acesso a Dados. Vejam que as bancas se autocopiam -
essa questão é quase idêntica à anterior.
Gabarito: Letra E

ig.(FCC / AL-SP - 2010) Sobre as camadas do modelo de arquitetura MVC
(Model- View-
Controller) usado no desenvolvimento web é correto afirmar:

a) Todos os dados e a lógica do negócio para processá-los devem ser representados na camadaController.

b) A camada Model pode interagir com a camada View para converter as ações do cliente em ações que são compreendidas e executadas na camada Controller.
c) A camada View é a camada responsável por exibir os dados ao usuário. Em todos os casos essa camada somente pode acessar a camada Model por meio da camada Controller.
d) A camada Controller geralmente possui um componente controlador padrão criado para atender a todas as requisições do cliente.
e) Em aplicações web desenvolvidas com Java as servlets são representadas na camada Model.

Comentários:

(a) Errado, fica na Camada de Modelo; (b) Errado, quase tudo correto, mas as ações são executadas na Camada de Modelo; (c) Errado, trata-se de uma arquitetura triangular, logo pode ser acessada diretamente; (d) Correto, geralmente há um controlador padrão, sim (Ex: Servlets); (e)Errado, as
Servlets são representadas na Camada de Controle.

Gabarito: Letra D

2o.(FCC / TRT3 - 2009) Considerando o conjunto de tarefas que se relacionam em um módulo e o espectro de medidas da força funcional relativa dos módulos (coesão), a respectiva sequência,da pior para a melhor, é:

a) sequencial, temporal e lógica.

b) procedimental, coincidental e funcional.

c) temporal, lógica e sequencial.

d) temporal, comunicacional e sequencial.

e) procedimental, funcional e lógica.

Comentários:

Indesejáveis: Coincidental, Lógica e Temporal; Intermediárias: Procedural,
Comunicacional e
Sequencial; Desejável: Funcional. Então, do pior para a melhor, temos: Temporal,
Comunicacional e Sequencial.
Gabarito: Letra D

2i.(FCC / TJ-SE - 2009) No modelo de três camadas MVC para web services, o responsável pela apresentação que também recebe os dados de entrada do usuário é a camada:
a) View.

b) Application.

c) Controller.

d) Data.

e) Model.

Comentários:

Apresentação? Camada de Visão (View).

Gabarito: Letra A

22. (FCC /TRT-MA-2009) Considere as funções:

I. Seleção do comportamento do modelo.

II. Encapsulamento dos objetos de conteúdo.

III. Requisição das atualizações do modelo.

Na arquitetura Model-View-Control - MVC, essas funções correspondem, respectivamente, a:

a) Model, View e Control.

b) Control, View e Model.

c) View, Model e Control.

d) Control, Model e View.

e) View, Control e Model.

Comentários:

A seleção do comportamento do modelo é feita pela Camada de Controle; Encapsulamento dos objetos de conteúdo é feito pela Camada de Modelo; Requisição das atualizações do modelo são feitas pela Camada de Visão.
Gabarito: Letra D

23. (FCC /TRT-GO-2008) Visando obter maior independência funcional, é adequado que o esforço seja direcionado ao projeto de módulos:
a) que não usem estruturas de seleção.

b) cujas tarefas tenham elevada coesão.

c) cujas tarefas tenham coesão procedimental.

d) que não usem estruturas de repetição.

e) cujas tarefas tenham coesão lógica.

Comentários:

Maior independência funcional ocorre com alta coesão!

Gabarito: Letra B

24.(FCC / TRF5 - 2008) Via de regra as divisões da arquitetura de software em três camadas orientam para níveis que especificam:
a) os casos de uso, a estrutura dos dados e os processos de manutenção.

b) a apresentação, as regras de negócio e os testes.

c) a apresentação, os processos operacionais e a seqüência de execução.

d) a apresentação, os componentes virtuais e a seqüência de execução.

e) a apresentação, as regras de negócio e o armazenamento de dados.

Comentários:

Tranquila também, só mudaram as palavras! Apresentação, Regras de Negócio e Armazenamento de Dados.
Gabarito: Letra E

QUESTõES CoMENTADAS - DIvERSAS BANCAS

í. (CS-UFG / SANEGO-GO - 2018) Dentro dos bons princípios de projeto e construção de software, a Lei de Démeter diz que "um método deve enviar mensagens somente para objetos a que ele tem acesso direto". Essa lei tem como objetivo:
a) aumentara coesão.

b) diminuir o acoplamento.

c) facilitar a criação de dependência entre as classes.

d) aumentar a quantidade de casos de teste.

Comentários:

Como a Lei de Démeter diz que o objeto pode enviar mensagens apenas para objetos a que ele tem acesso direto, a intenção é diminuir o acoplamento, ou seja, diminuir o nível de dependência entre as classes.
Gabarito: Letra B

2. (UFG / SANEAGO - 2017) O emprego de boas práticas de projeto (design) de software visa resultarem um código:
a) altamente acoplado e altamente coeso.

b) altamente acoplado e fracamente coeso.

c) fracamente acoplado e altamente coeso.

d) fracamente acoplado e fracamente coeso.

Comentários:

A regra de ouro de uma arquitetura de software: alta/forte coesão e baixo/fraco acoplamento!

Gabarito: Letra C

3. (UFG / SANEAGO - 2017) Dentro dos padrões arquiteturais de software, a arquitetura Model-View-ViewModel (MVVM) é próxima da arquitetura Model-View-Presenter (MVP),
porém diferencia-se desta pelo fato de:
a) ser desprovida de um componente controlador como existe no Model-View-Controller (MVC).

b) implementar o padrão de projeto Observer na ligação entre dados (ViewModel) e tela (view).

c) ligar diretamente as classes de tela (view) e dados (Model) dentro da estrutura do projeto.

d) vincular a realização de atualizações de tela (view) à atualização de dados (ViewModel).

Comentários:

Perfeito! É a aplicação do Padrão de Projeto Observer!

Gabarito: Letra B

4. (IBFC/EBSERH-2017) O modelo de três camadas físicas (3-tier), especificado nas alternativas,divide um aplicativo de modo que a lógica de negócio resida no meio das três camadas, foi adaptado como uma arquitetura para as aplicações Web em todas as linguagens de programação maiores. Muitos frameworks de aplicação comerciais e não comerciais foram criados tendo como base a arquitetura:
a) MVC (Model-View-Controller)

b) MDB (Model-Data-Business)

c) UDC (User-Data-Controller)

d) MDC (Model-Data-Controller)

e) UVB (User-View-Business).

Comentários:

A divisão do aplicativo que separa em três camadas é a Arquitetura MVC (Model, View e Control).

Gabarito: Letra A

5. (CESGRANRIO / CEFET-RJ - 2014) No contexto da Arquitetura de Sistemas, o MVC
(model -
view-controller) é um estilo arquitetural:

a) interativo b) estrutural c) distribuído d) adaptável e) monolítico
Comentários:

É um estilo arquitetural interativo, no sentido de que é um estilo para interface de usuário,fornecendo diversas visões diferentes para um mesmo modelo de dados.

Gabarito: Letra A

6. (IBFC / TRE-AM - 2014) Na arquitetura cliente-servidor, além dos dois principais componentesCliente e o Servidor, existe um terceiro elemento intermediando os dois. Esse componente é chamado tecnicamente de:
a) coreware.

b) middleware.

c) mainware.

d) centerware.

Comentários:

O conceito de Middleware é amplamente utilizado em diversos contextos da computação.
Como o próprio nome remete, ele é um "software do meio" ou "software intermediário". Possui diversas aplicações, como: intermediar a comunicação entre cliente e servidor(muito utilizado em ambientes distribuídos); intermediar a comunicação entre Softwares que utilizam protocolos ou plataformas diferentes; Intermediar a comunicação entre Sistema Operacional e Aplicações.
Gabarito: Letra B

7. (IBFC / TRE-AM - 2014) No desenvolvimento de sistemas dentro do conceito da arquitetura cliente-servidor de três camadas, temos as seguintes camadas:
1. Camada de Dados.

2. Camada de Apresentação.

3. Camada de Aplicações.

4. Camada de Negócio.

Estão corretas as afirmativas:

a) somente 1, 2 e 4.

b) somente 2, 3 e 4.

c) somente 1, 3 e 4.

d) somente 1, 2 e 3.

Comentários:

A arquitetura cliente-servidor se divide em Camada de Dados, Camada de Apresentação e
Camada de Negócio. Logo, somente 1,2 e 4.
Gabarito: Letra A

8. (ESAF/CGU-2012) A definição de que um sistema deve ser desenvolvido em três níveis é feita pelo padrão de projeto:
a) MVC (Model View Controller).

b) MVC-Dev (Model Value Constructive Development).

c) TMS (Time Milestones Setting).

d) PMC (Project Main Controller).

e) MCA (Model Classes Assignment).

Comentários:

A questão trata do MVC (Model View Controller).

Gabarito: Letra A

9. (ESAF / CVM - 2010) Modelo MVC significa:

a) Modo-View-Construtor.

b) Modelo-View-Controlador.

c) Modelo-Versão-Case.

d) Módulo-Verificador-Controlador.

e) Medida-Virtual-Concepção.

Comentários:

A questão trata do Modelo-View-Controlador.

Gabarito: Letra B

LISTA DE QUESTõES - CESPE

í. (CESPE / BNB - 2022) No padrão MVC, o componente de modelo gerencia as requisições dos usuários.
2. (CESPE / BNB - 2022) Na arquitetura em camadas, os componentes da camada mais interna opera o sistema operacional, ao passo que os da camada mais externa interagem com o usuário.
3. (CESPE / Petrobrás - 2022) Enquanto a arquitetura é responsável pela infraestrutura de alto nível do software, o design é responsável pelo software a nível de código, como, por exemplo, o que cada módulo está fazendo, o escopo das classes e os objetivos das funções.
4. (CESPE/TJ-RJ -2021) Na arquitetura MVC (Model-View-Controller), asfuncionalidades de cada segmento são mais bem descritas como:
a) o modelo encapsula as funcionalidades; o view gerencia as requisições dos usuários; o controlador prepara dados do modelo.
b) o modelo encapsula objetos de conteúdo; a visão solicita atualizações do modelo; o controlador seleciona o comportamento do modelo.
c) o modelo incorpora todos os estados; o view gerencia as requisições dos usuários; o controlador encapsula objetos de conteúdo.
d) o modelo encapsula objetos de conteúdo; o view seleciona o comportamento do modelo; o controlador solicita atualizações do modelo.
e) o modelo seleciona a resposta da visão; a visão apresenta a visão selecionada pelo controlador; o controlador encapsula objetos de conteúdo.
5. (CESPE / TJ-RJ - 2021) Em um ambiente cliente/servidor, a arquitetura que permite a mesma aplicação assumir tanto o papel de cliente quanto o de servidor é conhecida como arquiteturaC/S:

a) simples.

b) de dois níveis.

c) multinível.

d) de três camadas.

e) par-par.

6. (CESPE / TELEBRÁS - 2021) Na arquitetura de software, a arquitetura cliente/servidor tem como vantagem uma maior facilidade de manutenção e segurança dos dados, e como desvantagens possíveis bloqueios no tráfego da rede, além de problemas de atualização da interface de aplicação.
7. (CESPE / TELEBRÁS - 2021) Por se tratar de uma arquitetura distribuída, o modelo cliente-servidor pressupõe facilidades para atualizar os servidores de forma transparente, sem que isso afete outras partes do sistema.
8. (CESPE / TRE-BA - 2017) Com referência às arquiteturas multicamadas de aplicações para o ambiente web, assinale a opção correta.
a) Se, na camada de dados, for realizada uma alteração no banco de dados, o restante das camadas também será afetado.
b) O modelo de três camadas recebe essa denominação caso um sistema cliente-servidor seja desenvolvido mantendo-se a camada de negócio do lado do cliente e as camadas de apresentação e dados no lado do servidor.
c) Cada camada é normalmente mantida em um servidor específico para tornar-se o mais escalonável e independente possível em relação a outras camadas, estando entre as suas principais características o eficiente armazenamento e a reutilização de recursos.
d) O objetivo das arquiteturas multicamadas consiste na junção de responsabilidades entre os componentes das aplicações web, de modo a atender aos requisitos funcionais e não funcionais esperados pela aplicação.
e) Na arquitetura de duas camadas — apresentação e armazenamento —, o computador que contivera base de dados terá de ficar junto com os computadores que executarem as aplicações.
9. (CESPE / STJ - 2015) Na arquitetura em camadas MVC (modelo-visão-controlador), o modelo encapsula o estado de aplicação, a visão solicita atualização do modelo e o controlador gerencia a lógica de negócios.
10. (CESPE / MEC - 2015) O controlador gerencia as requisições dos usuários encapsulando as funcionalidades e prepara dados do modelo.
11. (CESPE / MEC - 2015) A visão encapsula objetos de conteúdo, solicita atualizações do modelo e seleciona o comportamento do modelo.
12. (CESPE / STJ - 2015) No padrão em camadas modelo-visão-controle (MVC), o controle é responsável por mudanças de estado da visão.
13. (CESPE / ANTAQ - 2014) O modelo MVC é um padrão de arquitetura que consiste na definição de camadas para a construção de softwares.
14. (CESPE/ANTAQ-2014) O controllertem a responsabilidade de armazenar e buscar os dados que deverão ser exibidos pelo view.
15. (CESPE / INPI - 2013) De acordo com os princípios da engenharia de software relacionados à independência funcional, os algoritmos devem ser construídos por módulos visando unicamente ao alto acoplamento e à baixa coesão, caso a interface entre os módulos dê-se pela passagem de dados.
16. (CESPE / STF - 2013) Quanto maior for o número de camadas, menor será o desempenho do software como um todo.
17. (CESPE / STF - 2013) Cada camada tem comunicação (interface) com todas as demais camadas,tanto inferiores quanto superiores.

18. (CESPE / STF-2013) Em uma arquitetura em camadas, a camada de persistência é responsável por armazenar dados gerados pelas camadas superiores e pode utilizar um sistema gerenciador de banco de dados para evitar, entre outros aspectos, anomalias de acesso concorrente dos dados e problemas de integridade de dados.
19. (CESPE / FUB - 2013) Aplicações cliente-servidor multicamadas são usualmente organizadas em três camadas principais: apresentação, lógica e periférico.
20. (CESPE / FUB-2013) Entre as desvantagens de se executartodas as camadas de uma aplicação cliente-servidor no lado do servidor se destaca a dificuldade de atualização e correção da aplicação.
21. (CESPE / BACEN - 2013) MVC (Model-View-Controller) é um modelo de arquitetura de software que separa, de um lado, a representação da informação e, de outro, a interação do usuário com a informação.
22. (CESPE /TCE-ES-2013) No Padrão MVC, as regras do negócio que definem a forma de acesso e modificação dos dados são geridas pelo controlador.
23. (CESPE / Banco da Amazônia - 2012) De acordo com o princípio da coesão de classes, cada classe deve representar uma única entidade bem definida no domínio do problema. O grau de coesão diminui com o aumento contínuo de código de manutenção nas classes.
24. (CESPE / Banco da Amazônia - 2012) O acoplamento de métodos expressa o fato de que qualquer método deve ser responsável somente por uma tarefa bem definida.
25. (CESPE / CET - 2011) No padrão de desenvolvimento modelo-visualização-controlador
(MVC),
o controlador é o elemento responsável pela interpretação dos dados de entrada e pela manipulação do modelo, de acordo com esses dados.
26. (CESPE / MEC - 2011) O modelo MVC pode ser usado para construir a arquitetura do software a partir de três elementos: modelo, visão e controle, sendo definidas no controle as regras de negócio que controlam o comportamento do software a partir de restrições do mundo real.
27. (CESPE / MEC - 2011) O controlador, no modelo MVC, realiza a comunicação entre as camadas de visão e modelo.
28. (CESPE / MEC - 2011) No MVC, o modelo representa o estado geral do sistema.

29. (CESPE / MEC - 2011) Apesar do seu amplo emprego em aplicações web, o MVC deve ser utilizado apenas em interfaces gráficas em função de sua arquitetura de componentes.
30. (CESPE / MEC - 2011) No MVC, é o modelo que permite apresentar, de diversas formas diferentes, os dados para o usuário.
31. (CESPE / MEC - 2011) O controlador é o responsável pelas regras de negócio e pelos dados de uma aplicação no MVC.
32. (CESPE / MEC - 2011) A independência dos componentes é um dos atributos que reflete a qualidade do projeto. O grau de independência pode ser medido a partir dos conceitos de acoplamento e coesão, os quais, idealmente, devem ser alto e baixo, respectivamente.
33. (CESPE / MEC - 2011) O termo cliente é usado para designar uma parte distinta de um sistema de computador que gerencia um conjunto de recursos relacionados e apresenta sua funcionalidade para usuários e aplicativos.
34. (CESPE / MEC - 2011) A arquitetura cliente/servidor proporciona a sincronização entre duas aplicações: uma aplicação permanece em estado de espera até que outra aplicação efetue uma solicitação de serviço.
35. (CESPE / MEC - 2011) A arquitetura cliente/servidor enseja o desenvolvimento de um sistema com, no máximo, duas camadas, quais sejam, cliente e servidor.
36. (CESPE / ABIN-2010) Em sistemas de grande porte, um único requisito pode ser implementado por diversos componentes; cada componente, por sua vez, pode incluir elementos de vários requisitos, o que facilita o seu reúso, pois os componentes implementam, normalmente,uma única abstração do sistema.
37. (CESPE / INMETRO - 2010) A coesão e o acoplamento são formas de se avaliar se a segmentação de um sistema em módulos ou em componentes foi eficiente. Acerca da aplicação desses princípios, assinale a opção correta.
a) O baixo acoplamento pode melhorar a manutebilidade dos sistemas, pois ele está associado à criação de módulos como se fossem caixas-pretas.
b) Os componentes ou os módulos devem apresentar baixa coesão e um alto grau de acoplamento.
c) Os componentes ou os módulos devem serfortemente coesos e fracamente acoplados.

d) Um benefício da alta coesão é permitir realizar a manutenção em um módulo sem se preocupar com os detalhes internos dos demais módulos.
e) A modularização do programa em partes especializadas pode aumentar a qualidade desses componentes, mas pode prejudicar o seu reaproveitamento em outros programas.
38.(CESPE/BASA-2oIo) Nessa arquitetura (arquitetura multicamadas), quando são consideradas três camadas, a primeira camada deve ser implementada por meio do servidor de aplicação.
3g.(CESPE / BASA - 2010) Em arquitetura multicamadas, o servidor de aplicação nada mais é do que um programa que fica entre o aplicativo cliente e o sistema de gerenciamento de banco de dados.
40. (CESPE / BASA - 2010) Uma desvantagem dessa arquitetura (arquitetura multicamadas)
é o aumento na manutenção da aplicação, pois alterações na camada de dados, por exemplo,acarretam mudanças em todas as demais camadas.

41. (CESPE / BASA - 2010) Em uma arquitetura cliente-servidor, os clientes compartilham dos recursos gerenciados pelos servidores, os quais também podem, por sua vez, ser clientes de outros servidores.
ZJ2.(CESPE / BASA - 2010) A Internet baseia-se na arquitetura cliente-servidor, na qual a parte cliente, executada no host local, solicita serviços de um programa aplicativo denominado servidor, que é executado em um host remoto.
43-(CESPE / BASA - 2010) A arquitetura cliente-servidor viabiliza o uso simultâneo de diferentes dispositivos computacionais, do seguinte modo: cada um deles realiza a tarefa para a qual é mais capacitado, havendo a possibilidade de uma máquina ser cliente em uma tarefa e servidor em outra.
44. (CESPE / EMBASA - 2010) O MVC promove a estrita separação de responsabilidades entre os componentes de uma interface.
45. (CESPE / EMBASA - 2010) No MVC, a visão é responsável pela manutenção do estado da aplicação.
46. (CESPE / EMBASA - 2010) O modelo no MVC tem como atribuição exibir a parte que é responsável pela manutenção da aplicação para o usuário.
47. (CESPE/ EMBASA-2010) O controladoré responsável pela coordenação entre atualizações no modelo e interações com o usuário.
48. (CESPE / EMBASA - 2010) Por meio do MVC, é possível o desenvolvimento de aplicações em 3camadas para a Web.

4g.(CESPE / UNIPAMPA - 2009) Normalmente, a arquitetura em três camadas conta com as camadas de apresentação, de aplicação e de dados.
50. (CESPE / UNIPAMPA - 2009) Em uma arquitetura em três camadas, na camada de aplicação,usualmente está um servidor de banco de dados que gerencia o conjunto de requisições.

51. (CESPE / UNIPAMPA -2009) O uso de middlewares é comum em aplicações de n camadas.

52. (CESPE / UNIPAMPA - 2009) Na camada de persistência dos dados em aplicações n camadas,podem ser utilizados o banco de dados orientado a objetos e o banco de dados relacionais.

53. (CESPE / UNIPAMPA - 2009) Nas aplicações cliente-servidor, em duas camadas, é simples acessar fontes de dados heterogêneas porque o legado de base de dados não precisa de drivers de conexões diferentes.
54. (CESPE/ANTAQ-2oog) Os principais componentes da arquitetura cliente-servidor,
que é um modelo de arquitetura para sistemas distribuídos, são o conjunto de servidores que oferecem serviços para outros subsistemas, como servidores de impressão e servidores de arquivos,o conjunto de clientes que solicitam os serviços oferecidos por servidores, e a rede que permite aos clientes acessarem esses serviços.
55. (CESPE / BASA - 2009) Em arquiteturas cliente-servidor multicamadas, na maior parte das aplicações, o browser é adotado como cliente universal.
56. (CESPE / ANAC - 2009) O framework modelo visão controlador (MVC - model view controller)é muito utilizado para projeto da GUI (graphical user interface) de programas orientados a objetos.
57. (CESPE / TCU - 2009) No MVC (model-view-controller), um padrão recomendado para aplicações interativas, uma aplicação é organizada em três módulos separados.Um para o modelo de aplicação com a representação de dados e lógica do negócio, o segundo com visões que fornecem apresentação dos dados e input do usuário e o terceiro para um controlador que despacha pedidos e controle de fluxo.
58. (CESPE/ANATEL-2oog) Uma das vantagens da arquitetura distribuída é o compartilhamento de recursos, que permite que sistemas, aplicativos e dispositivos periféricos,como discos,
impressoras, arquivos, estejam associados a diferentes computadores em uma rede.
Uma segunda vantagem é a concorrência, uma vez que vários processos podem operar ao mesmo tempo em diferentes computadores na rede. E, por fim, uma terceira vantagem é a proteção,pois o acesso é feito de forma centralizada.

59. (CESPE/ANTAQ-2009) Uma das desvantagens da arquitetura distribuída é sua complexidade,
uma vez que é mais difícil compreender as propriedades emergentes dos sistemas que as dos sistemas centralizados.
60. (CESPE / INMETRO - 2009) Em uma arquitetura distribuída, middleware é definido como uma camada de software cujo objetivo é mascarar a heterogeneidade e fornecer um modelo de programação conveniente para os programadores de aplicativos. Como exemplos de middlewares é correto citar: Sun RPC, CORBA, RMI Java e DCOM da Microsoft.
61. (CESPE/IPEA-2008) Na arquitetura cliente-servidor com três camadas (three tier), a camada de apresentação, a camada de aplicação e o gerenciamento de dados ocorrem em diferentes máquinas. A camada de apresentação provê a interface do usuário e interage com o usuário,sendo máquinas clientes responsáveis pela sua execução. A camada de aplicação é responsável pela lógica da aplicação, sendo executada em servidores de aplicação. Essa camada pode interagir com um ou mais bancos de dados ou fontes de dados. Finalmente, o gerenciamento de dados ocorre em servidores de banco de dados, que processam as consultas da camada de aplicação e enviam os resultados.
62. (CESPE/ STJ -2008) A arquitetura de um sistema de software pode se basearem determinado estilo de arquitetura. Um estilo de arquitetura é um padrão de organização. No estilo cliente-servidor, o sistema é organizado como um conjunto de serviços, servidores e clientes associados que acessam e usam os serviços. Os principais componentes desse estilo são servidores que oferecem serviços e clientes que solicitam os serviços.
63. (CESPE / TJ-CE - 2008) A arquitetura MVC fornece uma maneira de dividir a funcionalidade envolvida na manutenção e apresentação dos dados de uma aplicação web.
64. (CESPE / TJ-CE - 2008) A arquitetura MVC foi desenvolvida recentemente para mapear as tarefas complexas de saída do sistema do usuário.
65. (CESPE / TJ-CE - 2008) Na arquitetura MVC, um controlador define o comportamento da aplicação, já que este é o responsável por interpretar as ações do usuário e as relaciona com as chamadas do modelo.
66. (CESPE / TJ-CE - 2008) A arquitetura MVC não separa a informação de sua apresentação,porque, em sistemas web, informação e apresentação estão na mesma camada.

67. (CESPE / TJ-CE - 2008) O desenvolvimento de sistemas web ocorre tipicamente em três camadas. A arquitetura MVC aumenta o escopo do desenvolvimento para, no máximo, quatro camadas, sendo a quarta camada o processamento dos dados do usuário.
68. (CESPE / IPEA - 2008) A arquitetura distribuída é caracterizada pelo compartilhamento de recursos computacionais e serviços por meio da comunicação direta e descentralizada entre os sistemas envolvidos e inclui, entre outras coisas, a troca de informações, ciclos de processamento e espaço de armazenamento em disco.
69. (CESPE / SERPRO - 2008) Uma arquitetura distribuída permite a divisão de uma mesma tarefa em diferentes processadores em uma mesma CPU. Essa característica aumenta a velocidade de processamento de uma informação.
70. (CESPE / TCU - 2007) A arquitetura cliente-servidor tem por motivação sincronizar a execução de dois processos que devem cooperar um com outro. Assim, dadas duas entidades que queiram comunicar-se, uma deve iniciar a comunicação enquanto a outra aguarda pela requisição da entidade que inicia a comunicação.
71. (CESPE / DATAPREV - 2006) Uma arquitetura cliente/servidor caracteriza-se pela separação do cliente, o usuário que acessa ou demanda informações, do servidor. Um exemplo típico é um navegador que acessa páginas na Internet. É uma arquitetura que permite o acesso a serviços remotos através de rede de computadores, e que tem como principal deficiência a falta de escalabilidade.
72. (CESPE / DATAPREV - 2006) Arquiteturas cliente/servidor podem ser decompostas em mais de duas camadas. Uma configuração muito utilizada é aquela em que os clientes acessam informações por meio de servidores de aplicação, que por sua vez acessam servidores de banco de dados. Este tipo de arquitetura é conhecida como arquitetura em 3 camadas, ou three-tier.
73. (CESPE/CENSIPAM-2006) O padrão MVC organiza um software em modelo, visão e controle.
O modelo encapsula as principais funcionalidades e dados. As visões apresentam os dados aos usuários. Uma visão obtém os dados do modelo via funções disponibilizadas pelo modelo;só há uma visão para um modelo. Usuários interagem via controladoras que traduzem os eventos em solicitações ao modelo ou à visão; podem existir várias controladoras associadas a uma mesma visão.
74.(CESPE / CENSIPAM - 2006) No padrão MVC, se um usuário modifica o modelo, as visões que dependem desse modelo refletem essas modificações, pois o modelo notifica as visões quando ocorre uma modificação nos seus dados. Portanto, é usado um mecanismo para propagação de modificações que mantém um registro dos componentes que dependem do modelo.
75. (CESPE / SEAD-PA - 2004) Em um modelo cliente-servidor em que o processamento é concentrado nos clientes e o armazenamento concentrado no servidor, observa-se uma baixa carga de tráfego na rede.
76. (CESPE / SERPRO - 2004) Uma das vantagens da arquitetura cliente-servidor é que parte da carga de processamento é retirada do servidor e colocada nos vários clientes.
77. (CESPE / STJ - 2004) As camadas da arquitetura cliente-servidor de três camadas são: camada de interface de usuário, camada de regras de negócio e camada de acesso ao banco de dados.
78. (CESPE / STJ - 2004) Na arquitetura cliente-servidor multicamadas, uma alteração na camada de acesso aos dados não afeta a camada de interface de usuário, desde que essas camadas estejam na mesma máquina.
79. (CESPE / STJ - 2004) A arquitetura cliente-servidor multicamadas possui a vantagem de que a camada de interface de usuário pode se comunicar diretamente com qualquer outra camada,ou seja, não existe hierarquia entre camadas.
80. (CESPE / TRE-RS - 2003) Aplicações com arquitetura cliente-servidor são assimétricas, no sentido de que o cliente e o servidor possuem papéis diferentes na arquitetura de comunicações.
81. (CESPE / TRE-RS - 2003) O servidor, por possuir normalmente um hardware mais robusto,sempre deve executara parte mais pesada do processamento.

82. (CESPE / TRE-RS - 2003) Do ponto de vista das funcionalidades de usuários, o servidor não precisa necessariamente de uma interface de usuário.
GABARITo

1. ERRADO 41. CORRETO
81. ERRADO

2. CORRETO 42. CORRETO
82. CORRETO

3- CORRETO 43- CORRETO

4- LETRA B 44. ANULADA

5- LETRA E 45- ERRADO

6. CORRETO 46. ERRADO

7- CORRETO 47- CORRETO

8. CORRETO 48. CORRETO

9- ERRADO 49- CORRETO

10. ERRADO 50. ERRADO

li. ERRADO 51- CORRETO

12. ERRADO 52. CORRETO

13- ERRADA 53- ERRADO

14- ERRADO 54- CORRETO

x5- ERRADO 55- CORRETO

i6. CORRETO 56. CORRETO

17- ERRADO 57- CORRETO

i8. CORRETO 58. ERRADO

19. ERRADO 59- CORRETO

20. ERRADO 60. CORRETO

21. CORRETO 61. CORRETO

22. ERRADO 62. CORRETO

23- CORRETO 63. CORRETO

24. ERRADO 64. ERRADO

25- CORRETO 65. CORRETO

26. ERRADO 66. ERRADO

27- CORRETO 67. ERRADO

28. CORRETO 68. CORRETO

29. ERRADO 69. ERRADO

30. ERRADO 70. CORRETO

31- ERRADO 71- ERRADO

32. ERRADO 72. CORRETO

33- ERRADO 73- ERRADO

34- CORRETO 74- CORRETO

35- ERRADO 75- CORRETO

36. ERRADO 76. CORRETO

37- CORRETO 77- CORRETO

38. ERRADO 78. ERRADO

39- CORRETO 79- ERRADO

40. ERRADO 80. CORRETO

LISTA DE QUESTõES - FCC

í. (FCC / TRF3 - 2019) Os conceitos alta coesão e baixo acoplamento, utilizados no processo de desenvolvimento de software, são princípios essenciais de:
a) Abstração.

b) Modularidade.

c) Incrementação.

d) Separação de Interesses.

e) Generalidade.

2. (FCC /DPE-AM- 2018)

Trecho 1:

public int pensaoAlimenticia(){

return Util.getFuncoes.getFuncoesData.calculaPensao(processo);

Trecho 2:

public int pensaoAlimenticia(){

return Util.calculaPensao(processo);

Em um sistema Orientado a Objetos bem desenvolvido, os princípios relativos a acoplamento e coesão devem ser respeitados. O código Java apresentando no trecho 1 mostra um exemplo de a) baixo acoplamento e o trecho 2 o corrige para alto acoplamento.
b) alta coesão e o trecho 2 o corrige para baixa coesão.

c) alto acoplamento e o trecho 2 o corrige para baixo acoplamento.

d) baixo acoplamento e o trecho 2 mostra um exemplo de baixa coesão.

e) baixa coesão e o trecho 2 mostra um exemplo de alto acoplamento.

3. (FCC / TCM-GO - 2015 - Adaptada) Quanto à Arquitetura em 3 Camadas, é necessário um arranjo que possibilite a reutilização do código e facilite sua manutenção e seu aperfeiçoamento.Deve- se separar Apresentação, Regra de Negócio e Acesso a Dados. Busca-se a decomposição de funcionalidades de forma a permitir aos desenvolvedores concentrarem-se em diferentes partes da aplicação durante a implementação.
4. (FCC / CNMP - 2015) Há algumas variantes possíveis de arquitetura a serem utilizadas em um sistema de bancos de dados. Sobre essas variantes, é correto afirmar que:
a) na arquitetura de 3 camadas, não há uma camada específica para a aplicação.

b) a camada de apresentação da arquitetura de 2 camadas situa-se, usualmente, no servidor de banco de dados.
c) na arquitetura de 3 camadas, a camada de servidor de banco de dados é denominada cliente.

d) a arquitetura de 3 camadas é composta pelas camadas cliente, aplicação e servidor de banco de dados.
e) na arquitetura de 2 camadas não há necessidade de uso de um sistema gerenciadorde bancos de dados.
5. (FCC/TJ-AP-2014) Uma arquitetura muito comum em aplicações web é o Modelo Arquitetural
3 Camadas:

I. Camada de Persistência.

II. Camada de Lógica de Negócio.

III. Camada de Apresentação.

Neste modelo, a correta associação dos componentes com as camadas é:

a) l-Servidor de Banco de Dados - ll-Servidor de Aplicação - lll-Máquina Cliente.

b) l-Servidor Web - ll-Servidor Cliente -1ll-Servidor de Aplicação.

c) l-Servidor Web - ll-Servidor de Banco de Dados - lll-Máquina Cliente.

d) l-Servidor de Banco de Dados - ll-Máquina Cliente - IIl-Servidor de Aplicação.

e) l-Máquina Cliente - ll-Servidor de Banco de Dados - lll-Servidor Web.

6. (FCC / TST - 2012) Uma arquitetura em camadas:

a) possui apenas 3 camadas, cada uma realizando operações que se tornam progressivamente mais próximas do conjunto de instruções da máquina.
b) tem, na camada mais interior, os componentes que implementam as operações de interface com o usuário.
c) pode ser combinada com uma arquitetura centrada nos dados em muitas aplicações de bancos de dados.
d) tem, como camada intermediária, o depósito de dados, também chamado de repositório ou quadro-negro.
e) tem, na camada mais externa, os componentes que realizam a interface com o sistema operacional.
7- (FCC / TRF2 - 2012) São aspectos que podem caracterizar uma arquitetura cliente-servidor,estabelecida logicamente em 4 camadas:

I. A camada Cliente contém um navegador de Internet, caracterizado como cliente universal.

II. A camada de Lógica do Negócio se quebra em duas: camada de Aplicação e camada Web,
em que o servidor Web representa a camada de Apresentação.
III. Na camada de Lógica do Negócio, o servidor de aplicação passa a utilizar middleware, para suporte a thin clients (PDA, celulares, smart cards, etc) e soluções baseadas em componentes,tais como, J2EE e .Net.

IV. Se, de um lado, a camada de Aplicação estabelece uma interface com a camada de
Dados,
do outro o faz com a camada Web e com os thin clients da camada Cliente.

Está correto o que consta em:

a) I e II, apenas.

b) III e IV, apenas.

c) I, II e III, apenas.

d) II, III e IV, apenas.

e) 1,11, III e IV.

8. (FCC/TST-2012) No padrão MVC é possível definir grupos de componentes principais:
o Model
(Modelo), o View (Apresentação) e o Controller (Controle). Deve fazer parte do componente:

a) Controller, uma classe que contém um método com a finalidade de calcular o reajuste de salário dos funcionários.
b) View, uma classe que contém um método para persistir o salário reajustado de um funcionário.
c) Controller, as animações desenvolvidas em Flash.

d) View, as validações necessárias ao sistema, geralmente definidas através de um conjunto de comparações.
e) Model, as classes com métodos conhecidos como setters e getters e que representam tabelas do banco de dados.
9. (FCC / MPE-AP - 2012) Em uma Aplicação Web desenvolvida utilizando o design pattern MVC,as páginas HTML e as classes com métodos que acessam o banco de dados e executam instruções SQL são representadas, respectivamente, nos componentes:
a) Presentation e Business.

b) View e Model.

c) Controller e Model.

d) Model e Business.

e) View e Business.

io.(FCC / MPE-PE - 2012) O padrão de projeto utilizado em aplicações WEB que permite separar as páginas e classes da aplicação em três grupos (muitas vezes chamados de camadas)conhecidos como Apresentação, Controle e Modelo é denominado de:

a) 3-tier.

b) DAO.

c) MVC.

d) DTO.

e) DBO.

n.(FCC / TRT-PE - 2012) O padrão de arquitetura MVC é um modelo de camadas que divide a aplicação em três componentes: Model (modelo), View (visualizador) e Controller(controlador).
As funções de cada um destes três componentes são apresentadas abaixo:

I. interpreta eventos de entrada e envia requisições para o modelo de dados; em seguida,processa os dados carregados a partir do modelo e envia para o visualizador.

II. encapsula o acesso aos dados e funções básicas da aplicação, fornecendo ao usuário procedimentos que executam tarefas específicas.
III. exibe para o usuário os dados fornecidos pelo controle e estabelece uma interface para interação entre o usuário e a aplicação.
A associação correta do componente do padrão MVC com sua função está expressa,respectivamente, em a) (I) Controller; (II) Model; (III) View;
b) (I) Model; (II) Controller; (III) View;

c) (I) View; (II) Model; (III) Controller;

d) (I) Controller; (II) View; (III) Model;

e) (I) Model; (II) View; (III) Controller;

12. (FCC / TJ-PE - 2012) Com relação à arquitetura MVC, considere:

I. O MODEL representa os dados da empresa e as regras de negócio que governam o acesso e atualização destes dados.
II. O VIEW acessa os dados da empresa através do MODEL e especifica como esses dados devem ser apresentados. É de responsabilidade do VIEW manter a consistência em sua apresentação,quando o MODEL é alterado.

III. O CONTROLLER traduz as interações do VIEW em ações a serem executadas pelo MODEL.
Com base na interação do usuário e no resultado das ações do MODEL, o CONTROLLER
responde selecionando uma VIEW adequada.

IV. Permite uma única VIEW para compartilhar o mesmo modelo de dados corporativos em um fluxo de comunicação sequencial.
Está correto o que se afirma em:

a) I, II, III e IV.

b) I, II e III, apenas.

c) II e III, apenas.

d) II, III e IV, apenas.

e) I e II, apenas.

13. (FCC / MPE-PE - 2012) O componente Controller do MVC:

a) Define o comportamento da aplicação, as ações do usuário para atualizar os componentes de dados e seleciona os componentes para exibir respostas de requisições.
b) Envia requisições do usuário para o controlador e recebe dados atualizados dos componentes de acesso a dados.
c) Responde às solicitações de queries e encapsula o estado da aplicação.

d) Notifica os componentes de apresentação das mudanças efetuadas nos dados e expõe a funcionalidade da aplicação.
e) É onde são concentradas todas as regras de negócio da aplicação e o acesso aos dados.

14. (FCC /TRT-MT -2011) No projeto de arquitetura modelo-visão-controle (MVC), o controlador:

a) renderiza a interface de usuário a partir da visão, o modelo encapsula funcionalidades e objetos de conteúdo e a visão processa e responde a eventos e invoca alterações ao controlador.
b) encapsula funcionalidades e objetos de conteúdo, o modelo processa e responde a eventos e invoca alterações ao controlador e a visão renderiza a interface de usuário a partir do modelo.
c) encapsula funcionalidades e objetos de conteúdo, o modelo renderiza a interface de usuário a partir da visão e a visão processa e responde a eventos e invoca alterações ao controlador.
d) processa e responde a eventos e invoca alterações ao modelo, o modelo encapsula funcionalidades e objetos de conteúdo e a visão renderiza a interface de usuário a partir do modelo.
e) processa e responde a eventos e invoca alterações ao modelo, o modelo renderiza a interface de usuário a partir da visão e a visão encapsula funcionalidades e objetos de conteúdo.
15. (FCC/TRT-SE-2Oio) No desenvolvimento de sistemas, no âmbito das relações intermodulares entre as classes, diz-se que o programa está bem estruturado quando há:
a) maior coesão e maior acoplamento.

b) menor coesão e maior acoplamento.

c) menor coesão e menor acoplamento.

d) maior coesão e menor acoplamento.

e) apenas coesão ou apenas acoplamento.

16. (FCC /TCM-PA-2010) Extensão natural do conceito de ocultação de informações, que diz: "um módulo deve executar uma única tarefa dentro do procedimento de software, exigindo pouca interação com procedimentos que são executados em outras partes de um programa", é o conceito de:
a) coesão.

b) enfileiramento.

c) acoplamento.

d) visibilidade.

e) recursividade.

17. (FCC/TRT-SE-2oio) A arquitetura multicamadas divide-se em três camadas lógicas. São elas:

a) Apresentação, Negócio e Acesso a Dados.

b) Apresentação, Natureza e Acesso a Dados.

c) Apresentação, Negócio e Alteração.

d) Manipulação, Natureza e Acesso a Dados.

e) Manipulação, Negócio e Acesso a Dados.

18. (FCC / METRÔ-SP - 2010) A arquitetura multicamadas divide-se em três camadas lógicas. São elas:
a) Apresentação, Negócio e Alteração.

b) Manipulação, Natureza e Acesso a Dados.

c) Manipulação, Negócio e Acesso a Dados.

d) Apresentação, Natureza e Acesso a Dados.

e) Apresentação, Negócio e Acesso a Dados.

ig.(FCC / AL-SP - 2010) Sobre as camadas do modelo de arquitetura MVC
(Model- View-
Controller) usado no desenvolvimento web é correto afirmar:

a) Todos os dados e a lógica do negócio para processá-los devem ser representados na camada
Controller.

b) A camada Model pode interagir com a camada View para converter as ações do cliente em ações que são compreendidas e executadas na camada Controller.
c) A camada View é a camada responsável por exibir os dados ao usuário. Em todos os casos essa camada somente pode acessar a camada Model por meio da camada Controller.
d) A camada Controller geralmente possui um componente controlador padrão criado para atender a todas as requisições do cliente.
e) Em aplicações web desenvolvidas com Java as servlets são representadas na camada Model.

20. (FCC / TRT3 - 2009) Considerando o conjunto de tarefas que se relacionam em um módulo e o espectro de medidas da força funcional relativa dos módulos (coesão), a respectiva sequência,da pior para a melhor, é:

a) sequencial, temporal e lógica.

b) procedimental, coincidental e funcional.

c) temporal, lógica e sequencial.

d) temporal, comunicacional e sequencial.

e) procedimental, funcional e lógica.

21. (FCC / TJ-SE - 2009) No modelo de três camadas MVC para web services, o responsável pela apresentação que também recebe os dados de entrada do usuário é a camada:
a) View.

b) Application.

c) Controller.

d) Data.

e) Model.

22. (FCC / TRT-MA — 2009) Considere as funções:

I. Seleção do comportamento do modelo.

II. Encapsulamento dos objetos de conteúdo.

III. Requisição das atualizações do modelo.

Na arquitetura Model-View-Control - MVC, essas funções correspondem, respectivamente, a:

a) Model, View e Control.

b) Control, View e Model.

c) View, Model e Control.

d) Control, Model e View.

e) View, Control e Model.

23. (FCC /TRT-GO-2008) Visando obter maior independência funcional, é adequado que o esforço seja direcionado ao projeto de módulos:
a) que não usem estruturas de seleção.

b) cujas tarefas tenham elevada coesão.

c) cujas tarefas tenham coesão procedimental.

d) que não usem estruturas de repetição.

e) cujas tarefas tenham coesão lógica.

24. (FCC / TRF5 - 2008) Via de regra as divisões da arquitetura de software em três camadas orientam para níveis que especificam:
a) os casos de uso, a estrutura dos dados e os processos de manutenção.

b) a apresentação, as regras de negócio e os testes.

c) a apresentação, os processos operacionais e a seqüência de execução.

d) a apresentação, os componentes virtuais e a seqüência de execução.

e) a apresentação, as regras de negócio e o armazenamento de dados.

GABARITo

1. LETRA B 9- LETRA B
17- LETRA A

2. LETRA C 10. LETRAC
18. LETRA E

3- LETRAC íi. LETRA A
19- LETRA D

4- LETRA D 12. LETRA B
20. LETRA D

5- LETRA A 13- LETRA A
21. LETRA A

6. LETRAC 14- LETRA D
22. LETRA D

7- LETRA E 15- LETRA D
23- LETRA B

8. LETRA A i6. LETRA A
24- LETRA E

LISTA DE QUESTõES - DIvERSAS BANCAS

í. (CS-UFG / SANEGO-GO - 2018) Dentro dos bons princípios de projeto e construção de software, a Lei de Démeter diz que "um método deve enviar mensagens somente para objetos a que ele tem acesso direto". Essa lei tem como objetivo:
a) aumentar a coesão.

b) diminuir o acoplamento.

c) facilitar a criação de dependência entre as classes.

d) aumentar a quantidade de casos de teste.

2. (UFG / SANEAGO - 2017) O emprego de boas práticas de projeto (design) de software visa resultarem um código:
a) altamente acoplado e altamente coeso.

b) altamente acoplado e fracamente coeso.

c) fracamente acoplado e altamente coeso.

d) fracamente acoplado e fracamente coeso.

3. (UFG / SANEAGO - 2017) Dentro dos padrões arquiteturais de software, a arquitetura Model-View-ViewModel (MVVM) é próxima da arquitetura Model-View-Presenter (MVP),
porém diferencia-se desta pelo fato de:
a) serdesprovida de um componente controladorcomo existe no Model-View-Controller(MVC).

b) implementar o padrão de projeto Observer na ligação entre dados (ViewModel) e tela (view).

c) ligar diretamente as classes de tela (view) e dados (Model) dentro da estrutura do projeto.

d) vincular a realização de atualizações de tela (view) à atualização de dados (ViewModel).

4. (IBFC / EBSERH-2017) O modelo de três camadas físicas (3-tier), especificado nas alternativas,divide um aplicativo de modo que a lógica de negócio resida no meio das três camadas, foi adaptado como uma arquitetura para as aplicações Web em todas as linguagens de programação maiores. Muitos frameworks de aplicação comerciais e não comerciais foram criados tendo como base a arquitetura:
a) MVC (Model-View-Controller)

b) MDB (Model-Data-Business)

c) UDC (User-Data-Controller)

d) MDC (Model-Data-Controller)

e) UVB (User-View-Business).

5- (CESGRANRIO / CEFET-RJ - 2014) No contexto da Arquitetura de Sistemas, o MVC
(model -
view-controller) é um estilo arquitetural:

a) interativo b) estrutural c) distribuído d) adaptável e) monolítico
6. (IBFC / TRE-AM - 2014) Na arquitetura cliente-servidor, além dos dois principais componentesCliente e o Servidor, existe um terceiro elemento intermediando os dois. Esse componente é chamado tecnicamente de:
a) coreware.

b) middleware.

c) mainware.

d) centerware.

7. (IBFC / TRE-AM - 2014) No desenvolvimento de sistemas dentro do conceito da arquitetura cliente-servidor de três camadas, temos as seguintes camadas:
1. Camada de Dados.

2. Camada de Apresentação.

3. Camada de Aplicações.

4. Camada de Negócio.

Estão corretas as afirmativas:

a) somente 1, 2 e 4.

b) somente 2, 3 e 4.

c) somente 1, 3 e 4.

d) somente 1, 2 e 3.

8. (ESAF/CGU-2012) A definição de que um sistema deve ser desenvolvido em três níveis é feita pelo padrão de projeto:
a) MVC (Model View Controller).

b) MVC-Dev (Model Value Constructive Development).

c) TMS (Time Milestones Setting).

d) PMC (Project Main Controller).

e) MCA (Model Classes Assignment).

9. (ESAF / CVM - 2010) Modelo MVC significa:

a) Modo-View-Construtor.

b) Modelo-View-Controlador.

c) Modelo-Versão-Case.

d) Módulo-Verificador-Controlador.

e) Medida-Virtual-Concepção.

GABARITo

1. LETRA B 4- LETRA A
7- LETRA A

2. LETRA C 5- LETRA A
8. LETRA A

3- LETRA B 6. LETRA B
9- LETRA B

Conceitos Básicos

ARQUITETURA HEXACoNAL

ARQUITETURA HEXAGONAL

Também chamada de Ports and Adapters, a arquitetura hexagonal é uma forma de organizar o código em camadas, cada qual com a sua responsabilidade, tendo como objetivo isolar totalmente a lógica da aplicação do mundo externo. Este isolamento é feito por meio de portas e adaptadores, onde as portas sâo as interfaces que as camadas de baixo nível expõe e adaptadores sâo as implementações para as interfaces em questão.
Uma das principais ideias da arquitetura hexagonal é separar o código-fonte de negócio do código-fonte de tecnologia. Ainda assim, não apenas isso, também devemos garantir que o lado da tecnologia dependa do lado do negócio para que este possa evoluir sem nenhuma preocupação sobre qual tecnologia é usada para cumprir os objetivos de negócios. Etambém devemos ser capazes de alterar o código da tecnologia sem causar danos à sua contraparte comercial.
Para atingir esses objetivos, devemos determinar um local onde o código de negócios existirá,isolado e protegido de quaisquer preocupações de tecnologia. Isso dará origem à criação do nosso primeiro hexágono: Hexágono de Domínio.
No Hexágono de Domínio, reunimos os elementos responsáveis por descrever os problemas centrais que queremos que nosso software resolva. Entidades e objetos de valor são os principais elementos utilizados nesse hexágono. As entidades representam coisas às quais podemos atribuir uma identidade e os objetos de valor são componentes imutáveis que podemos usar para compor nossas entidades. Tudo isso é bastante baseado no DDD (Domain Driven Design).
Também precisamos de maneiras de usar, processar e orquestrar as regras de negócios provenientes do hexágono de domínio - é isso que faz o Hexágono de Aplicação. Ele fica entre os lados de negócios e tecnologia, servindo como intermediário para interagir com ambas as partes.O Hexágono de Aplicação utiliza portas e casos de uso para executar suas funções.

Já o Hexágono de Framework fornece a interface do mundo externo. Esse é o lugar onde temos a oportunidade de determinar como expor os recursos da aplicação-é aqui que definimos endpointsREST/gRPC, por exemplo. E para consumir coisas de fontes externas, usamos o Hexágono de
Framework para especificar os mecanismos que buscam dados de bancos de dados, agentes de mensagens ou qualquer outro sistema.
Na arquitetura hexagonal, materializamos as decisões de tecnologia por meio de adaptadores. Odiagrama a seguir fornece uma visão de alto nível da arquitetura:

Dependency Inversion

Hexágono de Domínio

O Hexágono de Domínio representa um esforço para entender e modelar um problema do mundo real. Suponha que você esteja em um projeto que precise criar um inventário de rede e topologia para uma empresa de telecomunicações. O principal objetivo deste inventário é fornecer uma visão abrangente de todos os recursos que compõem a rede. Dentre esses recursos, temos roteadores,switches, racks, estantes e outros tipos de equipamentos.

Nosso objetivo aqui é usar o Hexágono de Domínio para modelar o conhecimento necessário para identificar, categorizar e correlacionar esses elementos de rede e topologia em código-fonte, bem como fornecer uma visão lúcida e organizada do inventário desejado. Esse conhecimento deve ser,tanto quanto possível, representado de forma agnóstica em relação à tecnologia.

Esta busca não é trivial. Os desenvolvedores envolvidos podem não conhecer empresas de telecomunicações e deixar de lado esse negócio de inventário. É necessário consultar especialistas de domínio ou outros desenvolvedores que já conheçam o problema do domínio. Se nenhum deles estiver disponível, você deve tentar preencher a lacuna de conhecimento consultando livros ou qualquer outro material que ensine sobre o domínio do problema.
Dentro do Hexágono de Domínio, temos entidades correspondentes a dados e regras críticas de negócios. Eles são críticos porque representam um modelo do problema real. Esse modelo leva algum tempo para evoluir e refletir consistentemente o problema que estamos tentando modelar.Esse é o caso de novos projetos de software em que nem os desenvolvedores nem os especialistas do domínio têm uma visão clara do objetivo do sistema em seus estágios iniciais.
Em tais cenários, que são particularmente recorrentes em ambientes de startups,
é normal e previsível ter um modelo de domínio inicial desajeitado que evolui apenas conforme as ideias de negócios evoluem e são validadas por usuários e especialistas do domínio. É uma situação curiosa onde o modelo de domínio é desconhecido, mesmo para os chamados especialistas de domínio.
Por outro lado, em cenários onde o domínio do problema existe e está claro nas mentes dos especialistas do domínio, se não conseguirmos compreenderesse domínio do problema e como ele se traduz em entidades e outros objetos do domínio, como objetos de valor,construiremos nosso software baseado em suposições fracas ou erradas. Isso pode ser considerado um dos motivos pelos quais qualquer software começa simples e, à medida que sua base de código cresce,acumula dívida técnica e se torna mais difícil de manter.
Essas suposições fracas podem levar a um código frágil e inexpressivo que pode inicialmente resolver problemas de negócios, mas não está pronto para acomodar mudanças de maneira coesa.Lembre-se de que o hexágono do domínio é composto por qualquertipo de categoria de objeto que você considere adequado para representar o domínio do problema. Aqui está uma representação baseada apenas em Entidades e Objetos de Valor:
Domain

Entities

Value Objects

Hexágono de Aplicação

Até agora, discutimos como o hexágono Domínio encapsula regras de negócios com entidades e objetos de valor. Mas há situações em que o software não precisa operar diretamente no nível doDomínio. Algumas operações existem apenas para permitir a automação fornecida pelo software.Essas operações - embora suportem regras de negócios - não existiriam fora do contexto do software. Estamos falando de operações específicas da aplicação.
O Hexágono de Aplicação é onde lidamos abstratamente com tarefas específicas do aplicativo.Quero dizer abstrato porque ainda não estamos lidando diretamente com questões de tecnologia.Esse hexágono expressa a intenção e os recursos do usuário do software com base nas regras de negócios do Hexágono de Domínio.
Com base na mesma topologia e cenário de rede de inventário descritos anteriormente,
suponha que você precise de uma maneira de consultar roteadores do mesmo tipo. Seria necessário algum tratamento de dados para produzir tais resultados. Seu software precisaria capturar alguma entrada do usuário para consultar os tipos de roteador. Você pode querer usar uma regra de negócios específica para validar a entrada do usuário e outra regra de negócios para verificar os dados obtidos de fontes externas.
Se nenhuma restrição for violada, seu software fornecerá alguns dados mostrando uma lista de roteadores do mesmo tipo. Podemos agrupartodas essas diferentes tarefas em um caso de uso. Odiagrama a seguir descreve a estrutura de alto nível do hexágono do aplicativo com base em casos de uso, portas de entrada e portas de saída:
Application

Hexágono de Framework

As coisas parecem bem organizadas com nossas regras críticas de negócios restritas ao
Hexágono de Domínio, seguido pelo Hexágono de Aplicação que lida com algumas operações específicas da aplicação por meio de casos de uso, portas de entrada e portas de saída. Agora chega o momento em que precisamos decidir quais tecnologias devem ter permissão para se comunicar com nosso software.
Essa comunicação pode ocorrer de duas formas, uma conhecida como Driver e outra conhecida como Driven. Para o lado do Driver, usamos adaptadores de entrada, e para o lado doDriven,
usamos adaptadores de saída, conforme o diagrama a seguir:

Framework

Input Adapters

Output Adapters

As operações de Driversão as que solicitam ações ao software. Pode ser um usuário com um cliente de linha de comando ou um aplicativo front-end em nome do usuário, por exemplo. Pode haver alguns conjuntos de teste verificando a exatidão das coisas expostas pelo seu software.Ou podem ser apenas outros aplicativos em um grande ecossistema que precisam interagir com alguns recursos de software expostos.
Essa comunicação ocorre por meio de uma API (Application Programming Interface)
construída sobre os adaptadores de entrada. Essa API define como as entidades externas irão interagir com seu sistema e, em seguida, traduzir sua solicitação para o aplicativo do seu domínio.O termo Driver é usado porque essas entidades externas estão dirigindo o comportamento do sistema. Os adaptadores de entrada podem definir os protocolos de comunicação suportados pelo aplicativo,conforme mostrado aqui:

Do outro lado da moeda, nós temos as Operações Driven. Essas operações são acionadas a partir da sua aplicação e vão para o mundo externo para obter dados a fim de atender às necessidades do software. Uma Operação Driven geralmente ocorre em resposta a alguma condução. Como você pode imaginar, a forma como definimos o lado acionado é através de adaptadores de saída. Esses adaptadores devem estar em conformidade com nossas portas de saída ao implementá-los.
Lembre-se que uma porta de saída nos diz que tipo de dados ela precisa para executar algumas tarefas específicas da aplicação. Cabe ao adaptador de saída descrever como obterá os dados.Vejam um diagrama de adaptadores de saída e Operações Driven:

Principais Vantagens

Se você busca um padrão que o ajude a padronizar a forma como o software é desenvolvido em sua empresa ou até mesmo em projetos pessoais, a arquitetura hexagonal pode ser utilizada como base para criar essa padronização, influenciando como classes, pacotes e a estrutura de código-fonte como um todo estão organizados. A arquitetura hexagonal ajuda as organizações a estabelecer os princípios fundamentais nos quais o software é estruturado. Vamos ver as principais vantagens...
Tolerância a Mudanças

As mudanças tecnológicas estão acontecendo em um ritmo acelerado. Novas linguagens de programação e uma infinidade de ferramentas sofisticadas surgem todos os dias. Para vencer a concorrência, muitas vezes, não basta apenas ficar com tecnologias bem estabelecidas e testadas pelo tempo.
O uso de tecnologia de ponta deixa de ser uma escolha e passa a ser uma necessidade, e se o software não estiver preparado para acomodar tais mudanças, a empresa corre o risco de perder dinheiro e tempo em grandes refatorações porque a arquitetura do software não é tolerante a mudanças.
Dessa forma, a natureza das portas e adaptadores da arquitetura hexagonal nos dá uma grande vantagem ao fornecer os princípios arquitetônicos para criar aplicativos prontos para incorporar mudanças tecnológicas com menos atrito.
Manutenibilidade

Se for necessário alterar alguma regra de negócio, você sabe que a única coisa que deve ser alterada é o Hexágono de Domínio. Por outro lado, se precisarmos permitir que um recurso existente seja acionado por um cliente que usa uma determinada tecnologia ou protocolo que ainda não é suportado pela aplicação, basta criar um novo adaptador, o que só podemos fazer noHexágono de
Framework.

Essa separação de preocupações parece simples, mas quando aplicada como um princípio de arquitetura, ela concede um grau de previsibilidade suficiente para diminuir a sobrecarga mental de compreender as estruturas básicas de software antes de mergulhar profundamente em suas complexidades. O tempo sempre foi um recurso escasso e, se houver uma chance de economizá-lo por meio de uma abordagem de arquitetura que remova algumas barreiras mentais, deve-se ao menos tentar.
Testabilidade

Um dos objetivos finais da arquitetura hexagonal é permitir que os desenvolvedores testem a aplicação quando suas dependências externas não estiverem presentes, como sua interface de usuário e bancos de dados. Isso não significa, entretanto, que essa arquitetura ignore os testes de integração. Em vez disso, permite uma abordagem de integração mais contínua,dando-nos a flexibilidade necessária para testar a parte mais crítica do código, mesmo na ausência de dependências de tecnologia.
Avaliando cada um dos elementos que compõem a arquitetura hexagonal e sabendo das vantagens que ela pode trazer aos nossos projetos, estamos agora munidos dos fundamentos para desenvolver aplicações hexagonais.
(BANRISUL-2022) Em uma arquitetura hexagonal, as classes de domínio independem das classes de infraestrutura, tecnologias e sistemas externos.
Comentários: Perfeito! A arquitetura hexagonal é uma abordagem de design de software projetada para promover o encapsulamento de dependências. Ela separa os componentes de um sistema em três hexágonos: o mais interno, que contém funcionalidades do domínio; e outros dois, que contém funcionalidades de infraestrutura(aplicação e framework). O objetivo dessa arquitetura é isolar os requisitos de negócio da infraestrutura de software,permitindo assim que o código de domínio possa ser reutilizado em diferentes ambientes, como aplicações web, serviços da web, aplicativos móveis ou outras plataformas.Ela também torna mais fácil a substituição de infra estruturas ou tecnologias, pois não há dependências entre o domínio e a infraestrutura, resultando em um código de domínio de alta qualidade e portabilidade (Correto).
