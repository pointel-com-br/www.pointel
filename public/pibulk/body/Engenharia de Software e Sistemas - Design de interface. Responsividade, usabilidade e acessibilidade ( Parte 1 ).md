# Engenharia de Software e Sistemas - Design de interface. Responsividade, usabilidade e acessibilidade ( Parte 1 )

Índice

1) Engenharia de Usabilidade

2) Engenharia de Usabilidade - Guias de Estilo deUsabilidade

3) Engenharia de Usabilidade - Usabilidade para Aplicativosem Dispositivos Móveis.

4) Engenharia de Usabilidade - Folhas de Estilo

5) Engenharia de Usabilidade - e-PWG

6) Resumo - Engenharia de Usabilidade

7) Questões Comentadas - Engenharia de Usabilidade - CESPE

8) Questões Comentadas - Engenharia de Usabilidade - FCC

9) Questões Comentadas - Engenharia de Usabilidade - FGV

10) Questões Comentadas - Engenharia de Usabilidade - Diversas.

11) Lista de Questões - Engenharia de Usabilidade - CESPE

12) Lista de Questões - Engenharia de Usabilidade - FCC

13) Lista de Questões - Engenharia de Usabilidade - FGV

14) Lista de Questões - Engenharia de Usabilidade - Diversas.

ENGENHARIA DE USABILIDADE

Conceitos Básicos

INCIDÊNCIA EM PROVA: MÉDIA

Pessoal, vocês já interagiram com um website que não está bem organizado ou que é complexo demais e não possui um menu de a/uda?Talvez vocêsjá usaram algum programa que por conta de um clique acidental os fez perder algum arquivo; ou um controle remoto com muito mais botões do que o que você realmente precisa; ou um touch-screen de caixa eletrônico que não responde rápido às suas ações.
Todos esses são problemas de usabilidade! Projetistas podem identificar muitos desses problemas e até consertá-los ao se focarem na usabilidade durante o processo de design do sistema. Eles podem aplicar métodos de usabilidade, como testes de usabilidade para assegurar que um produto satisfaz critérios de usabilidade ou InteligênciaArtificial para adaptar-se automaticamente ao usuário.
Vamos primeiro ver o que é usabilidade? A Norma ISO/IEC 9126 define usabilidade como a capacidade que um sistema interativo oferece a seu usuário, em determinado contexto de operação, para a realização de tarefas de maneira eficaz, eficiente e agradável. É a facilidade com que um usuário pode aprender a operar, preparar entradas para um sistema ou componente e interpretar suas saídas.
A Norma ISO/IEC 9241-11 define a usabilidade como sendo a medida na qual um produto pode ser usado por usuários específicos para alcançar objetivos específicos com eficácia,eficiência e satisfação em um contexto específico de uso. A Norma lembra que a usabilidade é dependente do contexto de uso e o nível alcançado dependerá das circunstâncias específicas nas quais o produto é utilizado.
De acordo com a Cartilha de Usabilidade do Governo Eletrônico (e-PWG - Usabilidade),
ela pode ser definida como o estudo ou a aplicação de técnicas que proporcionem a facilidade de uso de um dado objeto, no caso, um sítio. A usabilidade busca assegurar que qualquer pessoa consiga utilizar o sítio e que este funcione da forma esperada por essa pessoa.
Em resumo, usabilidade tem como objetivos a: facilidade de uso; facilidade de aprendizado;facilidade de memorização de tarefas; produtividade na execução de tarefas; prevenção,
visando a redução de erros; satisfação do indivíduo; entre outros. Para a usabilidade, o ponto de partida do desenvolvimento é sempre o usuário. Usuário é cada pessoa que utiliza o objeto em questão por meio de uma interface.
O RUP afirma que se trata da criação de sistemas melhores através da compreensão de quem são usuários finais e do envolvimento de usuários nos requisitos, no design de interface do usuário e nos esforços de testes, incluindo subcategorias: fatores humanos, estética,consistência na interface do usuário, ajuda online e contextuai, assistentes e agentes,documentação dos usuários e materiais de treinamento.
Inclusive, entre as técnicas de elicitação de requisitos de usabilidade,
podemos mencionar:
entrevistas e questionários, observações, cenários, grupos de foco, walkthroughs,
heurísticas para avaliação de usabilidade, e avaliação da estrutura de navegação. Percebam que algumas dessas técnicas são comuns às técnicas de elicitação de requisitos genéricos (aqueles que não têm nenhuma relação com usabilidade).
Jakob Nielsen afirma que usabilidade é um atributo de qualidade que avalia o nível de facilidade de uso de uma interface ou a medida de qualidade da experiência de um usuário ao interagir com um produto ou um sistema. Galera,esse cara é conhecido como o papa, rei, guru, líder quando o assunto é usabilidade! Vic Costello define usabilidade como a medida da experiência pessoal com uma interface de usuário. Podemos aplicar esse conceito a qualquer coisa que um usuário utiliza, do hardware ao software. A usabilidade se refere à medida em que os usuários podem alcançar seus objetivos de um contexto específico de forma efetiva,eficiente e com satisfação.

Usuários podem atingir seus objetivos com sucesso? Quanto esforço eles precisam fazer para completar uma dada tarefa? E quanto eles apreciam a experiência? Em outras palavras, usabilidade é sobre o usuário! Ela foca em como fazer uma interface mais fácil para as pessoas utilizarem,em vez de como treinar pessoas para se adaptarem melhor a uma interface desenhada de maneira desleixada.
É muito difícil mudar os hábitos de um grande número de usuários, e se uma interface for difícil de utilizar, muitos usuários encontrarão um produto alternativo ou página web que seja mais intuitiva. Ao final, uma interface usável oferece vantagem competitiva, mais lucro (ROI)e menos custos de manutenção1. Nielsen define cinco componentes ou critérios de qualidade que fazem algo ser usável:
CRITÉRIOS DE
QUALIDADE

DESCRIÇÃO

1 Pressman afirma: "Entre os muitos benefícios mensuráveis derivados de um sistema usável estão o aumento de vendas e a satisfação do usuário,vantagem competitiva, melhores opiniões na mídia, melhores comentários, custos de manutenção reduzidos, produtividade do usuário final melhorada, custos de treinamento reduzidos, custos de documentação reduzidos, probabilidade reduzida de litígio por clientes insatisfeitos".
LEARNABILITY
(FACILIDADE DE
APRENDIZADO)

EFFICIENCY
(EFICIÊNCIA)

MEMORABILITY
(MEMORIZAÇÃO)

ERRORS
(ERROS)

SATISFACTION
(SATISFAÇÃO)

Também conhecida como Intuitividade, o sistema deve ser de fácil aprendizado e assimilação,de forma que um usuário - mesmo sem experiência - possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
O sistema deve ser eficiente no uso, isto é, uma vez que o usuário tenha aprendido o design do sistema, ele deve poder executartarefas com um alto nível de produtividade.
O sistema deve ser fácil de lembrar, para que o usuário seja capaz de retornar depois de um tempo sem ter que aprendertudo novamente.
O sistema deve ter um baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Ademais, erros catastróficos não devem ocorrer.
O sistema deve ser agradável de usar, para que os usuários fiquem satisfeitos e voltem mais vezes para usá-lo.
Esses não são os únicos componentes de qualidade, existe outro muito famoso que deve ser pensado de forma paralela com a usabilidade - trata-se da Utilidade! Uma interface que provê utilidade é aquela que fornece as características de que você necessita. A usabilidade diz quão fáceis e prazerosas essas características são de usar. Uma interface útil é aquela que une utilidade e usabilidade! Pessoal, vocês conhecem o Ciclo da Engenharia de Usabilidade?
Ele foi proposto por Deborah Mayhew e se divide em três fases: Análise de Requisitos;
Projetof
Testes e Implementação; e Instalação. Vamos nos focar apenas na primeira fase! Bem,
você pode reunir ou elicitar os requisitos dos usuários para o seu produto em um número diverso de maneiras.
Ex: você pode desenhar protótipos em papel para dar às pessoas representações impressas de como seu produto ficará parecido visualmente e como o sistema vai reagir às entradas do usuário.
Não importa como você obtém seus requisitos, você deve se certificar de avaliar os seguintes pontos abaixo para garantir que você tenha todas as opções cobertas. Vejamos:
Para cada categoria de usuário, projetistas devem conhecer atributos pessoais
(idade, sexo, limitações, motivação) e suas habilidades e competências (na tarefa,
na organização e com sistemas informatizados).

Para cada tarefa a ser apoiada pelo sistema, os projetistas devem conhecer os objetivos e resultados, a estrutura, a duração, as dependências, os custos, a carga mental, as interrupções, os incidentes, entre outros.
Devem ser examinadas as possibilidades e restrições em termos de equipamentos, sistemas operacionais, ambientes de janelas, recursos de rede,entre outros.

Pesquisa e catalogação do conhecimento ergonômico disponível para a concepção da interface no tipo de contexto de uso (usuário, tarefa, equipamento e ambiente) no qual o sistema está inserido.
E como avaliar a usabilidade? Bem, utilizam-se metodologias para medir os aspectos de usabilidade da interface de um sistema e identificar problemas específicos. O processo de avaliação de usabilidade inclui atividades como: captura, que coleta dados de usabilidade, tempo de execução, erros, etc; análise, que interpreta os dados para identificar problemas; e crítica, que sugere soluções e melhorias.
E AÍ, USABILIDADE NÃO É IMPORTANTE?

Vamos conversar agora! Eu sei que alguns de vocês são programadores ou analistas e acham um saco essa história de usabilidade! Os especialistas em usabilidade vão discordar e dizer que se trata da melhor metodologia possível. No entanto, há um ditado que cabe bem aqui: "Oótimo é inimigo do bom"\ Insistir na utilização apenas dos melhores métodos pode resultar em nenhum método sendo utilizado.
Sendo assim, alguns se concentram em alcançar "o bom", no que diz respeito a ter algum trabalho de engenharia de usabilidade realizado no sistema, em vez de se concentrar demais nos métodos de usabilidade para alcançar o - talvez inalcançável - "ótimo" em questão. Lembrem-se que frequentemente projetos mais bem desenhados também são mais caros. Essa introdução toda foi para falar que os engenheiros de usabilidade foram espertos e também tiveram essa sacada!
Jakob Nielsen criou a Engenharia de Usabilidade Descontada/Reduzida, que é um método de simplificação da usabilidade para realizar melhorias rápidas e baratas nas interfaces de usuário:
TÉCNICAS DE ENGENHARIA DE
USABILIDADE DESCONTADA

OBSERVAÇÕES DO
USUÁRIO E DA TAREFA

DESCRIÇÃO

Trata-se da observação de usuários utilizando o sistema para descobrir nível de utilização, desentendimentos, entre outros.
CENÁRIOS DE USO Trata-se de uma espécie de prototipação para obterfeedback sobre a usabilidade do sistema.
VERBALIZAÇÃO SIMPLIFICADA Trata-se de um usuário de teste por vez realizando um conjunto de tarefas no sistema enquanto se pede que ele verbalize o que pensa.
AVALIAÇÕES HEURÍSTICAS Trata-se de avaliações que examinam se uma interface está de acordo com princípios reconhecidos de usabilidade (heurísticas).
Aqui cabe salientaralgumas coisas! Jakob Nielsen cita dez princípios gerais ou recomendações para avaliação de heurísticas, apresentadas a seguir:
PRINCÍPIOS PARA
AVALIAÇÃO DE HEURÍSTICAS

VISIBILIDADE DO STATUS DO

SISTEMA

DESCRIÇÃO

0 sistema deve sempre manter os usuários informados sobre o que está acontecendo, através de feedback apropriado e em tempo razoável.
LIBERDADE E CONTROLE DO

USUÁRIO

PREVENÇÃO CONTRA

ERROS

FLEXIBILIDADE E EFICIÊNCIA DE

UTILIZAÇÃO

AUXILIAR USUÁRIOS A
RECONHECER, DIAGNOSTICAR E

RESOLVER ERROS

COMPATIBILIDADE ENTRE SISTEMA

EO MUNDO REAL

Usuários frequentemente escolhem algumas funções do sistema por engano e vão precisar sempre de uma "saída de emergência" claramente marcada para sair daquele estado indesejado sem ter que passar por um extenso "diálogo". Apoio ao desfazer e refazer.
Ainda melhor do que boas mensagens de erro é um projeto cuidadoso que impede que, em primeiro lugar, esse erro possa ocorrer. Eliminando as condições passíveis de erros ou verificá-las, apresentado aos usuários uma opção de confirmação antes de se comprometerem com uma determinada ação.
Aceleradores - invisíveis para o usuário novato - podem frequentemente acelerar a interação para o usuário experiente, que o sistema pode atender a ambos os usuários inexperientes e experientes. Permitir aos usuários personalizar ações frequentes.
Mensagens de erros devem ser expressas em linguagem clara (sem códigos),
indicar com precisão o problema e construtivamente sugerir uma solução.

O sistema deve falar a linguagem dos usuários, com palavras, frases e conceitos familiares ao usuário, ao invés de termos orientados ao sistema. Siga convenções do mundo real, tornando as informações que aparecem em uma ordem natural e lógica.
Os usuários não precisam adivinhar que diferentes palavras, situações ou ações significam a mesma coisa. Siga as convenções da plataforma e mantenha a previsibilidade do sistema.
Minimizar a carga de memória do usuário tornando objetos, ações e opções visíveis. O usuário não deve ter que se lembrar da informação de uma parte do diálogo para outra. Instruções de uso do sistema devem estar visíveis e serem facilmente recuperáveis quando necessário.
Os diálogos não devem conter informações irrelevantes ou raramente necessárias. Cada unidade extra de informação em um diálogo compete com as unidades relevantes de informação e diminui sua visibilidade relativa.
Mesmo que seja melhor que um sistema possa ser usado sem documentação,
pode ser necessário fornecer uma ajuda e documentação. Qualquer informação deve serfácil de ser pesquisada, com foco na atividade do usuário, lista de passos concretos a serem realizados, e não ser muito grande.
Depois de considerar todos os fatores de usabilidade já citados, deve haver uma maneira de descobrir se um site alcançou certo grau de usabilidade - para tal, fazemos testes de usabilidade! Claro que não estamos tentando encontrar problemas funcionais. Oobjetivo é aprender mais sobre usuários potenciais, saber o que eles sabem, como pensam, reagem e o que realmente querem de um website.
Primeiro, é necessário separar clientes de usuários. Se estamos desenhando um website de e-commerce da Dona Maria, não devemos fazer testes de usabilidade conduzidos pela Dona
Maria,
muito menos pelos programadores ou web designers. Nós devemos fazer os testes de usabilidade com os potenciais usuários que poderiam realizar compras por esse website - assim a avaliação é mais confiável!
Dessa forma, escolhemos os potenciais usuários, depois desenhamos as tarefas a serem testadas,em seguida devemos planejar a quantidade de tempo gasto com cada usuário e alocar papéis para os testadores (Ex: Facilitador, Anotador e Observador). Por fim, recomenda-se guardar todos esses dados por meio de papel e caneta ou gravadores de áudio e vídeo. Roger Pressman adota outra sequência de atividades para realizar testes de usabilidade em aplicações web:
í. Definir categorias de testes de usabilidade e identificar cada objetivo;

2. Projetar testes que possibilitam que cada objetivo possa ser avaliado;

3. Selecionar participantes que irão conduzir ostestes de usabilidade;

4. Dar instrumentos para a interação dos participantes com a aplicação;

5. Desenvolver um mecanismo para avaliar a usabilidade na aplicação.

O autor também afirma que a única maneira de determinar a usabilidade é por meio de testes e avaliações. Deve-se observar usuários interagindo com o sistema e responder uma série de questões, entre elas: O sistema é usável sem ajuda ou instrução contínua? As regras de interação ajudam um usuário bem informado sobre como o sistema funciona eficientemente? Ainteração é simples?
Aqui cabe enfatizar rapidamente o conceito de Design Centrado no Usuário (DCU)! Ele surge nosEstados Unidos no bojo da popularização da computação pessoal. Os sistemas computacionais eram projetados até então para serem operados por especialistas em computação e, quando um especialista em outro assunto ia usar, tinha grande dificuldade. As pesquisas de InteligênciaArtificial prometiam minimizar as interfaces de usuário, evitando o "erro humano".

Algoritmos conseguiriam antecipar as necessidades dos usuários e entregar o resultado direto. Adificuldade de implementartal proposta levou pesquisadores da cognição humana a formular uma abordagem menos formal em que o usuário seria essencial ao projeto, ao invés de um fator de risco.O Design Centrado no Usuário coloca a culpa dos "erros humanos" em parte nos sistemas computacionais. Porque?
Porque eles não levaram em consideração as características cognitivas de seus usuários,apresentando interfaces confusas que induziam ao erro. Além de prevenir o erro humano,
propõe-
se uma série de outras qualidades para os sistemas computacionais do ponto de vista do uso,sendo a mais conhecida a usabilidade. De acordo com o RUP, o Design Centrado no Usuário possui quatro componentes:
Foco nos Usuários: desenvolvedores devem decidir quem serão os usuários e devem envolvê-
los o quanto antes no projeto;

Integração com Design: tarefas de usabilidade devem ser realizadas em paralelo desde o início do desenvolvimento do software;
Teste com o Usuário no Início: a criação inicial de protótipos, normalmente esboços e modelos de baixa fidelidade;
Design Iterativo: um processo iterativo, que se adapta bem a problemas que necessitam de refinamento de compreensão.
Além disso, o framework afirma que o Design Centrado no Usuário fornece:
atendimento das necessidades dos usuários; design da interface do usuário; e uma conformidade com legislações e padrões. Ademais, uma interface de usuário deve atender um espectro de experiência que aborde duas dimensões: a experiência com o computador e a experiência com o domínio. Sabe-se que os usuários vão ganhando experiência ao usaro sistema, mas isso não significa que se tornarão peritos!
Por que, professor? Por baixa frequência de uso, baixa motivação ou alta complexidade.
De modo contrário, alguns sistemas podem ter, predominantemente, usuários peritos ou especialistas. Os fatores aqui podem ser treinamento, alta frequência de uso ou alta motivação(confiança no emprego). Algumas dessas questões e seus efeitos no design da interface de usuário são mostrados na tabela a seguir:
BAIXA ALTA

EXPERIÊNCIA
COMO USUÁRIO

EXPERIÊNCIA
COM O DOMÍNIO

TREINAMENTO
FREQUÊNCIA DE

_ _ _ _ _ _ USO

MOTIVAÇÃO

Pergunta e resposta simples,
preenchimento de formulário simples, estilo de interface web (com hyperlinks) ou de menus.
Terminologia e conceitos usuais.

Foco na facilidade de aprendizagem
(consistente, previsível, memorável).

Fácil de aprender e lembrar, estilo de interface simples.
Uso recompensado, poderoso sem parecer complexo.
Preenchimento de formulário complexo, estilo de interface web (com hyperlinks) ou de menus(pergunta/resposta ou preenchimento de formulário simples seria muito frustrante para usuários experientes).
Terminologia e conceitos específicos ao domínio.

Foco na facilidade de uso (direto, personalizável, não intrusivo).
Fácil de usar, vários atalhos e técnicas para permitir o controle pelo usuário.
Sofisticado com muitas características avançadas e personalizáveis.
Vocês sabem o que é a letra H em HTTP/HTML? Significa Hypertext ou Hipertexto!
Trata-se de um texto interativo, com informações acessíveis por computadores, smartphones,tabletes, etc - o usuário é capaz de ler de forma não linear, ou seja, ele escolhe entre o início, o meio ou o fim do conteúdo. Além disso, o hipertexto pode ser considerado um tipo de hipermídia.Lembrando que a hipermídia inclui textos comuns, sons, animações e vídeos.
Trata-se da reunião de várias mídias num ambiente computacional, suportada por sistemas eletrônicos de comunicação. Professor, por que você está falando sobre isso? Porque existem diversas estruturas de navegação hipermídia, que organizam os conteúdos (hierarquia e arquitetura da informação). Dessa forma, os conteúdos podem ser relacionados e simultaneamente permitir que o usuário tenha relativa liberdade para a exploração dos conteúdos. Vejamos:
ESTRUTURAS DE
NAVEGAÇÃO

DESCRIÇÃO

LINEAR Os usuários só podem navegar sequencialmente, de uma tela para outra, ou de um campo de informação para o outro.
HIERÁRQUICO Os usuários navegam ao longo das ramificações de uma estrutura do tipo árvore que é formada pela lógica natural do assunto.
NÃO-LINEAR Os usuários podem navegar livremente através do conteúdo da aplicação multimídia, sem qualquer restrição.
COMPOSTO Os usuários navegam livremente, mas existem situações com restrições lineares ou hierárquicas, porexemplo.
Temos que falar também sobre os seis princípios fundamentais de Don Norman! Quem é esse cara,professor? É um dos pais da usabilidade! Ele realça a importância de se pensar nas pessoas e na interação que elas terão com os produtos e sistemas que estão em desenvolvimento. Épor conta disso que áreas como UX Design são tão importantes dentro de uma empresa. Para garantir que as experiências dos usuários finais sejam as melhores possíveis.
E como garantir que todos esses usuários tenham uma excelente experiência com os seus designs?
Norman escreveu - baseado no conceito de Design Centrado no Usuário -seis princípios:

O princípio da visibilidade traz a questão da descoberta. O usuário descobre as funções da interface pelo simples fato de estarem visíveis para interação. Ou seja, quanto mais visível uma função estiver, mais os usuários a notarão e utilizarão. Nesse sentido, botões e menus visíveis tornam a jornada do usuário mais fácil. Ao passo que, se essas funções não estiverem visíveis, elas não serão utilizadas.
Sobre a visibilidade, é importante estar atento à priorização das funções.
Não é recomendável colocar botões e menus para todas as funcionalidades de um sistema. A tela fica poluída e não há distinção das funções mais importantes. O grande desafio é entender como priorizar o conteúdo e as funções.
O Feedback é a resposta que o usuário deve receber após efetuar alguma ação na interface.Para toda interação em um produto, é natural criara expectativa por uma resposta. Seja ela confirmando o sucesso ou o insucesso da ação. Caso isso não ocorra, o usuário pode ficar com dúvidas e sua experiência ser impactada. Um exemplo bastante simples e do dia a dia é o simples clique de um botão.
Se não houver um feedback garantindo que o botão foi acionado, o usuário continuará clicando. Há duas categorias de feedback: ativador, quando a resposta para uma ação é sensorial, como um efeito visual ou sonoro; ou comportamental, quando a resposta indica que a ação teve algum efeito dentro do sistema.
Para evitar qualquer ação inválida/incorreta pelo usuário, um sistema deve conter restrições.Dentro do Design de Interação, elas podem ser tanto físicas quanto comportamentais. As restrições físicas podem ser exemplificadas com a própria tela do celular. Não há como ter interação fora dela. Já restrições comportamentais estão mais relacionadas com a experiência do usuário e com quais ações ele pode efetuar-ou não-dentro da interface.
Um exemplo interessante são os botões de ação de qualquer programa de computador.
Quando uma ação está restrita ao usuário, o botão geralmente aparece cinza e opaco,
deixando claro que a função não está disponível naquele momento. Este tipo de restrição também é comum em formulários online, onde o botão "submeter" fica inativo até todo o formulário estar preenchido corretamente.
A falta de restrições pode gerar confusão e frustração para o usuário, fazendo com que ele clique incorretamente em botões inativos, ou envie um formulário com informações incompletas.
Está claro que qualquer ícone, botão ou controle, ao ser ativado, acionará alguma função dentro do sistema. Mas, além disso, é importante que haja uma relação entre o design e a função atrelada a ele. Esta relação, dentro do Design de Interação, chama-se Mapeamento.Nesse sentido, quanto mais o usuário assimila os controles com a sua percepção da realidade,
melhor é a interação e a experiência.

Por exemplo: o botão de volume mostra barras mais longas conforme o volume aumenta, e barras mais curtas conforme o volume diminui. Apesar de parecer óbvio, o mapeamento requer bastante atenção e testes com usuários reais. Uma maneira interessante de saber se o mapeamento está correto é observar o design de um controle e pensar na expectativa que se tem sobre ele.
Se é um controle que indica aumento ou diminuição gradual, pode-se pensar em usar os símbolos "+" e se a ideia é começar um vídeo, a expectativa é que o botão tenha um triângulo simbolizando o play.
Uma das maneiras de melhorar a experiência do usuário e garantir uma curva de aprendizagem rápida, é a utilização de padrões. Criar padrões ajuda o usuário a assimilar melhor o seu sistema, fazendo com que a navegação se torne mais simples e fácil. AConsistência, em design de interação, nada mais é do que criar esses padrões dentro do sistema.
CONSISTÊNCIA

Representar de forma semelhante os controles com funções semelhantes, posicionar os botões no mesmo lugare da mesma forma, usaras mesmas cores, etc. Afalta de consistência pode causar demora na ação e confusão para o usuário. A ideia é sempre fazer com que ele assimile cada função do seu sistema, sem ter que se preocupar com exceções. Além disso, é importante entender se há consistência com outros sistemas semelhantes.
Por exemplo: se em todos os sites a escrita e a leitura são feitas da esquerda para a direita,não é recomendável que o seu site faça de outra forma. Fazer algo de forma diferente é bom se não for atrapalhar a maneira com que o usuário já está acostumado a fazê-lo em outros sistemas.
Para finalizar, vamos falar sobre Style Guides, que são guias de estilo que fornecem um Look andFeel consistente. Em geral, são definidos como parte dos requisitos de usabilidade. Professor, por que utilizá-los? Porque elas incorporam as boas práticas em design de interface; porque aumenta a coerência entretelas; porque reduz otempo de desenvolvimento; e porque melhora a qualidade da interface. Entendido?
Guias de Estilo de Usabilidade

INCIDÊNCIA EM PROVA: BAIXA

Um guia de estilo comum é aquele documento que contém descrições sobre o uso e estilo de determinados componentes de interação, como menus, caixas de diálogo e mensagens. Já um guia de estilo de usabilidade tem como objetivo estabelecer padrões, na forma de diretrizes,para o desenho da interface com o usuário. Os padrões definidos no guia visam garantir a consistência interna e externa do desenho da interface com o usuário.
Lembrando que a consistência interna se refere aos elementos da interface de um produto e a consistência externa se refere à consistência com outros produtos de uma família de produtos de software. Em geral, o guia é desenvolvido ou atualizado junto com o projeto da interface com o usuário. Para o desenvolvedor da interação, serve como referência para o desenho da interface e como registro de novos padrões estabelecidos. Para usuários e clientes, o guia deve ser usado como uma meta-documentação do desenho da interface externa.
Ele deve ser preferencialmente desenvolvido já nas atividades de projeto para capturar e documentar decisões e prevenir mudanças futuras. Esse documento geralmente apresenta uma introdução com objetivos do documento; audiência/público do documento; intenção de uso;histórico do documento; escopo; consistência com outros padrões; referências a documentos relevantes; identificação do cliente e do fornecedor; dados do projeto; e organização.
Em seguida, ele pode apresentaras diretrizes gerais: princípios de design; diretrizes de usabilidade;e diretrizes para o desenho da interface (cores, fundo, ícones, fontes, textos, etc).
Por fim, pode falar sobre os padrões específicos da família de produtos: aspectos gerais;padrões de comportamento da interface; elementos de interação; mensagens; dispositivos de interface de hardware; e padrões específicos.
Usabilidade Para Aplicativos em Dispositivos Móveis

INCIDÊNCIA EM PROVA: BAIXA

O crescente mercado de dispositivos móveis capazes de executar aplicações desenvolvidas por terceiros está gerando uma concorrência cada dia maior para o mercado de aplicativos,os quais estão tendo que melhorar continuamente para sobreviver. A chave para esta melhora está no aumento da experiência do usuário. A área da computação que estuda esse assunto é a usabilidade.
Pois é! Em meados da década passada, os conceitos de usabilidade eram mais aplicados aos desktops e sistemas web. A maioria dos dispositivos móveis que existiam tentavam ao máximo se aproximar de um desktop e pelo seu tamanho reduzido sua usabilidade ficava muito prejudicada. Ao final da década, as maiores empresas do ramo começaram a perceber esta deficiência.
Foi, então, que o mercado começou a diferenciar a usabilidade dos sistemas levando em conta as peculiaridades de uso dos dispositivos móveis em relação aos desktops. Com a melhoria, as vendas cresceram vertiginosamente, chegando - em 2013 - a ultrapassar a venda de celulares comuns. Atualmente, grande parte do sucesso dos dispositivos móveis está na capacidade de executar aplicativos.
A Apple já lançou a Apple Store preocupada com a usabilidade dos aplicativos que ali seriam disponibilizados - assim como sempre foi preocupada com a usabilidade de seus sistemas.Atualmente, para que um aplicativo de um desenvolvedor externo fique à venda na loja,
deve passar antes por uma revisão minuciosa de profissionais que verificam todos os pontos de usabilidade.
Caso não cheguem ao seu nível de aceitação, o aplicativo é rejeitado e volta a ser reavaliado após eventuais ajustes. Quais são as peculiaridades da usabilidade do universo mobile,professor? Segundo
Jakob Nielsen, os mesmos pontos definidos anteriormente para usabilidade geral de sistemas podem ser considerados com os devidos ajustes e, claro, dando bastante importância aos critérios de design.
Dessa forma, para um sistema mobile ter boa usabilidade, deve ter suas tarefas executadas pelo usuário com a maior eficiência possível. Para isto, deve levar em conta as limitações de hardware,como processador mais lento que o de um computador, memória menor, limitações de tamanho de tela e de uso com os dedos ou canetas de toque. É neste ponto que o design deve ser muito bem pensado.
O usuário do sistema deve aprender a realizar todas as suas tarefas facilmente e isto implica dizer que, mais uma vez, o design do sistema deve estar organizado da melhor forma possível para que o usuário não seja obrigado a dedicar muito esforço em cada tarefa, considerando as limitações já citadas. Já a satisfação do usuário deve ser conseguida bem mais rapidamente em um sistema mobile. Porque, Diego?
Porque as tarefas realizadas em um dispositivo móvel geralmente são menores e executadas mais rapidamente. Os sistemas móveis devem ser relembrados após um período sem uso pelo usuário. Além disso, deve ocorrer o menor número possível de erros durante a execução,levando em conta que o dispositivo móvel tem mais limitações e, portanto, maior possibilidade de esses erros acontecerem.
Muitos pontos que podem melhorar a usabilidade normalmente só podem ser considerados depois da etapa de desenvolvimento, já na fase de testes do sistema com usuários reais, fazendo com o que componentes tenham que ser refeitos ou remodelados, tornando o processo iterativo e consequentemente mais custoso, tanto sob o ponto de vista de orçamento quanto sob o ponto de vista do prazo.
O desafio é mostrar à equipe de desenvolvimento a importância de se priorizar a usabilidade durante todo o processo de desenvolvimento obtendo um melhor resultado inicial,diminuindo o custo de produção e aumentando o fluxo de trabalhos. As etapas de análise e validação de requisitos também são importantes no desenvolvimento de softwares para dispositivos móveis. Porque, professor?
Porque são nelas que as peculiaridades deste tipo de sistema são colocadas em relação às funcionalidades reais. Na etapa de análise de requisitos, é de suma importância que sejam definidas todas as ações necessárias para suprir as limitações dos dispositivos móveis como requisitos, mas também apresentá-las como riscos quando convir. Por que? Porque nem sempre será possível obedecer a todas as restrições de projeto para implementá-lo.
A etapa de verificação e validação dos requisitos é a mais importante neste processo de otimização do aumento da usabilidade no processo de desenvolvimento, pois diversos testes de usabilidade podem ser aplicados em protótipos de alta fidelidade, fazendo com que ajustes possam serfeitos nas especificações do sistema para que seja revalidado e desenvolvido já com a mais alta usabilidade possível.
Tomando uma empresa de comércio eletrônico como exemplo, o site padrão da empresa tem toda sua interface voltada para ser acessada por computadores desktop, deixando difícil a usabilidade ao ser acessada por dispositivos móveis devido aos muitos itens disponíveis na tela ao mesmo tempo e ao tamanho reduzido - e até mesmo à natureza desse tipo de página. Ecomo contornar esse problema?
A empresa utiliza um site mobile, que é aberto automaticamente quando o usuário acessa de um dispositivo móvel. Neste site mobile, vários pontos de usabilidade podem ser melhorados como o tamanho dos itens ou a quantidades de itens na tela por vez, mas outros precisam de recursos existentes em cada plataforma móvel específica. Para isto a empresa usa um aplicativo específico para cada plataforma, o qual segue cada respectivo padrão de interface e de forma de uso.
Isso faz com que sejam agregados mais recursos e o usuário aprenda a usar o sistema mais rapidamente, elevando a usabilidade e consequentemente as suas vendas.
Folhas de Estilo

INCIDÊNCIA EM PROVA: BAIXA

As Folhas de Estilo em Cascata (CSS) são uma extensão elegantemente desenhada para a web e uma das maiores esperanças de recuperar o ideal da separação de apresentação e conteúdo da web.Use uma única folha de estilo para todas as páginas do seu site. Um dos principais benefícios das folhas de estilo é assegurar continuidade visual à medida que o usuário navega no seu site. Sempre use folhas de estilo externas em vez de incorporados (Jnline).
Somente ao referenciar um arquivo externo, você obterá os benefícios de manutenção de poder atualizar a aparência de todo o seu site com uma única alteração. Além disso, puxando definições de estilo para fora de suas páginas, você os torna menores e mais rápidos de baixar.Se você usar uma única folha de estilo para todo o seu site, esse arquivo será um único download de uma vez por todas.
Para cada site, todas as folhas de estilo devem ser projetadas por um único grupo de design central. Essa recomendação existe por dois motivos: primeiro, o design centralizado é a única maneira de garantir um estilo consistente e de aproveitar um dos principais benefícios das folhas de estilo. Segundo, a maioria dos criadores de conteúdo web não são capazes de projetar e escrever boas folhas de estilo.
A experiência com processadores de texto que suportam folhas de estilos indica que a maioria dos autores manuseia mal suas folhas de estilo. Folhas de estilo da web estão em cascata,isto é, a folha de estilo do site é mesclada com a folha de estilo do usuário para criar a apresentação final. Essas diferenças tornam importante que as folhas de estilo sejam projetadas por um especialista que entenda as várias maneiras pelas quais o resultado pode parecer diferente do que está em tela.
Se a usabilidade é a capacidade que um sistema oferece ao usuário de realizar tarefas, é claro que as folhas de estilo -que cuidam da apresentação de uma página -tem influência em sua usabilidade.
e-PWG: Cartilha de Usabilidade do Governo Eletrônico

INCIDÊNCIA EM PROVA: MÉDIA

Vocês já devem conhecer o e-PING (que trata de interoperabilidade) e o e-MAG (que trata de acessibilidade), no entando existe também o e-PWG (Padrões Web em Governo Eletrônico).Ele fornece recomendações de boas práticas na área digital, com o objetivo de aprimorar a comunicação, o fornecimento de informações e serviços prestados por meios eletrônicos pelos órgãos do Governo Federal.
A adoção do e-PWG traz vantagens na gestão de sítios, como a garantia do nível de qualidade, pois possibilita a mensuração de resultados. Fornece também requisitos para a correta contratação da equipe responsável por desenvolver o sítio, diminui o tempo e o custo de desenvolvimento e manutenção das páginas. Além disso, a padronização desses ambientes acelera o processo de adaptação e migração para tecnologias mais modernas.
Pessoal, essa cartilha busca apresentar a usabilidade, mas no contexto do desenvolvimento e manutenção de páginas web do governo eletrônico. Essa cartilha possui recomendações que devem ser observadas, assim como subsídios para testes que podem ser utilizados tanto pela equipe interna do órgão quanto para a contratação ou licitação. A usabilidade é importante em diversos contexto - é de se imaginar que não seria diferente em sítios do governo.
Ela é indispensável para que as informações e serviços prestados pela
Administração Pública
Federal sejam desenvolvidos e mantidos de acordo com as expectativas e necessidades do cidadão e para que este se utilize das informações e serviços de forma plena e satisfatória.Essa cartilha propõe ser um guia na aplicação de usabilidade em sítios do governo de forma clara e descomplicada.
Apesar de serem recomendações voltadas ao desenvolvimento de sítios,
elas servem perfeitamente ao desenvolvimento de qualquer aplicativo desenvolvido pelo governo. Ausabilidade - a facilidade de uso - deve ser observada em todas as interfaces do governo com o cidadão. Pessoal, o mundo evolui rápido e a administração pública deve sempre tentar acompanhar(Ex: aplicativos governamentais mobile).

Nesse contexto, define-se usabilidade como estudo ou aplicação de técnicas que proporcionem a facilidade de uso de um dado objeto (Ex: sítio web). A usabilidade busca assegurar que qualquer pessoa consiga utilizar o sítio e que este funcione da forma esperada. Em suma, a usabilidade tem como objetivos a facilidade de uso, de aprendizado e de memorização de tarefas;produtividade na execução de tarefas; prevenção, visando a redução de erros; e satisfação do indivíduo.
Para a usabilidade, o ponto de partida do desenvolvimento é o usuário. Ele é o termo técnico utilizado em usabilidade para referir-se a cada pessoa que utiliza o objeto em questão por meio de uma interface. No caso, temos o cidadão como usuário e o objeto são as páginas, informações e serviços disponibilizados eletronicamente pelo governo federal. A interface é o meio pelo qual a pessoa intervém, dialoga, modifica o objeto da interação (no caso, um sítio).
Se a interface é fácil de aprender, simples, direta e amigável, a pessoa estará inclinada a usar. Sítios com usabilidade pensam sob o ponto de vista do cidadão. Para tal, deve-se observar alguns pontos:
CIDADÃO

CONTEXTO DE UTILIZAÇÃO

OBJETIVO

É necessário conhecer, entender e trabalhar com as pessoas que representam os atuais e potenciais utilizadores do produto. Níveis de educação, familiaridade com o meio eletrônico e idade são fatores extremamente importantes;
De onde o cidadão acessa, em que ambiente e em que condições. As pessoas estão,
geralmente, ocupadas e querem realizar rapidamente uma tarefa à qual se sentem obrigadas a fazer (Ex: solicitação de algum benefício ou pagamento de qualquer espécie);
As pessoas utilizam os sítios com um objetivo. O sucesso e a satisfação na realização desse objetivo estão diretamente relacionados com o tempo, o número de passos necessários,a possibilidade de prever o que deve ser feito e a necessidade de aprendizado.

Todo projeto deve ter em conta a experiência que o cidadão irá vivenciar nas páginas do sítio.O objetivo da aplicação da usabilidade é que cada pessoa que visite o sítio encontre o que está buscando de maneira simples, e que se sinta à vontade para retornar ao sítio sempre que quiser ou precisar. Pensem comigo: a quem a usabilidade interessa? Sabe-se que a usabilidade é um processo colaborativo e interdisciplinar.
Dessa forma, é importante que todo membro da equipe envolvida com o sítio possua,
pelo menos,
a consciência da necessidade da usabilidade e conheça o básico da sua aplicação. Pode existir um especialista ou a contratação de uma empresa/consultor, mas não deve caber apenas a estes o comprometimento com a usabilidade. A preocupação com a facilidade de utilizar o sítio deve estar presente em diversos aspectos:
Na concepção do sítio e de seus serviços; na programação da aplicação; na criação de funções; no desenho das páginas; na estruturação das informações (arquitetura de informação); na redação das informações. A total utilização e manutenção da usabilidade do sítio é possível apenas quando esta faz parte do conhecimento comum da equipe. Problemas de usabilidade ocorrem quando pessoas encontram dificuldades para realizar algo que precisam fazer ou querem fazer com uma interface.
Tais dificuldades podem ter origens variadas e ocasionar perda de dados,
diminuição da produtividade, a não exploração de seções ou serviços, podendo chegar ao abandono do sítio. Odesenvolvimento de sítios utilizando a usabilidade tem como consequência comum uma redução nos custos e, posteriormente, uma diminuição no número de correções nas funcionalidades do sítio.Sítios e serviços com boa usabilidade requerem menos treinamento, suporte e manutenção.

Uma pergunta boba: vocês sabem a diferença entre usabilidade e acessibilidade? Ambas têm como foco de atenção o usuário (cidadão) e, muitas vezes, se sobrepõe como áreas de saber.No entanto, acessibilidade trata do acesso a locais, produtos, serviços ou informações efetivamente disponíveis ao maior número e variedade possível de pessoas independente de suas capacidades físico-motoras e perceptivas, culturais e sociais, já a usabilidade trata da facilidade de uso.
Um sítio pode ser acessível, mas difícil de ser utilizado; ou ser fácil de ser utilizado, todavia inacessível a parte da população. No entanto, a acessibilidade e usabilidade são disciplinas complementares e é mais provável que um sítio com boa acessibilidade tenha uma boa usabilidade,assim como um sítio com boa usabilidade seja mais acessível. Bacana? Existem também os conceitos de navegabilidade e comunicabilidade.
A navegabilidade é a propriedade ou a capacidade que a interface de um site possui de facilitar ao usuário chegar ao seu destino da maneira mais eficiente possível. Anavegabilidade corresponde à qualidade da estrutura viária que dá acesso ao conteúdo das informações no site. Já a comunicabilidade é a capacidade de os usuários entenderem o design tal como concebido pelos projetistas (designers).
Quando um usuário entende as decisões que o projetista tomou ao construira interface,
aumentam suas chances de fazer um bom uso daquele sistema. Em sistemas com alta comunicabilidade, os usuários são capazes de responder: para que o sistema serve, como funciona, entre outros. A web não respeita limites de tempo e espaço. É um meio de inclusão social, não fazendo juízo de quem a utiliza.
Ao prover um serviço público ou ao fornecer informação por meio eletrônico, devemos lembrar que não existirá um cidadão idêntico ao outro. Em resumo, estamos lidando com pessoas com níveis diferentes de familiaridade com computadores e internet; com níveis diferentes de interesses nos serviços e informações; com diferentes cargas de conhecimento e educação;com idades diversas em momentos diversos da vida; Com características demográficas diversas.
A forma com que as pessoas navegam em um sítio é, quase sempre, bem diferente do que imaginamos. Apenas uma minoria de pessoas entrará no sítio da forma esperada. Apenas uma parcela passará pela página inicial antes de ir para onde deseja. Muitas chegarão ao serviço desejado através de motores de busca por páginas intermediárias. As pessoas exploram as páginas aleatoriamente e clicam na primeira coisa que acham que deve ser o que estavam procurando.
Se não for, utilizam o botão "voltar" do navegador e retornam a página anterior, fazendo isso quantas vezes acharem adequado em busca do que desejam. A partir daí, podem utilizar a caixa de busca, aliás, muitas utilizam a caixa de busca direto - sem se preocupar em ler os menus.Não encontrando o que buscam, podem sair para nunca mais voltar, buscando a forma presencial do serviço, sobrecarregando os outros canais, entre outros.
Em suma: pessoas exploram páginas; não buscam a melhor alternativa; não buscam saber como as coisas funcionam; querem qualidade e credibilidade; seguem sua intuição; e querem ter o controle do que ocorre no sítio. Porfim, não devemos abusarda paciência do cidadão! Quanto menos ações ou campos a serem preenchidos, menor a chance de erros, menor o tempo para concluir um serviço e teremos a certeza de que ele escolherá a web como seu canal de comunicação com o governo.
Vamos ver agora algumas diretrizes recomendadas para desenvolvimento de sítios. Diretrizes devem ser tomadas como ponto de partida no desenvolvimento e teste de sítios, nunca como uma receita ou lista de itens a serem seguidos. Contexto e bom-senso são fundamentais no desenvolvimento de sítios. As diretrizes propostas por esta cartilha baseiam-se na observação concreta de problemas comuns nas páginas de instituições públicas no Brasil. São elas:
Contexto e Navegação
Carga de Informação
Consistência e Familiaridade

DIRETRIZES

Autonomia

Erros
Desenho
Redação

Diretriz í-Contexto e Navegação

A internet é um ambiente não-linear, ou seja, ela não possui um fluxo único. Cada página possui diversas entradas e saídas e o resultado disso é, por muitas vezes, a desorientação de quem utiliza o sítio. Por isso, é importante que o sítio informe à pessoa em que contexto ela se encontra,o que a página faz e demarque claramente a navegação (não apenas a página inicial, mas todas as páginas).
Muitas vezes a pessoa chega a uma página interna do sítio através de uma busca. Ela deve saber de pronto a que sítio aquela página pertence e quais as opções disponíveis. Em resumo o cidadão deve conseguir: rapidamente compreender o que é e como funciona o sítio;facilmente localizar o que busca; realizar os passos do serviço sem dificuldade.
RECOMENDAÇÕES DE CONTEXTO E NAVEGAÇÃO

í.i Página inicial clara.

1.2 Estrutura do sítio lógica e fácil.

1.3 Estruturar a informação de forma lógica e intuitiva para 0 cidadão.

1.4 O conteúdo mais importante antes da dobra.

1.5 Elementos da identidade visual localizados sempre no mesmo lugar.

1.6 A ferramenta de busca presente em todas as páginas
1.7As páginas, seções ou serviços mais utilizados visíveis.

1.8 Não use páginas de transição.

1.9 Documentação, tutorial e ajuda.

1.10 Formatos especiais de arquivo e download.

1.11 Não use janelas pop-up ou abra links em nova janela.

1.12 Busca simples e depois, avançada.

1.13 Resultados da caixa de busca.

1.14 Formulários amigáveis.

Diretriz 2 - Carga de Informação

A carga de informação é a soma de todos os elementos da interface: textos, links, ícones,funcionalidades, cores, etc. Até o menor elemento decorativo adiciona carga de informação. Um ser humano é capaz de absorver um determinado número de informações (memória de curto prazo)
- de forma inconsciente. A partir de certo ponto, o cérebro não processa algumas informações.

Uma carga de informação alta confunde o cidadão. Nestes casos, é mais provável a ocorrência de erros. No caso de serviços, quanto mais numerosas e complexas forem as ações necessárias para se concluir o serviço, maior será a carga de informação e a probabilidade de erros. Em suma, deve-se: reduzir a carga de informação; focar a atenção do cidadão ao objetivo (tarefa) da página ou serviço.
RECOMENDAÇÕES DE CARGA DE INFORMAÇÃO

1.15 Não abarrote a página inicial com excesso de informações.

1.16 Elimine elementos desnecessários das páginas.

1.17 Elimine passos desnecessários em serviços e preenchimento de formulários.

1.18 Em textos extensos, oferecer a opção de baixar o documento.

1.19 Apenas peça os dados necessários.

1.20 Peça para 0 cidadão converter dados, medidas ou valores

1.21 Cidadão não deve necessitar memorizar dados.

1.22 A rolagem vertical ou horizontal de tela.

1.23 O bom senso no número de filtros e opções disponíveis.

Diretriz 3 - Autonomia

Na internet, qualquer tipo de controle (não esperado) vindo do sitio é indesejado. Controlar o tamanho das janelas, utilizar soluções proprietárias,desabilitar funcionalidades de navegadores são práticas que intervém no controle do cidadão. Em suma: o comportamento e as funcionalidades do navegador não devem ser alterados para satisfazer páginas; cidadão deve ter autonomia na utilização do sítio.
RECOMENDAÇÕES DE AUTONOMIA

1.24 Mantenha a função do botão de retrocesso (back/voltar) do navegador.

1.25 Não crie páginas que abram e funcionem em tela cheia.

1.26 Permitirão cidadão marcar(favoritar) qualquer página de seu interesse.

1.27 Não usar expressões como "compatível com" "melhor visto na resolução...".

1.28 Possibilitar ao cidadão interromper ou cancelar o processamento ou transação.

1.29 É do cidadão 0 controle sobre a navegação

1.30 Não usar plug-ins auto-instaláveis.

1.31 Permitir a cópia de trechos de documentos.

1.32 Quando possível, oferecer a personalização da página.

Diretriz 4-Erros

Errar é humano. O cidadão pode não entender como proceder em determinado passo do serviço e cometer erros. Além da correção do erro, é importante dar o retorno ao cidadão, tanto aos seus erros cometidos, quanto aos problemas do sítio. Em suma: falhas ou indisponibilidades previstas devem ser divulgadas e esclarecidas ao cidadão; todo erro cometido pelo cidadão deve ser passível de ser corrigido.
RECOMENDAÇÕES DE ERROS

1.33As ações do portal devem ser reversíveis.

1.34 Permita erros de digitação em busca.

1.35 Avise toda indisponibilidade (Ex: troca de servidores).

1.36 Em formulários, mostre 0 formato desejado.

1.37 Em formulários, só deixe no campo 0 número de caracteres desejado.

1.38 As mensagens de erro devem ser sucintas e explicativas

1.39 Não limpe 0 conteúdo do formulário inteiro porcausa de um erro.

Diretriz 5 - Desenho

Um bom desenho (design, programação visual) tem um impacto significativo na credibilidade e usabilidade do sítio. Ele deve, sobretudo, respeitar o cidadão. Um sítio legível e esteticamente agradável hierarquiza e facilita a decodificação das informações apresentadas, influenciando seu nível de satisfação durante a interação com o portal. Em resumo o desenho deve:
-Trabalhar em favor do cidadão;

- Seguir a função do sítio;

- Auxiliar a compreensão do seu conteúdo;

- Manter a clareza, simplicidade e legibilidade da informação;

- Contribuir para a encontrabilidade dos itens de informação do sítio;

- Garantir a facilidade de navegação.

1.40 Utilizar um projeto padrão de páginas.

RECOMENDAÇÕES DE DESENHO

1.41 Agrupar e hierarquizar, de forma clara, as áreas de informação.

1.42 Usar espaço em branco para separar conteúdos ou assuntos diferentes.

1.43 Usarfundos neutros, que não comprometam o objetivo do sítio.

1.44 Evitar caixa com opções ou de menus de cortina na navegação principal e persistente.

1.45 O desenho deve estar a serviço da informação

1.46 Elementos do desenho não devem trabalhar em benefício de uma estética particular.

1.47 Utilizar a animação com bom senso.

1.48 Conteúdo agradável de ser lido.

1.49 Texto alinhado à esquerda.

1.50 Esquema consistente de cores e fontes.

1.51 Respeitar a velocidade de conexão do público-alvo.

1.52 Utilizar de forma consciente plug-ins e multimídia.

Diretriz 6-Redação

A comunicação em sítios do governo é, sobretudo utilitária, visando prestar serviços e informações aos cidadãos. A redação deve levar em conta a audiência, o conhecimento das pessoas que acessam o sítio. O texto deve ser diagramado para facilitar o entendimento da informação. Em resumo: o sítio deve "falar" a língua das pessoas, com palavras, frases e conceitos familiares; o texto deve ser objetivo.
RECOMENDAÇÕES DE REDAÇÃO

1.53 Utilizar uma linguagem clara e familiar

1.54 O texto objetivo.

1.55 Dividir o texto em tópicos.

1.56 Títulos informativos e com destaque visual.
1.57Título da página explanatório e único.

1.58 Utilizartermos simples e claros como rótulos de menu.

1.59 Gramática correta.

1.60 Use ênfase e negrito.

1.61 Evitar o uso de caixa alta.

Diretriz 7 - Consistência e Familiariadade

O cidadão deve sentir-se bem-vindo ao entrar em um sítio do governo.
O desempenho dos cidadãos de qualquer sistema interativo melhora quando os procedimentos necessários ao cumprimento da tarefa são compatíveis com as suas características psicológicas, culturais e técnicas e quando os procedimentos e as tarefas são organizados de acordo com as expectativas e costumes dos cidadãos.
Em resumo: o cidadão deve sentir-se bem-vindo no sítio; e o sítio deve ser familiar, identificado com a experiência de vida.
1.62 Usar convenções.

RECOMENDAÇÕES DE CONSISTÊNCIA E FAMILIARIADADE

1.63 Usarformato de data e unidades de medida de acordo com 0 padrão utilizado na instituição ou país.
1.64 Planejara estrutura do sítio de acordo com o contexto das tarefas realizadas pelos cidadãos.

1.65 Facilitara navegação do sítio.

1.66 Planejara estrutura do portal de acordo com 0 contexto das tarefas realizadas pelos cidadãos.

1.67 Remeter a formulários os links de contato.

Pessoal, quem quiser saber mais detalhes sobre cada recomendação;
sobre métodos de investigação; sobre os tipos de testes possíveis no ciclo de desenvolvimento;o processo de teste de usabiIidade; protótipos; custos de avaliação de usabilidade; entre outros, recomendo ler a cartilha de usabilidade do governo eletrônico com maior profundidade. Vamos falar um pouquinho agora sobre Métodos de Avaliação.
Cada método de avaliação de interfaces possui uma série de propriedades que fornecem certas vantagens ou desvantagens. Isso inclui, por exemplo, o tempo, o esforço e o nível de habilidade e conhecimento para a utilização do método, facilidades e equipamentos necessários para a condução eficaz do método. Para Jordan (1998), a maioria dos métodos para a avaliação de interfaces envolve a utilização de participantes -tais métodos são conhecidos como empíricos.
Não há algo capaz de substituir a observação de indivíduos tentando utilizar um determinado produto. Os métodos de avaliação também são divididos em métodos de investigação,métodos de inspeção e testes de usuário. Os Métodos de Investigação são usados nas etapas iniciais de projeto e são métodos contextuais para identificar requisitos, obtendo informações através da indagação de pessoas e da observação destes usando o sistema.
São eles: Observações de Campo, Entrevistas, Registro de Uso, Questionários,
Lista de Verificação de Características, Métodos de Avaliação, Workshop de Usuários e Grupos deFoco. Os métodos de inspeção são avaliações baseadas em um conjunto de diretrizes usualmente derivadas de estudos em Interação Humano-Computador e/ou Psicologia Cognitiva. São eles:Percurso Cognitivo,
Avaliação Heurística, Análise de Tarefas, Lista de Verificação de Propriedades,
Inspeção de Padrões e Avaliação de Peritos.
Testes de Usuário são técnicas etnográficas nas quais pessoas interagem com um produto. Podem ser aplicados ao sítio inteiro, em apenas algumas seções, em uma funcionalidade a qualquer momento do desenvolvimento do sítio. São eles: Arranjos de Cartões;Co-Descoberta; Avaliação
Cooperativa; Diário de Incidentes; Experimentos Controlados; Protocolos
"Pensar Alto"; e
Registro de Conversações. Vamos ver métodos de avaliação empíricos de interfaces:

MÉTODOS EMPÍRICOS | DESCRIÇÃO

Utilizado para descobrir o modelo mental que os participantes têm de determinado

ARRANJO DE CARTÕES
(CARD SORTING)

AVALIAÇÃO COOPERATIVA

CO-DESCOBERTA

espaço de informação. Isso gera, dessa forma, a arquitetura da informação de uma interface. É utilizado para entender como os participantes agrupam as informações de acordo com suas relações de característica e significância, isto é, como os indivíduos categorizam o conteúdo de uma interface.
Ocorre na medida que os participantes e os pesquisados avaliam juntos a interface. Os participantes são encorajados a perguntar sobre o processo de interagir com esta interface e o pesquisadorfaz perguntas sobre o entendimento do participante em relação à mesma. Isso faz com que o procedimento pareça bastante natural para o participante e exija menos recursos.
Método que envolve dois participantes que trabalham juntos para explorar uma interface e descobrir como determinadas tarefas são realizadas. Através da análise das verbalizações dos participantes, o pesquisador pode obter um melhor entendimento das questões de usabilidade associadas com a interface - geralmente os participantes são amigos ou, no mínimo, conhecidos.
DIÁRIOS DE INCIDENTES

ENTREVISTAS

GRUPO DE FOCO

EXPERIMENTOS
CONTROLADOS

LISTAS DE VERIFICAÇÃO
DE CARACTERÍSTICAS

MÉTODOS DE AVALIAÇÃO

OBSERVAÇÕES DE CAMPO

WORKSHOP DE USUÁRIOS

PROTOCOLOS"PENSAR

ALTO"

QUESTIONÁRIOS:

São miniquestionários emitidos para os participantes, para que os indivíduos tomem notas de qualquer problema encontrado durante a utilização de uma interface.Tipicamente, solicita-se que estes participantes forneçam uma descrição por escrito do problema que eles encontraram. Então, pergunta-se como resolveriam tal problema e como ele era incômodo.
O pesquisador compila uma série de questões propostas diretamente aos participantes.
É importante ressaltar que há três categorias de entrevistas: sem estrutura (quando não há perguntas preparadas anteriormente para dirigir a discussão), semiestruturadas(quando há algumas perguntas preparadas) e estruturadas (quando todas as perguntas já estão preparadas).
É um grupo de pessoas reunidas para discutir um assunto particular. Esta discussão pode abranger, por exemplo, as experiências dos usuários em relação à utilização de uma interface em particular, os requerimentos para uma nova interface, informações sobre o contexto em que se realiza tarefas específicas, ou problemas de usabilidade que são associados com a utilização de uma interface.
O processo de experimentos controlados é dividido em quatro etapas: uma série de observações controladas; realizadas em uma situação artificial; através da manipulação deliberadas de algumas variáveis; e com o objetivo de testar uma ou mais hipóteses específicas. É uma avaliação formalmente projetada através de controles e balanços muito bem ajustados.
Uma lista de verificação de características nada mais é do que uma lista de funcionalidades de uma interface, ou seja, solicita-se que os participantes marquem as características utilizadas nesta interface. Saberquais as características são usadas e quais não são utilizadas faz com que a lista seja uma forma útil de capturar os requisitos de um produto.
Avalia a importância que os participantes atribuem à determinadas características de uma interface. Geralmente, pergunta-se às pessoas o quanto elas pagariam a mais por uma interface que contenha determinadas características. Considera-se que a quantidade de indivíduos que pagaria por estas essas características seja um indicativo da importância da resolução de problemas.
O método de observações de campo envolve a observação dos participantes no ambiente real em que uma interface é utilizada. Isto promove um grau de validade ambiental que pode ser perdida em avaliações conduzidas em um local um tanto quanto estéril, como um laboratório de usabilidade, por exemplo.
Uma "oficina" de usuários é caracterizada por um grupo de participantes reunidos para discutir assuntos relacionados com o projeto e a utilização da interface. Geralmente, estes participantes são envolvidos na fase de projetação de uma nova interface. Isto significa,simplesmente, listar seus requisitos em termos de usabilidade e funcionalidade.

Este método envolve um participante que fala sobre o que ele está fazendo e pensando ao utilizar uma determinada interface. Pode-se solicitar que este indivíduo realize uma tarefa específica na interface, ou, simplesmente, lhe seja dada a oportunidade de uma livre exploração da interface gráfica.
A função do questionário é estabelecer (obter gradualmente) uma comunicação particular. Espera-se que o respondente possua certas informações, ideias ou atitudes sobre o assunto do inquérito e precisa-se obter tais dados com o mínimo de distorção possível. A maioria dos questionários é classificada como fechado (uma opção entre várias alternativas) ou aberto (não tem alternativas).
REGISTRO DE
CONVERSAÇÕES

REGISTRO DE USO
(LOGGING USE)

Com exceção de pequenas instruções dadas pelo pesquisador no início da avaliação, os procedimentos deste método são realizados inteiramente pelo participante. Consiste basicamente no fato do indivíduo entrarem uma cabine privada e falar, para uma câmera de vídeo, sobre um tópico pré-determinado pelo investigador.
Nas interfaces gráficas digitais, é possível instalar dispositivos de registro automático que captam as interações dos participantes com a interface. Todas as teclas digitadas pelas pessoas podem ser registradas, por exemplo, ou então todos os comandos selecionados a partir de menus. A utilização de um método deste tipo resulta na informação sobre a extensão da interação.
E os métodos não-empíricos, professor? São aqueles métodos que geralmente não utilizam participantes. Vamos ver alguns exemplos:
MÉTODOS NÃO-EMPÍRICOS | DESCRIÇÃO

A medição da complexidade de uma tarefa é feita através do número de passos necessários para completar a mesma. Logo, quanto menos passos, mais simples é a
ANÁLISE DE TAREFA

AVALIAÇÃO HEURÍSTICA

tarefa. O método de análise da tarefa pode ser utilizado para o desenvolvimento de predições sobre o quanto é fácil/difíciI desempenhar uma determinada tarefa, ou quanto esforço é necessário para chegar ao final dela.
Um pequeno grupo de peritos em design de telas examina uma determinada interface e procura dos problemas que violem alguns princípios gerais de projeto. Pede-se que estes peritos avaliem a interface isoladamente, evitando que os achados de um sejam influenciados pelos de outro indivíduo. Posteriormente, comparam-se os resultados.
AVALIAÇÃO DE PERITOS

LISTAS DE VERIFICAÇÃO
DE PROPRIEDADES

PERCURSO COGNITIVO

A interface é avaliada através da opinião de um perito. Neste último caso, os peritos podem trabalhar tanto separadamente quanto em conjunto, para fornecer suas avaliações. O perito, neste contexto, é uma pessoa cujo background o qualifica para a realização de julgamentos sobre os problemas de usabilidade relacionados à interface avaliada.
As listas de verificação apresentam uma série de propriedades de projeto que, de acordo com asteorias do design, da ergonomia e do ergodesign, asseguram que uma interface é fácil de usar. Geralmente, as listas indicam as propriedades de nível elevado para a usabilidade da interface, como da consistência, compatibilidade, padrões, bom feedback,entre outros.

O percurso cognitivo é um método de avaliação da usabilidade realizado por peritos.
Entretanto, existe uma diferença entre a avaliação de peritos,
apresentada anteriormente, e o percurso cognitivo. No segundo, o pesquisador tenta realizara sua avaliação de acordo com o ponto de vista de um usuário típico da interface.
INSPEÇÃO DE PADRÕES

Neste método de avaliação de interface de usuário, a interface é avaliada por um especialista a partir de um determinado padrão previamente escolhido, tal como: e-MAG(Padrão de Acessibilidade do Governo Eletrônico). Avalia-se a conformidade com o que foi preconizado pelo padrão escolhido anteriormente.
RESUMo

USABILIDADE

Trata-se de um atributo de qualidade que avalia o nível de facilidade de uso de uma interface ou a medida de qualidade da experiência de um usuário ao interagir com um produto ou um sistema. Pode também ser definida como a medida em que os usuários podem alcançar seus objetivos de um contexto específico de forma efetiva,eficiente e com satisfação.

Também conhecida como Intuitividade, o sistema deve ser de fácil aprendizado e assimilação,
de forma que um usuário - mesmo sem experiência - possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
O sistema deve ser eficiente no uso, isto é, uma vez que o usuário tenha aprendido o design do sistema, ele deve poder executartarefas com um alto nível de produtividade.
O sistema deve ser fácil de lembrar, para que o usuário seja capaz de retornar depois de um tempo sem ter que aprendertudo novamente.
O sistema deve ter um baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Ademais, erros catastróficos não devem ocorrer.
O sistema deve ser agradável de usar, para que os usuários fiquem satisfeitos e voltem mais vezes para usá-lo.
ANÁLISE DO PERFIL

DO USUÁRIO

ANÁLISE DO CONTEXTO

DA TAREFA

ANÁLISE DAS CAPACIDADES
E RESTRIÇÕES DA PLATAFORMA

ANÁLISE DE PRINCÍPIOS
GERAIS DO PROJETO

Para cada categoria de usuário, projetistas devem conhecer atributos pessoais
(idade, sexo, limitações, motivação) e suas habilidades e competências (na tarefa,
na organização e com sistemas informatizados).

Para cada tarefa a ser apoiada pelo sistema, os projetistas devem conhecer os objetivos e resultados, a estrutura, a duração, as dependências, os custos, a carga mental, as interrupções, os incidentes, entre outros.
Devem ser examinadas as possibilidades e restrições em termos de equipamentos, sistemas operacionais, ambientes de janelas, recursos de rede,entre outros.

Pesquisa e catalogação do conhecimento ergonômico disponível para a concepção da interface no tipo de contexto de uso (usuário, tarefa, equipamento e ambiente) no qual o sistema está inserido.
TÉCNICAS DE ENGENHARIA DE
USABILIDADE DESCONTADA

OBSERVAÇÕES DO
USUÁRIO E DA TAREFA

DESCRIÇÃO

Trata-se da observação de usuários utilizando o sistema para descobrir nível de utilização, desentendimentos, entre outros.
CENÁRIOS DE USO Trata-se de uma espécie de prototipação para obterfeedback sobre a usabilidade do sistema.
VERBALIZAÇÃO SIMPLIFICADA Trata-se de um usuário de teste por vez realizando um conjunto de tarefas no sistema enquanto se pede que ele verbalize o que pensa.
AVALIAÇÕES HEURÍSTICAS Trata-se de avaliações que examinam se uma interface está de acordo com princípios reconhecidos de usabilidade (heurísticas).
PRINCÍPIOS PARA
AVALIAÇÃO DE HEURÍSTICAS

VISIBILIDADE DO STATUS DO

SISTEMA

DESCRIÇÃO

0 sistema deve sempre manter os usuários informados sobre o que está acontecendo, através de feedback apropriado e em tempo razoável.
LIBERDADE E CONTROLE DO

USUÁRIO

PREVENÇÃO CONTRA

ERROS

FLEXIBILIDADE E EFICIÊNCIA DE

UTILIZAÇÃO

AUXILIAR USUÁRIOS A
RECONHECER, DIAGNOSTICAR E

RESOLVER ERROS

COMPATIBILIDADE ENTRE SISTEMA

EO MUNDO REAL

CONSISTÊNCIA E

PADRÕES

RECONHECIMENTO EM LUGAR

DE LEMBRANÇA

PROJETO MINIMALISTA

E ESTÉTICO

Usuários frequentemente escolhem algumas funções do sistema por engano e vão precisar sempre de uma "saída de emergência" claramente marcada para sair daquele estado indesejado sem ter que passar por um extenso "diálogo". Apoio ao desfazer e refazer.
Ainda melhor do que boas mensagens de erro é um projeto cuidadoso que impede que, em primeiro lugar, esse erro possa ocorrer. Eliminando as condições passíveis de erros ou verificá-las, apresentado aos usuários uma opção de confirmação antes de se comprometerem com uma determinada ação.
Aceleradores - invisíveis para o usuário novato - podem frequentemente acelerar a interação para o usuário experiente, que o sistema pode atender a ambos os usuários inexperientes e experientes. Permitir aos usuários personalizar ações frequentes.
Mensagens de erros devem ser expressas em linguagem clara (sem códigos),
indicar com precisão o problema e construtivamente sugerir uma solução.

O sistema deve falar a linguagem dos usuários, com palavras, frases e conceitos familiares ao usuário, ao invés de termos orientados ao sistema. Siga convenções do mundo real, tornando as informações que aparecem em uma ordem natural e lógica.
Os usuários não precisam adivinhar que diferentes palavras, situações ou ações significam a mesma coisa. Siga as convenções da plataforma e mantenha a previsibilidade do sistema.
Minimizar a carga de memória do usuário tornando objetos, ações e opções visíveis. O usuário não deve ter que se lembrar da informação de uma parte do diálogo para outra. Instruções de uso do sistema devem estar visíveis e serem facilmente recuperáveis quando necessário.
Os diálogos não devem conter informações irrelevantes ou raramente necessárias. Cada unidade extra de informação em um diálogo compete com as unidades relevantes de informação e diminui sua visibilidade relativa.
AJUDA E
DOCUMENTAÇÃO

Mesmo que seja melhor que um sistema possa ser usado sem documentação,
pode ser necessário fornecer uma ajuda e documentação. Qualquer informação deve serfácil de ser pesquisada, com foco na atividade do usuário, lista de concretos a serem realizados, e não ser muito grande.
ESTRUTURAS DE
NAVEGAÇÃO

DESCRIÇÃO

LINEAR Os usuários só podem navegar sequencialmente, de uma tela para outra, ou de um campo de informação para 0 outro.
HIERÁRQUICO Os usuários navegam ao longo das ramificações de uma estrutura do tipo árvore que é formada pela lógica natural do assunto.
NÃO-LINEAR Os usuários podem navegar livremente através do conteúdo da aplicação multimídia, sem qualquer restrição.
COMPOSTO Os usuários navegam livremente, mas existem situações com restrições lineares ou hierárquicas, porexemplo.
RECOMENDAÇÕES DE CONTEXTO E NAVEGAÇÃO

í.i Página inicial clara.

1.2 Estrutura do sítio lógica e fácil.

1.3 Estruturar a informação de forma lógica e intuitiva para 0 cidadão.

1.4 O conteúdo mais importante antes da dobra.

1.5 Elementos da identidade visual localizados sempre no mesmo lugar.

1.6 A ferramenta de busca presente em todas as páginas
1.7As páginas, seções ou serviços mais utilizados visíveis.

1.8 Não use páginas de transição.

1.9 Documentação, tutorial e ajuda.

1.10 Formatos especiais de arquivo e download.

1.11 Não use janelas pop-up ou abra links em nova janela.

1.12 Busca simples e depois, avançada.

1.13 Resultados da caixa de busca.

1.14 Formulários amigáveis.

RECOMENDAÇÕES DE CARGA DE INFORMAÇÃO

1.15 Não abarrote a página inicial com excesso de informações.

1.16 Elimine elementos desnecessários das páginas.

1.17 Elimine passos desnecessários em serviços e preenchimento de formulários.

1.18 Em textos extensos, oferecer a opção de baixar o documento.

1.19 Apenas peça os dados necessários.

1.20 Peça para 0 cidadão converter dados, medidas ou valores

1.21 Cidadão não deve necessitar memorizar dados.

1.22 A rolagem vertical ou horizontal de tela.

1.23 O bom senso no número de filtros e opções disponíveis.

RECOMENDAÇÕES DE AUTONOMIA

1.24 Mantenha a função do botão de retrocesso (back/voltar) do navegador.

1.25 Não crie páginas que abram e funcionem em tela cheia.

1.26 Permitirão cidadão marcar(favoritar) qualquer página de seu interesse.

1.27 Não usar expressões como "compatível com" "melhor visto na resolução...".

1.28 Possibilitar ao cidadão interromper ou cancelar o processamento ou transação.

1.29 É do cidadão 0 controle sobre a navegação

1.30 Não usar plug-ins auto-instaláveis.

1.31 Permitir a cópia de trechos de documentos.

1.32 Quando possível, oferecer a personalização da página.

RECOMENDAÇÕES DE ERROS

1.33As ações do portal devem ser reversíveis.

1.34 Permita erros de digitação em busca.

1.35 Avise toda indisponibilidade (Ex: troca de servidores).

1.36 Em formulários, mostre 0 formato desejado.

1.37 Em formulários, só deixe no campo o número de caracteres desejado.

1.38 As mensagens de erro devem ser sucintas e explicativas

1.39 Não limpe 0 conteúdo do formulário inteiro por causa de um erro.

1.40 Utilizar um projeto padrão de páginas.

RECOMENDAÇÕES DE DESENHO

1.41 Agrupar e hierarquizar, de forma clara, as áreas de informação.

1.42 Usar espaço em branco para separar conteúdos ou assuntos diferentes.

1.43 Usarfundos neutros, que não comprometam 0 objetivo do sítio.

1.44 Evitar caixa com opções ou de menus de cortina na navegação principal e persistente.

1.45 O desenho deve estar a serviço da informação

1.46 Elementos do desenho não devem trabalhar em benefício de uma estética particular.

1.47 Utilizar a animação com bom senso.

1.48 Conteúdo agradável de ser lido.

1.49 Texto alinhado à esquerda.

1.50 Esquema consistente de cores e fontes.

1.51 Respeitar a velocidade de conexão do público-alvo.

1.52 Utilizar de forma consciente plug-ins e multimídia.

RECOMENDAÇÕES DE REDAÇÃO

1.53 Utilizar uma linguagem clara e familiar

1.54 O texto objetivo.

1.55 Dividir o texto em tópicos.

1.56 Títulos informativos e com destaque visual.
1.57Título da página explanatório e único.

1.58 Utilizartermos simples e claros como rótulos de menu.

1.59 Gramática correta.

1.60 Use ênfase e negrito.

1.61 Evitar o uso de caixa alta.

1.62 Usar convenções.

RECOMENDAÇÕES DE CONSISTÊNCIA E FAMILIARIADADE

1.63 Usarformato de data e unidades de medida de acordo com 0 padrão utilizado na instituição ou país.
1.64 Planejara estrutura do sítio de acordo com o contexto das tarefas realizadas pelos cidadãos.

1.65 Facilitara navegação do sítio.

1.66 Planejara estrutura do portal de acordo com 0 contexto das tarefas realizadas pelos cidadãos.

1.67 Remeter a formulários os links de contato.

MÉTODOS EMPÍRICOS | DESCRIÇÃO

Utilizado para descobrir o modelo mental que os participantes têm de

ARRANJO DE CARTÕES
(CARD SORTING)

AVALIAÇÃO COOPERATIVA

CO-DESCOBERTA

DIÁRIOS DE INCIDENTES

ENTREVISTAS

GRUPO DE FOCO

EXPERIMENTOS
CONTROLADOS

determinado espaço de informação. Isso gera, dessa forma, a arquitetura da informação de uma interface. É utilizado para entender como os participantes agrupam as informações de acordo com suas relações de característica e significância, isto é, como os indivíduos categorizam o conteúdo de uma interface.
Ocorre na medida que os participantes e os pesquisados avaliam juntos a interface. Os participantes são encorajados a perguntar sobre o processo de interagir com esta interface e o pesquisadorfaz perguntas sobre o entendimento do participante em relação à mesma. Isso faz com que o procedimento pareça bastante natural para o participante e exija menos recursos.
Método que envolve dois participantes que trabalham juntos para explorar uma interface e descobrir como determinadas tarefas são realizadas. Através da análise das verbalizações dos participantes, o pesquisador pode obter um melhor entendimento das questões de usabilidade associadas com a interface -geralmente os participantes são amigos ou, no mínimo, conhecidos.

São miniquestionários emitidos para os participantes, para que os indivíduos tomem notas de qualquer problema encontrado durante a utilização de uma interface. Tipicamente, solicita-se que estes participantes forneçam uma descrição por escrito do problema que eles encontraram. Então, pergunta-se como resolveriam tal problema e como ele era incômodo.
O pesquisador compila uma série de questões propostas diretamente aos participantes. É importante ressaltar que há três categorias de entrevistas: sem estrutura (quando não há perguntas preparadas anteriormente para dirigir a discussão), semiestruturadas (quando há algumas perguntas preparadas) e estruturadas (quando todas as perguntas já estão preparadas).
É um grupo de pessoas reunidas para discutir um assunto particular. Esta discussão pode abranger, por exemplo, as experiências dos usuários em relação à utilização de uma interface em particular, os requerimentos para uma nova interface, informações sobre o contexto em que se realiza tarefas específicas, ou problemas de usabilidade que são associados com a utilização de uma interface.
O processo de experimentos controlados é dividido em quatro etapas: uma série de observações controladas; realizadas em uma situação artificial; através da manipulação deliberadas de algumas variáveis; e com o objetivo de testar uma ou mais hipóteses específicas. É uma avaliação formalmente projetada através de controles e balanços muito bem ajustados.
LISTAS DE VERIFICAÇÃO
DE CARACTERÍSTICAS

MÉTODOS DE AVALIAÇÃO

OBSERVAÇÕES DE CAMPO

WORKSHOP DE USUÁRIOS

PROTOCOLOS"PENSAR

ALTO"

QUESTIONÁRIOS:

REGISTRO DE
CONVERSAÇÕES

REGISTRO DE USO
(LOGGING USE)

Uma lista de verificação de características nada mais é do que uma lista de funcionalidades de uma interface, ou seja, solicita-se que os participantes marquem as características utilizadas nesta interface. Saber quais as características são usadas e quais não são utilizadas faz com que a lista seja uma forma útil de capturar os requisitos de um produto.
Avalia a importância que os participantes atribuem à determinadas características de uma interface. Geralmente, pergunta-se às pessoas o quanto elas pagariam a mais por uma interface que contenha determinadas características. Considera-se que a quantidade de indivíduos que pagaria por estas essas características seja um indicativo da importância da resolução de problemas.
O método de observações de campo envolve a observação dos participantes no ambiente real em que uma interface é utilizada. Isto promove um grau de validade ambiental que pode ser perdida em avaliações conduzidas em um local um tanto quanto estéril, como um laboratório de usabilidade, por exemplo.
Uma "oficina" de usuários é caracterizada por um grupo de participantes reunidos para discutir assuntos relacionados com o projeto e a utilização da interface.Geralmente, estes participantes são envolvidos na fase de projetação de uma nova interface. Isto significa, simplesmente, listar seus requisitos em termos de usabilidade e funcionalidade.
Este método envolve um participante que fala sobre o que ele está fazendo e pensando ao utilizar uma determinada interface. Pode-se solicitar que este indivíduo realize uma tarefa específica na interface, ou, simplesmente, lhe seja dada a oportunidade de uma livre exploração da interface gráfica.
A função do questionário é estabelecer (obter gradualmente) uma comunicação particular. Espera-se que o respondente possua certas informações, ideias ou atitudes sobre o assunto do inquérito e precisa-se obtertais dados com o mínimo de distorção possível. A maioria dos questionários é classificada como fechado(uma opção entre várias alternativas) ou aberto (não tem alternativas).

Com exceção de pequenas instruções dadas pelo pesquisador no início da avaliação, os procedimentos deste método são realizados inteiramente pelo participante. Consiste basicamente no fato do indivíduo entrar em uma cabine privada e falar, para uma câmera de vídeo, sobre um tópico pré-determinado pelo investigador.
Nas interfaces gráficas digitais, é possível instalar dispositivos de registro automático que captam as interações dos participantes com a interface. Todas as teclas digitadas pelas pessoas podem ser registradas, por exemplo, ou então todos os comandos selecionados a partir de menus. A utilização de um método deste tipo resulta na informação sobre a extensão da interação.
MÉTODOS NÃO-EMPÍRICOS | DESCRIÇÃO

A medição da complexidade de uma tarefa é feita através do número de passos

ANÁLISE DE TAREFA

necessários para completar a mesma. Logo, quanto menos passos, mais simples é a tarefa. O método de análise da tarefa pode ser utilizado para o desenvolvimento
AVALIAÇÃO HEURÍSTICA

AVALIAÇÃO DE PERITOS

LISTAS DE VERIFICAÇÃO
DE PROPRIEDADES

PERCURSO COGNITIVO

INSPEÇÃO DE PADRÕES

de predições sobre o quanto é fácil/difíciI desempenhar uma determinada tarefa,
ou quanto esforço é necessário para chegar ao final dela.

Um pequeno grupo de peritos em design de telas examina uma determinada interface e procura dos problemas que violem alguns princípios gerais de projeto.Pede-se que estes peritos avaliem a interface isoladamente, evitando que os achados de um sejam influenciados pelos de outro indivíduo. Posteriormente,comparam-se os resultados.

A interface é avaliada através da opinião de um perito. Neste último caso,
os peritos podem trabalhartanto separadamente quanto em conjunto, para fornecer suas avaliações. O perito, neste contexto, é uma pessoa cujo background o qualifica para a realização de julgamentos sobre os problemas de usabilidade relacionados à interface avaliada.
As listas de verificação apresentam uma série de propriedades de projeto que, de acordo com as teorias do design, da ergonomia e do ergodesign, asseguram que uma interface é fácil de usar. Geralmente, as listas indicam as propriedades de nível elevado para a usabilidade da interface, como da consistência,compatibilidade, padrões, bom feedback, entre outros.

O percurso cognitivo é um método de avaliação da usabilidade realizado por peritos. Entretanto, existe uma diferença entre a avaliação de peritos,apresentada anteriormente, e o percurso cognitivo. No segundo, o pesquisador tenta realizar a sua avaliação de acordo com o ponto de vista de um usuário típico da interface.
Neste método de avaliação de interface de usuário, a interface é avaliada por um especialista a partir de um determinado padrão previamente escolhido, tal como:e-MAG (Padrão de Acessibilidade do Governo Eletrônico). Avalia-se a conformidade com o que foi preconizado pelo padrão escolhido anteriormente.
D PARA MAIS DICAS: WWW.INSTAGRAM.COM/PROFESSORDIEGOCARVALHO

QUESTõES CoMENTADoS - CESPE

í. (CESPE / BANRISUL - 2022) A arquitetura da informação estuda a operação de uma interface de usuário para avaliar se está assegurado o correto funcionamento e o entendimento dos conteúdos com a apresentação eficiente e atrativa das informações.
Comentários:

Quem estuda a operação de uma interface de usuário é a usabilidade - a arquitetura da informação estuda como organizar, estruturar e apresentar conteúdo de maneira que seja intuitiva e fácil de usar para os usuários. Em outras palavras, a arquitetura da informação trata da estrutura/organização das informações e a usabilidade trata da melhor forma de projetar sistemas para melhorar o uso do usuário.
Gabarito: Errado

2. (CESPE / BANRISUL - 2022) A acessibilidade está relacionada à facilidade com que determinada informação é assimilada por pessoas com alguma deficiência.
Comentários:

A acessibilidade se refere à capacidade de alguém de acessar e entender informações,independentemente de suas habilidades físicas, mentais ou socioeconômicas.
É importante que as informações sejam fáceis de ler e compreender, para que as pessoas com deficiência possam usufruir do conteúdo. Isso pode incluir a utilização de recursos como áudio,vídeo, imagens e texto para tornar a informação mais acessível.
Gabarito: Correto

3. (CESPE/ DPE-RO-2021) Durante a utilização do sistema, existe uma sensibilidade ao contexto e, em vez de inúmeras opções, é indicado apenas o que se deve fazer como próximo passo válido; assim, o usuário pode inferir o que o sistema espera que seja feito em seguida.
Sabendo que, na engenharia de usabilidade, devem ser observados alguns princípios do projeto de interação, assinale a opção que indica o princípio do projeto de interação abordado no texto precedente.
a) consistência.

b) restrições.

c) feedback (retorno).

d) visibilidade.

e) mapeamento.

Comentários:

O mapeamento significa a relação entre o controle e o efeito, ou seja,
com um bom design, os controles se aparentam bastante com os seus efeitos. Um bom exemplo é uma barra de rolagem vertical de uma página: é intuitivo ver que - se arrastamos a barra para baixo - a página irá rolar para baixo; e se arrastarmos para cima, a página irá rolar para cima. Abarra de rolagem não tem diversas funções, apenas aquilo que ela deve fazer.
Gabarito: Letra E

4. (CESPE/TCU -2005) Uma estrutura linear de navegação para uma aplicação em ambiente web deve ser utilizada quando a aplicação for caracterizada por uma sequência previsível de interações, com poucas variantes de fluxos de navegação.
Comentários:

ESTRUTURAS DE
NAVEGAÇÃO

DESCRIÇÃO

LINEAR Os usuários só podem navegar sequencialmente, de uma tela para outra, ou de um campo de informação para 0 outro.
HIERÁRQUICO Os usuários navegam ao longo das ramificações de uma estrutura do tipo árvore que é formada pela lógica natural do assunto.
NÃO-LINEAR Os usuários podem navegar livremente através do conteúdo da aplicação multimídia, sem qualquer restrição.
COMPOSTO Os usuários navegam livremente, mas existem situações com restrições lineares ou hierárquicas, por exemplo.
Trata-se da estrutura de navegação linear, isto é, sequência previsível de interações, com poucas variantes de fluxo de navegação.
Gabarito: Correto

5. (CESPE / TCU - 2005) No projeto da interface usuário de um sistema,
a quantidade de ações,
tarefas e estados do sistema indicados no modelo da interface permite prever a carga de memória dos usuários desse sistema.
Comentários:

Quanto mais ações, tarefas e estados, maiora carga de informações que o usuárioterá que guardar.Logo, é possível prever essa carga de memória dos usuários baseado nesses critérios. Recomenda-se projetar bem a interface com o usuário para reduzir a carga de memória do usuário.

Gabarito: Correto

6. (CESPE / TCU - 2005) A variabilidade do tempo de resposta de um sistema tem pouca importância para o desempenho médio do usuário na realização de tarefas com esse sistema.
Comentários:

Recomenda-se que o sistema seja efetivo, no sentido de dar respostas pelo menos razoavelmente rápidas para as ações dos usuários - dentro de certos limites de tempo.Atrasos excessivos podem ser irritantes, interromper a concentração, causar preocupação no usuário e prejudicar a produtividade, à medida que limitações na memória dos usuários começam a ser desafiadas. Logo,a variabilidade do tempo de resposta de um sistema tem bastante importância para o desempenho médio do usuário na realização de tarefas.
Gabarito: Errado

7. (CESPE / TRE-MS - 2013) A engenharia da usabilidade é embasada no uso das técnicas de:

a) avaliações heurísticas e cenários de uso.

b) helps online e call center.

c) observação do usuário e helps online.

d) cenários de uso e informações na tela do sistema.

e) verbalização simplificada e helps online.

Comentários:

TÉCNICAS DE ENGENHARIA DE
USABILIDADE DESCONTADA

OBSERVAÇÕES DO
USUÁRIO E DA TAREFA

CENÁRIOS DE USO
VERBALIZAÇÃO SIMPLIFICADA
AVALIAÇÕES HEURÍSTICAS

DESCRIÇÃO

Trata-se da observação de usuários utilizando o sistema para descobrir nível de uti I ização, desentendimentos# entre outros.
Trata-se de uma espécie de prototipação para obterfeedback sobre a usabilidade do sistema.
Trata-se de um usuário de teste por vez realizando um conjunto de tarefas no sistema enquanto se pede que ele verbalize o que pensa.
Trata-se de avaliações que examinam se uma interface está de acordo com princípios reconhecidos de usabilidade (heurísticas).
A tabela nos mostra que se trata de cenários de uso e avaliações heurísticas.

Gabarito: Letra A

8. (CESPE / CNJ - 2013) Uma página desenvolvida em conformidade com as normas sintáticas deJavascript, Java ou PHPterá necessariamente usabilidade de boa qualidade, bem como de boa acessibilidade.
Comentários:

Seguir as normas de sintaxe de linguagem de programação não credencia página alguma a ter boa usabilidade. Não há nenhuma relação entre esses aspectos - são utilizadas outras técnicas para garantir boa usabilidade.
Gabarito: Errado

9. (CESPE / CNJ - 2013) Se o preenchimento de um formulário cadastral de um sistema ocasiona cinco erros, em média, e esses erros representam um esforço de uma hora para correção, então,nessa situação, infere-se que não foi utilizada adequadamente a engenharia de usabilidade durante a fase de desenvolvimento.
Comentários:

Também conhecida como Intuitividade, 0 sistema deve ser de fácil aprendizado e assimilação,
de forma que um usuário - mesmo sem experiência - possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
O sistema deve ser eficiente no uso, isto é, uma vez que 0 usuário tenha aprendido 0 design do sistema, ele deve poder executar tarefas com um alto nível de produtividade.
O sistema deve ser fácil de lembrar, para que 0 usuário seja capaz de retornar depois de um tempo sem ter que aprender tudo novamente.
O sistema deve ter um baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Ademais, erros catastróficos não devem ocorrer.
O sistema deve ser agradável de usar, para que os usuários fiquem satisfeitos e voltem mais vezes para usá-lo.
Para avaliar se esse formulário segue as regras adequadas de engenharia de usabilidade, podemos utilizar o critério de erros, isto é, o sistema deve ter baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Não é o que parece acontecer pelo que foi informado na questão, logo infere-se que não foi utilizada adequadamente a engenharia de usabilidade durante a fase de desenvolvimento.
Gabarito: Correto io.(CESPE / CNJ - 2013) A usabilidade consiste em extrair informações a respeito de quando o sistema não suporta a carga aplicada, sendo importante para estruturar e dimensionar a arquitetura e prover informações para escalar o sistema.
Comentários:

Problemas de arquitetura ou escalabilidade não fazem parte do rol de responsabilidades da engenharia de usabilidade. A questão não faz o menor sentido; talvez estaria correta se estivesse falando sobre testes de carga.
Gabarito: Errado

11. (CESPE / UNIPAMPA - 2013) Utilidade é considerada um atributo-chave que deve ser pensado de forma paralela com a usabilidade.
Comentários:

Perfeito! A utilidade realmente deve ser pensada de forma paralela com a usabilidade. Uma interface que provê utilidade é aquela que fornece as características de que você necessita. Ausabilidade diz quão fáceis e prazerosas essas características são de usar. Uma interface útil é aquela que une utilidade e usabilidade!
Gabarito: Correto

12.(CESPE / UNIPAMPA - 2013) A usabilidade deve ser acompanhada necessariamente de avaliações.
Comentários:

Para julgar se a usabilidade é adequada ou não, é necessário realizar avaliações. Utilizam-se metodologias para medir os aspectos de usabilidade da interface de um sistema e identificar problemas específicos. O processo de avaliação de usabilidade inclui atividades como: captura, que coleta dados de usabilidade, tempo de execução, erros, etc; análise, que interpreta os dados para identificar problemas; e crítica, que sugere soluções e melhorias.
Gabarito: Correto

13. (CESPE / HEMOBRÁS - 2013) De acordo com Jakob Nielsen, a usabilidade tornou-se popular entre as empresas que a utilizam websites devido ao retorno financeiro que ela pode proporcionar.
Comentários:

A usabilidade evita perdas e proporciona Return On Investment (ROI),
isto é, retorno financeiro gerando lucros. Uma interface usável oferece vantagem competitiva, mais lucro (ROI) e menos custos de manutenção
Gabarito: Correto iZf.(CESPE / HEMOBRÁS - 2008) Entre os princípios de usabilidade descritos por Nielsen está o uso de uma linguagem familiar ao usuário.
Comentários:

COMPATIBILIDADE ENTRE SISTEMA

EO MUNDO REAL

O sistema deve falar a linguagem dos usuários, com palavras, frases e conceitos familiares ao usuário, ao invés de termos orientados ao sistema. Siga convenções do mundo real, tornando as informações que aparecem em uma ordem natural e lógica.
Perfeito! O sistema deve falar a linguagem dos usuários, com palavras, frases e conceitos familiares ao usuário, ao invés de termos orientados ao sistema.
Gabarito: Correto i5.(CESPE / HEMOBRÁS - 2008) De acordo com Jakob Nielsen, para melhorar a usabilidade de um sistema, o designer deve avaliar outras interfaces existentes.
Comentários:

TÉCNICAS DE ENGENHARIA DE
USABILIDADE DESCONTADA

OBSERVAÇÕES DO
USUÁRIO E DA TAREFA

CENÁRIOS DE USO
VERBALIZAÇÃO SIMPLIFICADA
AVALIAÇÕES HEURÍSTICAS

DESCRIÇÃO

Trata-se da observação de usuários utilizando o sistema para descobrir nível de uti I ização, desentendimentos# entre outros.
Trata-se de uma espécie de prototipação para obterfeedback sobre a usabilidade do sistema.
Trata-se de um usuário de teste por vez realizando um conjunto de tarefas no sistema enquanto se pede que ele verbalize o que pensa.
Trata-se de avaliações que examinam se uma interface está de acordo com princípios reconhecidos de usabilidade (heurísticas).
Por meio de avaliações heurísticas de interfaces, é possível examinar se uma interface está de acordo com princípios reconhecidos de usabilidade.
Gabarito: Correto i6.(CESPE/ SERPRO-2008) De acordo com Jakob Nielsen, um dos cinco atributos da usabilidade é a facilidade com que o sistema é lembrado.
Comentários:

Também conhecida como Intuitividade, 0 sistema deve ser de fácil aprendizado e assimilação,de forma que um usuário - mesmo sem experiência - possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
O sistema deve ser eficiente no uso, isto é, uma vez que 0 usuário tenha aprendido 0 design do sistema, ele deve poder executar tarefas com um alto nível de produtividade.
O sistema deve ser fácil de lembrar, para que 0 usuário seja capaz de retornar depois de um tempo sem ter que aprender tudo novamente.
O sistema deve ter um baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Ademais, erros catastróficos não devem ocorrer.
O sistema deve ser agradável de usar, para que os usuários fiquem satisfeitos e voltem mais vezes para usá-lo.
A questão trata do critério de memorização, isto é, o sistema deve ser fácil de lembrar, para que o usuário seja capaz de retornar depois de um tempo sem ter que aprendertudo novamente.
Gabarito: Correto i7.(CESPE / SERPRO - 2008) O grau de usabilidade de um sistema de informação independe do grau de integração do usuário no processo de design do sistema.
Comentários:

De acordo com esse item, o usuário não interfere ou influencia no processo de design do sistema -isso não faz nenhum sentido!

Gabarito: Errado i8.(CESPE / TCU - 2005) Segundo a norma ISO 9241, um produto pode ter níveis significativamente diferentes de usabilidade quando usado em diferentes contextos.
Comentários:

A Norma ISO/IEC 9241-11 define usabiIidade como medida na qual um produto pode ser usado por usuários específicos para alcançar objetivos específicos com eficácia, eficiência e satisfação em um contexto específico de uso. Logo, o nível de usabilidade dependerá do contexto!
Gabarito: Correto ig.(CESPE / TCU - 2005) Os atributos eficácia, eficiência e satisfação dos usuários definidos na norma ISO 9241 são atributos diretamente mensuráveis e verificáveis.
Comentários:

A Norma ISO/IEC 9241-11 define usabilidade como medida na qual um produto pode ser usado por usuários específicos para alcançar objetivos específicos com eficácia, eficiência e satisfação em um contexto específico de uso. A Norma lembra que a usabilidade é dependente do contexto de uso e 0nível alcançado dependerá das circunstâncias específicas nas quais o produto é usado.

Eficácia, eficiência e satisfação realmente são atributos definidos na norma!
No entanto, não é possível mensurar satisfação porque é algo muito subjetivo. Cada usuário pode dar uma opinião diferente sobre a usabilidade de uma interface.
Gabarito: Errado

2o.(CESPE / ABIN - 2010) As técnicas de avaliação de usabilidade experimentais ou empíricas contam com a participação direta dos usuários e compreendem, basicamente, os testes com usuários por meio do monitoramento de sessões de uso do produto, ou protótipo, em consideração. Em geral, ostestes de usabilidade com a participação dos usuários são avaliações confiáveis.
Comentários:

A participação de usuários potenciais realmente torna as avaliações mais confiáveis! Deve-se fazer os testes de usabilidade com os potenciais usuários para chegar a uma avaliação é mais confiável!
Gabarito: Correto

2i.(CESPE / PCF - 2004) Considere que se deseja desenvolver um sistema para controle de caixa de supermercado tendo como base um computador que registra os produtos vendidos,interagindo com dispositivos de entrada e saída tais como impressora, teclado e leitora de código de barras. Esse sistema deve interagirtambém com o operadordo caixa e com um banco de dados do estabelecimento. A facilidade de uso é uma das funções mais importantes do sistema.
Comentários:

Nunca entendi por que essa questão está errada! O máximo que eu consigo elucubrar é que a facilidade de uso é uma das funções mais importantes da interface do usuário e, não,do sistema.
Ainda assim, discordo da banca e a considero o item correto!:(

Gabarito: Errado

22.(CESPE / SEFAZ-AL - 2002) A utilização de recursos visuais na interface de um sistema não é suficiente para garantir níveis adequados de facilidade de uso.
Comentários:

Utilizar recursos visuais na interface não suficiente! Há que se atentar para todos aqueles fatores:erros, facilidade de aprendizado, memorização, eficiência e satisfação.

Gabarito: Correto

23. (CESPE / SEFAZ-AL - 2002) Técnicas de inteligência artificial podem ser usadas para permitir que um sistema adapte-se automaticamente ao usuário, aumentando a facilidade de uso para este usuário.
Comentários:

A Inteligência Artificial realmente pode ser usada para permitir que um sistema se adapte aos seus usuários automaticamente.
Gabarito: Correto

24.(CESPE / TCU - 2010) Vantagem competitiva e redução de custos de manutenção estão entre os benefícios mensuráveis que podem ser obtidos de um sistema usável.
Comentários:

Pressman afirma: "Entre os muitos benefícios mensuráveis derivados de um sistema usável.
estão 0
aumento de vendas e a satisfação do usuário, vantagem competitiva, melhores opiniões na mídia,melhores comentários, custos de manutenção reduzidos, produtividade do usuário final melhorada,custos de treinamento reduzidos, custos de documentação reduzidos, probabilidade reduzida de litígio por clientes insatisfeitos".
Logo, a vantagem competitiva e redução de custos de manutenção realmente estão entre os benefícios mensuráveis que podem ser obtidos de um sistema usável.
Gabarito: Correto

25. (CESPE / TCU - 2010) Identificar categorias e definir os objetivos de teste para cada categoria são recomendações normalmente consideradas para a elaboração de teste de usabilidade.
Comentários:

Roger Pressman adota outra sequência de atividades para realizar testes de usabilidade em aplicações web: (1) definir categorias de testes de usabilidade e identificar cada objetivo; (2)projetar testes que possibilitam que cada objetivo possa ser avaliado; (3) selecionar participantes que irão conduzir os testes de usabilidade; (4) dar instrumentos para a interação dos participantes com a aplicação; (5) desenvolver um mecanismo para avaliar a usabilidade na aplicação.
Gabarito: Correto

26.(CESPE / TCU - 2010) Se um sistema é utilizável com instrução ou ajuda contínua,
então há usabilidade nesse sistema.
Comentários:

Se o sistema é usável com instrução ou ajuda contínua, então não há usabilidade! Já pensou se, para tudo que 0 usuário quiser fazer, ele precisar abrir um manual? Isso é um indício de que há carência de usabilidade!
Gabarito: Errado

27. (CESPE/TCU-2010) Uma questão do tipo A interação é simples? jamais deve ser utilizada para determinar se a usabilidade foi atingida em um sistema.
Comentários:

Deve ser utilizada, sim! Trata-se de uma pergunta básica que deve ser feita para questionar se há,ou não, usabilidade em um sistema. Deve-se perguntar: O sistema é usável sem ajuda ou instrução contínua? As regras de interação ajudam um usuário bem informado sobre como 0 sistema funciona eficientemente? A interação é simples?
Gabarito: Errado

28.(CESPE / ECT - 2011) A engenharia da usabilidade é aplicada em qualquer tipo de interface,como, por exemplo, sítios web, software e desktop. Uma das principais fases da engenharia de usabilidade é a que permite o conhecimento do usuário ao qual o software se destina.
Comentários:

ANÁLISE DO PERFIL

DO USUÁRIO

ANÁLISE DO CONTEXTO

DA TAREFA

ANÁLISE DAS CAPACIDADES
E RESTRIÇÕES DA PLATAFORMA

ANÁLISE DE PRINCÍPIOS
GERAIS DO PROJETO

Para cada categoria de usuário, projetistas devem conhecer atributos pessoais
(idade, sexo, limitações, motivação) e suas habilidades e competências (na tarefa,
na organização e com sistemas informatizados).

Para cada tarefa a ser apoiada pelo sistema, os projetistas devem conhecer os objetivos e resultados, a estrutura, a duração, as dependências, os custos, a carga mental, as interrupções, os incidentes, entre outros.
Devem ser examinadas as possibilidades e restrições em termos de equipamentos, sistemas operacionais, ambientes de janelas, recursos de rede,entre outros.

Pesquisa e catalogação do conhecimento ergonômico disponível para a concepção da interface no tipo de contexto de uso (usuário, tarefa, equipamento e ambiente) no qual o sistema está inserido.
De fato, ela é aplicada a diversos tipos de interface (web, desktop, mobile, etc) -
sendo que uma das principais fases da engenharia de usabilidade é a análise do perfil do usuário para conhecer melhor o usuário ao qual o software se destina.
Gabarito: Correto

QUESTõES CoMENTADoS - FCC

í. (FCC / TCE-PR-2011) A terminologia e os conceitos aplicados em uma interface de usuário que afetam o design da interface estão associados ao fator:
a) experiência com o computador.

b) experiência de domínio.

c) frequência de uso.

d) motivação.

e) treinamento.

Comentários:

BAIXA ALTA

EXPERIÊNCIA
COMO USUÁRIO

EXPERIÊNCIA
COMO DOMÍNIO

TREINAMENTO
FREQUÊNCIA DE

_ _ _ _ _ _ _ USO

MOTIVAÇÃO

Pergunta e resposta simples,
preenchimento de formulário simples, estilo de interface web (com hyperlinks) ou de menus.
Terminologia e conceitos usuais.

Foco na facilidade de aprendizagem
(consistente, previsível, memorável).

Fácil de aprender e lembrar, estilo de interface simples.
Uso recompensado, poderoso sem parecer complexo.
Preenchimento de formulário complexo, estilo de interface web (com hyperlinks) ou de menus(pergunta/resposta ou preenchimento de formulário simples seria muito frustrante para usuários experientes).
Terminologia e conceitos específicos ao domínio.

Foco na facilidade de uso (direto, personalizável, não intrusivo).
Fácil de usar, vários atalhos e técnicas para permitir o controle pelo usuário.
Sofisticado com muitas características avançadas e personalizáveis.
A questão trata do fator: Experiência Com o Domínio. Questão puramente decoreba :(

Gabarito: Letra B

2. (FCC / TCE-PR-2011) O sistema deve apresentar facilidade de uso, permitindo que mesmo um usuário sem experiência seja capaz de produzir algum trabalho satisfatoriamente. Trata-se de um critério básico de usabilidade denominado:
a) eficiência.

b) memorização.

c) satisfação.

d) intuitividade.

e) erro.

Comentários:

Também conhecida como Intuitividade, o sistema deve serde fácil aprendizado e assimilação,de forma que um usuário - mesmo sem experiência - possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
O sistema deve ser eficiente no uso, isto é, uma vez que o usuário tenha aprendido o design do sistema, ele deve poder executartarefas com um alto nível de produtividade.
O sistema deve ser fácil de lembrar, para que o usuário seja capaz de retornar depois de um tempo sem terque aprendertudo novamente.
0 sistema deve ter um baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Ademais, erros catastróficos não devem ocorrer.
O sistema deve ser agradável de usar, para que os usuários fiquem satisfeitos e voltem mais vezes para usá-lo.
A questão trata-se da facilidade de aprendizado (intuitividade)! O sistema deve ser de fácil aprendizado e assimilação, de forma que um usuário - mesmo sem experiência- possa rapidamente obter algum resultado satisfatório.
Gabarito: Letra D

3. (FCC / TJ-PE - 2012) Para que ocorra minimamente uma interação, a interface deve apresentar características que facilitem sua utilização, permitindo que usuários básicos ou avançados possam aprender seus recursos de forma clara e objetiva. Segundo Jacob Nielsen, entre os atributos que compõe a usabilidade este é o mais importante e está associado a:
a) eficiência.

b) memorização.

c) satisfação.

d) erros.

e) intuitividade.

Comentários:

CRITÉRIOS DE
QUALIDADE
LEARNABILITY

(FACILIDADE DE

APRENDIZADO)

DESCRIÇÃO

Também conhecida como Intuitividade, o sistema deve serde fácil aprendizado e assimilação,de forma que um usuário - mesmo sem experiência - possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
EFFICIENCY
(EFICIÊNCIA)

MEMORABILITY
(MEMORIZAÇÃO!

SATISFACTION
(SATISFAÇÃO]

O sistema deve ser eficiente no uso, isto é, uma vez que o usuário tenha aprendido o design do sistema, ele deve poder executartarefas com um alto nível de produtividade.
O sistema deve ser fácil de lembrar, para que o usuário seja capaz de retornar depois de um tempo sem terque aprendertudo novamente.
O sistema deve ter um baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Ademais, erros catastróficos não devem ocorrer.
O sistema deve ser agradável de usar, para que os usuários fiquem satisfeitos e voltem mais vezes para usá-lo.
A questão trata-se da facilidade de aprendizado (intuitividade)! O sistema deve ser de fácil aprendizado e assimilação, de forma que um usuário - mesmo sem experiência- possa rapidamente obter algum resultado satisfatório.
Gabarito: Letra E

4. (FCC/TRT6-2012) Em relação ao desenho (design, programação visual), que tem um impacto significativo na credibilidade e usabilidade de um site, é correto afirmar:
a) A função do site e a informação, devem ser soberanas sobre o desenho.
Qualquer tipo de conformação que beneficie o desenho em detrimento da informação,usabilidade e funcionalidade do site deve ser abandonada.
b) O fundo deve chamar mais atenção do que a informação, desde que seja relacionado ao tema do site. Um fundo de impacto imprime uma personalidade diferenciada ao site.
c) Não se deve usar espaço em branco para separar conteúdos ou assuntos diferentes.
Devem-
se usar linhas grossas para permitir uma percepção melhor da separação de conteúdo.

d) Todos os tipos de informação devem ser disponibilizados em uma longa lista sem mecanismos de classificação, pois o usuário pode localizar a informação desejada por meio da opção de busca do navegador.
e) Utilizar um projeto padrão de páginas passa a não ser necessário, uma vez que o usuário possui, porexperiência, contato com uma grande diversidade de sites com diferentes desenhos.
Comentários:

RECOMENDAÇÕES DE DESENHO

1.40 Utilizar um projeto padrão de páginas (Letra E).

1.41 Agrupar e hierarquizar, de forma clara, as áreas de informação (Letra D).

1.42 Usar espaço em branco para separar conteúdos ou assuntos diferentes (Letra C).

1.43 Usar fundos neutros, que não comprometam 0 objetivo do sítio (Letra B).

1.44 Evitar caixa com opções ou de menus de cortina na navegação principal e persistente.

1.45 O desenho deve estar a serviço da informação.

1.46 Elementos do desenho não devem trabalhar em benefício de uma estética particular.

1.47 Utilizar a animação com bom senso.

1.48 Conteúdo agradável de ser lido.

1.49 Texto alinhado à esquerda.

1.50 Esquema consistente de cores e fontes.

1.51 Respeitar a velocidade de conexão do público-alvo.

1.52 Utilizarde forma consciente plug-ins e multimídia.

A função do sítio-a informação-é soberana sobre o desenho. Qualquertipo de conformação que beneficie o desenho em detrimento a informação, usabilidade e funcionalidade do sítio deve ser abandonada.
Gabarito: Letra A

31. (FCC / TRT6 - 2012) NÃO consta entre as diretrizes de usabilidade em Governo Eletrônico:

a) Contexto e navegação - é importante que o site informe a pessoa em que contexto ela se encontra, o que a página faz e demarque claramente a navegação.
b) Carga de informação - Uma carga de informação alta e diversificada confunde o usuário.Nestes casos, é mais provável a ocorrência de erros.

c) Autonomia - Na Internet qualquer tipo de controle (não esperado) vindo por parte do site é indesejado.
d) Erros - O usuário pode não entender como proceder em determinado passo do serviço e cometer erros. Além da correção do erro, é importante dar o retorno devido ao usuário, tanto dos erros cometidos por ele, quanto dos problemas momentâneos do site.
e) Documentação - O usuário deve ter acesso a um manual impresso que descreva passo-a-passo a forma correta de navegação no site e as tecnologias utilizadas na sua construção, assim como cada um dos recursos disponíveis.
Comentários:

Contexto e Navegação (Letra A)
Carga de Informação (Letra B)
Consistência e Familiaridade

DIRETRIZES

Erros (Letra D)
Desenho
Redação

Autonomia (Letra C)

Não existe a diretriz Documentação. E, mesmo que você não soubesse disso, não faz sentido algum dizer que o usuário deve ter um manual impresso. Além disso, não faz sentido dizer ao usuário as tecnologias utilizadas na construção da página - isso deve ser transparente para o usuário.
Gabarito: Letra E

32.(FCC / TCE-CE - 2015) As avaliações de usabilidade permitem a concepção de interfaces que atendam as expectativas e necessidades dos usuários além de garantir melhores decisões de projeto e evitar custos de correções tardias. Os métodos de avaliação podem ser divididos emMétodos de investigação, Métodos de inspeção e Teste com usuários. São
Métodos de inspeção: Percurso Cognitivo (Cognitive Walkthrought)
a) Avaliação Cooperativa e Diário de Incidentes.

b) Avaliação Heurística e Inspeção de padrões.

c) Arranjo de Cartões (card-sorting) e Inspeção de padrões.

d) Arranjo de Cartões (card-sorting) e Avaliação Cooperativa.

e) Co-descoberta e Diário de Incidentes.

Comentários:

Os métodos de inspeção são avaliações baseadas em um conjunto de diretrizes usualmente derivadas de estudos em Interação Humano-Computador e/ou Psicologia Cognitiva.São eles:
Percurso Cognitivo, Avaliação Heurística, Análise de Tarefas, Lista de Verificação de
Propriedades,
Inspeção de Padrões e Avaliação de Peritos.

Gabarito: Letra B

QUESTõES CoMENTADoS - FCV

í. (FGV / Senado Federal - 2008) A usabilidade consiste num conjunto de técnicas que aferem:

a) a relação entre a configuração de uma interface de informação e a eficácia e a satisfação do usuário na sua utilização.
b) a relação entre o design de um equipamento de informática e a fadiga do usuário na sua utilização.
c) a relação entre a beleza de uma interface e a emoção do usuário na sua utilização.

d) a relação entre os usuários num ambiente de rede interativo.

e) a duração (tempo de vida útil) de um equipamento de informática antes que se torne obsoleto tecnologicamente.
Comentários:

A usabilidade se refere à medida em que os usuários podem alcançarseus objetivos de um contexto específico de forma efetiva, eficiente e com satisfação - nenhum dos outros itens faz qualquer sentido lógico.
Gabarito: Letra A

2. (FGV / ALERJ - 2017) O Antiquário "Só Velharia" possui um sistema de catálogo de produtos,desenvolvido há três anos, que é utilizado por todos os seus funcionários. Há cerca de um ano,devido à crise no país, a empresa teve que demitir alguns funcionários. Recentemente a
"Só
Velharia" conseguiu fechar um convênio com alguns investidores para retornar sua produtividade normal. Assim, a empresa decidiu recontratar alguns de seus antigos funcionários. Em relação ao sistema, a empresa acredita que não precisará readaptar esses funcionários. O critério básico da engenharia de usabilidade que garantirá que esses funcionários não necessitarão de novo treinamento no sistema, mesmo após um ano sem utilizá-lo, é:
a) memorização b) satisfação c) erro d) criatividade e) eficiência
Comentários:

Também conhecida como Intuitividade, o sistema deve serde fácil aprendizado e assimilação,de forma que um usuário - mesmo sem experiência - possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
O sistema deve ser eficiente no uso, isto é, uma vez que o usuário tenha aprendido o design do sistema, ele deve poder executartarefas com um alto nível de produtividade.
O sistema deve ser fácil de lembrar, para que o usuário seja capaz de retornar depois de um tempo sem terque aprendertudo novamente.
0 sistema deve ter um baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Ademais, erros catastróficos não devem ocorrer.
0 sistema deve ser agradável de usar, para que os usuários fiquem satisfeitos e voltem mais vezes para usá-lo.
A questão trata do critério de memorização: o sistema deve serfácil de lembrar, para que o usuário seja capaz de retornar depois de um tempo sem ter que aprendertudo novamente.
Gabarito: Letra A

3. (FGV / IBGE - 2016) Atualmente, existem vários métodos de avaliação de usabilidade, alguns analisando as ações dos usuários finais, outros que dependem apenas de especialistas.Para avaliar um usuário de cada vez, encorajando-o a verbalizar as dificuldades encontradas, o webdesigner deverá trabalhar com:
a) grupo de foco;

b) avaliação heurística;

c) análise do especialista;

d) avaliação cooperativa;

e) walkthrough heurístico.

Comentários:

MÉTODOS EMPÍRICOS | DESCRIÇÃO

Ocorre na medida que os participantes e os pesquisados avaliam juntos a interface. Os participantes são encorajados a perguntar sobre 0 processo de interagir com esta
AVALIAÇÃO COOPERATIVA

interface e 0 pesquisadorfaz perguntas sobre 0 entendimento do participante em relação à mesma. Isso faz com que 0 procedimento pareça bastante natural para 0 participante e exija menos recursos.
A questão trata da Avaliação Cooperativa.

Gabarito: Letra D

QUESTõES CoMENTADoS - DIvERSAS BANCAS

í. (ESAF / TCU - 2002) Se um programa não for amigável ao usuário (user friendliness)freqüentemente estará destinado ao fracasso, mesmo que as funções que ele execute sejam valiosas. A usabilidade é a forma de se quantificar este fator e pode ser medida segundo quatro características. Uma destas características é a(o):
a) facilidade com que o programa pode ser corrigido se um erro for encontrado.

b) grau de corretitude com que o software executa a função que é dele exigida.

c) habilidade física e/ou intelectual exigida para se aprender o sistema.

d) medida onde um defeito é definido como uma falta verificada de conformidade aos requisitos.
e) custo para se corrigir defeitos encontrados depois que o software foi liberado para o usuário final.
Comentários:

Também conhecida como Intuitividade, 0 sistema deve serde fácil aprendizado e assimilação,de forma que um usuário - mesmo sem experiência - possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
O sistema deve ser eficiente no uso, isto é, uma vez que 0 usuário tenha aprendido 0 design do sistema, ele deve poder executartarefas com um alto nível de produtividade.
O sistema deve ser fácil de lembrar, para que 0 usuário seja capaz de retornar depois de um tempo sem terque aprendertudo novamente.
O sistema deve ter um baixo índice de erros, e se existirem devem permitir uma recuperação rápida e fácil. Ademais, erros catastróficos não devem ocorrer.
O sistema deve ser agradável de usar, para que os usuários fiquem satisfeitos e voltem mais vezes para usá-lo.
A questão trata da facilidade de aprendizado (ou intuitividade). O sistema deve ser de fácil aprendizado e assimilação, de forma que um usuário - mesmo sem experiência- possa rapidamente obter algum resultado satisfatório. Trata-se do atributo mais importante de acordo com Jakob Nielsen.
i. (ESAF/CVM -2oio) No ciclo da Engenharia da Usabilidade, as atividades da fase de análise são:
a) Análise da instituição do usuário. Análise do contexto da tarefa. Análise das possibilidades e restrições do treinamento. Análise de princípios setoriais para o projeto.
b) Análise do perfil do usuário. Análise do contexto da plataforma. Análise de compatibilidade gerencial. Análise de princípios gerais para o projeto.
c) Análise do perfil do usuário. Análise do contexto da tarefa. Análise das possibilidades e restrições da plataforma. Análise de princípios gerais para o projeto.
d) Análise do perfil do desenvolvedor. Análise de requisitos. Análise das possibilidades e sistemas da plataforma. Análise de princípios gerais para as transações.
e) Análise da instituição do usuário. Análise de compromissos. Análise das possibilidades e restrições da estrutura. Análise de ameaças à segurança do projeto.
Comentários:

ANÁLISE DO PERFIL

DO USUÁRIO

ANÁLISE DO CONTEXTO

DA TAREFA

ANÁLISE DAS CAPACIDADES
E RESTRIÇÕES DA PLATAFORMA

ANÁLISE DE PRINCÍPIOS
GERAIS DO PROJETO

Para cada categoria de usuário, projetistas devem conhecer atributos pessoais
(idade, sexo, limitações, motivação) e suas habilidades e competências (na tarefa,
na organização e com sistemas informatizados).

Para cada tarefa a ser apoiada pelo sistema, os projetistas devem conhecer os objetivos e resultados, a estrutura, a duração, as dependências, os custos, a carga mental, as interrupções, os incidentes, entre outros.
Devem ser examinadas as possibilidades e restrições em termos de equipamentos, sistemas operacionais, ambientes de janelas, recursos de rede,entre outros.

Pesquisa e catalogação do conhecimento ergonômico disponível para a concepção da interface no tipo de contexto de uso (usuário, tarefa, equipamento e ambiente) no qual o sistema está inserido.
As atividades da análise são: análise do perfil do usuário; análise do contexto da tarefa; análise das possibilidades e restrições da plataforma; e análise de princípios gerais para o projeto.
Gabarito: Letra C

3. (ESAF / CVM - 2010) São heurísticas de usabilidade:

a) Coerência e padrões. Prevenção de erros. Relembrar em vez de Reconhecer.
Flexibilidade e eficiência de mapeamento. Ajuda e documentação.
b) Visibilidade do estado do sistema. Mapeamento entre o sistema e o mundo real.
Liberdade e
Controle ao Usuário. Prevenção de erros. Reconhecer em vez de relembrar.

c) Versatilidade do estado do sistema. Previsão de acertos. Reconhecer em vez de relembrar.Design estético e maximalista. Suporte para o usuário reconhecer, diagnosticar e recuperar erros.
d) Mapeamento entre o sistema e os programas. Liberdade e Controle ao
Desenvolvedor.
Consistência e padrões. Flexibilidade e eficiência de uso. Ajuda e informação.

e) Visibilidade da estrutura do sistema. Compromisso entre o sistema e a configuração.Liberdade e Controle ao Usuário. Suporte para o usuário reconhecer,
diagnosticar e aplicar erros. Ajuda à implementação.
Comentários:

PRINCÍPIOS PARA
AVALIAÇÃO DE HEURÍSTICAS

VISIBILIDADE DO STATUS DO

SISTEMA

DESCRIÇÃO

O sistema deve sempre manter os usuários informados sobre o que está acontecendo, através de feedback apropriado e em tempo razoável.
LIBERDADE E CONTROLE DO

USUÁRIO

PREVENÇÃO CONTRA ERROS

COMPATIBILIDADE ENTRE SISTEMA

EO MUNDO REAL

Usuários frequentemente escolhem algumas funções do sistema por engano e vão precisar sempre de uma "saída de emergência" claramente marcada para sair daquele estado indesejado sem ter que passar por um extenso "diálogo". Apoio ao desfazer e refazer.
Ainda melhordo que boas mensagens de erro é um projeto cuidadoso que impede que, em primeiro lugar, esse erro possa ocorrer. Eliminando as condições passíveis de erros ou verificá-las, apresentado aos usuários uma opção de confirmação antes de se comprometerem com uma determinada ação.
O sistema deve falar a linguagem dos usuários, com palavras, frases e conceitos familiares ao usuário, ao invés de termos orientados ao sistema. Siga convenções do mundo real, tornando as informações que aparecem em uma ordem natural e lógica.
RECONHECIMENTO EM LUGAR DE

LEMBRANÇA

Minimizar a carga de memória do usuário tornando objetos, ações e opções visíveis. O usuário não deve ter que se lembrar da informação de uma parte do diálogo para outra. Instruções de uso do sistema devem estar visíveis e serem facilmente recuperáveis quando necessário.
São heurísticas de usabilidade: visibilidade do estado do sistema; mapeamento entre o sistema e o mundo real; liberdade e controle ao usuário; prevenção de erros; e reconhecer em vez de relembrar.
Gabarito: Letra B

4- (CESGRANRIO / BACEN - 2009) Uma empresa, contratada para desenvolver uma aplicação standalone de análise financeira, deve utilizar um manual de orientações para construção da interface gráfica dessa aplicação. De acordo com as heurísticas de Nielsen, qual é a orientaçãoINCORRETA apresentada nesse manual?

a) Um mesmo comando deve provocar efeitos distintos, de acordo com o nível do usuário.

b) Os usuários devem ser informados sobre o que estão fazendo, com feedback imediato.

c) Os diálogos devem conter somente informações relevantes e necessárias.

d) A terminologia deve ser baseada na linguagem do usuário e não orientada ao sistema.

e) A interface deve ter convenções que não sejam ambíguas.

Comentários:

Vamos pensar um pouco: será que é recomendável que em um manual, um mesmo conteúdo provoque efeitos distintos de acordo com 0 nível do usuário? Jamais, deve provocar os mesmos efeitos,independentemente do nível do usuário!

Gabarito: Letra A

5. (CESGRANRIO / PETROBRÁS - 2008) Assinale a opção que NÃO expressa um princípio de projeto de interface com o usuário.
a) Reduzira demanda de memória de curto prazo do usuário.

b) Basear o layout visual em uma metáfora do mundo real.

c) Permitir que a interação com o usuário seja interruptível e possa ser desfeita (undo).

d) Estabelecer defaults (para escolhas e preenchimento de formulários) que façam sentido para o usuário.
e) Mostrar informações completas a priori, permitindo que o usuário reduza o nível de detalhe se desejar.
Comentários:

Nós já vimos que deve ser mostrado apenas o que é necessário e, se o usuário desejar mais informações, ele deve buscá-las.
Gabarito: Letra E

6. (QUADRIX/ CFP-2012) Com relação às recomendações de usabilidade em websites, é correto afirmar que:
a) janelas pop-up devem sempre ser utilizadas porque são acessíveis aos deficientes visuais e fornecem informações úteis antes mesmo de o usuário pedir.
b) documentos para download devem ser sempre disponibilizados em formatos especiais ou proprietários.
c) páginas de transição, de abertura (splash-pages) ou "em construção" devem ser usadas para melhorara navegação.
d) elementos comuns a todas as páginas, como logotipos, atalhos e caixas de busca,
não devem estar sempre na mesma posição nas páginas do site para não cansar o usuário visualmente.
e) o comportamento e as funcionalidades do navegador não devem ser alterados para satisfazer necessidades especiais das páginas, pois o usuário deve ter autonomia na utilização do site.
Comentários:

RECOMENDAÇÕES DE CONTEXTO E NAVEGAÇÃO

í.i Página inicial clara.

1.2 Estrutura do sítio lógica e fácil.

1.3 Estruturar a informação de forma lógica e intuitiva para 0 cidadão.

1.4 O conteúdo mais importante antes da dobra.

1.5 Elementos da identidade visual localizados sempre no mesmo lugar.

1.6 A ferramenta de busca presente em todas as páginas.

1.7 As páginas, seções ou serviços mais utilizados visíveis.

1.8 Não use páginas de transição.

1.9 Documentação, tutorial e ajuda.

1.10 Formatos especiais de arquivo e download.

1.11 Não use janelas pop-up ou abra links em nova janela.

1.12 Busca simples e depois, avançada.

1.13 Resultados da caixa de busca.

1.14 Formulários amigáveis.

O comportamento e as funcionalidades do navegador não devem ser alterados para satisfazer necessidades especiais das páginas, pois o usuário deve ter autonomia na utilização do site.
Gabarito: Letra E

LISTA DE QUESTõES - CESPE

í. (CESPE / BANRISUL - 2022) A arquitetura da informação estuda a operação de uma interface de usuário para avaliar se está assegurado o correto funcionamento e o entendimento dos conteúdos com a apresentação eficiente e atrativa das informações.
2. (CESPE / BANRISUL - 2022) A acessibilidade está relacionada à facilidade com que determinada informação é assimilada por pessoas com alguma deficiência.
3. (CESPE/ DPE-RO-2021) Durante a utilização do sistema, existe uma sensibilidade ao contexto e, em vez de inúmeras opções, é indicado apenas o que se deve fazer como próximo passo válido; assim, o usuário pode inferir o que o sistema espera que seja feito em seguida.
Sabendo que, na engenharia de usabilidade, devem ser observados alguns princípios do projeto de interação, assinale a opção que indica o princípio do projeto de interação abordado no texto precedente.
a) consistência.

b) restrições.

c) feedback (retorno).

d) visibilidade.

e) mapeamento.

4. (CESPE/TCU-2005) Uma estrutura linear de navegação para uma aplicação em ambiente web deve ser utilizada quando a aplicação for caracterizada por uma sequência previsível de interações, com poucas variantes de fluxos de navegação.
5. (CESPE / TCU - 2005) No projeto da interface usuário de um sistema, a quantidade de ações,tarefas e estados do sistema indicados no modelo da interface permite prever a carga de memória dos usuários desse sistema.
6. (CESPE / TCU - 2005) A variabilidade do tempo de resposta de um sistema tem pouca importância para o desempenho médio do usuário na realização de tarefas com esse sistema.
7. (CESPE /TRE-MS - 2013) A engenharia da usabilidade é embasada no uso das técnicas de:

a) avaliações heurísticas e cenários de uso.

b) helps online e call center.

c) observação do usuário e helps online.

d) cenários de uso e informações na tela do sistema.

e) verbalização simplificada e helps online.

8. (CESPE / CNJ - 2013) Uma página desenvolvida em conformidade com as normas sintáticas deJavascript, Java ou PHP terá necessariamente usabilidade de boa qualidade, bem como de boa acessibilidade.
9. (CESPE / CNJ - 2013) Se o preenchimento de um formulário cadastral de um sistema ocasiona cinco erros, em média, e esses erros representam um esforço de uma hora para correção, então,nessa situação, infere-se que não foi utilizada adequadamente a engenharia de usabilidade durante a fase de desenvolvimento.
10. (CESPE / CNJ - 2013) A usabilidade consiste em extrair informações a respeito de quando o sistema não suporta a carga aplicada, sendo importante para estruturar e dimensionar a arquitetura e prover informações para escalar o sistema.
11. (CESPE / UNIPAMPA - 2013) Utilidade é considerada um atributo-chave que deve ser pensado de forma paralela com a usabilidade.
12. (CESPE / UNIPAMPA - 2013) A usabilidade deve ser acompanhada necessariamente de avaliações.
13. (CESPE / HEMOBRÁS - 2013) De acordo com Jakob Nielsen, a usabilidade tornou-se popular entre as empresas que a utilizam websites devido ao retorno financeiro que ela pode proporcionar.
14. (CESPE / HEMOBRÁS - 2008) Entre os princípios de usabilidade descritos por Nielsen está o uso de uma linguagem familiar ao usuário.
15. (CESPE / HEMOBRÁS - 2008) De acordo com Jakob Nielsen, para melhorar a usabilidade de um sistema, o designer deve avaliar outras interfaces existentes.
16. (CESPE/SERPRO-2oo8) De acordo com Jakob Nielsen, um dos cinco atributos da usabilidade é a facilidade com que o sistema é lembrado.
17. (CESPE / SERPRO - 2008) O grau de usabilidade de um sistema de informação independe do grau de integração do usuário no processo de design do sistema.
18. (CESPE / TCU - 2005) Segundo a norma ISO 9241, um produto pode ter níveis significativamente diferentes de usabilidade quando usado em diferentes contextos.
19. (CESPE / TCU - 2005) Os atributos eficácia, eficiência e satisfação dos usuários definidos na norma ISO 9241 são atributos diretamente mensuráveis e verificáveis.
20.(CESPE / ABIN - 2010) As técnicas de avaliação de usabilidade experimentais ou empíricas contam com a participação direta dos usuários e compreendem, basicamente, os testes com usuários por meio do monitoramento de sessões de uso do produto, ou protótipo, em consideração. Em geral, ostestes de usabilidade com a participação dos usuários são avaliações confiáveis.
2i.(CESPE / PCF - 2004) Considere que se deseja desenvolver um sistema para controle de caixa de supermercado tendo como base um computador que registra os produtos vendidos,interagindo com dispositivos de entrada e saída tais como impressora, teclado e leitora de código de barras. Esse sistema deve interagirtambém com o operador do caixa e com um banco de dados do estabelecimento. A facilidade de uso é uma das funções mais importantes do sistema.
22. (CESPE / SEFAZ-AL - 2002) A utilização de recursos visuais na interface de um sistema não é suficiente para garantir níveis adequados de facilidade de uso.
23. (CESPE / SEFAZ-AL - 2002) Técnicas de inteligência artificial podem ser usadas para permitir que um sistema adapte-se automaticamente ao usuário, aumentando a facilidade de uso para este usuário.
24. (CESPE / TCU - 2010) Vantagem competitiva e redução de custos de manutenção estão entre os benefícios mensuráveis que podem ser obtidos de um sistema usável.
25. (CESPE / TCU - 2010) Identificar categorias e definir os objetivos de teste para cada categoria são recomendações normalmente consideradas para a elaboração de teste de usabilidade.
26. (CESPE / TCU - 2010) Se um sistema é utilizável com instrução ou ajuda contínua,
então há usabilidade nesse sistema.
27. (CESPE/TCU -2010) Uma questão do tipo A interação é simples? jamais deve ser utilizada para determinar se a usabilidade foi atingida em um sistema.
28. (CESPE / ECT - 2011) A engenharia da usabilidade é aplicada em qualquer tipo de interface,como, por exemplo, sítios web, software e desktop. Uma das principais fases da engenharia de usabilidade é a que permite o conhecimento do usuário ao qual o software se destina.
GABARITo

1. ERRADO li. CORRETO
21. ERRADO

2. CORRETO 12. CORRETO
22. CORRETO

3- LETRA E 13- CORRETO
23. CORRETO

4- CORRETO 14- CORRETO
24. CORRETO

5- CORRETO 15- CORRETO 25-
CORRETO

6. ERRADO i6. CORRETO
26. ERRADO

7- LETRA A 17- ERRADO
27- ERRADO

8. ERRADO i8. CORRETO
28. CORRETO

9- CORRETO 19- ERRADO

10. ERRADO 20. CORRETO

LISTA DE QUESTõES - FCC

í. (FCC / TCE-PR-2011) A terminologia e os conceitos aplicados em uma interface de usuário que afetam o design da interface estão associados ao fator:
a) experiência com o computador.

b) experiência de domínio.

c) frequência de uso.

d) motivação.

e) treinamento.

2. (FCC /TCE-PR- 2011) O sistema deve apresentarfacilidade de uso, permitindo que mesmo um usuário sem experiência seja capaz de produzir algum trabalho satisfatoriamente. Trata-se de um critério básico de usabilidade denominado:
a) eficiência.

b) memorização.

c) satisfação.

d) intuitividade.

e) erro.

3. (FCC / TJ-PE - 2012) Para que ocorra minimamente uma interação, a interface deve apresentar características que facilitem sua utilização, permitindo que usuários básicos ou avançados possam aprender seus recursos de forma clara e objetiva. Segundo Jacob Nielsen, entre os atributos que compõe a usabilidade este é o mais importante e está associado a:
a) eficiência.

b) memorização.

c) satisfação.

d) erros.

e) intuitividade.

4. (FCC /TRT6 - 2012) Em relação ao desenho (design, programação visual), que tem um impacto significativo na credibilidade e usabilidade de um site, é correto afirmar:
a) A função do site e a informação, devem ser soberanas sobre o desenho.
Qualquer tipo de conformação que beneficie o desenho em detrimento da informação,usabilidade e funcionalidade do site deve ser abandonada.
b) O fundo deve chamar mais atenção do que a informação, desde que seja relacionado ao tema do site. Um fundo de impacto imprime uma personalidade diferenciada ao site.
c) Não se deve usar espaço em branco para separar conteúdos ou assuntos diferentes.
Devem-
se usar linhas grossas para permitir uma percepção melhor da separação de conteúdo.

d) Todos os tipos de informação devem ser disponibilizados em uma longa lista sem mecanismos de classificação, pois o usuário pode localizar a informação desejada por meio da opção de busca do navegador.
e) Utilizar um projeto padrão de páginas passa a não ser necessário, uma vez que o usuário possui, por experiência, contato com uma grande diversidade de sites com diferentes desenhos.
5. (FCC / TRT6 - 2012) NÃO consta entre as diretrizes de usabilidade em Governo Eletrônico:

a) Contexto e navegação - é importante que o site informe a pessoa em que contexto ela se encontra, o que a página faz e demarque claramente a navegação.
b) Carga de informação - Uma carga de informação alta e diversificada confunde o usuário.Nestes casos, é mais provável a ocorrência de erros.

c) Autonomia - Na Internet qualquer tipo de controle (não esperado) vindo por parte do site é indesejado.
d) Erros - O usuário pode não entender como proceder em determinado passo do serviço e cometer erros. Além da correção do erro, é importante dar o retorno devido ao usuário, tanto dos erros cometidos por ele, quanto dos problemas momentâneos do site.
e) Documentação - O usuário deve ter acesso a um manual impresso que descreva passo-a-passo a forma correta de navegação no site e as tecnologias utilizadas na sua construção, assim como cada um dos recursos disponíveis.
6. (FCC / TCE-CE - 2015) As avaliações de usabilidade permitem a concepção de interfaces que atendam as expectativas e necessidades dos usuários além de garantir melhores decisões de projeto e evitar custos de correções tardias. Os métodos de avaliação podem ser divididos emMétodos de investigação, Métodos de inspeção e Teste com usuários. São
Métodos de inspeção: Percurso Cognitivo (Cognitive Walkthrought)
a) Avaliação Cooperativa e Diário de Incidentes.

b) Avaliação Heurística e Inspeção de padrões.

c) Arranjo de Cartões (card-sorting) e Inspeção de padrões.

d) Arranjo de Cartões (card-sorting) e Avaliação Cooperativa.

e) Co-descoberta e Diário de Incidentes.

GABARITo

1. LETRA B

2. LETRA D

3. LETRA E

4. LETRA A

5. LETRA E

6. LETRA B

LISTA DE QUESTõES - FC V

í. (FGV / Senado Federal - 2008) A usabilidade consiste num conjunto de técnicas que aferem:

a) a relação entre a configuração de uma interface de informação e a eficácia e a satisfação do usuário na sua utilização.
b) a relação entre o design de um equipamento de informática e a fadiga do usuário na sua utilização.
c) a relação entre a beleza de uma interface e a emoção do usuário na sua utilização.

d) a relação entre os usuários num ambiente de rede interativo.

e) a duração (tempo de vida útil) de um equipamento de informática antes que se torne obsoleto tecnologicamente.
2. (FGV / ALERJ - 2017) O Antiquário "Só Velharia" possui um sistema de catálogo de produtos,desenvolvido há três anos, que é utilizado por todos os seus funcionários. Há cerca de um ano,devido à crise no país, a empresa teve que demitir alguns funcionários. Recentemente a
"Só
Velharia" conseguiu fechar um convênio com alguns investidores para retornar sua produtividade normal. Assim, a empresa decidiu recontratar alguns de seus antigos funcionários. Em relação ao sistema, a empresa acredita que não precisará readaptar esses funcionários. O critério básico da engenharia de usabilidade que garantirá que esses funcionários não necessitarão de novo treinamento no sistema, mesmo após um ano sem utilizá-lo, é:
a) memorização b) satisfação c) erro d) criatividade e) eficiência
3. (FGV / IBGE - 2016) Atualmente, existem vários métodos de avaliação de usabilidade, alguns analisando as ações dos usuários finais, outros que dependem apenas de especialistas.Para avaliar um usuário de cada vez, encorajando-o a verbalizar as dificuldades encontradas, o webdesigner deverá trabalhar com:
a) grupo de foco;

b) avaliação heurística;

c) análise do especialista;

d) avaliação cooperativa;

e) walkthrough heurístico.

GABARITo

1. LETRA A 2. LETRA A
3. LETRA D

LISTA DE QUESTõES - DIvERSAS BANCAS

í. (ESAF / TCU - 2002) Se um programa não for amigável ao usuário (user friendliness)freqüentemente estará destinado ao fracasso, mesmo que as funções que ele execute sejam valiosas. A usabilidade é a forma de se quantificar este fator e pode ser medida segundo quatro características. Uma destas características é a(o):
a) facilidade com que o programa pode ser corrigido se um erro for encontrado.

b) grau de corretitude com que o software executa a função que é dele exigida.

c) habilidade física e/ou intelectual exigida para se aprender o sistema.

d) medida onde um defeito é definido como uma falta verificada de conformidade aos requisitos.
e) custo para se corrigir defeitos encontrados depois que o software foi liberado para o usuário final.
2. (ESAF / CVM - 2010) No ciclo da Engenharia da Usabilidade, as atividades da fase de análise são:
a) Análise da instituição do usuário. Análise do contexto da tarefa. Análise das possibilidades e restrições do treinamento. Análise de princípios setoriais para o projeto.
b) Análise do perfil do usuário. Análise do contexto da plataforma. Análise de compatibilidade gerencial. Análise de princípios gerais para o projeto.
c) Análise do perfil do usuário. Análise do contexto da tarefa. Análise das possibilidades e restrições da plataforma. Análise de princípios gerais para o projeto.
d) Análise do perfil do desenvolvedor. Análise de requisitos. Análise das possibilidades e sistemas da plataforma. Análise de princípios gerais para as transações.
e) Análise da instituição do usuário. Análise de compromissos. Análise das possibilidades e restrições da estrutura. Análise de ameaças à segurança do projeto.
3. (ESAF / CVM - 2010) São heurísticas de usabilidade:

a) Coerência e padrões. Prevenção de erros. Relembrar em vez de Reconhecer. Flexibilidade e eficiência de mapeamento. Ajuda e documentação.
b) Visibilidade do estado do sistema. Mapeamento entre o sistema e o mundo real.
Liberdade e
Controle ao Usuário. Prevenção de erros. Reconhecer em vez de relembrar.

c) Versatilidade do estado do sistema. Previsão de acertos. Reconhecer em vez de relembrar.Design estético e maximalista. Suporte para o usuário reconhecer, diagnosticar e recuperar erros.
d) Mapeamento entre o sistema e os programas. Liberdade e Controle ao
Desenvolvedor.
Consistência e padrões. Flexibilidade e eficiência de uso. Ajuda e informação.

e) Visibilidade da estrutura do sistema. Compromisso entre o sistema e a configuração.Liberdade e Controle ao Usuário. Suporte para o usuário reconhecer,
diagnosticar e aplicar erros. Ajuda à implementação.
4. (CESGRANRIO / BACEN - 2009) Uma empresa, contratada para desenvolver uma aplicação standalone de análise financeira, deve utilizar um manual de orientações para construção da interface gráfica dessa aplicação. De acordo com as heurísticas de Nielsen, qual é a orientaçãoINCORRETA apresentada nesse manual?

a) Um mesmo comando deve provocar efeitos distintos, de acordo com o nível do usuário.

b) Os usuários devem ser informados sobre o que estão fazendo, com feedback imediato.

c) Os diálogos devem conter somente informações relevantes e necessárias.

d) Aterminologia deve ser baseada na linguagem do usuário e não orientada ao sistema.

e) A interface deve ter convenções que não sejam ambíguas.

5. (CESGRANRIO / PETROBRÁS - 2008) Assinale a opção que NÃO expressa um princípio de projeto de interface com o usuário.
a) Reduzira demanda de memória de curto prazo do usuário.

b) Basear o layout visual em uma metáfora do mundo real.

c) Permitir que a interação com o usuário seja interruptível e possa ser desfeita (undo).

d) Estabelecer defaults (para escolhas e preenchimento de formulários) que façam sentido para o usuário.
e) Mostrar informações completas a priori, permitindo que o usuário reduza o nível de detalhe se desejar.
6. (QUADRIX/CFP-2012) Com relação às recomendações de usabilidade em websites, é correto afirmar que:
a) janelas pop-up devem sempre ser utilizadas porque são acessíveis aos deficientes visuais e fornecem informações úteis antes mesmo de o usuário pedir.
b) documentos para download devem ser sempre disponibilizados em formatos especiais ou proprietários.
c) páginas de transição, de abertura (splash-pages) ou "em construção" devem ser usadas para melhorara navegação.
d) elementos comuns a todas as páginas, como logotipos, atalhos e caixas de busca,
não devem estar sempre na mesma posição nas páginas do site para não cansar o usuário visualmente.
e) o comportamento e as funcionalidades do navegador não devem ser alterados para satisfazer necessidades especiais das páginas, pois o usuário deve ter autonomia na utilização do site.
GABARITo

1. LETRA C

2. LETRA C

3. LETRA B

4. LETRA A

5. LETRA E

6. LETRA E

