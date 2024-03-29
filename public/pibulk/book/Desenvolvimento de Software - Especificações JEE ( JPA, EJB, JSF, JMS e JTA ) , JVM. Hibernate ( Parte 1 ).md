# Desenvolvimento de Software - Especificações JEE ( JPA, EJB, JSF, JMS e JTA ) , JVM. Hibernate ( Parte 1 )

Índice

1) Java EE - Conceitos Básicos - Teoria

2) Java EE - Common Annotations - Teoria

3) Java EE - Conceitos Básicos - Questões Comentadas.

4) Java EE - Conceitos Básicos - Lista de Questões.

5) Java EE - JSP - Teoria

6) Java EE - JSP - Questões Comentadas - CEBRASPE

7) Java EE - JSP - Questões Comentadas - Multibancas.

8) Java EE - JSP - Lista de Questões - Cebraspe

9) Java EE - JSP - Lista de Questões - Multibancas.

10) Java EE - Servlets - Teoria

11) Java EE - Servlets - Questões Comentadas - CEBRASPE

12) Java EE - Servlets - Questões Comentadas - MULTIBANCAS

13) Java EE - Servlets - Lista de Questões - CEBRASPE

14) Java EE - Servlets - Lista de Questões - CEBRASPE

15) Java EE - JSF - Teoria

16) Java EE - JSF - Questões Comentadas.

17) Java EE - JSF - Lista de Questões.

18) Java EE - JPA - Teoria

19) Java EE - JPA - Questões Comentadas.

20) Java EE - JPA - Lista de Questões.

21) Java EE - Hibernate - Teoria

22) Java EE - Hibernate - Questões Comentadas.

23) Java EE - Hibernate - Lista de Questões.

24) Java EE - JDBC - Teoria

25) Java EE - JDBC - Questões Comentadas.

26) Java EE - JDBC - Lista de Questões.

*

JAVA EE

Bem, galera... nosso foco aqui é Java EEl! Empresas de tecnologia da informação sofrem atualmente com a altíssima competitividade. Não é raro ver uma gigante, que todo mundo achava que seria eterna, desmoronando-se por conta de uma nova tecnologia que surgiu ou paradigma que apareceu! Ou alguém aí ainda usa IRC, ICQ, MSN para se comunicar?
É verdade, professor! As empresas de Tecnologia da Informação têm vida curta! Não são só elas!Hoje em dia, empresas de quaisquer áreas precisam de aplicações para satisfazer as suas necessidades de negócio, que estão se tornando cada vez mais complexas. E tudo isso se torna mais complicado com a globalização - as empresas estão cada vez mais espalhadas por cidades,países e continentes.

E, ainda assim, realizam seus negócios 24/7 por meio da internet, com um bocado de data centers e sistemas internacionalizados para lidar com diferentes línguas, moedas,fusos-horários, etc. E
elas param de trabalhar em algum momento? Não! Estão sempre tentando diminuir seus custos,tempo de resposta de seus serviços, armazenar mais dados de maneira confiável e segura, entre outros.
E tudo isso de forma transparente para o cliente, que simplesmente acessa uma interface gráfica amigável achando que isso tudo é muito simples (mal sabem o que ocorre por trás).Pessoal, tudo tem que funcionar para o usuário não reclamar ou trocar de prestadora de serviço -e, claro, sem perder dinheiro, i.e., tem que haver prevenção de falhas, alta disponibilidade,redundância,
escalabilidade e segurança.

Além disso, as corporações têm de enfrentar constantes mudanças de requisitos,
tecnologias,
políticas, leis, etc. Em 2014, grande parte do que citamos é oferecido pelo Java
Enterprise Edition
(Java EE). Mas, então, o que é de fato o Java EE? É um conjunto de especificações destinadas ao desenvolvimento de aplicações distribuídas, robustas, potentes, escaláveis, multicamadas e de alta disponibilidade.
Rapaziada, vamos ver agora algumas novidades trazidas pela Plataforma Java EE 6:
conceito de profiles ou perfis; Java API for RESTful Web Services (JAX-RS); Managed Beans; Contexts andDependency Injection (CDI); Dependency Injection for Java; Bean Validation;
entre outras tecnologias concernentes a Enterprise JavaBeans, JavaServer Faces e Servlets.
Como ele oferece tudo isso, nós veremos por meio do estudo de um assunto muito importante:Arquitetura Java EE - apresentada na imagem abaixo:

1 Esse nome já mudou repetidas vezes! Inicialmente, chamava-se J2EE; depois foi modificado para
JEE; e atualmente é conhecido como Java EE.
Database

O Client System é a Camada do Cliente; Web Container é a Camada Web; o EJB
Container é a
Camada de Negócio; e o Database é a Camada de Dados2. No entanto, há quem condense a
Camada Web e a Camada de Negócio em uma camada chamada Servidor Java EE, representada pelo retângulo maior à direita - veremos com detalhes mais à frente!
Vamos falar um pouco agora sobre o Modelo de Aplicações Java EE! Galera, Java EE é projetado para suportar aplicações que implementam serviços corporativos para clientes, empregados,fornecedores, parceiros e outros que demandem ou contribuem com a organização! Essas

2 É também conhecida como Camada EIS (Enterprise Information System), que disponibiliza informações relevantes ao negócio e,diferente do que apresenta a imagem, não trata apenas do banco de dados, mas também de sistemas legados, processamento de transações de mainframe, sistemas externos, entre outros.
aplicações são inerentemente complexas, acessando dados de diversas fontes e distribuindo as aplicações entre os clientes.
O Modelo de Aplicações Java EE define uma arquitetura para implementação de serviços como aplicações multicamadas que fornecem escalabilidade, acessibilidade e gerenciabilidade necessários para aplicações corporativas. Dessa forma, a lógica de apresentação e a lógica de negócio são implementadas pelo desenvolvedor e os outros serviços são fornecidos pela plataforma Java EE!
Conforme mostra a imagem acima, existem duas aplicações multicamadas Java EE divididas em níveis descritos como se segue:
Camada do Cliente: componentes rodam na Máquina Cliente;

Camada Web: componentes rodam no Servidor Java EE;

Camada de Negócio: componentes rodam no Servidor Java EE;

Camada EIS: software roda no Servidor EIS.

Galera, a imagem abaixo apresenta um pouco da evolução do Java EE e a tabela que segue apresenta as APIs do Java EE:
Jbjava

----------- COMPATIBLE

ENTERPRISE
EDITION

Enterprise
Java
Platform

J2EE 1.2

Servlet, JSP:

Robustness

J2EE 1.3

CMP,

Connector
Architecture

Web
Services

J2EE 1.4

Web Services,
Management.
Deployment,
Async.

Connector

Ease of
Development

Java EE 5

Ease of
Development
Annotations
EJB 3.0

Persistence API
New and
Updated

Web Services

Flexible

Java EE 6

Pruning
Extensibility
Profiles
Ease-of-dev
EJB Lite
RESTful WS
CDI

Web Profile
&

Managed

Stable

Java EE 7

Ease of use

Complete
Java EE 6

JPE

Project

EJB, JMS
RMI/IIOP

Beans 1.0

May 1998

Dec1999

10 specs

Sep2001

13 specs

Nov 2003 May 2006

20 specs 23 specs

Dec2009

28 specs

April 2013

28+ specs

JAVA EE 6 (10/12/2009) JAVA EE 7 (12/06/2013)

*

-

Java API for WebSocket
Java API for JSON Processing

Java Servlet 3.0 Java Servlet 3.1

JavaServer Faces (JSF) 2.0 JavaServer Faces (JSF) 2.2
Expression Language (EL) 2.2 Expression Language (EL) 3.0
JavaServer Pages (JSP) 2.2 JavaServer Pages (JSP) 2.3

JavaServer Pages Standard Tag Library
(JSTL) 1.2

JavaServer Pages Standard Tag Library
(JSTL) 1.2

- Batch Applications for the
Java Platform

- Concurrency Utilities for
Java EE 1.0

Contexts and Dependency Injection for
Java 1.0

Contexts and Dependency Injection for
Java 1.1

Dependency Injection for Java 1.0 Dependency Injection for Java 1.0
Bean Validation 1.0 Bean Validation 1.1

Enterprise JavaBeans (EJB) 3.1 Enterprise JavaBeans (EJB) 3.2
Interceptors 1.1 Interceptors 1.2

Java EE Connector Architecture 1.6 Java EE Connector Architecture 1.7
Java Persistence API (JPA) 2.0 Java Persistence API (JPA) 2.1

Common Annotations for the Java
Platform 1.1

Common Annotations for the Java
Platform 1.2

Java Message Service API (JMS) 1.1 Java Message Service API (JMS) 2.0
Java Transaction API (JTA) 1.1 Java Transaction API (JTA) 1.2
JavaMail API 1.4 JavaMail API 1.5

Java API for RESTful Web Services
(JAX-RS) 1.1

Java API for RESTful Web Services (JAX-
RS) 2.0

- Implementing Enterprise Web
Services

1.3

Java API for XML-Based Web Services
(JAX-WS) 2.2

Web Services Metadata for the Java
Platform 2.1

Java API for XML-based RPC (JAX-
RPC) 1.1

Java APIs for XML Messaging (JAXM)
1.3

Java API for XML-Based Web Services
(JAX-WS) 2.2

Web Services Metadata for the Java
Platform

Java API for XML-based RPC (JAX-RPC)
(Opcional) 1.1

Java APIs for XML Messaging 1.3

Java API for XML Registries (JAXR) 1.0 Java API for XML Registries (JAXR) 1.0

Java Authentication Service Provider
Interface for Containers (JASPIC) 1.0
Java Authorization Service Provider
Contract for Containers (JACC) 1.4

Java Authentication Service Provider
Interface for Containers (JASPIC) 1.1
Java Authorization Service Provider
Contract for Containers (JACC) 1.5

Java EE Application Deployment 1.2 Java EE Application Deployment

(Opcional) 1.2

J2EE Management 1.1 J2EE Management 1.1

- Debugging Support for Other
Languages

1.0

Java Architecture for XML Binding
(JAXB) 2.2

Java Architecture for XML Binding (JAXB)
2.2

- Java API for XML Processing
(JAXP) 1.3

- Java Database Connectivity
4.0

- Java Management Extensions
(JMX) 2.0

- JavaBeans Activation
Framework (JAF)

1.1

- Streaming API for XML
(StAX) 1.0

Managed Beans 1.0 -

Web Services 1.3 -

Debuggin Support for Other -
Languages 1.0

A versão Java EE 6 traz o conceito de profile (ou perfil)! O que é isso, professor?
Um perfil busca definir um subconjunto das tecnologias dentre aquelas da plataforma Java EE. Como assim? Bem,pensem comigo: cada aplicação tem sua particularidade, portanto não é necessário implementar obrigatoriamente todas as tecnologias da plataforma, i.e., eu posso criar perfis - cada um com sua configuração!
Imaginem que vamos fazer um sisteminha pequeno! Eu preciso implementar tudo que está na plataforma? Não, posso criar um perfil que implementa somente um subconjunto de funcionalidades! Existem dois perfis importantes: Web Profile e Full Profile! O primeiro perfil é um subconjunto do segundo e ajuda desenvolvedores a criarem aplicações mais leves que podem rodar em um Servlet Container.
Plataforma Java EE
WEB FULL

Java Servlet

Java Server Faces (JSF)
Java Server Pages (JSP)
Expression Language (EL)

Standard Tag Library for JavaServer Pages (JSTL)
Debugging Support for Other Languages

,

Contexts and Dependency Injection for the Java EE Platform
Dependency Injection for Java

Enterprise JavaBeans (EJB)
Java Persistence API

Common Annotations for the Java Platform
Java Transaction API

Bean Validation

Java EE Connector Architecture

Java API for RESTful Web Services (JAX-RS)

Observem que a tabela abaixo apresenta o EJB 3.1 como parte do Web Profile. Na verdade, noWeb Profile, trata-se do EJB 3.1 Lite, que é mais leve. Como assim, professor? Assim como os perfis, ele possui um subconjunto dos features do EJB 3.1 FuII. Por que? Porque é uma API utilizada especificamente para aplicações web. Vejam a diferença de acordo com a tabela abaixo.
Percebam que o EJB 3.1 Lite deixa de fora funcionalidades que são pouco utilizadas em aplicações web. De forma similar o Web Profile não oferece suporte a JAX-WS, JAX-RPC, JAXR,SAAJ, JAX-
RS, JAXB, JMS, JAAS, JASPIC, JACC, JCA, JavaMail, Management Specification e Deployment
Specification - além disso, ele não oferece suporte a Arquivos EAR (apenas Arquivos WAR).

/ 235

/

Feature EJB Lite EJI

Stateless beans ✓ ✓

Stateful beans ✓ ✓

Síngleton beans ✓ ✓

Message driven beans ✓

Remoting ✓

Web service (SOAP/REST) ✓

Asynchronous invoca tion ✓

Interceptors ✓ ✓

Dedarative security ✓ ✓

Dedarative transa ctions ✓ ✓

Programai atic transactions ✓

Tinner service ✓

EJB 2 support ✓

COR BA interoperability ✓

Table 2: EJB
and EJB Lite
Feature Com-
parison

Para finalizar, vamos entender algumas coisinhas! O processo de implantar (para alguns,
instalar)
uma aplicação em um Servidor Java EE é chamado Deploy ou Deployment.
Sabe-se que componentes são agrupados em módulos, compactados em .ZIP e, na Implantação,mapeia-se cada componente do Java EE para seu contêiner correspondente. Existem três tipos básicos de módulo:
MÓDULO DESCRIÇÃO

EAR Também chamado Enteprise Application Archives, contém a aplicação completa, com todos os seus módulos e componentes. É composta por vários arquivos .war e .jar.
WAR Também chamado Web Application Archives, contém a Aplicação Web
(JSP, HTML, Servlets, Arquivos de Configuração, Imagens, etc) - é o que forma uma página em si.
JAR Também chamado Java Application Archives, contém a Aplicação EJB,
Aplicação Cliente e Applets3, além de arquivos de configuração dos aplicativos.
RAR Também chamado Resource Adapter, contém interfaces, classes,
bibliotecas, etc.

3 A bem da verdade, todos os módulos são Arquivos JAR com a extensão modificada. Por que essa mudança? Para que o servidor possa diferenciar o que está sendo implantado.
/ 235

/

COMMON ANNOTATIONS

Galera, o objeto primário dessa especificação é definir um pequeno conjunto de anotações disponíveis para utilização dentro de outras especificações. Dessa forma, evitam-se redundâncias ou duplicações desnecessárias entre anotações definidas em especificações diferentes, incluindo até mesmo aquelas utilizadas em plataformas distintas. 5aca/?a.7Vamos ver as anotações:
javax.annotation.Generated:

Essa anotação é utilizada para marcar o código-fonte que foi gerado. Ela pode ser especificada em classes, métodos ou campos. Também pode ser usada para diferenciar o código escrito pelo programador e código gerado automaticamente em um mesmo arquivo. Possui três elementos:value, que é o nome do gerador de código; date, que é a data de geração; e comments, que são simplesmente comentários.
javax.annotation.Resource:

Essa anotação é utilizada para declarar uma referência a um recurso. Ela pode ser especificada em classes, métodos ou campos. Quando aplicada a métodos ou campos, o contêiner injetará uma instância do recurso requisitado na aplicação quando ela for inicializada. Se for aplicada a classes,ela declara um recurso que a aplicação procurará em tempo de execução.

javax.annotation.Resources:

Essa anotação é utilizada para declarar uma referência a um recurso. Ela age como um contêiner para múltiplas declarações de recursos. Pessoal, não confundam com a anterior! Uma éResource e a outra é Resources. Quando se têm mais de uma declaração de referência a um recurso,utilizamos a segunda! Não há muito segredo nessa anotação.

javax.annotation.PostConstruct:

Essa anotação é utilizada em um método que necessita ser executado após uma injeção de dependência terminar para executar uma inicialização. Ele é invocado antes de a classe ser colocada em serviço. Essa anotação deve ser suportada em todas as classes que suportam injeção de dependência. O método em que essa anotação é aplicada deve satisfazer diversos critérios.
javax.annotation.PreDestroy:

Essa anotação é utilizada em métodos como uma notificação de retorno para sinalizar que uma instância está no processo de ser removida pelo contêiner. O método com essa anotação é tipicamente utilizado para liberar recursos que esteja mantendo. O método em que essa anotação é aplicada deve satisfazer diversos critérios.
,

javax.annotation.Priority:

Essa anotação pode ser aplicada a classes para indicar em que ordem as classes devem ser utilizadas. O efeito do uso dessa anotação em uma instância particular é definido por outras especificações que definem o uso de uma classe específica - cada classe específica vai dizer qual deverá ser a prioridade de chamada das outras classes. Entenderam?
javax.annotation.security.RunAs:

Essa anotação define a função da aplicação durante a execução em um Contêiner Java
EE. Ela pode especificada em uma classe. Isso permite que os desenvolvedores executem uma aplicação sob uma função particular. A função deve ser mapeada para as informações de usuário/grupo no domínio de segurança do contêiner. O elemento value, nesse elemento, é uma função de segurança.
javax.annotation.security.RolesAllowed:

Essa anotação especifica as funções de segurança permitidas para acessar métodos em uma aplicação. O elemento value dessa anotação é uma lista de nomes de funções de segurança. Essa anotação pode ser especificada em uma classe, quando se aplica a todos os métodos dessa classe;ou em um método, quando se aplica apenas ao método específico.

javax.annotation.security.PermitAII:

Essa anotação especifica que todas as funções de segurança estão autorizadas a invocar métodos específicos. Em outras palavras, podemos dizer que os métodos específicos estão"unchecked".
Essa anotação pode ser especificada em uma classe, quando se aplica a todos os métodos dessa classe; ou em um método, quando se aplica apenas ao método específico.
javax.annotation.security.DenyAII:

Essa anotação especifica que nenhuma função de segurança está autorizada a invocar métodos específicos. Em outras palavras, podemos dizer que os métodos serão excluídos noContêiner Java
EE. Essas três últimas anotações definem quais funções de segurança estão autorizadas a acessar os métodos em que elas foram aplicadas.
javax.annotation.security.DeclareRoles:

Essa anotação é utilizada para especificar as funções de segurança de uma aplicação.
Ela pode ser especificada em uma classe. Ela tipicamente é utilizada para definir funções que poderiam ser testadas de dentro de métodos das classes anotadas. Ela também pode ser utilizada para declarar papéis que não estão implicitamente declarados.
,

javax.annotation.sql.DataSourceDefinition:

Essa anotação é utilizada para definir um contêiner DataSource e para ser registrada com JNDI(Java Naming and Directory Interface). O DataSource pode ser configurado através da definição dos elementos de anotação para propriedades de DataSource comumente utilizadas.Ele é registrado sob o nome especificado no elemento name e determina a acessibilidade da fonte de dados de outros componentes.
javax.annotation.sql.DataSourceDefinitions:

O mesmo que o anterior, porém é possível definir vários DataSource.

javax.annotation.ManagedBean:

Essa anotação é utilizada para declarar um Managed Bean. O que é um Managed Bean? É
um contêiner de objetos gerenciados que suportam um pequeno conjunto de serviços básicos, tais como injeção de recursos, chamadas de ciclo de vida e interceptadores. Um Managed Bean pode opcionalmente possuir um nome, isto é, uma string especificada no elemento value.
OBSERVAÇÕES

Prezados, sabe quantos editais eu encontrei cobrando esse assunto? Somente um!
Sabe quantas questões eu encontrei sobre esse assunto? Absolutamente nenhuma! Logo,saibam dosar seus níveis de atenção e estudos em cada disciplina.
QUESTõES CoMENTADAS -JAVA EE - MULTIBANCAS

1. (CESPE - 2009 - INMETRO - Analista de Sistemas) São exemplos de tipos de componentes de software reusáveis desenvolvidos na plataforma JEE: JSP (Java Server Page); biblioteca de tags;Servlet; EJB. O grau de reúso provido por esses componentes, EJBs e JSPs, é usualmente superior a bibliotecas de TAG.
Comentários:

Galera, vamos responder isso intuitivamente! Como uma Página JSP ou um
Componente EJB
poderia oferecer maior reusabilidade que uma biblioteca? Ora, essa é uma das principais características de uma biblioteca: sua reusabilidade! Logo, isso não faz sentido! Bibliotecas deTags são mais reusáveis. Gabarito: E

2. (CESPE - 2005 - SERPRO - Analista de Sistemas) A tecnologia Enterprise JavaBeans (EJB) é uma arquitetura de componentes do tipo cliente que atua na plataforma J2EE.
Comentários:

Database

JAVA EE 6 (10/12/2009) JAVA EE 7 (12/06/2013)

Enterprise JavaBeans (EJB) 3.1 Enterprise JavaBeans (EJB) 3.2

Conforme vimos em aula, Enterprise Java Bean (EJB) não é uma arquitetura, é um componente daArquitetura J2EE. Além disso, é do tipo Servidor (veja a imagem acima). Gabarito: E

3. (CESPE - 2010 - TCU - Auditor Federal de Controle Externo) A web profile da plataforma JEE
apresenta, em relação ao perfil application server definido em edições anteriores da plataforma
Java, as seguintes vantagens: fornece suporte para POJOs (Plain Old Java
Objects) e
Annotations; possui modelo de empacotamento de componentes mais simples; a configuração dos seus descritores XML (extensible markup language) é mais fácil; é aderente ao padrão SOA.
Comentários:

Imaginem que vamos fazer um sisteminha pequeno! Eu preciso implementar tudo que está na plataforma? Não, posso criar um perfil que implementa somente um subconjunto de funcionalidades! Existem dois perfis importantes: Web Profile e Full Profile! O primeiro perfil é um subconjunto do segundo e ajuda desenvolvedores a criarem aplicações mais leves que podem rodar em um Servlet Container.
Conforme vimos em aula, primeiro, não existe Application Server Profile -
existe apenas Web
Profile e Full Profile. Segundo, o conceito de Perfis foi introduzido apenas no Java
EE 6 - eu calculo que ele esteja considerando Full Profile como Application Server Profile.Terceiro, POJOs e
Annotations são tecnologias do Java EE 5. Quarto, pode-se dizer que é aderente ao SOA
por conta do JAX-RS, no entanto o Full Profile também é (inclusive é aderente ao JAX-RStambém).
Logo, a questão está errada desde o início. Gabarito: E

4. (CESPE - 2010 - TRE/MT - Analista Judiciário - Tecnologia da Informação - A) Clientes J2EE são necessariamente páqinas web dinâmicas que normalmente não fazem acessos a banco de dados,nem executam regras de negócio complexas.

Comentários:

Database

/ 235

/

Conforme vimos em aula, os clientes Java EE não são necessariamente Páginas Web
Dinâmicas
(Browser). A imagem acima mostra que eles podem ser também uma Aplicação Cliente.
Gabarito:
E

5. (CESPE - 2010 - TRE/MT - Analista Judiciário - Tecnologia da Informação - D) Um componente
J2EE é uma unidade funcional de software autocontida, escrito na linguagem de programação
Java e executado exclusivamente em servidores.

Comentários:

Database

Conforme vimos em aula, um componente Java EE é uma unidade autocontida, porque pode ser reusada sem a necessidade de incluir ou depender de outros componentes. Ademais,eles são escritos na linguagem de programação Java, no entanto não são necessariamente executados exclusivamente em servidores, podem ser executados no cliente (conforme imagem acima).Gabarito: E

6. (CESPE - 2011 - PREVIC - Analista de Sistemas) Em uma aplicação multicamadas na plataforma
Java EE, servlets, JavaServer Faces e JSP consistem em tecnologias utilizadas na camada web.

Comentários:

/ 235

/

Data base

Conforme vimos em aula, a Camada Web é composta por JSP, JSF e Servlets. Gabarito: C

7. (ESAF - 2012 - CGU - Analista de Finanças e Controle) Os níveis da plataforma J2EE são:

a) Patrocinador. Web. Negócios. Sistemas de Computação Corporativos.

b) Cliente. Web. Negócios. Sistemas de Informação Corporativos.

c) Cliente. Interno. Externo. Negócios.

d) Fornecedor. Web. Político. Sistemas de Informação Camada.

e) Cliente. Stakeholders. Negócios. Background corporativo.

Comentários:

Camada do Cliente: componentes rodam na Máquina Cliente;
Camada Web: componentes rodam no Servidor Java EE;
Camada de Negócio: componentes rodam no Servidor Java EE;
Camada EIS: software roda no Servidor EIS.

Conforme vimos em aula, os níveis são: Cliente, Web, Negócios e Sistemas de
Informação
Corporativos (EIS). Gabarito: B

8. (CESGRANRIO - 2008 - BNDES - Analista de Sistemas) Uma aplicação empresarial contendo componentes EJB e módulos web deverá ser publicada em um servidor de aplicações compatível com J2EE. No contexto do empacotamento dessa aplicação para publicação (deploy), é correto afirmar que:
a) não há como juntar componentes EJB e módulos web em uma mesma aplicação,
pois deverão ser publicados separadamente.
/ 235

/

b) um arquivo EAR poderá conter arquivos WAR e JAR representativos dos módulos web e
EJB.

c) o tamanho do pacote, em bytes, sempre fica maior que o código original, em virtude do algoritmo empregado no empacotamento da aplicação em um arquivo EAR.
d) módulos web não devem ser empacotados, pois isso inviabiliza seu acesso pela Internet.

e) arquivos JAR servem apenas para empacotar componentes EJB.

Comentários:

Para finalizar, vamos entender algumas coisinhas! O processo de implantar (para alguns,
instalar)
uma aplicação em um Servidor Java EE é chamado Deployment. Sabe-se que componentes são agrupados em módulos, compactados em .ZIP e, na Implantação, mapeia-se cada componente daArquitetura Java EE para seu contêiner correspondente. Existem três tipos básicos de módulo:

Conforme vimos em aula, a primeira opção está errada, porque pode-se junta ambos em umArquivo EAR; a segunda opção está correta e justifica a primeira; a terceira opção está errada,porque são arquivos compactados em .ZIP; a quarta opção está errada, porque simplesmente não faz nenhum sentido; e a última opção está errada porque arquivo JARpode empacotar componentes EJB, Cliente e Applet. Gabarito: B
9. (FCC - 2011 - TRT/19 - Analista de Sistemas) A especificação Java EE define os seguintes componentes:
I. Clientes da aplicação (Application Clients) e applets.

II. Java Servlet, JavaServer Faces e JavaServer Pages.

III. Enterprise Javabeans (EJB).

Os componentes I, II e III rodam, respectivamente, em:

a) cliente, cliente, servidor.

b) servidor, cliente, servidor.

c) cliente, servidor, servidor.

d) servidor, cliente, cliente.

e) cliente, servidor, cliente.

Comentários:

/ 235

/

Database

Conforme vimos em aula, tanto aplicações clientes como applets rodam no cliente;
Servlets, JSF
e JSP rodam no Servidor, assim como o EJBs. Gabarito: C

1O.(FCC - 2011 - TRT - 1a REGIÃO (RJ) - Analista Judiciário - Tecnologia da Informação) J2EE é uma plataforma de programação para servidores na linguagem de programação Java, que integra uma série de especificações e containers, cada uma com funcionalidades distintas. Nesse contexto, é correto afirmar que são integrantes do J2EE:
a) Servlets, Jcompany e JSP.

b) JDBC, JSP, EJBs.

c) EJBs, Servlets e JBoss.

d) JDBC, Hibernate e JPA.

e) JSP, JSF e Eclipse.

Comentários:

JAVA EE 6 (10/12/2009) JAVA EE 7 (12/06/2013)

JavaServer Pages (JSP) 2.2 JavaServer Pages (JSP) 2.3

Enterprise JavaBeans (EJB) 3.1 Enterprise JavaBeans (EJB) 3.2

- Java Database Connectivity
4.0

Conforme vimos em aula, trata-se do JDBC, JSP e EJB! Muitas pessoas me perguntam:
"Professor,
Hibernate não é integrante do J2EE?". Galera, o Hibernate é um framework que implementa a especificação JPA. Logo, ele não faz parte do J2EE ou Java EE. Beleza? Gabarito: B
/ 235

/

11.(FCC - 2010 - TRT - 8a Região (PA e AP) - Analista Judiciário - Tecnologia da
Informação) O
Contêiner J2EE que fornece aos desenvolvedores o ambiente para rodar Java Server Pages
(JSPs) e servlets é:

a) Applet (Applet container).

b) Enterprise Java Beans (EJB).

c) Interface (Interface container).

d) do cliente do aplicativo (Application client container).

e) Web (Web container).

Comentários:

Database

Conforme vimos em aula, o Contêiner Web é o responsável por rodar JSP/ServIet! Gabarito: E

12.(FCC - 2010 - TCE-SP - Agente da Fiscalização Financeira - Informática - Suporte de Web) São apenas tipos de componentes executados em servidores Web:
a) Beans, Servlets e J2EE.

b) JVM, Servlets e JSP.

c) Beans, Servlets e JSP.

d) Beans, Swing e JSP.

e) Beans, Swing e JVM.

Comentários:

/ 235

/

Database

Conforme vimos em aula, JSP e Servlets são fáceis! E os beans? Pois é,
excepcionalmente eles podem ser executados em Servidores Web (Contêiner Web). Gabarito: C
13. (FCC - 2014 - TRT/2 - Analista de Sistemas) Um contêiner Java EE pode oferecer serviços como gestão de memória, ciclo de vida e estado de objetos, conexões, transações, serviços de nomes,segurança, tolerância a falhas, integração, clustering, alta disponibilidade, confiabilidade e web services. Um servidor Java EE completo disponibiliza dois tipos principais de contêiner, que são:
a) Contêiner MVC e Contêiner EJB.

b) Applet Container e Web Container.

c) Contêiner Web e Contêiner EJB.

d) Servlet Container e JSP Container.

e) Application Client Container e Web Container.

Comentários:

Database

Conforme vimos em aula, disponibiliza o Contêiner Web e Contêiner EJB! Gabarito: C

14. (FCC - 2012 - TJ/PE - Analista de Sistemas) Sobre a plataforma Java EE 6, é correto afirmar:

/ 235

/

a) Simplifica a implantação sem a necessidade de descritores de implantação, com exceção do descritor de implantação exigido pela especificação servlet, o arquivo web.xml.
b) Necessita do descritor de implantação ejb-jar.xml e entradas relacionadas aos web services no arquivo web.xml.
c) Faz uso de anotações (annotations). Anotações são modificadores Java, semelhantes aos públicos e privados, que devem ser especificados nos arquivos de configuração XML.
d) A especificação EJB 3, que é um subconjunto da especificação Java EE, define anotações apenas para o tipo bean.
e) Anotações são marcados com um caracter # (cerquilha).

Comentários:

(a) Correto. Pessoal, a plataforma Java EE realmente simplifica a implantação removendo a necessidade de descritores de implantação, mas há uma exceção: o arquivo web.xml;
(b) Descritores de implantação, como o ejb-jar.xml e entradas relacionadas aos Web services no web.xml, já estão obsoletos - não se usa mais!
(c) A Plataforma Java EE utiliza Anotações, que são modificadores Java, semelhantes aos públicos e privados. No entanto, eles são especificados no código!
(d) Ele define anotações para o tipo Bean, tipo de Interface, referências de recurso,
atributos de transação, segurança, etc;
(e) Essa ele entregou! Anotações são marcados com @. Gabarito: A

/ 235

/

LISTA DE QUESTõES-JAVA EE - MULTIBANCAS

1. (CESPE - 2009 - INMETRO - Analista de Sistemas) São exemplos de tipos de componentes de software reusáveis desenvolvidos na plataforma JEE: JSP (Java Server Page); biblioteca de tags;Servlet; EJB. O grau de reúso provido por esses componentes, EJBs e JSPs, é usualmente superior a bibliotecas de TAG.
2. (CESPE - 2005 - SERPRO - Analista de Sistemas) A tecnologia Enterprise JavaBeans (EJB) é uma arquitetura de componentes do tipo cliente que atua na plataforma J2EE.
3. (CESPE - 2010 - TCU - Auditor Federal de Controle Externo) A web profile da plataforma JEE
apresenta, em relação ao perfil application server definido em edições anteriores da plataforma
Java, as seguintes vantagens: fornece suporte para POJOs (Plain Old Java
Objects) e
Annotations; possui modelo de empacotamento de componentes mais simples; a configuração dos seus descritores XML (extensible markup language) é mais fácil; é aderente ao padrão SOA.
4. (CESPE - 2010 - TRE/MT - Analista Judiciário - Tecnologia da Informação - A) Clientes J2EE são necessariamente páginas web dinâmicas que normalmente não fazem acessos a banco de dados,nem executam regras de negócio complexas.

5. (CESPE - 2010-TRE/MT -Analista Judiciário-Tecnologia da Informação - D) Um componenteJ2EE é uma unidade funcional de software autocontida, escrito na linguagem de programação
Java e executado exclusivamente em servidores.

6. (CESPE - 2011 - PREVIC - Analista de Sistemas) Em uma aplicação multicamadas na plataforma
Java EE, servlets, JavaServer Faces e JSP consistem em tecnologias utilizadas na camada web.

7. (ESAF - 2012 - CGU - Analista de Finanças e Controle) Os níveis da plataforma J2EE são:

a) Patrocinador. Web. Negócios. Sistemas de Computação Corporativos.

b) Cliente. Web. Negócios. Sistemas de Informação Corporativos.

c) Cliente. Interno. Externo. Negócios.

d) Fornecedor. Web. Político. Sistemas de Informação Camada.

e) Cliente. Stakeholders. Negócios. Background corporativo.

/ 235

/

8. (CESGRANRIO - 2008 - BNDES - Analista de Sistemas) Uma aplicação empresarial contendo componentes EJB e módulos web deverá ser publicada em um servidor de aplicações compatível com J2EE. No contexto do empacotamento dessa aplicação para publicação (deploy), é correto afirmar que:
a) não há como juntar componentes EJB e módulos web em uma mesma aplicação, pois deverão ser publicados separadamente.
b) um arquivo EAR poderá conter arquivos WAR e JAR representativos dos módulos web e
EJB.

c) o tamanho do pacote, em bytes, sempre fica maior que o código original, em virtude do algoritmo empregado no empacotamento da aplicação em um arquivo EAR.
d) módulos web não devem ser empacotados, pois isso inviabiliza seu acesso pela Internet.

e) arquivos JAR servem apenas para empacotar componentes EJB.

9. (FCC - 2011 - TRT/19 - Analista de Sistemas) A especificação Java EE define os seguintes componentes:
I. Clientes da aplicação (Application Clients) e applets.

II. Java Servlet, JavaServer Faces e JavaServer Pages.

III. Enterprise Javabeans (EJB).

Os componentes I, II e III rodam, respectivamente, em:

a) cliente, cliente, servidor.

b) servidor, cliente, servidor.

c) cliente, servidor, servidor.

d) servidor, cliente, cliente.

e) cliente, servidor, cliente.

10. (FCC - 2011 - TRT - 1a REGIÃO (RJ) - Analista Judiciário - Tecnologia da Informação) J2EE é uma plataforma de programação para servidores na linguagem de programação Java, que integra uma série de especificações e containers, cada uma com funcionalidades distintas. Nesse contexto, é correto afirmar que são integrantes do J2EE:
a) Servlets, Jcompany e JSP.

b) JDBC, JSP, EJBs.

c) EJBs, Servlets e JBoss.

d) JDBC, Hibernate e JPA.

e) JSP, JSF e Eclipse.

11. (FCC - 2010 - TRT - 8a Região (PA e AP) - Analista Judiciário - Tecnologia da
Informação) O
Contêiner J2EE que fornece aos desenvolvedores o ambiente para rodar Java Server Pages
(JSPs) e servlets é:

a) Applet (Applet container).

b) Enterprise Java Beans (EJB).

c) Interface (Interface container).

d) do cliente do aplicativo (Application client container).

e) Web (Web container).

12. (FCC - 2010 - TCE-SP - Agente da Fiscalização Financeira - Informática - Suporte de Web) São apenas tipos de componentes executados em servidores Web:
a) Beans, Servlets e J2EE.

b) JVM, Servlets e JSP.

c) Beans, Servlets e JSP.

d) Beans, Swing e JSP.

e) Beans, Swing e JVM.

13. (FCC - 2014 - TRT/2 - Analista de Sistemas) Um contêiner Java EE pode oferecer serviços como gestão de memória, ciclo de vida e estado de objetos, conexões, transações, serviços de nomes,segurança, tolerância a falhas, integração, clustering, alta disponibilidade, confiabilidade e web services. Um servidor Java EE completo disponibiliza dois tipos principais de contêiner, que são:
a) Contêiner MVC e Contêiner EJB.

b) Applet Container e Web Container.

c) Contêiner Web e Contêiner EJB.

d) Servlet Container e JSP Container.

e) Application Client Container e Web Container.

14. (FCC - 2012 - TJ/PE - Analista de Sistemas) Sobre a plataforma Java EE 6, é correto afirmar:

a) Simplifica a implantação sem a necessidade de descritores de implantação, com exceção do descritor de implantação exigido pela especificação servlet, o arquivo web.xml.
b) Necessita do descritor de implantação ejb-jar.xml e entradas relacionadas aos web services no arquivo web.xml.
,

c) Faz uso de anotações (annotations). Anotações são modificadores Java, semelhantes aos públicos e privados, que devem ser especificados nos arquivos de configuração XML.
d) A especificação EJB 3, que é um subconjunto da especificação Java EE, define anotações apenas para o tipo bean.
e) Anotações são marcados com um caracter # (cerquilha).

/ 235

/

GABARITo

GABARITO

1. E 6. C
11. E

2. E 7. B
12. C

3. E 8. B
13. C

4. E 9. C
14. A

5. E 10. B

/

JAVA SERVER PAGES (JSP)

Primeiro, o que é JSP? É uma tecnologia da plataforma Java Enterprise Edition (Java
EE) que permite utilizar ou o código Java dentro das páginas web ou tags que realizam sua lógica. Por ser tecnologia Java, seus objetos são definidos segundo define a linguagem, i.e.,podendo utilizar todos os seus recursos, tais como modificadores de acesso, tratamento de exceções, entre outros.
Galera, trata-se de uma tecnologia para geração de documentos baseados em texto e executados do lado do servidor (assim como Servlets). Professor, como assim texto? Esse texto pode ser um conjunto de dados estáticos (Ex: HTML e XML); ou pode ser um conjunto de elementosJSP e tags customizadas, que definem como a página construirá conteúdo dinâmico.
Professor, como funciona esse tal de JSP? Cara, Páginas JSP utilizam tags XML e
Scriptlets escritos em Java para encapsular a lógica que gera o conteúdo para a página web. Ele separa a lógica do conteúdo da sua apresentação. Páginas JSP são compiladas em Servlets e podem chamar beans a fim de executar o processamento no servidor. Espera, professor! Como assim são compiladas em Servlets?
Cara, Páginas JSP tipicamente se tornam uma Servlet! Vocês podem me perguntar: Por que, então,precisamos da tecnologia JSP se já temos a tecnologia de Servlets?
Teoricamente, é possível escrever apenas Servlets para desenvolver suas aplicações web. No entanto, a TecnologiaJSP foi desenhada para simplificar o processo de criação de páginas ao separar a apresentação do conteúdo.
Em muitas aplicações, a resposta enviada ao cliente é a combinação dos dados de apresentação(template) com dados de conteúdo gerados dinamicamente. Nesse caso, é muito mais fácil trabalhar com Páginas JSP do que fazer tudo com Servlets. Galera, basta pensar nos conceitos de coesão, acoplamento e modularidade. Vocês entenderam a sacada do negócio?
É mais simples, organizado e legível utilizar uma tecnologia para fazer a apresentação e outra para gerar dados dinamicamente - assim, mantém-se a divisão de responsabilidades, a independência entre os módulos, entre outros benefícios. Você ainda não entendeu? Acho que sei como fazer isso entrar na sua cabeça: vamos ver agora uma Servlet e uma Página JSP!
Arquivo: HelloWorld.jsp (No MVC, em geral, é utilizada como Visão)

<html>

<head>

<title>

<%="Hello World "%>

</title>

/ 235

/

</head>

<body>

<%out.println("Hello Again!");%>

</body>

</html>

Arquivo: HelloWorld.java (No MVC, em geral, utilizada como Controladora)

//Definições e importações.

public void doGet(HttpServletRequest request, HttpServIetResponse response) throws lOException, ServIetException {
Writer out = response.getWriter();

out.println("<htmlxheadxtitle>");
out.println(" HelloWorld");
out.println("</title></headxbody>");
out.println(" HelloAgain");
out.println("</bodyx/html>");
out.flush();

out.closeO;

}

Galera, esses códigos são semelhantes: o primeiro é uma Página JSP (Arquivo .jsp ou
.jspx1) e o segundo é uma Servlet (Arquivo .java). Vocês percebem que no primeiro código nós temos códigoHTML com algumas coisas de Java? Já no segundo nós temos Java com algumas coisas de
HTML?
Vejam como é chato escrever o segundo código - é preciso colocar as tags HTML dentro das funções de escrita do Java.
Já imaginaram que insuportável fazer isso para arquivos muito grandes? Pois é, JSP
torna possível desenvolver aplicações web sem ter que escrever todo código estático dentro de servlets.Professor, eu posso ter uma Página JSP sem nenhum código Java? Claro, não é obrigatório ter código Java, no entanto é ele quem permite suportar comportamento dinâmico em páginas web.
Outra desvantagem importante é que o programador, além de ser bom em Java, tem que ser bom em Web Design! No entanto, quando ele está escrevendo o código Java, ele não possui as ferramentas de Web Design! O JSP permite essa separação, i.e., os Desenvolvedores Java criam as Servlets (Lógica de Negócio) e os Web Designers criam as Páginas JSP(Lógica de
Apresentação)!2 Bacana?

1 .jspx refere-se ao Arquivo JSP que obedecer às regras de formação do XML.

2 Antes, para cada mudança no Código HTML, uma recompilação da servlet era necessária. Para fazer essa separação que foi criada a Tecnologia JSP.
x'"'

/ 235

/

Um grande benefício dessa tecnologia é a integração com HTML! Galera, HTML é uma linguagem amplamente conhecida e estudada! Portanto, facilita a criação de páginas web dinâmicas tendo que, posteriormente, apenas embutir o código Java! O que isso significa? Significa que,quando o código Java for executado, parte da página será gerada em tempo de execução (dinamismo).
Além da perfeita integração com HTML, Páginas JSP também oferecem modos de manipulação de arquivos texto (Ex: PDF, DOCX, etc); suportam criptografia de dados; suportam a utilização de cookies e sessões; suportam a manipulação de Arquivos XML; suportam diversos bancos de dados e sistemas de relatórios; possuem baixo custo de aprendizagem; entre outras vantagens.
Em suma: JSP é uma linguagem de script server-side com especificação aberta cujo principal objetivo é a geração simples, prática e rápida de conteúdo dinâmico para páginas web.É uma tecnologia que possui o suporte de vários servidores, tais como: Tomcat, GlassFish,JBoss, entre outros. Ela define a interação entre Servidor e Página JSP, e descreve o formato e sintaxe da página. Vamos ver como tudo funciona?
Bem, lá em cima eu disse que Páginas JSP tipicamente se tornam uma Servlet! Como assim,professor? Em relação a Servlets, o processamento da Página JSP passa por uma camada adicional em que a página é compilada e transformada em uma Servlet no Servidor Web. Simples,não?! Se vocês possuem uma página .html, renomeiem-a para .jsp e coloquem-na em um Servidor Web.
Ao fazer isso, a página é automaticamente transformada em uma Servlet! No primeiro acesso, a compilação é realizada. Nos acessos subsequentes, a requisição é redirecionada para aServlet que foi gerada anteriormente. Quando o arquivo .html se transforma em um arquivo .jsp,ele já pode conter scriptlets, diretivas, expressões, etc. Entendido?
A partir daí, o ciclo de vida é exatamente igual ao de uma Servlet, porém com métodos diferentes(apesar de semelhantes). Agora que tal vermos em detalhes um pouco sobre a sintaxe da nossa linguagem, i.e., declarações, expressões, scriptlets, comentários, ações e diretivas.Antes de partir para as sintaxes, vamos ver um pouco sobre os objetos implícitos!
Galera, objetos implícitos são os objetos que são criados de forma automática pelo
Contêiner JSP
e posteriormente disponibilizados para os desenvolvedores, de maneira que eles não precisam ser instanciados explicitamente. No JSP, existem nove: request, response, pageContext,application,
out, config, page, session e exception. Em seguida, veremos a sintaxe da linguagem!

,

PROVA!

OBJETO DESCRIÇÃO

request Objeto do tipo HttpServIetRequest e contém a informação do pedido HTTP.
response Objeto do tipo HttpServIetResponse e contém a resposta HTTP
que vai ser enviada ao cliente. Não é usado com frequência.

pageContext Objeto do tipo PageContext e contém informações de contexto para execução da página.
application Objeto do tipo ServIetContext que permite compartilhar informações entre todos os componentes web da aplicação.
out Objeto da classe JspWriter que permite imprimir para o response através do método println.
config Objeto do tipo ServIetConfig da página JSP.

page Sinônimo do operador "this" do objeto HttpJspPage. Não é usado com frequência.
session Objeto do tipo HttpSession que guarda informações da sessão de um usuário específico entre múltiplas requisições.
exception É o objeto Throwable que é resultante de uma situação de erro numa página JSP.
Declarações

Galera, Declarações são similares às declarações em Java e definem variáveis, objetos e métodos para uso subsequente em expressões ou scriptlets. Alguns alunos me perguntam como eu decoro isso! Bem, uma declaração declara! Declara o quê? Variáveis! Como? Com ponto de exclamação.
Quando eu gosto de enfatizar uma declaração, eu uso um ponto de exclamação!
No JSP, é similar...
//Declarações JSP

<%! public final static String[] estacões = {"Primavera", "Verão", "Outono", "Inverno"} %>

Expressões

Expressões retornam valores que são inseridos dinamicamente na página no lugar da expressão,i.e., toda expressão é avaliada, executada, convertida em uma string e inserida no local onde aparece a expressão no Arquivo JSP. Falando de outra maneira: expressões são utilizadas para embutir o resultado da avaliação de uma expressão na Página JSP. Detalhe: não se termina a expressão com ponto-e-vírgula!
O valor é convertido em um objeto string e inserido no objeto implícito out. Esse objeto tem escopo de página e permite acessar o fluxo de saída da Servlet. Como você decorava isso,professor? Bem, eu me lembrava de expressões matemáticas! Por que? Porque, assim como asExpressões JSP, elas geralmente possuem o sinal de igualdade (=). Expressões são similares aScriptlets!

//Expressões JSP

<%= idade = idade + 1 %>

<%= "Esse é seu aniversário de " + idade + "anos" %>

Scriptlets

Scriptlets são importantíssimos e, de todos, é facilmente o que mais cai em prova3!
Trata-se de blocos de Código Java embutidos em uma Página JSP. Qualquer código válido na linguagemJava pode ser inserido em um scriptlet! Galera, como eu decorava isso? É o mais simples:é o único que não possui nada após o sinal de porcentagem.
Quando transformamos Páginas JSP em Servlets, tudo aquilo que for scriptlet é traduzido para chamadas out.println() no método JspService da servlet gerada. A variável de uma linguagem de programação criada dentro de um scriptlet pode ser acessada de qualquer lugar dentro da PáginaJSP. Dentro das scriptlets, estamos lidando com Java. Abaixo a instrução manda escrever
"Bem vindo!".
3 Apesar disso, hoje em dia, é considerado má prática utilizar Scriptlets em Páginas JSP.

Vocês se lembram que eu falei que expressões são similares a scriptlets? Pois é, a expressão <%expressão %> equivale a out.println(expressão), visto que o valor da expressão é convertido em uma string e inserido no objeto implícito out. A partir daí, funciona como um scriptlet <%out.println(expressão) %>. Entenderam agora a similaridade entre ambos? ;)

//Scriptlets JSP

<html>

<body>

<%! String mensagem = "Bem vindo!"; %>

<% out.println(mensagem); %>

</body>

</html>

Comentários

Comentários não mudam muito em relação a outras linguagens. Eles são completamente ignorados pelo tradutor da página e, nesse caso, possui uma sintaxe bastante parecida com a daLinguagem HTML. Enfim, eles servem apenas para ajudar o desenvolvedor e em nada interferem na página que o cliente visualiza! Há duas maneiras de se fazer um comentário:
//Comentários JSP

<%— Comentário JSP —%> // Em HTML, seria: <!- Comentário HTML —>

Ações

Ações permitem acessar e alterar regras de negócio por meio das propriedades de
JavaBeans4.
Ademais, disponibilizam comando para redirecionamento de Requisições JSP para outra Servlet ou Página JSP. Esse também é tranquilo de decorar, porque é o único que utiliza a sigla jsp.Professor, você pode dar um exemplo de Ação JSP? Claro, meu querido! Temos vinte delas:

JSP:USEBEAN jsp:param jsp:invoque

JSP:SETPRoPERTY jsp:fallback jsp:doBody

JSP:GETPRoPERTY jsp:text jsp:elemento

JSP:INCLUDE jsp:plugin jsp:body

JSP:FoRwARD jsp:params jsp:attribute jsp:output jsp:root jsp:declaration jsp:scriptlet jsp:expression
4 JavaBeans são componentes reutilizáveis de software que podem ser manipulados visualmente com a ajuda de uma ferramenta de desenvolvimento.
/ 235

/

Essas ações ajudam a controlar o comportamento da Engine da Servlet. As ações mais famosas e conhecidas são:
jsp:include: usada para inserir conteúdo dinâmico em tempo de solicitação;

jspdorward: usada para redirecionar requisições para outra Página JSP;

jsp:param: usada para passar parâmetros para outra Ação JSP;

jsp:useBean: usada quando se deseja invocar/instanciar um JavaBean5;

jsp:plugin: usada para executar e mostrar um objeto (Ex: Applet) no browser.

jsp:setProperty: usada para setar o valor da propriedade de um JavaBean;

jsp:getProperty: usada para recuperar o valor da propriedade de um JavaBean.

Diretivas são instruções enviadas ao servidor contendo informações que definam algum procedimento para o processo de compilação da página. Em outras palavras, podemos dizer que são instruções processadas quando a Página JSP é compilada em uma Servlet. As Diretivas são utilizadas para importar classes de um pacote, inserir dados de arquivos externos e habilitar o uso de bibliotecas de tags.
Ao compilar uma Página JSP em uma Servlet, essas instruções podem afetar sua estrutura, no entanto não criam nenhuma saída visível. Ademais, são interpretadas pelo contêiner antes mesmo de qualquer elemento! Existem três diretivas principais:
* page - define atributos de configuração da Página JSP.

PROVA!

ATRIBUTO PROPÓSITO

5 Ele ajuda a localizar a instanciar Componentes JavaBean. Dessa forma, não é necessário instanciar explicitamente um objeto da classe para acessar seus métodos.
buffer Especifica o modelo de buffering da saída padrão.

autoFlush Controla o comportamento da saída padrão da Servlet.

contentType Define a codificação de caracteres e media type (MIME)
errorPage Define a URL de outro JSP que reporta exceções.
isErrorPage Indica se a Página JSP possui URL de outra página.

Extends Especifica uma superclasse a ser estendida pela servlet.

Import Especifica uma lista de pacotes ou classes importadas.

Info Define uma string que pode ser acessada para informações.

isThreadSafe Define se a servlet é capaz de atender múltiplas solicitações.

language Define a linguagem de programação utilizada.

Session Especifica se a Página JSP participa de Sessões HTTP.

isELIgnored Especifica se Linguagens de Expressão serão ignoradas.

isScriptingEnabled Determina se elementos de script são permitidos.

//Diretiva PAGE

<%@ page import = "java.swing.*" %>

// Page pode usar 11 atributos: Info; Language; ContentType; Extends; Import; Session;
Buffer;
AutoFIush; isThreadSafe; errorPage; isErrorPage.

include - inclui recursos estáticos em uma Página JSP.

//Diretiva INCLUDE

<%@ include file = "teste.jsp" %>

taglib - estende o conjunto de tags através de uma biblioteca de tags.

//Diretiva TAGLIB

<%@ taglib uri = "http://serlets.com/testes" prefix = "ops" %>

COMPONENTES EM INGLÊS SINTAXE

Declarações Declarations

Expressões Expressions

Scriptlets Scriptlets

<%! %>

<%= Expressão %>

<% Scriptlet %>

,

Comentários Comments

Ações Actions

Diretivas Directives

<%- Comentário -%>

<jsp: Ação />

<%@ Diretiva %>

Por fim, vamos falar um pouquinho sobre Expression Language! Como vimos, podemos utilizarScriptlets e Expressões para recuperar atributos e parâmetros em Páginas JSP por meio de CódigoJava e utilizá-los para propósitos de Apresentação (ou Visão). No entanto - para Web
Designers -

, Código Java é difícil de entender e foi para isso que foi criada a Expression Language6!

Desenvolvida pela Sun, ela é interpretada pelo Servlet Container e busca remover um pouco doCódigo Java que fica na Página JSP. Agora Web Designers pode recuperar atributos e parâmetros facilmente utilizando tags HTML-like. Em geral, quando se especifica o valor de um atributo em uma tag JSP, simplesmente utiliza-se uma string, como é mostrado abaixo:
<jsp:setProperty name="cubo" property="perímetro" value="120"/>

O exemplo apresentado acima apresenta algumas propriedades de um Componente
JavaBean,
de forma que um Cubo possui um Perímetro de 120 unidades de medida (Ex: Centímetro).
Uma
JSP Expression Language (JSPEL) permite especificar uma expressão para qualquer um desses valores de atributos mostrados acima. Uma sintaxe simples é:
${expressão}

Os operadores mais comuns do JSPEL são e "[ ]". Esses dois operadores (ponto e colchetes)permitem acessar diversas atributos de Componentes JavaBeans. Por exemplo,
poderíamos escrever a primeira expressão da maneira mostrada abaixo! Quando o Compilador JSPencontrar a forma ${...} em um atributo, ele gerará código para avaliar a expressão e substituir seu valor.
<jsp:setProperty name="cubo" property="aresta" value="10"/>

<jsp:setProperty name="cubo" property="perímetro" value="${12*cubo.aresta}"/>

Vejam que o Valor do Perímetro do Cubo é dado pela expressão contida em value presente na segunda linha. O operador Ponto permite acessar o valor da propriedade aresta do JavaBeans cubo e disso, seu valor continua sendo 120 unidades de medida. No entanto,o Operador
Colchetes é mais poderoso, visto que pode recuperar dados de listas, vetores e mapas.
Vejamos abaixo:
${Lista[1 ]}

${Lista["1"]} // É exatamente igual ao anterior

6 O JSP 2.1 trouxe suporte a Unified Expression Language (UEL), que representa a união da linguagem de expressão oferecida pelo JSP 2.0 e a criada linguagem de expressão criada para o JSF.
${Lista[ "Carro"]}

${Lista.Carro} // É exatamente igual ao anterior

A JSPEL suporta a maioria dos operadores aritméticos e lógicos do Java, além de muitos outros.Além disso, ela é baseada em propriedades aninhadas e coleções; operadores relacionais,
lógicos e aritméticos, funções estendidas de mapeamento em métodos estáticos de Classes Java; e um conjunto de objetos implícitos. Ademais, podem ser usados em textos estáticos e atributos de tags.
Professor, o que é esse negócio vermelho do último parágrafo? Cara, JSPEL permite a definição de funções (por meio de tags personalizadas) que podem ser chamadas em uma expressão.Para tal, deve-se definir o método da classe que realiza a função como público e estático.Em seguida,
deve-se mapear o nome da função no Tag Library Descriptors (TLD, ou Descritor de
Biblioteca de
Tags).

Por fim, devemos utilizar a Diretiva Taglib para importar a Biblioteca de Tags personalizada que agora contém essa função e invocá-la pelo seu prefixo. Professor, o nome do método público que realiza a função deve ser o mesmo nome da própria função? Não é obrigatório! Afunção pode se chamar Multiplica e o método que a realiza se chamar Divida - sem nenhum problema.
,

QUESTõES CoMENTADAS - JSP - CEBRASPE

1. (CESPE - 2013 - CNJ - Analista de Sistemas) Como forma de incluir dinamismo em páginasJSP, é possível incluir blocos de código Java conhecidos como scriptlets.

Comentários:

Scriplets são importantíssimos e, de todos, é facilmente o que mais cai em prova!
Trata-se de blocos de Código Java embutidos em uma Página JSP. Qualquer código válido na linguagemJava pode ser inserido em um scriplet! Galera, como eu decorava isso? É o mais simples: é o único que não possui nada após o sinal de porcentagem.
Conforme vimos em aula, trata-se dos Scriplets. Gabarito: C

2. (CESPE - 2011 - PREVIC - Analista de Sistemas) O container JSP provê uma lista de objetos instanciados, chamados de objetos implícitos. É através do objeto aplicação (application object) que são rastreadas as informações de um cliente específico entre múltiplas requisições.
Comentários:

OBJETO DESCRIÇÃO

request Objeto do tipo HttpServIetRequest e contém a informação do pedido HTTP.
response Objeto do tipo HttpServIetResponse e contém a resposta HTTP
que vai ser enviada ao cliente. Não é usado com frequência.

pageContext Objeto do tipo PageContext e contém informações de contexto para execução da página.
application Objeto do tipo ServIetContext que permite compartilhar informações entre todos os componentes web da aplicação.
,

out Objeto da classe JspWriter que permite imprimir para o response através do método println.
config Objeto do tipo ServIetConfig da página JSP.

page Sinônimo do operador "this" do objeto HttpJspPage. Não é usado com frequência.
session Objeto do tipo HttpSession que guarda informações da sessão de um usuário específico entre múltiplas requisições.
exception É o objeto Throwable que é resultante de uma situação de erro numa página JSP.
Galera, olhem para as duas definições acima! A questão está se referindo ao Objeto
Application ou Session? Evidente que é o Session! Gabarito: E
3. (CESPE - 2013 - TRT/10 - Analista de Sistemas) Nas páginas JSP, combinam-se modelos estáticos, incluindo fragmentos de HTML ou XML, com o código para gerar conteúdo dinâmico e compilar páginas JSP dinamicamente em servlets, quando solicitado.
Comentários:

Galera, trata-se de uma tecnologia para geração de documentos baseados em texto e executados do lado do servidor (assim como Servlets). Professor, como assim texto? Esse texto pode ser um conjunto de dados estáticos (Ex: HTML e XML); ou pode ser um conjunto de elementosJSP e tags customizadas, que definem como a página construirá conteúdo dinâmico.
Conforme vimos em aula, combina estático e dinâmico, compilando em servlets. Gabarito: C

4. (CESPE - 2013 - TRT/10 - Analista de Sistemas) O JSP, cuja base é a linguagem de programação Java, tem portabilidade de plataforma, o que o permite ser executado em diversos sistemas operacionais, como o Windows e o Linux.
Comentários:

/ 235

/

Primeiro, o que é JSP? É uma tecnologia da plataforma Java Enterprise Edition (Java
EE) que permite utilizar ou o código Java dentro das páginas web ou tags que realizam sua lógica. Por ser tecnologia Java, seus objetos são definidos segundo define a linguagem, i.e.,podendo utilizar todos os seus recursos, tais como modificadores de acesso, tratamento de exceções, entre outros.
Conforme vimos em aula, é uma Tecnologia Java! Logo, é portável e multiplataforma,
podendo ser executada em qualquer sistema operacional que possua uma Java VirtualMachine (JVM).
Gabarito: C

5. (CESPE - 2013 - TRT/10 - Analista de Sistemas) Para usar o JSP com Java embutido e algumas tags de marcação complexas, o programador tem de conhecer a fundo as complexidades do desenvolvimento de aplicações.
Comentários:

Conhecer a fundo as complexidades do desenvolvimento de aplicações? Galera, quem hoje em dia conhece a fundo o desenvolvimento de aplicações? Nós estamos em uma era de especialização e componentização, ou seja, cada um é especialista em uma área. O programador deve conhecer bem JSP e, não, os meandros de todo desenvolvimento de aplicações. Não faz sentido dizer que ele precisa conhecer a fundo as complexidades do desenvolvimento de aplicações. Gabarito: E
6. (CESPE - 2013 - SERPRO - Analista - Suporte Técnico) Um scriptlet na tecnologia
JSP (Java server pages) abrange todo o código entre "<#" e
Comentários:

COMPONENTES EM INGLÊS SINTAXE

Declarações Declarations <%! %>

Expressões Expressions <%= Expressão %>

Scriptlets Scriptlets <% Scriptlet
%>

Comentários Comments <%- Comentário -%>

,

Ações Action s <jsp: Ação
/>

Diretivas Directives <%@ Diretiva
%>

Conforme vimos em aula, scriplets vem entre "<%" e Gabarito: E

7. (CESPE - 2011 - CBM-DF - Oficial Bombeiro Militar Complementar - Informática) O
uso de
Javabeans, o controle de transferência entre as páginas e o suporte independente de appletsJava pelos browsers são possibilidades proporcionadas pela action tag da JSP.

Comentários:

JSP:USEBEAN jsp:param jsp:invoque jsp:output
JSP:SETPRoPERTY jsp:fallback jsp:doBody jsp:root

JSP:GETPRoPERTY jsp:text jsp:elemento jsp:declaration
JSPJNCLUDE jsp:plugin jsp:body jsp:scriptlet
JSP:FoRwARD jsp:params jsp:attribute jsp:expression
Essas ações ajudam a controlar o comportamento da Engine da Servlet. As ações mais famosas e conhecidas são: (...)
* jsp:useBean: usada quando se deseja invocar/instanciar um JavaBean;

* jsp:plugin: usada para executar e mostrar um objeto (Ex: Applet) no browser.

Conforme vimos em aula, temos: jsp:useBean (para uso de javabeans); jsp:forward (para controle de transferência entre páginas); e jsp:plugin (para suporte a applets). Gabarito: C
8. (CESPE - 2011 - PREVIC - Analista de Tecnologia da Informação) Em uma aplicação multicamadas na plataforma Java EE, servlets, JavaServer Faces e JSP consistem em tecnologias utilizadas na camada web.
Comentários:

,

Galera, todos eles são da Camada Web! A fonte oficial diz: "Java Servlet, JavaServer
Faces, and
JavaServer Pages (JSP) technology components are web components that run on the server",conforme podemos ver na imagem abaixo:

Java EE Application 1 Java EE Application 2

Application
Client

Dynamic
HTML Pages

Client Tier

_ Client

Machine

_ Java EE
Server

EIS Tier

_ Database
Server

Gabarito: C

9. (CESPE - 2017 - TRE/BA - Analista de Sistemas) A respeito da JSP (JavaServer Pages), assinale a opção correta.
a) As páginas JSP compiladas não precisam ser executadas em uma máquina virtual Java (JVM).

b) O scriptlet é o conteúdo integral de um trecho de código Java que esteja dentro das tags
<script>código< /script>.

c) O comando <c:out value="conteúdo"/> avalia uma expressão e insere o seu resultado na saída,podendo o conteúdo do atributo value ser dinâmico como um texto literal ou uma expressão escrita.
d) O método POST do HTML não pode ser utilizado para enviar ou receber dados.

e) Uma página criada com a tecnologia JSP, depois de instalada em um servidor de aplicação compatível, estará pronta para ser executada, não havendo a necessidade de ela ser transformada em um Servlet.
Comentários:

(a) Errado, elas precisam ser executadas em uma JVM; (b) Errado, <script> e </script>
são tags para inserir código Javaccript em Páginas HTML - o correto para scriplets seria <%... %>; (c)
Correto. O comando <c:out> é uma tag JSTL que exibe o resultado de uma expressão,
sendo o
"value" a informação de saída. Poderia ser utilizado <%= %>, mas o comando <c:out>
oferece x'
/ 235

/

oportunidade de dar dinâmica ao permitir que o valor seja um bean e que se possa utilizar a notação "Para acessar propriedades; (d) Errado, é claro que pode - é para isso que ele serve;
(e) Errado, há necessidade de ser transformada em uma Servlet. Gabarito: C

QUESTõES CoMENTADAS - JSP - MULTIBANCAS

1. (FCC - 2012 - TRE-SP - Técnico Judiciário - Programação de Sistemas) As tags utilizadas em uma página JSP para importar classes de um pacote, habilitar o uso de bibliotecas de classes(por exemplo, JSTL) e incluir arquivos (por exemplo, JSP Fragments) são conhecidas como tags:
a) diretivas.

b) de scriptlet.

c) de declaração.

d) de expressão.

e) standard action.

Comentários:

Diretivas são instruções enviadas ao servidor contendo informações que definam algum procedimento para o processo de compilação da página. Em outras palavras, podemos dizer que são instruções processadas quando a Página JSP é compilada em uma Servlet. AsDiretivas são utilizadas para importar classes de um pacote, inserir dados de arquivos externos e habilitar o uso de bibliotecas de tags.
Conforme vimos em aula, trata-se das Diretivas. Gabarito: A

2. (FCC - 2009 - PGE-RJ - Técnico Superior de Análise de Sistemas e Métodos) Blocos ou trechos de operações em código Java podem ser incluídos em uma página JSP por meio de:
a) diretiva page.

b) diretiva include.

c) comentário.

d) taglib.

e) scriptlet.

Comentários:

,

Scriplets são importantíssimos e, de todos, é facilmente o que mais cai em prova!
Trata-se de blocos de Código Java embutidos em uma Página JSP. Qualquer código válido na linguagemJava pode ser inserido em um scriplet! Galera, como eu decorava isso? É o mais simples: é o único que não possui nada após o sinal de porcentagem.
Conforme vimos em aula, trata-se das Scriplets. Gabarito: E

3. (FCC - 2010 - TRT - 20a REGIÃO (SE) - Técnico Judiciário - Tecnologia da
Informação) Na diretiva page, do JSP, podemos utilizar o atributo import que permite:
a) configurar arquivos html.

b) importar figuras.

c) configurar pacotes.

d) importar arquivos htm e) importar pacotes.
Comentários:

ATRIBUTO PROPÓSITO

buffer Especifica o modelo de buffering da saída padrão.
autoFIush Controla o comportamento da saída padrão da Servlet.
contentType Define a codificação de caracteres e media type (MIME)
errorPage Define a URL de outro JSP que reporta exceções.
isErrorPage Indica se a Página JSP possui URL de outra página.

Extends Especifica uma superclasse a ser estendida pela servlet.
Import Especifica uma lista de pacotes ou classes importadas.

Info Define uma string que pode ser acessada para informações.
isThreadSafe Define se a servlet é capaz de atender múltiplas solicitações.

/ 235

/

language Define a linguagem de programação utilizada.

Session Especifica se a Página JSP participa de Sessões HTTP.
isELIgnored Especifica se Linguagens de Expressão serão ignoradas.
isScriptingEnabled Determina se elementos de script são permitidos.

Conforme vimos em aula, ele especifica uma lista de pacotes ou classes importadas.

Gabarito: E

4. (FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da Informação) Em JSP,
a diretiva taglib define:

a) uma biblioteca de tags para serem usadas na página.

b) um conjunto de classes importadas para serem usadas na página.

c) uma nova tag para ser usada na página.

d) uma biblioteca para ser inserida na página.

e) um módulo logicamente coesivo.

Comentários:

0 taglib - estende o conjunto de tags através de uma biblioteca de tags.

//Diretiva TAGLIB

<%@ taglib uri = "http://serlets.com/testes" prefix = "ops" %>

Conforme vimos em aula, a Diretiva Taglib estende o conjunto de tags através de uma biblioteca de tags, similar ao que diz a primeira opção. Gabarito: A
/ 235

/

5. (FCC - 2008 - MPE-RS - Técnico em Informática - Área Sistemas) Para incluir blocos de códigoJava em uma página JSP utiliza-se a categoria de tags denominada:

a) diretivas.

b) expressões.

c) declarações.

d) scriptlets.

e) comentários.

Comentários:

Scriplets são importantíssimos e, de todos, é facilmente o que mais cai em prova!
Trata-se de blocos de Código Java embutidos em uma Página JSP. Qualquer código válido na linguagemJava pode ser inserido em um scriplet! Galera, como eu decorava isso? É o mais simples: é o único que não possui nada após o sinal de porcentagem.
Conforme vimos em aula, trata-se dos Scriplets. Gabarito: D

6. (FCC - 2010 - METRÔ-SP - Analista - Tecnologia da Informação) Na diretiva page,
do JSP,
utiliza-se o atributo import, que permite:

a) configurar pacotes.

b) importar arquivos html.

c) importar pacotes.

d) configurar arquivos html.

e) importar figuras.

Comentários:

ATRIBUTO PROPÓSITO

buffer Especifica o modelo de buffering da saída padrão.

autoFIush Controla o comportamento da saída padrão da Servlet.
contentType Define a codificação de caracteres e media type (MIME)
errorPage Define a URL de outro JSP que reporta exceções.
isErrorPage Indica se a Página JSP possui URL de outra página.

Extends Especifica uma superclasse a ser estendida pela servlet.
Import Especifica uma lista de pacotes ou classes importadas.

Info Define uma string que pode ser acessada para informações.
isThreadSafe Define se a servlet é capaz de atender múltiplas solicitações.
language Define a linguagem de programação utilizada.

Session Especifica se a Página JSP participa de Sessões HTTP.
isELIgnored Especifica se Linguagens de Expressão serão ignoradas.
isScriptingEnabled Determina se elementos de script são permitidos.

Conforme vimos em aula, ele especifica uma lista de pacotes ou classes importadas.
Gabarito: C

7. (FCC - 2012 - TRE-SP - Técnico Judiciário - Programação de Sistemas) No JavaServer Pages a tag <%=conteúdo %> é uma:
a) Declaration tag.

b) Directive tag.

c) Scriplet tag.

d) Action tag.

e) Expression tag.

Comentários:

,

COMPONENTES EM INGLÊS SINTAXE

Declarações Declarations <%! %>

Expressões Expressions <%= Expressão
%>

Scriptlets Scriptlets <%
Scriptlet %>

Comentários Comments <%- Comentário
-%>

Ações Actions <jsp:
Ação />

Diretivas Directives <%@ Diretiva
%>

Conforme vimos em aula, trata-se da Tag Expression! Gabarito: E

8. (FCC - 2011 - TRE/AP - Analista de Sistemas - A) Em JSP o conceito de classes e objetos não leva em conta os princípios de proteção de dados tanto nas propriedades quanto nos métodos.
Comentários:

Primeiro, o que é JSP? É uma tecnologia da plataforma Java Enterprise Edition (Java
EE) que permite utilizar ou o código Java dentro das páginas web ou tags que realizam sua lógica. Por ser tecnologia Java, seus objetos são definidos segundo define a linguagem, i.e.,podendo utilizar todos os seus recursos, tais como modificadores de acesso, tratamento de exceções, entre outros.
Conforme vimos em aula, leva - sim - em consideração. Gabarito: E

9. (FCC - 2011 - TRE/AP - Analista de Sistemas - C) Em JSP pode-se chamar o construtor do objeto pai em qualquer parte do código e não há tratamento de exceções nos métodos nativos.
Comentários:

Primeiro, o que é JSP? É uma tecnologia da plataforma Java Enterprise Edition (Java
EE) que permite utilizar ou o código Java dentro das páginas web ou tags que realizam sua lógica. Por ser x'
/ 235

/

tecnologia Java, seus objetos são definidos segundo define a linguagem, i.e.,
podendo utilizar todos os seus recursos, tais como modificadores de acesso, tratamento de exceções, entre outros.
Conforme vimos em aula, é código java - sendo assim, pode-se chamar o construtor do objeto pai, pode fazer uso de tratamento de exceções, etc. Gabarito: E
1O.(FCC - 2010 - MPU - Analista de Sistemas) O contêiner, que executa
JSP, transforma o programa JSP em Servlet, assim, a expressão "<%= Math.Random()%>" se torna argumento para out.println().
Comentários:

Expressões retornam valores que são inseridos dinamicamente na página no lugar da expressão,i.e., toda expressão é avaliada, executada, convertida em uma string e inserida no local onde aparece a expressão no Arquivo JSP. Falando de outra maneira: expressões são utilizadas para embutir o resultado da avaliação de uma expressão na Página JSP. Detalhe: não se termina a expressão com ponto-e-vírgula!
Vocês se lembram que eu falei que expressões são similares a scriplets? Pois é, a expressão <%expressão %> equivale a out.println(expressão), visto que o valor da expressão é convertido em uma string e inserido no objeto implícito out. A partir daí, funciona como um scriplet <%out.println(expressão) %>. Entenderam agora a similaridade entre ambos? ;)

Conforme visto em aula, a expressão Math.Random() será avaliada, executada, convertida em uma string e inserida no local onde aparece a expressão no Arquivo JSP. E,por essa razão, é considerada equivalente à Scriplet:
out.println(Math.RandomO)
Gabarito: C

11 .(FCC - 2011 - TRE/AP - Analista de Sistemas - A) Para que métodos estáticos de classes Java sejam executados a partir das funções da linguagem de expressão em JSP, é necessário que o nome da função coincida com o nome do método da classe Java.
Comentários:

/ 235

/

Por fim, devemos utilizar a Diretiva Taglib para importar a Biblioteca de Tags personalizada que agora contém essa função e invocá-la pelo seu prefixo. Professor, o nome do método público que realiza a função deve ser o mesmo nome da própria função? Não é obrigatório! Afunção pode se chamar Multiplica e o método que a realiza se chamar Divida - sem nenhum problema.
Conforme vimos em aula, não é obrigatório. Gabarito: E

12.(FCC - 2009 - TCE/SP - Analista de Sistemas - A) Quando se usa classes do tipo bean, não é necessário instanciar explicitamente um objeto da classe para poder acessar seus métodos. Ainstância do objeto é criada pelo elemento especial:

a) <jsp:useJavaBean/>

b) <jsp:useJava/>

c) <jsp:useBean.Java/>

d) <jsp:useJava.Bean/>

e) <jsp:useBean/>

Comentários:

Essas ações ajudam a controlar o comportamento da Engine da Servlet. As ações mais famosas e conhecidas são:
* jsp:include: usada para inserir conteúdo dinâmico em tempo de solicitação;

* jsp:forward: usada para redirecionar requisições para outra Página JSP;

* jsp:param: usada para passar parâmetros para outra Ação JSP;

* jsp:useBean: usada quando se deseja invocar/instanciar um JavaBean;

* jsp:setProperty: usada para setar o valor da propriedade de um JavaBean;

* jsp:getProperty: usada para recuperar o valor da propriedade de um JavaBean.

Conforme vimos em aula, trata-se do <jsp:useBean>. Gabarito: E

13.(FCC - 2008 - TCE/SP - Analista de Sistema) Nas páginas dinâmicas escritas em JSP,
para declaração de atributos ou métodos, utilizam-se as tags:
a) <% %>

/ 235

/

b) <%! %>

c) <%= %>

d) <%- -%>

e) /* */

Comentários:

COMPONENTES EM INGLÊS SINTAXE

Declarações Declarations <%! %>

Expressões Expressions <%= Expressão
%>

Scriptlets Scriptlets <%
Scriptlet %>

Comentários Comments <%- Comentário
-%>

Ações Actions <jsp:
Ação />

Diretivas Directives <%@ Diretiva
%>

Declarações lembra...? Ponto de Exclamação! Gabarito: B

14. (FCC - 2012 - TST - Analista de Sistemas) Páginas JavaServer Pages são páginas web:

a) que permitem combinar códigos Java, HTML estático, CSS, XML e JavaScript.

b) escritas em Java, sem código HTML

c) Interpretadas e não compiladas.

d) Transformadas em bytecode e executadas no cliente.

e) Combinadas com servlets no desenvolvimento exclusivo de páginas estáticas.

Comentários:

Galera, trata-se de uma tecnologia para geração de documentos baseados em texto e executados do lado do servidor (assim como Servlets). Professor, como assim texto? Esse texto pode ser um conjunto de dados estáticos (Ex: HTML e XML); ou pode ser um conjunto de elementosJSP e tags customizadas, que definem como a página construirá conteúdo dinâmico.
Conforme vimos em aula, pode combinar Java, HTML, CSS, XML, Javascript. A segunda opção está errada porque possui código HTML. A terceira opção está errada porque páginas JSPsão compiladas e interpretadas. A quarta opção está errada porque são executadas no servidor. E,por fim, a última opção está errada porque não é desenvolvimento exclusivo de páginas estáticas
- seu foco é no desenvolvimento de páginas dinâmicas. Gabarito: A

15.(FCC - 2009 - TRT/3 - Analista de Sistemas) NÃO possui uma habilidade de armazenar e recuperar valores de atributos arbitrários o objeto implícito de JSP:
a) Session.

b) Request.

c) Exception.

d) Application.

e) pageContext.

Comentários:

OBJETO DESCRIÇÃO

request Objeto do tipo HttpServIetRequest e contém a informação do pedido HTTP.
response Objeto do tipo HttpServIetResponse e contém a resposta HTTP
que vai ser enviada ao cliente. Não é usado com frequência.

pageContext Objeto do tipo PageContext e contém informações de contexto para execução da página.
application Objeto do tipo ServIetContext que permite compartilhar informações entre todos os componentes web da aplicação.
out Objeto da classe JspWriter que permite imprimir para o response através do método println.
config Objeto do tipo ServIetConfig da página JSP.

page Sinônimo do operador "this" do objeto HttpJspPage. Não é usado com frequência.
session Objeto do tipo HttpSession que guarda informações da sessão de um usuário específico entre múltiplas requisições.
exception É o objeto Throwable que é resultante de uma situação de erro numa página JSP.
Observem que todos eles manipulam informações (atributos arbitrários),
exceto o Objeto
Exception, que apenas retorna erros. Gabarito: C

16. (FCC - 2007 - TRF/4 - Analista de Sistemas) Uma ferramenta usada especificamente para gerar páginas dinâmicas de HTML, baseada em programação Java, é:
a) o WSDL

b) o DTD.

c) a JCP.

d) a XSL

e) o JSP.

Comentários:

Galera, trata-se de uma tecnologia para geração de documentos baseados em texto e executados do lado do servidor (assim como Servlets). Professor, como assim texto? Esse texto pode ser um conjunto de dados estáticos (Ex: HTML e XML); ou pode ser um conjunto de elementosJSP e tags customizadas, que definem como a página construirá conteúdo dinâmico.
/ 235

/

Sabe aquelas questões que você não pode errar de tão fácil? Ei-la! Gabarito: E

17.(FCC - 2013 - ALERN - Analista de Sistemas) Em uma aplicação web desenvolvida utilizando a plataforma Java EE 6, há a seguinte classe Java:
package dados;

public class Cliente {
private String nome;
public ClienteO {

}

public String getNome() {
return nome;

}

public void setNome(String nome) {
this.nome = nome;

}

}

Em uma página JSP da mesma aplicação, para instanciar um objeto desta classe pode-se utilizar a tag:
a) <jsp:setBean name="cliente" class="dados.Cliente"/>

b) <jsp:setBean id="cliente" class="dados.Cliente"/>

c) <jsp:useBean name="cliente" class="dados.Cliente"/>

d) <jsp:useBean id="cliente" class="dados.Cliente"/>

e) <jsp:newlnstance id="cliente" class= "dados.Cliente"/>

Comentários:

,

JSP:USEBEAN jsp:param jsprinvoque jsp:output
JSP:SETPRoPERTY jspdallback jsp:doBody jsp:root

JSP:GETPRoPERTY jsp:text jsp:elemento jsp:declaration
JSPIINCLUDE jsp:plugin jsp:body jsp:scriptlet
JSP:FoRwARD jsp:params jsp:attribute jsp:expression
Essas ações ajudam a controlar o comportamento da Engine da Servlet. As ações mais famosas e conhecidas são: (...)
* jsp:useBean: usada quando se deseja invocar/instanciar um JavaBean;

//Ações JSP - Exemplo

<jsp: useBean id="user" scope="session" type="org.apache.struts"/>

Conforme vimos em aula, trata-se da penúltima opção. Gabarito: D

18.(FCC - 2012 - MPE-PE - Analista Ministerial - Informática) Em uma aplicação web
Java que utiliza JSP, as linhas de código comuns a diversas páginas podem ser criadas em um arquivo
..I.., que pode ser incluído nas páginas utilizando-se a diretiva ..II...

As lacunas I e II são preenchidas correta e respectivamente por a) I. Javascript, <%@page
II. file="caminho/nome_do_arquivo"%>.

b) I. Java Servlet, <%@include

II. uri="caminho/nome_do_arquivo"%>.

c) I. JSTL, <%@taglib

II. uri="caminho/nome_do_arquivo"%>.

d) I. JSF, <%@page

,

II. import="caminho/nome_do_arquivo%>.

e) I. JSPF, <%@include

II. file="caminho/nome_do_arquivo"%>.

Comentários:

0 include - inclui recursos estáticos em uma Página JSP.

//Diretiva INCLUDE

<%@ include file = "teste.jsp" %>

Professor, que raios é esse JSPF? Cara, não se assuste! É apenas o nome dado a um fragmento deJSP que é inserido em outro JSP. E que diretiva pode ser utilizada para inserir um recurso em umaPágina JSP? @include. Gabarito: E

19.(FCC - 2012 - MPE-PE - Analista - Tecnologia da Informação) Em uma página JSP,
para importar uma classe de um pacote e para fazer referência a uma biblioteca (como, por exemplo,JSTL)
podem ser utilizadas, respectivamente, as diretivas:

a) <%@page import="pacote.Classe"%> e <%@taglib uri="caminho/biblioteca"prefix="prefixo"%>.

b) <%@include import= "pacote.Classe"%> e <%@taglib uri="caminho/biblioteca"%>.

c) <%import= "pacote.Classe"%> e <%taglib uri="caminho/biblioteca"%>.

d) <%@page include= "pacote.Classe"%> e <%@library uri="caminho/biblioteca"%>.

e) <%@import class= "pacote.Classe"%> e <%@taglib urli="caminho/biblioteca"%>.

Comentários:

0 page - define atributos de configuração da Página JSP.

ATRIBUTO PROPÓSITO

buffer Especifica o modelo de buffering da saída padrão.

autoFlush Controla o comportamento da saída padrão da Servlet.
contentType Define a codificação de caracteres e media type (MIME)
errorPage Define a URL de outro JSP que reporta exceções.
isErrorPage Indica se a Página JSP possui URL de outra página.

Extends Especifica uma superclasse a ser estendida pela servlet.
Import Especifica uma lista de pacotes ou classes importadas.

Info Define uma string que pode ser acessada para informações.
isThreadSafe Define se a servlet é capaz de atender múltiplas solicitações.
language Define a linguagem de programação utilizada.

Session Especifica se a Página JSP participa de Sessões HTTP.
isELIgnored Especifica se Linguagens de Expressão serão ignoradas.
isScriptingEnabled Determina se elementos de script são permitidos.

0 taglib - estende o conjunto de tags através de uma biblioteca de tags.

Conforme vimos em aula, podemos usar a Diretiva page com o Atributo import e a
Diretiva taglib.
Gabarito: A

2O.(FCC - 2012 -TRE-CE - Analista Judiciário - Análise de Sistemas) <%@ page atributo1
= "valor1"
atributo2="valor2"... %> é a sintaxe típica da diretiva Page, em JSP. Um de seus atributos, se definido para true, indica o processamento normal do servlet quando múltiplas requisições podem ser acessadas simultaneamente na mesma instância de servlet. Trata-se do atributo:
a) Extends.

b) Import.

c) isThreadSafe.

d) Session.

e) AutoFIush.

Comentários:

ATRIBUTO PROPÓSITO

buffer Especifica o modelo de buffering da saída padrão.
autoFlush Controla o comportamento da saída padrão da Servlet.
contentType Define a codificação de caracteres e media type (MIME)
errorPage Define a URL de outro JSP que reporta exceções.
isErrorPage Indica se a Página JSP possui URL de outra página.

Extends Especifica uma superclasse a ser estendida pela servlet.
Import Especifica uma lista de pacotes ou classes importadas.

Info Define uma string que pode ser acessada para informações.
isThreadSafe Define se a servlet é capaz de atender múltiplas solicitações.
language Define a linguagem de programação utilizada.

Session Especifica se a Página JSP participa de Sessões HTTP.
isELIgnored Especifica se Linguagens de Expressão serão ignoradas.
isScriptingEnabled Determina se elementos de script são permitidos.

Conforme vimos em aula, trata-se do atributo isThreadSafe. Gabarito: C

21 .(FCC - 2008 - MPE-RS - Técnico em Informática - Área Sistemas) Se uma super classe de servlet deve ser gerada, será definida na diretiva page do JSP por meio do atributo:
a) info.

/ 235

/

b) extends.

c) session.

d) import.

e) autoFIush.

Comentários:

ATRIBUTO PROPÓSITO

buffer Especifica o modelo de buffering da saída padrão.
autoFIush Controla o comportamento da saída padrão da Servlet.
contentType Define a codificação de caracteres e media type (MIME)
errorPage Define a URL de outro JSP que reporta exceções.
isErrorPage Indica se a Página JSP possui URL de outra página.

Extends Especifica uma superclasse a ser estendida pela servlet.
Import Especifica uma lista de pacotes ou classes importadas.

Info Define uma string que pode ser acessada para informações.
isThreadSafe Define se a servlet é capaz de atender múltiplas solicitações.
language Define a linguagem de programação utilizada.

Session Especifica se a Página JSP participa de Sessões HTTP.
isELIgnored Especifica se Linguagens de Expressão serão ignoradas.
isScriptingEnabled Determina se elementos de script são permitidos.

Conforme vimos em aula, trata-se do Atributo Extends.

Gabarito: B

22.(FGV - 2008 - Senado Federal - Analista de Sistemas) No contexto do Desenvolvimento
WEB
JAVA, analise as afirmativas a seguir, a respeito da tecnologia JSP ("JavaServer Page"):

I. Disponibiliza uma tecnologia simples e rápida para criar páginas que exibem conteúdo gerado dinamicamente, define a interação entre o servidor e a página JSP, e descreve o formato e sintaxe da página.
II. Emprega servlets - programas escritos na linguagem Java e executados no servidor,
em oposição aos applets, executados no browser do cliente.
III. Utiliza páginas JSP, com extensão .jsp ou .jspx, criadas pelo desenvolvedor da web e que incluem especificações JSP e tags customizadas, em combinação com outras tags estáticas,HTML ou XML.

Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente as afirmativas I e II estiverem corretas.

c) se somente as afirmativas I e III estiverem corretas.

d) se somente as afirmativas II e III estiverem corretas.

e) se todas as afirmativas estiverem corretas.

Comentários:

I. Em suma: JSP é uma linguagem de script server-side com especificação aberta cujo principal objetivo é a geração simples, prática e rápida de conteúdo dinâmico para páginas web.É uma tecnologia que possui o suporte de vários servidores, tais como: Tomcat, GlassFish,JBoss, entre outros. Ela define a interação entre Servidor e Página JSP, e descreve o formato e sintaxe da página. Vamos ver como tudo funciona?
Foi considerada errada. Eu discordo do gabarito, assim como a Documentação oficial da
Oracle,
que ratifica o que foi dito em aula.

II.Professor, como funciona esse tal de JSP? Cara, Páginas JSP utilizam tags XML e
Scriplets escritos em Java para encapsular a lógica que gera o conteúdo para a página web. Ele separa a lógica do conteúdo da sua apresentação. Páginas JSP são compiladas emServlets e podem

/ 235

/

chamar beans a fim de executar o processamento no servidor. Espera, professor! Como assim são compiladas em Servlets?
Perfeito, empregam Servlets (executadas no Servidor) em oposição às Applets
(executadas no cliente).
III. Galera, esses códigos são semelhantes: o primeiro é uma Página JSP (Arquivo .jsp ou .jspx) e o segundo é uma Servlet (Arquivo .java). Vocês percebem que no primeiro código nós temos códigoHTML com algumas coisas de Java? Já no segundo nós temos Java com algumas coisas de
HTML?
Vejam como é chato escrever o segundo código - é preciso colocar as tags HTML dentro das funções de escrita do Java.
Galera, trata-se de uma tecnologia para geração de documentos baseados em texto e executados do lado do servidor (assim como Servlets). Professor, como assim texto? Esse texto pode ser um conjunto de dados estáticos (Ex: HTML e XML); ou pode ser um conjunto de elementosJSP e tags customizadas, que definem como a página construirá conteúdo dinâmico.
Conforme visto em aula, está perfeito. Gabarito: D

23.(CESGRANRIO - 2010 - BNDES - Analista de Sistemas) É característica de um arquivo JSP a:

a) compilação em um servlet.

b) presença maciça de código Assembly.

c) impossibilidade de inclusão de comentários.

d) execução exclusiva em sistemas Windows.

e) execução exclusiva em sistemas Linux.

Comentários:

Professor, como funciona esse tal de JSP? Cara, Páginas JSP utilizam tags XML e
Scriplets escritos em Java para encapsular a lógica que gera o conteúdo para a página web. Ele separa a lógica do conteúdo da sua apresentação. Páginas JSP são compiladas em Servlets e podem chamar beans a fim de executar o processamento no servidor. Espera, professor! Como assim são compiladas em Servlets?
Conforme vimos em aula, Páginas JSP são compiladas em Servlets. Gabarito: A

/ 235

/

24.(NCE - 2005 - BNDES - Analista de Sistemas) Considere as seguintes afirmativas sobre JSP e
Servlets:

I. É possível usar uma página JSP para gerar um arquivo de imagem do tipo JPEG, GIF ou PNG.

II. Um servlet é executado no servidor, ao passo que uma página JSP é executada no browser do cliente.
III. Uma página gerada por um servlet não pode conter código Javascript.

IV. Uma página JSP é executada no servidor enquanto que um servlet é executado no browser do cliente.
A quantidade de afirmativas corretas é:

a) 0;

b) 1;

c) 2;

d) 3;

e) 4.

Comentários:

ATRIBUTO PROPÓSITO

buffer Especifica o modelo de buffering da saída padrão.
autoFlush Controla o comportamento da saída padrão da Servlet.
contentType Define a codificação de caracteres e media type (MIME)
errorPage Define a URL de outro JSP que reporta exceções.
isErrorPage Indica se a Página JSP possui URL de outra página.

Extends Especifica uma superclasse a ser estendida pela servlet.

,

Import Especifica uma lista de pacotes ou classes importadas.

Info Define uma string que pode ser acessada para informações.
isThreadSafe Define se a servlet é capaz de atender múltiplas solicitações.
language Define a linguagem de programação utilizada.

Session Especifica se a Página JSP participa de Sessões HTTP.
isELIgnored Especifica se Linguagens de Expressão serão ignoradas.
isScriptingEnabled Determina se elementos de script são permitidos.

I. Conforme visto em aula, o atributo contentType da Diretiva Page permite definir a codificação dos caracteres e o Media Type (Ex: text/plain, image/jpeg, vídeo/mp4). Logo, é possível sim usar uma Página JSP para gerar um arquivo de imagem do tipo JPEG, GIF ou PNG.
Galera, trata-se de uma tecnologia para geração de documentos baseados em texto e executados do lado do servidor (assim como Servlets). Professor, como assim texto? Esse texto pode ser um conjunto de dados estáticos (Ex: HTML e XML); ou pode ser um conjunto de elementosJSP e tags customizadas, que definem como a página construirá conteúdo dinâmico.
II. Conforme visto em aula, ambos são executados no Servidor.

III. Não existe isso! JavaScript roda no browser do cliente, logo é completamente possível ter código JavaScript em uma Página JSP.
Galera, trata-se de uma tecnologia para geração de documentos baseados em texto e executados do lado do servidor (assim como Servlets). Professor, como assim texto? Esse texto pode ser um conjunto de dados estáticos (Ex: HTML e XML); ou pode ser um conjunto de elementosJSP e tags customizadas, que definem como a página construirá conteúdo dinâmico.
IV. Conforme visto em aula, ambos são executados no Servidor.

Gabarito: B

x'

/ 235

/

25.(CESGRANRIO - 2012 - CEF-Analista de Sistemas) Um objeto implícito é utilizado dentro de páginas JSP sem que haja necessidade de declará-lo. Que objeto é esse?
a) Integer.

b) queryString.

c) getParameter.

d) String.

e) Request.

Comentários:

OBJETO DESCRIÇÃO

request Objeto do tipo HttpServIetRequest e contém a informação do pedido HTTP.
response Objeto do tipo HttpServIetResponse e contém a resposta HTTP
que vai ser enviada ao cliente. Não é usado com frequência.

pageContext Objeto do tipo PageContext e contém informações de contexto para execução da página.
application Objeto do tipo ServIetContext que permite compartilhar informações entre todos os componentes web da aplicação.
out Objeto da classe JspWriter que permite imprimir para o response através do método println.
config Objeto do tipo ServIetConfig da página JSP.

page Sinônimo do operador "this" do objeto HttpJspPage. Não é usado com frequência.
,

session Objeto do tipo HttpSession que guarda informações da sessão de um usuário específico entre múltiplas requisições.
exception É o objeto Throwable que é resultante de uma situação de erro numa página JSP.
Conforme vimos em aula, trata-se do Objeto Request. Gabarito: E

26.(FMP-RS - 2013 - MPE-AC - Analista - Tecnologia da Informação) No contexto de arquiteturaJava Enterprise Edition,é uma tecnologia que simplifica o processo de gerar páginas dinamicamente, pois permite embutir Java diretamente em uma página HTMLou XML

Assinale a única alternativa que completa corretamente a lacuna acima:

a) Java Virtual Machine (JVM)

b) JavaServer Pages (JSP)

c) Java ME (Java Micro Edition)

d) Enterprise JavaBeans (EJB)

e) Java Persistence API (JPA)

Comentários:

Primeiro, o que é JSP? É uma tecnologia da plataforma Java Enterprise Edition (Java
EE) que permite utilizar ou o código Java dentro das páginas web ou tags que realizam sua lógica. Por ser tecnologia Java, seus objetos são definidos segundo define a linguagem, i.e.,podendo utilizar todos os seus recursos, tais como modificadores de acesso, tratamento de exceções, entre outros.
Conforme vimos em aula, trata-se do JSP! Gabarito: B

27.(CESGRANRIO - 2011 - FINEP - Analista - Desenvolvimento de Sistemas) Qual ação padrão do
JSP interrompe o processamento das requisições pela página corrente e as direciona para outro componente Web?
/ 235

/

a) <jsp:invoke>

b) <jsp:include>

c) <jsp:forward>

d) <jsp:plugin>

e) <jsp:call>

Comentários:

JSP:USEBEAN jsp:param jsp:invoque jsp:output
JSP:SETPRoPERTY jsp:fallback jsp:doBody jsp:root

JSPIGETPRoPERTY jsp:text jsp:elemento jsp:declaration
JSPJNCLUDE jsp:plugin jsp:body jsp:scriptlet
JSPlFORWARD jsp:params jsp:attribute jsp:expression
Essas ações ajudam a controlar o comportamento da Engine da Servlet. As ações mais famosas e conhecidas são: (...)
* jspdorward: usada para redirecionar requisições para outra Página JSP;
Conforme vimos em aula, trata-se do jspdorward. Gabarito: C

28.(ESAF - 2009 - ANA - Analista Administrativo - Tecnologia da Informação -
Desenvolvimento)
O mecanismo de inclusão, que permite o conteúdo dinâmico ser incluído em uma JSP em tempo de solicitação, é denominado:
a) Ação <jsp:plugin>.

b) Ação <jsp:include>.

c) Diretiva include.

d) Diretiva Page.

e) Diretiva taglib.

/ 235

/

Comentários:

JSP:USEBEAN jsp:param jsp:invoque jsp:output
JSP:SETPRoPERTY jsp:fallback jsp:doBody jsp:root

JSP:GETPRoPERTY jsp:text jsp:elemento jsp:declaration
JSPlINCLUDE jsp:plugin jsp:body jsp:scriptlet
JSP:FoRwARD jsp:params jsp:attribute jsp:expression
Essas ações ajudam a controlar o comportamento da Engine da Servlet. As ações mais famosas e conhecidas são: (...)
* jsp:include: usada para inserir conteúdo dinâmico em tempo de solicitação;

Conforme vimos em aula, trata-se da Ação jsp:include. Gabarito: B

QQ SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital)

LISTA DE QUESTõES - JSP - CEBRASPE

1. (CESPE - 2013 - CNJ - Analista de Sistemas) Como forma de incluir dinamismo em páginasJSP, é possível incluir blocos de código Java conhecidos como scriptlets.

2. (CESPE - 2011 - PREVIC - Analista de Sistemas) O container JSP provê uma lista de objetos instanciados, chamados de objetos implícitos. É através do objeto aplicação (application object) que são rastreadas as informações de um cliente específico entre múltiplas requisições.
3. (CESPE - 2013 - TRT/10 - Analista de Sistemas) Nas páginas JSP, combinam-se modelos estáticos, incluindo fragmentos de HTML ou XML, com o código para gerar conteúdo dinâmico e compilar páginas JSP dinamicamente em servlets, quando solicitado.
4. (CESPE - 2013 - TRT/10 - Analista de Sistemas) O JSP, cuja base é a linguagem de programação Java, tem portabilidade de plataforma, o que o permite ser executado em diversos sistemas operacionais, como o Windows e o Linux.
5. (CESPE - 2013 - TRT/10 - Analista de Sistemas) Para usar o JSP com Java embutido e algumas tags de marcação complexas, o programador tem de conhecer a fundo as complexidades do desenvolvimento de aplicações.
6. (CESPE - 2013 - SERPRO - Analista - Suporte Técnico) Um scriptlet na tecnologia
JSP (Java server pages) abrange todo o código entre "<#" e "#>".
7. (CESPE - 2011 - CBM-DF - Oficial Bombeiro Militar Complementar - Informática) O
uso de
Javabeans, o controle de transferência entre as páginas e o suporte independente de applets
Java pelos browsers são possibilidades proporcionadas pela action tag da JSP.

8. (CESPE - 2011 - PREVIC - Analista de Tecnologia da Informação) Em uma aplicação multicamadas na plataforma Java EE, servlets, JavaServer Faces e JSP consistem em tecnologias utilizadas na camada web.
9. (CESPE - 2017 - TRE/BA - Analista de Sistemas) A respeito da JSP (JavaServer Pages), assinale a opção correta.
a) As páginas JSP compiladas não precisam ser executadas em uma máquina virtual Java (JVM).

b) O scriptlet é o conteúdo integral de um trecho de código Java que esteja dentro das tags

<script>código< /script>.

c) O comando <c:out value="conteúdo"/> avalia uma expressão e insere o seu resultado na saída,

podendo o conteúdo do atributo value ser dinâmico como um texto literal ou uma expressão escrita.
d) O método POST do HTML não pode ser utilizado para enviar ou receber dados.

e) Uma página criada com a tecnologia JSP, depois de instalada em um servidor de aplicação compatível, estará pronta para ser executada, não havendo a necessidade de ela ser transformada em um Servlet.
,

GABARITo

GABARITO

1. c

2. E

3. C

4. C

5. E

6. E

7. C

8. C

9. C

,

LISTA DE QUESTõES -JSP - MULTIBANCAS

1. (FCC - 2012 - TRE-SP - Técnico Judiciário - Programação de Sistemas) As tags utilizadas em uma página JSP para importar classes de um pacote, habilitar o uso de bibliotecas de classes(por exemplo, JSTL) e incluir arquivos (por exemplo, JSP Fragments) são conhecidas como tags:
a) diretivas.

b) de scriptlet.

c) de declaração.

d) de expressão.

e) standard action.

2. (FCC - 2009 - PGE-RJ - Técnico Superior de Análise de Sistemas e Métodos) Blocos ou trechos de operações em código Java podem ser incluídos em uma página JSP por meio de:
a) diretiva page.

b) diretiva include.

c) comentário.

d) taglib.

e) scriptlet.

3. (FCC - 2010 - TRT - 20a REGIÃO (SE) - Técnico Judiciário - Tecnologia da
Informação) Na diretiva page, do JSP, podemos utilizar o atributo import que permite:
a) configurar arquivos html.

b) importar figuras.

c) configurar pacotes.

d) importar arquivos htm e) importar pacotes.
,

4. (FCC - 2009 - TRT -16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da Informação) Em JSP,
a diretiva taglib define:

a) uma biblioteca de tags para serem usadas na página.

b) um conjunto de classes importadas para serem usadas na página.

c) uma nova tag para ser usada na página.

d) uma biblioteca para ser inserida na página.

e) um módulo logicamente coesivo.

5. (FCC - 2008 - MPE-RS - Técnico em Informática - Área Sistemas) Para incluir blocos de código
Java em uma página JSP utiliza-se a categoria de tags denominada:

a) diretivas.

b) expressões.

c) declarações.

d) scriptlets.

e) comentários.

6. (FCC - 2010 - METRÔ-SP - Analista - Tecnologia da Informação) Na diretiva page, do JSP,
utiliza-se o atributo import, que permite:

a) configurar pacotes.

b) importar arquivos html.

c) importar pacotes.

d) configurar arquivos html.

e) importar figuras.

7. (FCC - 2012 - TRE-SP - Técnico Judiciário - Programação de Sistemas) No JavaServer Pages a tag <%=conteúdo %> é uma:
a) Declaration tag.

b) Directive tag.

c) Scriplet tag.

d) Action tag.

e) Expression tag.

8. (FCC - 2011 - TRE/AP - Analista de Sistemas - A) Em JSP o conceito de classes e objetos não leva em conta os princípios de proteção de dados tanto nas propriedades quanto nos métodos.
9. (FCC - 2011 - TRE/AP - Analista de Sistemas - C) Em JSP pode-se chamar o construtor do objeto pai em qualquer parte do código e não há tratamento de exceções nos métodos nativos.
10. (FCC - 2010 - MPU - Analista de Sistemas) O contêiner, que executa JSP,
transforma o programa JSP em Servlet, assim, a expressão "<%= Math.Random()%>" se torna argumento para out.printlnQ.
11 .(FCC - 2011 - TRE/AP - Analista de Sistemas - A) Para que métodos estáticos de classes Java sejam executados a partir das funções da linguagem de expressão em JSP, é necessário que o nome da função coincida com o nome do método da classe Java.
12. (FCC - 2009 - TCE/SP - Analista de Sistemas ) Quando se usa classes do tipo bean, não é necessário instanciar explicitamente um objeto da classe para poder acessar seus métodos. Ainstância do objeto é criada pelo elemento especial:

a) <jsp:useJavaBean/>

b) <jsp:useJava/>

c) <jsp:useBean.Java/>

d) <jsp:useJava.Bean/>

e) <jsp:useBean/>

13. (FCC - 2008 - TCE/SP - Analista de Sistema) Nas páginas dinâmicas escritas em
JSP, para declaração de atributos ou métodos, utilizam-se as tags:
a) <% %>

b) <%! %>

/ 235

/

c) <%= %>

d) <%- -%>

e) /* */

14. (FCC - 2012 - TST - Analista de Sistemas) Páginas JavaServer Pages são páginas web:

a) que permitem combinar códigos Java, HTML estático, CSS, XML e JavaScript.

b) escritas em Java, sem código HTML.

c) Interpretadas e não compiladas.

d) Transformadas em bytecode e executadas no cliente.

e) Combinadas com servlets no desenvolvimento exclusivo de páginas estáticas.

15. (FCC - 2009 - TRT/3 - Analista de Sistemas) NÃO possui uma habilidade de armazenar e recuperar valores de atributos arbitrários o objeto implícito de JSP:
a) Session.

b) Request.

c) Exception.

d) Application.

e) pageContext.

16. (FCC - 2007 - TRF/4 - Analista de Sistemas) Uma ferramenta usada especificamente para gerar páginas dinâmicas de HTML, baseada em programação Java, é:
a) o WSDL.

b) o DTD.

c) a JCP.

d) a XSL.

e) o JSP.

17. (FCC - 2013 - ALERN - Analista de Sistemas) Em uma aplicação web desenvolvida utilizando a plataforma Java EE 6, há a seguinte classe Java:
,

package dados;

public class Cliente {
private String nome;
public ClienteO {

}

public String getNome() {
return nome;

}

public void setNome(String nome) {
this.nome = nome;

}

}

Em uma página JSP da mesma aplicação, para instanciar um objeto desta classe pode-se utilizar a tag:
a) <jsp:setBean name="cliente" class="dados.Cliente"/>

b) <jsp:setBean id="cliente" class="dados.Cliente"/>

c) <jsp:useBean name="cliente" class="dados.Cliente"/>

d) <jsp:useBean id="cliente" class="dados.Cliente"/>

e) <jsp:newlnstance id="cliente" class= "dados.Cliente"/>

18.(FCC - 2012 - MPE-PE - Analista Ministerial - Informática) Em uma aplicação web
Java que utiliza JSP, as linhas de código comuns a diversas páginas podem ser criadas em um arquivo
..I.., que pode ser incluído nas páginas utilizando-se a diretiva ..II.. .

As lacunas I e II são preenchidas correta e respectiva mente por a) I. Javascript, <%@page
II. file="caminho/nome_do_arquivo"%>.

/ 235

/

b) I. Java Servlet, <%@include

II. uri="caminho/nome_do_arquivo"%>.

c) I. JSTL, <%@taglib

II. uri="caminho/nome_do_arquivo"%>.

d) I. JSF, <%@page

II. import="caminho/nome_do_arquivo%>.

e) I. JSPF, <%@include

II. file="caminho/nome_do_arquivo"%>.

19.(FCC - 2012 - MPE-PE - Analista - Tecnologia da Informação) Em uma página JSP, para importar uma classe de um pacote e para fazer referência a uma biblioteca (como, por exemplo, JSTL)podem ser utilizadas, respectivamente, as diretivas:

a) <%@page import="pacote.Classe"%>e<%@taglib uri="caminho/biblioteca"prefix="prefixo"%>.

b) <%@include import= "pacote.Classe"%> e <%@taglib uri="caminho/biblioteca"%>.

c) <%import= "pacote.Classe"%> e <%taglib uri="caminho/biblioteca"%>.

d) <%@page include= "pacote.Classe"%> e <%@library uri="caminho/biblioteca"%>.

e) <%@import class= "pacote.Classe"%> e <%@taglib urli="caminho/biblioteca"%>.

20. (FCC - 2012 - TRE-CE - Analista Judiciário - Análise de Sistemas) <%@ page atributol =
"valorl"
atributo2="valor2"... %> é a sintaxe típica da diretiva Page, em JSP. Um de seus atributos, se definido para true, indica o processamento normal do servlet quando múltiplas requisições podem ser acessadas simultaneamente na mesma instância de servlet. Trata-se do atributo:
a) Extends.

b) Import.

c) isThreadSafe.

d) Session.

e) AutoFIush.

21 .(FCC - 2008 - MPE-RS - Técnico em Informática - Área Sistemas) Se uma super classe de servlet deve ser gerada, será definida na diretiva page do JSP por meio do atributo:
a) info.

b) extends.

c) session.

d) import.

e) autoFIush.

22.(FGV - 2008 - Senado Federal - Analista de Sistemas) No contexto do Desenvolvimento
WEB
JAVA, analise as afirmativas a seguir, a respeito da tecnologia JSP ("JavaServer Page"):

I. Disponibiliza uma tecnologia simples e rápida para criar páginas que exibem conteúdo gerado dinamicamente, define a interação entre o servidor e a página JSP, e descreve o formato e sintaxe da página.
II. Emprega servlets - programas escritos na linguagem Java e executados no servidor,
em oposição aos applets, executados no browser do cliente.
III. Utiliza páginas JSP, com extensão .jsp ou .jspx, criadas pelo desenvolvedor da web e que incluem especificações JSP e tags customizadas, em combinação com outras tags estáticas,HTML ou XML.

Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente as afirmativas I e II estiverem corretas.

c) se somente as afirmativas I e III estiverem corretas.

d) se somente as afirmativas II e III estiverem corretas.

e) se todas as afirmativas estiverem corretas.

23.(CESGRANRIO - 2010 - BNDES - Analista de Sistemas) É característica de um arquivo JSP a:

a) compilação em um servlet.

b) presença maciça de código Assembly.

/ 235

/

c) impossibilidade de inclusão de comentários.

d) execução exclusiva em sistemas Windows.

e) execução exclusiva em sistemas Linux.

24.(NCE - 2005 - BNDES - Analista de Sistemas) Considere as seguintes afirmativas sobre JSP e
Servlets:

I. É possível usar uma página JSP para gerar um arquivo de imagem do tipo JPEG, GIF ou PNG.

II. Um servlet é executado no servidor, ao passo que uma página JSP é executada no browser do cliente.
III. Uma página gerada por um servlet não pode conter código Javascript.

IV. Uma página JSP é executada no servidor enquanto que um servlet é executado no browser do cliente.
A quantidade de afirmativas corretas é:

a) 0;

b) 1;

c) 2;

d) 3;

e) 4.

25.(CESGRANRIO - 2012 - CEF - Analista de Sistemas) Um objeto implícito é utilizado dentro de páginas JSP sem que haja necessidade de declará-lo. Que objeto é esse?
a) Integer.

b) queryString.

c) getParameter.

d) String.

e) Request.

/ 235

/

26.(FMP-RS - 2013 - MPE-AC - Analista - Tecnologia da Informação) No contexto de arquiteturaJava Enterprise Edition,é uma tecnologia que simplifica o processo de gerar páginas dinamicamente, pois permite embutir Java diretamente em uma página HTMLou XML

Assinale a única alternativa que completa corretamente a lacuna acima:

a) Java Virtual Machine (JVM)

b) JavaServer Pages (JSP)

c) Java ME (Java Micro Edition)

d) Enterprise JavaBeans (EJB)

e) Java Persistence API (JPA)

27.(CESGRANRIO - 2011 - FINEP - Analista - Desenvolvimento de Sistemas) Qual ação padrão do
JSP interrompe o processamento das requisições pela página corrente e as direciona para outro componente Web?
a) <jsp:invoke>

b) <jsp:include>

c) <jsp:forward>

d) <jsp:plugin>

e) <jsp:call>

28.(ESAF - 2009 - ANA - Analista Administrativo - Tecnologia da Informação -
Desenvolvimento)
O mecanismo de inclusão, que permite o conteúdo dinâmico ser incluído em uma JSP em tempo de solicitação, é denominado:
a) Ação <jsp:plugin>.

b) Ação <jsp:include>.

c) Diretiva include.

d) Diretiva Page.

e) Diretiva taglib.

/ 235

/

GABARITo

GABARITO

1. A 8. E
15. C 22. D

2. E 9. E
16. E 23. A

3. E 10. C
17. D 24. B

4. A 11. E
18. E 25. E

5. D 12. E
19. A 26. B

6. C 13. B
20. C 27. C

7. E 14. A
21. B 28. B

SERVLETS

Pessoal, lá no Contêiner Web, há uma tal de Servlet! O que é isso,
professor? É uma API
independente de plataforma, escrita em Java, que roda no servidor
(Container Web)
processando requisições de clientes e enviando respostas, e que pode ser traduzida como'servidorzinho'. Como é? É isso mesmo! Porque ele é utilizado para estender as funcionalidades de um servidor.
A documentação oficial afirma que se trata de uma classe java pura utilizada para estender as capacidades dos servidores que hospedam aplicações acessadas por meio de um modelo de requisição-resposta. Em geral, elas funcionam para fornecer conteúdo web dinâmicos(normalmente em HTML) às páginas web, processando requisições/respostas, filtrando dados,acessando o banco de dados, etc.

Vocês podem me perguntar se as servlets utilizam apenas HTTP. Não! Elas utilizam qualquer protocolo, no entanto ele é o protocolo mais utilizado por clientes web. Professor, o que você quis dizer com "classe java pura"? Cara, isso significa que essa classe só contém código java. Professor as servlets rodam no cliente ou no servidor? Pô... essa é muito fácil: Servlets rodam no Servidor(JVM)!* 1 ;)

— MENU Q TIMES
globoesporte.com Q BUSCAR

OLHA

AL-AHLI FAMINTO

Interesse de clube árabe complica a renovação de Guerrero com o Timão
* Mano Menezes não descarta dirigir o Palmeiras

Depois da decepção nos 50m, Cielo quer recompensa: "Mais dois pódios"
* Cielo perde para algoz francês e leva o bronze

Bem, acima eu afirmei que as servlets são responsáveis por fornecer conteúdo web dinâmicos. Eaí, alguém sabe o que é uma página web dinâmica? Bem, nós temos dois tipos de página web dinâmicas: client-side e server-side. O primeiro se refere a páginas que permitem mudanças em sua interface como resposta a ações do mouse, teclado, entre outros. Vejam o exemplo da imagem anterior!
1 Oracle afirma: "A servlet can almost be thought of as an applet that runs on the server side".

* 05152001900 - Everton
Murilo Vieira

Q TIMES globoesporte.com
Q BUSCAR

princípios editoriais grupo globo futebol mma f1
eu atleta

+ esportes seu estado tv brasileirãoSporTV
cartola fc

FUTEBOL

brasileirão série a estatísticas brasileirão série b mundial de clubes copa sul-americana estaduais e regionais >tabelas de a a z cartola fc vai e vem do mercado futebol internacional >seleção brasileira troféu armando nogueira artilheiro do ano futpédia
SÉRIE A SÉRIE B

times de A aZ»

interesse ae auDe araDe compnca a renovação de Guerrero com o Timão
* Mano Menezes não descarta dirigir o Palmeiras uepuis da decepção nos 50m, Cielo quer recompensa: "Mais dois pódios"
* Cielo perde para algoz francês e leva o bronze agora observem que a página acima é modificada quando se move o cursor do mouse sobre o link"menu" - ela é dinâmica! Bem, mas nosso interesse nessa aula são as páginas web dinâmicas server-side, i.e., que variam de acordo com os parâmetros fornecidos por um usuário/programa com o intuito de aumentar o potencial de comunicação e interação com cada usuário especificamente.
Antigamente, para gerar conteúdo dinâmico, utilizava-se o CGI (Common Gateway Interface)
- ele permitia escrever pequenos programas para apresentar páginas web dinâmicas utilizando outras linguagens de programação. Em 1997, apareceu a tecnologia de servlets, que são utilizadas para gerar páginas web dinâmicas por meio da linguagem Java. Professor, deixa eu ver uma servlet?Vamos lá:

import java.io.*;
import java.text.*;
import java.util.*;
import javax.servlet.*;

import javax.servlet.http.*;

public class ServIetTeste extends HttpServIet

{

public void doGet(HttpServletRequest req, HttpServIetResponse res)
throws lOException, ServIetException {

res.setContentType("text/html");
PrintWriter out = res.getWriter();

out.println("<html>");

* 05152001900 - Everton
Murilo Vieira out.println("<body bgcolor = \"white\">");out.println("<h1 >Hello Servlet</h1 >");
out.println(" </body>");
out.println("</html>");

}

}

Dado esse código, vamos ver alguns detalhes importantes: primeiro, foi importado o pacote javax.servlet, que é um conjunto de classes e interfaces responsáveis pela comunicação com diversos protocolos - lá se encontram, por exemplo, as interfacesServIetRequest e
ServIetResponse. No entanto, observem abaixo que se importa também o pacote javax.servlet.http - cuja estrutura é mostrada a seguir:
Ele se trata de um conjunto de classes e interfaces responsáveis pela comunicação especificamente com o protocolo HTTP - lá se encontram as interfaces HttpServIetRequest eHttpServIetResponse,
e também uma classe abstrata chamada HttpServIet2. Essa classe define diversos métodos para lidar com Requisições HTTP: doGet, doPost, doPut, doDelete, doHead, doTrace e doOptions, etc.
Dentro da javax.servlet, temos também a interface ServIetContext! Ela define um contexto, i.e.,uma unidade de aplicação web que possui suas próprias configurações. Para executar
Servlets e
Páginas JSP, é necessário colocá-los dentro de um contexto de uma aplicação web -
existe um
Contexto por Aplicação Web por JVM. Entenderam mais ou menos? É simples, só é um pouco abstrato!
A interface ServIetContext é um conjunto de métodos que uma servlet utiliza para interagir com seu Servlet Container - por exemplo, para recuperar um arquivo, despachar requisições ou escrever em um arquivo de log! Bem, conforme a imagem abaixo, cada servlet possui seuServIetConfig. Já o ServIetContext serve para qualquer servlet do contexto e pode ser acessado por meio do objeto ServIetConfig.
2 Seu nome completo é: javax.servlet.http.HttpServIet.

,

Voltando ao nosso código: importamos os dois pacotes, estendemos essa classe abstrata e passamos como parâmetro as duas interfaces. Se a Requisição HTTP foi feita utilizando o MétodoGET, executaremos o método doGet; se foi com o Método POST, executaremos o método doPost. Esses métodos recebem dois parâmetros: uma requisição HttpServIetRequest e uma resposta HttpServIetResponse.
Vocês observarão um padrão muito comum em servlets. Qual, professor? Para devolver a resposta ao cliente, devemos primeiro definir o tipo de saída. Para tal, utilizamos a função setContentType do HttpServIetResponse - nossa servlet definiu como text/html, i.e., teremos uma saída em HTML!A seguir, utilizamos o método getWriter para capturar os caracteres da resposta e inseri-los em um objeto out.
Após isso, nós já podemos utilizar o método println do objeto out para escrever a saída, resultando em uma Página HTML "Hello Servlet" - como é apresentado na imagem abaixo. Qualé,professor?
O que tem de dinâmico aí? Isso foi só um exemplo para vocês verem como é possível receber dados de entrada do usuário e manipulá-los dinamicamente.
O único objetivo da servlet acima é exibir uma mensagem HTML simples para os usuários que a requisitarem. No entanto, note como seria muito fácil escrever outros códigos Java mais poderosos para gerar as strings do HTML baseadas em informações dinâmicas vindas, por exemplo, de um banco de dados. Vocês entenderam direitinho?
/ 235

/

sin
CFlA OBJeftÇ

\Y A *=;1 Kl A

É importante entender também como funciona um dos métodos mais importantes da interfaceHttpServIetRequest: método getParameter3! Bem, ele retorna o valor do parâmetro de uma requisição como uma String; E por que é importante? Porque ele é útil na passagem de dados de um formulário do cliente, i.e., por meio dele, a servlet pode capturar dados de formulários! Agora vamos ver o ciclo das servlets ;)
Conforme a imagem acima, o Servidor recebe uma Requisição HTTP e a repassa para o
Servlet
Container. Já existe uma instância4 da servlet capaz de responder a essa requisição? Se sim,delega-se a requisição para essa instância; se não, carrega-se a classe servlet na memória, cria-se uma instância dela e a inicializa por meio do método init. Esse método recebe como parâmetro um objeto ServIetConfig!
Esse objeto contém informações de configuração e parâmetros de inicialização da aplicação web.A partir do momento que a servlet é inicializada, o contêiner pode utilizá-la para tratar requisições dos clientes. Chama-se então o método service com dois parâmetros:ServIetRequest, que contém a solicitação do cliente; e o ServIetResponse, que contém a resposta - ambos criados pelo contêiner.
Na prática, o método service determina qual Método HTTP (GET/POST) deve ser chamado na servlet. Por fim, o contêiner chama o método destroy a fim de remover a instância da servlet da memória e liberar os recursos e os dados. Tanto o método init quanto o método destroy são executados apenas uma vez durante o ciclo de vida da servlet. Professor, quem gerencia tudo nisso? O Servlet Container!
3 Já o Método getlnitParameter retorna o valor do parâmetro de inicialização.

4 A cada nova thread, cria-se uma nova instância?Não, existe apenas uma instância e a cada nova requisição do cliente,o contêiner gera um novo par de objetos request e response, cria uma nova thread e os passa para ela.
/ 235

/

QUESTõES CoMENTADAS - SERVLETS - CEBRASPE

1. (CESPE - 2013 - TRT - 10a REGIÃO (DF e TO) - Técnico Judiciário
- Tecnologia da
Informação) No ciclo de vida de um servlet, o servidor recebe uma requisição e a repassa para o container, que a delega a um servlet. O container carrega a classe na memória,cria uma instância da classe do servlet e inicia a instância chamando o método init().

Comentários:

O Servidor recebe uma Requisição HTTP e a repassa para o Servlet Container. Já existe uma instância da servlet capaz de responder a essa requisição? Se sim, delega-se a requisição para essa instância; se não, carrega-se a classe servlet na memória, cria-se uma instância dela e a inicializa por meio do método init. Esse método recebe como parâmetro um objeto ServIetConfig!
Perfeito, conforme visto em aula.

Gabarito: C

2. (CESPE - 2013 - DPE/SP - Analista de Sistemas) No ciclo de vida de um servlet,
o servidor recebe uma requisição e a repassa para o container, que a delega a um servlet. Ocontainer carrega a classe na memória, cria uma instância da classe do servlet e inicia a instância chamando o método init().
Comentários:

O Servidor recebe uma Requisição HTTP e a repassa para o Servlet Container. Já existe uma instância da servlet capaz de responder a essa requisição? Se sim, delega-se a requisição para essa instância; se não, carrega-se a classe servlet na memória, cria-se uma instância dela e a inicializa por meio do método init. Esse método recebe como parâmetro um objeto ServIetConfig!
Conforme vimos em aula, está perfeito!

Gabarito: C

3. (CESPE - 2008 - MPE/RR - Analista de Sistemas) O nome completo da classe da qual herda a classe acima declarada é javax.servIet.HttpServIet. A classe indicada também
,

herda, indiretamente, da classe java.lang.Object. Portanto, é correto afirmar que classes em Java podem ter herança múltipla.
Comentários:

Ele se trata de um conjunto de classes e interfaces responsáveis pela comunicação especificamente com o protocolo HTTP - lá se encontram as interfaces HttpServIetRequest eHttpServIetResponse,
e também uma classe abstrata chamada HttpServlet2. Essa classe define diversos métodos para lidar com Requisições HTTP: doGet, doPost, doPut, doDelete, doHead, doTrace e doOptions, etc.
A classe acima herda da classe HttpServIet, cujo nome completo é javax.servIet.http.HttpServIet.Além disso, todas (todas mesmo!) as classes (inclusive a classe HttpServIet) herdam da classeObject (ou java.lang.Object). No entanto, a classe BookStoreServIet não herda diretamente deObject, logo não há que se falar em Herança Múltipla.

Gabarito: E

import java.io.*; import javax.servlet.*; import javax.servlet.http.*;
public class BookStoreServIet extends HttpServIet {

public void service (HttpServIetRequest request,
HttpServIetResponse response)

throws ServIetException, lOException {

// Get the dispatcher; it gets the main page to the user
RequestDispatcher dispatcher =

getServletContext().getRequestDispatcher(
"/bookstore/bookstore.html");

if (dispatcher == null) {

System.out.println("There was no dispatcher");

//No dispatcher means the html file could not be found.
response.sendError(response.SC_NO_CONTENT);

} else {

System.out.println("There is a dispatcher");

// Get or start a new session for this user
HttpSession session = request.getSession();

// Send the user the bookstore's opening page dispatcher.forward(request,response);
,

}

}

public String getServletlnfo() {

return "The BookStore servlet returns the main web page " +
"for Duke's Bookstore.";

}

}

4. (CESPE - 2008 - MPE/RR - Analista de Sistemas) Para a recuperação dos parâmetros que o browser envia para essa servlet, deve-se fazer acesso ao objeto apontado pela variável request, declarada na linha 3.
Comentários:

Perfeito, isso vale para qualquer servlet. Se você deseja ter acesso a parâmetros enviados pelo usuário por meio do browser para a servlet, você precisa ter acesso ao objeto request do tipoHttpServIetRequest.

Gabarito: C

5. (CESPE - 2008 - MPE/RR - Analista de Sistemas) Se, durante o processamento de um pedido por essa servlet, quando da execução da linha de código 10, o valor da variável dispatcher for null (nulo), então, a mensagem There was no dispatcher será apresentada na interface do usuário.
Comentários:

Questão de programador mesmo. Essa questão parece boba, mas observem que ela diz que a mensagem será apresentada na interface do usuário (i.e., no browser). Galera, para apresentar no browser, é necessário utilizar o objeto PrintWriter, caso contrário ele irá imprimir esse valor naJVM e o usuário não visualizará!

Gabarito: E

6. (CESPE - 2008 - MPE/RR - Analista de Sistemas) Durante o funcionamento de uma aplicação web na qual esteja em uso a servlet acima declarada, cada pedido http enviado pelo browser e direcionado à servlet BookStoreServIet implicará a criação de uma nova instância da classe BookStoreServIet, bem como a criação de uma thread que invoca o
/ 235

/

método service(HttpServletRequest, HttpServIetResponse), declarado no código apresentado.
Comentários:

Galera, implicará a criação de uma nova instância? Não, só existe uma instância! Na verdade,implicará a criação de uma nova thread para cada novo pedido.

Gabarito: E

7. (CESPE - 2008 - TRT/5 - Analista de Sistemas) Java Servlets são componentes Java executados somente do lado do servidor.
Comentários:

Pessoal, lá no Contêiner Web, há uma tal de Servlet! O que é isso,
professor? É uma API
independente de plataforma, escrita em Java, que roda no servidor (Container Web)
processando requisições de clientes e enviando respostas, e que pode ser traduzida como'servidorzinho'.
Como é? É isso mesmo! Porque ele é utilizado para estender as funcionalidades de um servidor.

Perfeito, conforme visto em aula.

Gabarito: C

8. (CESPE - 2011 - AL/ES - Analista de Sistemas) Servlet pode ser considerado um applet que é executado no lado servidor.
Comentários:

Na minha opinião, essa questão está errada! O Guia da Oracle afirma: "A servlet can almost be thought of as an applet that runs on the server side—without a face. Java servlets make many Web applications possible". Para mim, isso é diferente de dizer que um servlet pode ser considerado um applet que é executado no lado do servidor. Eu diria: "Em termos de local de execução, uma servlet pode ser considerada uma applet que é executada no lado servidor", no entanto a banca não entendeu dessa maneira :(
Gabarito: C

,

9. (CESPE - 2011 - TRE/ES - Analista de Sistemas) Um servlet é uma classe Java utilizada para ampliar a capacidade de acesso dos servidores a aplicações por meio do modelo requisição-resposta. Embora os servlets possam responder a um tipo específico de requisição hospedada em servidores web, os servlets não respondem a requisições genéricas.
Comentários:

Pessoal, lá no Contêiner Web, há uma tal de Servlet! O que é isso,
professor? É uma API
independente de plataforma, escrita em Java, que roda no servidor (Container Web)
processando requisições de clientes e enviando respostas, e que pode ser traduzida como'servidorzinho'.
Como é? É isso mesmo! Porque ele é utilizado para estender as funcionalidades de um servidor.

Vocês podem me perguntar se as servlets utilizam apenas HTTP. Não! Elas utilizam qualquer protocolo, no entanto ele é o protocolo mais utilizado por clientes web. Professor, o que você quis dizer com "classe java pura"? Cara, isso significa que essa classe só contém código java. Professor as servlets rodam no cliente ou no servidor? Pô... essa é muito fácil: Servlets rodam no Servidor(JVM)!;)

Embora os servlets possam responder a qualquer tipo de requisição, eles são mais utilizados para tratar requisições HTTP.
Gabarito: E

10.(CESPE - 2013 - CNJ - Analista de Sistemas) Apesar de serem independentes de plataforma, os servlets, para funcionarem, precisam utilizar o protocolo HTTP.
Comentários:

Vocês podem me perguntar se as servlets utilizam apenas HTTP. Não! Elas utilizam qualquer protocolo, no entanto ele é o protocolo mais utilizado por clientes web. Professor, o que você quis dizer com "classe java pura"? Cara, isso significa que essa classe só contém código java. Professor as servlets rodam no cliente ou no servidor? Pô... essa é muito fácil: Servlets rodam no Servidor(JVM)! ;)

Opa, não precisa utilizar HTTP (apesar de ele ser o mais comum).

Gabarito: E

,

11 .(CESPE - 2013 - TRE/MS - Analista de Sistemas - D) O servlet é uma classe de programa em Java utilizada para estender a capacidade dos servidores em aplicações web que trabalham com a filosofia requisição e resposta.
Comentários:

Pessoal, lá no Contêiner Web, há uma tal de Servlet! O que é isso,
professor? É uma API
independente de plataforma, escrita em Java, que roda no servidor (Container Web)
processando requisições de clientes e enviando respostas, e que pode ser traduzida como'servidorzinho'.
Como é? É isso mesmo! Porque ele é utilizado para estender as funcionalidades de um servidor.

Perfeito, conforme visto em aula.

Gabarito: C

12.(CESPE - 2008 - STJ - Analista Judiciário - Tecnologia da Informação) Na plataforma
J2EE,
uma aplicação web para a Internet pode ser composta por servlets, Java
Server Pages
(JSP) e páginas HTML. Nessas aplicações, a apresentação dos dados pode ser separada da lógica do negócio, adotando-se o estilo de arquitetura model view controller (MVC).Nesse caso, pode-se usar servlets operando como controladoras que recebem as solicitações dos usuários e providenciam o processamento das mesmas. Em uma mesma aplicação, entretanto, só pode existir um servlet operando como controladora.
Comentários:

Não faz sentido, visto que mais de uma servlet pode operar como controladora de uma aplicação.
Gabarito: E

13.(CESPE - 2010 - TRE-BA - Analista Judiciário - Análise de Sistemas) Todo servlet pode interagir com o contexto no qual ele está inserido por meio dos métodos especificados na interface ServIetContext.
Comentários:

Dentro da javax.servlet, temos também a interface ServIetContext! Ela define um contexto, i.e.,uma unidade de aplicação web que possui suas próprias configurações. Para executar
Servlets e
Páginas JSP, é necessário colocá-los dentro de um contexto de uma aplicação web -
existe um
Contexto por Aplicação Web por JVM. Entenderam mais ou menos? É simples, só é um pouco abstrato!
x'"'

/ 235

/

A interface ServIetContext é um conjunto de métodos que uma servlet utiliza para interagir com seu Servlet Container - por exemplo, para recuperar um arquivo, despachar requisições ou escrever em um arquivo de log! Bem, conforme a imagem abaixo, cada servlet possui seuServIetConfig. Já o ServIetContext serve para qualquer servlet do contexto e pode ser acessado por meio do objeto ServIetConfig.
Conforme vimos em aula, os servlets interagem com o contexto por meio de métodos especificados na interface ServIetContext - que estão contidos em um Servlet Container.
Gabarito: C

14.(CESPE - 2011 - Correios - Analista de Correios - Analista de Sistemas
- Produção) Entre outras aplicações, os servlets são utilizados para escrever aplicativos webJ2EE dinâmicos em servidores web. Um servlet pode utilizar seus recursos para realizar ações como, por exemplo, usar os registros (logging) para permitir que o servidor possa autenticar usuários.
Comentários:

Essa é uma questão bastante difícil! Tive que pesquisar e, de fato, pode-se utilizar recursos de servlets para autenticação, auditoria e logging!
Gabarito: C

15.(CESPE - 2009 - SECONT-ES - Auditor do Estado - Tecnologia da
Informação) No desenvolvimento de uma aplicação web que siga o padrão JEE, a tecnologiaJSP (Java
Server Pages) permite criar páginas web com componentes estáticos e dinâmicos;
o AJAX
permite a troca e manipulação de dados XML com comunicação assíncrona,
utilizando
XMLHttpRequest; e o servlet é exemplo de servidor de aplicações que contém diretórios como o bin e o webapps e é responsável por gerenciar requisições recebidas de clientes.
Comentários:

Pessoal, lá no Contêiner Web, há uma tal de Servlet! O que é isso,
professor? É uma API
independente de plataforma, escrita em Java, que roda no servidor (Container Web)
processando requisições de clientes e enviando respostas, e que pode ser traduzida como'servidorzinho'.
Como é? É isso mesmo! Porque ele é utilizado para estender as funcionalidades de um servidor.

Confome vimos em aula, servlet não é um servidor de aplicação, mas simplesmente uma
Classe
Java.

/ 235

/

Gabarito: E

SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023 (Pós-I

QUESTõES CoMENTADAS - SERVLETS - MULTIBANCAS

1. (FCC - 2007 - TRE-SE - Analista Judiciário - Tecnologia da Informação) Quando um servlet é carregado pela primeira vez para a máquina virtual Java do servidor:
a) ocorre um destroyO no processo cliente.

b) o seu método init() é invocado.

c) o método serviceO é definido.

d) ocorre a execução do método getOutputStream().

e) o seu método stream() é invocado.

Comentários:

O Servidor recebe uma Requisição HTTP e a repassa para o Servlet Container. Já existe uma instância da servlet capaz de responder a essa requisição? Se sim, delega-se a requisição para essa instância; se não, carrega-se a classe servlet na memória, cria-se uma instância dela e a inicializa por meio do método init. Esse método recebe como parâmetro um objeto ServIetConfig!
Perfeito, conforme visto em aula.

Gabarito: B

2. (FCC - 2011 - TRT - 1a REGIÃO - Analista de Sistemas) Em relação às tecnologias Java, éINCORRETO afirmar que as Servlets:

a) deixam para a API utilizada na sua escrita a responsabilidade com o ambiente em que elas serão carregadas e com o protocolo usado no envio e recebimento de informações.
b) fornecem um mecanismo simples e consistente para estender a funcionalidade de um servidorWeb.

c) podem ser incorporadas em vários servidores Web diferentes.

d) podem rodar em qualquer plataforma sem a necessidade de serem reescritas ou compiladas novamente.
e) são carregadas apenas uma vez e, para cada nova requisição, a servlet gera uma nova thread.

Comentários:

/ 235

/

(a) Deixa a responsabilidade do ambiente de execução e protocolo para a API? De jeito algum!Isso é uma escolha do programador; (b) Perfeito, já vimos diversas vezes que elas são responsáveis por estender a funcionalidade de servidores; (c) Perfeito, está disponível para diversos servidores web; (d) Perfeito, nunca se esqueçam que são classes Java; (e) Perfeito, é uma thread para cada requisição.
Gabarito: A

3. (FCC - 2010 - DPE/SP - Analista de Sistemas) Servlets são projetadas para fornecer aos desenvolvedores uma solução JAVA para criar aplicações web. Para criarServlets é necessário importar as classes padrão de extensão dos pacotes:
a) javax.servlet e javax.servlet.http.

b) javax.servlet e javax.http.servlet.

c) javax.servlet.html e javax.servlet.http.

d) servlet.javax e servlet.javax.http.

e) javax.servlet.smtp e javax.servlet.html.

Comentários:

Dado esse código, vamos ver alguns detalhes importantes: primeiro, foi importado o pacote javax.servlet, que é um conjunto de classes e interfaces responsáveis pela comunicação com diversos protocolos - lá se encontram, por exemplo, as interfacesServIetRequest e
ServIetResponse. No entanto, observem abaixo que se importa também o pacote javax.servlet.http - cuja estrutura é mostrada a seguir:
Conforme vimos em aula, trata-se da javax.servlet e javax.servlet.http.
Gabarito: A

4. (FCC - 2012 - TRE/CE - Analista de Sistemas) No contexto do ciclo de vida de um servlet,considere:

I. Quando o servidor recebe uma requisição, ela é repassada para o container que, por sua vez, carrega a classe na memória e cria uma instância da classe do servlet.
II. Quando um servlet é carregado pela primeira vez para a máquina virtual Java do servidor,o método init() é invocado, para preparar recursos para a execução do serviço ou para estabelecer conexão com outros serviços.
,

III. Estando o servlet pronto para atender as requisições dos clientes, o container cria um objeto de requisição (ServIetRequest) e de resposta (ServIetResponse) e depois chama o método service(), passando os objetos como parâmetros.
IV. O método destroy() permite liberar os recursos que foram utilizados,
sendo invocado quando o servidor estiver concluindo sua atividade.
Está correto o que se afirma em:

a) I, II e III, apenas.

b) I, II e IV, apenas.

c) I, III e IV, apenas.

d) II, III e IV, apenas e) I, II, III e IV.
Comentários:

Conforme a imagem acima, o Servidor recebe uma Requisição HTTP e a repassa para o
Servlet
Container. Já existe uma instância da servlet capaz de responder a essa requisição? Se sim,delega-se a requisição para essa instância; se não, carrega-se a classe servlet na memória, cria-se uma instância dela e a inicializa por meio do método init. Esse método recebe como parâmetro um objeto ServIetConfig!
(I) Galera, isso só ocorre se já não existir uma instância da servlet. No entanto,
guardem isso para sempre na vida de concurseiros: "Um item só está errado se contiver um erro". O item disse que ocorre sempre assim? Não. Existe um caso em que o que foi descrito no item ocorre? Sim! Logo, não há erro! Ele descreveu um caso, não disse que era o único caso! Item completamente perfeito...
Conforme a imagem acima, o Servidor recebe uma Requisição HTTP e a repassa para o
Servlet
Container. Já existe uma instância da servlet capaz de responder a essa requisição? Se sim,delega-se a requisição para essa instância; se não, carrega-se a classe servlet na memória, cria-se uma instância dela e a inicializa por meio do método init. Esse método recebe como parâmetro um objeto ServIetConfig!
(II) Conforme vimos em aula, esse método contém as configurações que preparam os recursos para a execução do serviço ou conexão com outros serviços.
Esse objeto contém informações de configuração e parâmetros de inicialização da aplicação web. A partir do momento que a servlet é inicializada, o contêiner pode utilizá-la para tratar requisições dos clientes. Chama-se então o método service com dois parâmetros:
ServIetRequest, que contém a solicitação do cliente; e o ServIetResponse, que contém a resposta - ambos criados pelo contêiner.
(III) Conforme vimos em aula, eles são criados para tratar a solicitação e resposta para o cliente e são criados pelo contêiner.
Na prática, o método service determina qual Método HTTP (GET/POST) deve ser chamado na servlet. Por fim, o contêiner chama o método destroy a fim de remover a instância da servlet da memória e liberar os recursos e os dados. Tanto o método init quanto o método destroy são executados apenas uma vez durante o ciclo de vida da servlet. Professor, quem gerencia tudo nisso? O Servlet Container!
(IV) Conforme vimos em aula, está perfeito! Quando a servlet tiver cumprido seu papel, o servidor liberará os recursos investidos.
Gabarito: E

5. (FCC - 2013 - DPE/SP - Analista de Sistemas) Um Servlet Contêiner controla o ciclo de vida de uma servlet onde são invocados três métodos essenciais: um para inicializar a instância da servlet, um para processar a requisição e outro para descarregar a servlet da memória. Os itens a seguir representam, nessa ordem, o que ocorre quando um usuário envia uma requisição HTTP ao servidor:
I. A requisição HTTP recebida pelo servidor é encaminhada ao Servlet
Contêiner que mapeia esse pedido para uma servlet específica.
II. O Servlet Contêiner invoca o método init da servlet. Esse método é chamado em toda requisição do usuário à servlet não sendo possível passar parâmetros de inicialização.
III. O Servlet Contêiner invoca o método service da servlet para processar a requisição HTTP,passando os objetos request e response. O método service não é chamado a cada requisição,mas apenas uma vez, na primeira requisição do usuário à servlet.

IV. Para descarregar a servlet da memória, o Servlet Contêiner chama o método unload, que faz com que o garbage collector retire a instância da servlet da memória.
Está correto o que se afirma em:

a) I, II, III e IV.

b) I, apenas.

/ 235

/

c) I e IV, apenas.

d) II, III e IV, apenas.

e) II e III, apenas.

Comentários:

Conforme a imagem acima, o Servidor recebe uma Requisição HTTP e a repassa para o
Servlet
Container. Já existe uma instância da servlet capaz de responder a essa requisição? Se sim,delega-se a requisição para essa instância; se não, carrega-se a classe servlet na memória, cria-se uma instância dela e a inicializa por meio do método init. Esse método recebe como parâmetro um objeto ServIetConfig!
(I) Conforme vimos em aula, o contêiner verifica se há uma servlet específica para responder a esse pedido.
Conforme a imagem acima, o Servidor recebe uma Requisição HTTP e a repassa para o
Servlet
Container. Já existe uma instância da servlet capaz de responder a essa requisição? Se sim,delega-se a requisição para essa instância; se não, carrega-se a classe servlet na memória, cria-se uma instância dela e a inicializa por meio do método init. Esse método recebe como parâmetro um objeto ServIetConfig!
(II) Conforme vimos em aula, esse método pode - e recebe - parâmetros de inicialização.

Esse objeto contém informações de configuração e parâmetros de inicialização da aplicação web. A partir do momento que a servlet é inicializada, o contêiner pode utilizá-la para tratar requisições dos clientes. Chama-se então o método service com dois parâmetros:ServIetRequest, que contém a solicitação do cliente; e o ServIetResponse, que contém a resposta - ambos criados pelo contêiner.
(III) Na verdade, esse método é chamado a cada requisição, porque cada requisição possui parâmetros diferentes.
Na prática, o método service determina qual Método HTTP (GET/POST) deve ser chamado na servlet. Por fim, o contêiner chama o método destroy a fim de remover a instância da servlet da memória e liberar os recursos e os dados. Tanto o método init quanto o método destroy são executados apenas uma vez durante o ciclo de vida da servlet. Professor, quem gerencia tudo nisso? O Servlet Container!
(IV) Conforme vimos em aula, não se chama método unload - o nome do método é destroy!

/ 235

/

Gabarito: B

6. (FCC - 2006 - BACEN - Analista de Sistemas) Para ser um servlet,
uma classe deve estender a classe I e exceder as ações "doGet" ou "doPost" (ou ambas),dependendo se os dados estão sendo enviados por uma ação GET ou por uma ação POST. Estes métodos tomam dois argumentos: um II e um III em sua execução. Preenchem correta e respectivamente I, II e III:
I II III

A HttpJspServIet

B JspServIet

C HttpServIetRequest

D HttpServIet

E HttpServIet

Xml HttpServIet
HttpServIetResponse
XmlHttpServIetRquest
HttpServIetRequest
HttpServIetRequest

Xml HttpServIetResponse
HttpServIetRequest

Xml HttpServIetResponse
HttpServIetResponse
HttpSen/letResponse.write

Comentários:

Voltando ao nosso código: importamos os dois pacotes, estendemos essa classe abstrata e passamos como parâmetro as duas interfaces. Se a Requisição HTTP foi feita utilizando o MétodoGET, executaremos o método doGet; se foi com o Método POST, executaremos o método doPost. Esses métodos recebem dois parâmetros: uma requisição HttpServIetRequest e uma resposta HttpServIetResponse.
Para ser um servlet, uma classe deve estender a classe HttpServIet e exceder as ações
"doGet"
ou "doPost" (ou ambas), dependendo se os dados estão sendo enviados por uma ação GET
ou por uma ação POST. Estes métodos tomam dois argumentos: um HttpServIetRequest e umHttpServIetResponse em sua execução.

Gabarito: D

7. (FCC - 2007 - TRE-SE - Analista Judiciário - Tecnologia da
Informação) Em Java, a passagem de dados de um formulário do cliente para o servlet pode ocorrer por meio do uso do método:
a) importO

b) return()

c) catch()

d) getParameterO

e) nameComponentO

/ 235

/

Comentários:

É importante entender também como funciona um dos métodos mais importantes da interface
HttpServIetRequest: método getParameter! Bem, ele retorna o valor do parâmetro de um requisito como uma String; Por que isso é importante? Porque ele é útil na passagem de dados de um formulário do cliente, i.e., por meio dele, a servlet pode capturar dados de formulários!Agora vamos ver o ciclo das servlets ;)

Conforme vimos em aula, trata-se do método getParameter().

Gabarito: D

8. (FCC - 2012 - TRE-CE - Programador de computador) A tecnologia
Java Servlet é baseada na construção de classes servlet que executam no servidor recebendo dados de requisições do cliente, processando esses dados, opcionalmente acessando recursos externos como bancos de dados, e respondendo ao cliente com conteúdo no formato HTML.
Com relação ao tema, analise as asserções a seguir:

Embora as servlets sejam muito boas no que fazem, tornou-se difícil responder ao cliente com conteúdo no formato HTML.
PORQUE

Geralmente quem trabalha com o conteúdo HTML é o web designer que normalmente não é programador Java experiente. Ao misturar HTML dentro de uma servlet,torna-se muito difícil separar as funções de web designer e desenvolvedor Java. Além disso, é difícil fazer alterações no conteúdo HTML, pois para cada mudança, uma recompilação da servlet tem que acontecer. Para contornar as limitações da tecnologia Java Servlet a SunMicrosystems criou a tecnologia JavaServer Pages (JSP).
Acerca dessas asserções, é correto afirmar:

a) Tanto a primeira quanto a segunda asserções são proposições falsas.

b) A primeira asserção é uma proposição verdadeira e a segunda uma proposição falsa.

c) A primeira asserção é uma proposição falsa e a segunda uma proposição verdadeira.

d) As duas asserções são proposições verdadeiras, mas a segunda não é a justificativa correta da primeira.
/ 235

/

e) As duas asserções são proposições verdadeiras e a segunda é a justificativa correta da primeira.
Comentários:

Outra desvantagem importante é que o programador, além de ser bom em Java, tem que ser bom em Web Design! No entanto, quando ele está escrevendo o código Java, ele não possui as ferramentas de Web Design! O JSP permite essa separação, i.e., os DesenvolvedoresJava criam as Servlets (Lógica de Negócio) e os Web Designers criam as Páginas JSP (Lógica deApresentação)! Bacana?

Roubei esse parágrafo da aula de JSP! Observem que ambas as assertivas estão corretas e a segunda justifica a primeira.
Gabarito: E

9. (FCC - 2013 - AL-RN - Analista Legislativo - Analista de Sistemas) No Java
EE 6 os métodos doPost e doGet podem ser sobrescritos em uma servlet criada na aplicação para receberem as requisições vindas de páginas HTML. Quando sobrescritos na servlet, eles substituem seus métodos ancestrais existentes na classe abstrata:
a) GenericServIet.

b) HttpServIet.

c) HttpServIetRequest.

d) HttpServIetResponse.

e) HttpServIetObject.

Comentários:

Ele se trata de um conjunto de classes e interfaces responsáveis pela comunicação especificamente com o protocolo HTTP - lá se encontram as interfaces HttpServIetRequest eHttpServIetResponse, e também uma classe abstrata chamada HttpServIet. Essa classe define diversos métodos para lidar com Requisições HTTP: doGet, doPost, doPut, doDelete, doHead,doTrace e doOptions, etc.

Conforme vimos em aula, essa classe abstrata é a HttpServIet.

Gabarito: B

/ 235

/

1O.(FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da
Informação)
Para ler os parâmetros de inicialização do contexto de um servlet utiliza-se o método:

a) String getlnitParameter(String).

b) Enumeration getlnitParameterNames().

c) InputStream getResourceAsStream().

d) setAttribute(String nome, Object).

e) Object getAttribute(String nome).

Comentários:

É importante entender também como funciona um dos métodos mais importantes da interface
HttpServIetRequest: método getParameter3! Bem, ele retorna o valor do parâmetro de uma requisição como uma String; E por que é importante? Porque ele é útil na passagem de dados de um formulário do cliente, i.e., por meio dele, a servlet pode capturar dados de formulários!Agora vamos ver o ciclo das servlets ;)

Conforme vimos em aula, a nota de rodapé 3 afirma que o Método getlnitParameter retorna o valor do parâmetro de inicialização de uma servlet.
Gabarito: A

11.(FMP/RS - 2013 - MPE/AC - Analista de Sistemas) No contexto da arquitetura JavaEnterprise Edition, são, em termos de estrutura,
classes Java especializadas que se assemelham muito à estrutura dos applets Java, porém rodando em um servidor web e não no do cliente.
Assinale a única alternativa que completa corretamente a lacuna acima.

a) Java ME (Java Micro Edition)

b) portlets c) Java Persistence API (JPA)
d) Enterprise JavaBeans (EJB)

e) servlets

Comentários:

A Oracle afirma: "A servlet can almost be thought of as an applet that runs on the server side".Portanto, no contexto da arquitetura Java Enterprise Edition, servlets são, em termos de estrutura, classes Java especializadas que se assemelham muito à estrutura dos appletsJava,
porém rodando em um servidor web e não no do cliente.

,

Gabarito: E

12.(VUNESP - 2013 - FUNDUNESP - Analista de Sistemas) Na plataforma J2EE, a classe
ServIetRequest define:

a) a estrutura do objeto principal do Servlet, permitindo que sejam feitas requisições ao Servlet.

b) métodos que permitem que o Servlet faça requisições de forma assíncrona.

c) métodos que permitem que o Servlet faça requisições aos clientes.

d) propriedades que permitem que seja alterado o comportamento do Servlet.

e) um objeto que fornecerá informações sobre a requisição feita pelo cliente ao Servlet.

Comentários:

Dado esse código, vamos ver alguns detalhes importantes: primeiro, foi importado o pacote javax.servlet, que é um conjunto de classes e interfaces responsáveis pela comunicação com diversos protocolos - lá se encontram, por exemplo, as interfacesServIetRequest e
ServIetResponse. No entanto, observem abaixo que se importa também o pacote javax.servlet.http - cuja estrutura é mostrada a seguir:
Conforme vimos em aula, ServIetRequest é uma interface e, não, uma classe! Vacilou, banca!
Bem, essa interface funciona como a interface ServIetHttpRequest, porém não é específica para o Protocolo HTTP! Bem, ambas servem para manipular informações de uma requisição feito pelo cliente ao servlet.
Gabarito: E

13.(CESGRANRIO - 2006 - DECEA - Analista de Sistemas - A) Servlets e arquivos JSP são executados no WEB Container.
Comentários:

Pessoal, lá no Contêiner Web, há uma tal de Servlet! O que é isso, professor? É uma
API
independente de plataforma, escrita em Java, que roda no servidor
(Container Web)
processando requisições de clientes e enviando respostas, e que pode ser traduzida como'servidorzinho'. Como é? É isso mesmo! Porque ele é utilizado para estender as funcionalidades de um servidor.
Conforme vimos em aula, são executados no Container Web.

Gabarito: C

,

14.(CESGRANRIO - 2006 - DECEA - Analista de Sistemas - B) Applets e
Servlets são compilados e executados no servidor.
Comentários:

Pessoal, lá no Contêiner Web, há uma tal de Servlet! O que é isso, professor? É uma
API
independente de plataforma, escrita em Java, que roda no servidor
(Container Web)
processando requisições de clientes e enviando respostas, e que pode ser traduzida como'servidorzinho'. Como é? É isso mesmo! Porque ele é utilizado para estender as funcionalidades de um servidor.
Conforme vimos em aula, servlets rodam no servidor, mas applets rodam no cliente.

Gabarito: E

15.(CESGRANRIO - 2009 - BNDES - Analista de Sistemas - A) Ao estudar as especificações e frameworks Java EE, um Analista de Sistemas concluiu que o container WEB do servidor de aplicações é o responsável por gerenciar o ciclo de vida de servlets e de EJBs utilizados numa aplicação Java.
Comentários:

Na prática, o método service determina qual Método HTTP (GET/POST) deve ser chamado na servlet. Por fim, o contêiner chamar o método destroy a fim de remover a instância da servlet da memória e liberar os recursos e os dados. Tanto o método init quanto o método destroy são executados apenas uma vez durante o ciclo de vida da servlet. Professor, quem gerencia tudo nisso? O Servlet Container!
Conforme vimos em aula, o ciclo de vida das servlets é gerenciado pelo Servlet
Container (que se encontra dentro do Web Container). No entanto, o Web Container não é responsável pelo ciclo de vida de EJBs (seria impossível!).
Gabarito: E

16.(CESGRANRIO - 2009 - BNDES - Analista de Sistemas - B) Ao estudar as especificações e frameworks Java EE, um Analista de Sistemas concluiu que no container WEB, uma página JSP transforma-se em um servlet, que é compilado, carregado e inicializado.
Comentários:

/ 235

/

Isso é da aula de Páginas JSP, no entanto é sabido que Pásginas JSP se transformam emServlets!

Gabarito: C

17.(CESGRANRIO - 2012 - PETROBRÁS - Analista de Sistemas) Seja o código a seguir:

public class Servletl extends HttpServlet {

protected void processRequest(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {

response. setContentType ("text/html; charset=UTF-8") ;
PrintWriter out = response.getWriter();

try {

out. println ("<html><body>Meu Servlet</body></html>") ;

} finally {

out.close();

}

}

@0verride protected void doGet(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException {

processRequest(request, response);

}

êOverride protected void doPost(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException {

processRequest(request, response);

}

}

Sobre esse código, do qual foram omitidas as declarações de importação e o método getServIetlnfo por concisão, considere as afirmativas a seguir.
I - Como o método servicef) não foi redefinido, o container não saberá qual método chamar para cada tipo de pedido, gerando uma exceção.
II - Como o método init() não foi redefinido, o construtor padrão da classe mãe será chamado.

III - Como o método destroyO não foi redefinido, o container gerará um erro registrando-o no arquivo de logs ao terminar este aplicativo.
É correto APENAS o que se afirma em:

a) I

b) II

c) III

d) I e III

e) II e III

Comentários:

(I) Na questão, estamos herdando de HttpServIet e, não, Servlet diretamente.
Logo, não precisamos sobrescrever o método service, basta utilizar doGet e doPost.
(II) Perfeito, quem geralmente chama o método init é o contêiner e, não, o programador. Se ele não redefini-lo, será chamado o construtor da classe mãe (super.init(config)).
(III) Galera, quem geralmente chama o método destroy é o contêiner e, não, o programador. Logo,não é necessário redefini-lo.

Gabarito: B

1 import java.io.*; import javax.servlet.*; import javax.servlet.http.*;

2 public class BookStoreServlet extends HttpServIet {

3 public void service (HttpServletRequest request,

4 HttpServletResponse response)

5 throws ServletException, IOException {

6 // Get the dispatcher; it gets the main page to the user

7 RequestDispatcher dispatcher =

8 getServletContext().getRequestDispatcher(

9 "/bookstore/bookstore.html");

10 if (dispatcher == null) {

11 System. out.println("There was no dispatcher");

12 // No dispatcher means the html file could not be found.

13 response.sendError(response.SC_NO_CONTENT) ;

14 } else {

15 System. out.println("There is a dispatcher");

16 // Get or start a new session for this user

17 HttpSession session = request.getSession();

18 // Send the user the bookstore's opening page

19 dispatcher.forward(request, response);

20 }

21 }

22 public String getServletlnfo() {

23 return "The BookStore servlet returns the main web page " +

24 "for Duke's Bookstore.";

25 }

26 }

18.(ESAF - 2008 - CGU - Analista de Sistemas - A) Servlets são classes de programação Java que geram conteúdo dinâmico (normalmente para páginas HTML) e interagem com os clientes, utilizando o modelo challenge/request. Normalmente utilizam o protocolo HTTP,apesar de não serem restritas a ele.

Comentários:

A documentação oficial afirma que se trata de uma classe java pura utilizada para estender as capacidades dos servidores que hospedam aplicações acessadas por meio de um modelo de requisição-resposta. Em geral, elas funcionam para fornecer conteúdo web dinâmicos(normalmente em HTML) às páginas web, processando requisições/respostas, filtrando dados,acessando o banco de dados, etc.

Opa, utiliza-se um modelo Request/Response e, não, Challenge/Request.

Gabarito: E

19.(CIAAR - 2012 - CIAAR - Oficial Temporário - Análise de Sistemas) O método chamado para liberar quaisquer recursos mantidos pelo servlet, quando o contêiner de servlets termina o servlet, denomina-se:
a) get.

b) post.

c) destroy.

d) prerender.

Comentários:

Na prática, o método service determina qual Método HTTP (GET/POST) deve ser chamado na servlet. Por fim, o contêiner chamar o método destroy a fim de remover a instância da servlet da memória e liberar os recursos e os dados. Tanto o método init quanto o método destroy são executados apenas uma vez durante o ciclo de vida da servlet. Professor, quem gerencia tudo nisso? O Servlet contêiner!
Conforme vimos em aula, trata-se do método Destroy!

Gabarito: C

20.(AOCP - 2012 - BRDE - Analista de Sistemas - Desenvolvimento de Sistemas - (Prova TIPO
4)) Sobre Servlets, analise as assertivas e assinale a alternativa que aponta as corretas.

I. Servlets são implementadas como arquivos de classe da Linguagem Java.

II. Servlets são independentes de plataforma, de modo que podem ser executadas em diferentes servidores, em diferentes sistemas operacionais.
/ 235

/

III. As Servlets podem acessar qualquer uma das APIs Java. Uma Servlet pode usar a
API
JDBC para acessar e armazenar dados ou para acessar objetos remotos.

IV. Ao criar uma Servlet, somos obrigados a reescrever nove métodos presentes à interface que foi implementada.
a) Apenas I e II.

b) Apenas I e III.

c) Apenas II e III.

d) Apenas I, II e III.

e) I, II, III e IV.

Comentários:

I. Galera, não sei o que a banca quis dizer com isso! Imagino que seja que Servlets são ClassesJava (diferente de JSP) - logo, o item está correto.

II. Não gosto de dizer que são independentes de plataforma, prefiro dizer que são multiplataformas, mas está correto.
III. Conforme já foi dito, são classes Java! Logo, podem acessar APIs Java como qualquer outra.

IV. Não, somos obrigados a implementar, se for Servlet HTTP, os métodos doGet ou doPost.

Gabarito: D

21.(VUNESP - 2013 - FUNDUNESP - Analista Programador Júnior) Para criar um Servlet que processará as requisições HTTP na plataforma J2EE, deve-se:
a) criar uma classe que implemente a interface Servlet.

b) criar uma classe que estenda a classe HttpServIet.

c) implementar o método processHttpHeader.

d) instanciar a classe Servlet, passando para o parâmetro requestType o valorServlet. HTTP_REQUEST.

,

e) invocar o método Servlet.service(Servlet.HTTP_REQUEST) antes do processamento da requisição.
Comentários:

Dado esse código, vamos ver alguns detalhes importantes: primeiro, foi importado o pacote javax.servlet, que é um conjunto de classes e interfaces responsáveis pela comunicação com diversos protocolos - lá se encontram, por exemplo, as interfacesServIetRequest e
ServIetResponse. No entanto, observem abaixo que se importa também o pacote javax.servlet.http - cuja estrutura é mostrada a seguir:
Ele se trata de um conjunto de classes e interfaces responsáveis pela comunicação especificamente com o protocolo HTTP - lá se encontram as interfaces HttpServIetRequest eHttpServIetResponse,
e também uma classe abstrata chamada HttpServlet2. Essa classe define diversos métodos para lidar com Requisições HTTP: doGet, doPost, doPut, doDelete, doHead, doTrace e doOptions, etc.
Conforme vimos em aula, quando queremos criar uma Servlet que processará especificamente requisições HTTP, devemos criar uma classe que estenda a classe HttpServIet - como mostrado na imagem.
Gabarito: B

22.(FEPESE - 2013 - JUCESC - Analista Técnico em Gestão de Registro Mercantil -
Analista de Informática) Assinale a alternativa que defne corretamente um Servlet.
a) É um método da JPA utilizado na persistência assíncrona de dados.

b) É um componente que roda do lado do cliente para tratar problemas de comunicação.

/ 235

/

c) É uma classe Java utilizada para estender as capacidades de um servidor.

d) É uma biblioteca JBOSS que emula servidores no lado do cliente.

e) É uma JSP que possibilita a execução de código no lado do cliente, mesmo sem comunicação com um servidor.
Comentários:

Pessoal, lá no Contêiner Web, há uma tal de Servlet! O que é isso,
professor? É uma API
independente de plataforma, escrita em Java, que roda no servidor (Container Web)
processando requisições de clientes e enviando respostas, e que pode ser traduzida como'servidorzinho'.
Como é? É isso mesmo! Porque ele é utilizado para estender as funcionalidades de um servidor.

Conforme vimos em aula, trata-se da terceira opção - todas as outras são absurdas!

Gabarito: C

23.(VUNESP - 2013 - FUNDUNESP - Analista Programador Júnior) Considere o
Servlet a seguir:
import java.io.*;
import javax.servlet.*;

import javax.servlet.http.*;

public class ClasseServIet extends HttpServIet {

public void doGet(HttpServletRequest request,
HttpServIetResponse response){
response.write("<html>");
response.write("<body>");
response.write("Servlet em operação!");
response. write("</body>");
response.write("</html>");

}

}

Sobre o código do Servlet, é possível afirmar que:

a) ao ser executado por um contêiner de Servlet, será exibida uma tela em branco no navegador.

/ 235

/

b) ao ser executado por um contêiner de Servlet, será exibida a mensagem "Servlet em operação!"na tela do navegador.

c) não pode ser compilado, pois a classe HttpServIetResponse não possui o método write.

d) não pode ser compilado, pois HttpServIet é uma interface e, portanto, não pode ser estendida por uma classe.
e) o conteúdo exibido na tela do navegador não será codificado corretamente, pois a codificação da página não foi informada.
Comentários:

Vocês observarão um padrão muito comum em servlets. Qual, professor? Para devolver a resposta ao cliente, devemos primeiro definir o tipo de saída. Para tal, utilizamos a função setContentType do HttpServIetResponse - nossa servlet definiu como text/html, i.e., teremos uma saída em HTML!A seguir, utilizamos o método getWriter para capturar os caracteres da resposta e inseri-los em um objeto out.
Conforme vimos em aula, nós utilizamos o método getWriter para capturar a resposta e passar para um objeto PrintWriter. A HttpServIetResponse não possui qualquer método write.
Gabarito: C

24.(CESGRANRIO - 2008 - TJ-RO - Analista Judiciário - Tecnologia da Informação) O
método da interface javax.servlet.http.HttpSession, utilizado para finalizar uma sessão de usuário em um container J2EE, é a) cancel()
b) delete()

c) destroy()

d) invalidate()

e) release()

Comentários:

/ 235

/

Galera, coloquei essa questão para que vocês saibam que nem sempre será possível responder todas as questões de uma prova. A banca tem o poder de cobrar o que ela quiser. Eassim ela o faz, porque toda prova tem seus itens impossíveis. Não fiquem tristes, porque um item como esse ninguém acerta (exceto no chute). É inviável e não vale a pena estudar todos os métodos,parâmetros, objetos de uma linguagem ou tecnologia. Bem, no caso dessa questão, a resposta era invalidate().
Gabarito: D

1. (CESPE - 2013 - TRT - 10a REGIÃO (DF e TO) - Técnico Judiciário - Tecnologia da Informação)
No ciclo de vida de um servlet, o servidor recebe uma requisição e a repassa para o container,
que a delega a um servlet. O container carrega a classe na memória, cria uma instância da classe do servlet e inicia a instância chamando o método init().
2. (CESPE - 2013 - DPE/SP - Analista de Sistemas) No ciclo de vida de um servlet, o servidor recebe uma requisição e a repassa para o container, que a delega a um servlet. O container carrega a classe na memória, cria uma instância da classe do servlet e inicia a instância chamando o método init().
import java.io.*; import javax.servlet.*; import javax.servlet.http.*;
public class BookStoreServIet extends HttpServIet {

public void service (HttpServIetRequest request,
HttpServIetResponse response)

throws ServIetException, lOException {

// Get the dispatcher; it gets the main page to the user
RequestDispatcher dispatcher =

getServletContext().getRequestDispatcher(
"/bookstore/bookstore.html");

if (dispatcher == null) {

System.out.println("There was no dispatcher");

//No dispatcher means the html file could not be found.
response. sendError(response.SC_NO_CONTENT);

} else {

System.out.println("There is a dispatcher");

// Get or start a new session for this user
HttpSession session = request.getSession();

// Send the user the bookstore's opening page dispatcher.forward(request, response);
}

}

public String getServIetlnfoQ {

return "The BookStore servlet returns the main web page " +

"for Duke's Bookstore.";

}

}

3. (CESPE - 2008 - MPE/RR - Analista de Sistemas) O nome completo da classe da qual herda a classe acima declarada é javax.servIet.HttpServIet. A classe indicada também herda,indiretamente, da classe java.lang.Object. Portanto, é correto afirmar que classes em
Java podem ter herança múltipla.
4. (CESPE - 2008 - MPE/RR - Analista de Sistemas) Para a recuperação dos parâmetros que o browser envia para essa servlet, deve-se fazer acesso ao objeto apontado pela variável request, declarada na linha 3.
5. (CESPE - 2008 - MPE/RR - Analista de Sistemas) Se, durante o processamento de um pedido por essa servlet, quando da execução da linha de código 10, o valor da variável dispatcher for null (nulo), então, a mensagem There was no dispatcher será apresentada na interface do usuário.
6. (CESPE - 2008 - MPE/RR - Analista de Sistemas) Durante o funcionamento de uma aplicação web na qual esteja em uso a servlet acima declarada, cada pedido http enviado pelo browser e direcionado à servlet BookStoreServIet implicará a criação de uma nova instância da classeBookStoreServIet, bem como a criação de uma thread que invoca o método service(HttpServletRequest, HttpServIetResponse), declarado no código apresentado.
7. (CESPE - 2008 - TRT/5 - Analista de Sistemas) Java Servlets são componentes Java executados somente do lado do servidor.
8. (CESPE - 2011 - ALVES - Analista de Sistemas) Servlet pode ser considerado um applet que é executado no lado servidor.
9. (CESPE - 2011 - TRE/ES - Analista de Sistemas) Um servlet é uma classe Java utilizada para ampliar a capacidade de acesso dos servidores a aplicações por meio do modelo requisição-resposta. Embora os servlets possam responder a um tipo específico de requisição hospedada em servidores web, os servlets não respondem a requisições genéricas.
10.(CESPE - 2013 - CNJ - Analista de Sistemas) Apesar de serem independentes de plataforma,
os servlets, para funcionarem, precisam utilizar o protocolo HTTP.

11 .(CESPE - 2013 - TRE/MS - Analista de Sistemas - D) O servlet é uma classe de programa em
Java utilizada para estender a capacidade dos servidores em aplicações web que trabalham com a filosofia requisição e resposta.
12.(CESPE - 2008 - STJ - Analista Judiciário - Tecnologia da Informação) Na plataforma J2EE, uma aplicação web para a Internet pode ser composta por servlets, Java Server Pages (JSP)e páginas HTML. Nessas aplicações, a apresentação dos dados pode ser separada da lógica do negócio, adotando-se o estilo de arquitetura model view controller (MVC). Nesse caso, pode-se usar servlets operando como controladoras que recebem as solicitações dos usuários e providenciam o processamento das mesmas. Em uma mesma aplicação, entretanto, só pode existir um servlet operando como controladora.
13.(CESPE - 2010 - TRE-BA - Analista Judiciário - Análise de Sistemas) Todo servlet pode interagir com o contexto no qual ele está inserido por meio dos métodos especificados na interfaceServIetContext.

14.(CESPE - 2011 - Correios - Analista de Correios - Analista de Sistemas - Produção) Entre outras aplicações, os servlets são utilizados para escrever aplicativos web J2EE dinâmicos em servidores web. Um servlet pode utilizar seus recursos para realizar ações como, por exemplo,usar os registros (logging) para permitir que o servidor possa autenticar usuários.

15.(CESPE - 2009 - SECONT-ES - Auditor do Estado - Tecnologia da
Informação) No desenvolvimento de uma aplicação web que siga o padrão JEE, a tecnologia JSP (Java ServerPages) permite criar páginas web com componentes estáticos e dinâmicos; o AJAX permite a troca e manipulação de dados XML com comunicação assíncrona, utilizando XMLHttpRequest;e o servlet é exemplo de servidor de aplicações que contém diretórios como o bin e o webapps e é responsável por gerenciar requisições recebidas de clientes.
GABARITo

GABARITO

c 5. E 9. E

c 6. E 10. E

E 7. C
11. C 15

c 8. C 12. E

LISTA DE QUESTõES - SERvLET - MULTIBANCAS

1. (FCC - 2007 - TRE-SE - Analista Judiciário - Tecnologia da Informação) Quando um servlet é carregado pela primeira vez para a máquina virtual Java do servidor:
a) ocorre um destroyO no processo cliente.

b) o seu método init() é invocado.

c) o método service() é definido.

d) ocorre a execução do método getOutputStream().

e) o seu método stream() é invocado.

2. (FCC - 2011 - TRT - 1a REGIÃO - Analista de Sistemas) Em relação às tecnologias Java, é
INCORRETO afirmar que as Servlets:

a) deixam para a API utilizada na sua escrita a responsabilidade com o ambiente em que elas serão carregadas e com o protocolo usado no envio e recebimento de informações.
b) fornecem um mecanismo simples e consistente para estender a funcionalidade de um servidor
Web.

c) podem ser incorporadas em vários servidores Web diferentes.

d) podem rodar em qualquer plataforma sem a necessidade de serem reescritas ou compiladas novamente.
e) são carregadas apenas uma vez e, para cada nova requisição, a servlet gera uma nova thread.

3. (FCC - 2010 - DPE/SP - Analista de Sistemas) Servlets são projetadas para fornecer aos desenvolvedores uma solução JAVA para criar aplicações web. Para criar Servlets é necessário importar as classes padrão de extensão dos pacotes:
a) javax.servlet e javax.servlet.http.

b) javax.servlet e javax.http.servlet.

c) javax.servlet.html e javax.servlet.http.

d) servlet.javax e servlet.javax.http.

e) javax.servlet.smtp e javax.servlet.html.

4. (FCC - 2012 - TRE/CE - Analista de Sistemas) No contexto do ciclo de vida de um servlet,
considere:

I. Quando o servidor recebe uma requisição, ela é repassada para o container que, por sua vez, carrega a classe na memória e cria uma instância da classe do servlet.
II. Quando um servlet é carregado pela primeira vez para a máquina virtual Java do servidor,
o método init() é invocado, para preparar recursos para a execução do serviço ou para estabelecer conexão com outros serviços.
III. Estando o servlet pronto para atender as requisições dos clientes, o container cria um objeto de requisição (ServIetRequest) e de resposta (ServIetResponse) e depois chama o método serviceQ, passando os objetos como parâmetros.
IV. O método destroyO permite liberar os recursos que foram utilizados, sendo invocado quando o servidor estiver concluindo sua atividade.
Está correto o que se afirma em:

a) I, II e III, apenas.

b) I, II e IV, apenas.

c) I, III e IV, apenas.

d) II, III e IV, apenas e) I, II, III e IV.
5. (FCC - 2013 - DPE/SP - Analista de Sistemas) Um Servlet Contêiner controla o ciclo de vida de uma servlet onde são invocados três métodos essenciais: um para inicializar a instância da servlet, um para processar a requisição e outro para descarregar a servlet da memória. Os itens a seguir representam, nessa ordem, o que ocorre quando um usuário envia uma requisição HTTP ao servidor:
I. A requisição HTTP recebida pelo servidor é encaminhada ao Servlet Contêiner que mapeia esse pedido para uma servlet específica.
II. O Servlet Contêiner invoca o método init da servlet. Esse método é chamado em toda requisição do usuário à servlet não sendo possível passar parâmetros de inicialização.
III. O Servlet Contêiner invoca o método service da servlet para processar a requisição HTTP,
passando os objetos request e response. O método service não é chamado a cada requisição, mas apenas uma vez, na primeira requisição do usuário à servlet.
IV. Para descarregar a servlet da memória, o Servlet Contêiner chama o método unload, que faz com que o garbage collector retire a instância da servlet da memória.
Está correto o que se afirma em:

a) I, II, III e IV.

b) I, apenas.

c) I e IV, apenas.

d) II, III e IV, apenas.

e) II e III, apenas.

6. (FCC - 2006 - BACEN - Analista de Sistemas) Para ser um servlet, uma classe deve estender a classe I e exceder as ações "doGet" ou "doPost" (ou ambas), dependendo se os dados estão sendo enviados por uma ação GET ou por uma ação POST. Estes métodos tomam dois argumentos: um II e um III em sua execução. Preenchem correta e respectivamente I,II e III:

I

A HttpJspServIet

B JspServIet

II

XmIHttpServIet
HttpServIetResponse

III

Xml HttpServIetResponse
HttpServIetRequest

C HttpSen/letRequest

Xm I HttpServIetRquest Xml HttpServIetResponse

D HttpServIet

E HttpServIet

HttpServIetRequest
HttpServIetRequest

HttpServIetResponse
HttpServIetResponse.write

7. (FCC - 2007 - TRE-SE - Analista Judiciário - Tecnologia da Informação) Em Java, a passagem de dados de um formulário do cliente para o servlet pode ocorrer por meio do uso do método:
a) importO

b) return()

c) catch()

d) getParameterO

e) nameComponentO

8. (FCC - 2012 - TRE-CE - Programador de computador) A tecnologia Java Servlet é baseada na construção de classes servlet que executam no servidor recebendo dados de requisições do cliente, processando esses dados, opcionalmente acessando recursos externos como bancos de dados, e respondendo ao cliente com conteúdo no formato HTML.
Com relação ao tema, analise as asserções a seguir:

Embora as servlets sejam muito boas no que fazem, tornou-se difícil responder ao cliente com conteúdo no formato HTML.
PORQUE

Geralmente quem trabalha com o conteúdo HTML é o web designer que normalmente não é programador Java experiente. Ao misturar HTML dentro de uma servlet, torna-se muito difícil separar as funções de web designer e desenvolvedor Java. Além disso, é difícil fazer alterações no conteúdo HTML, pois para cada mudança, uma recompilação da servlet tem que acontecer.Para contornar as limitações da tecnologia Java Servlet a Sun Microsystems criou a tecnologia
JavaServer Pages (JSP).

Acerca dessas asserções, é correto afirmar:

a) Tanto a primeira quanto a segunda asserções são proposições falsas.

b) A primeira asserção é uma proposição verdadeira e a segunda uma proposição falsa.

c) A primeira asserção é uma proposição falsa e a segunda uma proposição verdadeira.

d) As duas asserções são proposições verdadeiras, mas a segunda não é a justificativa correta da primeira.
e) As duas asserções são proposições verdadeiras e a segunda é a justificativa correta da primeira.

9. (FCC - 2013 - AL-RN - Analista Legislativo - Analista de Sistemas) No Java EE 6 os métodos doPost e doGet podem ser sobrescritos em uma servlet criada na aplicação para receberem as requisições vindas de páginas HTML. Quando sobrescritos na servlet, eles substituem seus métodos ancestrais existentes na classe abstrata:
a) GenericServIet.

b) HttpServIet.

c) HttpServIetRequest.

d) HttpServIetResponse.

e) HttpServIetObject.

10.(FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da Informação) Para ler os parâmetros de inicialização do contexto de um servlet utiliza-se o método:
a) String getlnitParameter(String).

b) Enumeration getlnitParameterNames().

c) InputStream getResourceAsStream().

d) setAttribute(String nome, Object).

e) Object getAttribute(String nome).

11.(FMP/RS - 2013 - MPE/AC - Analista de Sistemas) No contexto da arquitetura Java
Enterprise Edition, são, em termos de estrutura, classes
Java especializadas que se assemelham muito à estrutura dos applets Java, porém rodando em um servidor web e não no do cliente.
Assinale a única alternativa que completa corretamente a lacuna acima.

a) Java ME (Java Micro Edition)

b) portlets c) Java Persistence API (JPA)
d) Enterprise JavaBeans (EJB)

e) servlets

12.(VUNESP - 2013 - FUNDUNESP - Analista de Sistemas) Na plataforma J2EE, a classe
ServIetRequest define:

a) a estrutura do objeto principal do Servlet, permitindo que sejam feitas requisições ao Servlet.

b) métodos que permitem que o Servlet faça requisições de forma assíncrona.

c) métodos que permitem que o Servlet faça requisições aos clientes.

d) propriedades que permitem que seja alterado o comportamento do Servlet.

e) um objeto que fornecerá informações sobre a requisição feita pelo cliente ao Servlet.

13.(CESGRANRIO - 2006 - DECEA - Analista de Sistemas - A) Servlets e arquivos JSP são executados no WEB Container.
14.(CESGRANRIO - 2006 - DECEA - Analista de Sistemas - B) Applets e Servlets são compilados e executados no servidor.
15.(CESGRANRIO - 2009 - BNDES - Analista de Sistemas - A) Ao estudar as especificações e frameworks Java EE, um Analista de Sistemas concluiu que o container WEB do servidor de aplicações é o responsável por gerenciar o ciclo de vida de servlets e de EJBs utilizados numa aplicação Java.
16.(CESGRANRIO - 2009 - BNDES - Analista de Sistemas - B) Ao estudar as especificações e frameworks Java EE, um Analista de Sistemas concluiu que no container WEB, uma páginaJSP transforma-se em um servlet, que é compilado, carregado e inicializado.

17.(CESGRANRIO - 2012 - PETROBRÁS - Analista de Sistemas) Seja o código a seguir:

public class Servletl extends HttpServlet {

protected void processRequest(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {

response. setContentType ("text/html; charset=UTF-8");
PrintWriter out = response.getWriter();

try {

out.println("<html><body>Meu Servlet</body></html>") ;

} finally {

out.close();

}

}

@0verride protected void doGet(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException {

processRequest(request, response);

}

@0verride protected void doPost(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException {

processRequest(request, response);

}

}

Sobre esse código, do qual foram omitidas as declarações de importação e o método getServIetlnfo por concisão, considere as afirmativas a seguir.
I - Como o método service() não foi redefinido, o container não saberá qual método chamar para cada tipo de pedido, gerando uma exceção.
II - Como o método init() não foi redefinido, o construtor padrão da classe mãe será chamado.

III - Como o método destroyO não foi redefinido, o container gerará um erro registrando-o no arquivo de logs ao terminar este aplicativo.
É correto APENAS o que se afirma em:

a) I

b) II

c) III

d) I e III

e) II e III

1 import java.io.*; import javax.servlet.*; import javax.servlet.http.*;

2 public class BookStoreServlet extends HttpServlet {

3 public void service (HttpServletRequest request,

4 HttpServletResponse response)

5 throws ServletExceptionr IOException {

6 // Get the dispatcher; it gets the main page to the user

7 RequestDispatcher dispatcher =

8 getServletContext().getRequestDispatcher(

9 "/bookstore/bookstore.html ") ;

10 if (dispatcher = null) {

11 System. out.println("There was no dispatcher");

12 // No dispatcher means the html file could not be found.

13 response.sendError(response.SC_NO_CONTENT);

14 } else {

15 System.out.println("There is a dispatcher");

16 // Get or start a new session for this user

17 HttpSession session = request.getSession();

18 // Send the user the bookstore's opening page

19 dispatcher.forward(requestr response);

20 }

21 }

22 public String getServletlnfo() {

23 return "The Bookstore servlet returns the main web page " +

24 "for Duke's Bookstore.";

25 }

26 }

18.(ESAF - 2008 - CGU - Analista de Sistemas - A) Servlets são classes de programação Java que geram conteúdo dinâmico (normalmente para páginas HTML) e interagem com os clientes, utilizando o modelo challenge/request. Normalmente utilizam o protocolo HTTP,apesar de não serem restritas a ele.

19.(CIAAR - 2012 - CIAAR - Oficial Temporário - Análise de Sistemas) O método chamado para liberar quaisquer recursos mantidos pelo servlet, quando o contêiner de servlets termina o servlet, denomina-se:
a) get.

b) post.

c) destroy.

d) prerender.

20.(AOCP - 2012 - BRDE - Analista de Sistemas - Desenvolvimento de Sistemas - (Prova TIPO
4)) Sobre Servlets, analise as assertivas e assinale a alternativa que aponta as corretas.

I. Servlets são implementadas como arquivos de classe da Linguagem Java.

II. Servlets são independentes de plataforma, de modo que podem ser executadas em diferentes servidores, em diferentes sistemas operacionais.
III. As Servlets podem acessar qualquer uma das APIs Java. Uma Servlet pode usar a API JDBC
para acessar e armazenar dados ou para acessar objetos remotos.

IV. Ao criar uma Servlet, somos obrigados a reescrever nove métodos presentes à interface que foi implementada.
a) Apenas I e II.

b) Apenas I e III.

c) Apenas II e III.

d) Apenas I, II e III.

e) I, II, III e IV.

21.(VUNESP - 2013 - FUNDUNESP - Analista Programador Júnior) Para criar um Servlet que processará as requisições HTTP na plataforma J2EE, deve-se:
a) criar uma classe que implemente a interface Servlet.

b) criar uma classe que estenda a classe HttpServIet.

c) implementar o método processHttpHeader.

d) instanciar a classe Servlet, passando para o parâmetro requestType o valor
Servlet.HTTP_REQUEST.

e) invocar o método Servlet.service(Servlet.HTTP_REQUEST) antes do processamento da requisição.
22.(FEPESE - 2013 - JUCESC - Analista Técnico em Gestão de Registro Mercantil - Analista de
Informática) Assinale a alternativa que defne corretamente um Servlet.

a) É um método da JPA utilizado na persistência assíncrona de dados.

b) É um componente que roda do lado do cliente para tratar problemas de comunicação.

c) É uma classe Java utilizada para estender as capacidades de um servidor.

d) É uma biblioteca JBOSS que emula servidores no lado do cliente.

e) É uma JSP que possibilita a execução de código no lado do cliente, mesmo sem comunicação com um servidor.
23.(VUNESP - 2013 - FUNDUNESP - Analista Programador Júnior) Considere o Servlet a seguir:

import java.io.*;
import javax.servlet.*;

import javax.servlet.http.*;

public class ClasseServIet extends HttpServIet {

public void doGet(HttpServletRequest request,
HttpServIetResponse response){
response.write("<html>");
response.write("<body>");
response.write("Servlet em operação!");
response.write("</body>");
response.write("</html>");

}

}

Sobre o código do Servlet, é possível afirmar que:

a) ao ser executado por um contêiner de Servlet, será exibida uma tela em branco no navegador.

b) ao ser executado por um contêiner de Servlet, será exibida a mensagem "Servlet em operação!"
na tela do navegador.

c) não pode ser compilado, pois a classe HttpServIetResponse não possui o método write.

d) não pode ser compilado, pois HttpServIet é uma interface e, portanto, não pode ser estendida por uma classe.
e) o conteúdo exibido na tela do navegador não será codificado corretamente, pois a codificação da página não foi informada.
24.(CESGRANRIO - 2008 - TJ-RO - Analista Judiciário - Tecnologia da Informação) O método da interface javax.servlet.http.HttpSession, utilizado para finalizar uma sessão de usuário em um container J2EE, é a) cancel()
b) delete()

c) destroy()

d) invalidate()

e) release()

GABARITo

GABARITO

1. B 11. E 21. B

2. A 12. E 22. C

3. A 13. C 23. C

4. E 14. E 24. D

5. B 15. E

6. D 16. C

7. D 17. B

8. E 18. E

9. B 19. C

10. A 20. D

JAVA SERVER FACES (JSF)

Galera, vou contar uma historinha para vocês! Durante muito tempo, usuários se acostumaram com Aplicações Desktop. O que é isso, professor? É aquele programinha que você baixa e instala em seu computador local, acessando diretamente bancos de dados ou gerenciadores de arquivos.Para criar essas aplicações eram utilizadas as tecnologias Visual Basic, Delphi, Swing (Java), etc.

Pois é, esses programas em geral não necessitam de um navegador para rodar!
Eles são construídos como um conjunto de componentes oferecidos pela plataforma de desenvolvimento para cada sistema operacional e estão associados a eventos, ações ou procedimentos que executam lógicas de negócio. Muitas das vezes, são componentes muito ricos.
No entanto, sabe-se que Aplicações Desktop sofrem com problemas de manutenção e gerenciabilidade. Vejam que as regras de negócio rodam no cliente - aliás, uma cópia integral da aplicação está no cliente! Logo, se deu pau em alguma funcionalidade, eu tenho que propagar as alterações para todas as máquinas que têm o programa, visto que as regras de negócio estão no cliente!
Para resolver esse tipo de problema, surgiram as Aplicações Web. Elas rodam em um servidor central onde os usuários podem acessá-las por meio de um navegador (Chrome, Firefox,etc) e um protocolo HTTP. Nesse caso, todas as regras de negócio da aplicação se encontram noServidor,
sendo muito mais fácil gerenciá-las e, eventualmente, depurá-las.

Ora, deu pau em alguma funcionalidade, eu vou lá no servidor central e conserto -
não preciso ir em todas as máquinas que têm a aplicação! Claro, nem tudo são flores, é necessário conhecer diversas tecnologias, linguagens, scripts, entre outros - além de seguir um modelo de requisição/resposta. Agora vejam que interessante, eu posso combinar esses dois universos.
É possível unir as melhores características desses dois mundos, com componentes ricos,abstraindo protocolos, etc. Vocês já ouviram falar da Arquitetura
Model-View-Controller (MVC)?
Pois é, trata-se de uma arquitetura que divide os componentes de uma aplicação em camadas independentes (Modelo, Visão e Controle)! O Controle faz o meio campo entre a Visão e oModelo.

Bem, ela foi amplamente utilizada em Aplicações Desktop até que um dia alguém pensou:
Poxa,
por que não utilizá-la na web? E resolveu assim fazê-lo! Como assim? Alguém decidiu então combinar a Arquitetura MVC com o modelo tradicional de desenvolvimento de páginas web dinâmicas! Qual seria esse modelo, professor? Trata-se da utilização de Servlets e JSP!
O resultado foi a criação do framework Struts! Ele era uma implementação da
Arquitetura MVC
para desenvolvimento de páginas web dinâmicas! Bacana? Esse framework fez tanto sucesso que a Sun Microsystems junto com uma comunidade de desenvolvedores resolveu criar uma especificação padronizada baseada nesse framework, denominado Java Server Faces (JSF).
Cuidado com as questões de prova que afirmam que se trata apenas de uma especificação
- ele é tanto uma especificação quanto um framework* 1. Cuidado também com aquelas que afirmam que só trata de interfaces gráficas. Ele trata de componentes de interface com usuário - as interfaces gráficas (GUI) são um tipo de interface com o usuário (UI). Essa tecnologia consiste em dois aspectos:
Primeiro, uma API para representar componentes e gerenciar seus estados;
manipular eventos;
realizar validação server-side; converter dados; definir navegação de páginas; suportar internacionalização e acessibilidade; e prover extensibilidade. Segundo, taglibs(bibliotecas de tags) para adicionar componentes a páginas web e conectar componentes a objetos server-side.
Galera, ele provê um modelo de programação bem definido e robusto, além de fornecer diversas taglibs - inclusive o desenvolver pode criar sua própria taglib. Essas taglibs contêm manipuladores de tags que implementam os componentes de tags. Essas características facilitam significativamente o peso da construção e manutenção de Aplicações Web com interfaces de usuário server-side.
O Modelo de Componentes JSF define três taglibs:

HTML: possui componentes que representam diversos elementos HTML.
o Namespace: xmlns:h = "http://java.sun.com/jsf/html"

CORE: responsável por internacionalização, validação, conversão e outros.
o Namespace: xmlns:f="http://java.sun.com/jsf/core"

FACELETS: fornece tags para criar templates para aplicações web.
o Namespace: xmlns:ui="http://java.sun.com/jsf/facelets"

Com o mínimo de esforço é possível criar uma página web; adicionar componentes em uma página ao adicionar tags de componentes; vincular componentes de uma página a dados server-side;conectar eventos gerados por componentes ao código da aplicação; salvar e restaurar o estado da aplicação além da vida da requisição do servidor; e reutilizar e estender componentes por meio de customização.
Podemos definir a Tecnologia JSF como uma tecnologia que nos permite criar Aplicações
Web utilizando componentes visuais pré-prontos, de forma que o desenvolvedor não se procupe comJavascript ou HTML. A funcionalidade fornecida por uma Aplicação JSF é similar a qualquer outraAplicação Web. Ela possui as seguintes partes:

* Um conjunto de Páginas Web em que são colocados os componentes;

* Um conjunto de tags para adicionar componentes à página web;

1 As implementações da especificação mais famosas são Oracle Mojarra e o Apache MyFaces.

* Um conjunto de Managed Beans (ou Beans Gerenciados);

* Um Descritor de Implantação Web (web.xml);

* Um ou mais arquivos de configuração (Ex: faces-config.xml);

* Um conjunto de objetos customizados (Ex: validadores, conversores, etc);

* Um conjunto de tags customizadas para representar objetos customizados;

Pessoal, o JSF oferece diversos validadores embutidos para validar seus Componentes UI
- essa validação ocorre no lado do servidor. Eles podem ser invocados a partir de sua tag específica e podem validar o tamanho de um campo, tipo de entrada, range de um valor numérico,expressão regular, entre outros. É possível, inclusive, criar o seu próprio validador customizado.
Browser

WebContainer myfacelet.xhtml
Access page
(HTTP Request)

ji

Generates
Gomponent
Tree

Renders HTML
(HTTP Response)

myVieíw

Observem a imagem acima! Uma Página Web myfacelet.xhtml é construída utilizando tags deComponentes JSF. Essas tags são usadas para adicionar componentes à visão (myView), que é uma representação server-side da página. Além dos componentes, uma página web pode referenciar objetos como listeners, validadores, conversores, entre outros.
Em resposta a uma requisição do cliente, uma página web é renderizada por um contêiner web que implementa a tecnologia JSF! Uma de suas grandes vantagens é que ele oferece uma clara separação entre comportamento e apresentação. Ele mapeia solicitações HTTP para o tratamento de eventos específicos dos componentes e gerencia os componentes como objetos stateful no servidor.
Outro importante objetivo é aproveitar componentes e conceitos já familiares aos programadores,sem limitá-los a uma tecnologia de script ou a uma linguagem de marcação específicas. Isso possibilita a utilização de diferentes tecnologias de apresentação, a criação de componentes próprios a partir das classes de componentes, e a geração de saídas para diversos dispositivos (Ex:Celular, Tablet).

O JSF fornece uma maneira fácil e amigável para criar Aplicações Web por meio de,
basicamente,

três atividades:

* Criar uma Página Web (usando tags de componentes);

* Desenvolver Managed Beans;

* E mapear a instância FacesServIet.

Aqui vamos fazer uma pequena pausa! Professor, o que é um Managed Bean? São apenas
POJOs com a annotation @ManagedBeans. Pensem no seguinte: meu sistema precisa escrever "Olá,pessoal" no navegador. Bem, esse texto não precisa de nenhuma informação, não acessa nada, é muito simples - basta colocá-lo diretamente na camada de visão e mostrá-lo!
E se eu tenho que dar um "Olá, X", em que X é o nome da pessoa que acessou o sistema? Em outras palavras, se eu acessei, deve mostrar "Olá, Diego"; se o Messi acessou, deve mostrar "Olá,Messi"! Para tal, eu vou precisar acessar o banco de dados, buscar informações do sistema, talvez saber o horário de acesso, i.e., vou precisar interagir com o modelo,lógica de negócio ou componentes visuais.
Ora, nós prezamos pela separação de responsabilidades! Logo, esse código ficará em uma classe de modelo e, jamais, na visão. Os Managed Beans são os objetos que intermediam a comunicação entre a visão e o modelo. Eles são registrados no descritor de implantação(ou por meio de annotations) e tem seu ciclo de vida controlado e gerenciado pelo próprio JSF!
As principais tarefas de um Managed Bean (ou Backing Beans) é fornecer dados que serão exibidos nas telas; receber dados enviados nas requisições; executar tarefas de acordo com as ações dos usuários; validar dados. E o que seria a FacesServIet? É uma servlet que gerencia o ciclo de vida do processamento de requisições de aplicações web que estão utilizandoJSF para construir a interface com o usuário.
Elas são responsáveis por receber as requisições da View, redirecioná-las para os
Managed Beans do Model e respondê-las. Devemos configurá-la no descritor de implantação web.xml das aplicações web - ele faz a conexão entre Web Container e Web Application. Após isso,devemos configurar também o arquivo de configuração faces-config.xml, referente a uma aplicação específica que utiliza JSF.
Ele é responsável por descrever e configurar elementos e subelementos que compõem o projeto,tais como conversores, managed beans, validadores, fluxo da comunicação,
configurações de localização e o mapeamento da navegação - ademais, ele faz a conexão entre View eController.
Vamos resumir essa diferença entre esses dois arquivos?

O faces-config.xml é mais específico, tratando de regras e mapeamento de navegação;
definição de managed beans; configuração de detalhes de internacionalização; entre outros. Já o web.xml é mais genérico, tratando da especificação de detalhes de segurança; configuração de páginas de erro; mapeamento e declaração de servlets e filtros; configuração de parâmetros de inicialização;entre outros.

O faces-config.xml tem sido rapidamente substituído por annotations - novidade do JSF
2.0. Essa versão trouxe: suporte a facelets; utilização de templates para a aplicação;simplificação do desenvolvimento de componentes; suporte nativo a Ajax (f:ajax); navegação implícita e condicional; suporte ao Método GET; adição de novos escopos (Flash e View);composição de componentes customizados; etc.
,

O JSF1 tinha os escopos Request (Default), Session e Application. A partir do JSF2,
ganhamos o
View, Flash, None e Custom. O @RequestScoped vive o tempo do ciclo de umaRequisição/Resposta HTTP; o @ViewScoped vive enquanto houver interação com a mesma view,
i.e., enquanto persistir a mesma página; o @ApplicationScoped persiste toda a duração da aplicação web.
O @SessionScoped persiste o tempo que durar uma sessão, i.e., até invocar um método inválido ou o tempo acabar (lembrar de um carrinho de compras); o@FlashScoped dura um redirecionamento de página; o @NoneScoped indica que o escopo não está definido para a aplicação; por fim, o @CustomScoped é um escopo personalizado.
I 1

ENTIDADES

REPDSITÚRIDS

Agora eu queria falar uma curiosidade interessante! Existe um Padrão de Projeto Java
EE chamado
Front Controller. Nesse padrão, todas as requisições do usuário são recebidas pelo mesmo componente. Dessa forma, tarefas que devem ser realizadas em todas as requisições podem ser implementadas por esse componente - evitando repetição de código e facilitando a manutenção do sistema.
No JSF, esse componente é o FacesServIet! Como mostra a imagem da estrutura geral de umaAplicação JSF, o processamento de uma requisição enviada por um navegador começa naFacesServIet. Observem que ela controla a execução das seis etapas do ciclo de vida,
interagindo com o Model (Entidades e repositórios) e com as Views (Telas, Templates, etc).
Os Managed Beans estão à disposição da FacesServIet durante todo o processamento da requisição. Nas etapas Render Response e Restore View, a ela aciona os Managed Beans para recuperar os dados que devem ser usados na construção ou reconstrução da árvore de componentes. Na etapa Update Model, a FacesServIet armazena nos Managed Beans os dados já convertidos e validados.
Na etapa Invoke Application, a FacesServIet dispara um método em um
Managed Bean responsável pelo processamento da regra de negócio correspondente à requisição atual. Todas as regras de negócio são implementadas no modelo, que também administra os dados da aplicação. Os Managed Beans acionam o modelo para executar regras de negócio,recuperar dados administrados pelo modelo, etc.
As telas da aplicação são definidas na camada de visão. A FacesServIet acessa essa camada toda vez que necessita construir ou reconstruir a árvore de componentes de uma determinada tela. Isso ocorre nas etapas Restore View e Render Response. Aliás, vamos ver agora rapidamente -porque não cai muuuuito em provas - o ciclo de vida do JSF! Ele é apresentado na imagem abaixo:
Render Response

Pelo fato do framework JSF ser talvez uma evolução da linguagem JSP, o ciclo de vida do JSF é parecido com o do JSP. Por exemplo, quando o cliente faz uma Requisição HTTP para a página,o servidor responde com a página traduzida para HTML. Porém, ele é dividido em múltiplas fases,apresentando um modelo de componentes de interface com usuário mais sofisticado.

Restore View: restauram-se os objetos e estruturas de dados que representam a visão. Claro,se essa for a primeira visita à página, deve-se criar a visão. Quando o JSF cria e renderiza uma página JSF, ele cria objetos de interface com o usuário para cada componente da visão. Os componentes são armazenados em uma árvore de componentes e o estado da visão é salvo para requisições futuras.
Apply Request Values: qualquer dado que for enviado como parte da requisição é passado para os componentes apropriados. Essas visões atualizam seus estados com os valores dos
/ 235

/

dados. Dados podem vir de formulários, cookies enviados com a requisição ou por meio de cabeçalhos da requisição. Alguns dados são validados e, se houver erro, são adicionados àFacesServIet.

Process Validation: os dados que foram submetidos com o formulário são validados
(se já não o foram anteriormente). Assim como na fase anterior, isso ainda não atualiza os objetos de negócio na aplicação. Isso ocorre porque, se a Aplicação atualizar os objetos de negócio junto com a validação dos dados e uma parte da validação falhar, o modelo será atualizado com um estado inválido.
Update Model Values: após todas essas validações terminarem, os objetos de negócio que criam a aplicação são atualizados com os dados validados da requisição. Ademais, se qualquer um dos dados precisar ser convertido em um formato diferente para atualizar o modelo(Ex:
String para Data), a conversão ocorrerá nessa fase.

Invoke Application: durante essa fase, os métodos de ação de qualquer botão ou link que foi ativado serão chamados. Além disso, todos os eventos que foram gerados durante as fases anteriores e que ainda não tenham sido manipulados são passados para a Aplicação Web para que ela possa concluir qualquer outro processamento da requisição que seja necessário.
Render Response: os Componentes UI de resposta são renderizados e a resposta é enviada para o cliente. O estado dos componentes é salvo de modo que a árvore de componente possa ser restaurada quando o cliente enviar outra requisição. Em suma, essa fase renderizará a página de resposta requisitada pelo usuário.
Lembrando que FacesContext (javax.faces.context) é o objeto utilizado para representar todas as informações de contexto associadas ao processamento da requisição de entrada e à criação da resposta correspondente. Ela é criada pela FacesServIet, que é executada antes do início do ciclo de vida de processamento de requisições e é responsável por gerenciar a execução das etapas do ciclo de vida.
Vamos falar um pouquinho sobre Component Binding! O que é isso, professor? Cara, essa é uma nova característica da tecnologia JSF que permite associar componentes de uma view e controlar todos os aspectos desse componente. Como assim? Algumas vezes, nós temos um componente visual que nos oferece alguma informação (Ex: um mapa em que o usuário escolhe estado).
Bem, em geral, nós necessitamos apenas do valor, i.e., o usuário escolheu 'DF'. O
Component
Binding permite que nós tenhamos acesso ao componente como um todo. Para que? Nós,eventualmente, podemos querer manipular o componente dinamicamente, por exemplo.
Assim,
é possível acessar métodos do componente - se você quiser, pode até mudar seu comportamento.

JSF: Faceletes

Pessoal, tem uma característica do JSF que é extremamente importante: Facelets!
Trata-se de uma linguagem de declaração de página poderosa, apesar de leve. Antigamente, utiliza-se a tecnologia JSP como camada de visão do JSF, porém ele não suporta todas as características disponíveis na Plataforma Java EE - sendo considerada obsoleta para JSF!
Facelets é uma parte da especificação JSF e também a tecnologia de apresentação preferida para construir aplicações JSF - substituindo JSP. Ela suporta todos os componentes de UI doJSF e constrói Árvores de Componentes; e Views (utilizando Templates HTML). Um tipo especial de template são os Componentes Compostos, que agem como um componente. Ademais,é bom destacar algumas características:
* Utilização de XHTML para criação de Páginas Web;

* Suporte a Facelets Tag Libraries (além do JSFTL e JSTL);

* Suporte a Linguagens de Expressão (Expression Languages);

* Suporte a templates para componentes e páginas.

Em suma, a utilização de Facelets reduz o tempo e esforço gastos no desenvolvimento e implantação. Em geral, Facelets Views são criadas com Páginas HTML e XHTML(criadas em conformidade com Transation DTD). Além disso, elas utilizam linguagens de expressão para referenciar propriedades e Managed Beans. Para desenvolver uma Aplicação Facelets simples, é necessário:
* Desenvolver um Managed Bean;

* Criar páginas usando tags de componentes;

* Definir a navegação das páginas;

* Mapear a instância javax.faces.webapp.FacesServIet;

* Adicionar declarações de Managed Beans.

JSF: Filtros

Em JSF, um Filtro (do inglês, Filter) é um objeto capaz de realizar tarefas de filtragem tanto na requisição de um recurso (Servlet ou conteúdo estático), ou na resposta desse recurso,ou ambos

- para tal, eles utilizam o método doFilter. Todo Filtro possui acesso a um objeto
FilterConfig, do qual ele pode obter seus parâmetros de inicialização; e a uma ServIetContext, do qual ele pode carregar recursos.
Os Filtros são configurados nos descritores de implantação de uma Aplicação Web. Ele possibilita o gerenciamento de todas as Requisições HTTP do Servidor, capaz de filtrar o endereço que está sendo acessado. Dessa forma, quando um usuário acessar uma determinada URL proibida,pode-
se imediatamente redirecioná-lo para outro endereço, antes que a resposta seja dada ao cliente.

Para tal, deve-se implementar a interface javax.servlet.Filter! Existem dezenas de aplicações para filtros, além da mostrada acima. Podemos ter filtros de autenticação; filtros de log e auditoria;filtros de conversão de imagens; filtros de compressão de dados; filtros de criptografia; filtros de tokenização; filtros XSLT; filtros que acionam eventos de acesso a recursos, entre outros.
/ 235

/

QUESTõES CoMENTADAS - JSF - MULTIBANCAS

1. (FCC - 2013 - TRT/12 - Analista de Sistemas) Considere as instruções abaixo encontradas em um arquivo de uma aplicação que utiliza JSF:
<managed-bean>

<managed-bean-name>func</managed-bean-name>

<managed-bean-class>bean.Funcionario</managed-bean-class>

<managed-bean-scope>session</managed-bean-scope>

</managed-bean>

Essas instruções indicam a existência de um bean gerenciado (classe Funcionario.java) no pacote bean que poderá ser referenciado nas páginas JSP por meio da palavra func. Oarquivo correto no qual essas instruções são colocadas é o:

a) context.xml.

b) web-inf.xml.

c) web.xml.

d) faces-config.xml.

e) config-bean.xml.

Comentários:

Elas são responsáveis por receber as requisições da View, redirecioná-las para os
Managed
Beans do Model e respondê-las. Devemos configurá-la no descritor de implantação web.xml das aplicações web - ele faz a conexão entre Web Container e Web Application. Após isso,devemos configurar também o arquivo de configuração faces-config.xml, referente a uma aplicação específica que utiliza JSF.
Conforme vimos em aula, o responsável é o faces-config.xml. Gabarito: D

2. (CESPE - 2009 - SECONT-ES - Auditor do Estado - Tecnologia da Informação) O JSF
é um framework web embasado em interface gráfica, capaz de renderizar componentes e manipular eventos em aplicações web no padrão Java EE, no qual os componentes JSFsão orientados a eventos. O JSF fornece, ainda, mecanismos para conversão, validação,
execução de lógica de negócios e controle de navegação.

Comentários:

Primeiro, uma API para representar componentes e gerenciar seus estados;
manipular eventos;
realizar validação server-side; converter dados; definir navegação de páginas; suportar internacionalização e acessibilidade; e prover extensibilidade. Segundo, taglibs(bibliotecas de tags) para adicionar componentes a páginas web e conectar componentes a objetos server-side.
/ 235

/

Conforme vimos em aula, a questão está perfeita! Gabarito: C

3. (FCC - 2012 - TJ-PE - Programador de computador) Em uma aplicação que utiliza
JSF,
para configurar o fluxo de comunicação presente na servlet de controle, é utilizado um arquivo de configuração:
a) webfaces.xml.

b) actionform.xml.

c) faces-config.xml.

d) webcontext.xml.

e) serverconfig.xml.

Comentários:

Elas são responsáveis por receber as requisições da View, redirecioná-las para os
Managed
Beans do Model e respondê-las. Devemos configurá-la no descritor de implantação web.xml das aplicações web - ele faz a conexão entre Web Container e Web Application. Após isso,devemos configurar também o arquivo de configuração faces-config.xml, referente a uma aplicação específica que utiliza JSF.
Ele é responsável por descrever e configurar elementos e subelementos que compõem o projeto, tais como conversores, managed beans, validadores, fluxo da comunicação,configurações de localização e o mapeamento da navegação - ademais, ele faz a conexão entreView e Controller. Vamos resumir essa diferença entre esses dois arquivos?

Conforme vimos em aula, trata-se do faces-config.xml. Gabarito: C

4. (CESPE - 2010 - TRE-BA - Analista Judiciário - Análise de Sistemas) Entre os itens que o padrão Java Server Faces (JSF) utiliza, estão os componentes, os eventos e a navegabilidade.
Comentários:

Primeiro, uma API para representar componentes e gerenciar seus estados;
manipular eventos;
realizar validação server-side; converter dados; definir navegação de páginas; suportar internacionalização e acessibilidade; e prover extensibilidade. Segundo, taglibs(bibliotecas de tags) para adicionar componentes a páginas web e conectar componentes a objetos server-side.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

5. (FCC - 2013 - TRT/9 - Analista de Sistemas) Uma aplicação utilizando o framework
JSF e a IDE NetBeans gera automaticamente dois componentes essenciais assim descritos:
,

I. É responsável por receber requisições dos componentes View do MVC, redirecioná-las para os beans gerenciados (managed beans) do componente Model do MVC e responder a essas requisições.
II. É o arquivo principal de configuração de uma aplicação web que utiliza o frameworkJSF. É responsável por descrever os elementos e sub-elementos que compõem o projeto,
tais como as regras de navegação, beans gerenciados, configurações de localização etc.

As descrições I e II referem-se, respectivamente, aos componentes:

a) servlet Controller.java e ao arquivo faces_config.xml b) FaceletServIet e ao arquivo web_config.xml.
c) FacesServIet e ao arquivo faces-config.xml.

d) servlet Controller e ao arquivo web-config.xml.

e) servlet Facelet e ao arquivo web.xml.

Comentários:

Elas são responsáveis por receber as requisições da View, redirecioná-las para os
Managed
Beans do Model e respondê-las. Devemos configurá-la no descritor de implantação web.xml das aplicações web - ele faz a conexão entre Web Container e Web Application. Após isso,devemos configurar também o arquivo de configuração faces-config.xml, referente a uma aplicação específica que utiliza JSF.
Ele é responsável por descrever e configurar elementos e subelementos que compõem o projeto, tais como conversores, managed beans, validadores, fluxo da comunicação,configurações de localização e o mapeamento da navegação - ademais, ele faz a conexão entreView e Controller. Vamos resumir essa diferença entre esses dois arquivos?

Conforme vimos em aula, o primeiro é o FacesServIet e o segundo faces-config.xml.
Gabarito:
C

6. (CESPE - 2012 - ANAC - Analista Administrativo - Área 4) A validação de dados de um componente pode ser uma das funções de um backing bean, em uma aplicação JSF.
Comentários:

As principais tarefas de um Managed Bean (ou Backing Beans) é fornecer dados que serão exibidos nas telas; receber dados enviados nas requisições; executar tarefas de acordo com as ações dos usuários; validar dados. E o que seria a FacesServIet? É uma servlet que gerencia o ciclo de vida do processamento de requisições de aplicações web que estão utilizando JSFpara construir a interface com o usuário.

Conforme vimos em aula, Backing Beans são Managed Beans, e essa pode ser uma de suas funções. Gabarito: C
/ 235

/

7. (FCC - 2012 - TST - Analista de Sistemas) O framework JavaServer Faces
(JSF) é utilizado no desenvolvimento de aplicações web que utiliza o design pattern MVC. O JSF:
a) disponibiliza controles pré-construídos e código para manipular eventos, estimulando o uso de código Java convencional no componente View do MVC.
b) recebe requisições dos componentes da View do MVC, através do servlet FaveServerServIet.

c) armazena os mapeamentos das ações e regras de navegação em projetos JSF nos arquivosWEB-INF.xml e FACES-CONFIG.xml.

d) possui bibliotecas que suportam Ajax (Asynchronous JavaScript And XML).

e) provê um conjunto de tags limitado para criar somente páginas HTML/XHTML.

Comentários:

Ora, nós prezamos pela separação de responsabilidades! Logo, esse código ficará em uma classe de modelo e, jamais, na visão. Os Managed Beans são os objetos que intermediam a comunicação entre a visão e o modelo. Eles são registrados no descritor de implantação(ou por meio de annotations) e tem seu ciclo de vida controlado e gerenciado pelo próprio JSF!
(a) Conforme vimos em aula, está incorreto, i.e., é desestimulado colocar código convencional(regras de negócio) na View, mas - sim - no Model.

Elas são responsáveis por receber as requisições da View, redirecioná-las para os
Managed
Beans do Model e respondê-las. Devemos configurá-la no descritor de implantação web.xml das aplicações web - ele faz a conexão entre Web Container e Web Application. Após isso,devemos configurar também o arquivo de configuração faces-config.xml, referente a uma aplicação específica que utiliza JSF.
(b) Conforme vimos em aula, de fato recebe requisições dos componentes da View, no entanto o nome da servlet é FacesServIet.
Elas são responsáveis por receber as requisições da View, redirecioná-las para os
Managed
Beans do Model e respondê-las. Devemos configurá-la no descritor de implantação web.xml das aplicações web - ele faz a conexão entre Web Container e Web Application. Após isso,devemos configurar também o arquivo de configuração faces-config.xml, referente a uma aplicação específica que utiliza JSF.
,

Ele é responsável por descrever e configurar elementos e subelementos que compõem o projeto, tais como conversores, managed beans, validadores, fluxo da comunicação,configurações de localização e o mapeamento da navegação - ademais, ele faz a conexão entreView e Controller. Vamos resumir essa diferença entre esses dois arquivos?

(c) Conforme vimos em aula, o mapeamento de ações e regras de navegação é responsabilidade somente do faces-config.xml.
O faces-config.xml têm sido rapidamente substituído por annotations - novidade do JSF 2.0.Essa versão trouxe: suporte a facelets; utilização de templates para a aplicação;
simplificação do desenvolvimento de componentes; suporte nativo a Ajax (f:ajax); navegação implícita e condicional; suporte ao Método GET; adição de novos escopos (Flash e View); composição de componentes customizados; etc.
(d) Conforme vimos em aula, a questão está perfeita! O Ajax não só é suportado, esse suporte é nativo.
Galera, ele provê um modelo de programação bem definido e robusto, além de fornecer diversas taglibs - inclusive o desenvolver pode criar sua própria taglib. Essas taglibs contêm manipuladores de tags que implementam os componentes de tags. Essas características facilitam significativamente o peso da construção e manutenção de AplicaçõesWeb com interfaces de usuário server-side.
(e) Conforme vimos em aula, não se trata de um conjunto limitado de tags. É possível criar suas próprias tags!
Gabarito: D

8. (CESPE - 2013 - SERPRO - Analista - Desenvolvimento de Sistemas) O JSF
provê uma linguagem de expressão exclusiva para acesso a objetos armazenados em bancos de dados.
Comentários:

Em suma, a utilização de Facelets reduz o tempo e esforço gastos no desenvolvimento e implantação. Em geral, Facelets Views são criadas com Páginas HTML e XHTML(criadas em conformidade com Transationl DTD). Além disso, elas utilizam linguagens de expressão para referenciar propriedades e Managed Beans. Para desenvolver uma Aplicação Facelets simples, é necessário:
Conforme vimos em aula, ela serve para referenciar propriedades e Managed Beans.

/ 235

/

Gabarito: E

9. (FCC - 2012 - TST - Analista de Sistemas) Para criar as páginas
XHTML de uma aplicação JSF é possível utilizar um conjunto de bibliotecas de tags JSF. Algumas dessas bibliotecas são HTML, Core e Facelets. Considere os fragmentos de códigos abaixo, que utilizam tags dessas bibliotecas:
Fragmento de código

<ui:insert name="tituloM>Título <Aii:insert>

Fragmento de código II:

<h:mputText id="usuário" value=M#{usuano8ean.usuário,
nome}".'*

Fragmento de código III:

<h:selectOneMenu id="lista">

<f:selectltems va I u e="#{o pti o n Be a n .o pti on List}"Xf: se I e ctlte m >
<7h: se le ctOne M e n u >

A correlação correta entre o fragmento de código e a biblioteca de tags utilizada é:

a) l-Facelets, ll-HTMLe lll-Core.

b) l-Core, ll-Facelets, e lll-HTML.

c) l-HTML, ll-Core, e lll-Facelets.

d) l-HTML, ll-Facelets, e lll-HTML

e) l-HTML, ll-HTML, e lll-Core.

Comentários:

O Modelo de Componentes JSF define três taglibs:

HTML: possui componentes que representam diversos elementos HTML.
o Namespace: xmlns:h = "http://java.sun.com/jsf/html"

CORE: responsável por internacionalização, validação, conversão e outros,
o Namespace: xmlns:f="http://java.sun.com/jsf/core"

FACELETS: fornece tags para criar templates para aplicações web.

/ 235

/

o Namespace: xmlns:ui="http://java.sun.com/jsf/facelets"

Conforme vimos em aula, temos que olhar os namespaces. Dessa forma, o primeiro fragmento é referente a FACELETS; o segundo fragmento é referente a HTML; e o terceiro referente a CORE.Gabarito: A

1O.(CESPE - 2010 - TCU - Analista de Sistemas) No desenvolvimento de conteúdos para apresentação, o uso de facelets traz vantagens em relação ao uso de JSP. Uma delas é a maior modularidade, com o uso de templates e componentes compostos (composite).
Comentários:

Facelets é uma parte da especificação JSF e também a tecnologia de apresentação preferida para construir aplicações JSF - substituindo JSP. Ela suporta todos os componentes de UI doJSF e constrói Árvores de Componentes; e Views (utilizando Templates HTML). Um tipo especial de template são os Componentes Compostos, que agem como um componente. Ademais,é bom destacar algumas características:
Conforme vimos em aula, ela faz uso de Templates e Componentes Compostos, que aumentam a modularidade e a reusabilidade Gabarito: C
11.(FCC - 2012 - TJ-PE - Analista Judiciário - Análise de Sistemas) No JSF, o componenteController do MVC é composto por uma classe servlet, por arquivos de configuração e por um conjunto de manipuladores de ações e observadores de eventos. Essa servlet é chamada de:
a) ControllerServIet.

b) Facelet.

c) HttpServIet.

d) FacesConfig.

e) FacesServIet.

Comentários:

As principais tarefas de um Managed Bean (ou Backing Beans) é fornecer dados que serão exibidos nas telas; receber dados enviados nas requisições; executar tarefas de acordo com as ações dos usuários; validar dados. E o que seria a FacesServIet? É uma servlet que gerencia o ciclo de vida do processamento de requisições de aplicações web que estão utilizando JSFpara construir a interface com o usuário.

Conforme vimos em aula, trata-se da FacesServIet. Gabarito: E

/ 235

/

12.(CESPE - 2012 - TJ/AL - Analista de Sistemas - B) Em um aplicativo Facelets, a tag f:ajax adiciona funcionalidades Ajax que necessitam de adicionais de codificação e configuração para as componentes de interface do usuário.
Comentários:

O faces-config.xml têm sido rapidamente substituído por annotations - novidade do JSF 2.0.Essa versão trouxe: suporte a facelets; utilização de templates para a aplicação;
simplificação do desenvolvimento de componentes; suporte nativo a Ajax (f:ajax); navegação implícita e condicional; suporte ao Método GET; adição de novos escopos (Flash e View); composição de componentes customizados; etc.
Conforme vimos em aula, o suporte é nativo. Logo, não é necessário codificação e configuração adicionais:
"By using the f:ajax tag along with another standard component in a Facelets application. This method adds Ajax functionality to any UI component without additional coding and configuration". Gabarito: E
13.(FCC - 2012 - TRE-CE - Analista Judiciário - Análise de Sistemas) No ciclo de vida do JavaServer Faces trata-se da fase na qual o componente deve primeiro ser criado ou recuperado a partir do FacesContext, seguido por seus valores, que são geralmente recuperados dos parâmetros de request e, eventualmente, dos cabeçalhos ou cookies gerados. Trata-se da fase:
a) Restore View.

b) Apply Request Values.

c) Process Validation.

d) Update Model Values.

e) Invoke Application.

Comentários:

Apply Request Values: qualquer dado que for enviado como parte da requisição é passado para os componentes apropriados. Essas visões atualizam seus estados com os valores dos dados. Dados podem vir de formulários, cookies enviados com a requisição ou por meio de cabeçalhos da requisição. Alguns dados são validados e, se houver erro, são adicionados àFacesServIet.

Conforme vimos em aula, trata-se da fase Apply Request Values. Gabarito: B

/ 235

/

14.(CESPE - 2012 - TJ/RO - Analista de Sistemas - E) JNDI, parte do projeto de JSF,
utiliza
XHTML como tecnologia de apresentação dos dados, possibilitando a separação entre as camadas de negócio e de controle.
Comentários:

Em suma, a utilização de Facelets reduz o tempo e esforço gastos no desenvolvimento e implantação. Em geral, Facelets Views são criadas com Páginas HTML e XHTML(criadas em conformidade com Transationl DTD). Além disso, elas utilizam linguagens de expressão para referenciar propriedades e Managed Beans. Para desenvolver uma Aplicação Facelets simples, é necessário:
Conforme vimos em aula, a questão trata - na verdade - das Facelets. Gabarito: E

15.(FCC - 2012 - TRT - 11a Região (AM) - Técnico Judiciário - Tecnologia da
Informação)
Sobre o framework JavaServer Faces é correto afirmar:

a) A grande limitação do JSF é a dificuldade de integração com outros frameworks comoSpring, JPA e EJB.

b) Expression Language (EL) é a linguagem utilizada para apresentação de conteúdo em aplicações que utilizam JSF. Sua principal limitação é a impossibilidade de acessar valores e métodos em beans gerenciados.
c) Facelets é uma parte da especificação JSF e também a tecnologia para implementar as regras de negócio em aplicações que utilizam JSF.
d) Disponibiliza as bibliotecas de tags core e html para criar as páginas que compõem a interface do usuário.
e) Define uma única forma para realizar a validação de dados em formulários JSP, por meio da implementação de uma classe de validação que estende a interface Validator.
Comentários:

(a) Na verdade, está na Camada Web, facilmente integrável com Spring, JPA e EJB;

(b) Na verdade, é facilmente possível;

(c) Na verdade, Facelets tratam da camada de visão e, não, de regras de negócio;

(d) Perfeito, basta utilizar várias taglibs prontas ou criá-las;

(e) Na verdade, existem diversas formas.

Gabarito: D

,

16.(CESPE - 2013 - CPRM - Analista de Sistemas) Facelets são utilizadas para desenvolver visões (views) JavaServer Faces (JSF) com linguagem HTML e XHTML, em conformidade com a transitional document type definition, sendo, ainda, compatível com a biblioteca de tag JSF.
Comentários:

Em suma, a utilização de Facelets reduz o tempo e esforço gastos no desenvolvimento e implantação. Em geral, Facelets Views são criadas com Páginas HTML e XHTML(criadas em conformidade com Transationl DTD). Além disso, elas utilizam linguagens de expressão para referenciar propriedades e Managed Beans. Para desenvolver uma Aplicação Facelets simples, é necessário:
Conforme vimos em aula, a questão está perfeita! Gabarito: C

17.(FCC - 2011 - TRE-AP - Técnico Judiciário - Programação de Sistemas) O JSF extrai todos os valores digitados pelo usuário e guarda esse valor nos seus respectivos componentes.Se o valor digitado não coincidir com o componente, um erro vai ser adicionado na classeFacesContext e será mostrado na fase Render Response Phase.

No ciclo de vida do JSF trata-se de um evento típico da fase:

a) Process Validations Phase.

b) Restore View Phase.

c) Apply Request Values Phase.

d) Update Model Values Phase.

e) Invoke Application Phase.

Comentários:

Apply Request Values: qualquer dado que for enviado como parte da requisição é passado para os componentes apropriados. Essas visões atualizam seus estados com os valores dos dados. Dados podem vir de formulários, cookies enviados com a requisição ou por meio de cabeçalhos da requisição. Alguns dados são validados e, se houver erro, são adicionados àFacesServIet.

Conforme vimos em aula, trata-se da fase Apply Request Values. Gabarito: C

18.(CESPE - 2013 - INPI - Analista Judiciário - Análise de Sistemas) Quando registrado emJSF 2 (Java Server Faces), um managed bean permanece no escopo de session.

/ 235

/

Comentários:

O JSF1 tinha os escopos Request (Default), Session e Application. A partir do JSF2,
ganhamos o
View, Flash, None e Custom. O @RequestScoped vive o tempo do ciclo de umaRequisição/Resposta HTTP; o @ViewScoped vive enquanto houver interação com a mesma view,
i.e., enquanto persistir a mesma página; o @ApplicationScoped persiste toda a duração da aplicação web.
No JSF2, o Escopo Request continua sendo o padrão (default)! Gabarito: E

19.(CESPE - 2010 - TCU - Analista de Sistemas) Para suportar a construção de aplicações com Ajax e JSF, recomenda-se aos desenvolvedores de páginas que usem a tag <f:ajax>,relacionada ao processamento de pedidos http assíncronos.

Comentários:

O faces-config.xml têm sido rapidamente substituído por annotations - novidade do JSF
2.0. Essa versão trouxe: suporte a facelets; utilização de templates para a aplicação;simplificação do desenvolvimento de componentes; suporte nativo a Ajax (f:ajax); navegação implícita e condicional; suporte ao Método GET; adição de novos escopos (Flash e View);composição de componentes customizados; etc.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

2O.(FCC - 2011 - TRE-RN - Técnico Judiciário - Programação de Sistemas) No ciclo de vida do JSF copiar os parâmetros de requisição para valores submetidos pelos componentes,é a tarefa típica da fase:

a) Restaurar Visão (Restore view).

b) Invocar aplicação (Invoke application).

c) Aplicar valores de requisição (Apply request values).

d) Processar validações (Process validation).

e) Atualizar valores do modelo (Update model values).

Comentários:

Apply Request Values: qualquer dado que for enviado como parte da requisição é passado para os componentes apropriados. Essas visões atualizam seus estados com os valores dos dados.
/ 235

/

Dados podem vir de formulários, cookies enviados com a requisição ou por meio de cabeçalhos da requisição. Alguns dados são validados e, se houver erro, são adicionados à FacesServIet.
Conforme vimos em aula, trata-se da fase Apply Request Values. Gabarito: C

21.(CESPE - 2010- MPU - Analista de Sistemas) Uma aplicação web deve prover mecanismos de validação de dados. O JSF fornece vários validadores de dados padrões que podem ser utilizados no lado do cliente (client-side).
Comentários:

Pessoal, o JSF oferece diversos validadores embutidos para validar seus Componentes UI
- essa validação ocorre no lado do servidor. Eles podem ser invocados a partir de sua tag específica e podem validar o tamanho de um campo, tipo de entrada, range de um valor numérico,expressão regular, entre outros. É possível, inclusive, criar o seu próprio validador customizado.
Conforme vimos em aula, ocorre do lado servidor! Gabarito: E

22.(FCC - 2010 - TRT - 22a Região (PI) - Técnico Judiciário - Tecnologia da
Informação) É um framework MVC utilizado no desenvolvimento de aplicações para a internet de forma visual, que utiliza o recurso de arrastar e soltar os componentes na tela para definir suas propriedades:
a) Enterprise JavaBeans.

b) JavaServer Faces.

c) Java 2 Enterprise Edition.

d) Servlets.

e) Java Server Pages.

Comentários:

O resultado foi a criação do framework Struts! Ele era uma implementação da
Arquitetura MVC
para desenvolvimento de páginas web dinâmicas! Bacana? Esse framework fez tanto sucesso que a Sun Microsystems junto com uma comunidade de desenvolvedores resolveu criar uma especificação padronizada baseada nesse framework, denominado Java Server Faces (JSF).
Conforme vimos em aula, trata-se do JSF! Gabarito: B

/ 235

/

23.(CESPE - 2015 - TCU - Analista de Sistemas) A partir da interpretação do trecho JSF(JavaServer Faces), versão 2, no código a seguir, verifica-se que uma providência válida é configurar o managed-bean clientePage no arquivo faces-config.xml.
<f:view>

<h:form id="clienteForm">

<h:outputl_abel for="informeNome" value="lnforme Nome"/>

<h:inputText id="informeNome" value ="#{clientePage.nome}"/>

<h:commandButton value="Nome do Cliente"
action="#{clientePage.cliente}"/>

</h:form>

</f:view>

Comentários:

O faces-config.xml é mais específico, tratando de regras e mapeamento de navegação;
definição de managed beans; configuração de detalhes de internacionalização; entre outros. Já o web.xml é mais genérico, tratando da especificação de detalhes de segurança; configuração de páginas de erro; mapeamento e declaração de servlets e filtros; configuração de parâmetros de inicialização;entre outros.

Conforme vimos em aula, a questão está perfeita! É possível declarar managed beans por meio de anotações ou por meio do arquivo de configuração faces-config.xml. Gabarito: C
24.(CESPE - 2014 - TJ-SE - Analista Judiciário - Análise de Sistemas) Antes de uma aplicação web desenvolvida nos moldes da JSF executar sua primeira página web, uma instânciaFacesServIet é executada, a fim de gerenciar as requisições dessa aplicação.

Comentários:

Lembrando que FacesContext (javax.faces.context) é o objeto utilizado para representar todas as informações de contexto associadas ao processamento da requisição de entrada e à criação da resposta correspondente. Ela é criada pela FacesServIet, que é executada antes do início do ciclo de vida de processamento de requisições e é responsável por gerenciar a execução das etapas do ciclo de vida.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

25.(FGV - 2013 - ALEMA - Analista de Sistemas) Com relação à especificação Java Server
Faces (JSF), assinale V para a afirmativa verdadeira e F para a falsa.

() Visa substituir a especificação Java Server Pages.

() Java Server Faces são usadas como uma fachada para Servlets e Java Server Pages.

() Define um framework MVC (Model View Controler) para aplicações Web.

As afirmativas são, respectivamente,

a) F, F e V.

b) F, V e V.

c) V, F e F.

d) V, V e F.

e) F, V e F.

Comentários:

Facelets é uma parte da especificação JSF e também a tecnologia de apresentação preferida para construir aplicações JSF - substituindo JSP. Ela suporta todos os componentes de UI doJSF e constrói Árvores de Componentes; e Views (utilizando Templates HTML). Um tipo especial de template são os Componentes Compostos, que agem como um componente. Ademais,é bom destacar algumas características:
(F) Conforme vimos em aula, Facelets vieram para substituir JSP e, não, JSF!

Essa eu vou explicar melhor, porque sempre me perguntar: se eu afirmar que o Facebook visava substituir o MSN, isso é certo ou errado? Errado, ele está em um contexto muito maior; uma de suas funcionalidades (chat) veio de fato a substituir o MSN! JSF é um framework imenso, com centenas de funcionalidades. Ora, eu não posso afirmar que ele visa substituir JSP! Na verdade,uma de suas funcionalidades vem substituindo JSP, mas não o JSF como um todo.

(F) Não, esse item não faz nenhum sentido.

O resultado foi a criação do framework Struts! Ele era uma implementação da
Arquitetura MVC
para desenvolvimento de páginas web dinâmicas! Bacana? Esse framework fez tanto sucesso que a Sun Microsystems junto com uma comunidade de desenvolvedores resolveu criar uma especificação padronizada baseada nesse framework, denominado Java Server Faces (JSF).
(V) Perfeito, implementa o padrão MVC! Gabarito: A

,

26.(CESPE - 2014 - TJ-SE - Analista Judiciário - Análise de Sistemas) Em aplicações web nos padrões da JSF, é possível utilizar recursos Ajax para criar páginas dinâmicas, como,por exemplo, por meio da tag f:ajax, conforme apresentado na sintaxe abaixo.
<h:inputText value="#{bean.message}">

<f:ajax />

</h:inputText>

Comentários:

O faces-config.xml têm sido rapidamente substituído por annotations - novidade do JSF
2.0. Essa versão trouxe: suporte a facelets; utilização de templates para a aplicação;simplificação do desenvolvimento de componentes; suporte nativo a Ajax (f:ajax); navegação implícita e condicional; suporte ao Método GET; adição de novos escopos (Flash e View);composição de componentes customizados; etc.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

27.(CESPE - 2014 - TJ-SE - Analista Judiciário - Análise de Sistemas) É possível utilizar XHTMLno desenvolvimento de facelets para criar páginas web compatíveis com a JSF (JavaServer
Faces) para apresentação dos dados. Na versão Java EE 7, essa forma de apresentação é mais indicada que a JSP (JavaServer Pages), uma vez que esta não suporta todos os novos recursos da versão Java EE 7.
Comentários:

Pessoal, tem uma característica do JSF que é extremamente importante: Facelets! Trata-se de uma linguagem de declaração de página poderosa, apesar de leve. Antigamente, utiliza-se a tecnologiaJSP como camada de visão do JSF, porém ele não suporta todas as características disponíveis naPlataforma Java EE - sendo considerada obsoleta para JSF!

Conforme vimos em aula, a questão está perfeita! Gabarito: C

/ 235

/

LISTA DE QUESTõES-JSF - MULTIBANCAS

1. (FCC - 2013 - TRT/12 - Analista de Sistemas) Considere as instruções abaixo encontradas em um arquivo de uma aplicação que utiliza JSF:
<managed-bean>

<managed-bean-name>func</managed-bean-name>

<managed-bean-class>bean.Funcionario</managed-bean-class>

<managed-bean-scope>session</managed-bean-scope>

</managed-bean>

Essas instruções indicam a existência de um bean gerenciado (classe Funcionario.java) no pacote bean que poderá ser referenciado nas páginas JSP por meio da palavra func. Oarquivo correto no qual essas instruções são colocadas é o:

a) context.xml.

b) web-inf.xml.

c) web.xml.

d) faces-config.xml.

e) config-bean.xml.

2. (CESPE - 2009 - SECONT-ES - Auditor do Estado - Tecnologia da Informação) O JSF
é um framework web embasado em interface gráfica, capaz de renderizar componentes e manipular eventos em aplicações web no padrão Java EE, no qual os componentes JSFsão orientados a eventos. O JSF fornece, ainda, mecanismos para conversão, validação,
execução de lógica de negócios e controle de navegação.

3. (FCC - 2012 - TJ-PE - Programador de computador) Em uma aplicação que utiliza
JSF,
para configurar o fluxo de comunicação presente na servlet de controle, é utilizado um arquivo de configuração:
a) webfaces.xml.

b) actionform.xml.

c) faces-config.xml.

d) webcontext.xml.

,

4. (CESPE - 2010 - TRE-BA - Analista Judiciário - Análise de Sistemas) Entre os itens que o padrão Java Server Faces (JSF) utiliza, estão os componentes, os eventos e a navegabilidade.
5. (FCC - 2013 - TRT/9 - Analista de Sistemas) Uma aplicação utilizando o framework
JSF e a IDE NetBeans gera automaticamente dois componentes essenciais assim descritos:
I. É responsável por receber requisições dos componentes View do MVC, redirecioná-las para os beans gerenciados (managed beans) do componente Model do MVC e responder a essas requisições.
II. É o arquivo principal de configuração de uma aplicação web que utiliza o framework JSF.É responsável por descrever os elementos e sub-elementos que compõem o projeto, tais como as regras de navegação, beans gerenciados, configurações de localização etc.
As descrições I e II referem-se, respectivamente, aos componentes:

a) servlet Controller.java e ao arquivo faces_config.xml b) FaceletServIet e ao arquivo web_config.xml.
c) FacesServIet e ao arquivo faces-config.xml.

d) servlet Controller e ao arquivo web-config.xml.

e) servlet Facelet e ao arquivo web.xml.

6. (CESPE - 2012 - ANAC - Analista Administrativo - Área 4) A validação de dados de um componente pode ser uma das funções de um backing bean, em uma aplicação JSF.
7. (FCC - 2012 - TST - Analista de Sistemas) O framework JavaServer Faces (JSF) é utilizado no desenvolvimento de aplicações web que utiliza o design pattern MVC. O JSF:
a) disponibiliza controles pré-construídos e código para manipular eventos, estimulando o uso de código Java convencional no componente View do MVC.
b) recebe requisições dos componentes da View do MVC, através do servlet FaveServerServIet.

c) armazena os mapeamentos das ações e regras de navegação em projetos JSF nos arquivosWEB-INF.xml e FACES-CONFIG.xml.

d) possui bibliotecas que suportam Ajax (Asynchronous JavaScript And XML).

/

e) provê um conjunto de tags limitado para criar somente páginas HTML/XHTML.

8. (CESPE - 2013 - SERPRO - Analista - Desenvolvimento de Sistemas) O JSF provê uma linguagem de expressão exclusiva para acesso a objetos armazenados em bancos de dados.
9. (FCC - 2012 - TST - Analista de Sistemas) Para criar as páginas XHTML de uma aplicaçãoJSF é possível utilizar um conjunto de bibliotecas de tags JSF. Algumas dessas bibliotecas são HTML, Core e Facelets. Considere os fragmentos de códigos abaixo, que utilizam tags dessas bibliotecas:
Fragmento de código

<ui:insert name=''tituloM>Título <ui:insert>

</h1>

Fragmento de código II:

<h:mputText id="usuárioM value=M#{usuario8ean.usuário.
nome}">

Fragmento de código III:

< h: sei ectOne Me n u id="I i sta">

<f:selectltems va I u e= "#{o ptio n Be a n .o pti on L ist}M><f: se lectltem >
</h: se I e ctOne Me n u >

A correlação correta entre o fragmento de código e a biblioteca de tags utilizada é:

a) l-Facelets, ll-HTML e lll-Core.

b) l-Core, ll-Facelets, e lll-HTML.

c) l-HTML, ll-Core, e lll-Facelets.

d) l-HTML, ll-Facelets, e lll-HTML

e) l-HTML, ll-HTML, e lll-Core.

10.(CESPE - 2010 - TCU - Analista de Sistemas) No desenvolvimento de conteúdos para apresentação, o uso de facelets traz vantagens em relação ao uso de JSP. Uma delas é a maior modularidade, com o uso de templates e componentes compostos (composite).
,

11.(FCC - 2012 - TJ-PE - Analista Judiciário - Análise de Sistemas) No JSF, o componenteController do MVC é composto por uma classe servlet, por arquivos de configuração e por um conjunto de manipuladores de ações e observadores de eventos. Essa servlet é chamada de:
a) ControllerServIet.

b) Facelet.

c) HttpServIet.

d) FacesConfig.

e) FacesServIet.

12.(CESPE - 2012 - TJ/AL - Analista de Sistemas - B) Em um aplicativo Facelets, a tag f:ajax adiciona funcionalidades Ajax que necessitam de adicionais de codificação e configuração para as componentes de interface do usuário.
13.(FCC - 2012 - TRE-CE - Analista Judiciário - Análise de Sistemas) No ciclo de vida do JavaServer Faces trata-se da fase na qual o componente deve primeiro ser criado ou recuperado a partir do FacesContext, seguido por seus valores, que são geralmente recuperados dos parâmetros de request e, eventualmente, dos cabeçalhos ou cookies gerados. Trata-se da fase:
a) Restore View.

b) Apply Request Values.

c) Process Validation.

d) Update Model Values.

e) Invoke Application.

14.(CESPE - 2012 - TJ/RO - Analista de Sistemas - E) JNDI, parte do projeto de JSF,
utiliza
XHTML como tecnologia de apresentação dos dados, possibilitando a separação entre as camadas de negócio e de controle.
15.(FCC - 2012 - TRT - 11a Região (AM) - Técnico Judiciário - Tecnologia da
Informação)
Sobre o framework JavaServer Faces é correto afirmar:

a) A grande limitação do JSF é a dificuldade de integração com outros frameworks como Spring,
JPAeEJB.

b) Expression Language (EL) é a linguagem utilizada para apresentação de conteúdo em aplicações que utilizam JSF. Sua principal limitação é a impossibilidade de acessar valores e métodos em beans gerenciados.
c) Facelets é uma parte da especificação JSF e também a tecnologia para implementar as regras de negócio em aplicações que utilizam JSF.
d) Disponibiliza as bibliotecas de tags core e html para criar as páginas que compõem a interface do usuário.
e) Define uma única forma para realizar a validação de dados em formulários JSP, por meio da implementação de uma classe de validação que estende a interface Validator.
16.(CESPE - 2013 - CPRM - Analista de Sistemas) Facelets são utilizadas para desenvolver visões (views) JavaServer Faces (JSF) com linguagem HTML e XHTML, em conformidade com a transitional document type definition, sendo, ainda, compatível com a biblioteca de tag JSF.
17.(FCC - 2011 - TRE-AP - Técnico Judiciário - Programação de Sistemas) O JSF extrai todos os valores digitados pelo usuário e guarda esse valor nos seus respectivos componentes.Se o valor digitado não coincidir com o componente, um erro vai ser adicionado na classeFacesContext e será mostrado na fase Render Response Phase.

No ciclo de vida do JSF trata-se de um evento típico da fase:

a) Process Validations Phase.

b) Restore View Phase.

c) Apply Request Values Phase.

d) Update Model Values Phase.

e) Invoke Application Phase.

18. (CESPE - 2013 - INPI - Analista Judiciário - Análise de Sistemas) Quando registrado emJSF 2 (Java Server Faces), um managed bean permanece no escopo de session.

19. (CESPE - 2010 - TCU - Analista de Sistemas) Para suportar a construção de aplicações com Ajax e JSF, recomenda-se aos desenvolvedores de páginas que usem a tag <f:ajax>,relacionada ao processamento de pedidos http assíncronos.

20. (FCC - 2011 - TRE-RN - Técnico Judiciário - Programação de Sistemas) No ciclo de vida do JSF copiar os parâmetros de requisição para valores submetidos pelos componentes,é a tarefa típica da fase:

a) Restaurar Visão (Restore view).

b) Invocar aplicação (Invoke application).

c) Aplicar valores de requisição (Apply request values).

d) Processar validações (Process validation).

e) Atualizar valores do modelo (Update model values).

/ 235

/

21. (CESPE - 2010 - MPU - Analista de Sistemas) Uma aplicação web deve prover mecanismos de validação de dados. O JSF fornece vários validadores de dados padrões que podem ser utilizados no lado do cliente (client-side).
22. (FCC - 2010 - TRT - 22a Região (PI) - Técnico Judiciário - Tecnologia da
Informação) É
um framework MVC utilizado no desenvolvimento de aplicações para a internet de forma visual, que utiliza o recurso de arrastar e soltar os componentes na tela para definir suas propriedades:
a) Enterprise JavaBeans.

b) JavaServer Faces.

c) Java 2 Enterprise Edition.

d) Servlets.

e) Java Server Pages.

23. (CESPE - 2015 - TCU - Analista de Sistemas) A partir da interpretação do trecho
JSF
(JavaServer Faces), versão 2, no código a seguir, verifica-se que uma providência válida é configurar o managed-bean clientePage no arquivo faces-config.xml.
<f:view>

<h:form id="clienteForm">

<h:outputl_abel for="informeNome" value="lnforme Nome"/>

<h:inputText id="informeNome" value ="#{clientePage.nome}"/>

<h:commandButton value="Nome do Cliente"
action="#{clientePage.cliente}"/>

</h:form>

</f:view>

24.(CESPE - 2014 - TJ-SE - Analista Judiciário - Análise de Sistemas) Antes de uma aplicação web desenvolvida nos moldes da JSF executar sua primeira página web, uma instância FacesServIet é executada, a fim de gerenciar as requisições dessa aplicação.
25.(FGV - 2013 - ALEMA - Analista de Sistemas) Com relação à especificação Java Server
Faces (JSF), assinale V para a afirmativa verdadeira e F para a falsa.

() Visa substituir a especificação Java Server Pages.

() Java Server Faces são usadas como uma fachada para Servlets e Java Server Pages.
() Define um framework MVC (Model View Controler) para aplicações Web.

As afirmativas são, respectivamente.

a) F, F e V.

b) F, V e V.

c) V, F e F.

*

d) V, Ve F.

e) F, V e F.

26.(CESPE - 2014 - TJ-SE - Analista Judiciário - Análise de Sistemas) Em aplicações web nos padrões da JSF, é possível utilizar recursos Ajax para criar páginas dinâmicas,como,
por exemplo, por meio da tag f:ajax, conforme apresentado na sintaxe abaixo.

<h:inputText value="#{bean.message}">

<f:ajax />

</h:inputText>

27.(CESPE - 2014 - TJ-SE - Analista Judiciário - Análise de Sistemas) É possível utilizar XHTMLno desenvolvimento de facelets para criar páginas web compatíveis com a JSF (JavaServer
Faces) para apresentação dos dados. Na versão Java EE 7, essa forma de apresentação é mais indicada que a JSP (JavaServer Pages), uma vez que esta não suporta todos os novos recursos da versão Java EE 7.
GABARITO

1. D 8. E
15. D 22. B

2. C 9. A
16. C 23. C

3. C 10. C
17. C 24. C

4. C 11. E
18. E 25. A

5. C 12. E
19. C 26. C

6. C 13. B
20. C 27. C

7. D 14. E
21. E

JAVA PERSISTENCE API (JPA)

Galera, Java começou a ficar extremamente popular em ambientes corporativos,
mas havia um problema que estava incomodando os desenvolvedores: a produtividade estava prejudicada porque eles estavam perdendo muito tempo nas codificações de Queries SQL e em seu respectivo código JDBC. E quando era necessário mudar o banco de dados por um de outro fabricante? Oque fazer?

Além disso, Java ajudou a popularizar o Paradigma Orientado a Objetos, em que informações eram representadas por meio de classes, atributos, herança, polimorfismo,encapsulamento, etc.
Isso gerava conflito com o Paradigma Relacional dos bancos de dados, em que as informações eram representadas por meio de tabelas, colunas, linhas, chaves primárias, chaves estrangeiras,etc.

Pois bem! Era trabalhoso transformar objetos de uma classe em registros de uma tabela e vice-versa. Logo, começaram a surgir algumas ferramentas que auxiliavam essa tarefa - são as famosasORM - Object-Relational Mapping (ou Mapeamento Objeto-Relacional). As mais conhecidas eramHibernate1 e TopLink- a primeira, open-source, tornou-se uma referência mundial.

Essas ferramentas facilitam o mapeamento dos atributos de uma base de dados relacional para o modelo de objetos de uma aplicação por meio de Descritores de Implantação (XML) ouAnotações
(Annotations) - principalmente para consultas e atualizações de dados. O
desenvolvedor define como os objetos são mapeados e o framework faz o resto - acessa o Banco de Dados,gera
Comandos SQL, etc.

A utilização desses frameworks de mapeamento objeto-relacional permitiu preservar as vantagens do Paradigma Relacional (Robustez, Maturidade, Facilidade de Pesquisa, etc) para aCamada de
Persistência; e preservar as vantagens do Paradigma Orientado a Objetos (Reúso,
Modularidade,
Herança, Polimorfismo, etc) para a Camada de Negócios.

Antes de continuar, preciso que vocês entendam o conceito de POJO (Plain Old
Java Object).
Trata-se de objetos simples e comuns que não deveriam ter que:

* Estender interfaces pré-especificadas:

public class Foo extends javax.servIet.http.HttpServIet { ...

* Implementar classes pré-especificadas:

public class Bar implements javax.ejb.EntityBean { ...

* Conter anotações pré-especificadas:
@javax.persistence.Entity public class Baz { ...

1 Possui até uma versão para .NET - chama-se NHibernate.

/ 235

/

Galera, esse conceito é teórico! Na prática, por dificuldades técnicas (entre outras razões),consideram-se POJO também as classes que contenham anotações pré-especificadas.
Qual a vantagem de se utilizar POJO? Como ele não estende nada nem implementa interfaces, ele não possui dependências por frameworks corporativos e pode se focar somente na lógica de negócio.
Ele também é importante para desacoplar o código da aplicação dos frameworks de infraestrutura.Mudou o framework? O POJO continuará funcionando - inclusive, a mudança será fácil e conterá menos riscos! Até a Especificação EJB 2.0, a persistência de dados era parte daPlataforma EJB e era realizada por meio de Entity Beans - que eram uma espécie de POJO.
Rapidamente: algumas pessoas me perguntam qual a diferença entre um POJO e um JavaBean!
Todo JavaBean é um POJO, mas nem todo POJO é um JavaBean. Eles são muito parecidos,
mas o JavaBean segue diversas convenções de programação, tais como:
nomenclatura dos métodos, construtor público padrão e sem parâmetros, entre outros. Para o JPA, oPOJO é a unidade básica!
INDO MAIS

FUNDO!

Que tal, agora, entrar mais a fundo no JPA? Bem, os frameworks do mercado possuíam algumas diferenças! A Sun MicroSystems, então, fez uma proposta ao líder do Projeto Hibernate:fazer uma especificação com o objetivo de padronizar os frameworks de mapeamento objeto-relacional!Para tal, ele pegou as melhores ideias do Hibernate, TopLink, JDO, etc e condensou em uma especificação.
FAQ: JPA

Q: Why didn't you adopt Hibernate or JDO as the persistence API?

A: We chose to combine the best ideas from many sources in the new persistence API
and create a practical, easy to use API to meet the needs of a majority of Java EE andJava SE
community members. The Java Persistence API is not based on any single existing persistence framework but incorporates- and improves upon - ideas contributed by many popular frameworks, including Hibernate, TopLink, JDO, and others.
E foi assim que surgiu o Java Persistence API (JPA)! Olha que engraçado: a especificação surgiu após as implementações! Como uma das vantagens, pode-se trocar de implementação(Ex:
Hibernate para TopLink) sem a necessidade de modificar o código-fonte.
Enfim, ele foi incorporado ao EJB 3.0 (apesar de ser independente deste), permitindo sua utilização emAmbientes Java SE e Java EE.

Em suma, podemos dizer que o JPA é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais emAplicações Java - em outras palavras, ele simplifica a persistência de dados.
Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
E interessante notar um pouco da evolução do Java Persistence API (JPA) e como ele evolui harmonicamente com o Ambiente Java EE. Ele apareceu pela primeira vez no Java EE 5(JSR220).
Depois ele se transformou em JPA 2.0 no Java EE 6 (JSR 317) e, atualmente, temos o
JPA 2.1 -
no Java EE 7 (JSR 338). De todo modo, ele consiste em quatro partes:

Java Persistence API (JPA): define um mapeamento objeto/relacional para gerenciamento de dados relacionais;
Java Persistence Query Language (JPQL): define queries, em geral, estáticas para entidades e seus estados persistentes;
Java Persistence Criteria API (JPCA): define queries, em geral, dinâmicas para entidades e seus estados persistentes;
Mapeamento de Metadados O/R: define um mapeamento por meio de Descritores de
Implantação (XML) ou Anotações (Annotations).

Há duas formas de mapear classes de negócio em entidades de um banco de dados:
Descritores de Implantação (XML) ou Anotações (Annotations)! O XML foi praticamente engolido pelas anotações, tanto que hoje em dia é muito raro utilizá-lo para certas tarefas. Por que, professor?Porque as anotações evitam a criação de complexos arquivos de configuração em XML.
Vejamos algumas anotações:
ANOTAÇÃO DESCRIÇÃO

@Entity Indica que uma classe é uma entidade que deve ser persistida como tabela.
@Table Indica o nome de uma tabela para qual a entidade é mapeada.

@Column Indica que um atributo de uma classe é uma coluna de uma tabela.
@ld Indica que um atributo é a chave primária de uma entidade.

@namedQuery Define uma consulta.

@namedQueries Define várias consultas.

@UniqueConstraint Indica que uma propriedade não pode conter valores duplicados.

@Transient Indica que uma propriedade não deve ser persistida no banco de dados.
@lnheritance Define um relacionamento de herança à entidade.
@ManyToOne Mapeamento muitos para um (N:1).
@OneToMany Mapeamento um para muitos (1 :N).
@OneToOne Mapeamento um para um (1:1).

/ 235

/

Galera, vocês sabem o que é um EntityManager? Trata-se de uma interface que funciona como serviço centralizado para todas as ações de persistência - mapeando um conjunto de classes para um banco de dados particular. Em outras palavras, ele é responsável por realizar operações de sincronismo com o Banco de Dados (Inserir, Remover, Atualizar e Consultar), além de gerenciar o ciclo de vida das entidades.
javax.perslstence

- FlushMode: FlushModeType

- getTraflsacròortO: EntífyTjransactíon

- persíStíO&yecfJ

- removefOÈyéctJ

- refresftfO&yeeíJ

- /ockíO&jecL LocWotfeTyoeJ

- í/?dfC/ass<r>I OítfecíJ: T

- g?ef/:?eferencefC/a5S<T>, Oòjecyr 7

- contarns(Oü/ectJ: boo/ean

- flushf)

- cíearfj

- createQueryfStríng): Query

- createNamedQLfefyfStringJ: Query

- createNaíjVeQueryf..J: Query

- isQpenf): booíean

- ctosefj

EntityManager.persist(Object): persiste o objeto Object;

EntityManager. remove (Object): remove o objeto Object;

EntityManager.find(Object): busca o objeto Object;

EntityManager.refresh(Object): atualiza o objeto Object;

EntityManager.createQuery(String): realiza uma consulta String;

Sabe quando você deseja realizar uma inserção no banco de dados? Pois é,
o objeto do
EntityManager irá realizar essa tarefa! Esse gerenciador de entidades interage com um
Persistence
Context, que é um local em que ficam armazenados os objetos (entidades) que estão sendo manipulados pelo EntityManager corrente. Ele funciona como um contêiner que guarda as entidades gerenciadas pelo EntityManager.
Um artigo do DevMedia faz uma excelente comparação entre Persistence Context e a
Memória
Cache de um Processador (aquela mais rápida):

/ 235

/

(Profs. Paolla Ramos e Raphael L

ESCLARECENDO!

Imagine o Persistence Context como um container capaz de armazenar todas as entidades que serão manipuladas pelo EntityManager. No início da nossa aplicação, não temosPersistence
Context ou EntityManager, pois não realizamos nenhuma operação com o banco.
Então, você decide buscar o usuário "Mario" no BD e, neste momento, são criados 1EntityManager + 1
PersistenceContext (ligados diretamente).

O EntityManager vai até o Persistence Context e checa se o usuário "Mario" já está lá, e como não está, ele irá ao banco de dados realizar a consulta desejada retornando o objeto Mario preenchido e populado. Depois de retornar o usuário "Mario" do BD, o EntityManager grava esse objeto no Persistence Context (Nosso Cache). Assim, da próxima vez que precisar deste objeto,não precisará ir ao banco de dados.

Então como você pode perceber no cenário acima, o EntityManager sempre consulta o
Persistence
Context, checando se o objeto já está lá e, caso não esteja, aí sim ele irá até o banco de dados.Quando o EntityManager é destruído (no fim de uma requisição) o Persistence Context também será destruído, impossibilitando de usá-los em outrosEntityManager com outros
PersistenceContext.

Lá em cima, eu afirmei que um EntityManager mapeava um conjunto de classes para um banco de dados particular. Esse conjunto de classes é denominado Persistence Unit2 .Antes mesmo de pensar em criar entidades ou consultá-las por meio do EntityManager, é necessário empacotar esse conjunto de classes em um Persistence Unit, que é definido no Descritor de Implantação(persistence.xml).

O EntityManager pode ser criado ou pode ser obtido de um EntityManagerFactory
- que seria uma espécie de fábrica de EntityManager. No Java SE, deve-se utilizar oEntityManagerFactory para obter o EntityManager, o que não é necessariamente exigido no Java EE. Para obter umEntityManager, devemos primeiro criar o EntityManagerFactory e, só depois, criar oEntityManager:

EntityManagerFactory emf = Persistence.createEntityManagerFactory("Exemplo");
em = emf.createEntityManagerO;

É importante notar que a classe javax.persistence.Persistence procura o Descritor de
Implantação persistence.xml dentro de seu classpath. Ele procurará o Persistence Unit com o mesmo nome do parâmetro da função createEntityManagerFactory, i.e., "Exemplo".Obtido o
EntityManagerFactory, basta chamar a função createEntityManager.

2 Ele especifica qual implementação será utilizada (Hibernate, Toplink, JDO, etc); conexão com banco, etc.
www. estra tegiaconcursos. com. br

* = Extended persiste nce context

O ciclo de vida dos objetos de entidade consiste em quatro estados: Novo (New),
Gerenciado
(Managed), Removido (Removed) e Destacado (Detached). Quando um objeto é criado inicialmente seu estado é Novo. Nesse estado, o objeto ainda não está associado a umEntityManager e não possui qualquer representação no banco de dados. Bacana?

Um objeto se torna Gerenciado quando é persistido no banco de dados por meio do método de persistência do EntityManager, que deve ser invocado dentro de uma transação ativa.Quando se dá um Commit na transação, o objeto é persistido no banco de dados. Objetos recuperados do banco de dados por um EntityManager também estão no estado Gerenciado.
Se um objeto Gerenciado é modificado dentro de uma transação ativa, a mudança é detectada pelo EntityManager e a atualização é propagada no banco de dados após o Commit. Um objetoGerenciado também pode ser recuperado do banco de dados e marcado para remoção,
utilizando o método remove do EntityManager dentro de uma transação ativa.
O objeto modifica seu estado de Gerenciado para Removido, e é fisicamente deletado do banco de dados após o Commit. O último estado, Destacado, representa um objeto que foi desconectado do EntityManager. Quando um objeto é Destacado, mudanças sucessivas não irão mais ser rastreadas e nenhuma sincronização automática do banco de dados será realizada.
,

Por fim, é interessante mencionar uma implementação do JPA que tem feito sucesso ultimamente:EclipseLink. Trata-se de uma implementação baseada no TopLink que se diferencia por sua simplicidade em relação ao Hibernate e implementa outros padrões além do JPA,como JAXB,
JCA e SDO. Galera, isso nunca caiu em prova, mas eu acho importante saber que existe essa implementação também. Blz?
QUESTõES CoMENTADAS - JPA - MULTIBANCAS

1. (FCC - 2007 - TRE/MS - Analista de Sistemas - III) A API de Persistência Java pode ser utilizada no container Web e/ou no container EJB e disponibiliza recursos de mapeamento objeto-relacional as aplicações Java EE.
Comentários:

Java Persistence API (JPA) é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais emAplicações Java - em outras palavras, ele simplifica a persistência de dados. Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
Conforme vimos em aula, a questão está completamente perfeita! Gabarito: C

2. (CESPE - 2014 - TJ-SE - Analista Judiciário - Banco de Dados) A JPA, que foi criada como alternativa para o Hibernate para conexão com os sistemas gerenciadores de banco de dados, está nativa no Java SE a partir da versão 1.3.
Comentários:

Que tal, agora, entrar mais a fundo no JPA? Bem, os frameworks do mercado possuíam algumas diferenças! A Sun MicroSystems, então, fez uma proposta ao líder doProjeto
Hibernate: fazer uma especificação com o objetivo de padronizar os frameworks de mapeamento objeto-relacional! Para tal, ele pegou as melhores ideias do Hibernate,TopLink,
JDO, etc e condensou em uma especificação.

Conforme vimos em aula, JPA não é uma alternativa ao Hibernate! JPA é a especificação eHibernate é a implementação dessa especificação (assim como TopLink, OpenJPA, JDO, etc).
Gabarito: E

3. (FCC - 2014 - TRT - 13a Região (PB) - Técnico Judiciário - Tecnologia da
Informação) Java
Persistence API (JPA) é uma API padrão da linguagem Java para persistência de dados em bancos de dados relacionais. Em uma aplicação que utiliza JPA:
a) pode ser utilizada, como provedor de persistência, as bibliotecas
EclipseLink, Hibernate,
OracleTopLink, JBossSeam e JDBCProvider.

/ 235

/

b) as classes de entidade do banco de dados permitem o mapeamento entre objetos da classe e tabelas do banco de dados, utilizando anotações como @Table, @Entity,@PrimaryKey,
@Column, @Constraint, @Foreignkey e @EJB.

c) todas as operações realizadas nas tabelas do banco de dados, como inserção de dados,alteração, consultas e exclusão, são realizadas sem o uso de instruções SQL,
ou seja, o desenvolvedor não precisa conhecer SQL para programar.
d) as configurações de acesso a banco de dados normalmente ficam no arquivo persistence.xml,ligado à aplicação, de forma que se for alterado o servidor de banco de dados não seja necessário alterar o código-fonte Java da aplicação.
e) as relações existentes entre as tabelas do banco de dados não são refletidas nas classes de entidade criadas na aplicação, o que torna a execução mais rápida. O mapeamento de relações é feito em tempo de execução pelas bibliotecas do provedor de persistência.
Comentários:

(a) Provedor de Persistência é o framework que fornece meios de se fazer o mapeamento objeto/relacional - em geral, implementam a Especificação JPA. Dentro os listados, JBossSeam e JDBCProvider não realizam esse trabalho; (b) @EJB não auxilia no mapeamento entre objetos da classe e tabelas do banco de dados, (c) Vejam que ele citou as quatro operações básicas, mas existem outras e é possível que se necessite saber SQL para programar; (d)Perfeito, as configurações de acesso ao banco ficam no persistence.xml, permitindo mudanças de servidor de banco de dados sem a necessidade de alterar o código, (e) Claro que as relações devem ser refletidas nas classes de entidade (@OneToOne, @ManyToOne, etc). Gabarito: D
4. (CESPE - 2010 - MPU - Analista de Sistemas) A versão 3.0 da API de Persistência
Java utiliza descritores de implantação, não permitindo uso de anotações.
Comentários:

É interessante notar um pouco da evolução do Java Persistence API (JPA) e como ele evolui harmonicamente com o Ambiente Java EE. Ele apareceu pela primeira vez no Java EE 5(JSR220).
Depois ele se transformou em JPA 2.0 no Java EE 6 (JSR 317) e, atualmente, temos o
JPA 2.1 -
no Java EE 7 (JSR 338). De todo modo, ele consiste em quatro partes:

Essas ferramentas facilitam o mapeamento dos atributos de uma base de dados relacional para o modelo de objetos de uma aplicação por meio de Descritores de Implantação (XML) ouAnotações
(Annotations) - principalmente para consultas e atualizações de dados. O
desenvolvedor define

/ 235

/

como os objetos são mapeados e o framework faz o resto - acessa o banco, gera os comandosSQL, etc.

Conforme vimos em aula, não existe JPA 3.0 - vocês acham que a banca anulou? De todo modo,a versão atual permite - sim - a utilização de Descritores de Implantação e
Anotações. Gabarito:
E

5. (CESPE - 2010 - MPU - Analista de Sistemas) A versão 3.0 da API de
Persistência Java provê uma linguagem de consulta de persistência Java que é uma forma melhorada da linguagem de consulta do EJB.
Comentários:

É interessante notar um pouco da evolução do Java Persistence API (JPA) e como ele evolui harmonicamente com o Ambiente Java EE. Ele apareceu pela primeira vez no Java EE 5(JSR220).
Depois ele se transformou em JPA 2.0 no Java EE 6 (JSR 317) e, atualmente, temos o
JPA 2.1 -
no Java EE 7 (JSR 338). De todo modo, ele consiste em quatro partes:

Java Persistence API (JPA): define um mapeamento objeto/relacional para gerenciamento de dados relacionais;
Java Persistence Query Language (JPQL): define queries estáticas, em geral, para entidades e seus estados persistentes;
Java Persistence Criteria API (JPCA): define queries dinâmicas, em geral, para entidades e seus estados persistentes;
Mapeamento de Metadados O/R: define um mapeamento por meio de
Descritores de
Implantação (XML) ou Anotações (Annotations).

Conforme vimos em aula, não existe JPA 3.0 - vocês acham que a banca anulou? De todo modo,ele fornece - sim - uma linguagem de consulta de persistência: JPQL. De fato, ela é melhor que aEJB-QL, que existia anteriormente - vejamos o que diz o FAQ:

Q: What are some of the main features of the Java Persistence API?

A: The Java Persistence API is a POJO persistence API for object/relational mapping.
It contains a full object/relational mapping specification supporting the use of Java language metadata annotations and/or XML descriptors to define the mapping between Java objects and a relational database. It supports a rich, SQL-like query language (which is a significant extension upon EJBQL) for both static and dynamic queries. It also supports the use of pluggable persistence providers.
/ 235

/

Gabarito: C

6. (CESPE - 2010 - MPU - Analista de Sistemas) A API de Persistência Java é embasada em ideias contidas em frameworks líderes de mercado, como Hibernate, OracleTopLink e
Objetos de Dados Java.

Comentários:

Que tal, agora, entrar mais a fundo no JPA? Bem, os frameworks do mercado possuíam algumas diferenças! A Sun MicroSystems, então, fez uma proposta ao líder do Projeto Hibernate:fazer uma especificação com o objetivo de padronizar os frameworks de mapeamento objeto-relacional!Para tal, ele pegou as melhores ideias do Hibernate, TopLink, JDO, etc e condensou em uma especificação.
Conforme vimos em aula, JPA pegou as melhores ideias dos frameworks líderes de mercado e condensou em uma especificação. Gabarito: C
7. (CESPE - 2013 - TRE/MS - Analista de Sistemas) Assinale a opção correspondente ao elemento que, além de ser utilizado para definir um meio de mapeamento objeto-relacional para objetos Java simples e comuns (POJOs), denominados beans de entidade, também é utilizado para gerenciar o desenvolvimento de entidades do modelo relacional em plataforma nativa Java SE e Java EE.
a) JSF

b) SVN

c) JPA

d) spring e) struts
Comentários:

Em suma, podemos dizer que o JPA é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais em Aplicações Java - em outras palavras, ele simplifica a persistência de dados. Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
Rapidamente: algumas pessoas me perguntam qual a diferença entre um POJO e umJavaBean! Todo JavaBean é um POJO, mas nem todo POJO é um JavaBean. Eles são muito parecidos, mas o JavaBean segue diversas convenções de programação, tais como:nomenclatura dos métodos, construtor público padrão e sem parâmetros, entre outros. Para oJPA, o POJO é a unidade básica!

/ 235

/

E foi assim que surgiu o Java Persistence API (JPA)! Olha que engraçado: a especificação surgiu após as implementações! Como uma das vantagens, pode-se trocar de implementação(Ex:
Hibernate para TopLink) sem a necessidade de modificar o código-fonte. Enfim,
ele foi incorporado ao EJB 3.0 (apesar de ser independente deste), permitindo sua utilização emAmbientes Java SE e Java EE.

Ele também é importante para desacoplar o código da aplicação dos frameworks de infraestrutura. Mudou o framework? O POJO continuará funcionando - inclusive, a mudança será fácil e conterá menos riscos! Até a Especificação EJB 2.0, a persistência de dados era parte da Plataforma EJB e era realizada por meio de Entity Beans - que eram uma espécie de POJO.
Conforme vimos em aula, JPA é utilizado para realizar o mapeamento objeto/relacional,utilizando POJOs, em ambientes Java SE e Java EE. Gabarito: C

8. (FCC - 2012 - TJ-PE - Analista Judiciário - Análise de Sistemas) Quando se utiliza JPA, umEntityManager mapeia um conjunto de classes a um banco de dados particular.
Este conjunto de classes, definido em um arquivo chamado persistence.xml, é denominado:
a) persistence context.

b) persistence unit.

c) entity manager factory.

d) entity transaction.

e) persistence provider.

Comentários:

Lá em cima, eu afirmei que um EntityManager mapeava um conjunto de classes para um banco de dados particular. Esse conjunto de classes é denominado Persistence Unit. Antes mesmo de pensar em criar entidades ou consultá-las por meio do EntityManager, é necessário empacotar esse conjunto de classes em um Persistence Unit, que é definido no Descritor deImplantação
(persistence.xml).

Conforme vimos em aula, trata-se do Persistence Unit. Gabarito: B

9. (CESPE - 2013 - CNJ - Técnico Judiciário - Programação de Sistemas) Os objetos mapeados na linguagem Java que devem ser persistidos como objetos precisam utilizar JPA (JavaPersistence API), pois o JPA permite realizar o mapeamento objeto/relacional automatizado e transparente e sua persistência em um banco de dados relacional.
Comentários:

/ 235

/

Em suma, podemos dizer que o JPA é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais emAplicações Java - em outras palavras, ele simplifica a persistência de dados. Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
Pessoal, olhem que questão maluca! Você precisa necessariamente do JPA? Não, eu posso usar frameworks que não implementam o JPA. Discordo do gabarito! Gabarito: C
1O.(FGV - 2009 - MEC - Analista de Sistemas - C) JPA é uma tecnologia utilizada no desenvolvimento de aplicações para Web, similar às tecnologias Active Server Pages (ASP)da Microsoft ou PHP.

Comentários:

Em suma, podemos dizer que o JPA é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais emAplicações Java - em outras palavras, ele simplifica a persistência de dados. Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
Conforme vimos em aula, essa definição não faz sentido algum para JPA! No entanto,
substituindo
JPA por JSP, a definição seria perfeita! Gabarito: E

11.(CESPE - 2010 - TRE-BA - Programador de computador) As tecnologias JPA e
EJB
permitem, com o uso da linguagem Java, a manipulação de dados que estão em um banco de dados.
Comentários:

Em suma, podemos dizer que o JPA é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais emAplicações Java - em outras palavras, ele simplifica a persistência de dados. Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
Conforme vimos em aula, está perfeito - lembrando que JPA faz parte da Especificação do EJB
3.0. Gabarito: C

12.(CESPE - 2013 - CPRM - Analista em Geociências - Sistemas) Java Persistence API
(JPA) é uma solução para persistência de dados, utilizada, inclusive, quando há mapeamento do modelo orientado a objeto para bancos de dados relacionais.
/ 235

/

Comentários:

Em suma, podemos dizer que o JPA é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais emAplicações Java - em outras palavras, ele simplifica a persistência de dados. Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
Conforme vimos em aula, está perfeito - praticamente idêntica à definição! Gabarito: C

13.(CESPE - 2013 - TRE/MS - Analista de Sistemas - C) JPA é um framework MVC de aplicações web que se destina a simplificar o desenvolvimento de interfaces de usuário embasadas em web.
Comentários:

Em suma, podemos dizer que o JPA é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais emAplicações Java - em outras palavras, ele simplifica a persistência de dados. Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
Conforme vimos em aula, essa definição não faz sentido algum para JPA! No entanto,
substituindo
JPA por JSF, a definição seria perfeita! Gabarito: E

14.(CESPE - 2010 - TRE/MT - Analista de Sistemas - E) JPA lida com a forma como dados relacionais são mapeados para objetos Java e com a forma como esses objetos são armazenados em um banco de dados relacional.
Comentários:

Em suma, podemos dizer que o JPA é um padrão para persistência de dados que fornece aos desenvolvedores um mapeamento objeto/relacional para gerenciamento de dados relacionais emAplicações Java - em outras palavras, ele simplifica a persistência de dados. Ele pode ser utilizado pelo Container EJB, pelo Container Web ou pelo Application Client.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

15.(CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - II) JPA é parte integrante da especificação EJB e serve para definir as interfaces de acesso local e/ou remoto de um componente EJB.
,

Comentários:

E foi assim que surgiu o Java Persistence API (JPA)! Olha que engraçado: a especificação surgiu após as implementações! Como uma das vantagens, pode-se trocar de implementação(Ex:
Hibernate para TopLink) sem a necessidade de modificar o código-fonte.
Enfim, ele foi incorporado ao EJB 3.0 (apesar de ser independente dessa), permitindo sua utilização emAmbientes Java SE e Java EE.

Conforme vimos em aula, é parte integrante da Especificação EJB, mas é uma especificação de persistência para mapeamento objeto-relacional. Gabarito: E
16.(CESPE - 2012 - TJ-RO - Analista Judiciário - Análise de Sistemas - Desenvolvimento
- A)
JPA, um framework utilizado na camada de persistência, define uma forma para mapear
POJO (Plain Old Java Objects) para um banco de dados.

Comentários:

Rapidamente: algumas pessoas me perguntam qual a diferença entre um POJO e um JavaBean!
Todo JavaBean é um POJO, mas nem todo POJO é um JavaBean. Eles são muito parecidos,
mas o JavaBean segue diversas convenções de programação, tais como: nomenclatura dos métodos,construtor público padrão e sem parâmetros, entre outros. Para o JPA, o POJO é a unidade básica!

Conforme vimos em aula, a questão já começa errada! JPA é uma especificação e, não, um framework. Como ela não foi anulada, vamos continuar nossa avaliação da questão.Antigamente,
nós usávamos Entity Beans. Após o EJB 3.0 e o surgimento da Especificação JPA,
passamos a utilizar POJO - que são fracamente acoplados, simples e portáteis. Se ignorarmos o início, a questão está correta. Gabarito: C
17.(FCC - 2013 - MPE/MA - Analista de Sistemas) Considere a classe Java a seguir em uma aplicação que utiliza JPA, uma API que permite fazer o mapeamento de persistência objeto/relacional:
package dao;

import javax.persistence.*;
public class ClienteDao {

private EntityManagerFactory emf;
private EntityManager em;

private EntityTransaction et;

,

private void iniciarTransacao()

{

emf = Persistence.createEntityManagerFactory(" Exemplo");
em = emf.createEntityManagerO;

et = em.getTransactionO;
et.begin();

}

}

O parâmetro "Exemplo", passado para o método createEntityManagerFactory da classePersistence refere-se ao nome:

a) da unidade de persistência definido na tag persistence-unit contida no arquivo persistence.xml.

b) do arquivo de persistência Exemplo.xml que contém as tags com os parâmetros de conexão com o banco de dados.
c) do banco de dados relacional ao qual a aplicação deseja se conectar.

d) da tabela do banco de dados na qual os dados da aplicação serão persistidos.

e) da classe que faz a conexão com o banco de dados relacional ao qual a aplicação deseja se conectar.
Comentários:

É importante notar que a classe javax.persistence.Persistence procura o Descritor de
Implantação persistence.xml dentro de seu classpath. Ele procurará o Persistence Unit com o mesmo nome do parâmetro da função createEntityManagerFactory, i.e., "Exemplo".Obtido o
EntityManagerFactory, basta chamar a função createEntityManager.

Conforme vimos em aula (e esse é um exemplo padrão, logo a questão veio com os mesmos nomes), o parâmetro é o Persistence Unit definido no Descritor de Implantação(persistence.xml).
Gabarito: A

18. (FCC - 2012 - TJ-PE - Programador de computador) Em uma classe de entidade de uma aplicação que utiliza JPA, a anotação que define um atributo que não será salvo no banco de dados é a:
a) @Optional.

b) @Transient c) @Stateless.
/ 235

/

d) @Stateful.

e) @Local.

Comentários:

ANOTAÇÃO DESCRIÇÃO

@Entity Indica que uma classe é uma entidade que deve ser persistida como tabela.
@Table Indica o nome de uma tabela para qual a entidade é mapeada.

@Column Indica que um atributo de uma classe é uma coluna de uma tabela.
@ld Indica que um atributo é a chave primária de uma entidade.

@namedQuery Define uma consulta.

@namedQueries Define várias consultas.

@UniqueConstraint Indica que uma propriedade não pode conter valores duplicados.

@Transient Indica que uma propriedade não deve ser persistida no banco de dados.
@lnheritance Define um relacionamento de herança à entidade.
@ManyToOne Mapeamento muitos para um (N:1).
@OneToMany Mapeamento um para muitos (1 :N).
@OneToOne Mapeamento um para um (1:1).

Conforme vimos em aula, trata-se da anotação @Transient. Gabarito: B

19. (FCC - 2011 - TRT - 19a Região (AL) - Técnico Judiciário - Tecnologia da
Informação) Os estados do ciclo de vida de uma instância de uma entidade, definidos na JPA 2.0, são:
a) novo (new), gerenciado (managed), destacado (detached) e removido (removed).

b) ativo (active), inativo (inactive) e removido (removed).

/ 235

/

c) novo (new), temporário (temporary), permanente (permanent) e destacado (detached).

d) novo (new), temporário (temporary) e destacado (detached)

e) gerenciado (managed), temporário (temporary), permanente (permanent) e destacado(detached).

Comentários:

O ciclo de vida dos objetos de entidade consiste em quatro estados: Novo (New),
Gerenciado
(Managed), Removido (Removed) e Destacado (Detached). Quando um objeto é criado inicialmente seu estado é Novo. Nesse estado, o objeto ainda não está associado a umEntityManager e não possui qualquer representação no banco de dados. Bacana?

Conforme vimos em aula, trata-se da primeira opção! Gabarito: A

20. (FEPESE - 2013 - JUCESC - Analista Técnico em Gestão de Registro Mercantil -
Analista de Informática) Em relação à JPA e Hibernate, considere as seguintes afirmativas.
1. JPA especifica uma JSR.

2. Hibernate especifica uma JSR.

3. Hibernate cuida da camada de persistência enquanto JPA da camada de transação.

4. Hibernate é uma implementação de JSR.

5. JPA é uma implementação de JSR.

Assinale a alternativa que indica todas as afirmativas corretas.

a) São corretas apenas as afirmativas 1 e 4.

b) São corretas apenas as afirmativas 2 e 3.

c) São corretas apenas as afirmativas 3 e 4.

d) São corretas apenas as afirmativas 1,2 e 3.

e) São corretas apenas as afirmativas 3, 4 e 5

Comentários:

/ 235

/

Que tal, agora, entrar mais a fundo no JPA? Bem, os frameworks do mercado possuíam algumas diferenças! A Sun MicroSystems, então, fez uma proposta ao líder doProjeto
Hibernate: fazer uma especificação com o objetivo de padronizar os frameworks de mapeamento objeto-relacional! Para tal, ele pegou as melhores ideias do Hibernate,TopLink,
JDO, etc e condensou em uma especificação.

(1) Quando se cria uma especificação, dá-se um Número de JSR (Ex: JPA é JSR 338; JTA é
JSR
907; JMS é JSR 914; JSF é JSR 314, etc), portanto JPA especifica, sim, uma JSR; (2)
Não,
Hibernate implementa uma JSR; (3) Não, JPA também cuida da Camada de Persistência; (4)
Perfeito, é uma implementação de JSR; (4) Não, JPA é uma especificação de JSR.

Gabarito: A

21. (FCC - 2011 - TCE/PR - Analista de Sistemas) A JPA:

a) pode ser usada fora de componentes EJB e fora da plataforma Java EE, em aplicações JavaSE.

b) utiliza persistência gerenciada por contêiner (CMP), ou seja, as classes de entidade e persistência necessitam de um contêiner presente em um servidor de aplicações para serem executadas.
c) utiliza descritores XML para especificar informações do mapeamento relacional de objeto,mas não oferece suporte a anotações.

d) suporta consultas dinâmicas nomeadas nas classes de entidade que são acessadas apenas por instruções SQL nativas.
e) possui uma interface EntityBeans que padroniza operações Create Read Update
Delete
(CRUD) que envolvem tabelas.

Comentários:

E foi assim que surgiu o Java Persistence API (JPA)! Olha que engraçado: a especificação surgiu após as implementações! Como uma das vantagens, pode-se trocar de implementação(Ex:
Hibernate para TopLink) sem a necessidade de modificar o código-fonte. Enfim,
ele foi incorporado ao EJB 3.0 (apesar de ser independente dessa), permitindo sua utilização emAmbientes Java SE e Java EE.

(a) Conforme vimos em aula, pode ser usada independente do EJB 3.0, inclusive em
Ambiente
Java SE.

(b) Esse item é obsoleto atualmente. Não vale a pena discuti-lo, vai confundir a cabeça de vocês. Está errado!
/ 235

/

Essas ferramentas facilitam o mapeamento dos atributos de uma base de dados relacional para o modelo de objetos de uma aplicação por meio de Descritores de Implantação(XML) ou
Anotações (Annotations) - principalmente para consultas e atualizações de dados. Odesenvolvedor define como os objetos são mapeados e o framework faz o resto - acessa o banco, gera os comandos SQL, etc.
(c) Conforme vimos em aula, pode-se utilizar Descritores de Implantação (XML) e
Anotações
(Annotations).

Java Persistence API (JPA): define um mapeamento objeto/relacional para gerenciamento de dados relacionais;
Java Persistence Query Language (JPQL): define queries, em geral, estáticas, para entidades e seus estados persistentes;
Java Persistence Criteria API (JPCA): define queries, em geral, dinâmicas para entidades e seus estados persistentes;
Mapeamento de Metadados O/R: define um mapeamento por meio de
Descritores de
Implantação (XML) ou Anotações (Annotations).

(d) Conforme vimos em aula, pode-se utilizar JPQL e JPCA, com acesso feito por SQL ou Java.

Galera, vocês sabem o que é um EntityManager? Trata-se de uma interface que funciona como serviço centralizado para todas as ações de persistência - mapeando um conjunto de classes para um banco de dados particular. Em outras palavras, ele é responsável por realizar operações de sincronismo com o Banco de Dados (Inserir, Remover, Atualizar eConsultar),
além de gerenciar o ciclo de vida das entidades.

(e) Conforme vimos em aula, o responsável por isso é a interface EntityManager.

Gabarito: A

22.(FCC - 2011 - TRT - 23a REGIÃO (MT) - Técnico Judiciário - Tecnologia da Informação) Em relação à JPA (Java Persistence API) é INCORRETO afirmar que:
/ 235

/

©Entity

@Table(name - "domic")
@NamedQueries ({

@NamedQuery(name - "Domic.findByid", query - "SELECT r FRoM Domic r wHERE r.id - :1d"),
@NamedQuery(name « "Domic.findByNome", query = "SELECT r FRoM Domic r wHERE r.nome = :nome")

public class Domic implements serializable {
private static final long serialversionuiD = 1L;
@ld

@column(name = "id", nullable - false)
private integer id;

@column(name = "nome")
private string nome;

@oneToMany(cascade = cascadeType.ALL, mappedBy = "domicld")
private collection<Predio> prediocoliection;

a) @NamedQuery é aplicada para definir várias consultas.

b) ©Entity define que haverá correspondência da classe com uma tabela do banco de dados.

c) @ld define que o atributo que está mapeado com tal anotação corresponderá à chave primária da tabela.
d) @Column(name = "id", nullable = false) define que o atributo da classe mapeado com tal anotação deve estar associado à coluna cujo nome é "id", além de definir que tal campo não pode ser nulo.
e) @OneToMany indica que o atributo contém um conjunto de entidades que a referenciam.

Comentários:

ANOTAÇÃO

DESCRIÇÃO

@Entity Indica que uma classe é uma entidade que deve ser persistida como tabela.
@Table Indica o nome de uma tabela para qual a entidade é mapeada.

@Column Indica que um atributo de uma classe é uma coluna de uma tabela.
@ld Indica que um atributo é a chave primária de uma entidade.

@namedQuery Define uma consulta.

@namedQueries Define várias consultas.

@UniqueConstraint Indica que uma propriedade não pode conter valores duplicados.

@Transient Indica que uma propriedade não deve ser persistida no banco de dados.
@lnheritance Define um relacionamento de herança à entidade.
@ManyToOne Mapeamento muitos para um (N:1).
@OneToMany Mapeamento um para muitos (1 :N).
@OneToOne Mapeamento um para um (1:1).

Conforme vimos em aula, namedQuery define apenas uma consulta! A Anotação namedQueries é quem define diversas consultas! Gabarito: A
LISTA DE QUESTõES - JPA- MULTIBANCAS

1. (FCC - 2007 - TRE/MS - Analista de Sistemas - III) A API de Persistência Java pode ser utilizada no container Web e/ou no container EJB e disponibiliza recursos de mapeamento objeto-relacional as aplicações Java EE.
2. (CESPE - 2014 - TJ-SE - Analista Judiciário - Banco de Dados) A JPA, que foi criada como alternativa para o Hibernate para conexão com os sistemas gerenciadores de banco de dados, está nativa no Java SE a partir da versão 1.3.
3. (FCC - 2014 - TRT - 13a Região (PB) - Técnico Judiciário - Tecnologia da
Informação) Java
Persistence API (JPA) é uma API padrão da linguagem Java para persistência de dados em bancos de dados relacionais. Em uma aplicação que utiliza JPA:
a) pode ser utilizada, como provedor de persistência, as bibliotecas
EclipseLink, Hibernate,
OracleTopLink, JBossSeam e JDBCProvider.

b) as classes de entidade do banco de dados permitem o mapeamento entre objetos da classe e tabelas do banco de dados, utilizando anotações como @Table, @Entity,@PrimaryKey,
@Column, @Constraint, @Foreignkey e @EJB.

c) todas as operações realizadas nas tabelas do banco de dados, como inserção de dados,alteração, consultas e exclusão, são realizadas sem o uso de instruções SQL,
ou seja, o desenvolvedor não precisa conhecer SQL para programar.
d) as configurações de acesso a banco de dados normalmente ficam no arquivo persistence.xml, ligado à aplicação, de forma que se for alterado o servidor de banco de dados não seja necessário alterar o código-fonte Java da aplicação.
e) as relações existentes entre as tabelas do banco de dados não são refletidas nas classes de entidade criadas na aplicação, o que torna a execução mais rápida. O mapeamento de relações é feito em tempo de execução pelas bibliotecas do provedor de persistência.
4. (CESPE - 2010 - MPU - Analista de Sistemas) A versão 3.0 da API de
Persistência Java utiliza descritores de implantação, não permitindo uso de anotações.
5. (CESPE - 2010 - MPU - Analista de Sistemas) A versão 3.0 da API de
Persistência Java provê uma linguagem de consulta de persistência Java que é uma forma melhorada da linguagem de consulta do EJB.
6. (CESPE - 2010 - MPU - Analista de Sistemas) A API de Persistência Java é embasada em ideias contidas em frameworks líderes de mercado, como Hibernate, OracleTopLink e
Objetos de Dados Java.

,

7. (CESPE - 2013 - TRE/MS - Analista de Sistemas) Assinale a opção correspondente ao elemento que, além de ser utilizado para definir um meio de mapeamento objeto-relacional para objetos Java simples e comuns (POJOs), denominados beans de entidade, também é utilizado para gerenciar o desenvolvimento de entidades do modelo relacional em plataforma nativa Java SE e Java EE.
a) JSF

b) SVN

c) JPA

d) spring e) struts
8. (FCC - 2012 - TJ-PE - Analista Judiciário - Análise de Sistemas) Quando se utiliza JPA, umEntityManager mapeia um conjunto de classes a um banco de dados particular.
Este conjunto de classes, definido em um arquivo chamado persistence.xml, é denominado:
a) persistence context.

b) persistence unit.

c) entity manager factory.

d) entity transaction.

e) persistence provider.

9. (CESPE - 2013 - CNJ - Técnico Judiciário - Programação de Sistemas) Os objetos mapeados na linguagem Java que devem ser persistidos como objetos precisam utilizar JPA (JavaPersistence API), pois o JPA permite realizar o mapeamento objeto/relacional automatizado e transparente e sua persistência em um banco de dados relacional.
1O.(FGV - 2009 - MEC - Analista de Sistemas - C) JPA é uma tecnologia utilizada no desenvolvimento de aplicações para Web, similar às tecnologias Active Server Pages (ASP)da Microsoft ou PHP.

11.(CESPE - 2010 - TRE-BA - Programador de computador) As tecnologias JPA e
EJB
permitem, com o uso da linguagem Java, a manipulação de dados que estão em um banco de dados.
12.(CESPE - 2013 - CPRM - Analista em Geociências - Sistemas) Java Persistence API
(JPA) é uma solução para persistência de dados, utilizada, inclusive, quando há mapeamento do modelo orientado a objeto para bancos de dados relacionais.
,

13.(CESPE - 2013 - TRE/MS - Analista de Sistemas - C) JPA é um framework MVC de aplicações web que se destina a simplificar o desenvolvimento de interfaces de usuário embasadas em web.
14.(CESPE - 2010 - TRE/MT - Analista de Sistemas - E) JPA lida com a forma como dados relacionais são mapeados para objetos Java e com a forma como esses objetos são armazenados em um banco de dados relacional.
15.(CESGRANRIO - 2011 - PETROBRÁS - Analista de Sistemas - II) JPA é parte integrante da especificação EJB e serve para definir as interfaces de acesso local e/ou remoto de um componente EJB.
16.(CESPE - 2012 - TJ-RO - Analista Judiciário - Análise de Sistemas - Desenvolvimento
- A)
JPA, um framework utilizado na camada de persistência, define uma forma para mapear
POJO (Plain Old Java Objects) para um banco de dados.

17.(FCC - 2013 - MPE/MA - Analista de Sistemas) Considere a classe Java a seguir em uma aplicação que utiliza JPA, uma API que permite fazer o mapeamento de persistência objeto/relacional:
package dao;

import javax.persistence.*;
public class ClienteDao {

private EntityManagerFactory emf;
private EntityManager em;

private EntityTransaction et;
private void iniciarTransacao()

{

emf = Persistence.createEntityManagerFactoryC Exemplo11);
em = emf.createEntityManager();

et = em.getTransactionO;
et.begin();

}

}

O parâmetro "Exemplo", passado para o método createEntityManagerFactory da classe
Persistence refere-se ao nome:

/ 235

/

a) da unidade de persistência definido na tag persistence-unit contida no arquivo persistence.xml.
b) do arquivo de persistência Exemplo.xml que contém as tags com os parâmetros de conexão com o banco de dados.
c) do banco de dados relacional ao qual a aplicação deseja se conectar.

d) da tabela do banco de dados na qual os dados da aplicação serão persistidos.

e) da classe que faz a conexão com o banco de dados relacional ao qual a aplicação deseja se conectar.
18. (FCC - 2012 - TJ-PE - Programador de computador) Em uma classe de entidade de uma aplicação que utiliza JPA, a anotação que define um atributo que não será salvo no banco de dados é a:
a) @Optional.

b) @Transient.

c) @Stateless.

d) @Stateful.

e) @Local.

19.(FCC - 2011 - TRT - 19a Região (AL) - Técnico Judiciário - Tecnologia da
Informação) Os estados do ciclo de vida de uma instância de uma entidade, definidos na JPA 2.0, são:
a) novo (new), gerenciado (managed), destacado (detached) e removido (removed).

b) ativo (active), inativo (inactive) e removido (removed).

c) novo (new), temporário (temporary), permanente (permanent) e destacado (detached).

d) novo (new), temporário (temporary) e destacado (detached)

e) gerenciado (managed), temporário (temporary), permanente (permanent) e destacado(detached).

2O.(FEPESE - 2013 - JUCESC - Analista Técnico em Gestão de Registro Mercantil -
Analista de
Informática) Em relação à JPA e Hibernate, considere as seguintes afirmativas.

1. JPA especifica uma JSR.

2. Hibernate especifica uma JSR.

3. Hibernate cuida da camada de persistência enquanto JPA da camada de transação.

4. Hibernate é uma implementação de JSR.

5. JPA é uma implementação de JSR.

Assinale a alternativa que indica todas as afirmativas corretas.

a) São corretas apenas as afirmativas 1 e 4.

b) São corretas apenas as afirmativas 2 e 3.

c) São corretas apenas as afirmativas 3 e 4.

d) São corretas apenas as afirmativas 1, 2 e 3.

e) São corretas apenas as afirmativas 3, 4 e 5

21 .(FCC - 2011 - TCE/PR - Analista de Sistemas) A JPA:

a) pode ser usada fora de componentes EJB e fora da plataforma Java EE, em aplicações JavaSE.

b) utiliza persistência gerenciada por contêiner (CMP), ou seja, as classes de entidade e persistência necessitam de um contêiner presente em um servidor de aplicações para serem executadas.
c) utiliza descritores XML para especificar informações do mapeamento relacional de objeto,mas não oferece suporte a anotações.

d) suporta consultas dinâmicas nomeadas nas classes de entidade que são acessadas apenas por instruções SQL nativas.
e) possui uma interface EntityBeans que padroniza operações Create Read Update
Delete
(CRUD) que envolvem tabelas.

22. (FCC - 2011 - TRT - 23a REGIÃO (MT) - Técnico Judiciário - Tecnologia da Informação) Em relação à JPA (Java Persistence API) é INCORRETO afirmar que:
©Entity

@Table(name - "domic")
@NamedQueries ({

@NamedQuery(name - "Domic.findByid", query - "SELECT r FRoM Domic r wHERE r.id - :1d"),
@NamedQuery(name « "Domic.findByNome", query = "SELECT r FRoM Domic r wHERE r.nome = :nome")

public class Domic implements serializable {
private static final long serialversionuiD = 1L;
@ld

@column(name = "id", nullable - false)
private integer id;

@column(name = "nome")
private string nome;

@oneToMany(cascade = cascadeType.ALL, mappedBy = "domicld")
private collection<Predio> prediocoliection;

a) @NamedQuery é aplicada para definir várias consultas.

b) @Entity define que haverá correspondência da classe com uma tabela do banco de dados.

c) @ld define que o atributo que está mapeado com tal anotação corresponderá à chave primária da tabela.
d) @Column(name = "id", nullable = false) define que o atributo da classe mapeado com tal anotação deve estar associado à coluna cujo nome é "id", além de definir que tal campo não pode ser nulo.
e) @OneToMany indica que o atributo contém um conjunto de entidades que a referenciam.

,

GABARITo

GABARITO

lo

1. c 8. B
15. E

2. E 9. C
16. C

3. D 10. E
17. A

4. E 11. C
18. B

5. C 12. C
19. A

6. C 13. E
20. A

7. C 14. C
21. A

SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023 (Pós-I

HIBERNATE

^HIBERNATE

Galera, Java começou a ficar extremamente popular em ambientes corporativos,
mas havia um problema que estava incomodando os desenvolvedores: a produtividade estava prejudicada porque eles estavam perdendo muito tempo nas codificações de Queries SQL e em códigosJDBC.
E quando era necessário mudar o banco de dados por um de outro fabricante? O que fazer?

Além disso, Java ajudou a divulgar o Paradigma Orientado a Objetos, em que informações eram representadas por meio de classes, atributos, herança, polimorfismo,encapsulamento, etc. Isso gerava conflito com o Paradigma Relacional dos bancos de dados, em que as informações eram representadas por meio de tabelas, colunas, linhas, chaves primárias, chaves estrangeiras, etc.
Pois bem! Era trabalhoso transformar objetos de uma classe em registros de uma tabela e vice-versa. Logo, começaram a surgir alguns frameworks que auxiliavam essa tarefa - são as famosasFerramentas de ORM - Object-Relational Mapping (ou Mapeamento Objeto-Relacional).
As mais conhecidas eram Hibernate e TopLink - a primeira, livre, open-source, tornou-se uma referência mundial1 .
Essas ferramentas facilitam o mapeamento dos atributos de uma base de dados relacional para o modelo de objetos de uma aplicação por meio de mapeamentos, comoDescritores de
Implantação (XML) ou Anotações (Annotations) - principalmente para consultas e atualizações de dados. O desenvolvedor define como os objetos são mapeados e o framework faz o resto.
O trabalho do desenvolvedor é definir como os objetos são mapeados nas tabelas do banco de dados e o Hibernate faz todo o acesso ao banco, gerando inclusive o código SQLnecessário - não é necessário fazer SELECT, UPDATE, INSERT, DELETE, etc! Permite fazer uma persistência automática entre classes e tabelas, propriedades e colunas, associações e chaves estrangeiras,tipos Java e tipos SQL, entre outros.

1 Hibernate tornou-se um framework tão popular que acabou por ser utilizado como referência para construção da Especificação de Persistência Java (JPA). Apesar disso, ele também é oferecido para executar a mesma função na plataforma .NET - é o famosoNHibernate.

OBSERVAÇÕES

O Mapeamento Objeto-Relacional (ORM) funciona com a transformação dos dados de um objeto em uma tupla (linha) de uma tabela de um banco de dados, ou de forma inversa, com a transformação de uma tupla (linha) da tabela em um objeto da aplicação - é um relacionamento bidirecional.
Quando utilizamos o Hibernate para realizar consultas no banco de dados, temos a oportunidade de trabalhar com SQL (Structured Query Language), HQL (Hibernate QueryLanguage) e com
Criteria Query API. Esta última fornece uma maneira elegante de construção de queries dinâmicas para consultas no banco de dados. A API é uma alternativa às Consultas HQL e também ao SQLtradicional.

Lembrando que o HQL é uma linguagem muito parecida com o SQL. No entanto, comparado a este último, o HQL é totalmente orientado a objetos, e compreende noções de herança,polimorfismo e associações. Dessa forma, ele se aproxima mais das regras de negócio das aplicações, visto que essas também são escritas em geral em um paradigma orientado a objetos.
Vocês percebem a diferença entre essas duas linguagens de consulta? SQL é uma linguagem relacional e HQL é uma linguagem orientada a objetos. A sintaxe é bastante parecida,inclusive existem várias cláusulas em comum, mas elas operam sobre objetos persistentes e suas propriedades em vez de tabelas e colunas. Bacana? Nice! ;-)
Christian Bauer afirma que o Hibernate é uma ferramenta que transforma os dados da estrutura lógica de um banco de dados em objetos definidos pelo desenvolvedor. Usando oHibernate, não há a necessidade de escrever muito do código de manipulação de banco de dados, pois ele utilizaHQL, acelerando a velocidade do seu desenvolvimento de uma forma fantástica.

Ele continua por dizer que se pode mudar a qualquer momento o SGDB utilizado. O
framework não é uma boa ferramenta para aplicações que fazem uso extensivo de stored procedures,triggers ou que implementam a maior parte da lógica da aplicação no banco de dados, contando com um modelo de objetos simples - não vai se beneficiar com o uso do Hibernate.
Vocês sacaram? Ele é mais indicado para sistemas que contam com um modelo mais rico,
em que a maior parte da lógica de negócios fica na própria aplicação, dependendo pouco de funções específicas do banco de dados. Ora, se a lógica de negócio estiver no banco de dados, não faz muito sentido utilizar o Hibernate, porque ele continuará manipulando o banco de dados diretamente.
/ 235

/

OBSERVAÇÕES

Quando da utilização de Hibernate, não é proibitiva a utilização de SQLI Galera...
vejam só: é muito difícil trabalhar com dois paradigmas conceituais diferentes. Antigamente,perdia-se muito tempo criando instruções SQL para transformar objetos em tuplas do banco de dados -esse era um processo exaustivo e cheio de falhas. O Mapeamento Objeto-Relacional propõe a transformação de classes e objetos em tabelas e tuplas de maneira fácil e reutilizável.
Em vez de o desenvolvedor criar todas as instruções SQL, ele pode utilizar um framework sem sair do paradigma de orientação a objetos e de maneira transparente. Assim,todo aquele trabalho árduo de codificação e testes se resume a algumas configurações e um mínimo de código, sem manter um contato direto com o banco de dados. O Hibernate fornece o papel de persistência, de forma praticamente transparente para o programador,i.e., ele praticamente só usa anotações e interfaces!
Além do oferecer Mecanismos de ORM, o framework também pode trabalhar com um sistema de cache das informações do banco de dados, aumentando ainda mais a performance das aplicações.O esquema de cache é complexo e extensível, existindo diversas implementações possíveis.
Um recurso interessante é o Query Cache, que permite fazer um cache das queries executadas diversas vezes.
Hibernate: Arquitetura

A imagem abaixo mostra de maneira absurdamente abstrata uma sugestão de arquitetura em que o Hibernate funciona como uma Camada de Persistência que conecta os objetos da aplicação a uma base de dados relacional. As classes, interfaces e outros componentes são definidos no pacote org.hibernate. Além disso, existem três arquivos de configuração:hibernate.cfg.xml,
hibernate.properties e hbm.xml.

Application
Persistent Objects

Hibernate hibernate.properties

XML Mapping

Database

Qual a diferença entre eles, professor? O primeiro e o segundo executam a mesma função, i.e.,configurar um serviço hibernate. Se ambos estiverem configurados, o primeiro sobrescreve o segundo. Ele contém informações sobre o local em que se encontra o banco de dados;conexões,
usuário, senha, propriedades; tipo de cache utilizado; local onde se encontram os caminhos para os arquivos hbm.xml; etc:
<?xml version=" 1.0" encoding="UTF-8"?>
http://www.hibernate.Org/dtd/hibernate-configuration-3.0.dtd">

<hibernate-configuration>

<session-factory>

<property name="hibernate.connection.driver_class">com.mysql.jdbc.Driver</property>

<property name="hibernate.connection.uri">jdbc:mysql://localhost/banco_dados</property>
<property name= "hibernate.connection.username">usuario</property>

<property name="hibernate.connection.password"/>senha</property>

<property name="hibernate.dialect">org.hibernate.dialect.MySQLDialect</property>

<property name= "show_sql">true</property>

<property name="hibernate.format_sql" >true</property>

<property name="hibernate.generate_statistics">true</property>

<mapping resource="classePOJO.hbm.xml"/>

</session-factory>

</hibernate-configuration>

,

Observem também que ele configura a SessionFactory, que é a classe utilizada pelo
Hibernate para interagir com o banco de dados por meio de sessões. Por fim, o arquivo hbm.xml é responsável por mapear o banco de dados, informando o nome da tabela, tipo de dados,identificadores, entre outros - como pode ser visto representado no código abaixo.

<?xml version = " 1.0" encoding="UTF-8"?>
http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd">

<hibernate-mapping>

<class name="aplicacao.exemplo" table="tabela_exemplo">

<id column="id" name="id" type="java.lang.Long">

<generator class=" native"></generator>

</id>

<property column = "nome" name="nome" length = "50" type="java.lang.String"/>

<property column = "email" name="email" length="50" type="java.lang.String"/>

<property column="data_nascimento" name="data_nascimento" type="java.util.Date"/>

</class>

</hibernate-mapping>

Em outras palavras, o primeiro arquivo trata principalmente da interação com o banco de dados.Já o segundo trata do mapeamento de classe do modelo de domínio orientado a objetos para uma base de dados relacional. É uma boa prática de programação criar um arquivo de mapeamento hbm.xml individuais para cada classe de persistência1 e, então,referenciá-la e mapeá-la no cfg.xml.
Prosseguindo... há ainda uma forma de representar a arquitetura de maneira mais ampla,
conforme é apresentado na imagem acima! Observem que entre a Aplicação e o Banco de Dados,temos uma camada de persistência do Hibernate (com seus componentes - alguns opcionais) e temos uma camada de APIs (JNDI, JDBC e JTA). Vamos ver alguns desses componentes responsáveis por controlar transações:
2 Classes Persistentes não precisam implementar interfaces ou herdar de uma classe-base especial!

* Session (org.hibernate.Session): trata-se de um objeto leve, single-threaded, de vida curta que representa uma comunicação entre a aplicação e os objetos persistentes, através de uma conexão JDBC. É criada por uma SessionFactory e é instanciada cada vez que uma interação com o banco de dados for necessária. É por meio dela que objetos persistentes são salvos e recuperados.
* SessionFactory (org.hibernate.SessionFactory): trata-se de um objeto pesado,
thread-safe e imutável de coleções de mapeamentos objeto-relacional para um único banco de dados -deve existir apenas uma instância na aplicação. É uma fábrica de sessões é necessário umSessionFactory por banco de dados utilizando um arquivo de configuração separado -semelhante ao EntityManagerFactory do JPA.

* Transaction (org.hibernate.Transaction): trata-se de um objeto single-threaded de vida curta utilizado por uma aplicação para especificar unidades indivisíveis e atômicas de uma operação de manipulação de dados. Ele abstrai os detalhes de transações de camadas inferiores, sendo opcional - o desenvolvedor escolhe se o utiliza ou se gerencia transações em seu próprio código de aplicação.
* Configuration (org.hibernate.Configuration): trata-se de um objeto utilizado para realizar as configurações de inicialização do Hibernate. Por meio dele,definem-se diversas configurações (driver de banco, dialeto, etc) e, a partir de uma instância desse objeto,indica-se como os mapeamentos entre classes e tabelas de banco de dados devem ser realizados.
OBSERVAÇÕES

Classes Persistentes são aquelas que implementam as entidades de domínio de negócio! O
Hibernate trabalha associando cada tabela do banco de dados a um POJO (Plain Old Java
Object) - que nada mais é que um objeto simples que possui um construtor padrão sem argumentos.
Hibernate: Ciclo De Vida Da Persistência

Agora vamos falar um pouco sobre os estados de um objeto no Hibernate! Nas diversas aplicações existentes, sempre que for necessário propagar o estado de um objeto que está em memória para o banco de dados ou vice-versa, há a necessidade de que a aplicação interaja com uma camada de persistência. Isto é feito, invocando o gerenciador de persistência e as interfaces de consultas do Hibernate.
Quando interagindo com o mecanismo de persistência, é necessário ter conhecimento sobre os estados do ciclo de vida. Em aplicações orientadas a objetos, a persistência permite que um objeto continue a existir mesmo após a destruição do processo que o criou. Na verdade, o que continua a existir é seu estado, já que pode ser armazenado em disco e então ser recriado em um novo objeto.
Galera, um objeto de classes persistentes pode estar em um dos três diferentes estados:Transiente (Transient), Persistente (Persistent) ou Desanexado (Detached), como nós podemos ver representado na imagem acima! Bem, vamos falar agora um pouquinho sobre cada um desses estados - eu recomendo que vocês entendam bem o funcionamento:
* Transiente: a instância não esteve nem está associada a um contexto persistente,
isto é, não há uma representação no banco de dados, nem um valor identificador. Ela é instanciada,utilizada, destruída e não pode ser reconstruída de forma automática.

* Persistente: a instância está atualmente associada a um contexto persistente, isto é, há uma representação no banco de dados e um valor identificador. Qualquer mudança em um objeto nesse estado é detectada e sincronizada com a base de dados.
/ 235

/

* Desanexado: a instância foi associada a um contexto persistente3, no entanto não está mais associada por alguma razão (Ex: Fim de sessão). Ainda existe uma referência, o objeto ainda pode ser modificado e essas modificações podem futuramente ser persistidas - trata-se de um estado intermediário.
O processo funciona assim: cria-se, inicialmente, o objeto POJO! Ele estará em estado transiente,i.e., não foi persistido, não representa uma linha no banco de dados e não está associado a uma sessão. Quando o objeto é salvo ou atualizado, ele finalmente é persistido, i.e.,representa uma linha no banco de dados e está associado a uma única sessão.
Caso o objeto seja despejado, fechado ou o cache seja limpado, ele se torna desanexado, i.e., ele tem uma entrada no banco de dados, porém não está conectado a nenhuma sessão. Caso ele seja atualizado, salvo, atualizado ou trancado, ele volta para o estado persistente. E se,depois disso,
ele for deletado, volta para o estado transiente.

3Contexto Persistente é outro nome para o objeto Session do Hibernate.

Hibernate: Anotações E Tipos De Mapeamento

Para finalizar, vamos falar um pouco sobre anotações! As anotações podem ser definidas como metadados que aparecem no código fonte e são ignorados pelo compilador.Qualquer símbolo em um código Java que comece com uma @ (arroba) é uma anotação. Este recurso foi introduzido na linguagem Java a partir da versão Java SE 5.0. As anotações mais comuns são:
ANOTAÇÃO DESCRIÇÃO

@Table

Utilizada para especificar detalhes da tabela que serão utilizados para persistir entidades na base de dados. Caso essa anotação seja omitida, não resultará em erro, porém será utilizado o nome da classe como valor default. Dessa forma, apenas definimos a anotação se quisermos sobrescrever o nome da classe. Possui os atributos: name, catalog, schema.
@ld Utilizada para especificar qual propriedade da tabela será a identificadora, isto é, será a chave primária. Pode ser um campo único ou a combinação de múltiplos campos dependendo da estrutura da tabela.
@Column

Utilizada para especificar detalhes da coluna para o qual um campo ou propriedade será mapeado. Pode-se utilizar essa anotação com os atributos: name, length, nullable e unique.
@Entity

Utilizada para marcar uma classe como uma Entidade ou POJO.
Deve conter um construtor sem argumentos que seja visível com o menor escopo de proteção.
Em outras palavras, as anotações marcam partes de objetos de forma que tenham algum significado especial. Quanto ao mapeamento, devemos ter alguns cuidados especiais com seus tipos! Como assim, professor? Quando preparamos um documento de mapeamento de tipos, nós mapeamos tipos de dados Java para tipos de dados usados em bases de dados relacionais.
Os tipos declarados e utilizados nos arquivos de mapeamento não são tipos de dados
Java nem tipos de dados SQL - eles são denominados Tipos Hibernate e podem traduzir do Java para SQLe vice-versa. Entenderam bem? Eles podem até ter nomes parecidos, mas não são iguais(Hibernate: float; Java: Float; SQL: FLOAT). Vejamos a tabela abaixo com os tipos primitivos:

Tipo de
Mapeamento

Tipo Java Tipo SQL

integer long short float double big decimal character string byte boolean yes/no true/false int or java.lang.Integer long or java.lang.Long short or java.lang.Short float or java.lang.Float double or java.lang.Double java.math.BigDecimal java.lang.String java.lang.String byte or java.lang.Byte boolean or java.lang.Boolean boolean or java.lang.Boolean boolean or java.lang.Boolean
INTEGER
BIGINT
SMALLINT
FLOAT

DOUBLE

NUMERIC
CHAR(1)

VARCHAR

TINYINT

BIT
CHAR(1) ('Y' or

'N')
CHAR(1) (T or

'F')

,

Vamos ver um exemplo de uma Tabela EMPREGADO:

create table EMPREGADO (

id INT NOT NULL autojncrement,
primeiro_nome VARCHAR(20) default NULL,
ultimo_nome VARCHAR(20) default NULL,
salario INT default NULL,

PRIMARY KEY (id)

Abaixo podemos ver o mapeamento da Classe Empregado com anotações para mapear objetos definidos na tabela EMPREGADO:
import javax.persistence.*;
@Entity

@Table(name = "EMPREGADO")
public class Empregado {

@ld @GeneratedValue
@Column(name = "id")

private int id;

@Column(name = "primeiro_nome")
private String primeiroNome;

@Column(name = "ultimo_nome")
private String ultimoNome;

@Column(name = "salario")
private int salario;

public EmpregadoO {}
public int getld() {

return id;

}

public void setld( int id ) {
this.id = id;

}

public String getPrimeiroNome() {
return primeitoNome;

}

/ 235

/

public void setPrimeiroNome( String primeiro_nome) {
this.primeiroNome= primeiro_nome;

}

public String getUlitmoNomeO {
return ultimoNome;

}

public void setUltimoNome( String ultimo_nome) {
this. ultimoNome = ultimo_nome;

}

public int getSalario() {
return salario;

}

public void setSalario( int salario) {
this.salario = salario;

}

}

Agora vamos analisar as anotações! O Hibernate detecta a anotação @ld em um campo,
assume que ele deve ser uma chave primária e deverá acessar as propriedades de um objeto diretamente através desse campo em tempo de execução. Se colocássemos essa anotação no método getld(
), permitiríamos o acesso às propriedades através de métodos getters e setters.

Da mesma forma, todas as outras anotações também são colocadas em campos ou métodos,dependendo da estratégia adotada. A anotação @Entity marca a classe como um
POJO, já a anotação @Table especifica detalhes da tabela que será persistida, isto é,seu nome será
"EMPREGADO". A anotação @GeneratedValue determina a chave primária mais apropriada em termos de portabilidade.
Galera, vamos falar agora rapidamente também sobre as associações! O termo associação é utilizado para se referir aos relacionamentos entre as entidades. Os relacionamentos1-para-1 (um-
para-um), 1-para-n (um-para-muitos) e n-para-n (muitos-para-muitos) são os mais comuns entre as entidades de um banco de dados. Bacana?
O relacionamento um-para-um (1-1) é bem simples de entender. Basta verificar a relação noivo e noiva. Ora, um noivo só possui uma noiva e uma noiva só possui um noivo. Outro exemplo: um número de identidade só se refere a uma pessoa e uma pessoa só tem um número de identidade.Tranquilo de entender, não é? A anotação utilizada para esse mapeamento é @OneToOne.

O relacionamento um-para-muitos (1-n) é bem simples de entender. Basta verificar a relação entre time de futebol e jogadores. Ora, um time de futebol tem vários jogadores, mas um jogador só joga em um time de futebol. Outro exemplo: um órgão tem vários servidores, mas um servidor
/ 235

/

pertence a um único órgão. Tranquilo de entender, não é? A anotação utilizada para esse mapeamento é @OneToMany.
O relacionamento muitos-para-muitos (n-n) é também bem fácil de entender. Basta verificar a relação entre times de futebol e campeonatos de futebol. Ora, um time de futebol joga vários campeonatos e um campeonato contém vários times de futebol. Tranquilo de entender, não é? Aanotação utilizada para esse mapeamento é @ManyToMany. Certinho?

Galera, a operação simples de acessar uma base de dados é uma operação muito custosa,
mesmo quando se trata de uma simples consulta. Aliás, uma simples consulta, por exemplo,envolve uma requisição para o servidor, o banco de dados deve compilar essa consulta, rodar e retornar um resultado que por sua vez será retornado ao cliente.
A maioria das bases de dados utilizam caches para os resultados de uma consulta, caso essas consultas são executadas inúmeras vezes. Dessa forma, elimina-se o overhear de l/O do disco e tempo de compilação da consulta. No entanto, isso terá pouco valor caso exista um grande número de clientes fazendo diferentes solicitações.
Além disso, mesmo quando temos um cache para os resultados, isso não elimina o tempo que levamos para transmitir a informação na rede, que é considerada a parte mais relevante do atraso.Algumas aplicações são capazes de tirar vantagens de aplicações contidas na própria base de dados, mas isso é uma exceção e tais bases de dados possuem suas limitações.
Em vez disso, o mais apropriado é termos uma cache no cliente final que faz a conexão com a base de dados. Isto não é provido ou suportado diretamente pela API JDBC, mas o Hibernate provê uma cache de nível um, também chamado de L1 ou simplesmente de cache, através da qual todas as requisições devem passar. Uma cache de segundo nível é opcional e configurável.
A cache de nível um (L1) garante que dentro de uma session, requisições para um dado objeto da base de dados retornará sempre a mesma instância do objeto, prevenindo assim que um mesmo objeto seja carregado múltiplas vezes pelo Hibernate ou que a informação entre em conflito. Sobre esse assunto, é isso que vocês precisam saber.
,

QUESTõES CoMENTADAS - HIBERNATE - MULTIBANCAS

1. (FCC - 2011 - TRT - 19a Região (AL) - Técnico Judiciário - Tecnologia da Informação) Linguagem de queries, fornecida pelo Hibernate, que é similar em aparência ao SQL e que, no entanto, é orientada a objeto e compreende noções como herança, polimorfismo e associação. Trata-se de:
a) HiBD-QL.

b) OOQL.

c) ORM-QL.

d) HQL.

e) JEEQL

Comentários:

Quando utilizamos o Hibernate para realizar consultas no banco de dados, temos a oportunidade de trabalhar com SQL (Structured Query Language), HQL (HibernateQuery
Language) e com Criteria Query API. Esta última fornece uma maneira elegante de construção de queries dinâmicas para consultas no banco de dados. A API é uma alternativa àsConsultas
HQL e também ao SQL tradicional.

Conforme vimos em aula, trata-se do HQL! Gabarito: D

2. (FCC - 2010 - TRT - 8a Região (PA e AP) - Analista Judiciário - Tecnologia da Informação) Os três estados de objeto definidos pelo framework Hibernate são:
a) Temporário (Temporary), Permanente (Permanent) e Resiliente (Resilient).

b) Transiente (Transient), Persistente (Persistent) e Resiliente (Resilient).

c) Temporário (Temporary), Persistente (Persistent) e Destacado (Detached).

d) Transiente (Transient), Persistente (Persistent) e Destacado (Detached).

e) Transiente (Transient), Permanente (Permanent) e Resiliente (Resilient).

Comentários:

SaJc( )

EvictC)

ClcfccC) C)

ClearCKy

Conforme vimos em aula, trata-se do Transiente, Persistente e Destacado. Gabarito: D

3. (FCC - 2012 - TRE-CE - Técnico Judiciário - Programação de Sistemas) Com relação ao framework
Hibernate é correto afirmar:

a) Permite fazer a persistência automatizada dos objetos em uma aplicação Java para as tabelas de um banco de dados relacional, utilizando metadados (descrição dos dados) que descrevem o mapeamento entre os objetos e o banco de dados.
b) É uma boa opção apenas para sistemas que fazem muito uso de stored procedures,
triggers ou que implementam a maior parte da lógica da aplicação no banco de dados vai se beneficiar mais com o uso do Hibernate.
c) Permite enviar unidirecionalmente uma representação de dados de um banco de dados relacional para um modelo de objeto utilizando um esquema baseado exclusivamente emHibernate Query Language (HQL).

d) A Java Persistence API (JPA) implementa o Hibernate, que é parte do Enterprise
JavaBeans
4.0.

e) Em uma aplicação criada com Hibernate, para cada classe de persistência é necessário criar um arquivo de mapeamento XML que deve ser salvo obrigatoriamente com o nome da classe seguido pelo sufixo .map.xml.
Comentários:

/ 235

/

O trabalho do desenvolvedor é definir como os objetos são mapeados nas tabelas do banco de dados e o Hibernate faz todo o acesso ao banco, gerando inclusive os comandos SQLnecessários - não é necessário fazer SELECT, UPDATE, INSERT, DELETE, etc! Permite fazer uma persistência automática entre classes e tabelas, propriedades e colunas,associações e chaves estrangeiras, tipos Java e tipos SQL, entre outros.
Essas ferramentas facilitam o mapeamento dos atributos de uma base de dados relacional para o modelo de objetos de uma aplicação por meio de mapeamentos, comoDescritores de
Implantação (XML) ou Anotações (Annotations) - principalmente para consultas e atualizações de dados. O desenvolvedor define como os objetos são mapeados e o framework faz o resto!
(a) Conforme vimos em aula, tudo está perfeito!

Ele continua por dizer que vale lembrar que se pode mudar a qualquer momento o SGDB
utilizado. O framework não é uma boa ferramenta para aplicações que fazem uso extensivo de stored procedures, triggers ou que implementam a maior parte da lógica da aplicação no banco de dados, contando com um modelo de objetos simples - não vai se beneficiar com o uso do Hibernate.
(b) Conforme vimos em aula, esses não irão se beneficiar!

Quando utilizamos o Hibernate para realizar consultas no banco de dados, temos a oportunidade de trabalhar com SQL (Structured Query Language), HQL (HibernateQuery
Language) e com Criteria Query API. Esta última fornece uma maneira elegante de construção de queries dinâmicas para consultas no banco de dados. A API é uma alternativa àsConsultas
HQL e também ao SQL tradicional.

(c) Conforme vimos em aula, não é exclusivamente HQL - há ainda HQL e Criteria.
Ademais, é uma relação bidirecional!
Nota de Rodapé: Hibernate tornou-se um framework tão popular que acabou por ser utilizado como referência para construção da Especificação de Persistência Java (JPA). Apesar disso, ele também é oferecido para executar a mesma função na plataforma .NET - é o famosoNHibernate.

(d) Conforme vimos em aula, Hibernate implementa JPA (e, não, o contrário)!

Em outras palavras, o primeiro arquivo trata principalmente da interação com o banco de dados. Já o segundo trata do mapeamento de classe do modelo de domínio orientado a objetos para uma base de dados relacional. É uma boa prática de programação criar um arquivo de mapeamento hbm.xml individuais para cada classe de persistência e,então,
referenciá-la e mapeá-la no cfg.xml.

/ 235

/

(e) Conforme vimos em aula, pode-se usar annotations. Ademais, o sufixo seria hbm.xml.

Gabarito: A

4. (FCC - 2010 - TRT - 22a Região (PI) - Técnico Judiciário - Tecnologia da Informação)
Hibernate é um framework:
a) que separa as funções que envolvem a construção de aplicações Web, através da associação dos eventos do lado cliente com os manipuladores dos eventos do lado do servidor.
b) pelo qual o programador utiliza a infraestrutura do servidor de aplicação voltada para o desenvolvimento de aplicações de missão crítica e de aplicações empresariais em geral.
c) no qual as questões de infraestrutura, segurança, disponibilidade e escalabilidade são responsabilidade do servidor de aplicações, permitindo que o programador se concentre,apenas, nas necessidades do negócio do cliente.

d) que permite ao desenvolvedor de páginas para internet produzir aplicações que acessem o banco de dados, manipulem arquivos no formato texto e capturem informações a partir de formulários.
e) cujo objetivo é diminuir a complexidade entre os programas Java que precisam trabalhar com um banco de dados do modelo relacional.
Comentários:

O trabalho do desenvolvedor é definir como os objetos são mapeados nas tabelas do banco de dados e o Hibernate faz todo o acesso ao banco, gerando inclusive os comandos SQLnecessários - não é necessário fazer SELECT, UPDATE, INSERT, DELETE, etc! Permite fazer uma persistência automática entre classes e tabelas, propriedades e colunas,associações e chaves estrangeiras, tipos Java e tipos SQL, entre outros.
(e) Conforme vimos em aula, seu objetivo é fazer um mapeamento para persistência automática
- reduzindo a complexidade entre programas que precisam trabalhar com o modelo relacional.
Gabarito: E

5. (FCC - 2007 - TRE-SE - Analista Judiciário - Tecnologia da Informação) Sendo um grupo de classes e componentes responsáveis pelo armazenamento e recuperação de dados, esta camada inclui necessariamente um modelo das entidades do domínio de negócios (mesmo que seja somente um modelo de metadados). No âmbito do mapeamento objeto-relacional (hibernate) esta é a camada de:
,

a) negócio.

b) restrição.

c) apresentação.

d) consistência.

e) persistência.

Comentários:

A imagem abaixo mostra de maneira absurdamente abstrata uma sugestão de arquitetura em que o Hibernate funciona como uma Camada de Persistência que conecta os objetos da aplicação a uma base de dados relacional. As classes, interfaces e outros componentes são definidos no pacote org.hibernate. Além disso, existem três arquivos de configuração:hibernate.cfg.xml, hibernate.properties e hbm.xml.

Conforme vimos em aula, a camada responsável pelo armazenamento e recuperação de dados é a Camada de Persistência. Gabarito: E
6. (FCC - 2007 - MPU - Analista de Informática - Desenvolvimento de Sistemas) Objetos que têm uma representação no banco de dados, mas não fazem mais parte de uma sessão do Hibernate,o que significa que o seu estado pode não estar mais sincronizado com o banco de dados, são do tipo:
a) transient.

b) detached.

c) attached.

d) persistent.

e) consistent.

Comentários:

Galera, um objeto de classes persistentes pode estar em um dos três diferentes estados:Transiente (Transient), Persistente (Persistent) ou Desanexado (Detached), como nós podemos ver representado na imagem acima! Bem, vamos falar agora um pouquinho sobre cada um desses estados - eu recomendo que vocês entendam bem o funcionamento:
Transiente: a instância não esteve nem está associada a um contexto persistente,
isto é, não há uma representação no banco de dados, nem um valor identificador. Ela é instanciada,utilizada,
destruída e não pode ser reconstruída de forma automática.

Persistente: a instância está atualmente associada a um contexto persistente, isto é, há uma representação no banco de dados e um valor identificador. Qualquer mudança em um objeto nesse estado é detectada e sincronizada com a base de dados.
/ 235

/

Desanexado: a instância foi associada a um contexto persistente, no entanto não está mais associada por alguma razão (Ex: Fim de sessão). Ainda existe uma referência, o objeto ainda pode ser modificado e essas modificações podem futuramente ser persistidas - trata-se de um estado intermediário.
Conforme vimos em aula, trata-se do Tipo Detached (Desanexado)l Gabarito: B

7. (FCC - 2010 - TRT - 8a Região (PA e AP) - Analista Judiciário - Tecnologia da Informação) Em sua essência, o Hibernate é um framework para:
a) mapeamento objeto-relacional (ORM).

b) desenvolvimento de aplicações de Internet rica (Rich Internet Application - RIA).

c) implementação da camada Controller do padrão MVC (Model - View - Controller).

d) construção de aplicações utilizando-se inversão de controle (loC).

e) injeção de dependência (dependency injection) em aplicativos.

Comentários:

Pois bem! Era trabalhoso transformar objetos de uma classe em registros de uma tabela e vice-versa. Logo, começaram a surgir alguns frameworks que auxiliavam essa tarefa - são as famosasFerramentas de ORM - Object-Relational Mapping (ou Mapeamento Objeto-Relacional).
As mais conhecidas eram Hibernate e TopLink - a primeira, livre, open-source, tornou-se uma referência mundial.
Conforme vimos em aula, trata-se de um framework para mapeamento objeto-relacional.

Gabarito: A

8. (FCC - 2012 - TRF - 2a REGIÃO - Técnico Judiciário - Informática) Quando se cria uma aplicação
Java utilizando um recurso de Mapeamento Objeto-Relacional como o Hibernate, o mapeamento entre classes e tabelas, propriedades e colunas, associações e chaves estrangeiras,tipos do Java e tipos do SQL, é feito através de metadados. Esses metadados normalmente podem ser colocados em arquivos XML ou diretamente nas classes, próximos da informação que eles descrevem. Quando são colocados nas classes, esses metadados são conhecidos como:
a) mappings.

b) annotations.

c) descriptions.

d) patterns.

/ 235

/

e) actions.

Comentários:

Essas ferramentas facilitam o mapeamento dos atributos de uma base de dados relacional para o modelo de objetos de uma aplicação por meio de mapeamentos, comoDescritores de
Implantação (XML) ou Anotações (Annotations) - principalmente para consultas e atualizações de dados. O desenvolvedor define como os objetos são mapeados e o framework faz o resto.
Conforme vimos em aula, trata-se de Annotations! Gabarito: B

9. (FCC - 2008 - TRF5 - Analista de Sistemas) Usando o Hibernate, as pesquisas podem ser realizadas em bancos de dados por meio de:
a) HQL, apenas.

b) Criteria Query API, apenas.

c) Criteria Query API e HQL, apenas.

d) Criteria Query API e SQL, apenas.

e) Criteria Query API, HQL e SQL.

Comentários:

Quando utilizamos o Hibernate para realizar consultas no banco de dados, temos a oportunidade de trabalhar com SQL (Structured Query Language), HQL (Hibernate QueryLanguage) e com
Criteria Query API. Esta última fornece uma maneira elegante de construção de queries dinâmicas para consultas no banco de dados. A API é uma alternativa às Consultas HQL e também ao SQLtradicional.

Conforme vimos em aula, trata-se do Criteria Query API, HQL e SQL. Gabarito: E

10. (CONSULPLAN - 2012 - TSE - Analista Judiciário - Análise de Sistemas) Por suas características,
Hibernate 3.5 constitui uma ferramenta com a finalidade de realizar o seguinte tipo de mapeamento:
a) objeto/relacional para Java.

b) gerencial/operacional para sites interativos textuais.

c) entidade/relacionamento para modelagem de dados.

d) lógico/físico para desenvolvimento por meio da prototipação.

Comentários:

Pois bem! Era trabalhoso transformar objetos de uma classe em registros de uma tabela e vice-versa. Logo, começaram a surgir alguns frameworks que auxiliavam essa tarefa - são as famosasFerramentas de ORM - Object-Relational Mapping (ou Mapeamento Objeto-Relacional).
As mais conhecidas eram Hibernate e TopLink - a primeira, livre, open-source, tornou-se uma referência mundial.
Conforme vimos em aula, trata-se de um mapeamento objeto-relacional em Java.

Gabarito: A

11.(CESPE - 2010 - TRE-BA - Analista Judiciário - Análise de Sistemas) No Hibernate,
apenas a linguagem de consulta HQL (Hibernate Query Language) pode ser utilizada. A HQL executa os pedidos SQL sobre as classes de persistência do Java em vez de tabelas no banco de dados, o que diminui a distância entre o desenvolvimento das regras de negócio e o banco de dados.
Comentários:

Quando utilizamos o Hibernate para realizar consultas no banco de dados, temos a oportunidade de trabalhar com SQL (Structured Query Language), HQL (Hibernate QueryLanguage) e com
Criteria Query API. Esta última fornece uma maneira elegante de construção de queries dinâmicas para consultas no banco de dados. A API é uma alternativa às Consultas HQL e também ao SQLtradicional.

Lembrando que o HQL é uma linguagem muito parecida com o SQL. No entanto, comparado a este último, o HQL é totalmente orientado a objetos, e compreende noções de herança,polimorfismo e associações. Dessa forma, ele se aproxima mais das regras de negócio das aplicações, visto que essas também são escritas em geral em um paradigma orientado a objetos.
Conforme vimos em aula, pode-se utilizar SQL e Criteria Query API. A segunda parte afirma que o HQL atua sobre o modelo orientado a objetos em vez do modelo relacional, logo ele diminui a distância entre o desenvolvimento de regras de negócio e o banco de dados, porque -em geral

- as regras de negócio são escritas seguindo o paradigma orientado a objetos. Gabarito: E

12.(CESPE - 2009 - SECONT-ES - Auditor do Estado - Tecnologia da Informação) O Hibernate, um framework de mapeamento objeto relacional (ORM), cria uma camada persistência na solução desenvolvida, o que permite ligar os objetos aos bancos de dados relacionais. Entre seus serviços, o Hibernate provê um meio de se controlar transações, por meio de métodos de suas interfaces session e transaction, tendo ainda suporte a herança e polimorfismo. É distribuído sob a licença LGPL, o que permite seu uso em projetos comerciais ou open source.
Comentários:

A imagem abaixo mostra de maneira absurdamente abstrata uma sugestão de arquitetura em que o Hibernate funciona como uma camada de persistência que conecta os objetos da aplicação a uma base de dados relacional. As classes, interfaces e outros componentes são definidos no pacote org.hibernate. Além disso, existem três arquivos de configuração:hibernate.cfg.xml,
hibernate.properties e hbm.xml.

Prosseguindo... há ainda uma forma de representar a arquitetura de maneira mais ampla,
conforme é apresentado na imagem acima! Observem que entre a Aplicação e o Banco de Dados,temos uma camada de persistência do Hibernate (com seus componentes - alguns opcionais) e temos uma camada de APIs (JNDI, JDBC e JTA). Vamos ver alguns desses componentes responsáveis por controlar transações:
Conforme vimos em aula, cria-se de fato uma camada de persistência, que contém componentes que controlam as transações com o banco de dados. Gabarito: C
13.(CESPE - 2010 - TCU - Auditor Federal de Controle Externo - Tecnologia da Informação - Parte
II)

Uma equipe de desenvolvimento de software recebeu a incumbência de desenvolver um sistema com as características apresentadas a seguir.
-O sistema deverá ser integrado, interoperável, portável e seguro.

-O sistema deverá apoiar tanto o processamento online, quanto o suporte a decisão e gestão de conteúdos.
-O sistema deverá ser embasado na plataforma JEE (Java enterprise edition) v.6,
envolvendo servlets, JSP (Java server pages), Ajax, JSF (Java server faces) 2.0, Hibernate 3.5,SOA e web services.
O líder da equipe iniciou, então, um extenso processo de coleta de dados com o objetivo de identificar as condições limitantes da solução a ser desenvolvida e tomar decisões arquiteturais e tecnológicas que impactarão várias características funcionais e não funcionais do sistema, ao longo de seu ciclo de vida. A partir dessa coleta, o líder deverá apresentar à equipe um conjunto de informações e de decisões.
A tecnologia Hibernate 3.5 é apropriada para o sistema a ser desenvolvido:
entre as características que a credenciam, está o fato de ela possibilitar a recuperação de objetos por meio da formulação de queries em linguagens HQL (hibernate query language) e SQL (structured query language), bem como pelo uso de APIs (application programming interfaces) de busca por critério, entre outras.
Comentários:

Quando utilizamos o Hibernate para realizar consultas no banco de dados, temos a oportunidade de trabalhar com SQL (Structured Query Language), HQL (Hibernate QueryLanguage) e com
Criteria Query API. Esta última fornece uma maneira elegante de construção de queries dinâmicas para consultas no banco de dados. A API é uma alternativa às Consultas HQL e também ao SQLtradicional.

Conforme vimos em aula, está perfeito! Vocês já notaram que isso cai bastante, né?l Gabarito: C

14. (CESPE - 2009 - CEHAP-PB - Programador de computador) No framework Hibernate, é comum que uma instância de uma classe persistente tenha três estados específicos. Assinale a opção que contém esses três estados.
a) plugged, disconnected, timewait b) connected, disconnected, detached c) transient, persistent, detached d) transient, connected, timewait
Comentários:

Conforme vimos em aula, trata-se do Transient, Persistent e Detached. Gabarito: C

15. (CESPE - 2010 - DETRAN-ES - Analista de Sistemas) O Hibernate, framework utilizado no desenvolvimento de consultas e atualização de dados em um banco relacional, foi criado para facilitar a integração entre programas em Java, funcionando também em ambientes .Net(N Hibernate).

Comentários:

/ 235

/

Nota de Rodapé: Hibernate tornou-se um framework tão popular que acabou por ser utilizado como referência para construção da Especificação de Persistência Java (JPA). Apesar disso, ele também é oferecido para executar a mesma função na plataforma .NET - é o famoso NHibernate.
Conforme vimos em aula, está perfeito (com uma ressalva)! Ele não foi criado com o intuito de facilitar a integração entre Aplicações Java - não faz sentido! Ele foi criado com o intuito de facilitar a integração entre Aplicações Java e Bancos de Dados Relacionais, fazendo o mapeamento entre ambos os paradigmas. Bacana? Gabarito: C
16. (CESPE - 2011 - Correios - Analista de Correios - Analista de Sistemas - Desenvolvimento de
Sistemas) No Hibernate, o recurso Query Cache possibilita fazer o cache de queries que são executadas várias vezes.
Comentários:

Além do oferecer Mecanismos de ORM, o framework também pode trabalhar com um sistema de cache das informações do banco de dados, aumentando ainda mais a performance das aplicações.O esquema de cache é complexo e extensível, existindo diversas implementações possíveis.
Um recurso interessante é o Query Cache, que permite fazer um cache das queries executadas diversas vezes.
Conforme vimos em aula, a questão está perfeita! Gabarito: C

17. (CESPE - 2013 - INPI - Analista de Planejamento - Desenvolvimento e Manutenção de Sistemas)
No Hibernate, caso o nome da classe seja diferente do nome da tabela mapeada, é necessário informar, na anotação @Table, o nome da tabela, por meio do atributo name.
Comentários:

ANOTAÇÃO DESCRIÇÃO

Utilizada para especificar detalhes da tabela que serão utilizados para persistir entidades na base de dados. Caso essa anotação seja omitida, não resultará em erro, porém será utilizado o nome da
@Table classe como valor default. Dessa forma, apenas definimos a anotação se quisermos sobrescrever o nome da classe. Possui os atributos: name, catalog, schema.
Conforme vimos em aula, é exatamente isso! Sobrescreve-se o nome da tabela por meio do atributo name. Gabarito: C
/ 235

/

18. (CESPE - 2013 - SERPRO - Analista - Desenvolvimento de Sistemas) Em Hibernate, a configuração de conexões de banco de dados deve ser feita somente por meio do uso de arquivo de propriedade.
Comentários:

A imagem abaixo mostra de maneira absurdamente abstrata uma sugestão de arquitetura em que o Hibernate funciona como uma camada de persistência que conecta os objetos da aplicação a uma base de dados relacional. As classes, interfaces e outros componentes são definidos no pacote org.hibernate. Além disso, existem três arquivos de configuração:hibernate.cfg.xml,
hibernate.properties e hbm.xml.

Qual a diferença entre eles, professor? O primeiro e o segundo executam a mesma função, i.e.,configurar um serviço hibernate. Se ambos estiverem configurados, o primeiro sobrescreve o segundo. Ele contém informações sobre o local em que se encontra o banco de dados;conexões,
usuário, senha, propriedades; tipo de cache utilizado; local onde se encontram os caminhos para os arquivos hbm.xml; etc:
Conforme vimos em aula, pode ser feito por meio do arquivo de propriedades(hibernate.properties) ou arquivo de configuração (hibernate.cfg.xml). Gabarito: E

19. (CESPE - 2014 - SUFRAMA - Analista de Sistemas) De acordo com o mapeamento mostrado abaixo, no Hibernate, a coluna EventoJD manterá a chave primária da tabela Eventos.
<hibernate-mappingpackage=
"org. hibernate. tutorial.domain">

<class name="Evento" table="Eventos">

<id name="id" column="Evento_ID">

<generator class="native"/>

</id>

</class>

</hibernate-mapping>

Comentários:

ANOTAÇÃO DESCRIÇÃO

@Table

Utilizada para especificar detalhes da tabela que serão utilizados para persistir entidades na base de dados. Caso essa anotação seja omitida, não resultará em erro, porém será utilizado o nome da
@ld classe como valor default. Dessa forma, apenas definimos a anotação se quisermos sobrescrever o nome da classe. Possui os atributos: name, catalog, schema.
Utilizada para especificar qual propriedade da tabela será a identificadora, isto é, será a chave primária. Pode ser um campo único ou a combinação de múltiplos campos dependendo da estrutura da tabela.
@Column

Utilizada para especificar detalhes da coluna para o qual um campo ou propriedade será mapeado. Pode-se utilizar essa anotação com os atributos: name, length, nullable e unique.
@Entity

Utilizada para marcar uma classe como uma Entidade ou POJO.
Deve conter um construtor sem argumentos que seja visível com o menor escopo de proteção.
Conforme vimos em aula, houve o mapeamento da classe Evento para a Tabela Eventos,
cujo atributo identificador "id" será a coluna "EventoJD". Gabarito: C
20. (CESPE - 2010 - TRE-BA - Programador de computador) O Hibernate, um framework para o mapeamento objeto-relacional, é escrito na linguagem Java e, por isso, somente pode ser executado no ambiente Java.
Comentários:

Nota de Rodapé: Hibernate tornou-se um framework tão popular que acabou por ser utilizado como referência para construção da Especificação de Persistência Java (JPA). Apesar disso, ele também é oferecido para executar a mesma função na plataforma .NET - é o famoso NHibernate.
Conforme vimos em aula, ele também pode ser executado em ambiente .NET. Gabarito: E

21. (CESPE - 2013 - MPOG - Técnico de Nível Superior - V - Categoria Profissional 7) Quando se desenvolve um mapeamento com Hibernate, uma classe persistente criada não precisa implementar ou herdar qualquer classe especial do framework Hibernate.
Comentários:

Nota de Rodapé: Classes Persistentes não precisam implementar interfaces ou herdar de uma classe-base especial!
Conforme vimos em aula, classes persistentes não precisam implementar interfaces ou herdar uma classe-base especial. Gabarito: C
22. (CESPE - 2013 - INPI - Analista de Planejamento - Desenvolvimento e Manutenção de Sistemas)
O objeto Session Factory do Hibernate mantém o mapeamento objeto relacional na sessão.

Comentários:

SessionFactory (org.hibernate.SessionFactory): trata-se de um objeto pesado, thread-safe e imutável de coleções de mapeamentos objeto-relacional para um único banco de dados -deve existir apenas uma instância na aplicação. É uma fábrica de sessões e é necessário umSessionFactory por banco de dados utilizando um arquivo de configuração separado -
semelhante ao EntityManagerFactory do JPA.
Conforme vimos em aula, é na sessão que se mantém o mapeamento objeto-relacional.
Gabarito:
C

23. (CESPE - 2013 - INPI - Analista de Planejamento - Desenvolvimento e Manutenção de Sistemas)
A Interface Criteria do Hibernate é utilizada para realizar consultas ao banco de dados.

Comentários:

Quando utilizamos o Hibernate para realizar consultas no banco de dados, temos a oportunidade de trabalhar com SQL (Structured Query Language), HQL (Hibernate QueryLanguage) e com
Criteria Query API. Esta última fornece uma maneira elegante de construção de queries dinâmicas para consultas no banco de dados. A API é uma alternativa às Consultas HQL e também ao SQLtradicional.

Conforme vimos em aula, Criteria Query API é - sim - utilizada para consultas em bancos de dados.
Gabarito: C

24. (CESPE - 2014 - SUFRAMA - Analista de Sistemas) Os tipos de mapeamento do Hibernate são considerados tipos de dados SQL e precisam de conversão para dados Java nas respectivas classes Java.
Comentários:

Os tipos declarados e utilizados nos arquivos de mapeamento não são tipos de dados
Java nem tipos de dados SQL - eles são denominados Tipos Hibernate e podem traduzir do Java para SQLe vice-versa. Entenderam bem? Eles podem até ter nomes parecidos, mas não são iguais(Hibernate: date; Java: Date; SQL: DATE). Vejamos a tabela abaixo:

/ 235

/

Conforme vimos em aula, os tipos de mapeamento não são tipos SQL, muito menos Java -
são
Tipos Hibernate! Gabarito: E

LISTA DE QUESTõES - HIBERNATE - MULTIBANCAS

1. (FCC - 2011 - TRT - 19a Região (AL) - Técnico Judiciário - Tecnologia da Informação) Linguagem de queries, fornecida pelo Hibernate, que é similar em aparência ao SQL e que, no entanto, é orientada a objeto e compreende noções como herança, polimorfismo e associação. Trata-se de:
a) HiBD-QL.

b) OOQL.

c) ORM-QL.

d) HQL.

e) JEEQL

2. (FCC - 2010 - TRT - 8a Região (PA e AP) - Analista Judiciário - Tecnologia da Informação) Os três estados de objeto definidos pelo framework Hibernate são:
a) Temporário (Temporary), Permanente (Permanent) e Resiliente (Resilient).

b) Transiente (Transient), Persistente (Persistent) e Resiliente (Resilient).

c) Temporário (Temporary), Persistente (Persistent) e Destacado (Detached).

d) Transiente (Transient), Persistente (Persistent) e Destacado (Detached).

e) Transiente (Transient), Permanente (Permanent) e Resiliente (Resilient).

3. (FCC - 2012 - TRE-CE - Técnico Judiciário - Programação de Sistemas) Com relação ao framework
Hibernate é correto afirmar:

a) Permite fazer a persistência automatizada dos objetos em uma aplicação Java para as tabelas de um banco de dados relacional, utilizando metadados (descrição dos dados) que descrevem o mapeamento entre os objetos e o banco de dados.
b) É uma boa opção apenas para sistemas que fazem muito uso de stored procedures,
triggers ou que implementam a maior parte da lógica da aplicação no banco de dados vai se beneficiar mais com o uso do Hibernate.
c) Permite enviar unidirecionalmente uma representação de dados de um banco de dados relacional para um modelo de objeto utilizando um esquema baseado exclusivamente emHibernate Query Language (HQL).

d) A Java Persistence API (JPA) implementa o Hibernate, que é parte do Enterprise
JavaBeans
4.0.

e) Em uma aplicação criada com Hibernate, para cada classe de persistência é necessário criar um arquivo de mapeamento XML que deve ser salvo obrigatoriamente com o nome da classe seguido pelo sufixo .map.xml.
/ 235

/

4. (FCC - 2010 - TRT - 22a Região (PI) - Técnico Judiciário - Tecnologia da Informação)
Hibernate é um framework:
a) que separa as funções que envolvem a construção de aplicações Web, através da associação dos eventos do lado cliente com os manipuladores dos eventos do lado do servidor.
b) pelo qual o programador utiliza a infraestrutura do servidor de aplicação voltada para o desenvolvimento de aplicações de missão crítica e de aplicações empresariais em geral.
c) no qual as questões de infraestrutura, segurança, disponibilidade e escalabilidade são responsabilidade do servidor de aplicações, permitindo que o programador se concentre,apenas, nas necessidades do negócio do cliente.

d) que permite ao desenvolvedor de páginas para internet produzir aplicações que acessem o banco de dados, manipulem arquivos no formato texto e capturem informações a partir de formulários.
e) cujo objetivo é diminuir a complexidade entre os programas Java que precisam trabalhar com um banco de dados do modelo relacional.
5. (FCC - 2007 - TRE-SE - Analista Judiciário - Tecnologia da Informação) Sendo um grupo de classes e componentes responsáveis pelo armazenamento e recuperação de dados, esta camada inclui necessariamente um modelo das entidades do domínio de negócios (mesmo que seja somente um modelo de metadados). No âmbito do mapeamento objeto-relacional (hibernate) esta é a camada de:
a) negócio.

b) restrição.

c) apresentação.

d) consistência.

e) persistência.

6. (FCC - 2007 - MPU - Analista de Informática - Desenvolvimento de Sistemas) Objetos que têm uma representação no banco de dados, mas não fazem mais parte de uma sessão do Hibernate,o que significa que o seu estado pode não estar mais sincronizado com o banco de dados, são do tipo:
a) transient.

b) detached.

c) attached.

d) persistent.

e) consistent.

7. (FCC - 2010 - TRT - 8a Região (PA e AP) - Analista Judiciário - Tecnologia da Informação) Em sua essência, o Hibernate é um framework para:
/ 235

/

a) mapeamento objeto-relacional (ORM).

b) desenvolvimento de aplicações de Internet rica (Rich Internet Application - RIA).

c) implementação da camada Controller do padrão MVC (Model - View - Controller).

d) construção de aplicações utilizando-se inversão de controle (loC).

e) injeção de dependência (dependency injection) em aplicativos.

8. (FCC - 2012 - TRF - 2a REGIÃO - Técnico Judiciário - Informática) Quando se cria uma aplicação
Java utilizando um recurso de Mapeamento Objeto-Relacional como o Hibernate, o mapeamento entre classes e tabelas, propriedades e colunas, associações e chaves estrangeiras,tipos do Java e tipos do SQL, é feito através de metadados. Esses metadados normalmente podem ser colocados em arquivos XML ou diretamente nas classes, próximos da informação que eles descrevem. Quando são colocados nas classes, esses metadados são conhecidos como:
a) mappings.

b) annotations.

c) descriptions.

d) patterns.

e) actions.

9. (FCC - 2008 - TRF5 - Analista de Sistemas) Usando o Hibernate, as pesquisas podem ser realizadas em bancos de dados por meio de:
a) HQL, apenas.

b) Criteria Query API, apenas.

c) Criteria Query API e HQL, apenas.

d) Criteria Query API e SQL, apenas.

e) Criteria Query API, HQL e SQL.

10. (CONSULPLAN - 2012 - TSE - Analista Judiciário - Análise de Sistemas) Por suas características,
Hibernate 3.5 constitui uma ferramenta com a finalidade de realizar o seguinte tipo de mapeamento:
a) objeto/relacional para Java.

b) gerencial/operacional para sites interativos textuais.

c) entidade/relacionamento para modelagem de dados.

d) lógico/físico para desenvolvimento por meio da prototipação.

11. (CESPE - 2010 - TRE-BA - Analista Judiciário - Análise de Sistemas) No Hibernate,
apenas a linguagem de consulta HQL (Hibernate Query Language) pode ser utilizada. A HQL executa os pedidos SQL sobre as classes de persistência do Java em vez de tabelas no banco de dados, o que diminui a distância entre o desenvolvimento das regras de negócio e o banco de dados.
/ 235

/

12. (CESPE - 2009 - SECONT-ES - Auditor do Estado - Tecnologia da Informação) O Hibernate, um framework de mapeamento objeto relacional (ORM), cria uma camada persistência na solução desenvolvida, o que permite ligar os objetos aos bancos de dados relacionais. Entre seus serviços, o Hibernate provê um meio de se controlar transações, por meio de métodos de suas interfaces session e transaction, tendo ainda suporte a herança e polimorfismo. É distribuído sob a licença LGPL, o que permite seu uso em projetos comerciais ou open source.
13. (CESPE - 2010 - TCU - Auditor Federal de Controle Externo - Tecnologia da Informação - Parte
II)

Uma equipe de desenvolvimento de software recebeu a incumbência de desenvolver um sistema com as características apresentadas a seguir.
-O sistema deverá ser integrado, interoperável, portável e seguro.

-O sistema deverá apoiar tanto o processamento online, quanto o suporte a decisão e gestão de conteúdos.
-O sistema deverá ser embasado na plataforma JEE (Java enterprise edition) v.6,
envolvendo servlets, JSP (Java server pages), Ajax, JSF (Java server faces) 2.0, Hibernate 3.5,SOA e web services.
O líder da equipe iniciou, então, um extenso processo de coleta de dados com o objetivo de identificar as condições limitantes da solução a ser desenvolvida e tomar decisões arquiteturais e tecnológicas que impactarão várias características funcionais e não funcionais do sistema, ao longo de seu ciclo de vida. A partir dessa coleta, o líder deverá apresentar à equipe um conjunto de informações e de decisões.
A tecnologia Hibernate 3.5 é apropriada para o sistema a ser desenvolvido:
entre as características que a credenciam, está o fato de ela possibilitar a recuperação de objetos por meio da formulação de queries em linguagens HQL (hibernate query language) e SQL(structured query language), bem como pelo uso de APIs (application programming interfaces)
de busca por critério, entre outras.

14. (CESPE - 2009 - CEHAP-PB - Programador de computador) No framework Hibernate, é comum que uma instância de uma classe persistente tenha três estados específicos. Assinale a opção que contém esses três estados.
a) plugged, disconnected, timewait b) connected, disconnected, detached c) transient, persistent, detached d) transient, connected, timewait
/ 235

/

15. (CESPE - 2010 - DETRAN-ES - Analista de Sistemas) O Hibernate, framework utilizado no desenvolvimento de consultas e atualização de dados em um banco relacional, foi criado para facilitar a integração entre programas em Java, funcionando também em ambientes .Net(N Hibernate).

16. (CESPE - 2011 - Correios - Analista de Correios - Analista de Sistemas - Desenvolvimento de
Sistemas) No Hibernate, o recurso Query Cache possibilita fazer o cache de queries que são executadas várias vezes.
17. (CESPE - 2013 - INPI - Analista de Planejamento - Desenvolvimento e Manutenção de Sistemas)
No Hibernate, caso o nome da classe seja diferente do nome da tabela mapeada, é necessário informar, na anotação @Table, o nome da tabela, por meio do atributo name.
18. (CESPE - 2013 - SERPRO - Analista - Desenvolvimento de Sistemas) Em Hibernate, a configuração de conexões de banco de dados deve ser feita somente por meio do uso de arquivo de propriedade.
19. (CESPE - 2014 - SUFRAMA - Analista de Sistemas) De acordo com o mapeamento mostrado abaixo, no Hibernate, a coluna EventoJD manterá a chave primária da tabela Eventos.
<hibemate-mappingpackage=

" org.hibemate.tutorial.domain" >

<class name="Evento" table="Eventos">

<id name="id" column="Evento_ID">

<generator class="native"/>

</id>

</class>

</hibernate-mapping>

20. (CESPE - 2010 - TRE-BA - Programador de computador) O Hibernate, um framework para o mapeamento objeto-relacional, é escrito na linguagem Java e, por isso, somente pode ser executado no ambiente Java.
21. (CESPE - 2013 - MPOG - Técnico de Nível Superior - V - Categoria Profissional 7) Quando se desenvolve um mapeamento com Hibernate, uma classe persistente criada não precisa implementar ou herdar qualquer classe especial do framework Hibernate.
22. (CESPE - 2013 - INPI - Analista de Planejamento - Desenvolvimento e Manutenção de Sistemas)
O objeto Session Factory do Hibernate mantém o mapeamento objeto relacional na sessão.

23. (CESPE - 2013 - INPI - Analista de Planejamento - Desenvolvimento e Manutenção de Sistemas)
A Interface Criteria do Hibernate é utilizada para realizar consultas ao banco de dados.

*

24. (CESPE - 2014 - SUFRAMA - Analista de Sistemas) Os tipos de mapeamento do Hibernate são considerados tipos de dados SQL e precisam de conversão para dados Java nas respectivas classes Java.
GABARITo

GABARITO

1. D 8. B
15. C 22. C

2. D 9. E
16. C 23. C

3. A 10. A
17. C 24. E

4. E 11. E
18. E

5. E 12. C
19. C

6. B 13. C
20. E

7. A 14. C
21. C

JDBC

De acordo com a documentação oficial: trata-se de uma API que fornece acesso universal a dados a partir da linguagem de programação Java. É possível acessar praticamente qualquer fonte de dados, desde bancos de dados relacionais a planilhas ou arquivos simples. OJDBC também fornece uma base comum sobre a quais ferramentas e interfaces alternativas podem ser construídas.
Ele estabelece conexões com um banco de dados, envia comandos SQL e processa os resultados.Aliás, com a utilização de JDBC, torna-se fácil enviar um comando SQL para diferentes bancos de dados relacionais. Em outras palavras, não é necessário escrever um programa para acessar um banco de dados Oracle, outro para acessar um banco de dados SQL Server, e assim por diante.
Essa tecnologia permite invocar comandos SQL a partir de métodos em classes Java. Ela fornece uma API do tipo call-level para acesso a bancos de dados baseado em SQL. Os componentes dessa API estão localizados nos pacotes java.sql e javax.sql. Para conseguir acesso a diversos bancos de dados diferentes de maneira uniforme e padronizada, utilizam-se Drivers.
Como assim, professor? O Driver faz a interface entre a Aplicação Web e o SGBD! Para eu me conectar a um banco de dados individual, eu preciso ter os drivers para aquele banco de dados específico. O JDBC permite a conexão com praticamente qualquer SGBD (Oracle,DB2, SQL
Server, MySQL, PostgreSQL, etc). Existem, atualmente, quatro tipos de Drivers:

JDBC-ODBC Bridge: É o tipo mais simples. Utiliza ODBC para conectar-se com o banco de dados, convertendo métodos JDBC em chamadas às funções do ODBC. Esta ponte é normalmente usada quando não há um driver puro-Java para determinado banco de dados,pois seu uso é desencorajado devido à dependência de plataforma.

Native API: converte chamadas JDBC na API do cliente em chamadas para o SGBD
Oracle,
Sybase, Informix, etc. São escritos parcialmente em Java e parcialmente em código nativo.Requer que algum código binário específico do SO seja carregado em cada máquina cliente e usa uma biblioteca nativa específica no cliente para a fonte de dados para que eles se conectem.
Network Protocol: traduz chamadas JDBC em um protocolo de rede independente do
SGBD,
que é então convertido para um protocolo específico do SGBD por um middleware. Em geral,esta é a alternativa JDBC mais flexível de todas, em que fornecedores disponibilizam produtos adequados para uso na internet.
Database Protocol: permite chamada direta da máquina do cliente para o Servidor
SGBD.
Converte as chamadas JDBC diretamente no protocolo do banco de dados. Implementado em
Java, normalmente é independente de plataforma e escrito pelos próprios desenvolvedores.
É
o tipo mais recomendado para ser usado.

/ 235

/

Open Database Connectivity (ODBC) é um padrão aberto desenvolvido para que linguagens de programação ou sistemas operacionais se comuniquem com bancos de dados de maneira independente de plataforma. O JDBC utiliza um driver específico para banco de dados; oODBC
utiliza sempre o mesmo Driver e depois configuram-se as propriedades do sistema para acessar determinado banco.
Dado que foi utilizado o driver adequado para acesso ao banco de dados, pode-se utilizar a classeConnection para estabelecer a conexão, de fato, com o banco. Essa classe se encontra no pacote java.sql - que contém uma biblioteca para acesso e processamento de dados em uma fonte de dados. As classes, métodos e interfaces dele mais importantes são:
Driver: interface pública abstrata que todo driver deve implementar para executar instruções SQL.
DriverManager: classe que contém o registro de cada driver, oferecendo métodos estáticos para gerenciá-los.
Connection: interface que representa uma conexão com o banco de dados - possui diversos métodos importantes.
Statement: interface pública abstrata que é utilizada para executar instruções SQL estáticas e obter os resultados de sua execução.
ResuItSet: essa interface é uma tabela de dados que representa o resultado de uma instrução SQL em um banco de dados.
PreparedStatement: interface pública abstrata utilizada para estender a interface Statement e criar um objeto que represente uma instrução SQL.
CalIableStatement: interface que permite executar funções ou procedimentos armazenados no banco.
try

{

Class.forName("sun.jdbc.odbc.JdbcOdbcDriver").getlnstance();

Connection con =

DriverManager. getConnection("jdbc:odbc:meusCdsDb"," conta", "sen ha");

}

catch(SQLException e)

2-22

/ 235

/

{ // Se o carregador não localizar o driver do banco para conexão, lança a

// exceção java.lang.ClassNotFoundExeption e.printStackTrace();
}

Para acessar um banco de dados, o primeiro passo é estabelecer uma conexão! É
possível fazer isso em duas etapas: primeiro, carrega-se o driver do banco de dados. Uma vez carregado, o driver se registra para o DriverManager e está disponível para a aplicação. Então usa-se oDriverManager para abrir uma conexão com o banco de dados. A interface Connection designa um objeto con para receber a conexão.
Statement stm = con.createStatementO;

String SQL = "Select colunai, coluna2, coluna3 from TabelaX";

Estabelecida a conexão, podemos executar comandos SQL no banco de dados. Para realizar uma operação, podemos usar três interfaces. A primeira delas é a interface Statement, que permite a execução dos comandos fundamentais de SQL (SELECT, INSERT, UPDATE ou DELETE). Ainterface
PreparedStatement nos permite usufruir de SQL armazenado ou pré-compilado no banco.

ResuItSet rs = stm.executeQuery(SQL);

A terceira interface é CalIableStatement, e permite executar procedimentos e funções armazenados no banco (quando o banco suportar este recurso). A interfaceResuItSet permite colher os resultados da execução de nossa query no banco de dados. Esta interface apresenta uma série de métodos para prover o acesso aos dados. Depois é só encerrar o acesso,liberando recursos.
final ly

{

try

{

con.closeO;

}

catch(SQLException onConClose)

/ 235

/

{

System.out.println("ERRO NO FECHAMENTO DA CONEXÃO");
onConClose.printStackT race();

}

}

Podemos fazer isso fechando o Statement, que libera os recursos associados à execução desta consulta, mas deixa a conexão aberta para a execução de uma próxima consulta; ou fechando diretamente a conexão, que encerra a comunicação com o banco de dados. Para termos certeza de que vamos encerrar esta conexão mesmo que uma exceção ocorra, reservamos o fechamento para a cláusula finally().
,

QUESTõES CoMENTADAS - JDBC - MULTIBANCAS

1. (FCC - 2006 - BACEN - Analista de Sistemas) O estabelecimento de conexão entre um aplicativo
Java e um banco de dados, para processar instruções SQL de consulta e atualização, é possibilitado por meio do padrão aberto, desenvolvido pela Microsoft, denominado:
a) API.

b) ODBC.

c) SGDB.

d) JDBC.

e) OLE.

Comentários:

Open Database Connectivity (ODBC) é um padrão aberto desenvolvido para que linguagens de programação ou sistemas operacionais se comuniquem com bancos de dados de maneira independente de plataforma. O JDBC utiliza um driver específico para banco de dados; oODBC
utiliza sempre o mesmo Driver e depois configuram-se as propriedades do sistema para acessar determinado banco.
Conforme vimos em aula, trata-se do ODBC. Gabarito: B

2. (CESPE - 2008 - IPEA - Analista de Sistemas) O JDBC é usado, entre outras coisas, para acesso a bancos de dados sem SQL, por meio de Java.
Comentários:

De acordo com a documentação oficial: trata-se de uma API que fornece acesso universal a dados a partir da linguagem de programação Java. É possível acessar praticamente qualquer fonte de dados, desde bancos de dados relacionais a planilhas ou arquivos simples. OJDBC também fornece uma base comum sobre a quais ferramentas e interfaces alternativas podem ser construídas.
Conforme vimos em aula, ele pode acessar praticamente qualquer coisa. Gabarito: C

3. (FCC - 2008 - TRT - 2a REGIÃO (SP) - Analista Judiciário - Tecnologia da Informação) A
utilização de JDBC, em um programa Java, inicia com a indicação do pacote que contém a JDBC API pela declaração:
a) import java.awt.*;

b) import java.util.*;

,

c) import java.sql.*;

d) import java.swing.*;

e) import java.jdbc.*;

Comentários:

Essa tecnologia permite invocar comandos SQL a partir de métodos em classes Java. Ela fornece uma API do tipo call-level para acesso a bancos de dados baseado em SQL. Os componentes dessa API estão localizados no pacote java.sql e javax.sql. Para conseguir acesso a diversos bancos de dados diferentes de maneira uniforme padronizada, utilizam-se Drivers.
Conforme vimos em aula, trata-se do java.sql. Gabarito: C

4. (ESAF - 2009 - ANA - Analista Administrativo - Tecnologia da Informação - Desenvolvimento) Em uma aplicação Java, se o carregador de classes não conseguir localizar a classe do driver de banco de dados para uma conexão JDBC, é lançada a exceção a) java.lang.ClassNotFoundException.
b) java.io.FileNotFoundException.

c) java.lang.SecurityException.

d) java.io.lOException.

e) java.util.lnputMismatchException.

Comentários:

try

{

Class.forName("sun.jdbc.odbc.JdbcOdbcDriver").getlnstance();

Connection con =
DriverManager.getConnection("jdbc:odbc:meusCdsDb"," conta", "sen ha");

}

catch(SQLException e)

{ // Se o carregador não localizar o driver do banco para conexão, lança a

// exceção java.lang.ClassNotFoundExeption e.printStackTrace();
/ 235

/

Conforme vimos em aula, trata-se do java.lang.ClassNotFoundException. Gabarito: A

5. (FGV - 2009 - MEC - Analista de Sistemas - Especialista) Observe o código abaixo, que se refere á implementação de Java no acesso a Banco de Dados em JDBC.
package wlss.jdbcTT;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

class TI {

public static void main(String args[])
Connection con = null;

try {

Class.forName("sun.jdbc.odbc.JdbcOdbcDriver").getInstance(

) ;

con =
DriverManager.getConnection("jdbc:odbc:meusCdsDb",

" conta ", " senha ");
Statement stm = con.createStatement();
String SQL = " Select titulo, autor,

total_faixas from MeusCDs ";

ResultSet rs = stm.executeQuery(SQL);
while (rs . next () ) {

String tit = rs.getString("titulo");
String aut = rs.getString("autor");

int totalFaixas = rs.getlnt("total_faixas");
System.out.println(48 + " Titulo: " + tit + "

Autor: " + aut

}

+ " 49: Tot. Faixas: " + totalFaixas);

} catch (SQLException e) {

} finally {
try {

con.close();

} catch (SQLException onConClose) {
System.out.println(" Houve erro no fechamento da conexão ");
)

}

}

onConClose.printStackTrace();

Analise a instrução a seguir: con = DriverManager.getConnection("jdbc:odbc:meusCdsDb", "
conta ", " senha "); Assinale a alternativa que indique corretamente o significado da instrução acima.
a) Abrir as tabelas do Banco de Dados.

b) Fechar a conexão com o Banco de Dados.

c) Liberar a conexão com o Banco de Dados.

d) Estabelecer a conexão com o Banco de Dados.

e) Criar uma variável para logon do Banco de Dados.

Comentários:

Para acessar um banco de dados, o primeiro passo é estabelecer uma conexão! É
possível fazer isso em duas etapas: primeiro, carrega-se o driver do banco de dados. Uma vez carregado, o driver se registra para o DriverManager e está disponível para a aplicação. Então usa-se oDriverManager para abrir uma conexão com o banco de dados. A interface Connection designa um objeto con para receber a conexão.
Conforme vimos em aula, trata-se do estabelecimento de uma conexão. Gabarito: D

6. (FCC - 2012 - MPE-AP - Técnico Ministerial - Informática) Analise as linhas a seguir presentes em um programa Java que não apresenta erros.
a = DriverManager.getConnection("jdbc:odbc:Driver={Microsoft Access
Driver
(*.mdb)};DBQ=E:\\bd.mdb",

b = a.createStatement();

c = b.executeQueryfselect * from cliente where id = "+ valor +"");

Considere que os objetos a, b e c são de interfaces contidas no pacote java.sql. Pode-se concluir que esses objetos são, respectivamente, das interfaces a) Connection, SessionStatement e Result.
b) DriverManager, PreparedStatement e RecordSet.

c) ConnectionStatement, PreparedStatement e RecordSet.

d) Connection, Statement e ResuItSet.

e) DaoConnection, Statement e ResuItSet.

Comentários:

Conforme vimos em aula: a = Connection; b = Statement; c = ResuItSet. Gabarito: D

7. (CESPE - 2012 - TJ-RO - Analista Judiciário - Análise de Sistemas - Desenvolvimento - B) JDBC,
uma biblioteca vinculada a API da arquitetura JEE, define como um cliente pode acessar bancos de dados OO exclusivamente.
Comentários:

De acordo com a documentação oficial: trata-se de uma API que fornece acesso universal a dados a partir da linguagem de programação Java. É possível acessar praticamente qualquer fonte de dados, desde bancos de dados relacionais a planilhas ou arquivos simples. OJDBC também fornece uma base comum sobre a quais ferramentas e interfaces alternativas podem ser construídas.
Conforme vimos em aula, ele pode acessar bancos de dados de quaisquer paradigmas (OO,Relacional, etc). Gabarito: E

8. (COPEVE-UFAL - 2012 - ALGÁS - Analista de Tecnologia da Informação - I) Na arquitetura do
JDBC, a diferença entre os tipos Statement e PreparedStatement é o fato do PreparedStatement manter os dados criptografados durante o tráfego entre o cliente e o servidor do SGBD.
Comentários:

Não existe isso! De fato, o PreparedStatement é mais seguro, visto que ajuda a impedir SQLInjection. No entanto, ele não mantém dados criptografados. Gabarito: E

9. (FGV - 2009 - MEC - Administrador de Banco de Dados) O pacote "java.sql" da API Java consiste de um conjunto de classes e interfaces que permitem embutir código SQL em métodos Java para por meio de drivers JDBC acessar diversos SGBDs. As alternativas a seguir apresentam interfaces do pacote "java.sql", à exceção de uma. Assinale-a.
a) SQLData b) ResuItSet c) Statement d) DriverManager e) Connection
Comentários:

Pegadinha de banca que não sabe avaliar conhecimento! DriverManager não é uma interface, é uma classe! Gabarito: D
10. (CESPE - 2008 - HEMOBRÁS - Analista de Gestão Corporativa - Administrador de
Banco de
Dados) O JDBC fornece a classe CalIableStatementSQL, que permite que procedimentos ou funções SQL armazenados sejam chamados.
Comentários:

A terceira interface é CalIableStatement, e permite executar procedimentos e funções armazenados no banco (quando o banco suportar este recurso). A interfaceResuItSet permite

/ 235

/

colher os resultados da execução de nossa query no banco de dados. Esta interface apresenta uma série de métodos para prover o acesso aos dados. Depois é só encerrar o acesso,liberando recursos.
Conforme vimos em aula, o nome correto é CalIableStatement. Gabarito: E

LISTA DE QUESTõES - JDBC - MULTIBANCAS

1. (FCC - 2006 - BACEN - Analista de Sistemas) O estabelecimento de conexão entre um aplicativo
Java e um banco de dados, para processar instruções SQL de consulta e atualização, é possibilitado por meio do padrão aberto, desenvolvido pela Microsoft, denominado:
a) API.

b) ODBC.

c) SGDB.

d) JDBC.

e) OLE.

2. (CESPE - 2008 - IPEA - Analista de Sistemas) O JDBC é usado, entre outras coisas, para acesso a bancos de dados sem SQL, por meio de Java.
3. (FCC - 2008 - TRT - 2a REGIÃO (SP) - Analista Judiciário - Tecnologia da Informação) A
utilização de JDBC, em um programa Java, inicia com a indicação do pacote que contém a JDBC API pela declaração:
a) import java.awt.*;

b) import java.util.*;

c) import java.sql.*;

d) import java.swing.*;

e) import java.jdbc.*;

4. (ESAF - 2009 - ANA - Analista Administrativo - Tecnologia da Informação - Desenvolvimento) Em uma aplicação Java, se o carregador de classes não conseguir localizar a classe do driver de banco de dados para uma conexão JDBC, é lançada a exceção a) java.lang.ClassNotFoundException.
b) java.io.FileNotFoundException.

c) java.lang.SecurityException.

d) java.io.lOException.

e) java.util.lnputMismatchException.

,

5. (FGV - 2009 - MEC - Analista de Sistemas - Especialista) Observe o código abaixo, que se refere á implementação de Java no acesso a Banco de Dados em JDBC.
package wlss.jdbcTT;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

class TI {

public static void main(String args[])
Connection con = null;

try {

Class.forName("sun.jdbc.odbc.JdbcOdbcDriver").getInstance(

) ;

con =
DriverManager.getConnection("jdbc:odbc:meusCdsDb",

" conta ", " senha ");
Statement stm = con.createStatement();
String SQL = " Select titulo, autor,

total_faixas from MeusCDs ";

ResultSet rs = stm.executeQuery(SQL);
while (rs . next () ) {

String tit = rs.getString("titulo");
String aut = rs.getString("autor");

int totalFaixas = rs.getlnt("total_faixas");
System.out.println(48 + " Titulo: " + tit + "

Autor: " + aut

}

+ " 49: Tot. Faixas: " + totalFaixas);

} catch (SQLException e) {

} finally {
try {

con.close();

} catch (SQLException onConClose) {
System.out.println(" Houve erro no fechamento da conexão ");
}

}

}

onConClose.printStackTrace();

Analise a instrução a seguir: con = DriverManager.getConnection("jdbc:odbc:meusCdsDb", "
conta ", " senha "); Assinale a alternativa que indique corretamente o significado da instrução acima.
a) Abrir as tabelas do Banco de Dados.

b) Fechar a conexão com o Banco de Dados.

c) Liberar a conexão com o Banco de Dados.

d) Estabelecer a conexão com o Banco de Dados.

e) Criar uma variável para logon do Banco de Dados.

6. (FCC - 2012 - MPE-AP - Técnico Ministerial - Informática) Analise as linhas a seguir presentes em um programa Java que não apresenta erros.
a = DriverManager.getConnection("jdbc:odbc:Driver={Microsoft Access
Driver
(*.mdb)};DBQ=E:\\bd.mdb", ""l b = a.createStatement();
c = b.executeQuery("select * from cliente where id = "+ valor +"");

Considere que os objetos a, b e c são de interfaces contidas no pacote java.sql. Pode-se concluir que esses objetos são, respectivamente, das interfaces a) Connection, SessionStatement e Result.
b) DriverManager, PreparedStatement e RecordSet.

c) ConnectionStatement, PreparedStatement e RecordSet.

d) Connection, Statement e ResuItSet.

e) DaoConnection, Statement e ResuItSet.

7. (CESPE - 2012 - TJ-RO - Analista Judiciário - Análise de Sistemas - Desenvolvimento - B) JDBC,
uma biblioteca vinculada a API da arquitetura JEE, define como um cliente pode acessar bancos de dados OO exclusivamente.
8. (COPEVE-UFAL - 2012 - ALGÁS - Analista de Tecnologia da Informação - I) Na arquitetura do
JDBC, a diferença entre os tipos Statement e PreparedStatement é o fato do PreparedStatement manter os dados criptografados durante o tráfego entre o cliente e o servidor do SGBD.
9. (FGV - 2009 - MEC - Administrador de Banco de Dados) O pacote "java.sql" da API Java consiste de um conjunto de classes e interfaces que permitem embutir código SQL em métodos Java para por meio de drivers JDBC acessar diversos SGBDs. As alternativas a seguir apresentam interfaces do pacote "java.sql", à exceção de uma. Assinale-a.
a) SQLData b) ResuItSet c) Statement d) DriverManager e) Connection
10. (CESPE - 2008 - HEMOBRÁS - Analista de Gestão Corporativa - Administrador de
Banco de
Dados) O JDBC fornece a classe CalIableStatementSQL, que permite que procedimentos ou funções SQL armazenados sejam chamados.
,

GABARITo

GABARITO

1. B

2. C

3. C

4. A

5. D

6. D

7. E

8. E

9. D

10. E

,

