# Engenharia de Software e Sistemas - Metodologia de Desenvolvimento ( Parte 2 )

Índice

1) Metodologias de Desenvolvimento - Parte 2 - Modelo Iterativo e Incremental

2) Metodologias de Desenvolvimento - Parte 2 - Modelos Específicos.

3) Resumo - Metodologias de Desenvolvimento - Parte 2

4) Questões Comentadas - Metodologiasde Desenvolvimento -Parte2 - CESPE

5) Questões Comentadas - Metodologiasde Desenvolvimento -Parte2 - FCC

6) Questões Comentadas - Metodologiasde Desenvolvimento -Parte2 - FGV

7) Questões Comentadas - Metodologiasde Desenvolvimento -Parte2 - DIVERSAS

8) Lista de Questões - Metodologias de Desenvolvimento - Parte 2 - CESPE

9) Lista de Questões - Metodologias de Desenvolvimento - Parte 2 - FCC

10) Lista de Questões - Metodologias de Desenvolvimento - Parte 2 - FGV

11) Lista de Questões - Metodologias de Desenvolvimento - Parte 2 - Diversas.

PRoCESSoS DE DESENVoLVIMENTo

1 - Modelo Iterativo e Evolucionário

INCIDÊNCIA EM PROVA: ALTÍSSIMA

MODELOS
SEQUENCIAIS

PRINCIPAIS MODELOS MODELOS ESPECÍFICOS*

CASCATA OU
CLÁSSICO

MODELO

MODELO
ITERATIVO

MÉTODOS
EORMAIS

BASEADO EM
COMPONENTES

METODOLOGIAS
ÁGEIS

MODELO INCREMENTAL MODELO EVOLimVO

ESPIRAL
PROTOTIPAGEM

EXPLORATÓRIA/ M THROW-AWAY/
EVOLUCIONÁRIA DESCARTÁVEL

Antes de começarmos, eu acho oportuno dizer que a imensa maioria dos autores consideram o modelo evolucionário/evolutivo como um tipo de modelo iterativo conforme mostra a imagem acima! Um dos nossos autores consagrados, Roger Pressman afirma: "os modelos evolucionários são iterativos, apresentando características que possibilitam desenvolver versões cada vez mais completas do software". Agora é hora de ver isso melhor...
Ele também afirma que softwares, assim como outros sistemas complexos, evoluem ao longo do tempo. Conforme o desenvolvimento do projeto avança, as necessidades de negócio e de produto mudam, tornando inadequado seguir um planejamento em linha reta de um produto final.Prazos apertados tornam impossível completar um produto de software abrangente, porém uma versão limitada tem de ser introduzida para aliviar e/ou atender às pressões comerciais ou da concorrência.
Em determinadas situações, faz-se necessário um modelo de processo que tenha sido projetado especificamente para desenvolver um produto que evolua ao longo do tempo e os modelos evolucionários possibilitam desenvolver versões cada vez mais completas de software. Eujá sei que você está com uma dúvida na ponta da língua: professor, qual é a diferença entre o modelo incremental e o modelo evolucionário? Pois é...
Na última edição do livro do lan Sommerville, ele simplesmente desapareceu com o termo modelo evolucionário e o considerou como sinônimo de modelo incremental - como se não houvesse nenhuma diferença entre eles! Já Roger Pressman trata ambos quase como idênticos, a não ser por uma diferença bastante sutil: de acordo com o autor, o modelo incremental sempre apresenta uma funcionalidade operacional ou um produto de trabalho a cada iteração.
Já o modelo evolucionário, durante as primeiras iterações, pode gerar versões compostas apenas por modelos em papel, documentação ou produtos não operacionais para o usuário. Épossível, por exemplo, ter uma iteração utilizada só para estudar melhor o produto. Isso é uma funcionalidade operacional para o cliente? Não! É importante mencionar que muitas questões ignoram essa diferença e simplesmente tratam o modelo evolucionário como modelo incremental!
Bem, pessoal... as implementações mais famosas do modelo evolucionário são:
prototipagem e espiral! Vamos estudá-las um pouco melhor:)
(Senado Federal - 2013) Para Sommerville (2007) modelos evolucionários se caracterizam por sua iteratividade e permitem o desenvolvimento de versões de software cada vez mais completas. Assinale a alternativa que caracteriza os dois tipos processos mais comuns destes modelos:
a) Rup e Cascata.

b) Cascata e incremental.

c) RAID e Cascata.

d) Espiral e Prototipação.

Comentários: modelos evolucionários se dividem em espiral e prototipação (Letra D).

1.1 - Modelos em Prototipagem

INCIDÊNCIA EM PROVA: MÉDIA

Frequentemente, o cliente define uma série de objetivos gerais para o software, mas não identifica detalhadamente os requisitos para funções e recursos. Em outros casos, o desenvolvedor encontra-se inseguro quanto à eficiência de um algoritmo, quanto à adaptabilidade de um sistema operacional ou quanto à forma em que deva ocorrer a interação homem/máquina. Em situações assim e em muitas outras, o paradigma de prototipação pode ser a melhor abordagem.
Embora a prototipação possa ser utilizada como um modelo de processo isolado
(stand-alone process), ela é mais comumente utilizada como uma técnica passível de ser implementada no contexto de outros processos. Independentemente da forma como é aplicado,quando os requisitos estão obscuros, o paradigma da prototipação auxilia os interessados a compreender melhor o que está para ser construído .
A prototipagem é utilizada quando não se conhecem bem os requisitos. Trata-se de uma forma de entendê-los melhor para posteriormente desenvolver o software. Ela se configura como um processo iterativo, interativo e rápido de desenvolvimento e o protótipo serve como um mecanismo de identificação dos requisitos do software, que servirão para uma futura especificação ou serão refinados e entregues ao cliente.
Um protótipo é uma versão inicial de um sistema de software utilizado para demonstrar conceitos, experimentar opções de projeto e, geralmente, conhecer mais sobre o problema e suas possíveis soluções. O desenvolvimento rápido e iterativo do protótipo é essencial para que os custos sejam controlados e os stakeholders do sistema possam experimentá-lo no início do processo de software.
Um protótipo de software pode ser usado em um processo de desenvolvimento de software para ajudar a antecipar as mudanças que podem ser requisitadas:
a) No processo de engenharia de requisitos, um protótipo pode ajudar na elicitação e validação de requisitos do sistema.
b) Processo de projeto do sistema, um protótipo pode ser usado para estudar soluções específicas de software e apoiar o projeto de interface com o usuário.
Protótipos do sistema permitem aos usuários ver quão bem o sistema dá suporte a seu trabalho. Eles podem obter novas ideias para requisitos e encontrar pontos fortes e fracos do software; podem, então, propor novos requisitos do sistema. Além disso, o desenvolvimento do protótipo pode revelar erros e omissões nos requisitos propostos. A função descrita em uma especificação pode parecer útil e bem definida.
No entanto, quando essa função é combinada com outras, os usuários muitas vezes percebem que sua visão inicial foi incorreta ou incompleta. A especificação do sistema pode então ser modificada para refletir o entendimento dos requisitos alterados. Enquanto o sistema está em projeto, um protótipo do sistema pode ser usado para a realização de experimentos de projeto visando à verificação da viabilidade da proposta.
Por exemplo: um projeto de banco de dados pode ser prototipado e testado para verificar se suporta de modo eficiente o acesso aos dados para as consultas mais comuns dos usuários.Prototipação também é uma parte essencial do processo de projeto da interface de usuário Devido à natureza dinâmica de tais interfaces, descrições textuais e diagramas não são bons o suficiente para expressar seus requisitos.
Dessa forma, a prototipação rápida com envolvimento do usuário final é a única maneira sensata de desenvolver interfaces gráficas de usuário para sistemas de software. Um modelo de processo para desenvolvimento de protótipos é apresentado na imagem seguinte. Os objetivos da prototipação devem ser explicitados desde o início do processo (Ex: prototipar a interface de usuário, prototipar um sistema para validação dos requisitos funcionais do sistema, etc).
Estabelecer objetivos do protótipo
Definir

—► funcionalidade do —►
protótipo

Desenvolver protótipo
—► Avaliar o protótipo

O mesmo protótipo não pode cumprir todos os objetivos. Se os objetivos não são declarados, a gerência ou os usuários finais podem não entender a função do protótipo.Consequentemente, eles podem não obter os benefícios que esperavam do desenvolvimento do protótipo.O próximo estágio do processo é decidir o que colocar e, talvez mais importante ainda, o que deixar de fora do sistema de protótipo.
Para reduzir os custos de prototipação e acelerar o cronograma de entrega, pode-se deixar alguma funcionalidade fora do protótipo. Você pode optar por relaxar os requisitos não funcionais, como tempo de resposta e utilização de memória. Gerenciamento e tratamento de erros podem ser ignorados, a menos que o objetivo do protótipo seja estabelecer uma interface de usuário. Padrões de confiabilidade e qualidade de programa podem ser reduzidos.
O estágio final do processo é a avaliação do protótipo. Durante esse estágio,
provisões devem ser feitas para o treinamento do usuário, e os objetivos do protótipo devem ser usados para derivar um plano de avaliação. Os usuários necessitam de um tempo para se sentir confortáveis com um sistema novo e para se situarem em um padrão normal de uso. Uma vez que estejam usando o sistema normalmente, eles descobrem erros e omissões de requisitos.
Já Pressman entende a prototipação conforme apresenta a imagem ao lado: o paradigma de prototipação começa com a comunicação. Faz-se uma reunião com os envolvidos para definir os objetivos gerais do software, identificar quais requisitos já são conhecidos e esquematizar quais áreas necessitam, obrigatoriamente, de uma definição mais ampla.Uma iteração de prototipação é planejada rapidamente e ocorre a modelagem (na forma de um "projeto rápido").
Um projeto rápido se concentra em uma representação daqueles aspectos do software que serão visíveis aos usuários finais (Por exemplo: o layout da interface com o usuário ou os formatos de exibição na tela). O projeto rápido leva à construção de um protótipo, que é empregado e avaliado pelos envolvidos, que fornecerão um retorno (também chamado de feedback), que servirá para aprimorar os requisitos.
A iteração ocorre conforme se ajusta o protótipo às necessidades de vários interessados e, ao mesmo tempo, possibilita a melhor compreensão das necessidades que devem ser atendidas.Na sua forma ideal, o protótipo atua como um mecanismo para identificar os requisitos do software.Caso seja necessário desenvolver um protótipo operacional, pode-se utilizar partes de programas existentes ou aplicarferramentas que possibilitem gerar rapidamente tais programas operacionais.
O que fazer com o protótipo quando este já serviu ao propósito descrito anteriormente? Na maioria dos projetos, o primeiro sistema dificilmente é utilizável. Pode estar muito lento, muito grande, muito estranho em sua utilização ou as três coisas juntas. Não há alternativa, a não ser começar de novo e desenvolver uma versão redesenhada na qual esses problemas são resolvidos. Oprotótipo pode servir, portanto, como "o primeiro sistema"-que pode ser jogado fora!
No entanto, essa pode ser uma visão idealizada. Embora alguns protótipos sejam construídos como"descartáveis", outros são evolucionários, no sentido de que evoluem lentamente até se transformar no sistema real. Tanto os interessados como os engenheiros de software gostam do paradigma da prototipação. Os usuários podem ter uma ideia prévia do sistema final, ao passo que os desenvolvedores passam a desenvolver algo imediatamente.
Em outras palavras, protótipos são inviáveis de serem utilizados na maioria dos casos,
por ser muito lento e/ou muito grande e/ou muito difícil de utilizar. Em geral, os protótipos são descartados assim que os objetivos de levantamento de requisitos são alcançados. No entanto,alguns preferem refiná-los iterativamente até evoluirão sistema final requisitado pelo usuário. O que vocês precisam guardar de tudo isso?
Em suma, o que vocês precisam saber é que o modelo de prototipação/prototipagem se baseia na ideia de construção de um protótipo que auxiliem a construção do produto de duas maneiras: (1)ou para levantar os requisitos do sistema junto aos usuários e depois ser efetivamente descartado; ou (2) para ser refinado, refinado e refinado até chegar ao sistema final desejado pelos usuários.
DESENVOLVIMENTO
EXPLORATÓRIO OU
EVOLUCIONÁRIO

PROTOTIPAÇÃO
THROWAWAYOU

DESTARTÁVEL

O objetivo do processo de desenvolvimento exploratório é trabalhar com o cliente para explorar os requisitos e entregar um sistema final. O desenvolvimento começa com as partes do sistema compreendidas. O sistema evolui por meio da adição de novas características propostas pelo cliente.
O objetivo do processo de prototipação throwaway é compreender os requisitos do cliente e, a partir disso, desenvolver melhor definição de requisitos para o sistema. O protótipo se concentra na experimentação dos requisitos mal compreendidos do cliente, mas é posteriormente descartado.
INDO MAIS

FUNDO!

Quando uma questão não especifica o tipo de prototipação, geralmente se trata de Prototipação
Throw-away/Descartável e, não, Evolucionária/Exploratória. lan Sommerville declara: "O uso o termo prototipação no sentido de processo iterativo de desenvolvimento de um sistema experimental que não é destinado à disponibilização ao cliente".
(TJDFT - 2008) Uma vantagem da prototipação é promover a participação e o comprometimento do usuário em relação ao sistema em desenvolvimento.
Comentários: protótipos permitem que os usuários introduzam novas ideias para os requisitos e encontrem pontos fortes e fracos no software. Ademais, protótipos podem revelar erros e omissões nos requisitos propostos, além de reduzirem o tempo de desenvolvimento, treinamento e documentação o sistema. Logo, a prototipação promove uma grande participação dos usuários no processo de desenvolvimento (Correto).
(INMETRO-2010) Um dos riscos da prototipação é o usuário confundir o protótipo com o sistema verdadeiro e criar falsas expectativas com relação a prazos e recursos.
Comentários: usuários realmente podem confundir o protótipo com o sistema final, sendo que serão descartados posteriormente - trata-se de um erro comum (Correto).
1.2 - Modelo em Espiral

INCIDÊNCIA EM PROVA: MÉDIA

O Modelo em Espiral foi proposto originalmente, em 1988, por Boehm. Sua ideia era representar um processo de software orientado a riscos. Em vez de
Determinar objetivos,
alternativas e restrições

Análise de riscos
Análise

Análise de riscos
Avaliar alternativas,
identificar, resolver riscos representar o processo como uma de riscos „ . . ,
Protótipo 3

f^XProtótipo 2

Protótipo operacional sequência de atividades com algum
REVISÃO

Análise de riscos Protó-
retorno entre uma atividade e outra, o

EEL1

Simulações, modelos, benchmarks processo é representado como uma
Plano de requisitos
Plano de ciclo de vida

Conceito de operação de S"*' Projeto de produto Projeto espiral. Ele combina atividades de desenvolvimento com aspectos gerenciais
Plano de desenvolvimento
Plano de integração

Validação de requisitos
Projeto detalhadoCódigo

Teste unitário

Teste de

(Planejamento, Tomada de Decisão,

Planejar próxima fase e testes
V&V

<7. . integração
Teste de

Análise de Riscos, etc).

Operação aceitai*ao Desenvolver e verificar próximo nível do produto
O modelo em espiral é também conhecido como prototipagem-em-etapas, por combinar, em geral, o modelo em cascata com a prototipação. Cada loop representa uma fase do processo de software. Dessa forma, o loop mais interno pode estar relacionado à viabilidade do sistema; o próximo loop, à definição de requisitos; o próximo, ao projeto de sistema e assim pordiante. Divide-se em quatro setores:

SETORES (POR BOEHM] | DESCRIÇÃO

Definem-se os objetivos da do projeto (aumentar performance, consertar

DETERMINAR OBJETIVOS, ALTERNATIVAS

E RESTRIÇÕES

AVALIAR ALTERNATIVAS, IDENTIFICAR E

RESOLVER RISCOS

funcionalidade, melhorar qualidade), identificam-se alternativas (reúso de componentes, comprar pronto) e identificam-se restrições impostas (custo,cronograma, entre outros).

Avaliam-se as alternativas identificadas em relação aos objetivos e restrições. Frequentemente, esse processo identifica áreas de incerteza
(custos excessivos, falta de recursos) e resolve ou reduz os riscos identificados - um protótipo pode ser construído.
Após a redução dos riscos, um modelo de desenvolvimento para o sistema é selecionado (Exemplo: prototipação evolucionária, modelos formais,modelo em cascata, modelos baseados em componentes). O software é desenvolvido e, posteriormente, testado.
Revisa-se o projeto e decide-se sobre o prosseguimento ao próximo loop da espiral. Se a decisão for pelo prosseguimento, são elaborados planos para a próxima fase do projeto, e terminamos um loop.
Planejamento estimativa de custos cronograma análise de riscos
Modelagem análise projeto
De acordo com Pressman, cada espiral é dividida em cinco setores1:

SETORES (POR PRESSMAN] | DESCRIÇÃO

COMUNICAÇÃO É a comunicação em si

PLANEJAMENTO Estimativa de custos, cronograma e análise de riscos

MODELAGEM Análise e design
CONSTRUÇÃO Codificação e teste
IMPLANTAÇÃO Entrega efeedback

Vocês entenderam isso?O Pressman explica isso por meio da imagem acima! Percebam que o loop mais interno (1) pode tratar do projeto de desenvolvimento de conceito, o segundo loop(2) pode tratar do projeto de desenvolvimento de um produto, o terceiro loop (3) pode tratar do projeto de melhoria e o último (4), mais claro, pode tratar do projeto de manutenção. Pode tratar de todo ciclo de vida...
1 Na edição anterior, eram seis etapas no Modelo em Espiral (Planejamento, Análise de
Riscos, Engenharia, Construção e Liberação, Avaliação do
Cliente e Comunicação com Cliente). Variações do modelo consideram entre três e seis setores da espiral. Infelizmente, cada autor pega a versão original e adapta, criando sua versão, portanto vocês verão muitos nomes diferentes para cada setor.
Cada loop é uma fase e a fase é escolhida de acordo com as necessidades do negócio!
Já os setores do processo são fixos para todos os loops. No entanto, Boehm utiliza uma divisão de setores diferente do Pressman. No caso de dúvida na hora da prova, considerem a versão original doModelo de Boehm. Além disso, ao final de cada loop, há uma tomada de decisão a respeito do projeto.
Vocês perceberam, pela imagem exibida anteriormente, que existem protótipos que são utilizados para verificar a viabilidade do projeto. Ao final de cada loop na espiral, deve-se decidir se o projeto continuará ou se será interrompido. Pessoal, por que esse modelo se destaca em relação aos outros modelos? Porque ele enfatiza bastante um aspecto que o diferencia dos demais: Análise de Riscos.
Este é um modelo complexo que precisa ser gerenciado por pessoas que tenham grande experiência na avaliação de riscos. Geralmente, o modelo é utilizado em sistemas críticos e grandes!Por fim, vamos ver um tema mais polêmico: ele é evolucionário ou é incremental?
Pressman diz que é iterativo, mas, não, incremental-sendo, então, evolucionário. Logo, é nele em que vamos nos basear!
O conceito essencial do modelo é minimizar os riscos pelo uso repetido de protótipos e outros meios. Ao contrário de outros modelos, em cada fase a análise de risco é realizada.O modelo funciona através da construção de versões progressivamente mais completas do software,iniciando no centro da espiral para o exterior. A cada volta, o cliente avalia o trabalho e são feitas sugestões.
O modelo, então, se diferencia porter uma abordagem cíclica, para aumentar incrementalmente o grau de definição e de implementação de um sistema enquanto diminui seu grau de risco; e por ter conjunto de marcos de ancoragem, para garantir o comprometimento dos interessados com soluções exequíveis e mutuamente satisfatórias para o sistema. Vamos ver agora suas maiores vantagens e desvantagens:
| VANTAGENS
DESVANTAGENS |

Suporta mecanismos de redução de riscos. Exige analistas de risco bastante experientes.
Obtêm-se versões do sistema a cada iteração. Exige uma equipe de desenvolvimento extremamente qualificada.
Entregando produtos cada vez mais refinados e de melhor qualidade.
Exige um gerenciamento de processo mais complexo.

Reflete as práticas reais de engenharia atual. Não é recomendado resolver problemas mais simples e pequenos.
Apresenta uma abordagem sistemática.
Apresenta estimativas realistas.

Pessoal, é importante ver como esse modelo é tratado por Roger Pressman. De acordo com o autor,o modelo espiral é um modelo de processo de software evolucionário que acopla a natureza iterativa da prototipação com os aspectos sistemáticos e controlados do modelo cascata.Fornece potencial para o rápido desenvolvimento de versões cada vez mais completas do software.Usando-se o modelo espiral, o software será desenvolvido em uma série de versões evolucionárias.

Nas primeiras iterações, a versão pode consistir em um modelo ou em um protótipo. Já nas iterações posteriores, são produzidas versões cada vez mais completas do sistema que passa pelo processo de engenharia. Assim que esse processo evolucionário começa, a equipe de software realiza atividades indicadas por um circuito em torno da espiral no sentido horário,começando pelo seu centro. Os riscos são considerados à medida que cada revolução é realizada.
Diferente de outros modelos de processo, que terminam quando o software é entregue, o modelo espiral pode ser adaptado para ser aplicado ao longo da vida do software. Em sua essência, a espiral permanece em operação até que o software seja retirado. Trata-se de uma abordagem realista para o desenvolvimento em larga escala. Pelo fato de o software evoluir à medida que o processo avança, desenvolvedor e cliente compreendem e reagem melhor aos riscos em cada evolução.
Esse modelo usa a prototipação como mecanismo de redução de riscos e torna possível a aplicação da prototipação em qualquer estágio do processo evolutivo do produto. Mantém a abordagem em etapas sugerida pelo ciclo de vida clássico, mas a incorpora em uma metodologia iterativa que reflete mais o mundo real. O modelo espiral requer consideração direta dos riscos técnicos em todos os estágios e é capaz de reduzir riscos antes de se tornarem problemáticos.
(ANTAQ - 2009) O modelo em espiral, que descreve o processo de desenvolvimento de um software, apresenta uma espiral em que cada loop representa uma fase distinta desse processo. A ausência de risco nesse modelo o diferencia dos demais modelos de software.
Comentários: na verdade, é a presença da análise de riscos que 0 diferencia (Errado).

(IPEA-2003) O modelo espiral é um modelo evolucionário de processo de software que combina a prototipagem com o modelo em cascata. Contudo, a incerteza em relação ao número de ciclos necessários para construir o projeto, leva tal abordagem a empregar o modelo de métodos formais para viabilizá-lo.
Comentários: a primeira parte do enunciado está perfeita! No entanto, não faz sentido empregar 0
modelo de métodos formais porque não se sabe estimar 0 número de ciclos para construir um projeto. Ele tem uma natureza iterativa que permite reduzir riscos a cada loop (Errado).
Cada loop é uma fase do processo de sofWare

Foco EXPLÍCITO na J
Análise de Risco

= Cascata + Prototlpação
(Prototlpação - em - Etapas)

V 1

Setores (por Pressman 9a Ed)

Comunicação
Planejamen+o

Modelagem 1

í

Modelo Espiral

I

Setores (por Boehm)

Avaliar alternativas, identificar e resolver riscos

«Demsenvaolver e testar

Setores (por Pressman 7a Ed)
Comunicação
Planejamento

Análise de Riscos

Setores (Variação) Avaliação do cliente

Fases não são fixas, atividades sim. No entanto,atividades não são obrigatórias
Planejamento

Análise de Riscos ou Avaliação de Alternativas e deRiscos
Engenharia, Execução ou Desenvolvimento de Software

Modelos Específicos

Métodos Formais

INCIDÊNCIA EM PROVA: BAIXÍSSIMA

Agora vamos falar sobre alguns modelos específicos que caem bem menos que os anteriores!Professor, por que esse nome? Bem, é só para agrupar modelos que não se encaixam diretamente em outros grupos. Comecemos pelos Métodos Formais, termo usado para indicar atividades que contem com representações matemáticas de software, especificação formal, prova de especificação, desenvolvimento transformacional, entre outros.
Esse modelo é utilizado em ambientes extremamente complexos com requisitos rigorosos. São bastante lentos e dispendiosos, além de exigirem um treinamento intensivo. Em geral, são utilizados para o desenvolvimento de sistemas que necessitam de grande robustez e confiabilidade diante da possibilidade de perda de vidas ou sério prejuízo, caso haja falhas. Os chamados métodos formais não são amplamente usados no desenvolvimento de software industrial.
A maioria das empresas de desenvolvimento de software não considera adequados com relação aos seus custos. Por outro lado, a especificação formal é uma excelente maneira para descobrir erros de especificação e apresentar a especificação do sistema de modo não ambíguo. As poucas organizações que têm feito investimentos em métodos formais têm constatado menos erros no software entregue aos clientes e tudo isso sem aumento de custos.
Os métodos formais podem ser adequados em termos de custo caso seu uso seja limitado a partes do núcleo do sistema e caso as empresas desejem fazer alto investimento inicial nessa tecnologia. Professor, pode dar um exemplo de método formal? Sim! O Método Cleanroom,que trata o desenvolvimento semelhante a uma sala limpa de cirurgia. Vamos ver mais alguns detalhes importante...
Métodos Formais são métodos utilizados para elaboração de sistemas computacionais dando prioridade a sua coesão, isto porque estes métodos são desenvolvidos a partir de princípios matemáticos que garantem a sua exatidão na capacidade de expressão das ideias vinculadas ao projeto de software. Estes métodos foram desenvolvidos para auxiliar todas as etapas de desenvolvimento de software1. Vejamos as etapas:
ETAPAS | DESCRIÇÃO

ESPECIFICAÇÃO FORMAL PARA
DEFINIÇÃO DE REQUISITOS

REFINAMENTO PARA
CONCEPÇÃO DE PROJETO

SÍNTESE PARA
IMPLEMENTAÇÃO

PROTOTIPAÇÃOPARA

VALIDAÇÃO
PROVA PARA A VERIFICAÇÃO

Busca formalizar os requisitos descobertos utilizando algum método formal, criando uma modelagem com o uso de elementos.
Busca conceber o projeto de software, ou seja, nesta fase é pensado na arquitetura do sistema com seus diversos componentes e suas interfaces, dados e relacionamentos entre os mesmos.
Busca gerar esqueleto de código, a partirdo modelo refinado, que pode servircomo base para implementação real do sistema.
Busca elaborar um protótipo funcional do sistema para validar se o mesmo, atende as necessidades do cliente.
Busca verificar se o sistema desenvolvido foi concebido atendendo a todos os
Requisitos Funcionais e Não-Funcionais elicitados.

O uso de métodos formais pode ser aplicado durante todas as etapas de desenvolvimento do software ou somente em algumas etapas ou partes do projeto de desenvolvimento. De acordo comRoger Pressman, os métodos formais possibilitam especificar, desenvolver e verificar um sistema baseado em computadoratravés da aplicação de uma notação matemática rigorosa. Eles oferecem um mecanismo que elimina muitos dos problemas difíceis de ser superados com outros modelos.
Ambiguidade, incompletude e inconsistência podem ser descobertas e corrigidas mais facilmente — não por meio de uma revisão local, mas devido à aplicação de análise matemática.Quando são utilizados métodos formais durante o projeto, servem como base para verificar a programação e, portanto, possibilitam que se descubra e se corrijam erros que, de outra forma,poderiam passar despercebidos.

Embora não seja uma abordagem predominante, ele oferece a promessa de software sem defeitos.No entanto, foram mencionados motivos para preocupação a respeito de sua aplicabilidade em um ambiente de negócios: (1) atualmente, o desenvolvimento de modelos formais consome muito tempo e dinheiro; (2) pelo fato de poucos desenvolvedores de software possuírem formação e experiência necessárias para aplicação dos métodos formais, é necessário treinamento extensivo.
1 Pode ser utilizado também para modelar hardwares.

(3) É difícil usar os modelos como um meio de comunicação com clientes tecnicamente despreparados (não sofisticados tecnicamente). Apesar de tais preocupações, a abordagem de métodos formais tem conquistado adeptos entre os desenvolvedores de software que precisam desenvolver software com fator crítico de segurança, bem como entre desenvolvedores que sofreriam pesadas sanções econômicas se ocorressem erros no software.
Já lan Sommerville afirma que, por mais de 30 anos, muitos pesquisadores têm defendido o uso de métodos formais de desenvolvimento de software. Os métodos formais são abordagens baseadas em matemática para o desenvolvimento de software, em que é definido um modelo formal do software. É possível analisar formalmente esse modelo e usá-lo como base para uma especificação formal de sistema.
Em princípio, é possível começar com um modelo formal de software e provar que o programa desenvolvido é consistente com o modelo, eliminando-se, assim, falhas de software resultantes de erros de programação. O ponto de partida para todos os processos formais de desenvolvimento é um modelo formal de sistema, que serve como uma especificação de sistema. Para criar esse modelo, você traduz os requisitos de usuário do sistema. Como assim, Diego?
Os requisitos de usuário são expressos em linguagem natural, diagramas e tabelas - a ideia é representá-los em uma linguagem matemática que defina formalmente a semântica. Aespecificação formal é uma descrição inequívoca do que o sistema deve fazer (sem ambiguidades).Usando métodos manuais ou apoiados por ferramentas, é possível verificar se o comportamento de um programa é consistente com a especificação.
As especificações formais não são apenas essenciais para uma verificação do projeto e implementação do software. Elas são a maneira mais precisa de especificação dos sistemas e,assim, de redução da possibilidade de mal-entendidos. Além disso, a construção de uma especificação formal força uma análise detalhada dos requisitos, e essa é uma maneira eficaz de descobrir problemas de requisitos.
Em uma especificação em linguagem natural, os erros podem ser ocultados pela imprecisão da linguagem. Já as especificações formais, em geral, são desenvolvidas como parte de um processo baseado em planos, no qual o sistema é completamente especificado antes do desenvolvimento.Apesar dessas vantagens, os métodos formais tiveram um impacto limitado no desenvolvimento prático de software, mesmo para sistemas críticos.
(UNEMAT - 2012 - A) Métodos Formais é o termo usado para definir o processo de especificação de software fundamentado em linguagens formais.
Comentários: métodos formais realmente definem um processo de especificação de software baseado em linguagens formais(Correto).

Modelo Baseado Em Componentes

INCIDÊNCIA EM PROVA: BAIXA

Pessoal, vocês já pararam para pensar porque a disciplina de Engenharia de Software é denominada Engenharia de Software? Vamos contar essa história: esse conceito surgiu em 1968, em uma conferência organizada para discutir a Crise do Software. Essa crise foi o resultado da introdução de circuitos integrados em computadores. E isso era ruim, professor? Não, pelo contrário!
Desde o ingresso dos circuitos integrados, tornou-se possível e viável fazer aplicações extremamente complexas. No entanto, o desenvolvimento de software era bastante informal e incipiente, criando softwares, cujo custo superava as previsões, não confiáveis, difíceis de manter e de desempenho insatisfatório. Naquela época, os custos de hardware estavam caindo,enquanto os custos de software aumentavam rapidamente.
Novas técnicas e métodos eram necessários para controlar a complexidade inerente aos grandes sistemas de software. E por que 0 nome engenharia de software? Porque foi uma tentativa de contornar a crise ao utilizar princípios de engenharia, a fim de obter um software de maneira econômica e que fosse confiável, dando um tratamento mais sistemático e controlado(comum às engenharias) ao desenvolvimento de sistemas de software complexos.
Pessoal, pensem comigo: a engenharia evolui seus métodos há centenas de anos,
enquanto o desenvolvimento de software é bastante recente! Logo, faz sentido utilizar os conceitos consolidados de engenharia para melhorar seus processos de desenvolvimento de software.Não acham? Ok, professor! Mas 0 que isso tem a ver com reúso de componentes? Ora, aEngenharia é especializada em produzir componentes reusáveis.
Engenheiros raramente fabricam um componente a partirdo nada. Eles baseiam seus projetos em componentes exaustivamente testados em outros sistemas. Quando se fala em Modelo baseado em Componentes, refere-se a uma estratégia de engenharia de software na qual o processo de desenvolvimento é voltado à reusabilidade. E qual a vantagem disso? Isso resulta em redução de custos de produção e manutenção, entregas mais rápidas e aumento de qualidade.
A abordagem para desenvolvimento de software Component-Based Software Engineering
(CBSE)
tem utilizado o reúso como peça principal. Essa abordagem depende de uma grande base de componentes reusáveis e algum framework de integração. Apesar não termos valores precisos,sabemos que os custos de desenvolvimento são menores que os custos de integração e de teste.
Esses custos aumentam porque é necessário assegurar que os componentes utilizados realmente satisfazem às especificações e funcionam com outros componentes. Agora voltando um pouco: o que seria exatamente um componente? Pressman afirma que é um bloco de construção modular,isto é, uma parte do sistema modular, executável, implantável, independente, padronizada e reutilizável que encapsula a implementação e expõe um conjunto de interfaces do sistema.
ESPECIFICAÇÃO DE
REQUISITOS

ANÁLISE DE
COMPONENTES

ALTERAÇÃO DE
REQUISITOS

VALIDAÇÃO DE
SISTEMA

DESENVOLVIMENTO
E INTEGRAÇÃO

PROJETO DE
SISTEMA COM
REÚSO

FASES 00 MODELO
BASEADO EM
COMPONENTES

ESPECIFICAÇÃO DE

REQUISITOS

ANÁLISE DE
COMPONENTES

MODIFICAÇÃO DE
REQUISITOS

DESCRIÇÃO

Tem o objetivo de traduzir as informações coletadas durante a atividade de análise em um documento que define um conjunto de requisitos de software. Devem ser incluídos dois tipos de requisitos nesse documento: os Requisitos de Usuário e Requisitos de Sistema.
Nesta fase, é feita uma busca pelos componentes para implementar essa especificação.
Geralmente, não existe uma correspondência exata entre o componente encontrado e o procurado. Muitas vezes, os componentes que podem ser usados fornecem apenas parte da funcionalidade necessária.
Os requisitos são analisados usando as informações sobre os componentes encontrados, que são modificados para refletir os componentes disponíveis. Quando as modificações são impossíveis, a atividade de análise de componentes pode ser novamente realizada para procurar alternativas.
O framework do sistema é projetado ou um framework existente é reutilizado. Os projetistas levam em consideração os componentes reusados. Pode ser necessário projetar algum software novo caso os componentes reusáveis não estejam disponíveis para aquisição para o sistema.
Software que não pode ser adquirido externamente é desenvolvido e os componentes e os sistemas COTS são integrados para criar os novos sistemas. A integração de sistema, neste modelo, pode ser parte do processo de desenvolvimento, em vez de ser uma atividade separada.
Processo de verificação de se um sistema atende às necessidades e expectativas do cliente.
Professor, o que são Sistemas COTS? Esse é o acrônimo de Commercial Off-The-Shelf, que é um conjunto de soluções pré-fabricadas e disponíveis no mercado, podendo ser compradas ou licenciadas, i.e., uma grande biblioteca de componentes prontos.
Os Componentes COTS são desenvolvidos por vendedores que os oferecem como produtos,disponibilizam a funcionalidade almejada juntamente com as interfaces bem definidas,
sendo que essas interfaces permitem que o componente seja integrado ao software a ser desenvolvido. Omodelo de desenvolvimento baseado em componentes incorpora muitas das características do modelo espiral.
Ele é evolucionário por natureza, demandando uma abordagem iterativa para a criação de software. O modelo de desenvolvimento baseado em componentes desenvolve aplicações a partir de componentes de software pré-empacotados e conduz ao reúso do software; sendo que essa reusabilidade proporciona uma série de benefícios mensuráveis aos engenheiros de software.O modelo evolucionário assume que recursos adicionais podem ser adicionados, se necessários.

No entanto, componentes de software de prateleira (COTS) não podem ser atualizados por uma equipe de desenvolvimento particular. A ausência de código-fonte barra a equipe de desenvolvimento de ajustar estes componentes de software para suas necessidades. Então,apesar de conter algumas características do modelo em cascata e do modelo evolucionário, ele não pode ser considerado como parte desses modelos.
(SERPRO - 2008) O modelo orientado a reúso parte de um software existente para que se crie outro, no todo ou apenas em parte de seus componentes.
Comentários: esse modelo realmente parte de um software ou componente existente para se criar outro
(Correto).

(SERPRO-2004) O grande objetivo do uso de engenharia de software porcomponentes é a produção de software de alta qualidade e baixo custo.
Comentários: de fato, criam-se componentes de alta qualidade e baixo custo de produção e manutenção
(Correto).

Modelo Orientado a Aspectos

INCIDÊNCIA EM PROVA: BAIXA

A maioria dos processos de desenvolvimento de software vem considerando sistemas com unidades cada vez menores de desenvolvimento, isto é, vem modularizando cada vez mais os sistemas. A Engenharia de Software provê as bases para o desenvolvimento de software,já as linguagens de programação permitem a abstração de unidades e composição destas de inúmeras formas possíveis.
Sabe-se que no desenvolvimento de software existem propriedades que não se enquadram em componentes da decomposição funcional, tais como: tratamento de exceções, restrições de tempo real, distribuição e controle de concorrência. Vocês compreendem isso? A grande maioria das unidades de programação podem ser decompostas em uma função, porém existem unidades que não podem.
Qual o problema, professor? Bem, essas unidades normalmente ficam espalhadas em diversos componentes do sistema afetando a performance e a semântica da aplicação.Vamos traduzir?
Quando nós modularizamos um sistema, torna-se mais fácil e intuitivo entender o funcionamento de uma aplicação; essas unidades que não podem ser decompostas em funções atrapalham esse entendimento.
Imaginem que temos um método que recebe um valor, realiza um processamento e devolve outro valor. Uma função dentro desse método possui um tratamento de exceção! Galera,tratamento de exceção não faz parte da funcionalidade principal, no entanto - mesmo assim - ela fica presente no código (atrapalhando a modularização e o acoplamento). De fato, essas unidades podem ser visualizadas e analisadas relativamente em separado.
No entanto, sua implementação utilizando linguagens orientadas a objeto ou estruturadas torna-se confusa e seu código encontra-se espalhado através do código da aplicação, dificultando a separação da funcionalidade básica do sistema dessas propriedades. A Programação Orientada a Aspectos (POA) é uma abordagem que permite a separação dessas propriedades ortogonais2dos componentes funcionais de uma forma natural e concisa.

Ela se utiliza de mecanismos de abstração e de composição para a produção de código executável.Vocês podem me perguntar: Professor, por que não podemos utilizar programação orientada a objetos ou programação estruturada? Atualmente, conhecem-se vários problemas de programação em que astécnicas de orientação a objetos ou de programação estruturada não são suficientes para separar claramente todas as decisões de projeto que o programa deve implementar.
Isto se deve ao fato de que as abordagens mais utilizadas se concentram em encontrar e compor unidades funcionais da decomposição do sistema. Já outras questões importantes não são bem localizadas no projeto funcional. Exemplos disto podem ser propriedades que envolvem várias unidades funcionais, tais como: sincronização, restrições de tempo,concorrência,
distribuição de objetos, persistência, etc.

Em suma, POA é um paradigma de desenvolvimento de software que separa responsabilidades,
requisitos e interesses de um sistema. A modularização dos aspectos produz uma arquitetura fácil de projetar, implementar e manter. Muitos acham que esse paradigma veio para substituir aProgramação Orientada a Objetos (POO). Está certo isso? Claro que não! POA
veio para complementar a POO (visto que utilizá-la isoladamente não traz benefícios para o projeto).
Para tal, ela mantém o foco na separação de interesses (Separation of
Concerns), que são requisitos específicos que devem ser atendidos para satisfazer o objetivo de um sistema, mas que não pertencem ao domínio do negócio. Há dois tipos: (1) InteressesPrincipais (Core
Concerns): capturam as funcionalidades centrais de um módulo; (2) Interesses
Ortogonais
(Crosscutting Concerns): capturam funcionalidades periféricas.

Por que separar interesses? Porque, dessa forma, gera-se código de melhor qualidade;
gera-se maior modularidade; facilita-se atribuição de responsabilidade entre módulos distintos; promove-se a reusabilidade de código; facilita-se a evolução de software; viabiliza-se a análise do problema dentro de domínios específicos; entre outras tantas vantagens. Ok, professor...mas 0 que são exatamente aspectos?
Aspectos são propriedades de um sistema envolvendo diversos componentes funcionais que não podem ser expressos usando notações e linguagens atuais de uma maneira precisa (Ex:sincronização, persistência, interação entre componentes, etc). Os interesses são carregados em um módulo chamado aspecto. Professor, um aspecto é um componente?Não, componentes podem ser encapsulados em um procedimento generalizado (objeto, método, procedimento, etc).
2 Quando duas propriedades sendo programadas devem ser compostas de maneira diferente e ainda coordenarem-se é dito que elas são ortogonais entre si.
Aspectos, em geral, não são unidades de decomposição funcional do sistema, mas propriedades que envolvem diversas unidades de um sistema, afetando a semântica dos componentes funcionais sistematicamente. Por exemplo: controle de concorrência em operações em uma mesma conta bancária, registro das transações de uma determinada conta, política de segurança de acesso aos usuários de um sistema, restrições de tempo real associadas à entrega de mensagens.
Dada a definição de componentes e aspectos, é possível colocar o objetivo da programação orientada a aspectos: oferecer suporte para o programador na tarefa de separar claramente os componentes dos aspectos, os componentes entre si e os aspectos entre si,utilizando-se de mecanismos que permitam a abstração e composição destas, produzindo o sistema desejado3.E o que Roger Pressman tem a dizer sobre esse paradigma? Vejamos...
Independentemente do processo de software escolhido, os desenvolvedores de software complexos, invariavelmente, implementam um conjunto de recursos, funções e conteúdo localizados. Essas características de software localizadas são modeladas como componentes (por exemplo, classes orientadas a objetos) e, em seguida, construídas dentro do contexto da arquitetura do sistema.
À medida que os modernos sistemas baseados em computadores se tornam mais sofisticados,certas restrições - propriedades exigidas pelo cliente ou áreas de interesse técnico —
se estendem por toda a arquitetura. Algumas restrições são propriedades de alto nível de um sistema (Ex:segurança, tolerância a falhas). Outras afetam funções (Ex: a aplicação de regras de negócio), sendo que outras são sistêmicas (Ex: sincronização de tarefas ou gerenciamento de memória).
De acordo com o autor, o modelo orientado a aspectos é um paradigma de engenharia de software relativamente novo que oferece uma abordagem metodológica e de processos para definir,especificar, projetar e construir aspectos. Já lan Sommerville nos oferece uma visão mais detalhada
- ele nos introduz o assunto da seguinte maneira: na maioria dos sistemas de grande porte, os relacionamentos entre requisitos e componentes de programa são complexos.
Um único requisito pode ser implementado por uma série de componentes, e cada componente pode incluir elementos de vários requisitos. Na prática, isso significa que mudar requisitos pode envolver o entendimento e a alteração de vários componentes. Como alternativa, um componente pode prover alguma funcionalidade central, mas também incluir o código que implementa vários requisitos de sistema.
Mesmo quando parece haver reúso significativo em potencial, pode ficar caro reusar tais componentes. O reúso pode envolver sua alteração para remover um código extra que não esteja associado com a funcionalidade central do componente. O modelo orientado a aspectos é uma abordagem para desenvolvimento de software que se propõe a resolver esse problema e tornar os programas mais fáceis de manter e reusar.
3 AspectJ é a mais famosa linguagem de programação orientada a aspectos.

Ela é baseada em abstrações chamadas aspectos, que implementam funcionalidade de sistema que pode ser requerida em vários lugares diferentes em um programa. Eles encapsulam a funcionalidade que cruza e coexiste com outra funcionalidade que existe no sistema e são usados junto com outras abstrações, como objetos e métodos. O principal benefício de uma abordagem orientada a aspectos é que ela suporta a separação de interesses.
Separar interesses em elementos diferentes em vez de incluir interesses diferentes na mesma abstração lógica é uma boa prática de engenharia de software. Ao apresentar interesses transversais como aspectos, esses interesses podem ser entendidos, reusados e modificados de forma independente, sem a preocupação de onde o código é usado. Um exemplo clássico é a autenticação de usuário...
A autenticação de usuário é uma funcionalidade que pode ser representada como um aspecto que requisita um nome de usuário e uma senha. Isso pode serautomaticamente embutido no programa sempre que uma autenticação for requerida. Digamos que você tenha um requisito de que a autenticação de usuário seja requerida antes de qualquer alteração dos detalhes pessoais ser feita no banco de dados - isso pode ser um aspecto.
RESUMo

MODELO EVOLUCIONÁRIO

Modelo Evolucionário x Iterativo: o modelo evolucionário funciona também com base em iterações ou repetições com o intuito de refinar o software a partir do feedback do cliente. Aideia é utilizar um esboço inicial e ir incrementando, melhorando, aperfeiçoando o software de acordo com as necessidades dos clientes até chegara uma versão. Ao fim, o sistema pode ser entregue ao cliente ou ser refeito de forma mais estruturada.
MODELO EM PROTOTIPAGEM

Estabelecer objetivos do protótipo
Definir

—► funcionalidade do —►
protótipo

Desenvolver protótipo
—► Avaliar o protótipo

Plano de prototipação
Protótipo

Definição geral executável

Relatório de avaliação
DESENVOLVIMENTO
EXPLORATÓRIO OU
EVOLUCIONÁRIO

PROTOTIPAÇÃO
THROWAWAYOU

DESTARTÁVEL

O objetivo do processo de desenvolvimento exploratório é trabalhar com o cliente para explorar os requisitos e entregar um sistema final. O desenvolvimento começa com as partes do sistema compreendidas. O sistema evolui por meio da adição de novas características propostas pelo cliente.
O objetivo do processo de prototipação throwaway é compreender os requisitos do cliente e, a partir disso, desenvolver melhor definição de requisitos para o sistema. Oprotótipo se concentra na experimentação dos requisitos mal compreendidos do cliente, mas é posteriormente descartado.
MODELO EM ESPIRAL

O Modelo em Espiral foi proposto originalmente, em 1988, por Boehm. Sua ideia era representar um processo de software orientado a riscos. Em vez de representar 0 processo como uma sequência de atividades com algum retorno entre uma atividade e outra, o processo é representado como uma espiral. Éconhecido como prototipagem-
em-etapas, por combinar, em geral, 0 modelo em cascata com a prototipação. Cada loop representa uma fase do processo de software.
SETORES (POR BOEHM) | DESCRIÇÃO

Definem-se os objetivos da do projeto (aumentar performance, consertar

DETERMINAR OBJETIVOS, ALTERNATIVAS

E RESTRIÇÕES

funcionalidade, melhorar qualidade), identificam-se alternativas (reúso de componentes, comprar pronto) e identificam-se restrições impostas (custo,cronograma, entre outros).

AVALIAR ALTERNATIVAS, IDENTIFICAR E

RESOLVER RISCOS

DESENVOLVERETESTAR

PLANEJAR PRÓXIMAS FASES

Avaliam-se as alternativas identificadas em relação aos objetivos e restrições. Frequentemente, esse processo identifica áreas de incerteza(custos excessivos, falta de recursos) e resolve ou reduz os riscos identificados - um protótipo pode ser construído.
Após a redução dos riscos, um modelo de desenvolvimento para o sistema é selecionado (Exemplo: prototipação evolucionária, modelos formais,modelo em cascata, modelos baseados em componentes). O software é desenvolvido e, posteriormente, testado.
Revisa-se o projeto e decide-se sobre o prosseguimento ao próximo loop da espiral. Se a decisão for pelo prosseguimento, são elaborados planos para a próxima fase do projeto, e terminamos um loop.
Planejamento estimativa de custos cronograma análise de riscos
VANTAGENS

Suporta mecanismos de redução de riscos.
Obtêm-se versões do sistema a cada iteração.

Entregando produtos cada vez mais refinados e de melhor qualidade.
Reflete as práticas reais de engenharia atual.
Apresenta uma abordagem sistemática.

DESVANTAGENS

Exige analistas de risco bastante experientes.

Exige uma equipe de desenvolvimento extremamente qualificada.
Exige um gerenciamento de processo mais complexo.

Não é recomendado resolver problemas mais simples e pequenos.
Apresenta estimativas realistas.

MÉTODOS FORMAIS

Métodos Formais permitem indicar atividades que contem com representações matemáticas de software,especificação formal, prova de especificação, desenvolvimento transformacional, etc. Esse modelo é utilizado em ambientes extremamente complexos. São bastante lentos e dispendiosos, além de exigirem um treinamento intensivo. Em geral, são utilizados para o desenvolvimento de sistemas que necessitam de grande robustez e confiabilidade diante da possibilidade de perda de vidas ou sério prejuízo, caso haja falhas.
ETAPAS | DESCRIÇÃO

ESPECIFICAÇÃO FORMAL PARA
DEFINIÇÃO DE REQUISITOS

REFINAMENTO PARA
CONCEPÇÃO DE PROJETO

SÍNTESE PARA
IMPLEMENTAÇÃO

PROTOTIPAÇÃOPARA

VALIDAÇÃO
PROVA PARA A VERIFICAÇÃO

Busca formalizar os requisitos descobertos utilizando algum método formal, criando uma modelagem com o uso de elementos.
Busca conceber o projeto de software, ou seja, nesta fase é pensado na arquitetura do sistema com seus diversos componentes e suas interfaces, dados e relacionamentos entre os mesmos.
Busca gerar esqueleto de código, a partirdo modelo refinado, que pode servircomo base para implementação real do sistema.
Busca elaborar um protótipo funcional do sistema para validar se o mesmo, atende as necessidades do cliente.
Busca verificar se o sistema desenvolvido foi concebido atendendo a todos os
Requisitos Funcionais e Não-Funcionais elicitados.

MODELO BASEADO EM COMPONENTES

O Modelo Baseado em Componentes tem utilizado o reúso como peça principal. Essa abordagem depende de uma grande base de componentes reusáveis e algum framework de integração.
ESPECIFICAÇÃO DE
REQUISITOS

ANÁLISE DE
COMPONENTES

ALTERAÇÃO DE
REQUISITOS

VALIDAÇÃO DE
SISTEMA

DESENVOLVIMENTO E
INTEGRAÇÃO

PROJETO DE SISTEMA
COMREÚSO

FASES 00 MODELO
BASEADO EM
COMPONENTES

ESPECIFICAÇÃO DE

REQUISITOS

DESCRIÇÃO

Tem o objetivo de traduzir as informações coletadas durante a atividade de análise em um documento que define um conjunto de requisitos de software. Devem ser incluídos dois tipos de requisitos nesse documento: os Requisitos de Usuário e Requisitos de Sistema.
ANÁLISE DE
COMPONENTES

MODIFICAÇÃO DE
REQUISITOS

Nesta fase, é feita uma busca pelos componentes para implementar essa especificação.
Geralmente, não existe uma correspondência exata entre o componente encontrado e o procurado. Muitas vezes, os componentes que podem ser usados fornecem apenas parte da funcionalidade necessária.
Os requisitos são analisados usando as informações sobre os componentes encontrados, que são modificados para refletir os componentes disponíveis. Quando as modificações são impossíveis, a atividade de análise de componentes pode ser novamente realizada para procurar alternativas.
PROJETO DE SISTEMA

COMREÚSO

DESENVOLVIMENTO E

INTEGRAÇÃO

VALIDAÇÃO DE

SISTEMA

O framework do sistema é projetado ou um framework existente é reutilizado. Os projetistas levam em consideração os componentes reusados. Pode ser necessário projetar algum software novo caso os componentes reusáveis não estejam disponíveis para aquisição para o sistema.
Software que não pode ser adquirido externamente é desenvolvido e os componentes e os sistemas COTS são integrados para criar os novos sistemas. A integração de sistema,neste modelo, pode ser parte do processo de desenvolvimento, em vez de ser uma atividade separada.
Processo de verificação de se um sistema atende às necessidades e expectativas do cliente.Professor, o que são Sistemas COTS? Esse é o acrônimo de Commercial Off-The-Shelf, que é um conjunto de soluções pré-fabricadas e disponíveis no mercado, podendo ser compradas ou licenciadas, i.e., uma grande biblioteca de componentes prontos.
MODELO ORIENTADO A ASPECTOS

A Programação Orientada a Aspectos é uma abordagem que permite a separação dessas propriedades ortogonais dos componentes funcionais de uma forma natural e concisa, utilizando-se de mecanismos de abstração e de composição para a produção de código executável.
PARA MAIS DICAS: WWW.INSTAGRAM.COM/PROFESSORDIEGOCARVALHO

QUESTõES CoMENTADAS - CESPE

í. (CESPE / BANRISUL - 2022) Uma descrição ideal de um componente de software reutilizável deve ser feita com base no modelo 3C, que significa composição, conteúdo e contexto.
Comentários:

De acordo com Roger Pressman: "Um componente de software reutilizável pode ser descrito de várias maneiras; porém, uma descrição ideal engloba aquilo que Tracz denominou modelo gC -conceito,
conteúdo e contexto-, uma descrição daquilo que 0 componente faz, como isso é obtido com conteúdo que pode ficar oculto para usuários eventuais e que precisa ser conhecido apenas por aqueles que pretendem modificar ou testar 0 componente e onde 0 componente reside em seu domínio de aplicabilidade".
Gabarito: Errado

2. (CESPE / MPC-SC - 2022) No processo de desenvolvimento de software, a prototipação pode ajudartanto na elicitação de requisitos do sistema quanto no estudo de soluções específicas do software de modo a apoiar o projeto de interface de usuário.
Comentários:

Perfeito! A prototipação é um processo útil para ajudar a desenvolver e obter feedback sobre o design de um software. No processo de elicitação de requisitos, a prototipação pode ajudar a identificar quais são as necessidades do usuário e quais funcionalidades precisam ser incluídas no sistema. Isso também ajuda a verificar se o projeto está abrangendo todas as necessidades do usuário. Além disso, a prototipação também pode ser usada para explorar diferentes soluções para o design da interface do usuário. Isso permite que os desenvolvedores experimentem diferentes soluções para ver qual é a melhor maneira de atender às necessidades do usuário.Logo, a questão está correta, mas foi anulada porque o conteúdo extrapolava o edital.
Gabarito: Anulado

3. (CESPE / MPC-SC - 2022) Usabilidade consiste em determinar, em uma solução de software,quão fácil é corrigir um problema após a sua detecção, uma vez que a engenharia de usabilidade refere-se à capacidade de diagnosticar o problema e modificar os componentes necessários para corrigi-lo.
Comentários:

A questão trata de Manutenibilidade e, não, da Usabilidade. Logo, a questão está errada, mas foi anulada porque o conteúdo extrapolava o edital.
Gabarito: Anulado

4. (CESPE / MPC-SC - 2022) No modelo espiral de Boehm, cada volta na espiral representa uma fase do processo de software: na parte mais interna, enfoca-se a viabilidade do sistema e, no ciclo seguinte, a definição de requisitos, assim por diante, executando-se, ao longo dos ciclos, a análise de riscos, prototipação e codificação.
Comentários:

Perfeito! O Modelo Espiral de Boehm foi desenvolvido para dar suporte a projetos de desenvolvimento de software que envolvam riscos importantes, incertezas e decisões que precisem ser tomadas. É uma evolução do modelo em cascata, pois torna possível o ajuste a mudanças durante o desenvolvimento de um projeto. Esse modelo é representado por uma espiral,no qual cada volta na espiral representa uma fase do processo de software. A partir da volta mais interna,enfoca-se a viabilidade do sistema, seguida pela definição de requisitos,
análise de riscos,
prototipação, planejamento e design do sistema, codificação, testes e implementação. Toda vez que o projeto é executado, o processo se repete. Logo, a questão está correta, mas foi anulada porque o conteúdo extrapolava o edital.
Gabarito: Anulado

5. (CESPE / DPE-RO - 2021) Um analista deve escolher uma metodologia de desenvolvimento para elaborar o planejamento do ciclo de vida de um produto de software de larga escala. Osistema é inédito e o reúso de código semelhante não deve ser considerado como base para o novo desenvolvimento. O analista deve considerar, ainda, a necessidade de reduzir os riscos em todas as fases do projeto, pois é provável que os requisitos sejam aprimorados e mudem ao longo do processo. Entre os riscos a serem mitigados, está o de não ter sido contratado pessoal de software suficiente para construir o produto, além de a equipe contratada não ter experiência suficiente no desenvolvimento de produtos em larga escala. Ainda, há o risco de o fornecedor do hardware necessário ao projeto não entregartodas as estações clientes no prazo do contrato.
Nessa situação hipotética, para a metodologia do processo de software em questão, é mais apropriado o uso do:
a) modelo codificar-e-corrigir.

b) modelo espiral.

c) modelo integração e configuração.

d) modelo em cascata.

e) modelo baseado em protótipos.

Comentários:

Observem que o analista busca reduzir o risco em todas as fases do projeto, logo podemos eliminar de cara o modelo em cascata, visto que ele atrasa a redução de riscos, fazendo-a somente nas fases finais. Também podemos eliminar o modelo corrigir-e-codificar (Code and Fix), pois nele é difícil avaliar a qualidade e os riscos do projeto. Esse é mal considerado uma metodologia,dado que ele envolve ir desenvolvendo e corrigindo erros por experimentação. O modelo integração e configuração é baseado em reúso, logo também deve ser eliminado. O modelo baseado em protótipos é utilizado quando o cliente não definiu detalhadamente os requisitos do software, logo não faz sentido aqui. Porfim, o modelo mais adequado para a redução dos riscos é o modelo espiral,que é orientado à redução de riscos.

Gabarito: Letra B

6. (CESPE / Polícia Federal - 2021) Embora não seja dirigido a riscos, o modelo de desenvolvimento de sistemas espiral de Boehm inclui, em seu framework, a etapa de análise e validação dos requisitos.
Comentários:

O Modelo em Espiral foi proposto originalmente, em 1988, por Boehm. Sua ideia era representar um processo de software orientado a riscos. Em vez de representar o processo como uma sequência de atividades com algum retorno entre uma atividade e outra, o processo é representado como uma espiral. Ele combina atividades de desenvolvimento com aspectos gerenciais(Planejamento,
Tomada de Decisão, Análise de Riscos, etc).

Gabarito: Errado

7. (CESPE / SERPRO - 2021) No modelo formal, as etapas do desenvolvimento do software incluem especificação formal para definição de requisitos, refinamento para concepção de projeto e prova para a verificação.
Comentários:

As etapas são especificação formal para definição de requisitos, refinamento para concepção de projeto, síntese para implementação, prototipagem para a validação e prova para a verificação.Logo, todas essas listadas no enunciado estão contempladas.

Gabarito: Correto

8. (CESPE / SLU-DF - 2019) No modelo de desenvolvimento de software em cascata, a abordagem é orientada ao risco e as tarefas são organizadas nos seguintes ciclos:determinar objetivos, identificar e resolver riscos, desenvolver e testar, e planejar a próxima iteração.
Comentários:

Opa... as fases e a característica de ser orientado a risco tratam do modelo em espiral e, não, do modelo em cascata.
Gabarito: Errado

9. (CESPE / MPC-PA- 2019) Os modelos espiral e RAD (Rapid Application
Development) são classificados, respectivamente, como modelos de processo de desenvolvimento de software dos tipos a) incremental e sequencial.
b) evolutivo e incremental.

c) evolutivo e sequencial.

d) incremental e evolutivo.

e) evolutivo e evolutivo.

Comentários:

Ambos são classificados como modelos de desenvolvimento de software do tipo evolutivo e incremental.
Gabarito: Letra B

10.(CESPE / TRT-CE - 2017) Os modelos de processo em que o sistema é dividido em pequenos subsistemas funcionais que, a cada ciclo, são acrescidos de novas funcionalidades são denominados:
a) evolutivos.

b) unificados.

c) sequenciais.

d) incrementais.

Comentários:

O modelo de processo que divide o sistema em subsistemas funcionais que, a cada ciclo, são acrescidas novas funcionalidades é o modelo incremental.
Gabarito: Letra D

11.(CESPE / MEC - 2014) No desenvolvimento de software de grande porte, não se usam,
em conjunto, os seguintes modelos de processo de software genéricos: modelo em cascata,desenvolvimento evolucionário e engenharia de software embasada em computador.

Comentários:

De acordo com Sommerville, os modelos genéricos de processos de software amplamente utilizados são o modelo em cascata, o modelo de desenvolvimento evolucionário e o modelo de desenvolvimento baseado em componentes. Estes, não são mutuamente exclusivos e comumente são utilizados em conjunto, especialmente para desenvolvimento de sistemas de grande porte.
Nós vimos em aula que o modelo evolucionário, por exemplo, não é recomendado para sistemas de grande porte. No entanto, a questão trata da utilização desses três modelos em conjunto - o que é possível! No entanto, não existe "engenharia de software embasada em computador"-o que existe é "engenharia de software baseada em componentes".
Gabarito: Errado i2.(CESPE / TRT-io - 2013) No modelo prototipação, a construção de software tem várias atividades que são executadas de forma sistemática e sequencial.
Comentários:

Na verdade, quem constrói software por meio de atividades executadas de forma sistemática e sequencial é o Modelo em Cascata; a prototipação é iterativa.
Gabarito: Errado

13. (CESPE / STF - 2013) O processo de software fundamentado no modelo em espiral apresenta o processo em loops compostos basicamente por setores, como, por exemplo,definição de objetivos, avaliação de riscos, planejamento e desenvolvimento e avaliação.
Comentários:

Perfeito! Os setores são: determinar objetivos, alternativas e restrições;
avaliar alternativas,
identificar e resolver riscos; desenvolver e testar; e planejar próximas fases.

Gabarito: Correto

14.(CESPE / ANT - 2013) O paradigma de programação orientada a aspectos traz soluções para alguns dos problemas existentes no paradigma orientado a objetos, como herança múltipla e sobrecarga de operadores.
Comentários:

Já outras questões importantes não são bem localizadas no projeto funcional.
Exemplos disto podem ser propriedades que envolvem várias unidades funcionais, tais como: sincronização,
restrições de tempo, concorrência, distribuição de objetos, persistência, etc.
Galera, vocês Já conseguiram chegar a uma definição de Programação Orientada a Aspectos? E se cair na discursiva?
Galera, não são esses os problemas resolvidos pela POA! Ela resolve problemas que envolvem várias unidades funcionais, ajudando a separar responsabilidades - não há qualquer relação com herança múltipla ou sobrecarga de operadores. Ademais, vejam a pegadinha: herança múltipla e sobrecarga de operadores é um problema do paradigma orientado a objetos? Não, galera -é um problema do Java! Lembrem-se que Java não é uma linguagem completamente orientada a objetos!
Gabarito: Errado i5.(CESPE / SERPRO - 2013) A POA, uma evolução da programação orientada a objetos, é implementada nas linguagens Java, C++, Smalltalk e Prolog.
Comentários:

Prolog? Galera, Prolog é uma linguagem lógica; POA não pode ser implementada nesta linguagem!

Gabarito: Errado

16. (CESPE / TRT17 - 2013) O modelo espiral de modelagem de processos para desenvolvimento de software é finalizado quando o software é implantado.
Comentários:

Galera, modelo espiral de modelagem de processos de desenvolvimento de software não existe!Ele é um modelo de desenvolvimento de software e, não, modelagem de processos.

Gabarito: Errado

17. (CESPE / MEC - 2011) O modelo de processo denominado em espiral combina as atividades de desenvolvimento com o gerenciamento de riscos, de modo a minimizá-los e controlá-los.
Comentários:

O modelo em espiral realmente combina atividades de desenvolvimento com gerenciamento de riscos com o intuito de minimizá-los e controlá-los.
Gabarito: Correto

18.(CESPE / AL-ES - 2011) No ciclo de vida em espiral, a de análise de risco é realizada na etapa da modelagem do produto.
Comentários:

Na verdade, é realizada na etapa de planejamento e, não, de modelagem. De acordo com oPressman, as etapas são: comunicação, planejamento, modelagem, construção e implantação ou emprego, sendo que a análise de riscos está presente na etapa de planejamento.
Gabarito: Errado

19.(CESPE / FUB - 2011) Os diversos modelos de processo de software disponíveis permitem a representação abstrata de um processo de software sob diferentes perspectivas.No modelo evolucionário, sob a perspectiva da arquitetura, a velocidade de desenvolvimento faz que a produção de documentos que reflitam cada versão do sistema seja economicamente inviável,gerando problemas na validação independente de sistemas.

Comentários:

Se os sistemas são desenvolvidos rapidamente, não é viável economicamente produzir documentos para cada versão do sistema.
Gabarito: Correto

20. (CESPE / MEC - 2011) No modelo de prototipação, o processo de desenvolvimento de software é modelado como uma sequência linear de fases, enfatizando um ciclo de desenvolvimento de breve duração.
Comentários:

Não é linear, é iterativo! A questão menciona uma sequência linear de fases, que lembra o Modelo em Cascata; e um ciclo de desenvolvimento de breve duração, que lembra oDesenvolvimento
Rápido de Aplicações (RAD).

Gabarito: Errado

21. (CESPE / TRE-MT - 2010) A metodologia de prototipagem evolutiva é uma abordagem que visualiza o desenvolvimento de concepções do sistema conforme o andamento do projeto,por meio de protótipos visuais.
Comentários:

A prototipagem evolutiva é uma abordagem que visualiza o desenvolvimento de concepções do sistema conforme o andamento do projeto até chegar ao resultado final. Esta metodologia baseia-se na utilização de prototipagem visual ou modelos do sistema final. Logo, pode-se afirmar que é apresentado ao usuário funcionalidades por meio de protótipos visuais conforme o andamento do projeto.
Gabarito: Correto

22.(CESPE / INMETRO - 2010) Um dos benefícios da prototipação é a documentação normalmente gerada, que facilita a manutenção dos sistemas a longo prazo e a elaboração de casos de teste.
Comentários:

Trata-se justamente do inverso! A documentação geralmente é prejudicada quando se utiliza a prototipação! Imaginem só: você precisa entregar algo rápido para o usuário verificar se satisfaz seus requisitos, não é viável fazer uma documentação formal.
Gabarito: Errado

23.(CESPE / INMETRO - 2010) Na abordagem evolutiva para desenvolvimento de software, um protótipo do software é produzido e utilizado para identificar possíveis problemas com os requisitos, sendo descartado logo em seguida, e o desenvolvimento do software propriamente dito é, então, iniciado.
Comentários:

Se o protótipo é descartado, então não se trata de uma abordagem evolutiva! Cuidado,
porque esses nomes confundem: existe modelo evolutivo e abordagem evolutiva - a PrototipaçãoThrow-
away não é uma abordagem evolutiva, mas é parte do Modelo Evolutivo.

Gabarito: Errado

2ZJ.(CESPE / SERPRO - 2010) O modelo em espiral de ciclo de vida de software é iterativo e incremental, uma vez que a mesma sequência de atividades relacionadas à produção de software é realizada a cada ciclo da espiral.
Comentários:

Na verdade, ele é iterativo e evolucionário!

Gabarito: Errado

25.(CESPE / SERPRO - 2010) O modelo de desenvolvimento em espiral permite repensar o planejamento diversas vezes durante o desenrolar do projeto.
Comentários:

Trata-se do modelo iterativo, portanto permite replanejamento a cada nova iteração.

Gabarito: Correto

26.(CESPE / INMETRO - 2010) No modelo em espiral, um exemplo de modelo iterativo,
cada loop da espiral representa uma fase do processo de software. Nesse modelo, os riscos não são considerados, pois podem impactar o projeto.
Comentários:

Na verdade, os riscos são considerados uma vez que podem impactar o projeto!

Gabarito: Errado

27.(CESPE / TRE-MT - 2010) O modelo de desenvolvimento em espiral, que tem a codificação como segunda etapa, gera o código do sistema muito mais rapidamente que o modelo de prototipação.
Comentários:

Na verdade, é a quarta etapa e não gera o código mais rapidamente que o modelo de prototipação,que é bem mais rápido.

Gabarito: Errado

28.(CESPE / TRE-BA - 2010) Na engenharia de software baseada em componentes, na qual se supõe que partes do sistema já existam, o processo de desenvolvimento concentra-se mais na integração dessas partes que no seu desenvolvimento a partir do início. Essa abordagem é baseada em reúso para o desenvolvimento de sistemas de software.
Comentários:

Ora, a Engenharia é especializada em produzir componentes reusáveis. Engenheiros raramente fabricam um componente a partir do nada. Eles baseiam seus projetos em componentes exaustivamente testados em outros sistemas. Quando se fala em Modelo baseado emComponentes, refere-se a uma estratégia de engenharia de software na qual o processo de desenvolvimento é voltado à reusabilidade. Percebam, portanto, que há uma concentração dos esforços mais na integração de partes existentes do que no seu desenvolvimento desde o início.
Gabarito: Correto

2g.(CESPE / UNIPAMPA - 2009) No modelo de desenvolvimento prototipagem, um protótipo é desenvolvido para ajudar no entendimento dos requisitos do sistema.
Comentários:

A Prototipagem é utilizada quando não se conhece bem os requisitos. É uma forma de entendê-los melhor para posteriormente desenvolver o software. Ela se configura como um processo iterativo,interativo e rápido de desenvolvimento e o protótipo serve como um mecanismo de identificação dos requisitos do software, que servirão para uma futura especificação. Finalmente, um protótipo é em geral desenvolvido para ajudar no entendimento dos requisitos do sistema.
Gabarito: Correto

3O.(CESPE /TCE-RN - 2009) A prototipação, uma abordagem para desenvolvimento de software na qual se cria um modelo do software que será implementado, é composta de quatro etapas:planejamento, análise de risco, engenharia e avaliação do cliente.

Comentários:

As etapas são Comunicação, Plano Rápido, Modelagem de Plano Rápido, Construção do
Protótipo,
e Implantação, Entrega e Feedback. As etapas mencionadas na questão são do Modelo em Espiral.

Gabarito: Errado

3i.(CESPE / DETRAN-DF - 2009) O modelo de processo de desenvolvimento de software evolucionário parte do desenvolvimento de uma implementação inicial cujos resultados são apresentados aos clientes e refinados por meio de várias versões até que se alcance o sistema adequado. A prototipação, como processo, tem por objetivo compreender as especificações do software para se chegar aos requisitos para o sistema.
Comentários:

A questão afirma que a prototipação tem por objetivo (1) compreender as especificações do software para (2) se chegar aos requisitos para o sistema. Na verdade, é justamente o contrário!Primeiro, eu levanto os requisitos do sistema e, depois, eu faço a especificação. Cabe ressaltar que a especificação é o detalhamento dos requisitos, logo ele não pode vir antes do levantamento dos requisitos.
Gabarito: Errado

32.(CESPE / UNIPAMPA - 2009 O modelo espiral admite retorno às fases anteriores de desenvolvimento, suportando ainda a execução paralela de fases.
Comentários:

Na verdade, ele não admite retorno às fases anteriores e, como é uma espiral, não permite a execução paralela de fases.
Gabarito: Errado

33.(CESPE / ANATEL - 2009) Entre os modelos de ciclo de vida de software, o modelo espiral possui maior proximidade com as práticas da engenharia clássica empregadas, por exemplo,na construção de casas, quando comparado aos modelos cascata e de componentes reusáveis.
Comentários:

Na verdade, o modelo em cascata tem uma maior proximidade com as práticas de engenharia clássica.
Gabarito: Errado

34.(CESPE / INMETRO-2009) Uma das características marcantes do modelo de desenvolvimento em espiral é o fato de ele ser cíclico, e não linear, como o modelo de desenvolvimento em cascata.
Comentários:

Planejamento estimativa de custos cronograma análise de riscos
Modelagem análise projeto
Perfeito! No entanto, cuidado para não escorregar no português: a questão parece ambígua, mas ela afirma que uma das características marcantes do modelo de desenvolvimento em espiral é o fato de o modelo espiral ser cíclico, diferente do modelo em cascata, que é linear.
Gabarito: Correto

35. (CESPE / UNIPAMPA - 2009) O modelo de desenvolvimento espiral foi desenvolvido somente para abranger as melhores características do ciclo de vida clássico.
Comentários:

Esse item não faz qualquer sentido! Ele não é uma implementação do Modelo em Cascata
- ele é um modelo híbrido que combina características do Modelo em Cascata com oModelo de
Prototipagem.

Gabarito: Errado

36.(CESPE / UNIPAMPA - 2009) No modelo de desenvolvimento em espiral, a análise de riscos não impacta na elaboração de um produto ou protótipo.
Comentários:

É claro que impacta -tanto que ela é considerada explicitamente.

Gabarito: Errado

37. (CESPE / TJDFT - 2008) A prototipação evolucionária não gera problemas de manutenção de sistema porque o desenvolvimento é rápido e não sofre grandes mudanças.
Comentários:

Na verdade, gera problemas, sim! Muitas mudanças tendem a corromper a estrutura do software e isso as tornam difíceis e caras. Observação: o ideal seria que a questão dissesse Modelo ouAbordagem Evolucionária e, não, Prototipação Evolucionária.

Gabarito: Errado

38. (CESPE/ MPE-AM-2008) No modelo de prototipação, a especificação de requisitostem pouca importância, pois o software é continuamente adaptado em função dos desejos do usuário
Comentários:

A prototipação serve não só para o levantamento de requisitos, mas também para sua especificação. Galera, como não tem importância? É exatamente para isso que ele serve!
Gabarito: Errado

39. (CESPE/TJDFT-2008) A prototipação de um software é uma técnica de desenvolvimento não-interativa porque o teste do sistema só ocorre na versão final.

Comentários:

A Prototipagem é utilizada quando não se conhece bem os requisitos. É uma forma de entendê-los melhor para posteriormente desenvolver o software. Ela se configura como um processo iterativo,interativo e rápido de desenvolvimento e o protótipo serve como um mecanismo de identificação dos requisitos do software, que servirão para uma futura especificação. Logo, ela é tanto iterativa(repete-se diversas vezes) quanto interativa (conta com a participação ativa dos usuários).

Gabarito: Errado

4o.(CESPE / TJDFT - 2008) Uma das finalidades da prototipação é reduzir o esforço de desenvolvimento de um software.
Comentários:

A prototipação realmente ajuda a reduzir o esforço! A prototipação (não importa qual tipo) ajuda a esclarecer requisitos. Caso eu não faça um protótipo, pode ocorrer de eu não compreender bem requisitos obscuros e, eventualmente, ter que refazer o desenvolvimento.
Gabarito: Correto

4i.(CESPE / TJDFT - 2008) A prototipação evolucionária permite que a versão inicial do protótipo seja desenvolvida e refinada em estágios sequenciados, até que se chegue à versão final do sistema.
Comentários:

Na prototipação evolucionária, a versão é desenvolvida em estágios sequenciados e, não, o processo de desenvolvimento. Esse é iterativo e, não, sequenciado. No entanto, as versões são sequenciais, no sentido de que as versões seguem uma ordem.
Gabarito: Correto

42.(CESPE /TJDFT- 2008) O modelo em espiral é um modelo de processos de software que reúne a natureza iterativa da prototipação com os aspectos sistemáticos e controlados do modelo sequencial linear.
Comentários:

O Modelo em Espiral étambém conhecido como prototipagem-em-etapas porcombinaro modelo em cascata com a prototipação.
Gabarito: Correto

43-(CESPE / TJDFT - 2008) Empregando o modelo de desenvolvimento em espiral, o software é desenvolvido em uma série de versões intermediárias incrementais.
Comentários:

O Pressman discorda! A questão fala que o software é desenvolvido em uma série de versões intermediárias incrementais. Ora, modelos iterativos geram uma série de versões intermediárias;modelos incrementais geram incrementos. Logo, pode-se assumir que a questão afirma que se trata de um modelo iterativo e incremental. Pressman discorda, mas não é incomum autores tratarem o modelo em espiral como iterativo e incremental.
Gabarito: Correto

44.(CESPE / SERPRO - 2008) O modelo iterativo e o modelo em espiral possuem características semelhantes: ambos permitem que as atividades do processo sejam planejadas e avaliadas ao longo do ciclo de vida.
Comentários:

Perfeito! O modelo em espiral possui uma fase para planejar próximas fases. Lembrando que oModelo Espiral é um tipo de Modelo Iterativo.

Gabarito: Correto

45.(CESPE / MPE-AM - 2008) A utilização de um modelo de desenvolvimento embasado em componentes é uma forma de desenvolvimento em espiral que busca a reutilização de trechos de software desenvolvidos e testados em projetos anteriores e armazenados em um repositório.
Comentários:

De fato, ambos os modelos possuem características em comum, mas é muito forte afirmar que o modelo baseado em componentes é uma forma de desenvolvimento em espiral. O modelo espiral preconiza a identificação de alternativas (reúso de componentes, comprar pronto). Logo,acredito que essa questão caberia recurso.
Gabarito: Correto

Zj6.(CESPE / SERPRO - 2008) Para a especificação de software e verificação de sistemas, uma alternativa que se fundamenta na matemática discreta e na lógica é o modelo incremental.
Comentários:

Na verdade, a alternativa mais adequada é a utilização de métodos formais.

Gabarito: Errado

47.(CESPE / TSE - 2007) Um possível objetivo da prototipação é criar rapidamente um sistema experimental que possa ser avaliado por usuários finais. Um protótipo aprovado pelos usuários pode vir a ser usado como ponto de partida para a construção do sistema.
Comentários:

Na maioria dos casos, o protótipo é inviável de ser utilizado por ser muito lento e/ou muito grande e/ou difícil de utilizar. Em geral, os protótipos são descartados assim que os objetivos de levantamento de requisitos são alcançados. No entanto, alguns preferem refiná-los iterativamente até evoluir ao sistema final requisitado pelo usuário. Logo, trata-se de uma alternativa, isto é, pode-se utilizá-lo como ponto de partida para construção do sistema em vez de descartá-lo!

Gabarito: Correto

48.(CESPE / TRE-AL - 2004) No modelo de prototipação, o desenvolvedor cria inicialmente um modelo de software que será posteriormente implementado.
Comentários:

A metodologia de Prototipagem Evolutiva (ou Evolucionária) é uma abordagem que visualiza o desenvolvimento de concepções do sistema conforme o andamento do projeto até chegar ao resultado final. Esta metodologia baseia-se na utilização de prototipagem visual ou modelos do sistema final. Estes modelos podem ser simples desenhos ou imagens do sistema.
Na maioria dos casos, o protótipo é inviável de ser utilizado, por ser muito lento e/ou muito grande e/ou difícil de utilizar. Em geral, os protótipos são descartados assim que os objetivos de levantamento de requisitos são alcançados. No entanto, alguns preferem refiná-los iterativamente até evoluir ao sistema final requisitado pelo usuário. Captaram?
Cria-se, inicialmente, um modelo do sistema final! Além disso, o protótipo pode ser implementado e se tornar esse sistema final. Galera, essa questão foi retirada literalmente doPressman (1995):
"Prototyping is a process that enables the construction of a model of the software which is to be built". Qual o problema dessa questão? Sua tradução!
Pressman afirma que a Prototipação é um processo que permite ao desenvolvedor a construção de um modelo do software que será construído. Em outras palavras, a prototipação é um modelo/esboço do software que posteriormente será construído. Pensem em um software qualquer! Antes de construir o software, faremos um modelo/esboço dele (não importando se iremos descartá-lo ou não). A questão não afirma em nenhum momento que o protótipo será evoluído ou descartado.
Gabarito: Correto

49. (CESPE / COHAB - 2004) O modelo espiral é um modelo de processo de software que combina a natureza iterativa da prototipagem com os aspectos controlados e sistemáticos do modelo sequencial linear.
Comentários:

O Modelo em Espiral étambém conhecido como prototipagem-em-etapas porcombinaro modelo em cascata com a prototipação. Galera, eu não errei! Essa questão é quase idêntica à anterior: é oCESPE copiando do CESPE!

Gabarito: Correto

50. (CESPE / PBV-RR - 2004) O modelo em cascata é linear e sequencial. Modelos como o espiral e o Rational Unified Process pregam o desenvolvimento iterativo.
Comentários:

Ele realmente é linear e sequencial. Além disso, o modelo em espiral e o RUP são ambos iterativos.

Gabarito: Correto

51. (CESPE / BASA-2004) O modelo em espiral evolui à medida que o processo avança,
permitindo ao desenvolvedor e ao cliente entenderem melhor os riscos e reagirem em cada nível evolucionário.
Comentários:

De fato, ele evolui à medida que o processo avança, permitindo ao desenvolvedor e ao cliente entender melhor os riscos e como reagir a eles.
Gabarito: Correto

52. (CESPE / PBV-RR - 2004) O modelo em espiral para desenvolvimento de software é fundamentado no faseamento comumente adotado em projetos de engenharia a partir da década de 70 do século passado. Tal modelo considera as seguintes fases: análise de requisitos,definição, projeto, implementação, integração e testes, operação e manutenção.

Comentários:

As atividades (chamadas de fases na questão) são: Comunicação, Planejamento,
Modelagem,
Construção e Implantação. As fases mencionadas são do Modelo em Cascata.

Gabarito: Errado

53.(CESPE / PBV-RR - 2004) O modelo em espiral de desenvolvimento proposto por Boehm apresenta a análise de riscos como uma das suas fases essenciais.
Comentários:

Na verdade, a análise de riscos não é umafase-é uma atividade. No entanto, a banca não entendeu dessa maneira :(
Gabarito: Correto

54-(CESPE / STJ -2004) O modelo de desenvolvimento em espiral requer a consideração dos riscos técnicos em todos os estágios ou interações do projeto, o que permite reduzir os riscos antes que se concretizem.
Comentários:

Perfeito! Deve-se considerar os riscos técnicos em todos os estágios para reduzi-los antes que se concretizem.
Gabarito: Correto

55.(CESPE/TRE-AL-2OO4) O modelo de desenvolvimento em espiral engloba o que há de melhor no modelo cascata e no modelo de prototipação, acrescentando a análise de risco,inexistente nestes dois modelos.
Comentários:

Existe - sim - análise de riscos no modelo em espiral. No entanto, isso não significa que ela seja inexistente no Modelo em Cascata e no Modelo de Prototipação, ela apenas não é explícita como no Modelo em Espiral.
Gabarito: Errado

56. (CESPE / SERPRO - 2004) Enquanto o reúso em engenharia de software convencional está geralmente limitado à extensão e à manutenção de um sistema específico, o reúso, em engenharia de software por componentes, é um requisito de desenvolvimento,independentemente do projeto em consideração.

Comentários:

O que a questão quis dizer é que você pode utilizar o reúso na engenharia de software tradicional em um caso aqui outro ali. No entanto, na Engenharia de Software Baseada emComponentes a reusabilidade não é um bônus, ela é a base, o alicerce, a fundação de toda a sua teoria. Então,trata-
se de um requisito de desenvolvimento - no sentido de que já no desenvolvimento, você tem que pensar em como será sua arquitetura baseada em componentes reusáveis. Não existe ESBCsem a reusabilidade de seus componentes e, por isso, ela independe do projeto em consideração. Então,você está correto: se o projeto for muito específico, talvez não seja o caso de se utilizar o CBSE.

Gabarito: Correto

57.(CESPE / SERPRO - 2004) O uso de componentes pode estar condicionado a regras de licenciamento. Essa preocupação, no entanto, não existe se os componentes forem classificados como software livre.
Comentários:

Há regras de licenciamento, sim. Não confundam componentes livres com componentes gratuitos.Não é porque um software é classificado como software livre que ele é grátis ou não possui regras de licenciamento.
Gabarito: Errado

QUESTõES CoMENTADAS - FCC

í. (FCC / TRF - 3a REGIÃO - 2019) No modelo em espiral de processo de software
(Boehm), antes de cada atividade de prototipação, é sempre realizada uma atividade de:
a) plano de desenvolvimento.

b) validação de requisitos.

c) teste de aceitação.

d) análise de riscos.

e) plano de ciclo de vida.

Comentários:

©yEEE.1988).

Antes de cada atividade de prototipação, é realizada a análise de riscos.

Gabarito: Letra D

2. (FCC / TRF - 3a REGIÃO - 2019) Considere o modelo de ciclo de vida de software constituído por rotinas de trabalho com a participação de todos os membros da equipe, onde falhas não são toleráveis e por isso, entre as atividades, duas têm grande importância no processo:uma delas dedicada ao planejamento da etapa e outra à de análise de riscos. As atividades são apoiadas pela geração de protótipos. Suporta o desenvolvimento de sistemas complexos e de grande porte. Trata-se do modelo:
a) Interativo e Incremental.

b) RAD - Rapid Application Development.

c) Espiral.

d) Cascata.

e) Evolutivo.

Comentários:

Todas as características apresentadas no enunciado nos remetem ao modelo espiral - com ênfase na análise de riscos.
Gabarito: Letra C

3. (FCC /TRT16 -2014) Os modelos de processo são uma representação abstrata de um processo de software, que podem ser usados para explicar diferentes abordagens para o desenvolvimento de sistemas. Analise as seguintes abordagens:
Desenvolvimento I: intercala as atividades de especificação, desenvolvimento e validação.
Um sistema inicial é desenvolvido rapidamente baseado em especificações abstratas e depois é refinado com as entradas do cliente para produzir um produto que o satisfaça.
Modelo II: considera as atividades fundamentais do processo, compreendendo especificação,desenvolvimento, validação e evolução e as representa como fases de processo separadas,
tais como especificação de requisitos, projeto de software, implementação, teste etc.
III: baseia-se na existência de um número significativo de partes reusáveis.
O processo de desenvolvimento do sistema enfoca a integração destas partes, ao invés de desenvolvê-las a partir do zero.
Os modelos de processo genéricos descritos em I, II e III são, correta e respectivamente,associados a:

a) em Espiral - Baseado em Componentes - RAD

b) Evolucionário - em Cascata - Baseado em Componentes c) Baseado em Componentes - Sequencial - Refactoring d) Ágil - Sequencial - Unified Process e) em Cascata - Ágil - Refactoring
Comentários:

Intercala atividades de especificação, desenvolvimento e validação só pode ser o
Desenvolvimento
Evolucionário. Apenas com isso, nós já podemos matar a questão. De todo modo, o
Modelo II trata do modelo em cascata e o Modelo III trata do modelo baseado em componentes.
Gabarito: Letra B

4. (FCC / DPE-SP - 2013) No desenvolvimento de software, podem ser utilizados os chamados modelos evolucionários, cujo objetivo é lidar com produtos que possam evoluir ao longo do tempo. Assinale a alternativa que contém APENAS modelos evolucionários de desenvolvimento de software.
a) UML e de qualidade.

b) Componentes e arquétipo.

c) Prototipagem e espiral.

d) Redes de Petri e certificação.

e) Semântico e validação.

Comentários:

A alternativa que contém apenas modelos evolucionários de desenvolvimento de software é a prototipagem e espiral.
Gabarito: Letra C

5. (FCC/TST-2012) O Ciclo de Vida de um Sistema especifica todas as fases de desenvolvimento,desde sua concepção até o processo de manutenção e declínio. No que diz respeito ao desenvolvimento de software, existem alguns processos conhecidos. Um destes processos,possui característica iterativa e incremental, inicia cada fase do projeto realizando um planejamento prévio, realiza a execução da fase, verifica o progresso e os resultados da fase(riscos, lições aprendidas) e incrementa novos objetivos para a fase seguinte, seguindo para a próxima iteração. O processo de software em questão é o:
a) Modelo espiral.

b) Ciclo de vida em cascata.

c) Modelo de desenvolvimento evolucionário (prototipação).

d) Modelo de desenvolvimento ágil.

e) Método de desenvolvimento Cleanroom (Sala Limpa).

Comentários:

Conforme vimos no esquema, ele citou todos os setores do Modelo Espiral (os nomes estão um pouco diferentes, mas é apenas uma variação). Essa questão tem um detalhe: ela afirma que o modelo espiral é iterativo e incremental, mas já vimos que o Pressman afirma que ele é iterativo e evolucionário, mas não incremental.
Gabarito: Letra A

6. (FCC / TRE-CE - 2012) No desenvolvimento de software em espiral (Boehm), cada loop está dividido em quatro setores. NÃO se trata da denominação de um destes setores:
a) levantamento.

b) definição de objetivos.

c) avaliação e redução de riscos d) desenvolvimento e validação.
e) planejamento.

Comentários:

Os setores são: determinar objetivos, alternativas e restrições; avaliar alternativas, identificar e resolver riscos; desenvolver e testar; e planejar próximas fases. Logo, levantamento não é um dos setores.
Gabarito: Letra A

7. (FCC / TRT20 - 2010) À medida que se avança pelo modelo ocorre uma iteração e o software evolui para estágios superiores, normalmente com aumento da complexidade. Cada iteração está provida das atividades determinadas pelos quadrantes planejamento,avaliação de alternativas e riscos, desenvolvimento do software e avaliação do cliente. No ciclo de vida de desenvolvimento de software, trata-se da propriedade do modelo:
a) Cascata.

b) Incremental.

c) Espiral.

d) Prototipação.

e) Balbúrdia.

Comentários:

A questão fala de iteração, logo não pode ser Modelo em Cascata! Por outro lado, a questão fala em avaliação de alternativas e riscos, enfatizada (em verde em nosso esquema). Logo, trata-se claramente do Modelo em Espiral. Percebam que a questão faz uma confusão com os setores de cada autor, mas está correta.
Gabarito: Letra C

8. (FCC / MPE-RN - 2010) O modelo em espiral difere principalmente dos outros modelos de processo de software por:
a) não contemplar o protótipo.

b) reconhecer explicitamente o risco.

c) não ter fases.

d) possuir uma fase única evolucionária.

e) não contemplar o projeto do produto.

Comentários:

A principal característica do modelo em espiral é reconhecer explicitamente os riscos.

Gabarito: Letra B

9. (FCC / BAHIAGÁS - 2010) No modelo em espiral do processo de software cada loop na espiral representa:
a) uma disciplina de requisitos.

b) um enfoque de banco de dados.

c) uma tomada de decisão.

d) uma fase do processo.

e) um ciclo de programa.

Comentários:

Cada loop representa uma fase do processo de software. Dessa forma, o loop mais interno pode estar relacionado à viabilidade do sistema; o próximo loop, à definição de requisitos;o próximo, ao projeto de sistema e assim por diante.
Gabarito: Letra D

QUESTõES CoMENTADAS - FCV

í. (FGV / IBGE-2016) Aempresa SONOVATOS desenvolve sistemas há pouco tempo no mercado e, como padrão, sempre utilizou o modelo Cascata de ciclo de vida. Alguns clientes ficaram insatisfeitos com os produtos desenvolvidos pela empresa por não estarem de acordo com suas necessidades. Atualmente a SONOVATOS está desenvolvendo sistemas muito maiores,com duração de vários anos, e com requisitos ainda instáveis. O próprio processo de desenvolvimento da empresa também está em reformulação. Assim, a adoção de um novo modelo de ciclo de vida está sendo avaliada pelos gerentes da empresa. A intenção daSONOVATOS é, principalmente, gerenciar riscos e poder reavaliar constantemente o processo de desenvolvimento ao longo do projeto, o que permitiria correções nesse processo ou até mudança do tipo de processo. O modelo mais adequado para os sistemas atuais de longa duração da SONOVATOS é:
a) Rapid Application Development (RAD);

b) Espiral;

c) Extremme Programming;

d) Prototipação;

e) Modelo V.

Comentários:

A questão menciona algumas palavras-chave: requisitos instáveis, gerenciamento dos riscos,reavaliação constante, correções/mudanças do processo. Dito isso, vamos analisar: (a)
Errado, esse modelo não trata de gerenciamento de riscos e é mais voltado para projetos com entregas rápidas;
(b) Correto, esse modelo traz explicitamente uma preocupação com o gerenciamento de riscos,além de permitir uma reavaliação/correção/adaptação/mudança constantemente; (c)
Errado, esse modelo não trata explicitamente do gerenciamento de riscos - apesar de concordar que caberia recurso aqui; (d) Errado, esse modelo também não trata explicitamente de riscos; (e)Errado, esse modelo é uma variação do modelo em cascata.
Como a questão afirma que a intenção principal da empresa é gerenciar riscos, o modelo que explicitamente coloca um foco no gerenciamento de riscos é o modelo em espiral.
Gabarito: Letra B

2. (FGV / TCM-SP - 2015) Software, assim como todos os sistemas complexos, evolui ao longo do tempo. Modelos de processos evolucionários reconhecem a natureza iterativa e incremental da maioria dos projetos de engenharia de software e são projetados para adequar mudanças.Os modelos a serem utilizados em um processo evolucionário são:
a) cascata e modelo V;

b) prototipação e modelo espiral;

c) concorrente e métodos formais;

d) incremental e baseado em componentes;

e) processo unificado e orientado a aspectos.

Comentários:

Os modelos a serem utilizados em um processo evolucionário são: prototipação e espiral.

Gabarito: Letra B

3. (FGV / Fiocruz - 2010) Como modelo evolucionário do processo de software, uma característica da prototipagem é:
a) independer do estabelecimento e da definição de requisitos.

b) configurar um processo interativo e rápido de desenvolvimento.

c) iniciar o processo de desenvolvimento pela implantação e pelos testes.

d) gerar uma primeira versão do sistema completa e isenta de erros.

e) descartar a participação do cliente no processo de desenvolvimento e de implantação.

Comentários:

(a) Errado, claro que depende da definição de requisitos; (b) Correto, é um processo interativo,iterativo e rápido de desenvolvimento; (c) Errado. Você vai implantar e testar o que?
Você primeiro tem que levantar, especificar e desenvolver; (d) Errado, se é uma primeira versão, não é completa.Além disso, não há sistemas sem erros; (e) Errado, você deve incentivara participação do cliente.

Gabarito: Letra B

4. (FGV / BADESC - 2010) O Modelo Espiral, segundo Pressman (1995), incorpora as melhores características do Ciclo de Vida Clássico e da Prototipação e acrescenta o seguinte elemento:
a) análise dos riscos.

b) análise de projetos.

c) avaliação de usuários.

d) refinamento de requisitos.

e) refinamento de protótipos.

Comentários:

O Modelo Espiral foi o primeiro modelo a tratar explicitamente de análise de riscos.

Gabarito: Letra A

5- (FGV / Senado Federal - 2008) Considere as seguintes assertivas sobre modelos de processos de software:
I. No modelo em cascata, a fase seguinte não deve iniciar antes que a fase precedente tenha sido concluída.
II. No modelo evolucionário, a mudança constante tende a corromper a estrutura do software

III. A explícita consideração dos riscos no modelo em espiral distingue esse modelo dos modelos em cascata e evolucionário.
As assertivas corretas são:

a) somente I.

b) somente I e II.

c) somente I e III.

d) somente II e III.

e) I, lie III.

Comentários:

(I) Correto, uma fase só se inicia após o término e aprovação da fase anterior; (II)
Correto, muitas mudanças tendem a corromper a estrutura do software e isso as tornam difíceis e caras; (III)Correto, a ideia do modelo espiral é representar um processo de software orientado a riscos, o que o diferencia dos demais modelos.
Gabarito: Letra E

QUESTõES CoMENTADAS - DIVERSAS

í. (VUNESP / TJM-SP- 2021) Algumas atividades que fazem parte do modelo espiral de desenvolvimento de software são:
Construção - Implantação - Comunicação -
Planejamento - Modelagem

A ordem correta com que tais atividades são executadas, considerando o modelo espiral, é:

a) Comunicação, Planejamento, Modelagem, Construção e Implantação.

b) Construção, Implantação, Comunicação, Modelagem e Planejamento.

c) Modelagem, Planejamento, Construção, Implantação e Comunicação.

d) Planejamento, Construção, Implantação, Comunicação e Modelagem.

e) Planejamento, Modelagem, Comunicação, Construção e Implantação.

Comentários:

Planejamento estimativa de custos cronograma análise de riscos
Modelagem análise projeto
As atividades do modelo espiral são: Comunicação, Planejamento, Modelagem,
Construção e
Implantação (ou Emprego).

Gabarito: Letra A

2. (VUNESP / CETESB - 2009) Considere um sistema cujos requisitos de interface são definidos apenas quando o cliente realiza um test-drive na aplicação e aprova essa interface.Assinale a alternativa que apresenta o modelo mais adequado para o desenvolvimento da interface desse sistema.
a) Ágil.

b) Cascata.

c) Iterativo incremental.

d) Prototipação.

e) Rapid Application Development.

Comentários:

A afirmativa diz que o sistema possui requisitos de interface que são definidos apenas quando o cliente realiza um test-drive, i.e., um teste inicial na aplicação e aprova essa interface. Em outras palavras, o cliente valida ou não esses requisitos a partirde uma primeira utilização do sistema. Que metodologia de desenvolvimento de software pode ser utilizada para levantar e validar/aprovar requisitos? Trata-se da Prototipação!
Gabarito: Letra D

3. (CESGRANRIO / PETROBRAS - 2018) O chefe dos desenvolvedores de sistemas de uma empresa acompanhou o seguinte diálogo entre um de seus subordinados, um usuário e o diretor de operações.
Diretor - Acho que já poderíamos começar o desenvolvimento daquele sistema que o departamento de esportes pediu.
Usuário- Não é cedo demais? Ainda não temos todas as funcionalidades bem definidas.

Desenvolvedor - É verdade, mas acho que já é possível especificar e implementar algumas funcionalidades mais importantes e construir uma primeira versão até o final do mês.Depois acrescentaríamos outras funcionalidades à medida que as fôssemos construindo,gerando, a partir da experiência do uso, versões sucessivas e cada vez mais completas.
Diretor-Acho isso ótimo, assim já teremos uma noção do impacto que o sistema poderá causar no desempenho dos atletas. Comecemos logo, não temos um efetivo tão grande em TI.
Usuário - OK, vamos em frente, mas não contem nada para aquele especialista em risco.
Já temos muito trabalho pela frente. Nossa estrutura ainda não suporta esse tipo de cuidado; se entrarmos nessa, o projeto vai atrasar. E mantenham o contato e o foco no objetivo:um produto simples, mas de qualidade.
A partir desse episódio e refletindo sobre o que ouvira, o chefe dos desenvolvedores deverá optar pelo modelo de processo de software:
a) RAD

b) incremental c) cascata d) espiral e) baseado em componentes
Comentários:

(a) Errado. No RAD, não há versões intermediárias, visto que se trata de um processo de desenvolvimento extremamente rápido; (b) Correto. O modelo incremental é realmente indicado quando não há funcionalidades bem definidas, logo se inicia pelas mais importantes e são lançadas versões sucessivas e cada vez mais completas posteriormente; (c) Errado. Se ainda não há funcionalidades bem definidas, não se deve utilizaro modelo em cascata; (d) Errado. Omodelo em espiral é dirigido a riscos e a conversa deixa claro que não se deve contarcom o especialista em risco
-como o risco não é considerado, não é recomendável utilizar o modelo em espiral; (e)
Errado. Não há nada que leve a crer que se trata do modelo baseado em componentes.
Gabarito: Letra B

4. (CESGRANRIO / PETROBRÁS - 2014) Um técnico de informática, com o objetivo de agilizar o desenvolvimento de um software, escolheu o desenvolvimento evolucionário, uma abordagem da área de Engenharia de Software, que:
a) facilita a produção de sistemas bem estruturados, privilegiando um processo de mudanças contínuas, cada vez mais fáceis e baratas.
b) se baseia na existência de um número significativo de componentes reusáveis, num processo de desenvolvimento que enfoca a integração desses componentes, em vez de desenvolvê-los a partir do zero c) considera como atividades fundamentais do processo a especificação, o desenvolvimento,a validação e a evolução, representado-as como fases de processo separadas, sendo que para uma fase ser iniciada, a outra deve estar completamente terminada.
d) é mutuamente exclusiva com o modelo em cascata e de Engenharia de Software baseada em componentes, sendo que os subsistemas contidos em um sistema maior precisam ser desenvolvidos, usando a mesma abordagem ou modelo.
e) intercala as atividades de especificação, desenvolvimento e validação,
permitindo que um sistema inicial seja desenvolvido rapidamente, baseado em especificações abstratas.
Comentários:

Ele realmente intercala atividades de especificação, desenvolvimento e validação,
permitindo que um sistema inicial seja desenvolvido de maneira muito rápida baseado em especificações abstratas.
Gabarito: Letra E

5. (COSEAC / UFF - 2019) Nos projetos, quando o time quebra o produto em vários pedaços menores, trabalhando e entregando uma parte de cada vez, sem se preocupar com agilidade, e somente quando esta parte estiver pronta o time parte para outro pedaço, iniciando uma nova fase, constata-se um ciclo de vida:
a) preditivo.

b) iterativo e incremental.

c) adaptativo.

d) RUP.

e) cascata.

Comentários:

Quebra 0 produto em vários pedaços menores? Entrega uma parte de cada vez?
São todas características do modelo iterativo e incremental. Somente quando essa parte estiver pronta 0 time parte para outro pedaço? Sim, a equipe que está trabalhando no subsistema funcional somente partirá para o outro subsistema funcional quando terminá-lo.
Gabarito: Letra B

6. (IF-PA/IF-PA-2019) Tem-se como boas práticas em projetos de software a definição dos seus requisitos funcionais e suas funcionalidades. No decorrer dessa definição, pode surgir a necessidade de fornecer, de forma prioritária, um conjunto de funcionalidades iniciais básicas e,após esse fornecimento, podemos melhorar e expandir as funcionalidades em versões de software posteriores, até atingir todos os requisitos definidos. Nesse caso, estamos aplicando um modelo de processo de software denominado:
a) Métodos Formais.

b) Business Process Management (BPM).

c) Capability Maturity Model Integration (CMMI)

d) Incremental.

e) Entidade e Relacionamento.

Comentários:

"Fornecer, de forma prioritária, um conjunto de funcionalidades iniciais básicas e, após esse fornecimento, podemos melhorar e expandir as funcionalidades em versões de software posteriores,até atingir todos os requisitos definidos"-todas são características do modelo incremental.

Gabarito: Letra D

7- (FADESP / IF-PA - 2019) O princípio fundamental é que, a cada ciclo, uma versão operacional do sistema será produzida e entregue para uso ou avaliação detalhada do cliente. Os requisitos têm de ser levantados e é preciso constatar que o sistema é modular. Esse é o modelo:
a) Incremental.

b) Espiral.

c) Cascata.

d) RAD.

e) XP.

Comentários:

Uma versão operacional a cada ciclo para avaliação do cliente em um sistema modular é uma característica do modelo incremental.
Gabarito: Letra A

8. (CETREDE / Prefeitura de São Gonçalo do Amarante - CE - 2019) Sobre Engenharia deSoftware, marque a opção INCORRETA.

a) O modelo Cascata tem como característica intercalar as atividades de especificação,desenvolvimento e validação. Esta abordagem, permite a entrega de um produto ao fim de um longo ciclo de desenvolvimento e com baixa perspectiva de falha funcional.
b) A engenharia de software baseada em componentes baseia-se na existência de um número significativo de componentes reusáveis, enfocando o desenvolvimento na integração destes componentes.
c) No desenvolvimento exploratório, o objetivo do processo é trabalhar com o cliente para explorar os requisitos e entregar o sistema final.
d) No processo de engenharia de requisitos, a etapa de elicitação e análise dos requisitos é responsável pela derivação de requisitos através da observação de sistemas existentes,discussões com usuários potenciais, análise de tarefas etc.

e) Especificação, projeto e implementação, validação e evolução do software são etapas comuns em qualquer processo de software.
Comentários:

Todos os itens estão corretos, exceto o primeiro. A questão trata do modelo evolucionário ou incremental (depende da versão do livro) e, não, do modelo em cascata.
Gabarito: Letra A

9. (COSEAC / UFF - 2019) Dos modelos de desenvolvimento de software, aquele que prioriza a análise dos riscos envolvidos no desenvolvimento de cada parte do software é o modelo:
a) em cascata.

b) de prototipação.

c) incremental.

d) espiral.

e) baseado em componentes.

Comentários:

O modelo que prioriza a análise de riscos envolvidos no desenvolvimento é o modelo em espiral.

Gabarito: Letra D

10. (INSTITUTO AOCP / UFFS - 2019) Assinale a alternativa que apresenta uma característica do modelo espiral para engenharia de software.
a) Na etapa "engenharia", são identificadas as alternativas e as restrições.

b) Contempla a análise de riscos, além das melhores características do ciclo de vida clássico e prototipação.
c) O modelo espiral veio para substituir o modelo cascata, que caiu em desuso por sua alta complexidade.
d) Esse modelo contempla as seguintes atividades: engenharia de sistemas, análise,
projeto,
codificação, teste e manutenção.

e) Esse modelo define que, na etapa de desenvolvimento, deve ser adotada uma metodologia ágil de desenvolvimento.
Comentários:

(a) Errado, essa é a etapa de planejamento; (b) Correto, tanto que é conhecido como uma prototipação em etapas; (c) Errado, ele não veio para substituir o modelo em cascata e o modelo em cascata não é altamente complexo; (d) Errado, as atividades são: planejamento,análise de riscos, engenharia, construção e liberação, avaliação do cliente e comunicação com cliente; (e)Errado, não existe essa definição.

Gabarito: Letra B

11. (COVEST-COPSET / UFPE - 2019) A respeito de modelos de processo de software,
assinale a alternativa correta:
a) O modelo em cascata é inconsistente com outros modelos de processos de engenharia,
tendo documentação produzida em cada fase do ciclo. Dessa forma, o processo torna-se pouco visível,dificultando o monitoramento do progresso pelos gerentes, de acordo com o plano de desenvolvimento.
b) No modelo espiral de Boehm, o processo de software é representado como uma espiral em que cada volta representa uma fase do processo de software. O modelo não se tornou popular devido a problemas ligados ao gerenciamento de riscos de projeto.
c) Existem alguns tipos de sistema para os quais o desenvolvimento e a entrega incrementais não são a melhor abordagem. Por exemplo, alguns sistemas críticos, em que todos os requisitos devem ser analisados na busca por iterações capazes de comprometer a proteção ou a segurança do sistema.
d) Um modelo de processo para desenvolvimento de protótipos em que os objetivos da prototipação são descobertos ao final de cada iteração, depois que os usuários experimentarem os diversos protótipos produzidos ao longo do processo. Isso torna a abordagem pouco previsível e mais incerta.
e) Na entrega incremental, os clientes podem usar os incrementos iniciais como protótipos e visualizar o avanço gradativo no desenvolvimento, mas necessitam reaprender o uso do sistema quando sua versão final estiver disponível.
Comentários:

(a) Errado, é um modelo consistente com outros modelos e o processo é visível,
facilitando o monitoramento do progresso; (b) Errado, ele se tornou popularjustamente por ser voltado a riscos;
(c) Correto; (d) Errado, são descobertos no início do processo - além disso, isso torna a abordagem mais previsível e certeira; (e) Errado, não é necessário reaprendê-lo visto que o sistema vai sendo incrementado aos poucos, logo - ao final - estará da maneira especificada pelo usuário.
Gabarito: Letra C

i2.(IBFC/ Prefeitura de Cuiabá - MT - 2019) Heitor é gerente de projeto e precisa decidir qual modelo utilizará no processo de desenvolvimento do próximo software da empresaBrasil.
Quanto a alguns dos modelos do ciclo de vida de desenvolvimento de software, assinale a alternativa incorreta.
a) Modelo Espiral: produto final é entregue rapidamente b) Modelo Incremental: produzem o sistema de forma incremental até a sua versão final c) Metodologias Ágeis: dura de i(uma) a ^(quatro) semanas e ao final de cada iteração deve haver entrega ao cliente d) Modelo em Cascata: componente do sistema é entregue por fases, podendo acontecer paralelamente
Comentários:

(a) Correto, é a principal característica do RAD, mas o modelo espiral também tem esse potencial;

(b) Correto; (c) Correto, apesar de se referir especificamente ao Scrum; (d) Errado,
tudo é entregue ao final e as fases não podem ocorrer paralelamente.
Gabarito: Letra D
i3.(COSEAC / UFF - 2019) Em relação aos modelos de processos de software, avalie se são verdadeiras (V) ou falsas (F) as afirmativas a seguir:
I. O modelo de desenvolvimento orientado a reúso tem a vantagem da redução de riscos e de custos.
II. O modelo de desenvolvimento incremental possui a vantagem da facilidade de mapear os requisitos dos clientes dentro de incrementos de tamanho correto.
III. O modelo em cascata deve ser utilizado somente quando os requisitos forem bem compreendidos.
As afirmativas I, II e III são, respectivamente:

a) V, F e V.

b) F, V e V.

c) V, F e F.

d) F, F e V.

e) V, V e V.

Comentários:

(I) Correto, o modelo de desenvolvimento orientado a reúso realmente tem a vantagem da redução de riscos e de custos; (II) Errado, apesar disso eu não consigo identificar o erro da questão, mas esse foi o gabarito definitivo; (III) Correto, ele é adequado justamente quando os requisitos forem bem compreendidos.
Gabarito: Letra A

14.OADES / CFM -2018) O Modelo Espiral (Spiral) foi originalmente proposto por Boehm
(1986) e é fortemente orientado à redução de riscos.
WAZLAWICK, R. S. Engenharia de Software: Conceitos e práticas. São Paulo: Elsevier, 2013.

Considerando o exposto e o Modelo Espiral de ciclo de vida de software, assinale a alternativa correta:
a) O Modelo Espiral realiza uma etapa de cada vez, partindo para a próxima etapa apenas após a anterior estartotalmente validada.
b) Tal modelo de ciclo de vida tem foco apenas na resolução de riscos de requisitos mal compreendidos, fornecendo tempo suficiente para que estes possam ser entendidos e implementados.
c) O projeto é dividido em subprojetos, cada qual abordando um ou mais elementos de alto risco, até que todos os riscos identificados tenham sido tratados.
d) Cada iteração é iniciada sem planejamento prévio, resolvendo-se os problemas no momento em que surgem.
e) O início do ciclo de vida do projeto se parece mais com o Modelo Cascata.

Comentários:

(a) Errado, esse item trata do modelo em cascata; (b) Errado, não se trata apenas de riscos de requisitos mal compreendidos, mas diversos outros tipos de riscos como riscos de desempenho,arquitetural, entre outros; (c) Correto, o projeto é realmente dividido em subprojetos abordando um ou mais elementos de alto risco até que todos os riscos sejam identificados; (d)Errado, o planejamento é realizado com base nos riscos identificados, e, em cada nova interação,é definida uma abordagem; (e) Errado, ele divide o projeto em partes, no início com protótipos,identifica os principais riscos, e, em cada ciclo, os riscos são mitigados.
Gabarito: Letra C

15. (FADESP / IF-PA - 2018) Usando o modelo, o sistema é desenvolvido em ciclos,sendo que os primeiros ciclos podem não conter todas as atividades. O produto resultante de um primeiro ciclo pode ser uma especificação do produto ou um estudo de viabilidade.Os ciclos subsequentes podem ser protótipos, chegando progressivamente a versões operacionais do software, até se obter o produto completo. Modelos podem ser úteis para ajudar a levantar e validar requisitos, mas pode ocorrer de os clientes e usuários só terem uma verdadeira dimensão do que está sendo construído se forem colocados diante do sistema. Nestes casos, o uso da éfundamental.
As expressões que completam corretamente os espaços em branco, respectivamente, são:

a) espiral, prototipação.

b) cascata, prototipação.

c) XP, conversa com os clientes.

d) espiral, cascata.

e) incremental, prototipação.

Comentários:

Usando o modelo espiral, o sistema é desenvolvido em ciclos, sendo que os primeiros ciclos podem não conter todas as atividades. O produto resultante de um primeiro ciclo pode ser uma especificação do produto ou um estudo de viabilidade. Os ciclos subsequentes podem ser protótipos, chegando progressivamente a versões operacionais do software, até se obter o produto completo. Modelos podem ser úteis para ajudar a levantar e validar requisitos, mas pode ocorrer de os clientes e usuários só terem uma verdadeira dimensão do que está sendo construído se forem colocados diante do sistema. Nestes casos, o uso da prototipação é fundamental.
Gabarito: Letra A

i6.(AOCP / UNIR - 2018) O desenvolvimento formal de sistemas é uma abordagem que tem pontos diferentes ao modelo em cascata e usa uma base da transformação matemática modal de uma especificação de sistemas em um programa executável.
Comentários:

O desenvolvimento formal de sistemas é uma variação do modelo em cascata, logo os pontos são muito parecidos. Ademais, ele utiliza uma base de transformação matemática formal e, não,modal.

Gabarito: Errado i7.(CS-UFG/UFG-20i7) É um modelo de processo geral de software que tem como característica a existência de duas fases distintas relacionadas à engenharia de requisitos. Qual é esse modelo?
a) Modelo em cascata.

b) Modelo orientado a reúso de componentes.

c) Modelo espiral de Boehm.

d) Modelo de entregas em estágios.

Comentários:

Trata-se do modelo orientado a reúso de componentes e as fases são: especificação de requisitos e alteração de requisitos.
Gabarito: Letra B

i8.(IFB / IFB - 2017) O modelo de processo de software evolucionário que acopla a natureza iterativa da prototipação com os aspectos sistemáticos e controlados do modelo cascata denomina-se:
a) Modelo Ágil.

b) Modelo Concorrente.

c) Modelo Iterativo.

d) Modelo Orientado a Objetos.

e) Modelo Espiral.

Comentários:

Modelo evolucionário que combina a natureza iterativa da prototipação com aspectos sistemáticos e controlados do modelo em cascata-também conhecido como prototipação em etapas-só pode se tratar do modelo em espiral.
Gabarito: Letra E

ig.(IESES / CEGÁS - 2017) Considerando o referencial de Boehm para o processo de desenvolvimento de software, modelo em espiral, assinale a alternativa que define as quatro ações que devem ocorrer em cada iteração:
a) Sprint, definição das funcionalidades, Desenvolvimento e validação e
Planejamento da próxima iteração.
b) Definição do product owner, Avaliação e redução de riscos,
Sprint, definição das funcionalidades.
c) Determinação dos objetivos, Avaliação e redução de riscos, Desenvolvimento e validação ePlanejamento da próxima iteração.

d) Determinação dos objetivos, Avaliação e redução de riscos, Sprint,
definição das funcionalidades.
Comentários:

Perfeito! De acordo com Boehm, os setores são: determinação dos objetivos; avaliação e redução de riscos; desenvolvimento e validação e planejamento da próxima iteração.
Gabarito: Letra C

2O.(IFB / IFB - 2017) Um framework de processo de software dirigido a riscos foi proposto porBoehm (1988) e é conhecido como modelo em espiral. Este processo de software é representado como uma espiral, e não como uma sequência de atividades. Cada volta na espiral representa uma fase do processo de software. Segundo Sommerville (2011), no modelo em espiral de Boehm, cada volta está dividida em quatro setores. Uma das alternativas abaixo NÃOdenomina um desses quatro setores. Assinale-a:

a) Desenvolver e verificar próximo nível do produto.

b) Avaliar alternativas, identificar, resolver riscos.

c) Gerenciar a qualidade e o custo do desenvolvimento.

d) Determinar objetivos, alternativas e restrições.

e) Planejar da próxima fase.

Comentários:

De acordo com Boehm, os setores são: determinar objetivos, alternativas e restrições; avaliar alternativas, identificar e resolver riscos; desenvolver e testar; e planejar as próximas fases. Logo,não existe: gerenciar a qualidade e o custo do desenvolvimento.

Gabarito: Letra C

2i.(FEPESE / MPE-SC - 2014) Assinale a alternativa abaixo que melhor identifica o modelo de processo de software no qual uma implementação inicial é exposta ao usuário para que possam ser realizados refinamentos posteriores que representam novas versões do sistema. As atividades de especificação, desenvolvimento e validação são intercaladas.
a) Relational Unified Process (RUP)

b) Desenvolvimento Evolucionário c) Método Ágil de Desenvolvimento d) Modelo de Desenvolvimento em Cascata e) Modelo de Engenharia de Software Baseado em Componentes
Comentários:

Mais uma questão bastante parecida: só pode ser o modelo (ou desenvolvimento) evolucionário.

Gabarito: Letra B

22.(IBFC/ EBSERH -2013) No modelo Cascata os requisitos são declarados pelos usuários no início do projeto e depois não se retoma mais a essa fase. Devido ao dinamismo das necessidades dos usuários pode-se minimizar esse problema com:
a) a prototipagem.

b) um desenvolvimento sequencial.

c) a análise por ponto de função.

d) caso de uso.

Comentários:

(a) Correto, a prototipagem permite minimizar problemas com requisitos tanto na fase de elicitação quanto na fase de validação de requisitos; (b) Errado, isso piora o problema do dinamismo de requisitos; (c) Errado, isso não tem nenhum relacionamento com os requisitos; (d)Errado, isso é apenas uma técnica de representação de requisitos.
Gabarito: Letra A

23. (ESAF / MPOG - 2010) As atividades do modelo espiral de Engenharia de Software são:

a) Planejamento, Análise dos Componentes, Análise de Hierarquia e Avaliação feita pelo cliente.

b) Planejamento, Análise dos Riscos, Engenharia e Avaliação feita pelo cliente.

c) Projeto, Análise dos Benefícios, Engenharia e Avaliação feita pelo gestor.

d) Planejamento, Eliminação dos Riscos, Análise de Contingência e Avaliação feita pelo cliente.

e) Planejamento, Projeto, Análise dos Riscos e Engenharia.

Comentários:

Nós vimos que uma das variações dos setores é: planejamento; análise de riscos;
engenharia; e avaliação do cliente.
Gabarito: Letra B

24.(FUNCAB / PRODAM-AM - 2010) Qual das alternativas a seguir corresponde ao modelo de processo, proposto no final da década de 80, que tem como principais características ser evolucionário, iterativo e focado na redução dos riscos?
a) Modelo em Espiral.

b) Modelo em Cascata.

c) Modelo em V.

d) Modelo Transformacional.

e) Modelo de Especificação Operacional.

Comentários:

Perfeito! Ele disse que o modelo é evolucionário e iterativo-além de falardos riscos!
É claro que se trata do Modelo em Espiral.
Gabarito: Letra A

25.(ESAF / ANA - 2009) O modelo de processo de software caracterizado por intercalar as atividades de especificação, desenvolvimento e validação, denomina-se:
a) modelo de workflow.

b) modelo de fluxo de dados.

c) desenvolvimento evolucionário.

d) transformação formal.

e) modelo em cascata.

Comentários:

Intercalar atividades de especificação, desenvolvimento e validação são características do modelo ou desenvolvimento evolucionário.
Gabarito: Letra C

26.(UFBA / UFBA - 2009) No processo de software baseado em componentes, cada componente projetado para reuso é uma entidade executável independente, que deve manipular exceções.
Comentários:

Para Pressman, um componente é uma parte do sistema modular, executável,
implantável,
independente, padronizada e reutilizável que encapsula a implementação e expõe um conjunto de interfaces do sistema. Logo, a primeira parte está correta! A segunda parte afirma que os componentes devem manipular exceções. Concurseiro lê um "deve" e já fica de olho aberto! Na verdade, de acordo com Sommerville:
"Os componentes não devem tratar as exceções por si mesmos, pois cada aplicação terá seus próprios requisitos para tratamento de exceções. Antes, 0 componente deve definir quais exceções podem surgir e publicá-las como parte da interface".
Gabarito: Errado

LISTA DE QUESTõES - CESPE

í. (CESPE / BANRISUL - 2022) Uma descrição ideal de um componente de software reutilizável deve ser feita com base no modelo 3C, que significa composição, conteúdo e contexto.
2. (CESPE / MPC-SC - 2022) No processo de desenvolvimento de software, a prototipação pode ajudartanto na elicitação de requisitos do sistema quanto no estudo de soluções específicas do software de modo a apoiar o projeto de interface de usuário.
3. (CESPE / MPC-SC - 2022) Usabilidade consiste em determinar, em uma solução de software,quão fácil é corrigir um problema após a sua detecção, uma vez que a engenharia de usabilidade refere-se à capacidade de diagnosticar o problema e modificar os componentes necessários para corrigi-lo.
4. (CESPE / MPC-SC - 2022) No modelo espiral de Boehm, cada volta na espiral representa uma fase do processo de software: na parte mais interna, enfoca-se a viabilidade do sistema e, no ciclo seguinte, a definição de requisitos, assim por diante, executando-se, ao longo dos ciclos, a análise de riscos, prototipação e codificação.
5. (CESPE / DPE-RO - 2021) Um analista deve escolher uma metodologia de desenvolvimento para elaborar o planejamento do ciclo de vida de um produto de software de larga escala. Osistema é inédito e o reúso de código semelhante não deve ser considerado como base para o novo desenvolvimento. O analista deve considerar, ainda, a necessidade de reduzir os riscos em todas as fases do projeto, pois é provável que os requisitos sejam aprimorados e mudem ao longo do processo. Entre os riscos a serem mitigados, está o de não ter sido contratado pessoal de software suficiente para construiro produto, além de a equipe contratada não ter experiência suficiente no desenvolvimento de produtos em larga escala. Ainda, há o risco de o fornecedor do hardware necessário ao projeto não entregartodas as estações clientes no prazo do contrato.
Nessa situação hipotética, para a metodologia do processo de software em questão, é mais apropriado o uso do:
a) modelo codificar-e-corrigir.

b) modelo espiral.

c) modelo integração e configuração.

d) modelo em cascata.

e) modelo baseado em protótipos.

6. (CESPE / Polícia Federal - 2021) Embora não seja dirigido a riscos,
o modelo de desenvolvimento de sistemas espiral de Boehm inclui, em seu framework, a etapa de análise e validação dos requisitos.
7- (CESPE / SERPRO - 2021) No modelo formal, as etapas do desenvolvimento do software incluem especificação formal para definição de requisitos, refinamento para concepção de projeto e prova para a verificação.
8. (CESPE / SLU-DF - 2019) No modelo de desenvolvimento de software em cascata, a abordagem é orientada ao risco e as tarefas são organizadas nos seguintes ciclos:determinar objetivos, identificar e resolver riscos, desenvolver e testar, e planejar a próxima iteração.
9. (CESPE / MPC-PA- 2019) Os modelos espiral e RAD (Rapid Application
Development) são classificados, respectivamente, como modelos de processo de desenvolvimento de software dos tipos a) incremental e sequencial.
b) evolutivo e incremental.

c) evolutivo e sequencial.

d) incremental e evolutivo.

e) evolutivo e evolutivo.

10. (CESPE / TRT-CE - 2017) Os modelos de processo em que o sistema é dividido em pequenos subsistemas funcionais que, a cada ciclo, são acrescidos de novas funcionalidades são denominados:
a) evolutivos.

b) unificados.

c) sequenciais.

d) incrementais.

11. (CESPE / MEC - 2014) No desenvolvimento de software de grande porte, não se usam, em conjunto, os seguintes modelos de processo de software genéricos: modelo em cascata,desenvolvimento evolucionário e engenharia de software embasada em computador.

12. (CESPE / TRT-10 - 2013) No modelo prototipação, a construção de software tem várias atividades que são executadas de forma sistemática e sequencial.
13. (CESPE / STF - 2013) O processo de software fundamentado no modelo em espiral apresenta o processo em loops compostos basicamente por setores, como, por exemplo,definição de objetivos, avaliação de riscos, planejamento e desenvolvimento e avaliação.
i4.(CESPE / ANT - 2013) O paradigma de programação orientada a aspectos traz soluções para alguns dos problemas existentes no paradigma orientado a objetos, como herança múltipla e sobrecarga de operadores.
15. (CESPE / SERPRO - 2013) A POA, uma evolução da programação orientada a objetos,
é implementada nas linguagens Java, C++, Smalltalk e Prolog.
16. (CESPE / TRT17 - 2013) O modelo espiral de modelagem de processos para desenvolvimento de software é finalizado quando o software é implantado.
17. (CESPE / MEC-2011) O modelo de processo denominado em espiral combina as atividades de desenvolvimento com o gerenciamento de riscos, de modo a minimizá-los e controlá-los.
18. (CESPE / AL-ES - 2011) No ciclo de vida em espiral, a de análise de risco é realizada na etapa da modelagem do produto.
19. (CESPE / FUB - 2011) Os diversos modelos de processo de software disponíveis permitem a representação abstrata de um processo de software sob diferentes perspectivas.No modelo evolucionário, sob a perspectiva da arquitetura, a velocidade de desenvolvimento faz que a produção de documentos que reflitam cada versão do sistema seja economicamente inviável,gerando problemas na validação independente de sistemas.

20. (CESPE / MEC - 2011) No modelo de prototipação, o processo de desenvolvimento de software é modelado como uma sequência linear de fases, enfatizando um ciclo de desenvolvimento de breve duração.
21. (CESPE / TRE-MT - 2010) A metodologia de prototipagem evolutiva é uma abordagem que visualiza o desenvolvimento de concepções do sistema conforme o andamento do projeto,por meio de protótipos visuais.
22. (CESPE / INMETRO - 2010) Um dos benefícios da prototipação é a documentação normalmente gerada, que facilita a manutenção dos sistemas a longo prazo e a elaboração de casos de teste.
23. (CESPE / INMETRO - 2010) Na abordagem evolutiva para desenvolvimento de software,
um protótipo do software é produzido e utilizado para identificar possíveis problemas com os requisitos, sendo descartado logo em seguida, e o desenvolvimento do software propriamente dito é, então, iniciado.
24. (CESPE / SERPRO - 2010) O modelo em espiral de ciclo de vida de software é iterativo e incremental, uma vez que a mesma sequência de atividades relacionadas à produção de software é realizada a cada ciclo da espiral.
25. (CESPE / SERPRO - 2010) O modelo de desenvolvimento em espiral permite repensar o planejamento diversas vezes durante o desenrolar do projeto.
26. (CESPE / INMETRO - 2010) No modelo em espiral, um exemplo de modelo iterativo,
cada loop da espiral representa uma fase do processo de software. Nesse modelo, os riscos não são considerados, pois podem impactar o projeto.
27. (CESPE / TRE-MT - 2010) O modelo de desenvolvimento em espiral, que tem a codificação como segunda etapa, gera o código do sistema muito mais rapidamente que o modelo de prototipação.
28. (CESPE / TRE-BA - 2010) Na engenharia de software baseada em componentes, na qual se supõe que partes do sistema já existam, o processo de desenvolvimento concentra-se mais na integração dessas partes que no seu desenvolvimento a partir do início. Essa abordagem é baseada em reúso para o desenvolvimento de sistemas de software.
29. (CESPE / UNIPAMPA - 2009) No modelo de desenvolvimento prototipagem, um protótipo é desenvolvido para ajudar no entendimento dos requisitos do sistema.
30. (CESPE / TCE-RN - 2009) A prototipação, uma abordagem para desenvolvimento de software na qual se cria um modelo do software que será implementado, é composta de quatro etapas:planejamento, análise de risco, engenharia e avaliação do cliente.

31. (CESPE / DETRAN-DF - 2009) O modelo de processo de desenvolvimento de software evolucionário parte do desenvolvimento de uma implementação inicial cujos resultados são apresentados aos clientes e refinados por meio de várias versões até que se alcance o sistema adequado. A prototipação, como processo, tem por objetivo compreender as especificações do software para se chegar aos requisitos para o sistema.
32. (CESPE / UNIPAMPA - 2009 O modelo espiral admite retorno às fases anteriores de desenvolvimento, suportando ainda a execução paralela de fases.
33. (CESPE / ANATEL - 2009) Entre os modelos de ciclo de vida de software, o modelo espiral possui maior proximidade com as práticas da engenharia clássica empregadas, por exemplo,na construção de casas, quando comparado aos modelos cascata e de componentes reusáveis.
34. (CESPE / IN METRO-2009) Uma das características marcantes do modelo de desenvolvimento em espiral é o fato de ele ser cíclico, e não linear, como o modelo de desenvolvimento em cascata.
35. (CESPE / UNIPAMPA - 2009) O modelo de desenvolvimento espiral foi desenvolvido somente para abranger as melhores características do ciclo de vida clássico.
36.(CESPE / UNIPAMPA - 2009) No modelo de desenvolvimento em espiral, a análise de riscos não impacta na elaboração de um produto ou protótipo.
37. (CESPE / TJDFT - 2008) A prototipação evolucionária não gera problemas de manutenção de sistema porque o desenvolvimento é rápido e não sofre grandes mudanças.
38.(CESPE / MPE-AM - 2008) No modelo de prototipação, a especificação de requisitos tem pouca importância, pois o software é continuamente adaptado em função dos desejos do usuário
39. (CESPE/TJDFT-2oo8) A prototipação de um software é uma técnica de desenvolvimento não-interativa porque o teste do sistema só ocorre na versão final.

40. (CESPE / TJDFT - 2008) Uma das finalidades da prototipação é reduzir o esforço de desenvolvimento de um software.
41. (CESPE / TJDFT- 2008) A prototipação evolucionária permite que a versão inicial do protótipo seja desenvolvida e refinada em estágios sequenciados, até que se chegue à versão final do sistema.
42. (CESPE /TJDFT- 2008) O modelo em espiral é um modelo de processos de software que reúne a natureza iterativa da prototipação com os aspectos sistemáticos e controlados do modelo sequencial linear.
43. (CESPE / TJDFT - 2008) Empregando o modelo de desenvolvimento em espiral, o software é desenvolvido em uma série de versões intermediárias incrementais.
44. (CESPE / SERPRO - 2008) O modelo iterativo e o modelo em espiral possuem características semelhantes: ambos permitem que as atividades do processo sejam planejadas e avaliadas ao longo do ciclo de vida.
45. (CESPE / MPE-AM - 2008) A utilização de um modelo de desenvolvimento embasado em componentes é uma forma de desenvolvimento em espiral que busca a reutilização de trechos de software desenvolvidos e testados em projetos anteriores e armazenados em um repositório.
46. (CESPE / SERPRO - 2008) Para a especificação de software e verificação de sistemas, uma alternativa que se fundamenta na matemática discreta e na lógica é o modelo incremental.
47. (CESPE / TSE - 2007) Um possível objetivo da prototipação é criar rapidamente um sistema experimental que possa ser avaliado por usuários finais. Um protótipo aprovado pelos usuários pode vir a ser usado como ponto de partida para a construção do sistema.
48. (CESPE / TRE-AL - 2004) No modelo de prototipação, o desenvolvedor cria inicialmente um modelo de software que será posteriormente implementado.
49. (CESPE/COHAB-2004) O modelo espiral é um modelo de processo de software que combina a natureza iterativa da prototipagem com os aspectos controlados e sistemáticos do modelo sequencial linear.
50. (CESPE / PBV-RR - 2004) O modelo em cascata é linear e sequencial. Modelos como o espiral e o Rational Unified Process pregam o desenvolvimento iterativo.
51.(CESPE/ BASA-2004) O modelo em espiral evolui à medida que o processo avança,
permitindo ao desenvolvedor e ao cliente entenderem melhor os riscos e reagirem em cada nível evolucionário.
52. (CESPE / PBV-RR - 2004) O modelo em espiral para desenvolvimento de software é fundamentado no faseamento comumente adotado em projetos de engenharia a partir da década de 70 do século passado. Tal modelo considera as seguintes fases: análise de requisitos,definição, projeto, implementação, integração e testes, operação e manutenção.

53. (CESPE / PBV-RR - 2004) O modelo em espiral de desenvolvimento proposto por Boehm apresenta a análise de riscos como uma das suas fases essenciais.
54. (CESPE / STJ-2004) O modelo de desenvolvimento em espiral requer a consideração dos riscos técnicos em todos os estágios ou interações do projeto, o que permite reduzir os riscos antes que se concretizem.
55. (CESPE/TRE-AL-2004) O modelo de desenvolvimento em espiral engloba o que há de melhor no modelo cascata e no modelo de prototipação, acrescentando a análise de risco,inexistente nestes dois modelos.
56. (CESPE / SERPRO - 2004) Enquanto o reúso em engenharia de software convencional está geralmente limitado à extensão e à manutenção de um sistema específico, o reúso, em engenharia de software por componentes, é um requisito de desenvolvimento,independentemente do projeto em consideração.

57. (CESPE / SERPRO - 2004) O uso de componentes pode estar condicionado a regras de licenciamento. Essa preocupação, no entanto, não existe se os componentes forem classificados como software livre.
GABARITo

1. ERRADO 20. ERRADO
39- ERRADO

2. ANULADO 21. CORRETO
40. CORRETO

3- ANULADO 22. ERRADO
41. CORRETO

4- ANULADO 23- ERRADO
42. CORRETO

5- LETRA B 24. ERRADO
43- CORRETO

6. ERRADO 25- CORRETO
44. CORRETO

7- CORRETO 26. ERRADO
45- CORRETO

8. ERRADO 27- ERRADO
46. ERRADO

9- LETRA B 28. CORRETO
47- CORRETO

10. LETRA D 29. CORRETO
48. CORRETO

íi. ERRADO 30. ERRADO
49- CORRETO

12. ERRADO 31- ERRADO
50. CORRETO

13- CORRETO 32. ERRADO
51- CORRETO

x4- ERRADO 33- ERRADO
52. ERRADO

15- ERRADO 34- CORRETO
53- CORRETO

i6. ERRADO 35- ERRADO
54- CORRETO

17- CORRETO 36. ERRADO
55- ERRADO

i8. ERRADO 37- ERRADO
56. CORRETO

19- CORRETO 38. ERRADO
57- ERRADO

LISTA DE QUESTõES - FCC

í. (FCC / TRF - 3a REGIÃO - 2019) No modelo em espiral de processo de software
(Boehm), antes de cada atividade de prototipação, é sempre realizada uma atividade de:
a) plano de desenvolvimento.

b) validação de requisitos.

c) teste de aceitação.

d) análise de riscos.

e) plano de ciclo de vida.

2. (FCC/TRF - 3a REGIÃO-2019) Considere o modelo de ciclo devida de software constituído por rotinas de trabalho com a participação de todos os membros da equipe, onde falhas não são toleráveis e por isso, entre as atividades, duas têm grande importância no processo:uma delas dedicada ao planejamento da etapa e outra à de análise de riscos. As atividades são apoiadas pela geração de protótipos. Suporta o desenvolvimento de sistemas complexos e de grande porte. Trata-se do modelo:
a) Interativo e Incremental.

b) RAD - Rapid Application Development.

c) Espiral.

d) Cascata.

e) Evolutivo.

3. (FCC / TRT16 - 2014) Os modelos de processo são uma representação abstrata de um processo de software, que podem serusados para explicardiferentes abordagens para o desenvolvimento de sistemas. Analise as seguintes abordagens:
Desenvolvimento I: intercala as atividades de especificação, desenvolvimento e validação.
Um sistema inicial é desenvolvido rapidamente baseado em especificações abstratas e depois é refinado com as entradas do cliente para produzir um produto que o satisfaça.
Modelo II: considera as atividades fundamentais do processo, compreendendo especificação,desenvolvimento, validação e evolução e as representa como fases de processo separadas,
tais como especificação de requisitos, projeto de software, implementação, teste etc.
III: baseia-se na existência de um número significativo de partes reusáveis.
O processo de desenvolvimento do sistema enfoca a integração destas partes, ao invés de desenvolvê-las a partir do zero.
Os modelos de processo genéricos descritos em I, II e III são, correta e respectivamente,associados a:

a) em Espiral - Baseado em Componentes - RAD

b) Evolucionário - em Cascata - Baseado em Componentes c) Baseado em Componentes - Sequencial - Refactoring d) Ágil - Sequencial - Unified Process e) em Cascata - Ágil - Refactoring
4. (FCC / DPE-SP - 2013) No desenvolvimento de software, podem ser utilizados os chamados modelos evolucionários, cujo objetivo é lidar com produtos que possam evoluir ao longo do tempo. Assinale a alternativa que contém APENAS modelos evolucionários de desenvolvimento de software.
a) UML e de qualidade.

b) Componentes e arquétipo.

c) Prototipagem e espiral.

d) Redes de Petri e certificação.

e) Semântico e validação.

5. (FCC/TST-2012) O Ciclo deVida de um Sistema especifica todas as fases de desenvolvimento,desde sua concepção até o processo de manutenção e declínio. No que diz respeito ao desenvolvimento de software, existem alguns processos conhecidos. Um destes processos,possui característica iterativa e incremental, inicia cada fase do projeto realizando um planejamento prévio, realiza a execução da fase, verifica o progresso e os resultados da fase(riscos, lições aprendidas) e incrementa novos objetivos para a fase seguinte, seguindo para a próxima iteração. O processo de software em questão é o:
a) Modelo espiral.

b) Ciclo de vida em cascata.

c) Modelo de desenvolvimento evolucionário (prototipação).

d) Modelo de desenvolvimento ágil.

e) Método de desenvolvimento Cleanroom (Sala Limpa).

6. (FCC / TRE-CE - 2012) No desenvolvimento de software em espiral (Boehm), cada loop está dividido em quatro setores. NÃO se trata da denominação de um destes setores:
a) levantamento.

b) definição de objetivos.

c) avaliação e redução de riscos d) desenvolvimento e validação.
e) planejamento.

7. (FCC / TRT20 - 2010) À medida que se avança pelo modelo ocorre uma iteração e o software evolui para estágios superiores, normalmente com aumento da complexidade. Cada iteração está provida das atividades determinadas pelos quadrantes planejamento, avaliação de alternativas e riscos, desenvolvimento do software e avaliação do cliente. No ciclo de vida de desenvolvimento de software, trata-se da propriedade do modelo:
a) Cascata.

b) Incremental.

c) Espiral.

d) Prototipação.

e) Balbúrdia.

8. (FCC / MPE-RN - 2010) O modelo em espiral difere principalmente dos outros modelos de processo de software por:
a) não contemplar o protótipo.

b) reconhecer explicitamente o risco.

c) não ter fases.

d) possuir uma fase única evolucionária.

e) não contemplar o projeto do produto.

9. (FCC / BAHIAGÁS - 2010) No modelo em espiral do processo de software cada loop na espiral representa:
a) uma disciplina de requisitos.

b) um enfoque de banco de dados.

c) uma tomada de decisão.

d) uma fase do processo.

e) um ciclo de programa.

GABARITo

1. LETRA D 4- LETRA C
7- LETRA C

2. LETRAC 5- LETRA A
8. LETRA B

3- LETRA B 6. LETRA A
9- LETRA D

LISTA DE QUESTõES - FCV

í. (FGV / IBGE-2016) A em presa SONOVATOS desenvolve sistemas há pouco tempo no mercado e, como padrão, sempre utilizou o modelo Cascata de ciclo de vida. Alguns clientes ficaram insatisfeitos com os produtos desenvolvidos pela empresa por não estarem de acordo com suas necessidades. Atualmente a SONOVATOS está desenvolvendo sistemas muito maiores,com duração de vários anos, e com requisitos ainda instáveis. O próprio processo de desenvolvimento da empresa também está em reformulação. Assim, a adoção de um novo modelo de ciclo de vida está sendo avaliada pelos gerentes da empresa. A intenção daSONOVATOS é, principalmente, gerenciar riscos e poder reavaliar constantemente o processo de desenvolvimento ao longo do projeto, o que permitiria correções nesse processo ou até mudança do tipo de processo. O modelo mais adequado para os sistemas atuais de longa duração da SONOVATOS é:
a) Rapid Application Development (RAD);

b) Espiral;

c) Extremme Programming;

d) Prototipação;

e) Modelo V.

2. (FGV ITCM-SP - 2015) Software, assim como todos os sistemas complexos, evolui ao longo do tempo. Modelos de processos evolucionários reconhecem a natureza iterativa e incremental da maioria dos projetos de engenharia de software e são projetados para adequar mudanças.Os modelos a serem utilizados em um processo evolucionário são:
a) cascata e modelo V;

b) prototipação e modelo espiral;

c) concorrente e métodos formais;

d) incremental e baseado em componentes;

e) processo unificado e orientado a aspectos.

3. (FGV / Fiocruz - 2010) Como modelo evolucionário do processo de software, uma característica da prototipagem é:
a) independer do estabelecimento e da definição de requisitos.

b) configurar um processo interativo e rápido de desenvolvimento.

c) iniciar o processo de desenvolvimento pela implantação e pelos testes.

d) gerar uma primeira versão do sistema completa e isenta de erros.

e) descartar a participação do cliente no processo de desenvolvimento e de implantação.

4. (FGV / BADESC - 2010) O Modelo Espiral, segundo Pressman (1995), incorpora as melhores características do Ciclo de Vida Clássico e da Prototipação e acrescenta o seguinte elemento:
a) análise dos riscos.

b) análise de projetos.

c) avaliação de usuários.

d) refinamento de requisitos.

e) refinamento de protótipos.

5. (FGV / Senado Federal - 2008) Considere as seguintes assertivas sobre modelos de processos de software:
I. No modelo em cascata, a fase seguinte não deve iniciar antes que a fase precedente tenha sido concluída.
II. No modelo evolucionário, a mudança constante tende a corromper a estrutura do software

III. A explícita consideração dos riscos no modelo em espiral distingue esse modelo dos modelos em cascata e evolucionário.
As assertivas corretas são:

a) somente I.

b) somente I e II.

c) somente I e III.

d) somente II e III.

e) I, lie III.

GABARITo

1. LETRA B

2. LETRA B

3. LETRA B

4. LETRA A

5. LETRA E

LISTA DE QUESTõES - DIVERSAS

í. (VUNESP / TJM-SP- 2021) Algumas atividades que fazem parte do modelo espiral de desenvolvimento de software são:
Construção - Implantação - Comunicação -
Planejamento - Modelagem

A ordem correta com que tais atividades são executadas, considerando o modelo espiral, é:

a) Comunicação, Planejamento, Modelagem, Construção e Implantação.

b) Construção, Implantação, Comunicação, Modelagem e Planejamento.

c) Modelagem, Planejamento, Construção, Implantação e Comunicação.

d) Planejamento, Construção, Implantação, Comunicação e Modelagem.

e) Planejamento, Modelagem, Comunicação, Construção e Implantação.

2. (VUNESP / CETESB - 2009) Considere um sistema cujos requisitos de interface são definidos apenas quando o cliente realiza um test-drive na aplicação e aprova essa interface.Assinale a alternativa que apresenta o modelo mais adequado para o desenvolvimento da interface desse sistema.
a) Ágil.

b) Cascata.

c) Iterativo incremental.

d) Prototipação.

e) Rapid Application Development.

3. (CESGRANRIO / PETROBRAS - 2018) O chefe dos desenvolvedores de sistemas de uma empresa acompanhou o seguinte diálogo entre um de seus subordinados, um usuário e o diretor de operações.
Diretor - Acho que já poderíamos começar o desenvolvimento daquele sistema que o departamento de esportes pediu.
Usuário - Não é cedo demais? Ainda não temos todas as funcionalidades bem definidas.

Desenvolvedor - É verdade, mas acho que já é possível especificar e implementar algumas funcionalidades mais importantes e construir uma primeira versão até o final do mês.Depois acrescentaríamos outras funcionalidades à medida que as fôssemos construindo,gerando, a partir da experiência do uso, versões sucessivas e cada vez mais completas.
Diretor-Acho isso ótimo, assim já teremos uma noção do impacto que o sistema poderá causar no desempenho dos atletas. Comecemos logo, não temos um efetivo tão grande em TI.
Usuário - OK, vamos em frente, mas não contem nada para aquele especialista em risco.
Já temos muito trabalho pela frente. Nossa estrutura ainda não suporta esse tipo de cuidado; se entrarmos nessa, o projeto vai atrasar. E mantenham o contato e o foco no objetivo:um produto simples, mas de qualidade.
A partir desse episódio e refletindo sobre o que ouvira, o chefe dos desenvolvedores deverá optar pelo modelo de processo de software:
a) RAD

b) incremental c) cascata d) espiral e) baseado em componentes
4. (CESGRANRIO / PETROBRÁS - 2014) Um técnico de informática, com o objetivo de agilizar o desenvolvimento de um software, escolheu o desenvolvimento evolucionário, uma abordagem da área de Engenharia de Software, que:
a) facilita a produção de sistemas bem estruturados, privilegiando um processo de mudanças contínuas, cada vez mais fáceis e baratas.
b) se baseia na existência de um número significativo de componentes reusáveis, num processo de desenvolvimento que enfoca a integração desses componentes, em vez de desenvolvê-los a partir do zero c) considera como atividades fundamentais do processo a especificação, o desenvolvimento,a validação e a evolução, representado-as como fases de processo separadas, sendo que para uma fase ser iniciada, a outra deve estar completamente terminada.
d) é mutuamente exclusiva com o modelo em cascata e de Engenharia de Software baseada em componentes, sendo que os subsistemas contidos em um sistema maior precisam ser desenvolvidos, usando a mesma abordagem ou modelo.
e) intercala as atividades de especificação, desenvolvimento e validação,
permitindo que um sistema inicial seja desenvolvido rapidamente, baseado em especificações abstratas.
5. (COSEAC / UFF - 2019) Nos projetos, quando o time quebra o produto em vários pedaços menores, trabalhando e entregando uma parte de cada vez, sem se preocupar com agilidade, e somente quando esta parte estiver pronta o time parte para outro pedaço, iniciando uma nova fase, constata-se um ciclo de vida:
a) preditivo.

b) iterativo e incremental.

c) adaptativo.

d) RUP.

e) cascata.

6. (IF-PA / IF-PA-2019) Tem-se como boas práticas em projetos de software a definição dos seus requisitos funcionais e suas funcionalidades. No decorrer dessa definição, pode surgir a necessidade de fornecer, de forma prioritária, um conjunto de funcionalidades iniciais básicas e,após esse fornecimento, podemos melhorar e expandir as funcionalidades em versões de software posteriores, até atingir todos os requisitos definidos. Nesse caso, estamos aplicando um modelo de processo de software denominado:
a) Métodos Formais.

b) Business Process Management (BPM).

c) Capability Maturity Model Integration (CMMI)

d) Incremental.

e) Entidade e Relacionamento.

7. (FADESP / IF-PA - 2019) O princípio fundamental é que, a cada ciclo, uma versão operacional do sistema será produzida e entregue para uso ou avaliação detalhada do cliente. Os requisitos têm de ser levantados e é preciso constatar que o sistema é modular. Esse é o modelo:
a) Incremental.

b) Espiral.

c) Cascata.

d) RAD.

e) XP.

8. (CETREDE / Prefeitura de São Gonçalo do Amarante - CE - 2019) Sobre Engenharia deSoftware, marque a opção INCORRETA.

a) O modelo Cascata tem como característica intercalar as atividades de especificação,desenvolvimento e validação. Esta abordagem, permite a entrega de um produto ao fim de um longo ciclo de desenvolvimento e com baixa perspectiva de falha funcional.
b) A engenharia de software baseada em componentes baseia-se na existência de um número significativo de componentes reusáveis, enfocando o desenvolvimento na integração destes componentes.
c) No desenvolvimento exploratório, o objetivo do processo é trabalhar com o cliente para explorar os requisitos e entregar o sistema final.
d) No processo de engenharia de requisitos, a etapa de elicitação e análise dos requisitos é responsável pela derivação de requisitos através da observação de sistemas existentes,discussões com usuários potenciais, análise de tarefas etc.

e) Especificação, projeto e implementação, validação e evolução do software são etapas comuns em qualquer processo de software.
9. (COSEAC / UFF - 2019) Dos modelos de desenvolvimento de software, aquele que prioriza a análise dos riscos envolvidos no desenvolvimento de cada parte do software é o modelo:
a) em cascata.

b) de prototipação.

c) incremental.

d) espiral.

e) baseado em componentes.

10. (INSTITUTO AOCP / UFFS - 2019) Assinale a alternativa que apresenta uma característica do modelo espiral para engenharia de software.
a) Na etapa "engenharia", são identificadas as alternativas e as restrições.

b) Contempla a análise de riscos, além das melhores características do ciclo de vida clássico e prototipação.
c) O modelo espiral veio para substituir o modelo cascata, que caiu em desuso por sua alta complexidade.
d) Esse modelo contempla as seguintes atividades: engenharia de sistemas, análise,
projeto,
codificação, teste e manutenção.

e) Esse modelo define que, na etapa de desenvolvimento, deve ser adotada uma metodologia ágil de desenvolvimento.
n.(COVEST-COPSET / UFPE - 2019) A respeito de modelos de processo de software, assinale a alternativa correta:
a) O modelo em cascata é inconsistente com outros modelos de processos de engenharia,
tendo documentação produzida em cada fase do ciclo. Dessa forma, o processo torna-se pouco visível,dificultando o monitoramento do progresso pelos gerentes, de acordo com o plano de desenvolvimento.
b) No modelo espiral de Boehm, o processo de software é representado como uma espiral em que cada volta representa uma fase do processo de software. O modelo não se tornou popular devido a problemas ligados ao gerenciamento de riscos de projeto.
c) Existem alguns tipos de sistema para os quais o desenvolvimento e a entrega incrementais não são a melhor abordagem. Por exemplo, alguns sistemas críticos, em que todos os requisitos devem ser analisados na busca por iterações capazes de comprometer a proteção ou a segurança do sistema.
d) Um modelo de processo para desenvolvimento de protótipos em que os objetivos da prototipação são descobertos ao final de cada iteração, depois que os usuários experimentarem os diversos protótipos produzidos ao longo do processo. Isso torna a abordagem pouco previsível e mais incerta.
e) Na entrega incremental, os clientes podem usar os incrementos iniciais como protótipos e visualizar o avanço gradativo no desenvolvimento, mas necessitam reaprender o uso do sistema quando sua versão final estiver disponível.
12. (IBFC/ Prefeitura de Cuiabá - MT - 2019) Heitor é gerente de projeto e precisa decidir qual modelo utilizará no processo de desenvolvimento do próximo software da empresaBrasil.
Quanto a alguns dos modelos do ciclo de vida de desenvolvimento de software, assinale a alternativa incorreta.
a) Modelo Espiral: produto final é entregue rapidamente b) Modelo Incremental: produzem o sistema de forma incremental até a sua versão final c) Metodologias Ágeis: dura de i(uma) a ^(quatro) semanas e ao final de cada iteração deve haver entrega ao cliente d) Modelo em Cascata: componente do sistema é entregue por fases, podendo acontecer paralelamente
13. (COSEAC / UFF - 2019) Em relação aos modelos de processos de software, avalie se são verdadeiras (V) ou falsas (F) as afirmativas a seguir:
I. O modelo de desenvolvimento orientado a reúso tem a vantagem da redução de riscos e de custos.
II. O modelo de desenvolvimento incremental possui a vantagem da facilidade de mapear os requisitos dos clientes dentro de incrementos de tamanho correto.
III. O modelo em cascata deve ser utilizado somente quando os requisitos forem bem compreendidos.
As afirmativas I, II e III são, respectivamente:

a) V, F e V.

b) F, V e V.

c) V, F e F.

d) F, Fe V.

e) V, V e V.

14.OADES / CFM -2018) O Modelo Espiral (Spiral) foi originalmente proposto por Boehm
(1986) e é fortemente orientado à redução de riscos.
WAZLAWICK, R. S. Engenharia de Software: Conceitos e práticas. São Paulo: Elsevier, 2013.

Considerando o exposto e o Modelo Espiral de ciclo de vida de software, assinale a alternativa correta:
a) O Modelo Espiral realiza uma etapa de cada vez, partindo para a próxima etapa apenas após a anterior estartotalmente validada.
b) Tal modelo de ciclo de vida tem foco apenas na resolução de riscos de requisitos mal compreendidos, fornecendo tempo suficiente para que estes possam ser entendidos e implementados.
c) O projeto é dividido em subprojetos, cada qual abordando um ou mais elementos de alto risco,até que todos os riscos identificados tenham sido tratados.

d) Cada iteração é iniciada sem planejamento prévio, resolvendo-se os problemas no momento em que surgem.
e) O início do ciclo de vida do projeto se parece mais com o Modelo Cascata.

15. (FADESP / IF-PA-2018) Usando o modelo, o sistema é desenvolvido em ciclos,sendo que os primeiros ciclos podem não conter todas as atividades. O produto resultante de um primeiro ciclo pode ser uma especificação do produto ou um estudo de viabilidade.Os ciclos subsequentes podem ser protótipos, chegando progressivamente a versões operacionais do software, até se obter o produto completo. Modelos podem ser úteis para ajudar a levantar e validar requisitos, mas pode ocorrer de os clientes e usuários só terem uma verdadeira dimensão do que está sendo construído se forem colocados diante do sistema. Nestes casos, o uso da éfundamental.
As expressões que completam corretamente os espaços em branco, respectivamente, são:

a) espiral, prototipação.

b) cascata, prototipação.

c) XP, conversa com os clientes.

d) espiral, cascata.

e) incremental, prototipação.

16. (AOCP / UNIR - 2018) O desenvolvimento formal de sistemas é uma abordagem que tem pontos diferentes ao modelo em cascata e usa uma base da transformação matemática modal de uma especificação de sistemas em um programa executável.
(CS-UFG / UFG -2017) É um modelo de processo geral de software que tem como característica a existência de duas fases distintas relacionadas à engenharia de requisitos. Qual é esse modelo?
a) Modelo em cascata.

b) Modelo orientado a reúso de componentes.

c) Modelo espiral de Boehm.

d) Modelo de entregas em estágios.

i8.(IFB / IFB - 2017) O modelo de processo de software evolucionário que acopla a natureza iterativa da prototipação com os aspectos sistemáticos e controlados do modelo cascata denomina-se:
a) Modelo Ágil.

b) Modelo Concorrente.

c) Modelo Iterativo.

d) Modelo Orientado a Objetos.

e) Modelo Espiral.

ig.(IESES / CEGÁS - 2017) Considerando o referencial de Boehm para o processo de desenvolvimento de software, modelo em espiral, assinale a alternativa que define as quatro ações que devem ocorrer em cada iteração:
a) Sprint, definição das funcionalidades, Desenvolvimento e validação e
Planejamento da próxima iteração.
b) Definição do product owner, Avaliação e redução de riscos,
Sprint, definição das funcionalidades.
c) Determinação dos objetivos, Avaliação e redução de riscos, Desenvolvimento e validação ePlanejamento da próxima iteração.

d) Determinação dos objetivos, Avaliação e redução de riscos, Sprint,
definição das funcionalidades.
20.(IFB / IFB - 2017) Um framework de processo de software dirigido a riscos foi proposto porBoehm (1988) e é conhecido como modelo em espiral. Este processo de software é representado como uma espiral, e não como uma sequência de atividades. Cada volta na espiral representa uma fase do processo de software. Segundo Sommerville (2011), no modelo em espiral deBoehm, cada volta está dividida em quatro setores. Uma das alternativas abaixo NÃO
denomina um desses quatro setores. Assinale-a:
a) Desenvolver e verificar próximo nível do produto.

b) Avaliar alternativas, identificar, resolver riscos.

c) Gerenciar a qualidade e o custo do desenvolvimento.

d) Determinar objetivos, alternativas e restrições.

e) Planejar da próxima fase.

21. (FEPESE / MPE-SC - 2014) Assinale a alternativa abaixo que melhor identifica o modelo de processo de software no qual uma implementação inicial é exposta ao usuário para que possam ser realizados refinamentos posteriores que representam novas versões do sistema. As atividades de especificação, desenvolvimento e validação são intercaladas.
a) Relational Unified Process (RUP)

b) Desenvolvimento Evolucionário c) Método Ágil de Desenvolvimento d) Modelo de Desenvolvimento em Cascata e) Modelo de Engenharia de Software Baseado em Componentes
22. (IBFC / EBSERH -2013) No modelo Cascata os requisitos são declarados pelos usuários no início do projeto e depois não se retoma mais a essa fase. Devido ao dinamismo das necessidades dos usuários pode-se minimizar esse problema com:
a) a prototipagem.

b) um desenvolvimento sequencial.

c) a análise por ponto de função.

d) caso de uso.

23. (ESAF / MPOG - 2010) As atividades do modelo espiral de Engenharia de Software são:

a) Planejamento, Análise dos Componentes, Análise de Hierarquia e Avaliação feita pelo cliente.

b) Planejamento, Análise dos Riscos, Engenharia e Avaliação feita pelo cliente.

c) Projeto, Análise dos Benefícios, Engenharia e Avaliação feita pelo gestor.

d) Planejamento, Eliminação dos Riscos, Análise de Contingência e Avaliação feita pelo cliente.

e) Planejamento, Projeto, Análise dos Riscos e Engenharia.

24. (FUNCAB / PRODAM-AM - 2010) Qual das alternativas a seguir corresponde ao modelo de processo, proposto no final da década de 80, que tem como principais características ser evolucionário, iterativo e focado na redução dos riscos?
a) Modelo em Espiral.

b) Modelo em Cascata.

c) Modelo em V.

d) Modelo Transformacional.

e) Modelo de Especificação Operacional.

25. (ESAF / ANA - 2009) O modelo de processo de software caracterizado por intercalar as atividades de especificação, desenvolvimento e validação, denomina-se:
a) modelo de workflow.

b) modelo de fluxo de dados.

c) desenvolvimento evolucionário.

d) transformação formal.

e) modelo em cascata.

26.(UFBA / UFBA - 2009) No processo de software baseado em componentes, cada componente projetado para reuso é uma entidade executável independente, que deve manipular exceções.
GABARITo

1. LETRA A 10. LETRA B
19. LETRA C

2. LETRA D li. LETRA C
20. LETRA C

3- LETRA B 12. LETRA D
21. LETRA B

4- LETRA E 13- LETRA A
22. LETRA A

5- LETRA B 14- LETRA C
23- LETRA B

6. LETRA D 15- LETRA A
24. LETRA A

7- LETRA A i6. ERRADO
25- LETRA C

8. LETRA A 17- LETRA B
26. ERRADO

9- LETRA D i8. LETRA E

