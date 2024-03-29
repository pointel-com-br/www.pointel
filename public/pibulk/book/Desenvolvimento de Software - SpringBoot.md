# Desenvolvimento de Software - SpringBoot

Índice

1) Java EE - Spring Framework - Teoria

2) Java EE - Spring Framework - Questões Comentadas.

3) Java EE - Spring Framework - Lista de Questões.

x

/

SPRING FRAMEWORK

O spring by Pi votai
Spring é um framework open-source de desenvolvimento para Plataforma Java! Trata-se de uma tecnologia não-intrusiva (aplicação não depende do framework em si) cujo intuito é desenvolver aplicações mais fáceis de usar e promover (e, não, impor) boas práticas por meio de um modelo de programação baseada em POJO. Ele veio como alternativa ao modelo baseado em EJB! Equais são seus benefícios?

BENEFÍCIOS DESCRIÇÃO

Leveza
(Lightweight)

Trata-se de um framework leve, quando se trata de tamanho e transparência. A versão básica tem cerca de 2MB.
Não-lntrusivo

Trata-se de um framework em que o código da lógica de aplicação não depende do em si do Framework Spring. Se algum dia eu quiser modificar o framework, o código estará preparado.
Inversão de
Controle (IOC)

Trata-se de um framework que promove baixo acoplamento por meio do padrão arquitetural de Inversão de Controle. Os objetos oferecem suas dependências em vez de criarem ou procurarem objetos dependentes.
Orientada a
Aspectos

Trata-se de um framework orientado a aspectos que separa a lógica de negócio da aplicação dos serviços de suporte do sistema.
Container

Trata-se de um framework que gerencia o ciclo de vida e configuração de objetos da aplicação por meio de um container.
MVC

Trata-se de um framework desenhado para o Padrão MVC, que oferece diversas alternativas a frameworks web - permite construir aplicações robustas e manuteníveis.
Gerenciamento de Transação
Trata-se de um framework que provê uma interface consistente de gerenciamento de transações que pode variar de uma transação global a uma transação local.
Tratamento de Exceções
Trata-se de um framework capaz de traduzir exceções de uma tecnologia específica em outros tipos de exceções hierarquicamente.
Spring
Security

Trata-se de um framework que fornece um mecanismo de segurança declarativo, que é um aspecto crítico de diversas aplicações.
Spring
Boot

Spring Data
JPA

Spring Data
Envers

Trata-se de uma forma de configurar e publicar aplicações. A
intenção é ter o seu projeto rodando o mais rápido possível e sem complicação. Basta informar suas convenções (módulos)que ele reconhecerá e configurará. Ex: Web, Template,
Persistência, Segurança, etc.

Trata-se de um framework para facilitar a criação de repositórios, liberando o desenvolvedor de implementar interfaces referentes aos repositórios (ou DAOs), e também deixando pré-implementado algumas funcionalidades (Ex:ordenação das consultas; paginação de registros).

Trata-se de um framework que estende o JPA ao adicionar uma camada extra de abstração sobre o JPA. Essa camada permite criar repositórios JPA ao estender interfaces de repositório doSpring JPA. Auxilia bastante a criação de funções de auditoria.

Vamos a algumas explicações mais detalhadas sobre algumas características citadas acima -comecemos com a Inversão de Controle! Imaginem que vocês implementam uma classe de usuário, e dentro dessa classe vocês precisam utilizar a classe de e-mail. O que vocês fazem?Instanciam a classe de e-mail dentro da classe de usuário. O que isso gera?
Acoplamento (i.e.,
dependência entre as partes).

Agora a classe de usuário depende da classe de e-mail. Um dos problemas que a inversão de controle veio resolver é o de módulos de mais alto nível (Ex: Classe de Usuário)dependendo de módulos de mais baixo nível (Ex: Classe de E-mail). O que é mais importante: usuário ou e-mail?Ora, usuário - o e-mail, em geral, é apenas um acessório do usuário! Vamos ver um exemplo mais claro:
Deem uma olhada na casa de vocês e contem quantos dispositivos têm baterias que precisam ser recarregadas de alguma maneira: câmera fotográfica, celular, fone de ouvido sem-fio,controle de videogame, ipod, máquina de barbear, etc. Ora, esses dispositivos não têm uma interface de
/ 15

/

recarga de bateria comum, i.e., um usa micro-usb, o outro mini-usb, outro usb, a apple sempre inventa algo diferente, enfim...
Qual o resultado disso? Você não possui um único carregador para recarregar todos os seus dispositivos - você é obrigado a ter um carregador para cada um deles! E se você mudar de celular? Lá se vai mais um carregador. Se você der um upgrade no ipod? Outro carregador! O que acontece no final? Aposto que vocês (como bons nerds) possuem uma gaveta lotada de carregadores diferentes! ®
Eu sei que vocês entenderam a história, mas eu gostaria que vocês internalizassem a ideia principal! Em vez de os carregadores dependerem dos dispositivos, os dispositivos estão dependendo dos carregadores. Isso não soa absurdo? É o mais importante dependendo do menos importante; é o essencial dependendo do acessório; é o "poste mijando no cachorro".
Bem, um dos princípios do Spring Framework é a Inversão de Controle (ou
Inversão de
Dependência). É uma forma de subverter essa lógica! Vamos fazer classes de baixo nível dependerem de classes de alto nível. Vamos programar para interfaces e, não, para implementações. Como podemos fazer isso, professor? Por meio da Injeção deDependências
(não confundam, são conceitos independentes!).

Professor, o que seria a injeção de dependências? Trata-se de um padrão de desenvolvimento de software utilizado para inverter controles e manter o baixo acoplamento entre os módulos de um sistema. Ela visa remover dependências desnecessárias entre as classes ou torná-las mais suaves, e ajuda a ter um design de software que seja mais fácil de manter e de evoluir.
Lembram-se do exemplo anterior? Para eu utilizar uma classe de e-mail na classe de usuário, eu teria que instanciar a classe de e-mail dentro da classe de usuário. Ora, isso já acoplaria as classes,fazendo com que a classe de usuário dependesse da classe de e-mail, ou seja, a classe de alto nível estaria dependendo da classe de baixo nível. Vamos resolver esse problema com aInjeção de Dependência!
, 15

Grosso modo, injetar dependências nada mais é que passar uma classe (que será utilizada) para outra classe (que irá consumi-la). Ora, realmente a classe de usuário precisa da classe de e-mail,mas é possível utilizá-la sem acoplá-las. Como? Delegando a responsabilidade de criação do objeto da classe e-mail a outra parte do sistema. Quem pode fazer isso? O Container!
Ele é responsável por criar, gerenciar, conectar e configurar objetos e seus ciclos de vida. O padrão de Injeção de Dependência é baseado no padrão Builder, que é aquele cara responsável por construir objetos e armazená-los. Ele permite a separação da construção de um objeto complexo da sua representação, de forma que o mesmo processo de construção possa criar diferentes representações.
O que acontece? Passa-se a responsabilidade de criar um objeto para o container (que funciona como o builder), indicando qual interface desejamos que seja implementada. Ele criará a o objeto que implementa a interface e injeta essa dependência em outra classe. Em nosso caso,ele criará o objeto de e-mail e injetará no objeto de pessoa.
O container é capaz de resolver dependências complexas transparentemente, i.e., eu não estou nem ligando para como ele vai resolver. O container é simplesmente um mapeador de dependências que as suas classes necessitam com a lógica de criação dessas dependências(por meio de XML/Annotation). Ele trata todos os objetos sob seu gerenciamento como beans.
Podemos afirmar, então, que a injeção de dependência desacopla a construção das suas classes da construção de suas dependências. Professor, deu nó na cabaça! A frase apenas afirma que a responsabilidade para a criação da classe E-mail não é mais da classe Usuário, é do container.Bacana? Dessa forma, quebramos o acoplamento e invertemos o controle.

Em vez de depender de uma classe concreta, passamos a depender de uma abstração. O
código estará mais desacoplado, modular, flexível - sendo mais fácil a manutenção e a evolução. Épossível injetar dependências de três formas: Injeção por Construtor; Injeção por Propriedade(Setter); e Injeção por Interface - esse último é injeção de dependência sem inversão de controle.

Continuando nosso papo: Spring faz praticamente tudo que EJB faz (e mais uma pancada de coisas). Ele pode ser utilizado por qualquer Aplicação Java, mas possui diversas extensões específicas para Java EE! Ele é composto por diversos módulos, todos construídos sobre o CoreContainer. Ele é livre para escolher quais características ele necessita e eliminar módulos que ele não deseja utilizar.
A imagem abaixo apresenta os containers. Nós não vamos ver todos eles, vamos passar pelos mais importantes - começando pelo mais importante de todos: Core! O Container Core é o responsável por fornecer Inversão de Controle e Injeção de Dependência. O Módulo Beans é o responsável pelo BeanFactory, que é uma implementação do padrão Factory1. O que esse padrão faz?
Ele cria beans por meio de configurações XML - tudo isso por meio da interface:org.springframework.beans.factory.BeanFactory. O Módulo AOP fornece uma implementação

1 Atualmente, recomenda-se utilizar ApplicationContext
(org.springframework.context.ApplicationContext) em vez de
BeanFactory, porque ele fornece mais funcionalidades. Enquanto o primeiro permite a instanciação e conexão (wire) de beans, o segundo permite também il8n, publicação de eventos, automatizações, etc.
7 15

/

orientada a objetos que permite definir, por exemplo, interceptadores.
Já o Módulo DAO
fornece uma camada de abstração para JDBC, eliminando grande parte da codificação necessária para interagir com um banco de dados.
O Módulo ORM fornece camadas de integração para mapeamento objeto-relacional com tecnologias como JPA, Hibernate, etc. O Módulo JMS fornece a possibilidade de produzir e consumir mensagens, com integração nativa com JMS. Galera, vamos falar um pouco agora sobreSpring Security! Trata-se de um framework que fornece diversos serviços de segurança aAplicações Java EE.

Ele faz isso de maneira amigável e flexível para o desenvolvedor, aderindo às práticas bem estabelecidas e introduzidas pelo Spring Framework. Ele tenta endereçar todas as camadas de segurança dentro da aplicação. Além disso, vem com um conjunto de opções de configuração que o torna bastante poderoso. Sua principal função é fornecer autenticação e autorização sobre o Spring Framework.
ví**-

l^ESCLARECENDO!

Apenas para lembrar esses conceitos, a autenticação é o processo de estabelecer se alguém é quem afirma ser, e a autorização é o processo de decidir se alguém pode ou não realizar alguma ação em uma aplicação. Ele pode ser utilizado em conjunto com aplicações web ou standalone.Além disso, é capaz de proteger de ataques como: session fixation, clickjacking, cross site request forgery, etc.
Ele é capaz de lidar com diversos modelos de autenticação - e isso é muito atrativo para desenvolvedores. Pode fornecer segurança em nível de visões, métodos, serviços, URL,domínios,
etc. Antes que eu me esqueça, ele é open-source - claro, é parte dos Projetos
Spring, junto com
Spring Batch, Spring Integration, Spring Web Services, Spring Social, Spring Web Flow e
Spring
Data.

As configurações de segurança são realizadas no arquivo appIicationContext-security.xml no diretório WEB-INF. Para que qualquer página ou diretório sejam seguros, é necessário adicionar a esse arquivo o elemento <intercept-url>. Como, professor? Mais ou menos assim:<intercept-url pattern="/something" access="hasRole('ROLE_USER')"/>. É isso, galera! Acredito que isso seja suficiente...
/ 15

/

QUESTõES CoMENTADAS - SPRING - MULTIBANCAS

1. (CESPE - 2012 - PEFO/CE - Analista de Sistemas) No Spring, as configurações de segurança são realizadas no arquivo appIicationContext-security.xml, e, para que qualquer página ou diretório seja seguro, é necessário adicionar a esse arquivo o elemento <intercept-url>.
Comentários:

As configurações de segurança são realizadas no arquivo appIicationContext-security.xml no diretório WEB-INF. Para que qualquer página ou diretório sejam seguros, é necessário adicionar a esse arquivo o elemento <intercept-url>. Como, professor? Mais ou menos assim:<intercept-url pattern="/something" access="hasRole('ROLE_USER')"/>. É isso, galera! Acredito que isso seja suficiente...
Conforme vimos em aula, a questão está perfeita!

Gabarito: C

2. (FCC - 2010 - TRT/8 - Analista de Sistemas) Interface que representa o container loC(Inversão de Controle) do framework Spring:

a) org.springframework.pojo.factory.PojoFactory.

b) org.springframework.ioc.factory.lOCFactory.

c) org.springframework.beans.factory.BeanFactory.

d) org.springframework.mvc.factory.MVCContainer.

e) org.springframework.beans.factory.CoreContainer.

Comentários:

Ele cria beans por meio de configurações XML - tudo isso por meio da interface:org.springframework.beans.factory.BeanFactory. O Módulo AOP fornece uma implementação orientada a objetos que permite definir, por exemplo, interceptadores. Já o Módulo DAOfornece uma camada de abstração para JDBC, eliminando grande parte da codificação necessária para interagir com um banco de dados.
/ 15

/

Sabe aquela imagem aula de Spring? Ela é um pouco confusa em termos de nomenclatura porque,dentro do Core Container, nós temos o Módulo Core (além do Módulo Beans, Módulo
Context e
Módulo SpEL). Os módulos Core e Beans são responsáveis tanto pela loC quanto pela Dl.

Dentro deles, nós temos um pacote chamado org.springframework.beans, que contém interfaces e classes para manipulação de JavaBeans. Uma de suas interfaces é chamada BeanFactory,que é responsável por fornecer um mecanismo de configuração avançado e capaz de gerenciar qualquer tipo de objeto. Logo, resposta: C.
Gabarito: C

3. (FCC - 2011 - TRT/23 - Analista de Sistemas) Na estrutura do Spring o módulo que provê uma camada de abstração para JDBC, eliminando grande parte da codificação necessária para interagir com um banco de dados é o:
a) Spring Core b) Spring ORM
c) Spring Context d) Spring DAO
e) Spring AOP

Comentários:

Ele cria beans por meio de configurações XML - tudo isso por meio da interface:org.springframework.beans.factory.BeanFactory. O Módulo AOP fornece uma implementação orientada a objetos que permite definir, por exemplo, interceptadores. Já o Módulo DAOfornece uma camada de abstração para JDBC, eliminando grande parte da codificação necessária para interagir com um banco de dados.
Conforme vimos em aula, trata-se do Módulo Spring DAO.

Gabarito: D

4. (FCC - 2014 - PRODAM/AM - Analista de Sistemas) O framework Spring permite a troca de mensagens entre clientes através do suporte nativo ao:
a) SpringMessaging Service(SMS).

b) JavaMessaging Service(JMS).

/ 15

/

c) SpringChat Service(SCS).

d) JavaChat Service(SCS).

e) Chat andMessaging Service(CMS).

Comentários:

O Módulo ORM fornece camadas de integração para mapeamento objeto-relacional com tecnologias como JPA, Hibernate, etc. O Módulo JMS fornece a possibilidade de produzir e consumir mensagens, com integração nativa com JMS. Galera, vamos falar um pouco agora sobreSpring Security! Trata-se de um framework que se foca em fornecer autenticação e autorização aAplicações Java.

Conforme vimos em aula, trata-se do Módulo JMS!

Gabarito: B

5. (CONSULPLAN - 2012 - TSE - Analista de Sistemas) No contexto do framework Spring existem, basicamente, dois tipos de injeção de dependência, sendo que em um deles, a dependência é resolvida por meio de um construtor do objeto a receber o objeto dependente. Este tipo é conhecido por:
a) Bean Injection.

b) Setter Injection.

c) Factory Injection.

d) Constructor Injection.

Comentários:

Em vez de depender de uma classe concreta, passamos a depender de uma abstração. O
código estará mais desacoplado, modular, flexível - sendo mais fácil a manutenção e a evolução. Épossível injetar dependências de três formas: Injeção por Construtor; Injeção por Propriedade(Setter); e Injeção por Interface - esse último é injeção de dependência sem inversão de controle.

Conforme vimos em aula, são três tipos. Acredito que a questão deixou de fora o último por ele não realizar a inversão de controle. De todo modo, trata-se do Constructor Injection.
Gabarito: D

/ 15

/

LISTA DE QUESTõES - SPRING - MULTIBANCAS

1. (CESPE - 2012 - PEFO/CE - Analista de Sistemas) No Spring, as configurações de segurança são realizadas no arquivo appIicationContext-security.xml, e, para que qualquer página ou diretório seja seguro, é necessário adicionar a esse arquivo o elemento<intercept-
url>.

2. (FCC - 2010 - TRT/8 - Analista de Sistemas) Interface que representa o container loC(Inversão de Controle) do framework Spring:

a) org.springframework.pojo.factory.PojoFactory.

b) org.springframework.ioc.factory.lOCFactory.

c) org.springframework.beans.factory.BeanFactory.

d) org.springframework.mvc.factory.MVCContainer.

e) org.springframework.beans.factory.CoreContainer.

3. (FCC - 2011 - TRT/23 - Analista de Sistemas) Na estrutura do Spring o módulo que provê uma camada de abstração para JDBC, eliminando grande parte da codificação necessária para interagir com um banco de dados é o:
a) Spring Core b) Spring ORM
c) Spring Context d) Spring DAO
e) Spring AOP

4. (FCC - 2014 - PRODAM/AM - Analista de Sistemas) O framework
Spring permite a troca de mensagens entre clientes através do suporte nativo ao:
a) SpringMessaging Service(SMS).

b) JavaMessaging Service(JMS).

c) SpringChat Service(SCS).

d) JavaChat Service(SCS).

e) Chat andMessaging Service(CMS).

5. (CONSULPLAN - 2012 - TSE - Analista de Sistemas) No contexto do framework
Spring existem, basicamente, dois tipos de injeção de dependência, sendo que em um deles, a
/ 15

/

dependência é resolvida por meio de um construtor do objeto a receber o objeto dependente. Este tipo é conhecido por:
a) Bean Injection.

b) Setter Injection.

c) Factory Injection.

d) Constructor Injection.

/ 15

/

GABARITo

GABARITO

1. c

2. C

3. D

4. B

5. D

,

/

