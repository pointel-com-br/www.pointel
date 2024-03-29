# Engenharia de Computadores e Redes - Servidores Web

Índice

1) Sistemas Distribuídos - Teoria

2) Servidores de Aplicação JBoss Wildfly - Teoria

3) Sistemas Distribuídos - Questões Comentadas - Multibancas.

4) Servidores de Aplicação JBoss Wildfly - Questões Comentadas - Multibancas.

5) Sistemas Distribuídos - Lista de Questões - Multibancas.

6) Servidores de Aplicação JBoss Wildfly - Lista de Questões - Multibancas.

7) Servidores Web - Apache - Teoria

8) Servidores Web -1IS - Teoria

9) Servidores Web - Apache - Questões Comentadas - Multibancas.

10) Servidores Web - IIS - Questões Comentadas - Multibancas.

11) Servidores Web - Apache - Lista de Questões - Multibancas.

12) Servidores Web - IIS - Lista de Questões - Multibancas.

Somente 2

SISTEMAS DISTRIBUÍDoS

Vamos começar o assunto com a definição de sistemas distribuídos, segundo dois autores conhecidos. Silberschatz define um sistema distribuído como:
"Uma coleção de processadores que não compartilham a memória ou um clock. Em vez disso,cada processador possui sua própria memória local. Os processadores se comunicam entre si através de diversas redes de comunicações, como barramentos de alta velocidade".
Tanenbaum define que: "Um sistema distribuído é um conjunto de computadores independentes entre si que se apresenta a seus usuários como um sistema único e coerente."
Resumindo, são sistemas que o usuário "enxerga" como um único computador, mas na verdade existem alguns (ou muitos), geograficamente distribuídos. Como as mensagens são trocadas e como é realizado o processamento, o usuário nem fica sabendo (é transparente), ele só recebe o resultado final.
Imagine uma situação em que são necessários diversos cálculos para resolver um problema, como por exemplo, verificar se há sinais enviados através de estrelas ou planetas (vida extraterrestre).Então, quem quiser participar desse projeto, pode ceder processamento de seu computador quando estiver ocioso (através de um programa previamente instalado). Os computadores voluntários realizam os cálculos e enviam resultados a outros computadores. Parece loucura, não?Mas existe esse projeto, é só verificar em <https://www.seti.org/>.

Note que o exemplo acima, que é real, mostra que para um usuário se trata de um único sistema,mas "por baixo dos panos" diversos computadores interagem, realizam cálculos etc. Pode ser que um computador possua processador RISC, outro CISC, um com sistema operacional Unix,Linux,
Windows, Mac OS, e por aí vai. No fim, todos se entendem (de forma transparente) e o usuário vê apenas uma interface.
Quando falamos em transparência, não é apenas em relação à localização. Vamos ver na tabela a seguir que um sistema distribuído pode requerer alguns tipos de transparência.
Transparência Descrição

Acesso Oculta diferenças na representação de dados e no modo de acesso a um recurso.
Localização Oculta o lugar em que um recurso está localizado.

Migração Oculta que um recurso pode ser movido para outra localização.
Relocação Oculta que um recurso pode ser movido para outra localização enquanto em uso.
Semente 3

Replicação
Concorrência

Falha

Oculta que um recurso é replicado.

Oculta que um recurso pode ser compartilhado por diversos usuários concorrentes.
Oculta a falha e a recuperação de um recurso.

Os sistemas distribuídos são muito comuns em ambientes que exigem alta disponibilidade, pois mesmo, que parte dele "caia", o sistema ainda continua operando. Em comparação a um sistema centralizado, as principais vantagens são a possibilidade de crescimento incremental e a possibilidade de implementação de tolerância a falhas através da replicação de processos em unidades de computação distintas.
Vejamos alguns exemplos de sistemas distribuídos bastante conhecidos:

Buscadores:

Google VAtioor

Internet:

Computação em Nuvem:

Spmênte 4

y 72

/

Alguns conceitos recorrentes em provas de concurso são:

Middleware: camada de software localizada logicamente entre uma camada de nível mais alto(usuários e aplicações) e uma camada subjacente (frameworks e facilidades de comunicação). As principais funções da camada de middleware são:
* Ocultar do usuário que a aplicação é executada em diferentes máquinas distribuídas geograficamente;
* Ocultar a heterogeneidade dos sistemas operacionais (ex.: Windows, Linux etc.) e protocolos de comunicação subjacentes.
Ocultar do usuário que a aplicação é executada em diferentes máquinas distribuídas geograficamente
Ocultar a heterogeneidade dos sistemas operacionais e protocolos de comunicação subjacentes
3GL and 4GL
Applications

Applicattons eBusIness XMLExchanges

Proprietary EDI
Fotmats

F

p

Middleware

Messaging
Systems

Application Servers
Transaction Systems

ReldtioiMl

Screen-Based
Systems

Processo: conjunto dos recursos alocados a uma tarefa para sua execução. Um processo é um programa em execução ou uma forma de gerenciar recursos. Cada tarefa precisa de um conjunto de recursos para executar e atingir o seu objetivo: processador, memória,dados, arquivos,
conexões de rede etc.

Escalonamento: em muitas situações pode haver mais de um processo competindo pelo uso de um mesmo recurso. O escalonador do sistema distribuído é o responsável em decidir o nó de processamento responsável pelo processamento da tarefa. Portanto, trata-se de um dos componentes mais importantes, o qual utiliza um algoritmo de escalonamento.
Spménte 5

/ 72

/

As principais características de um sistema distribuído são:

* Concorrência: diferentes nós do sistema distribuído executam-se em concorrência;

* Não há relógio global: os relógios locais não estão necessariamente iguais, assim a única forma de coordenação é por troca de mensagens;
* Falhas independentes: qualquer componente pode falhar de forma independente de outros

As principais características de um sistema distribuído são r
Concorrência Falhas independentes
As vantagens de sistemas distribuídos incluem a possibilidade de seu crescimento incremental(computadores e linhas de comunicação podem ser acrescidos ao sistema), a possibilidade de implementação de aplicações inerentemente distribuídas e a possibilidade de implementação de tolerância a falhas e a replicação de processos em unidades de computação distintas.
As principais motivações para a utilização de um sistema distribuído podem ser:

* Distribuição geográfica (organização com instalações em várias localidades diferentes);

* Necessidade de ligação entre organizações independentes;

* Necessidade de extensibilidade, modularidade ou crescimento gradual;

* Partilha de recursos como troca de informação entre departamentos e/ou empresas;

* Necessidade de maior disponibilidade ou replicação de dados;

* Necessidade de maior desempenho ou de distribuição de carga.

Parece que tem só coisa boa, heim? Não...vamos a alguns desafios:

* Segurança: intrusões podem acarretar na leitura de mensagens em trânsito e/ou a injeção de novas mensagens;
* Escalabilidade: o sistema deve continuar a funcionar de forma eficaz mesmo que haja um crescimento significativo no número de recursos e no número de clientes;
* Heterogeneidade: Equipamentos com representações de dados diferentes
(arquiteturas
RISC, CISC), sistemas operacionais diferentes (Windows, Linux etc.) devem ser integrados no mesmo sistema distribuído.
Spménte 6

/ 72

/

Funções, Modelos/Arquiteturas e Plataformas

Gerenciamento de recursos: a principal tarefa do sistema é garantir o controle sobre quem usa o quê. Esse controle também permite o compartilhamento dos recursos.
Gerenciamento de processos: essa funcionalidade distribui o processamento de forma justa entre as aplicações, evitando que uma aplicação monopolize o recurso. A gerência do processador está diretamente relacionada ao escalonamento. A sensação de que um processador está sendo compartilhado entre os vários processos é dita pseudoparalelismo.
Nos sistemas distribuídos podemos observar o paralelismo real,
típico dos sistemas multiprocessados. O ciclo de processamento típico pode ser resumido da seguinte maneira:
* Requisitar: se a requisição não pode ser atendida imediatamente, então o processo requisitante deve esperar até obter o recurso;
* Usar: O processo pode operar sobre o recurso;

* Liberar: O processo libera o recurso.

Modelo cliente-servidor: os servidores mantêm recursos e servem pedidos de operações sobre esses recursos. Servidores podem ser clientes de outros servidores. Os próprios nomes ajudam a entender (servidor serve recursos e o cliente é quem solicita). Trata-se de uma arquitetura simples e permite distribuir sistemas centralizados muito diretamente, porém é pouco escalável, limitado pela capacidade do servidor e pela rede que o liga aos clientes. Ou seja, um único servidor não consegue atender milhares de clientes de forma satisfatória, por exemplo.
Modelo peer-to-peer: todos os processos possuem papeis semelhantes, sem distinção entre clientes e servidores. As principais características são mais ampla distribuição de carga(computação e rede), maior escalabilidade, o sistema expande-se acrescentando mais pares,
e a coordenação mais complicada que cliente-servidor.
Componentes interagem entre si como "pares" por meio de chamadas/retorno numa rede. Não há hierarquia, como ocorre em um modelo cliente-servidor, e cada par pode interagir com qualquer outro. Exemplos de sistemas distribuídos em Peer-to-Peer (P2P) são abundantes, mas os atualmente mais conhecidos podem ser citados: BitTorrent, uTorrent, eMule, entre outros.
Vamos ver algumas plataformas que dão suporte aos sistemas e aplicações distribuídas:

* Java Messages: gestão de filas de mensagens da plataforma J2EE;

* MSMQ: sistemas de filas de mensagens da Microsoft;

* MQseries: sistemas de filas de mensagens da IBM;

* Active Enterprise: plataforma de integração da fabricante Tibco;

* Biztalk: Enterprise integration broker da Microsoft;

Spménte 7

/ 72

/

São inúmeras as soluções tecnológicas para implementar a distribuição:

* Utilização das interfaces de comunicação distribuída com sockets-,

* Plataformas Cliente-Servidor;

* Brokersóe Mensagens ou Message Oriente d Midd/eware',

* Sistemas de Invocação Remota de Objetos (ex.: RMI ou CORBA);

* Sistemas Operacionais Distribuídos que permitam distribuição de todos os serviços do sistema;
* Web Services.

Cluster x Grid

Agora vamos ver um tópico BASTANTE ABORDADO em provas de concurso, os tipos de sistemas distribuídos: computação em cluster, computação em grade {grid} e computação em nuvem.Vamos focar nos dois primeiros, a seguir.

Clusters são sistemas de processamento compostos por uma coleção de computadores autônomos, interconectados e que trabalham em conjunto para processar uma tarefa.Tipicamente na computação de cluster é utilizada programação paralela na qual um único programa é executado em paralelo. Dependendo do objetivo que se pretenda, podemos ter os seguintes tipos de cluster:
* Cluster de alto desempenho: direcionado a aplicações bastante exigentes no que diz respeito ao processamento;
* Cluster de alta disponibilidade: tem como objetivo permanecer ativo por um longo período e em plena condição de uso. Consegue detectar erros e se proteger de possíveis falhas;
* Cluster de balanceamento de carga: controla a distribuição equilibrada do processamento.
As tarefas de processamento são distribuídas o mais uniformemente possível entre os nós.

As principais vantagens da utilização de clusters são:

* custo-benefício: pode-se obter resultados tão bons quanto ou até superiores que um servidor sofisticado a partir de um conjunto de máquinas simples;
* escalabilidade: é possível aumentar a capacidade de um cluster com a adição de nós ou remover máquinas para reparos sem interromper a aplicação;
* facilidade de personalização para o atendimento da aplicação;

* existência de opções de softwares sem custos de licenciamento para cluster.

Spmênte 8

y 72

/

Resumindo, cluster é um agregado de computadores, um recurso de processamento utilizado em situações em que se exige a alocação exclusiva de um conjunto de recursos por longo período de tempo. Geralmente, existe um nó mestre que gerencia e divide as tarefas entre os demais nós(escravos).

Por exemplo, um software para tentar quebrar uma senha por força bruta pode ser paralelizado em um cluster, sendo que o mestre envia para cada escravo uma fatia das possibilidades de senha(um recebe a fatia de AAAA... até AZZZ..., outro recebe de BAAA... até BZZZ..., e assim por diante,se algum escravo descobrir a senha, avisa ao mestre para que tome as providências de cancelar as tarefas dos demais). Para finalizar o exemplo, esse cluster possui 8 computadores do mesmo modelo, sistema operacional Linux e o programa foi feito em C, com uma biblioteca MPI(para programação paralela).
Importante levar para o prova que um cluster é um sistema fortemente acoplado, ou seja, os computadores compartilham uma rede local, o mesmo sistema operacional em cada computador e há troca de mensagens entre eles. Note que foge um pouco do conceito geral de sistemas distribuídos, ficando mais voltado para um sistema paralelo. Mas para efeito de concurso, os clusters são cobrados junto com os grids (que veremos na sequência).
A computação em grid (grade - em português) possui uma estrutura de processamento descentralizada que não exige um tipo de controle central (não há um nó mestre),trabalhando em um ambiente cooperativo. Possui uma estrutura fracamente acoplada, com múltiplas máquinas interligadas através de uma rede de computadores. Por exemplo, milhares de máquinas no mundo, com sistemas operacionais diferentes, utilizadas para resolver cálculos para encontrar vida extraterrestre (já vimos nesta aula). Não há um requisito de alta disponibilidade dos equipamentos e a localização dos equipamentos é transparente para os usuários.
Spménte 9

/ 72

/

|

: 1. (CESPE/IPHAN - 2018) Cluster e GRID possuem características semelhantes, como o ;
multiprocessamento distribuído, mas se distinguem pelas seguintes razões: cluster é uma j coleção de máquinas paralelas conectadas entre si que, por trabalharem juntas, fornecem alta ;disponibilidade e(ou) balanceamento de carga; o GRID, por sua vez, envolve a integração, j gestão de recursos computacionais fracamente acoplados e geograficamente distribuídos.
i Comentários:

: Um belo resumo! Para o cluster pense em máquinas em uma mesma rede, numa mesma
"sala", :

: são fortemente acoplados (mesmo sistema operacional, mesmo tipo de hardware). Os grids são i
: espalhados pelo mundo, fracamente acoplados (sistemas operacionais e máquinas diferentes). :
\ Portanto, a questão está correta.
i iGabarito: Correta :

;2. (CESPE/TRE-PE - 2015) Os sistemas operacionais têm rotinas que não são executadas de forma ;I
linear, masz sim, concorrentemente, em função de eventos assíncronos.

Spmênte 10

y 72

/

= Comentários:

As rotinas do sistema operacional são executadas conforme as características das tarefas (jobs). i i Existem os jobs do tipo CPU bound e os l/O bound. Os eventos variam conforme a necessidade :
i dos usuários (mais uso do processador ou de dispositivos de entrada/saída). Por isso, a assertiva afirmou que as rotinas são executadas em função de eventos assíncronos! Portanto, a questão está :
i correta.

Gabarito: Correta

Spménte 11

/ 72

/

SERVIDoR DE APLICAçÃo JBoSS/WILDFLY

JBoss é um servidor de aplicação de código fonte aberto baseado na plataforma JEE, é implementado completamente na linguagem de programação Java, podendo ser utilizado em qualquer sistema operacional que suporte essa linguagem.
O JBoss Application Server (AS) é a versão open source, desenvolvida em comunidadesJBoss/RedHat, traz inovações em um ritmo mais rápido com foco em novas funcionalidades,
mas seu principal diferencial é que ele não possui suporte oficial.
O JBoss Enterprise Application Platform (EAP) é a versão paga, normalmente evolui a partir das inovações das versões estáveis do JBoss AS, é integrada com recursos como o JBossDeveloper
Studio e o com o JBoss Operations Network, após um processo de testes
(desempenho,
escalabilidade etc.), além de possuir suporte oficial.

JBoss Application Server (AS)
JBoss Enterprise Application

Platform (EAP)

O JBoss é uma plataforma de middleware1 baseada em padrões abertos, e que mantém conformidade com a especificação Java EE. É servidor de aplicação que provê recursos de alta disponibilidade, dustering, mensageria, cache distribuído, entre outros. Além disso, ele também inclui APIs e frameworks de desenvolvimento para aplicações Java EE escaláveis.
A partir da versão 8 o JBoss passou a se chamar Wildfly, além de ter várias melhorias e mudanças como a troca do container que era o JBossWeb para o Undertow.
Arquitetura e Modos

Na figura a seguir podemos ver a arquitetura do JBoss/Wildfly, cabendo um destaque aos subsistemas, onde encontramos algumas API JEE, tais como EJB, JPA, JMX, Mensageria,entre outros.
1 Software que se encontra entre o sistema operacional e os aplicativos nele executados, funcionando de forma essencial como uma camada oculta de tradução. Permite a comunicação e o gerenciamento de dados para aplicativos distribuídos.
Spmênte 12

Core Infrastructure

Subsystems

Com essa figura fica claro que o JBoss é um servidor de aplicação que implementa diversas características da especificação JEE. Um conceito essencial nas últimas versões é o de domínio.Em um servidor JBoss, um domínio fornece gerenciamento centralizado de várias instâncias de servidor e hosts físicos, enquanto um servidor standalone permite uma única instância do servidor.Configurações, implantações, socket, módulos, extensões e propriedades do sistema podem ser gerenciadas para grupo de servidores. Vamos ver mais detalhes desses dois modos a seguir.
Modo Standalone: é o modo tradicional das versões anteriores. Basicamente implica em ter uma instalação diferente (ou um diretório standalone diferente) para cada instância deWildfly. Ou seja,
para cada Wildfly em execução no seu ambiente é necessário alterar seus próprios arquivo de configuração, suas próprias opções de execução para JVM etc. A inicialização nesse modo é realizada ao iniciar o script JBOSS_HOME/standalone.sh(no Linux) ou
JBOSS_HOME/standalone.bat (no Windows).

Modo Domain: é o modo que foi introduzido no JBoss AS 7, permitindo gerenciar um conjunto de instâncias Wildfly, agrupando-os e assim permitindo compartilhar configurações comuns entre eles. Além de compartilhar configurações, é possível também através de um único console de gerenciamento iniciar ou parar instâncias (ou grupos inteiros), verificar seu status e estatísticas de cada subsystem etc. O gerenciamento das instâncias é coordenado pelo Domain Controller,tendo várias instâncias (JVMs) por Host e o controle total do ciclo de vida dos servidores via HostController. Para iniciar no modo domain é executado o script JBOSS_HOME/domain.sh no
Linux ou JBOSS_HOME/domain.bat no Windows.
Quando o domain.sh (ou o domain.bat) é executado em um host, um processo conhecido comoHost Controller é lançado, o qual é responsável pelo gerenciamento do servidor. Ele não lida diretamente com a carga de aplicações no servidor, sendo responsável por iniciar e terminar os
Spménte 13

/ 72

/

processos que rodam em cada servidor, interagindo com o Domain Controller para ajudar no gerenciamento.
Por padrão, cada Host Controller lê sua configuração no arquivo domain/configuration/host.xml,que possui informações de configuração específicas do host. Abaixo podemos ver uma figura com quatro hosts, um Domain Controller e três Host Controllers, sendo que cada HostController pode ter um ou mais servidores.
A figura acima mostra uma configuração em modo domain, sendo que todas as configurações e o gerenciamento são realizados de forma centralizada, no Domain Controller.Todas as configurações realizadas para o Domain são replicadas nas instâncias JBoss. Adicionar um novo grupo de servidores, configurar logs, criar data sources, alterar portas, entre outras coisas, tudo isso é feito no domain.xml do arquivo de configuração do Domain Controller (master).
Características como clustering, high availability (HA), fail-over e outros recursos do JEE estão disponíveis nos dois modos. Domain Controller é quem controla o gerenciamento do domain.Nele estão as configurações que são compartilhadas entre as instâncias que estão nesse domain,e a política de gerenciamento de todos os servidores. O Domain Controller é basicamente um processo Host Controller que dependendo da arquitetura se torna o Domain Controller.
Foi reduzida a necessidade de editar arquivos de configuração XML
manualmente. O
gerenciamento da segurança é realizado de forma simplificada, inclusive para domínios de segurança. O diretório "modules" centraliza os módulos do servidor de aplicações, em vez do diretório "lib". Os diretórios "domain" e "standalone" possuem os arquivos de configurações para dep/oys (implantações) em modo domain e standalone.
O mecanismo de carga de classe é modular, então os módulos são carregados e descarregados sob demanda, o que propicia uma melhora na segurança, além de menores tempos para iniciar ou reiniciar o servidor. Duas bibliotecas iguais de versões diferentes podem conviver no mesmo servidor.
Spménte 14

/ 72

/

Instalação, Configuração e Implantação

Para a instalação, existe a opção de baixar o JBoss/Wildfly em binário, em arquivo zip ou com um instalador. A maneira mais rápida é fazer o download do binário, e descompactar em um diretório.Há alguns riscos que devem ser evitados na instalação, para evitar falhas de segurança. Assim,após a instalação, há a necessidade de ajustar e personalizar a configuração do servidor, antes de colocar o servidor em produção.
O pré-requisito para instalar o JBoss é o Java Development Kit (JDK) ou Java Runtime
Environment
(JRE) instalado. O download do JBoss/Wildfly pode ser realizado no site da
RedHat. Após o download, os arquivos de instalação devem ser colocados na pasta adequada,para iniciar a instalação.
Após a instalação, é necessário configurar o JBoss/Wildfly como serviço. Não é recomendado iniciá-lo, e deixá-lo configurado com o usuário root, pois isto pode comprometer a segurança de toda a plataforma, já que a plataforma Java oferece APIs para execução de códigos nativos do sistema operacional e mecanismos de gerenciamento remoto.
O ideal é que no Linux seja criado um usuário com privilégios adequados para iniciar o serviço doJBoss, e no Windows seja criado um usuário com poderes administrativos, mas com privilégios reduzidos. Como as questões de concurso geralmente abordam comandos (para a configuração ou para a administração), vamos dar uma olhada...
Após a instalação, é necessário criar um grupo:
## groupadd jboss

Para adicionar o usuário jboss no grupo jboss:

## useradd -s /bin/bash -d /home/jboss -m -g jboss jboss

Na sequência, a criação da estrutura de diretórios para armazenar o JBoss, atribuindo o dono e o grupo "jboss" a essa estrutura:
## mkdir /EAP_HOME/jboss

## chown jboss:jboss /EAP_HOME/jboss
## su jboss

Depois é necessário configurar a senha para que o usuário utilize na conexão entre o HostController e o Domain Controller. Dando continuidade, agora vamos criar os perfis para o domain controler (master) e para os host controllers (slave), baseados no modo Domain e renomeá-los:
Spménte 15

/ 72

/

## cp -Rap /EAP_HOME/domain /EAP_HOME/master
## cp -Rap /EAP_HOME/domain /EAP_HOME/slave01

Após a definição do modo (standalone ou domain), é necessário definir um perfil para oJBoss/Wildfly, que é um conjunto de tecnologias ou subsistemas (subsystems) que serão utilizados na aplicação. Essa definição varia conforme os requisitos de cada sistema. O JBoss possui 4 perfis(profiles) por padrão: default, full, ha, full-ha.

Depois de concluída a configuração inicial, as aplicações devem ser "colocadas"
no JBoss,
processo conhecido como deploy (implantação).

O deploy varia conforme o tipo de perfil (profHe) definido para o JBoss/Wildfly. Vamos ver como é feito o deploy de uma aplicação no JBoss EAP. Primeiro, devemos acessar o consoleWeb na
URL http://x.x.x.x:9990/console/ (onde x.x.x.x é o endereço IP do servidor).
Note que a porta utilizada pelo servidor é a 9990, mas roda a aplicação na 8080. Ou seja, oJBoss/Wildfly roda em uma porta e a aplicação em outra.
Em seguida devem ser inseridos o usuário e a senha, aqueles definidos na instalação.
Para realizar um deploy e o gerenciamento das instâncias pode ser realizado o console:
JBOSS ENTERPRISE c 0

APPLICATION PLATFORM6 0
Profiles server
Runtime d Domam Status
Server Instances

Server Groups

JVM Status

B Subsystem Metrics Server Group

Proflle

Datasources * main-server-group full
JPA other-server-group fúll-ha
JMS Destinations

@ @ 1-2 of 2 0 ®

Transactions

Web Deployments for main-server-group

B Runtime Operations

OSGi

B Deployments

Webservices

Name Runtime Name Enabled
En/Disable Remove sample2.war sample2warDaabie Remove

« 1-1 of1

O deploy também pode realizado feito através da linha de comando, o que propicia maior flexibilidade e facilidade na criação de scdpts de administração. Abaixo um exemplo de deploy para todos os servidores:
## deploy /path/to/test-application.war —all -server-groups

Como já vimos, servidores de aplicação são a interface entre o componente e o sistema operacional específico que o suporta. Antes do componente ser executado no servidor,ele precisa

Spménte 16

/ 72

/

ser montado em uma estrutura que o container possa entender e executar. No
JBoss/Wildfly, a estrutura de empacotamento é definida na especificação JSR 088 Java EE ApplicationDeployment
Specification. Os formatos padrão são WAR, JAR e EAR.

Estrutura de Diretórios

Após a instalação, o JBoss/Wildfly cria uma estrutura de diretórios que deve ser conhecida, pois é necessária para a administração.
* bin/: contém os scripts de inicialização do JBoss EAP, no Linux e no Windows;

* appclient/: contém detalhes de configuração do container da aplicação cliente;

* modules/: contém módulos dinamicamente carregados pelo JBoss EAP quando requeridos pelos serviços;
* standalone/: arquivos de configuração, conteúdo do deploy, e outras áreas utilizáveis quando o JBoss/Wildfly executa como um servidor standalone;
* domain/: contém arquivos de configuração, conteúdo do deploy e outras áreas utilizáveis quando JBoss/Wildfly executa como domínio gerenciado (domain);
* does/: possui diversos tipos de arquivos como exemplos de configuração,
exemplos se como executar o Wildfly como serviço, licenças e outros arquivos que ajudam a aprender mais sobre o Wildfly;
* welcome-content/: diretório de uso interno do servidor que não deve ser modificado por usuários finais, possui páginas de boas vindas e páginas de erros;
* jboss-modules.jar: mecanismo de carga dos módulos.

Além da estrutura de diretórios apresentada, o JBoss/Wildfly cria automaticamente alguns caminhos (paths) padrão:
* jboss.home: diretório root do JBoss EAP;

* user.home: diretório de usuário comum;

* user.dir: diretório de trabalho do usuário atual;

* java.home: diretório de instalação do Java;

* jboss.server.base.dir: diretório root de uma instância de um servidor;

* jboss.server.data.dir: diretório que o servidor usa para persistência de dados no storage;

* jboss.server.log.dir: diretório que o servidor usa no armazenamento de logs;

* jboss.server.tmp.dir: diretório de arquivos temporários;

* jboss.domain.servers.dir: diretório no qual um host controller cria a área de trabalho de uma instância em um domínio gerenciado.
Spménte 17

/ 72

/

ESTA É

DIFÍCIL!

1. (IBFC/EMBASA - 2017) Para que o servidor JBOSS Application Server 7 possa ser plenamente executado, existe a necessidade que esteja previamente instalado e configurado o:
A) JMF

: B) JCE

: C) JXL

D) JDK

! Comentários:

; JBoss é um servidor de aplicação de código fonte aberto baseado na plataforma JEE, é
: implementado completamente na linguagem de programação Java, podendo ser utilizado em i qualquer sistema operacional que suporte essa linguagem.
j Para suportar a linguagem Java, deve haver instalado o JDK (Java Development Kit),
que é um

: ambiente utilizado para o desenvolvimento de softwares em Java. O JDK
inclui o JRE (Java

: Runtime Environment), um interpretador/carregador, um compilador (javac),
entre outros
Ê componentes.

: Pode ter apenas o JRE instalado, que também funciona! Mas nas alternativas só encontramos o
; JDK!

: Portanto, a alternativa D está correta e é o gabarito da questão.

i
Gabarito: Letra D

;2. (FCC/TRT11 - 2017) Após instalar o servidor JBoss AS 5 para Windows, deve-se entrar na pasta

$JBOSS_HOME/bin e digitar run.bat para iniciá-lo. Com o servidor iniciado, para acessar a área de login do JBoss AS Administration Console deve-se digitar,
A) na linha de endereço do navegador, http://localhost:8080/admin-console.
i B) em linha de comando, jboss -a console.

Q-Q SERPRO (Analista - Especialização: Tecnologia) Servidores Web e de Aplicação -

2023 (Pós-Edital) Soménte 18

/ 72

C) na linha de endereço do navegador, http://localhost:8084/settings.

D) em linha de comando, jboss -a mode=console.

E) na linha de endereço do navegador, http://localhost:80/server-console.

Comentários:

O deploy varia conforme o tipo de perfil (profile) definido para o JBoss/Wildfly.
Vamos ver como é feito o deploy de uma aplicação no JBoss EAP. Primeiro, devemos acessar o consoleWeb na
URL http://x.x.x.x:9990/console/ (onde x.x.x.x é o endereço IP do servidor).
Note que a porta utilizada pelo servidor é a 9990, mas roda a aplicação na 8080. Ou seja, oJBoss/Wildfly roda em uma porta e a aplicação em outra.
Note que foi cobrada uma versão mais antiga (AS 5) e teve uma leve variada o nome,
mas o que vale é focar na porta 8080, que é a chave da questão!
Portanto, a alternativa A está correta e é o gabarito da questão.

Gabarito: Letra A

Spménte 19

/ 72

/

QUESTõES CoMENTADAS - SISTEMAS DISTRIBUÍDoS -
MULTIBANCAS

1. (CESPE/MBASA - 2010) Clusters ou combinações de clusters são usados quando os conteúdos são críticos, apesar de não haver necessidade de estarem disponíveis e (ou) processados rapidamente.
Comentários:

Os clusters são estruturas cujo propósito é proporcionar alta disponibilidade,
em situações nas quais há requisitos de criticidade de fornecimento do conteúdo, portanto há a necessidade que estejam disponíveis e geralmente se deseja um processamento rápido. Portanto, a questão está errada.
Gabarito: Errada

2. (IADES/PG-DF - 2011) Segundo Andrew Tanembaum (2007) "Sistema Distribuído é uma coleção de computadores independentes que se apresenta ao usuário como um sistema único e consistente". Assinale a alternativa correta a respeito de um sistema de informação distribuído.
A) A distribuição de tarefas se dá a partir de requisições do usuário, que indica o endereço do servidor onde deseja executar tal tarefa.
B) Em uma rede de computadores há servidores dedicados a atender pedidos dos clientes e estes,por sua vez, têm função exclusiva de requisitantes.

C) Todos os computadores de uma rede executam tarefas de cliente e servidor, quando se deseja integrá-los em uma arquitetura de sistemas distribuídos.
D) A transparência de acesso é uma característica dos sistemas distribuídos que permite que recursos sejam acessados sem que sua localização seja determinada.
E) Em um sistema de objetos distribuídos é possível invocar métodos de um objeto,
ainda que este não esteja presente no computador do usuário.
Comentários:

(A) A distribuição de tarefas indica a tarefa a ser desempenhada, sem indicar o endereço do servidor onde será executada tal tarefa. Lembre que um dos princípios de sistemas distribuídos é a transparência, portanto o usuário não tem ideia qual servidor será utilizado.
Spmênte 20

y 72

/

(B) Em um sistema distribuído não há a figura fixa dos servidores dedicados a atender requisições.

(C) Todos? Se for utilizada a arquitetura peer-to-peer até pode ser, mas quando é utilizada a arquitetura cliente-servidor?
(D) O conceito mostrado é o da transparência de localização, não de acesso! Vejamos:

* Transparência de acesso: oculta diferenças na representação de dados e no modo de acesso a um recurso.
* Transparência de localização: oculta o lugar em que um recurso está localizado.

(E) É isso aí! Em um sistema de objetos distribuídos é possível invocar métodos de um objeto remoto. Para tanto, podemos fazer uso de tecnologias como RMI (Remote MethodInvocation) ou
Corba.

Portanto, a alternativa E está correta e é o gabarito da questão.

Gabarito: Letra E

3. (FCC/TRE-PE - 2011) Arquitetura padrão proposta pelo Object Management Group (OMG)
para estabelecer e simplificar a troca de dados entre sistemas distribuídos heterogêneos por meio de uma estrutura comum para o gerenciamento de objetos distribuídos que é conhecida como Object Manager Architecture (OMA). Trata-se de
A) IDL.

B) RPC.

C) DCON.

D) CORBA.

E) COM.

Comentários:

Uma das possibilidades de invocação de métodos remotos em sistemas distribuídos é através do uso de Corba ou RMI. RMI é mais utilizado, por ser mais simples que Corba. Corba é a arquitetura padrão proposta pelo Object Management Group (OMG) para estabelecer e simplificar a troca de dados entre sistemas distribuídos heterogêneos por meio de uma estrutura comum para o gerenciamento de objetos distribuídos. Portanto, a alternativa D está correta e é o gabarito da questão.
Gabarito: Letra D

Spménte 21

/ 72

/

4. (CESPE/SERPRO - 2013) Com relação à arquitetura de sistemas distribuídos, julgue os próximos itens. Na arquitetura distribuída, os sistemas orientados a eventos possuem processos fortemente acoplados.
Comentários:

Na arquitetura distribuída, os sistemas orientados a eventos possuem processos fracamente acoplados. Portanto, a questão está errada.
Gabarito: Errada

5. (FUNCAB/MDA - 2014) São desvantagens dos sistemas distribuídos:

A) dependência de hardware e custo maior de desenvolvimento.

B) custo maior de desenvolvimento e maior probabilidade de ocorrência de falhas (bugs) no programa.
C) dependência de sistemas operacionais e necessidade de maior processamento.

D) necessidade de maior processamento e pouca disponibilidade.

E) ausência de controle das suas operações e dependência do tipo de rede utilizada para ligar as localidades.
Comentários:

(A) Sistemas distribuídos são heterogêneos (plataformas de hardware e sistemas operacionais distintos). (B) Sistemas distribuídos possuem maior complexidade de desenvolvimento (mais chance de bugs) e maior custo. (C) Sistemas distribuídos não dependem de sistemas operacionais específicos. (D) Sistemas distribuídos estão mais disponíveis. (E) Sistemas distribuídos permitem controle das operações e não dependem do tipo de rede utilizada para ligar as localidades.Portanto, a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

6. (CESPE/TRE-PE - 2015) Os sistemas operacionais têm rotinas que não são executadas de forma linear, mas, sim, concorrentemente, em função de eventos assíncronos.
Comentários:

As rotinas do sistema operacional são executadas conforme as características das tarefas
(jobs).
Existem os jobs do tipo CPU bound e os l/O bound. Os eventos variam conforme a necessidade dos usuários (mais uso do processador ou de dispositivos de entrada/saída). Por isso,a assertiva

Spmênte 22

y 72

/

afirmou que as rotinas são executadas em função de eventos assíncronos! Portanto, a questão está correta.
Gabarito: Correta

7. (CESPE/TJ-DFT - 2015) Nos sistemas implementados a partir do uso de uma arquitetura de componentes distribuídos, o middleware tem a responsabilidade de gerenciar a interação entre esses componentes.
Comentários:

Middleware: camada de software localizada logicamente entre uma camada de nível mais alto(usuários e aplicações) e uma camada subjacente (frameworks e facilidades de comunicação). As principais funções da camada de middleware são:
* Ocultar do usuário que a aplicação é executada em diferentes máquinas distribuídas geograficamente;
* Ocultar a heterogeneidade dos sistemas operacionais (ex.: Windows, Linux etc.) e protocolos de comunicação subjacentes.
Portanto, a questão está correta.

Gabarito: Correta

8. (CESPE/STJ - 2015) A arquitetura orientada a serviços é forma de desenvolvimento de sistemas distribuídos em que os componentes de sistemas são serviços autônomos, razão por que,devido à interoperabilidade, as ligações entre os serviços devem ser rígidas para não provocar mudanças durante sua execução.
Comentários:

Não é o foco de nossa aula a arquitetura orientada a serviços. Mas como é um assunto pertinente,vamos ver... A arquitetura orientada a serviços é forma de desenvolvimento de sistemas distribuídos em que os componentes são autônomos e as ligações entre os serviços devem ser flexíveis durante sua execução. Portanto, a questão está errada.
Gabarito: Errada

9. (IBFC/EBSERH - 2017) Assinale a alternativa correta. Cluster é um conceito que está diretamente relacionado aos sistemas de alta disponibilidade. Existem vários tipos de cluster,no entanto há alguns que são mais conhecidos, como:

A) cluster paralelo - cluster de alta disponibilidade - cluster de três camadas

Spmênte 23

y 72

/

B) cluster de alto desempenho - cluster virtual - cluster matricial

C) cluster paralelo - cluster virtual - cluster para balanceamento de carga

D) cluster de alto desempenho - cluster matricial - cluster de três camadas

E) cluster de alto desempenho - cluster de alta disponibilidade - cluster para balanceamento de carga
Comentários:

Clusters são sistemas de processamento compostos por uma coleção de computadores autônomos, interconectados e que trabalham em conjunto para processar uma tarefa.Tipicamente na computação de cluster é utilizada programação paralela na qual um único programa é executado em paralelo. Dependendo do objetivo que se pretenda, podemos ter os seguintes tipos de cluster:
* Cluster de alto desempenho: direcionado a aplicações bastante exigentes no que diz respeito ao processamento;
* Cluster de alta disponibilidade: tem como objetivo permanecer ativo por um longo período de tempo e em plena condição de uso. Consegue detectar erros e se proteger de possíveis falhas;
* Cluster de balanceamento de carga: controla a distribuição equilibrada do processamento.As tarefas de processamento são distribuídas o mais uniformemente possível entre os nós.

Portanto, a alternativa E está correta e é o gabarito da questão.

Gabarito: Letra E

1O.(FGV/IBGE - 2017) Keyse é gerente de um centro de dados que hospeda distintos tipos de aplicação. Recentemente Keyse recebeu uma solicitação de hospedagem de uma aplicação de missão crítica, a qual requer uma disponibilidade de 99,8% ao ano.
Considerando V para as afirmativas verdadeiras e F para as falsas, analise as características do cluster para atender o requisito de alta disponibilidade do sistema.
( ) capacidade de distribuir igualmente todo o tráfego de entrada entre todos os nós do cluster, para evitar a sobrecarga de requisições a qualquer um deles e o consequente travamento do cluster;
( ) ter nós em espera, em quantidade suficiente, para assumir automaticamente a função de outro nó defeituoso;
( ) realizar processamento da aplicação de forma paralela entre os vários nós do cluster;

Spmênte 24

y 72

/

( ) monitoramento dos nós feito por eles mesmos, por uma rede diferente da rede de dados.
A sequência correta é:

A) V - F - V - F;

B) F - V - F - V;

C) V - V - V - F;

D) V-V-F-F;

E) F - F - V - V.

Comentários:

O foco do cluster é a alta disponibilidade, então vejamos:

(F) Seria verdadeira se o foco fosse o balanceamento de carga!

(V) Ter nós sobrando é importante para garantir a alta disponibilidade, no caso de falhas de outros
(F) O foco é manter o funcionamento (alta disponibilidade) e não paralelizar a execução dos programas (o que seria o foco do alto desempenho).
(V) O monitoramento dos nós feito por eles mesmos, sem depender de "alguém de fora"
e a rede utilizada é separada da rede de dados.
Portanto, a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

11.(CESPE/IPHAN - 2018) Cluster e GRID possuem características semelhantes, como o multiprocessamento distribuído, mas se distinguem pelas seguintes razões: cluster é uma coleção de máquinas paralelas conectadas entre si que, por trabalharem juntas, fornecem alta disponibilidade e(ou) balanceamento de carga; o GRID, por sua vez, envolve a integração,gestão de recursos computacionais fracamente acoplados e geograficamente distribuídos.

Comentários:

Um belo resumo! Para o cluster pense em máquinas em uma mesma rede, numa mesma
"sala",
são fortemente acoplados (mesmo sistema operacional, mesmo tipo de hardware). Os grids são espalhados pelo mundo, fracamente acoplados (sistemas operacionais e máquinas diferentes).Portanto, a questão está correta.

Spménte 25

/ 72

/

Gabarito: Correta

12.(UFLA/UFLA - 2018) O aumento da facilidade de acesso à Internet tem permitido uma grande disponibilização da informação. Para dar suporte a essa facilidade de acesso é necessária uma enorme infraestrutura de hardware e software. Considerando as características de computadores paralelos, analise as proposições a seguir:
I. Um sistema de multiprocessamento simétrico pode ser composto por milhares de computadores com processadores e sistemas operacionais heterogêneos.
II. Um sistema de processamento paralelo em massa visa resolver problemas que exigem capacidade de utilização de memória compartilhada usando um único conjunto de núcleos de processamento localizados em um mesmo computador.
III. Um cluster de computadores é uma coleção de dois ou mais computadores usados para executar um dado problema podendo conter processadores multicore.
IV. Um grid computing provê uma plataforma na qual recursos computacionais são organizados dentro de um ou mais conjuntos lógicos, as tarefas são divididas entre diversos computadores locais ou remotos formando um "super computador virtual".
Assinale a alternativa CORRETA:

A) Somente as proposições I e II estão corretas.

B) Somente as proposições II e III estão corretas.

C) Somente as proposições III e IV estão corretas.

D) Somente as proposições I e IV estão corretas.

Comentários:

(I) Não vimos nesta aula, mas não tem como garantir a simetria com milhares de computadores com processadores e sistemas operacionais distintos!
(II) Um sistema de processamento paralelo (cluster) utiliza troca de mensagens, pois cada computador tem sua memória. Ex.: o mestre envia tarefas aos escravos (via troca de mensagens),os escravos realizam as tarefas e retornam com os resultados. E por aí vai...

(III) Exato, um agregado de computadores (multicore ou não), utilizados para executar um dado problema (ex.: quebrar uma senha por força bruta).
Spménte 26

/ 72

/

(IV) Grid é fracamente acoplado, geralmente "espalhado pelo mundo",
tendo os recursos computacionais organizados dentro de um ou mais conjuntos lógicos. A ideia é possuir um "super computador virtual".
Portanto, a alternativa C está correta e é o gabarito da questão.

Gabarito: Letra C

13.(INSTITUTO AOCP/PC-ES - 2019) Se um servidor Web estiver sobrecarregado, basta agregar novos servidores e dividir a carga de processamento. Considerando o funcionamento dos principais serviços de rede, como é conhecido o esquema de agregação de servidores?
A) SIP Apache.

B) Divserver.

C) Cluster.

D) Upload.

E) ARPANET.

Comentários:

Clusters são sistemas de processamento compostos por uma coleção de computadores autônomos, interconectados e que trabalham em conjunto para processar uma tarefa.Tipicamente na computação de cluster é utilizada programação paralela na qual um único programa é executado em paralelo. Dependendo do objetivo que se pretenda, podemos ter os seguintes tipos de cluster:
* Cluster de alto desempenho: direcionado a aplicações bastante exigentes no que diz respeito ao processamento;
* Cluster de alta disponibilidade: tem como objetivo permanecer ativo por um longo período e em plena condição de uso. Consegue detectar erros e se proteger de possíveis falhas;
* Cluster de balanceamento de carga: controla a distribuição equilibrada do processamento.
As tarefas de processamento são distribuídas o mais uniformemente possível entre os nós.

Portanto, a alternativa C está correta e é o gabarito da questão.

Gabarito: Letra C

14.(UFMG/UFMG - 2019) Um Cluster de Alta Disponibilidade é caracterizado por

Spmênte 27

y 72

/

A) no máximo 2 servidores para redundância ou tolerância a falhas e fontes de energia redundantes, dentre outros dispositivos.
B) diversos servidores para redundância ou tolerância a falhas e fontes de energia redundantes,dentre outros dispositivos.

C) diversos servidores conectados por uma rede wifi e fontes de energia redundantes, dentre outros dispositivos.
D) um único servidor com diversas fontes de energia redundantes ligados a um gerador para que esse servidor quase nunca desligue por falta de energia.
Comentários:

Cluster de alta disponibilidade: tem como objetivo permanecer ativo por um longo período e em plena condição de uso. Consegue detectar erros e se proteger de possíveis falhas.
Ou seja, deve haver diversos servidores e fonte de energia redundante (geradores,
fornecimento de energia por mais de uma empresa etc.). Portanto, a alternativa B está correta e é o gabarito da questão.
Gabarito: Letra B

Spménte 28

/ 72

QUESTõES CoMENTADAS - SERVIDoR DE APLICAçÃo
JBoSS/WILDFLY - MULTIBANCAS

1. (IBFC/EBSERH - 2016) "JBoss é um servidorde código fontebaseado na plataforma e implementado na linguagem de programaçãoAssinale a alternativa que completa correta e respectivamente as lacunas:
A) de arquivos - aberto - JEE - JavaScript

B) de aplicação - fechado - JSE - Java

C) de arquivos - fechado - JEE - JavaScript

D) de aplicação - aberto - JEE - Java

E) de impressão - aberto - JSE - JavaScript

Comentários:

Conceitos básicos que vimos logo no primeiro parágrafo:

JBoss é um servidor de aplicação de código fonte aberto baseado na plataforma JEE, é implementado completamente na linguagem de programação Java, podendo ser utilizado em qualquer sistema operacional que suporte essa linguagem. O JBoss ApplicationServer utiliza o arquivo standalone.bat (ou standalone.sh) para prover a sua inicialização. Portanto, a alternativa Destá correta e é o gabarito da questão.

Gabarito: Letra D

2. (FUNCAB/CREA-AC - 2016) Um administrador de rede instalou o Jboss AS 7 no modo domain.
Nesse caso, um dos processos principais, que coordena as instâncias e distribui o arquivo implantado para todas as instâncias do domínio, é denominado:
A) application process.

B) host controller.

C) JVM process.

D) system controller.

E) standalone controler.

Spménte 29

/ 72

/

Comentários:

Quando o domain.sh (ou o domain.bat) é executado em um host, um processo conhecido comoHost Controller é lançado, o qual é responsável pelo gerenciamento do servidor. Ele não lida diretamente com a carga de aplicações no servidor, sendo responsável por iniciar e terminar os processos que rodam em cada servidor, interagindo com o Domain Controller para ajudar no gerenciamento.
Por padrão, cada Host Controller lê sua configuração no arquivo domain/configuration/host.xml,que possui informações de configuração específicas do host. Abaixo podemos ver uma figura com quatro hosts, um Domain Controller e três Host Controllers, sendo que cada HostController pode ter um ou mais servidores.
Portanto, a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

3. (FCC/TRT11 - 2017) Após instalar o servidor JBoss AS 5 para Windows, deve-se entrar na pasta

$JBOSS_HOME/bin e digitar run.bat para iniciá-lo. Com o servidor iniciado, para acessar a área de login do JBoss AS Administration Console deve-se digitar,
A) na linha de endereço do navegador, http://localhost:8080/admin-console.

B) em linha de comando, jboss -a console.

C) na linha de endereço do navegador, http://localhost:8084/settings.

D) em linha de comando, jboss -a mode=console.

E) na linha de endereço do navegador, http://localhost:80/server-console.

Comentários:

Spmênte 30

y 72

/

O deploy varia conforme o tipo de perfil (profile) definido para o JBoss/Wildfly.
Vamos ver como é feito o deploy de uma aplicação no JBoss EAP. Primeiro, devemos acessar o consoleWeb na
URL http://x.x.x.x:9990/console/ (onde x.x.x.x é o endereço IP do servidor).
Note que a porta utilizada pelo servidor é a 9990, mas roda a aplicação na 8080. Ou seja, oJBoss/Wildfly roda em uma porta e a aplicação em outra.
Note que foi cobrada uma versão mais antiga (AS 5) e teve uma leve variada o nome,
mas o que vale é focar na porta 8080, que é a chave da questão!
Portanto, a alternativa A está correta e é o gabarito da questão.

Gabarito: Letra A

4. (IBFC/EMBASA - 2017) Para que o servidor JBOSS Application Server 7 possa ser plenamente executado, existe a necessidade que esteja previamente instalado e configurado o:
A) JMF

B) JCE

C) JXL

D) JDK

Comentários:

JBoss é um servidor de aplicação de código fonte aberto baseado na plataforma JEE, é implementado completamente na linguagem de programação Java, podendo ser utilizado em qualquer sistema operacional que suporte essa linguagem.
Para suportar a linguagem Java, deve haver instalado o JDK (Java Development Kit), que é um ambiente utilizado para o desenvolvimento de softwares em Java. O JDK inclui o JRE (JavaRuntime Environment), um interpretador/carregador, um compilador (javac),
entre outros componentes.
Pode ter apenas o JRE instalado, que também funciona! Mas nas alternativas só encontramos oJDK!

Portanto, a alternativa D está correta e é o gabarito da questão.

Gabarito: Letra D

5. (FGV/Câmara de Salvador-BA - 2018) No âmbito do JBoss AS 7.x, os modos de operação disponíveis são denominados:
Spmênte 31

y 72

/

A) Domain e Standalone;

B) Elevated e Standard;

C) Local e Remote;

D) Monouser e Multiuser;

E) Open e Authenticated.

Comentários:

Modo Standalone: é o modo tradicional das versões anteriores. Basicamente implica em ter uma instalação diferente (ou um diretório standalone diferente) para cada instância deWildfly. Ou seja,
para cada Wildfly em execução no seu ambiente é necessário alterar seus próprios arquivo de configuração, suas próprias opções de execução para JVM etc. A inicialização nesse modo é realizada ao iniciar o script JBOSS_HOME/standalone.sh(no Linux) ou
JBOSS_HOME/standalone.bat (no Windows).

Modo Domain: é o modo que foi introduzido no JBoss AS 7, permitindo gerenciar um conjunto de instâncias Wildfly, agrupando-os e assim permitindo compartilhar configurações comuns entre eles. Além de compartilhar configurações, é possível também através de um único console de gerenciamento iniciar ou parar instâncias (ou grupos inteiros), verificar seu status e estatísticas de cada subsystem etc. O gerenciamento das instâncias é coordenado pelo Domain Controller,tendo várias instâncias (JVMs) por Host e o controle total do ciclo de vida dos servidores via HostController. Para iniciar no modo domain é executado o script JBOSS_HOME/domain.sh no
Linux ou JBOSS_HOME/domain.bat no Windows.
Portanto, a alternativa A está correta e é o gabarito da questão.

Gabarito: Letra A

6. (FCC/MPE-PE - 2018) Em uma instalação padrão do JBoss Application Server (AS) 7, o diretório que contém a página de boas-vindas do AS é o
A) standalone.

B) welcome-content.

C) appclient.

D) server-welcome.

E) bundles.

Spménte 32

/ 72

/

Comentários:

Após a instalação, o JBoss/Wildfly cria uma estrutura de diretórios que deve ser conhecida, pois é necessária para a administração.
* bin/: contém os scripts de inicialização do JBoss EAP, no Linux e no Windows;

* appclient/: contém detalhes de configuração do container da aplicação cliente;

* modules/: contém módulos dinamicamente carregados pelo JBoss EAP quando requeridos pelos serviços;
* standalone/: arquivos de configuração, conteúdo do deploy, e outras áreas utilizáveis quando o JBoss/Wildfly executa como um servidor standalone;
* domain/: contém arquivos de configuração, conteúdo do deploy e outras áreas utilizáveis quando JBoss/Wildfly executa como domínio gerenciado (domain);
* does/: possui diversos tipos de arquivos como exemplos de configuração,
exemplos se como executar o Wildfly como serviço, licenças e outros arquivos que ajudam a aprender mais sobre o Wildfly;
* welcome-content/: diretório de uso interno do servidor que não deve ser modificado por usuários finais, possui páginas de boas vindas e páginas de erros;
* jboss-modules.jar: mecanismo de carga dos módulos.

Portanto, a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

7. (FCC/CLDF - 2018) Considere que o servidor de aplicações JBoss AS 7 está instalado e configurado em modo padrão em um computador com sistema operacional Windows 10. Para testar se o servidor JBoss está funcionando, utilizando um navegador, deve-se digitar o URL
A) server://127.0.0.1:0800

B) ftp://localhost:0800

C) http://localhost:8080

D) server://localhost:80

E) http://127.0.0.1:80

Comentários:

O deploy varia conforme o tipo de perfil (profile) definido para o JBoss/Wildfly.
Vamos ver como é feito o deploy de uma aplicação no JBoss EAP. Primeiro, devemos acessar o consoleWeb na
URL http://x.x.x.x:9990/console/ (onde x.x.x.x é o endereço IP do servidor).
Note que a porta

Spménte 33

/ 72

/

utilizada pelo servidor é a 9990, mas roda a aplicação na 8080. Ou seja, o
JBoss/Wildfly roda em uma porta e a aplicação em outra. Portanto, a alternativa C está correta e é o gabarito da questão.
Gabarito: Letra C

Spmênte 34

y 72

/

LISTA DE QUESTõES - SISTEMAS DISTRIBUÍDoS -
MULTIBANCAS

1. (CESPE/MBASA - 2010) Clusters ou combinações de clusters são usados quando os conteúdos são críticos, apesar de não haver necessidade de estarem disponíveis e (ou) processados rapidamente.
2. (IADES/PG-DF - 2011) Segundo Andrew Tanembaum (2007) "Sistema Distribuído é uma coleção de computadores independentes que se apresenta ao usuário como um sistema único e consistente". Assinale a alternativa correta a respeito de um sistema de informação distribuído.
A) A distribuição de tarefas se dá a partir de requisições do usuário, que indica o endereço do servidor onde deseja executar tal tarefa.
B) Em uma rede de computadores há servidores dedicados a atender pedidos dos clientes e estes,por sua vez, têm função exclusiva de requisitantes.

C) Todos os computadores de uma rede executam tarefas de cliente e servidor, quando se deseja integrá-los em uma arquitetura de sistemas distribuídos.
D) A transparência de acesso é uma característica dos sistemas distribuídos que permite que recursos sejam acessados sem que sua localização seja determinada.
E) Em um sistema de objetos distribuídos é possível invocar métodos de um objeto,
ainda que este não esteja presente no computador do usuário.
3. (FCC/TRE-PE - 2011) Arquitetura padrão proposta pelo Object Management Group (OMG)
para estabelecer e simplificar a troca de dados entre sistemas distribuídos heterogêneos por meio de uma estrutura comum para o gerenciamento de objetos distribuídos que é conhecida como Object Manager Architecture (OMA). Trata-se de
A) IDL.

B) RPC.

C) DCON.

D) CORBA.

E) COM.

Spmênte 35

y 72

/

4. (CESPE/SERPRO - 2013) Com relação à arquitetura de sistemas distribuídos, julgue os próximos itens. Na arquitetura distribuída, os sistemas orientados a eventos possuem processos fortemente acoplados.
5. (FUNCAB/MDA - 2014) São desvantagens dos sistemas distribuídos:

A) dependência de hardware e custo maior de desenvolvimento.

B) custo maior de desenvolvimento e maior probabilidade de ocorrência de falhas (bugs) no programa.
C) dependência de sistemas operacionais e necessidade de maior processamento.

D) necessidade de maior processamento e pouca disponibilidade.

E) ausência de controle das suas operações e dependência do tipo de rede utilizada para ligar as localidades.
6. (CESPE/TRE-PE - 2015) Os sistemas operacionais têm rotinas que não são executadas de forma linear, mas, sim, concorrentemente, em função de eventos assíncronos.
7. (CESPE/TJ-DFT - 2015) Nos sistemas implementados a partir do uso de uma arquitetura de componentes distribuídos, o middleware tem a responsabilidade de gerenciar a interação entre esses componentes.
8. (CESPE/STJ - 2015) A arquitetura orientada a serviços é forma de desenvolvimento de sistemas distribuídos em que os componentes de sistemas são serviços autônomos, razão por que,devido à interoperabilidade, as ligações entre os serviços devem ser rígidas para não provocar mudanças durante sua execução.
9. (IBFC/EBSERH - 2017) Assinale a alternativa correta. Cluster é um conceito que está diretamente relacionado aos sistemas de alta disponibilidade. Existem vários tipos de cluster,no entanto há alguns que são mais conhecidos, como:

A) cluster paralelo - cluster de alta disponibilidade - cluster de três camadas

B) cluster de alto desempenho - cluster virtual - cluster matricial

C) cluster paralelo - cluster virtual - cluster para balanceamento de carga

D) cluster de alto desempenho - cluster matricial - cluster de três camadas

E) cluster de alto desempenho - cluster de alta disponibilidade - cluster para balanceamento de carga
Spmênte 36

y 72

/

1O.(FGV/IBGE - 2017) Keyse é gerente de um centro de dados que hospeda distintos tipos de aplicação. Recentemente Keyse recebeu uma solicitação de hospedagem de uma aplicação de missão crítica, a qual requer uma disponibilidade de 99,8% ao ano.
Considerando V para as afirmativas verdadeiras e F para as falsas, analise as características do cluster para atender o requisito de alta disponibilidade do sistema.
( ) capacidade de distribuir igualmente todo o tráfego de entrada entre todos os nós do cluster, para evitar a sobrecarga de requisições a qualquer um deles e o consequente travamento do cluster;
( ) ter nós em espera, em quantidade suficiente, para assumir automaticamente a função de outro nó defeituoso;
( ) realizar processamento da aplicação de forma paralela entre os vários nós do cluster;

( ) monitoramento dos nós feito por eles mesmos, por uma rede diferente da rede de dados.
A sequência correta é:

A) V - F - V - F;

B) F - V - F - V;

C) V - V - V - F;

D) V-V-F-F;

E) F - F - V - V.

11. (CESPE/IPHAN - 2018) Cluster e GRID possuem características semelhantes,
como o multiprocessamento distribuído, mas se distinguem pelas seguintes razões: cluster é uma coleção de máquinas paralelas conectadas entre si que, por trabalharem juntas, fornecem alta disponibilidade e(ou) balanceamento de carga; o GRID, por sua vez, envolve a integração,gestão de recursos computacionais fracamente acoplados e geograficamente distribuídos.

12. (UFLA/UFI_A - 2018) O aumento da facilidade de acesso à Internet tem permitido uma grande disponibilização da informação. Para dar suporte a essa facilidade de acesso é necessária uma enorme infraestrutura de hardware e software. Considerando as características de computadores paralelos, analise as proposições a seguir:
I. Um sistema de multiprocessamento simétrico pode ser composto por milhares de computadores com processadores e sistemas operacionais heterogêneos.
Spmênte 37

II. Um sistema de processamento paralelo em massa visa resolver problemas que exigem capacidade de utilização de memória compartilhada usando um único conjunto de núcleos de processamento localizados em um mesmo computador.
III. Um cluster de computadores é uma coleção de dois ou mais computadores usados para executar um dado problema podendo conter processadores multicore.
IV. Um grid computing provê uma plataforma na qual recursos computacionais são organizados dentro de um ou mais conjuntos lógicos, as tarefas são divididas entre diversos computadores locais ou remotos formando um "super computador virtual".
Assinale a alternativa CORRETA:

A) Somente as proposições I e II estão corretas.

B) Somente as proposições II e III estão corretas.

C) Somente as proposições III e IV estão corretas.

D) Somente as proposições I e IV estão corretas.

13.(INSTITUTO AOCP/PC-ES - 2019) Se um servidor Web estiver sobrecarregado, basta agregar novos servidores e dividir a carga de processamento. Considerando o funcionamento dos principais serviços de rede, como é conhecido o esquema de agregação de servidores?
A) SIP Apache.

B) Divserver.

C) Cluster.

D) Upload.

E) ARPANET.

14.(UFMG/UFMG - 2019) Um Cluster de Alta Disponibilidade é caracterizado por

A) no máximo 2 servidores para redundância ou tolerância a falhas e fontes de energia redundantes, dentre outros dispositivos.
B) diversos servidores para redundância ou tolerância a falhas e fontes de energia redundantes,dentre outros dispositivos.

C) diversos servidores conectados por uma rede wifi e fontes de energia redundantes, dentre outros dispositivos.
Spménte 38

/ 72

/

D) um único servidor com diversas fontes de energia redundantes ligados a um gerador para que esse servidor quase nunca desligue por falta de energia.
GABARITo

GABARITO

1- Errada 6- Correta
11- Correta

2- E 7- Correta
12- C

3- D 8- Errada
13- C

4- Errada 9- E
14- B

5- B 10- B

Spmênte 39

y 72

/

LISTA DE QUESTõES - SERVIDoR DE APLICAçÃo
JBoSS/WILDFLY - MULTIBANCAS

1. (IBFC/EBSERH - 2016) "JBoss é um servidorde código fontebaseado na plataforma e implementado na linguagem de programaçãoAssinale a alternativa que completa correta e respectivamente as lacunas:
A) de arquivos - aberto - JEE - JavaScript

B) de aplicação - fechado - JSE - Java

C) de arquivos - fechado - JEE - JavaScript

D) de aplicação - aberto - JEE - Java

E) de impressão - aberto - JSE - JavaScript

2. (FUNCAB/CREA-AC - 2016) Um administrador de rede instalou o Jboss AS 7 no modo domain.
Nesse caso, um dos processos principais, que coordena as instâncias e distribui o arquivo implantado para todas as instâncias do domínio, é denominado:
A) application process.

B) host controller.

C) JVM process.

D) system controller.

E) standalone controler.

3. (FCC/TRT11 - 2017) Após instalar o servidor JBoss AS 5 para Windows, deve-se entrar na pasta

$JBOSS_HOME/bin e digitar run.bat para iniciá-lo. Com o servidor iniciado, para acessar a área de login do JBoss AS Administration Console deve-se digitar,
A) na linha de endereço do navegador, http://localhost:8080/admin-console.

B) em linha de comando, jboss -a console.

C) na linha de endereço do navegador, http://localhost:8084/settings.

D) em linha de comando, jboss -a mode=console.

Spménte 40

/ 72

/

E) na linha de endereço do navegador, http://localhost:80/server-console.

4. (IBFC/EMBASA - 2017) Para que o servidor JBOSS Application Server 7 possa ser plenamente executado, existe a necessidade que esteja previamente instalado e configurado o:
A) JMF

B) JCE

C) JXL

D) JDK

5. (FGV/Câmara de Salvador-BA - 2018) No âmbito do JBoss AS 7.x, os modos de operação disponíveis são denominados:
A) Domain e Standalone;

B) Elevated e Standard;

C) Local e Remote;

D) Monouser e Multiuser;

E) Open e Authenticated.

6. (FCC/MPE-PE - 2018) Em uma instalação padrão do JBoss Application Server (AS) 7, o diretório que contém a página de boas-vindas do AS é o
A) standalone.

B) welcome-content.

C) appclient.

D) server-welcome.

E) bundles.

7. (FCC/CLDF - 2018) Considere que o servidor de aplicações JBoss AS 7
está instalado e configurado em modo padrão em um computador com sistema operacional Windows 10. Para testar se o servidor JBoss está funcionando, utilizando um navegador, deve-se digitar o URL
A) server://127.0.0.1:0800

Spmênte 41

y 72

/

B) ftp://localhost:0800

C) http://localhost:8080

D) server://localhost:80

E) http://127.0.0.1:80

GABARITo

GABARITO

1- D

2- B

3- A

4- D

5- A

6- B

7- C

Spménte 42

/ 72

/

APACHE

O Apache é um servidor Web livre (possui código-fonte aberto) que funciona em ambiente multiplataforma (Windows, Novell, OS/2, Unix, Linux, FreeBSD etc.). No Linux o servidor utiliza o daemon httpd. Suas funcionalidades são mantidas através de uma estrutura de módulos,permitindo inclusive que o usuário escreva seus próprios módulos.

Em ambientes Unix-like os arquivos de configuração, por padrão, ficam localizados no diretório
/etc/apache. O servidor é configurado por um arquivo denominado httpd.conf e opcionalmente pode haver configurações para cada diretório utilizando arquivos com o nome .htaccess,onde é possível utilizar autenticação de usuário pelo próprio protocolo HTTP (combinação de arquivo
.htaccess com um arquivo .htpasswd, que guardará os usuários e senhas criptografadas).

Existem dois tipos de páginas que podem ser adicionadas ao Apache: a página raiz e subpáginas.A página raiz é especificada através da diretiva DocumentRoot e será mostrada quando se entrar no domínio principal, como http://. Na configuração padrão doApache, DocumentRoot aponta para o diretório /var/www. Esse diretório será assumido como raiz caso os diretórios não sejam iniciados por uma /:
home/estrategia -> aponta para /var/www/home/estrategia

/home/estrategia Aponta para /home/estrategia

Apachectl {Apache HTTP Server Control Interface}', trata-se de um front end para o servidorApache. É utilizado para ajudar o administrador a controlar o funcionamento do daemon httpd. Oscript apachectl pode operar em dois modos:

Apachectl *trata-se de um front endpara o servidor

* Front end simples que configura quaisquer variáveis de ambiente necessárias e então chama o httpd, passando argumentos de linha de comando;
* Script de inicialização, recebendo argumentos simples como start, restart, e stop,

traduzindo-os em sinais apropriados ao httpd.

Quando utilizado no modo de script de inicialização, o apachectl aceita como argumentos
(pode-
se utilizar "-k" antes do argumento):

* start: inicializa o daemon httpd;

Spménte 43

/ 72

/

* stop: finaliza o daemon httpd;

* restart: reinicializa o daemon httpd. Se não estiver rodando, o httpd é inicializado;

* fullstatus: mostra um relatório completo do status do mod_status. Para isso, o módulo mod_status deve estar habilitado;
* status: mostra um relatório resumido do status. Similar à opção fullstatus, mas a lista de requisições correntes que estão sendo servidas é omitida;
* graceful: reinicializa o daemon de forma "gentil". Se não estiver rodando, o httpd é inicializado. A diferença para uma inicialização normal é que as conexões correntes não são abortadas;
* graceful-stop: finaliza o daemon de forma "gentil". A diferença para uma finalização normal é que as conexões correntes não são abortadas;
* configtest: executa um teste no arquivo de configuração. Após verificar a sintaxe, informa se está ok ou aponta os erros encontrados.
Para inicializar o httpd, vimos que um comando possível é apachectl start, mas há outras formas também, dependendo da distribuição utilizada:
* Red Hat: service httpd start;

* Ubuntu: /etc/init.d/apache2 start.

O argumento "start" pode ser trocado por "restart", "stop" etc., para as demais ações.

Segurança: o servidor dispõe de um módulo "mod_ssl", o qual adiciona a capacidade do servidor atender requisições utilizando o protocolo HTTPS. Esse protocolo utiliza uma camada SSLpara criptografar todos os dados transferidos entre o cliente e o servidor,provendo maior grau de segurança, confidencialidade e confiabilidade dos dados. A camada SSL é compatível com certificados X.509, que são os certificados digitais fornecidos e assinados por grandes entidades certificadoras no mundo.
Diretivas

Diretrizes (ou diretivas) nos arquivos de configuração (httpd.confe .htaccess) podem ser aplicadas ao servidor inteiro ou podem ser restritas na aplicação de determinados diretórios,arquivos, hosts ou URLs. Vamos ver o significado de algumas delas:
<Directory> é utilizada para definir um grupo de diretrizes que devem ser aplicadas apenas ao diretório definido, seus subdiretórios, e aos arquivos dentro deles. Exemplo:
<Directory '7usr/local/httpd/htdocs">
Options Indexes FollowSymLinks

</Directory>

Spménte 44

/ 72

/

<Files> limita o escopo das diretrizes pelos de nomes de arquivos. Funciona igual ao
<Directory>,
mas agora o foco são arquivos. Exemplo:

<Files "?at.*">

## Aplica-se a cat.html, bat.html, hat.php etc., pois "?" significa um caractere qualquer
## e * significa qualquer coisa daquela posição em diante

## Colocar as diretrizes aqui

</Files>

<VirtualHost> permite servir mais de um site no mesmo servidor (sites virtuais). Podem ser utilizadas diretivas específicas para o controle do site virtual, como nome do administrador, erros de acesso a página, controle de acesso e outros dados úteis para personalizar e gerenciar o site.
Virtual Hosts baseados em nome: utiliza nomes para identificar os sites servidos e requerem somente um endereço IP. Assim é possível servir um número ilimitado de sites virtuais. Onavegador do cliente deve suportar os cabeçalhos necessários para garantir o funcionamento desse recurso (os navegadores mais comuns possuem tal suporte). Exemplo:
<VirtualHost www.sitel .com.br>
ServerName www.sitel.com.br
ServerAdmin site1@site1.com.br

DocumentRoot /var/www/www_site1_com_br
TransferLog /var/log/apache/site1/access.log
ErrorLog /var/log/apache/site1/error.log

User www-data

Group www-data

</VirtualHost>

<VirtualHost www.site2.com.br>

ServerName www.site2.com.br
DocumentRoot /var/www/www_site2_com_br

Spménte 45

/ 72

/

CustomLog /var/log/apache/site2/access.log combined
ErrorLog /var/log/apache/site2/error.log

</VirtualHost>

A diretiva Listen instrui o httpd a escutar endereços IP específicos ou portas específicas. Por padrão o servidor responde a requisições em todas interfaces IP. Essa diretiva é obrigatória (a partir da versão 2.4), ou seja, se não estiver presente no arquivo de configuração, o servidor falhará ao iniciar. Diretivas múltiplas podem ser utilizadas para especificar diferentes endereços ou portas.Exemplo:

Listen 80

Listen 8000

Para especificar duas interfaces e suas portas, utiliza-se, por exemplo:
Listen 192.188.1.1:80

Listen 192.188.1.2:8000

Endereços IPvó devem ser colocados entre colchetes:
Listen [2001 :db8::a00:20ff:fea7:ccea]:80

Para o protocolo HTTPS (HTTP seguro), a porta padrão é 443, ou seja, se nada for especificado, o servidor assume essa porta. Para configurar outra porta:
Listen 192.188.1.2:9443 https

A diretiva Indexlgnore adiciona à lista de arquivos a serem escondidos quando listar um diretório.Pode utilizar caracteres coringas ("?" e "*"). Múltiplas diretivas Indexlgnore acrescentam na lista,ao invés de substituir. Por padrão, a lista contém "." (o diretório corrente). Exemplo:

<Directory '7var/www">

Indexlgnore *.bak .??* *# HEADER* README* RCS CVS *,v *,t

</Directory>

A diretiva KeepAlive habilita/desabilita conexões HTTP persistentes.
MaxKeepAliveRequests define o número máximo de requisições permitidas (0 = sem limite). KeepAliveTimeout define o tempo (em segundos) a esperar para a próxima requisição do mesmo cliente (na mesma conexão).Exemplo:

Q-Q SERPRO (Analista - Especialização: Tecnologia) Servidores Web e de Aplicação - 2023
(Pós-Edital) Sj lente 46
KeepAlive On
MaxKeepAliveRequests 50

KeepAliveTimeout 10

ESTA CAI NA

PROVA!

*
.

: 1. (Quadrix/CRM-PR - 2018) Um servidor Apache pode hospedar muitos sites web diferentes, ;
simultaneamente, com o uso do método chamado de Virtual hosting.

Ê Comentários:

I

: Exato! E através de diretivas, pode ser utilizada a <VirtualHost>. Portanto, a questão está correta, i
I
I

Gabarito: Correta i

= 2. (CS-UFG/CELG-GT-GO - 2017) Na configuração do Apache HTTP Server (httpd), o uso da ;
diretiva <virtualHost> indica que o servidor Web irá

I

I

A) executar em uma máquina virtual.
i i B) executar em um servidor virtual em ambiente de nuvem:

: C) rodar mais de um website em uma mesma máquina.

D) ser replicado em várias máquinas, embora aparente ser um único host.
i i Comentários:
I

i i <VirtualHost> permite servir mais de um site no mesmo servidor (sites virtuais). Podem ser iÊ utilizadas diretivas específicas para o controle do site virtual, como nome do administrador, erros i i de acesso a página, controle de acesso e outros dados úteis para personalizar e gerenciar o site, i i Portanto, a alternativa C está correta e é o gabarito da questão.i

Gabarito: Letra C

Spmênte 47

y 72

/

IIS (INTERNET INFoRMATIoN SERVICES)

O IIS {Internet Information Services} é um servidor Web criado pela Microsoft para seus sistemas operacionais para servidores. A versão mais recente é o IIS 10 (Windows Server 2016 eWindows
10). A função do IIS no Windows Server é oferecer uma plataforma para a hospedagem de sites,serviços e aplicativos, permitindo a integração das seguintes tecnologias:
ASP.NET, FTP, PHP,
WCF e o próprio IIS.

Uma de suas funcionalidades mais utilizadas é a geração de páginas HTML dinâmicas,
através da tecnologia proprietária ASP {Active Server Pages}, mas também pode utilizar outras tecnologias com adição de módulos de terceiros. Depois do lançamento da plataforma .NET (em 2002),o IIS
ganhou também a função de gerenciar o ASP.NET. Este é formado basicamente por dois tipos de aplicações:
* Páginas Web: tradicionais acessadas por usuários (extensão ASPX);

* Web Services: funções disponibilizadas pela rede, chamada por aplicativos ASMX.

O ASP.NET é compilado antes da execução, trazendo vantagens no desempenho em relação às opções interpretadas, como o ASP e o PHP.
Algumas características do IIS são:

* Maximiza a segurança da Web através de um consumo de servidor reduzido e do isolamento automático de aplicativo;
* Implanta e executa o ASP.NET, o ASP clássico e os aplicativos Web do PHP no mesmo servidor;
* Faz o isolamento de aplicativo concedendo aos processos de trabalho, por padrão, uma identidade exclusiva e uma configuração de área restrita (maior segurança);
* Adiciona e remove os componentes internos do IIS, e até mesmo os substitui por módulos personalizados;
* Agiliza o site através de um cache dinâmico interno e de uma compactação avançada;

* Usa o Gerenciador do IIS para configurar recursos do IIS e administrar sites;

* Usa o protocolo FTP {Fiie Transfer Protocoi} para permitir que proprietários de site carreguem e baixam arquivos;
* Usa o Windows PowerShell para automatizar o gerenciamento da maioria das tarefas de administração do servidor Web;
* Configura vários servidores Web em um farm de servidores que podem ser gerenciados usando o IIS;
* O diretório base do site padrão é "UNIDADE:\lnetpub\wwwroot", geralmente
"C:\lnetpub\wwwroot";

* O diretório base para o FTP é "UNIDADE:\lnetpub\ftproot", geralmente
"C:\inetpub\ftproot" (note que só muda o "www" por "ftp").

Spménte 48

/ 72

/

Vamos falar um pouco sobre pool de aplicativos (app/ication pool- IIS7/7.5):

Um pool de aplicativos define um grupo de um ou mais processos de trabalho,
configurado com definições comuns que atendem uma ou mais aplicações atribuídas a este pool. Cada pool de aplicativos utiliza 1 ou 2 modos de integração .NET (modo integrado e modo clássico) para executar aplicações ASP.NET. O modo definido para o pool de aplicativos define como será processado qualquer requisição que chegar a esse pool.
Modo integrado: permite que o IIS processe requisições no pool de aplicativos utilizando o"Integrated Pipeline", o que permite que os módulos do ASP.NET participem do processamento das requisições.
Modo clássico: utiliza o pipeline de processamento do IIS 6, inicialmente as requisições são processadas através dos módulos do IIS7, as requisições do ASP.NET são transportadas para os"ISAPI Filter - aspnet_isapi.dll", o pipeline de processamento do ASP.NET é separado do pipeline de processamento do IIS7. Ou seja, o fluxo de processamento é muito mais lento do que o modo integrado.
F 1

Modo integrado kÁ

r 1

Modo clássico

L À

* permite que o IIS processe requisições no pool de aplicativos utilizando o "Integrated Pipeline"
* utiliza o pipeline de processamento do IIS 6,
inicialmente as requisições são processadas através dos módulos do IIS7 A
Daria para entrar em detalhes em alguns itens abordados acima, mas para fins de concurso não vale a pena. Vamos focar no que as bancas costumam pedir!
Segurança: No Windows Server, durante a instalação do IIS, há opção de segurança
"Filtragem de solicitações", que serve para analisar as requisições feitas ao servidor Web e impedir alguns ataques de manipulação de URL. Por padrão, a filtragem de solicitações no IIS 7.0permite um comprimento máximo de URL de 4096 caracteres e de cadeia de caracteres de consulta um máximo de 2048 caracteres.
A "Filtragem de solicitações" verifica todas as requisições recebidas no servidor e as filtra com base nas regras definidas pelo administrador. Muitos ataques maliciosos compartilham características em comum, como URLs muito longas ou solicitações de uma ação rara. Ao filtrar as solicitações, há uma tentativa de reduzir o impacto desses tipos de ataques.
Mais duas informações importantes, que valem para os outros servidores Web também:

* A porta padrão para requisições HTTP é a 80;

Spménte 49

/ 72

/

A porta padrão para requisições HTTPS (HTTP seguro) é a 443.

PROVA!

1. (INAZ do Pará/DPE-PR - 2017) No Windows Server 2012, durante a instalação do
Servidor WEB
(IIS), que opção de segurança deve ser utilizada para analisar as requisições feitas ao servidorWeb e impedir os ataques manipulando URLs?

A) Autenticação Digest, resolve o problema do firewall e de redes internas e externas.

B) Autenticação de Mapeamento de Certificado de Cliente.

C) Autenticação do Windows.

D) Restrições de IP e Domínio.

E) Filtragem de solicitações.

Comentários:

Segurança: No Windows Server, durante a instalação do IIS, há opção de segurança
"Filtragem de solicitações", que serve para analisar as requisições feitas ao servidor Web e impedir alguns ataques de manipulação de URL. Por padrão, a filtragem de solicitações no IIS 7.0permite um comprimento máximo de URL de 4096 caracteres e de cadeia de caracteres de consulta um máximo de 2048 caracteres.
A "Filtragem de solicitações" verifica todas as requisições recebidas no servidor e as filtra com base nas regras definidas pelo administrador. Muitos ataques maliciosos compartilham características em comum, como URLs muito longas ou solicitações de uma ação rara. Ao filtrar as solicitações, há uma tentativa de reduzir o impacto desses tipos de ataques.
Portanto, a alternativa E está correta e é o gabarito da questão.

Gabarito: Errada

2. (Colégio Pedro ll/Colégio Pedro II - 2016) Assinale a alternativa que
NÃO apresenta uma característica do servidor de aplicação IIS.
A) Gera páginas HTML dinâmicas.

B) Também é um servidor de aplicativo.

C) Executa códigos PHP, Perl, Javascript e ASP.

D) Usa o protocolo FTP para permitir que proprietários de sites carreguem e baixem arquivos.

Comentários:

De tudo o que é descrito nas alternativas, sabemos que o IIS não executa códigos Perl!Lembrando: O IIS implanta e executa o ASP.NET, o ASP clássico e os aplicativos Web do PHP no mesmo servidor. Portanto, a alternativa C está correta e é o gabarito da questão.
Gabarito: Letra C

Spménte 51

/ 72

/

QUESTõES CoMENTADAS - APACHE - MULTIBANCAS

1. (CESPE/FUB - 2015) O Apache, que provê páginas por meio do protocolo
HTTP, possui código-fonte aberto, funciona em ambiente multiplataforma, tanto no Windows quanto noLinux.

Comentários:

O Apache é um servidor Web livre (possui código-fonte aberto) que funciona em ambiente multiplataforma (Windows, Novell, OS/2, Unix, Linux, FreeBSD etc.). Portanto, a questão está correta.
Gabarito: Correta

2. (CESPE/STJ - 2015) Com relação ao servidor Apache, julgue o próximo item.

As diretrizes <Directory> e <Files> são utilizadas em arquivos htaccess para permitir que usuários controlem o acesso a seus arquivos.
Comentários:

Essas duas diretrizes servem para delimitar quais diretrizes devem ser aplicadas a um diretório(<Directory>) e a arquivos (<Files>). Portanto, a questão está errada.

Gabarito: Errada

3. (CESPE/STJ - 2015) Com relação ao servidor Apache, julgue o próximo item.

Um administrador pode incluir uma configuração para determinado diretório por meio da diretriz <Directory>.
Comentários:

<Directory> é utilizada para definir um grupo de diretrizes que devem ser aplicadas apenas ao diretório definido, seus subdiretórios, e aos arquivos dentro deles. Exemplo:
<Directory "/usr/local/httpd/htdocs">
Options Indexes FollowSymLinks

</Directory>

Portanto, a questão está correta.

Spménte 52

/ 72

/

Gabarito: Correta

4. (FCC/Prefeitura de Teresina-PI - 2016) Uma das formas de se iniciar o servidor Apache é por meio do comando
A) apache inic

B) apachectl start

C) apachectl run

D) apachectl go

E) apache send
Comentários:

Quando utilizado no modo de script de inicialização, o apachectl aceita como argumentos:

* start: inicializa o daemon httpd;

* stop: finaliza o daemon httpd;

* restart: reinicializa o daemon httpd. Se não estiver rodando, o httpd é inicializado;

* etc.

Portanto, a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

5. (CESPE/TRT8 - 2016) A diretiva que limita a apresentação dos arquivos que têm a extensão

.conf, em um servidor Apache Web Server, é

A) Deny *.conf

B) Allow - conf

C) Directory *.conf

D) Location - conf

E) Indexlgnore *.conf
Comentários:

Spménte 53

/ 72

/

A diretiva Indexlgnore adiciona à lista de arquivos a serem escondidos quando listar um diretório.Pode utilizar caracteres coringas ("?" e Múltiplas diretivas Indexlgnore acrescentam na lista,ao invés de substituir. Por padrão, a lista contém "." (o diretório corrente). Exemplo:

<Directory '7var/www">

Indexlgnore *.conf

</Directory>

Portanto, a alternativa E está correta e é o gabarito da questão.

Gabarito: Letra E

6. (FIOCRUZ/FIOCRUZ - 2016) São exemplos de comandos para reiniciar o Apache nas versões linux RedHat e Ubuntu, respectivamente:
A) service apache restart ou /etc/init.d/http restart.

B) service httpd restart ou /etc/init.d/apache2 restart.

C) /etc/init.d/apache2 reload ou /etc/init.d/apache2 restart.

D) /etc/init.d/httpd reload ou /etc/init.d/apache2 restart.

E) service apache reload ou /etc/init.d/http reload.

Comentários:

Para inicializar o httpd, vimos que um comando possível é apachectl start, mas há outras formas também, dependendo da distribuição utilizada:
* Red Hat: service httpd start;

* Ubuntu: /etc/init.d/apache2 start.

O argumento "start" pode ser trocado por "restart", "stop" etc., para as demais ações.
Portanto,
a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

7. (CCV-UFC/UFC - 2016) Qual das diretivas abaixo deve ser configurada no arquivo de configuração do servidor Apache para informar se serão aceitas ou não conexões HTTPpersistentes?

Spmênte 54

y 72

/

A) Mutex.

B) Timeout.

C) KeepAlive.

D) CacheEnable.

E) HostnameLookups.

Comentários:

A diretiva KeepAlive habilita/desabilita conexões HTTP persistentes.
MaxKeepAliveRequests define o número máximo de requisições permitidas (0 = sem limite). KeepAliveTimeout define o tempo (em segundos) a esperar para a próxima requisição do mesmo cliente (na mesma conexão).Exemplo:

KeepAlive On
MaxKeepAliveRequests 50

KeepAliveTimeout 10

Portanto, a alternativa C está correta e é o gabarito da questão.

Gabarito: Letra C

8. (CS-UFG/CELG-GT-GO - 2017) Na configuração do Apache HTTP Server (httpd), o uso da diretiva <virtualHost> indica que o servidor Web irá
A) executar em uma máquina virtual.

B) executar em um servidor virtual em ambiente de nuvem

C) rodar mais de um website em uma mesma máquina.

D) ser replicado em várias máquinas, embora aparente ser um único host.

Comentários:

<VirtualHost> permite servir mais de um site no mesmo servidor (sites virtuais). Podem ser utilizadas diretivas específicas para o controle do site virtual, como nome do administrador, erros de acesso a página, controle de acesso e outros dados úteis para personalizar e gerenciar o site.
Portanto, a alternativa C está correta e é o gabarito da questão.

Gabarito: Letra C

Spmênte 55

y 72

/

9. (SUGEP-UFRPE/UFRPE - 2018) Numa instalação com o Servidor Apache existe a necessidade de alterar o arquivo de configuração. O arquivo de configuração padrão doApache é o arquivo:
A) httpd.conf

B) apch.ini

C) http.confg

D) apache.ini

E) apch.conf
Comentários:

No Linux é muito comum que o arquivo de configuração tenha a "extensão" .conf e muitas vezes o nome do arquivo é o mesmo nome do daemon, então fica httpd.conf. Ok, e noWindows? Segue o mesmo nome! Portanto, a alternativa A está correta e é o gabarito da questão.
Gabarito: Letra A

10. (CESPE/ABIN - 2018) A determinação da porta e do endereço que o servidor Apache irá escutar deve ser feita por meio da diretiva listen. Sem sua definição, o servidorApache se mantém fora de operação.
Comentários:

A diretiva Listen instrui o httpd a escutar endereços IP específicos ou portas específicas. Por padrão o servidor responde a requisições em todas interfaces IP. Essa diretiva é obrigatória (a partir da versão 2.4), ou seja, se não estiver presente no arquivo de configuração, o servidor falhará ao iniciar.
Pessoal, a questão não deixa claro qual a versão do Apache! Segundo a documentação, a partir da versão 2.4 seria obrigatória a diretiva listen! Na minha opinião, caberia recurso,pois a banca definiu como errada a questão!
Portanto, a questão está errada.

Gabarito: Errada
11.(Quadrix/CRM-PR - 2018) Um servidor Apache pode hospedar muitos sites web diferentes,
simultaneamente, com o uso do método chamado de Virtual hosting.

Spménte 56

/ 72

/

Comentários:

Exato! E através de diretivas, pode ser utilizada a <VirtualHost>. Portanto, a questão está correta.
Gabarito: Correta

12. (FGV/Prefeitura de Niterói-RJ - 2018) O arquivo httpd.conf é o arquivo de configuração principal do servidor Web Apache. Ele contém diretivas que controlam o funcionamento do servidor.
Assinale a opção que indica a diretiva que pode ser usada para especificar endereço e portas alternativas para o servidor web receber requisições externas.
A) ServerRoot

B) Listen

C) AcceptFilter

D) Redirect

E) SetlnputFilter
Comentários:

Para especificar duas interfaces e suas portas, utiliza-se, por exemplo:
Listen 192.188.1.1:80

Listen 192.188.1.2:8000

Portanto, a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

13. (CESPE/EBSERH - 2018) Para que arquivos para funcionamento de um sítio web armazenados no diretório /var/www/sitio01 fiquem acessíveis via HTTP usando o Apache, é necessário incluir, no arquivo de configuração do servidor, a seguinte linha.
DocumentRoot /var/www/sitio01
Comentários:

Existem dois tipos de páginas que podem ser adicionadas ao Apache: a página raiz e subpáginas.A página raiz é especificada através da diretiva DocumentRoot e será mostrada quando se entrar
Spmênte 57

y 72

/

no domínio principal, como http://. Na configuração padrão doApache, DocumentRoot aponta para o diretório /var/www. Esse diretório será assumido como raiz caso os diretórios não sejam iniciados por uma /:
home/estrategia -> aponta para /var/www/home/estrategia

/home/estrategia -> Aponta para /home/estrategia
Portanto, a questão está correta.

Gabarito: Correta

14.(FCC/SEMEF Manaus-AM - 2019) Um programador deseja reiniciar o Servidor HTTP
Apache
Versão 2.4 de forma que os visitantes ativos do site possam concluir os downloads em andamento antes de o servidor ser reiniciado. Para isso deve usar o comando
A) apachectl -k graceful

B) apachectl -j restart

C) restartserver -j graceful

D) start -s graceful-stop

E) runserver -j restart
Comentários:

Quando utilizado no modo de script de inicialização, o apachectl aceita como argumentos
(pode-
se utilizar "-k" antes do argumento):

* start: inicializa o daemon httpd;

* stop: finaliza o daemon httpd;

* restart: reinicializa o daemon httpd. Se não estiver rodando, o httpd é inicializado;

* graceful: reinicializa o daemon de forma "gentil". Se não estiver rodando, o httpd é inicializado. A diferença para uma inicialização normal é que as conexões correntes não são abortadas;
* graceful-stop: finaliza o daemon de forma "gentil". A diferença para uma finalização normal é que as conexões correntes não são abortadas;
* etc.

Portanto, a alternativa A está correta e é o gabarito da questão.

Gabarito: Letra A

Spménte 58

/ 72

/

QUESTõES CoMENTADAS - IIS (INTERNET INFoRMATIoN
SERVICES) - MULTIBANCAS

1. (CESPE/MEC - 2011) A partir da instalação do IIS é disponibilizado um sítio-padrão cujas pastas estão instaladas no servidor, no caminho físico c:\lnetpub\wwwroot.
Comentários:

O diretório base do site padrão é
"UNIDADE:\lnetpub\wwwroot", geralmente
"C:\lnetpub\wwwroot". Portanto, a questão está correta.

Gabarito: Correta

2. (FCC/TRT19 - 2011) O serviço que faz do Windows 2003 um Servidor Web é o IIS
(Internet
Information Services). Quando o IIS é instalado da maneira padrão, é disponibilizado um site com uma única página chamada iisstart.htm. Essa página pode ser encontrada no caminho físico
A) c:\lnetpub\wwwroot

B) c:\root\

C) c:\root\www

D) c:\http\www

E) c:\net\web
Comentários:

As bancas gostam dessa...repetindo:

O diretório base do site padrão é
"UNIDADE:\lnetpub\wwwroot", geralmente
"C:\lnetpub\wwwroot". Portanto, a alternativa A está correta e é o gabarito da questão.

Gabarito: Letra A

3. (Quadrix/SERPRO - 2014) IIS e Apache são servidores cuja finalidade é:

A) prover serviços de impressão para o Windows e o Linux, respectivamente.

B) prover serviços WEB.

Spménte 59

/ 72

/

C) prover serviços de WEB e e-mail, respectivamente.

D) prover serviços de WEB para Linux e Windows, respectivamente.

E) viabilizar programas para execução de páginas HTML também conhecidos como browsers.

Comentários:

O Apache surgiu para sistema Unix-like, mas é multiplataforma (existe para
Windows, por exemplo). O IIS é proprietário da Microsoft. Ambos são servidores Web. Portanto, a alternativa Bestá correta e é o gabarito da questão.

Gabarito: Letra B

4. (UFRJ/UFRJ - 2015) Considere as seguintes afirmativas acerca do servidor Web IIS 7:
I - Nesta versão do IIS não é possível mais instalar e configurar o serviço FTP.

II - No IIS 7, os pools de aplicativos podem ser executados dos seguintes modos:
integrado ou clássico.
III - No IIS 7, a porta padrão para servir páginas em HTTPS é a 4343.
Pode-se afirmar que:

A) apenas II e III estão corretas.

B) apenas I e II estão corretas.

C) apenas II está correta.

D) apenas I está correta.

E) I, II e III estão corretas.

Comentários:

(I) O FTP nunca foi desabilitado para o uso com o IIS. (II) Um pool de aplicativos define um grupo de um ou mais processos de trabalho, configurado com definições comuns que atendem uma ou mais aplicações atribuídas a este pool. Cada pool de aplicativos utiliza 1 ou 2 modos de integração
.NET (modo integrado e modo clássico) para executar aplicações ASP.NET. O modo definido para o pool de aplicativos define como será processado qualquer requisição que chegar a esse pool.
(III) A porta padrão para o HTTPS é 443 e a do HTTP é a 80. Portanto, a alternativa C está correta e é o gabarito da questão.
Gabarito: Letra C

Spmênte 60

y 72

/

5. (Colégio Pedro ll/Colégio Pedro II - 2016) Assinale a alternativa que
NÃO apresenta uma característica do servidor de aplicação IIS.
A) Gera páginas HTML dinâmicas.

B) Também é um servidor de aplicativo.

C) Executa códigos PHP, Perl, Javascript e ASP.

D) Usa o protocolo FTP para permitir que proprietários de sites carreguem e baixem arquivos.

Comentários:

De tudo o que é descrito nas alternativas, sabemos que o IIS não executa códigos Perl!Lembrando: O IIS implanta e executa o ASP.NET, o ASP clássico e os aplicativos Web do PHP no mesmo servidor. Portanto, a alternativa C está correta e é o gabarito da questão.
Gabarito: Letra C

6. (IBFC/EBSERH - 2016) Ao ser instalado o IIS (Internet Information Services), no disco rígido C:,por padrão os diretórios que serão criados para hospedagem de páginas e para FTP serão respectivamente:
A) C:/iisserver/wwwroot e C:/iisserver/ftproot

B) C:/inetpub/wwwroot e C:/inetpub/ftproot

C) C:/iisserver/wwwdir e C:/iisserver/ftpdir

D) C:/inetpub/wwwdir e C:/inetpub/ftpdir

E) C:/inetpub/rootwww e C:/inetpub/rootftp
Comentários:

Para hospedagem, já vimos em algumas questões que é "C:\inetpub\wwwroot" (note que a barra está invertida nas alternativas, mas tudo bem). Para o FTP é só substituir o "www" por "ftp":"C:\inetpub\ftproot".

Portanto, a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

Spmênte 61

y 72

/

7. (FCC/TRE-SP - 2017) Hipoteticamente, o Técnico, responsável pela administração do servidor com Windows Server 2012 do TRE-SP, realizou a instalação do serviço IIS com a configuração padrão de fornecimento. Considerando-se que ele não atribuiu o endereço IP e desligou o servidor da rede de computadores para evitar acesso externo, para que esse profissional realize o teste local do servidor IIS, ele deve utilizar um navegador e acessar, naBarra de endereços do navegador, a URL:
A) http://127.0.0.1

B) ftp://10.0.0.1

C) https://192.168.0.1

D) http://192.168.0.1

E) https://255.255.255.0
Comentários:

Na verdade, essa não é uma questão exclusiva para o IIS, pode ser para o Apache ou outro servidorWeb! Para testar o servidor Web que está instalado na própria máquina é só fazer referência ao protocolo HTTP e o endereço do localhost (127.0.0.1), ou seja: "http://127.0.0.1". Se você colocar agora em seu navegador não deve aparecer uma mensagem como "Não é possível acessar esse site", a não ser que você tenha instalado um servidor Web (IIS, Apache ou outro)!Portanto, a alternativa A está correta e é o gabarito da questão.
Gabarito: Letra A

8. (INAZ do Pará/DPE-PR - 2017) No Windows Server 2012, durante a instalação do
Servidor WEB
(IIS), que opção de segurança deve ser utilizada para analisar as requisições feitas ao servidorWeb e impedir os ataques manipulando URLs?

A) Autenticação Digest, resolve o problema do firewall e de redes internas e externas.

B) Autenticação de Mapeamento de Certificado de Cliente.

C) Autenticação do Windows.

D) Restrições de IP e Domínio.

E) Filtragem de solicitações.

Comentários:

Spménte 62

/ 72

/

Segurança: No Windows Server, durante a instalação do IIS, há opção de segurança
"Filtragem de solicitações", que serve para analisar as requisições feitas ao servidor Web e impedir alguns ataques de manipulação de URL. Por padrão, a filtragem de solicitações no IIS 7.0permite um comprimento máximo de URL de 4096 caracteres e de cadeia de caracteres de consulta um máximo de 2048 caracteres.
A "Filtragem de solicitações" verifica todas as requisições recebidas no servidor e as filtra com base nas regras definidas pelo administrador. Muitos ataques maliciosos compartilham características em comum, como URLs muito longas ou solicitações de uma ação rara. Ao filtrar as solicitações, há uma tentativa de reduzir o impacto desses tipos de ataques.
Portanto, a alternativa E está correta e é o gabarito da questão.

Gabarito: Letra E

9. (IBFC/IDAM - 2019) Quanto às diferenças entre os servidores Apache e
IIS, analise as afirmativas abaixo, dê valores Verdadeiro (V) ou Falso (F).
( ) o Apache pode rodar em várias plataformas como o Windows, Unix e Linux.
( ) normalmente o servidor IIS utiliza a sua linguagem proprietária o ASP.

( ) somente o Apache é capaz de responder as requisições HTTP de máquinas clientes.
Assinale a alternativa que apresenta a sequência correta de cima para baixo.

A) V, F, F

B) V, V, F

C) F, V, V

D) F, F, V
Comentários:

(V) O Apache é multiplataforma, se você entrar do site http://apache.org/, poderá ver opções de download para Windows e Linux, por exemplo.
(V) Não somente o ASP, que é proprietária a Microsoft, como também outras linguagens.

(F) Claro que não! O IIS também faz isso! Além de outros servidores Web, pois isso é o conceito fundamental!
Portanto, a alternativa B está correta e é o gabarito da questão.

Gabarito: Letra B

Spmênte 63

y 72

/

LISTA DE QUESTõES - APACHE - MULTIBANCAS

1. (CESPE/FUB - 2015) O Apache, que provê páginas por meio do protocolo
HTTP, possui código-fonte aberto, funciona em ambiente multiplataforma, tanto no Windows quanto noLinux.

2. (CESPE/STJ - 2015) Com relação ao servidor Apache, julgue o próximo item.

As diretrizes <Directory> e <Files> são utilizadas em arquivos htaccess para permitir que usuários controlem o acesso a seus arquivos.
3. (CESPE/STJ - 2015) Com relação ao servidor Apache, julgue o próximo item.

Um administrador pode incluir uma configuração para determinado diretório por meio da diretriz <Directory>.
4. (FCC/Prefeitura de Teresina-PI - 2016) Uma das formas de se iniciar o servidor
Apache é por meio do comando
A) apache inic

B) apachectl start

C) apachectl run

D) apachectl go

E) apache send

5. (CESPE/TRT8 - 2016) A diretiva que limita a apresentação dos arquivos que têm a extensão
.conf, em um servidor Apache Web Server, é

A) Deny *.conf

B) Allow - conf

C) Directory *.conf

D) Location - conf

E) Indexlgnore *.conf

6. (FIOCRUZ/FIOCRUZ - 2016) São exemplos de comandos para reiniciar o Apache nas versões linux RedHat e Ubuntu, respectivamente:
Spménte 64

/ 72

/

A) service apache restart ou /etc/init.d/http restart.

B) service httpd restart ou /etc/init.d/apache2 restart.

C) /etc/init.d/apache2 reload ou /etc/init.d/apache2 restart.

D) /etc/init.d/httpd reload ou /etc/init.d/apache2 restart.

E) service apache reload ou /etc/init.d/http reload.

7. (CCV-UFC/UFC - 2016) Qual das diretivas abaixo deve ser configurada no arquivo de configuração do servidor Apache para informar se serão aceitas ou não conexões HTTPpersistentes?

A) Mutex.

B) Timeout.

C) KeepAlive.

D) CacheEnable.

E) HostnameLookups.

8. (CS-UFG/CELG-GT-GO - 2017) Na configuração do Apache HTTP Server (httpd), o uso da diretiva <virtualHost> indica que o servidor Web irá
A) executar em uma máquina virtual.

B) executar em um servidor virtual em ambiente de nuvem

C) rodar mais de um website em uma mesma máquina.

D) ser replicado em várias máquinas, embora aparente ser um único host.

9. (SUGEP-UFRPE/UFRPE - 2018) Numa instalação com o Servidor Apache existe a necessidade de alterar o arquivo de configuração. O arquivo de configuração padrão doApache é o arquivo:
A) httpd.conf

B) apch.ini

C) http.confg

Spmênte 65

y 72

/

D) apache.ini

E) apch.conf

10. (CESPE/ABIN - 2018) A determinação da porta e do endereço que o servidor Apache irá escutar deve ser feita por meio da diretiva listen. Sem sua definição, o servidorApache se mantém fora de operação.
11. (Quadrix/CRM-PR - 2018) Um servidor Apache pode hospedar muitos sites web diferentes,simultaneamente, com o uso do método chamado de Virtual hosting.

12. (FGV/Prefeitura de Niterói-RJ - 2018) O arquivo httpd.conf é o arquivo de configuração principal do servidor Web Apache. Ele contém diretivas que controlam o funcionamento do servidor.
Assinale a opção que indica a diretiva que pode ser usada para especificar endereço e portas alternativas para o servidor web receber requisições externas.
A) ServerRoot

B) Listen

C) AcceptFilter

D) Redirect

E) SetlnputFilter

13. (CESPE/EBSERH - 2018) Para que arquivos para funcionamento de um sítio web armazenados no diretório /var/www/sitio01 fiquem acessíveis via HTTP usando o Apache, é necessário incluir, no arquivo de configuração do servidor, a seguinte linha.
DocumentRoot /var/www/sitio01

14. (FCC/SEMEF Manaus-AM - 2019) Um programador deseja reiniciar o Servidor HTTP Apache
Versão 2.4 de forma que os visitantes ativos do site possam concluir os downloads em andamento antes de o servidor ser reiniciado. Para isso deve usar o comando
A) apachectl -k graceful

B) apachectl -j restart

C) restartserver -j graceful

D) start -s graceful-stop

Spmênte 66

y 72

/

E) runserver -j restart

GABARITo

GABARITO

1- Correta 6- B
11- Correta

2- Errada 7- C
12- B

3- Correta 8- C
13- Correta

4- B 9- A
14- A

5- E 10- Errada

Spmênte 67

y 72

/

LISTA DE QUESTõES - IIS (INTERNET INFoRMATIoN
SERVICES) - MULTIBANCAS

1. (CESPE/MEC - 2011) A partir da instalação do IIS é disponibilizado um sítio-padrão cujas pastas estão instaladas no servidor, no caminho físico c:\lnetpub\wwwroot.
2. (FCC/TRT19 - 2011) O serviço que faz do Windows 2003 um Servidor Web é o IIS
(Internet
Information Services). Quando o IIS é instalado da maneira padrão, é disponibilizado um site com uma única página chamada iisstart.htm. Essa página pode ser encontrada no caminho físico
A) c:\lnetpub\wwwroot

B) c:\root\

C) c:\root\www

D) c:\http\www

E) c:\net\web

3. (Quadrix/SERPRO - 2014) IIS e Apache são servidores cuja finalidade é:

A) prover serviços de impressão para o Windows e o Linux, respectivamente.

B) prover serviços WEB.

C) prover serviços de WEB e e-mail, respectivamente.

D) prover serviços de WEB para Linux e Windows, respectivamente.

E) viabilizar programas para execução de páginas HTML também conhecidos como browsers.

4. (UFRJ/UFRJ - 2015) Considere as seguintes afirmativas acerca do servidor Web IIS 7:
I - Nesta versão do IIS não é possível mais instalar e configurar o serviço FTP.

II - No IIS 7, os pools de aplicativos podem ser executados dos seguintes modos:
integrado ou clássico.
III - No IIS 7, a porta padrão para servir páginas em HTTPS é a 4343.
Pode-se afirmar que:

A) apenas II e III estão corretas.

Spmênte 68

B) apenas I e II estão corretas.

C) apenas II está correta.

D) apenas I está correta.

E) I, II e III estão corretas.

5. (Colégio Pedro ll/Colégio Pedro II - 2016) Assinale a alternativa que NÃO apresenta uma característica do servidor de aplicação IIS.
A) Gera páginas HTML dinâmicas.

B) Também é um servidor de aplicativo.

C) Executa códigos PHP, Perl, Javascript e ASP.

D) Usa o protocolo FTP para permitir que proprietários de sites carreguem e baixem arquivos.

6. (IBFC/EBSERH - 2016) Ao ser instalado o IIS (Internet Information Services), no disco rígido C:,por padrão os diretórios que serão criados para hospedagem de páginas e para FTP serão respectivamente:
A) C:/iisserver/wwwroot e C:/iisserver/ftproot

B) C:/inetpub/wwwroot e C:/inetpub/ftproot

C) C:/iisserver/wwwdir e C:/iisserver/ftpdir

D) C:/inetpub/wwwdir e C:/inetpub/ftpdir

E) C:/inetpub/rootwww e C:/inetpub/rootftp

7. (FCC/TRE-SP - 2017) Hipoteticamente, o Técnico, responsável pela administração do servidor com Windows Server 2012 do TRE-SP, realizou a instalação do serviço IIS com a configuração padrão de fornecimento. Considerando-se que ele não atribuiu o endereço IP e desligou o servidor da rede de computadores para evitar acesso externo, para que esse profissional realize o teste local do servidor IIS, ele deve utilizar um navegador e acessar, naBarra de endereços do navegador, a URL:
A) http://127.0.0.1

B) ftp://10.0.0.1

SpmêntE 69

y 72

/

C) https://192.168.0.1

D) http://192.168.0.1

E) https://255.255.255.0

8. (INAZ do Pará/DPE-PR - 2017) No Windows Server 2012, durante a instalação do
Servidor WEB
(IIS), que opção de segurança deve ser utilizada para analisar as requisições feitas ao servidorWeb e impedir os ataques manipulando URLs?

A) Autenticação Digest, resolve o problema do firewall e de redes internas e externas.

B) Autenticação de Mapeamento de Certificado de Cliente.

C) Autenticação do Windows.

D) Restrições de IP e Domínio.

E) Filtragem de solicitações.

9. (IBFC/IDAM - 2019) Quanto às diferenças entre os servidores Apache e
IIS, analise as afirmativas abaixo, dê valores Verdadeiro (V) ou Falso (F).
( ) o Apache pode rodar em várias plataformas como o Windows, Unix e Linux.
( ) normalmente o servidor IIS utiliza a sua linguagem proprietária o ASP.

( ) somente o Apache é capaz de responder as requisições HTTP de máquinas clientes.
Assinale a alternativa que apresenta a sequência correta de cima para baixo.

A) V, F, F

B) V, V, F

C) F, V, V

D) F, F, V

Spmênte 70

y 72

/

GABARITo

GABARITO

1- Correta

2- A

3- B

4- C

5- C

6- B

7- A

8- E

9- B

Spménte 71

/ 72

/

