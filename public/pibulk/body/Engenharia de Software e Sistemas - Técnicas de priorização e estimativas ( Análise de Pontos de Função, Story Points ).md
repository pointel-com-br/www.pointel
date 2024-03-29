# Engenharia de Software e Sistemas - Técnicas de priorização e estimativas ( Análise de Pontos de Função, Story Points )

Índice

1) APF - Contexto Histórico

2) APF - Ponto de Função

3) APF - Principais Benefícios.

4) APF - Componentes Fundamentais.

5) APF - Etapas do Processo de Contagem

6) APF-NESMA

7) Resumo - APF

8) Questões Comentadas - APF - CESPE

9) Questões Comentadas - APF - FCC

10) Questões Comentadas - APF - FGV

11) Questões Comentadas - APF - Diversas.

12) Lista de Questões - APF - CESPE

13) Lista de Questões - APF - FCC

14) Lista de Questões - APF - FGV

15) Lista de Questões - APF - Diversas.

APRESENTAçÃo

Queridíssimos alunos(as), eu não vou mentir para vocês - essa é uma aula um pouquinho chata.Como assim, Diego? Galera, esse assunto pode ser muito abstrato se você nunca contou pontos de função na prática. Não há nada extremamente difícil, mas - por vezes - é possível que vocês se sintam um pouco perdidos porque a ideia aqui não é ensiná-los a contagem na prática,é acertar questões de prova. Agora, relaxem que ao final da aula vocês vão estar acertando tudo!
PROFESSOR DIEGO CARVALHO - WWW.INSTAGRAM.COM/PROFESSORDIEGOCARVALHO

Galera, todos os tópicos da aula possuem Faixas de Incidência, que indicam se o assunto cai muito ou pouco em prova. Diego, se cai pouco para que colocar em aula? Cair pouco não significa que não cairá justamente na sua prova! A ideia aqui é: se você está com pouco tempo e precisa ver somente aquilo que cai mais, você pode filtrar pelas incidências média, alta e altíssima; se você tem tempo sobrando e quer vertudo, vejam também as incidências baixas e baixíssimas. Fechado?
Além disso, essas faixas não são por banca - é baseado tanto na quantidade de vezes que caiu em prova independentemente da banca e também em minhas avaliações sobre cada assunto...
#ATENÇÃO

Avisos
Importantes

0 curso abrange todos os níveis de conhecimento...

Esse curso foi desenvolvido para ser acessível a alunos com diversos níveis de conhecimento diferentes. Temos alunos mais avançados que têm conhecimento prévio ou têm facilidade com o assunto. Por outro lado, temos alunos iniciantes, que nunca tiveram contato com a matéria ou até mesmo que têm trauma dessa disciplina. A ideia aqui é tentar atingir ambos os públicos -
iniciantes e avançados - da melhor maneira possível..

Por que estou enfatizando isso?

O material completo é composto de muitas histórias, exemplos, metáforas, piadas, memes, questões,
desafios, esquemas, diagramas, imagens, entre outros. Já o material simplificado possui exatamente o mesmo núcleo do material completo, mas ele é menor e bem mais objetivo. Professor, eu devo estudar por qual material? Se você quiser se aprofundar nos assuntos ou tem dificuldade com a matéria,necessitando de um material mais passo-a-passo, utilize o material completo. Se você não quer se aprofundar nos assuntos ou tem facilidade com a matéria, necessitando de um material mais direto ao ponto, utilize o material simplificado.
Por fim...

O curso contém diversas questões espalhadas em meio à teoria. Essas questões possuem um comentário mais simplificado porque têm o único objetivo de apresentar ao aluno como bancas de concurso cobram o assunto previamente administrado. A imensa maioria das questões para que o aluno avalie seus conhecimentos sobre a matéria estão dispostas ao final da aula na lista de exercícios e possuem comentários bem mais completos, abrangentes e direcionados.
ANÁLISE DE PoNToS DE FUNçÃo

Contexto Histórico

INCIDÊNCIA EM PROVA: BAIXA

Vamos contar um pouquinho da história da análise de pontos de função.
Em meados da década de setenta, Allan Albrecht - pesquisador da IBM -
estava buscando uma maneira de calcular a produtividade relativa de projetos de software desenvolvidos por um departamento da empresa.Em especial, ele procurava alguma técnica que permitisse realizar estimativas confiáveis que pudessem ser aplicadas antes que se investisse muita grana em um projeto.
Vamos colocar uma situação-problema: imagine que você passe em seu sonhado concurso público e comece a trabalhar em um grande órgão. Após alguns meses, você tem uma ideia genial de um software que poderia automatizar vários processos organizacionais economizando bastante dinheiro público. Você marca uma reunião com o chefe do órgão, conta a sua ideia e ele concorda com o desenvolvimento do software idealizado por você.
No entanto, há um problema: você não sabe quanto custará a implementação desse software! Ese for muito caro e o órgão não tiver grana suficiente? Bem, o jeito é fazer um orçamento com diversas empresas de software. Da mesma forma que você faz cotações com marceneiros para avaliar quanto custaria para produzir móveis planejados para a sua casa, você faz cotações com empresas de desenvolvimento para avaliar quanto custaria para produzir um software.
Galera, antes de surgir a análise de pontos de função, as estimativas de custo para produzir um software não eram nada confiáveis. Era comum o produto final acabar custando duas ou três vezes aquilo que havia sido previsto inicialmente. E como fazer para estimar o custo de um software? O nosso pesquisador já havia se feito a mesma pergunta e estava incomodado com a discrepância entre os valores estimados e realizados para desenvolvimento de softwares da IBM.
Além disso, como uma empresa pode se planejar se ela imagina que vai investir um determinado montante, mas ao final acaba tendo que investir o dobro ou triplo? Bem, então ele notou que seria necessário descobrir alguma forma de calcular o tamanho de um software - dessa forma,seria possível estimar quanto ele custaria. Naquela época, havia uma métrica muito comum chamadaLinhas de Código (Unes ofCode - LOC). Como funcionava?

Basicamente essa métrica calculava a quantidade de linhas possuía o código-fonte de um software.Qual é o problema disso? \-\á dezenas de desvantagens, dentre as quais: por vezes, códigos eficientes são escritos em menos linhas1; a codificação em si corresponde a apenas cerca de 30% do esforço
1 Algumas pesquisas mostram que um programador altamente qualificado pode escrever menos linha de código para desenvolver a mesma total de desenvolvimento de um software; além disso, linguagens de programação diferentes podem ser mais ou menos verbosas.
Esse último ponto é interessante de explicar para que vocês entendam como essa não é uma boa métrica! Vejam o lema do Estratégia Concursos escrito em diversas linguagens:
LÍNGUA | FRASE |
QUANTIDADE DE CARACTERES

O segredo do sucesso é a constância no objetivo

The secret of success is constancy in the goal

Das Erfolgsgeheimnis ist Konstanz im Ziel
4i

CekpeTycnexa - HoCToAHCTBo B u,e/in

No desenvolvimento de software, ocorre de maneira bastante similar: algumas linguagens são mais verbosas e outras são mais sintéticas. O exemplo a seguir mostra quatro linguagens de programação executando uma mesma atividade, qual seja, a de escrever na tela "Olá,Mundo!".
Percebam como as linguagens JavaScript e Python são mais sintéticas enquanto as linguagensAssembly 8051 e C são mais verbosas.

LINGUAGEM JAVASCRIPT LINGUAGEM PYTHON

01 console.log("01á, Mundo!");
01 print "Olá, Mundo!"

01 Org 0

LINGUAGEM ASSEMBLY 8051 LINGUAGEM C

01 class HelloWorld

02 mov dptr,#msg

03 mov R0,#30h

04 loop:

05 clr a

06 move a,@a+dptr

07 jz end

08 mov @R0,a

09 inc R0

10 inc dptr

11 sjmp loop

12 end:

13 jmp $

14 msg:

15 db "Olá, Mundo!",0

02 {

03 static void Main()
04 {

05 System.Console.Writel_ine( "Olá, Mundo!");
06 }

07 }

Vocês já conseguem entender porque essa não é uma boa métrica para calcular ou estimar o tamanho de um software - uma mesma funcionalidade poderia custar quinze vezes a mais que a outra só por conta de linguagem de programação utilizada. Pois bem, Albretch precisava de algum critério chave que fosse de aplicação universal e que pudesse ser aplicado já nos primeiros estágios do ciclo de vida de desenvolvimento de um software.
Ele e sua equipe criaram uma técnica relativamente nova e estruturada para quantificação de software baseado principalmente na identificação consistente das capacidades desse software. Agrande quebra de paradigma dessa ideia foi se basear na visão usuário do software -
aspectos externos do software, isto é, suas funcionalidades. Esse pensamento significava que o'tamanho'
funcional era independente da tecnologia escolhida para implementação.

Ora, no exemplo das linguagens de programação apresentado anteriormente, o usuário visualiza apenas a funcionalidade de escrever "Olá, Mundo!" - o usuário não está ligando para a tecnologia utilizada. Dessa forma, nós temos a medida universal que tanto desejávamos. Amedição do tamanho funcional lida com a medição da quantidade de funcionalidade que o aplicativo de software fornece de fato ao usuário ou cliente. Bacana?
Dessa forma, podemos dizer que a análise de pontos de função é um método para dividir o aplicativo de software em componentes menores e medi-los em relação as suas funcionalidades para estimar o seu tamanho. A definição desse método agora é gerenciada peloInternational Function Point Users' Group (IFPUG)-organização sem fins lucrativos responsável por manter o Manual de Práticas de Contagem (CPM). O que é isso, Diego?
Trata-se de um conjunto de conhecimentos usado por analistas de pontos de função para medir o tamanho funcional de softwares - ele contém um conjunto de regras para quebrar um software em partes e contar seus pontos de função. Galera, esse foi apenas um contexto histórico para contar para vocês um pouco sobre a motivação para a criação dessa métrica criada na década de setenta, mas ainda vigente nos dias atuais. Fechado? Vamos seguir...
(TCE/SC - 2015) A métrica de contagem de pontos por função, disseminada pelo IFPUG
(InternationalFunction Point User Group) e constituída na evolução das métricas de linhas de código (LOC), visa estimar recursos para projetos de softwares orientados a objetos a partir de documentos de visão e de casos de uso.
Comentários: ele visa estimar 0 tamanho funcional de um software a partir do ponto de vista do usuário de forma independente de tecnologias, como 0 paradigma de programação orientado a objetos (Errado).
(STM - 2018) As funcionalidades são medidas sob o ponto de vista dos analistas responsáveis pela conceituação do sistema; a contagem em projetos de melhoria considera a exclusão de funcionalidades implementadas, bem como a inclusão de novas funcionalidades.
Comentários: não é sob 0 ponto de vista dos analistas - é sob 0 ponto de vista dos usuários
(Errado).

Ponto de Função

INCIDÊNCIA EM PROVA: BAIXA

O que é um Ponto de Função? Trata-se simplesmente de uma unidade de medida como outra qualquer, mas que mede o tamanho funcional de um software.
PESO TEMPO TEMPERATURA
TAMANHO DE SOFTWARE

QUILOGRAMA MINUTO CELSIUS
PONTO DE FUNÇÃO

O ponto de função é uma unidade de medida de software que quantifica funcionalidades fornecidas ao usuário com base em seu projeto lógico, baseado na visão do usuário e independente de tecnologia (Ex: linguagem de programação). Já a Análise de Pontos de Função (APF)é uma técnica que permite medir o tamanho funcional de um software independente de tecnologia e sob o ponto de vista dos requisitos funcionais dos usuários.
Vamos destrinchar melhor essa definição! O que seria um requisito funcional?
É basicamente qualquer função ou serviço executado ou fornecido pelo software! Por exemplo: eu quero que o software calcule o IMC de uma pessoa baseado em dados de altura e peso é um requisito funcional.E como se mede o tamanho dessa funcionalidade? Bem, agora você me pegou... realmente não existe uma maneira de medir o tamanho de uma funcionalidade diretamente.
Como assim, D/ego? Vocês devem se lembrar que a métrica de linhas de código conseguia medir diretamente o tamanho de um software baseado em sua dimensão física (quantidade de linhas de código), no entanto essa métrica não permitia comparações por conta de todas aquelas desvantagens que eu mencionei anteriormente. Logo, uma de suas vantagens era conseguir medir diretamente um software, mas uma de suas desvantagens eram as comparações.
A métrica de ponto de função é justamente o contrário: é excelente para realizar comparações,mas não é possível utilizá-la para calcular diretamente o tamanho de um software.
Diego, estou viajando... simplifica aí! É bem simples: vamos supor que eu te informe que a funcionalidade do IMCequivale a 500 linhas de código! Poxa, é algo que você consegue assimilar tranquilamente - basta contar a quantidade de linhas possui o código-fonte e você tem uma medida direta.
E se eu afirmo que a funcionalidade do IMC equivale a 25 pontos de função! Você consegue assimilar tranquilamente? Não, porque essa medição é dependente de diversas outras, logo dizemos que se trata de uma medição indireta. A métrica de pontos de função foi pensada como resultado da experiência de diversos especialistas sobre características de vários projetos de software similares executados no Dassado e cataloaados em dados históricos.
Eu sei que ainda está obscuro, então vamos ver outro exemplo hipotético! Imagine que o GovernoFederal deseja renovar a frota de carros da polícia legislativa. Para escolher o carro que será adquirido, basta escolher o mais barato? Não, trata-se de um carro de polícia que necessita de características bastante específicas e diversas. Como assim? Bem, o carro precisa ser potente,espaçoso, barato, discreto, resistente e estável.

Galera, existe alguma métrica capaz de avaliar diretamente todas essas características em conjunto?Não! No entanto, o Governo Federal poderia criar uma unidade de medida hipotética chamadaPonto de Carro (PC). O que vocês acham? Dessa forma, ele poderia atribuir pesos para cada uma dessas características mencionadas até chegar a um valor final para o veículo -exemplo: Sio,
Corolla e Hilux valem respectivamente 41, 48 e 37 Pontos de Carro.

POTÊNCIA
ESPAÇO
VALOR
DISCRIÇÃO
RESISTÊNCIA
ESTABILIDADE

TOTAL

6 POTÊNCIA

7 ESPAÇO

9 VALOR

8 DISCRIÇÃO

8 RESISTÊNCIA

10 ESTABILIDADE

48 TOTAL

Agora vem o pulo do gato... e se eu disser para vocês que 0 ponto de função funciona de forma parecida? Para calcular a quantidade de pontos de função de uma funcionalidade, diversos especialistas da área atribuíram pesos - de acordo com a sua complexidade -a cinco características ou componentes de software (que veremos mais à frente) com o intuito de quantificar seu tamanho funcional. Legal, não?
Galera, por que tudo isso é independente de tecnologia? Porque essa técnica busca medir o que o software faz e, não, como ele foi construído. Logo, ele é independente de linguagem de programação, ambiente de desenvolvimento, plataforma computacional, entre outros.Por fim, a definição diz que ele mede as funcionalidades requisitadas pelo usuário. Não caiam em nenhuma pegadinha: é sempre sob o ponto de vista do usuário!!!
O que isso significa? Isso significa basicamente que, se uma funcionalidade foi extremamente complexa de se implementar, o programador queimou o cérebro por uma semana para fazer,mas essa funcionalidade não é percebida diretamente pelo usuário durante a utilização do software,
então ela será solenemente ignorada na contagem não ajustada porque a análise de pontos de função se dá sempre sob o ponto de vista do usuário.
Porfim, vamos falar um pouquinho mais sobre métricas indiretas. Algumas vezes, órgãos públicos ou empresas privadas precisam contratar um programador. Eis que surge a dúvida: eu pago um salário fixo independente do que ele produzir ou eu pago somente pelo que ele efetivamente produzir?Bem, vocês sabem que um dos princípios da administração pública é a eficiência, logo uma abordagem interessante seria pagar por produtividade.
Legal, mas como seria esse cálculo? Na APF, a produtividade é expressa como o número de pontos de função implementados pelo programador por mês. Logo, se ele for um programador menos produtivo, receberá menos do que um programador bastante produtivo. Justo, não?Além da produtividade, é possível realizar outros cálculos baseado em pontos de função como esforço,tempo, custo, qualidade, entre outros. Fechado? Agora chegou o momento do meu desafio...

(SERPRO - 2013) Na análise por pontos de função, não são medidos o tempo de desenvolvimento nem a produtividade ou o esforço de desenvolvimento; a análise está condicionada ao ambiente de desenvolvimento usado.
Comentários: ela não está condicionada ao ambiente de desenvolvimento utilizado nem qualquer outra tecnologia, linguagem de programação, plataforma computacional, entre outros (Errado).
(TRE/BA - 2010) A precisão de estimativas de tamanho, que depende de informações que nem sempre estão disponíveis no início dos projetos, auxilia a discussão de contratos ou determinação da viabilidade do projeto em termos da análise de custos e benefícios.
Comentários: a análise de pontos de função - que é uma técnica de estimativa de tamanho funcional -
depende realmente de informações que nem sempre estão disponíveis no início de um projeto e auxilia bastante na discussão de contratos e determinação da viabilidade de um projeto como no exemplo do programador (Correto).
(DNIT-2013) O objetivo principal da Análise de Pontos de Função é:

a) verificar a fundamentação da funcionalidade de um software ou aplicativo.

b) medir a oportunidade qualitativa de um software ou aplicativo.

c) medir a funcionalidade de um software ou aplicativo.

d) simplificar a complexidade funcional de um software ou aplicativo.

e) medir a funcionalidade dos pontos de acesso à operacionalização de um software ou aplicativo.
Comentários: (a) Errado, não é verificar a fundamentação das funcionalidades - é medir seu tamanho;
(b) Errado, ele não mede qualidade diretamente; (c) Correto, ele mede a funcionalidade ou tamanho funcional de um software ou aplicativo; (d) Errado,esse item não faz qualquer sentido; (e) Errado, esse item não faz qualquer sentido (Letra C).

(TRT/iZj - 2016) A métrica Pontos de Função:

a) é utilizada em projetos de software estruturados, não se aplicando a projetos orientados a objetos.
b) apresenta, como um dos produtos finais, o documento de especificação de requisitos.

c) foi criada para atender projetos baseados em metodologias de desenvolvimento ágeis.
d) fornece uma avaliação aproximada do tamanho de um software com base na escala
FDD.

e) permite medir o tamanho do software por meio do uso de regras de contagem.

Comentários: (a) Errado, ela é utilizada em projetos de qualquer paradigma de programação - orientado a objetos,estruturados, etc; (b) Errado, esse é 0 resultado da engenharia de requisitos e, não, da análise de pontos de função; (c) Errado,foi criado para atender projetos baseados em quaisquer metodologias de desenvolvimento de software; (d) Errado, não existe nenhuma escala FDD; (e) Correto, ele permite medir 0 tamanho funcional de um software por meio do uso de regras de contagem sob 0 ponto de vista do usuário (Letra E).
(SUFRAMA - 2014) Um dos objetivos da APF é medir funções impactadas pelo desenvolvimento independentemente da tecnologia empregada.
Comentários: ela realmente mede funções ou funcionalidades de forma independente da tecnologia empregada (Correto)
Se você chegou até aqui e acha que está entendendo tudo, então eu tenho um desafio de perguntas e respostas para você. Caso você consiga respondê-las, é porque você está afiado...
QUAL É A DIFERENÇA ENTRE ANÁLISE DE PONTOS DE FUNÇÃO E PONTO DE FUNÇÃO?

Análise de Pontos de Função é uma técnica, enquanto o ponto de função é 0
resultado da aplicação dessa técnica.

0 QUE MEDE A MÉTRICA DE PONTO DE FUNÇÃO? SOB A PERSPECTIVA DE QUEM?

Ele mede 0 tamanho funcional de um software sob 0 ponto de vista do usuário -
0 que ele faz e, não, como ele faz.

A APF É DEPENDENTE DE ALGUMA TECNOLOGIA ESPECÍFICA?

Não, ela é completamente independente de tecnologia, plataforma, linguagem de programação, etc.
A APF MEDE DIRETAMENTE 0 ESFORÇO, PRODUTIVIDADE OU CUSTO DE UM SOFTWARE?

Não, mas é possível correlacionar essas variáveis à métrica de pontos de função.

Principais Benefícios

INCIDÊNCIA EM PROVA: BAIXÍSSIMA

As organizações usam pontos de função com diferentes propósitos. Podem-se destacar vários benefícios da aplicação da APF nas organizações:
PRINCIPAIS BENEFÍCIOS

Funciona como uma ferramenta para determinar o tamanho de um pacote adquirido, através da contagem de todas as funções incluídas (pode auxiliar no momento da venda de um sistema de software) e suporta a análise de produtividade e qualidade em conjunto com outras métricas como esforço, defeitos e custo.
Provê auxílio aos usuários na determinação dos benefícios de um pacote para sua organização, através da contagem das funções que especificamente correspondem aos seus requisitos. Ao avaliar o custo do pacote, o tamanho das funções que serão utilizadas, a produtividade e o custo da própria equipe, é possível analisar se vale a pena comprar ou fabricar.
Apoia o gerenciamento de escopo de projetos. Um desafio de todo gerente de projetos é controlar o aumento do escopo. Ao realizar estimativas e medições em cada fase do seu ciclo de vida, é possível determinar se os requisitos funcionais cresceram ou diminuíram; e se esta variação corresponde a novos requisitos ou aos existentes e que foram apenas mais detalhados.
Complementa o gerenciamento dos requisitos auxiliando na verificação da solidez e completeza dos requisitos especificados. O processo de contagem favorece uma análise sistemática e estruturada da especificação de requisitos e traz benefícios semelhantes ao de uma revisão em pares - basta lembrar que a contagem é baseada em requisitos do usuário.
Um meio de estimar custo e recursos para o desenvolvimento e manutenção de software. Através da realização de uma contagem ou estimativa de pontos de função no início do ciclo de vida de um projeto, é possível determinar seu tamanho funcional. Esta medida pode ser então utilizada como entrada para diversos modelos de estimativa de esforço, prazo e custo.
Uma ferramenta para fundamentar a negociação de contratos. Pode-se utilizar pontos de função para gerar diversos indicadores de níveis de serviço em contratos de desenvolvimento e manutenção de sistemas. Além disso,permite o estabelecimento de contratos a preço unitário, onde a unidade representa um bem tangível para o cliente - reduzindo riscos.
Um fator de normalização para comparação de software ou para a comparação da produtividade na utilização de diferentes técnicas. Diversas organizações, como o ISBSG, disponibilizam um imenso repositório de dados de projetos de software que permitem a realização de benchmarking com projetos similares do mercado e uma boa base de comparação.
INDO MAIS

FUNDO!

Enfatizo novamente que a Análise de Pontos de Função não mede diretamente esforço, produtividade, custo, qualidade, ENTRE OUTROS. No entanto, ela pode ser usada em conjunto com outras grandezas e dados históricos da organização para medir essas variáveis. Por exemplo: determinado programador desenvolve uma funcionalidade específica em 10 Horas/PF.
Pessoal, a análise de pontos de função pode ser aplicada em diversos domínios funcionais ou domínios de informação. O que é isso? É uma área de interesse (Ex: sistema de uma universidade,hospital, banco, etc). Ademais, a produtividade - diferente da funcionalidade - é dependente de tecnologia. Basta pensar que programar em Delphi é mais produtivo do que em Java que é mais produtivo do que em C.
Professor, como uma organização consegue saber qual deve ser a produtividade esperada para um projeto que ainda irá se iniciar? Bem, isso pode ocorrer de duas maneiras: ela pode manter um repositório privado com dados sobre seus projetos anteriores ou ela pode utilizar um repositório público com dados de diversos projetos para realizar essas estimativas. E existe esse repositório público?
Existem vários, sendo que o mais conhecido se chama International Software
Benchmarking
Standards Group (ISBSG). Ele contém mais de 6.000 projetos de diferentes tamanhos,complexidades, linguagens de programação, domínios de informação, entre outros. Dessa forma,é possível utilizá-lo para estimar futuras produtividades - sempre considerando o contexto de como os números foram obtidos.
Componentes Fundamentais

INCIDÊNCIA EM PROVA: ALTA

Pronto, agora vamos avançar mais em nosso estudo! Vocês devem se lembrar que eu disse anteriormente que - para medir uma funcionalidade - era necessário quantificar algumas características da aplicação de acordo com sua complexidade. Vocês se lembram da nossa métrica hipotética de Pontos de Carro? Lá, baseado na minha experiência, eu decidi que aqueles seis critérios deveriam ser utilizados para medir um carro.
Aqui a ideia é semelhante: nóstemos cinco funções, componentes ou características que devem ser consideradas no momento calcular o tamanho funcional de um software. As cinco funções são:Arquivo Lógico Interno (ALI); Arquivo de Interface Externa (AIE); Entrada
Externa (EE); Saída
Externa (SE); e Consulta Externa (CE). Essas funções se dividem basicamente em dois tipos: as funções de dados e as funções de transação - conforme apresenta o esquema a seguir:
Funções do Tipo Dado: representam requisitos de armazenamento do usuário. Galera,
quando vocês virem um ícone em formato de cilindro, provavelmente está representando algum mecanismo de armazenamento de dados. O termo arquivo aqui não significa arquivo físico ou tabela. Nesse caso, arquivo se refere a um grupo de dados logicamente relacionados e não à implementação física destes grupos de dados.
o ALI - Arquivo Lógico Interno o AIE-Arquivo de Interface Externa
Funções do Tipo Transação: representam requisitos de processamento do usuário.
Galera,
quando vocês virem uma seta, provavelmente está representando uma transação. Em outras palavras, uma transação trata de um processamento de criação, modificação ou exclusão de dados que estão armazenados em um arquivo lógico interno ou em um arquivo de interface externa.
o EE - Entrada Externa o CE - Consulta Externa o SE-Saída Externa
Há uma coisa que nós não mencionamos sobre a imagem anterior. O que, Diego? A
Fronteira da
Aplicação - trata-se de uma interface conceituai entre o software sob estudo e seus usuários.Galera, lembrem-se que em uma organização um software está geralmente integrado com vários outros softwares. Imagine um sistema de folha de pagamento, ele geralmente está integrado com o sistema de pessoal da organização.
Logo, quando eu for realizar a contagem de pontos de função do sistema de folha de pagamento,eu tenho que entender onde está a fronteira que o separa, por exemplo, do sistema de pessoal da organização. Logo, a fronteira de uma aplicação define o que é externo à aplicação;ela indica a fronteira entre o software que está sendo medido e o usuário; e ela atua como uma interface através da qual os dados processados pelas transações passam para dentro ou fora da aplicação.
É importante enfatizar que a fronteira é determina através do ponto de vista do usuário - o foco deve estar no que pode ser compreendido e descrito pelo usuário. Ela é baseada em funções empresariais separadas, da forma como são vistas pelos usuários e, não, através de necessidades tecnológicas. Se o usuário entender que o sistema de folha de pagamento e o sistema de pessoal é uma coisa só, então elas serão contadas como uma coisa só.
Vejam o esquema que representa uma aplicação de recursos humanos que possui funcionalidades como o cadastro de empregados, solicitação e apresentação de informações de um empregado,geração de relatórios sumarizados, cálculo de remuneração, entre outros. Notem também que essa linha pontilhada representa a fronteira da aplicação-tudo que está dentro é considerado interno e tudo que está fora é considerado externo à aplicação.
(IBGE-2016) A Análise de Pontos de Função é uma técnica que mede as funcionalidades de um software sob o ponto de vista do usuário, para determinar o tamanho funcional do software. Para aplicar a APF, Glaucia precisa definir um recurso com as seguintes características:
- age como uma membrana pela qual entram e saem os dados processados pelas transações da aplicação;
-contém os dados mantidos pela aplicação;

- ajuda a identificar os dados referenciados pela aplicação, definindo o que é interno e o que é externo.
Glaucia deve definir o(a):

a) Entrada Externa;

b) Consulta Externa;

c) Processo Elementar;

d) Fronteira da Aplicação;

e) Arquivo De Interface Externa.

Comentários: a questão trata da fronteira da aplicação (Letra D).

(MJ-2015) No âmbito da análise de pontos de função, as funções de dados representam as funcionalidades fornecidas ao usuário para atender requisitos internos e externos referentes a dados. De acordo com o IFPUG, são dois tipos de função de dados:
a) arquivo lógico externo e arquivo de interface interno.

b) arquivo lógico interno e arquivo lógico externo.

c) arquivo lógico interno e arquivo de interface externo.

d) arquivo de interface interno e arquivo de interface externo.

e) consulta externa e entrada externa.

Comentários: as funções de dados são Arquivo Lógico Interno e Arquivo de Interface Externo (Letra
C)

(UFPB - 2014) Quais são as funções de dados da análise de pontos de função?

a) Arquivo de Interface Externa (AIE) e Saída Externa (SE).

b) Arquivo Lógico Interno (ALI) e Arquivo de Interface Externa (AIE).

c) Arquivo Lógico Interno (ALI) e Saída Externa (SE).

d) Entrada Externa (EE) e Saída Externa (SE).

e) Entrada Externa (EE), Consulta Externa (CE) e Saída Externa (SE).

Comentários: as funções de dados são Arquivo Lógico Interno e Arquivo de Interface Externo (Letra
B).

Arquivo Lógico Interno (ALI)

INCIDÊNCIA EM PROVA: ALTA

Trata-se de um grupo de dados ou informações de controle logicamente relacionados,reconhecidos pelo usuário, mantidos dentro da fronteira da aplicação. Sua função é armazenar dados mantidos dentro da fronteira da aplicação. O Arquivo Lógico Interno contribui para o cálculo de pontos de função com base na quantidade e complexidade funcional relativa.Professor do céu... não entendi bulhufas!
Calma, seus lindos... vamos explicar essa definição tim-tim por tim-tim! O que é um grupo de dados ou informações de controle1 logicamente relacionados? São dados que não podem ser subdivididos sem perda de significado ou sentido. Por exemplo: os itens de uma nota fiscal estão intimamente conectados ao seu cabeçalho de tal forma que eles não fazem sentido se entendidos separadamente. E o que quer dizer 'reconhecidos pelo usuário'?
Galera, isso significa apenas que são requisitos que foram acordados entre o usuário e o desenvolvedor do software - sempre sob o ponto de vista do usuário. E o que significa mantidos dentro da fronteira da aplicação? Significa que são dados que podem ser lidos, incluídos,modificados ou excluídos por meio de uma ou mais transações. Professor Diego,
as coisas começaram a clarear, mas você pode dar um exemplo?
1 dados que influenciam um processo elementar da aplicação sendo contada. Especifica o que, quando ou como os dados devem ser processados, e
Vejam esse formulário do nosso sistema de recursos humanos hipotético. Observem que nós temos alguns campos para o cadastro de um funcionário. Galera, nós temos um grupo de dados ou informações de controle logicamente relacionados? Sim, notem que os dados de nome,telefone,
endereço ou estado civil de forma isolada não têm significado. Além disso, são certamente dados reconhecidos pelo usuário que requisitou o sistema.
Por fim, será que esses dados são mantidos dentro da fronteira da aplicação? Ora,
dados cadastrais de funcionários são dados que fazem todo sentido de serem mantidos pelo próprio sistema de recursos humanos e, não, por outro sistema. Logo, provavelmente estamos tratando de um arquivo lógico interno. Galera, agora segue a dica: em geral, um arquivo lógico interno é uma tabela ou conjunto de tabelas físicas armazenadas em um banco de dados.
Não é sempre, professor? Não, pessoal! Lembrem-se que o conceito de funções de dados e funções de transação no contexto da análise de pontos de função é um conceito lógico - até por isso,chamamos de Arquivo Lógico Interno. Não se trata necessariamente de um conceito físico,
apesar de ser na maioria das vezes. Em nosso exemplo, provavelmente esses dados cadastrais são armazenados fisicamente em uma tabela que guarda dados de funcionários.
No entanto, isso não é obrigatório! Por que? Porque estamos tratando do conceito lógico de armazenar informações (não importa onde, apesar de normalmente ser em uma tabela do banco de dados). Entenderam, pessoal? Nós vamos ver a seguir alguns exemplos e não-exemplos de arquivos lógicos internos. Esses exemplos caem em prova, professor? Algumas vezes, sim- porém eu recomendo que vocês não tentem decorar esse tipo de coisa.
EXEMPLO DE ARQUIVO LÓGICO

INTERNO (ALI)

NÃO EXEMPLO DE ARQUIVO
LÓGICO INTERNO (AU)

Dados da aplicação (arquivos mestres, como cadastro de clientes); arquivos de dados de segurança da aplicação; arquivos de dados de auditoria; arquivos de mensagem de auxílio; arquivos de mensagens de erro; arquivo de cópia de segurança (só se para atender requisitos da aplicação; arquivo que sofra manutenção por mais de uma aplicação.
Arquivos temporários; arquivos de trabalho; arquivos de classificação; arquivos de cópia de segurança (backup); arquivos introduzidos somente por causa da tecnologia usada (Ex: arquivos de parâmetro para um software WFL, JCL, etc); operações de junção e projeção; arquivos de índices alternativos.
(Câmara de Belo Horizonte-2018) Em análise de pontos de função, uma função do tipo dado representa a funcionalidade fornecida pela aplicação do usuário, de maneira a atender às suas necessidades de dados internos e externos à aplicação, ou seja, eles estão representando os seus requisitos de armazenamento de dados e possuem duas classificações. Um grupo de dados ou informações de controle, identificável pelo usuário e logicamente relacionado, se refere a características comuns às duas classificações.Entretanto, uma dessas classificações possui como característica ser mantido na fronteira da aplicação; assinale-a.
a) Arquivo Referenciado.

b) Arquivo Lógico Interno.

c) Arquivo de Interface Interna.

d) Arquivo de Interface Externa.

Comentários: tanto Arquivos Lógicos Internos quanto Arquivos de Interface Externas são considerados um grupo de dados ou informações de controle, identificável pelo usuário e logicamente relacionado, no entanto aquele que tem como característica ser mantido na fronteira da aplicação é o Arquivo Lógico Interno (Letra B).
(TRE/PA - 2010) Arquivos de sistema são considerados na contagem de pontos de função como arquivo lógico interno (ALI) somente se forem requisitados para procedimentos normais de backup e recuperação.
Comentários: arquivos de cópia de segurança (backup) não são considerados ALI. Professor, vou ter que decorar tudo isso? Não,essa é aquela famosa questão que você pula feliz (Errado).

(CGU - 2006) Na Análise de Ponto por Função, para que uma determinada função seja contada como um Arquivo Lógico Interno (ALI), algumas regras devem ser atendidas.Uma dessas regras visa a garantir que o grupo de dados:

a) é referenciado pela aplicação contada, porém é mantido fora da sua fronteira.

b) não é referenciado pela aplicação contada e deve ser mantido fora da sua fronteira.

c) não participa de nenhum tipo de relacionamento com o usuário.

d) é mantido por outra aplicação, porém é considerado um ALI nesta outra aplicação.

e) ou informações de controle é logicamente relacionado e identificável pelo usuário.

Comentários: (a) Errado, é mantido dentro da sua fronteira; (b) Errado, é mantido pela aplicação contada e deve ser mantido dentro de sua fronteira; (c) Errado, eles devem sempre ser reconhecidos pelo usuário; (d) Errado, é mantido pela aplicação sendo contada; (e) Correto, é a definição clássica: grupo de dados ou informações de controle logicamente relacionadas e reconhecidas/identificáveis pelo usuário (Letra E).
(CORREIOS - 2011) Um arquivo lógico interno (ALI) é utilizado para o armazenamento de dados de arquivos temporários, que são gerados para processamento em outra aplicação.
Comentários: arquivos temporários não são considerados Arquivo Lógico Interno (Errado).

(TCE/PA - 2016) Arquivo lógico interno (ALI) é um grupo de dados logicamente relacionados, reconhecidos pelos usuários, mantidos por meio de um processo elementar de outra aplicação e referenciado pela aplicação que está sendo contada.
Comentários: ele é mantido por meio de processos elementares dentro da fronteira da aplicação - a questão faz referência aoArquivo de Interface Externa (Errado)

Arquivo de Interface Externa (AIE)

INCIDÊNCIA EM PROVA: ALTA

Trata-se de um grupo de dados ou informações de controle logicamente relacionados,reconhecidos pelo usuário, mantidos dentro da fronteira de outra aplicação (externa) -
os dados são armazenados fora da fronteira da aplicação. Sua principal intenção é a de armazenar dados referenciados da aplicação sendo contada. Dessa forma, um arquivo de interface externa de uma aplicação sempre será contado como um arquivo lógico interno de outra aplicação.
APLICAÇÃO DE SOFTWARE 1 APLICAÇÃO DE
SOFTWARE 2

I

I

Deixe-me enfatizar isso mais uma vez, tendo em vista que isso já caiu umas... sei lá... seiscentos e cinquenta milhões de vezes em prova! Se um arquivo de interface externa é mantido por outra aplicação, logo ele obrigatoriamente será um ALI naquela aplicação. O que eu quero dizer com isso? O AIE da Aplicação de Software 1 é um ALI da Aplicação de Software 2 - sendo que nunca um arquivo será contado como ALI e AIE simultaneamente na mesma aplicação.
Galera, vocês se lembram do nosso esquema do sistema de recursos humanos hipotético?
Havia dois sistemas, sendo que o outro era o Sistema Monetário. Essa interação com esse sistema pode ser porque o sistema de recursos humanos precisa calcular alguma verba indenizatória atrasada de um funcionário e quer realizar o pagamento com os juros e correções baseado nos dados da inflação dos últimos meses, por exemplo, contidos no sistema monetário.
Porque o sistema monetário é um arquivo de interface externa? Porque se trata de um grupo de dados logicamente relacionados, reconhecidos pelo usuário e mantidos dentro da fronteira de outra aplicação - no caso, o sistema monetário. Galera, se os dados são mantidos fora da fronteira da aplicação sendo contada, isso significa que por meio da aplicação de recursos humanos não é possível inserir, modificar ou excluir dados do sistema monetário - apenas consultá-los.
EXEMPLO DE ARQUIVO DE
INTERFACE EXTERNA (AIE)

NÃO EXEMPLO DE ARQUIVO DE
INTERFACE EXTERNA (AIE)

Arquivos de mensagens de auxílio; arquivos de mensagens de erro.

Dados recebidos de outra aplicação usados para adicionar, alterar ou remover dados em um ALI; dados cuja manutenção éfeita pela aplicação que está sendo avaliada, mas que são acessados e utilizados por outra aplicação; dados formatados e processados para uso por outra aplicação.
(IBGE - 2017) A Análise de Pontos de Função (APF) é uma técnica para a medição de software que estabelece uma medida de tamanho independente da linguagem de programação ou da tecnologia utilizada em seu desenvolvimento.
No processo de contagem de pontos de função, um grupo de dados logicamente relacionados ou informações de controle, identificado pelo usuário, requerido para referência ou validação pelo software que está sendo contado e cuja manutenção é feita por outra aplicação é denominado:
a) Arquivos Lógicos Internos;

b) Arquivos de Interface Externa;

c) Entradas Externas;

d) Saídas Externas;

e) Consultas Externas.

Comentários: grupo de dados mantido por outra aplicação é 0 AIE (Letra B).

(DATAPREV - 2012) O agrupamento lógico de dados relacionados ou informações de controle referenciadas por uma aplicação e que residem dentro dos limites de uma outra aplicação é um:
a) Arquivo de interface externa b) Arquivo de lógica externa c) Arquivo de saída lógica d) Arquivo de entrada externa.
e) Arquivo de saída externa.

Comentários: referenciadas por uma aplicação e que residem dentro dos limites de uma outra aplicação é um Arquivo deInterface Externa (Letra A).

(Correios - 2011) Um arquivo de interface externa é obrigatoriamente um ALI de outra aplicação.
Comentários: um arquivo de interface externa sempre será um arquivo lógico interno de outra aplicação (Correto).
(MEC - 2011) O arquivo de interface externa, que armazena dados referenciados, é um tipo de função de dados lidos e mantidos pela aplicação.
Comentários: eles são lidos e mantidos fora da fronteira da aplicação (Errado).

Entrada Externa (EE)

INCIDÊNCIA EM PROVA: ALTA

Trata-se de um processo elementar que processa dados ou informações de controle recebidos de fora da fronteira da aplicação e cujo objetivo é manter um ou mais arquivos lógicos internos e/ou alterar o comportamento do sistema. Uma EE provoca uma inclusão, exclusão e/ou alteração nos dados do arquivo lógico interno. Cada EE se origina de um usuário ou é transmitida de outra aplicação e fornece dados distintos orientados à aplicação ou informação de controle.
O que é um processo elementar? Trata-se da menor unidade de atividade que é significativa para o usuário - ela deve ser independente e deixar a aplicação em um estado consistente.Parece complexo, mas é muito simples-processo elementaré sinônimo detransação. Em outras palavras,é uma atividade ou funcionalidade que a aplicação fornece ao usuário para processar dados - em geral usa verbos como: incluir, alterar, excluir, editar, registrar, gravar, carregar, etc.
Galera, o formulário de cadastro de funcionário que nós vimos anteriormente corresponde a umaEntrada Externa, porque os dados inseridos serão enviados para a aplicação com o propósito de manter o arquivo lógico interno de funcionários. Apesar de a intenção primária da entrada externa seja manter um arquivo lógico interno, por vezes a intenção pode ser apenas alterar o comportamento do sistema. Como é, Diego? Vamos voltar ao nosso sistema hipotético...
Se eu preencho um formulário de funcionários que contém nome, data de nascimento e número de identidade, esses dados serão simplesmente inseridos no banco de dados sem nenhum tipo de cálculo adicional. No entanto, se eu preencho esse mesmo formulário, mas após inserir há um processamento que - por meio da data de nascimento - calcula e insere no banco de dados a idade do funcionário, eu estou alterando o comportamento do sistema.
Na realidade, eu posso manter arquivos lógicos internos sem alterar o comportamento do sistema como também posso alterar o comportamento do sistema sem manter arquivos lógicos internos. Ficou claro? Dito isso, as funções de transação seguem uma regrinha básica a respeito da alteração do comportamento do sistema que eu gostaria muito que vocês guardassem para toda a vida. Ela diz algo mais ou menos assim:
SAÍDA EXTERNA ENTRADA EXTERNA CONSULTA
EXTERNA

SEMPRE ALTERA 0 COMPORTAMENTO DO SISTEMA PODE ALTERAR 0 COMPORTAMENTO 00 SISTEMA NUNCA ALTERA 0
COMPORTAMENTO DO SISTEMA

EXEMPLO DE ENTRADA

_ _ _ _ _ _ _ EXTERNA (EE)
NÃO EXEMPLO DE ENTRADA

EXTERNA (EE)

Operações de inclusões e alterações de registros em arquivos da aplicação, janelas que permitem adicionar, excluir e alterar registros em arquivos de dados.
Menus, telas de login, telas de filtro de relatórios e consultas, múltiplos métodos de se executar uma mesma lógica de entrada, entre outros.
(TCU - 2015) Imprimir um cheque e identificá-lo como pago na conta-corrente será considerado um processo elementar se, juntas, essas atividades corresponderem à menor unidade da atividade significativa para o usuário.
Comentários: somente será um processo elementar se essas atividades realmente corresponderem à menor unidade da atividade significativa para 0 usuário (Correto).
(Prefeitura de Niterói - 2018) A análise de pontos de função é uma técnica para medir o tamanho funcional de um software do ponto de vista do usuário. No processo de contagem dos pontos de função, as transações que processam dados ou informações de controle originados de fora da fronteira da aplicação são classificadas como:
a) arquivo lógico interno.

b) arquivo de interface externa.

c) entrada externa.

d) saída externa.

e) consulta externa.

Comentários: transações que processam dados ou informações de controle originados de fora da fronteira da aplicação são classificadas como entrada externa (Letra C).
(TCE-SP - 2015) A análise por pontos de função constitui uma técnica utilizada para medição da estimativa de esforço no desenvolvimento de software. Um dos tipos de componentes básicos dessa análise introduz dados externos para dentro do domínio do software sob análise. Esse componente é denominado:
a) consultas externas.

b) entradas externas.

c) medidas externas.

d) números externos.

e) saídas externas.

Comentários: esse componente que introduz dados externos para dentro do domínio do software sob análise é a entrada externa (Letra B).
(MEC - 2011) Na análise por pontos de função, as transações que podem alterar o comportamento do sistema sem que os arquivos lógicos internos sejam modificados denominam-se função do tipo transação entrada externa (EE).
Comentários: entrada externa é um processo elementar que processa dados ou informações de controle recebidos de fora da fronteira da aplicação e cujo objetivo é manter um ou mais arquivos lógicos internos e/ou alterar o comportamento do sistema. Logo, entradas externas podem alterar o comportamento do sistema sem que haja modificações dos arquivos lógicos internos (Correto).
Saída Externa (SE)

INCIDÊNCIA EM PROVA: ALTA

Trata-se do processo elementar que envia dados ou informações de controle para fora da fronteira da aplicação. Seu objetivo é exibir informações recuperadas através de processamento lógico que envolva cálculos ou criação de dados derivados e não apenas uma simples recuperação de dados. Uma saída externa pode manter um arquivo lógico interno e/ou alterar o comportamento do sistema.
Representam atividades do sistema que transforma dados do arquivo lógico interno e gera resultados ao usuário. A ideia aqui é o seguinte: na entrada externa, você -que está fora da fronteira da aplicação - entra com dados no sistema; na saída externa, os dados saem do sistema e vão para fora da fronteira da aplicação. É justamente o inverso! Então, o usuário faz alguma consulta, ocorre um cálculo interno e informações são retornadas ao usuário.
Vamos supor que agora eu não quero mais inserir um funcionário no sistema de recursos humanos
- agora eu quero consultar todos os funcionários com o nome Jorge. Se essa consulta de dados retornar para fora da fronteira da aplicação um relatório com todos os funcionários com nome Jorge e realizar algum cálculo (Ex: a soma dos funcionários com esse nome), então nós teremos uma saída externa.
Nós veremos a seguir a consulta externa, mas eu já adianto que a única diferença é que a consulta externa não realiza nenhum cálculo - ela apenas retornaria o nome dos funcionários chamadosJorge sem somatório algum. Nunca se esqueçam da nossa regrinha básica: da mesma forma que entradas externas podem alterar o comportamento do sistema (sem obrigatoriedade),a saída externa sempre altera o comportamento do sistema. Fechou?
SAÍDA EXTERNA ENTRADA EXTERNA
CONSULTA EXTERNA

SEMPRE ALTERA 0 COMPORTAMENTO DO SISTEMA PODE ALTERAR 0 COMPORTAMENTO 00 SISTEMA NUNCA ALTERA 0
COMPORTAMENTO DO SISTEMA

EXEMPLO DE SAÍDA
EXTERNA (SE)

NÃO EXEMPLO DE SAÍDA

EXTERNA (SE)

Dados transferidos para outra aplicação; relatórios; relatórios online;
gráficos; gerador de relatórios.

Telas de ajuda; literais; data, hora, controles de paginação, etc; relatórios múlti com a mesma lógica e formato; relatórios criados pelo usuário de forma dinâmica usuário usando uma linguagem como SQL.
(ITAIPU BINACIONAL - 2015) No que diz respeito à técnica Pontos por Função,
a definição "correspondem a transações cujo objetivo é a apresentação de informações aos usuários, não necessariamente provenientes de arquivos, podendo ocorrer a geração de dados derivados, atualização de arquivos e a utilização de cálculos/fórmulas" se refere a:
a) Arquivos Lógicos Internos.

b) Arquivos de Interface Externa.

c) Entradas Externas.

d) Saídas Externas.

e) Consultas Externas.

Comentários: apresentação de informações ao usuário podendo ocorrera geração de dados derivados,
atualização de arquivos e a utilização de cálculos/fórmulas é uma saída externa (Letra D).
(FINEP - 2014) Em um sistema de acompanhamento de empréstimos, um processo elementar tem como finalidade principal apresentar ao usuário um relatório, com cálculos on line, do valor presente e dos valores futuros de um empréstimo, para um período e uma taxa de juros fornecidos pelo usuário.
De acordo com a prática de contagem de pontos de funções, devemos caracterizar essa função como um(a):
a) arquivo lógico interno b) arquivo de interface externa c) saída externa d) entrada externa e) consulta externa
Comentários: apresentar ao usuário um relatório, com cálculos online, do valor presente e dos valores futuros de um empréstimo, para um período e uma taxa de juros fornecidos pelo usuário é uma saída externa (LetraC).

(BNDES - 2008) O sistema de cadastro de eventos de uma empresa de consultoria em
TI dispõe de uma tela que lista as palestras gratuitas realizadas no mês, ordenadas por dia, com totalização. No contexto de Análise de Pontos de Função, essa tela do sistema é contada como:
a) Consulta Externa (CE), pois não há dados derivados.

b) Consulta Externa (CE), pois há totalização de dados.

c) Arquivo Lógico Interno (ALI), já que os dados foram extraídos de um arquivo referenciado.
d) Saída Externa (SE), pois há dados derivados.

e) Entrada Externa (EE), já que existe mudança de comportamento do sistema.

Comentários: dispõe em tela, isto é, apresenta ao usuário uma lista de palestras gratuitas realizadas no mês, ordenadas por dia,com totalização-trata-se de uma Saída Externa porque há dados derivados. Quais? A totalização das palestras é derivada da soma da quantidade de palestras (Letra D).
Consulta Externa (CE)

INCIDÊNCIA EM PROVA: ALTA

Trata-se do processo elementar que envia dados ou informações de controle para fora da fronteira da aplicação. Seu objetivo é apresentar informação o usuário por meio de uma simples recuperação de dados de um arquivo lógico interno ou arquivo de interface externa. A lógica de processamento não deve conter cálculo matemático, criar dados derivados, atualizar nenhum arquivo lógico interno e/ou alterar o comportamento do sistema.
Pode ser definida como uma entrada online que resulta na geração de alguma resposta imediata do software sob a forma de uma saída online. Só para não esquecer, vamos à nossa regra:
SAÍDA EXTERNA ENTRADA EXTERNA
CONSULTA EXTERNA

SEMPRE ALTERA 0 COMPORTAMENTO DO SISTEMA PODE ALTERAR 0 COMPORTAMENTO 00 SISTEMA
NUNCA ALTERA 0 COMPORTAMENTO 00 SISTEMA

EXEMPLO DE
CONSULTA EXTERNA (CE]

NÃO EXEMPLO DE
CONSULTA EXTERNA (CE]

Telas de logon, telas de help, telas de alteração/remoção que mostram o que alterado ou removido antes de sua efetivação; tela de menus que permitem info parâmetros para a consulta na tela escolhida.
Dados derivados; documentação online; sistema de teste; sistemas relatórios e consultas (c/ cálculo).
(SUFRAMA - 2014) Na APF, uma consulta externa não precisa ter referência de um arquivo lógico interno (ALI) ou externo (ALE).
Comentários: ela precisa recuperar dados de um arquivo lógico interno ou de um arquivo de interface externa - a sigla correta é AIE (Errado).
(ANP - 2013) De acordo com a análise de pontos de função, um relatório que apresenta informações ao usuário por meio de uma simples recuperação de dados é considerado uma consulta externa.
Comentários: a recuperação simples de dados é uma Consulta Externa (Correto).

(MEC - 2011) Denominam-se consulta externa as funções do tipo transação que não fazem processamento nem alteram o comportamento do sistema.
Comentários: consulta externa realmente é uma função de transação que não faz nenhum processamento adicional - eu acredito a questão caberia recurso (Correto).
Etapas do Processo de Contagem

INCIDÊNCIA EM PROVA: BAIXA

O procedimento de contagem de pontos de função segue etapas bem definidas, no entanto aqui é importante falar um pouquinho sobre versões. Nós temos basicamente o IFPUG 4.2 (2005)e o
IFPUG 4.3 (2010). Professor, nós vamos estudar a versão mais atual, né? Não, nós vamos apenas mencionara versão maisatual, mas vamos nos focar na versão anterior. Por que? Porque nunca caiu nenhuma questão da versão atual e já caíram dezenas das etapas apresentadas a seguir:
Bem, não muda muita coisa entre as duas versões! Basicamente, a principal mudança trata das etapas do processo de contagem, sendo que a versão atual segue as seguintes etapas:
REUNIRA
DOCUMENTAÇÃO

DETERMINAR ESCOPO E
FRONTEIRA OA CONTAGEM.
IDENTIFICANDO REQUISITOS

CALCULAR
TAMANHO

DOCUMENTAR

FASES-IFPUG 4.2 (2005) FASES-IFPUG 4.3 (2010)

- REUNIR A
DOCUMENTAÇÃO

DETERMINAR 0 TIPO DE CONTAGEM
DETERMINAR 0 ESCOPO E FRONTEIRA
CALCULAR PONTOS DE FUNÇÃO NÃO AJUSTADOS
CALCULAR FATOR DE AJUSTE
CALCULAR PONTOS DE FUNÇÃO AJUSTADOS

DETERMINAR ESCOPO E FRONTEIRA DA CONTAGEM, IDENTIFICANDO
REQUISITOS FUNCIONAIS DO USUÃRIO

MEDIR FUNÇÕES DE DADOS/TRANSAÇÕES
CALCULAR TAMANHO FUNCIONAL
DOCUMENTAR E REPORTAR

Pessoal, as etapas são basicamente as mesmas, mas divididas de uma forma diferente. De toda forma, existem duas fases extras na última versão do processo de contagem. São elas:
Reunir a Documentação: trata-se da etapa que reúne toda a documentação disponível. Adocumentação de suporte de uma contagem deve descrever a funcionalidade entregue pelo software ou a funcionalidade impactada pelo projeto de software medido.
Documentar e Reportar: Trata-se da etapa em que a contagem de pontos de função deve ser documentada, registrando todas as informações anteriores (o propósito, o tipo da contagem, o escopo, a fronteira da aplicação, entre outros).
Vamos resumir: existem duas versões do IFPUG! A versão mais antiga é a mais cobrada até hoje e a versão mais recente nunca foi cobrada em prova. A grande diferença entre ambas está na organização das etapas do processo de contagem conforme visto na tabela acima. Além disso, a versão mais recente possui duas etapas a mais que a versão mais antiga. Por fim, nós vamos estudar de acordo com a versão mais antiga porque a versão mais nova nunca caiu em prova.
(SERPRO-2013) Na análise de pontos de função, a contagem dos pontos de função não ajustados precede a determinação do fator de ajuste.
Comentários: conforme podemos ver na imagem anterior, a contagem dos pontos de função não ajustados realmente prece a determinação do fator de ajuste (Correto).
(CNJ - 2013) A determinação do tipo de contagem é realizada após a identificação do escopo da contagem e fronteira da aplicação que será contada.
Comentários: ela é realizada antes da identificação do escopo e fronteira (Errado).

Determinar o Tipo de Contagem

INCIDÊNCIA EM PROVA: MÉDIA

O procedimento de contagem de pontos de função de um aplicativo que ainda será desenvolvido é diferente do procedimento de contagem de um aplicativo pronto. Bem como o procedimento de contagem de um aplicativo pronto difere do procedimento de contagem de manutenção de outro aplicativo. Galera, existem três tipos de contagem: projeto de desenvolvimento;projeto de manutenção ou melhoria; e projeto de aplicação ou produção.
TIPO DE CONTAGEM | DESCRIÇÃO

Mede a funcionalidade fornecida aos usuários finais do software quando da primeira instalação entregue quando 0 projeto estiver pronto. Esta contagem também abrange as
PROJETO DE

DESENVOLVIMENTO

funções de conversão de dados que serão precisas para a implantação do software. Como exemplo defunção de conversão de dados pode-se citara necessidade de importardados de um sistema antigo para 0 sistema em implantação.
PROJETO DE
MANUTENÇÃO/MELHORIA

PROJETO DE
APLICAÇÃO/PRODUÇÃO

Mede as modificações realizadas para aplicações existentes, isto é, funções adicionais -
modificadas ou excluídas do sistema pelo projeto e as funções de conversão de dados.
Após a conclusão e implantação do projeto de manutenção, 0 número de pontos de função da aplicação deve seratualizado para refletiras mudanças nas funcionalidades da aplicação. As manutenções podem ser somente evolutivas e, não,corretivas e preventivas.
Mede uma aplicação instalada e em pleno funcionamento. É também referenciada como contagem de baseline ou contagem instalada e avalia as funcionalidades correntes providas aos usuários finais da aplicação. Ela não é estimativa, é bastante precisa, na medida em que 0 aplicativo já está pronto e em funcionamento. Ela é iniciada ao final da contagem do projeto de desenvolvimento e atualizado no final do projeto de melhoria.
(TCE/AP-2012) Um dos primeiros passos para efetuara contagem porpontos defunção de um sistema, é definir o tipo de contagem que será efetuado. Esses tipos se dividem em:
a) entrada, saída e processamento.

b) requisitos, elaboração e testes.

c) desenvolvimento, manutenção e aplicação.

d) controle, mecanismo e processamento e) lógico, físico e modelagem.
Comentários: trata-se da contagem de desenvolvimento, manutenção/melhoria e aplicação/produção
(Letra C).

(MJ - 2015) Existem tipos de contagem de ponto de função diferentes que devem ser aplicados de acordo com o propósito da contagem. OIFPUG define os seguintes tipos de contagem de pontos de função:
a) evolutiva, corretiva e ajuste.

b) corretiva, desenvolvimento e melhoria.

c) inicial, parcial e final.

d) aplicação, evolutiva e ajuste.

e) desenvolvimento, melhoria e aplicação.

Comentários: trata-se da contagem de desenvolvimento, manutenção/melhoria e aplicação/produção
(Letra E).

(EBSERH - 2017) O primeiro passo a ser seguido para a contagem de PF (Pontos de
Função) de um projeto de software é determinar o tipo de contagem. Neste passo é estabelecido o tipo de contagem que será usado para medir o projeto de software, tanto no processo como no produto. Assinale a alternativa que apresenta três tipos de contagem possíveis:
a) do projeto de integração, do projeto de melhoria (manutenção), de depuração (testes)

b) do projeto de desenvolvimento, do projeto de requerimentos
(requisitos), da aplicação (produção)
c) do projeto de desenvolvimento, do projeto de melhoria (manutenção), da aplicação
(produção)

d) do projeto de integração, do projeto de requerimentos (requisitos), de depuração(testes)

e) do projeto de desenvolvimento, do projeto de requerimentos
(requisitos), de depuração (testes)
Comentários: trata-se da contagem de desenvolvimento, manutenção/melhoria e aplicação/produção
(Letra C).

(TRT/ES - 2013) Quando a primeira versão de um novo software de cadastro de funcionários de uma empresa é desenvolvido, sua contagem será do tipo Projeto deDesenvolvimento.

Comentários: na primeira versão teremos uma contagem do tipo projeto de desenvolvimento (Correto).

Determinar o Escopo e Fronteira

INCIDÊNCIA EM PROVA: MÉDIA

Após determinar o tipo de contagem, deve-se determinar o escopo e a fronteira da aplicação.A identificação do escopo visa definir a abrangência da contagem estipulando se ela referirá um ou mais sistemas ou a apenas parte de um sistema. Dessa forma, como exemplo,o escopo da contagem de uma aplicação pode abranger todas as funcionalidades disponíveis, algumas funcionalidades específicas ou apenas as funcionalidades utilizadas pelo usuário.
Nós já vimos um pouco sobre a fronteira da aplicação e sabemos que ela é responsável por separar a aplicação que está sendo contada das aplicações externas, indicando o limite entre a aplicação e os demais usuários. A fronteira é definida estabelecendo um limite lógico entre a aplicação que está sendo contada, o usuário e as outras aplicações. Ao identificar a fronteira da aplicação deve-se estabelecer alguns critérios. Quais, professor?

Deve-se estabelecer os limites entre as funções a serem atendidas pela aplicação ou projeto dimensionado e àquelas pertencentes ao ambiente externo; a propriedade dos dados considerados pelo processo de contagem; e o relacionamento entre os processos, com indicação de onde eles ocorrem. A identificação da fronteira é importante, pois um posicionamento incorreto pode levar a uma contagem incorreta dos pontos de função.
(ANP - 2013) A fronteira entre aplicações para efeito de contagem de pontos de função é definida de acordo com a tecnologia aplicada.
Comentários: a análise de pontos de função é independente de tecnologia. O que deve ser feito é considerar 0 ponto de vista do usuário, ou seja, 0 que 0 usuário pode entender e descrever como função da aplicação. Ademais, a fronteira entre aplicações relacionadas deve considerar a funcionalidade das aplicações em termos das funções de negócio identificadas pelo usuário, e não sob 0 ponto de vista das interfaces necessárias (Errado).
Calcular Pontos de Função Não-Ajustados

No cálculo de pontos de função não-ajustados, medem-se as funções de dados e as funções de transação. O Arquivo Lógico Interno armazena dados mantidos pela aplicação que está sendo medida, já o Arquivo de Interface Externa armazena dados referenciados pela aplicação que está sendo medida. Lembrem-se que nós já vimos dezenas de vezes que um AIE de uma aplicação é sempre ALI de outra aplicação!
No exemplo da imagem acima, tem-se um usuário (em preto) interagindo com um sistema
(em verde) e esse sistema interagindo com outro sistema (em cinza). A Entrada Externa ocorre quando um usuário inclui uma nota fiscal e o sistema processa a informação-alterando o comportamento da aplicação ou atualizando, editando, modificando, excluindo dados de um Arquivo LógicoInterno.

A Consulta Externa ocorre quando um usuário requisita uma lista de notas fiscais, o sistema apenas recupera os dados sem fazer qualquer tipo de processamento ou cálculos matemáticos. ASaída
Externa ocorre quando um usuário requisita um relatório sumarizado de notas fiscais, o sistema processa uma informação-fazendo algum tipo de cálculo matemático-e retorna para o usuário.
Agora eu preciso da atenção de vocês, porque essa parte é meio chatinha de entender! Vejam bem:
Todos os ALI/AIE são igualmente complexos? Não. Então, como se mede sua complexidade?
Pela quantidade de Dados Elementares Referenciados (DER) e Registros Lógicos Referenciados
(RLR). O que diabos é isso, professor? DER é um atributo único, reconhecido pelo usuário e não repetido, isto é, campos de uma tabela ou atributos de um objeto.
Por exemplo: na modelagem orientada a objetos, pode-se modelar um objeto Pessoa com diversos atributos (nome, idade, endereço, telefone, e-mail, etc). Cada atributo desses é um DadoElementar Referenciado! Simples, não? Já o RLR é um subgrupo de dados elementares referenciados, reconhecido pelos usuários dentro de um ALI/AIE. Pode traduzir,professor?
Claaaaaaaaro que sim...

Pelo exemplo anterior, consideramos o atributo Endereço como elementar, mas nós poderíamos ter considerado como um subgrupo de dados que pode ser dividido em Rua, Número,Cidade e CEP.
Nesse caso, o atributo Endereço deixa de ser um DER para se tornar um RLR. E quem decide isso,professor? O usuário - é sempre o usuário! De todo modo, vocês percebem que há um subgrupo de dados bastante óbvio no exemplo? O próprio objeto Pessoa é um subgrupo de dados.
Diante disso, podemos afirmar que toda função de dados tem pelo menos um RLR. As regras de contagem de um Registro Lógico Referenciado (RLR) são: (1) caso não haja subgrupo de informações (referentes a outro ALI), contar um RLR para cada ALI/AIE; (2) contar umRLR para cada subgrupo de dados de um ALI/AIE independentemente de ser o subgrupo opcional ou mandatório. Professor, 0 que seria um subgrupo opcional ou mandatário? Vamos ver...
Mandatórios: são subgrupos de dados que o usuário deve usar pelo menos uma vez durante o processo elementar de criação de um item num AIE.
Opcionais: são subgrupos de dados que o usuário tema opção de usar ou não durante o processo elementar de criação de um item em um AIE.
Agora alguns sinônimos: há provas que chamam Registro Lógico Referenciado de Item de
Registro ou, mais comumente, Tipo de Registro (TR). Há, também, provas que chamam DadosElementares
Referenciados de Item de Dados ou, mais comumente, Tipo de Dados (TD). Logo, fiquem atentos!Eu disse para vocês que o ALI/AIE são medidos por meio do DER/RLR. A
complexidade de cada função de dados é determinada de acordo com a tabela:
DADOS ELEMENTARES REFERENCIADOS (DER) OU TIPO DE DADOS (TD)

REGISTRO LÓGICO QUANTIDADE 1-19
20-50 >50
REFERENCIADO (RLR) 1 BAIXA
BAIXA MÉDIA
OU TIPO DE REGISTRO 2-5 BAIXA
MÉDIA ALTA

(TR) >5 MÉDIA
ALTA ALTA

Como se interpreta essa tabela? Funciona assim: caso seu arquivo tenha 3 RLRs e 80 DERs, ele terá complexidade alta (basta cruzar na tabela). Ok, mas para que eu quero saber qual a complexidade dele, professor? Porque você usará esse resultado em outra tabela, que vai te dizer qual o tamanho funcional do seu ALI/AIE por meio dessa complexidade, como pode ser visto na tabela abaixo:
COMPLEXIDADE FUNCIONAL
BAIXA

MÉDIA
ALTA

TIPOS DE DADOS

| ALI | AIE
|

Pronto, expliquei para vocês como funciona com o cálculo de complexidade das funções de dados.Agora vamos entender como funciona o de funções de transação. Vocês acham que CE/EE/SE
são igualmente complexos? Não. Então, como se mede sua complexidade? Pela quantidade deDados
Elementares Referenciados (DER) e a novidade: Arquivos Lógicos Referenciados (ALR).

Nós já vimos o DER! No entanto, aqui ele tem outro contexto: considera-se como o dado que atravessa a fronteira durante o processamento da transação. Já o ALR é um ALI/AIE que foi acessado por uma função de transação. Em outras palavras, quanto mais ALI/AIE acessados por uma função de transação, maior a complexidade do ALR. A complexidade daEE/SE/CE é determinada a seguir:
ENTRADA EXTERNA (EE) DADOS ELEMENTARES REFERENCIADOS (DER]

| QUANTIDADE 1-4 5-15
>15

ARQUIVO LÓGICO 0-1 BAIXA
BAIXA MÉDIA

REFERENCIADO (ALR) 2 BAIXA
MÉDIA ALTA

>2 MÉDIA ALTA
ALTA

SAÍDA EXTERNA (SE) / CONSULTA EXTERNA (CE) I DADOS ELEMENTARES
REFERENCIADOS (DER]

| QUANTIDADE 1-5 6-19
>19

ARQUIVO LÓGICO 0-1 BAIXA
BAIXA MÉDIA

REFERENCIADO (ALR] 2-3 BAIXA
MÉDIA ALTA

>3 MÉDIA ALTA
ALTA

Como interpreta essa tabela? Caso seu arquivo lógico acesse 1 ALRs e tenha 4 DERs,
ele terá complexidade baixa. Ok, mas para que eu quero saber qual a complexidade dele,professor? Porque você usará esse resultado em outra tabela, que vai dizer qual o tamanho funcional do seuCE/SE/EE por meio dessa complexidade, como pode ser visto na tabela abaixo:

COMPLEXIDADE FUNCIONAL
BAIXA

MÉDIA
ALTA

TIPOS DE TRANSAÇÃO |

| ENTRADA EXTERNA (EE) | SAÍDA EXTERNA (SE) | CONSULTA EXTERNA (CE) |

Pessoal, eu expliquei tudo isso para que vocês entendam o fundamento de onde vêm esses números, mas na prática vocês só precisam decorar a tabela a seguir:
FUNÇÕES DE DADOS E TRANSAÇÃO
CONSULTA EXTERNA (CE!

ENTRADA EXTERNA (EE)
SAÍDA EXTERNA (SE)
ARQUIVO DE INTERFACE EXTERNA (AIE)
ARQUIVO LÓGICA INTERNA (ALI)

COMPLEXIDADE FUNCIONAL |

| BAIXA | MÉDIA | ALTA |

Pessoal, nenhuma das outras tabelas precisa ser decorada, exceto essa última! Essa realmente não dá para fugir - vocês precisam decorar!Professor, isso é realmente importante para o entendimento geral de vocês sobre esse assunto? Claro que não! Isso é apenas um detalhe-vocês têm que decorar isso pelo simples fato de que isso cai muito em prova! Eu sei,é ridículo cobrar um decoreba desse! Mas o que eu posso fazer?
Infelizmente esse decoreba cai demais - muito mesmo. Por favor,
decorem, decorem, decorem...

Após definir a fronteira da aplicação, o tipo de contagem e o reconhecimento as funções de dados e de transação, pode-se calcular os Pontos de Função Não-Ajustados (PFNA) - chamados brutos -multiplicando-se o total de ALI, AIE, EE, SE, e CE pelas suas respectivas complexidades apresentadas na tabela que eu implorei para vocês decorarem. Para calcular,basta utilizar a fórmula a seguir-considerando que Quantidade = QT e a Complexidade = CP.
PFNA = [QT(ALI)xCP(ALI)J + [QT(AIE)xCP(AIE)J + [QT(EE)xCP(EE)] + [QT(SE)xCP(SE)] +
[QT(CE)xCP(CE)j

Vamos falar de alguns detalhes que raaaaaaaaramente caem em prova. Imaginem que o
Governo
Federal contratou uma empresa para fabricar um aplicativo e estimou que ele teria 1000 PFs.Porém, no momento de implantar o software, seria necessário fazer algumas conversões de dados. Como assim, professor? Bem, pode ser que tenha que se fazer alguma integração com sistemas existentes, sistemas legados ou outras adaptações.
Nós sabemos que isso tem um custo para a empresa fabricante do sistema, mesmo que não seja algo efetivamente para o software encomendado. Essas funções tem o nome de Funções deConversão e são descartadas logo após a implantação. O que eu quero dizer com isso tudo? Bem,
esse custo é repassado para o Governo Federal. Então, em Projetos de Desenvolvimento,
há uma fórmula para calcular o total de pontos de função: DFP = ADD + CFP.
DPF é o tamanho das funções de desenvolvimento; ADD é o tamanho das funções a serem entregues pelo projeto de desenvolvimento; e CFP é o tamanho das funções de conversão1. Nos casos de Projeto de Aplicação, não há o que se discutir: AFP = ADD. Em outras palavras, o tamanho total das funções de aplicação é equivalente a quantidade existente no momento da contagem,sem nenhuma função de conversão, porque o aplicativo já está implantado.

Por fim, em Projetos de Melhoria, a fórmula é um pouco mais complicada: EFP = ADD +
CHGA +
CFP + DEL. Pontos de Função de Melhoria é equivalente ao tamanho das funções adicionadas, mais o tamanho das funções alteradas, mais o tamanho das funções de conversão, mais o tamanho das funções excluídas. Bem pessoal... não é tão complicado, certo?/Vamos agora para a penúltima fase do processo de contagem de pontos de função: Cálculo do Fator de Ajuste!
(TRT/RJ - 2011) No processo de Análise de Pontos de Função - APF, aplicam-se os mesmos valores: 3, 4 e 6, correspondentes, respectivamente, aos níveis simples, médio e complexo, nos tipos de função:
a) entrada externa e saída externa.

b) entrada externa e consulta externa.

c) consulta externa e saída externa.

d) arquivo lógico interno e consulta externa.

e) arquivo lógico interno e arquivo de interface externa.

Comentários: se você decorou a nossa tabela, basta lembrar que esses são os valores para consulta externa e entrada externa.Intuitivamente daria para lembrar que as funções do tipo dado são mais complexas que funções do tipo transação! Além disso,CE/EE são menos complexas que SE. Logo, já daria para chutar (Letra B).

(TRE/AP - 2011) Na métrica de pontos de função, Entrada Externa de média complexidade e Arquivo Lógico Interno de alta complexidade valem, respectivamente,em pontos:

a)3e7-

1 Funções de conversão são aquelas funcionalidades providas apenas na instalação do sistema para converter dados ou proporcionar outros requisitos b) 3 e io.
c) 4 e io.

d) 4ei5.

e) 5ei5.

Comentários: mais uma vez, vocês teriam que lembrar da tabelinha. Logo, descobririam que EE Média =
4 e ALI Alta = 15 (Letra
D).

(PETROQUÍMICA/SUAPE - 2012) Um analista, seguindo o Processo de Contagem de
Pontos de Função para um sistema novo, considerado pequeno, identificou 5 entradas externas, 3 saídas externas e 5 arquivos lógicos internos. Verificando a complexidade,tanto das funções de transação quanto das funções de dados, determinou que todas deveriam ser consideradas com o grau de complexidade funcional baixo.
Com apenas essa informação, quantos pontos de função não ajustados ele encontrou?

a) 52

b) 62

c) 65

d) 67

e) 87

Comentários: sabe-se que temos 5EE, 3SE e 5ALI - ademais, todos possuem grau de complexidade funcional baixo. Dessa forma, se lembrarmos da tabelinha, veremos que EE Baixo = 3, SE Baixo = 4 e ALI Baixo = 7. Então,agora basta fazer a conta:
5*3 + 3*4 + 5*7 = 15+12+35 = 59 (Letra B).

(TRE/PE - 2017) Com relação ao processo de contagem de pontos de função, assinale a opção correspondente à etapa responsável por reconhecer a complexidade e a contribuição de cada uma das funções contadas.
a) Calcular os pontos de função não ajustados.

b) Contar as funções transacionais.

c) Identificar o escopo de contagem e a fronteira da aplicação.

d) Determinar a contagem de pontos de função não ajustados.

e) Determinar o valor do fator de ajuste.

Comentários: a etapa responsável por reconhecer a complexidade e a contribuição de cada uma das funções contadas é a terceira: calcular pontos de função não-ajustados ou determinar a contagem de pontos de função não ajustados. Logo, a questão possui duas respostas, mas infelizmente não foi anulada (Letra A).
Calcular Fator de Ajuste

INCIDÊNCIA EM PROVA: MÉDIA

Nesta etapa, nós vamos calcular o fator de ajuste. O que é isso, Diegão? Cara, a técnica de análise por pontos de função considera que alguns fatores - que estão relacionados com características da aplicação - podem afetar o tamanho funcional de um sistema. No cálculo dos PFNA não é levada em conta a tecnologia usada nem os requisitos não funcionais. E nós sabemos que há certas características que devem ser consideradas para se obter maior precisão sobre o cálculo.
Por essa razão, essas características são quantificadas de modo a obter um valor chamado Valor doFator de Ajuste (VFA) baseado em 14 características gerais de sistema (14 CGS). São elas:

01 - COMUNICAÇÃO DE DADOS

02-PROCESSAMENTO DISTRIBUÍDO

03-PERFORMANCE

04-CONFIGURAÇÃO DO EQUIPAMENTO

05-VOLUME DE TRANSAÇÕES

06-ENTRADA DE DADOS ONLINE

07-INTERFACE C0M0 USUÁRIO

14 CARACTERÍSTICA GERAIS DO SISTEMA (CGS]

08-ATUALIZAÇÃO ONLINE

09-PROCESSAMENTO COMPLEXO

10- REUSABILIDADE

11- FACILIDADE DE IMPLANTAÇÃO

12- FACILIDADE OPERACIONAL

13- MÚLTIPLOS LOCAIS

14- FACILIDADE DE MUDANÇAS

Esses valores ajudam a encontrar o tamanho funcional do sistema de uma forma mais exata. Vamos ver agora o que significa cada uma dessas características:
CARACTERÍSTICA | DESCRIÇÃO

Descreve o grau pelo qual a aplicação comunica-se diretamente com o processador. Os dados
COMUNICAÇÃO DE

DADOS

ou informações de controle utilizados pela aplicação são enviados ou recebidos por meio de recursos de comunicação.
PROCESSAMENTO
DISTRIBUÍDO

Descreve o grau pelo qual a aplicação transfere dados entre seus componentes.

PERFORMANCE

CONFIGURAÇÃO D0
EQUIPAMENTO

VOLUME DE
TRANSAÇÕES

Descreve o grau pelo qual considerações de tempo de resposta e performance de throughput influenciam o desenvolvimento da aplicação. Os objetivos estabelecidos ou aprovados pelo usuário, em termos de tempo de resposta ou taxa de transações, influenciam o projeto,desenvolvimento, instalação e suporte da aplicação.

Descreve o grau pelo qual as restrições de recursos computacionais influenciam o desenvolvimento da aplicação. Uma configuração operacional altamente utilizada,necessitando de considerações especiais de projeto, é uma característica da aplicação.
Exemplo:
usuário deseja executar a aplicação em um equipamento já existente e que será altamente utilizado.
Descreve em que nível o alto volume de transações de negócio influencia o projeto,desenvolvimento, instalação e suporte da aplicação.

ENTRADA DE
DADOS ONLINE

INTERFACE COMO

USUÁRIO

ATUALIZAÇÃO

ONLINE

PROCESSAMENTO

COMPLEXO

REUSABILIDADE

FACILIDADE DE
IMPLANTAÇÃO

FACILIDADE
OPERACIONAL

MÚLTIPLOS

LOCAIS

FACILIDADE DE
MUDANÇAS

Descreve o grau pelo qual dados são informados pela execução de transações interativas.

Descreve em que nível considerações sobre fatores humanos e facilidade de uso pelo usuário final influenciam o desenvolvimento da aplicação. As funções interativas fornecidas pela aplicação enfatizam um projeto para o aumento da eficiência do usuário final.
Descreve o grau pelo qual arquivos lógicos internos são atualizados de forma on-line.

Descreve em que nível o processamento lógico ou matemático influencia o desenvolvimento da aplicação.
Descreve em que nível a aplicação e seu código foram especificamente projetados,desenvolvidos e suportados para serem utilizados em outras aplicações.

Descreve em que nível a conversão de ambientes preexistentes influencia o desenvolvimento da aplicação. Um plano e/ou ferramentas de conversão e instalação foram fornecidos e testados durante a fase de teste do sistema.
Descreve em que nível a aplicação atende a alguns aspectos operacionais, como:
inicialização,
segurança e recuperação. A aplicação minimiza a necessidade de atividades manuais, como montagem de fitas, manipulação de papel e intervenção manual pelo operador.
Descreve em que nível a aplicação foi especificamente projetada, desenvolvida e suportada para diferentes ambientes de hardware e software.
Descreve em que nível a aplicação foi especificamente desenvolvida para facilitara mudança de sua lógica de processamento ou estrutura de dados.
Com base nos requisitos do usuário, cada característica geral do sistema deve ter seu nível de influência avaliado numa escala de o a 5. Cada característica contém diretrizes para determinar o seu nível de influência. Galera, émeio complicado de entenderassim! O que vocês acham um exemplo?Vamos ver como isso é pontuado para a característica geral conhecida como Comunicação deDados:

Pontue o, se a aplicação é puramente batch ou uma estação de trabalho que se encontra isolada.
Pontue if se a aplicação é puramente batch, mas possui entrada de dados ou impressão remota.
Pontue 2, se a aplicação é batch, mas possui alguma entrada de dados e alguma impressão remota.
Pontue 3, se a aplicação possui entrada de dados on-line, front-end de teleprocessamento para um processamento batch ou sistema de consulta.
Pontue 4, se a aplicação é mais que um front-end, mas suporta apenas um tipo de protocolo de comunicação.
Pontue 5, se a aplicação é mais que um front-end, e suporta mais de um tipo de protocolo de comunicação.
PONTUAÇÃO INFLUÊNCIA 00 SISTEMA

2 Não presente ou sem influência.
Influência mínima.

2 Influência moderada.

3 Influência média.

4 Influência significativa.

5 Forte influência.

Professor, eu preciso decorar essas pontuações? Não, não é necessário! De todo modo,
calcula-se o
VFA a partir da soma dos pontos obtidos para cada característica pela fórmula:

VFA = (SNI x o,oi) + 0,65

Sendo que SNI - Somatório do Nível de Influência! Dessa forma, se-no sistema estudado-todas as 14 características tiverem Nível de Influência 5, basta fazer: SNI = 14*5 = 70 e,em seguida,
VFA = (70*0,01) + 0,65 = 1,35. Se, no sistema estudado, todas as 14 características tiverem Nível de Influência o (isto é, não influenciam em nada o sistema), basta fazer: SNI = 14*0= o e, em seguida, VFA = (0*0,01) + 0,65 = 0,65.
Conclui-se, então, que as características gerais do sistema podem influenciar no seu tamanho variando no intervalo de -35% a +35%. Pessoal, porque eu disse anteriormente que 0cálculo do fator de ajuste tem sido negligenciado? Porque as 14 características são subjetivas e desatualizadas.Ademais, os pesos são contraditórios e há requisitos não apreciados por essas características.

(SEPLAG/DF-2009) A análise por pontos de função (APF) visa estabelecer uma medida de tamanho de um software em pontos de função. O nível de influência utilizado na APFé calculado com base nas quatorze características gerais do sistema (CGS). Assinale a alternativa que lista três dessas características.
a) Processamento complexo, eficiência do usuário final, desempenho.

b) Desempenho, saída externa, arquivos lógicos internos.

c) Eficiência do usuário final, reutilização de código, entradas externas.

d) Entradas externas, processamento complexo, arquivos lógicos internos.

e) Entrada de dados on-line, consultas externas, entradas externas.

Comentários: (a) Correto, todas são características gerais do sistema; (b) Errado, saída externa e arquivos lógicos internos não são características gerais do sistema; (c) Errado, entradas externas não são características gerais do sistema; (d) Errado, entradas externas e arquivos lógicos internos não são características gerais do sistema; (e) Errado,consultas externas e entradas externas não são características gerais do sistema (Letra A).
(TRE-PI - 2009) O valor do fator de ajuste (VAF) para calcular os pontos de função ajustados é baseado:
a) nas características gerais de sistema e no nível de influência de cada característica.

b) nas características gerais de sistema e na complexidade das funções do sistema.

c) nas funções do sistema e no nível de influência de cada função.

d) nos pontos de função não ajustados e no nível de influência das características do sistema.
e) nos pontos de função não ajustados e na complexidade de cada função do sistema.

Comentários: (a) Correto, é baseado em ambos; (b) Errado, não é baseado na complexidade das funções do sistema; (c) Errado,não é baseado nas funções do sistema nem no nível de influência de cada função, mas de cada característica; (d) Errado, não é baseado nos pontos de função não-ajustados; (e) Errado, não é baseado nos pontos de função não-ajustados nem na complexidade de cada função do sistema, mas de cada característica (Letra A).
(TRE-GO - 2009) Na aplicação da métrica Análise de Pontos por Função, caso haja influência forte em quatro das 14 Características Gerais de Sistema, os pontos ajustados serão:
a) 65% dos pontos brutos.

b) 75% dos pontos brutos.

c) 80% dos pontos brutos.

d) 85% dos pontos brutos.
e) 115% dos pontos brutos.

Comentários: se há influência em quatro das 14 CGS, então temos que VFA = SNIxo,oi + 0,65 =
(4xs)xo,oi + 0,65 = 20x0,01 +
0,65 = 0,20+0,65 = 0,85 ou 85% dos pontos brutos. (Letra D).

Calcular os Pontos de Função Ajustados

INCIDÊNCIA EM PROVA: MÉDIA

Esta etapa é extremamente simples! Basta calcular PFA = PFNA x VFA. Em outras palavras, osPontos de Função Ajustados (PFA) equivalem aos Pontos de Função Não-Ajustados
(PFNA)
multiplicado pelo Valor do Fator de Ajuste (VFA) calculado na etapa anterior. Pronto,
findamos a contagem de pontos de função, agora temos alguns exercícios para vocês treinarem e depois vamos falar sobre o NESMA...
(EBSERH - 2013) Se o total de Pontos de Função não ajustados for 107, e o nível de influência geral dado é 30, teremos como total de pontos de função ajustados:
a) 91,65

b) 100,65

c) 101,65

d) 102,65

Comentários: PFA = PFNA x VFA e VFA = (SNI x0,01) + 0,65. Logo, temos que: PFA = PFNA x [(SNI
x0,01) + 0,65]. Dessa forma,
temos que: 107 x [(30 x 0,01) + 0,65] = 107 x [0,3 + 0,65] = 107 x 0,95 = 101,65 (Letra C).

(REFAP/SA - 2017) Utilizando a análise por pontos de função em uma determinada porção de um software, foram obtidos os seguintes valores:
Nível de influência geral = 38

Pontos de função não ajustados = 3100

Qual a quantidade de pontos de função ajustados?
a) 1240

b) 1860

0)3062

d) 3138

e) 3193

Comentários: PFA = PFNA x VFA e VFA = (SNI x0,01) + 0,65. Logo, temos que: PFA = PFNA x [(SNI
x0,01) + 0,65]. Dessa forma,
temos que: 3100 x [(38 x 0,01) + 0,65] = 3100 x [0,38 + 0,65] = 3100 x 1,03 = 3193 (Letra E).

(SLU/DF - 2019) Os pontos por função não ajustados (PFNA) devem ser multiplicados pelo seu fator de ajuste (FA) para que se obtenha, assim, o valor final dos pontos por função.
Comentários: perfeito, bastava lembrar da fórmula: PFA = PFNA x VFA (Correto).

NESMA

INCIDÊNCIA EM PROVA: MÉDIA

nesma

O Netherlands Software Metrics Users Association (NESMA) é uma organização mais recente que promove uma outra abordagem de contagem de pontos de função. IFPUG e NESMA possuem abordagens praticamente idênticas para o cálculo em projetos de desenvolvimento e aplicação,no entanto é bem diferente para Projetos de Melhoria. Ela utiliza o conceito de deflatores, que são basicamente um artifício para reduzir distorções na contagem de projetos de melhoria.
A NESMA abrange três tipos de contagem: indicativa (de baixa precisão), estimativa (de média precisão) e detalhada (de alta precisão). Vamos ver...
Contagem Indicativa

INCIDÊNCIA EM PROVA: MÉDIA

A Contagem Indicativa oferece um cálculo estimado da quantidade de pontos de função,
sem a necessidade de se conhecer em detalhes o modelo de negócios da organização. Égeralmente utilizada na fase inicial da proposta de desenvolvimento, quando há só um modelo preliminar de dados. Os elementos utilizados para a contagem indicativa são apenas e tão somente os arquivos lógicos internos e os arquivos de interface externa.
A simplificação é muito simples: para cada Arquivo Lógico Interno (ALI) identificado,
contam-se 35
Pontos de Função; e para cada Arquivo de Interface Externa (AIE), contam-se 15 Pontos deFunção. Dessa forma, notem que aqui não é necessário decorar toda aquela tabelinha complexa -basta lembrar desses números mais simplificados. O número de Pontos de Função
Não-Ajustados é dado pela fórmula:
PFNA = 35 x ALI + 15 x AIE

Essa contagem se baseia na premissa de que-para cada arquivo lógico interno-existem 3EE
+ iCE

+ 2SE; e - para cada arquivo de interface externa - existem iCE e 1 SE. Professor,
para que serve a contagem indicativa se ela será bastante imprecisa? Porque pode ser útil na análise de viabilidade de um projeto! No início da aula, nós falamos sobre a importância de estimar o custo de um projeto no início para saber se o projeto é viável ou não financeiramente.
Contagem Estimativa

INCIDÊNCIA EM PROVA: MÉDIA I

A Contagem Estimativa pode ser utilizada em sistemas quando não existe uma precisão do nível de complexidade das funções existentes. Ela determina que todos os tipos de dados possuem complexidade baixa e que todos os tipos de transação possuem complexidade média-trata-se de um tipo de contagem rápida, porém ainda não tão precisa. Os elementos utilizados para a contagem estimativa são todas as funções: ALI, AIE, EE, CE e SE.
Nesse tipo de contagem, após efetuar a identificação de todas as funcionalidades do projeto, se utiliza a classificação de complexidades do IFPUG, porém considerando que todo arquivo lógico interno e todo arquivo de interface externa possuem complexidade baixa e toda entrada externa, saída externa e consulta externa possuem complexidade média. Dessa forma, a fórmula final para esse tipo de contagem fica da seguinte forma:
PFNA = [QT(ALI)X7] + [QT(AIE)xs] + [QT(EE)x4] + [QT(SE)xs] + [QT(CE)x4)j

Contagem Detalhada

INCIDÊNCIA EM PROVA: MÉDIA

A Contagem Detalhada é basicamente semelhante à contagem do IFPUG. Logo, ela fornece a quantidade de pontos de função do sistema, obtido a partir do grau de complexidade das funções levantadas. Pode ser utilizada em qualquerfase de desenvolvimento, desde que se possua detalhes do processo e do modelo de dados, como descrição de telas e relatórios ou um protótipo do sistema. Fechado, seus lindos? Acabamos a aula... êÊÊêêÊêêêÊÊÊÊeÊê ©
(STM - 2018) Os arquivos lógicos internos são desconsiderados em contagens indicativas, reconhecidos pelo usuário, referenciados pela aplicação sob medição e mantidos dentro da fronteira de outra aplicação.
Comentários: na verdade os elementos utilizados para a contagem indicativa são justamente os arquivos lógicos internos e os arquivos de interface externa (Errado).
(TJ-PE - 2015) Considere:

I. Contagem de pf detalhada.

II. Contagem de pf estimativa.

III. Contagem de pf indicativa.

Quanto ao tipo de contagem, a Netherlands Software Metrics Association reconhece o que consta em:
a) I, apenas.

b) I e II, apenas.

c) II, apenas.

d) II e III, apenas.

e) I, lie III.

Comentários: ela reconhece a contagem detalhada, estimativa e indicativa (Letra E).

(ESAF - 2015) Considere:

A NESMA- Netherlands Software Metrics Association reconhece três tipos de contagem de pontos de função (PF): detalhada, estimada e indicativa. Os parâmetros para contagem de pontos de função não ajustados são funções dos tipos: ArquivoLógico
Interno (ALI); Arquivo de Interface Externa (AIE); Entradas Externas (EE);
Saídas
Externas (SE); Consultas Externas (CE). Em relação a esses métodos, é correto afirmar que:
a) na contagem detalhada toda função do tipo ALI e AIE tem sua complexidade funcional avaliada como alta.
b) na contagem detalhada toda função transacional EE, SE, CE é avaliada como de complexidade funcional baixa.
c) na contagem estimada toda função do tipo ALI e AIE tem sua complexidade funcional avaliada como média.
d) na contagem estimada toda função transacional EE, SE, CE é avaliada como de complexidade funcional baixa.
e) na contagem indicativa determina-se a quantidade das funções do tipo dado (ALIs e
AlEs). O total de pontos de função não ajustados é obtido contando 35 PFs para cada
ALI
identificado e 15 PFs para cada AIE identificado.

Comentários: (a) Errado, a contagem detalhada funciona como o IFPUG; (b) Errado, a contagem detalhada funciona como oIFPUG; (c) Errado, tem sua complexidade avaliada como baixa; (d) Errado, tem sua complexidade funcional avaliada como média; (e) Correto, a contagem indicativa considera ALI = 35 e AIE = 15 (Letra E).
RESUMo

QUAL É A DIFERENÇA ENTRE ANÁLISE DE PONTOS DE FUNÇÃO E PONTO DE FUNÇÃO?

Análise de Pontos de Função é uma técnica, enquanto o ponto de função é o resultado da aplicação dessa técnica.
0 QUE MEDE A MÉTRICA DE PONTO DE FUNÇÃO? SOB A PERSPECTIVA DE QUEM?

Ele mede o tamanho funcional de um software sob o ponto de vista do usuário - o que ele faz e, não,
como ele faz.

A APF É DEPENDENTE DE ALGUMA TECNOLOGIA ESPECÍFICA?

Não, ela é completamente independente de tecnologia, plataforma, linguagem de programação, etc.

A APF MEDE DIRETAMENTE 0 ESFORÇO, PRODUTIVIDADE OU CUSTO DE UM SOFTWARE?

Não, mas é possível correlacionar essas variáveis à métrica de pontos de função.

PRINCIPAIS BENEFÍCIOS

Funciona como uma ferramenta para determinar o tamanho de um pacote adquirido, através da contagem de todas as funções incluídas (pode auxiliar no momento da venda de um sistema de software) e suporta a análise de produtividade e qualidade em conjunto com outras métricas como esforço, defeitos e custo.
Provê auxílio aos usuários na determinação dos benefícios de um pacote para sua organização, através da contagem das funções que especificamente correspondem aos seus requisitos. Ao avaliar o custo do pacote, o tamanho das funções que serão utilizadas, a produtividade e o custo da própria equipe, é possível analisar se vale a pena comprar ou fabricar.
Apoia o gerenciamento de escopo de projetos. Um desafio de todo gerente de projetos é controlar o aumento do escopo. Ao realizar estimativas e medições em cada fase do seu ciclo de vida, é possível determinar se os requisitos funcionais cresceram ou diminuíram; e se esta variação corresponde a novos requisitos ou aos existentes e que foram apenas mais detalhados.
Complementa o gerenciamento dos requisitos auxiliando na verificação da solidez e completeza dos requisitos especificados. O processo de contagem favorece uma análise sistemática e estruturada da especificação de requisitos e traz benefícios semelhantes ao de uma revisão em pares - basta lembrar que a contagem é baseada em requisitos do usuário.
Um meio de estimar custo e recursos para o desenvolvimento e manutenção de software. Através da realização de uma contagem ou estimativa de pontos de função no início do ciclo de vida de um projeto, é possível determinar seu tamanho funcional. Esta medida pode ser então utilizada como entrada para diversos modelos de estimativa de esforço, prazo e custo.
Uma ferramenta para fundamentar a negociação de contratos. Pode-se utilizar pontos de função para gerar diversos indicadores de níveis de serviço em contratos de desenvolvimento e manutenção de sistemas. Além disso,permite o estabelecimento de contratos a preço unitário, onde a unidade representa um bem tangível para o cliente - reduzindo riscos.
Um fator de normalização para comparação de software ou para a comparação da produtividade na utilização de diferentes técnicas. Diversas organizações, como o ISBSG, disponibilizam um imenso repositório de dados de projetos de software que permitem a realização de benchmarking com projetos similares do mercado e uma boa base de comparação.
COMPONENTES

Funções do Tipo Dado: representam requisitos de armazenamento do usuário. Galera,
quando vocês virem um ícone em formato de cilindro, provavelmente está representando algum mecanismo de armazenamento de dados. O termo arquivo aqui não significa arquivo físico ou tabela. Nesse caso, arquivo se refere a um grupo de dados logicamente relacionados e não à implementação física destes grupos de dados.
o ALI - Arquivo Lógico Interno o AIE-Arquivo de Interface Externa
Funções do Tipo Transação: representam requisitos de processamento do usuário.
Galera,
quando vocês virem uma seta, provavelmente está representando uma transação. Em outras palavras, uma transação trata de um processamento de criação, modificação ou exclusão de dados que estão armazenados em um arquivo lógico interno ou em um arquivo de interface externa.
o EE - Entrada Externa o CE - Consulta Externa o SE-Saída Externa
ARQUIVO LÚGICO INTERNO

(ALO

EXEMPLO DE ARQUIVO LÚGICO

INTERNO (ALO

NÃO EXEMPLO DE ARQUIVO
LÓGICO INTERNO (ALI)

Trata-se de um grupo de dados ou informações de controle logicamente relacionados, reconhecidos pelo usuário, mantidos dentro da fronteira da aplicação.Sua função é armazenardados mantidos dentro da fronteira da aplicação. O Arquivo
Lógico Interno contribui para o cálculo de pontos de função com base na quantidade e complexidade funcional relativa.
Dados da aplicação (arquivos mestres, como cadastro de clientes); arquivos de dados de segurança da aplicação; arquivos de dados de auditoria; arquivos de mensagem de auxílio; arquivos de mensagens de erro; arquivo de cópia de segurança (só se para atender requisitos da aplicação; arquivo que sofra manutenção por mais de uma aplicação.
Arquivos temporários; arquivos de trabalho; arquivos de classificação; arquivos de cópia de segurança (backup); arquivos introduzidos somente por causa da tecnologia usada (Ex: arquivos de parâmetro para um software WFL, JCL, etc); operações junção e projeção; arquivos de índices alternativos.
ARQUIVO DE INTERFACE

EXTERNA (AIE)

EXEMPLO DE ARQUIVO DE
INTERFACE EXTERNA (AIE)

Trata-se de um grupo de dados ou informações de controle logicamente relacionados, reconhecidos pelo usuário, mantidos dentro da fronteira de outra aplicação (externa) - os dados são armazenados fora da fronteira da aplicação. Sua principal intenção é a de armazenar dados referenciados da aplicação sendo contada. Dessa forma, um arquivo de interface externa de uma aplicação sempre será contado como um arquivo lógico interno de outra aplicação.
Arquivos de mensagens de auxílio; arquivos de mensagens de erro.

NÃO EXEMPLO DE ARQUIVO DE
INTERFACE EXTERNA (AIE)

Dados recebidos de outra aplicação usados para adicionar, alterar ou remover dados em um ALI; dados cuja manutenção é feita pela aplicação que está sendo avaliada,mas que são acessados e utilizados por outra aplicação; dados formatados e processados para uso por outra aplicação.
Trata-se de um processo elementar que processa dados ou informações de controle recebidos de fora da fronteira da aplicação e cujo objetivo é manter um ou mais arquivos lógicos internos e/ou alterar o comportamento do sistema. Uma EE provoca uma inclusão, exclusão e/ou alteração nos dados do arquivo lógico interno. Cada EEse origina de um usuário ou é transmitida de outra aplicação e fornece dados distintos orientados à aplicação ou informação de controle.
EXEMPLO DE ENTRADA

_ _ _ _ _ _ _ EXTERNA (EE)
NÃO EXEMPLO DE ENTRADA

EXTERNA (EE)

Operações de inclusões e alterações de registros em arquivos da aplicação, jane que permitem adicionar, excluir e alterar registros em arquivos de dados.
Menus, telas de login, telas de filtro de relatórios e consultas, múltiplos métodos se executar uma mesma lógica de entrada, entre outros.
SAÍDA EXTERNA ENTRADA EXTERNA CONSULTA
EXTERNA

SEMPRE ALTERA 0 COMPORTAMENTO DO SISTEMA PODE ALTERAR 0 COMPORTAMENTO DO SISTEMA NUNCA ALTERA 0
COMPORTAMENTO DO SISTEMA

SAÍDA EXTERNA

(SE)

EXEMPLO DE SAÍDA
EXTERNA (SE)

Trata-se do processo elementar que envia dados ou informações de controle para fora da fronteira da aplicação. Seu objetivo é exibir informações recuperadas através de processamento lógico que envolva cálculos ou criação de dados derivados e não apenas uma simples recuperação de dados. Uma saída externa pode manter um arquivo lógico interno e/ou alterar o comportamento do sistema.
Dados transferidos para outra aplicação; relatórios; relatórios online;
gráficos; gerador de relatórios.

NÃO EXEMPLO DE SAÍDA

EXTERNA (SE)

Telas de ajuda; literais; data, hora, controles de paginação, etc; relatórios múlti com a mesma lógica e formato; relatórios criados pelo usuário de forma di pelo usuário usando uma linguagem como SQL.
SAÍDA EXTERNA ENTRADA EXTERNA
CONSULTA EXTERNA

SEMPRE ALTERA 0 COMPORTAMENTO DO SISTEMA PODE ALTERAR 0 COMPORTAMENTO DO SISTEMA NUNCA ALTERA 0
COMPORTAMENTO DO SISTEMA

Trata-se do processo elementar que envia dados ou informações de controle para fora da fronteira da aplicação. Seu objetivo é apresentar informação o usuário por meio de uma simples recuperação de dados de um arquivo lógico interno ou arquivo de interface externa. A lógica de processamento não deve conter cálculo matemático, criar dados derivados, atualizar nenhum arquivo lógico interno e/ou alterar o comportamento do sistema.
EXEMPLO DE
CONSULTA EXTERNA (CE]

NÃO EXEMPLO DE
CONSULTA EXTERNA (CE)

Telas de logon, telas de help, telas de alteração/remoção que mostram o que será alterado ou removido antes de sua efetivação; tela de menus que permitem informar parâmetros para a consulta na tela escolhida.
Dados derivados; documentação online; sistema de teste; sistemas tutoriais;
relatórios e consultas (c/ cálculo).

SAÍDA EXTERNA ENTRADA EXTERNA
CONSULTA EXTERNA

SEMPRE ALTERA 0 COMPORTAMENTO DO SISTEMA PODE ALTERAR 0 COMPORTAMENTO 00 SISTEMA NUNCA ALTERA 0
COMPORTAMENTO DO SISTEMA

REUNIRA
DOCUMENTAÇÃO

DETERMINAR ESCOPO E
FRONTEIRA DA CONTAGEM,
IDENTIFICANDO REQUISITOS
FUNCIONAIS DO USUÁRIO

CALCULAR
TAMANHO
FUNCIONAL

DOCUMENTAR k

EREPORTAR F

FASES-IFPUG 4.2 (2005J

DETERMINAR 0 TIPO DE CONTAGEM
DETERMINAR 0 ESCOPO E FRONTEIRA

CALCULAR PONTOS DE FUNÇÃO NÃO AJUSTADOS
CALCULAR FATOR DE AJUSTE

CALCULAR PONTOS DE FUNÇÃO AJUSTADOS

FASES-IFPUG 4.3(2010]

REUNIR A DOCUMENTAÇÃO

DETERMINAR ESCOPO E FRONTEIRA DA CONTAGEM, IDENTIFICANDO
REQUISITOS FUNCIONAIS D0 USUÃRIO

MEDIR FUNÇÕES DE DADOS/TRANSAÇÕES
CALCULAR TAMANHO FUNCIONAL
DOCUMENTAR E REPORTAR

TIPO DE CONTAGEMj DESCRIÇÃO

PROJETO DE
DESENVOLVIMENTO

Mede a funcionalidade fornecida aos usuários finais do software quando da primeira instalação entregue quando o projeto estiver pronto. Esta contagem também abrange as funções de conversão de dados que serão precisas para a implantação do software. Como exemplo defunção de conversão de dados pode-se citara necessidade de importardados de um sistema antigo para o sistema em implantação.
PROJETO DE
MANUTENÇÃO/MELHORIA

PROJETO DE
APLICAÇÃO/PRODUÇÃO

Mede as modificações realizadas para aplicações existentes, isto é, funções adicionais -
modificadas ou excluídas do sistema pelo projeto e as funções de conversão de dados.
Após a conclusão e implantação do projeto de manutenção, o número de pontos de função da aplicação deve seratualizado para refletiras mudanças nas funcionalidades da aplicação. As manutenções podem ser somente evolutivas e, não,corretivas e preventivas.
Mede uma aplicação instalada e em pleno funcionamento. É também referenciada como contagem de baseline ou contagem instalada e avalia as funcionalidades correntes providas aos usuários finais da aplicação. Ela não é estimativa, é bastante precisa, na medida em que o aplicativo já está pronto e em funcionamento. Ela é iniciada ao final da contagem do projeto de desenvolvimento e atualizado no final do projeto de melhoria.
FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CEJ
ENTRADA EXTERNA (EE)
SAÍDA EXTERNA (SE)

ARQUIVO DE INTERFACE EXTERNA (AIE)
ARQUIVO LÓGICA INTERNA (ALIJ

| COMPLEXIDADE FUNCIONAL |

| BAIXA | MÉDIA | ALTA |

01-COMUNICAÇÃO DE DADOS

02-PROCESSAMENTO DISTRIBUÍDO

03-PERFORMANCE

04-CONFIGURAÇÃO DO EQUIPAMENTO

05-VOLUME DE TRANSAÇÕES

06-ENTRADA DE DADOS ONLINE

07-INTERFACE C0M0 USUÁRIO

14 CARACTERÍSTICA GERAIS DO SISTEMA ÍCGS)

08-ATUALIZAÇÃO ONLINE

09-PROCESSAMENTO COMPLEXO

10 — REUSABILIDADE

11- FACILIDADE DE IMPLANTAÇÃO

12- FACILIDADE OPERACIONAL

13- MÚLTIPLOS LOCAIS

14- FACILIDADE DE MUDANÇAS

CARACTERÍSTICA | DESCRIÇÃO

Descreve o grau pelo qual a aplicação comunica-se diretamente com o processador. Os dados
COMUNICAÇÃO DE

DADOS

ou informações de controle utilizados pela aplicação são enviados ou recebidos por meio de recursos de comunicação.
PROCESSAMENTO
DISTRIBUÍDO

Descreve o grau pelo qual a aplicação transfere dados entre seus componentes.

PERFORMANCE

CONFIGURAÇÃO DO
EQUIPAMENTO

VOLUME DE
TRANSAÇÕES

ENTRADA DE
DADOS ONLINE

INTERFACE COMO

USUÁRIO

ATUALIZAÇÃO

ONLINE

PROCESSAMENTO

COMPLEXO

REUSABILIDADE

FACILIDADE DE
IMPLANTAÇÃO

FACILIDADE
OPERACIONAL

MÚLTIPLOS

LOCAIS

FACILIDADE DE
MUDANÇAS

Descreve o grau pelo qual considerações de tempo de resposta e performance de throughput influenciam o desenvolvimento da aplicação. Os objetivos estabelecidos ou aprovados pelo usuário, em termos de tempo de resposta ou taxa de transações, influenciam o projeto,desenvolvimento, instalação e suporte da aplicação.

Descreve o grau pelo qual as restrições de recursos computacionais influenciam o desenvolvimento da aplicação. Uma configuração operacional altamente utilizada,necessitando de considerações especiais de projeto, é uma característica da aplicação.
Exemplo:
usuário deseja executar a aplicação em um equipamento já existente e que será altamente utilizado.
Descreve em que nível o alto volume de transações de negócio influencia o projeto,desenvolvimento, instalação e suporte da aplicação.

Descreve o grau pelo qual dados são informados pela execução de transações interativas.

Descreve em que nível considerações sobre fatores humanos e facilidade de uso pelo usuário final influenciam o desenvolvimento da aplicação. As funções interativas fornecidas pela aplicação enfatizam um projeto para o aumento da eficiência do usuário final.
Descreve o grau pelo qual arquivos lógicos internos são atualizados de forma on-line.

Descreve em que nível o processamento lógico ou matemático influencia o desenvolvimento da aplicação.
Descreve em que nível a aplicação e seu código foram especificamente projetados,desenvolvidos e suportados para serem utilizados em outras aplicações.

Descreve em que nível a conversão de ambientes preexistentes influencia o desenvolvimento da aplicação. Um plano e/ou ferramentas de conversão e instalação foram fornecidos e testados durante a fase de teste do sistema.
Descreve em que nível a aplicação atende a alguns aspectos operacionais, como:
inicialização,
segurança e recuperação. A aplicação minimiza a necessidade de atividades manuais, como montagem de fitas, manipulação de papel e intervenção manual pelo operador.
Descreve em que nível a aplicação foi especificamente projetada, desenvolvida e suportada para diferentes ambientes de hardware e software.
Descreve em que nível a aplicação foi especificamente desenvolvida para facilitara mudança de sua lógica de processamento ou estrutura de dados.
VFA = (SNI x 0,01)4-0,65
PFA = PFNAxVFA

TIPO DE CONTAGEM (NESMA) | DESCRIÇÃO

Oferece um cálculo estimado da quantidade de pontos de função, sem a necessidade de se conhecer em detalhes 0 modelo de negócios da organização. É geralmente
CONTAGEM INDICATIVA

utilizada na fase inicial da proposta de desenvolvimento, quando há só um modelo preliminar de dados. Os elementos utilizados para a contagem indicativa são apenas e tão somente os arquivos lógicos internos e os arquivos de interface externa.
CONTAGEM ESTIMATIVA

CONTAGEM DETALHADA

A Contagem Estimativa pode ser utilizada em sistemas quando não existe uma precisão do nível de complexidade das funções existentes. Ela determina que todos os tipos de dados possuem complexidade baixa e que todos os tipos de transação possuem complexidade média - trata-se de um tipo de contagem rápida, porém ainda não tão precisa. Os elementos utilizados para a contagem estimativa são todas as funções: ALI,AIE, EE, CEeSE.
A Contagem Detalhada é basicamente semelhante à contagem do IFPUG. Logo, ela fornece a quantidade de pontos de função do sistema, obtido a partir do grau de complexidade das funções levantadas. Pode ser utilizada em qualquer fase de desenvolvimento, desde que se possua detalhes do processo e do modelo de dados,como descrição de telas e relatórios ou um protótipo do sistema.

PARA MAIS DICAS: WWW.INSTAGRAM.COM/PROFESSORDIEGOCARVALHO

QUESTõES CoMENTADAS - CESPE

í. (CESPE / Ministério de Economia - 2020) As informações a seguir são relativas a uma mensuração de sistemas em pontos de função.
I manutenção de sete páginas HTML estáticas no portal da organização, contida em um projeto de desenvolvimento
II manutenção na interface, especificamente de logotipos, e mudança de botões da aplicação,que totalizam nove pontos de função transacionais impactados

III criação de identidade visual para dez páginas do portal associadas à área de comunicação social da organização função consultas externas (CE)
arquivos de interface externa (AIE)
entradas externas (EE)

arquivos lógicos internos (ALI)

complexidade baixa média alta alta quantidade
]

Tendo como referência as informações precedentes, julgue o próximo item, de acordo com o roteiro de métricas de software do SISP (versão 2.1).
De acordo com a tabela apresentada, as funções de dados representam mais de 55 pontos de função.
Comentários:

FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CE]
ENTRADA EXTERNA (EE)
SAÍDA EXTERNA (SE)

ARQUIVO DE INTERFACE EXTERNA (AIE)
ARQUIVO LÓGICA INTERNA (ALI)

COMPLEXIDADE FUNCIONAL |

| BAIXA , | MÉDIA | ALTA |

As funções de dados da questão são: AIE e ALI. Logo, basta contabilizar: 1AIE (Média) e 3 ALI
(Alta).
Logo, basta lembrar da tabelinha e calcular: Funções de Dados = 1x7 + 3x15 = 7 +45 = 52.

Gabarito: Errado

2. (CESPE / Ministério de Economia - 2020) As informações a seguir são relativas a uma mensuração de sistemas em pontos de função.
I manutenção de sete páginas HTML estáticas no portal da organização, contida em um projeto de desenvolvimento
II manutenção na interface, especificamente de logotipos, e mudança de botões da aplicação,que totalizam nove pontos de função transacionais impactados

III criação de identidade visual para dez páginas do portal associadas à área de comunicação social da organização função consultas externas (CE)
arquivos de interface externa (AIE)
entradas externas (EE)

arquivos lógicos internos (AL1)

complexidade baixa média alta alta quantidade
]

Tendo como referência as informações precedentes, julgue o próximo item, de acordo com o roteiro de métricas de software do SISP (versão 2.1).
De acordo com os dados da tabela apresentada, as funções transacionais representam 21pontos de função.

Comentários:

FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CE]
ENTRADA EXTERNA (EE)
SAÍDA EXTERNA (SE]

ARQUIVO DE INTERFACE EXTERNA (AIE]
ARQUIVO LÓGICA INTERNA (ALI)

COMPLEXIDADE FUNCIONAL |

| BAIXA | MÉDIA | ALTA |

As funções de transação da questão são: CE e EE. Logo, basta contabilizar: 3 CE (Baixa) e 2 EE
(Alta).
Logo, basta lembrar da tabelinha e calcular: Funções de Transação = 3x3 + 2x6 = 94-12 = 21.

Gabarito: Correto

3. (CESPE / Ministério de Economia - 2020) Uma técnica paramétrica para estimativa de esforço para desenvolvimento de software é a análise por pontos de função, que se baseia em linhas de código que são convertidas em valores numéricos, os quais, depois de ajustados à capacidade da empresa desenvolvedora, representarão o esforço necessário para se desenvolver o sistema.
Comentários:

Opa! A análise por pontos de função não se baseia em linhas de código e, sim, no tamanho funcional do software baseado na visão do usuário.
Gabarito: Errado

4. (CESPE / Ministério de Economia - 2020) A identificação de funções de dados e de tipos funcionais somente deve ocorrer após o estabelecimento da fronteira da contagem.
Comentários:

Dentre as etapas mencionadas na questão, primeiro determinamos a fronteira da contagem;depois identificamos os tipos funcionais (dados ou transação) para depois medi-los.

Gabarito: Correto

5. (CESPE / Ministério de Economia - 2020) A estimativa de esforço de projeto de software,representada pela fórmula a seguir, deve ser usada em substituição à contagem por pontos de função quando esta não for suficiente para estimar o tamanho do projeto, esforço(horas) =
tamanho (PF) x índice de produtividade (HH/PF).

Comentários:

De acordo com o Roteiro de Métricas de Software do SISP, uma vez que o tamanho do projeto foi estimado em pontos de função, o próximo passo é estimar o esforço de desenvolvimento do projeto, bem como sua distribuição pelas fases do ciclo de vida do desenvolvimento do software.
O Modelo Simplificado de Estimativas consiste em obter um índice de produtividade em horas/PFpara o projeto específico em questão, e então multiplicar o tamanho em PF do projeto pelo índice de produtividade, conforme a fórmula:
Esforço (horas) = Tamanho (PF) x índice de Produtividade (HH/PF)

Logo, não se trata de uma substituição! A ideia aqui é utilizar a APF para realizar uma estimativa de produtividade.
Gabarito: Errado

6. (CESPE / Ministério de Economia - 2020) A identificação de requisitos funcionais é resultado da análise da documentação do projeto, primeira atividade do procedimento de contagem dePF do Manual de Práticas de Contagem (CPM).

Comentários:

Perfeito! Basta lembrar da imagem clássica :)

Gabarito: Correto

7. (CESPE / Ministério de Economia - 2020) Na métrica de pontos por função, entradas externas,saídas externas e consultas externas são computadas separadamente.

Comentários:

Perfeito! Cada uma delas tem sua particularidade, logo são computadas de maneira separada.

Gabarito: Correto

8. (CESPE / Ministério de Economia - 2020) A análise de pontos de função é utilizada para medir o tamanho das funções que serão construídas de acordo com a visão do usuário, e não do desenvolvedor.
Comentários:

Perfeita definição de análise de pontos de função! Memorizem :)

Gabarito: Correto

9. (CESPE / SLU-DF - 2019) A contagem das funções de transações (FT) deve ser precedida pela contagem dos tipos de funções de dados.
Comentários:

Eu divirjo do gabarito oficial! A contagem de funções de transação e de funções de dados é simultânea, logo uma não deve ser precedida da outra.
Gabarito: Correto io. (CESPE / SLU-DF - 2019) Os pontos por função não ajustados (PFNA) devem ser multiplicados pelo seu fator de ajuste (FA) para que se obtenha, assim, o valor final dos pontos por função.
Comentários:

Perfeito! Basta lembrar da fórmula: PFA = PFNA x VFA. Em outras palavras, os Pontos de FunçãoAjustados (PFA) equivalem aos Pontos de Função Não-Ajustados (PFNA) multiplicado pelo
Valor do Fator de Ajuste (VFA) calculado na etapa anterior.
Gabarito: Correto

11. (CESPE /TJ-AM - 2019) A partir dos resultados apresentados pela métrica ponto por função, é possível estimar a quantidade de erros que serão encontrados durante o teste.
Comentários:

Perfeito! Essa métrica estima diretamente a quantidade de erros que serão encontrados durante o teste? Não, mas por meio dela é possível estimar indiretamente a quantidade de erros encontrados através de dados históricos.
Gabarito: Correto

12. (CESPE / TJ-AM - 2019) Na contagem dos tipos de elementos usados para a determinação da complexidade dos tipos de função, os tipos de elementos de registro correspondem ao número de campos distintos e não repetitivos identificáveis pelo usuário.
Comentários:

A questão inverte as definições entre Dado Elementar Referenciado (DER) e
Registro Lógico
Referenciado (RLR), sendo que o RLR também pode ser chamado de Tipo de Elemento de
Registro
(TER). Ocorre que os campos distintos e não repetitivos identificáveis pelo usuário são
DER e, não,
RLR. Logo, questão incorreta!

Gabarito: Errado

13. (CESPE / TJ-AM - 2019) Devido a suas características, uma tela de login pode ser considerada como um exemplo de consulta externa em uma contagem de pontos de função.
Comentários:

Uma tela de login pode ser considerada uma consulta externa? Pode, desde que ela não realize nenhum processamento como cálculos matemáticos, criação de dados derivados,atualização de arquivos lógicos internos e alteração do comportamento do sistema.
Gabarito: Correto

14.(CESPE / STM -2018) As funcionalidades de conversão de dados serão contadas como entrada externa, no caso da carga inicial dos dados, e como consultas ou saídas externas,quando o usuário solicitar relatório associado à funcionalidade de migração de dados.
Comentários:

A funcionalidade de conversão de dados existe quando há requisitos para migrar ou converter dados durante um novo projeto de desenvolvimento, projeto de melhoria.Assim, essas funcionalidades de conversão de dados deverão ser contadas como Entrada Externa para a funcionalidade de migração ou carga inicial dos dados e Consultas ou Saídas Externas quando forem requisitados pelo usuário relatórios associados à funcionalidade de migração de dados.
Gabarito: Correto

15. (CESPE / STM - 2018) Segundo a Nesma, a contagem indicativa considera a quantidade existente de arquivos lógicos internos e de interface externa, considerando,ainda, que toda função do tipo dado tem sua complexidade funcional avaliada como baixa e as funções transacionais avaliadas como de complexidade média.
Comentários:

Ela não leva em consideração nada disso! Essa contagem se baseia na premissa de que,
para cada
ALI, existem 3EE + iCE + 2SE e, para cada AIE, existem iCE e 1 SE.

Gabarito: Errado

16.(CESPE / CGM-PB - 2018) A APF é capaz de medir projetos de desenvolvimento e manutenção de software, com a restrição de ser dependente da tecnologia de implementação.
Comentários:

Não há restrição quanto à tecnologia de implementação.

Gabarito: Errado

17. (CESPE / TRE-BA - 2017) Na contagem de pontos de função inicial de uma aplicação, consiste em uma saída externa a:
a) consulta que calcula o valor de um boleto a ser pago com juros e multa por atraso.

b) listagem dos nomes de todos os clientes de um estabelecimento comercial.

c) tela onde é possível alterar a tabela de desconto a ser concedido para cada tipo de cliente.

d) recuperação de um texto de ajuda guardado no sistema como imagem.

e) atualização em lote das vendas efetuadas por uma loja em um dia.

Comentários:

(a) Correto, uma SE é uma CE com cálculo; (b) Errado, trata-se de uma CE; (c)
Errado, trata-se de uma EE; (d) Errado, trata-se de uma CE; (e) Errado, trata-se de uma EE.
Gabarito: Letra A

18.(CESPE /TCE-PR-2016) Com relação à técnica análise de pontos de função (APF)
utilizada para estimarfuncionalidades de um software, assinale a opção correta.
a) Os pontos de funções não ajustados são calculados por meio da soma dos arquivos lógicos internos (ALIs) e dos arquivos de interface externa (AlEs).
b) No processo de contagem de pontos por função do IPFUG, a identificação da fronteira da aplicação antecede a determinação do tipo de contagem.
c) A APF deve ser aplicada exclusivamente em projetos de software que utilizam metodologias ágeis, antes do início do desenvolvimento do software.
d) Os pontos porfunção não ajustados devem serdeterminados antes do cálculo dos pontos por função ajustados.
e) O fator de ajuste é calculado com base em três princípios da qualidade de software: facilidade de alteração, facilidade de instalação, facilidade de operação.
Comentários:

(a) Errado. São calculados por meio da soma de ALI, AIE, SE, EE e CE; (b) Errado.
A determinação do tipo de contagem antecede a identificação da fronteira da aplicação; (c) Errado.Não é exclusivo de projetos que utilizam metodologias ágeis - e não é necessariamente no início do desenvolvimento do software; (d) Correto. Calculam-se os PFNA, depois calcula-se o FAe, por fim,
calculam-se os PFA; (e) Correto. O item não afirma que é baseado apenas nesses três princípios.Ora, há 14 fatores, mas esses três fatores mencionados são - sim - princípios de qualidade de software (de acordo com a NBR ISO/IEC 9126) que ajudam o cálculo do fator de ajuste.Logo, na minha opinião, as duas últimas opções estão corretas e a questão deveria ser anulada.
Gabarito: Letra D

ig.(CESPE / TCU - 2015) Quando duas ou mais aplicações mantém e(ou) referenciam a mesma função de dados, deve-se contar os DERs (dados elementares referenciados) de todas as funções de dados das aplicações envolvidas.
Comentários:

Apesar de a redação confundir um pouco, a questão quis dizer que temos uma única base de dados(ALI/AIE) sendo referenciada por duas ou mais aplicações. Faz sentido contar os Dados
Elementares
Referenciados (DER) para cada aplicação? Não, conta-se apenas uma vez.

Gabarito: Errado

2o.(CESPE / MPOG-ATI - 2015) A aplicação da análise de pontos de função determina o custo do software a ser desenvolvido, independentemente dos índices de produtividade de cada empresa.
Comentários:

A APF permite determinar indiretamente o custo do software a ser desenvolvido,
no entanto é necessário saber os históricos de índices de produtividade de cada empresa.
Gabarito: Errado

2i.(CESPE / STJ - 2015) Na contagem de pontos de função, deve-se contar um dado elementar referenciado (DER), correspondente a uma função de dados, para cada atributo único ou não,repetido e reconhecido pelo usuário, mantido na função de dados ou recuperado dessa função por meio da execução de todos os processos elementares pertinentes ao escopo da contagem.
Comentários:

Os campos devem ser obrigatoriamente únicos e eles devem ser obrigatoriamente não-repetidos.

Gabarito: Errado

22. (CESPE / CGE-PI - 2015) No processo de contagem da aplicação, um dos passos é determinar o tamanho funcional de cada função de dados, que pode ser classificada, em relação a sua complexidade, como simples, média ou complexa.
Comentários:

Q-Q

Não vislumbro qualquer erro nessa questão! Alguns afirmam que é o nome: deveria ser baixa, média ou alta, em vez de simples, média ou complexa. No entanto, há bibliografias com ambas as denominações. Outra possibilidade seria a de que não existe um passo para determinar o tamanho funcional de cada função de dados. Ora, não é um dos cinco passos principais, mas é um dos passos para a contagem. Enfim, a banca considerou a questão errada e eu acho que nunca saberemos porquê. Para mim, está perfeita, correta e impecável...
Gabarito: Errado

23. (CESPE / STJ - 2015) O custo para projetar, codificar e testar o software pode ser estimado por meio do uso de ponto de função em dados históricos de sistemas similares.
Comentários:

Essa métrica pode ser usada para estimar indiretamente custos baseado em cruzamentos de dados históricos.
Gabarito: Correto

24.(CESPE / CGE-PI - 2015) Um processo elementar que tenha a intenção primária de apresentar informações ao usuário e que referencie uma função de dados para recuperar dados ou informações de controle pode ser uma saída externa ou uma consulta externa.
Comentários:

Tanto a consulta externa quanto a saída externa possuem a intenção primária de apresentar informações ao usuário e que referencie uma função de dados para recuperar dados ou informações de controle.
Gabarito: Correto

25.(CESPE / MEC - 2015) Os projetos de melhoria não podem envolver inclusões de funcionalidades.
Comentários:

Projetos de melhoria envolvem inclusões de funcionalidades.

Gabarito: Errado

26. (CESPE /TCDF-2014) Na técnica de Nesma utilizada para calculara estimativa do tamanho do software, realiza-se um detalhamento de cada elemento e de cada função, o que torna a técnica mais trabalhosa que outras.
Comentários:

Ela é bem menos trabalhosa porque não é necessário um detalhamento de cada elemento efunção,por meio dos deflatores.

Gabarito: Errado

27. (CESPE / ANTAQ - 2014) De acordo com a análise de pontos de função, o desenvolvimento de aplicações sem a preocupação de produzir código reusável não influencia na contagem do fator de ajuste.
Comentários:

Galera, essa foi - temos que admitir - uma excelente pegadinha da banca! Quem já está sacando um pouco do assunto deve ter lembrado: "Pô, uma das 14 Características Gerais do Sistema(CGS) é
Reusabilidade". Logo, se não há preocupação de produzir código reusável, então a influência é zero,e o papo acaba aqui mesmo!

Porém, outra pessoa pode ter confundido Fator de Ajuste com Pontos de Função Ajustados e deve ter se lembrado da fórmula (FA = (o,oi*NI) + 0,65), sendo que se NI = o, PFA =PFNA*o,6s. Então,
se for zero, ele influencia - sim - os Pontos de Função Ajustados, mas não influenciam o Fator deAjuste. Difícil de entender, não é? CESPE é assim mesmo!

Gabarito: Correto

28. (CESPE /TCDF-2014) Arquivos de interface externa (AIE) e arquivo lógico interno
(ALI) são as funções de dados utilizadas para a contagem de pontos de função.
Comentários:

Ambas são funções de dados utilizadas para contagem de pontos de função.

Gabarito: Correto

29.(CESPE /TCDF-2014) Na contagem de funções de transações, uma entrada externa (EE) é um processo que trata ou processa informações ou dados externos à aplicação. Contudo, umaEE
não modifica os dados dos arquivos lógicos internos (ALIs).

Comentários:

O objetivo é manter um ou mais arquivos lógicos internos e/ou alterar o comportamento do sistema.
Gabarito: Errado

30. (CESPE/SUFRAMA-2014) Em um projeto de melhoria, apenas as funções incluídas e alteradas devem ser contadas para se medir o tamanho funcional do projeto.
Comentários:

Opa... as excluídas também devem ser contadas.

Gabarito: Errado

31. (CESPE / CNJ - 2013) Entrada externa, arquivo referenciado e saída externa são funções do tipo transação.
Comentários:

Arquivo referenciado não é uma função do tipo transação.

Gabarito: Errado

32. (CESPE / MPOG - 2013) Na contagem por pontos de função, um arquivo de interface externa(AIE) sempre será um arquivo lógico interno (ALI) de outra aplicação.

Comentários:

Um arquivo de interface externa sempre será um arquivo lógico interno de outra aplicação.

Gabarito: Correto

33. (CESPE / CNJ -2013) O principal objetivo de um arquivo de interface externa
(AIE) é armazenar dados referenciados por um ou mais processos elementares da aplicação que está sendo contada. Além disso, um AIE contado para uma aplicação deve ser um arquivo lógico interno para outra aplicação.
Comentários:

Ele realmente armazena dados referenciados por um ou mais processos elementares da aplicação sendo contada. Ademais, um AIE de uma aplicação é sempre um ALI de outra...
Gabarito: Correto

34.(CESPE / CNJ - 2013) Na contagem de um projeto de manutenção ou de melhoria, as funções de conversão de dados não devem ser contadas.
Comentários:

Esse tipo de contagem mede as modificações realizadas para aplicações existentes, isto é, funções adicionais - modificadas ou excluídas do sistema pelo projeto e as funções de conversão de dado.
Gabarito: Errado

35. (CESPE / AL-ES - 2011 - Letra A) A análise de pontos de função é uma técnica de medição das funcionalidades oferecidas por um software do ponto de vista de seus usuários com a qual se busca medir o que o software é capaz de fazer, e não a forma como ele foi construído.
Comentários:

Item mais perfeito, é impossível. Descreveu exatamente o que é a Análise de Pontos de
Função!
Mede funcionalidades; sempre do ponto de vista do usuário; sem ligar para como o software foi construído e, sim, o que ele é capaz de fazer.
Gabarito: Correto

36.(CESPE / ANATEL - 2011) A análise de pontos de função de um programa produz estimativas de tamanho funcional de um produto de software embasada em cinco parâmetros-chave:entradas externas, saídas externas, consultas externas, arquivos lógicos internos e arquivos de interface externos. Os três primeiros parâmetros são funções transacionais, enquanto os dois últimos são funções de dados. As operações CRUD (create, read, update e delete) são consideradas pertencentes às entradas externas.
Comentários:

Read não é Entrada Externa, mas Consulta Externa -trata-se de leitura!

Gabarito: Errado

37. (CESPE / BRB - 2011) Se duas aplicações mantiverem o mesmo arquivo lógico interno, então esse arquivo será contado apenas na aplicação que detém o arquivo físico.
Comentários:

Na verdade, não importa onde está o arquivo físico. Importa, apenas, como ele é percebido logicamente pelo usuário. Logo, ele é contado em ambas as aplicações.
Gabarito: Errado

38.(CESPE / ECT - 2011) A técnica de análise de pontos de função tem como objetivos primários,
entre outros, a medição da funcionalidade que o usuário solicita e recebe, a medição do desempenho e a manutenção de software independentemente da tecnologia utilizada para sua implementação.
Comentários:

Essa questão foi dada como certa, mas - na minha opinião - está errada! Medir desempenho não é objetivo primário da APF! Além disso, manutenção de software não é sequer um objetivo da APF.
Gabarito: Correto

3g.(CESPE / MEC - 2011) São funções do tipo transação: entradas externas, saídas externas e consultas externas. Uma das principais diferenças entre as saídas externas e as consultas externas é que as primeiras devem conter alguma fórmula matemática ou cálculo, enquanto as consultas externas representam uma recuperação simples de dados.
Comentários:

Perfeito Lembrem-se sempre que uma Saída Externa (SE) é uma Consulta Externa (CE),
porém com cálculo ou processamento! Jamais esqueçam isso...
Gabarito: Correto

/fO.(CESPE / MEC - 2011) A NESMA — manual de contagem de pontos de função embasado noCPM — facilita a estimativa do tamanho do produto e tem como referência as funções de dados e transações, sem que haja detalhamento de cada elemento da função.
Comentários:

A NESMA possui a contagem Detalhada, Estimativa e Indicativa. Na Detalhada,
contam-se as funções de dados e transações, com todas as suas peculiaridades. Na Estimativa,contam-se as funções de dados e transações, porém consideram-se as funções de dados como de complexidade baixa e as funções de transação como de complexidade média. Na Indicativa, contam-se apenas as funções de dados. A questão não especificou qual tipo de contagem, mas duas delas satisfazem o descrito na questão, portanto é verdadeira.
Gabarito: Correto

4i.(CESPE / BRB - 2011) Uma consulta que possua contador incrementado é considerada uma saída externa.
Comentários:

Se uma consulta contiver um contador incrementado ou faça qualquer outro tipo de cálculo, então temos uma saída externa.
Q-Q SERPRO (Analista - Especialização: Tecnologia) Engenharia de software - 2023
(Pós-Edital)

Gabarito: Correto

42.(CESPE / TJ-ES - 2011) De acordo com o manual de contagem de pontos de função,
consulta externa é um processo elementar que envia dados ou informações de controle para fora da fronteira, sendo considerada componente funcional básico.
Comentários:

Essa definição valeria tanto para consulta externa quanto para saída externa - ambas tratam de um processo elementar que envia dados ou informações de controle para fora da fronteira, sendo considerada componente funcional básico.
Gabarito: Correto

43. (CESPE / CET - 2011) Uma consulta externa disponibiliza informações para o usuário por meio de lógica de processamento, ou seja, não se limita apenas a recuperação de dados. Alógica de processamento deve conter pelo menos uma fórmula matemática ou cálculo, ou criar dados derivados.
Comentários:

A lógica de processamento por si só não significa que houve cálculos ou fórmulas matemáticas - a questão trata, na verdade, da saída externa.
Gabarito: Errado

44. (CESPE / STM - 2011) O conceito de projeto de melhoria do IFPUG envolve as manutenções evolutivas, corretivas e preventivas da aplicação.
Comentários:

Opa... não envolve manutenções preventivas.

Gabarito: Errado

45.(CESPE / STM - 2010) O padrão ISO/IEC 20926 considera a técnica até a determinação dos pontos de função não ajustados. As características gerais de sistema utilizadas para a determinação do fator de ajuste e dos pontos de função ajustado contêm requisitos tecnológicos e de qualidade.
Comentários:

De fato, as Características Gerais de Sistema são utilizadas para determinar o fator de ajuste e os pontos de função ajustados, contêm requisitos tecnológicos e de qualidade. No entanto, essa questão foi anulada porque a ISO/IEC 20926 (Norma que especifica um conjunto de definições,regras e passos para aplicação da contagem de pontos de função do IFPUG) não constava do Edital.

Gabarito: Correto

Zj6.(CESPE / STM - 2010) Na análise de ponto de funções, a contagem de pontos relativos aos arquivos lógicos internos que se referem a grupo de dados ou informações de controle logicamente relacionados, reconhecidos pelo usuário e mantidos dentro da fronteira da aplicação, é contabilizada como pontos não ajustados.
Comentários:

Arquivos lógicos internos são realmente um grupo de dados ou informações de controle logicamente relacionadas, reconhecidas pelo usuário e mantidos dentro da fronteira da aplicação.Ademais, é contabilizada como pontos não ajustados.

Gabarito: Correto

47.(CESPE / STM - 2010) A NESMA (Netherlands Software Metrics Users
Association) tem objetivos e ações bem próximos aos do IFPUG; ambos apresentam abordagens semelhantes para a aplicação da análise de pontos de função em projetos de melhoria de software e na fase inicial do desenvolvimento do produto de software.
Comentários:

A medição de um projeto de desenvolvimento ou de uma aplicação produz resultados bem próximos tanto na abordagem do IFPUG quanto da NESMA. Por outro lado, ambas organizações possuem abordagens distintas para a aplicação da análise de pontos de função em projetos de melhoria de software.
Gabarito: Errado

/f8.(CESPE / MPU - 2010) Na análise por pontos de função (APF), as funções podem ser do tipo transação e do tipo dados. Nas funções do tipo transação, são manipulados os arquivos de interface externa (AIE) bem como os arquivos lógicos internos (ALI).
Comentários:

As funções do tipo transação são Entradas Externas, Saídas Externas e Consultas
Externas - ALI e
AIE são funções do tipo dados.

Gabarito: Errado

49.(CESPE / TRE-BA - 2009) A APF auxilia a compreender e agir sobre problemas típicos de gerenciamento de projetos, tais como baixos custos, atrasos no pagamento,insatisfação do usuário e produtividade de desenvolvedores, bem como sobre as dificuldades de medição do progresso do projeto.
Comentários:

Ué, galera! Baixos custos é um problema ou uma solução? É solução! Ademais, como ela pode agir sobre problemas como atrasos no pagamento ou insatisfação dos usuários? Questão errada!
Gabarito: Errado

5O.(CESPE / TRE-BA - 2009) A APF visa estabelecer uma medida de tamanho do software,
em pontos de função (PF), por meio da quantificação das funções implementadas sob o ponto de vista do desenvolvedor. A função de ajuste denominada cálculos complexos considera em que nível o processamento lógico ou matemático influencia o desenvolvimento da aplicação.
Comentários:

Sob o ponto de vista do desenvolvedor? Não, ponto de vista do usuário! Além disso, a função de ajuste denominada Fator de Ajuste considera o nível de influência do processamento lógico/matemática no desenvolvimento da aplicação.
Gabarito: Errado

51. (CESPE /TRE-BA-2009) Para se determinar o número de PF não ajustados, após identificar as funções de dados e transacionais, deve-se multiplicar, pela respectiva complexidade, o total de arquivos lógicos internos, arquivos de interface externa, entidades externas, saídas externas e consultas externas. De acordo com a complexidade, cada uma das funções de dados e transacionais contribui com determinado número de PF.
Comentários:

Entidades Externas? Não, são Entradas Externas! Esse é o único erro da questão! Eu digo isso,porque já vi gente dizendo que está errado afirmar que esse é o procedimento para se determinar o número de pontos de função não-ajustados. Galera, não confundam! Eu utilizo valores de complexidade para chegar à quantidade de pontos de função não-ajustados e utilizo valores de nível de influência para chegar à quantidade de pontos de função ajustados.
Gabarito: Errado

52. (CESPE /TCU -2009) Uma organização executa projetos de desenvolvimento de aplicativos de software embasados na arquitetura J2EE, com padrões de desenho, framework MVC,
interoperabilidade XML e bancos de dados relacionais. Além disso, ela adota um processo de desenvolvimento de software baseado no RUP/UML e realiza estimativas de projeto por meio de análise de pontos de função. Considere que seja necessário estimarotamanho de um projeto de uma nova aplicação a ser desenvolvida na plataforma mencionada. Nessa situação, é correto afirmar que a adição de uma nova página HTML produzirá um aumento no número total de pontos de função não ajustados; que o atendimento a uma demanda por produção de componentes de código reusáveis, para uso em outro projeto de desenvolvimento de software na mesma organização, incrementará o fator de ajuste de medição (value adjustment factor)para esse projeto.

Comentários:

A página receberá algum dado? Devolverá algum dado? Fará alguma consulta? Modificará algum arquivo de uma base de dados interna ou externa? Se ela fizer qualquer uma dessas, ela irá aumentar o número total de pontos de função não-ajustados, caso contrário não!Portanto não podemos considerar a questão como verdadeira, visto que não foi dito o que a página fará. Da mesma forma,apesar de realmente existir uma característica geral do sistema que trata de reusabilidade, a questão não deixa claro qual o nível de influência que essa característica terá no projeto, logo nada se pode afirmar.
Gabarito: Errado

53.(CESPE / TRE-BA - 2009) A contagem não ajustada de pontos de função é a soma das contribuições de cada função identificada na aplicação que esteja sendo contada. Para se obter a contagem ajustada de pontos de função, a referida soma é multiplicada pelo valor do fator de ajuste.
Comentários:

É verdade! Após a contagem não-ajustada, aplica-se o fator de ajuste para chegar à contagem de pontos de função ajustada.
Gabarito: Correto

54.(CESPE / TRE-BA - 2009) Em um projeto de desenvolvimento, uma contagem deve incluir a funcionalidade provida pela conversão de dados e relatórios associados com os requisitos de conversão de dados.
Comentários:

Perfeito! O projeto de desenvolvimento inclui as funcionalidades da contagem inicial da aplicação e as funcionalidades requeridas para conversão de dados.
Gabarito: Correto

55- (CESPE /TRE-ES - 2009) Logo após o início das atividades técnicas de um projeto,
o gerente e a equipe de desenvolvimento devem estimar o trabalho a ser realizado, os recursos necessários,o tempo de duração e, por fim, o custo do projeto. Para se estimar o tamanho do software, deve-se seguir a métrica de pontos de função (PF), desde que esta seja compatível com a tecnologia empregada na implementação do sistema.
Comentários:

Não há nenhuma imposição para utilização da métrica de pontos de função.
Além disso, ela independe da tecnologia empregada.
Gabarito: Errado

56.(CESPE / TRE-PR - 2009) O primeiro passo para a contagem das unções de dados consiste em identificar arquivos lógicos internos (ALIs) e arquivos de interface externa(AlEs). Cada uma dessas funções de dados deve ser classificada segundo sua complexidade funcional, que é definida com base em conceitos de registros lógicos e de itens de dados.
Comentários:

A questão menciona "funções de dados", logo é realmente ALI e AIE! Essas funções realmente devem ser classificadas segundo sua complexidade funcional - questão perfeita!
Gabarito: Correto

57. (CESPE / TRE-PR - 2009) Registros lógicos são subconjuntos de dados dentro de um
ALI/AIE
que foram reconhecidos pelo usuário. Caso o usuário não reconheça subconjuntos de dados em um ALI/AIE, este deve ser contado como um registro lógico.
Comentários:

Perfeito! Se há um objeto Pessoa contendo um campo Endereço que se divide em Rua,
Cidade e
Estado, então Endereço será um registro lógico, desde que seja reconhecido pelo usuário! Caso o usuário reconheça Endereço como uma coisa única (isto é, sem subconjuntos), então ele não deve ser contado como um registro lógico, mas como um dado elementar. De todo modo, mesmo no segundo caso (em que não há subconjuntos), há pelo menos um RLR. Quem? O próprio ALI/AIE.
Gabarito: Correto

58.(CESPE / TRE-PR - 2009) A contagem de pontos de função é efetuada com base na especificação do sistema e complementada por informações dos usuários e analistas, para medir o tamanho funcional de um sistema, independentemente de sua forma de implementação. Na análise de pontos de função, são contados os seguintes componentes:
arquivos lógicos internos, arquivos de interface interna, entradas externas, consultas externas e saídas externas.
Comentários:

A contagem de Pontos de Função é realmente efetuada com base na especificação do sistema,complementada por informações dos usuários e analistas. Além disso, ela serve para medir o tamanho funcional de um sistema e é, de fato, independente da forma de implementação.Agora,
atenção: Arquivo de Interface Interna? All? Não! É Arquivo de Interface Externa (AIE).

Gabarito: Errado

59. (CESPE / UNIPAMPA-2009) A métrica pontos de função tem como finalidade aferir o tamanho dos projetos de desenvolvimento e a manutenção de software.
Comentários:

Perfeito! Além de projetos de desenvolvimento e manutenção, afere também o tamanho de projetos de aplicação.
Gabarito: Correto

60.(CESPE / TRE-GO - 2009) O método de análise de pontos de função descreve como calcular as dez características gerais de um sistema, as quais são usadas para produzir, juntamente com outras informações, a contagem de pontos de função ajustados.
Comentários:

Sabemos que são 14 CGS e, não, 10 CGS.

Gabarito: Errado

61.(CESPE / ANAC - 2009) Os tipos de contagem de pontos por função podem ser de projetos de desenvolvimento, projetos de melhorias ou de aplicações, sendo a contagem de pontos por função por estimativa realizada nos estágios iniciais de contagem.
Comentários:

Os tipos de contagem podem realmente ser de projetos de desenvolvimento,
melhoria ou aplicação. Além disso, a contagem de pontos porfunção por estimativa - no caso daNESMA-é de fato realizada nos estágios iniciais de contagem.
Gabarito: Correto

62.(CESPE / STF - 2008) Em um projeto de desenvolvimento de software que adota o modelo de processos e as disciplinas propostas pelo RUP, a contagem de pontos de função não-ajustados(unadjusted function points) produzirá resultados mais eficazes para o gerente de projetos durante a fase de elaboração do que durante a fase de transição.
Comentários:

Outra questão que causou uma boa polêmica na época, mas vamos analisá-la com calma. Acontagem de pontos de função não-ajustados (isto é, aquela que desconsidera requisitos não-funcionais) produz resultados mais eficazes para o gerente de projetos durante a fase de elaboração do que durante a fase de transição? Ué, sim! A contagem não-ajustada é mais eficaz para o gerente de projetos no início do projeto, quando ainda se pensa sobre a viabilidade do projeto, estimativas de escopo, tempo, custo, entre outros.
Gabarito: Correto

63.(CESPE / TER-BA - 2008) Na APF, a precisão da estimativa melhora à medida que se obtém mais informações da análise e do projeto de sistemas. Assim, é possível estimar o tamanho do software continuamente ao longo do processo de desenvolvimento do projeto. No método backfiring, o número de pontos de função de uma aplicação é derivado a partir de seu tamanho físico, que é assumido linear entre os tamanhos funcional e físico.
Comentários:

O Método Backfiring busca estimar a quantidade de pontos de função (isto é,
seu tamanho funcional) a partir de seu tamanho físico (isto é, por meio da quantidade de linhas de código e um fator de conversão dependente da linguagem de programação utilizada).
Gabarito: Correto

64-(CESPE / MPE-AM - 2008) Uma entrada do usuário é definida como uma ação do usuário que resulta na geração de uma resposta imediata do software na forma de uma saída entregue ao usuário.
Comentários:

Por imediato, entende-se que não houve processamento! Logo, trata-se de uma Consulta
Externa ou Consulta do Usuário.
Gabarito: Errado

6s.(CESPE/ MPE-AM -2007) Um fator de complexidade permite dar um peso a cada característica do domínio da informação usada como parâmetro de entrada da análise.
Comentários:

A questão está correta, apesar de o nome exato ser Fator de Ajuste e, não, Fator de Complexidade.

Gabarito: Correto

66. (CESPE / MPE-AM - 2007) Valores de ajuste de complexidade são obtidos a partir da resposta a uma série de questões relativas ao contexto de desenvolvimento e utilização do software. Esses valores são usados conjuntamente com a contagem dos parâmetros característicos do domínio para calcular o número de pontos de função.
Comentários:

Perfeito! É preciso usar alguns valores para ajustar a contagem de pontos de função de acordo com alguns parâmetros.
Gabarito: Correto

67.(CESPE / MPE-AM - 2007) A fórmula de cálculo de pontos de função exprime uma relação exponencial entre os parâmetros de entrada da análise e a quantidade de pontos de função calculados.
Comentários:

Relação exponencial? Não, linear!

Gabarito: Errado

68. (CESPE/TST-2007) A estimativa de características de projeto por pontos de função requer que as características do domínio de informação do software sejam categorizadas como de realização simples, média ou complexa, em função do grau de dificuldade de desenvolvimento em determinada organização.
Comentários:

Em função do grau de dificuldade de desenvolvimento? Não, em função da quantidade de arquivos lógicos e itens de dados referenciados.
Gabarito: Errado

69. (CESPE / PRODEST - 2006) Uma função pode ser definida como uma coleção de instruções que realizam uma tarefa. Em uma função, pode-se também ter declarações de parâmetros formais e de variáveis locais manipuladas pelas instruções. A métrica denominada pontos de função (function points) é igual ao número de funções em um programa. Essa métrica possibilita uma medição precisa da complexidade de um programa.
Comentários:

Opa... não confundam função de linguagens de programação (semelhantes a procedimentos)
com funcionalidades.
Gabarito: Errado

7o.(CESPE / TSE - 2006) A estimativa do tamanho de um software pode ser usada para guiar a alocação de recursos em um projeto. A análise de pontos de função mede diretamente o tamanho de um software contando o número de linhas de código e não quantidades e complexidades de entradas e saídas observadas pelos usuários.
Comentários:

Opa... APF não se baseia em quantidade de linhas de código! Ela utiliza justamente as quantidades e complexidades de funções de dados (entradas e saídas) e arquivos.
Gabarito: Errado

71. (CESPE / IGEPREV-PA-2005 - A) A relação entre linhas de código fonte e os pontos de função de um software depende da linguagem de programação usada para implementar este software.
Comentários:

Essa questão é uma bela pegadinha do CESPE. Ela quis dizer que, uma vez calculada a quantidade de pontos de função de um software (Ex: 1000 PFs), a quantidade de linhas de código necessária para implementá-los depende da linguagem de programação utilizada.
Perceba que a Contagem de Pontos de Função independe de linguagem de programação, isto é,uma Entrada Externa é uma Entrada Externa em Java ou em Haskell. No entanto, a quantidade de linhas de código para implementar uma determinada Entrada Externa depende sim da linguagem de programação utilizada.
Gabarito: Correto

QUESTõES CoMENTADAS - FCC

í. (FCC / SEFAZ-AP - 2022) Considere a contagem de Pontos de Função (PF) para três Arquivos
Lógicos Internos (ALI), que possuem as seguintes especificações:

I. ZnTDeiTR.

II. 7TDe 2TR.
IH.8TDe2TR.

Dado que complexidades funcionais baixas equivalem a 7 pontos, médias a 10 pontos e altas a15 pontos, a contribuição total em PF desses três ALIs é de:

a) 32.

b) 27.

c) 30.

d) 22.

e) 21.

Comentários:

Vocês se lembram da nossa tabelinha? Bastta consultá-la:

DADOS ELEMENTARES REFERENCIADOS (DER] OU TIPO DE DADOS ITDJ

REGISTRO LÓGICO QUANTIDADE 1-19
20-50 >50
REFERENCIADO (RLR) 1 BAIXA
BAIXA MÉDIA
OU TIPO DE REGISTRO 2-5 BAIXA
MÉDIA ALTA

(TRJ >5 MÉDIA
ALTA ALTA

- O primeiro ALI tem 4 TDs e 1TR, logo tem complexidade Baixa = 7 pontos;

- O segundo ALI tem 7 TDs e 2 TRs, logo tem complexidade Baixa = 7 pontos;

- O terceiro ALI tem 8 TDs e 2 TR, logo tem complexidade Baixa = 7 pontos;
Dessa forma, temos que 7 + 7 + 7 = 21 Pontos!

Gabarito: Letra E

2. (FCC / AL-AP- 2020) Para um cálculo hipotético de Ponto por Função - PF, considere as quantidades e correspondentes funções:
- 3 EE baixa complexidade

- 1EE média complexidade

- 2 EE alta complexidade

- 2 ALI baixa comolexidade

- 2 ALI média complexidade

- 4 AIE baixa complexidade

- 3 AIE alta complexidade

- 5 SE baixa complexidade

- 5 CE média complexidade

E os seguintes valores padrão:

- 3, para EE baixa

- 4, para EE média

- 6, para EE alta

- 7, para ALI baixa

- io, para ALI média

- 5, para AIE baixa

- io, para AIE alta

- 4, para SE baixa

- 4, para CE média

Sem considerar o fator de ajuste, o total de pontos Função de Dados e o total de pontos Função de Transação são, respectivamente,
a) 12 e 65.

b) 91e16.

c) 91 e 65.

d) 12 e 91.

e) 16 e 65.

Comentários:

FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CE]
ENTRADA EXTERNA (EE)
SAÍDA EXTERNA (SE)

ARQUIVO DE INTERFACE EXTERNA (AIE)
ARQUIVO LÓGICA INTERNA (ALI)

COMPLEXIDADE FUNCIONAL |

| BAIXA , | MÉDIA | ALTA |

- 3 ALI (Baixa) = 3 x 7 = 21

- 2 ALI (Média) = 2 x 10 = 20

- 4 AIE (Baixa) = 4 x 5 = 20

- 3 AIE (Alta) = 3 x 10 = 30

Total de Pontos de Função de Dados (ALI/AIE) = 21 + 20 + 20 + 30 = 91 PFs

- 3 EE (Baixa) = 3x3 = 9

-1 EE (Média) = 1x4 = 4

- 2 EE (Alta) = 2 x 6 = 12

- 5 SE (Baixa) = 5 x 4 = 20

- 5 CE (Média) = 5 x 4 = 20

Total de Pontos de Função de Transação (EE/SE/CE) = 9 + 4 +12 + 20 + 20 = 65 PFs

Gabarito: Letra C

3. (FCC/ TRF - 3a REGIÃO - 2019) Em uma contagem de pontos de função, um ALI - Arquivo
Lógico Interno, com grau de complexidade média, contribui para a contagem com:

a) 50 pontos.

b) 20 pontos.

c) 10 pontos.

d) 07 pontos.

e) 15 pontos.

Comentários:

Temos sempre que lembrar da nossa tabelinha clássica:

FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CE]
ENTRADA EXTERNA (EE]
SAÍDA EXTERNA (SE]

ARQUIVO DE INTERFACE EXTERNA (AIE)
ARDUIVO LÓGICA INTERNA (ALI)

COMPLEXIDADE FUNCIONAL |

| BAIXA | MÉDIA | ALTA |

Gabarito: Letra C

4. (FCC / TRF - 3a REGIÃO - 2019) Em Análise de Pontos de Função, uma Consulta Externa - CE
constitui-se de dados extraídos de:

a) Arquivos Lógicos Externos (ALEs) para, após os cálculos necessários, efetuar a atualização dos Arquivos Lógicos Internos (ALIs).
b) Arquivos Lógicos Internos (ALIs), de Arquivos de Interface Externa (AlEs) e/ou de
Informações de Controle, após realizarcálculos e atualizaros arquivos que são enviados para fora da fronteira do sistema.
c) Arquivos Lógicos Externos (ALEs), de Arquivos de Interface Interna (AlIs) e de
Informações de
Controle, podendo realizar cálculos e manutenção nos arquivos que cruzam a fronteira para dentro do sistema.
d) Arquivos Lógicos Externos (ALEs), de Arquivos de Interface Externa (AlEs) e de
Informações de Controle, podendo realizar cálculos e manutenção nos arquivos que cruzam a fronteira para dentro do sistema.
e) Arquivos Lógicos Internos (ALIs), de Arquivos de Interface Externa (AlEs) e/ou de
Informações de Controle sem realizar cálculos ou manutenção nos arquivos que cruzam a fronteira do sistema e sem alterar seu comportamento.
Comentários:

(a) Errado, não existe Arquivo Lógico Externo (ALE); (b) Errado, as consultas externas não realizam cálculos; (c) Errado, não existe Arquivo Lógico Externo (ALE) ou Arquivo de InterfaceInterna (All);

(d) Errado, não existe Arquivo Lógico Externo (ALE); (e) Correto, as consultas externas tratam de dados extraídos de ALI, AIE e/ou Informações de Controle sem realizar cálculos ou manutenção dos arquivos que cruzam a fronteira do sistema e sem alterar seu comportamento.
Gabarito: Letra E

5. (FCC/TRE-PB-2015) Análise de Pontos de Função - APF é uma técnica para medir o tamanho funcional de um software cujo processo de medição envolve diversas etapas, dentre elas,a medição das funções de dados, que envolvem as funcionalidades fornecidas pelo sistema ao usuário para atender a suas necessidades de armazenamento de dados. Dentre as funções de dados estão:
a) os Arquivos de Ponto de Controle - APC.

b) as Saídas Externas - SE.

c) as Entradas Externas - EE.

d) os Arquivos de Interface Externa - AIE.

e) as Consultas Externas - CE.

Comentários:

(a) Errado, isso não é uma função; (b) Errado, isso é uma função de transação; (c) Errado, isso é uma função de transação; (d) Correto, isso é uma função de dados; (e) Errado, isso é uma função de transação.
Gabarito: Letra D

6. (FCC / MPE-MA - 2013) O primeiro passo do processo de contagem por análise de pontos de função é determinar o tipo de contagem. Contagem de pontos de função podem ser associadas a projetos ou aplicações e existem 3 tipos de contagem: Desenvolvimento, mel horia ou:
a) aplicação.

b) suporte.

c) pesquisa.

d) interoperabilidade.

e) testes.

Comentários:

Trata-se da contagem de desenvolvimento, manutenção/melhoria e aplicação/produção.

Gabarito: Letra A

7. (FCC / TST - 2012) O Gerente de Projetos de Software aplica os conhecimentos,
habilidades e ferramentas às atividades do projeto com o objetivo de garantirque o produto seja desenvolvido de acordo com os requisitos. A métrica de análise de Pontos de Função, de acordo com a normaISO/IEC 20968,

a) auxilia o Gerente de Projetos de Software a estimar o esforço necessário e custo para o desenvolvimento de sistemas com a abordagem da análise estruturada de sistemas.
b) possibilita ao Gerente de Projetos de Software medir o esforço e qualidade necessários para desenvolver softwares, desde que esteja usando a análise orientada a objetos e os diagramas daUML.

c) classifica a contagem das funções do tipo dado em Entradas Externas (EE), Consultas
Externas
(CE) e Saídas Externas (SE), representando requisitos que gerem o armazenamento de dados do usuário.
d) define que os Arquivos Lógicos Internos (ALI) e os Arquivos de Interface Externa
(AIE) são funções do tipo transição, os quais representam requisitos relacionados ao processamento.
e) auxilia o Gerente de Projetos de Software com técnicas para medir o esforço necessário para o desenvolvimento de um sistema, apoiando-o, também, no levantamento dos custos, análise de qualidade e análise de produtividade.
Comentários:

(a) Pessoal, eu disse diversas vezes que a análise de pontos de função não depende de tecnologia ou abordagem de programação. No entanto, a questão - em nenhum momento - restringiu a isso,apenas disse que ela auxiliava o gerente de projetos na estimativa de esforço de projetos com essa abordagem. Em minha opinião, não há erro algum na questão, porém não foi assim que a banca entendeu =/ (b) APF não mede esforço e qualidade, ela mede tamanho de software. Ela auxilia a medir esforço e qualidade indiretamente, por meio de outras métricas - cuidado com isso! De todo modo, a questão diz que isso só é válido caso esteja sendo usada a análise orientada a objetos e os diagramas da UML - é independente de tecnologia, abordagem de programação ou tipos de diagramas, (c) Não, são funções do tipo transação! (d) Primeiro: não existe função do tipo transição,mas transação. Ademais, arquivos são funções do tipo dados, portanto está errado duas vezes, (e)Agora sim! Essa é a resposta correta.

Gabarito: Letra E

8. (FCC/MPE-AP-2012) Dentre os métodos disponíveis na utilização de métricas de sistema está a análise de pontos de função (Function Point Analysis). Nesse método,
a) a função realizada pelos objetos do sistema, seus atributos e operações são catalogados,possibilitando medir a quantidade de classes e objetos que serão necessários para este sistema.

b) as funções utilizadas em linguagens de desenvolvimento tradicional, bem como os métodos e operações utilizados em arquiteturas orientadas a objeto são contados para a definição do tamanho funcional do sistema.
c) é atribuída uma pontuação para cada função ou método executado por uma determinada linguagem de programação. Este número é formulado com base em cálculos matemáticos e,posteriormente, é utilizado para fazer a classificação das métricas do sistema.

d) são analisados os pontos de execução de cada função dentro de um determinado sistema,são gerados registros de sistemas (logs) e, posteriormente, é gerada uma classificação em função dos valores obtidos dessa análise..
e) as funcionalidades do sistema são elencadas sem a necessidade de preocupação com a tecnologia que será utilizada para o desenvolvimento do sistema.
Comentários:

(a) Função realizada pelos objetos do sistema? Não, função identificada por usuários do sistema, (b)O método é chamado Análise de Pontos de Função! Galera, essa função não é aquela função similar a um procedimento da análise estruturada nem mesmo similar a um método da orientação a objetos! APF mede o tamanho funcional de um software independentemente da tecnologia utilizada, apenas isso! (c) Pontuação para cada função ou método? Não! Galera, não pode confundir função em linguagens de programação com a funcionalidade medida na APF. (d) Que viagem é essa? APF não tem nada a ver com isso! (e) Agora, sim! Perfeito, mede-se funcionalidade sem nenhuma relação com a tecnologia empregada no desenvolvimento do sistema.
Gabarito: Letra E

9. (FCC / TRE-SP - 2012) Sobre a análise de pontos por função, considere:

I. É um método de contagem padrão capaz de medir as funcionalidades de um sistema sobre o ponto de vista do desenvolvedor.
II. A contagem sem ajustes (UFPC - unadjusted function point count) reflete as funcionalidades contáveis específicas disponibilizadas pelo sistema ou aplicação para o usuário.
III. É uma ferramenta para ajudar usuários a determinar os benefícios de um pacote de aplicativos para sua empresa por meio de contagem das funcionalidades que especificamente atendem seus requerimentos.
Está correto o que consta em:

a) II, apenas.

b) I e II, apenas.

c) I e III, apenas.

d) II e III, apenas.

e) I, lie III.

Comentários:

(I) Sob o ponto de vista do desenvolvedor? Não! Sob o ponto de vista do usuário!
(II) Perfeito! Por que, galera? Porque ela considera apenas os requisitos funcionais - UFPC não está nem aí para as características gerais do sistema. (III) Perfeito! Essa é uma das vantagens da análise de pontos de função, isto é, ela serve para que o cliente avalie se vale a pena adquirir um pacote de aplicativos em vez de desenvolvê-lo. Galera, alguns alunos já me falaram: Professor, não é uma ferramenta! Éuma técnica, metodologia. Pessoal, é verdade, mas vocês têm que ter a sacada de ver que esse não é o foco da questão, porque não adianta marcar errado, pois a banca não vai aceitar recu rsos. Ok?
Gabarito: Letra D

10.(FCC / TRE-CE - 2012) Considere 3 AlEs simples, 5 EEs médias, 8 CEs complexas, 3
ALIs complexos e 7 SEs médias. O cálculo de PF bruto é:
a) 136.

b) 148.

c) 159.

d) 163.

Q-Q SERPRO (Analista - Especialização: Tecnologia) Engenharia de software - 2023
(Pós-Edital)

e) 212.

Comentários:

Galera, esse tipo de questão é extremamente fácil se você sabe a tabela decorada ou impossível se você não sabe!
FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CE]
ENTRADA EXTERNA (EE)
SAÍDA EXTERNA (SE)
ARQUIVO DE INTERFACE EXTERNA (AIE)
ARQUIVO LÓGICA INTERNA (ALI)

| COMPLEXIDADE FUNCIONAL |

| BAIXA | MÉDIA | ALTA |

3 AlEs Simples

5 EEs Médias

^3*5 =15

5*4 = 20

8 CEs Complexas

3 ALIs Complexos

7 SEs Médias

8*6 =48

^3*15 = 45

"^7*5 =35

TOTAL = 163

Gabarito: Letra D

n.(FCC / TRT-AM - 2011) Segundo a IFPUG em relação à métrica do software por análise por pontos de função, considere:
I. Análise por pontos de função executa a medição do software determinando a quantidade de funcionalidades que o software fornece ao usuário baseado principalmente na arquitetura lógica.
II. O objetivo da análise por pontos de função é medir as funcionalidades que o usuário requisita e recebe e, também, medir o desenvolvimento e manutenção do software com dependência na implementação utilizada pela empresa.
III. O processo de contagem dos pontos de função deve ser simples o suficiente para minimizar a sobrecarga do processo de medida e consistente dentre os vários projetos e organizações.
Está correto o que se afirma em:

a) I e II, apenas.

b) I e III, apenas.

c) II e III, apenas.

d) III, apenas.

e) I, lie III.

Comentários:

(I) Perfeito! Professor, por que principalmente na arquitetura lógica? Porque a arquitetura lógica é o meio termo entre o conceituai e o físico! APF não leva em conta aspectos tecnológicos em si, no entanto ela considera as características gerais do sistema, portanto está no meio termo. (II) Com dependência na implementação utilizada? Não, é independente de tecnologia! (III)Galera, a contagem não pode dar muito trabalho! Ademais, deve ser consistente entre os projetos e organizações.
Gabarito: Letra B

12. (FCC / INFRAERO - 2011) Analise a tabela utilizada no cálculo de Pontos de Função.

Tipo de Função

I
II
III

Complexidade Funcional
Simples Média Complexa
7 10 15

5 7 10

4 5 7

Preenchem correta e respectivamente os tipos de função I, II e III:

a) ALI, AIE e SE.

b) ALI, CEeAIE.

c) CE, EEeALI.

d) AIE, AL e EE.

e) EE, CEeSE.

Comentários:

FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CE]
ENTRADA EXTERNA (EE]
SAÍDA EXTERNA (SEJ
ARQUIVO DE INTERFACE EXTERNA (AIE]
AROUIVO LÚDICA INTERNA (ALI]

| COMPLEXIDADE FUNCIONAL |

| BAIXA | MÉDIA | ALTA |

Perceberam que tem que decorar essa tabela, né?! Trata-se de ALI, AIE e SE!

Gabarito: Letra A

13. (FCC / INFRAERO - 2011) A métrica análise por pontos de função foi desenvolvida na década de 1970, como uma forma de medir software. Analise os itens a seguir relacionados a essa métrica:
I. Considera mais importante o número de linhas de código do que as funcionalidades criadas.

II. Pode ser aplicada antes do código ser escrito, baseando-se na descrição arquitetural do projeto.
III. É dependente da tecnologia utilizada no desenvolvimento.

IV. Dois programas muito diferentes podem possuir a mesma contagem de pontos de função.

Está correto o que consta em:

a) I, II, III e IV.

b) II e IV, apenas.

c) I, II e IV, apenas.

d) I, II e III, apenas.

e) I e III, apenas.

Comentários:

(I) Como é? Não! Considera as funcionalidades criadas mais importantes! (II) Perfeito,
é isso mesmo!
Pode ser feita antes? Sim. Baseado na arquitetura? Se uma arquitetura for muito bem desenhada, é possível fazer uma estimativa baseado na descrição arquitetural do projeto. (III) Não é dependente de tecnologia utilizada no desenvolvimento. (IV) Perfeito, claro que podem!
Gabarito: Letra B

14.(FCC /TRT-RS-2011) Após a aplicação do fator de ajuste, o total de pontos de função em uma contagem ficou em 110,60. Antes da aplicação do ajuste, os pontos de função brutos estavam em 140,00. Portanto, o somatório dos 14 itens do nível de influência global foi:
a) 11.

b) 14.

c) 15-

d) 18.

e) 19.

Comentários:

Sabe-se que PFA = VFA*PFNA = no,6o e PFNA = 140,00. Logo, VFA = 110,60/140,00 =
0,79. Sabe-

se, também, que VFA = SNI*o,oi + 0,65 = 0,79 = SNI*o,oi + 0,65 - 0,14/0,01 = 14.

Gabarito: Letra B

i5.(FCC/TRT-PI-2oio) Considere, no âmbito da Análise de Pontos de Função:

(I) Um ALI é contado com base em uma avaliação do número de campos de dados não recursivos do usuário e do número de tipos de elementos de registros lógicos nele contidos.
(II) Um AIE é uma entidade lógica e persistente, que é requerida para referência ou validação pelo software sendo contado, mas que é mantido por outro aplicativo de software.
(III) Uma entrada externa é contada com base no número de campos de dados do usuário envolvidos e na soma dos ALI, mas não dos AIE participantes do processo.
Está correto o que se afirma em:

a) I, apenas.

b) II, apenas.

c) III, apenas.

d) I e II, apenas.

e) I, lie III.

Comentários:

(I) Perfeito! ALI é contado com base no número de dados não recursivos (também conhecidos comoDados Elementares Referenciados) e tipos de elementos lógicos de registros (também conhecidos como Registros Lógicos Referenciados). Um DER é um campo de dados não-recursivos do usuário,portanto está tudo perfeito! (II) Perfeito, é isso mesmo! (III) Não, uma EE é calculada por meio da quantidade de Dados Elementares Referenciados (DER) e Arquivos Lógicos Referenciados (ALR).
Gabarito: Letra D

i6.(FCC / TRF4 - 2010) Sobre a métrica análise por pontos de função, é correto afirmar:

a) Não pode ser aplicada para estimar esforço de manutenção em sistemas já em funcionamento.
b) A medida não pode ser aplicada com base na descrição arquitetural do projeto, mas sim no código desenvolvido.
c) É dependente da tecnologia utilizada no desenvolvimento.

d) A contagem de pontos de função pode ser aplicada logo após a definição da arquitetura,permitindo estimar o esforço e o cronograma de implementação de um projeto.

e) Para determinar o número de pontos de função, deve-se desconsiderar a contagem de dados e de transações.
Comentários:

(a) Pode, sim, ser aplicada! O primeiro passo é definir o tipo de contagem, que pode ser de desenvolvimento, melhoria ou aplicação, (b) Pode, sim, ser aplicada com base na descrição arquitetural do projeto, (c) É independente de tecnologia, (d) Perfeito, observe que a questão diz que permite estimar esforço e cronograma - claro que indiretamente, (e) Como assim?Deve-se considerar EE, SE, CE, ALI e AIE -funções do tipo dado e transação.
Gabarito: Letra D

i7.(FCC/TRT-PR-2oio) Na análise de pontos de função, são apenas do tipo Transação as funções:

a) ALI e SE.

b) ALI e AIE.

c) ALI, AIE e SE.

d) CE, EEeSE.

e) CE, EE, SE e AIE.

Comentários:

As funções de transação são: CE, EE e SE!

Gabarito: Letra D

i8.(FCC / TCM-PA - 2010) É um processo lógico do negócio que mantém os dados recebidos de fora da fronteira da aplicação em um ou mais arquivos lógicos internos ou, ainda, é um processo de controle que direciona o software para atender os requisitos de negócio do usuário. No âmbito da Análise de Pontos de Função, tal é a definição de:
a) SE.

b) AIE.

c) EE.

d) ALI.

e) CE.

Comentários:

Mantém dados recebidos de fora da fronteira da aplicação em um ou mais arquivos lógicos internos é a definição de entrada externa.
Gabarito: Letra C

ig.(FCC / TCM-PA - 2009) Quanto aos pontos brutos, na Análise de Pontos de Função o fator de ajuste aplicado pode aumentá-los:
a) em até 35% ou diminuí-los em até 65%.

b) ou diminuí-los em até 35%.

c) ou diminuí-los em até 65%.

d) ou diminuí-los em até 1,35%.

e) em até 65% ou diminuí-los em até 35%.

Comentários:

Para entender melhor, vamos pegar os casos limítrofes...

1) Se o sistema contado não sofre influência de nenhuma das características gerais do sistema,então o somatório será o [o+o+o+o+o+o+o+o+o+o+o+o+o+o]. Logo, FA = (0*0,01) + 0,65 =
0,65 =
65%.

2) Se o sistema contado sofre forte influência de todas as características gerais do sistema, então o somatório será 70 [5+5+5+5+5+5+5+5+5+5+5+5+5+5]. Logo, FA = (70*0,01) + 0,65 = 1,35 = 135%.
Portanto, há uma variação de 65% a 135%. Logo, o Fator de Ajuste pode aumentar ou diminuir a contagem de pontos brutos em até 35% - para mais ou para menos.
Gabarito: Letra B

í. (FGV/ IMBEL-2021) A análise de ponto de função é uma técnica comumente utilizada para:

a) avaliar a produtividade de programadores desenvolvedores.

b) estabelecer configurações de hardware para sistemas em produção.

c) medir o tamanho de projetos de desenvolvimento de software.

d) medir a produtividade de equipes de desenvolvimento de software.

e) medir os tempos de resposta de sistemas instalados e operacionais.

Comentários:

(a) Errado. Ela pode ser usada para avaliar indiretamente a produtividade de programadores e desenvolvedores, mas não é sua função mais comum; (b) Errado, não tem nenhuma relação com essa atividade; (c) Correto; (d) Errado. Ela pode ser usada para avaliar indiretamente a produtividade de equipes, mas não é sua função mais comum; (e) Errado, não tem nenhuma relação com essa atividade.
Gabarito: Letra C

2. (FGV / DPE-RJ - 2019) Determinado órgão governamental está utilizando a técnica de
Análise de Pontos de Função (APF) para efetuar a contagem de suas aplicações e gerar uma base histórica própria.
Sendo assim, para a contagem de um sistema que atende a atividade-fim desse órgão,
será necessário:
a) acessar o código-fonte para contar as funções desenvolvidas ou incorporadas ao sistema;

b) explorar o modelo físico (esquema físico) do banco de dados para quantificar as funções de dados;
c) quantificar as funcionalidades implementadas, considerando a visão do usuário;

d) detalhar e medir os requisitos não funcionais solicitados pelo usuário;

e) medir as funções das transações executadas e gerenciadas pelo banco de dados.

Comentários:

(a) Errado, não é necessário acessar o código-fonte; (b) Errado, não é necessário explorar o modelo físico; (c) Correto, o que importa é a visão do usuário e, não, como o sistema é efetivamente implementado; (d) Errado, não se medem requisitos não-funcionais; (e) Errado,uma função de transação não necessariamente é executada e gerenciada por um SGBD.
Gabarito: Letra C

0 0

3- (FGV / DPE-RJ - 2019) Determinado órgão governamental está utilizando a técnica de
Análise de Pontos de Função (APF) para efetuar a contagem de suas aplicações e gerar uma base histórica própria. Sendo assim, para a contagem de um sistema que atende a atividade-fim desse órgão, será necessário:
a) acessar o código-fonte para contar as funções desenvolvidas ou incorporadas ao sistema;

b) explorar o modelo físico (esquema físico) do banco de dados para quantificar as funções de dados;
c) quantificar as funcionalidades implementadas, considerando a visão do usuário;

d) detalhar e medir os requisitos não funcionais solicitados pelo usuário;

e) medir as funções das transações executadas e gerenciadas pelo banco de dados.

Comentários:

(a) Errado, não é necessário acessar o código-fonte; (b) Errado, não é necessário explorar o modelo físico; (c) Correto, o que importa é a visão do usuário e, não, como o sistema é efetivamente implementado; (d) Errado, não se medem requisitos não-funcionais; (e) Errado,uma função de transação não necessariamente é executada e gerenciada por um SGBD.
Gabarito: Letra C

4. (FGV / MPE-AL - 2018) Carlos é o responsável técnico pelo Sistema de Informação
Financeiro
(SISFIN) de sua corporação. O SISFIN passou por um processo de melhorias que corrigiu erros em duas funcionalidades, incluiu três novas funcionalidades e excluiu uma funcionalidade.Com o intuito de atualizar o tamanho funcional do SISFIN, ao término das alterações, as funções doSISFIN serão contadas utilizando a técnica de Análise de Ponto de Função (APF). Sendo assim,é correto afirmar que o tamanho funcional do SISFIN foi alterado por causa da contagem dos pontos de função da(s):
a) seis funcionalidades.

b) três novas funcionalidades.

c) três funcionalidades novas e da excluída.

d) funcionalidade excluída.

e) duas correções e da funcionalidade excluída.

Comentários:

Correções de funcionalidades não alteram a contagem de pontos de função, apenas as três novas funcionalidades e a exclusão de uma funcionalidade. Sim, a exclusão de funcionalidades também é contada! Dessa forma, é correto afirmar que o tamanho funcional foi alterado por causa da contagem dos pontos de função das três funcionalidades novas e da excluída.
Gabarito: Letra C

5- (FGV / Banestes- 2018) Em termos de Análise de Pontos de Função (APF),
analise as afirmativas a seguir.
I. É capaz de medir projetos de desenvolvimento e manutenção de software, com a restrição de ser dependente da tecnologia de implementação.
II. A técnica de derivar o número de pontos de função a partir da quantidade de linhas de código do programa é baseada num fator de conversão que independe da linguagem de programação usada.
III. Visa medir a funcionalidade de um software do ponto de vista de seus usuários.
Essa medição ocorre antes mesmo do desenvolvimento do software, de forma a estimar o seu tamanho e o seu custo.
Está correto somente o que se afirma em:

a) I;

b) II;

c) III;

d) I e II;

e) lie III.

Comentários:

(I) Errado, é independente da tecnologia utilizada; (II) Errado, existe realmente uma técnica que permite derivar o número de pontos de função a partir da quantidade de linhas de código do programa, mas o fator de conversão depende da linguagem de programação utilizada; (III)Correto,
ela realmente mede o tamanho funcional de um software de acordo com a visão dos usuários e, por meio da contagem estimativa, permite estimar o tamanho antes mesmo de seu desenvolvimento.
Gabarito: Letra C

6. (FGV / COMPESA - 2018) O levantamento da complexidade das oito funções de um sistema a ser desenvolvido, seguindo a técnica de Contagem de Pontos de Função,resultou nos elementos listados na tabela a seguir.
Nome da Função
ALI-1

ALI-2

EE-1
EE-2
EE-3
CE-1
SE-1
SE-2

Tipo da Função
Arquivo Lógico Interno
Arquivo Lógico Interno
Entrada Externa
Entrada Externa
Entrada Externa
Consulta Externa
Saída Externa

Saída Externa

Complexidade
Baixa
Média
Baixa
Média
Alta
Média
Baixa

Alta

Assinale a opção que corresponde ao total de pontos de função não ajustados computado para o conjunto das funções listadas na tabela:
a) 42

b) 43

c) 44

d) 45

e) 46

Comentários:

FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CE]
ENTRADA EXTERNA (EE)
SAÍDA EXTERNA (SE]
ARQUIVO DE INTERFACE EXTERNA (AIEJ
ARQUIVO LÓGICA INTERNA (ALI)

Vamos fazer as contas:
ALI-i: Baixo = 7

ALI-2: Medio = 10

EE-i: Baixo = 3

EE-2: Medio = 4

EE-3: Alto = 6

CE-i: Medio = 4

SE-i: Baixo = 4

SE-2: Alto = 7

TOTAL = 45

| COMPLEXIDADE FUNCIONAL |

| BAIXA | MÉDIA | ALTA |

Gabarito: Letra D

7- (FGV / COMPESA - 2018) O levantamento da complexidade das oito funções de um sistema a ser desenvolvido, seguindo a técnica de Contagem de Pontos de Função,resultou nos elementos listados na tabela a seguir.
Nome da Função
ALI-1

AU-2
lEE-1
EE-2
EE-3
CE-1
SE-1
SE-2

Tipo da Função
Arquivo Lógico Interno
Arquivo Lógico Interno

Entrada Externa

Entrada Externa
Entrada Externa
Consulta Externa
Saída Externa
Saída Externa

Complexidade
Baixa
Média
Baixa
Média
Alta
Média
Baixa
Alta

Assinale a opção que corresponde ao total de pontos de função não ajustados computado para o conjunto das funções listadas na tabela.
a) 42

b) 43

c) 44

d) 45

e) 46

Comentários:

Tendo a tabelinha memorizada, bastava calcular: 1*7 (ALI/Baixa) + 1*10
(ALI/Média) + 1*3
(EE/Baixa) + 1*4 (EE/Média) + 1*6 (EE/Alta) + 1*4 (CE/Média) + 1*4 (SE/Baixa) + 1*7
(SE/Alta) = 7 +
10 + 3 + 4 + 6 + 4 + 4 + 7 = 45.

Gabarito: Letra D

8. (FGV/ IBGE -2017) A Análise de Pontos de Função (APF) é um método de medição de tamanho funcional de um software. Nesse método são contadas as funções de dados e funções de transação. Após essas contagens são aplicados fatores de ajuste. A opção que apresenta fatores de ajuste desse método é:
a) Volume de transações, entrada de dados online e presença de stakeholders negativos;

b) Walkthrough, Processamento distribuído e Performance;

c) Facilidade de Mudanças, Prototipação e Comunicação de dados;

d) Atualização online, interface com usuário e Múltiplos locais;

e) Facilidade de Implantação, Facilidade operacional e Facilidade de obsolescência.

Comentários:

14 CARACTERÍSTICA GERAIS DO SISTEMA (CGS)

01-COMUNICAÇÃO DE DADOS

02-PROCESSAMENTO DISTRIBUÍDO

03-PERFORMANCE

04-CONFIGURAÇÃO DO EQUIPAMENTO

05-VOLUME DE TRANSAÇÕES

06-ENTRADADE DADOS ONLINE

07-INTERFACE C0M0 USUÁRIO

08-ATUALIZAÇAO ONLINE

09-PROCESSAMENTO COMPLEXO

10- REUSABILIDADE

11- FACILIDADE DE IMPLANTAÇÃO

12- FACILIDADE OPERACIONAL

13- MÚLTIPLOS LOCAIS

14- FACILIDADE DE MUDANÇAS

Trata-se da Atualização online, interface com usuário e Múltiplos locais.

Gabarito: Letra D

g. (FGV / Prefeitura de Paulínia - SP - 2016) Ponto de Função é uma métrica orientada à função utilizada para medir o tamanho funcional do software. Na contagem de Pontos de Função,a função de transação que não altera o comportamento do sistema, embora possa conter validações, é denominada:
a) entrada externa.

b) consulta externa.

c) saída externa.

d) arquivo lógico interno.

e) arquivo de interface externa.

Comentários:

Aquestão trata de uma função de transação, logo podemos eliminaras opções (d) e (e).
Além disso,
a função de transação que não altera o comportamento do sistema é a consulta externa,
porque as outras duas realizam essas alterações.
Gabarito: Letra B

10.(FGV / IBGE - 2016) O requisito Obter Histórico de Compras do sistema A consiste em uma referência a um grupo de dados "X" logicamente relacionado, mantido e armazenado no sistema B, conforme representado no diagrama a seguir.
Sistema A

Na visão do usuário do sistema A, o grupo de dados "X" é visto na técnica de
Análise por Pontos de Função como:
a) ALI - Arquivo Lógico Interno;

b) AIE - Arquivo de Interface Externa;

c) EE - Entrada Externa;

d) SE-Saída Externa;

e) CE - Consulta Externa.

Comentários:

Na visão do usuário do Sistema A, o grupo de dados X é um AIE; já na visão do usuário do SistemaB, o grupo X é um ALI.

Gabarito: Letra B

n.(FGV / PGE-RO - 2015) Roger e sua equipe de métricas de software foram designados para estimar o custo e o tempo necessário para desenvolver um sistema de informação. Apartir dos requisitos levantados desse sistema, a equipe de Roger contou o número de:
Arquivos Lógicos Internos (ALIs); Arquivos de Interface Externa (AlEs); Entradas Externas
(EEs);
Consultas Externas (CEs); e Saídas Externas (SEs). Com base nessas contagens, Roger e sua equipe podem fazer as estimativas de software aplicando o método:
a) Linhas de código;

b) Pontos por Casos de Uso;

c) Pontos de Função;

d) Complexidade Estrutural;

e) Ponderado por Classe.,

Comentários:

Com base nessas contagens, Roger e sua equipe podem fazer as estimativas de software aplicando o método será Dossível estimar utilizando Dontos de função.
Gabarito: Letra C

12. (FGV / TJ-PI - 2015) Vários entes governamentais brasileiros têm utilizado a métrica de Pontos de Função (PF) nas estimativas e dimensionamento de tamanho funcional de projetos de software devido aos diversos benefícios de utilização da métrica e às recomendações dos órgãos de controle do governo brasileiro. Sobre a métrica de Pontos de Função, é correto afirmar que
/
e:

a) baseada no projeto físico da aplicação;

b) usada para quantificaras linhas de código contidas na aplicação;

c) composta de Arquivos Lógicos Externos (ALEs), Arquivos de Interface Interna (Alls),
Entradas
Externas (EEs), Consultas Internas (CIs) e Saídas Externas (SEs);

d) independente da solução tecnológica utilizada na aplicação;

e) um indicador da produtividade da equipe de desenvolvimento de uma aplicação.

Comentários:

(a) Errado, é baseada na visão do usuário; (b) Errado, é usada para medir o tamanho funcional de um software; (c) Errado, é composta de ALI, AIE, EE, CE e SE e, não, ALE, All, EE, Cl e SE; (d)Correto,
é realmente independente de solução tecnológica utilizada; (e) Errado, ela pode ser utilizada para indicar produtividade de forma indireta, mas ela - em si - não indica produtividade de uma equipa de desenvolvimento.
Gabarito: Letra D

13.(FGV / PROCEMPA - 2014) A técnica de contagem de pontos de função define algumas abstrações necessárias à determinação do tamanho funcional de um projeto de software.Relacione cada um dos elementos da contagem de pontos de função, listadas a seguir,
às suas respectivas características.
1. Consulta Externa

2. Arquivo de Interface Externa

3. Arquivo Lógico Interno

4. Entrada Externa

5. Saída Externa

() Tabelas de banco de dados lidas pela aplicação, mas atualizadas por outra aplicação.
() Tabelas de banco de dados atualizadas pela aplicação.

() Transação que processa dados ou informações de controle originados de fora da fronteira da aplicação.
() Função que apresenta informações ao usuário por meio da lógica de processamento que não seja apenas uma simples recuperação de dados ou informação de controle.
() Função que apresenta informações ao usuário, por meio da simples recuperação de dados ou informações de controle, dentro da fronteira da aplicação.
Assinale a opção que indica a sequência correta, de cima para baixo.
a) 3-2-5-i-4

b) 2-3-4-5-1

c) 3-2-4-i-5

d) 2-3-5-4-1

e) 3-2-i-5-4

Comentários:

(2) Tabelas de banco de dados lidas pela aplicação, mas atualizadas por outra aplicação; (3) Tabelas de banco de dados atualizadas pela aplicação; (4) Transação que processa dados ou informações de controle originados de fora da fronteira da aplicação; (5) Função que apresenta informações ao usuário por meio da lógica de processamento que não seja apenas uma simples recuperação de dados ou informação de controle; (1) Função que apresenta informações ao usuário, por meio da simples recuperação de dados ou informações de controle, dentro da fronteira da aplicação.
Gabarito: Letra B

i4.(FGV / INEA-RJ - 2013) A análise preliminar de um sistema a ser desenvolvido possui as seguintes características:
* doze entradas externas sendo três simples, quatro médias e cinco complexas.

* seis saídas externas sendo duas simples e quatro médias.

Infelizmente, não foi possível determinar o número de Arquivos Lógicos Internos
(ALI) do sistema, mas sabe-se que todos são do tipo simples. O desenvolvedor sabe que, por contrato, o sistema deve possuir um total de pontos de função igual a 118. O número de ALIs simples que o sistema deve conter, de forma a atingir, exatamente, o total de pontos contratuais,deverá ser igual a Dados: Tabela de pesos para cálculo de pontos de função.
Elemento
Entrada
Saída
Arquivo

Simples

Médio

Complexo a) 3-
b) 4-

c) 5-

d) 6.

e) 7-

Comentários:

Informação 1:12 EE = 3 x 3 (Simples) + 4x4 (Médio) + 5x6 (Complexo) = 55;

Informação 2: 6 SE = 2 x 4 (Simples) + 4x5 (Médio) = 28.

Logo, temos um total de 55 + 28 = 83 Pontos de Função. No entanto, o desenvolvedor sabe que, por contrato, o sistema deve possuir um total de pontos de função igual a 118. Logo,faltam 118 - 83 =

35 Pontos de Função. Como sabemos que um ALI (Simples) equivale a 7 e faltam 35
Pontos de
Função, isso significa que temos 35/7 = 5 ALIs. Questão bem bacana :)

Gabarito: Letra C

15. (FGV / Senado Federal - 2012) Com relação ao tema de análise por pontos de função, avalie as afirmativas a seguir.
I. O termo Arquivo Lógico Interno designa um grupo de dados ou informações de controle,logicamente relacionados, reconhecido pelo usuário e mantido dentro da fronteira da aplicação.

II. O termo Saída Externa designa um processo elementar que processa dados ou informações de controle enviados de fora da fronteira da aplicação.
III. O termo Entrada Externa designa um processo elementar que envia dados ou informações de controle para fora da fronteira e que executa um processamento adicional baseado nestes dados ou controles.
Assinale:

a) se somente a alternativa I estiver correta.

b) se somente a alternativa II estiver correta.

c) se somente a alternativa III estiver correta.

d) se somente as alternativas I e II estiverem corretas.

e) se nenhuma alternativa estiver correta.

Comentários:

(I) Correto, perfeita definição de ALI; (II) Errado, isso seria uma Entrada Externa;
(III) Errado, isso seria uma Saída Externa.
Gabarito: Letra A

16.(FGV / MPM-MS- 2012) A NESMA- Netherlands Software Metrics Association (Associação de
Métricas de Software da Holanda) - é uma organização similar ao IFPUG, que mantém seu próprio Manual de Práticas de Contagens. A diferença entre as regras mantidas pela NESMA e as mantidas pelo IFPUG é que a NESMA reconhece três tipos de contagem de pontos de função.Assinale a alternativa que os indica.

a) Aplicativa, Metodológica e Aprimorada.

b) Detalhada, Estimativa e Indicada.

c) Real, Precisa e Resumida.

d) Complexa, Definida e Invertida.

e) Simplificada, Ajustada e Completa.

Comentários:

Detalhada, Estimativa e Indicativa - a questão diz "Indicada", mas podemos considerar como verdadeira.
Gabarito: Letra B

17. (FGV / DETRAN-RN - 2010) A equipe de métricas de software do TJPI realizou uma estimativa do tamanho da aplicação de processo eletrônico chamada SisProcessos. Utilizando a técnica deAnálise por Pontos de Função (APF), a equipe chegou ao valor de 100 pontos de função não ajustados. A equipe também levantou o valor de influência de cada uma das 14características gerais dos sistemas definidas pela técnica de APF, conforme listado a seguir:
COMUNICAÇÃO DE DADOS: 2
PROCESSAMENTO DISTRIBUÍDO: o
PERFORMANCE: 5

UTILIZAÇÃO DO EQUIPAMENTO: o
VOLUME DE TRANSAÇÕES: 5
ENTRADA DE DADOS "ON-LINE": 3
EFICIÊNCIA DO USUÁRIO FINAL: 3
ATUALIZAÇÃO "ON-LINE": 3

PROCESSAMENTO COMPLEXO: 1
REUTILIZAÇÃO DE CÓDIGO: 3
FACILIDADES DE IMPLANTAÇÃO: o
FACILIDADE OPERACIONAL: 3
MÚLTIPLOS LOCAIS: o
FACILIDADES DE MUDANÇAS: 3

A partir dessas informações, a equipe precisa finalizar a contagem através do cálculo dos pontos de função ajustados, cujo valor é expresso corretamente em:
a) 94;

b) 96;

c) 98;

d) 100;

e) 102.

Comentários:

Bastava somar o nível de influência das características gerais do sistema (SNI = 31)
e aplicar a fórmula PFA = PFNA x VFA = 100 x VFA. Vocês se lembram da fórmula do Fator de Ajuste? É assim:FA = (SNI x o,oi) + 0,65 = (31 x 0,01) + 0,65 = 0,31 + 0,65 - 0,96. Voltando à fórmula anterior,
temos que PA - 100 x 0,96 = 96.
Gabarito: Letra B

i8.(FGV / FIOCRUZ - 2010) Pontos por função - PF são derivados usando uma relação empírica baseada em medidas de contagem direta do domínio de informação do software e avaliação de complexidade do software. Um valor de domínio de informação é definido como uma entrada on-line, que resulta na geração de alguma resposta imediata do software, sob a forma de uma saída on-line. Esse valor de domínio de informação PE é denominado:
a) número de entradas externas (Externai Inputs - Eis).

b) número de saídas externas (Externai Outputs - EOs).

c) número de consultas externas (Externai Inquires - EQs).

d) número de arquivos lógicos internos (Internai Logical Files - ILFs).

e) número de arquivos de interface externa (Externai Interface Files - EIFs).

Comentários:

Entrada online que resulta na geração de uma resposta imediata na forma de uma saída online? T rata-
se de uma consulta externa! Porque não poderia ser uma entrada online, professor?
Porque ela não gera uma resposta imediata na forma de uma saída. Por que não poderia ser uma saída externa,professor? Até poderia, mas a descrição não menciona processamentos e cálculos matemáticos.

Gabarito: Letra C

ig.(FGV / FIOCRUZ - 2010) A métrica "Pontos de Função" (Function Point, FP)
é usada efetivamente como meio para medir a funcionalidade entregue por um sistema. Considerando dados históricos, analise as afirmativas associadas ao uso da FP.
I. Estimar o custo ou esforço necessário para projetar, codificar e testar o software.

II. Prever o número de erros que vão ser encontrados durante o teste.

III. Prever o número de componentes e/ou o número de linhas de código projetadas no sistema implementado.
Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente a afirmativa II estiver correta.

c) se somente a afirmativa III estiver correta.

d) se somente as afirmativas I e II estiverem corretas.

e) se todas as afirmativas estiverem corretas.

Comentários:

Dados históricos de análise de pontos defunção podem serutilizados para estimarcusto ou esforço necessário para projetar, codificar e testar o software; prever o número de erros que vão ser encontrados durante o teste; e prevero número de componentes e/ou o número de linhas de código projetadas no sistema implementado. Percebam: a questão não disse que a análise de pontos de função determina, por exemplo, o número de linhas de código. O que ocorre é que, por meio da contagem de pontos de funções, é possível inferir/prever a quantidade de componentes ou de linhas de código a partir dos dados históricos.
Gabarito: Letra E

2o.(FGV / BADESC - 2010) Acerca das características e conceitos da técnica de Análise de Pontos de Função (APF), avalie as afirmativas a seguir.
I. Um relatório com a totalização de dados é um exemplo de saída externa.

II. Um dos objetivos da APF é mediras funcionalidades do sistema, requisitadas e recebidas pelo usuário.
III. O termo "Arquivo", sob a ótica da APF, refere-se a um grupo de dados logicamente relacionados e reconhecido pelo usuário.
Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente as afirmativas I e II estiverem corretas.

c) se somente as afirmativas I e III estiverem corretas.

d) se somente as afirmativas II e III estiverem corretas.

e) se todas as afirmativas estiverem corretas.

Comentários:

(I) Correto. Como a totalização é um cálculo matemático, trata-se de uma saída externa (caso contrário, seria uma consulta externa); (II) Correto, esse é um dos objetivos da análise de pontos de função; (III) Correto, trata-se de um grupo de dados logicamente relacionado e reconhecido pelo usuário. Se ele for mantido dentro da fronteira da própria aplicação, é um ALI; se ele for mantido dentro da fronteira de outra aplicação, é um AIE.
Gabarito: Letra E

2i.(FGV / MEC - 2009) Num sistema de controle acadêmico, uma tela permite visualizar um relatório com três tipos diferentes de ordenação. O rodapé do relatório sempre traz o total de registros listados. Do ponto de vista da Análise de Pontos de Função, a totalização de registros listados pode ser contada como:
a) uma saída externa.

b) três saídas externas.

c) uma consulta externa.

d) um parâmetro externo.

e) três consultas externas.

Comentários:

Se o rodapé do relatório sempre traz o total de registros listados, então temos um somatório dos registros - que é um dado derivado. Logo, temos uma saída externa.
Gabarito: Letra A

22. (FGV/Senado Federal -2008) Considere as assertivas sobre a técnica de pontos de função para a estimativa de custo de desenvolvimento de um software:
I. A medida de pontos de função é independente da linguagem de implementação do software.

II. Os pontos de função são mais apropriados para medir os sistemas de processamento de dados dominados por operações de entrada e saída.
III. Existem grandes variações na contagem de pontos de função, dependendo do julgamento de quem fez a estimativa.
As assertivas corretas são:

a) somente II e III

b) somente I e II.

c) somente I e III.

d) I, lie III.

e) somente I.

Comentários:

(I) Correto, ela é independente de tecnologias; (II) Correto, tanto que se medem as funções de transação como Entrada Externa e Saída Externa; (III) Errado, existem diferenças, mas -em regra -
não devem ser grandes. No entanto, a banca considerou o terceiro item como correto -
eu divirjo do entendimento da banca.
Gabarito: Letra D

QUESTõES CoMENTADAS - DIvERSAS BANCAS

As questões 11 e 12 baseiam-se nas Figura io(a), io(b) e io(c). Sobre a Figura io(a), considere os seguintes aspectos:
(1) ela mostra uma tabela na qual constam, intencionalmente, os requisitos de software de um novo projeto de desenvolvimento de software, que serão completamente levantados e analisados apenas nos dois primeiros meses de trabalho;
(2) no primeiro mês, serão levantados e analisados os requisitos "Manter
Aluno", "Manter
Professor", "Manter Curso" e "Manter Disciplina";

(3) cada um dos "Manter", do primeiro mês, é composto unicamente pelas funcionalidades incluir,consultar, atualizar e excluir (CRUD). Por exemplo, "Manter Aluno" é composto,
apenas, pelos processos elementares "Incluir Aluno", "Consultar Aluno", "Atualizar Aluno" e "Excluir Aluno".
A Figura io(b) exibe uma visão geral do "Processo Unificado Rational" (RUP), no qual se inseriu, em alguns lugares, retângulos para ocultar qualquertexto existente nesses locais. A Figura io(c) mostra uma tabela utilizada para determinação da contribuição de Pontos de Função (PF) em contagens estimadas, segundo a NESMA (NESMA Early FPA Counting), na qual serão consideradas,apenas,
as "Entradas Externas" (EE), "Consultas Externas" (CE) e "Saídas Externas" (SE).

Requisitos de software a serem
Levantados e Analisados

12 Mês

(Módulo 1)
Manter Aluno
Manter Professor
Manter Curso
Manter Disciplina

29 Mês

(Módulo 2)
Manter Nota
Manter Frequência

Manter coordenador
Revisar lançamentos

Figura 10(a) - Requisitos de software

Figura 10(b) - Visão geral do RUP

Tipo de
Função

EE
SE
CE

Média de PF
4,3

5,4

3,8

Complexidade
Alta Média Baixa

6 4 3

7 5 4

6 4 3

Figura 10(c) - Tabela para determinação da contribuição de PF
í. (FUNDATEC / ISS-Porto Alegre - 2022) Sabe-se que em todos os processos elementares de"CONSULTA", dos "CRUD's" do primeiro mês, haverá contabilização, devendo ser apresentado,
no rodapé de cada página do relatório gerado, o número da página atual e o seu total, por exemplo, 1/5 (página 1 de 5). Nesse caso, considerando apenas as funções do tipo transação, a contagem estimada de Pontos de Função, do Módulo 1, segundo a NESMA, será um número:
a) Menor ou igual a 40.

b) Maior que 40 e menor ou igual a 50.

c) Maior que 50 e menor ou igual a 60.

d) Maior que 60 e menor ou igual a 70.

e) Maior que 70.

Comentários:

Primeira informação importante: a questão afirma que a contagem de pontos de funções deverá se basear no NESMA! Logo, podemos considerar que todas as funções de transação serão avaliadas como de complexidade funcional média.
Segunda informação importante: o enunciado pede para ser considerado na contagem de pontos de função apenas as funções de transação (CE, EE, SE), isto é, vamos ignorar solenemente as funções de dados (ALI, AIE).
Terceira informação importante: a questão nos informa que há uma contabilização de número de página no relatório gerado, logo não se trata de uma Consulta Externa (CE) e, sim,uma Saída
Externa (SE).

No primeiro mês, temos quatro requisitos: Manter Aluno, Manter Professor, Manter Curso e ManterDisciplina. Pelo enunciado, sabemos que cada um desses requisitos é composto pelas funcionalidades de incluir, consultar, atualizar e excluir. Sabemos que as funcionalidades de inclusão, alteração e exclusão são representadas como Entradas Externas (EE). E a consulta? Ela seria representada como uma Consulta Externa (CE), mas o enunciado nos disse que o relatório possui uma contabilização, logo será representado como uma Saída Externa (SE).
Dessa forma, para cada um dos quatro requisitos temos as seguintes funcionalidades:

-Inclusão: iEE

-Alteração: iEE

- Exclusão: 1 EE

-Consulta: iSE

Ocorre que a primeira informação importante nos disse que todas as funções de transação deveriam ser consideradas como de complexidade funcional média. Vamos consultar a tabela:
Tipo de
Função

EE
SE
CE

Média de PF
4,3

5,4

3,8

Complexidade

Alta Média Baixa
6 4 3

7 5 4

6 4 3

Sabendo que a complexidade média de uma Entrada Externa (EE) é 4 e que a complexidade média de uma Saída Externa (SE) é 5, podemos efetivamente aplicaras complexidades:
-Inclusão: iEE = 1x4 = 4

-Alteração: iEE = 1x4 = 4

-Exclusão: iEE=1x4=4

-Consulta: 1 SE = 1x5 = 5

Total: 17! Acabou, professor? Não! Esse é total para apenas um requisito,
mas temos quatro requisitos na questão. Logo, basta multiplicar por quatro: 17 x 4 = 68 (> 60 e <=70).
Gabarito: Letra D

2. (CEPUERJ / UERJ - 2021) Observe as seguintes descrições de funcionalidades que compõem um sistema de controle de ponto:
Rnpatru dr Ponta

Pnntipd mtençloc jtuaktv o ifqonro jpantaonmto

Ltadu» <ta teta Câheçftlho axsi nuote e logotipo <ta finpcfM,
comando (tarU Enter ou hotâo OK1 nvnugrm peno oraáno, indicador de ertrada oa Miita
Arounrot totondw apontanwtvtD

taitaxta etn Mn» <t»m luUdxrtiví

Principal mtrnçÀo atualuar as arquivai «puntunrato t paabficativa
Ltadoi ta teta Cabeçalho own nome e logotipo ta etnprtM.

cominóo ítecta Fnter ou botao OK|, mmMpnr pari o usuário. hora de entrada e |u»tifxibvaArquivoa MTBMíina aponustmio r tarttfratrra

Coaralta Apontamento Diário

PmxTpai intençto aprrxrur taóot do arquivo apontamento
Dados da teta Cabeçalho com nccne e logotipo da empresa,

comando (tecia Ertw oU Nxlo OKi nvnwgem para o anuário, data, hortrio de entrada, horário de uúdaAfquvca aottMbdoa apontamento

Considerando as complexidades e contribuições para funções de transação apresentadas noManual de Práticas de Pontos de Função do IFPUG , versão 4.3.1
desconsiderando qualquer funcionalidade não citada como, por exemplo, o login no sistema ou alteração dos registros , o número de transações do tipo entrada externa (EE), consulta externa (CE) e saída externa (SE), além do somatório de pontos de função (PF) de todas as funções do tipo transação é expresso corretamente em:
a) 2 entradas externas, 1 consulta externa, 1 saída externa, 15 PFs b) 2 entradas externas, 1 consulta externa, 1 saída externa, 14 PFs c) 2 entradas externas, 2 consultas externas, 15 PFs d) 2 entradas externas, 2 consultas externas, 14 PFs
Comentários:

- Primeira EE:

1ALR (arquivo de apontamento)
1 DER (horário do ponto)
Complexidade: BAIXA (3 pontos)

- Segunda EE:

2 ALR (arquivo de apontamento, arquivo de justificativa)
2 DERs (horário do ponto, justificativa)

Complexidade: BAIXA (3 pontos)

-CE:

3 DERs (data, horário de entrada, horário de saída)
iALR

Complexidade: BAIXA (3 pontos)

-SE:

6 DERs (data inicial, data final, matrícula, nome, total de horas, número de justificativas)
3 ALRs (pessoa, apontamento, justificativa)

Complexidade: MÉDIA (5 pontos)

Contagem final: 1 EE Baixa (3 pontos) + 1 EE Baixa (3 pontos) + 1 CE Baixa (3 pontos) + 1 SE Média

(5 pontos) = 14 pontos.

Gabarito: Letra B

3. (AOCP / Prefeitura de Novo Hamburgo - RS - 2020) Como se denomina um modelo de projeto preliminar usado para a estimativa de esforço inicial de um software e baseada nos seus requisitos?
a) Número de pontos de função.

b) Número de linhas de código.

c) Número de linhas de reúso.

d) Número de tabelas do sistema.

e) Número de pontos de aplicação.

Comentários:

Modelo usado para a estimativa de esforço inicial e baseada em requisitos é a quantidade de pontos de função. Professor, análise de pontos de função pode ser utilizada para medir esforço? Sim, ela é utilizada para medir o tamanho funcional de um software e, a partir dela, é possível estimar o esforço indiretamente.
Gabarito: Letra A

4. (AOCP / Prefeitura de Betim - MG - 2020) Considerando a métrica de pontos por função, os dados derivados da aplicação que fornecem informações para o usuário são classificados como:
a) entradas externas.

b) fator de ajuste.

c) arquivos lógicos internos.

d) arquivos de interface externos.

e) saídas internas.

Comentários:

A Saída Externa é o processo elementar que envia dados ou informações de controle para fora da fronteira da aplicação. Seu objetivo é exibir informações recuperadas através de processamento lógico que envolva cálculos ou criação de dados derivados e não apenas uma simples recuperação de dados. No entanto, a questão deveria ter sido anulada porque não existe SaídaInterna e, sim,
Saída Externa.

Gabarito: Letra E

5. (IBFC / TRE-PA - 2020) Conforme a IFPUG (International Function Point
Users Group), no
Manual de Práticas de Contagem de Pontos de Função, o primeiro passo para se fazer o cálculo do Valor do Fator de Ajuste (VAF) é o de avaliar cada uma das:
a) 14 características gerais do sistema na escala de o a 5 para determinar o nível de influência(NI)

b) 10 características gerais do sistema na escala de 0 a 3 para determinar o nível de influência
(NI)

c) 7 características gerais do sistema na escala de 1 a 3 para determinar 0 nível de influência
(NI)

d) 5 características gerais do sistema na escala de o a 5 para determinar o nível de influência
(NI)

Comentários:

A técnica de análise por pontos de função considera que alguns fatores - que estão relacionados com características da aplicação - podem afetar o tamanho funcional de um sistema. No cálculo dos PFNA não é levada em conta a tecnologia usada nem os requisitos não funcionais.E nós sabemos que há certas características que devem ser consideradas para se obter maior precisão sobre o cálculo.
Por essa razão, essas características são quantificadas de modo a obter um valor chamado Valor doFator de Ajuste (VFA) baseado em 14 características gerais de sistema (14 CGS). Com base nos requisitos do usuário, cada característica geral do sistema deve ter seu nível de influência avaliado numa escala de o a 5. Cada característica contém diretrizes para determinar o seu nível de influência.
Em suma: o primeiro passo para se fazer o cálculo do VAF é o de avaliar cada uma das 14características gerais do sistema na escala de o a 5 para determinar o nível de influência.

Gabarito: Letra A

6. (VUNESP / EBSERH - 2020) A métrica de software baseada em pontos de função:

a) possui 12 fatores de ajuste de valor.

b) independe do número de entradas externas do programa.

c) depende do número de usuários simultâneos do programa.

d) considera o número de desvios incondicionais existentes.

e) leva em conta o número de arquivos lógicos internos.

Comentários:

(a) Errado, são 14 características gerais de sistema e, não, 12 fatores de ajuste;
(b) Errado, depende do númerode entradas externas; (c) Errado, ela mede otamanhofuncional de um software baseado na visão do usuário - não há dependência do número de usuários simultâneos;(d) Errado, a quantidade de desvios incondicionais existentes é irrelevante - nem sequer se analisa código; (e)Correto, é realmente dependente da quantidade de arquivos lógicos internos.

Gabarito: Letra E

7. (VUNESP / Câmara de Piracicaba - SP - 2019) Uma das principais métricas utilizadas para avaliação de software é a Métrica por Pontos de Função. Tal tipo de métrica considera alguns valores denominados de domínio da informação, dentre os quais se inclui o número de:
a) chamadas de função.

b) desvios incondicionais c) entradas externas.
d) estruturas complexas.

e) variáveis internas.

Comentários:

A análise de pontos de função pode ser aplicada em diversos domínios funcionais ou domínios de informação. O que é isso? É uma área de interesse (Ex: sistema de uma universidade, hospital,
banco, entre outras). Dentre as alternativas, a única que apresenta valores de domínio da informação é a Entrada Externa (EE).
Gabarito: Letra C

8. (Avança SP / Câmara Municipal de Taboão da Serra - SP - 2019) No que se refere à análise de pontos por função, analise os itens a seguir e, ao final, assinale a alternativa correta:
I - Pontua a complexidade do código desenvolvido em Java.

II - Analisa arquivos, arquivos de interface externa, entradas do usuário, saídas do usuário e consultas do usuário.
III - É um método para elicitação de requisitos.

a) Apenas o item I é verdadeiro.

b) Apenas o item II é verdadeiro.

c) Apenas o item III é verdadeiro.

d) Apenas os itens I e III são verdadeiros.

e) Todos os itens são verdadeiros.

Comentários:

(I) Errado, a análise de pontos de função independe da tecnologia utilizada;
(II) Correto, está realmente perfeita; (III) Errado, não há nenhuma relação com elicitação de requisitos.
Gabarito: Letra B

9. (ACEP / Prefeitura de Aracati - CE - 2019) Uma das atribuições mais comuns na
Gerência de
Projetos de software é realizar estimativa de software. Sobre essas estimativas, é correto afirmar que:
a) a estimativa baseada em Pontos de Função são dependentes da estrutura tecnológica para a qual se pretende desenvolver software.
b) através da Análise de Pontos de Função, um gerente de projetos é capaz de realizarestimativa de software mesmo sem experiência na área.
c) métricas de dimensão de sistema, como o LOC, e de produtividade são dependentes da linguagem de programação empregada.
d) o COCOMO 2 é um modelo em dois níveis: Nível Pós-Arquitetura e Nível
Inicial de
Prototipação.

Comentários:

(a) Errado, é independente da estrutura tecnológica; (b) Errado, mas eu acho a redação desse item confusa: ele quis dizer'experiência' no sentido de já terfeito contagens anteriores ou no sentido de conhecer o método de contagem dos pontos de função? Ele precisa ao menos conhecer o método de contagem para realizar a estimativa, mas não precisa ter experiência de contagens anteriores;
(c) Correto, esse tipo de métrica - sim - é realmente dependente da linguagem de programação empregada; (d) Errado, esse modelo tem três níveis- faltou mencionar o nível inicial de projeto.
Gabarito: Letra C

io.(CESGRANRIO / TRANSPETRO - 2018) Um pequeno sistema passou por um processo de contagem de pontos de função, resultando na Tabela abaixo.
Entrada Externa
Saída Externa
Consulta Externa

Arquivo de Interface Externa
Arquivo Lógico Interno

Baixa

Média

Alta

Quantos pontos de função não ajustados tem tal sistema?

a) 103

b) 106

c) 120

d) 121

e) 122

Comentários:

FUNÇÕES DE DADOS E TRANSAÇÃO

CONSULTA EXTERNA (CE]
ENTRADA EXTERNA (EE)
SAÍDA EXTERNA (SE)
ARQUIVO DE INTERFACE EXTERNA (AIE)
ARQUIVO LÓGICA INTERNA (ALI)

Dada a tabela, temos que:

EE -> 2*3 + 1*4 + 1*6 = 6+4+6 = i6
SE 1*4 + 4*5 + 1*7 = 4 + 20 + 7 = 3i
CE o*3 + o*4 + o*6 = 0+0+0 0

AIE-> 0*5 + 0*7 + 1*10 = 0 + 0 + 10 10

| COMPLEXIDADE FUNCIONAL |

| BAIXA | MÉDIA | ALTA |

ALI 2*7 + 2*10 + 2*15 = 14 + 20 + 30= 64

Somando tudo, temos: 16 + 31 + o + 10 + 64 = 121.

Gabarito: Letra D

11. (IBFC / EBSERH - 2018) Na análise de pontos de função, as funções transacionais representam as funcionalidades efetivamente fornecidas para o usuário e são categorizadas em entradas externas, saídas externas e consultas externas.
Comentários:

Essas são - de fato - as funções transacionais...

Gabarito: Correto

12. (IBFC / EMBASA - 2017) A NESMA reconhece três métodos de Análise de Pontos de
Função
(APF), que são métodos de Medição de Tamanho Funcional (FSM) autossuficientes. Esse três métodos são respectivamente:
a) APF Detalhada, APF de Alto Nível (ou APF Estimada) e APF Indicativa b) APF Generalista, APF de Baixo Nível (ou APF Arcaica) e APF Indicativa c) APF Generalista, APF de Alto Nível (ou APF Estimada) e APF Específica d) APF Detalhada, APF de Baixo Nível (ou APF Arcaica) e APF Específica.
Comentários:

Os três métodos são: Contagem Detalhada, Estimada e Indicativa.

Gabarito: Letra A

13. (IBFC / EBSERH - 2017) O primeiro passo a ser seguido para a contagem de PF
(Pontos de
Função) de um projeto de software é determinar o tipo de contagem. Neste passo é estabelecido o tipo de contagem que será usado para medir o projeto de software,tanto no processo como no produto. Assinale a alternativa que apresenta três tipos de contagem possíveis:
a) do projeto de integração, do projeto de melhoria (manutenção), de depuração (testes)

b) do projeto de desenvolvimento, do projeto de requerimentos (requisitos), da aplicação(produção)

c) do projeto de desenvolvimento, do projeto de melhoria (manutenção), da aplicação(produção)

d) do projeto de integração, do projeto de requerimentos (requisitos), de depuração (testes)

e) do projeto de desenvolvimento, do projeto de requerimentos (requisitos), de depuração(testes).

Comentários:

Os tipos de contagem são de desenvolvimento, melhoria/manutenção e aplicação/produção.

Gabarito: Letra C

íZf.OBFC / EBSERH -2017) Um dos passos básicos na contagem de pontos de função inclui contar os tipos de funções de dados identificados pelas siglas ALI e AIEque representam respectivamente:
a) Árvore da Logística Interna - Árvore de Integração Externa b) Arquivo Lógico Interno - Arquivo de Interface Externa c) Arquitetura Lógica Interna - Arquitetura Integrada Externa d) Artefatos Lógicos Internos - Artefatos de Integração Externa e) Acervo de Livros Internos - Acervo de Interfaces Externas.
Comentários:

ALI é o Arquivo Lógico Interno; AIE é o Arquivo de Interface Externa.

Gabarito: Letra B

15. (IBFC / EBSERH - 2017) O conceito de Ponto de Função foi definido originalmente em 1977 naIBM e é padronizada internacionalmente pela ISO. Pode-se definir o conceito de Ponto deFunção como sendo:

a) uma unidade de medida de software para estimar o tamanho de um sistema de informação baseando-se na funcionalidade percebida pelo usuário do sistema, independentemente da tecnologia usada para implementá-lo.
b) uma medida de tamanho de software que estima o esforço (número de pessoas-hora) e o prazo associados ao desenvolvimento dos programas e sistemas por meio da quantidade de linhas de código-fonte (SLOC - Source Lines Of Code).
c) a medição do software por meio de uma indicação quantitativa da extensão,
quantidade,
dimensão, capacidade ou tamanho dos programas e sistemas através da velocidade de execução em um computador padrão.
d) é uma métrica ou um indicador, ou a combinação dos dois, que fornece compreensão do processo de software, de um sistema de informação basicamente utilizando medidas diretas tais como a complexidade ciclomática de um programa ou sistema.
Q-Q SERPRO (Analista - Especialização: Tecnologia) Engenharia de software - 2023
(Pós-Edital)

e) é uma medida de software, que possibilita um conjunto de métricas de qualidade e produtividade, fortemente ligado à linguagem de programação utilizada,impossibilitando a utilização de dados históricos para projetos que não utilizam a mesma linguagem.
Comentários:

(a) Correto, é realmente uma unidade de medida para estimarotamanho de um sistema baseando-se na funcionalidade percebida pelo usuário do sistema, independente da tecnologia; (b)
Errado,
ela não mede o esforço diretamente (apenas indiretamente) e definitivamente não utiliza a quantidade de linhas de código; (c) Errado, não há nenhuma relação com a velocidade de execução em um computador; (d) Errado, ela não oferece compreensão do processo de software e não utiliza complexidade ciclomática; (e) Errado, não é ligado à linguagem de programação ou outras tecnologias e possibilita -sim -utilização de dados históricos.
Gabarito: Letra A

i6.(IBFC / EBSERH - 2016) Um dos passos básicos na contagem de pontos de função inclui contar os tipos de funções de dados identificados pelas siglas ALI e AIEque representam respectivamente:
a) Árvore da Logística Interna - Árvore de Integração Externa b) Arquivo Lógico Interno - Arquivo de Interface Externa c) Arquitetura Lógica Interna - Arquitetura Integrada Externa d) Artefatos Lógicos Internos - Artefatos de Integração Externa e) Acervo de Livros Internos - Acervo de Interfaces Externas.
Comentários:

ALI é o Arquivo Lógico Interno e AIE é o Arquivo de Interface Externa.

Gabarito: Letra B

i7-(ESAF / ANAC - 2016) Segundo a versão 2.0 do Roteiro de Métricas de Software do
SISP, o grupo de dados, logicamente relacionados, reconhecido pelo usuário, mantido por meio de um processo elementar da aplicação que está sendo contada, é o:
a) Arquivo de Interface Externa.

b) Arquivo Lógico Externo.

c) Arquivo Lógico Interno.

d) Arquivo de Interface Interno.

e) Arquivo de Interface Lógica.

Comentários:

O grupo de dados, logicamente relacionados, reconhecido pelo usuário, mantido por meio de um processo elementar da aplicação que está sendo contada, é o Arquivo Lógico Interno (ALI).
Gabarito: Letra C

i8.(IBFC/EBSERH -2015) De acordo com as Métricas de Software, a Análise de Pontos de
Função é uma técnica de medição das funcionalidade fornecida por um software sob o ponto de vista:
a) do Gerente do Projeto.

b) dos Usuários.

c) do Programador.

d) do Analista de Sistema.

e) do Engenheiro de Software.

Comentários:

É uma técnica de medição das funcionalidade fornecida por um software sob o ponto de vista dos usuários...
Gabarito: Letra B

ig.(IDECAN / PRODEB-2015) A APF (Análise de Pontos de Função) pode ser definida como sendo uma técnica para medir as funcionalidades fornecidas por um determinado software, do ponto de vista do usuário. O ponto de função é a unidade de medida desta técnica, e o objetivo principal étornara medição independente datecnologia que se utiliza para construir o software.Em resumo, a APF busca medir o que realmente o software faz e não da forma que ele foi construído. Uma dessas funções é a do tipo dado que representa a funcionalidade que está sendo fornecida pela aplicação, ou seja, representa os seus arquivos de armazenamento de dados. São classificados nas seguintes categorias:
a) Arquivos Lógicos Internos (ALI); Arquivos de Interface Externa (AIE).

b) Arquivos Lógicos Referenciados (ALR); Arquivos Lógicos Internos (ALI).

c) Arquivos de Interface Externa (AIE); Arquivos Lógicos Referenciados (ALR).

d) Arquivos de Interface Externa (AIE); Arquivos Referenciados Externos (AER).

Comentários:

(a) Correto, ambas são categorias de funções do tipo dado; (b) Errado,
Arquivos Lógicos
Referenciados não são uma função do tipo dado; (c) Errado, Arquivos Lógicos
Referenciados não são uma função do tipo dado; (d) Errado, Arquivos Referenciados Externos não existem.
Gabarito: Letra A

2O.(IESES / MSGÁS - 2015) O sistema de reservas de automóveis de uma locadora possui uma funcionalidade que consiste em uma interface web para entrada de dados do cliente e armazenamento desses dados num banco de dados relacional. Considerando o contexto daAnálise de Pontos de Função, esta função disponibilizada pela interface no sistema será contada como:
a) Um Arquivo de Interface Externa (AIE), pois a interface permite a entrada de dados.

b) Uma Entrada Externa (EE), pois existe mudança de comportamento do sistema.

c) Uma Saída Externa (SE), pois existe dados derivados na transação.

d) Um Arquivo Lógico Interno (ALI), pois os dados foram salvos no banco de dados.

Comentários:

Temos uma interface web para entrada de dados do cliente e armazenamento desses dados em um banco de dados relacional, portanto temos uma entrada externa - visto que se trata de um cliente inserindo dados que modificam o comportamento do sistema.
Gabarito: Letra B

2i.(VUNESP / PRODEST-ES - 2014) Na métrica de software conhecida como ponto por função,
são considerados valores do domínio da informação. Dois desses domínios são: o número de a) desvios condicionais e de arquivos lógicos internos.
b) entradas externas e de consultas externas.

c) estruturas complexas e de loops e cases.

d) registros das tabelas e de arquivos de interface externa.

e) tabelas e de saídas externas.

Comentários:

Os valores de domínio da informação são o número de Entradas Externas e Consultas Externas.

Gabarito: Letra B

22. (AOCP / UFPB - 2014) Preencha a lacuna e assinale a alternativa correta.

"Na análise de pontos de função, os requisitos funcionais devem ser identificados conforme

//

a) a visão do programador.

b) a visão do usuário.

c) a tecnologia.

d) a linguagem de programação utilizada.

e) o sistema gerenciador de banco de dados utilizado.

Comentários:

Na análise de pontos de função, os requisitos funcionais devem ser identificados conforme a visão do usuário.
Gabarito: Letra B

23. (UFBA / UFSBA - 2014) Pontos de Função apenas medem o tamanho funcional do software baseando-se em uma avaliação padronizada dos requisitos dos usuários e, diferentemente deLinhas de Código, não são dependentes da implementação física e das linguagens utilizadas no desenvolvimento do software.
Comentários:

Galera, que item maravilhoso - é uma das coisas mais lindas que eu já vi. Tudo perfeito...

Gabarito: Correto

24-(ESAF/ SUFRAMA-2013) O fator de ajuste indica a:

a) viabilidade geral provida pelo projeto ou aplicação para o desenvolvedor.

b) ajustabilidade provida pelo projeto para a aplicação.

c) funcionalidade geral provida pelo projeto ou aplicação para o usuário.

d) funcionalidade geral provida pela aplicação do projeto.

e) funcionalidade setorial provida pelo projeto ou aplicação para as interfaces.

Comentários:

O fator de ajuste indica a funcionalidade geral provida pelo projeto ou aplicação para o usuário.

Gabarito: Letra C

25.OBFC / EBSERH - 2013) Se o total de Pontos de Função não ajustados for 107, e o nível de influência geral dado é 30, teremos como total de pontos de função ajustados:
a) 91,65

b) 100,65

c) 101,65

d) 102,65.

Comentários:

Vamos lembrar da fórmula: PFA = PFNA x [(NI x 0,01) + 0,65]. Se os Pontos de
Função Não-
Ajustados (PFNA) é 107 e o Nível de Influência é 30, então temos que: PFA = 107 x [(30x0,01)4-0,65]

= 107 x [(0,3) 4- 0,65] = 107 x 0,95 = 101,65.

Gabarito: Letra C

26.(IBFC / EBSERH -2013) Em APF (Análise de Pontos de Função) existe o importante conceito dePonto de Função. Pode-se conceituar basicamente Ponto de Função como:

a) a medida do tamanho funcional do software.

b) a capacidade do hardware para processar o sistema.

c) a relação entre o hardware e o software exigido pelo sistema.

d) o ciclo de software composto pelo sistema.

Comentários:

Ponto de Função é realmente a medida do tamanho funcional do software - as outras opções não fazem qualquer sentido.
Gabarito: Letra A

27-(ESAF / CGU - 2012) São características gerais de sistema utilizadas para cálculo do fator de ajuste:
a) Reutilização, Taxa de recepção de dados.

b) Atualização off-line, Modificações facilitadas.

c) Modificações facilitadas, Processamento paralelo.

d) Entrada de dados off-line, Compatibilidade Web.

e) Múltiplos locais, Processamento complexo.

Comentários:

(a) Errado, taxa de recepção de dados não é uma característica geral do sistema; (b)
Errado,
atualização off-line não é uma característica geral do sistema; (c) Errado,
processamento paralelo não é uma característica geral do sistema; (d) Errado, ambos não são características gerais do sistema; (e) Correto, ambos são características gerais do sistema.
Gabarito: Letra E

28.(ESAF / CGU - 2012) São exemplos de ALI:

a) Arquivos de índices.

b) Arquivos temporários, de trabalho ou de classificação.

c) Arquivos de backup.

d) Arquivos de mensagens de erro desde que mantidos pela aplicação.

e) Arquivos introduzidos exclusivamente em função da tecnologia utilizada.

Comentários:

A única opção que apresenta um exemplo de ALI são os arquivos de mensagens de erro.

Gabarito: Letra D

2g.(ESAF / CGU - 2012) Cada Arquivo Lógico Interno e cada Arquivo de Interface
Externa devem ser classificados com relação à sua complexidade funcional com base em:
a) Número de Tipos de Dados, Número de Tipos de Registros.

b) Número de Tipos de Arquivos, Número de Tipos de Registros.

c) Número de Tipos de Dados, Número de Tipos de Consultas.

d) Número de Tipos de Campos, Número de Tipos de Arquivos.

e) Número de Tipos de Tabelas, Número de Tipos de Campos.

Comentários:

Cada Arquivo Lógico Interno e cada Arquivo de Interface Externa devem ser classificados com relação à sua complexidade funcional com base em Tipos de Dados e Tipos de Registro.
Gabarito: Letra A

30. (ESAF / CGU - 2012) São características gerais de sistema utilizadas para cálculo do fator de ajuste:
a) Reutilização, Taxa de recepção de dados.

b) Atualização off-line, Modificações facilitadas.

c) Modificações facilitadas, Processamento paralelo.

d) Entrada de dados off-line, Compatibilidade Web.

e) Múltiplos locais, Processamento complexo.

Comentários:

14 CARACTERÍSTICAS GERAIS DO SISTEMA (CGSJ

01-COMUNICAÇÃO DE DADOS 08-ATUALIZAÇÃO ONLINE

02-PROCESSAMENTO DISTRIBUÍDO 09-PROCESSAMENTO COMPLEXO

03-PERFORMANCE 10-REUSABILIDADE

04-CONFIGURAÇÃO D0 EQUIPAMENTO

05-VOLUME DE TRANSAÇÕES

06-ENTRADADE DADOS ONLINE

11- FACILIDADE DE IMPLANTAÇÃO

12- FACILIDADE OPERACIONAL

13- MÚLTIPLOS LOCAIS

07-INTERFACE C0M0 USUÁRIO 14-FACILIDADE DE
MUDANÇAS

As características são múltiplos locais e processamento complexo.

Gabarito: Letra E

31. (CONSULPLAN /TSE-2012) A análise de Ponto de Função engloba diversas etapas, sendo que a contagem está associada fundamentalmente a projetos de desenvolvimento e de melhoria.Nesse contexto, uma função é representada pelas necessidades do usuário em termos de processamento de dados e que caracteriza a lógica, sendo identificadas como entradas externas(EE), saídas externas (SE) e consultas externas (CE). Essa descrição caracteriza o tipo denominado Funções a) Dados.
b) Processos.

c) Transacionais.

d) Organizacionais.

Comentários:

EE, SE e CE são funções de transação ou transacionais.

Gabarito: Letra C

32.(ESAF - 2010 - SUSEP - Analista de Sistemas) Na contagem de Arquivos
Lógicos
Referenciados (ALR):

a) não se deve contar ALR para Arquivo Lógico Interno mantido.

b) deve-se contar dois ALR caso haja acesso a arquivo de mensagens de erros.

c) deve-se contar um ALR caso haja acesso apenas a arquivos criptografados.

d) deve-se contar um ALR para cada par de Arquivos Lógicos Internos que são lidos e mantidos por entidades externas distintas.
e) deve-se contar apenas um ALR para cada Arquivo Lógico Interno que é lido e mantido por uma entidade externa.
Comentários:

Um ALR é um ALI/AIE que foi acessado por uma função de transação. No entanto, a redação da questão ficou horrível! Se o ALR é lido e mantido por uma entidade externa, então ele é um AIE e,não, um ALI. Galera, vocês têm que aprender a abstrair essas coisas e tentar imaginar o que o examinador queria avaliar. É claro que, apesar da escrita estranha, ele queria avaliar se o aluno sabe que não se deve contar duas vezes, isto é, se um ALI é um AIE de outra aplicação,conta-se apenas uma vez.
Gabarito: Letra E

33- (ESAF / MPOG - 2010) Assinale a afi rmativa correta relativa à Análise por Pontos de Função
(APF).

a) Uma Consulta Externa é um relacionamento composto por entradas que resultam em uma exclusão de informação.
b) A complexidade de um Arquivo Lógico Interno é calculada a partir da quantidade de
Registros
Físicos Direcionados.

c) O objetivo principal da APF é medir a funcionalidade de um software ou aplicativo,
baseando-
se primeiramente no desenho lógico e de acordo com a perspectiva do usuário.

d) São Arquivos Lógicos Internos: cadastros de clientes e de produtos, arquivo de classificação e arquivos temporários.
e) A quantidade de Arquivos Lógicos Internos é calculada a partir da quantidade de
Arquivos
Referenciados e da manipulação de Dados Elementares.

Comentários:

(a) Errado, resultam apenas na recuperação dos dados; (b) Errado, é a partir da quantidade deRegistros Lógicos Referenciados; (c) Correto, esse é o objetivo principal; (d) Errado,
arquivos de classificação e temporários não são; (e) Errado, é a partir da quantidade deRegistros Lógicos
Referenciados e Dados Elementares Referenciados.

Gabarito: Letra C

34.(ESAF / CVM - 2010) O cálculo dos pontos de função de um projeto de desenvolvimento consiste dos componentes de funcionalidade:
a) reusabilidade de aplicação; reusabilidade de conversão; fator de ajuste da aplicação.

b) funcionalidade de aplicação; funcionalidade de compressão; fator de ponderação da aplicação.
c) reusabilidade de aplicação; funcionalidade de programação; fator de ajuste da aplicação.

d) funcionalidade de aplicação; funcionalidade de conversão; fator de ajuste da aplicação.

e) funcionalidade de programação; funcionalidade de conversão;
funcionalidade de manutenção.
Comentários:

É a funcionalidade da aplicação, funcionalidade de conversão, e fator de ajuste da aplicação.

Gabarito: Letra D

35. (ESAF / CVM - 2010) Algumas das Características Gerais do Sistema (CGS) são:

a) Comunicação de Dados. Funções intrínsecas. Performance. Especificação de equipamento.
Saída de dados on-line. Processamento complexo. Reusabilidade.
Facilidade de
Implementação.

b) Transmissão de Dados. Funções distribuídas. Modularidade. Fornecedores de equipamentos.
Entrada de dados on-line. Processamento complexo. Reengenharia. Múltiplos subprogramas.

c) Comunicação de Dados. Servidores distribuídos. Performance.
Configuração de equipamento. Entrada de dados on-line. Processamento cognitivo. Facilidade deManutenção.
Múltiplos locais.

d) Comunicação de Dados. Funções distribuídas. Performance. Configuração de equipamento.
Entrada de dados on-line. Processamento complexo. Reusabilidade. Facilidade de Implantação.

e) Transmissão de Dados. Ações distribuídas. Performance. Configuração de equipamento.Entrada de dados on-line e off-line. Direcionamento complexo. Reusabilidade.
Facilidade de
Implantação.

Comentários:

01-COMUNICAÇÃO DE DADOS

02-PROCESSAMENTO DISTRIBUÍDO

03-PERFORMANCE

04-CONFIGURAÇÃO DO EQUIPAMENTO

05-VOLUME DE TRANSAÇÕES

06-ENTRADADE DADOS ONLINE

07-INTERFACE C0M0 USUÁRIO

14 CARACTERÍSTICA GERAIS DO SISTEMA (CGS]

08-ATUALIZAÇÃO ONLINE

09-PROCESSAMENTO COMPLEXO

10- REUSABILIDADE

11- FACILIDADE DE IMPLANTAÇÃO

12- FACILIDADE OPERACIONAL

13- MÚLTIPLOS LOCAIS

14- FACILIDADE DE MUDANÇAS

Trata-se da quarta opção! O examinador utilizou uma tradução errada para
Processamento
Distribuído, chamando-o de Funções Distribuídas, mas o restante está correto...

Gabarito: Letra D

36.(ESAF / CVM - 2010) Baseando-se nas Características Gerais do Sistema (CGS), um dos passos para o cálculo do fator de ajuste é:
a) avaliar o impacto de cada uma das 14 CGS no aplicativo que está sendo contado,
atribuindo peso de 0 a 5 para cada característica.
b) calcular o nível de influência por meio da multiplicação dos pesos de cada uma das 14 CGS.

c) avaliar as entradas de cada uma das 14 CGS no aplicativo que está sendo contado,
atribuindo peso de 0 a 10 para cada característica.
d) avaliar o impacto de cada uma das 14 CGS no aplicativo que está sendo contado,
atribuindo peso de 0 a 10 para cada característica.
e) calcular o nível de influência por meio da soma dos pesos da primeira metade das 14 CGS.

Comentários:

Avalia-se o impacto de cada uma das 14 CGS no aplicativo que está sendo contado,
atribuindo peso de 0 a 5 para cada característica.
Gabarito: Letra A

37-(ESAF / CVM - 2010) Considerando Arquivos de Interface Externa (AIE), na contagem deRegistros Lógicos Referenciados (RLR),

a) caso não haja um subgrupo de informações, conte um RLR para cada dupla de AIE.

b) conte um RLR para cada subgrupo de dados de um AIE, somente quando o subgrupo for mandatório.
c) conte um RLR para cada subgrupo de dados de um AIE, somente quando o subgrupo for opcional.
d) caso não haja um subgrupo de informações, não conte RLR para nenhum AIE.

e) conte um RLR para cada subgrupo de dados de um AIE, seja o subgrupo opcional ou mandatório.
Comentários:

Deve-se contar um RLR para cada subgrupo de dados de um AIE, seja o grupo opcional ou mandatário.
Gabarito: Letra E

38.(ESAF / SUSEP - 2010) São Características Gerais do Sistema (CGS) do fator de ajuste que avaliam a funcionalidade geral da aplicação:
a) Performance, Pontos de transição e Composição on-line.

b) Comunicação de dados, Interface com o usuário e Reusabilidade.

c) Taxa de acertos, Funções de transações e Atualização on-line.

d) Saída de dados on-line, Facilidade de planejamento e Performance.

e) Comunicação de transações, Interação entre programas e Usabilidade.

Comentários:

(a) Errado, apenas performance é uma característica geral do sistema; (b)
Correto, todas são características gerais do sistema; (c) Errado, apenas atualização on-line é uma característica geral do sistema; (d) Errado, apenas performance é uma característica geral do sistema; (e) Errado,nenhum é uma característica geral do sistema.

Gabarito: Letra B

LISTA DE QUESTõES - CESPE

í. (CESPE / Ministério de Economia - 2020) As informações a seguir são relativas a uma mensuração de sistemas em pontos de função.
I manutenção de sete páginas HTML estáticas no portal da organização, contida em um projeto de desenvolvimento
II manutenção na interface, especificamente de logotipos, e mudança de botões da aplicação,que totalizam nove pontos de função transacionais impactados

III criação de identidade visual para dez páginas do portal associadas à área de comunicação social da organização função consultas externas (CE)
arquivos de interface externa (AIE)
entradas externas (EE)

arquivos lógicos internos (AL1)

complexidade baixa média alta alta quantidade
]

Tendo como referência as informações precedentes, julgue o próximo item, de acordo com o roteiro de métricas de software do SISP (versão 2.1).
De acordo com a tabela apresentada, as funções de dados representam mais de 55 pontos de função.
2. (CESPE / Ministério de Economia - 2020) As informações a seguir são relativas a uma mensuração de sistemas em pontos de função.
I manutenção de sete páginas HTML estáticas no portal da organização, contida em um projeto de desenvolvimento
II manutenção na interface, especificamente de logotipos, e mudança de botões da aplicação,que totalizam nove pontos de função transacionais impactados

III criação de identidade visual para dez páginas do portal associadas à área de comunicação social da organização função consultas externas (CE)
arquivos de interface externa (AIE)
entradas externas (EE)

arquivos lógicos internos (AL1)

complexidade baixa média alta alta quantidade
]

Tendo como referência as informações precedentes, julgue o próximo item, de acordo com o roteiro de métricas de software do SISP (versão 2.1).
De acordo com os dados da tabela apresentada, as funções transacionais representam 21
pontos de função.
3- (CESPE / Ministério de Economia - 2020) Uma técnica paramétrica para estimativa de esforço para desenvolvimento de software é a análise por pontos de função, que se baseia em linhas de código que são convertidas em valores numéricos, os quais, depois de ajustados à capacidade da empresa desenvolvedora, representarão o esforço necessário para se desenvolver o sistema.
4. (CESPE / Ministério de Economia - 2020) A identificação de funções de dados e de tipos funcionais somente deve ocorrer após o estabelecimento da fronteira da contagem.
5. (CESPE / Ministério de Economia - 2020) A estimativa de esforço de projeto de software,representada pela fórmula a seguir, deve ser usada em substituição à contagem por pontos de função quando esta não for suficiente para estimar o tamanho do projeto, esforço(horas) =
tamanho (PF) x índice de produtividade (HH/PF).

6. (CESPE / Ministério de Economia - 2020) A identificação de requisitos funcionais é resultado da análise da documentação do projeto, primeira atividade do procedimento de contagem dePF do Manual de Práticas de Contagem (CPM).

7. (CESPE / Ministério de Economia - 2020) Na métrica de pontos por função,
entradas externas,
saídas externas e consultas externas são computadas separadamente.

8. (CESPE / Ministério de Economia - 2020) A análise de pontos de função é utilizada para medir o tamanho das funções que serão construídas de acordo com a visão do usuário, e não do desenvolvedor.
9. (CESPE / SLU-DF - 2019) A contagem das funções de transações (FT) deve ser precedida pela contagem dos tipos de funções de dados.
10. (CESPE / SLU-DF-2019) Os pontos porfunção não ajustados (PFNA) devem ser multiplicados pelo seu fator de ajuste (FA) para que se obtenha, assim, o valor final dos pontos por função.
11. (CESPE / TJ-AM - 2019) A partir dos resultados apresentados pela métrica ponto por função, é possível estimar a quantidade de erros que serão encontrados durante o teste.
12. (CESPE / TJ-AM - 2019) Na contagem dos tipos de elementos usados para a determinação da complexidade dos tipos de função, os tipos de elementos de registro correspondem ao número de campos distintos e não repetitivos identificáveis pelo usuário.
13. (CESPE / TJ-AM - 2019) Devido a suas características, uma tela de login pode ser considerada como um exemplo de consulta externa em uma contagem de pontos de função.
14.(CESPE / STM -2018) As funcionalidades de conversão de dados serão contadas como entrada externa, no caso da carga inicial dos dados, e como consultas ou saídas externas,quando o usuário solicitar relatório associado à funcionalidade de migração de dados.
15. (CESPE / STM - 2018) Segundo a Nesma, a contagem indicativa considera a quantidade existente de arquivos lógicos internos e de interface externa, considerando,ainda, que toda função do tipo dado tem sua complexidade funcional avaliada como baixa e as funções transacionais avaliadas como de complexidade média.
16. (CESPE / CGM-PB - 2018) A APF é capaz de medir projetos de desenvolvimento e manutenção de software, com a restrição de ser dependente da tecnologia de implementação.
17. (CESPE / TRE-BA - 2017) Na contagem de pontos de função inicial de uma aplicação, consiste em uma saída externa a:
a) consulta que calcula o valor de um boleto a ser pago com juros e multa por atraso.

b) listagem dos nomes de todos os clientes de um estabelecimento comercial.

c) tela onde é possível alterar a tabela de desconto a ser concedido para cada tipo de cliente.

d) recuperação de um texto de ajuda guardado no sistema como imagem.

e) atualização em lote das vendas efetuadas por uma loja em um dia.

18.(CESPE/TCE-PR-2016) Com relação à técnica análise de pontos de função (APF) utilizada para estimarfuncionalidades de um software, assinale a opção correta.
a) Os pontos de funções não ajustados são calculados por meio da soma dos arquivos lógicos internos (ALIs) e dos arquivos de interface externa (AlEs).
b) No processo de contagem de pontos por função do IPFUG, a identificação da fronteira da aplicação antecede a determinação do tipo de contagem.
c) A APF deve ser aplicada exclusivamente em projetos de software que utilizam metodologias ágeis, antes do início do desenvolvimento do software.
d) Os pontos porfunção não ajustados devem serdeterminados antes do cálculo dos pontos por função ajustados.
e) O fator de ajuste é calculado com base em três princípios da qualidade de software: facilidade de alteração, facilidade de instalação, facilidade de operação.
19.(CESPE / TCU - 2015) Quando duas ou mais aplicações mantém e(ou) referenciam a mesma função de dados, deve-se contar os DERs (dados elementares referenciados) de todas as funções de dados das aplicações envolvidas.
20.(CESPE I MPOG-ATI - 2015) A aplicação da análise de pontos de função determina o custo do software a ser desenvolvido, independentemente dos índices de produtividade de cada empresa.
21. (CESPE / STJ - 2015) Na contagem de pontos de função, deve-se contar um dado elementar referenciado (DER), correspondente a uma função de dados, para cada atributo único ou não,repetido e reconhecido pelo usuário, mantido na função de dados ou recuperado dessa função por meio da execução de todos os processos elementares pertinentes ao escopo da contagem.
22. (CESPE / CGE-PI - 2015) No processo de contagem da aplicação, um dos passos é determinar o tamanho funcional de cada função de dados, que pode ser classificada, em relação a sua complexidade, como simples, média ou complexa.
23. (CESPE / STJ - 2015) O custo para projetar, codificar e testar o software pode ser estimado por meio do uso de ponto de função em dados históricos de sistemas similares.
24. (CESPE / CGE-PI - 2015) Um processo elementar que tenha a intenção primária de apresentar informações ao usuário e que referencie uma função de dados para recuperar dados ou informações de controle pode ser uma saída externa ou uma consulta externa.
25. (CESPE / MEC - 2015) Os projetos de melhoria não podem envolver inclusões de funcionalidades.
26. (CESPE/TCDF-2OiZj) Na técnica de Nesma utilizada para calcular a estimativa do tamanho do software, realiza-se um detalhamento de cada elemento e de cada função, o que torna a técnica mais trabalhosa que outras.
27. (CESPE / ANTAQ - 2014) De acordo com a análise de pontos de função, o desenvolvimento de aplicações sem a preocupação de produzir código reusável não influencia na contagem do fator de ajuste.
28. (CESPE / TCDF - 2014) Arquivos de interface externa (AIE) e arquivo lógico interno (ALI) são as funções de dados utilizadas para a contagem de pontos de função.
29. (CESPE / TCDF - 2014) Na contagem de funções de transações, uma entrada externa
(EE) é um processo que trata ou processa informações ou dados externos à aplicação. Contudo, umaEE
não modifica os dados dos arquivos lógicos internos (ALIs).

30. (CESPE/SUFRAMA-2oi4) Em um projeto de melhoria, apenas as funções incluídas e alteradas devem ser contadas para se medir o tamanho funcional do projeto.
31. (CESPE / CNJ -2013) Entrada externa, arquivo referenciado e saída externa são funções do tipo transação.
32. (CESPE / MPOG - 2013) Na contagem por pontos de função, um arquivo de interface externa(AIE) sempre será um arquivo lógico interno (ALI) de outra aplicação.

33- (CESPE/CNJ-2013) O principal objetivo de um arquivo de interface externa (AIE) é armazenar dados referenciados por um ou mais processos elementares da aplicação que está sendo contada. Além disso, um AIE contado para uma aplicação deve ser um arquivo lógico interno para outra aplicação.
34. (CESPE / CNJ - 2013) Na contagem de um projeto de manutenção ou de melhoria, as funções de conversão de dados não devem ser contadas.
35. (CESPE / AL-ES - 2011 - Letra A) A análise de pontos de função é uma técnica de medição das funcionalidades oferecidas por um software do ponto de vista de seus usuários com a qual se busca medir o que o software é capaz de fazer, e não a forma como ele foi construído.
36. (CESPE / ANATEL - 2011) A análise de pontos de função de um programa produz estimativas de tamanho funcional de um produto de software embasada em cinco parâmetros-chave:entradas externas, saídas externas, consultas externas, arquivos lógicos internos e arquivos de interface externos. Os três primeiros parâmetros são funções transacionais, enquanto os dois últimos são funções de dados. As operações CRUD (create, read, update e delete) são consideradas pertencentes às entradas externas.
37. (CESPE / BRB - 2011) Se duas aplicações mantiverem o mesmo arquivo lógico interno, então esse arquivo será contado apenas na aplicação que detém o arquivo físico.
38. (CESPE / ECT - 2011) A técnica de análise de pontos de função tem como objetivos primários,entre outros, a medição da funcionalidade que o usuário solicita e recebe,
a medição do desempenho e a manutenção de software independentemente da tecnologia utilizada para sua implementação.
39. (CESPE / MEC - 2011) São funções do tipo transação: entradas externas, saídas externas e consultas externas. Uma das principais diferenças entre as saídas externas e as consultas externas é que as primeiras devem conter alguma fórmula matemática ou cálculo, enquanto as consultas externas representam uma recuperação simples de dados.
40. (CESPE / MEC - 2011) A NESMA — manual de contagem de pontos de função embasado noCPM — facilita a estimativa do tamanho do produto e tem como referência as funções de dados e transações, sem que haja detalhamento de cada elemento da função.
41. (CESPE / BRB - 2011) Uma consulta que possua contador incrementado é considerada uma saída externa.
42. (CESPE / TJ-ES - 2011) De acordo com o manual de contagem de pontos de função,
consulta externa é um processo elementar que envia dados ou informações de controle para fora da fronteira, sendo considerada componente funcional básico.
43- (CESPE / CET - 2011) Uma consulta externa disponibiliza informações para o usuário por meio de lógica de processamento, ou seja, não se limita apenas a recuperação de dados. Alógica de processamento deve conter pelo menos uma fórmula matemática ou cálculo, ou criar dados derivados.
44. (CESPE / STM - 2011) O conceito de projeto de melhoria do IFPUG envolve as manutenções evolutivas, corretivas e preventivas da aplicação.
45. (CESPE / STM - 2010) O padrão ISO/IEC 20926 considera a técnica até a determinação dos pontos de função não ajustados. As características gerais de sistema utilizadas para a determinação do fator de ajuste e dos pontos de função ajustado contêm requisitos tecnológicos e de qualidade.
46. (CESPE / STM - 2010) Na análise de ponto de funções, a contagem de pontos relativos aos arquivos lógicos internos que se referem a grupo de dados ou informações de controle logicamente relacionados, reconhecidos pelo usuário e mantidos dentro da fronteira da aplicação, é contabilizada como pontos não ajustados.
47. (CESPE / STM - 2010) A NESMA (Netherlands Software Metrics Users
Association) tem objetivos e ações bem próximos aos do IFPUG; ambos apresentam abordagens semelhantes para a aplicação da análise de pontos de função em projetos de melhoria de software e na fase inicial do desenvolvimento do produto de software.
48. (CESPE / MPU - 2010) Na análise por pontos de função (APF), as funções podem ser do tipo transação e do tipo dados. Nas funções do tipo transação, são manipulados os arquivos de interface externa (AIE) bem como os arquivos lógicos internos (ALI).
49. (CESPE / TRE-BA - 2009) A APF auxilia a compreender e agir sobre problemas típicos de gerenciamento de projetos, tais como baixos custos, atrasos no pagamento,insatisfação do usuário e produtividade de desenvolvedores, bem como sobre as dificuldades de medição do progresso do projeto.
50. (CESPE / TRE-BA - 2009) A APF visa estabelecer uma medida de tamanho do software, em pontos de função (PF), por meio da quantificação das funções implementadas sob o ponto de vista do desenvolvedor. A função de ajuste denominada cálculos complexos considera em que nível o processamento lógico ou matemático influencia o desenvolvimento da aplicação.
51. (CESPE / TRE-BA - 2009) Para se determinar o número de PF não ajustados, após identificar as funções de dados e transacionais, deve-se multiplicar, pela respectiva complexidade, o total de arquivos lógicos internos, arquivos de interface externa, entidades externas, saídas externas e consultas externas. De acordo com a complexidade, cada uma das funções de dados e transacionais contribui com determinado número de PF.
52. (CESPE/TCU -2009) Uma organização executa projetos de desenvolvimento de aplicativos de software embasados na arquitetura J2EE, com padrões de desenho,framework MVC,
interoperabilidade XML e bancos de dados relacionais. Além disso, ela adota um processo de desenvolvimento de software baseado no RUP/UML e realiza estimativas de projeto por meio de análise de pontos de função. Considere que seja necessário estimar o tamanho de um projeto de uma nova aplicação a ser desenvolvida na plataforma mencionada. Nessa situação, é correto afirmar que a adição de uma nova página HTML produzirá um aumento no número total de pontos de função não ajustados; que o atendimento a uma demanda por produção de componentes de código reusáveis, para uso em outro projeto de desenvolvimento de software na mesma organização, incrementará o fator de ajuste de medição (value adjustment factor)para esse projeto.

53. (CESPE / TRE-BA - 2009) A contagem não ajustada de pontos de função é a soma das contribuições de cada função identificada na aplicação que esteja sendo contada. Para se obter a contagem ajustada de pontos de função, a referida soma é multiplicada pelo valor do fator de ajuste.
54. (CESPE / TRE-BA - 2009) E m um projeto de desenvolvimento, uma contagem deve incluir a funcionalidade provida pela conversão de dados e relatórios associados com os requisitos de conversão de dados.
55. (CESPE /TRE-ES - 2009) Logo após o início das atividades técnicas de um projeto,
o gerente e a equipe de desenvolvimento devem estimaro trabalho a ser realizado, os recursos necessários,o tempo de duração e, por fim, o custo do projeto. Para se estimaro tamanho do software, deve-se seguir a métrica de pontos de função (PF), desde que esta seja compatível com a tecnologia empregada na implementação do sistema.
56. (CESPE / TRE-PR - 2009) O primeiro passo para a contagem das unções de dados consiste em identificar arquivos lógicos internos (ALIs) e arquivos de interface externa(AlEs). Cada uma dessas funções de dados deve ser classificada segundo sua complexidade funcional, que é definida com base em conceitos de registros lógicos e de itens de dados.
57. (CESPE / TRE-PR - 2009) Registros lógicos são subconjuntos de dados dentro de um
ALI/AIE
que foram reconhecidos pelo usuário. Caso o usuário não reconheça subconjuntos de dados em um ALI/AIE, este deve ser contado como um registro lógico.
58. (CESPE / TRE-PR - 2009) A contagem de pontos de função é efetuada com base na especificação do sistema e complementada por informações dos usuários e analistas, para medir o tamanho funcional de um sistema, independentemente de sua forma de implementação. Na análise de pontos de função, são contados os seguintes componentes:arquivos lógicos internos, arquivos de interface interna, entradas externas, consultas externas e saídas externas.
59-(CESPE/ UNIPAMPA-2009) A métrica pontos de função tem como final idade aferir o tamanho dos projetos de desenvolvimento e a manutenção de software.
60. (CESPE / TRE-GO - 2009) O método de análise de pontos de função descreve como calcular as dez características gerais de um sistema, as quais são usadas para produzir, juntamente com outras informações, a contagem de pontos de função ajustados.
61. (CESPE / ANAC - 2009) Os tipos de contagem de pontos por função podem ser de projetos de desenvolvimento, projetos de melhorias ou de aplicações, sendo a contagem de pontos por função por estimativa realizada nos estágios iniciais de contagem.
62. (CESPE / STF - 2008) Em um projeto de desenvolvimento de software que adota o modelo de processos e as disciplinas propostas pelo RUP, a contagem de pontos de função não-ajustados(unadjusted function points) produzirá resultados mais eficazes para o gerente de projetos durante a fase de elaboração do que durante a fase de transição.
63. (CESPE / TER-BA - 2008) Na APF, a precisão da estimativa melhora à medida que se obtém mais informações da análise e do projeto de sistemas. Assim, é possível estimar o tamanho do software continuamente ao longo do processo de desenvolvimento do projeto. No método backfiring, o número de pontos de função de uma aplicação é derivado a partir de seu tamanho físico, que é assumido linear entre os tamanhos funcional e físico.
64. (CESPE / MPE-AM - 2008) Uma entrada do usuário é definida como uma ação do usuário que resulta na geração de uma resposta imediata do software na forma de uma saída entregue ao usuário.
65. (CESPE / MPE-AM -2007) Um fator de complexidade permite dar um peso a cada característica do domínio da informação usada como parâmetro de entrada da análise.
66. (CESPE / MPE-AM - 2007) Valores de ajuste de complexidade são obtidos a partir da resposta a uma série de questões relativas ao contexto de desenvolvimento e utilização do software. Esses valores são usados conjuntamente com a contagem dos parâmetros característicos do domínio para calcular o número de pontos de função.
67. (CESPE / MPE-AM - 2007) A fórmula de cálculo de pontos de função exprime uma relação exponencial entre os parâmetros de entrada da análise e a quantidade de pontos de função calculados.
68. (CESPE / TST- 2007) A estimativa de características de projeto por pontos de função requer que as características do domínio de informação do software sejam categorizadas como de realização simples, média ou complexa, em função do grau de dificuldade de desenvolvimento em determinada organização.
69. (CESPE / PRODEST - 2006) Uma função pode ser definida como uma coleção de instruções que realizam uma tarefa. Em uma função, pode-se também ter declarações de parâmetros formais e de variáveis locais manipuladas pelas instruções. A métrica denominada pontos de função (function points) é igual ao número de funções em um programa. Essa métrica possibilita uma medição precisa da complexidade de um programa.
70. (CESPE / TSE - 2006) A estimativa do tamanho de um software pode ser usada para guiar a alocação de recursos em um projeto. A análise de pontos de função mede diretamente o tamanho de um software contando o número de linhas de código e não quantidades e complexidades de entradas e saídas observadas pelos usuários.
71. (CESPE / IGEPREV-PA-2005-A) A relação entre linhas de código fonte e os pontos de função de um software depende da linguagem de programação usada para implementar este software.
GABARITo

1. ERRADO 40. CORRETO

2. CORRETO 41. CORRETO

3- ERRADO 42. CORRETO

4- CORRETO 43- ERRADO

5- ERRADO 44. ERRADO

6. CORRETO 45- CORRETO

7- CORRETO 46. CORRETO

8. CORRETO 47- ERRADO

9- CORRETO 48. ERRADO

10. CORRETO 49- ERRADO

li. CORRETO 50. ERRADO

12. ERRADO 5i- ERRADO

13- CORRETO 52. ERRADO

14- CORRETO 53- CORRETO

x5- ERRADO 54- CORRETO

16. ERRADO 55- ERRADO

17- LETRA A 56. CORRETO

i8. LETRA D 57- CORRETO

19. ERRADO 58. ERRADO

20. ERRADO 59- CORRETO

21. ERRADO 60. ERRADO

22. ERRADO 61. CORRETO

23- CORRETO 62. CORRETO

24. CORRETO 63. CORRETO

25- ERRADO 64. ERRADO

26. ERRADO 65- CORRETO

27- CORRETO 66. CORRETO

28. CORRETO 67. ERRADO

29- ERRADO 68. ERRADO

30. ERRADO 69. ERRADO

31- ERRADO 70. ERRADO

32. CORRETO 7i- CORRETO

33- CORRETO

34- ERRADO

35- CORRETO

36. ERRADO

37- ERRADO

38. CORRETO

39- CORRETO

LISTA DE QUESTõES - FCC

í. (FCC / SEFAZ-AP - 2022) Considere a contagem de Pontos de Função (PF) para três Arquivos
Lógicos Internos (ALI), que possuem as seguintes especificações:

I. ^TDeiTR.

II. 7TDe 2TR.
IH.8TDe2TR.

Dado que complexidades funcionais baixas equivalem a 7 pontos, médias a 10 pontos e altas a15 pontos, a contribuição total em PF desses três ALIs é de:

a) 32.

b) 27.

c) 30.

d) 22.

e) 21.

2. (FCC / AL-AP- 2020) Para um cálculo hipotético de Ponto por Função - PF, considere as quantidades e correspondentes funções:
- 3 EE baixa complexidade

- 1 EE média complexidade

- 2 EE alta complexidade

- 3 ALI baixa complexidade

- 2 ALI média complexidade

- 4 AIE baixa complexidade

- 3 AIE alta complexidade

- 5 SE baixa complexidade

- 5 CE média complexidade

E os seguintes valores padrão:

- 3, para EE baixa

- 4, para EE média

- 6, para EE alta

- 7, para ALI baixa

- 10, para ALI média

- 5, para AIE baixa

- 10, para AIE alta

- 4, para SE baixa

- 4, para CE média

Sem considerar o fator de ajuste, o total de pontos Função de Dados e o total de pontos Função de Transação são, respectivamente,
a) 12 e 65.

b) 91 e 16.

c) 91 e 65.

d) 12 e 91.

e) 16 e 65.

3. (FCC/ TRF - 3a REGIÃO - 2019) Em uma contagem de pontos de função, um ALI -
Arquivo
Lógico Interno, com grau de complexidade média, contribui para a contagem com:

a) 50 pontos.

b) 20 pontos.

c) 10 pontos.

d) 07 pontos.

e) 15 pontos.

4. (FCC / TRF - 3a REGIÃO - 2019) Em Análise de Pontos de Função, uma Consulta
Externa - CE
constitui-se de dados extraídos de:

a) Arquivos Lógicos Externos (ALEs) para, após os cálculos necessários, efetuar a atualização dos Arquivos Lógicos Internos (ALIs).
b) Arquivos Lógicos Internos (ALIs), de Arquivos de Interface Externa (AlEs) e/ou de
Informações de Controle, após realizar cálculos e atualizar os arquivos que são enviados para fora da fronteira do sistema.
c) Arquivos Lógicos Externos (ALEs), de Arquivos de Interface Interna (AlIs) e de
Informações de
Controle, podendo realizar cálculos e manutenção nos arquivos que cruzam a fronteira para dentro do sistema.
d) Arquivos Lógicos Externos (ALEs), de Arquivos de Interface Externa (AlEs) e de
Informações de Controle, podendo realizar cálculos e manutenção nos arquivos que cruzam a fronteira para dentro do sistema.
e) Arquivos Lógicos Internos (ALIs), de Arquivos de Interface Externa (AlEs) e/ou de
Informações de Controle sem realizar cálculos ou manutenção nos arquivos que cruzam a fronteira do sistema e sem alterar seu comportamento.
5. (FCC /TRE-PB-2015) Análise de Pontos de Função - APF é uma técnica para medir o tamanho funcional de um software cujo processo de medição envolve diversas etapas, dentre elas,a medição das funções de dados, que envolvem as funcionalidades fornecidas pelo sistema ao usuário para atender a suas necessidades de armazenamento de dados. Dentre as funções de dados estão:
a) os Arquivos de Ponto de Controle - APC.

b) as Saídas Externas - SE.

c) as Entradas Externas - EE.

d) os Arquivos de Interface Externa - AIE.

e) as Consultas Externas - CE.

6. (FCC / MPE-MA - 2013) O primeiro passo do processo de contagem por análise de pontos de função é determinar o tipo de contagem. Contagem de pontos de função podem ser associadas a projetos ou aplicações e existem 3 tipos de contagem: Desenvolvimento, melhoria ou:
a) aplicação.

b) suporte.

c) pesquisa.

d) interoperabilidade.

e) testes.

7. (FCC / TST - 2012) O Gerente de Projetos de Software aplica os conhecimentos,
habilidades e ferramentas às atividades do projeto com o objetivo de garantirque o produto seja desenvolvido de acordo com os requisitos. A métrica de análise de Pontos de Função, de acordo com a normaISO/IEC 20968,

a) auxilia o Gerente de Projetos de Software a estimar o esforço necessário e custo para o desenvolvimento de sistemas com a abordagem da análise estruturada de sistemas.
b) possibilita ao Gerente de Projetos de Software medir o esforço e qualidade necessários para desenvolver softwares, desde que esteja usando a análise orientada a objetos e os diagramas daUML.

c) classifica a contagem das funções do tipo dado em Entradas Externas (EE), Consultas
Externas
(CE) e Saídas Externas (SE), representando requisitos que gerem o armazenamento de dados do usuário.
d) define que os Arquivos Lógicos Internos (ALI) e os Arquivos de Interface Externa
(AIE) são funções do tipo transição, os quais representam requisitos relacionados ao processamento.
e) auxilia o Gerente de Projetos de Software com técnicas para medir o esforço necessário para o desenvolvimento de um sistema, apoiando-o, também, no levantamento dos custos, análise de qualidade e análise de produtividade.
8. (FCC / MPE-AP - 2012) Dentre os métodos disponíveis na utilização de métricas de sistema está a analise de pontos de função (Function Point Analysis). Nesse método,
a) a função realizada pelos objetos do sistema, seus atributos e operações são catalogados,possibilitando medir a quantidade de classes e objetos que serão necessários para este sistema.

b) as funções utilizadas em linguagens de desenvolvimento tradicional, bem como os métodos e operações utilizados em arquiteturas orientadas a objeto são contados para a definição do tamanho funcional do sistema.
c) é atribuída uma pontuação para cada função ou método executado por uma determinada linguagem de programação. Este número é formulado com base em cálculos matemáticos e,posteriormente, é utilizado para fazer a classificação das métricas do sistema.

d) são analisados os pontos de execução de cada função dentro de um determinado sistema,são gerados registros de sistemas (logs) e, posteriormente, é gerada uma classificação em função dos valores obtidos dessa análise..
e) as funcionalidades do sistema são elencadas sem a necessidade de preocupação com a tecnologia que será utilizada para o desenvolvimento do sistema.
9. (FCC / TRE-SP - 2012) Sobre a análise de pontos por função, considere:

I. É um método de contagem padrão capaz de medir as funcionalidades de um sistema sobre o ponto de vista do desenvolvedor.
II. A contagem sem ajustes (UFPC - unadjusted function point count) reflete as funcionalidades contáveis específicas disponibilizadas pelo sistema ou aplicação para o usuário.
III. É uma ferramenta para ajudar usuários a determinar os benefícios de um pacote de aplicativos para sua empresa por meio de contagem das funcionalidades que especificamente atendem seus requerimentos.
Está correto o que consta em:

a) II, apenas.

b) I e II, apenas.

c) I e III, apenas.

d) II e III, apenas.

e) I, lie III.

10. (FCC / TRE-CE - 2012) Considere 3 AlEs simples, 5 EEs médias, 8 CEs complexas, 3 ALIs complexos e 7 SEs médias. O cálculo de PF bruto é:
a) 136.

b) 148.

C) 159-

d) 163.

e) 212.

n.(FCC / TRT-AM - 2011) Segundo a IFPUG em relação à métrica do software por análise por pontos de função, considere:
I. Análise por pontos de função executa a medição do software determinando a quantidade de funcionalidades que o software fornece ao usuário baseado principalmente na arquitetura lógica.
II. O objetivo da análise por pontos de função é medir as funcionalidades que o usuário requisita e recebe e, também, medir o desenvolvimento e manutenção do software com dependência na implementação utilizada pela empresa.
III. O processo de contagem dos pontos de função deve ser simples o suficiente para minimizar a sobrecarga do processo de medida e consistente dentre os vários projetos e organizações.
Está correto o que se afirma em:

a) I e II, apenas.

b) I e III, apenas.

c) II e III, apenas.

d) III, apenas.

e) I, lie III.

12. (FCC / INFRAERO - 2011) Analise a tabela utilizada no cálculo de Pontos de Função.

Tipo de Função

I
II
III

Complexidade Funcional
Simples Média Complexa
7 10 15

5 7 10

4 5 7

Preenchem correta e respectivamente os tipos de função I, II e III:

a) ALI, AIE e SE.

b) ALI, CEe AIE.

c) CE, EEeALI.

d) AIE, ALe EE.

e) EE, CEe SE.

13- (FCC / INFRAERO - 2011) A métrica análise por pontos de função foi desenvolvida na década de 1970, como uma forma de medir software. Analise os itens a seguir relacionados a essa métrica:
I. Considera mais importante o número de linhas de código do que as funcionalidades criadas.

II. Pode ser aplicada antes do código ser escrito, baseando-se na descrição arquitetural do projeto.
III. É dependente da tecnologia utilizada no desenvolvimento.

IV. Dois programas muito diferentes podem possuir a mesma contagem de pontos de função.

Está correto o que consta em:

a) I, II, III e IV.

b) II e IV, apenas.

c) I, II e IV, apenas.

d) I, II e III, apenas.

e) I e III, apenas.

14. (FCC /TRT-RS -2011) Após a aplicação do fator de ajuste, o total de pontos de função em uma contagem ficou em 110,60. Antes da aplicação do ajuste, os pontos de função brutos estavam em 140,00. Portanto, o somatório dos 14 itens do nível de influência global foi:
a) 11.

b) 14-

c) 15-

d) 18.

e) 19.

15. (FCC/TRT-PI-2oio) Considere, no âmbito da Análise de Pontos de Função:

(I) Um ALI é contado com base em uma avaliação do número de campos de dados não recursivos do usuário e do número de tipos de elementos de registros lógicos nele contidos.
(II) Um AIE é uma entidade lógica e persistente, que é requerida para referência ou validação pelo software sendo contado, mas que é mantido por outro aplicativo de software.
(III) Uma entrada externa é contada com base no número de campos de dados do usuário envolvidos e na soma dos ALI, mas não dos AIE participantes do processo.
Está correto o que se afirma em:

a) I, apenas.

b) II, apenas.

c) III, apenas.

d) I e II, apenas.

e) I, lie III.

i6.(FCC / TRFzj - 2010) Sobre a métrica análise por pontos de função, é correto afirmar:

a) Não pode ser aplicada para estimar esforço de manutenção em sistemas já em funcionamento.
b) A medida não pode ser aplicada com base na descrição arquitetural do projeto, mas sim no código desenvolvido.
c) É dependente da tecnologia utilizada no desenvolvimento.

d) A contagem de pontos de função pode ser aplicada logo após a definição da arquitetura,permitindo estimar o esforço e o cronograma de implementação de um projeto.

e) Para determinar o número de pontos de função, deve-se desconsiderar a contagem de dados e de transações.
17. (FCC/TRT-PR-2Oio) Na análise de pontos de função, são apenas do tipo Transação as funções:

a) ALIeSE.

b) ALIeAIE.

c) ALI, AlEeSE.

d) CE, EEeSE.

e) CE, EE, SEeAIE.

18. (FCC / TCM-PA - 2010) É um processo lógico do negócio que mantém os dados recebidos de fora da fronteira da aplicação em um ou mais arquivos lógicos internos ou, ainda, é um processo de controle que direciona o software para atender os requisitos de negócio do usuário. No âmbito da Análise de Pontos de Função, tal é a definição de:
a) SE.

b) AIE.

c) EE.

d) ALI.

e) CE.

ig.(FCC / TCM-PA - 2009) Quanto aos pontos brutos, na Análise de Pontos de Função o fator de ajuste aplicado pode aumentá-los:
a) em até 35% ou diminuí-los em até 65%.

b) ou diminuí-los em até 35%.

c) ou diminuí-los em até 65%.

d) ou diminuí-los em até 1,35%.

e) em até 65% ou diminuí-los em até 35%.

GABARITo

1. LETRA E

2. LETRA C

3. LETRA C

4. LETRA E

5. LETRA D

6. LETRA A

7. LETRA E

8. LETRA E

9. LETRA D

10. LETRA D

11. LETRA B

12. LETRA A

13. LETRA B

14. LETRA B

15. LETRA D

16. LETRA D

17. LETRA D

18. LETRA C

19. LETRA B

LISTA DE QUESTõES - FC V

í. (FGV/ IMBEL-2021) A análise de ponto de função é uma técnica comumente utilizada para:

a) avaliar a produtividade de programadores desenvolvedores.

b) estabelecer configurações de hardware para sistemas em produção.

c) medir o tamanho de projetos de desenvolvimento de software.

d) medir a produtividade de equipes de desenvolvimento de software.

e) medir os tempos de resposta de sistemas instalados e operacionais.

2. (FGV / DPE-RJ - 2019) Determinado órgão governamental está utilizando a técnica de Análise de Pontos de Função (APF) para efetuar a contagem de suas aplicações e gerar uma base histórica própria.
Sendo assim, para a contagem de um sistema que atende a atividade-fim desse órgão,
será necessário:
a) acessar o código-fonte para contar as funções desenvolvidas ou incorporadas ao sistema;

b) explorar o modelo físico (esquema físico) do banco de dados para quantificar as funções de dados;
c) quantificar as funcionalidades implementadas, considerando a visão do usuário;

d) detalhar e medir os requisitos não funcionais solicitados pelo usuário;

e) medir as funções das transações executadas e gerenciadas pelo banco de dados.

3. (FGV / DPE-RJ - 2019) Determinado órgão governamental está utilizando a técnica de Análise de Pontos de Função (APF) para efetuar a contagem de suas aplicações e gerar uma base histórica própria. Sendo assim, para a contagem de um sistema que atende a atividade-fim desse órgão, será necessário:
a) acessar o código-fonte para contar as funções desenvolvidas ou incorporadas ao sistema;

b) explorar o modelo físico (esquema físico) do banco de dados para quantificar as funções de dados;
c) quantificar as funcionalidades implementadas, considerando a visão do usuário;

d) detalhar e medir os requisitos não funcionais solicitados pelo usuário;

e) medir as funções das transações executadas e gerenciadas pelo banco de dados.

4. (FGV / MPE-AL- 2018) Carlos é o responsável técnico pelo Sistema de Informação
Financeiro
(SISFIN) de sua corporação. O SISFIN passou por um processo de melhorias que corrigiu erros em duas funcionalidades, incluiu três novas funcionalidades e excluiu uma funcionalidade.Com o intuito de atualizar 0 tamanho funcional do SISFIN, ao término das alterações, as funções doSISFIN serão contadas utilizando a técnica de Análise de Ponto de Função (APF). Sendo assim,

é correto afirmar que o tamanho funcional do SISFIN foi alterado por causa da contagem dos pontos de função da(s):
a) seis funcionalidades.

b) três novas funcionalidades.

c) três funcionalidades novas e da excluída.

d) funcionalidade excluída.

e) duas correções e da funcionalidade excluída.

5. (FGV / Banestes- 2018) Em termos de Análise de Pontos de Função
(APF), analise as afirmativas a seguir.
I. É capaz de medir projetos de desenvolvimento e manutenção de software, com a restrição de ser dependente da tecnologia de implementação.
II. A técnica de derivar o número de pontos de função a partir da quantidade de linhas de código do programa é baseada num fator de conversão que independe da linguagem de programação usada.
III. Visa medir a funcionalidade de um software do ponto de vista de seus usuários.
Essa medição ocorre antes mesmo do desenvolvimento do software, de forma a estimar o seu tamanho e o seu custo.
Está correto somente o que se afirma em:

a) I;

b) II;

C) III;

d) I e II;

e) lie III.

6. (FGV / COMPESA - 2018) O levantamento da complexidade das oito funções de um sistema a ser desenvolvido, seguindo a técnica de Contagem de Pontos de Função,resultou nos elementos listados na tabela a seguir.
Nome da Função

ALI-1
ALI-2
EE-1
EE-2
EE-3
CE-1
SE-1
SE-2

Tipo da Função
Arquivo Lógico Interno
Arquivo Lógico Interno

Entrada Externa
Entrada Externa
Entrada Externa
Consulta Externa
Saída Externa
Saída Externa

Complexidade
Baixa
Média
Baixa
Média

Alta
Média
Baixa
Alta

Assinale a opção que corresponde ao total de pontos de função não ajustados computado para o conjunto das funções listadas na tabela:
a) 42

b) 43

c) 44

d) 45

e) 46

7. (FGV / COMPESA - 2018) O levantamento da complexidade das oito funções de um sistema a ser desenvolvido, seguindo a técnica de Contagem de Pontos de Função,resultou nos elementos listados na tabela a seguir.
Nome da Função
ALI-1

AU-2
lEE-1
EE-2
EE-3
CE-1
SE-1
SE-2

Tipo da Função
Arquivo Lógico Interno
Arquivo Lógico Interno

Entrada Externa

Entrada Externa
Entrada Externa
Consulta Externa
Saída Externa
Saída Externa

Complexidade
Baixa
Média
Baixa
Média
Alta
Média
Baixa
Alta

Assinale a opção que corresponde ao total de pontos de função não ajustados computado para o conjunto das funções listadas na tabela.
a) 42

b) 43

c) 44

d) 45

e) 46

8. (FGV / IBGE -2017) A Análise de Pontos de Função (APF) é um método de medição de tamanho funcional de um software. Nesse método são contadas as funções de dados e funções de transação. Após essas contagens são aplicados fatores de ajuste. A opção que apresenta fatores de ajuste desse método é:
a) Volume de transações, entrada de dados online e presença de stakeholders negativos;

b) Walkthrough, Processamento distribuído e Performance;

c) Facilidade de Mudanças, Prototipação e Comunicação de dados;

d) Atualização online, interface com usuário e Múltiplos locais;

e) Facilidade de Implantação, Facilidade operacional e Facilidade de obsolescência.

g. (FGV / Prefeitura de Paulínia - SP - 2016) Ponto de Função é uma métrica orientada à função utilizada para medir o tamanho funcional do software. Na contagem de Pontos de Função,a função de transação que não altera o comportamento do sistema, embora possa conter validações, é denominada:
a) entrada externa.

b) consulta externa.

c) saída externa.

d) arquivo lógico interno.

e) arquivo de interface externa.

10.(FGV / IBGE - 2016) O requisito Obter Histórico de Compras do sistema A consiste em uma referência a um grupo de dados "X" logicamente relacionado, mantido e armazenado no sistema B, conforme representado no diagrama a seguir.
Obter
Histórico de Compras
Sistema B

Manter
Grupo de dados "X"
Usuário Sistema B

Na visão do usuário do sistema A, o grupo de dados "X" é visto na técnica de
Análise por Pontos de Função como:
a) ALI - Arquivo Lógico Interno;

b) AIE - Arquivo de Interface Externa;

c) EE - Entrada Externa;

d) SE - Saída Externa;

e) CE - Consulta Externa.

11. (FGV / PGE-RO - 2015) Roger e sua equipe de métricas de software foram designados para estimar o custo e o tempo necessário para desenvolver um sistema de informação. Apartir dos requisitos levantados desse sistema, a equipe de Roger contou o número de:
Arquivos Lógicos Internos (ALIs); Arquivos de Interface Externa (AlEs); Entradas Externas
(EEs);
Consultas Externas (CEs); e Saídas Externas (SEs). Com base nessas contagens, Roger e sua equipe podem fazer as estimativas de software aplicando o método:
a) Linhas de código;

b) Pontos por Casos de Uso;

c) Pontos de Função;

d) Complexidade Estrutural;

e) Ponderado por Classe.,

12. (FGV / TJ-PI - 2015) Vários entes governamentais brasileiros têm utilizado a métrica de Pontos de Função (PF) nas estimativas e dimensionamento de tamanho funcional de projetos de software devido aos diversos benefícios de utilização da métrica e às recomendações dos órgãos de controle do governo brasileiro. Sobre a métrica de Pontos de Função, é correto afirmar que e:
a) baseada no projeto físico da aplicação;

b) usada para quantificaras linhas de código contidas na aplicação;

c) composta de Arquivos Lógicos Externos (ALEs), Arquivos de Interface Interna (AlIs),
Entradas
Externas (EEs), Consultas Internas (CIs) e Saídas Externas (SEs);

d) independente da solução tecnológica utilizada na aplicação;

e) um indicador da produtividade da equipe de desenvolvimento de uma aplicação.

13. (FGV / PROCEMPA - 2014) A técnica de contagem de pontos de função define algumas abstrações necessárias à determinação do tamanho funcional de um projeto de software.Relacione cada um dos elementos da contagem de pontos de função, listadas a seguir,
às suas respectivas características.
1. Consulta Externa

2. Arquivo de Interface Externa

3. Arquivo Lógico Interno

4. Entrada Externa

5. Saída Externa

() Tabelas de banco de dados lidas pela aplicação, mas atualizadas por outra aplicação.
() Tabelas de banco de dados atualizadas pela aplicação.

() Transação que processa dados ou informações de controle originados de fora da fronteira da aplicação.
() Função que apresenta informações ao usuário por meio da lógica de processamento que não seja apenas uma simples recuperação de dados ou informação de controle.
() Função que apresenta informações ao usuário, por meio da simples recuperação de dados ou informações de controle, dentro da fronteira da aplicação.
Assinale a opção que indica a sequência correta, de cima para baixo.
a) 3-2-5-i-4

b) 2-3-4-5-1

c) 3-2-4-i-5

d) 2-3-5-4-i e)3-2-i-5-4
i4.(FGV / INEA-RJ - 2013) A análise preliminar de um sistema a ser desenvolvido possui as seguintes características:
* doze entradas externas sendo três simples, quatro médias e cinco complexas.

* seis saídas externas sendo duas simples e quatro médias.

Infelizmente, não foi possível determinar o número de Arquivos Lógicos Internos
(ALI) do sistema, mas sabe-se que todos são do tipo simples. O desenvolvedor sabe que, por contrato, o sistema deve possuir um total de pontos de função igual a 118. O número de ALIs simples que o sistema deve conter, de forma a atingir, exatamente, o total de pontos contratuais,deverá ser igual a Dados: Tabela de pesos para cálculo de pontos de função.
Elemento
Entrada
Saída
Arquivo

Simples

Médio

Complexo a) 3.
b) zp.

c) 5-

d) 6.

e) 7-

15. (FGV / Senado Federal - 2012) Com relação ao tema de análise por pontos de função, avalie as afirmativas a seguir.
I. O termo Arquivo Lógico Interno designa um grupo de dados ou informações de controle,logicamente relacionados, reconhecido pelo usuário e mantido dentro da fronteira da aplicação.

II. O termo Saída Externa designa um processo elementar que processa dados ou informações de controle enviados de fora da fronteira da aplicação.
III. O termo Entrada Externa designa um processo elementar que envia dados ou informações de controle para fora da fronteira e que executa um processamento adicional baseado nestes dados ou controles.
Assinale:

a) se somente a alternativa I estiver correta.

b) se somente a alternativa II estiver correta.

c) se somente a alternativa III estiver correta.

d) se somente as alternativas I e II estiverem corretas.

e) se nenhuma alternativa estiver correta.

16. (FGV / MPM-MS - 2012) A NESMA - Netherlands Software Metrics Association
(Associação de
Métricas de Software da Holanda) - é uma organização similar ao IFPUG, que mantém seu próprio Manual de Práticas de Contagens. A diferença entre as regras mantidas pelaNESMA e as mantidas pelo IFPUG é que a NESMA reconhece três tipos de contagem de pontos de função.Assinale a alternativa que os indica.

a) Aplicativa, Metodológica e Aprimorada.

b) Detalhada, Estimativa e Indicada.

c) Real, Precisa e Resumida.

d) Complexa, Definida e Invertida.

e) Simplificada, Ajustada e Completa.

17. (FGV / DETRAN-RN - 2010) A equipe de métricas de software do TJPI realizou uma estimativa do tamanho da aplicação de processo eletrônico chamada SisProcessos. Utilizando a técnica deAnálise por Pontos de Função (APF), a equipe chegou ao valor de 100 pontos de função não ajustados. A equipe também levantou o valor de influência de cada uma das 14características gerais dos sistemas definidas pela técnica de APF, conforme listado a seguir:
COMUNICAÇÃO DE DADOS: 2
PROCESSAMENTO DISTRIBUÍDO: o
PERFORMANCE: 5

UTILIZAÇÃO DO EQUIPAMENTO: o
VOLUME DE TRANSAÇÕES: 5
ENTRADA DE DADOS "ON-LINE": 3
EFICIÊNCIA DO USUÁRIO FINAL: 3
ATUALIZAÇÃO "ON-LINE": 3

PROCESSAMENTO COMPLEXO: 1
REUTILIZAÇÃO DE CÓDIGO: 3
FACILIDADES DE IMPLANTAÇÃO: o
FACILIDADE OPERACIONAL: 3
MÚLTIPLOS LOCAIS: o
FACILIDADES DE MUDANÇAS: 3

A partirdessas informações, a equipe precisa finalizara contagem através do cálculo dos pontos de função ajustados, cujo valor é expresso corretamente em:
a) 94;

b) 96;

c) 98;

d) 1OO;

e) 102.

i8.(FGV / FIOCRUZ - 2010) Pontos por função - PF são derivados usando uma relação empírica baseada em medidas de contagem direta do domínio de informação do software e avaliação de complexidade do software. Um valor de domínio de informação é definido como uma entrada on-line, que resulta na geração de alguma resposta imediata do software, sob a forma de uma saída on-line. Esse valor de domínio de informação PE é denominado:
a) número de entradas externas (Externai Inputs - Eis).

b) número de saídas externas (Externai Outputs - EOs).

c) número de consultas externas (Externai Inquires - EQs).

d) número de arquivos lógicos internos (Internai Logical Files - ILFs).

e) número de arquivos de interface externa (Externai Interface Files - EIFs).

ig.(FGV / FIOCRUZ - 2010) A métrica "Pontos de Função" (Function Point, FP)
é usada efetivamente como meio para medir a funcionalidade entregue por um sistema. Considerando dados históricos, analise as afirmativas associadas ao uso da FP.
I. Estimar o custo ou esforço necessário para projetar, codificar e testar o software.

II. Prever o número de erros que vão ser encontrados durante o teste.

III. Prever o número de componentes e/ou o número de linhas de código projetadas no sistema implementado.
Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente a afirmativa II estiver correta.

c) se somente a afirmativa III estiver correta.

d) se somente as afirmativas I e II estiverem corretas.

e) se todas as afirmativas estiverem corretas.

20.(FGV / BADESC - 2010) Acerca das características e conceitos da técnica de Análise de Pontos de Função (APF), avalie as afirmativas a seguir.
I. Um relatório com a totalização de dados é um exemplo de saída externa.

II. Um dos objetivos da APFé medir as funcional idades do sistema, requisitadas e recebidas pelo usuário.
III. O termo "Arquivo", sob a ótica da APF, refere-se a um grupo de dados logicamente relacionados e reconhecido pelo usuário.
Assinale:

a) se somente a afirmativa I estiver correta.

b) se somente as afirmativas I e II estiverem corretas.

c) se somente as afirmativas I e III estiverem corretas.

d) se somente as afirmativas II e III estiverem corretas.

e) se todas as afirmativas estiverem corretas.

21. (FGV / MEC - 2009) Num sistema de controle acadêmico, uma tela permite visualizar um relatório com três tipos diferentes de ordenação. O rodapé do relatório sempre traz o total de registros listados. Do ponto de vista da Análise de Pontos de Função, a totalização de registros listados pode ser contada como:
a) uma saída externa.

b) três saídas externas.

c) uma consulta externa.

d) um parâmetro externo.

e) três consultas externas.

22. (FGV/Senado Federal -2008) Considere as assertivas sobre a técnica de pontos de função para a estimativa de custo de desenvolvimento de um software:
I. A medida de pontos de função é independente da linguagem de implementação do software.

II. Os pontos de função são mais apropriados para medir os sistemas de processamento de dados dominados por operações de entrada e saída.
III. Existem grandes variações na contagem de pontos de função, dependendo do julgamento de quem fez a estimativa.
As assertivas corretas são:

a) somente II e III.

b) somente I e II.

c) somente I e III.

d) I, lie III.

e) somente I.

GABARITo

1. LETRAC 9- LETRA B
17- LETRA B

2. LETRA C 10. LETRA B
18. LETRA C

3- LETRAC íi. LETRAC
19. LETRA E

4- LETRAC 12. LETRA D
20. LETRA E

5- LETRA C 13- LETRA B
21. LETRA A

6. LETRA D 14- LETRA C
22. LETRA D

7- LETRA D 15- LETRA A

8. LETRA D 16. LETRA B

LISTA DE QUESTõES - DIvERSAS BANCAS

As questões 11 e 12 baseiam-se nas Figura io(a), io(b) e io(c). Sobre a Figura io(a), considere os seguintes aspectos:
(1) ela mostra uma tabela na qual constam, intencionalmente, os requisitos de software de um novo projeto de desenvolvimento de software, que serão completamente levantados e analisados apenas nos dois primeiros meses de trabalho;
(2) no primeiro mês, serão levantados e analisados os requisitos "Manter
Aluno", "Manter
Professor", "Manter Curso" e "Manter Disciplina";

(3) cada um dos "Manter", do primeiro mês, é composto unicamente pelas funcionalidades incluir,consultar, atualizar e excluir (CRUD). Por exemplo, "Manter Aluno" é composto,
apenas, pelos processos elementares "Incluir Aluno", "Consultar Aluno", "Atualizar Aluno" e "Excluir Aluno".
A Figura io(b) exibe uma visão geral do "Processo Unificado Rational" (RUP), no qual se inseriu, em alguns lugares, retângulos para ocultar qualquer texto existente nesses locais. A Figura io(c) mostra uma tabela utilizada para determinação da contribuição de Pontos de Função (PF) em contagens estimadas, segundo a NESMA (NESMA Early FPA Counting), na qual serão consideradas,apenas,
as "Entradas Externas" (EE), "Consultas Externas" (CE) e "Saídas Externas" (SE).

Requisitos de software a serem
Levantados e Analisados lô Mês(Módulo 1)

Manter Aluno
Manter Professor
Manter Curso
Manter Disciplina

22 Mês

(Módulo 2)
Manter Nota
Manter Frequência

Manter coordenador
Revisar lançamentos

Figura 10(a) - Requisitos de software

Figura 10(b) - Visão geral do RUP

Tipo de
Função

EE
SE
CE

Média de PF
4,3

5,4

3,8

Complexidade

Alta Média Baixa
6 4 3

7 5 4

6 4 3

Figura 10(c) - Tabela para determinação da contribuição de PF
í. (FUNDATEC / ISS-Porto Alegre - 2022) Sabe-se que em todos os processos elementares de"CONSULTA", dos "CRUD's" do primeiro mês, haverá contabilização, devendo ser apresentado,
no rodapé de cada página do relatório gerado, o número da página atual e o seu total, por exemplo, 1/5 (página 1 de 5). Nesse caso, considerando apenas as funções do tipo transação, a contagem estimada de Pontos de Função, do Módulo 1, segundo a NESMA, será um número:
a) Menor ou igual a 40.

b) Maior que 40 e menor ou igual a 50.

c) Maior que 50 e menor ou igual a 60.

d) Maior que 60 e menor ou igual a 70.

e) Maior que 70.

2. (CEPUERJ / UERJ - 2021) Observe as seguintes descrições de funcionalidades que compõem um sistema de controle de ponto:
Rrghtro d» Ponta

Pnnopd intençk* Jtualoar o irqunro jponteanrnto
Dtdo» d> teta Ciheçilho «xoi mv e kgettpu dâ «nprtM.

rooundo (tivU Enter ou botto OKi ptrao rnuáno, mdtoedor de cntrud» ou laiilaAjqum» KtMftdoi apontamento

Infcrxta em <um luUxfxXiv*

iVmnpal mterçÀo «huluar at anquivcn apontamento r justifcati*a
Dtdoi da teta CiheçaOto cIxn nome e da emprtx.

coüundo | tecta Frter ou botto OK), mrrajprTT. pjrs <1

tmtario. hora dr entrada e fiBhíxibvi

Arquivia a ipcrtammto e fuBttôratnr*.

Consulta Apontamento Diirio

Pnnipil sfwenMr dados do arquivo apontamento
Dados da teta Cabeçalho cntn nome e logotipo da empresa.

<ixnando (teria Eraer ou Nxio OK t mrnwgm para o usuário, date, horário de entrada, horáno de uüdaAnptfvoa amatdoa apontamento

Emitir Relatório de Presença

PrtndpaJ mtençAo apresentar dados do» arqurn» apontamento,
pMtxfaatrra e pevoa, n» totehiaçto

LAadin da teia Cabeçalho com nome e bogptopo da eospma.
i cenando itota Enter ou hrtto OK|. mmMgrm para o utuAno, date nctel, date finai, matricula,
nociw, total de hora* do trabalhador, numm> dr pstrikativM
Arquivos acmidna peaaoa. apontamento e pauta ativa

Considerando as complexidades e contribuições para funções de transação apresentadas noManual de Práticas de Pontos de Função do IFPUG , versão 4.3.1
desconsiderando qualquer funcionalidade não citada como, por exemplo, o login no sistema ou alteração dos registros , o número de transações do tipo entrada externa (EE), consulta externa (CE) e saída externa (SE), além do somatório de pontos de função (PF) de todas as funções do tipo transação é expresso corretamente em:
a) 2 entradas externas, 1 consulta externa, 1 saída externa, 15 PFs b) 2 entradas externas, 1 consulta externa, 1 saída externa, 14 PFs c) 2 entradas externas, 2 consultas externas, 15 PFs d) 2 entradas externas, 2 consultas externas, 14 PFs
3. (AOCP / Prefeitura de Novo Hamburgo - RS - 2020) Como se denomina um modelo de projeto preliminar usado para a estimativa de esforço inicial de um software e baseada nos seus requisitos?
a) Número de pontos de função.

b) Número de linhas de código.

c) Número de linhas de reúso.

d) Número de tabelas do sistema.

e) Número de pontos de aplicação.

4. (AOCP / Prefeitura de Betim - MG - 2020) Considerando a métrica de pontos por função, os dados derivados da aplicação que fornecem informações para o usuário são classificados como:
a) entradas externas.

b) fator de ajuste.

c) arquivos lógicos internos.

d) arquivos de interface externos.

e) saídas internas.

5. (IBFC / TRE-PA - 2020) Conforme a IFPUG (International Function Point Users
Group), no
Manual de Práticas de Contagem de Pontos de Função, o primeiro passo para se fazer o cálculo do Valor do Fator de Ajuste (VAF) é o de avaliar cada uma das:
a) 14 características gerais do sistema na escala de o a 5 para determinar o nível de influência(NI)

b) 10 características gerais do sistema na escala de o a 3 para determinar o nível de influência
(NI)

c) 7 características gerais do sistema na escala de 1 a 3 para determinar o nível de influência
(NI)

d) 5 características gerais do sistema na escala de 0 a 5 para determinar o nível de influência
(NI)

6. (VUNESP / EBSERH - 2020) A métrica de software baseada em pontos de função:

a) possui 12 fatores de ajuste de valor.

b) independe do número de entradas externas do programa.

c) depende do número de usuários simultâneos do programa.

d) considera o número de desvios incondicionais existentes.

e) leva em conta o número de arquivos lógicos internos.

7. (VUNESP / Câmara de Piracicaba - SP - 2019) Uma das principais métricas utilizadas para avaliação de software é a Métrica por Pontos de Função. Tal tipo de métrica considera alguns valores denominados de domínio da informação, dentre os quais se inclui o número de:
a) chamadas de função.

b) desvios incondicionais c) entradas externas.
d) estruturas complexas.

e) variáveis internas.

8. (Avança SP / Câmara Municipal de Taboão da Serra - SP - 2019) No que se refere à análise de pontos por função, analise os itens a seguir e, ao final, assinale a alternativa correta:
I - Pontua a complexidade do código desenvolvido em Java.

II - Analisa arquivos, arquivos de interface externa, entradas do usuário, saídas do usuário e consultas do usuário.
III - É um método para elicitação de requisitos.

a) Apenas o item I é verdadeiro.

b) Apenas o item II é verdadeiro.

c) Apenas o item III é verdadeiro.

d) Apenas os itens I e III são verdadeiros.

e) Todos os itens são verdadeiros.

9. (ACEP / Prefeitura de Aracati - CE - 2019) Uma das atribuições mais comuns na
Gerência de
Projetos de software é realizar estimativa de software. Sobre essas estimativas, é correto afirmar que:
a) a estimativa baseada em Pontos de Função são dependentes da estrutura tecnológica para a qual se pretende desenvolver software.
b) através da Análise de Pontos de Função, um gerente de projetos é capaz de realizar estimativa de software mesmo sem experiência na área.
c) métricas de dimensão de sistema, como o LOC, e de produtividade são dependentes da linguagem de programação empregada.
d) o COCOMO 2 é um modelo em dois níveis: Nível Pós-Arquitetura e Nível
Inicial de
Prototipação.

10. (CESGRANRIO / TRANSPETRO - 2018) Um pequeno sistema passou por um processo de contagem de pontos de função, resultando na Tabela abaixo.
Entrada Externa
Saída Externa
Consulta Externa

Arquivo de Interface Externa
Arquivo Lógico Interno

Baixa

Média

Alta

Quantos pontos de função não ajustados tem tal sistema?

a) 103

b) 106

c) 120

d) 121

e) 122

11. (IBFC / EBSERH - 2018) Na análise de pontos de função, as funções transacionais representam as funcionalidades efetivamente fornecidas para o usuário e são categorizadas em entradas externas, saídas externas e consultas externas.
12. (IBFC / EMBASA - 2017) A NESMA reconhece três métodos de Análise de Pontos de
Função
(APF), que são métodos de Medição de Tamanho Funcional (FSM) autossuficientes. Esse três métodos são respectivamente:
a) APF Detalhada, APF de Alto Nível (ou APF Estimada) e APF Indicativa b) APF Generalista, APF de Baixo Nível (ou APF Arcaica) e APF Indicativa c) APF Generalista, APF de Alto Nível (ou APF Estimada) e APF Específica d) APF Detalhada, APF de Baixo Nível (ou APF Arcaica) e APF Específica.
13. (IBFC / EBSERH - 2017) O primeiro passo a ser seguido para a contagem de PF
(Pontos de
Função) de um projeto de software é determinar o tipo de contagem. Neste passo é estabelecido o tipo de contagem que será usado para medir o projeto de software,tanto no processo como no produto. Assinale a alternativa que apresenta três tipos de contagem possíveis:
a) do projeto de integração, do projeto de melhoria (manutenção), de depuração (testes)

b) do projeto de desenvolvimento, do projeto de requerimentos (requisitos), da aplicação(produção)

c) do projeto de desenvolvimento, do projeto de melhoria (manutenção), da aplicação(produção)

d) do projeto de integração, do projeto de requerimentos (requisitos), de depuração (testes)

e) do projeto de desenvolvimento, do projeto de requerimentos (requisitos), de depuração(testes).

14. (IBFC / EBSERH -2017) Um dos passos básicos na contagem de pontos de função inclui contar os tipos de funções de dados identificados pelas siglas ALI e AIEque representam respectivamente:
a) Árvore da Logística Interna - Árvore de Integração Externa b) Arquivo Lógico Interno - Arquivo de Interface Externa c) Arquitetura Lógica Interna - Arquitetura Integrada Externa d) Artefatos Lógicos Internos - Artefatos de Integração Externa e) Acervo de Livros Internos - Acervo de Interfaces Externas.
15- (IBFC / EBSERH - 2017) O conceito de Ponto de Função foi definido originalmente em 1977 naIBM e é padronizada internacionalmente pela ISO. Pode-se definir o conceito de Ponto deFunção como sendo:

a) uma unidade de medida de software para estimar o tamanho de um sistema de informação baseando-se na funcionalidade percebida pelo usuário do sistema, independentemente da tecnologia usada para implementá-lo.
b) uma medida de tamanho de software que estima o esforço (número de pessoas-hora) e o prazo associados ao desenvolvimento dos programas e sistemas por meio da quantidade de linhas de código-fonte (SLOC - Source Lines Of Code).
c) a medição do software por meio de uma indicação quantitativa da extensão,
quantidade,
dimensão, capacidade ou tamanho dos programas e sistemas através da velocidade de execução em um computador padrão.
d) é uma métrica ou um indicador, ou a combinação dos dois, que fornece compreensão do processo de software, de um sistema de informação basicamente utilizando medidas diretas tais como a complexidade ciclomática de um programa ou sistema.
e) é uma medida de software, que possibilita um conjunto de métricas de qualidade e produtividade, fortemente ligado à linguagem de programação utilizada,impossibilitando a utilização de dados históricos para projetos que não utilizam a mesma linguagem.
Comentários:

(a) Correto, é realmente uma unidade de medida para estimarotamanho de um sistema baseando-se na funcionalidade percebida pelo usuário do sistema, independente da tecnologia; (b)
Errado,
ela não mede o esforço diretamente (apenas indiretamente) e definitivamente não utiliza a quantidade de linhas de código; (c) Errado, não há nenhuma relação com a velocidade de execução em um computador; (d) Errado, ela não oferece compreensão do processo de software e não utiliza complexidade ciclomática; (e) Errado, não é ligado à linguagem de programação ou outras tecnologias e possibilita -sim -utilização de dados históricos.
Gabarito:

16.(IBFC / EBSERH - 2016) Um dos passos básicos na contagem de pontos de função inclui contar os tipos de funções de dados identificados pelas siglas ALI e AIEque representam respectivamente:
a) Árvore da Logística Interna - Árvore de Integração Externa b) Arquivo Lógico Interno - Arquivo de Interface Externa c) Arquitetura Lógica Interna - Arquitetura Integrada Externa d) Artefatos Logicos Internos - Artefatos de Integração Externa e) Acervo de Livros Internos - Acervo de Interfaces Externas.
17. (ESAF / ANAC - 2016) Segundo a versão 2.0 do Roteiro de Métricas de Software do
SISP, o grupo de dados, logicamente relacionados, reconhecido pelo usuário, mantido por meio de um processo elementar da aplicação que está sendo contada, é o:
a) Arquivo de Interface Externa.

b) Arquivo Lógico Externo.

c) Arquivo Lógico Interno.

d) Arquivo de Interface Interno.

e) Arquivo de Interface Lógica.

18. (IBFC / EBSERH -2015) De acordo com as Métricas de Software, a Análise de Pontos de Função é uma técnica de medição das funcionalidade fornecida por um software sob o ponto de vista:
a) do Gerente do Projeto.

b) dos Usuários.

c) do Programador.

d) do Analista de Sistema.

e) do Engenheiro de Software.

ig.(IDECAN / PRODEB-2015) A APF (Análise de Pontos de Função) pode serdefinida como sendo uma técnica para medir as funcionalidades fornecidas por um determinado software, do ponto de vista do usuário. O ponto de função é a unidade de medida desta técnica, e o objetivo principal é tornar a medição independente da tecnologia que se utiliza para construir o software.Em resumo, a APF busca medir o que realmente o software faz e não da forma que ele foi construído. Uma dessas funções é a do tipo dado que representa a funcionalidade que está sendo fornecida pela aplicação, ou seja, representa os seus arquivos de armazenamento de dados. São classificados nas seguintes categorias:
a) Arquivos Lógicos Internos (ALI); Arquivos de Interface Externa (AIE).

b) Arquivos Lógicos Referenciados (ALR); Arquivos Lógicos Internos (ALI).

c) Arquivos de Interface Externa (AIE); Arquivos Lógicos Referenciados (ALR).

d) Arquivos de Interface Externa (AIE); Arquivos Referenciados Externos (AER).

2o.(IESES / MSGÁS - 2015) O sistema de reservas de automóveis de uma locadora possui uma funcionalidade que consiste em uma interface web para entrada de dados do cliente e armazenamento desses dados num banco de dados relacional. Considerando o contexto daAnálise de Pontos de Função, esta função disponibilizada pela interface no sistema será contada como:
a) Um Arquivo de Interface Externa (AIE), pois a interface permite a entrada de dados.

b) Uma Entrada Externa (EE), pois existe mudança de comportamento do sistema.

c) Uma Saída Externa (SE), pois existe dados derivados na transação.

d) Um Arquivo Lógico Interno (ALI), pois os dados foram salvos no banco de dados.

21. (VUNESP/ PRODEST-ES - 2014) Na métrica de software conhecida como ponto por função,
são considerados valores do domínio da informação. Dois desses domínios são: o número de a) desvios condicionais e de arquivos lógicos internos.
b) entradas externas e de consultas externas.

c) estruturas complexas e de loops e cases.

d) registros das tabelas e de arquivos de interface externa.

e) tabelas e de saídas externas.

22. (AOCP / UFPB - 2014) Preencha a lacuna e assinale a alternativa correta.

"Na análise de pontos de função, os requisitos funcionais devem ser identificados conforme a) a visão do programador.
b) a visão do usuário.

c) a tecnologia.

d) a linguagem de programação utilizada.

e) o sistema gerenciador de banco de dados utilizado.

23. (UFBA / UFSBA - 2014) Pontos de Função apenas medem o tamanho funcional do software baseando-se em uma avaliação padronizada dos requisitos dos usuários e, diferentemente deLinhas de Código, não são dependentes da implementação física e das linguagens utilizadas no desenvolvimento do software.
24. (ESAF/SUFRAMA-20i3) O fator de ajuste indica a:

a) viabilidade geral provida pelo projeto ou aplicação para o desenvolvedor.

b) ajustabilidade provida pelo projeto para a aplicação.

c) funcionalidade geral provida pelo projeto ou aplicação para o usuário.

d) funcionalidade geral provida pela aplicação do projeto.

e) funcionalidade setorial provida pelo projeto ou aplicação para as interfaces.

25.OBFC / EBSERH - 2013) Se o total de Pontos de Função não ajustados for 107, e o nível de influência geral dado é 30, teremos como total de pontos de função ajustados:
a) 91,65

b) 100,65

c) 101,65

d) 102,65.

26.(IBFC / EBSERH -2013) Em APF (Análise de Pontos de Função) existe o importante conceito de
Ponto de Função. Pode-se conceituar basicamente Ponto de Função como:

a) a medida do tamanho funcional do software.

b) a capacidade do hardware para processar o sistema.

c) a relação entre o hardware e o software exigido pelo sistema.

d) o ciclo de software composto pelo sistema.

27-(ESAF / CGU - 2012) São características gerais de sistema utilizadas para cálculo do fator de ajuste:
a) Reutilização, Taxa de recepção de dados.

b) Atualização off-line, Modificações facilitadas.

c) Modificações facilitadas, Processamento paralelo.

d) Entrada de dados off-line, Compatibilidade Web.

e) Múltiplos locais, Processamento complexo.

28.(ESAF / CGU - 2012) São exemplos de ALI:

a) Arquivos de índices.

b) Arquivos temporários, de trabalho ou de classificação.

c) Arquivos de backup.

d) Arquivos de mensagens de erro desde que mantidos pela aplicação.

e) Arquivos introduzidos exclusivamente em função da tecnologia utilizada.

2g.(ESAF / CGU - 2012) Cada Arquivo Lógico Interno e cada Arquivo de Interface Externa devem ser classificados com relação à sua complexidade funcional com base em:
a) Número de Tipos de Dados, Número de Tipos de Registros.

b) Número de Tipos de Arquivos, Número de Tipos de Registros.

c) Número de Tipos de Dados, Número de Tipos de Consultas.

d) Número de Tipos de Campos, Número de Tipos de Arquivos.

e) Número de Tipos de Tabelas, Número de Tipos de Campos.

30. (ESAF / CGU - 2012) São características gerais de sistema utilizadas para cálculo do fator de ajuste:
a) Reutilização, Taxa de recepção de dados.

b) Atualização off-line, Modificações facilitadas.

c) Modificações facilitadas, Processamento paralelo.

d) Entrada de dados off-line, Compatibilidade Web.

e) Múltiplos locais, Processamento complexo.

31. (CONSULPLAN /TSE-2012) A análise de Ponto de Função engloba diversas etapas, sendo que a contagem está associada fundamentalmente a projetos de desenvolvimento e de melhoria.Nesse contexto, uma função é representada pelas necessidades do usuário em termos de processamento de dados e que caracteriza a lógica, sendo identificadas como entradas externas(EE), saídas externas (SE) e consultas externas (CE). Essa descrição caracteriza o tipo denominado Funções a) Dados.
b) Processos.

c) Transacionais.

d) Organizacionais.

32. (ESAF - 2010 - SUSEP - Analista de Sistemas) Na contagem de Arquivos
Lógicos
Referenciados (ALR):

a) não se deve contar ALR para Arquivo Lógico Interno mantido.

b) deve-se contar dois ALR caso haja acesso a arquivo de mensagens de erros.

c) deve-se contar um ALR caso haja acesso apenas a arquivos criptografados.

d) deve-se contar um ALR para cada par de Arquivos Lógicos Internos que são lidos e mantidos por entidades externas distintas.
e) deve-se contar apenas um ALR para cada Arquivo Lógico Interno que é lido e mantido por uma entidade externa.
33. (ESAF / MPOG - 2010) Assinale a afi rmativa correta relativa à Análise por
Pontos de Função
(APF).

a) Uma Consulta Externa é um relacionamento composto por entradas que resultam em uma exclusão de informação.
b) A complexidade de um Arquivo Lógico Interno é calculada a partir da quantidade de
Registros
Físicos Direcionados.

c) O objetivo principal da APF é medir a funcionalidade de um software ou aplicativo,
baseando-
se primeiramente no desenho lógico e de acordo com a perspectiva do usuário.

d) São Arquivos Lógicos Internos: cadastros de clientes e de produtos, arquivo de classificação e arquivos temporários.
e) A quantidade de Arquivos Lógicos Internos é calculada a partir da quantidade de
Arquivos
Referenciados e da manipulação de Dados Elementares.

34.(ESAF / CVM - 2010) O cálculo dos pontos de função de um projeto de desenvolvimento consiste dos componentes de funcionalidade:
a) reusabilidade de aplicação; reusabilidade de conversão; fator de ajuste da aplicação.

b) funcionalidade de aplicação; funcionalidade de compressão; fator de ponderação da aplicação.
c) reusabilidade de aplicação; funcionalidade de programação; fator de ajuste da aplicação.

d) funcionalidade de aplicação; funcionalidade de conversão; fator de ajuste da aplicação.

e) funcionalidade de programação; funcionalidade de conversão;
funcionalidade de manutenção.
35. (ESAF / CVM - 2010) Algumas das Características Gerais do Sistema (CGS) são:

a) Comunicação de Dados. Funções intrínsecas. Performance. Especificação de equipamento.
Saída de dados on-line. Processamento complexo. Reusabilidade.
Facilidade de
Implementação.

b) Transmissão de Dados. Funções distribuídas. Modularidade. Fornecedores de equipamentos.
Entrada de dados on-line. Processamento complexo. Reengenharia. Múltiplos subprogramas.

c) Comunicação de Dados. Servidores distribuídos. Performance.
Configuração de equipamento. Entrada de dados on-line. Processamento cognitivo. Facilidade deManutenção.
Múltiplos locais.

d) Comunicação de Dados. Funções distribuídas. Performance. Configuração de equipamento.
Entrada de dados on-line. Processamento complexo. Reusabilidade. Facilidade de Implantação.

e) Transmissão de Dados. Ações distribuídas. Performance. Configuração de equipamento.Entrada de dados on-line e off-line. Direcionamento complexo. Reusabilidade.
Facilidade de
Implantação.

36. (ESAF / CVM - 2010) Baseando-se nas Características Gerais do Sistema (CGS), um dos passos para o cálculo do fator de ajuste é:
a) avaliar o impacto de cada uma das 14 CGS no aplicativo que está sendo contado,
atribuindo peso de 0 a 5 para cada característica.
b) calcular o nível de influência por meio da multiplicação dos pesos de cada uma das 14 CGS.

c) avaliar as entradas de cada uma das 14 CGS no aplicativo que está sendo contado,
atribuindo peso de 0 a 10 para cada característica.
d) avaliar o impacto de cada uma das 14 CGS no aplicativo que está sendo contado,
atribuindo peso de 0 a 10 para cada característica.
e) calcular o nível de influência por meio da soma dos pesos da primeira metade das 14 CGS.

37-(ESAF / CVM - 2010) Considerando Arquivos de Interface Externa (AIE), na contagem de
Registros Lógicos Referenciados (RLR),

a) caso não haja um subgrupo de informações, conte um RLR para cada dupla de AIE.

b) conte um RLR para cada subgrupo de dados de um AIE, somente quando o subgrupo for mandatório.
c) conte um RLR para cada subgrupo de dados de um AIE, somente quando o subgrupo for opcional.
d) caso não haja um subgrupo de informações, não conte RLR para nenhum AIE.

e) conte um RLR para cada subgrupo de dados de um AIE, seja o subgrupo opcional ou mandatório.
38.(ESAF / SUSEP - 2010) São Características Gerais do Sistema (CGS) do fator de ajuste que avaliam a funcionalidade geral da aplicação:
a) Performance, Pontos de transição e Composição on-line.

b) Comunicação de dados, Interface com o usuário e Reusabilidade.

c) Taxa de acertos, Funções de transações e Atualização on-line.

d) Saída de dados on-line, Facilidade de planejamento e Performance.

e) Comunicação de transações, Interação entre programas e Usabilidade.

GABARITo

1. LETRA D 14. LETRA B
27- LETRA E

2. LETRA B 15- LETRA A
28. LETRA D

3- LETRA A 16. LETRA B
29. LETRA A

4- LETRA E 17- LETRAC
30. LETRA E

5- LETRA A 18. LETRA B
31- LETRA C

6. LETRA E 19. LETRA A
32. LETRA E

7- LETRAC 20. LETRA B
33- LETRA C

8. LETRA B 21. LETRA B
34- LETRA D

9- LETRA C 22. LETRA B
35- LETRA D

10. LETRA D 23- CORRETO
36. LETRA A

li. CORRETO 24. LETRA C
37- LETRA E

12. LETRA A 25- LETRAC
38. LETRA B

13- LETRA C 26. LETRA A

