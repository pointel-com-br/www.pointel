# Engenharia de Computadores e Redes - IaaS - Infraestrutura com Serviço. SaaS - Software como Serviço. PaaS - Plataforma como Serviço

Índice

1) Computação em Nuvem

Sumário

Cluster, Grid e Balanceamento de Carga

Cluster

Grid

Balanceamento de Carga

Computação em Nuvem (Cloud Computing)

Co-location

Hosting

Nuvem Privada

Nuvem Pública

Nuvem Comunitária

Nuvem Híbrido

Arquiteturas de Cloud Computing

Infrastruture as a Service (laaS)

Platform as a Service (PaaS)

Software as a Service (SaaS)

Communication as a Service (CaaS)

Data base as a Service (DBaaS)

Function as a Service (FaaS)

Everything as a Service (XaaS)

Workloads.

Tipos de migração

Serverless.

Serviços AWS- GOOGLE - AZURE

Questões Comentadas.

Cluster e Grid

Computação em Nuvem

Questões Comentadas Complementares.

Computação em Nuvem

Lista de Questões.

Cluster e Grid

Computação em Nuvem

Lista de Questões Complementares.

Computação em Nuvem

Gabarito.

Gabarito - Questões CESPE

Gabarito - Questões FCC

Resumo

Considerações Finais

CLUSTER, GRID E BALANCEAMENTo DE CARCA

Temos aqui alguns conceitos muitos importantes que serviram como premissas dos serviços de computação em nuvem, os quais veremos no tópico a seguir.
A ideia por trás dos termos que veremos sempre estará vinculada a agregar recursos de dispositivos individuais com vistas a otimizar o desempenho quando estes atuam em conjunto.
Com essa ideia em mente, vamos avaliar cada um deles.

INDO MAIS

FUNDO!

CLUSTER

De forma bem objetiva temos que o Cluster é um agregado de computadores conectados entre si via hardware ou software que compartilham seus recursos passando a funcionar como uma única unidade lógica.Todos os dispositivos que pertencem a um cluster visam o mesmo objetivo, ou seja, cooperam para o processamento de determinada requisição em conjunto.
Além disso, atuam debaixo de uma mesma administração ou gerência fornecendo alto desempenho aos usuários ou sistemas. Na maioria dos casos, os computadores ou servidores que fazem parte do Cluster possuem as mesmas características e capacidades, sendo possível distribuir as tarefas de forma igualitária.
GRID

Também chamado de COMPUTAÇÃO EM GRADE. A ideia de compartilhamento de recursos não é diferente.O foco também é aumentar o desempenho de um sistema para o processamento de determinadas requisições. Entretanto, existem algumas características que distinguem o Grid.
Primeiramente, nâo há limitação de espaço e localização como há no Cluster. Dessa forma, pode-se ter computadores espalhados por toda a Internet que compartilham recursos.
Como assim professor?? Explico. Cada dispositivo que faz parte do Grid processa determinadas tarefas e retornam o resultado do processamento ao sistema principal.
A título de exemplo, a NASA tem um projeto em que ela necessita realizar muitos cálculos, muitos mesmo!Dessa forma, qualquer computador na Internet pode se cadastrar no programa e receber algumas tarefas para processar e retornar o resultado à NASA, participando então do Grid.
Algumas outras características que são muito importantes a respeito do Grid:

* A administração e gerência dos dispositivos é descentralizada, ou seja, a NASA não controla os dispositivos pessoais dos usuários que participam do Grid, mas sim os próprios donos;
* As capacidades de processamento sâo diversificadas e heterogêneas. Pode-se ter computadores individuais de alta capacidade de processamento, bem como se pode ter dispositivos bem mais simples com muito mais limitações.
* Utiliza padrões abertos, permitindo assim plena interoperabilidade entre os dispositivos;

(CESPE - SERPRO/Analista- Suporte Técnico/2008) Nos GRIDs, a alocação dos recursos é feita por um gerente de recursos centralizado, e os nós que compõem o GRID trabalham cooperativamente como um recurso unificado. Nos clusters, cada nó tem seu gerente de recursos. Os nós em clusters são autônomos e não o sâo nos GRIDs.
Comentários:

Falou em GRID, temos uma gerência descentralizada. Além disso, o recurso não é unificado. Edistribuído tarefas específicas. Temos uma inversão dos conceitos entre CLUSTER e GRID na questão.

Gabarito: E

BALANCEAMENTo DE CARGA

Aqui temos outro recurso muito utilizado em ambientes de rede e datacenters para fornecer serviços em geral. Entre os objetivos do balanceamento de carga estão a distribuição de carga entre os dispositivos que fornecem recursos, aumento de disponibilidade e redução no tempo de resposta às requisições além de maior escalabilidade do sistema.
A ideia atrelada ao balanceamento de carga está em fazer vários servidores que trabalham individualmente responderem por um mesmo serviço ou requisição. Para o cliente ou usuário do serviço, tal funcionamento se torna transparente, pois para ele, o serviço está sendo fornecido por um servidor qualquer.
Com a utilização do balanceamento de carga, pode-se realizar manutenções programadas nos servidores ou dispositivos sem que o serviço seja afetado.
Podemos dividir a implementação do balanceamento de carga em duas categorias:

* Balanceamento de carga por software: Consiste na instalação e configuração de um Software,podendo ser inclusive a nível de sistema operacional, em servidores que fazem parte de um cluster.Podem implementar diversas técnicas. A mais usual e simples é a técnica de
Round-Robin, que nada mais é do que a distribuição uniforme entre os servidores. Isto é, uma requisição para cada um de forma alternada.
* Balanceamento de carga por hardware: Temos que um hardware específico atua como intermediário e é responsável por efetuar a distribuição das requisições entre os dispositivos. Pode ser um switch,roteador ou até mesmo um servidor com tal funcionalidade.

EXEMPLIFICANDO

A seguir temos um exemplo de um cenário sem a implementação de balanceamento de carga:

Percebe-se que todo o tráfego é encaminhado ao servidor de Banco de dados. Já na figura a seguir, temos uma implementação de balanceamento de carga em software:
Podemos verificar a utilização do IP virtual, algo semelhante ao VRRP. No caso em questão, não há a utilização de um balanceador de carga a nível de hardware, pois se utiliza o conceito de IP virtual em que os servidores se comunicam para atender de forma alternada às requisições.
Já na figura abaixo, temos a implementação de um balanceamento em hardware:

,s"'

/

(CESPE - BACEN - Analista de Sistemas/2013) O usuário pode acessar, seus dados armazenados na nuvem, independentemente do sistema operacional e do hardware que esteja usando em seu computador pessoal.
Comentários:

Conforme vimos em aula, é exatamente isso! A integração com os mais diversos dispositivos e a independência de sistemas operacionais ou hardware do lado do cliente é uma característica da computação em nuvem. Algumas pessoas encrencam com o "independentemente" — não vamos criar problemas com a banca. Vamos entender o foco da questão e responder objetivamente.
Gabarito: C

CoMPUTAçÃo EM NUVEM (CLoUD CoMPUTING)

Um Datacenter típico possibilita que diversos serviços sejam disponibilizados e comercializados garantindo os principais requisitos de sistemas robustos. Podemos citar, por exemplo: alta disponibilidade, confiabilidade dos dados, critérios de segurança lógica e física, planos e políticas de recuperação de dados em ambientes críticos, entre outros.
Uma vez que os altos investimentos são realizados para construir ambientes desse tipo
(Ex: Datacenter em uma sala cofre), as grandes empresas buscam aproveitar ao máximo a utilização de seus recursos considerando um retorno sobre o investimento. E nesse contexto que surgem termos comoCo-location e o
Hosting.

INDO MAIS

FUNDO!

CO-LOCATION

O serviço de Co-Location (ou Colocation) contempla o fornecimento de infraestrutura de
Datacenter para os clientes. Isso inclui, em determinado local geográfico diferente do ambiente do cliente e o fornecimento de espaço físico (inclusive racks e bandejas) para instalação dos servidores e outros equipamentos do próprio cliente. Em português, podemos traduzir como Compartilhamento de Localização.
Ele contempla ainda critérios de segurança física (Ex: acesso ao ambiente), medidas contra catástrofes (Ex:continuidade do negócio e disponibilidade), climatizaçõo adequada (Ex: sistemas de ar-condicionado e arrefecimento), energia elétrica, conectividade de rede, ambientes de armazenamento e backups, entre muitas outras coisas.
*

HoSTING

O serviço de hosting está muito mais voltado para o conceito de hospedagem em termos de serviço. Dessa forma, utiliza-se a infraestrutura de terceiros para hospedar determinados serviços que o cliente deseja disponibilizar - a prática mais comum é a hospedagem de sites. O cliente possui as páginas criadas e implementadas, porém depende de um servidor web para disponibilização desses serviços.
Nem sempre o cliente possui seu próprio servidor web e, dessa forma, ele pode contratar o serviço de hosting para a devida hospedagem de seu site. Pessoal, alguns serviços agregados geralmente são incluídos nesse contexto, como políticas de backup, recuperação de dados, espaços extras de armazenamento, banco de dados, entre outros.
Seguindo o mesmo conceito de aproveitamento de infraestrutura, as soluções ofertadas no mercado evoluíram, não mais dependendo de hospedagem física de seus próprios equipamentos como no Colocation.Novos modelos de serviços agora preveem um ambiente completo para o cliente, incluindo servidores em geral, equipamentos de interconexão de rede, serviços propriamente ditos, entre outros.
E, olhem só, todos esses serviços acessíveis pela Internet sem limitação geográfica e com custos acessíveis. Aesses serviços, que possuem como premissa o compartilhamento de recursos pela Internet,
dá-se o nome de
Computação em Nuvem (Cloud Computing).

Essa tecnologia possui diversos benefícios, tais como: escalabilidade; capacidade de ajustes dinâmico dos servidores em termos de capacidade de disco e outros recursos; distribuição geográfica transparente ao usuário; o cliente paga somente por aquilo que usa efetivamente, reduzindo bastante o desperdício de investimento; recuperação em caso de desastres; entre outros.
Vamos ver a definição de Cloud Computing proposta pelo NIST (Instituto Nacional de
Padrões e Tecnologias do Departamento de Comércio Norte-Americano):
"Computação em nuvem é um modelo para permitir acesso ubíquo, conveniente e sob demanda via rede a um agrupamento compartilhado e configurável de recursos computacionais (por exemplo,redes, servidores,
equipamentos de armazenamento, aplicações e serviços), que pode ser rapidamente fornecido e liberado com esforços mínimos de gerenciamento ou interação com o provedor de serviços".
Podemos afirmar que a Computação em Nuvem é um modelo no qual a computação (software,processamento e armazenamento) está disponível em algum lugar da rede de forma escalável, sendo possível acessá-la remotamente independentemente de tecnologia ou plataforma do cliente e com (possível)pagamento sob demanda (Pay-per-use). Abaixo algumas características de um ambiente de nuvem de forma objetiva:
0.0

FIQUE

ATENTO!

CARACTERÍSTICA DESCRIÇÃO

ÁUTOSSERVIÇÒ

SOB DEMANDA
ACESSO AMPLO

VIA REDE
AGRUPAMENTO

DE RECURSOS
ELASTICIDADE

RÁPIDA
SERVIÇOS

MENSURADOS

O cliente deve ser capaz de alocar novos recursos automaticamente sem interação humana.
Além de estar disponível por toda a rede, deve ser acessível através dos diversos dispositivos.
Recursos de hardware e software devem ser agrupados de tal forma que permita ao consumidor obter seus recursos, podendo ou não ser de forma automática. Deve fornecer um nível de abstração a respeito da localidade dos recursos.
Os recursos devem ser alocados e liberados de forma elástica e rápida, podendo ou não ser automática. O cliente deve ter a percepção de que o recurso é ilimitado
Tanto o cliente quanto o provedor de serviços devem ter acesso a utilização dos recursos, com geração de relatórios e medições online. Tal princípio busca total transparência ao cliente
Antes de adentrarmos nas arquiteturas e tipos de serviços, vamos conhecer um pouco sobre os aspectos de perfis de visibilidade, acesso e segurança desses ambientes de Computação em Nuvem.Eles podem ser divididos em 4 categorias: Nuvem Privada, Nuvem Pública, Nuvem Comunitária e NuvemHíbrida. Vamos ver cada uma delas:
NUVEM PRIVADA

Nesse modelo, a infraestrutura que provê os serviços em nuvem é mantida pela própria organização para uso exclusivo desta e de terceiros vinculados a ela. Ela pode ser uma infraestrutura local ou remota(quando remota, existem referências que a categorizam como "Privada Hospedada"). E
importante dizer que ela também pode ser mantida por terceiros, mas com um uso restrito aos grupos apresentados.
O modelo de Nuvem Privada é utilizado para ambiente mais críticos em termos de segurança e gerenciamento, até porque envolve custos mais elevados de infraestrutura. Ela possui alta capacidade de customização.
Professor, pode dar um exemplo? Sim! Imaginem uma universidade implantando um serviço em nuvem para seus departamentos, seus laboratórios e outros setores acadêmicos.
MBF PP ESTE MAIS

ATENÇÃO!

Importante sempre trazermos as definições na medida que elas nos ajudam, inclusive, a sustentar recursos frente às bancas. Vejam a tradução literal da definição do NIST, em seu documento800-145, que trata dos conceitos de nuvem:
: "A infraestrutura de nuvem é provisionada para uso exclusivo por uma única :
: organização compreendendo vários consumidores (por exemplo, unidades de negócios). :

: Pode ser propriedade, gerida e operada pela organização, um terceiro, ou alguma :

: combinação deles, e pode existir dentro ou fora das instalações.
" :

NUVEM PÚBLICA

É o serviço mais comum oferecido para o público geral, contemplando usuários individuais até grandes instituições, bastando ter como requisito o conhecimento do endereço público da nuvem para acesso.
Ainda que seja pública não implica em falta de segurança ou de técnicas de autenticação e autorização. Na verdade, tem-se um grande cuidado com esses aspectos justamente por ser um meio compartilhado.
Dessa forma, um usuário não possui acesso ao ambiente de outro usuário, a não ser que seja autorizado por este. A capacidade de customização, monitoramento e controle é bem menor quando comparado com a nuvem privada. Ela possui infraestrutura física remota instalada no provedor de serviços de propriedade do próprio provedor e não mais da empresa. Um exemplo desse modelo é o serviço de nuvem oferecido pelaAmazon ou Google.

B FPRESTE MAIS

T ATENÇÃO!

*

Vamos ver novamente, a definição do NIST:

.

: "A infraestrutura de nuvem é provisionada para uso aberto pelo público em geral.
Pode :

: ser de propriedade, gerenciada e operada por uma organização empresarial, :

: acadêmica ou governamental, ou alguma combinação deles. Ele existe nas instalações :

: do provedor de nuvem.
"
:

NUVEM CoMUNITÁRIA

O objetivo desse modelo é o compartilhamento de serviços comuns e semelhantes entre empresas e instituições. Desse modo, pode-se reduzir custos de implantação quando comparado com um modelo deNuvem Privada a ser implantado por apenas uma empresa. Geralmente é administrado e gerenciado pela própria comunidade ou por uma empresa designada por aquela.
Este modelo pode ser implantado de forma local ou remota. Um exemplo desse serviço seria uma empresa de tecnologia do Governo Federal fornecendo o serviço em nuvem para todos os outros órgãos do governo.E isso já acontece atualmente — o SERPRO (Serviço Federal de Processamento de Dados)
fornece diversos serviços em nuvem para vários órgãos.
w *

FPRESTE MAIS

T ATENÇÃO!

Seguindo a definição do NIST, temos:

: A infraestrutura em nuvem é provisionada para uso exclusivo por uma comunidade de :

: consumidores de organizações que compartilham preocupações (por exemplo, missão, :

: requisitos de segurança, política e considerações de conformidade). Pode ser de :
: propriedade, gerenciada e operada por uma ou mais organizações da comunidade, :

: uma entidade externa ou terceira, ou alguma combinação deles, e pode existir dentro
:

: ou fora das instalações.
:

NUVEM HÍBRIDA

A computação em nuvem do tipo híbrida é a composição de uma dupla entre nuvens públicas, privadas ou comunitárias. Permite que uma nuvem privada possa ter recursos ampliados a partir de uma reserva de recursos em uma nuvem pública. Determinadas aplicações são direcionadas às nuvens públicas, já outras mais críticas permanecem na nuvem privada. Pode ser implantado de forma local ou remota.
Com a definição do NIST, temos:

: A infraestrutura de nuvem é uma composição de duas ou mais tipos de nuvens distintas =

: (privadas, comunitárias ou públicas) que permanecem como entidades únicas, mas estão :

: vinculadas por tecnologia padronizada ou proprietária que permite que dados e :
: aplicativos sejam portados (por exemplo, grande volume de dados em nuvem para :

: balanceamento de carga entre nuvens).
:

Pessoal, é salutar conhecer o nome comercial mercado atualmente, tais como:
de alguns serviços de nuvem pública que hegemonizam o

* iCloud:

A empresa responsável pelo iCloud é a Apple. Ele permite a integração e compartilhamento de dados entre os diversos dispositivos deste fabricante. Entre eles,podemos citar os iPhones, lpad's e Mac's.

* OneDrive:

A empresa responsável pelo OneDrive é a Microsoft. É a evolução do
SkyDrive. Ele fornece recursos de armazenamento e compartilhamento de arquivos na nuvem e possui integração nativa com os sistemas Windows —possui uma versão business mais completa.

OneDrive

* GoogleDrive:

A empresa responsável pelo GoogleDrive é a Google. Ele fornece recursos semelhantes aos do OneDrive, além da possibilidade de edição e programação online de forma compartilhada e simultânea — é integrado com outros serviços.
* DropBox:

A empresa responsável pelo DropBox é a própria DropBox. Ele fornece recursos semelhantes aos do OneDrive e Google para o armazenamento e sincronização dos arquivos. Permite a integração com o sistema de diretórios do cliente a nível deSistema Operacional. Não sei se vocês se lembram, mas ele foi o primeiro a se popularizar no mercado com grandes capacidades de armazenamento para seus clientes.
Dropbox

Reparem que todos os serviços acima podem ser utilizados de forma gratuita ou

0 0

pago. Neste último caso, são fornecidos alguns recursos adicionais que permitem inclusive a utilização desses serviços por grandes corporações.
HORA DE

PRATICAR!

(CESPE - ANTT - Analista de Sistemas/2013) Os modelos de implementação para computação em nuvem podem ser classificados em público, privado, comunitário e restrito.
Comentários:

Vimos que em termos de visibilidade, podemos categorizar os ambientes de computação em nuvem em quatro espécies: Nuvem Privada, Nuvem Pública, Nuvem Comunitária e NuvemHíbrida. Portanto, a banca trocou o perfil híbrido por restrito.
Gabarito: E

ARQUITETURAS DE CLoUD CoMPUTING

Bom, agora entramos no assunto que é mais cobrado em provas, i.e., as arquiteturas e serviço oferecidos -as mais importantes são laaS, PaaS e SaaS. Vejamos:

INDO MAIS

FUNDO!

INFRASTRUTURE AS A SERVICE (IAAS):

É caracterizada pelo provimento de toda a infraestrutura física e lógica de forma virtualizada na nuvem,com capacidades de hardware definidas (Ex: Processamento, Memória, Armazenamento).
Nesse ambiente,
pode-se ter a interação com hosts, switches, balanceadores, roteadores,
servidores, inclusive com a capacidade de adição de novos servidores de forma simples e transparente.
Ele é a base necessária para a implementação do SaaS e PaaS.

Exemplo: Amazon EC2 ou Google Compute Engine (GCE).

PLATFoRM AS A SERVICE (PAAS):

É caracterizada pela possibilidade de implementação e realização de testes de aplicações na nuvem. Ousuário tem acesso e permissão para alterar configurações e parâmetros das aplicações hospedadas na nuvem. E disponibilizado um ambiente completo de desenvolvimento para o usuário como um sistema operacional, linguagens de programação e bancos de dados. Toda a estrutura para controle de versões e testes é fornecido na plataforma em tese.
Possui recurso de colaboração de desenvolvedores.

Exemplo: PaaS Google App Engine (GAE).

SoFTwARE AS A SERVICE (SAAS):

É caracterizada pelo uso compartilhado de um software na nuvem. Este software pode ser acessado por qualquer dispositivo, independentemente de SO ou software, em qualquer lugar, desde que haja as devidas permissões. Dessa forma, atualizações e manutenções são transparentes ao usuário.
Os softwares nesse tipo de nuvem também podem ser gratuitos ou pagos, bem como o PaaS.

Exemplo: Google Does.

COMMUNICATION AS A SERVICE (CAAS)Í

É caracterizado por prover infraestrutura para comunicação em nuvem com um conjunto de serviços que facilitam a comunicação empresarial. E utilizado para reduzir custos e aumentar a eficiência de processos organizacionais por meio de VolP, Teleconferências e Videoconferências. Toda a responsabilidade de disponibilidade e qualidade de serviço fica por conta do provedor do serviço com Acordos de Nível deServiço - ANS - arrojados.

Os softwares nesse tipo de nuvem já são bastante populares.

Exemplo: Skype e Facetime.

DATABASE AS A SERVICE (DBAAS):

Este tipo de serviço é uma das formas de disponibilizaçõo de base de dados na nuvem.
Dessa forma, o serviço se restringe a fornecer diversos tipos de banco de dados (Simples, Relacional,Orientado a Objetos,
entre outros) aos usuários como um serviço. Ele não tem que se preocupar com a instalação ou manutenção da base de dados.
Esse tipo de arquitetura de nuvem ainda é um pouco incipiente.

Exemplo: SimpleBD e Amozon Relational Dotobose Service.

FUNCTIoN AS A SERVICE (FAAS)

FaaS significa "Functions as a Service" (Funções como Serviço, em português) e é uma categoria de serviço de computação em nuvem que permite aos desenvolvedores carregar funções individuais de software em um ambiente de nuvem gerenciado, executar e escalar automaticamente essas funções conforme necessário, sem precisar gerenciar a infraestrutura subjacente.
Em um modelo FaaS, o provedor de nuvem é responsável por gerenciar a infraestrutura de computação e rede necessária para executar as funções, permitindo que os desenvolvedores se concentrem apenas na lógica do negócio e no código das funções individuais. O modelo FaaS é altamente escalável e pode ser usado para implementar facilmente funções de back-end para aplicativos móveis, web ou loT, bem como para implementar funções de processamento de eventos e outras tarefas de processamento em lote.
Os provedores de nuvem populares que oferecem serviços FaaS incluem a Amazon Web
Services (AWS) com o AWS Lambda, o Google Cloud Platform com o Google Cloud Functions e o MicrosoftAzure com o Azure
Functions.

EVERYTHINC AS A SERVICE (XAAS)

XaaS é um modelo de negócios que se refere a "tudo como serviço" (Everything as a
Service). É uma evolução do modelo de software como serviço (SaaS).O XaaS se refere a um conjunto de serviços que são oferecidos na nuvem e disponibilizados aos usuários como uma solução completa,abrangendo desde infraestrutura como serviço (laaS), plataforma como serviço (PaaS) e software como serviço (SaaS), até serviços mais específicos, como banco de dados como serviço (DBaaS), segurança como serviço (SECaaS) e monitoramento como serviço (MaaS).
O XaaS é caracterizado pela flexibilidade, escalabilidade e facilidade de uso,
permitindo que as empresas se concentrem em suas atividades principais, enquanto os provedores de serviços gerenciam as infraestruturas de TI necessárias para suportar seus negócios.
A adoção do modelo XaaS tem crescido rapidamente nos últimos anos, impulsionada pela necessidade das empresas de reduzir custos de infraestrutura, simplificar processos e melhorar a eficiência operacional. Ao adotar o XaaS, as empresas podem reduzir o tempo e o custo de implementação, aumentar a flexibilidade,melhorar a segurança e a disponibilidade dos serviços e reduzir o tempo de inatividade. Além disso, o modelo XaaS permite que as empresas sejam mais ágeis, respondendo rapidamente às mudanças de mercado e às necessidades dos clientes.
; (FCC - CNMP/Analista de Suporte/2015) Na Computação em Nuvem (Cloud Computing), diversos

\ tipos de serviços podem ser disponibilizados aos usuários. O serviço

0-0

que fornece uma infraestrutura de integração para implementar e testar aplicações elaboradas para a nuvem, é denominado a) AaaS -Application as a Service.
b) DaaS -Development as a Service.

c) laaS -Implementation as a Service.

d) PaaS "Platform as a Service.

e) SaaS -Software as a Service.

Comentário;

Pessoal, falou em geração de ambiente de desenvolvimento, implementação e testes, fala-se então do
PaaS.

Gabarito: D

A figura abaixo nos dá uma visão em termos de responsabilidades (se é do cliente ou do provedor de serviços) das três principais arquiteturas:
Separation of Responsibilities

On-Premi$es

JL

Infrastructure

|**lSerw«|

Cloud Computing

Platform Software
(ai«

Applicdtions

WORKLOADS

Ainda no bojo da computação em nuvem, é importante entendermos os conceitos de
Workload ou processos de trabalho, ou ainda cargas de trabalho. Basicamente, trata-se do recurso que deverá ser trabalhado ou suportado pela nuvem. Na prática, será uma base de dados que precisará funcionar em backup, uma aplicação que precisará ser disponibilizada, um contêiner que precisa ser migrado, entre outros.
Em suma, representa a necessidade do negócio a ser provido pelo serviço em nuvem.
Assim, para cada necessidade, há de se avaliar as características do Workload, para que seja possível o estudo e proposição da arquitetura mais adequada, bem como a indicação da melhor estratégia de migração desse Workload para nuvem. Esses itens podem ser medidos e avaliados em termos da quantidade de acessos totais,simultâneos, projeção de consumo de memória ou processador, volume de dados armazenados,
estrutura e arquitetura da aplicação, entre outros. Por fim, a partir desse Workload, deve-se sempre considerar pontos de melhoria e oportunidade em torno da aplicação ou serviço, já ponderando as vantagens e serviços agregados da computação em nuvem.
Nesse processo, daremos destaque às diferentes estratégias que podem ser adotadas a partir workloads abaixo, e seus comportamentos. Assim, temos, como base, os tipos a seguir:
Vamos comentar um pouco sobre cada um deles e seus desdobramentos.

dos

1. Static Workload

Recursos de TI que possuem comportamento igual ao longo do tempo. Nesse contexto, de fato, há uma espécie de linha reta em termos dos recursos exigidos, com limites bem definidos.
Neste caso, não há ganhos reais a serem experimentados pela nuvem em termos da elasticidade no provimento de recursos, associado ao pagamento por uso, com a melhor alocação possível.A dinâmica de consumo sendo constante, pode justificar, inclusive, a manutenção desse Workload no ambiente local (on-premisse).

A seguir, um exemplo comparativo com recurso fixado em comparação com recurso alocado dinamicamente:
Percebam que na primeira imagem, a simples fixação do recurso seria suficiente para atender a necessidade. Na ótica de alocação elástica, conforme segunda imagem, poderia, em algum momento, haver ganhos pontuais em termos de não correr riscos nas variações próximas ao limite superior estabelecido.
2. Periodic Workload

A partir de agora, já temos condições de experimentar ganhos reais para esses Workloads, com a possibilidade de elasticidade nos recursos em nuvem. Para o Workload periódico,como o nome já nos apresenta, há um comportamento variável, porém, periódico. Com isso, é possível exercer a previsibilidade de tráfego e indicar uma dinâmica que molde o tráfego a partir dos recursos disponibilizados.
Assim, os picos e vales, podem ser claramente percebidos. Talvez este seja o perfil de workload que mais se aproxima das aplicações em um contexto geral. Vejamos um exemplo básico de rotina de trabalho. Em regra, sistemas internos e de gestão são acessados em horário comercial, podendo ainda potencializar esse pico na janela central do período da manhã e também da tarde. Isso se repete todos os dias, de segunda a sexta.
V ESCLARECENDO!

ww. estrategiaconcursos. com.br

Ou seja, percebemos, claramente, uma dinâmica periódica nesse exemplo. Podemos ainda pensar em sistemas com fluxos semanais, como fechamento de folha de ponto, ou ainda,fluxos mensais, como pagamento de funcionários, entre outros. Nesse sentido, pensando em garantir os recursos necessários para os picos, e reduzir os custos de infraestrutura nos períodos de baixa, nada mais adequado do que moldar o tráfego respeitando essa dinâmica.
Vejamos na imagem a seguir, justamente a proposta:

3. Once-in-a-lifetime Workload

Seguindo com os tipos de workloads, agora vamos falar sobre o
Once-in-a-lifetime Worload. Basicamente,
para esse contexto, tem-se um tráfego que acontece de forma esporádica ou ainda única. O melhor exemplo para esse tipo de tráfego é a famosa blackfriday.
Na ocasião, tem-se um dia específico do ano, que pode se estender ainda por alguns dias até a eventual cybermonday, onde há um grande tráfego concentrado, gerando picos e volumes de demandas, tanto simultâneas quanto acumuladas, capazes de gerar impactos nos serviços,tornando-os lentos ou até indisponíveis.
INDO MAIS

FUNDO!

Nesse contexto, é necessário reagir de forma pontual durante esse período. Assim,
olhando para a primeira imagem, é possível observar que haveria um desperdício de recursos muito alto para tentar alocar de forma antecipada e fixa. Entretanto, importante destacar que não se trata de um tráfego desconhecido ou ainda inesperado. Há uma certa previsibilidade de data e hora para sua ocorrência.O que se tem de certa imprevisibilidade é o pico que será alcançado com o volume.
Justamente nesse sentido, tem-se a demonstração da segunda imagem. Perceba que faz-se uma primeira alocação para se esperar um volume inicial (representado pelo primeiro degrau), e, à medida que o tráfego vai aumentando, vê-se a necessidade de aumentar um pouco mais o provimento inicial,gerando sempre uma faixa adicional para suportar o novo pico. Somente após perceber que o fluxo e volume de usuários passa a diminuir é que começa o processo de desprovisionamento, até retornar para a linhar de base original.
0 0

4. Unpredictable Workload

Avançando para o quarto tipo de workload, temos agora o não previsível, em tradução literal. Como o próprio nome diz, a alocação fixa de recursos para tráfegos imprevisíveis,inevitavelmente vai incorrer em um dos dois problemas clássicos:
1. Ociosidade de recursos alocados e consequentemente desperdício de recursos;

2. Recursos alocados insuficientes e que geram problemas na solução como lentidão e até indisponibilidade.
Vejam que na prática, não tem para onde correr. Então aqui, tem-se o modelo clássico de utilização do serviço em nuvem com recursos de auto scalling. A eficiência do processo está na capacidade do recurso de automação em provisionar os recursos à medida que o tráfego muda,gerando um processo de moldagem real do tráfego.
5. Continuously Changing Workload

Por fim, o úlitmo tipo de workload, aquele referenciado sempre com "mudança contínua".
Aqui, a ideia reside também em dois pontos básicos:
TOME

NOTA!

1. Modelo de incremento funcional da solução, de tal modo que a cada nova feature ou recurso, há necessidade de expansão da capacidade de provimento, com acréscimo de novos usuários e aumento do consumo.
2. Dinâmica de otimização da solução hospedada em nuvem, que visa reduzir o consumo a partir de evoluções e mudanças arquiteturais, ou ainda funcionais, agregando ferramentas e soluções para tal finalidade.
O destaque é que a imagem da direita representa o primeiro caso, até porque, no segundo caso, teríamos uma redução do consumo real e, consequentemente, do provisionamento associado.
TIPoS DE MIGRAçÃo

0 processo de migração para o ambiente em nuvem, depende do ponto de partida. A Google traz algumas referências de nomenclatura que servem como base para entendimento do processo e definição das ações a serem realizadas.
Migrar uma carga de trabalho ou workload de um ambiente local legado ou de um ambiente de hospedagem privado para um ambiente nativo da nuvem, como uma nuvem pública, pode ser desafiador e arriscado. Migrações bem-sucedidas alteram a carga de trabalho para migrar o mínimo possível durante as operações de migração.
Mover aplicativos locais legados para a nuvem geralmente requer várias etapas de migração. Há três tipos principais de migração:
1. Migração lift-and-shift

2. Improve-and-move

3. Remover e substituir (às vezes chamado de rip-and-replace)

Nas seções a seguir, cada tipo de migração é definido com exemplos de quando usar cada tipo.

1. Migração lift-and-shift

Em uma migração lift-and-shift, as cargas de trabalho são movidas de um ambiente de origem para um ambiente de destino com pequenas ou nenhuma modificação ou refatoração. As cargas de trabalho a serem migradas são modificadas o mínimo possível, apenas o bastante para que elas operem no ambiente de destino.
Uma migração lift-and-shift é ideal quando uma carga de trabalho pode operar no ambiente de destino no estado em que se encontra ou quando há pouca ou nenhuma necessidade corporativa de mudança. Esse tipo de migração requer menos tempo porque a quantidade de refatoração é mínima.
Pode haver problemas técnicos que forçam uma migração lift-and-shift. E obrigatório usar a migração lift-and-shift caso não seja possível refatorar a carga de trabalho para migrar ou descomissionar a carga de trabalho.
Por exemplo, pode ser difícil ou impossível modificar o código-fonte da carga de trabalho, ou o processo de compilação não é direto, de modo que não seja possível produzir novos artefatos após a refatoração do código-fonte.
As migrações lift-and-shift são as mais fáceis de executar porque as equipes do cliente podem continuar usando o mesmo conjunto de ferramentas e habilidades que estava usando antes. Essas migrações também são compatíveis com softwares prontos. Como as cargas de trabalho atuais são migradas com o mínimo de refatoração, as migrações lift-and-shift tendem a ser as mais rápidas do que migrações improve-and-move ou rip-and-replace.

Por outro lado, os resultados de uma migração lift-and-shift são cargas de trabalho nativas da nuvem executadas no ambiente de destino. Essas cargas de trabalho não aproveitam ao máximo os recursos da plataforma de nuvem, como escalabilidade horizontal, preços detalhados e serviços altamente gerenciados.
2. Migração improve-and-move

Em uma migração improve-and-move, a carga de trabalho é modernizada durante a migração.
Nesse tipo de migração, as cargas de trabalho são modificadas para otimizá-las para os recursos nativos da nuvem,não apenas para que elas funcionem no novo ambiente. E possível aprimorar o desempenho, os recursos,o custo ou a experiência do usuário para cada carga de trabalho.

Se a arquitetura ou a infraestrutura atual de um aplicativo não for compatível com o ambiente de destino,será necessário um certo nível de refatoração para superar essas limitações.

A abordagem improve-and-move também é recomendada quando é necessária uma atualização importante na carga de trabalho, além das atualizações exigidas para migrar.
As migrações improve-and-move permitem que seu aplicativo aproveite os recursos de uma plataforma de nuvem, como escalabilidade e alta disponibilidade. Também é possível arquitetar o aprimoramento para aumentar a portabilidade do aplicativo.
Por outro lado, as migrações improve-and-move levam mais tempo do que as migrações lift-and-shift,porque precisam ser refatoradas para que o aplicativo migre. E necessário avaliar o tempo e o esforço extra como parte do ciclo de vida do aplicativo.
Uma migração improve-and-move também exige que as equipes dominem os conhecimentos dos novos produtos e tecnologias a serem utilizadas.
3. rip-and-replace

Em uma migração rip-and-replace, desativa-se um aplicativo atual e faz um projeto completamente novo para reescrevê-lo na forma de um aplicativo nativo da nuvem.
Se o aplicativo atual não estiver atingindo os objetivos e metas, por exemplo, pode ser interessante descontinuá-lo, uma vez que pode ser muito caro migrar usando uma das abordagens mencionadas anteriormente ou ele pode não ser compatível com o ambiente de nuvem, sendo necessária a uma migração rip-and-replace.
As migrações rip-and-replace permitem que o aplicativo aproveite ao máximo os recursos da nuvem, com estrutura totalmente nativa, como escalabilidade horizontal, serviços altamente gerenciados e alta disponibilidade. Como a aplicação está sendo reescrita do zero, o débito técnico da versão legada atual também é removido.
No entanto, as migrações rip-and-replace podem levar mais tempo do que migrações lift-and-shift e improve-and-move. Além disso, esse tipo de migração não é adequado para aplicativos prontos para serem usados porque requer a reelaboração do aplicativo. E necessário avaliar o tempo e o esforço extras para reformular e reescrever o aplicativo como parte de seu ciclo de vida.
Uma migração rip-and-replace também requer novas habilidades. E necessário usar novas ferramentas para provisionar e configurar o novo ambiente e implantar o aplicativo nesse ambiente.
: Cebraspe - Técnico Judiciário - Tecnologia da Informação (TRT-AP/PA)/2022

I

i Um tribunal regional do trabalho planeja realizar a migração de suas cargas de trabalho í modificando-as de modo a otimizá-las para os recursos nativos da Google Cloud a medida que i estão sendo migradas. Como requisito, a carga de trabalho é modernizada durante a migração de í modo a aprimorar o desempenho da carga.
í Com base na situação apresentada, assinale a opção que indica o modelo de implantação
= presente no texto.

\ a) improve-and-move.
i b) lift-and-shift.

; c) repurchase-replatform.

; d) rip-and-replace.

\ e) rehost-replatform.

; Comentário;

i Vamos lá... Antes de validarmos os conceitos e tipos, vejam que a questão traz alguns termos chaves e o mero conhecimento de inglês ajudaria, pois vejam que o enunciado destaca o modo de modernização durante a migração de modo a aprimorar o desempenho. Ou seja, temos aí um improve-and-move.
Agora, vinculando ao conteúdo, vejam que há uma descrição de um processo de melhoria e modernização, ou seja, há um processo de refatoraçõo.
Gabarito: A

SERVERLESS

Um outro conceito de que surge nas bancas, e também está muito associado à modernização e ampliação dos recursos em nuvem é o serverless, ou, em tradução literal, sem servidor.
A ideia básica pessoal não é muito diferente do que já vimos a partir das camadas de abstração de infraestrutura e plataformas associadas. Entretanto, o foco para esse contexto é nas esteiras de desenvolvimento e produção rápida. Busca-se, portanto, uma simplificação no processo de desenvolvimento,testes e deploy de aplicações.

Desse modo, gera-se uma independência e abstração no processo de provisionamento e gerenciamento de servidores, com uma arquitetura modernas, totalmente orientada a serviços e com custos e faturamento por eventos e tempo de processamento realizado.
TOME

NOTA!

Trata-se de um conceito atualmente utilizado e muito explorado por startups e pequenas empresas, que geralmente não possuem equipes de tecnologia suficientes para realizarem o gerenciamento de serviços de infraestrutura em nuvem.
A seguir, temos a lista dos principais serviços disponibilizados pelas grandes empresas provedoras de serviços em nuvem. Recomendo que realizem duas leituras na documentação oficial do fabricante nesse aspecto. A primeira, uma leitura transversal e dinâmica em inglês para absorver os termos e as chamadas técnicas que podem ser referenciadas pelas bancas nos seus termos originais. E a segunda, caso tenha dificuldade na tradução, em português para entender as características básicas dos serviços.
1. AWS

https://aws.amazon.com/pt/serverless/

2. GOOGLE

https://cloud.google.com/serverless

3. AZURE

https://azure.microsoft.eom/en-us/solutions/serverless/#solutions

Reforço que esta parte do conteúdo está sendo melhor explorada na nossa aula em vídeo, onde navego nos portais tecendo alguns comentários.
SERVIçoS AWS - COOCLE - AZURE

Avançando mais um pouco, temos algumas bancas que já estão apresentando cobranças mais direcionadas aos principais serviços dos provedores em nuvem. Nesse aspecto, seguindo a mesma dinâmica dos produtos serverless, deixo os links abaixo que direcionarão vocês para as páginas principais de cada provedor, com acesso amplo ao catálogo de serviços.
INDO MAIS

FUNDO!

Da mesma forma, também realizei alguns comentários e apresentei a forma de navegação para explorar esse conjunto de informações. Vamos tratar dos principais itens em exercícios à medida que forem aparecendo com mais constância nas bancas.
» 1. AWS - https://bityli.com/hacOz

» 2. GOOGLE - https://cloud.google.com/products

» 3. AZURE - https://azure.microsoft.com/pt-br/

Um ponto que chamo atenção é a importância de se saber os principais serviços e suas categorias. Isso já adiantará bastante o seu aprendizado. Vejam que todas as páginas possuem serviços em destaque, e as diversas categorias. Recomendo que naveguem, em cada categoria, para extrair os serviços em destaque apresentados.
QUESTõES CoMENTADAS

CLUSTER E GRID

1. (CESPE - ANTT/Analista Administrativo/2013) A computação em grade difere da computação em cluster, principalmente pelo fato de as unidades de processamento de um cluster serem conectadas em uma topologia em anel.
Comentários;

Pessoal, o Grid possui uma estrutura totalmente distribuída e descentralizada. Já o
Cluster, geralmente é implementado em estrela ou barramento.
Gabarito: E

2. (CESPE - CGE-PI/Auditor Governamental/2015) Na constituição de um cluster,
é possível a utilização de sistemas operacionais diferentes, entretanto, desktops domésticos ou de escritório não são permitidos como nós do cluster.
Comentários:

Pessoal, geralmente os clusters são implementados como sistemas homogêneos, conforme vimos, incluindo sistemas operacionais iguais.
Gabarito: E

3. (CESPE - SERPRO/Analista- Suporte Técnico/2008) Nos GRIDs, a alocação dos recursos é feita por um gerente de recursos centralizado, e os nós que compõem o GRIDtrabalham cooperativamente como um recurso unificado. Nos clusters, cada nó tem seu gerente de recursos.Os nós em clusters são autônomos e não o são nos GRIDs.

Comentários:

Falou em GRID, temos uma gerência descentralizada. Além disso, o recurso não é unificado. É distribuído tarefas específicas. Temos uma inversão dos conceitos entre CLUSTER e GRID na questão.
Gabarito: E

4. (CESPE - BACEN/Analista - Suporte à Infraestrutura de TI/2013) Se houver o serviço de cluster,os volumes de disco não poderão ser compartilhados.

Comentários;

As implementações de cluster podem ser diversas. Uma boa implementação,
inclusive em ambientes virtualizados, é agregar os recursos de memória e processamento utilizando volumes de discos com implementações em RAID de forma compartilhada.
Gabarito: E

5. (CESPE — SERPRO/Analista — Suporte Técnico/2013) A utilização de clusters de servidores proporciona serviços com alta disponibilidade e balanceamento de carga, porém, implica em perda significativa de desempenho do sistema.
Comentários:

Não né pessoal? Temos ganho de desempenho do sistema também.

Gabarito: E

6. (CESPE - TRE-ES/Analista de Sistemas/2011) A instalação de um cluster possibilita simular a existência de diversos computadores utilizando-se de um único hardware, o que torna factível a execução de sistemas operacionais diferentes.
Comentários:

Inverteram os conceitos mais uma vez. A utilização de um cluster permite enxergar diversos hardwares como um único dispositivo lógico, sendo infactível a utilização de SO's distintos.
Gabarito: E

CoMPUTAçÃo EM NUVEM

7. (CESPE — CNJ/Analista de Sistemas/2013) A computação em nuvem consiste na disponibilização de serviços por meio da Internet, os quais são pagos conforme a necessidade de uso(pay-per-
use), oferecendo ao cliente a possibilidade de aumentar ou diminuir sua capacidade de armazenamento conforme a quantidade necessária para o uso.
Comentários;

Conforme vimos em aula, a questão está perfeita! Muita gente não concordou,
porque a questão dá a entender que toda nuvem é paga. Não, não é! No entanto, ela foi criada essencialmente para ser, isto é,sendo escalável, flexível e pay-per-use.

Gabarito: C

8. (CESPE - CNJ/Analista de Sistemas/2013) Para que a aplicação seja considerada realmente na nuvem, ela deve atender a características essenciais, tais como autosserviço sob demanda;acesso por banda larga; agrupamento de recursos; elasticidade rápida; e serviço mensurado.

Comentários:

Diretamente da nossa tabela:

CARACTERÍSTICA DESCRIÇÃO

AUTOSSERVIÇO

SOB DEMANDA
ACESSO AMPLO

VIA REDE

O cliente deve ser capaz de alocar novos recursos automaticamente sem interação humana.
Além de estar disponível por toda a rede, deve ser acessível através dos diversos dispositivos.
AGRUPAMENTO Recursos de hardware e software devem ser agrupados de tal forma que permita ao consumidor obter seus recursos de forma automática. Deve fornecer
DE RECURSOS um nível de abstração a respeito da localidade dos recursos

ELASTICIDADE

RÁPIDA

Os recursos devem ser alocados e liberados de forma elástica e rápida, além de ser automática. O cliente deve ter a percepção de que o recurso é ilimitado
SERVIÇOS Tanto o cliente quanto o provedor de serviços devem ter acesso a utilização dos recursos, com geração de relatórios e medições online. Tal princípio busca total
MENSURADOS transparência ao cliente

0-0

Gabarito: C

9. (CESPE - PCF /Analista de Sistemas/2013) O GAE (Google App Engine) pertence à categoria de computação em nuvem conhecida como laaS (Infrastructure as a Service) e caracteriza-se por prover máquinas virtuais, infraestrutura de armazenamento, firewalls, balanceamento de carga,entre outros recursos, de forma a hospedar aplicações web nos datacenters da Google.

Comentários;

Pessoal, não acho bacana cobrar especificidades de um produto comercial, mas a resposta está no link:https://cloud.google.com/appengine/docs.

Como podemos ver, GAE é PaaS e fornece uma série de ferramentas e linguagens como
Python, Java, PHP,
MySQL para desenvolvimento de aplicações na nuvem.

Gabarito: E

10. (CESPE - BACEN - Analista de Sistemas/2013) O usuário pode acessar, seus dados armazenados na nuvem, independentemente do sistema operacional e do hardware que esteja usando em seu computador pessoal.
Comentários:

Conforme vimos em aula, é exatamente isso! A integração com os mais diversos dispositivos e a independência de sistemas operacionais ou hardware do lado do cliente é uma característica da computação em nuvem. Algumas pessoas encrencam com o "independentemente" — não vamos criar problemas com a banca. Vamos entender o foco da questão e responder objetivamente.
Gabarito: C

11. (CESPE — BACEN — Analista de Sistemas/2013) Multitenancy é uma importante característica da computação em nuvem que garante que cada usuário acesse recursos da nuvem de forma exclusiva.
Comentários:

Aqui temos um termo utilizado pela Microsoft. Discordo de uma banca cobrar isso em prova, mas vamos lá! Adefinição é: "importante característica da computação em nuvem que garante que cada usuário acesse recursos de forma compartilhada sob a ótica de uma arquitetura SaaS".
Logo, o item está incorreto por dizer que é exclusiva!

Ainda que não soubéssemos o que é isso, convenhamos que é estranho dizer que o acesso a recursos de uma nuvem é feito de forma exclusiva, porque a essência é o compartilhamento.
Gabarito: E

12. (CESPE - STF - Analista de Sistemas/2013) Os serviços Google Does e Google
Drive sâo exemplos de aplicações em nuvem.
Comentários;

Conforme vimos em aula, está perfeito! Lembrando que o GoogleDocs é uma plataforma de edição de documentos na nuvem de forma compartilhada e simultânea com outros usuários.
Gabarito: C

13. (CESPE - STF - Analista de Sistemas/2013) Na infraestrutura como serviço (laaS),
os provedores podem oferecer infraestrutura física ou virtualizada aos clientes, a depender da situação.
Comentários:

Conforme vimos, esse modelo de fato pode ser implementado de forma virtualizada
(lógica) ou física, com servidores e ambiente dedicado. Tudo vai depender da demanda do cliente. Lembremos que o pré-requisito de computação em nuvem não entra no mérito da forma do hardware, sendo ele físico ou virtualizado, mas sim do acesso universal, alta disponibilidade, escalabilidade e outros fatores.
Gabarito: C

14. (CESPE — STF — Analista de Sistemas/2013) No modelo de plataforma como serviços (PaaS), os provedores de serviço oferecem banco de dados e servidores de aplicação. No caso de ferramentas de desenvolvimento, o único modelo funcional é o de software como serviço (SaaS).
Comentários:

Conforme vimos em aula, o PaaS é que fornece uma plataforma para desenvolvimento e testes com as principais suítes de soluções para tal.
Gabarito: E

15. (CESPE- SUFRAMA - Analista de Sistemas/2014) O modelo de implantação de computação em nuvem do tipo híbrido é executado por terceiros. Nesse modelo, as aplicações dos usuários ficam misturadas nos sistemas de armazenamento e a existência de outras aplicações executadas na mesma nuvem permanece transparente para usuários e prestadores de serviços.
Comentários;

A questão trata de nuvem pública e, não, híbrida. A nuvem híbrida combina dois de três tipos: privada,pública e comunitária. Portanto, afirmar que o tipo híbrido necessariamente será executado por terceiros é uma inverdade, pois pode ser uma combinação de nuvem privada e comunitária sem envolver qualquer terceiro, sendo totalmente interna.
Gabarito: E

16. (CESPE - ANTT - Analista de Sistemas/2013) laaS, PaaS e SaaS são modelos de serviço em nuvem.
Comentários:

Conforme vimos em aula, a questão trata apenas das siglas das três principais arquiteturas.

Gabarito: C

17. (CESPE — ANTT - Analista de Sistemas/2013) Os modelos de implementação para computação em nuvem podem ser classificados em público, privado, comunitário e restrito.
Comentários:

Vimos que em termos de visibilidade, podemos categorizar os ambientes de computação em nuvem em quatro espécies: Nuvem Privada, Nuvem Pública, Nuvem Comunitária e Nuvem Híbrida.Portanto, a banca trocou o perfil híbrido por restrito.
Gabarito: E

0 0

18. (CESPE - ANATEL - Analista de Sistemas/2013) A DaaS (Database as a Service), uma das formas de disponibilizar computação nas nuvens, oferece uma solução de comunicação unificada,hospedada em uma central de dados do provedor ou fabricante, entre fornecedores e clientes.

Comentários;

Conforme vimos em aula, a assertiva faz menção ao CaaS! Falou em comunicação unificada, é CaaS!

Gabarito: E

19. (CESPE - ANATEL — Analista de Sistemas/2013) Quanto aos três modelos de serviços de cloud, é correto afirmar que o laaS fornece recursos computacionais (hardware ou software) para o PaaS,que, por sua vez, fornece recursos e ferramentas para o desenvolvimento e a execução de serviços a serem disponibilizados como SaaS.
Comentários:

Pessoal, esse é o encadeamento perfeito das arquiteturas! A laaS serve como base para a PaaS, que serve como base para o SaaS.
Gabarito: C

20. (CESPE - STM - Analista Judiciário - Análise de Sistemas/2011) Cloud computing pode ser vista como a evolução e convergência das tecnologias de virtualização e das arquiteturas orientadas a serviços.
Comentários:

De fato, os serviços oferecidos pela computação em nuvem são virtualizados. Ademais,
ele pode obedecer a uma arquitetura orientada a serviços - no caso de serviços web! Logo, esse item está perfeito! Vale lembrar as diversas arquiteturas fornecidas como serviço: laaS, PaaS, SaaS, etc...
Gabarito: C

21. (CESPE - Correios - Analista de Correios — Jornalismo/2011) Um dos recursos proporcionados pela denominada computação em nuvens (cloud computing) é a recuperação de acervos em caso danos aos computadores.
Comentários;

Conforme vimos em aula, esse é um dos benefícios do Cloud Computing. Vale lembrar que toda os recursos de um ambiente de datacenter robustos podem ser oferecidos indiretamente aos clientes de serviços de computação em nuvem.
Gabarito: C

22. (CESPE - TRT - 17a Região (ES) - Técnico Judiciário - Área Administrativa/
2013) O cloud computing permite a utilização de diversas aplicações por meio da Internet,com a mesma facilidade obtida com a instalação dessas aplicações em computadores pessoais.
Comentários:

Pessoal, uma aplicação nas nuvens é tão fácil de usar quanto uma aplicação que você utiliza aí no seu computador.
Gabarito: C

23. (CESPE - Policia Federal/Perito Criminal Federal/2013) O GAE (Google App Engine)
pertence à categoria de computação em nuvem conhecida como laaS (Infrastructure as aService) e caracteriza-se por prover máquinas virtuais, infraestrutura de armazenamento,firewalls,
balanceamento de carga, entre outros recursos, de forma a hospedar aplicações web nos datacenters da Google.
Comentários:

O GAE é um tipo de PaaS e não laaS conforme apresentado. Um exemplo de laaS é o
Amazon EC2 ou o
Google Compute Engine (GCE)

Gabarito: E

24. (CESPE — STJ/Analista Judiciário — Suporte em TI/2015) Em um provedor que fornece um serviço como PaaS (platform-as-a-service), o consumidor consegue configurar a rede e o sistema operacional utilizados.
Comentários:

Essas características estão presentes no laaS e não no PaaS. O PaaS já assume uma configuração de rede e sistema operacional pré definida cabendo ao usuário tratar de aspectos de plataformas para desenvolvimento de aplicações, linguagens de programação e alguns aspectos de bancos de dados.
Gabarito: E

25. (CESPE - STJ/Analista Judiciário - Suporte em TI/2015) As características da computação na nuvem incluem a elasticidade, que consiste na capacidade de adicionar ou remover recursos para lidar com a variação de demanda.
Comentários;

Esse é de fato um dos principais recursos presentes na computação em nuvem e geralmente atua em conjunto com o conceito de autoserviço de tal modo que o próprio usuário pode aumentar ou diminuir a capacidade conforme sua necessidade. Vimos inclusive essas definições conforme define o NIST.
Gabarito: C

26. (CESPE - TRE/RS / Analista Judiciário/2015) Assinale a opção correta acerca de cloud computing.
a) No modelo de serviço SaaS, o cliente gerencia e controla remotamente os recursos da infraestrutura subjacente da nuvem, como rede, servidores, sistemas operacionais e áreas de armazenamento.
b) No modelo de serviço PaaS em cloud computing, o cliente tem controle remoto dos recursos de rede e segurança, dos servidores, dos sistemas operacionais, das áreas de armazenamento, das aplicações disponibilizadas e das configurações de hospedagem das aplicações.
c) No modelo de public cloud, a infraestrutura computacional em nuvem é compartilhada por várias organizações, a critério da empresa hospedeira; cada uma dessas organizações tem visibilidade e controle sobre onde está hospedada a sua infraestrutura computacional.
d) Organizações que têm a sua própria infraestrutura computacional e se utilizam de cloud computing para manter um sítio de becape para fins de continuidade de negócios enquadram-se no modelo denominado hybrid cloud.
e) Uma das características essenciais de cloud computing é propiciar a capacidade de medição dos serviços em níveis de abstração apropriados: o uso dos recursos é monitorado, controlado e reportado, o que confere transparência aos fornecedores e aos clientes do serviço.
Comentários:

Vamos aos itens:

a) Temos aqui a descrição do laaS. INCORRETO

b) Mais uma vez a descrição do laaS. INCORRETO

c) Esse modelo é conhecido como nuvem comunitária. INCORRETO

d) Esse modelo é conhecido como nuvem privada. INCORRETO

e) Faz parte de umas das cinco características definidas pelo NIST para o modelo de computação em nuvem.As demais são: autosserviço sob demanda, acesso amplo via rede, agrupamento de recursos e elasticidade rápida. CORRETO
Gabarito: E

27. (CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015) Em provedor que fornece serviço como laaS (infrastructure-as-a-service), o consumidor consegue configurar o sistema operacional utilizado pela nuvem.
Comentários;

No serviço laaS, o cliente consegue customizar todo o ambiente de rede, desde os ativos de rede até as aplicações, contemplando, portanto, os sistemas operacionais a serem utilizados.
Gabarito: C

28. (CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015) A possibilidade de monitorar e controlar os recursos utilizados na computação na nuvem proporciona maior transparência tanto para o provedor quanto para o consumidor do serviço.
Comentários:

Vimos que esta é uma das características que determinam um serviço de computação em nuvem segundo oNIST.

Gabarito: C

29. (CESPE - FUNPRESP/ Área 8/2016) Hadoop e Elasticsearch são exemplos de tecnologias que permitem a computação em nuvem.
Comentários:

Temos uma questão extremamente nova, com um alto grau de dificuldade que com certeza pegou a maioria dos candidatos. Para quem nunca leu a respeito, não havia alternativa a não ser deixar em branco. As duas ferramentas possuem a finalidade de tratar o aspecto do processamento e armazenamento dos dados de forma distribuída com recursos de buscas e tratamento. Atualmente, a maioria dos sites especializados defende a utilização do HADOOP em detrimento do Elasticsearch.
Gabarito: C

30. (CESPE - FUNPRESP/ Área 8/2016) A computação em nuvem permite o processamento de dados de maneira distribuída em máquinas com diferentes arquiteturas físicas.
Comentários;

Esse é um conceito advindo da computação em GRID que foi extrapolado para o modelo de computação em nuvem. Assim, podem-se ter diversos DATACENTERs com diversos equipamentos com arquiteturas distintas,processando diversos blocos de informações.

Gabarito: C

QUESTõES CoMENTADAS CoMPLEMENTARES

CoMPUTAçÃo EM NUVEM

1. (FCC - TJ TRE SP/Apoio Especializado/Operaçâo de Computadores/2012) A
tecnologia ou conjuntos de tecnologias que permitem utilizar programas, serviços e armazenamento em servidores conectados à internet, sem a necessidade de instalação de programas no computador do usuário, é chamado de a) model view controller (MVC).
b) serviços web (web services).

c) aplicações web (web applications).

d) arquitetura orientada a serviços (SOA).

e) computação em nuvem (cloud computing).

Comentário;

Questão bem básica em relação ao Cloud Computing, certo pessoal? Quando observamos sob a perspectiva do usuário, nenhum procedimento de instalação de programas ou servidores precisa ser feito, sendo toda configuração e padronização efetuada diretamente na Internet através da Nuvem.
Gabarito: E

2. (FCC - AFF (TCE-SP)/lnformática/Suporte Técnico/2009) Quanto à computação em nuvem,considere:

I. Ao acessar seus dados na nuvem computacional, o usuário não precisa se preocupar com o hardware nem com o sistema operacional de seu computador, uma vez que dele utilizará somente o navegador.
II. O trabalho corporativo e o compartilhamento de arquivos se tornam mais fáceis, uma vez que todas as informações se encontram no mesmo espaço físico, o que assegura ao próprio usuário manter seus dados sob sigilo.
III. O usuário tem um melhor controle de gastos ao usar aplicativos, pois a maioria dos sistemas de computação em nuvem fornecem aplicações gratuitamente e, quando cobrado, o usuário paga somente pelo tempo de utilização dos recursos.
0 0

IV. A Computação em nuvem é uma tendência integrante da Web 2.0 de se levar todo tipo de dados de usuários a servidores online, tornando desnecessário o uso de dispositivos de armazenamento.
É correto o que consta em a) I, II e III, apenas.
b) I, III e IV, apenas.

c) I e II, apenas.

d) III e IV, apenas.

e) I, II, III e IV.

Comentário;

Pessoal, com exceção do item II, os todos estão corretos com características referentes à computação em nuvem.
No item II, o erro está em afirmar que todas as informações se encontram em um mesmo espaço físico. Acaracterística da computação em nuvem é exatamente o contrário, tendo uma grande distribuição geográfica.
Gabarito: B

3. (FCC - CNMP/Analista de Suporte/2015) Na Computação em Nuvem (Cloud Computing),
diversos tipos de serviços podem ser disponibilizados aos usuários. O serviço que fornece uma infraestrutura de integração para implementar e testar aplicações elaboradas para a nuvem, é denominado a) AaaS --Application as a Service.
b) DaaS "tZlDevelopment as a Service.

c) laaS "dlmplementation as a Service.

d) PaaS -EZlPIatform as a Service.

e) SaaS -DSoftware as a Service.

Comentário:

Pessoal, falou em geração de ambiente de desenvolvimento, implementação e testes, fala-se então do
PaaS.

Gabarito: D

4. (FCC - CNMP/Analista de Suporte/2015) A computação em nuvem distribui os recursos na forma de serviços. Esses serviços, por sua vez, podem ser disponibilizados em qualquer uma das camadas que suportam a arquitetura para desenvolvimento em nuvem.Considere a figura abaixo:

Sistema de Armazenamento

Servidor

A figura apresenta um exemplo da relação entre os cenários de uma arquitetura em nuvem, na qual dois
I são usados para a construção de umII, que, por sua vez, é utilizado para a implementação de duas aplicações
( Hl )*

Preenchem as lacunas I, II e III, correta e respectivamente,

a) SaaS - laaS - PaaS

b) laaS - PaaS - SaaS

c) laaS - SaaS - PaaS

d) PaaS - SaaS - laaS

e) SaaS - PaaS - laaS

Comentário:

Pessoal, em termos de escopo e abrangência, vimos que o laaS é a base de todos, inclusive PaaS e
SaaS. Já o PaaS serve como base para o SaaS. A figura do enunciado representa muito bem essa questão. Einteressante reparar que laaS distintos podem servir como base para um mesmo sistema.

Gabarito: B

O.

5. (FCC - INFRAERO - Analista de redes e comunicação de dados/2011) Em cloud computing, trata-se de uma forma de trabalho onde o produto é oferecido como serviço. Assim, o usuário não precisa adquirir licenças de uso para instalação ou mesmo comprar computadores ou servidores para executá-los. No máximo, paga-se um valor periódico, como se fosse uma assinatura,somente pelos recursos utilizados e/ou pelo tempo de uso. Essa definição refere-se a:

a) Platform as a Service (PaaS).

b) Development as a Service (DaaS).

c) Infrastructure as a Service (laaS).

d) Communication as a Service (CaaS).

e) Software as a Service (SaaS).

Comentários;

Conforme vimos em aula, essas são características de um Software as a Service (SaaS).
Lembremos que toda a responsabilidade de infraestrutura, plataforma e aplicação é de responsabilidade do provedor de serviços, restando ao cliente ou usuário simplesmente usar o serviço oferecido.
Gabarito: E

6. (FCC — TRT-MG/Analista Judiciário/2015) A computação na nuvem apresenta a grande vantagem de acessar os recursos computacionais (processamento, banco de dados, etc) a partir da internet sem a necessidade de instalar programas e aplicações nos computadores e dispositivos. Dentre os diferentes tipos de serviços da computação na nuvem, quando recursos de hardware são acessados na nuvem, está se utilizando o tipo de serviço a) DevaaS.
b) laaS.

c) CaaS.

d) SaaS.

e) PaaS.

Comentários:

Temos aí a principal característica da computação em nuvem do tipo laaS:
manipulação a nível de hardware, rede, entre outros elementos característicos de uma infraestrutura de rede e datacenters.
Alguns conceitos mais modernos trazem o PaaS restrito a uma plataforma específica,
enquanto o DevaaS
(Development as a Service), possui uma gama maior de ferramentas em nuvem para este fim.

Gabarito: B

7. (FCC - AJ TRT15/Apoio Especializado/Tecnologia da lnformação/2013) Luiza trabalha noTribunal Regional do Trabalho da 15a Região e suas responsabilidades incluem assegurar que todos os funcionários do Tribunal tenham o software e o hardware de que precisam para fazer seu trabalho. Fornecer computadores para todos não é suficiente, Luiza também tem que buscar adquirir software ou licenças de software para suprir os funcionários com as ferramentas que eles necessitam. Sempre que um novo funcionário é admitido, Luiza tem que adquirir mais software ou assegurar que a atual licença de software permita mais outro usuário. Isso tem estressado muito Luiza, que resolveu buscar novas alternativas. Ela leu a seguinte notícia em uma publicação de TI: "Ao invés de instalar uma suíte de aplicativos em cada computador, basta carregar uma aplicação. Essa aplicação permitiria aos funcionários fazerem o login em um serviço baseado na web que hospeda todos os programas de que o usuário precisa para seu trabalho. Máquinas remotas de outra empresa executariam tudo: de e-mails e processadores de textos até complexos programas de análise de dados.".
A solução a que a publicação se refere e a empresa responsável por armazenar e executar todos os aplicativos são, respectivamente:
a) sistema gerenciador de banco de dados e hospedeira.

b) arquitetura cliente-servidor e servidora de aplicações.

c) computação em nuvem e data center.

d) outsourcing e downsizing.

e) downsizing e outsourcing.

Comentário:

Bem tranquilo o primeiro ponto, certo pessoal? Todos esses aspectos de descentralização de serviços e provimento via Internet é característica da computação em nuvem.Entretanto, considerar o termo
DATACENTER como uma empresa é demais! Nada mais é do que um grande centro de dados que é capaz de armazenar e hospedar diversos serviços e servidores.
Gabarito: C

0 0 SERPRO (Analista - Especialização: Tecnologia) Segurança da Informação - 2023
(Pós-Edital) 43

8. (FCC - TJ TRT15/Apoio Especializado/Tecnologia da lnformação/2015) Os serviços de edição de texto online, como o do Google Does, são serviços disponibilizados na internet por meio do conceito de Computação na Nuvem. Dentre os diferentes tipos de Computação na Nuvem,esses serviços são do tipo a) PaaS ~ Plataform as a Service.
b) laaS - Infrastructure as a Service.

c) CaaS Communication as a Service.

d) DBaas - Data Base as a Service.

e) SaaS - Software as a Service.

Comentário;

Temos aí o exemplo clássico de aplicação do tipo SaaS.

Gabarito: E

1. (CESPE - ANTT/Analista Administrativo/2013) A computação em grade difere da computação em cluster, principalmente pelo fato de as unidades de processamento de um cluster serem conectadas em uma topologia em anel.
2. (CESPE - CGE-PI/Auditor Governamental/2015) Na constituição de um cluster,
é possível a utilização de sistemas operacionais diferentes, entretanto, desktops domésticos ou de escritório não são permitidos como nós do cluster.
3. (CESPE - SERPRO/Analista- Suporte Técnico/2008) Nos GRIDs, a alocação dos recursos é feita por um gerente de recursos centralizado, e os nós que compõem o GRIDtrabalham cooperativamente como um recurso unificado. Nos clusters, cada nó tem seu gerente de recursos.Os nós em clusters são autônomos e não o são nos GRIDs.

4. (CESPE - BACEN/Analista - Suporte à Infraestrutura de TI/2013) Se houver o serviço de cluster,os volumes de disco não poderão ser compartilhados.

5. (CESPE - SERPRO/Analista - Suporte Técnico/2013) A utilização de clusters de servidores proporciona serviços com alta disponibilidade e balanceamento de carga, porém, implica em perda significativa de desempenho do sistema.
6. (CESPE - TRE-ES/Analista de Sistemas/2011) A instalação de um cluster possibilita simular a existência de diversos computadores utilizando-se de um único hardware, o que torna factível a execução de sistemas operacionais diferentes.
CoMPUTAçÃo EM NUVEM

7. (CESPE — CNJ/Analista de Sistemas/2013) A computação em nuvem consiste na disponibilização de serviços por meio da Internet, os quais são pagos conforme a necessidade de uso(pay-per-
use), oferecendo ao cliente a possibilidade de aumentar ou diminuir sua capacidade de armazenamento conforme a quantidade necessária para o uso.
8. (CESPE - CNJ/Analista de Sistemas/2013) Para que a aplicação seja considerada realmente na nuvem, ela deve atender a características essenciais, tais como autosserviço sob demanda;acesso por banda larga; agrupamento de recursos; elasticidade rápida; e serviço mensurado.

9. (CESPE - PCF /Analista de Sistemas/2013) O GAE (Google App Engine) pertence à categoria de computação em nuvem conhecida como laaS (Infrastructure as a Service) e caracteriza-se por prover máquinas virtuais, infraestrutura de armazenamento, firewalls, balanceamento de carga,entre outros recursos, de forma a hospedar aplicações web nos datacenters da Google.

10. (CESPE - BACEN - Analista de Sistemas/2013) O usuário pode acessar, seus dados armazenados na nuvem, independentemente do sistema operacional e do hardware que esteja usando em seu computador pessoal.
11. (CESPE — BACEN — Analista de Sistemas/2013) Multitenancy é uma importante característica da computação em nuvem que garante que cada usuário acesse recursos da nuvem de forma exclusiva.
12. (CESPE - STF - Analista de Sistemas/2013) Os serviços Google Does e
Google Drive são exemplos de aplicações em nuvem.
13. (CESPE — STF - Analista de Sistemas/2013) Na infraestrutura como serviço (laaS),
os provedores podem oferecer infraestrutura física ou virtualizada aos clientes, a depender da situação.
14. (CESPE — STF — Analista de Sistemas/2013) No modelo de plataforma como serviços
(PaaS), os provedores de serviço oferecem banco de dados e servidores de aplicação. No caso de ferramentas de desenvolvimento, o único modelo funcional é o de software como serviço (SaaS).
0 0

15. (CESPE- SUFRAMA - Analista de Sistemas/2014) O modelo de implantação de computação em nuvem do tipo híbrido é executado por terceiros. Nesse modelo, as aplicações dos usuários ficam misturadas nos sistemas de armazenamento e a existência de outras aplicações executadas na mesma nuvem permanece transparente para usuários e prestadores de serviços.
16. (CESPE - ANTT - Analista de Sistemas/2013) laaS, PaaS e SaaS são modelos de serviço em nuvem.
17. (CESPE — ANTT - Analista de Sistemas/2013) Os modelos de implementação para computação em nuvem podem ser classificados em público, privado, comunitário e restrito.
18. (CESPE - ANATEL - Analista de Sistemas/2013) A DaaS (Database as a Service), uma das formas de disponibilizar computação nas nuvens, oferece uma solução de comunicação unificada,hospedada em uma central de dados do provedor ou fabricante, entre fornecedores e clientes.

19. (CESPE - ANATEL — Analista de Sistemas/2013) Quanto aos três modelos de serviços de cloud, é correto afirmar que o laaS fornece recursos computacionais (hardware ou software) para o PaaS,que, por sua vez, fornece recursos e ferramentas para o desenvolvimento e a execução de serviços a serem disponibilizados como SaaS.
20. (CESPE - STM - Analista Judiciário - Análise de Sistemas/2011) Cloud computing pode ser vista como a evolução e convergência das tecnologias de virtualização e das arquiteturas orientadas a serviços.
21. (CESPE - Correios - Analista de Correios — Jornalismo/2011) Um dos recursos proporcionados pela denominada computação em nuvens (cloud computing) é a recuperação de acervos em caso danos aos computadores.
22. (CESPE - TRT - 17a Região (ES) - Técnico Judiciário - Área Administrativa/
2013) O cloud computing permite a utilização de diversas aplicações por meio da Internet,com a mesma facilidade obtida com a instalação dessas aplicações em computadores pessoais.
0 0

23. (CESPE - Policia Federal/Perito Criminal Federal/2013) O GAE (Google App Engine)
pertence à categoria de computação em nuvem conhecida como laaS (Infrastructure as aService) e caracteriza-se por prover máquinas virtuais, infraestrutura de armazenamento,firewalls,
balanceamento de carga, entre outros recursos, de forma a hospedar aplicações web nos datacenters da Google.
24. (CESPE — STJ/Analista Judiciário — Suporte em TI/2015) Em um provedor que fornece um serviço como PaaS (platform-as-a-service), o consumidor consegue configurar a rede e o sistema operacional utilizados.
25. (CESPE - STJ/Analista Judiciário - Suporte em TI/2015) As características da computação na nuvem incluem a elasticidade, que consiste na capacidade de adicionar ou remover recursos para lidar com a variação de demanda.
26. (CESPE - TRE/RS / Analista Judiciário/2015) Assinale a opção correta acerca de cloud computing.
a) No modelo de serviço SaaS, o cliente gerencia e controla remotamente os recursos da infraestrutura subjacente da nuvem, como rede, servidores, sistemas operacionais e áreas de armazenamento.
b) No modelo de serviço PaaS em cloud computing, o cliente tem controle remoto dos recursos de rede e segurança, dos servidores, dos sistemas operacionais, das áreas de armazenamento, das aplicações disponibilizadas e das configurações de hospedagem das aplicações.
c) No modelo de public cloud, a infraestrutura computacional em nuvem é compartilhada por várias organizações, a critério da empresa hospedeira; cada uma dessas organizações tem visibilidade e controle sobre onde está hospedada a sua infraestrutura computacional.
d) Organizações que têm a sua própria infraestrutura computacional e se utilizam de cloud computing para manter um sítio de becape para fins de continuidade de negócios enquadram-se no modelo denominado hybrid cloud.
e) Uma das características essenciais de cloud computing é propiciar a capacidade de medição dos serviços em níveis de abstração apropriados: o uso dos recursos é monitorado, controlado e reportado, o que confere transparência aos fornecedores e aos clientes do serviço.
27. (CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015) Em provedor que fornece serviço como laaS (infrastructure-as-a-service), o consumidor consegue configurar o sistema operacional utilizado pela nuvem.
28.(CESPE - TJDFT/Analista Judiciário - Suporte em TI/2015) A possibilidade de monitorar e controlar os recursos utilizados na computação na nuvem proporciona maior transparência tanto para o provedor quanto para o consumidor do serviço.
29. (CESPE - FUNPRESP/ Área 8/2016) Hadoop e Elasticsearch são exemplos de tecnologias que permitem a computação em nuvem.
30. (CESPE - FUNPRESP/ Área 8/2016) A computação em nuvem permite o processamento de dados de maneira distribuída em máquinas com diferentes arquiteturas físicas.
LISTA DE QUESTõES CoMPLEMENTARES

CoMPUTAçÃo EM NUVEM

1. (FCC - TJ TRE SP/Apoio Especializado/Operação de Computadores/2012) A
tecnologia ou conjuntos de tecnologias que permitem utilizar programas, serviços e armazenamento em servidores conectados à internet, sem a necessidade de instalação de programas no computador do usuário, é chamado de a) model view controller (MVC).
b) serviços web (web services).

c) aplicações web (web applications).

d) arquitetura orientada a serviços (SOA).

e) computação em nuvem (cloud computing).

2. (FCC - AFF (TCE-SP)/lnformática/Suporte Técnico/2009) Quanto à computação em nuvem,considere:

I. Ao acessar seus dados na nuvem computacional, o usuário não precisa se preocupar com o hardware nem com o sistema operacional de seu computador, uma vez que dele utilizará somente o navegador.
II. O trabalho corporativo e o compartilhamento de arquivos se tornam mais fáceis, uma vez que todas as informações se encontram no mesmo espaço físico, o que assegura ao próprio usuário manter seus dados sob sigilo.
III. O usuário tem um melhor controle de gastos ao usar aplicativos, pois a maioria dos sistemas de computação em nuvem fornecem aplicações gratuitamente e, quando cobrado, o usuário paga somente pelo tempo de utilização dos recursos.
IV. A Computação em nuvem é uma tendência integrante da Web 2.0 de se levar todo tipo de dados de usuários a servidores online, tornando desnecessário o uso de dispositivos de armazenamento.
É correto o que consta em a) I, II e III, apenas.
b) I, III e IV, apenas.

c) I e II, apenas.

d) III e IV, apenas.

e) I, II, III e IV.

3. (FCC - CNMP/Analista de Suporte/2015) Na Computação em Nuvem (Cloud
Computing),
diversos tipos de serviços podem ser disponibilizados aos usuários.
O serviço que fornece uma infraestrutura de integração para implementar e testar aplicações elaboradas para a nuvem, é denominado a) AaaS - Application as a Service.
b) DaaS - Development as a Service.

c) laaS " Implementation as a Service.

d) PaaS ~ Platform as a Service.

e) SaaS - Software as a Service.

4. (FCC - CNMP/Analista de Suporte/2015) A computação em nuvem distribui os recursos na forma de serviços. Esses serviços, por sua vez, podem ser disponibilizados em qualquer uma das camadas que suportam a arquitetura para desenvolvimento em nuvem.Considere a figura abaixo:

Sistema de Armazenamento

Servtdor

A figura apresenta um exemplo da relação entre os cenários de uma arquitetura em nuvem, na qual dois
I são usados para a construção de umII, que, por sua vez, é utilizado para a implementação de duas aplicações(III)*

Preenchem as lacunas I, II e III, correta e respectivamente,

a) SaaS - laaS - PaaS

b) laaS - PaaS - SaaS

c) laaS - SaaS - PaaS

d) PaaS - SaaS - laaS

e) SaaS - PaaS - laaS

5. (FCC - INFRAERO - Analista de redes e comunicação de dados/2011) Em cloud computing, trata-se de uma forma de trabalho onde o produto é oferecido como serviço. Assim, o usuário não precisa adquirir licenças de uso para instalação ou mesmo comprar computadores ou servidores para executá-los. No máximo, paga-se um valor periódico, como se fosse uma assinatura,somente pelos recursos utilizados e/ou pelo tempo de uso. Essa definição refere-se a:

a) Platform as a Service (PaaS).

b) Development as a Service (DaaS).

c) Infrastructure as a Service (laaS).

d) Communication as a Service (CaaS).

e) Software as a Service (SaaS).

6. (FCC — TRT-MG/Analista Judiciário/2015) A computação na nuvem apresenta a grande vantagem de acessar os recursos computacionais (processamento, banco de dados, etc) a partir da internet sem a necessidade de instalar programas e aplicações nos computadores e dispositivos. Dentre os diferentes tipos de serviços da computação na nuvem, quando recursos de hardware são acessados na nuvem, está se utilizando o tipo de serviço a) DevaaS.
b) laaS.

c) CaaS.

d) SaaS.

e) PaaS.

7. (FCC - AJ TRT15/Apoio Especializado/Tecnologia da lnformaçâo/2013)
Luiza trabalha no
Tribunal Regional do Trabalho da 15a Região e suas responsabilidades incluem assegurar que todos os funcionários do Tribunal tenham o software e o hardware de que precisam para fazer seu trabalho. Fornecer computadores para todos não é suficiente, Luiza também tem que buscar adquirir software ou licenças de software para suprir os funcionários com as ferramentas que eles necessitam. Sempre que um novo funcionário é admitido, Luiza tem que adquirir mais software ou assegurar que a atual licença de software permita mais outro usuário. Isso tem estressado muito Luiza, que resolveu buscar novas alternativas. Ela leu a seguinte notícia em uma publicação de TI: "Ao invés de instalar uma suíte de aplicativos em cada computador, basta carregar uma aplicação. Essa aplicação permitiria aos funcionários fazerem o login em um serviço baseado na web que hospeda todos os programas de que o usuário precisa para seu trabalho. Máquinas remotas de outra empresa executariam tudo: de e-mails e processadores de textos até complexos programas de análise de dados.".
A solução a que a publicação se refere e a empresa responsável por armazenar e executar todos os aplicativos são, respectivamente:
a) sistema gerenciador de banco de dados e hospedeira.

b) arquitetura cliente-servidor e servidora de aplicações.

c) computação em nuvem e data center.

d) outsourcing e downsizing.

e) downsizing e outsourcing.

8. (FCC - TJ TRT15/Apoio Especializado/Tecnologia da lnformação/2015) Os serviços de edição de texto online, como o do Google Does, são serviços disponibilizados na internet por meio do conceito de Computação na Nuvem. Dentre os diferentes tipos de Computação na Nuvem,esses serviços são do tipo a) PaaS ~ Plataform as a Service.
b) laaS - Infrastructure as a Service.

c) CaaS Communication as a Service.

d) DBaas - Data Base as a Service.

e) SaaS - Software as a Service.

GABARITO

GABARITo

GABARITo - QUESTõES CESPE

r ..

5 E

6 E

7 C

8 C

9 E

10 C

15 E

16 C

17 E

18 E

19 C

20 C

25 C

26 E

27 C

28 C

29 c

30 c

GABARITo - QUESTõES FCC

1 E

2 B

3 D

4 B

5 E

6 B

7 C

RESUMo

Cluster, Grid e Balanceamento de Carga o Cluster - É um agregado de computadores conectados entre si via hardware ou software que compartilham seus recursos passando a funcionar como uma única unidade lógica.
o Grid - A administração e gerência dos dispositivos é descentralizada. As capacidades de processamento são diversificadas e heterogêneas. E utiliza padrões abertos.
o Balanceamento de Carga

* SOFTWARE - Consiste na instalação e configuração de um Software, podendo ser inclusive a nível de sistema operacional, em servidores que fazem parte de um cluster.
* HARDWARE - Atua como intermediário e é responsável por efetuar a distribuição das requisições entre os dispositivos.
Computação em Nuvem (Cloud Computing)

o Co-Location - O serviço de Co-Location (ou Colocation) contempla o fornecimento de infraestrutura de Datacenter para os clientes. Ele contempla ainda critérios de segurança física.
o Hosting - O serviço de hosting está muito mais voltado para o conceito de hospedagem em termos de serviço.
r

Nuvem Nuvem
Privada Comunitária k k1 J
r F

Nuvem Nuvem

Pública Híbrida k J
Arquiteturas de Cloud Computing o laaS - E caracterizada pelo provimento de toda a infraestrutura física e lógica de forma virtualizada na nuvem, com capacidades de hardware definidas.
o PaaS - E caracterizada pela possibilidade de implementação e realização de testes de aplicações na nuvem.
o SaaS - E caracterizada pelo uso compartilhado de um software na nuvem.

o CaaS - E caracterizado por prover infraestrutura para comunicação em nuvem com um conjunto de serviços que facilitam a comunicação empresarial.
o DBaaS - Este tipo de serviço é uma das formas de disponibilizaçõo de base de dados na nuvem.

o Workloads

Static Workload ou Carga de Trabalho estática

Periodic Workload ou Carga de Trabalho periódica

Once-in-a-lifetime Workload ou Carga de Trabalho Único de Vida

Unpredictable Workload ou Carga de Trabalho Imprevisível ww. estrategiaconcursos. com.br o Serverless - Trata-se de um conceito atualmente utilizado e muito explorado por startups e pequenas empresas, que geralmente não possuem equipes de tecnologia suficientes para realizarem o gerenciamento de serviços de infraestrutura em nuvem.
o Serviços AWS - GOOGLE - AZURE

» 1. AWS - https://bityli.com/hacOz

» 2. GOOGLE - https://cloud.gooqle.com/products

» 3. AZURE - https://azure.microsoft.com/pt-br/

CoNSIDERAçõES FINAIS

Chegamos ao término de mais uma aula!

Caso tenha ficado alguma dúvida, me procure no fórum que buscaremos respondê-lo o mais breve possível.E se você está curtindo o nosso curso, não deixe de me seguir no Instagram.

Um grande abraço.
Prof. André Castro.

@ProfAndreCastro t.me/ProfessorAndreCastro

