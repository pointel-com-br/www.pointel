# Desenvolvimento de Informação - Processamento de Dados. Massivo e paralelo. Batch. Real time. MapReduce

Índice

1) Processamento de Dados

Conteúdo da aula
Processamento de Dados

Conceitos de processamento massivo e paralelo
Processamento em lote (batch) e em Tempo Real

Ferramentas de processamento e streaming de dados em tempo real

CAVALCANTI

PROFESSOR

CoNTEÚDo DA AULA

Processamento de dados. Conceitos de processamento massivo e paralelo. Processamento em lote(batch). Processamento em tempo real (real time).

PRoCESSAMENTo DE DADoS

Nos últimos 60 anos, a tecnologia da computação passou por uma série de mudanças de plataforma e ambiente. Em vez de usar um computador centralizado para resolver problemas computacionais,um sistema de computação paralelo e distribuído usa vários computadores para resolver problemas de grande escala na Internet. Assim, a computação distribuída torna-se intensiva em dados e centrada na rede.
Bilhões de pessoas usam a Internet todos os dias. Como resultado, sites de supercomputadores e grandes centros de dados devem fornecer serviços de computação de alto desempenho para muitos usuários da Internet simultaneamente. Devido a essa alta demanda, o LinpackBenchmark para aplicativos de computação de alto desempenho (HPC) não é mais ideal para medir o desempenho do sistema. O surgimento de computação na nuvem, em vez disso, exige sistemas de computação de alto rendimento (HTC) construídos com tecnologias de computação paralela e distribuída.
Por muitos anos, os sistemas HPC enfatizam o desempenho de velocidade bruta. A
velocidade dos sistemas HPC aumentou de Gflops no início de 1990 para agora Pflops em 2010. Essa melhoria foi impulsionada principalmente pelas demandas das comunidades científicas, de engenharia e de manufatura. Por exemplo, os 500 sistemas de computador mais poderosos do mundo são medidos pela velocidade de ponto flutuante nos resultados de benchmark Linpack. No entanto, o número de usuários de supercomputadores é limitado a menos de 10% de todos os usuários de computador.
A comunidade de alta tecnologia discutiu por muitos anos sobre as definições precisas de computação centralizada, computação paralela, computação distribuída e computação em nuvem. Em geral, a computação distribuída é o oposto da computação centralizada. O campo da computação paralela se sobrepõe à computação distribuída em grande medida, e a computação em nuvem se sobrepõe à computação distribuída, centralizada e paralela. A lista a seguir define esses termos com mais clareza:
* Computação centralizada - este é um paradigma de computação pelo qual todos os recursos do computador são centralizados em um sistema físico. Todos os recursos (processadores,memória e armazenamento) são totalmente compartilhados e fortemente acoplados em um sistema operacional integrado. Muitos data centers e supercomputadores são sistemas centralizados,mas são usados em aplicações paralelas, distribuídas e de computação em nuvem.
* Computação paralela - na computação paralela, todos os processadores estão fortemente acoplados à memória compartilhada centralizada ou fracamente acoplados à memória distribuída. Alguns autores referem-se a esta disciplina como processamento paralelo. Acomunicação entre processadores é realizada por meio de memória compartilhada ou por meio de passagem de mensagens. Um sistema computacional capaz de executar a computação paralela é comumente conhecido como computador paralelo. Os programas executados em um computador paralelo são chamados de programas paralelos. O processo de escrever programas paralelos é muitas vezes referido como programação paralela.
* Computação distribuída - este é um campo da ciência/engenharia da computação que estuda sistemas distribuídos. Um sistema distribuído consiste em vários computadores autônomos, cada um com sua própria memória privada, comunicando-se através de uma rede de computadores.A
troca de informações em um sistema distribuído é realizada por meio de mensagens. Um programa de computador executado em um sistema distribuído é conhecido como programa distribuído.O
processo de escrever programas distribuídos é conhecido como programação distribuída.

* Computação em nuvem - uma nuvem de recursos na Internet pode ser um sistema de computação centralizado ou distribuído. A nuvem aplica computação paralela ou distribuída,ou ambas. As nuvens podem ser construídas com recursos físicos ou virtualizados em grandes data centers centralizados ou distribuídos. Alguns autores consideram a computação em nuvem como uma forma de computação utilitária ou computação como serviço.
Quando os aplicativos de software modernos são executados lentamente, o problema geralmente é ter muitos dados a serem processados. Os aplicativos manipulam imagens ou vídeos, com milhões a trilhões de pixels. Aplicações científicas modelam a dinâmica de fluidos usando bilhões de células de grade. As aplicações de dinâmica molecular devem simular interações entre milhares a milhões de átomos. A programação de companhias aéreas lida com milhares de voos, tripulações e portões de aeroportos.
É importante ressaltar que a maioria desses pixels, partículas, células, interações,
voos e assim por diante pode ser tratada de forma bastante independente. A conversão de um pixel colorido em escala de cinza requer apenas os dados desse pixel. O desfoque de uma imagem calcula a média da cor de cada pixel com as cores dos pixels próximos, exigindo apenas os dados dessa pequena vizinhança de pixels. Mesmo uma operação aparentemente global, como encontrar o brilho médio de todos os pixels em uma imagem, pode ser dividido em muitos cálculos menores que podem ser executados independentemente.
Essa avaliação independente é a base do paralelismo de dados que trata de
(re)organizar o processamento em torno dos dados, de modo que possamos executar as computações independentes em paralelo para concluir o trabalho geral mais rapidamente, geralmente muito mais rápido.
CoNCEIToS DE PRoCESSAMENTo MASSIvo E PARALELo.

No mundo de hoje, você encontrará muitos desafios que exigem o uso extensivo e eficiente de recursos de computação. A maioria das aplicações que requerem desempenho tradicionalmente estavam no domínio científico. Mas, com o uso da inteligência artificial (IA) e dos aplicativos de aprendizado de máquina a demanda por processamento cresceu e a quantidade de usuários cresceu em diversas frentes. Alguns exemplos dessas aplicações incluem:
* Modelagem de incêndios para auxiliar as equipes de bombeiros e ajudar a população

* Modelagem de tsunamis e tempestades de furacões

* Reconhecimento de voz para interfaces de computador

* Modelagem de disseminação de vírus e desenvolvimento de vacinas

* Modelagem das condições climáticas ao longo de décadas e séculos

* Reconhecimento de imagem para tecnologia de carros autônomos

* Equipar as equipes de emergência com simulações em execução de perigos, como inundações

* Reduzindo o consumo de energia para dispositivos móveis

Com as técnicas de processamento paralelo, é possível lidar com problemas e conjuntos de dados maiores, além de executar simulações dez, cem ou até mil vezes mais rápido. Os aplicativos típicos deixam grande parte da capacidade de computação dos computadores atuais inexplorada. Acomputação paralela é a chave para liberar o potencial dos recursos. Então, o que é computação paralela e como você pode usá-la para turbinar a execução dos seus aplicativos?
A computação paralela é a execução de muitas operações em uma única instância no tempo. Aexploração completa da computação paralela não acontece automaticamente. Requer algum esforço do programador. Primeiro, você deve identificar e expor o potencial de paralelismo em um aplicativo. Potencial paralelismo ou simultaneidade, significa que você certifica que é seguro realizar operações em qualquer ordem à medida que os recursos do sistema se tornam disponíveis.E, com a computação paralela, há um requisito adicional: essas operações devem ocorrer ao mesmo tempo. Para que isso aconteça, você também deve aproveitar adequadamente os recursos para executar essas operações simultaneamente.
A computação paralela introduz novas preocupações que não estão presentes em um mundo serial. Precisamos mudar nossos processos de pensamento para nos adaptarmos às complexidades adicionais da execução paralela. Esta aula inicia sua descoberta sobre como acessar o poder da computação paralela, mas você poderá expandir os horizontes depois da aprovação no concurso.
A vida apresenta inúmeros exemplos de processamento paralelo, e essas instâncias muitas vezes se tornam a base para estratégias de computação. A figura a seguir mostra uma fila de caixa de supermercado, onde o objetivo é fazer com que os clientes paguem rapidamente pelos itens que desejam comprar. Isso pode ser feito empregando vários caixas para processar ou fazer o "check-out" dos clientes, um de cada vez. Nesse caso, os caixas qualificados podem executar mais rapidamente o processo para que os clientes saiam mais rapidamente.
Outra estratégia é empregar muitas estações de autoatendimento e permitir que os clientes executem o processo por conta própria. Essa estratégia exige menos recursos humanos do supermercado e pode abrir mais vias para processar os clientes. Os clientes podem não conseguir fazer o check-out com a mesma eficiência de um caixa treinado.
Resolvemos problemas computacionais desenvolvendo algoritmos: um conjunto de etapas para alcançar um resultado desejado. Na analogia do supermercado, o processo de check-out é o algoritmo. Nesse caso, inclui descarregar itens de uma cesta, escanear os itens para obter um preço e pagar pelos itens. Este algoritmo é sequencial (ou serial); deve seguir esta ordem.Se houver centenas de clientes que precisam executar essa tarefa, o algoritmo para verificar muitos clientes contém um paralelismo que pode ser aproveitado. Teoricamente, não há dependência entre dois clientes que passam pelo processo de checkout. Ao usar várias linhas de caixa ou estações de autoatendimento, os supermercados expõem o paralelismo, aumentando assim a taxa em que os clientes compram mercadorias e saem da loja. Cada escolha de como implementamos esse paralelismo resulta em custos e benefícios diferentes.
15 items or less
/) r'\

I
I
I

▼

Figuro 1- Porolelismo cotidiano em filas de caixas de supermercados. Os caixas de checkout (com bonés) processam sua fila de clientes (com cestas). À esquerda, um caixa processa quatro filas de autoatendimento simultaneamente. À direita,é necessário um caixa para cada fila de caixa. Cada opção afeta os custos do supermercado e as taxas de checkout.
DEFINIÇÃO Computação paralela é a prática de identificar e expor o paralelismo em algoritmos,expressá-lo em nosso software e compreender os custos, benefícios e limitações da implementação escolhida.
No final, a computação paralela é sobre desempenho. Isso inclui mais do que trabalhar aspectos de velocidade, mas também entender o tamanho do problema e a eficiência energética. Nosso objetivo é fornecer a você uma compreensão da amplitude do campo atual de computação paralela e familiarizá-lo com o suficiente das linguagens, técnicas e ferramentas mais usadas para que você possa enfrentar questões de prova sobre computação paralela com confiança. Decisões importantes sobre como incorporar o paralelismo geralmente são tomadas no início de um projeto. Um design racional é um passo importante para o sucesso. Evitar a etapa de design pode levar a problemas muito mais tarde. É igualmente importante manter as expectativas realistas e conhecer os recursos disponíveis e a natureza do projeto.
Outro objetivo desta aula é apresentar a terminologia usada na computação paralela.
Como esse campo e a tecnologia cresceram de forma incremental, o uso de muitos dos termos na comunidade é muitas vezes desleixado e impreciso. Com o aumento da complexidade do hardware e do paralelismo dentro dos aplicativos, é importante estabelecermos um uso claro e inequívoco da terminologia.
Bem-vindo ao mundo da computação paralela! À medida que você se aprofunda, as técnicas e abordagens se tornam mais naturais e você descobrirá que seu poder é cativante.
Por que você deve aprender sobre computação paralela?

O futuro é paralelo. O aumento no desempenho serial se estabilizou à medida que os designs dos processadores atingiram os limites de miniaturização, frequência de clock, potência e até calor. Afigura abaixo mostra as tendências na frequência de clock (a taxa na qual uma instrução pode ser executada), consumo de energia, número de núcleos computacionais (ou núcleos para abreviar) e desempenho de hardware ao longo do tempo para processadores comuns.
Figura 2 - Desempenho de thread único, frequência de clock da CPU (MHz), consumo de energia da CPU
(watts) e o número de núcleos da CPU
de 1970 a 2018. A era da computação paralela começa por volta de 2005, quando a contagem de núcleos nos chips da CPU começa a aumentar, enquanto a frequência do clock e o consumo de energia se estabilizam, mas o desempenho aumenta constantemente.
Em 2005, o número de núcleos aumentou abruptamente de um único núcleo para vários núcleos. Ao mesmo tempo, a frequência do relógio e o consumo de energia se estabilizaram. Odesempenho teórico aumentou constantemente porque o desempenho é proporcional ao produto da frequência de clock e o número de núcleos. Essa mudança para aumentar o número de núcleos em vez da velocidade do clock indica que alcançar o desempenho ideal de uma unidade de processamento central (CPU) só está disponível por meio de computação paralela.
O hardware de computação moderno vem equipado com várias unidades de processamento central(CPUs) e/ou unidades de processamento gráfico (GPUs) que processam vários conjuntos de instruções simultaneamente. Esses sistemas menores geralmente rivalizam com o poder de computação dos supercomputadores de duas décadas atrás. Fazer uso total dos recursos de computação (em laptops, estações de trabalho, smartphones e assim por diante) exige que você, o programador, tenha um conhecimento prático das ferramentas disponíveis para escrever aplicativos paralelos. Você também deve entender os recursos de hardware que aumentam o paralelismo.
Como existem muitos recursos de hardware paralelos diferentes, isso apresenta novas complexidades para o programador. Um desses recursos é o hyperthreading,introduzido pela
Intel.Ter duas filas de instruções intercalando o trabalho para as unidades lógicas de hardware permite que um único núcleo físico apareça como dois núcleos para o sistema operacional (SO). Os processadores vetoriais são outro recurso de hardware que começou a aparecer em processadores comuns por volta de 2000. Eles executam várias instruções ao mesmo tempo. A largura em bits do processador vetorial (também chamado de unidade vetorial) especifica o número de instruções a serem executadas simultaneamente. Assim, uma unidade vetorial de 256 bits de largura pode executar quatro instruções de 64 bits (doubles) ou oito de 32 bits(single-precision) ao mesmo tempo.
Vejamos um exemplo ...

Vamos pegar uma CPU de 16 núcleos com hyperthreading e uma unidade vetorial de 256
bits de largura, comumente encontrada em desktops domésticos. Um programa serial usando um único núcleo e sem vetorização usa apenas 0,8% da capacidade teórica de processamento deste processador! O cálculo é
16 núcleos x 2 hyperthreads x (unidade de vetor de 256 bits de largura)/(double de 64 bits) =

paralelismo de 128 vias onde 1 caminho serial dividido pelos 128 caminhos paralelos = 0,008 ou 0,8%. A figura a seguir mostra que esta é uma pequena fração do poder total de processamento da CPU.
Serial 0.8%

Parallel 99.2%

Figura 3 - Um aplicativo serial acessa apenas 0,8% do poder de processamento de uma CPU de 16
núcleos.

Calcular expectativas teóricas e realistas para desempenho em série e paralelo, conforme mostrado neste exemplo, é uma habilidade importante. Algumas melhorias nas ferramentas de desenvolvimento de software ajudaram a adicionar paralelismo aos nossos kits de ferramentas e,atualmente, a comunidade de pesquisa está fazendo mais, mas ainda está longe de resolver a lacuna de desempenho. Isso coloca muito peso sobre nós, os desenvolvedores de software, para obter o máximo de uma nova geração de processadores.
Infelizmente, os desenvolvedores de software demoraram a se adaptar a essa mudança fundamental no poder da computação. Além disso, a transição de aplicativos atuais para usar arquiteturas paralelas modernas pode ser assustadora devido à explosão de novas linguagens de programação e interfaces de programação de aplicativos (APIs). Mas um bom conhecimento prático de seu aplicativo, a capacidade de ver e expor o paralelismo e uma sólida compreensão das ferramentas disponíveis podem resultar em benefícios substanciais. Exatamente que tipo de benefícios os aplicativos veriam? Vamos olhar mais de perto.
Quais são os benefícios potenciais da computação paralela?

A computação em paralelo pode reduzir o tempo de solução, aumentar a eficiência energética em seu aplicativo e permitir que você resolva problemas maiores no hardware existente. Hoje, a computação paralela não está presente apenas nos maiores sistemas de computação. Atecnologia agora está presente no desktop ou laptop de todos, e até mesmo em dispositivos portáteis. Isso possibilita que todos os desenvolvedores de software criem software paralelo em seus sistemas locais, expandindo muito a oportunidade para novos aplicativos.
Pesquisas de ponta da indústria e da academia revelam novas áreas para computação paralela à medida que o interesse se amplia da computação científica para aprendizado de máquina,big data,
computação gráfica e aplicativos de consumo. O surgimento de novas tecnologias,
como carros autônomos, visão computacional, reconhecimento de voz e IA, exige grandes recursos computacionais tanto no dispositivo do consumidor quanto na esfera de desenvolvimento, onde grandes conjuntos de dados de treinamento devem ser consumidos e processados. Na computação científica, que há muito tem sido o domínio exclusivo da computação paralela, também existem novas e empolgantes possibilidades. A proliferação de sensores remotos e dispositivos portáteis que podem alimentar dados em cálculos maiores e mais realistas ajudando na tomada de decisões, por exemplo, em torno de desastres naturais e causados pelo homem permite dados mais extensos.
Deve ser lembrado que a computação paralela em si não é o objetivo. Em vez disso, os objetivos são os resultados da computação paralela: reduzir o tempo de execução, realizar cálculos maiores ou diminuir o consumo de energia. Vejamos de forma mais organizada os benefícios da computação paralela.
* Tempo de execução mais rápido com mais núcleos de computação

Redução do tempo de execução de um aplicativo ou a aceleração, muitas vezes é considerado o objetivo principal da computação paralela. Na verdade, este é geralmente o seu maior impacto. Acomputação paralela pode acelerar cálculos intensivos, processamento multimídia e operações de big data, quer seus aplicativos levem dias ou até semanas para processar ou os resultados sejam necessários em tempo real.
No passado, o programador gastava maiores esforços na otimização serial para extrair algumas melhorias percentuais. Agora, existe o potencial para ordens de magnitude de melhoria com vários caminhos para escolher. Isso cria um problema na exploração dos possíveis paradigmas paralelos-mais oportunidades do a mão de obra disponível. Mas, um conhecimento profundo do seu aplicativo e uma consciência das oportunidades de paralelismo podem levá-lo a um caminho mais claro para reduzir o tempo de execução dos seus aplicativos.
* Tamanhos de problemas maiores com mais nós de computação

Usando o paralelismo em seu aplicativo, você pode aumentar o tamanho do seu problema para dimensões que estavam fora do alcance em um aplicativo serial. Isso ocorre porque a quantidade de recursos de computação determina o que pode ser feito, e expor o paralelismo permite operar em recursos maiores, apresentando oportunidades que nunca foram consideradas antes. Os tamanhos maiores são habilitados por maiores quantidades de memória principal,armazenamento em disco, largura de banda em redes e em disco e CPUs. Em analogia com o supermercado, como mencionado anteriormente, expor o paralelismo é equivalente a empregar mais caixas ou abrir mais caixas de autoatendimento para atender um número maior e crescente de clientes.
* Eficiência energética fazendo mais com menos

Uma das novas áreas de impacto da computação paralela é a eficiência energética. Com o surgimento de recursos paralelos em dispositivos portáteis, o paralelismo pode acelerar os aplicativos. Isso permite que o dispositivo retorne ao "modo de suspensão" mais cedo e permite o uso de processadores mais lentos, porém mais paralelos, que consomem menos energia.Assim,
mover aplicativos multimídia pesados para rodar em GPUs pode ter um efeito mais dramático na eficiência energética, ao mesmo tempo em que resulta em um desempenho muito melhor. Oresultado líquido do emprego do paralelismo reduz o consumo de energia e prolonga a vida útil da bateria, o que é uma forte vantagem competitiva neste nicho de mercado.
Outra área em que a eficiência energética é importante é com sensores remotos,
dispositivos de rede e dispositivos operacionais implantados em campo, como estações meteorológicas remotas. Muitas vezes, sem grandes fontes de alimentação, esses dispositivos devem ser capazes de funcionar em pequenos pacotes com poucos recursos. O paralelismo expande o que pode ser feito nesses dispositivos e descarrega o trabalho do sistema de computação central em uma tendência crescente que é chamada de computação de borda. Mover a computação para a borda da rede permite o processamento na origem dos dados, condensando-os em um conjunto de resultados menor que pode ser enviado mais facilmente pela rede.
Calcular com precisão os custos de energia de uma aplicação sem medições diretas do uso de energia é um desafio. No entanto, você pode estimar o custo multiplicando a potência do projeto térmico do fabricante pelo tempo de execução do aplicativo e o número de processadores usados. Apotência de projeto térmico é a taxa na qual a energia é gasta sob cargas operacionais típicas. Oconsumo de energia para sua aplicação pode ser estimado usando a fórmula

P-(N Processadores) x ( R Watts/Processadores) x ( T horas)

onde P é o consumo de energia, N é o número de processadores, R é a potência do projeto térmico e Té o tempo de execução do aplicativo.
Vejamos um exemplo ...

O processador Intel Xeon E5-4660 de 16 núcleos tem uma potência de design térmico de
120 W.
Suponha que seu aplicativo use 20 desses processadores por 24 horas para ser executado até a conclusão. O uso de energia estimado para sua aplicação é
P - (20 Processadores) x (120 W/Processadores) x (24 horas) - 57,60 kWh

Em geral, as GPUs têm um poder de design térmico maior do que as CPUs modernas, mas podem reduzir potencialmente o tempo de execução ou exigir apenas algumas GPUs para obter o mesmo resultado. A mesma fórmula pode ser usada como antes, onde N agora é visto como o número deGPUs.

Vamos para outro exemplo ...

Suponha que você tenha portado seu aplicativo para uma plataforma multi-GPU. Agora você pode executar seu aplicativo em quatro GPUs NVIDIA Tesla V100 em 24 horas! A GPU TeslaV100 da
NVIDIA tem uma potência máxima de design térmico de 300 W. O consumo de energia estimado para seu aplicativo é
P = (4 GPUs) x (300 W/GPUs) x (24 horas) = 28,80 kWh

Neste exemplo, o aplicativo acelerado por GPU é executado pela metade do custo de energia da versão somente para CPU. Observe que, neste caso, embora o tempo de solução permaneça o mesmo, o gasto de energia é reduzido pela metade!
Alcançar uma redução no custo de energia por meio de dispositivos aceleradores como
GPUs requer que o aplicativo tenha paralelismo suficiente que possa ser exposto. Isso permite o uso eficiente dos recursos do dispositivo.
* A computação paralela pode reduzir custos

O custo real monetário está se tornando uma preocupação mais visível para equipes de desenvolvedores de software, usuários de software e pesquisadores. À medida que o tamanho dos aplicativos e sistemas cresce, precisamos realizar uma análise de custo-benefício dos recursos disponíveis. Por exemplo, com a próxima grande computação de alto desempenho(HPC), os custos de energia são projetados em três vezes o custo de aquisição de hardware.
Os custos de uso também promoveram a computação em nuvem como uma alternativa, que está sendo cada vez mais adotada em universidades, startups e indústrias. Em geral, os provedores de nuvem cobram pelo tipo e quantidade de recursos usados e pelo tempo gasto com eles.Embora as
GPUs sejam geralmente mais caras do que as CPUs por unidade de tempo, alguns aplicativos podem aproveitar os aceleradores de GPU de modo que haja reduções suficientes no tempo de execução em relação à despesa da CPU.
Cuidados com o a computação paralela

A computação paralela não é uma panaceia. Muitos aplicativos não são grandes o suficiente ou exigem tempo de execução suficiente para precisar de computação paralela. Alguns podem nem ter paralelismo inerente suficiente para explorar. Além disso, a transição de aplicativos para o uso de hardware de vários núcleos e vários núcleos (GPU) requer um esforço dedicado que pode desviar temporariamente a atenção da pesquisa direta ou dos objetivos do produto. Oinvestimento de tempo e esforço deve primeiro ser considerado valioso. É sempre mais importante que o aplicativo seja executado e gere o resultado desejado antes de torná-lo rápido e dimensioná-lo para problemas maiores.
É altamente recomendável que você inicie seu projeto de computação paralela com um plano. Éimportante saber quais opções estão disponíveis para acelerar a aplicação e, em seguida, selecionar a mais adequada para o seu projeto. Depois disso, é crucial ter uma estimativa razoável do esforço envolvido e dos possíveis retornos (em termos de custo em dólares ou reais, consumo de energia,tempo de solução e outras métricas que podem ser importantes). Nas próximas seções,
começamos a fornecer a você o conhecimento e as habilidades para tomar decisões em projetos de computação paralela.
As leis fundamentais da computação paralela

Dentro da computação serial, todas as operações aceleram à medida que a frequência do clock aumenta. Em contraste, com a computação paralela, precisamos pensar um pouco e modificar nossos aplicativos para explorar totalmente o hardware paralelo. Por que a quantidade de paralelismo é importante? Para entender isso, vamos dar uma olhada nas leis de computação paralela.
O limite da computação paralela: Lei de Amdahl

Nós precisamos de uma maneira de calcular o potencial de aceleração de um cálculo com base na quantidade do código paralelo. Isso pode ser feito usando a Lei de Amdahl, proposta por GeneAmdahl em 1967. Essa lei descreve a aceleração de um problema de tamanho fixo à medida que os processadores aumentam. A equação a seguir mostra isso, onde P é a fração paralela do código, S é a fração serial, o que significa que P + S= le/Véo número de processadores:
SpeedUplN) = -1-7,

A Lei de Amdahl destaca que por mais rápido que façamos a parte paralela do código,
sempre estaremos limitados pela parte serial. A figura as seguir visualiza essa limitação. Este dimensionamento de um problema de tamanho fixo é referido como dimensionamento forte.
Figura 4 - Speedup para um problema de tamanho fixo de acordo com a Lei de Amdahl é mostrado em função do número de processadores.
As linhas mostram a aceleração ideal quando 100% de um algoritmo é paralelizado e para 90%, 75%e 50%. A Lei de Amdahl afirma que a aceleração é limitada pelas frações de código que permanecem em série.
DEFINIÇÃO Escala forte representa o tempo de solução em relação ao número de processadores para um tamanho total fixo.
Rompendo o limite da paralela: Lei de Gustafson-Barsis

Gustavoe Barsis apontou em 1988 que execuções de código paralelo deveriam aumentar o tamanho do problema à medida que mais processadores fossem adicionados. Isso pode nos dar uma maneira alternativa de calcular o potencial de aceleração do nosso aplicativo. Se o tamanho do problema cresce proporcionalmente ao número de processadores, a aceleração agora é expressa como:
Aceleração(N) = N - S* (A/ -1)

onde N é o número de processadores e S é a fração serial como antes. O resultado é que um problema maior pode ser resolvido ao mesmo tempo usando mais processadores.Isso oferece oportunidades adicionais para explorar o paralelismo. De fato, aumentar o tamanho do problema com o número de processadores faz sentido porque o usuário do aplicativo deseja se beneficiar de mais do que apenas o poder do processador adicional. O dimensionamento em tempo de execução para este cenário, mostrado na figura a seguir, é chamado de dimensionamento fraco.
Number of processors

Figura 5 - Speedup para quando o tamanho de um problema cresce com o número de processadores disponíveis de acordo com a Lei deGustafson-Borsis é mostrado em função do número de processadores.

As linhas mostram a aceleração ideal quando 100% de um algoritmo é paralelizado e para 90%, 75%e 50%.

DEFINIÇÃO Escala fraca representa o tempo de solução em relação ao número de processadores para um problema de tamanho fixo por processador.
A Figura a seguir mostra a diferença entre escala forte e fraca em uma representação visual. Oargumento de escalonamento fraco de que o tamanho da malha deve permanecer constante em cada processador faz bom uso dos recursos do processador adicional. A perspectiva de escala forte está principalmente preocupada com a aceleração do cálculo. Na prática, tanto o dimensionamento forte quanto o dimensionamento fraco são importantes porque abordam diferentes cenários de usuário.
Strong scaling Total mesh size stays constant

1000

I—II—II—II—I

- ---

1000

----

250 ----

Figura 6 - O dimensionamento forte mantém o tamanho geral de um problema e o divide em processadores adicionais. No escalonamento froco, o tamanho da malha permanece o mesmo paro cada processador e o tamanho total aumenta.
O termo escalabilidade é frequentemente usado para se referir a se mais paralelismo pode ser adicionado no hardware ou no software e se há um limite geral de quanta melhoria pode ocorrer.Embora o foco tradicional seja o dimensionamento em tempo de execução, argumentaremos que o dimensionamento de memória geralmente é mais importante.
A Figura abaixo mostra um aplicativo com escalabilidade de memória limitada.
Uma matriz replicada(R) é um conjunto de dados que é duplicado em todos os processadores. Uma matriz distribuída(D) é particionada e dividida entre os processadores. Por exemplo, em uma simulação de jogo, 100 caracteres podem ser distribuídos em 4 processadores com 25caracteres em cada processador. Mas o mapa do tabuleiro do jogo precisa ser copiado para cada processador.
Na figura, a matriz replicada é duplicada na malha. Como esse valor é relacionado ao escalonamento fraco, o tamanho do problema aumenta à medida que o número de processadores aumenta.Para 4
processadores, o array é 4 vezes maior em cada processador. À medida que o número de processadores e o tamanho do problema aumentam, logo não há memória suficiente em um processador para que o trabalho seja executado. A escala de tempo de execução limitada significa que a tarefa é executada lentamente; o dimensionamento de memória limitado significa que o trabalho não pode ser executado. Também ocorre que, se a memória do aplicativo puder ser distribuída, o tempo de execução geralmente também será dimensionado.
Memory sizes for weak scaling with replicated and distributed arrays

Array R
Array D

1 proc

Proc 0

|1OO MB|
1100 MB|

2 proc

Proc 0 Proc 1

| 200 MB |r 200 MB |

1100 MB | 100 MB|

4 proc

Proc 0 Proc 1

400 MB 400 MB

1100 MB| 1100 MB |

Proc 2 Proc 3

| 400 MB | | 400 MB |
1100 MB | 1100 MB I

Array R - Array is replicated (copied) to every processor
Array D - Array is distributed across processors

Figura 7 - Os arrays distribuídos permanecem do mesmo tamanho que o problema e o número de processadores dobra (escala fraca). Mas arrays replicados (copiados) precisam de todos os dados em cada processador, e a memória cresce rapidamente com o número de process
Mesmo que o tempo de execução seja escalonado fracamente (permanece constante), os requisitos de memória limitam a escalabilidade.
Uma visão de um trabalho computacionalmente intensivo é que cada byte de memória é tocado em cada ciclo de processamento, e o tempo de execução é uma função do tamanho da memória. Reduzir o tamanho da memória necessariamente reduzirá o tempo de execução. Ofoco inicial no paralelismo deve ser, portanto, reduzir o tamanho da memória à medida que o número de processadores cresce.
Como funciona a computação paralela?

A computação paralela requer a combinação de uma compreensão de hardware,
software e paralelismo para desenvolver um aplicativo. É mais do que apenas passar mensagens ou encadear. O
hardware e o software atuais oferecem muitas opções diferentes para levar a paralelização ao seu aplicativo. Algumas dessas opções podem ser combinadas para gerar ainda mais eficiência e agilidade.
É importante ter uma compreensão da paralelização em seu aplicativo e da maneira como os diferentes componentes de hardware permitem que você o exponha. Além disso, os desenvolvedores precisam reconhecer que, entre seu código-fonte e o hardware, seu aplicativo deve percorrer camadas adicionais, incluindo um compilador e um sistema operacional:
Figura 8 - A paralelização é expressa em uma camada de software aplicativo que é mapeada para o hardware do computador por meio do compilador e do sistema operacional.
Como desenvolvedor, você é responsável pela camada de software do aplicativo, que inclui seu código-fonte. No código-fonte, você faz escolhas sobre a linguagem de programação e as interfaces de software paralelas usadas para aproveitar o hardware subjacente. Além disso, você decide como dividir seu trabalho em unidades paralelas. Um compilador é projetado para traduzir seu código-fonte em um formato que o hardware possa executar. Com essas instruções em mãos, um sistema operacional consegue executá-las no hardware do computador.
Mostraremos a você através de um exemplo como introduzir a paralelização em um algoritmo por meio de um aplicativo. Este processo ocorre na camada de software de aplicação, mas requer uma compreensão do hardware do computador. Por enquanto, vamos nos abster de discutir a escolha do compilador e do SO. Adicionaremos incrementalmente cada camada de paralelização para que você possa ver como isso funciona. A cada estratégia paralela, explicaremos como o hardware disponível influencia as escolhas feitas. O objetivo ao fazer isso é demonstrar como os recursos de hardware influenciam as estratégias paralelas. Categorizamos as abordagens paralelas que um desenvolvedor pode adotar
* Paralelização baseada em processos

* Paralelização baseada em thread

* Vetorização

* Processamento de fluxo

Seguindo o exemplo, apresentaremos um modelo para ajudá-lo a pensar em hardware moderno. Esse modelo divide o hardware de computação moderno em componentes individuais e a variedade de dispositivos de computação. Finalmente, discutiremos com mais detalhes as camadas de aplicação e de software.
Conforme mencionado, categorizamos as abordagens paralelas que um desenvolvedor pode adotar em paralelização baseada em processo, paralelização baseada em thread,vetorização e processamento de fluxo. A paralelização baseada em processos individuais com seus próprios espaços de memória pode ter memória distribuída em diferentes nós de um computador ou dentro de um nó. O processamento de fluxo é geralmente associado a GPUs. O modelo para hardware e software de aplicativo moderno ajudará você a entender melhor como planejar a portabilidade de seu aplicativo para o hardware paralelo atual.
Percorrendo um aplicativo de exemplo

Nesta introdução à paralelização, veremos uma abordagem paralela de dados. Essa é uma das estratégias de aplicativos de computação paralela mais comuns. Vamos realizar o cálculo em uma malha espacial composta por uma grade regular bidimensional (2D) de elementos retangulares ou células. As etapas (resumidas aqui e descritas em detalhes posteriormente) para criar a malha espacial e preparar o cálculo são:
1. Discretizar (dividir) o problema em células ou elementos menores

2. Definir um kernel computacional (operação) para conduzir em cada elemento da malha

3. Adicionar as seguintes camadas de paralelização em CPUs e GPUs para realizar o cálculo:

o Vetorização — Trabalhe em mais de uma unidade de dados por vez o Tópicos—Implante mais de um caminho de computação para envolver mais núcleos de processamento o Processos — Instâncias de programa separadas para distribuir o cálculo em espaços de memória separados o Descarregando o cálculo para GPUs — Envie os dados para o processador gráfico para calcular
Começamos com um domínio de problema 2D de uma região do espaço. Para fins de ilustração,usaremos uma imagem 2D do vulcão Krakatau (figura a seguir) como nosso exemplo. O
objetivo do nosso cálculo pode ser modelar a pluma vulcânica, o tsunami resultante ou a detecção precoce de uma erupção vulcânica usando aprendizado de máquina. Para todas essas opções, a velocidade de cálculo é fundamental se quisermos que resultados em tempo real informem nossas decisões.
Figura 9 - Um exemplo de domínio espacial 2D para uma simulação numérica. As simulações numéricas geralmente envolvem operações de estêncil1 ou grandes sistemas vetoriais de matriz. Esses tipos de operações são frequentemente usados na modelagem de fluidos para gerar previsões de tempos de chegada do tsunami, previsões do tempo, propagação de fumaça e outros processos necessários para decisões informadas.
PASSO 1: DISCRETIZE O PROBLEMA EM CÉLULAS OU ELEMENTOS MENORES

Para qualquer cálculo detalhado, devemos primeiro dividir o domínio do problema em partes menores, processo que é chamado de discretização. No processamento de imagens,geralmente são apenas os pixels em uma imagem de bitmap. Para um domínio computacional, eles são chamados de células ou elementos. A coleção de células ou elementos formam uma malha computacional que cobre a região espacial para a simulação. Os valores de dados para cada célula podem ser inteiros,flutuantes ou double.

1 Em matemática, especialmente nas áreas de análise numérica concentrando-se na solução numérica de equações diferenciais parciais, um estêncil é um arranjo geométrico de um grupo nodal que se relaciona com o ponto de interesse usando uma rotina de aproximação numérica.
PASSO 2: DEFINA UM KERNEL COMPUTACIONAL, OU OPERAÇÃO, PARA CONDUZIR EM CADA
ELEMENTO DA MALHA

Os cálculos nesses ciados discretizados geralmente são alguma forma de operação de estêncil, assim chamada porque envolve um padrão de células adjacentes para calcular o novo valor para cada célula. Isso pode ser uma média (uma operação de desfoque, que desfoca a imagem ou a torna mais difusa), um gradiente (detecção de bordas, que aguça as bordas da imagem) ou outra operação mais complexa associada à resolução de sistemas físicos descritos por diferencial parcial equações (PDE).A Figura abaixo mostra uma operação de estêncil como um estêncil de cinco pontos que executa uma operação de desfoque usando uma média ponderada dos valores de estêncil.
xj,i ~ (xj,i—l + xj-l,i + xj,i + xj,i+l +

Na figura acima, um operador de estêncil de cinco pontos como um padrão cruzado na malha computacional. Os dados marcados pelo estêncil são lidos na operação e armazenados na célula central. Este padrão é repetido para cada célula. O operador de desfoque, um dos operadores de estêncil mais simples, é uma soma ponderada dos cinco pontos marcados com os pontos grandes e atualiza um valor no ponto central do estêncil. Este tipo de operação é feito para operações de suavização ou simulações numéricas de propagação de ondas.
Mas o que são essas equações diferenciais parciais? Vamos voltar ao nosso exemplo e imaginar que desta vez é uma imagem colorida composta de matrizes vermelhas, verdes e azuis separadas para fazer um modelo de cores RGB. O termo "parcial" aqui significa que há mais de uma variável e que estamos separando a mudança de vermelho com espaço e tempo daquela de verde e azul.Em seguida, realizamos o operador de desfoque separadamente em cada uma dessas cores.
Há mais um requisito: precisamos aplicar uma taxa de mudança com o tempo e o espaço.
Em outras palavras, o vermelho se espalharia em uma taxa e verde e azul em outras. Isso pode ser para produzir um efeito especial em uma imagem ou pode descrever como as cores reais sangram e se fundem em uma imagem fotográfica durante o desenvolvimento. No mundo científico, em vez de vermelho,verde e azul, podemos ter massa e velocidade x e y.

PASSO 3: VETORIZAÇÃO PARA TRABALHAR EM MAIS DE UMA UNIDADE DE DADOS POR VEZ

Comece a introduzir a paralelização observando a vetorização. O que é vetorização? Alguns processadores têm a capacidade de operar em mais de um dado por vez; uma capacidade referida como operações vetoriais. Os blocos sombreados na figura abaixo ilustram como vários valores de dados são operados simultaneamente em uma unidade vetorial em um processador com uma instrução em um ciclo de clock.
Vector unit

Figura 11 - Uma operação vetorial especial é realizada em quatro unidades. Esta operação pode ser executada em um único ciclo de clock com pouco custo de energia adicional à operação serial.
ETAPA 4: THREADS PARA IMPLANTAR MAIS DE UM CAMINHO DE COMPUTAÇÃO PARA ENVOLVER
MAIS NÚCLEOS DE PROCESSAMENTO

Sabemos que a maioria das CPUs hoje tem pelo menos quatro núcleos de processamento,
usamos threading para operar os núcleos simultaneamente em quatro linhas por vez. A Figura abaixo mostra o processamento seguindo essa divisão.
Vector unit

Figura 12 - Quatro threads processam quatro linhas de unidades vetoriais simultaneamente.

ETAPA 5: PROCESSOS PARA DISTRIBUIR O CÁLCULO PARA SEPARAR OS ESPAÇOS DE MEMÓRIA

Nós podemos dividir ainda mais o trabalho entre processadores em dois desktops, geralmente chamados de nós em processamento paralelo. Quando o trabalho é dividido entre nós, os espaços de memória para cada nó são distintos e separados. Isto é indicado colocando um espaço entre as linhas como na figura abaixo.
Vector unit

Na figura acima observamos que este algoritmo pode ser paralelizado ainda mais distribuindo os blocos 4x4 entre processos distintos. Cada processo usa quatro threads, cada um manipulando uma unidade vetorial de quatro nós em um único ciclo de clock. O espaço em branco adicional na figura ilustra os limites do processo.
Mesmo para este cenário de hardware bastante modesto, há uma aceleração potencial de
32x. Isso é mostrado pelo seguinte:
2 desktops (nós) x 4 núcleos x (unidade de vetor de 256 bits de largura)/(duplo de
64 bits) =
aceleração potencial de 32x

Se olharmos para um cluster high-end com 16 nós, 36 núcleos por nó e um processador vetorial de
512 bits, o potencial de aceleração teórica é 4.608 vezes mais rápido que um processamento em serial:
16 nós x 36 núcleos x (unidade vetorial de 512 bits de largura)/(duplo de 64 bits)
= aceleração potencial de 4.608x
ETAPA 6: DESCARREGAR O CÁLCULO PARA GPUS

A GPU é outro recurso de hardware para paralelização. Com GPUs, podemos aproveitar muitos multiprocessadores de streaming para trabalho. Por exemplo, a figura a seguir mostra como o trabalho pode ser dividido separadamente em blocos de 8x8. Usando as especificações de hardware para a GPU NVIDIA Volta, esses blocos podem ser operados por 32 núcleos de precisão dupla espalhados por 84 multiprocessadores de streaming, dando-nos um total de 2.688núcleos de precisão dupla que funcionam simultaneamente. Se tivermos uma GPU por nó em um cluster de 16
nós, cada um com um multiprocessador de streaming de precisão dupla de 2.688, essa é uma paralelização de 43.008 vias de 16 GPUs.
nn - -- riBn ui i - -- i ii ii i ui i ------
- -- nnn ii - --
n«n

--------

- -- n s
' >

84 streaming multiprocessors

Figuro 13 - Em umo GPU, o comprimento do vetor é muito moior do que em uma CPU. Aqui, blocos 8x8
são distribuídos entre os grupos de trobolho do GPU.
Esses são números impressionantes, mas, neste momento, devemos moderar as expectativas reconhecendo que a aceleração real está muito aquém desse potencial total. Nosso desafio da vida real é organizar camadas tão extremas e díspares de paralelização para obter o máximo de aceleração possível, (mas isso foge do escopo de concursos públicos.
Para este passo a passo do aplicativo de alto nível, deixamos de fora muitos detalhes. Mas mesmo esse nível nominal de detalhes destaca algumas das estratégias para expor a paralelização de um algoritmo. Para poder desenvolver estratégias semelhantes para outros problemas, é necessário um entendimento de hardware e software modernos.
PRoCESSAMENTo EM LoTE (BATCH) E EM TEMPo REAL

Existem algumas diferenças significativas entre o processamento em lote e em tempo real. Vamos começar apresentando uma tabela que resume as:
Processamento em lote Processamento em tempo real
Os dados estão em repouso
O tamanho do lote é limitado
Os dados estão em movimento

Os dados estão essencialmente chegando como um fluxo e são ilimitados
Acesso a dados inteiros Acesso aos dados na transação atual/janela deslizante
Dados processados em lotes
O processamento é feito em evento, janela ou, no máximo,em nível de microlote

Administração eficiente e fácil
Insights em tempo real, mas os sistemas são frágeis em comparação com lotes
FERRAMENTAS DE PRoCESSAMENTo E STREAMINC DE DADoS EM TEMPo

REAL

O streaming de dados em tempo real é o processo de análise de uma grande quantidade de dados ao produzi-los. Você pode processar todas as informações valiosas para o seu negócio usando uma ferramenta de processamento em tempo real. Por exemplo, ferramentas de streaming de dados como Flume e Kafka permitem conexões diretas com Hive, Spark e HBase.
As ferramentas de processamento de dados em tempo real ajudam os dados a serem integrados ao sistema e a processar tudo sem escrever. Assim, a funcionalidade robusta é usada aqui,que é a ideologia da arquitetura de data lake.
Aqui estão algumas das principais ferramentas de streaming de dados em tempo real::

#1. FLUME

O Flume é conhecido por ter conectividade bem estabelecida, é compatível com o Hadoop e requer um alvo predefinido chamado sink. O Flume é uma das ferramentas mais amplamente suportadas entre todas as distribuições comerciais do Hadoop. Além de ser uma característica atraente e essencial, Kafka e Flume se complementam muito bem.
O Flume não tem muitas desvantagens, exceto uma, que é bastante assustadora. Se a ferramenta de streaming de dados Flume falhar, os dados serão apagados completamente e,consequentemente, você não poderá recuperar ou replicar nenhum evento passado.

#2. KAFKA

Kafka está disponível em todos os lugares e altamente redundante. Também é bastante escalável e possui recursos como mensagens um para muitos.
Kafka possui recursos como tolerância a falhas e redundância de dados. Por exemplo,
sempre que um agente Kafka ficar inativo, algum outro agente Kafka retransmitirá o tópico. Em suma, você não experimentará a mesma conectividade comercial que o Flume.
Kafka e Flume são talvez a melhor aposta para você. Você poderá vincular ambos em um sistema de produção em larga escala. Mas para os sistemas de pequena escala, é melhor se você escolher o sistema que atende às suas necessidades gerais. Embora o Kafka seja redundante, é um pouco mais difícil de operar, pois é uma tecnologia relativamente nova. Além disso,Kafka carece do departamento de suporte comercial. Ele também não possui os conectores embutidos que são importantes.
#3. APACHE NIFI

Apache NIFI é outra boa ferramenta para processamento de dados em tempo real. O
Apache NIFI
possui recursos de logística de dados integrados. Ele cria uma plataforma para automatizar a movimentação de dados entre diferentes destinos.
O NIFI suporta fontes distributivas, como arquivos, feeds sociais, arquivos de log e vídeos. NIFI é capaz de mover dados de qualquer fonte para qualquer destino. Ele também rastreia os dados em tempo real.
#4. APACHE STORM

Construído pelo Twitter, o Apache Storm é uma ferramenta obrigatória para processamento de dados em tempo real. Ao contrário do Hadoop que realiza o processamento em lote, oApache Storm foi desenvolvido especificamente para fluxos de dados em fluxo.Tem outros usos também. Aprendizado de máquina online e ETL, entre outras coisas para as quais oApache Storm pode ser usado.
O Apache Storm pode processar dados ridiculamente rápido. O Apache Storm se diferencia na execução de processos no nó ao qual está atribuído. Além disso, pode ser integrado aoHadoop para ampliar ainda mais suas habilidades.
#5. AMAZON KINESIS

Com o Amazon Kinesis, as empresas podem criar aplicativos de streaming em tempo real usando bibliotecas Java e editor SQL. O Kinesis cuida do trabalho pesado de executar os aplicativos e dimensionar para atender aos requisitos quando necessário. Por causa do kinesis, você poderá se livrar do incômodo de gerenciar servidores e outras complexidades relacionadas à criação e gerenciamento de aplicativos para processamento em tempo real.
A flexibilidade fornecida pelo Kinesis ajuda as empresas a começar com relatórios básicos e insights dos dados desejados. Mas, à medida que as demandas aumentam, ele também pode ser usado para aprender algoritmos para análises aprofundadas.
THIAGO CAVALCANTI

PROFESSOR

