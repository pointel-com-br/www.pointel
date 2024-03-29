# Desenvolvimento de Informação - Ciência de dados. Big Data. Processamento distribuído. Data lake

Índice

1) Introdução Big Data, NoSQL e Hadoop

2) NoSQL

3) Hadoop

4) Metadados de Arquivos

5) Questões Comentadas - Big Data, NoSQL e Hadoop - Multibancas

INTRoDUçÃo

Nesta aula nosso intuito é desenvolver um pouco seu conhecimento sobre bancos de dados não relacionais ou NoSQL (Not onlySQL). Esse conceito surgiu pela necessidade de utilização de Big Data.Ou, visto de uma forma mais intuitiva, da necessidade de tratar um grande volume de dados das mais variadas formas, gerados em uma velocidade cada vez mais acelerada.
Podemos falar sobre espaço de armazenamento, algo semelhante ao que dizemos a respeito de dinheiro, você tende a utilizar todo o espaço de armazenamento disponível. Considerando que o custo de armazenamento fica cada vez menor, principalmente com o surgimento de CloudComputing, é possível focar nossa atenção na organização destas bases e no processamento dos dados.
Para isso, utilizamos respectivamente bases de dados NoSQL e a infraestrutura de processamento e armazenamento distribuído como o Hadoop. Vem comigo conhecer um pouco deste universo paralelo de banco de dados! ©
BIG DATA: DEFINIçõES E CoNCEIToS

A humanidade, nos dias de hoje, produz uma quantidade diária de dados que é simplesmente improcessável pelos próprios seres humanos.
Para se ter uma ideia, a IBM, em 2013, estimou que 2,5 exabytes
(2.500.000.000.000.000.000) de bytes de dados são criados por dia. Se cada um dos 7 bilhões de habitantes tivesse que se debruçar sobre essas informações, seriam aproximadamente 300MB de dados diários para cada cidadão,incluindo bebês e idosos, rs.

São vídeos no youtube, postagens em redes sociais, blogs, portais de notícias, emails,
dentre outros.
E o que esses dados possuem em comum? São dados não-estruturados. Estima-se que 85%
das informações com as quais as empresas lidam hoje não estão estruturadas. Desta forma, o SGBD
tradicional e a modelagem relacional (datados da década de 60) não são mais suficientes para lidar com a realidade atual. É necessária uma nova abordagem. Surge então o conceito de Big Data!
Big Data pode ser entendido como a captura, gerenciamento e análise de dados que vão além de dados estruturados típicos, que podem ser consultados por sistemas de gerenciamento de banco de dados relacional — frequentemente em arquivos não estruturados, vídeo digital, imagens, dados de sensores, arquivos de log e, na verdade,qualquer dado não contido nos registros com campos pesquisáveis distintos.

Em um certo sentido, os dados não estruturados são dados interessantes, mas difíceis de sintetizar ou tirar conclusões deles, a menos que possam ser correlacionados a dados estruturados.Big data apresenta soluções para integrar os dados estruturados e desestruturados.
Em um primeiro momento, o Big Data pode até ser confundido com a Business
Intelligence, mas difere na ordem de grandeza do volume de dados (que é muito maior), e na natureza dos dados.Enquanto as ferramentas de BI tradicionais extraem dados de fontes estruturadas, "abrindo exceções para a captura de dados não estruturados", o Big Data entende que os dados não-estruturados são a "maioria", por assim dizer.

Nossa ideia é começar o assunto apresentando, de forma sucinta, os conceitos básicos que permeiam o termo Big Data. Vamos começar pela definição que surgiu em 2001 no MetaGroup
(que viria a se juntar com a Gartner1 mais adiante) por meio do analista Doug Laney.
Para compor o conceito ele se utilizou de três termos, conhecidos como os 3Vs: Volume, Velocidade eVariedade.
Vejamos a definição de cada um deles.

TOME NOTA!

Volume. Existem muitos fatores que contribuem para o aumento do volume de dados armazenados e trafegados. Podemos citar como exemplo: dados de transações armazenados ao longo de vários anos, dados de texto, áudio ou vídeo disponíveis em streaming nas mídias sociais e a crescente quantidade de dados coletados por sensores.No passado o volume de dados excessivo criou um problema de armazenamento. Mas,
com os atuais custos de armazenamento decrescentes, outras questões surgem,incluindo, como determinar a relevância entre grandes volumes de dados e como criar valor a partir dessa relevância.
Velocidade. De acordo com o Laney, velocidade significa o quão rápido os dados estão sendo produzidos e o quão rápido os dados devem ser tratados para atender as demandas. Etiquetas de RFID e sensores inteligentes estão impulsionando uma
1 Gartner é uma empresa de consultoria fundada em 1979 por Gideon Gartner.
A Gartner desenvolve tecnologias relacionadas a introspecção necessária para seus clientes tomarem suas decisões todos os dias.
necessidade crescente de lidar com dados quase em tempo real. Reagir rápido o suficiente para lidar com a velocidade é um desafio para a maioria das organizações.
Variedade. Os dados de hoje vêm em todos os tipos de formatos. Sejam bancos de dados tradicionais, hierarquias de dados criadas por usuários finais e sistemas OLAP, arquivos de texto, e-mail, medidores ou sensores de coleta de dados, vídeo, áudio, dados de ações do mercado e transações financeiras. Em algumas estimativas, 80% dos dados de uma organização não são numéricos! Mas, estes dados também precisam ser incluídos nas análises e nas tomadas de decisões das empresas.
Big Data é importante porque permite que as organizações recolham, armazenem,
administrem e manipulem grandes quantidades de dados na velocidade certa, no tempo certo para conseguir os conhecimentos corretos. A novidade é que, pela primeira vez, o custo de ciclos de computação e armazenamento alcançou uma relação interessantes de curso x benefício. Por que isso é importante? Há alguns anos atrás, as empresas normalmente armazenariam"fotos" ou subconjuntos de informações importantes, porque o custo de armazenamento e a limitação do processamento os impedia de armazenar tudo o que queriam analisar.
Além da melhoria na capacidade de processamento e armazenamento, melhorias na velocidade de rede e confiança removeram outras limitações físicas da capacidade de administrar quantidades massivas de dados a um passo aceitável. Assim, as organizações querem ser capazes de compreender e acionar resultados de diferentes tipos de dados na velocidade certa —não importa quantos dados estejam envolvidos.
Se as empresas podem analisar peta bytes de dados (o equivalente a 20 milhões de gabinetes, com quatro gavetas cheias de arquivos de texto ou 13.3 anos de conteúdo de HDTV) com desempenho aceitável para discernir padrões e anomalias, elas podem começar a compreender dados de novas maneiras.
Judith Hurwiz, et ai - Big Data Para Leigos

A mudança para Big Data não é exclusivamente em negócios. Ciência, pesquisa e atividades do governo também ajudaram a impulsioná-la. Pense sobre analisar o genoma humano ou lidar com todos os dados astronômicos coletados em observatórios para avançar nosso conhecimento do mundo à nossa volta. Considere também a quantidade de dados que o governo coleta em suas atividades antiterroristas e você entenderá a ideia de que Big Data não é só sobre negócios.
RESUMINDO

Volume

Velocidade

Variedade

W* V*W* V**V

Dados em repouso

* Terabytes ou exabytes de dados existentes para o processo
Dados em movimento
* Streaming data (fluxo de dados
* Requer milissegundos ou segundos para resposta.
O

* *
o

Dados em diferentes formas
* Estruturados

* Semiestruturado

* Não estruturado

* Texto

* Multimídia

Dados em dúvida

* Incerteza sobre a consistência e completude.
* Ambiguidade, latência,
modelos de aproximação.
Dados em dinheiro

* Os dados devem estar associados aos modelos de negócio.
* Preocupação com a geração de retorno.
Vejam a figura apresentada acima. Ela representa uma indicação do conceito de
Big Data relacionando os três V's sobre os quais tratamos até agora, adicionando duas caraterísticas:veracidade e valor. Contudo, existem ainda outros V's, são eles Visibilidade,
Variabilidade e
Visualização que complementam o conceito, detalhando um pouco mais algumas características deBig Data. Vamos apresentar a definição destes termos no quadro abaixo.

INDO MAIS

FUNDO!

Veracidade. A veracidade foi um termo cunhado pela IBM, considerado o quarto V, que representa a falta de confiabilidade inerente em algumas fontes de dados. Por exemplo,medir os sentimentos dos clientes em mídias sociais é incerto por natureza,
já que implicam uso do juízo humano. No entanto, eles contêm valiosas informações. Assim, a necessidade de lidar com dados imprecisos e incertos é outra faceta de BigData,
geralmente resolvida usando ferramentas e análises desenvolvidas para gerenciamento e mineração de dados imprecisos.
É necessário avaliar as inconsistências, incompletudes, ambiguidades, latência e possíveis modelos de aproximação utilizados. Os dados podem ainda perder a vigência. Verificar se os dados são consistentes é extremamente necessário para qualquer análise de dados.
Visibilidade. É a relevância dos dados. A organização está ciente de todos os dados que ele gera? Estes poderiam ser (aparentemente) registros de dados inconsequentes. Em outras palavras tentamos entender se todos os dados gerados estão disponíveis, e se são de fato armazenados e ficam visíveis para os analistas de dados.
Valor. A Oracle introduziu valor como um atributo na definição de Big Data. Com base na definição da Oracle, Big Data é, muitas vezes, caracterizado por uma "densidade de valor relativamente baixa". Isto é, os dados recebidos na forma original, geralmente tem um valor baixo em relação ao seu volume. Entretanto, um valor elevado pode ser obtido pela análise de grandes volumes destes mesmos dados. Assim, as informações geradas devem produzir algum valor para as organizações.
Variabilidade (e complexidade). A SAS apresentou variabilidade (e complexidade) como duas dimensões adicionais para Big Data. Variabilidade refere-se à variação nas taxas de fluxo de dados. Muitas vezes, a velocidade de Big Data não é consistente e tem picos e depressões periódicas. Complexidade refere-se ao fato de Big Data gerar ou receber informações através de uma multiplicidade de fontes. Isso impõe um desafio crucial: a necessidade de se conectar, integrar, limpar e transformar os dados recebidos de diferentes fontes.
Visualização. É o modo como aqueles dados complexos serão representados ou apresentados.
Big data é um termo utilizado para descrever grandes volumes de dados e que ganha cada vez mais relevância à medida que a sociedade se depara com um aumento sem precedentes no número de informações geradas. As dificuldades em armazenar, analisar e utilizar grandes conjuntos de dados têm sido um considerável gargalo para as organizações. Vamos fazer mais uma questão recente sobre esses conceitos:
CAIU

na prova!

1. Ano: 2017 Órgão: TCE-PE Cargo: Auditor de Obras Públicas Questão: 120

Com relação a Big Data, julgue o item subsequente.

[120] Além de estar relacionado à grande quantidade de informações a serem analisadas,
o Big
Data considera o volume, velocidade e a variedade dos dados estruturados - dos quais se conhece a estrutura de armazenamento - bem como dos não estruturado, como imagens,vídeos, áudios e documentos.

Comentário: Big Data é o termo que descreve o imenso volume de dados - estruturados e não estruturados - que impactam os negócios no dia a dia. A definição da questão está perfeitamente de acordo com o conceito, citando inclusive os 3Vs da definição inicial de DougLaney. Sendo assim, a resposta para esta alternativa está correta.

Gabarito: C

Dimensões sobre os dados

A IBM cita atualmente 7 dimensões sobre os dados. Essas dimensões são uma outra forma de apresentar as características que vimos até o momento. As definições de velocidade,variedade,
volume, valor e variedade são as mesmas neste contexto. Incluímos mais duas percepções que não foram listadas acima: governança e pessoas. Vejamos suas definições:
Governança - Ao decidir implementar ou não uma plataforma de big data, uma organização pode estar olhando novas fontes e novos tipos de elementos de dados nos quais a propriedade não está definida de forma clara. Por exemplo, no caso de assistência médica, é legal acessar dados de paciente para obter insight? É correto mapear as despesas do cartão de crédito do cliente para sugerir novas compras? Regras semelhantes regem todos os segmentos de mercado. Além da questão da governança de TI, também pode ser necessário redefinir ou modificar os processos de negócios de uma organização para que ela possa adquirir, armazenar e acessar dados externos.
Pessoas - É necessário ter pessoas com aptidões específicas para entender, analisar os requisitos e manter uma solução de Big Data. Envolve conhecimento do segmento de mercado, domínio técnico sobre as ferramentas de Big Data e conhecimentos específicos de modelagem, estatística e outros.
Essas duas dimensões, na percepção da IBM, juntamente com volume, variedade,
velocidade,
veracidade e valor dão viabilidade a um projeto de Big Data, podemos observar de forma organizada esses termos na figura abaixo.
á k

Giovernanc;a

F

*

Pessoas

^F

Volume

^F

w á k ariedad e
F

3lociadac

Valor

^F

á k

Veracidadle

F

Big data trata, portanto, de grandes volumes, alta velocidade e variedade dos ativos de informação,procurando formas inovadoras e rentáveis de processamento da informação, visando uma melhor percepção dos fatos e uma tomada de decisão mais consistente.
Outra definição da TechAmerica define big data da seguinte forma:

"Big Data é um termo que descreve grandes volumes de dados de alta velocidade, complexos e variáveis que exigem técnicos e tecnologias avançadas para permitir a captura, armazenamento, distribuição, gestão e análise da informação".
Antes de serguirmos em frente veja no infográfico do Jornal O Globo algumas soluções corporativas que envolvem Big Data:
A NOVIDADE

A grande novidade das soluções de Big Data é lidar também com os chamados dados nào-estruturados, que até então só podiam ser compreendidos por pessoas. São tweets,posts no Facebook, videos, geolocalização e comportamentos de clientes que dependem de contexto para ter sentido.
Esses dados não-estruturados representam 85% das informações com as quais as empresas lidam hoje
85%

O mercado de Big
Data crescerá quase 40% ao ano até 2015
A quantidade global de dados digitais deve crescer de 1,8 zetta byte, hoje, para
7,9 zettabytes em 2015. Daqui a três anos,

toda a informação do mundo poderá ser armazenada em:
bilhões de iPads
COMPARE

1 Zettabyte é igual
1.000.000.000.000.000.000.000 bytes

1 Gigabyte é igual
1.000.000.000 bytes

Alguns exemplos de como a solução tem sido usada

A companhia Skybox tira fotos de satélite e vende a seus clientes informações em tempo real sobre a disponibilidades de vagas de estacionamento livres numa cidade em determinada hora ou quantos navios estào ancorados no mundo neste momento
O projeto Global Pulse,
das Nações Unidas, vai utilizar um programa que decifra a linguagem humana na análise de mensagens de texto e posts em redes sociais para prever o aumento do desemprego, o esfriamento econômico e epidemias de doenças
A varejista americana
Dollar General monitora as combinações de produtos que seus clientes põem nos carrinhos. Ganhou eficácia e ainda descobriu curiosidades: quem bebe Gatorade tem mais chances de comprar também laxante
A Sprint Nextel saltou da última para a primeira posição no ranking de satisfação dos usuários de celular nos EUA ao integrar os dados de todos os seus canais de relacionamento. De quebra, cortou pela metade os gastos com call center
No terremoto do
Haiti, pesquisadores americanos perceberam antes de todo mundo a diáspora de PortoPríncipe por meio dos dados de geolocalização de 2
milhões de chips SIM
de celulares,
facilitando a atuação da ajuda humanitária
—————TT————

Um hospital no
Canadá usou tecnologia da IBM e da Universidade deOntário para monitorar em tempo real dezenas de indicadores de saúde de bebés prematuros.O cruzamento permitiu aos médicos antecipar ameaças às vidas das crianças
Em busca dos melhores lugares para instalar turbinas eólicas, a dinamarquesa VestasWind analisou petabytes de dados climáticos, de nível das marés, mapas de desmatamento etc. Oque costumava levar semanas durou algumas horas p
Big Data pelo mundo. Fonte: Jornal O Globo.

Entendido os conceitos básicos vamos avançar no assunto. Antes de falar sobre as premissas e aplicações, gostaria de tecer alguns comentários sobre falácias ou mitos associados a Big Data.
FALÁCIAS2 SoBRE BIG DATA

Quando pensamos em premissas sobre Big Data imaginamos uma caixa preta que vai receber dados de um lado e entregar algo pronto do outro. Nesta linha de raciocínio, provavelmente falaciosa,antes de apresentamos as condições ideias para funcionamento dos sistemas ou projetos de BigData, nós mostraremos os erros que muitos assumem como verdade. Chamaremos de falácias ou mitos sobre Big Data.
Falácia 01 - Big Data engloba somente dados estruturados.

Com o crescente volume de dados, o banco de dados relacional precisou ser complementado com outras estruturas de armazenamento, devido principalmente à escalabilidade e flexibilidade das novas soluções tecnológicas. Entretanto, os dados relacionais continuam sendo valiosos e são muito utilizados em soluções de Big Data. O que mudou de fato foi a inclusão de mais tipos de dados, além dos estruturados. Lembre-se do conceito de variedade.
Falácia 02 - Big Data refere-se somente a soluções com petabytes de dados

Embora o volume de dados seja o fator que impulsionou o fenômeno Big Data, aplicações que utilizam conjuntos de dados em uma escala menor do que petabytes também podem se beneficiar das tecnologias de Big Data. Afinal, o mais importante nessas aplicações é a capacidade de extrair valor dos dados.
Falácia 03 - Big data é aplicado somente às empresas do Vale do Silício (Califórnia)

Quando se fala em Big Data, é normal associarmos os termos às grandes empresas de tecnologia que prestam serviços na Web, tais como Facebook, Twitter, Netflix, Google. Embora elas tenham sido as primeiras a serem desafiadas com o grande volume, variedade e velocidade de dados,atualmente empresas de outros domínios, como agricultura, varejo e logística,
também se beneficiam das tecnologias de Big Data.
Falácia 04 - Big Data é aplicado somente em grandes organizações

Ainda existe essa percepção de que Big Data oferece valor exclusivamente para grandes organizações. Entretanto, pequenas e médias empresas também podem obter vantagem competitiva por meio de soluções de Big Data, oferecendo uma melhor experiência aos seus clientes,otimizando processos, reduzindo custos ou criando novos produtos e serviços.

Falácia 05 - Big Data requer uso de dados externos

Embora a adoção de dados de diferentes fontes seja uma prática muito adotada em soluções de BigData, a aquisição de dados externos é um requisito obrigatório. Na verdade, a sugestão para quem inicia um projeto de Big data é buscar extrair valor primeiramente dos dados internos para somente depois ampliar suas jornadas a dados de terceiros.
2 O termo falácia deriva do verbo latino fallere, que significa enganar. Designa-se por falácia um raciocínio errado com aparência de verdadeiro. Na lógica e na retórica, uma falácia é um argumento logicamente inconsistente, sem fundamento, inválido ou falho na tentativa de provar eficazmente o que alega.
Falácia 06 - Big Data pode prever o futuro

Big data e todas as suas ferramentas de análise, comentários, experiências científicas e visualizações não podem dizer o que vai acontecer no futuro. Por quê? Os dados que você coletar vem inteiramente do passado. Temos ainda de atingir um grau de evolução em que será possível coletar dados e os valores do futuro. Sendo assim, nós podemos analisar o que aconteceu no passado e tentar desenharas tendências entre as ações e os pontos de decisão, e as suas consequências,baseadas nos dados. Podemos usar isso para adivinhar que, em circunstâncias semelhantes, se uma decisão semelhante for tomada, resultados semelhantes ocorreriam como resultado.Mas não podemos prever o futuro.
Falácia 07 - Big Data pode substituir seus valores ou os da sua organização

Big Data é pobre para substituir valores ou aqueles costumes e padrões pelos quais você vive sua vida e sua empresa se esforça para operar. Suas escolhas sobre essas questões podem ser bem cristalinas, e pode ser mais fácil e claro resolver as vantagens e desvantagens de diferentes cursos da ação, mas os dados em si não podem ajudá-lo a interpretar como as decisões certas se comparam com os padrões que você definiu para si e para a sua empresa.
Os dados podem descrever todos os tipos de cenários, tanto os próprios números quanto com a ajuda de software de visualização. Sua equipe pode criar muitas projeções de cenários sobre um determinado assunto, mas esses resultados são simplesmente isso - uma projeção. Otrabalho de um executivo, como um CIO, é utilizar as ferramentas e pessoal disponível dentro de seu negócio, e realmente reconciliar os dados contra os valores da sua empresa.
Falácia 08 - Big Data pode resolver problemas não quantificáveis

Eis o velho ditado: Quando você só tem um martelo, tudo parece um prego. Uma vez que você começa a ter algum sucesso usando big data para prever e resolver problemas de negócios, haverá inevitavelmente uma tentação para "perguntar aos dados" toda vez que você tiver um problema ou um item sobre o qual a resolução não está clara.
Como mencionado anteriormente, os dados podem apresentar mais e melhores opções e,
talvez,
deixar claro o que pode acontecer com cada uma dessas escolhas. Às vezes, porém, os dados não são bons e isso ocorre quando ele é usado de forma individual.
Por quê? É quase impossível de quantificar o comportamento de um indivíduo. As pessoas têm seus próprios conjuntos de circunstâncias, os seus próprios universos, suas próprias razões e contextos.É impossível aplicar a matemática para um único indivíduo. Em vez disso, você tem que olhar para um grupo de indivíduos, de preferência um subgrupo com características semelhantes. Só então você pode observar as tendências de comportamento que se aplicam a todo o grupo.
Agora que sabemos o que pode e o que não pode ser feito com Big Data, vamos entender quais as premissas que devem ser verificadas quando decidimos pela implementação de um projeto de BigData. Primeiro precisamos considerar os elementos fundamentais para o crescimento de Big
Data tais como o aumento da capacidade de armazenamento, aumento do poder de processamento e disponibilidade de dados.
APLICAçõES DE BIG DATA

As aplicações de Big Data e análise de dados são as mais variadas. Uma lista retirada do livro doAguinaldo Aragon nos traz as seguintes opções de uso: desenvolvimento de mercado,
inovação,
desenvolvimento de produtos e serviço, eficiência operacional, previsões de demanda de mercado,detecção de fraudes, gerenciamento de riscos, previsão de concorrência, vendas, campanhas de marketing, avaliação de desempenho de funcionários, alocação de orçamento anual,estabelecimento de previsões financeiras, gestão de planos de saúde, identificação de potenciais compradores e entendimento da base de cliente. Essa lista extensa nos mostra apenas parte das oportunidades geradas pela utilização de Big Data.
O uso de Big Data por empresas como Amazon e Netflix tem demostrado como a mineração de dados pode gerar resultados surpreendentes. A partir destes dados, é possível conhecer melhor as escolhas dos usuários. Implementações dos conceitos de Big Data permitem, hoje,possibilidades quase infinitas, utilizando, por exemplo, mineração de dados conseguimos verdadeiros insights sobre os dados.
Um exemplo disso foi a pesquisa feita pela Consultoria MGI. Ela estudou dados em cinco grandes domínios - saúde nos Estados Unidos, o setor público na Europa, varejo nos EstadosUnidos, dados de produção e dados de localização de pessoas em nível mundial. Big Data poderia gerar valor em cada um deles. Por exemplo, um varejista pode utilizar do conceito para aumentar sua margem operacional em mais de 60%.
Oaproveitamento de Big Data no setor público tem um potencial enorme também. Se o programa de saúde dos Estados Unidos fosse usar big data de forma criativa e eficaz poderia impulsionar a eficiência e qualidade, o setor poderia criar mais de US$ 300 bilhões em valor a cada ano. Dois terços dos quais seriam sob a forma de redução nas despesas de saúde dos EUA em cerca de 8 por cento.Nas economias desenvolvidas da Europa, os administradores do governo poderiam economizar mais de € 100 bilhões em melhorias de eficiência operacional usando big data, não incluindo o uso para reduzir a fraude e erros ou aumentar a cobrança das receitas fiscais.
A quantidade de dados em nosso mundo está explodindo, e a análise de grandes conjuntos de dados
- os chamados big data - se tornará uma base essencial na concorrência pelo mercado ou na prestação de um serviço público de qualidade, apoiando novas ondas de crescimento na produtividade, inovação e expectativa dos consumidores. Líderes em todos os setores terão de lidar com as implicações de Big Data, não apenas os gestores orientados a dados, ou cientistas de dados.
O crescente volume e detalhamento das informações capturadas por empresas, o aumento de dados multimídia, mídia social, e a Internet das Coisas vão alimentar o crescimento exponencial dos dados no futuro.
A minha experiência pessoal no estudo de Big Data é que quando começamos a ler sobre o assunto esses conceitos teóricos vistos até aqui são apresentados de forma semelhante em vários artigos disponíveis na internet e em livros especializados, mas aí você deve estar fazendo a seguinte pergunta: E como eu implemento esse trem? (Homenagem aos meus amigos mineiros). Ealguém vai te responder: usa uma base NoSQL com a infraestrutura do Hadoop!
CAIU

na prova!

2. Ano: 2017 Banca: CESPE Órgão: TCE-PE Cargo: Analista De Controle Externo Área: Auditoria
De Contas Públicas Questão: 120

No que se refere a Big Data, julgue o item subsecutivo.

120 O termo Big Data Analytics refere-se aos poderosos softwares que tratam dados estruturados e não estruturados para transformá-los em informações úteis às organizações,permitindo-lhes analisar dados, como registros de call center, postagens de redes sociais, de blogs, dados de CRM e demonstrativos de resultados.
Comentário: Vejamos uma definição forma de Big Data Analytics: "... é o trabalho analítico e inteligente de grandes volumes de dados, estruturados ou não-estruturados,que são coletados, armazenados e interpretados por softwares de altíssimo desempenho. Trata-se do cruzamento de uma infinidade de dados do ambiente interno e externo, gerando uma espécie de "bússola gerencial" para tomadores de decisão."
Vejam que a definição está plenamente de acordo com o texto da questão, nos habilitando a confirmar como correta a alternativa.
Gabarito: C

CLASSIFICAçÃo DE BIG DATA

É possível categorizar problemas de negócios em tipos de problemas de big data. Quando problemas de big data são categorizados por tipo, é mais fácil ver as características de cada tipo de dados.Essas características ajudam a entender como os dados são obtidos, como são processados para o formato apropriado e com que frequência novos dados estão disponíveis.
Dados de diferentes fontes possuem características diferentes; por exemplo, dados de mídia social podem ter vídeos, imagens e texto não estruturado, como postagens de blog, entrando continuamente.
Quer conferir alguns exemplos? A tabela a seguir contém problemas comuns de negócios e atribui um tipo de big data a cada um.
ESQUEMATIZANDO

Problemas de negócios

Tipo de big data

Descrição

Serviços públicos:
Prever o consumo de energia
Dados gerados por máquina
Concessionárias de serviços públicos implementaram medidores inteligentes para medir o consumo de água, gás e eletricidade a intervalos regulares de uma hora ou menos. Esses medidores inteligentes geram enormes volumes de dados de intervalo que precisam ser analisados.
Para ter eficiência operacional, a empresa precisa monitorar os dados entregues pelo sensor. Uma solução de big data pode analisar dados de geração de energia (fornecimento) e de consumo de energia(demanda) usando medidores inteligentes.

Telecomunicações:
Analítica de perda de clientes
Dados da web e sociais
Dados de transação(operacionais)

Operadores de telecomunicações precisam criar modelos detalhados de perda de clientes que incluam dados de mídias sociais e de transação, para estar à frente da concorrência.
Provedores que implementam uma estratégia de analítica preditiva podem gerenciar e prever a perda analisando os padrões de chamada dos assinantes.
Varejo: Sistema de mensagens personalizado com base em reconhecimento facial e mídia social
Dados da web e sociais
Biométrica

Varejistas podem usar tecnologia de reconhecimento facial combinada a uma foto da mídia social para fazer ofertas personalizadas a clientes com base no comportamento de compra e na localização.
Esse recurso pode ter um impacto tremendo nos programas de fidelização dos varejistas, mas há sérias considerações sobre a privacidade. Os varejistas precisariam ser transparentes com relação à privacidade para implementar esses aplicativos.
Problemas de negócios de big data por tipo. Fonte:
http://www.ibm.com/developerworks/br/librarv/bd-
archpatternsl/

A figura a seguir mostrará as várias categorias ou taxonimias que podemos usar para classificar BigData, e as possíveis divisões ou grupos em cada categoria. As categorias mais relevantes estão em azul turquesa.
Analysis Type

Data Frequency

On demand

Contmuous

Time series feedsPiê mey fie avente vn «nwdty. weeAy. daty

'rv>-»'7 pe* wiiXe w íwcrxí òeirt

Meta Data Master Data

Histoncal

Transactional

Structured

Images

Text

Unstructored

Videos

Semi-
Structured

Documei Audio rmag®*. Tert. ixi«o.í. Auaw »r.c Doam**** «ao fie at -7p»Strucnxerf, t./nsfii.t-M»*? «wvr 5«>rv»smrf«ri)0

Hardware

Comnxxity
Hardware

State of Art
Hardware

| | Key Cateporlee for õennirg &o Date Petterie j

Falando um pouco mais sobre as classificações:

Tipo de análise — Se os dados são analisados em tempo real ou agrupados para análise posterior.Essa escolha afeta várias outras decisões sobre produtos, ferramentas, hardware, fontes de dados e a frequência estimada dos dados. Para alguns casos de uso é necessária uma mistura dos dois tipos.
Metodologia de processamento — O tipo de técnica a ser aplicada para processar dados
(por exemplo, preditiva, analítica, consulta ad hoc e relatórios). As necessidades de negócios determinam a metodologia de processamento apropriada. É possível usar uma combinação de técnicas.A escolha de metodologia de processamento ajuda a identificar as ferramentas e técnicas apropriadas para uso na solução de big data.
Frequência e tamanho dos dados — O volume estimado de dados e a frequência com que chegam.
Saber a frequência e o tamanho ajuda a determinar o mecanismo de armazenamento,
formato de armazenamento e as ferramentas necessárias de pré-processamento. Frequência e tamanho de dados dependem das fontes.
* Sob demanda, como dados de mídia social

* Feed contínuo, em tempo real (dados de clima ou transacionais)

* Série temporal (dados com base em tempo)

Tipo de dados — Tipo dos dados a serem processados — transacionais, históricos,
principais e outros. Saber o tipo de dados ajuda a segregar os dados no armazenamento.
Formato de conteúdo — Formato dos dados recebidos — estruturados (SGBDR, por exemplo),
não estruturados (áudio, vídeo e imagens, por exemplo) ou semiestruturados. Oformato determina como os dados recebidos precisam ser processados e é essencial para escolher ferramentas e técnicas e definir uma solução de uma perspectiva de negócios.
Fonte de dados— Fontes de dados (onde os dados são gerados) — web e mídia social,
gerados por máquina, gerados por humanos, etc. Identificar todas as fontes de dados ajuda a determinar o escopo de uma perspectiva de negócios.
Consumidores de dados — Uma lista de todos os possíveis consumidores dos dados processados:

* Processos de negócios

* Usuários corporativos

* Aplicativos corporativos

* Pessoas individuais em várias funções de negócios

* Parte dos fluxos do processo

* Outros repositórios de dados ou aplicativos corporativos

Hardware — O tipo de hardware no qual a solução de big data será implementada —
hardware barato ou de ponta. Entender as limitações do hardware ajuda na escolha da solução big data.
PADRõES ATôMICoS E CoMPoSToS DE UMA SoLUçÃo DE BIG DATA

Os padrões auxiliam a definir os parâmetros, quando da adoção de uma solução de big data.Veremos dois tipos principais: os padrões atômicos descrevem as abordagens típicas para o consumo, processamento, acesso e armazenamento de big data; os padrões compostos, que são formados por padrões atômicos, são classificados de acordo com o escopo da solução de big data.
Por apresentarem as ideias mais relevantes acerca do Big Data, exploraremos os padrões atômicos.

PADRÕES ATÔMICOS

Os padrões atômicos ajudam a identificar a forma que os dados são consumidos,
processados,
armazenados e acessados por problemas de big data. Eles também podem ajudar a identificar os componentes necessários.
Cada padrão lida com requisitos específicos — visualização, análise de dados históricos,
dados de mídia social e armazenamento de dados não estruturados, por exemplo. Os padrões atômicos podem trabalhar em conjunto para criar um padrão composto. Não há camadas ou sequência para esses padrões atômicos. Por exemplo, os padrões de visualização podem interagir com os padrões de acesso a dados para mídia social diretamente e os padrões de visualização podem interagir com o padrão de processamento de análise avançada.
Padrões atômicos de Big Data. Fonte: http://www.ibm.com/developerworks/br/library/bd-archpatterns4/

Vejamos um pouco de cada padrão atômico:

PADRÕES DE CONSUMO

Lidam com as várias formas em que o resultado da análise de dados é consumido.
Inclui padrões de consumo de dados para atender a diversos requisitos. Vejamos os principais padrões de consumo a seguir:
Visualização

A forma tradicional de visualizar dados se baseia em gráficos, painéis e relatórios de resumo. Essas abordagens tradicionais não são sempre a melhor maneira de visualizar os dados.
Os requisitos típicos para visualização de big data, incluindo os requisitos emergentes,
são listados abaixo:
* Realizar análise em tempo real e exibição de dados de fluxo

* Extrair dados de forma interativa, com base no contexto

* Executar procuras avançadas e obter recomendações

* Visualizar informações paralelamente

* Ter acesso a hardware avançado para necessidades de visualização futuristas

A pesquisa para determinar como os insights de big data podem ser consumidos por humanos e máquinas está em andamento. Os desafios incluem o volume de dados envolvido e a necessidade de associar contexto a eles. O insight dever apresentado no contexto adequado.
Descoberta ad hoc

Criar de relatórios padrão que sejam adequados para todas as necessidades de negócios,
via de regra, não é viável, pois as empresas têm requisitos de consultas de dados de negócios diversas. Os usuários precisam da capacidade de enviar consultas ad hoc, ou seja, consultas criadas"na hora",
ao procurar por informações especificas, dependendo do problema.

Aumentar os armazenamentos de dados tradicionais

Aumentar os armazenamentos de dados existentes ajuda a ampliar o escopo de dados disponível para a analítica atual para incluir dados que residem dentro e fora dos limites organizacionais, como dados de mídia social, que podem melhorar os dados principais. Ao ampliar o escopo para incluir novas tabelas de fatos, dimensões e dados principais nos armazenamentos existentes e adquirir dados de clientes a partir de mídia social, uma organização pode obter um insight mais profundo do cliente.
Notificação

Os insights de big data permitem que as pessoas, negócios e máquinas ajam instantaneamente usando notificações para indicar eventos. A plataforma de notificação deve ser capaz de lidar com o volume antecipado de notificações a serem enviadas de maneira oportuna. Essas notificações são diferentes das malas diretas ou do envio em massa de mensagens SMS, pois o conteúdo geralmente é específico para o consumidor. Por exemplo, os mecanismos de recomendação podem fornecer insights sobre a enorme base de clientes em todo o mundo, e as notificações podem ser envidas para tais clientes.
Iniciar uma resposta automatizada

Os insights de negócios derivados do big data podem ser usados para acionar ou iniciar outros processos de negócios ou transações.
PADRÕES DE PROCESSAMENTO

O big data pode ser processado quando os dados estão em repouso ou em movimento.
Dependendo da complexidade da análise, os dados podem não ser processados em tempo real. Esse padrão lida com como o big data é processado em tempo real, quase em tempo real ou em lote(rotinas batch,
processadas em horários pré-determinados).

Vejamos um pouco mais sobre esses padrões a seguir:

Análise de dados históricos

A análise de dados históricos tradicional é limitada a um período predefinido de dados, que normalmente depende das políticas de retenção de dados. Após desse período, geralmente os dados são arquivados ou limpos em virtude de limitações de armazenamento e processamento.
A análise histórica envolve analisar as tendências históricas para um determinado período, conjunto de períodos e produtos e compará-las aos dados atuais disponíveis.
Analítica Avançada

O big data fornece enormes oportunidades de obter insights criativos. É
possível correlacionar diferentes conjuntos de dados em muitos contextos. A descoberta desses relacionamentos requer técnicas e algoritmos complexos inovadores.
A análise avançada inclui previsões, decisões, processos inferenciais, simulações,
identificações de informações contextuais e resoluções da entidade. Os aplicativos de analítica avançada incluem análise de dados biométricos, por exemplo, análise de DNA, análise espacial, analítica baseada em localização, análise científica, pesquisa e muitas outras. A analítica avançada requer a computação exigente para gerenciar a enorme quantidade de dados.
Pré-processar dados brutos

A extração de dados a partir de dados não estruturados, como imagens, áudio, vídeo,
feeds binários ou até mesmo texto, é uma tarefa complexa e precisa de técnicas como aprendizado de máquina e processamento de idioma natural, etc. O outro grande desafio é como verificar a precisão e a exatidão do resultado de tais técnicas e algoritmos.
Para executar a análise em quaisquer dados, eles devem estar em algum tipo de formato estruturado. Os dados não estruturados acessados de várias fontes podem ser armazenados como estão e, em seguida, transformados em dados estruturados e novamente armazenados nos sistemas de armazenamento de big data. O texto não estruturado pode ser convertido em dados estruturados ou semiestruturados. Da mesma forma, os dados de imagem, áudio e vídeo precisam ser convertidos nos formatos que podem ser usados para análise. Além disso, a precisão e exatidão da analítica avançada que usa algoritmos preditivos e estatísticos dependem da quantidade de dados e algoritmos usados para treinar os modelos.
CAIU

na prova!

3. Ano: 2014 Banca: CESPE Órgão: TJ/SE Cargo: Analista Judiciário

Em soluções Big Data, a análise dos dados comumente precisa ser precedida de uma transformação de dados não estruturados em dados estruturados.
Comentário: Para que um dado possa ser analisado, é preciso que ele esteja em algum tipo de formato estruturado, envolvendo metadados, relacionado a algum outro dado ou informação.
Gabarito: C

Análise ad hoc

O processamento de consultas ad hoc no big data traz desafios diferentes daqueles incorridos ao realizar consultas ad hoc em dados estruturados pelo fato de as fontes e formatos dos dados não serem fixos e exigirem mecanismos diferentes para recuperá-los e processá-los.
Embora as consultas ad hoc simples possam ser resolvidas pelos provedores de big data,
na maioria dos casos, elas são complexas porque os dados, algoritmos, formatos e resoluções da entidade devem ser descobertos dinamicamente. O conhecimento dos cientistas de dados e dos usuários corporativos é necessário para definir a análise exigida para as seguintes tarefas:
* Identificar e descobrir os cálculos e algoritmos

* Identificar e descobrir as fontes de dados

* Definir os formatos necessários que podem ser consumidos pelos cálculos

* Executar os cálculos nos dados paralelamente

CAIU

na prova!

4. Ano: 2014 Banca: CESPE Órgão: TJ/SE Cargo: Analista Judiciário -

O processamento de consultas ad hoc em Big Data, devido às características de armazenamento dos dados, utiliza técnicas semelhantes àquelas empregadas em consultas do mesmo tipo em bancos de dados tradicionais.
Comentário: O processamento de consultas ad hoc no big data traz desafios diferentes daqueles incorridos ao realizar consultas ad hoc em dados estruturados pelo fato de as fontes e formatos dos dados não serem fixos e exigirem mecanismos diferentes para recuperá-los e processá-los. Em Big Data, tais consultas serão bem mais complexas e dinâmicas.
Gabarito: E.

PADRÕES DE ACESSO

Existem muitas fontes de dados e formas em que os dados podem ser acessados em uma solução de big data, vejamos as mais comuns:
Web e mídias sociais

A Internet é a fonte de dados que fornece muitos dos insights produzidos atualmente.
A web e a mídia social são úteis em praticamente todas as análises, mas são necessários mecanismos de acesso diferentes para obter esses dados.
A web e a mídia social são a fonte de dados mais complexa de todas em virtude de sua enorme variedade, velocidade e volume. Há aproximadamente de 40 a 50 categorias de websites e cada uma exigirá um tratamento diferente para acessar esses dados.
(gerados por) Dispositivos

O conteúdo gerado por dispositivos inclui dados de sensores. Os dados são detectados a partir das origens de dados, como informações sobre o clima, medições elétricas e dados sobre poluição, e capturados pelos sensores. Os dados podem ser fotos, vídeos, texto e outros formatos binários.
Dados transacionais, operacionais e de Warehouse

É possível armazenar os dados operacionais e transacionais em warehouse existentes para evitar a limpeza ou o arquivamento deles (em virtude de limitações de armazenamento e processamento)ou para reduzir a carga no armazenamento tradicional quando os dados são acessados por outros consumidores.
Os dados transacionais podem ser inseridos no armazenamento de warehouse usando conectores padrão disponibilizados por diversos fornecedores de banco de dados. Opré-processamento de dados transacionais é muito mais fácil, pois a maior parte deles é estruturada. Os processos de extração, transformação e carregamento simples podem ser usados para mover os dados transacionais para o armazenamento em um data warehouse.
PADRÕES DE ARMAZENAMENTO

Os padrões de armazenamento auxiliam a determinar o armazenamento adequado para diversos formatos e tipos de dados. Os dados podem ser armazenados como estão, com relação a pares de valores de chave ou em formatos predefinidos. Vejamos os principais padrões:
Dados não estruturados e distribuídos

A maior parte do big data não é estruturada, já sabemos, e pode conter informações que podem ser extraídas de diferentes formas para diferentes contextos. Na maioria das vezes,os dados não estruturados devem ser armazenados como estão, em seu formato original.
Tais dados podem ser armazenados em sistemas de arquivos distribuídos, como HDFS (Hadoop
Distributed File System), e em armazenamento de documentos NoSQL (Not Only SQL), como o
MongoDB. Esses sistemas fornecem uma maneira eficiente de recuperar dados não estruturados.

Dados estruturados e distribuídos

Os dados estruturados incluem aqueles que chegam da fonte de dados e já estão em um formato estruturado e os dados não estruturados que foram pré-processados. Esses dados convertidos devem ser armazenados para evitar a frequente conversão de dados brutos para dados estruturados.
Tecnologias como BigTable do Google são usadas para armazenar dados estruturados. O
BigTable é um sistema de autogerenciamento tolerante a falhas de grande escala que inclui terabytes de memória e petabytes de armazenamento.
Armazenamento de dados tradicionais

O armazenamento de dados tradicional não é a melhor opção para armazenar big data,
mas nos casos em que as empresas estão realizando a exploração de dados inicial, elas podem optar por usar o data warehouse, o sistema RDBMS (sistemas relacionais) e outros armazenamentos de conteúdo existentes. Esses sistemas de armazenamento existentes podem ser usados para armazenar os dados que são compilados e filtrados usando a plataforma de big data. Os sistemas de armazenamento de dados tradicionais não são adequados para o big data.
Armazenamento na nuvem

Muitos provedores de infraestrutura da nuvem possuem recursos de armazenamento estruturado e não estruturado distribuídos. As tecnologias de big data são um pouco diferentes das perspectivas de configurações, manutenção, gerenciamento de sistemas e programação e modelagem tradicionais. Além disso, as qualificações necessárias para implementar as soluções de big data são raras e caras. As empresas explorando as tecnologias de big data podem usar soluções de nuvem que fornecem o gerenciamento de sistemas, manutenção e armazenamento de big data.
Contudo, não-raro, os dados a serem armazenados são confidenciais, incluindo dados biométricos e registros médicos. A segurança de dados, o compartilhamento de dados, a governança de dados e outras políticas relacionadas aos dados, são aspectos a serem considerados ao ponderar a nuvem como um repositório de armazenamento para big data. A capacidade de transferir enormes quantidades de dados também é outra consideração fundamental para o armazenamento em nuvem.
CAIU

na prova!

5. Ano: 2014 Banca: CESPE Órgão: TJ/SE Prova: Analista Judiciário

Ao utilizar armazenamento dos dados em nuvem, a localização do processamento de aplicações Big Data não influenciará os custos e o tempo de resposta, uma vez que os dados são acessíveis a partir de qualquer lugar.
Comentário: Naturalmente, por envolver transferência de volumes muito grandes de dados, o tempo de resposta das aplicações pode ser afetado. Além disso, ao adotar armazenamento em nuvem, espera-se uma diminuição dos custos de armazenamento, que será feito por um terceiro.
Gabarito: E.

CAIU

na prova!

6. Ano: 2013 Banca: CESPE Órgão: TRE/GO Prova: Técnico Judiciário Área: Administrativa

A Big Data pode ser utilizada na EAD para se entender as preferências e necessidades de aprendizagem dos alunos e, assim, contribuir para soluções mais eficientes de educação mediada por tecnologia.
Comentário: O Big Data poder ser utilizado para melhor conhecer o perfil e o comportamento dos alunos, para que cursos à distância sejam mais eficazes. Este tipo de sentença CESPE(Tal coisa PODE ser utilizada...) só estará errado se estiver escrito algo muito absurdo a seguir. De qualquer forma, sugiro a leitura complementar:
http://convergenciadigital.uol.com.br/cgi/cgilua.exe/sys/start.htm?infoid=37729#.VaLtKvlVh
Bc

Gabarito: C.

MAPA ESTRATÉGICo

Conceitos de Big Data

Volume (tamanho)
Petabytes da dados X
Custo de armazenamento

Variedade (tipo)
Texto estruturado e não estruturado, multimídia,...
Velocidade (speed)
Offline para Online
Performance x Custo

Limitações de tecnologias tradicionais(RSGBD)

r NoSQL/SQL Avançado 1 r MapReduce/MPP

Armazenamento distribuído k Processamento distribuído J
Ferramentas de Big Data /
Tecnologias

(Hadoop, Mongo, HPCC,...)

NoSQL

Começaremos analisando os conceitos e os modelos de dados que dão suporte a bases de dadosNoSQL. Lembrem-se que o foco aqui é entender os conceitos e não a parte técnica do assunto.Alguns nomes técnicos de ferramentas e aplicações que usam esses tipos de modelos de dados serão apresentados, contudo, você não tem necessidade de conhecer nenhuma dessas ferramentas.Vamos em frente!?

CoNCEIToS

Os bancos de dados relacionais foram bem-sucedidos porque trouxeram os benefícios de armazenamento de dados persistentes de forma mais organizada, com controle de concorrência entre as transações. As transações desempenham um papel importante na hora de lidar com os erros, pois é possível fazer uma alteração e, caso ocorra um erro durante seu processamento, pode-se desfazê-la e voltar ao estado anterior.

Embora haja diferenças de um banco de dados relacional para outro os mecanismos principais permanecem os mesmos: os dialetos SQL utilizados por diversos fornecedores são similares, e as transações são realizadas praticamente da mesma forma. Banco de dados relacionais fornecem muitas vantagens, mas não são, de forma alguma, perfeitos. Desde que surgiram, há muita frustração e críticas em relação a seu uso. Vejamos as palavras chaves de uma comparação entreSQL (Relacional) e NoSQL.

Emergente
Maduro

Escalável

Não Relacional
Relacional

Semi-estrturado
Estrtuturado

Sólido

Flexível
Rigido

Consistêncial Eventual
Consistente

Para os desenvolvedores de aplicativos, a maior frustração tem sido a diferença entre o modelo relacional e as estruturas de dados na memória, comumente chamada de incompatibilidade de impedância. Os modelos de dados relacionais organizam os dados em uma estrutura de tabelas e linhas, ou, mais apropriadamente, de relações e tuplas. Uma tupla é um conjunto de pares nome-valor e uma relação é um conjunto de tuplas.

Ao longo dos anos, tornou-se mais fácil lidar com a incompatibilidade de impedância devido à ampla disponibilidade de frameworks de mapeamento objeto-relacional, como Hibernate e iBATIS, que implementam padrões de mapeamento bastante conhecidos. Embora a questão do mapeamento ainda seja controversa dado que os frameworks poupam muito trabalho pesado às pessoas,mas podem se tornar um problema quando estas exageram ao ignorar o banco de dados,comprometendo o desempenho das operações de manipulação de dados sobre a base.

Outro ponto relevante dentro do contexto apareceu devido ao crescimento dos Sistemas
Web. Lidar com o aumento da quantidade de dados e com o tráfego exigiu mais recursos computacionais. Para comportar esse crescimento, há duas opções: ir para cima (crescimento vertical)ou para fora
(horizontal). Ir para cima significa adquirir máquinas maiores, mais processadores, ter maior capacidade de armazenamento em disco e memória. Máquinas maiores, todavia, tornam-se cada vez mais caras, sem mencionar que há limites físicos quanto ao aumento do seu tamanho ou para se escalar verticalmente.
A alternativa seria utilizar mais máquinas menores em um cluster. Um cluster de máquinas pequenas pode utilizar hardware mais acessível e acaba se tornando mais barato para a aplicação. Ele também pode ser mais resiliente. Embora falhas em máquinas individuais sejam comuns, o cluster, como um todo, pode ser criado para continuar funcionando apesar dessas falhas,fornecendo alta confiabilidade.
Duas empresas em particular - Google e Amazon - têm sido influentes no processo de desenvolvimento de rotas alternativas para armazenamento baseado na ideia de clusters.Ambas estiveram à frente na execução de grandes clusters. Além disso, obtiveram quantidades de dados relevantes para testarem e comprovarem seus modelos. Elas eram empresas bem-sucedidas e em crescimento com fortes componentes técnicos, proporcionando-lhes os meios e as oportunidades.
Não é surpresa o fato de que essas empresas tinham em mente acabar com seus bancos de dados relacionais. Quando a década de 2000 chegou, elas produziram artigos concisos, porém altamente influentes, a respeito de seus trabalhos: BigTable (Google) e Dynamo (Amazon).
Os exemplos do BigTable e do Dynamo inspirou a criação de projetos, que faziam experimentações com armazenamentos alternativos de dados, e discussões sobre o assunto haviam se tornado uma parte essencial das melhores conferências sobre software daquela época. O termo "NoSQL"que conhecemos hoje é resultado de uma reunião realizada no dia 11 de junho de 2009, emSão
Francisco - Califórnia, organizada por Johan Oskarsson, um desenvolvedor de software de Londres.
Johan estava interessado em descobrir mais sobre esses novos bancos de dados enquanto estava em São Francisco para um evento sobre Hadoop. Já que dispunha de pouco tempo, achou que não seria viável visitar todas as empresas, de modo que resolveu organizar uma reunião em que todos pudessem estar presentes e apresentar seu trabalho para quem estivesse interessado em conhecê-lo.

A chamada original, NoSQL Meetup, para a reunião pedia por "bancos de dados não relacionais,distribuídos e de código aberto". As palestras lá realizadas versaram sobre Voldemort,
Cassandra,
Dynomite, HBase, Hypertable, CouchDB e MongoDB, mas o termo nunca ficou limitado a esse grupo

Q-Q

original. Não há uma definição genericamente aceita nem uma autoridade para fornecer uma, de modo que tudo o que podemos fazer é discutir algumas características comuns em bancos de dados que tendem a ser chamados de "NoSQL".
As características comuns dos bancos de dados NoSQl são: não utilizam o modelo relacional, tem uma boa execução em clusters, ter código aberto (open source), são criados para suportar propriedades da web do século XXI, e não tem um esquema definido (schema free).
O resultado mais importante do surgimento do NoSQL é a persistência poliglota. Em vez de escolher o banco de dados relacional mais utilizado por todos, precisamos entender a natureza dos dados que estamos armazenando e como queremos manipulá-los. O resultado é que a maioria das organizações terá uma mistura de tecnologias de armazenamento de dados para diferentes circunstâncias. Veja a figura abaixo:
Aplicação Web

MoDELoS DE DADoS

Um modelo de dados é a forma pela qual percebemos e manipulamos nossos dados. Para as pessoas utilizarem um banco de dados precisam de um modelo que descreve a forma pela qual interagimos com os dados desse banco. Embora o termo formal para modelo esteja relacionado a um metamodelo ou uma abstração sobre os dados, quando tratamos de modelos dentro do contexto de NoSQL estamos nos referindo a forma ou o modo pelo qual o gerenciador do banco de dados organiza seus dados.
O modelo de dados dominante nas últimas décadas é o modelo relacional, já falamos bastante sobre ele em uma aula anterior, que pode ser entendido como um conjunto de tabelas. Cada tabela possui linhas e cada linha representa uma entidade de interesse. Descrevemos essa entidade por meio de colunas, cada uma tendo um único valor. Uma coluna pode se referir a outra linha da mesma tabela ou em uma tabela diferente, o que constitui um relacionamento entre essas entidades.
Uma das mudanças mais evidentes trazidas pelo NoSQLé o afastamento do modelo relacional. Cada solução NoSQL possui um modelo diferente, os quais dividimos em quatro categorias amplamente utilizadas no ecossistema NoSQL: chave-valor, documento, família de colunas ou colunar, e grafos.Dessas as três primeiras compartilham uma característica em comum conhecida como
"orientação agregada".
A orientação agregada reconhece que você, frequentemente, deseja trabalhar com dados na forma de unidades que tenham uma estrutura mais complexa do que um conjunto de tuplas. Pode ser útil pensar em termos de um registro complexo que permita que listas e outras estruturas de dados sejam aninhadas dentro dele. Partindo desta ideia é possível agora definir o conceito de agregado.
Um agregado é um conjunto de objetos relacionados que desejamos tratar como uma unidade. Em particular, é uma unidade de manipulação de dados e gerenciamento de consistência.Normalmente, preferimos atualizar agregados como operações atômicas e comunicarmo-nos com nosso armazenamento de dados em termos agregados.
Essa definição corresponde bem ao funcionamento dos bancos de dados chave-valor,
documento e família de colunas. Lidar com agregados facilita muito a execução desses bancos de dados em um cluster, uma vez que o agregado constitui uma unidade natural para replicação e fragmentação.Agregados também são, frequentemente, mais simples de ser manipulados pelos programadores de aplicativos.
Vejam um exemplo de um modelo agregado na figura abaixo. Observem que nestes casos é possível criar uma estrutura hierárquica dentro dos atributos dos objetos. Para fazer isso usamos podemos usar JSON ou XML.
Modelo Agregado

//em cientes
(

"kT:l

"nome" "Marcos",

"endcotxanca": [{"cidade": "Chicago-}]

}

//em pedidos
(

"*d" 99

"idCbente" 1.
"ttensPeddo":[

(

"idProduto":2,
"preço": 35,00,

"produtoNome" "Laptop"

}

L

"endereçoEntrega " [("cdade"Natal"}]
"pagamentoPedido": [

<

"num Cart ao" "1000-1000-1000-1000",

"endCotxançrf':{"cidade" "Natal"}

}

L

}

Vamos agora tratar com um pouco mais de detalhes cada uma das categorias de modelos que apresentamos anteriormente.
MoDELo DE DADoS CHAVE-VALoR

O modelo de dados chave-valor trata o agregado como um todo opaco, o que significa que somente será possível fazer uma pesquisa por chave para o agregado como um todo, não sendo possível executar uma consulta nem recuperar apenas parte do agregado.
Esse é o tipo de banco de dados NoSQL mais simples e permite a visualização do banco de dados como uma grande tabela hash. Conforme falamos acima, o banco de dados é composto por um conjunto de chaves, as quais estão associadas um único valor. A figura abaixo apresenta um exemplo de um banco de dados que armazena informações pessoais no formato chave-valor. A chave representa um campo como o nome, enquanto o valor representa a instância do correspondente.
Chave-Valor

Usuário id nome sobrenome idend
Marcos Silva 5

I 1

2 Leandro Dantas 1

5 Joao Castro 4

4 Junior Ferraz 2

Key Value

"nome: Marcos, sobrenome: Silva, cidade: São Paulo, estado: SP.cep: 66745-025"

Exemplos: Redis, DynamoDB, Riak

Este modelo, por ser de fácil compreensão e implementação, permite que os dados sejam rapidamente acessados pela chave, principalmente em sistemas que possuem alta escalabilidade,contribuindo para aumentar a disponibilidade de acesso aos dados. As operações disponíveis para manipulação de dados são bem simples, como get() e set(), que permitem retornar e capturar valores, respectivamente. A desvantagem deste modelo é que não permite a recuperação de objetos por meio de consultas mais complexas.
Como exemplo de banco de dados NoSQL que adota o modelo chave-valor podemos destacar o
DynamoDB, o qual foi desenvolvido pela Amazon. Dentre as principais funcionalidades do
Dynamo temos a possibilidade de realizar particionamento, replicação e versionamento dos dados.
Além do Dynamo, outras soluções NoSQL seguem o mesmo conceito de chave-valor: Redis,
Riak e

GenieDB.

MoDELo DE DADoS DE DoCUMENTo

O modelo de documentos torna o agregado transparente para o banco de dados, permitindo que sejam executadas consultas e recuperações parciais. Entretanto, pelo fato de o documento não possuir esquema, o banco de dados não pode atuar muito na estrutura desse documento para otimizar o armazenamento e a recuperação de partes do agregado.
Um documento, em geral, é um objeto com um identificador único e um conjunto de campos, que podem ser strings, listas ou documentos aninhados. Estes campos se assemelham a estrutura chave-valor, que cria uma única tabela hash para todo o banco de dados. No modelo orientado a documentos temos um conjunto de documentos e em cada documento temos um conjunto de campos (chaves) e o valor deste campo.
Outra característica importante é que este modelo não depende de um esquema rígido, ou seja, não exige uma estrutura fixa como ocorre nos bancos de dados relacionais. Assim, é possível que ocorra uma atualização na estrutura do documento, com a adição de novos campos, por exemplo,sem causar problemas no banco de dados.
Na figura a seguir temos um exemplo de documento representado por um banco de dados de fornecedor (supplier) que tem os campos ID, Name, Address e Order. Para cada um desses campos temos os valores associados. Vejam que o atributo order aponta para outro documento.
Como principais soluções que adotam o modelo orientado a documentos destacamos o
CouchDB e o MongoDB. CouchDB utiliza o formato JSON e é implementado em Java, além disso permite replicação e consistência. O MongoDB foi implementado em C++ e permite tanto concorrência como replicação.
MoDELo CoLUNAR

Modelos de famílias de colunas dividem o agregado em famílias de colunas, permitindo ao banco de dados tratá-las como unidades de dados dentro do agregado da linha. Isso impõe alguma estrutura ao agregado, mas também permite que o banco de dados aproveite a estrutura para melhorar sua acessibilidade.
Vejam que neste caso, mudamos o paradigma em relação ao modelo chave-valor. A
orientação deixa de ser por registros ou tuplas para orientação por colunas. Neste modelo os dados são indexados por uma trilha (linha, coluna e timestamp), onde as linhas e colunas são identificadas por chaves e o timestamp permite diferenciar múltiplas versões de um mesmo dado.
Usuário Endereço

1 nome sobrenome cidade estado cepMarcos Silva Sâo Paulo SP
66745-025

Vale ressaltar que operações de leitura e escrita são atômicas, ou seja, todos os valores associados a uma linha são considerados na execução destas operações, independentemente das colunas que estão sendo lidas ou escritas. Outro conceito associado ao modelo é o de família de colunas (column family), que é usado com o intuito de agrupar colunas que armazenam o mesmo tipo de dados.
Observem abaixo o que geralmente acontece na prática em banco de dados colunar. Neste caso as colunas das tabelas são serializadas e armazenadas em disco.
Este modelo de dados surgiu com o BigTable do Google, por isso é comum falar sobre o modelo de dados BigTable. Dentre as características deste modelo temos a possibilidade de particionamento dos dados, além de oferecer forte consistência, mas não garante alta disponibilidade. Outras soluções sugiram após o BigTable, dentre elas o Cassandra, desenvolvido pelo Facebook.Temos também o Hbase, que é um banco de dados open source semelhante ao BigTable, que utiliza oHadoop.

MoDELo DE GRAFoS

Bancos de dados de grafos são motivados por uma frustração diferente com banco de dados relacionais e, por isso, têm um modelo oposto - registros pequenos com interconexões complexas.A ideia desse modelo é representar os dados e/ou o esquema dos dados como grafos dirigidos, ou como estruturas que generalizem a noção de grafos.
O modelo de grafos é mais interessante que outros quando informações sobre a interconectividade ou a topologia dos dados são mais ou tão importantes quantos os dados propriamente ditos. Omodelo orientado a grafos possui três componentes básicos: os nós (são os vértices do grafo), os relacionamentos (são as arestas) e as propriedades (ou atributos) dos nós e relacionamentos.
Neste caso, o banco de dados pode ser visto como um multigrafo rotulado e direcionado, onde cada par de nós pode ser conectado por mais de uma aresta. Um exemplo pode ser: "Quais cidades foram visitadas anteriormente (seja residindo ou viajando) por pessoas que viajaram para o Rio deJaneiro?".

No modelo relacional esta consulta poderia ser muito complexa devido a necessidade de múltiplas junções, o que poderia acarretar uma diminuição no desempenho da aplicação. Porém, por meio dos relacionamentos inerentes aos grafos, estas consultas tornam-se mais simples e diretas.
Usuário id nome sobrenome id endMarcos Silva h 3 1
2 Leandro Dantas 1

3 Joao Castro 4

4 Junior Ferraz 2

Endereço id cidade estado cep
1 Belém PA 66823-010

2 Goiânia GO 66625-640

Sào Paulo SP 66745-025 |

I3

4 Salvador BA 66548-020

Vértice Vértice nome: Marcos sobrenome: Silva"
cidade: Sao Paulo estado: 'SP'cep:"66745-025"

Exemplos: Neo4J, Infinite Graph, InforGrid

Alguns bancos que utilizam esse padrão são: Neo4J, Infinite Graph, InfoGrid,
HyperGraphDB. Vejam a figura abaixo que apresenta duas características relacionadas aos bancos de dados de grafos: o processamento e o armazenamento nativo.
Microsoft

-£^nentDB'

Neo4j the graph databasc
/AmFnimrrrir!cVi

InfiniteGraph

The Graph
Database Space

Graph Storage

AllegroGraph

?CFW8

Native

CoNSIDERAçõES FINAIS SoBRE MoDELoS

Bancos de dados orientados a agregados tornam os relacionamentos entre agregados mais difíceis de lidar do que relacionamentos intra-agregados.
Bancos de dados sem esquema permitem que campos sejam adicionados livremente aos registros,mas geralmente há um esquema implícito esperado pelos usuários dos dados.

Banco de dados orientados a agregados, muitas vezes, criam visões materializadas para fornecer dados organizados de um modo diferente de seus agregados primários. Isso,muitas vezes, é realizado com computação MapReduce.
Outro ponto importante é saber associar cada categoria dos modelos de dados aos seus respectivos representantes ou principais referências. Veja nas figuras a seguir essa lista de forma organizada.
4 I I

Product
ID

Type

Schema is defined per iteX

Redis

1 BookID Odyssey Homer 187

2 Album ID 6 Partitas Bach

Album ID:

TracklD

Partita

No. 1

Drama, J

Amazon aipazotf DynamoDB
websew

3 MovielD TheKid

Comedy /

WACLÉX Oracle

, BERKELEYDBj BerkeleyBD

MongoDB

CouchDB

Azure
DocumentDB

^TiTAh Titan

FoRMAS DE DISTRIBUIçÃo

Há dois estilos de distribuição de dados: a replicação e a fragmentação. A
fragmentação distribui dados diferentes em múltiplos servidores, de modo que cada servidor atue como a única fonte de um subconjunto de dados. A replicação copia os dados para servidores distintos, de modo que cada parte dos dados pode ser encontrada em múltiplos lugares. Um sistema pode utilizar ambas as técnicas.
A replicação mestre-escravo torna um nodo a cópia oficial, a qual lida com gravações,
enquanto os escravos sincronizam-se com o mestre e podem lidar com as leituras. A replicação ponto a ponto permite gravações em qualquer nodo; os nodos são coordenados para sincronizar suas cópias de dados. A replicação mestre-escravo reduz a chance de conflitos de atualização, mas a ponto a ponto evita carregar todas as gravações em um único ponto de falha.
TEoREMA CAP

No mundo NoSQL, é comum referimo-nos ao teorema CAP como o motivo pelo qual pode-se precisar relaxar a consistência. Ele foi proposto originalmente por Eric Brewer em 2000, e recebeu uma prova formal de Seth Gilbert e Nancy Lynch alguns anos depois. É possível ouvir referências aos termos como conjectura de Brewer.
A declaração do teorema CAP é que, dadas as três propriedades de Consistência, Disponibilidade e de Tolerância a partições, somente é possível obter duas delas. A sigla vem do nome dessas propriedades em inglês: Consistency, Availability, e Partition tolerance. Logicamente, a existência do teorema vai depender de como são definidas cada uma dessas propriedades. Vejamos então a definição de cada uma delas. Antes vejam a figura abaixo o diagrama de Van que representa o relacionamento entre as três propriedades.
consistency

C+A

availability

C+A+P not possible
C+P A+P

partition tolerance
A consistência refere-se ao fato de que uma leitura em qualquer um dos nodos de um sistema retorna como resultado a mesma informação. Vejam a figura abaixo:
Peer A

id amount

1 21

2 32

3 49

| id amount 1

1 21

2 32

3 49

read id 3 = 49
A disponibilidade trata do fato das requisições de leitura e escrita sempre serão reconhecidas e respondidas sobre a forma de sucesso ou falha. Desta forma, toda solicitação recebida por um nodo que não esteja no estado de falha deve resultar em uma resposta.
A tolerância a partições significa que o cluster pode suportar falhas na comunicação que o dividam em múltiplas partições incapazes de se comunicar entre si, essa situação é conhecida como divisão cerebral (split brain).
Observe na figura a seguir um exemplo de disponibilidade e tolerância a partições.
Veja que a partição B não possui os dados referentes ao id 3 e recebe uma mensagem de erros no caso de uma partição.
Partition A

Peer A

User A

amount = 68

Partition B

update amoun id 3 = 82
operation failed

ACID X BASE

ACID é um princípio de design de banco de dados relacionado ao gerenciamento de transações. Éum acrônimo que significa: Atomicidade, Consistência, Isolamento e Durabilidade.

ACID é um estilo de gerenciamento de transações que utiliza controles de simultaneidade pessimista para garantir que a consistência seja mantida através da aplicação de bloqueios de registo. ACID é a abordagem tradicional de gerenciamento de transações de banco de dados, uma vez que é aproveitada pelos sistemas de gerenciamento de banco de dados relacionais.
Quando olhamos para o teorema CAP, os bancos de dados relacionais estão associados à priorização das propriedades de Consistência e Disponibilidade.
O Modelo BASE (Basically Avaliable, Soft State, Eventual Consistency), foi sugerido como contraposição ao ACID. O ACID é pessimista e força a consistência no final de cada operação,enquanto o modelo BASE é otimista e aceita que a consistência no banco de dados estará em um estado de fluxo, ou seja, não ocorrerá no mesmo instante, gerando uma "fila" de consistência de posterior execução.
A disponibilidade do Modelo BASE é garantida tolerando falhas parciais no sistema, sem que o sistema todo falhe. Por exemplo, se um banco de dados está particionado em cinco nós e um deles falha, apenas os clientes que acessam aquele nó serão prejudicados, pois o sistema como todo não cessará seu funcionamento.
A consistência pode ser relaxada permitindo que a persistência no banco de dados não seja efetivada em tempo real (ou seja, logo depois de realizada uma operação sobre o banco). PeloACID, quando uma operação é realizada no SGBD, ela só será finalizada se houver a certeza de que a persistência dos dados foi realizada no mesmo momento, fato que é derivado da propriedade da durabilidade.
Já no BASE isso não se confirma. Para garantir a disponibilidade, algumas etapas são dissociadas à operação requisitada, sendo executadas posteriormente. O cliente realiza uma operação no banco de dados e, não necessariamente, a persistência será efetivada naquele instante. OModelo BASE
pode elevar o sistema a níveis de escalabilidade que não podem ser obtidos com ACID.

No entanto, algumas aplicações necessitam que a consistência seja precisamente empregada.Nenhuma aplicação bancária poderá colocar em risco operações de saque, depósito,
transferência,
etc. O projetista do banco de dados deverá estar ciente de que se utilizar o
Modelo BASE ganhará disponibilidade em troca de consistência, o que pode afetar os usuários da aplicação referente ao banco de dados.
Quando um banco de dados suporta BASE, favorece a disponibilidade sobre a consistência.
Em outras palavras, a base de dados é A + P a partir de uma perspectiva de teorema CAP. Em essência,BASE aproveita concorrência otimista, relaxando restrições fortes de consistência determinadas pelas propriedades ACID.
Se um banco de dados é basicamente disponível, esse banco de dados sempre dará conhecimento ao pedido de um cliente, quer sob a forma dos dados solicitados ou de uma notificação de sucesso/fracasso. Na figura abaixo, o banco de dados é basicamente disponível, mesmo que tenha sido particionado como um resultado de uma falha de rede.
DBMS

Partition A
Peer A

Partition B

id amount

1 37

2 42

3 18

Softstate significa que um banco de dados pode estar em um estado inconsistente quando os dados são lidos. Assim, os resultados podem mudar se os mesmos dados forem solicitados novamente.Isso ocorre porque os dados podem ser atualizados para a consistência, mesmo que nenhum usuário tenha escrito no banco de dados entre duas leituras. Esta propriedade está intimamente relacionada com a consistência eventual.
Na figura abaixo, 1. Um usuário atualiza um registro no peer A. 2. Antes dos outros peers serem atualizados, o usuário B solicita o mesmo registro do peer C. 3. A base de dados está agora em um estado soft, e dados obsoletos são devolvido ao usuário B.
Peer A

User A

update amoi/t
Consistência eventual é o estado em que leituras feitas por diferentes clientes,
imediatamente após a gravação para o banco de dados, podem não retornar resultados consistentes. O banco de dados só alcança a consistência uma vez que as mudanças foram propagadas para todos os nós.Embora a base de dados esteja em processo para atingir o estado de consistência, estaremos em um estado soft.
Na figura a seguir: 1. Um usuário atualiza um registro. 2. O registro só fica atualizado no peer A, mas antes que os outros pares possam ser atualizados, o usuário B solicita o mesmo registro. 3. A base de dados está agora em um estado soft, dados obsoletos são retornados para o usuário B do Peer C.
4. No entanto, a consistência é eventualmente atingida, e usuário C recebe o valor correto.

DBMS

Peer A

BASE enfatiza disponibilidade imediata em relação à consistência, em contraste com o
ACID, que garante a consistência imediata à custa de disponibilidade devido a bloqueio de registo. Esta abordagem soft para a consistência permite que as bases de dados compatíveis com BASE possam servir a múltiplos clientes sem qualquer latência embora servindo resultados inconsistentes. No entanto, as bases de dados compatíveis com BASE não são úteis para sistemas transacionais onde a falta de consistência é uma preocupação.
MAPREDUCE

MapReduce é um padrão que permite que operações computacionais sejam realizadas em um cluster. A tarefa de mapeamento lê dados de um agregado e os agrupa em partes chave-valor relevante. Mapeamentos somente leem um único registro de cada vez e podem,assim, ser paralelizados e executados no nodo que armazena o registro.
A tarefa de redução recebe muitos valores de uma única chave de saída, a partir da tarefa de mapeamento, e os resume em uma única saída. Cada redutora trabalha sobre o resultado de uma única chave, de modo que podem ser paralelizados por chave.
MapReduce é complicado de entender no início, por isso vamos tentar compreendê-lo com um exemplo simples. Vamos supor que temos um arquivo que tem algumas palavras e o arquivo é dividido em blocos, e temos que contar o número de ocorrências de uma palavra no arquivo. Iremos passo a passo para alcançar o resultado usando a funcionalidade MapReduce. Todo o processo é ilustrado no diagrama a seguir:
Elementos que tenham o mesmo formato de entrada e saída podem ser combinadas em pipelines.Isso melhora o paralelismo e reduz a quantidade de dados a serem transferidos.
Operações de
MapReduce podem ser compostas em pipelines, nos quais a saída de uma redução é a entrada do mapeamento de outra operação.
Se o resultado de uma computação MapReduce for amplamente utilizado, pode ser armazenado como uma visão materializada. Visões materializadas podem ser atualizadas por meio de operaçõesMapReduce que apenas computem alterações na visão, em vez de computar novamente tudo desde o início.
HADooP

Hadoop é um framework de código aberto para armazenamento de dados em grande escala e processamento de dados que seja compatível com o hardware específico. O frameworkHadoop se estabeleceu como uma plataforma da indústria de fato para soluções de Big Data contemporâneas.Ele pode ser usado como um motor de ETL ou como um mecanismo de análise para o processamento de grandes quantidades de dados estruturados, semiestruturados e não estruturados. Apartir de uma perspectiva de análise, Hadoop implementa a estrutura de processamento de MapReduce.A
figura abaixo ilustra algumas das características do Hadoop.

Hadoop textual data structured data
XML

data processing storage I
Hadoop é usado amplamente na indústria para processamento de grande escala, massivamente paralelo e distribuído. Hadoop é altamente tolerante a falhas e configurável para tantos níveis quanto precisarmos. O que tem um impacto direto no número de vezes que os dados são armazenados.
Como já abordado, em sistemas de Big Data, a arquitetura gira em torno de dois componentes principais: a computação distribuída e processamento paralelo. No Hadoop, a computação distribuída é tratada por meio do HDFS e processamento paralelo é tratado peloMapReduce. Em suma, podemos dizer que o Hadoop é uma combinação de HDFS e MapReduce, como mostrado na imagem a seguir:
Store Process

Hadoop = HDFS + MapReduce

Hadoop tem uma série de vantagens, e algumas delas são:

Baixo custo - Funciona em hardware simples (commodity): Hadoop pode ser executado em hardware simples e não requer um sistema de alto desempenho, o que pode ajudar no controle de custos e, mesmo assim, alcançar escalabilidade e desempenho. Adicionar ou remover nós do cluster é simples. O custo por terabyte é mais baixo para armazenamento e processamento no Hadoop.
Flexibilidade de armazenamento: Hadoop pode armazenar dados em formato plano (raw) em um ambiente distribuído. Hadoop pode processar os dados não estruturados e dados semiestruturados melhor que a maioria das tecnologias disponíveis.
Comunidade de código aberto: Hadoop é de código aberto e apoiado por muitos contribuintes com uma crescente rede de desenvolvedores em todo o mundo. Muitas organizações, tais comoYahoo,
Facebook, Hortonworks, e outros têm contribuído imensamente para o progresso do
Hadoop e outros subprojetos relacionados.
Tolerante a falhas: Hadoop é altamente escalável e tolerante a falhas. Hadoop é confiável em termos de disponibilidade de dados, e até mesmo se alguns nós falharem, Hadoop pode recuperar os dados. A arquitetura assume que os nós podem falhar e o sistema deve ser capaz de continuar a processar os dados.
Análise de dados complexos: Com o surgimento de Big Data, a ciência de dados também tem crescido aos trancos e barrancos, e nós temos de algoritmos intensivos complexos e pesados para análise de dados. Hadoop pode processar tais algoritmos para um conjunto de dados muito grande.
Alguns exemplos onde o Hadoop pode ser utilizado são os seguintes: pesquisa ou mineração de texto, processamento de registros, sistemas de recomendação, inteligência de negócios,análise de vídeo e imagem, reconhecimento de padrões, avaliação de risco e análise de sentimentos.
O ECOSSISTEMA DO HADOOP

O ecossistema Hadoop é composto por uma série de subprojetos e podemos configurar esses projetos conforme precisamos em um cluster Hadoop. Como Hadoop é um software de código aberto, vemos um monte de contribuições e melhorias do Hadoop feitas por diferentes organizações. Todos os utilitários são absolutamente úteis e ajudam na gestão do sistema de forma mais eficiente. Para simplificar, vamos entender as diferentes ferramentas, categorizando-as.
A figura abaixo mostra as camadas e as ferramentas e utilitários dentro dessas camadas, no ecossistema Hadoop:
No Hadoop, sabemos que os dados são armazenados em um ambiente de computação distribuída,de modo que os arquivos estão espalhados por todo o cluster. Devemos ter um sistema de arquivos eficiente para gerenciar os arquivos no Hadoop. O sistema de arquivos usado em Hadoop é o HDFS,sigla para Hadoop Distributed File System.

O HDFS é extremamente escalável e tolerante a falhas. Ele é projetado para processar de forma eficiente de forma paralela em ambiente distribuído no mesmo hardware simples(commodity).
HDFS tem processos daemon em Hadoop, que gerenciam os dados. Os processos são NameNode,
DataNode, BackupNode, e Checkpoint NameNode.

Programação distribuída

Para aproveitar o poder de um sistema de arquivos de armazenamento distribuído, Hadoop utiliza programação distribuída que pode fazer programação paralela massiva. A programação distribuída é o coração de qualquer sistema de Big Data, por isso é extremamente crítica. Aseguir estão os diferentes frameworks que podem ser usados para a programação distribuída: MapReduce,Hive,
Pig e Spark.

A camada de base em Hadoop para a programação distribuída é MapReduce. Se você observar a figura os outros frameworks rodam em cima do MapReduce.
Hadoop MapReduce: MapReduce é o coração do sistema Hadoop de programação distribuída.MapReduce é projetado como processamento paralelo em um ambiente distribuído.
Hadoop
MapReduce foi inspirado pelo artigo do Google MapReduce. Hadoop MapReduce possui uma estrutura de processamento escalável e massivamente paralela, que pode trabalhar com BigData e é projetado para ser executado em um cluster de hardware commodity.
Antes do Hadoop 2.x, MapReduce era a única estrutura de processamento que podia ser usada para a execução. Nas versões mais recentes, esse utilitário foi ampliado e se criou um wrapper para uma programação mais fácil que torna o desenvolvimento mais rápido.
Apache Hive: Hive fornece uma infraestrutura de sistemas de data warehouse para Hadoop,
ele cria uma interface de wrapper SQL chamada HiveQL, em cima do MapReduce. Hive pode ser usado para executar algumas consultas ad hoc, agregações básicas e processamento de sumarizações com os dados do Hadoop. HiveQL não é compatível com SQL92. Hive foi desenvolvido peloFacebook e foi doado para o Apache. Hive é projetado em cima do MapReduce, o que significa uma consulta HiveQLvai executar os trabalhos usando MapReduce para o processamento da consulta.
Podemos até mesmo estender HiveQL usando User Defined Functions (UDF).
Apache Pig: Pig fornece um invólucro baseado em script escrito na linguagem
Pig Latin para processar os dados com uma sintaxe script-like. Pig foi desenvolvido pelo Yahoo e foi doado para oApache. Pig, também traduz o código de script Pig Latin para MapReduce e executa o trabalho. Pig é normalmente utilizado para analisar conjuntos de dados semiestruturados e grandes.
Apache Spark: Oferece uma alternativa poderosa para o MapReduce do Hadoop. Apache Spark é um framework de processamento de dados paralelo que pode executar programas em até 100vezes mais rápido do que o Hadoop MapReduce na memória, ou 10 vezes mais rápido no disco.Spark é utilizado para o processamento de fluxo em tempo real e análise dos dados.
Bancos de dados NoSQL

Nós já discutimos sobre NoSQL como um dos sistemas emergentes e amplamente adotados.
Dentro ecossistema do Hadoop, temos um banco de dados NoSQL chamado HBase. HBase é um dos componentes chave que fornece um design flexível e alto volume de operações de leitura e escritas simultâneas com baixa latência, portanto, é amplamente adotado.
HBase é inspirado no BigTable do Google. HBase é um mapa ordenado, que é esparso,
consistente,
distribuído e multidimensional. HBase é um banco de dados NoSQL, orientado coluna e chave-valor,que funciona no topo do HDFS. HBase fornece um lookup mais rápido e também um alto volume de inserções e atualizações de acesso aleatório em uma escala elevada. O esquema HBase é muito flexível e realmente variável, onde as colunas podem ser adicionadas ou removidas em tempo de execução. HBase suporta baixa latência e operações de gravação e leitura fortemente consistentes.É apropriado para agregação de alta velocidade. Muitas organizações ou empresas usam
HBase, tais como Yahoo, Adobe, Facebook, Twitter, Stumblellpon, NGData, Infolinks, TrendMicro, e muitos mais.
INGESTÃo DE DADoS

O gerenciamento de dados em big data é um aspecto importante e crítico. Temos de importar e exportar dados em grande escala para fazer o processamento, o que pode se tornar incontrolável no ambiente de produção.
No Hadoop, lidamos com um conjunto diferente de fontes, tais como batch, streaming,
dados em tempo real, e fontes de dados que são complexos do ponto de vista de formatos,alguns são semiestruturadas e não estruturadas. A gestão de tais dados é muito difícil, por isso temos algumas ferramentas para gerenciamento de dados, como Flume, Sqoop, Kafka, NiFi e Storm. Alguns deles podem ser visualizados na figura abaixo.
Observe primeiramente que cada ferramenta atual sobre um tipo de estrutura de dados ou de armazenamento diferente. Desta forma, quando estiver estudando sobre o assunto procure entender qual a fonte de dados de leitura/escrita de cada uma destas ferramentas.Vejamos as principais delas.
Apache Flume: Apache Flume é uma ferramenta amplamente utilizada para coleta eficiente,agregação e movimentação de grandes quantidades de dados de muitas fontes diferentes para um armazenamento de dados centralizado. Flume é um sistema distribuído, confiável e disponível. Ele executa bem se uma fonte está fornecendo streaming.
O flume, pode ser visto como uma ferramenta para ingestão de alto volume no Hadoop de dados baseados em eventos. Por exemplo, coletar arquivos de log de um banco de servidores da Web e,em seguida, mover os eventos de log desses arquivos para o HDFS (fluxo de cliques).

O objetivo principal do Flume é ingerir dados de eventos no HDFS (Hadoop Distributed
File System)
de forma simples e automatizada. Porém, seu uso não se limita apenas ao HDFS, é possível enviar também dados para um arquivo ou banco de dados, entre outros.
Seu funcionamento é orientado a agentes. Um agente Flume roda na JVM (Java Virtual
Machine) e possui os seguintes componentes:
* Source: responsável pela entrada de dados.

* Channel: armazena os dados que passam do source para o sink. Seu comportamento é parecido com uma fila.
* Sink: responsável por enviar os dados ao destino/saída. A saída pode ser outro agente Flume.
filesystem

A configuração de um agente é feita por meio de um arquivo local que tem o formato de um arquivo properties utilizado em Java. Veja um exemplo de arquivo de configuração e seus respectivos componentes possíveis na figura abaixo:
agentl.sources = sourcel agentl.sinks = sinkl agentl.channels = channell agentl.sources.sourcel.channels = channell agentl.sinks.sinkl.channel = channell agentl.sources.sourcel.type = spooldir agentl.sources.sourcel.spoolDir = /var/spooldir agentl.sinks.sinkl.type = hdfs agentl.sinks.sinkl.hdfs.path = hdfs://hostname:8020/user/flume/logs agentl.sinks.sinkl.hdfs.filetype = DataStream agentl.channels.channell.type = memory agentl.channels.channell.capacity = 10000
agentl.channels.channell.transactionCapacity = 100

flume-ng agent —name agentl -conf $FLUME_HOME/conf

Category

Source

Sink

Channel

Component

Avro
Exec

HTTP
JMS

Netcat

Sequence generator
Spooling directory
Syslog

Thrift
Twitter
Avro

Elasticsearch

File roll
HBase
HDFS

IRC

Logger

Morphline (Solr)
Null

Thrift
File
JDBC

Memory

Apache Sqoop: 0 Sqoop pode ser usado para gerenciar dados entre sistemas NoSQL Hadoop e bancos de dados relacionais ou data warehouses corporativos. Sqoop tem diferentes conectores com os respectivos dados armazenados e utilizando esses conectores, Sqoop pode importar e exportar dados em MapReduce, e ainda importar e exportar dados no modo paralelo. Sqoop também é tolerante a falhas.
O Sqoop agenda as tarefas de map reduce jobs para efetivar os imports and exports.
Ele sempre requer um conector e o driver JDBC. Cada driver JDBC serve a um servidor de banco de dados específico, estes drivers devem ser copiados para /usr/lib/sqoop/lib. Para executar uma operação com o Scoop você deve fazer uso de um comando semelhantes ao descrito abaixo:
Sqoop TOOL PROPERTY_ARGS SQOOP_ARGS

A estrutura da linha de comando tem é composta dos seguintes termos:

* TOOL: indica a operação que você deseja executar, por exemplo, import e export.

* PROPERTY_ARGS - conjunto de parâmetros que são inseridos como propriedades
Java no formato -Dname=value.

* SQOOP_ARGS - todos os vários parâmetros sqoop.

Vejamos um exemplo:

EXEMPLO:

sqoop import \

—connect jdbc:oracle:thin:@devdbll-s.concurso.ch:10121/devdbll_s.concurso.ch \

—username hadoop_tutorial \

-P \

—num-mappers 1 \

—target-dir visitcount rfidlog \

—table VISITCOUNT.RFIDLOG

NiFi 1.3.0: Criado para automatizar o fluxo de dados entre os sistemas. Com essa ferramenta o fluxo automatizado e gerenciado de informações entre sistemas. Esse espaço problemático existe desde que as empresas tinham mais de um sistema, onde alguns dos sistemas criavam dados e alguns dos sistemas consumiam dados.
Os conceitos fundamentais de projeto da NiFi estão intimamente relacionados às principais ideias da Programação Baseada em Fluxo [fbp]. Apresentaremos alguns dos principais conceitos doNiFi e como eles são mapeados para o FBP.
NiFi Term FBP Term Descrição

FlowFile Information
Packet

Um FlowFile representa cada objeto que se move através do sistema, NiFi acompanha um mapa de cadeias de atributos em pares de chave/valor e seu conteúdo associado de zero ou mais bytes.
FlowFile Processor Black Box Os processadores realmente executam o trabalho. Ele faz alguma combinação de roteamento de dados, transformação ou mediação entre sistemas. Têm acesso aos atributos de um determinado FlowFile e seu fluxo de conteúdo (content stream). Processadores podem operar em zero ou mais FlowFiles em uma determinada unidade de trabalho e confirmar ou reverter esse trabalho.
Connection Bounded Buffer Conexões fornecem a ligação real entre processadores. Eles atuam como filas e permitem que vários processos interajam a taxas diferentes. Essas filas podem ser priorizadas dinamicamente e podem ter limites superiores na carga.
Flow Controller Scheduler O Controlador de Fluxo mantém o conhecimento, de como os processos se conectam e gerencia os encadeamentos e alocações que todos os processos usam. O Controlador de Fluxo age como o intermediário, facilitando a troca deFlowFiles entre processadores.

Process Group subnet Um grupo de processos é um conjunto específico de processos e suas conexões,
que podem receber dados por meio de portas de entrada e enviar dados por meio de portas de saída. Dessa maneira, os grupos de processos permitem a criação de componentes inteiramente novos simplesmente pela composição de outros componentes.
O NiFi é executado dentro de uma JVM em um sistema operacional host. Os componentes principais do NiFi na JVM são os seguintes:
Servidor web: O objetivo do servidor da Web é hospedar a API de comando e controle baseada emHTTP do NiFi.

Controlador de Fluxo: O controlador de fluxo é o cérebro da operação. Ele fornece encadeamentos para que as extensões sejam executadas e gerencia o planejamento de quando as extensões recebem recursos a serem executados.
Extensões: Existem vários tipos de extensões NiFi descritas em outros documentos. O
ponto chave aqui é que as extensões operam e executam dentro da JVM.
Repositório FlowFíle: O Repositório do FlowFile é onde o NiFi acompanha o estado do que sabe sobre um determinado FlowFile que está atualmente ativo no fluxo. A implementação do repositório é conectável. A abordagem padrão é um log Write-Ahead persistente localizado em uma partição de disco especificada.
Repositório de Conteúdo: O Repositório de Conteúdo é onde os bytes de conteúdo reais de um determinado FlowFile estão ativos. A implementação do repositório é conectável.A abordagem padrão é um mecanismo bastante simples, que armazena blocos de dados no sistema de arquivos.É possível especificar mais de um local de armazenamento do sistema de arquivos para obter partições físicas diferentes ativadas para reduzir a contenção em qualquer volume individual.
Repositório de Proveniência: O Repositório de Proveniência é o local onde todos os dados de eventos de proveniência são armazenados. A construção do repositório é conectável, sendo a implementação padrão usada para usar um ou mais volumes de disco físico. Dentro de cada local,os dados do evento são indexados e pesquisáveis.

Vejamos esses componentes na figura abaixo:

NiFi também é capaz de operar dentro de um cluster. Neste caso, cada nó em um cluster NiFi executa as mesmas tarefas nos dados, mas, cada um opera em um conjunto diferente de dados. OApache
ZooKeeper elege um único nó como o Coordenador de Cluster, e o failover é tratado automaticamente pelo ZooKeeper.
Todos os nós do cluster relatam informações de status ao Coordenador de Cluster. O
Coordenador de Cluster é responsável por desconectar e conectar nós. Além disso, todo cluster tem um NóPrimário, também eleito pelo ZooKeeper. Como gerente do DataFlow, você pode interagir com o cluster NiFi por meio da interface do usuário (UI) de qualquer nó. Qualquer alteração feita é replicada para todos os nós no cluster, permitindo vários pontos de entrada. Veja está configuração na figura abaixo:
ZooKeeper Server

* Cluster Coordinator

* Primary Node
ZooKeeper Client

KAFKA: O Apache Kafka é uma plataforma de transmissão de dados distribuída, semelhante a uma fila de mensagens ou um sistema de mensagens corporativo. Foi desenvolvido para providenciar,em tempo real, um fluxo de dados com baixa latência e uma alta taxa de transferência, tendo como principal objetivo a construção de ligações de transmissão de dados entre sistemas para obtenção dos mesmos.
Thiago Cavalcanti)

Funciona como um cluster em um ou mais servidores, guardando o registo da transmissão de dados em categorias chamados de Tópicos. A estrutura do Kafka consiste ainda de Brokers,Partições,
Líderes e Réplicas, estas são as principais palavras chave no funcionamento do Kafka.

Um Tópico é uma categoria ou um nome dum fluxo em que os registos são publicados,
isto significa que cada tópico tem informações diferentes uns dos outros, e o Kafka mantém uma ordem dentro do tópico, mas não entre tópicos. Os Tópicos estão divididos num número de partições que permitem paralelizar um tópico, dividindo os dados num tópico em particular através de múltiplosBrokers.

Um Broker por outro lado é responsável por gerir e replicar mensagens que entram no cluster doKafka, mantendo um número de partições. Cada partição tanto pode ser um Líder ou uma
Réplica para um Tópico. Processos de escrita e leitura passam por um Líder e o mesmo coordena e atualiza as Réplicas com a nova informação. Se um Líder falha, uma Réplica fica no seu lugar como novoLíder. Veja essa estrutura na figura abaixo.

Na figura apareceu ainda dois papeis, produtores e consumidores, vamos falar um pouco sobre cada um deles:
* Produtor: tem a principal função de introduzir as mensagens para os Tópicos do
Kafka, permitindo às aplicações publicar fluxos de registos. Escreve para um só
Líder, providenciando uma produção balanceada de carregamento para que cada processo de escrita possa ser servido por um Broker e uma máquina em separado.
* Consumidor: retira mensagens de um Tópico Kafka, permitindo que as aplicações subscrevam ao mesmo tópico e processem o fluxo de registos. Lê de uma só partição dando a opção de escalar através do consumo de mensagens num estilo similar a uma produção de mensagens. Pode também ser organizado em forma de grupo de consumidores para um dado tópico, cada consumidor dentro do grupo lê duma única partição e o grupo como um todo consome todas a mensagens do tópico inteiro.
Apache Storm: Apache Storm fornece uma solução em tempo real, escalável e distribuída para streaming de dados. Storm permite atividades orientadas a dados e automatizadas. Pode ser utilizado com qualquer linguagem de programação e garante que os fluxos de dados são processados sem perda de dados. Storm possui tipagem de dados agnóstica, ou seja, ele processa fluxos de dados de qualquer tipo.
OUTRoS CoMPoNENTES Do HADooP

Vamos voltar agora a analisar os componentes do Hadoop focando na parte de programação de serviços.
Programação de serviços

Programação em um ambiente distribuído é complexa e cuidados tem que ser tomados, caso contrário, ela pode se tornar ineficiente. Para desenvolver aplicativos adequadamente distribuídos em Hadoop, temos algumas ferramentas de programação de serviços que fornecem utilitários que cuidam do aspecto da gestão de distribuição e de recursos. As ferramentas que iremos discutir são as seguintes: Apache YARN e Apache Zookeeper.
Apache YARN - Yet another Resource Negotiator (YARN) tem sido uma revolução na versão principal do Hadoop versão 2.x. YARN oferece gerenciamento de recursos e deve ser utilizado como uma plataforma comum para a integração e gerenciamento de diferentes ferramentas e utilitários em um cluster Hadoop. YARN é um gerenciador de recursos que foi criado separando as capacidades do motor de processamento e gestão de recursos do MapReduce. Ele também fornece a plataforma para outros fins, tais como, Storm, Spark, e assim por diante.
YARN melhorou suas capacidades, agora ele também pode ser ajustado para streaming e análise em tempo real, o que é um benefício enorme e uma necessidade em alguns cenários. YARNtambém é compatível com vários aplicativos MapReduce existentes. Alguns aplicativos alimentados porYARN
são os seguintes: Apache Hadoop MapReduce, Apache Spark, Apache Strom, Apache Tez e
Apache
S4.

Apache Zookeeper - ZooKeeper é um aplicativo distribuído, de código aberto e usado para a coordenação de serviços para aplicações distribuídas. Zookeeper expõe um conjunto simples de primitivas que aplicações distribuídas podem usar para sincronização, configuração,manutenção,
agrupamento e nomeação de recursos para a realização da coordenação, alta disponibilidade e sincronização. Zookeeper é executado em Java e tem ligações (bindings) para Java e C.HBase, Solr,
kata, Neo4j, e assim por diante, são algumas ferramentas que utilizam Zookeeper para coordenar as atividades.
Agendamento

O sistema Hadoop pode ter vários jobs e estes têm de ser agendados muitas vezes. O
agendamento de trabalhos do Hadoop é complexo e difícil de estruturar, gerenciar e monitorar.Podemos usar um sistema como Oozie para coordenar e monitorar os trabalhos do Hadoop de forma eficiente.
Apache Oozie: Oozie é um sistema de processamento de fluxo de trabalho e coordenação de serviços que permite que os usuários gerenciem múltiplas tarefas, como uma cadeia de trabalhos escritos em MapReduce, Pig, e Hive, também programas Java e scripts shell, e permite ligá-los uns aos outros.
Oozie é um serviço extensível, escalável e com reconhecimento de dados. Oozie pode ser usado para definir regras, começando e terminando um fluxo de trabalho, e detectando a conclusão de tarefas.
Análise de dados e aprendizagem de máquina

Em Hadoop, a análise dos dados é uma área de interesse chave. Hadoop é uma poderosa ferramenta para processar programas complexos e algoritmos que visam melhorar o processo de negócios. Aanálise de dados pode identificar insights e ajudar a otimizar o processo em relação aos competidores. Devido à natureza de processamento poderosa do Hadoop, o aprendizado de máquina tem estado em foco e vários algoritmos e técnicas têm sido adaptados para Hadoop.
As técnicas de aprendizado de máquina também são usadas em análises preditivas. A
análise de dados e a aprendizagem de máquina são necessárias para organizações ficarem à frente na competição. Para alguns pesquisadores, especialmente em ciências da vida, usam-se esses algoritmos para processar genes e padrões de registros médicos com o objetivo de gerar insights e detalhes importantes e úteis que são muito necessários na área médica.
Isso também é necessário para pesquisadores no campo da robótica para fornecer inteligência a máquinas para a execução e otimização de uma tarefa. RHadoop é uma linguagem estatística de análise de dados integrada com o Hadoop. Mahout é uma API de aprendizagem de máquina de código aberto usada pelo Hadoop.
Apache Mahout: Mahout é uma API escalável de aprendizagem de máquina, que tem uma variedade de bibliotecas de aprendizado de máquina implementada. Mahout é um projeto isolado que pode ser utilizado como uma biblioteca de aprendizagem de máquina pura, mas o poder doMahout aumenta quando ele é integrado com o Hadoop. Alguns dos algoritmos que são popularmente utilizados no Mahout são: Recomendação, Clustering e Classificação.
Administração de sistema

Implantar, provisionar, gerenciar e monitorar um cluster Hadoop requer conhecimento de script e normalmente leva uma boa quantidade de tempo e esforço manual, mas é repetitivo. Para a realização de tais atividades em Hadoop, podemos usar ferramentas como Ambari.
Apache Ambari - Ambari pode ser usado por desenvolvedores de aplicativos e integradores de sistemas para gerenciar a maioria das atividades de administração de um cluster Hadoop.Ambari é um framework open source do ecossistema Hadoop, que pode ser usado para a instalação,provisionamento, implantação, gerenciamento e monitoramento de um cluster
Hadoop. Seus principais objetivos são esconder a complexidade do gerenciamento de um clusterHadoop e fornecer uma interface web fácil e intuitiva. Uma característica fundamental do Ambari é que ele fornece APIs RESTful, que podem ser usadas para integração com outras ferramentas externas para uma melhor gestão.
Finalmente terminamos nossos comentários sobre alguns dos possíveis frameworks e tecnologias relacionadas ao Hadoop. A figura que apresentamos no início mostra a integração entre esses componentes de forma gráfica. Esperamos que você tenha gostado.
A seguir apresentaremos nossa tradicional lista de questões comentadas! Elas fazem parte da aula e devem ajudar você na fixação do conteúdo. São apresentadas questões das mais variadas bancas para abranger de forma mais ampla o conteúdo.
A maioria das evidências digitais é armazenada no sistema de arquivos do computador, mas entender como os sistemas de arquivos funcionam é um dos conceitos tecnicamente mais desafiadores para um investigador digital, porque existe pouca documentação.
Arquiteturas de dados modernas prometem a capacidade de acesso a diferentes tipos de dados para um número crescente de consumidores dentro de uma organização. Sem uma governança adequada, possibilitada por uma base sólida de metadados, essas arquiteturas geralmente se mostram apenas uma promessa que, em última análise, não conseguem entregar um resultado consistente.
Vamos analisar a logística distribuição de uma empresa como uma analogia para explicar os metadados e por que é essencial gerenciar os dados no ambiente de negócios atual.Quando você está enviando um pacote para um destino internacional, você quer saber onde na rota o pacote está localizado, e receber informações caso algo de errado aconteça com a entrega do pacote. As empresas de logística já mantêm manifestos para acompanhar o movimento de pacotes e a entrega bem-sucedida deles ao longo do processo de envio.
Os metadados fornecem esse mesmo tipo de visibilidade no ambiente atual, rico em dados. Os dados estão entrando e saindo das organizações, assim como trafegam dentro das empresas.Acompanhar as alterações de dados e detectar qualquer processo que cause problemas quando você estiver fazendo a análise de dados será difícil se você não tiver informações sobre os dados e o processo de movimentação deles. Hoje, até mesmo a alteração de uma única coluna em uma tabela de origem pode afetar centenas de relatórios que usam esses dados, o que torna extremamente importante saber de antemão quais colunas serão afetadas.
Os metadados fornecem informações sobre cada conjunto de dados, como tamanho, esquema de banco de dados, formato, horário da última modificação, listas de controle de acesso, uso, etc. Ouso de metadados permite o gerenciamento de uma plataforma e arquitetura de dados escaláveis,
bem como a governança dos dados. Metadados são comumente armazenados em um catálogo central para fornecer aos usuários informações sobre os conjuntos de dados disponíveis.
Os metadados podem ser classificados em três grupos:

1. Os metadados técnicos capturam a forma e a estrutura de cada conjunto de dados,
como o tamanho e a estrutura do esquema ou tipo de dados (texto, imagens, JSON, Avro etc.). Aestrutura do esquema inclui os nomes dos campos, seus tipos de dados, seus comprimentos, se eles podem estar vazios e assim por diante. A estrutura é geralmente fornecida por um banco de dados relacional ou pelo título em uma planilha, mas também pode ser adicionada durante a ingestão e a preparação de dados. Existem alguns metadados técnicos básicos que podem ser obtidos diretamente dos conjuntos de dados (por exemplo, tamanho), mas outros tipos de metadados são derivados.
2. Os metadados operacionais capturam a linhagem, a qualidade, o perfil e a proveniência (por exemplo, quando os elementos de dados chegaram, onde estão localizados, de onde vieram,qual é a qualidade dos dados, etc.). Também pode conter quantos registros foram rejeitados durante a preparação de dados ou uma execução de tarefa, e o sucesso ou fracasso da própria execução. Os metadados operacionais também identificam com que frequência os dados podem ser atualizados ou atualizados.
3. Metadados de negócios capturam o que os dados significam para o usuário final a fim de tornar os campos de dados mais fáceis de localizar e entender, por exemplo, nomes de empresas,descrições, tags, qualidade e regras de mascaramento. Eles se vinculam à definição de atributos de negócios para que todos estejam interpretando consistentemente os mesmos dados por um conjunto de regras e conceitos definido pelos usuários corporativos. Um glossário de negócios é um local central que fornece uma descrição de negócios para cada elemento de dados por meio do uso de informações de metadados.
Veja que esses critérios acima estão descrevendo metadados em um contexto global da empresa. Eessas informações são essenciais para tomada de decisão ou auxílio para o tratamento adequado das informações. É diferente de um perito que acompanha uma apreensão de computadores e precisa tomar alguns cuidados para não modificar os arquivos bem como os seus metadados. Veja o quadro abaixo um pouco mais sobre as atividades de perícia.
CURIOSIDADE

* Conectar a mídia original sem proteção de escrita pode alterar dados ou metadados de arquivos e essas alterações podem ser questionadas pelas partes envolvidas. Outra atividade essencial ao fazer a cópia é calcular o hash dos dados originais e o da cópia. Esses valores devem coincidir, garantindo-se, com isso, a integridade e a cadeia de custódia das evidências digitais.
* Ao se deparar com máquinas que estejam desligadas, vide regra, não se deve ligá-
las. O principal motivo dessa recomendação é a preservação dos dados. Ao se ligar as máquinas, o próprio processo de inicialização do sistema operacional fará alterações em alguns dados, e essas alterações podem ser detectadas examinando-se os metadados de carimbo de tempo dos arquivos. Além disso,acessar arquivos de interesse diretamente nas máquinas, também alterará, no mínimo, os dados de tempo dos arquivos. Desse modo, é preferível fazer imagem dos computadores e proceder as análises sobre as imagens
Informações de metadados podem ser obtidas de diferentes maneiras. Às vezes, ela é codificada nos conjuntos de dados, outras vezes pode ser inferida pela leitura do conteúdo; ou as informações podem ser espalhadas pelos arquivos de log que são gravados pelos processos que acessam esses conjuntos de dados.
DATA LAKE

Em todos os casos, os metadados são um elemento-chave no gerenciamento de um Data
Lake. Data
Lake é um termo recente, criado pelo CTO (Chief Technical Officer) do Pentaho, James
Dixon, para descrever um componente importante no universo da análise de dados e do Big Data. Aideia é ter um único repositório dentro da empresa, para que todos os dados brutos estejam disponíveis a qualquer pessoa que precise fazer análise sobre eles. Comumente utiliza-se o Hadoop para trabalhar com os Data Lakes, mas o conceito é bem mais amplo do que apenas Hadoop.
Os metadados são a base que permite que as seguintes características e recursos de data lake ou lago de dados sejam alcançados:
A visibilidade de dados é fornecida usando o gerenciamento de metadados para rastrear quais dados estão no lago de dados, junto com a origem, o formato e a linhagem. Isso também pode incluir uma exibição de série temporal, na qual você pode ver quais ações foram atribuídas ou executadas e ver exclusões e inclusões de dados. Isso é muito útil se você quiser fazer uma análise de impacto,o que pode ser necessário quando você faz o gerenciamento de alterações ou cria uma plataforma de dados ágil.
A confiabilidade dos dados dá a você a confiança de que suas análises estão sempre sendo executadas nos dados certos, com a qualidade certa, o que também pode incluir a análise dos metadados. Uma boa prática é usar uma combinação de abordagens top-down e bottom-up. Na abordagem de cima para baixo, um conjunto de regras definidas por usuários de negócios,administradores de dados ou um centro de excelência é aplicado e essas regras são armazenadas como metadados. Por outro lado, na abordagem de baixo para cima, os consumidores de dados podem qualificar ou modificar os dados ou avaliar os dados em termos de usabilidade,atualização,
etc. Os recursos de colaboração em uma plataforma de dados se tornaram uma maneira comum de alavancar a "sabedoria das multidões" para determinar a confiabilidade dos dados para um caso de uso específico.
A criação de perfil (profilling) de dados permite que os usuários obtenham informações sobre conjuntos de dados específicos e tenham uma noção do formato e do conteúdo dos dados.Ele permite que os cientistas de dados e os analistas de negócios tenham uma forma rápida de determinar se desejam usar os dados. O objetivo do perfil de dados é fornecer uma visão para os usuários finais que os ajude a entender o conteúdo do conjunto de dados, o contexto no qual eles podem ser usados na produção e quaisquer anomalias ou problemas que possam exigir correção ou proibir o uso dos dados. Em uma plataforma de dados ágil, o perfil de dados deve ser dimensionado para atender a qualquer volume de dados e estar disponível como um processo automatizado de entrada de dados ou como um processo ad hoc disponível para cientistas de dados,analistas de negócios ou administradores de dados que possam aplicar conhecimentos específicos ao assunto.
Ciclo de vida/idade dos dados: é provável que existam requisitos de envelhecimento diferentes para os dados em seu lago de dados, e eles podem ser definidos usando metadados operacionais.Os esquemas de retenção podem se basear em regras globais ou em casos de uso de negócios específicos, mas sempre têm como objetivo traduzir o valor dos dados em uma política de acesso e armazenamento apropriada. Isso maximiza o armazenamento disponível e dá prioridade aos dados mais críticos ou de alta utilização. As implementações iniciais de lagos de dados muitas vezes negligenciaram o ciclo de vida dos dados, pois o baixo custo de armazenamento e a natureza distribuída dos dados tornaram essa uma prioridade pouco relevante. À medida que essas implementações amadurecem, as organizações estão percebendo que gerenciar o ciclo de vida dos dados é fundamental para manter um data lake eficaz e compatível.
Segurança de dados e privacidade: os metadados permitem o controle de acesso e o mascaramento de dados (por exemplo, para informações de identificação pessoal) e garantem a conformidade com a indústria e outras regulamentações. Como é possível definir quais conjuntos de dados são confidenciais, você pode proteger os dados, criptografar colunas com informações pessoais ou conceder acesso aos usuários certos com base em metadados. Definir conjuntos de dados com metadados de segurança também simplifica os processos de auditoria e ajuda a expor quaisquer pontos fracos ou vulnerabilidades nas políticas de segurança existentes. Aidentificação de dados privados ou confidenciais pode ser determinada integrando os metadados do lago de dados com soluções de governança de dados corporativos, examinando os dados após a ingestão para procurar padrões comuns (SSN, códigos do setor etc.) ou utilizando o perfil de dados.
Acesso democratizado a dados úteis: os metadados permitem criar um sistema para ampliar a acessibilidade do usuário final e o autoatendimento (para aqueles com permissões) visando obter mais valor dos dados. Com uma extensa estratégia de metadados, você pode fornecer um catálogo robusto para os usuários finais, a partir do qual é possível pesquisar e encontrar dados em qualquer número de facetas ou critérios. Por exemplo, os usuários podem localizar facilmente os dados do cliente de um depósito Teradata que contém dados Pll, sem precisar conhecer nomes de tabelas específicos ou o layout do lago de dados.
Linhagem de dados e captura de dados alterados: Nos atuais pipelines de produção de dados, a maioria das empresas se concentra apenas nos metadados dos dados de entrada e saída.No entanto, é comum ter vários processos entre os conjuntos de dados de entrada e de saída, e esses processos nem sempre são gerenciados usando metadados e, portanto, nem sempre capturam alteração de dados ou linhagem. Em qualquer análise de dados ou processo de aprendizado de máquina, os resultados são sempre obtidos da combinação de algoritmos específicos em execução sobre conjuntos de dados específicos, por isso torna-se extremamente importante ter informações de metadados sobre os processos intermediários, a fim de melhorar a análise ao longo do tempo.
Os Data Lakes devem ser arquitetados adequadamente para aproveitar metadados e integrar-se a ferramentas de metadados existentes, caso contrário, criará um buraco no processo de governança de dados das organizações, pois a forma como os dados são usados, transformados e relacionados fora do data lake podem ser perdidos. Uma arquitetura de metadados incorreta muitas vezes pode impedir que os lagos de dados façam a transição de uma caixa de proteção analítica para uma plataforma de dados corporativos.
Em última análise, a maior parte do tempo gasto na análise de dados está preparando e limpando os dados, e os metadados ajudam a reduzir o tempo de insight1 fornecendo acesso fácil para
1 1 Descobrir algum padrão ou obter um resultado da análise.

descobrir quais dados estão disponíveis e mantendo um mapa de rastreamento de dados completo (linhagem de dados).
QUESTõES CoMENTADAS - MULTIBANCAS

1. Ano: 2018 Banca: CESPE Assunto: Informática para Polícia Federal Cargo: Agente Conteúdo
Big Data

Julgue os itens que se seguem, relativos a noções de mineração de dados,
big data e aprendizado de máquina.
85 Big data refere-se a uma nova geração de tecnologias e arquiteturas projetadas para processar volumes muito grandes e com grande variedade de dados, permitindo alta velocidade de captura, descoberta e análise.
Comentário: Vamos comentar cada uma das afirmações acima.

85. Mais uma vez, temos uma definição correta de Big Data. Veja que a afirmação aborda os 3V's presentes na definição original: volume, variedade e velocidade. Logo,
temos uma alternativa correta.
Gabarito: C.

CAIU

na prova!

2. Ano: 2018 Banca: CESPE Órgão: TCM-BA Cargo: Auditor de Contas Questão: 14

Acerca de big data, assinale a opção correta.

A A utilização de big data nas organizações não é capaz de transformar os seus processos de gestão e cultura.
B Sistemas de recomendação são métodos baseados em computação distribuída, que proveem uma interface para programação de clusters, a fim de recomendar os tipos certos de dados e processar grandes volumes de dados.
C Pode-se recorrer a software conhecidos como scrapers para coletar automaticamente e visualizar dados que se encontram disponíveis em sítios de navegabilidade ruim ou em bancos de dados difíceis de manipular.
D As ações inerentes ao processo de preparação de dados incluem detecção de anomalias,
deduplicação, desambiguação de entradas e mineração de dados.

E O termo big data se baseia em cinco Vs: velocidade, virtuosidade, volume, vantagem e valor.

Comentário: Vamos comentar cada uma das alternativas acima:

A) Esse conceito de transformar processos de gestão e cultura está associado a outro conceito,o de gestão de processos de negócio, conhecido como BPM. Logo, temos uma alternativa incorreta.
B) Um Sistema de Recomendação combina várias técnicas computacionais para selecionar itens personalizados com base nos interesses dos usuários e conforme o contexto no qual estão inseridos. Tais itens podem assumir formas bem variadas como, por exemplo, livros,filmes,
notícias, música, vídeos, anúncios, links patrocinados, páginas de internet, produtos de uma loja virtual, etc. Empresas como Amazon, Netflix e Google são reconhecidas pelo uso intensivo de sistemas de recomendação com os quais obtém grande vantagem competitiva. Veja que não existe nenhuma obrigação dos sistemas serem estruturados em um cluster e usarem computação distribuída.
C) Essa é a nossa resposta, e confesso desde já que não apresentamos esse conceito em nosso material. Data scraping (do inglês, raspagem de dados) é uma técnica computacional na qual um programa extrai dados de saída legível somente para humanos, proveniente de um serviço ou aplicativo. Os dados extraídos geralmente são minerados e estruturados em um formato padrão como CSV, XML ou JSON. Vejam que o objetivo é transformar os dados não estruturados em modelos mais fáceis de manipular.
D) Data preparation é o processo de coletar, limpar, normalizar, combinar, estruturar e organizar dados para análise. Ele é o passo inicial (e fundamental) para que o trabalho com BigData seja bem-sucedido, uma vez que aumenta a qualidade dos dados - e,
consequentemente,
dos resultados com data mining. Dados "pobres", de qualidade ruim, geram resultados incorretos e não-confiáveis ao fim do processo de uso das tecnologias de Data Science.Vejam que a mineração de dados é uma ação feita em uma etapa posterior a preparação dos dados.Logo, temos uma alternativa incorreta.

E) Observem que os v's listados na alternativa não são os que está descrito na definição de big data, os conceitos corretos são: Volume, Velocidade, Variedade, Veracidade e Valor.
Gabarito: C.

CAIU

na prova!

3. Ano: 2018 Banca: Cesgranrio Órgão: Petrobras Cargo: Analista de Processo de
Negócio
Questão: 42

A principal definição de Big Data parte de três características, conhecidas como 3 V do Big Data,
a saber: velocidade, variedade e volume.

O termo velocidade refere-se, principalmente, à

(A) necessidade das aplicações de gerar respostas rapidamente, a partir de grandes massas de dados.
(B) existência de um alto fluxo de dados na entrada.

(C) necessidade de gerar aplicações rapidamente, em função da demanda do negócio.

(D) importância da facilidade de manipular cubos de visualização de dados, rapidamente.

(E) rapidez com que os dados se tornam inválidos com o tempo.

Comentário: Essa é a primeira questão de Big Data elaborada pela Cesgranrio. Acho que a falta de experiência nesse assunto fez com que as alternativas A e B pudessem ser consideradas a resposta correta. Vamos construir os conceitos para ver se chegamos a alguma conclusão sobre o pensamento do examinador ao elaborar essa questão. Começamos pela definição de big data.
Big data é um termo que descreve grandes volumes de alta velocidade, dados complexos e variáveis que exigem técnicas avançadas tecnologias para permitir a captura,armazenamento,
distribuição, gestão e análise da informação.

Agora vamos voltar para os 3 V's da definição original. Volume refere-se à magnitude dos dados. Variedade refere-se à heterogeneidade estrutural em um conjunto de dados. E o volume?
Velocidade refere-se à taxa na qual os dados são gerados e a velocidade com que devem ser analisados e utilizados. A proliferação de dispositivos digitais, como smartphones e sensores,levou a uma taxa sem precedentes de criação de dados e está impulsionando a necessidade crescente de análise em tempo real e planejamento baseado em evidências.
Mesmo os varejistas convencionais estão gerando dados numa frequência extremamente alta.
O Wal-Mart, por exemplo, processa mais de um milhão de transações por hora. Os dados provenientes de dispositivos móveis e fluindo por meio de aplicativos produzem um universo de informações que podem ser usadas para gerar ofertas personalizadas em tempo real para clientes comuns.
Esses dados fornecem informações sólidas sobre os clientes, como localização geoespacial,
dados demográficos e padrões de compra anteriores, que podem ser analisados em tempo real para criar um valor real para o cliente.
Vejam que o fluxo de dados na entrada ou a taxa de geração de dados é uma medida relevante para a velocidade. Agora, se formos analisar a alternativa A tem dois pontos que me deixaram com uma pulga atrás da orelha.
O primeiro deles se refere ao fato dele afirmar que existe uma necessidade das aplicações(vamos supor que sejam as aplicações de Big Data) gerarem resposta rapidamente. Isso de fato tem relação com velocidade, mas não é uma obrigatoriedade. Já o segundo ponto refere-se a grandes massas de dados veja que esse termo está mais associado ao volume do que à velocidade. Assim, acabei me convencendo que a alternativa B era de fato a resposta para a questão.
Contudo, com uma boa referência, é possível refutar a banca mostrando a presença de duas afirmações corretas entre as alternativas.
Gabarito: B.

CAIU

na prova!

4. Ano: 2018 Banca: CESPE Órgão: TCE-PB Prova: Auditor de Contas Públicas - Demais Áreas

Com referência a big data, assinale a opção correta.

a) A definição mais ampla de big data restringe o termo a duas partes — o volume absoluto e a velocidade —, o que facilita a extração das informações e dos insights de negócios.
b) O sistema de arquivos distribuído Hadoop implementa o algoritmo Dijkstra modificado para busca irrestrita de dados em árvores aglomeradas em clusters com criptografia.
c) Em big data, o sistema de arquivos HDFS é usado para armazenar arquivos muito grandes de forma distribuída, tendo como princípio o write-many, read-once.
d) Para armazenar e recuperar grande volume de dados, o big data utiliza bancos SQL
nativos,
que são bancos de dados que podem estar configurados em quatro tipos diferentes de armazenamentos: valor chave, colunar, gráfico ou documento.
e) O MapReduce é considerado um modelo de programação que permite o processamento de dados massivos em um algoritmo paralelo e distribuído.
Comentário: Vejamos cada uma das afirmações acima.

a) a definição mais simples de big data já estrutura o termo em 3 conceitos: volume,
variedade e velocidade. Logo, temos uma alternativa incorreta.
b) Essa questão tem diversos conceitos dispersos que não fazem sentido da forma como foi apresentada no texto. Veja que o Hadoop possui de fato um sistema de armazenamento distribuído: o HDFS. O HDFS possui uma arquitetura mestre/escravo. Um cluster HDFSconsiste em um único NameNode, considerado o servidor mestre que gerencia o namespace do sistema de arquivos e regula o acesso a arquivos por clientes. Além disso, há váriosDataNodes,
geralmente um por nó do cluster, que gerenciam o armazenamento associado aos nós em que são executados. Não existe o uso do algoritmo de Dijkstra1 para busca em registros, ele está preocupado em achar o menor caminho e um grafo.
Sobre criptografia, o HDFS implementa criptografia transparente de ponta a ponta. Depois de configurados, os dados lidos e gravados em diretórios HDFS especiais são criptografados e descriptografados de forma transparente, sem exigir alterações no código do aplicativo do usuário.
c) Em big data temos um princípio semelhante ao do data warehoure, os dados são escritos apenas uma vez, write-once e lido por diversas pessoas, read-many. Assim, a alternativa c também está errada.
d) Sabemos que os bancos de dados NoSQL não são SQL nativos, logo, não podemos marcar essa alternativa como resposta.
e) Sobrou apenas essa alternativa que apresentou uma definição consistente de MapReduce.
Logo, marcamos nossa resposta nesta letra E.

1 Uma aplicação de busca em um grafo comum é encontrar o caminho mais curto obtido entre um nó inicial e um ou mais nós de destino. Comumente feito em uma única máquina com o Algoritmo deDijkstra.

Gabarito: E.

CAIU

na prova!

5. Ano: 2018 Banca: FCC Prova: Análise de Informações Concurso: TCE-RS Q.: 49

49. Um sistema de Big Data costuma ser caracterizado pelos chamados 3 Vs, ou seja,
volume,
variedade e velocidade. Por variedade entende-se que

(A) há um grande número de tipos de dados suportados pelo sistema.

(B) há um grande número de usuários distintos acessando o sistema.

(C) os tempos de acesso ao sistema apresentam grande variação.

(D) há um grande número de tipos de máquinas acessando o sistema.

(E) os tamanhos das tabelas que compõem o sistema são muito variáveis.

Comentários: Big data permite que as organizações armazenem, administrem e manipulem vastas quantidades de dados na velocidade certa e no tempo certo. Para conseguir os insights certos, big data é, normalmente, dividido em três características:
Volume: Quantidade de dados.

Velocidade: Com que rapidez os dados são gerados.

Variedade: Os vários tipos de dados.

Assim, o gabarito pode ser observado na alternativa A.

CAIU

na prova!

6. Ano: 2017 Banca: FCC Órgão: DPE-RS Prova: Analista - Banco de Dados

Os sistemas de Big Data costumam ser caracterizados pelos chamados 3 Vs, sendo que o V de a) Veracidade corresponde à rapidez na geração e obtenção de dados.
b) Valor corresponde à grande quantidade de dados acumulada.

c) Volume corresponde à rapidez na geração e obtenção de dados.

d) Velocidade corresponde à confiança na geração e obtenção dos dados.

e) Variedade corresponde ao grande número de tipos ou formas de dados.

Comentário: Analisando as alternativas acima, podemos aproveitar para relembrar os conceitos corretos associados a cada um dos termos. Os primeiros esforços para definir o significado do Big Data caracterizaram-no em termos dos Três Vs: Volume,Velocidade,
Variedade. À medida que mais organizações começaram a aproveitar o potencial do Big
Data,
a lista de V se expandiu, vejamos cada um deles:

Volume: refere-se à quantidade de dados. O Big Data geralmente tem milhares de entidades ou elementos em bilhões de registros.
Velocidade: refere-se à velocidade na qual os dados são capturados,
gerados ou compartilhados. Big Data é frequentemente gerado e pode ser distribuído e até analisado em tempo real.
Variedade/Variabilidade: Refere-se às formas em que os dados são capturados ou entregues.
Big Data requer armazenamento de vários formatos de arquivos e dados (estruturados e não estruturados).
Volatilidade: refere-se à frequência com que as alterações de dados ocorrem e, portanto,
quanto tempo os dados são úteis.

Veracidade: refere-se ao grau de confiabilidade dos dados. Assim, podemos marcar nossa resposta na alternativa E.
Gabarito: E.

CAIU

na prova!

7. Ano: 2018 Banca: CESPE Órgão: CGM de João Pessoa - PB Prova: Auditor
Municipal de
Controle Interno - Desenvolvimento de Sistemas

A respeito de business intelligence, julgue o próximo item.

Situação hipotética: Um órgão público pretende fazer uma análise de big data com o objetivo de realizar mineração em grandes conjuntos de dados corporativos para localizar ou encontrar padrões ocultos, o que exigirá uma grande quantidade de processamento.
Assertiva: Nesse caso, há necessidade de contratação de um SaaS (software como serviço),
que acrescentará uma camada adicional de integração com frameworks de desenvolvimento de aplicativos, recursos de middleware e funções como bancos de dados.
Comentário: Para respondermos a essa questão precisamos olhara para os conceitos deInfraestrutura, Plataforma e Software como serviço, vamos, primeiramente olhara para a figura a seguir:
Infrastructure Platform Software

(as a Service) ar

<9

C

(as a Service) (as a Service)

Applications

<S9 L- l Applications jj Applications

1 . 1

Runtimes H

-

$ Runtimes

Runtimes

Security flr Intrgr JIHwI |||| Sccuiit/ & lntegraoon z
Da ta ba sos H Data bases OI

Ql

(8

Securit, & Intecpaoon

Data bases

Servets
Virtualization

Server HW

z

-o»

<£>

8.

Serveis

CL

Virtualization

<
(9

Server HW 3

o

Servers
Virtualization
Servei HW

Storage
Networking s Storage Stoiage
Q.

O Networking Networking

O modelo laaS inclui os recursos de infraestrutura desde as instalações até as plataformas de hardware que ali residem. Incorpora a capacidade de abstrair recursos e oferecer conectividade física e lógica a estes recursos. Fornece também um conjunto de APIs que permitem a gestão e outras formas de interação com a infraestrutura por parte dos clientes.
O modelo PaaS acrescenta uma camada adicional de integração com frameworks de desenvolvimento de aplicativos, recursos de middleware e funções como banco de dados,mensagens e filas, permitindo aos desenvolvedores criarem aplicativos para a plataforma cujas linguagens de programação e ferramentas são suportadas pela pilha.
O modelo SaaS fornece um ambiente operacional autocontido usado para entregar todos os recursos do usuário, incluindo o conteúdo, a apresentação, as aplicações e a capacidade de gestão.
Analisando a questão:

"... SaaS (software como serviço), que acrescentará uma camada adicional de integração com frameworks de desenvolvimento de aplicativos, recursos de middleware e funções como bancos de dados."
A assertiva cita uma contratação de SaaS, porém apresenta as características de uma contratação PaaS (integração com frameworks de desenvolvimento de aplicativos, recursos de middleware e funções como bancos de dados.).
Logo a questão está errada.

Gabarito: E.

CAIU

na prova!

8. Ano: 2017 Banca: FGV Órgão: IBGE Prova: Analista Censitário - Análise de
Sistemas -
Desenvolvimento de Aplicações - Web Mobile

Bancos de Dados NoSQL podem armazenar dados em diversos formatos não relacionais, como documentos compostos por pares de campo-e-valor (field-and-value), conforme a estrutura exemplificada a seguir.
O Banco de Dados NoSQL utilizado para armazenar documentos compostos por pares campo-
e-valor, no formato BSON (JSON-like), é o:

a) OpenLink Virtuoso;

b) Neo4j;

c) Apache HBase;

d) MongoDB;

e) Titan.

Comentário: Veja que a questão exige apenas que você saiba qual desses nomes acima é um banco de dados NoSQL do tipo chave-valor. Vejam a figura abaixo para saber onde cada alternativa se enquadra e quais os outros exemplos de cada tipo de base de dados NoSQL.
Amazon
DynamoDB

Chave-valor

BERKELEYDB

Grafo

4 InfiniteGraph

Tabular â redis
HBASE Cassandra

Documento

Desta forma, podemos marcar nossa resposta na alternativa D

Gabarito: D.

CAIU

na prova!

9. Ano: 2015 Banca: CESPE Órgão: TJDFT Cargo: Suporte em Tecnologia da Informação
-
Questões 92 e 93

A respeito de tipos de bancos de dados, julgue os itens que se seguem.

92 A capacidade de estender tipos de dados básicos é uma das características dos bancos de dados objeto relacional.
93 Sistemas de bancos de dados classificados como NoSQL permitem a inserção de dados sem que haja um esquema predefinido.
Comentários: Essa questão trata na alternativa 92 de banco de dados relacionais. A
ideia descrita na alternativa trata dos itens conhecidos como user defined type-DDT. Eles aparecem dentro do padrão SQL e permitem que novos tipos possam ser estendidos dos tipos básicos.
A alternativa 93, por sua vez, refere-se ao assunto presente nesta aula. Vejam que a existência de esquema bem definido não é uma obrigatoriedade dentro do contexto de bancos de dadosNoSQL. Essa propriedade é conhecida como schema free ou livre de esquema.

Pelo exposto acima, as duas alternativas estão corretas.

Gabarito: C C.

CAIU

na prova!

10. Ano: 2016 Banca: FGV Órgão: IBGE Cargo: WEB MOBILE Questão: 41

Considere as seguintes características de um projeto de banco de dados.

I. O modelo de dados é conhecido a priori e é estável;

II. A integridade dos dados deve ser rigorosamente mantida;

III. Velocidade e escalabilidade são preponderantes.

Dessas características, o emprego de bancos de dados NoSQL é favorecido somente por:

(A) I;

(B) lell;

(C) II;

(D) II e III;

(E) III.

Comentário: Veja que a questão trata das propriedades ou características de um projeto de banco de dados NoSQL. Sabemos que bancos de dados deste tipo substituem a sigla ACID(atomicidade, consistência, isolamento e durabilidade) que está relacionado com transações pela sigla BASE que está relacionada com os conceitos de BA -(Basically Available)
disponibilidade é prioridade, S - (Soft-State) - Não precisa ser consistente o tempo todo e E -(Eventually Consistent) - Consistente em momento indeterminado. Outro ponto importante é a relação de NoSQL com o modelo de dados, geralmente o banco é considerado schema free,ou seja, livre de esquema ou de um modelo pré-determinado a priori.

Partindo desta exposição básica sobre NoSQL podemos analisar as alternativas I, II e
III. Vejam que as duas primeiras são definições associadas a banco de dados relacionais ou transacionais.A alternativa III trata de outro aspecto que não vimos ainda, mas que também está relacionada ao conceito de NoSQL e Big Data. NoSQL é uma tecnologia que trouxe o foco de banco de dados para performance e escalabilidade. A pergunta é como analisar uma grande quantidade de dados.
Gabarito: E.

CAIU

na prova!

11. Ano: 2016 Banca: ESAF Órgão: ANAC Cargo: Analista de TI - QUESTÃO 62

Big Data é:

a) volume + variedade + agilidade + efetividade, tudo agregando + valor + atualidade.

b) volume + oportunidade + segurança + veracidade, tudo agregando + valor.

c) dimensão + variedade + otimização + veracidade, tudo agregando + agilidade.

d) volume + variedade + velocidade + veracidade, tudo agregando + valor.

e) volume + disponibilidade + velocidade + portabilidade, tudo requerendo - valor.

Comentário: Embora o termo "big data" seja relativamente novo, o ato de recolher e armazenar grandes quantidades de informações para eventual análise de dados é bem antigo.O conceito ganhou força no início dos anos 2000, quando um analista famoso deste setor,
Doug
Laney, articulou a definição de big data como os três Vs:

Volume. Organizações coletam dados de uma grande variedade de fontes,
incluindo transações comerciais, redes sociais e informações de sensores ou dados transmitidos de máquina a máquina. No passado, armazenar tamanha quantidade de informações teria sido um problema - mas novas tecnologias (como o Hadoop) têm aliviado a carga.
Velocidade. Os dados fluem em uma velocidade sem precedentes e devem ser tratados em tempo hábil. Tags de RFID, sensores, celulares e contadores inteligentes estão impulsionado a necessidade de lidar com imensas quantidades de dados em tempo real, ou quase real.
Variedade. Os dados são gerados em todos os tipos de formatos - de dados estruturados,
dados numéricos em bancos de dados tradicionais, até documentos de texto não estruturados,e-mail, vídeo, áudio, dados de cotações da bolsa e transações financeiras.

Outros Vs foram adicionados ao longo dos anos:

Veracidade. O quarto V do conceito está ligado à veracidade do conteúdo. Nem todos os dados gerados possuem consistência dentro do contexto. É preciso destacar o que é rico e correto em conteúdo no meio de tanta informação. Ao garantir essa separação, que é possível fazer a partir do Big Data, o que sobra são conhecimentos importantes para compreender melhor a entidade analisada ou o negócio em questão.
Valor. Para garantir que o trabalho dos outros Vs traga retorno, é preciso gerar valor para os resultados que retornam do Big Data. Assim, aparece o último V do conceito.
Juntando todos os conceitos acima, chegamos a nossa resposta na alternativa D.

Gabarito: D.

CAIU

na prova!

12. Ano: 2016 Banca: ESAF Órgão: ANAC Cargo: Analista de TI - QUESTÃO 70

Para o processamento de grandes massas de dados, no contexto de Big Data, é muito utilizada uma plataforma de software em Java, de computação distribuída, voltada para clusters,inspirada no MapReduce e no GoogleFS. Esta plataforma é o(a)

a) Yam Common.

b) GoogleCrush.

c) EMRx.

d) Hadoop.

e) MapFix

Comentário: Questão inspirada na WIKIPEDIA:

Hadoop é uma plataforma de software em Java de computação distribuída voltada para clusters e processamento de grandes massas de dados. Foi inspirada no MapReduce e noGoogleFS (GFS). Trata-se de um projeto da Apache de alto nível, que vem sendo construído por uma comunidade de colaboradores utilizando em sua maior parte a linguagem de programação Java, com algum código nativo em C e alguns utilitários de linha de comando escrito utilizando scripts shell. Assim podemos marcar nossa resposta na alternativa D.
Gabarito: D.

CAIU

na prova!

13. ANO: 2015 BANCA: FGV ÓRGÃO: TJ-SC PROVA: ANALISTA JUDICIÁRIO - ANALISTA DE
SISTEMAS

Os termos Business Intelligence (BI) e Big Data confundem-se em certos aspectos. Uma conhecida abordagem para identificação dos pontos críticos de cada paradigma é conhecida como 3V, e destaca:
A variedade, visualização, volume;

B velocidade, virtualização, volume;
C variedade, velocidade, volume;

D virtualização, visualização, volume;

E variedade, visualização, virtualização.

Comentário: Questão interessante! Trata dos 3 Vs que definem o primeiro conceito de Big
Data. Sabemos que se trata da Variedade, Velocidade e Volume. O primeiro faz referência aos diferentes tipos de dados ou informações que devem ser processadas. O segundo se preocupa com o tempo para o processamento e armazenamento de forma consistente e acessível das informações geradas. Por fim, o volume consiste na percepção de que a quantidade dos dados aumenta a cada dia em grandes proporções.
Gabarito: C.

CAIU

na prova!

14. ANO: 2014 BANCA: CESPE ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - BANCO DE DADOS

Julgue os itens que se seguem, no que se refere a Big Data.

[1] O processamento de consultas ad hoc em Big Data, devido às características de armazenamento dos dados, utiliza técnicas semelhantes àquelas empregadas em consultas do mesmo tipo em bancos de dados tradicionais.
Comentário: O processamento de consultas ad hoc no contexto de big data traz desafios diferentes daqueles incorridos ao realizar consultas ad hoc em dados estruturados pelo fato de as fontes e formatos dos dados não serem fixos e exigirem mecanismos diferentes para recuperá-los e processá-los.
Embora as consultas ad hoc simples possam ser resolvidas pelos provedores de big data,
na maioria dos casos, elas são complexas porque os dados, algoritmos, formatos e resoluções da entidade devem ser descobertos dinamicamente. O conhecimento dos cientistas de dados e dos usuários corporativos é necessário para definir a análise exigida para as seguintes tarefas:
* Identificar e descobrir os cálculos e algoritmos

* Identificar e descobrir as fontes de dados

* Definir os formatos necessários que podem ser consumidos pelos cálculos

* Executar os cálculos nos dados paralelamente

Gabarito: E.

CAIU

na prova!

15. ANO: 2014 BANCA: CESPE ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - BANCO DE DADOS

Julgue os itens que se seguem, no que se refere a Big Data.

Em soluções Big Data, a análise dos dados comumente precisa ser precedida de uma transformação de dados não estruturados em dados estruturados.
Comentário: As soluções de big data são, em sua maioria, dominadas por sistemas Hadoop e tecnologias baseadas em MapReduce, que são soluções simples de instalar para processamento e armazenamento distribuídos. No entanto, a extração de dados a partir de dados não estruturados, como imagens, áudio, vídeo, feeds binários ou até mesmo texto,é uma tarefa complexa e precisa de técnicas como aprendizado de máquina e processamento de idioma natural, etc. O outro grande desafio é como verificar a precisão e a exatidão do resultado de tais técnicas e algoritmos.
Para executar a análise em quaisquer dados, eles devem estar em algum tipo de formato estruturado. Os dados não estruturados acessados de várias fontes podem ser armazenados como estão e, em seguida, transformados em dados estruturados (por exemplo,JSON) e novamente armazenados nos sistemas de armazenamento de big data. O texto não estruturado pode ser convertido em dados estruturados ou semiestruturados. Da mesma
I forma, os dados de imagem, áudio e vídeo precisam ser convertidos nos formatos que podem ser usados para análise. Além disso, a precisão e exatidão da analítica avançada que usa algoritmos preditivos e estatísticos dependem da quantidade de dados e algoritmos usados para treinar os modelos.
Gabarito: C.

CAIU

na prova!

16. ANO: 2014 BANCA: CESPE ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - BANCO DE DADOS

Julgue os itens que se seguem, no que se refere a Big Data.

[1] Ao utilizar armazenamento dos dados em nuvem, a localização do processamento de aplicações Big Data não influenciará os custos e o tempo de resposta, uma vez que os dados são acessíveis a partir de qualquer lugar.
Comentário: Muito embora haja uma abstração quanto ao local do processamento, afinal, se contrata um serviço e pouco importa como e onde ele será prestado, essa escolha tem consequências.
Muitos provedores de serviço na nuvem, como a Amazon, possuem tarifas diferenciadas com relação à localização de cada servidor. Cada país tem seus custos e suas especificidades.
Além disso, quanto mais longe o servidor estiver do interessado, maior será o tempo de espera entre a requisição e a resposta.
Gabarito: E.

CAIU

na prova!

17. ANO: 2015 BANCA: FGV ÓRGÃO: TJ-BA PROVA: TÉCNICO DO JUDICIÁRIO - TECNOLOGIA DA
INFORMAÇÃO

Analise as afirmativas a respeito da classe de gerenciadores de bancos de dados, surgida em anos recentes, conhecida como NoSQL.
I. Mesmo sem suportar tabelas relacionais, baseiam-se em esquemas de dados previamente definidos;
II. Suas estruturas não permitem o uso de linguagens do tipo do SQL para recuperação de dados;
III. Garantem operações com as propriedades conhecidas pela sigla ACID;

IV. Privilegiam a rapidez de acesso e a disponibilidade dos dados em detrimento das regras de consistência das transações.
O número de afirmativas corretas é:

A uma;
B duas;
C três;

D quatro;
E cinco.

Comentário: Se voltarmos a parte da nossa aula teórica que trata de NoSQL veremos que a única alternativa correta é a presente na assertiva IV.
Gabarito: A.

CAIU

na prova!

18. ANO: 2015 BANCA: CESPE ÓRGÃO: TCU PROVA: AUDITOR FEDERAL DE CONTROLE EXTERNO

- TECNOLOGIA DA INFORMAÇÃO

Julgue os itens subsecutivos, a respeito de sistemas de bancos de dados.

Como forma de permitir as buscas em documentos semiestruturados, um banco de dados
NoSQL do tipo orientado a documentos armazena objetos indexados por chaves utilizando tabelas de hash distribuída.
Comentário: Quando tratamos de bases de dados NoSQL podemos classificá-las em quatro diferentes tipos, são eles:
Chave/valor (Key/Value): conhecidos como tabelas de hash distribuídas. Armazenam objetos indexados por chaves, e facilita a busca por esses objetos a partir de suas chaves.
Orientados a Documentos: os documentos dos bancos são coleções de atributos e valores onde um atributo pode ser multivalorado. Em geral, os bancos de dados orientados a documento não possuem esquema, ou seja, os documentos armazenados não precisam possuir estrutura em comum. Essa característica faz deles boas opções para o armazenamento de dados semiestruturados.
Colunar: Bancos relacionais normalmente guardam os registros das tabelas contiguamente no disco. Por exemplo, caso se queira guardar id, nome e endereço de usuários em um banco de dados relacional, os registros seriam:
Idl, Nomel, Endereçol;
Id2, Nome2, Endereço2.

Essa estrutura torna a escrita muito rápida, pois todos os dados de um registro são colocados no disco com uma única escrita no banco. Também é eficiente caso se queira ler registros inteiros. Mas para situações onde se quer ler algumas poucas colunas de muitos registros, essa estrutura é pouco eficiente, pois muitos blocos do disco terão de ser lidos.
Para esses casos onde se quer otimizar a leitura de dados estruturados, bancos de dados de famílias de colunas são mais interessantes, pois eles guardam os dados contiguamente por coluna.
O exemplo anterior em um banco de dados dessa categoria ficaria:

Idl, Id2; Nomel, Nome2; Endereçol, Endereço2.

Os bancos de dados de famílias de colunas são mais interessantes para processamento analítico online (OLAP). Bigtable é uma implementação da Google dessa categoria de bancos de dados.
Orientado a Grafos: diferente de outros bancos de dados NoSQL, esse está diretamente relacionado a um modelo de dados estabelecido, o modelo de grafos. A ideia desse modelo é representar os dados e / ou o esquema dos dados como grafos dirigidos, ou como estruturas que generalizem a noção de grafos. O modelo de grafos é aplicável quando "informações sobre a interconectividade ou a topologia dos dados são mais importantes, ou tão importante quanto os dados propriamente ditos". Possui três componentes básicos: os nós (são os vértices do grafo), os relacionamentos (são as arestas) e as propriedades (ou atributos)dos nós e relacionamentos.
Vejam que a afirmativa do CESPE confunde os conceitos de orientado a documentos com o conceito de chave valor. Quanto nós tratamos de tabelas hash distribuídas está associada ao tipo chave-valor e não ao conceito de orientado a documentos como está dito na questão.Sendo, portanto, alternativa errada.

Gabarito: E.

CAIU

na prova!

19. ANO: 2014 BANCA: CESPE ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - BANCO DE DADOS

Acerca de bancos de dados semiestruturados e bancos de dados NOSQL, julgue os itens subsecutivos.
Bancos de dados NOSQL orientados a documentos são apropriados para o armazenamento de dados semiestruturados.
Comentário: Exatamente, neles é possível armazenamento de documentos que embora tenham uma estrutura básica, eles, geralmente não são definidos por nenhum modelo ou schema. Podemos, então, encontrar propriedades dentro dos documentos, mas não existe uma obrigatoriedade sobre a existência delas.
Gabarito: C

CAIU

na prova!

20. ANO: 2014 BANCA: CESPE ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - BANCO DE DADOS

Acerca de bancos de dados semiestruturados e bancos de dados NOSQL, julgue os itens subsecutivos.
Para garantir a eficiência das consultas a bancos de dados semiestruturados, é fundamental a adoção de técnica de indexação que leve em consideração, além das informações, as propriedades estruturais dos dados.
Comentário: A questão 87 envolve alguns conceitos interessantes. Começa falando sobre dados semiestruturados, por exemplo, XML ou JSON. Para viabilizar a indexação de dados semiestruturados é preciso conhecimento das propriedades dos objetos de dados. Consultas em bancos de dados semiestruturados consideram tanto a estrutura quanto os valores. Outra questão é a criação de índice sobre um conjunto de dados semiestruturados. Para avaliar se um índice deve ou não ser criado é importante usar as informações sobre a estrutura dos dados e os valores armazenados. Neste caso, considerando a necessidade de um espaço maior para armazenamento e do custo de manutenção, a criação do índice deve melhorar a performance para ser de fato implementado. Logo, a assertiva está correta.
Gabarito: C

CAIU

na prova!

21. ANO: 2014 BANCA: CESPE ÓRGÃO: TJ-SE PROVA: ANALISTA JUDICIÁRIO - BANCO DE DADOS

Acerca de bancos de dados semiestruturados e bancos de dados NOSQL, julgue os itens subsecutivos.
Devido à escalabilidade esperada para os bancos de dados NOSQL, a implementação desses bancos utiliza modelos de armazenamento de dados totalmente distintos dos utilizados em sistemas relacionais.
Comentário: Nem todos os modelos de armazenamentos são totalmente distintos dos sistemas relacionais. Se pensarmos no modelo de armazenamento colunar ele é semelhante a uma tabela, mas guardam os dados das colunas contiguamente no disco.
NoSQL são diferentes sistemas de armazenamento que vieram para suprir necessidades em demandas onde os bancos de dados tradicionais (relacionais) são ineficazes. Muitas dessas bases apresentam características muito interessantes, como alta performance, escalabilidade,replicação, suporte à dados estruturados e sub colunas.

O NoSQL surgiu da necessidade de uma performance superior e de uma alta escalabilidade. Os atuais bancos de dados relacionais são muito restritos a isso, sendo necessária a distribuição vertical de servidores, ou seja, quanto mais dados, mais memória e mais disco um servidor precisa. O NoSQL tem uma grande facilidade na distribuição horizontal, ou seja, mais dados,mais servidores, não necessariamente de alta performance. Um grande utilizador desse conceito é o Google, que usa computadores de pequeno e médio porte para a distribuição dos dados; essa forma de utilização é muito mais eficiente e econômica. Além disso, os bancos de dados NoSQL são muito tolerantes a erros.
No caso dos bancos NoSQL, toda a informação necessária estará agrupada no mesmo registro,ou seja, em vez de você ter o relacionamento entre várias tabelas para formar uma informação,ela estará em sua totalidade no mesmo registro.

Gabarito: E

CAIU

na prova!

22. ANO: 2013 BANCA: CESPE ÓRGÃO: CNJ PROVA: ANALISTA JUDICIÁRIO - ANÁLISE DE
SISTEMAS

No que se refere ao desenvolvimento web de alto desempenho, julgue os itens subsequentes.
Uma característica de bancos de dados NoSQL é o suporte à replicação de dados. Entre as abordagens utilizadas para replicação, inclui-se a mestre-escravo.
Comentário: São dois tipos de replicação: mestre-escravo e ponto a ponto. A
replicação mestre-escravo torna um nodo a cópia oficial, a qual lida com gravações, enquanto os escravos sincronizam-se com o mestre e podem lidar com as leituras. A replicação ponto a ponto permite gravações em qualquer nodo; os nodos são coordenados para sincronizar suas cópias de dados. A replicação mestre-escravo reduz a chance de conflitos de atualização, mas a ponto a ponto evita carregar todas as gravações em um único ponto de falha.
Gabarito: C

CAIU

na prova!

23. ANO: 2013 BANCA: CESPE ORGAO: CNJ PROVA: ANALISTA JUDICIÁRIO - ANALISE DE
SISTEMAS

No que se refere ao desenvolvimento web de alto desempenho, julgue os itens subsequentes.

A escalabilidade dos bancos de dados NoSQL é garantida pela ausência de um esquema
(scheme free).

Comentário: A escalabilidade é garantida através da característica nativa de clusterização do banco de dados.
Gabarito: E

CAIU

na prova!

24. ANO: 2013 BANCA: CESPE ORGAO: CNJ PROVA: ANALISTA JUDICIÁRIO - ANALISE DE
SISTEMAS

No que se refere ao desenvolvimento web de alto desempenho, julgue os itens subsequentes.

[1] Apesar de implementarem tecnologias distintas, todos os bancos de dados
NoSQL
apresentam em comum a implementação da tecnologia chave-valor.

Comentário: Sabemos que são cada solução NoSQL possui um modelo de armazenamento diferente, os quais dividimos em quatro categorias amplamente utilizadas no ecossistemaNoSQL: chave-valor, documento, família de colunas ou colunar, e grafos.

Gabarito: E

CAIU

na prova!

25. ANO: 2016 BANCA: CESPE CONCURSO: FUNPRESP CARGO: ESPECIALISTA ÁREA:
TECNOLOGIA DA INFORMAÇÃO (TI)

Com relação à forma como os dados são armazenados e manipulados no desenvolvimento de aplicações, julgue os itens a seguir.
[69] Em um banco de dados NoSQL do tipo grafo, cada arco é definido por um identificador único e expresso como um par chave/valor.
Comentários: Abaixo analisaremos cada uma das alternativas.

69. A alternativa vai exigir conhecimento sobre os modelos de armazenamento utilizados por bancos de dados NoSQL. Quando tratamos de bases de dados NoSQL podemos classifica-las em quatro diferentes tipos, dois deles são citados na questão:
Chave/valor (Key/Value): conhecidos como tabelas de hash distribuídas. Armazenam objetos indexados por chaves, e facilita a busca por esses objetos a partir de suas chaves.
Orientado a Grafos: diferente de outros bancos de dados NoSQL, esse está diretamente relacionado a um modelo de dados estabelecido, o modelo de grafos. A ideia desse modelo é representar os dados e/ou o esquema dos dados como grafos dirigidos, ou como estruturas que generalizem a noção de grafos. O modelo de grafos é aplicável quando "informações sobre a interconectividade ou a topologia dos dados são mais importantes, ou tão importante quanto os dados propriamente ditos". Possui três componentes básicos: os nós (são os vértices do grafo), os relacionamentos (são as arestas) e as propriedades (ou atributos)dos nós e relacionamentos.
Vejam que a questão mistura os dois conceitos o que torna a alternativa incorreta.

Gabarito: E

CAIU

na prova!

26. ANO: 2016 BANCA: CESPE CONCURSO: FUNPRESP CARGO: ESPECIALISTA ÁREA:
TECNOLOGIA DA INFORMAÇÃO (TI)

A respeito dos fundamentos e das principais tecnologias relacionadas à computação em nuvem, julgue os próximos itens.
[90] Hadoop e Elasticsearch são exemplos de tecnologias que permitem a computação em nuvem.
[91] A computação em nuvem permite o processamento de dados de maneira distribuída em máquinas com diferentes arquiteturas físicas.
Comentário: Vamos comentar cada uma das alternativas acima. Começando pela definição de
Hadoop e ElasticSearch.

O Hadoop é uma implementação de código aberto do paradigma de programação MapReduce.
MapReduce é um paradigma introduzido pelo Google para processar e analisar grandes conjuntos de dados. Os programas que são desenvolvidos nesse paradigma realizam o processamento paralelo de conjuntos de dados e podem, portanto, ser executados em diferentes servidores sem muito esforço. A razão para a escalabilidade desse paradigma é a natureza intrinsecamente distribuída do funcionamento da solução. Uma grande tarefa é dividida em várias pequenas tarefas que são então executadas em paralelo em máquinas diferentes e então combinadas para chegar à solução. Os exemplos de uso do Hadoop são analisar padrões de usuários em sites de e-commerce e sugerir novos produtos para os mesmos.
ElasticSearch é uma engine de busca open-source, amplamente distribuível,
facilmente escalável para uso empresarial ou pessoal. Acessível através de uma API extensa e bem elaborada, o ElasticSearch pode acionar pesquisas extremamente rápidas que suportam diversos tipos de integração.
90 Também conhecida no Brasil como computação nas nuvens ou computação em nuvem, a cloud computing se refere, essencialmente, à noção de utilizarmos, em qualquer lugar e independente de plataforma, as mais variadas aplicações por meio da internet com a mesma facilidade de tê-las instaladas em computadores locais. Dentro deste contexto, tantoHadoop quanto ElastichSearch são ferramentas que contribuem para a infraestrutura para provimento de serviços de computação na nuvem. Sendo assim alternativa encontra-se correta.
91. O uso das ferramentas citadas no item anterior vai permitir um grande paralelismo no processamento por meio da distribuição entre os diferentes nós ou hosts do sistema.Mais uma alternativa correta.
Gabarito: C C

