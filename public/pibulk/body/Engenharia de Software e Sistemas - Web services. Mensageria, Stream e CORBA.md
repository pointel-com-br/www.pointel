# Engenharia de Software e Sistemas - Web services. Mensageria, Stream e CORBA

Índice

1) SOA - Mensageria e CORBA

2) WS e REST

3) WS e REST - Arquitetura Web Services

4) Resumo - WS e REST

5) Questões Comentadas - WS e REST - CESPE

6) Questões Comentadas - WS e REST - FCC

7) Questões Comentadas - WS e REST - FGV

8) Questões Comentadas - WS e REST - Diversas

9) Lista de Questões - WS e REST - CESPE

10) Lista de Questões - WS e REST - FCC

11) Lista de Questões - WS e REST - FGV

12) Lista de Questões - WS e REST - Diversas

Mensageria e CORBA

INCIDÊNCIA EM PROVA: BAIXÍSSIMA

Antes de detalhar do que se trata os conceitos de Mensageria e CORBA, é interessante discutir um pouco sobre comunicação síncrona e assíncrona. Em um sistema distribuído, as partes têm que conversar entre si e essa comunicação é realizada, em geral, por meio de trocas de mensagens.Existem duas famosas abordagens de comunicação: síncrona e assíncrona. Vamos ver de maneira bastante lúdica a diferença entre elas...
Minha - à época - namorada gostava de me ligar várias vezes durante o dia para tratar de assuntos pessoais. Até que um dia, eu tive que chegar para ela e dizer: "Amor, eu não aguento mais!Nós precisamos reduzir essa quantidade de comunicação síncrona e substituí-la por outro meio de comunicação assíncrona porque você está me atrapalhando!". Tomei um sopapo no pé da orelha e reorganizei meus pensamentos de uma forma que ela entendesse melhor! O que eu queria dizer?
A comunicação síncrona exige, como o próprio nome diz, sincronia, ou seja,
quando ela me telefonava eu tinha que parar o que estava fazendo e respondê-la imediatamente - eu não podia simplesmente ouvir e respondê-la depois. Então ela dizia: "Oi, tudo bem?"; eu respondia: "Oi, tudo bem! E você?"; ela dizia: "Tudo ótimo! Está no trabalho?"; eu respondia: "Sim, e você?"... enfim, a troca de mensagens era síncrona, ela falava algo, eu ouvia e respondia, ela também.
Como eu não podia ouvir uma pergunta dela e não a responder, isso se chamava comunicação síncrona! Foi então que um gênio colocou no Whatsapp uma nova feature que permitia enviar mensagens de voz. Dessa forma, eu podia ouvir a mensagem dela, ir fazer outra atividade e respondê-la só mais tarde quando eu tivesse um tempo livre, ou seja, a mensagem dela não bloqueava mais as minhas atividades e isso (obrigado, Deus!) se chama comunicação assíncrona.
Quando vamos para o contexto de sistemas, a abordagem assíncrona de comunicação permite que a troca de mensagens seja feita de tal maneira que o sistema que envia a mensagem não precisa esperar o processamento da resposta, ficando livre para continuar sua rotina, diferente de tecnologias de integração com RPC (Remote Procedure Call). Trata-se de uma invocação não-blocante!

É nesse cenário que se insere a mensageria, isto é, trata-se de uma maneira de resolver problemas complexos de integração de sistemas por meio da comunicação indireta entre as partes. Eporque dizemos indiretas? Suponha que tenhamos um problema complexo de integração,isto é, temos dois ou mais sistemas que precisam "conversar", entretanto eles não possuem uma linguagem comum para tal.
Para resolver esse tipo de problema, é comum inserir um middleware que auxiliará a comunicação entre os dois sistemas com o intuito e, por conta desse middleware, diz-se que a comunicação é indireta. A mensageria permite, portanto, o processamento de requisições de forma assíncrona
- além de integrar sistemas desenvolvidos em tecnologias diferentes (Ex: Java e .NET).
Qual a vantagem disso? Reduzir o grau de acoplamento (isto é, dependência) entre os componentes.
De mais a mais, a mensageria reduz gargalos dos sistemas, contribui para o aumento da escalabilidade e facilita uma arquitetura flexível e ágil, capaz de responder mais rapidamente a mudanças. Em suma, podemos dizer que a mensageria é um padrão de comunicação assíncrona utilizado em sistemas distribuídos para troca de mensagens entre diferentes componentes ou serviços.
É uma abordagem que permite o envio, recebimento e processamento de mensagens entre aplicações de forma independente e escalável. No contexto da mensageria, os sistemas são compostos por diferentes partes chamadas de produtores de mensagens e consumidores de mensagens. Os produtores de mensagens são responsáveis por gerar e enviar as mensagens para uma fila (ou tópico) de mensagens.
Os consumidores de mensagens, por sua vez, recebem essas mensagens da fila e as processam de acordo com sua lógica de negócio. Vejamos seus principais benefícios:
BENEFÍCIO | DESCRIÇÃO
|

As mensagens podem ser enviadas e processadas de forma assíncrona, ou seja, o produtor de mensagens não precisa esperar pela resposta imediata do consumidor. Isso
ASSINCRONICIDADE

permite uma maior flexibilidade e escalabilidade no sistema, já que os componentes podem trabalhar de forma independente e não precisam estar ativos simultanemente.
ACOPLAMENTO FRACO

ESCALABILIDADE

A comunicação por mensagens permite um acoplamento fraco entre os componentes do sistema. Os produtores e consumidores não precisam conhecer detalhes de implementação uns dos outros, pois a comunicação é feita por meio das mensagens.Isso facilita a manutenção e evolução dos sistemas, uma vez que os componentes podem ser modificados sem afetar diretamente os outros.
O uso de filas de mensagens permite uma maior escalabilidade horizontal do sistema.
Mais produtores e consumidores podem ser adicionados conforme necessário, e as filas podem ser dimensionadas para suportar grandes volumes de mensagens, garantindo um processamento eficiente e distribuído.
TOLERÂNCIA A FALHAS

A mensageria permite a implementação de sistemas resilientes, capazes de lidar com falhas de rede, indisponibilidade temporária de componentes e falhas pontuais. As mensagens podem ser armazenadas em filas duráveis, garantindo que nenhuma mensagem seja perdida e possa ser processada posteriormente.
A mensageria é amplamente utilizada em cenários como integração de sistemas,
processamento de eventos em tempo real, comunicação entre microsserviços, sistemas distribuídos em nuvem e muitas outras aplicações onde a troca assíncrona de mensagens é necessária. Já o CORBA1 é uma
1 CORBA = Common Object Request Broker Architeture arquitetura padrão para estabelecer e simplificar a troca de dados entre sistemas distribuídos heterogêneos por meio de uma estrutura comum para gerenciamento de objetos distribuídos.
O componente fundamental para o CORBA é o ORB (Object Request Broker'), que é responsável pela interoperabilidade entre objetos. Por meio do IOR (Interoperable ObjectReference), o ORB
consegue localizar os objetos e transmitir informações. O ORB é um módulo intermediário entre cliente/objeto, sendo responsável por aceitar requisições, enviá-las ao objeto correto e entregar a resposta ao cliente.
Além disso, ele utiliza a IDL (Interface Definition Language), uma linguagem utilizada para descrever as interfaces das implementações dos objetos na rede (seria algo similar aoWSDL).
Uma interface escrita em IDL especifica o formato da chamada das operações providas pelo objeto e os parâmetros de entrada ou saída necessários para efetuar a operação. O CORBA é dependente de linguagem de programação?
Não só ele é independente de linguagem de programação, como ele é independente de tecnologia (como plataformas, etc). Ele atua de modo que os objetos (componentes de software)possam se comunicar de forma transparente ao usuário, mesmo que para isso seja necessário interoperar com outro software, sistema operacional, ferramentas, entre outras. Vamos resumir o principal sobre o CORBA...
Trata-se de uma arquitetura de software baseada em objetos que foi desenvolvida pela
Object
Management Group (OMG) como um padrão para permitir a comunicação e interoperabilidade entre componentes de software distribuídos em uma rede. É uma tecnologia que facilita a construção de sistemas distribuídos heterogêneos, nos quais os componentes podem ser desenvolvidos em diferentes linguagens de programação e executarem diferentes plataformas.
O CORBA utiliza um modelo cliente/servidor, no qual os objetos distribuídos podem ser acessados e invocados por meio de solicitações de serviços (chamadas de métodos). Seus componentes são:
PRINCIPAIS COMPONENTES | DESCRIÇÃO
|

São componentes de software que encapsulam a lógica de negócio e oferecem serviços e operações para serem invocados remotamente. Os objetos CORBA são
OBJETOS

implementados usando uma linguagem de programação suportada pelo CORBA, como
C++, Java ou Python, e são registrados em um Serviço de Nomes (Naming Service).

OBJECT REQUEST BROKER

(ORB)

É uma infraestrutura de software responsável por facilitar a comunicação entre os objetos CORBA. O ORB atua como intermediário entre os clientes que solicitam serviços e os objetos distribuídos que oferecem esses serviços. Ele lida com a localização do objeto correto, a serialização dos parâmetros da solicitação, o envio da solicitação ao objeto e a entrega da resposta ao cliente.
INTERFACE DEFINITION
LANGUAGE (IDL)

É uma linguagem neutra de definição de interfaces utilizada para especificar a estrutura e as operações dos objetos CORBA. A IDL permite que desenvolvedores descrevam a interface de um objeto CORBA de forma independente da linguagem de programação usada para implementá-lo. A partir da IDL, é possível gerar código-fonte em diferentes linguagens para a implementação do objeto e a criação dos stubs e skeletons necessários para a comunicação CORBA.
Com o CORBA, os objetos distribuídos podem ser acessados de forma transparente, como se fossem objetos locais, independentemente de onde estejam executando. Isso significa que um objeto CORBA pode ser invocado por um cliente em uma máquina diferente, em uma plataforma diferente e até mesmo usando uma linguagem de programação diferente. O CORBAoferece diversos benefícios...

Entre eles, podemos citar a reutilização de componentes, interoperabilidade entre sistemas heterogêneos, extensibilidade, escalabilidade eflexibilidade. No entanto, o CORBAtambém possui complexidade adicional devido à necessidade de definir interfaces usando a IDLe configurar e gerenciar o ORB. Embora o CORBA tenha sido amplamente utilizado no passado, sua adoção diminuiu com o tempo em favor de tecnologias mais recentes, como WS e SOA.
No entanto, o CORBA ainda é usado em alguns domínios específicos que exigem interoperabilidade entre sistemas legados e novos ou onde a integração de sistemas distribuídos complexos é necessária. Porfim, vamos falar rapidamente sobre stream: trata-se de uma sequência contínua de dados que é transmitida, processada e consumida em tempo real. Ela é composta por um fluxo de elementos, como bytes, caracteres, números, eventos ou até mesmo objetos mais complexos.
Uma stream é conceitualmente semelhante a um fluxo de água contínuo, onde a água flui constantemente. Da mesma forma, uma stream de dados é uma sequência contínua de informações que podem ser lidas, gravadas ou manipuladas deforma incremental, em vez de serem acessadas em sua totalidade de uma vez. Elas são amplamente utilizadas em sistemas de processamento de dados em tempo real. Eles estão na moda atualmente, concordam?
Eu falo de transmissões de vídeo, áudio, mensagens instantâneas, feeds de redes sociais e muitos outros casos de uso. Elas permitem que os dados sejam transmitidos e processados de forma contínua, conforme são gerados, em vez de esperar pela disponibilidade completa dos dados. As streams podem ter várias fontes e destinos, dependendo do contexto. As operações em geral envolvem a leitura, gravação, filtragem, transformação e agregação dos dados em tempo real.
As streams podem ser processadas de forma sequencial, onde cada elemento é processado um de cada vez, ou de forma paralela, onde os elementos podem ser processados simultaneamente em diferentes threads ou nós de um sistema distribuído. Uma vantagem é a capacidade de lidar com grandes volumes de dados de forma eficiente, uma vez que os dados são processados à medida que chegam, em vez de armazenar tudo em memória ou em um local de armazenamento intermediário.
Além disso, as streams permitem a construção de sistemas assíncronos e resilientes,
onde os produtores e consumidores de dados podem operar em diferentes velocidades e se adaptar a flutuações de carga, atrasos de rede ou falhas pontuais, garantindo a continuidade do fluxo de dados. Galera, esses assuntos não caem muito em prova, mas não são assuntos complexos,então vale a leitura.
Conceitos Básicos

WEB SERvICES

INCIDÊNCIA EM PROVA: MÉDIA

Como esse é um tema mais técnico, eu vou precisar fazer uma grande contextualização para que o assunto faça sentido para vocês. Quando começaram a surgir as primeiras redes de computadores,o processamento de dados era centralizado em poucos servidores que não se comunicavam entre si. Com o passar do tempo, foram surgindo redes em todo lugar-tanto pública quanto privada formando esse emaranhado de redes que existem atualmente.
Essas redes começaram a se comunicar e as aplicações que hospedadas em poucos servidores passaram a ser hospedadas de forma distribuída em vários servidores -surgiram, então, as aplicações distribuídas. Ora, aplicações diferentes dentro de uma mesma organização precisavam se comunicar, assim como aplicações de organizações diferentes. Para resolver esse problema,surgiram os Web Services (Serviços Web).

Os web services têm a missão de fazer a integração sistemas heterogêneos. Como assim,
professor? Softwares são desenvolvidos com linguagens de programação diferentes
(Ex: Java,
Python, C, Go, JavaScript), para arquiteturas diferentes (Ex: x86, X64), para sistemas operacionais(Ex: Windows, Linux, MacOS), para dispositivos diferentes (Ex: Desktop, Mobile), entre outros. Ora,como fazer tudo isso se comunicar? Por meio dos Web Services!

Agora vamos destrinchar esse ponto: 0 que é um serviço no contexto de engenharia de software?Trata-se de um mecanismo que permite acessar um conjunto de recursos, no qual o acesso é fornecido por meio de uma interface descrita e exercitada consistentemente de acordo com restrições e políticas especificadas pela descrição do serviço. Professor, eu não compreendi uma palavra do que você disse! Calma, aos poucos isso vai fazer sentido! Vamos ver outras definições:
DEFINIÇÕES DE WEB SERVICES

Web Services tratam da disponibilização de um serviço pela internet que pode ser acessado em qualquer lugar.
Web Services são componentes de aplicativos baseados em XML, autocontidos e autodescritivos, que se comunicam usando protocolos abertos.
Web Services são uma interface que descreve uma coleção de operações que são acessíveis pela rede através de mensagens XML padronizadas.
Web Services tratam essencialmente da interoperabilidade entre programas e aplicações-especialmente quando eles usam linguagens, ferramentas ou plataformas diferentes.
Web Services são um sistema de software projetado para permitir interoperabilidade na interação entre máquinas através de uma rede.
Web Services são componentes de software com baixo fator de acoplamento, utilizado por meio de padrões de internet.
Web Services representam uma função/lógica de negócio ou um serviço que pode ser acessado por uma outra aplicação na web, sobre redes públicas e, geralmente, disponibilizado por protocolos conhecidos.
Web Services são soluções utilizadas na integração de sistemas e na comunicação entre aplicações diferentes,permitindo que elas enviem e recebam dados.

Web Services são, portanto, componentes de software que permitem a integração de aplicações distribuídas desenvolvidas com tecnologias heterogêneas, por meio do fornecimento de serviços de baixo acoplamento, protocolos abertos e interfaces bem definidas a fim de garantir a comunicação e interoperabilidade no envio e recebimento de dados entre máquinas dispostas em redes de computadores.
CARACTERÍSTICA | DESCRIÇÃO

WEB SERVICES SÃO
AUTOCONTIDOS
WEB SERVICES SÃO
AUTODESCRITIVOS

WEB SERVICES UTILIZAM
PROTOCOLOS ABERTOS

WEB SERVICES SÃO FRACAMENTE

ACOPLADOS
WEB SERVICES SÃO
INDEPENDENTES DE TECNOLOGIA

Isso significa que eles não necessitam ou dependem de outros componentes para ter uma existência própria.
Isso significa que eles não necessitam de informações externas para expor suas funcionalidades.
Isso significa que os protocolos não são de propriedade de nenhuma organização,
são apenas protocolos padrões da internet.

Isso significa que a interface do serviço pode mudar sem comprometer a capacidade do cliente de interagir com o serviço.
Isso significa que eles são independentes de plataforma, sistema operacional,
arquitetura de processador, linguagem de programação, entre outros.

Galera, vamos agora fazer uma comparação para ficar mais claro! Há alguns meses, eu
(cliente de serviço) decidi mudar de operadora de celular (provedor de serviço). Eu fui até o shopping mais próximo, entrei na loja específica, escolhi o plano que se adequava às minhas necessidades e fui assinar o contrato de serviço. O que é um contrato? É um documento que formaliza um acordo entre duas ou mais partes. Qual era o acordo que eu estava firmando?
No meu caso, eu pagaria mensalmente uma quantia em reais todo dia 10. Em troca, eles me ofereceriam o serviço de ligações ilimitadas e um pacote de internet. É claro que o contrato tem várias outras especificações em relação ao objeto, à prestação do serviço, aos direitos e deveres, à contestação de débitos, à suspensão da prestação do serviço, ao extravio do chip, à vigência, à rescisão, ao atendimento ao cliente, entre outros.
Agora vejam que a ideia aqui é semelhante: web service é um serviço! Vocês se lembram da definição de serviço? Trata-se de um mecanismo que permite acessar um conjunto de recursos, no qual o acesso é fornecido por meio de uma interface descrita e exercitada consistentemente de acordo com restrições e políticas especificadas pela descrição do serviço. Viram como é semelhante ao serviço da operadora de celular?
Ela oferece um mecanismo que permite acessar um conjunto de recursos (ligações e internet), no qual o acesso é fornecido por meio de uma interface descrita e exercitada consistentemente de acordo com restrições e políticas especificadas pela descrição do serviço (contrato). Adisponibilização de um serviço ocorre por meio de um contrato, que é uma interface padronizada que disponibiliza suas funcionalidades.
Qual é a grande vantagem da interface, professor? Galera, a interface permite que dois ou mais sistemas se comuniquem de forma transparente, isto é, sem se preocupar com detalhes de implementação. Vamos voltar à metáfora: quando eu assino o contrato (interface) com a operadora celular, ela nãoquersaberoqueeuvouterquefazerpara pagaro valormensal eeu não quero saber o que ela vai ter que fazer para oferecer o serviço de telefonia e internet móvel.
O que importa para mim é o serviço sendo prestado conforme as condições do contrato e o que importa para ela é receber a grana mensalmente na data acordada. É semelhante com os serviços web: quando um provedor oferece um serviço a um cliente, o cliente não está nem aí para como o serviço será implementado - ele só quer consumir o serviço da forma como está descrito em sua interface e ponto final. Essa é a beleza dos serviços web...
Bem, vamos ver um exemplo de Web Se/v/ce? Vamos! Eu escolhi veros dados abertos da Câmara dos
Deputados. Quem quiser acessá-los, acesse o link a seguir:

HTTPS://www2.CAMARA.LEG.BR/TRANSPARENCIA/DADoS-ABERToS/DADoS-ABERToS-LEGISLATIVo/wEBSERVICES/DEPUTAD
oS

Notem que essa página apresenta um Web Service! Logo, ela deve possuir uma interface
(contrato)
que define os serviços que são oferecidos por meio de métodos:

Métodos

Nome Descrição

ObterDeputados Retorna os deputados em exercício na Câmara dos Deputados

ObterDetalhesDeputado Retorna detalhes dos deputados com histórico de participação em comissões, períodos de exercício, filiações partidárias e lideranças.
ObterLideresBancadas Retorna os deputados líderes e vice-líderes em exercício das bancadas dos partidosObterPartidosCD Retorna os partidos com representação na Câmara dos Deputados
ObterPartidosBlocoCD Retorna os blocos parlamentares na Câmara dos Deputados.

Nesse contexto, nós somos clientes de serviços e a página é o provedor de serviço.
Que serviços ela oferece? Ela permite listar os deputados em exercício; listar detalhes dos deputados com histórico de participação em comissões, períodos de exercício, filiações partidárias e lideranças; listar os deputados líderes e vice-líderes em exercício das bancadas dos partidos; listar os partidos com representação; e listar os blocos parlamentares.
Professor, como eu faço efetivamente para utilizar esses serviços? Eu preciso saber o endpoint do serviço (URL). Notem que a página informa o endereço do endpoint-.
EndPoint https://www.camara.gov.br/SitCamaraWS/Deputados.asrTix7wsdl
Esse endpoint exibe todos os serviços oferecidos, mas é possível acessar cada um individualmente.
Como, Diego? Basta utilizar os nomes dos métodos exibidos anteriormente:

HTTPSy/WWW.CAMARA.LEG.BR/SITCAMARAWS/DEPUTADOS.ASMX/OBTERDEPUTADOS

O endereço acima contém ao final o método ObterDeputados, que lista todos os deputados dessa casa legislativa. Se eu acessar os detalhes do contrato, vou encontrar algo assim:
Dados Abertos -
Legislativo

Webservices
Deputados
Orgaos

OBTERDEPUTADOS

Retorna os deputados em exercício na Câmara dos Deputados

Proposicoes Parâmetros

SessoesReunioes

O método não possui parâmetros

Retorno

Deputados (List<Deputado>): Lista dos deputados em exercício

Nome Valor Descrição ideCadastro Int ID do parlamentar condicao String Retorna se o deputado e Titular ou suplenteNome String Nome civil do parlamentar
NomeParlamentar String Nome de tratamento do parlamentar
UrIFoto String URL para a foto do parlamentar

Sexo String Sexo (masculino ou feminino)

UF String Unidade da Federação de representação do parlamentarPartido String Sigla do partido que o parlamentar representa

Gabinete String Numero do Gabinete do parlamentar

Anexo String Anexo (prédio) onde o gabinete está localizado
Fone String Numero do telefone do gabinete

Email String Email institucional do parlamentar

Comissoes comissoes Comissões da Câmara dos Deputados que o parlamentar é membro
Acima está uma espécie de contrato do Web Service. Como assim, Diego? Ele está dizendo que, se eu acessar esse serviço web por meio do endereço apresentado anteriormente(sem nenhum parâmetro), ele me retornará a lista de todos os deputados em exercício com diversos dados dos deputados, tais como Nome, Matrícula, Sexo, UF, Partido, Gabinete, Anexo, Telefone,E-Mail, etc.
Vamos fazer um experimento?Testem aí no navegador de vocês-o resultado será algo assim:

This XML file does not appear to have any style information associated with it. The document tree is shown below.
▼<deputados>

▼<deputado>

<ideCadastro>73701</ideCadastro>

<codOrcamento>1310</codOrcamento>

<condicao>Titular</condicao>

<matricula>29K/matricula>

<idParlamentar>1637158</idParlamentar>

<nome>BENEDITA SOUZA DA SILVA SAMPAIO</nome>

<nomeParlamentar>Benedita da Silva </nomeParlamentar>

<urlFoto>http://www.camara.gov.br/internet/deputado/bandep/73701.jpg</urlFoto>

<sexo>feminino</sexo»

<uf>RJ</uf>

<partido>PT</partido>

<gabinete>330</gabinete>

<anexo>4</anexo>

<fone>3215-5330</fone>

<email>dep.beneditadasilva@camara.leg.br</email>

▼<comissoes>

<titular/>

<suplente/>

</comissoes>

</deputado»

O resultado veio em formato XML (formato de dados adotado pela W3C para troca de informações entre aplicações distribuídas). Note que ele trouxe diversos dados da deputada BeneditaSouza da
Silva Sampaio. Agora notem: eu (cliente) cumpri a minha parte e fiz uma requisição web respeitando o formato do endereço do endpoint e ele fez a parte dele me retornando uma resposta que respeita o formato acordado no contrato. Coisa linda, não é?
Vamos fazer um teste um pouco mais complexo agora! Se eu mudar o finalzinho do endereço anterior para ObterDetalhesDeputado, eu consigo listar histórico de participações, etc.
HTTPS://www.CAMARA.LEG.BR/SITCAMARAwS/DEPUTADoS.ASMX/oBTERDETALHESDEPUTADo

No entanto, vendo os detalhes do contrato desse método, é possível verificar que ele permite receber alguns parâmetros de entrada para filtrar os resultados de saída. Vejamos:
Dados Abertos -
Legislativo

Webservices
Deputados
Orgaos
Proposicoes
SessoesReunioes

OBTERDETALHESDEPUTADO

Retorna detalhes dos deputados com histórico de participação em comissões, períodos de exercício,
filiações partidárias e lideranças.
Parâmetros

Nome Valor Descrição ideCadastro String(Opcional) Identificador do deputado obtido na chamada aoObterDeputados.

numLegislatura Int(Opcional) Número da legislatura. Campo vazio, todas as legislaturas do Deputado.
Retorno deputados(List<deputado>): Lista os detalhes do Deputado nos mandatos.
Nome Valor Descrição email String Email do parlamentar nomeProfissao String Profissão do parlamentar dataNascimento String Data de nascimento dataFalecimento String Data de falecimento ufRepresentacaoAtual String UF da representação parlamentar situacaoNaLegislaturaAtual string Situação do parlamentar na legislatura (Em exercício.Licenciado, Afastado,

Vacância e Suplência)

ideCadastro Identificado único do parlamentar nomeParlamentarAtual Nome parlamentar nomeCivil Nome Civil sexo Sexo
Ela permite inserir o identificador do deputado e o número de sua legislatura para filtrar os detalhes do deputado com histórico de participação em comissões, períodos de exercícios,filiações partidárias e lideranças. Para visualizar os dados detalhados da deputada Benedita Souza da SilvaSampaio, eu vou inserir o seu identificador de cadastro (73701) e o número da legislatura (55) -ambos os dados estavam no resultado do serviço web visto anteriormente.

O resultado é apresentado a seguir: é apresentado e-mail, profissão, data de nascimento, estado,sexo, partido e, além disso, é mostrado o histórico de quais comissões ela participou nessa legislatura (Ex: CREDN - Comissão de Relações Exteriores e de Defesa Nacional -Entrada em
15/04/2015 e saída em 02/02/2016). Caso eu não informe o parâmetro da legislatura,
será retornado o histórico de todas as legislaturas de que a deputada participou.
This XML file does not appear to have any style information associated with it. The document tree is shown below.
▼<Deputados>

▼<Deputado>

<numLegislatura>55</numLegislatura>

<email>dep.beneditadasilva@camara.leg.br</email>

<nomeProfissao>Assistente social, Auxiliar de enfermagem, Professor, Servidor público</nomeProfissao>
<dataNascimento>26/04/1942</dataNascimento>

<dataFalecimento> </dataFalecimento>

<ufRepresentacaoAtual>R3</ufRepresentacaoAtual>

<situacaoNaLegislaturaAtual>F</situacaoNaLegislaturaAtual>

<ideCadastro>73701</ideCadastro>

<idParlamentarDeprecated>76</idParlamentar0eprecated>

<nomeParlamentarAtual>BENEDITA DA SILVA</nomeParlamentarAtual>

<nomeCivil>BENEDITA SOUZA DA SILVA SAMPAIO</nomeCivil>

<sexo>F</sexo>

▼<partidoAtual>

<idPartido>PT</idPartido>

<sigla>PT</sigla>

<nome>Partido dos Trabalhadores</nome>

</partidoAtual>

▼<gabinete>

<numero> </numero>

<anexo> </anexo>

<telefone> </telefone>

</gabinete>

▼<comissoes>

▼<comissao>

<id0rgaoLegislativoCD>537953</id0rgaoLegislativoCD>

<siglaComissao>CEXFISC</siglaComissao>

<nomeComissao>Comissão Externa, sem ônus para a Câmara dos Deputados, destinada a acompanhar a crise fiscal instalada no Estado do Rio de Janeiro</nomeComissao>
<condicaoMembro>Titular</condicaoMembro>

<dataEntrada>10/ll/2016</dataEntrada>

<dataSaida>31/01/2019</dataSaida>

</comissao>

Está ficando mais claro? Vocês viram que há um contrato que define a interface do serviço web disponível e que, caso o cliente faça a requisição do serviço por meio da sintaxe correta do endereço de seu endpoint, serão retornadas as informações exatamente de acordo com o que estava descrito no contrato. Professor, eu achei muito feio esse formato de saída das informações dos web services...
Galera, o formato XML é utilizado para representar e transportar dados de forma que possa ser lido tanto por máquinas quanto por humanos. Perceba que a ideia desse formato não é exibir uma saída visualmente bonitinha - é simplesmente representar e transportar os dados. Aliás,agora vem a grande sacada: caso uma aplicação queira se integrar com as aplicações daCâmara dos
Deputados, ela poderá fazê-lo por meio por meio de Web Service! Como é, Diego?

Imagine que eu crie uma ONG (Organização Não-Governamental) cujo intuito é fiscalizar o trabalho dos deputados federais. Para facilitar o trabalho dos fiscais que eu contratei para a minha ONG,seria interessante desenvolver uma aplicação de software. Além disso, é óbvio que a minha aplicação deveria ter acesso aos dados oficiais da Câmara dos Deputados! O que eu poderia fazer para realizar essa integração?
Eu poderia entrar em contato com área de tecnologia da Câmara dos Deputados e perguntar quais tecnologias são utilizadas para fazer a programação, qual é o sistema gerenciador de banco de dados utilizado, quais eram os dados disponíveis, entre outros. Para quê? Para tentar fazer com que a minha aplicação (que eventualmente pode ser feita utilizando tecnologias diferentes) se comunique de forma compatível com a aplicação dessa casa legislativa.
Vamos supor que, por um milagre do destino, eu consiga fazer toda essa integração entre os sistemas! O que aconteceria se eventualmente eles mudassem alguma tecnologia? E se eles mudassem a implementação do sistema? E se eles mudassem de sistema gerenciador de banco de dados? E se eles mudassem o formato de armazenamento dos dados?Tudo isso poderia impactar de forma negativa a integração e a comunicação entre os dois sistemas.
O ideal, portanto, seria fazer a integração dos sistemas por meio de um Web Service.
A utilização de serviços web permite que todas essas mudanças ocorram indiscriminadamente desde que a interface (contrato) permaneça a mesma. Como é, Diego? É isso mesmo! A Câmara dos Deputados pode fazer a alteração que quiser: se ela mantiver a interface imutável, meu sistema sequer vai perceber que houve mudanças - será transparente para ele.
Essa é a grande sacada dos serviços web: aplicações distribuídas que foram desenvolvidas com tecnologias completamente diferentes podem ser comunicar por meio de serviços de baixo acoplamento, protocolos abertos e interfaces bem definidas. Clientes enviam requisições com informações bem definidas e recebem respostas também bem definidas de forma síncrona ou assíncrona. E mais: uma vez descrito, padronizado e catalogado, o serviço se torna reutilizável.
Vejam que bacana: o serviço web permite a interoperabilidade entre aplicações distribuídas, não é necessário conhecer sua implementação, possibilita a comunicação com novas aplicações ou também com aplicações legadas, é reutilizável e independente de tecnologia,utiliza protocolos padronizados e padrões abertos (não proprietários), melhora a usabilidade,possui baixo acoplamento, reduz os custos, não requer a interação de usuários finais1, entre outros.
1 Há implementações de Web Services que tratam da interação máquina-máquina ou aplicação-aplicação - sem a obrigatoriedade de interferência humana.
Arquitetura de Web Services

INCIDÊNCIA EM PROVA: MÉDIA

A arquitetura de Web Services envolve basicamente três categorias de participantes:
Provedor de
Serviço (Service Provider), Solicitante do Serviço (Service Requester) e Agente de
Serviço
(Service Broker). Quem é o provedor de serviço? É qualquer aplicação que forneça serviços web.Quem é o solicitante do serviço? É qualquer aplicação que deseje utilizar serviços web. E quem é o agente de serviço? É qualquer aplicação que faça a intermediação entre provedor e solicitante.
Quem aíjá investiu na bolsa de valores? Para você comprar ou vender ações, é necessário ter acesso a um Home Broker! O que é isso? É um sistema que atua na intermediação da compra e venda de valores mobiliários de investidores. Por exemplo: eu uso o Home Broker para fazer uma oferta de compra de uma ação e outro investidortambém o utiliza para fazer uma oferta de venda.Se nossas ofertas forem compatíveis, o negócio é fechado!
Com os serviços web, ocorre de maneira bastante semelhante! Um Service Broker faz a intermediação entre o Service Provider e o Service Requester. O fornecedor de serviços publica os seus serviços disponíveis no agente de serviços e o solicitante pesquisa por serviços que o satisfaçam. É importante destacar que quando um fornecedor e um solicitante entram em acordo, ocorre o que chamamos de Bind (Vínculo).
Paradigma SOAP

Galera, agora vamos começar a falar de termos mais técnicos! Uma das formas de realizar a comunicação entre serviços web é por meio de três padrões fundamentais:
PADRÕES | DESCRIÇÃO

SOAP (SIMPLE/SINGLE OBJECT

ACCESS PROTOCOL)
WSDL (WEB SERVICES
DESCRIPTION LANGUAGEJ

UDDI [UNIVERSAL DESCRIPTION,
DISCOVERYANDINTEGRATIONJ

Baseado em XMLZ define uma organização para troca estruturada de dados entre
Web Services.

Baseado em XML, define como as interfaces dos Web Services podem ser representadas.
Baseado em XML, trata-se do padrão de descobrimento que define como as informações podem ser organizadas.
Professor, há outras maneiras de implementar serviços web? Sim, existem outras tecnologias e paradigmas - os principais são os Paradigmas SOAP e REST! Vamos iniciar falando sobre o primeiro, já que ele é o mais antigo. Bem, a tabelinha apresentada acima é muito muito muito importante - ela sozinha permite responder dezenas ou até centenas de questões de provas. Essa é a base para os serviços web do Paradigma SOAP.
WS-
ENCRPYTIDN

WS-SERCURE
CONVERSATIDN

ws-
PDLICY

ws-
SIGNATURE

WS-
FEDERATIDN

WS-
TRUST

liVS-SECURITY
SOAP

WS-I
BASIC SECURITY

WS-
AUTHDRIZATIDN

ws-
PRIVACY

No entanto, com o passar do tempo, começaram a surgir algumas lacunas de qualidade-especialmente nas áreas de segurança relacionadas a criptografia, assinatura digital,autorização, conversação, federação, políticas de segurança, privacidade, entre outros. Surgiram, então,diversas extensões para fornecer um conjunto sofisticado de componentes construídos para supriressas lacunas. Esse conjunto de extensões de segurança ficou conhecido como WS-Security.
Em seguida, surgiram outras especificações relacionadas a outros temas, como processos de negócio, mensageria, especificação de metadados, especificação de recursos,especificação de gerenciamento, interoperabilidade, transações, entre outros. Esse conjunto de especificações com suas respectivas extensões foram chamados de WS-*. O que você precisa guardar é que o escopo foi aumentando cada vez mais...
SOAP

INCIDÊNCIA EM PROVA: ALTÍSSIMA

DEFINIÇÃO DE SOAP

Trata-se de uma das formas de comunicação para encapsular dados transferidos no formato
XML para Web
Services.

Trata-se de um formato baseado em XML para intercâmbio de mensagens - é utilizado para realizar o encapsulamento e o transporte de dados.
Trata-se de um formato para envio e recebimento de mensagens independentemente de plataforma e tecnologia.
Trata-se de um protocolo baseado em XML que define uma organização para a troca estruturada de dados entreWeb Services.

Um dos motivos que tornam os serviços web tão atrativos é o fato de serem baseados em tecnologias padrão. Como assim, Diego? Existe uma organização de padronização da web chamadaW3C (WWW Consortium). Ela agrega empresas, órgãos governamentais e organizações independentes com a finalidade de estabelecer padrões para a criação e a interpretação de conteúdos para a web.
Em outras palavras, essa organização recomenda um conjunto de tecnologias e formatos aprovados para que sistemas web possam se comunicar sem problemas. Vocês já imaginaram se alguém cria um componente em uma página web com uma tecnologia proprietária que eu só consigo acessar se eu tiver que pagar por aquela tecno/og/a?Complicaria toda a interação entre componentes web.
A W3C recomenda padrões como XML, HTML, PNG, SVG, XHTML, CSS, etc-todos eles são abertos, logo não são de propriedade de nenhuma organização e podem ser utilizados livremente. Pois bem... os serviços web utilizam tecnologias padrão da internet comoXML e HTTP.
Essas tecnologias são comumente utilizadas para disponibilizar serviços web, podendo ser acessados por outras aplicações.
Nesse contexto, temos o SOAP! Trata-se de um protocolo baseado na linguagem XML para a troca de mensagens. Ele foi projetado para invocar aplicações remotas em um ambiente independente de tecnologias, sendo o padrão para serviços web que utilizem o ParadigmaSOAP.
É importante destacar que XML é apenas a linguagem comum para intercomunicação entre diferentes sistemas, mas o protocolo utilizado para transportar a mensagem é HTTP.
Professor, é obrigatório utilizar esse protocolo para envio/recebimento de informações entre serviços web? Não, é possível utilizar outros protocolos (Ex: SMTP), mas esse é o protocolo padrão da web,logo ele é o mais utilizado atualmente (inclusive em outros paradigmas). Professor,
está começando a ficar muito abstrato e eu não estou conseguindo acompanhar! Então vamos passar para alguns pontos mais concretos...
0 que é o SOAP? É um protocolo! Para quê? Para a troca estruturada de dados entre serviços web em redes de computadores. Ele não é um formato? Sim, esse protocolo especifica um formato comum de mensagens. Baseado em quê? Baseado na linguagem XML. E o que é o XML? Éuma linguagem de marcação que permite definir um conjunto de regras para troca de dados,podendo ser compreendida tanto por humanos quanto por máquinas.
Vamos conhecer o tal do formato especificado pelo SOAP? O SOAP consiste basicamente dos elementos descritos na tabela seguinte:
ELEMENTOS | SITUAÇÃO DESCRIÇÃO
|

Trata-se do elemento-raiz do documento XML. Ele identifica o documento XML como

ENVELOPE
(ENVOLOPE)

CABEÇALHO
(HEADER]

CORPO

OBRIGATÓRIO

OPCIONAL

uma mensagem SOAP e funciona como um recipiente que contém os demais elementos da mensagem (Ex: Header e Body). Corresponde à descrição da mensagem e do que deve ser processado.
Trata-se do elemento que carrega informações adicionais específicas para a aplicação a fim de estender as funcionalidades das Mensagens SOAP. Desta forma, é possível adicionar novas funcionalidades como autenticação, criptografia, autorização,assinatura digital, etc. Podem ser definidos vários cabeçalhos.

Trata-se do elemento que contém a carga útil (payload) da Mensagem SOAP. É aqui que

OBRIGATÓRIO

(BODYJ

estão as informações propriamente ditas do serviço web remetidas ao destinatário final da mensagem, incluindo a chamada ao procedimento ou o retorno de seu resultado.
Trata-se do elemento contido no corpo responsável por relatar possíveis erros de envio

FALHA
IFAULTJ

OPCIONAL

ou processamento de mensagens, informando localização e formato dos erros encontrados. Quando estiver presente deve aparecer como um elemento filho do elemento Body.
Vamos ver como é uma Mensagem SOAP? No exemplo a seguir, temos uma requisição em que é chamado um procedimento chamado retornaNome, que recebe CPF como parâmetro:
POST /InStock HTTP/1.1
Host: www.dre.ufrj.br

Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="l.0"?>

<soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap- envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding"
xmlns:tiposns="http://www.w3.org/2001/XMLSchema">

<soap:Header>

<m:atenticacao xmlns:m="http://www.dre.ufrj.br/ws/dre">21423edf69fgs</m:atenticacao

</soap:Header>

<soap:Body>

<m:retornaNome xmlns:m="http://www.dre.ufrj.br/ws/dre">

<numdre type="tiposns:int">123.456.789-00</drenum>

</m:retornaNome>

</soap:Body>

</soap:Envelope>

Notem que, em verde, temos o envelope; em laranjado, temos o cabeçalho (que adiciona uma funcionalidade de autenticação); e, em azul, temos o corpo (que recebe o CPF). E a resposta:
HTTP/1.1 200 OK

Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="l.0"?>

<soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap- envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding"
xmlns:tiposns="http://www.w3.org/2001/XMLSchema">

<soap:Header>

<m:atenticacao xmlns:m="http://www.dre.ufrj.br/ws/dre">2kg469fgs</m:atenticacao>

</soap:Header>

<soap:Body>

<m:retornaNomeResponse xmlns:m="http://www.dre.ufrj.br/ws/dre">

<nome type="tiposns:string">3oão da Silva</nome>

</m:retornaNomeResponse>

</soap:Body>

</soap:Envelope>

Notem que a resposta do serviço web retornou o nome João da Silva para o CPF
informado como parâmetro. Vejam também que há, em amarelo, o elemento/au/t vazio, porque não houve falhas.Professor, eu preciso entender esse código em detalhe? Não, pessoal... basta saber a função dos quatro elementos. Vejam que não é difícil identificá-los em uma Mensagem SOAP! Você faz uma requisição e recebe uma resposta como resultado.
WSDL

INCIDÊNCIA EM PROVA: ALTÍSSIMA

DEFINIÇÃO DE WSDL

Trata-se de uma linguagem de descrição de web services, escrita emXML, para descrever serviços web,
especificar as formas de acesso, as operações/métodos disponíveis.
Trata-se de uma linguagem para descrever serviços de rede como endpoints(ou portas) que operam em mensagens que contêm informações orientadas à documento/procedimento.
Trata-se efetivamente de especificação que define como descrever serviços web em uma gramática XML.

Trata-se de um protocolo baseado em XML para troca de informações em ambientes distribuídos e descentralizados (sim, alguns autores o consideram também como um protocolo).
Vocês já pensaram de que forma um cliente de um serviço web sabe qual formato dos métodos a serem chamados? Quais os parâmetros que devem ser passados? Como se deve processar uma requisição específica? Para responder a essas questões, criou-se uma linguagem para padronizar as descrições das funcionalidades oferecidas por um Web Service. Trata-se de uma linguagem para descrição de serviços web.
Baseada em XML, é utilizada para descrever um Web Service e deve, portanto,
definirtodas as suas interfaces, operações, métodos, parâmetros, esquemas de codificação, portas de comunicação,protocolos, formatos de mensagens, entre outros. Tão logo o cliente tenha acesso à descrição do serviço a ser utilizado, a implementação do Web Service pode ser feita em qualquer linguagem de programação.
Quando um cliente deseja enviar uma requisição para um serviço web, ele obtém a descrição do serviço e, em seguida, constrói a mensagem de acordo com a especificação da descrição encontrada no documento. Em seguida, a mensagem é enviada para o endereço onde o serviço está localizado, a fim de que possa ser processada. O serviço web recebe a mensagem e realiza uma validação conforme as informações contidas no Documento WSDL.
Vamos recapitular? O SOAP é o protocolo responsável por especificar a organização das mensagens trocadas entre o cliente e o fornecedor de serviços web, isto é, a composição da estrutura das mensagens. Já o WSDL é o documento que, resumidamente, descreve quais são as operações disponíveis em um serviço web com todas as particularidades de suas interfaces como métodos,parâmetros, protocolos, entre outros. Vamos aprofundar um pouco mais?

WSDL separa a descrição de um serviço em duas perspectivas:
Abstrata e Concreta! A perspectiva abstrata trata da interface do serviço. Em outras palavras, descreve o que o serviço faz:parâmetros, tipos, operações, entradas, saídas, mensagens fault,
etc. Já a perspectiva concreta trata da implementação do serviço. Em outras palavras, descreve como o serviço é feito: protocolos de comunicação, codificação de dados, localização, portas, endereço de rede, etc. Ela também adiciona informações sobre como o serviço se comunicará e quem pode alcançá-lo.
Professor, qual a vantagem de fazer essa separação? A vantagem é que, caso a implementação(perspectiva concreta) do serviço seja modificada por alguma razão, a interface
(perspectiva abstrata) pode continuar a ser disponibilizada sem problemas - e até reutilizada para diversas implementações diferentes. Porfim, o WSDL define quatro padrões de mensagens suportadas para quatro tipos de operações:
TIPO | DEFINIÇÃO

ONE-WAY A operação pode receber uma requisição, mas não retornará uma resposta.

REQUEST-RESPONSE A operação pode receber uma requisição e retornará uma resposta.

SOLICIT-RESPONSE A operação pode enviar uma requisição e esperará por uma resposta.

NOTIFICATION A operação pode enviar uma mensagem, mas não esperará por uma resposta.

UDDI

INCIDÊNCIA EM PROVA: ALTÍSSIMA

DEFINIÇÃO DE UDDI

Trata-se de um serviço de diretório, baseado em XML, em que é possível registrare localizar Web
Services.
Trata-se de uma especificação técnica que tem como objetivo descrever, descobrir e integrar Web
Services.

Trata-se de um diretório/registro para armazenamento de informações sobre Web Services - é um repositório de interfaces de Web Services descritas por WSDL.
Trata-se de um protocolo que é um dos maiores blocos de construção requeridos para construir Web
Services com sucesso (Sim, alguns o chamam de protocolo!).
Trata-se de um padrão de descoberta que define como são organizadas as informações de descrição do serviço,permitindo que os solicitantes descubram os serviços.

Galera, nós já sabemos que o SOAP é responsável por especificar a organização para a troca de mensagens entre serviços web e também sabemos que o WSDL é responsável por nos descrever a interface das operações disponíveis em um serviço web. Agora uma pergunta:como eu vou encontrar um serviço web? Aonde eu procuro? Onde eles estão? O que comem? Onde vivem?Para respondera essas perguntas, existe o UDDI!
Quando se constrói um serviço web, ele deve ser disponibilizado em algum lugar para que seja acessível por diversas aplicações-cliente. O UDDI é uma especificação técnica, ou protocolo e um serviço de diretório onde empresas podem registrar, publicar, descrever, buscar,descobrir e integrar serviços web. Ele contém informações genéricas sobre a provedores de serviços web,implementações e metadados básicas sobre eles.

Vamos testar a faixa etária dos meus alunos agora! Alguém sabe o que é esse livro da imagem ao lado? Galera, isso é uma lista telefônica. Quando o telefone fixo começou a se popularizar, todas as casas e empresas possuíam seus telefones. E se acabasse o gás na minha casa e eu precisasse ligar em uma companhia de gás para terminar meu almoço,jovem? Não tinha internet! Você tinha que pegar sua pesada lista telefônica e pesquisar nas páginas amarelas por empresas de gás para descobrir seu telefone.
A lista telefônica era dividida em duas partes: as páginas brancas continham os nomes e os números de telefone não comerciais (isto é, residenciais) e as páginas amarelas continham os nomes e os números de telefone comerciais (isto é, empresariais). O que isso tem a ver com a aula, Diego? OUDDI era basicamente uma Lista Telefônica! Ambos eram um serviço de diretório para registrar,publicar, descrever, buscar, descobrir e integrar telefones ou serviços web.

Essa metáfora é tão óbvia que está na própria teoria dos serviços web. Como assim,
professor?
Galera, as informações capturadas no contexto do UDDI podem serclassificadas em três categorias principais: Páginas Brancas, Páginas Verdes ou Páginas Amarelas. No entanto, evidentemente aqui elas possuem um significado um pouco diferente do significado das listas telefônicas de antigamente...
As Páginas Brancas contêm informações gerais sobre a organização que está oferecendo o serviço web, tais como nome e descrição do negócio (de preferência, em diversas línguas).Utilizando essas informações, é possível encontrar algum serviço sobre o qual já se pode conhecer algumas informações. Há também informações de contato do negócio (Ex: Endereço,Telefone, Fax,
Identificadores, etc).

A Páginas Amarelas contêm uma classificação do serviço ou negócio disponíveis baseado em taxonomias padronizadas (Ex: SIC, NAICS, UNSPSC). Como é, Diego?Ás Páginas Amarelas usam os esquemas de categorização industrial mais aceitos no mercado, códigos de indústria,códigos de produtos, códigos de identificação comerciais e similares para tornar mais fácil para as empresas procurarem por meio de listas e encontrarem exatamente o que elas desejam.
Professor, eu ainda não entendi! Por exemplo: UNSPSC (United Nations Standard Products andServices Code) é uma taxonomia de produtos e serviços para e-commerce. Ela possui um conjunto de códigos que permitem classificar e identificar uma organização quanto ao setor comercial.Sacaram? Já as Páginas Verdes contêm informações mais técnicas sobre como acessar um serviço web.
Elas são utilizadas para indicar os serviços oferecidos por cada negócio,
incluindo todas as informações técnicas envolvidas na interação e acesso ao serviço. Em geral, essas informações incluem uma referência para uma especificação externa e um endereço para invocar o serviço. Por meio do UDDI, é possível encontrar os contados do dono do serviço web, seu setor de serviço,algumas informações técnicas e uma referência para o WSDL.

O UDDI praticamente morreu nos últimos anos. Por que, professor? Porque não faz mais sentido você manter seus serviços web em um diretório específico. Qualquer pesquisa simples noGoogle permite encontrar serviços web da organização que você deseja. Eu, por exemplo,simplesmente escrevi web services câmara dos deputados no Google e já encontrei uma página contendo os serviços web fornecidos por esse órgão.
web services câmara dos deputados X B
Q,

Q Todas Q Imagens (y) Notícias 0 Videos Q Maps * Mais Configurações Ferramentas
Aproximadamente 450.000 resultados (0,71 segundos)

https://www2.camara.leg.br dados-abertos-legislativo »

Webservices — Portal da Câmara dos Deputados

Câmara dos Deputados - Palácio do Congresso Nacional - Praça dos Três Poderes Brasília -
DF - Brasil - CEP 70160-900 CNPJ: 00.530.352/0001-59.

Galera, um repositório de serviços web é inútil sem alguma forma de acessá-lo. O
padrão UDDI
versão 2.0 especifica duas interfaces com diversos métodos/operações para consumidores e provedores de serviços interagirem. Os consumidores de serviço usam a Interface deConsulta
(Inquiry) para localizar e consultar um serviço, e os provedores de serviço usam a
Interface de
Publicação (Publisher) para publicar e atualizar um serviço.

Vamos agora fazer um resumão do Paradigma SOAP! Uma aplicação
(Cliente/Solicitante de
Serviço) utiliza um serviço de diretórios (Agente de Serviço)-como o UDDI-para localizar o serviço web oferecido por um servidor (Servidor/Fornecedor de Serviço). O UDDIfornece várias informações sobre o serviço web, incluindo a sua descrição por meio do WSDL. Ocliente analisa o
WSDL e envia uma Mensagem SOAP requisitando um serviço de acordo com as especificações.

A mensagem é, então, enviada para o fornecedor do serviço, que interpreta a mensagem
(realiza o parsing da mensagem) e invoca o método apropriado, passando os parâmetros fornecidos na mensagem. O método executado, então, retorna o resultado para o Servidor SOAP, que escreve uma Mensagem SOAP respondendo a requisição inicial com o resultado e envia para oCliente
SOAP. Por fim, este último lê a mensagem e repassa o resultado para a aplicação requisitante.

Paradigma REST

INCIDÊNCIA EM PROVA: ALTA

Antes de falarmos sobre o REST, precisamos falar um pouco sobre HTTP. O HTTP
(HyperText
Transfer Protocol) é um protocolo de comunicação utilizado para transferência de hipertextos.O que seria um hipertexto?Trata-se de um texto que pode ser integrado a diversas outras formas de informação, como imagens, sons e outras mídias, acessíveis por meio de hiperlinks. Dito isso, o que importa de fato para o desenvolvimento de sistemas?
Bem, esse protocolo define oito métodos de requisição (também chamados de verbos)responsáveis por indicar a ação a ser executada para um dado recurso. Como é, Diego? Quando você utiliza esse protocolo, você está basicamente fazendo uma requisição de um recurso na web(Ex: Página Web). No entanto, esse protocolo permite fazer bem mais do que simples requisições de recursos. Vamos conhecer esses oito métodos:
MÉTODO | DESCRIÇÃO
|

GET Esse método solicita a representação de um recurso específico. Requisições utilizando o método GETdevem retornar apenas dados.

HEAD Esse método solicita uma resposta de forma idêntica ao método GET, porém sem conter o corpo da resposta.
PUT Esse método substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.
POST Esse método é utilizado para submeter uma entidade a um recurso específico,
frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor.
DELETE Esse método remove um recurso específico.

TRACE Esse método executa um teste de chamada loop-backjunto com o caminho para o recurso de destino.
CONNECT Esse método estabelece um túnel para o servidor identificado pelo recurso de destino.
OPTIONS Esse método é usado para descrever as opções de comunicação com o recurso de destino.
PATCH Esse método é utilizado para aplicar modificações parciais em um recurso.

Nosso interesse aqui está apenas nos métodos GET e POST! Notem que eu estou utilizando oProtocolo HTTP. Eu estou requisitando a página index.php que está hospedada no diretório chamado pasta do servidor cujo domínio é sitequalquer.com. Para solicitar esse recurso(página web), eu forneci dois parâmetros após o ponto de interrogação: nome e senha. O GET é utilizado para solicitar um recurso específico...
HTTP://WWW.SITEQUALQUER.COM/PASTA/INDEX.PHP?NOME=DIEGO&SENHA=ESTRATEGIA

Já o POST é utilizado para enviar dados para um recurso, geralmente realizando alguma alteração.
Dessa forma, GET é utilizado para leitura e POST é utilizado para criação! Ambos permitem o envio de parâmetros, no entanto há uma diferença fundamental entre eles: GETdeixa os parâmetros visíveis na URL; POST esconde os parâmetros no corpo da mensagem. No exemplo anterior, os parâmetros estão visíveis, logo se trata de um GET.
No entanto, há um risco na requisição anterior! Já notaram qual é? Como eu estou utilizando GET,os parâmetros estão visíveis, mas um dos parâmetros é uma senha-isso é perigosíssimo!
Imaginem sua senha circulando por aí entre roteadores e servidores até chegar ao destino final.Logo, deve-
se evitar utilizar o GET quando as informações de parâmetros forem sensíveis -
recomenda-se utiliza o POST.
Lembrando que o GET é utilizado para recuperar informações (em geral, poucas) e POST
é utilizado para enviar informações (em geral, muitas - como formulários). Agora, vamos examinar como as conexões seguras podem ser alcançadas. Quando a web repentinamente chegou ao público,ela foi utilizada apenas para páginas estáticas, mas - em pouco tempo - algumas empresas tiveram a ideia de usá-la para transações dinâmicas.
Como assim, Diego? Uma página estática é aquela que só tem o texto com alguns links, mas que não possuem recursos dinâmicos que se alteram de acordo com parâmetros, login, entre outros. Já uma página dinâmica é como a página do Estratégia Concursos: você acessa, faz o login, vê os cursos em que você está matriculado, altera configurações de usabilidade, entre outros. Como empresas da área de finanças começaram a fazer páginas dinâmicas, surgiu uma demanda...
Era necessário ter uma tecnologia para conexões mais seguras! Em 1995, a
Netscape-empresa que dominava o mercado de navegadores web - introduziu um recurso de segurança chamado SSL(Secure Sockets Layer) para atender a essa demanda. O Netscape permitia, portanto, ter uma comunicação segura e criptografada. E a junção do SSL + HTTP resultou no HTTPS(atualmente, é utiliza o TLS em vez do SSL).
O Protocolo SSL constrói uma conexão segura entre dois dispositivos -
trata-se de uma nova camada colocada entre a camada de aplicação e transporte. Depois que a conexão segura é estabelecida, a principal tarefa da SSL é manipular a compactação e a criptografia.Galera, há muitos outros pontos que podem ser abordados sobre esse protocolo, mas vamos parar aqui porque isso tudo é só para entendermos melhor o Paradigma REST!
Inicialmente, vamos falar sobre a motivação para criação do Paradigma REST!
Professor, 0
Paradigma SOAP não era tudo de bom? Galera, ele realmente tinha muitas vantagens-ele permitia o desenvolvimento de serviços web altamente confiáveis, complexos e de qualidade. No entanto, como vocês devem saber, o mundo da tecnologia muda bastante de forma muito rápida em pouco tempo.
Em 2007, começaram a se popularizar os smartphones, mas eles possuíam um baixo poder computacional (hoje em dia, eles são verdadeiras máquinas, mas naquela época eram bem mais fracos). Além disso, as redes móveis de internet ainda suportavam baixa velocidade - a tecnologia
3G original possuía uma velocidade máxima de download de 0.3 Mbps; o 4G atual suporta até 900Mbps; e o 5G promete chegar aos sGbps.

Em um contexto de dispositivos com baixo poder computacional e baixa velocidade de internet móvel, o overhead (sobrecarga) do Paradigma SOAP começou a pesar! Como assim, Diego?Nós vimos que uma Mensagem SOAP é composta de um Envelope com Cabeçalho, Corpo e Falhas.Além disso, ela pode conter recursos que estendem suas funcionalidades, como criptografia,assinatura digital, autorização, privacidade, entre outros.

Vejam, portanto, que os dados em si estão no corpo da mensagem. No entanto, há diversos outros elementos que pesam a troca de dados. Essa foi a grande motivação para o surgimento de um novo paradigma mais simples e leve: Paradigma REST (REpresentational StateTransfer). Trata-se de um estilo arquitetural ou de desenvolvimento para projetar e construir aplicações de rede distribuídas fracamente acopladas. Vamos conhecer as principais diferenças...
you need t the point A t0 P°'n - tch: Until somethmg * jn to
SOAP

you th. Catch-. 'o*

ot the compie*51"
weight'

Na imagem acima, temos algumas representações: o dado que deve ser transportado é representado por uma pessoa e o meio de transporte é o cavalo. Logo, temos que o dado (Pessoa)será efetivamente transportada de um ponto para outro por meio de um cavalo
(HTTP). Além disso, temos a representação dos dois paradigmas principais: REST e SOAP. Vamos entender a principal diferente entre eles...
No primeiro caso, se você quiser enviar um dado de um ponto para outro,
você pode simplesmente subir no cavalo e cavalgar. No segundo caso, também temos uma pessoa e um cavalo, mas junto temos uma carroça. Vocês lembram que nós falamos sobre 0 overhead? Pois é, a carroça é a carga extra (sobrecarga) para transportar uma pessoa entre dois pontos. Logo, o segundo caso possui um peso a mais na troca de mensagens.
Ambos levam uma pessoa (dado) de um Ponto A para um Ponto B por meio de um cavalo
(HTTP),
mas o primeiro é bem mais leve que o segundo. Professor, posso dizer que RESTé melhor que SOAP?
Não, tudo dependerá do contexto! Se você apenas deseja chamar um serviço leve com parâmetros e respostas bem diretos, utilize o REST; se você deseja passar diversos parâmetros compostos e aninhados com respostas complexas, utilize o SOAP. Enfim...
REST é menos burocrático, tem menos overhead, suporta diversas linguagens e tem maior desempenho/escalabilidade. SOAP é mais burocrático, tem mais overhead, suporta apenas XMLe tem menor desempenho/escalabilidade. Além disso, há mais uma diferença importante: noSOAP, existe uma especificação que deve ser seguida para todas as requisições/respostas
(chamada WSDL); no REST, não existe nenhuma especificação obrigatória.

SOAP

[SIMPLE OBJECT ACCESS PROTOCOLJ

REST
[REPRESENTATIONAL STATE TRANSFERI

É um protocolo de comunicação baseado em XML. É um estilo arquitetural ou de desenvolvimento independente de tecnologia.
Utiliza um Envelope enviado por geralmente por HTTP

para transmitir dados.
Suporta somente recursos no formato XML.

Permite invocar serviços por meio de Métodos RPC

(Remote Procedure Cal Is).
Em geral, apresenta desempenho e escalabilidade menor, devido ao alto overhead.
Não permite fazer caching.

Requer maior largura de banda para trafegar os dados.
Suporta recursos da WS-Security para incrementar a segurança.JavaScript pode chamar SOAP, mas é de difícil de implementação.
Utiliza diretamente recursos oferecidos de forma nativa,
em regra, pelo HTTP.

Suporta recursos no formato HTML XML, JSON, YAML,
TXT, etc.

Permite invocar serviços por meio da própria URI/URL.

Em geral, apresenta desempenho e escalabilidade maior, devido ao baixo overhead.
Permite fazer caching.

Requer menor largura de banda para trafegar os dados.

Suporta apenas SSL/TLS e HTTPS para incrementar a segurança.
JavaScript pode facilmente chamar REST.

Compreendidas essas diferenças, vamos ver agora outras características! Roy Fielding propôs seis restrições ou princípios que nós vamos ver em mais detalhes na tabela seguinte:
Responsabilidades devem ser separadas entre clientes e servidores. Isso permite que os componentes do cliente e do servidor evoluam de forma independente e, por sua vez, permite que o sistema seja escalável. Em outras palavras, busca-se separar a arquitetura e responsabilidades em dois ambientes.
STATELESS
(SEM ESTADO)

SISTEMA EM
CAMADAS

INTERFACE
UNIFORME

CÓDIGO SOB
DEMANDA

Dessa forma, o cliente não se preocupa com tarefas como a comunicação com banco de dados,
gerenciamento de cache, log, entre outros; e o contrário também é válido, o servidor não se preocupa com tarefas como interface, experiência do usuário, entre outros. Permitindo, assim,a evolução independente das duas arquiteturas.

A comunicação entre cliente e servidor deve ser stateless (isto é, sem guardar estado). Oservidor não precisa lembrar do estado do cliente. Em vez disso, os clientes devem incluirtodas as informações necessárias na requisição para que o servidor possa entendê-la e processá-la.
Em outras palavras, um mesmo cliente pode mandarvárias requisições para o servidor, porém cada uma delas deve ser independente, ou seja, toda requisição deve conter todas as informações necessárias para que o servidor consiga entendê-la e processá-la adequadamente(qualquer informação de estado deve ficar no cliente).

Múltiplas camadas hierárquicas, como gateways, firewalls e proxies podem existir entre o cliente e o servidor. As camadas podem ser adicionadas, modificadas, reordenadas, ou removidas de forma transparente para melhorar a escalabilidade - deve ser fácil, então,manipular camadas (tornando o sistema mais flexível).

Não é recomendado que o cliente chame diretamente o servidor sem antes passar por um intermediador como um Balanceador de Carga (Load Balancer). Isso garante que o cliente se preocupe apenas com a comunicação com o intermediador e o intermediadorfique responsável por distribuir as requisições aos servidores da melhor maneira possível.
Respostas do servidor devem ser declaradas como cacheable ou noncacheable. Isso permite que o cliente ou seus componentes intermediários armazenem em cache respostas e reutilizem-nas para pedidos posteriores. Isto reduz a carga no servidore ajuda a melhoraro desempenho.
Isso significa que, quando um primeiro cliente solicita um determinado recurso ao servidor, esse processa a requisição e o cliente a armazena temporariamente em cache. Quando houver uma nova requisição, a resposta armazenada já está pronta para ser utilizada e nem precisará ser recuperada novamente.
Todas as interações entre cliente, servidor e componentes intermediários são baseadas na uniformidade de suas interfaces. Isso simplifica a arquitetura geral, visto que componentes podem evoluir de forma independente à medida que implementem o que foi acordado em contrato.
É basicamente um contrato para comunicação entre cliente e servidor. São regras para fazer um componente o mais genérico possível, tornando-o muito mais fácil de ser refatorado e melhorado. Obedece a quatro princípios: identificação de recursos; representação de recursos;respostas auto-explicativas/descritivas; e hypermídia.

Esse princípio é opcional, na medida em que não faz parte da arquitetura em si. Ele trata da possibilidade de clientes poderem estender suas funcionalidades através do download e execução do código sob demanda. Exemplos incluem scripts Javascript, Applets Java,Silverlight, etc.

Em outras palavras, permite que o cliente possa executar algum código sob demanda, ou seja,
estender parte da lógica do servidor para o cliente, seja através de applets ou scripts. Assim,
diferentes clientes podem se comportar de maneiras específicas mesmo que utilizando exatamente os mesmos serviços providos pelo servidor.
Todas aplicações que siga essas restrições são consideradas Aplicações RESTful. Como vocês devem ter notado, essas restrições não ditam a tecnologia a ser utilizada para o desenvolvimento das aplicações. Em vez disso, a adesão a estas orientações e melhores práticas oferece a oportunidade de uma aplicação escalável, portátil, confiável e capaz de ter um desempenho melhor. Professor, aplicações RESTful são obrigadas a utilizar RESTcom HTTP? Não!
Na teoria, elas podem utilizar qualquer protocolo para transferência dos dados; na prática, elas utilizam HTTP em quase 100% das vezes. Por que? Porque há muitas vantagens em utilizar características e recursos desse protocolo como seus métodos/verbos: GET, POST, etc. Por falar nisso, 0 que é um recurso? Também chamado de Resource, é qualquer coisa que possa ser acessada ou manipulada (Ex: páginas, vídeos, imagens, documentos, impressoras, etc).
Também é importante compreender o que é URI (JJniform Resource Identifier)'. Trata-se de uma string (cadeia de caracteres) utilizada para identificar unicamente um recurso.Vocês já devem conhecera URL (Uniform Resource Locator)-trata-se de uma URI que-além de permitir identificar
-também indica como acessar um recurso (basta lembrar de endereços de sites). Recursos podem ser representados em JSON, HTML, XML, TXT, etc.
Vamos ver um exemplo: há um serviço web que-dado o nome de uma pessoa - ele informa os três países mais prováveis da origem da pessoa. Vamos testar com o nome: Romário.
HTTPS://API.NATIONALIZE.IO/?NAME=ROMARIO

{"name":"romario","country":[{"country_id":"BR","probability":0.5007485103753054},{"country_id"
:"NL","probability":0.15063534117504848},

{"country_id":"RU","probability":0.10129493121297602}]}

O resultado está no formato JSON (que é bem mais simples que XML). Vamos formatá-lo para melhorar sua visualização:
O resultado afirma que uma pessoa com nome Romário tem 50.0% de chance de ser do
Brasil (BR);
15.0% de chance de ser da Holanda (NL); e 10.1% de chance de ser da Rússia (RU).
Se testarmos com Klaus, retornará 28.9% de ser da Alemanha (DE); 27.2% de ser da Áustria (AT); e 25% de ser da
Dinamarca (DK). Se testarmos com Sato, retornará 97.2% de ser do Japão (JP); 1.5% de ser daTurquia (TR); e 0.006% de ser da Itália (IT).

Viram que eu coloquei o parâmetro na própria URL? Pois é, eu utilizei o Método GET do HTTP! Notem que eu não tive que acessar nenhum Repositório UDDI; eu não tive que usar nenhum envelope com cabeçalho, corpo, falhas, namespace, encoding, recursos adicionais de segurança - eu simplesmente utilizei diretamente os próprios recursos do HTTP para consumir um serviço web por meio do Paradigma REST. Mais simples, não?
E se eu quiser mandar um monte de informações de um formulário enorme no corpo de uma requisição em formato JSON que atualize um banco de dados em um servidor? Também é possível e eu posso fazer tudo isso pela própria URL utilizando o Método POST! Para finalizar, eu gostaria de destacar o porquê desse estilo arquitetural se chamar REST (RepresentationalState Transfer ou
Transferência de Estado Representacional).

Basicamente isso significa que essa tecnologia permite transferir (criar, recuperar,
alterar ou remover) o estado (também chamado de valor) de um recurso (qualquer objeto informacional)disponibilizado por um serviço web por meio de um formato de representação (Ex: JSON,
XML,
etc). Então, fechamos aqui a nossa aula... eu sei que se trata de um assunto complexo e técnico,mas vocês vão ver que os exercícios não são tão complicados. Vamos lá...

RESUMo

DEFINIÇÕES DE WEB SERVICES

Web Services tratam da disponibilização de um serviço pela internet que pode ser acessado em qualquer lugar.
Web Services são componentes de aplicativos baseados em XML, autocontidos e autodescritivos, que se comunicam usando protocolos abertos.
Web Services são uma interface que descreve uma coleção de operações que são acessíveis pela rede através de mensagens XML padronizadas.
Web Services tratam essencialmente da interoperabilidade entre programas e aplicações -
especialmente quando eles usam linguagens, ferramentas ou plataformas diferentes.
Web Services são um sistema de software projetado para permitir interoperabilidade na interação entre máquinas através de uma rede.
Web Services são componentes de software com baixo fator de acoplamento, utilizado por meio de padrões de internet.
Web Services representam uma função/lógica de negócio ou um serviço que pode ser acessado por uma outra aplicação na web, sobre redes públicas e, geralmente, disponibilizado por protocolos conhecidos.
Web Services são soluções utilizadas na integração de sistemas e na comunicação entre aplicações diferentes,permitindo que elas enviem e recebam dados.

CARACTERÍSTICA | DESCRIÇÃO

WEB SERVICES SÃO
AUTOCONTIDOS
WEB SERVICES SÃO
AUTODESCRITIVOS
WEB SERVICES UTILIZAM
PROTOCOLOS ABERTOS
WEB SERVICES SÃO FRACAMENTE

ACOPLADOS

WEB SERVICES SÃO
INDEPENDENTES DE TECNOLOGIA

Isso significa que eles não necessitam ou dependem de outros componentes para ter uma existência própria.
Isso significa que eles não necessitam de informações externas para expor suas funcionalidades.
Isso significa que os protocolos não são de propriedade de nenhuma organização, são apenas protocolos padrões da internet.
Isso significa que a interface do serviço pode mudar sem comprometer a capacidade do cliente de interagir com o serviço.
Isso significa que eles são independentes de plataforma, sistema operacional,
arquitetura de processador, linguagem de programação, entre outros.

PADRÕES | DESCRIÇÃO

SOAP (SIMPLE/SINGLE OBJECT

ACCESS PROTOCOLJ
WSDL (WEB SERVICES
DESCRIPTION LANGUAGEJ

UDDI (UNIVERSAL DESCRIPTION,
DISCOVERYANDINTEGRATIONJ

Baseado em XML, define uma organização para troca estruturada de dados entre
Web Services.

Baseado em XML, define como as interfaces dos Web Services podem ser representadas.
Baseado em XML, trata-se do padrão de descobrimento que define como as informações podem ser organizadas.
DEFINIÇÃO DE SOAP

Trata-se de uma das formas de comunicação para encapsular dados transferidos no formato XML para Web
Services.

Trata-se de um formato baseado em XML para intercâmbio de mensagens - é utilizado para realizar o encapsulamento e o transporte de dados.
Trata-se de um formato para envio e recebimento de mensagens independentemente de plataforma e tecnologia.
Trata-se de um protocolo baseado em XML que define uma organização para a troca estruturada de dados entre Web Services.
ELEMENTOS | SITUAÇÃO | DESCRIÇÃO

Trata-se do elemento-raiz do documento XML. Ele identifica o documento XML como

ENVELOPE
(ENVOLOPE)

CABEÇALHO
(HEADER]

CORPO
(BODY!

FALHA
(FAULT)

OBRIGATÓRIO

OPCIONAL

OBRIGATÓRIO

OPCIONAL

uma mensagem SOAP e funciona como um recipiente que contém os demais elementos da mensagem (Ex: Header e Body). Corresponde à descrição da mensagem e do que deve ser processado.
Trata-se do elemento que carrega informações adicionais específicas para a aplicação a fim de estender as funcionalidades das Mensagens SOAP. Desta forma, é possível adicionar novas funcionalidades como autenticação, criptografia, autorização,assinatura digital, etc. Podem ser definidos vários cabeçalhos.

Trata-se do elemento que contém a carga útil (payload) da Mensagem SOAP. É aqui que estão as informações propriamente ditas do serviço web remetidas ao destinatário final da mensagem, incluindo a chamada ao procedimento ou o retorno de seu resultado.
Trata-se do elemento contido no corpo responsável por relatar possíveis erros de envio ou processamento de mensagens, informando localização e formato dos erros encontrados. Quando estiver presente deve aparecer como um elemento filho do elemento Body.
DEFINIÇÃO DE WSDL

Trata-se de uma linguagem de descrição de web services, escrita em XML, para descrever serviços web,especificaras formas de acesso, as operações/métodos disponíveis.

Trata-se de uma linguagem para descrever serviços de rede como endpoints (ou portas)
que operam em mensagens que contêm informações orientadas à documento/procedimento.
Trata-se efetivamente de especificação que define como descrever serviços web em uma gramática XML.

Trata-se de um protocolo baseado em XML para troca de informações em ambientes distribuídos e descentralizados (sim, alguns autores o consideram também como um protocolo).
WSDL 1.1 WSDL 2.0

definitions types í message
L

portType operation input Houtput P—I

i s description types
Ü L

interface operation
| input H

| output 1—I

service

I Port !

TIPO | DEFINIÇÃO

ONE-WAY A operação pode receber uma requisição, mas não retornará uma resposta.

REQUEST-RESPONSE A operação pode receber uma requisição e retornará uma resposta.

SOLICIT-RESPONSE A operação pode enviar uma requisição e esperará por uma resposta.

NOTIFICATION A operação pode enviar uma mensagem, mas não esperará por uma resposta.

DEFINIÇÃO DE UDDI

Trata-se de um serviço de diretório, baseado em XML, em que é possível registrar e localizar Web
Services.

Trata-se de uma especificação técnica que tem como objetivo descrever, descobrir e integrar Web
Services.

Trata-se de um diretório/registro para armazenamento de informações sobre Web Services - é um repositório de interfaces de Web Services descritas por WSDL.
Trata-se de um protocolo que é um dos maiores blocos de construção requeridos para construir Web
Services com sucesso (Sim, alguns o chamam de protocolo!).
Trata-se de um padrão de descoberta que define como são organizadas as informações de descrição do serviço,permitindo que os solicitantes descubram os serviços.

Service
Provider

Service DescripMlloionn

Service Interface

Publish
Invoke/Bind

SOAP Request
WSDL

SOAP Response SOAP Request SOAP Response

>ervice Descriptior

SOAP Request

SOAP Response
WSDL

Service

(* Requester

Find

Service Registry

MÉTODO | DESCRIÇÃO
|

GET Esse método solicita a representação de um recurso específico. Requisições utilizando o métodoGET devem retornar apenas dados.

HEAD Esse método solicita uma resposta de forma idêntica ao método GET, porém sem conter o corpo da resposta.
PUT Esse método substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.
POST Esse método é utilizado para submeter uma entidade a um recurso específico,
frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor.
DELETE
TRACE
CONNECT
OPTIONS
PATCH

Esse método remove um recurso específico.

Esse método executa um teste de chamada loop-back junto com o caminho para o recurso de destino.
Esse método estabelece um túnel para o servidor identificado pelo recurso de destino.

Esse método é usado para descrever as opções de comunicação com o recurso de destino.
Esse método é utilizado para aplicar modificações parciais em um recurso.

SOAP

[SIMPLE OBJECT ACCESS PROTOCOLJ

REST
[REPRESENTATIONAL STATE TRANSFERI

É um protocolo de comunicação baseado em XML. É um estilo arquitetural ou de desenvolvimento independente de tecnologia.
Utiliza um Envelope enviado por geralmente por

HTTP para transmitir dados.

Utiliza diretamente recursos oferecidos de forma nativa, em regra, pelo HTTP.
Suporta somente recursos no formato XML. Suporta recursos no formato HTML XML,
JSON,

YAML, TXT, etc.

Permite invocar serviços por meio de Métodos RPC

(Remote Procedure Cal Is).
Em geral, apresenta desempenho e escalabilidade menor, devido ao alto overhead.
Não permite fazer caching.

Permite invocar serviços por meio da própria URI/URL.

Em geral, apresenta desempenho e escalabilidade maior, devido ao baixo overhead.
Permite fazer caching.

Requer maior largura de banda para trafegar os dados.Suporta recursos da WS-Security para incrementar a segurança.
JavaScript pode chamar SOAP, mas é de difícil de implementação.
Requer menor largura de banda para trafegar os dados.
Suporta apenas SSL/TLS e HTTPS para incrementara segurança.
JavaScript pode facilmente chamar REST.

RESTRIÇÃO OU

PRINCÍPIO

CLIENTE/SERVIDOR

STATELESS
(SEM ESTADO)

DESCRIÇÃO

Responsabilidades devem ser separadas entre clientes e servidores. Isso permite que os componentes do cliente e do servidor evoluam de forma independente e, por sua vez,permite que o sistema seja escalável. Em outras palavras, busca-se separar a arquitetura e responsabilidades em dois ambientes.
Dessa forma, o cliente não se preocupa com tarefas como a comunicação com banco de dados, gerenciamento de cache, log, entre outros; e o contrário também é válido, o servidor não se preocupa com tarefas como interface, experiência do usuário, entre outros.Permitindo, assim, a evolução independente das duas arquiteturas.

A comunicação entre cliente e servidor deve ser stateless (isto é, sem guardar estado). O
servidor não precisa lembrar do estado do cliente. Em vez disso, os clientes devem incluir todas as informações necessárias na requisição para que o servidor possa entendê-la e processá-la.
SISTEMA EM
CAMADAS

CACHE

INTERFACE
UNIFORME

CÓDIGO SOB
DEMANDA

Em outras palavras, um mesmo cliente pode mandar várias requisições para o servidor,
porém cada uma delas deve ser independente, ou seja, toda requisição deve contertodas as informações necessárias para que o servidor consiga entendê-la e processá-la adequadamente (qualquer informação de estado deve ficar no cliente).
Múltiplas camadas hierárquicas, como gateways, firewalls e proxies podem existir entre o cliente e o servidor. As camadas podem ser adicionadas, modificadas, reordenadas, ou removidas de forma transparente para melhorar a escalabilidade - deve ser fácil, então,manipular camadas (tornando o sistema mais flexível).

Não é recomendado que o cliente chame diretamente o servidor sem antes passar por um intermediadorcomo um Balanceador de Carga (Load Balancer). Isso garante que o cliente se preocupe apenas com a comunicação com o intermediador e o intermediador fique responsável por distribuir as requisições aos servidores da melhor maneira possível.
Respostas do servidor devem ser declaradas como cacheable ou noncacheable. Isso permite que o cliente ou seus componentes intermediários armazenem em cache respostas e reutilizem-nas para pedidos posteriores. Isto reduz a carga no servidor e ajuda a melhorar o desempenho.
Isso significa que, quando um primeiro cliente solicita um determinado recurso ao servidor,
esse processa a requisição e o cliente a armazena temporariamente em cache. Quando houver uma nova requisição, a resposta armazenada já está pronta para ser utilizada e nem precisará ser recuperada novamente.
Todas as interações entre cliente, servidor e componentes intermediários são baseadas na uniformidade de suas interfaces. Isso simplifica a arquitetura geral, visto que componentes podem evoluir de forma independente à medida que implementem o que foi acordado em contrato.
É basicamente um contrato para comunicação entre cliente e servidor. São regras para fazer um componente o mais genérico possível, tornando-o muito mais fácil de ser refatorado e melhorado. Obedece a quatro princípios: identificação de recursos; representação de recursos; respostas auto-explicativas; e hypermídia.
Esse princípio é opcional, na medida em que não faz parte da arquitetura em si. Ele trata da possibilidade de clientes poderem estender suas funcionalidades através do download e execução do código sob demanda. Exemplos incluem scripts Javascript, Applets Java,Silverlight, etc.

Em outras palavras, permite que o cliente possa executar algum código sob demanda, ou seja, estender parte da lógica do servidor para o cliente, seja através de applets ou scripts.Assim, diferentes clientes podem se comportar de maneiras específicas mesmo que utilizando exatamente os mesmos serviços providos pelo servidor.
H PARA MAIS DICAS: WWW.INSTA6RAM.COM/PROFESSORDIEGOCARVALHO

QUESTõES CoMENTADAS - CESPE

í. (CESPE / BANRISUL - 2022) Em um serviço RESTful, todos os métodos são identificados pela mesma URL, sendo cada método acionado por uma porta específica.
Comentários:

Opa! Em um serviço RESTful, cada método é identificado por uma URL diferente. Os métodos são acionados por um verbo HTTP específico, como GET, POST, PUT ou DELETE. E em regra,RESTful trata de URI e, não, URL.
Gabarito: Errado

2. (CESPE / TRT8 - 2022) Em uma API RESTful, cada solicitação deve conter todos os dados necessários ao seu atendimento para não depender de informações armazenadas em outras sessões, o que caracteriza uma restrição de:
a) cache.

b) arquitetura cliente-servidor.

c) interface uniforme.

d) sistema de camadas.

e) comunicação stateless.

Comentários:

STATELESS
(SEM ESTADO]

A comunicação entre cliente e servidor deve ser stateless (isto é, sem guardar estado). O
servidor não precisa lembrar do estado do cliente. Em vez disso, os clientes devem incluir todas as informações necessárias na requisição para que o servidor possa entendê-la e processá-la.
Em outras palavras, um mesmo cliente pode mandar várias requisições para o servidor, porém cada uma delas deve ser independente, ou seja, toda requisição deve contertodas as informações necessárias para que o servidor consiga entendê-la e processá-la adequadamente(qualquer informação de estado deve ficar no cliente).

Gabarito: Letra E

3. (CESPE / TRT8 2022) O método que serve para depuração em HTTP, ao instruir o servidor a enviar de volta a solicitação, é o:
a) options b) get c) trace d) connect e) post
Comentários:

MÉTODO | DESCRIÇÃO

GET Esse método solicita a representação de um recurso específico. Requisições utilizando o método
GET devem retornar apenas dados.

HEAD Esse método solicita uma resposta de forma idêntica ao método GET, porém sem conter o corpo da resposta.
PUT Esse método substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.
POST Esse método é utilizado para submeter uma entidade a um recurso específico,
frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor.
DELETE Esse método remove um recurso específico.

Esse método executa um teste de chamada loop-back por todo o caminho até o recurso alvo no qual foi destinado, provendo um mecanismo útil para depuração.
CONNECT Esse método estabelece um túnel para o servidor identificado pelo recurso de destino.OPTIONS Esse método é usado para descrever as opções de comunicação com o recurso de destino.PATCH Esse método é utilizado para aplicar modificações parciais em um recurso.
O método que serve para depuração em HTTP, ao instruir o servidor a enviar de volta a solicitação,é o Trace.

Gabarito: Letra C

4. (CESPE / FUNPRESP-EXE - 2022) SOAP (Simple Object Access Protocol) é um protocolo de comunicação usado para a troca de mensagens XML entre o cliente e o provedor de serviço.
Comentários:

Perfeito! Trata-se da definição do SOAP! O SOAP trata-se de um protocolo baseado em
XML que define uma organização para a troca estruturada de dados entre Web Services.
Gabarito: Correto

5. (CESPE / FUNPRESP-EXE - 2022) UDDI (Universal Description Discovery and
Integration) é um padrão utilizado em SOA para a criação de repositórios de descrição de serviços.
Comentários:

Perfeito! O UDDI trata-se de um diretório/registro para armazenamento de informações sobre WebServices - é um repositório de interfaces de Web Services descritas por WSDL. Em uma analogia,podemos dizer que o UDDI é como uma lista telefônica.

Gabarito: Correto

6. (CESPE / FUNPRESP-EXE - 2022) Um documento WSDL possui um conjunto de elementos de nós abstratos e concretos que especificam a localização de um serviço.
Comentários:

O WSDL é o documento que, resumidamente, descreve quais são as operações disponíveis em um serviço web com todas as particularidades de suas interfaces como métodos,parâmetros,
protocolos, entre outros. Além disso, o WSDL separa a descrição de um serviço em duas perspectivas: abstratas e concretas.
Gabarito: Correto

7. (CESPE / Petrobrás - 2022) Web service é um sistema de software projetado para suportar interação entre máquinas através de uma rede; esse sistema possui uma interface descrita em formato processável por máquina, especificamente o WSDL (web services descriptor language).
Comentários:

Perfeito! Conforme vimos em aula, Web Services são um sistema de software projetado para permitir interoperabilidade na interação entre máquinas através de uma rede. Além disso,o WSDL
(web services descriptor language), que é baseado em XML, define como as interfaces dos WebServices podem ser representadas.

Gabarito: Correto

8. (CESPE / Petrobrás - 2022) Uma das vantagens do SOAP é a sua utilização correta dos métodosHTML (PUT, GET, POST, DELETE), enquanto o REST utiliza apenas o método POST para realizar as requisições através de um arquivo XML.
Comentários:

Na verdade, tais métodos são do HTTP, e não do HTML. Além disso, o REST suporta diversas linguagens, como HTML, XML, JSON, YAML, já o SOAP suporta apenas o XML.
Gabarito: Errado

9. (CESPE / Petrobrás - 2022) Os protocolos SOAP e REST são os padrões mais utilizados na comunicação entre os sistemas por meio do web service; esses protocolos, unidos à estrutura básica XML, compõem a estrutura básica dos web services.
Comentários:

SOAP e REST são os padrões mais utilizados em web services, além disso eles são utilizados em conjunto com o XML. Porém, há uma pequena observação a ser realizada, SOAP é um protocolo de comunicação e o REST é um estilo arquitetural. Ao meu ver, o item deveria ter sido anulado.
Gabarito: Correto

10. (CESPE / DPE-RO - 2021) O REST emprega um protocolo universal, o HTTP, para oferecer um serviço web simples e aberto. Verbos HTTP são usados para realizar chamadas e indicar para o serviço que ação deve ser realizada. Assinale a opção que indica o verbo usado tipicamente para a atualização de um recurso existente:
a) PUT.

b) CREATED.

c) GET.

d) POST.

e) TRACE.

Comentários:

Os verbos (também chamados de métodos de requisição) são responsáveis por indicar a ação a ser executada para um dado recurso. O verbo utilizado para a atualização de um recurso é o PUT. Ele substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.
Gabarito: Letra A

A respeito de tecnologia de integração com RESTful, julgue os itens a seguir.

11. (CESPE / SERPRO - 2021) Webservices possibilitam tanto a recuperação do estado atual de um recurso quanto a exclusão do recurso.
Comentários:

REST significa Representational State Transfer (Transferência de Estado
Representacional). Isso significa que ele transfere (cria, recupera, altera ou remove) o estado(valores) de um recurso
(qualquer objeto informacional) por meio de um formato de representação (Ex: JSON, XML,
etc).
Logo, webservices RESTful realmente possibilitam tanto a recuperação do estado atual de um recurso quanto a exclusão do próprio recurso.
Gabarito: Correto i2.(CESPE / SERPRO - 2021) O protocolo de comunicação HTTP e a identificação de recursos podem ser utilizados por meio de URL (Uniform Resource Locator).
Comentários:

Vou respeitosamente discordar do gabarito preliminar dessa questão (Errado)! O
HTTP e a identificação de recursos podem ser utilizados por meio de URL? Sim! URI identifica um recurso; URLidentifica e informa qual protocolo permite acessá-lo. Logo, em relação a serviços web
RESTful,
pode-se utilizar apenas URL, URI + HTTP ou URL + HTTP.

Gabarito: Errado

13. (CESPE / SERPRO - 2021) As interações acontecem sem controle de estado, o que é conhecido como stateless.
Comentários:

A Web é o principal sistema que utiliza o modelo REST. Hoje ela suporta bilhões de clientes conectados e trocando informações. Agora como é possível a Web ter uma escalabilidade e performance tão boas, a ponto de conseguir suportar tamanho número de clientes sem problemas? Aresposta: Comunicação Stateless!

Requisições feitas por um cliente a um serviço REST devem conter todas as informações necessárias para que o servidor as interprete e as execute corretamente.Clientes não devem depender de dados previamente armazenados no servidor para processar uma requisição.Qualquer informação de estado deve ser mantida pelo cliente e não pelo servidor.

Isso reduz a necessidade de grandes quantidades de recursos físicos, como memória e disco, e também melhora a escalabilidade de um serviço REST. É justamente por essa característica que aWeb consegue ter uma escalabilidade praticamente infinita, pois ela não precisa manter as informações de estado de cada um dos clientes.
Gabarito: Correto i4.(CESPE / SERPRO - 2021) A arquitetura RESTful não possibilita o uso de servidores intermediários, chamados de balanceadores de carga, razão porque o cliente sempre se conecta ao servidor final.
Comentários:

Na verdade, é recomendado que-entre o cliente e o servidor-haja um balanceadorde carga
(Load
Balancer), responsável justamente por distribuir as requisições entre os servidores de alguma forma.
Gabarito: Errado i5.(CESPE/ MEC-2020) REST usa um modelo centrado em recursos de serviços encapsulados,em que cada recurso fornecido pelo serviço possui uma URL e todos os recursos oferecem suporte a uma interface uniforme.
Comentários:

Perfeito! É realmente centrado em recursos; os recursos possuem uma URL; e todos os recursos fornecem suporte a uma interface uniforme (URL - Uniform Resource Location).
Gabarito: Correto i6.(CESPE / SLU-DF - 2019) Um web service pode assumir o papel de provedor de serviço e de consumidor de serviço.
Comentários:

Perfeito! Um serviço web pode fazer o papel de provedor, fornecendo serviço para outra entidades ou de consumidor, consumindo serviço de outros serviços web.
Gabarito: Correto

17. (CESPE / SEFAZ-BA - 2019) Os web services são componentes de software na web que podem fornecer determinados serviços a aplicações criadas em diferentes linguagens. Podem usar o protocolo SOAP para transferência de mensagens em formato XML. Para descrever a estrutura destas mensagens geralmente utiliza-se:
a) REST.

b) WSDL.

c) CORBA.

d) RESTFUL.

e) HTML.

Comentários:

O padrão utilizado para descrever a estrutura de Mensagens SOAP é o WSDL.

Gabarito: Letra B

i8.(CESPE ITRT-CE - 2019) Assinale a opção que apresenta o método HTTP que deve ser usado para a busca de recursos por meio do web service RESTful.
a) delete b) get c) put d) options
Comentários:

O Método HTTP que permite buscar recursos é o GET.

Gabarito: Letra B

ig.(CESPE / BNB - 2018) SOAP utiliza um sistema de mensagens SMTP sobre a camada de transporte.
Comentários:

SOAP até pode utilizar SMTP, mas não é sobre a camada de transporte - é sobre a camada de aplicação.
Gabarito: Errado

2O.(CESPE / MPE-PI - 2018) Para implementar um web service de baixo overhead que tenha recursos identificáveis e localizáveis por meio de uma URI (Uniform ResourceIdentifier)
mediante o protocolo HTTP, pode-se utilizar o REST (Representational State Transfer).

Comentários:

Perfeito! Não tem nem o que acrescentar...

Gabarito: Correto

2i.(CESPE / STJ - 2018) Web service é uma solução utilizada na integração de sistemas e na comunicação entre aplicações diferentes.
Comentários:

Perfeito! Ele realmente permite integrar sistemas e realizar a comunicação entre aplicações.

Gabarito: Correto

22.(CESPE / STJ -2018) Os serviços Web RESTful utilizam o HTTP como um meio de comunicação entre cliente e servidor.
Comentários:

Perfeito! Eles utilizam os métodos do HTTP como uma forma de realizar a comunicação entre um cliente e um servidor.
Gabarito: Correto

23.(CESPE / STJ - 2018) A REST define uma arquitetura cliente-servidor na qual o servidor não mantém contexto de cliente entre transações, ou seja, é stateless e toda transação contém as informações necessárias para satisfazer a solicitação.
Comentários:

Perfeito! É stateless, logo não guarda o estado da transação.

Gabarito: Correto
2ZJ.(CESPE / STM - 2018) O SOAP é um tipo de modelo de dados XML elaborado para facilitar a inserção de campos HTML em páginas web.
Comentários:

Não tem nenhuma relação com a inserção de campos HTML em páginas web - ele é utilizado para a troca de mensagens entre aplicações distribuídas.
Gabarito: Errado

25. (CESPE / SEDF - 2017) Serviços expressos por meio de contratos web services têm o potencial de evitar completamente a transformação, objetivo-chave dos contratos de serviços padronizados.
Comentários:

Galera, essa questão afirma que, quando eu ofereço serviços por meio de Web Services e seus contratos (isto é, suas interfaces), eu tenho um grande potencial de evitar a transformação. Isso é verdade! Nós sabemos que mudar a implementação do serviço é irrelevante desde que se mantenha sua interface. No entanto, eventualmente eu posso precisar alterar a interface de um serviço - e, nesse caso, não dá para evitar a transformação do contrato do serviço.
Logo, o contrato não é imutável, deve-se realmente evitar modificá-lo, mas ele não é imune a mudanças e não evita completamente transformações. No entanto, a questão afirma que o uso de contratos tem o "potencial" de evitar completamente a transformação. Ter o potencial significa ter a capacidade de realização ou execução de algo, e isso é verdadeiro nesse contexto.Vejam o que diz a especificação:
"Regardless ofthe development approach you utilize for service development there is no question that service contracts must be designed in an extensible manner to minimize disruptive versioning changes.Service contracts should be designed with the assumption that once published,
they cannot be modified—this approach forces developers to buildflexibilityinto their schema designs".
Gabarito: Correto

26.(CESPE / TRE-BA - 2017) No que se refere a web services, assinale a opção correta.

a) As solicitações e respostas XML trafegam no protocolo HTTP, não sendo possível utilizá-las nos protocolos FTP e SMTP.
b) Um dos componentes de um Web Service SOAP (Simple Object Access Protocol) é a UDDI
(Universal Description, Discovery and Integration), a qual é um arquivo do tipo XML que descreve detalhadamente um Web Service, especificando como deve ser o formato de entrada e saída de cada operação.
c) As duas formas de envio de mensagem para que um cliente possa efetuar solicitações a umWeb Service são One-Way Messaging e Request-Response Messaging.

d) O WSDL (Web Services Description Language) é uma linguagem para o desenvolvimento de
Web Services similar ao XML.

e) Os Web Services permitem a integração de sistemas, todavia dependem da linguagem de programação sob a qual tenham sido desenvolvidos e do sistema operacional do computador onde esses sistemas forem executados.
Comentários:

(a) Errado, é possível utilizar FTP e SMTP; (b) Errado, quem descreve detalhadamente é o WSDL;
(c) Correto, existem quatro tipos de operação e essas duas constam delas; (d) Errado,
não é para desenvolvimento - é para descrição de Web Services; (e) Errado, eles são independentes de tecnologia, logo não dependem de linguagem de programação ou sistema operacional.
Gabarito: Letra C

27. (CESPE / TRE-PE - 2017) REST (Representational State Transfer) é:

a) um estilo de desenvolvimento que utiliza o protocolo HTTP e se baseia na interação simples entre cliente e servidor.
b) um software de infraestrutura em um sistema distribuído que auxilia no gerenciamento de interações entre entidades distribuídas em serviços web.
c) uma linguagem web voltada a definição de predicados que se apliquem a classes de objetos e de interações em um modelo UML.
d) uma linguagem de programação com tipos dinâmicos, voltada principalmente para desenvolvimento de aplicações web.
e) um modelo de desenvolvimento de software estruturado e organizado como um conjunto de classes de objeto e de relações entre essas classes.
Comentários:

(a) Correto; (b) Errado, não é um software de infraestrutura; (c) Errado, não é uma linguagem web;
(d) Errado, não é uma linguagem de programação; (e) Erraod, não tem nenhuma relação com modelos estruturados ou classes de objetos.
Gabarito: Letra A

28.(CESPE / MEC - 2016) A respeito dos conceitos de web services e REST, assinale a opção correta.
a) O método POST é utilizado na atualização de um recurso existente.

b) Pode-se utilizar qualquer meio de transporte existente para o envio de uma requisição,incluindo HTTP, SMTP e TCP.

c) O modelo REST impõe restrições ao formato da mensagem.

d) Ao desenvolver uma aplicação, o recurso é transferido pela rede.

e) As chamadas às URIs (uniform resource indicator) são feitas por meio de métodos
HTTP, os quais indicam para o serviço a ação a ser realizada com o recurso.
Comentários:

(a) Errado, esse seria o PUT; (b) Errado, TCP não pode ser utilizado; (c) Errado, não há restrições ao formato da mensagem; (d) Errado, essa frase sequer faz sentido; (e) Correto.
Gabarito: Letra E

2g.(CESPE / TRE-MT - 2016) Acerca de REST (representational state transfer), assinale a opção correta.
a) O protocolo REST utiliza SOAP e XML.

b) REST utiliza recurso não identificável baseado em PUT e GET.

c) REST pode ser utilizado para implementar WebServices de baixo overhead.

d) Embora opcionalmente, um recurso REST pode conter uma URI.

e) REST consiste em um estilo de desenvolvimento baseado em complexa interação cliente/servidor.
Comentários:

(a) Errado, ele não é um protocolo e não utiliza SOAP; (b) Errado, ele só utiliza recurso identificável por meio de URI; (c) Correto; (d) Errado, é obrigatório; (e) Errado, não é uma interação complexa, é uma interação simples.
Gabarito: Letra C

3O.(CESPE/ TCE-PA - 2016) Os web services devem ser projetados para ser utilizados independentemente de paradigmas de programação.
Comentários:

Perfeito! Eles são independentes de tecnologia...

Gabarito: Correto

3i.(CESPE/ TCE-PA - 2016) Para que um web service funcione corretamente, os softwares cliente/servidor devem ser escritos na mesma linguagem.
Comentários:

Na verdade, independe de tecnologias - inclusindo as linguagens de programação.

Gabarito: Errado

32. (CESPE/ TCE-PA - 2016) Ao se usar o protocolo SOAP (Simple Object Access
Protocol), cada solicitação e cada resposta são colocadas em um envelope SOAP, nos momentos de invocação e retorno de um web service, respectivamente.
Comentários:

Perfeito! Toda requisição e toda resposta trafega encapsulada em um Envelope SOAP.

Gabarito: Correto

33. (CESPE / MEC - 2015) Entre as restrições da REST está a interface uniforme, a qual requer que um serviço ofereça várias operações e aguarde a solicitação dessas operações pelo servidor.
Comentários:

A questão não trata da restrição de Interface Uniforme - acredito que a restrição que mais se aproxima dessa descrição seja o Sistema em Camadas.
Gabarito: Errado

34. (CESPE / MEC-2015) Afim de implementar serviços em REST, recomenda-se utilizar os
WSDL
já existentes com mínima alteração do cabeçalho, informando somente que o protocolo a ser utilizado é o REST.
Comentários:

REST não utiliza WSDL! Essa é uma tecnologia de Web Services SOAP.

Gabarito: Errado

35. (CESPE / MEC-2015) As principais características do REST (Representationl State
Transfer) são interface uniforme, stateless e cache.
Comentários:

Perfeito! Essas são três características/restrições do REST.

Gabarito: Correto

36.(CESPE/ MEC - 2015) Em uma web service, a linguagem de implementação e a plataforma utilizada são relevantes para os clientes.
Comentários:

Na verdade, é independe de tecnologia - logo a linguagem de implementação e a plataforma são irrelevantes para os clientes.
Gabarito: Errado

37. (CESPE / ANTAQ - 2014) Em arquiteturas REST, nenhum contexto de cliente pode ser mantido em servidor.
Comentários:

REST é statless (sem estado), isto é, o servidor não guarda o estado/conteto do cliente.

Gabarito: Correto

38.(CESPE / ANATEL - 2014) REST é uma técnica de engenharia de software para sistemas hipermídia distribuídos. De acordo com essa técnica, o estado da informação deve ser mantido no cliente, e o servidor não deve guardar o estado da comunicação de nenhum cliente que se comunique com o servidor, além de uma única requisição.
Comentários:

De fato, ele é utilizado no desenvolvimento de sistemas hipermídia distribuídos. Por outro lado, o servidor não precisa lembrar o estado do cliente. Em vez disso, os clientes devem incluir todas as informações necessárias na requisição para que o servidor possa entendê-la e processá-la. Dentro de um mesmo contexto de conexão, não existe mais de uma requisição HTTP,isto é, cada requisição HTTP é única e não reflete estado no servidor.
Gabarito: Correto

39.(CESPE / CNJ - 2013) Uma das formas de comunicação para encapsular dados transferidos no formato XML para aplicações serviço web (Webservice) é o SOAP (Simple ObjectAccess
Protocol).

Comentários:

Perfeito! Ele realmente é uma forma de comunicação - dado que é um protocolo - para encapsular dados transferidos no formato XML para aplicações web services.
Gabarito: Correto

40.(CESPE / CNJ - 2013) A linguagem WSDL é utilizada para descrever web services limitadas ao tipo request-response.
Comentários:

TIPO | DEFINIÇÃO

ONE-WAY A operação pode receber uma requisição, mas não retornará uma resposta.

REQUEST-RESPONSE A operação pode receber uma requisição e retornará uma resposta.

SOLICIT-RESPONSE A operação pode enviar uma requisição e esperará por uma resposta.

NOTIFICATION A operação pode enviar uma mensagem, mas não esperará por uma resposta.

Não está limitada ao tipo request-response- existem quatro tipos diferentes de operações.

Gabarito: Errado

4i.(CESPE / CNJ - 2013) Nos registros de negócio UDDI, a descrição da forma de acesso aos web services é um procedimento contido nas páginas verdes (green pages).
Comentários:

As páginas verdes contêm descrições técnicas sobre as formas de acesso aos web services. Elas são utilizadas para indicar os serviços oferecidos por cada negócio, incluindo todas as informações técnicas envolvidas na interação e acesso ao serviço. Em geral, essas informações incluem uma referência para uma especificação externa e um endereço para invocar o serviço.
Gabarito: Correto

42.(CESPE / CNJ - 2013) Um dos elementos de uma mensagem SOAP é o corpo (body), no qual devem estar contidas as informações de erro e status.
Comentários:

Questão polêmica! Um dos elementos realmente é o Body e as informações de erro e status ficam localizadas dentro do Fault. No entanto, o Fault fica contido dentro doBody. Logo, por transitividade, as informações de erro e status ficam contidas no Body. Eu não vejo nenhum erro nessa questão, mas a banca a considerou errada.
Gabarito: Errado

43.(CESPE / ANTT - 2013) Web Services provêm um meio padrão para interoperação entre diferentes aplicativos de software, que podem ser executados em uma variedade de plataformas e(ou) frameworks.
Comentários:

Perfeito! Web Services são independentes de plataforma, sistema operacional,
arquitetura de processador, linguagem de programação, entre outros.
Gabarito: Correto

44.(CESPE / TCE-RO - 2013) O SOAP permite a troca de mensagens estruturadas em ambiente distribuído e descentralizado, com o uso de tecnologias XML. Essas mensagens podem ser trocadas por uma variedade de protocolos subjacentes como, por exemplo, o HTTP.
Comentários:

Perfeito! SOAP é um protocolo projetado para invocar aplicações remotas em um ambiente independente de plataforma, linguagem de programação, entre outros.Ele garante a interoperabilidade e intercomunicação entre diferentes sistemas, através da utilização de uma linguagem (XML) e de um mecanismo de transferência de dados que, geralmente, é o HTTP.
Gabarito: Correto

45.(CESPE / SERPRO - 2013) A comunicação entre sistemas clientes e servidores para troca de mensagens pode ser realizada por meio de SOAP (Simple Object Access Protocol), que é um protocolo para troca de informações estruturadas independente de linguagem de programação.
Comentários:

Perfeito! SOAP é um protocolo projetado para invocar aplicações remotas em um ambiente independente de plataforma, linguagem de programação, entre outros.
Gabarito: Correto

46.(CESPE / CNJ - 2013) Uma das formas de comunicação para encapsular dados transferidos no formato XML para aplicações serviço web (webservice) é o SOAP (Simple ObjectAccess
Protocol).

Comentários:

Perfeito! SOAP é uma das formas de comunicação para encapsular dados transferidos no formatoXML para Web Services.

Gabarito: Correto

47.(CESPE / TRE-MS - 2013) O WS-Security propõe uma série de extensões para aprimorar a segurança dos web services no UDDI e no WSDL. Por questão de compatibilidade, essas extensões não afetam os cabeçalhos do envelope SOAP.
Comentários:

Na verdade, ele propõe extensões para aprimorar a segurança dos Web Services no SOAP!
Além disso, ele afeta os cabeçalhos do envelope porque é justamente no cabeçalho que eles são especificados.
Gabarito: Errado

48.(CESPE / BACEN - 2013) O estilo arquitetural REST define um conjunto de restrições para uma aplicação, como, por exemplo, utilização de arquitetura par-a-par, manutenção de informações de estado, não uso de cache no cliente e apresentação de uma interface uniforme.
Comentários:

A questão deu três chances para acertá-la. As restrições são: utilização de uma arquiteturaCliente/Servidor (e, não, Par-a-Par); não manutenção de informações de estado, isto é,
Stateless; e utilização de cache no cliente (Cacheable).
Gabarito: Errado

49. (CESPE / SERPRO - 2013) Um web service pode ocorrer sobre o HTTP (Hypertext
Transfer
Protocol), utilizando-se os serviços RESTfull (Representational State Transfer).

Comentários:

Perfeito! Um Web Service pode ocorrer sobre HTTP, utilizando os serviços RESTful. No entanto,essa questão foi anulado sob a seguinte justificativa:

"Houve prejuízo do julgamento objetivo do item, pois, onde se lê ''RESTfull" deveria ler-se ''RESTful".Dessa forma, opta-se pela anulação do item."

Gabarito: Anulada

50.(CESPE / STF - 2013) A REST (Representational State Transfer), protocolo de comunicação embasado em XML, permite a comunicação de mensagens entre aplicações por meio de qualquer protocolo de comunicação em rede. Normalmente, esse protocolo é utilizado na integração de sistemas legados.
Comentários:

REST não é um protocolo e não é embasado em XML.

Gabarito: Errado

51. (CESPE / MPU - 2013) Web services é um método de comunicação entre serviços na
Web que aderem estritamente ao XML, como é o caso de serviços cuja comunicação é baseada na interface da arquitetura REST.
Comentários:

O REST não adere estritamente o XML - SOAP, sim!

Gabarito: Errado

52. (CESPE / PEFOCE - 2012) SOAP é um protocolo leve destinado à troca de informações estruturadas em um ambiente distribuído e descentralizado. Uma mensagem SOAP,por exemplo, é um documento XML composto de três partes obrigatórias: envelope, cabeçalho e corpo.
Comentários:

SOAP é um protocolo pesado e, não, leve -justamente por conta do overhead causado pelos seus elementos (envelope, cabeçalho, corpo, etc).
Gabarito: Errado

53. (CESPE / MPE-PI - 2012) Em web services, utiliza-se o protocolo SOAP (Simple
Object Access
Protocol) para a comunicação entre os serviços.

Comentários:

Perfeito! SOAP é uma das formas de comunicação para encapsular dados transferidos no formatoXML para Web Services.

Gabarito: Correto

54-(CESPE / TJ-RO - 2012) Representational state transfer (REST), que utiliza o WSDL como linguagem de descrição de serviços, é uma forma de implementação de SOA na web.
Comentários:

REST não utiliza WSDL!

Gabarito: Errado

55.(CESPE / MEC - 2011) O UDDI (Universal Description Discovery and
Integration), que corresponde a um registro de web services, é dividido em páginas brancas, amarelas e verdes,nas quais são prestadas aos clientes informações sobre a empresa, os serviços porela oferecidos e as especificações WSDL desses serviços.
Comentários:

VM50 i
SZXÓtJc I

III1 USI) L I1

cowros

^l I LIAoMLS I
J

Perfeito! As informações capturadas no contexto do UDDI são classificadas em três categorias principais: Páginas Brancas, Páginas Verdes ou Páginas Amarelas.
Gabarito: Correto

56.(CESPE / PREVIC - 2011) No WSDL (Web Services Definition Language), é prescrito o leiaute de banco de dados com descrições de serviços, por meio das quais os clientes de web service podem procurar serviços relevantes.
Comentários:

WSDL é Web Service Description Language e, não, Web Services Definition Lanquagel Além disso, ele não prescreve leiaute de banco de dados.
Gabarito: Errado

57.(CESPE / PREVIC-2011) Web Services são sistemas embasados na Web que oferecem serviços gerais para aplicações remotas, não requerendo interações imediatas de usuários finais.
Comentários:

De fato, há implementações de Web Services que tratam da interação máquina-máquina ou aplicação-aplicação - sem a obrigatoriedade de interferência humana.
Gabarito: Correto

58.(CESPE / MEC - 2011) Em formulários HTML, apenas o método post é suportado; o método get é utilizado em aplicações JavaScript.
Comentários:

Formulários geralmente utilizam POST, mas nada impede que se utilize GET (apenas os dados serão enviados de forma visível pela URL).
Gabarito: Errado

59.(CESPE / MEC-2011) Um web service pode ser desenvolvido, também, com o uso de
REST, que utiliza o protocolo HTTP para comunicação entre emissor e destinatário, e oSOAP, para encapsular as mensagens trafegadas.
Comentários:

Redação esquisita! Um serviço web realmente pode ser desenvolvido com o uso de REST
(que utiliza HTTP) ou SOAP (que encapsula as mensagens trafegadas). No entanto, não pode utilizar ambos.
Gabarito: Errado

6o.(CESPE / MPU - 2010) REST (Representationals State Transfer) é uma tecnologia que está sendo utilizada em web services, como substituta das tecnologias SOAP (Simple ObjectAccess
Protocol) e WSDL.

Comentários:

Não está sendo utilizada como substituta - cada uma é adequada a um contexto específico.

Gabarito: Errado

61. (CESPE / TCU - 2010) Uma equipe de desenvolvimento de software recebeu a incumbência de desenvolver um sistema com as características apresentadas a seguir.
- O sistema deverá ser integrado, interoperável, portável e seguro.

- O sistema deverá apoiar tanto 0 processamento online, quanto 0 suporte a decisão e gestão de conteúdos.
- O sistema deverá ser embasado na plataforma JEE (Java enterprise edition) v.6,
envolvendo servlets, JSP (Java server pages), Ajax, JSF (Java server faces) 2.0, Hibernate 3.5,SOA e web services.
O líder da equipe iniciou, então, um extenso processo de coleta de dados com o objetivo de identificar as condições limitantes da solução a ser desenvolvida e tomar decisões arquiteturais e tecnológicas que impactarão várias características funcionais e não funcionais do sistema, ao longo de seu ciclo de vida. A partir dessa coleta, o líder deverá apresentar à equipe um conjunto de informações e de decisões.
Com relação às diferentes arquiteturas e tecnologias que, se escolhidas,
impactarão as características do sistema descrito no texto, julgue o item:
O estilo de arquitetura de software denominado REST (Representational State
Transfer)
demanda mais recursos computacionais que o modelo de desenvolvimento de sistemas embasado em SOAP (Single Object Access Protocol), por isso não é recomendável a adoção do padrão REST de arquitetura de software no desenvolvimento do sistema em questão.
Comentários:

REST tem um overhead bem menor que o SOAP, demandando menos recursos computacionais.

Gabarito: Errado

62.(CESPE / MPU - 2010) A descrição de um web service é feita utilizando-se WSDL
(Web Services
Description Language), que é uma linguagem embasada em RPC (Remote Procedure Call) e
UDDI (Universal Description Discovery and Integration), com a qual se descreve a forma de acesso dos serviços e seus parâmetros de entrada e de saída.
Comentários:

Vamos reescrever a questão: descrição de um web service é feita utilizando-se
WSDL (Web
Services Description Language), que é uma linguagem embasada em XML RPC (Remote
Procedure
Call) e UDDI (Universal Description Discovery and Integration), com a qual se descreve a forma de acesso dos serviços e seus parâmetros de entrada e de saída.
Gabarito: Errado

63-(CESPE /TRE-MT -2010) Com relação a web services, assinale a opção correta.

a) As arquiteturas de aplicação de web services são arquiteturas firmemente acopladas,
nas quais as ligações entre serviços não podem mudar durante a execução.
b) SOAP (Simple Object Access Protocol) é um protocolo com base em HTML que permite troca de informações entre aplicações em um ambiente distribuído.
c) UDDI (Universal Description, Discovery and Integration) é um diretório para armazenamento de informações a respeito de web sevices. Essas informações são descritas em SOAP.
d) A linguagem WSDL (Web Services Description Language) é utilizada para descrever web services.
e) Segundo o W3C (World Wide Web Consortium), web services são apropriados somente para aplicações em que componentes de um sistema distribuído são executados em plataformas semelhantes de um mesmo fornecedor.
Comentários:

(a) Errado, são fracamente acopladas; (b) Errado, é baseado em XML e, não, HTML; (c)
Errado, são descritas em WSDL; (d) Correto; (e) Errado, eles são independente de tecnologias(plataformas,
hardware, etc).

Gabarito: Letra D

64.CESPE / ANATEL - 2009) Os três padrões fundamentais que possibilitam comunicações entre web services são: Simple Object Access Protocol (SOAP) — protocolo que define uma organização para a troca estruturada de dados entre web services; Web ServicesDescription
Language (WSDL) — protocolo que define como as interfaces dos Web Services podem ser representadas; Universal Description, Discovery And Integration (UDDI) —padrão de descoberta que define como são organizadas as informações de descrição do serviço,permitindo que os solicitantes descubram os serviços. Um desses padrões não utiliza a
XML
(Extensible Mark-up Language).

Comentários:

Na verdade, todos esses padrões se baseiam em XML!

Gabarito: Errado

6s.(CESPE / CEHAP-PB - 2009) São padrões de Web Services o SOAP, o WSDL e o UDDI,
todos baseados em HTTP.
Comentários:

Na verdade, todos são baseados em XML e, não, HTTP!

Gabarito: Errado

66. (CESPE / INMETRO - 2009) Na SOA, a descrição do serviço é mantida em um repositórioWSDL, em formato UDDI (Universal Description, Discovery and Integration).

Comentários:

SOA (Service Oriented Architecture) é uma arquitetura orientada a serviços!
Nesse contexto, a descrição do serviço é mantida em um repositório WSDL UDDI, em formato UDDI WSDL.
Gabarito: Errado

67.(CESPE / ANTAQ - 2009) Nos serviços web, clientes e servidores, direta ou indiretamente,podem acessar documentos UDDI completos por meio de seus URIs (Uniform
Resource
Identifier), usando um serviço de diretório, tal como o WSDL.

Comentários:

Nos serviços web, clientes e servidores, direta ou indiretamente, podem acessar documentos UDDIWSDL completos por meio de seus URIs (Uniform Resource Identifier), usando um serviço de diretório, tal como o WSDL UDDI.
Gabarito: Errado

68. (CESPE / ANTAQ - 2009) Um componente importante da arquitetura de serviços web é formado por um serviço de diretório que armazena descrições de serviços. Esse serviço deve obedecer ao padrão UDDI (Universal Description, Discovery And Integration).
Comentários:

Perfeito! O Padrão UDDI define o serviço de diretório que armazena descrições de serviços.

Gabarito: Correto

69. (CESPE / ANTAQ - 2009) Em serviços web, o SOAP pode ser transportado por protocolos como REST, HTTP, SMTP e JMS.
Comentários:

Essa questão foi anulada! REST não é um protocolo, mas um estilo arquitetural!
Inclusive, ele utiliza o Protocolo HTTP.
Gabarito: Anulada

7O.(CESPE / TRT-BA - 2008) O UDDI é uma especificação técnica que tem como objetivo descrever, descobrir e integrar web services; é embasado na tecnologia XML, que fornece uma plataforma neutra de dados e permite descrever relações hierárquicas de modo natural.
Comentários:

Basta lembrar da sigla: Universal Description, Discovery and Integration (Integração,
Descoberta e
Descrição Universal). Dessa forma, trata-se realmente de uma especificação técnica que tem como objetivo descrever, descobrir e integrar Web Services. É baseada em XML? Sim! Permite descrever relações hierárquicas? Sim!
Gabarito: Correto

7i.(CESPE / STJ - 2008) O serviço UDDI fornece uma interface para publicar e atualizar informações acerca de serviços web; possibilita pesquisar descrições WSDL pelo nome;provê uma interface que possibilita executar consultas de modo a recuperar uma entidade que corresponda a uma chave ou recuperar entidades que correspondam a um conjunto de critérios de busca.
Comentários:

O padrão UDDI versão 2.0 especifica duas interfaces com diversos métodos/operações para consumidores e provedores de serviços interagirem. Os consumidores de serviço usam aInterface de Consulta (Inquiry) para localizar e consultar um serviço, e os provedores de serviço usam aInterface de Publicação (Publisher) para publicar e atualizar um serviço.

Gabarito: Correto

72.(CESPE / STJ - 2008) O WSDL separa a parte abstrata de uma descrição de serviço da parte concreta; nessa descrição, a parte concreta contém as definições de tipos usados pelo serviço e a parte abstrata especifica como e onde o serviço pode ser contatado. Os documentosWSDL
podem ser acessados via um serviço de diretório como o UDDI; as definições WSDL podem ser geradas a partir de definições de interfaces escritas em outras linguagens.
Comentários:

A questão inverteu as bolas: as definições de tipo pertencem à parte abstrata; e como/onde o serviço pode ser contatado (endereço de rede, portas, etc) pertence à parte concreta.Alguns me perguntam se as definições WSDL podem ser geradas a partir de definições de interfaces escritas em outras linguagens. Em teoria, elas podem ser escritas em outras linguagens que, não, XML.
Gabarito: Errado

73.(CESPE / STJ - 2008) O SOAP encapsula mensagens que podem ser transmitidas via
HTTP;
permite o modelo de interação cliente-servidor; define como usar XML para representar mensagens de requisição e resposta. Um documento XML é transportado no corpo de uma mensagem SOAP; no modelo cliente-servidor, o corpo de uma mensagem SOAP pode conter uma requisição, mas não uma resposta.
Comentários:

SOAP encapsula mensagens que podem ser transmitidas via HTTP? Sim, assim como outros protocolos de comunicação. Permite 0 modelo de interação cliente-servidor? Define como usar XMLpara representar mensagens de requisição e resposta? Sim, utiliza um paradigma de requisição/resposta, típico de aplicações cliente-servidor. Um documento XML é transportado no corpo de uma mensagem SOAP? Sim, ele é encapsulado por uma Mensagem SOAP. O corpo de uma mensagem SOAP pode conter uma requisição, mas não uma resposta? Não, ele pode conter tanto uma requisição quanto uma resposta.
Gabarito: Errado

74. (CESPE / MPE-AM - 2008) No protocolo HTTP (Hypertext Transfer Protocol), o método
GET é utilizado em solicitações enviadas pelo servidor ao navegador para que este solicite dados ao usuário de uma página ou para que o próprio navegador forneça os dados solicitados.
Comentários:

A questão bagunçou tudo! O método GET é utilizado em solicitações enviadas pelo navegador ao servidor para solicitar dados de uma página ou para que o próprio servidor forneça os dados solicitados.
Gabarito: Errado

QUESTõES CoMENTADAS - FCC

í. (FCC / AL-MS - 2016) Considere o texto abaixo:

Atualmente muitos desenvolvedores têm exposto seus serviços utilizando uma abordagem que usa um padrão de URI, fazendo chamadas para um serviço web utilizando, por exemplo:http://www.empresa.com.br/programa/metodo?parâmetros=xxx Esta abordagem é adequada para ser utilizada em situações nas quais há limitação de recursos e de largura de banda,necessitando de uma estrutura de retorno em qualquer formato definido pelo desenvolvedor e suportada por qualquer navegador. Usa 0 padrão de chamadas GET, PUT, POST e DELETE e pode usar também objetos XMLHttpRequest que a maioria dos navegadores modernos suporta.
O texto trata especificamente de a) ESB.
b) SOAP.

c) REST.

d) SOA.

e) CORBA.

Comentários:

Quem usa o padrão de chamadas do Protocolo HTTP é o REST.

Gabarito: Letra C

2. (FCC / CM-SP - 2014) Pela sua simplicidade e facilidade de entendimento,
praticamente qualquer cliente ou servidor com suporte aos protocolos ...I pode fazer uso do REST. Uma de suas principais vantagens é 0 aproveitamento da infraestrutura web existente, mas a baixa segurança é seu principal ponto fraco. Em situações em que não se faz necessária alta padronização e alta segurança essa tecnologia funciona bem. Os web services RESTful expõem recursos para seus clientes, que são identificados através de ...II... . A manipulação dos recursos se dá através de operações básicas como ...III
As lacunas I, II e III são, correta e respectivamente, preenchidas por:

a) TCP/IP - caches - PUT, GET, POST e DELETE

b) XML/JSON/RSS/Atom - URIs - CRUD stateless: Create, Read, Update, Delete c) HTTP/HTTPS - URIs - PUT, GET, POST e DELETE
d) XML/JSON/RSS/Atom - URLs - CRUD stateless: Create, Read, Update, Delete e) HTTP/HTTPS - caches - CRUD stateless: Create, Read, Update, Delete
Comentários:

Pela sua simplicidade e facilidade de entendimento, praticamente qualquer cliente ou servidor com suporte aos protocolos HTTP/HTTPS pode fazer uso do REST. Os web services RESTful expõem recursos para seus clientes, que são identificados através de URIs. A manipulação dos recursos se dá através de operações básicas como PUT, GET, POST, DELETE.
Gabarito: Correto

3. (FCC / AL-SP - 2010) GET e POST são alguns dos principais métodos que determinam o que o servidor deve fazer com o URLfornecido no momento da requisição de um recurso.Relacionado a esses métodos, considere:
I. Dados enviados em uma requisição utilizando o método GET ficam visíveis na linha de endereço do navegador.
II. Se não for especificado um método, o POST é adotado como padrão.

III. O método GET é geralmente utilizado para enviar grandes quantidades de dados por meio de um formulário.
IV. O método POST não exibe os dados enviados na linha de endereço do navegador.

Está correto o que se afirma APENAS em:

a) I e II.

b) I e IV.

c) II, III e IV.

d) III.

e) IV.

Comentários:

(I) Correto; (II) Errado, o padrão é GET; (III) Errado, o Método POST é geralmente utilizado para enviar grandes quantidades de dados por meio de um formulário; (IV) Correto.
Gabarito: Letra B

QUESTõES CoMENTADAS - FG V

í. (FGV / TJDFT - 2022) No âmbito de Web services, analise as afirmativas a seguir sobre a abordagem REST e o uso de tecnologias baseadas em SOAP.
I. Uma característica dos serviços Web RESTful é a capacidade de transmitir dados diretamente via HTTP.
II. As mensagens SOAP precisam ser retornadas como documentos XML.

III. Um navegador não pode armazenar em cache uma solicitação concluída por uma API SOAP.
É correto o que se afirma em:

a) somente II;

b) somente I e II;

c) somente I e III;

d) somente II e III;

e) I, lie III.

Comentários:

(I) Correto, a grande vantagem do WerService RESTful é poder transmitir dados diretamente viaHTTP; (II) Correto, é fundamental que seja utilizado XML; (III) Correto, navegadores realmente não podem armazenar em cache uma solicitação concluída a uma API SOAP. Por isso, não é possível acessá-la depois sem fazer o reenvio à API.
Gabarito: Letra E

2. (FGV / TJDFT - 2022) O analista de sistemas Pedro desenvolveu o webservice RService aplicando o estilo de arquitetura REST (Representational State Transfer). As aplicações clientes que utilizam o RService são desenvolvidas de forma desacoplada e dissociada de RService e manipulam os recursos de RService através de representações transferidas em mensagens autodescritivas.
Para habilitar a independência no desenvolvimento de aplicações clientes com o uso de representações em mensagens autodescritivas, Pedro aplicou em RService o princípio REST:
a) arquitetura cliente-servidor;

b) código sob demanda;

c) interface uniforme;

d) sistema em camadas;

e) capacidade de cache.

Comentários:

A questão se refere ao princípio de interface uniforme: as mensagens devem conter mensagens auto-descritivas - cada requisição deve conter informações suficientes para o servidor poder processara informação.
Todas as interações entre cliente, servidor e componentes intermediários são baseadas na uniformidade de suas interfaces. Isso simplifica a arquitetura geral, visto que componentes podem evoluir de forma independente à medida que implementem o que foi acordado em contrato. Ébasicamente um contrato para comunicação entre cliente e servidor. São regras para fazer um componente o mais genérico possível, tornando-o muito mais fácil de ser refatorado e melhorado.
Gabarito: Letra C

3. (FGV / TJDFT - 2022) Kátia é uma web designer contratada para fazer uma página web para oTribunal de Justiça. Ela fará uso do protocolo HTTP, pois este é um protocolo da camada de aplicação, o qual executa sob o TCP e associado à web. As operações nesse protocolo são chamadas de métodos. Kátia, então, testa o envio da página pelo servidor, cria uma coleção de páginas web em um servidor remoto e instrui o servidor a enviar de volta a solicitação.
Para implementar a página web, Kátia deve usar, respectivamente, os métodos:

a) POST, HEAD, DELETE;

b) GET, CONNECT, TRACE;

c) PUT, CONNECT, OPTIONS;

d) POST, HEAD, OPTIONS;

e) GET, PUT, TRACE.

Comentários:

O envio da página se dá pelo Método GET; a criação de dados no servidor se dá pelo
Método PUT;
e o envio de volta da solicitação se dá pelo Método TRACE.

Lembrando que o TRACE realiza um teste de loopback enviando uma mensagem por todo o caminho até o recurso alvo no qual foi destinado, provendo um mecanismo útil para debug.
Gabarito: Letra E

4. (FGV / FUNSAÚDE - 2021) Com relação ao HTTP no contexto de aplicações web, assinale a lista que contém dois dos métodos desse protocolo.
b) GETePOST.

c) OPEN e CLOSE.

d) READ e WRITE.

e) STARTe END.

Comentários:

Os métodos do HTTP são: GET, POST, PUT, DELETE, TRACE, OPTIONS, PATCH, CONNECT. No entanto, os dois primeiros são disparadamente os mais conhecidos e cobrados em prova.
Gabarito: Letra B

5. (FGV / Prefeitura de Niterói-RJ - 2018) As tecnologias SOAP e REST são largamente utilizadas para troca de informações estruturadas em sistemas distribuídos. Sobre essas tecnologias,analise as afirmativas a seguir.

I. REST pressupõe que cada solicitação do cliente ao servidor deve contertodas as informações necessárias para processar o pedido e não pode tirar proveito de qualquer contexto armazenado no servidor.
II. As mensagens SOAP são documentos XML construídos especificamente para trafegar através do protocolo de transporte HTTP/HTTPS.
III. REST é mais eficiente que o SOAP porque utiliza exclusivamente mensagens menores no formato JSON.
Está correto o que se afirma em:

a) I, apenas.

b) II, apenas.

c) III, apenas.

d) I e II, apenas.

e) I, lie III.

Comentários:

(I) Correto, visto que eles são autocontidos e steteless; (II) Errado, não é obrigatório utilizar HTTP /HTTPS; (III) Errado, não é obrigatório utilizar JSON.

Gabarito: Letra A

6. (FGV/AL-RO-2018) O padrão REST define um conjunto de restrições e propriedades baseado em HTTP. Sobre REST, analise as afirmativas a seguir.
I. Web services que obedecem ao padrão REST precisam utilizar o formato
JSON para encapsular os dados da resposta às requisições dos sistemas solicitantes.
II. Os métodos GET, POST, PUT e DELETE do protocolo de comunicação HTTP são compatíveis com operações CRUD para a persistência de dados.
III. O padrão REST pressupõe que requisições de um mesmo sistema solicitante são dependentes, permitindo manter o estado de cada solicitante durante várias solicitações.
Está correto o que se afirma em:

a) I, somente.

b) II, somente.

c) III, somente.

d) I e II, somente.

e) I, lie III.

Comentários:

(I) Errado, não é obrigatório utilizar JSON; (II) Correto. CRUD se refere a Create (POST), Read
(GET),
Update (PUT) e Delete (DELETE); (III) Errado, ele pressupõe que são indepedentes, não mantendo o estado de cada solicitante durante várias solicitações (state/ess).
Gabarito: Letra B

7. (FGV / AL-RO - 2018) SOAP é um protocolo para troca de informações estruturadas.
Sobre a estrutura da mensagem SOAP, analise as afirmativas a seguir.
I. O formato da mensagem é baseado na linguagem de marcação XML.

II. Os elementos Header e Body são filhos obrigatórios do elemento Envelope.

III. O elemento Fault é opcional e quando estiver presente deve aparecer como um elemento filho do elemento Envelope.
Está correto o que se afirma em:

a) I, somente.

b) II, somente.

c) III, somente.

d) I e III, somente.

e) I, lie III.

Comentários:

(I) Correto; (II) Errado, Header é opcional; (III) Errado, quando estiver presente deve aparecer como um elemento filho do elemento Body.
Gabarito: Letra A

8. (FGV / BANESTES - 2018) Sobre os princípios do padrão REST, analise as afirmativas a seguir.

I. As mensagens REST são documentos texto no formato JSON.

II. REST é independente do protocolo de transporte, podendo ser implementado com HTTP,
SMTPou JMS.

III. Serviços REST são stateless, isto é, cada solicitação deve conter todas as informações necessárias para ser compreendida pelo servidor.
Está correto o que se afirma em:

a) somente I;

b) somente II;

c) somente III;

d) somente I e III;

e) I, lie III.

Comentários:

(I) Errado, não são necessariamente documentos no formato JSON; (II) Errado,
não pode ser implementado com JMS; (III) Correto.
Gabarito: Letra C

9. (FGV / BANESTES - 2018) A linguagem baseada em XML utilizada para descrever um web service, suas operações e como acessá-lo é:
a) XSLT

b) XSD

c) DTD

d) WSDL

e) UDDI

Comentários:

A linguagem baseada em XML utilizada para descrever um web service, suas operações e como acessá-lo é o WSDL.
Gabarito: Letra D

io.(FGV / BANESTES - 2018) Sobre a implementação de serviços web com padrão SOAP,
analise as afirmativas a seguir.
I. As mensagens SOAP são documentos XML.

II. A dependência do SOAP ao protocolo de transporte HTTP é uma restrição para implementação deste padrão.
III. O padrão é inadequado para troca de informações em uma plataforma descentralizada e distribuída.
Está correto o que se afirma em:

a) somente I;

b) somente II;

c) somente III;

d) somente I e II;

e) I, lie III.

Comentários:

(I) Correto; (II) Errado, ele não é dependente do HTTP; (III) Errado, é totalmente adequado para troca de informações em uma plataforma descentralizada e distribuída.
Gabarito: Letra A

11. (FGV / BANESTES - 2018) Usualmente, WebServices envolvem a utilização dos padrões
XML,
SOAP e WSDL. A função de cada um deles é, respectivamente:

a) descrever os parâmetros, disponibilizar o serviço, transferir as mensagens;

b) transferir as mensagens, descrever o algoritmo, transportar as mensagens;

c) rotular e formatar os dados, transferir as mensagens, descrever a disponibilidade do serviço;

d) transferir as mensagens, descrever a disponibilidade do serviço, formatar os parâmetros;

e) descrever as classes e suas interfaces, instanciar os objetos, descrever os algoritmos.

Comentários:

A função de cada um deles é, respectivamente, rotular e formatar os dados,
transferir as mensagens, descrevera disponibilidade do serviço.
Gabarito: Letra C

i2.(FGV / IBGE - 2017) SOAP (Simple Object Access Protocol) é um protocolo de comunicação projetado para permitir a troca de informações de maneira estruturada entre sistemas distribuídos. Em relação à estrutura da mensagem SOAP versão 1.2 definida pela W3C,analise as afirmativas a seguir:
I. A mensagem SOAP é definida em um documento XML que contém um elemento raiz denominado Envelope.
II. Header é um elemento mandatório que fornece informações específicas para autenticação.

III. Error é um elemento opcional que contém as informações dos erros ocorridos no envio da mensagem.
Está correto o que se afirma em:

a) somente I;

b) somente II;

c) somente III;

d) somente I e III;

e) I, lie III.

Comentários:

(I) Correto; (II) Errado, é opcional; (III) Errado, não se chama Error-chama-se Fault.

Gabarito: Letra A

13. (FGV / IBGE - 2017) Com relação a REST e SOAP, analise as afirmativas a seguir:

I. REST é baseado em orientação a recursos, sendo indicado para operações stateless.

II. SOAP é um protocolo para troca de mensagens estruturadas, que podem possuir diferentes formatos, tais como JSON, HTML ou XML.
III. Tanto REST quanto SOAP foram concebidos para utilizar diferentes protocolos de comunicação, além do HTTP.
Está correto somente o que se afirma em:

a) I;

b) H;

C) III;

d) I e II;

e) I e III.

Comentários:

(I) Correto, ele é stateless; (II) Errado, deve necessariamente possuir o formato XML;
(III) Errado,
podem até utilizar outros, mas foram concebidos para utilizar HTTP.

Gabarito: Letra A

i4.(FGV / IBGE - 2017) SOAP (Simple Object Access Protocol) é um protocolo de comunicação utilizado para troca de informações estruturadas entre sistemas computacionais.Analise as afirmativas a seguir sobre a estrutura de uma mensagem SOAP:
I. É codificada como um documento XML e o elemento <Envelope> é o elemento-raiz da mensagem.
II. O elemento <Header> é opcional e o elemento <Body> obrigatório.

III. O elemento <Fault> é utilizado para transportar informações de erro dentro de uma mensagem SOAP.
Está correto o que se afirma em:

a) somente I;

b) somente II;

c) somente III;

d) somente I e III;

e) I, lie III.

Comentários:

(I) Correto; (II) Correto; (III) Correto. Na a acrescentar - são itens muito objetivos.

Gabarito: Letra E

i5.(FGV / IBGE - 2016) Uma mensagem no protocolo SOAP, versão 1.2, é representada por um documento XML capaz de transportar dados de serviços Web. Os elementos considerados opcionais são:
a) Title e Meta;

b) Envope e Body;

c) Headere Fault;

d) Model e Control;

e) Footer e Namespace.

Comentários:

Envelope e Body são obrigatórios; Header e Fault são opcionais.

Gabarito: Letra C

i6.(FGV / DPE-RO - 2015) A REST (Representational State Transfer, em português
Transferência de Estado Representacional) dá ênfase:
a) na multiplicidade de representação de recursos, utilizando apenas os métodos padrão do protocolo HTTP (GET, POST, PUT, DELETE, etc);
b) na multiplicidade de representação de métodos, utilizando apenas os recursos padrão do protocolo HTTP (GET, POST, PUT, DELETE, etc);
c) em utilizar o protocolo SOAP sobre o protocolo HTTP;

d) na segurança por meio do protocolo HTTPS 2.0;

e) na integração baseada em troca de mensagens assíncronas por meio de web-sockets.

Comentários:

(a) Correto; (b) Errado, são métodos e, não, recursos; (c) Errado, REST não utiliza
SOAP; (d) Errado,
honestamente não vejo erro nesse item; (e) Errado, não há nenhuma relação com websocket.

Gabarito: Letra A

17. (FGV / DPE-RO - 2015) A função da WSDL (Web Services Description Language -
Linguagem de Descrição de Serviços Web) é:
a) executar métodos de um serviço SOAP;

b) descrever um serviço Web, informando o local do serviço e os métodos expostos por ele;

c) descrever os objetos de um Serviço REST;

d) linguagem de programação para serviços SOAP;

e) linguagem de programação para XML.

Comentários:

(a) WSDL não executa nada, apenas descrever serviços web; (b) Correto; (c) Errado,
descreve serviços web e, não, objetos; (d) Errado, não é uma linguagem de programação; (e)Errado, não é uma linguagem de programação.
Gabarito: Letra B

i8.(FGV / TJ-GO - 2014) Mensagem utilizada para comunicação com um Serviço
Web (Web
Service), implementado com o protocolo SOAP 1.2.

< soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope">
< soap:Header>

< m:Trans xmlns:m=http://www.w3schools.com/transaction/
soap:mustUnderstand="false" >234 < /m:Trans >

< /soap:Header>

< soap:Body xmlns:m="http://www.example.org/stock" >

< m:GetStockPrice >

< m:StockName>IBM

< /m:GetStockPrice >

< /soap:Body >

< /soap:Envelope >

0(s) elemento(s) que pode(m) ser retirado(s) da mensagem, de acordo com a especificação do protocolo SOAP, sem prejuízo para a comunicação com o Serviço Web, é/são:
a) soap:Envelope;

b) soap:Headere soap:Body;

c) soap:Body e soap:Envelope;

d) soap:Header;

e) soap:Body.

Comentários:

Os elementos que podem ser retirados da mensagem são os elementos opcionais. Vamos avaliar os itens: (a) Errado, é obrigatório; (b) Errado, soap:Body é obrigatório; (c)Errado, ambos são obrigatórios; (d) Correto; (e) Errado, é obrigatório.
Gabarito: Letra D

ig.(FGV/AL-MA-2013) Com relação à especificação SOAP versão 1.2, assinale V para a afirmativa verdadeira e F para a falsa.
() O elemento "SOAP HEADER" é obrigatório em qualquer mensagem SOAP.

() A especificação SOAP fornece um modelo de processamento distribuído, o qual assume que uma mensagem SOAP é originada em um remetente inicial SOAP e é enviada para um receptorSOAP final, através de zero ou mais intermediários SOAP.

( ) A ocorrência de falhas em uma mensagem SOAP é indicada pelo elemento
"SOAP
EXCEPTION".

As afirmativas são, respectivamente,

a) F, V e F.

b) F, V e V.

c) V, F e F.

d) V, V e F.

e) F, F e V.

Comentários:

(F) É opcional; (V) Correto; (F) É pelo elemento SOAP FAULT.

Gabarito: Letra A

2o.(FGV/ Senado Federal -2012) A respeito de mensagens SOAP, assinale a alternativa correta.

a) O elemento Envelope deve usar o namespace "http://www.w3.org/2oo1/12/soap-envelope".

b) O elemento Envelope não é obrigatório em uma mensagem SOAP.

c) O elemento Body não é obrigatório em uma mensagem SOAP.

d) O elemento Fault é obrigatório em uma mensagem SOAP.

e) O elemento Header é obrigatório em uma mensagem SOAP.

Comentários:

(a) Correto. Não vamos entrar em detalhes, mas o namespace é um conjunto de nomes únicos utilizados para diferenciá-los de itens com o mesmo nome e esse endereço é o namespace de todo elemento Envelope; (b) Errado, é obrigatório; (c) Errado, é obrigatório; (d)Errado, não é obrigatório; (e) Errado, não é obrigatório.
Gabarito: Letra A

2i.(FGV / SEAD-AP - 2010) Originalmente SOAP representava um protocolo para troca de informações estruturadas em uma plataforma descentralizada e distribuída, utilizando tecnologias baseadas em um determinada linguagem. Foi importante para o desenvolvimento de aplicações para permitiram a comunicação via Internet entre programas,empregando o
Remote Procedure CaIIs (RPC) entre objetos como DCOM e CORBA. Atualmente, SOAP provê um caminho de comunicação entre aplicações "rodando" em diferentes sistemas operacionais,com diferentes tecnologias e linguagens de programação.

De acordo com o enfoque do World Wide Web Consortium - W3C, as mensagens SOAP são documentos baseados na seguinte linguagem:
a) WSDL

b) XML

c) JAVASCRIPT

d) AJAX

e) XSLT

Comentários:

As mensagens SOAP são documentos baseados na seguinte linguagem XML

Gabarito: Letra B

22.FGV / MEC - 2009) Um Web Service é definido pela W3C como um sistema de software projetado para fornecer interoperabilidade entre máquinas em uma determinada rede. Dentro do contexto dos Web Services assinale a alternativa correta.
a) A UDDI (Universal Description, Discovery, and Integration) é uma linguagem baseada emXML que descreve o que um Web Service pode fazer, onde ele reside e como chamá-lo.

b) SOAP (Simple Object Access Protocol) é um protocolo, baseado em XML, para troca de informação estruturada com Web Services em redes de computadores.
c) A interoperabilidade entre os Web Services e aplicações é garantida devido ao uso obrigatório da linguagem Java na implementação das aplicações.
d) SOA (Simple Object Access) é uma plataforma de arquitetura orientada a serviços,
utilizada como base para suportar os Web Services.
e) A WSDL (Web Services Description Language) é uma especificação para publicar e localizar informações sobre Web Services.
Comentários:

(a) Errado, esse seria o WSDL; (b) Correto; (c) Errado, não é obrigatório utilizar a linguagem Java;
(d) Errado, SOA é Service Oriented Architecture e não utiliza obrigatoriamente serviços web; (e)Errado, esse seria o UDDI.

Gabarito: Letra B

23.(FGV / MEC - 2009) A respeito das tecnologias relacionadas a Web Services, analise as afirmativas a seguir:
I. A UDDI é uma plataforma de arquitetura orientada a serviços assíncronos utilizada como base para suportar os Web Services.
II. A WSDL (Web Services Description Language) é uma interface de programação que permite a execução de chamadas remotas no estilo RPC.
III. SOAP (Simple Object Access Protocol) é um protocolo, baseado em XML, para troca de informação estruturada com Web Services em redes de computadores.
Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente a afirmativa II estiver correta.

c) se somente a afirmativa III estiver correta.

d) se somente as afirmativas II e III estiverem corretas.

e) se todas as afirmativas estiverem corretas.

Comentários:

(I) Errado, é um serviço de diretório para descrição, publicação, descoberta e integração de serviços web; (II) Errado, é uma linguagem para descrição de serviços web; (III) Correto.
Gabarito: Letra C

24-(FGV / Senado Federal - 2008) Considere as assertivas a seguir sobre as relações entre SOAP,WSDLeUDDI:

I. UDDI é um diretório de serviços web descrito por WSDL.

II. WSDL pode ser usado para descrever serviços SOAP.

III. O UDDI é um diretório de descrições SOAP.
As assertivas corretas são:

a) somente I.

b) somente I e II.

c) somente I e III.

d) somente II e III.

e) I, lie III.

Comentários:

(I) Correto; (II) Errado, é utilizado para descrever serviços web; Errado, é diretório para descrição de serviços web.
Gabarito: Letra A

QUESTõES CoMENTADAS - DIvERSAS BANCAS

í. (FAURGS / BANRISUL - 2018) Quais são as quatro operações para realizar tarefas definidas pelo serviço web no formato REST?
a) CREATE, GET, PUT e UPDATE

b) PUT, UPDATE, INSERT e DELETE

c) POST, GET, PUT e DELETE

d) PUT, GET, INSERT e DELETE

e) SELECT, GET, PUT e DELETE

Comentários:

As quatro operações são: POST, GET, PUT e DELETE.

Gabarito: Letra C

2. (IBFC / TJ-PE - 2017) Existe a necessidade em um documento XML ser identificado como uma mensagem SOAP. A estrutura da mensagem SOAP (Simple Object Access Protocol), em um documento XML, contém os seguintes elementos:
a) Title (obrigatório) - Head (opcional) - Body (obrigatório)

b) Envelope (obrigatório) - Header (opcional) - Main (obrigatório)

c) Title (obrigatório) - Head (opcional) - Main (obrigatório)

d) Envelope (obrigatório) - Header (opcional) - Body (obrigatório)

e) Envelope (obrigatório) - Head (opcional) - Main (obrigatório)

Comentários:

SOAP contém Envelope (Obrigatório) - Header (Opcional) - Body (Obrigatório).

Gabarito: Letra D

3. (IBFC / EBSERH - 2017) Assinale a alternativa que apresenta o serviço de diretório onde empresas podem registrar (publicar) e buscar (descobrir) por Serviços Web (Web Services):
a) UDDI

b) NIS

c) WSDL

d) X.500

e) LDAP

Comentários:

Serviço de diretório? Permite registrar/publicar e buscar/descobrir web services? Trata-se do UDDI
(Universal Description, Discovery and Integration').

Gabarito: Letra A

4. (IBFC / EBSERH -2017) Web service é uma solução utilizada na integração de sistemas. Os Web services são componentes que permitem às aplicações enviar e receber dados, como padrão,em formato:

a) NAT

b) ARP

c) XML

d) TLS

e) XDR.

Comentários:

O formato padrão de Web Services (SOAP) é o XML! As outras opções não fazem o menor sentido...

Gabarito: Letra C

5. (IBFC / EBSERH - 2017) Conforme o W3C (World Wide Web Consortium) pode-se definir umWeb Service como sendo:

a) uma estrutura conceituai para reger projetos de engenharia de software.

b) técnicas baseadas em formalismos matemáticos para a especificação,
desenvolvimento e verificação dos sistemas de softwares e hardwares.
c) um modelo de referência que contém práticas necessárias à manutenção do software.

d) um sistema de software projetado para suportar a interoperabilidade entre máquinas sobre rede.
e) um modelo de dados que representa um conjunto de conceitos dentro de um domínio e os relacionamentos entre estes.
Comentários:

(a) Errado, acredito que isso seria um modelo de processo de software; (b) Errado,
acredito que isso seria o processo de software de métodos formais; (c) Errado, acredito que isso seria mais relacionado ao CMMI; (d) Correto, ele é extremamente útil para suportar interoperabilidade na troca de informações entre máquinas da rede; (e) Errado, acredito que isso seria mais relacionado ao modelo entidade relacionamento.
Gabarito: Letra D

6. (IBFC / EMDEC -2016) Quanto as tecnologias aplicadas em um Web Service temos:

"Para a representação e estruturação dos dados nas mensagens recebidas/enviadas é utilizado o . As chamadas às operações, incluindo os parâmetros de entrada/saída, são codificadas no protocolo. Os serviços (operações, mensagens, parâmetros,etc.) são descritos usando a linguagem. O processo de publicação/pesquisa/descoberta de WebServices utiliza o protocolo."

Assinale a alternativa que complete correta e respectivamente as lacunas:

a) SOAP - WSDL - UDDI - XML

b) WSDL - UDDI - XML - SOAP

c) UDDI-XML-SOAP-WSDL

d) XML - SOAP - WSDL - UDDI.

Comentários:

Para a representação e estruturação dos dados nas mensagens recebidas/enviadas é utilizado oXML. As chamadas às operações, incluindo os parâmetros de entrada/saída, são codificadas no protocolo SOAP. Os serviços (operações, mensagens, parâmetros, etc.) são descritos usando a linguagem WSDL. O processo de publicação/pesquisa/descoberta de Web Services utiliza o protocolo UDDI.
Gabarito: Letra D

7. (CCV / UFC - 2016) Sobre Web Services, assinale a opção correta.

a) Web services não possui suporte a mensagens com arquivos binários.

b) WSDL é baseado em XML, enquanto SOAP é baseado em javascript.

c) WSDL e SOAP podem ser utilizados juntos para prover Web Services.

d) WDSL e SOAP não são recomendação do W3C (World Wide Web Consortium).

e) Um componente Web Service desenvolvido em linguagem Java não pode ser acessado por meio da linguagem PHP.
Comentários:

(a) Errado, ele suporta sim; (b) Errado, ambos são baseados em XML; (c) Correto; (d)
Errado, ambos são recomendados pela W3C; (e) Errado, é claro que pode.
Gabarito: Letra C

8. (IF-PI / IF-PI - 2016) Trata-se de um protocolo de comunicação de web services descrito por uma WSDL (Web Services Description Language), ele consiste de um grande arquivo XMLtrafegando entre sistemas para realizar a comunicação. O conceito se refere ao:

a) SOAP.

b) OpenLDAP.
C)X25.

d) DHCP.

e) DNS.

Comentários:

O protocolo de comunicação descrito por um WSDL que trafega entre sistemas para realizar a comunicação é o SOAP.
Gabarito: Letra A

9. (FUNIVERSA / IF-AP - 2016) SOAP (Simple Object Access Protocol) é um protocolo de comunicação que permite a troca de mensagens entre aplicações Web, geralmente usandoHTTP e Webservices. Assinale a alternativa que apresenta o formato das mensagens utilizadas pelo SOAP.
a) UDP (User Datagram Protocol)

b) TCP (Transmission Control Protocol)

c) XML (eXtensible Markup Language)

d) FTP (File Transfer Protocol)

e) ODF (Open Document Format)

Comentários:

O formato das mensagens utilizadas pelo SOAP é o XML.

Gabarito: Letra C

io.(ESAF / ANAC -2016) São tecnologias essenciais para Web Services:

a) Protocolo HSTP. XML. SIP. WSDL. UMDI.

b) Protocolo HTTP. RML. SOAP. WDLL. UDDI.

c) Protocolo TC/IP. XML. SORP. WSDL. UDTS.

d) Protocolo HTIP. XDL. SO2AP. WSDD. UDDI.

e) Protocolo HTTP. XML. SOAP. WSDL. UDDI.

Comentários:

Protocolo HTTP, XML, SOAP, WSDL e UDDI.

Gabarito: Letra E

li. (FUMARC / AL-MG - 2014) Analise as seguintes afirmativas sobre os métodos HTML:

I. HTML POST é utilizado para enviar dados para serem processados em um servidor Web.

II. HTML GET solicita ao servidor apenas o cabeçalho de uma URL para que o cliente decida se deve requisitar o conteúdo completo ou não.
III. HTML PUT é utilizado para criar recursos dentro de um servidor Web.

Estão CORRETAS as afirmativas:

a) I e II, apenas.

b) I e III, apenas.

c) II e III, apenas.

d) I, lie III.

Comentários:

Vejam que absurdo: essa questão não foi anulada! Não existe Método HTML -existe Método
HTTP!
Enfim... vamos ignorare comentara questão: (I) Correto; (II) Errado, esse seria o
Método HEAD; (III)
Correto.

Gabarito: Letra B

12. (MPE-RS / MPE-RS - 2012) Um formulário em HTML é um modelo de entrada de um conjunto de dados. O primeiro passo a ser dado para a construção de um formulário é fazer as etiquetas que desenham as janelas de entrada de dados. Os métodos que transferem dados do browser para o servidor são denominadose.
a) input-output b) post-get c) push - pop d) post-cat e) push - pull
Comentários:

Os métodos que transferem dados do browser (cliente) para o servidor são denominados
POST e
GET.

Gabarito: Letra B

13.(MPE-RS / MPE-RS - 2012) Considere as seguintes afirmações a respeito de REST(Representational State Transfer).

I. REST é um protocolo para troca de mensagens entre componentes de uma aplicação web.

II. REST é uma arquitetura, onde cada aplicação é um conjunto de recursos sobre os quais podemos realizar ações.
III. Os formatos dos arquivos utilizados numa aplicação que segue REST são JSON, XML
ou
YAML.

Quais estão corretas?

a) Apenas I.

b) Apenas II.

c) Apenas III.

d) Apenas I e III.

e) Apenas II e III.

Comentários:

(I) Errado, REST não é um protocolo - é um estilo arquitetural; (II) Correto,
trata-se de um estilo arquitetural (termo mais correto) baseado em recursos; (III) Correto, todos esses formatos podem ser utilizados.
Gabarito: Letra E

i4.(COPEVE-UFAL / ALGÁS - 2012) REST é uma técnica de engenharia de software utilizada no desenvolvimento de sistemas hipermídia distribuídos e adequada para a Web.
Comentários:

Eu sei que é estranho falar em REST como uma técnica de engenharia de software, mas vamos abstrair! De fato, ele é utilizado no desenvolvimento de sistemas hipermídia distribuídos e muito adequada a Web.
Gabarito: Correto

15.UFF / UFF - 2009) No tocante ao protocolo de transferência de hipertexto
(HTTP), esse protocolo da categoria "solicitação e resposta" possui três métodos de solicitação. São eles:
a) HEAD, BODYeINIT;

b) FLAG, TOS e TTL;

c) GET, HEADePOST;

d) PUT, GETe INIT;

e) PUSH, POSTeHEAD.

Comentários:

Os três métodos de solicitação são GET, HEAD e POST.

Gabarito: Letra C

i6.(CESGRANRIO / PETROBRÁS - 2008) A interoperabilidade entre aplicações nos dias atuais é fortemente baseada no uso de web services. Duas abordagens arquiteturais distintas para o projeto e implementação de web services têm-se firmado no cenário de tecnologia. São elas:
a) RESTeWS-*

b) SOAPeWSDL

c) RPCeRMI

d) SGML e HTML

e) B2B e B2C

Comentários:

As duas abordagens são WS-* e REST.

Gabarito: Letra A

17. (CESGRANRIO / REFAP-ES - 2007) O estilo arquitetural REST (Representational
State
Transfer) para WEB tem como característica:

a) permitir o uso de RPC diretamente sobre SSL, para aplicações seguras.

b) acelerar a transferência do FTP com a implementação de cache.

c) combater o SPAM, utilizando redes neurais como técnica de aprendizagem.

d) usar SOAP para interoperabilidade entre sistemas heterogêneos.

e) utilizar os métodos HTTP: GET, POST, PUT e DELETE.

Comentários:

(a) Errado, ele não utiliza RPC; (b) Errado, acelera a transferência do HTTP com a implementação de cache; (c) Errado, não há nenhuma relação com combate a SPAM; (d) Errado, não utiliza SOAP;
(e) Correto.

Gabarito: Letra E

QUESTõES CoMENTADAS - CESPE

í. (CESPE / BANRISUL - 2022) Em um serviço RESTful, todos os métodos são identificados pela mesma URL, sendo cada método acionado por uma porta específica.
2. (CESPE / TRT8 - 2022) Em uma API RESTful, cada solicitação deve conter todos os dados necessários ao seu atendimento para não depender de informações armazenadas em outras sessões, o que caracteriza uma restrição de:
a) cache.

b) arquitetura cliente-servidor.

c) interface uniforme.

d) sistema de camadas.

e) comunicação stateless.

3. (CESPE / TRT8 - 2022) O método que serve para depuração em HTTP, ao instruir o servidor a enviar de volta a solicitação, é 0:
a) options b) get c) trace d) connect e) post
4. (CESPE / FUNPRESP-EXE - 2022) SOAP (Simple Object Access Protocol) é um protocolo de comunicação usado para a troca de mensagens XML entre o cliente e o provedor de serviço.
5. (CESPE / FUNPRESP-EXE - 2022) UDDI (Universal Description Discovery and
Integration) é um padrão utilizado em SOA para a criação de repositórios de descrição de serviços.
6. (CESPE / FUNPRESP-EXE - 2022) Um documento WSDL possui um conjunto de elementos de nós abstratos e concretos que especificam a localização de um serviço.
7. (CESPE / Petrobrás - 2022) Web service é um sistema de software projetado para suportar interação entre máquinas através de uma rede; esse sistema possui uma interface descrita em formato processável por máquina, especificamente o WSDL (web services descriptor language).
8. (CESPE / Petrobrás - 2022) Uma das vantagens do SOAP é a sua utilização correta dos métodos
HTML (PUT, GET, POST, DELETE), enquanto o REST utiliza apenas o método POST para realizar as requisições através de um arquivo XML.
9. (CESPE / Petrobrás - 2022) Os protocolos SOAP e REST são os padrões mais utilizados na comunicação entre os sistemas por meio do web service; esses protocolos, unidos à estrutura básica XML, compõem a estrutura básica dos web services.
10. (CESPE / DPE-RO - 2021) O REST emprega um protocolo universal, o HTTP, para oferecer um serviço web simples e aberto. Verbos HTTP são usados para realizar chamadas e indicar para o serviço que ação deve ser realizada. Assinale a opção que indica o verbo usado tipicamente para a atualização de um recurso existente:
a) PUT.

b) CREATED.

c) GET.

d) POST.

e) TRACE.

A respeito de tecnologia de integração com RESTful, julgue os itens a seguir.

11. (CESPE / SERPRO - 2021) Webservices possibilitam tanto a recuperação do estado atual de um recurso quanto a exclusão do recurso.
12. (CESPE / SERPRO - 2021) O protocolo de comunicação HTTP e a identificação de recursos podem ser utilizados por meio de URL (Uniform Resource Locator).
13. (CESPE / SERPRO - 2021) As interações acontecem sem controle de estado, o que é conhecido como stateless.
14. (CESPE / SERPRO - 2021) A arquitetura RESTful não possibilita o uso de servidores intermediários, chamados de balanceadoresde carga, razão porque o cliente sempre se conecta ao servidor final.
15. (CESPE/ MEC-2020) REST usa um modelo centrado em recursos de serviços encapsulados,
em que cada recurso fornecido pelo serviço possui uma URL e todos os recursos oferecem suporte a uma interface uniforme.
16. (CESPE / SLU-DF - 2019) Um web service pode assumir o papel de provedor de serviço e de consumidor de serviço.
17. (CESPE / SEFAZ-BA - 2019) Os web services são componentes de software na web que podem fornecer determinados serviços a aplicações criadas em diferentes linguagens. Podem usar o protocolo SOAP para transferência de mensagens em formato XML. Para descrever a estrutura destas mensagens geralmente utiliza-se:
a) REST.

b) WSDL.

c) CORBA.

d) RESTFUL.

e) HTML.

i8.(CESPE / TRT-CE - 2019) Assinale a opção que apresenta o método HTTP que deve ser usado para a busca de recursos por meio do web service RESTful.
a) delete b) get c) put d) options ig.(CESPE / BNB - 2018) SOAP utiliza um sistema de mensagens SMTP sobre a camada de transporte.
20. (CESPE / MPE-PI - 2018) Para implementar um web service de baixo overhead que tenha recursos identificáveis e localizáveis por meio de uma URI (Uniform ResourceIdentifier)
mediante o protocolo HTTP, pode-se utilizar o REST (Representational State Transfer).

21. (CESPE / STJ - 2018) Web service é uma solução utilizada na integração de sistemas e na comunicação entre aplicações diferentes.
22. (CESPE / STJ -2018) Os serviços Web RESTful utilizam o HTTP como um meio de comunicação entre cliente e servidor.
23. (CESPE / STJ - 2018) A REST define uma arquitetura cliente-servidor na qual o servidor não mantém contexto de cliente entre transações, ou seja, é stateless e toda transação contém as informações necessárias para satisfazer a solicitação.
24. (CESPE / STM - 2018) O SOAP é um tipo de modelo de dados XML elaborado para facilitar a inserção de campos HTML em páginas web.
25. (CESPE / SEDF - 2017) Serviços expressos por meio de contratos web services têm o potencial de evitar completamente a transformação, objetivo-chave dos contratos de serviços padronizados.
26. (CESPE / TRE-BA - 2017) No que se refere a web services, assinale a opção correta.

a) As solicitações e respostas XML trafegam no protocolo HTTP, não sendo possível utilizá-las nos protocolos FTP e SMTP.
b) Um dos componentes de um Web Service SOAP (Simple Object Access Protocol) é a UDDI
(Universal Description, Discovery and Integration), a qual é um arquivo do tipo XML que descreve detalhadamente um Web Service, especificando como deve ser o formato de entrada e saída de cada operação.
c) As duas formas de envio de mensagem para que um cliente possa efetuar solicitações a umWeb Service são One-Way Messaging e Request-Response Messaging.

d) O WSDL (Web Services Description Language) é uma linguagem para o desenvolvimento de
Web Services similar ao XML.

e) Os Web Services permitem a integração de sistemas, todavia dependem da linguagem de programação sob a qual tenham sido desenvolvidos e do sistema operacional do computador onde esses sistemas forem executados.
27. (CESPE / TRE-PE - 2017) REST (Representational State Transfer) é:

a) um estilo de desenvolvimento que utiliza o protocolo HTTP e se baseia na interação simples entre cliente e servidor.
b) um software de infraestrutura em um sistema distribuído que auxilia no gerenciamento de interações entre entidades distribuídas em serviços web.
c) uma linguagem web voltada a definição de predicados que se apliquem a classes de objetos e de interações em um modelo UML.
d) uma linguagem de programação com tipos dinâmicos, voltada principalmente para desenvolvimento de aplicações web.
e) um modelo de desenvolvimento de software estruturado e organizado como um conjunto de classes de objeto e de relações entre essas classes.
28. (CESPE / MEC-2016) A respeito dos conceitos de web services e REST, assinale a opção correta.

a) O método POST é utilizado na atualização de um recurso existente.

b) Pode-se utilizar qualquer meio de transporte existente para o envio de uma requisição,incluindo HTTP, SMTP e TCP.

c) O modelo REST impõe restrições ao formato da mensagem.

d) Ao desenvolver uma aplicação, o recurso é transferido pela rede.

e) As chamadas às URIs (uniform resource indicator) são feitas por meio de métodos
HTTP, os quais indicam para o serviço a ação a ser realizada com o recurso.
2g.(CESPE / TRE-MT - 2016) Acerca de REST (representational state transfer), assinale a opção correta.
a) O protocolo REST utiliza SOAP e XML

b) REST utiliza recurso não identificável baseado em PUT e GET.

c) REST pode ser utilizado para implementar WebServices de baixo overhead.

d) Embora opcionalmente, um recurso REST pode conter uma URI.

e) REST consiste em um estilo de desenvolvimento baseado em complexa interação cliente/servidor.
30. (CESPE/ TCE-PA - 2016) Os web services devem ser projetados para ser utilizados independentemente de paradigmas de programação.
31. (CESPE/ TCE-PA - 2016) Para que um web service funcione corretamente,
os softwares cliente/servidor devem ser escritos na mesma linguagem.
32. (CESPE/ TCE-PA - 2016) Ao se usar o protocolo SOAP (Simple Object Access
Protocol), cada solicitação e cada resposta são colocadas em um envelope SOAP, nos momentos de invocação e retorno de um web service, respectivamente.
33. (CESPE / MEC - 2015) Entre as restrições da REST está a interface uniforme, a qual requer que um serviço ofereça várias operações e aguarde a solicitação dessas operações pelo servidor.
34. (CESPE/ MEC-2015) Afim de implementar serviços em REST, recomenda-se utilizar os
WSDL
já existentes com mínima alteração do cabeçalho, informando somente que o protocolo a ser utilizado é o REST.
35. (CESPE / MEC-2015) As principais características do REST (Representationl State
Transfer) são interface uniforme, stateless e cache.
36. (CESPE/ MEC - 2015) E m uma web service, a linguagem de implementação e a plataforma utilizada são relevantes para os clientes.
37. (CESPE / ANTAQ - 2014) Em arquiteturas REST, nenhum contexto de cliente pode ser mantido em servidor.
38.(CESPE / ANATEL - 2014) REST é uma técnica de engenharia de software para sistemas hipermídia distribuídos. De acordo com essa técnica, o estado da informação deve ser mantido no cliente, e o servidor não deve guardar o estado da comunicação de nenhum cliente que se comunique com o servidor, além de uma única requisição.
3g.(CESPE / CNJ - 2013) Uma das formas de comunicação para encapsular dados transferidos no formato XML para aplicações serviço web (Webservice) é o SOAP (Simple ObjectAccess
Protocol).

40.(CESPE / CNJ - 2013) A linguagem WSDL é utilizada para descrever web services limitadas ao tipo request-response.
Zji.(CESPE / CNJ - 2013) Nos registros de negócio UDDI, a descrição da forma de acesso aos web services é um procedimento contido nas páginas verdes (green pages).
42. (CESPE / CNJ - 2013) Um dos elementos de uma mensagem SOAP é o corpo (body),
no qual devem estar contidas as informações de erro e status.
43. (CESPE / ANTT - 2013) Web Services provêm um meio padrão para interoperação entre diferentes aplicativos de software, que podem ser executados em uma variedade de plataformas e(ou) frameworks.
44. (CESPE / TCE-RO - 2013) O SOAP permite a troca de mensagens estruturadas em ambiente distribuído e descentralizado, com o uso de tecnologias XML. Essas mensagens podem ser trocadas por uma variedade de protocolos subjacentes como, por exemplo, o HTTP.
45. (CESPE / SERPRO - 2013) A comunicação entre sistemas clientes e servidores para troca de mensagens pode ser realizada por meio de SOAP (Simple Object Access Protocol), que é um protocolo para troca de informações estruturadas independente de linguagem de programação.
46. (CESPE / CNJ - 2013) Uma das formas de comunicação para encapsular dados transferidos no formato XML para aplicações serviço web (webservice) é o SOAP (Simple ObjectAccess
Protocol).

47. (CESPE / TRE-MS - 2013) O WS-Security propõe uma série de extensões para aprimorar a segurança dos web services no UDDI e no WSDL. Por questão de compatibilidade, essas extensões não afetam os cabeçalhos do envelope SOAP.
48. (CESPE / BACEN - 2013) O estilo arquitetural REST define um conjunto de restrições para uma aplicação, como, por exemplo, utilização de arquitetura par-a-par, manutenção de informações de estado, não uso de cache no cliente e apresentação de uma interface uniforme.
49. (CESPE / SERPRO - 2013) Um web service pode ocorrer sobre o HTTP (Hypertext
Transfer
Protocol), utilizando-se os serviços RESTfull (Representational State Transfer).

50. (CESPE / STF - 2013) A REST (Representational State Transfer), protocolo de comunicação embasado em XML, permite a comunicação de mensagens entre aplicações por meio de qualquer protocolo de comunicação em rede. Normalmente, esse protocolo é utilizado na integração de sistemas legados.
51. (CESPE / MPU - 2013) Web services é um método de comunicação entre serviços na
Web que aderem estritamente ao XML, como é o caso de serviços cuja comunicação é baseada na interface da arquitetura REST.
52. (CESPE / PEFOCE - 2012) SOAP é um protocolo leve destinado à troca de informações estruturadas em um ambiente distribuído e descentralizado. Uma mensagem SOAP,por exemplo, é um documento XML composto de três partes obrigatórias: envelope, cabeçalho e corpo.
53. (CESPE / MPE-PI - 2012) Em web services, utiliza-se o protocolo SOAP (Simple
Object Access
Protocol) para a comunicação entre os serviços.

54-(CESPE / TJ-RO - 2012) Representational state transfer (REST), que utiliza o WSDL como linguagem de descrição de serviços, é uma forma de implementação de SOA na web.
55. (CESPE / MEC - 2011) O UDDI (Universal Description Discovery and
Integration), que corresponde a um registro de web services, é dividido em páginas brancas, amarelas e verdes,nas quais são prestadas aos clientes informações sobre a empresa, os serviços por ela oferecidos e as especificações WSDL desses serviços.
56. (CESPE / PREVIC - 2011) No WSDL (Web Services Definition Language), é prescrito o leiaute de banco de dados com descrições de serviços, por meio das quais os clientes de web service podem procurar serviços relevantes.
57. (CESPE / PREVIC-2011) Web Services são sistemas embasados na Web que oferecem serviços gerais para aplicações remotas, não requerendo interações imediatas de usuários finais.
58. (CESPE/MEC-2011) E m formulários HTML, apenas o método post é suportado; o método get é utilizado em aplicações JavaScript.
59. (CESPE / MEC -2011) Um web service pode ser desenvolvido, também, com o uso de
REST, que utiliza o protocolo HTTP para comunicação entre emissor e destinatário, e oSOAP, para encapsular as mensagens trafegadas.
60. (CESPE / MPU - 2010) REST (Representationals State Transfer) é uma tecnologia que está sendo utilizada em web services, como substituta das tecnologias SOAP (Simple ObjectAccess
Protocol) e WSDL.

61. (CESPE / TCU - 2010) Uma equipe de desenvolvimento de software recebeu a incumbência de desenvolver um sistema com as características apresentadas a seguir.
- 0 sistema deverá ser integrado, interoperável, portável e seguro.

- O sistema deverá apoiar tanto o processamento online, quanto o suporte a decisão e gestão de conteúdos.
- O sistema deverá ser embasado na plataforma JEE (Java enterprise edition) v.6,
envolvendo servlets, JSP (Java server pages), Ajax, JSF (Java server faces) 2.0, Hibernate 3.5,SOA e web services.
O líder da equipe iniciou, então, um extenso processo de coleta de dados com o objetivo de identificar as condições limitantes da solução a ser desenvolvida e tomar decisões arquiteturais e tecnológicas que impactarão várias características funcionais e não funcionais do sistema, ao longo de seu ciclo de vida. A partir dessa coleta, o líder deverá apresentar á equipe um conjunto de informações e de decisões.
Com relação às diferentes arquiteturas e tecnologias que, se escolhidas,
impactarão as características do sistema descrito no texto, julgue o item:
O estilo de arquitetura de software denominado REST (Representational State
Transfer)
demanda mais recursos computacionais que o modelo de desenvolvimento de sistemas embasado em SOAP (Single Object Access Protocol), por isso não é recomendável a adoção do padrão REST de arquitetura de software no desenvolvimento do sistema em questão.
62. (CESPE / MPU - 2010) A descrição de um web service é feita utilizando-se WSDL
(Web Services
Description Language), que é uma linguagem embasada em RPC (Remote Procedure Call) e
UDDI (Universal Description Discovery and Integration), com a qual se descreve a forma de acesso dos serviços e seus parâmetros de entrada e de saída.
63. (CESPE / TRE-MT -2010) Com relação a web services, assinale a opção correta.

a) As arquiteturas de aplicação de web services são arquiteturas firmemente acopladas,
nas quais as ligações entre serviços não podem mudar durante a execução.
b) SOAP (Simple Object Access Protocol) é um protocolo com base em HTML que permite troca de informações entre aplicações em um ambiente distribuído.
c) UDDI (Universal Description, Discovery and Integration) é um diretório para armazenamento de informações a respeito de web sevices. Essas informações são descritas em SOAP.
d) A linguagem WSDL (Web Services Description Language) é utilizada para descrever web services.
e) Segundo o W3C (World Wide Web Consortium), web services são apropriados somente para aplicações em que componentes de um sistema distribuído são executados em plataformas semelhantes de um mesmo fornecedor.
64. CESPE / ANATEL - 2009) Os três padrões fundamentais que possibilitam comunicações entre web services são: Simple Object Access Protocol (SOAP) — protocolo que define uma organização para a troca estruturada de dados entre web services; Web ServicesDescription
Language (WSDL) — protocolo que define como as interfaces dos Web Services podem ser representadas; Universal Description, Discovery And Integration (UDDI) —padrão de descoberta que define como são organizadas as informações de descrição do serviço,permitindo que os solicitantes descubram os serviços. Um desses padrões não utiliza a
XML
(Extensible Mark-up Language).

65. (CESPE / CEHAP-PB - 2009) São padrões de Web Services o SOAP, o WSDL e o UDDI,
todos baseados em HTTP.
66. (CESPE / INMETRO - 2009) Na SOA, a descrição do serviço é mantida em um repositórioWSDL, em formato UDDI (Universal Description, Discovery and Integration).

67. (CESPE / ANTAQ - 2009) Nos serviços web, clientes e servidores, direta ou indiretamente,podem acessar documentos UDDI completos por meio de seus URIs (Uniform
Resource
Identifier), usando um serviço de diretório, tal como o WSDL.

68. (CESPE / ANTAQ - 2009) Um componente importante da arquitetura de serviços web é formado por um serviço de diretório que armazena descrições de serviços. Esse serviço deve obedecer ao padrão UDDI (Universal Description, Discovery And Integration).
69. (CESPE / ANTAQ - 2009) Em serviços web, o SOAP pode ser transportado por protocolos como REST, HTTP, SMTP e JMS.
70. (CESPE / TRT-BA - 2008) O UDDI é uma especificação técnica que tem como objetivo descrever, descobrir e integrar web services; é embasado na tecnologia XML, que fornece uma plataforma neutra de dados e permite descrever relações hierárquicas de modo natural.
71. (CESPE / STJ - 2008) O serviço UDDI fornece uma interface para publicar e atualizar informações acerca de serviços web; possibilita pesquisar descrições WSDL pelo nome;provê uma interface que possibilita executar consultas de modo a recuperar uma entidade que corresponda a uma chave ou recuperar entidades que correspondam a um conjunto de critérios de busca.
72. (CESPE / STJ - 2008) O WSDL separa a parte abstrata de uma descrição de serviço da parte concreta; nessa descrição, a parte concreta contém as definições de tipos usados pelo serviço e a parte abstrata especifica como e onde o serviço pode ser contatado. Os documentosWSDL
podem ser acessados via um serviço de diretório como o UDDI; as definições WSDL podem ser geradas a partir de definições de interfaces escritas em outras linguagens.
73. (CESPE / STJ - 2008) O SOAP encapsula mensagens que podem ser transmitidas via
HTTP;
permite o modelo de interação cliente-servidor; define como usar XML para representar mensagens de requisição e resposta. Um documento XML é transportado no corpo de uma mensagem SOAP; no modelo cliente-servidor, o corpo de uma mensagem SOAP pode conter uma requisição, mas não uma resposta.
74. (CESPE / MPE-AM -2008) No protocolo HTTP (Hypertext Transfer Protocol), o método
GET é utilizado em solicitações enviadas pelo servidor ao navegador para que este solicite dados ao usuário de uma página ou para que o próprio navegador forneça os dados solicitados.
GABARITo

1. ERRADO 42.
ERRADO

2. LETRA E 43-
CORRETO

3- LETRA C 44. CORRETO

4- CORRETO 45- CORRETO

5- CORRETO 46. CORRETO

6. CORRETO 47- ERRADO

7- CORRETO 48. ERRADO

8. ERRADO 49-
ANULADA

9- CORRETO 50. ERRADO

10. LETRA A 5i- ERRADO

íi. CORRETO 52. ERRADO

12. ERRADO 53- CORRETO

13- CORRETO 54- ERRADO

14- ERRADO 55- CORRETO

15- CORRETO 56. ERRADO

i6. CORRETO 57- CORRETO

17- LETRA B 58. ERRADO

i8. LETRA B 59- ERRADO

19. ERRADO 60. ERRADO

20. CORRETO 61. ERRADO

21. CORRETO 62. ERRADO

22. CORRETO 63. LETRA D

23- CORRETO 64. ERRADO

24. ERRADO 65. ERRADO

25- CORRETO 66. ERRADO

26. LETRA C 67. ERRADO

27- LETRA A 68. CORRETO

28. LETRA E 69.
ANULADA

29. LETRA C 70. CORRETO

30. CORRETO 71- CORRETO

3i- ERRADO 72. ERRADO

32. CORRETO 73- ERRADO

33- ERRADO 74- ERRADO

34- ERRADO

35- CORRETO

36. ERRADO

37- CORRETO

38. CORRETO

39- CORRETO

40. ERRADO

4i- CORRETO

í. (CESPE / TRT8 - 2022) Em uma API RESTful, cada solicitação deve conter todos os dados necessários ao seu atendimento para não depender de informações armazenadas em outras sessões, o que caracteriza uma restrição de:
a) cache.

b) arquitetura cliente-servidor.

c) interface uniforme.

d) sistema de camadas.

e) comunicação stateless.

2. (CESPE / TRT8 - 2022) O método que serve para depuração em HTTP, ao instruir o servidor a enviar de volta a solicitação, é o:
a) options b) get c) trace d) connect e) post
3. (CESPE / FUNPRESP-EXE - 2022) SOAP (Simple Object Access Protocol) é um protocolo de comunicação usado para a troca de mensagens XML entre o cliente e o provedor de serviço.
4. (CESPE / FUNPRESP-EXE - 2022) UDDI (Universal Description Discovery and
Integration) é um padrão utilizado em SOA para a criação de repositórios de descrição de serviços.
5. (CESPE / FUNPRESP-EXE - 2022) Um documento WSDL possui um conjunto de elementos de nós abstratos e concretos que especificam a localização de um serviço.
6. (CESPE / Petrobrás - 2022) Web service é um sistema de software projetado para suportar interação entre máquinas através de uma rede; esse sistema possui uma interface descrita em formato processável por máquina, especificamente o WSDL (web services descriptor language).
7. (CESPE / Petrobrás - 2022) Uma das vantagens do SOAP é a sua utilização correta dos métodos
HTML (PUT, GET, POST, DELETE), enquanto o REST utiliza apenas o método POST para realizar as requisições através de um arquivo XML.
8. (CESPE / Petrobrás - 2022) Os protocolos SOAP e REST são os padrões mais utilizados na comunicação entre os sistemas por meio do web service; esses protocolos, unidos à estrutura básica XML, compõem a estrutura básica dos web services.
0 0

9. (CESPE / DPE-RO - 2021) O REST emprega um protocolo universal, o HTTP, para oferecer um serviço web simples e aberto. Verbos HTTP são usados para realizar chamadas e indicar para o serviço que ação deve ser realizada. Assinale a opção que indica o verbo usado tipicamente para a atualização de um recurso existente:
a) PUT.

b) CREATED.

c) GET.

d) POST.

e) TRACE.

A respeito de tecnologia de integração com RESTful, julgue os itens a seguir.

10. (CESPE / SERPRO -2021) Webservices possibilitam tanto a recuperação do estado atual de um recurso quanto a exclusão do recurso.
11. (CESPE / SERPRO - 2021) O protocolo de comunicação HTTP e a identificação de recursos podem ser utilizados por meio de URL (Uniform Resource Locator).
12. (CESPE / SERPRO -2021) As interações acontecem sem controle de estado, o que é conhecido como stateless.
13. (CESPE / SERPRO - 2021) A arquitetura RESTful não possibilita o uso de servidores intermediários, chamados de balanceadores de carga, razão por que o cliente sempre se conecta ao servidor final.
14.(CESPE/ MEC-2020) REST usa um modelo centrado em recursos de serviços encapsulados,
em que cada recurso fornecido pelo serviço possui uma URL e todos os recursos oferecem suporte a uma interface uniforme.
15. (CESPE / SLU-DF - 2019) Um web service pode assumir o papel de provedor de serviço e de consumidor de serviço.
16. (CESPE / SEFAZ-BA-2019) Os web services são componentes de software na web que podem fornecer determinados serviços a aplicações criadas em diferentes linguagens. Podem usar o protocolo SOAP para transferência de mensagens em formato XML. Para descrever a estrutura destas mensagens geralmente utiliza-se:
a) REST.

b) WSDL.

c) CORBA.

d) RESTFUL.

e) HTML.

17. (CESPE / TRT-CE - 2019) Assinale a opção que apresenta o método HTTP que deve ser usado para a busca de recursos por meio do web service RESTful.
a) delete b) get c) put d) options
18. (CESPE / BNB - 2018) SOAP utiliza um sistema de mensagens SMTP sobre a camada de transporte.
19. (CESPE / MPE-PI - 2018) Para implementar um web service de baixo overhead que tenha recursos identificáveis e localizáveis por meio de uma URI (Uniform ResourceIdentifier)
mediante o protocolo HTTP, pode-se utilizar o REST (Representational State Transfer).

20. (CESPE / STJ - 2018) Web service é uma solução utilizada na integração de sistemas e na comunicação entre aplicações diferentes.
21. (CESPE / STJ -2018) Os serviços Web RESTful utilizam o HTTP como um meio de comunicação entre cliente e servidor.
22. (CESPE / STJ - 2018) A REST define uma arquitetura cliente-servidor na qual o servidor não mantém contexto de cliente entre transações, ou seja, é stateless e toda transação contém as informações necessárias para satisfazer a solicitação.
23. (CESPE / STM - 2018) O SOAP é um tipo de modelo de dados XML elaborado para facilitar a inserção de campos HTML em páginas web.
24. (CESPE / SEDF - 2017) Serviços expressos por meio de contratos web services têm o potencial de evitar completamente a transformação, objetivo-chave dos contratos de serviços padronizados.
25. (CESPE / TRE-BA - 2017) No que se refere a web services, assinale a opção correta.

a) As solicitações e respostas XML trafegam no protocolo HTTP, não sendo possível utilizá-las nos protocolos FTP e SMTP.
b) Um dos componentes de um Web Service SOAP (Simple Object Access Protocol) é a UDDI
(Universal Description, Discovery and Integration), a qual é um arquivo do tipo XML que descreve detalhadamente um Web Service, especificando como deve ser o formato de entrada e saída de cada operação.
c) As duas formas de envio de mensagem para que um cliente possa efetuar solicitações a umWeb Service são One-Way Messaging e Request-Response Messaging.

d) O WSDL (Web Services Description Language) é uma linguagem para o desenvolvimento deWeb Services similar ao XML.

e) Os Web Services permitem a integração de sistemas, todavia dependem da linguagem de programação sob a qual tenham sido desenvolvidos e do sistema operacional do computador onde esses sistemas forem executados.
26.(CESPE /TRE-PE -2017) REST (Representational State Transfer) é:

a) um estilo de desenvolvimento que utiliza o protocolo HTTP e se baseia na interação simples entre cliente e servidor.
b) um software de infraestrutura em um sistema distribuído que auxilia no gerenciamento de interações entre entidades distribuídas em serviços web.
c) uma linguagem web voltada a definição de predicados que se apliquem a classes de objetos e de interações em um modelo UML.
d) uma linguagem de programação com tipos dinâmicos, voltada principalmente para desenvolvimento de aplicações web.
e) um modelo de desenvolvimento de software estruturado e organizado como um conjunto de classes de objeto e de relações entre essas classes.
27. (CESPE / MEC-2016) A respeito dos conceitos de web services e REST, assinale a opção correta.

a) O método POST é utilizado na atualização de um recurso existente.

b) Pode-se utilizar qualquer meio de transporte existente para o envio de uma requisição,incluindo HTTP, SMTP e TCP.

c) O modelo REST impõe restrições ao formato da mensagem.

d) Ao desenvolver uma aplicação, o recurso é transferido pela rede.

e) As chamadas às URIs (uniform resource indicator) são feitas por meio de métodos
HTTP, os quais indicam para o serviço a ação a ser realizada com o recurso.
28. (CESPE / TRE-MT - 2016) Acerca de REST (representational state transfer), assinale a opção correta.
a) O protocolo REST utiliza SOAP e XML.

b) REST utiliza recurso não identificável baseado em PUT e GET.

c) REST pode ser utilizado para implementar WebServices de baixo overhead.

d) Embora opcionalmente, um recurso REST pode conter uma URI.

e) REST consiste em um estilo de desenvolvimento baseado em complexa interação cliente/servidor.
29. (CESPE/ TCE-PA - 2016) Os web services devem ser projetados para ser utilizados independentemente de paradigmas de programação.
30. (CESPE/ TCE-PA - 2016) Para que um web service funcione corretamente,
os softwares cliente/servidor devem ser escritos na mesma linguagem.
31. (CESPE/ TCE-PA - 2016) Ao se usar o protocolo SOAP (Simple Object Access
Protocol), cada solicitação e cada resposta são colocadas em um envelope SOAP, nos momentos de invocação e retorno de um web service, respectivamente.
32. (CESPE / MEC - 2015) Entre as restrições da REST está a interface uniforme, a qual requer que um serviço ofereça várias operações e aguarde a solicitação dessas operações pelo servidor.
33. (CESPE / MEC -2015) Afim de implementar serviços em REST, recomenda-se utilizar os
WSDL
já existentes com mínima alteração do cabeçalho, informando somente que o protocolo a ser utilizado é o REST.
34. (CESPE / MEC-2015) As principais características do REST(Representationl State
Transfer) são interface uniforme, stateless e cache.
35. (CESPE/ MEC - 2015) Em uma web service, a linguagem de implementação e a plataforma utilizada são relevantes para os clientes.
36. (CESPE / ANTAQ-2014) Em arquiteturas REST, nenhum contexto de cliente pode ser mantido em servidor.
37. (CESPE / ANATEL - 2014) REST é uma técnica de engenharia de software para sistemas hipermídia distribuídos. De acordo com essa técnica, o estado da informação deve ser mantido no cliente, e o servidor não deve guardar o estado da comunicação de nenhum cliente que se comunique com o servidor, além de uma única requisição.
38. (CESPE / CNJ - 2013) Uma das formas de comunicação para encapsular dados transferidos no formato XML para aplicações serviço web (Webservice) é o SOAP (Simple ObjectAccess
Protocol).

39. (CESPE / CNJ - 2013) A linguagem WSDL é utilizada para descrever web services limitadas ao tipo request-response.
40. (CESPE / CNJ - 2013) Nos registros de negócio UDDI, a descrição da forma de acesso aos web services é um procedimento contido nas páginas verdes (green pages).
41. (CESPE / CNJ - 2013) Um dos elementos de uma mensagem SOAP é o corpo (body),
no qual devem estar contidas as informações de erro e status.
42. (CESPE / ANTT - 2013) Web Services provêm um meio padrão para interoperação entre diferentes aplicativos de software, que podem ser executados em uma variedade de plataformas e(ou) frameworks.
43. (CESPE / TCE-RO - 2013) O SOAP permite a troca de mensagens estruturadas em ambiente distribuído e descentralizado, com o uso de tecnologias XML. Essas mensagens podem ser trocadas por uma variedade de protocolos subjacentes como, por exemplo, o HTTP.
44-(CESPE / SERPRO - 2013) A comunicação entre sistemas clientes e servidores para troca de mensagens pode ser realizada por meio de SOAP (Simple Object Access Protocol), que é um protocolo para troca de informações estruturadas independente de linguagem de programação.
45. (CESPE / CNJ - 2013) Uma das formas de comunicação para encapsular dados transferidos no formato XML para aplicações serviço web (webservice) é o SOAP (Simple ObjectAccess
Protocol).

46. (CESPE / TRE-MS - 2013) O WS-Security propõe uma série de extensões para aprimorar a segurança dos web services no UDDI e no WSDL. Por questão de compatibilidade, essas extensões não afetam os cabeçalhos do envelope SOAP.
47. (CESPE / BACEN - 2013) O estilo arquitetural REST define um conjunto de restrições para uma aplicação, como, por exemplo, utilização de arquitetura par-a-par, manutenção de informações de estado, não uso de cache no cliente e apresentação de uma interface uniforme.
48. (CESPE / SERPRO - 2013) Um web service pode ocorrer sobre o HTTP (Hypertext
Transfer
Protocol), utilizando-se os serviços RESTfull (Representational State Transfer).

49. (CESPE / STF - 2013) A REST (Representational State Transfer), protocolo de comunicação embasado em XML, permite a comunicação de mensagens entre aplicações por meio de qualquer protocolo de comunicação em rede. Normalmente, esse protocolo é utilizado na integração de sistemas legados.
50. (CESPE / MPU - 2013) Web services é um método de comunicação entre serviços na
Web que aderem estritamente ao XML, como é o caso de serviços cuja comunicação é baseada na interface da arquitetura REST.
51. (CESPE / PEFOCE - 2012) SOAP é um protocolo leve destinado à troca de informações estruturadas em um ambiente distribuído e descentralizado. Uma mensagem SOAP,por exemplo, é um documento XML composto de três partes obrigatórias: envelope, cabeçalho e corpo.
52. (CESPE / MPE-PI - 2012) Em web services, utiliza-se o protocolo SOAP (Simple
Object Access
Protocol) para a comunicação entre os serviços.

53. (CESPE / TJ-RO - 2012) Representational state transfer (REST), que utiliza o WSDL
como linguagem de descrição de serviços, é uma forma de implementação de SOA na web.
54. (CESPE / MEC - 2011) O UDDI (Universal Description Discovery and
Integration), que corresponde a um registro de web services, é dividido em páginas brancas, amarelas e verdes,nas quais são prestadas aos clientes informações sobre a empresa, os serviços por ela oferecidos e as especificações WSDL desses serviços.
55. (CESPE / PREVIC - 2011) No WSDL (Web Services Definition Language), é prescrito o leiaute de banco de dados com descrições de serviços, por meio das quais os clientes de web service podem procurar serviços relevantes.
56. (CESPE / PREVIC-2011) Web Services são sistemas embasados na Web que oferecem serviços gerais para aplicações remotas, não requerendo interações imediatas de usuários finais.
57. (CESPE I MEC -2011) Em formulários HTML, apenas o método post é suportado; o método get é utilizado em aplicações JavaScript.
58. (CESPE / MEC -2011) Um web service pode ser desenvolvido, também, com o uso de REST, que utiliza o protocolo HTTP para comunicação entre emissor e destinatário, e oSOAP, para encapsular as mensagens trafegadas.
59. (CESPE / MPU - 2010) REST (Representationals State Transfer) é uma tecnologia que está sendo utilizada em web services, como substituta das tecnologias SOAP (Simple ObjectAccess
Protocol) e WSDL.

60. (CESPE / TCU - 2010) Uma equipe de desenvolvimento de software recebeu a incumbência de desenvolver um sistema com as características apresentadas a seguir.
- O sistema deverá ser integrado, interoperável, portável e seguro.

- O sistema deverá apoiar tanto 0 processamento online, quanto 0 suporte a decisão e gestão de conteúdos.
- O sistema deverá ser embasado na plataforma JEE (Java enterprise edition) v.6,
envolvendo servlets, JSP (Java server pages), Ajax, JSF (Java server faces) 2.0, Hibernate 3.5,SOA e web services.
0 líder da equipe iniciou, então, um extenso processo de coleta de dados com o objetivo de identificar as condições limitantes da solução a ser desenvolvida e tomar decisões arquiteturais e tecnológicas que impactarão várias características funcionais e não funcionais do sistema, ao longo de seu ciclo de vida. A partir dessa coleta, o líder deverá apresentar á equipe um conjunto de informações e de decisões.
Com relação às diferentes arquiteturas e tecnologias que, se escolhidas,
impactarão as características do sistema descrito no texto, julgue o item:
O estilo de arquitetura de software denominado REST (Representational State
Transfer)
demanda mais recursos computacionais que o modelo de desenvolvimento de sistemas embasado em SOAP (Single Object Access Protocol), por isso não é recomendável a adoção do padrão REST de arquitetura de software no desenvolvimento do sistema em questão.
61. (CESPE / MPU - 2010) A descrição de um web service é feita utilizando-se WSDL
(Web Services
Description Language), que é uma linguagem embasada em RPC (Remote Procedure Call) e
UDDI (Universal Description Discovery and Integration), com a qual se descreve a forma de acesso dos serviços e seus parâmetros de entrada e de saída.
62. (CESPE /TRE-MT-2010) Com relação a web services, assinale a opção correta.

a) As arquiteturas de aplicação de web services são arquiteturas firmemente acopladas,
nas quais as ligações entre serviços não podem mudar durante a execução.
b) SOAP (Simple Object Access Protocol) é um protocolo com base em HTML que permite troca de informações entre aplicações em um ambiente distribuído.
c) UDDI (Universal Description, Discovery and Integration) é um diretório para armazenamento de informações a respeito de web sevices. Essas informações são descritas em SOAP.
d) A linguagem WSDL (Web Services Description Language) é utilizada para descrever web services.
e) Segundo o W3C (World Wide Web Consortium), web services são apropriados somente para aplicações em que componentes de um sistema distribuído são executados em plataformas semelhantes de um mesmo fornecedor.
63.CESPE / ANATEL - 2009) Os três padrões fundamentais que possibilitam comunicações entre web services são: Simple Object Access Protocol (SOAP) — protocolo que define uma organização para a troca estruturada de dados entre web services; Web ServicesDescription
Language (WSDL) — protocolo que define como as interfaces dos Web Services podem ser representadas; Universal Description, Discovery And Integration (UDDI) —padrão de descoberta que define como são organizadas as informações de descrição do serviço,
permitindo que os solicitantes descubram os serviços. Um desses padrões não utiliza a
XML
(Extensible Mark-up Language).

64. (CESPE / CEHAP-PB - 2009) São padrões de Web Services o SOAP, o WSDL e o UDDI,
todos baseados em HTTP.
65. (CESPE/INMETRO-2Oog) Na SOA, a descrição do serviço é mantida em um repositório
WSDL,
em formato UDDI (Universal Description, Discovery and Integration).

66. (CESPE / ANTAQ - 2009) Nos serviços web, clientes e servidores, direta ou indiretamente,podem acessar documentos UDDI completos por meio de seus URIs (Uniform
Resource
Identifier), usando um serviço de diretório, tal como o WSDL.

67. (CESPE / ANTAQ - 2009) Um componente importante da arquitetura de serviços web é formado por um serviço de diretório que armazena descrições de serviços. Esse serviço deve obedecerão padrão UDDI (Universal Description, Discovery And Integration).
68. (CESPE / ANTAQ - 2009) E m serviços web, o SOAP pode ser transportado por protocolos como REST, HTTP, SMTP e JMS.
69. (CESPE / TRT-BA - 2008) O UDDI é uma especificação técnica que tem como objetivo descrever, descobrir e integrar web services; é embasado na tecnologia XML, que fornece uma plataforma neutra de dados e permite descrever relações hierárquicas de modo natural.
70. (CESPE / STJ - 2008) O serviço UDDI fornece uma interface para publicar e atualizar informações acerca de serviços web; possibilita pesquisar descrições WSDL pelo nome;provê uma interface que possibilita executar consultas de modo a recuperar uma entidade que corresponda a uma chave ou recuperar entidades que correspondam a um conjunto de critérios de busca.
71. (CESPE / STJ - 2008) O WSDL separa a parte abstrata de uma descrição de serviço da parte concreta; nessa descrição, a parte concreta contém as definições de tipos usados pelo serviço e a parte abstrata especifica como e onde o serviço pode ser contatado. Os documentosWSDL
podem ser acessados via um serviço de diretório como o UDDI; as definições WSDL podem ser geradas a partir de definições de interfaces escritas em outras linguagens.
72. (CESPE / STJ - 2008) O SOAP encapsula mensagens que podem ser transmitidas via
HTTP;
permite o modelo de interação cliente-servidor; define como usar XML para representar mensagens de requisição e resposta. Um documento XML é transportado no corpo de uma mensagem SOAP; no modelo cliente-servidor, o corpo de uma mensagem SOAP pode conter uma requisição, mas não uma resposta.
73. (CESPE / MPE-AM -2008) No protocolo HTTP (Hypertext Transfer Protocol), o método
GET é utilizado em solicitações enviadas pelo servidor ao navegador para que este solicite dados ao usuário de uma página ou para que o próprio navegador forneça os dados solicitados.
GABARITo

1. LETRA E 42. CORRETO

2. LETRA C 43- CORRETO

3- CORRETO 44. CORRETO

4- CORRETO 45- CORRETO

5- CORRETO 46. ERRADO

6. CORRETO 47- ERRADO

7- ERRADO 48. ANULADA

8. CORRETO 49- ERRADO

9- LETRA A 50. ERRADO

10. CORRETO 51- ERRADO

li. ERRADO 52. CORRETO

12. CORRETO 53- ERRADO

13- ERRADO 54- CORRETO

14- CORRETO 55- ERRADO

15- CORRETO 56. CORRETO

16. LETRA B 57- ERRADO

17- LETRA B 58. ERRADO

i8. ERRADO 59- ERRADO

19- CORRETO 60. ERRADO

20. CORRETO 61. ERRADO

21. CORRETO 62. LETRA D

22. CORRETO 63. ERRADO

23- ERRADO 64. ERRADO

24. ERRADO 65- ERRADO

25- LETRAC 66. ERRADO

26. LETRA A 67. CORRETO

27- LETRA E 68. ANULADA

28. LETRAC 69. CORRETO

29. CORRETO 70. CORRETO

30. ERRADO 7i- ERRADO

31- CORRETO 72. ERRADO

32. ERRADO 73- ERRADO

33- ERRADO

34- CORRETO

35- ERRADO

36. CORRETO

37- CORRETO

38. CORRETO

39- ERRADO

40. CORRETO

41. ERRADO

QUESTõES CoMENTADAS - FC V

í. (FGV / TJDFT - 2022) No âmbito de Web services, analise as afirmativas a seguir sobre a abordagem REST e o uso de tecnologias baseadas em SOAP.
I. Uma característica dos serviços Web RESTful é a capacidade de transmitir dados diretamente via HTTP.
II. As mensagens SOAP precisam ser retornadas como documentos XML.

III. Um navegador não pode armazenar em cache uma solicitação concluída por uma API SOAP.
É correto o que se afirma em:

a) somente II;

b) somente I e II;

c) somente I e III;

d) somente II e III;

e) I, lie III.

2. (FGV / TJDFT - 2022) O analista de sistemas Pedro desenvolveu o webservice RService aplicando o estilo de arquitetura REST (Representational State Transfer). As aplicações clientes que utilizam o RService são desenvolvidas de forma desacoplada e dissociada de RService e manipulam os recursos de RService através de representações transferidas em mensagens autodescritivas.
Para habilitar a independência no desenvolvimento de aplicações clientes com o uso de representações em mensagens autodescritivas, Pedro aplicou em RService o princípio REST:
a) arquitetura cliente-servidor;

b) código sob demanda;

c) interface uniforme;

d) sistema em camadas;

e) capacidade de cache.

3. (FGV / TJDFT - 2022) Kátia é uma web designer contratada para fazer uma página web para oTribunal de Justiça. Ela fará uso do protocolo HTTP, pois este é um protocolo da camada de aplicação, o qual executa sob o TCP e associado à web. As operações nesse protocolo são chamadas de métodos. Kátia, então, testa o envio da página pelo servidor, cria uma coleção de páginas web em um servidor remoto e instrui o servidor a enviar de volta a solicitação.
Para implementar a página web, Kátia deve usar, respectivamente, os métodos:

a) POST, HEAD, DELETE;

b) GET, CONNECT, TRACE;

c) PUT, CONNECT, OPTIONS;

d) POST, HEAD, OPTIONS;

e) GET, PUT, TRACE.

4. (FGV/ FUNSAÚDE - 2021) Com relação ao HTTP no contexto de aplicações web,
assinale a lista que contém dois dos métodos desse protocolo.
a) CONNECT e EXIT.

b) GETePOST.

c) OPEN e CLOSE.

d) READ e WRITE.

e) STARTe END.

5. (FGV / Prefeitura de Niterói-RJ -2018) As tecnologias SOAP e REST são largamente utilizadas para troca de informações estruturadas em sistemas distribuídos. Sobre essas tecnologias,analise as afirmativas a seguir.

I. REST pressupõe que cada solicitação do cliente ao servidor deve contertodas as informações necessárias para processar o pedido e não pode tirar proveito de qualquer contexto armazenado no servidor.
II. As mensagens SOAP são documentos XML construídos especificamente para trafegar através do protocolo de transporte HTTP/HTTPS.
III. REST é mais eficiente que o SOAP porque utiliza exclusivamente mensagens menores no formato JSON.
Está correto o que se afirma em:

a) I, apenas.

b) II, apenas.

c) III, apenas.

d) I e II, apenas.

e) I, lie III.

6. (FGV/AL-RO-2018) O padrão REST define um conjunto de restrições e propriedades baseado em HTTP. Sobre REST, analise as afirmativas a seguir.
I. Web services que obedecem ao padrão REST precisam utilizar o formato
JSON para encapsular os dados da resposta às requisições dos sistemas solicitantes.
II. Os métodos GET, POST, PUT e DELETE do protocolo de comunicação HTTP são compatíveis com operações CRUD para a persistência de dados.
III. O padrão REST pressupõe que requisições de um mesmo sistema solicitante são dependentes, permitindo manter o estado de cada solicitante durante várias solicitações.
Está correto o que se afirma em:

a) I, somente.

b) II, somente.

c) III, somente.

d) I e II, somente.

e) I, lie III.

7. (FGV / AL-RO - 2018) SOAP é um protocolo para troca de informações estruturadas. Sobre a estrutura da mensagem SOAP, analise as afirmativas a seguir.
I. O formato da mensagem é baseado na linguagem de marcação XML.

II. Os elementos Header e Body são filhos obrigatórios do elemento Envelope.

III. O elemento Fault é opcional e quando estiver presente deve aparecer como um elemento filho do elemento Envelope.
Está correto o que se afirma em:

a) I, somente.

b) II, somente.

c) III, somente.

d) I e III, somente.

e) I, lie III.

8. (FGV / BANESTES - 2018) Sobre os princípios do padrão REST, analise as afirmativas a seguir.

I. As mensagens REST são documentos texto no formato JSON.

II. REST é independente do protocolo de transporte, podendo ser implementado com HTTP,
SMTPou JMS.

III. Serviços REST são stateless, isto é, cada solicitação deve conter todas as informações necessárias para ser compreendida pelo servidor.
Está correto o que se afirma em:

a) somente I;

b) somente II;

c) somente III;

d) somente I e III;

e) I, lie III.

9. (FGV / BANESTES - 2018) A linguagem baseada em XML utilizada para descrever um web service, suas operações e como acessá-lo é:
a) XSLT

b) XSD

c) DTD

d) WSDL

e) UDDI

10. (FGV / BANESTES -2018) Sobre a implementação de serviços web com padrão SOAP,
analise as afirmativas a seguir.
I. As mensagens SOAP são documentos XML.

II. A dependência do SOAP ao protocolo de transporte HTTP é uma restrição para implementação deste padrão.
III. O padrão é inadequado para troca de informações em uma plataforma descentralizada e distribuída.
Está correto o que se afirma em:

a) somente I;

b) somente II;

c) somente III;

d) somente I e II;

e) I, lie III.

11. (FGV / BANESTES - 2018) Usualmente, WebServices envolvem a utilização dos padrões
XML,
SOAP e WSDL. A função de cada um deles é, respectivamente:

a) descrever os parâmetros, disponibilizar o serviço, transferir as mensagens;

b) transferir as mensagens, descrever o algoritmo, transportar as mensagens;

c) rotular e formatar os dados, transferir as mensagens, descrever a disponibilidade do serviço;

d) transferir as mensagens, descrever a disponibilidade do serviço, formatar os parâmetros;

e) descrever as classes e suas interfaces, instanciar os objetos, descrever os algoritmos.

12. (FGV / IBGE - 2017) SOAP (Simple Object Access Protocol) é um protocolo de comunicação projetado para permitir a troca de informações de maneira estruturada entre sistemas distribuídos. Em relação à estrutura da mensagem SOAP versão 1.2 definida pela W3C,analise as afirmativas a seguir:
I. A mensagem SOAP é definida em um documento XML que contém um elemento raiz denominado Envelope.
II. Header é um elemento mandatório que fornece informações específicas para autenticação.

III. Error é um elemento opcional que contém as informações dos erros ocorridos no envio da mensagem.
Está correto o que se afirma em:

a) somente I;

b) somente II;

c) somente III;

d) somente I e III;

e) I, lie III.

13. (FGV / IBGE - 2017) Com relação a REST e SOAP, analise as afirmativas a seguir:

I. REST é baseado em orientação a recursos, sendo indicado para operações stateless.

II. SOAP é um protocolo para troca de mensagens estruturadas, que podem possuir diferentes formatos, tais como JSON, HTML ou XML.
III. Tanto REST quanto SOAP foram concebidos para utilizar diferentes protocolos de comunicação, além do HTTP.
Está correto somente o que se afirma em:

a) I;

b) II;

c) Hl;

d) I e II;

e) I e III.

14. (FGV / IBGE - 2017) SOAP (Simple Object Access Protocol) é um protocolo de comunicação utilizado para troca de informações estruturadas entre sistemas computacionais.Analise as afirmativas a seguir sobre a estrutura de uma mensagem SOAP:
I. É codificada como um documento XML e o elemento <Envelope> é o elemento-raiz da mensagem.
II. O elemento <Header> é opcional e o elemento <Body> obrigatório.

III. O elemento <Fault> é utilizado para transportar informações de erro dentro de uma mensagem SOAP.
Está correto o que se afirma em:

a) somente I;

b) somente II;

c) somente III;

d) somente I e III;

e) I, lie III.

15. (FGV / IBGE - 2016) Uma mensagem no protocolo SOAP, versão 1.2, é representada por um documento XML capaz de transportar dados de serviços Web. Os elementos considerados opcionais são:
a) Title e Meta;

b) Envope e Body;

c) Header e Fault;

d) Model e Control;

e) Footer e Namespace.

16. (FGV / DPE-RO - 2015) A REST (Representational State Transfer, em português
Transferência de Estado Representacional) dá ênfase:
a) na multiplicidade de representação de recursos, utilizando apenas os métodos padrão do protocolo HTTP (GET, POST, PUT, DELETE, etc);
b) na multiplicidade de representação de métodos, utilizando apenas os recursos padrão do protocolo HTTP (GET, POST, PUT, DELETE, etc);
c) em utilizar o protocolo SOAP sobre o protocolo HTTP;

d) na segurança por meio do protocolo HTTPS 2.0;

e) na integração baseada em troca de mensagens assíncronas por meio de web-sockets.

17. (FGV / DPE-RO - 2015) A função da WSDL (Web Services Description Language -
Linguagem de Descrição de Serviços Web) é:
a) executar métodos de um serviço SOAP;

b) descrever um serviço Web, informando o local do serviço e os métodos expostos por ele;

c) descrever os objetos de um Serviço REST;

d) linguagem de programação para serviços SOAP;

e) linguagem de programação para XML.

i8.(FGV / TJ-GO - 2014) Mensagem utilizada para comunicação com um Serviço Web (Web
Service), implementado com o protocolo SOAP 1.2.

< soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope">
< soap:Header>

< m:Trans xmlns:m=http://www.w3schools.com/transaction/
soap:mustUnderstand="false" >234 < /m:Trans >

< /soap:Header>

< soap:Body xmlns:m="http://www.example.org/stock" >

< m:GetStockPrice >

< m:StockName>IBM

< /mzGetStockPrice >

< /soap:Body >

< /soap:Envelope >

0(s) elemento(s) que pode(m) ser retirado(s) da mensagem, de acordo com a especificação do protocolo SOAP, sem prejuízo para a comunicação com o Serviço Web, é/são:
a) soap:Envelope;

b) soap:Headere soap:Body;

c) soap:Body e soap:Envelope;

d) soap:Header;

e) soap:Body.

ig.(FGV/AL-MA-2013) Com relação à especificação SOAP versão 1.2, assinale V para a afirmativa verdadeira e F para a falsa.
() O elemento "SOAP HEADER" é obrigatório em qualquer mensagem SOAP.

() A especificação SOAP fornece um modelo de processamento distribuído, o qual assume que uma mensagem SOAP é originada em um remetente inicial SOAP e é enviada para um receptorSOAP final, através de zero ou mais intermediários SOAP.

( ) A ocorrência de falhas em uma mensagem SOAP é indicada pelo elemento
"SOAP
EXCEPTION".

As afirmativas são, respectivamente,

a) F, V e F.

b) F, V e V.

c) V, F e F.

d) V, V e F.

e) F, F e V.

20. (FGV / Senado Federal - 2012) A respeito de mensagens SOAP, assinale a alternativa correta.

a) O elemento Envelope deve usar o namespace "http://www.w3.org/2oo1/12/soap-envelope".

b) O elemento Envelope não é obrigatório em uma mensagem SOAP.

c) O elemento Body não é obrigatório em uma mensagem SOAP.

d) O elemento Fault é obrigatório em uma mensagem SOAP.

e) O elemento Header é obrigatório em uma mensagem SOAP.

21. (FGV / SEAD-AP - 2010) Originalmente SOAP representava um protocolo para troca de informações estruturadas em uma plataforma descentralizada e distribuída, utilizando tecnologias baseadas em um determinada linguagem. Foi importante para o desenvolvimento de aplicações para permitiram a comunicação via Internet entre programas,empregando o
Remote Procedure Cal Is (RPC) entre objetos como DCOM e CORBA. Atualmente, SOAP provê um caminho de comunicação entre aplicações "rodando" em diferentes sistemas operacionais,com diferentes tecnologias e linguagens de programação.

De acordo com o enfoque do World Wide Web Consortium - W3C, as mensagens SOAP são documentos baseados na seguinte linguagem:
a) WSDL

b) XML

c) JAVASCRIPT

d) AJAX

e) XSLT

22. FGV / MEC - 2009) Um Web Service é definido pela W3C como um sistema de software projetado para fornecer interoperabilidade entre máquinas em uma determinada rede. Dentro do contexto dos Web Services assinale a alternativa correta.
a) A UDDI (Universal Description, Discovery, and Integration) é uma linguagem baseada emXML que descreve o que um Web Service pode fazer, onde ele reside e como chamá-lo.

b) SOAP (Simple Object Access Protocol) é um protocolo, baseado em XML, para troca de informação estruturada com Web Services em redes de computadores.
c) A interoperabilidade entre os Web Services e aplicações é garantida devido ao uso obrigatório da linguagem Java na implementação das aplicações.
d) SOA (Simple Object Access) é uma plataforma de arquitetura orientada a serviços,
utilizada como base para suportar os Web Services.
e) A WSDL (Web Services Description Language) é uma especificação para publicar e localizar informações sobre Web Services.
23. (FGV / MEC - 2009) A respeito das tecnologias relacionadas a Web Services, analise as afirmativas a seguir:
I. A UDDI é uma plataforma de arquitetura orientada a serviços assíncronos utilizada como base para suportar os Web Services.
II. A WSDL (Web Services Description Language) é uma interface de programação que permite a execução de chamadas remotas no estilo RPC.
III. SOAP (Simple Object Access Protocol) é um protocolo, baseado em XML, para troca de informação estruturada com Web Services em redes de computadores.
Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente a afirmativa II estiver correta.

c) se somente a afirmativa III estiver correta.

d) se somente as afirmativas II e III estiverem corretas.

e) se todas as afirmativas estiverem corretas.

24. (FGV / Senado Federal - 2008) Considere as assertivas a seguir sobre as relações entre SOAP,
WSDLeUDDI:

I. UDDI é um diretório de serviços web descrito por WSDL.

II. WSDL pode ser usado para descrever serviços SOAP.

III. O UDDI é um diretório de descrições SOAP.
As assertivas corretas são:

a) somente I.

b) somente I e II.

c) somente I e III.

d) somente II e III.

e) I, lie III.

GABARITo

1. LETRAC 9- LETRA B
17- LETRA E

2. CORRETO 10. LETRA A
i8. LETRA C

3- LETRA B li. LETRAC
19. LETRA A

4- LETRA E 12. LETRA D
20. LETRA B

5- LETRA C 13- LETRA A
21. LETRA D

6. LETRA E 14- LETRAC
22. LETRA A

7- LETRA B x5- LETRA A
23- LETRA A

8. LETRA A i6. LETRA A
24- LETRA B

QUESTõES CoMENTADAS - DIvERSAS BANCAS

í. (FAURGS / BANRISUL - 2018) Quais são as quatro operações para realizar tarefas definidas pelo serviço web no formato REST?
a) CREATE, GET, PUT e UPDATE

b) PUT, UPDATE, INSERT e DELETE

c) POST, GET, PUT e DELETE

d) PUT, GET, INSERT e DELETE

e) SELECT, GET, PUT e DELETE

2. (IBFC / TJ-PE - 2017) Existe a necessidade em um documento XML ser identificado como uma mensagem SOAP. A estrutura da mensagem SOAP (Simple Object Access Protocol), em um documento XML, contém os seguintes elementos:
a) Title (obrigatório) - Head (opcional) - Body (obrigatório)

b) Envelope (obrigatório) - Header (opcional) - Main (obrigatório)

c) Title (obrigatório) - Head (opcional) - Main (obrigatório)

d) Envelope (obrigatório) - Header (opcional) - Body (obrigatório)

e) Envelope (obrigatório) - Head (opcional) - Main (obrigatório)

3. (IBFC / EBSERH - 2017) Assinale a alternativa que apresenta o serviço de diretório onde empresas podem registrar (publicar) e buscar (descobrir) por Serviços Web (Web Services):
a) UDDI

b) NIS

c) WSDL

d) X.500

e) LDAP

4. (IBFC / EBSERH -2017) Web service é uma solução utilizada na integração de sistemas. Os Web services são componentes que permitem às aplicações enviar e receber dados, como padrão,em formato:

a) NAT

b) ARP

c) XML

d) TLS

e) XDR.

5. (IBFC / EBSERH - 2017) Conforme o W3C (World Wide Web Consortium) pode-se definir umWeb Service como sendo:

a) uma estrutura conceituai para reger projetos de engenharia de software.

b) técnicas baseadas em formalismos matemáticos para a especificação,
desenvolvimento e verificação dos sistemas de softwares e hardwares.
c) um modelo de referência que contém práticas necessárias à manutenção do software.

d) um sistema de software projetado para suportar a interoperabilidade entre máquinas sobre rede.
e) um modelo de dados que representa um conjunto de conceitos dentro de um domínio e os relacionamentos entre estes.
6. (IBFC / EMDEC -2016) Quanto as tecnologias aplicadas em um Web Service temos:

"Para a representação e estruturação dos dados nas mensagens recebidas/enviadas é utilizado o . As chamadas às operações, incluindo os parâmetros de entrada/saída, são codificadas no protocolo. Os serviços (operações, mensagens, parâmetros,etc.) são descritos usando a linguagem. O processo de publicação/pesquisa/descoberta de WebServices utiliza o protocolo."

Assinale a alternativa que complete correta e respectivamente as lacunas:

a) SOAP - WSDL - UDDI - XML

b) WSDL - UDDI - XML - SOAP

c) UDDI-XML-SOAP-WSDL

d) XML - SOAP - WSDL - UDDI.

7. (CCV / UFC - 2016) Sobre Web Services, assinale a opção correta.

a) Web services não possui suporte a mensagens com arquivos binários.

b) WSDL é baseado em XML, enquanto SOAP é baseado em javascript.

c) WSDL e SOAP podem ser utilizados juntos para prover Web Services.

d) WDSL e SOAP não são recomendação do W3C (World Wide Web Consortium).

e) Um componente Web Service desenvolvido em linguagem Java não pode ser acessado por meio da linguagem PHP.
8. (IF-PI / IF-PI -2016) Trata-se de um protocolo de comunicação de web services descrito por umaWSDL (Web Services Description Language), ele consiste de um grande arquivo XMLtrafegando entre sistemas para realizar a comunicação. O conceito se refere ao:

a) SOAP.

b) OpenLDAP.

c) X25.

d) DHCP.

e) DNS.

9. (FUNIVERSA / IF-AP - 2016) SOAP (Simple Object Access Protocol) é um protocolo de comunicação que permite a troca de mensagens entre aplicações Web, geralmente usandoHTTP e Webservices. Assinale a alternativa que apresenta o formato das mensagens utilizadas pelo SOAP.
a) UDP (User Datagram Protocol)

b) TCP (Transmission Control Protocol)

c) XML (eXtensible Markup Language)

d) FTP (File Transfer Protocol)

e) ODF (Open Document Format)

10. (ESAF/ANAC-2016) São tecnologias essenciais para Web Services:

a) Protocolo HSTP. XML. SIP. WSDL. UMDI.

b) Protocolo HTTP. RML. SOAP. WDLL. UDDI.

c) Protocolo TC/IP. XML. SORP. WSDL. UDTS.

d) Protocolo HTIP. XDL. SO2AP. WSDD. UDDI.

e) Protocolo HTTP. XML. SOAP. WSDL. UDDI.

11. (FUMARC / AL-MG - 2014) Analise as seguintes afirmativas sobre os métodos HTML:

I. HTML POST é utilizado para enviar dados para serem processados em um servidor Web.

II. HTML GET solicita ao servidor apenas o cabeçalho de uma URL para que o cliente decida se deve requisitar o conteúdo completo ou não.
III. HTML PUT é utilizado para criar recursos dentro de um servidor Web.

Estão CORRETAS as afirmativas:

a) I e II, apenas.

b) I e III, apenas.

c) II e III, apenas.

d) I, lie III.

12. (MPE-RSI MPE-RS - 2012) Um formulário em HTML é um modelo de entrada de um conjunto de dados. O primeiro passo a ser dado para a construção de um formulário é fazer as etiquetas que desenham as janelas de entrada de dados. Os métodos que transferem dados do browser para o servidor são denominadose.
a) input-output b) post-get c) push - pop d) post-cat e) push - pull
13.(MPE-RS / MPE-RS - 2012) Considere as seguintes afirmações a respeito de REST(Representational State Transfer).

I. REST é um protocolo para troca de mensagens entre componentes de uma aplicação web.

II. REST é uma arquitetura, onde cada aplicação é um conjunto de recursos sobre os quais podemos realizar ações.
III. Os formatos dos arquivos utilizados numa aplicação que segue REST são JSON, XML
ou
YAML.

Quais estão corretas?

a) Apenas I.

b) Apenas II.

c) Apenas III.

d) Apenas I e III.

e) Apenas II e III.

14. (COPEVE-UFAL / ALGÁS - 2012) REST é uma técnica de engenharia de software utilizada no desenvolvimento de sistemas hipermídia distribuídos e adequada para a Web.
15. UFF / UFF - 2009) No tocante ao protocolo de transferência de hipertexto (HTTP), esse protocolo da categoria "solicitação e resposta" possui três métodos de solicitação. São eles:
a) HEAD, BODYeINIT;

b) FLAG, TOS e TTL;

c) GET, HEADePOST;

d) PUT, GETe INIT;

e) PUSH, POSTeHEAD.

16. (CESGRANRIO / PETROBRÁS - 2008) A interoperabilidade entre aplicações nos dias atuais é fortemente baseada no uso de web services. Duas abordagens arquiteturais distintas para o projeto e implementação de web services têm-se firmado no cenário de tecnologia. São elas:
a) REST e WS-*

b) SOAPeWSDL

c) RPCeRMI

d) SGML e HTML

e) B2B e B2C

i7.(CESGRANRIO / REFAP-ES - 2007) O estilo arquitetural REST (Representational State
Transfer) para WEB tem como característica:

a) permitir o uso de RPC diretamente sobre SSL, para aplicações seguras.

b) acelerar a transferência do FTP com a implementação de cache.

c) combater o SPAM, utilizando redes neurais como técnica de aprendizagem.

d) usar SOAP para interoperabilidade entre sistemas heterogêneos.

e) utilizar os métodos HTTP: GET, POST, PUT e DELETE.

GABARITo

1. LETRAC 7- LETRA C
13- LETRA E

2. LETRA D 8. LETRA A
14. CORRETO

3- LETRA A 9- LETRAC
15- LETRAC

4- LETRAC 10. LETRA E
16. LETRA A

5- LETRA D íi. LETRA B
17- LETRA E

6. LETRA D 12. LETRA B

