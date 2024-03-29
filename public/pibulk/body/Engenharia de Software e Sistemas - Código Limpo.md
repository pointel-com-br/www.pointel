# Engenharia de Software e Sistemas - Código Limpo

O que é o Código Limpo, ou Clean Code em inglês? Há muitas definições, mas algumas respostas e características encontradas são comuns, como por exemplo, a codificação deve ser simples e de fácil manutenção, não pode haver repetições de código, testes de unidade devem ser implementados, implementação de forma organizada, entre outros.
O Código Limpo é um conjunto de técnicas de programação que quando praticadas pelos desenvolvedores tem como objetivo garantir a legibilidade e qualidade do código produzido.
Escrever um código compreensível para outros colaboradores tornou-se crucial para melhorar a colaboração e a produtividade. O Código Limpo tornou-se uma das práticas de software mais relevantes e tem sido amplamente adotado como sinônimo de qualidade de código por desenvolvedores de software e organizações de desenvolvimento de software em todo o mundo. No entanto, muito pouco se sabe sobre se os desenvolvedores concordam com os princípios do Código Limpo e como eles os aplicam na prática.
Há inúmeras definições para Código Limpo, ao longo dessa parte da aula, vou apresentar as citações mais importantes de grandes programadores, os mais conhecidos, trazidos pelo livro

Código Limpo.

Um código ruim incita o crescimento do caos num código. Quando outras pessoas alteram um código ruim, elas tendem a piorá-lo. Dave Thomas e Andy Hunt expressam isso de outra forma. Eles usam a metáfora das janelas quebradas. Uma construção com janelas quebradas parece que ninguém cuida dela. Dessa forma, outras pessoas deixam de se preocupar com ela também. Elas quebram. Elas estragam a fachada com pichações e deixam acumular lixo. Uma única janela inicia o processo de degradação.

Para Bjarne um código limpo faz bem apenas uma coisa. Não é por acaso que há inúmeros princípios de desenvolvimento de software que podem ser resumidos a essa simples afirmação. Um código ruim tenta fazer coisas demais, ele está cheio de propósitos obscuros e ambíguos. O código limpo é centralizado. Cada função, cada classe, cada módulo expõe uma única tarefa que nunca sofre interferência de outros detalhes ou fica rodeada por eles.
Um código limpo é simples e direto. Ele é tão bem legível quanto uma prosa bem escrita. Ele jamais torna confuso o objetivo do desenvolvedor, em vez disso, ele está repleto de abstrações claras e linhas de controle objetivas.

Além de seu criador, um desenvolvedor pode ler e melhorar um código limpo. Ele tem testes de unidade e de aceitação, nomes significativos; ele oferece apenas uma maneira, e não várias, de se fazer uma tarefa; possui poucas dependências, as quais são explicitamente declaradas e oferecem um API mínimo e claro. O código deve ser inteligível já que dependendo da linguagem, nem toda informação necessária pode ser expressa no código em si.

Eu poderia listar todas as qualidades que vejo em um código limpo, mas há uma predominante que leva a todas as outras. Um código limpo sempre parece que foi escrito por alguém que se importava. Não há nada de óbvio no que se pode fazer para torná-lo melhor. Tudo foi pensado pelo autor do código, e se tentar pensar em algumas melhoras, você voltará ao início, ou seja, apreciando o código deixado para você por alguém que se importa bastante com essa tarefa.

Vejamos as palavras de Ron Jeffries: nestes anos recentes, comecei, e quase finalizei, com as regras de Beck sobre código simples. Em ordem de prioridade, são:

1. Efetue todos os testes;

2. Sem duplicação de código;

3. Expressa todas as ideias do projeto que estão no sistema;

4. Minimiza o número de entidades, como classes, métodos funções e outras do tipo;

Dessas quatro, Jeffries foca mais na de duplicação. Quando a mesma coisa é feita repetidas vezes, é sinal de que uma ideia em sua cabeça não está bem representada no código. Tento descobrir o que é e, então, expressar aquela ideia com mais clareza.

Expressividade, para Jeffries, são nomes significativos. Com ferramentas de programação modernas, como a Eclipse, renomear é bastante fácil. Entretanto, a expressividade vai além de nomes. Também se verifica se um método ou objeto faz mais de uma tarefa. Se for um objeto, provavelmente ele precisará ser dividido em dois ou mais. Se for um método, sempre usa-se a refatoração do Método de Extração nele, resultando em um método que expressa mais claramente sua função e em outros métodos que dizem como ela é feita.

Duplicação e expressividade levam ao que é considerado um código limpo, e melhorar um código ruim com apenas esses dois conceitos na mente pode fazer uma grande diferença. Redução de duplicação de código, alta expressividade e criação no início de abstrações simples. É isso que torna um código limpo.

Sem duplicação;

Uma tarefa;

Alta expressividade;

Pequenas abstrações.

Você sabe que está criando um código limpo quando cada rotina que você leia se mostra como o que você esperava. Você pode chamar de código belo quando ele também faz parecer que a linguagem foi feita para o problema.

Um código só está realmente limpo se ele for validado. Mas a questão é, como é possível manter um teste limpo? A resposta é simples, da mesma maneira que mantemos o nosso código limpo, com clareza, simplicidade e consistência de expressão.
Testes limpos seguem as regras do acrônimo FIRST (Fast, Indepedent, Repeatable, Self-validation, Timely).

· Rapidez: os testes devem ser rápidos para que possam ser executados diversas vezes;

· Independência: quando testes são dependentes, uma falha pode causar um efeito dominó dificultando a análise individual;

· Repetitividade: deve ser possível repetir o teste em qualquer ambiente;

· Auto validação: bons testes possuem como resultado respostas do tipo verdadeiro ou falso. Caso contrário, a falha pode se tornar subjetiva;

· Pontualidade: os testes precisam ser escritos antes do código de produção, onde os testes serão aplicados. Caso contrário, o código pode ficar complexo demais para ser testado ou até pode ser que o código não possa ser testado.

Índice

1 3 R's da Arquitetura de software

1.1 Readability (legibilidade) - Nomes Significativos
1.2 Reusability (Reuso) - Reutilização de funcionalidades
1.3 Refatoring (refatoração) - Otimização da estrutura

1.3.1 Comentários Compensam um Código Ruim
1.3.2 Explique-se no Código
1.3.3 Comentários bons
1.3.4 Comentários Ruins
1.3.5 Formatação
1.3.6 O Objetivo da Formatação
1.3.7 Objetos e Estruturas de Dados

3 R's da Arquitetura de software
O conceito do Clean Code é baseado nos 3 R's da Arquitetura de software, que são Readability (legibilidade), Reusability (reuso) e Refatoring (refatoração). Os 3 conceitos se complementam para a obtenção de um projeto sustentável à empresa.
A legibilidade prioriza a clareza na escolha de nomes, padronização da escrita e formatação da codificação, tendo como principais características:

· Nomes de variáveis;

· Nomes de funções;

· Formatação;

· Níveis de aninhamento;

· Quantidade de linhas em funções;

· Quantidade de Argumentos passados a uma função.

A reutilização diz respeito à criação de funcionalidades que possam ser reutilizadas dentro do sistema, priorizando fatores como:

· Um nível de abstração;

· Tamanho da função;

· Indentação;

· Níveis de aninhamento;

· Efeitos colaterais;

· Parâmetros de saída.

O refatoramento diz respeito à capacidade do sistema em permitir a otimização da estrutura sem que outras funcionalidades sejam afetadas. Nesta etapa são priorizados os seguintes fatores:

· Efeitos colaterais isolados;

· Testes constantes de funcionalidades;

· Refinamento sucessivo.

Readability (legibilidade) - Nomes Significativos

A partir desta introdução aos conceitos da Arquitetura de Software vamos aprofundar nossos conhecimentos sobre a legibilidade do código. Iniciaremos falando sobre a parte mais importante do seu código, nomes. Os nomes dizem muito sobre o desenvolvedor responsável, eles devem expressar as vontades de seu criador, os propósitos para que foi criado e todo o seu apreço pelo projeto. Dizer que os nomes devem demonstrar seu propósito é fácil. Escolher bons nomes leva tempo, mas economiza mais.

Nomes Significativos

Descrição

Use Nomes que Revelem seu Propósito

Cuide de seus nomes e troque-os quando encontrar melhores. O nome de uma variável, função ou classe deve responde a todas as grandes questões. Ele deve lhe dizer por que existe, o que faz e como é usado. Exemplo:
int d; // tempo decorrido em dias
O nome d não revela nada. Melhores opções:
int elapsedTimeInDays;
int daysSinceCreation;
int daysSinceModification;
int fileAgeInDays;

Evite Informações Erradas

Deve-se evitar passar dicas falsas que confundam o sentido do código. Devemos evitar palavras cujos significados podem se desviar daquele que desejamos. Por exemplo, hp, aix e sco seriam nomes ruins de variáveis, pois são nomes de plataformas Unix ou variantes. Mesmo se estiver programando uma hipotenusa e hp parecer uma boa abreviação, o nome pode ser mal interpretado. Lembre-se que ao criar um objeto levamos em conta o nome dado àquela classe, não os comentários ou lista de métodos que ela contém.

Faça Distinções Significativas

As IDE's não possibilitam que dois elementos tenham o mesmo nome, isso implica ao desenvolvedor utilizar nomes semelhantes ou em sequência como: a1, a2, a3, esta prática além de dificultar a leitura vai contra a regra anterior. Não há problemas em usar prefixos, porém sempre pensando em distinção significativa, devemos analisar os nomes para retirar trechos desnecessários como ambiguidades. Também devemos evitar palavras muito comuns ou vagas, pois podem passar ao leitor vários significados e permitir que ele entenda da forma que quiser dentro das possibilidades.

Use Nomes Pronunciáveis

Exemplo de classe com nomes não pronunciáveis: class DtaRcrd102 {
};
private Date genymdhms; private Date modymdhms;
private final String pszqint = "102";
Exemplo com Nomes Pronunciáveis class Customer {
};
private Date generationTimestamp; private Date modificationTimestamp; private final String recordId = "102";

Use Nomes Passíveis de Busca

Nomes de uma só letra ou números possuem um problema em particular por não ser fácil localizá-los ao longo de um texto. Pode-se usar facilmente o grep para MAX_CLASSES_PER_STUDENT, mas buscar o número 7 poderia ser mais complicado. Nomes, definições de constantes e várias outras expressões que possuam tal número, usado para outros propósitos podem ser resultados da busca.

Evite Codificações

Codificar informações do escopo ou tipos em nomes simplesmente adiciona uma tarefa extra de decifração. É uma sobrecarga mental desnecessária ao tentar resolver um problema. Nomes codificados raramente são pronunciáveis, além de ser fácil escrevê-los incorretamente.

Evite Mapeamento Mental

Devemos evitar a tradução mental de nomes, atribuindo nomes de domínio ou de solução que sejam diretos e objetivos. Esta regra ressalta o problema em utilizar nomes com apenas uma letra, pois permite que seu leitor interprete de maneira livre, apenas levando em conta o conceito contido naquele trecho de código. De maneira geral, desenvolvedores são muito espertos e provavelmente consigam mapear uma variável apenas pelo contexto do trecho, porém devemos pensar em todos os possíveis leitores. Uma diferença entre um programador esperto e um programador profissional é o entendimento sobre a clareza em que expressa seu código.

Nomes de Classes

Classes e objetos devem ter nomes com substantivo(s), como Cliente, PaginaWiki, Conta e AnaliseEndereco. Evite palavras como Gerente, Processador, Dados ou Info no nome de uma classe, que também não deve ser um verbo.

Nomes de Métodos

Os nomes de métodos devem ter verbos, como postarPagamento, excluirPagina ou salvar. Devem-se nomear métodos de acesso, alteração e autenticação segundo seus valores e adicionar os prefixos get, set ou is de acordo com o padrão javabean.*

Selecione uma Palavra por Conceito

Faça uma análise de palavras do domínio e coloque um padrão na utilização de conceitos. Por exemplo, é confuso utilizar pegar, recuperar e obter como métodos equivalentes em classes diferentes. Os ambientes de desenvolvimento, como o Eclipse ou IntelliJ, oferecem dicas relacionadas ao contexto como listas com métodos e nomes de variáveis que você pode chamar em determinado objeto. Mas devemos notar que a lista retornada não oferece os comentários sobre a função, então deve-se ter clareza na escolha dos nomes para que nesta etapa não seja necessário revisar trechos de código.

Use Nomes a partir do Domínio da Solução

Lembre-se sempre de que serão programadores que lerão seu código, então utilize termos da área, nomes de padrões e termos matemáticos. Não é prudente utilizar um nome a partir do domínio do problema, pois seria um transtorno identificar o conceito do problema para saber o significado do nome. Nomes como AccountVisitor ou JobQueue se expressam muito bem ao programador, então nomes técnicos, normalmente, são os mais adequados.

Adicione um Contexto Significativo

Há poucos nomes significativos por si só, portanto devemos utilizar nomes que tragam contexto ao leitor. Utilize nomes expressivos e que se complementam para formar uma linha de raciocínio, os nomes em uma classe devem se complementar e transmitir a ideia de seu desenvolvedor.

Não Adicione Contexto Desnecessário

Em sistemas desenvolvidos no domínio da AZ, seria uma péssima ideia adicionar prefixos "AZ" em todas as classes. Este contexto adicionado vai contra as suas ferramentas, pois a busca resultará um resultado enorme de todas as classes que tenham o prefixo. Nomes curtos geralmente são melhores, apenas precisam ser claros. Sempre revize seu código e melhore os nomes utilizados, gaste um tempo a mais com o objetivo de criar um código legível.

Para criar nomes que revelem seu propósito devemos seguir os seguintes conceitos:

· Nomes de variáveis devem informar seu conteúdo ou sua finalidade.

· Nomes de funções devem informar a atividade executada pela função.

· Nomes bons dispensam comentários, sempre troque comentários sobre variáveis por um nome que facilite o entendimento.

· Faça um bom uso do Naming Convention. Nomes de constantes no padrão SNAKE_CASE e demais nomes no padrão CamelCase.

Reusability (Reuso) - Reutilização de funcionalidades

A primeira regra para funções é que elas devem ser pequenas. A segunda é que precisam ser mais espertas do que isso. De acordo com o autor do livro Clean Code, por cerca de quatro décadas criando funções de tamanhos variados. Essa experiência ensinou que, ao longo de muitas tentativas e erros, as funções devem ser muito pequenas.
Por outro lado, quando se trata de reutilização de funcionalidades, temos as seguintes diretrizes:

Reutilização de funcionalidades

Descrição

Funções Devem ser pequenas

O livro aconselha a construir funções cada vez menores, pois são mais fáceis de realizar manutenção. A recomendação é: As funções devem ter no máximo 20 linhas.

Blocos de endentação

É fortemente recomendado que blocos dentro de instruções if, else, while e outros devem ter apenas uma linha, possivelmente seja uma chamada de outra função. Esta recomendação mantém a função pequena e adiciona um valor significativo. Esta recomendação também implica que as funções não devem ser grandes e possuir vários níveis de aninhamento, ocasionando em um nível de indentação de no máximo dois blocos.

Faça apenas uma coisa

No SRP (Princípio de Responsabilidade Única) há uma regra sobre funções de uma única ação. Quando se tem mais de uma ação sendo executada dentro de uma única função pode-se gerar erros difíceis de serem encontrados e é mais propenso a erros. As funções devem fazer uma coisa e devem fazê-la bem. No início do projeto pode-se realizar um mapeamento de ações que devem ser implementados e por meio desse mapeamento podemos decompor as ações em funções menores, pensando sempre em fazer apenas uma ação.

Um nível de abstração por função

A fim de confirmar se nossa função tem uma responsabilidade, é necessário verificar se todas as instruções dentro da função estão no mesmo nível de abstração. O nível de abstração diz respeito aos conceitos implementados dentro da função, deve-se deixar bem claro o nível de importância sobre aquele trecho separando meros detalhes de conceitos extremamente importantes.

Regra decrescente

Como em uma narrativa, queremos que o código seja lido de cima para baixo e que cada próximo conceito passe a ideia de um contexto maior que se complementa a cada novo trecho. Cada parágrafo deve descrever o nível atual e fazer referência aos parágrafos consecutivos do próximo nível. Temos a orientação da leitura nas direções da esquerda para a direita e de cima para baixo, devemos facilitar aos usuários a leitura dessa forma padrão.

Use nomes descritivos

NOVAMENTE! Os nomes atribuídos às funções devem ses autoexplicativos e claros, devem transmitir ao leitor a ideia colocada pelo desenvolvedor dentro daquela função. Não tenha medo de criar nomes extensos para as funções, pois estes são melhores que nomes pequenos e enigmáticos e também poupa o trabalho de adicionar comentários de descrição sobre as funções. Lembre-se sempre das convenções de nomenclaturas, elas possibilitam a melhor leitura dos nomes.

Parâmetros de funções

A quantidade ideal de parâmetros para uma função é de zero, seguida por um parâmetro, depois dois parâmetros e assim por diante. Deve-se, sempre que possível, evitar funções com três parâmetros, apenas com motivos muito especiais devemos ignorar essa regra. Esta regra é imposta por ser uma tarefa difícil complementar o nome da função com os nomes dos parâmetros.

Funções mônades comuns

As funções citadas no livro como mônades, são funções que possuem um único parâmetro. Elas são utilizadas quando, você está fazendo uma pergunta sobre aquele parâmetro, como em boolean fileExists("Myfile"), ou você pode trabalhar sobre aquele parâmetro transformando-o em outro elemento ou retornando-o.

Parâmetros lógicos

Mais conhecidos como flags, não passam de valores booleanos passados a uma função. Certamente é uma prática horrível, pois viola a regra de que a função deve ter apenas uma responsabilidade. caso o valor seja falso ela terá um comportamento, caso contrário será outro comportamento diferente. O ideal é que sejam divididas em duas funções que são responsáveis para cada estado da flag.

Funções díades

Funções díades possuem uma dificuldade maior na leitura em comparação com funções mônades. Há casos que dois parâmetros são necessários e devemos realizar uma análise sobre os parâmetros passados, filtrando a utilização apenas em casos que os parâmetros são valores independentes e necessários.

Funções tríades

Devemos evitar ao máximo o uso desse tipo de funções, além de ser consideravelmente mais difíceis de entender, ainda possuem questões de ordenação e pausa que são mais recorrentes.

Evite efeitos colaterais

Efeitos colaterais são mentiras ocasionadas pelo contexto da função. Se sua função atende a regra de fazer apenas uma coisa, não teremos efeitos colaterais pois sabemos bem o que está sendo executado. Ações a mais em uma função podem fazer alterações desnecessárias aos parâmetros conhecidos, sejam os da função ou globais.

Separação comando-consulta

As funções devem fazer ou responder algo, nunca ambos. Lembre-se de criar funcionalidades fazendo a separação entre a alteração de informações e retorno delas, efetuar as duas tarefas costuma gerar confusão.

Evite Duplicação

Faça uma análise das funcionalidades implementadas e caso note a semelhança entre ações, transforme em uma só. A duplicação no código pode passar despercebida e isso leva a maiores oportunidades para a omissão de erros.
A duplicação pode ser a raiz de todo o mal no software, muitos princípios e práticas têm sido criados com a finalidade de controlá-la ou eliminá-la.Considere que a programação orientada a objeto serve para centralizar o código em classes-base que seriam redundantes em outro conceito.

Refatoring (refatoração) - Otimização da estrutura

Nada pode ser tão útil quanto um comentário bem colocado. Porém nada pode ser tão prejudicial quanto comentários desnecessários e supérfluos, no máximo os comentários são um mal necessário.
O uso adequado de comentários compensa nosso fracasso em nos expressar no código, comentários são utilizados quando não encontramos outra forma de nos expressar adequadamente. Portanto, quando você estiver numa situação na qual precise criar um comentário, pense bem e veja se não há uma maneira melhor de se expressar através do código.

Ao utilizar comentários lembre-se de que as tecnologias estão em constante evolução e seus comentários podem se tornar antiquados ou desatualizados. Muitas das vezes os comentários mentem, quanto mais antigo e mais longe do trecho que ele descreve, mais provável que esteja errado.

Comentários Compensam um Código Ruim

Uma das motivações mais comuns para criar comentários é um código ruim. Temos ciência da bagunça que criamos e adicionamos um comentário com o pensamento de que o código será melhor, quando na verdade ainda temos um código ruim sendo poluído com comentários ruins.
Códigos claros e expressivos com poucos comentários são de longe superiores a um amontoado e complexo com muitos comentários. Ao invés de perder seu tempo criando comentários utilize para limpar e melhorar o código.

Explique-se no Código

Há vezes em que não é possível se expressar direito no código. Infelizmente muitos programadores assumiram que o código é um bom meio para se explicar.
Passe algum tempo pensando em como ter expressividade no seu código, com certeza não será um tempo perdido. Muitas das vezes a mudança é apenas nomear as funções com o que você tem em mente para um comentário.

Comentários bons

Certos comentários são necessários ou benéficos. Entretanto tenha em mente que o único comentário verdadeiramente bom é aquele em que você encontrou uma forma de não o escrever.

Tipos de Comentários bons

Descrição

Comentários Legais

Às vezes nossos padrões de programação corporativa nos forçam a escrever certos comentários por questões legais. Então devemos adicionar um comentário padrão no cabeçalho dos arquivos, contendo as informações sobre direitos autorais da aplicação. Sempre que possível coloque estes comentários em arquivos externos.

Comentários Informativos

Às vezes precisamos fornecer informações básicas sobre uma funcionalidade, seja pelo valor ou pelo formato retornado pelas variáveis. caso o nome da função já informe o leitor, então deve-se ignorar o comentário, mas é aceitável criar um comentário informativo para esta situação. Muitas vezes um comentário vai além de ser apenas informações úteis sobre a implementação, ele fornece a intenção por trás de uma decisão. O esclarecimento sobre a utilização de parâmetros também é aceitável.

Alerta Sobre consequências

As consequências da execução e manutenção de determinados trechos podem estar em comentários. O comentário pode auxiliar o leitor a identificar as consequências e permite uma ação prévia, como:
\\execute apenas se tiver tempo disponível await browser.waitFor(1000000000);

Comentário TODO

Os comentários podem elencar os próximos passos a fazer. TODOs são tarefas que os programadores acham que devem ser efetuadas, mas por alguma razão não podem implementá-las no momento. Podem ser um lembretesobre uma alteração que deve ser feita, um pedido para a verificação de outro membro. Hoje em dia, a maioria das IDEs oferecem ferramentas e recursos para localizar os comentários TODO; portanto não é provável que fiquem perdidos no código. Revise regularmente seu código e elimine os comentários TODO.
Comentários Ruins

Quase todos os comentários caem nesta categoria, geralmente os comentários se tornam suporte ou desculpas para um código de baixa qualidade.

Tipo de comentário ruim

Descrição

Murmúrio

Usar um comentário que não fará sentido ao leitor, simplesmente é um comentário sobre as frustrações na hora da codificação são tidos como murmúrios e não agregam valor ao projeto.

Comentários Enganadores

Às vezes, mesmo com as melhores intenções, o programador faz uma afirmação não muito clara em seus comentários. Uma pequena desinformação expressada em comentário pode dificultar a leitura e provocar erros futuros.

Comentários ruidosos

Por vezes os comentários não são nada além de chiados, que dizem obviedades e não fornecem novas informações sobre o código. Estes comentários levam ao leitor a ignorá- los, com o tempo os olhos passam direto por eles e conforme a manutenção do código estes comentários passam a mentir.

Marcadores de Posição

Alguns programadores gostam de marcar uma posição determinada no arquivo fonte, como:
for(var i in itens){
}//for////
Raramente as junções por comentários fazem sentido em certas funções, mas de modo geral eles são aglomerações e devemos excluí-los. Tenha em mente que indicadores são chamativos no código, use-os esporadicamente para não se tornarem ruídos.
Código em comentários

Nunca, nunca mesmo, deixe código comentado no corpo de seu arquivo. Outros desenvolvedores que tiverem o contato com esse código não teriam coragem de excluir os comentários, pois passam a impressão de que estão lá por um motivo e são importantes demais para serem apagados. Essa prática tende a acumular comentários desnecessários e leva o leitor à uma confusão.

Informações não-locais

O comentário deve estar próximo ao código que ele descreve. Não forneça informações gerais do sistema no contexto de um comentário local. Considere por exemplo o comentário do Javadoc abaixo. Além de ser terrivelmente redundante, ele também fala sobre uma porta padrão que a função ainda não tem acesso.

Cabeçalhos de funções e fechamentos

É muito comum adicionarmos cabeçalhos em funções para passar alguma informação sobre a próxima função, porém funções curtas não requerem muita explicação. Um nome bem selecionado costuma ser melhor do que um comentário no cabeçalho.
Também são desnecessários os comentários de fechamento das ações e blocos, eles não contribuem em nenhum aspecto. Uma boa formatação substitui os comentários de fechamento.

Entretanto, há situações em que é recomendado fazer uso dos comentários, como:

· Legal Comments: copyright e authorship podem ser necessários e razoáveis de se colocar no início de cada arquivo.

· Informative Comments: por exemplo, explicando o formato aceito por uma expressão regular.

· Explanation of Intent: explicar a intenção por trás de uma decisão.

· Clarification: quando o código não puder ser modificado e algo obscuro necessitar ser explicado.

· Warning of Consequences: avisar os efeitos colaterais de se executar um método.Ex: Test case demorado.

· TODO Comments: não é uma desculpa para deixar código ruim no sistema. Serve como um lembrete.

· Amplification: amplifica a importância de uma ação que caso contrário poderia parecer sem importância.

Formatação

Quando as pessoas olham nosso código desejamos que fiquem impressionadas com a clareza, consistência e a atenção aos detalhes presentes. Queremos passar toda a organização, o apreço e o profissionalismo que aplicamos na criação do projeto.
Você deve tomar conta para que seu código fique bem formatado, escolher uma série de regras simples que governem seu código e aplicá-las de forma consistente. Estas regras devem ser tomadas pela equipe, se for o caso, e todo o projeto deve girar em torno dessas regras.

O Objetivo da Formatação

A formatação do código é importante. Ela serve como uma comunicação e é a primeira regra para um desenvolvedor profissional. A funcionalidade que você cria tem grandes chances de ser modificada na próxima manutenção, mas a legibilidade do seu código terá um grande efeito sobre essas modificações, então se preocupe com a legibilidade. Seu estilo e disciplina sobrevivem, mesmo que seu código não.

Faça uma boa utilização das Naming Conventions, temos alguns padrões para as linguagens que facilitam a leitura.

Os principais padrões de Naming Conventions para o java são:

· CamelCase - Utilizado para nomear funções e variáveis, este padrão remete que são utilizadas palavras compostas e faz a distinção por iniciais em maiúsculo. EX: daysInMonth.

· SNAKE_CASE - Utilizado para nomear constantes, este padrão é normalmente utilizado com todos os caracteres em maiúsculo e um "_" para a separação das palavras compostas, como no exemplo a seguir:

Tipos de Formatação

Descrição

Formatação Vertical

O seu código-fonte deve ser de que tamanho? O Robert responde a essa questão, o número máximo deve ser de 500 linhas. Há uma grande diversidade de tamanhos e algumas diferenças notáveis em estilo. No livro são elencados sete projetos diferentes: JUnit, FitNesse, testNG, Time and Money, JDepend, Ant e Tomcat. As linhas verticais de todos eles atendem ao máximo de 500 linha e o mínimo encontrado foi um arquivo de 6 linhas. A partir destes exemplos podemos dizer que é possível construir sistemas significativos a partir de códigos simples de 200 linhas, com um limite máximo de 500. Arquivos pequenos costumam ser mais fáceis de se entender.

Espaçamento vertical entre conceitos

Quase todo o código é lido da esquerda para a direita e de cima para baixo. Todas as linhas representam expressões e estruturas, cada grupo de linhas representa um pensamento completo. A cada pensamento escrito no código devemos separar por uma linha em branco, isso facilita a leitura e cria uma separação entre os conceitos.

Continuidade Vertical

Se o espaçamento separa conceitos, então a continuidade vertical indica uma associação íntima entre o código. Assim, linhas de código que possuem relação dos conceitos devem aparecer verticalmente unidas. Note no exemplo acima que os elementos de um mesmo conceito estão próximos, enquanto outros possuem o espaçamento de 1 linha.

Distância vertical

A equipe de desenvolvimento deve elaborar regras para a codificação. O livro cita algumas regras que são utilizadas como padrão sobre distância vertical, são:
Declaração de variáveis: Deve ser o mais próximo do local onde serão utilizadas, como pretendemos criar funções pequenas as variáveis devem estar no topo.
Instância de variáveis: Deve ocorrer no início da classe. Há muita discussão sobre a posição das instâncias, em C++ é comum a regra da tesoura, na qual colocamos todas no final da classe. O Java a convenção é colocá-las no início da classe.
Funções dependentes: Se uma função chama outra, elas devem ficar verticalmente próximas e a que chamar deve ficar acima da função que é chamada. Essa recomendação permite que o leitor se localize no código por meio das funções, quando há uma chamada é esperado que a outra função esteja abaixo.
Afinidade conceitual: Quanto maior a afinidade entre as funcionalidades, menor deve ser a distância entre elas. A afinidade conceitual pode ser definida por meio de funcionalidades que se complementam, mesmas tarefas básicas ou chamadas.

Formatação horizontal

Após falarmos sobre o tamanho do arquivo e o espaçamento vertical, podemos entrar no debate sobre o tamanho horizontal do código. Qual deve ser o tamanho de uma linha? Novamente analisando os sete projetos citados no livro temos uma regularidade com cerca de 45 caracteres, nestes projetos os desenvolvedores claramente preferem linhas curtas. É aceitável que o tamanho de uma linha seja de 100 a 120 caracteres, porém é totalmente desnecessário ter de rolar a tela para a direita para acessar informações.

Indentação

Um arquivo é mais como uma hierarquia do que algo esquematizado. Há informações sobre o arquivo como um todo, às classes individuais, aos métodos dentro das classes e blocos de cada método. A fim de tornar visível a hierarquia desses escopos, indentamos as linhas de nosso código de acordo com sua posição na hierarquia. Classes e instruções a nível do arquivo não necessitam de indentação, métodos dentro de uma classe são indentados um nível à direita e assim consecutivamente. Os programadores dependem muito desse esquema de indentação, eles alinham visualmente na esquerda as linhas para ver em qual escopo elas estão. Esta técnica permite que escopos desnecessários ao leitor sejam pulados como as estruturas de if e while. Procuram mais a esquerda por novas declarações de métodos, novas variáveis e até novas classes.

Regras de equipes

A equipe de desenvolvedores deve escolher um único estilo de formatação para ser utilizado no projeto. O estilo deve ser consistente, não queremos que pensem que o código foi escrito por uma equipe em desacordo sobre as definições.
Lembre-se: um bom software é composto de uma série de documentos de fácil leitura. Eles também necessitam ter um estilo consistente e sutil. O leitor precisa confiar que a formatação sempre irá transmitir as mesmas informações.

Sugestões para criar um código que seja limpo, robusto, que trate erros com elegância e estilo:

Exceções

Descrição

Use exceções ao invés de retornar código de erro

É melhor lançar uma exceção quando um erro for encontrado, o código de chamada fica mais limpo e sua lógica não é ofuscada pelo tratamento de erro.

Crie primeiro sua estrutura try- catch-finally

O bloco try funciona como uma transação que pode ser cancelada a qualquer momento e deve continuar no bloco catch. O bloco catch deve deixar seu programa num estado mais consistente sem se importar com o que aconteça no try. Por isso é recomendável que as funcionalidades que possuem a probabilidade de gerar erros sejam iniciadas por blocos try-catch, isso ajuda a definir o que o usuário deve esperar, independente do que ocorre no try.

Não passe ou retorne Null

Quando retornamos null estamos criando problemas para a execução, basta esquecer uma verificação e tudo irá por água abaixo. Não passe null, a menos que esteja trabalhando com uma API que espere receber null. Passando valores null a única certeza que temos é de que será lançada uma NullPointerException. Na maioria das linguagens não há uma boa forma de lidar com valores nulos passados acidentalmente para uma chamada.

Utilize Exceções não verificadas

As exceções checadas surgiram com a primeira versão do java, de fato era uma ótima ideia carregar uma lista de exceções juntamente com a assinatura de um método. Desta maneira todas as assinaturas de exceções conhecidas pelo sistema serão notificadas ao usuário sempre que fossem necessárias. O preço de se utilizar exceções checadas é a necessidade de assinalar ao Caller todas as vezes que for utilizar o método, assim poluindo a interface. Uma saída para o problema em utilizar exceções checadas é transformá-las em exceções não checadas por meio da RuntimeException.

Objetos e Estruturas de Dados
Os objetos expõem as ações e ocultam os dados. Isso facilita a adição de novos tipos de objetos sem precisar modificar as ações existentes e dificulta a inclusão de novas atividades em objetos existentes.
As estruturas de dados expõem os dados e não possuem ações significativas. Isso facilita a adição de novas ações às estruturas de dados existentes e dificulta a inclusão de novas estruturas de dados em funções existentes.
Em um dado sistema, às vezes, desejaremos flexibilidade para adicionar novos tipos de dados, e, portanto, optaremos por objetos. Em outras ocasiões, desejaremos querer flexibilidade para adicionar novas ações, e, portanto, optaremos por tipos de dados e procedimentos.
Bons desenvolvedores de software entendem essas questões sem preconceito e selecionam a abordagem que melhor se aplica no momento.
Pessoal, as bancas estão aprofundando cada vez mais na cobrança, veja a questão abaixo e estude com afinco os tópicos seguintes descritos na tabela - pode cair na sua prova, como já caiu em provas anteriores!

Objetos e Estruturas de Dados

Descrição

Anti-simetria data/objeto

Os objetos usam abstrações para esconder seus dados, e expõem as funções que operam em tais dados. As estruturas de dados expõem seus dados e não possuem funções significativas. Note a natureza complementar das duas definições. Elas são praticamente opostas. Essa diferença pode parecer trivial, mas possui grandes implicações.

A lei de Demeter

Um módulo não deve enxergar o interior dos objetos que ele manipula. Os objetos escondem seus dados e expõem as operações. Isso significa que um objeto não deve expor sua estrutura interna por meio dos métodos acessores, pois isso seria expor, e não ocultar, sua estrutura interna. Mais precisamente, a Lei de Demeter diz que um método f de uma classe C só deve chamar os métodos de:

- C

- Um objeto criado por f

- Um objeto passado como parâmetro para f

- Um objeto dentro de uma instância da variável C

O método não deve chamar os métodos em objetos retornados por qualquer outra das funções permitidas. Em outras palavras, fale apenas com conhecidos, não com estranhos.

Carrinhos de trem

Esse tipo de código costuma ser chamador de carrinho de trem, pois parece com um monte de carrinhos de trem acoplados. Cadeias de chamadas como essa geralmente são consideradas descuidadas e devem ser evitadas. Na maioria das vezes é melhor dividi-las.

Híbridos

Estruturas híbridas ruins são metade objeto e metade estrutura de dados. Elas possuem funções que fazem algo significativo, e também variáveis ou métodos de acesso e de alteração públicos que, para todos os efeitos, tornam públicas as variáveis privadas, incitando outras funções externas a usarem tais variáveis da forma como um programa procedimental usaria uma estrutura de dados". Esses híbridos dificultam tanto a adição de novas funções como de novas estruturas de dados. Eles são a pior coisa em ambas as condições. Evite criá-los. Eles indicam um modelo confuso cujos autores não tinham certeza - ou pior, não sabiam se precisavam se proteger de funções ou tipos.

Estruturas Ocultas

A mistura adicionada de diferentes níveis de detalhes é um pouco confusa. Pontos, barras, extensão de arquivos e objetos não devem ser misturadas entre si e nem com o código que os circunda.

Objetos de transferência de dados

A forma perfeita de uma estrutura de dados é uma classe com variáveis públicas e nenhuma função. Às vezes, chama- se isso de objeto de transferência de dados, ou DTO (sigla em inglês). Os DTOs são estruturas muitos úteis, especialmente para se comunicar com bancos de dados ou analisar sintaticamente de mensagens provenientes de sockets e assim por diante. Eles costumam se tornar os primeiros numa série de estágios de tradução que convertem dados brutos num banco de dados em objetos no código do aplicativo. Os beans têm variáveis privadas manipuladas por métodos de escrita e leitura. O aparente encapsulamento dos beans parece fazer alguns puristas da OO sentirem-se melhores, mas geralmente não oferece vantagem alguma.

O Active Record

Os Active Records são formas especiais de DTOS. Eles são estruturas de dados com variáveis públicas (ou acessadas por Beans); mas eles tipicamente possuem métodos de navegação, como save (salvar) e find (buscar). Esses Active Records são traduções diretas das tabelas de bancos de dados ou de outras fontes de dados. Infelizmente, costumamos encontrar desenvolvedores tentando tratar essas estruturas de dados como se fossem objetos, colocando métodos de regras de negócios neles. Isso é complicado, pois cria um híbrido entre uma estrutura de dados e um objeto. A solução, é claro, é tratar o Record Active como uma estrutura de dados e criar objetos separados que contenham as regras de negócio e que ocultem seus dados internos (que provavelmente são apenas instâncias do Active Record).

