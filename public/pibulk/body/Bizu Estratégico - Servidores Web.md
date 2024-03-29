# Bizu Estratégico - Servidores Web

Olá, prezado aluno. Tudo certo?

Neste material, traremos uma seleção de bizus da disciplina de Servidores Web e de Aplicação para o concurso de Analista - Especialidade: Tecnologia.
0 objetivo é proporcionar uma revisão rápida e de alta qualidade aos alunos por meio de tópicos que possuem as maiores chances de incidência em prova.
Todos os bizus destinam-se a alunos que já estejam na fase bem final de revisão (que já estudaram bastante o conteúdo teórico da disciplina e, nos últimos dias, precisam revisar por algum material bem curto e objetivo).
Além disso, utilizamos os materiais do professor Evandro para elaborar esse Bizu.

Apresentação

Antes de começarmos, gostaria de me apresentar. Meu nome é Elizabeth Menezes, tenho 32 anos e sou natural do Pernambuco. Sou graduada em Administração pela
UFPE e Pós-Graduada em Direito Administrativo e Constitucional.

Atualmente, exerço o cargo de Auditora de Controle Externo no
Tribunal de Contas do Estado de São Paulo (TCE-SP). Também fui aprovada e nomeada para outros concursos da área fiscal (Auditor FiscalEstadual e Municipal) e da área de controle.

Serei a responsável pelo Bizu Estratégico de Servidores Web e de Aplicação e, com ele, pretendo abordar os tópicos mais cobrados nessa disciplina, de maneira concisa e objetiva, por meio de uma linguagem bem clara!
Espero que gostem!

Um grande abraço e bons estudos!

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

Servidores Web e de Aplicação - SERPRO

Assunto Bizu

Servidores web e de aplicação. Wildfly, I IS, Apache. 1

Caderno de Questões http://questo.es/io3ms3
Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

Servidores Web e de Aplicação

1. Servidores web e de aplicação. 2.1 Wildfly, IIS,
Apache.

Servidores web e de aplicação. Wildfly, IIS, Apache.

* Tanenbaum define que: "Um sistema distribuído é um conjunto de computadores independentes entre si que se apresenta a seus usuários como um sistema único e coerente."
* Resumindo, são sistemas que o usuário "enxerga" como um único computador, mas na verdade existem alguns (ou muitos), geograficamente distribuídos. Como as mensagens são trocadas e como é realizado o processamento, o usuário nem fica sabendo (é transparente), ele só recebe o resultado final.
Transparência

Acesso

Localização
Migração

Re locação

Replicação
Concorrência

Falha

Descrição

Oculta diferenças na representação de dados e no modo de acesso a um recurso.
Oculta o lugar em que um recurso está localizado.

Oculta que um recurso pode ser movido para outra localização.
Oculta que um recurso pode ser movido para outra localização enquanto em uso.
Oculta que um recurso ê replicado.

Oculta que um recurso pode ser compartilhado por diversos usuários concorrentes.
Oculta a falha e a recuperação de um recurso.

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Ju

* Middleware: camada de software localizada logicamente entre uma camada de nível mais alto(usuários e aplicações) e uma camada subjacente (frameworks e facilidades de comunicação). As principais funções da camada de middleware são:
- Ocultar do usuário que a aplicação é executada em diferentes máquinas distribuídas geograficamente;
- Ocultar a heterogeneidade dos sistemas operacionais (ex.: Windows, Linux etc.) e protocolos de comunicação subjacentes.
As principais características de um sistema distribuído são r
Concorrência Falhas independentes
* Gerenciamento de recursos: a principal tarefa do sistema é garantir o controle sobre quem usa o quê. Esse controle também permite o compartilhamento dos recursos.
* Gerenciamento de processos: essa funcionalidade distribui o processamento de forma justa entre as aplicações, evitando que uma aplicação monopolize o recurso.A gerência do processador está diretamente relacionada ao escalonamento. A sensação de que um processador está sendo compartilhado entre os vários processos é dita pseudoparalelismo.
* Modelo cliente-servidor: os servidores mantêm recursos e servem pedidos de operações sobre esses recursos. Servidores podem ser clientes de outros servidores. Os próprios nomes ajudam a entender (servidor serve recursos e o cliente é quem solicita). Trata-se de uma arquitetura simples e permite distribuir sistemas centralizados muito diretamente, porém é pouco escalável,limitado pela capacidade do servidor e pela rede que o liga aos clientes. Ou seja,
um único servidor não consegue atender milhares de clientes de forma satisfatória, por exemplo.
Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Ju

* Modelo peer-to-peer: todos os processos possuem papeis semelhantes, sem distinção entre clientes e servidores. As principais características são mais ampla distribuição de carga(computação e rede), maior escalabilidade, o sistema expande-se acrescentando mais pares,
e a coordenação mais complicada que cliente-servidor.
* Clusters são sistemas de processamento compostos por uma coleção de computadores autônomos, interconectados e que trabalham em conjunto para processar uma tarefa.Tipicamente na computação de cluster é utilizada programação paralela na qual um único programa é executado em paralelo. Dependendo do objetivo que se pretenda, podemos ter os seguintes tipos de cluster: - Cluster de alto desempenho: direcionado a aplicações bastante exigentes no que diz respeito ao processamento;
- Cluster de alta disponibilidade: tem como objetivo permanecer ativo por um longo período e em plena condição de uso. Consegue detectar erros e se proteger de possíveis falhas;
- Cluster de balanceamento de carga: controla a distribuição equilibrada do processamento. As tarefas de processamento são distribuídas o mais uniformemente possível entre os nós.
JBoss Application Server (AS)

JBoss Enterprise Application
Platform (EAP)

* versão open source e não possui suporte

* O Apache é um servidor Web livre (possui código-fonte aberto) que funciona em ambiente multiplataforma (Windows, Novell, OS/2, Unix, Linux, FreeBSD etc.). No Linux o servidor utiliza o daemon httpd. Suas funcionalidades são mantidas através de uma estrutura de módulos,permitindo inclusive que o usuário escreva seus próprios módulos.

* Apachectl (Apache HTTP Server Control Interface): trata-se de um front end para o servidorApache. É utilizado para ajudar o administrador a controlar o funcionamento do daemon httpd.O script apachectl pode operar em dois modos:

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Ju

- Front end simples que configura quaisquer variáveis de ambiente necessárias e então chama o httpd, passando argumentos de linha de comando;
- Script de inicialização, recebendo argumentos simples como start, restart, e stop,
traduzindo-
os em sinais apropriados ao httpd.

* O IIS (Internet Information Services) é um servidor Web criado pela Microsoft para seus sistemas operacionais para servidores. A versão mais recente é o IIS 10 (Windows Server 2016 eWindows
10). A função do IIS no Windows Server é oferecer uma plataforma para a hospedagem de sites,serviços e aplicativos, permitindo a integração das seguintes tecnologias: ASP.NET, FTP,
PHP,
WCF e o próprio IIS.

* permite que o IIS processe requisições no pool de aplicativos utilizando o "Integrated Pipeline"
Modo clássico

* utiliza o pipeline de processamento do IIS 6,
inicialmente as requisições são processadas através .

dos m ódulos do IIS7

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Ju

Vamos ficando por aqui.

Esperamos que tenha gostado do nosso Bizu!
Bons estudos!

