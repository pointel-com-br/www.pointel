# Bizu Estratégico - Desenvolvimento de Informação

Olá, prezado aluno. Tudo certo?

Neste material, traremos uma seleção de bizus da disciplina de Banco de Dados para o concurso do SERPRO.

O objetivo é proporcionar uma revisão rápida e de alta qualidade aos alunos por meio de tópicos que possuem as maiores chances de incidência em prova.

Todos os bizus destinam-se a alunos que já estejam na fase bem final de revisão (que já estudaram bastante o conteúdo teórico da disciplina e, nos últimos dias, precisam revisar por algum material bem curto e objetivo).

ANÁLISE ESTATÍSTICA

Pessoal, segue abaixo uma análise estatística dos assuntos mais exigidos pela banca CEBRASPE no âmbito da disciplina de Banco de Dados, além de cadernos com questões focadas na banca:

Assunto. Banco de dados. (Introdução). Incidência. 7,50%

Assunto. Modelagem de banco de dados: físico, lógico e conceitual. (Modelo Conceitual). Incidência. 1,25%

Assunto. Modelagem de banco de dados: físico, lógico e conceitual. (Modelo Relacional). Incidência. 32,50%

Assunto. Álgebra relacional, SQL/ANSI e linguagens procedurais embarcadas. Incidência. 22,50%

Assunto. Arquitetura de banco de dados: relacional ( Oracle ). Incidência. 5,00%

Assunto. Arquitetura de banco de dados: relacional ( SqlServer). Incidência. 0,00%

Assunto. Arquitetura de banco de dados: relacional ( PostgreSQL ). Incidência. 7,50%

Assunto. Ciência de dados. Big Data. Incidência. 16,25%

Assunto. Processamento de Dados. Conceitos de processamento massivo e paralelo. Processamento em lote (batch). Processamento em tempo real (real time). Processamento MapReduce. Incidência. 3,75%

Assunto. Aprendizado de máquina. (Aprendizado Supervisionado). Incidência. 3,75%

Assunto. Aprendizado de máquina. (Aprendizado NÃO Supervisionado). Incidência. 0,00%

Assunto. Visão computacional. Deep learning. Incidência. 0,00%

Assunto. Processamento de linguagem natural (PLN). Incidência. 0,00%

Assunto. Linguagem R. Incidência. 0,00%

Assunto. Análise de dados (Pandas, NumPy). Incidência. 0,00%

## Banco de Dados

1. BANCOS DE DADOS

* Dados: fatos brutos, que não foram organizados, processados, relacionados, avaliados ou interpretados.
* Informação: é um dado acrescido de contexto, relevância e propósito.

* Conhecimento: é uma informação contextuai, relevante e acionável.

Tipos de Dados:

* Não estruturados: não possuem uma estrutura definida. Podem ser listados como exemplo documentos, textos, imagens e vídeos.
* Estruturados: são aqueles quem possuem a mesma estrutura de representação rígida e previamente projetada, ou sejam, existe um esquema que descreve as características dos dados que serão armazenados .
* Semiestruturados: apresentam uma organização bastante heterogênea , por exemplo o XML.

ESCLARECENDO!

Há dois tipos de redundância de dados:

Redundância controlada de dados: Acontece quando o software tem conhecimento da múltipla representação da informação e garante a sincronização entre as diversas representações.
Redundância não controlada: Acontece quando a responsabilidade pela manutenção da sincronia entre as diversas representações de uma informação está com o usuário e não com o software.
Sistema de Gerenciamento de Banco de Dados (SGBD) para atuar como um guardião do banco de dados, que substituiu a abordagem de arquivos. Vejamos uma figura para esclarecer esses contextos:
Sistema de arquivos.

Sistema de Banco de Dados.

Banco tem diversas definições possíveis no dicionário da língua portuguesa. Dentre elas a que melhor se encaixa no nosso contexto é um conjunto organizado e categorizado de objetos, por exemplo, podemos ter um banco de fotografias ou um banco de leite.

Dados são fatos conhecidos que podem ser registrados e possuem um significado implícito. Esse conceito, porém, é um pouco amplo e abstrato para nosso intuito. Quando reduzimos o escopo à tecnologia da informação, temos um conceito mais adequado para dado. Ele é a representação física de um evento no tempo e espaço que não agrega fundamento ou significado para quem o sente ou recebe. É, basicamente, um registro!

MINTO! O banco de dados, por si só, pode ser considerado como o equivalente eletrônico de um armário de arquivamento; ou seja, ele é um repositório ou recipiente para uma coleção de arquivos de dados computadorizados.
Banco de dados é um conjunto de dados integrados que tem por objetivo atender a uma comunidade de usuários - Carlos Heuser.
Banco de dados é um conjunto de dados estruturados que são confiáveis,
coerentes e compartilhados por usuários que têm necessidades de informações diferentes. - Sílberchatz
Acho que você já entendeu o conceito de banco de dados! Na lista acima, você conheceu todas as definições que podem aparecer na sua prova.:)

2. Modelo Relacional.

* O modelo relacional retrata os dados como sendo armazenados em tabelas retangulares bidimensionais, chamadas de relações.

Cada linha de uma tabela é conhecida como uma tupla, ou uma coleção de valores relacionados. Cada coluna é vista como um atributo, cujo valor pertence um determinado conjunto de valores possíveis: o domínio.
Álgebra Relacional.

* É uma coleção de operações de alto nível sobre relações ou conjuntos cujo resultado é uma nova relação ou conjunto.

OPERAÇÃO. SELEÇÃO. É COMUTATIVA. RELAÇÃO UNÁRIA. FINALIDADE. Seleciona todas as linhas que satisfazem a condição de seleção de uma Tabela T 1.

OPERAÇÃO. PROJEÇÃO. NÃO É COMUTATIVA. RELAÇÃO UNÁRIA. FINALIDADE. Produz uma nova tabela com apenas algumas das colunas de uma tabela T 1 e remove linhas duplicadas.

OPERAÇÃO. PRODUTO CARTESIANO. É COMUTATIVA. RELAÇÃO BINÁRIA. FINALIDADE. Produz uma nova tabela com todas as combinações possíveis de linhas de duas tabelas T 1 e T 2.

OPERAÇÃO. JUNÇÃO. É COMUTATIVA. RELAÇÃO BINÁRIA. FINALIDADE. Produz uma nova tabela com todas as combinações possíveis de linhas de duas tabelas T 1 e T 2 que satisfazem uma condição de seleção.

OPERAÇÃO. UNIÃO. É COMUTATIVA. RELAÇÃO BINÁRIA. FINALIDADE. Produz uma nova tabela que inclui todas as linhas das Tabela T 1 e T 2, eliminando as duplicatas - as tabelas devem ser união-compatíveis.

OPERAÇÃO. INTERSECÇÃO. É COMUTATIVA. RELAÇÃO BINÁRIA. FINALIDADE. Produz uma tabela aue inclui todas as linhas em comum das Tabela T 1 e T 2 - as tabelas devem ser união-compatíveis.

OPERAÇÃO. DIFERENÇA. NÃO É COMUTATIVA. RELAÇÃO BINÁRIA. FINALIDADE. Produz uma tabela que inclui todas as linhas de uma Tabela T 1 que não estão na Tabela T 2 - as tabelas devem ser união compatíveis.

Views

* É um subconjunto de um banco de dados. Permite que se visualize apenas parte dos dados de uma tabela. A view não necessariamente existe em forma física, sendo muitas vezes uma tabela virtual.

índices

* É um mecanismo utilizado para melhorar a velocidade de acesso aos dados. O excesso de índices pode prejudicar o desempenho.

Chaves

* Superchave: conjunto de um ou mais atributos que permite identificar uma tupla de forma exclusiva.

* Chave primária: é uma superchave mínima escolhida para identificar uma linha da tabela.

* Chave candidata: Superchaves de tamanho mínimo, candidatas a serem possíveis chaves primárias de uma tabela.

* Chave estrangeira: chave primária de um outra relação.

Operadores de conjuntos tradicionais.

* União, Interseção, Diferença e Produto cartesiano

* Todos eles um pouco modificados para levar em conta o fato de que seus operandos são, especificamente,relações e não conjuntos arbitrários.

Operadores relacionais especiais.

* De restrição (também conhecido como seleção),
projeção, junção e divisão.

Primeira forma normal.

* Uma relação R existe na primeira forma normal (1FN) se, e somente se, todos os domínios subjacentes contiverem apenas valores atômicos.
* No modelo relacional, um domínio é atômico se os elementos do domínio são considerados unidades indivisíveis. Um esquema de relação R está na primeira forma normal se todos os atributos de R são atômicos.
* A primeira forma normal afirma que o domínio de um atributo deve incluir apenas valores atômicos (simples e indivisíveis) e que o valor de qualquer atributo em uma tupla deve ser um único valor do domínio desse atributo.
* A primeira forma normal evita as chamadas relações aninhadas, essas relações contêm vários atributos em uma única coluna e não são permitidas no modelo relacional.
Resumindo as Formas Normais.

O que é necessário na primeira forma normal dos bancos de dados?
Eliminar atributos não atómicos.

O que é necessário na segunda forma normal dos bancos de dados?
Eliminar dependências funcionais não plenas.

O que é necessário na terceira forma normal dos bancos de dados?
Eliminar dependências transitivas.

O que é necessário na forma normal FNBC dos bancos de dados?
Eliminar dependência funcional cujo determinante não é chave candidata.

O que é necessário na quarta forma normal dos bancos de dados?
Eliminar dependência multi valorada.

O que é necessário na quinta forma normal dos bancos de dados?
Encontrar e eliminar a dependência de junção.

3. Álgebra Relacional, SQL/ANSI e linguagens procedurais embarcadas

Pontos Importantes

Primeiramente, SQL é uma linguagem de programação reconhecida internacionalmente e usada para definição e manutenção de bancos de dados relacionais. A principal característica da linguagem é ser declarativa1, ou seja, os detalhes de implementação dos comandos são deixados para os SGBDs relacionais. Não esqueça disso! Já caiu várias vezes em provas anteriores. No SQL você declara o que você quer e o SGBD vai achar os dados para você no banco, caso existam é claro.

* DDL- Data Definition Language - A linguagem de definição de dados contém comandos que criam, modificam e excluem objetos de banco de dados. São exemplos de comando: CREATE, ALTER, DROP e TRUNCATE.

* DML - Data Manipulation Language - A linguagem de manipulação de dados fornece instruções para trabalhar com os dados armazenados como SELECT, INSERT, UPDATE, DELETE e MERGE.

* DQL - Data Query Language-A linguagem de consulta de dados é um subconjunto da DML que possui apenas a instrução de SELECT.

* DTL- Data Transaction Language - Linguagem de transação de dados inclui comandos de COMMIT, ROLLBACK e SAVEPOINT

* DCL - Data Control Language - A linguagem de controle de dados contém os comandos relacionados com as permissões de controle de acesso. Garante os privilégios aos usuários para acessar os objetos do banco. Os mais conhecidos comandos são o GRANT e o REVOKE.

Linguagens de Banco de Dados.

PL/SQL - Encontrado em SGBDs Orade. PL/SQ.L, que é a sigla para Procedural Language/SQL, contém muitas semelhanças com a linguagem de programação geral.

Transact-SQL - Usado pelo Microsoft SQ.L Server e Sybase Adaptive Server. Como Microsoft e Sybase se afastaram, a plataforma comum que compartilhavam no início na década de 1990 foi dividida, suas implementações de agora também divergem, produzindo dois dialetos distintos de Transact-SQL.

SQL PL - extensão processual do IBM DB2 para SQL, introduzido na versão Item. 7.0 do SGBD, fornece construções necessárias para a execução de controle de fluxo em torno de consultas SQL tradicionais e operações.

PL/pgSQL - O nome do dialeto SQjLe das extensões implementadas no PostgreSQL A sigla significa Procedural Language/PostgreSQL

MySQL — O MySQL introduziu uma linguagem procedural em seu banco de dados na versão 5, mas não há nenhum nome oficial para ela. Ela segue o padrão definido pela ANSI (SQL/PSM).

Principais pontos do PL/SQL.

1. Os blocos de códigos podem ser usados para escrever programas inteiros.

2. Por ser procedural, devemos descrever COMO as coisas devem ser feitas.

3. São executados em blocos inteiros.

4. Usados para criar aplicações.

5. Uma extensão de SQL, é permitido o uso de código SQL dentro do código PL/SQL.

Principais pontos do SQL.

1. Os comandos são usados para executar operações .de DMLe DDL

2. Por ser declarativa, devemos definir apenas O QUE deve ser feito.

3. São executados em declarações únicas, (statements).

4. Usados para manutenção dos dados.

5. Não pode conter código PL/SQL.

Resumindo os principais comandos usadas para definição de objetos em SQL, conhecidos como DDL (Data Definition Language) são:

COMANDO. CREATE. DESCRIÇÃO. Comando utilizado para criar bancos de dados, tabelas, índices, entre outros.
COMANDO. DROP. DESCRIÇÃO. Comando utilizado para deletar uma tabela do banco de dados.

COMANDO. TRUNCATE. DESCRIÇÃO. Comando utilizado para apagar os dados de uma tabela do banco de dados.

COMANDO. ALTER. DESCRIÇÃO. Comando utilizado para adicionar, deletar ou modificar colunas do banco de dados.

COMANDO. RENAME. DESCRIÇÃO. Comando utilizado para renomear uma tabela do banco de dados.

* Restrições em tabelas - Definida dentro de uma definição de tabela. A restrição pode ser definida como parte da definição de coluna ou como um elemento ao final da definição. Restrições definidas no nível de tabela podem ser aplicadas a uma ou mais colunas.

* Assertions (Afirmações) - Um tipo de restrição que é definida dentro de uma definição afirmação (separado da definição da tabela). Uma afirmação pode ser relacionada com uma ou mais tabelas.

* Restrições de domínio - Um tipo de restrição que é definida dentro de uma definição de domínio (separado da definição da tabela). A restrição de domínio está associada com qualquer coluna que é definida baseada no domínio específico. Aqui você pode criar um domínio para atribuí-lo a uma coluna de uma tabela.

CLÁUSULA. SELECT. DESCRIÇÃO. Comando utilizado para selecionar dados de uma tabela.

CLÁUSULA. FROM. DESCRIÇÃO. Comando utilizado para indiicar de onde os dados devem ser selecionados.

CLÁUSULA. WHERE. DESCRIÇÃO. Comando utilizado para filtrar os dados.

CLÁUSULA. GROUP BY. DESCRIÇÃO. Comando utilizado para agregar um conjunto de dados.

CLÁUSULA. HAVING. DESCRIÇÃO. Comando utilizado para filtrar dados agregados.

CLÁUSULA. ORDER BY. DESCRIÇÃO. Comando utilizado para ordenar os dados recuperadas.

## Ciência de Dados. Big Data

Big Data pode ser entendido como a captura, gerenciamento e análise de dados que vão além de dados estruturados típicos, que podem ser consultados por sistemas de gerenciamento de banco de dados relacional — frequentemente em arquivos não estruturados, vídeo digital, imagens, dados de sensores, arquivos de log e, na verdade, qualquer dado não contido nos registros com campos pesquisáveis distintos.

OS V'S DO BIG DATA.

Item. Volume.

Dados em repouso.

* Terabytes ou exabytes de dados existentes para o processo.

Item. Velocidade.

Dados em movimento.

* Streammg data (fluxo de dados)

* Requer milissegundos ou segundos para resposta.

Item. Variedade.

Dados em diferentes formas.

* Estruturados

* Semiestruturado

* Não estruturado

* Texto

* Multimídia

Item. Veracidade.

Dados em dúvida.

* Incerteza sobre a consistência e completude.

* Ambiguidade, latência. modelos de aproximação.

Item. Valor.

Dados em dinheiro.

* Os dados devem estar associados aos modelos de negócio.

* Preocupação com a geração de retorno.

## Arquitetura de Banco de Dados: Relacional (PostgreSQL)

O PostgreSQL é um descendente de código aberto do programa original desenvolvido em Berkeley. Ele suporta grande parte dos comandos da linguagem SQL/ANSI padrão e oferece muitas características modernas, entre elas: consultas complexas, chaves estrangeiras, triggers, visões atualizáveis, integridade transacional e controle de concorrência multiversão.

Uma instância do PostgreSQL é chamada de cluster porque uma única instância pode servir e lidar com vários bancos de dados Cada banco de dados é um espaço isolado onde usuários e aplicativos podem armazenar dados. Um banco de dados é acessado por usuários autorizados, mas os usuários conectados a um banco de dados não podem cruzar os limites do banco de dados e interagir com os dados contidos em outro banco de dados, a menos que se conectem explicitamente ao último banco de dados também.

O PostgreSQL divide os usuários em duas categorias principais:

* Usuários normais: esses usuários são aqueles que podem se conectar e manipular bancos de dados e objetos, dependendo de seu conjunto de privilégios
* Superusuários: Esses usuários podem fazer qualquer coisa com qualquer objeto de banco de dados.
Esta é uma rápida recapitulação dos principais termos usados no PostgreSQL:

* Cluster: refere-se a todo o serviço PostgreSQL.

* Postmaster: este é o primeiro processo que o cluster executa, e este processo é responsável por manter o controle das atividades de todo o cluster. O postmaster bifurca-se em um processo de back-end toda vez que uma nova conexão é estabelecida.

* Banco de dados o banco de dados é um contêiner de dados isolado ao qual os usuários (ou aplicativos) podem se conectar. Um cluster pode lidar com vários bancos de dados. Um banco de dados pode ser feito por diferentes objetos, incluindo esquemas (namespaces), tabelas, gatilhos e outros objetos.

* PGDATA: é o nome do diretório que, no armazenamento persistente, é totalmente dedicado ao PostgreSQL e seus dados. O PostgreSQL armazena os dados nesse diretório.

* WALs: contém o log de intenção de alterações do banco de dados, usado para recuperar dados de um travamento crítico

/bin - programas de linha de comando do PostgreSQL, como psql.

/data - arquivos de configuração e tabelas compartilhadas por todos os bancos de dados. Por exemplo, uma tabela pg_shadow compartilhada por todos os bancos de dados,

/data/base - um subdiretório é criado para cada banco de dados Usando os comandos du e Is, os administradores podem exibir a quantidade de espaço em disco usado por cada banco de dados, tabela ou índice.

/doc - documentação do PostgreSQL.

/include - inclui os arquivos usados por várias linguagens de programação.

/lib - bibliotecas usadas por várias linguagens de programação. Este subdiretório também contém os arquivos usados durante a inicialização, e exemplos e templates de arquivos de configuração, que podem ser copiados para /data e modificados.

* checkpoint: é um processo responsável por executar os pontos de verificação, quesão pontos no tempo em que o banco de dados garante que todos os dados sejam realmente armazenados de forma persistente no disco.

* background writer: é responsável por ajudar a enviar os dados da memória para o armazenamento permanente.

* walwriter: é responsável por gravar os Logs Write-Ahead (WALs), os logs que são necessários para garantir a confiabilidade dos dados, mesmo no caso de uma falha do banco de dados.

* stats collector: é um processo que monitora a quantidade de dados que o PostgreSQL está manipulando, armazenando-os para uma análise e decisões posteriores, como decidir quais índices usar para satisfazer uma consulta.

* logical replication launcher: é um processo responsável por lidar com a replicação lógica.

Descrição das Autenticações.

1. Trust. Permite a conexão incondicionalmente. Este método permite a qualquer pessoa se conectar ao servidor de banco de dados PostgreSQL e se autenticar com o usuário que desejarem, sem a necessidade de senha ou qualquer outra autenticação.

2. Reject. Rejeita qualquer conexão incondicionalmente. Isso é útil para "filtragem" de certos hospedeiros de um grupo, por exemplo, uma linha de reject poderia bloquear um host específico para conexão, enquanto uma linha mais tarde permite que os hosts restantes possam se conectar.

3. scram-sha-256. Executa a autenticação SCRAM-SHA-256 para verificar a senha do usuário.

4. md5. Exige que o cliente forneça uma senha MD5 para autenticação.

5. password. Exige que o cliente forneça uma senha não criptografada para autenticação. Uma vez que a senha é enviada em texto simples através da rede, não deve ser usado em redes não confiáveis.
6. gss. Usa GSSAPI para autenticar o usuário. Este método só está disponível para conexões TCP/IP.
7. sspi. Usa SSPI para autenticar o usuário. O método só está disponível no Windows.
8. ident. Obtém o nome do usuário do sistema operacional do cliente entrando em contato com o servidor e verifica se ele corresponde ao nome do usuário do banco de dados. A autenticação ident só pode ser utilizada em conexões TCP/IP. Quando especificado para conexões locais, peer authentication será utilizado em seu lugar.
9. peer. Obtém o nome de usuário do sistema operacional do cliente e verifica se ele corresponde ao nome do usuário solicitado do banco de dados. Isto só está disponível para conexões locais.
10. ldap. Autentica o cliente usando um servidor LDAP.

11. radius. Autentica usando um servidor RADIUS.

12. cert. Autentica usando certificados de cliente SSL.

13. PAM. Autentica utilizando o serviço Pluggable Authentication Modules
(PAM) fornecido pelo sistema operacional.

O PostgreSQL 12 gerencia os seguintes tipos de particionamento de tabela:

* Range partitioning - quando a tabela é dividida em "intervalos". Os intervalos não devem se sobrepor e a faixa é definida por meio do uso de um campo ou conjunto de campos. Aqui estamos falando de valores numéricos.

* List partitioning - a tabela será particionada usando uma lista de valores. Essa lista tende a ser um conjunto discreto, por exemplo, cidades ou time de futebol.

* Hash partitioning - a tabela será particionada usando um valor de hash que será usado como o valor para dividir os dados em tabelas diferentes.

O PostgreSQL possui um mecanismo de transação muito rico e compatível com os padrões que permite aos usuários definir exatamente as propriedades da transação, incluindo transações aninhadas.

O PostgreSQL depende muito de transações para manter os dados consistentes em conexões simultâneas e atividades paralelas e, graças aos registros Write-Ahead (WALs), o PostgreSQL faz o possível para manter os dados seguros e confiáveis. Além disso, o PostgreSQL implementa o Multi-Version Concurrency Control (MVCC), uma forma de manter a alta simultaneidade entre as transações.

Como não temos muitas transações simultâneas de conexões diferentes não temos como visualizar o que acontece com essa variáveis em um grande banco de dados corporativo. Mas vou apresentar abaixo uma tabela que descreve as colunas do sistemas que influenciam nas transações.

1. xmin. A identidade (ID da transação) da transação de inserção para esta versão de linha. Aqui você começa a entender o MVCC. Toda vez que uma modificação é feita, uma nova linha é inserida. A versão anterior da linha vai ver excluída do banco de dados em um momento posterior por um processo conhecido como VACCUM.

2. xmax. Armazena o ID da transação ("xid") da transação que excluiu a tupla. Lembre-se de que UPDATE também exclui uma tupla no PostgreSQL. Então você passa a ter um intervalo entre o xmin e xmax no qual a tupla é válida. O xmax também pode armazenar a transação que está bloqueando a tupla.

3. cmin. O identificador de comando (começando em zero) dentro da transação de inserção.

4. cmax. O identificador de comando dentro da transação de exclusão ou zero.

Vamos ficando por aqui.

Esperamos que tenha gostado do nosso Bizu!
Bons estudos!
