# Desenvolvimento de Informação - Tecnologias de integração. Workflow

Índice

1) Workflow

WORKFLOW

Vamos agora tratar dos conceitos relacionados a fluxo de trabalho.

PRoCESSo, SUBPRoCESSo, ATIVIDADE, PRoCEDIMENTo E TAREFA

Antes de falarmos sobre workflow precisamos entender que existe uma hierarquia entre os termos presentes no título deste tópico que pode ser observada na figura abaixo.
A definição tem início pelo processo de negócio que é o conjunto de atividades
(cadeia de eventos) que tem por objetivo transformar entradas, por meio de procedimentos,em saídas (bens ou serviços) que serão entregues a clientes. Um processo é uma série de atividades inter-relacionadas que convertem entradas em saídas. Processo é uma série de atividades que consomem recursos e produzem bens ou serviços.
Um subprocesso é o conjunto de atividades correlacionadas, que executa uma parte específica do processo, do qual recebe insumos e para o qual envia o produto do trabalho realizado por todas as atividades que o compõe. Um processo deve ser dividido em subprocessos quando ele é muito complexo, contém grande número de atividades,inúmeras entradas e saídas de para outros processos.

Atividade é o conjunto de procedimentos que deve ser executado a fim de produzir um determinado resultado. É considerada uma unidade de trabalho executada por um único responsável, que tem condições determinadas de início e fim. Enfim, qualquer ação ou trabalho específico.
Atividades podem ser divididas em primárias, que têm participação direta na criação do bem ou serviço. As atividades primárias podem ser críticas ou não críticas. As críticas têm papel crucial para a integridade do processo sem folga de tempo ou recursos. Não podem atrasar ou gastar mais do que previsto. As atividades não críticas,embora imprescindíveis, podem ser realizadas em condições mais flexíveis.
As atividades secundárias não estão diretamente envolvidas com a produção do bem ou serviço que a organização vende, elas permitem que as atividades principais possam ser executadas. Temos ainda as atividades transversais, que são o conjunto de várias especialidades, executadas em uma única operação com a finalidade de resolver problemas, por exemplo, um recall da indústria automobilística.
Os procedimentos são considerados eventos, ou seja, algum acontecimento. Toda atividade contém pelo menos um evento e é por meio da realização de um evento que cada atividade produz sua parte do produto, dentro do processo. O que interessa para umWorkflow é controlar os eventos. Quando um processo é programado em uma ferramenta de Workflow define-se cada evento dentro deles. Para executar um evento temos o procedimento, que por sua vez é dividido em tarefas.
Os procedimentos podem ser formais e informais. Os formais são formados por um conjunto de informações que indica para o responsável por uma atividade como, quando e com que um evento deve ser executado. Já os informais trazem o conjunto de práticas não escritas que o ocupante de um posto incorpora à realização do seu trabalho.
Por fim temos as tarefas, que é uma decomposição de um procedimento. É a menor parte realizável de um procedimento. Esse detalhamento, além de permitir a execução do evento, serve para racionalizar a atividade.
Ao estudarmos os conceitos de workflow abaixo, veremos que uma ferramenta de workflow fornece uma série de relatórios que permitem aos gerentes analisarem o desempenho de cada atividade e com isso descobrirem onde estão os gargalos e as folgas na execução dos processos.
Gostaria antes de dar continuidade ao assunto esclarece que o CBOK faz uma divisão diferentes dos processos de negócio. Novos níveis são incluídos na hierarquia que acabamos de apresentar. Primeiramente, a função de negócio aparece entre os subprocessos e as atividades. Em segundo lugar os procedimentos são excluídos da hierarquia. E, por fim, os cenários e os passos são incorporados.
Nesta situação a tarefa deixa de ser o menor elemento e passa a ser a decomposição das atividades em um conjunto de passos ou ações para realizar o trabalho determinado.Já o cenário é uma modalidade de execução da tarefa, que pode ser subdividido em passos,

que, neste caso, é uma ação no nível atômico. Outro ponto interessante é que o CBOK
apresenta a visão lógica e visão física na modelagem de um workflow.

Visão lógica

(Processo) i 00

Representa processo de negócio primário, de suporte ou de gerenciamento
Decomposição do processo de negócio por afinidade, objetivo ou resultado desejado
Visão física

Workflow é uma tecnologia que possibilita automatizar processos, racionalizando-os e potencializando-os por meio de dois componentes implícitos: organização e tecnologia.Transforma radicalmente a maneira da empresa executar processos, atividades,
tarefas,
políticas e procedimentos.

Outra definição para workflow seria: "automatização de processos ou de fluxos de trabalho nos quais são passados documentos, informação ou tarefas,segundo determinadas regras ou procedimentos, de um participante para outro". Vejam que o termo"passados" quer dizer transferir. Basicamente temos várias pessoas, que fazem partes de uma tarefa e o fluxo vai transitar pelas etapas de execução de acordo com a responsabilidade de cada participante.
Ferramentas de workflow possibilitam a automatização de processos de negócio transversais à organização. Elas ajudam na normalização das formas de trabalho e aumentam a eficiência global das atividades de uma empresa ou organização. É possível,por exemplo, formalizar a aprovação ou reprovação de uma tarefa.

Imagine que você fez um relatório e seu chefe tenha que validá-lo. Por meio de uma ferramenta de workflow, você pode inserir esse documento e enviar para o seu chefe para validação. Ao receber a mensagem, ele pode abrir o documento, verificar e aprovar.Neste momento, pode-se gerar um hash do documento para que ele não possa mais ser modificado.
Outras características ou funcionalidades de uma ferramenta de workflow são:potencializar o a gestão dos recursos, permitir a obtenção de indicadores operacionais,assegurar a segurança da execução dos processos e integrar procedimentos manuais ao fluxo.
Essas funcionalidades geram várias vantagens competitivas para seu negócio.
Primeiramente, melhora-se o tempo de execução dos processos, reduz os custos associados à obtenção e movimentação de informações ao longo do processo e tem-se um ganho de produtividade na realização das tarefas. Outro fator relevante está relacionado à obtenção de indicadores operacionais e de gestão recolhidos ao longo da execução do processo. Imagine que esses dados aumentam a precisão e dimensão das análises.
No que diz respeito à segurança na execução do processo temos uma redução do número de erros operacionais e uma melhor rastreabilidade do processo. Algumas definições são importantes para entendermos um fluxo descrito em uma ferramenta de workflow. Vejam o conjunto de conceitos abaixo:
* Participante - Entidade (usuário ou sistema) que interage num dos passos de um processo.
* Tarefa/atividade (work) - Ação que um participante realiza no âmbito do processo.

* Função do participante (role) - Conceito que junta participantes que podem realizar uma mesma tarefa. Define o nível de acesso dos participantes para a execução das tarefas. Estabelece também a capacidade dos participantes para realizarem determinadas tarefas.
* Lista de tarefas (worklist) - Lista das tarefas que um usuário específico/role tem que executar no âmbito dos processos em que é interveniente.
* Rendezvous - Espera por informação que permite reativar um processo, ou geração de um evento que indique que a informação não chegou. Exemplo: a aprovação de uma cirurgia para um seguro de saúde necessita de um relatório médico. O sistema deve correlacionar a chegada do relatório com o processo(suspenso) de aprovação.

* Distribuição de trabalho - Distribuição das tarefas entre um conjunto de participantes disponíveis.
* Exceção - Evento que ocorre fora da sequência normal de um processo de trabalho.
* Privacidade e Segurança - Trata de quem faz o quê e quando. Deve armazenar o histórico da execução processo e não só dos dados presentes nas etapas. Os processos sensíveis são atribuídos a um grupo limitado de participantes.
Depois de termos o conhecimento das definições acima podemos agora listar os tipos de workflows. Mais precisamente, listaremos na próxima seção uma taxonomia para a classificação dos fluxos de trabalho.
TIPoS DE WoRKFLowS

Cada um dos tipos de workflow relacionados a seguir tem um tipo de abrangência, e consequente domínio, sobre o processo de negócio. Observem a figura abaixo:
3* Nirvel

2* Nlvfll

VNÍvel.

PROCESSO

Parte do processo abrangida pelo Wprkílow

A definição e os tipos de workflow variam de autor para autor. Alguns especialistas dividem Workflow em quatro tipos: ad hoc, orientado à produção,orientado à administração e baseado no conhecimento. Já outros autores preferem classificar da seguinte forma: ad hoc, baseado em transações, orientado a objeto, mas com três modelos de processo: orientado a correio eletrônico, orientado a documentos e orientado a processos. A combinação entre os vários tipos de Workflow e modelos de processo fazem com que a implementação dessa tecnologia seja flexível e praticamente abranja todas as necessidades de automatização de fluxos de trabalho.
Vamos comentar um pouco sobre cada um dos tipos de workflow.

AD HoC

Para ser usado dinamicamente por grupos de trabalho cujos participantes necessitem executar procedimentos individualizados para cada documento processado. Os sistemas de workflow do tipo ad hoc são adequados para processos simples e flexíveis, com atividades de natureza não estruturada e em áreas onde produtividade e segurança não sejam as maiores preocupações.
Permitem aos usuários criar e adaptar, de modo fácil e rápido, definições de processos simples que satisfaçam as circunstâncias que surgem com a execução de uma instância de processo. Um exemplo são os processos de aquisição descentralizados, sem uma sequência padrão para a recepção dos produtos adquiridos, cabendo a cada unidade administrativa compradora definir um fluxo ad hoc de acordo com o tipo de aquisição.
Outro exemplo são os processos de submissão de artigos em revistas, em que tais processos, são, normalmente, demorados e seguem protocolos diferentes, que dependem da revista em questão. O número de revisões e autores varia de acordo com cada caso.Vejam o exemplo de um workflow ad hoc na figura abaixo:

Servidor de InXnef

Cond-çâo

Fax

ADMINISTRATIVo

Orientado para as rotinas administrativas. Ideal para tratamento de documentos e formulários. Gerenciamento de prazos com todos os tipos de alarmes possíveis. Raramente necessitam processar grandes volumes de ocorrências. Os sistemas de workflow administrativo são adequados para processos simples e estruturados. Geralmente,são processos burocráticos, repetitivos, com regras bem definidas para a coordenação de suas atividades, que são do conhecimento de todos os participantes do fluxo.
A solicitação de adiantamento salarial para realização de viagem a serviço de uma empresa é um bom exemplo deste tipo de workflow. O funcionário que necessita do adiantamento preenche um formulário e o encaminha ao setor responsável por realizar o pagamento. Esse, ao receber a solicitação, confirma com a gerência do funcionário a necessidade da viagem. Se houver autorização, o setor competente providencia o pagamento de acordo com o nível salarial do funcionário. Ou seja, é um processo simples,predefinido e burocrático.

PRoDUçÃo

Peso pesado das aplicações Workflow. Orientado para aplicações que envolvem grandes quantidades de dados, muitas regras de negócio e recursos financeiros em grande escala. Os sistemas de workflow de produção são adequados para processos em que haja pouca intervenção de pessoas e, quando ocorrerem, essas intervenções sejam simples e de curta duração.
Esse tipo de sistema pode ser utilizado para administrar processos extremamente complexos e fortemente integrados com os sistemas já existentes numa organização.Pode ser aperfeiçoado até atingir altos níveis de qualidade e precisão,
principalmente na execução de atividades repetitivas, com grande volume de instâncias,normalmente processadas de modo ininterrupto. Um exemplo são os sistemas de análise e concessão de empréstimos e seguros de bancos e seguradoras: repetitivos, previsíveis e de larga escala. Veja um exemplo na figura a seguir relativo a um empréstimo bancário:
COLABORATIVO

Os sistemas de workflow colaborativo são adequados para processos que envolvam trabalho cooperativo realizado por equipes com objetivos comuns. Podem ser adotados para automatizar processos empresariais críticos que não são orientados à transação.Diferentemente de outros tipos de workflow, baseados na premissa de que sempre há progresso em avançar para a etapa seguinte, um workflow colaborativo pode demandar várias repetições de um mesmo passo do processo até que alguma forma de acordo seja alcançada, podendo até mesmo retornar a estágios anteriores.
Além disso, workflows colaborativos tendem a ser muito dinâmicos no sentido de que são definidos conforme progridem. Um exemplo são os processos para revisão de artigos acadêmicos. As suas atividades consistem basicamente na seleção de revisores,distribuição dos artigos e acompanhamento das revisões: tudo de forma colaborativa para produzir uma revisão conjunta (consolidada) do artigo.
ORIENTADo PARA OBJETo

Um objeto é o conjunto de atributos, ou dados, e instruções sobre como os dados e os atributos devem ser processados, estocados, recuperados e visualizados pelo usuário.Exemplo: Na mudança de regra, os documentos passam a ser tratados e processados com a regra nova sem afetar documentos da regra antiga. Veja o exemplo a seguir para entender o exemplo de um workflow orientado para objeto.
TRANSACIoNAL

Os sistemas de workflow transacional são adequados para processos cujas atividades podem ser agrupadas em unidades atômicas. A atomicidade exige que todas as atividades sejam concluídas corretamente; caso contrário, o processo deve retornar para a situação em que estava no início da execução da unidade.
Na prática, a restrição de atomicidade é muitas vezes relaxada para evitar bloqueios.
Este tipo de workflow pode ser utilizado nos casos em que é necessário garantir a exatidão e a confiabilidade de uma aplicação em situações de concorrência e falha. Um exemplo atual de aplicação desse tipo de workflow são os sistemas de vendas online, conhecidos como aplicações e-business.
Esses sistemas são aplicações críticas que necessitam sincronizar e confirmar as várias atividades desenvolvidas ao longo do fluxo do processo, como: aceitação da compra pela empresa do cartão de crédito; disponibilidade do produto em estoque ou atendimento da solicitação pelo fornecedor; e remessa do produto para o cliente.
BASEADo No CoNHECIMENTo

Aprende com seus próprios erros e acertos. Vai além da execução pura e simples das regras preestabelecida e incorpora exceções a seus procedimentos. Tem seu paradigma baseado na gestão de processos podendo utilizar tecnologias de InteligênciaArtificial.
Possui características e ferramentas que o permitem aprender com seus próprios erros e acertos. Tem funcionalidades que o capacitará ir além da execução pura e simples das regras preestabelecidas e incorporar novas regras e exceções aos seus procedimentos.
Com isso terminamos a apresentação da principal classificação dos fluxos de trabalho.

Vamos agora falar das regras, rotas e papeis.

Os TRÊS R'S Do WoRKFLow

Conhecido como três Rs do workflow por suas palavras ou termos no inglês começarem por R, quais sejam: Roles, Rules and Routes. Se pensarmos em uma peça de teatro podemos fazer a seguinte metáfora: O papel é sempre o mesmo, as responsabilidades são sempre as mesmas para cada personagem existente no texto, o que pode mudar são os atores, mas eles têm o texto exemplificando suas responsabilidades e com o qual podem aprender e assim desempenhar o seu papel com segurança. O diretor da peça diz como cada um deve representar (as regras) e ensaia a movimentação do elenco em cena (as rotas).
Definindo de maneira mais formal, um papel (role) é o conjunto de características e habilidades necessárias para executar determinada tarefa pertencente a um evento existente em uma atividade. Definimos, portanto, quem faz o que, não se refere a pessoas ou cargos, mas a papéis.
As regras (rules) são atributos que definem de que forma os dados que trafegam no fluxo de trabalho devem ser processados, roteados e controlados pelo sistema deWorkflow.
Definem quais informações devem transitar pelo fluxo, sob quais condições e como cada tarefa deve ser executada. Cada documento enviado contém informações que serão usadas por quem as recebe.
Mas, associado ao documento existem regras que especificam a operação do documento, quais as atividades que devem recebê-lo, quais as rotas a serem seguidas etc.Um exemplo seria um documento deve ser preenchido e aprovado por um grupo de pessoas, dentro de um tempo predeterminado e rígido. As aprovações seguem regras específicas.
Por fim, temos as rotas (routes) que são caminhos lógicos que, definidos sobre regras específicas, têm a função de transferir a informação dentro do processo,ligando as atividades e seus eventos associados ao fluxo de trabalho. É o controle de movimentação exercido sobre os documentos. Controlam como os documentos se movem de um ponto a outro dentro do fluxo de trabalho. As rotas podem ser sequenciais, paralelas ou condicionais, conforme verificamos na figura abaixo:
Rota Sequencial

