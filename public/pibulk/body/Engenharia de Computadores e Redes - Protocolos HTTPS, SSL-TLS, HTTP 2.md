# Engenharia de Computadores e Redes - Protocolos HTTPS, SSL-TLS, HTTP 2

Índice

1) Protocolos HTTP-HTTPS

2) Questões Comentadas - Protocolos HTTP-HTTPS - Cebraspe

3) Questões Comentadas - Protocolos HTTP-HTTPS - FCC

4) Lista de Questões - Protocolos HTTP-HTTPS - Cebraspe

5) Lista de Questões - Protocolos HTTP-HTTPS - FCC

6) SSL (Security Socket Layer) e TLS (Transport Layer Security)

7) Questões Comentadas - SSL (Security Socket Layer) e TLS (Transport Layer
Security) - Cebraspe 59

8) Questões Comentadas - SSL (Security Socket Layer) e TLS (Transport Layer
Security) - FCC 63

9) Lista de Questões - SSL (Security Socket Layer) e TLS (Transport Layer Security) - Cebraspe

10) Lista de Questões - SSL (Security Socket Layer) e TLS (Transport Layer Security) - FCC

PRoToCoLoS E TECNoLoGIAS DA CAMADA DE APLICAçÃo

Chegamos na etapa que será uma verdadeira sopa de letrinhas com diversos protocolos vinculados aos diversos tipos de serviços oferecidos via rede. As bancas cobram recorrentemente detalhes de cada tipo desses protocolos e por esse motivo, vamos esmiuçar um por um com vistas a termos um aprendizado completo sobre os assuntos.
PRoToCoLo HTTP

O protocolo HTTP (Hypertext Transfer Protocol) foi criado sob a perspectiva de ser utilizado de uma arquitetura CLIENTE-SERVIDOR. É um protocolo chave para a comunicação de dados na Internet que permite a navegação WEB.
Algumas questões trazem a definição crua do HTTP:

"Protocolo para a troca ou transferência de hipertexto utilizado em sistemas de hipermídia,distribuídos ou colaborativos."

Outra característica é a padronização de mensagens que os clientes enviam aos servidores e vice-versa.

Por ser baseado na arquitetura CLIENTE-SERVIDOR, utiliza o modelo de REQUISIÇÃO-RESPOSTA.
Utiliza ainda o conceito de sessão a nível de aplicação. O seu procedimento básico ocorre nas seguintes etapas:
* O cliente estabelece uma conexão TCP com o servidor, geralmente, na porta 80, sendo esta a porta padrão do protocolo;
* O servidor responde à mensagem indicando o estado corrente da requisição, além da versão suportada e outras informações do servidor;
* A partir de então, se não houver mensagem de erro, a conexão será estabelecida;

Utiliza codificação dos dados em textos ASCII, para que possam ser devidamente interpretados pelos servidores e clientes.
Para efeito de concurso, o HTTP possui 2 versões:

* HTTPvl.O - Não realiza conexões persistentes. Isto é, para cada troca de informação entre cliente e servidor, necessita-se estabelecer e encerrar uma nova conexão TCP;
* HTTPvl.l - Realiza conexões persistentes. Estabelece-se apenas uma requisição TCP
para a troca de diversas mensagens entre o cliente e servidor. Além disso, pode-se enviar mais de uma requisição sem necessariamente aguardar a confirmação da requisição anterior.
Além disso, é importante destacar que o HTTP em sua versão persistente pode trabalhar ainda de forma sequencial ou paralela. No primeiro caso, troca-se mensagens de requisição e resposta sempre par a par, ou seja, só se envia uma nova requisição depois do recebimento da referida resposta.
Já no modo paralelo (também conhecido como modo pipelining), pode-se apresentar várias requisições independentemente do recebimento das respostas. A figura abaixo representa todas as possibilidades.
Client Server Client Server Client
Server

Short-lived connections Persistent connection
HTTP Pipelining

Além disso, o protocolo HTTP é considerado um protocolo sem estado (stateless), pois não armazena informações do usuário.
Um ponto importante a mencionar é que o servidor pode enviar informações ao usuário com vistas a manter a sessão entre eles aberta, além de poder recuperar certas informações futuramente. Esse recurso pode ser provido com o uso de COOKIES, que podem ser armazenados no browser do cliente.
Assim tem-se um ambiente statefull, porém, vale lembrar que isso é um recurso complementar. OHTTP nativamente é stateless.

ESTRUTURA DA MENSAGEM HTTP

Como vimos, existem dois tipos de mensagem HTTP: requisição e resposta. Vamos verificar a estrutura de cada uma delas:
* Requisição: Pode ser dividida em 3 partes: linha de requisição, cabeçalho e corpo da entidade;
O método utilizado, o caminho do objeto e a versão do protocolo fazem parte da linha de requisição. Outras informações referentes ao nome da página, estado corrente da conexão,informações de navegador (User Agent) e línguas aceitas ficam por conta do cabeçalho.

Na requisição, o Corpo da Entidade é utilizado com o método POST uma vez que o cliente envia informações ao servidor para preenchimento do objeto de resposta.
A figura abaixo é um exemplo de composição da mensagem HTTP:

GET /index.html HTTP/1.1

Date: Thu, 20 May 2004 21:12:55 GMT

Connection: close

Host: www.myfavoriteamazingsite.com

From: joebloe@somewebsitesomewhere.com
Accept: text/html, text/plain

User-Agent: Mozilla/4.0 (compatible: MSIE 6.0: Windows NT 5.1)

Request Line
General Headers

Request Headers

Entity Headers

Message Body

HTTP

Request

* Resposta: Pode ser dividida em 3 partes: linha de estado, cabeçalho e corpo da entidade;

Aversão do protocolo e o estado da conexão são apresentados na linha de estado. Os demais campos são semelhantes às mensagens de Requisição. Abaixo temos o exemplo:
HTTP/1.1 200 OK
Status Line

Date: Thu, 20 May 2004 21:12:58 GMT

Connection: close
Server: Apache/1.3.27
Accept-Ranges: bytes

Content-Type: text/html
Content-Length: 170

Last-Modified: Tue, 18 May 2004 10:14:49 GMT

<html>

<head>

<title>Welcome to the Amazíng Site!</title>

</head>

<body>

<p>This site is under construction. Please come back later. Sorry!</p>
</body>

</html>

General Headers
Response Headers

Entity Headers

Message Body

HTTP

Response

MÉToDoS HTTP

Cada método é responsável por determinar o tipo de requisição feita e a forma como o dado será tratado. Atenção para o fato de que todos devem ser escritos em letras maiúsculas. Oprotocolo faz a devida diferenciação. Vamos conhecê-los:
Q-Q SERPRO (Analista - Especialização: Tecnologia) Segurança da Informação - 2023
(Pós-Edital)

* GET - Solicitação de leitura de determinado objeto. A requisição de páginas WEB
pode ser feita através desse método;
* PUT - Solicitação de gravação de determinado objeto. Pode-se enviar páginas para um servidor remoto através desse método;
* POST - Método utilizado para anexar informações ou enviar arquivos de dados ou formulários como complemento de uma requisição de leitura. Dessa forma, a resposta dependerá da informação enviada. Basicamente trata a criação/atualização de um objeto ou recurso existente.
* HEAD - Mesma lógica do GET. Entretanto, solicita a leitura apenas do cabeçalho de um objeto ou página WEB. Tranquilo quando você vincula o nome do método com a estrutura do dado, certo? HEAD = CABEÇALHO. Com isso pode-se obter informações como a data da última modificação da página.
* DELETE- Remove o objeto ou página no servidor;

* OPTIONS - Realiza a consulta de determinadas opções;

* TRACE - Utilizado para teste com mensagens do tipo loopback;

* CONNECT- Utilizado para comunicação com servidores PROXY;

* PATCH- Utilizado para aplicar modificações parciais a um recurso;

CÓDIGOS DE ESTADO

Os códigos de estado são definidos em classes, conforme a seguir, com a descrição dos principais códigos:
* lxx - Classe informacional - Esta classe indica uma resposta provisória, que consiste de informações do estado da requisição e cabeçalhos opcionais.
* 2xx - Classe de Sucesso - Indica que a requisição foi recebida, entendida, aceita e processada.

* 3xx - Classe de Redirecionamento - Indica a necessidade de atuação por parte do clienteHTTP para completar a requisição. Pode ou não ser o caso de atuação direta do usuário.

* 4xx - Classe de Erro de Cliente - Indica a possibilidade de que houve um erro na requisição por parte do cliente. Caso não seja uma requisição com método HEAD, o servidor enviará uma explicação da situação do erro e se esta é permanente ou temporária.
400 (BAD REQUEST) - A requisição não pode ser entendida pelo servidor devido erro de sintaxe.
401 (UNAUTHORIZED) - A requisição depende de autenticação por parte do usuário.

403 (FORBIDDEN) - O servidor entendeu a requisição, mas se recusa a atendê-la. Pode ser enviado a descrição do motivo da recusa.
404 (NOT FOUND) - O servidor não encontrou nenhum documento que coincida com a URI
informada.

* 5xx - Classe de Erro de Servidor - Indica que o servidor reconheceu um erro interno ou a incapacidade de atender a requisição.
500 (INTERNAL SERVER ERROR) - Erro inesperado que impediu o atendimento a requisição.

503 (SERVICE UNAVAILABLE) - Servidor está incapacitado de atender as requisições devido à sobrecarga ou manutenção. Indica uma condição temporária.
505 (VERSION NOT SUPPORTED) - O servidor não suporta ou não está habilitado a responder para a versão requisitada. O servidor indica o motivo do erro, além de informar as versões que são suportadas e permitidas.
Esses códigos são característicos das mensagens de resposta de um servidor WEB qualquer.

CoNCEITo DE CACHE WEB

O funcionamento do CACHE WEB reside na possibilidade de otimização do procedimento deRequisição e Resposta entre o cliente e o servidor. Esse CACHE WEB busca evitar que novas consultas que sejam idênticas a consultas anteriores consumam recursos do servidor de destino,além de diminuir o tempo de resposta.
Sua implementação pode se dar:

* Servidor Proxy - Pode-se adicionar um elemento intermediário entre o cliente e o servidor,

de tal forma que as consultas necessariamente passem pelo nó intermediário antes de chegar ao destino. Esse nó, é chamado de Proxy e armazena as últimas informações requisitas pelos clientes aos servidores.
Dessa forma, caso haja uma nova requisição em que o proxy possua as informações necessárias para resposta, este não repassará a consulta ao servidor, atendendo a requisição imediatamente. É importante ressaltar que a presença do PROXY implica em duas conexões a serem estabelecidas: Cliente e PROXY; PROXY e Servidor.
* Proxy reverso - Esse conceito gera alguns benefícios na implementação de serviços
HTTP no lado do servidor. Entre eles temos os recursos de proteção, balanceamento e distribuição de requisições e armazenamento em cache das informações estáticas. Dessa forma, quando há uma requisição a um objeto estático, o proxy reverso é capaz de responder diretamente à requisição.
Já quando há uma requisição a objetos dinâmicos, este repassa a requisição aos servidores internos conforme a porta utilizada do serviço específico. A figura abaixo nos apresenta o modelo comentado:
* Cache Local - Os browsers possuem a capacidade de armazenar as informações recebidas do servidor de tal forma que uma nova requisição idêntica à anterior não enseje uma nova consulta ao servidor. Desse modo, a requisição será atendida diretamente pelo Browser.
Acrescento ainda a informação de que o protocolo HTTP pode ser utilizado de forma segura com a nomenclatura HTTPS, operando na porta 443/TCP.
A definição do tipo de criptografia a ser utilizado fica por conta dos protocolos SSL e TLS. Estes serão responsáveis por estabelecer uma camada de segurança para que o HTTP possa trafegar de forma segura.
Dessa forma, quando temos uma navegação em HTTPS, dizemos que os dados serão cifrados para uma comunicação segura, além da capacidade de se verificar a autenticidade do servidor através de recursos de certificados digitais. Acrescido a isso, temos também a possibilidade de autenticação do usuário de forma opcional. Essa é a diferença da versão de tunelamento: simples e mútua.
A primeira autentica apenas o servidor, enquanto a segunda, também autentica o cliente.
Desse modo, deve haver uma intervenção no cliente para que se implemente a configuração e instalação de certificado digital para que este possa ser usado no processo de autenticação do cliente.
Esse ponto gerou uma polêmica com a banca CESPE ao afirmar que o HTTPS necessariamente tratará os aspectos de autenticação do servidor e cliente, quando na prática, isso não acontece.
Quando acessamos os serviços da GOOGLE por exemplo, não enviamos nosso certificado digital para a devida autenticação, utilizando, portanto, o modo simples do SSL/TLS.
A Imagem abaixo nos dá uma visão das fases envolvidas no processo de conexão, troca de chaves e,
finalmente, troca dos dados:

Receiver

K=J

As três primeiras mensagens são de estabelecimento da conexão TCP. Entretanto,
a terceira mensagem indicada por "ACK/CLIENTHELLO" já congrega a última mensagem de ACK do TCP e a primeira do HTTPS (Hello). Em seguida, tem-se o reconhecimento e a definição dos algoritmos suportados com a devida troca de chaves, para, enfim, iniciar a troca de informação, de fato!
Algumas bancas em provas mais técnicas cobram as características de alguns campos dos cabeçalhos do protocolo HTTP. Dessa forma, recomendo a leitura do link:http://www.w3.org/Protocols/rfc2616/rfc2616-secl4.html

HTTP 2.0

Aprofundando um pouco mais a nossa conversa a respeito do HTTP, gostaria de comentar com vocês diversas características do protocolo HTTP em sua versão 2.0. Algumas bancas já estão apresentando questões que exigem conhecimento da referida versão e como o nosso objetivo é sempre estar atualizado, nada mais certo do que abordarmos tal assunto.
O surgimento dessa versão veio com o objetivo de contemplar a nova forma de navegação web.Temos um cenário com sites mais elaborados com um grande volume de dados, regras e protocolos que visam garantir princípios de segurança, navegação em dispositivos móveis, muitos outros.
A empresa GOOGLE buscou largar na frente nessa jornada e apresentou um novo protocolo próprio conhecido como SPDY. Foi uma camada de complementação de serviços e recursos ao HTTP padrão.Essa camada torna diversos recursos obrigatórios, entre eles o fato de se compactar e criptografar os dados e os cabeçalhos HTTP. Outro recurso interessante que surge para otimizar a utilização da banda é a multiplexação no HTTP. Tal recurso possibilitar gerar diversas requisições ao mesmo tempo em uma mesma conexão.
Mas porque estamos falando desse protocolo André? Devido aos excelentes resultados apresentados, ele tem servido como base para a elaboração da versão 2.0 do HTTP.
Desse modo, a versão 2.0 suporta todos os recursos básicos das versões anteriores,
porém, com grande foco na eficiência da comunicação em termos de velocidade e racionamento de recursos.
A versão 2.0 incluiu outros tipos de quadros além dos padrões já conhecidos que são o HEADER eDATA, conforme versão anterior. Nesse contexto, surge quadros do tipo SETTINGS,WINDOW_UPDATE e PUSH_PROMISSE, com vistas a implementação de novos recursos no HTTPv2.0.

Surge ainda o conceito de STREAMS ou fluxos independentes e bidirecionais em uma mesma conexão. Desse modo, um problema de bloqueio ou congestionamento em algum desses fluxos não impacta os demais. Devido a essa característica, busca-se ainda implementar controles de fluxo e priorização de STREAMS.
Há de se mencionar que todas as conexões do HTTPv2.0 são persistentes. Desse modo, os clientes não devem ser capazes de abrir mais de uma conexão para o mesmo host/porta.Entretanto, pode-
se estabelecer novas conexões em detrimento da anteriormente estabelecida para algumas finalidades, entre elas, a renegociação de chaves para uma conexão TLS ou conexões que estão com erros.
Vamos abordar então os diversos pontos que são mais relevantes a respeito da implementação doHTTPv2.0, inclusive em conjunto com protocolos auxiliares como o TLS.

* Compressão Automática

Nas implementações padrões das versões anteriores do HTTP, quando se almejava incremento do desempenho, utiliza-se a ferramenta GZIP no lado do servidor que era responsável pela compressão dos dados que serviam como respostas às requisições dos clientes.
Na versão 2.0, tal implementação é utilizada como padrão e de forma obrigatória. Além disso, utiliza-se um algoritmo conhecido como HPACK para compressão de todos os HEADERS, sejam aqueles destinados às requisições ou a respostas, diminuindo bastante o volume de dados trafegados nosHEADERS.

* Criptografia e Segurança

Para comunicações seguras, tem-se a utilização do HTTPS de forma obrigatória com vistas a tratar os diversos aspectos de segurança da informação. É importante mencionar que tal recurso implica em uma difusão global de certificados digitais para que tenhamos ambientes mais robustos e seguros nas comunicações com HTTPS.
Desse modo, o SSL é um protocolo fundamental na implementação e transição do HTTPS
para o
HTTP2.0.

* Paralelização de Fluxos com Multiplexing

Como vimos anteriormente, o HTTP em suas versões anteriores utiliza o conceito de envio de recursos de forma sequencial. Assim, ao se abrir a conexão, envia-se um request e espera-se uma resposta para o referido request antes de enviar a nova requisição.
A evolução desse recurso, ainda implementado para as versões anteriores, era abrir diversas conexões e cada uma ter o seu próprio fluxo. Percebam que aqui tínhamos uma paralelização de conexões, algo em torno de 4 a 8 conexões para um host comum.
O HTTP2.0 surge então com uma nova abordagem, a de paralelização de fluxos ou de requisições e respostas em uma mesma conexão, totalmente independentes entre si, assíncronos e bidirecionais.
Como já vimos e reforçamos, tal recurso é conhecido como MULTIPLEXING. A imagem abaixo nos traz essa representação em que não é necessário aguardar a resposta específica para uma requisição, antes de enviar uma nova requisição:
Q-Q

Diante do modelo proposto, o controle de fluxo em cada um desses streams é fundamental, devendo ser garantido esse aspecto. O HTTP2.0 utiliza o quadro WINDOW_UPDATE para tal funcionalidade.Ele pode ser aplicado tanto para controle de fluxo de cada stream como da conexão como um todo.

Outro recurso interessante que surge no HTTP2.0 é a otimização de tráfego com vistas a não enviar informações redundantes que já foram trafegadas. Ou seja, por padrão, o HTTP em sua versão anterior manda informações idênticas a cada requisição ou resposta, como é o caso do parâmetro"User-Agent" que informa características do Browser do cliente.

Na nova versão, envia-se apenas informações de cabeçalho que são diferentes das informações já enviadas, reduzindo, assim, o fluxo de dados desnecessários.
* Priorização de Requests

O HTTPv2.0 possui a capacidade de distinguir as respostas a serem enviadas e categorizá-las conforme a necessidade de montagem da página. Desse modo, pode-se enviar, por exemplo,de forma prioritária, o arquivo base da página "index.html" e posteriormente, complementá-la com as demais informações.
Assim, busca-se dar agilidade e trazer um caráter mais ágil na construção da página no lado do cliente.
A figura a seguir nos traz essa representação:

* Server-Push

A ideia desse recurso é identificar a necessidade do cliente de tal modo que ele não necessite fazer a requisição para cada recurso. Na figura acima, verificamos que para cada resposta,houve uma requisição. Ora, o servidor entende que sempre que há o pedido de envio da página index.html,necessariamente virá pedidos para as demais páginas. Desse modo, ele antecipa tal questão e já envia os recursos independentemente da requisição do cliente.
* HTTP2.0 com TLS 1.2

Para implementação do HTTP em sua versão 2.0, deve-se utilizar a extensão do TLS conhecida como
Server Name Indication (SNI). Para as versões do TLS 1.3 ou superior, a implementação e suporte doSNI é suficiente.

Já a versão 1.2 apresenta uma série de requisitos que devem ser seguidos para que seja possível a sua implantação. Caso esses requisitos não sejam atendidos, pode-se ter problemas de diversos,principalmente no que concerne à troca de chaves e estabelecimento da sessão TLS na fase de negociação.
Nesses casos, utiliza-se mensagens do tipo INADEQUATE_SECURITY ou categoriza-se como erro de conexão.
Dessa forma, vamos checar quais são os requisitos que devem ser atendidos:

Desabilitar a COMPRESSÃO

A compressão pode gerar problemas de vazamento de dados ou exposição indevida. É
importante lembrar que compressões genéricas são desnecessárias uma vez que o
HTTPv2 apresenta recurso de compressão intrínseca criada e configurada para uma operação plena no HTTPv2 em termos de desempenho, seguranças e outros pontos.
Desabilitar a RENEGOCIAÇÃO

Por motivo da troca de chaves e certificados no estabelecimento da conexão, os terminais devem tratar a renegociação como um erro de conexão. A renegociação deve ser utilizada exclusivamente para fins de confidencialidade na troca de informações de credenciais no estabelecimento da conexão e não conectividade.
EXERCÍCIOS COMENTADOS

HTTP

1. CESPE - STJ/Analista Judiciário - Suporte em TI/2015

Uma forma de se melhorar o desempenho do acesso a páginas web frequentemente visitadas é armazenar-se o conteúdo dessas páginas para que sejam rapidamente carregadas em solicitações futuras, estando, entre os possíveis processos para executar essa tarefa, o proxy, ao qual serão encaminhadas todas as requisições de acesso a páginas web.
Comentários:

De fato, um proxy poderá ser utilizado para este fim. Entretanto, é importante lembrarmos que a funcionalidade mencionada na questão é o recurso do cache. Através do cache, pode-se armazenar conteúdos estáticos das páginas web e disponibilizar tais recursos diretamente aos hosts requisitantes sem necessariamente consultar o servidor.Isso possibilidade um incremento de desempenho em tempo de resposta e alivia a carga de consultas ao servidor.
Gabarito: C

2. CESPE - TJ TRE MS/Apoio Especializado/Programação de Sistemas/2013

O elemento em que uma das partes de uma informação é armazenada como cadeia de texto na máquina do usuário e cuja função principal é a de manter a persistência de sessões HTTP é denominado a) frame.
b) java Script.
cj tag.

d) cookie.

e) XML.

Comentários:

Uma das funções do cookie é exatamente a apresentada na questão, além da possibilidade de ser armazenar informações específicas de cada host para agilizar consultas ou fornecer um serviço personalizado.
Gabarito: D

3. CESPE - TJ TRE MS/Apoio Especializado/Programação de Sistemas/2013

Com referência ao Hyper Text Transfer Protocol (HTTP) — protocolo de aplicação utilizado para o tratamento de pedidos e respostas entre cliente e servidor na Internet e com o qual, normalmente, são desenvolvidas as aplicações para a Web —, assinale a opção em que todas as expressões identificam métodos de requisição HTTP que devem ser implementados por um servidor HTTP 1.1 usado pelo cliente.
a) SOAP, WS, WSDL, UDDI

b) TCP, IP, NETBIOS, UDP, IPX

c) NFS, SMB, IPP, SMTP, P0P3, IMAP,XMPP, SIP

d) SET, GET, CONSTRUCTOR, DESTRUCTOR

e) GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS

Comentários:

A alternativa "E" descreve 7 dos 9 existentes. Faltam ainda os métodos CONNECT e
PATCH. Os mais utilizados sem dúvida são os 3 primeiros.

Gabarito: E

4. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

O protocolo HTTP, que não armazena informações sobre o estado do cliente, classifica-se como do tipo stateless.
Comentários:

Vimos que essa é uma característica nativa do protocolo HTTP.

Gabarito: C

5. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

Um servidor HTTP consiste em um servidor de aplicações.

Comentários:

Um servidor HTTP é considerado um servidor WEB e não um servidor de aplicações completo com muito mais recursos. Dizemos que um servidor WEB integra um servidor um servidor de aplicações.
Gabarito: E

6. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

Ao receber uma requisição, o servidor procura pelo recurso requisitado e envia, ao cliente,
uma resposta com um código, que pode iniciar-se por lxx, que indica sucesso no recebimento da requisição; 2xx, que indica redirecionamento da requisição; 3xx, que informa erros acontecidos no cliente; e 4xx, que informa erros no servidor.
Comentários:

Pessoal, a ordem correta é:
lxx - Classe informacional
2xx - Classe de sucesso

3xx - Classe de redirecionamento
4xx - Erros no lado do cliente
5xx - Erros no lado do servidor

Gabarito: E

7. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

As estratégias usadas para diminuir o tráfego causado pelo grande número de acessos a páginas web podem ser do tipo cache web, que é implementado no cliente, no GETcondicional ou na rede servidor Proxy Web.

Comentários:

Pessoal, vimos que o cache pode estar localizado tanto no cliente, em um browser por exemplo ou em um servidor Proxy. Complemento ainda o fato da existência da utilização do método GET de forma condicional. Na requisição GET, o cliente envia informações de data do objeto desejado em um cache web. Caso o objeto não tenha sido modificado a partir da data, extrai-se a informação do cache. Caso tenha havido mudança, o servidor envia o objeto atualizado.
Gabarito: C

8. CESPE - MPU/Analista Judiciário - Suporte e lnfraestrutura/2013

Os servidores proxy criam um cache com as solicitações de cada usuário, deforma a otimizar consultas futuras de um mesmo usuário, sendo esse cache de uso exclusivo de seu respectivo usuário.
Comentários:

Pessoal, vimos que o cache pode ser utilizado para armazenar informações de páginas para acesso geral de qualquer usuário desse servidor Proxy. Além disso, em relação às informações para customização do acesso, armazena-se informações em cache de cada usuário para uso de cada um no momento adequado.
Gabarito: E

9. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

O código abaixo ilustra uma resposta de um servidor web.

GET /internet/index.html

User-agente: Mozilla /4.5 [en]
AcceptP: text/plain, text/html, image/gif,

HTTP/1.0

(WinNT; I)

image/x-xbitmap,

image/jpeg, image/pjpeg, image/png, */*

Accept-Charset: isso-8859-1,
Accept-Enconding:

Accept-Language: em

*, utf-8

gzip

Comentários:

O lado que se utiliza dos métodos é o cliente e logo na primeira linha vemos o métodoGET, logo, o trecho é um tipo de requisição. As respostas são iniciadas com os códigos que vimos anteriormente.
Gabarito: E

10.CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

O protocolo HTTP utiliza, por padrão, a porta 80 para tráfego seguro de dados, sendo o pacote de sincronismo da conexão o responsável por indicar o tipo de cifra que será utilizado na sessão.
Comentários:

A porta 80 é utilizada pelo protocolo HTTP padrão. A implementação segura fica a carga do protocolo HTTPS na porta TCP/443. A definição de critérios de criptografia ocorre no momento do estabelecimento da conexão.
Gabarito: E

ll.CESPE - TJ TRT17/Apoio Especializado/Tecnologia da lnformação/2013

Como maneira de se evitar o desenvolvimento de novos protocolos de camada de aplicação, diversas aplicações usam o HTTP como forma de transferir dados fim afim na camada de aplicação.
Comentários:

De fato. Por sem um protocolo amplamente consolidado, simples e eficiente, diversos protocolos acabam usando sua estrutura para reaproveitar o modelo na transferência de dados simples.
Gabarito: C

12.CESPE - Tec MPU/Técnico Administrativo/Tecnologia da Informação e
Comunicação/2013

O serviço HTTP é implementado sem estado, enquanto o HTTPS é sua versão stateful (com estado).
Comentários:

O HTTPS nada mais é do que uma implementação segura do protocolo HTTP. Os princípios do protocolo são mantidos os mesmos.
Gabarito: E

13.CESPE - Ana MPU/Tecnologia da Informação e Comunicação/Suporte e lnfraestrutura/2013
A primeira versão do serviço HTTP utiliza conexões não persistentes; a persistência foi acrescentada na versão subsequente desse serviço.
Comentários:

Exatamente como vimos não é pessoal. Somente a partir da versão 1.1 é que foi implementado o recurso de conexões persistentes.
Gabarito: C

14.CESPE - TRT(DF e GO)/Técnico Judiciário - Tecnologia da lnformação/2013

Os servidores de HTTP mais utilizados atualmente são Apache HTTP Server, Internet
Information Server e Enterprise Server.

Comentários:

Pessoal, de fato os dois principais são o Apache (Sun Microsystems) e o
Internet
Information Server (IIS - Microsoft). O Enterprise Server, entendo que a banca tentou nos trazer um conceito mais geral de servidores coorporativos, sendo essa uma verdade,com diversas possibilidades de implementações. Trazendo então uma visão mais genérica, não vejo problema em considerarmos a questão como correta.
Gabarito: C

15.CESPE - CNJ/Técnico Judiciário - Programação de Sistemas/2013

Se o endereço de página inicia com HTTPS, então os dados serão transmitidos por meio de uma conexão cifrada e a autenticidade do servidor e do cliente será verificada com o uso de certificados digitais.
Comentários:

Temos aqui a questão problemática de autenticação via HTTPS que mencionei. Percebam que o enunciado afirma que será realizado o método de autenticação mútua, o que não é bem verdade. É um recurso opcional que depende de configuração no lado do cliente.Desse modo, fiquemos com o aprendizado da forma de intepretação do CESPE para não errarmos esse mesmo ponto em provas futuras.
Gabarito: C (Gabarito do Professor: E)

16.CESPE - TCU/Analista de Controle Externo - TI/2007

O protocolo HTTP, definido nas RFCs 1945 e 2616, não permite a utilização de conexões persistentes.

Comentários:

A versão 1.1 do HTTP suporta conexões persistentes.

Gabarito: E

17.CESPE - TRT -17^ Região (ES)/Técnico Judiciário - TI/2013

HTTPS usa certificados digitais, requer o uso de TLS e utiliza a porta 443 por padrão.

Comentários:

Questão bem tranquila, certo pessoal? Muito cuidado para não ficar buscando problemas onde não há. Atualmente, o SSL/TLS é considerado como sendo um mesmo protocolo apesar de suas pequenas diferenças e de não serem compatíveis entre si. Desse modo,não devemos encrencar com esse aspecto para essa questão, dizendo que seria possível a utilização de SSL ao invés do TLS.
Gabarito: C

18.CESPE - TRE-GO/Técnico Judiciário/2015

Na busca de um produto em uma loja virtual por meio de um webservice, quando o produto é encontrado, o protocolo HTTP retorna um HTTP/1.1 404, o que facilita o tratamento do pedido no programa cliente.
Comentários:

Vimos na nossa lista de códigos que a família 4xx corresponde a erros do lado do cliente.
Mais especificamente o 404, temos que o recurso não foi encontrado, retornando uma mensagem "not found", ou seja, tem-se um URI inválida.
Gabarito: E

19.CESPE - TRE-GO/Técnico Judiciário - Programação de Sistemas/2015

Por meio do protocolo chave HTTP, é possível utilizar o método PUTpara se criar um novo recurso de um webservice.
Comentários:

Vimos que o método PUT permite submeter um arquivo ou recurso no servidor a partir de um cliente. Pode-se enviar uma nova página sem maiores dificuldades.
Gabarito: C

20.CESPE - TRE-GO/Técnico Judiciário - Programação de Sistemas/2015

Uma conexão entre um computador cliente a um computador considerado servidor, para visualizar uma página web, através do protocolo HTTP, é possível afirmar que será utilizado o protocolo de transporte TCP (transmission control protocol).
Comentários:

Pessoal, tenham cuidado para não confundir a obrigatoriedade de se usar o protocolo TCP
como o fato do HTTP ser stateless. Lembremos que o primeiro está relacionado ao estabelecimento da conexão necessária para envio e recebimento dos dados, enquanto o segundo diz respeito ao armazenamento do estado da sessão, sendo que este último não é fornecido pelo HTTP.
Gabarito: C

21.CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015

A técnica de compressão não é recomendada ao se utilizar a versão 2 do HTTP sobre o protocolo TLS 1.2.
Comentários:

Vimos que essa é uma das recomendações apresentadas a respeito do HTTP 2.0.

Gabarito: C

22.CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015

Na implementação do HTTP versão 2 sobre o protocolo TLS 1.2, é mandatário desabilitar a renegociação da conexão.
Comentários:

Esse é um ponto necessário para o funcionamento do HTTP em conjunto com o TLS 1.2.

Gabarito: C

23.CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015

No HTTP, a técnica geral do controle de fluxo garante que não haja interferência entre as conexões independentes. Entretanto essa técnica foi abandonada na versão 2 do HTTP, que criou o conceito de WINDOWJJPDATE frame.
Comentários:

Muito pelo contrário. 0 WINDOWJJPDATE foi criado para tal funcionalidade.

Gabarito: E

PRoToCoLoS DE CoRREIo ELETRôNICo (SMTPJMAP E POP3)

24.CESPE - TCE-PR/Analista de Controle - Área TI/2016

0 padrão por
A

que meio viabiliza da
Mail a transmissão de dados não utilização de SMTP
Transfer

ASCII por email é denominado
Protocol.

B Multiporpose

C Post

D Internet

Internet Mail

Office

Message Access

Extension.
Protocol.
Protocol.

E Hypertext Transfer Protocol.

Comentários:

Temos aí o MIME, certo pessoal? Questão bem tranquila passível de ser resolvida por eliminação. O MIME surgiu exatamente no contexto em que o padrão de codificação ASCIInão era mais suficiente para representação de anexos de binários e conteúdos multimídia. O MIME passa então a suportar padrões de textos como HTML e XML,imagens do tipo GIF e JPEG, áudio e vídeo.

Gabarito: B

25.CESPE - TCE-SC/AFCE - Área TI/2016

Após o servidor local SMTP aceitar uma mensagem para subsequente envio, é necessário determinar o endereço do servidor de email do destinatário. Essa etapa é realizada mediante consulta DNS a um servidor de nomes capaz de prover a informação, no qual serão verificados os registros especiais MX (mail Exchange).
Comentários:

Temos a descrição do princípio exercido pelo protocolo DNS, que é a tradução de nomes para endereços IP. Além disso, temos uma especificidade do seu funcionamento no que tange ao tipo de consulta realizada. O DNS é capaz de realizar diversos tipos de serviços,as quais são definidas a partir das referências a seguir, em um caráter não exaustivo:

A - Address IPv4 - Quando um cliente usa esse tipo de registro, o objetivo é descobrir o endereço IPv4 que responde por determinado nome de domínio;
AAAA - Address IPv6 - Quando um cliente usa esse tipo de registro, o objetivo é descobrir o endereço IPv6 que responde por determinado nome de domínio;
CNAME (Canonical Name) - Faz o mapeamento de um alias (apelido) ou um DNS
alternativo.

PTR - Pointer - Realiza o caminho inverso. A partir de um endereço IPv4, deseja-
se obter o respectivo nome de domínio;

NS - Nameserver - Especifica o nome do servidor DNS responsável por determinado domínio;
MX - Mail Exchange - Fornece o nome do servidor de e-mail de maior prioridade que responde por determinado domínio de e-mail. Após a obtenção desse nome, é preciso ainda realizar uma consulta do tipo address para se determinar o endereçoIP;

Essas identificações serão fornecidas no campo TYPE da estrutura de resposta DNS.
Portanto, percebemos que o MX, de fato, diz respeito à tradução do nome do servidor de e-mail para o respectivo endereço IP.
Gabarito: C

26.CESPE - STF/Apoio Especializado/Suporte em Tecnologia da lnformação/2013

Caso o emissor da mensagem não envie nenhum comando ao servidor SMTP, servidores de correio eletrônico modernos com suporte ao SMTP implementarão técnicas de timeout.
Comentários:

Pessoal, vimos que o protocolo SMTP encerra a sessão com o comando QUIT. Entretanto,
possui um tempo default de 5 minutos. Caso não haja troca de mensagens nesse intervalo,
automaticamente o servidor derruba a conexão.

Gabarito: C

27.CESPE - TRE-RJ/Analista Judiciário - Análise de Sistemas/2012

O SMTP (simple mail transfer protocol) é um protocolo de correio eletrônico para recebimento de e-mail pelos usuários.
Comentários:

Não né pessoal? O SMTP é para envio. Os protocolos para recebimento são o IMAP e o
POP3.

Gabarito: E

28.CESPE - Banco da Amazônia/Técnico Científico/2012

O protocolo SMTP, ao utilizar a porta 25 para enviar e receber mensagens, é capaz de criptografar o cabeçalho da mensagem transmitida.
Comentários:

O SMTP nativamente e por si só não implementa recursos de criptografia. Vale observar que o protocolo SMTP foi referenciado na porta 25 para enviar e receber mensagens. Na prática, o cliente abre uma conexão TCP na porta 25 do servidor. Sob a perspectiva do cliente então, a porta 25 será utilizada para envio, sob a perspectiva do servidor, a porta
25 será utilizada para recebimento. Não vejo motivo para esse trecho, portanto, estar errado.
Gabarito: E

29.CESPE - Câmara dos Deputados/Analista - Engenharia Eletrônica/2012

O SMTP consiste em um protocolo muito utilizado pelos servidores de transporte de email modernos, apesar de possuir tecnologia bastante arcaica, surgida antes mesmo do protocolo HTTP.
Comentários:

De fato, o SMTP é bem antigo, vindo antes mesmo do HTTP, conforme vimos. Isso não limita seu uso em servidores atuais e modernos, por ele ser simples e eficaz frente ao seu propósito.
Gabarito: C

30.CESPE - TRE-RJ/Analista Judiciário - Análise de Sistemas/2012

O protocolo SMTP é um protocolo cliente-servidor, uma vez que os servidores de correio eletrônico funcionam ora como clientes, ao enviarem emails, ora como servidores, ao receberem emails.
Comentários:

Vimos que essa é uma das formas de atuação dos MTA's. Possui uma função de relay na rede ao repassar essas informações. Atenção para o detalhe muito bem pontuado pela banca. Ao enviar, atua como cliente, ao receber, atua como servidor. Se tivesse escrito de forma inversa estaria errado.
Gabarito: C

31.CESPE - STF/Apoio Especializado/Suporte em Tecnologia da lnformação/2013

Ainda que uma mensagem de email com SMTP possua diversos destinatários, o comando
RCPT é realizado no servidor de destino somente uma vez.

Comentários:

Pessoal, vimos que o comando RCPT aceita somente uma entrada de email por vez.
Portanto, para múltiplos destinatários, deve-se enviar diversos comandos RCPT com os endereços dos destinatários.
Gabarito: E

32.CESPE - STF/Apoio Especializado/Suporte em Tecnologia da lnformação/2013

0 uso de Open Relay para configurar servidores de email ligados à Internet é considerado má prática administrativa. Normalmente, esse tipo de servidor é passível de ser inscrito em listas negras na Internet.
Comentários:

Vimos que o conceito de open relay são aqueles MTA's mal configurados ou sem implementação de recursos de segurança. Dessa forma, tendem a repassar conteúdo indesejado e malicioso e acabam por diversas vezes figurando nas blacklists(listas negras) na Internet.
Gabarito: C

33.CESPE - ANTT/Tecnologia da Informação/lnfraestrutura de TI/2013

Quando um serviço de correio eletrônico disponibiliza o IMAP (Internet message access protocol) para o usuário final, este utiliza um software cliente de email para manipular e manter suas mensagens no servidor de correio eletrônico.
Comentários:

Vimos que a principal característica dos servidores IMAP é justamente a capacidade de se acessar e gerenciar os e-mails diretamente no servidor de e-mails, sem a necessidade de realizar o download das mensagens. Detalhe para o software cliente que pode ser um software específico ou o próprio browser com acesso web.
Gabarito: C

34.CESPE - TRE-RJ/Analista Judiciário - Análise de Sistemas/2012

Os protocolos OSPF e LDAP são utilizados para ler, editar, responder e criar novos e-mails.

Comentários:

Bem tranquilo, não é pessoal? OSPF é um protocolo de roteamento e o LDAP é um protocolo de acesso a serviços de diretórios em redes TCP/IP. Protocolos para tais recursos são o SMTP, IMAP e POP.
Gabarito: E

35.CESPE - Banco da Amazônia/Técnico Científico - Suporte Técnico/2012

O recurso de greylist recusa, deforma temporária, o recebimento de uma mensagem e aguarda sua retransmissão, levando em consideração que servidores de e-mail legítimos possuem políticas de retransmissão em caso de erros.
Comentários:

Vimos que o método greylist é um híbrido, entre o whitelist e blacklist que implementa justamente o funcionamento descrito no enunciado.
Gabarito: C

36.CESPE - Banco da Amazônia/Técnico Científico - Suporte Técnico/2012

O bloqueio de conteúdo pelo servidor SMTP pode recusar a mensagem enviando um código de erro, acrescido da mensagem Message Content Rejected ou desviando-a para uma área chamada de quarentena.
Comentários:

Pessoal, vimos que essas duas são possibilidades de atuação de um MTA frente a um possível email malicioso ou considerado SPAM.
Gabarito: C

37.CESPE - Banco da Amazônia/Técnico Científico - Suporte Técnico/2012

Ao detectar que uma mensagem de e-mail é um spam, as ferramentas de antispam são capazes de modificar o assunto da mensagem, para alertar o usuário de que se trata de spam, e depois entregá-la na conta de e-mail do usuário.
Comentários:

Mais uma vez, temos a descrição de uma possibilidade de atuação do servidor de email,
agora frente a um possível SPAM, transferindo a responsabilidade para o usuário considerar ou não a ponderação do servidor de email.
Gabarito: C

38.CESPE - TRE/RS / Técnico Judiciário - Área 7/2015 (ADAPTADA)

Para a transferência efetiva de mensagens de email, o SMTP deve estar disponível nos servidores de correio do remetente e do destinatário, sem a possibilidade de implementação de outros protocolos.
Comentários:

A característica do SMTP é seu funcionamento assíncrono ou também conhecido como store-and-forward. Ou seja, caso um servidor receba determinada mensagem, ele por guardar essa mensagem pelo tempo necessário até que o servidor que deva recebê-la esteja online, não necessitando que seja feito de forma simultânea.
Gabarito: E

39.CESPE - TRE/RS / Técnico Judiciário/2015 (ADAPTADA)

O POP é um protocolo para envio de email.

Comentários:

O SMTP é um protocolo de envio, enquanto o POP3 e IMAP são para recebimento.

Gabarito: E

40.CESPE - TJDFT/Analista Judiciário - Análise de Sistemas/2015

PGP (Pretty Good Privacy) é um pacote que fornece recursos de compactação, privacidade e assinaturas digitais, além de poder criptografar mensagens de correio eletrônico.
Comentários:

0 PGP É um pacote que é implementado na camada de aplicação que utiliza recursos de funções HASH, como o SHA-1 e criptografia simétrica e assimétrica. Somando-se todos esses recursos, é possível buscar os princípios de confidencialidade, integridade e autenticidade através da assinatura digital e criptografia dos dados com chaves de sessão. Suporta o recurso de múltiplas assinaturas, compressão de forma segura,fragmentação de mensagens. Há de se mencionar que esses recursos não necessariamente são utilizados em conjunto, podendo ser aplicados de forma independentes, ou seja, posso querer não implementar o recurso de compressão e manter todos os demais.
Gabarito: C

41.CESPE - TRE-PE/Área 1 - Operação de Computadores/2016 (ADAPTADA)

Os protocolos IP, SNMP, SMTP e ARP fazem parte da camada de rede (Internet) do modelo TCP/IP.
Comentários:

Somente os protocolos IP e ARP fazem parte da camada de rede. O SNMP e SMTP fazem parte da camada de aplicação.
Gabarito: E

EXERCÍCIOS COMENTADOS COMPLEMENTARES

HTTP

1. FCC - TRT - 155 Região/Analista Judiciário - TI/2015

Um serviço da internet utiliza diferentes protocolos, por exemplo, protocolos relacionados com a função de roteamento, transmissão de dados e transferência de hipertexto para efetivar a comunicação. Os respectivos protocolos, do conjunto (suite) de protocolosTCP/IP, relacionados com as funções apresentadas, são:

a) IP, TCP e HTTP.

b) TCP, FTP e HTML.

c) IP, FTP e HTML.

d) ARP, FTP e HTTP.

e) TCP, IP e HTTP.

Comentário:

Temos três aspectos para considerar.

1. Protocolo relacionado com roteamento nos leva a considerar a camada de rede e o principal protocolo para encaminhamento de pacotes entre redes,que é o IP.

2. Quando se fala de transmissão de dados, devemos remeter à capacidade de transportar a informação fim a fim. Isso nos leva à camada de transporte,logo, temos os protocolos TCP ou UDP como principais opções.

3. E por último, o protocolo de transferência de hipermídia, sendo essa a palavra chave para referenciarmos o protocolo HTTP.
Gabarito: A

2. FCC - TRT -165 Região (MA) /Técnico Judiciário - TI/2014

Os diversos protocolos do conjunto (suite) TCP/IP são organizados em camadas de funcionalidade. Quando um usuário da internet realiza um acesso à página Web, ele está utilizando o protocolo da camada de Aplicação denominado a) WWW.
b) IMAP.

c) HTTP.

d) TCP.
ej IP.

Comentário:

Pessoal, vimos que as requisições WEB estão debaixo da operação e funcionamento do protocolo HTTP.
Gabarito: C

3. FCC - TRT - 29 Região (SP)/Técnico Judiciário - TI/2014

No modelo de referência de 4 camadas da suíte de protocolos TCP/IP, os protocolos
Ethernet, HTTP e ICMP localizam-se, respectivamente, nas camadas a) Internet, Apresentação e Interface de rede b) Interface de rede, Aplicação e Internet.
c) Transporte, Internet e Interface de rede.

d) Transporte, Aplicação e Enlace de dados.

e) Física, Transporte e Enlace de dados.

Comentário:

Mais uma questão que aborda o posicionamento dos diversos protocolos nas camadas da arquitetura TCP/IP. Bem tranquilo, certo? Vemos que a camada de Acesso à Rede está sendo referenciada como Interface de Rede. Vimos que o protocolo Ethernet está na camada 2 do modelo OSI, logo, faz parte da camada Interface de Rede. Já o HTTP atua na camada de aplicação, inclusive atuando na porta 80 conforme vimos. E por último o protocolo ICMP que atua de forma complementar ao IP na camada de rede.
Gabarito: B

4. FCC - TRF - 49 Região/Técnico Judiciário - TI/2014

Pedro, técnico em informática do TRF da 4- Região, deve comprovar os seus conhecimentos sobre 0 modelo OSI identificando os protocolos às respectivas camadas do modelo. Assim,um correto relacionamento identificado por Pedro é:

a) FTP - Camada de Transporte.

SERPRO (Analista - Especialização: Tecnologia) Segurança da Informação - 2023 (Pós-I

b) HTTP - Camada de Transporte.

c) ICMP - Camada de Aplicação.

d) HTTP - Camada de Aplicação.

e) SNMP - Camada de Rede.

Comentário:

Questão típica das provas de técnico judiciário em vincular os protocolos às camadas do modelo OSI. FTP, HTTP e SNMP são da camada de aplicação, enquanto o ICMP da camada de rede.
Gabarito: D

5. FCC - TRF - 23 Região/Analista Judiciário - lnformática/2012

Sobre o protocolo HTTP, é correto afirmar:

a) Usa o TCP e o UDP como seus protocolos de transporte e presta serviço por default na porta 80.
b) Em uma mensagem de requisição HTTP, a linha de cabeçalho User-agent: especifica o agente de usuário, isto é, o browser que está fazendo a requisição ao servidor.
c) Quando utiliza conexões persistentes, cada conexão TCP é encerrada após o servidor enviar o objeto resposta ao cliente que fez a requisição. Cada conexão TCP transporta exatamente uma mensagem de requisição e uma mensagem de resposta.
dj A resposta do servidor a uma requisição HTTP é dividida em três seções. A primeira é denominada cabeçalho (header) e contém informações do servidor sobre o recurso solicitado. A segunda seção é denominada corpo (body) e contém o recurso propriamente dito. A terceira seção, denominada rodapé (footerf contém informações de status da requisição e o relatório de erros, quando houver.
e) Os únicos métodos (comandos) de requisição do protocolo HTTP são GET e POST. O
status de retorno de número 404 do método HTTP indica que o serviço está indisponível.

Comentário:

Vamos aos itens:

a) Para efeito de prova, ficamos com a afirmação de que o HTTP utiliza somente o protocolo TCP na porta 80. INCORRETO
b) Vimos que as informações referentes ao nome da página, estado corrente da conexão,
informações do navegador (User Agent) e língua aceitas, entre outros, fazem parte da estrutura do cabeçalho HTTP. CORRETO
c) Essa é uma característica das conexões não persistentes, ou seja, da versão 1.0. As conexões persistentes abrem uma única conexão para transporte de todos os dados da comunicação. INCORRETO
d) A resposta à requisição é dividida em três partes: linha de estado, cabeçalho e corpo da entidade. INCORRETO
e) Diversos são os métodos suportados pelo HTTP, não se restringindo ao GET e POST.
INCORRETO

Gabarito: B

6. FCC - TCE-SP/Auxiliar de Fiscalização Financeira/2012

Sobre o protocolo HTTP, é correto afirmar:

a) Se um cliente solicita ao servidor o mesmo objeto duas vezes em um período de poucos segundos, o servidor responde dizendo que acabou de enviar o objeto ao cliente e não envia novamente o objeto.
b) E implementado em dois programas: um programa cliente e outro servidor. Os dois programas, implementados em sistemas finais diferentes, conversam um com o outro por meio da troca de mensagens HTTP. O HTTP não define a estrutura dessas mensagens, mas define o modo como cliente e servidor as trocam.
c) O HTTP usa o TCP como seu protocolo de transporte subjacente. O cliente HTTP
primeiramente inicia uma conexão TCP com o servidor. Uma vez estabelecida a conexão,
os processos do browser e do servidor acessam o TCP por meio de suas interfaces socket.
d} Os servidores web implementam apenas o lado cliente do HTTP e abrigam objetos web, cada um endereçado por um URL. O Apache e o IIS são servidores web populares,
e) O HTTP define como clientes web requisitam páginas web aos servidores, mas não define como eles as transferem aos clientes.
Comentário:

Vamos aos itens:

a) O protocolo HTTP é um protocolo sem estado. Ou seja, toda requisição recebida, ainda que do mesmo host a respeito do mesmo objeto, será interpretado como uma nova requisição. INCORRETO
b) O HTTP define muito bem a estrutura das mensagens de requisição e resposta.
INCORRETO

c) Temos aí um exemplo de funcionamento do HTTP. CORRETO

d) Servidores WEB implementam o lado do servidor e não do cliente. O resto da questão está conforme esperado. INCORRETO
e) Conforme já conversamos, o HTTP possui uma estrutura completa de requisição e resposta. INCORRETO
Gabarito: C

7. FCC - MPE-AM/Agente de Apoio - Manutenção e Suporte de lnformática/2013

HTTPS (HyperText Transfer Protocol Secure) é um protocolo que combina o uso do HTTP
com o a) SSL e o TLS, afim de prover conexões seguras.
b) DES e AES, afim de prover criptografia assimétrica.

cj RSA, a fim de prover certificação digital por meio de criptografia simétrica.

d) IDS e IPS, a fim de prover segurança contra invasores.
ej IMAP e POP, a fim de prover comunicação segura.

Comentário:

Conforme vimos, o HTTPS utiliza a porta 443 para uma implementação de uma camada de segurança abaixo do HTTP. Utiliza-se basicamente os protocolos SSL e TLS para o estabelecimento dessa camada de segurança.
Gabarito: A

8. FCC - TRF -12 Região/Analista Judiciário - Área de Apoio Especializado/2014

Orecebe os pedidos HTTP na porta configurada e processa todos os pedidos da web que chegam, podendo distribuí-los. Os pedidos de objetos que podem ser armazenados no cache (informações estáticas que não mudam com frequência como páginas em HTML e imagens GIF) são processados pelo proxy. Os pedidos de objetos que não podem ser armazenados no cache (informações dinâmicas que mudam com frequência} são processados pelo servidor web de origem na porta configurada. Essa configuração pode ser feita para proteger um servidor intranet da Internet e reduzir a carga nos servidores web públicos mantidos na intranet, por exemplo, criando umfront end para um servidor web.
A lacuna é corretamente preenchida por a} cache HTTP.
b} acelerador HTTPS.

cj proxy estático-dinâmico,
d} filtro de logs.

e)proxy reverso.

Comentário:

Vimos que essas são as características do proxy reverso, conforme figura abaixo:

Gabarito: E

9. FCC - TRT - 6- Região (PE)/Analista Judiciário - TI/2012

Protocolos de rede podem ser classificados como "sem estados" (statelessj ou "com estado" (stateful). A este respeito é correto afirmar que a) protocolos sem estados exigem que tanto cliente como servidor mantenham um histórico da conexão.
b) o uso de cookies é uma maneira de contornar o fato de que HTTP é um protocolo com estados.
c) protocolos sem estados têm a desvantagem de não admitir encapsulamento criptográfico.
d) o uso de cookies é uma maneira de contornar o fato de que HTTP é um protocolo sem estados.
e) protocolos com estados exigem que cada mensagem trocada entre cliente e servidor contenha informação respectiva ao estado da transação.
Comentário:

Vimos que o HTTP é um protocolo sem estados. Vale lembrar que o conceito de persistência é diferente do fato de não armazenar estado. Nesse sentido, uma alternativa é a utilização de cookies no lado do cliente para que o servidor possa obter algumas informações e tentar retomar alguns aspectos ou características do usuário com vistas a"simular" uma condição com estados.

Gabarito: D

10.FCC - TJ-AP/Analista Judiciário - TI/2014

O protocolo HTTPS (HyperText Transfer Protocol Secure) é uma implementação elaborada a partir do protocolo HTTP, na qual se incorporou uma camada de segurança.
O protocolo de segurança originalmente utilizado nessa camada é o a) POP3 (Post Office Protocol).
b) SMTP (Simple Mail Transfer Protocol).

c) IMAP (Internet Message Access Protocol).

d) SSL (Secure Sockets Layer).

e) SSH (Secure Shell).

Comentário:

Conforme vimos, pode ser tanto SLL quanto TLS.

Gabarito: D

ll.FCC - Câmara Municipal de São Paulo - SP/Consultor Técnico Legislativo -
lnformática/2014

Quando há incompatibilidade entre as versões do protocolo HTTP instaladas no cliente e no servidor, é retornado um código de estado 5xx, com uma mensagem como "O servidor não é compatível com a versão do protocolo HTTP usada na solicitação".
Comentário:

Entrando mais no detalhe, o código específico é o de número 505. Lembrando que o grupo 5xx corresponde a erros ou negativa por parte do servidor.
Gabarito: C

12.FCC - TRE-CE/Técnico Judiciário - Operação de Computador/2012

0 protocolo HTTPS é uma implementação do protocolo HTTP utilizando um meio de comunicação seguro entre dois computadores, como por exemplo TLS/SSL. Por padrão, a porta TCP utilizada para a comunicação HTTPS é a porta a) 80.
b) 443.

c) 993.

d) 465.

e) 512.

Comentário:

Mais uma questão bem tranquila, certo? A porta padrão do HTTP é 80 e a sua utilização de modo seguro se dá através da porta 443, ambos no protocolo TCP.
Gabarito: B

13.FCC - AL-SP/Agente Técnico Legislativo Especializado - Segurança de Redes/2010

Protocolos de rede podem ser classificados como "sem estados" (stateless) ou "com estado" (stateful). Um exemplo de protocolo "sem estados" é o protocolo a) HTTP.
b) FTP.

c) SMTP.

d) DHCP.

e) NFS.

Comentário:

Pessoal, muito cuidado para não confundir o critério de ser com ou sem estados com o fato de ser persistente ou não (conexão). O HTTP, seja ele persistente ou não, sempre será sem estados ou stateless.
Gabarito: A

LISTA DE EXERCÍCIOS

HTTP

1. CESPE - STJ/Analista Judiciário - Suporte em TI/2015

Uma forma de se melhorar o desempenho do acesso a páginas web frequentemente visitadas é armazenar-se o conteúdo dessas páginas para que sejam rapidamente carregadas em solicitações futuras, estando, entre os possíveis processos para executar essa tarefa, o proxy, ao qual serão encaminhadas todas as requisições de acesso a páginas web.
2. CESPE - TJ TRE MS/Apoio Especializado/Programação de Sistemas/2013

0 elemento em que uma das partes de uma informação é armazenada como cadeia de texto na máquina do usuário e cuja função principal é a de manter a persistência de sessões HTTP é denominado a) frame.
b) Java Script.

c) tag.

d) cookie.

e) XML.

3. CESPE - TJ TRE MS/Apoio Especializado/Programação de Sistemas/2013

Com referência ao Hyper Text Transfer Protocol (HTTP) — protocolo de aplicação utilizado para o tratamento de pedidos e respostas entre cliente e servidor na Internet e com o qual, normalmente, são desenvolvidas as aplicações para a Web —, assinale a opção em que todas as expressões identificam métodos de requisição HTTP que devem ser implementados por um servidor HTTP 1.1 usado pelo cliente.
a) SOAP, WS, WSDL, UDDI

b) TCP, IP, NETBIOS, UDP, IPX

c) NFS, SMB, IPP, SMTP, P0P3,1MAP,XMPP, SIP

d) SET, GET, CONSTRUCTOR, DESTRUCTOR

e) GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS

4. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

0 protocolo HTTP, que não armazena informações sobre o estado do cliente, classifica-se como do tipo stateless.
5. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

Um servidor HTTP consiste em um servidor de aplicações.

6. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

Ao receber uma requisição, o servidor procura pelo recurso requisitado e envia, ao cliente,
uma resposta com um código, que pode iniciar-se por lxx, que indica sucesso no recebimento da requisição; 2xx, que indica redirecionamento da requisição; 3xx, que informa erros acontecidos no cliente; e 4xx, que informa erros no servidor.
7. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

>1$ estratégias usadas para diminuir o tráfego causado pelo grande número de acessos a páginas web podem ser do tipo cache web, que é implementado no cliente, no GETcondicional ou na rede servidor Proxy Web.

8. CESPE - MPU/Analista Judiciário - Suporte e lnfraestrutura/2013

Os servidores proxy criam um cache com as solicitações de cada usuário, deforma a otimizar consultas futuras de um mesmo usuário, sendo esse cache de uso exclusivo de seu respectivo usuário.
9. CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

0 código abaixo ilustra uma resposta de um servidor web.

GET /internet/index.html HTTP/1.0
üser-agente: Mozilla /4.5 [en] (WinNT; I)
AcceptP: text/plain, text/html, image/gif, image/x-xbitmap,
image/jpeg, image/pjpeg, image/png, */*
Accept-Charset: isso-8859-1, *, utf-8
Accept-Enconding: gzip

Accept-Language: em

10.CESPE - TJ TRTIO/Apoio Especializado/Tecnologia da lnformação/2013

0 protocolo HTTP utiliza, por padrão, a porta 80 para tráfego seguro de dados, sendo o pacote de sincronismo da conexão o responsável por indicar o tipo de cifra que será utilizado na sessão.
11.CESPE - TJ TRT17/Apoio Especializado/Tecnologia da lnformação/2013

Como maneira de se evitar o desenvolvimento de novos protocolos de camada de aplicação, diversas aplicações usam o HTTP como forma de transferir dados fim afim na camada de aplicação.
12.CESPE - Tec MPU/Técnico Administrativo/Tecnologia da Informação e
Comunicação/2013

0 serviço HTTP é implementado sem estado, enquanto o HTTPS é sua versão stateful (com estado].
13.CESPE - Ana MPU/Tecnologia da Informação e Comunicação/Suporte e lnfraestrutura/2013
A primeira versão do serviço HTTP utiliza conexões não persistentes; a persistência foi acrescentada na versão subsequente desse serviço.
14.CESPE - TRT(DF e GO)/Técnico Judiciário - Tecnologia da lnformação/2013

Os servidores de HTTP mais utilizados atualmente são Apache HTTP Server, Internet
Information Server e Enterprise Server.

15.CESPE - CNJ/Técnico Judiciário - Programação de Sistemas/2013

Se o endereço de página inicia com HTTPS, então os dados serão transmitidos por meio de uma conexão cifrada e a autenticidade do servidor e do cliente será verificada com o uso de certificados digitais.
16.CESPE-TCU/Analista de Controle Externo-TI/2007

0 protocolo HTTP, definido nas RFCs 1945 e 2616, não permite a utilização de conexões persistentes.
17.CESPE - TRT - 17^ Região (ES)/Técnico Judiciário - TI/2013

HTTPS usa certificados digitais, requer o uso de TLS e utiliza a porta 443 por padrão.

18.CESPE - TRE-GO/Técnico Judiciário/2015

Na busca de um produto em uma loja virtual por meio de um webservice, quando o produto é encontrado, o protocolo HTTP retorna um HTTP/1.1 404, o que facilita o tratamento do pedido no programa cliente.
19.CESPE - TRE-GO/Técnico Judiciário - Programação de Sistemas/2015

Por meio do protocolo chave HTTP, é possível utilizar o método PUT para se criar um novo recurso de um webservice.
20.CESPE - TRE-GO/Técnico Judiciário - Programação de Sistemas/2015

Uma conexão entre um computador cliente a um computador considerado servidor, para visualizar uma página web, através do protocolo HTTP, é possível afirmar que será utilizado o protocolo de transporte TCP (transmission control protocol).
21.CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015

A técnica de compressão não é recomendada ao se utilizar a versão 2 do HTTP sobre o protocolo TLS 1.2.
22.CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015

Na implementação do HTTP versão 2 sobre o protocolo TLS 1.2, é mandatário desabilitar a renegociação da conexão.
23.CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015

No HTTP, a técnica geral do controle de fluxo garante que não haja interferência entre as conexões independentes. Entretanto essa técnica foi abandonada na versão 2 do HTTP, que criou o conceito de WINDOWJJPDATEframe.
GABARITO

GABARITo - QUESTõES CESPE

1 C

2 D

3 E

4 C

5 E

6 E

7 C

8 E

9 E

10 E

11 C

12 E

13 C

14 C

15 c

16 E

17 c

18 E

19 C

20 c

21 c

22 c

23 E

LISTA DE EXERCÍCIOS COMPLEMENTARES

HTTP

1. FCC - TRT - 155 Região/Analista Judiciário - TI/2015

Um serviço da internet utiliza diferentes protocolos, por exemplo, protocolos relacionados com a função de roteamento, transmissão de dados e transferência de hipertexto para efetivar a comunicação. Os respectivos protocolos, do conjunto (suite) de protocolosTCP/IP, relacionados com as funções apresentadas, são:

a) IP, TCP e HTTP.

b) TCP, FTP e HTML.

c) IP, FTP e HTML.

d) ARP, FTP e HTTP.

e) TCP, IP e HTTP.

2. FCC - TRT - 165 Região(MA)/Técnico Judiciário - TI/2014

Os diversos protocolos do conjunto (suite) TCP/IP são organizados em camadas de funcionalidade. Quando um usuário da internet realiza um acesso à página Web, ele está utilizando o protocolo da camada de Aplicação denominado a) WWW.
b) IMAP.

c) HTTP.

d) TCP.

e) IP.

3. FCC - TRT - 25 Região (SP)/Técnico Judiciário - TI/2014

No modelo de referência de 4 camadas da suíte de protocolos TCP/IP, os protocolos
Ethernet, HTTP e ICMP localizam-se, respectivamente, nas camadas a) Internet, Apresentação e Interface de rede b) Interface de rede, Aplicação e Internet.
c) Transporte, Internet e Interface de rede.

d) Transporte, Aplicação e Enlace de dados.

e) Física, Transporte e Enlace de dados.

4. FCC - TRF - 4^ Região/Técnico Judiciário - TI/2014

Pedro, técnico em informática do TRF da 4ã Região, deve comprovar os seus conhecimentos sobre o modelo OSI identificando os protocolos às respectivas camadas do modelo. Assim,um correto relacionamento identificado por Pedro é:

a) FTP - Camada de Transporte.

b) HTTP - Camada de Transporte.

c) ICMP - Camada de Aplicação.

d) HTTP - Camada de Aplicação.

e) SNMP - Camada de Rede.

5. FCC - TRF - 25 Região/Analista Judiciário - lnformática/2012

Sobre 0 protocolo HTTP, é correto afirmar:

a) Usa 0 TCP e o UDP como seus protocolos de transporte e presta serviço por default na porta 80.
b) Em uma mensagem de requisição HTTP, a linha de cabeçalho User-agent: especifica o agente de usuário, isto é, o browser que está fazendo a requisição ao servidor.
c) Quando utiliza conexões persistentes, cada conexão TCP é encerrada após 0 servidor enviar o objeto resposta ao cliente que fez a requisição. Cada conexão TCP transporta exatamente uma mensagem de requisição e uma mensagem de resposta.
d) A resposta do servidor a uma requisição HTTP é dividida em três seções. A primeira é denominada cabeçalho (header) e contém informações do servidor sobre o recurso solicitado. A segunda seção é denominada corpo (body) e contém 0 recurso propriamente dito. A terceira seção, denominada rodapé (footer), contém informações de status da requisição e 0 relatório de erros, quando houver.
e) Os únicos métodos (comandos) de requisição do protocolo HTTP são GET e POST. 0
status de retorno de número 404 do método HTTP indica que o serviço está indisponível.

6. FCC - TCE-SP/Auxiliar de Fiscalização Financeira/2012

Sobre 0 protocolo HTTP, é correto afirmar:

a) Se um cliente solicita ao servidor o mesmo objeto duas vezes em um período de poucos segundos, 0 servidor responde dizendo que acabou de enviar 0 objeto ao cliente e não envia novamente o objeto.
b) É implementado em dois programas: um programa cliente e outro servidor. Os dois programas, implementados em sistemas finais diferentes, conversam um com o outro por meio da troca de mensagens HTTP. 0 HTTP não define a estrutura dessas mensagens, mas define 0 modo como cliente e servidor as trocam.
c) 0 HTTP usa o TCP como seu protocolo de transporte subjacente. 0 cliente HTTP
primeiramente inicia uma conexão TCP com o servidor. Uma vez estabelecida a conexão,
os processos do browser e do servidor acessam o TCP por meio de suas interfaces socket.

d) Os servidores web implementam apenas o lado cliente do HTTP e abrigam objetos web, cada um endereçado por um URL. 0 Apache e o IIS são servidores web populares.
e) 0 HTTP define como clientes web requisitam páginas web aos servidores, mas não define como eles as transferem aos clientes.
7. FCC - MPE-AM/Agente de Apoio - Manutenção e Suporte de lnformática/2013

HTTPS (HyperText Transfer Protocol Secure) é um protocolo que combina o uso do HTTP
com o a) SSL e o TLS, afim de prover conexões seguras.
b) DES e AES, afim de prover criptografia assimétrica.

c) RSA, a fim de prover certificação digital por meio de criptografia simétrica.

d) IDS e IPS, a fim de prover segurança contra invasores.

e) IMAP e POP, a fim de prover comunicação segura.

8. FCC - TRF -1^ Região/Analista Judiciário - Área de Apoio Especializado/2014

0recebe os pedidos HTTP na porta configurada e processa todos os pedidos da web que chegam, podendo distribuí-los. Os pedidos de objetos que podem ser armazenados no cache (informações estáticas que não mudam com frequência como páginas em HTML e imagens GIF) são processados pelo proxy. Os pedidos de objetos que não podem ser armazenados no cache (informações dinâmicas que mudam com frequência) são processados pelo servidor web de origem na porta configurada. Essa configuração pode ser feita para proteger um servidor intranet da Internet e reduzir a carga nos servidores web públicos mantidos na intranet, por exemplo, criando umfront end para um servidor web.
A lacuna é corretamente preenchida por a) cache HTTP.
b) acelerador HTTPS.

c) proxy estático-dinâmico.

d) filtro de logs.

e) proxy reverso.

9. FCC - TRT - 65 Região (PE)/Analista Judiciário - TI/2012

Protocolos de rede podem ser classificados como "sem estados" (stateless) ou "com estado" (stateful). A este respeito é correto afirmar que a) protocolos sem estados exigem que tanto cliente como servidor mantenham um histórico da conexão.
b) o uso de cookies é uma maneira de contornar o fato de que HTTP é um protocolo com estados.
c) protocolos sem estados têm a desvantagem de não admitir encapsulamento criptográfico.
d) o uso de cookies é uma maneira de contornar o fato de que HTTP é um protocolo sem estados.
e) protocolos com estados exigem que cada mensagem trocada entre cliente e servidor contenha informação respectiva ao estado da transação.
10. FCC - TJ-AP/Analista Judiciário - TI/2014

0 protocolo HTTPS (HyperText Transfer Protocol Secure) é uma implementação elaborada a partir do protocolo HTTP, na qual se incorporou uma camada de segurança.0 protocolo de segurança originalmente utilizado nessa camada é o a) P0P3 (Post Office Protocol).
b) SMTP (Simple Mail Transfer Protocol).

c) IMAP (Internet Message Access Protocol).

d) SSL (Secure Sockets Layer).

e) SSH (Secure Shell).

11.FCC - Câmara Municipal de São Paulo - SP/Consultor Técnico Legislativo -
lnformática/2014

Quando há incompatibilidade entre as versões do protocolo HTTP instaladas no cliente e no servidor, é retornado um código de estado 5xx, com uma mensagem como "0 servidor não é compatível com a versão do protocolo HTTP usada na solicitação".
12.FCC - TRE-CE/Técnico Judiciário - Operação de Computador/2012

0 protocolo HTTPS é uma implementação do protocolo HTTP utilizando um meio de comunicação seguro entre dois computadores, como por exemplo TLS/SSL. Por padrão, a porta TCP utilizada para a comunicação HTTPS é a porta a) 80.
b) 443.

c) 993.

d) 465.

e) 512.

13.FCC - AL-SP/Agente Técnico Legislativo Especializado - Segurança de Redes/2010

Protocolos de rede podem ser classificados como "sem estados" (stateless) ou "com estado" (stateful). Um exemplo de protocolo "sem estados" é o protocolo a) HTTP.
b) FTP.

c) SMTP.

d) DHCP.

e) NFS.

GABARITO

GABARITo - QUESTõES FCC

1 A

2 C

3 B

4 D

5 B

6 C

7 A

8 E

9 D

10 D

11 C

12 B

13 A

SSL(SECURITY SoCKET LAYER) E TLS (TRANSPoRT LAYER
SECURITY)

Este é um assunto cobrado recorrentemente em concursos que contêm a disciplina de segurança e por vezes não é explicitamente mencionado no edital por ser um protocolo e recurso de segurança presente em vários outros protocolos e serviços.
O protocolo SSL surgiu a partir da necessidade de se obter uma comunicação segura em meios compartilhados como a Internet. Em termos práticos, o objetivo era possibilitar a criação de um meio suficientemente seguro para garantir a confidencialidade de transações bancárias que são a base para o comércio eletrônico. Nesse sentido, investiu-se pesado em métodos de criptografia para criação desses túneis.
Ao longo do tempo, surgiu então o sucessor do SSL, conhecido como TLS, com algumas diferenças que mencionaremos em momento oportuno. Para termos uma ideia cronológica da evolução desse protocolo, vamos ver a figura a seguir:
SSL 1.0

design complete

SSL 2.0

product ships

PCT1.0

publtshcd

SSL 3.0

publisbed

TLS WG

formcd

TLS 1.0

publisbed

993 1 994 1995 1996 1997

NCSA

Mosaic rdeased
Internet
Exploror relcascd
Netscape
Navigatoc releascd
SSL

Falando agora especificamente das características do SSL, é importante destacarmos que ele permite o envio de informações de forma segura até um destino específico, agregando recursos de autenticidade, integridade e confidencialidade.
O intuito de sua criação, era criar uma camada de segurança para que as aplicações como HTTP,POP3 e SMTP pudessem ter tais recursos. Assim, criou-se o SSL de tal modo que fosse independentemente do tipo de protocolo utilizado na camada da aplicação e que pudesse rodar sobre as camadas mais inferiores. Por esse motivo, temos que o SSL se posiciona em uma camada intermediária entre as camadas de aplicação e transporte da arquitetura TCP/IP conforme imagem abaixo:
Camada de Aplicação (HTTP)

O desenvolvimento original foi realizado pela Netscape, chegando a desenvolver três versões do protocolo.
Assim, um exemplo de utilização de protocolo é através das comunicações WEB via HTTP
de modo seguro, utilizando o SSL. Essas comunicações passam a funcionar em uma porta diferente e são chamadas de HTTPS. Uma característica do SSL é ser transparente ao usuário.
Ao trazermos os principais objetivos a serem alcançados pelo SSL, podemos listar:

* Autenticação entre clientes e servidores;

* Garantia da Integridade dos dados (caso estes sejam alterados, pode-se detectar facilmente);
* Garantia da Confidencialidade: As informações transmitidas não podem ser interceptadas e interpretadas devido ao uso da criptografia, devendo ser lida apenas pelo destinatário que possui a chave de sessão.
Desse modo, diz-se que o SSL não é um protocolo simples e único, mas sim um conjunto de protocolos auxiliares que atuam em conjunto em prol dos objetivos acima. Esse conjunto de protocolos pode ser dividido em duas camadas:
* Camada de segurança e integridade dos dados: SSL Record;

* Camada de conexão SSL: SSL Handshake protocol, SSL ChangeCipher SpecProtocol e SSL
Alert Protocol.

Assim, para termos um aspecto visual da estrutura do protocolo, podemos analisar a imagem a seguir:
Handshake
Protocol

Alert
Protocol

Change
Cipher
Spec

Record Protocol

Falando um pouco sobre cada um dos protocolos:

* Handshake Protocol - Responsável pelo estabelecimento da comunicação segura e autenticação das partes, com a escolha dos algoritmos de criptografia.Falaremos mais detalhadamente a seguir.
* Alert Protocol - É o protocolo responsável pelo controle do protocolo através da troca de mensagens vinculadas ao funcionamento e transmissão de dados na conexão. Faz algo semelhante ao protocolo ICMP em relação ao IP. Possui duas identificações clássicas:
"Warning" e "Fatal". Ao ser enviado uma mensagem do tipo FATAL, a transmissão é interrompida imediatamente. Possui uma estrutura de dois bytes em que o primeiro é o tipo da falha e o segundo diz respeito ao alerta ou erro ocorrido.
* Change Cipher Spec - É constituído por um tipo de mensagem que caracteriza um marco onde, a partir dessa mensagem, toda comunicação será criptografada conforme negociações feitas no estabelecimento da comunicação. É uma mensagem de duas vias, onde ambas as partes precisam emitir essa mensagem. Assim, diz-se que a sessão SSL de fato está aberta e será utilizado o RECORD PROTOCOL.
* Record Protocol - Protocolo responsável pelo encapsulamento dos dados. Esse protocolo recebe os dados abertos da camada superior, encapsula, encripta e/ou adiciona o MessageAuthentication Codes (MACs) para garantir a segurança. É nessa fase que percebemos a total independência dos protocolos.
Importante mencionar que o algoritmo aqui utilizado é simétrico,
conforme princípios de criptografia, além da capacidade de se comprimir as mensagens.
O estabelecimento de uma conexão SSL se dá em etapas. Toda comunicação começa com oHANDSHAKE PROTOCOL. Detalhando um pouco mais essa fase, temos que essas etapas permitem a definição de algoritmos para geração de chaves de sessão. As etapas são:
1. Negociação dos Algoritmos - Busca-se definir qual algoritmo é suportado por ambos e será utilizado. A tendência é escolher sempre o algoritmo mais robusto. O cliente faz a requisição da comunicação segura e o servidor responde com uma lista de algoritmos suportados.
2. Troca de Chaves e Autenticação - Após a ciência e definição pelo servidor do algoritmo,ambos trocam chaves para realizarem a autenticação entre si. Nesse primeiro momento,utiliza-se algoritmos de criptografia assimétrica como RSA, Diffie-Hellman, entre outros.

Aplica-se aqui o conceito de certificado digital por parte do servidor com todas as informações inerentes a essa tecnologia.
3. Encriptação simétrica e autenticação das mensagens - A partir de então as mensagens utilizam funções HASH para autenticação, garantindo assim a integridade,segurança e autenticação.
Traduzindo em termos de fluxo a dinâmica apresentada, vejamos a imagem a seguir:

Ainda, com vistas a materializar ainda mais essa dinâmica, podemos perceber em um cenário real de captura de pacotes por meio do Wireshark, o respectivo fluxo:
No. Time Source Des tina tion Protocol Length Into
18 22.330973 10.10.20.16 10.10.20.101 TCP
162 42718 -» 443 [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK PERM=1 TSval=2820682635
TSecr=0 WS=64

\ 19 22.331147 10.10.20.101 10.10.20.16 TCP
181 443 42718 [SYN, ACK] Seq=0 Ack=l Win=4380 Len=0 MSS=1460 TSval=3550930914
TSecr=2820682635 SACK PERM=1

/>y20 22.332539 10.10.20.16 10.10.20.101 TCP
173 42718 -» 443 [ACK] Seq=l Ack=l Win=14600 Len=0 TSval=2820682637 TSecr=3550930914

21 22.582442 10.10.20.16 10.10.20.101 TLSvl
253 Client Hello

22 22.588323 10.10.20.101 10.10.20.16 TCP
173 443 -» 42718 [ACK] Seq=l Ack=81 Win=4460 Len=0 TSval=3550931166 TSecr=2820682886

23 22.591846 10.10.20.101 10.10.20.16 TLSvl
1743 Server Hello, Certificate, Server Key Exchange, Server Hello Done

24 22.592228 10.10.20.16 10.10.20.101 TCP
173 42718 -» 443 [ACK] Seq=81 Ack=1449 Win-17376 Len=0 TSval=2820682896 TSecr=3550931173

25 22.593567 10.10.20.16 10.10.20.101 TCP
173 42718 -> 443 [ACK] Seq=81 Ack=1571 Win=17376 Len=0 TSval=2820682896 TSecr=3550931173

26 22.602640 10.10.20.16 10.10.20.101 TLSvl
371 Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message

27 22.602672 10.10.20.101 10.10.20.16 TCP
173 443 -> 42718 [ACK] Seq=1571 Ack=279 Win=4658 Len=0 TSval=3550931186 TSecr=2820682907

28 22.604871 10.10.20.101 10.10.20.16 TLSvl
179 Change Cipher Spec

29 22.604882 10.10.20.101 10.10.20.16 TLSvl
226 Encrypted Handshake Message

30 22.605190 10.10.20.16 10.10.20.101 TCP
173 42718 -> 443 [ACK] Seq=279 Ack=1630 Win=17376 Len=0 TSval=2820682909 TSecr=3550931188

31 22.605432 10.10.20.16 10.10.20.101 TLSvl
370 Application Data

32 22.605445 10.10.20.101 10.10.20.16 TCP
173 443 -» 42718 [ACK] Seq=1630 Ack=476 Win=4855 Len=0 TSval=3550931189 TSecr=2820682909

33 22.612455 10.10.20.101 10.10.20.16 TLSvl
498 Application Data

34 22.612462 10.10.20.101 10.10.20.16 TCP
173 443 -» 42718 [FIN, ACK] Seq=1955 Ack=476 Win=4855 Len=0 TSval=3550931196
TSecr=2820682909

35 22.612884 10.10.20.16 10.10.20.101 TLSvl
210 Encrypted Alert

36 22.612904 10.10.20.101 10.10.20.16 TCP
173 443 -» 42718 [ACK] Seq=1956 Ack=513 Win=4892 Len=0 TSval=3550931196
TSecr=2820682917

37 22.613451 10.10.20.16 10.10.20.101 TCP
173 42718 -» 443 [FIN, ACK] Seq=513 Ack=1956 Win=20272 Len=0 TSval=2820682917
TSecr=3550931196

38 22.613494 10.10.20.101 10.10.20.16 TCP
173 443 -» 42718 [ACK] Seq=1956 Ack=514 Win=4892 Len=0 TSval=3550931197 TSecr=2820682917

TLS

Conforme vimos anteriormente, o SSLfoi desenvolvido pela Netscape. Trazendo o desenvolvimento dessa solução de modo independente de plataforma, o IETF assumiu tal responsabilidade,renomeando, assim, para TLS. Este foi baseado na versão 3.0 do protocolo SSL.

Atualmente não se faz tanto essa distinção, sempre nos referenciando ao conjunto de ambos:SSL/TLS. Isso se deve por não haver uma distinção substancial destes protocolos.

Agora um fato muito importante para prova Estes dois protocolos não são compatíveis,
isto é, eles não interoperam entre si.
Abordando então as diferenças entre esses protocolos, podemos citar:

* O TLS tem a capacidade de trabalhar em portas diferentes e usa algoritmos de criptografia mais robustos como o HMAC, enquanto o SSL suporta apenas o MAC.
* O TLS, quando utilizado em infraestrutura de chaves públicas, pode ser utilizado por uma autoridade intermediária, não necessitando recorrer à raiz de um Autoridade deCertificação como o SSL.
OPENSSL

O OpenSSL é a implementação em código aberto dos padrões estudados anteriormente. Muita atenção, pois, apesar do nome, o OpenSSL também suporta o TLS.
A sua codificação é escrita em linguagem C. Por ser um código aberto, visa sempre integrar os mais diversos protocolos e linguagens. Pode-se utilizar o Wrapper que permite a integração com várias outras linguagens. Atualmente se encontra na versão 1.0.2.
Possui suporte a uma gama de algoritmos de criptografia, conforme listagem abaixo:

Algoritmos simétricos: AES (128,192 e 256), Blowfish, Camellia, SEED,
CAST128, DES, IDEA, RC2, RC4, RC5, Triple DES, GOST 28147-89

- Algoritmos assimétricos: RSA, DSA, Diffie-Hellman key exchange, Elliptic curve, GOST R
34.10-2001

- Funções HASH: MD5, MD4, MD2, SHA-1, SHA-2, RIPEMD-160, MDC-2, GOST R 34.11-94

Suporta ainda outros protocolos agregados como o S/MIME, bastante utilizado para assinatura e cifragem de mensagens de e-mail.
EXERCÍCIOS COMENTADOS

SSL/TLS

1. CESPE - FUB/Técnico de TI/2015

O protocolo SSL (secure socket layer) é utilizado em diversas aplicações TCP/IP para que se aumente a segurança na transmissão de dados. Ele é composto por protocolos base e auxiliares, tais como o SSL Record Protocol, responsável pelo transporte de informações autenticada e encriptada.
Comentários:

Vimos que são exatamente esses os objetivos e as características do protocolo SSL.
Relembrando das diversas camadas, temos:

Handshake
Protocol

Alert
Protocol

Change
Cipher
Spec

I 1

Record Protocol

E de fato, a camada SSL Record Protocolo é responsável pelas funções aqui elencadas.

Gabarito: C

2. CESPE - TJ-ES/Analista Judiciário - Análise de Suporte/2011

HTTPS — o HTTP usado sobre o SSL (secure socket layer) — é uma alternativa adequada para suprir a necessidade de segurança em alguns serviços a serem disponibilizados no sítio do tribunal em questão. O HTTPS usa como padrão a porta 443, sendo tarefa do SSL,após o estabelecimento da conexão segura, compactar e criptografar os dados.

Comentários:

Vimos na sessão de protocolos da camada de aplicação a capacidade do HTTP de utilizar o SSL, passando a ser chamado de HTTPS. Nesse modo, é utilizado a porta 443 e não mais a porta 80.
Vimos ainda que a camada SSL Record Protocol do SSL implementa compressão dos dados e compactação.
Gabarito: C

3. CESPE - STJ/Técnico Judiciário - lnformática/2008

HTTPS (hyper text transfer protocol securej, que verifica um certificado digital por meio de criptografia simétrica, é uma implementação do protocolo HTTP sobre uma camadaSSL ou TLS.

Comentários:

Pessoal, muita atenção. Conforme mencionamos, a fase de estabelecimento da conexão,
que envolve as consultas e trocas de certificados para troca de chaves será feita através da criptografia assimétrica e não simétrica, conforme mencionado.
Gabarito: E

4. CESPE - TCU/Auditor Federal de Controle Externo/2010

A confidencialidade dos votos não será violada pela captura de tráfego na Internet, sem que sejam quebradas as proteções oferecidas pelo protocolo TLS/SSL.
Comentários:

Conforme vimos, ainda que os dados sejam interceptados, dependerá ainda da quebra da criptografia para que seja possível decriptar as mensagens criptografadas em uma comunicação TLS/SSL.
Gabarito: C

5. CESPE - PC-DF/Agente de Polícia/2013

Os protocolos TLS (Transport Layer Security) e SSL (Secure Sockets LayerJ possuem propriedades criptográficas que permitem assegurar a confidencialidade e a integridade da comunicação.
Comentários:

Questão bem básica a respeito das propriedades e possibilidades do TSL e SSL, certo?

Gabarito: C

6. CESPE - ANP/Analista Administrativo - Área 5/2013

No acesso a um sítio da web que utilize protocolo HTTP, no momento da transferência dos dados para autenticação utilizando usuário e senha, pode-se agregar o TLS/SSL para que os dados sejam criptografados ao serem enviados.
Comentários:

Mais uma questão tratando da capacidade de se enviar uma mensagem confidencial e criptografada a partir do TLS/SSL.
Gabarito: C

7. CESPE - STF/Analista Judiciário - Suporte em Tecnologia da lnformação/2013

0 OpenSSL usa algoritmos de hash, como o SHA1 e MD5.

Comentários:

Em regra, temos que o OpenSSL suporta uma grande diversidade de algoritmos conforme vimos, entre eles SHAÍ e MD5.
Gabarito: C

8. CESPE - STF/Analista Judiciário - Suporte em Tecnologia da lnformação/2013

O OpenSSL não suporta S/MIME, o qual é utilizado para assinar e cifrar mensagens de email.
Comentários:

Mais um protocolo suportado pelo OpenSSL conforme vimos na sessão teórica.

Gabarito: E

9. CESPE - STF/Analista Judiciário - Suporte em Tecnologia da lnformação/2013

0 OpenSSL usa o padrão AES com chaves de 128,192 e 256 bits.

Comentários:

Reforçando mais uma vez a nossa lista de protocolos suportados pelo OpenSSL.

Gabarito: C

EXERCÍCIOS COMENTADOS COMPLEMENTARES

SSL

1. FCC - TRT-MG/Analista Judiciário/2015

Para reduzir a vulnerabilidade dos acessos pelo protocolo HTTP, foi introduzido, acima desse protocolo, o SSL, originando assim o HTTPS. O HTTPS
(A) realiza a autenticação do endereço IP que visita os sites.

(B) criptografa o endereço IP origem que visita os sites.

(C) torna o protocolo IP mais seguro por meio da checagem da integridade.

(D) criptografa o pacote TCP por completo.

(E) provê recursos de autenticação de sites visitados.

Comentário:

Temos aqui uma questão que pode ter gerado problema para alguns candidatos. Na prática, as principais características do HTTPS é garantir a confidencialidade através de um túnel criptografado e realizar a autenticação dos sites visitados,garantindo um aspecto de legitimidade, principalmente com o uso de certificados digitais. Entretanto,esses pontos não são exaustivos. Segundo Tanenbaum:

"A SSL constrói uma

1. Negociação de

2. Autenticação
3.

conexão segura parâmetros mútua de
Comunicação entre dois soquetes,entre cliente e cliente e incluindo:servidor.
servidor.
secreta.

4. Proteção da integridade dos dados"

Diante desse posicionamento, percebemos que com o uso do HTTPS, podemos utilizar também de recursos de autenticação do lado do cliente, além de prover recursos de integridade.
Entretanto pessoal, percebam que o SSL atua em uma camada intermediária entre a camada de aplicação e transporte da arquitetura TCP/IP. Ou seja, não há o que se falar de implementação do SSL para prover recursos de segurança em um sentido amplo para os protocolos TCP/UDP ou IP, pois estão abaixo da implementação do SSL. O protocoloHTTP sim usufruirá desses recursos através do encapsulamento dos dados pelo SSL.

Gabarito: E

LISTA DE EXERCÍCIOS

SSL/TLS

1. CESPE - FUB/Técnico de TI/2015

0 protocolo SSL (secure socket layer) é utilizado em diversas aplicações TCP/IP para que se aumente a segurança na transmissão de dados. Ele é composto por protocolos base e auxiliares, tais como o SSL Record Protocol, responsável pelo transporte de informações autenticada e encriptada.
2. CESPE - TJ-ES/Analista Judiciário - Análise de Suporte/2011

HTTPS — o HTTP usado sobre o SSL (secure socket layer) — é uma alternativa adequada para suprir a necessidade de segurança em alguns serviços a serem disponibilizados no sítio do tribunal em questão. 0 HTTPS usa como padrão a porta 443, sendo tarefa do SSL,após o estabelecimento da conexão segura, compactar e criptografar os dados.

3. CESPE - STJ/Técnico Judiciário - lnformática/2008

HTTPS (hyper text transfer protocol secure), que verifica um certificado digital por meio de criptografia simétrica, é uma implementação do protocolo HTTP sobre uma camadaSSL ou TLS.

4. CESPE - TCU/Auditor Federal de Controle Externo/2010

A confidencialidade dos votos não será violada pela captura de tráfego na Internet, sem que sejam quebradas as proteções oferecidas pelo protocolo TLS/SSL.
5. CESPE - PC-DF/Agente de Polícia/2013

Os protocolos TLS (Transport Layer Security) e SSL (Secure Sockets Layer) possuem propriedades criptográficas que permitem assegurar a confidencialidade e a integridade da comunicação.
6. CESPE - ANP/Analista Administrativo - Área 5/2013

No acesso a um sítio da web que utilize protocolo HTTP, no momento da transferência dos dados para autenticação utilizando usuário e senha, pode-se agregar o TLS/SSL para que os dados sejam criptografados ao serem enviados.
7. CESPE - STF/Analista Judiciário - Suporte em Tecnologia da lnformação/2013

0 OpenSSL usa algoritmos de hash, como o SHA1 e MD5.

8. CESPE - STF/Analista Judiciário - Suporte em Tecnologia da lnformação/2013

0 OpenSSL não suporta S/MIME, o qual é utilizado para assinar e cifrar mensagens de email.
9. CESPE - STF/Analista Judiciário - Suporte em Tecnologia da lnformação/2013

0 OpenSSL usa o padrão AES com chaves de 128,192 e 256 bits.

GABARITO

GABARITo - QUESTõES CESPE

1 C

2 c

3 E

4 C

5 c

6 c

7 c

8 E

9 c

SSL (SECURITY SoCKET LAYER) E TLS (TRANSPoRT LAYER SECURITY)

1. FCC - TRT-MG/Analista Judiciário/2015

Para reduzir a vulnerabilidade dos acessos pelo protocolo HTTP, foi introduzido, acima desse protocolo, o SSL, originando assim o HTTPS. 0 HTTPS
(A) realiza a autenticação do endereço IP que visita os sites.

(B) criptografa o endereço IP origem que visita os sites.

(C) torna o protocolo IP mais seguro por meio da checagem da integridade.

(D) criptografa o pacote TCP por completo.

(E) provê recursos de autenticação de sites visitados.

GABARITo - QUESTõES FCC

