# Engenharia de Software e Sistemas - XP

Índice

1) Metodologias Ágeis - XP

2) Metodologias Ágeis - XP - Principais Práticas

3) Metodologias Ágeis - XP - Processo do XP

4) Metodologias Ágeis - XP - Valores Fundamentais

5) Metodologias Ágeis - XP - Princípios Básicos

6) Resumo - Metodologias Ágeis - XP

7) Questões Comentadas - Metodologias Ágeis - XP - CESPE

8) Questões Comentadas - Metodologias Ágeis - XP - FCC

9) Questões Comentadas - Metodologias Ágeis - XP - FGV

10) Questões Comentadas - Metodologias Ágeis - XP - Diversas ...

11) Lista de Questões - Metodologias Ágeis - XP - CESPE

12) Lista de Questões - Metodologias Ágeis - XP - FCC

13) Lista de Questões - Metodologias Ágeis - XP - FGV

14) Lista de Questões - Metodologias Ágeis - XP - Diversas

APRESENTAçÃo

O assunto da aula de hoje é: Extreme Programming! Trata-se de uma famosa metodologia de desenvolvimento ágil. É muuuuuuuuito tranquila de entender, teoria pequena e muitas questões para treinar. Essa é aquela aula para dar uma relaxada porque não exige muito. Tentem fazertodas as questões propostas e a chance de você errar uma questão de prova sobre esse tema será bem pequena. Vamos lá...
PROFESSOR DIEGO CARVALHO - WWW.INSTAGRAM.COM/PROFESSORDIEGOCARVALHO

Extreme programming

IHCIIIC^^' icrator.net |

Galera, todos os tópicos da aula possuem Faixas de Incidência, que indicam se o assunto cai muito ou pouco em prova. Diego, se cai pouco para que colocar em aula? Cair pouco não significa que não cairá justamente na sua prova! A ideia aqui é: se você está com pouco tempo e precisa ver somente aquilo que cai mais, você pode filtrar pelas incidências média, alta e altíssima; se você tem tempo sobrando e quer vertudo, vejam também as incidências baixas e baixíssimas. Fechado?
INCIDÊNCIA EM PROVA: BAIXÍSSIMA
INCIDÊNCIA EM PROVA: BAIXA

TCÍDÊNCÍÃÈMPRÕVÕÉDÍ^

INCIDÊNCIA EM PROVA: ALTA

TIÕÍDÉNCÍ^Ã^RÕV^UÍSSÍMT

Além disso, essas faixas não são por banca - é baseado tanto na quantidade de vezes que caiu em prova independentemente da banca e também em minhas avaliações sobre cada assunto...
#ATENÇÃO

Avisos
Importantes

O curso abrange todos os níveis de conhecimento...

Esse curso foi desenvolvido para ser acessível a alunos com diversos níveis de conhecimento diferentes. Temos alunos mais avançados que têm conhecimento prévio ou têm facilidade com o assunto. Por outro lado, temos alunos iniciantes, que nunca tiveram contato com a matéria ou até mesmo que têm trauma dessa disciplina. A ideia aqui é tentar atingir ambos os públicos -
iniciantes e avançados - da melhor maneira possível..

Por que estou enfatizando isso?

O material completo é composto de muitas histórias, exemplos, metáforas, piadas, memes, questões,
desafios, esquemas, diagramas, imagens, entre outros. Já o material simplificado possui exatamente o mesmo núcleo do material completo, mas ele é menor e bem mais objetivo. Professor, eu devo estudar por qual material? Se você quiser se aprofundar nos assuntos ou tem dificuldade com a matéria,necessitando de um material mais passo-a-passo, utilize o material completo. Se você não quer se aprofundar nos assuntos ou tem facilidade com a matéria, necessitando de um material mais direto ao ponto, utilize o material simplificado.
Por fim...

O curso contém diversas questões espalhadas em meio à teoria. Essas questões possuem um comentário mais simplificado porque têm o único objetivo de apresentar ao aluno como bancas de concurso cobram o assunto previamente administrado. A imensa maioria das questões para que o aluno avalie seus conhecimentos sobre a matéria estão dispostas ao final da aula na lista de exercícios e possuem comentários bem mais completos, abrangentes e direcionados.
EXTREME PRoCRAMMINC (XP)

Conceitos Básicos

Em 1996, Kent Beck desenvolveu um novo paradigma de desenvolvimento de software que rompia com grande parte das metodologias tradicionais e a batizou deExtreme Programming. Por que extremo? Porque ele recomenda que as boas práticas sejam levadas ao extremo! Ahn? Como assim, professor?
Testar é bom?

Então vamos testar toda hora!

Iterar é bom?

Então vamos iterartoda hora!

Integrar é bom?

Então vamos integrartoda hora!

O eXtreme Programming é uma metodologia ágil de desenvolvimento de software para equipes pequenas, coesas e multidisciplinares cujos projetos possuem requisitos vagos e em constante mudança. Ele parte do princípio de que o código-fonte é a melhor documentação, pois qualquer outra se torna rapidamente desatualizada e perde sua confiabilidade. Aliás, a codificação/programação é a atividade principal no XP!
No eXtreme Programming, todos os requisitos são expressos como cenários (também chamados histórias do usuário1), que são implementados diretamente como uma série de tarefas. Os programadores trabalham em pares e desenvolvem testes para cada tarefa antes da escrita do código-fonte em si. Sempre que há integração de uma nova funcionalidade, há novos testes e o usuário realiza uma priorização dos requisitos para o desenvolvimento.
A equipe de desenvolvimento (ou programadores) avalia cada um dos cenários e os divide em tarefas. Cada tarefa representa uma característica discreta/isolada do sistema e um teste unitário pode então ser projetado para essa tarefa. Os testes de aceitação (ou testes de cliente)são especificados pelo cliente e mantêm o foco nas características e funcionalidades visíveis do sistema como um todo.
No XP, o desenvolvimento incremental é apoiado por pequenos e frequentes releases do sistema e por uma abordagem de descrição de requisitos baseada nos cenários do cliente. Além disso, o envolvimento do cliente em tempo integral facilita bastante o desenvolvimento e melhora
1 Por vezes, também chamado de estórias de usuário.

a qualidade do produto. Agora vejam só... eu falei muito rapidamente sobre histórias de usuário,mas é importante se aprofundar um pouco porque ela é muito importante.

Histórias de Usuário (User Stories) são artefatos de desenvolvimento utilizados em sistemas geridos segundo metodologias ágeis. Nós podemos dizer que as histórias de usuário são uma descrição resumida de alguma funcionalidade fornecida pelo sistema do ponto de vista de um usuário desse sistema. Ela representa uma pequena parte da funcionalidade do sistema a ser construído - não se trata de uma especificação completa de uma funcionalidade. Vejamos...
Uma história de usuário é apenas um símbolo das conversas passadas e futuras entre o cliente e os programadores. Lembrando que a presença do cliente no local minimiza a necessidade de documentar extensamente cada história. Por que? Porque os programadores podem simplesmente dar alguns passos e fazer suas perguntas ao cliente. Galera, é muito mais proveitoso tirar uma eventual dúvida rapidamente do que marcar uma reunião formal para dias depois...
Os detalhes das histórias de usuário são capturados nos testes automatizados de aceitação que são posteriormente usados para validar a implementação da história. Eventualmente poderá não ser necessário escrever descrições para todas as histórias, visto que o nome de algumas histórias já irá fornecer informações suficientes. E o que indica uma boa história de usuário? O cliente deverá se preocupar com ela.
A história deverá ter valor de negócio na visão do cliente, para que possa ser priorizada. Às vezes uma história precisa ser decomposta em partes menores para caber em uma iteração. Se por si só a história não fornecer valor de negócio, deverá fornecer no mínimo progresso em direção a uma funcionalidade de valor ao negócio. As histórias de usuário atravessam verticalmente a arquitetura do produto - normalmente elas não estão focadas em um subsistema específico.
Histórias de usuário podem ser razoavelmente estimadas pelos desenvolvedores e as histórias que não puderem ser estimadas idealmente deverão ser reescritas. Além disso, casos de teste devem ser escritos para verificar se os programadores as implementaram corretamente. Oque são casos de teste, Diego? É um conjunto de condições usadas para teste de software -ele especifica os valores de entrada e os resultados esperados do processamento de uma funcionalidade.
Por fim, elas devem ser concluídas em até uma iteração. Uma história de usuário que não caiba em uma iteração deverá ser decomposta em duas ou mais histórias menores de modo que caibam em uma iteração. Galera, as histórias criam um ambiente de propriedade do cliente em relação aos recursos e prioridades em um contexto incremental e iterativo de desenvolvimento. Aseguir, podemos ver mais alguns exemplos de histórias de usuário:

pagflkvteiAzto - Boleto

Como ciiente, quero ixtilizar a forma de pagamento P>oieto bancárioPara pagar meus pedidos.

Pagamento - Cartão de
Crédito - P>andeira A

Como Kkvt ciiente, quero ixtilizar a forma de pagamento Cartão de Crédito da bandeira A
Para pagar meus pedidos.

Pagamento - Pébito em
Conta - Panco ±

Como um Ciiente, quero ixtílizar a forma de pagamento Bébito em Conta do P>aneo 1
Para pagar meus pedidos.

Pagamento - Cartão de
Crédito - bandeira B

Como um Ciiente, quero utiiízar a forma de pagamento Cartão de Crédito da bandeira B
Para pagar meus pedidos.

Pagamento - Péloíto em
Conta - Panco 2

Como um Ciiente, quero utilizar a forma de pagamento Pébito em Conta do P>anco 2
Para pagar meus pedidos.

Pagamento - Cartão de
Crédito - Pandeira C

Como um Ciiente, quero ixtilizar a forma de pagamento Cartão de Crédito da bandeira C
Para pagar meus pedidos.

Principais Práticas

O XP possui um conjunto de práticas que são frequentemente utilizadas. Galera... isso cai, mas cai com muita força em prova! Talvez seja a parte mais importante da aula :)
DESCRIÇÃO

Os requisitos são registrados em cartões de histórias e as histórias a serem incluídas em um release são determinadas pelo tempo disponível e sua prioridade relativa. Os desenvolvedores dividem essas histórias em tarefas.
O conjunto mínimo útil de funcionalidade que agrega valor ao negócio é desenvolvido primeiro. Releases do sistema são frequentes e adicionam funcionalidade incrementalmente ao primeiro release.
É realizado um projeto suficientemente simples de modo que atenda aos requisitos atuais e nada mais. Deve-se lembrar que um código simples não é código fácil (KIS- Keep lt Simple).
Um framework automatizado de teste unitário é usado para escrever os testes para uma nova parte da funcionalidade antes que esta seja implementada. Portanto, primeiro se escreve 0teste, depois faz-se a implementação.

Espera-se que todos os desenvolvedores recriem 0 código continuamente tão logo os aprimoramentos do código forem encontrados. Isso torna 0 código simples de entender e fácil de manter.
Os desenvolvedores trabalham em pares, um verificando 0 trabalho do outro e fornecendo apoio para realizarsempre um bom trabalho. Eles utilizam 0 mesmo mouse, teclado e monitor.
Os pares de desenvolvedores trabalham em todas as áreas do sistema, de tal maneira que não se formem ilhas de conhecimento, com todos os desenvolvedores de posse de todo o código.Qualquerum pode mudar qualquer coisa.

Tão logo o trabalho em uma tarefa seja concluído, este é integrado ao sistema como um todo.
Depois de qualquer integração, todos os testes unitários do sistema devem ser realizados.

Grandes quantidades de horas extras não são consideradas aceitáveis, pois, no médio prazo,
há uma redução na qualidade do código e na produtividade. Trabalhar por longos períodos se torna contraproducente - recomenda-se 40 horas semanais.
A equipe se comunica sobre 0 desenvolvimento de software por meio de metáforas, caso consiga encontrar uma que realmente faça sentido dentro do contexto e possa facilitar a comunicação.
Um representante do usuário final do sistema deve estar disponível em tempo integral para apoiara equipe. No XP, 0 cliente é um membro da equipe de desenvolvimento e é responsável portrazeros requisitos do sistema.
Reuniões são realizadas em pé para não se perder 0 foco nos assuntos, produzindo reuniões mais rápidas, somente abordando as tarefas realizadas e tarefas a realizar pela equipe no futuro.
A equipe de desenvolvimento é formada por pessoas engajadas e multidisciplinares, i.e., elas possuem habilidades para diversas áreas do projeto.
JOGO DO
PLANEJAMENTO

O planejamento de um release e das iterações são feitos com base nas histórias e conta com a colaboração de toda equipe de desenvolvimento, inclusive o cliente, divididos em papeis:negócio e técnico. Os clientes priorizam e os desenvolvedores avaliam e estimam.

É claro que - no contexto do dia a dia - nem todas as práticas são utilizadas por organizações que adotam o XP. Em regra, cada organização escolhe aquelas que consideram mais úteis,eficientes e viáveis. Ex: para acomodar os diferentes níveis de habilidade, alguns programadores não fazem refatoração em partes do sistema que não desenvolveram; nem sempre é possível programar em pares; etc. É claro que a teoria trata do mundo ideal...
Processo do XP

E como seria o processo do Extreme Programming? Galera, no contexto de programação, a abordagem orientada a objetos é o paradigma de desenvolvimento preferido do XP e envolve um conjunto de regras e práticas em torno de quatro atividades metodológicas principais: (1)Planejamento, (2) Projeto, (3) Codificação e (4) Teste. Observem na imagem abaixo como tudo isso funciona:
projeto simples soluções pontuais cartões CRC protótipos
1 - PLANEJAMENTO

A atividade de planejamento se inicia com a atividade de ouvir-uma atividade de levantamento de requisitos que capacita os membros técnicos da equipe a entender o ambiente de negócios e a fim de ter uma percepção ampla sobre os resultados solicitados, fatores principais e funcionalidade."Ouvir" conduz à criação de um conjunto de histórias de usuários que descreve o resultado, as características e a funcionalidade requisitados para o software a ser construído.
Cada história é escrita pelo cliente e é colocada em uma ficha. Ele atribui um valor
(prioridade) à história baseando-se no valor de negócio global do recurso/função. Os membros da equipeXP
avaliam cada história e atribuem um custo a ela medido em semanas de desenvolvimento.
Se a história requerer, por estimativa, mais que três semanas de desenvolvimento, é solicitado ao cliente para dividir a história em histórias menores e a atribuição de valor e custo ocorre novamente.
É importante notar que podem ser escritas novas histórias a qualquer momento.
Clientes e desenvolvedores trabalham juntos para decidir como agrupar histórias para a versão seguinte(o próximo incremento de software) a ser desenvolvida pela equipe XP. Conseguindo chegar a um compromisso básico (concordância sobre quais histórias serão incluídas, data de entrega, etc)para uma versão, a equipe XP ordena as histórias a ser desenvolvidas em uma das três formas:

(í) todas serão implementadas imediatamente (em um prazo de poucas semanas); (2) as histórias de maior valor serão deslocadas para cima no cronograma e implementadas primeiro; ou(3) as histórias de maior risco serão deslocadas para cima no cronograma e implementadas primeiro.Depois de a primeira versão do projeto (também denominada incremento de software) ter sido entregue, a equipe XP calcula a velocidade do projeto.
De forma simples, a velocidade do projeto é o número de histórias de clientes implementadas durante a primeira versão. Assim, a velocidade do projeto pode ser utilizada para (1)ajudar a estimar as datas de entrega e o cronograma para versões subsequentes e (2) determinar se foi assumido um compromisso exagerado para todas as histórias ao longo de todo o projeto de desenvolvimento.
Se ocorrer um exagero, o conteúdo das versões é modificado ou as datas finais de entrega são alteradas. Conforme o trabalho de desenvolvimento prossegue, o cliente pode acrescentar histórias, mudar o valor de uma existente, dividir algumas ou eliminá-las. Em seguida,a equipe XP
reconsidera todas as versões remanescentes e modifica seus planos de acordo. Vamos ver agora como funciona o Projeto...
2 - PROJETO

O projeto XP segue rigorosamente o princípio KIS (Keep lt Simple, ou seja,
preserve a simplicidade). É preferível sempre um projeto simples do que uma representação mais complexa.Como acréscimo, o projeto oferece um guia de implementação para uma história à medida que é escrita — nada mais, nada menos. O projeto de funcionalidade extra (pelo fato de o desenvolvedor supor que ela será necessária no futuro) é desencorajado.
O Extreme Programming encoraja o uso de cartões CRC (Classe -
Responsabilidade -
Colaborador) como um mecanismo eficaz para pensar sobre o software em um contexto orientado a objetos. Os cartões CRC identificam e organizam as classes orientadas a objetosy relevantes para o incremento de software corrente. Os cartões CRC são o único artefato de projeto produzidos como parte do processo XP.
Se um difícil problema de projeto for encontrado como parte do projeto de uma história, o XPrecomenda a criação imediata de um protótipo operacional dessa parte do projeto.
Denominada solução pontual, o protótipo do projeto é implementado e avaliado. O objetivo é reduzir o risco para quando a verdadeira implementação iniciar e validar as estimativas originais para a história contendo o problema de projeto.
Anteriormente, nós dissemos que o XP encoraja a refatoração - uma técnica de construção que também é um método para otimização de projetos. Refatoração é o processo de alteração de um sistema de software de tal forma que não se altere o comportamento externo do código, mas se aprimore a estrutura interna. É uma forma disciplinada de organizar código (e modificar/simplificar o projeto interno) que minimiza as chances de introdução de bugs.
Ao se refatorar, se está aperfeiçoando o projeto de codificação depois de este ter sido feito. Como o XP não usa praticamente nenhuma notação e produz poucos, se algum, artefatos,além dos cartões CRC e soluções pontuais, o projeto é visto como algo transitório que pode e deve ser continuamente modificado conforme a construção prossegue. O objetivo é controlar modificações sugerindo pequenas mudanças de projeto capazes de melhorá-lo radicalmente.
Deve ser observado, no entanto, que o esforço necessário para a refatoração pode aumentar dramaticamente à medida que o tamanho de uma aplicação cresça. Um aspecto central noXP é o de que a elaboração do projeto ocorre tanto antes como depois de se ter iniciado a codificação.Na realidade, a própria atividade de desenvolvimento guiará a equipe XP quanto à aprimoração do projeto. Vamos partir para a codificação...
3 - CODIFICAÇÃO:

Depois de desenvolvidas as histórias e o trabalho preliminar de elaboração do projeto ter sido feito, a equipe não passa para a codificação, mas - sim - desenvolve uma série de testes de unidades que exercitarão cada uma das histórias a ser inclusas na versão corrente(incremento de software). Uma vez criado o teste de unidades, o desenvolvedor poderá melhor focar-se no que deve ser implementado para ser aprovado no teste. Nada estranho é adicionado (KIS)!
Estando o código completo, este pode ser testado em unidade imediatamente, e, dessa forma,prover - instantaneamente - feedback para os desenvolvedores. Conforme vimos,
um conceito-
chave na atividade de codificação é a programação em dupla. O Extreme
Programming recomenda que duas pessoas trabalhem juntas em uma mesma estação de trabalho para criar código para uma história.
Isso fornece um mecanismo para resolução de problemas em tempo real (duas cabeças normalmente funcionam melhor do que uma) e garantia da qualidade em tempo real (o código é revisto à medida que é criado). Ele também mantém os desenvolvedores focados no problema em questão. Na prática, cada pessoa assume um papel ligeiramente diferente. Por exemplo: uma pessoa pensa nos detalhes de codificação, enquanto outra trata dos padrões de codificação.
Conforme a dupla de programadores completa o trabalho, o código que desenvolveram é integrado ao trabalho de outros. Em alguns casos, isso é realizado diariamente por uma equipe de integração.Em outros, a dupla de programadores é responsável pela integração. A estratégia de integração contínua ajuda a evitar problemas de compatibilidade e de interfaceamento, além de criar um ambiente "teste da fumaça" que ajuda a revelar erros precocemente.
4-TESTES:

Já foi observado que a criação de testes de unidade, antes de começar a codificação, é um elemento-chave da abordagem XP. Os testes de unidade criados devem ser implementados usando-se uma metodologia que os capacite a ser automatizados (assim, poderão ser executados fácil e repetidamente). Isso encoraja uma estratégia de testes de regressão, toda vez em que o código for modificado (o que é frequente, dada a filosofia de refatoração do XP).
Como os testes de unidades individuais são organizados em um "conjunto de testes universal", os testes de integração e validação do sistema podem ocorrer diariamente. Isso dá à equipe XP uma indicação contínua do progresso e também permite lançar alertas logo no início, caso as coisas não andem bem. Wells afirma: "Corrigir pequenos problemas em intervalos de poucas horas leva menos tempo do que corrigir problemas enormes próximo ao prazo de entrega".
E como é a visão de Sommerville sobre o Processo XP? Bem., ele afirma que os clientes estão intimamente envolvidos na especificação e priorização dos requisitos do sistema. Os requisitos não estão especificados como uma lista de funções requeridas do sistema. Pelo contrário, o cliente do sistema é parte da equipe de desenvolvimento e discute cenários com outros membros da equipe. Juntos, eles desenvolvem um cartão de história, englobando as necessidades do cliente:
Prescrição de medicamentos

Kate é uma médica que deseja prescrever medicamentos para um paciente de uma clínica. 0 prontuário do paciente já está sendo exibido em seu computador, assim, ela clica o campo'medicação'e pode selecionarYnedicação atual','nova medicação',ou'formulário'.

Se ela selecionar'medicação atual', o sistema pede que ela verifique a dose. Se ela quiser mudar a dose, ela altera esta e em seguida, confirma a prescrição.
Se ela escolher'nova medicação', o sistema assume que ela sabe qual medicação receitar.

Ela digita as primeiras letras do nome do medicamento. 0 sistema exibe uma lista de possíveis fármacos que começam com essas letras. Ela escolhe a medicação requerida e o sistema responde, pedindo-lhe para verificar se o medicamento selecionado está correto.
Ela insere a dose e, em seguida, confirma a prescrição.

Se ela escolhe'formulário', o sistema exibe uma caixa de busca para o formulário aprovado.

Ela pode, então, procurar pelo medicamento requerido. Ela seleciona um medicamento e é solicitado que verifique se a medicação está correta. Ela insere a dose e, em seguida, confirma a prescrição.
0 sistema sempre verifica se a dose está dentro da faixa permitida. Caso não esteja, Kate é convidada a alterar a dose.
Após Kate confirmar a prescrição, esta será exibida para verificação. Ela pode escolher'OK'ou
'Alterar'. Se clicar em 'OK' a prescrição fica gravada nos bancos de dados da auditoria.
Se ela clicar em Alterar', reinicia o processo de'Prescrição de Medicamentos'.

A equipe de desenvolvimento, então, tenta implementar esse cenário em uma release futura do software. Os cartões de história são as principais entradas para o processo de planejamento em XPou Jogo de Planejamento. Uma vez que tenham sido desenvolvidos, a equipe de desenvolvimento os divide em tarefas e estima o esforço e os recursos necessários para a realização de cada tarefa.Esse processo geralmente envolve discussões com o cliente para refinamento dos requisitos.

O cliente, então, prioriza as histórias para implementação, escolhendo aquelas que podem ser usadas imediatamente para oferecer apoio aos negócios. A intenção é identificar funcionalidade útil que possa ser implementada em cerca de duas semanas, quando o próximo release do sistema é disponibilizado para o cliente. Claro que, como os requisitos mudam, as histórias não implementadas mudam ou podem ser descartadas.
Tarefa 1: Alterar dose de medicamentos prescritos
Tarefa 2: Seleção de formulário

Tarefa 3: Verificação de dose

A verificação da dose é uma precaução de segurança para verificar se o médico não receitou uma dose perigosamente pequena ou grande.
Usando o ID do formulário para o nome do medicamento genérico, procure o formulário e obtenha a dose mínima e máxima recomendada.
Verifique a dose mínima e máxima prescrita. Caso esteja fora da faixa, emita uma mensagem de erro dizendo que a dose está muito alta ou muito baixa.
Caso esteja dentro da faixa, habilite o botão 'Confirmar'.

Se houver necessidade de mudanças em um sistema que já tenha sido entregue, novos cartões de histórias são desenvolvidos e, mais uma vez, o cliente decide se essas mudanças devem ter prioridade sobre a nova funcionalidade. Às vezes, durante o jogo de planejamento, emergem questões que não podem ser facilmente respondidas, tornando necessário algum trabalho adicional para explorar possíveis soluções.
A equipe pode fazer algum protótipo ou desenvolvimento-teste para entender o problema e a solução. Em termos XP, isso é chamado de spike - um incremento em que nenhum tipo de programação é realizado. Também pode haver spikes de projeto da arquitetura do sistema ou para desenvolvera documentação do sistema. De acordo com Sommerville, eis o ciclo de um incremento no Extreme Programming:
PROCESSO PARA DESENVOLVER UM INCREMENTO

Avaliar o sistema
Liberar o software
Desenvolver,
integrar e testar software
Valores Fundamentais

VALORES
FUNDAMENTAIS

COMUNICAÇÃO

DESCRIÇÃO

Para se desenvolver um sistema de software, exige-se comunicar os requisitos de sistema para os desenvolvedores. Em metodologias formais de desenvolvimento de software, esta tarefa é realizada por meio de documentação. O Extreme Programming favorece projetos simples,metáforas comuns, a colaboração dos usuários, programadores e outros stakeholders, a comunicação verbal frequente e o feedback.
SIMPLICIDADE

XP incentiva que se comece com a solução mais simples. Funcionalidades adicionais podem ser acrescentadas posteriormente. Alega-se que desenvolverfunções que não são necessárias hoje pode ser prejudicial, na medida em que futuramente essa função pode não ser mais útil.Codificação e projeto de necessidades futuras incertas implicam o risco de gastar recursos em algo não mais necessários, embora talvez atrasando aspectos cruciais.
FEEDBACK

O feedback ocorre quando os testes unitários ou testes de integração retornam o estado do sistema após a implementação das mudanças. Ademais, como os clientes participam do desenvolvimento de testes, eles podem dar um feedback instantâneo. Dessa forma, o cliente pode orientar o desenvolvimento em uma possível recodificação do sistema. Quando o cliente traz um novo requisito, recebe um feedback de tempo e orçamento.
CORAGEM

A coragem permite que os desenvolvedores se sintam confortáveis com ao refatorar o seu código, quando necessário. Eventualmente, há de se ter coragem para jogar fora um código ou para remover um código obsoleto, não importa quanto esforço e tempo se gastou para produzi-lo. Além disso, coragem significa persistência, pois um programador pode se encontrar preso em um problema complexo durante um dia inteiro sem conseguir resolver.
RESPEITO

Aqui se inclui o respeito pelos outros, assim como o auto-respeito. Membros devem respeitar seu próprio trabalho, sempre se esforçando para oferecer alta qualidade e buscando o melhor projeto para a solução através de refatoração. Ninguém na equipe deve se sentir desvalorizado ou ignorado. Isso garante um alto nível de motivação e incentiva a lealdade dentro da equipe. Este valor é muito dependente dos outros valores.
CORAGEM

Cor

SIMPLICIDADE

Sim

51607774

Com

FEEDBACK

Fe

RESPEITO

Re

CorSim ComFeRe

Princípios Básicos

Da mesma forma que existem valores fundamentais, há também princípios básicos. Galera, não confundam esses dois conceitos! É muito fácil de confundi-los porque eles também são cinco. Os princípios básicos devem ser seguidos por equipes que forem utilizar o XPem projetos. Os princípios servirão para ajudar na escolha de alternativas de solução de problemas durante o curso do projeto. Vejamos quais são:
Retorno tempestivo do cliente, isto é, o sistema é apresentado e - a cada mudança - há um novo retorno positivo ou negativo do cliente.
Mudanças devem ser bem-vindas e ocorrerão de acordo com o melhor entendimento do projeto.
Todo problema deve sertratado para ser resolvido da forma mais simples possível.

A solução deve ser aperfeiçoada a cada iteração de modo a satisfazer, ao fim, as expectativas do usuário.
A qualidade jamais deve ser comprometida-essa é uma das razões para se ter a codificação dos testes antes da codificação do sistema.
No XP, as novas versões de software podem ser compiladas várias vezes por dia e os incrementos são entregues para os clientes aproximadamente a cada duas semanas. Quando um programador compila o sistema para criar uma nova versão, ele deve executar todos os testes automatizados existentes bem como os testes para a nova funcionalidade. A nova compilação do software será aceita somente se todos os testes foram executados com sucesso.
Um preceito essencial da engenharia de software tradicional é projetar mudanças. Em outras palavras, você deve antecipar mudanças futuras para o software e projetá-lo de tal maneira que essas mudanças possam ser implementadas facilmente. O Extreme Programming,contudo,
descarta esse princípio alegando que projetar para a mudança é, geralmente,
um esforço completamente inútil.
As mudanças antecipadas muitas vezes não ocorrem e as solicitações de mudança realizadas são completamente diferentes, causando diversos prejuízos ao sistema. Entenderam o problema? Oproblema com a implementação de mudanças não antecipadas é que elas tendem a degradar a estrutura do software, fazendo com que as mudanças se tornem cada vez mais difíceis de implementar.
O Extreme Programming lida com este problema defendendo que o software deve passar por refatoramento constantemente. Isso significa que a equipe de programação procura por possíveis melhorias no software, implementando-as imediatamente. Portanto, o software deve
/ 112

sempre ser fácil de compreender e alterar quando novas histórias de usuário são implementadas.Essa agilidade é muito importante no desenvolvimento ágil de software. Bacana?

Por último, vamos falar um pouco mais sobre Testes de Software. Sommerville afirma que uma das diferenças importantes entre o desenvolvimento incremental e o desenvolvimento dirigido a planos está na forma como o sistema é testado. Com o desenvolvimento incremental, não há especificação do sistema que possa ser usada por uma equipe de teste externa para desenvolvimento de testes do sistema.
Como consequência, algumas abordagens para o desenvolvimento incremental têm um processo de testes muito informal em comparação com os testes dirigidos a planos. Para evitar alguns dos problemas de teste e validação do sistema, o XP enfatiza a importância dos testes de software e inclui uma abordagem de testes que reduz as chances de erros desconhecidos na versão atual do sistema.
As principais características dos testes na metodologia XP são: (1) Desenvolvimento test-first; (2)Desenvolvimento de teste incrementais a partir de cenários; (3) Envolvimento dos usuários no desenvolvimento de testes e validação; (4) Uso de frameworks de testes automatizados. Bem,pessoal! Finalizamos toda a teoria do XP. Vocês viram que não é difícil e as questões são bem decorebas. Entendendo o fundamento, é possível respondê-las. Vamos lá...
RESUMo

EXTREME PROGRAMMING

O eXtreme Programming é uma metodologia ágil de desenvolvimento de software para equipes pequenas,
coesas e multidisciplinares cujos projetos possuem requisitos vagos e em constante mudança.

EXEMPLO DE HISTÓRIAS DE USUÁRIO

GwiO

Atèn, eh Hh/Wí tu audo doi

-tâfrxS/Ldú h&is ÁçMl, oua Atia,

. .

PROCESSOS DO EXTREME PROGRAMMING

valores das histórias de usuários critérios de teste de aceitação plano de iteração projeto simples cartões C7?C
soluções pontuais protótipos refabricacão programação em dupla
Versão incremento de software velocidade de projeto registrada(computada)

teste de unidades integração contínuo teste de aceitação
DESCRIÇÃO

Os requisitos são registrados em cartões de histórias e as histórias a serem incluídas em um release são determinadas pelo tempo disponível e sua prioridade relativa. Os desenvolvedores dividem essas histórias em tarefas.
O conjunto mínimo útil de funcionalidade que agrega valor ao negócio é desenvolvido primeiro. Releases do sistema são frequentes e adicionam funcionalidade incrementalmente ao primeiro release.
É realizado um projeto suficientemente simples de modo que atenda aos requisitos atuais e nada mais. Deve-se lembrar que um código simples não é código fácil (KIS- Keep lt Simple).
Um framework automatizado de teste unitário é usado para escrever os testes para uma nova parte da funcionalidade antes que esta seja implementada. Portanto, primeiro se escreve 0teste, depois faz-se a implementação.

Espera-se que todos os desenvolvedores recriem 0 código continuamente tão logo os aprimoramentos do código forem encontrados. Isso torna 0 código simples de entender e fácil de manter.
Os desenvolvedores trabalham em pares, um verificando 0 trabalho do outro e fornecendo apoio para realizarsempre um bom trabalho. Eles utilizam 0 mesmo mouse, teclado e monitor.
Os pares de desenvolvedores trabalham em todas as áreas do sistema, de tal maneira que não se formem ilhas de conhecimento, com todos os desenvolvedores de posse de todo o código.Qualquerum pode mudar qualquer coisa.

Tão logo o trabalho em uma tarefa seja concluído, este é integrado ao sistema como um todo.
Depois de qualquer integração, todos os testes unitários do sistema devem ser realizados.

Grandes quantidades de horas extras não são consideradas aceitáveis, pois, no médio prazo,
há uma redução na qualidade do código e na produtividade. Trabalhar por longos períodos se torna contraproducente - recomenda-se 40 horas semanais.
A equipe se comunica sobre 0 desenvolvimento de software por meio de metáforas, caso consiga encontrar uma que realmente faça sentido dentro do contexto e possa facilitar a comunicação.
Um representante do usuário final do sistema deve estar disponível em tempo integral para apoiara equipe. No XP, 0 cliente é um membro da equipe de desenvolvimento e é responsável portrazeros requisitos do sistema.
Reuniões são realizadas em pé para não se perder 0 foco nos assuntos, produzindo reuniões mais rápidas, somente abordando as tarefas realizadas e tarefas a realizar pela equipe no futuro.
A equipe de desenvolvimento é formada por pessoas engajadas e multidisciplinares, i.e., elas possuem habilidades para diversas áreas do projeto.
O planejamento de um release e das iterações são feitos com base nas histórias e conta com a colaboração de toda equipe de desenvolvimento, inclusive o cliente, divididos em papeis:negócio e técnico. Os clientes priorizam e os desenvolvedores avaliam e estimam.

VALORES
FUNDAMENTAIS

DESCRIÇÃO

COMUNICAÇÃO Para se desenvolver um sistema de software, exige-se comunicar os requisitos de sistema para os desenvolvedores. Em metodologias formais de desenvolvimento de software, esta tarefa é
SIMPLICIDADE

FEEDBACK

CORAGEM

RESPEITO

realizada por meio de documentação. O Extreme Programming favorece projetos simples,
metáforas comuns, a colaboração dos usuários, programadores e outros stakeholders, a comunicação verbal frequente e o feedback.
XP incentiva que se comece com a solução mais simples. Funcionalidades adicionais podem ser acrescentadas posteriormente. Alega-se que desenvolverfunções que não são necessárias hoje pode ser prejudicial, na medida em que futuramente essa função pode não ser mais útil.Codificação e projeto de necessidades futuras incertas implicam o risco de gastar recursos em algo não mais necessários, embora talvez atrasando aspectos cruciais.
O feedback ocorre quando os testes unitários ou testes de integração retornam o estado do sistema após a implementação das mudanças. Ademais, como os clientes participam do desenvolvimento de testes, eles podem dar um feedback instantâneo. Dessa forma, o cliente pode orientar o desenvolvimento em uma possível recodificação do sistema. Quando o cliente traz um novo requisito, recebe um feedback de tempo e orçamento.
A coragem permite que os desenvolvedores se sintam confortáveis com ao refatorar o seu código, quando necessário. Eventualmente, há de se ter coragem para jogar fora um código ou para remover um código obsoleto, não importa quanto esforço e tempo se gastou para produzi-lo. Além disso, coragem significa persistência, pois um programador pode se encontrar preso em um problema complexo durante um dia inteiro sem conseguir resolver.
Aqui se inclui o respeito pelos outros, assim como o auto-respeito. Membros devem respeitar seu próprio trabalho, sempre se esforçando para oferecer alta qualidade e buscando o melhor projeto para a solução através de refatoração. Ninguém na equipe deve se sentir desvalorizado ou ignorado. Isso garante um alto nível de motivação e incentiva a lealdade dentro da equipe. Este valor é muito dependente dos outros valores.
DESCRIÇÃO

Retorno tempestivo do cliente, isto é, o sistema é apresentado e - a cada mudança - há um novo retorno positivo ou negativo do cliente.
Mudanças devem ser bem-vindas e ocorrerão de acordo com o melhor entendimento do projeto.
Todo problema deve sertratado para ser resolvido da forma mais simples possível.

A solução deve ser aperfeiçoada a cada iteração de modo a satisfazer, ao fim, as expectativas do usuário.
A qualidade jamais deve ser comprometida - essa é uma das razões para se ter a codificação dos testes antes da codificação do sistema.
PARA MAIS DICAS: WWW.INSTAGRAM.COM/PROFESSORDIEGOCARVALHO

QUESTõES CoMENTADAS - CESPE

í. (CESPE / BANRISUL - 2022) Um aspecto central na XP é o fato de que a elaboração do projeto ocorre tanto antes quanto depois de se ter iniciado a codificação.
Comentários:

Perfeito! XP enfatiza a necessidade de ajustar e refinar o projeto à medida que o trabalho progride.Em vez de tentar prever o que será necessário com antecedência, a XP incentiva os desenvolvedores a se adaptarem às mudanças e aos requisitos emergentes durante o processo de desenvolvimento.Isso significa que o projeto é continuamente refinado e aperfeiçoado à medida que a codificação avança. É por isso que a XP destaca a necessidade de ter um equilíbrio entre a programação e o planejamento.
Gabarito: Correto

2. (CESPE / BANRISUL - 2022) Na metodologia XP (Extreme Programming), a atividade de planejamento se inicia com o levantamento de requisitos, em que são obtidas histórias de usuários, similares aos casos de uso; a seguir, clientes e desenvolvedores trabalham juntos para decidir como agrupar essas histórias.
Comentários:

Perfeito! O XP apoia a colaboração entre clientes e desenvolvedores para que todos possam entender as necessidades de negócio e as melhores abordagens para implementar as funcionalidades necessárias. O levantamento de requisitos é um dos principais pilares desta abordagem, e é por isso que é importante que os clientes e desenvolvedores trabalhem juntos para agruparas histórias de usuário e priorizaras necessidades.
Gabarito: Correto

3. (CESPE / Ministério da Economia - 2020) Grandes quantidades de horas extras são aceitáveis em médio e longo prazo, para agilizar a entrega de requisitos.
Comentários:

Uma das práticas do XP é o ritmo sustentável! Grandes quantidades de horas extras não são consideradas aceitáveis, pois - no médio prazo - há uma redução na qualidade do código e na produtividade. Trabalhar por longos períodos se torna contraproducente - recomenda-se 40horas semanais.
Gabarito: Errado

4- (CESPE / Ministério da Economia - 2020) Como forma de agilizar as implantações de novas releases nesse modelo, são acumulados grandes grupos de funcionalidades e implantadas grandes releases.
Comentários:

Uma das práticas do XP são as pequenas releases! O conjunto mínimo útil de funcionalidade que agrega valor ao negócio é desenvolvido primeiro. Releases do sistema são frequentes e adicionam funcionalidade incrementalmente ao primeiro release.
Gabarito: Errado

5. (CESPE / Ministério da Economia - 2020) Os programadores trabalham em pares para que um possa verificar e apoiar o trabalho do outro e, assim, realizem um bom trabalho.
Comentários:

Uma das práticas do XP é a programação em pares! Os desenvolvedores trabalham em pares, um verificando o trabalho do outro e fornecendo apoio para realizar sempre um bom trabalho. Eles utilizam o mesmo mouse, teclado e monitor.
Gabarito: Correto

6. (CESPE / Ministério da Economia - 2020) O refactoring de código não faz parte do modelo XP,visto que a expectativa é a entrega ágil, e não deve ser considerada em tempo de projeto a recriação de código para aprimoramento.
Comentários:

Uma das práticas do XP é a refatoração! Espera-se que todos os desenvolvedores recriem o código continuamente tão logo os aprimoramentos do código forem encontrados. Isso torna o código simples de entender e fácil de manter.
Gabarito: Errado

7. (CESPE / Ministério da Economia - 2020) O XP possui planejamento incremental com requisitos registrados em histórias.
Comentários:

No eXtreme Programming, todos os requisitos são expressos como cenários (também chamados histórias do usuário), que são implementados diretamente como uma série de tarefas.
Gabarito: Correto

8. (CESPE / TCE-RO - 2019) No que diz respeito a processos e práticas ágeis, o desenvolvimento incremental a) é, assim como otest-driven development, uma prática da XP (Extreme Programming)que exige teste automatizado, domain-driven design, refactoring e integração contínua.
b) é, na XP (Extreme Programming), sustentado por meio de pequenos e frequentes releases do sistema, e os clientes estão intimamente envolvidos na especificação e na priorização dos requisitos do sistema.
c) enfoca, assim como oacceptance test-driven development, a qualidade do código desenvolvido quanto a recursividade, declaração das variáveis e clean code, de modo a torná-lo de fácil entendimento, modificação e testagem d) pressupõe o uso do behavior driven development, que considera a linguagem de programação a ser usada, da 4.a geração em diante, com foco,principalmente, no comportamento visual, interativo e cognitivo do sistema.
e) enfoca a integração contínua como uma prática de desenvolvimento de software,incompatível com a XP (E xtreme Programming) e o Scrum, que permite aos desenvolvedores agregarem alterações de código e realizarem testes.
Comentários:

(a) Errado. Esse item é bastante confuso, o desenvolvimento incremental não exige o domain-driven design (DDD); (b) Correto. No XP, o envolvimento do cliente ocorre em tempo integral,facilitando o desenvolvimento e a melhora do produto; (c) Errado. Na verdade, trata-se do TDD; (d)Errado. Ele não pressupõe o uso do Behavior Driven Development; (e) Errado.
A integração contínua não é incompatível com o XP e com o Scrum.
Gabarito: Letra B

9. (CESPE I TJ-AM - 2019) No XP (Extreme Programming), o valor de uma história de usuário é atribuído pelos membros da equipe e é medido em termos de semanas estimadas para o desenvolvimento.
Comentários:

No Extreme Programming, cada história é escrita pelo cliente e é colocada em uma ficha! O cliente atribui um valor (prioridade) à história baseando-se no valor de negócio global do recurso/função.
Os membros da equipe XP avaliam cada história e atribuem um custo a ela medido em semanas de desenvolvimento. Logo, quem atribui um valor é o cliente e, não, os membros da equipe.
Gabarito: Errado io.(CESPE / ABIN - 2018) Na extreme programming, como não há especificação de sistema que possa ser usada por equipe de teste externa, a característica de test-first exige que os implementadores de tarefa compreendam detalhadamente a especificação de comportamento da funcionalidade em desenvolvimento, a fim de que possam escrever o teste para o sistema.
Comentários:

Pessoal, vimos que umas das principais práticas do XP é a do Desenvolvimento
Test-First. Essa prática faz uso de testes unitários para cada funcionalidade, além disso, os testes devem ser escritos antes da implementação da funcionalidade e para isso os implementadores devem conhecer detalhadamente as especificações da funcionalidade que está sendo desenvolvida.
Gabarito: Correto n.(CESPE / BNB-2018) Em XP, a técnica de planning game é utilizada pelo cliente para identificar as prioridades do que deve ser construído em um software, sem a participação dos desenvolvedores.
Comentários:

Uma das práticas do XP é o jogo do planejamento. Nessa prática, o planejamento de uma release e das iterações são feitos com base nas histórias e conta com a colaboração de toda equipe de desenvolvimento, inclusive o cliente, divididos em papeis: negócio e técnico. Os clientes priorizam e os desenvolvedores avaliam e estimam.
Gabarito: Errado

12. (CESPE / ABIN - 2018) O ritmo ágil de desenvolvimento de softwares é uma prática usada para favorecer a entrega das releases quando grandes volumes de horas extras são tolerados.
Comentários:

Não se trata de ritmo ágil e, sim, ritmo sustentável! Grandes quantidades de horas extras não são consideradas aceitáveis, pois, no médio prazo, há uma redução na qualidade do código e na produtividade. Trabalhar por longos períodos se torna contraproducente - recomenda-se 40horas semanais).
Gabarito: Errado i3.(CESPE / ABIN - 2018) Para apoiar a equipe de desenvolvimento, é uma prática o uso do cliente on-site em tempo integral.
Comentários:

De fato, cliente on-site é uma prática do XP. Um representante do usuário final do sistema deve estar disponível em tempo integral para apoiar a equipe. No XP, o cliente é um membro da equipe de desenvolvimento e é responsável portrazeros requisitos do sistema.
Gabarito: Correto i4.(CESPE / STM - 2018) Na XP (Extreme Programming), programadores trabalham em pares,e requisitos são expressos como cenários, denominados histórias de usuários, os quais são implementados como uma série de tarefas.
Comentários:

A programação em pares é uma das práticas do XP. Além disso, requisitos realmente são expressos como cenários ou histórias de usuário, que são implementados como uma série de tarefas.
Gabarito: Correto

15. (CESPE / TRT - 7a Região (CE) - 2017) Acerca de metodologia XP, assinale a opção correta.

a) Para atingir a agilidade necessária, a equipe de desenvolvimento deve ser composta de pessoas com experiência comprovada na linguagem utilizada.
b) A prática de planning game do XP permite que o escopo do projeto seja alterado a cada semana.
c) Mesmo sendo considerada uma metodologia ágil, XP exige uma especificação completa e formal dos requisitos.
d) Em XP, denomina-se explanação o processo por meio do qual uma pessoa tenta explicar um assunto fazendo comparações com o mundo real.
Comentários:

(a) Errado, não há esse requisito; (b) Correto, vimos que no XP a prática do planning game é realmente adotada; (c) Errado, um projeto XP tem especificações simples; d) Errado,trata-se das metáforas.
Gabarito: Letra B

i6.(CESPE / TRE-BA - 2017) Considerando uma situação hipotética com o uso da XP
(eXtreme
Programming) concomitante com Scrum em um projeto de desenvolvimento de software em uma organização, julgue os seguintes itens.
I. É viável a utilização do TDD (Test Driven Development) na fase de sprint, de modo que se escreva o teste automático antes da codificação.
II. O princípio da integração contínua da XP deve ser utilizado especificamente na retrospectiva da sprint com vistas a integrar a equipe scrum.
III. Integrantes da equipe scrum podem realizar a programação do código em pares, o que proporciona, entre outras vantagens, o nivelamento de conhecimento da equipe.
IV. O conceito de requisito "pronto" continuaria válido, contudo, inviabilizaria o refactoring, pois é proibitivo inserir o mesmo item (requisito) em várias sprints.
Estão certos apenas os itens:

a) I e II.

b) I e III.

c) lie IV.

d) I, III e IV.

e) II, III e IV

Comentários:

(I) Correto. TDD é uma prática XP em que se escreve o teste antes de escrever o código do componente e é viável utilizá-lo em uma Sprint; (II) Errado. A Integração Contínua é uma práticaXP, mas não se integra a equipe, integram-se componentes e não deve ser utilizado na retrospectiva da sprint, mas na sprint em si; (III) Correto. A Programação em Pares é uma práticaXP e evidentemente proporciona o nivelamento de conhecimento da equipe;
(IV) Errado.
Refatoração é uma prática XP, mas não é proibido inserir o mesmo requisito em várias sprints.

Gabarito: Letra B

i7.(CESPE / TRE-TO - 2017) Em projetos de desenvolvimento de software, a extreme programming (XP) é um método ágil que usa a prática de:
a) projetos com planejamento completo sem incrementos.

b) grandes releases.

c) grande quantidade de horas extras.

d) trabalho em pares de desenvolvedores.

e) integrações após a entrega do software completo.

Comentários:

(a) Errado, planejamento incremental e, não, completo; (b) Errado, pequenas releases e, não,grandes; (c) Errado, ritmo sustentável e, não, grande quantidade de horas extras; (d)
Correto; (e)
Errado, integração contínua e, não, após a entrega do software completo.

Gabarito: Letra D

i8.(CESPE/ FUNPRESP-JUD-2016) Uma característica da metodologia XP é a existência de uma equipe técnica voltada para a agilidade e velocidade do desenvolvimento do software, de forma que todo o desenvolvimento seja feito sem a interferência ou ajuda do cliente até que os releases sejam disponibilizados para que o desenvolvimento se torne o mais ágil possível.
Comentários:

No XP o envolvimento do cliente ocorre em tempo integral. O que isso significa?
Significa que o cliente pode interferir em qualquer etapa do desenvolvimento. Esse envolvimento em tempo integral do cliente facilita o desenvolvimento e a melhora da qualidade do produto.
Gabarito: Errado ig.(CESPE / TCE-PA - 2016) E m XP (Extreme Programming), as user stories não objetivam definir o escopo global do sistema, mas avaliar a complexidade de cada uma de suas partes a fim serem estimados prazos na perspectiva dos usuários ou clientes do sistema.
Comentários:

No XP, todos os requisitos são expressos como cenários (histórias dos usuários). Ou seja, as user stories são uma descrição resumida de alguma funcionalidade, por isso não estão relacionadas ao escopo global, mas sim a funcionalidades específicas. Além disso, as user stories permitem que se avaliem a complexidade e que se defina as estimativas para as entregas aos clientes.
Gabarito: Correto

20. (CESPE/ FUNPRESP-JUD-2016) A programação em pares, em que os desenvolvedores atuam avaliando entre si o trabalho do outro, é uma prática da metodologia XP.
Comentários:

Perfeito! Os desenvolvedores trabalham em pares, um verificando otrabalho do outro efornecendo apoio para realizar sempre um bom trabalho. Eles utilizam o mesmo mouse, teclado e monitor.
Gabarito: Correto

21. (CESPE / FUNPRESP-JUD - 2016) As práticas da extreme programming, que tem por princípio liberar grandes releases de software, visam agregar valor ao negócio.
Comentários:

As práticas do XP têm por princípio liberar pequenas releases e, não, grandes releases. O conjunto mínimo útil de funcionalidade que agrega valor ao negócio é desenvolvido primeiro.Releases do sistema são frequentes e adicionam funcionalidade incrementalmente ao primeiro release.
Gabarito: Errado

22. (CESPE /TRT-PR - 2016) Um projeto desenvolvido mediante XP (Extreme Programming)
segue princípios opostos aos de um projeto implementado com base em KIS (Keep lt Simple).
Comentários:

Projeto Simples significa que é realizado um projeto suficientemente simples de modo que atenda aos requisitos atuais e nada mais. Deve-se lembrar que um código simples não é código fácil (KIS -Keep lt Simple). Logo, seguem princípios análogos/semelhantes e, não, opostos aos de um projeto implementado com base no Keep lt Simple.
Gabarito: Errado

23. (CESPE / TRE-RS- 2015) Tendo em vista que, em um processo ágil de desenvolvimento de software, foi adotado o XP (eXtreme Programming) e que os requisitos levantados foram expressos na forma de histórias de usuário, assinale a opção que apresenta,corretamente,
recomendações técnicas para a elaboração de um cartão de histórias de usuário.

a) Como um professor, quero calcular as médias semestrais dos alunos de modo que eu possa identificar quais serão aprovados.
b) O professor deseja o cálculo de notas semestrais com precisão de até duas casas decimais.

c) O sistema deve calcular as médias semestrais dos alunos com base nas notas atribuídas a eles pelos professores.
d) Como analista de requisitos, eu preciso oferecer o cálculo das notas semestrais aos professores em menos de um minuto.
e) Como um professor, eu preciso de releases semanais de funcionalidades, mesmo que elas possam ser refatoradas posteriormente.
Comentários:

A questão pergunta por recomendações para elaboração de histórias de usuários. Uma boa história de usuário é aquela em que o cliente se preocupa com ela. Além disso, ela deve ter valor de negócio na visão do cliente. Em suma, as histórias de usuários são feitas pelos clientes. Por fim, as histórias devem descrever o resultado, as características e a funcionalidade solicitados para o software a ser construído.
(a) Correto. O professor é o cliente, ele criou a história e definiu corretamente o resultado, as características e a funcionalidade; (b) Errado. O professor não definiu corretamente a funcionalidade; (c) Errado. O sistema não é o cliente; (d) Errado, o cliente é que deve elaborar a história; (e) Errado. Isso é papel do desenvolvedor.
Gabarito: Letra A

24.(CESPE / TJDFT - 2015) Na metodologia XP (extreme programming), em que todos os requisitos são expressos como cenários, deve-se aguardar, após a conclusão das tarefas,ciclos de cento e oitenta dias para a publicação de grandes releases do software.
Comentários:

Não, não há absolutamente nenhuma condição para a publicação de grandes releases - muito menos 180 dias! Já imaginaram isso? 180 dias!!!
Gabarito: Errado

25.(CESPE / TJDFT - 2015) As características da metodologia XP incluem o desenvolvimento interativo, que dispõe de um processo de testes informais.
Comentários:

Vamos lá! Já começo dizendo que não gostei dessa questão. Porque? Porque várias vezes a banca escreve interativo, em vez de iterativo, e dá como errado. Ora, é característica de qualquer tipo de desenvolvimento a interatividade, logo isso não deveria ser alvo de questão alguma, mas só algumas metodologias de desenvolvimento são iterativas e, isso sim, deveria ser alvo de questões.
O fato é que a questão não está errada ao dizer que o XP possui como característica o desenvolvimento interativo. Mas, porém, todavia, entretanto, ele dispõe de um processo de testes formais, como diz Sommerville - ele possui mecanismos para tal. Logo, para mim, a questão está errada, mas a banca a deu como correta e infelizmente não foram acatados recursos.
Gabarito: Correto

26.(CESPE / TRE-RS- 2015) Em um desenvolvimento ágil de sistemas utilizando o XP, foram adotadas as seguintes ações: foi dita a verdade ao cliente acerca do progresso do projeto e acerca de suas estimativas, além de haverem sido realizadas adaptações quando mudanças importantes aconteceram no projeto. Essas ações estão coerentes com o valor do XPdenominado:

a) sinceridade.

b) comunicação.

c) coragem.

d) feedback.

e) respeito.

Comentários:

A questão trata do valor da coragem! Ela permite que os desenvolvedores se sintam confortáveis com ao refatorar o seu código, quando necessário. Eventualmente, há de se ter coragem para jogar fora um código ou para remover um código obsoleto, não importa quanto esforço e tempo se gastou para produzi-lo. Além disso, coragem significa persistência, pois um programador pode se encontrar preso em um problema complexo durante um dia inteiro sem conseguir resolver.
Gabarito: Letra C

27.(CESPE / TRE-RS- 2015) Assinale a opção que apresenta uma característica relacionada a projetos que utilizam o método XP (eXtreme Programming), muito utilizado em projetos para
' o desenvolvimento de softwares.

a) grandes releases b) programação individual c) cliente off-site d) grandes volumes de horas extras e) planejamento incremental
Comentários:

(a) Errado, a prática adequada são pequenas releases; (b) Errado, a prática adequada é a programação em pares; (c) Errado, a prática adequada é cliente on-site; (d)Errado, a prática adequada é o ritmo sustentável; (e) Correto, essa é uma prática bastante utilizada no contexto doXP.

Gabarito: Letra E

28.(CESPE / STJ- 2015) Na Extreme Programming, a programação em pares cria ilhas de especialistas na equipe por meio da análise simultânea de duas pessoas no desenvolvimento do software.
Comentários:

Pelo contrário, a programação em pares permite que os programadores trabalhem em diversas áreas do sistema, de tal maneira que não se formem ilhas de conhecimento,com todos os desenvolvedores de posse de todo o código.
Gabarito: Errado

2g.(CESPE / FUB- 2015) Práticas de desenvolvimento de software aos pares de programadores,em que um programador verifica o trabalho do outro, são uma característica do método de desenvolvimento XP.
Comentários:

Perfeito! É uma das práticas mais cobradas em prova sobre o XP.

Gabarito: Correto

3o.(CESPE/ FUB-2015) É considerada como ritmo sustentável a carga horária de trabalho extensa para gerar rapidamente entregas de produtos de software, o que provoca grande quantidade de horas extras.
Comentários:

Opaaa... grandes quantidades de horas extras não são consideradas aceitáveis, pois, no médio prazo, há uma redução na qualidade do código e na produtividade. Trabalhar por longos períodos se torna contraproducente - recomenda-se 40 horas semanais.
Gabarito: Errado

3i.(CESPE / ANTT - 2013) São práticas ou princípios recomendados no modelo de desenvolvimento de software XP (eXtreme Programming) proposto porKent Beck:
programação em pares; semana de trabalho de 40 horas; refatoração sem piedade;desenvolvimento orientado a testes TDD (Test Driven Development); e desenvolvimento de metáforas arquiteturais.
Comentários:

Vamos verificar? Programação em Pares, ok. Semana de 40 horas, ok. Desenvolvimento orientado a testes TDD, ok. Desenvolvimento de metáforas arquiteturais, ok. Refatoração sem piedade, como é? Sem piedade? Galera, não faço ideia de onde a banca tirou esse nome!É simplesmente refatoração. No entanto, é melhor não brigar com a banca...
Gabarito: Correto

32. (CESPE / STF - 2013) XP (Extreme Programming) é uma metodologia ágil voltada para equipes pequenas e médias que desenvolvam software baseado em requisitos vagos e se caracteriza por possibilitar modificações rápidas.
Comentários:

É uma metodologia ágil? Sim! Voltada para equipes pequenas e médias? Sim! Desenvolvem software baseado em requisitos vagos? Sim! Possibilita modificações rápidas? Sim, lembrem-se que é um método ágil!
Gabarito: Correto

33. (CESPE/TCE-RO-2013) No método XP (eXtreming programming), os sistemas são concebidos a partir de uma metáfora e descritos em estórias do usuário. Esse método busca facilitar a comunicação com o cliente, entendendo a realidade deste e guiando o desenvolvimento com o uso de estória simples.
Comentários:

Perfeito! Uma das vantagens das metáforas é que elas simplificam o entendimento...

Gabarito: Correto

34.(CESPE / MPU 2013) XP é um método de desenvolvimento de software em que os requisitos são especificados em user stories; requisitos, arquitetura e design surgem durante o curso do projeto; e o desenvolvimento ocorre de maneira incremental.
Comentários:

Perfeito! De fato, ela utiliza histórias de usuário. Além disso, requisitos, arquitetura e design surgem durante o curso do projeto - elas não são completamente definidas previamente. Por fim, o desenvolvimento é incremental porque se trata de um método iterativo e incremental.
Gabarito: Correto

35. (CESPE / MPE-PI - 2012) O XP (Extreme Programming) é um método ágil, que preconiza a criação de um caso de teste unitário antes do início da codificação.
Comentários:

O XP é, de fato, um método ágil que preconiza o Test-First Design como uma de suas práticas, isto é, primeiro cria-se o teste para depois codificar a funcionalidade referente a esse teste.
Gabarito: Correto

36.(CESPE / ANAC - 2012) Para o método ágil de desenvolvimento conhecido como extreme programming, todos os requisitos funcionais são expressos como cenários (histórias do usuário)que são implementados diretamente como uma série de tarefas.

Comentários:

Corretíssimo! Requisitos funcionais são representados como cenários ou histórias de usuário, que são implementadas diretamente como uma série de tarefas.
Gabarito: Correto

37.(CESPE / ANAC - 2012) A técnica conhecida como refactoring é constantemente aplicada no desenvolvimento baseado no método ágil extreme programming.
Comentários:

Perfeito! Também conhecida como refatoração, essa é uma das técnicas amplamente preconizadas pelo XP!
Gabarito: Correto

38.(CESPE / ANAC - 2012) No modelo extreme programming, os testes de software só são realizados na etapa final de desenvolvimento do software e, somente nessa etapa, os programadores trabalham, obrigatoriamente, em pares, utilizando cada um o próprio computador.
Comentários:

Primeiro, testes de software não ocorrem somente na etapa final de desenvolvimento,
eles são realizados a todo momento. Ademais, programadores trabalham em pares a todo instante: um computador para dois programadores.
Gabarito: Errado

3g.(CESPE / ANAC - 2012) Na metodologia ágil XP (extreme programming), as metáforas são formas de transmitir ideias complexas de maneira simples, ou seja, utiliza-se uma linguagem simples entre a equipe e o cliente, com o objetivo de que, entre as inúmeras variáveis de controle em projetos, tais como tempo, custo, qualidade e escopo, obtenha-se maiorfoco no tempo,em detrimento do planejamento do release.
Comentários:

A primeira parte da questão está perfeita, isto é, metáforas ajudam a transmitir ideias complexas de maneira simples. No entanto, o objetivo dela não é obter maior foco no tempo.Ademais, o planejamento da release é dependente do tempo, logo não há essa distinção de foco!
Gabarito: Errado

4O.(CESPE/ EBC-2011) O XP segue um conjunto de valores, princípios e regras básicas que visam alcançar eficiência e efetividade no processo de desenvolvimento de software. Os valores são cinco: comunicação, simplicidade, feedback, coragem e respeito.
Comentários:

De fato, esses são os valores preconizados pelo XP: Comunicação, Simplicidade,
Feedback,
Coragem e Respeito.

Gabarito: Correto

/fi.(CESPE / STM - 2011) O Extreme Programming (XP), que se inclui entre os métodos ágeis,apresenta, entre outras, as seguintes características: pequenos releases, projeto simples,refactoring, programação em pares e propriedade coletiva.

Comentários:

Perfeito! Todas essas são características/práticas do Extreme Programming.

Gabarito: Correto

42.(CESPE / TRE-BA - 2010) Em XP, a prática denominada programação em pares
(pair programming) é realizada por um desenvolvedor em dois computadores, com o objetivo de aumentara produtividade.
Comentários:

Na verdade, são dois desenvolvedores utilizando apenas um computador. Observem que o intuito é aumentar a qualidade do software por meio da revisão constante pelo par.
Gabarito: Errado

43- (CESPE / ABIN - 2010) Na Extreme Programming, os requisitos são expressos como cenários e implementados diretamente como uma série de tarefas. O representante do cliente faz parte do desenvolvimento e é responsável pela definição de testes de aceitação do sistema.
Comentários:

Perfeito! Os requisitos são expressos como cenários (ou histórias de usuário)
e implementados como tarefas. Ademais, recomenda-se o Cliente On-Site, isto é, um representante do usuário final do sistema deve estar disponível em tempo integral para apoiar a equipe. Além disso,Pressman, 7a
Ed., pág. 77, afirma:

"XP acceptance tests, also called customer tests, are specified by the customer andfocus on overall system features and functionality that are visible and reviewable by the costumer.Acceptance tests are derivedfrom userstories that have been implemented as part ofa software release".
Gabarito: Correto

44.(CESPE / MPU - 2010) Extreme programming (XP) é embasado em requisitos conhecidos,definidos de antemão, que não sofram muitas alterações, devendo ser usado por equipes de pequeno porte, formadas por representantes de todos os stakeholders.
Comentários:

XP é um método ágil de desenvolvimento de software com requisitos vagos e em constante mudança, devendo ser usado por equipes de pequeno a médio porte, formadas - se possível - por representantes de todos os stakeholders.
Gabarito: Errado

45.(CESPE / TRE-BA - 2010) Os quatro valores fundamentais da metodologia XP são:comunicação, simplicidade, feedback e coragem.

Comentários:

No início, havia apenas quatro valores- posteriormente, foi adicionado um novo valor:
respeito! Na época dessa questão, ainda havia apenas quatro valores.
Gabarito: Correto

46.(CESPE / TCU - 2010) O processo XP (extreme programming) envolve a realização das atividades de planejamento, de projeto, de codificação e de teste.
Comentários:

valores das histórias de usuários critérios de teste de aceitação plano de iteração projeto simples soluções pontuais cartões CRC protótipos refabricacõo programação em dupla
Versão incremento de software velocidade de projeto registrada[computada)

teste de unidades integração contínuo teste de aceitação
Perfeito! Essas são as atividades do Processo XP...

Gabarito: Correto

47. (CESPE / SECONT-ES - 2009) Métodos ágeis de desenvolvimento de sistemas foram propostos principalmente para apoiar o desenvolvimento de aplicações de negócios nas quais os requisitos de sistema mudam rapidamente durante o processo de desenvolvimento. Entre esses métodos está o extreme programming, que envolve um número de práticas, como o planejamento incremental, a definição de um ritmo de trabalho sustentável e a divisão das equipes de trabalho por meio da especialização de seus membros.
Comentários:

A questão está quase toda correta, exceto pela última parte! O XP recomenda que não haja especialização de membros, apresentando uma equipe coesa e multidisciplinar, isto é, todos participam de todas as atividades.
Gabarito: Errado

48. (CESPE / IPEA - 2009) A extreme programming (XP) é um método de desenvolvimento ágil.Nele, os requisitos são expressos como cenários implementados diretamente como uma série de tarefas.
Comentários:

XP é um método ágil? Sim! Os requisitos são expressos como cenários implementados como uma série de tarefas? Sim! Questão bastante comum em concursos!
Gabarito: Correto

49. (CESPE / TRE-MG - 2009) Extreme programming é um método centrado no usuário, na produtividade do desenvolvimento e na documentação de apoio.
Comentários:

Centrado na documentação de apoio? Não! Lembrem-se que não há foco em documentação em metodologias ágeis.
Gabarito: Errado

50.(CESPE / TRE-BA - 2009) A metodologia XP prevê valores e princípios básicos para serem considerados durante o desenvolvimento de software. Feedback, coragem e respeito são exemplos de valores; mudanças incrementais, abraçar mudanças e trabalho de qualidade são exemplos de princípios básicos.
Comentários:

Perfeito! Valores Fundamentais: Feedback, Coragem, Respeito, Comunicação e
Simplicidade;
Princípios Básicos: Feedback Rápido, Abraçar Mudanças, Presumir Simplicidade,
Mudanças
Incrementais e Trabalho de Qualidade.

Gabarito: Correto

51. (CESPE / ANAC - 2009) Extreme Programming é um modelo de processo de desenvolvimento de software para equipes com grande número de pessoas, que desenvolvem software com base em requisitos vagos e que são modificados rapidamente.
Comentários:

Grande número de pessoas? Não, equipes de pequeno e médio porte!

Gabarito: Errado

52. (CESPE / ANTAQ - 2009) O extreme programming (XP) constitui método ágil de desenvolvimento de software. Uma das práticas que se enquadram nos princípios dos métodos ágeis é a programação em pares, que promove o compartilhamento da autoria do código do sistema. Além dessa vantagem, a programação em pares atua como processo informal de revisão porque cada linha de código é vista por pelo menos duas pessoas.
Comentários:

Perfeito! A Programação em Par promove a Propriedade Coletiva! Além disso, serve como uma revisão informal.
Gabarito: Correto

53.(CESPE / PRODEST - 2008) Projetar detalhadamente todo o software antes de iniciar a sua implementação é uma prática recomendada pelo XP. O software deve ser projetado para atender tanto aos requisitos atuais quanto aos potenciais requisitos futuros. Para atingir esse objetivo, são analisados os possíveis cenários de evolução futura e são empregados padrões de projeto para facilitar a manutenção.
Comentários:

Projetar detalhadamente? Não! O Manifesto Ágil já dizia: responder a mudanças é mais valorizado do que seguir um plano específico.
Gabarito: Errado

54.(CESPE / PRODEST - 2008) Constituem práticas recomendadas pelo XP a colocação rápida de uma versão simples em produção, a liberação das novas versões em curtos intervalos de tempo,a programação em duplas, a refatoração (refactor) dos códigos produzidos, a adoção de padrões para a codificação; a integração e o teste contínuos de códigos; a limitação em 40horas da carga de trabalho semanal.
Comentários:

Perfeito! Todas essas são práticas recomendadas pelo XP!

Gabarito: Correto

55. (CESPE / PRODEST - 2008) O XP é um processo que visa a um desenvolvimento ágil e portanto não recomenda os testes de unidade, pois eles consomem muitos recursos.Durante o desenvolvimento, o primeiro teste recomendado é o smoke test que foca os detalhes de funcionamento. O smoke test é realizado após as unidades serem integradas. Após o smoke test, é realizado o teste de sistema.
Comentários:

Como é? XP recomenda veementemente a utilização de testes de unidade!

Gabarito: Errado

QUESTõES CoMENTADAS - FCC

í. (FCC /SANASA Campinas -2019) Em um projeto de software baseado na metodologia ágilXP,
um Analista de TI deve a) consultar o cliente quando uma história exigir, por estimativa, menos do que 3semanas de desenvolvimento, para que o cliente a complemente com mais tarefas.
b) ouvir o cliente, durante o levantamento de requisitos, para que este crie as histórias de usuários. Após essa importante etapa nenhuma história nova deve ser criada para não comprometer o cronograma do projeto.
c) evitar que o projeto caia na armadilha de seguir o princípio KISS de forma a estimular que o projeto de uma funcionalidade extra, que poderá ser necessária no futuro, faça parte do modelo do software.
d) realizar os testes de unidade de forma manual, evitando que sejam usadas baterias de testes automatizados, pois estes impedem a realização de testes de regressão.
e) estimular o uso de cartões CRC como um mecanismo eficaz para pensar o software em um contexto orientado a objetos.
Comentários:

Para Pressman: "A XP estimula 0 uso de cartões CRC como um mecanismo eficaz para pensar 0software em um contexto orientado a objetos. Os cartões CRC
(classe-responsabilidade-colaborador)
identificam e organizam as classes orientadas a objetos relevantes para 0 incremento de software corrente".
Gabarito: Letra E

2. (FCC / DPE-AM - 2018) Considere a definição de algumas práticas da eXtreme
Programming -
XP.

I. Todo o código desenvolvido pelo time é incorporado em um repositório comum várias vezes ao dia. Isso garante que qualquer problema de integração ao longo do projeto possa ser notado e corrigido rapidamente.
II. Qualquer programador do time pode alterar qualquer seção do código, se necessário.
Por mais que esta prática pareça perigosa, ela aumenta a velocidade do desenvolvimento e problemas em potencial podem ser detectados pelos testes de unidade.
III. Traz a ideia de que qualquer pessoa do time seja capaz de verificar o código sendo desenvolvido em alto nível e ter uma compreensão clara de qual funcionalidade do sistema está sendo trabalhada.
IV. Permite aplicar melhorias ao código sem mudar sua funcionalidade,
visando sua simplificação. Se o cliente deseja alterar alguma coisa no produto final, o time pode fazer os ajustes rapidamente, e esta prática contribui para alcançar este objetivo.
As práticas de I a IV são, correta e respectivamente,

a) pair programming -test-driven development-system metaphor-continuous integration.

b) planning game-pairprogramming-system simplicity-continuous integration.

c) planning game-test-driven development-system simplicity-refactoring.

d) continuous integration - pair programming -feedback- planning game.

e) continuous integration -collective code ownership -system metaphor- refactoring.

Comentários:

(I) Trata-se da prática de Integração Contínua, que diz que tão logo o trabalho em tarefa seja concluído, este é integrado ao sistema, são também realizados testes unitários; (II)Trata-se da prática da Propriedade Coletiva do Código, ou seja, o código pertence a todos os integrantes da equipe, além disso, essa prática aumenta a velocidade de desenvolvimento; (III) Trata-se da prática das Metáforas, que visa facilitar a comunicação entre os membros da equipe, de forma que sejam transmitidas ideias complexas de maneira simples; (IV) Por fim, melhorar o código sem afetar o comportamento externo do sistema, trata-se da prática de refatoramento.
Gabarito: Letra E

3. (FCC /TST-2017) Uma dupla de programadores, utilizando o modelo Extreme Programming
-
XP, realiza, na fase de:

a) desenvolvimento, a implementação das user stories que fazem parte da iteração corrente.

b) desenvolvimento, a entrega das user stories totais do sistema.

c) validação do sistema, a análise dos requisitos técnicos entregáveis.

d) validação do sistema, a integração total dos incrementos das user stories.

e) projeto da arquitetura do sistema, a implementação das user stories totais do sistema.

Comentários:

No XP, todos os requisitos são expressos como histórias do usuário, que são implementados diretamente como uma série de tarefas. Além disso, essa implementação ocorre na fase de desenvolvimento.
Gabarito: Letra A

4. (FCC / DPE-RS - 2017) Considere que um Analista esteja participando de um projeto que utiliza as melhores práticas da Extreme Programming - XP. No início de uma iteração a equipe de desenvolvimento, da qual o Analista fazia parte, convidou o cliente a escrever as funcionalidades que desejava no sistema em pequenos cartões chamados user stories. Depois disso, a equipe de desenvolvimento estimou o tempo e o custo de cada funcionalidade para o cliente. Ocliente foi informado do tempo e custo, e foi solicitado a decidir a prioridade em que cada user story deveria ser desenvolvida. Esta prática XP é conhecida como:
a) Releases e é utilizada para que o cliente possa utilizar o sistema, possibilitando à equipe de desenvolvimento saber se há defeitos ou não no código.
b) Releases e visa reorganizar o código fonte para melhorar sua qualidade interna,
facilitar seu entendimento pelo cliente e diminuir o tempo gasto com manutenção.
c) Metáforas e permite que o cliente transmita ideias complexas de forma simples e clara,usando um vocabulário comum.

d) Planning Game e permite que o Analista e outro desenvolvedor escolham uma user story e codifiquem juntos aquela funcionalidade.
e) Planning Game e busca assegurar que a equipe esteja sempre trabalhando no que é mais importante e gere mais valor para o cliente.
Comentários:

O cliente escreve as funcionalidades em um cartão chamado user stories: trata-se da prática do jogo do planejamento (planning game). Ou seja, o planejamento dos releases e das iterações é feito com base nas prioridades do cliente, o trabalho dos desenvolvedores é avaliar e estimar as entregas dessas prioridades.
Gabarito: Letra E

5. (FCC / CREMESP - 2016) Considere que nos projetos do CREMESP baseados em XP
pratica-se a propriedade coletiva de código, de forma que todos os desenvolvedores podem fazer alterações e refatoração de qualquer parte do código a qualquer momento. Para isso, é necessário que também haja:
a) padrões de codificação.

b) time-box de 40 horas.

c) testes apenas depois da codificação.

d) releases grandes.

e) integração das funcionalidades, mesmo com erros.

Comentários:

A codificação é a principal atividade no XP, além disso, os programadores trabalham em pares e a propriedade do código é coletiva. Por isso, é necessário que haja uma padronização na elaboração do código.
Gabarito: Letra A

6. (FCC / Prefeitura de Teresina - PI - 2016) Os métodos ágeis de desenvolvimento de software como eXtreme Programming - XP consideram um conjunto de valores fundamentais derivados do manifesto ágil. Assim, estes métodos valorizam MENOS:
a) os indivíduos e a interação entre eles, do que os processos e ferramentas.

b) o software funcionando, do que uma documentação abrangente.

c) a colaboração com o cliente, do que negociação de contratos.

d) a resposta rápida a mudanças, do que seguir um plano previamente definido.

e) a rigorosidade dos processos, do que a adaptação às mudanças.

Comentários:

Primeiramente, vê se que a questão pede os fundamentos que o Manifesto Ágil valoriza menos. OManifesto Ágil valoriza mais a resposta às mudanças do que seguir um plano, por isso,
ele valoriza menos a rigorosidade dos processos do que a adaptação às mudanças. Arigorosidade dos processos está mais ligada às metodologias tradicionais.
Gabarito: Letra E

7. (FCC / TRE-PB- 2015) Extreme Programming - XP pode ser considerado um modelo de desenvolvimento de software baseado em uma série de valores, princípios e regras, dentre eles,
a) criar obrigatoriamente uma matriz de rastreabilidade de requisitos.

b) manter o foco na documentação, detalhada e diversificada.

c) definir sprint de no máximo duas semanas.

d) escrever sempre o código, depois, o teste de unidade.

e) realizar semanalmente o jogo do planejamento (planning game).

Comentários:

(a) Errado. Não há essa obrigação; (b) Errado. O XP por ser uma metodologia ágil,
valoriza mais um software em funcionamento do que uma documentação detalhada e diversificada; (c) Errado,na verdade, os incrementos é que são entregues em aproximadamente duas semanas; (d) Errado. O
XP adota o desenvolvimento test-first, ou seja, primeiro escreve-se o teste; (e)
Correto. O planning game pode ocorrer semanalmente.
Gabarito: Letra E

8. (FCC / TST - 2012) O XP (Extreme Programming) utiliza uma abordagem orientada a objetos como seu paradigma de desenvolvimento predileto. Ele:
a) recomenda que duas pessoas trabalhem juntas para criar o código correspondente a uma história.
b) recomenda que a equipe XP e os clientes trabalhem de forma separada para não mudar o compromisso básico definido para a versão a ser entregue.
c) segue rigorosamente o princípio FDD - Feature Driven Development.

d) recomenda que depois que as histórias forem desenvolvidas e o trabalho preliminar do projeto for feito, a equipe XP avance diretamente para o código.
e) inclui um conjunto de regras e práticas que ocorrem no contexto de 3 atividades de arcabouço:projeto, implementação e entrega.

Comentários:

(a) Correto, trata-se da programação em pares; (b) Errado, recomenda-se o cliente on-site, isto é, o cliente está sempre presente para auxiliar com seu conhecimento sobre a área de negócio; (c)Errado, ela segue o TDD - Test-Driven Development; (d) Errado, Pressman afirma que se recomenda desenvolver testes unitários que exercitarão as histórias; (e) Errado, Pressman afirma que XP inclui um conjunto de regras e práticas que ocorrem no contexto de quatro atividades de arcabouço: planejamento, projeto, codificação e teste.
Gabarito: Letra A

9. (FCC / MPE-AP - 2012) O Extreme Programming (XP) é, talvez, o mais conhecido e mais utilizado dos métodos ágeis. Dentre suas práticas se encontram programação em pares,integração contínua, refatoração e:

a) propriedade coletiva, que garante uma participação nos lucros aos membros da equipe de desenvolvimento, técnica que incentiva e aumenta o desempenho de toda a equipe.
b) envolvimento do cliente apenas na fase final do sistema, fator que difere de outras metodologias como SCRUM e TDD e confere agilidade ao processo de desenvolvimento.
c) processo de desenvolvimento contínuo, em que a equipe se mantém focada no sistema até que uma funcionalidade específica seja entregue, comumente agregando horas extras ao turno de trabalho.
d) utilização de técnicas de ofuscação do código fonte, trazendo segurança e garantindo que apenas a equipe de desenvolvimento poderá ter acesso a este código e) desenvolvimento incremental e sustentado por meio de pequenos e frequentes releases do sistema. Os requisitos são baseados em cenários ou em simples histórias de clientes.
Comentários:

(a) Errado. Participação nos lucros? Quem dera! Essa prática significa que todos podem visualizar e editar um código-fonte; (b) Errado, o envolvimento ocorre durante todo o processo; (c) Errado,deve-se manter um ritmo sustentável, evitando horas-extras; (d) Errado. Pelo contrário, quanto mais limpo o código, melhor; (e) Perfeito, não há nada a acrescentar.
Gabarito: Letra E

io.(FCC / MPE-PE - 2012) Dentre as práticas do método ágil Extreme Programming (XP),
está a prática de propriedade coletiva. É correto afirmar que, nessa prática,
a) os trabalhos são desenvolvidos em conjunto, para que um programador possa analisar o trabalho do outro.
b) cada projeto é realizado para atender às necessidades globais dos usuários, focando na coletividade da distribuição da informação.
c) os pares de desenvolvedores trabalham em todas as áreas do sistema, de modo que não se desenvolvam ilhas de expertise.
d) grandes quantidades de horas extras não são consideradas aceitáveis, pois o resultado final,muitas vezes, é a redução da qualidade do código e da produtividade a médio prazo,
sendo que o indivíduo pode afetar o desempenho de todo o time.
e) um representante do usuário final do sistema deve estar disponível todo o tempo à equipe de desenvolvimento. Nesse modelo de desenvolvimento, o cliente é membro da equipe e participa da responsabilidade do código desenvolvido.
Comentários:

(a) Trata-se do Pair Programming; (b) Não sei o que é, mas não há relação com
Propriedade
Coletiva; (c) Trata-se da Propriedade Coletiva; (d) Trata-se do Ritmo Sustentável; (e)
Trata-se do
Cliente On-Site.

Alguns afirmam que a terceira opção está mais para a prática de Pair Programming e,
não, para
Propriedade Coletiva. Eu admito que é um pensamento razoável, mas nenhuma outra opção se encaixa em Propriedade Coletiva. Dessa forma, deve-se ter essa noção nas questões daFCC, isto é,
marcar a mais correta ou a menos errada.

Gabarito: Letra C

11. (FCC/TJ-PE-2012) NoS métodos ágeis XP e Scrum, as entregas de partes funcionais do projeto são divididas em ciclos, geralmente compreendidos no período de 1 a 4 semanas. Estes ciclos denominam-se, respectivamente,
a) iterações e sprint.

b) reunião de planejamento e backlog.

c) período de entrega e reunião de revisão.

d) backlog e planejamento da produção.

e) entrega e retrospectiva.

Comentários:

No XP, temos as iterações; no Scrum, temos a sprint!

Gabarito: Letra A

12.(FCC / TRT-MT - 2011) NÃO se aplica à disciplina de desenvolvimento de software extreme programming (XP):
a) Usa notações próprias para construir os diversos produtos de trabalho do projeto.

b) Encoraja a refabricação para modificar um sofware sem alterar o comportamento externo do código.
c) Recomenda que dois programadores trabalhem juntos no mesmo computador para escrever um código.
d) Baseada em valores de simplicidade, comunicação, feedback e coragem.

e) Adota como um elemento-chave a criação de testes unitários antes da codificação começar.

Comentários:

(a) Errado, não há nenhuma notação própria; (b) Correto, trata-se do Refactoring; (c)
Correto, trata-
se da programação em pares; (d) Correto, há também respeito; (e) Correto,
teste primeiro e codifique depois.
Gabarito: Letra A

13. (FCC / TRE-RN - 2011) Considere as seguintes características:

I. Propriedade coletiva.

II. Integração contínua.

III. Metáfora.

Dentre as práticas componentes da Extreme Programming, aplica-se o que consta em:

a) I, apenas.

b) II, apenas.

c) I e II, apenas.

d) II e III, apenas.

e) I, lie III.

Comentários:

Todas as opções estão corretas: Propriedade Coletiva, Integração Contínua e Metáfora.

Gabarito: Letra E

i4.(FCC/TRT-23-20ii) No desenvolvimento de software em Extreme Programming (XP)
há uma confiança muito grande na sinergia entre as práticas, já que os pontos fracos de cada uma são superados pelos pontos fortes de outras. Dentre elas, aquela em que o código fonte não tem dono e ninguém precisa solicitar permissão para poder modificá-lo, permitindo, assim,que a equipe conheça todas as partes do sistema, é chamada de:
a) Whole Team (Time Coeso).

b) Sustainable Pace (Ritmo Sustentável).

c) Pair Programming (Programação em Pares).

d) Collective Ownership (Posse Coletiva).

e) Coding Standards (Padrões de Codificação).

Comentários:

O código fonte não tem dono e ninguém precisa solicitar permissão para poder modificá-lo,permitindo, assim, que a equipe conheça todas as partes do sistema,
é chamada de
Posse/Propriedade Coletiva (Collective Ownership).

Gabarito: Letra D

15. (FCC / TRE-RN - 2011) Assegurar que a equipe se concentre em fazer, primeiro,
apenas aquilo que é claramente necessário e evite fazer o que poderia vir a ser necessário, mas ainda não se provou essencial. Este é um dos cinco valores fundamentais do XP (Extreme Programming),denominado:

a) coragem.

b) respeito.

c) comunicação.

d) simplicidade.

e) feedback.

Comentários:

Fazer o necessário e essencial é exatamente o valor da simplicidade.

Gabarito: Letra D

16.(FCC / TRE-RS - 2010) No eXtreme Programming, XP:

a) o código é integrado e testado depois de alguns dias e, no máximo, até o final da semana.

b) a codificação é feita em grupos de programadores (no mínimo 3
integrantes),
preferencialmente num único computador.

c) as equipes de desenvolvimento estabelecem suas próprias regras, mas uma equipe pode adotar as regras de outra equipe.
d) releases quando complexos não podem deixar de fora os requisitos de negócio de maior valor para o cliente.
e) módulos não são propriedade de nenhum desenvolvedor; todo desenvolvedor da equipe tem o direito de checar um módulo e modificá-lo.
Comentários:

(a) Errado, recomenda-se a integração sempre que possível; (b) Errado, é feita por um par de programadores; (c) Errado, as equipes são auto-organizáveis de acordo com as suas habilidades,
logo não faz sentido se organizar de acordo com outra equipe; (d) Errado, releases devem ser simples e, não, complexas; (e) Correto, o código é compartilhado.
Gabarito: Letra E

i7.(FCC / MPE-RN - 2010) Refactoring, programação em pares e Stand-up
Meeting são características das práticas do:
a) PRINCE2.

b) Rational Unified Process.

c) Extreme programming.

d) PMBOK.

e) SCRUM.

Comentários:

Refactoring (Refatoração), Pair-Programming (Programação em Pares) e Standup
Meeting
(Reuniões em Pé) são todas práticas do XP.

Gabarito: Letra C

i8.(FCC/TJ-PI-2oog)XP (eXtreme Programming) é uma metodologia ágil para equipes pequenas e médias que desenvolverão software com requisitos vagos e em constante mudança. Para isso,adota a estratégia de constante acompanhamento e realização de vários pequenos ajustes durante o desenvolvimento de software. Para aplicar os valores e princípios durante o desenvolvimento de software, a XP propõe uma série de práticas, sendo uma delas:sempre que produzir uma nova funcionalidade, nunca esperar uma semana para integrar à versão atual do sistema a fim de evitar o aumento da possibilidade de conflitos e da possibilidade de erros no código fonte. Tal prática é denominada:
a) Time Coeso.

b) Refatoração.

c) Integração Contínua.

d) Desenvolvimento Orientado a Testes.

e) Ritmo Sustentável.

Comentários:

Essa é a prática da Integração Contínua! É comum a utilização de servidores de integração contínua que automatizam esse processo para os desenvolvedores.
Gabarito: Letra C

ig.(FCC / TCE-AL - 2008) Originalmente, o único produto da atividade de Projeto que é realizado como parte do processo XP (Extreme Programming):
a) é a definição do caso de uso de contexto.

b) são os cartões CRC.

c) são os diagramas de objetos.

d) são os diagramas de sequência.

e) é a codificação, feita em pares.

Comentários:

Pressman afirma: "Como 0 projeto XP praticamente não usa nenhuma notação e produz poucos, ou nenhum produto de trabalho que não sejam os cartões CRC e as soluções de ponta, 0projeto é visto como um artefato provisório que pode e deve sercontinuamente modificado à medida que a construção prossegue". Dessa forma, trata-se dos Cartões CRC.
Gabarito: Letra B

2O.(FCC/TRE-SE-2OO7) Na XP (eXtreme Programming):

a) deve-se usar o modelo em cascata para o desenvolvimento do software.

b) os programadores desenvolvem o software criando primeiramente os testes.

c) deve ser evitada a comunicação pessoal entre clientes e desenvolvedores, sempre dando preferência a outros meios de comunicação mais formais.
d) os programadores desenvolvem o software fazendo todos os testes possíveis no término do desenvolvimento.
e) deve-se projetar todas as funções possíveis com a máxima previsão do que ocorrerá no futuro,antes do desenvolvimento do software, a fim de evitar alterações desnecessárias.

Comentários:

(a) Errado, esse item não faz o menor sentido; (b) Correto, testa-se primeiro,
codifica-se depois; (c)
Pelo contrário, deve-se estimular a comunicação pessoal entre clientes e desenvolvedores e evitar outros meios mais formais; (d) Errado, testes são feitos a todo momento; (e) Errado.Pelo contrário,
XP lida bem com mudanças.

Gabarito: Letra B

QUESTõES CoMENTADAS - FG V

í. (FGV/ SEFAZ-BA- 2022) Com relação à programação por pares, analise as afirmativas a seguir e assinale (V) para a verdadeira e (F) para a falsa.
() É uma prática proposta no método ágil, onde programadores (um experiente e um novato)atuam no desenvolvimento de código-fonte.

() Requer uma mudança cultural. A prática consiste em uma pessoa programando enquanto a outra atua como revisor.
( ) Este tipo de programação não exemplifica uma prática de construção colaborativa de modelos e de elaboração de código-fonte.
As afirmativas são, na ordem apresentada, respectivamente,

a) F-V-F.

b) V-V-F.

c) F-F-V.

d) V-F-V.

e) V-F-F.

Comentários:

(V) Ela realmente foi proposta pelo XP e é comum a organização com um programador experiente e um novato; (V) De fato, requer uma mudança cultural e um programador realmente age como um revisor do outro; (F) Pelo contrário, trata-se justamente de uma prática de construção colaborativa de modelos e de elaboração de código-fonte.
Gabarito: Letra B

2. (FGV / Prefeitura de Paulínia - SP- 2016) A empresa de desenvolvimento de sistemas "Inovation" tem ampla experiência no mercado e, até o momento,utilizou diversos modelos de ciclo de vida para o desenvolvimento de sistemas. A "Inovation" já recebeu diversas reclamações dos seus clientes por causa da demora em apresentar alguma tela em funcionamento, bem como da falta de envolvimento dos clientes no desenvolvimento. Aempresa, assim, decidiu passar a utilizar um novo modelo de ciclo de vida. Esta decisão visa aproveitar a grande experiência de sua equipe e trazer o cliente para a equipe de desenvolvimento, com iterações de desenvolvimento extremamente curtas. Qualquer membro da equipe implementa parte do código, que pode ser evoluído por qualquer outro membro.O novo modelo adotado pela "Inovation" é denominado:

a) Extremme Programming (XP).

b) Modelo V.

c) Evolutivo.

d) Incremental.

e) Espiral.

Comentários:

A empresa demora a apresentar incrementos visíveis para o usuário e peca na falta de envolvimento com os clientes. Ela deseja utilizar um novo modelo que traz o cliente para perto da equipe e realiza iterações de desenvolvimento extremamente curtas (olha a dica!). Por fim, ela quase dá a resposta para a questão afirmando que qualquer membro da equipe implementa parte do código,que pode ser evoluído por qualquer outro membro.
A questão apresentou diversas características do modelo Extreme Programming (XP):

PRÁTICAS DESCRIÇÃO

PEQUENOS
RELEASES

PROPRIEDADE

COLETIVA

O conjunto mínimo útil de funcionalidade que agrega valor ao negócio é desenvolvido primeiro. Releases do sistema são frequentes e adicionam funcionalidade incrementalmente ao primeiro release.
Os pares de desenvolvedores trabalham em todas as áreas do sistema, de tal maneira que não se formem ilhas de conhecimento, com todos os desenvolvedores de posse de todo o código. Qualquerum pode mudarqualquercoisa.
Um representante do usuário final do sistema deve estar disponível em tempo integral para apoiara equipe. No XP, o cliente é um membro da equipe de desenvolvimento e é responsável portrazeros requisitos do sistema.
Gabarito: Letra A

3. (FGV / Câmara Municipal do Recife-PE - 2014) Uma das práticas do método ágil XP
(eXtreme
Programming) é:

a) documentação extensiva;

b) prototipação;

c) ciclos longos de desenvolvimento;

d) desenvolvimento orientado a testes (TDD);

e) utilização de todos os artefatos do RUP.

Comentários:

O TDD é uma prática XP em que se escreve o teste antes de escrever o código do componente.

Gabarito: Letra D

QUESTõES CoMENTADAS - DIvERSAS BANCAS

í. (COMPERVE ITJ-RN - 2020) O método ágil Extreme Programming ou XP é um dos métodos ágeis mais conhecidos. Sobre as características desse método, é correto afirmar:
a) o planning game é uma reunião que ocorre a cada iteração com o objetivo de discutir o que foi feito na última iteração.
b) o código fonte que será executado no ambiente de produção é desenvolvido em pares,
sendo que o par se alterna nos papéis de condutor e navegador.
c) é importante tentar prever o que o cliente deseja e executar antes mesmo de comunicá -lo,mostrando proatividade na resolução de possíveis problemas.

d) o código fonte de cada página pertence a um membro da equipe. Qualquer alteração a ser realizada precisa ser informada ao respectivo membro.
Comentários:

(a) Errado. Na verdade, o planning game é uma reunião de planejamento para discutir o que será feito; (b) Correto. Desenvolvedores trabalham em pares, um verificando o trabalho do outro; (c)Errado. No XP, o envolvimento do cliente ocorre em tempo integral; (d) Errado. XP
valoriza o trabalho em equipe e, por isso, o código fonte pertence a equipe.
Gabarito: Letra B

2. (IBFC /TRE-PA -2020) Para aplicar valores e princípios do XP (Extreme Programming),
durante os processos e práticas ágeis de desenvolvimento de software, se propõe uma série específica de práticas. Assinale a alternativa que apresenta algumas dessas "boas práticas" utilizadas tradicionalmente em projetos, usando XP.
a) Reformation - Pair Programming - PlayStation Game b) Refactoring - Pair Programming - Planning Game c) Reformation - Pair Production - Planning Game d) Refactoring - Pair Production - PlayStation Game
Comentários:

- Não existe prática chamada reformation e, sim, refactoring;

- Não existe prática chamada pair production e, sim, pair programming;

- Não existe prática chamada PlayStation game e, sim, planning game.
Logo, trata-se de: Refactoring, Pair Programming e Planning Game.

Gabarito: Letra B

3- (UFCG/ UFCG- 2019) Marque a alternativa INCORRETA com relação a
Extreme
Programming (XP).

a) Comunicação, coragem e respeito são valores dessa metodologia.

b) Em XP, uma das regras é codificar os testes de unidade primeiro.

c) Refatoramento é uma prática recomendada nesse processo.

d) O código a ser enviado para produção é criado por duas pessoas trabalhando juntas em um único computador.
e) O autor, Don Wells, exige que o processo seja seguido à risca, de forma que todas suas regras devem ser respeitadas e, nenhum projeto pode ser realizado sem adaptações e/ou remoção dessas regras.
Comentários:

(a) Correto. Todos são valores do XP; (b) Correto, primeiro se escreve o teste,
depois faz-se a implementação; (c) Correto. A refatoração é uma prática recomendada no XP; (d) Correto.No XP,
o desenvolvimento ocorre em pares; (e) Errado. Pelo contrário, organizações não precisam seguir tudo à risca - podem adaptar o processo.
Gabarito: Letra E

4. (IDECAN / UNIVASF - 2019) Extreme Programming (XP), em sua essência, possui um conjunto de regras que devem ser seguidas em projetos ágeis que queiram utilizá-la em sua completude.Sobre as regras do XP, assinale a alternativa correta.

a) Apenas as operações mais críticas devem possuirtestes unitários.

b) Todo o código-fonte de produção deve ser implementado em programação em pares.

c) A integração de código deve ser feita nos computadores dos desenvolvedores.

d) É importante estabelecero papel de umXP Master, que será responsável pela implementação da metodologia.
e) A velocidade do projeto deve ser medida com o objetivo de informarão cliente o tempo médio de correção de falhas.
Comentários:

(a) Errado. No XP, são desenvolvidos testes para cada uma das tarefas; (b) Correto. No
XP, uma das características é a programação em pares; (c) Errado. A integração de código é feita em um sistema;
(d) Errado. Não há o papel de XP Master no XP; (e) Errado. No XP, o envolvimento do cliente é em tempo integral.
Gabarito: Letra B

5- (CESGRANRIO / UNIRIO - 2019) Uma das principais práticas de XP (Extreme
Programming) é o Iteration Planning Game. Entre as atividades realizadas em uma sessão de IterationPlanning,
está a:

a) definição, pelos programadores, de quais story cards serão implementados em uma iteração.

b) estimação do esforço que será necessário para implementar cada story card.

c) estimação da data de entrega de um release baseado na estimativa de esforço de cada story card.
d) estimação, feita por cada programador, do tempo que será necessário para realizar cada tarefa sob sua responsabilidade.
e) designação, por parte do coach, dos programadores que irão realizar as tarefas contidas na lista de tarefas.
Comentários:

(a) Errado. Na verdade, essa definição é feita pelos clientes; (b) Errado. Ocorre estimação do tempo e, não, do esforço; (c) Errado, não existe a estimativa do esforço; (d) Correto. Cada programador estima o tempo de suas tarefas; (e) Errado. Não existe a figura do coach no XP.
Gabarito: Letra D

6. (INSTITUTO AOCP / UFPB - 2019) Um dos principais métodos ágeis de desenvolvimento de software foi concebido para impulsionar práticas reconhecidas como boas, por exemplo, o desenvolvimento iterativo a nível extremo, em que novas versões de um determinado sistema podem ser implementadas, integradas e, até mesmo, testadas em um único dia por programadores diferentes. Essa é uma das características de qual método de desenvolvimento ágil de software?
a) Scrum.

b) Adaptative Software Development.

c) Extreme Programming.

d) Pramatic Programming.

e) Test Driven Development.

Comentários:

O método de desenvolvimento ágil que permite o desenvolvimento iterativo a nível extremo, em que novas versões de um determinado sistema podem ser implementadas, integradas e, até mesmo, testadas em um único dia por programadores diferentes é o Extreme Programming.
Gabarito: Letra C

7- (FCM / Prefeitura de Caranaíba - MG - 2019) De acordo com Pressman e Maxim
(2016), a
Programação Extrema (Extreme Programming -XP) é uma abordagem amplamente utilizada do desenvolvimento ágil de software que consiste das atividades:
a) Planejamento (Planning) / Projeto (Designing) / Codificação (Coding) / Teste (Test).

b) Colaboração (Collaboration) / Projeto (Designing) / Codificação (Coding) / Teste (Test).

c) Colaboração (Collaboration) / Projeto (Designing) / Codificação (Coding) /
Teste (Test) /
Adaptação (Adaptation).

d) Colaboração (Collaboration) / Projeto (Designing) / Codificação (Coding) /
Teste (Test) /
Adaptação (Adaptation) / Melhoria (Improvement).

Comentários:

projeto simples soluções pontuais cartões CRC protótipos
Trata-se do Planejamento (Planning), Projeto (Designing), Codificação (Coding) e Teste (Test).

Gabarito: Letra A

8. (VUNESP / Câmara de Piracicaba - SP-2019) Um dos processos ágeis de desenvolvimento de software é a programação extrema (extreme programming - XP), cuja fase ou atividade inicial é composta pela descrição dos cenários (características e funcionalidades)requisitadas para o software a ser desenvolvido. Essa atividade recebe a denominação de:
a) métodos práticos.

b) histórias de usuário.

c) estruturas de apoio.

d) classes de projeto.

e) artefatos de usuário

Comentários:

De acordo com Sommerville, a primeira atividade do ciclo de uma release é "selecionar histórias de usuário para esta release"-não é exatamente o nome da atividade, mas é o que mais se aproxima!
Gabarito: Letra B

9. (INSTITUTO AOCP / ADAF - AM - 2018) Na metodologia ágil Extreme Programming (XP),
a propriedade do código é coletiva, dessa forma, todos compartilham o mesmo orgulho e as mesmas críticas. Considerando o exposto, assinale a alternativa que apresenta uma das regras da codificação em XP.
a) No Overtime.

b) Eliminar gargalos de hardware no início.

c) O usuário não deve participar do planejamento das interfaces.

d) No Outsourcing.

e) No Sprint.

Comentários:

O XP tem como uma de suas práticas o ritmo sustentável, dessa forma, grandes quantidades de horas extras não são consideradas aceitáveis. Overtime está relacionado a horas extras, dessa forma, é uma prática que não deve ser adotada. As demais alternativas não têm relação com o XP.
Gabarito: Letra A

10.(AOCP / SUSIPE-PA- 2018) Sobre as práticas do XP (Extreme Programming),
assinale a alternativa INCORRETA.
a) O cliente deve conduzir o desenvolvimento a partir do feedback que recebe do sistema.

b) O código deve ser padronizado, visando tornar o sistema mais homogêneo.

c) O XP trabalha com releases curtos, buscando a integração contínua de valor para o cliente.

d) O XP trabalha com código coletivo, no qual todos os membros da equipe têm acesso ao código.
e) O XP utiliza-se de programação em par para permitir que o código seja revisado permanentemente enquanto é desenvolvido.
Comentários:

A banca deu a alternativa (d) como incorreta, mas eu acredito que caberia recurso. O
XP valoriza o trabalho em equipe e, por isso, o código fonte pertence à equipe - as demais alternativas são também práticas adotadas no XP.
Gabarito: Letra D

n.(COMPERVE / UFRN-2018) Programação Extrema (XP - Extreme Programming) é uma das principais metodologias ágeis já propostas. A respeito de XP, considere as afirmativas abaixo.
I XP promove a execução de testes automatizados de avaliação do desempenho a cada iteração de desenvolvimento do sistema.
II Em XP, os requisitos do sistema são especificados através de casos de uso.

III A prática de integração contínua do XP envolve a geração frequente de versões
(builds) do sistema, assim como execução dos testes automatizados sobre as versões geradas.
IV A prática de refatoração do XP envolve a modificação interna do código de classes do sistema,mas sem modificar seu comportamento externo (interfaces dos métodos).

Estão corretas as afirmativas a) III e IV.
b) I e II.

c) I e III.

d) lie IV.

Comentários:

(I) Errado. Testes automatizados são realizados a cada entrega; (II) Errado. No XP, os requisitos de sistema são especificados por meio de histórias de usuários; (III) Correto. O XP adota a prática de integração contínua e de testes automatizados; (IV) Correto. O XP utiliza a refatoração como uma de suas práticas.
Gabarito: Letra A

12. (COMPERVE / UFRN - 2018) Programação Extrema (XP - Extreme Programming) é uma das principais metodologias ágeis já propostas. Considere as seguintes afirmativas a respeito de suas práticas.
I A técnica de refatoração promove mudanças no código que visam à adição de novas funcionalidades.
II XP determina a produção de um executável do sistema desenvolvido a cada iteração.

III XP motiva a criação de projetos simples onde requisitos futuros não são inicialmente contemplados.
IV Integração contínua consiste na geração de builds diários do sistema.

Estão corretas as afirmativas a) lie IV.
b) I e IV.

c) I e III.

d) lie III.

Comentários:

(I) Errado. A refatoração é a modificação interna do código sem alterar seu comportamento externo; (II) Correto. Refere-se à prática do lançamento de pequenos releases; (III)Correto. De fato,
uma das práticas adotadas pelo XP é a dos projetos simples; (IV) Errado. Logo que o trabalho em uma tarefa é concluído, ele é integrado ao sistema, mas não há essa relação com builds diários.
Gabarito: Letra D

13. (IF-RS / IF-RS - 2018) Sobre as práticas encontradas na metodologia ágil de desenvolvimento de software, conhecida por Programação Extrema (XP Programming), de acordo com Dooley(2017) no livro Software Development, Design and Coding, classifique cada uma das afirmativas abaixo como verdadeira (V) ou falsa (F) e assinale a alternativa que apresenta a sequênciaCORRETA, de cima para baixo:

() Participação intensa do representante do cliente no desenvolvimento do projeto.

() Testes são realizados continuamente. Quando todos os testes forem aprovados, o módulo foi concluído.
() Programação em par: enquanto um escreve o código, o outro monitora falhas, realiza testes,faz sugestões e planeja próximas ações.

() Lançamentos frequentes de novas versões.

a) F-V-V-F

b) V-F-F-V

c) V-V-F-V

d) V-V-V-V

e) F-F-V-V

Comentários:

No XP, temos o envolvimento em tempo integral do cliente, por isso o item I é verdadeiro. Osegundo item também é verdadeiro e está de acordo com a prática da Integração
Contínua. O
terceiro item também é verdadeiro, de fato, no XP é adotada a prática da programação em pares.Por fim, o último item também é verdadeiro e remete à prática de pequenos releases.

Gabarito: Letra D

i4.(IADES/ ARCON-PA- 2018) Um dos métodos de desenvolvimento de software mais conhecido e utilizado é o extreme programming (XP). Esse consiste em um modelo:
a) que evita a refatoração de código.

b) que realiza testes de integração apenas ao final de todo o desenvolvimento.

c) que valoriza o trabalho de forma individualizada, evitando a programação em pares.

d) que busca atenderás necessidades atuais, e nada mais.

e) no qual não se faz necessária a disponibilidade de um representante do cliente a todo o tempo.
Comentários:

(a) Errado, o XP utiliza a refatoração; (b) Errado, utiliza durante todo o desenvolvimento; (c) Errado,valoriza a propriedade coletiva e a programação em pares; (d) Correto, de fato, busca atender as necessidades atuais; (e) Errado, o envolvimento do cliente ocorre em tempo integral.
Gabarito: Letra D

15. (FAURGS / TJ-RS - 2018) Considere as seguintes afirmações sobre princípios ou práticas da XP(Extreme Programming).

I - Um representante do usuário final do sistema (cliente) deve estar disponível todo o tempo à equipe de XP. Em um processo de Extreme Programming, o cliente é um membro da equipe de desenvolvimento e é responsável por levar ao grupo os requisitos de sistema para implementação.
II - Todos os desenvolvedores devem refatorar o código continuamente, assim que encontrarem oportunidades de melhorias de código.
III - Os desenvolvedores trabalham em todas as áreas do sistema, de modo que não se desenvolvam ilhas de expertise. Todos os desenvolvedorestêm responsabilidade em relação ao código; qualquer um pode mudar qualquer coisa.
Quais estão corretas?

a) Apenas I.

b) Apenas I e II.

c) Apenas I e III.

d) Apenas II e III.

e) I, lie III.

Comentários:

(I) Perfeito! Trata-se do Client On-Site, ou seja, o cliente no local de trabalho, junto dos desenvolvedores.
(II) Isso mesmo! A Refatoração também é uma prática recomendada pelo XP - sempre que o desenvolvedor encontrar uma oportunidade de refatorar o código, recomenda-se fazê-lo.
(III) Corretíssimo! As equipes devem ser multidisciplinares -todo mundo modela,
desenvolve, testa,
implanta, etc. Sem ilhas de expertise porque isso pode causar dependência de um determinado membro da equipe.
Gabarito: Letra E

i6.(FUNRIO / Câmara de São João de Meriti - RJ - 2018) A figura abaixo ilustra a metodologiaExtreme Programming (XP) que usa uma abordagem orientada a objetos, incluindo um conjunto de regras e práticas que ocorrem ao longo do desenvolvimento do projeto.
As fases I, II, III e IV são denominadas respectivamente:

a) modelagem, construção, implantação e homologação.

b) planejamento, construção, codificação e homologação.

c) planejamento, projeto, implantação e teste.

d) planejamento, projeto, codificação e teste.

e) modelagem, projeto, codificação e homologação.

Comentários:

As fases são planejamento, projeto, codificação e teste.

Gabarito: Letra D

17. (INSTITUTO AOCP / PRODEB - 2018) O método de desenvolvimento ágil denominado de XP
(Extreme Programming) tem sua estrutura baseada em algumas prerrogativas, dentre as quais,é correto citar como princípios do XP:

a) Princípio da Legalidade, Princípio da Agilidade e Princípio do Feedback.

b) Princípio da Coragem, Princípio da Agilidade e Princípio da Simplicidade.

c) Princípio da Comunicação, Princípio da Simplicidade, Princípio do Feedback e
Princípio da
Coragem.

d) Princípio da Agilidade, Princípio da Qualidade, Princípio do Feedbacke Princípio da Coragem.

e) Princípio da Simplicidade, Princípio do Desenvolvimento e Princípio de Governança.

Comentários:

VALORES
FUNDAMENTAIS

COMUNICAÇÃO

SIMPLICIDADE

DESCRIÇÃO

Para se desenvolver um sistema de software, exige-se comunicar os requisitos de sistema para os desenvolvedores. Em metodologias formais de desenvolvimento de software, esta tarefa é realizada por meio de documentação. O Extreme Programming favorece projetos simples,metáforas comuns, a colaboração dos usuários, programadores e outros stakeholders, a comunicação verbal frequente e o feedback.
XP incentiva que se comece com a solução mais simples. Funcionalidades adicionais podem ser acrescentadas posteriormente. Alega-se que desenvolver funções que não são necessárias hoje pode ser prejudicial, na medida em que futuramente essa função pode não ser mais útil.Codificação e projeto de necessidades futuras incertas implicam o risco de gastar recursos em algo não mais necessários, embora talvez atrasando aspectos cruciais.
O feedback ocorre quando os testes unitários ou testes de integração retornam o estado do sistema após a implementação das mudanças. Ademais, como os clientes participam do desenvolvimento detestes, eles podem dar um feedback instantâneo. Dessa forma, o cliente pode orientar o desenvolvimento em uma possível recodificação do sistema. Quando o cliente traz um novo requisito, recebe um feedback de tempo e orçamento.
A coragem permite que os desenvolvedores se sintam confortáveis com ao refatorar o seu código,
quando necessário. Eventualmente, há de se ter coragem para jogar fora um código ou para remover um código obsoleto, não importa quanto esforço e tempo se gastou para produzi-lo. Além disso, coragem significa persistência, pois um programador pode se encontrar preso em um problema complexo durante um dia inteiro sem conseguir resolver.
Aqui se inclui o respeito pelos outros, assim como o auto-respeito. Membros devem respeitar seu próprio trabalho, sempre se esforçando para oferecer alta qualidade e buscando o melhor projeto para a solução através de refatoração. Ninguém na equipe deve se sentir desvalorizado ou ignorado. Isso garante um alto nível de motivação e incentiva a lealdade dentro da equipe. Este valor é muito dependente dos outros valores.
Na verdade, o ideal seria chamar de valores fundamentais e, não, princípios do XP. De toda forma,trata-se do princípio da comunicação, princípio da simplicidade, princípio do feedback e princípio da coragem.
Gabarito: Letra C

18.(INSTITUTO AOCP / PRODEB- 2018) O Pair Programming (Programação em Pares)
é uma característica de um determinado método de desenvolvimento de software em que dois programadores trabalham juntos no desenvolvimento de um código. Qual foi o método que criou essa prática?
a) Lean.

b) XP.

c) Scrum.

d) FDD.

e) Cascata.

Comentários:

O método ágil que criou essa prática foi o XP!

Gabarito: Letra B

19.(INSTITUTO AOCP / UFOB- 2018) Uma das práticas do Extreme Programming é o uso do código coletivo, na qual todos os desenvolvedores têm acesso ao código.
Comentários:

De fato, essa é uma das práticas do XP! Os pares de desenvolvedores trabalham em todas as áreas do sistema, de tal maneira que não se formem ilhas de conhecimento, com todos os desenvolvedores de posse de todo o código. Qualquer um pode mudar qualquer coisa.
Gabarito: Correto

2O.(IBADE/IPM - JP-2018) Metodologias ágeis podem ser aplicadas para facilitara adaptação do processo de desenvolvimento de software a mudanças. Trata-se de uma abordagem de desenvolvimento de software ágil amplamente conhecida e utilizada, denominada:
a) desenvolvimento direto.

b) modelagem extrema.

c) programação dinâmica.

d) modelagem direta.

e) programação extrema.

Comentários:

A única alternativa que apresenta uma abordagem de desenvolvimento de software ágil amplamente conhecida e utilizada é a programação extrema (ou extreme programming).
Gabarito: Letra E

21. (INSTITUTO AOCP/ PRODEB - 2018) Extreming Programming (XP) é um método de desenvolvimento ágil amplamente utilizado pelas software houses. Com base neste método,qual alternativa a seguir possui uma prática que NÃO faz parte do XP?

a) Small Releases (Pequenas Entregas).

b) Pair Programming (Programação em Pares).

c) Sprint Review (Reunião de revisão da Sprint).

d) Sustainable Pace (Ritmo Saudável).

e) Collective Owership (Posse Coletiva).

Comentários:

Todas as alternativas apresentam práticas do XP, exceto sprint review - que é uma cerimônia doScrum e, não, do XP.

Gabarito: Letra C

22. (IBFC / TJ-PE - 2017) Está sendo implementado o XP (eXtreme Programming) em uma equipe de TL Para tanto, está sendo colocada a seguinte série de práticas específicas da metodologiaXP em análise:

I. Programação Pareada (Pair Programming).

II. Fases pequenas (Small Releases).

III. Refatoração (Refactoring).

IV. Jogo de Planejamento (Planning Game).

Com base no seu conhecimento sobre a metodologia citada acima, suas práticas específicas estão corretamente relacionadas nos itens:
a) I, II e III, apenas b) I, II e IV, apenas c) II, III e IV, apenas d) I, III e IV, apenas e) I, II, III e IV
Comentários:

O XP utiliza como prática a programação em pares, pequenos releases, refatoração e o jogo do planejamento -todos os itens estão corretos.
Gabarito: Letra E

23.(UFG/SANEAGO-2oi7) Dentro do framework Extreme Programming (XP), uma metodologia ágil, a ação de teste de código é responsabilidade da pessoa:
a) diretamente ligada à criação do artefato em questão.

b) responsável pela equipe de teste de software, que não pode ser a pessoa que o desenvolve.

c) utilizadora do código diariamente.

d) facilitadora da comunicação entre a equipe de desenvolvimento e o cliente.

Comentários:

(a) Errado. Regra clássica: quem desenvolve, não teste e quem testa, não desenvolve!
Logo, a ação de teste não é de responsabilidade ad pessoa diretamente ligada à criação do artefato;(b) Errado,
lembrem-se que no XP a equipe é multidisciplinar, logo não existe uma equipe dedicada de testes;
(c) Errado, não é o cliente que testa - ele apenas homologa posteriormente; (d)
Errado, o teste é realizado pelos desenvolvedores de outras funcionalidades.
Questão anulada sob a justificativa de que o tema não constava do Edital, porém a razão verdadeira
- na minha opinião - é que de que não há resposta correta.

Gabarito: Anulada

2Zf.(IBFC / EBSERH - 2017) Dentro das práticas do XP (eXtreme Programming)
existe uma fundamental que é o Jogo de Planejamento (Planning Game). Para serem realizadas adequadamente essas reuniões com os usuários, deve(m) ter sido feito(s) antecipadamente:
a) o Sustainable Pace b) as Small Releases c) os Customer Tests d) as User Stories e) um Simple Design
Comentários:

Antes de fazer reuniões com os usuários para o jogo do planejamento, deve-se fazer antecipadamente as user stories (histórias de usuário). Caso contrário, não é possível priorizar!
Gabarito: Letra D

25.(COPEVE-UFAL / UFAL - 2016) Assinale a alternativa que contém apenas características ou práticas relacionadas ao método ágil para desenvolvimento de softwares ExtremeProgramming (XP):

a) Planejamento incremental, cliente disponível em tempo integral e programação em pares.

b) Requisitos expressos como cenários, programação incremental e programação individual.

c) Cliente não participa do desenvolvimento, desenvolvimento em cascata e programação em pares.
d) Equipe heterogênea especializada, requisitos expressos como histórias e desenvolvimento em espiral.
e) Toda equipe altera qualquer parte do código, desenvolvimento em cascata e programação individual.
Comentários:

(a) Correto. O XP utiliza uma abordagem incremental, o envolvimento do cliente ocorre em tempo integral e também é adotada a prática da programação em pares; (b) Errado. Aprogramação não é individual; (c) Errado. O envolvimento do cliente ocorre em tempo integral; (d) Errado.Os requisitos são expressos como histórias, mas as outras duas práticas não fazem sentido;(e) Errado. A
programação não é individual e não há relação com desenvolvimento em cascata.

Gabarito: Letra A

26.(IF-PE / IF-PE - 2016) Extreme Programming é uma metodologia ágil para equipes pequenas e médias que desenvolvem software com requisitos vagos e em constante mudança. Sobre os valores do XP, analise as definições abaixo e assinale a alternativa CORRETA.
a) Simplicidade - procura-se que a equipe concentre-se, primeiro, em fazer o necessário.

b) Comunicação - prioriza-se a troca de e-mail como melhor forma de comunicação,independente do horário.

c) Coragem - a metodologia XP prega coragem para dizer "não" ao cliente e evitar mudanças do projeto.
d) Feedback- é valorizado o feedback positivo do cliente. Desta forma,
procura-se evitar a entrega de software sem a realização de testes detalhados.
e) Respeito - prega o respeito à hierarquia, ouvindo e respeitando, apenas, o que é determinado pelo líder de projeto.
Comentários:

(a) Correto. De fato, XP incentiva soluções mais simples, se preocupando primeiramente nas partes essenciais; (b) Errado. O XP valoriza a comunicação verbal frequente; (c) Errado. Na verdade, a coragem refere-se aos desenvolvedores se sentirem confortáveis ao realizarem mudanças no código; (d) Errado. O cliente pode trazer um feedback, mas normalmente o feedback ocorre por meio dos testes unitários ou de integração; (e) Errado. O respeito deve ser um valor amplo, e não deve se limitar ao que é determinado pelo líder do projeto.
Gabarito: Letra A

27. (UFCG / UFCG - 2016) Sobre XP (Extreme Programming), marque a assertiva INCORRETA.

a) É um processo criado por Kent Beck.

b) São exemplos de boas práticas do processo: desenvolvimento orientado a testes, pair programming e documentação em todas as suas fases.
c) Esse processo almeja reduzir o custo de mudanças a partir de múltiplos ciclos de desenvolvimento de curta duração.
d) Simplicidade ao projetar e programar é uma das chaves para o sucesso na visão do XP.

e) Nesse processo, deve-se refatorar o código sempre que possível.

Comentários:

(a) Correto, foi criado por Kent Beck em 1996; (b) Errado, apesar do XP ser orientado a testes e adotar a prática da programação em pares, ele não tem como prática a documentação em todas as fases; (c) Correto, o XP utiliza o desenvolvimento incremental; (d) Correto, o XPincentiva soluções mais simples; (e) Correto, o refatoramento é uma prática adotada.
Gabarito: Letra B

28.(IF-SE / IF-SE - 2016) A Programação Extrema (Extreme Programming - XP) possui diversas práticas. Analise as afirmativas abaixo.
I. As releases do sistema são frequentes e incrementais.

II. Os requisitos são representados através de casos de uso.

III. Os desenvolvedores não trabalham em pares.

IV. Depois de qualquer integração, todos os testes de unidade devem passar.

De acordo com as afirmativas, marque a alternativa CORRETA

a) As afirmativas I e II estão incorretas.

b) Apenas as afirmativas I e II estão corretas.

c) As afirmativas II e III estão incorretas d) As afirmativas III e IV estão incorretas
Comentários:

(I) Correto. O XP adota a prática dos pequenos releases, que são frequentes e incrementais; (II)Errado. Na verdade, são representados pelas histórias de usuários; (III) Errado. Eles trabalham em pares; (IV) Correto. É o que diz a prática da integração contínua.
Gabarito: Letra C

2g.(IF-PE/ IF-PE - 2016) Com relação à metodologia ágil de desenvolvimento de software conhecido como eXtreme Programming (XP), quais são os quatro processos ou atividades metodológicas encontradas nela?
a) Análise, projeto, codificação e teste.

b) Planejamento, análise, projeto e codificação.

c) Planejamento, projeto, codificação e testes.

d) Planejamento, análise, codificação e testes.

e) Levantamento, análise, projeto e codificação.

Comentários:

As atividades são: planejamento, projeto, codificação e testes.

Gabarito: Letra C

3O.(IBFC/ EBSERH - 2016) Equipes XP (eXtreme Programming) planejam utilizando histórias escritas em pequenos cartões. Essas histórias devem ter como objetivo:
a) a modelagem de dados b) as métricas de software c) os requisitos não-funcionais d) os requisitos funcionais e) tanto os requisitos funcionais como os requisitos não-funcionais
Comentários:

Os cartões devem conter os requisitos funcionais do software a ser desenvolvido.

Gabarito: Letra D

3i.(IBFC / EBSERH - 2016) Para aplicar os valores e princípios durante o desenvolvimento de software, a Programação Extrema (eXtreme Programming - XP) propõe uma série de práticas.Selecione a única alternativa que NÃO seja uma dessas práticas:

a) Time Coeso (Whole Team).

b) Design Complexo (Complex Design).

c) Programação Pareada (Pair Programming).

d) Semana de 40 horas (Sustainable Pace).

e) Refatoração (Refactoring).

Comentários:

Todas as alternativas apresentam práticas do XP, exceto design complexo. O XP
preconiza o design/projeto simples em que o projeto é suficientemente simples de modo que atenda aos requisitos atuais e nada mais.
Gabarito: Letra B

32.(IDECAN/ INMETRO - 2015) Na extreme programming, todos os requisitos são expressos como cenários (chamados histórias do usuário) que são implementados diretamente como uma série de tarefas. Sabe-se que o extreme programming envolve um número de práticas que se enquadram nos princípios dos métodos ágeis. Acerca de algumas dessas práticas,relacione adequadamente as colunas a seguir.
1. Releases pequenos.

2. Refactoring.

3. Propriedade coletiva.

4. Integração contínua.

5. Ritmo sustentável.

() Os pares de desenvolvedores trabalham em todas as áreas do sistema, de tal maneira que não se formem ilhas de conhecimento.
( )O conjunto mínimo útil de funcionalidade que agrega valor ao negócio é desenvolvido primeiro.
() Grandes quantidades de horas-extras não são consideradas aceitáveis, pois, no médio prazo,há uma redução na quantidade de código e na produtividade.

( ) Espera-se que todos desenvolvedores recriem o código continuamente tão logo os aprimoramentos do código forem encontrados.
() Tão logo o trabalho em uma tarefa seja concluído, este é integrado ao sistema como um todo a) 5, 3,1, 4, 2.
B) 2, 4, 3, 5,1.

c) 4, 5, 2,1, 3.

d) 3,1, 5, 2, 4.

e) 5, 2, 4, 3,1.

Comentários:

Desenvolvedores trabalham em todas as áreas do sistema? (3) Estamos falando da prática da propriedade coletiva do código; Conjunto mínimo útil de funcionalidades? (1) T rata-se da prática dos pequenos releases; Excesso de horas-extras e redução da produtividade? (5) Trata-se da prática de ritmo sustentável; Desenvolvedores recriam o código continuamente? (2) Estamos falando da prática do refatoramento; Integração assim que um trabalho é concluído? Trata-se da propriedade da integração contínua (4).
Gabarito: Letra D

33. (UFPel-CES / UFPEL - 2015) Em projetos nos quais se aplicam o método ágil XP, a fase em que o propósito é empresa e cliente concordarem em uma data na qual o menor e melhor conjunto de histórias de usuários deverá ser implementado é a fase de:
a) planejamento.

b) exploração.

c) iterações e entregas.

d) produção.

e) manutenção.

Comentários:

projeto simples soluções pontuais cartões CRC protótipos
De acordo com a figura, vemos que a fase que está relacionada diretamente com os valores das histórias de usuários é a fase de planejamento. É na fase de planejamento que os desenvolvedores definem com os clientes as userstories, que nada mais são do que requisitos. Além disso, para cada requisito é definido uma complexidade e prazo de entrega.
Gabarito: Letra A

34.(CS-UFG/ AL-GO- 2015) Extreme Programming (XP) é um exemplo de método ágil que foi definido por Kent Beck. O XP inclui uma abordagem de teste que:
a) valoriza o desenvolvimento test-last.

b) depende da técnica de teste baseada em defeitos c) desenvolve teste incremental baseado em cenários d) utiliza processo de teste dirigido a planos.
Comentários:

(a) Errado. O XP trabalha com desenvolvimento test-first; (b) Errado. O teste é baseado em cenários; (c) Correto. O XP tem como características testes incrementais a partir de cenários - é importante lembrar que os cenários são também chamados de histórias de usuários (user stories);
(d) Errado. Os testes são dirigidos a cenários.

Gabarito: Letra C

35. (CETRO / AMAZUL- 2015) Assinale a alternativa que não apresenta um princípio/
valor da metodologia de desenvolvimento de software XP (Extreme Programming):
a) Simplicidade.

b) Programação individual ou não em pares.

c) Comunicação.

d) Coragem.

e) Feedback.

Comentários:

Todas as alternativas apresentam valores do XP, exceto a programação individual.
Primeiro, porque isso é uma prática; segundo, porque é a programação em pares e, não, individual.
Gabarito: Letra B

3Ô.(IESES / TRE-MA - 2015) No desenvolvimento de software em XP, são empregadas algumas práticas. Avalie as assertivas abaixo:
I. Programação em pares.

II. Time coeso.

III. Integração contínua.

IV. Desenvolvimento orientado a testes.

Quantas afirmativas são verdadeiras?

a) 2

b) 1

c) 4

d) 3

Comentários:

Todas as alternativas apresentam práticas do XP.

Gabarito: Letra C

37. (FUNCAB / SEFAZ-BA - 2014) São características do Extreme Programming (XP), EXCETO:

a) apresentar desenvolvimento incremental.

b) admitir a existência de uma especificação detalhada.

c) utilizar programação com pares de desenvolvedores.

d) permitir a integração de usuário com o time de desenvolvimento.

e) suportar testes automáticos contínuos.

Comentários:

(a) Correto. O desenvolvimento é incremental; (b) Errado. Na verdade, o projeto deve ser simples,e não detalhado; (c) Correto. O XP utiliza a programação em pares; (d) Correto, o envolvimento do cliente ocorre em tempo integral; (e) Correto. Há testes automatizados e contínuos no XP.
Gabarito: Letra B

38.(INSTITUTO AOCP/ MPE-BA- 2014) O processo ágil XP possui doze práticas que são os princípios fundamentais do processo. A prática que encoraja a equipe inteira a trabalhar mais unida em busca de qualidade no código fazendo melhorias e refatoramentos em qualquer parte do código a qualquertempo é conhecida como:
a) propriedade coletiva do código.

b) semana de quarenta horas.

c) programação em pares.

d) padrões de codificação.

e) integração contínua.

Comentários:

Uma das principais práticas do XP é a propriedade coletiva do código, ela diz que os pares de desenvolvedores podem trabalhar em todas as áreas do sistema, de forma que não se formem ilhas de conhecimento.
Gabarito: Letra A

39.(FUNCAB / MDA- 2014) A "Extreme Programming - XP" representa um dos mais conhecidos métodos ágeis. Uma das práticas utilizadas na XP é:
a) empregar um esquema em que os desenvolvedores trabalham individualmente.

b) integrar o sistema exclusivamente quando todos os módulos forem concluídos.

c) usar cenários para expressar requisitos implementados como uma série de tarefas.

d) impedir que o cliente interaja com a equipe de desenvolvimento na fase de especificação.

e) eliminar a necessidade da realização de testes durante a fase de desenvolvimento.

Comentários:

(a) Errado, os desenvolvedores trabalham em pares; (b) Errado, uma das práticas é a de pequenos releases durante o desenvolvimento; (c) Correto, no XP os requisitos são expressos como cenários;
(d) Errado, o cliente tem envolvimento em tempo integral; (e) Errado, os testes são frequentes.

Gabarito: Letra C

4O.(CESGRANRIO / Banco da Amazônia - 2014) Uma prática que NÃO é adotada por Extreme
Programming (XP) é a) usarduas pessoas trabalhando juntas em um único computador para produzirtodo o código que será enviado para a produção.
b) criar os testes antes do código que será testado.

c) refatorar frequentemente, e ao longo de todo o projeto, o código produzido pelos desenvolvedores.
d) integrar continuamente o código recém-produzido com o código existente no repositório.

e) variar a duração de cada iteração durante todo o projeto para acomodar eventuais mudanças de prioridade dos requisitos, definidas pelo cliente.
Comentários:

Lembrem-se: tempo fixo e escopo variável e, não, o contrário! A última opção afirma que o tempo muda de acordo com o escopo/mudanças e isso não é verdade.
Gabarito: Letra E

4i.(CESGRANRIO / BNDES - 2013) Sendo atualmente conhecida por just-in-time, a produção enxuta contém princípios que compõem a base dos processos ágeis de desenvolvimento de software, como o Extremme Programming (XP). Um dos princípios básicos do XP, a eliminação de desperdícios, busca:
a) evitar o efeito negativo que uma definição de risco, na fase inicial do projeto,
possa causar na performance do software como um todo, tendo, como saída, informações não relevantes para o processo.
b) produzir requisitos bem definidos e completos de forma a abranger todos os processos e rotinas administrativas, funcionais e produtivas almejadas pelos stakeholders envolvidos no projeto.
c) reduzir, o máximo possível, o volume de trabalho executado e os subprodutos envolvidos nesse trabalho, concentrando os esforços apenas no que pode produzir um resultado objetivo e palpável ao cliente final.
d) descrever os processos que garantam a inclusão, no projeto, de todo o serviço necessário, e somente o serviço necessário, para que esse projeto seja finalizado com sucesso.
e) descrever os processos envolvidos no planejamento, no monitoramento e na garantia de que o projeto será realizado dentro dos prazos definidos no escopo, mantendo a qualidade definida e o enxugamento dos custos inicialmente programados.
Comentários:

A frase chave é "...concentrando os esforços apenas no que pode produzir um resultado objetivo e palpável ao cliente final". Tudo que não for entregar valor ao cliente é desperdício.
Gabarito: Letra C

42.(INSTITUTO AOCP / EBSERH - 207) O Extreme Programming (XP) surgiu em 1999, a partir de uma publicação sobre o assunto, mas suas bases se conectam a princípios da década de 80 e ao manifesto ágil. O XP é baseado em 4 atividades de arcabouços. Assinale a alternativa que contém 3 desses arcabouços:
a) Levantamento de requisitos, análise de negócio, planejamento e documentação.

b) Levantamento de requisitos, planejamento, documentação e implantação.

c) Levantamento de requisitos, documentação, codificação e teste.

d) Planejamento, projeto, documentação e implantação.

e) Governança, planejamento, codificação e teste.

Comentários:

A resposta é: Governança, Planejamento, Codificação e Testes. Professor, você está cego?
Onde tem governança na imagem? A questão não deveria ser anulada? Não! A questão afirma que oXP é baseado em quatro atividades de arcabouços e pede para assinalar a alternativa que contém três desses arcabouços. Governança não faz parte, mas projeto, codificação e testes fazem!
Gabarito: Letra E

LISTA DE QUESTõES - CESPE

í. (CESPE / BANRISUL - 2022) Um aspecto central na XP é o fato de que a elaboração do projeto ocorre tanto antes quanto depois de se ter iniciado a codificação.
2. (CESPE / BANRISUL - 2022) Na metodologia XP (Extreme Programming), a atividade de planejamento se inicia com o levantamento de requisitos, em que são obtidas histórias de usuários, similares aos casos de uso; a seguir, clientes e desenvolvedores trabalham juntos para decidir como agrupar essas histórias.
3. (CESPE / Ministério da Economia - 2020) Grandes quantidades de horas extras são aceitáveis em médio e longo prazo, para agilizar a entrega de requisitos.
4. (CESPE / Ministério da Economia - 2020) Como forma de agilizar as implantações de novas releases nesse modelo, são acumulados grandes grupos de funcionalidades e implantadas grandes releases.
5. (CESPE / Ministério da Economia - 2020) Os programadores trabalham em pares para que um possa verificar e apoiar o trabalho do outro e, assim, realizem um bom trabalho.
6. (CESPE / Ministério da Economia - 2020) O refactoring de código não faz parte do modelo XP,visto que a expectativa é a entrega ágil, e não deve ser considerada em tempo de projeto a recriação de código para aprimoramento.
7. (CESPE / Ministério da Economia - 2020) O XP possui planejamento incremental com requisitos registrados em histórias.
8. (CESPE ITCE-RO - 2019) No que diz respeito a processos e práticas ágeis, o desenvolvimento incremental a) é, assim como otest-driven development, uma prática da XP (Extreme Programming)que exige teste automatizado, domain-driven design, refactoring e integração contínua.
b) é, na XP (Extreme Programming), sustentado por meio de pequenos e frequentes releases do sistema, e os clientes estão intimamente envolvidos na especificação e na priorização dos requisitos do sistema.
c) enfoca, assim como oacceptance test-driven development, a qualidade do código desenvolvido quanto a recursividade, declaração das variáveis e clean code, de modo a torná-lo de fácil entendimento, modificação e testagem d) pressupõe o uso do behavior driven development, que considera a linguagem de programação a ser usada, da 4.a geração em diante, com foco,principalmente, no comportamento visual, interativo e cognitivo do sistema.
e) enfoca a integração contínua como uma prática de desenvolvimento de software,incompatível com a XP (E xtreme Programming) e o Scrum, que permite aos desenvolvedores agregarem alterações de código e realizarem testes.
9. (CESPE / TJ-AM - 2019) No XP (Extreme Programming), o valor de uma história de usuário é atribuído pelos membros da equipe e é medido em termos de semanas estimadas para o desenvolvimento.
10. (CESPE / ABIN - 2018) Na extreme programming, como não há especificação de sistema que possa ser usada por equipe de teste externa, a característica de test-first exige que os implementadores de tarefa compreendam detalhadamente a especificação de comportamento da funcionalidade em desenvolvimento, a fim de que possam escrever o teste para o sistema.
11. (CESPE/BNB-2018) Em XP, a técnica de planning game é utilizada pelo cliente para identificar as prioridades do que deve ser construído em um software, sem a participação dos desenvolvedores.
12. (CESPE / ABIN - 2018) O ritmo ágil de desenvolvimento de softwares é uma prática usada para favorecer a entrega das releases quando grandes volumes de horas extras são tolerados.
13. (CESPE / ABIN - 2018) Para apoiar a equipe de desenvolvimento, é uma prática o uso do cliente on-site em tempo integral.
14. (CESPE / STM - 2018) Na XP (Extreme Programming), programadores trabalham em pares, e requisitos são expressos como cenários, denominados histórias de usuários, os quais são implementados como uma série de tarefas.
15. (CESPE / TRT - 7a Região (CE) - 2017) Acerca de metodologia XP, assinale a opção correta.

a) Para atingir a agilidade necessária, a equipe de desenvolvimento deve ser composta de pessoas com experiência comprovada na linguagem utilizada.
b) A prática de planning game do XP permite que o escopo do projeto seja alterado a cada semana.
c) Mesmo sendo considerada uma metodologia ágil, XP exige uma especificação completa e formal dos requisitos.
d) Em XP, denomina-se explanação o processo por meio do qual uma pessoa tenta explicar um assunto fazendo comparações com o mundo real.
i6.(CESPE / TRE-BA - 2017) Considerando uma situação hipotética com o uso da XP
(eXtreme
Programming) concomitante com Scrum em um projeto de desenvolvimento de software em uma organização, julgue os seguintes itens.
I. É viável a utilização do TDD (Test Driven Development) na fase de sprint, de modo que se escreva o teste automático antes da codificação.
II. O princípio da integração contínua da XP deve ser utilizado especificamente na retrospectiva da sprint com vistas a integrar a equipe scrum.
III. Integrantes da equipe scrum podem realizar a programação do código em pares, o que proporciona, entre outras vantagens, o nivelamento de conhecimento da equipe.
IV. O conceito de requisito "pronto" continuaria válido, contudo, inviabilizaria o refactoring, pois é proibitivo inserir o mesmo item (requisito) em várias sprints.
Estão certos apenas os itens:

a) I e II.

b) I e III.

c) lie IV.

d) I, III e IV.

e) II, III e IV

17. (CESPE / TRE-TO - 2017) Em projetos de desenvolvimento de software, a extreme programming (XP) é um método ágil que usa a prática de:
a) projetos com planejamento completo sem incrementos.

b) grandes releases.

c) grande quantidade de horas extras.

d) trabalho em pares de desenvolvedores.

e) integrações após a entrega do software completo.

18. (CESPE/ FUNPRESP-JUD-2016) Uma característica da metodologia XP é a existência de uma equipe técnica voltada para a agilidade e velocidade do desenvolvimento do software, de forma que todo o desenvolvimento seja feito sem a interferência ou ajuda do cliente até que os releases sejam disponibilizados para que o desenvolvimento se torne o mais ágil possível.
ig.(CESPE / TCE-PA - 2016) Em XP (Extreme Programming), as user stories não objetivam definir o escopo global do sistema, mas avaliar a complexidade de cada uma de suas partes a fim serem estimados prazos na perspectiva dos usuários ou clientes do sistema.
20.(CESPE / FUNPRESP-JUD-2016) A programação em pares, em que os desenvolvedores atuam avaliando entre si o trabalho do outro, é uma prática da metodologia XP.
21. (CESPE / FUNPRESP-JUD - 2016) As práticas da extreme programming, que tem por princípio liberar grandes releases de software, visam agregar valor ao negócio.
22. (CESPE/TRT-PR-2016) Um projeto desenvolvido mediante XP (Extreme Programming)
segue princípios opostos aos de um projeto implementado com base em KIS (Keep lt Simple).
23. (CESPE / TRE-RS- 2015) Tendo em vista que, em um processo ágil de desenvolvimento de software, foi adotado o XP (eXtreme Programming) e que os requisitos levantados foram expressos na forma de histórias de usuário, assinale a opção que apresenta,corretamente,
recomendações técnicas para a elaboração de um cartão de histórias de usuário.

a) Como um professor, quero calcular as médias semestrais dos alunos de modo que eu possa identificar quais serão aprovados.
b) O professor deseja o cálculo de notas semestrais com precisão de até duas casas decimais.

c) O sistema deve calcular as médias semestrais dos alunos com base nas notas atribuídas a eles pelos professores.
d) Como analista de requisitos, eu preciso oferecer o cálculo das notas semestrais aos professores em menos de um minuto.
e) Como um professor, eu preciso de releases semanais de funcionalidades, mesmo que elas possam ser refatoradas posteriormente.
24. (CESPE / TJDFT - 2015) Na metodologia XP (extreme programming), em que todos os requisitos são expressos como cenários, deve-se aguardar, após a conclusão das tarefas,ciclos de cento e oitenta dias para a publicação de grandes releases do software.
25. (CESPE / TJDFT - 2015) As características da metodologia XP incluem o desenvolvimento interativo, que dispõe de um processo de testes informais.
26. (CESPE / TRE-RS - 2015) Em um desenvolvimento ágil de sistemas utilizando o XP,
foram adotadas as seguintes ações: foi dita a verdade ao cliente acerca do progresso do projeto e acerca de suas estimativas, além de haverem sido realizadas adaptações quando mudanças importantes aconteceram no projeto. Essas ações estão coerentes com o valor do XPdenominado:

a) sinceridade.

b) comunicação.

c) coragem.

d) feedback.

e) respeito.

27. (CESPE / TRE-RS - 2015) Assinale a opção que apresenta uma característica relacionada a projetos que utilizam o método XP (eXtreme Programming), muito utilizado em projetos para o desenvolvimento de softwares.
a) grandes releases b) programação individual c) cliente off-site d) grandes volumes de horas extras e) planejamento incremental
28. (CESPE / STJ- 2015) Na Extreme Programming, a programação em pares cria ilhas de especialistas na equipe por meio da análise simultânea de duas pessoas no desenvolvimento do software.
29. (CESPE / FUB - 2015) Práticas de desenvolvimento de software aos pares de programadores,em que um programador verifica o trabalho do outro, são uma característica do método de desenvolvimento XP.
30. (CESPE/FUB-2oi5) É considerada como ritmo sustentável a carga horária de trabalho extensa para gerar rapidamente entregas de produtos de software, o que provoca grande quantidade de horas extras.
31. (CESPE / ANTT - 2013) São práticas ou princípios recomendados no modelo de desenvolvimento de software XP (eXtreme Programming) proposto porKent Beck:
programação em pares; semana de trabalho de 40 horas; refatoração sem piedade;desenvolvimento orientado a testes TDD (Test Driven Development); e desenvolvimento de metáforas arquiteturais.
32. (CESPE / STF - 2013) XP (Extreme Programming) é uma metodologia ágil voltada para equipes pequenas e médias que desenvolvam software baseado em requisitos vagos e se caracteriza por possibilitar modificações rápidas.
33. (CESPE/TCE-RO-2013) No método XP (eXtreming programming), os sistemas são concebidos a partir de uma metáfora e descritos em estórias do usuário. Esse método busca facilitar a comunicação com o cliente, entendendo a realidade deste e guiando o desenvolvimento com o uso de estória simples.
34.(CESPE / MPU 2013) XP é um método de desenvolvimento de software em que os requisitos são especificados em user stories; requisitos, arquitetura e design surgem durante o curso do projeto; e o desenvolvimento ocorre de maneira incremental.
35. (CESPE / MPE-PI - 2012) O XP (Extreme Programming) é um método ágil, que preconiza a criação de um caso de teste unitário antes do início da codificação.
36.(CESPE / ANAC - 2012) Para o método ágil de desenvolvimento conhecido como extreme programming, todos os requisitos funcionais são expressos como cenários (histórias do usuário)que são implementados diretamente como uma série de tarefas.

37-(CESPE / ANAC - 2012) A técnica conhecida como refactoring é constantemente aplicada no desenvolvimento baseado no método ágil extreme programming.
38.(CESPE / ANAC - 2012) No modelo extreme programming, os testes de software só são realizados na etapa final de desenvolvimento do software e, somente nessa etapa, os programadores trabalham, obrigatoriamente, em pares, utilizando cada um o próprio computador.
39. (CESPE / ANAC - 2012) Na metodologia ágil XP (extreme programming), as metáforas são formas de transmitir ideias complexas de maneira simples, ou seja, utiliza-se uma linguagem simples entre a equipe e o cliente, com o objetivo de que, entre as inúmeras variáveis de controle em projetos, tais como tempo, custo, qualidade e escopo, obtenha-se maiorfoco no tempo,em detrimento do planejamento do release.
40. (CESPE / EBC - 2011) O XP segue um conjunto de valores, princípios e regras básicas que visam alcançar eficiência e efetividade no processo de desenvolvimento de software. Os valores são cinco: comunicação, simplicidade, feedback, coragem e respeito.
41. (CESPE / STM - 2011) O Extreme Programming (XP), que se inclui entre os métodos ágeis,apresenta, entre outras, as seguintes características: pequenos releases, projeto simples,refactoring, programação em pares e propriedade coletiva.

42. (CESPE / TRE-BA - 2010) Em XP, a prática denominada programação em pares (pair programming) é realizada por um desenvolvedor em dois computadores, com o objetivo de aumentara produtividade.
43. (CESPE / ABIN - 2010) Na Extreme Programming, os requisitos são expressos como cenários e implementados diretamente como uma série de tarefas. O representante do cliente faz parte do desenvolvimento e é responsável pela definição de testes de aceitação do sistema.
44. (CESPE / MPU - 2010) Extreme programming (XP) é embasado em requisitos conhecidos,definidos de antemão, que não sofram muitas alterações, devendo ser usado por equipes de pequeno porte, formadas por representantes de todos os stakeholders.
45.(CESPE / TRE-BA - 2010) Os quatro valores fundamentais da metodologia XP são:comunicação, simplicidade, feedback e coragem.

46.(CESPE / TCU - 2010) O processo XP (extreme programming) envolve a realização das atividades de planejamento, de projeto, de codificação e de teste.
47. (CESPE/SECONT-ES-2009) Métodos ágeis de desenvolvimento de sistemas foram propostos principalmente para apoiar o desenvolvimento de aplicações de negócios nas quais os requisitos de sistema mudam rapidamente durante o processo de desenvolvimento. Entre esses métodos está o extreme programming, que envolve um número de práticas, como o planejamento incremental, a definição de um ritmo de trabalho sustentável e a divisão das equipes de trabalho por meio da especialização de seus membros.
48. (CESPE / IPEA - 2009) A extreme programming (XP) é um método de desenvolvimento ágil.Nele, os requisitos são expressos como cenários implementados diretamente como uma série de tarefas.
49. (CESPE / TRE-MG - 2009) Extreme programming é um método centrado no usuário, na produtividade do desenvolvimento e na documentação de apoio.
50. (CESPE / TRE-BA - 2009) A metodologia XP prevê valores e princípios básicos para serem considerados durante o desenvolvimento de software. Feedback, coragem e respeito são exemplos de valores; mudanças incrementais, abraçar mudanças e trabalho de qualidade são exemplos de princípios básicos.
51. (CESPE / ANAC - 2009) Extreme Programming é um modelo de processo de desenvolvimento de software para equipes com grande número de pessoas, que desenvolvem software com base em requisitos vagos e que são modificados rapidamente.
52. (CESPE / ANTAQ - 2009) O extreme programming (XP) constitui método ágil de desenvolvimento de software. Uma das práticas que se enquadram nos princípios dos métodos ágeis é a programação em pares, que promove o compartilhamento da autoria do código do sistema. Além dessa vantagem, a programação em pares atua como processo informal de revisão porque cada linha de código é vista por pelo menos duas pessoas.
53. (CESPE / PRODEST - 2008) Projetar detalhadamente todo o software antes de iniciar a sua implementação é uma prática recomendada pelo XP. O software deve ser projetado para atender tanto aos requisitos atuais quanto aos potenciais requisitos futuros. Para atingir esse objetivo, são analisados os possíveis cenários de evolução futura e são empregados padrões de projeto para facilitar a manutenção.
54. (CESPE / PRODEST - 2008) Constituem práticas recomendadas pelo XP a colocação rápida de uma versão simples em produção, a liberação das novas versões em curtos intervalos de tempo,a programação em duplas, a refatoração (refactor) dos códigos produzidos, a adoção de padrões para a codificação; a integração e o teste contínuos de códigos; a limitação em 40horas da carga de trabalho semanal.
55. (CESPE / PRODEST - 2008) O XP é um processo que visa a um desenvolvimento ágil e portanto não recomenda os testes de unidade, pois eles consomem muitos recursos.Durante o desenvolvimento, o primeiro teste recomendado é o smoke test que foca os detalhes de funcionamento. O smoke test é realizado após as unidades serem integradas. Após o smoke test, é realizado o teste de sistema.
GABARITo

1. CORRETO 20. CORRETO
39- ERRADO

2. CORRETO 21. ERRADO
40. CORRETO

3- ERRADO 22. ERRADO
41. CORRETO

4- ERRADO 23- LETRA A
42. ERRADO

5- CORRETO 24. ERRADO
43- CORRETO

6. ERRADO 25- CORRETO
44. ERRADO

7- CORRETO 26. LETRA C
45- CORRETO

8. LETRA B 27- LETRA E
46. CORRETO

9- ERRADO 28. ERRADO
47- ERRADO

10. CORRETO 29. CORRETO
48. CORRETO

li. ERRADO 30. ERRADO
49- ERRADO

12. ERRADO 31- CORRETO
50. CORRETO

13- CORRETO 32. CORRETO 51-
ERRADO

14- CORRETO 33- CORRETO 52.
CORRETO

x5- LETRA B 34- CORRETO
53- ERRADO

i6. LETRA B 35- CORRETO
54- CORRETO

17- LETRA D 36. CORRETO
55- ERRADO

i8. ERRADO 37- CORRETO

19. CORRETO 38. ERRADO

í. (FCC /SANASA Campinas -2019) Em um projeto de software baseado na metodologia ágilXP,
um Analista de TI deve a) consultar o cliente quando uma história exigir, por estimativa, menos do que 3semanas de desenvolvimento, para que o cliente a complemente com mais tarefas.
b) ouvir o cliente, durante o levantamento de requisitos, para que este crie as histórias de usuários. Após essa importante etapa nenhuma história nova deve ser criada para não comprometer o cronograma do projeto.
c) evitar que o projeto caia na armadilha de seguir o princípio KISS de forma a estimular que o projeto de uma funcionalidade extra, que poderá ser necessária no futuro, faça parte do modelo do software.
d) realizar os testes de unidade de forma manual, evitando que sejam usadas baterias de testes automatizados, pois estes impedem a realização de testes de regressão.
e) estimular o uso de cartões CRC como um mecanismo eficaz para pensar o software em um contexto orientado a objetos.
2. (FCC / DPE-AM - 2018) Considere a definição de algumas práticas da eXtreme Programming -
XP.

I. Todo o código desenvolvido pelo time é incorporado em um repositório comum várias vezes ao dia. Isso garante que qualquer problema de integração ao longo do projeto possa ser notado e corrigido rapidamente.
II. Qualquer programador do time pode alterar qualquer seção do código, se necessário.
Por mais que esta prática pareça perigosa, ela aumenta a velocidade do desenvolvimento e problemas em potencial podem ser detectados pelos testes de unidade.
III. Traz a ideia de que qualquer pessoa do time seja capaz de verificar o código sendo desenvolvido em alto nível e ter uma compreensão clara de qual funcionalidade do sistema está sendo trabalhada.
IV. Permite aplicar melhorias ao código sem mudar sua funcionalidade,
visando sua simplificação. Se o cliente deseja alterar alguma coisa no produto final, o time pode fazer os ajustes rapidamente, e esta prática contribui para alcançar este objetivo.
As práticas de I a IV são, correta e respectivamente,

0 0

a) pair programming -test-driven development-system metaphor-continuous integration.

b) planning game - pair programming -system simplicity- continuous integration.

c) planning game-test-driven development-system simplicity - refactoring.

d) continuous integration - pair programming -feedback- planning game.

e) continuous integration -collective code ownership -system metaphor- refactoring.

3. (FCC /TST-2017) Uma dupla de programadores, utilizando o modelo Extreme Programming
-
XP, realiza, na fase de:

a) desenvolvimento, a implementação das user stories que fazem parte da iteração corrente.

b) desenvolvimento, a entrega das user stories totais do sistema.

c) validação do sistema, a análise dos requisitos técnicos entregáveis.

d) validação do sistema, a integração total dos incrementos das user stories.

e) projeto da arquitetura do sistema, a implementação das user stories totais do sistema.

4. (FCC / DPE-RS - 2017) Considere que um Analista esteja participando de um projeto que utiliza as melhores práticas da Extreme Programming - XP. No início de uma iteração a equipe de desenvolvimento, da qual o Analista fazia parte, convidou o cliente a escrever as funcionalidades que desejava no sistema em pequenos cartões chamados user stories. Depois disso, a equipe de desenvolvimento estimou o tempo e o custo de cada funcionalidade para o cliente. Ocliente foi informado do tempo e custo, e foi solicitado a decidir a prioridade em que cada user story deveria ser desenvolvida. Esta prática XP é conhecida como:
a) Releases e é utilizada para que o cliente possa utilizar o sistema, possibilitando à equipe de desenvolvimento saber se há defeitos ou não no código.
b) Releases e visa reorganizar o código fonte para melhorar sua qualidade interna,
facilitar seu entendimento pelo cliente e diminuir o tempo gasto com manutenção.
c) Metáforas e permite que o cliente transmita ideias complexas de forma simples e clara,usando um vocabulário comum.

d) Planning Game e permite que o Analista e outro desenvolvedor escolham uma user story e codifiquem juntos aquela funcionalidade.
e) Planning Game e busca assegurar que a equipe esteja sempre trabalhando no que é mais importante e gere mais valor para o cliente.
5. (FCC / CREMESP - 2016) Considere que nos projetos do CREMESP baseados em XP
pratica-se a propriedade coletiva de código, de forma que todos os desenvolvedores podem fazer alterações e refatoração de qualquer parte do código a qualquer momento. Para isso, é necessário que também haja:
a) padrões de codificação.

b) time-box de 40 horas.

c) testes apenas depois da codificação.

d) releases grandes.

e) integração das funcionalidades, mesmo com erros.

6. (FCC/ Prefeitura de Teresina - PI - 2016) Os métodos ágeis de desenvolvimento de software como eXtreme Programming - XP consideram um conjunto de valores fundamentais derivados do manifesto ágil. Assim, estes métodos valorizam MENOS:
a) os indivíduos e a interação entre eles, do que os processos e ferramentas.

b) o software funcionando, do que uma documentação abrangente.

c) a colaboração com o cliente, do que negociação de contratos.

d) a resposta rápida a mudanças, do que seguir um plano previamente definido.

e) a rigorosidade dos processos, do que a adaptação às mudanças.

7. (FCC / TRE-PB- 2015) Extreme Programming - XP pode ser considerado um modelo de desenvolvimento de software baseado em uma série de valores, princípios e regras, dentre eles,
a) criar obrigatoriamente uma matriz de rastreabilidade de requisitos.

b) manter o foco na documentação, detalhada e diversificada.

c) definir sprint de no máximo duas semanas.

d) escrever sempre o código, depois, o teste de unidade.

e) realizar semanalmente o jogo do planejamento (planning game).

8. (FCC / TST - 2012) O XP (Extreme Programming) utiliza uma abordagem orientada a objetos como seu paradigma de desenvolvimento predileto. Ele:
a) recomenda que duas pessoas trabalhem juntas para criar o código correspondente a uma história.
b) recomenda que a equipe XP e os clientes trabalhem de forma separada para não mudar o compromisso básico definido para a versão a ser entregue.
c) segue rigorosamente o princípio FDD - Feature Driven Development.

d) recomenda que depois que as histórias forem desenvolvidas e o trabalho preliminar do projeto for feito, a equipe XP avance diretamente para o código.
e) inclui um conjunto de regras e práticas que ocorrem no contexto de 3 atividades de arcabouço:projeto, implementação e entrega.

g. (FCC / MPE-AP - 2012) O Extreme Programming (XP) é, talvez, o mais conhecido e mais utilizado dos métodos ágeis. Dentre suas práticas se encontram programação em pares,integração contínua, refatoração e:

a) propriedade coletiva, que garante uma participação nos lucros aos membros da equipe de desenvolvimento, técnica que incentiva e aumenta o desempenho de toda a equipe.
b) envolvimento do cliente apenas na fase final do sistema, fator que difere de outras metodologias como SCRUM e TDD e confere agilidade ao processo de desenvolvimento.
c) processo de desenvolvimento contínuo, em que a equipe se mantém focada no sistema até que uma funcionalidade específica seja entregue, comumente agregando horas extras ao turno de trabalho.
d) utilização de técnicas de ofuscação do código fonte, trazendo segurança e garantindo que apenas a equipe de desenvolvimento poderá ter acesso a este código e) desenvolvimento incremental e sustentado por meio de pequenos e frequentes releases do sistema. Os requisitos são baseados em cenários ou em simples histórias de clientes.
10.(FCC / MPE-PE - 2012) Dentre as práticas do método ágil Extreme Programming (XP),
está a prática de propriedade coletiva. É correto afirmar que, nessa prática,
a) os trabalhos são desenvolvidos em conjunto, para que um programador possa analisar o trabalho do outro.
b) cada projeto é realizado para atender às necessidades globais dos usuários, focando na coletividade da distribuição da informação.
c) os pares de desenvolvedores trabalham em todas as áreas do sistema, de modo que não se desenvolvam ilhas de expertise.
d) grandes quantidades de horas extras não são consideradas aceitáveis, pois o resultado final,muitas vezes, é a redução da qualidade do código e da produtividade a médio prazo,
sendo que o indivíduo pode afetar o desempenho de todo o time.
e) um representante do usuário final do sistema deve estar disponível todo o tempo à equipe de desenvolvimento. Nesse modelo de desenvolvimento, o cliente é membro da equipe e participa da responsabilidade do código desenvolvido.
ii.(FCC/TJ-PE-20i2) NoS métodos ágeis XP e Scrum, as entregas de partes funcionais do projeto são divididas em ciclos, geralmente compreendidos no período de 1 a 4 semanas. Estes ciclos denominam-se, respectivamente,
a) iterações e sprint.

b) reunião de planejamento e backlog.

c) período de entrega e reunião de revisão.

d) backlog e planejamento da produção.

e) entrega e retrospectiva.

12. (FCC / TRT-MT - 2011) NÃO se aplica à disciplina de desenvolvimento de software extreme programming (XP):
a) Usa notações próprias para construir os diversos produtos de trabalho do projeto.

b) Encoraja a refabricação para modificar um sofware sem alterar o comportamento externo do código.
c) Recomenda que dois programadores trabalhem juntos no mesmo computador para escrever um código.
d) Baseada em valores de simplicidade, comunicação, feedback e coragem.

e) Adota como um elemento-chave a criação de testes unitários antes da codificação começar.

13. (FCC / TRE-RN - 2011) Considere as seguintes características:

I. Propriedade coletiva.

II. Integração contínua.

III. Metáfora.

Dentre as práticas componentes da Extreme Programming, aplica-se o que consta em:

a) I, apenas.

b) II, apenas.

c) I e II, apenas.

d) II e III, apenas.

e) I, lie III.

14.(FCC/TRT-23-2oII) No desenvolvimento de software em Extreme Programming (XP)
há uma confiança muito grande na sinergia entre as práticas, já que os pontos fracos de cada uma são superados pelos pontos fortes de outras. Dentre elas, aquela em que o código fonte não tem dono e ninguém precisa solicitar permissão para poder modificá-lo, permitindo, assim,que a equipe conheça todas as partes do sistema, é chamada de:
a) Whole Team (Time Coeso).

b) Sustainable Pace (Ritmo Sustentável).

c) Pair Programming (Programação em Pares).

d) Collective Ownership (Posse Coletiva).

e) Coding Standards (Padrões de Codificação).

15. (FCC / TRE-RN - 2011) Assegurar que a equipe se concentre em fazer, primeiro,
apenas aquilo que é claramente necessário e evite fazer o que poderia vir a ser necessário, mas ainda não se provou essencial. Este é um dos cinco valores fundamentais do XP (Extreme Programming),denominado:

a) coragem.

b) respeito.

c) comunicação.

d) simplicidade.

e) feedback.

16. (FCC / TRE-RS - 2010) No eXtreme Programming, XP:

a) o código é integrado e testado depois de alguns dias e, no máximo, até o final da semana.

b) a codificação é feita em grupos de programadores (no mínimo 3
integrantes),
preferencialmente num único computador.

c) as equipes de desenvolvimento estabelecem suas próprias regras, mas uma equipe pode adotar as regras de outra equipe.
d) releases quando complexos não podem deixar de fora os requisitos de negócio de maior valor para o cliente.
e) módulos não são propriedade de nenhum desenvolvedor; todo desenvolvedor da equipe tem o direito de checar um módulo e modificá-lo.
17.(FCC / MPE-RN - 2010) Refactoring, programação em pares e Stand-up Meeting são características das práticas do:
a) PRINCE2.

b) Rational Unified Process.

c) Extreme programming.

d) PMBOK.

e) SCRUM.

i8.(FCC/TJ-PI-2Oog)XP (eXtreme Programming) é uma metodologia ágil para equipes pequenas e médias que desenvolverão software com requisitos vagos e em constante mudança. Para isso,adota a estratégia de constante acompanhamento e realização de vários pequenos ajustes durante o desenvolvimento de software. Para aplicar os valores e princípios durante o desenvolvimento de software, a XP propõe uma série de práticas, sendo uma delas: sempre que produzir uma nova funcionalidade, nunca esperar uma semana para integrar à versão atual do sistema a fim de evitar o aumento da possibilidade de conflitos e da possibilidade de erros no código fonte. Tal prática é denominada:
a) Time Coeso.

b) Refatoração.

c) Integração Contínua.

d) Desenvolvimento Orientado a Testes.

e) Ritmo Sustentável.

ig.(FCC / TCE-AL - 2008) Originalmente, o único produto da atividade de Projeto que é realizado como parte do processo XP (Extreme Programming):
a) é a definição do caso de uso de contexto.

b) são os cartões CRC.

c) são os diagramas de objetos.

d) são os diagramas de seqüência.

e) é a codificação, feita em pares.

2O.(FCC/TRE-SE-2OO7) NaXP (eXtreme Programming):

a) deve-se usar o modelo em cascata para o desenvolvimento do software.

b) os programadores desenvolvem o software criando primeiramente os testes.

c) deve ser evitada a comunicação pessoal entre clientes e desenvolvedores, sempre dando preferência a outros meios de comunicação mais formais.
d) os programadores desenvolvem o software fazendo todos os testes possíveis no término do desenvolvimento.
e) deve-se projetar todas as funções possíveis com a máxima previsão do que ocorrerá no futuro,antes do desenvolvimento do software, a fim de evitar alterações desnecessárias.

GABARITo

1. LETRA E

2. LETRA E

3. LETRA A

4. LETRA E

5. LETRA A

6. LETRA E

7. LETRA E

8. LETRA A

9. LETRA E

10. LETRA C

11. LETRA A

12. LETRA A

13. LETRA E

14. LETRA D

15. LETRA D

16. LETRA E

17. LETRA C

18. LETRA C

19. LETRA B

20. LETRA B

LISTA DE QUESTõES - FCV

í. (FGV/ SEFAZ-BA- 2022) Com relação à programação por pares, analise as afirmativas a seguir e assinale (V) para a verdadeira e (F) para a falsa.
() É uma prática proposta no método ágil, onde programadores (um experiente e um novato)atuam no desenvolvimento de código-fonte.

() Requer uma mudança cultural. A prática consiste em uma pessoa programando enquanto a outra atua como revisor.
( ) Este tipo de programação não exemplifica uma prática de construção colaborativa de modelos e de elaboração de código-fonte.
As afirmativas são, na ordem apresentada, respectivamente,

a) F-V-F.

b) V-V-F.

c) F-F-V.

d) V-F-V.

e) V-F-F.

2. (FGV / Prefeitura de Paulínia - SP- 2016) A empresa de desenvolvimento de sistemas "Inovation" tem ampla experiência no mercado e, até o momento,utilizou diversos modelos de ciclo de vida para o desenvolvimento de sistemas. A "Inovation" já recebeu diversas reclamações dos seus clientes por causa da demora em apresentar alguma tela em funcionamento, bem como da falta de envolvimento dos clientes no desenvolvimento. Aempresa, assim, decidiu passar a utilizar um novo modelo de ciclo de vida. Esta decisão visa aproveitar a grande experiência de sua equipe e trazer o cliente para a equipe de desenvolvimento, com iterações de desenvolvimento extremamente curtas. Qualquer membro da equipe implementa parte do código, que pode ser evoluído por qualquer outro membro.O novo modelo adotado pela "Inovation" é denominado:

a) Extremme Programming (XP).

b) Modelo V.

c) Evolutivo.

d) Incremental.

e) Espiral.

3. (FGV / Câmara Municipal do Recife-PE - 2014) Uma das práticas do método ágil XP
(eXtreme
Programming) é:

a) documentação extensiva;

b) prototipação;

c) ciclos longos de desenvolvimento;

d) desenvolvimento orientado a testes (TDD);

e) utilização de todos os artefatos do RUP.

GABARITo

1. LETRA B 2. LETRA A
3. LETRA D

LISTA DE QUESTõES - DIvERSAS BANCAS

í. (COMPERVE / TJ-RN - 2020) O método ágil Extreme Programming ou XP é um dos métodos ágeis mais conhecidos. Sobre as características desse método, é correto afirmar:
a) o planning game é uma reunião que ocorre a cada iteração com o objetivo de discutir o que foi feito na última iteração.
b) o código fonte que será executado no ambiente de produção é desenvolvido em pares,
sendo que o par se alterna nos papéis de condutor e navegador.
c) é importante tentar prever o que o cliente deseja e executar antes mesmo de comunicá -lo,mostrando proatividade na resolução de possíveis problemas.

d) o código fonte de cada página pertence a um membro da equipe. Qualquer alteração a ser realizada precisa ser informada ao respectivo membro.
2. (IBFC /TRE-PA -2020) Para aplicar valores e princípios doXP (Extreme Programming),
durante os processos e práticas ágeis de desenvolvimento de software, se propõe uma série específica de práticas. Assinale a alternativa que apresenta algumas dessas "boas práticas" utilizadas tradicionalmente em projetos, usando XP.
a) Reformation - Pair Programming - PlayStation Game b) Refactoring - Pair Programming - Planning Game c) Reformation - Pair Production - Planning Game d) Refactoring - Pair Production - PlayStation Game
3. (UFCG/ UFCG- 2019) Marque a alternativa INCORRETA com relação a
Extreme
Programming (XP).

a) Comunicação, coragem e respeito são valores dessa metodologia.

b) Em XP, uma das regras é codificar os testes de unidade primeiro.

c) Refatoramento é uma prática recomendada nesse processo.

d) O código a ser enviado para produção é criado por duas pessoas trabalhando juntas em um único computador.
e) O autor, Don Wells, exige que o processo seja seguido à risca, de forma que todas suas regras devem ser respeitadas e, nenhum projeto pode ser realizado sem adaptações e/ou remoção dessas regras.
4. (IDECAN / UNIVASF - 2019) Extreme Programming (XP), em sua essência, possui um conjunto de regras que devem serseguidas em projetos ágeis que queiram utilizá-la em sua completude.Sobre as regras do XP, assinale a alternativa correta.

a) Apenas as operações mais críticas devem possuirtestes unitários.

b) Todo o código-fonte de produção deve ser implementado em programação em pares.

c) A integração de código deve ser feita nos computadores dos desenvolvedores.

d) É importante estabelecer o papel de um XP Master, que será responsável pela implementação da metodologia.
e) A velocidade do projeto deve ser medida com o objetivo de informar ao cliente o tempo médio de correção de falhas.
5. (CESGRANRIO / UNIRIO - 2019) Uma das principais práticas de XP (Extreme
Programming) é o Iteration Planning Game. Entre as atividades realizadas em uma sessão de IterationPlanning,
está a:

a) definição, pelos programadores, de quais story cards serão implementados em uma iteração.

b) estimação do esforço que será necessário para implementar cada story card.

c) estimação da data de entrega de um release baseado na estimativa de esforço de cada story card.
d) estimação, feita por cada programador, do tempo que será necessário para realizar cada tarefa sob sua responsabilidade.
e) designação, por parte do coach, dos programadores que irão realizar as tarefas contidas na lista de tarefas.
6. (INSTITUTO AOCP/ UFPB - 2019) Um dos principais métodos ágeis de desenvolvimento de software foi concebido para impulsionar práticas reconhecidas como boas, por exemplo, o desenvolvimento iterativo a nível extremo, em que novas versões de um determinado sistema podem ser implementadas, integradas e, até mesmo, testadas em um único dia por programadores diferentes. Essa é uma das características de qual método de desenvolvimento ágil de software?
a) Scrum.

b) Adaptative Software Development.

c) Extreme Programming.

d) Pramatic Programming.

e) Test Driven Development.

7. (FCM/ Prefeitura de Caranaíba - MG - 2019) De acordo com Pressman e Maxim
(2016), a
Programação Extrema (Extreme Programming - XP) é uma abordagem amplamente utilizada do desenvolvimento ágil de software que consiste das atividades:
a) Planejamento (Planning) / Projeto (Designing) / Codificação (Coding) / Teste (Test).

b) Colaboração (Collaboration) / Projeto (Designing) / Codificação (Coding) / Teste (Test).

c) Colaboração (Collaboration) / Projeto (Designing) / Codificação (Coding) /
Teste (Test) /
Adaptação (Adaptation).

d) Colaboração (Collaboration) / Projeto (Designing) / Codificação (Coding) /
Teste (Test) /
Adaptação (Adaptation) / Melhoria (Improvement).

8. (VUNESP / Câmara de Piracicaba - SP - 2019) Um dos processos ágeis de desenvolvimento de software é a programação extrema (extreme programming - XP), cuja fase ou atividade inicial é composta pela descrição dos cenários (características e funcionalidades)requisitadas para o software a ser desenvolvido. Essa atividade recebe a denominação de:
a) métodos práticos.

b) histórias de usuário.

c) estruturas de apoio.

d) classes de projeto.

e) artefatos de usuário

9. (INSTITUTO AOCP / ADAF - AM - 2018) Na metodologia ágil Extreme Programming
(XP), a propriedade do código é coletiva, dessa forma, todos compartilham o mesmo orgulho e as mesmas críticas. Considerando o exposto, assinale a alternativa que apresenta uma das regras da codificação em XP.
a) No Overtime.

b) Eliminar gargalos de hardware no início.

c) O usuário não deve participar do planejamento das interfaces.

d) No Outsourcing.

e) No Sprint.

10. (AOCP/ SUSIPE-PA- 2018) Sobre as práticas do XP (Extreme Programming),
assinale a alternativa INCORRETA.
a) O cliente deve conduzir o desenvolvimento a partir do feedback que recebe do sistema.

b) O código deve ser padronizado, visando tornar o sistema mais homogêneo.

c) O XP trabalha com releases curtos, buscando a integração contínua de valor para o cliente.

d) O XP trabalha com código coletivo, no qual todos os membros da equipe têm acesso ao código.
e) O XP utiliza-se de programação em par para permitir que o código seja revisado permanentemente enquanto é desenvolvido.
11. (COMPERVE / UFRN - 2018) Programação Extrema (XP - Extreme Programming) é uma das principais metodologias ágeis já propostas. A respeito de XP, considere as afirmativas abaixo.
I XP promove a execução de testes automatizados de avaliação do desempenho a cada iteração de desenvolvimento do sistema.
II Em XP, os requisitos do sistema são especificados através de casos de uso.

III A prática de integração contínua do XP envolve a geração frequente de versões
(builds) do sistema, assim como execução dos testes automatizados sobre as versões geradas.
IV A prática de refatoração do XP envolve a modificação interna do código de classes do sistema,mas sem modificar seu comportamento externo (interfaces dos métodos).

Estão corretas as afirmativas a) III e IV.
b) I e II.

c) I e III.

d) lie IV.

12. (COMPERVE / UFRN - 2018) Programação Extrema (XP - Extreme Programming) é uma das principais metodologias ágeis já propostas. Considere as seguintes afirmativas a respeito de suas práticas.
I A técnica de refatoração promove mudanças no código que visam à adição de novas funcionalidades.
II XP determina a produção de um executável do sistema desenvolvido a cada iteração.

III XP motiva a criação de projetos simples onde requisitos futuros não são inicialmente contemplados.
IV Integração contínua consiste na geração de builds diários do sistema.

Estão corretas as afirmativas a) lie IV.
b) I e IV.

c) I e III.

d) lie III.

13. (IF-RS / IF-RS - 2018) Sobre as práticas encontradas na metodologia ágil de desenvolvimento de software, conhecida por Programação Extrema (XP Programming), de acordo com Dooley(2017) no livro Software Development, Design and Coding, classifique cada uma das afirmativas abaixo como verdadeira (V) ou falsa (F) e assinale a alternativa que apresenta a sequênciaCORRETA, de cima para baixo:

() Participação intensa do representante do cliente no desenvolvimento do projeto.

() Testes são realizados continuamente. Quando todos os testes forem aprovados, o módulo foi concluído.
() Programação em par: enquanto um escreve o código, o outro monitora falhas, realiza testes,faz sugestões e planeja próximas ações.

() Lançamentos frequentes de novas versões.

a) F-V-V-F

b) V-F-F-V

c) V-V-F-V

d) V-V-V-V

e) F-F-V-V

14. (IADES/ ARCON-PA- 2018) Um dos métodos de desenvolvimento de software mais conhecido e utilizado é o extreme programming (XP). Esse consiste em um modelo:
a) que evita a refatoração de código.

b) que realiza testes de integração apenas ao final de todo o desenvolvimento.

c) que valoriza o trabalho de forma individualizada, evitando a programação em pares.

d) que busca atenderás necessidades atuais, e nada mais.

e) no qual não se faz necessária a disponibilidade de um representante do cliente a todo o tempo.
15. (FAURGS / TJ-RS - 2018) Considere as seguintes afirmações sobre princípios ou práticas da XP(Extreme Programming).

I - Um representante do usuário final do sistema (cliente) deve estar disponível todo o tempo à equipe de XP. Em um processo de Extreme Programming, o cliente é um membro da equipe de desenvolvimento e é responsável por levar ao grupo os requisitos de sistema para implementação.
II - Todos os desenvolvedores devem refatorar o código continuamente, assim que encontrarem oportunidades de melhorias de código.
III - Os desenvolvedores trabalham em todas as áreas do sistema, de modo que não se desenvolvam ilhas de expertise. Todos os desenvolvedorestêm responsabilidade em relação ao código; qualquer um pode mudar qualquer coisa.
Quais estão corretas?

a) Apenas I.

b) Apenas I e II.

c) Apenas I e III.

d) Apenas II e III.

e) I, lie III.

i6.(FUNRIO / Câmara de São João de Meriti - RJ - 2018) A figura abaixo ilustra a metodologiaExtreme Programming (XP) que usa uma abordagem orientada a objetos, incluindo um conjunto de regras e práticas que ocorrem ao longo do desenvolvimento do projeto.
As fases I, II, III e IV são denominadas respectivamente:

a) modelagem, construção, implantação e homologação.

b) planejamento, construção, codificação e homologação.

c) planejamento, projeto, implantação e teste.

d) planejamento, projeto, codificação e teste.

e) modelagem, projeto, codificação e homologação.

17. (INSTITUTO AOCP / PRODEB - 2018) O método de desenvolvimento ágil denominado de XP
(Extreme Programming) tem sua estrutura baseada em algumas prerrogativas, dentre as quais,é correto citar como princípios do XP:

a) Princípio da Legalidade, Princípio da Agilidade e Princípio do Feedback.

b) Princípio da Coragem, Princípio da Agilidade e Princípio da Simplicidade.

c) Princípio da Comunicação, Princípio da Simplicidade, Princípio do Feedback e
Princípio da
Coragem.

d) Princípio da Agilidade, Princípio da Qualidade, Princípio do Feedback e Princípio da Coragem.

e) Princípio da Simplicidade, Princípio do Desenvolvimento e Princípio de Governança.

18. (INSTITUTO AOCP / PRODEB - 2018) O Pair Programming (Programação em Pares) é uma característica de um determinado método de desenvolvimento de software em que dois programadores trabalham juntos no desenvolvimento de um código. Qual foi o método que criou essa prática?
a) Lean.

b) XP.

c) Scrum.

d) FDD.

e) Cascata.

ig.(INSTITUTO AOCP / UFOB- 2018) Uma das práticas do Extreme Programming é o uso do código coletivo, na qual todos os desenvolvedores têm acesso ao código.
20. (IBADE / IPM - JP-2018) Metodologias ágeis podem ser aplicadas para facilitar a adaptação do processo de desenvolvimento de software a mudanças. Trata-se de uma abordagem de desenvolvimento de software ágil amplamente conhecida e utilizada, denominada:
a) desenvolvimento direto.

b) modelagem extrema.

c) programação dinâmica.

d) modelagem direta.

e) programação extrema.

21. (INSTITUTO AOCP/ PRODEB - 2018) Extreming Programming (XP) é um método de desenvolvimento ágil amplamente utilizado pelas software houses. Com base neste método,qual alternativa a seguir possui uma prática que NÃO faz parte do XP?

a) Small Releases (Pequenas Entregas).

b) Pair Programming (Programação em Pares).

c) Sprint Review (Reunião de revisão da Sprint).

d) Sustainable Pace (Ritmo Saudável).

e) Collective Owership (Posse Coletiva).

22. (IBFC / TJ-PE - 2017) Está sendo implementado o XP (eXtreme Programming) em uma equipe de TI. Para tanto, está sendo colocada a seguinte série de práticas específicas da metodologiaXP em análise:

I. Programação Pareada (Pair Programming).

II. Fases pequenas (Small Releases).

III. Refatoração (Refactoring).

IV. Jogo de Planejamento (Planning Game).

Com base no seu conhecimento sobre a metodologia citada acima, suas práticas específicas estão corretamente relacionadas nos itens:
a) I, II e III, apenas b) I, II e IV, apenas c) II, III e IV, apenas d) I, III e IV, apenas e) 1,11, III e IV
23. (UFG / SANEAGO-2017) Dentro doframework Extreme Programming (XP), uma metodologia ágil, a ação de teste de código é responsabilidade da pessoa:
a) diretamente ligada à criação do artefato em questão.

b) responsável pela equipe de teste de software, que não pode ser a pessoa que o desenvolve.

c) utilizadora do código diariamente.

d) facilitadora da comunicação entre a equipe de desenvolvimento e o cliente.

24.OBFC / EBSERH- 2017) Dentro das práticas do XP (eXtreme Programming)
existe uma fundamental que é o Jogo de Planejamento (Planning Game). Para serem realizadas adequadamente essas reuniões com os usuários, deve(m) ter sido feito(s) antecipadamente:
a) o Sustainable Pace b) as Small Releases c) os CustomerTests d) as User Stories e) um Simple Design
25. (COPEVE-UFAL / UFAL - 2016) Assinale a alternativa que contém apenas características ou práticas relacionadas ao método ágil para desenvolvimento de softwares ExtremeProgramming (XP):

a) Planejamento incremental, cliente disponível em tempo integral e programação em pares.

b) Requisitos expressos como cenários, programação incremental e programação individual.

c) Cliente não participa do desenvolvimento, desenvolvimento em cascata e programação em pares.
d) Equipe heterogênea especializada, requisitos expressos como histórias e desenvolvimento em espiral.
e) Toda equipe altera qualquer parte do código, desenvolvimento em cascata e programação individual.
26. (IF-PE / IF-PE - 2016) Extreme Programming é uma metodologia ágil para equipes pequenas e médias que desenvolvem software com requisitos vagos e em constante mudança. Sobre os valores do XP, analise as definições abaixo e assinale a alternativa CORRETA.
a) Simplicidade - procura-se que a equipe concentre-se, primeiro, em fazer o necessário.

b) Comunicação - prioriza-se a troca de e-mail como melhor forma de comunicação,independente do horário.

c) Coragem - a metodologia XP prega coragem para dizer "não" ao cliente e evitar mudanças do projeto.
d) Feedback- é valorizado o feedback positivo do cliente. Desta forma,
procura-se evitar a entrega de software sem a realização de testes detalhados.
e) Respeito - prega o respeito à hierarquia, ouvindo e respeitando, apenas, o que é determinado pelo líder de projeto.
27. (UFCG / UFCG - 2016) Sobre XP (Extreme Programming), marque a assertiva INCORRETA.

a) É um processo criado por Kent Beck.

b) São exemplos de boas práticas do processo: desenvolvimento orientado a testes, pair programming e documentação em todas as suas fases.
c) Esse processo almeja reduzir o custo de mudanças a partir de múltiplos ciclos de desenvolvimento de curta duração.
d) Simplicidade ao projetar e programar é uma das chaves para o sucesso na visão do XP.

e) Nesse processo, deve-se refatorar o código sempre que possível.

28.(IF-SE / IF-SE - 2016) A Programação Extrema (Extreme Programming - XP) possui diversas práticas. Analise as afirmativas abaixo.
I. As releases do sistema são frequentes e incrementais.

II. Os requisitos são representados através de casos de uso.

III. Os desenvolvedores não trabalham em pares.

IV. Depois de qualquer integração, todos os testes de unidade devem passar.

De acordo com as afirmativas, marque a alternativa CORRETA

a) As afirmativas I e II estão incorretas.

b) Apenas as afirmativas I e II estão corretas.

c) As afirmativas II e III estão incorretas d) As afirmativas III e IV estão incorretas
2g.(IF-PE/ IF-PE - 2016) Com relação à metodologia ágil de desenvolvimento de software conhecido como eXtreme Programming (XP), quais são os quatro processos ou atividades metodológicas encontradas nela?
a) Análise, projeto, codificação e teste.

b) Planejamento, análise, projeto e codificação.

c) Planejamento, projeto, codificação e testes.

d) Planejamento, análise, codificação e testes.

e) Levantamento, análise, projeto e codificação.

3o.(IBFC/ EBSERH - 2016) Equipes XP (eXtreme Programming) planejam utilizando histórias escritas em pequenos cartões. Essas histórias devem ter como objetivo:
a) a modelagem de dados b) as métricas de software c) os requisitos não-funcionais d) os requisitos funcionais e) tanto os requisitos funcionais como os requisitos não-funcionais
3i.(IBFC / EBSERH - 2016) Para aplicar os valores e princípios durante o desenvolvimento de software, a Programação Extrema (eXtreme Programming - XP) propõe uma série de práticas.Selecione a única alternativa que NÃO seja uma dessas práticas:

a) Time Coeso (Whole Team).

b) Design Complexo (Complex Design).

c) Programação Pareada (Pair Programming).

d) Semana de 40 horas (Sustainable Pace).

e) Refatoração (Refactoring).

32.(IDECAN/ INMETRO - 2015) Na extreme programming, todos os requisitos são expressos como cenários (chamados histórias do usuário) que são implementados diretamente como uma série de tarefas. Sabe-se que o extreme programming envolve um número de práticas que se enquadram nos princípios dos métodos ágeis. Acerca de algumas dessas práticas,relacione adequadamente as colunas a seguir.
1. Releases pequenos.

2. Refactoring.

3. Propriedade coletiva.

4. Integração contínua.

5. Ritmo sustentável.

() Os pares de desenvolvedores trabalham em todas as áreas do sistema, de tal maneira que não se formem ilhas de conhecimento.
( )O conjunto mínimo útil de funcionalidade que agrega valor ao negócio é desenvolvido primeiro.
() Grandes quantidades de horas-extras não são consideradas aceitáveis, pois, no médio prazo,há uma redução na quantidade de código e na produtividade.

( ) Espera-se que todos desenvolvedores recriem o código continuamente tão logo os aprimoramentos do código forem encontrados.
() Tão logo o trabalho em uma tarefa seja concluído, este é integrado ao sistema como um todo a) 5, 3, T 4, 2.
B) 2, 4, 3, 5,1.

c) 4, 5, 2,1, 3-

d) 3,1, 5, 2, 4.

e) 5, 2, 4, 3, i-

33. (UFPel-CES / UFPEL - 2015) Em projetos nos quais se aplicam o método ágil XP, a fase em que o propósito é empresa e cliente concordarem em uma data na qual o menor e melhor conjunto de histórias de usuários deverá ser implementado é a fase de:
a) planejamento.

b) exploração.

c) iterações e entregas.

d) produção.

e) manutenção.

34-(CS-UFG/ AL-GO- 2015) Extreme Programming (XP) é um exemplo de método ágil que foi definido por Kent Beck. O XP inclui uma abordagem de teste que:
a) valoriza o desenvolvimento test-last.

b) depende da técnica de teste baseada em defeitos c) desenvolve teste incremental baseado em cenários d) utiliza processo de teste dirigido a planos.
35. (CETRO / AMAZUL- 2015) Assinale a alternativa que não apresenta um princípio/ valor da metodologia de desenvolvimento de software XP (Extreme Programming):
a) Simplicidade.

b) Programação individual ou não em pares.

c) Comunicação.

d) Coragem.

e) Feedback.

36. (IESES / TRE-MA - 2015) No desenvolvimento de software em XP, são empregadas algumas práticas. Avalie as assertivas abaixo:
I. Programação em pares.

II. Time coeso.

III. Integração contínua.

IV. Desenvolvimento orientado a testes.

Quantas afirmativas são verdadeiras?

a) 2

b) 1

c) 4

d) 3

37. (FUNCAB / SEFAZ-BA - 2014) São características do Extreme Programming (XP), EXCETO:

a) apresentar desenvolvimento incremental.

b) admitir a existência de uma especificação detalhada.

c) utilizar programação com pares de desenvolvedores.

d) permitir a integração de usuário com o time de desenvolvimento.

e) suportar testes automáticos contínuos.

38. (INSTITUTO AOCP/ MPE-BA- 2014) O processo ágil XP possui doze práticas que são os princípios fundamentais do processo. A prática que encoraja a equipe inteira a trabalhar mais unida em busca de qualidade no código fazendo melhorias e refatoramentos em qualquer parte do código a qualquer tempo é conhecida como:
a) propriedade coletiva do código.

b) semana de quarenta horas.

c) programação em pares.

d) padrões de codificação.

e) integração contínua.

39. (FUNCAB / MDA- 2014) A " Extreme Programming - XP" representa um dos mais conhecidos métodos ágeis. Uma das práticas utilizadas na XP é:
a) empregar um esquema em que os desenvolvedores trabalham individualmente.

b) integrar o sistema exclusivamente quando todos os módulos forem concluídos.

c) usar cenários para expressar requisitos implementados como uma série de tarefas.

d) impedir que o cliente interaja com a equipe de desenvolvimento na fase de especificação.

e) eliminar a necessidade da realização de testes durante a fase de desenvolvimento.

40. (CESGRANRIO / Banco da Amazônia - 2014) Uma prática que NÃO é adotada por Extreme
Programming (XP) é a) usarduas pessoas trabalhando juntas em um único computador para produzirtodo o código que será enviado para a produção.
b) criar os testes antes do código que será testado.

c) refatorar frequentemente, e ao longo de todo o projeto, o código produzido pelos desenvolvedores.
d) integrar continuamente o código recém-produzido com o código existente no repositório.

e) variar a duração de cada iteração durante todo o projeto para acomodar eventuais mudanças de prioridade dos requisitos, definidas pelo cliente.
4i.(CESGRANRIO / BNDES - 2013) Sendo atualmente conhecida por just-in-time, a produção enxuta contém princípios que compõem a base dos processos ágeis de desenvolvimento de software, como o Extremme Programming (XP). Um dos princípios básicos do XP, a eliminação de desperdícios, busca:
a) evitar o efeito negativo que uma definição de risco, na fase inicial do projeto, possa causar na performance do software como um todo, tendo, como saída, informações não relevantes para o processo.
b) produzir requisitos bem definidos e completos de forma a abranger todos os processos e rotinas administrativas, funcionais e produtivas almejadas pelos stakeholders envolvidos no projeto.
c) reduzir, o máximo possível, o volume de trabalho executado e os subprodutos envolvidos nesse trabalho, concentrando os esforços apenas no que pode produzir um resultado objetivo e palpável ao cliente final.
d) descrever os processos que garantam a inclusão, no projeto, de todo o serviço necessário, e somente o serviço necessário, para que esse projeto seja finalizado com sucesso.
e) descrever os processos envolvidos no planejamento, no monitoramento e na garantia de que o projeto será realizado dentro dos prazos definidos no escopo, mantendo a qualidade definida e o enxugamento dos custos inicialmente programados.
42.(INSTITUTO AOCP / EBSERH - 207) O Extreme Programming (XP) surgiu em 1999, a partir de uma publicação sobre o assunto, mas suas bases se conectam a princípios da década de 80 e ao manifesto ágil. O XP é baseado em 4 atividades de arcabouços. Assinale a alternativa que contém 3 desses arcabouços:
a) Levantamento de requisitos, análise de negócio, planejamento e documentação.

b) Levantamento de requisitos, planejamento, documentação e implantação.

c) Levantamento de requisitos, documentação, codificação e teste.

d) Planejamento, projeto, documentação e implantação.

e) Governança, planejamento, codificação e teste.

GABARITo

1. LETRA B 15- LETRA E
29. LETRA C

2. LETRA B 16. LETRA D
30. LETRA D

3- LETRA E 17- LETRAC
3i- LETRA B

4- LETRA B i8. LETRA B
32. LETRA D

5- LETRA D 19. CORRETO
33- LETRA A

6. LETRAC 20. LETRA E
34- LETRA C

7- LETRA A 21. LETRA C
35- LETRA B

8. LETRA B 22. LETRA E
36. LETRAC

9- LETRA A 23- ANULADA
37- LETRA B

10. LETRA D 24. LETRA D
38. LETRA A

íi. LETRA A 25- LETRA A
39- LETRA C

12. LETRA D 26. LETRA A
40. LETRA E

13- LETRA D 27- LETRA B
41. LETRA C

14- LETRA D 28. LETRAC
42. LETRA E

