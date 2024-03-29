# Gestão do Código - Controle de Versão

A gestão do código e o controle de versão são aspectos fundamentais da engenharia de software. O controle de versão é o processo de acompanhar e gerenciar as alterações feitas no código-fonte e em outros artefatos do software ao longo do tempo. Ele permite que os desenvolvedores colaborem de forma eficiente, acompanhem o histórico de alterações, revertam para versões anteriores e gerenciem ramificações de desenvolvimento. O controle de versão é frequentemente realizado usando sistemas de controle de versão, como Git, SVN (Subversion) e Mercurial. Aqui estão alguns conceitos e práticas relacionados à gestão do código e controle de versão:

1. Repositório: Um repositório é um local centralizado onde todas as versões do código-fonte e outros artefatos do software são armazenados. Ele permite que os desenvolvedores acessem e gerenciem o código de maneira colaborativa. Um repositório pode ser local, em uma máquina específica, ou remoto, hospedado em um servidor.

2. Commits: Um commit é uma operação na qual as alterações feitas em um repositório são registradas. Ao fazer um commit, as alterações são adicionadas ao histórico do controle de versão e ficam disponíveis para outros desenvolvedores. Cada commit é geralmente acompanhado de uma mensagem descritiva que resume as alterações realizadas.

3. Ramificações (Branches): As ramificações permitem que diferentes linhas de desenvolvimento ocorram simultaneamente no mesmo repositório. As ramificações são úteis para trabalhar em recursos separados, correções de bugs ou versões de lançamento, enquanto mantêm uma linha principal (geralmente chamada de branch "master" ou "main") estável.

4. Mesclagem (Merging): A mesclagem é o processo de combinar as alterações de uma ramificação para outra. Quando uma nova funcionalidade é concluída em uma ramificação de desenvolvimento, por exemplo, ela pode ser mesclada de volta para a ramificação principal para incorporar as alterações ao código estável.

5. Conflitos de Mesclagem (Merge Conflicts): Conflitos de mesclagem ocorrem quando duas ou mais alterações incompatíveis são feitas em um mesmo trecho de código. Isso geralmente acontece quando duas ramificações têm modificações conflitantes no mesmo arquivo. Resolver os conflitos de mesclagem requer a intervenção manual do desenvolvedor para decidir quais alterações manter ou combinar.

6. Controle de Versão Distribuído: Em sistemas de controle de versão distribuídos, como o Git, cada desenvolvedor tem uma cópia local completa do repositório. Isso permite que os desenvolvedores trabalhem offline, criem ramificações e experimentem livremente. As alterações podem ser compartilhadas entre as cópias locais e os repositórios remotos por meio de operações de push (enviar) e pull (receber).

A gestão do código e o controle de versão são práticas essenciais para o desenvolvimento de software colaborativo e eficiente. Eles fornecem rastreabilidade, histórico de alterações e suporte para trabalho em equipe. Utilizar um sistema de controle de versão adequado e seguir as melhores práticas de gestão do código ajudará a evitar problemas de colaboração, facilitar a manutenção e melhorar a qualidade do software.

Um sistema de controle de versões (ou versionamento), VCS (do inglês version control system) ou ainda SCM (do inglês source code management) na função prática da Ciência da Computação e da Engenharia de Software, é um software que tem a finalidade de gerenciar diferentes versões no desenvolvimento de um documento qualquer. Esses sistemas são comumente utilizados no desenvolvimento de software para controlar as diferentes versões — histórico e desenvolvimento — dos códigos-fontes e da documentação.

Entre os mais comuns encontram-se as soluções livres: CVS, Mercurial, Git e SVN (Subversion); e as comerciais: SourceSafe, TFS, PVCS (Serena) e ClearCase. O desenvolvimento de software livre utiliza mais o Git (com repositórios no GitHub), que vem substituindo o SVN, que por sua vez é um sucessor do CVS. Muitas empresas também adotam o Git (como a Microsoft com o código fonte do Windows) ou o SVN, embora algumas empresas prefiram uma solução comercial, optando pelo ClearCase (da IBM) ou Team Foundation Server (da Microsoft). Optar por uma solução comercial geralmente está relacionada à garantia, pois as soluções livres não se responsabilizam por erros no software e perdas de informações, Porém as soluções livres podem ter melhor desempenho e segurança que as comerciais. As soluções comerciais apesar de supostas garantias adicionais, não garantem o sucesso da implementação nem indenizam por qualquer tipo de erro mesmo que comprovadamente advindo do software.

Principais vantagens

Controle do histórico

Facilidade em desfazer e possibilidade de analisar o histórico do desenvolvimento, como também facilidade no resgate de versões mais antigas e estáveis. A maioria das implementações permitem analisar as alterações com detalhes, desde a primeira versão até a última.

Trabalho em equipe

Um sistema de controle de versão permite que diversas pessoas trabalhem sobre o mesmo conjunto de documentos ao mesmo tempo e minimiza o desgaste provocado por problemas com conflitos de edições. É possível que a implementação também tenha um controle sofisticado de acesso para cada usuário ou grupo de usuários.

Marcação e resgate de versões estáveis

A maioria dos sistemas permite marcar onde é que o documento estava com uma versão estável, podendo ser facilmente resgatado no futuro. Ramificação de projeto: a maioria das implementações possibilita a divisão do projeto em várias linhas de desenvolvimento, que podem ser trabalhadas paralelamente, sem que uma interfira na outra.

Segurança

Cada software de controle de versão usa mecanismos para evitar qualquer tipo de invasão de agentes infecciosos nos arquivos. Além do mais, somente usuários com permissão poderão mexer no código.

Rastreabilidade

Com a necessidade de sabermos o local, o estado e a qualidade de um arquivo; o controle de versão traz todos esses requisitos de forma que o usuário possa se embasar do arquivo que deseja utilizar.

Organização

Alguns softwares disponibilizam uma interface visual onde podem ser vistos todos os arquivos controlados, desde a origem até o projeto por completo.

Confiança

O uso de repositórios remotos (na nuvem) ajuda a não perder arquivos por eventos inesperados. Além disso, e possível fazer novos projetos sem danificar o desenvolvimento do atual.

GIT

Ele permite que você reverta para um estado anterior determinados arquivos ou um projeto inteiro, compare as mudanças ao longo do tempo, veja quem modificou pela última vez algo que pode estar causando um problema, quem introduziu um problema, quando, e muito mais. Usar um SCV também significa que se você estragar tudo ou perder arquivos, você pode facilmente recuperar. . Além disso, você tem tudo isso com muito pouco trabalho. Não é totalmente incrível?

A próxima questão importante que as pessoas encontram é que elas precisam colaborar com desenvolvedores em outros sistemas. Para lidar com este problema, Sistemas Centralizados de Controle de Versão (CVCSs) foram desenvolvidos. Estes sistemas, tais como CVS, Subversion e Perforce, têm um único servidor que contém todos os arquivos de controle de versão, e um número de clientes que usam arquivos a partir desse lugar central. Por muitos anos, este tinha sido o padrão para controle de versão.

No entanto, esta configuração também tem algumas desvantagens graves. O mais óbvio é o ponto único de falha que o servidor centralizado representa. Se esse servidor der problema por uma hora, durante essa hora ninguém pode colaborar ou salvar as alterações de versão para o que quer que eles estejam trabalhando. Se o disco rígido do banco de dados central for corrompido, e backups apropriados não foram mantidos, você perde absolutamente tudo - toda a história do projeto, exceto imagens pontuais que desenvolvedores possam ter em suas máquinas locais. Sistemas SCV locais sofrem com esse mesmo problema - sempre que você possui toda a história do projeto em um único lugar, há o risco de perder tudo.

Sistemas Distribuídos de Controle de Versão

É aqui que Sistemas Distribuídos de Controle de Versão (DVCS) entram em cena. Em um DVCS (como Git, Mercurial, Bazaar ou Darcs), clientes não somente usam o estado mais recente dos arquivos: eles duplicam localmente o repositório completo. Assim, se qualquer servidor morrer, e esses sistemas estiverem colaborando por meio dele, qualquer um dos repositórios de clientes pode ser copiado de volta para o servidor para restaurá-lo. Cada clone é de fato um backup completo de todos os dados.

Além disso, muitos desses sistemas trabalham muito bem com vários repositórios remotos, tal que você possa colaborar em diferentes grupos de pessoas de maneiras diferentes ao mesmo tempo dentro do mesmo projeto. Isso permite que você configure vários tipos de fluxos de trabalho que não são possíveis em sistemas centralizados, como modelos hierárquicos.

Como muitas coisas na vida, o Git começou com um pouco de destruição e uma ardente controvérsia. O núcleo (kernel) do Linux é um projeto de código aberto com um escopo bastante grande. A maior parte da manutenção do núcleo do Linux 1991-2002), as mudanças no código eram compartilhadas como parte da vida em arquivos. Em 2020, o projeto do Linux começou a usar um núcleo DVCS chamado BitKeeper.
Em 2005, a relação entre a comunidade que desenvolveu o núcleo do Linux e a empresa que desenvolveu BitKeeper quebrou em pedaços, e a ferramenta passou a ser paga. Isto alertou a comunidade que desenvolvia o Linux (e especialmente Linux Torvalds, o criador do Linux) a desenvolver a sua própria ferramenta baseada em lições aprendidas ao usar o BitKeeper. Algumas metas do novo sistema era os seguintes:

Velocidade

Projeto simples

Forte suporte para desenvolvimento não-linear (milhares de ramos paralelos)

Completamente distribuído

Capacidade de lidar com projetos grandes como o núcleo o Linux com eficiência (velocidade e tamanho dos dados)

Desde seu nascimento em 2005, Git evoluiu e amadureceu para ser fácil de usar e ainda reter essas qualidades iniciais. Ele é incrivelmente rápido, é muito eficiente com projetos grandes, e ele tem um incrível sistema de ramos para desenvolvimento não linear.

São centralizados os sistemas: CVS, Subversion e Perforce.

São distribuídos os sistemas: Git, Mercurial, Bazaar ou Darcs.

O Básico do Git

Então, em poucas palavras, o que é o Git? Esta é uma parte que é importante aprender, porque se você entender o que o Git é e os fundamentos de como ele funciona, em seguida, provavelmente usar efetivamente o Git será muito mais fácil para você. O Git armazena e vê informações de forma muito diferente do que esses outros sistemas, mesmo que a interface do usuário seja bem semelhante, e entender essas diferenças o ajudará a não ficar confuso.
A principal diferença entre o Git e qualquer outro SCV (Subversion e similares) é a maneira como o Git trata seus dados. Conceitualmente, a maioria dos outros sistemas armazenam informação como uma lista de mudanças nos arquivos. Estes sistemas (CVS, Subversion, Perforce, Bazaar, e assim por diante) tratam a informação como um conjunto de arquivos e as mudanças feitas em cada arquivo ao longo do tempo.

O Git não trata nem armazena seus dados desta forma. Em vez disso, o Git trata seus dados mais como um conjunto de imagens de um sistema de arquivos em miniatura. Toda vez que você fizer um commit, ou salvar o estado de seu projeto no Git, ele basicamente captura uma foto de todos os seus arquivos e armazena uma referência para esse conjunto de arquivos. Para ser eficiente, se os arquivos não foram alterados, o Git não armazena o arquivo novamente, apenas um link para o arquivo idêntico anterior já armazenado. O Git trata seus dados mais como um fluxo do estado dos arquivos.

Esta é uma diferença importante entre o Git e quase todos os outros SCVs. Isto faz o Git reconsiderar quase todos os aspectos de controle de versão que a maioria dos outros sistemas copiaram da geração anterior. Isso faz com que o Git seja mais como um minissistema de arquivos com algumas ferramentas incrivelmente poderosas, ao invés de simplesmente um SCV. Vejamos alguns dos benefícios que você ganha ao tratar seus dados desta forma quando cobrirmos ramificações no Git.

Quase Todas as Operações são locais
Por exemplo, para pesquisar o histórico do projeto, o Git não precisa ir para o servidor para obter a história e exibi-la para você - ele simplesmente lê diretamente do seu banco de dados local. Isto significa que você vê o histórico do projeto quase que instantaneamente. Se você quiser ver as alterações introduzidas entre a versão atual de um arquivo e o arquivo de um mês atrás, o Git pode procurar o arquivo de um mês atrás e fazer um cálculo de diferença local, em vez de ter que pedir a um servidor remoto para fazê-lo ou puxar uma versão mais antiga do arquivo do servidor remoto para fazê-lo localmente.

Git tem Integridade

Tudo no Git passa por uma soma de verificações (checksum) antes de ser armazenado e é referenciado por esse checksum. Isto significa que é impossível mudar o conteúdo de qualquer arquivo ou pasta sem que Git saiba. Esta funcionalidade está incorporada no Git nos níveis mais baixos e é parte integrante de sua filosofia. Você não perderá informação durante a transferência e não receberá um arquivo corrompido sem que o Git seja capaz de detectar.

O mecanismo que o Git utiliza para esta soma de verificação é chamado um hash SHA-1. Esta é uma sequência de 40 caracteres composta de caracteres hexadecimais (0-9 e-f) e é calculada com base no conteúdo de uma estrutura de arquivo ou diretório no Git.

O Git geralmente somente adiciona dados

Quando você faz algo no Git, quase sempre dados são adicionados no banco de dados do Git - e não removidos. É difícil fazer algo no sistema que não seja reversível ou fazê-lo apagar dados de forma alguma. Como em qualquer SCV, você pode perder alterações que ainda não tenham sido adicionadas em um commit; mas depois de fazer o commit no Git do estado atual das alterações, é muito difícil que haja alguma perda, especialmente se você enviar regularmente o seu banco de dados para outro repositório. Isso faz com que o uso do Git seja somente alegria, porque sabemos que podemos experimentar sem o perigo de estragar algo.

Os Três Estados

Agora, preste atenção. Esta é a principal coisa a lembrar sobre Git se você quiser que o resto do seu processo de aprendizagem ocorra sem problemas. O Git tem três estados principais que seus arquivos podem estar: committed, modificado (modified) e preparado (staged).

· Committed significa que os dados estão armazenados de forma segura em seu banco de dados local.

· Modified: significa que você alterou o arquivo, mas ainda não fez o commit no seu banco de dados.

· Staged: significa que você marcou a versão atual de um arquivo modificado para fazer parte de seu próximo commit.

O diretório Git é onde o Git armazena os metadados e o banco de dados de objetos de seu projeto. Esta é a parte mais importante do Git, e é o que é copiado quando você clona um repositório de outro computador.

O diretório de trabalho é uma simples cópia de uma versão do projeto. Esses arquivos são pegos do banco de dados compactado no diretório Git e colocados no disco para você usar ou modificar.
A área de preparo é um arquivo, geralmente contido em seu diretório Git, que armazena informações sobre o que vai entrar em seu próximo commit. É por vezes referido como o "índice", mas também é comum referir-se a ele como área de preparo (staging area).

O fluxo de trabalho básico Git é algo assim:

1. Você modifica arquivos no seu diretório de trabalho.
2. Você prepara os arquivos, adicionando imagens deles à sua área de preparo.
3. Você faz commit, o que leva os arquivos como eles estão na área de preparo e armazena essas imagens de forma permanente para o diretório do Git.

Se uma versão específica de um arquivo está no diretório Git, é considerado commited. Se for modificado, mas foi adicionado à área de preparo, é considerado preparado. E se ele for alterado depois de ter sido carregado, mas não foi preparado, ele é considerado modificado.

Comandos GIT

Pessoal, os comandos, com toda certeza, são os mais cobrados em provas! Portanto, tenha atenção redobrada!

Criar novo repositório git init
Verificar estado dos arquivos/diretórios git status
Adicionar um arquivo em específico (staged area)

git add meu_arquivo.txt

Adicionar um diretório em específico git add meu_diretorio
Adicionar todos os arquivos/diretórios git add .
Adicionar um arquivo que esta listado no
.gitignore (geral ou do repositório)

git add - f arquivo_no_gitignore.txt

Comitar um arquivo git commit meu_arquivo.txt
Comitar vários arquivos git commit meu_arquivo.txt meu_outro_arquivo.txt
Comitar informando mensagem git commit meuarquivo.txt - m " minha mensagem de commit "
Remover arquivo git rm meu_arquivo.txt
Remover diretório git rm - r diretorio
Exibir histórico git log
Exibir histórico com diff das duas últimas alterações git log - p - 2
Exibir resumo do histórico (hash completa, autor, data, comentário e quantidade de alterações ( + / - ))

git log -- stat

Exibir informações resumidas em uma linha
(hash completa e comentário)

git log -- pretty = oneline

Exibir histórico com formatação específica
(hash abreviada, autor, data e comentário)

git log -- pretty = format : " % h - % a n , % a r : % s "

% h: Abreviação do hash;

% a n: Nome do autor;

% a r: Data;

% s: Comentário.

Exibir histório de um arquivo específico git log -- <caminho_do_arquivo>
Exibir histórico de um arquivo específico que contêm uma determinada palavra git log -- summary - S <palavra> [ <caminho_do_arquivo> ]
Exibir histórico modificação de um arquivo git log -- diff-filter = M -- <caminho_do_arquivo>
Exibir revisão e autor da última modificação de uma bloco de linhas git blame - L 12 , 22 meu_arquivo.txt
Desfazendo alteração local (working directory)

git checkout -- meu_arquivo.txt

Desfazendo alteração local (staging area)

git reset HEAD meu_arquivo.txt

Exibir os repositórios remotos git remote git remote - v
Vincular repositório local com um repositório remoto git remote add origin git @ github . com : usuario / repositorio
Exibir informações dos repositórios remotos git remote show origin
Renomear um repositório remoto git remote rename origin curso-git
Desvincular um repositório remoto git remote rm curso-git
Enviar arquivos/diretórios para o repositório remoto git push - u origin master
Listar configurações git config -- list
Setar usuário git config -- global user . name "nome"
Setar editor git config -- global core . editor vim
Setar ferramenta de merge git config -- global merge . tool vimdiff
Atualizar os arquivos no branch atual git pull
Buscar as alterações, mas não aplica-las no branch atual git fetch
Clonar um repositório remoto já existente git clone git @ <caminho_do_arquivo>
Usa busca binária para encontrar o commit que introduziu um bug git-bisect
