# Desenvolvimento de Informação - Linguagem R

Índice

1) Linguagem R - Teoria

Linguagem R -Introdução

1) Conceitos básicos.

2) Nossa primeira aula de R

3) Objetos em R

Uma viagem pelo R

1) Pacotes.

2) Funções do R-base

3) Constantes.

4) Matrizes.

5) Funções.

6) Estruturas de controle

Resumo

Exercícios

1) Questões e Exercício Prático - Baixe o R e R STUDIO!

2) Exercícios.

3) Gabarito

4) Código da videoaula

✓—

THIAGO CAVALCANTI

LINGUAGEM R - INTRoDUçÃo

1) CoNCEIToS BÁSICoS

Em nossa videoaula, mostramos o passo a passo para instalação do R e do R Studio. É um processo simples, semelhante a instalação de um programa qualquer. É muito importante você ter o ambiente configurado na sua máquina para fazer os exemplos que veremos ao longo da aula. Dito isto, vamos começar nossa aula com uma simples pergunta: o que é R?
R é uma linguagem computacional que permite que usuário programe algoritmos e utilize ferramentas que foram programadas por outras pessoas.
Calma professor!! Já tem um monte de informações nas linhas acima que eu não entendi!

Ok! Vamos devagar! As unidades de processamento (CPUs) são projetadas para reconhecer instruções codificadas como padrões de bits. Essa coleção de instruções, juntamente com o sistema de codificação, é chamada de linguagem de máquina. Pense como seria difícil se todo programa que fosse escrito tivesse que fazer uso de linguagem de máquina.
As linguagens de programação têm sido desenvolvidas buscando permitir que algoritmos sejam expressos em um formato palatável aos humanos e facilmente convertidos em instruções de linguagem de máquina. Ou seja, uma linguagem de programação é uma forma se comunicar com o computador.
Agora vamos falar de algoritmos. Vejamos a definição de algoritmos na figura abaixo:

Um passo a passo para produzir algo. O computador precisa que você descreva TODAS as ações que você quer que ele execute! Se algum passo for esquecido, ele não será executado ... Pense em uma receita de bolo ... esquecer algum ingrediente pode gerar um efeito terrível sobre o resultado. ©
O R é uma linguagem funcional/orientada a objetos criada em 1996 por Ross lhaka e
Robert
Gentleman que aliada a um ambiente integrado permite a manipulação de dados, realização de cálculos e geração de gráficos. Uma curiosidade é que o nome R é a letra inicial do primeiro nome de cada um dos seus criadores. Mas não foi apenas por isso que a linguagem recebeu esse nome ...
R é semelhante à linguagem S desenvolvida pela AT&T's Bell Laboratories e que já era utilizada para análise de dados, mas com a vantagem de ser de livre distribuição (open-source).Para a instalação do R basta conectar-se ao site http://cran.r-project.org. CRAN é o acrônimo para"Comprehensive R Archive Network, neste site você consegue escolher o local mais próximo de onde você encontra-se e fazer o download da última versão do R.
Mas ... para que serve o R mesmo?

R é uma linguagem de programação com foco em análise de dados. Ou seja, voltada à interação dinâmica com os dados e modelos. Além disso, R é gratuito e de código aberto e seu ambiente permite explorar dados interativamente; mas, à medida que a análise evolui, R é visto como uma linguagem de programação completa para desenvolver e automatizar soluções,desenvolver softwares e pacotes.
Vejamos uma figura que resume as funcionalidades ou capacidades da programação em R.

FIQUE

ATENTOI

Figura 1 - (1) Trabalhar com todos os conjuntos de dados. (2) Muitos pacotes. (3) Várias bibliotecas gráficas. (4) Cálculos rápidos. (5) Linguagem abrangente. (6) Código aberto.
Além disso, R é uma linguagem interpretada e uma ferramenta poderosa para manipulação,processamento, visualização e análise de dados, bem como simulações e modelagem estatísticas.Mas o que seria uma linguagem interpretada? Relaxa ... eu explico.

INDO MAIS

FUNDO!

Linguagem compiladas x interpretadas

Uma das classificações possíveis para linguagens de programação é quanto a execução.
Nesta taxonomia podemos classificar a linguagem como compilada ou interpretada.

O processo de converter um programa de uma linguagem para outra é chamado de tradução ou compilação. O programa em sua forma original é o programa fonte; a versão traduzida é o programa objeto.
O processo de tradução consiste em três atividades - análise léxica, análise sintática e geração de código realizadas por unidades do tradutor conhecidas como analisador léxico, analisador sintático (ou parser) e gerador de código. Vejamos esse fluxo em uma figura:
Programa fonte
Programa objeto
Observem que o programa objeto será executado e sua organização depende do sistema operacional. Na execução do código os dados ou parâmetros são passados.
Já a linguagem interpretada é uma linguagem de programação, onde o código fonte é executado por um programa de computador chamado interpretador. O interpretador lê um programa escrito em linguagem de alto nível e o executa, ou seja, faz o que o programa diz. Ele processa o programa um pouco de cada vez, alternadamente: ora lendo algumas linhas, ora realizando computações.
Código fonte independente do sistema operacional atua cada vez que se executa o programa'
resultado

Como vantagens da linguagem interpretada podemos listar:

* São rápidas e práticas, permitem agregar funcionalidades sem depender de ferramentas e compiladores.
* Podem seradaptadas a diversas tecnologias

* Não dependem de instalações e ou bibliotecas.

* Não precisam de uma ferramenta específica de desenvolvimento.

Já as desvantagens são:

* Por não ser compilada, erros de sintaxe não são identificados no desenvolvimento.

* Não tem acesso completo a recursos da máquina por questões de segurança.

* Depende de um interpretador local para ser executado.

Agora ... se eu pedir para você preencher a lacuna ...Ré uma linguagem!

O que você acha? Interpretada, certo?! Preenche a lacuna e grifa para você não esquecer!

Vamos em frente!

Hora de abrir o R ... muito provavelmente você terá esse ícone na área de trabalho (esse do lado esquerdo!)
A instalação padrão do R vem com uma interface gráfica para o usuário
(Graphical User

Interface - GUI). I«RGui(64R.bRGjtu)i (64-bit)

File Edrt ViewNMoisWc iPnadcokawgses"Wl,einEddiot w"sicwHeelapcka9tt ^indows Help z - 7X"
voce encontrara o R no menu iniciare no Macvocê verá o ícone do R entre seus aplicativos. No meu caso, consigo encontrar o executável RGui (64-bits) na busca doWindows. Ao executar o mesmo, a seguinte interface é aberta.
Apesar de o R vir com uma interface gráfica interessante, existe umAmbiente de Desenvolvimento
Integrado (Jntegrated Development
Environment- IDE) chamado RStudio,
com várias funcionalidades e gratuito. O
RStudio possui algumas vantagens em relação ao R Gui:
l^lQll^lelolíõlíâ]

TOME

NOTA!

* Highlight do código;

* Autocomplete;

* Match automático de parênteses e chaves;

* Interface intuitiva para objetos, gráficos e script;

* Criação de "projetos" com interface para controle de versão;

* Facilidade na criação de pacotes;

* Interação com HTML, entre outras.

Você pode abrir o RStudio em seu computador e iniciar um novo Script em "File" ->
"New File" ->
"New RScript". Você também pode fazer isso com CTRL + SHIFT + N ou acessando o botão abaixo.

Podemos dividira tela do RStudio em quatro grandes áreas:

í. Script: A tela superior esquerda do RStudio é o editor de texto onde você vai escrever seus Scripts. Ele possui code highlighting entre outras funcionalidades.
2. Console: No canto inferior esquerdo fica o console. O console nada mais é do que uma seção aberta de R, em que os comandos são executados.
3. Área de trabalho e histórico: Ficam no canto superior direito. Os objetos criados e o histórico dos comandos podem ser acessados ali.
4. Arquivos, Gráficos, Pacotes, Ajuda: Ficam no canto inferior direito. Você pode explorar pastas e arquivos diretamente do RStudio na aba "Files"; os gráficos que forem feitos apareceram na aba "Plots". Os pacotes instalados em sua máquina estão listados em"Packages". As ajudas das funções aparecem em "Help". E o "Viewer" serve para visualização de páginas em HTML e JavaScript.
Essas áreas podem servistas na figura a seguir:

O RStudio

X

File £dit £ode View Plots Session fiuild Qebug Profile lools Help

O * H 1 1 * .
* Addins -

t Project |None|

z R data sets O AprovadosBB.R*
tnvironment History (Mirwbom

Source on Save * *Run "**
"* Source * -* fej *"* Import Dataset * /
list *
1 1
1 Global
Environment *

1:1 (Top levei) :
Console Terminei

RScript :

=

Copyright (c) 2018 The R Foundation for statistical Computing
Platform: x86_64-w64-mingw32/x64 (64-bit)

R is free software and comes with ABSoLUTELv No WARRANTY.
YoU are welcome to redistribute it under certain conditions.
Type 'HcenseO* or 'licenceO' for distribution details.

R is a collaborative project with many contributors.

Type 'contributorsO' for more 1nformat1on and
'citationO' on how to cite R or R packages in publications.

Type 'demoO' for some demos, 'helpO' for on-line help, or
'help. startO' for an HTML browser Interface to help.

Type 'qO' to quit R.

Nossa aula apresentará os conceitos básicos sobre o assunto que são suficientes para provas de concursos. Caso você queira se aprofundar um pouco mais no assunto e conhecer mais sobre a linguagem sugiro o seguinte curso gratuito e on-line:
https://livro.curso-r.com/

TOME

NOTA!

Acostume-se a escrever o código no Script ao invés de ficar escrevendo diretamente no console.Para começarmos a nos familiarizarmos com o RStudio, escreva o código abaixo no Script:

>1 + 1

E aperte CTRL+ENTER (CMD+ENTER no mac). Isso envia o comando para o console e o resultado é exibido logo abaixo.
> 1 + 1

[1] 2

Agora escreva o seguinte código no Script.

> # Gráfico dos números de 1 a 10

> plot(l: 10)

O primeiro comando tfGráfico dos números de 1 a 10 é, na verdade, um comentário.Comentários nos scripts do R são precedidos do símbolo #, e tudo que estiver após #
não será executado. É uma boa prática comentar seu código! Isso faz com que ele seja de fácil manutenção, tanto para você mesmo (acredite, depois de um tempo você não lembrará o que fez) quanto para seus colegas.
O segundo comando diz ao R para plotar um gráfico. Aperte CTRL+ENTER nas duas linhas.
O
gráfico aparecerá no canto inferior direito do RStudio.

Files Plots Packages Help Viewer
D

>*' Zoom S Export ' O
Publish * | (S> I

O

n 1 1 1 r

2 4 6 8 10

Index

Vamos fazer alguns exercícios para ver se você compreendeu tudo que vimos até aqui:

HORA DE

PRATICAR!

í. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

1) R é uma linguagem e um ambiente de desenvolvimento integrado, para cálculos estatísticos e gráficos.
2) Foi criada originalmente por Ross lhaka e por Robert Gentleman no departamento deEstatística da universidade de Auckland, Nova Zelândia, e foi desenvolvido por um esforço colaborativo de pessoas em vários locais do mundo.
3) 0 código fonte do R está disponível sob a licença GNU GPL e as versões binárias pré-compiladas são fornecidas para Windows, Macintosh, e muitos sistemas operacionais
Unix/Linux.

4) R é também altamente expansível com o uso dos pacotes, que são bibliotecas para funções específicas ou áreas de estudo específicas.
5) Um conjunto de pacotes é incluído com a instalação de R, com muito outros disponíveis na rede de distribuição do R (em inglês CRAN).
Comentário: A lista acima é um resumo de tudo que vimos até aqui. Todas as alternativas estão corretas, espero que você não tenha encontrado nenhum erro também.
A título de curiosidade ... o nome R provêm em parte das iniciais dos criadores e de um jogo desenvolvido com a linguagem S (da Bell Laboratories, antiga AT&T).
Gabarito: C C C C C

2) NoSSA PRIMEIRA AULA DE R

Agora que já sabemos alguns conceitos básicos sobre R e o R Studio vamos tentar organizar melhor as ideias apresentando alguns outros pontos importantes da linguagem. Se você nunca programou deixa eu conversar um pouco contigo. Vamos mudar de contexto! Qual a comida que você mais gosta? Pode ser a pizza caseira da sua tia, a dobradinha da sua mãe ou a feijoada da sua sogra ...Mas o que essas comidas tem em comum? Uma receita!!! Uma receita que estabelece os ingredientes, a quantidade e a sequência correta de ações para que seu prato predileto fique perfeito.
Agora vamos pensar no contexto computacional. O computador é uma máquina que obedece às suas instruções e se você quiser fazer com que ele faça algum cálculo ou desenhe algum gráfico, é necessário passar os comandos corretos. Esses comandos devem ser escritos em uma linguagem de computação, que pode ser compilada ou interpretada. Você deve se lembrar que R é uma linguagem INTERPRETADA.
Os dados processados pelo nosso programa precisam ser armazenados em algum lugar, numa planilha Excel ou num banco de dados. Durante o processamento, vamos trazer os dados para o nosso ambiente e armazená-los em variáveis ou símbolos. Vamos criar uma variável e associar a essa variável um valor.
> olamundo <- "Helloworld

A linha acima permite a criação de uma variável denominada olamundo, o símbolo <- é usado para atribuição, ele faz com que o valor presente do seu lado direito seja atribuído a variável do lado esquerdo. Esse valor fica disponível no ambiente e pode ser acessado. A função printÇ)pode ser usada para imprimiro valorda variável no console. Observamos o comando na listagem abaixo.
> print(olamundo)

[1] "Helloworld!"

Se você ainda não instalou o R e RStudio na sua máquina, gostaria de reforçar que a prática dos comandos vai ajudar significativamente seu aprendizado.
Ok! Já temos uma variável no nosso ambiente, mas queremos mais!! Agora vamos definirum vetor.Um vetor pode ser construído a partir da concatenação de valores do mesmo tipo. No nosso caso vamos criar um conjunto de dados numérico simples que é formado pelos números 1, 2 e4 e nomeá-
lo como x:

> x <- c (1,2,4)

Mais uma vez, temos o operador de atribuição padrão em R (<-). Você também pode usar
=, mas isso é desencorajado, pois não funciona em algumas situações especiais. Observe que não há tipos fixos associados a variáveis. Ou seja, não definimos que os valores 1, 2 e 4 são números, mas o Rentende que estamos criando um vetor numérico. Aqui, atribuímos um vetor a x. Sendo x uma variável, pode ter seu valor alterado, basta usar o símbolo de atribuição e passar outro valor válido.
O ç significa concatenar. No exemplo acima, estamos concatenando os números 1, 2 e 4.
Mais precisamente, esta mos concatenando três vetores de um elemento que consistem nesses números.Isso ocorre porque qualquer número também é considerado um vetor de um elemento.

Agora também podemos escrever o seguinte:

> q <- c (x, x, 8)

que define q como um vetor com os valores (1,2,4,1,2,4,8) (sim, incluindo os duplicados). Perceba que estamos concatenando duas vezes o conjunto de valores de x e, em seguida o 8 em um novo conjunto.
Agora vamos confirmar que os dados estão realmente em x. Para imprimir o vetor na tela, basta digitar seu nome. Se você digitar qualquer nome de variável (ou qualquer expressão)enquanto estiver no modo interativo, o R imprimirá o valor dessa variável (ou expressão) noConsole. Os programadores familiarizados com outras linguagens, como o Python, acharão esse recurso familiar. Para o nosso exemplo, insira isto:
> x

[1] 12 4

Sim, com certeza, x consiste nos números 1, 2 e 4. Outro ponto interessante é que você pode acessar elementos individuais de um vetor via colchetes "[ ]" . Veja como podemos imprimir o terceiro elemento de x:
> x [3]

[1] 4

Como em outras linguagens, o seletor (aqui, 3) é chamado de índice. Aqueles familiarizados com as linguagens da família ALGOL, como C e C++, devem observar que os elementos dos vetores Rsão indexados a partir de 1, não do 0. Outro ponto é que os subconjuntos podem ser extraídos de vetores. Veja um exemplo:
> x <- c (1,2,4)

> x [2:3]

[1] 24

A expressão x [2: 3] refere-se ao subvetor de x que consiste dos elementos nas posições 2 e 3, que são 2 e 4.
Podemos encontrarfacilmente a média e o desvio padrão do nosso conjunto de dados, da seguinte forma:
> mean(x)

W 2,333333

> sd (x)

[1] 1.527525

Isso demonstra, novamente, que a simples digitação de uma expressão no prompt
(console) é suficiente para imprimir seu resultado. Na primeira linha, nossa expressão é a função média aritmética, em inglês mean(x). O valor de retorno da chamada é impresso automaticamente, sem exigir uma chamada para a função printf) de R que apresentamos anteriormente.
Se quisermos salvar a média calculada em uma variável em vez de apenas imprimi-la na tela,poderíamos executar este código:

> y <- mean(x)

Mais uma vez, vamos confirmar que y realmente contém a média de x:

> y

[1] 2,333333

Como observado anteriormente, usamos # para escrever comentários, assim:

> y # imprime

[i] 2,333333

Os comentários são especialmente valiosos para documentar o código do programa, mas também são úteis em sessões interativas, uma vez que R registra o histórico de comandos executados. Se você salvar sua sessão e retomar mais tarde, os comentários podem ajudá-lo a lembrar o que você estava fazendo.
Por fim, vamos fazer algo com um dos conjuntos de dados internos de R. O R oferece uma lista de dados que podem ser usados para demonstrações e aprendizado. Por exemplo, a listaOrange armazena dados sobre o crescimento de algumas árvores de laranja. Você pode obter uma lista desses conjuntos de dados digitando o seguinte:
> data O

Um dos conjuntos de dados é chamado de Nile e contém dados sobre o fluxo de água do rio Nilo ao longo de íoo anos. Essa lista é uma série temporal que vai de 1870 a 1970. Vamos encontrara média e o desvio padrão desse conjunto de dados:
> mean (Nile)

W 9i9,35

> sd (Nile)

[1] 169.2275

Podemos também traçar um histograma dos dados:

> hi st (Nilo)

Se estivermos usando o RGui, uma janela aparece com o histograma, conforme mostrado na figura abaixo. Este gráfico é simples, mas R tem todos os tipos de gráficos para plotagem.Dentro de cada tipo de gráfico você pode manipular algumas das suas características, por exemplo, no histograma você pode alterar o número de categorias especificando o parâmetro. Uma chamada ao comando hi st(z, breaks=12) desenharia um histograma do conjunto de dados z com 12 caixas ou intervalos.
Você também pode criar rótulos mais agradáveis, fazer uso de cores e outras alterações para criar um gráfico mais informativo e atraente. Quando você se familiarizar mais com o R,poderá construir gráficos de cores ricas e complexas de beleza impressionante (mas isso será depois da sua aprovação), por enquanto seu foco é passar no concurso. Enquanto isso vejamos o gráfico com os dados do Nilo em uma apresentação simples.
Histogram of Nile

Nile

Figura 2 - Histograma com os dados do Nilo

Bem, esse é o final de nossa introdução de cinco minutos ao R. Saia do R chamando a função q() (ou alternativamente pressionando ctrl-D no Linux ou cmd-D em um Mac):
Rq O

Save workspace image? [y/n/c] : n

Esse último prompt pergunta se você deseja salvar suas variáveis para que você possa retomar o trabalho ma is tarde. Se você responder "y", todos esses objetos serão carregados automaticamente na próxima vez que você executar R. Esse é um recurso muito importante,especialmente ao trabalhar com conjuntos de dados grandes ou numerosos. Responder "y" aqui também salva o histórico de comandos da sessão.
Para finalizar essa sessão gostaria de falar dos comandos de ajuda. A ajuda do R
pode ser muito útil quando se deseja saber qual função utilizar ou como utilizar uma função determinada.Na tabela abaixo são listados alguns comandos para realizar buscas no R:
TOME

NOTA!

Açào de Ajuda

Procurar por "multivariate" em todos os pacotes instalados
Obter ajuda sobre o comando X

Iniciar ajuda no browser padrão instalado
Obter ajuda sobre (p.ex.) o pacote cluster

Comando que procura objetos (p.ex.) pelo nome anova
Mostrar exemplos do "comandoX"

Listar as funções e operações contidas no pacote base do R

Comando help.search("muitivariate")help(comandoX)
help.start()
help(package=cluster)
apropos("anova")
example(comandoX)

ls ("package:base")

Vejamos algumas questões sobre esses assuntos para você não avançar no conteúdo sem ter a certeza de que está aprendo tudo! ©
HORA DE

PRATICAR!

2. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos comandos da linguagem R.

1) A figura acima representa uma imagem do RGui.

2) Se utilizamos o console e escrevermos plot(Orange) o aplicativo em questão vai gerar os gráficos referentes aos dados de Orange e apresentar na área de Output, mas especificamente na aba Plots.
3) O comando abaixo vai atribuir um valor textual a variável Nome:

Nome <- "Thiago Cavalcanti tem um grupo massa no Telegram, você já conhece? Ainda não? Então, tá perdendo!"
4) Para tirar a média dos valores do conjunto de dados do datasets Nile devemos usar o comando media(Nile)
Comentário: Vamos comentar cada uma das alternativas acima. Desta vez, nem todas estavam certas. Espero que você tenha percebido! :)
1) Alternativa errada, essa é a interface do RStudio.

2) Certa! Se usarmos o plot(Orange) ele vai exibir o seguinte resultado na aba Plots:

o=

C"J

circumference o o o iTj
3) Certa. Perceba que a variável Nome possui uma letra maiúscula. Logo, se você precisar utilizá-la novamente deve respeitar essa característica, caso contrário o R não vai encontrar a variável.
4) Errada. Perceba que as funções padrão do R são em inglês, logo, para calcular a média você deve usar a função mean(Nile). Se tentarmos rodar o comando media(Nile) vamos obter a seguinte mensagem de erro:
Error in media(Ni1e) : could not find function "media"

Gabarito: E C C E

3) OBJEToS EM R

O que são os Objetos do R? Existem muitos tipos de objetos no R que só passamos a conhecê-los bem com o passar do tempo. Por enquanto vamos aprender os tipos básicos de objetos.
PRESTE MAIS

ATENÇÃO!

a) vetores: uma sequência de valores numéricos ou de caracteres (letras,
palavras)
sempre do mesmo tipo. Os vetores no R podem ser, entre outros, de tipos:

* numeric (número comum) - ex: 1,2,3;

* integer (inteiro) - ex: 2oL,IoL;

* complex (número complexo) ex.: 6 - zp;

* character (texto)-ex.: "O Estratégia é TOP";

* logical (lógicos, booleanos) ex.: TRUE, FALSE.

b) matrizes: coleção de vetores em linhas e colunas, todos os vetores dever ser do mesmo tipo (numérico ou de caracteres).
c) dataframe: O mesmo que uma matriz, mas aceita vetores de tipos diferentes(numérico e caracteres). Geralmente nós guardamos nossos dados em objetos do tipo data frame, pois sempre temos variáveis numéricas e variáveis categóricas (por exemplo,largura do rio e nome do rio, respectivamente). Similar a uma tabela do SQL, um banco de dados.
d) listas: conjunto de vetores, dataframes ou de matrizes. Não precisam ter o mesmo comprimento, é a forma que a maioria das funções retorna os resultados. Muito útil para armazenar resultados de cálculos estatísticos.
e) funções: as funções criadas para fazer diversos cálculos também são objetos do R.

f) factors (fatores): fatores são formas de representar objetos categóricos no R.

Todo objeto possui atributos intrínsecos: tipo e tamanho. Com relação ao tipo ele pode ser:numérico, caractere, complexo e lógico. Existem outros tipos, como por exemplo, funções ou expressões, porém esses não representam dados. As funções mode() e lengthQ mostram o tipo e tamanho de um objeto, respectivamente. Por exemplo:
EXEMPLIFICANDO

> x<-c(l,3,5,7,11)

> mode(x)

> length(x) #mostra o tipo e tamanho do objeto x

[i] "numeric"

[i] 5

Observamos acima a atribuição de um vetor de números a variável x. Nomes de variáveis no Rpodem conter combinações arbitrárias de números, textos, bem como ponto (.) e underscore (_).Entretanto, os nomes não podem começar com números ou underscore.

Outra forma de descobrira classe de um objeto é usando a função class().

> x <- 1

> class(x)

[1] "numeric"

> y <- "a"

> class(y)

[1] "character"

> z <- TRUE

> class(z)
El] "logical"

A tabela abaixo sintetiza os objetos e seus possíveis atributos (tipos). Veja:

Tabela 1 - Quando um objeto suporta tipos diferentes ele é chamado de heterogêneo, quando admite apenas objetos do mesmo tipo é denominado homogêneo.
Objeto Tipos
Suporta tipos diferentes vetor numérico, caractere, complexo ou lógicoNão fator numérico ou caractereNão matriz numérico, caractere, complexo ou lógicoNão array numérico, caractere, complexo ou lógicoNão dataframc numérico, caractere, complexo ou lógicoSim ts numérico, caractere, complexo ou lógicoSim lista numérico, caractere, complexo, lógico, função,expressão, etc

Sim

Saber as diferenças entre os diversos tipos de objetos é importante para um uso mais adequado do

R. Existem vários tipos de objetos que podem ser criados e manipulados. Já vimos que o R pode trabalhar com vetores - objetos que armazenam mais de um valor. A função c() é usada para criar um vetor a partir de seus argumentos. Os argumentos de c() podem ser escalares ou vetores.
Há ainda outras formas de se gerar um vetor. Por exemplo, para gerar uma sequência de números inteiros usam-se os "dois pontos". Veja:
> a<-l:10 #cria uma sequência de inteiros de 1 a 10

> a #exibe o conteúdo do objeto "a"
[1] 1 2 3 4 5 6 7 8 9 10

Uma maneira mais geral de produzir sequências de valores é usando a função seq() que tem como argumentos o início, fim e o incremento da sequência, por exemplo,, seq (1,10,1)é o mesmo que 1:10.
Outra função útil para produzir vetores é a função rep() que retorna o primeiro argumento repetido o número de vezes indicado pelo segundo argumento, o comando rep(l, 10) cria um vetor com io valores i.
UMA VIAGEM PELO R

Agora que já temos conhecimento dos objetos em R vamos conhecer um pouco mais sobre as funções. Funções são operações que pode ser executada sobre os objetos. Elas podem ser implementadas pelo próprio usuário/desenvolvedor ou serem distribuídas por meio de pacotes.Esses pacotes são interessantes para realizar diversas operações sobre os dados, desde a parte gráfica, melhorando a exibição das informações, até as funções estatísticas. Vamos falar um pouco mais sobre pacotes...
1) PACoTES

A principal forma de distribuição de códigos no R é por meio de pacotes. Um pacote pode ser entendido como um conjunto de códigos autocontido que adiciona funcionalidades ao R. Para carregar um pacote, use a função libraryQ.
Ao carregar um pacote, você está adicionando suas funções ao search da seção,
permitindo que você chame estas funções diretamente. Por exemplo, a função mvrnorm, que gera números aleatórios de uma normal multivariada, está no pacote MASS.
Vamos tentar gerar um vetor x que é representado pelo conjunto de 100 observações geradas por uma função mvrnorm. O código abaixo gera uma matriz de variância e covariância,estabelece as médias e tenta chamar a função. Mas veja que recebemos uma mensagem de erro.
> Sigma <- matrix(c(10,3,3,2),nrow=2,ncol=2) # Matriz de var-Covar

> mu <- c(l, 10) # Médias

> x <- mvrnorm(n=100, mu, Sigma) # Tenta gerar 100 obs. , mas dá erro!
Error in mvrnormfn = 100, mu, Sigma) : could not find function "mvrnorm"
## não foi possível achar a função mvrnorm

Para que a função esteja disponível é necessário carregarmos a biblioteca. Já sabemos que para isso devemos usara funçõa library().
> 1ibrary(MASS) # Carrega pacote

> x <- mvrnorm(n=100, mu, Sigma) # Agora funciona

> x

Para ver o que está disponível para utilização do R, utilize a função search(). Note que o pacoteMASS agora está lá.

> search()

El] ".GlobalEnv" "package:MASS"
E5] "package:graphics" "package:grDevices

"tools:rstudio" "package:stats"
"package:uti1s" "package:datasets

[9] "package:methods" "Autoloads" "package:base"

Para descarregar um pacote, utilize a função detach().

> detach(package:MASS)

Às vezes, você pode ter o mesmo nome de funções em pacotes distintos. Neste caso, se ambos forem carregados, a função que prevalece é a do pacote que foi carregado por último.Uma outra forma de resolver isso é usar o nome do pacote e o operador "n" antes de chamar a função e descrever o nome do pacote que você está querendo usar.. Neste caso não há ambiguidade.
> x <- MASS::mvrnorm(n=100, mu, Sigma)

Grande parte dos pacotes do R estão centralizados em um repositório chamado
CRAN (The
Comprehensive R Archive Network), com diversos espelhos ao redor do mundo. Se o pacote não estiver na sua máquina, você vai precisar baixar e instalar o mesmo. Essas ações vão deixar o pacote disponível para carregamento na sua área de trabalho. Para instalar um pacote, use a função install.
O legal é que qualquer pessoa pode fazer um novo pacote e disponibilizar para a comunidade, o que acelera bastante o desenvolvimento da ferramenta. Dificilmente você vai fazer uma análise apenas com as funções básicas do R e quase sempre vai existir um pacote com as funções que você precisa.
Existem três principais maneiras de instalar pacotes. Em ordem de frequência, são:
Via CRAN (Comprehensive R Archive Network):

> install.packages("nome-do-pacote") .

Via Github:

> devtools::instal1_gíthub("nome-do-repo/nome-do-pacote").

Via arquivo .zip/.tar.gz:

> install.packages("C:/caminho/nome-do-pacote.zip", repos =
NULL) .

Esses pacotes instalados via CRAN são pacotes de contribuições feitas por desenvolvedores da comunidade R.
2) FUNçõES Do R-BASE

Quando instalamos o R em nosso computador, programa R é composto de 3 partes básicas:

1. O R-base, o "coração" do R que contém as funções principais disponíveis quando iniciamos o programa,
2. Os pacotes recomendados (recommended packages) que são instalados junto com o R-base mas não são carregados quando iniciamos o programa. Por exemplo os pacotes MASS,lattice, nlme são pacotes recomendados - e há vários outros.

3. Os pacotes de contribuição de usuários (contributed packages) não são instalados junto com o R-base. Já vimos acima como resolver esse problema! ©
Agora queria apresentar para os senhores e as senhoras algumas funções que são bastante usadas quando estamos desenvolvendo. Vamos a elas is.xxx()
Já vimos que a função class() é útil para identificar a classe de um objeto. Mas,
muitas vezes, no meio do nosso código, queremos ter certeza de que uma variável armazena um valor de um tipo específico. Você podetestarse um vetoré de determinada classe com asfunções is.xxx(sendo "xxx"
a classe). Vejamos alguns exemplos:

> is.numeric(numero)

[1] TRUE

> is.character(numero)

[1] FALSE

> is.character(texto)

[1] TRUE

> is.logical(texto)

[1] FALSE

as.xxx()

Você pode forçar a conversão de um vetor de uma classe para outra com as funções as.xxx() (sendo"xxx" a classe). Entretanto, nem sempre essa conversão faz sentido, e pode resultar em erros ouNA's. NA significa não disponível em inglês, falaremos sobre ele mais adiante. Vamos mostrar alguns exemplos do uso das funções as.xxxQ:
> as.character(numero) # Vira texto
[1] "546.9" "10" "789"

> as.numeric(logico) # TRUE -> 1, FALSE -> 0
[1] 101

> as.numeric(texto) # Não faz sentido
Warning: NAs introduzidos por coerção

[1] NA NA NA

> as.numeric("1012312") # Faz sentido
[1] 1012312

lenght()

Para obter o tamanho de um objeto, utilize a função length(). Por exemplo:

> lenght(y)

Aproveito para inserir aqui uma nova característica da linguagem. Comandos no
R podem ser colocados na mesma linha se separados por ponto-e-vírgula (;), por exemplo.
> 1ength(ltensDoChurrascoDePosse);length(x);1engthflogico)

Para ver a estrutura de um objeto no R, use a função str(). Esta é uma função simples, mas talvez das mais úteis do R.
> str(aprovadoConcurso) #lembre-se que o objeto precisa existir no ambiente para ter sua descrição impressa no console.
plot()

O R já vem com funções básicas que fazem gráficos estatísticos de todas as naturezas.
As funções abaixo podem ser usadas para melhorar a apresentação dos dados e facilitar o entendimento das relações entre eles.
* Vantagens: são rápidas e simples.

* Desvantagens: são feias e difíceis para gerar gráficos complexos.

Nesta seção, mostraremos como construir alguns tipos de gráficos usando as funções base do R,existem outros pacotes mais robustos como o ggplot2.

Gráfico de dispersão

Para construir um gráfico de dispersão, utilizamos a função plot(). Seus principais parâmetros são:

* x, y - vetores para representarem os eixos x e y.

* type - tipo de gráfico. Pode ser pontos, linhas, escada, entre outros.
Para mais detalhes sobre os argumentos, ver help(plot).

Além de gerar gráficos de dispersão, tentar chamar a função plot(objeto_diferentao) para qualquer tipo de objeto do R geralmente gera um gráfico interessante! Sempre tente fazer isso, a menos que seu objeto seja um data.frame com milhares de colunas! Vejamos um exemplo:
> n <- 100

> x <- l:n

> y <- 5 + 2 * x + rnorm(n, sd = 30)

> plot(x, y)

Figura 3 - Gráfico de dispersão gerado pelo plot.

Se quisermos podemos inserir entre parênteses o parâmetro type = "I" indicando que desej que os pontos sejam interligados por linhas. O comando por ser visto abaixo:
> plot(x, y, type = "1")

X

Figura 4 - Gráfico de dispersão ligado por uma linho (I).

Histograma

Para construir histogramas, utilizamos a função hist(). Os principais parâmetros são:

* x - o vetor numérico para o qual o histograma será construído.

* Breaks - o número (aproximado) de retângulos.

> hist(rnorm(1000))

Histogram of rnorm(IOOO)

-2 0 2

morm(1000)

Figura 5 - Histograma de mil elementos.

Veja que se definirmos o parâmetro breaks, o nosso histograma será dividido em n barras, no exemplo abaixo temos que breaks = 6.
> hist(rnorm(1000), breaks = 6)

Histogram of rnorm(1000)

rnorm(1000)

Figura 6 - Histograma com 6 breaks

Boxplot

Para construir esse tipo de gráfico, utilizamos a função boxplot(). Os principais parâmetros são:

* X - O vetor numérico para o qual o boxplot será construído.

Vejamos um exemplo, neste exemplo usamos mais um conjunto de dados do próprio R. OInsectSprays é um data.frame que apresenta a contagem de insetos em unidades experimentais agrícolas tratadas com diferentes inseticidas. Possui duas colunas ou variáveis count e spray.Observe que o argumento col= "purple" muda a cor da caixa do boxplot.

> boxplot(lnsectSprays$count, col = "purple")

Figura 7 - Boxplot de uma variável.

Para mapear duas variáveis no gráfico, utilizamos um objeto da classe formula (~) e o argumento data=. Veja que o comando abaixo descreve para cada tipo de inseticida (A, B, C, D, E e F) a variação da quantidade de insetos contabilizados.
> boxplot(count ~ spray, data = InsectSprays, col = "blue")

A
F

Figura 8 - Gráfico de boxplot com duas variáveis.

Gráfico de barras

Para construir gráficos de barras, precisamos combinar as funções table() e barplot().
No gráfico abaixo, criamos uma tabela de frequências com a função table() e, em seguida,construímos o gráfico com a função barplot(). Lembre-se que a função data carrega bases de dados de pacotes instalados. Neste caso, como vamos usar uma base do pacote ggplot2 vamos precisar instalar o mesmo.
> install.packages("ggplot2")

> 1ibrary(ggplot2)

> data(diamonds, package = "ggplot2")

> tabela <- table(diamonds$color)

> barplot(tabela)

Figura 9 - Gráfico de barplot das quantidades x cores dos diamantes do tabela

Também podemos mapear duas variáveis a um gráfico de barras utilizando tabelas de dupla entrada. VADeaths representa o gráfico de mortes por 1000 mil habitantes na Virgínia em 1940divididos porfaixa etária, sexo e local de residência (urbana ou rural).

> VADeaths

Rural Male Rural Female Urban Male urban Female
50-54 11.7 8.7 15.4 8.4

55-59 18.1 11.7 24.3 13.6

60-64 26.9 20.3 37.0 19.3

65-69 41.0 30.9 54.6 35.1

70-74 66.0 54.3 71.1 50.0

> barplot(VADeaths)

o

CM

O

in -

o o o m o
Rural Male Rural Female Urban Male Urban Female

Figura 10 - Gráfico de barras com duas variáveis.

names()

Objetos podem ter elementos nomeados. Por exemplo, vamos nomear os elementos do vetor notas.
> notas <- c(9.5, 9.9, 10)

> notas

[1] 9.5 9.9 10.0

> names(notas) <- c('Ri cardo', 'Aline', 'Amanda')

> notas

Ricardo Aline Amanda
9.5 9.9 10.0

Quando colocamos nomes nos elementos de um vetor ou nas colunas e linhas de uma matriz, é possível acessar os dados usando esses nomes. Por exemplo:
> numero <- c(546.9, 10.0, 789.0)

> names(numero) <- c("numerol", "numero2", "numero3")

> numero["numerol"]
numerol

546.9

Outra questão interessante sobre acessar elementos de um vetor passando parâmetros entre colchetes é a possibilidade de usar números negativos, neste caso estamos recuperando o vetor sem o dado da posição especificada pelo número. Por exemplo:
> numero[-l] # todos menos o primeiro numero2 numero3
10 789

sort() e order()

A função orderQ retorna um vetor com as posições para que um objeto fique em ordem crescente.

> order(numero) #indices
[1] 3 2 1

> numero[order(numero)J # ordena numero numero3 numero2 numerol
-10.0 12.3 100.0

A função sort() retorna o vetor ordenado.

> sort(numero)

numero3 numero2 numerol

-10.0 12.3 100.0

Perceba que o resultado das duas funções acima sempre apresenta os vetores ordenados de forma crescente (do menor para o maior). As duas funções têm o parâmetro decreasing(decrescente) que,
quando TRUE, retornam o vetor de em ordem decrescente. Neste caso o código seria escrito da seguinte forma:
> sort(numero, decreasing = TRUE) # Retorna o vetor ordenado de forma decrescente.
Is() e objectsQ

Para listar todos os objetos que estão na sua área de trabalho, você pode usar a função ls() ou objects(). Faça um teste e veja se todos os objetos que você criou até aqui aparecem na lista.
rm()

A função rm(objeto) remove um objeto da área de trabalho. Ele recebe um parâmetro de texto ou uma lista com os nomes dos objetos para remover.
save.imageO e load()

Para salvar uma cópia da sua área de trabalho você pode utilizar a função save.image():

## salva a área de trabalho no arquivo "aula_linguagemR.RData"

> save.image(file=" aula_linguagemR.RData ")

Agora você pode recuperar todos os objetos com load()

> load(file=" aula_linguagemR.RData ")

summaryO

A função summaryO é uma função genérica usada para produzir resumos de resultados de várias funções. A função chama métodos específicos que dependem da classe do primeiro argumento.Vejamos um exemplo:

> medial_inear<-lm(hwy ~ displ, mpg)

> summary(medi al_i near)

Call :

lm(formula = hwy ~ displ, data = mpg)

Resi duals:

Min 1q Median 3Q Max

-7.1039 -2.1646 -0.2242 2.0589 15.0105

Coeffi ci ents:

Estimate Std . Error t value Pr(>|t|)
(Intercept) 35.6977 0.7204 49.55 <2e-16 ***

displ -3.5306 0.1945 -18.15 <2e-16 ***

Signif. codes: 0 "***' 0.001 *' 0.01 0.05 '' 0.1
Residual standard error: 3.836 on 232 degrees of freedom

Multiple R-squared: 0.5868, Adjusted R-squared: 0.585
F-statistic: 329.5 on 1 and 232 DF, p-value: < 2.2e-16

Não quero, por favor, que você se preocupe em entender os valores acima!!! Se preocupe apenas em perceber que a função summary descreve várias características do objeto mediaLinear.
Aritimética

O R tem uma série de operadores de aritmética básica e todos são vetorizados. Os operadores nada mais são do que um atalho conveniente para funções, isto é, 1+2 é a mesma coisa de '+'(1,2).Assim,
temos a lista de operadores:

* Soma (+),

* Subtração (-),

* Multiplicação (* *)

* Divisão (/)

* Exponenciação (A)

* Resto da divisão (%%)

Além dos operadores básicos, há uma série de funções matemáticas, tais como:

* abs(x) # valor absoluto

* log(x) # logaritmo

* exp(x) #exponenciação

* sqrt (x) # raiz quadrada

* factorial (x) fffatorial

* choose (10,2) #combinação

Há também diversas funções trigonométricas, como seno sin(), cosseno cos(), tangente tan() e outras.
> sin(0.5);cos(0.4);tan(3)
[1] 0.4794255

[1] 0.921061

[1] -0.1425465

Há também funções que operam com todos os valores do vetor. Por exemplo, a função sum()retorna o somatório ou a função prod() o produtório. Essas funções também têm sua versão acumulada. Vamos criar um vetor x e brincar um pouco com ele:
> x

[1] 1.0 2.0 -3.0 4.0 -20.3

> mean(x) # média
[1] -3.26

> sum(x) # somatório
[1] -16.3

> prod(x) # produtório
[1] 487.2

> cumsum(x) # somatório acumulado
[1] 1.0 3.0 0.0 4.0 -16.3

> cumprod(x) # produtório acumulado
[11 1.0 2.0 -6.0 -24.0 487.2

3) CoNSTANTES

Algumas constantes especiais estão disponíveis.

I. Lógicas: TRUE, FALSE (evite T e F)

II. Valores especiais:

Em muitos casos, o resultado de uma operação é infinito ou não determinado. Outras vezes, há valores ausentes em sua base de dados. O R tem objetos especiais para lidar com esses tipos de situação. Por exemplo, quando tiramos o log de um número negativo, obtemos como resultado o valor NaN (Not an Number). Outros valores de interesse são Inf (Infinito) e NA (NotAvailable).
Vejam uma lista de valões especiais abaixo:

Descrição Exemplo

-NaN "not a number" (o/o) ou log(-i)

-NA valor faltante (desconhecido)

-NULL valor indefinido (objeto nulo)

-Inf ou -Inf infinito (i/o, -i/o)

-Pi
3.141593...

O NA representa valores ausentes e é bastante utilizado quando se lida com bases de dados. Muitas funções têm parâmetros que indicam como ela deve lidar com valores ausentes.
III. Outras Constantes:

-LETTERS "A", "B", ..., "Z"

-letters "a", "b",..., "z"

- month.abb"Jan", "Feb","Dec"

- month.name "January", "February",..., "December"

4) MATRIZES

A ideia de matriz no R é similar a da matriz que conhecemos na matemática. Seus componentes são indexados pelo índice da linha e da coluna correspondente. Para o R, uma matriz é uma coleção de elementos de uma mesma classe arranjados em duas dimensões.
< 01,1 alh2 ' Gl,n

G2,l a2h2 a2,re

-

Ç Gm,l OT71,2 )

Figura 11 - Exemplo de uma matriz m x n

Criando matrizes

O processo de criação de uma matriz no R é relativamente simples. No exemplo a seguir, vamos criar uma matriz com 100 elementos numéricos em sequência de ia 100. Nossa matrizterá10 linhas e io colunas.
> matrizOl <- matrix(

seq(l, 100),

ncol = 10,

nrow = 10)

Percebemos que o R, por default, preenche a matriz por colunas e não por linhas. No entanto,podemos criar uma matriz preenchendo primeiro as linhas e depois as colunas. Para isso, basta definirmos o argumento byrow = TRUE. Vejamos o resultado do exemplo anterior com o preenchimento por linhas e depois por colunas.
> matrizOl <- matrix(

seq(l, 100),

ncol = 10,

nrow = 10,
byrow = TRUE)

O R trabalha com o conceito de reciclagem, onde operações ou objetos criados de um vetor,quando necessário repete os elementos do vetor. Para que haja reciclagem um dos elementos envolvidos deve ser um vetor (e.g. o outro pode ser uma matriz). Veja o exemplo:
> A <- matrix(l:10, nrow = 1);

> B <- 4:5;

> A + B;

> A * B

Operações matemáticas com matrizes

As operações com matrizes numéricas seguem praticamente a mesma lógica dos vetores. Ao realizar qualquer operação com uma constante numérica, a operação é feita para todos os elementos da matriz.
> matrizOl * 10

Já funções como meanO, sum(), sd() funcionam também como ocorre com os vetores, ou seja,levam em consideração todos os elementos da matriz. Há uma série de funções úteis para trabalharmos com matrizes, seguem algumas:
Função Descrição t() Retorna a matriz transposta diag(k) Cria uma matriz identidade kxk det() Calcula o determinante da matriz diag() Retorna os elementos da diagonal principal dim() Retorna a dimensão da matriz ncol Retorna o número de colunas da matriz nrow() Retorna o número de linhas da matriz rowSumsO Retorna a soma das linhas da matriz rowMeans() Retorna a média das linhas da matriz coISumsO Retorna a soma das colunas da matriz colMeansQ Retorna a média das colunas da matriz
Manipulando matrizes

Assim como nos vetores, podemos selecionar quaisquer elementos de uma matriz. A
diferença é que, para selecionarmos um elemento em uma matriz, devemos informarem qual linha e coluna se encontra o dado que queremos. Digamos que o elemento que desejamos obter o valor se encontra na terceira linha da quarta coluna da nossa matrizoi, criada anteriormente. A solução é a seguinte:
> matriz01[3, 4]

[1] 24

Muitas vezes não desejamos extrair o dado de apenas um elemento, mas de uma linha ou de uma coluna inteira de uma matriz. Para selecionarmos uma linha da nossa matrizoi,utilizamos o seguinte comando: matrizoi[i, ]. Onde i é a posição da linha que desejamos selecionar.Vejamos como fazemos para selecionar a linha 4 da matrizoi:
> matriz01[4, ]

[1] 31 32 33 34 35 36 37 38 39 40

Para selecionar um intervalo de linhas, a lógica é semelhante a que utilizamos para intervalos de elementos em vetores. Segue exemplo:
> matriz01[2:6, ]

[,U [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9] [,10]

[1,1 11 12 13 14 15 16 17 18 19 20

[2,1 21 22 23 24 25 26 27 28 29 30

[3,1 31 32 33 34 35 36 37 38 39 40

[4,1 41 42 43 44 45 46 47 48 49 50

[5,1 51 52 53 54 55 56 57 58 59 60

Na seleção de colunas, o R funciona de maneira igual, bastando informar qual coluna,
ou intervalo de colunas, que queremos fazer a seleção. Segue exemplo de seleção da coluna 5:
> matri z01[ ,5]

[1] 5 15 25 35 45 55 65 75 85 95

Nomeando linhas e colunas de uma matriz

Para facilitar a utilização e leitura dos dados de uma matriz, às vezes é interessante nomear suas linhas e colunas. Como exemplo, suponha que você está diante de uma matriz das notas de matemática de uma turma durante o ano de 2020. Cada linha representa um aluno e cada coluna representa um bimestre. Os dados estão estruturados conforme segue.
> notas

[1,1

[,H

[,21

[, 3]

[,4]

[2,1 9 7 4 6

[3,1 6 7 4 5

[4,1 6 7 4 7

[5,1 8 10 5 5

[6,1 8 9 9 6

[7,1 4 4 8 10

[8,1 6 8 10 5

[9,1 8 10 7 8

[10,] 8 5 9 5

Para deixar a leitura mais fácil, podemos nomear as linhas e colunas através das funções rownamesO e colnames(), respectivamente. Segue exemplo:
> colnames(notas)

> rownames(notas)
"Fernanda" , "Guste

> notas

<- cC'bim-1", "bim-2",

<- c("João", "Pedro",

ivo","Severino", "Paulo"

"bim-3",
"Amanda"

, "Laura"

"bim-4")

"Fábio",

, "Túlio")

bim-1 bim-2 bim-3 bim-4

João 5 7 5 6

Pedro 9 7 4 6

Amanda 6 7 4 5

Fábi o 6 7 4 7

Jul ia 8 10 5 5

Gustavo 8 9 9 6

Severi no 4 4 8 10

Paulo 6 8 10 5

Laura 8 10 7 8

Túl io 8 5 9 5

Uma vez com nomes das linhas e colunas, podemos utilizar os mesmos para realizarfiltros em nossa matriz. Para exibirapenas as notas da aluna Fernanda, fazemos:
> notas["Julia", ]

bim-1 bim-2 bim-3 bim-4

8 10 5 5

O procedimento para seleção das colunas segue a mesma lógica.

Unindo matrizes

A união de matrizes é bastante importante para formarmos um conjunto de dados maior a partir de dados menores. Essa união pode ocorrer de duas formas: por linhas e por colunas. Para unirmos duas matrizes através das colunas, utilizamos a função cbind(). Já para fazer a união através das linhas, usamos a função rbind().
Vamos continuar os exemplos com nossa matriz notas. No entanto, considere que, durante o ano de 2020, dois alunos foram transferidos da escola e suas notas de matemática nos dois primeiros bimestres estão armazenadas na matriz notas_transf. Vamos aos dados:
> notas_transf bim-1 bim-2 bim-3 bim-4Dimas 6 8 NA NA

Alessandra 8 9 NA NA

Para consolidar os dados, precisamos unir as matrizes notas e notas_transf por linhas. Para executartal tarefa, vamos usar a função rbind().
> rbind(notas,

notas_transf)

bi m-1 bim-2 bim-3 bim-4

João 5 7 5 6

Pedro 9 7 4 6

Amanda 6 7 4 5

Fábi o 6 7 4 7

Jul ia 8 10 5 5

Gustavo 8 9 9 6

Severi no 4 4 8 10

Paulo 6 8 10 5

Laura 8 10 7 8

Túlio 8 5 9 5

Dimas 6 8 NA NA

Alessandra 8 9 NA NA

Para unirmos duas matrizes por colunas, o procedimento é similar. Porém, temos que observar que para unir matrizes através das colunas, devemos ter o mesmo número de linhas em todas as matrizes que desejamos unir. A lógica se aplica também à união por linhas, ou seja, as matrizes envolvidas devem ter o mesmo número de colunas.
Resumindo...

cbind() é a função combina vetor, matrizes ou quadro de dados por colunas.

O

rbind() é a função combina vetor, matriz ou quadro de dados por linhas.

Uma das grandes vantagens de usar uma linguagem de programação é automatizar o seu trabalho ou análise. Você será capaz de realizar grande parte do trabalho utilizando as funções internas do Rou de pacotes de terceiros em um script. Entretanto, você ganha ainda maisflexibilidade e agilidade criando suas próprias funções. Uma função, no R, é definida da seguinte forma:
nomeDaFuncao <- function(argl, arg2, arg3 = default3, . ..){
## corpo da função: uma série de cornados válidos return(resultado) # opcional
}

* o comando function() diz para o R que você está definindo uma função.

* os valores dentro dos parênteses de function() são os argumentos (ou parâmetros)
da função. Argumentos podem ter valores de/du/t(padrão), que são definidos com o sinal de igualdade (no caso arg3 tem como default o valor default3). Existe um parâmetro "coringa" muito útil, o ..., que permite passar argumentos para outras funções.
* dentro das chaves encontra-se o "corpo" da função, isto é, uma série de comandos válidos que serão realizados.
* o comando return() encerra a função e retorna seu argumento. O
return() é opcional. Caso omitido, a função retorna o último objeto calculado.
Criemos uma função simples que retorna o quadrado de um valor passado como parâmetro:

1 I # retorna o quadrado de um número quadrado <- function(x){
xA2

}

quadrado(3)

## [1] 9

Funções criam um ambiente local e, em geral, não alteram o objeto ao qual são aplicadas. Isto é, se você passa um valor x para uma função que eleva x ao quadrado, o valor original de x não muda.Funções tomam objetos como argumentos e criam outro objeto, modificado, como resultado. Na maior parte dos casos, a ideia é que uma função no R não tenha efeitos colaterais,isto é, que ela não modifique objetos fora de seu ambiente.
6) ESTRUTURAS DE CoNTRoLE

Para escrever funções mais complexas pode ser necessário utilizarmos algumas estruturas de controle como if, ifelse e for. Vejamos algumas informações a respeito deles.
Há ocasiões em queremos ou precisamos executar parte do código apenas se alguma condição for atendida. O R fornece três opções básicas para estruturar seu código dessa maneira:if(), if() else e ifelse(). Vejamos cada uma delas.
A estrutura básica do if() é a seguinte:

if (condicao) {

## comandos que
## serão rodados

## caso condicao = TRUE

}

* O início do código se dá com o comando //seguido de parênteses e chaves;

* Dentro dos parênteses temos uma condição lógica, que deverá ter como resultado ou TRUE ou FALSE;
* Dentro das chavestemos o bloco de código que será executado se-e somente se

-a condição dos parênteses forTRUE.

A estrutura básica do if() else é a seguinte:

if (condicao) {

## comandos que
## serão rodados

## caso condicao = TRUE

} else {

## comandos que
## serão rodados

## caso condicao = FALSE

}

* O início do código se dá com o comando if seguido de parênteses e chaves;

* Dentro dos parênteses temos uma condição lógica, que deverá ter como resultado ou TRUE ou FALSE;
* Dentro das chaves do if() temos um bloco de código que será executado se-e somente se - a condição do parênteses for TRUE.
* Logo em seguida temos o else seguido de chaves;

* Dentro das chaves do else temos um bloco de código que será executado se - e somente se - a condição dos parênteses for FALSE.
Os comandos if() e if() else não são vetorizados. Uma alternativa para casos como esses é utilizar a função ifelse(). A função ifelse() tem a seguinte estrutura básica:
ifelse(vetor_de_condicoes, valor_se_TRUE, valor_se_FALSE)

* o primeiro argumento é um vetor (ou uma expressão que retorna um vetor) com vários TRUEe FALSE;
* o segundo argumento é o valor que será retornado quando o elemento do vetor_de_condicoes forTRUE;
* o terceiro argumento é o valor que será retornado quando o elemento do vetor_de_condicoes for FALSE.
Minha experiência com programação tem demonstrado que usar funções que operam sobre vetores ou matrizes é muito mais performático do que usar outras funções não vetorizadas.
Laços com for (repetições)

Frequentemente, precisamos executar uma sequência de comandos um certo número de vezes.
O
conjunto de comandos é executado uma vez e, em seguida, o fluxo de execução retorna ao primeiro comando do conjunto e o processo continua um certo número de vezes. Esta estrutura de repetições de uma sequência de comandos é chamada de laço (em inglês loop). Cada uma das repetições é chamada de iteração.
Suponhamos você queira somar os elementos de um vetor numérico e não tivéssemos a função sum() à nossa disposição. Um maneira de realizar esta soma no R é usar uma estrutura como no exemplo abaixo:
x = c(l:10, 21:30)

soma = 0

for (i in l:length(x)) {

soma = soma + x[i]

}

soma

## [1] 310

Os laços formados com a palavra-chave/or executam os comandos entre chaves quantas vezes a expressão entre parênteses especificar. No exemplo acima, o comando soma = soma +x[ij vai ser executado para cada valor de i, que assume em sequência os valores de i até o comprimento do vetorx. Assim, a variável soma vai adicionando sucessivamente os valores do vetorx.
Existe uma função chamada seq_len() que substitui a expressão i:length(). Então laço for acima poderia ser escrito como:
for (i in seq_len(x)) {
soma = soma + x[i]

}

Laços aninhados

Laços podem ser aninhamos quantas vezes forem necessárias, embora, normalmente, mais de três níveis de aninhamento seja raramente necessário.
O código abaixo calcula a soma dos elementos de uma matriz, onde no laço externo, i percorre as linhas da matriz, e, no laço interno, j percorre as colunas da matriz.
Inicialmente i - 1 e j assume o valor 1. O laço interno é executado para cada valor de j, que assume sucessivamente os valores de 1 a 5. No laço interno, a variável soma vai adicionando os respectivos valores de x[i,j], Quando j chegar a 5, o fluxo retorna para o laço mais externo, i é incrementado de uma unidade e o fluxo retorna para o laço interno, onde j novamente assume os valores de 1 a 5. Asequência de iterações se encerra quando i chega à última linha e j percorre as colunas da matriz.

x <- matrix(ll:35, 3, 5)

## Warning in matrix(ll:35, 3, 5): comprimento dos dados [25] não é um submúltiplo
## ou múltiplo do número de linhas [3]

soma = 0

for(i in seq_len(nrow(x))) {
for(j in seq_len(ncol(x))) {

soma = soma + x[i,j]

}

}

soma

## [1] 270

laços com while

Laços do tipo while possuem a seguinte estrutura:

while ( expressão lógica ) { * sequência de comandos }*

Inicialmente a expressão lógica é avaliada. Se ela for verdadeira, a sequência de comandos entre chaves é executada. Em seguida a expressão lógica é novamente avaliada e, assim por diante, até que a expressão lógica seja falsa e então o fluxo de execução sai do laço.
Vamos reescrever o código para calcular a soma dos elementos de um vetor numérico utilizando o laço com while. Observe a expressão lógica /<= length(x) que é testada a cada iteração. Inicialmente i é igual a 1 e é incrementado em uma unidade a cada iteração. Quando i atinge o valor igual ao comprimento de x, o laço é interrompido.
x = c(l:10, 21:30)

soma - 0

i = 1

while (i <= length(x)) {

soma - soma + x[i]

i = i + 1

}

soma

## [1] 310

No exemplo, o laço com for é mais simples. Em laços com while, é preciso tomar cuidado para que a expressão lógica não seja sempre verdadeira. Caso a expressão lógica nunca se torne falsa, o laço nunca terminará. Esse tipo de situação é conhecido como loop infinito.
laços com repeat e break

Um laço com repeat no R é executado sucessivas vezes até ser interrompido pelo comando break.

Vamos novamente reescrever o código para calcular a soma dos elementos de um vetor numérico utilizando agora o laço com repeat. Inicialmente i é igual a i e é aumentado de uma unidade a cada iteração. Quando i atinge o valor igual ao comprimento de x,a condição / >
length(x) é verdadeira e o comando break é executado, interrompendo o laço.

x = c(l:10, 21:30)

soma = 0

i = 1

repeat{

soma = soma + x[i]
i = i + 1

if (i > length(x)) {
break

}

}

soma

## [1] 310

O comando break, como o nome indica, interrompe a execução de um loop sempre que for executado.
next

O comando next é usado para pular uma iteração de um laço.

Vamos supor que desejamos somar somente os elementos a partir do décimo-primeiro. O
código deveria ser alterado como abaixo:
x = c(l:10, 21:30)

soma - 0

for (i in l:length(x)) {
if (i < 11) {

next

}

soma - soma + x[i]

}

soma

## [1] 255

RESUMo

Nesta aula, aprendemos que R é uma linguagem de programação multi-paradigma
(funcional e orientada a objetos), dinâmica, fortemente tipada, voltada à manipulação, análise e visualização de dados. O código fonte do R está disponível sob a licença GNU GPL (software livre) e as versões binárias pré-compiladas são fornecidas para Windows, Macintosh, e muitos sistemas operacionaisUnix/Linux.

A linguagem R disponibiliza uma ampla variedade de técnicas estatísticas e gráficas,
incluindo modelação linear e não linear, testes estatísticos clássicos, análise de séries temporais (time-series analysis), classificação, agrupamento e outras. R é facilmente extensível através de funções e extensões, e a comunidade R é reconhecida pelas contribuições feitas por meio de pacotes.
A R é uma linguagem interpretada tipicamente utilizada através de um Interpretadorde comandos.Como muitas outras linguagens, a R suporta matrizes aritméticas. A estrutura de dados da R inclui escalares, vetores, matrizes, dataframes (similares a tabelas numa base de dados relacional) e listas. O sistema de objetos da R é extensível e inclui objetos para, entre outros,modelos de regressão, séries temporais e coordenadas geoespaciais.
Mais uma vantagem de utilizar a linguagem R está no RStudio, que é uma IDE, ou ambiente de desenvolvimento integrado, para o R. Com sua utilização gratuita, o RStudio é uma excelente ferramenta para desenvolvimento em R, extremamente visual quando comparado com ambientes de outras linguagens e também com o console do R, e muito simples de se utilizar.
Ao longo da aula, mostramos vários comandos e apresentamos suas respectivas descrições e sintaxe. Abaixo vamos fazer um resumo destes comandos separados por categoria:
PEDINDO AJUDA e COMPREENDENDO OBJETOS

Comando I Descrição help(tópico)str("tópico")

summary(a)

ls()
dir("diretório")

Documentação do tópico, que pode ser uma função ou um objeto.
Mostra a estrutura do tópico no R

Mostra o resumo de 'a'. Geralmente um resumo estatístico. Mas há diferentes operações para diferentes classes de 'a'.
lista os objetos criados no console.
lista arquivos de determinado diretório.

IMPORTANDO E EXPORTANDO

Comando Descrição load(): carrega datasets(dados) escritos com save data(x) carrega dados específicos library(x) carrega um pacote de dados.
read.ta ble(file)

lê um arquivo no formato de tabela e cria a partir dele um dataframe; O
separador padrão sep="" é qualquer espaço em branco; use header=TRUE para ler a primeira linha como cabeçalho das colunas.
save(arquivo,...) salva o objeto especificado na plataforma binária printfa,...) mostra a saída no console do objeto 'a'.
CRIANDO DADO

Comando Descrição c(-)
pode se entender c de combinar. É uma função genérica que combina os argumentos em um vetor.
frormto gera uma sequência. Os dois pontos (:) tem a prioridade na operação.Exemplo: 1:4+1, a saída no console é "2,3,4,5".

gera uma sequência. Possui os seguintes parâmentros, by=específica o incremento. Iength=específica o tamanho desejado da sequência.Perceba que by e lenght não podem ser usados como argumentos ao mesmo tempo. Ex:
ˢᵉq⁽ᶠʳᵒᵐ,ᵗᵒ⁾ > seq(l,10, by= 2)
[1] 1 3 5 7 9

> seq(l,4, length = 5)

[1] 1.00 1.75 2.50 3.25 4.00

repete x vezes; use each=para repetir cada elemento x vezes.
Exemplos:

rep(x,times) > rep(c(l,2,3),2)
[1] 1 2 3 1 2 3

> rep(c(l,2,3),2, each = 2)
[1] 1 1 2 2 3 3 1 1 2 2 3 3

data.frameO cria um data frame com os argumentos, nomeados ou não.

listo cria uma lista com os argumentos matrix(x,nrow=,ncol=)
cria uma matrix; com nrow=número de linhas e ncol=número de colunas.
Elementos menores serão reciclados.

rbind(...)

combina os argumentos por linhas em uma matriz, data frame e entre outros.
cbind(...)

combina os argumentos por colunas em uma matriz, data frame e entre outros.
FRAGMENTANDO E EXTRAINDO DADOS

Em vetores podemos ter acesso elementos específicos, vejamos algumas opções

Comando Descrição x[n] Seleciona o elemento presente no n índice do vetorx x[-n] Seleciona todos os elementos do vetorx, exceto o elemento n x[i:n] Seleciona os primeiros n elementos do vetorx x[c(i,3,5)l
Seleciona os elementos do vetor x nas posições especificadas, neste caso, i,3 e 5.
x["nome"] Seleciona o elemento do vetorx, pelo nome indicado.

Seleciona todos os elementos do vetor x maiores que 3, vejamos um exemplo:
x[x>3] x[x>l]

[1] 2.549633 5.888932 4.145929 1.332829 4.538

487 4.140993 4.745690 2.988220

PLOTANDO GRÁFICOS

Comando Descrição plot(a)
Cria um gráfico com os valores de a no eixo y e no eixo x a sua respectiva posição.
plot(a,b)

Cria um gráfico em que os valores de a estarão no eixo x e os valores de b no eixo y.
cria um histograma de frequência de x.

Histogramas hist(x)
cria um histograma com os valores de x; use horiz=TRUE para criar barras horizontais.
Maximum Temperatures in a Week barplot(x)
Degree Celsius pie(x)
cria um gráfico de setores (o famoso gráfico de pizza).

Pie Chart of Countries

Australia cria um gráfico do tipo box-plot.
n = 8

CO

boxplot(x)

C0

n * 20

B C D

EXERCÍCIoS

1) QUESTõES E EXERCÍCIo PRÁTICo - BAIXE o R E R STUDIO!

Como não temos muitas questões sobre R para alegrar nossa aula e abrilhantar nosso estudo,resolvemos ressuscitar uma banca histórica de concurso público conhecida como
TRC. Criativa,
inteligente, dinâmica e objetiva a banca vai focar nos principais pontos do assunto com questões.

HORA DE

PRATICAR!

í. CEBRASPE (CESPE) - Analista de Previdência Complementar (FUNPRESP-
EXE)/lnvestimentos/2O22

A respeito de estatística e da linguagem de programação R, julgue o item a seguir.

No programa R, a função aritmética básica (2+2)A2=16 pode ser calculada digitando-se > 2+2 A
2.

Comentário: A linguagem R é uma linguagem de programação considerada científica com foco em estatística, portanto operações matemáticas de variadas formas são possíveis de se fazer.Quando há operações matemáticas vamos utilizar, portanto, os operadores aritméticos. Os mais comuns em R são:
+ -> somar

- -> subtrair

/ -> dividir

* -> multiplicar

A -> elevar à uma potência.

Da mesma forma que na aritmética básica, a linguagem segue uma ordem de precedência entre os operadores. Logo, ao digitar 2 + 2A2, primeiramente será calculado a exponenciação para, em seguida, executar a soma, dando o resultado de 6. Por isso, a alternativa está incorreta.
Vejam os comentários com a ordem de precedência dos operadores da linguagem:

:: ::: access variables in a namespace

$ @ component / slot extraction
[ [[ indexing

A exponentiation (right to left)

- + unary minus and plus

: sequence operator

%any% special operators (including %% and %/%)

* / multiply, divide

+ - (binary) add, subtract

<><=>= == != ordering and comparison

! negation
& && and
I II or

~ as in formulae

->-» rightwards assignment

<-«- assignment (right to left)

= assignment (right to left)

? help (unary and binary)

Gabarito: E

2. CEBRASPE (CESPE) - Analista de Previdência Complementar (FUNPRESP-
EXE)/lnvestimentos/2O22

A respeito de estatística e da linguagem de programação R, julgue o item a seguir.

No programa R, o comando > sample (1:60, 6) fornece os seis números aleatórios para um jogo na Mega Sena.
Comentário: A função do R usada na questão denominada sample possui os seguintes parâmetros:
sample (x, size, replace) em que x é o conjunto de dados da amostra. Ele também pode aparecer com limite inferior e superior,por exemplo x:y.lsso significa que temos uma sequência de número que vai de x até y.

size representa a quantidade de amostras que queremos.

replace é utilizado para indicar se vamos ter reposição (true) do dado retirado ou não
(false). Caso ele não seja especificado, o padrão é FALSE.

Sendo assim, ao digitar sample (1:60, 6), vamos escolher 6 números de um jogo da mega sena.

Gabarito: C

3. FGV-Auditor Federal de Controle Externo (TCU)/Controle Externo/Auditoria
Governamental/2022

A tabela presente no código em R abaixo apresenta a quantidade de processos analisados por três analistas (denotados por Al, A2 e A3) em diferentes anos.
dados = tibble: :tibble(

Analista=c("Al", "Al", "Al", "A2","A2", "A3", "A3", "A3"),
Ano=c(2018,2019,2020,2019,2020,2018,2019,2020),
Processos=c(10,15,20,25,20,8,7,12))

Um programador roda o código abaixo em R.

tidyr::pivot_wider(data=dados, names_from="Analista", values_from="Processos")
Os valores esperados na primeira linha do objeto resultante do comando acima são:
A 2018, 10, NA, 8;

B Al, 10, 15, 20;

CAI, 2018, 10;

D 2018, 18;

E A2, 2019, 25.

Comentário: Vamos analisar a questão:

dados = tibble::tibble(Analista=c("Al", "Al", "Al", "A2", "A2", "A3", "A3", "A3"),
Ano=c(2018,2019,2020,2019,2020,2018,2019,2020),
Processos=c(10,15,20,25,20,8,7,12))

No trecho de código acima, foi criada uma variável chamada dados para receber um data frame com o nome de analistas, o ano e a quantidade de processos que cada um executou.Os data frames, por sua vez, foram criados utilizando Tibbles, que permite que os resultados sejam mais agradáveis ao analisar.
É como se o Tibble construísse uma tabela visualmente mais organizada colocando cada informação sobre o seu referente.
tidyr::pivot_wider(data=dados, names_from="Analista", values_from="Processos")

No código acima temos a apresentação dos dados, os quais foram organizados pelo Tibble.
Aqui, estamos criando uma tabela para organizar os dados com a função pivot_wider. Essa função agrupa os dados em colunas com incorporando diversos valores para cada registro.
Ao executar o código acima, temos o seguinte resultado:

## A tibble: : 3 x 4

Ano Al A2 A3

<db7> <cA

t>7<>£77? 7>

<db 7>

1 2018 10 NA 8

"7 2019 15 25 7

3 2020 20 20 12

Obs. Na primeira linha aparece a notação NA, pois não há ocorrências de processos para A2 no ano de 2018. Perceba, portanto, a lógica do agrupamento, cada célula corresponde a guantidade de processos por ano.
Com a tabela acima, podemos ver, de forma mais clara, que o Analista:
Al teve 10 processos em 2018, 15 em 2019 e 20 em 2020.

A2 não teve processos em 2018, teve 25 em 2019 e 20 em 2020

A3 teve 8 processos em 2018, 7 em 2019 e 12 em 2020.

A visualização acima foi possível pois o Tibble criou o dataframe, organizando as informações,e a função pivot_winder os mostrou em uma tabela organizada e bonita visualmente.

Os valores esperados na primeira linha do objeto resultante do comando acima são: 2018,
10, NA, 8. Logo, temos a nossa resposta na alternativa A.

Gabarito: A.

Zf. CEBRASPE (CESPE) - Estatístico (FUB)/2022

R R CoHíüle ! ° 11 s Ikad

JB raquire (cldyvtr»)

idade <- c( 20, 30, Rkr 30 r 40f 50)
altura <- c<l. 6,1.7,1.5,1.8,1-7,1.7)

dadoa <- data.frame(1dade r altura J
dados idade alrura
1 20 1.6

2 30 1.7

3 Nh 1. S

4 30 1.8

5 40 1.7

€ 50 1.7

|

►

Considerando que um usuário inicie uma sessão R escrevendo um código na janela R
Console conforme mostra a figura apresentada, julgue o item subsequente.
Os códigos dados %>% na.omit() e dados %>% drop_na() proporcionam o mesmo resultado.

Comentário: Na questão, temos uma tabela de dados com informações desconhecidas, ou perdidas. Por vezes queremos exibir nossas tabelas sem essas informações e procurá-las para eliminar manualmente pode ser um trabalho dolorido.
Pensando nisso temos algumas funções que nos permitem fazer esse trabalho e imprimir uma tabela sem nenhum dado desconhecido.
Uma dessas funções é conhecida como na.omit(). Ao utilizá-la vamos omitir todos os casos considerados desnecessários, ou seja, vamos retirar do nosso resultado todos os valores NA.
Outra função que faz algo parecido é a função drop_na(). Ela elimina as linhas que contém NAno conjunto de dados.

A diferença entre as duas funções é a que a primeira apenas omite a linha, a segunda apaga a linha. Veja abaixo os resultados, porém com a numeração das linhas.
> dados

1 dade altura

1 20 1. 5

2 30 1.7

3 NA 1. 5

4 30 1.8

5 40 1.7

6 50 1.7

> dados
1 dade altura na.omit
1 20 1. 5

2 30 1.7

4 30 1.8

5 40 1.7

6 50 1.7

> dados
1 dade

%>% drop_na al tura
1 20 1. 5

2 30 1.7

3 30 1.8

4 40 1.7

5 50 1.7

Perceba que quando utilizamos a função na.omit() saltamos da linha 2 para a linha 4.
Já ao utilizar a função drop_na() reagrupamos as linhas após a exclusão da linha que continha o NA.Portanto, temos um item correto.

Gabarito: C

5. CEBRASPE (CESPE) - Estatístico (FUB)/2022

RR Console _<

> require(tidyverse)

> * <" c(O, 2f3,4f 5)

> V <* C(5.4,6, 4,7. 5)

> z <- c ("a", "b", "b", na"r "a")

> gr af <*- data . f rame (x, yr z)

> I

w

Considerando o código mostrado na figura apresentada, julgue o próximo item.

A figura a seguir é obtida mediante aplicação do seguinte código R:
ggplot(data=graf,mapping=aes(x=x, y=y))+

geom_line()+
geom_point()+
xlab("x")+

ylab("y")

Comentário: Se executarmos o código acima, vamos obter a seguinte figura:

0 1 2
3 4

X

Perceba que falta incluir os círculos e triângulos que representam os tipos ( ou eixo z) dos elementos. Para obtermos o resultado informado pela questão devemos utilizar o código:
ggplot(data=graf, mapping=aes(x=x,y=y))+
geom_line()+

geom_point(shape = factor(z),size=4)+
geom_smooth(aes(group=z))+

xlab("x")+

ylab("y")

Logo, temos uma alternativa incorreta.

Gabarito: E.

6. FGV - Analista Judiciário (TJDFT)/Apoio Especializado/Estatística/2022

Utilizando a Linguagem R tem-se um objeto x como consta a seguir.
x

## [1] 1 3 4 3 4 <NA>

## Leveis: 13 4
is.factor(x)

## [1] TRUE

0 comando que resulta na soma dos elementos numéricos de x é:

A sum(as.numeric(as.character(x)), na.rm = TRUE);
B sum(x);

C sum(as.numeric(x), na.rm = TRUE);
D sum(as.numeric(x), na.rm = FALSE);
E sum(x[-5]).

Comentário: Essa questão tem uma pegadinha ... e muitos alunos me mandam dúvidas sobre ela ... vejam que x é uma factor, portanto, ela terá elementos e todos esses elementos pertencerão a um conjunto descrito pelos níveis (Leveis). Neste caso, temos 1, 3 e 4.
Agora vamos executar as alternativas A e C ... que são a fonte de toda discórdia no nosso fórum.
sum(as.numeric(as.character(x)), na.rm =TRUE)

[1] 15

sum(as.numeric(x), na.rm = TRUE)
[1] 11

Mas por que isso acontece? Vamos por partes ... se eu executo o código as.numeric(x),
eu obtenho os seguintes valores:
[1] 1 2 3 2 3

Veja que ele mostra o nível (posição) de cada um dos valores da factor. Por isso,
precisamos transformar a factor em caracteres primeiro, pois o código as.character(x), nos mostra os seguinte resultado:
0 0

Agora sim, podemos transformar a lista acima em número e somá-los para obter o valore
16.
Sendo assim, nossa resposta encontra-se na alternativa A.

Gabarito: A

7. FGV - Analista (MPE SC)/Dados e Pesquisas/2022

No contexto da linguagem de programação R, analise o código a seguir.
for (x in 1:10) {

if (x >= 4) {
print(x)
next}

if (x == 8) {break}

}

O número de linhas exibidas pela execução desse código é:

A 6;

B7;

0 8;

D 9;

E 10.

Comentário: A questão trata de um código em R, linguagem muito utilizada para realizar trabalho com muitos dados. Nesse sentido, o código define um intervalo para x que varia de 1até 10 na primeira linha. Logo após, temos uma condição if. O valor de print só irá ser exibido se passarmos por essa condição, vejamos:
if (x >= 4) {// se x for maior que 4
print(x)// saída de x será de 4 até 10

next} // passa para execução do próximo item do laço.
if (x == 8) {break} // nunca será executado!

Com isso, teremos 7 linhas. Uma para cada número de 4 até 10. Logo, a resposta encontra-se na alternativa B.
Gabarito: B

8. FGV - Analista (MPE SC)/Dados e Pesquisas/2022

Analise o código da linguagem de programação R a seguir.

xpto <- array(c(l:24), dim = c(4, 3, 2))
print (xpto[3, 2, 1])

Na execução desse código, o print produz o valor:
A5

B 7

C 10

D 18

E 19

Comentário: Ao executar o código acima, temos o seguinte resultado.

R R Console xpto - array(c(1:24), dim=c (4,3,2) )
> xpto r , 1
LU [z2] L3]

[1,1 1 5 9

[2,] 2 6 10

[3,] 3 Q 11

[4,] 4 8 12

, , 2

LU L2] L3]

[1,1 13 17 21

[2,] 14 18 22

[3,] 15 19 23

[4,1 16 20 24

>

Veja que temos 4 LINHAS, 3 COLUNAS e 2 MATRIZES.

Logo, a posição 3, 2,1, está na terceira linha e na segunda coluna da matriz 1.

Gabarito: B

9. FGV - Analista (MPE SC)/Dados e Pesquisas/2022

No contexto da linguagem de programação R, analise as afirmativas a seguir.

I. Vetores (vectors) são listas de itens que devem ter o mesmo tipo.

II. R trabalha com vários tipos de dados (data types), numéricos, lógicos e textuais,
mas as variáveis podem mudar de tipo mesmo depois da instanciação.
III. Os itens de uma lista (list) não podem ser substituídos. São permitidas apenas a inserção e a remoção de itens.
Está correto somente o que se afirma em:

Al;
B II;

C III;

D I e II;
E II e III.

Comentário: A questão trata da linguagem de programação R e pede que se assinale a assertiva correta quanto aos conceitos:
I. Correta. Os vetores de fato são listas que contém o mesmo tipo, como string,
inteiros,
complexos, entre outros. São muito importantes, pois são explorados nos cálculos,principalmente na estátistica, um dos principais usos dessa linguagem.

II. Correta. De fato, mesmo após a instanciação, elas podem ser substituídas.

III. Errada. É possível utilizar a função replace para fazer essa tarefa de substituição, portanto,não é só a remoção e inserção de itens.

Portanto, I e II são corretas.

I

J

Gabarito: D

10. IBFC - Supervisor de Pesquisas (IBGE)/Suporte Gerencial/2021

Função da linguagem de programação R que permite fazer gráficos de dispersão. De acordo com a descrição, a função é:
A head
B plot

C grafhic

D dispersion
E mean

Comentário: Existem algumas funções para criação de gráficos em R e plot é uma delas. Logo,
temos a resposta na alternativa B.

Gabarito: B

11. CEBRASPE (CESPE) - Agente de Polícia Federal/2021 (e mais 2 concursos)
Com relação a conceitos de programação Python e R, julgue o item que se seguem.
O resultado do código R seguinte será "12".

f<- function(x) {

g <- function(y) {

y + z

}

z <- 4

x + g(x)

}

z <-10
f(4)

Comentário: Essa questão não é trivial ... você precisa acompanhar a execução para entender o que está acontecendo. Vamos a um passo a passo:
1. Primeiramente o valor 4 é passado como parâmetro para a função f.

2. Dentro dessa função temos a definição da função g e, em seguida, um código que chama a função g passando x —> g(x).
3. Antes, porém, é definido o valor de z para o contexto, z <-4.

4. Assim, entramos na função g com o valor de y = 4 e de z = 4, o que nos retorna o valor 8.

5. Então, somamos ao valor 8 obtido por g(x) o valor 4 que é o valor de x ... obtendo 12.

A resposta pergunta se o valor "12" é retornado. Na realidade o valor retornado não deveria aparecer entre aspas por se tratar de um número. A linguagem R não delimita números com aspas. Entretanto, o examinador considerou que, se seguir a norma culta da língua portuguesa o valor deveria, de fato, aparecer entre aspas no enunciado.
Gabarito: Certo

12.CEBRASPE (CESPE) - Técnico Bancário III (BANESE)/lnfomnática/Desenvolvimento/202i

Com respeito ao pacote reticulate da linguagem R, que propicia uma interface com os módulos,classes e funções do Python, julgue o item a seguir

O código seguinte permite importar o módulo math para utilização no ambiente R.
library(reticulate)

math <- use_python("math")

Comentário: O pacote reticulate, realmente, fornece uma interface R para módulos, classes e funções do Python. O erro acima está no fato de que não é use_python o método que deve ser usado aí para importar, e sim o método import. O correto seria:
math <- import("math")

Logo, temos uma alternativa errada!

Gabarito: Errado

13. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
As funcionalidades do R são divididas em vários pacotes.

Comentário: A funcionalidade R é dividida em vários pacotes. O
sistema R possui pacotes básicos e recomendados. O CRAN também hospeda muitos pacotes complementares que podem ser usados para estender a funcionalidade do R.
Gabarito: C

14. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

O sistema base R contém, entre outras coisas, o pacote base necessário para executar o R e contém as funções mais fundamentais.
Comentário: A funcionalidade R é dividida em vários pacotes. O pacote "base"
no R contém as funções mais fundamentais.
Gabarito: C

15. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

Os pacotes utils, lang e tools são considerados pacotes básicos do R.

Comentário: O sistema R "base" contém, entre outras coisas, o pacote base necessário para executar o R e contém as funções mais fundamentais. Os outros pacotes contidos no sistema"base" incluem utils, stats, datasets, graphics, grDevices, grid,
methods, tools, parallel,
compiler, splines, tcltk, and stats4. Veja que lang não faz parte dos pacotes básicos.

Gabarito: E

16.Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
A função abaixo pula as primeiras 20 iterações do loop.

for(i in 1:100)
if(i <= 20) {

next

}

print(i)

}

Comentário: O comando next pula para a próxima iteração loop.

Gabarito: C

17. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

O resultado da função abaixo é 5
x <-3

switch(x, 2+2, mean(l:10), rnorm(5))

Comentário: Na função switch(valor, lista, ...), se o primeiro parâmetro for um número entre 1e o comprimento da lista, o elemento correspondente da lista será avaliado e o resultado retornado. Aqui, valor é um número (3), portanto, o terceiro valor é obtido da lista de valores,que é rnorm (5). A saída para rnorm (5) será impressa.

> x <- 3

> switch(x, 2+2, mean(l:10), rnorm(5))

[1] 0.2363995 0.1745040-2.7320329 0.1886224 -0.2821843

Se o valor numérico estiver fora do intervalo (maior que o número de itens na lista ou menor que 1), NULL será retornado. Vejamos alguns exemplos:
> switch(2,"red","green","blue")

[1] "green"

>switch(l,"red","green","blue")
[1]"red"

> switch(4,"red","green","blue")
NULL

> switch(0,"red","green","blue")
NULL

Gabarito: E.

18.Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
next é usado para pular uma iteração dentro do loop.

Comentário: Em construções de loop como while, repeat, e podemos usar next para pular para a próxima iteração. Vejamos um exemplo:
x <-1:5

for (vai in x) {
if (vai == 3){

next

}

print(val)

}
[1]1

[1]2

[1]4

[1] 5

Gabarito: C

19. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

Uma instrução break é usada dentro de um loop (repaet, for, while) para interromper as iterações e fazer fluir o controle para fora do loop.
Comentário: O break é usado para sair de um loop imediatamente, independentemente de qual iteração o loop possa estar. Vejamos um exemplo:
x<-1:5

for (vai in x) {
if (vai == 3){
break

}

print(val)

}
[1]1

[1]2

Gabarito: C

20. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

break e next são duas estruturas de controle para controlar explicitamente o loop.

Comentário: Existem duas instruções que podem ser usadas para controlar explicitamente looping, break e next.
Gabarito: C

21. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
Escrever funções é uma atividade secundária de um programador R.

Comentário: Escrever funções é uma atividade principal de um programador R.
As funções são frequentemente usadas para encapsular uma sequência de expressões que precisam ser executadas várias vezes.
Gabarito: E

22. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

As funções são definidas usando a diretiva function() e são armazenadas como objetos R.

Comentário: As funções são criadas usando a diretiva function() e são armazenadas como objetos R, assim como todos os outros elementos de R. Em suma, são objetos R da classe"function".

Gabarito: C

23. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

A função graph() é usada para plotagem de gráficos no R base.

Comentário: plot () é uma função genérica para plotagem de objetos
R. Para gráficos de dispersão simples, o plot será usado. No entanto, existem métodos de plotagem para muitos objetos R, incluindo funções, data.frames, objetos de densidade, etc.
Gabarito: E

24. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

A função names() lista nomes das variáveis em um data.frame.

Comentário: names é uma função assessora genérica para lista o nome das variáveis. Os métodos padrão obtêm e definem o atributo "names" de um vetor(incluindo uma lista) ou pairlist.
Gabarito: C

25. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
x <- c(l, 2, NA, 4, NA, 5)

deuruim <- is.na(x)
print(deuruim)

O resultado do código acima é:

FALSE FALSE TRUE FALSE TRUE FALSE

Comentário: Uma tarefa comum na análise de dados é remover valores ausentes
(NAs). is.na()
retornará TRUE se o elemento for NA, caso contrário, retornará false. Aqui,
o vetor x contém dois valores NAs no terceiro e quinto índice.
Portanto, ele exibirá no console:

FALSE FALSE TRUE FALSE TRUE FALSE

Gabarito: C

26.Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

O pacote dplyr pode ser instalado a partir do CRAN, usando library("dplyr").

Comentário: Você pode instalar pacotes R disponíveis nos repositórios online usando install.packages e carregá-los. O código correto seria:
install.packages ("dplyr")

Gabarito: E

27. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
Arquivos contendo scripts R terminam com a extensão .R

Comentário: Os arquivos que contêm scripts R têm uma extensão ".R".

Gabarito: C

28.Ano: 2018 Banca: CESPE Assunto: Informática para Polícia Federal Cargo: Agente
Conteúdo: Linguagem R

Julgue os próximos itens, relativos a noções de programação Python e R.
93 Considere o programa a seguir, escrito em R.

x <- c (3, 5, 7)

y <- c (1, 9,11)

print (x + y)

Após a execução do programa, será obtido o seguinte resultado.
W36

94 Considere o programa a seguir, escrito em R.
x<-TRUE

y<-FALSE

print (xy)

Após a execução do programa, será obtido o seguinte resultado.

[i] FALSE

Comentário: Vamos comentar as alternativas acima.

93. Neste caso temos 2 vetores com 3 elementos cada um. A operação x + y vai fazer o somatório dos de cada um dos termos. Veja o código abaixo:
> x <- c (3, 5, 7)

| > y <- c Cl, 9, 11)

> print (x + y)
[1] 4 14 18

Neste caso o valor retornado pela função print vai retornar como resultado o vetor 4,14 e 18.
Logo, a alternativa está incorreta.

94. Nesta alternativa atribuímos valores booleanos as variáveis x e y. Em seguida, pedimos para imprimir o atributo xy, que não existe no sistema. Isso retornar um erro conforme visto abaixo.
> x <- TRUE

> y <- FALSE

> print (xy)

Error in print(xy): object 'xy' not found
Logo, temos mais uma alternativa errada.

Gabarito: 93. E 94. E

29.Ano: 2018 Prova: Perito - Polícia Federal Banca: CESPE Assunto: Conhecimentos básicos -
banco de dados e teoria da informação.

Com relação à programação Python e R, julgue os itens que se seguem.

43 Considere os comandos a seguir, na linguagem R, os quais serão executados no ambiente do R, e considere, ainda, que > seja um símbolo desse ambiente.
> helloStr <- "Hello world!"

> print(helloStr)

Nesse caso, após a execução dos comandos, será obtido o resultado a seguir.

[1] "Hello world!"

Comentário: Vamos comentar cada uma das afirmações acima.

Neste caso os comandos vão de fato fazer o que está descrito.
Primeiramente, vamos atribuir a uma variável helloStr um conjunto de caracteres ("Hello world!").Em seguida vamos imprimir no Console esse mesmo valor. Neste caso temos [1] "Hello world!",exatamente como no enunciado. Logo, a alternativa está correta.
Gabarito: C.

Nossa sugestão é que você tente usar o R para fazer alguns exercícios que vão ajudar você na fixação do conteúdo. Você pode usar como referência a própria aula ou os slides da videoaula sobre R.
30. Banca: TRC Ano: 2020 Concurso: Simualdo

Abra o R Studio e tente fazer o seguinte exercício.

1. Remova todos os objetos do ambiente de trabalho.

2. Crie objetos com nomes dados_Agente, dados_Perito, dados_Papi, dados_Escrivao.
Faça com que os objetos sejam do tipo numérico, character, lógico e inteiro.

3. Verifique a classe e a estrutura dos objetos criados.

4. Use ls() para listar apenas os dados de Perito. E depois para listar apenas os dados de
Agente.

5. Use rm() para remover apenas os dados de Escrivão (dica: você vai precisar de usar o resultado de ls()).
6. Salve sua área de trabalho com o nome exercicio_objetos_aula_de_R.RData.

Uma possível solução para os itens acima:

1. rm(list=ls()) # remove todos os objetos

2. dados_Agente <-10.5
dados_Perito <- "texto"
dados_Papi <-TRUE
dados_Escrivao <- 24L

3. class(dados_Agente)

class(dados_Perito)
class(dados_Papi)
class(dados_Escrivao)
str(dados_Agene)
str(dados_Parito)
str(dados_Papi)
str(dados_Escrivao)

4. perito <- ls(pattern="Perito")

agente <- ls(pattern="Agente")

5. rm(list=(ls(pattern="Escrivao"))

6. save.image(file=" objetos aula de R.RData")

2) EXERCÍCIoS

í. CEBRASPE (CESPE) - Analista de Previdência Complementar (FUNPRESP-
EXE)/lnvestimentos/2O22

A respeito de estatística e da linguagem de programação R, julgue o item a seguir.

No programa R, a função aritmética básica (2+2)A2=16 pode ser calculada digitando-se > 2+2 A
2.

2. CEBRASPE (CESPE) - Analista de Previdência Complementar (FUNPRESP-
EXE)/lnvestimentos/2O22

A respeito de estatística e da linguagem de programação R, julgue o item a seguir.

No programa R, o comando > sample (1:60, 6) fornece os seis números aleatórios para um jogo na Mega Sena.
3. FGV-Auditor Federal de Controle Externo (TCU)/Controle Externo/Auditoria
Governamental/2022

A tabela presente no código em R abaixo apresenta a quantidade de processos analisados por três analistas (denotados por Al, A2 e A3) em diferentes anos.
dados = tibble: :tibble(

Analista=c("Al", "Al", "Al", "A2","A2", "A3", "A3", "A3"),
Ano=c(2018,2019,2020,2019,2020,2018,2019,2020),
Processos=c(10,15,20,25,20,8,7,12))

Um programador roda o código abaixo em R.

tidyr::pivot_wider(data=dados, names_from="Analista", values_from="Processos")
Os valores esperados na primeira linha do objeto resultante do comando acima são:
A 2018, 10, NA, 8;

B Al, 10, 15, 20;

C Al, 2018, 10;

D 2018, 18;

E A2, 2019, 25.

4. CEBRASPE (CESPE) - Estatístico (FUB)/2022

R R Console : 11 a

> require (cldyvtr»)

> Idade <- c( 2Õf 30, Rkr 30, 40, 50)

> altura <- c<l. 6,1.7,1.5,1.8,1-7,1.7)

> dadoa < — data.freme(1dade r altura)

> dados idade altura
1 20 1.6

2 30 1.7

3 Nh 1. S

4 30 1.8

5 40 1.7

€ 50 1.7

► rM

Considerando que um usuário inicie uma sessão R escrevendo um código na janela R Console conforme mostra a figura apresentada, julgue o item subsequente.
Os códigos dados %>% na.omit() e dados %>% drop_na() proporcionam o mesmo resultado.

5. CEBRASPE (CESPE) - Estatístico (FUB)/2022

R R Console | o |[ Q

A

> requlre(üidyverae)

> X <- «(0,1,3,3,',$)

> y <- c(5.4,6.4,?. 9}

> z <- c("anf"b","awf' b", "a",

> graf o data-framé(x,yr 2)

> I

Considerando o código mostrado na figura apresentada, julgue o próximo item.
A figura a seguir é obtida mediante aplicação do seguinte código R:

ggplot(data=graf,mapping=aes(x=x, y=y))+
geom_line()+

geom_point()+
xlab("x")+

ylab("y")

6. FGV - Analista Judiciário (TJDFT)/Apoio Especializado/Estatística/2022

Utilizando a Linguagem R tem-se um objeto x como consta a seguir.
x

## [1] 1 3 4 3 4 <NA>

## Leveis: 13 4
is.factor(x)

## [1] TRUE

0 comando que resulta na soma dos elementos numéricos de x é:
A sum(as.numeric(as.character(x)), na.rm = TRUE);

B sum(x);

C sum(as.numeric(x), na.rm = TRUE);
D sum(as.numeric(x), na.rm = FALSE);
E sum(x[-5]).

7. FGV - Analista (MPE SC)/Dados e Pesquisas/2022

No contexto da linguagem de programação R, analise o código a seguir,
for (x in 1:10) {

if (x >= 4) {
print(x)
next}

if (x == 8) {break}

}

O número de linhas exibidas pela execução desse código é:

A 6;

B 7;

C 8;

D 9;

E 10.

8. FGV - Analista (MPE SC)/Dados e Pesquisas/2022
Analise o código da linguagem de programação R a seguir.
xpto <- array(c(l:24), dim = c(4, 3, 2))

print (xpto[3, 2, 1])

Na execução desse código, o print produz o valor:

A5
B 7

C 10

D 18

E 19

9. FGV - Analista (MPE SC)/Dados e Pesquisas/2022

No contexto da linguagem de programação R, analise as afirmativas a seguir.

I. Vetores (vectors) são listas de itens que devem ter o mesmo tipo.

II. R trabalha com vários tipos de dados (data types), numéricos, lógicos e textuais, mas as variáveis podem mudar de tipo mesmo depois da instanciação.
III. Os itens de uma lista (list) não podem ser substituídos. São permitidas apenas a inserção e a remoção de itens.
Está correto somente o que se afirma em:

Al;
B II;

C III;

D I e II;
E II e III.

10. IBFC - Supervisor de Pesquisas (IBGE)/Suporte Gerendal/2021

Função da linguagem de programação R que permite fazer gráficos de dispersão.
De acordo com a descrição, a função é:
A head
B plot

C grafhic

D dispersion
E mean n.CEBRASPE (CESPE) - Agente de Polícia Federal/2021 (e mais 2 concursos)
Com relação a conceitos de programação Python e R, julgue o item que se seguem.
0 resultado do código R seguinte será "12".

f<- function(x) {

g <- function(y) {
y + z

}

z <-4

x + g(x)

}

z <-10
f(4)

12. CEBRASPE (CESPE) - Técnico Bancário III (BANESE)/lnformática/Desenvolvimento/202i

Com respeito ao pacote reticulate da linguagem R, que propicia uma interface com os módulos,classes e funções do Python, julgue o item a seguir

O código seguinte permite importar o módulo math para utilização no ambiente R.
library(reticulate)

math <- use_python("math")

13. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
As funcionalidades do R são divididas em vários pacotes.

14. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

O sistema base R contém, entre outras coisas, o pacote base necessário para executar o R e contém as funções mais fundamentais.
15. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

Os pacotes utils, lang e tools são considerados pacotes básicos do R.

16. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
A função abaixo pula as primeiras 20 iterações do loop.

for(i in 1:100)
if(i <= 20) {

next

}

print(n)

}

17. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

O resultado da função abaixo é 5
x <-3

switch(x, 2+2, mean(l:10), rnorm(5))

18. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
next é usado para pular uma iteração dentro do loop.

19. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

Uma instrução break é usada dentro de um loop (repaet, for, while) para interromper iterações e fazer fluir o controle para fora do loop.
20. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

break e next são duas estruturas de controle para controlar explicitamente o loop.

21. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
Escrever funções é uma atividade secundária de um programador R.

22. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

As funções são definidas usando a diretiva function() e são armazenadas como objetos R.

23. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

A função graph() é usada para plotagem de gráficos no R base.

24. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

A função names() lista nomes das variáveis em um data.frame.

25. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
x <- c(l, 2, NA, 4, NA, 5)

deuruim <- is.na(x)
print(deuruim)

O resultado do código acima é :

FALSE FALSE TRUE FALSE TRUE FALSE

26. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.

O pacote dplyr pode ser instalado a partir do CRAN, usando library("dplyr").

27. Ano: 2020 Prova: Simulado Banca: TRC Assunto: Linguagem R

Julgue os itens baixo a respeito dos conceitos básicos do R.
Arquivos contendo scripts R terminam com a extensão .R

28. Ano: 2018 Banca: CESPE Assunto: Informática para Polícia Federal Cargo: Agente

Conteúdo: Linguagem R

Julgue os próximos itens, relativos a noções de programação Python e R.
93 Considere o programa a seguir, escrito em R.

x <- c (3, 5, 7)

y <- c (1, 9,11)

print (x + y)

Após a execução do programa, será obtido o seguinte resultado.
W36

94 Considere o programa a seguir, escrito em R.
x<-TRUE

y<-FALSE

print (xy)

Após a execução do programa, será obtido o seguinte resultado.

[i] FALSE

29.Ano: 2018 Prova: Perito - Polícia Federal Banca: CESPE Assunto: Conhecimentos básicos -
banco de dados e teoria da informação.

Com relação à programação Python e R, julgue os itens que se seguem.

43 Considere os comandos a seguir, na linguagem R, os quais serão executados no ambiente do R, e considere, ainda, que > seja um símbolo desse ambiente.
> helloStr <- "Hello world!"

> print(helloStr)

Nesse caso, após a execução dos comandos, será obtido o resultado a seguir.

[1] "Hello world!"

3) GABARITo

1. Errado

2. Certo

3. A

4. C

5. E

6. A

7. B

8. B

9. D

10. B

11. Certo

12. Errado

13. C

14. C

15. E

16. C

17. E

18. C

19. C

20. C

21. E

22. C

23. E

24. C

25. C

26. E

27. C

28. E E

29. C

4) CÓDIGO DA VIDEOAULA

#Criando objeto textual y <- "José íris DS Junior"y

#Criando objeto numérico z <- 10
z

#Criando vetores x <- c(l,2,4)
q <- c(x, x, 5)

t <- c(z,y)

#Acessando o sexto elemento do vetor t t [6]
#Acessando do segundo ao sexto elemento do vetort t[2 :6]
#Calculando a média do vetor q mean(q) #calcula a média de q
#Conhecendo o dataset Nile

Ni 1 e

#Calculando o desvio padrão sd(Ni1e)
#Usando o help heip(Ni1e)
#criando um histograma com o serie temporal de fluxo de água no rio Nilo hi st (Ni 1 e)
#Usando o for para descobrir o conjunto de números pares e ímpares de um vetor k <- 0
o <- 0

x <- c(l,2,3,4,5,6,7,8,9,10)

for (n in x) {
pri nt(n)

if ( n %% 2 == 1) {

k <- k + 1

} else {

o <- o + 1

}

}

k o
#Questão PF 2018

helloStr <- "Hello world!"
pri nt(hel 1 oStr)

#Criando variáveis aprovado <- "Cachoeirense Concurseiro"aprovado2 <- 'Hugo'

aprovado2

#Variável do tipo lógico convocado <- T
itensDoChurrascoDePosse <- c("Picanha",
"Pão de Alho")

ItensDoChurrascoDePosse

"Carvão", "Maminha",

Convi dadosDoChurrasco <- c("Prof. Thi ago", "Mai nha",
"Painho", "Hugo", "dosé íris")

#Usando operados aritméticos xl <- 10
x2 <- 20

x3 <- 4

xl + x2 + x3

y <- xl*x2 + x3
y

#Questão - PF (01)

x <- c (3, 5, 7)

y <- c (1, 9, 11)

print (x + y)

#Questão - PF (02)

X <- TRUE
y <- TRUE

print (xy) #gera um erro

#antes de você rodar o código, qual seria o erro na sua opi ni ão?
#Exemplo de cbind xl <- read.csv("data01.csv",header=T,sep=",")x2 <- read.csv("data02.csv",header=T,sep=",")

x3 <- cbind(xl,x2)
x3

#Exemplo de rbind x4 <- read.csv("data01.csv",header=T,sep=",")x5 <- read.csv("data03.csv",header=T,sep=",")

#conhecendo a estrutura de x5
str(x5)

x6 <- rbind(x4,x5)
x6

#Criando uma função elizabethFunction <- function(x = 5){factori al(x)+5

#data frame mat <- matrix(c("a","b",1,2) , ncol= 2)
df <- data.frame(x = c("a","b"), y = c(l,2))
str(mat)

##chr[i:2,1:2] "a" "b" "i" "2"

str(df)

## 'data.frame': 2 obs. of 2 variables:

## $ x: Factorw/ 2 leveis "a","b": 12
## $ y: num 1 2

#Dando nomes as linhas e as colunas rownames(df) <- c("l1","12")colnames(df) <- c("letras", "numeros")
str(df)

df

