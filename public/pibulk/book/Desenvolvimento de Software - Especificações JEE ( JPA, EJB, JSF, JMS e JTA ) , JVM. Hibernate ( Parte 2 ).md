# Desenvolvimento de Software - Especificações JEE ( JPA, EJB, JSF, JMS e JTA ) , JVM. Hibernate ( Parte 2 )

Índice

1) Java EE - JTA - Teoria

2) Java EE - JTA - Questões Comentadas.

3) Java EE - JTA - Lista de Questões.

4) Java EE - JMS - Teoria

5) Java EE - JMS - Questões Comentadas.

6) Java EE - JMS - Lista de Questões.

7) Java EE - EJB - Teoria

8) Java EE - EJB - Questões Comentadas.

9) Java EE - EJB - Lista de Questões

10) Java EE - CDI e Injeção de Dependência - Teoria x
/

JAVA TRANSACTION API (JTA)

Esse é um tema raro em concursos - eu procurei em centenas de provas e encontrei apenas quatro questões, logo vamos ser breves. Bacana? Bem, o Java EE possui uma API que permite que aplicações executem transações distribuídas, ou seja, transações que acessam e atualizam dados em dois ou mais recursos do computador conectados em rede - trata-se da JavaTransaction
API (JSR 907).

Ele especifica um conjunto de interfaces padronizadas entre um gerenciador (monitor) de transações e as partes envolvidas em um sistema de transação distribuída: a aplicação,o servidor de aplicações, um adaptador de recursos e o gerenciador de recursos, que controla o acesso aos recursos compartilhados afetados por essas transações. Antes de continuar, vamos definir alguns conceitos.
Uma transação define uma unidade lógica de trabalho que ou é completamente bem sucedida ou não produz absolutamente nenhum resultado - ou é tudo ou é nada! Uma transação distribuída é simplesmente uma transação que acessa e atualiza dados em dois ou mais recursos compartilhados em rede e, portanto, deve ser coordenada entre esses recursos.
Essa especificação busca padronizar o uso e tratamento de transações distribuídas, permitindo gerenciar transações (Ex: fazer Commit e Rollback), controlando concorrência, paralelismo,integridade de dados e, isso tudo, sem precisar utilizar transações diretamente por meio de umDriver JDBC. As interfaces mais importantes são User Transaction,
Transaction Manager,
Transaction, XA Resource e Xid.

/ 51

/

QUESTõES CoMENTADAS - JTA - MULTIBANCAS

1. (CESPE - 2010 - TRE/BA - Analista de Sistemas) Em um sistema de transação distribuído,o Java Transaction API (JTA) permite especificar um conjunto de interfaces entre o gerenciador de transações e as partes envolvidas.
Comentários:

Ele especifica um conjunto de interfaces padronizadas entre um gerenciador (monitor) de transações e as partes envolvidas em um sistema de transação distribuída: a aplicação,o servidor de aplicações, um adaptador de recursos e o gerenciador de recursos, que controla o acesso aos recursos compartilhados afetados por essas transações. Antes de continuar, vamos definir alguns conceitos.
Conforme vimos em aula, essa especificação contém um conjunto de interfaces para coordenar todas as partes envolvidas. Gabarito: C
2. (CESPE - 2010 - TRE/BA - Analista de Sistemas) JTA pode ser utilizado para o gerenciamento de transações distribuídas.
Comentários:

Esse é um tema raro em concursos - eu procurei em centenas de provas e encontrei apenas sete questões, logo vamos ser breves. Bacana? Bem, o Java EE possui uma API que permite que aplicações executem transações distribuídas, ou seja, transações que acessam e atualizam dados em dois ou mais recursos do computador conectados em rede - trata-se da JavaTransaction API
(JTA).

Conforme vimos em aula, é exatamente essa a função dele! Gabarito: C

3. (FGV - 2009 - FGV - Analista de Sistemas - B) JTA é uma API da linguagem
Java que permite a componentes baseados em Java/J2EE criar, enviar, receber e ler mensagens.
Comentários:

Não, essa questão tenta confundir JTA e JMS! Gabarito: E

x' 4

/ 51

/

4. (FUMARC - 2011 - BDMG - Analista de Sistemas - III) JTA é uma API que padroniza o tratamento de transações dentro de uma aplicação Java.
Comentários:

Essa especificação busca padronizar o uso e tratamento de transações distribuídas, permitindo gerenciar transações (Ex: fazer Commit e Rollback), controlando concorrência, paralelismo,integridade de dados e, isso tudo, sem precisar utilizar transações diretamente por meio de umDriver JDBC. As interfaces mais importantes são User Transaction,
Transaction Manager,
Transaction, XA Resource e Xid.

Conforme vimos em aula, ele de fato padroniza o tratamento de transações dentro de umaAplicação Java. Gabarito: C

/ 51

LISTA DE QUESTõES - JTA - MULTIBANCAS

1. (CESPE - 2010 - TRE/BA - Analista de Sistemas) Em um sistema de transação distribuído,o Java Transaction API (JTA) permite especificar um conjunto de interfaces entre o gerenciador de transações e as partes envolvidas.
2. (CESPE - 2010 - TRE/BA - Analista de Sistemas) JTA pode ser utilizado para o gerenciamento de transações distribuídas.
3. (FGV - 2009 - FGV - Analista de Sistemas - B) JTA é uma API da linguagem
Java que permite a componentes baseados em Java/J2EE criar, enviar, receber e ler mensagens.
4. (FUMARC - 2011 - BDMG - Analista de Sistemas - III) JTA é uma API que padroniza o tratamento de transações dentro de uma aplicação Java.
/ 51

/

GABARITo

GABARITO

1. c

2. C

3. E

4. C

JAVA MESSACE SERVICE (JMS)

Java Message Service (JMS) é uma API Java que possui o intuito de permitir que aplicativos escritos em Java possam criar, receber e enviar mensagens destinadas ou oriundas de outros aplicativos.Galera, esse é um tema que cai pouquíssimo em prova! Quando cai, em geral, basta saber a definição e as características básicas de seu funcionamento. Podemos defini-lo de diversas formas:
* Trata-se de uma especificação para envio e processamento de mensagens entre componentes de software distribuídos.
* Trata-se de uma tecnologia para envio de mensagens entre dois ou mais clientes distintos.

* Trata-se de um middleware que permite que aplicações possam criar, enviar, receber e ler mensagens.
* Trata-se de uma API que permite a comunicação entre diferentes componentes de uma aplicação distribuída.
Todas essas definições estão corretas! Além disso, ele realiza processamentos fracamente acoplados, em que todas as operações que envolvem a troca de mensagens são feitas de forma assíncrona, fazendo com que as aplicações participantes não precisem ficar bloqueadas esperando o término de alguma computação remotamente solicitada (por meio de RPC ou RMI).
Ele define um grupo de interfaces e semânticas que permitem que aplicações Java possam acessar os serviços de qualquer MOM! Professor, o que é isso? É o acrônimo deMessage-Oriented
Middleware, i.e., um middleware que promove a integração das operações de troca de mensagens intra e entre corporações, possibilitando que elementos de negócio sejam intercambiados de forma confiável.
JMS é importante? Sim! Primeiro, a especificação inclui duas estratégias populares de envio de mensagem: ponto a ponto e publish/subscribe. Segundo, ele suporta o envio de mensagens síncronas e assíncronas. Terceiro, ele apoia uma abordagem orientada a eventos para recepção de mensagens. Quarto, muitas implementações fornecem extensiva segurança integrada(Certificação
Digital, Criptografias, etc).

Sobre as estratégias de envio de mensagens citadas acima, temos ponto-a-ponto e publish/subscribe - ambas são bastante parecidas. No primeiro caso, o emissor cria uma fila de mensagens no servidor e envia as mensagens para essa fila. O receptor se registra no servidor para receber as mensagens enviadas para essa fila. Há um relacionamento um-para-um(Unicast)
entre o cliente emissor e o cliente receptor.

/ 51

/

Nesse caso, apenas um receptor irá ler a mensagem. Como se trata de uma comunicação assíncrona, não é necessário que o emissor esteja em execução no momento em que o consumidor lê a mensagem. Da mesma forma, não é necessário que o receptor esteja em execução no momento em que o produtor envia a mensagem. Quando lida a mensagem, o receptor envia um aviso para o emissor.
Msg Msg

Cltent 1 — Sends <—Consumes 1 C|(0nt2

Acknowledges —|

Queue

No segundo caso, o emissor cria um tópico no servidor e publica mensagens para esse tópico. Os receptores se registram (i.e., dão subscribe) no servidor para receber mensagens por tópico. Há um relacionamento um-para-muitos (Multicast) entre o emissor e os receptores.Dessa forma,
diversos receptores podem ler a mensagem publicada no servidor.

Existe também uma dependência temporal entre o emissor e o receptor de um tópico. O
receptor deve permanecer continuamente ativo para receber mensagens. Uma observação de nomenclatura: no primeiro caso, chamamos o emissor de produtor e o receptor de consumidor;no segundo caso, chamamos o emissor de publicador e o receptor de assinante (subscriber).

A Arquitetura JMS possui três elementos principais:

* Provedor: sistema de mensagem que implementa Interfaces JMS e fornece componentes administrativos e de controle.
* Cliente: programas ou componentes, escritos em Java, que produzem e consomem mensagens. Qualquer aplicação Java EE pode ser um cliente.
* Mensagem: trata-se dos objetos que comunicam informações entre Clientes JMS - os dados em si.
, 51

QUESTõES CoMENTADAS - JMS - MULTIBANCAS

1. (CESGRANRIO - 2013 - BNDES - Profissional Básico - Análise de Sistemas - Suporte)
Java
Message Service (JMS) é uma tecnologia voltada para o envio e processamento de mensagens na qual o a) modelo ponto a ponto de troca de mensagens estabelece que cada mensagem enviada para uma fila deve ser recebida por um único consumidor.
b) modelo ponto a ponto de troca de mensagens permite que cada mensagem enviada para uma fila seja lida várias vezes por diferentes consumidores.
c) modelo publish/subscribe de troca de mensagens estabelece que até dois consumidores podem ler o conteúdo de uma mensagem enviada.
d) modelo publish/subscribe de troca de mensagens estabelece que somente um consumidor pode ler o conteúdo de uma mensagem enviada.
e) conceito de tópico de mensagens é usado no modelo ponto a ponto para o envio de uma mensagem em multicast, enquanto o conceito de filas de mensagens é usado no modelo publish/subscribe para o envio de uma mensagem para no máximo um consumidor.
Comentários:

Sobre as estratégias de envio de mensagens citadas acima, temos ponto-a-ponto e publish/subscribe - ambas são bastante parecidas. No primeiro caso, o emissor cria uma fila de mensagens no servidor e envia as mensagens para essa fila. O receptor se registra no servidor para receber as mensagens enviadas para essa fila. Há um relacionamento um-para-um (Unicast) entre o cliente emissor e o cliente receptor.

Conforme vimos em aula, ele possui duas abordagens para envio e processamento de mensagens: ponto-a-ponto e publish/subscribe. No primeiro caso, cada mensagem enviada para uma fila deve ser recebida por um único consumidor (Unicast). Gabarito: A
/ 51

/

2. (CESGRANRIO - 2006 - PETROBRÁS - Analista de Sistemas - D) Para se garantir a entrega de uma mensagem para um único destinatário, o modelo de troca de mensagens publish/subscribe do JMS com o modo de entrega persistente e um assinante durável é mais indicado, enquanto que se a mensagem for para vários destinatários, pode-se utilizar o modelo ponto a ponto doJMS com um modo de entrega persistente.

Comentários:

Sobre as estratégias de envio de mensagens citadas acima, temos ponto-a-ponto e publish/subscribe - ambas são bastante parecidas. No primeiro caso, o emissor cria uma fila de mensagens no servidor e envia as mensagens para essa fila. O receptor se registra no servidor para receber as mensagens enviadas para essa fila. Há um relacionamento um-para-um (Unicast) entre o cliente emissor e o cliente receptor.

No segundo caso, o emissor cria um tópico no servidor e publica mensagens para esse tópico.Os receptores se registram (i.e., dão subscribe) no servidor para receber mensagens por tópico. Há um relacionamento um-para-muitos (Multicast) entre o emissor e os receptores.Dessa forma, diversos receptores podem ler a mensagem publicada no servidor.

Conforme vimos em aula, a questão está invertida! O Modelo Publish/Subscribe é um-para-muitos (Multicast) e o Modelo Ponto-a-Ponto é um-para-um (Unicast). Gabarito: E

3. (CESPE - 2010 - SERPRO - Analista de Sistemas) A API JMS é usada para a construção de sistemas de mensageria na plataforma JEE, sendo algumas de suas características relevantes a assincronia das mensagens, a arquitetura peer-to-peer e o suporte ao estilo de mensageria publish-subscribe.
Comentários:

JMS é importante? Sim! Primeiro, a especificação inclui duas estratégias populares de envio de mensagem: ponto a ponto e publish/subscribe. Segundo, ele suporta o envio de mensagens síncronas e assíncronas. Terceiro, ele apoia uma abordagem orientada a eventos para recepção de mensagens. Quarto, muitas implementações fornecem extensiva segurança integrada(Certificação Digital, Criptografias, etc).

Conforme vimos em aula, a questão está perfeita! Gabarito: C

/ 51

/

LISTA DE QUESTõES -JMS - MULTIBANCAS

1. (CESGRANRIO - 2013 - BNDES - Profissional Básico - Análise de Sistemas - Suporte)
Java
Message Service (JMS) é uma tecnologia voltada para o envio e processamento de mensagens na qual o a) modelo ponto a ponto de troca de mensagens estabelece que cada mensagem enviada para uma fila deve ser recebida por um único consumidor.
b) modelo ponto a ponto de troca de mensagens permite que cada mensagem enviada para uma fila seja lida várias vezes por diferentes consumidores.
c) modelo publish/subscribe de troca de mensagens estabelece que até dois consumidores podem ler o conteúdo de uma mensagem enviada.
d) modelo publish/subscribe de troca de mensagens estabelece que somente um consumidor pode ler o conteúdo de uma mensagem enviada.
e) conceito de tópico de mensagens é usado no modelo ponto a ponto para o envio de uma mensagem em multicast, enquanto o conceito de filas de mensagens é usado no modelo publish/subscribe para o envio de uma mensagem para no máximo um consumidor.
2. (CESGRANRIO - 2006 - PETROBRÁS - Analista de Sistemas - D) Para se garantir a entrega de uma mensagem para um único destinatário, o modelo de troca de mensagens publish/subscribe do JMS com o modo de entrega persistente e um assinante durável é mais indicado, enquanto que se a mensagem for para vários destinatários, pode-se utilizar o modelo ponto a ponto doJMS com um modo de entrega persistente.

3. (CESPE - 2010 - SERPRO - Analista de Sistemas) A API JMS é usada para a construção de sistemas de mensageria na plataforma JEE, sendo algumas de suas características relevantes a assincronia das mensagens, a arquitetura peer-to-peer e o suporte ao estilo de mensageria publish-subscribe.
/

GABARITo

GABARITO

1. A

2. E

3. C

/

Enterprise JavaBeans (EJB) é uma arquitetura para aplicações corporativas orientada à transação e baseada em componentes. Além de uma arquitetura, eles são também componentes server-side que oferecem uma infraestrutura para o desenvolvimento e implantação de aplicações distribuídas, escaláveis, transacionais, seguras, concorrentes, persistentes, e portáteis de maneira fácil de acessar e simples de usar.
O Contêiner EJB é um recipiente (em tempo de execução) para Enterprise
Beans que são implantados em um Servidor de Aplicação. Ele é criado automaticamente quando o servidor é inicializado e oferece serviços como: gerenciamento de ciclo de vida, geração de código,gerenciamento de persistência, gerenciamento de segurança, gerenciamento de transações,controle de concorrência, etc. Vejamos:

Ciclo de Vida: o desenvolvedor não precisa se preocupar com a criação de processos, threads,ativação ou destruição de objetos.

Segurança: o contêiner fornece suporte a autenticação e controle de acesso orientado a papéis.

Transações: o contêiner automaticamente gerencia o início, enrollment, commitment e rollback de transações.
Persistência: beans não precisam se preocupar com sua persistência em um banco de dados.

Estado: o estado conversacional de Beans (se houver) é gerenciado
(salvo/recuperado)
automaticamente.

A estrutura de um Enterprise Bean e seu comportamento em tempo de execução são definidos em um ou mais Descritores de Implantação (Anotações XML). Programadores criam esses arquivos durante o processo de empacotamento de EJB e os descritores se tornam parte da implantação do EJB quando o Enterprise Bean é compilado. O Descritor de Implantação do EJB 3.2 é o ejb-jar.xml.

Os descritores de implantação do J2EE 1.4 eram, em geral, complexos e era fácil cometer erros ao preenchê-los. Em vez disso, a Plataforma Java EE usa Anotações(Annotations), que são modificadores semelhantes a público e privado. O EJB 3, por exemplo, define anotações para o tipo de bean, tipo de interface, referências de recurso, atributos de transação,segurança e muito mais.
Um conjunto de anotações semelhante é fornecido para Web services pela especificação
JAX-WS

2.0. Em geral, anotações são usadas para gerar artefatos; outras para documentar o código; outras mapeiam classes Java para XML; outras mapeiam classes Java para bancos de dados; outras mapeiam métodos para operações; outras especificam dependências externas, entre outros.
Existem vários formatos (Ex: EAR, WAR, JAR) para padronizar o encapsulamento da lógica de negócio sob uma única interface - e o EJB é o núcleo da Tecnologia JavaEE. Bem, esse

/ 51

/

componente é executado no Container EJB de um Servidor de Aplicação! Professor, o que tem de tão especial nessa tecnologia? Cara, ela permite o desenvolvimento rápido e simplificado de aplicações complexas.
LOCAL CONTÊINER COMPONENTE

CLIENTE Aplicação Cliente
Applet

SERVIDOR Web
EJB

Componentes de Aplicação
Applet

Java Servlet

JavaServer Pages (JSP)
JavaServer Faces (JSF)
Enterprise Beans

Em outras palavras, ele deixa o programador livre para se concentrar na lógica de negócio e na resolução do problema. Assim, o desenvolvedor não precisa mais se preocupar com codificação envolvendo infraestrutura (segurança, escalabilidade, entre outros)l.Ademais, eles são extremamente portáveis e reusáveis. Logo, pode-se construir aplicações a partir de beans pré-existentes.

Uma vez construídos seguindo as especificações, eles podem rodar em qualquer
Servidor de
Aplicação Java EE! Professor, agora eu quero usar Enterprise JavaBeans sempre e em qualquer condição - ele é demais! Calma lá, pequeno gafanhoto! E inviável utilizá-lo em algumas condições.É recomendável observar algumas características do sistema de software.

Recomenda-se utilizá-lo caso sua aplicação realmente necessite ser escalável, segura,
transacional,
persistente, escalável, portável, distribuída, etc Se você for desenvolver o sistema de uma padaria,em geral, não é viável utilizar Enterprise JavaBeans. Faça-se algumas perguntas: Muitas pessoas vão acessar o sistema da padaria simultaneamente? Haverá picos de acesso? Épreciso de segurança?
1 Programadores precisam escrever apenas a lógica de negócio em Componentes
EJB. Não precisa implementar nenhuma programação ou serviço em nível de sistema, tais como transações ou segurança, pois isso é oferecido pelo Container EJB.
/

OBJETIVOS GERAIS DA ARQUITETURA EJB

A Arquitetura EJB será a arquitetura de componentes padrão para construção de aplicações corporativas orientadas a objetos em Java.
A Arquitetura EJB suportará o desenvolvimento, implantação e utilização de aplicações corporativas em Java.
A Arquitetura EJB suportará o desenvolvimento, implantação e utilização de Web
Services.

A Arquitetura EJB facilitará a escrita de aplicações: desenvolvedores não terão que entender detalhes de transação, gerenciamento de estados, multithreading, etc.
Aplicações EJB - após desenvolvidas - poderão implantadas em múltiplas plataformas sem necessidade de recompilação ou modificação do código-fonte.
A Arquitetura EJB abordará os aspectos de desenvolvimento, implantação e tempo de execução do ciclo de vida de uma aplicação corporativa.
A Arquitetura EJB definirá os contratos que habilitam ferramentas de vários fabricantes a desenvolver e implantar componentes interoperáveis em runtime.
A Arquitetura EJB tornará possível a criação de aplicativos através da combinação de componentes desenvolvidos utilizando ferramentas de diferentes fabricantes.
A Arquitetura EJB fornecerá interoperabilidade entre Beans Corporativos e componentes do Java EE, bem como aplicações de outras linguagens (não Java).
A Arquitetura EJB será compatível com as plataformas de servidores existentes.
Fornecedores serão capazes de estender seus produtos para apoiar EJBs.

/ 51

/

A Arquitetura EJB será compatível com outras APIs da linguagem de programação
Java.

A Arquitetura EJB será compatível com Protocolos CORBA.

Se realmente for necessário, a Tecnologia EJB é a escolha certa! É legal enfatizar também que aArquitetura EJB é neutra em relação a seus protocolos - pode ser utilizada com HTTP,
IIOP, RMP,
DOM, etc. Pessoal, o Enterprise JavaBean evoluiu muito rápido. Logo, ainda caem algumas questões de prova sobre as novidades do EJB 3.1. Vamos ver o que ele trouxe de novo:
NOVIDADES DO EJB 3.1

Novo tipo de componente (Singleton Session Bean) que implementa o Padrão
Singleton e permite capturar eventos de inicialização e encerramento da aplicação

Interface opcional para componentes - Flexibilização na criação de componentes
EJBs sem a obrigatoriedade da criação de uma interface remota ou local.

Melhorias no serviço de agendamento que permitem novas possibilidades através de uma notação similar ao Unix Cron e agendamento de forma declarativa.
Deploy de EJBs na camada web (.war) - Permite o uso de EJBs diretamente na camada Web.
Chamadas assíncronas a métodos - Uma alternativa simplificada à MDBs para chamada assíncrona que pode ser utilizada em cenários menos complexos.
/ 51

/

Nomes JNDI globais padronizados - Esse recurso facilita ainda mais a portabilidade.
EJB Lite - Define uma versão mais leve para um conteiner de EJBs.

Embeddable EJB - Possibilidade de executar EJBs no ambiente JavaSE.

Os Componentes EJB podem ser acessados diretamente, no entanto ainda podem ser utilizadas as interfaces que são disponibilizadas para acesso remoto ou local. O Bean não implementa essas interfaces, cada fabricante de Servidores de Aplicação provê a implementação para as interfacesRemote e Home definidas para o componente - são respectivamente as interfaces EJB
Object e
EJB Home.

A Interface EJBObject implementa a interface para acessos remotos e locais, e funciona como um wrapper, i.e., encapsulando a instância EJB solicitada pelo cliente. Já a InterfaceEJBHome faz exatamente a mesma coisa, no entanto ela também é responsável por auxiliar o contêiner a gerenciar o ciclo de vida de um Bean - realizando criações, buscas e remoções de objetos.
Existem três tipos de EJB, mas o Entity Bean é opcional a partir do EJB 3.2. Ele só existe na especificação por questão de compatibilidade com versões anteriores, mas sabe-se que ele já foi substituído pela Java Persistence API (JPA). Ademais, como é um EnterpriseJavaBean, eles encapsulam uma lógica de negócio. Pois bem, sobram dois tipos -Message-driven Beans e
Session Beans:

Message-driven Beans (MDB): trata-se de um objeto não-persistente que combina características de um Session Bean e uma escuta/monitor (listener) de mensagens, permitindo a um componente de negócio receber e tratar mensagens de forma assíncrona - geralmente, providas peloJMS.
Pode-se dizer que eles são executados após o recebimento de uma única mensagem do cliente.

Um Contêiner EJB provê um ambiente de execução escalável para executar um grande número de MDBs concorrentemente. Eles podem ser Stateless, apenas. Ademais, devem ser invocados
/ 51

/

por meio de programação por um cliente local ou remoto. Como são não-persistentes, o cliente não acessa um MDB diretamente, mas por meio do JMS enviando mensagens para o destinatário.
Session Beans (SB): trata-se de um objeto não-persistente que implementa alguma lógica de negócio ou fluxo de trabalho no servidor. Eles servem para executar alguma tarefa em nome de um único cliente e implementam a interface javax.ejb.SessionBean, podendo implementar WebServices. O Contêiner EJB provê um ambiente escalável para executar um grande número de SBs concorrentemente.
Um Session Bean encapsula a lógica de negócio que pode ser invocada programaticamente por um cliente localmente, remotamente ou por meio de webservices. Os SBs permitem enviar e receber mensagens JMS, porém somente de forma síncrona. Seus dados não são persistidos em uma base de dados e eles podem ser de três tipos: stateful, stateless e singleton!Vamos vê-los a seguir:
Stateless Session Beans: são objetos de negócio que não mantém estado entre invocações de métodos. Após cada chamada de método, o contêiner pode escolher destruir,recriar ou manter o Bean. Eles podem ter variáveis de instância armazenadas em um pool, no entanto elas serão compartilhadas por vários usuários (entretanto, não de forma concorrente).
1. Dependency injection, if any

2. PostConstruct callbacks, if any

PreDestroy callbacks, if any

Observem o ciclo de vida mostrado acima e percebam que ele tem dois estados: no estágioDoes Not Exist, a instância simplesmente ainda não existe; no estágio Ready,
diversas instâncias podem ser criadas e posicionadas em um pool - prontas para serem utilizadas.Percebam que ela nunca entra em modo passivo para economizar recursos.

Stateful Session Beans: são objetos de negócio que mantém estado entre chamadas de métodos. São projetados, em geral, para situações que requerem várias requisições simultâneas ou transações. Aqui as variáveis de instância representam o estado de uma sessão.Decorem isso: são objetos que mantém o estado entre as chamadas de métodos.

/ 51

1. Create

2. Dependency injection, if any

3. PostConstruct callback, if any

4. Init method, or ejbCreate<MÉTHOD>,

if any PrePassivate

I callback, if any

Does Not F

Exist I

1. Remove

2. PreDestroy callback, if any

Ready

F

PostActivate callback, if any
Passive

Observem o ciclo de vida mostrado acima e percebam que ele tem três estados: no estágioDoes Not Exist, a instância simplesmente ainda não existe; no estágio Ready, a instância está vinculada a um determinado cliente e ocupada em uma conversação; no estágio Passive, a instância sai da memória principal para a memória secundária para economizar recursos.
Singleton Session Beans: são objetos de negócio instanciados uma única vez pela aplicação e existem por todo ciclo de vida da aplicação. São utilizados quando umEnterprise Bean é compartilhado e acesso por vários clientes. Percebam que ele também nunca entra em modo passivo para economizar recursos - assim como os Stateless Session Beans.
1. Dependency injection, if any

2. PostConstruct callbacks, if any

| Ready
L

PreDestroy callbacks, if any

Observem o ciclo de vida mostrado acima e percebam que ele tem apenas dois estados:
no estágio Does Not Exist, a instância simplesmente ainda não existe; já no estágioReady, uma única instância é criada e estará pronta para ter seus métodos de negócio invocados pelos clientes. Trata-se de um ciclo de vida bastante simples, concordam?
Por fim, gostaria de falar um pouco sobre o CDI (Context and Dependency Injection).
Alguém sabe o que é Injeção de Dependência? Trata-se de um design pattern que consiste na passagem de uma classe para outra, sendo que esta última irá utilizá-la
(consumi-la), visando eliminar o forte acoplamento geralmente existente entre os módulos da aplicação e facilitar a realização de testes.
Pessoal, imaginem que eu preciso fazer vários testes unitários. Ora, se toda classe que eu for testar tiver dependendo de outra classe, eu terei que sair instanciando tudo para poder fazer um mero teste unitário. Ademais, se eu faço uma estrutura fracamente acoplada entre classes e módulos,pode-se ganhar em extensibilidade e reusabilidade.

/ 51

/

Basicamente, pode-se implementar a Injeção de Dependência de três formas:
injetam-se as dependências no construtor da classe; injetam-se as dependências no método setter de alguma propriedade; ou injetam-se as dependências via instância de abstração - por meio de interfaces ou classes abstratas. A Especificação CDI é o Padrão Java para injeção de dependência.
Ela fornece uma arquitetura que permite que os componentes Java EE existam dentro do ciclo de vida de um aplicativo com escopos bem definidos. Além disso, os serviços CDI permitem que os componentes Java EE, tais como EJB Session Beans e JSF Managed Beans, sejam injetados e interajam de uma maneira fracamente acoplada e flexível, iniciando e observando eventos.
/ 51

/

QUESTõES CoMENTADAS - EJB - MULTIBANCAS

1. (FCC - 2011 - TRT/19 - Analista de Sistemas) Tipo de session bean EJB 3.1 cujas instâncias não têm estado conversacional, isto é, todas as instâncias são equivalentes quando não estão envolvidas em atender um método invocado pelo cliente. Trata-se de:
a) Stateful.

b) Stateless.

c) Singleton.

d) Message driven.

e) Entity.

Comentários:

Stateless Session Beans: são objetos de negócio que não mantém estado entre invocações de métodos. Após cada chamada de método, o contêiner pode escolher destruir, recriar ou manter o Bean. Eles podem ter variáveis de instância, no entanto elas serão compartilhadas por vários usuários (entretanto, não de forma concorrente).
Conforme vimos em aula, são os Stateless Session Beans que não mantêm estado
(conversacional)!

Gabarito: B

2. (CESPE - 2005 - SERPRO - Analista de Sistemas) O Entrerprise JavaBeans (EJB),
cuja especificação mais recente é a da versão 2.1, define, em sistemas Java, um conjunto de tecnologias utilizadas do lado cliente.
Comentários:

Enterprise JavaBeans (EJB) é uma arquitetura para aplicações corporativas orientada à transação e baseada em componentes. Além de uma arquitetura, eles são também componentes server-side que oferecem uma infraestrutura para o desenvolvimento e implantação de aplicações distribuídas, escaláveis, transacionais, seguras, concorrentes, persistentes, e portáteis de maneira fácil de acessar e simples de usar.
LOCAL CONTÊINER COMPONENTE

CLIENTE Aplicação Cliente Componentes de Aplicação

Applet Applet

SERVIDOR Web

Java Servlet

JavaServer Pages (JSP)
JavaServer Faces (JSF)

EJB Enterprise Beans

Conforme vimos em aula, trata-se de um conjunto de tecnologias server-side, i.e.,
utilizada do lado do servidor. Gabarito: E
3. (FCC - 2012 - TJ/PE - Analista de Sistemas - D) A especificação EJB 3, que é um subconjunto da especificação Java EE, define anotações apenas para o tipo bean.
Comentários:

Os descritores de implantação do J2EE 1.4 eram, em geral, complexos e era fácil cometer erros ao preenchê-los. Em vez disso, a Plataforma Java EE usa Anotações(Annotations), que são modificadores semelhantes a público e privado. O EJB 3, por exemplo, define anotações para o tipo de bean, tipo de interface, referências de recurso, atributos de transação,segurança e muito mais.
Conforme vimos em aula, não são apenas para o tipo Bean. Gabarito: E

4. (CESPE - 2009 - TRE/BA - Analista de Sistemas) As tecnologias JPA e EJB permitem, com o uso da linguagem Java, a manipulação de dados que estão em um banco de dados.
Comentários:

Existem três tipos de EJB, mas o Entity Bean é opcional a partir do EJB 3.2. Ele só existe na especificação por questão de compatibilidade com versões anteriores, mas sabe-se que ele já foi substituído pela Java Persistence API (JPA). Ademais, como é um EnterpriseJavaBean, eles encapsulam uma lógica de negócio. Pois bem, sobram dois tipos -Message-driven Beans e
Session Beans:

Conforme vimos em aula, ambos permitem a manipulação de dados que estão em um banco de dados. Atualmente, os Entity Beans são opcionais, mas continuam existindo! Gabarito: C
/ 51

/

5. (FCC - 2011 - TCE/PR - Analista de Sistemas) Sobre o Java EE 6 é correto afirmar:

a) Um message-driven bean encapsula a lógica de negócios e deve ser invocado por meio de programação por um cliente local ou remoto. Os message-driven beans são persistentes.
b) Um session bean encapsula a lógica de apresentação e deve ser invocado por meio de programação apenas por cliente remoto. Para acessar um aplicativo que é implantado no servidor, o cliente invoca métodos do session bean.
c) Os serviços CDI permitem aos componentes do Java EE, como beans de sessão EJB e beans gerenciados do JavaServer Faces (JSF), serem injetados e interagir de maneira acoplada e flexível iniciando e observando eventos.
d) Message-driven beans permitem que aplicações Java EE possam processar mensagens de forma síncrona. São persistentes e gerenciam a troca de mensagens com o banco de dados.
e) Os Singleton Session Beans são utilizados na troca de mensagem JMS de forma assíncrona entre aplicações.
Comentários:

Message-driven Beans (MDB): trata-se de um objeto não-persistente que combina características de um Session Bean e uma escuta/monitor (listener) de mensagens, permitindo a um componente de negócio receber e tratar mensagens de forma assíncrona - geralmente,providas pelo JMS.
Pode-se dizer que eles são executados após o recebimento de uma única mensagem do cliente.

Um Contêiner EJB provê um ambiente de execução escalável para executar um grande número de MDBs concorrentemente. Eles podem ser Stateless, apenas. Ademais, devem ser invocados por meio de programação por um cliente local ou remoto. Como não são persistentes, o cliente não acessa um MDB diretamente, mas por meio do JMSm enviando mensagens para o destinatário.
(a) Conforme vimos em aula, ele não é persistente.

(d) Conforme vimos em aula, é de forma assíncrona.

x'

/ 51

/

Um Session Bean encapsula a lógica de negócio que pode ser invocada programaticamente por um cliente localmente, remotamente ou por meio de webservices. Os SBs permitem enviar e receber mensagens JMS, porém somente de forma síncrona. Seus dados não são persistidos em uma base de dados e eles podem ser de três tipos: stateful, stateless e singleton!Vamos vê-los a seguir:
(b) Conforme vimos em aula, pode ser invocado de forma local, remota ou por WS.

(e) Conforme vimos em aula, a questão trata do MDBs.

Ela fornece uma arquitetura que permite que os componentes Java EE existam dentro do ciclo de vida de um aplicativo com escopos bem definidos. Além disso, os serviços CDI permitem que os componentes Java EE, tais como EJB Session Beans e JSF Managed Beans, sejam injetados e interajam de uma maneira fracamente acoplada e flexível, iniciando e observando eventos.
(c) Conforme vimos em aula, seria mais interessante se a questão tivesse dito "fracamente acoplada", assim não geraria ambiguidades. Gabarito: C
6. (CESPE - 2009 - TRE/PA - Analista de Sistemas) O EJB (Enterprise JavaBeans) é responsável por aspectos de apresentação e tratamento de eventos.
Comentários:

LOCAL CONTÊINER COMPONENTE

CLIENTE Aplicação Cliente Componentes de Aplicação

Applet Applet

SERVIDOR Web

Java Servlet

JavaServer Pages (JSP)
JavaServer Faces (JSF)

EJB Enterprise Beans

, 51

Conforme podemos ver na tabela, apresentação e tratamento de eventos são tipicamente responsabilidades de JSP e Servlets. Gabarito: E
7. (FCC - 2011 - TRT - 23a REGIÃO (MT) - Técnico Judiciário - Tecnologia da Informação) No JEE 6
é a especificação que tem como propósito unir os modelos de componentes do JSF Managed-
Beans com o EJB, proporcionando um modelo de fácil implementação para aplicações web:

a) Contexts and Dependency Injection (CDI).

b) Bean Validation.

c) Expression Language (EL).

d) Bibliotecas padrão para o JSP.

e) Enterprise JavaBeans (EJB).

Comentários:

Ela fornece uma arquitetura que permite que os componentes Java EE existam dentro do ciclo de vida de um aplicativo com escopos bem definidos. Além disso, os serviços CDI permitem que os componentes Java EE, tais como EJB Session Beans e JSF Managed Beans, sejam injetados e interajam de uma maneira acoplada flexível, iniciando e observando eventos.
Conforme vimos em aula, trata-se do CDI! Gabarito: A

8. (CESPE - 2009 - TRT/21 - Analista de Sistemas) Na implementação de projeto corporativo de comércio eletrônico construído na plataforma J2EE, a lógica do negócio poderá ser encapsulada em EJBs (Enterprise JavaBeans).
Comentários:

Podemos dizer também que se trata de uma tentativa de padronizar o encapsulamento da lógica de negócio sob uma única interface - EJB é o núcleo da Tecnologia JavaEE. Bem, esse componente é executado no Container EJB de um Servidor de Aplicação! Professor, o que tem de tão especial nessa tecnologia? Cara, ela simplifica o desenvolvimento de aplicações complexas e distribuídas.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

9. (ESAF - 2012 - CGU - Analista de Sistemas) Os serviços de gerenciamento,
oferecidos pelo contêiner EJB (Enterprise JavaBeans), são de:
a) Transações. Persistência. Ciclo de Vida. Segurança.

b) Transições. Pertinência. Ciclo de Vida. Risco

/ 51

/

c) Transformações. Persistência. Ciclo de Projeto. Segurança.

d) Transações. Comunicação. Ciclo de Vida. Mercado.

e) Transações. Consistência. Fases. Segurança.

Comentários:

O Contêiner EJB é um recipiente (em tempo de execução) para Enterprise
Beans que são implantados em um Servidor de Aplicação. Ele é criado automaticamente quando o servidor é inicializado e oferece serviços como: gerenciamento de ciclo de vida, geração de código,gerenciamento de persistência, gerenciamento de segurança, gerenciamento de transações,controle de concorrência, etc. Vejamos:

Conforme vimos em aula, trata-se das Transações, Persistência, Ciclo de Vida e Segurança.
Gabarito: A

10. (CESPE - 2009 - CEHAP/PB - Analista de Sistemas - A) A camada EJB hospeda, entre outros,
os beans de entidade, os beans de transporte, os objetos de acesso aos dados e os objetos de valor.
Comentários:

Existem três tipos de EJB, mas o Entity Bean é opcional a partir do EJB 3.2. Ele só existe na especificação por questão de compatibilidade com versões anteriores, mas sabe-se que ele já foi substituído pela Java Persistence API (JPA). Ademais, como é um EnterpriseJavaBean, eles encapsulam uma lógica de negócio. Pois bem, sobram dois tipos -Message-driven Beans e
Session Beans:

Conforme vimos em aula, temos três tipos de beans corporativos: Session Beans,
Message-driven
Beans e Entity Beans (atualmente opcional). Logo, a questão só acertou um deles! Gabarito: E

11.(FGV - 2013 - INEA/RJ - Analista de Sistemas - III) Um dos componentes da plataforma JEE é o
Enterprise JavaBeans (EJB), cujos os principais objetivos são fornecer um desenvolvimento rápido e simplificado de aplicações Java baseado em componentes distribuídos, transacionais,seguros e portáveis.

Comentários:

Podemos dizer também que se trata de uma tentativa de padronizar o encapsulamento da lógica de negócio sob uma única interface - EJB é o núcleo da Tecnologia JavaEE. Bem, esse componente é executado no Container EJB de um Servidor de Aplicação! Professor, o que tem
/ 51

/

de tão especial nessa tecnologia? Cara, ela permite o desenvolvimento rápido e simplificado de aplicações complexas.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

12. (CESPE - 2009 - CEHAP/PB - Analista de Sistemas - C) A camada EJB não hospeda os serviços em nível de sistema como o gerenciamento de transações, o controle de concorrência e a segurança.
Comentários:

Programadores precisam escrever apenas a lógica de negócio em Componentes EJB. Não precisa implementar nenhuma programação ou serviço em nível de sistema, tais como transações ou segurança, pois isso é oferecido pelo Container EJB.
Conforme afirma a nota de rodapé, o programador não precisa codificar o componente EJB
para oferecer tais serviços, porque o Contêiner EJB o faz! Gabarito: E
13.(CESGRANRIO - 2006 - PETROBRÁS - Analista de Sistemas - C) Um descritor de instalação,localizado dentro de um arquivo Java Archive (JAR), permite que as propriedades de um EJB
sejam mantidas fora do código Java e que o desenvolvedor do bean torne as informações sobre o bean disponíveis para o montador da aplicação e para o instalador do bean.
Comentários:

A estrutura de um Enterprise Bean e seu comportamento em tempo de execução são definidos em um ou mais Descritores de Implantação (Anotações XML). Programadores criam esses arquivos durante o processo de empacotamento de EJB e os descritores se tornam parte da implantação do EJB quando o Enterprise Bean é compilado. O Descritor de Implantação do EJB 3.2 é o ejb-jar.xml.

Conforme vimos em aula, o item está perfeito! Gabarito: C

14. (CESPE - 2009 - CEHAP/PB - Analista de Sistemas - D) Os beans corporativos e seus respectivos recipientes de acompanhamento são executados no cliente JEE.
Comentários:

LOCAL CONTÊINER COMPONENTE

CLIENTE Aplicação Cliente Componentes de Aplicação

Applet Applet

SERVIDOR Web

Java Servlet

JavaServer Pages (JSP)
JavaServer Faces (JSF)

EJB Enterprise Beans

Conforme vimos em aula, Beans Corporativos (Enterprise Beans) e seus
Recipientes (Container
EJB) são executados no Servidor e, não, no Cliente. Gabarito: E

15.(CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - I) EJB fornece ao programadorJava EE os seguintes tipos fundamentais: Entity Beans, Session Beans e Message Driven Beans.

Comentários:

Existem três tipos de EJB, mas o Entity Bean é opcional a partir do EJB 3.2. Ele só existe na especificação por questão de compatibilidade com versões anteriores, mas sabe-se que ele já foi substituído pela Java Persistence API (JPA). Ademais, como é um EnterpriseJavaBean, eles encapsulam uma lógica de negócio. Pois bem, sobram dois tipos -Message-driven Beans e
Session Beans:

Conforme vimos em aula, ainda existem três tipos fundamentais, mas - a partir do EJB
3.1 - os
Entity Beans foram substituídos pelo JPA (e, hoje, são mantidos como opcionais por questão de compatibilidade). Gabarito: C
16. (CESPE-2010-TCU - Analista de Sistemas) A tecnologia EJB (enterprise Java beans) apresenta,
na sua versão 3.1, melhorias que propiciam facilidades para o uso de beans singleton e que permitem o uso de beans de uma classe, sem necessidade de desenvolvimento de sua interface correspondente, e a invocação assíncrona de beans de sessão.
Comentários:

/

NOVIDADES DO EJB 3.1

Novo tipo de componente (Singleton Session Bean) que implementa o Padrão
Singleton e permite capturar eventos de inicialização e encerramento da aplicação

Interface opcional para componentes - Flexibilização na criação de componentes
EJBs sem a obrigatoriedade da criação de uma interface remota ou local.

Melhorias no serviço de agendamento que permitem novas possibilidades através de uma notação similar ao Unix Cron e agendamento de forma declarativa.
Deploy de EJBs na camada web (.war) - Permite o uso de EJBs diretamente na camada Web.
Chamadas assíncronas a métodos - Uma alternativa simplificada à MDBs para chamada assíncrona que pode ser utilizada em cenários menos complexos.
Nomes JNDI globais padronizados - Esse recurso facilita ainda mais a portabilidade.
EJB Lite - Define uma versão mais leve para um conteiner de EJBs.

Embeddable EJB - Possibilidade de executar EJBs no ambiente JavaSE.

Conforme vimos em aula, todos estão perfeitos! Gabarito: C

/ 51

/

17. (CESGRANRIO - 2013 - BNDES - Analista de Sistemas) Cada tipo de enterprise bean passa por diferentes fases durante seu ciclo de vida. Um desses tipos possui um estado denominadoPassivo. Quando um bean entra nesse estado, o container EJB o desloca da memória principal para a memória secundária. Qual tipo de bean se comporta dessa maneira?
a) Stateless Session Bean b) Stateful Session Bean c) Web Service Bean d) Singleton Session Bean e) Message-Driven Bean
Comentários:

Observem o ciclo de vida mostrado acima e percebam que ele tem três estados: no estágio DoesNot Exist, a instância simplesmente ainda não existe; no estágio Ready, a instância está vinculada a um determinado cliente e ocupada em uma conversação; no estágio Passive, a instância sai da memória principal para a memória secundária para economizar recursos.
Conforme vimos em aula, trata-se do Stateful Session Bean. Gabarito: B

18. (CESPE - 2010 - TRE/MT - Analista de Sistemas - B) Em uma aplicação J2EE típica, um EJB é criado, controlado e destruído pela aplicação cliente.
Comentários:

O Contêiner EJB é um recipiente (em tempo de execução) para Enterprise
Beans que são implantados em um Servidor de Aplicação. Ele é criado automaticamente quando o servidor é inicializado e oferece serviços como: gerenciamento de ciclo de vida, geração de código,gerenciamento de persistência, gerenciamento de segurança, gerenciamento de transações,controle de concorrência, etc. Vejamos:

LOCAL CONTÊINER COMPONENTE

CLIENTE Aplicação Cliente Componentes de Aplicação

Applet Applet

SERVIDOR Web

Java Servlet

JavaServer Pages (JSP)
JavaServer Faces (JSF)

EJB Enterprise Beans

Conforme vimos em aula, o gerenciamento do ciclo de vida (Criação, Controle e
Destruição de
EJB) é de responsabilidade do Contêiner EJB. Gabarito: E

19. (CESGRANRIO - 2009 - BNDES - Analista de Sistemas - C) Enterprise JavaBeans é um modelo de componentes padronizado, executado no lado do cliente e que facilita a construção de aplicações distribuídas robustas.
Comentários:

Enterprise JavaBeans (EJB) é uma arquitetura para aplicações corporativas orientada à transação e baseada em componentes. Além de uma arquitetura, eles são também componentes server-side que oferecem uma infraestrutura para o desenvolvimento e implantação de aplicações distribuídas, escaláveis, transacionais, seguras, concorrentes, persistentes, e portáteis de maneira fácil de acessar e simples de usar.
Podemos dizer também que se trata de uma tentativa de padronizar o encapsulamento da lógica de negócio sob uma única interface - EJB é o núcleo da Tecnologia JavaEE. Bem, esse componente é executado no Container EJB de um Servidor de Aplicação! Professor, o que tem de tão especial nessa tecnologia? Cara, ela permite o desenvolvimento rápido e simplificado de aplicações complexas.
Conforme vimos em aula, trata-se de um modelo de componentes padronizado, no entanto eles são server-side. Gabarito: E
20. (CESPE - 2010 - TRT/21 - Analista de Sistemas) Na implementação de projeto corporativo de comércio eletrônico construído na plataforma J2EE, a lógica do negócio poderá ser encapsulada em EJBs (Enterprise JavaBeans).
/

Comentários:

Podemos dizer também que se trata de uma tentativa de padronizar o encapsulamento da lógica de negócio sob uma única interface - EJB é o núcleo da Tecnologia JavaEE. Bem, esse componente é executado no Container EJB de um Servidor de Aplicação! Professor, o que tem de tão especial nessa tecnologia? Cara, ela simplifica o desenvolvimento de aplicações complexas e distribuídas.
Conforme vimos em aula, essa é a função dos EJBs. Gabarito: C

21.(Quadrix - 2011 - DATAPREV - Analista de Tecnologia da Informação - Desenvolvimento deSistemas) Analise os itens a seguir sobre JEE e EJB.

I. Um servidor J2EE fornece contêineres EJB e Web.

II. O contêiner EJB gerencia a execução de EJBs em aplicações J2EE.

III. O contêiner Web gerencia a execução de páginas JSP e componentes servlet em aplicações
J2EE.

IV. Um session bean representa um único cliente dentro do servidor J2EE. Para acessar um aplicativo que é instalado no servidor, o cliente invoca os métodos do session bean.
Está correto o que se afirma em:

a) l,ll, III e IV.

b) I e II, apenas.

c) I, III e IV, apenas.

d) I e IV, apenas.

e) III e IV, apenas.

Comentários:

LOCAL CONTÊINER COMPONENTE

CLIENTE Aplicação Cliente Componentes de Aplicação

Applet Applet

/ 51

/

SERVIDOR Web

Java Servlet

JavaServer Pages (JSP)
JavaServer Faces (JSF)

EJB Enterprise Beans

Session Beans (SB): trata-se de um objeto não-persistente que implementa alguma lógica de negócio ou fluxo de trabalho no servidor. Eles servem para executar alguma tarefa em nome de um único cliente e implementam a interface javax.ejb.SessionBean, podendo implementar WebServices. O Contêiner EJB provê um ambiente escalável para executar um grande número de SBs concorrentemente.
Conforme vimos em aula, um Servidor de Aplicação Java EE fornece um Contêiner EJB e umContêiner Web. De fato, um Session Bean representa um único cliente dentro do servidor. Todos os itens estão perfeitos! Gabarito: A
22. (CESPE - 2011 - MEC - Analista de Sistemas) A tecnologia EJB (Enterprise
JavaBeans),
arquitetura de componentes do lado do servidor, permite o desenvolvimento rápido e simplificado de aplicações transacionais, seguras e portáteis, baseadas na tecnologia Java. Seu objetivo é facilitar o trabalho do desenvolvedor para que ele não tenha de se preocupar com aspectos de infraestrutura.
Comentários:

Podemos dizer também que se trata de uma tentativa de padronizar o encapsulamento da lógica de negócio sob uma única interface - EJB é o núcleo da Tecnologia JavaEE. Bem, esse componente é executado no Container EJB de um Servidor de Aplicação! Professor, o que tem de tão especial nessa tecnologia? Cara, ela permite o desenvolvimento rápido e simplificado de aplicações complexas.
Em outras palavras, ele deixa o programador livre para se concentrar na lógica de negócio e na resolução do problema. Assim, o desenvolvedor não precisa mais se preocupar com codificação envolvendo infraestrutura (segurança, escalabilidade, entre outros).Ademais, eles são extremamente portáveis e reusáveis. Logo, pode-se construir aplicações a partir de beans pré-existentes.

Conforme vimos em aula, o item está perfeito! Gabarito: C

23.(FUNCAB - 2010 - PRODAM-AM - Analista de TI - Desenvolvimento de Sistemas) Sejam as seguintes assertivas sobre os tipos de EJB existentes:
/

I Process beans são excelentes opções para a implementação da lógica do negócio, dos processos de negócio e dos fluxos de trabalho.
II Entity beans representam os objetos persistentes em uma aplicação EJB.

III Asynchronous beans podem ser usados para o envio (recebimento) de mensagens assíncronas para (de) outros sistemas.
Marque a alternativa correta em relação às assertivas acima.

a) Apenas a assertiva I é verdadeira.

b) Apenas a assertiva II é verdadeira.

c) Apenas a assertiva III é verdadeira.

d) Todas as assertivas são verdadeiras.

e) Todas as assertivas são falsas.

Comentários:

Session Beans (SB): trata-se de um objeto não-persistente que implementa alguma lógica de negócio ou fluxo de trabalho no servidor. Eles servem para executar alguma tarefa em nome de um único cliente e implementam a interface javax.ejb.SessionBean, podendo implementar WebServices. O Contêiner EJB provê um ambiente escalável para executar um grande número de SBs concorrentemente.
(I) Conforme vimos em aula, trata-se - na verdade - dos Session Beans.

Existem três tipos de EJB, mas o Entity Bean é opcional a partir do EJB 3.2. Ele só existe na especificação por questão de compatibilidade com versões anteriores, mas sabe-se que ele já foi substituído pela Java Persistence API (JPA). Ademais, como é um EnterpriseJavaBean, eles encapsulam uma lógica de negócio. Pois bem, sobram dois tipos -Message-driven Beans e
Session Beans:

(II) Conforme vimos em aula, trata-se - de fato - dos Entity Beans.

Message-driven Beans (MDB): trata-se de um objeto não-persistente que combina características de um Session Bean e uma escuta/monitor (listener) de mensagens, permitindo a um componente de negócio receber e tratar mensagens de forma assíncrona - geralmente,providas pelo JMS.
Pode-se dizer que eles são executados após o recebimento de uma única mensagem do cliente.

/ 51

/

(II) Conforme vimos em aula, trata-se - na verdade - dos Message-driven Beans. Gabarito: B

24. (CESPE - 2008 - TRT/5 - Analista de Sistemas) Enterprise JavaBeans são componentes de negócios em Java que são executados do lado do cliente.
Comentários:

LOCAL CONTÊINER COMPONENTE

CLIENTE Aplicação Cliente Componentes de Aplicação

Applet Applet

SERVIDOR Web

Java Servlet

JavaServer Pages (JSP)
JavaServer Faces (JSF)

EJB Enterprise Beans

Conforme vimos em aula, Beans Corporativos (Enterprise Beans) e seus
Recipientes (Container
EJB) são executados no Servidor e, não, no Cliente. Gabarito: E

25.(COPEVE-UFAL - 2012 - ALGÁS - Analista de Tecnologia da Informação - III) EJB é parte integrante do Java Enterprise Edition e permite o desenvolvimento de componentes de software reutilizáveis e executáveis em servidores de aplicação, como, por exemplo, o JBoss.
Comentários:

Em outras palavras, ele deixa o programador livre para se concentrar na lógica de negócio e na resolução do problema. Assim, o desenvolvedor não precisa mais se preocupar com codificação envolvendo infraestrutura (segurança, escalabilidade, entre outros).Ademais, eles são extremamente portáveis e reusáveis. Logo, pode-se construir aplicações a partir de beans pré-existentes.

Conforme vimos em aula, eles fazem parte do Java EE; são extremamente reusáveis; e são executados em Servidores de Aplicação - como o JBoss. Gabarito: C
/ 51

/

26. (CESPE-2006-CENSIPAM-Analista de Sistemas) Um EJB tem as seguintes características: um stateless session bean não pode ter variáveis de instância, pois não mantém informações de estado após um método ser executado por um cliente; em um stateful session bean as variáveis da instância representam o estado de uma sessão e o estado é mantido entre as chamadas aos métodos; um entity bean representa um objeto persistente que pode ser compartilhado por clientes, a persistência pode ser gerenciada pelo container ou pelo bean.
Comentários:

Stateless Session Beans: são objetos de negócio que não mantém estado entre invocações de métodos. Após cada chamada de método, o contêiner pode escolher destruir, recriar ou manter o Bean. Eles podem ter variáveis de instância, no entanto elas serão compartilhadas por vários usuários (entretanto, não de forma concorrente).
Conforme vimos em aula, eles podem - sim - ter variáveis de instância. Gabarito: E

27. (COPEVE-UFAL - 2012 - ALGÁS - Analista de Tecnologia da Informação - IV) EJB é o nome dado para o conjunto de soluções Web em Java, constituído por Servlets e JSP.
Comentários:

LOCAL CONTÊINER COMPONENTE

CLIENTE Aplicação Cliente Componentes de Aplicação

Applet Applet

SERVIDOR Web

Java Servlet

JavaServer Pages (JSP)
JavaServer Faces (JSF)

EJB Enterprise Beans

Conforme vimos em aula, eles são compostos por Enterprise Beans e, não,
Servlets e JPS.

Gabarito: E

28. (CESPE - 2008 - SERPRO - Analista - Desenvolvimento de Sistemas) A tecnologia Enterprise
JavaBeans (EJB) é uma arquitetura de componentes do tipo cliente que atua na plataforma J2EE.

/

Comentários:

Enterprise JavaBeans (EJB) é uma arquitetura para aplicações corporativas orientada à transação e baseada em componentes. Além de uma arquitetura, eles são também componentes server-side que oferecem uma infraestrutura para o desenvolvimento e implantação de aplicações distribuídas, escaláveis, transacionais, seguras, concorrentes, persistentes, e portáteis de maneira fácil de acessar e simples de usar.
Conforme vimos em aula, eles são do tipo servidor! Gabarito: E

29.(FUNCAB - 2010 - PRODAM-AM - Analista de TI - Desenvolvimento de Sistemas) Qual interface deve ser usada para criar, procurar e remover objetos EJB?
a) javax.ejb.EJBLocalObject b) javax.ejb.EJBHome c) javax.ejb.EJBObject d) javax.ejb.EntityBean e) javax.ejb.EJBMetaData.
Comentários:

A Interface EJBObject implementa a interface para acessos remotos e locais, e funciona como um wrapper, i.e., encapsulando a instância EJB solicitada pelo cliente. Já a InterfaceEJBHome faz exatamente a mesma coisa, no entanto ela também é responsável por auxiliar o contêiner a gerenciar o ciclo de vida de um Bean - realizando criações, buscas e remoções de objetos.
Conforme vimos em aula, trata-se da interface javax.ejb.EJBHome. Gabarito: B

3O.(CESPE - 2012 - PEFOCE - Perito Criminal - Análise de Sistemas) Em uma arquitetura
JEE
distribuída, um contêiner representa um ambiente de execução padronizado que fornece serviços específicos a determinado componente. Um contêiner EJB, por exemplo, destina-se a prover a infraestrutura necessária para a execução de componentes que executem funcionalidades que realizam a lógica de negócio e dados específicos de determinada aplicação.
Comentários:

Enterprise JavaBeans (EJB) é uma arquitetura para aplicações corporativas orientada à transação e baseada em componentes. Além de uma arquitetura, eles são também componentes server-side que oferecem uma infraestrutura para o desenvolvimento e implantação de aplicações distribuídas, escaláveis, transacionais, seguras, concorrentes, persistentes, e portáteis de maneira fácil de acessar e simples de usar.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

31.(FUMARC - 2012 - TJ-MG - Técnico Judiciário - Analista de Sistemas - II) EJB é um framework de componentes, baseado na arquitetura MVC, para construção de interfaces com usuário.
Comentários:

Enterprise JavaBeans (EJB) é uma arquitetura para aplicações corporativas orientada à transação e baseada em componentes. Além de uma arquitetura, eles são também componentes server-side que oferecem uma infraestrutura para o desenvolvimento e implantação de aplicações distribuídas, escaláveis, transacionais, seguras, concorrentes, persistentes, e portáteis de maneira fácil de acessar e simples de usar.
Conforme vimos em aula, essa definição está incorreta! Na verdade, essa é a definição de JSF!
Gabarito: E

32. (Instituto AOCP - 2013 - Colégio Pedro II - Técnico de Tecnologia da Informação) Muitos sistemas corporativos são construídos seguindo a arquitetura definida pelo padrão Enterprise JavaBeans(EJB). Ao utilizar essa arquitetura, as aplicações ganham certos benefícios. Qual das alternativas abaixo indica alguns desses benefícios?
a) Concorrência, multithreading, faces server, conversões, gerenciamento de telas.

b) Conversões, transações, Persistência, segurança e gerenciamento de telas.

c) Gerenciamento de telas, Persistência, conversões.

d) Transações, Persistência, Segurança, Remotabilidade.

e) Remotabilidade, gerenciamento de telas, faces server.

Comentários:

O Contêiner EJB é um recipiente (em tempo de execução) para Enterprise
Beans que são implantados em um Servidor de Aplicação. Ele é criado automaticamente quando o servidor é inicializado e oferece serviços como: gerenciamento de ciclo de vida, geração de código,
/ 51

/

gerenciamento de persistência, gerenciamento de segurança, gerenciamento de transações,controle de concorrência, etc. Vejamos:

Conforme vimos em aula, estão todos corretos - inclusive a remotabilidade, que é intrínseco ao componente. Gabarito: D
/

LISTA DE QUESTõES - EJB - MULTIBANCAS

1. (FCC - 2011 - TRT/19 - Analista de Sistemas) Tipo de session bean EJB 3.1 cujas instâncias não têm estado conversacional, isto é, todas as instâncias são equivalentes quando não estão envolvidas em atender um método invocado pelo cliente. Trata-se de:
a) Stateful.

b) Stateless.

c) Singleton.

d) Message driven.

e) Entity.

2. (CESPE - 2005 - SERPRO - Analista de Sistemas) O Entrerprise JavaBeans (EJB),
cuja especificação mais recente é a da versão 2.1, define, em sistemas Java, um conjunto de tecnologias utilizadas do lado cliente.
3. (FCC - 2012 - TJ/PE - Analista de Sistemas - D) A especificação EJB 3, que é um subconjunto da especificação Java EE, define anotações apenas para o tipo bean.
4. (CESPE - 2009 - TRE/BA - Analista de Sistemas) As tecnologias JPA e EJB permitem, com o uso da linguagem Java, a manipulação de dados que estão em um banco de dados.
5. (FCC - 2011 - TCE/PR - Analista de Sistemas) Sobre o Java EE 6 é correto afirmar:

a) Um message-driven bean encapsula a lógica de negócios e deve ser invocado por meio de programação por um cliente local ou remoto. Os message-driven beans são persistentes.
b) Um session bean encapsula a lógica de apresentação e deve ser invocado por meio de programação apenas por cliente remoto. Para acessar um aplicativo que é implantado no servidor, o cliente invoca métodos do session bean.
c) Os serviços CDI permitem aos componentes do Java EE, como beans de sessão EJB e beans gerenciados do JavaServer Faces (JSF), serem injetados e interagir de maneira acoplada e flexível iniciando e observando eventos.
d) Message-driven beans permitem que aplicações Java EE possam processar mensagens de forma síncrona. São persistentes e gerenciam a troca de mensagens com o banco de dados.
e) Os Singleton Session Beans são utilizados na troca de mensagem JMS de forma assíncrona entre aplicações.
/ 51

/

6. (CESPE - 2009 - TRE/PA - Analista de Sistemas) O EJB (Enterprise JavaBeans) é responsável por aspectos de apresentação e tratamento de eventos.
7. (FCC - 2011 - TRT - 23a REGIÃO (MT) - Técnico Judiciário - Tecnologia da Informação) No JEE 6
é a especificação que tem como propósito unir os modelos de componentes do JSF Managed-
Beans com o EJB, proporcionando um modelo de fácil implementação para aplicações web:

a) Contexts and Dependency Injection (CDI).

b) Bean Validation.

c) Expression Language (EL).

d) Bibliotecas padrão para o JSP.

e) Enterprise JavaBeans (EJB).

8. (CESPE - 2009 - TRT/21 - Analista de Sistemas) Na implementação de projeto corporativo de comércio eletrônico construído na plataforma J2EE, a lógica do negócio poderá ser encapsulada em EJBs (Enterprise JavaBeans).
9. (ESAF - 2012 - CGU - Analista de Sistemas) Os serviços de gerenciamento,
oferecidos pelo contêiner EJB (Enterprise JavaBeans), são de:
a) Transações. Persistência. Ciclo de Vida. Segurança.

b) Transições. Pertinência. Ciclo de Vida. Risco c) Transformações. Persistência. Ciclo de Projeto. Segurança.
d) Transações. Comunicação. Ciclo de Vida. Mercado.

e) Transações. Consistência. Fases. Segurança.

10. (CESPE - 2009 - CEHAP/PB - Analista de Sistemas - A) A camada EJB hospeda, entre outros,
os beans de entidade, os beans de transporte, os objetos de acesso aos dados e os objetos de valor.
11. (FGV - 2013 - INEA/RJ - Analista de Sistemas - III) Um dos componentes da plataforma JEE é o
Enterprise JavaBeans (EJB), cujos os principais objetivos são fornecer um desenvolvimento rápido e simplificado de aplicações Java baseado em componentes distribuídos, transacionais,seguros e portáveis.

x'

/ 51

/

12. (CESPE - 2009 - CEHAP/PB - Analista de Sistemas - C) A camada EJB não hospeda os serviços em nível de sistema como o gerenciamento de transações, o controle de concorrência e a segurança.
13.(CESGRANRIO - 2006 - PETROBRÁS - Analista de Sistemas - C) Um descritor de instalação,localizado dentro de um arquivo Java Archive (JAR), permite que as propriedades de um EJB
sejam mantidas fora do código Java e que o desenvolvedor do bean torne as informações sobre o bean disponíveis para o montador da aplicação e para o instalador do bean.
14. (CESPE - 2009 - CEHAP/PB - Analista de Sistemas - D) Os beans corporativos e seus respectivos recipientes de acompanhamento são executados no cliente JEE.
15.(CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - I) EJB fornece ao programadorJava EE os seguintes tipos fundamentais: Entity Beans, Session Beans e Message Driven Beans.

16. (CESPE-2010-TCU - Analista de Sistemas) A tecnologia EJB (enterprise Java beans) apresenta,
na sua versão 3.1, melhorias que propiciam facilidades para o uso de beans singleton e que permitem o uso de beans de uma classe, sem necessidade de desenvolvimento de sua interface correspondente, e a invocação assíncrona de beans de sessão.
17. (CESGRANRIO - 2013 - BNDES - Analista de Sistemas) Cada tipo de enterprise bean passa por diferentes fases durante seu ciclo de vida. Um desses tipos possui um estado denominadoPassivo. Quando um bean entra nesse estado, o container EJB o desloca da memória principal para a memória secundária. Qual tipo de bean se comporta dessa maneira?
a) Stateless Session Bean b) Stateful Session Bean c) Web Service Bean d) Singleton Session Bean e) Message-Driven Bean
18. (CESPE - 2010 - TRE/MT - Analista de Sistemas - B) Em uma aplicação J2EE típica, um EJB é criado, controlado e destruído pela aplicação cliente.
/

19. (CESGRANRIO - 2009 - BNDES - Analista de Sistemas - C) Enterprise JavaBeans é um modelo de componentes padronizado, executado no lado do cliente e que facilita a construção de aplicações distribuídas robustas.
20. (CESPE - 2010 - TRT/21 - Analista de Sistemas) Na implementação de projeto corporativo de comércio eletrônico construído na plataforma J2EE, a lógica do negócio poderá ser encapsulada em EJBs (Enterprise JavaBeans).
21.(Quadrix - 2011 - DATAPREV - Analista de Tecnologia da Informação - Desenvolvimento deSistemas) Analise os itens a seguir sobre JEE e EJB.

I. Um servidor J2EE fornece contêineres EJB e Web.

II. O contêiner EJB gerencia a execução de EJBs em aplicações J2EE.

III. O contêiner Web gerencia a execução de páginas JSP e componentes servlet em aplicações
J2EE.

IV. Um session bean representa um único cliente dentro do servidor J2EE. Para acessar um aplicativo que é instalado no servidor, o cliente invoca os métodos do session bean.
Está correto o que se afirma em:

a) l,ll, III e IV.

b) I e II, apenas.

c) I, III e IV, apenas.

d) I e IV, apenas.

e) III e IV, apenas.

22. (CESPE - 2011 - MEC - Analista de Sistemas) A tecnologia EJB (Enterprise
JavaBeans),
arquitetura de componentes do lado do servidor, permite o desenvolvimento rápido e simplificado de aplicações transacionais, seguras e portáteis, baseadas na tecnologia Java. Seu objetivo é facilitar o trabalho do desenvolvedor para que ele não tenha de se preocupar com aspectos de infraestrutura.
23.(FUNCAB - 2010 - PRODAM-AM - Analista de TI - Desenvolvimento de Sistemas) Sejam as seguintes assertivas sobre os tipos de EJB existentes:
I Process beans são excelentes opções para a implementação da lógica do negócio, dos processos de negócio e dos fluxos de trabalho.
, <

/

II Entity beans representam os objetos persistentes em uma aplicação EJB.

III Asynchronous beans podem ser usados para o envio (recebimento) de mensagens assíncronas para (de) outros sistemas.
Marque a alternativa correta em relação às assertivas acima.

a) Apenas a assertiva I é verdadeira.

b) Apenas a assertiva II é verdadeira.

c) Apenas a assertiva III é verdadeira.

d) Todas as assertivas são verdadeiras.

e) Todas as assertivas são falsas.

24. (CESPE - 2008 - TRT/5 - Analista de Sistemas) Enterprise JavaBeans são componentes de negócios em Java que são executados do lado do cliente.
25.(COPEVE-UFAL - 2012 - ALGÁS - Analista de Tecnologia da Informação - III) EJB é parte integrante do Java Enterprise Edition e permite o desenvolvimento de componentes de software reutilizáveis e executáveis em servidores de aplicação, como, por exemplo, o JBoss.
26. (CESPE - 2006-CENSIPAM - Analista de Sistemas) Um EJB tem as seguintes características: um stateless session bean não pode ter variáveis de instância, pois não mantém informações de estado após um método ser executado por um cliente; em um stateful session bean as variáveis da instância representam o estado de uma sessão e o estado é mantido entre as chamadas aos métodos; um entity bean representa um objeto persistente que pode ser compartilhado por clientes, a persistência pode ser gerenciada pelo container ou pelo bean.
27. (COPEVE-UFAL - 2012 - ALGÁS - Analista de Tecnologia da Informação - IV) EJB é o nome dado para o conjunto de soluções Web em Java, constituído por Servlets e JSP.
28. (CESPE - 2008 - SERPRO - Analista - Desenvolvimento de Sistemas) A tecnologia Enterprise
JavaBeans (EJB) é uma arquitetura de componentes do tipo cliente que atua na plataforma J2EE.

29.(FUNCAB - 2010 - PRODAM-AM - Analista de TI - Desenvolvimento de Sistemas) Qual interface deve ser usada para criar, procurar e remover objetos EJB?
a) javax.ejb.EJBLocalObject b) javax.ejb.EJBHome c) javax.ejb.EJBObject d) javax.ejb.EntityBean e) javax.ejb.EJBMetaData.
30. (CESPE - 2012 - PEFOCE - Perito Criminal - Análise de Sistemas) Em uma arquitetura JEEdistribuída, um contêiner representa um ambiente de execução padronizado que fornece serviços específicos a determinado componente. Um contêiner EJB, por exemplo, destina-se a prover a infraestrutura necessária para a execução de componentes que executem funcionalidades que realizam a lógica de negócio e dados específicos de determinada aplicação.
31.(FUMARC - 2012 - TJ-MG - Técnico Judiciário - Analista de Sistemas - II) EJB é um framework de componentes, baseado na arquitetura MVC, para construção de interfaces com usuário.
32. (Instituto AOCP - 2013 - Colégio Pedro II - Técnico de Tecnologia da Informação) Muitos sistemas corporativos são construídos seguindo a arquitetura definida pelo padrão Enterprise JavaBeans(EJB). Ao utilizar essa arquitetura, as aplicações ganham certos benefícios. Qual das alternativas abaixo indica alguns desses benefícios?
a) Concorrência, multithreading, faces server, conversões, gerenciamento de telas.

b) Conversões, transações, Persistência, segurança e gerenciamento de telas.

c) Gerenciamento de telas, Persistência, conversões.

d) Transações, Persistência, Segurança, Remotabilidade.

e) Remotabilidade, gerenciamento de telas, faces server.

/

GABARITo

GABARITO

1. B 12. E
23. B

2. E 13. C
24. E

3. E 14. E
25. C

4. C 15. C
26. E

5. C 16. C
27. E

6. E 17. B
28. E

7. A 18. E
29. B

8. C 19. E
30. C

9. A 20. C
31. E

10. E 21. A
32. B

11. C 22. C

, <

/

INVERSÃo DE CoNTRoLE E INJEçÃo DE DEPENDÊNCIA

Vamos a algumas explicações mais detalhadas sobre esses dois conceitos - comecemos com aInversão de Controle! Imaginem que vocês implementam uma classe de usuário, e dentro dessa classe vocês precisam utilizar a classe de e-mail. O que vocês fazem? Instanciam a classe de e-mail dentro da classe de usuário. O que isso gera? Acoplamento (i.e., dependência entre as partes).
Agora a classe de usuário depende da classe de e-mail. Um dos problemas que a inversão de controle veio resolver é o de módulos de mais alto nível (Ex: Classe de Usuário)dependendo de módulos de mais baixo nível (Ex: Classe de E-mail). O que é mais importante: usuário ou e-mail?Ora, usuário - o e-mail, em geral, é apenas um acessório do usuário! Vamos ver um exemplo mais claro:
Deem uma olhada na casa de vocês e contem quantos dispositivos têm baterias que precisam ser recarregadas de alguma maneira: câmera fotográfica, celular, fone de ouvido sem-fio,controle de videogame, ipod, máquina de barbear, etc. Ora, esses dispositivos não têm uma interface de recarga de bateria comum, i.e., um usa micro-usb, o outro mini-usb, outro usb, a apple sempre inventa algo diferente, enfim...
Qual o resultado disso? Você não possui um único carregador para recarregar todos os seus dispositivos - você é obrigado a ter um carregador para cada um deles! E se você mudar de celular? Lá se vai mais um carregador. Se você der um upgrade no ipod? Outro carregador! O que acontece no final? Aposto que vocês (como bons nerds) possuem uma gaveta lotada de carregadores diferentes! ®
Eu sei que vocês entenderam a história, mas eu gostaria que vocês internalizassem a ideia principal! Em vez de os carregadores dependerem dos dispositivos, os dispositivos estão dependendo dos carregadores. Isso não soa absurdo? É o mais importante dependendo do menos importante; é o essencial dependendo do acessório; é o "poste mijando no cachorro".
Bem, a Inversão de Controle (ou Inversão de Dependência) é uma forma de subverter essa lógica!Vamos fazer classes de baixo nível dependerem de classes de alto nível. Vamos programar para interfaces e, não, para implementações. Como podemos fazer isso, professor? Por meio daInjeção de Dependências (não confundam, são conceitos independentes!).
, 51

VlhaViS

ÍS W

Professor, o que seria a injeção de dependências? Trata-se de um padrão de desenvolvimento de software utilizado para inverter controles e manter o baixo acoplamento entre os módulos de um sistema. Ela visa remover dependências desnecessárias entre as classes ou torná-las mais suaves,e ajuda a ter um design de software que seja mais fácil de manter e de evoluir.

Lembram-se do exemplo anterior? Para eu utilizar uma classe de e-mail na classe de usuário, eu teria que instanciar a classe de e-mail dentro da classe de usuário. Ora, isso já acoplaria as classes,fazendo com que a classe de usuário dependesse da classe de e-mail, ou seja, a classe de alto nível estaria dependendo da classe de baixo nível. Vamos resolver esse problema com aInjeção de
Dependência!

Grosso modo, injetar dependências nada mais é que passar uma classe (que será utilizada) para outra classe (que irá consumi-la). Ora, realmente a classe de usuário precisa da classe de e-mail,mas é possível utilizá-la sem acoplá-las. Como? Delegando a responsabilidade de criação do objeto da classe e-mail a outra parte do sistema. Quem pode fazer isso? O Container!
Ele é responsável por criar, gerenciar, conectar e configurar objetos e seus ciclos de vida. O padrão de Injeção de Dependência é baseado no padrão Builder, que é aquele cara responsável por construir objetos e armazená-los. Ele permite a separação da construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes representações.
O que acontece? Passa-se a responsabilidade de criar um objeto para o container (que funciona como o builder), indicando qual interface desejamos que seja implementada. Ele criará a o objeto x'
/ 51

/

que implementa a interface e injeta essa dependência em outra classe. Em nosso caso,
ele criará o objeto de e-mail e injetará no objeto de pessoa.
O container é capaz de resolver dependências complexas transparentemente, i.e., eu não estou nem ligando para como ele vai resolver. O container é simplesmente um mapeador de dependências que as suas classes necessitam com a lógica de criação dessas dependências(por meio de XML/Annotation). Ele trata todos os objetos sob seu gerenciamento como beans.
Podemos afirmar, então, que a injeção de dependência desacopla a construção das suas classes da construção de suas dependências. Professor, deu nó na cabaça! A frase apenas afirma que a responsabilidade para a criação da classe E-mail não é mais da classe Usuário, é do container.Bacana? Dessa forma, quebramos o acoplamento e invertemos o controle.

Em vez de depender de uma classe concreta, passamos a depender de uma abstração. O
código estará mais desacoplado, modular, flexível - sendo mais fácil a manutenção e a evolução. É possível injetar dependências de três formas: Injeção por Construtor; Injeção porPropriedade (Setter); e
Injeção por Interface - esse último é injeção de dependência sem inversão de controle.

Por fim, vamos falar um pouquinho do Context and Dependency Injection (CDI). Galera,
Em seu lançamento, uma das maiores críticas para a adoção do EJB era a complexidade exigida para o programador na hora de usar suas APIs, o que levou ao desenvolvimento e popularização de frameworks mais práticos, como Spring e Hybernate. Beleza?
A partir do EJB3, buscou-se o uso intenso de annotations para simplificar a sintaxe e o uso dessasAPIs (Ex: JSF). Annotations permitem que certas operações, como injeções de dependência,
sejam mais simples. No CDI, define-se um conjunto de serviços que permite que componentesJEE como servlets, EJB e POJO possam ser manipulados dentro do ciclo de vida da aplicação com escopos bem definidos.
CDI também permite que componentes JEE, EJB e JSF ManagedBeans serem injetados com baixo acoplamento: unificando e simplificando o modelo de programação entre estas duas tecnologias.Dentro dos muitos serviços, ele traz suporte a transação dentro do web container,
facilitando a utilização de recursos relacionados as fontes de dados e mecanismos de persistência.
Por exemplo, com CDI fica muito fácil construir uma aplicação web que acesse um banco de dados usando como persistência alguma especificação do JPA.
, 51

