# Desenvolvimento de Informação - Arquitetura de banco de dados relacional - Oracle

Índice

1) Sistemas Gerenciadores de Banco de Dados-Oracle

2) Criando um Banco de Dados com DBCA

3) Objetos do Schema

4) Estrutura de Memória

5) Estrutura de Processos

6) Processos do Oracle Database

7) Modo de Inicialização e de Encerramento de Servidor

8) Questões Comentadas - Banco de Dados ORACLE - Multibancas

9) Lista de Questões - Banco de Dados ORACLE - Multibancas

SISTEMAS GERENCIADoRES DE BANCo DE DADoS: ORACLE

Esta aula faz um estudo sobre o SGBD Oracle. Nossa ideia é tratar de detalhes da estrutura do SGBD
apresentando sua estrutura lógica e física, objetos do schema, tipos de dados e estrutura de memória. Vamos aproveitar a oportunidade para tratar do processo de instalação e configuração.Por fim, vamos falar sobre detalhes da estrutura do SGBD como estrutura de processos,
modo de inicialização e de encerramento de servidor e backup. Vamos começar?
BANCo DE DADoS ORACLE

O Oracle Database é um banco de dados relacional com várias funcionalidades adicionais que suportam diversos objetos e o formato Extensible Markup Language (XML). Numa base de dados relacional, todos os dados são armazenados em tabelas bidimensionais que são compostas de linhas e colunas. O Oracle permite que você armazene, atualize e recupere dados de forma eficiente, com um alto grau de desempenho, confiabilidade e escalabilidade. Ele é composto basicamente dos seguintes elementos:
O software Oracle que você instala no seu computador (host) ou servidor.

O banco de dados, que é uma coleção de arquivos físicos distribuídos em um ou mais discos.

O banco de dados contém dados do usuário, metadados e estruturas de controle.
Metadados,
ou dados que descrevem os dados, é uma coleção de informações que permite ao software
Oracle gerenciar os dados do usuário. Um exemplo de metadados é o dicionário de dados. As estruturas de controle (por exemplo, control file e online redo log files) garantem a integridade,disponibilidade e capacidade de recuperação de dados do usuário.
A instância Oracle, que é organizada da seguinte forma:

Ela possui processos de background, que são os processos do sistema operacional ou threads que executam as atividades de acesso, armazenamento, monitoramento e recuperação de dados do usuário, metadados e arquivos de controle associados ao banco de dados.
Também fazem parte da instância as áreas de memória compartilhada utilizadas pelos processos em segundo plano.
Processos servidores que realizam o trabalho em nome dos usuários e aplicativos conectados ao servidor, e o armazenamento de memória temporária utilizada por estes processos. Processos do servidor analisam e executam instruções SQL e recuperam ou retornam os resultados para o usuário ou aplicação.
Oracle Net, que é uma camada de software que permite os aplicativos do cliente e o banco de dados Oracle se comunicarem através da rede, e o Oracle Net Listener, que é um processo que atende a solicitações de conexão de rede ao banco.
Para viabilizar o uso do Oracle, precisamos primeiramente fazer a instalação do SGBD
em um servidor. Antes, porém, gostaria de falar um pouco sobre bancos de dados Autônomos.
BANCo DE DADoS AUTôNoMo ORACLE

Um banco de dados autônomo é um banco de dados em nuvem que usa machine learning para automatizar o ajuste de banco de dados, a segurança, os backups, as atualizações e outras tarefas rotineiras de gerenciamento que tradicionalmente eram executadas por DBAs. Ao contrário de um banco de dados convencional, um banco de dados autônomo executa todas essas tarefas e muito mais sem intervenção humana.
Um banco de dados autônomo aproveita a IA e o machine learning para fornecer automação completa de ponta a ponta para provisionamento, segurança, atualizações,disponibilidade,
desempenho, gerenciamento de alterações e prevenção de erros.

Nesse sentido, um banco de dados autônomo tem características específicas.

É independente. Todos os processos de gerenciamento, monitoramento e ajuste de banco de dados e infraestrutura são automatizados. Os DBAs ainda são necessários para tarefas, como gerenciar a conexão de aplicativos e ajudar os desenvolvedores a usar os recursos e funções do banco de dados sem o código do aplicativo.
É intrinsecamente seguro. Os recursos integrados protegem contra ataques externos e usuários internos maliciosos. Isso ajuda a eliminar as preocupações com ataques cibernéticos em bancos de dados sem patch ou sem criptografia.
É autorreparável. Isso pode impedir o tempo de inatividade, incluindo a manutenção não planejada. Um banco de dados autônomo pode exigir menos de 2,5 minutos de tempo de inatividade por mês, incluindo aplicação de patches.
O banco de dados autônomo traz vários benefícios.

* Máximo tempo de atividade, desempenho e segurança, incluindo patches e correções automáticas
* Eliminação de tarefas de gerenciamento manuais e propensas a erros por meio da automação
* Custos reduzidos e produtividade aprimorada ao automatizar tarefas do dia a dia

O Oracle Autonomous Database é executado nativamente na Oracle Cloud
Infrastructure,
fornecendo serviços em nuvem otimizados para cargas de trabalho para processamento de transações e data warehousing.
O Autonomous Data Warehouse é um serviço de banco de dados em nuvem otimizado para processamento analítico. Ele dimensiona automaticamente a computação e o armazenamento,oferece desempenho rápido de consulta e não requer administração de banco de dados.

O Autonomous Transaction Processing é um serviço de banco de dados em nuvem que simplifica as operações do banco de dados para OLTP e aplicativos analíticos em tempo real. Com ele é possível reduzir os custos de tempo de execução em até 90% e obter escala, desempenho e segurança incomparáveis com automações incorporadas ao machine learning.
HORA DE

PRATICAR!

(Ministério da Economia - Infraestrutura - 2020) Com relação ao sistema gerenciador de banco de dados Oracle, julgue o próximo item.
93 O Oracle possui uma versão conhecida como banco de dados autônomo, que é capaz de aplicar atualizações automaticamente sem tornar indisponível o serviço provido.
Comentários: Um banco de dados autônomo aproveita a IA e o aprendizado de máquina para fornecer automação completa de ponta a ponta para provisionamento, segurança, atualizações, disponibilidade, desempenho,gerenciamento de alterações e prevenção de erros. Nesse sentido, um banco de dados autônomo tem características específicas.
É independente. Todos os processos de gerenciamento, monitoramento e ajuste de banco de dados e infraestrutura são automatizados. Os DBAs ainda são necessários para tarefas, como gerenciar a conexão de aplicativos e ajudar os desenvolvedores a usar os recursos e funções do banco de dados sem o código do aplicativo.
É intrinsecamente seguro. Os recursos integrados protegem contra ataques externos e usuários internos maliciosos. Isso ajuda a eliminar as preocupações com ataques cibernéticos em bancos de dados sem patch ou sem criptografia.
É autorreparável. Isso pode impedir o tempo de inatividade, incluindo a manutenção não planejada. Um banco de dados autônomo pode exigir menos de 2,5 minutos de tempo de inatividade por mês, incluindo aplicação de apaches.
Os bancos de dados autônomos são projetados para resistir automaticamente a falhas de hardware,
incluindo aquelas em sites da plataforma de nuvem, e oferecem correção on-line completa de software, firmware, virtualização e clustering.
Gabarito Certo.

INSTALANDo ORACLE DATABASE

Para instalar o software de banco de dados Oracle, use o Oracle Universal Installer
(OUI). OUI
é um utilitário de interface gráfica que permite que você instale o software de banco de dadosOracle. É possível encontrar uma ajuda on-line para guiá-lo através do processo de instalação.

Durante o processo de instalação, é dada a oportunidade de criar um banco de dados.
Se você optar por fazê-lo, o OUI inicia automaticamente o Oracle Database ConfigurationAssistant (DBCA)
para guiá-lo através do processo de criação e configuração de um banco de dados.

Antes de iniciar o processo de instalação, é importante obter informações sobre os pré-requisitos e opções de instalação.

Pré-requisitos

Quando vamos instalar o Oracle, o OUI realiza diversas verificações automatizadas para garantir que o computador cumpre os requisitos básicos de hardware e software para a instalação do Oracle Database. Se o seu computador não atender a um dos requisitos, uma mensagem de erro é exibida. Os requisitos podem variar dependendo do tipo de computador e sistema operacional que você está usando. Os pré-requisitos incluem um mínimo de 1 GB de memória física,espaço de paginação disponível, os service packs ou patches apropriados do seu sistema operacional estarem instalados e o formato do sistema de arquivos utilizado ser apropriado.
Opções de instalação

A Oracle Universal Installer orienta você através de um conjunto de fases ou etapas.Semelhante a uma entrevista ou um questionário, você vai especificar suas escolhas durante a instalação e criação do banco de dados. A sequência exata de passos depende do seu sistema operacional. Quando você progride através da instalação, você é apresentado às opções sobre como configurar o banco de dados. Vejamos algumas delas:
Opções de instalação

Você pode optar por criar e configurar um banco de dados, ou apenas por instalar o software de banco de dados. É possível criar um banco de dados pré-configurado ou um banco de dados com uma configuração personalizada durante a instalação. Se você optar por não criar um banco de dados durante a instalação, você deve executar o DBCA após a instalação.
Bancos de dados pré-configurados são baseados em templates que a Oracle fornece ou que você mesmo pode criar. Cada template Oracle fornecido é otimizado para um tipo específico de carga de trabalho.
Se você optar por usar o método de instalação Desktop Class, um modelo de banco de dados de propósito geral é usado. Para criar um banco de dados personalizado, em que você configura sua própria estrutura de banco de dados, é necessário utilizar opções avançadas de instalação.
Se você precisa criar um banco de dados, o Oracle recomenda que você instale um banco de dados pré-configurado, que é mais rápido e mais fácil. Você pode personalizar o banco de dados após ele ter sido criado.
Métodos de instalação

Os métodos de instalação são divididos em Desktop Class e Server Class:

Desktop Class - Esta classe de instalação é mais apropriada para computadores laptop ou desktop. Ela inclui um banco de dados inicial e requer uma configuração mínima.
Server Class - Esta instalação é para servidores, encontrada em um datacenter, ou usada para suportar aplicações de nível empresarial. A escolha desta classe de instalação deve ser feita se você precisar de acesso às opções avançadas de configuração.
Durante a instalação Desktop Class, você faz apenas escolhas básicas. Para uma instalaçãoServer Class, você pode optar por qualquer uma das instalações típicas (onde você seleciona apenas opções básicas) ou a instalação avançada. Durante a instalação Desktop ou instalação típica, oOracle
Database instala automaticamente os esquemas de banco de dados de exemplo.

Tipos de instalação

Durante a instalação do Oracle, seja na opção básica ou avançada, você precisa responder a algumas questões. O OUI possui uma opção definida como padrão (default) para cada uma delas.Uma dessas perguntas seria: qual o tipo da edição de banco de dados (database edition) você deseja? Você deve escolher entre uma das opções abaixo:
* Enterprise Edition - Esse tipo de instalação vai configurar todas as funcionalidades do produto Oracle Database que prover gerenciamento de dados em nível empresarial. Sua intenção é garantir o desempenho e a segurança para sistemas transacionais (OLTP) e ambientes deData
Warehousing (OLAP).

* Standard Edition - Esse tipo de instalação se encaixa perfeitamente em aplicações de nível departamental ou utilizada por grupos de trabalho. Visa também o atendimento das demandas de pequenas e médias empresas. Provê apenas o core, ou as principais funcionalidades e serviços para gerenciamento de dados. Podem ser inclusos algumas ferramentas de gerenciamento,replicação,
funcionalidades Web e outras facilidades para aplicações comerciais.

* Standard One Edition - Essa instalação é perfeita para grupos de trabalho,
departamentos ou aplicações web. Ela provê o core dos serviços e opções para gerenciamento e banco de dados relacionais em ambientes de servidor único (single-server) ou extremamente distribuídos. Ainstalação inclui todas as facilidades necessárias para construir uma aplicação de negócio crítica.

* Personal Edition - Apenas para o sistema operacional Windows. Essa instalação é composta das mesmas funcionalidades do Enterprise Edition, mas suporta apenas um usuário(single-user).
Seu foco é a utilização para desenvolvimento e publicação (deployments) de aplicações.

Diretórios de instalação

É preciso informar alguns endereços onde serão armazenados os arquivos. Primeiro você deve especificar o diretório que o software Oracle Database será instalado, ou o local onde os arquivos binários do produto serão copiados para a instalação. É preciso selecionar uma localização que tenha espaço em disco suficiente e que seja acessível ao usuário de sistemas que está executando a instalação.
Você também deve definir a localização do diretório base para o Oracle. Ele será utilizado pelos produtos ou ferramentas da Oracle instalados no servidor. A primeira vez que você instalar o Oracle será necessário especificar a localização do diretório de inventário, conhecido como oralnventory.
Localização do arquivo de banco de dados

Um banco de dados possui uma série de arquivos que armazenam dados de usuários,metadados e informações necessárias para uma recuperação após falha. O DBA deve decidir qual tipo de subsistema de armazenamento (storage) usar para esses arquivos. É possível selecionar entre as seguintes opções:
File System - Essa é a opção padrão (default), ela cria arquivos que são gerenciados pelo sistema de arquivos do sistema operacional. É possível especificar o caminho do diretório onde os arquivos serão armazenados.
Automatic Storage Management (ASM) - Essa opção permite gravar os arquivos em um grupo de discos Oracle Automatic Storage Management (ASM). Se essa opção for escolhida, então o SGBDOracle vai gerenciar a localização dos arquivos. Para ambientes com muitos discos, essa opção simplifica a administração e maximiza o desempenho. O software Oracle ASM pode executar o particionamento e a replicação em nível de arquivo visando uma maior flexibilidade,performance e disponibilidade.
Identificadores de banco de dados

Essa opção está relacionada com a inclusão de um identificador global para o nome e a identificação do seu banco de dados (SID). O SID é um identificador único que permite que você diferencie uma instância do Oracle de outra instalada no mesmo sistema.
Durante a instalação é possível definir ainda várias outras opções, principalmente, se você seguir pelas opções avançadas de instalação. Essas opções são mais relevantes quando você está usando o método Server Class. É importante salientar que o processo inclui opções default para todos os itens em cada uma das etapas.
Vamos listar algumas das opções com os valores default entre parênteses para que você possa entender o contexto de cada uma delas.
1) Product Languages você escolhe o idioma usado após a instalação (English).

2) Database Configuration Type define um template usado para a configuração do seu banco de dados, você pode escolher entre General Purpose/Transaction Processing ouData Warehousing (General Purpose).

3) Database Configuration Options, aqui você pode configurar o banco de dados criado durante a instalação. É possível definir o espaço de memória, opções de gerenciamento,o character set usado para o armazenamento, opções de segurança para acesso e outras opções.
É possível, ainda dentro das configurações avançadas, definir: (4) As opções para gerenciamento de banco de dados que pode ser central ou local. O primeiro permite gerenciamento múltiplo, tanto de base de dados quanto de aplicações, usando uma única interface.Usando o gerenciamento local, podemos gerenciar apenas uma única instância de banco de dados por vez. (5)Outras opções configuráveis seriam as opções de recuperação, devemos especificar quando backups devem ser executados. Se você escolher essa opção, é necessário qualificar qual espaço de armazenamento será usado para tal finalidade. (6) Finalizando, devemos definir durante a instalação a senha para os usuários que são criados automaticamente: SYS, SYSTEM, SYSMAN e DBSNMP. Eles permitem que você gerencie seu banco de dados.
Instalando o Oracle

Depois de tratarmos sobre quais são as opções que podemos definir durante o processo de instalação, vamos observar abaixo o passo a passo do processo de instalação do Oracle llg usando o Oracle Universal Installer (OUI). Os passos a seguir consideram que o computador não possui nenhuma versão do Oracle instalada.
1. Efetue o login no computador que deseja instalar o Oracle com o privilégio de administrador com autorização para instalar o software, criar e executar o banco de dados.
2. Supondo que você já possui os arquivos de instalação, execute o Oracle Universal Installer.

3. A primeira tela que aparece é para definir a forma como você quer tratar as atualizações de segurança. Você pode optar por receber as notificações de segurança no seu e-mail.Vamos para a próxima tela.
4. Nesta tela, você deve selecionar a opção de instalação. Escolha a opção "criar e configurar um banco de dados". Selecione Next!
5. Nesta tela, você deve escolher o método de instalação. Sugerimos que você escolha
Desktop
Class e passe para a próxima tela. Veja a seguir uma tela semelhante a que você deve estar visualizando. Caso você opte pela opção Server Class, você deve seguir inserindo os dados para as configurações avançadas.
6. Nesta tela, você deve informar os seguintes detalhes de configuração: (1)
Localização ou diretório da base do Oracle, (2) Diretório de instalação do software, (3) Localização dos arquivos de banco de dados, (4) Tipo de instalação, (5) Character Set, (6) OSDBA Group, apenas para plataformasLinux e Unix, especifica o grupo do sistema operacional para o DBA, geralmente denominado dba,
(7) Um nome global para o banco de dados e, por fim, (8) a senha administrativa,
para as contas de gerenciamento que tratamos anteriormente.
7. Para a primeira instalação em sistemas operacionais Linux e Unix, especifique um diretório para os arquivos de instalação e o nome de algum grupo do sistema operacional com permissão de escrita neste diretório.
8. Se for a primeira vez que procedemos a instalação do Oracle no computador, uma janela para definir o diretório de inventário (Inventory Directory) deve aparecer. Preencha essa janela com o diretório, ele será utilizado pelo OUI para registrar todas as instalações do SGBD no seu computador. Passe para próxima tela.
9. Esta tela vai verificar os pré-requisitos que comentamos anteriormente. Se alguma das verificações falhar, tome as ações corretivas necessárias e siga em frente!
10. Uma tela de sumário vai listar todos os dados. Revise as informações e selecione
Finish para começar a instalação. Uma janela mostrará o progresso da instalação. Após a instalação,aparecerá outra janela de configuração com o assistente de configuração de banco de dados. Depois da criação do banco de dados, aparecerá um resumo das informações.
11. Este passo é opcional. Você pode clicar em Password Management para desbloquear as contas de usuário, fazendo com que elas estejam acessíveis aos usuários. As contas SYS e SYSTEMsão desbloqueadas por padrão.

12. Para Linux e Unix, execute os scripts especificados.

13. Tome nota das informações da janela de finalização e saia do OUI. Parabéns, você concluiu a instalação do Oracle! Sei que a maioria dos alunos não deve ter seguido esse roteiro, mas a ideia aqui é que você tenha conhecimento das informações utilizadas durante uma instalação.Veremos,
a seguir, a criação e gerenciamento de um banco de dados.

CRIANDo UM BANCo DE DADoS CoM DBCA

Com o Oracle Database você pode ter um banco de dados que dá suporte a múltiplas aplicações. Você não precisar de múltiplas instalações do banco de dados para rodar diferentes aplicações, é possível separar os objetos que dão suporte às diferentes aplicações em diferentes schemas no mesmo banco de dados.
A criação de um banco de dados utilizando a ferramenta Database Configuration Assistant
(BDCA) é bastante simples. A ferramenta apresenta um conjunto de passos que devem ser seguidos.São várias telas, cada uma solicita algumas informações a respeito do banco de dados a ser criado.Para executar a ferramenta, basta executar a mesma na aba Configuration and Migration
Tools no
Windows ou executar o comando dbca para Unix, Linux ou na linha de comando do Windows.

São dozes passos. No primeiro passo, você deve definir o que exatamente você quer fazer com o assistente. Você deve escolher entre (1) criar um banco de dados, (2) configurar as opções de um banco de dados, (3) excluir um banco de dados ou (4) gerenciar templates. No momento nossa intenção é criar um banco de dados, então escolheremos a primeira opção.
No segundo passo, escolheremos um dos templates de banco de dados. Estes incluem detalhes para a criação do banco de dados. Eles contribuem para que você consiga criar uma base em alguns minutos. São três os templates que geralmente encontramos:
(1) General Purpose ou Transaction Processing,

(2) Custom Database

(3) Data Warehouse.

Na próxima tela, são especificados o Global Database Name e o SID. É possível que eles tenham o mesmo nome. A quarta tela permite que você configure a opção para o gerenciamento que pode ser, por exemplo, local.
O passo cinco trata das credencias de acesso. Nela você vai definir as senhas para os quatro usuários criados por default para o banco. Você pode definir uma senha para todos ou senhas diferentes para cada usuário.
No sexto passo, você consegue definir as opções de storage type, podendo ser: sistema de arquivo ou ASM. A localização ou diretório dos arquivos também pode ser definido nesta tela.
O passo seguinte trata da configuração de recuperação. Nesta tela, você deve estabelecer se vai usar uma área de recuperação flash e se vai habilitar o uso do archive mode. Aetapa oito do nosso fluxo visa tratar dos exemplos de esquema e script, geralmente, não é muito relevante.
O passo nove vai permitir ajustes nos parâmetros de inicialização. São quatro grupos de informações: (1) Memória, (2) Sizing, nesta guia, você especifica o menor tamanho de bloco e o número máximo de processos que podem se conectar simultaneamente ao banco de dados, (3)Character Sets e (4) Connection Mode, que pode ser escolhido entre DedicatedServer Mode e SharedServer Mode.

No passo seguinte, são definidas opções de storage. Nele você define a localização e quantidade dos arquivos de controle, de dados e de redo log.
O passo onze permite que você, além de criar o banco de dados, salve a configuração utilizada como um template e ainda gere o script de criação do banco de dados.
Com o banco de dados corretamente criado, podemos começar a trabalhar, adicionar objetos e fazer operações sobre eles. Mas antes, precisamos conhecer alguns aspectos sobre aEstrutura
Lógica e Física, os Objetos do Schema, os Tipos de Dados e a Estrutura de Memória.

ESTRUTURA LóGICA E FÍSICA

Vamos agora começar a tratar da arquitetura do banco de dados Oracle. O banco de dados é uma coleção de dados tratados de forma unitária. A finalidade de um banco de dados é armazenar e recuperar informações relacionadas. O servidor de banco de dados é a chave para resolver os problemas de gestão da informação. Em geral, um servidor gere de forma confiável uma grande quantidade de dados em um ambiente multiusuário, de modo que muitos clientes possam acessar,ao mesmo tempo, os mesmos dados. Tudo isso realizado, simultaneamente, deve oferecer alta performance. Um servidor de banco de dados também impede o acesso não autorizado e fornece soluções eficientes para a recuperação após falhas.
O Oracle Database é o primeiro banco de dados projetado para Grid Computing, a maneira mais flexível e de baixo custo de gerenciar informações e aplicativos. Grid Computing empresarial cria grandes agrupamentos de padrões industriais, armazenamento modular e servidores. Com esta arquitetura, cada novo sistema pode ser rapidamente provido a partir do conjunto de componentes.Não há necessidade de considerar os picos de trabalho, porque a capacidade pode ser facilmente adicionada ou realocada do pool de recursos, conforme necessário.
O banco de dados tem estruturas lógicas e estruturas físicas. Uma vez que as estruturas físicas e lógicas são separadas, o armazenamento físico de dados pode ser controlado sem afetar o acesso às estruturas de armazenamento lógico.
Visão geral da estrutura física

Nesta seção, explicamos as estruturas de banco de dados físicos de um banco de dados Oracle,
incluindo arquivos de dados (datafile), arquivos de log redo e arquivos de controle.

Datafiles

Cada banco de dados Oracle tem um ou mais arquivos de dados físicos. Os arquivos de dados contêm todos os dados do banco de dados. Os dados de estruturas de banco de dados lógicos, como tabelas e índices, estão fisicamente armazenados em arquivos de dados.
As características dos arquivos de dados são:

* Um arquivo de dados pode ser associado com apenas um banco de dados.

* Arquivos de Dados podem ter certas características definidas para deixá-los estender ou crescer, automaticamente, quando o banco de dados fica sem espaço.
* Um ou mais arquivos de dados formam uma unidade lógica de armazenamento de banco de dados chamada tablespace.
Os dados em um arquivo de dados são lidos, se necessário, durante a operação de banco de dados normal, e armazenados no cache de memória do Oracle. Por exemplo, suponha que um usuário queira acessar alguns dados de uma tabela de um banco de dados. Se a informação solicitada não estiver no cache de memória, ela é lida dos arquivos de dados apropriados e armazenados na memória.
Dados modificados ou novos dados não são necessariamente escritos para um arquivo de dados imediatamente. Para reduzir a quantidade de acesso ao disco e aumentar o desempenho, os dados são agrupados em memória e escritos para os arquivos de dados apropriados de uma só vez,como determinado pelo processo de gravação de dados que roda em background (database writer process - DBWn).
E como podemos incluir um datafile em uma tablespace? O comando do Oracle responsável pela alteração de espaços de tabela pode ser usado para diferentes propósitos. Pela sintaxe do comando, podemos observar esse fato:
ALTER TABLESPACE tablespace_name

{ DEFAULT

[ { COMPRESS | NOCOMPRESS } ] storoge_ctouse

| MINIMUM EXTENT integer [K|M|G|T|P|E]

| RESIZE integer [K|M|G|T|P|E]

| COALESCE

| RENAME TO new_tablespace_name

| { BEGIN | END } BACKUP

| { ADD { DATAFILE | TEMPFILE }

[ fi.Le_specificati.on

[, fiLe_specification ]

]

| DROP {DATAFILE | TEMPFILE } { 'filename' | file_number }

| RENAME DATAFILE 'filename' [, 'filename' ] TO 'filename' [, 'filename' ]

| { DATAFILE | TEMPFILE } { ONLINE | OFFLINE }

}

| { loggingclause | [ NO ] FORCE LOGGING }

| TABLESPACE GROUP { tablespace_group_name | '' }

| { ONLINE

| OFFLINE [ NORMAL | TEMPORARY | IMMEDIATE ]

}

| READ { ONLY | WRITE }

| { PERMANENT | TEMPORARY }

| AUTOEXTEND

{ OFF

| ON [ NEXT integer [K|M|G|T|P|E]]

[ MAXSIZE { UNLIMITED | integer [K|M|G|T|P|E]}]

}

| FLASHBACK { ON | OFF }

| RETENTION { GUARANTEE | NOGUARANTEE }

} ;

Nosso interesse está na adição de um novo DATAFILE a um TABLESPACE. Na definição do file_specification acima, temos a possibilidade de definir o tamanho (SIZE) para oDATAFILE, bem como outros parâmetros importantes para a incorporação e expansão dele. Veja na figura a seguir:
{ [ 'filename' | 'ASM_filename' ]

[ SIZE integer [K|M|G|T|P|EJ]
[ REUSE ]

[ AUTOEXTEND

{ OFF

| 0N [ NEXT integer [K|M|G|T|P|EJ]

[ MAXSIZE { UNLIMITED | integer [K|M|G|T|P|E]}]

}

]

[ 'filename | ASM_filename'

| ('filename | ASM_filename'

[, 'filename | ASM_filename' ] )

[ SIZE integer [K|M|G|T|P|E]J
[ REUSE ]

}

Apenas complementando com algumas informações extras. O tamanho de um tablespace é o tamanho dos arquivos de dados (DATAFILES) que constituem o tablespace. O tamanho de um banco de dados é o tamanho coletivo dos tablespaces que constituem o banco de dados. Para alocar mais espaço em um banco de dados, você pode optar por usar uma das três maneiras seguintes: adicionar um arquivo de dados a um tablespace, adicionar um novo tablespace ou aumentar o tamanho de um arquivo de dados.
Um tablespace em um banco de dados Oracle consiste em um ou mais arquivos de dados físicos. Um arquivo de dados pode ser associado a apenas um tablespace e a apenas um banco de dados.
Você pode alterar o tamanho de um arquivo de dados após sua criação ou especificar que um arquivo de dados deve crescer dinamicamente à medida que os objetos de esquema no espaço de tabela crescem. Essa funcionalidade permite que você tenha menos arquivos de dados em cada tablespace e pode simplificar a administração de arquivos de dados.
Você utiliza o SIZE para definir o tamanho do DATAFILE, quando adiciona o mesmo a uma tablespace. Agora é possível ainda utilizar a auto expansão, o tamanho máximo e o incremento feito a cada execução. Veja abaixo:
ALTER TABLESPACE users

ADD DATAFILE 7u02/oracle/rbdbl/users03.dbf' SIZE 10M
AUTOEXTEND ON

NEXT 512K
MAXSIZE 250M;

1. Ano: 2017 Banca: FGV Órgão: Alerj Cargo: Analista de Tecnologia da Informação Q. 44

O SGBD Oracle llg armazena logicamente seus dados em tablespaces e fisicamente em datafiles associados à tablespace. Considere um banco de dados com a tablespace tbs_03.
Para aumentar esse banco, adicionando o datafile tbs_f04.dbf à tablespace tbs_03, deve-se executar o comando:
(A) CREATE TABLESPACE tbs_03 DATAFILE 'tbs_f04.dbf;

(B) ALTER TABLESPACE tbs_03 ADD DATAFILE 'tbs_f04.dbf SIZE 100K;

(C) CREATE DATAFILE 'tbs_f04.dbf ON tbs_03 TABLESPACE;

(D) ALTER DATABASE AUTOEXTEND 'tbs_f04.dbf ON tbs_03;

(E) ADD DATAFILE 'tbs_f04.dbf ON TABLESPACE tbs_03 SIZE 100K;

i Comentário: Já falamos sobre a incorporação de um datafile a um espaço de tabelas.
Desta forma, podemos considerar a alternativa B como correta por apresentar uma sintaxe consistente com o comando em questão.
Gabarito: B

Arquivos de controle

Cada banco de dados Oracle tem um arquivo de controle binário. Um arquivo de controle contém entradas que especificam a estrutura física do banco de dados. Por exemplo, ele contém as seguintes informações:
* Nome do banco

* Nomes e localizações de arquivos de dados e arquivos de log de redo

* Carimbo de tempo da criação de banco de dados

O banco de dados Oracle pode fazer multiplex do arquivo de controle, ou seja, manter simultaneamente um número de cópias idênticas do arquivo de controle para se proteger contra uma falha envolvendo o arquivo.
Toda vez que uma instância de um banco de dados Oracle é iniciada, seu arquivo de controle identifica o banco de dados e os arquivos de log de redo que devem ser abertos para a operação prosseguir. Se a composição física do banco de dados é alterada (por exemplo, se um novo arquivo de dados ou arquivo de log é criado), então o arquivo de controle é automaticamente modificado pelo Oracle para refletir a mudança. Um arquivo de controle também é usado na recuperação de banco de dados.
HORA DE

PRATICAR!

(Ministério da Economia - Infraestrutura - 2020) Com relação ao sistema gerenciador de banco de dados Oracle, julgue o próximo item.
96 Arquivos de controle possuem formato texto plano, que registra toda a estrutura lógica do banco de dados; sem eles, o banco pode ser montado, mas não pode ser recuperado em caso de incidente.
Comentários:

O arquivo de controle é um arquivo binário necessário para iniciar e operar com sucesso o banco de dados. Caso o arquivo de controle não esteja acessível por alguma razão, o banco de dados não irá funcionar corretamente,podendo trazer problemas ao iniciar a instância. Todo arquivo de controle é sempre associado somente a um único banco de dados,não podendo existir um arquivo de controle que seja utilizado por mais de uma instância.
Gabarito Errado.

Arquivos de log de redo

Cada banco de dados Oracle tem um conjunto de dois ou mais arquivos de log de redo.
O
conjunto de arquivos de log de redo é coletivamente conhecido como o log de redo do banco de dados. Um log redo é composto de entradas de redo (também chamados de registros de redo).
A principal função do log de redo é gravar todas as alterações feitas nos dados. Se uma falha impede que os dados modificados sejam gravados permanentemente nos arquivos de dados,então as alterações podem ser obtidas a partir de log de redo. Por isso, o trabalho nunca é perdido.
Para se proteger contra uma falha envolvendo o redo log em si, o Oracle permite que um log de redo seja multiplexado visando que duas ou mais cópias do log de redo sejam mantidas em discos diferentes.
As informações em um arquivo de log redo são usadas apenas para recuperar o banco de dados a partir de uma falha do sistema ou mídia que impede que os dados do banco de dados sejam gravados nos arquivos de dados. Por exemplo, se uma falha de energia inesperada termina a operação de banco de dados, assim os dados na memória não puderam ser escritos nos arquivos de dados e podem ser perdidos. No entanto, os dados perdidos podem ser recuperados quando o banco de dados é reiniciado, após a energia ser restaurada.
Ao aplicar as informações mais recentes dos arquivos de log de redo nos arqu.ivos de dados, oOracle restaura o banco de dados para o momento em que a falha de energia ocorreu.
O processo de aplicação de log de redo durante uma operação de recuperação é chamado roll foward. O roll forward consiste em aplicar sequencialmente as alterações de blocos (redo records)contidas nos registros do redo log.
Archive Log Files

Você pode ativar o arquivamento automático do log de redo. A
Oracle arquiva automaticamente os arquivos de log quando o banco de dados está no modo ARCHIVELOG.
Arquivos de Parâmetros

Arquivos de parâmetros contêm uma lista de parâmetros de configuração para a instância e o banco de dados.
A Oracle recomenda que você crie um arquivo de parâmetro de servidor (SPFILE), como uma forma dinâmica de manter parâmetros de inicialização. Um arquivo de parâmetro de servidor permite armazenar e gerenciar seus parâmetros de inicialização persistentemente em um arquivo no disco do lado do servidor.
Arquivos de alerta ou trace de log

Cada processo do servidor e de background pode escrever em um arquivo de rastreamento associado. Quando um erro interno é detectado por um processo, ele despeja informações sobre o erro em seu arquivo de rastreamento. Algumas das informações gravadas em um arquivo de rastreamento são projetadas para o administrador de banco de dados, enquanto outras são para osServiços de Apoio Técnico da Oracle. Informações do arquivo de rastreamento também são usadas para otimização de aplicações e instâncias.
O arquivo de alerta, ou log de alerta, é um arquivo de rastreamento especial. O log de alerta de um banco de dados é um registro cronológico de mensagens e erros.
Arquivos de Backup

Restaurar um arquivo é basicamente substituí-lo pelo dado contido no arquivo de backup.Normalmente, você restaura um arquivo quando um erro de falha de mídia ou usuário tenha danificado ou excluído o arquivo original.
O backup e a recuperação gerenciados pelo usuário requerem que você realmente restaure os arquivos de backup antes de poder executar uma recuperação. Backup e recuperação são gerenciados pelo processo servidor. Tarefas como o agendamento de backups, bem como o processo de recuperação, por exemplo, devem aplicar o arquivo de backup correto quando a recuperação é necessária.
Após conhecer todos os arquivos físicos presentes no Oracle, vamos agora fazer uma análise da estrutura lógica do SGBD.
Visão geral da estrutura lógica

As estruturas de armazenamento lógicas, incluindo blocos de dados, extensões e segmentos,
permitem ao Oracle ter um controle refinado do uso de espaço em disco. Antes de tratarmos de alguns detalhes destas estruturas, observem abaixo a figura que mostra a hierarquia entre elas:
Lagical Physical

O gráfico acima descreve a relação entre estruturas de armazenamento físico e lógico em pé notação de galinha. Na coluna à esquerda, temos as estruturas lógicas que são Tablespace,Segmento, extensão e bloco de dados Oracle. Cada tipo tem um relacionamento um-para-muitos com o tipo abaixo dele. Na coluna à direita, apresentamos as estruturas físicas, que são os arquivos de dados e blocos de sistema operacional. Tablespace tem um relacionamento um-para-muitos comDatafile. Bloco de dados Oracle tem um relacionamento um-para-muitos com bloco de SO.

Tablespaces

Um banco de dados é dividido em unidades de armazenamento lógicas denominadas tablespaces, que são grupos de estruturas lógicas relacionadas. Por exemplo, tablespaces comumente agrupam todos os objetos de uma aplicação para simplificar algumas operações administrativas.
Cada banco de dados é logicamente dividido em uma ou mais áreas de tabela. Um ou mais arquivos de dados são criados explicitamente para cada tablespace visando armazenar fisicamente os dados de todas das estruturas lógicas em um espaço de tabela. A soma dos tamanhos(size) dos arquivos de dados em um espaço de tabela é a capacidade de armazenamento total da tablespace.
Cada banco de dados Oracle contém uma tablespace SYSTEM e uma tablespace SYSAUX. O
Oracle cria automaticamente cada tablespace quando o banco de dados é criado. O padrão do sistema é criar uma smallfile tablespace, que é o tipo tradicional de tabelspace Oracle. As tablespaces SYSTEM e SYSAUX são criados como espaços de tabela smallfile.
A Oracle também permite criar espaços de tabela bigfile. Isso permite que o Oracle
Database contenha espaços de tabela formados a partir de poucos arquivos grandes em vez de vários menores. Isso ajuda ao Oracle Database utilizar a capacidade dos sistemas de 64 bits para criar e gerenciar arquivos do tipo ultralarge. A consequência disto é que o Oracle Database agora pode ser dimensionado para até oito exabytes de tamanho. Com os arquivos de gerenciamento daOracle, os espaços de tabela bigfile são arquivos de dados completamente transparentes aos usuários. Em outras palavras, você pode executar operações em tablespaces, em vez de utilizar os arquivos de dados subjacentes.
Uma tablespace pode ser on-line (acessível) ou offline (não acessível). Um espaço de tabela é geralmente on-line, de modo que os usuários podem acessar as informações da tablespace.No entanto, por vezes, uma tablespace é tirada do ar fazendo com que parte da base de dados fique indisponível, ao mesmo tempo em que permite o acesso normal ao restante da base de dados. Isso faz com que muitas tarefas administrativas sejam mais fáceis de executar.
2. BANCA: FCC ANO: 2014 ÓRGÃO: TRT - REGIÃO (RJ) PROVA: ANALISTA JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

O sistema gerenciador de Bancos de Dados Oracle llg armazena as tabelas de dicionário de dados na tablespace
A MAIN.

B SYSTEM.
C SYSAUX.
D UNDO.
ETEMP.

Comentário. Todas as tabelas relativas ao dicionário de dados são armazenadas na tablespaceSYSTEM. As views do dicionário de dados servem como uma referência para todos os usuários do banco de dados. Algumas views podem ser acessadas por todos os usuários, enquanto outras são específicas para administradores do sistema de gerenciamento do banco de dados.
O dicionário de dados consiste em um conjunto de views. Em vários casos, um conjunto consiste em três views contendo informações similares, mas que são diferenciadas por seus respectivos prefixos: USER, ALL e DBA.
USER_*: são views que disponibilizam informações a respeito do schema de determinado usuário (USER);
ALL_*: são views que estão disponíveis para o usuário;

DBA_*: são views que disponibilizam informações de administração e contêm dados de todos os schemas de usuários.
Podemos, portanto, marcar nossa reposta na alternativa B.

Gabarito B

Oracle Data Blocks

No menor nível de granularidade, os dados de banco de dados Oracle são armazenados em blocos de dados. Um bloco de dados corresponde a um número específico de bytes de dados de espaço físico no disco. O tamanho do bloco padrão é especificado pelo parâmetro de inicializaçãoDB_BLOCK_SIZE. Além disso, você pode especificar até cinco outros tamanhos de blocos. Um banco de dados usa e aloca seu espaço livre em termos de blocos de dados Oracle.
Extensões

O próximo nível lógico de espaço de banco de dados é o da extensão. Uma extensão é um número específico de blocos de dados contíguos, obtido numa única atribuição,usado para armazenar um tipo específico de informação.
Segmentos

Acima de extensões, o nível de armazenamento de base de dados lógica é o segmento. Um segmento é um conjunto de extensões alocadas para uma determinada estrutura lógica. Alista a seguir descreve os diferentes tipos de segmentos.
* Segmento de dados - Cada tabela sem clusters tem um segmento de dados. Todos os dados de uma tabela são armazenados nas extensões de segmento de dados. Para uma tabela com partições, cada partição tem um segmento de dados. Cada cluster também tem um segmento de dados. Os dados de todas as tabelas de um cluster são armazenados no segmento de dados do cluster.
* Segmento de índice - Cada índice tem um segmento de índice que armazena todos os seus dados. Para um índice particionado, cada partição tem um segmento de índice.
* Segmento temporário - Segmentos temporários são criados pela Oracle quando uma instrução SQL precisa de uma área de banco de dados temporária para concluir a execução. Quando a instrução termina, as extensões do segmento temporário são devolvidas ao sistema para uso futuro.
* Segmento de rollback - Se você estiver operando no modo de gerenciamento automático de undo, o servidor de banco de dados gerencia o desfazer com a utilização de tablespaces. A Oracle recomenda que você use o gerenciamento de undo automático.
As versões anteriores da Oracle usam segmentos de rollbalk para armazenar informações de undo. A informação em um segmento de reversão era usada durante a recuperação de banco de dados para gerar informações de leitura consistente e para reverter as transações não confirmadas(commit). A gestão de espaço para esses segmentos de reversão era complexa, e a
Oracle resolveu depreciar esse método.
A Oracle faz uso do segmento de rollback SYSTEM para a realização de transações do sistema.
Existe apenas um segmento de rollback SYSTEM, que é criado automaticamente durante a execução do comando CREATE DATABASE e é sempre colocado online na inicialização da instância.Você não é obrigado a executar quaisquer operações para gerenciar o segmento de rollback SYSTEM.
A Oracle aloca dinamicamente espaço quando as extensões existentes em um segmento ficam completas. Em outras palavras, quando as extensões de um segmento estão cheias, aOracle aloca outra para aquele segmento. Devido ao fato de as extensões serem atribuídas conforme a necessidade, as extensões de um segmento podem ou não serem armazenadas de forma contígua no disco.
Vamos agora fazer uma questão sobre este assunto. Ao final da aula, traremos mais algumas questões que abordam esse conteúdo.
3. BANCA: FCC ANO: 2008 ÓRGÃO: TRT - 2§ REGIÃO (SP) PROVA: ANALISTA JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

A estrutura lógica de armazenamento nas bases de dados Oracle é representada na sequência hierárquica de
A segmentos, blocos de dados e extensões.
B segmentos, extensões e blocos de dados.
C extensões, segmentos e blocos de dados.
D extensões, blocos de dados e segmentos.
E blocos de dados, segmentos e extensões.

Comentário: Apenas relembrando a sequência da hierarquia de armazenamento: bloco de dados < extensões < segmentos < tablespace. Já falamos sobre isso em questões anteriores.Esta questão é somente para fixarmos o conteúdo.

Gabarito: B

OBJEToS Do SCHEMA

Um esquema é uma coleção de objetos de banco de dados. Um esquema é de propriedade de um usuário de banco de dados e, geralmente, tem o mesmo nome do usuário. Objetos de esquema são as estruturas lógicas que fazem referência direta aos dados do banco de dados.Objetos de esquema incluem estruturas, como tabelas, visões e índices. (Não há nenhuma relação entre uma tablespace e um esquema. Os objetos no mesmo esquema podem estar em diferentes espaços de tabela e uma tablesapce pode conter objetos de diferentes esquemas). Alguns dos objetos de esquema mais comuns são definidos abaixo:
Tables

As tabelas são a unidade básica de armazenamento de dados em um banco de dados
Oracle.
Tabelas de um banco de dados armazenam os dados acessíveis ao usuário. Cada tabela tem colunas e linhas. Uma tabela que tem os dados do empregado, por exemplo, pode ter uma coluna chamadaCPF do funcionário, e cada linha nessa coluna representa o CPF de um empregado.

índices

Os índices são estruturas opcionais associados às tabelas. Os índices podem ser criados para aumentar o desempenho de recuperação de dados. Assim como o índice desta aula ajuda a localizar mais rapidamente informações específicas, um índice Oracle fornece um caminho mais rápido de acesso aos dados da tabela.
Quando processa uma consulta SQL, o Oracle pode utilizar alguns ou todos os índices disponíveis para localizar as linhas solicitadas de forma mais eficiente. Os índices são úteis quando as aplicações querem consultar uma tabela para um intervalo de linhas (por exemplo,todos os funcionários com um salário maior do que 1000 dólares) ou para uma linha específica.
Os índices são criados sobre uma ou mais colunas de uma tabela. Depois de criado, um
Índice é mantido e utilizado pelo Oracle automaticamente. Alterações nos dados da tabela (como a adição de novas linhas, atualização ou exclusão de linhas) são automaticamente incorporadas em todos os índices relevantes com total transparência para os usuários.
Views

As views são apresentações personalizadas de dados em uma ou mais tabelas ou de outras visões. Uma visão também pode ser considerada uma consulta armazenada. Visões não contêm os dados realmente. Em vez disso, elas derivam seus dados das tabelas nas quais se baseiam,conhecidas como as tabelas de base da visão.

Como tabelas, os dados de uma view podem ser consultados, atualizados, inseridos e excluídos,com algumas restrições. Todas as operações executadas em uma visão afetam as tabelas base da visão.
Visões fornecem um nível adicional de segurança para a tabela, restringindo o acesso a um conjunto predeterminado de linhas e colunas. Eles também escondem a complexidade de dados e armazenam consultas complexas.
Clusters

Clusters são grupos de uma ou mais tabelas armazenadas fisicamente juntas, porque elas compartilham colunas comuns e são muitas vezes utilizadas em conjunto.Porque linhas relacionadas são armazenadas fisicamente juntas, o tempo de acesso ao disco melhora.
Como índices, os clusters não afetam o design da aplicação. Se uma tabela é parte de um cluster ou não, isso é transparente para os usuários e aplicações. Os dados armazenados em uma tabela em cluster são acessados por SQL da mesma forma como os dados armazenados em uma tabela sem clusters.
Synonyms

Um sinônimo é um alias para qualquer tabela, visão, visão materializada,
sequência,
procedimento armazenado, função, pacote, tipo, objeto de esquema de classe Java, um tipo de objeto definido pelo usuário, ou outro sinônimo. Porque um sinônimo é simplesmente um alias, não requer nenhum armazenamento, além da sua definição no dicionário de dados.
DICIoNÁRIo DE DADoS

Cada banco de dados Oracle tem um dicionário de dados. Um dicionário de dados Oracle é um conjunto de tabelas e visões que são usadas como uma referência apenas de leitura sobre o banco de dados. Por exemplo, um dicionário de dados armazena informações sobre a estrutura lógica e física do banco de dados. Um dicionário de dados também armazena as seguintes informações:
* Os usuários válidos de um banco de dados Oracle

* Informações sobre restrições de integridade definidas para tabelas no banco de dados

* A quantidade de espaço alocado para um objeto de esquema e quanto está em uso

Um dicionário de dados é criado quando uma base de dados é criada. Para refletir com precisão o status do banco de dados em todos os momentos, o dicionário de dados é atualizado automaticamente pelo Oracle em resposta a ações específicas, como quando a estrutura do banco de dados é alterada. O banco de dados conta com o dicionário de dados para registrar, verificar e realizar trabalhos em curso. Por exemplo, durante a operação de banco de dados, oOracle lê o dicionário de dados para verificar a existência de objetos de esquema e quais usuários têm acesso a eles.
TIPoS DE DADoS

Existe uma variedade de tipos de dados no Oracle. Para entender esses tipos de dados,
é preciso conhecer como eles se classificam. Uma das formas que nos ajuda a entender é comparar os tipos do Oracle com os de SQL. SQL inclui cinco tipos de dados pré-definidos:string, numéricos,
datetime, interval e boolean. Primeiramente, vamos falar dos tipos de dados formados por cadeias de caracteres. No SQL padrão, esses tipos são divididos em tamanho fixo e variável. Todas as cadeias de caracteres em SQL podem ser de comprimento fixo ou variável.
Como você pode imaginar, essa flexibilidade tem um preço de desempenho, pois o SGBD
deve executar a tarefa adicional de alocação dinâmica. Um CHAR ou CHARACTER especifica o número exato de caracteres que serão armazenados para cada valor. Por exemplo, se você definir o número de caracteres em 10, mas o valor tiver apenas seis caracteres, os quatro caracteres restantes serão completados com espaços em branco. Um exemplo da sintaxe do comando seria:CONCURSOJMOME CHAR (100).

O outro tipo de cadeia de caracteres é o CHARACTER VARYING ou VARYING CHAR ou VARCHAR.
Ele especifica o número máximo de caracteres que pode ser incluído em um dado. O
número de caracteres armazenados é exatamente o mesmo número do valor introduzido, de modo nenhum espaço é adicionado ao valor. Um exemplo da definição de uma coluna deste tipo:CONCURSO_NOME VARCHAR (60).

Ainda dentro das strings, temos as strings binárias. Uma string binária é uma sequência de bytes da mesma forma que uma string de caracteres é uma sequência de caracteres. Ao contrário de strings de caracteres que geralmente contêm informações na forma de texto, ela é usada para armazenar dados não tradicionais, tais como imagens, áudio e arquivos de vídeo,executáveis de programa, e assim por diante. Sua definição no SQL é BINARY LARGE OBJECT, conhecida como BLOB.O BLOB armazena grandes grupos de bytes, até o valor especificado.

Estes são os principais tipos de dados de caracteres. As instruções SQL que criam tabelas e clusters também podem usar tipos de dados ANSI. O Oracle reconhece o nome do tipo de dadosANSI que difere do nome do tipo de dados do Oracle Database. Ele converte o tipo de dados no tipo de dados Oracle equivalente, registra o tipo de dados Oracle como o nome do tipo de dados da coluna e armazena os dados da coluna no tipo de dados Oracle com base nas conversões mostradas nas tabelas a seguir:
Conversão de Tipos de Dados do ANSI SQL para Oracle
ANSI SQL Data Type Oracle Data Type

CHARACTER(n)

CHAR(n)

CHARACTER VARYING(n)
CHAR VARYING(n)
NATIONAL CHARACTER(n)
NATIONAL CHAR(n)
NCHAR(n)

NATIONAL CHARACTER VARYING(n)
NATIONAL CHAR VARYING(n)
NCHAR VARYING(n)

NUMERIC[(p,s)]

DECIMAL[(p,s)]
INTEGER

INT
SMALLINT
FLOAT

DOUBLE PRECISION
REAL

CHAR(n)
VARCHAR2(n)

NCHAR(n)

NVARCHAR2(n)

NUMBER(p,s)

NUMBER(p,0)

FLOAT(126)
FLOAT(126)
FLOAT(63)

Vamos agora tratar dos tipos de dados numéricos. Eles são divididos em duas grandes categorias: números exatos (exact numbers) e números aproximados (approximate).Os números exatos podem ser números inteiros (lápis, pessoas ou planetas) ou ter casas decimais(preços, pesos ou percentuais). Os números podem ser positivos e negativos.
Eles podem ter precisão e escala. O que seria isso? A precisão(p) determina o número total máximo de dígitos decimais que podem ser armazenados (tanto à esquerda quanto à direita do ponto decimal). E escala(e) especifica o número máximo de casas decimais permitidas.Eles estão disponíveis da seguinte forma no SGBD Oracle:
Os números de ponto flutuantes ou aproximados são números que não podem ser representados com precisão absoluta. Vejam acima a relação entre os tipos SQL padrão e o Oracle.Alguns comentários importantes sobre os aspectos numéricos do Oracle.

Os tipos de dados NUMERIC e DECIMAL do SQL ANSI são representados pelo tipo NUMBER no
Oracle. Eles só podem ser definidos como números de ponto fixo. E para esses tipos de dados o valor padrão para a escala é zero (0). O tipo de dado FLOAT é um tipo de ponto flutuante com precisão binária b. O valor default para a precisão neste tipo de dados é de 126 casa binárias ou 38 casas decimais.
Perceba que utilizamos o tipo FLOAT do Oracle para representar os tipos DOUBLE PRECISION e
REAL do SQL ANSI. O tipo de dados DOUBLE PRECISON é também um número de ponto flutuante com precisão binária de 126. E por fim, o tipo REAL é um ponto flutuante com precisão de 63 casas binárias ou 18 casas decimais. Esses valores são informados como parâmetros, conforme podemos observar na tabela acima.
1. PROVAS: FCC ANO: 2013 PROVA: TRT - 12^ REGIÃO (SC) - TÉCNICO JUDICIÁRIO - TECNOLOGIA
DA INFORMAÇÃO

Disciplina: Banco de Dados (TI) - Assuntos:

NÃO é um dos tipos de dados nativos do Oracle:

a) LONG.

b) BINARY_DOUBLE

c) NUMERIC.

d) BINARY_FLOAT.

e) ROWID.

í Comentário: Essa questão faz uma remissão ao assunto que acabamos de estudar.
Percebam a importância de conhecer os tipos de dados e as diferenças em relação ao padrão SQLANSI.
Neste caso, temos um tipo de dados, o NUMERIC, que não é um tipo de dados padrão do
Oracle, mas é do SQL ANSI. E importante entender que o Oracle aceita. Sendo assim,
nossa resposta está presente na alternativa C.
Gabarito: C

Para concluir o nosso estudo sobre tipos de dados numéricos, apresentamos uma tabela que relaciona os tipos com o espação de armazenamento necessário para cada valor associado e o range,que seria os valores possíveis ou domínio de um determinado tipo numérico.

Vamos agora falar sobre o tipo DATE. DATE é uma estrutura que consiste em três elementos:ano, mês e dia. O ano é um número de quatro dígitos que permite que os valores de 0000 a 9999. O
mês é um elemento de dois dígitos com valores de 01 a 12 e dia, que tem dois dígitos com um intervalo de 01 a 31. O SQL ANSI define a semântica de data usando a estrutura descrita acima, mas os SGBDs não são obrigados a usar essa abordagem, desde que a implementação produza os mesmos resultados.
O tipo TIME consiste de hora, minuto e segundo. A hora é um número de 00 a 23. O
minuto é um número de dois algarismos, de 00 a 59. O segundo é um inteiro entre 00-59 ou um número decimal com uma escala mínima de cinco e precisão mínima de três, que pode conter valores de00.000 a 59.999.

DATA TYPE STORAGE SIZE
(BYTES)

RANGE

INTEGER 4 -2,147,483,648 to

+2,147,483,647

TINYINT 1 0 through 255

SMALLINT 2 -32,768 to + 32,768

BIGINT 8 -9,223,372,036,854,775,808
to

+9,223,372,036,854,775,808

MONEY 8 - 922,337,203,685,477.5808 to +

922,337,203,685,477.5807

SMALLMONEY 4 - 214,748.3648 to

+ 214,748.3647

REAL 4 The range is from negative 3.402E

+ 38 to negative 1.T75E - 37, or from positive 1.175E - 37 to 3.402E + 38. It also includes 0.
FLOAT 4 to 8 The number can be zero or can range from -1.79769E + 308 to-2.225E
- 307, or from 2.225E - 307 to
1.79769E + 308.

DOUBLE 8 The number can be zero or can range from -1.79769E + 308 to -2.225E
- 307, or from 2.225E - 307 to
1.79769E + 308.

Temos ainda os tipos: 1. DATETIME, que combina data e hora em um único tipo, com intervalo de datas; 2. TIMESTAMP, que engloba os campos DATE e TIME, mais seis posições para a fração decimal de segundos e uma qualificação opcional WITH TIME ZONE; e 3. INTERVAL, que serve para calcular o intervalo entre dois objetos que representam tempos.
Por fim, é importante saber que o valor nulo é membro de todos os tipos de domínios. Se você declarar o domínio de um atributo como NOT NULL, o SGBD vai proibir a inserção de valores nulos para essa coluna. Agora que vimos os tipos de dados, vamos passar rapidamente pela estrutura de memória do Oracle.
2. BANCA: FCC ANO: 2012 ÓRGÃO: TST PROVA: ANALISTA JUDICIÁRIO - TECNOLOGIA DA
INFORMAÇÃO

No SGDB Oracle, versão llg, os limites de tamanho para os tipos de dados CHAR e CHAR VARYING
são, respectivamente,

A 1000 e 2000 bytes.

B 1000 e 4000 bytes.

C 2000 e 4000 bytes.

D 2000 e 8000 bytes.

E 4000 e 8000 bytes.

Comentário: Falamos dos tamanhos dos tipos numéricos, mas não tratamos ainda do tamanho máximo dos tipos de dados de caracteres. Vejam abaixo os tamanhos dos tipos VARCHAR2 eCHAR, juntamente á sintaxe para a criação do tipo.

VARCHAR2(size [BYTE | CHAR])

O comprimento variável da sequência de caracteres tem seu valor máximo definido pelo parâmetro size, que pode ser definido em bytes ou char. O tamanho máximo é de 4000bytes ou caracteres, e o mínimo é de um byte ou um caractere. Você deve obrigatoriamente especificar o tamanho do tipo VARCHAR2.
CHAR [(size [BYTE | CHAR])]

Dados de caracteres com comprimento fixo de dados, que pode ser definido em bytes ou caracteres. O tamanho máximo é de 2000 bytes ou caracteres. O valor padrão e, também,mínimo é de um byte.

Desta forma podemos verificar os valores 2000 e 4000 bytes na alternativa C da questão acima.

Gabarito: C

Antes de continuarmos, vamos apresentar algumas tabelas que descrevem, de forma sucinta,
cada um dos tipos de dados que apresentamos nesta seção:
Oracle Data Type Descrição

Um conjunto de caracteres de comprimento variáve. CHAR indica que a semântica de caracteres é usada para dimensionar a string; BYTE indica que a semântica de bytes é usada.
VARCHAR2(size [BYTE | CHAR])

NVARCHAR2(síze)
NUMBER [ (p [, s]) ]
FLOAT [(p)]

LONG

DATE

BINARY-FLOAT
BINARY-DOUBLE
TIMESTAMP

[(fractional seconds precision)]
TIMESTAMP

[(fractional_seconds_precision)] WITH
TIMEZONE

TIMESTAMP

[(fractional_seconds_precision)] WITH
LOCAL TIMEZONE

INTERVAL YEAR [(year_precision)] TO
MONTH

INTERVAL DAY [(day_precision)] TO
SECOND

[(fractionalsecondsprecision)]
RAW(size)

LONG RAW
ROWID

UROWID [(size)]

CHAR [(size [BYTE | CHAR])]

NCHAR[(size)]
CLOB

NCLOB
BLOB
BFILE

Tamanho mínimo é 1 byte ou 1 caracter. Tamanho máximo é:

32767 bytes ou characters, se MAX_STRING_SIZE = EXTENDED
4000 bytes ou characters, se MAX STRING SIZE = STANDARD

Um conjunto de caracteres de comprimento variável com tamanho máximo:
32767 bytes, se MAX_STRING_SIZE = EXTENDED

4000 bytes, se MAX STRING SIZE = STANDARD

Um número com uma precisão (p) e escala (s). A precisão varia de 1 a 38 e a escala pode ser de -84 a 127.
Subtipo do tipo de dados NUMBER com precisão p. Um FLOAT é representado internamente como NUMBER. A precisão pode variar de 1 a 126 dígitos binários. Um FLOAT valor requer de 1a 22 bytes de espaço para seu armazenamento.

Um dado de caractere de comprimento variável com um comprimento até 2GB (231-1)
Valores de data de 1^ de janeiro de 4712 A.C. a 31 de dezembro de 9999 A.D.

Um número de ponto flutuante de 32 bits.
Um número de ponto flutuante de 64 bits.

Ano, mês, dia, hora, minuto, segundo e segundos fracionários. O valor de segundos_fracionários pode variar de 0 a 9; em outras palavras, até a precisão de um bilionésimo de um segundo. O padrão é 6 (um milionésimo).
Contém um valor de TIMESTAMP além de um valorde deslocamento de fuso horário. O
deslocamento de fuso horário pode ser um deslocamento UTC (como "-6:00") ou um nome de região (por exemplo, "US/Central").
Similar a TIMESTAMP with TIMEZONE, exceto que (1) os dados são normalizados de acordo com o fuso horário do banco de dados quando são armazenados e (2) durante a recuperação de colunas com esse tipo de dados, o usuário vê os dados no fuso horário da sessão.
Armazena um período de tempo em anos e meses.Ovalorde precisão_do_ano é o número de dígitos do campo YEAR.
Armazena um período de tempo como dias, horas, minutos, segundos e segundos fracionários. O valor para precisão_do_dia varia de 0 a 9, com um padrão igual a 2. O valorde precisão_dos_segundos_fracionários é similaraos segundos fracionários em um valorTIMESTAMP; o intervalo é de 0 a 9, com um padrão igual a 6.

Dados binários brutos, com com tamanho máximo:

32767 bytes, se MAX_STRING_SIZE = EXTENDED

2000 bytes, se MAX STRING SIZE = STANDARD

Dados binários brutos, comprimento variável, até 2GB.

Uma string em base 64 representando o endereço único de uma linha na sua tabela correspondente. Esse endereço é exclusivo em todo o banco de dados.
Uma string em base 64 representando o endereço lógico de uma linha na sua tabela organizada por índices. O tamanho máximo é 4000 bytes.
Uma string de caractere de comprimento fixo, cujo comprimento corresponde ao comprimento tamanho. O tamanho mínimo éleomáximoé 2000 bytes. Os parâmetros BYTE e CHAR, como em VAR-CHAR2.
Uma string de caractere de comprimento fixo de até 2000 bytes; o argumento tamanho máximo depende da definição do conjunto de caracteres nacional para o banco de dados. O
argumento tamanho padrão é igual a 1.

Um Character Large Object contendo caracteres single-byte ou multibytes; suporta conjunto de caracteres de largura fixa ou de largura variável. O tamanho máximo é (4GB - 1) *
DB BLOCK SIZE.

Similar ao CLOB, exceto que caracteres Unicode são armazenados tanto de conjuntos de caracteres de largura fixa quanto de largura variável. O tamanho máximo é (4GB - 1) *DB-BLOCK-SIZE.

Um Binary Large Object; o tamanho máximo é (4GB -1) * DB_BLOCK_SIZE.

Um ponteiro para um Large Binary File armazenado fora do banco de dados. Arquivos binários devem ser acessíveis a partir do servidor que executa a instância Oracle. O tamanho máximo é de 4GB.
ESTRUTURA DE MEMóRIA

Um servidor de banco de dados Oracle consiste em um banco de dados Oracle e uma instânciaOracle. Cada vez que um banco de dados for iniciado, a área global de sistema (SGA-
System global area) é alocada e processos da Oracle de background são iniciados. A combinação dos processos em segundo plano com os buffers de memória é chamada de instância Oracle.
Algumas arquiteturas de hardware (por exemplo, sistemas de disco compartilhados) permitem que vários computadores possam compartilhar o acesso aos dados, ao software ou a dispositivos periféricos. O Real Application Clusters (RAC) tira proveito de tal arquitetura, executando várias instâncias que compartilham um único banco de dados físico. Na maioria das aplicações,o RAC
permite o acesso a um único banco de dados por usuários em vários computadores com melhor desempenho.
3. BANCA: CESPE ANO: 2013 ÓRGÃO: TRT - 82 REGIÃO (PA E AP) PROVA: ANALISTA JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

A respeito do sistema de gerenciamento de banco de dados Oracle, versão llg, assinale a opção correta. Nesse sentido, considere que a sigla RAC, sempre que utilizada,refere-se a Real
Application Clusters.

A PGA (Program Global Area) é um grupo de estruturas de memória compartilhada pelos usuários da instância Oracle. Quando uma instância Oracle é iniciada, a memória é alocada para a PGA com base nos valores especificados no arquivo de parâmetros de inicialização.
B O processo Log Writer executa a recuperação de falhas, aplicando as entradas dos arquivos de redo log online aos arquivos de dados.
C Um servidor Oracle é composto de duas entidades: a instância e o banco de dados. O banco de dados é aberto durante o processo de inicialização e, depois, a instância é iniciada.
D Oracle Enterprise Manager Grid Control é uma ferramenta gráfica para gerenciar um banco de dados, que pode ser um banco de dados em cluster, com a funcionalidade de RAC ao passo que o Grid Control dispõe de recursos para gerenciamento e monitoramento em tempo real,para executar tarefas agendadas, como operações de backup e para reportar condições de alerta interativamente e por email.
E Por meio do recurso RAC, é possível que mais de uma instância, em servidores separados, acesse os mesmos arquivos de dados. Para implementar o RAC, o banco de dados compartilhado deve estar armazenado em um subsistema de discos com RAID ativado para garantir que cada componente do sistema de armazenamento seja tolerante a falhas.
Comentário: Vamos comentar cada uma das alternativas acima:

Na alternativa A, temos uma troca entre os conceitos de SGA e PGA. Lembrem-se que SGA
(SYSTEM GLOBAL AREA) refere-se à área de memória compartilhada. Já o PGA (PROGRAM

GLOBAL AREA) trata da área de memória não compartilhada, ou seja, um PGA é alocado para cada processo.
Já a alternativa B expõe o LGWR (Log Writer), que é responsável pelo gerenciamento do buffer do log de redo. Uma transação só é considerada completa ou efetivada quando o LGWRgrava com sucesso as informações do redo.
Para responder a alternativa C, temos que ter em mente que um servidor Oracle é composto por duas entidades: a instância e o banco de dados. A primeira possui as estruturas de memória e os processos. Durante o processo de inicialização, a instância é inicializada(started)
e o banco de dados é aberto (open).

O ORACLE ENTERPRISE MANAGER DATABASE CONTROL é uma ferramenta gráfica para gerenciar bancos de dados, que pode ser definido como um banco de dados isolado ou um cluster, com a funcionalidade de RAC. Por outro lado, o GRID CONTROL dispõe de recursos para gerenciamento e monitoramento em tempo real, para executar tarefas agendadas,como operações de backup e para reportar condições de alerta interativamente e por e-mail.
Vejam que pelas explicações teóricas elencadas até aqui, não nos resta muita opção. A resposta está presente alternativa E. Não precisamos de muito conhecimento sobre RAC para resolver a questão. Apenas a definição é suficiente para marcarmos a alternativa correta.Vejamos alguns pontos importantes sobre RAC:
O Oracle Real Application Clusters (RAC) é uma opção do Banco de dados Oracle introduzida pela primeira vez com o Oracle 9i. O Oracle RAC fornece opções para dimensionar aplicações,além da capacidade de um único servidor. Isso permite que os clientes tirem proveito de hardwares padronizados de baixo custo para reduzir seu custo total de propriedade e para fornecer um ambiente de computação redimensionável que suporte a carga de trabalho de suas aplicações.
O Oracle RAC permite que o Banco de dados Oracle execute todos os tipos de aplicações i corporativas de base em clusters, incluindo produtos empacotados (conhecidos como o OracleApplications, Peoplesoft, SAP), aplicações desenvolvidas internamente, que podem ser OLTP,
DSS ou uma carga de trabalho mista. Assim, podemos marcar o gabarito na alternativa E.

Gabarito: E

Um servidor de banco de dados Oracle usa estruturas de memória e processos para gerenciar e acessar o banco de dados. Todas as estruturas de memória principal existem na memória dos computadores que constituem o sistema de base de dados. Os processos são postos de trabalho(Jobs) que funcionam na memória desses computadores.

O Oracle cria e usa estruturas de memória para completar ou executar vários jobs. Por exemplo, a memória armazena o código do programa que está sendo executado e os dados compartilhados entre os usuários. Duas estruturas de memória básicas são associadas com a Oracle:Área global de sistema (SGA - system global area) e área global do programa (PGA -
program global area). Abaixo explicaremos cada uma delas em detalhes. Antes vejam as estruturas descritas na figura:
System Global Area (SGA)

System Global Area (SGA) é uma região de memória compartilhada que contém os dados e informações de controle para uma instância Oracle. O Oracle aloca a SGA quando uma instância é iniciada e desaloca quando a instância é finalizada. Cada instância tem seu próprio SGA.
Usuários conectados a um banco de dados Oracle compartilham os dados da SGA. Para um desempenho ideal, a SGA deve sertão grande quanto possível (enquanto houver espaço na memória real) para armazenar os dados em memória e minimizar operações de l/O no disco.
Por ser uma área de memória em modo de leitura e gravação, todos os processos de segundo plano e processos servidores do banco de dados executados em nome dos usuários terão permissão para ler ou gravar blocos de dados dentro da instância da SGA.
O Oracle permite, por ser uma memória dinâmica, que o tamanho da SGA seja ajustado em tempo de execução, sem a necessidade de baixar ou indisponibilizar o ambiente de banco de dados.
A memória para a SGA é alocada em unidades granulares, onde um grão pode ter 4MB ou
16MB. Se a SGA for menor ou igual a 128MB, o crescimento será de 4MB. Do contrário,
o aumento será de 16MB.
A quantidade total de memória alocada para a SGA é definida pelo parâmetro
SGA_MAX_SIZE.
Se o parâmetro SGA_MAX_SIZE, especificado no arquivo de parâmetros de inicialização,
apresentar um valor menor do que a soma de todos os valores especificados dos demais componentes da SGA,no momento da inicialização, a configuração no arquivo de parâmetros de inicialização será ignorada.
Para visualizar o tamanho atual da SGA, utilize o comando SHOW SGA. Nas seções subsequentes, iremos discutir as áreas que constituem a SGA. As informações armazenadas na SGAsão divididas em vários tipos de estruturas de memória, incluindo os buffers de banco de dados,redo log buffer e a shared pool.

Database Buffer Cache

O cache do buffer do banco de dados, também chamado de cache do buffer, é a área de memória que armazena cópias de blocos de dados lidos a partir de arquivos de dados.
Um buffer é um endereço de memória principal, no qual o gerenciador de buffer armazena temporariamente um bloco de dados recentemente usado. Todos os usuários conectados simultaneamente a uma instância de banco de dados compartilham o acesso ao mesmo cache do buffer.
O cache de buffer contém blocos de dados modificados, bem como blocos não modificados.
Como os dados mais recentemente (e, muitas vezes, o mais frequentemente) usados são mantidos na memória, menos operações de l/O em disco são necessárias, e o desempenho é melhorado.
Os blocos de dados, preservados no Buffer Cache, podem adquirir três tipos de estados:

* Buffers sujos (Dirty Buffers)

* Buffers livres (Free Buffers)

* Buffers fixados (Pinned Buffers).

Buffers sujos contêm blocos de dados alterados ou acrescentados, devido a uma instrução
DML, que ainda não foram submetidos a commit. Esse buffer não pode ser reutilizado até que estes blocos de dados sejam gravados com êxito no disco.
Buffers livres são buffers que não possuem dados armazenados ou que guardam blocos de dados que são idênticos aos blocos correspondentes no disco. Áreas de buffers livres podem ser substituídas em uma operação de leitura do disco a qualquer momento.
Buffers fixados são buffers que estão em uso por comandos DML ou são explicitamente salvos para uso futuro e, portanto, não podem ser utilizados por outras transações.
No momento em que uma consulta é processada, é realizada uma varredura no buffer cache pelos blocos solicitados. Se o bloco não for localizado em memória, será efetuada uma leitura física do bloco no arquivo de dados em disco e enviada uma cópia dos blocos necessários para o BufferCache. Esta é uma das principais funções do buffer cache: manter os blocos de dados mais recentemente solicitados em memória, evitando desta forma releituras físicas de um mesmo bloco de dados.
Os buffers caches utilizam dois algoritmos de lista para organizar os dados: a lista de gravação

(write list) e a lista dos dados usados mais recentemente, ou LRU (Least Recently Used).

A lista de gravação (Write List) mantém os buffers sujos, que contêm os dados que foram modificados, mas que ainda não foram gravados permanentemente no disco. Para alocar novos blocos de dados no buffer cache, a Oracle utiliza o algoritmo LRU, que remove os blocos de dados mais antigos da área de buffer e insere os novos blocos de dados solicitados.
O parâmetro de inicialização DB_CACHE_SIZE (anteriormente db_block_buffers) governa o tamanho da região do cache do buffer de dados RAM. A Oracle possui o utilitário v$db_cache_advice para determinar o benefício marginal (em termos de redução de leituras de disco), quando adicionamos mais cache de dados.
O tamanho de cada bloco no Database Buffer Cache é especificado pelo parâmetroDB_CACHE_SIZE. Para visualizar o tamanho atual do Cache de Buffer, utilize o comando
SHOW
PARAMETER DB_CASH_SIZE ou SHOW SGA. O valor do DB_CACHE_SIZE deve ser pelo menos 4M *
número de CPUs (valores menores são automaticamente arredondados para esse valor).

Um valor especificado pelo usuário maior do que isso é arredondado para o tamanho mais próximo. Um valor de zero é ilegal porque é necessário para um pool de memória padrão do tamanho do bloco primário, que é o tamanho do bloco usado para a tablespace SYSTEM.
A partir do Oracle 9i, é possível adicionar dois caches auxiliares que alocam memória independente dos outros caches na SGA: o Pool de Buffers KEEP e o Pool de Buffers RECYCLE. Ambos funcionam como o cache principal. A sintaxe para usar esse tipo de buffer é a seguinte:
BUFFER_POOL { KEEP | RECYCLE | DEFAULT }

CREATE TABLE table_name (coll number) STORAGE (BUFFER_POOL KEEP;

ALTER INDEX index_name STORAGE (BUFFER_POOL RECYCLE;

Buffer de Redo Log

O buffer de redo log armazena entradas de registros de redo - um log das alterações feitas ao banco de dados. As entradas de redo armazenadas nos buffers de log de redo são gravadas em um log de redo on-line, que é usado se a recuperação do banco de dados for necessária.O tamanho do log de redo é estático.
No momento em que uma instrução DML atualiza uma determinada tabela, imagens de redo são criadas e armazenados no buffer de redo log.
O buffer de redo log registra o bloco que foi alterado, o local da alteração e o novo valor em uma entrada de redo nos arquivos de redo log, pois, se necessário, serão utilizados para a recuperação do banco de dados. Além disso, as alterações efetuadas por uma transação podem ser intercaladas com alterações realizadas por outras transações.
Por sua vez, os registros de redo são armazenados em uma forma circular no redo log buffer,sendo reutilizados depois que o redo log buffer é preenchido. Estes são gravados em um dos arquivos de redo log pelo processo de segundo plano LGWR (Log Writer) nas seguintes situações:sempre que uma transação for confirmada, a cada três segundos, ou quando o redo log buffer atingir o tamanho de 1MB.
Um de seus principais objetivos é permitir refazer uma determinada transação que possa ter sofrido alguma falha e, assim, proteger o banco de dados de alguma falha da instância.
Seu tamanho em bytes é definido pelo parâmetro LOG_BUFFER. Para visualizar o tamanho atual do Redo Log, utilize o comando SHOW PARAMETER LOG_BUFFER ou SHOW SGA.
Shared Pool

O pool compartilhado contém construções de memória compartilhada, como as áreas de SQL
compartilhadas. É uma área de memória constituída por dois subcaches principais: o cache de biblioteca (Library Cache), utilizado para armazenar os comandos SQL e PL/SQLexecutados recentemente no banco de dados; e o cache de dicionário de dados (Data DictionaryCache), que armazena um subconjunto de colunas dastabelas do dicionário de dados, após serem lidos no buffer cache.
A área SQL compartilhada é necessária para processar cada instrução SQL original submetida ao banco de dados. Ela contém informações como a árvore de análise e o plano de execução para a instrução correspondente. Uma única área de SQL compartilhada é usada por vários aplicativos que emitem a mesma declaração, deixando livre uma quantidade maior de memória compartilhada para outros usos.
Estes comandos SQL podem ser solicitados por processos do usuário ou, no caso de stored procedures, lidos do dicionário de dados. O shared pool é dimensionado pelo parâmetro de inicialização SHARED_POOL_SIZE. Para visualizar o tamanho atual da Shared Pool,utilize o comando SHOW PARAMETER SHARED_POOL_SIZE.
Statement handles ou cursores

Um cursor é um identificador ou nome para uma área particular do código SQL, em que uma declaração e outras informações para o processamento da declaração são mantidas. (OracleCall
Interface, OCI, refere-se a estes como alças de instrução ou statement handles). Embora a maioria dos usuários Oracle dependa de manipulação automática do cursor de utilitários da Oracle, as interfaces de programação de aplicações oferecem aos designers mais controle sobre cursores.
Por exemplo, no desenvolvimento de um aplicativo pré-compilador, um cursor é um recurso nomeado disponível, podendo ser usado, especificamente, para analisar instruções SQLembutidas dentro de um aplicativo. Os desenvolvedores de aplicativos podem codificar um aplicativo que controla as fases de execução da instrução SQL e, portanto, melhorar o desempenho do aplicativo.
Programa Global Area

A Área de Programa Global (PGA) é um buffer de memória que contém os dados e informações de controle para um processo servidor. A PGA é criada pelo Oracle quando um processo do servidor é iniciado. As informações em uma PGA dependem da configuração do Oracle.
A PGA é uma memória não compartilhada (Non-Shared Memory) criada e alocada quando um novo processo é inicializado no servidor, contendo uma área de memória para cada usuário ativo na instância. Dentro da PGA, existem três estruturas: uma contendo um espaço para a pilha(para armazenar as variáveis e matrizes), outra contendo dados sobre a sessão do usuário e uma terceira com as informações dos cursores usados.
Para especificar a quantidade máxima de memória disponível à área de PGA, é utilizado o parâmetro de inicialização PGA_AGGREGATE_TARGET.
User Global Area

A Área Global do Usuário (UGA) é a memória associada a uma sessão de usuário. Nesta sessão,
a memória é alocada para as variáveis de sessão, como informações de logon e outras informações exigidas por uma sessão de banco de dados. Essencialmente, a UGA armazena o estado da sessão.A figura que descreve a UGA pode ser vista abaixo:

UGA

4. Ano: 2017 Banca: FGV Órgão: Alerj Cargo: Analista de Tecnologia da Informação Q. 46

Quando uma instância é iniciada, o SGBD Oracle llg aloca uma área de memória e inicia processos de background. A memória alocada para variáveis de sessão, como informações de logon e outras informações necessárias por uma sessão do banco de dados, é a:
(A) Reserved Pool;

(B) Data Dictionary Cache;

(C) User Global Area;

(D) Java Pool;

(E) Database Buffer Cache

Comentário: Vejam que o comentário anterior está diretamente associado ao texto do enunciado. Sendo assim, podemos concluir que nossa resposta está na alternativa C.
Gabarito: C

Um servidor de banco de dados Oracle consiste em um banco de dados Oracle e uma instânciaOracle. Cada vez que um banco de dados for iniciado, a área global de sistema
(SGA-System global area) é alocada e processos da Oracle de background são iniciados. A combinação dos processos em segundo plano com os buffers de memória é chamada de instância Oracle.
Algumas arquiteturas de hardware (por exemplo, sistemas de disco compartilhados) permitem que vários computadores possam compartilhar o acesso aos dados, ao software ou a dispositivos periféricos. O Real Application Clusters (RAC) tira proveito de tal arquitetura, executando várias instâncias que compartilham um único banco de dados físico. Na maioria das aplicações,o RAC
permite o acesso a um único banco de dados por usuários em vários computadores com melhor desempenho.
1. BANCA: CESPE ANO: 2013 ÓRGÃO: TRT - 8? REGIÃO (PA E AP) PROVA: ANALISTA JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

A respeito do sistema de gerenciamento de banco de dados Oracle, versão llg, assinale a opção correta. Nesse sentido, considere que a sigla RAC, sempre que utilizada,refere-se a Real
Application Clusters.

A PGA (Program Global Area) é um grupo de estruturas de memória compartilhada pelos usuários da instância Oracle. Quando uma instância Oracle é iniciada, a memória é alocada para a PGA com base nos valores especificados no arquivo de parâmetros de inicialização.
B O processo Log Writer executa a recuperação de falhas, aplicando as entradas dos arquivos de redo log online aos arquivos de dados.
C Um servidor Oracle é composto de duas entidades: a instância e o banco de dados. O
banco de dados é aberto durante o processo de inicialização e, depois, a instância é iniciada.
D Oracle Enterprise Manager Grid Control é uma ferramenta gráfica para gerenciar um banco de dados, que pode ser um banco de dados em cluster, com a funcionalidade de RAC ao passo que o Grid Control dispõe de recursos para gerenciamento e monitoramento em tempo real,para executar tarefas agendadas, como operações de backup e para reportar condições de alerta interativamente e por email.
E Por meio do recurso RAC, é possível que mais de uma instância, em servidores separados, acesse os mesmos arquivos de dados. Para implementar o RAC, o banco de dados compartilhado deve estar armazenado em um subsistema de discos com RAID ativado para garantir que cada componente do sistema de armazenamento seja tolerante a falhas.
Comentário: Vamos comentar cada uma das alternativas acima:

Na alternativa A, temos uma troca entre os conceitos de SGA e PGA. Lembrem-se que SGA
(SYSTEM GLOBAL AREA) refere-se à área de memória compartilhada. Já o PGA (PROGRAM

GLOBAL AREA) trata da área de memória não compartilhada, ou seja, um PGA é alocado para cada processo.
Já a alternativa B expõe o LGWR (Log Writer), que é responsável pelo gerenciamento do buffer do log de redo. Uma transação só é considerada completa ou efetivada quando o LGWRgrava com sucesso as informações do redo.
Para responder a alternativa C, temos que ter em mente que um servidor Oracle é composto por duas entidades: a instância e o banco de dados. A primeira possui as estruturas de memória e os processos. Durante o processo de inicialização, a instância é inicializada(started)
e o banco de dados é aberto (open).

O ORACLE ENTERPRISE MANAGER DATABASE CONTROL é uma ferramenta gráfica para gerenciar bancos de dados, que pode ser definido como um banco de dados isolado ou um cluster, com a funcionalidade de RAC. Por outro lado, o GRID CONTROL dispõe de recursos para gerenciamento e monitoramento em tempo real, para executar tarefas agendadas,como operações de backup e para reportar condições de alerta interativamente e por e-mail.
Vejam que pelas explicações teóricas elencadas até aqui, não nos resta muita opção. A resposta está presente alternativa E. Não precisamos de muito conhecimento sobre RAC para resolver a questão. Apenas a definição é suficiente para marcarmos a alternativa correta.Vejamos alguns pontos importantes sobre RAC:
O Oracle Real Application Clusters (RAC) é uma opção do Banco de dados Oracle introduzida pela primeira vez com o Oracle 9i. O Oracle RAC fornece opções para dimensionar aplicações,além da capacidade de um único servidor. Isso permite que os clientes tirem proveito de hardwares padronizados de baixo custo para reduzir seu custo total de propriedade e para fornecer um ambiente de computação redimensionável que suporte a carga de trabalho de suas aplicações.
O Oracle RAC permite que o Banco de dados Oracle execute todos os tipos de aplicações i corporativas de base em clusters, incluindo produtos empacotados (conhecidos como o OracleApplications, Peoplesoft, SAP), aplicações desenvolvidas internamente, que podem ser OLTP,
DSS ou uma carga de trabalho mista. Assim, podemos marcar o gabarito na alternativa E.

Gabarito: E

Um servidor de banco de dados Oracle usa estruturas de memória e processos para gerenciar e acessar o banco de dados. Todas as estruturas de memória principal existem na memória dos computadores que constituem o sistema de base de dados. Os processos são postos de trabalho(Jobs) que funcionam na memória desses computadores.

O Oracle cria e usa estruturas de memória para completar ou executar vários jobs. Por exemplo, a memória armazena o código do programa que está sendo executado e os dados compartilhados entre os usuários. Duas estruturas de memória básicas são associadas com a Oracle:Área global de sistema (SGA - system global area) e área global do programa (PGA -
program global area). Abaixo explicaremos cada uma delas em detalhes. Antes vejam as estruturas descritas na figura:
System Global Area (SGA)

System Global Area (SGA) é uma região de memória compartilhada que contém os dados e informações de controle para uma instância Oracle. O Oracle aloca a SGA quando uma instância é iniciada e desaloca quando a instância é finalizada. Cada instância tem seu próprio SGA.
Usuários conectados a um banco de dados Oracle compartilham os dados da SGA. Para um desempenho ideal, a SGA deve sertão grande quanto possível (enquanto houver espaço na memória real) para armazenar os dados em memória e minimizar operações de l/O no disco.
Por ser uma área de memória em modo de leitura e gravação, todos os processos de segundo plano e processos servidores do banco de dados executados em nome dos usuários terão permissão para ler ou gravar blocos de dados dentro da instância da SGA.
O Oracle permite, por ser uma memória dinâmica, que o tamanho da SGA seja ajustado em tempo de execução, sem a necessidade de baixar ou indisponibilizar o ambiente de banco de dados.
A memória para a SGA é alocada em unidades granulares, onde um grão pode ter 4MB ou
16MB. Se a SGA for menor ou igual a 128MB, o crescimento será de 4MB. Do contrário,
o aumento será de 16MB.
A quantidade total de memória alocada para a SGA é definida pelo parâmetro
SGA_MAX_SIZE.
Se o parâmetro SGA_MAX_SIZE, especificado no arquivo de parâmetros de inicialização,
apresentar um valor menor do que a soma de todos os valores especificados dos demais componentes da SGA,no momento da inicialização, a configuração no arquivo de parâmetros de inicialização será ignorada.
Para visualizar o tamanho atual da SGA, utilize o comando SHOW SGA. Nas seções subsequentes, iremos discutir as áreas que constituem a SGA. As informações armazenadas na SGAsão divididas em vários tipos de estruturas de memória, incluindo os buffers de banco de dados,redo log buffer e a shared pool.

Database Buffer Cache

O cache do buffer do banco de dados, também chamado de cache do buffer, é a área de memória que armazena cópias de blocos de dados lidos a partir de arquivos de dados.
Um buffer é um endereço de memória principal, no qual o gerenciador de buffer armazena temporariamente um bloco de dados recentemente usado. Todos os usuários conectados simultaneamente a uma instância de banco de dados compartilham o acesso ao mesmo cache do buffer.
O cache de buffer contém blocos de dados modificados, bem como blocos não modificados.
Como os dados mais recentemente (e, muitas vezes, o mais frequentemente) usados são mantidos na memória, menos operações de l/O em disco são necessárias, e o desempenho é melhorado.
Os blocos de dados, preservados no Buffer Cache, podem adquirir três tipos de estados:

* Buffers sujos (Dirty Buffers)

* Buffers livres (Free Buffers)

* Buffers fixados (Pinned Buffers).

Buffers sujos contêm blocos de dados alterados ou acrescentados, devido a uma instrução
DML, que ainda não foram submetidos a commit. Esse buffer não pode ser reutilizado até que estes blocos de dados sejam gravados com êxito no disco.
Buffers livres são buffers que não possuem dados armazenados ou que guardam blocos de dados que são idênticos aos blocos correspondentes no disco. Áreas de buffers livres podem ser substituídas em uma operação de leitura do disco a qualquer momento.
Buffers fixados são buffers que estão em uso por comandos DML ou são explicitamente salvos para uso futuro e, portanto, não podem ser utilizados por outras transações.
No momento em que uma consulta é processada, é realizada uma varredura no buffer cache pelos blocos solicitados. Se o bloco não for localizado em memória, será efetuada uma leitura física do bloco no arquivo de dados em disco e enviada uma cópia dos blocos necessários para o BufferCache. Esta é uma das principais funções do buffer cache: manter os blocos de dados mais recentemente solicitados em memória, evitando desta forma releituras físicas de um mesmo bloco de dados.
Os buffers caches utilizam dois algoritmos de lista para organizar os dados: a lista de gravação

(write list) e a lista dos dados usados mais recentemente, ou LRU (Least Recently Used).

A lista de gravação (Write List) mantém os buffers sujos, que contêm os dados que foram modificados, mas que ainda não foram gravados permanentemente no disco. Para alocar novos blocos de dados no buffer cache, a Oracle utiliza o algoritmo LRU, que remove os blocos de dados mais antigos da área de buffer e insere os novos blocos de dados solicitados.
O parâmetro de inicialização DB_CACHE_SIZE (anteriormente db_block_buffers) governa o tamanho da região do cache do buffer de dados RAM. A Oracle possui o utilitário v$db_cache_advice para determinar o benefício marginal (em termos de redução de leituras de disco), quando adicionamos mais cache de dados.
O tamanho de cada bloco no Database Buffer Cache é especificado pelo parâmetroDB_CACHE_SIZE. Para visualizar o tamanho atual do Cache de Buffer, utilize o comando
SHOW
PARAMETER DB_CASH_SIZE ou SHOW SGA. O valor do DB_CACHE_SIZE deve ser pelo menos 4M *
número de CPUs (valores menores são automaticamente arredondados para esse valor).

Um valor especificado pelo usuário maior do que isso é arredondado para o tamanho mais próximo. Um valor de zero é ilegal porque é necessário para um pool de memória padrão do tamanho do bloco primário, que é o tamanho do bloco usado para a tablespace SYSTEM.
A partir do Oracle 9i, é possível adicionar dois caches auxiliares que alocam memória independente dos outros caches na SGA: o Pool de Buffers KEEP e o Pool de Buffers RECYCLE. Ambos funcionam como o cache principal. A sintaxe para usar esse tipo de buffer é a seguinte:
BUFFER_POOL { KEEP | RECYCLE | DEFAULT }

CREATE TABLE table_name (coll number) STORAGE (BUFFER_POOL KEEP;

ALTER INDEX index_name STORAGE (BUFFER_POOL RECYCLE;

Buffer de Redo Log

O buffer de redo log armazena entradas de registros de redo - um log das alterações feitas ao banco de dados. As entradas de redo armazenadas nos buffers de log de redo são gravadas em um log de redo on-line, que é usado se a recuperação do banco de dados for necessária.O tamanho do log de redo é estático.
No momento em que uma instrução DML atualiza uma determinada tabela, imagens de redo são criadas e armazenados no buffer de redo log.
O buffer de redo log registra o bloco que foi alterado, o local da alteração e o novo valor em uma entrada de redo nos arquivos de redo log, pois, se necessário, serão utilizados para a recuperação do banco de dados. Além disso, as alterações efetuadas por uma transação podem ser intercaladas com alterações realizadas por outras transações.
Por sua vez, os registros de redo são armazenados em uma forma circular no redo log buffer,sendo reutilizados depois que o redo log buffer é preenchido. Estes são gravados em um dos arquivos de redo log pelo processo de segundo plano LGWR (Log Writer) nas seguintes situações:sempre que uma transação for confirmada, a cada três segundos, ou quando o redo log buffer atingir o tamanho de 1MB.
Um de seus principais objetivos é permitir refazer uma determinada transação que possa ter sofrido alguma falha e, assim, proteger o banco de dados de alguma falha da instância.
Seu tamanho em bytes é definido pelo parâmetro LOG_BUFFER. Para visualizar o tamanho atual do Redo Log, utilize o comando SHOW PARAMETER LOG_BUFFER ou SHOW SGA.
Shared Pool

O pool compartilhado contém construções de memória compartilhada, como as áreas de SQL
compartilhadas. É uma área de memória constituída por dois subcaches principais: o cache de biblioteca (Library Cache), utilizado para armazenar os comandos SQL e PL/SQLexecutados recentemente no banco de dados; e o cache de dicionário de dados (Data DictionaryCache), que armazena um subconjunto de colunas dastabelas do dicionário de dados, após serem lidos no buffer cache.
A área SQL compartilhada é necessária para processar cada instrução SQL original submetida ao banco de dados. Ela contém informações como a árvore de análise e o plano de execução para a instrução correspondente. Uma única área de SQL compartilhada é usada por vários aplicativos que emitem a mesma declaração, deixando livre uma quantidade maior de memória compartilhada para outros usos.
Estes comandos SQL podem ser solicitados por processos do usuário ou, no caso de stored procedures, lidos do dicionário de dados. O shared pool é dimensionado pelo parâmetro de inicialização SHARED_POOL_SIZE. Para visualizar o tamanho atual da Shared Pool,utilize o comando SHOW PARAMETER SHARED_POOL_SIZE.
Statement handles ou cursores

Um cursor é um identificador ou nome para uma área particular do código SQL, em que uma declaração e outras informações para o processamento da declaração são mantidas. (OracleCall
Interface, OCI, refere-se a estes como alças de instrução ou statement handles). Embora a maioria dos usuários Oracle dependa de manipulação automática do cursor de utilitários da Oracle, as interfaces de programação de aplicações oferecem aos designers mais controle sobre cursores.
Por exemplo, no desenvolvimento de um aplicativo pré-compilador, um cursor é um recurso nomeado disponível, podendo ser usado, especificamente, para analisar instruções SQLembutidas dentro de um aplicativo. Os desenvolvedores de aplicativos podem codificar um aplicativo que controla as fases de execução da instrução SQL e, portanto, melhorar o desempenho do aplicativo.
Programa Global Area

A Área de Programa Global (PGA) é um buffer de memória que contém os dados e informações de controle para um processo servidor. A PGA é criada pelo Oracle quando um processo do servidor é iniciado. As informações em uma PGA dependem da configuração do Oracle.
A PGA é uma memória não compartilhada (Non-Shared Memory) criada e alocada quando um novo processo é inicializado no servidor, contendo uma área de memória para cada usuário ativo na instância. Dentro da PGA, existem três estruturas: uma contendo um espaço para a pilha(para armazenar as variáveis e matrizes), outra contendo dados sobre a sessão do usuário e uma terceira com as informações dos cursores usados.
Para especificar a quantidade máxima de memória disponível à área de PGA, é utilizado o parâmetro de inicialização PGA_AGGREGATE_TARGET.
User Global Area

A Área Global do Usuário (UGA) é a memória associada a uma sessão de usuário. Nesta sessão,
a memória é alocada para as variáveis de sessão, como informações de logon e outras informações exigidas por uma sessão de banco de dados. Essencialmente, a UGA armazena o estado da sessão.A figura que descreve a UGA pode ser vista abaixo:

UGA

2. Ano: 2017 Banca: FGV Órgão: Alerj Cargo: Analista de Tecnologia da Informação Q. 46

Quando uma instância é iniciada, o SGBD Oracle llg aloca uma área de memória e inicia processos de background. A memória alocada para variáveis de sessão, como informações de logon e outras informações necessárias por uma sessão do banco de dados, é a:
(A) Reserved Pool;

(B) Data Dictionary Cache;

(C) User Global Area;

(D) Java Pool;

(E) Database Buffer Cache

Comentário: Vejam que o comentário anterior está diretamente associado ao texto do enunciado. Sendo assim, podemos concluir que nossa resposta está na alternativa C.
Gabarito: C

ESTRUTURA DE PRoCESSoS

Todos os usuários conectados ao banco de dados Oracle devem executar dois módulos de código para acessar uma instância de banco de dados Oracle.
1. Aplicação ou ferramenta Oracle: Um usuário de banco de dados executa uma aplicação de banco de dados (como um programa de pré-compilador) ou uma ferramenta Oracle (como oSQL *
Plus), que emite instruções SQL para um banco de dados Oracle.

2. Código do servidor de banco de dados Oracle: Cada usuário tem algum código de banco de dados Oracle em execução em seu nome, que interpreta e processa instruções SQL do aplicativo.
Estes módulos de código são executados por processos. Um processo é um
"thread de controle" ou um mecanismo em que um sistema operacional que pode executar uma série de passos(alguns sistemas operacionais usam os termos job ou tarefa). Um processo, normalmente,
tem a sua própria área privada de memória na qual ele é executado.
O Multiple-process Oracle (também chamado de multiusuário Oracle) usa vários processos para executar diferentes partes do código da Oracle e processos adicionais para os usuários - um processo para cada usuário conectado ou um ou mais processos compartilhados por vários usuários.A maioria dos sistemas de banco de dados é multiusuário, porque um dos principais benefícios de um banco de dados é a gestão de dados por diferentes usuários ao mesmo tempo.
Cada processo em uma instância Oracle Database realiza um trabalho específico. Ao dividir o trabalho do Oracle e das aplicações de banco de dados em vários processos, vários usuários e aplicativos podem se conectar a uma única instância de banco de dados,simultaneamente,
enquanto o sistema mantém um excelente desempenho.

TIPoS DE PRoCESSoS

Os processos em um sistema de banco de dados Oracle podem ser classificados em dois grandes grupos:
1. Processos de usuário que executam o aplicativo ou ferramenta de código Oracle.

2. Processos de banco de dados Oracle que executam o código do servidor de banco de dadosOracle. Eles incluem os processos do servidor e os processos em segundo plano.

A estrutura do processo varia para diferentes configurações de banco de dados
Oracle,
dependendo do sistema operacional e das escolhas de opções do SGBD Oracle. O código para usuários conectados pode ser configurado como um servidor dedicado ou um servidor compartilhado.
Com o servidor dedicado, para cada usuário, o aplicativo de banco de dados é executado por um processo diferente (um processo de usuário) do que aquele que executa o código do servidor de banco de dados Oracle (um processo servidor dedicado).
Com o servidor compartilhado, o aplicativo de banco de dados é executado por um processo diferente (um processo de usuário) do que aquele que executa o código do servidor de banco de dados Oracle. Cada processo servidor que executa o código do servidor de banco de dados Oracle(um processo de servidor compartilhado) pode servir a múltiplos processos de usuário.

A figura ilustra uma configuração de servidor dedicado. Cada usuário conectado tem um processo de usuário separado, e vários processos em segundo plano do OracleDatabase executando. A figura pode representar vários usuários simultâneos executando um aplicativo no mesmo computador que o banco de dados Oracle. Esta configuração particular,geralmente, é executada em um mainframe ou em um minicomputador.
User Use- -ser User
-ser t I I t r A
System Global Area
(SGA)

I I

Recoverer
(RECO)

Process
Monitor
(PMON)

Systern
Monitor
(SMON)

Database
Wnter
(DBWO)

Log
Writer
(LGWR)

Archiver
(ARCO)

Oracle
Processes
(background processes)
PRoCESSoS Do USUÁRIo

Agora vamos tratar dos processos do usuário. Quando um usuário executa um aplicativo,
como um programa Pro*C ou SQL*Plus, o sistema operacional cria um processo cliente (às vezes chamado de um processo de usuário) para executar o aplicativo. O aplicativo cliente tem bibliotecas do OracleDatabase ligadas nele, que fornecem as APIs necessárias para se comunicar com o banco de dados.

Processos do cliente diferem em vários aspectos dos processos do Oracle. Eles interagem diretamente com a instância. Os processos do Oracle servem ao processo cliente, pois podem ler e escrever na SGA, ao passo que o processo do cliente não pode. Um processo cliente pode ser executado em um host diferente do host do banco, enquanto o processo do Oracle não pode.
Por exemplo, suponha que um usuário em uma máquina cliente inicia o SQL * Plus e se conecta,
através da rede, ao banco de dados concursos em um host diferente (a instância de banco de dados não é iniciada):
SQL> CONNECT SYS@instl AS SYSDBA

Enter password: *********
Connected to an idle instance.

Observem que uma sessão foi estabelecida, bem como o processo do cliente sqlplus está rodando no lado do host. Conexão e sessão estão intimamente relacionadas ao processo de usuário,mas são muito diferentes em significado.

HORA DE

PRATICAR!

(Ministério da Economia - Infraestrutura - 2020) Com relação ao sistema gerenciador de banco de dados Oracle, julgue o próximo item.
94 No utilitário SQLPlus, o uso do comando CONNECT teste/teste AS SYSDBA permite a conexão ao Oracle com direitos administrativos capazes de iniciar uma instância de banco de dados, considerando-se que, nesse comando, teste define usuário e senha.
Comentários: Você pode fazer login e conectar como SYSDBA usando apenas a linha de comando SQL (SQL
* Plus). Você pode fazer isso fornecendo um nome de usuário e a senha SYS ou usando a autenticação do sistema operacional (SO).
Existem três privilégios específicos de sistema que dão aos administradores uma autenticação especial no banco de dados:SYSDBA, SYSOPER e SYSASM.

Um administrador com privilégio SYSOPER pode inicializar e efetuar shutdown no banco de dados,
entre outras tarefas.

O privilégio SYSDBA contém todos os direitos do SYSOPER, além de ser capaz de criar um banco de dados e conceder privilégiosSYSDBA ou SYSOPER a outros usuários daquele.

Para conectar-se ao banco de dados a partir de uma sessão SQL*Plus, acrescebt AS SYSDBA ou AS
SYSOPER ao seu comando

CONNECT. Vejamos um exemplo:

CONNECT SYS/password AS SYSDBA

Gabarito Certo.

Uma conexão é um canal de comunicação entre um processo de usuário e uma instância de banco de dados Oracle. É estabelecida utilizando os mecanismos de comunicação entre processos disponíveis (em um computador que roda tanto o processo do usuário quanto o banco de dadosOracle) ou um software de rede (quando diferentes computadores executam o aplicativo e o banco de dados Oracle, e precisam se comunicar através de uma rede).
Uma sessão é uma conexão específica de um usuário com uma instância Oracle Database,
através de um processo de usuário. Por exemplo, quando um usuário inicia o SQL *
Plus, o usuário deve fornecer um nome de usuário e senha válidos e, em seguida, uma sessão é estabelecida para esse usuário. Uma sessão dura desde o momento em que o usuário se conecta até o momento em que o usuário desconecta ou sai do aplicativo de banco de dados.
Várias sessões podem ser criadas e podem existir, simultaneamente, para um único usuário banco de dados Oracle usando o mesmo nome de usuário. Por exemplo, um usuário com o nome de usuário/senha de Thiago/12345 pode se conectar à mesma instância do Oracle várias vezes.
Em configurações sem o servidor compartilhado, o Oracle Database cria um processo de servidor em nome de cada sessão do usuário. No entanto, com o servidor compartilhado,muitas sessões de usuários podem compartilhar um único processo do servidor. Veja na figura abaixo um exemplo de conexão e sessão:
Esta seção descreve os dois tipos de processos que executam o código do servidor de banco de dados Oracle (os processos do servidor e os processos em segundo plano). Vamos descrever também os arquivos de trace e os logs de alerta, que armazenam os eventos de banco de dados para os processos de banco de dados Oracle.
Processos do Servidor

O Oracle Database cria processos do servidor para lidar com os pedidos dos processos de usuários conectados à instância. Em algumas situações, quando a aplicação e o banco de dadosOracle operam no mesmo computador, é possível combinar o processo do usuário e o processo de servidor correspondente em um único processo para reduzir a sobrecarga do sistema. No entanto,quando a aplicação e o banco operam em computadores diferentes, um processo do usuário sempre se comunica com o Oracle através de um processo servidor separado.
Processos do servidor (ou a parte do servidor de processos de usuário/servidor combinados)criados em nome de uma aplicação de usuário podem executar um ou mais dos seguintes procedimentos:
1. Analisar e executar instruções SQL emitidas através da aplicação.

2. Ler blocos de dados necessários a partir de arquivos de dados em disco para os buffers de dados partilhada da SGA, se os blocos já não estão presentes na SGA.
3. Retornar os resultados de tal maneira que a aplicação possa processar as informações.

Processos de segundo plano

Um banco de dados Oracle usa alguns processos adicionais chamados processos em segundo plano. Eles executam tarefas de manutenção necessárias ao funcionamento da base de dados e para maximizar o desempenho para os vários usuários.
Cada processo de background tem uma tarefa específica, mas pode trabalhar em conjunto com os outros processos. Por exemplo, o processo LGWR grava os dados do buffer de log de redo para o log de redo online. Quando um arquivo de log está pronto para ser arquivado, LGWRsinaliza para outro processo arquivar os dados.
O Oracle Database cria processos de segundo plano automaticamente quando uma instância de banco de dados é inicializada. Uma instância pode ter muitos processos em segundo plano, alguns
0515200190-0E-vEevrteorntoMn uMriulorilVoieViireaira dos quais nem sempre existem em cada configuração do banco de dados. A consulta a seguir lista os processos em segundo plano em execução no seu banco de dados:
SELECT PNAME
FROM V$PROCESS

WHERE PNAME IS NOT NULL
ORDER BY PNAME;

Processos de segundo plano obrigatórios

Os processos de segundo plano obrigatórios estão presentes em todas as configurações de banco de dados típicos. Estes processos são executados por padrão em uma instância de banco de dados iniciada com um arquivo de parâmetros de inicialização minimamente configurado.Abaixo vamos descrever os seguintes processos de fundo obrigatórios: Process Monitor Process(PMON),
System Monitor Process (SMON), Database Writer Process (DBWn), Log Writer Process (LGWR),
Checkpoint Process (CKPT), Manageability Monitor Processes (MMON and MMNL) e
Recoverer
Process (RECO). Vejam a organização deles na arquitetura do Oracle na figura a seguir.

Antes, porém, vejamos a questão abaixo:

1. BANCA: FCC ANO: 2009 ÓRGÃO: TRT - 15^ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

NÃO é um processo do tipo background contido em uma instância Oracle:
A system monitor process.

B checkpoint process.
C archiver process.

D server process.

E recoverer process.

Comentário: Vimos anteriormente que o server process não é um processo classificado como de segundo plano. Utilizando o texto acima, podemos associar,respectivamente, as alternativas A, B e E às siglas: SMON, CKPT, e RECO. Falta ainda tratar do processo de Archiver,que não é um processo de segundo plano obrigatório, como os que vimos até aqui. Ele será visto a seguir em detalhes, mas podemos adiantar que ele é classificado como OPCIONAL e sua sigla é ARCO. Podemos observar sua presença na figura a seguir.
Gabarito: D

RECO PMON SMON

l í l

System Global Area

Data ba se
Buffer Cache

Redo Log
Buffer

User
Process

Shared
Server
Process

J

Dedicated
Server
Process

User Process es

CKPT

ARCO

Offllne x StorageDevice

DBWO

LGWR

Legend:

RECO
PMON
SMON
CKPT
ARCO
DBWO
LGWR
DOOO

Recoverer process
Process monitor
System monitor
Checkpoint
Archiver

Database writer
Log writer
Dispatcher Process

Redo Log

Control

Process Monitor Process (PMON)

O Process Monitor ou PMON é um processo em segundo plano criado no momento em que a instância do banco de dados é inicializada. Ele disponibiliza recursos, se um dos processos do Oracle falhar. Por exemplo, se uma conexão de usuário cair, um processo do Oracle falhar ou ocorrer uma falha de hardware, o processo PMON aplica o rollback nas transações que estavam em andamento,remove os bloqueios nas linhas afetadas da tabela e exclui o processo desconectado da lista de processos ativos.
O PMON, normalmente, é executado a cada três segundos para efetuar atividades de limpeza.
Se o PMON não está sendo executado, a instância do banco de dados será encerrada.

Em um ambiente Linux, para identificar se o processo PMON está rodando, utilize o seguinte comando:
[oracle@XXXX ~]$ ps aux | grep pmon oracle 17011 0.0 0.0 60292 696 pts/O D+ 12:14 0:00 grep pmon
System Monitor Process (SMON)

O processo System Monitor verifica a consistência no banco de dados, localizando e validando o arquivo de controle no momento em que o banco é montado e, se necessário, inicia a recuperação do banco de dados quando ele é aberto. Além desta funcionalidade, o SMON é responsável por unir espaços livres nos tablespaces se eles forem gerenciados pelo dicionário.
Os arquivos de controle (Control Files) são arquivos físicos do sistema operacional responsáveis por armazenar informações necessárias para manter e verificar a integridade do banco de dados.Um banco de dados Oracle deve possuir, no mínimo, um arquivo de controle.

O SMON é o processo utilizado em circunstâncias como uma queda ou falha de sistema,
executando a recuperação de falhas e aplicando as entradas dos arquivos de redo log aos arquivos de dados. A sua principal função é abrir a conexão entre a instância e o banco de dados, além de realizar funções de monitoramento e organização.
É importante ressaltar que, ao ocorrer uma falha na instância Oracle, as informações contidas na área SGA que não foram gravadas em disco serão perdidas. Após a perda da instância, o processo de segundo plano SMON recupera automaticamente a instância quando o banco é reaberto.
O processo SMON deverá sempre ser mantido em execução para uma instância, caso contrário,a instância será encerrada.

Quando for necessária a recuperação de uma instância, o Oracle realizará as seguintes etapas através do SMON:
1. Executar rollforward para recuperar os dados que não foram registrados nos arquivos de dados, entretanto, que foram gravados no redo log online. Durante esse processo, oSMON lê os arquivos de redo log e aplica as alterações registradas nos blocos de dados;
2. Abrir o banco de dados para permitir que os usuários estabeleçam logon;

3. Submeter a rollback as transações não submetidas a commit.

Database Writer Process (DBWn)

O processo Database Writer é responsável por gravar os blocos de dados novos ou alterados do buffer cache do banco de dados nos arquivos de dados físicos (data files). Os data files, por sua vez, são arquivos físicos do sistema operacional que armazenam os dados do banco de dados propriamente ditos.
A gravação dos blocos de dados nos arquivos de dados é realizada de forma assíncrona e periódica. Tal evento ocorre nas seguintes condições: 1) quando um processo servidor realiza a leitura de um novo bloco para a memória e não existe espaço disponível no momento,ou ele está ocioso por alguns segundos; 2) quando o Oracle efetua um checkpoint do banco de dados ou da tablespace.
O DBWn é um processo servidor cuja principal função é gerenciar o database buffer cache,disponibilizando buffers quando solicitados e removendo os blocos de dados alterados da memória que ainda não foram salvos permanentemente. Isso tudo é feito em um esforço para reduzir a quantidade de leituras físicas e gravações em discos.
O processo DBWn utiliza o algoritmo LRU para descartar os blocos de dados menos utilizados recentemente do cache de buffer.
Log Writer Process (LGWR)

O processo LGWR é responsável por gerenciar o buffer de redo log, gravando as alterações registradas do buffer de redo log nos arquivos de redo log físicos (Redo log Files).Os redo log files armazenam as mudanças efetuadas no banco de dados para possibilitar a recuperação dos dados,em caso de falhas.

Este processo é continuamente executado na instância Oracle com as seguintes condições:
1)
quando uma transação recebe o commit (confirmação); 2) quando o buffer do redo log atingir 1 MBde espaço; 3) a cada três segundos, ou antes do processo DBWn escrever do buffer no data file.

O buffer de redo log é um buffer circular, logo, quando o LGWR grava entradas redo para um arquivo de redo log, os processos de servidor podem copiar novas entradas sobre as entradas no buffer de log redo que foram gravados no disco. Normalmente, o processo LGWR grava de forma otimizada os dados, garantindo, assim, que haverá espaço disponível no buffer para novas entradas,mesmo quando o acesso ao log redo estiver com uma carga alta.

É importante ressaltar que antes do processo DBWn escrever um bloco de dados do cash de buffer modificado no arquivo de dados, todos os registros de redo associados contendo alterações no redo buffer devem ser gravados no redo log files primeiramente.
Quando um usuário emite uma instrução COMMIT, o processo de servidor insere um registro de commit, junto com o SCN, no buffer de redo log.
Por conseguinte, o LGWR insere um registro de confirmação no buffer de redo log e escreve-o para o disco imediatamente, juntamente com as entradas de redo. Após esta etapa, o servidorOracle pode garantir que as alterações não serão perdidas mesmo que haja uma falha de instância.

Sempre que uma transação é submetida para commit, o servidor Oracle atribui um SCN(System Change Number, número de alteração do sistema) à transação. Ele é aproveitado pelo servidor Oracle para fornecer consistência de leitura, quando os dados forem recuperados dos arquivos de dados.
Os arquivos de redo log são arquivos físicos do sistema operacional que armazenam todas as alterações importantes realizadas no banco de dados para possibilitar a recuperação dos dados em caso de falhas na instância. Cada banco de dados deve conter ao menos dois arquivos de redo log,pois o Oracle utiliza-os de forma circular.

Checkpoint Process (CKPT)

O Checkpoint Process é responsável pela atualização do cabeçalho das informações de status do banco de dados nos arquivos de controle (Control Files) e nos arquivos de dados (Data Files)para refletir o último SCN (System Change Number).
Sempre que as alterações efetuadas no cache de buffer estão registradas no banco de dados de forma permanente, o processo CKPT informa ao processo DBWn o momento de gravar os dados em disco, auxiliando, assim, a reduzir a quantidade de tempo necessária para uma possível recuperação da instância.
O CKPT efetua, periodicamente, uma verificação (checkpoint) para se certificar de que todas as informações modificadas na memória estão armazenadas fisicamente no disco, sendo realizada nas seguintes condições:
* Quando ocorre um Log Switch. Um Log Switch (troca de log) acontece quando o Oracle troca de um redo log para outro. Enquanto isso, o servidor permanece gravando novas transações em outro grupo de log;
Durante um intervalo de tempo (definido no parâmetro LOG_CHECKPOINT_TIMEOUT do arquivo de parâmetros);
Quando acontece um shutdown;

* O DBA força um checkpoint;

* Quando a Tablespace é passada para Offline.

O processo de Checkpoint é habilitado através do parâmetro CHECKPOINT_PROCESS. Veja a figura abaixo com detalhes sobre o CKPT:
System Global Area
(SGA)

Database
Buffer Cache

Data File
Body

Manageability Monitor Processes (MMON and MMNL)

O processo monitor de gerenciamento (MMON) executa muitas tarefas relacionadas com o
Automatic Workload Repository (AWR). Por exemplo, o MMON escreve quando uma métrica viola seu valor limite e captura estatísticas para objetos SQL recentemente modificados.
O processo lite monitor de gerenciamento (MMNL) escreve estatísticas do buffer da Active
Session History (ASH) da SGA para o disco. MMNL escreve para o disco quando o buffer
ASH está cheio.
Recoverer Process (RECO)

Em um banco de dados distribuído, o processo de recuperação (RECO)
resolve automaticamente falhas em transações distribuídas. O processo RECO de um nó se conecta automaticamente a outros bancos de dados envolvidos em uma transação em dúvida. Quando oRECO restabelece uma conexão entre os bancos de dados, ele resolve automaticamente todas as transações em dúvida, removendo da tabela de transação pendente de cada banco de dados todas as linhas que correspondem às operações resolvidas.
2. BANCA: Cespe/2018 - Analista judiciário (STM)/ apoio especializado/ Análise de sistemas

Julgue o item que se segue, a respeito do processamento de transações e otimização de desempenho do SGBD e de consultas SQL.
No Oracle 12C, a Automatic Workload Repository (AWR) é uma funcionalidade similar ao autovacuum no Postgres 9.6, haja vista que ambos processam e mantêm estatísticas de desempenho para detecção de problemas e manutenção automática do banco de dados, por exemplo, reusando, ajustando e excluindo dados temporários e reusando espaço em blocos por linhas excluídas.
Certo
Errado

Comentário: Falamos sobre AWR e Autovacuum na nossa revisão para o concurso do STM. O
PostgreSQL e outros bancos de dados relacionais usam uma técnica chamada Multi-Version
Concurrency Control (MVCC) para manter o controle das transações. Uma penalidade de espaço surge quando usamos o MVCC, ela é conhecida como inchaço. O PostgreSQL precisa de ajuda de uma ferramenta externa chamada V ACU UM para poder limpar essa "sujeira".
As tabelas e os índices inchados não somente desperdiçam espaço, como também deixam as consultas mais lentas. Então, isso não é só uma questão de conseguir mais espaço no disco rígido. Antigamente, os DBAs precisavam executar o VACUUM manualmente. Hoje, é possível configurar um deamon chamado Autovacuum para executar essas limpezas em momentos oportunos.
Veja que Autovacuum não guarda nenhuma relação de similaridade funcional com o AWR.
Podemos afirmar, portanto, que a alternativa está incorreta. Sabemos que o AWR significa
Automatic Workload Repository, ou seja, é um repositório de informações a respeito da carga de trabalho do banco de dados. O framework do AWR coleta, processa e mantém estatísticas de desempenho para possibilitar detecção de problemas e é a base para as tarefas de tuning automáticas do Oracle. Estas estatísticas são coletadas, através de snapshots regulares,e armazenadas no AWR por um período definido. Elas são baseadas no momento do snapshot e podem ser utilizadas para elaborar um relatório. Os valores capturados pelo snapshot representam as mudanças em cada estatística coletada no período.
Gabarito: E

Processos de segundo plano opcionais

Um processo opcional é qualquer processo de background que não é definido como obrigatório. A maioria dos processos em segundo plano opcionais são específicos para tarefas ou recursos. Por exemplo, os processos de fundo que suportam o Oracle Streams AdvancedQueuing
(AQ) ou Oracle Automatic Storage Management (Oracle ASM) só estão disponíveis quando esses recursos estão ativados. Vamos descrever abaixo alguns processos desta categoria.
Archiver Processes (ARCn)

Os processos Archiver (ARCn) copiam arquivos do log de redo on-line para armazenamento off-line, após a mudança descrita no redo log ocorre. Esses processos também podem ainda coletar dados de redo para transação e transmiti-los para o modo de espera do banco de dados. Os processos ARCn existem somente quando o banco de dados está no modoARCHIVELOG e arquivamento automático está habilitado.
Job Queue Processes (CJQO and Jnnn)

O Oracle Database utiliza processos de fila de trabalho para executar tarefas do usuário, muitas vezes, em modo batch. Um trabalho é uma tarefa definida pelo usuário programada para ser executada uma ou mais vezes. Por exemplo, você pode usar uma fila de tarefas para agendar uma atualização em segundo plano. Dada uma data de início e um intervalo de tempo, a fila de tarefas processa a tarefa na próxima ocorrência do intervalo.
O Oracle Database gerencia processos de fila de trabalho dinamicamente, permitindo assim que os clientes possam adicionar mais trabalho, quando necessário. Os recursos do processo são liberados pelo banco de dados quando eles estão ociosos.
A fila de processos de trabalho dinâmica pode executar um grande número de jobs ao mesmo tempo em um determinado intervalo. A sequência de eventos é a seguinte:
1. O processo de coordenador de trabalho (CJQO) é automaticamente iniciado e interrompido quando necessário pelo Oracle Scheduler. O processo coordenador seleciona periodicamente trabalhos que precisam ser executados a partir de uma tabela de sistemas denominadaJOB$. Os trabalhos selecionados são ordenados, de acordo com o tempo.
2. O processo de coordenador cria dinamicamente processos escravos (Jnnn) para executar a fila trabalho (Jobs queue).
3. O processo da fila de trabalho executa um dos trabalhos que foi selecionado pelo processoCJQO para execução. Cada processo da fila de trabalho é executado até a conclusão.

4. Depois de terminar o processo de execução de cada trabalho, ele procura por mais jobs. Se não há trabalhos agendados para execução, ele entra em um estado de sleep, do qual ele acorda em intervalos periódicos e pesquisa por mais trabalhos. Se o processo não encontrar quaisquer novos jobs, ele termina após um intervalo pré-definido.
O parâmetro de inicialização JOB_QUEUE_PROCESSES representa o número máximo de processos na fila de trabalhos que podem ser executados concorrentemente em uma instância. No entanto, os clientes não devem assumir que todos os processos da fila de trabalho estão disponíveis para a execução.
Flashback Data Archiver Process (FBDA)

O processo arquivador de dados de flashback (FBDA) arquiva históricos de linhas de tabelas monitoradas em Arquivos de Dados de Flashback. Quando uma transação contendo DML em uma tabela controlada sofre commit, este processo armazena a pré-imagem das linhas para oFlashback
Data Archive. Além disso, mantém os metadados sobre as linhas.

O FBDA gerencia automaticamente o arquivo de dados de flashback em relação ao espaço,
à organização e à retenção. Além disso, o processo mantém o controle de quão longe o arquivamento de transações controladas ocorreu.
Space Management Coordinator Process (SMCO)

O processo de SMCO coordena a execução de diversas tarefas relacionadas ao gerenciamento de espaço, tais como a alocação de espaço proativo e a recuperação de espaço. O SMCOgera,
dinamicamente, processos escravos (Wnnn) para implementar a tarefa.

Com esse processo, terminamos os processos opcionais. Falta ainda tratarmos dos processos escravos. Processos escravos são processos de fundo, que realizam trabalho em nome de outros processos. Falaremos rapidamente dos processos escravo de l/O e de consulta paralela.
O processo escravo de l/O (Innn) simula uma E/S assíncrona para sistemas e dispositivos que não suportam. Em E/S assíncrona, não há nenhuma exigência para a transmissão de temporização,permitindo que outros processos possam começar antes que a transmissão tenha terminado.

Ouando falamos de execução paralela ou processamento paralelo,
múltiplos processos trabalham juntos, simultaneamente, para executar uma única instrução SQL. Ao dividir o trabalho entre vários processos, o Oracle Database pode executar a instrução mais rapidamente. Por exemplo, quatro processos de lidar com cada semestre em um ano em vez de um processo fazer o tratamento de todos os semestres, por si só. Veja na figura abaixo uma execução em paralelo:
Parallel Execution
Coordinator

Parallel Execution
Server Processes employees Table
SELECT COUNTf*)

FROM employees

WHERE phone_number LIKE *650%';

3. BANCA: FCC ANO: 2013 ÓRGÃO: MPE-MA PROVA: ANALISTA JUDICIÁRIO BANCO DE DADOS

Na arquitetura do Sistema Gerenciador de Bancos de Dados Oracle, existem os processos executados em background mandatórios e opcionais. Exemplos de processo mandatório e processo opcional são, respectivamente,
AJob Queue (CJQ) e Space Management Coordinator (SMCO).

B Recoverer (RECO) e Archiver (ARC).

C LogWriter (LGWR) e System Monitor (SMON).
D Archiver (ARC) e Checkpoint (CKPT).

E Flashback Data Archiver (FBDA) e Database Writer (DBW).

Comentário: Vejam que, pelo que acabamos de expor, os principais processos opcionais são
Archiver Processes (ARCn), Job Queue Processes (CJQO and Jnnn), Flashback Data Archiver
Process (FBDA) e Space Management Coordinator Process (SMCO). Vejam que, partindo destes processos, ficaríamos entre as alternativas A e B, para o processo definido como opcional.Contudo, observamos que o primeiro processo definido, na alternativa A, também é um processo opcional. Desta forma, podemos assinalar a alternativa B como a nossa resposta correta.
Gabarito: B

Finalmente, terminamos nossa explicação teórica sobre processos no Oracle. Ao final vamos observar como cada um dos processos está relacionado com a SGA. Vejam a figura abaixo:
MoDo DE INICIALIZAçÃo E DE ENCERRAMENTo DE

SERVIDoR

Vamos agora nos aprofundar no assunto sobre banco de dados Oracle e explicar os procedimentos envolvidos na inicialização e encerramento de uma instância de banco de dadosOracle.

Todo banco de dados Oracle em execução é associado a uma instância de banco de dados
Oracle. Quando um banco de dados é iniciado em um servidor de banco de dados(independentemente do tipo de computador), o Oracle aloca uma área de memória chamada
Área do Sistema Global (SGA) e inicia um ou mais processos de banco de dados Oracle. Esta combinação da SGA e dos processos Oracle é chamado de uma instância Oracle. A memória e os processos de uma instância gerenciam os dados do banco associado de forma eficiente e serve a um ou vários usuários de banco de dados.
Depois de iniciar uma instância, o Oracle Database associa a instância com o banco de dados especificado. Esta é uma base de dados montada (mounted). O banco de dados está,então, pronto para ser aberto, o que o torna acessível a usuários autorizados.
A inicialização e o encerramento do banco de dados são poderosas opções administrativas e são restritos a usuários que se conectam ao banco de dados Oracle com privilégios de administrador.Dependendo do sistema operacional, uma das seguintes condições estabelece privilégios de administrador para um usuário: 1. Privilégios do sistema operacional permitem ao usuário se conectar usando privilégios de administrador. 2. O usuário possui os privilégios deSYSDBA ou
SYSOPER e o banco de dados usa arquivos de senha para autenticar os administradores de banco de dados.
Para iniciar uma instância, o Oracle Database deve ler qualquer o arquivo de parâmetros de inicialização ou um arquivo de parâmetros de servidor. Esses arquivos contêm uma lista de parâmetros de configuração para essa instância e para o banco de dados. O OracleDatabase,
tradicionalmente, armazena os parâmetros de inicialização em um arquivo de parâmetro de inicialização de texto. Você também pode optar por manter os parâmetros de inicialização em um arquivo binário de parâmetros do lado do servidor (SPFILE).
Os parâmetros de inicialização armazenados em um arquivo de parâmetro de servidor são persistentes, na medida em que todas as alterações feitas aos parâmetros enquanto uma instância está sendo executado pode perdurar, por exemplo, após um encerramento e reinicialização.
VISÃo GERAL DA INICIALIZAçÃo DA INSTÂNCIA E Do BANCo DE DADoS

Os três passos para iniciar um banco de dados Oracle, tornando-o disponível para uso em todo o sistema são: 1. Iniciar uma instância., 2. Montar o banco de dados. 3. Abrir o banco de dados. Um administrador de banco de dados pode executar essas etapas usando a declaração STARTUP do SQLPlus ou Enterprise Manager.

Quando o Oracle Database inicia uma instância, ele lê o arquivo de parâmetro de servidor(SPFILE) ou arquivo de parâmetro de inicialização para determinar os valores iniciais dos parâmetros.Em seguida, ele aloca uma SGA, que é uma área comum de memória usada para informações de banco de dados, e cria processos em segundo plano. Neste ponto, nenhum banco de dados está associado com estes processos e estruturas de memória.
Quando inicia a instância, o banco de dados grava todas as definições de parâmetros explícitos no log de alerta na sintaxe de parâmetro válido. Se necessário, você pode copiar e colar esse texto em um novo arquivo de parâmetro e reiniciar a instância.
Você pode, ainda, iniciar uma instância em modo restrito (ou mais tarde alterar uma instância existente para estar no modo restrito). Isso restringe conexões a apenas os usuários que tenham obtido o privilégio de sistema sessão restrita (RESTRICTED SESSION).
Em circunstâncias incomuns, uma instância anterior pode não ter sido encerrada corretamente. Por exemplo, um dos processos da instância não poderia ter terminado de forma correta. Em tais situações, o banco de dados pode retornar um erro durante a inicialização de uma instância normal. Para resolver esse problema, você deve encerrar todos os processos remanescentes no banco de dados Oracle da instância anterior, antes de iniciar a nova instância.
A instância monta um banco de dados para associar o banco de dados com essa instância. Para montar o banco de dados, a instância encontra os arquivos de controle do banco de dados e os abre. Arquivos de controle são especificados no parâmetro de inicialização CONTROL_FILESno arquivo de parâmetro usado para iniciar a instância. O Oracle Database, então, lê os arquivos de controle para obter os nomes dos arquivos de dados do banco de dados e dos arquivos de log de redo.
Neste ponto, a base de dados ainda está fechada e só é acessível para o administrador do banco. O administrador de banco de dados pode manter o banco de dados fechado para completar as operações de manutenção específicas. No entanto, a base de dados ainda não está disponível para as operações normais de usuários.
Se o Oracle Database permite que várias instâncias montem o mesmo banco de dados simultaneamente, o administrador de banco de dados pode usar o parâmetro de inicializaçãoCLUSTER_DATABASE, para tornar o banco de dados disponível para várias instâncias. O valor padrão do parâmetro CLUSTER_DATABASE é falso. As versões do Oracle Database que não suportam OracleRAC só permitem CLUSTER_DATABASE ser falso.

Um clone de banco de dados é uma cópia de um banco de dados especializado que pode ser usado para a recuperação de espaço de tabela em um ponto no tempo. Quando você executa recuperação da tablespace point-in-time, você monta o banco de dados clone e recupera as áreas de tabela para o instante de tempo desejado. Em seguida, exporta os metadados a partir do clone para o banco de dados primário e copia os arquivos de dados a partir dos espaços de tabela recuperados.
Abrir um banco de dados montado torna disponível para as operações de banco de dados normais. Qualquer usuário válido pode se conectar a um banco de dados aberto e acessar suas informações. Normalmente, um administrador de banco de dados abre o banco de dados para torná-lo disponível para uso geral.
Quando você abre o banco de dados, o Oracle abre os arquivos de dados on-line e os arquivos de log de refazer. Se um espaço de tabela estava offline quando o banco de dados foi desligado anteriormente, o espaço de tabela e seus arquivos de dados correspondentes ainda serão desligados quando você reabrir o banco de dados.
Se nenhum dos arquivos de dados ou arquivos de log de refazer está presente quando você tenta abrir o banco de dados, o Oracle Database retorna um erro. Você deve executar a recuperação de um backup de todos os arquivos danificados ou ausentes antes de abrir o banco de dados.
VISÃo GERAL Do ENCERRAMENTo DA INSTÂNCIA E Do BANCo DE DADoS

As três etapas para encerrar um banco de dados e sua instância associada são: 1.
Fechar o banco de dados, 2. Desmontar o banco de dados e 3. Encerrar a instância. Um administrador de banco de dados pode executar essas etapas usando o Enterprise Manager. Oracle Database executa automaticamente todas as três etapas sempre que uma instância é desligada (shut down).
Fechar um banco de dados

Quando você fecha um banco de dados, o Oracle Database escreve todos os dados do banco de dados e de recuperação presentes na SGA para os arquivos de dados e arquivos de log de redo,respectivamente. Em seguida, o Oracle Database fecha todos os arquivos de dados on-line e os arquivos de log de redo. (Quaisquer arquivos de dados off-line de todos os espaços de tabela off-
line já foram fechados. Se posteriormente você reabrir o banco de dados, qualquer espaço de tabela que estava off-line e seus arquivos de dados permanecem off-line e fechados,respectivamente).
Neste ponto, o banco de dados é fechado e inacessível para as operações normais. Os arquivos de controle permanecerão abertos depois de um banco de dados ser fechado.
Você pode optar por fechar o banco de dados pelo encerramento da instância. Em situações de emergência, você pode terminar a instância de um banco de dados aberta para fechar e desligar completamente o banco de dados de forma instantânea. Este processo é rápido, porque a operação de escrever todos os dados dos buffers da SGA para os arquivos de dados e arquivos de log redo é ignorada. A reabertura posterior do banco de dados requer recuperação, que o OracleDatabase executa automaticamente.
Desmontar o banco de dados

Após o banco de dados ser fechado, o Oracle Database desmonta o banco de dados para dissociá-lo da instância. Neste ponto, a instância permanece na memória de seu computador. Depois que o banco de dados é desmontado, o Oracle Database fecha os arquivos de controle do banco de dados.
Encerrar uma instância

O passo final para encerramento do banco de dados é o desligamento da instância.
Quando você desligar uma instância, a SGA é removida da memória e os processos em segundo plano são terminados.
Em circunstâncias excepcionais, o desligamento de uma instância pode não ocorrer de forma limpa; todas as estruturas de memória podem não terem sido removidas da memória ou um dos processos de fundo pode não ter terminado. Quando existem restos de uma instância anterior, o startup da instância subsequente, provavelmente, irá falhar. Em tais situações, o administrador de banco de dados pode forçar a inicialização da nova instância, primeiro removendo os restos da instância anterior e, em seguida, iniciando uma nova instância, ou pela emissão de uma declaraçãoSHUTDOWN ABORT no SQL*Plus ou usando Enterprise Manager.

BACkUP

Backups de banco de dados podem ser físico ou lógico. Backups físicos, que é a principal preocupação dentro da estratégia de backup e recuperação, são cópias de arquivos de banco de dados físicos. Você pode fazer backups físicos com utilitários RMAN ou do sistema operacional.
Em contraste, os backups lógicos contêm dados lógicos, tais como tabelas e procedimentos armazenados. Você pode extrair os dados lógicos com um utilitário de banco de dadosOracle, como o Data Pump Export e armazená-lo em um arquivo binário. Backups lógicos podem complementar os backups físicos.
O objetivo principal de um backup de banco de dados é a proteção de dados, mas você também pode criar backups de arquivamento para preservação de dados. Por exemplo, suponha que você tenha um requisito de negócio para preservar registros de transações do cliente por um período especificado. Você pode usar o RMAN para criar um backup de arquivo do banco de dados,juntamente com os arquivos de redo necessários para torná-lo compatível para armazenamento externo. Você pode controlar quanto tempo esse backup de banco de dados está isento das políticas de retenção do RMAN que regem a eliminação de backups obsoletos.
Backup completo e parcial

Um backup de banco de dados inteiro ou completo (whole) é um backup de todos os arquivos de dados, mais o arquivo de controle. Backups de banco de dados integrais são o tipo mais comum de backup.
Como mostrado abaixo, um backup de banco de dados completo pode ser tomado em qualquer modo, ARCHIVELOG ou NOARCHIVELOG, e pode ser considerado um backup consistente ou um backup inconsistente. Se uma cópia de segurança é consistente, determina se você deve aplicar os logs de redo depois de restaurar o backup.
Whole database backups

ARCHIVELOG NOARCHIVELOG

open, inconsistent consistent closed open. inconsistent(not valid)

inconsistent consistent closed inconsistent(not recommended)

Um backup parcial inclui um subconjunto da base de dados, isto é, espaços de tabelas individuais ou arquivos de dados. Um backup de espaço de tabela é um backup dos arquivos de dados que compõem o espaço de tabela. Backups de espaços de tabelas, seja online ou offline, são válidos apenas se o banco de dados está operando no modo ARCHIVELOG. A razão é que o log de redo é necessário para tornar o espaço de tabela restaurado consistente.
Um backup de arquivo de dados é um backup de um único arquivo de dados. Backups de arquivo de dados, que não são tão comuns como backups de tabela, são válidos em bancos de dadosARCHIVELOG.

Em um backup de banco de dados consistente, toda leitura/gravação de arquivos de dados e arquivos de controle são marcadas (checkpoint) com o mesmo número de alteração do sistema (SCN
-System Change Number). Os arquivos de backup possuem a garantia de contertodas as alterações dentro dele SCN. Ao contrário de um backup inconsistente, um backup inteiro consistente não exige a recuperação depois que ele for restaurado.
A única maneira de fazer um backup de banco de dados inteiro consistente é desligar o banco de dados com as opções NORMAL, IMMEDIATE, ou TRANSACTIONAL e fazer o backup, enquanto o banco está fechado. Se um banco de dados não for encerrado de forma consistente, por exemplo,uma instância falhar ou você emitir uma declaração SHUTDOWN ABORT, os arquivos de dados são sempre inconsistentes, ao menos que o banco de dados seja de somente leitura.
O ponto importante é que você pode abrir o banco de dados após a restauração de um backup de banco de dados inteiro consistente sem a necessidade de recuperação, porque os dados já são consistentes: nenhuma ação é necessária para tornar os dados em arquivos de dados restaurados corretos. Assim, você pode restaurar um backup consistente de um ano atrás sem executar a recuperação de mídia e sem o banco de dados executar a recuperação de instância.
Quando você restaurar um backup de banco de dados inteiro consistente sem aplicar o log de redo, você perde todas as operações que foram feitas após o backup for feito.
Um backup de banco de dados inteiro consistente é a única opção de backup válido para bancos de dados que operam no modo NOARCHIVELOG. Outras opções de backup exigem a recuperação para manter a consistência, o que não é possível sem os arquivos de logs de redo.
Um backup de banco de dados inteiro consistente é também uma opção de backup válida para bancos de dados que operam no modo ARCHIVELOG. Quando esse tipo de backup é restaurado e os logs arquivados estão disponíveis, você tem a opção de abrir o banco de dados imediatamente e perder as transações que foram feitas após o backup, ou aplicar os logs de redo arquivados para recuperar essas transações.
Em um backup de banco de dados inconsistente, a leitura/gravação de arquivos de dados e arquivos de controle não possui garantia de sofrer um checkpoint para o mesmo SCN. Os arquivos no backup podem conter dados de diferentes pontos no tempo, o que significa que as mudanças podem ser perdidas. Esta situação pode ocorrer quando os arquivos de dados são modificados enquanto os backups estão sendo feitos.
Se você fizer um backup de banco de dados quando ele está aberto ou montado após um desligamento inconsistente, então o backup é inconsistente. Um backup de arquivos de dados on­line é chamado de online backup. Você deve executar o banco de dados no modo ARCHIVELOG para backups on-line.
Enquanto o banco de dados é executado no modo ARCHIVELOG, e você guarda os arquivos de logs de redo e arquivos de dados, os backups inconsistentes podem ser a base para uma estratégia de backup e recuperação. Backups inconsistentes oferecem disponibilidade superior, porque você não tem que desligar o banco de dados para fazer backups que protegem totalmente o banco de dados.
A recuperação de banco de dados Oracle faz backups inconsistentes se tornarem consistentes ao ler todos os logs de redo arquivados e on-line, começando pelo SCN mais recentes presentes em qualquer um dos cabeçalhos de arquivo de dados, e aplicando as alterações dos logs de redo nos arquivos de dados. Depois de fazer um backup inconsistente, você deve garantir que tem todo o log de redo necessário para recuperar o backup, arquivando os logs redo ainda não arquivados. Se você não tem todos os logs redo arquivados produzidos durante o backup, então você não pode recuperá-lo, porque você não tem os dados necessários para torná-lo consistente.

HORA DE

PRATICAR!

(Ministério da Economia - Infraestrutura - 2020) Com relação ao sistema gerenciador de banco de dados Oracle, julgue o próximo item.
95 Um banco de dados executado em modo de ARCHIVELOG permite que arquivos de redo log atualizem, em tempo real, banco de dados em formato active.
Comentários: Algumas estratégias são necessárias para garantir a máxima recuperabilidade do banco de dados Oracle em caso de falha, seja ela de instância ou mesmo de hardware. Uma dessas estratégias é assegurar que o banco opere em ArchivelogMode de forma que todas as alterações efetuadas possam ser verificadas e efetivadas em um momento de recuperação da instância do banco.
Os arquivos de log de redo são preenchidos com registros de redo. Um registro de refazer, também chamado de entrada de refazer, é composto de um grupo de vetores de mudança, cada um dos quais é uma descrição de uma mudança feita em um único bloco no banco de dados.
O log de redo de um banco de dados consiste em dois ou mais arquivos de log de redo. O banco de dados requer no mínimo dois arquivos para garantir que um esteja sempre disponível para gravação enquanto o outro está sendo arquivado.
Ao executar um banco de dados no modo ARCHIVELOG, você ativa o arquivamento do log de redo. O
arquivo de controle de banco de dados indica que um grupo de arquivos de redo log preenchidos não pode ser reutilizado pelo LGWR até que o grupo seja arquivado. Um grupo preenchido fica disponível para arquivamento imediatamente após a troca de log de redo ocorrer. Oarquivamento tem estas vantagens:

* Um backup de banco de dados, junto com arquivos de redo log online e arquivados, garante que você possa recuperar todas as transações confirmadas no caso de um sistema operacional ou falha de disco.
* Se você mantiver um log arquivado, poderá usar um backup feito enquanto o banco de dados está aberto e em uso normal do sistema.
* Você pode manter um banco de dados de reserva atualizado com seu banco de dados original aplicando continuamente os logs de redo arquivados originais ao banco de dados de reserva (secundário).
Veja que a função do ARCHIVELOG é manter um estrutura de recuperação em caso de falha no banco de dados primário. Não faz sentido usar o redo log para atualização do banco de dados ativo. Outro ponto é que a atualização de bancos de dados secundários não é feita em tempo real.
Gabarito Errado.

1. BANCA: FCC ANO: 2012 ÓRGÃO: TRE-CE PROVA: TÉCNICO DO JUDICIÁRIO - PROGRAMADOR DE
SISTEMAS

Sobre backup e recuperação do banco de dados Oracle é correto afirmar:

A As informações dos arquivos de controle do banco de dados não podem ser usadas para orientar a progressão automatizada da recuperação porque não trazem dados sobre a estrutura de arquivos e o número atual de sequência do registro que está sendo gravado.
B O backup de datafiles e dos arquivos de controle do banco de dados só poderá ser feito quando o banco de dados estiver fechado ou o tablespace estiver off-line.
C O backup dos datafiles de um tablespace individual ou o de um arquivo de controle são exemplos de backups completos.
D Os backups completos são executados quando o banco de dados está aberto e disponível para uso.
E O registro redo é um conjunto de arquivos que protegem os dados alterados do banco de dados alojados na memória e que não foram gravados nos datafiles.
I Comentário: Vejam que a alternativa E converge com o que acabamos de explicar sobre a participação do log de redo na recuperação do banco de dados Oracle. Vejamos o que está incorreto nas demais alternativas.
A. Vimos que o arquivo de controle grava as informações sobre o SCN, bem como contribui para o processo de recuperação.
B. Vimos que temos os tipos de backup online e off-line, bem como os consistentes e os inconsistentes.
C. Backups completos, como o próprio nome diz, é um backup de todos os arquivos de dados,
mais o arquivo de controle.

D. Como vimos, podemos executar backups completos online. Neste caso, precisamos dos arquivos de logs de redo, ou off-line.
Gabarito: E

RMAN

Recovery Manager (RMAN) é um cliente de banco de dados Oracle que executa tarefas de backup e recuperação em seus bancos de dados e automatiza a administração de suas estratégias de backup. Ele simplifica muito o backup, a restauração e a recuperação de arquivos de banco de dados.
O ambiente RMAN consiste de serviços e bancos de dados que desempenham um papel para fazer o backup dos seus dados. No mínimo, o ambiente para o RMAN deve incluir os seguintes componentes:
Um banco de dados de destino - Um banco de dados Oracle onde o RMAN está conectado por meio da palavra-chave TARGET. O target é um banco de dados em que o RMAN está executando as operações de backup e recuperação. RMAN sempre mantém metadados sobre suas operações em um banco de dados no arquivo do banco de dados de controle. Os metadados RMAN são conhecidos como o repositório RMAN.
O cliente RMAN - Um executável Oracle Database que interpreta comandos, dirige sessões de servidor para executar esses comandos e registra sua atividade no arquivo de controle de banco de dados de destino. O executável do RMAN é instalado automaticamente com o banco de dados e é normalmente localizado no mesmo diretório que os outros executáveis do banco de dados.Por exemplo, o cliente RMAN no Linux está localizado em $ ORACLE_HOME/bin.
Alguns ambientes podem usar os seguintes componentes opcionais:

A área de recuperação rápida (fast recovery area) - A localização do disco em que o banco de dados pode armazenar e gerenciar arquivos relacionados a backup e a recuperação. Você define a localização da área de recuperação rápida e o tamanho, com os parâmetros de inicializaçãoDB_RECOVERY_FILE_DEST e DB_RECOVERY_FILE_DEST_SIZE.

Um gerente de mídia (media manager) - Um aplicativo necessário para RMAN interagir com dispositivos de mídia sequenciais, como bibliotecas de fitas. Um gerente de mídia controla estes dispositivos durante o backup e a recuperação, o gerenciamento de carga, de rotulagem, e a descarga de mídia. Dispositivos de gerenciamento de mídia são às vezes chamados SBT(system backup to tape).
Um catálogo de recuperação - Um esquema de banco de dados separado usado para gravar a atividade RMAN contra um ou mais bancos de dados de destino. Um catálogo de recuperação RMAN
preserva os metadados do repositório se o arquivo de controle for perdido, tornando muito mais fácil para restaurar e recuperar, após a perda do arquivo de controle. O banco de dados poderá substituir registros mais antigos no arquivo de controle, mas o RMAN mantém registros para sempre no catálogo, a menos que os registros sejam excluídos pelo usuário.
Para executar um backup, basta iniciar o RMAN e conectar ao banco de dados TARGET e,
em seguida, executar o comando BACKUP DATABASE. Para saber mais sobre o comando, acesse.
2. BANCA: FCC ANO: 2014 ÓRGÃO: TRT - 13^ REGIÃO (PB) PROVA: ANALISTA JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

Recovery Manager - RMAN é um utilitário de banco de dados que faz o backup,
restauração e recuperação de bancos de dados Oracle llg. Este utilitário
A permite definir, para cada cópia de segurança, os valores de status: iniciado,
finalizado, em andamento, expirado e obsoleto.
B permite definir uma tag para identificar um backup como parte de um grupo de backups. Todos os seus backups são etiquetados com uma tag, exceto os incrementais.
C armazena os backups de bancos de dados como cópias de imagens (image copies),
conjuntos de backup (backup sets) ou backups de arquivos de configuração (configuration file backup).
ET mantém em um metadado o registro dos arquivos de banco de dados e backups para cada banco de dados em que executa operações.
E não suporta paralelismo, que é o uso de múltiplos canais e sessões de servidor para executar o trabalho de um backup ou a tarefa de recuperação.
Comentário: Recovery Manager (RMAN) é um utilitário Oracle que pode fazer backup,restaurar e recuperar arquivos de banco de dados. O produto é um recurso do servidor de banco de dados Oracle e não requer instalação separada.
O Recovery Manager é uma aplicação cliente-servidor que utiliza sessões do banco de dados para executar tarefas de backup e recuperação. Ele armazena metadados sobre suas operações no arquivo de controle (control file) do banco de dados sobre o qual está operando e,opcionalmente, no catálogo do schema de recovery de um banco de dados Oracle.

Você pode chamar o RMAN como um executável de linha de comando a partir do prompt do sistema operacional ou usar alguns recursos do RMAN através do Enterprise Manager GUI.
Gabarito: D

QUESTõES CoMENTADAS CoMPLEMENTARES

1. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

No Oracle llg, os advisors são desenvolvidos com base em componentes de infraestrutura,
sendo um deles o Automatic Workload Repository (AWR), que
(A) fornece informações sobre melhoria percentual no tempo do banco de dados para vários tamanhos de System Global Area.
(B) faz recomendações para melhorar a performance de uma carga de trabalho. Além de analisar índices e visualizações materializadas como em versões anteriores, ele analisa tabelas e consultas e faz recomendações sobre como otimizar estruturas de armazenamento.
(C) faz análise, detecta gargalos e recomenda soluções. As recomendações podem incluir o tipo de advisor que precisa ser usado para resolver o problema.
(D) analisa problemas com instruções SQL individuais como, por exemplo, o uso equivocado delas,além de fazer recomendações para melhorar a performance.

(E) fornece serviços para coletar, manter e utilizar estatísticas para fins de detecção de problemas e autoajuste e onde as informações estatísticas são armazenadas na forma de snapshots.
Comentários: O AWR coleta, processa e mantém estatísticas de desempenho para fins de detecção de problemas e auto ajuste. Esses dados reunidos são armazenados na memória e no banco de dados e são exibidos em relatórios e visualizações. As estatísticas coletadas e processadas pelo AWR incluem:
* Estatísticas de objeto que determinam estatísticas de acesso e uso de segmentos do banco de dados;
* Estatísticas do modelo de tempo com base no uso de tempo das atividades;

* Algumas das estatísticas do sistema e da sessão;

* Instruções SQL que estão produzindo a carga mais alta no sistema, com base em critérios como tempo decorrido e tempo de CPU;
* Estatísticas do histórico de sessões ativas (ASH), representando o histórico da atividade de sessões recentes.
Assim, temos o gabarito da questão na letra e).

Gabarito: E

2. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

Em condições normais de operação, na versãol2c do Oracle, é possível realizar operações online de manutenção em uma table sem causar lock na tabela em questão quando usando instruçõesDDL, tais como

(A) drop index online ou server free online.

(B) explain plan online ou drop constraint online.

(C) alter index unusable online ou drop index online.

(D) create index online ou merge online.

(E) call set online ou transaction online.

Comentários: Em geral, os bancos de dados multiusuários usam alguma forma de bloqueio de dados para resolver os problemas associados à simultaneidade, à consistência e à integridade de dados.
Um bloqueio é um mecanismo que impede a interação destrutiva entre transações que acessam o mesmo recurso. Estes mecanismos bloqueiam dados automaticamente ou conforme especificado pelo usuário durante as instruções SQL.
A versãol2c do Oracle inovou com novas operações online de manutenção em uma table sem causar lock na tabela. As seguintes instruções DDL foram incluídas nesta modalidade:
drop index online alter index unusable online alter table move partition online alter table move subpartition online
Temos a resposta da questão na letra c).

Gabarito: C

3. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

Antes do Oracle 12c, os tamanhos máximos em bytes dos data types varchar2, nvarchar2
e raw atingiam, respectivamente, 4.000, 4.000 e 2.000. Os correspondentes tamanhos máximos, em bytes, desses data types estendidos no Oracle 12c, Release 1 (12.1)podem atingir,
respectivamente,

(A) 32.767, 32.767 e 32.767.

(B) 16.256, 8.156 e 4.096.

(C) 16.256, 16.256 e 8.156.

(D) 32.767, 16.256 e 8.156.

(E) 32.767, 32.767 e 16.256.

Comentários: Vejamos alguns dos tipos de dados do Oracle.

No tipo VARCHAR2(size [BYTE | CHAR]), é preciso especificar o size para VARCHAR2. Tamanho mínimo é 1 byte ou 1 caracter. Tamanho máximo é:
32767 bytes ou caracteres, se MAX_STRING_SIZE = EXTENDED
4000 bytes ou caracteres, se MAX_STRING_SIZE = STANDARD

No tipo NVARCHAR2(size), é preciso especificar o size para NVARCHAR2. Tamanho máximo é:
32767 bytes, se MAX_STRING_SIZE = EXTENDED

4000 bytes, se MAX_STRING_SIZE = STANDARD

No tipo RAW(size), é preciso especificar o size para o número RAW. Tamanho máximo é:
32767 bytes, se MAX_STRING_SIZE = EXTENDED

2000 bytes, se MAX_STRING_SIZE = STANDARD

Assim, temos a resposta na letra a) com tamanho máximo de 32767 bytes para os três tipos de dados.
Gabarito: A

4. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

No âmbito do Oracle Data Guard, o Oracle Database 12cRl implementa uma standby role que realiza a coordenação entre o database primário e todos seus standby databases. Trata-se de um
(A) standby database em cascata que usa RMAN ativo para receber os redo logs de outro standby database chamado DSync Standby.
(B) standby database em cascata que recebe os redo logs de um primary database e atua como um repositório de archivelogs, chamado RouterSync Standby.
(C) secondary standby database específico chamado RemoteSync Standby que usa RMAN ativo para receber os redo logs do primary database.
(D) primary standby database específico chamado RMAN Standby que recebe os redo logs de um outro primary database evitando, assim, a necessidade de se usar um segundo cascading standby.
(E) standby database em cascata que atua como um repositório de archivelogs chamado
FarSync
Standby.

Comentários: A versão 12cRl implementou aprimoramentos para o comando DUPLICATE.

A cláusula FOR FARSYNC cria uma instância de sincronização remota do Oracle Data Guard.
Você pode usar a duplicação de banco de dados ativa ou a duplicação baseada em backup para criar uma instância de sincronização distante.
Uma instância de sincronização remota do Oracle Data Guard é um destino remoto do
Oracle
Data Guard que aceita redo a partir do banco de dados primário e, em seguida, envia esse redo para outros membros da configuração do Oracle Data Guard.
Uma instância FarSync gerencia um arquivo de controle, recebe redo em logs de reconfiguração de espera (SRLs) e arquiva esses SRLs em logs de redo locais, mas é aí que a similaridade com o standbys termina. Uma instância de sincronização FarSync não tem arquivos de dados do usuário, não pode ser aberta para acesso, não pode executar a aplicação de repetição e nunca pode funcionar na função principal ou ser convertida em qualquer tipo de banco de dados em espera.
Temos a resposta da questão na letra e).

Gabarito: E

5. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

Um profissional de TI necessitava proteger, em tempo real, a exibição de diversos dados sobre benefícios e salários de empregados e também de valores de tributos devidos por contribuintes,a alguns usuários, ou seja, que os dados armazenados permanecessem inalterados, enquanto os dados a serem exibidos fossem transformados on-the-fly antes de deixarem o banco de dados.Para isto, o profissional se utilizou de uma funcionalidade que foi introduzida no pacote AdvancedSecurity do Oracle Database 12c, chamada

(A) Oracle DataPump.

(B) Oracle Spot ADDM.

(C) Oracle Data Redaction.

(D) ASM Disk Scrubbing.

(E) SecureFiles LOBs.

Comentários: O gabarito é letra c). O Oracle Data Redaction, uma parte do Oracle
Advanced
Security, permite que você mascare (redija) dados consultados por usuários ou aplicativos com poucos privilégios. A redação ocorre em tempo real quando os usuários consultam os dados.Assim, usuários com privilégios baixo não consegue visualizar a informação completa de uma informação sensível. Observe a figura abaixo:
Data Redaction

XXXX-XXXX-XXXX-5100

O mascaramento ou reescrita de dados suporta os seguintes tipos de função:

Reescrita completa de dados: Nesse caso, o banco de dados redigirá todo o conteúdo das colunas especificadas em uma tabela ou exibição. Por exemplo, uma coluna VARCHAR2 para um sobrenome exibe um único espaço.
Reescrita parcial de dados: Nesse caso, o banco de dados redigirá partes da saída exibida. Por exemplo, um aplicativo pode apresentar um número de cartão de crédito que termina em1234
como xxxx-xxxx-xxxx-1234. Você pode usar expressões regulares para redação total e parcial.Uma expressão regular pode redigitar dados com base em um padrão de pesquisa. Por exemplo, você pode usar expressões regulares para redigir números de telefone específicos ou endereços de e-mail.
Reescrita de dados aleatórios: Nesse caso, o banco de dados exibe os dados como valores gerados aleatoriamente, dependendo do tipo de dados da coluna. Por exemplo, o número1234567 pode aparecer como 83933895.

Reescrita usando uma expressão regular: Nesta situação podemos formular uma expressão que procure por termos específicos nas informações e os substitua por palavras como"[hidden]". O Airbnb por exemplo, não permite a troca de informações de e-mail e telefone antes da confirmação do pagamento da reserva. Assim, se você tentar enviar seu telefone a aplicação vai substituir por "[phone-hidde]".
Fui

Partia!

RegExp

Random

Stored Data u i
10/09/1992

987-65-4328

first.last@exampl ecom

| 5105105105105100 J

Redacted Display

01/01/2001

| XXX-XX-4328

4012888888881881

A redação de dados não é uma solução de segurança abrangente. Por exemplo, ele não impede que usuários privilegiados conectados diretamente realizem ataques de inferência em dados redigidos. Tais ataques identificam colunas redigidas e, pelo processo de eliminação,tentam voltar aos dados reais repetindo as consultas SQL que adivinham os valores armazenados.Para detectar e evitar inferência e outros ataques de usuários privilegiados, a Oracle recomenda o pareamento do Oracle Data Redaction com produtos de segurança de banco de dados relacionados, como o Oracle Audit Vault e o Database Firewall, e o Oracle Database Vault.
Gabarito: C

6. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

Com respeito ao Automatic SQL Tuning no Oracle Database 12c, quando o SQL Tuning
Advisor é executado na tarefa automática na janela de manutenção, o seu foco principal é para as instruções SQL de alta carga já executadas anteriormente, em alguns períodos específicos. No escopo global, ele verifica e analisa o comportamento dessas instruções nesses períodos,para avaliar se podem ter seu desempenho melhorado aceitando ou não o sql profile estabelecido. Aanálise é feita tanto com base no tempo de CPU como no de l/O. A tarefa automática tem parâmetros configuráveis, sendo dois deles, os seguintes:
I. ACCEPT_SQL_PROFILES que significa aceitar o sql profile automaticamente ou não.

II. MAX_AUTO_SQL_PROFILES que significa quantos profiles podem ser aceitos em geral no banco de dados Oracle em qualquer ponto no tempo.
As configurações padrão (default) para esses parâmetros são, respectivamente,
(A) true - 20.000.

(B) false - 10.000.

(C) false- 15.000.
(D) true - 15.000.
(E) true - 10.000.

Comentários: Você pode configurar a tarefa de Ajuste automático de SQL usando o Cloud
Control ou a linha de comando. Para configurar a tarefa de ajuste automático de SQL
usando o Cloud Control,
você pode ativar e desativar todas as tarefas de manutenção automáticas, incluindo a tarefaAjuste automático de SQL, usando o Cloud Control. Você deve executar a operação como
SYS
ou ter o privilégio EXECUTE no pacote PL / SQL DBMS_AUTO_SQLTUNE.

Para configurar a tarefa de ajuste automático de SQL usando a linha de comando, o pacoteDBMS_AUTO_SQLTUNE permite que você configure o ajuste automático do SQL especificando os parâmetros da tarefa, usando o procedimento SET_AUTO_TUNING_TASK_PARAMETER.
Para definir os parâmetros da tarefa Ajuste automático de SQL:

Conecte o SQL * Plus ao banco de dados com os privilégios apropriados e,
opcionalmente,
consulte as configurações da tarefa atual.

Por exemplo, conecte o SQL * Plus ao banco de dados com privilégios de administrador e execute a seguinte consulta:
7. BANCA: FCC/2018 - analista em gestão (DPE AM)/ especializado em tecnologia da informação de defensoria/ analista de banco de dados
Na definição do armazenamento (storage), considerando o sistema gerenciador de banco de dadosOracle llg, para se especificar uma área inicial de 10 GB, com incrementos graduais de 1 GB, o subcomando a ser utilizado é a) STORAGE (FIRST 10G STEP 1G).
b) STORAGE (PRIMARY 10G INC 1G).

c) STORAGE (INITIAL 10G NEXT 1G).

d) STORAGE (MAIN 10G PLUS 1G).

e) STORAGE (MAJOR 10G ADD 1G).

Comentário: A cláusula storage permite especificar como o Oracle Database deve armazenar um objeto de banco de dados. Os parâmetros de armazenamento afetam o tempo de acesso aos dados armazenados no banco de dados e a eficiência com que o espaço no banco de dados é usado.
INITIAL: Especifica o tamanho da primeira extensão do objeto. O Oracle aloca espaço para essa extensão quando você cria o objeto de esquema.
NEXT: Especifica em bytes o tamanho da próxima extensão a ser alocada ao objeto

Gabarito: C

8. FCC/2018 - analista em gestão (DPE AM)/ especializado em tecnologia da informação de defensoria/ analista de banco de dados
Considerando o sistema gerenciador de banco de dados Oracle llg, uma tarefa de administração é a criação de tablespaces. Dessa forma, o comando para a criação de uma tablespace do tipo bigfile, denominada bl, com arquivo de dados (datafile) dl, com 40 MB e autoextensível é a) CREATE BIGFILE TABLESPACE bl DATAFILE 'dl.dbf'SIZE 40M AUTOEXTEND ON;

b) CREATE 'dl.dbf' TABLESPACE 'bl'40M AUTOEXTEND YES;

c) CREATE DATAFILE, TABLESPACE 'dl.dbf', bl SIZE 40MB AUTOEXT = 1;

d) CREATE FILE 40MB TYPE BIGFILE TABLESPACE bl
DATA 'dl.dbf' EXTENSION ON;

e) CREATE 'dl.dbf' TABLESPACE bl BIGFILE
SIZE 40M AUTOEXTEND ON;

Comentário: Para criar um espaço de tabela bigfile, especifique a palavra-chave BIGFILE
na instrução CREATE TABLESPACE (CREATE BIGFILE TABLESPACE ...). O Oracle Database cria automaticamente um espaço de tabela gerenciado localmente com gerenciamento automático de espaço de segmento.
A sintaxe restante da instrução é a mesma da instrução CREATE TABLESPACE, mas você pode especificar apenas um arquivo de dados, no caso o arquivo de dados (datafile) dl.
Como o enunciado da questão menciona também que o arquivo seja autoextensível,
precisamos ainda incluir AUTOEXTEND ON. Quando a autoextensão é necessária, o banco de dados estende o arquivo de dados pelo tamanho existente ou 100 MB, o que for menor.Você também pode especificar explicitamente a unidade autoextensível, usando o parâmetro NEXTda cláusula STORAGE quando especificar o arquivo de dados (em uma operação CREATE ou
ALTER TABLESPACE).

Gabarito: A

9. BANCA: FCC - Técnico Judiciário (TRT 23^ Região)/ Apoio Especializado/ Tecnologia da lnformação/2016
Com relação às estruturas que fazem parte de um banco de dados Oracle e que possuem um papel importante na reconstrução do banco de dados a partir de um backup,
a) o banco de dados consiste em uma ou mais unidades de armazenamento lógico chamadas tablespaces, que consistem em um ou mais arquivos chamados datafiles.
b) quando os dados são modificados no banco de dados, o que foi modificado é gravado primeiro no online redo log, depois, é aplicado nos datafiles. Apesar de sua função de repositório intermediário, o redo log não guarda o registro das alterações feitas nos datafiles.
c) quando os dados em um datafile são atualizados, imagens anteriores destes dados são gravados em offline redo logs. Se uma transação é revertida, as informações dos redo logs são usadas para restaurar o conteúdo do datafile original.
d) o control file contém apenas informações das estruturas lógicas do banco de dados,
como tablespaces, extends e segments. Mantém também o registro de todas as operações realizadas nos datafiles.
e) um segment é a menor estrutura de armazenamento do Oracle e seu tamanho, baseado no parâmetro DB_BLOCK_SIZE, é normalmente um múltiplo do tamanho de um bloco do SistemaOperacional.

Comentário: Vamos comentar cada uma das alternativas.

a) Um banco de dados Oracle consiste em uma ou mais unidades de armazenamento lógicas denominadas tablespaces, que armazenam coletivamente todos os dados do banco de dados.Cada tablespace em um banco de dados Oracle consiste em um ou mais arquivos denominados arquivos de dados (datafiles), que são estruturas físicas compatíveis com o sistema operacional no qual oOracle é executado. Sendo assim, essa é a nossa resposta.

b) O redo guarda as informações que são alteradas por algum tempo. Se o banco estiver em modo archive, ele redireciona essas informações para o archivelog. Logo, temos uma afirmação incorreta.
c) Não existe offline redo logs. A UNDO Tablespace armazena os dados das transações finalizadas e assim é possível fazer o undo.
d) As informações que o arquivo de controle possui são: nome do banco de dados, data de criação do banco de dados, os nomes e localizações de cada datafile e redo log associados ao banco de dados, informações sobre as tablespaces, possíveis datafiles com status offline, o histórico de logs,informações sobre os archives gerados, backup sets e backup pieces gerados pelo RMAN,
backups de datafiles e informações de redo log, cópia de datafiles, o valor atual do número da sequência do log e informações de checkpoint. Bem mais informações do que as sugeridas pela alternativa.
e) Sabemos que a menor estrutura de armazenamento do Oracle é o bloco, logo temos mais uma assertiva incorreta.
Gabarito: A

10. BANCA: FCC - Analista Judiciário (TRT 14§ Região)/Apoio Especializado/ Tecnologia da lnformação/2016
Em uma empresa, um servidor Oracle llg apresentou um problema e o disco no qual se localizavam os arquivos do banco de dados foi danificado e perderam-se todos os arquivos
(control files, datafiles, online redo log files etc.), porém, o disco no qual estava a flash recovery area ficou intacto. Neste caso,
a) não será possível restaurar um backup do banco de dados, pois os control files,
datafiles e online redo log files foram perdidos.
b) será possível restaurar um backup do banco de dados utilizando o aplicativo DUMP ou RESTORE
a partir da flash recovery area.

c) não será possível restaurar um banco de dados porque o servidor sempre fica off-line quando o disco é danificado, impedindo o acesso à flash recovery area.
d) será possível restaurar um backup RMAN em conjunto com os archive redo log files contidos na flash recovery area.
e) não será possível restaurar o banco de dados, pois o software Oracle foi corrompido e o disco no qual se localizavam os arquivos do banco de dados foi danificado.
Comentário: Imagine um cenário de desastre completo, ou seja, o servidor de banco de dados sofreu uma pane na qual não só o software Oracle se corrompeu, mas também o disco aonde se localizava os arquivos do banco de dados foi perdido. Neste caso, todos os arquivos de banco de dados como os controlfiles, datafiles, online redo log files, além do spfile, foram perdidos. Este cenário só não poderia ser pior, porque o disco onde fica localizada a flash recovery area ficou intacto. Portanto,voltar um backup RMAN em conjunto com os archive redo log files contidos na flash recovery area será possível. Desta forma, podemos marcar nossa resposta na alternativa D.
Gabarito: D

11. BANCA: FCC - Analista de Tecnologia da Informação (CREMESP)/Administração de Banco de
Dados/2016

O Recovery Manager (RMAN) é um recurso do Oracle llg que executa tarefas de backup e recuperação, automatizando o trabalho das estratégias de backup de um DBA. O ambiente doRMAN possui componentes mínimos e opcionais que incluem:

I. Área de disco na qual o banco de dados pode armazenar e manipular os arquivos envolvidos no backup e recuperação. A localização desta área é indicada no parâmetroDB_RECOVERY_FILE_DEST.

II. Componente que controla os dispositivos durante o backup e recuperação,
gerenciando o carregamento, labeling e descarregamento. Os dispositivos são chamados de SBT -System
Backup to Tape.

III. Executável que interpreta comandos, direciona sessões do servidor para executar os comandos e registra as atividades no arquivo de controle do target database.
Os componentes de I a III são, correta e respectivamente,

a) File Recovery Area - Media Manager - RMAN executable.

b) Disk Recovery Area - Device Backup Manager - target client.

c) Fast Recovery Area - Media Manager - RMAN client.

d) Fast Recovery Area - Device Backup Manager - target client.

e) File Recovery Area - Recovery Manager - RMAN client.

Comentário: O gabarito é letra C. Vamos aos comentários dos itens:

Fast Recovery Area: Para simplificar o gerenciamento de arquivos de backup e recuperação,você pode criar uma área de recuperação rápida para seu banco de dados. A
área de recuperação rápida é um diretório gerenciado pelo Oracle, sistema de arquivos ou grupo de discos do Oracle Automatic Storage Management que fornece um local de armazenamento centralizado para arquivos de backup e recuperação. O Oracle cria logs arquivados e logs de flashback na área de recuperação rápida. O Oracle Recovery Manager (RMAN) pode armazenar seus conjuntos de backup e cópias de imagem na área de recuperação rápida e usá-los ao restaurar arquivos durante a recuperação de mídia. A área de recuperação rápida também atua como um cache de disco para fita.
Media Manager: De acordo com a aula, refere-se a um aplicativo necessário para o RMAN
interagir com dispositivos de mídia sequenciais, como bibliotecas de fitas. Um gerente de mídia controla estes dispositivos durante o backup e a recuperação, gerenciamento de carga, de rotulagem, e descarga de mídia. Dispositivos de gerenciamento de mídia são às vezes chamados SBT (system backup to tape).
RMAN client: Um executável Oracle Database que interpreta comandos, dirige sessões de servidor para executar esses comandos, e registra sua atividade no arquivo de controle de banco de dados de destino. O executável do RMAN é instalado automaticamente com o banco de dados e é normalmente localizado no mesmo diretório que os outros executáveis do banco de dados.
Gabarito: C

12. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/ Administrador de Banco de Dados/2015

Sobre as estruturas de armazenamento do sistema gerenciador de banco de dados Oracle llg é correto afirmar:
a) Cada tablespace é mapeado em um único bloco de dados.

b) Um datafile é mapeado em mais de um tablespace.

c) Cada segmento possui uma única extensão (extent).

d) Um tablespace pode ser composto por um ou mais segmentos.

e) Uma extensão é mapeada em mais de um datafile.

Comentário: Um ou mais arquivos de dados formam uma unidade lógica de armazenamento de banco de dados chamada tablespace. Um tablespace em um banco de dados Oracle consiste em um ou mais arquivos de dados físicos. Um arquivo de dados pode ser associado a apenas um tablespace e apenas um banco de dados.
Gabarito: D

13. BANCA: FCC - Técnico Judiciário (TRT 16- Região)/Apoio Especializado/ Tecnologia da lnformação/2014
No Oracle, uma base de dados física consiste de arquivos armazenados no disco e uma instância lógica consiste de estruturas e processos na memória do servidor. Os três tipos fundamentais de arquivos físicos que compõem uma base de dados Oracle llg são: arquivos de controle,arquivos de log de repetição e arquivos de a) modelagem multidimensional.
b) comunicação com linguagens de programação.

c) integração.

d) mineração de dados.

e) dados.

Comentário: Vamos aos conceitos dos tipos fundamentais de arquivos físicos que compõem uma base de dados Oracle llg.
Arquivos de controle: Um arquivo de controle rastreia os componentes físicos do banco de dados. É o arquivo raiz que o banco de dados usa para encontrar todos os outros arquivos usados pelo banco de dados. Devido à importância do arquivo de controle, a Oracle recomenda que o arquivo de controle seja multiplexado ou tenha várias cópias idênticas.
Arquivos de log de repetição: Cada banco de dados Oracle possui um conjunto de dois ou mais arquivos de redo log on-line. O conjunto de arquivos de redo log on-line é conhecido coletivamente como redo log do banco de dados. Um redo log é composto de entradas de redo, que também são chamadas de redo records.
O redo log on-line armazena uma cópia das alterações feitas nos dados. Se uma falha exigir que um arquivo de dados seja restaurado a partir do backup, as alterações de dados recentes que estiverem faltando no arquivo de dados restaurado poderão ser obtidas dos arquivos de redo log on-line, para que o trabalho nunca seja perdido. Os arquivos de redo log on-line são usados para recuperar um banco de dados após falha de hardware, software ou mídia.Para proteger-se contra uma falha que envolve o próprio arquivo de redo log on-line, oOracle
Database pode multiplexar o arquivo de redo log on-line para que duas ou mais cópias idênticas do arquivo de redo log on-line possam ser mantidas em discos diferentes.
Arquivos de dados: Arquivos de dados são os arquivos do sistema operacional que armazenam os dados no banco de dados. Os dados são gravados nesses arquivos em um formato proprietário da Oracle que não pode ser lido por outros programas. Arquivos temporários são uma classe especial de arquivos de dados associados apenas a tablespaces temporários.
Arquivos de dados podem ser divididos nos seguintes componentes:

Segmento: Um segmento contém um tipo específico de objeto de banco de dados. Por exemplo, uma tabela é armazenada em um segmento de tabela e um índice é armazenado em um segmento de índice. Um arquivo de dados pode conter vários segmentos.
Extensão: Uma extensão é um conjunto contíguo de blocos de dados dentro de um segmento.O Oracle Database aloca espaço para segmentos em unidades de uma extensão. Quando as extensões existentes em um segmento estão cheias, o banco de dados aloca outra extensão para esse segmento.
Bloco de dados: Um bloco de dados, também chamado de bloco de banco de dados, é a menor unidade de E / S para o armazenamento do banco de dados. Uma extensão consiste em vários blocos de dados contíguos. O banco de dados usa um tamanho de bloco padrão na criação do banco de dados.
Gabarito: E

14. BANCA: FCC - Analista Judiciário (TRT 13â Região)/Apoio Especializado/Tecnologia da lnformação/2014
Considere o texto abaixo:

O Oracle llg possui ferramentas para gestão de banco de dados que fornecem orientação específica sobre como lidar com os principais desafios de gestão de dados.Uma dessas ferramentas analisa comandos SQL e faz recomendações de como melhorá-los. Esta ferramenta pode ser executada automaticamente durante os períodos de manutenção (normalmente à noite). Durante cada execução automática, ela seleciona consultas SQL de alta carga(high-load)
e gera recomendações para ajustar essas consultas. Permite realizar análises estatísticas, criação de perfis SQL, análise de caminho de acesso e análise de estruturas SQL.
O texto descreve uma ferramenta conhecida como a) SQL Tuning Advisor.
b) SQL Access Advisor.

c) Automatic Database Diagnostic Monitor.

d) SQL Analysis Advisor.

e) SQL Performance Impact Advisor.

Comentário. Vamos analisar cada uma das ferramentas acima, tentando descrever suas principais funcionalidades.
O SQL Tuning Advisor analisa as instruções SQL de alto volume e oferece recomendações de ajuste. Analisa um ou mais instruções SQL como uma entrada e chama o Automatic TuningOptimizer para realizar ajuste de SQL sobre os comandos. Ele pode ser executado contra qualquer instrução SQL. Fornece sugestões sob a forma de ações SQL precisas para ajustes nas instruções SQL juntamente com os benefícios de desempenho esperados. A recomendação ou conselho fornecido refere-se à coleção de dados estatísticos sobre os objetos. Acriação de novos índices, a reestruturação da instrução SQL, ou criação de um perfil de SQLpodem ser algumas das sugestões. Você pode optar por aceitar a recomendação para completar o ajuste das instruções SQL. O Oracle Database pode automaticamente ajustar as instruções SQL por meio da identificação de instruções SQL problemáticas e execução das recomendações de ajuste usando o SQL Tuning Advisor.
Visões materializadas e índices são essenciais para o tuning de banco de dados visando obter um desempenho ideal em consultas intensivas de dados complexos. O SQL Access Advisor ajuda você a atingir suas metas de desempenho, recomendando um conjunto apropriado de visões materializadas, materialized view logs e índices para uma determinada carga de trabalho. Compreender e usar estas estruturas é essencial para otimizar comandos SQL,fazendo com que eles possam gerar melhorias significativas de desempenho em consulta de dados. As vantagens, no entanto, não estão livres de custo. A criação e manutenção destes objetos podem ser demoradas, e os requisitos de espaço podem ser significativos.
Quando ocorrem problemas com um sistema, é importante realizar um diagnóstico preciso e oportuno do problema, antes de fazer quaisquer alterações. Muitas vezes,o DBA
simplesmente olha para os sintomas e imediatamente começa a mudar o sistema para corrigir esses sintomas. No entanto, um diagnóstico preciso do problema real na fase inicial aumenta significativamente a probabilidade de sucesso na resolução do problema.
No Oracle Database, os dados estatísticos necessários para o diagnóstico preciso do problema são armazenados no Automatic Workload Repository (AWR). O AutomaticDatabase
Diagnostic Monitor (ADDM) analisa os dados do AWR, diagnostica as causas dos problemas de desempenho, fornece recomendações para corrigir quaisquer problemas e, ainda, identifica as áreas não problemáticas do sistema.
A alternativa D, SQL Analysis Advisor, não existe dentro do rol de ferramentas do Oracle.

O SQL Performance Impact Advisor foi introduzido no Oracle Database llg. Ele permite você prever como mudanças de sistemas podem afetar na performance do SQL.
Gabarito: A

15. BANCA: FCC - Analista Judiciário (TRT 1- Região)/Apoio Especializado/Tecnologia da lnformação/2014
O sistema gerenciador de Bancos de Dados Oracle llg armazena as tabelas de dicionário de dados na tablespace
A MAIN.
BSYSTEM.
C SYSAUX.
D UNDO.

ETEMP.

Comentário. Uma das partes mais importantes de um banco de dados Oracle é o seu dicionário de dados, que é um conjunto de tabelas de somente leitura que contêm informações sobre o banco de dados. Um dicionário de dados contém:
1. As definições de todos os objetos de esquema no banco de dados (tabelas, índices,
clusters,
sinônimos, sequências, procedimentos, funções, pacotes, gatilhos, e assim por diante)

2. Quanto espaço foi alocado para e quanto é usado atualmente, para cada um dos objetos de esquema
3. Os valores padrão para colunas

4. Informações sobre as restrições de integridade

5. Os nomes de usuários do Oracle Database

6. Privilégios e funções que cada usuário tenha

7. Informações de auditoria, tais como quem acessou ou atualizou os objetos de esquema

8. Outras informações do banco de dados geral

I O dicionário de dados é estruturado em tabelas e visões, assim como outros dados de banco de dados. Todas as tabelas de dicionário de dados e visões para um determinado banco são armazenadas no espaço de tabela (tablespace) SYSTEM desse banco de dados.
O dicionário de dados não é importante somente para o banco de dados Oracle, é uma ferramenta importante para todos os usuários, desde usuários finais aos designers de aplicativos e administradores de banco de dados. É possível usar instruções SQL para acessar o dicionário de dados. Devido ao fato de o dicionário de dados ser somente para leitura, você pode emitir apenas consultas (instruções SELECT) contra as tabelas e visões.
Pelo exposto acima, confirmamos nossa resposta na alternativa B.

Gabarito: B

16. BANCA: FCC ANO: 2013 ÓRGÃO: TRT - 15^ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

Data warehouses geralmente contém tabelas com grande número de informações e requerem técnicas para manejá-las e prover um bom desempenho de pesquisa. O Oracle 10g provê meios de particionamento de tabelas para se adequar a este modelo. Os tipos de particionamento(partitioning) disponíveis são: Range, Hash, Composite e

A Recursive.
B List.

CIndexed.
D Neutral.

I

E Forecast.

Comentário. Oracle Partitioning oferece três métodos de distribuição de dados fundamentais como estratégias básicas de particionamento que controlam como os dados são colocados em partições individuais: Range, Hash e List. Usando esses métodos de distribuição de dados, uma tabela pode ser particionada como uma lista única ou como uma tabela de partição composta(Composite).

Gabarito: B

17. BANCA: FCC ANO: 2013 ÓRGÃO: TRT - 15^ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

Arquitetar e manter processos ETL é considerado por muitos uma das tarefas mais difíceis de um projeto de data warehouse. Muitos projetos deste tipo utilizam ferramentas para manter este processo, por exemplo, provê recursos de ETL e tira vantagem das capacidades de banco de dados inerentes. A lacuna acima é corretamente preenchida com Oracle
A Warehouse Builder (OWB).
B Loading Data (OLD).

C Data Transformation (ODT).
D Query and Input (OQI).

E Business Intelligence (OBI).

Comentário. Vamos analisar as definições de cada uma das alternativas e verificar qual preenche corretamente a lacuna.
O Oracle Warehouse Builder (OWB) é uma ferramenta única e abrangente para todos os aspectos relacionados à integração de dados. Warehouse Builder aproveita o OracleDatabase para transformar os dados em informação de alta qualidade. Ele fornece a qualidade dos dados, a auditoria de dados, a modelagem relacional e dimensional totalmente integrada e o gerenciamento de ciclo de vida completo de dados e metadados. Warehouse Builder permite criar data warehouses, migrar os dados de sistemas legados, consolidar dados de diferentes fontes, limpar e transformar dados para fornecer informação de qualidade e, ainda, pode gerir os metadados corporativos. Vejam que esta é a nossa resposta.
As alternativas B, C e D não existem nem como ferramentas nem como processos dentro doOracle. Engraçado que se você procurar no Google as expressões das alternativas, entre os primeiros links estarão várias citações para a própria questão acima.
Já letra E trata do Oracle Business Intelligence, uma plataforma única que permite aos clientes descobrirem novos insights e tomar decisões de negócios mais rápidas e mais bem informados,oferecendo análises visuais ágeis. Mobile Instant, dashboards altamente interativos,poderosos relatórios operacionais, alertas just-in-time, pesquisa por conteúdo e metadados,gestão da estratégia, acesso nativo a fontes de Big Data, computação in-memory sofisticada e gerenciamento de sistemas simplificados se combinam para tornar o Oracle BI 12c uma solução abrangente que reduz custos e aumenta o retorno sobre o investimento para toda a organização. É muito marketing! Mas é quase isso que a plataforma oferece. ©
Gabarito: A

18. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/ Administrador de Banco de Dados/2013

O gerenciamento de configuração é um componente fundamental nas operações de TI diárias de toda empresa. O Oracle Configuration Management Pack é a peça central da capacidade doOracle Enterprise Manager de gerenciar configurações e automatizar os processos de TI.
Um componente chave desta solução reduz o custo e atenua o risco, detectando,validando e reportando, de forma automática, alterações autorizadas e não autorizadas. Este componente é o a) Log Analiser.
b) Graphical Configurator Addon.

c) Configuration Change Console.

d) Data Recovery Manager.

e) Instant Support.

Comentário: O gabarito da questão é a letra c), Configuration Change Console.
Este componente fornece detecção de alterações de configuração em tempo real e automação de estruturas de conformidade, juntamente com autorização de observação automatizada usando um Conector de Gerenciamento de Mudanças.
Gabarito: C

19. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/Administrador de Banco de Dados/2013

Considere:

I. O módulo de nuvem do Oracle Secure Backup é implementado por meio da interface
SBT do
Oracle Recovery Manager (RMAN). A interface SBT permite que bibliotecas de backup externas sejam perfeitamente integradas com este recurso. Consequentemente, os administradores do banco de dados podem continuar a usar suas ferramentas de backup existentes para realizar backups em nuvem.
II. O Oracle Secure Backup aproveita a capacidade do RMAN para criptografar backups e garantir a segurança dos dados. A segurança e a privacidade dos dados são especialmente importantes em ambientes compartilhados, acessíveis publicamente, como a nuvem de armazenamento.
III. A integração com o mecanismo do banco de dados Oracle permite que o Oracle Secure Backup identifique e ignore o espaço não utilizado (blocos) no banco de dados. Os usuários também se beneficiam dos recursos sofisticados de compressão do RMAN. No momento de transmissão de backups em redes mais lentas, como a Internet pública, qualquer redução no tamanho do backup é percebida diretamente como um aumento no desempenho do backup.
Está correto o que consta em a) I, apenas.
b) I e II, apenas.

c) III, apenas.

d) II e III, apenas.

e) I, II e III.

Comentário: Todos os itens estão corretos. O módulo de nuvem do Oracle Secure Backup (OSB)
permite que um banco de dados Oracle envie seus backups para o S3 da Amazon. Ele é compatível com as versões do banco de dados Oracle 9i Release 2 e superior e exige uma conexão de rede com a Internet e provisionamento das formas de pagamento aos Serviços daWeb da Amazon.

O módulo de nuvem do Oracle Secure Backup é implementado por meio da interface SBT do
Oracle Recovery Manager (RMAN). A interface SBT permite que bibliotecas de backup externas sejam perfeitamente integradas com o RMAN. Consequentemente,os administradores do banco de dados podem continuar a usar suas ferramentas de backup existentes (Enterprise Manager, scripts do RMAN e outros, etc.) para realizar backups em nuvem.
O módulo de nuvem do Oracle Secure Backup também poderá ser usado quando o banco de dados estiver sendo executado no Amazon Elastic Compute Cloud (EC2). Nesse caso, ele se beneficia da maior largura de banda da rede interna e da ausência de custos de transferência para dentro ou para fora do S3. O módulo de nuvem do OSB está disponível para Linux 32 e 64,SPARC 64 e Windows 32.

A tecnologia reponsável por prover criptografia em bases de dados Oracle é chamadaTransparent Data Encryption (TDE). Ela é integrada ao RMAN e automaticamente criptografa dados escritos nos dispositivos de armazenamento e os decripta quando solicitados pela base de dados, após esta passar pela autenticação do TDE.
O backup realizado salva somente os dados, sendo capaz de ignorar os blocos não utilizados no banco de dados. Por produzir backups menores, gera melhor desempenho.
Gabarito: E

20. BANCA: FCC-Analista (DPE RS)/lnformática/2013

Sobre arquitetura do SGBD Oracle, considere:

I. Os componentes principais de um servidor corporativo típico são uma ou mais CPUs,
espaço em disco e memória. Enquanto o banco de dados Oracle é armazenado em um disco do servidor, uma instância Oracle existe na memória do servidor.
II. Os arquivos de dados em um BD Oracle são agrupados em uma ou mais tablespaces. Dentro de cada tablespace as estruturas lógicas do banco de dados, como tabelas e índices, são segmentos subdivididos em ainda mais extensões e blocos.
III. Um tablespace Oracle consiste em um ou mais arquivos de dados. Um arquivo de dados pode ser parte de mais de um tablespace. Numa instalação do Oracle são criados no mínimo 6tablespaces em vários bigfile tablespaces para facilitar o gerenciamento pelo DBA Oracle.

Está correto o que consta APENAS em a) II e III.
b) I e III.

c) I.

d) III.

e) I e II.

Comentário: Os itens I e II estão corretos. Já o item III está errado, pois um ou mais arquivos de dados são criados explicitamente para cada tablespace, visando armazenar fisicamente os dados de todas as estruturas lógicas em um espaço de tabela.
Cada banco de dados Oracle contém uma tablespace SYSTEM e uma tablespace SYSAUX. O
Oracle cria automaticamente cada tablespace quando o banco de dados é criado. O padrão do sistema é criar uma smallfile tablespace, que é o tipo tradicional de tablespaceOracle. As tablespaces SYSTEM e SYSAUX são criados como espaços de tabela smallfile.
Gabarito: E

21. BANCA: FCC - Analista Ministerial (MPE MA)/Banco de Dados/2013

Quando uma base de dados é criada no Sistema Gerenciador de Bancos de Dados Oracle,
são criadas, automaticamente, duas contas administrativas, cujas denominações são a) FILE e SNAME.
b) FORCE e MAXLOG.

c) SQLU e ROLL.

d) SYSe SYSTEM.

e) SIDeSGA.

Comentário: Cada banco de dados Oracle contém uma tablespace SYSTEM e uma tablespace
SYSAUX. O Oracle cria automaticamente cada tablespace quando o banco de dados é criado. O

padrão do sistema é criar uma smallfile tablespace, que é o tipo tradicional de tablespaceOracle. As tablespaces SYSTEM e SYSAUX são criados como espaços de tabela smallfile.

Gabarito: D

22. BANCA: FCC ANO: 2012 ÓRGÃO: TRE-CE PROVA: TÉCNICO DO JUDICIÁRIO - PROGRAMADOR DE
SISTEMAS

Sobre os mecanismos de segurança do banco de dados Oracle é correto afirmar:

A Como os papéis permitem o gerenciamento mais fácil e mais eficaz dos privilégios, eles podem ser concedidos a outros papéis.
B A única forma de atribuir privilégios a um usuário é por meio de papéis.

C Privilégios para criar um tablespace ou para excluir linhas de qualquertabela do banco de dados não são considerados privilégios de sistema.
D Todo usuário de um banco de dados pode acessar qualquer esquema desse banco, sem restrições.
E Um domínio de segurança no Oracle permite determinar papéis e privilégios para um usuário,
entretanto, não permitem definir cotas de tablespaces e limite de recursos da CPU.

Comentário. Um privilégio é um direito para executar um determinado tipo de instrução
SQL
ou para acessar objeto de outro usuário. O Oracle Database tem dois tipos de privilégios. Oprivilégio de sistema que pode ser concedido/revogado pelo DBA (CREATE TABLE, ALTER USER,
CREATE TRIGGER) e privilégio de objetos de schema, concedido/revogado pelo proprietário do objeto (SELECT, INSERT, UPDATE).
Em organizações muito grandes, com criação/exclusão frequentes de usuários que acessam o banco de dados, pode ser útil a implementação de outro tipo de permissão: papeis ou roles.Roles são grupos de privilégios relacionados que você concede a usuários ou outro papel. As roles são projetadas para facilitar a administração do sistema.
Funciona assim: o DBA cria um papel e concede a ele todos os privilégios que um usuário de um determinado setor da empresa precisaria para acessar/manipular os dados. Assim, quando ocorrer a contratação do próximo funcionário, o DBA não precisa atribuir novamente todas as permissões a esse usuário, mas simplesmente colocá-lo na role (papel) do setor.
Cada banco de dados Oracle tem uma lista de nomes de usuário. Para acessar um banco de dados, o usuário deve usar um aplicativo de banco de dados e tentar uma conexão com um nome de usuário válido do banco de dados. Cada nome de usuário tem uma senha associada para impedir o uso não autorizado. Cada usuário possui também um domínio de segurança,um conjunto de propriedades que determinam coisas como: as ações (privilégios e papeis)
disponíveis para o usuário, as quotas de tablespace (espaço em disco disponível) e os limites de recursos do sistema (por exemplo, o tempo de processamento da CPU) para o usuário.
Analisando as alternativas, observamos que o texto acima descreve exatamente o que está exposto na alternativa A. As demais letras possuem erros. A letra B diz que só podemos atribuir privilégios por meio de papeis, mas sabemos que é possível adquirir privilégios sobre objetos e funções diretamente por meio do comando GRANT. Na alternativa C, temos um privilégio de objetos (DELETE), que não pode ser, portanto, um privilégio de sistema. A alternativaD está incorreta, pois para acessar um esquema é necessário ter a permissão de SELECT sobre o mesmo. Por fim, a letra E também está errada, pois no domínio de segurança é possível definir cotas de tablespaces e limite de recursos da CPU. Vamos agora falar de outras características do subsistema de segurança do Oracle que provém ainda os seguintes mecanismos:
Contas de usuário. Quando você cria contas de usuário, você pode garantir segurança de uma variedade de maneiras. Você também pode criar perfis de senha para as políticas de senha mais seguras para o seu site.
Métodos de autenticação. O Banco de Dados Oracle fornece várias maneiras de configurar a autenticação para usuários e administradores de banco de dados. Por exemplo, você pode autenticar usuários no nível de base de dados a partir de protocolos do sistema operacional ou de informações de login de rede.
Privilégios e roles. Você pode usar privilégios e papéis para restringir o acesso do usuário aos dados. Falamos sobre eles acima.
Segurança do aplicativo. O primeiro passo para a criação de um banco de dados de aplicação é assegurar que ele é adequadamente protegido.
Acesso ao banco de dados no nível de linha e coluna usando Virtual Private Database.
Uma política de Banco de Dados pode usar essa ferramenta para incluir dinamicamente um predicado WHERE em instruções SQL.
Encryption. É possível criptografar os dados sobre a rede para evitar o acesso não autorizado.

Atividades de auditoria. Você pode auditar as atividades de banco de dados em termos gerais,como auditar todas as instruções SQL, privilégios SQL, objetos de esquema e atividade de rede.Ou, você pode auditar de forma granular, por exemplo, saber se endereços IP de fora da rede corporativa estão sendo usados.
Vejam abaixo uma figura que mostra as características de segurança do Oracle. Podemos incluir dentro da nossa explanação o redaction, que não permite que uma informação seja lida por completo por um grupo de usuário. Por exemplo, a atendente de telemarketing não pode ver meu CPF completo no sistema. Temos ainda a possibilidade de Masking, que ajuda a trazer parte dos dados de produção para ambientes de teste, contudo, ele aplica uma máscara que modifica os valores.
23. BANCA: FCC ANO: 2012 ÓRGÃO: TRE-CE PROVA: ANALISTA JUDICIÁRIO - ANALISTA DE
SISTEMAS

Visão do Oracle 10g que apresenta uma lista das diferentes métricas que dão uma estimativa da saúde do banco de dados e especifica uma condição sob a qual um alerta será emitido se a métrica alcançar o limiar ou exceder um valor especificado. Trata-se de
A DB_RECOVERY_FILE_DEST.
B DBA_TABLESPACES.

C DBA_THRESHOLDS.
D DBA_FREE_SPACE.
E DBA_SEGMENTS.

Comentário. Analisando cada uma das alternativas, temos:

DB_RECOVERY_FILE_DEST especifica o local padrão para a área de recuperação rápida. Essa área contém cópias multiplexados de arquivos atuais de controle e de logs de redo on-line,bem como os redo logs, logs de flashback, e backups do RMAN.

í DBA_TABLESPACES descreve todos os tablespaces de um banco de dados.

i DBA_THRESHOLDS descreve todos os limites configurados de um banco de dados, tais como:nome da métrica, operador de alarme, valor de alarme, operador crítico, valor crítico,
período de observação, ocorrências consecutivas, nome da instância, tipo de objeto, nome do objeto e estado.
DBA_FREE_SPACE descreve os extents livres em todos os tablespaces do banco de dados.

DBA_SEGMENTS descreve a quantidade de armazenamento alocada para todos os seguimentos (segments) no banco de dados.
Vejam, portanto, que confirmamos a resposta na alternativa C.

Gabarito: C

24. BANCA: FCC - Analista Judiciário (TST)/ Apoio Especializado/ Suporte em Tecnologia da lnformação/2012
Um banco de dados criado por meio do SGBD dados Oracle, versão llg, tem uma estrutura lógica e física peculiares, tendo como característica:
a) um segmento contém exatamente uma extensão.

b) o tablespace não comporta mais de um datafile.

c) um mesmo tablespace pode ser utilizado por vários bancos de dados, simultaneamente.

d) o banco de dados pode conter um ou mais tablespaces.

e) um segmento pode ser dividido em vários tablespaces.

Comentário. Para responder essa questão, nós precisamos entender as estruturas lógicas de armazenamento. O Oracle aloca espaços lógicos para todos os dados no banco de dados.As unidades lógicas para alocação de espaço no banco de dados são os data blocks,extents,
segments, e os tablespaces. Fisicamente, os dados são armazenados em arquivos de dados no disco.
Existe uma hierarquia lógica de armazenamento que pode ser vista na figura abaixo. Do nível mais baixo até o nível mais alto de armazenamento, temos: Oracle Data block, Extent,Segment e Tablespace. Em outras palavras, podemos dizer que: um extent é formado por um ou mais data blocks; um segment é formado por um ou mais extents; um tablespace é formado por um ou mais segments.
Data Blocks

Vamos agora analisar e definir cada uma das estruturas:

Data Blocks - O Oracle gerencia seu espaço de armazenamento lógico no arquivo de dados em unidades chamadas data blocks, também conhecidas como Oracle blocks ou pages. Um data block é a menor unidade de entrada e saída do banco de dados. No nível físico, os dados são armazenados em disco, de acordo com os blocos do sistema de arquivos do sistema operacional. Um bloco para o sistema operacional é a menor unidade de dados que pode ser lida ou escrita pelo sistema operacional. Por outro lado, um Oracle block é uma estrutura lógica de armazenamento cujo tamanho e estrutura não são conhecidos pelo sistema operacional.
Extents - Uma extensão é uma unidade de armazenamento lógico construída a partir de blocos contínuos. Os Data blocks em uma extent são logicamente contínuos, mas podem ser fisicamente dispersos.
Segments - Um segment é composto por um conjunto de extents que contém todos os dados de sua estrutura lógica dentro de um tablespace. Por exemplo, o Oracle aloca um ou mais extents para um segmento de dados de uma tabela. O banco de dados também aloca um ou mais extents para formar um segmento de índice para uma tabela.
Tablespaces - Um tablespace é uma estrutura de armazenamento lógico que contém segmentos. Segmentos são objetos de banco de dados, como tabelas e índices que consomem espaço. No nível físico, um tablespace armazena dados em um ou mais arquivos de dados ou arquivos temporários de dados.
Pelo menos dois tablespaces são obrigatórios no Oracle: SYSTEM e SYSAUX. Além destes dois tablespaces, o banco de dados Oracle é dividido em um ou mais tablespaces. Essa é a nossa resposta, que pode ser encontrada na letra D.
Gabarito: D

25. BANCA: FCC - Analista Judiciário (TRE CE)/ Apoio Especializado/ Análise de Sistemas/2012

No banco de dados Oracle 10g, os segmentos a) são as unidades mais básicas de armazenamento dentro das tuplas.
b) são as menores unidades de armazenamento, também chamados tablespaces.

c) estão um nível acima na hierarquia dos agrupamentos lógicos ou grids.

d) são agrupados em uma ou mais estruturas lógicas que são as views.

e) contêm todos os dados de um agrupamento lógico dentro de um tablespace.

i Comentário. Apenas relembrando, um segmento é composto por um conjunto de extents,
que contém todos os dados em uma estrutura lógica dentro de um tablespace. Por exemplo, oOracle aloca um ou mais extents para um segmento de dados de uma tabela.

O banco de dados também aloca um ou mais extents para formar um segmento de índice para uma tabela. Se a tabela ou o índice estiver particionado, cada partição é armazenada no seu próprio segmento. É possível ainda termos os segmentos conhecidos como temporários, que são utilizados quando o SGBD faz algum armazenamento intermediário durante o processamento da consulta.
A resposta da nossa questão está na alternativa E. Ela afirma, em outras palavras,
que o agrupamento de segmentos logicamente relacionados está dentro de um tablaspace.
Gabarito: E

26. BANCA: FCC - Analista Judiciário (TRE PE)/Apoio Especializado/Análise de Sistemas/2011

O processo de background Oracle que executa a recuperação, se necessário, na inicialização da instância e que é responsável pela limpeza dos segmentos temporários que não estão mais em uso é o a) Process Monitor Process (PMON).
b) Checkpoint Process (CKPT).

c) System Monitor Process (SMON).

d) Log Writer Process (LGWR).

e) Recoverer Process (RECO).

Comentário: O gabarito é a letra C), pois o processo System Monitor (SMON) verifica a consistência no banco de dados, localizando e validando o arquivo de controle no momento em que o banco é montado e, se necessário, inicia a recuperação do banco de dados quando ele é aberto. Além desta funcionalidade, o SMON é responsável por unir espaços livres nos tablespaces, se eles forem gerenciados pelo dicionário.
Gabarito: C

27. BANCA: FCC - Analista Judiciário (TRE PE)/Apoio Especializado/ Análise de Sistemas/2011

Contém apenas estruturas de armazenamento lógico do banco de dados Oracle:

a) data blocks, extents e segments.

b) datafiles, extents e segments.

c) datafiles, redo log files e control files.

d) datafiles, data blocks e control files.

e) control files, redo log files e data blocks.

Comentário: Temos como gabarito a letra a). As unidades de alocação de espaço do banco de dados são blocos de dados, extensões e segmentos.
Data blocks: No nível mais refinado de granularidade, o Oracle Database armazena dados em blocos de dados (também chamados de blocos lógicos, blocos do Oracle ou páginas). Um bloco de dados corresponde a um número específico de bytes do espaço físico do banco de dados no disco.
Extents: O próximo nível de espaço lógico do banco de dados é uma extensão. Uma extensão é um número específico de blocos de dados contíguos alocados para armazenar um tipo específico de informação.
Segments: O nível de armazenamento lógico do banco de dados maior que uma extensão é chamado de segmento. Um segmento é um conjunto de extensões, cada uma das quais foi alocada para uma estrutura de dados específica e todas elas são armazenadas no mesmo espaço de tabela. Por exemplo, os dados de cada tabela são armazenados em seu próprio segmento de dados, enquanto os dados de cada índice são armazenados em seu próprio segmento de índice. Se a tabela ou índice estiver particionado, cada partição será armazenada em seu próprio segmento.
Gabarito: A

28. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/Administrador de Banco de Dados/2010

As entradas da estrutura física do database ORACLE 10g são especificadas no a) Control file.
b) Data file.

c) Parameter file.

d) Archive log file.

e) Redo log file.

Comentário: O gabarito é letra a), pois um arquivo de controle contém informações sobre o banco de dados associado que é necessário para acesso por uma instância,tanto na inicialização quanto durante a operação normal. As informações do arquivo de controle podem ser modificadas apenas pelo Oracle Database; nenhum administrador de banco de dados ou usuário pode editar um arquivo de controle. Entre outras coisas, um arquivo de controle contém informações como:
* O nome do banco de dados

* O registro de data e hora da criação do banco de dados

* Os nomes e localizações de arquivos de dados associados e arquivos de redo log

* Informação de espaço de tabelas

* Intervalos offline de arquivos de dados

* O histórico de log

* Informação de log arquivada

* Conjunto de backup e informações de peça de backup

* Arquivo de dados de backup e informações de log de redo

* Informações de cópia do arquivo de dados

* O número de sequência do log atual

* Informação do ponto de verificação

Gabarito: A

29. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/ Administrador de Banco de Dados/2010

A sequência, do menor para o maior nível de granulidade, das unidade de alocação de espaço no
ORACLE 10g é (extent, data block e segment).

a) segment, data block e extent.

b) data block, extent e segment.

c) segment, extent e data block.

d) data block, segment e extent.

Comentário: Temos como gabarito a letra c). As unidades de alocação de espaço do banco de dados são blocos de dados, extensões e segmentos.
Data blocks: No nível mais refinado de granularidade, o Oracle Database armazena dados em blocos de dados (também chamados de blocos lógicos, blocos do Oracle ou páginas). Um bloco de dados corresponde a um número específico de bytes do espaço físico do banco de dados no disco.
Extents: O próximo nível de espaço lógico do banco de dados é uma extensão. Uma extensão é um número específico de blocos de dados contíguos alocados para armazenar um tipo específico de informação.
Segments: O nível de armazenamento lógico do banco de dados maior que uma extensão é chamado de segmento. Um segmento é um conjunto de extensões, cada uma das quais foi alocada para uma estrutura de dados específica e todas elas são armazenadas no mesmo espaço de tabela. Por exemplo, os dados de cada tabela são armazenados em seu próprio segmento de dados, enquanto os dados de cada índice são armazenados em seu próprio segmento de índice. Se a tabela ou índice estiver particionado, cada partição será armazenada em seu próprio segmento.
Gabarito: C

30. BANCA: FCC - Analista do Ministério Público de Sergipe/lnformática l/Gestão e Análise de
Projeto de lnfraestrutura/2010

Strings de caracteres de tamanho fixo são armazenados em um banco de dados ORACLE por meio do tipo de dados a) char ou nchar.
b) varchar ou nvarchar.

c) char ou varchar2.

d) varchar ou varchar2.

e) nchar ou nvarchar.

Comentário: O gabarito é a letra a). O tipo de dados CHAR armazena cadeias de caracteres de comprimento fixo. Ao criar uma tabela com uma coluna CHAR, você deve especificar um comprimento de cadeia (em bytes ou caracteres) entre 1 e 2.000 bytes para a largura da colunaCHAR.

NCHAR e NVARCHAR2 são tipos de dados Unicode que armazenam dados de caracteres
Unicode. O conjunto de caracteres dos tipos de dados NCHAR e NVARCHAR2 pode ser apenas
AL16UTF16 ou UTF8 e é especificado no momento da criação do banco de dados como o conjunto de caracteres nacional. AL16UTF16 e UTF8 são ambos codificação Unicode.
O tipo de dados NCHAR armazena cadeias de caracteres de comprimento fixo que correspondem ao conjunto de caracteres nacional.
O tipo de dados NVARCHAR2 armazena cadeias de caracteres de comprimento variável.

Gabarito: A

31. BANCA: FCC Analista do Ministério Público de Sergipe/ Informática l/Gestão e Análise de
Projeto de lnfraestrutura/2010

Uma instância do banco de dados ORACLE é constituída a) pela área global do sistema (SGA) e pelos processos user, server e background.
b) pelos processos user, server e background, apenas.

c) pelos processos user e server, apenas.

d) pela área global do sistema (SGA) e pelos processos background, apenas.

e) pela área global do sistema (SGA) e pelos processos user, apenas.

Comentário: O gabarito é a letra d), pois uma instância é formada pela área global do sistema(SGA) e pelos processos background. Todo banco de dados Oracle em execução é associado a uma instância de banco de dados Oracle. Quando um banco de dados é iniciado em um servidor de banco de dados (independentemente do tipo de computador), o Oracle aloca uma área de memória chamada Área do Sistema Global (SGA) e inicia um ou mais processos de banco de dados Oracle. Esta combinação da SGA e dos processos Oracle é chamado de uma instância Oracle. A memória e os processos de uma instância gerenciam os dados do banco associado de forma eficiente e serve a um ou vários usuários de banco de dados.
Gabarito: D

32. BANCA: FCC - Analista do Ministério Público de Sergipe/lnformática l/Gestão e Análise de
Projeto de lnfraestrutura/2010

O modo de execução no qual o ORACLE copia os online redo logs cheios para o disco é denominado a) commit.
b) rolling back.

c) rolling forward.

d) checkpoint.

e) archivelog.

Comentário: O gabarito é a letra e), pois o ARCHIVELOG mode é modo do banco de dados no qual as cópias do Oracle Database preencheram os redo logs on-line para o disco.Especifique o modo na criação do banco de dados ou usando a instrução ALTER DATABASE. Você pode ativar o arquivamento automático dinamicamente usando a instrução ALTER SYSTEMou definindo o parâmetro de inicialização LOG_ARCHIVE_START como TRUE.
Executar o banco de dados no modo ARCHIVELOG tem várias vantagens sobre o modoNOARCHIVELOG. Você pode:

Fazer backup do banco de dados enquanto ele estiver aberto e sendo acessado pelos usuários.

Recuperar o banco de dados para qualquer ponto desejado no tempo.

Para proteger o banco de dados do modo ARCHIVELOG em caso de falha, faça backup dos logs arquivados.
Gabarito: E

33. BANCA: FCC - Analista do Ministério Público de Sergipe/ Informática l/Gestão e Análise de
Projeto de lnfraestrutura/2010

NÃO se trata de um componente da estrutura lógica de um banco de dados ORACLE:

a) tablespaces.

b) schema objects.

c) control files.

d) data blocks.

e) segments.

Comentário: O gabarito é a letra c), pois os arquivos de controle fazem parte da estrutura física de um banco de dados. Cada banco de dados Oracle tem um arquivo de controle. Um arquivo de controle contém entradas que especificam a estrutura física do banco de dados. Por exemplo, ele contém as seguintes informações:
* Nome do banco

* Nomes e localizações de arquivos de dados e arquivos de log de redo

* Carimbo de tempo da criação de banco de dados

Gabarito: C

34. BANCA: FCC ANO: 2009 ÓRGÃO: TRT - 15§ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

São apenas tipos de objetos de um schema Oracle:

A table, index, cluster e profile.
B table, index, cluster e view.

C table, tablespace, index e cluster.

D tablespace, index, cluster e directory.
E tablespace, index, cluster e view

Comentário. Um esquema é um conjunto de estruturas lógicas de dados ou objetos de esquema. Um esquema é de propriedade de um usuário de banco de dados e tem o mesmo nome do usuário. Cada usuário possui um único esquema. Objetos de esquema podem ser criados e manipulados com SQL e incluem os seguintes tipos de objetos: Clusters,Database links, Database triggers, Indexes e index types, Mate ria lized views and materialized view logs,Sequences, Stored functions, procedures, and packages, Synonyms, Tables,
index-organized tables, Views.
Gabarito: B

35. BANCA: FCC ANO: 2009 ÓRGÃO: TRT - 15^ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

Cada database Oracle tem

I. um ou mais datafiles.

II. um control file.

III. um conjunto de dois ou mais redo log files.
Está correto o que consta em

A I, II e III.

B I, somente.
C II, somente.

D I e II, somente.
E I e III, somente.

Comentário. Vamos analisar as quantidades de cada um dos arquivos.

Um espaço de tabela em um banco de dados Oracle consiste em um ou mais arquivos de dados físicos. Um arquivo de dados pode ser associado com apenas uma tabela e apenas um banco de dados. Vejam que podemos ter um ou mais datafiles em uma instância do Oracle
O arquivo de controle de banco de dados é um pequeno arquivo binário necessário para o banco de dados iniciar e operar com sucesso. Um arquivo de controle é atualizado continuamente pelo Oracle Database durante a utilização do banco de dados, por isso deve estar disponível para escrita sempre que o banco de dados estiver aberto. Se por algum motivo o arquivo de controle não está acessível, então o banco de dados não pode funcionar corretamente. Cada arquivo de controle é associado a apenas um banco de dados Oracle.
O log redo de um banco de dados consiste em dois ou mais arquivos de log de redo. O banco de dados requer um mínimo de dois arquivos para garantir que um está sempre disponível para escrever, enquanto o outro está sendo arquivado (se o banco de dados está no modoARCHIVELOG).

Gabarito: A

36. BANCA: FCC ANO: 2008 ÓRGÃO: TRT - 2? REGIÃO (SP) PROVA: ANALISTA JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

O Oracle copiará os arquivos online redo logs cheios para o disco se a base de dados estiver em execução no modo
A undo.

B restricted.
C dedicated.
D archivelog.
E backup.

Comentário. A principal estrutura para as operações de recuperação é o log de redo,
que consiste em dois ou mais arquivos pré-alocados. Eles armazenam todas as alterações feitas ao banco de dados à medida que ocorrem. Cada instância de um banco de dados Oracle tem um log de redo associado, visando proteger o banco de dados em caso de falha na instância doSGBD.

O Oracle Database permite que você salve grupos de arquivos de log de redo cheios em um ou mais destinos off-line, conhecidos coletivamente como o archived redo log. O processo de transformar arquivos de log de redo em arquivos de log redo arquivados é chamado de arquivamento (archiving). Este processo só é possível se o banco de dados estiver sendo executado no modo ARCHIVELOG. Você pode escolher entre o arquivamento automático ou manual.
Caso o seu banco de dados esteja operando em ARCHIVELOG Mode, ele habilita o arquivamento do redo log. O arquivo de controle do banco de dados indica que um grupo de arquivos redo log cheios não podem ser reutilizados pelo LGWR (Log Writer) até que o grupo seja arquivado.
A outra opção seria usar o NOARCHIVELOG Mode, que não permite o processo de archiving.
Utilizando o modo NOARCHIVELOG, você somente poderá executar backups se o banco de dados estiver off-line. Para restaurar um banco de dados operando em NOARCHIVELOG Mode,você deverá utilizar backups efetuados quando o banco de dados estiver fechado (closed).
Portanto, se você decidir operar um banco de dados em NOARCHIVELOG Mode, faça backups completos em intervalos regulares e frequentes.
Vejam que, após entendermos as opções para arquivamento do log de redo, podemos marcar a alternativa D.
Gabarito: D

37. Ano: 2018 Banca: CESPE Órgão: STM Cargo: Analista de Sistemas Questão: 74

Um sistema gerenciador de banco de dados (SGBD) instalado no Linux deve ser configurado de modo a permitir os seguintes requisitos:
I no máximo, 1000 conexões simultâneas;

II somente conexões originadas a partir do servidor de aplicação com IP 10.10.10.2.
Tendo como referência essas informações, julgue os seguintes itens.

74 Caso o SGBD instalado seja o Oracle 12C, os requisitos I e II podem ser atendidos em tempo de execução, respectivamente, por meio dos comandos SET system sessions = 1000 e SETsystem listener = 10.10.10.2.
Comentário: Primeiramente, para alterar o parâmetro que define a quantidade de sessões,
usamos o comando ALTER SYSTEM SET SESSIONS = 1000. Assim, essa alternativa já está errada.
Ainda no servidor de banco de dados Oracle, o Oracle Net usa um processo ativo chamado listener para gerenciar conexões entre as aplicações e o servidor de Banco de Dados.As aplicações (remotas) não podem se conectar ao servidor de BD sem um listener. Um único listener pode servir múltiplas instâncias de BD e milhares de conexões clientes. Segue abaixo um exemplo de conteúdo do arquivo de configuração do listener, chamado listener.ora:
## listener.ora Network Configuration File:

LISTENER = (DESCRIPTION_LIST =
(DESCRIPTION =

(ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521)))

Gabarito: E

38. Ano: 2018 Banca: CESPE Órgão: STM Cargo: Analista de Sistemas Questões: 83 a 85

Acerca do Oracle 12C, julgue os próximos itens.

83 Especialmente voltado para o armazenamento de dados de sistemas de suporte a decisão(DSS) e data warehouse, os dados no Oracle podem ser armazenados em uma nova área opcional denominada In-Memory (IM). A IM é um suplemento que substitui a system global area(SGA),
pois se sobrepõe ao cache de buffer do banco de dados, permitindo alto poder de processamento ao varrer dados colunares rapidamente por meio de vetorização.
84 Os dados nos SGBDs são organizados em blocos, em que os sistemas de suporte à decisão(DSS) e os ambientes de banco de dados de data warehouse tendem a se beneficiar de valores de tamanho de bloco maiores.
85 Os blocos de dados são organizados em cabeçalho (row header) e dados (column data); a cada nova transação, o registro é armazenado como uma nova linha na tabela e, assim, um registro é armazenado em várias colunas em blocos de dados no disco.
Comentário: Vamos comentar cada uma das alternativas:

83. Vamos começar relembrando alguns conceitos. Uma Instância Oracle contém memória e conjunto de processos em background. A memória é dividida em duas áreas distintas: System
Global Area (SGA) e Program Global Area (PGA). O Oracle cria processos servidores para lidar com os pedidos de processamento dos usuários conectados à instancia. Uma das mais importantes tarefas do Processo Servidor: ler blocos de dados de objetos a partir de datafile dentro de um buffer do banco de dados que, por padrão, armazena os dados no buffer cache do banco de dados Oracle em formato de linha.
A partir do 12c, o Oracle Database Release 1 (12.1.0.2) adicionou uma nova área opcional naSGA chamado de In-Memory, que são objetos armazenados com o novo formato In-Memory
Column Store (IM column store). A IM Column store é opcional e armazena cópias das tabelas,partitions, colunas, materialized views (objetos especificados como INMEMORY usando DDL)
em um formato especial de colunas otimizadas para leituras rápidas.

A IM column store é um suplemento em vez de ser um substituto para o cache de buffer do banco de dados. A IM column store não substitui o buffer cache. Mas ambas as áreas de memória podem armazenar os mesmos dados em formatos diferentes e não é necessário para objetos armazenados na IM column store serem carregados no buffer cache do banco de dados, ou seja, os objetos são armazenados unicamente na IM column store. Sendo assim,temos uma afirmação incorreta.

Memory Memory

SALES SALES

Row Format Column Forrnat í SALES I
84. Um bloco é um conjunto contíguo de bits ou bytes que forma uma unidade de dados identificável. Em alguns bancos de dados, um bloco é a menor quantidade de dados que um programa pode solicitar. É um múltiplo de um bloco do sistema operacional, que é a menor quantidade de dados que podem ser recuperados do armazenamento ou da memória. Vários blocos em um banco de dados compreendem uma extensão.
No Oracle, o valor do DB_BLOCK_SIZE em vigor quando você cria o banco de dados determina o tamanho dos blocos. O valor deve permanecer definido como seu valor inicial. ParaReal
Application Clusters, este parâmetro afeta o valor máximo do parâmetro de armazenamento
FREELISTS para tabelas e índices. O Oracle usa um bloco de banco de dados para cada grupo freelist. O sistema de suporte à decisão (DSS) e os ambientes de banco de dados de data warehouse tendem a se beneficiar de valores de tamanho de bloco maiores.
85. Afigura abaixo descreve um bloco de arquivos no Oracle. Veja que existe um cabeçalho de bloco, que contém o endereço do bloco de dados, o diretório da tabela e o diretório da linha e os slots de transação usados quando as transações fazem alterações em linhas do bloco.Esses cabeçalhos crescem de cima para baixo. Temos também os espaços de dados, esses dados de colunas são inseridos no bloco de baixo para cima. Veja que, quando inserirmos os dados, eles serão armazenados nos registros em tabelas organizadas em linhas por colunas e estruturadas em blocos.
Row Header Column Data

Row Piece in a Database Block

I Common and Variable Header
H Table Directory

- Row Directory
I Free Space

- Row Data

Row Overhead
Number of Columns

Cluster Key ID (lf clustered)

ROWID of Chained Row Pieces (lf any)
Column Length

Column Value

Database
Block

Gabarito: E C C

39. BANCA: Cespe - Analista Judiciário (TRT Região)/Apoio Especializado/Tecnologia da lnformação/2016
Julgue o item seguinte, relativo ao banco de dados Oracle.

AWR (automatic workload repository) é um repositório de informações de estatísticas de desempenho que possibilita a detecção de problemas.
Certo
Errado

Comentário: A questão está correta. O AWR (Automatic Workload Repository,
Repositório
Automático de Carga de Trabalho) é um repositório interno que contém estatísticas de desempenho usadas pelo Banco de Dados Oracle para fins de detecção de problemas e autoajuste. Em intervalos regulares, o Oracle Database faz uma verificação instantânea de estatísticas vitais e informações de carga de trabalho e as armazena no AWR. Os dados contidos no AWR são analisados pelo Automatic Database Diagnostic Monitor (ADDM).
Gabarito: C

40. BANCA: Cespe - Analista Judiciário (TRT 8- Região)/Apoio Especializado/Tecnologia da lnformação/2016
Assinale a opção referente ao arquivo que grava todas as mudanças realizadas no DataBase e que é utilizado somente para recuperação de uma instância em um SGBD Oracle.
a) Parameter log file b) Archive log file c) Undo file d) Control file e) Alert log file
Comentário: O gabarito é a letra b). Os archiver processes (ARCn) copiam os arquivos de redo log para um dispositivo de armazenamento designado após a ocorrência de um log alternativo.Além disso, eles podem coletar dados de redo de transação e transmitir esses dados para destinos em espera. Os processos ARCn estão presentes apenas quando o banco de dados está no modo ARCHIVELOG e o arquivamento automático está ativado.
Gabarito: B

41. BANCA: Cespe - Analista Administrativo (ANTT)/Tecnologia da Informação/lnfraestrutura de
TI/2013

No que se refere ao sistema de gerenciamento de banco de dados (SGBD) Oracle e ao sistema operacional Linux, julgue o item seguinte.
No Oracle, uma das vantagens de se utilizar o ASM (automatic storage management) é a possibilidade de adição de um novo dispositivo de disco ao banco de dados sem o desligamento deste.
Certo
Errado

Comentário: A questão está correta. O Automatic Storage Management é uma solução de gerenciamento de armazenamento de alto desempenho para arquivos do Oracle Database. Ele simplifica o gerenciamento de um ambiente de banco de dados dinâmico, com a criação e o layout de bancos de dados e o gerenciamento de espaço em disco.
Gabarito: C

42. BANCA: CESPE ANO: 2012 ÓRGÃO: TJ-RO PROVA: ANALISTA JUDICIÁRIO - DESENVOLVIMENTO
DE SISTEMAS

Assinale a opção correta acerca das ferramentas, dos recursos e das características do
SGBD
Oracle 10.

A Por meio do recurso OSS (Oracle segment shrink) do Oracle 10g, pode-se compactar áreas de memória RAM marcadas como booked, transferindo-as para o disco, permitindo, assim, maior alocação de memória no processamento de consultas.
B lOTs (index organized tables) são estruturas de dados que permitem armazená-los de forma organizada com seus índices.
C DRM (database resource manager), uma área interna do Oracle 10g, é utilizada pelo tuning optimizer para prover recomendações de consultas SQL e criar índices, com o objetivo de melhorar o desempenho da recuperação de dados.
D Oracle 10g flashback é um conjunto de ferramentas mediante as quais é possível gerenciar e agendar a criação de becapes utilizando-se comandos RMAN.
E O Oracle 10g ADDM (automatic database diagnostic monitor), por intermédio do pacoteDBMS_SCHEDULER, gerencia triggers de sistemas e permite a autocriação de índices, a fim de melhorar o desempenho de acesso aos dados de forma programada.
Comentário. Cada uma das alternativas acima trata de uma ferramenta, um recurso ou uma característica do Oracle. Já falamos sobre algumas delas. Vamos apresentar um resumo abaixo para melhorar nosso entendimento.
Oracle segment shrink-Você pode usar redução de segmento on-line para recuperar o espaço livre fragmentado abaixo da marca de água alta em um segmento de banco de dadosOracle.
Os benefícios da redução de segmento são estes: 1. Compactação de dados que leva a uma melhor utilização do cache, que por sua vez leva a um melhor desempenho de processamento de transações online (OLTP). 2. Os dados compactados exigem menos blocos a serem verificados em varreduras de tabela inteira, que por sua vez leva a um melhor desempenho do sistema de apoio à decisão (DSS).
Redução de segmento é uma operação on-line local. Operações e consultas DML podem ser emitidas durante a fase de movimentação de dados de redução de segmento. Operações DMLsimultâneas são bloqueadas por um curto período de tempo no final da operação de redução,quando o espaço é desalocado. Os índices são mantidos durante a operação de redução e permanecem utilizáveis após a operação estiver sido concluída. Redução de segmento não requer espaço em disco extra.
Uma tabela organizada por índice (IOT) é um tipo de tabela que armazena dados em uma estrutura de índice B*tree. Tabelas relacionais normais, chamadas de tabelas organizadas por heap, armazenam registros em qualquer ordem. Em contraste, tabelas organizadas por índice armazenam registros em uma estrutura de índice B-tree, que é logicamente classificada na mesma ordem de chave primária. Ao contrário de índices de chave primária normais, que armazenam somente as colunas incluídas na sua definição, os índices IOT armazenam todas as colunas da tabela.
O objetivo principal do Database Resource Manager é fornecer ao servidor do Oracle
Database mais controle sobre as decisões de gerenciamento de recursos, problemas relacionados à alocação de recursos podem gerar uma gestão ineficiente do banco de dados.
O Oracle 9i introduziu o pacote DBMS_FLASHBACK para permitir que as consultas façam referência a versões mais antigas do banco de dados. O Oracle 10g tomou esta tecnologia um passo adiante, tornando mais simples de usar e muito mais flexível. Vejam que não tem nenhuma relação com gerenciamento de backups, como sugeriu a alternativa D.
Falamos do ADDM em uma questão anterior. O Automatic Database Diagnostic Monitor
(ADDM) analisa os dados do AWR, diagnostica as causas dos problemas de desempenho,
fornece recomendações para corrigir quaisquer problemas e, ainda, identifica as áreas não problemáticas do sistema.
Gabarito: B

43. BANCA: Cespe - Analista Judiciário (TJ AL)/ Apoio Especializado/ Análise de Sistemas/2012

Acerca de planos de manutenção e tuning em banco de dados Oracle llg, assinale a opção correta.
a) O Oracle Enterprise Manager exibe os resultados da tarefa do SQL Access Advisor listando as instruções SQL pela ordem de maior redução de custo.
b) O SQL Access Advisor oferece recomendações de partição somente para cargas de trabalho que têm predicados e junções em colunas de tipo VARCHAR.
c) O SQL Plan Management evita que regressões de performance resultem de alterações repentinas no plano de execução de uma instrução SQL, mas não fornece componentes para captura e seleção de informações capazes de auxiliar na evolução dos planos de execução de SQL.
d) O Automatic Database Diagnostic Monitor (ADDM) não proporciona análise de performance de gerenciamento de backup/recuperação ou análise de performance em cluster para bancos de dados com real application clusters (RAC).
e) Em cada execução do SQL Tuning Advisor, o administrador do banco de dados deve selecionar as consultas SQL de alta carga no sistema e gerar recomendações sobre como ajustá-las.
Comentário: O gabarito é a letra a). O SQL Access Advisor recomenda o conjunto adequado de visualizações materializadas, logs de visualização materializados, partições e índices para uma carga de trabalho especificada.
Visões, partições e índices materializados são essenciais ao ajustar um banco de dados para obter um desempenho ideal para consultas complexas e intensivas de dados. O SQL AccessAdvisor toma uma carga de trabalho real como entrada ou deriva uma carga de trabalho hipotética de um esquema.
A execução do SQL Access Advisor mostra as recomendações, com sua classificação e benefício total. A classificação é uma medida da importância das consultas que a recomendação ajuda.
O benefício é a melhoria total no custo de execução (em termos de custo do otimizador) de todas as consultas, usando a recomendação.
Vamos às demais alternativas:

b) O SQL Access Advisor recomenda o conjunto adequado de visualizações materializadas,
logs de visualização materializados, partições e índices para uma carga de trabalho especificada.Não está restrito a cargas de trabalho que têm predicados e junções em colunas de tipoVARCHAR.

c) O SQL Plan Management permite que o otimizador gerencie automaticamente os planos de execução, garantindo que o banco de dados use somente planos conhecidos ou verificados.
d) O Automatic Database Diagnostic Monitor (ADDM) é um software de autodiagnóstico integrado ao Oracle Database. O ADDM examina e analisa os dados capturados no AWR(Automatic Workload Repository - Repositório Automático de Carga de Trabalho)
para determinar possíveis problemas de desempenho do banco de dados.
e) Quem é responsável por esta atividade é o O SQL Access Advisor.

Gabarito: A

44. BANCA: Cespe - Oficial Bombeiro Militar (CBM DF)/ Complementar/ Informática/ 2011

No que se refere ao banco de dados Oracle, julgue o próximo item.

Os espaços de tabela bigfile se adaptam melhor a um ambiente que utiliza ASM
(Automatic
Storage Management), OMF (Oracle Managed Files) e RMAN (Recovery Manager) com uma Flash
Recovery Area, permitindo, ainda, um tamanho de espaço de tabela tão grande quanto 8
milhões de terabytes, conforme o tamanho do bloco do espaço de tabela.
Comentário: A questão está correta. A Oracle também permite criar espaços de tabela bigfile.Isso permite que o Oracle Database contenha espaços de tabela formados a partir de poucos arquivos grandes em vez de vários menores. Isso ajuda ao Oracle Database utilizar a capacidade dos sistemas de 64 bits para criar e gerenciar arquivos do tipo ultralarge. Aconsequência disto é que o Oracle Database agora pode ser dimensionado para até oito exabytes de tamanho.
Vale ressaltar que, devido principalmente ao seu tamanho, os espaços de tabela bigfile se adaptam melhor a um ambiente que utiliza ASM (Automatic Storage Management),OMF
(Oracle Managed Files) e RMAN (Recovery Manager) com uma Flash Recovery Area.

Gabarito: C

45. BANCA: Cespe Analista (FINEP)/ Informática/ Desenvolvimento de Sistemas/2009

Uma das instâncias do sistema gerenciador de banco de dados Oracle 10g consiste de arquivos em disco, área de memória e processos em execução. Cada processo é responsável por um conjunto de atividades. Nessa versão do Oracle, o processo responsável por recuperar espaço em segmentos temporários quando estes não estão mais sendo utilizados é o a) DBW (database writer).
b) LGWR (log writer).

c) SMON (system monitor).

d) PMON (process monitor).

e) CKPT (check point).

Comentário: O gabarito é a letra c). O SMON (system monitor) executa a recuperação quando uma instância com falha é inicializada novamente. Em um banco de dadosOracle Real
Application Clusters, o processo SMON de uma instância pode executar a recuperação da instância para outras instâncias que falharam. O SMON também limpa os segmentos temporários que não estão mais em uso e recupera as transações inativas ignoradas durante a falha do sistema e a recuperação da instância devido a erros de leitura de arquivo ou offline.Essas transações são eventualmente recuperadas pelo SMON, quando o espaço de tabela ou o arquivo é colocado de volta online.
Vamos às demais letras:

a) DBW (database writer): Grava os blocos modificados do cache de buffer do banco de dados nos arquivos de dados. O banco de dados Oracle permite um máximo de 20 processos de gravação de banco de dados (DBW0-DBW9 e DBWa-DBWj). O parâmetro de inicializaçãoDB_WRITER_PROCESSES especifica o número de processos DBWn. O banco de dados seleciona uma configuração padrão apropriada para esse parâmetro de inicialização ou ajusta uma configuração especificada pelo usuário, com base no número de CPUs e no número de grupos de processadores.
b) LGWR (log writer): Grava as entradas de redo log no disco. As entradas de log de redo são geradas no buffer de redo log da área global do sistema (SGA). O LGWR grava as entradas de redo log sequencialmente em um arquivo de redo log. Se o banco de dados tiver um log de redo multiplexado, o LGWR gravará as entradas de redo log em um grupo de arquivos de redo log.
d) PMON (process monitor): Executa a recuperação do processo, quando um processo do usuário falha. O PMON é responsável por limpar o cache e liberar recursos que o processo estava usando. O PMON também verifica os processos do dispatcher e os processos do servidor e os reinicia, se eles falharem.
e) CKPT (check point): Em horários específicos, todos os buffers de banco de dados modificados na área global do sistema são gravados nos arquivos de dados por DBWn.Esse evento é chamado de ponto de verificação. O processo de ponto de verificação é responsável por sinalizar DBWn nos pontos de verificação e atualizar todos os arquivos de dados e arquivos de controle do banco de dados para indicar o ponto de verificação mais recente.
Gabarito: C

46. BANCA: FGV ANO: 2015 ÓRGÃO: TJ-SC PROVA: ANALISTA JUDICIÁRIO - ANALISTA DE SISTEMAS

Dois utilitários frequentemente usados nas instalações ORACLE no auxílio à manutenção dos dados são:
A PL/SQL e SGA;

B SYSDBA eSYSADMIM;

C Transact SQL e SYSDBA;
D SQL*Loader e Data Pump;
E DBCAe ADRCI.

Comentário. A única das alternativas que trata de utilitários é a D. As demais possuem alguns termos conhecidos, dentro do escopo do Oracle Database. PL/SQL é uma linguagem procedural, SGA é a área global de sistema usada para gerenciamento dos processos.SYSDBA
e SYSOPER são privilégios do sistema Oracle, SYSADMIM não existe! Transact SQL é a linguagem procedural do SQLServer. Vamos agora falar um pouco mais sobre os utilitários.
O SQL*Loader carrega dados a partir de arquivos externos em tabelas de banco de dados
Oracle. Ele tem um poderoso mecanismo de análise de dados que introduz pouca limitação sobre o formato dos dados no arquivo de dados.
A sessão típica do SQL*Loader toma como entrada um arquivo de controle, que controla o comportamento do SQL*Loader, e um ou mais arquivos de dados. A saída do SQL*Loader é um banco de dados Oracle (onde os dados são carregados), um arquivo de log, um bad file e,potencialmente, um arquivo de descarte. Um exemplo do fluxo de uma sessão SQL
carregador

* é mostrado na figura:

A tecnologia Oracle Data Pump permite movimentar em alta velocidade dados e metadados de um banco para outro. Oracle Data Pump está disponível, a partir da versão 1 doOracle
Database 10g (10.1).

Confirmamos, portando, a resposta na alternativa D.

Gabarito: D

47. BANCA: FGV ANO: 2015 ÓRGÃO: TCE-SE PROVA: ANALISTA DE TECNOLOGIA DA INFORMAÇÃO

- DESENVOLVIMENTO

Analise as seguintes afirmativas sobre tablespaces no Oracle:

1. Uma tablespace pertence sempre a um único banco de dados.

2. Uma tablespace armazena apenas as tabelas de um banco de dados e seus respectivos índices.

3. Datafiles são sempre associados a somente uma tablespace.
Somente está correto o que se afirma em:

Al;

B 1 e 3;
C2;

D 2 e 3;
E3.

Comentário. Analisando cada uma das alternativas, temos:

Na alternativa "1", uma afirmativa correta, pois uma tablespace pertence a um único banco de dados.
O que se afirma na alternativa "2" está incorreto. Sabemos que uma tablespace não armazena apenas tabelas e índices. Ela é composta de segmentos, que por sua vez armazenam tabelas,índices, views, entre outros objetos de schema.

Por fim, a alternativa "3" está certa. Uma tablespace é um conjunto de datafiles, mas cada datafile pertence a apenas um tablespace.
Gabarito: B

LISTA DE QUESTõES - MULTIBANCAS

1. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

No Oracle llg, os advisors são desenvolvidos com base em componentes de infraestrutura,
sendo um deles o Automatic Workload Repository (AWR), que
(A) fornece informações sobre melhoria percentual no tempo do banco de dados para vários tamanhos de System Global Area.
(B) faz recomendações para melhorar a performance de uma carga de trabalho. Além de analisar índices e visualizações materializadas como em versões anteriores, ele analisa tabelas e consultas e faz recomendações sobre como otimizar estruturas de armazenamento.
(C) faz análise, detecta gargalos e recomenda soluções. As recomendações podem incluir o tipo de advisor que precisa ser usado para resolver o problema.
(D) analisa problemas com instruções SQL individuais como, por exemplo, o uso equivocado delas,além de fazer recomendações para melhorar a performance.

(E) fornece serviços para coletar, manter e utilizar estatísticas para fins de detecção de problemas e autoajuste e onde as informações estatísticas são armazenadas na forma de snapshots.
2. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

Em condições normais de operação, na versãol2c do Oracle, é possível realizar operações online de manutenção em uma table sem causar lock na tabela em questão quando usando instruçõesDDL, tais como

(A) drop index online ou server free online.

(B) explain plan online ou drop constraint online.

(C) alter index unusable online ou drop index online.

(D) create index online ou merge online.

(E) call set online ou transaction online.

3. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

Antes do Oracle 12c, os tamanhos máximos em bytes dos data types varchar2, nvarchar2
e raw atingiam, respectivamente, 4.000, 4.000 e 2.000. Os correspondentes tamanhos máximos, em bytes, desses data types estendidos no Oracle 12c, Release 1 (12.1)podem atingir,
respectivamente,

(A) 32.767, 32.767 e 32.767.

(B) 16.256, 8.156 e 4.096.

(C) 16.256, 16.256 e 8.156.

(D) 32.767, 16.256 e 8.156.

(E) 32.767, 32.767 e 16.256.

4. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

No âmbito do Oracle Data Guard, o Oracle Database 12cRl implementa uma standby role que realiza a coordenação entre o database primário e todos seus standby databases. Trata-se de um
(A) standby database em cascata que usa RMAN ativo para receber os redo logs de outro standby database chamado DSync Standby.
(B) standby database em cascata que recebe os redo logs de um primary database e atua como um repositório de archivelogs, chamado RouterSync Standby.
(C) secondary standby database específico chamado RemoteSync Standby que usa RMAN ativo para receber os redo logs do primary database.
(D) primary standby database específico chamado RMAN Standby que recebe os redo logs de um outro primary database evitando, assim, a necessidade de se usar um segundo cascading standby.
(E) standby database em cascata que atua como um repositório de archivelogs chamado
FarSync
Standby.

5. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

Um profissional de TI necessitava proteger, em tempo real, a exibição de diversos dados sobre benefícios e salários de empregados e também de valores de tributos devidos por contribuintes,a alguns usuários, ou seja, que os dados armazenados permanecessem inalterados, enquanto os dados a serem exibidos fossem transformados on-the-fly antes de deixarem o banco de dados.Para isto, o profissional se utilizou de uma funcionalidade que foi introduzida no pacote AdvancedSecurity do Oracle Database 12c, chamada

(A) Oracle DataPump.

(B) Oracle Spot ADDM.

(C) Oracle Data Redaction.

(D) ASM Disk Scrubbing.

(E) SecureFiles LOBs.

6. BANCA: FCC Sefaz/SC - Auditor-Fiscal da Receita Estadual (Tecnologia da lnformação)/2018

Com respeito ao Automatic SQLTuning no Oracle Database 12c, quando o SQLTuning Advisor é executado na tarefa automática na janela de manutenção, o seu foco principal é para as instruções SQL de alta carga já executadas anteriormente, em alguns períodos específicos. No escopo global, ele verifica e analisa o comportamento dessas instruções nesses períodos, para avaliar se podem ter seu desempenho melhorado aceitando ou não o sql profile estabelecido. Aanálise é feita tanto com base no tempo de CPU como no de l/O. A tarefa automática tem parâmetros configuráveis, sendo dois deles, os seguintes:
I. ACCEPT_SQL_PROFILES que significa aceitar o sql profile automaticamente ou não.

II. MAX_AUTO_SQL_PROFILES que significa quantos profiles podem ser aceitos em geral no banco de dados Oracle em qualquer ponto no tempo.
As configurações padrão (default) para esses parâmetros são, respectivamente,
(A) true - 20.000.

(B) false - 10.000.

(C) false- 15.000.
(D) true - 15.000.
(E) true - 10.000.

7. BANCA: FCC/2018 - analista em gestão (DPE AM)/ especializado em tecnologia da informação de defensoria/ analista de banco de dados
Na definição do armazenamento (storage), considerando o sistema gerenciador de banco de dados Oracle llg, para se especificar uma área inicial de 10 GB, com incrementos graduais de 1GB, o subcomando a ser utilizado é a) STORAGE (FIRST 10G STEP 1G).
b) STORAGE (PRIMARY 10G INC 1G).

c) STORAGE (INITIAL 10G NEXT 1G).

d) STORAGE (MAIN 10G PLUS 1G).

e) STORAGE (MAJOR 10G ADD 1G).

8. FCC/2018 - analista em gestão (DPE AM)/ especializado em tecnologia da informação de defensoria/ analista de banco de dados
Considerando o sistema gerenciador de banco de dados Oracle llg, uma tarefa de administração é a criação de tablespaces. Dessa forma, o comando para a criação de uma tablespace do tipo bigfile, denominada bl, com arquivo de dados (datafile) dl, com 40 MB e autoextensível é a) CREATE BIGFILE TABLESPACE bl DATAFILE 'dl.dbf'SIZE 40M AUTOEXTEND ON;

b) CREATE 'dl.dbf' TABLESPACE 'bl'40M AUTOEXTEND YES;

c) CREATE DATAFILE, TABLESPACE 'dl.dbf', bl SIZE 40MB AUTOEXT = 1;

d) CREATE FILE 40MB TYPE BIGFILE TABLESPACE bl

DATA 'dl.dbf' EXTENSION ON;

e) CREATE 'dl.dbf' TABLESPACE bl BIGFILE
SIZE 40M AUTOEXTEND ON;

9. BANCA: FCC - Técnico Judiciário (TRT 23- Região)/ Apoio Especializado/ Tecnologia da lnformação/2016
Com relação às estruturas que fazem parte de um banco de dados Oracle e que possuem um papel importante na reconstrução do banco de dados a partir de um backup,
a) o banco de dados consiste em uma ou mais unidades de armazenamento lógico chamadas tablespaces, que consistem em um ou mais arquivos chamados datafiles.
b) quando os dados são modificados no banco de dados, o que foi modificado é gravado primeiro no online redo log, depois, é aplicado nos datafiles. Apesar de sua função de repositório intermediário, o redo log não guarda o registro das alterações feitas nos datafiles.
c) quando os dados em um datafile são atualizados, imagens anteriores destes dados são gravados em offline redo logs. Se uma transação é revertida, as informações dos redo logs são usadas para restaurar o conteúdo do datafile original.
d) o control file contém apenas informações das estruturas lógicas do banco de dados,
como tablespaces, extends e segments. Mantém também o registro de todas as operações realizadas nos datafiles.
e) um segment é a menor estrutura de armazenamento do Oracle e seu tamanho, baseado no parâmetro DB_BLOCK_SIZE, é normalmente um múltiplo do tamanho de um bloco do SistemaOperacional.

10. BANCA: FCC - Analista Judiciário (TRT 14a Região)/Apoio Especializado/ Tecnologia da lnformação/2016
Em uma empresa, um servidor Oracle llg apresentou um problema e o disco no qual se localizavam os arquivos do banco de dados foi danificado e perderam-se todos os arquivos(control files, datafiles, online redo log files etc.), porém, o disco no qual estava a flash recovery area ficou intacto. Neste caso,
a) não será possível restaurar um backup do banco de dados, pois os control files, datafiles e online redo log files foram perdidos.
b) será possível restaurar um backup do banco de dados utilizando o aplicativo DUMP ou RESTORE
a partir da flash recovery area.

c) não será possível restaurar um banco de dados porque o servidor sempre fica off-line quando o disco é danificado, impedindo o acesso à flash recovery area.
d) será possível restaurar um backup RMAN em conjunto com os archive redo log files contidos na flash recovery area.
e) não será possível restaurar o banco de dados, pois o software Oracle foi corrompido e o disco no qual se localizavam os arquivos do banco de dados foi danificado.
11. BANCA: FCC - Analista de Tecnologia da Informação (CREMESP)/Administração de Banco de
Dados/2016

O Recovery Manager (RMAN) é um recurso do Oracle llg que executa tarefas de backup e recuperação, automatizando o trabalho das estratégias de backup de um DBA. O ambiente doRMAN possui componentes mínimos e opcionais que incluem:

I. Área de disco na qual o banco de dados pode armazenar e manipular os arquivos envolvidos no backup e recuperação. A localização desta área é indicada no parâmetroDB_RECOVERY_FILE_DEST.

II. Componente que controla os dispositivos durante o backup e recuperação,
gerenciando o carregamento, labeling e descarregamento. Os dispositivos são chamados de SBT -System
Backup to Tape.

III. Executável que interpreta comandos, direciona sessões do servidor para executar os comandos e registra as atividades no arquivo de controle do target database.
Os componentes de I a III são, correta e respectivamente,

a) File Recovery Area - Media Manager - RMAN executable.

b) Disk Recovery Area - Device Backup Manager - target client.

c) Fast Recovery Area - Media Manager - RMAN client.

d) Fast Recovery Area - Device Backup Manager - target client.

e) File Recovery Area - Recovery Manager - RMAN client.

12. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/ Administrador de Banco de Dados/2015

Sobre as estruturas de armazenamento do sistema gerenciador de banco de dados Oracle llg é correto afirmar:
a) Cada tablespace é mapeado em um único bloco de dados.

b) Um datafile é mapeado em mais de um tablespace.

c) Cada segmento possui uma única extensão (extent).

d) Um tablespace pode ser composto por um ou mais segmentos.

e) Uma extensão é mapeada em mais de um datafile.

13. BANCA: FCC - Técnico Judiciário (TRT 16- Região)/Apoio Especializado/ Tecnologia da lnformação/2014
No Oracle, uma base de dados física consiste de arquivos armazenados no disco e uma instância lógica consiste de estruturas e processos na memória do servidor. Os três tipos fundamentais de arquivos físicos que compõem uma base de dados Oracle llg são: arquivos de controle,arquivos de log de repetição e arquivos de a) modelagem multidimensional.
b) comunicação com linguagens de programação.

c) integração.

d) mineração de dados.

e) dados.

14. BANCA: FCC - Analista Judiciário (TRT 13- Região)/Apoio Especializado/Tecnologia da lnformação/2014
Considere o texto abaixo:

O Oracle llg possui ferramentas para gestão de banco de dados que fornecem orientação específica sobre como lidar com os principais desafios de gestão de dados.Uma dessas ferramentas analisa comandos SQL e faz recomendações de como melhorá-los. Esta ferramenta pode ser executada automaticamente durante os períodos de manutenção (normalmente à noite). Durante cada execução automática, ela seleciona consultas SQL de alta carga(high-load)
e gera recomendações para ajustar essas consultas. Permite realizar análises estatísticas, criação de perfis SQL, análise de caminho de acesso e análise de estruturas SQL.
O texto descreve uma ferramenta conhecida como a) SQL Tuning Advisor.
b) SQL Access Advisor.

c) Automatic Database Diagnostic Monitor.

d) SQL Analysis Advisor.

e) SQL Performance Impact Advisor.

15. BANCA: FCC - Analista Judiciário (TRT 1? Região)/Apoio
Especializado/Tecnologia da lnformação/2014
O sistema gerenciador de Bancos de Dados Oracle llg armazena as tabelas de dicionário de dados na tablespace
A MAIN.

B SYSTEM.
C SYSAUX.
D UNDO.

ETEMP.

16. BANCA: FCC ANO: 2013 ÓRGÃO: TRT - 15^ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

Data warehouses geralmente contém tabelas com grande número de informações e requerem técnicas para manejá-las e prover um bom desempenho de pesquisa. O Oracle 10g provê meios de particionamento de tabelas para se adequar a este modelo. Os tipos de particionamento(partitioning) disponíveis são: Range, Hash, Composite e

A Recursive.
B List.

CIndexed.
D Neutral.
E Forecast.

17. BANCA: FCC ANO: 2013 ÓRGÃO: TRT - 15^ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

Arquitetar e manter processos ETL é considerado por muitos uma das tarefas mais difíceis de um projeto de data warehouse. Muitos projetos deste tipo utilizam ferramentas para manter este processo, por exemplo, provê recursos de ETL e tira vantagem das capacidades de banco de dados inerentes. A lacuna acima é corretamente preenchida com Oracle
A Warehouse Builder (OWB).
B Loading Data (OLD).

C Data Transformation (ODT).
D Query and Input (OQI).

E Business Intelligence (OBI).

18. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/ Administrador de Banco de Dados/2013

O gerenciamento de configuração é um componente fundamental nas operações de TI diárias de toda empresa. O Oracle Configuration Management Pack é a peça central da capacidade doOracle Enterprise Manager de gerenciar configurações e automatizar os processos de TI.
Um componente chave desta solução reduz o custo e atenua o risco, detectando,validando e reportando, de forma automática, alterações autorizadas e não autorizadas. Este componente é o a) Log Analiser.
b) Graphical Configurator Addon.

c) Configuration Change Console.

d) Data Recovery Manager.

e) Instant Support.

19. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/Administrador de Banco de Dados/2013

Considere:

I. O módulo de nuvem do Oracle Secure Backup é implementado por meio da interface
SBT do
Oracle Recovery Manager (RMAN). A interface SBT permite que bibliotecas de backup externas sejam perfeitamente integradas com este recurso. Consequentemente, os administradores do banco de dados podem continuar a usar suas ferramentas de backup existentes para realizar backups em nuvem.
II. O Oracle Secure Backup aproveita a capacidade do RMAN para criptografar backups e garantir a segurança dos dados. A segurança e a privacidade dos dados são especialmente importantes em ambientes compartilhados, acessíveis publicamente, como a nuvem de armazenamento.
III. A integração com o mecanismo do banco de dados Oracle permite que o Oracle Secure Backup identifique e ignore o espaço não utilizado (blocos) no banco de dados. Os usuários também se beneficiam dos recursos sofisticados de compressão do RMAN. No momento de transmissão de backups em redes mais lentas, como a Internet pública, qualquer redução no tamanho do backup é percebida diretamente como um aumento no desempenho do backup.
Está correto o que consta em a) I, apenas.
b) I e II, apenas.

c) III, apenas.

d) II e III, apenas.

e) I, II e III.

20.BANCA: FCC-Analista (DPE RS)/lnformática/2013

Sobre arquitetura do SGBD Oracle, considere:

I. Os componentes principais de um servidor corporativo típico são uma ou mais CPUs, espaço em disco e memória. Enquanto o banco de dados Oracle é armazenado em um disco do servidor, uma instância Oracle existe na memória do servidor.
II. Os arquivos de dados em um BD Oracle são agrupados em uma ou mais tablespaces. Dentro de cada tablespace as estruturas lógicas do banco de dados, como tabelas e índices, são segmentos subdivididos em ainda mais extensões e blocos.
III. Um tablespace Oracle consiste em um ou mais arquivos de dados. Um arquivo de dados pode ser parte de mais de um tablespace. Numa instalação do Oracle são criados no mínimo 6tablespaces em vários bigfile tablespaces para facilitar o gerenciamento pelo DBA Oracle.

Está correto o que consta APENAS em a) II e III.
b) I e III.

c) I.

d) III.

e) I e II.

21. BANCA: FCC - Analista Ministerial (MPE MA)/Banco de Dados/2013

Quando uma base de dados é criada no Sistema Gerenciador de Bancos de Dados Oracle,
são criadas, automaticamente, duas contas administrativas, cujas denominações são a) FILE e SNAME.
b) FORCE e MAXLOG.

c) SQLU e ROLL.

d) SYS e SYSTEM.

e) SIDeSGA.

22. BANCA: FCC ANO: 2012 ÓRGÃO: TRE-CE PROVA: TÉCNICO DO JUDICIÁRIO - PROGRAMADOR DE
SISTEMAS

Sobre os mecanismos de segurança do banco de dados Oracle é correto afirmar:

A Como os papéis permitem o gerenciamento mais fácil e mais eficaz dos privilégios,
eles podem ser concedidos a outros papéis.
B A única forma de atribuir privilégios a um usuário é por meio de papéis.

C Privilégios para criar um tablespace ou para excluir linhas de qualquertabela do banco de dados não são considerados privilégios de sistema.
D Todo usuário de um banco de dados pode acessar qualquer esquema desse banco, sem restrições.
E Um domínio de segurança no Oracle permite determinar papéis e privilégios para um usuário,entretanto, não permitem definir cotas de tablespaces e limite de recursos da CPU.

23. BANCA: FCC ANO: 2012 ÓRGÃO: TRE-CE PROVA: ANALISTA JUDICIÁRIO - ANALISTA DE
SISTEMAS

Visão do Oracle 10g que apresenta uma lista das diferentes métricas que dão uma estimativa da saúde do banco de dados e especifica uma condição sob a qual um alerta será emitido se a métrica alcançar o limiar ou exceder um valor especificado. Trata-se de
A DB_RECOVERY_FILE_DEST.
B DBA_TABLESPACES.

C DBA_THRESHOLDS.
D DBA_FREE_SPACE.
E DBA_SEGMENTS.

24. BANCA: FCC - Analista Judiciário (TST)/ Apoio Especializado/ Suporte em Tecnologia da lnformação/2012
Um banco de dados criado por meio do SGBD dados Oracle, versão llg, tem uma estrutura lógica e física peculiares, tendo como característica:
a) um segmento contém exatamente uma extensão.

b) o tablespace não comporta mais de um datafile.

c) um mesmo tablespace pode ser utilizado por vários bancos de dados, simultaneamente.

d) o banco de dados pode conter um ou mais tablespaces.

e) um segmento pode ser dividido em vários tablespaces.

25. BANCA: FCC - Analista Judiciário (TRE CE)/ Apoio Especializado/ Análise de Sistemas/2012

No banco de dados Oracle 10g, os segmentos a) são as unidades mais básicas de armazenamento dentro das tuplas.
b) são as menores unidades de armazenamento, também chamados tablespaces.

c) estão um nível acima na hierarquia dos agrupamentos lógicos ou grids.

d) são agrupados em uma ou mais estruturas lógicas que são as views.

e) contêm todos os dados de um agrupamento lógico dentro de um tablespace.

26. BANCA: FCC - Analista Judiciário (TRE PE)/Apoio Especializado/Análise de Sistemas/2011

O processo de background Oracle que executa a recuperação, se necessário, na inicialização da instância e que é responsável pela limpeza dos segmentos temporários que não estão mais em uso é o a) Process Monitor Process (PMON).
b) Checkpoint Process (CKPT).

c) System Monitor Process (SMON).

d) Log Writer Process (LGWR).

e) Recoverer Process (RECO).

27. BANCA: FCC - Analista Judiciário (TRE PE)/Apoio Especializado/ Análise de Sistemas/2011

Contém apenas estruturas de armazenamento lógico do banco de dados Oracle:

a) data blocks, extents e segments.

b) datafiles, extents e segments.

c) datafiles, redo log files e control files.

d) datafiles, data blocks e control files.

e) control files, redo log files e data blocks.

28. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/Administrador de Banco de Dados/2010

As entradas da estrutura física do database ORACLE 10g são especificadas no a) Control file.
b) Data file.

c) Parameter file.

d) Archive log file.

e) Redo log file.

29. BANCA: FCC - Agente de Defensoria Pública (DPE SP)/ Administrador de Banco de Dados/2010

A sequência, do menor para o maior nível de granulidade, das unidade de alocação de espaço noORACLE 10g é (extent, data block e segment).

a) segment, data block e extent.

b) data block, extent e segment.

c) segment, extent e data block.

d) data block, segment e extent.

30. BANCA: FCC - Analista do Ministério Público de Sergipe/lnformática l/Gestão e Análise de
Projeto de lnfraestrutura/2010

Strings de caracteres de tamanho fixo são armazenados em um banco de dados ORACLE por meio do tipo de dados a) char ou nchar.
b) varchar ou nvarchar.

c) char ou varchar2.

d) varchar ou varchar2.

e) nchar ou nvarchar.

31. BANCA: FCC Analista do Ministério Público de Sergipe/ Informática l/Gestâo e Análise de
Projeto de lnfraestrutura/2010

Uma instância do banco de dados ORACLE é constituída a) pela área global do sistema (SGA) e pelos processos user, server e background.
b) pelos processos user, server e background, apenas.

c) pelos processos user e server, apenas.

d) pela área global do sistema (SGA) e pelos processos background, apenas.

e) pela área global do sistema (SGA) e pelos processos user, apenas.

32. BANCA: FCC - Analista do Ministério Público de Sergipe/lnformática l/Gestão e Análise de
Projeto de lnfraestrutura/2010

O modo de execução no qual o ORACLE copia os online redo logs cheios para o disco é denominado a) commit.
b) rolling back.

c) rolling forward.

d) checkpoint.

e) archivelog.

33. BANCA: FCC - Analista do Ministério Público de Sergipe/ Informática l/Gestão e Análise de
Projeto de lnfraestrutura/2010

NÃO se trata de um componente da estrutura lógica de um banco de dados ORACLE:

a) tablespaces.

b) schema objects.

c) control files.

d) data blocks.

e) segments.

34. BANCA: FCC ANO: 2009 ÓRGÃO: TRT - 15§ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

São apenas tipos de objetos de um schema Oracle:

A table, index, cluster e profile.
B table, index, cluster e view.

C table, tablespace, index e cluster.

D tablespace, index, cluster e directory.
E tablespace, index, cluster e view

35. BANCA: FCC ANO: 2009 ÓRGÃO: TRT - 15§ REGIÃO (CAMPINAS-SP) PROVA: ANALISTA
JUDICIÁRIO - TECNOLOGIA DA INFORMAÇÃO

Cada database Oracle tem

I. um ou mais datafiles.

II. um control file.

III. um conjunto de dois ou mais redo log files.
Está correto o que consta em

Al, II e III.

B I, somente.
C II, somente.

D I e II, somente.
E I e III, somente.

36. BANCA: FCC ANO: 2008 ÓRGÃO: TRT - 2^ REGIÃO (SP) PROVA: ANALISTA JUDICIÁRIO -
TECNOLOGIA DA INFORMAÇÃO

O Oracle copiará os arquivos online redo logs cheios para o disco se a base de dados estiver em execução no modo
A undo.

B restricted.
C dedicated.
D archivelog.
E backup.

37. Ano: 2018 Banca: CESPE Órgão: STM Cargo: Analista de Sistemas Questão: 74

Um sistema gerenciador de banco de dados (SGBD) instalado no Linux deve ser configurado de modo a permitir os seguintes requisitos:
I no máximo, 1000 conexões simultâneas;

II somente conexões originadas a partir do servidor de aplicação com IP 10.10.10.2.
Tendo como referência essas informações, julgue os seguintes itens.

74 Caso o SGBD instalado seja o Oracle 12C, os requisitos I e II podem ser atendidos em tempo de execução, respectivamente, por meio dos comandos SET system sessions = 1000 e SETsystem listener = 10.10.10.2.
38. Ano: 2018 Banca: CESPE Órgão: STM Cargo: Analista de Sistemas Questões: 83 a 85

Acerca do Oracle 12C, julgue os próximos itens.

83 Especialmente voltado para o armazenamento de dados de sistemas de suporte a decisão(DSS) e data warehouse, os dados no Oracle podem ser armazenados em uma nova área opcional denominada In-Memory (IM). A IM é um suplemento que substitui a system global area(SGA),
pois se sobrepõe ao cache de buffer do banco de dados, permitindo alto poder de processamento ao varrer dados colunares rapidamente por meio de vetorização.
84 Os dados nos SGBDs são organizados em blocos, em que os sistemas de suporte à decisão(DSS) e os ambientes de banco de dados de data warehouse tendem a se beneficiar de valores de tamanho de bloco maiores.
85 Os blocos de dados são organizados em cabeçalho (row header) e dados (column data); a cada nova transação, o registro é armazenado como uma nova linha na tabela e, assim, um registro é armazenado em várias colunas em blocos de dados no disco.
39. BANCA: Cespe - Analista Judiciário (TRT 8- Região)/Apoio Especializado/Tecnologia da lnformação/2016
Julgue o item seguinte, relativo ao banco de dados Oracle.

AWR (automatic workload repository) é um repositório de informações de estatísticas de desempenho que possibilita a detecção de problemas.
Certo
Errado

40. BANCA: Cespe - Analista Judiciário (TRT 8- Região)/Apoio Especializado/Tecnologia da lnformação/2016
Assinale a opção referente ao arquivo que grava todas as mudanças realizadas no DataBase e que é utilizado somente para recuperação de uma instância em um SGBD Oracle.
a) Parameter log file b) Archive log file c) Undo file d) Control file e) Alert log file
41. BANCA: Cespe - Analista Administrativo (ANTT)/Tecnologia da Informação/lnfraestrutura deTI/2013

No que se refere ao sistema de gerenciamento de banco de dados (SGBD) Oracle e ao sistema operacional Linux, julgue o item seguinte.
No Oracle, uma das vantagens de se utilizar o ASM (automatic storage management) é a possibilidade de adição de um novo dispositivo de disco ao banco de dados sem o desligamento deste.
Certo
Errado

42. BANCA: CESPE ANO: 2012 ÓRGÃO: TJ-RO PROVA: ANALISTA JUDICIÁRIO - DESENVOLVIMENTO
DE SISTEMAS

Assinale a opção correta acerca das ferramentas, dos recursos e das características do
SGBD
Oracle 10.

A Por meio do recurso OSS (Oracle segment shrink) do Oracle 10g, pode-se compactar áreas de memória RAM marcadas como booked, transferindo-as para o disco, permitindo, assim, maior alocação de memória no processamento de consultas.
B lOTs (index organized tables) são estruturas de dados que permitem armazená-los de forma organizada com seus índices.
C DRM (database resource manager), uma área interna do Oracle 10g, é utilizada pelo tuning optimizer para prover recomendações de consultas SQL e criar índices, com o objetivo de melhorar o desempenho da recuperação de dados.
D Oracle 10g flashback é um conjunto de ferramentas mediante as quais é possível gerenciar e agendar a criação de becapes utilizando-se comandos RMAN.
E O Oracle 10g ADDM (automatic database diagnostic monitor), por intermédio do pacoteDBMS_SCHEDULER, gerencia triggers de sistemas e permite a autocriação de índices, a fim de melhorar o desempenho de acesso aos dados de forma programada.
43. BANCA: Cespe - Analista Judiciário (TJ AL)/ Apoio Especializado/ Análise de Sistemas/2012

Acerca de planos de manutenção e tuning em banco de dados Oracle llg, assinale a opção correta.
a) O Oracle Enterprise Manager exibe os resultados da tarefa do SQL Access Advisor listando as instruções SQL pela ordem de maior redução de custo.
b) O SQL Access Advisor oferece recomendações de partição somente para cargas de trabalho que têm predicados e junções em colunas de tipo VARCHAR.
c) O SQL Plan Management evita que regressões de performance resultem de alterações repentinas no plano de execução de uma instrução SQL, mas não fornece componentes para captura e seleção de informações capazes de auxiliar na evolução dos planos de execução de SQL.
d) O Automatic Database Diagnostic Monitor (ADDM) não proporciona análise de performance de gerenciamento de backup/recuperação ou análise de performance em cluster para bancos de dados com real application clusters (RAC).
e) Em cada execução do SQL Tuning Advisor, o administrador do banco de dados deve selecionar as consultas SQL de alta carga no sistema e gerar recomendações sobre como ajustá-las.
44. BANCA: Cespe - Oficial Bombeiro Militar (CBM DF)/ Complementar/ Informática/ 2011

No que se refere ao banco de dados Oracle, julgue o próximo item.

Os espaços de tabela bigfile se adaptam melhor a um ambiente que utiliza ASM
(Automatic
Storage Management), OMF (Oracle Managed Files) e RMAN (Recovery Manager) com uma Flash
Recovery Area, permitindo, ainda, um tamanho de espaço de tabela tão grande quanto 8
milhões de terabytes, conforme o tamanho do bloco do espaço de tabela.
Certo
Errado

45. BANCA: Cespe Analista (FINEP)/ Informática/ Desenvolvimento de Sistemas/2009

Uma das instâncias do sistema gerenciador de banco de dados Oracle 10g consiste de arquivos em disco, área de memória e processos em execução. Cada processo é responsável por um conjunto de atividades. Nessa versão do Oracle, o processo responsável por recuperar espaço em segmentos temporários quando estes não estão mais sendo utilizados é o a) DBW (database writer).
b) LGWR (log writer).

c) SMON (system monitor).

d) PMON (process monitor).

e) CKPT (check point).

46. BANCA: FGV ANO: 2015 ÓRGÃO: TJ-SC PROVA: ANALISTA JUDICIÁRIO - ANALISTA DE SISTEMAS

Dois utilitários frequentemente usados nas instalações ORACLE no auxílio à manutenção dos dados são:
A PL/SQL e SGA;

B SYSDBA e SYSADMIM;

C Transact SQL e SYSDBA;
D SQL*Loader e Data Pump;
E DBCAe ADRCI.

47. BANCA: FGV ANO: 2015 ÓRGÃO: TCE-SE PROVA: ANALISTA DE TECNOLOGIA DA INFORMAÇÃO

- DESENVOLVIMENTO

Analise as seguintes afirmativas sobre tablespaces no Oracle:

1. Uma tablespace pertence sempre a um único banco de dados.

2. Uma tablespace armazena apenas as tabelas de um banco de dados e seus respectivos índices.

3. Datafiles são sempre associados a somente uma tablespace.
Somente está correto o que se afirma em:

Al;

B 1 e 3;
C2;

D 2 e 3;
E3.

GABARITo

1. E

2. C

3. A

4. E

5. C

6. B

7. C

8. A

9. A

10. D

11. C

12. D

13. E

14. A

15. B

16. B

17. A

18. C

19. E

20. E

21. D

22. A

23. C

24. D

25. E

26. C

27. A

28. A

29. C

30. A

31. D

32. E

33. C

34. B

35. A

36. D

37. E

38. ECC

39. C

40. B

41. C

42. B

43. A

44. C

45. C

46. D

47. B

