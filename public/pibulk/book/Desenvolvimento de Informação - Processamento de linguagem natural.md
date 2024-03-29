# Desenvolvimento de Informação - Processamento de linguagem natural

Índice

1) Machine Lerning Aplicado - PLN

Conteúdo da aula

Processamento de Linguagem Natural (PLN)

Processo de PLN

Semântica vetorial

Redução de dimensionalidade

Classificação de textos.

Modelagem de tópicos latentes.

Análise de sentimentos.

Conceitos complementares

Métricas de similaridade textual (similaridade do cosseno, distância euclidiana,
similaridade de
Jaccard, distância de Manhattan e coeficiente de Dice)

Aplicações de PLN

Questões Comentadas

Exercícios

Gabarito.

CAVALCANTI

PROFESSOR

CoNTEÚDo DA AULA

1.5 Noções de Processamento Natural de Linguagem. 1.6 Stop-words, stemização e n-grams.
1.7 TF-
IDF. 1.8 Modelagem de tópicos (LDA, NMF). 1.9 Word embeddings: CBOW e Skip Gram.

PRoCESSAMENTo DE LINGUAGEM NATURAL (PLN)

Para começar olhando para a PLN, vamos entender o que é a linguagem natural. Em termos simples,
é a linguagem que usamos para nos expressar. É um meio básico de comunicação. Para definir mais especificamente, a linguagem é um conjunto de protocolos mutuamente acordado envolvendo palavras/sons que usamos para nos comunicarmos. O uso da linguagem é sem dúvida a habilidade mais saliente que separa os humanos de outros animais.
Nesta era de digitalização e computação, tendemos a compreender a linguagem cientificamente.Isso ocorre porque estamos constantemente tentando fazer com que os objetos inanimados nos compreendam. Assim, tornou-se essencial desenvolver mecanismos pelos quais a linguagem pode ser alimentada para objetos inanimados, como computadores. O PLN nos ajuda a fazer isso.
Vejamos um exemplo. Você deve ter alguns e-mails em sua caixa de correio que foram marcados automaticamente como spam. Isso é feito com a ajuda de PLN. Aqui, um objeto inanimado- o serviço de e-mail - analisa o conteúdo dos e-mails, compreende e depois decide se esses e-mails precisam ser marcados como spam ou não.
PLN é uma área que se sobrepõe a outras. Surgiu em campos como inteligência artificial, linguística, linguagens formais e compiladores. Com o avanço das tecnologias de computação e o aumento da disponibilidade de dados, a forma como a linguagem natural está sendo processada mudou. Anteriormente, um sistema tradicional baseado em regras era usado para cálculos. Hoje, cálculos em linguagem natural são feitos usando aprendizado de máquina e técnicas de aprendizado profundo (deep learning).
O trabalho em PLN baseado em aprendizado de máquina começou na década de 1980. Durante a década de 1980,
avanços em várias disciplinas, como inteligência artificial, linguística,
linguagens formais e computação levaram ao surgimento de um assunto interdisciplinar chamado PLN.
Antes de avançarmos no assunto ... é importante perceber que análise de texto é diferente de PLN .

A análise de texto é o método de extrair percepções significativas e responder a perguntas a partir de dados de texto. Esses dados de texto não precisam ser uma linguagem humana. Vamos entender isso com um exemplo. Suponha que você tenha um arquivo de texto que contém suas chamadas de saída (ligações telefônicas que você fez) e dados de registro de SMS no seguinte formato:
Campo 01 Campo 02 Campo 03 Campo 04
Campo 05

Data Hora Ligação ou SMS

Telefone e nome da pessoa contactada. Se o número não está nos seus contatos o campo nome fica em branco
Duração da chamada em segundo, no caso de SMS o campo apresenta a mensagem de texto.
Na tabela anterior, os dois primeiros campos representam a data e a hora em que a chamada foi feita ou o SMS foi enviado. O terceiro campo representa o tipo de dados. Se os dados forem do tipo chamada, o valor desse campo será definido como voice_call.
Se o tipo de dados for sms, o valor deste campo será definido como sms. O quarto campo é para o número de telefone e o nome do contato. Se o número da pessoa não estiver na lista de contatos, o valor ficará em branco. O último campo é para a duração da chamada ou mensagem de texto. Se o tipo de dados for voice_call, o valor neste campo será a duração dessa chamada. Se o tipo de dados for sms, o valor neste campo será a mensagem de texto.
A figura a seguir mostra registros de dados de chamadas armazenados em um arquivo de texto:

Agora, os dados mostrados na figura anterior não são exatamente uma linguagem humana.
Mas contém várias informações que podem ser extraídas ao analisá-la. Algumas perguntas que podem ser respondidas olhando esses dados são as seguintes:
* Quantas saudações de Ano Novo foram enviadas por SMS no dia 1 de janeiro?

* Quantas pessoas foram contatadas cujo nome não consta da lista de contatos?

A arte de extrair percepções úteis de qualquer dado de texto pode ser chamada de análise de texto.
PLN, por outro lado, não se restringe apenas aos dados de texto. O reconhecimento e a análise de voz (fala) também estão sob o domínio do PLN. PLN pode ser amplamente categorizada em dois tipos: compreensão da linguagem natural (NLU - Natural Language Understanding) e Geração da linguagem natural (NLG - Natural Language Generation). Uma explicação adequada desses termos é fornecida da seguinte forma:
* NLU: NLU se refere a um processo pelo qual um objeto inanimado com poder de computação é capaz de compreender a linguagem falada.
* NLG : NLG refere-se a um processo pelo qual um objeto inanimado com poder de computação é capaz de manifestar seus pensamentos em uma linguagem que os humanos são capazes de entender.
Por exemplo, quando um humano fala com uma máquina, a máquina interpreta a linguagem humana com a ajuda do processo de NLU. Além disso, ao usar o processo NLG, a máquina gera uma resposta apropriada e a compartilha com o humano, tornando mais fácil para os humanos entenderem. Essas tarefas, que fazem parte da PNL, não fazem parte da análise de texto. A figura abaixo mostra as ações que são desempenhadas em um fluxo padrão, de alto nível, de um processamento de linguagem natural.
Entendimento da linguagem natural
Aprendizado de máquina
Geração de
Linguagem

Qual a política de devolução da loja?
Podemos devolver seu dinheiro até em 7 dias após a compra.
Processamento de Linguagem Natural

No nosso exemplo, a Carol precisa devolver um produto que comprou na Magalú. Para tal, ela quer saber quais as regras de devolução da empresa. Então, ela liga para a empresa, que possui uma central de atendimento eletrônico automatizada que utiliza PLN para tratar as ligações de clientes.A central recebe a pergunta da Carol questionando "qual seria a política de devolução da loja?" e faz um processamento inicial do que está sendo dito. Depois de traduzir o texto para linguagem formal,o nosso "robô" vai compreender o que está sendo dito e determinar qual a resposta correta para aCarol em linguagem formal. Mas a Carol não entende a linguagem formal da máquina,
esse resultado então precisa passar por uma geração de linguagem que vai devolver a resposta em formato adequada para a Carol. Perceba que o PLN é uma abordagem baseada em princípios para processar a linguagem humana. Trata-se de um subcampo da inteligência artificial (IA)que se refere a abordagens computacionais para processar, compreender e gerar a linguagem humana.
Processamento Compreensão Geração de

Aplicações de PNL

0 Processamento de Linguagem Natural é útil para empresas que buscam melhorar suas operações.Na verdade, grandes empresas que desejam rastrear e analisar milhares de interações com clientes podem se beneficiar do subconjunto de IA. Junto com o monitoramento de feedbacks, as empresas usam a PLN para automatizar o suporte e melhorar a experiência do usuário.
O reconhecimento de fala pode ser um dos aplicativos de PLN mais popular. Envolve o uso de processamento de linguagem natural para converter a linguagem falada em um formato legível por máquina. Além de ser útil em assistentes virtuais como o Alexa, a tecnologia de reconhecimento de voz possui algumas aplicações empresariais. Por exemplo, os programas de fala para texto (STT-speech to text) são úteis para transcrever chamadas e enviar e-mails. Outros aplicativos de PNLincluem tradução automática, análise de sentimento, detecção de palavras-chave, extração de texto e sumarização de texto.
A sumarização, em geral, é uma atividade bastante comum. Quando se narra um evento a uma pessoa, costuma-se fazer um resumo do que aconteceu, e não uma narração completa e detalhada.Inconscientemente, as pessoas estão sempre sumarizando. Muito frequentes também são os sumários escritos, como, por exemplo, notícias em jornais, artigos de revistas, resumo de textos científicos, entre muitos outros.
Os sumários produzidos a partir de textos são particularmente úteis, podendo servir como indexadores ou ser autocontidos. No primeiro caso, os sumários são lidos para descobrir qual é o assunto do texto-fonte correspondente e, caso seja de interesse, o leitor remete ao texto completo,para informar-se. No segundo caso, os sumários já são considerados informativos o suficiente e,portanto, o leitor pode dispensar o texto de origem e, ainda assim, apreender suas informações principais.
Devido a sua utilidade e aos avanços na área de
Processamento de Línguas Naturais (PLN), é de grande interesse a automação do processo de sumarização. A sumarização automática vem sendo objeto de estudo desde os primórdios da computação. Já no final da década de 50começaram a surgir alguns métodos estatísticos

Summary para extrair as sentenças principais de um texto. As pesquisas continuaram nas décadas seguintes.Em relação à forma de composição de sumarização, podemos classificar a sumarização como extrativa (quando selecionamos segmentos textuais inteiros) e abstrativa (quando realizamos operações de reescrita).
A sumarização extrativa gera um sumário selecionando os segmentos mais representativos(usualmente sentenças) dos textos-fonte, sem fazer nenhuma mudança nos segmentos.
A ideia desta abordagem é extrair as sentenças que contenham muita informação e novidade. Na seleção de sentenças mais relevantes, os métodos extrativos utilizam um mecanismo de ranqueamento para obter as sentenças com melhores pontuações, ou seja, as mais importantes. Entre os métodos mais utilizados temos: métodos baseados em grafos, baseados em aprendizado de máquina e baseados em informações estatísticas.
A sumarização abstrativa não apenas seleciona as sentenças dos textos-fonte, ela também analisa os documentos e automaticamente gera novas sentenças. Essa abordagem tenta produzir novos textos a partir dos fragmentos originais identificados como importantes. Com esta característica,esta abordagem pode solucionar o problema de falta de coesão da abordagem extrativa.
Hoje em dia, os modelos LSTM, BERT e Google's T5 transformer são utilizados em tarefas de sumarização abstrativa.
Abaixo vamos listar algumas aplicações de PLN em grau de complexidade crescente:

>

Verificação ortográfica
* á r
Recuperação de informação baseada em palavras chave b. j r
Modelagem de tópicos em texto(contexto)

r 1

Classificação de texto
* Análise de sentimento

* Detecção de idioma h á
Resposta de perguntas
Sumarização automática de texto
Agente de conversão de domínio fechado
Extração de informação
Traduçao automática de texto
Agente de conversão de domínio aberto
Uma das dificuldades encontradas em PLN é a ambiguidade sintática. Uma frase sintaticamente ambígua tem mais de uma interpretação de como a frase está estruturada. Você pode interpretar a frase de várias maneiras, dependendo da estrutura da frase em que você acredita. Antes de continuarmos, vamos fazer uma questão sobre o assunto:
1. Sobre o processamento de linguagem natural (PLN) assinale a alternativa correta.

a) O processamento é sempre feito sobre uma linguagem formal, como o português.

b) A questão da ambiguidade semântica não deve ser levada em consideração visto que é possível encontrar o significado das frases através do contexto.
c) O PLN pode ser dividido em três grandes ações o processamento, a compreensão do texto e a geração de resposta.
d) A sumarização de texto abstrativa é mais fácil de ser aplicada sobre um texto do que a extrativa.
e) Inteligência artificial é um subconjunto do processamento de linguagem natural.
Comentário: Vamos comentar cada uma das alternativas:

a) (Errada). Português é um exemplo de linguagem natural.

b) (Errada). A ambiguidade semântica deve ser levada em consideração.

c) (Certo). Essas são as 3 grandes ações do PLN: Processamento, compreensão e geração de resposta.
d) (Errada). A sumarização abstrativa é mais complexa do que a extrativa.

e) (Errada). O processamento de linguagem natural é um subconjunto da inteligência artificial.

Gabarito: C

PRoCESSo DE PLN

* ' 1

*? 1
r

Aquisição de

Limpeza de

- Pré-

Engenharia de

Monitoramento e atualização do modelo
Deployment Avaliação

» *

Modelagem

A primeira etapa no processo de desenvolvimento de qualquer sistema de PLN é coletar dados relevantes para a tarefa dada. Mesmo que estejamos construindo um sistema baseado em regras,ainda precisamos de alguns dados para projetar e testar nossas regras. Os dados que obtemos raramente são limpos, e é aqui que a limpeza de texto entra em jogo.
Após a limpeza, os dados de texto costumam ter muitas variações e precisam ser convertidos em um formato canônico. Isso é feito na etapa de pré-processamento. Isso é seguido pela engenharia de recursos, onde localizamos indicadores que são mais adequados para a tarefa em questão. Esses indicadores são convertidos em um formato compreensível por algoritmos de modelagem.
Em seguida, vem a fase de modelagem e avaliação, onde construímos um ou mais modelos e os comparamos e contrastamos usando uma(s) métrica(s) de avaliação relevante(s). Uma vez escolhido o melhor modelo entre os avaliados, avançamos no sentido de implantar este modelo na produção.Por fim, monitoramos regularmente o desempenho do modelo e, se necessário, o atualizamos para manter sua atuação.
Queria aproveitar que estamos falando do processo e detalhar um pouco as ações de pré-processamento. É um assunto que já foi objeto de provas anteriores e é um tópico que encontra forte interseção com a mineração de texto. A figura abaixo apresenta um conjunto de ações, dividida em etapas, que podem ser aplicadas aos pré-processamento em softwares de PLN.
Preliminares

Segmentação de sentenças
Passos
Frequentes

(Básicos)

Remoção de stop words
Stemming

Outros Passos

Processamento avançado
'

Tokenização de palavras
Lemmatization

Remoção de digitos e pontuação
Lowercasing

Parsing

- -

Coreference
Resolution

Embora nem todas as etapas sejam seguidas em todos os pipelines de PLN que encontramos, as duas primeiras são mais ou menos vistas em todos os lugares. Vamos dar uma olhada no que cada uma dessas etapas executa dentro do processo.
Preliminares

O software de PLN normalmente analisa o texto dividindo-o em palavras
(tokens) e sentenças.
Portanto, qualquer pipeline de PLN deve começar com um sistema confiável para dividir o texto em sentenças (segmentação de sentenças) e, posteriormente, dividir uma sentença em palavras
1 A transliteração/Translitaration é o processo de transferência de uma palavra do alfabeto de um idioma para outro. Atransliteração ajuda as pessoas a pronunciar palavras e nomes em línguas estrangeiras.

(tokenização de palavras). Superficialmente, essas tarefas parecem simples e você pode se perguntar por que precisam de um tratamento especial.
Como regra simples, podemos fazer segmentação de frases dividindo o texto em sentenças baseadas nos pontos finais e pontos de interrogação. No entanto, podem haver abreviaturas,descrições de endereços (Dr., Sr., etc.) ou reticências (...) que podem infringir a regra simples.Felizmente, não precisamos nos preocupar em como resolver esses problemas, já que a maioria das bibliotecas dePLN vem com alguma forma de divisão de frases e palavras implementada. Uma biblioteca comumente usada é o Natural Language Tool Kit (NLTK).
Passos Frequentes

Digamos que estejamos desenvolvendo um software que identifica a categoria de um artigo de notícias como política, esportes, negócios e outros. Suponha que temos um bom segmentador de frases e um tokenizador de palavras. Nesse ponto, teríamos que começar a pensar sobre que tipo de informação é útil para desenvolver uma ferramenta de categorização. Algumas das palavras mais usadas em inglês, como a, an, the, of, in, etc., não são particularmente úteis para essa tarefa, pois não carregam nenhum conteúdo por conta própria para separar o texto em uma das quatro categorias. Essas palavras são chamadas de palavras de parada ou stop words e são normalmente(embora nem sempre) removidas de análises adicionais em tais cenários de problema.

No entanto, não existe uma lista padrão de palavras de parada em inglês. Existem algumas listas populares (NLTK tem uma, por exemplo), entretanto o que pode ser visto como uma palavra de parada pode variar dependendo do contexto que estamos trabalhando.
Stopwords são muito utilizadas em um idioma e desempenham um papel importante na formação de uma sentença, mas raramente contribuem para o significado dessa sentença. Palavras que se espera que ocorram em 80 por cento ou mais dos documentos em uma coleção costumam ser chamadas de stopwords, e elas se tornam potencialmente inúteis. Por serem muito comuns e devido à função dessas palavras, elas não contribuem muito para a relevância de um documento para uma pesquisa. Alguns exemplos (em inglês) são palavras como the, of, to, a, and, in,said,for, that, was,
on, he, is, with, at, by e it.

Segundo o Navathe, a remoção de stopwords de um documento deve ser realizada antes da indexação. Artigos, preposições, conjunções e alguns pronomes geralmente são classificados como stopwords. As consultas também devem ser pré-processadas para remoção de stopword antes do processo de recuperação real. A remoção de Stopwords resulta na eliminação de possíveis índices faIsos, reduzindo assim o tamanho de uma estrutura de índice em cerca de 40 por cento ou mais.
Da mesma forma, em alguns casos, letras maiúsculas ou minúsculas podem não fazer diferença para o problema. Portanto, todo o texto deve ser transformado para letras minúsculas (ou maiúsculas,embora minúsculas seja mais comum). Também chamado de Case Folding, é o processo de converter todos os caracteres de um documento no mesmo tipo de letra - ou todas maiúsculas ou minúsculas (lowercasing). Isso tem a vantagem de acelerar comparações no processo de indexação.
Remover pontuação e/ou números também é uma etapa comum para muitos problemas de PLN,
como classificação de texto, recuperação de informações e análise de mídia social.

Stemming e lemmatization

A raiz ou radical de uma palavra é definida como a palavra obtida depois de remover o sufixo e o prefixo de uma palavra original. Por exemplo, 'comput' é a palavra raiz para computador,computação e computadorizado. Esses sufixos e prefixos são muito comuns no idioma português,para dar suporte à noção de verbos, tempos e formas no plural. As raízes reduzem as diferentes formas da palavra formada por inflexão (devido a plurais e tempos) e derivação a uma raiz comum.
consign consigning consign consignment
°°$

ooob consign

Figura 1 - Exemplo de Stemming

O processo de stemming é realizado considerando cada palavra isoladamente e tentando reduzi-la a sua provável palavra raiz. Isto tem a vantagem de eliminar sufixos, indicando formas verbais e/ou plurais; entretanto, algoritmos de stemming empregam linguística e são dependentes do idioma. Os algoritmos de stemming correntes não costumam usar informações do contexto para determinar o sentido correto de cada palavra, e realmente essa abordagem parece não ajudar muito.
Casos em que o contexto melhora o processo de stemming não são muito frequentes, e a maioria das palavras pode ser considerada como apresentando um significado único. Os erros resultantes de uma análise de sentido imprecisa das palavras, em geral, não compensam os ganhos que possam ser obtidos pelo aumento de precisão do processo de stemming.
Existem, porém, outros tipos de erros que devem ser observados e controlados durante a execução do stemming. Os erros mais comuns associados ao processo de stemming podem ser divididos em dois grupos:
* Overstemming: acontece quando a cadeia de caracteres removida não era um sufixo,
mas parte do stem. Isto pode resultar na conflação de termos não relacionados.

* Understemming-. acontece quando um sufixo não é removido. Isto geralmente causa uma falha na conflação de palavras relacionadas
Lemmatização é o processo de mapear todas as diferentes formas de uma palavra em sua palavra base, ou lema. Embora isso pareça próximo da definição de stemming, eles são, na verdade,diferentes. Por exemplo, o adjetivo "better" em inglês, quando passa pelo processo de stemming,permanece o mesmo. No entanto, na lematização, isso deve se tornar "good", conforme mostrado na figura abaixo. A lematização requer mais conhecimento linguístico, e modelar e desenvolver lematizadores eficientes continua sendo um problema aberto na pesquisa de PNL até agora.
Stemming adjustable-> adjust formality -> formaliti formaliti -> formal airliner -> airlin
Lemmatization was -> (to) be better-> good meeting->meeting
Figura 2 - Diferença entre Stemming e Lemmatization

Marcação PoS (part of Speech) ou rotulação de partes do discurso, refere-se a classes gramaticais.
A marcação PoS se refere ao processo de marcar palavras dentro das frases em suas respectivas classes gramaticais e, finalmente, rotulá-las. Extraímos tokens de partes de um discurso que constituem uma frase, para que possamos filtrar os PoS que são de interesse e analisá-los. Por exemplo, se olharmos para a frase "O céu é azul", obteremos quatro tokens - "O","céu", "é" e "azul"

- com a ajuda da tokenização. Agora, usando o tagger PoS, identificamos classes gramaticais para cada palavra / token. Isso terá o seguinte formato:
[('O', 'DT'), ('céu', 'NN'), ('é', 'VBZ'), ('azul1, 'JJ')]

Onde:

DT = determinante

NN = substantivo, comum, singular

VBZ = verbo, presente, 3g pessoa do singular
JJ = Adjetivo

Resumindo, o manuseio de arquivos texto apresenta alguns desafios. O primeiro deles envolve o formato dos textos com nenhuma ou pouca estruturação, o que dificulta a utilização imediata. Um outro desafio diz respeito ao tamanho dos arquivos em formato texto, comumente da ordem de milhares de palavras ou termos. Além disso, muitas dessas palavras são repetidas,expressam o mesmo significado ou possuem significado irrelevante.
As situações mencionadas acima, assim como outras, encontradas quando se lida com dados textuais, devem ser trabalhadas e resolvidas para viabilizar o melhor uso de arquivos texto em primeira instância e em segunda aumentar a eficiência de atividades executadas a posteriori. Além de promover uma redução dimensional, esta etapa tenta identificar similaridades em função da morfologia ou do significado dos termos, de modo a agrupar suas contribuições.
Uso do Thesaurus (ou dicionário)

Um dicionário pode ser definido como um vocabulário controlado que representa sinônimos,hierarquias e relacionamentos associativos entre termos para ajudar os leitores a encontrar a informação de que eles precisam. A pergunta é: para que eu quero montar um dicionário de palavras neste contexto?
Embora isto pareça estranho, é apenas uma questão de se entender para que serve um thesaurus.O valor do thesaurus vem justamente dos problemas inerentes à procura e indexação da linguagem natural. Usuários diferentes definem a mesma query (consulta) usando termos diferentes. Para resolver este problema, um thesaurus mapeia termos variantes -sinônimos, abreviações,
acrônimos, e ortografias alternativas - para um termo preferido único para cada conceito.

Para processos de indexação de documentos, o thesaurus informa que termos índices devem ser usados para descrever cada conceito. Isto reforça a consistência da indexação. Essa etapa de pré-processamento auxilia no fornecimento de um vocabulário padrão para indexação e pesquisa. Ouso de um tesauro, também conhecido como uma coleção de sinônimos, tem um impacto substancial a revocação2 de consulta dos sistemas de informação. Esse processo pode ser complicado porque muitas palavras possuem significados diferentes em variados contextos.
Um thesaurus pode também representar a riqueza dos relacionamentos associativos e hierárquicos.Usuários podem expressar a necessidade de informação com um nível de especificidade mais restrito ou mais amplo que o usado pelo indexador para descrever os documentos. Omapeamento de relacionamentos hierárquicos endereça este problema. Veja figura abaixo representando um tipo de relacionamento hierárquico.
Figura 3 - Figura representando a hierarquia da função biológica.

2 A revocação é definida como o número de documentos relevantes recuperados por uma pesquisa dividido pelo número total de documentos relevantes existentes.
SEMÂNTICA vEToRIAL

Muitos algoritmos de aprendizado de máquina e quase todas as arquiteturas de aprendizado profundo não são capazes de processar strings ou texto simples em sua forma bruta. Em um sentido amplo, eles requerem valores numéricos como entradas para realizar qualquer tipo de tarefa, como classificação, regressão e agrupamento. Além disso, é imperativo extrair algum conhecimento a partir da enorme quantidade de dados que está presente no formato de texto e construir quaisquer aplicações úteis.
Resumindo, podemos dizer que, para construir qualquer modelo em aprendizado de máquina,
os dados de entrada precisam estar na forma numérica porque os modelos não entendem dados de texto ou imagem diretamente como os humanos. Por exemplo, para usar redes neurais em seu aplicativo PLN, você precisa converter unidades linguísticas em números, como vetores.
Para converter os dados de texto em dados numéricos, precisamos de algumas formas inteligentes que são conhecidas como vetorização ou, no mundo do PLN, são conhecidas como Word embedding. Portanto, a vetorização ou incorporação de palavras é o processo de conversão de dados de texto em vetores numéricos. Posteriormente, esses vetores são usados para construir vários modelos de aprendizado de máquina. Temos diferentes maneiras de converter os dados do texto em vetores numéricos.
Ok! Você já entende que transformar os textos em vetores numéricos é importante.
Agora, gostaria de dar um passo para trás e apresentar o fluxo para resolução de um problema de PLNdetalhando um pouco mais as grandes etapas que vimos anteriormente:
Texto bruto [raw] Limpeza e pré-
processamento

Tokenização -
palavras ou outra unidade linguística
Avaliação sRepresentação matemática das unidades linguístcas s.
Nesta seção, daremos uma olhada nos diferentes métodos de representação de texto como um vetor numérico. Com relação ao quadro mais amplo de qualquer problema de PLN, o escopo desta seção é representado pela caixa pontilhada na figura acima.
A representação de recursos é uma etapa comum em qualquer projeto de ML, sejam com dados em texto, imagens, vídeos ou voz. No entanto, a representação de recursos para texto costuma ser muito mais complexa em comparação com outros formatos de dados. Para entender isso,vamos examinar alguns exemplos de como outros formatos de dados podem ser representados numericamente. Primeiro, considere o caso das imagens.
Digamos que queremos construir um classificador que possa distinguir imagens de gatos de imagens de cachorros. Agora, para treinar um modelo de ML para realizar essa tarefa,precisamos alimentá-
lo com imagens (rotuladas). Como alimentamos imagens em um modelo de ML? A forma como uma imagem é armazenada em um computador é na forma de uma matriz de pixels, onde cada célula [i,j] na matriz representa o pixel i, j da imagem. O valor real armazenado na célula
[i, j] representa a intensidade do pixel correspondente na imagem, conforme mostrado na figura abaixo. Esta representação de matriz mostra com precisão a imagem completa.
« JJ ÍT « is oo io oo n oi os n so « os
1S 10 ** 10 1T 01 10 SI «0 BT 1? 10 10 11 «» 10 01 S4 <2 OO

01 11 11 M SS « 11 01 11 11 10 0? M 04 M OS 11 11 1* «1

52 70- *4 24 04 40 11 42 4» 24 44 44 01 22 24 1*1 27 02 34 >1

22 31 14 71 41 47 43 8* 41 42 34 54 22 40 40 28 44 33 13 SO

24 47 32 43 49 03 49 02 44 75 33 43 79 34 t4 20 35 17 12 30

32 49 li 29 44 23 <7 10 24 >9 40 <7 59 94 70 44 l* 39 44 70

47 24 20 49 PJ 42 12 20 W 43 94 39 43 04 40 91 44 49 94 21

24 99 5t 09 44 7> 99 24 97 17 79 79 94 93 14 99 34 99 43 7f

21 94 23 09 79 00 74 44 20 45 35 14 OO 41 » 97 34 31 33 95

79 17 53 28 » 75 31 47 15 94 03 90 04 42 14 14 09 83 84 92

14 39 05 42 94 35 31 47 55 58 89 24 OO 17 54 24 34 29 95 37

94 34 OO 48 35 71 99 0? 05 44 44 37 44 40 21 58 81 54 17 55

19 90 91 48 05 94 «7 49 28 73 92 13 94 32 17 77 04 99 85 40

04 92 OS 83 97 39 99 14 07 97 57 32 14 24 24 79 33 27 98 44

99 34 48 97 57 <7 20 72 03 44 33 C7 44 » 12 32 C3 93 33 49

04 42 14 73 >e 75 39 11 24 94 72 19 09 44 29 32 40 42 74 34

20 49 34 41 72 30 23 99 34 42 99 <9 92 47 4» 95 74 04 34 14

20 73 33 29 79 31 90 01 74 31 49 71 49 94 91 34 23 57 Q5 54

01 70 54 71 93 81 84 49 14 92 33 49 41 43 52 01 99 19 47 43

Figura 4 - O que você vê em uma foto (esquerda) x o que o computador vê (direita)

OKÜ Mas como acontece a "tradução" da imagem em números? Geralmente usamos informações armazenadas nos pixels. Então, como você acha que deve ser feita a transformação de texto em números? ... vamos fazer algo sobre o conjunto de palavras e outros elementos do texto. Algo denominado word embedding ... Um word embedding (ou incorporação de palavras)é uma representação vetorial com valores reais de uma palavra. Se você achar o conceito de vetores intimidante, pense nele como uma matrize unidimensional de números, como o seguinte:
vec("cat") = [0.7, 0.5, 0.1]

vec("dog") = [0.8, 0.3, 0.1]

vec("pizza") = [0.1, 0.2, 0.8]

Como cada array/lista contém três elementos, você pode plotá-los como pontos em um espaço 3-Dcomo na figura abaixo. Observe que as palavras semanticamente relacionadas ("gato" e
"cachorro")
são colocadas mais perto uma das outras.

Figura 5 - Embeddings de palavras em um espaço 3-D

Neste momento, podemos observar a definição de semântica vetorial: refere-se ao conjunto de métodos de PLN que objetivam aprender as representações de palavras com base em propriedades de distribuição de palavras em um grande corpus.
Isso nos leva ao conceito de similaridade distributiva que é a ideia de que o significado de uma palavra pode ser entendido a partir do contexto em que a palavra aparece. Isso também é conhecido como conotação: o significado é definido pelo contexto. E se opõe à denotação que estabelece o significado literal de qualquer palavra.
E quais seriam essas propriedades de distribuição? Vejamos um esquema:

Hipótese distributiva

Representação distribucional
Representação distribuída
Palavras que ocorrem em contextos semelhantes têm significados semelhantes. Por exemplo, as palavras em inglês "cachorro" e "gato" ocorrem em contextos semelhantes. Assim, de acordo com a hipótese distributiva,deve haver uma forte semelhança entre os significados dessas duas palavras.
Refere-se a esquemas de representação obtidos com base na distribuição de palavras a partir do contexto em que as palavras aparecem. Esses esquemas são baseados em hipóteses distributiva.
Esquemas de representação distribuída comprimem significativamente a dimensionalidade. Isso resulta em vetores que são compactos (ou seja, de baixa dimensão) e densos (ou seja, quase nenhum zero). 0 espaço vetorial resultante é conhecido como representação distribuída.
Embedding

Um mapeamento entre o espaço vetorial proveniente da representação distribucional e o espaço vetorial proveniente da representação distribuída.
i * Conjunto de métodos de PLN que objetivam aprender as

Como já falamos, embeddings de palavras não são apenas importantes, mas essenciais para usar redes neurais com o intuito de resolver tarefas de PLN. As redes neurais são modelos de computação puramente matemáticos que podem lidar apenas com números. Elas não podem fazer operações simbólicas, como concatenar duas strings ou conjugar um verbo com o pretérito, a menos que esses itens sejam todos representados por números e operações aritméticas. Por outro lado,quase tudo na PLN, como palavras e rótulos, é simbólico e discreto. É por isso que você precisa criar uma ponte entre esses dois mundos, e usar embeddings é uma maneira de fazer isso. Observe a figura a seguir para uma visão geral sobre como usar embeddings de palavras para um aplicativo PLN.
Prediction

((

NLP

model

Training data

C° 0 0 °j) (<.° ° o °j) 0 0 JX

Large text data

Words

Figura 6 - Usando embeddings de palavras com modelos de PLN

Antes de explorarmos como calcular embeddings de palavras a partir de grandes dados textuais,gostaria de apresentar os elementos básicos da linguagem: caracteres, palavras e frases.

Caracteres, palavras e frases.

Um caractere (também chamado de grafema em linguística) é a menor unidade de um sistema de escrita. Em português, "a", "b" e "z" são caracteres. Os caracteres não carregam necessariamente um significado por si. Um caractere típico em muitos idiomas pode ser representado por um único número no código Unicode. Muitos idiomas usam uma combinação de mais de um ponto de códigoUnicode (por exemplo, acentos) para representar um único caractere. Sinais de pontuação,
como

(ponto final), "," (vírgula) e "?" (ponto de interrogação), também são caracteres.

Uma palavra é a menor unidade em um idioma que pode ser pronunciada independentemente e que geralmente carrega algum significado. Em português, "concurso", "Petrobras" e"Rio" são palavras. Na maioria dos idiomas escritos que usam o alfabeto latino, as palavras geralmente são separadas por espaços ou sinais de pontuação. Em alguns idiomas, como chinês, japonês e tailandês,
no entanto, as palavras não são explicitamente delimitadas por espaços e exigem uma etapa de pré-processamento chamada segmentação de palavras para identificar as palavras em uma frase.

Um conceito intimamente relacionado a uma palavra em PLN é um token. Um token é uma sequência de caracteres contíguos que desempenham uma determinada função em uma linguagem escrita. A maioria das palavras ("maçã", "banana", "zebra") também são tokens quando escritas. Os sinais de pontuação, como o ponto de exclamação ("!"), são tokens, mas não palavras,porque você não pode pronunciá-los isoladamente. Palavras e token são frequentemente usados alternadamente no PLN. Na verdade, quando você vê "palavra" no texto da PLN,geralmente significa
"token", porque a maioria das tarefas da PLN lida apenas com texto escrito que é processado de forma automática. Os tokens são a saída de um processo denominado tokenização, que explicarei com mais detalhes a seguir.
Outro conceito intimamente relacionado é o morfema. Um morfema é a menor unidade de significado em um idioma. Uma palavra típica consiste em um ou mais morfemas. Por exemplo,"maçã" é uma palavra e um morfema. "Maçãs" é uma palavra composta de dois morfemas,
"Maçã"
e "-s", que é usada para significar que o substantivo está no plural. O português contém muitos outros morfemas, incluindo "-ão," "-ismo," "contra-" e "ante-". O processo de identificação de morfemas em uma palavra ou frase é chamado de análise morfológica, e tem uma ampla gama de aplicações de PLN/linguística, mas isso está fora do escopo desta aula.
Uma frase é um grupo de palavras que desempenham um determinado papel gramatical. Por exemplo, "o Eduardo foi aprovado na Petrobras". O conceito de frase pode ser usado com certa liberalidade no PLN para significar qualquer grupo de palavras. Por exemplo, em muitas literaturas e tarefas de PLN, palavras como "Los Angeles" são tratadas como frases, embora,linguisticamente falando, estejam mais próximas de uma palavra.
Os conceitos apresentados acima podem ser visualizados na figura abaixo, que apresenta exemplos no idioma inglês.
Characters Words Morphemes
A b q . brown dog over brown jump -s

The quick brown fox jumps over the lazy dog.

The quick brown fox the lazy dog quick brown brown fox jumps
Tokens Phrases Word n-grams

Figura 7 - Blocos de construção do linguagem usados em PLN

N-grams

Finalmente, você pode encontrar o conceito de n-gramas na PLN. Um n-grama é uma sequência contígua de uma ou mais ocorrências de unidades linguísticas, como caracteres e palavras. Por exemplo, um n-grama de palavra é uma sequência contígua de palavras, como "Petrobras"(uma palavra), "concurso Petrobras" (duas palavras), "tomates verdes fritos" (três palavras).Da mesma forma, um n-grama de caractere é conjunto de caracteres, como "P" (um caractere), "PE"(dois caracteres), "PET" (três caracteres) e assim por diante. Um n-grama de tamanho 1(quando n = 1) é chamado de unigrama. N-gramas de tamanho 2 e 3 são chamados de bigramas e trigramas,respectivamente.

Os n-gramas de palavras costumam ser usadas como proxies para frases em PLN, porque se você enumerar todos os n-gramas de uma frase, elas geralmente contêm unidades linguisticamente interessantes que correspondem a frases como "Los Angeles" e "alçar voo". De forma semelhante,usamos n-gramas de caracteres quando queremos capturar unidades de subpalavras que correspondem a morfemas. No PLN, quando você vê "n-gramas" (sem um qualificador), eles costumam ser n-gramas de palavras.
Na prática, usamos n-gramas e as probabilidades de ocorrências de certas palavras em certas sequências pode melhorar as previsões dos sistemas de autocompletar. Da mesma forma,usamos
PLN e n-gramas para treinar robôs assistentes pessoais baseados em voz. Por exemplo,
usando um modelo de treinamento de 3-gramas ou trigramas, um bot será capaz de entender a diferença entre frases como "qual é a temperatura?" e "definir a temperatura".
Modelo de espaço vetorial (Vectorial Space Model - VSM)

Em PLN, representaremos unidades de texto (caracteres, fonemas, palavras, frases,
sentenças,
parágrafos e documentos) com vetores de números, isso é conhecido como modelo de espaço vetorial (VSM). É um modelo algébrico simples usado extensivamente para representar qualquer conteúdo em texto. VSM é fundamental para muitas operações de recuperação de informação,desde a pontuação de documentos em uma consulta até a classificação de documentos. É
um modelo matemático que representa unidades de texto como vetores. Na forma mais simples,são vetores de identificadores, como números de índice em um vocabulário de corpus. Nessa configuração, a maneira mais comum de calcular a similaridade entre dois textos é usando a similaridade do cosseno: o cosseno do ângulo entre seus vetores correspondentes. O cosseno de 0o é 1 e o cosseno de 180° é -1, perceba que o cosseno diminui monotonicamente3 de 0o para 180°.Dados dois vetores, A e B, cada um com n componentes, a similaridade entre eles é calculada da seguinte forma:
similaridade = cos(0) =

A * B

IMIIIIBII

3 Uma função é considerada monotônica quando os valores de entrar e de saída de uma função seguem uma ordem (direta ou inversa). No caso, quando o cosseno aumenta, de 0 a 180, o valor reduz de 1 até -1.
onde A, e 8/ são os componentes dos vectores A e B, respectivamente.

Vamos tentar melhorar um pouco as coisas ... estou sentido que estamos indo muito para o lado matemático da coisa ... gostaria de usar uma abordagem mais intuitiva. Vejamos um exemplo:
Vamos começar com uma ideia básica de representação de texto: mapeie cada palavra no vocabulário (V) do corpus do texto para um ID único (valor inteiro) e, em seguida,represente cada frase ou documento no corpus como um vetor V-dimensional. Como operacionalizamos essa ideia?Para entender isso melhor, vamos pegar um corpus com apenas quatro documentos - Dl,
D2 , D3 ,
D4 - como exemplo.

Dl Cachorro morde homem.
D2 Homem morde cachorro.
D3 Cachorro come carne.

D4 Homem come comida.

Considerando o texto em letras minúsculas e ignorando a pontuação, o vocabulário deste corpus é composto por seis palavras: [cachorro, morde, homem, come, carne, comida]. Podemos organizar o vocabulário em qualquer ordem. Neste exemplo, simplesmente pegamos a ordem em que as palavras aparecem no corpus. Cada documento neste corpus agora pode ser representado como um vetor de tamanho seis. Assumiremos que o texto já foi pré-processado (letras minúsculas, pontuação removidas) e tokenizado (string de texto dividida em tokens). Começaremos com a codificação one-hot. O que é isso? Calma! Eu explico ...

Na codificação one-hot, cada palavra w no vocabulário do corpus recebe um ID de inteiro único Wid que está entre 1 e |V|, onde V é o conjunto do vocabulário do corpus. Cada palavra é então representada por um vetor binário V-dimensional de Os e ls. Isso é feito por meio de um vetor de dimensão | V| preenchido com zero em todas as posições, exceto quando o índice for igual ao inteiroWid. Neste índice, simplesmente colocamos um 1. A representação de palavras individuais é então combinada para formar uma representação de frase.
Vamos entender isso por meio do nosso corpus de exemplo. Primeiro mapeamos cada uma das seis palavras para IDs únicos: cachorro = 1, morde = 2, homem = 3, carne = 4, comida =5, come = 6.
Vamos considerar o documento Dl: "cachorro morde homem". De acordo com o esquema, cada palavra é um vetor de seis dimensões. Cachorro é representado como [10 0 0 0 0], já que a palavra"cachorro" é mapeada para ID 1. Morde é representado como [0 1 0 0 0 0] e assim por diante. Desta fomra, Dl é representado como [[100000] [010000] [001000]]. D4 é representado como [[0
010 0] [000010] [000001]]. Outros documentos do corpus podem ser representados de forma semelhante. Vamos organizar isso em uma tabela.
Palavra = Wid Vetor binário Doc Representação dos documentos (One
Hot)
Cachorro = 1 [10 0 0 0 0] Dl [[1 0 0 0 0 0] [0 1
0 0 0 0] [0 0 1 0 0 0]]

Morde = 2 [010000] D2 [[0 0 1 0 0 0] [0
1 0 0 0 0] [1 0 0 0 0 0]]

Homem = 3 [001000] D3 [[1 0 0 0 0 0] [0 0
0 0 0 1] [0 0 0 1 0 0]]

Carne = 4 [000100] D4 [[0 0 1 0 0 0] [0
0 0 0 0 1] [0 0 0 0 1 0]]

Comida = 5 [000010]

Come = 6 [00000 1]

Figura 8 - Tabela da representação One-Hot

Agora que entendemos o esquema, vamos discutir alguns de seus prós e contras. Do lado positivo,a codificação one-hot é intuitiva de entender e direta de implementar. No entanto, ele sofre de algumas deficiências:
* O tamanho de um vetor one-hot é diretamente proporcional ao tamanho do vocabulário, e a maioria dos corporas do mundo real tem grandes vocabulários. Isso resulta em uma representação esparsa em que a maioria das entradas nos vetores são zeros, tornando-se computacionalmente ineficiente para armazenar, computar e aprender.
* Esta representação não fornece uma representação de comprimento fixo para o texto, ou seja, se um texto contém 10 palavras, você obtém uma representação mais longa do que um texto com 5 palavras. Para boa parte dos algoritmos de aprendizagem, precisamos que os vetores de características tenham o mesmo comprimento.
* Ele trata as palavras como unidades atômicas e não tem noção de (des)
similaridade entre as palavras. Por exemplo, considere três palavras: executar, correr e maçã. Executar e correr têm significados semelhantes em oposição a correr e maçã. Mas se pegarmos seus respectivos vetores e calcularmos a distância euclidiana entre eles, eles estão todos igualmente separados. Assim, semanticamente, eles são muito pobres em captar o significado da palavra em relação a outras palavras.
* Digamos que treinamos um modelo usando nosso corpus de exemplo. Em tempo de execução, recebemos uma frase: "homem come frutas". Os dados de treinamento não incluem "fruta" e não há como representá-lo em nosso modelo. Isso é conhecido como problema fora do vocabulário. Um esquema de codificação one-hot não pode lidar com esse problema.
Enfim, atualmente, o esquema de codificação one-hot raramente é usado. Algumas dessas deficiências podem ser resolvidas pela abordagem do saco de palavras descrita a seguir.
Saco de palavras (BoW - Bag of Words) é uma técnica clássica de representação de texto que tem sido usada comumente na PLN, especialmente em problemas de classificação de texto. Aideia-
chave por trás disso é a seguinte: representar o texto em análise como uma bolsa
(coleção) de palavras, ignorando a ordem e o contexto. A intuição básica por trás disso é que ele assume que o texto pertencente a uma determinada classe no conjunto de dados é caracterizado por um conjunto único de palavras. Se duas partes do texto tiverem quase as mesmas palavras, então elas pertencem à mesma bolsa (classe). Assim, ao analisar as palavras presentes em um trecho de texto, pode-se identificar a classe a que pertence.
Semelhante à codificação one-hot, a BoW mapeia palavras para IDs inteiros exclusivos entre 1 e |V|.Cada documento do corpus é então convertido em um vetor de |V| dimensões onde no /
ésimo componente do vetor, i = Wid, é simplesmente o número de vezes que a palavra w ocorre no documento, ou seja, simplesmente pontuamos cada palavra em V por sua contagem de ocorrências no documento.
Assim, para o nosso corpus de exemplo, onde as palavras IDs são cachorro = 1, morde
= 2, homem

= 3, carne = 4, comida = 5, come = 6, Dl torna-se [1 1 1 0 0 0]. Isso ocorre porque as três primeiras palavras do vocabulário apareceram exatamente uma vez em Dl e as três últimas não apareceram.D4 torna-se [0 0 1 0 1 lj.

Palavra = Wid Vetor binário Doc Representação dos documentos
(BoW)
Cachorro = 1 [10000 0] Dl
[[1 1 1000]]

Morde = 2 [010000] D2
[[1 1 1000]]

Homem = 3 [001000] D3
[[100 110]]

Carne = 4 [000100] D4
[[00 10 1 1]]

Comida = 5 [000010]

Come = 6 [00000 1]

Vejamos algumas das vantagens dessa codificação:

* Como a codificação one-hot, o BoW é bastante simples de entender e implementar.

* Com esta representação, documentos com as mesmas palavras terão suas representações vetoriais mais próximas entre si no espaço euclidiano em comparação com documentos com palavras completamente diferentes. A distância entre Di e Ü2Ó 0 em comparação com a distância entre Di e D 4, que é 2. Perceba que o espaço vetorial resultante do esquema BoWcaptura a semelhança semântica dos documentos. Portanto, se dois documentos tiverem vocabulário semelhante, eles estarão mais próximos um do outro no espaço vetorial e vice-versa.

* Temos uma codificação de comprimento fixo para qualquer frase de comprimento arbitrário.

No entanto, ele também tem suas desvantagens:

* O tamanho do vetor aumenta com o tamanho do vocabulário. Portanto, a dispersão continua a ser um problema. Uma maneira de controlá-la é limitando o vocabulário a um número n das palavras mais frequentes.
* Não captura a semelhança entre palavras diferentes que significam a mesma coisa.
Digamos que temos três documentos: "Eu corro", "Eu corri" e "Eu comi". Os vetores BoW de todos os três documentos estarão igualmente separados.
* Essa representação não tem como lidar com palavras fora do vocabulário (ou seja,
palavras novas que não foram vistas no corpus).
* Como o nome indica, é um "saco" de palavras - as informações sobre a ordem das palavras se perdem nessa representação. Ambos, Di e D2, terão a mesma representação neste esquema.
No entanto, apesar dessas deficiências, devido à sua simplicidade e facilidade de implementação,BoW é um esquema de representação de texto comumente usado, especialmente para classificação de texto entre outras PLN problemas.
Representações com n-gramas

Todos os esquemas de representação que vimos até agora tratam as palavras como unidades independentes. Não há noção de frases ou ordem de palavras. A abordagem do saco de n-gramas(BoN - Bag ofN-grams) tenta remediar isso. Isso é feito dividindo o texto em pedaços de n palavras contíguas (ou tokens). Tal ação pode nos ajudar a capturar algum contexto, que as abordagens anteriores não conseguiam. Cada pedaço do texto é chamado de n-grama. O vocabulário do corpus,V, nada mais é do que uma coleção de todos os n-gramas exclusivos do corpus do texto. Em seguida,
cada documento do corpus é representado por um vetor de comprimento |V|.
Esse vetor simplesmente contém as contagens de frequência de n-gramas presentes no documento ou zero para os n-gramas que não estão presentes.
Para elaborar, vamos considerar nosso corpus de exemplo. Vamos construir um modelo de
2-gramas
(também conhecido como bigrama) para ele. O conjunto de todos os bigramas no corpus é o seguinte: {cachorro morde, morde homem, homem morde, morde cachorro, cachorro come, come carne, homem come, come comida}. Então, a representação BoN consiste em um vetor de oito dimensões para cada documento.
A representação em bigrama para os dois primeiros documentos é a seguinte: Dl:
[1,1,0,0,0,0,0,0],
D2 : [0,0,1,1,0,0,0,0]. Os outros dois documentos seguem de forma semelhante. Observe que o esquema BoW é um caso especial do esquema BoN, com n = 1. Lembre-se, quando n = 2o modelo é chamado de "bigrama" e quando n = 3 é chamado de "modelo de trigrama". Além disso, observe que, aumentando o valor de n, podemos incorporar um contexto maior; no entanto, isso aumenta ainda mais a dispersão. No jargão da PLN, o esquema BoN também é chamado de "seleção de recursos de n-gram".
Aqui estão os principais prós e contras do BoN:

* Ele captura algumas informações de contexto e ordem de palavras na forma de n-gramas.

* O espaço vetorial resultante é capaz de capturar alguma semelhança semântica.
Documentos com os mesmos n-gramas terão seus vetores mais próximos uns dos outros no espaço euclidiano em comparação com documentos com n-gramas completamente diferentes.
* À medida que n aumenta, a dimensionalidade (e, portanto, a esparsidade) aumenta.

* Ele ainda não fornece uma maneira de resolver o problema de palavras fora do vocabulário.

TF-IDF

Em todas as três abordagens que vimos até agora, todas as palavras no texto são tratadas como igualmente importantes - não há noção de que algumas palavras no documento são mais importantes do que outras. TF-IDF, ou term frequency-inverse document frequency,aborda esse problema. Ele tem como objetivo quantificar a importância de uma determinada palavra em relação a outras palavras do documento e do corpus. É um esquema de representação comumente usado para sistemas de recuperação de informação, para extrair documentos relevantes de um corpus para uma determinada consulta de texto.
A intuição por trás do TF-IDF é a seguinte: se uma palavra w aparece muitas vezes em um documento di, mas não ocorre muito no resto dos documentos dj no corpus, então a palavra w deve ser de grande importância para o documento d,. A importância de w deve aumentar na proporção de sua frequência em di, mas, ao mesmo tempo, sua importância deve diminuir na proporção da frequência em outros documentos dj no corpus. Matematicamente, isso é capturado usando duas quantidades:TF e IDF. Os dois são então combinados para chegar à pontuação TF-IDF.

TF (frequência de termo) mede a frequência com que um termo ou palavra ocorre em um determinado documento. Visto que diferentes documentos no corpus podem ter comprimentos diferentes, um termo pode ocorrer com mais frequência em um documento mais longo do que em um documento mais curto. Para normalizar essas contagens, dividimos o número de ocorrências pelo comprimento do documento. TF de um termo t em um documento d é definido como:
TFÇt, d)

Número de ocorrências do termo t no documento d
Total de termos no documento d

IDF (frequência inversa do documento) mede a importância do termo em um corpus. No cálculo deTF, todos os termos recebem igual importância (ponderação). No entanto, é um fato conhecido que palavras irrelevantes como is, are, am, etc., não são importantes, embora ocorram com frequência.Para explicar esses casos, o IDF pondera os termos que são muito comuns em um corpus e os termos raros. O IDF de um termo t é calculado da seguinte forma:
IDF(t) = loge

Número total de documentos em um corpos
Número de documentos em que o termo t aparece

A pontuação TF-IDF é um produto desses dois termos. Assim, pontuação TF-IDF = TF *
IDF. Vamos calcular as pontuações do TF-IDF para o documento Di do nosso corpus de exemplo.Alguns termos aparecem em apenas um documento, alguns aparecem em dois, enquanto outros aparecem em três documentos. O tamanho do nosso corpus é N = 4. Portanto, os valores correspondentes de TF-IDFpara os termos do documento Di são mostrados na Tabela abaixo.

Palavra TF Score (Di) IDF Score
TF * IDF

Cachorro 1/3 Log(4/3) = 0,29
=0,096

Morde 1/3 Log(4/2) = 0,69
=0,23

Homem 1/3 Log(4/3) = 0,29
=0,096

Semelhante ao BoW, podemos usar os vetores TF-IDF para calcular a similaridade entre dois textos usando uma medida de similaridade como distância euclidiana ou similaridade de cosseno.O TF-IDF
é uma representação comumente usada em cenários de aplicativos, como recuperação de informações e classificação de texto. No entanto, apesar do fato de que TF-IDF ser melhor do que os métodos de vetorização que vimos anteriormente em termos de captura de semelhanças entre palavras, ele ainda sofre da maldição da alta dimensionalidade.
Mesmo hoje, o TF-IDF continua a ser um esquema de representação popular para muitas tarefas dePLN, especialmente nas versões iniciais da solução. Se olharmos para trás em todos os esquemas de representação que discutimos até agora, notamos três desvantagens fundamentais:
* Eles são representações discretas - ou seja, tratam unidades de linguagem
(palavras, n-
gramas, etc.) como unidades atômicas. Essa descrição dificulta sua capacidade de capturar relações entre palavras.
* Os vetores de recursos são representações esparsas e de alta dimensão. A
dimensionalidade aumenta com o tamanho do vocabulário, com a maioria dos valores sendo zero para qualquer vetor. Isso dificulta a capacidade de aprendizagem. Além disso, a representação de alta dimensionalidade os torna computacionalmente ineficientes.
* Eles não podem lidar com palavras fora do vocabulário.

Com isso, chegamos ao fim das abordagens básicas de vetorização. Antes de continuarmos gostaria de tratar de dois outros algoritmos CBOW e Skip-Gram
CBOW e Skip-Gram

Em 2013, Mikolov et. al propuseram em seu trabalho duas diferentes arquiteturas para computar palavras em representação vetorial. O objetivo era criar modelos com redes neurais que fossem treinados mais rapidamente e tivessem melhor acurácia em tarefas de processamento da linguagem natural. Essa pesquisa enfatizou que word embeddings são capazes de extrair conhecimento semântico indo além da ideia de alguns outros pesquisadores que limitavam a análise na extração sintática. Podemos justificar o poder de embutir conhecimento semântico sobre vetores com a seguinte operação mostrada:
V("rainha") = V("rei") - V("homem") + V("mulher")

Essa fórmula apresenta uma ideia em que o Embedding Space pode assimilar o contexto semântico,sendo V o vetor da palavra, pois consegue interpretar que algo próximo de rei e seja mulher, mas não seja homem, será mapeado para um vetor próximo ao de rainha. Os modelos foram construídos para serem usados em bases de dados muito grandes contendo entre milhões até bilhões de palavras.
Importante destacar que os modelos existentes na época não apresentaram boa performance de tempo na construção de vetores com dimensão 50 e 100 com uma grande base de treinamento. Por isso, os autores desenvolveram formas mais eficientes para computar. Desse modo, os autores definiram uma forma geral para o custo da complexidade de uma arquitetura qualquer,chegaram à conclusão de que o custo poderia ser deduzido como:
O=E*T*Q

Sendo E as épocas do treinamento, T é o número de palavras no conjunto de treinamento e Q como o custo total da arquitetura escolhida. Portanto, diminuir o custo significava uma simplificação na arquitetura em um modelo mais antigo, removendo camadas intermediárias percebendo que a"complexidade é causada pela camada oculta não-linear nesses modelos" e
"depende rigorosamente da normalização eficiente do softmax".
Os experimentos foram limitados a comparar apenas a representação de palavras aprendidas por redes neurais devido às limitações de performance e complexidade dos tipos de aprendizagem apresentados no treinamento com larga quantidade de dados. Segundo os autores "palavras podem ter múltiplos graus de similaridade". Devido a isto a comparação ocorreu através de diferentes tarefas com 23 níveis de similaridade, exemplos de similaridade foram criados manualmente gerando uma enorme lista de pares a serem testados.
Como exemplo os pares big e bigger sintaticamente correlacionadas, devem ser pouco distantes no espaço vetorial. Nos resultados foram constatados que grande quantidade de dados produz vetores semânticos úteis para indicar a similaridade semântica entre duas palavras, por exemplo,França e
Paris estão fortemente associados assim como Alemanha e Berlim. Os testes levaram menos que um dia para criar vetores de qualidade com cerca de 1.6 bilhões de palavras. Os autores conseguiram aumentar a acurácia e diminuir o custo computacional do modelo.
Continuous Bag-of-Words (CBOW)

CBOW é uma rede neural que prediz a palavra dado um contexto, sendo o contexto interpretado como uma sentença. A rede neural proposta considera um conjunto de palavras e procura predizer a probabilidade de uma próxima palavra ocorrer em determinada sentença. O resultado calculado na saída da projeção é a média de todos os vetores presentes no contexto da camada de entrada.Este modelo pode prever tanto palavras prévias como posteriores em um contexto.

Target Word

I anguage natural processmg
Context Word

WindowSiize 3

Context Word

0 custo do treinamento de CBOW pode ser dado pela fórmula:

Q = N*D + D* log2(y)

Onde, V é a quantidade de palavras distintas no vocabulário, N o tamanho da camada de projeção eD a dimensão dos vetores.

Skip-gram

O modelo Skip-gram desempenha uma função inversa do apresentado em CBOW, ou seja, dado uma palavra prediz as palavras mais prováveis ao contexto.
Target Word

Predict jump
Puredict the quick brown fox over the lazy dog
Co ntext Wo rd Context Wo rd

Window Size =4

Representação da arquitetura Skip-gram

O custo de treinamento para Skip-gram, no qual C é a distância máxima da palavra é apresentado abaixo. Perceba que o Skip-Gram quando comparado a CBOW é mais custoso:
Q = C * (D + D * log2(V))

Agora, vamos focar nossas atenções para os conceitos de redução de dimensionalidade.

REDUçÃo DE DIMENSIoNALIDADE

A redução de dimensão é uma série de técnicas para reduzir o tamanho dos dados enquanto retém seu conteúdo de informação. Essas técnicas permeiam muitas de nossas atividades digitais diárias.Suponha, por exemplo, que você acabou de voltar de férias da Grécia, depois de passar no concurso da PETROBRAS. Existem 10 fotos de férias em seu telefone que você deseja enviar a um amigo.Infelizmente, essas fotos são muito grandes e sua conexão sem fio atual é lenta. Cada foto tem 1.200pixels de altura e 1.200 pixels de largura. Isso ocupa 5,5 MB de memória e requer
15 segundos para ser transferido. A transferência de todas as 10 fotos levará 2,5 minutos.
Figura 9 - Algumas fotos da sua viagem a Grécia

Felizmente, seu aplicativo de mensagens oferece uma opção melhor: você pode reduzir cada foto de 1.200 x 1.200 pixels para 600 x 480 pixels. Isso reduz as dimensões de cada foto em seis vezes.Ao diminuir a resolução, você sacrificará alguns pequenos detalhes. Contudo, as fotos das férias manterão a maior parte de suas informações - a natureza exuberante, os mares azuis e as areias cintilantes permanecerão claramente visíveis nas imagens. Portanto, a compensação vale a pena.Reduzir a dimensionalidade em seis aumentará a velocidade de transferência em seis:
levará apenas
25 segundos para compartilhar as 10 fotos com seu amigo.

Há grandes vantagens em aplicar métodos de redução de dimensionalidade sobre os dados,
vejamos algumas delas:
* Dados mais compactos são mais fáceis de transferir e armazenar.

* Tarefas algorítmicas requerem menos tempo quando nossos dados são menores.

* Certas tarefas complexas podem ser simplificadas removendo informações desnecessárias.

Existem alguns métodos para redução de dimensionalidade que podem ser classificados de acordo com a figura a seguir:
A primeira grande divisão se baseia na quantidade de características relevantes ou recursos que"sobram" após a redução. Temos métodos que consideram apenas a característica mais importante como o backward elimination e forward selection. O funcionamento desses modelos é bem simples,no fowardselection, por exemplo, você treina o modelo e escolhe a variável ou recurso que produto o melhor resultado e repete a mesma lógica adicionando um novo recurso a cada passagem.
O Backward elimination faz o processo inverso. Primeiramente você treina o modelo com todos os recursos. Em seguida, treina o modelo com todas as combinações possíveis de n-1recursos. Se a variação de acurácia for muito baixa, por exemplo, um modelo com 5 variáveis explicativas produz90% de acurácia e sem a variável X produz 89,5%, percebemos que a presença de X
muda muito pouco a precisão do modelo, logo ele pode ser excluído. Essa lógica é repetida até que nenhum dos recursos/variáveis possa ser eliminado.
A segunda divisão inclui os métodos que resultam em mais de um recurso, ou seja, uma combinação de características. Neste caso, temos dois ramos principais da redução da dimensionalidade. Oprimeiro é conhecido como projeção linear, que envolve a projeção linear de dados de um espaço de alta dimensão para um espaço de baixa dimensão. Isso inclui técnicas como análise de componente principal (PCA), decomposição de valor singular e projeção aleatória.
O segundo ramo é conhecido como aprendizado múltiplo (manifold learning), que também é conhecido como redução de dimensionalidade não linear. Envolve técnicas como o isomapa,que aprende a distância curva (também chamada de distância geodésica) entre os pontos, em vez da distância euclidiana. Outras técnicas incluem escalonamento multidimensional (MDS),incorporação linear local (LLE), incorporação de vizinho estocástico da distribuição-t (t-SNE),aprendizagem de dicionário, incorporação de árvores aleatórias e análise de componentes independentes.Você não precisa decorar esses nomes!! É importante você entender a abstração que diferencia uma transformação linear de um não linear. A figura abaixo apresenta essa lógico de forma intuitiva:
Não faz sentido, em um curso para concurso falarmos de todos esses métodos. Vamos focar apenas no PCA - Principal Component Analysis que, provavelmente, é o método mais utilizado.Existem algumas variações do método: PCA padrão, PCA incremental, PCA esparso e PCA de kernel.Vamos nos limitar a expor os conceitos do PCA padrão:
O PCA padrão é uma das técnicas de redução de dimensionalidade linear mais comuns. No
PCA, o algoritmo encontra uma representação de baixa dimensão dos dados enquanto retém o máximo possível da variação (ou seja, das informações relevantes).
O PCA faz isso abordando a correlação entre os recursos. Se a correlação for muito alta entre um subconjunto de recursos, o PCA tentará combinar os recursos altamente correlacionados e representar esses dados com menos recursos linearmente não correlacionados. Oalgoritmo continua realizando essa redução de correlação, encontrando as direções de variância máxima nos dados dimensionais originais e projetando-as em um espaço dimensional menor. Esses componentes recém-derivados são conhecidos como componentes principais.
Com esses componentes, é possível reconstruir os recursos originais - não exatamente, mas geralmente perto o suficiente. O algoritmo PCA tenta ativamente minimizar o erro de reconstrução durante sua procura pelos componentes ideais. Abaixo vamos resumir o passo a passo para execução do algoritmo de PCA:
Cálculo da

Cálculo dos

[Hf]

Reduzir as

Normalização dos dados matriz de covariância autovetores e autovalores dimensões do conjunto de dados
Figura 10 - Passos que devemos seguir durante a implementação do PCA.

CLASSIFICAçÃo DE TEXToS

Todos nós verificamos o e-mail todos os dias, possivelmente várias vezes. Um recurso útil da maioria dos provedores de serviço de e-mail é a capacidade de separar automaticamente os e-mails de spam dos e-mails regulares. Este é um caso de uso de uma tarefa popular de PLN conhecida como classificação de texto. A classificação de texto é a tarefa de atribuir uma ou mais categorias a um determinado trecho de texto a partir de um conjunto maior de categorias possíveis.
No exemplo do separador de e-mail, temos duas categorias - spam e não spam - e cada e-mail recebido é atribuído a uma dessas categorias. Essa tarefa de categorizar textos com base em algumas propriedades tem uma ampla gama de aplicações em diversos domínios, como mídia social, e-commerce, saúde, direito e marketing, apenas para citar alguns. Embora o propósito e a aplicação da classificação do texto possam variar de domínio para domínio, o problema abstrato subjacente permanece o mesmo. Essa invariância do problema central e suas aplicações em uma miríade de domínios torna a classificação de texto de longe a tarefa de PLN mais usada na indústria e a mais pesquisada na academia.
No aprendizado de máquina, a classificação é o problema de categorizar uma instância de dados em uma ou mais classes conhecidas. A entrada de dados pode ser de diferentes formatos,como texto,
fala, imagem ou números. A classificação de texto é uma instância especial do problema de classificação, em que a(s) entrada(s) de dados de entrada são texto e o objetivo é categorizar o trecho de texto em um ou mais rótulos (chamados de classe) a partir de um conjunto de grupos predefinidos (classes).
O "texto" pode ter comprimento arbitrário: um caractere, uma palavra, uma frase, um parágrafo ou um documento completo. Considere um cenário onde queremos classificar todas as avaliações de clientes para um produto em três categorias: positivas, negativas e neutras.O desafio da classificação de texto é "aprender" essa categorização a partir de uma coleção de exemplos para cada uma dessas categorias e prever as categorias de novos produtos não vistos e de novas avaliações de clientes. No entanto, essa categorização nem sempre resulta em uma única categoria,
e pode haver qualquer número de categorias disponíveis. Vamos dar uma olhada rápida na taxonomia da classificação de texto para entender isso.
Binária

*Se o número de classes for dois

*Exemplo: classificar um e-mail como spam ou não spam

Multiclasse

*Se o número de classes for maior do que dois.

*Exemplo: Classificar o sentimento de uma resenha de cliente como negativo, neutro ou positivo

Multilabel

*Pode ter mais de um rótulo associado

*Exemplo: um artigo de notícias sobre uma partida de futebol pode pertencer a mais de uma categoria, como "esportes" e "futebol
Qualquer abordagem de classificação supervisionada, incluindo classificação de texto, pode ser posteriormente distinguida em três tipos com base no número de categorias envolvidas:classificação binária, multiclasse e multilabel. Se o número de classes for dois, é chamado de classificação binária. Se o número de classes for mais de dois, é referido como classificação multiclasse. Portanto, classificar um e-mail como spam ou não spam é um exemplo de configuração de classificação binária. Classificar o sentimento de uma resenha de cliente como negativo, neutro ou positivo é um exemplo de classificação multiclasse. Em configurações binárias e multiclasse, cada documento pertence a exatamente uma classe de C, onde C é o conjunto de todas as classes possíveis.
Na classificação multilabel, um documento pode ter um ou mais rótulos/classes anexados a ele. Por exemplo, um artigo de notícias sobre uma partida de futebol pode pertencer a mais de uma categoria, como "esportes" e "futebol", simultaneamente, enquanto outro artigo de notícias sobre as eleições nos Estados Unidos pode ter os rótulos "política", "EUA" e "Eleições."Assim, cada documento possui rótulos que são um subconjunto de C. Cada artigo pode estar em nenhuma classe,exatamente uma classe, várias classes ou todas as classes. Às vezes, o número de rótulos no conjunto
C pode ser muito grande (conhecido como "classificação extrema"). Em alguns outros cenários,podemos ter um sistema de classificação hierárquica, o que pode resultar em cada texto recebendo rótulos diferentes em níveis diferentes na hierarquia.
Assim, a classificação de texto, também conhecida como marcação de texto ou categorização de texto, é o processo de categorizar o texto em grupos organizados. Usando oProcessamento de
Linguagem Natural (PLN), os classificadores de texto podem analisar automaticamente o texto e, em seguida, atribuir um conjunto de tags ou categorias predefinidas com base em seu conteúdo.
A classificação de texto está se tornando uma parte cada vez mais importante dos negócios, pois permite obter facilmente insights de dados e automatizar processos de negócios.Alguns dos exemplos e casos de uso mais comuns para a classificação automática de texto incluem o seguinte:
Análise de sentimento: o processo de entender se um determinado texto está falando positiva ou negativamente sobre um determinado assunto (por exemplo, para fins de monitoramento de marca).
Detecção de tópicos: a tarefa de identificar o tema ou tópico de um trecho de texto
(por exemplo,
saber se uma crítica de produto é sobre facilidade de uso , suporte ao cliente ou preço ao analisar o feedback do cliente).
Detecção de idioma: o procedimento de detecção do idioma de um determinado texto (por exemplo, saber se um tíquete de suporte recebido é escrito em inglês ou espanhol para encaminhar automaticamente os tíquetes para a equipe apropriada).
MoDELAGEM DE TóPICoS LATENTES

Botar pra torar

Conhecimento

João Magalhães
Tm»?" Silvinha pcess° Alegria
Diversão A . . I IO

Prof.Thiago .Cavalcanti

Phelype QAT^I^TCU Python

Eduardo OdUdC Mareia Rocha
Interaçao Qaroline informação

Kairam Análise de Dados

Aprovação ConCUrSO

Anrandi"7adn do mámiina

A modelagem de tópicos é uma das aplicações mais comuns da PLN em casos de uso industrial. Para analisar diferentes formas de texto, de artigos de notícias a tweets, da visualização de nuvens de palavras à criação de gráficos de tópicos e documentos conectados, os modelos de tópicos são úteis para uma variedade de casos de uso. Os modelos de tópico são usados extensivamente para agrupamento de documentos e organização de grandes coleções de dados de texto, também são úteis para classificação de texto.
Mas o que é modelagem de tópicos? Digamos que recebamos uma grande coleção de documentos e que nos é solicitado para darmos sentido aos documentos. O que faremos? Obviamente,a tarefa não está bem definida. Dado o grande volume de documentos, passar por cada um deles manualmente não é uma opção. Uma forma de abordar o problema é trazer à tona algumas palavras que melhor descrevem o corpus, como as palavras mais comuns no corpus. Isso é chamado de nuvem de palavras. A chave para uma boa nuvem de palavras é remover as palavras irrelevantes.Se pegarmos qualquer corpus de texto em inglês e listarmos as k palavras mais frequentes, não obteremos nenhuma visão significativa, pois as palavras mais frequentes serão palavras irrelevantes(stop words). Entretanto, depois de fazer o pré-processamento apropriado, a nuvem de palavras pode gerar alguns insights significativos, dependendo da coleção de documentos.
Outra abordagem é dividir os documentos em palavras e frases e, em seguida, agrupar essas palavras e frases com base em alguma noção de semelhança entre elas. Os grupos de palavras e frases resultantes podem então ser usados para construir alguma compreensão do que é o corpus.Intuitivamente, se escolhermos uma palavra de cada grupo, o conjunto de palavras selecionadas representa (em um sentido semântico) do que trata o corpus. Outra possibilidade é usarTF-IDF.
Considere um corpus de documentos em que alguns documentos falam sobre agricultura.
Então,
termos como "fazenda", "safras", "trigo" e "agricultura" devem formar os "tópicos" nos documentos sobre agricultura. Qual é a maneira mais fácil de localizar esses termos que ocorrem com frequência em um documento, mas não ocorrem muito em outros documentos do corpus?
Topics

Document

Collection of Documents

Topic Model

Distribution of topics

Topic

Frequency of words

A modelagem de tópicos operacionaliza essa intuição. Tenta identificar as palavras "chave"(chamadas de "tópicos") presentes em um corpus de texto sem conhecimento prévio sobre ele. Afigura abaixo mostra uma visualização dos resultados de um modelo de tópico para um corpus ciências humanas.
Perfo<m«ng Azt»

Visual Arts

0 conceito de tópico ou evento é um acontecimento que decorre dentro de um determinado espaço e tempo, onde podem ser extraídas informações para previsão e caracterização de acontecimentos do mundo real. A detecção de tópicos tem como objetivo o agrupamento de informações de maneira contextualizada. Portanto, dado um conjunto A de textos, existe uma quantidade B de contextos(tema) associados a estes textos. Neste caso, B é menor ou igual a A, visto que mais de um texto pode discorrer sobre o mesmo tema.
Para compreender uma quantidade expressiva de informações, tem sido utilizado, cada vez mais,um aparato de ferramentas computacionais que possibilitam organizar, pesquisar e compreender melhor um determinado volume de informações disponibilizado na internet. AModelagem de
Tópicos possibilita realizar a tarefa de resumir e organizar corpus de dados por meio de algoritmos de Machine Learning e métodos estatísticos de forma que seja possível descobrir temas e relações,como as mudanças dos termos ao longo dos anos.

Deve-se notar que não existe um modelo de tópico único. A modelagem de tópicos geralmente se refere a uma coleção de métodos de aprendizado estatístico não supervisionado para descobrir tópicos latentes em uma grande coleção de documentos de texto. Alguns dos algoritmos de modelagem de tópicos populares são Latent Dirichlet Allocation (LDA), Latente SemanticIndexing
(LSI), e análise semântica latente probabilística (PLSA). Na prática, a técnica mais comumente usada é o LDA.
O que o LDA faz? Vamos começar com um corpus de exemplo. Digamos que temos uma coleção de documentos, Dl a D5, e cada documento consiste em uma única frase:
* Dl: Gosto de comer brócolis e banana.

* D2: Comi banana com salada no café da manhã.

* D3: Cachorros e gatinhos são fofos.

* D4: Minha irmã adotou um gatinho ontem.

* D5: Olhe este hamster fofo mastigando um pedaço de brócolis.

Aprender um modelo de tópico nesta coleção usando LDA pode produzir uma saída como esta:

a) Tópico A: 30% brócolis, 15% bananas, 10% café da manhã, 10% mastigando b) Tópico B: 20% cachorros, 20% gatinhos, 20% fofos, 15% hamster
* Documento 1 e 2: 100% Tópico A

* Documento 3 e 4: 100% Tópico B

* Documento 5: 60% Tópico A, 40% Tópico B

Assim, os tópicos nada mais são do que uma mistura de palavras-chave com uma distribuição de probabilidade, e os documentos são compostos de uma mistura de tópicos, novamente com uma distribuição de probabilidade. Um modelo de tópico fornece apenas uma coleção de palavras-chave por tópico. O que exatamente o tópico representa e como deve ser nomeado é normalmente deixado para a interpretação humana em um modelo LDA. Aqui, podemos olhar para oTópico A e dizer: "é sobre comida". Da mesma forma, para o tópico B, podemos dizer, "trata-se de animais de estimação".
Como o LDA consegue isso? O LDA pressupõe que os documentos são produzidos a partir de uma mistura de tópicos. Além disso, assume que o seguinte processo gera esses documentos:no início,
temos uma lista de tópicos com uma distribuição de probabilidade. Para cada tópico, há uma lista associada de palavras com uma distribuição de probabilidade. Tiramos amostras de k tópicos da distribuição de tópicos. Para cada um dos Utópicos selecionados, usamos uma amostra de palavras da distribuição correspondente. É assim que cada documento da coleção é gerado.
Agora, dado um conjunto de documentos, o LDA tenta retroceder o processo de geração e descobrir quais tópicos gerariam esses documentos em primeiro lugar. Os tópicos são chamados de"latentes"
porque estão ocultos e devem ser descobertos. Como o LDA faz isso? Ele faz isso fatorando uma matriz de termo de documento (M) que mantém a contagem de palavras em todos os documentos.
Essa matriz possui todos os m documentos Di, D 2, D 3... Dm dispostos ao longo das linhas e todas as n palavras Wi, W 2, W n no vocabulário do corpus organizados em colunas. M [/,;] é a contagem de frequência da palavra W/no Documento D/. A figura abaixo mostra uma dessas matrizes para um corpus hipotético que consiste em cinco documentos, com um vocabulário de seis palavras.
W1

Dl 0

D2 1

D3 2

D4 1

D5 0

W2 W3

3 0

0 0

1 2

1 1

1 2

W4 W5 W6

0 1 2

1 1 1

2 4 2

4 0 0

1 0 4

Observe que se cada palavra no vocabulário representa uma dimensão única e o vocabulário total é de tamanho n, então a /-esima linha dessa matriz é um vetor que representa o/-esimo documento neste espaço n- dimensional. LDA fatoriza M em duas submatrizes: Ml e M2. Ml é uma matriz de tópicos de documentos e M2 é uma matriz de termos de tópicos, com dimensões (M, K)e (K, N),
respectivamente. Com quatro tópicos (K1-K4), as submatrizes para M podem ser semelhantes às mostradas na figura abaixo. Aqui, k é o número de tópicos que estamos interessados em encontrar.
Kl

Dl 1

D2 1

D3 1

D4 1

D5 0

K2 K3 K4

0 0 1

1 0 0

0 0 1

0 1 0

1 1 1

W1

Kl 1

K2 0

K3 1

K4 1

W2 W3

0 0

1 1

1 0

0 0

W4 W5 W6

1 0 0

0 1 1

1 1 0

0 1 0

Figura 11 - Matrizes Fato radas

Essas submatrizes podem então ser usadas para entender a estrutura de tópicos de um documento e as palavras-chave das quais um tópico é composto. Agora que temos uma ideia do que acontece nos bastidores vamos apresentar uma definição forma do LDA:
Latent Dirichlet Allocation (LDA). Este método consiste em um modelo probabilístico,
no qual cada documento é modelado como uma combinação de tópicos, onde cada tópico corresponde a uma distribuição multinomial sobre as palavras. A distribuição documento-tópico e tópico-palavra aprendidas pelo LDA, por meio de inferênciaBayesiana, descrevem os melhores tópicos por documento e as palavras mais descritivas para cada tópico. Uma definição formal para um tópico, é uma distribuição sobre um vocabulário fixo. Por exemplo, o tópico sobre genética tem palavras sobre genética com alta probabilidade e o tópico biologia evolutiva tem palavras sobre biologia evolutiva com alta probabilidade.
Já falamos que para descobrimos a existência de tópicos podemos usar ainda outros algoritmos,vejamos a definição de mais dois deles:

Indexação semântica latente (LSI - Latent Semantic Indexing) é um método de indexação e recuperação que usa uma técnica matemática chamada decomposição de valor singular para identificar padrões nas relações entre os termos e conceitos contidos em uma coleção não estruturada de texto. O LSI é baseado no princípio de que palavras usadas nos mesmos contextos tendem a ter significados semelhantes. Uma característica fundamental do LSI é sua capacidade de extrair o conteúdo conceituai de um corpo de texto, estabelecendo associações entre os termos que ocorrem em contextos semelhantes
Non-negative Matrix Factorization (NMF). O NMF consiste em um algoritmo de fatoração de matrizes que encontra a fatoração positiva de uma matriz positiva recebida como entrada. Seja S o conjunto de documentos representados por uma matriz V de dimensão m x n, onde m é o número de termos distintos e n é equivalente ao número de documentos em S. O NMF encontra a menor aproximação de V em termos de alguma métrica específica fatorando V no produto (WH)de duas matrizes de menor dimensões W (m x k) e H (k x n), onde k é o número de tópicos.Cada coluna de
W é um vetor base que contém uma codificação semântica ou um conceito de V e cada coluna de Hcontém uma codificação da combinação linear dos vetores bases que aproxima a correspondente coluna de V.
ANÁLISE DE SENTIMENToS

My experience sofarhas been fantastic!
POSITIVE

The product is oklguess Yoursupportteam is useless
NEGATIVE

A análise de sentimento, também chamada de mineração de opinião, tem sido uma das áreas de pesquisa mais ativas no processamento de linguagem natural desde o início de 2000. Oobjetivo da análise de sentimento é definir ferramentas automáticas capazes de extrair informações subjetivas de textos em linguagem natural, como opiniões e sentimentos, de modo a criar um conhecimento estruturado e acionável para ser usado por um sistema de apoio à decisão ou um tomador de decisão.
Mais formalmente uma opinião é um quíntuplo,

(í?j, Cl(y, Stjfci, hk, ti)

onde e, é o nome de uma entidade, 0,7 é um aspecto de e,, Sijki é o sentimento sobre o aspecto a,y da entidade e,-, hk denota o titular da opinião e ti é o momento em que a opinião é expresso por hk.
O sentimento Syw é positivo, negativo ou neutro, ou expresso com diferentes níveis de força/intensidade, como o sistema de 1 a 5 estrelas usado pela maioria dos sites de avaliação (por exemplo, Amazon).
Por exemplo, considere que ontem João Magalhães comprou um iPhone (deveria estar estudando pro concurso da Petrobras, mas como vai servir de exemplo pra nossa aula, tá perdoado!). Ele o testou durante todo o dia e quando voltou para casa do trabalho (às 19h do dia 21/12/2021)escreveu em sua rede social favorita a mensagem " O iPhone é muito bom, mas ainda precisam resolver questões como a vida útil da bateria e questões de segurança." Vamos indexar"iPhone",
"vida da bateria" e "segurança" como 1, 2 e 3, respectivamente. João é indexado como
4 e o momento em que ele escreveu a frase é indexado como 5. Então João é o detentor da opinião e is ("19:00 21-12-2021") é o momento em que a opinião é expressa por hn (João). Otermo "iPhone"
é a entidade ei, "duração da bateria" e "problemas de segurança" são aspectos GU e au da entidade ei("iPhone"), S1245 - neg é o sentimento sobre o aspecto auC vida útil da bateria") da entidade e 1("

iPhone "). E $1345 = neg é o sentimento sobre o aspecto 013 ("questões de segurança") da entidade ei("lphone'). Quando a opinião é sobre a própria entidade como um todo, o aspecto especial"GERAL" é utilizado para denotá-la.

Hoje em dia, a análise de sentimento ganhou ainda mais valor com o advento das redes sociais. Sua grande difusão e seu papel na sociedade moderna representam uma das novidades mais interessantes, despertando o interesse de pesquisadores, jornalistas, empresas e governos.A densa interconexão que muitas vezes surge entre os usuários ativos gera um espaço de discussão capaz de motivar e envolver indivíduos de uma ágora maior, conectando pessoas com objetivos comuns e facilitando diversas formas de ação coletiva. As redes sociais estão, portanto, criando uma revolução digital, permitindo a expressão e disseminação de emoções e opiniões através da rede. Dados opinativos na rede, se adequadamente coletados e analisados, permitem não apenas compreender e explicar muitos fenômenos sociais complexos, mas também predizê-los.
A tendência geral nas pesquisas sobre análise de sentimento em redes sociais é aplicar as técnicas herdadas da análise de sentimento tradicional estudada desde o início de2000. No entanto,
considerando a evolução das fontes onde as opiniões são expressas, as estratégias disponíveis no estado da arte atual não são mais eficazes para a mineração de opiniões neste ambiente novo e desafiador. Na verdade, a análise de sentimento em rede social, além de herdar uma infinidade de questões da análise de sentimento tradicional e do processamento de linguagem natural,introduz outras complexidades (mensagens curtas, conteúdo barulhento, metadados como gênero,localização e idade) e novas fontes de informação.

Características de análise de sentimento

O primeiro objetivo, quando se trata de análise de sentimento, geralmente consiste em distinguir entre sentenças subjetivas e objetivas. Se uma determinada sentença é classificada como objetiva,nenhuma outra tarefa fundamental é necessária, enquanto se a sentença for classificada como subjetiva, sua polaridade (positiva, negativa ou neutra) precisa ser estimada. Aclassificação da subjetividade é a tarefa que distingue sentenças que expressam informações objetivas (ou factuais)(sentenças objetivas) de sentenças que expressam visões e opiniões subjetivas
(sentenças subjetivas).
Análise de sentimentos

Classificação

S ubj etiva/ 0 bj etiva

Polaridade

Um exemplo de frase objetiva é " O iPhone é um smartphone , enquanto um exemplo de frase subjetiva é "O iPhone é incrível A classificação de polaridade é a tarefa que distingue sentenças que expressam polaridades positivas, negativas ou neutras. Observe que uma frase subjetiva pode não expressar nenhum sentimento positivo ou negativo (por exemplo, "Acho que ele chegou."). Por esse motivo, deve ser classificada como "neutro".
A análise do sentimento se concentra na polaridade, mas também pode analisar sentimentos e emoções (raiva, felicidade, tristeza, etc.), urgência (urgente, não urgente) e até mesmo intenções(interessada x não interessada). Dependendo de como você deseja interpretar o feedback e as consultas do cliente, você pode definir e adaptar suas categorias para atender às suas necessidades de análise de sentimento.
Níveis de Análise

Conforme mencionado anteriormente, o objetivo da análise de sentimento é
"definir ferramentas automáticas capazes de extrair informações subjetivas de textos em linguagem natural Aprimeira escolha quando se aplica a análise de sentimento é definir o que o texto (ou seja,o objeto analisado)
significa no caso de estudo considerado. Em geral, a análise de sentimento em redes sociais pode ser investigada principalmente em três níveis, representados graficamente na figura abaixo:
Vamos descrever rapidamente cada um dos níveis:

* Nível da mensagem: o objetivo é classificar a polaridade de uma mensagem opinativa completa. Por exemplo, dada a avaliação de um produto, o sistema determina se a mensagem de texto expressa uma opinião geral positiva, negativa ou neutra sobre o produto. Asuposição é que a mensagem inteira expressa apenas uma opinião sobre uma única entidade
(por exemplo, um único produto).

* Nível da frase: o objetivo é determinar a polaridade de cada frase contida em uma mensagem de texto. O pressuposto é que cada frase, em uma determinada mensagem, denota uma única opinião sobre uma única entidade.
* Nível de entidade e aspecto: executa uma análise mais detalhada do que o nível de mensagem e frase. Parte-se da ideia de que uma opinião consiste em um sentimento e um alvo (de opinião). Por exemplo, a frase "O iPhone é muito bom, mas ainda precisa melhorar a vida útil da bateria e os resolver problemas de segurança" avalia três aspectos: iPhone(positivo), vida útil da bateria (negativo) e segurança (negativo).

Opinião Regular Versus Comparativa

Uma opinião pode assumir diferentes matizes e pode ser atribuída a um dos seguintes grupos:

* Opinião regular: uma opinião regular é muitas vezes referida na literatura como uma opinião padrão e tem dois subtipos principais:
o Opinião direta: uma opinião direta se refere a uma opinião expressa diretamente em uma entidade (por exemplo, "0 brilho da tela do iPhone é incrível").
o Opinião indireta: Uma opinião indireta é uma opinião expressa indiretamente sobre uma entidade com base em seus efeitos sobre algumas outras entidades. Por exemplo,a frase "Depois que mudei para o iPhone, perdi todos os meus dados!" descreve um efeito indesejável da ativação dos "meus dados" em outro celular, que indiretamente dá um sentimento negativo sobre o iPhone.
* Opinião comparativa: Uma opinião comparativa expressa uma relação de semelhanças ou diferenças entre duas ou mais entidades e/ou uma preferência do titular da opinião com base em alguns aspectos comuns das entidades. Por exemplo, as frases "O iOS tem melhor desempenho do que Android" e "O iOS é o sistema operacional móvel de melhor desempenho"expressam duas opiniões comparativas. Uma opinião comparativa é geralmente expressa com o uso da forma comparativa ou superlativa de um adjetivo ou advérbio.
Opiniões Explícitas Versus Implícitas

Entre as diferentes nuanças que uma opinião pode assumir, devemos distinguir as opiniões explícitas e implícitas:
* Opinião explícita: Uma opinião explícita é uma declaração subjetiva que dá uma opinião regular ou comparativa (por exemplo, "O brilho da tela do iPhone é incrível ").
* Opinião implícita: uma opinião implícita é uma declaração objetiva que implica uma opinião regular ou comparativa que geralmente expressa um fato desejável ou indesejável(por exemplo, "Sábado à noite irei ao cinema assistir 'Homem Aranha Sem Volta pra Casa'.Mal posso esperar para assistir!" e '"Resgate do Soldado Ryan' é mais violento do que 'BastardosInglórios'"). O primeiro exemplo sugere que há uma boa expectativa em relação ao filme,
embora não seja explicada em palavras, ao passo que entender a opinião oculta no segundo exemplo é difícil até para humanos. Para algumas pessoas, violência em filmes de guerra podem ser uma boa característica que torna o filme mais realista, enquanto pode ser uma característica negativa para outros. Minha esposa, por exemplo, não gosta de filmes de ação,chamar ela para assistir qualquer versão de Velozes e Furiosos não é uma boa ideia!

Lidando com figuras de linguagem

Uma figura de linguagem é qualquer desvio engenhoso do modo comum de falar ou escrever. Na tradição de Aristóteles, as figuras de linguagem podem ser divididas em dois grupos:esquemas e tropos. A função dos esquemas e tropos é realizar uma transferência de algum tipo;esquemas são caracterizados por uma transferência de ordem, enquanto tropos são caracterizados por uma transferência de significado.
Por exemplo, as figuras de linguagem mais problemáticas no processamento da linguagem natural são a ironia e o sarcasmo, que são colocados no grupo tropos. Embora a ironia seja frequentemente usada para enfatizar ocorrências que se desviam do esperado, como reviravoltas do destino, o sarcasmo é comumente usado para transmitir uma crítica implícita com uma vítima em particular como alvo. Exemplos de frases sarcásticas e irônicas são:
1.Sarcasmo (Nota: Silvinha odeia os livros de viagens de Eduardo)

- Silvinha: Sim, eu gosto, realmente gosto de seus livros de viagem, Dudu. Você é um autor muito habilidoso.
- Eduardo: Uhmmm.

2.Ironia (Nota: Mareia e João acabaram de ver uma peça realmente terrível no teatro.
Eles estão decepcionados.)
- João: Bem! Que uso valioso de uma noite!

- Mareia: Realmente!

No exemplo da ironia, não houve sarcasmo porque João não pretendia magoar Mareia com seu comentário. Ele estava usando a ironia para observar que sentia ter perdido sua noite no teatro. No exemplo do sarcasmo, Silvinha usou o sarcasmo para mostrar a Eduardo que ela não gostava de seus livros e achava que ele não era um bom escritor. Há ironia também, mas o tom transmite uma crítica implícita que a torna sarcástica.
Uma característica inerente dos atos de fala sarcásticos e irônicos é que às vezes são difíceis de reconhecer, primeiro para humanos e depois para máquinas. A dificuldade no reconhecimento do sarcasmo e da ironia causa mal-entendidos na comunicação cotidiana e coloca problemas para muitos sistemas de processamento de linguagem natural por causa dos maus resultados obtidos por trabalhos de última geração. No contexto da análise de sentimento (onde sarcasmo e ironia são geralmente considerados sinônimos), quando uma frase sarcástica/irônica é detectada como positiva, provavelmente significa negativa e vice-versa.
Ok! Chegamos ao final do conteúdo, mas você pode estar com a mesma dúvida do nosso aluno Igor ...
"Professor, não entendi a diferença entre opinião direta X opinião explícita e opinião indireta X opinião implícita. Pode me explicar, por favor?"
Com certeza!...

É bem sutil, mas existe!! :) Vejamos ...

Opinião direta X opinião explícita

Opinião direta é precisa ... trata-se da facilidade de entender o que está sendo expresso

Opinião explícita apresenta um conceito subjetivo ... eu digo algo que é minha opinão,
por exemplo

... "Cocada tem um gosto ótimo" (é a minha opinião sobre o doce, você pode não gostar, logo é direta e explícita)
Outro exemplo ... "Cocada tem um gosto melhor do que Doce de Leite." (é uma opinião comparativa mas explícita ... mais uma vez é minha opinião ... você pode gostar mais de Doce deLeite do que cocada).
Agora vamos para a segunda comparação:

Opinião indireta X opinião implícita.

Opinião indireta não é falada diretamente, alguma inferência precisa ser feita ...

Já a opinião implícita é objetiva, ela revela a realidade dos fatos ... não podemos mudar! Por exemplo
... Comprei o colchão há uma semana, e um buraco se formou. (Aqui temos uma opinião indireta e implícita). O fato de ter se formado um buraco reflete de forma objetiva a qualidade ruim do colchão.
Vejamos outro exemplo ... A vida útil da bateria dos telefones Nokia é mais longa do que a dos telefones Samsung (aqui temos uma opinião comparativa e implícita (objetiva)).
Pessoal, lembrem-se de usar o fórum de dúvidas sempre que necessário! Como sempre falo qualquer dúvida estou às ordens!
Forte abraço e bons estudos!

CoNCEIToS CoMPLEMENTARES

MÉTRICAS DE SIMILARIDADE TEXTUAL (SIMILARIDADE Do CoSSENo,
DISTÂNCIA EUCLIDIANA, SIMILARIDADE DE JACCARD, DISTÂNCIA DE
MANHATTAN E COEFICIENTE DE DICE).

As medidas de similaridade de texto desempenham um papel cada vez mais importante em pesquisas e aplicativos relacionados a texto em tarefas como recuperação de informações,classificação de texto, agrupamento de documentos, detecção de tópicos, rastreamento de tópicos,geração de perguntas, resposta a perguntas, pontuação de resposta curta,
tradução automática,
resumos de texto e outros.

Encontrar similaridade entre palavras é uma parte fundamental da similaridade de texto, que é então usada como um estágio primário para similaridades de frases, parágrafos e documentos. As palavras podem ser semelhantes de duas maneiras lexical e semanticamente. As palavras são lexicalmente semelhantes se tiverem uma sequência de caracteres semelhante.Palavras são semanticamente semelhantes se representam a mesma coisa, são opostas, se representam conceitos antagônicos.
A similaridade lexical é introduzida por meio de diferentes algoritmos baseados em strings, a similaridade semântica é introduzida por meio de algoritmos baseados em Corpus e baseados em conhecimento. Medidas baseadas em string operam em sequências de palavras. Uma métrica de string é uma métrica que mede semelhança ou dissimilaridade (distância) entre duas strings de texto para correspondência ou comparação aproximada de string. A similaridade baseada em corpus é uma medida de similaridade semântica que determina a similaridade entre palavras de acordo com as informações obtidas em grandes corpora. Similaridade baseada no conhecimento é uma medida de similaridade semântica que determina o grau de similaridade entre palavras usando informações derivadas de redes semânticas.
Os algoritmos baseados em strings são podem ser divididos em baseados em caracteres e baseado em termos. A lista apresentada acima, no título da seção, são todas métricas baseadas em strings,mais especificamente baseada em termos. Vejamos a definição de cada uma delas:

Distância de Manhattan - A distância do bloco também é conhecida como distância de
Manhattan,
distância do vagão, distância de valor absoluto ou distância LI calcula a distância que seria percorrida para ir de um ponto de dados a outro se um caminho semelhante a uma grade fosse seguido. A distância de bloco entre dois itens é a soma das diferenças de seus componentes correspondentes.
Manhattan Distance r /—I
Similaridade do cosseno - A similaridade de cosseno é uma medida de similaridade entre dois vetores de um espaço que mede o cosseno do ângulo entre eles.
Cosine Similarity

5 10 15

Coeficiente de Dice - O coeficiente de Dice é definido como duas vezes o número de termos comuns nas sequências comparadas dividido pelo número total de termos em ambas as sequências.
2 * |X n Y|

D(X,Y) =

|X| + |K|

Distância euclidiana - A distância euclidiana ou distância L2 é a raiz quadrada da soma das diferenças quadradas entre os elementos correspondentes dos dois vetores.
@dataaspirant.com

Similaridade de Jaccard - A similaridade de Jaccard é calculada como o número de termos compartilhados sobre o número de todos os termos únicos em ambos os conjuntos de caracteres.
Jaccard Similarity

SetA= | i

SetB=|^

IA I = 4 I B I = 5 ©dataaspirant.com

Union(A,B)

Intersection (A,B) =

I Union (A,B) I = 7 I Intersection (A,B)I= 2

Jaccard Similarity J (A,B) = I Intersection (A,B) I / I Union (A,B) I

= 2/7

= 0.286

APLICAçõES DE PLN

Agrupamento de texto

Para agrupar um conjunto de textos, é preciso determinar os atributos de cada instância do conjunto. Estes atributos podem ser em função de diversas métricas, como a quantidade de palavras ou parágrafos do texto, palavras presentes e suas frequências, sequências de palavras(n-gramas),
conjunto de palavras (bag of words), entre outros.

Como parte do aprendizado não supervisionado, o clustering é usado para agrupar pontos de dados semelhantes sem saber a qual cluster os dados pertencem. Então, em certo sentido,agrupamento de texto é sobre como textos semelhantes (ou sentenças) são agrupados.
O agrupamento utiliza um algoritmo de aprendizagem não supervisionado para agrupar dados em k grupos (k é geralmente o número é predefinido) sem realmente saber a qual agrupamento os dados pertencem. O algoritmo de agrupamento tentará aprender o padrão sozinho. Um dos algoritmos mais amplamente usados para agrupamento é o K-means . Este algoritmo pode agrupar tweets com base em sua distância com o centróide do grupo.
Tradução automática de texto

A tradução automática ou automática é talvez uma das tarefas de inteligência artificial mais desafiadoras, dada a fluidez da linguagem humana. Classicamente, sistemas baseados em regras foram usados para essa tarefa, que foram substituídos na década de 1990 por métodos estatísticos.Mais recentemente, os modelos de rede neural profunda alcançam resultados de última geração em um campo que é apropriadamente chamado de tradução neural automática.
Mas o que é tradução neural automática? Tradução automática neural, ou NMT - Neural
Machine
Translation - para abreviar, é o uso de modelos de rede neural para aprender um modelo estatístico para tradução automática. O principal benefício da abordagem é que um único sistema pode ser treinado diretamente no texto de origem e destino, não exigindo mais o pipeline de sistemas especializados usados no aprendizado de máquina estatístico.
Ao contrário do sistema de tradução tradicional baseado em frases, que consiste em muitos subcomponentes pequenos que são ajustados separadamente, a tradução neural automática tenta construir e treinar uma única rede neural grande que lê uma frase e produz uma tradução correta.Como tal, os sistemas de tradução automática neural são considerados sistemas ponta-a-ponta, pois apenas um modelo é necessário para a tradução.
A força da NMT está em sua capacidade de aprender diretamente, de ponta a ponta, o mapeamento do texto de entrada para o texto de saída associado.
Modelo codificador-decodificador - Modelos de rede neural Perceptron multicamadas podem ser usados para tradução automática, embora os modelos sejam limitados por uma sequência de entrada de comprimento fixo em que a saída deve ter o mesmo comprimento. Esses modelos iniciais foram melhorados recentemente por meio do uso de redes neurais recorrentes organizadas em uma arquitetura de codificador-decodificador (encoder-decoder) que permite sequências de entrada e saída de comprimento variável.
Uma rede neural codificadora lê e codifica uma frase de origem em um vetor de comprimento fixo.Um decodificador então produz uma tradução do vetor codificado. Todo o sistema codificador-decodificador, que consiste no codificador e no decodificador para um par de idiomas,
é treinado em conjunto para maximizar a probabilidade de uma tradução correta dada uma frase de origem.
A chave para a arquitetura do codificador-decodificador é a capacidade do modelo de codificar o texto de origem em uma representação interna de comprimento fixo chamada vetor de contexto.Curiosamente, uma vez codificados, diferentes sistemas de decodificação podem ser usados,
em princípio, para traduzir o contexto em diferentes idiomas.
Um modelo primeiro lê a sequência de entrada e emite uma estrutura de dados que resume a sequência de entrada. Chamamos este resumo de "contexto" C. Um segundo modo, geralmente umRNN, então lê o contexto C e gera uma frase no idioma de destino.

Codificadores-decodificadores com atenção - Embora eficaz, a arquitetura do codificador-decodificador tem problemas com longas sequências de texto a serem traduzidas.
O problema decorre da representação interna de comprimento fixo que deve ser usada para decodificar cada palavra na sequência de saída. A solução é o uso de um mecanismo de atenção que permite ao modelo aprender onde colocar a atenção na sequência de entrada conforme cada palavra da sequência de saída é decodificada.
Usar uma representação de tamanho fixo para capturar todos os detalhes semânticos de uma frase muito longa é muito difícil. Uma abordagem mais eficiente, no entanto, é ler toda a frase ou parágrafo, em seguida, produzir as palavras traduzidas uma de cada vez, cada vez com foco em uma parte diferente da frase de entrada para reunir os detalhes semânticos necessários para produzir a próxima palavra de saída.
A arquitetura de rede neural recorrente codificador-decodificador com atenção é atualmente o estado da arte em alguns problemas de referência para tradução automática. E essa arquitetura é usada no coração do sistema Google Neural Machine Translation, ou GNMT, usado em seu serviçoGoogle Translate (https://translate.google.com).

Três fraquezas inerentes à Tradução Neural Automática: seu treinamento e velocidade de inferência são lentos, ineficácia em lidar com palavras raras e, às vezes, falha em traduzir todas as palavras na frase de origem.
Embora eficazes, os sistemas de tradução automática neural ainda sofrem alguns problemas, como escalar para vocabulários de palavras maiores e a velocidade lenta de treinamento dos modelos.
Existem atualmente as áreas de foco para grandes sistemas de tradução neural de produção, como o sistema do Google. Um artigo recente do Google mudou a perspectiva sobre tradução, no paper de 2017, Attention Is All You Need, os pesquisadores afirmam que sistemas de tradução automática de última geração são movidos por modelos de atenção.
Reconhecimento de voz (STT - speech to text).

O reconhecimento de fala é um subcampo interdisciplinar da ciência da computação e da linguística computacional que desenvolve metodologias e tecnologias que permitem o reconhecimento e a tradução da linguagem falada em texto por computadores. Também é conhecido como reconhecimento automático de fala, reconhecimento de fala por computador ou fala em texto (STT
- speech to text). Ele incorpora conhecimento e pesquisa nas áreas de ciência da computação ,linguística e engenharia da computação .

Alguns sistemas de reconhecimento de voz requerem "treinamento" (também chamado de"inscrição"), em que um locutor individual lê texto ou vocabulário isolado no sistema.
O sistema analisa a voz específica da pessoa e a usa para ajustar o reconhecimento da fala dessa pessoa,resultando em maior precisão. Os sistemas que não usam o treinamento são chamados de sistemas"independentes do locutor". Os sistemas que usam treinamento são chamados de
"dependentes do locutor".
Os aplicativos de reconhecimento de voz incluem interfaces de usuário de voz, como discagem por voz (por exemplo, "ligar para casa"), roteamento de chamadas (por exemplo, "Eu gostaria de fazer uma chamada a cobrar"), controle de aparelho, palavras-chave de pesquisa (por exemplo,encontre um podcast com palavras específicas foram falados), entrada de dados simples (por exemplo, inserir um número de cartão de crédito), preparação de documentos estruturados (por exemplo, um relatório), determinação das características do locutor, e processamento de voz para texto (por exemplo, processadores de texto ou e-mails).
O termo reconhecimento de voz ou identificação do locutor refere-se à identificação do locutor, e não ao que ele está dizendo. Reconhecer o locutor pode simplificar a tarefa de traduzir a fala em sistemas que foram treinados na voz de uma pessoa específica ou pode ser usado para autenticar ou verificar a identidade de um locutor como parte de um processo de segurança.
Do ponto de vista da tecnologia, o reconhecimento de voz tem uma longa história com várias ondas de grandes inovações. Mais recentemente, o campo se beneficiou dos avanços no aprendizado profundo e big data. Os avanços são evidenciados não apenas pelo aumento de artigos acadêmicos publicados na área, mas também pela adoção da indústria mundial de uma variedade de métodos de aprendizado profundo no projeto e implantação de sistemas de reconhecimento de fala.
QUESTõES CoMENTADAS

1. (FGV - Auditor Federal de Controle Externo (TCU)/Controle Externo/Auditoria
Governamental/2022

Uma organização está implementando um sistema de busca de informações interno, e a equipe de desenvolvimento resolveu avaliar diferentes modelos de linguagem vetoriais que ajudariam a conectar melhor documentos e consultas em departamentos que usam terminologias distintas em áreas de negócio que se sobrepõem. Um dos analistas ressaltou que seria interessante guardar os vetores de todo o vocabulário do modelo em um cache, de forma a aumentar a eficiência de acesso e reduzir certos custos de implantação.
Das alternativas abaixo, aquela que lista apenas os modelos compatíveis com essa estratégia de caching é:
ATF-IDF, BERT;

B Word2Vec, BERT, GPT-2;,
C GloVe, GPT-2;

D Word2Vec, GloVe;
E GPT-2, BERT.

Comentário: Vejamos as definições de cada um dos termos apresentados nas alternativas da questão:
TF-IDF (Term Frequency - Inverse Document Frequency) -> é uma ferramenta utilizada para análise de texto e com isso saber a frequência e o peso das palavras dispostas em documentos dentro de um corpus. O objetivo é medir a importância de uma palavra dentre de um documento considerando a sua presença no próprio documento analisado e sua ausência nos demais documentos.
BERT (Bidirectional Encoder Representations from Transformers) -> é uma ferramenta criada pelo Google para permitir as máquinas entenderem, ou melhor, compreenderem a linguagem humana que foi digitada pelos usuários nos buscadores. Isso muda a maneira como nós,humanos, fazemos a busca, tornando essa tarefa mais amigável de ser feita.

Word2Vec é uma ferramenta de aprendizado não supervisionado para criação de representação vetorial, a qual está presente em textos que utilizem linguagem natural.Essa ferramenta trabalha em pares.
GPT-2 (Generative Pre-Training Transformer 2) -> é uma ferramenta de inteligência artificial utilizada, primordialmente, para geração de textos.
GloVe (Global Vectors for Word Representation) -> é uma ferramenta de aprendizado não supervisionado que é utilizado para representações vetoriais de palavras. Sua missão é,após a análise de um corpus, unir palavras semelhantes.
Desta forma, podemos marcar nossa resposta na alternativa D

Gabarito: Letra D

2. FGV - Auditor Federal de Finanças e Controle (CGU)/Tecnologia da lnformação/"Sem
Especialidade"/2022

Durante a elaboração de um sistema de busca de informações biomédicas, foi construído um modelo de linguagem vetorial não contextuai para estimar relações de similaridade semântica necessárias para comparação entre queries e documentos. Entretanto, verificou-se nos testes iniciais que o desempenho do modelo ficou insatisfatório, devido a muitos termos técnicos presentes nos documentos testados, que não haviam sido incorporados ao modelo.
Para aliviar esse problema, uma tarefa de processamento do texto e seu estágio correspondente no processamento de linguagem natural que poderiam ser aplicados na construção do modelo são, respectivamente:
A Word embedding; Análise léxic;
B Lematização; Análise sintática;

C Decomposição morfológica; Análise léxica;
D Word embedding; Análise semântica;

E Decomposição morfológica; Análise sintática.

Comentário: Primeiramente precisamos conhecer os estágios de PLN: Análise Léxica,
Sintática e Semântica.
A Análise Léxica é responsável por manipular o léxico, que é composto por palavras que armazenam os seus significados e categorias lexicais. Essa etapa é responsável por fazer a verificação ortográfica, podendo ser classificada como: substantivo, verbo,advérbio,
pronome, numeral, preposição, conjunção, interjeição, artigo e adjetivo.

Na análise sintática testa se os sintagmas foram postos na sequência correta, ou seja,
se por exemplo dois substantivos podem se seguir ou não.
A análise semântica precisa entrar no mérito de cada combinação de palavras para entender o contexto e sentido das frases.
Com isso, podemos saber que a Decomposição Morfológica faz parte da Análise Léxica, já que a morfologia é justamente a identificação de substantivos, adjetivos, entre outros. Assim,podemos marcar nossa resposta na alternativa C.

Gabarito: C

3. FGV - Analista (MPE SC)/Dados e Pesquisas/2022

A atividade de classificação de documentos envolve um grande número de tarefas de processamento de linguagem natural, o que pode levar a dúvidas quanto a sua aplicação.
A alternativa que contém apenas tarefas que sejam exemplos de classificação de documentos é:
A análise de sentimento, tokenização;

B POS-tagging, reconhecimento de entidades nomeadas;
C filtragem de SPAM, análise de sentimento;

D análise sintática, POS-tagging;

E filtragem de stopwords, reconhecimento de linguagem.

Comentário: Essa questão apresenta um conjunto de conceitos que podem ser divididos em grandes grupos: tarefas de pré-processamento, estágios de PLN e exemplos de classificação de documentos.
Como tarefas de pré-processamento temos: Tokenização, PoS-Tagging e
Filtragem de
Stopwords, Reconhecimento de entidades nomeadas.

Como estágios de PLN temos a análise sintática

Como exemplos de classificação de texto podemos listar a análise de sentimentos e a filtragem de Spam.
Assim, a nossa resposta encontra-se na alternativa C.

Gabarito: C

4. FGV - Auditor Federal de Controle Externo (TCU)/Controle Externo/Auditoria
Governamental/2022

Considere os documentos A e B a seguir.

A = "Há pessoas que choram por saber que as rosas têm espinho"
B = "Há outras que sorriem por saber que os espinhos têm rosas"

A submatriz da matriz de TF-IDF desses dois documentos correspondente aos termos "Rosas",
"Choram" e "Sorriem", nessa ordem, é:

log 2

1 1 0

0 i '

11 íi.

(C)

log_2

log 2 '

11 .

0 log 2

(E)

1 log 2 0

11 11

1 log 2

Item. .11 11 .

Comentário: Ao observar os documentos acima, vemos que a palavra "rosas"aparece nos dois documentos, portanto é uma palavra considerada comum nos documentos acima. Como estamos diante de uma palavra incomum, sua relevância na submatriz é 0.
A palavra "choram" aparece apenas no documento A, portanto é considerada uma palavra relevante, "inédita", logo, importante. No documento A, ela tem uma relevância e o seu valor na submatriz será logarítmico, Iog2/ll.lá no documento B essa palavra não aparece,portanto para esse documento, ela não tem relevância e seu valor é 0.
A palavra "sorriem" aparece apenas no documento B, portanto é considerada uma palavra relevante, "inédita", logo, importante. No documento B, ela tem uma relevância e o seu valor na submatriz será logarítmico, Iog2/ll. Já no documento A essa palavra não aparece,portanto para esse documento, ela não tem relevância e seu valor é 0.
Apenas com essas três palavras, a submatriz é a seguinte:

0 log2/.1 0

Essa submatriz é encontrada, apenas, na letra C, sendo esse o nosso gabarito.

Gabarito: C

5. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre o processamento de linguagem natural (PLN) assinale a alternativa correta.

a) O processamento é sempre feito sobre uma linguagem formal, como o português.

b) A questão da ambiguidade semântica não deve ser levada em consideração visto que é possível encontrar o significado das frases através do contexto.
c) O PLN pode ser dividido em três grandes ações o processamento, a compreensão do texto e a geração de resposta.
d) A sumarização de texto abstrativa é mais fácil de ser aplicada sobre um texto do que a extrativa.
e) Inteligência artificial é um subconjunto do processamento de linguagem natural.
Comentário: Vamos comentar cada uma das alternativas:

a) (Errada). Português é um exemplo de linguagem natural.

b) (Errada). A ambiguidade semântica deve ser levada em consideração.

c) (Certo). Essas são as 3 grandes ações do PLN: Processamento, compreensão e geração de resposta.
d) (Errada). A sumarização abstrativa é mais complexa do que a extrativa.

e) (Errada). O processamento de linguagem natural é um subconjunto da inteligência artificial.

Gabarito: C

6. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre os conceitos de semântica vetorial assinale a alternativa correta.

a) Um embedding é uma representação geométrica com valor real de algo que geralmente é contínuo.
b) O uso de embeddings é importante por algumas técnicas só entendem valor numéricos,
por exemplo, as redes neurais.

c) Stemming é um processo em que o texto de entrada é dividido em unidades menores.

d) Lematização é um processo para identificar radicais de palavras.

e) Tokenização é a forma original de uma palavra que você costuma encontrar como palavra-
chave em um dicionário

Comentário: Vamos comentar cada uma das alternativas a seguir:

a) (Errada) Um embedding é uma representação vetorial com valor real de algo que geralmente é discreto.
b) (Certo) Exatamente, alguns algortimos, em especial os de redes neurais só trabalham com valores numéricos.
c) (Errado) Stemming é um processo para identificar radicais de palavras.

d) (Errado) Um lema é a forma original de uma palavra que você costuma encontrar como palavra-chave em um dicionário. É também a forma básica da palavra antes da inflexão.A
lematização é usada para reduzir o conjunto de palavras.

e) (Errado) Tokenização é um processo em que o texto de entrada é dividido em unidades menores. Existem dois tipos de tokenização: (1) A tokenização de palavras que divide uma frase em tokens (equivalente a palavras e pontuação) (2) A tokenização de frases que divide um trecho de texto incluindo possivelmente mais de uma frase em frases individuais.
Logo, nossa resposta encontra-se na alternativa B.

Gabarito: B

7. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Uma das formas de reduzir a dimensionalidade em problemas de processamento de linguagem natural é:
a) Usando métodos lineares que procuram por combinações mais relevantes de recursos ou componentes, como o PCA.
b) Usando KNN para procurar os vizinhos mais próximos e agrupá-los em conjuntos semelhantes.
c) Usando dados não estruturados para facilitar a transferência deles entre os algoritmos d) Usando dados abertos pois o cidadão pode contribuir com a redução de dimensionalidade dos dados garantindo sua qualidade.
e) Usando N-grams para representar uma sequência contígua de uma ou mais ocorrências de unidades linguísticas
Comentário: A redução da dimensionalidade pode ser feita de duas maneiras diferentes:

* Mantendo apenas as variáveis mais relevantes do conjunto de dados original (esta técnica é chamada de seleção de recursos)
* Ao encontrar um conjunto menor de novas variáveis, cada uma sendo uma combinação das variáveis de entrada, contendo basicamente as mesmas informações que as variáveis de entrada (esta técnica é chamada de redução de dimensionalidade)
Agora, os métodos ou formas usadas para redução de dimensionalidade podem se utilizar de métodos lineares ou não lineares. Além disso, o resultado obtido pode conter um ou vários recursos dos dados. Essa classificação das formas de redução de dimensionalidade pode ser vista na figura a seguir:
Assim, temos nosso gabarito na alternativa A.

Gabarito: A.

8. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Qual o termo abaixo pode ser definido como uma coleção de documentos associados a um contexto específico:
a) Tokens b) Tópicos c) Corpora d) Corpus e) BibliotecaComentário:

v 1

Corpus k J
Documento

* Combinação de tópicos y
Tópico

* Combinação de termos
Termos

Possuem uma probabilidade associada.
Corpus é uma coleção de documentos de texto sobre os quais aplicaríamos rotinas de mineração de texto ou de processamento de linguagem natural para derivar inferências. Um conjunto de corpus é deonomidando Corpora. Logo, temos a nossa resposta na alternativa D.
Gabarito: D.

9. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre a classificação de texto, assinale a alternativa correta.

a) A classificação de texto é bem diferente da classificação utilizada na mineração de dados,
inclusive em relação ao processo.

b) Um dos tipos de classificação de texto é a classificação binária que vai definir um conjunto de três ou mais classes.
c) No processo de classificação, podemos dividir nossa base em 2 ou 3 partes. Quando dividimos em 3 grupos temos partes específicas para treinamento, teste e validação.
d) Não é necessário transforma o texto em um vetor, pois os algoritmos mais modernos já são capazes de trabalhar com dados textuais diretamente.
e) A avaliação do modelo deve ser feita depois da publicação do mesmo para a comunidade de usuários.
Comentário: Vamos comentar cada uma das alternativas acima:

a) (Errada) A classificação de texto segue a mesmas lógica da tarefa de classificação. O
modelo deve ser treinado com dados rotulados e, em seguida, pode ser usado para prever algo sobre novos textos.
b) (Errada) A classificação binária vai dividir o conjunto de dados em duas classes.

c) (Certa) Na prática, na maioria dos casos dividimos nossos dados em treinamento e teste,mas, em algumas condições usamos um terceiro subconjunto dos dados chamado de validação.
Vamos aproveitar a questão para rever a definição dos 3 conceitos:

* Conjunto de treinamento: Conjunto de exemplos utilizados para a aprendizagem, ou seja,para se adequar aos parâmetros do classificador.

* Conjunto de validação: um conjunto de exemplos usados para ajustar os parâmetros de um classificador, por exemplo, para escolher o número de unidades ocultas em uma rede neural.
* Conjunto de testes: um conjunto de exemplos usados apenas para avaliar o desempenho de um classificador totalmente especificado.
d) (Errada). Errado, algoritmos mais modernos, como BERT, fazem um embedding sobre os dados textuais para transformá-los em valores ou vetores numéricos.
e) (Errada) A avaliação do modelo deve ser feita antes de se pôr o modelo em produção.

Gabarito: C

10. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

* Sobre análise de sentimento, avalie a afirmativa incorreta.

a) O nível de análise por dividido em nível de mensagem, nível de sentença ou nível de entidade/aspecto.
b) O objetivo da análise de sentimento é definir ferramentas automáticas capazes de extrair informações subjetivas de textos em linguagem natural, como opiniões e sentimentos c) A análise de sentimento deve ser capaz de criar um conhecimento estruturado e acionável para ser usado por um sistema de apoio à decisão ou um tomador de decisão.
Podemos classificar uma opinião em regular ou comparativa.

A classificação de polaridade pode definir um texto como positivo, negativo ou neutro,
sendo, portanto, uma classificação objetiva.

Comentário: A questão pede para analisarmos as alternativas e descobrimos a incorreta.
O erro encontra-se na alternativa E. A classificação de polaridade é uma classificação subjetiva,conforme visto na figura abaixo.

Análise de sentimentos

Classificação Subjetiva

Polaridade

Sentença

Objetiva Subjetiva

I

Positiva Negativa Neutra

As demais alternativas fornecem um resumo do assunto.

Gabarito: E

11. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

PLN é uma área que se sobrepõe a outras. Surgiu em campos como inteligência artificial,linguística, linguagens formais e compiladores. Com o avanço das tecnologias de computação e o aumento da disponibilidade de dados, a forma como a linguagem natural está sendo processada mudou. Anteriormente, um sistema tradicional era usado para cálculos. Hoje, cálculos em linguagem natural são feitos usando e técnicas de aprendizado profundo (deep learning).
Assinale a alternativa que preenche corretamente as lacunas acima:

a) Baseado em regras - inteligência artificial b) Baseado em correlação - uma abordagem geométrica c) Baseado em instinto - uma abordagem analítica baseada em dados d) Baseado em regras - uma abordagem clerical e) Baseado em correlação - uma abordagem matricial
Comentário: Essa questão tenta deixar explícito a evolução dos modelos baseados em regras,que eram excessivamente complexos de especificar e não conseguiam cobrir todos os casos,
para os modelos baseados em inteligência artificial, por exemplo as redes neurais, que conseguem capturar nuances dos dados e executar tarefas como uma precisam maior. Os modelos de deep learning são uma evolução dos modelos que permitem capturar ainda mais detalhes das variações dos dados.
Assim, a nossa resposta encontra-se na alternativa A.

Gabarito: A

12. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

A redução de dimensionalidade apresenta diversos benefícios. Dentre as alternativas a seguir,qual destas não apresenta um benefício da redução de dimensionalidade:

a) O espaço necessário para armazenar os dados é reduzido conforme o número de dimensões diminui.
b) Um número menor de dimensões leva a menos tempo de computação/treinamento.

c) Melhora a execução de alguns algoritmos.

d) Trata problemas de multicolinearidade, removendo recursos redundantes.

e) Ajuda a encontrar valores ausentes.

Comentário: Aqui estão alguns dos benefícios da aplicação de redução de dimensionalidade a um conjunto de dados:
O espaço necessário para armazenar os dados é reduzido conforme o número de dimensões diminui
Um número menor de dimensões leva a menos tempo de computação/treinamento

Alguns algoritmos não funcionam bem quando temos grandes dimensões. Portanto, a redução dessas dimensões precisa acontecer para que o algoritmo seja útil.
Ela cuida da multicolinearidade removendo recursos redundantes. Por exemplo, você tem duas variáveis - 'tempo gasto na esteira em minutos' e 'calorias queimadas'. Essas variáveis estão altamente correlacionadas, pois quanto mais tempo você gasta correndo em uma esteira,mais calorias você queima. Portanto, não há nenhuma justificativa para armazenar ambos, pois apenas um deles faz o que você precisa
Ajuda na visualização de dados. É muito difícil visualizar dados em dimensões mais altas,portanto, reduzir nosso espaço para 2D ou 3D pode nos permitir traçar e observar padrões mais claramente
Perceba que encontrar valores ausentes é um benefício da exploração de dados e não da redução de dimensionalidade. Excluir uma coluna com vários valores ausentes pode ser considerado uma redução, mas simplesmente encontrar essa coluna não pode. Assim, temos a nossa resposta na alternativa E.
Gabarito: E

13. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

A classificação de texto é usada em várias aplicações e vários domínios, assinale a opção que não é considerada uma aplicação em que a classificação de textos pode ser usada:
a) Na identificação de idioma, como identificar o idioma de novos tweets ou postagens.

b) Na tradução de texto de português para inglês.

c) Na atribuição de autoria, ou identificação de autores desconhecidos de textos de um grupo de autores.
d) Para a triagem de postagens em um suporte online para serviços de saúde mental.

e) Para segregar notícias falsas de notícias reais.

Comentário: Na lista acima, apenas a tradução de texto não é considerada uma tarefa de classificação de texto. Logo, temos a resposta na alternativa B.
Gabarito: B

14. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural (HARD)

Sobre classificação de texto, assinale a alternativa incorreta:

a) Naive Bayes é um classificador probabilístico que usa o teorema de Bayes para classificar textos com base na evidência vista em dados de treinamento.
b) O desequilíbrio entre elementos das classes é um dos motivos mais comuns para um classificador não ter um bom desempenho.
c) Semântica vetorial é o mapeamento entre o espaço vetorial proveniente da representação distribucional e o espaço vetorial proveniente da representação distribuída.
d) No contexto de PLN, a conversão de texto bruto em uma forma numérica adequada é chamada de representação de texto.
e) A representação de unidades de texto (caracteres, fonemas, palavras, frases,
sentenças,
parágrafos e documentos) como vetores de números é conhecida como modelo de espaço vetorial.
Comentário: Essa questão apresenta conceitos um pouco mais avançados, tenta levar você a se aprofundar em alguns tópicos do assunto ... de cara, posso dizer que o erro da questão está na alternativa C.
Lembre-se que, embedding é um termo usado quando a partir de um conjunto de palavras em um corpus, fazemos um mapeamento entre o espaço vetorial proveniente da representação distribucional e o espaço vetorial proveniente da representação distribuída.
Já a semântica vetorial refere-se ao conjunto de métodos de PLN que objetivam aprender as representações de palavras com base em propriedades de distribuição de palavras em um grande corpus.
Vamos agora comentar um pouco sobre as demais alternativas:

Naive Bayes é um classificador probabilístico que usa o teorema de Bayes para classificar textos com base na evidência vista em dados de treinamento. Ele estima a probabilidade condicional de cada recurso de um determinado texto para cada classe com base na ocorrência desse recurso naquela classe e multiplica as probabilidades de todos os recursos de um determinado texto para calcular a probabilidade final de classificação para cada classe. Por fim, escolhe a classe com probabilidade máxima.
A questão do desequilíbrio entre dados pode ser exemplificada da seguinte forma.
Imagine que vamos classificar textos em relevantes ou irrelevantes para uma pesquisa acadêmica. Se existirem poucos exemplos de artigos relevantes (~ 20%) em comparação com os artigos não relevantes (~ 80%) no conjunto de dados. Esse desequilíbrio de classe faz com que o processo de aprendizagem seja desviado para a categoria de artigos não relevantes, pois há poucos exemplos de artigos "relevantes".
As demais alternativas estão corretas e reforçam a ideia de representação textual e modelo de espaço vetorial vista ao longo da aula.
Gabarito: C

15. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Qual das ações abaixo não é considerada uma das etapas para construção de um sistema de classificação de textos.
a) Coletar ou criar um conjunto de dados rotulado adequado para a tarefa.

b) Dividir o conjunto de dados em dois (treinamento e teste) ou três partes:
treinamento,
validação (ou seja, desenvolvimento) e conjuntos de teste e, em seguida, decidir a(s)
métrica(s)
de avaliação.

c) Transformar o texto bruto em vetores de recursos.

d) Treinar um classificador usando os vetores de recursos e os rótulos correspondentes do conjunto de teste.
e) Usar a(s) métrica(s) de avaliação, comparar o desempenho do modelo no conjunto de teste.

Comentário: A questão apresentar uma casca de banana, mas faz parte do tipo de questão que pode aparecer na sua prova. A alternativa incorreta está na letra D. Na realidade,você deve treinar um classificador usando os vetores de recursos e os rótulos correspondentes do conjunto de treinamento.
Gabarito: D

16. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Não é considerado um caso de uso de modelagem de tópicos:

a) Descrever sistemas interativos que permitem aos usuários interagir em linguagem natural.

b) Usar um documento como como um vetor de recursos para classificação de texto.

c) Projetar um sistema de recomendação de texto d) Resumir documentos ou tweets na forma de palavras-chave com base nas distribuições de tópicos aprendidos e) Detectar tendências de mídia social ao longo de um período
Comentário: A alternativa A apresenta a definição do conceito de chatbots que não tem uma relação com os casos de uso em que a modelagem de tópicos se aplica.
Gabarito: A

17. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

O estudo, usando distribuições estatísticas, de elementos da linguagem para caracterizar semelhanças entre documentos (por exemplo, e-mail), atos de fala (por exemplo, sentenças faladas ou escritas) ou seus elementos (por exemplo, frases, palavras) é denominado:
a) word embeddings b) tokenização c) semântica vetorial d) Hipótese distributiva e) semântica distributiva
Comentário: O conceito descrito na questão é o de semântica distributiva. Outros conceitos próximos que aprendemos na nossa aula são:
Hipótese distributiva - Palavras que ocorrem em contextos semelhantes têm significados semelhantes. Por exemplo, as palavras em inglês "cachorro" e "gato" ocorrem em contextos semelhantes. Assim, de acordo com a hipótese distributiva, deve haver uma forte semelhança entre os significados dessas duas palavras.
Representação distribucional - Refere-se a esquemas de representação obtidos com base na distribuição de palavras a partir do contexto em que as palavras aparecem. Esses esquemas são baseados em hipóteses distributiva.
Representação distribuída - Esquemas de representação distribuída comprimem significativamente a dimensionalidade. Isso resulta em vetores que são compactos (ou seja, de baixa dimensão) e densos (ou seja, quase nenhum zero). O espaço vetorial resultante é conhecido como representação distribuída.
Semântica vetorial - conjunto de métodos de PLN que objetivam aprender as representações de palavras com base em propriedades de distribuição de palavras em um grande corpus.
Logo, temos a nossa resposta na alternativa E.

Gabarito: E

18. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Alguns dos algoritmos de modelagem de tópicos são mais populares. Observer a lista a seguir:

1. Latent dirichlet allocation (LDA),

2. Latent semantic analysis (LSA)

3. Nonnegative matrix factorization (NMF)

4. Probabilistic latent semantic analysis (PLSA),

5. Support Vector Machine (SVM)

Qual dos algoritmos acima são utilizados na modelagem de tópicos de forma ampla.

a) 1, 2 e 3 apenas b) 1, 2, 3 e 4 apenas c) 2, 3, 4 e 5 apenas d) 1, 3 e 5 apenas e) 1, 2 e 4 apenas
Comentário: A modelagem de tópicos serve para extrair tópicos de uma coleção de documentos. É o método de mineração de texto amplamente utilizado no Processamento deLinguagem Natural para obter insights sobre os documentos em texto. Este processo altamente importante pode ser realizado por vários algoritmos ou métodos. Alguns deles são:
* Latent Dirichlet Allocation (LDA)

* Non Negative Matrix Factorization (NMF)

* Latent Semantic Analysis (LSA)

* Parallel Latent Dirichlet Allocation (PLDA)

* Pachinko Allocation Model (PAM)

Assim, temos a nossa reposta na alternativa B.

Gabarito: B

19. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre PLN, assinale a alternativa correta:

a) os tokens são convertidos em números antes de serem entregues a qualquer rede neural b) o processo de conversão de uma frase ou parágrafo em tokens é referido como Stemming c) o processo de remoção de palavras como "a", "e", "até", "uma", "o" de uma frase é chamado de Lemmatização.
d) TF-IDF ajuda a estabelecer uma. palavra que ocorre com mais frequência no documento.

e) as palavras representadas como vetores são chamadas de data frames de palavras neurais
Comentário: Vamos analisar cada uma das alternativas:

a) (Certo) Todas as palavras são convertidas em um número antes de alimentar uma rede neural.
b) (Errado) A declaração descreve o processo de tokenização c) (Errado) O nome do processo de remoção de palavras irrelevantes é chamado de remoção de stop words.
d) (Errado) TF-IDF ajuda a estabelecer a importância de uma palavra específica no contexto do corpus do documento. O TF-IDF leva em consideração a quantidade de vezes que a palavra aparece no documento e balanceada pela quantidade de documentos em que a palavra aparece no corpus.
e) (Errado) As palavras representadas como vetores são chamadas de embeddings de palavras neurais.
Gabarito: A

20. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Qual das seguintes não é uma técnica de pré-processamento em PLN:

a) Derivação e lematização b) Conversão para minúsculas c) Remoção de pontuações d) Remoção de stopwords e) Análise de sentimento
Comentário: A análise de sentimento não é uma técnica de pré-processamento. Esse tipo de análise é feito após o pré-processamento e é um caso de uso de PNL. Todos as outras opções listadas são usadas como parte do pré-processamento de instrução.
Gabarito: E.

Exercícios

1. (FGV - Auditor Federal de Controle Externo (TCU)/Controle Externo/Auditoria
Governamental/2022

Uma organização está implementando um sistema de busca de informações interno, e a equipe de desenvolvimento resolveu avaliar diferentes modelos de linguagem vetoriais que ajudariam a conectar melhor documentos e consultas em departamentos que usam terminologias distintas em áreas de negócio que se sobrepõem. Um dos analistas ressaltou que seria interessante guardar os vetores de todo o vocabulário do modelo em um cache, de forma a aumentar a eficiência de acesso e reduzir certos custos de implantação.
Das alternativas abaixo, aquela que lista apenas os modelos compatíveis com essa estratégia de caching é:
ATF-IDF, BERT;

B Word2Vec, BERT, GPT-2;,
C GloVe, GPT-2;

D Word2Vec, GloVe;
E GPT-2, BERT.

2. FGV - Auditor Federal de Finanças e Controle (CGU)/Tecnologia da lnformação/"Sem
Especialidade"/2022

Durante a elaboração de um sistema de busca de informações biomédicas, foi construído um modelo de linguagem vetorial não contextuai para estimar relações de similaridade semântica necessárias para comparação entre queries e documentos. Entretanto, verificou-se nos testes iniciais que o desempenho do modelo ficou insatisfatório, devido a muitos termos técnicos presentes nos documentos testados, que não haviam sido incorporados ao modelo.
Para aliviar esse problema, uma tarefa de processamento do texto e seu estágio correspondente no processamento de linguagem natural que poderiam ser aplicados na construção do modelo são, respectivamente:
A Word embedding; Análise léxic;
B Lematização; Análise sintática;

C Decomposição morfológica; Análise léxica;
D Word embedding; Análise semântica;

E Decomposição morfológica; Análise sintática.

3. FGV - Analista (MPE SC)/Dados e Pesquisas/2022

A atividade de classificação de documentos envolve um grande número de tarefas de processamento de linguagem natural, o que pode levar a dúvidas quanto a sua aplicação.
A alternativa que contém apenas tarefas que sejam exemplos de classificação de documentos é:
A análise de sentimento, tokenização;

B POS-tagging, reconhecimento de entidades nomeadas;
C filtragem de SPAM, análise de sentimento;

D análise sintática, POS-tagging;

E filtragem de stopwords, reconhecimento de linguagem.

4. FGV - Auditor Federal de Controle Externo (TCU)/Controle Externo/Auditoria
Governamental/2022

Considere os documentos A e B a seguir.

A = "Há pessoas que choram por saber que as rosas têm espinho"
B = "Há outras que sorriem por saber que os espinhos têm rosas"

A submatriz da matriz de TF-IDF desses dois documentos correspondente aos termos "Rosas",
"Choram" e "Sorriem", nessa ordem, é:

log?

1 1 0

(B) 11 11 1

Item. .11 11.

(C)

log?

log 2 '
11 .

0 0

(D)

ii log 2
(E)

1 log 2 0

11 11

1 log 2

Item. .11 11 .

5. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre o processamento de linguagem natural (PLN) assinale a alternativa correta.

a) O processamento é sempre feito sobre uma linguagem formal, como o português.

b) A questão da ambiguidade semântica não deve ser levada em consideração visto que é possível encontrar o significado das frases através do contexto.
c) O PLN pode ser dividido em três grandes ações o processamento, a compreensão do texto e a geração de resposta.
d) A sumarização de texto abstrativa é mais fácil de ser aplicada sobre um texto do que a extrativa.
e) Inteligência artificial é um subconjunto do processamento de linguagem natural.

6. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre os conceitos de semântica vetorial assinale a alternativa correta.

a) Um embedding é uma representação geométrica com valor real de algo que geralmente é contínuo.
b) O uso de embeddings é importante por algumas técnicas só entendem valor numéricos,
por exemplo, as redes neurais.

c) Stemming é um processo em que o texto de entrada é dividido em unidades menores.

d) Lematização é um processo para identificar radicais de palavras.

e) Tokenização é a forma original de uma palavra que você costuma encontrar como palavra-
chave em um dicionário

7. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Uma das formas de reduzir a dimensionalidade em problemas de processamento de linguagem natural é:
a) Usando métodos lineares que procuram por combinações mais relevantes de recursos ou componentes, como o PCA.
b) Usando KNN para procurar os vizinhos mais próximos e agrupá-los em conjuntos semelhantes.
c) Usando dados não estruturados para facilitar a transferência deles entre os algoritmos d) Usando dados abertos pois o cidadão pode contribuir com a redução de dimensionalidade dos dados garantindo sua qualidade.
e) Usando N-grams para representar uma sequência contígua de uma ou mais ocorrências de unidades linguísticas
8. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Qual o termo abaixo pode ser definido como uma coleção de documentos associados a um contexto específico:
a) Tokens b) Tópicos c) Corpora d) Corpus e) Biblioteca
9. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre a classificação de texto, assinale a alternativa correta.

a) A classificação de texto é bem diferente da classificação utilizada na mineração de dados,
inclusive em relação ao processo.

b) Um dos tipos de classificação de texto é a classificação binária que vai definir um conjunto de três ou mais classes.
c) No processo de classificação, podemos dividir nossa base em 2 ou 3 partes. Quando dividimos em 3 grupos temos partes específicas para treinamento, teste e validação.
d) Não é necessário transforma o texto em um vetor, pois os algoritmos mais modernos já são capazes de trabalhar com dados textuais diretamente.
e) A avaliação do modelo deve ser feita depois da publicação do mesmo para a comunidade de usuários.
10. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre análise de sentimento, avalie a afirmativa incorreta.

a) O nível de análise por dividido em nível de mensagem, nível de sentença ou nível de entidade/aspecto.
b) O objetivo da análise de sentimento é definir ferramentas automáticas capazes de extrair informações subjetivas de textos em linguagem natural, como opiniões e sentimentos c) A análise de sentimento deve ser capaz de criar um conhecimento estruturado e acionável para ser usado por um sistema de apoio à decisão ou um tomador de decisão.
d) Podemos classificar uma opinião em regular ou comparativa.

e) A classificação de polaridade pode definir um texto como positivo, negativo ou neutro,
sendo, portanto, uma classificação objetiva.

11. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

PLN é uma área que se sobrepõe a outras. Surgiu em campos como inteligência artificial,linguística, linguagens formais e compiladores. Com o avanço das tecnologias de computação e o aumento da disponibilidade de dados, a forma como a linguagem natural está sendo processada mudou. Anteriormente, um sistema tradicional era usado para cálculos. Hoje, cálculos em linguagem natural são feitos usando e técnicas de aprendizado profundo (deep learning).
Assinale a alternativa que preenche corretamente as lacunas acima:

a) Baseado em regras - inteligência artificial b) Baseado em correlação - uma abordagem geométrica c) Baseado em instinto - uma abordagem analítica baseada em dados d) Baseado em regras - uma abordagem clerical e) Baseado em correlação - uma abordagem matricial
12. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

A redução de dimensionalidade apresenta diversos benefícios. Dentre as alternativas a seguir,qual destas não apresenta um benefício da redução de dimensionalidade:

a) O espaço necessário para armazenar os dados é reduzido conforme o número de dimensões diminui.
b) Um número menor de dimensões leva a menos tempo de computação/treinamento.

c) Melhora a execução de alguns algoritmos.

d) Trata problemas de multicolinearidade, removendo recursos redundantes.

e) Ajuda a encontrar valores ausentes.

13. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

A classificação de texto é usada em várias aplicações e vários domínios, assinale a opção que não é considerada uma aplicação em que a classificação de textos pode ser usada:
a) Na identificação de idioma, como identificar o idioma de novos tweets ou postagens.

b) Na tradução de texto de português para inglês.

c) Na atribuição de autoria, ou identificação de autores desconhecidos de textos de um grupo de autores.
d) Para a triagem de postagens em um suporte online para serviços de saúde mental.

e) Para segregar notícias falsas de notícias reais.

14. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural (HARD)

Sobre classificação de texto, assinale a alternativa incorreta:

a) Naive Bayes é um classificador probabilístico que usa o teorema de Bayes para classificar textos com base na evidência vista em dados de treinamento.
b) O desequilíbrio entre elementos das classes é um dos motivos mais comuns para um classificador não ter um bom desempenho.
c) Semântica vetorial é o mapeamento entre o espaço vetorial proveniente da representação distribucional e o espaço vetorial proveniente da representação distribuída.
d) No contexto de PLN, a conversão de texto bruto em uma forma numérica adequada é chamada de representação de texto.
e) A representação de unidades de texto (caracteres, fonemas, palavras, frases,
sentenças,
parágrafos e documentos) como vetores de números é conhecida como modelo de espaço vetorial.
15. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Qual das ações abaixo não é considerada uma das etapas para construção de um sistema de classificação de textos.
a) Coletar ou criar um conjunto de dados rotulado adequado para a tarefa.

b) Dividir o conjunto de dados em dois (treinamento e teste) ou três partes:
treinamento,
validação (ou seja, desenvolvimento) e conjuntos de teste e, em seguida, decidir a(s)
métrica(s)
de avaliação.

c) Transformar o texto bruto em vetores de recursos.

d) Treinar um classificador usando os vetores de recursos e os rótulos correspondentes do conjunto de teste.
e) Usar a(s) métrica(s) de avaliação, comparar o desempenho do modelo no conjunto de teste.

16. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Não é considerado um caso de uso de modelagem de tópicos:

a) Descrever sistemas interativos que permitem aos usuários interagir em linguagem natural.

b) Usar um documento como como um vetor de recursos para classificação de texto.

c) Projetar um sistema de recomendação de texto d) Resumir documentos ou tweets na forma de palavras-chave com base nas distribuições de tópicos aprendidos e) Detectar tendências de mídia social ao longo de um período
17. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

O estudo, usando distribuições estatísticas, de elementos da linguagem para caracterizar semelhanças entre documentos (por exemplo, e-mail), atos de fala (por exemplo, sentenças faladas ou escritas) ou seus elementos (por exemplo, frases, palavras) é denominado:
a) word embeddings b) tokenização c) semântica vetorial d) Hipótese distributiva e) semântica distributiva
18. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Alguns dos algoritmos de modelagem de tópicos são mais populares. Observer a lista a seguir:

1. Latent dirichlet allocation (LDA),

2. Latent semantic analysis (LSA)

3. Nonnegative matrix factorization (NMF)

4. Probabilistic latent semantic analysis (PLSA),

5. Support Vector Machine (SVM)

Qual dos algoritmos acima são utilizados na modelagem de tópicos de forma ampla.

a) 1, 2 e 3 apenas b) 1, 2, 3 e 4 apenas c) 2, 3, 4 e 5 apenas d) 1, 3 e 5 apenas e) 1, 2 e 4 apenas
19. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Sobre PLN, assinale a alternativa correta:

a) os tokens são convertidos em números antes de serem entregues a qualquer rede neural b) o processo de conversão de uma frase ou parágrafo em tokens é referido como Stemming c) o processo de remoção de palavras como "a", "e", "até", "uma", "o" de uma frase é chamado de Lemmatização.
d) TF-IDF ajuda a estabelecer uma palavra que ocorre com mais frequência no documento.

e) as palavras representadas como vetores são chamadas de data frames de palavras neurais

20. Ano: 2021 Banca: TRC Assunto: Processamento de Linguagem Natural

Qual das seguintes não é uma técnica de pré-processamento em PLN:

a) Derivação e lematização b) Conversão para minúsculas c) Remoção de pontuações d) Remoção de stopwords e) Análise de sentimento
GABArito

1. D

2. C

3. C

4. C

5. C

6. B

7. A

8. D

9. C

10. E

11. A

12. E

13. B

14. C

15. D

16. A

17. E

18. B

19. A

20. E

THIAGO CAVALCANTI

PROFESSOR

