# Desenvolvimento de Software - DevOps. Infraestrutura. IAC. Ansible. Git e GitLab. Containers. Docker. Kubernetes, OpenShift

Índice

1) Sistemas de Controle de Versão - Conceitos Básicos - Teoria

2) Sistemas de Controle de Versão - Conceitos Básicos - Questões Comentadas.

3) Sistemas de Controle de Versão - Conceitos Básicos - Lista de Questões.

4) Sistemas de Controle de Versão - GIT - Teoria

5) Sistemas de Controle de Versão - GIT - Questões Comentadas.

6) Sistemas de Controle de Versão - GIT - Lista de Questões.

7) Noções Iniciais de DevOps.

8) Docker - Teoria

9) Docker - Questões Comentadas.

10) Docker - Lista de Questões.

11) Kubernets -100% - Teoria

12) Kubernets -100% - Questões Comentadas.

13) Kubernets -100% - Lista deQuestões.

14) OpenShift - 100% - Teoria

15) OpenShift -100% - Questões Comentadas.

16) OpenShift -100% - Lista de Questões.

FERRAMENTAS DE CoNTRoLE DE VERSÃo

Conceitos Básicos

Um sistema de controle de versões (ou versionamento), VCS (do inglês version control system) ou ainda SCM (do inglês source code management) na função prática da Ciência da Computação e daEngenharia de Software, é um software que tem a finalidade de gerenciar diferentes versões no desenvolvimento de um documento qualquer. Esses sistemas são comumente utilizados no desenvolvimento de software para controlar as diferentes versões —histórico e desenvolvimento — dos códigos-fontes e da documentação.
Pessoal, para facilitar, quando disser VCS - do inglês, ou SCV (sistema de controle de versões), estamos nos referindo a um sistema de controle de versão. Por outro lado, o CVS é um sistema de controle de versão que será tratado no próximo tópico sendo um dos controles de versão mais conhecidos, assim como o GIT e o SVN. Tentem lembrar, para não enlouquecer nas siglas. @
Esse tipo de sistema é muito presente em empresas e instituições de tecnologia e desenvolvimento de software. É também muito comum no desenvolvimento de software livre. É útil, em diversos aspectos,tanto para projetos pessoais pequenos e simples como também para grandes projetos comerciais.
Entre os mais comuns encontram-se as soluções livres: CVS, Mercurial, Git e SVN
(Subversion); e as comerciais: SourceSafe, TFS, PVCS (Serena) e ClearCase. O desenvolvimento de software livre utiliza mais o Git (com repositórios no GitHub), que vem substituindo o SVN, que por sua vez é um sucessor do CVS. Muitas empresas também adotam o Git (como a Microsoft com o código fonte doWindows)
ou o SVN, embora algumas empresas prefiram uma solução comercial, optando pelo
ClearCase (da
IBM) ou Team Foundation Server (da Microsoft). Optar por uma solução comercial geralmente está relacionada à garantia, pois as soluções livres não se responsabilizam por erros no software e perdas de informações, Porém as soluções livres podem ter melhor desempenho e segurança que as comerciais. As soluções comerciais apesar de supostas garantias adicionais, não garantem o sucesso da implementação nem indenizam por qualquer tipo de erro mesmo que comprovadamente advindo do software.
A eficácia do controle de versão de software é comprovada por fazer parte das exigências para melhorias do processo de desenvolvimento de certificações tais como CMMI e SPICE.
/ 85

/

Principais vantagens

As principais vantagens de se utilizar um sistema de controle de versão para rastrear as alterações feitas durante o desenvolvimento de software ou o desenvolvimento de um documento de texto qualquer são:
Vantagem | Descrição

Facilidade em desfazer e possibilidade de analisar o histórico do desenvolvimento, como também facilidade no resgate de versões mais
Controle do histórico antigas e estáveis. A maioria das implementações permitem analisar as alterações com detalhes, desde a primeira versão até a última.
Trabalho em equipe

Um sistema de controle de versão permite que diversas pessoas trabalhem sobre o mesmo conjunto de documentos ao mesmo tempo e minimiza o desgaste provocado por problemas com conflitos de edições.É possível que a implementação também tenha um controle sofisticado de acesso para cada usuário ou grupo de usuários.
Marcação e resgate de versões estáveis
A maioria dos sistemas permite marcar onde é que o documento estava com uma versão estável, podendo ser facilmente resgatado no futuro.Ramificação de projeto: a maioria das implementações possibilita a divisão do projeto em várias linhas de desenvolvimento, que podem ser trabalhadas paralelamente, sem que uma interfira na outra.
Segurança

Cada software de controle de versão usa mecanismos para evitar qualquer tipo de invasão de agentes infecciosos nos arquivos. Além do mais, somente usuários com permissão poderão mexer no código.
Rastreabilidade

Com a necessidade de sabermos o local, o estado e a qualidade de um arquivo; o controle de versão traz todos esses requisitos de forma que o usuário possa se embasar do arquivo que deseja utilizar.
Organização

Alguns softwares disponibilizam uma interface visual onde podem ser vistos todos os arquivos controlados, desde a origem até o projeto por completo.
Confiança

O uso de repositórios remotos (na nuvem) ajuda a não perder arquivos por eventos inesperados. Além disso, e possível fazer novos projetos sem danificar o desenvolvimento do atual.
/ 85

/

QUESTõES CoMENTADAS - SISTEMAS DE CoNTRoLE DE

VERSÃo - MULTIBANCAS

1. (FCC - 2011 - TRE-RN - Técnico Judiciário - Programação de Sistemas) São exemplos típicos de ferramentas open source para controle de versão no desenvolvimento de um software:
a) Git, ClearCase e CVS.

b) CVS, SVN e Git.

c) SourceSafe, CVS e ClearCase.

d) SVN, ClearCase e Git.

e) SourceSafe, ClearCase e SVN.

Comentários:

CENTRALIZADO DISTRIBUÍDO

LIVRE COMERCIAL LIVRE COMERCIAL

SCCS (1972)

RCS (1982)

CVS (1990)

CVSNT (1998)

SVN (2000)

CCC/HARVEST
(1977)
CLEARCASE
(1992)
SOURCESAFE
(1994)

PERFORCE (1995)

TFS (2005)

GNU ARCH (2001)

DCVS (2002)

GIT (2005)

MERCURIAL
(2005)

BAZAAR (2005)

TEAMWARE
(1990)

CODE CO-OP
(1997)

BITKEEPER (1998)

PLASTIC SCM
(2006)

Conforme vimos em aula, trata-se do CVS, SVN e GIT! Gabarito: B

2. (CESPE - 2014 - ANATEL - Analista de Sistemas) As ferramentas de controle de versão
Git e
SVN oferecem o mesmo grau de confiabilidade no armazenamento das informações e são ambas implantadas conforme o conceito de sistemas de controle de versão distribuído.
Comentários:

CENTRALIZADO DISTRIBUÍDO

LIVRE COMERCIAL LIVRE COMERCIAL

, 85

SCCS (1972)

RCS (1982)

CVS (1990)

CVSNT (1998)

SVN (2000)

CCC/HARVEST
(1977)
CLEARCASE
(1992)
SOURCESAFE
(1994)

PERFORCE (1995)

TFS (2005)

GNU ARCH (2001)

DCVS (2002)

GIT (2005)

MERCURIAL
(2005)

BAZAAR (2005)

TEAMWARE
(1990)

CODE CO-OP
(1997)

BITKEEPER (1998)

PLASTIC SCM
(2006)

Conforme vimos em aula, SVN é um modelo centralizado e, não, distribuído. Gabarito: E

/ 85

/

LISTA DE QUESTõES - SISTEMAS DE CoNTRoLE DE VERSÃo

- MULTIBANCAS

1. (FCC - 2011 - TRE-RN - Técnico Judiciário - Programação de Sistemas) São exemplos típicos de ferramentas open source para controle de versão no desenvolvimento de um software:
a) Git, ClearCase e CVS.

b) CVS, SVN e Git.

c) SourceSafe, CVS e ClearCase.

d) SVN, ClearCase e Git.

e) SourceSafe, ClearCase e SVN.

2. (CESPE - 2014 - ANATEL - Analista de Sistemas) As ferramentas de controle de versão
Git e
SVN oferecem o mesmo grau de confiabilidade no armazenamento das informações e são ambas implantadas conforme o conceito de sistemas de controle de versão distribuído.
/ 85

/

GABARITo

GABARITO

1. B

2. E

SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023 (Pós-I

GIT

FERRAMENTAS DE CoNTRoLE DE VERSÃo

0 que é "controle de versão", e por que eu deveria me importar?Controle de versão é um sistema que registra alterações em um arquivo ou conjunto de arquivos ao longo do tempo para que você possa lembrar as versões específicas mais tarde. Épossível realizar o Controle de versão com quase qualquer tipo de arquivo em um computador.
Se você é um designer gráfico ou web designer e todas as versões de uma imagem ou layout (o que você certamente deve querer), um sistema de controle de versão (SCV) é a coisa correta a ser usada.
Ele permite que você reverta para um estado anterior determinados arquivos ou um projeto inteiro,compare as mudanças ao longo do tempo, veja quem modificou pela última vez algo que pode estar causando um problema, quem introduziu um problema, quando, e muito mais.
Usar um SCV também significa que se você estragar tudo ou perder arquivos, você pode facilmente recuperar, w . Além disso, você tem tudo isso com muito pouco trabalho. Não é totalmente incrível? V
O método de controle da versão de muitas pessoas é copiar os arquivos para outro diretório (talvez um diretório com carimbo de tempo, se eles são espertos). Esta abordagem é muito comum, porque é incrivelmente propensa a erros. É fácil esquecer em qual diretório você está e acidentalmente sobrescrever o arquivo errado ou copiar arquivos que não quer.
Para lidar com este problema, programadores há muito tempo desenvolveram SCVs locais que tem um banco de dados simples que mantêm todas as alterações nos arquivos sob controle de revisão.
/ 85

/

Local Computer

Checkout Version Database

— -------- Version 3

Version 2

Version 1

Uma das ferramentas SCV mais populares foi um sistema chamado RCS, que ainda é distribuído para muitos computadores. Até mesmo o popular sistema operacional Mac OS X inclui o comando rcs quando você instala as Ferramentas de Desenvolvimento. RCS funciona mantendo conjuntos de alterações (ou seja, as diferenças entre os arquivos) em um formato especial no disco; ele pode, em seguida, recriar como qualquer arquivo se parecia em qualquer ponto no tempo, adicionando-se todas as alterações.
Sistemas Centralizados de Controle de Versão

A próxima questão importante que as pessoas encontram é que elas precisam colaborar com desenvolvedores em outros sistemas. Para lidar com este problema,Sistemas Centralizados de Controle de
Versão (CVCSs) foram desenvolvidos. Estes sistemas, tais como CVS, Subversion ePerforce, têm um único servidor que contém todos os arquivos de controle de versão, e um número de clientes que usam arquivos a partir desse lugar central. Por muitos anos, este tinha sido o padrão para controle de versão.
Esta configuração oferece muitas vantagens, especialmente sobre SCVs locais. Por exemplo,
todos sabem, até certo ponto o que cada um no projeto está fazendo. Os administradores têm controle refinado sobre quem pode fazer o que; e é muito mais fácil de administrar um CVCSdo que lidar com bancos de dados locais em cada cliente.
No entanto, esta configuração também tem algumas desvantagens graves. O mais óbvio é o ponto único de falha que o servidor centralizado representa. Se esse servidor der problema por uma hora,durante essa hora ninguém pode colaborar ou salvar as alterações de versão para o que quer que eles estejam trabalhando. Se o disco rígido do banco de dados central for corrompido,e backups apropriados não foram mantidos, você perde absolutamente tudo - toda a história do projeto,exceto imagens pontuais que desenvolvedores possam ter em suas máquinas locais. Sistemas
SCV

/ 85

/

locais sofrem com esse mesmo problema - sempre que você possui toda a história do projeto em um único lugar, há o risco de perder tudo.
Sistemas Distribuídos de Controle de Versão

É aqui que Sistemas Distribuídos de Controle de Versão (DVCS) entram em cena. Em um
DVCS
(como Git, Mercurial, Bazaar ou Dares), clientes não somente usam o estado mais recente dos arquivos: eles duplicam localmente o repositório completo. Assim, se qualquer servidor morrer, e esses sistemas estiverem colaborando por meio dele, qualquer um dos repositórios de clientes pode ser copiado de volta para o servidor para restaurá-lo. Cada clone é de fato um backup completo de todos os dados.
Além disso, muitos desses sistemas trabalham muito bem com vários repositórios remotos, tal que você possa colaborar em diferentes grupos de pessoas de maneiras diferentes ao mesmo tempo dentro do mesmo projeto. Isso permite que você configure vários tipos de fluxos de trabalho que não são possíveis em sistemas centralizados, como modelos hierárquicos.
Como muitas coisas na vida, o Git começou com um pouco de destruição e uma ardente controvérsia.
O núcleo (kernel) do Linux é um projeto de código aberto com um escopo bastante grande. A maior parte da manutenção do núcleo do Linux 1991-2002), as mudanças no código eram compartilhadas como parte da vida em arquivos. Em 2020, o projeto doLinux começou a usar um núcleo DVCS
chamadoO do BitKeeper.

Em 2005, a relação entre a comunidade que desenvolveu o núcleo do Linux e a empresa que desenvolveu BitKeeper quebrou em pedaços, e a ferramenta passou a ser paga. Isto alertou a comunidade que desenvolvia o Linux (e especialmente Linux Torvalds, o criador do Linux) a desenvolver a sua própria ferramenta baseada em lições aprendidas ao usar o BitKeeper.Algumas metas do novo sistema era os seguintes:
* Velocidade

* Projeto simples

/ 85

/

* Forte suporte para desenvolvimento não-linear (milhares de ramos paralelos)

* Completamente distribuído

* Capacidade de lidar com projetos grandes como o núcleo o Linux com eficiência (velocidade e tamanho dos dados)
Desde seu nascimento em 2005, Git evoluiu e amadureceu para ser fácil de usar e ainda reter essas qualidades iniciais. Ele é incrivelmente rápido, é muito eficiente com projetos grandes,e ele tem um incrível sistema de ramos para desenvolvimento não linear.
O Básico do Git

Então, em poucas palavras, o que é o Git? Esta é uma parte que é importante aprender, porque se você entender o que o Git é e os fundamentos de como ele funciona, em seguida,provavelmente usar efetivamente o Git será muito mais fácil para você.
O Git armazena e vê informações de forma muito diferente do que esses outros sistemas, mesmo que a interface do usuário seja bem semelhante, e entender essas diferenças o ajudará a não ficar confuso.
A principal diferença entre o Git e qualquer outro SCV (Subversion e similares) é a maneira como o
Git trata seus dados. Conceitualmente, a maioria dos outros sistemas armazenam informação como uma lista de mudanças nos arquivos. Estes sistemas (CVS, Subversion, Perforce, Bazaar, e assim por diante) tratam a informação como um conjunto de arquivos e as mudanças feitas em cada arquivo ao longo do tempo.
/ 85

/

Checkins Over Time

File A —► Al A2

File B
Al —► A2

A3

O Git não trata nem armazena seus dados desta forma. Em vez disso, o Git trata seus dados mais como um conjunto de imagens de um sistema de arquivos em miniatura. Toda vez que você fizer um commit, ou salvar o estado de seu projeto no Git, ele basicamente captura uma foto de todos os seus arquivos e armazena uma referência para esse conjunto de arquivos. Para ser eficiente, se os arquivos não foram alterados, o Git não armazena o arquivo novamente, apenas um link para o arquivo idêntico anterior já armazenado. O Git trata seus dados mais como um fluxo do estado dos arquivos.
Checkins Over Time

File A

File B

File C

Al

... J...

Cl

A2 A2

T

BI B2

C2 C3

Esta é uma diferença importante entre o Git e quase todos os outros SCVs. Isto faz o Git reconsiderar quase todos os aspectos de controle de versão que a maioria dos outros sistemas copiaram da geração anterior. Isso faz com que o Git seja mais como um minissistema de arquivos com algumas ferramentas incrivelmente poderosas, ao invés de simplesmente um SCV. Vejamos alguns dos benefícios que você ganha ao tratar seus dados desta forma quando cobrirmos ramificações no Git.
Quase Todas as Operações são locais

A maioria das operações no Git só precisa de arquivos e recursos locais para operar
- geralmente nenhuma informação é necessária de outro computador da rede. Se você estiver acostumado com um CVCS onde a maioria das operações têm aquela demora causada pela latência da rede,este aspecto do Git vai fazer você pensar que os deuses da velocidade abençoaram o Git com poderes extraterrestres. O Como você tem toda a história do projeto ali mesmo em seu disco local, a maioria das operações parecem quase instantâneas.
Por exemplo, para pesquisar o histórico do projeto, o Git não precisa ir para o servidor para obter a história e exibi-la para você - ele simplesmente lê diretamente do seu banco de dados local. Isto significa que você vê o histórico do projeto quase que instantaneamente. Se você quiser ver as alterações introduzidas entre a versão atual de um arquivo e o arquivo de um mês atrás, o Git pode procurar o arquivo de um mês atrás e fazer um cálculo de diferença local, em vez de ter que pedir a um servidor remoto para fazê-lo ou puxar uma versão mais antiga do arquivo do servidor remoto para fazê-lo localmente.
Isto também significa que há muito pouco que você não pode fazer se você estiver desconectado ou sem VPN. Se você estiver em um avião ou um trem e quiser trabalhar um pouco, você pode fazer commits alegremente até conseguir conexão de rede e enviar os arquivos. Se você chegar em casa e não conseguir conectar ao VPN, você ainda poderá trabalhar. Em muitos outros sistemas, isso é impossível ou "doloroso". No Perforce, por exemplo, você não pode fazer quase nada se você não estiver conectado ao servidor; e no Subversion e CVS, você pode editar os arquivos,mas não poderá enviar commits das alterações ao seu banco de dados (porque você não está conectado ao seu banco de dados). Isso pode não parecer muito, mas você poderá se surpreender com a grande diferença que isso pode fazer.
Git tem Integridade

Tudo no Git passa por uma soma de verificações (checksum) antes de ser armazenado e é referenciado por esse checksum. Isto significa que é impossível mudar o conteúdo de qualquer arquivo ou pasta sem que Git saiba. Esta funcionalidade está incorporada no Git nos níveis mais baixos e é parte integrante de sua filosofia. Você não perderá informação durante a transferência e não receberá um arquivo corrompido sem que o Git seja capaz de detectar.
O mecanismo que o Git utiliza para esta soma de verificação é chamado um hash SHA-1. Esta é uma sequência de 40 caracteres composta de caracteres hexadecimais (0-9 e-f) e é calculada com base no conteúdo de uma estrutura de arquivo ou diretório no Git. Um hash SHA-1 é algo como o seguinte:
24b9da6552252987aa493b52f8696cd6d3b00373

Você vai ver esses valores de hash em todo o lugar no Git porque ele os usa com frequência. Na verdade, o Git armazena tudo em seu banco de dados não pelo nome do arquivo, mas pelo valor de hash do seu conteúdo.
/ 85

/

O Cit geralmente somente adiciona dados

Quando você faz algo no Git, quase sempre dados são adicionados no banco de dados do Git - e não removidos. É difícil fazer algo no sistema que não seja reversível ou fazê-lo apagar dados de forma alguma. Como em qualquer SCV, você pode perder alterações que ainda não tenham sido adicionadas em um commit; mas depois de fazer o commit no Git do estado atual das alterações, é muito difícil que haja alguma perda, especialmente se você enviar regularmente o seu banco de dados para outro repositório. Isso faz com que o uso do Git seja somente alegria,porque sabemos que podemos experimentar sem o perigo de estragar algo, ií
Os Três Estados

Agora, preste atenção. Esta é a principal coisa a lembrar sobre Git se você quiser que o resto do seu processo de aprendizagem ocorra sem problemas. O Git tem três estados principais que seus arquivos podem estar: committed, modificado (modified) e preparado (staged).
* Committed significa que os dados estão armazenados de forma segura em seu banco de dados local.
* Modified: significa que você alterou o arquivo, mas ainda não fez o commit no seu banco de dados.
* Staged: significa que você marcou a versão atual de um arquivo modificado para fazer parte de seu próximo commit.
: (VUNESP - FUNDUNESP- 2016) O Git, ao tratar os arquivos que devem sofrer o processo de controle i de versões, classifica o estado desses arquivos em 3 categorias, definidas como i a) checked (verificado), tracked (acompanhado) e identified (identificado).i b) committed (consolidado), modified (modificado) e staged (preparado).

i c) identified (identificado), ignored (ignorado) e committed (consolidado).
i d) ignored (ignorado), ready (pronto) e staged (preparado).

i e) ready (pronto), cloned (clonado) e modified (modificado).

I

i Comentários: O Git tem três estados principais que seus arquivos podem estar: committed,

i modificado (modified) e preparado (staged). (Gabarito: Letra B)

Isso nos leva a três seções principais de um projeto Git: o diretório Git, o diretório de trabalho e área de preparo.
/ 85

/

O diretório Git é onde o Git armazena os metadados e o banco de dados de objetos de seu projeto.Esta é a parte mais importante do Git, e é o que é copiado quando você clona um repositório de outro computador.
O diretório de trabalho é uma simples cópia de uma versão do projeto. Esses arquivos são pegos do banco de dados compactado no diretório Git e colocados no disco para você usar ou modificar.
A área de preparo é um arquivo, geralmente contido em seu diretório Git,
que armazena informações sobre o que vai entrar em seu próximo commit. É por vezes referido como o "índice",mas também é comum referir-se a ele como área de preparo (staging area).

O fluxo de trabalho básico Git é algo assim:

1. Você modifica arquivos no seu diretório de trabalho.

2. Você prepara os arquivos, adicionando imagens deles à sua área de preparo.

3. Você faz commit, o que leva os arquivos como eles estão na área de preparo e armazena essas imagens de forma permanente para o diretório do Git.
Se uma versão específica de um arquivo está no diretório Git, é considerado commited.
Se for modificado, mas foi adicionado à área de preparo, é considerado preparado. E se ele for alterado depois de ter sido carregado, mas não foi preparado, ele é considerado modificado.
Comandos GIT

Pessoal, os comandos, com toda certeza, são os mais cobrados em provas! Portanto,
tenha atenção redobrada!
Comando
Criar novo repositório

Verificar estado dos arquivos/diretórios git init git status
Descrição

Adicionar um arquivo em específico

(staged area)
Adicionar um diretório em específico
Adicionar todos os arquivos/diretórios
Adicionar um arquivo que esta listado no

.gitignore (geral ou do repositório)

Comitar um arquivo

Comitar vários arquivos

Comitar informando mensagem

Remover arquivo
Remover diretório
Exibir histórico

Exibir histórico com diff das duas últimas alteraçõesExibir resumo do histórico (hash completa,
autor, data, comentário e qtde de alterações (+/-))
Exibir informações resumidas em uma linha

(hash completa e comentário)

Exibir histórico com formatação específica
(hash abreviada, autor, data e comentário)

Exibir historio de um arquivo específico

Exibir histórico de um arquivo específico que contêm uma determinada palavraExibir histórico modificação de um arquivo git add meu_arquivo.txt git add meu_diretorio git add .
git add -f arquivo_no_gitignore.txt git commit meu_arquivo.txt git commit meu_arquivo.txt meu_outro_arquivo.txt git commit meuarquivo.txt -m "minha mensagem de commit"
git rm meu_arquivo.txt git rm -r diretorio git log git log -p -2
git log --stat git log --pretty=oneline git log -pretty=format:"%h - %an, %ar: %s"
%h: Abreviação do hash;

%an: Nome do autor;

%ar: Data;

%s: Comentário.

git log -- <caminho_do_arquivo>

git log -summary -S<palavra>
[<caminho_do_arquivo>]

git log —diff-filter=M - <caminho_do_arquivo>

/ 85

/

Exibir revisão e autor da última modificação de uma bloco de linhasDesfazendo alteração local (working directory)1
Desfazendo alteração local (staging area)2
Exibir os repositórios remotos

Vincular repositório local com um repositório remotoExibir informações dos repositórios remotos
Renomear um repositório remoto
Desvincular um repositório remoto

Enviar arquivos/diretórios para o repositório remotoListar configurações

Setar usuário
Setar editor

Setar ferramenta de merge
Atualizar os arquivos no branch atual

Buscar as alterações, mas não aplica-las no branch atual
Clonar um repositório remoto já existente
Usa busca binária para encontrar o commit que introduziu um bug git blame -L 12,22 meu_arquivo.txt git checkout - meu_arquivo.txt git reset HEAD meu_arquivo.txt git remote git remote -v git remote add origin git@github.com:usuario/repositorio git remote show origin git remote rename origin curso-git git remote rm curso-git git push -u origin master git config —list git config -global user.name "nome"git config -global core.editor vim git config -global merge.tool vimdiff git pull git fetch git clone git@<caminho_do_arquivo>git-bisect

: (CESPE - 2020) No GIT, o comando git pull é usado para enviar ao repositório a alteração que foi :
i efetivada no computador local.

i Comentários:

I

i Pessoal, na verdade o comando usado para enviar ao repositório a alteração que foi efetivada no i i computador local é git push. (Gabarito: Errado)
Pessoal, vejamos um arquivo muito cobrado em provas que é o gitignore.
Basicamente, ele especifica arquivos não rastreados intencionalmente para ignorar. Um arquivo gitignore especifica arquivos não rastreados intencionalmente que o Git deve ignorar. Arquivos já rastreados pelo Git não são afetados.
Este comando deve ser utilizando enquanto o arquivo não foi adicionado na staged area.
Este comando deve ser utilizando quando o arquivo já foi adicionado na staged area.

/ 85

/

Cada linha em um arquivo gitignore especifica um padrão. Ao decidir ignorar um caminho, o Git normalmente verifica padrões gitignore de várias fontes, com a seguinte ordem de precedência, do maior para o menor (dentro de um nível de precedência, o último padrão correspondente decide o resultado):
Padrões lidos de um arquivo, gitignore no mesmo diretório que o caminho, ou em qualquer diretório pai (até o nível superior da árvore de trabalho), com padrões nos arquivos de nível superior sendo substituídos por aqueles em arquivos de nível inferior no diretório contendo o arquivo. Esses padrões correspondem à localização do arquivo .gitignore. Um projeto normalmente inclui esses arquivos .gitignore em seu repositório, contendo padrões para arquivos gerados como parte da construção do projeto.
/ 85

/

Questões Comentadas

1. (FCC - PGE-AM - 2022) Um Técnico utilizou corretamente um comando git para modificar a mensagem do commit mais recente, ou seja, o último commit feito por ele no projeto.Trata-se do comando git a) add merge.
b) push.

c) commit -amend.

d) add message.

e) checkout master.

Comentários: Pessoal, o comando commit -amend é usado para alterar o commit mais recente,veja: Alterar seu commit mais recente é provavelmente a reescrita mais comum do histórico que você fará. Muitas vezes você vai querer fazer duas coisas básicas no seu último commit:simplesmente mudar a mensagem do commit, ou mudar o conteúdo real do commit adicionando,removendo e modificando arquivos. Se você simplesmente deseja modificar sua última mensagem de confirmação, é só útilizar o comando: git commit -amend. Para complementar o conhecimento,o comando git commit -amend carrega a mensagem de confirmação anterior em uma sessão do editor, onde você pode fazer alterações na mensagem, salvar essas alterações e sair.Quando você salva e fecha o editor, o editor escreve um novo commit contendo essa mensagem de commit atualizada e o torna seu novo último commit.
Gabarito: Letra C

2. (FGV - TJDFT - 2022) O analista Mateus configurou um pipeline CI/CD para o projeto TJApp noGitLab. O repositório de TJApp denomina-se TJAppRepo. Mateus precisou controlar o comportamento do pipeline de TJApp condicionando o início de sua execução aos eventos de push de tags para o TJAppRepo.
Para aplicar essa condição ao pipeline de TJApp, Mateus precisou modificar o arquivo gitlab-ci.yml na raiz de TJAppRepo, adicionando uma regra na seção:

a) default;

b) include;

c) stages;

d) variables;

e) workflow.

Comentários: Pessoal, vejamos o que pede a questão: Uma configuração de pipeline GitLab
CI/CD
inclui: Palavras- chave globais que configuram o comportamento do pipeline.
default: Valores padrão personalizados para palavras-chave de trabalho, include: Importe a configuração de outros arquivos YAML. stages: Os nomes e a ordem dos estágios do pipeline. variables: Defina variáveis
CI/CD para todos os trabalhos no pipeline. workflow: Controle quais tipos de pipeline são executados. Pessoal, a questão foi contextualizada, mas é necessário se ater ao que foi solicitado:controlar o comportamento do pipeline, dessa forma, temos nosso gabarito na letra e)
workflow:
Controla quais tipos de pipeline são executados.

Gabarito: Letra E

3. (FGV - TJ TO - 2022) O técnico em informática José está desenvolvendo o software
TJTOPIugin com o apoio da ferramenta de versionamento Git. José criou o branch local pluginConnector e efetuou alguns commits neste branch, mas não replicou os commits em um repositório remoto.
A fim de replicar os commits e criar o branch pluginConnector no repositório remoto origin,utilizando um único comando no terminal de comandos do sistema operacional,
José deve executar o comando git com os argumentos:
a) mv pluginConnector origin;

b) diff pluginConnector origin;

c) merge origin/pluginConnector;

d) push origin pluginConnector;

e) remote add origin pluginConnector.

Comentários: Pessoal, o comando git-push atualiza referências remotas junto com objetos associados o técnico em informática José deseja replicar os commits e criar o branch pluginConnector no repositório remoto origin. Assim ele deve usar o comando git push origin pluginConnector. Já que esse comando atualiza referências remotas usando referências locais,enquanto envia objetos necessários para completar as referências fornecidas.

Gabarito: Letra D

4. (UFRPE - UFRPE - 2022) O git é um sistema de controle de versão distribuído e utilizado amplamente pela comunidade de desenvolvimento de software. Esse sistema possui um conjunto de comandos utilizados para o versionamento de código. Dito isso, qual o comando utilizado para enviar as alterações do repositório local para o repositório remoto?
a) git commit b) git push c) git add d) git pull e) git send
Comentários: Vamos relembrar cada comando: a) git commit: Comitar um arquivo, b) git push:Enviar arquivos/diretórios para o repositório remoto, c) git add: Adicionar um arquivo, d) git pull:
/ 85

/

Atualizar os arquivos no branch atual, e) git send: provavelmente o examinador quis dizer: git send-email: envia um e-mail.

Gabarito: Letra B

5. (CESPE - MPE CE - 2020) GitHub é uma plataforma de hospedagem de código que permite realizar o controle de versão de software, de modo que várias pessoas contribuam simultaneamente no mesmo projeto, editando e criando novos arquivos, sem o risco de suas alterações serem sobrescritas.
Comentários: Pessoal, definição perfeita do Git. GitHub é uma plataforma de hospedagem de código-fonte e arquivos com controle de versão usando o Git. Ele permite que programadores,utilitários ou qualquer usuário cadastrado na plataforma contribuam em projetos privados e/ouOpen Source de qualquer lugar do mundo. GitHub é amplamente utilizado por programadores para divulgação de seus trabalhos ou para que outros programadores contribuam com o projeto,além de promover fácil comunicação através de recursos que relatam problemas ou mesclam repositórios remotos
Gabarito: Correto

6. (CESPE - Ministério da Economia - 2020) O comando git clone permite baixar o repositório doGitHub para o computador do usuário.

Comentários: Pessoal, vejamos a definição do comando citado: git clone git@<caminho_do_arquivo>: Clonar um repositório remoto já existente, além disso,git-clone -
Clona um repositório em um novo diretório.

Gabarito: Correto

7. (CESPE - Ministério da Economia - 2020) No GIT, o comando git pull é usado para enviar ao repositório a alteração que foi efetivada no computador local.
Comentários: Pessoal, na verdade o comando usado para enviar ao repositório a alteração que foi efetivada no computador local é git push.
Gabarito: Errado

8. (UFRN - UFRN - 2020) O git é um sistema de controle de versão muito utilizado em desenvolvimento de sistemas de software. Sobre o git, é correto afirmar:
a) O comando git push é utilizado para envio das alterações confirmadas no diretório local para o repositório remoto.
b) O comando git clone faz a cópia apenas dos arquivos, sendo as informações do repositório inicializadas como no comando git init.
/ 85

/

c) O comando git add faz a confirmação das alterações de forma definitiva.

d) O comando git checkout faz uma atualização do diretório local com o diretório remoto.

Comentários: Pessoal vamos ver as definições dos comandos: git push envia arquivos/diretórios para o repositório remoto - Nosso gabarito! vejamos os demais comandos, git clone clona um repositório remoto, git add Adicionar um arquivo, git checkout desfaz alteração local.
Gabarito: Letra A

9. (UFC - UFC - 2019) Qual arquivo é necessário ser configurado para especificar intencionalmente que determinados arquivos não sejam rastreados (tracked) e que o Git deve ignorar no repositório Git local?
a) ignore.git b).gitignore c) git.ignore d) gitignore.txt e) .gitignore.txt
Comentários: O comando gitignore especifica arquivos não rastreados intencionalmente para ignorar. Arquivos já rastreados pelo Git não são afetados. Cada linha em um arquivo gitignore especifica um padrão. Portanto, o arquivo a ser configurado para especificar intencionalmente que determinados arquivos não sejam rastreados é o gitignore.
Gabarito: Letra B

10.(UFRN - Câmara de Parnamirim - 2019) A utilização do conceito de branches em sistemas de controle de versão permite ao desenvolvedor divergir da linha principal de desenvolvimento. Ao criar várias branches, o desenvolvedor deverá tomar cuidado para escolher a branch correta para iniciar qualquer modificação. Utilizando o sistema de versionamento de código GiT, para entrar em uma branch denominada mobile, utiliza-se o comando a) git branch mobile b) git checkout mobile c) git status mobile d) git change mobile
Comentários: Pessoal, o mais importante é saber o que cada comando faz: git-branch:
Lista, cria ou exclui branches. git-checkout: Troque ramificações ou restaure os arquivos da árvore de trabalho -nosso gabarito, git-status: Mostra o status da árvore de trabalho. Por fim,
git change não foi identificado.
Gabarito: Letra B

/ 85

/

11. (Quadrix - CRM-PR - 2018) A ferramenta SVN (subversion) realiza o controle de versão de software por meio do uso da plataforma Mercurial.
Comentários: Mercurial e SVN são sistemas de controle de versão. Ademais, o SVN não usa a plataforma Mercurial.
Gabarito: Errado

12. (FCC - Prefeitura de São Luís - MA - 2018) Um Auditor Fiscal fez uma pesquisa na internet e obteve as seguintes informações:
Há vários critérios para escolher uma ferramenta para esta finalidade, como popularidade,eficácia, desempenho, adequação e simplicidade. Este tipo de ferramenta serve para resolver três problemas:
I. registrar a evolução do projeto;

II. possibilitar o trabalho em equipe;

III. criar e manter variações do projeto.

Tanto o Subversion, quanto o Git e o Mercurial atendem estas necessidades.

O Auditor estava pesquisando sobre ferramentas de a) projeto e governança de portais corporativos.
b) controle de workflows e Business Process Management (BPM).

c) Gerenciamento Eletrônico de Documentos (GED) de projetos.

d) controle e gerenciamento de versão.

e) projetos de auditoria com base no PMBOK 5ã edição.

Comentários: Bem contextualizada a questão (a cara da FCC). Bom, há a descrição das características dos controle e gerenciamento de versão e a banca ainda solta dois sistemas muito comhecidos: Git e o Mercurial. Daí podemos marcar nosso gabarito na letra D.
Gabarito: Letra D

13. (CESPE - TRE TO - 2017) Considerando um programa em linguagem Java, assinale a opção que apresenta o comando do versionador Git que permite criar uma branch de nome new_branch e mudar para essa branch ao mesmo tempo.
a) git log new_branch b) git clone new_branch c) git checkout -b new_branch d) git init new_branch e) git commit -m 'new_branch'
/ 85

/

Comentários: O comando correto é: git checkout -b new_branch. Especificar -b faz com que um novo branch seja criado como se git-branch fosse chamado. Vejamos a definição de cada um deles, git log: Exibe o histórico, git clone: Clonar um repositório remoto, git init: Cria um novo repositório, git commit: Comita um arquivo.
Gabarito: Letra C

14. (UFPE - UFPE- 2017) Quando se usa o controle de versão através da ferramenta GIT, é possível interromper o fluxo de trabalho por meio da funcionalidade <STASH>. Pelo comando <git stash>,se faz possível:

a) criar uma ramificação (branching).

b) unificar ramificações (merging).

c) gerar uma solicitação de integração (pull request).

d) reverter a versão do código a uma versão específica (cherry pick).

e) exibir as diferenças entre duas versões quaisquer do código (diff).

Comentários: git-stash esconde as alterações em um diretório de trabalho sujo, ou seja,
retira toda sujeira do seu diretório de trabalho. Use git stashquando quiser gravar o estado atual do diretório de trabalho e o índice, mas quiser voltar para um diretório de trabalho limpo. Ocomando salva suas modificações locais e reverte o diretório de trabalho para corresponder ao HEAD commit.
Gabarito: Letra A

15. (UFPE - UFPE - 2017) O GIT é um sistema de controle de versão distribuído, e também um gerenciamento de código fonte. Projetado e desenvolvido por Linus Torvalds, a ferramenta foi utilizada por muitos projetos ao redor do mundo. A respeito do Git, é incorreto afirmar que:
a) o comando 'git commit' grava as mudanças realizadas no repositório atual.

b) o comando 'git clone' copia um repositório existente em um novo diretório.

c) o comando 'git reset' modifica a HEAD atual para um estado específico.

d) o comando 'git init' pode reinicializar um repositório já criado.

e) o comando 'git bisect' divide o repositório atual em um ou mais repositórios diferentes.

Comentários: Pessoal, vejamos a descricao de cada comando: git commit: Grava alterações no repositório, git clone: Clona/copia um repositório em um novo diretório, git-reset:Redefine/modifica o HEAD atual para o estado especificado, git-init: Cria um repositório
Git vazio ou reinicializa um existente, git bisect: Use busca binária para encontrar o commit que introduziu um bug. Como a banca pede a alternativa incorreta, nosso gabarito é a letra E.
Gabarito: Letra E

16. (UFPE - UFPE- 2017) A respeito de sistemas de controle de versão, assinale a alternativa correta.
a) O SVN pode ser considerado um sistema de controle de versão distribuído.

/ 85

/

b) 0 GIT pode ser considerado um sistema de controle de versão centralizado.

c) Um conflito representa uma situação onde dois usuários modificam o mesmo arquivo em intervalos de tempo distintos.
d) A operação de mesclagem (merge, em inglês) consiste na junção automática de diferentes versões de um arquivo.
e) Uma cópia local sempre estará atualizada quando se usa o controle de versões GIT.

Comentários: Vamos comentar cada alternativa: a letra a está errada, porque na verdade,
o SVN é centralizado. O Git é distribuído. Letra B está incorreta. Na verdade, um conflito representa uma situação onde dois usuários modificam o mesmo arquivo no mesmo intervalo de tempo. Por outro lado, a letra C está correta: A operação de mesclagem (merge, em inglês) consiste na junção automática de diferentes versões de um arquivo. A letra E está incorreta, na verdade é preciso executar o comando git pull ou o git fetch para atualizar.
Gabarito: Letra B

17. (FCC - Prefeitura de Teresina - PI - 2016) No sistema de controle de versões Mercurial, para exibir, em detalhes, cada evento que ocorreu no repositório utiliza-se o comando a) hg status all.
b) hg view -log.

c) svg all.

d) hg log -v.

e) hgrc show -a.

Comentários: o comando hg log -v mostra o histórico de revisões de todo o repositório ou arquivos.

Gabarito: Letra D

18. (VUNESP - FUNDUNESP- 2016) O Git, ao tratar os arquivos que devem sofrer o processo de controle de versões, classifica o estado desses arquivos em 3 categorias, definidas como a) checked (verificado), tracked (acompanhado) e identified (identificado).
b) committed (consolidado), modified (modificado) e staged (preparado).

c) identified (identificado), ignored (ignorado) e committed (consolidado).

d) ignored (ignorado), ready (pronto) e staged (preparado).

e) ready (pronto), cloned (clonado) e modified (modificado).

Comentários: O Git tem três estados principais que seus arquivos podem estar:
committed,
modificado (modified) e preparado (staged).

Gabarito: Letra B

19. (BIO-RIO - Pref São Gonçalo - 2016) No que diz respeito às características das ferramentas de controle de versão SVN e GIT, analise as afirmativas a seguir.
/ 85

/

I. SVN opera de forma centralizada, enquanto o GIT de forma distribuída.

II. SVN opera exclusivamente em distribuições Linux, enquanto o GIT
exclusivamente em ambientes Windows.
III. SVN suporta a operação de commit de forma atômica, ou seja, se a operação for interrompida pelo meio ela é desconsiderada, como por exemplo, em situações de queda de energia,diferentemente do GIT.

Assinale a alternativa correta:

a) somente a afirmativa I está correta.

b) somente a afirmativa II está correta.

c) somente a afirmativa III está correta.

d) somente as afirmativas I e II estão corretas.

e) todas as afirmativas estão corretas.

Comentários: Novamente, os Sistemas Centralizados de Controle de Versão (CVCSs) são: CVS,
Subversion (SVN) e Perforce. Já, Sistemas Distribuídos de Controle de Versão (DVCS)
temos como exemplo Git, Mercurial, Bazaar ou Dares. Sabendo disso, temos que o item I está correto, o item IIestá incorreto porque SVN e Git são multiplataforma. Ademais, ambos suportam commit atômico.

Gabarito: Letra A

20. (CESPE - STJ - 2015) O Git, sistema de controle de versões que mantém um histórico completo de todas as alterações, permite a recuperação das versões do projeto na busca de informações sobre o estado dos arquivos em versões anteriores.
Comentários: O Git é o sistema de controle de versão mais usado atualmente e está rapidamente se tornando o padrão para o controle de versão. Git é um sistema de controle de versão distribuído,o que significa que sua cópia local do código é um repositório completo de controle de versão. Esses repositórios locais totalmente funcionais facilitam o trabalho off-line ou remotamente.Você faz o commit do seu trabalho localmente e sincroniza sua cópia do repositório com a cópia no servidor.Esse paradigma difere do controle de versão centralizado, em que os clientes devem sincronizar o código com um servidor antes de criar novas versões de código. Ademais, o git permite a recuperação das versões do projeto na busca de informações sobre o estado dos arquivos em versões anteriores. Perfeita questão!
Gabarito: Correto

/ 85

/

21. (CESPE - ANATAQ - 2014) As ferramentas de controle de versão Git e SVN oferecem o mesmo grau de confiabilidade no armazenamento das informações e são ambas implantadas conforme o conceito de sistemas de controle de versão distribuído.
Comentários: Em um DVCS (tais como Git, Mercurial, Bazaar ou Dares), os clientes não apenas fazem cópias das últimas versões dos arquivos: eles são cópias completas do repositório.Assim, se um servidor falha, qualquer um dos repositórios dos clientes pode ser copiado de volta para o servidor para restaurá-lo. Cada checkout (resgate) é na prática um backup completo de todos os dados.Vimos que o Git é distribuído. Por outro lado, o SVN é centralizado, vejamos: Apache
Subversion,
também conhecido como Subversion, SVN representa o sistema de controle de versão centralizado mais popular do mercado. Com um sistema centralizado, todos os arquivos e dados históricos são armazenados em um servidor central. Os desenvolvedores podem confirmar suas alterações diretamente nesse repositório do servidor central.
Gabarito: Errado

22. (CESPE - ANATEL - 2014) Os comandos da ferramenta Git são relativamente simples:
para adicionar, por exemplo, um arquivo novo ao repositório no Git, basta utilizar o comando commit depois de efetuar o comando add.
Comentários: Pessoal, o comando para adicionar um arquivo novo ao repositório é o git add

Gabarito: Correto

/ 85

/

Lista de Questões

1. (FCC - PGE-AM - 2022) Um Técnico utilizou corretamente um comando git para modificar a mensagem do commit mais recente, ou seja, o último commit feito por ele no projeto.Trata-se do comando git a) add merge.
b) push.

c) commit -amend.

d) add message.

e) checkout master.

2. (FGV - TJDFT - 2022) O analista Mateus configurou um pipeline CI/CD para o projeto TJApp noGitLab. O repositório de TJApp denomina-se TJAppRepo. Mateus precisou controlar o comportamento do pipeline de TJApp condicionando o início de sua execução aos eventos de push de tags para o TJAppRepo.
Para aplicar essa condição ao pipeline de TJApp, Mateus precisou modificar o arquivo gitlab-ci.yml na raiz de TJAppRepo, adicionando uma regra na seção:

a) default;

b) include;

c) stages;

d) variables;

e) workflow.

3. (FGV - TJ TO - 2022) O técnico em informática José está desenvolvendo o software TJTOPlugin com o apoio da ferramenta de versionamento Git. José criou o branch local pluginConnector e efetuou alguns commits neste branch, mas não replicou os commits em um repositório remoto.
A fim de replicar os commits e criar o branch pluginConnector no repositório remoto origin,utilizando um único comando no terminal de comandos do sistema operacional,
José deve executar o comando git com os argumentos:
a) mv pluginConnector origin;

b) diff pluginConnector origin;

c) merge origin/pluginConnector;

d) push origin pluginConnector;

e) remote add origin pluginConnector.

/ 85

/

4. (UFRPE - UFRPE - 2022) O git é um sistema de controle de versão distribuído e utilizado amplamente pela comunidade de desenvolvimento de software. Esse sistema possui um conjunto de comandos utilizados para o versionamento de código. Dito isso, qual o comando utilizado para enviar as alterações do repositório local para o repositório remoto?
a) git commit b) git push c) git add d) git pull e) git send
5. (CESPE - MPE CE - 2020) GitHub é uma plataforma de hospedagem de código que permite realizar o controle de versão de software, de modo que várias pessoas contribuam simultaneamente no mesmo projeto, editando e criando novos arquivos, sem o risco de suas alterações serem sobrescritas.
6. (CESPE - Ministério da Economia - 2020) O comando git clone permite baixar o repositório doGitHub para o computador do usuário.

7. (CESPE - Ministério da Economia - 2020) No GIT, o comando git pull é usado para enviar ao repositório a alteração que foi efetivada no computador local.
8. (UFRN - UFRN - 2020) O git é um sistema de controle de versão muito utilizado em desenvolvimento de sistemas de software. Sobre o git, é correto afirmar:
a) O comando git push é utilizado para envio das alterações confirmadas no diretório local para o repositório remoto.
b) O comando git clone faz a cópia apenas dos arquivos, sendo as informações do repositório inicializadas como no comando git init.
c) O comando git add faz a confirmação das alterações de forma definitiva.

d) O comando git checkout faz uma atualização do diretório local com o diretório remoto.

9. (UFC - UFC - 2019) Qual arquivo é necessário ser configurado para especificar intencionalmente que determinados arquivos não sejam rastreados (tracked) e que o Git deve ignorar no repositório Git local?
a) ignore.git b).gitignore c) git.ignore d) gitignore.txt e) .gitignore.txt
/ 85

/

10. (UFRN - Câmara de Parnamirim - 2019) A utilização do conceito de branches em sistemas de controle de versão permite ao desenvolvedor divergir da linha principal de desenvolvimento. Ao criar várias branches, o desenvolvedor deverá tomar cuidado para escolher a branch correta para iniciar qualquer modificação. Utilizando o sistema de versionamento de código GiT, para entrar em uma branch denominada mobile, utiliza-se o comando a) git branch mobile b) git checkout mobile c) git status mobile d) git change mobile
11. (Quadrix - CRM-PR - 2018) A ferramenta SVN (subversion) realiza o controle de versão de software por meio do uso da plataforma Mercurial.
12. (FCC - Prefeitura de São Luís - MA - 2018) Um Auditor Fiscal fez uma pesquisa na internet e obteve as seguintes informações:
Há vários critérios para escolher uma ferramenta para esta finalidade, como popularidade,eficácia, desempenho, adequação e simplicidade. Este tipo de ferramenta serve para resolver três problemas:
I. registrar a evolução do projeto;

II. possibilitar o trabalho em equipe;

III. criar e manter variações do projeto.

Tanto o Subversion, quanto o Git e o Mercurial atendem estas necessidades.

O Auditor estava pesquisando sobre ferramentas de a) projeto e governança de portais corporativos.
b) controle de workflows e Business Process Management (BPM).

c) Gerenciamento Eletrônico de Documentos (GED) de projetos.

d) controle e gerenciamento de versão.

e) projetos de auditoria com base no PMBOK edição.

13. (CESPE - TRE TO - 2017) Considerando um programa em linguagem Java, assinale a opção que apresenta o comando do versionador Git que permite criar uma branch de nome new_branch e mudar para essa branch ao mesmo tempo.
a) git log new_branch b) git clone new_branch c) git checkout -b new_branch d) git init new_branch
/ 85

e) git commit -m 'new_branch'

14. (UFPE - UFPE- 2017) Quando se usa o controle de versão através da ferramenta GIT,
é possível interromper o fluxo de trabalho por meio da funcionalidade <STASH>. Pelo comando <git stash>,se faz possível:

a) criar uma ramificação (branching).

b) unificar ramificações (merging).

c) gerar uma solicitação de integração (pull request).

d) reverter a versão do código a uma versão específica (cherry pick).

e) exibir as diferenças entre duas versões quaisquer do código (diff).

15. (UFPE - UFPE - 2017) O GIT é um sistema de controle de versão distribuído, e também um gerenciamento de código fonte. Projetado e desenvolvido por Linus Torvalds, a ferramenta foi utilizada por muitos projetos ao redor do mundo. A respeito do Git, é incorreto afirmar que:
a) o comando 'git commit' grava as mudanças realizadas no repositório atual.

b) o comando 'git clone' copia um repositório existente em um novo diretório.

c) o comando 'git reset' modifica a HEAD atual para um estado específico.

d) o comando 'git init' pode reinicializar um repositório já criado.

e) o comando 'git bisect' divide o repositório atual em um ou mais repositórios diferentes.

16. (UFPE - UFPE- 2017) A respeito de sistemas de controle de versão, assinale a alternativa correta.
a) O SVN pode ser considerado um sistema de controle de versão distribuído.

b) O GIT pode ser considerado um sistema de controle de versão centralizado.

c) Um conflito representa uma situação onde dois usuários modificam o mesmo arquivo em intervalos de tempo distintos.
d) A operação de mesclagem (merge, em inglês) consiste na junção automática de diferentes versões de um arquivo.
e) Uma cópia local sempre estará atualizada quando se usa o controle de versões GIT.

17. (FCC - Prefeitura de Teresina - PI - 2016) No sistema de controle de versões
Mercurial, para exibir, em detalhes, cada evento que ocorreu no repositório utiliza-se o comando a) hg status all.
b) hg view -log.

c) svg all.

d) hg log -v.

e) hgrc show -a.

x

/ 35

/

18. (VUNESP - FUNDUNESP- 2016) O Git, ao tratar os arquivos que devem sofrer o processo de controle de versões, classifica o estado desses arquivos em 3 categorias, definidas como a) checked (verificado), tracked (acompanhado) e identified (identificado).
b) committed (consolidado), modified (modificado) e staged (preparado).

c) identified (identificado), ignored (ignorado) e committed (consolidado).

d) ignored (ignorado), ready (pronto) e staged (preparado).

e) ready (pronto), cloned (clonado) e modified (modificado).

19. (BIO-RIO - Pref São Gonçalo - 2016) No que diz respeito às características das ferramentas de controle de versão SVN e GIT, analise as afirmativas a seguir.
I. SVN opera de forma centralizada, enquanto o GIT de forma distribuída.

II. SVN opera exclusivamente em distribuições Linux, enquanto o GIT
exclusivamente em ambientes Windows.
III. SVN suporta a operação de commit de forma atômica, ou seja, se a operação for interrompida pelo meio ela é desconsiderada, como por exemplo, em situações de queda de energia,diferentemente do GIT.

Assinale a alternativa correta:

a) somente a afirmativa I está correta.

b) somente a afirmativa II está correta.

c) somente a afirmativa III está correta.

d) somente as afirmativas I e II estão corretas.

e) todas as afirmativas estão corretas.

20. (CESPE - STJ - 2015) O Git, sistema de controle de versões que mantém um histórico completo de todas as alterações, permite a recuperação das versões do projeto na busca de informações sobre o estado dos arquivos em versões anteriores.
21. (CESPE - ANATAQ - 2014) As ferramentas de controle de versão Git e SVN oferecem o mesmo grau de confiabilidade no armazenamento das informações e são ambas implantadas conforme o conceito de sistemas de controle de versão distribuído.
22. (CESPE - ANATEL - 2014) Os comandos da ferramenta Git são relativamente simples:
para adicionar, por exemplo, um arquivo novo ao repositório no Git, basta utilizar o comando commit depois de efetuar o comando add.
/ 85

/

GABARITo

1. LETRA C 9. LETRA B
17. LETRA D

2. LETRA E 10. LETRA B
18. LETRA B

3. LETRA D 11. ERRADO
19. LETRA A

4. LETRA B 12. LETRA D
20. CORRETO

5. CORRETO 13. LETRA C
21. ERRADO

6. CORRETO 14. LETRA A
22. CORRETO

7. ERRADO 15. LETRA E

8. LETRA A 16. LETRA B

x

/ 35

/

Conceitos Básicos

INCIDÊNCIA EM PROVA: MÉDIA

De um tempo para cá, nós temos vivenciado novos paradigmas em tecnologias de software.
As metodologias ágeis, por exemplo, vieram com um conjunto de práticas que desencadearam diversas outras práticas, de forma a obter software de maneira mais ágil e mais adaptável a possíveis mudanças. No entanto, o grande lance é que as mudanças ocorrem com um intervalo de tempo cada vez menor.
Vocês já devem ter percebido isso! Antigamente, softwares lançavam atualizações em intervalos de 18 a 24 meses (ou até mais). Atualmente, a dinâmica de consumo de aplicações de tecnologia da informação sofreu uma reviravolta e a demanda dos clientes é insana. As empresas de software atualmente são duramente pressionadas para lançar e atualizar aplicativos no mercado o mais rápido possível.
Pois é, o mundo mudou! O ciclo para a criação de novos aplicativos de software dura cerca de três meses para uma versão inicial e mais seis meses para o conjunto completo de recursos.Não só o ciclo de vida foi encurtado, mas os aplicativos se tornaram muito mais complexos e exigem colaboração e integração cruzada entre os diversos componentes de tecnologia da informação,como Dev, Ops e Q&A.

/ 85

/

Professor, espera um pouco aí! O que acontece se eu juntar conceitos de Desenvolvimento de Software,
Operação de Sistemas e Garantia de Qualidade? Surgirá, então, o conceito de DevOps!
Trata-se de um conceito muito simples, como apresenta a imagem acima. Essas ideias são tratadas em conjunto, em vez de separadas. O lance é ter uma maior comunicação, colaboração e integração entre essas áreas.
DEV

Professor, o que é exatamente DevOps? É uma cultura? É uma técnica? É uma metodologia de desenvolvimento de software? Ainda não existe uma resposta precisa para essas perguntas!Porque,
professor? Porque foi um movimento que começou ao mesmo tempo em diversos lugares diferentes, tratando de infraestrutura e desenvolvimento, mas não houve um manifesto formal, como o manifesto ágil.
The Dev

Innovates and creates applications.
DevOps disciplines

Integrate and automate processes.

The benefits of DevOps1

Percent improvement in business areas.

COLLABORATION 23%

APP QUALITY 22%

CUSTOMERS 22%

The Ops

NEW SERVICES 21%

Keeps infrastructure running smoothly.
TIME-TO-MARKET
REVENUE

20%

19%

COST SAVINGS 18%

DEPLOY FREQUENCY 17%

www. estra tegiaconcursos. com. br

Parece simples fazer a infraestrutura conversar de forma harmônica com o desenvolvimento,
mas não é tão fácil! Qual é o papel da infraestrutura? É sustentar os sistemas em produção;monitorar o funcionamento e a performance; cuidar da estabilidade, segurança, níveis de serviço;planejar mudanças, minimizando riscos; entre outros. O que acontece se uma aplicação em produção parar de funcionar?
Oneteam, onegoal

Development IT Operations ness and the NOC's concern with quality and stability on the ultimate goal of providing business value.
Source HP

Isso pode significar prejuízo financeiro ou institucional. Em suma, podemos dizer que a infraestrutura se preocupa em proteger o valor de negócio. E o desenvolvimento? Esses caras se preocupam com inovação e criatividade, baseado nos requisitos do usuário.Desenvolvedor fica louco quando sai uma biblioteca, componente ou tecnologia nova. A consequência disso é que cada inovação significa um novo Deploy (feito pela rapaziada da infraestrutura).
E se ocorrer algum problema? Deve ser realizado um rollback (também pelo pessoal da infraestrutura). Podemos afirmar, então, que o desenvolvedor se preocupa em aumentar o valor do negócio. Vocês já devem ter notado que há um conflito interessante nessa conversa.Ora, o desenvolvedor quer colocar suas aplicações no ar o mais rápido possível para que fique disponível para o cliente.
No entanto, a galera da infraestrutura quer ter certeza de que a aplicação está suficientemente estável para ir para produção sem gerar incidentes que parem o que já está funcionando. O que ocorria antigamente? As empresas permitiam apenas um deploy por semana ou por mês! Tem coisa mais não-ágil que isso? Vai totalmente de encontro aos ideais do manifesto ágil.Lembram-se dos conceitos de entrega, integração e teste contínuos?
Pois é, a infraestrutura teve que se adaptar a realizar deploys diários. No entanto, os desenvolvedores - muitas vezes - se esqueciam de considerar algumas diferenças importantes entre ambientes de desenvolvimento e produção. Isso gerava alguns incidentes, o cliente reclamava e começava uma briga muito comum representada pelas duas imagens anteriores.Sim, galera... rola essa briga!

Desenvolvedores afirmando que a Infraestrutura é engessada, lenta e que não oferece um ambiente adequado para o desenvolvimento de aplicações; já a Infraestrutura afirmava que os desenvolvedores faziam código ruim e instável, e que a culpa não era deles. Pessoal,voltem agora para a primeira imagem e percebam o que DevOps tenta integrar:Desenvolvimento,
Infraestrutura e Qualidade!

Parece briga de marido e mulher, mas ambos os lados têm que reconhecer seus erros,
ceder e se adaptar! O Desenvolvimento precisa pensar mais na Infraestrutura e controlar as fases de deploy (Ex: Deployment Pipeline). Já a Infraestrutura tem que evoluir para o mundo ágil.Começar a trabalhar de forma automatizada e dinâmica, ser mais veloz para subir ambientes;reconstruir ou duplicar ambientes de acordo com as necessidades do Desenvolvimento.

Galera, as principais características do DevOps são: colaboração entre equipes; fim de divisões;relação saudável entre áreas; teste, integração e entrega contínuos; automação de deploy; controle e monitoração; gerenciamento de configuração; orquestração de serviços; avaliação de métricas e desempenho; logs e integração; velocidade de entrega; feedback intenso;e comunicação constante.
Em suma, podemos dizerque ele é um movimento, um conceito, uma cultura, uma abordagem que trata do feedback, comunicação e colaboração entre áreas de tecnologia da informação com o objetivo de garantir qualidade do software, com menor custo, mais rapidez, menor risco e maior eficiência. É como se fosse a utilização de metodologias ágeis no desenvolvimento e na infraestrutura. Bacana?
Para o DevOps, o código gerado pela infraestrutura é apenas mais um artefato qualquer de desenvolvimento e, não, uma parte separada. Trata-se de uma prática importante, já que não basta somente o desenvolvedor escrever o código do sistema, é necessário que a área de infraestrutura também atue para liberar, controlar e entregar a versão do sistema de forma contínua, periódica e preferencialmente automática.
Z 85

/

TODAY'S DEVOPS

PART DEV PART OPS

Application
Performance

Modem developers use APM
tools to decrease latency, have complete visibility into code,databases, caches, queues,
and third-party services.

Application
Availability

The applications need to be up and running and it's Ops responsibility to ensure uptime and SLAs are in order.
End User
Analytics

A great developer understands end users have the best feedback and analytics play an enormous part of understanding users. Developers are constantly monitoring end user latency and checking performance by devices and browsers.
Application
Performance

Classic Ops generally rely on infrastructure metrics - CPU,memory, network and disk l/O,
etc. Modern Ops correlate all of

^hose metrics with application metrics to solve problems10x faster.

</> Quality Code

Developers need to ensure their deployments and new releases don't implode or degrade the overall performance.
Cõdé-Levél
Errors

When you have a large distributed application it is vital to lower MTTRby finding the root cause of errors and exceptions.
The goal is to know about and fix problems before end users complain, reduce the number of support tickets, and eliminate false alerts.
Performance

Automatically generated baselines of all metrics help Ops understand what has changed and where to focus their troubleshooting efforts.Alerts based upon deviation from observed baselines improve alert quality and reduce alert noise.
*

Vamos resumir: a preocupação é com os objetivos quase diametralmente opostos da galera deDesenvolvimento (DEV) e Operações (OPS). Os desenvolvedores querem programar novos recursos, melhorar o produto; corrigir bugs, etc. As operações querem colocar tudo em funcionamento e nunca mudar, já que as alterações causam novos erros, bugs,problemas de desempenho, entre outros.
O objetivo do DevOps é aliviar a tensão entre esses dois campos! Ter pessoas de
Operações nas trincheiras de Desenvolvimento é a principal maneira de alcançar esse objetivo. Seu trabalho é facilitar ao máximo que desenvolvedores e operações façam o que precisam fazer. Como assim? Por exemplo: fornecendo ambientes idênticos de desenvolvimento, testes, homologação,staging e qualidade; configuração de pipelines de teste e implementação automáticos.
Além de estar envolvido no processo de desenvolvimento para que eles estejam mais preparados para lidar com erros de produção. Tradicionalmente, as operações são quase alheias à base de código, uma vez que se preocupam apenas com sua infraestrutura. O objetivo é tornar todo o processo transparente de forma que você possa fazer milhares de implantações de produção por dia; ao contrário dos métodos tradicionais de configuração de uma janela de implantação uma vez a cada trimestre ou por mais tempo.
Claro que para fazer isso, é necessário utilizar um conjunto de práticas e ferramentas. Quais,professor? Ferramentas de Controle de versão (Git, CVS, Tortoise), Servidores de IntegraçãoContínua (Jenkins, Bamboo, Travis), Docker/Vagrant, Gerenciamento de Configuração
(SaltStack,
Chef, Puppet). Isso reduz a dor de cabeça tanto para os desenvolvedores quanto para os operadores e reduz a quantidade de problemas de desempenho e erros de codificação.
(STF - 2013) Integração contínua, entrega contínua, teste contínuo, monitoramento contínuo e feedback são algumas práticas do DevOps.
Comentários: as principais características do DevOps são: colaboração entre equipes; fim de divisões; relação saudável entre áreas; teste, integração e entrega contínuos; automação de deploy; controle e monitoração; gerenciamento de configuração;orquestração de serviços; avaliação de métricas e desempenho; logs e integração; velocidade de entrega; feedback intenso; e comunicação constante (Correto).
(STF-2013) Teste contínuo é uma prática do DevOps que, além de permitira diminuição dos custos finais do teste, ajuda as equipes de desenvolvimento a balancear qualidade e velocidade.
Comentários: teste, integração e entrega contínuos são realmente práticas do DevOps que permitem reduzir custos de teste e ajuda a equipe de desenvolvimento a balancear a qualidade e velocidade (Correto).
(TCU - 2015) De acordo com a abordagem DevOps (development - operations), os desafios da produção de software de qualidade devem ser vencidos com o envolvimento
Z 85

/

dos desenvolvedores na operação dos sistemas com os quais colaboraram no desenvolvimento.
Comentários: essa questão permite duas interpretações de 'envolvimento1: (1) no sentido de interação e colaboração entre equipes; (2) no sentido de mão na massa mesmo - na operação dos sistemas. Por conta da ambiguidade,a questão foi anulada
(Anulada).

(TRE-PE - 2017) O DevOps consiste em:

a) um processo similar ao IRUP (IBM Rational Unified Process), que tem como objetivo dividir o processamento em fases e disciplinas de software para paralelizar as ações de desenvolvimento e de manutenção das soluções.
b) uma plataforma aberta cuja função é substituir a virtualização de aplicações e serviços em containers e, com isso, agilizar a implantação de soluções de software.
c) um aplicativo que permite o gerenciamento de versões de códigos-fonte e versões de programas, bem como a implantação da versão mais recente de um software em caso de falha.
d) um processo de promoção de métodos que objetivam aprimorar a comunicação,
tornando a colaboração eficaz especialmente entre os departamentos de desenvolvimento e teste e entre os departamentos de operações e serviço para o negócio.
e) uma metodologia ágil que, assim como a XP (extreme programming) e o Scrum, tem foco na gestão de produtos complexos relativos à equipe de desenvolvimento.
Comentários: DevOps não é um processo similar ao iRUP, não é uma plataforma aberta,
não é um aplicativo e não é uma metodologia ágil. DevOps é um processo de promoção de métodos que objetivam aprimorar a comunicação, tornando a colaboração eficaz especialmente entre os departamentos de desenvolvimento e teste e entre os departamentos de operações e serviço para 0 negócio (Letra D).
(TRT-PA e AP - 2016) Acerca de DevOps, assinale a opção correta.

a) O DevOps concentra-se em reunir diferentes processos e executá-los mais rapidamente e com mais frequência, o que gera baixa colaboração entre equipes.
b) O DevOps tem como princípio produzir, a partir da avaliação dos times de desenvolvimento do serviço, grandes mudanças e farta documentação com valor agregado para os usuários, assemelhando-se, por isso, com objetivos dos métodos iterativos e em cascata.
/ 85

/

c) A infraestrutura de nuvem de provedores internos e externos vem restringindo o uso de DevOps pelas organizações.
d) O DevOps parte da premissa de adoção de grandes equipes de especialistas, com a menor interação possível, visando à padronização de processos e à mínima automação de atividades.
e) Atividades típicas em DevOps compreendem teste do código automatizado,
automação de fluxos de trabalho e da infraestrutura e requerem ambientes de desenvolvimento e produção idênticos.
Comentários: (a) Errado, isso gera alta colaboração entre equipes; (b) Errado, não se assemelha com objetivos de métodos em cascata, visto que essa metodologia possui entregas menos frequentes e é menos dinâmica; (c)Errado, é justamente o inverso

- elas usam com cada vez mais frequência; (d) Errado, recomenda-se a maior interação possível entre as equipes; (e) Correto,testes automatizados, automação de fluxos e infraestrutura são atividades frequentes que realmente exigem ambientes de desenvolvimento e produção idênticos (Letra E).
(STJ -2015) DevOps é um conceito pelo qual se busca entregar sistemas melhores, com menor custo, em menortempo e com menor risco.
Comentários: perfeito, perfeito, perfeito-todas são características do DevOps (Correto).

(STJ - 2015) O profissional especialista em DevOps deve atuar e conhecer as áreas de desenvolvimento (engenharia de software), operações e controle de qualidade, além de conhecer, também, de forma ampla, os processos de desenvolvimento ágil.
Comentários: ele é a combinação entre desenvolvimento, operação e controle de qualidade
- portanto questão perfeita
(Correto).

(SLU-DF - 2019) Em DevOps, o princípio monitorar e validar a qualidade operacional antecipa o monitoramento das características funcionais e não funcionais dos sistemas para o início do seu ciclo de vida, quando as métricas de qualidade devem sercapturadas e analisadas.
Comentários: 0 princípio monitorar e validar a qualidade operacional transfere 0
monitoramento para o início do ciclo de vida do software, para identificar antecipadamente problemas de qualidade que podem ocorrer no desenvolvimento. Na implantação e teste, as métricas de qualidade são capturadas e analisadas, sendo que essas métricas devem ser entendidas por todos os stakeholders (Correto).
(MPE-PI - 2018) A infraestrutura como código é uma prática DevOps caracterizada pela infraestrutura provisionada e gerenciada por meio de técnicas de desenvolvimento de código e de software, como, por exemplo, controle de versão e integração contínua.
Z 85

/

Comentários: trata-se realmente de uma prática em que a infra estrutura provisionada e gerenciada por meio de técnicas de desenvolvimento de código e de software - ela oferece controle de versão, entrega e integração contínua (Correto).
(STJ - 2018) Apesar de ser um processo com a finalidade de desenvolver, entregar e operar um software, o DevOps é incompatível com a aplicação de métodos ágeis como o Scrum ou, ainda, com o uso de ferramentas que permitam visualizar os fluxos do processo.
Comentários: pelo contrário, é completamente compatível com as aplicações de métodos ágeis como 0
Scrum ou, ainda, com
0 uso de ferramentas que permitam visualizar os fluxos do processo (Errado).

(STJ -2018) O gerenciamento de desenvolvimento de software por meio do Scrum pode ser combinado com o ciclo de vida do DevOps, haja vista que o DevOps combina práticas e ferramentas que aumentam a capacidade de uma organização de distribuir aplicativos e serviços; logo, a integração contínua do software pode ser realizada na sprint doScrum junto com a operação dos serviços da organização.
Comentários: ele realmente combina práticas e ferramentas que aumentam a capacidade de uma organização de distribuir aplicativos e serviços e pode ser realizado na sprint do Scrum por meio da integração contínua(Correto).

Conceitos Básicos

Caros alunos (as), o Docker é um software usado como contêiner da empresa Docker,
Inc, que fornece uma camada de abstração e automação para virtualização de sistema operacional noWindows e no Linux.

Como ele faz isso? Segundo o fornecedor: o Docker emprega isolamento de recurso do núcleo do Linux e espaços de nomes do núcleo, e um sistema de arquivos com recursos de união, comoOverlayFS
criando contêineres independentes para executar dentro de uma única instância do sistema operacional, evitando a sobrecarga de manter máquinas virtuais (VM).
O docker então é uma alternativa de virtualização em que o kernel da máquina hospedeira é compartilhado com a máquina virtualizada ou o software em operação, portanto um desenvolvedor pode agregar a seu software a possibilidade de levar as bibliotecas e outras dependências do seu programa junto ao software com menos perda de desempenho do que a virtualização do hardware de um servidor completo. Assim, odockertorna operações em uma infraestrutura como serviços web mais intercambiável, eficientes e flexíveis.
Na prática o docker é utilizado como uma ferramenta que pode empacotar um aplicativo e suas dependências em um recipiente virtual que pode ser executado em qualquer servidor que contenha o Docker instalado. Isso ajuda a permitir flexibilidade e portabilidade de onde o aplicativo pode ser executado, quer nas instalações, nuvem pública, nuvem privada, entre outros.Então o que exatamente o Docker faz e porque utilizamos ele? Docker é uma plataforma que utiliza containers como solução arquitetural, para aumentar a portabilidade e eficiência. Perai professor eu ainda não sei o que são containers.
0 QUE SÃO, DE ONDE VIERAM E POR QUE USAMOS CONTAINERS?

X 85

/

Pessoal, um container é um ambiente isolado, que representa um conjunto de processos executados a partir de uma imagem, a imagem é o local onde estão todos os arquivos necessários para execução do container, logo os containers compartilham o kernel e isolam os processos das aplicações do resto do sistema.
Por exemplo: se você está desenvolvendo uma aplicação para um cliente, você pode fazer suas configurações nessa aplicação. Mas, em um ambiente convencional, você precisará replicar estas configurações para os outros ambientes de execução. Ok?!
Com o Docker, você pode ir fazendo isso em um ambiente isolado e, por causa da facilidade para replicação de containers, você acaba criando ambientes padronizados, tanto em desenvolvimento como em produção, por exemplo. Assim, você pode disponibilizar essa arquitetura toda para seu cliente, onde ele estiver: basta replicar os containers, que serão executados da mesma maneira em qualquer lugar. Logo, podemos já derivar uma diferença fundamental entreContainers e
Virtualização, veja:

Aplicação

Aplicação

Aplicação

Birbáriós '
Bibliotecas

Binários t

BMIctecas

Binários '
Bibliotecas

S-O-

convidado

S.O-

convidado

Hype rvisor

S.O. do host

S-O.

convidado

Aplicação

Binários '
Bibliotecas

Aplicação

Binários /
Bibliotecas

S.O. do host

Aplicação

Binários i1
Bibliotecas

Hardware do servidor

Virtualizaçao

Hardware do servidor

Containers

Como o container possui uma imagem que contém todas as dependências de um aplicativo,
ele é portátil e consistente em todas as etapas de desenvolvimento. Essa imagem é um modelo de
X 85

/

somente leitura que é utilizada para subir um container. O Docker nos permite construir nossas próprias imagens e utilizá-las como base para os containers.
Pessoal, Docker é então uma plataforma open source escrito em Go, que é uma linguagem de programação de alto desempenho desenvolvida dentro do Google, que facilita a criação e administração de ambientes isolados. O Docker possibilita o empacotamento de uma aplicação ou ambiente inteiro dentro de um container, e a partir desse momento o ambiente inteiro torna-se portável para qualquer outro host que contenha o Docker instalado. O Docker pode ler instruções através de um arquivo texto que contém instruções para montar uma imagem(dockerfile).

Isso reduz drasticamente o tempo de deploy (implantação) de alguma infraestrutura ou até mesmo aplicação, pois não há a necessidade de ajustes de ambiente para o correto funcionamento do serviço. O ambiente é sempre o mesmo, basta configurar uma vez e replicar quantas vezes quiser! Outra facilidade do Docker é poder criar suas imagens (containers prontos para deploy) a partir de arquivos de definição, os chamados Dockerfiles.
Outro fator importante é que o Docker utiliza como backend padrão o LXC (Linux
Containers), com isso é possível definir limitações de recursos por container (memória, CPU, E/S etc.).O LXC é um método de virtualização a nível de sistema operacional que permite executar múltiplosSistemas
Linux (denominados containers) usando um único kernel. Pessoal, importante ressaltar um dos principais comandos do Docker, que serve para visualizar informações referentes ao consumo de recursos de todos os containers, deve-se executar no terminal: Docker container stats.
X 85

/

Assim, pode-se criar ambientes de teste e/ou produção utilizando o LXC de forma ágil e segura(isolada). Não há a necessidade de se preocupar com tantos detalhes como na virtualização tradicional.
Quanto as instruções Docker, uma se destaca por ser responsável por indicar ao docker a porta que o container deve utilizar em tempo de execução, trata-se da EXPOSE. Outras instruções importantes, seriam:
- ADD: Adiciona um arquivo ou diretório dos sistemas de arquivo local para a imagem;

- COPY: Copia arquivos remotos e/ou locais para a imagem.

- CMD: Comando padrão a ser executado pela imagem;

- ENTRYPOINT: Permite configurar o contêiner ou apenas definir o comando a ser executado(Sobrepõe o CMD);

- ENV: Define variáveis de ambiente;

- FROM: Inicia a imagem a partir de outra imagem: Ex "FROM debian:8";

- RUN: Roda um comando no sistema operacional da imagem;

- ARG: Define variáveis de ambiente, mas permite que no momento da construção da imagem seja passado o valor para a variável especificada. Útil para quando se deseja permitir que o usuário construa imagens para mais de uma versão do mesmo software usando o mesmo DockerFile.
Como o Docker trabalha utilizando cliente e servidor (toda a comunicação entre o DockerDaemon e Docker client é realizada através de API), basta apenas ter instalado o serviço doDocker em um lugar, e apontar em o Docker Client para esse servidor. A plataforma do
Docker em si utilizada alguns conjuntos de recursos, seja para a criação ou administração dos containers.
Entre esses conjuntos podemos destacar a biblioteca libcontainer, que é responsável pela comunicação entre o Docker Daemon e o backend utilizado, sendo ela a responsável pela criação do container, e através dela é possível configurar os limites de recursos por container.
IMPORTANTE

Vale lembrarque, apesar do Dockerter sido desenvolvido inicialmente com base na tecnologia LXC(Linux Containers - sendo, portanto, mais associado aos containers Linux), hoje essa tecnologia tornou-se independente de sistema operacional: podemos utilizar o Docker em ambientes Linux,Windows e até mesmo MacOS.

(CRA-PR - 2022) Em um sistema Linux Ubuntu com o Docker instalado, para visualizar informações referentes ao consumo de recursos de todos os containers, deve-se executar no terminal: Docker container stats.
Comentários: Perfeito! Conforme vimos em aula, 0 Docker container stats mostra os recursos de todos os containers, logo em um sistema Linux Ubuntu com 0 Docker instalado, para visualizar informações referentes ao consumo de recursos de todos os containers, deve-se executar no terminal: Docker container stats (Correto).
X 85

/

QUESTõES CoMENTADAS - DoCkER

í. (FEPESE / Prefeitura de Florianópolis - 2019) O Docker pode ler instruções através de um arquivo texto que contém instruções para montar uma imagem (dockerfile). Nesse contexto,qual a palavra-chave ou instrução que indica ao docker a porta que o container deve utilizar em tempo de execução?
a) HTTP

b) PORT

c) EXPOSE

d) DOCKER

e) SERVERPORT

Comentários:

Galera, a instrução que indica ao Docker a porta que o container deve utilizar em tempo de execução é o EXPOSE. Conforme vimos: "Quanto as instruções do Docker, uma se destaca por ser responsável por indicar ao docker a porta que o container deve utilizar em tempo de execução,trata-se da EXPOSE".

Gabarito: Letra C

2. (COMPERVE / TJ-RN - 2020) Os volumes são mecanismos utilizados para persistir os dados gerados e usados pelos containers do Docker. Embora as montagens de ligação dependam da estrutura de diretórios da máquina host, os volumes são completamente gerenciados peloDocker. Considerando que um analista queira criar um volume de nome my-volume dentro de um docker, ele deve executar o comando:
a) docker volume create my-volume b) docker create volume my-volume c) docker run create volume my-volume d) docker create run volume my-volume
Comentários:

Pessoal, caso a ideia seja criar um volume de nome "my-volume" a sintaxe no Docker deve ser:docker volume create my-volume. Bem simples, né?

Gabarito: Letra A

/ 85

/

3. (AOCP / MJSP - 2020) O Docker possibilita que uma imagem com todos os aplicativos e configurações realizadas em um contêiner sejam transferidos para outro host,bastando que este tenha o Docker instalado. Assinale a alternativa que apresenta o nome dessa operação:
a) Restore.

b) Dump.

c) Drill down Contêiner.

d) Portabilidade.

e) Drill up Contêiner.

Comentários:

Trata-se da operação de Portabilidade, quando o Docker possibilita que uma imagem com todos os aplicativos e configurações realizadas em um contêiner sejam transferidos para outro host.
Gabarito: Letra D

4. (COMPERVE/TJ-RN - 2020) Uma imagem do Dockeré criada a partirde uma série de camadas,onde cada uma representa uma instrução no Dockerfile da imagem. Considerando que um analista do Tribunal de Justiça queira listar as camadas (layers) da imagem docker mailserver,ele deve executar o comando:

a) docker expose mailserver b) docker layers mailserver c) docker history mailserver d) docker image mailserver
Comentários:

Para listar as layers da imagem Docker mailserver, o comando a ser executado é o
Docker history mailserver.
Gabarito: Letra C

5. (FURB / Prefeitura De Blumenau - 2022) Sobre Docker, marque a alternativa CORRETA:

a) Dockeré uma plataforma de software livre que permite que os desenvolvedores empacotem aplicativos em contêineres, que consistem em componentes executáveis e padronizados que combinam o código-fonte do aplicativo com as bibliotecas e dependências do sistema operacional (S.O.) que são necessárias para executar esse código em qualquer ambiente.
b) É projetado para ser flexível, ele estabelece um padrão para a construção de interfaces com o usuário do lado do servidor. A arquitetura define claramente uma separação entre a lógica da x
X 85

/

aplicação e a apresentação, enquanto torna maisfácil ligara camada de apresentação ao código do aplicativo.
c) É uma plataforma que estende a plataforma SE do Java e é o padrão para desenvolvimento de aplicativos empresariais entre a comunidade Java. Em outras palavras, trata-se de framework web MVC para a construção de interfaces de usuário baseadas em componentes.
d) Para começar a codificar o Docker, não é necessária nenhuma configuração especial ao servidor Glassfish. Basta instalar o Netbeans com suporte à tecnologia Java EE, que por padrão já será instalado o servidor Glassfish pré configurado.
e) É um popularframework para projetos JSF que pode ser usado para desenvolver rapidamente aplicações sofisticadas para empresas ou no desenvolvimento de sites padrão.Tecnicamente, é uma biblioteca de componentes de interface gráfica para as aplicações web baseadas em JSF.
Comentários:

Definição de Docker como uma plataforma de software livre que permite que os desenvolvedores empacotem aplicativos em contêineres, que consistem em componentes executáveis e padronizados que combinam o código-fonte do aplicativo com as bibliotecas e dependências do sistema operacional (S.O.) que são necessárias para executar esse código em qualquer ambiente,está perfeita.

Gabarito: Letra A

6. (CESPE / DPE-RO - 2022) A tecnologia Docker usa o kernel do Linux e recursos do kernel para segregar processos; as ferramentas baseadas nos contêineres Linux oferecem aos usuários acesso sem precedentes a aplicações, além da habilidade de implantarcom rapideze detertotal controle sobre as versões e distribuição. A respeito da tecnologia Docker, assinale a opção correta.
a) O Docker é uma tecnologia proprietária que automatiza a implantação da aplicação dentro do ambiente de contêiner.
b) O Docker oferece vantagem em questões como a limpeza de processos netos
(grandchild)
após o encerramento dos processos filhos (child).

c) O Docker fornece as mesmas funcionalidades oferecidas pelos contêineres Linux tradicionais,incluindo a capacidade de usar processos como cron ou syslog dentro do contêiner,
junto à aplicação.
d) As instâncias de aplicativos em contêiner Docker usam mais memória do que as máquinas virtuais, sendo inicializadas e interrompidas mais lentamente.
x

X 85

/

e) Os contêineres Docker facilitam a colocação rápida de novas versões de software, com novos recursos de negócios, e a rápida reversão para uma versão anterior, se necessário.
Comentários:

Pessoal, os contêineres Docker facilitam a colocação rápida de novas versões de software, com novos recursos de negócios, e a rápida reversão para uma versão anterior, se necessário. Essa é uma das mais relevantes vantagens de se utilizar Docker.
Gabarito: Letra E

7. (COPERV / UFSC - 2018) A respeito da solução de contêiner Docker, analise as afirmativas abaixo e assinale a alternativa correta.
I. Uma imagem pode ser versionada com múltiplos commits.

II. O arquivo Dockerfile contém variáveis, comandos e/ou operações para criar uma nova instância Docker.
III. Depois de uma imagem ser criada, para alterá-la é necessário reexecutar o processo de criação.
a) Somente as afirmativas I e III estão corretas.

b) Somente a afirmativa II está correta.

c) Somente as afirmativas II e III estão corretas.

d) Somente as afirmativas I e II estão corretas.

e) Somente a afirmativa I está correta.

Comentários:

Das alternativas somente a I está correta. No Docker uma imagem pode ser versionada com múltiplos commits. Não temos a criação de uma nova instância Docker como dito no itemII e sim de uma nova imagem e o item III está errado também, já que a imagem pode ser modificada no momento da execução.
Gabarito: Letra E

8. (CESPE / SLU - 2019) O Docker é uma ferramenta open source que permite a criação de ambientes virtuais por meio de Linux Containers, sendo uma das vantagens dos contêineresDockerfornecer uma virtualização em nível de sistema operacional, o que isola as aplicações em execução e não utiliza tantos recursos da máquina quanto as máquinas virtuais.
Comentários:

/ 85

/

Perfeito! O Docker é uma ferramenta open source que permite a criação de ambientes virtuais por meio de Linux Containers, sendo uma das vantagens dos contêineres Docker fornecer uma virtualização em nível de sistema operacional, o que isola as aplicações em execução e não utiliza tantos recursos da máquina quanto as máquinas virtuais.
Gabarito: Correto

9. (FCC / DPE-RS - 2017) Considere, por hipótese, que a equipe de analistas da
Defensoria Pública tenha optado pelo uso do Docker. Esta decisão foi motivada pelo fato de o Docker:
a) estar ganhando espaço como um gerenciador de máquinas virtuais no ambiente GNU/Linux e não ter bibliotecas próprias, mantendo as bibliotecas nativas utilizadas para gerenciar o LXC.
b) não utilizar Namespaces do Linux, o que permite prover espaços de trabalho isolados para os contêineres. Desta forma, quando um contêiner é criado, automaticamente é criada uma camada de isolamento para grupos de processos.
c) utilizar hypervisors, compatíveis com diversas plataformas, para executar máquinas virtuais que virtualizam hardware físico como parte de um desenvolvimento multiplataforma para testes e implementação de fluxo de trabalho.
d) permitir portabilidade de contêineres. É possível criar uma imagem de toda a configuração e aplicativos instalados em um contêiner e transferi-lo para outro host que tenha um Docker previamente instalado.
e) obter o mesmo desempenho da virtualização baseada em hypervisor, em que cada contêiner é executado em seu próprio sistema operacional, o que reduz a utilização de recursos de disco,embora os contêineres utilizem mais memória.

Comentários:

Docker permite a portabilidade de contêineres, vimos isso durante toda aula. Logo, com
Docker é possível criar uma imagem de toda a configuração e aplicativos instalados em um contêiner e transferi-lo para outro host que tenha um Docker previamente instalado.
Gabarito: Letra D

io.(FGV / CGU - 2022) Uma das estratégias para reduzir o tamanho de imagens Docker consiste em:
a) combinar comandos RUN em um único comando;

b) substituir a imagem base por uma versão mais recente;

c) separar comandos RUN complexos em comandos menores;

/ 85

/

d) reordenar os comandos de forma que o cache seja utilizado com maior frequência;

e) compactar arquivos a serem copiados para a imagem e descompactá-los durante a sua geração;
Comentários:

Conforme verificamos uma das estratégias para reduzir o tamanho de imagens Docker consiste em combinar comandos RUN em um único comando.
Gabarito: Letra A

n.(CEPUERJ / UERJ - 2021) Considerando-se os conceitos de docker, é correto afirmar que se trata de:
a) um complemento para virtualização completa, associado ao VMware ESXi b) um complemento para virtualização completa, associado ao VMware c) uma ferramenta para criar e manter máquinas virtuais d) uma ferramenta para criar e manter containers
Comentários:

Pessoal, conforme estudamos e segundo: aws.amazon.com.pt/docker/

"O Docker é uma plataforma de software que permite a criação, o teste e a implantação de aplicações rapidamente. O Docker cria pacotes de software em unidades padronizadas chamadas de contêineres que têm tudo o que 0 software precisa para ser executado, inclusive bibliotecas,ferramentas de sistema, código e runtime. Ao usaro Docker, é possível implantar e escalar rapidamente aplicações em qualquer ambiente e ter a certeza de que 0 seu código será executado."
Gabarito: Letra D

i2.(CESPE / SLU - 2019) O Docker é uma ferramenta open source que permite a criação de ambientes virtuais por meio de Linux Containers, sendo uma das vantagens dos contêineresDockerfornecer uma virtualização em nível de sistema operacional, o que isola as aplicações em execução e não utiliza tantos recursos da máquina quanto as máquinas virtuais.
Comentários:

De fato pessoal, conforme vimos o Docker é uma ferramenta open source que permite a criação de ambientes virtuais por meio de Linux Containers, sendo uma das vantagens dos contêineres Docker fornecer uma virtualização em nível de sistema operacional, o que isola as aplicações em execução e não utiliza tantos recursos da máquina quanto as máquinas virtuais.
X 85

/

Gabarito: Correto

13.OADES / BRB - 2021) O Docker é uma plataforma aberta para desenvolvimento, entrega e execução de aplicações. A respeito da funcionalidade tmpfs mounts, assinale a alternativa correta.
a) Assim como os volumes e bind mounts, é possível compartilhar o tmpfs mounts entre diversos containers.
b) Essa funcionalidade está presente apenas quando se executa o Docker no Linux.

c) O tmpfs mounts pode ser armazenado em unidade de armazenamento do tipo
SSD do servidor que hospeda o Docker.
d) O tmpfs mounts permanece persistente após a parada do container.

e) Não é possível limitar o seu tamanho; por padrão, ele é ilimitado.

Comentários:

A funcionalidade tmpfs mounts está presente apenas quando se executa o Docker no
Linux. Penso que esse tipo de conhecimento está muito mais atrelado ao SO Linux, mas sabe como é a banca né? Pede qualquer coisa sobre o tema na questão.
Gabarito: Letra B

í^.fCOMPERVE /TJ-RN-2020) O processo de virtualização é possibilitado por um hypervisor,
que é um software instalado em cima de um servidor físico e que, a partir dele, é possível a criação de máquinas virtuais que podem, cada uma, conter sistemas operacionais diferentes.Analise as seguintes afirmativas sobre o uso de Máquinas Virtuais e Docker.
I. A virtualização permite o isolamento total do ambiente da sua aplicação, pois ela não emula a máquina virtual por completo.
II. O Docker permite "empacotar" uma aplicação ou sistema dentro de um container,
sendo que este container pode posteriormente ser executado em qualquer máquina que tenha o Docker instalado.
III. Vários containers podem ser executados na mesma máquina e compartilhar o kernel do SOcom outros containers, cada um executando como processos isolados no espaço do usuário.

IV. Em um sistema de virtualização tradicional, o sistema operacional é isolado dos demais instalados dentro da máquina host.
Estão corretas apenas as afirmativas:

a) III e IV

x

X 85

b) II e IV

c) I, lie III

d) II, III e IV

Comentários:

A questão extrapola o conhecimento somente em Docker, porém trouxe aqui para vocês para nos atentarmos somente a alternativa II que está correta e foi a definição que vimos na aula. O Docker permite "empacotar" uma aplicação ou sistema dentro de um container, sendo que este container pode posteriormente ser executado em qualquer máquina que tenha o Docker instalado.
Gabarito: Letra D

i5.(CESPE / STJ - 2015) Dockerfile é um arquivo de texto que contém todos os comandos, em ordem, necessários para construir uma determinada imagem Docker. Sobre as instruções contidas em um Dockerfile, assinale a alternativa correta.
a) A instrução VOLUME configura o tamanho da imagem.

b) A instrução ENV adiciona metadados para uma imagem.

c) A instrução WORKDIR permite a criação de um diretório no host onde ficam armazenados os dados do container.
d) A instrução EXPOSE informa ao Docker que o container escuta nas portas de rede especificadas em tempo de execução.
e) A instrução FROM configura qual será a aplicação principal do container, sendo executada após a inicialização do container.
Comentários:

Dockerfile e não FileDocker é um arquivo de texto que contém todos os comandos, em ordem,necessários para construir uma determinada imagem Docker. Logo, conforme estudamos, a instrução EXPOSE informa ao Docker que o container escuta nas portas de rede especificadas em tempo de execução.
Gabarito: Letra D

i6.(COMPERVE/TJ-RN-2O2o) Uma imagem de container do Docker é um pacote de software leve,
independente e executável que inclui tudo o que é necessário para executar uma aplicação. Na criação de um arquivo Dockerfile, a instrução EXPOSE:
a) mapeia uma porta externa para uma porta interna à rede Docker.

b) divulga uma porta (TCP ou UDP) para os hosts externos à rede Docker.

c) expõe um serviço do container para a rede Docker default.

d) documenta quais portas se pretende publicar.

Comentários:

Conforme vimos, a instrução EXPOSE do Docker documenta quais portas se pretende publicar.

Gabarito: Letra D

17. (CESPE / SEFAZ-CE - 2021) As alterações efetuadas em arquivos e diretórios copiados de uma camada base para dentro de um container docker, por padrão, são vistas pelos múltiplos containers do mesmo sistema de arquivos.
Comentários:

As alterações efetuadas em arquivos ou diretórios dentro de um container são isoladas e não podem ser vistas fora dele.
Gabarito: Errado x
X 85

/

LISTA DE QUESTõES - DoCkER

í. (FEPESE / Prefeitura de Florianópolis - 2019) O Docker pode ler instruções através de um arquivo texto que contém instruções para montar uma imagem (dockerfile). Nesse contexto,qual a palavra-chave ou instrução que indica ao docker a porta que o container deve utilizar em tempo de execução?
a) HTTP

b) PORT

c) EXPOSE

d) DOCKER

e) SERVERPORT

2. (COMPERVE / TJ-RN - 2020) Os volumes são mecanismos utilizados para persistir os dados gerados e usados pelos containers do Docker. Embora as montagens de ligação dependam da estrutura de diretórios da máquina host, os volumes são completamente gerenciados peloDocker. Considerando que um analista queira criar um volume de nome my-volume dentro de um docker, ele deve executar o comando:
a) docker volume create my-volume b) docker create volume my-volume c) docker run create volume my-volume d) docker create run volume my-volume
3. (AOCP / MJSP - 2020) O Docker possibilita que uma imagem com todos os aplicativos e configurações realizadas em um contêiner sejam transferidos para outro host,bastando que este tenha o Docker instalado. Assinale a alternativa que apresenta o nome dessa operação.
a) Restore.

b) Dump.

c) Drill down Contêiner.

d) Portabilidade.

e) Drill up Contêiner.

4. (COMPERVE/TJ-RN - 2020) Uma imagem do Dockeré criada a partirde uma série de camadas,onde cada uma representa uma instrução no Dockerfile da imagem. Considerando que um analista do Tribunal de Justiça queira listar as camadas (layers) da imagem docker mailserver,ele deve executar o comando:

a) docker expose mailserver b) docker layers mailserver c) docker history mailserver d) docker image mailserver
5. (FURB / Prefeitura De Blumenau - 2022) Sobre Docker, marque a alternativa CORRETA:

a) Docker é uma plataforma de software livre que permite que os desenvolvedores empacotem aplicativos em contêineres, que consistem em componentes executáveis e padronizados que combinam o código-fonte do aplicativo com as bibliotecas e dependências do sistema operacional (S.O.) que são necessárias para executar esse código em qualquer ambiente.
b) É projetado para ser flexível, ele estabelece um padrão para a construção de interfaces com o usuário do lado do servidor. A arquitetura define claramente uma separação entre a lógica da aplicação e a apresentação, enquanto torna maisfácil ligara camada de apresentação ao código do aplicativo.
c) É uma plataforma que estende a plataforma SE do Java e é o padrão para desenvolvimento de aplicativos empresariais entre a comunidade Java. Em outras palavras, trata-se de framework web MVC para a construção de interfaces de usuário baseadas em componentes.
d) Para começar a codificar o Docker, não é necessária nenhuma configuração especial ao servidor Glassfish. Basta instalar o Netbeans com suporte à tecnologia Java EE, que por padrão já será instalado o servidor Glassfish pré configurado.
e) É um popularframework para projetos JSF que pode ser usado para desenvolver rapidamente aplicações sofisticadas para empresas ou no desenvolvimento de sites padrão.Tecnicamente, é uma biblioteca de componentes de interface gráfica para as aplicações web baseadas em JSF.
6. (CESPE / DPE-RO - 2022) A tecnologia Docker usa o kemel do Linux e recursos do kernel para segregar processos; as ferramentas baseadas nos contêineres Linux oferecem aos usuários acesso sem precedentes a aplicações, além da habilidade de implantarcom rapideze detertotal controle sobre as versões e distribuição. A respeito da tecnologia Docker, assinale a opção correta.
a) O Docker é uma tecnologia proprietária que automatiza a implantação da aplicação dentro do ambiente de contêiner.
b) O Docker oferece vantagem em questões como a limpeza de processos netos
(grandchild)
após o encerramento dos processos filhos (child).

c) O Docker fornece as mesmas funcionalidades oferecidas pelos contêineres Linux tradicionais,incluindo a capacidade de usar processos como cron ou syslog dentro do contêiner,
junto à aplicação.
d) As instâncias de aplicativos em contêiner Docker usam mais memória do que as máquinas virtuais, sendo inicializadas e interrompidas mais lentamente.
e) Os contêineres Docker facilitam a colocação rápida de novas versões de software, com novos recursos de negócios, e a rápida reversão para uma versão anterior, se necessário.
7. (COPERV / UFSC - 2018) A respeito da solução de contêiner Docker, analise as afirmativas abaixo e assinale a alternativa correta.
I. Uma imagem pode ser versionada com múltiplos commits.

II. O arquivo Dockerfile contém variáveis, comandos e/ou operações para criar uma nova instância Docker.
III. Depois de uma imagem ser criada, para alterá-la é necessário reexecutar o processo de criação.
a) Somente as afirmativas I e III estão corretas.

b) Somente a afirmativa II está correta.

c) Somente as afirmativas II e III estão corretas.

d) Somente as afirmativas I e II estão corretas.

e) Somente a afirmativa I está correta.

8. (CESPE / SLU - 2019) O Docker é uma ferramenta open source que permite a criação de ambientes virtuais por meio de Linux Containers, sendo uma das vantagens dos contêineresDockerfornecer uma virtualização em nível de sistema operacional, o que isola as aplicações em execução e não utiliza tantos recursos da máquina quanto as máquinas virtuais.
9. (FCC / DPE-RS - 2017) Considere, por hipótese, que a equipe de analistas da
Defensoria Pública tenha optado pelo uso do Docker. Esta decisão foi motivada pelo fato de o Docker:
a) estar ganhando espaço como um gerenciador de máquinas virtuais no ambiente GNU/Linux e não ter bibliotecas próprias, mantendo as bibliotecas nativas utilizadas para gerenciar o LXC.
b) não utilizar Namespaces do Linux, o que permite prover espaços de trabalho isolados para os contêineres. Desta forma, quando um contêiner é criado, automaticamente é criada uma camada de isolamento para grupos de processos.
c) utilizar hypervisors, compatíveis com diversas plataformas, para executar máquinas virtuais que virtualizam hardware físico como parte de um desenvolvimento multiplataforma para testes e implementação de fluxo de trabalho.
d) permitir portabilidade de contêineres. É possível criar uma imagem de toda a configuração e aplicativos instalados em um contêiner e transferi-lo para outro host que tenha um Docker previamente instalado.
X 65

/

e) obter o mesmo desempenho da virtualização baseada em hypervisor, em que cada contêiner é executado em seu próprio sistema operacional, o que reduz a utilização de recursos de disco,embora os contêineres utilizem mais memória.

io.(FGV / CGU - 2022) Uma das estratégias para reduzir o tamanho de imagens Docker consiste em:
a) combinar comandos RUN em um único comando;

b) substituir a imagem base por uma versão mais recente;

c) separar comandos RUN complexos em comandos menores;

d) reordenar os comandos de forma que o cache seja utilizado com maior frequência;

e) compactar arquivos a serem copiados para a imagem e descompactá-los durante a sua geração;
n.(CEPUERJ / UERJ - 2021) Considerando-se os conceitos de docker, é correto afirmar que se trata de:
a) um complemento para virtualização completa, associado ao VMware ESXi b) um complemento para virtualização completa, associado ao VMware c) uma ferramenta para criar e manter máquinas virtuais d) uma ferramenta para criar e manter containers i2.(CESPE / SLU - 2019) O Docker é uma ferramenta open source que permite a criação de ambientes virtuais por meio de Linux Containers, sendo uma das vantagens dos contêineresDockerfornecer uma virtualização em nível de sistema operacional, o que isola as aplicações em execução e não utiliza tantos recursos da máquina quanto as máquinas virtuais.
13.OADES / BRB - 2021) O Docker é uma plataforma aberta para desenvolvimento, entrega e execução de aplicações. A respeito da funcionalidade tmpfs mounts, assinale a alternativa correta.
a) Assim como os volumes e bind mounts, é possível compartilhar o tmpfs mounts entre diversos containers.
b) Essa funcionalidade está presente apenas quando se executa o Docker no Linux.

c) O tmpfs mounts pode ser armazenado em unidade de armazenamento do tipo
SSD do servidor que hospeda o Docker.
d) O tmpfs mounts permanece persistente após a parada do container.

e) Não é possível limitar o seu tamanho; por padrão, ele é ilimitado.

i4.(COMPERVE/TJ-RN-2O2o) O processo de virtualização é possibilitado por um hypervisor, que é um software instalado em cima de um servidor físico e que, a partir dele, é possível a criação de máquinas virtuais que podem, cada uma, conter sistemas operacionais diferentes.Analise as seguintes afirmativas sobre o uso de Máquinas Virtuais e Docker.
X 65

/

I. A virtualização permite o isolamento total do ambiente da sua aplicação, pois ela não emula a máquina virtual por completo.
II. O Docker permite "empacotar" uma aplicação ou sistema dentro de um container,
sendo que este container pode posteriormente ser executado em qualquer máquina que tenha o Docker instalado.
III. Vários containers podem ser executados na mesma máquina e compartilhar o kernel do SOcom outros containers, cada um executando como processos isolados no espaço do usuário.

IV. Em um sistema de virtualização tradicional, o sistema operacional é isolado dos demais instalados dentro da máquina host.
Estão corretas apenas as afirmativas a) III e IV
b) II e IV

c) I, lie III

d) II, III e IV

15. (CESPE / STJ - 2015) Dockerfile é um um arquivo de texto que contém todos os comandos, em ordem, necessários para construir uma determinada imagem Docker. Sobre as instruções contidas em um Dockerfile, assinale a alternativa correta.
a) A instrução VOLUME configura o tamanho da imagem.

b) A instrução ENV adiciona metadados para uma imagem.

c) A instrução WORKDIR permite a criação de um diretório no host onde ficam armazenados os dados do container.
d) A instrução EXPOSE informa ao Docker que o container escuta nas portas de rede especificadas em tempo de execução.
e) A instrução FROM configura qual será a aplicação principal do container, sendo executada após a inicialização do container.
16. (COMPERVE/TJ-RN-2O2o) Uma imagem de containerdo Dockeré um pacote de software leve,
independente e executável que inclui tudo o que é necessário para executar uma aplicação. Na criação de um arquivo Dockerfile, a instrução EXPOSE:
a) mapeia uma porta externa para uma porta interna à rede Docker.

b) divulga uma porta (TCP ou UDP) para os hosts externos à rede Docker.

c) expõe um serviço do container para a rede Docker default.

d) documenta quais portas se pretende publicar.

X 65

/

17. (CESPE / SEFAZ-CE - 2021) As alterações efetuadas em arquivos e diretórios copiados de uma camada base para dentro de um container docker, por padrão, são vistas pelos múltiplos containers do mesmo sistema de arquivos.
X 65

/

GABARITo - DoCkER

1. CORRETO 7. ERRADO
13. LETRA B

2. ERRADO 8. CORRETO
14. LETRA D

3. ERRADO 9. ERRADO
15. LETRA D

4. CORRETO ío.CORRETO
16.ERRADO

5. ERRADO li. ERRADO
17. ERRADO

6. CORRETO 12. CORRETO

X 65

/

Conceitos Básicos

KUBERNETS

INCIDÊNCIA EM PROVA: MÉDIA

O Kubernetesé um sistema de código aberto que foi desenvolvido pelo
Google para gerenciamento de aplicativos em containers através de múltiplos hosts de um cluster.Tem como principal objetivo facilitar a implantação de aplicativos baseados em microservices. Ele foi baseado na experiência do Google de muitos anos trabalho com containers,adaptando-o para se trabalhar com Docker.
kubernetes

O Kubernetes é uma ferramenta de orquestração que oferece recursos de gerenciamento para containers, foi muito útil para ser utilizado até o Docker Swarm 1.0, pois disponibilizava muitos recursos que o Docker não disponibilizava até aquele momento, entre eles:Balanceamento de carga e movimento de containers sem perda de dados.
A principal vantagem que se tem ao utilizar o Kubernetes é que você não está preso as limitações da API do Docker, logo você tem total liberdade já que o Kubernetes não foi desenvolvido especialmente para o Docker, você pode trocar a sua estrutura de Docker para Rockets e vice-versa por exemplo.
Hoje o Kubernetes é mantido pela Cloud Native Computing Foundation etem como papel principal prover o gerenciamento de clusters que executam as aplicações. Esses clusters podem ser hots disponíveis em nuvem, logo kubernetes é ideal para cloud native apps que podem exigir escalabilidade rápida.
X 65

/

Para ficar mais claro, imagine o seguinte: Você precisa fazer deploy de uma nova versão de uma aplicação em nuvem, milhares de coisas podem dar errado e você pode precisar realizar rollback para a versão anterior. Porém além disso, a aplicação é composta por dezenas de microsserviços,cada um com um ciclo de vida diferente do outro, releases diferentes, tecnologias diferentes, etc.

Pensando nisso a arquitetura de microsserviços adotou o Kubernetes como uma referência,
já que na prática as aplicações baseadas em arquitetura de microsserviços, incorporam automação em todo seu ciclo de vida, logo diferente de aplicações monolíticas, com forte acomplamento, as APIs com microsserviços tem características descentralizadas e fracamente acopladas.Logo, basta encapsular as principais características dos serviços em containers.
Como esses contêineres possuem o serviço e todas as suas dependências, eles se tornam independentes da infraestrutura, podendo ser facilmente migrados de uma cloud para outra, por exemplo, facilitando escalabilidade e deploy.
Dentro desse contexto, o Kubernetes oferece várias funcionalidades, dentre eles temos a ideia central, isto é, o estado da aplicação. Para o Kubernetes existes dois estados de uma aplicação:o atual e o desejado. O estado atual da aplicação descreve a realidade. Por exemplo,
quantas réplicas de um determinado serviço estão em execução, qual a versão em produção de cada serviço e por aí vai.
Já o estado desejado descreve como o time ou a pessoa responsável pela aplicação deseja que ela esteja naquele momento. O Kubernetes implementa uma série de loops que ficam constantemente verificando se o estado atual é igual ao estado desejado. Esse papel é desempenhado pelos chamados Controllers.
Quando um controller identifica que o estado atual é diferente do estado desejado, ele aciona outros componentes do sistema para fazer novamente com que o estado atual se iguale ao estado desejado. Todo esse processo de monitoramento e gestão do estado da aplicação, sem contar a execução da aplicação em si, exige uma série de componentes. É por isso que a arquitetura de um ambiente Kubernetes é baseada em um cluster de máquinas.
PROFESSOR, COMO FUNCIONA NA PRÁTICA 0 KUBERNETES?

Pessoal, o Kubernetes é composto por uma vários componentes, cada um com um propósito diferente. Para garantir que exista uma separação de responsabilidades e que o sistema seja resiliente, o kubernetes utiliza um clusterde máquinas para serexecutado, logo as máquinas de um cluster são separadas em três tipos: Node, Etcd e Master.
MÁQUINAS KUBERNETES DESCRIÇÃO

NODE O papel de um node é executar os contêineres que encapsulam as aplicações.

0 etcd é a base de dados distribuída que é utilizada para armazenar tudo o que acontece dentro do cluster, incluindo o estado da aplicação.
O master é responsável pelos principais componentes do kubernetes, como o scheduler, que tem a responsabilidadaede controlara alocação de recursos no cluster.
Como já vimos as aplicações que utilizam microsserviços, constumam utilizar containers para encapsulamento dos microsserviços. No entanto, quando falamos sobre aplicações sendo executadas em um cluster Kubernetes, não falamos sobre contêineres diretamente,mas sim sobre Pods. No Kubernetes, temos o kubeletque é uma pequena aplicação localizada em um nó que se comunica com o plano de controle, assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.
Pods são a unidade básica de um cluster. Os Pods encapsulam um ou mais containers de uma aplicação e representam um processo dentro do cluster. Logo, quando fazemos o deploy de uma aplicação no Kubernetes, estamos criando uma ou mais Pods. No Kubernetes,kubelet é uma pequena aplicação localizada em um nó que se comunica com o plano de controle,assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.
Porfim, para garantir que o acesso a um microsserviços esteja sempre disponível, temos um objeto no Kubernetes, chamado de Service, o Service é que encapsula um ou mais Pods e é capaz de encontra-los dinamicamente em qualquer lugar do cluster. A seguir conseguimos didaticamente ver a diferença da virtualização, do emprego de Docker e do Kubernetes:
r APP

4- LIBRARIES
* { APP

O kubernetes

L OPERATING SYSTEM

L LIBRARIES

Virtual machine Docker container

Hypervisor ijjjjF docker

> ►

| Operatinq system | 1 Operatinq system 1

te docker
Hardware I 1 Hardware I

áf docker docker

Virtualized deployment Container deployment Kubernetes deployment
X 65

/

Precisamos por últimos falar do CNFC (Cloud Native Computing Foundation):

CLOUD NATIVE

COMPUTING FOUNDATION

Pessoal, o CNFC é parte do Linux foundation e oferece suporte para projetos nativos em nuvem,como o Kubernetes, o Envoy e o Prometheus. Como fundação a CNFC é responsável por diversas certificações em Kubernetes, que é seu principal expoente, além de promover a culturaDevOps mundo a fora.
O que a Cloud Native Computing Foundation busca é promover o desenvolvimento e evolução do emprego de containers no desenvolvimento de soluções, principalmente em soluções nativas de nuvem.
(TJ-MS - 2017) Kubernetes é uma ferramenta de orquestração que oferece recursos de gerenciamento para containers, como balanceamento de carga e migração sem perda de dados.
Comentários: Perfeito! Foi a primeira que vimos: Kubernetes é uma ferramenta de orquestração que oferece recursos de gerenciamento para containers, como balanceamento de carga e migração sem perda de dados (Correto).
QUESTõES CoMENTADAS - KUBERNETES

í. (FGV / FUNSAÚDE-CE - 2021) Pod é uma unidade atômica de escalonamento, implantação e isolamento na execução de um grupo de contêineres no Kubernetes, analise as afirmativas a seguir.
I. Um Pod garante uma mesma localização para os seus contêineres, graças a isso eles têm diversas formas de interagir com bom desempenho, por exemplo, através de troca de arquivos,uso de interface de redes ou de mecanismos de comunicação entre processos.

II. Um Pod tem um endereço IP, um nome e uma faixa de portas compartilhadas por todos os contêineres pertencentes a ele. Isso significa que os contêineres de um mesmo Pod devem ser configurados cuidadosamente a fim de evitar conflitos de portas.
III. Um Pod é um elemento persistente no tempo, ele resiste às operações de redimensionamento, falhas de verificação de sanidade de contêineres e migrações entre nós.
Está correto o que se afirma em:

a) I, somente.

b) II, somente.

c) III, somente.

d) I e II, somente.

e) I e III, somente.

Comentários:

Um Pod tem um endereço IP, um nome e uma faixa de portas compartilhadas por todos os contêineres pertencentes a ele. Isso significa que os contêineres de um mesmo Pod devem ser configurados cuidadosamente a fim de evitar conflitos de portas. Além disso, um Pod garante uma mesma localização para os seus contêineres, graças a isso elestêm diversas formas de interagir com bom desempenho, por exemplo, através de troca de arquivos, uso de interface de redes ou de mecanismos de comunicação entre processos.
Gabarito: Letra D

2. (CESPE / SEFAZ-CE - 2021) Com a implantação do Kubernetes, é obtido um cluster com pelo menos um nó de trabalho (worker node); os nós de trabalho, por sua vez, hospedam vários componentes da carga de trabalho do aplicativo.
Comentários:

Pessoal, com a implantação do Kubernetes, é obtido um cluster com pelo menos um nó de trabalho(worker node); os nós de trabalho, por sua vez, hospedam vários componentes da carga de trabalho do aplicativo.
Gabarito: Correto

3. (CESPE / SERPRO - 2020) A camada de gerenciamento do Kubernetes possui o componente etcd, cuja função é observar pods que foram criados sem nenhum node atribuído e selecionar um node para execução.
Comentários:

Conforme vimos, o etcd é a base de dados distribuída que é utilizada para armazenar tudo o que acontece dentro do cluster, incluindo o estado da aplicação. Não tem função de observar pods que foram criados sem nenhum noda atribuído e selecionar um node para execução.
Gabarito: Errado

4. (IADES / BRB - 2021) Kubernetes é uma plataforma de código aberto, portável e extensiva para o gerenciamento de cargas de trabalho e serviços distribuídos em contêineres, que facilita tanto a configuração declarativa quanto a automação. Ele possui um ecossistema grande e de rápido crescimento. Serviços, suporte e ferramentas para Kubernetes estão amplamente disponíveis.Disponível em: <https://kubernetes.io/pt-br/docs/concepts/overview/>. Acesso em:
25 jun.
2021, com adaptações.

Com base notexto apresentado e considerando o contexto do Kubernetes, assinale a alternativa que corresponde à ferramenta disponibilizada para realizar operações nos clustersKubernetes,
por meio de interface de linha de comando, pela qual é possível realizar a implantação de aplicações, inspecionar e gerenciar recursos do cluster e visualizar logs.
a) Kubeadm b) Minikube c) Kubectl d) Kind e) Kubelet
Comentários:

Kubernetes é uma plataforma de código aberto, portável e extensiva para o gerenciamento de cargas de trabalho e serviços distribuídos em contêineres, que facilita tanto a configuração declarativa quanto a automação, a ferramenta para operações nos clusters, que é utilizada em linha de comando é o Kubectl.
x

X 85

/

Gabarito: Letra C

5. (CESPE / SEFAZ-CE - 2021) No Kubernetes, kubelet é uma pequena aplicação localizada em um nó que se comunica com o plano de controle, assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.
Comentários:

Exato! Literalmente o vimos na aula: No Kubernetes, temos o kubelet que é uma pequena aplicação localizada em um nó que se comunica com o plano de controle,assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto doKubernetes

Gabarito: Correto

6. (PUC-RS / TJ-MS - 2017) Sistemas virtualizados e containers são conceitos importantes para computação na nuvem. Para gerenciar grande número de servidores físicos,virtualizados e containers, utilizam-se ferramentas especializadas de configuração remota.Indique a afirmativa que descreve de forma CORRETA os conceitos relativos a sistemas virtualizados e containers e as ferramentas de gerenciamento disponíveis.
a) Puppet e Ansible são ferramentas que tem a finalidade de simplificar o processo de gerenciamento de servidores remotos. Essas ferramentas funcionam apenas com servidores físicos ou virtualizados. Elas não suportam containers.
b) Puppet e Ansible podem ser usados para gerenciar serviços virtualizados. Ansible é preferível por ser uma ferramenta multi-plataforma, enquanto Puppetfunciona apenas paraLinux, pois todos os seus comandos remotos são executados via SSH.
c) Containers e máquinas virtuais são sinônimos, pois ambos são usados para virtualizar o hardware que hospeda um sistema operacional completo, que pode ser diferente do sistema operacional da máquina física.
d) Containers do tipo Dockers podem ser orquestrados apenas pelo Docker Swarm, que foi desenvolvido especificamente para suportar essa tecnologia de container.
e) Kubernetes é uma ferramenta de orquestração que oferece recursos de gerenciamento para containers, como balanceamento de carga e migração sem perda de dados.
Comentários:

A questão extrapola no conhecimento e só a alternativa E foca no nosso assunto,
Kubernetes, sem mais enrolação, está perfeita a definição: Kubernetes é uma ferramenta de orquestração que x
X 85

/

oferece recursos de gerenciamento para containers, como balanceamento de carga e migração sem perda de dados.
Gabarito: Letra E

7. (CESPE / SEFAZ-CE - 2021) No Kubernetes, kubelet é uma pequena aplicação localizada em um nó que se comunica com o plano de controle, assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.
Comentários:

Conforme vimos, o kuberlet é uma aplicação localizada em um nó que se comunica com o plano de controle, assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.
Gabarito: Correto

8. (CESPE / SERPRO - 2021) Para obter o status de um node nomeado como nodei em um cluster,deve ser executado o comando a seguir: Kubectl describe node nodei.

Comentários:

É impossível decorartodos os comandos do Kubectl, parece que dessa vez a banca entendeu isso.

Gabarito: Anulada

9. (CESPE / SERPRO - 2021) A camada de gerenciamento possui o componente etcd, cuja função é observar pods que foram criados sem nenhum node atribuído e selecionar um node para execução.
Comentários:

O componente etcd, como vimios não tem a função de observar pods, veja:

MÁQUINAS KUBERNETES | DESCRIÇÃO

NODE O papel de um node é executar os contêineres que encapsulam as aplicações.

ETCD O etcd é a base de dados distribuída que é utilizada para armazenar tudo o que acontece dentro do cluster, incluindo o estado da aplicação.
MASTER O master é responsável pelos principais componentes do kubernetes, como o scheduler, que tem a responsabilidadae de controlar a alocação de recursos no cluster.
/ 85

/

A questão trata do kube scheduler que é o componente cuja função é observar pods que foram criados sem nenhum node atribuído e selecionar um node para execução.
Gabarito: Errado io.(FGV / TJ-RO - 2021) A equipe de desenvolvimento de sistemas de um tribunal de contas está guiando a implantação de um Webservice REST. A implantação será dividida nos seguintes grupos distintos de containers Docker-,
- Grupo A: responsável pela execução da aplicação do Webservice REST

- Grupo B: responsável pela execução do Sistema Gerenciador de Banco de Dados utilizado peloWebservice REST Os Grupos A e B terão seu próprio contexto de armazenamento e rede a serem orquestrados por um cluster de Kubernetes.
Para que a conexão de rede entre os containers dos Grupos A e B seja bem-sucedida pelo orquestrador, independentemente dos endereços IP a eles atribuídos, deverá ser configurado um novo:
a) pod b) replicaSet c) service d) ingress e) statefulSet
Comentários:

Deverá ser configurado um novo service. Pessoal, essa questão vai além na orquestração de clusters no Kubernetes, mas tudo bem. Note que o Pod já é um conjunto de containers, porém para que possamos cria-lo como serviço de rede, basta configurar um serviço (service).
Gabarito: Letra C

11. (CESPE / STJ - 2015) A orquestração automatiza a implantação, o gerenciamento, a escala e a rede dos contêineres. As ferramentas de orquestração de contêineres fornecem umframework para gerenciar arquiteturas de microsserviços e contêineres em escala, e muitas delas são usadas no gerenciamento do ciclo de vida dos contêineres; entre elas, oDocker Swarm é uma plataforma a) que permite utilizar diversos recursos e ferramentas, como Apache e PHP,porém tudo rodando em um mesmo sistema operacional.
b) de código aberto criada pelo Google para operações de implantação de contêiner,
aumento e redução e automação em clusters de hosts.
x

X 85

/

c) de orquestração de contêiner de código aberto, sendo o mecanismo de clusterização nativo para e pelo Docker, utilizando sua mesma linha de comando.
d) que roda sobre o Kubernetes instalado em sistema operacional na versão Enterprise da RedHat, agregando opções de monitoramento, integração e entrega contínua.

e) usada pela Amazon para fornecer outros serviços aos clientes, como DNS,
balanceamento,
segurança e monitoramento, se integrando nativamente.

Comentários:

O correto seria dizer que o Docker Swarm é plataforma de orquestração de contêiner de código aberto, sendo o mecanismo de clusterização nativo para e pelo Docker, utilizando sua mesma linha de comando. Docker Swarm e Kubernets são orquestradores de container independentes.
Gabarito: Letra C

/ 85

/

LISTA DE QUESTõES - KUBERNETES

í. (FGV / FUNSAÚDE-CE - 2021) Pod é uma unidade atômica de escalonamento, implantação e isolamento na execução de um grupo de contêineres no Kubernetes, analise as afirmativas a seguir.
I. Um Pod garante uma mesma localização para os seus contêineres, graças a isso eles têm diversas formas de interagir com bom desempenho, por exemplo, através de troca de arquivos,uso de interface de redes ou de mecanismos de comunicação entre processos.

II. Um Pod tem um endereço IP, um nome e uma faixa de portas compartilhadas por todos os contêineres pertencentes a ele. Isso significa que os contêineres de um mesmo Pod devem ser configurados cuidadosamente a fim de evitar conflitos de portas.
III. Um Pod é um elemento persistente no tempo, ele resiste às operações de redimensionamento, falhas de verificação de sanidade de contêineres e migrações entre nós.
Está correto o que se afirma em a) I, somente.
b) II, somente.

c) III, somente.

d) I e II, somente.

e) I e III, somente.

2. (CESPE / SEFAZ-CE - 2021) Com a implantação do Kubernetes, é obtido um cluster com pelo menos um nó de trabalho (worker node); os nós de trabalho, por sua vez, hospedam vários componentes da carga de trabalho do aplicativo.
3. (CESPE / SERPRO - 2020) A camada de gerenciamento do
Kubernetes possui o componente etcd, cuja função é observar pods que foram criados sem nenhum node atribuído e selecionar um node para execução.
4. (IADES / BRB - 2021) Kubernetes é uma plataforma de código aberto, portável e extensiva para o gerenciamento de cargas de trabalho e serviços distribuídos em contêineres, que facilita tanto a configuração declarativa quanto a automação. Ele possui um ecossistema grande e de rápido crescimento. Serviços, suporte e ferramentas para Kubernetes estão amplamente disponíveis.Disponível em: <https://kubernetes.io/pt-br/docs/concepts/overview/>. Acesso em:
25 jun.
2021, com adaptações.

Com base notexto apresentado e considerando o contexto do Kubernetes, assinale a alternativa que corresponde à ferramenta disponibilizada para realizar operações nos clustersKubernetes,
por meio de interface de linha de comando, pela qual é possível realizar a implantação de aplicações, inspecionar e gerenciar recursos do cluster e visualizar logs.
a) Kubeadm b) Minikube c) Kubectl d) Kind e) Kubelet
5. (CESPE / SEFAZ-CE - 2021) No Kubernetes, kubelet é uma pequena aplicação localizada em um nó que se comunica com o plano de controle, assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.
6. (PUC-RS / TJ-MS - 2017) Sistemas virtualizados e containers são conceitos importantes para computação na nuvem. Para gerenciar grande número de servidores físicos,virtualizados e containers, utilizam-se ferramentas especializadas de configuração remota.Indique a afirmativa que descreve de forma CORRETA os conceitos relativos a sistemas virtualizados e containers e as ferramentas de gerenciamento disponíveis.
a) Puppet e Ansible são ferramentas que tem a finalidade de simplificar o processo de gerenciamento de servidores remotos. Essas ferramentas funcionam apenas com servidores físicos ou virtualizados. Elas não suportam containers.
b) Puppet e Ansible podem ser usados para gerenciar serviços virtualizados. Ansible é preferível por ser uma ferramenta multi-plataforma, enquanto Puppet funciona apenas paraLinux, pois todos os seus comandos remotos são executados via SSH.
c) Containers e máquinas virtuais são sinônimos, pois ambos são usados para virtualizar o hardware que hospeda um sistema operacional completo, que pode ser diferente do sistema operacional da máquina física.
d) Containers do tipo Dockers podem ser orquestrados apenas pelo Docker Swarm, que foi desenvolvido especificamente para suportar essa tecnologia de container.
e) Kubernetes é uma ferramenta de orquestração que oferece recursos de gerenciamento para containers, como balanceamento de carga e migração sem perda de dados.
7. (CESPE / SEFAZ-CE - 2021) No Kubernetes, kubelet é uma pequena aplicação localizada em um nó que se comunica com o plano de controle, assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.
8. (CESPE/SERPRO-2021) Para obter o status de um node nomeado como nodei em um cluster,deve ser executado o comando a seguir: Kubectl describe node nodei

9. (CESPE / SERPRO - 2021) A camada de gerenciamento possui o componente etcd, cuja função é observar pods que foram criados sem nenhum node atribuído e selecionar um node para execução.
10. (FGV / TJ-RO - 2021) A equipe de desenvolvimento de sistemas de um tribunal de contas está guiando a implantação de um Webservice REST. A implantação será dividida nos seguintes grupos distintos de containers Docker-.
- Grupo A: responsável pela execução da aplicação do Webservice REST

- Grupo B: responsável pela execução do Sistema Gerenciador de Banco de Dados utilizado peloWebservice REST Os Grupos A e B terão seu próprio contexto de armazenamento e rede a serem orquestrados por um cluster de Kubernetes.
Para que a conexão de rede entre os containers dos Grupos A e B seja bem-sucedida pelo orquestrador, independentemente dos endereços IP a eles atribuídos, deverá ser configurado um novo:
a) pod b) replicaSet c) service d) ingress e) statefulSet
11. (CESPE / STJ - 2015) A orquestração automatiza a implantação, o gerenciamento, a escala e a rede dos contêineres. As ferramentas de orquestração de contêineres fornecem um framework para gerenciar arquiteturas de microsserviços e contêineres em escala, e muitas delas são usadas no gerenciamento do ciclo de vida dos contêineres; entre elas, oDocker Swarm é uma plataforma a) que permite utilizar diversos recursos e ferramentas, como Apache e PHP,porém tudo rodando em um mesmo sistema operacional.
b) de código aberto criada pelo Google para operações de implantação de contêiner,
aumento e redução e automação em clusters de hosts.
c) de orquestração de contêiner de código aberto, sendo o mecanismo de clusterização nativo para e pelo Docker, utilizando sua mesma linha de comando.
d) que roda sobre o Kubernetes instalado em sistema operacional na versão Enterprise da RedHat, agregando opções de monitoramento, integração e entrega contínua.

e) usada pela Amazon para fornecer outros serviços aos clientes, como DNS,
balanceamento,
segurança e monitoramento, se integrando nativamente.

x

X 85

/

GABARITo - KUBERNETES

1. CORRETO 5- ERRADO

2. CORRETO 6. ERRADO

3- CORRETO 7- CORRETO

4- CORRETO 8. ANULADA

9. ERRADO

10. LETRA C

11. LETRA C

x78

X 85

/

Conceitos Básicos

OPENSHIFT

INCIDÊNCIA EM PROVA: MÉDIA

O OpenShift é uma ferramenta muito poderosa que além de orquestrar e gerenciar containers,oferece segurança, monitoramento e controle. Com o OpenShift podemos criar um ambiente baseado em containers e colocar aplicações construídas em diversas linguagens como: Java,Python, Ruby, e PHP, para rodar e escalar facilmente, trazendo maior agilidade no desenvolvimento utilizando metodologias DevOps, atendendo mais rapidamente e com menor esforço as demandas de negócio.
Red Hat

OpenShift Container Platform

O ::: © kube:admin *

Home

Cataloq

Project: all projects

O Add *

Cluster Status

Workloads

Networking

Storage

Builds

Monitorlng

Compute

Administration

Health

Kubernetes API OpenShift Console
Alerts Firing Crashlooping Pods

UP UP 0

Allgood All good
Alerts Pods

Control Plane Status

API Servers Up Controller Managers Up
Schedulers Up API Request Success Rate

Software Info

Kubernetes vl.l3.4+f2cc675

Documentation

Full Documentation t?

From getting started with creating your flrst application. to trying out more advanced build and deployment techniques.these resources provide what you need to set up and manage your environment as a cluster administrator or an application developer.
Additional Support

Cluster S tatus
Cluster Settings
Namespaces
Service Accounts
Roles

Role Blndings
Resource Quotas
Limit Ranges

Custom Resource Definitlons

Capacity Planning

CPU Usage

Memory Usage

Disk Usage Pod Usage p)
Interactive Learnlng Portal c?
Local Development t?

YouTubec?
Blogc?

Events

All Categories
-itter £ vents by name or message.

A containerização é fator fundamental aqui no Openshift, já que ele monitora os status dos clusters. Se lembrar do funcionamento do Kubernete vai perceber que temos containers como serviço basicamente, que em essência nada mais é que a automatização do dimensionamento das operações com as aplicações. Obviamente também temos automonitoramento,balanceamento,
orquestração, armazenamento, etc.

Dito isso, no OpenShift a Red Hat buscou ampliar esse conceito, enquanto que o
Kubernetes é o
Kernel dos sistemas distribuídos em containers, o Openshift é uma plataforma de containers kubernetes baseada em nuvem, literalmente um legitimo PAAS (Plataform as a service),além de parcialmente serconstruído em Dockertambém.
Logo, o Openshift oferece segurança consistente, monitoramento integrado,
gerenciamento centralizado de políticas e compatibilidade com cargas de trabalho de contêiner doKubernetes. É rápido, permite o provisionamento de autoatendimento e se integra a uma variedade de ferramentas. Em outras palavras, não há dependência de fornecedor.
Tanto o Kubernetes quanto o OpenShift apresentam uma arquitetura robusta e escalável que permite o desenvolvimento, a implantação e o gerenciamento de aplicativos rápidos e em larga escala. Temos então algumas diferenças fundamentais aqui, principalmente no tocante a implantação, vejamos:
O Kubernetes oferece mais flexibilidade como uma estrutura de código aberto e pode ser instalado em praticamente qualquer plataforma — como Microsoft Azure e AWS — bem como em qualquer distribuição Linux, incluindo Ubuntu e Debian. O OpenShift, por outro lado,requer o Red Hat
Enterprise Linux Atomic Host (RHELAH), Fedora ou CentOS proprietário da Red Hat. Isso restringe as opções para muitas empresas, especialmente se elas ainda não estiverem usando essas plataformas. As imagens no Openshift são armazenadas no componente registry.
Enquanto que o Kubernetes contém uma interface web complexa que pode confundir os novatos. Os usuários que desejam acessar a interface gráfica do usuário (GUI)da Web do
Kubernetes devem instalar o painel do Kubernetes e usar o kube-proxy para enviar a porta de sua máquina para o servidor de cluster. Já o OpenShift, por outro lado, apresenta um console web intuitivo que inclui uma página de login com um toque. O console oferece uma interface simples e baseada em formulário, permitindo que os usuários adicionem, excluam e modifiquem recursos. As imagens dos contêineres no Openshift podem ser armazenadas no componente denominado registry. No Openshift o estado persistente do master é armazenado no componente etcd.
Logo, tanto o Kubernetes quanto o OpenShift são sistemas populares de gerenciamento de contêineres e cada um tem seus recursos e benefícios exclusivos. Enquanto o Kubernetes ajuda a automatizar a implantação, o dimensionamento e as operações de aplicativos, oOpenShift é a plataforma de contêiner que funciona com o Kubernetes para ajudar os aplicativos a serem executados com mais eficiência.
X 85

/

QUESTõES CoMENTADAS - OPENSHIFT

í. (CESPE / TJPA - 2020) O Openshift provê recursos a partir do kubernets, sendo capaz de executar e disponibilizar aplicações a partir de contêineres. As imagens dos contêineres noOpenshift podem ser armazenadas no componente denominado a) Pod b) Build c) Secret d) Registry e) Master
Comentários:

As imagens dos contêineres no Openshift conforme vimos são armazenadas no Registry.

Gabarito: Letra D

2. (FGV/FUNSAÚDE-CE-2021) Em um cluster Openshift, há uma série de configurações que são feitas e devem ser persistidas. O estado persistente do master é armazenado no componente a) etcd b) haproxy c) API server d) Namespace e) Replica controller
Comentários:

Conforme vimos, no Openshift o estado persistente do masteré armazenado no componente etcd.

Gabarito: Letra A

3. (CESPE / ME - 2020) Na situação em que vários aplicativos desenvolvidos e baseados em microsserviços com abordagem de containers devem ser disponibilizados aos usuários de uma organização, é correto instalar e configurar a OpenShift Container Platform, que é a solução de gerenciamento de containers da RedHat, pois não há solução da Microsoft que oferte serviços de Kubernetes para disponibilização desses aplicativos.
Comentários:

A questão não faz nenhum sentido, Kubernetes pode ser utilizado em qualquer plataforma, naMicrosoft é oferecido através do AKS (Serviço de Kubernetes da Azure) no restante sobreOpenShift está correto.

Gabarito: Errado

X 85

/

LISTA DE QUESTõES - OPENSHIFT

í. (CESPE / TJPA - 2020) O Openshift provê recursos a partir do kubernets, sendo capaz de executar e disponibilizar aplicações a partir de contêineres. As imagens dos contêineres noOpenshift podem ser armazenadas no componente denominado a) Pod b) Build c) Secret d) Registry e) Master
2. (FGV/FUNSAÚDE-CE-2021) Em um cluster Openshift, há uma série de configurações que são feitas e devem ser persistidas. O estado persistente do master é armazenado no componente a) etcd b) haproxy c) API server d) Namespace e) Replica controller
3. (CESPE / ME - 2020) Na situação em que vários aplicativos desenvolvidos e baseados em microsserviços com abordagem de containers devem ser disponibilizados aos usuários de uma organização, é correto instalar e configurar a OpenShift Container Platform, que é a solução de gerenciamento de containers da RedHat, pois não há solução da Microsoft que oferte serviços de Kubernetes para disponibilização desses aplicativos.
GABARITo - OPENSHIFT

1. ERRADO 2. LETRA A
3. LETRA D

/

