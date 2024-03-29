# Desenvolvimento de Informação - Visão computacional. Deep learning

Índice

Visão computacional

Reconhecimento facial

Classificação de imagens.

Detecção de objetos.

Aprendizado profundo

Redes Neurais Clássicas.

Redes neurais convolucionais.

Redes neurais recorrentes.

Redes de Hopfield

Long short-term memory (LSTM)

Redes Perceptron multicamadas recorrentes.

Máquinas de Boltzmann

Deep belief networks.

VISÃo CoMPUTACIoNAL.

A visão computacional ajuda os computadores a compreender o conteúdo de imagens digitais, como fotografias. Começando com um artigo seminal em 2012, as abordagens de aprendizado profundo para a visão computacional se tornaram extremamente bem-sucedidas.

Imagine que você está sentado em um jardim, observando o que está acontecendo ao seu redor.Existem dois sistemas em seu corpo que estão funcionando: seus olhos estão agindo como sensores e criando representações da cena, enquanto seu sistema cognitivo está dando sentido ao que seus olhos estão vendo. Assim, você pode ver um pássaro, uma minhoca e algum movimento e perceber que o pássaro pousou sobre a terra e está comendo a minhoca.
A bird came down the walk:
He did not know I saw;

He bit an angle-worm in halves
And ate the fellow raw.

Figura 1 - Sistemas sensorial e cognitivo em seres humanos.

A visão computacional tenta imitar as capacidades da visão humana fornecendo métodos para formação de imagem (imitando o sistema sensorial humano) e percepção da máquina(imitando o sistema cognitivo humano). A imitação do sistema sensorial humano está focada no hardware, no design e no posicionamento de sensores, como câmeras. A abordagem moderna para imitar o sistema cognitivo humano consiste em métodos de aprendizado de máquina (ML) que são usados para extrair informações de imagens.
Quando vemos a fotografia de uma flor (margarida), por exemplo, nosso sistema cognitivo humano é capaz de reconhecê-la como uma margarida. Os modelos de aprendizado de máquina para classificação de imagens imitam essa capacidade humana começando com fotografias de outras margaridas usadas para reconhecer o padrão estético da flor.
Figura 2 - Um modelo de aprendizado de máquina de classificação de imagens imito o sistema cognitivo humano.
Se você estivesse lendo um texto sobre visão computacional no início da década de
2010, os métodos usados para extrair informações de fotos não envolveriam aprendizado de máquina.Em vez disso, você estaria aprendendo sobre denoising1, localização de bordas, detecção de textura e operações morfológicas (baseadas na forma). Com os avanços na inteligência artificial (mais especificamente, os avanços no aprendizado de máquina), isso mudou.
A inteligência artificial (IA) explora métodos pelos quais os computadores podem imitar as capacidades humanas. O aprendizado de máquina é um subcampo de IA que ensina os computadores a fazer algo, mostrando a eles uma grande quantidade de dados e instruindo-os a aprender com eles. Os sistemas especialistas são outro subcampo da IA - os sistemas especialistas ensinam os computadores a imitar as capacidades humanas, programando-os para seguir a lógica humana.
Antes da década de 2010, as tarefas de visão computacional, como classificação de imagens, eram comumente feitas por meio da construção de filtros de imagem personalizados para implementar a lógica estabelecida por especialistas. Hoje em dia, a classificação de imagens é obtida por meio de redes convolucionais, uma forma de aprendizado profundo. Podemos organizar esses termos de acordo com técnicas e problemas, veja a figura abaixo:
1 Denoising é qualquer método de processamento de sinal que reconstrói um sinal de um sinal ruidoso.Seu objetivo é remover o ruído e preservar informações úteis.

Artificial intelligence

Figura 3 - A visão computacional é um subcompo da IA que tenta imitar o sistema visual humano;
embora antes dependesse de uma abordagem de sistemas especialistas, hoje isso é feito com aprendizado de máquina.
Veja, por exemplo, a imagem da margarida. Uma abordagem de aprendizado de máquina ensina um computador a reconhecer o tipo de flor em uma imagem, mostrando ao computador muitas imagens junto com seus rótulos (ou respostas corretas). Então, mostramos ao computador muitas imagens de margaridas, muitas imagens de tulipas e assim por diante. Com base nesse conjunto de dados de treinamento rotulado, o computador aprende como classificar uma imagem que não encontrou antes.
Em uma abordagem de sistema especialista, por outro lado, começaríamos entrevistando um botânico humano sobre como eles classificam as flores. Se o botânico explicou que bellis perennis(o nome científico de uma margarida) consiste em pétalas alongadas brancas ao redor de um centro amarelo e folhas verdes arredondadas, nós tentaríamos criar filtros de processamento de imagem para atender a esses critérios. Por exemplo, procuraríamos a prevalência de branco,amarelo e verde na imagem.

Em seguida, criaríamos filtros de borda para identificar as bordas das folhas e filtros morfológicos correspondentes para ver se eles correspondem à forma arredondada esperada. Podemos suavizar a imagem no espaço HSV (matiz, saturação, valor) para determinar a cor do centro da flor em comparação com a cor das pétalas. Com base nesses critérios, podemos chegar a uma pontuação para uma imagem que classifique a probabilidade de que seja uma margarida. Da mesma forma, projetaríamos e aplicaríamos diferentes conjuntos de regras para rosas, tulipas,girassóis e assim pordiante. Para classificar uma nova imagem.

Esta descrição ilustra o considerável trabalho sob medida que foi necessário para criar modelos de classificação de imagens. É por isso que a classificação de imagens costumava ter aplicabilidade limitada.
Tudo mudou em 2012 com a publicação do artigo AlexNet. Os autores - Alex
Krizhevsky, llya
Sutskever e Geoffrey E. Hinton - foram capazes de superar significativamente qualquer método de classificação de imagem existente aplicando redes convolucionais ao conjunto de dados de referência usado no ImageNet Large-Scale Visual Recognition Challenge(ILSVRC). Eles alcançaram um erro de 15,3%, enquanto a taxa de erro do segundo colocado foi de mais de 26%.As melhorias típicas em competições como esta são da ordem de 0,1%, então a melhoria que oAlexNet demonstrou foi cem vezes o que a maioria das pessoas esperava! Este foi um desempenho que chamou a atenção.
Então, o que há de novo no AlexNet? Quatro coisas:

Unidades de processamento gráfico (GPUs) - Redes neurais convolucionais são uma ótima ideia,mas são computacionalmente muito caras. Os autores do AlexNet implementaram uma rede convolucional em cima das bibliotecas de renderização de gráficos fornecidas por chips para fins especiais chamados GPUs. Na época, as GPUs eram usadas principalmente para visualização e jogos de última geração. O artigo agrupou as convoluções para ajustar o modelo em duas GPUs.As GPUs viabilizaram o treinamento das redes convolucionais.

Ativação da unidade linear retificada (ReLU) - Os criadores do AlexNet usaram uma função de ativação não saturante chamada ReLU em sua rede neural. Por enquanto, é suficiente saber que usar uma função de ativação não saturante linear por partes permitiu que seu modelo convergisse muito mais rápido.
Regularização - O problema com ReLUs - e a razão pela qual eles não foram muito usados até2012 - era que, como eles não saturavam, os pesos da rede neural se tornavam numericamente instáveis. Os autores do AlexNet usaram uma técnica de regularização para evitar que os pesos se tornassem muito grandes.
Profundidade - Com a capacidade de treinar mais rápido, eles foram capazes de treinar um modelo mais complexo que tinha mais camadas de rede neural. Dizemos que um modelo com mais camadas é mais profundo.
Os métodos de visão computacional fornecem soluções para uma variedade de problemas do mundo real. Além de OCR, métodos de visão computacional foram aplicados com sucesso ao diagnóstico médico (usando imagens como raios-X e ressonâncias magnéticas),automatizando operações de varejo (como leitura de códigos QR, reconhecimento de prateleiras vazias,verificação da qualidade de vegetais, etc.), vigilância (monitoramento de safra por satélite imagens, monitoramento por câmeras da vida selvagem, detecção de intrusos, etc.),reconhecimento de impressão digital e segurança automotiva (seguindo carros a uma distância segura, identificando mudanças nos limites de velocidade de sinais de trânsito,carros com estacionamento automático, carros autônomos, etc.).
A visão computacional encontrou uso em muitas indústrias. No governo, tem sido usado para monitorar imagens de satélite, na construção de cidades inteligentes e em fiscalizações alfandegárias e de segurança. Na área da saúde, tem sido usado para identificar doenças oculares e encontrar sinais precoces de câncer em mamografias. Na agricultura, tem sido usado para detectar bombas de irrigação que não funcionam bem, avaliar a produtividade das safras e identificar doenças foliares. Na manufatura, ele encontra uso no chão de fábrica para controle de qualidade e inspeção visual. Em seguros, tem sido usado para avaliar automaticamente os danos aos veículos após um acidente.
RECoNHECIMENTo FACIAL.

ROrbitalUpper (optional)
OrbitalUpper(opt)onal)

REyelidUpper

REyelidLower

R Orbital Lower

RNostnlBulge LNostritBulge

RNostrilBase LNostnIBase

RPuffer

RLipUpperBend LlpUpper

LLipUpperBend

RMouthCorner LMouthCorner

RLipLowerBend j LLipLowerBend

RJawEnd

*

LJawEnd

Reconhecimento facial é uma forma de identificar ou confirmar a identidade de uma pessoa usando seu rosto. Os sistemas de reconhecimento facial podem ser usados para identificar pessoas em fotos, vídeos ou em tempo real.
Muitas pessoas estão familiarizadas com a tecnologia de reconhecimento graças ao Face
ID, que é usado para desbloquear o iPhone (no entanto, esse é apenas um aplicativo de reconhecimento facial). Normalmente, o reconhecimento facial não conta com um banco de dados vasto de fotos para determinar a identidade de uma pessoa; ele simplesmente a identifica e reconhece como sendo a proprietária única do dispositivo, limitando o acesso de outros.
Além de desbloquear telefones, o reconhecimento facial funciona fazendo a correspondência entre os rostos de pessoas que passam por câmeras especiais com imagens de pessoas em uma lista de observação. As listas de observação podem conter imagens de qualquer pessoa,incluindo pessoas que não são suspeitas de irregularidades; e as imagens podem originar-se de qualquer lugar, até mesmo de nossas contas de redes sociais. Os sistemas de tecnologia facial podem variar, mas no geral, tendem a funcionar da seguinte forma:
Etapa i: Detecção do rosto

A câmera detecta e localiza a imagem de um rosto, sozinho ou no meio de uma multidão. Aimagem da pessoa pode ser de frente ou de perfil.

Etapa 2: Análise do rosto

Depois, uma imagem do rosto é capturada e analisada. A maioria das tecnologias de reconhecimento facial conta com imagens 2D em vez de 3D, porque é mais conveniente fazer a correspondência de imagens 2D com fotos públicas ou de um banco de dados. O software faz a leitura da geometria do seu rosto. Os principais fatores são a distância entre seus olhos, a profundidade de suas órbitas oculares, a distância entre a testa e o queixo, o formato da maçã do rosto e o contorno dos lábios, das orelhas e do queixo. O objetivo é identificar os pontos de referência faciais principais que distinguem seu rosto.
Etapa 3: Conversão da imagem em dados

O processo de captura facial transforma as informações analógicas (um rosto) em um conjunto de informações digitais (dados) com base nas características faciais da pessoa. A análise do seu rosto é basicamente transformada em uma fórmula matemática. O código numérico é chamado de impressão facial. Da mesma forma que as impressões digitais são únicas, cada pessoa possui sua própria impressão facial.
Etapa 4: Localização de uma correspondência

Sua impressão facial é comparada com um banco de dados de outros rostos conhecidos. Por exemplo, o FBI tem acesso até 650 milhões de fotos, extraídas de vários bancos de dados estaduais. No Facebook, qualquer foto marcada com o nome de uma pessoa torna-se parte do banco de dados do Facebook, que também pode usada para reconhecimento facial. Se a sua impressão facial corresponder a uma imagem de um banco de dados de reconhecimento facial,uma determinação será feita.

De todas as medições biométricas, o reconhecimento facial é considerado o mais natural.Intuitivamente, isso faz sentido, já que normalmente reconhecemos uns aos outros pelos nossos rostos, e não por impressões digitais e íris. Estima-se que mais da metade da população mundial passa por reconhecimento facial regularmente.
CLASSIFICAçÃo DE IMAGENS.

A classificação de imagens é um problema de aprendizado supervisionado descrito da seguinte forma: defina um conjunto de classes de destino (objetos a serem identificados em imagens) e treine um modelo para reconhecê-los usando fotos de exemplo já rotuladas. Os primeiros modelos de visão computacional se baseavam em dados de pixel brutos como entrada para o modelo. No entanto, como mostrado na figura abaixo, os dados de pixel brutos por si só não fornecem uma representação suficientemente estável para abrangera miríade de variações de um objeto conforme capturado em uma imagem. A posição do objeto, o plano de fundo atrás do objeto, a iluminação ambiente, o ângulo da câmera e o foco da câmera, todos podem produzir flutuação nos dados de pixel brutos; essas diferenças são significativas o suficiente para que não possam sercorrigidas pela média ponderada dos valores RGB de pixel.
Na figura acima temos à esquerda os gatos podem ser capturados em uma foto em uma variedade de poses, com diferentes cenários e condições de iluminação. Já a direita temos a média dos dados de pixel para contabilizar esta variedade não produz nenhuma informação significativa.
Para modelar objetos com mais flexibilidade, os modelos clássicos de visão computacional adicionaram novos recursos derivados de dados de pixel, como histogramas de cores,texturas e formas. A desvantagem dessa abordagem é que a engenharia sobre os recursos se tornou um fardo real, pois havia muitas entradas para ajustar. Para um classificador de gatos,quais cores foram mais relevantes? Quão flexíveis devem ser as definições de forma? Como os recursos precisavam ser ajustados com tanta precisão, construir modelos robustos foi bastante desafiador,e a precisão foi prejudicada.

Um avanço na construção de modelos para classificação de imagens veio com a descoberta de que uma rede neural convolucional(CNN) poderia ser usada para extrair progressivamente representações de nível distintos e sobrepostos do conteúdo da imagem. Em vez de pré-processar os dados para derivar recursos como texturas e formas, uma CNN pega apenas os dados de pixel brutos da imagem como entrada e "aprende" como extrair esses recursos e, por fim,inferir que objeto eles constituem.
Conv. Module #1 Conv. Module #2 Classification

Input

No final de uma rede neural convolucional (RNC) há uma ou mais camadas totalmente conectadas(quando duas camadas estão "totalmente conectadas", todos os nós da primeira camada são conectados a todos os nós da segunda camada). Seu trabalho é realizar a classificação com base nas características extraídas pelas convoluções. Normalmente, a camada final totalmente conectada contém uma função de ativação softmax, que produz um valor de probabilidade de o a i para cada um dos rótulos de classificação que o modelo está tentando prever.Falaremos mais sobre RNC na próxima seção.
DETECçÃo DE oBJEToS.

A classificação de imagens envolve a atribuição de um rótulo de classe a uma imagem,
enquanto a localização de objetos envolve o desenho de uma caixa delimitadora em torno de um ou mais objetos em uma imagem. A detecção de objetos é uma tarefa mais desafiadora e combina essas duas tarefas e desenha uma caixa delimitadora ao redor de cada objeto de interesse na imagem e atribui a eles um rótulo de classe. Juntos, todos esses problemas são chamados de reconhecimento de objetos.
Mas, como podemos distinguir entre essas três tarefas de visão computacional? Vejamos

Classificação da imagem: prever o tipo ou classe de um objeto em uma imagem.

Entrada: uma imagem com um único objeto, como uma fotografia.
Saída: um rótulo de classe.

Localização de objetos: localizar a presença de objetos em uma imagem e indique sua localização com uma caixa delimitadora.
Entrada: uma imagem com um ou mais objetos, como uma fotografia.

Saída: uma ou mais caixas delimitadoras (por exemplo, definido por um ponto, largura e altura).
Detecção de objetos: localizar a presença de objetos com uma caixa delimitadora e os tipos ou classes dos objetos localizados em uma imagem.
Entrada: uma imagem com um ou mais objetos, como uma fotografia.

Saída: Uma ou mais caixas delimitadoras (por exemplo, definido por um ponto, largura e altura) e um rótulo de classe para cada caixa delimitadora.
Uma extensão adicional a esta divisão das tarefas de visão computacional é a segmentação de objeto, também chamada de "segmentação de instância de objeto" ou "segmentação semântica",onde instâncias de objetos reconhecidos são indicados destacando os pixels específicos do objeto em vez de uma caixa delimitadora grosseira.
A partir dessa análise, podemos ver que o reconhecimento de objetos se refere a um conjunto de tarefas desafiadoras de visão computacional.
no

Figura 4 - Visão geral das tarefas de visão computacional para reconhecimento de objetos

APRENDIZADo PRoFUNDo.

Aprendizado profundo (DL - Deep Learning) é um campo em rápida evolução, que demonstrou resultados surpreendentes na execução de tarefas que tradicionalmente eram bem realizadas apenas por humanos. Exemplos de tais tarefas são classificação de imagens,geração de descrições de imagens em linguagem natural, tradução de linguagem natural, conversão de fala em texto e conversão de texto em fala.
Não temos de uma definição perfeita do que é DL, mas uma tentativa de estabelecer uma conceituação ao termos seria que:
DL é uma classe de algoritmos de aprendizado de máquina que usa várias camadas de unidades computacionais onde cada camada aprende sua própria representação dos dados de entrada. Essas representações são combinadas por camadas posteriores de forma hierárquica.Essa definição é um tanto abstrata, especialmente porque ainda não descrevemos o conceito de camadas e unidades computacionais, mas aos poucos vamos apresentar os conceitos,fornecendo muitos exemplos mais concretos do que isso significa.
Neste início da seção acho importante você entender que existe uma relação entre os termos inteligência artificial, aprendizado de máquina, aprendizagem profunda e redes neurais profundas. A figura abaixo demonstra que um redes neurais profundas é um subconjunto das soluções de DL. Vejamos:
Resumindo: Rede neural profunda (DNN) é um subconjunto de DL. DL é um subconjunto do aprendizado de máquina (ML), que é um subconjunto da inteligência artificial (IA).
Neste ponto, é suficiente pensar em uma rede como um sistema opaco que tem entradas e saídas.Seu modelo de uso consiste em apresentar algo, por exemplo, uma imagem ou uma sequência de texto, como entradas para a rede, e a rede produzirá algo útil em suas saídas, como uma interpretação do que a imagem contém ou uma tradução de um texto em um determinado idioma. Veja as figuras a seguir:
Opaque system
Figura 5 - Uma rede neural profunda como um sistema opaco que pode pegar uma imagem como entrada e,
em seguida, produzir uma indicação de que tipo de objeto está na imagem
2 Os tamanhos das diferentes formas ovais não representam o tamanho relativo de um campo em comparação com outro.
I am a student

Deep
Neural
Network

Je suis étudiant

Figura 6 - Um tradutor de rede neural que recebe uma frase em inglês como entrada e produz a frase correspondente em francês como saída
Uma peça central de uma rede neural é o neurônio artificial. O primeiro modelo de neurônio artificial foi introduzido em 1943 por McCulloch e Pitts, que deu início à primeira onda de pesquisas sobre redes neurais. O neurônio McCulloch e Pitts foi seguido em 1957 pelo perceptron de Rosenblatt. Uma contribuição importante do perceptron foi seu algoritmo de aprendizado automatizado associado, que demonstrou como um sistema pode aprender o comportamento desejado.
O perceptron tem algumas limitações fundamentais e, embora tenha sido demonstrado que essas limitações podem ser superadas pela combinação de vários perceptrons em uma rede multicamadas, o algoritmo de aprendizagem original não se estendeu a redes multicamadas.
A segunda onda de pesquisas sobre redes neurais foi iniciada na década de 1980. Foi fortemente influenciado por um artigo que descreveu o algoritmo de retropropagação para treinamento automático de redes multicamadas de Rumelhart em 1986. Rumelhart e seus colegas mostraram que este algoritmo pode ser usado para superar as limitações do perceptron.
Um resultado importante dessa segunda onda de pesquisa de redes neurais foi o desenvolvimento do LeNet em 1989. Está era uma rede neural convolucional (CNN), que demonstrou ser capaz de reconhecer códigos postais escritos à mão. Foi construída com base noNeocognitron de
Fukushima, que acreditamos ser a primeira CNN publicada. Uma versão aprimorada do LeNet foi posteriormente usada pelos principais bancos dos Estados Unidos para ler cheques manuscritos e,portanto, tornou-se uma das primeiras grandes aplicações comerciais de redes neurais.

A terceira onda de pesquisa de rede neural foi habilitada por uma combinação de progresso algorítmico, disponibilidade de conjuntos de dados massivos e a capacidade de usar unidades de processamento gráfico (GPU) para computação de propósito geral. De uma perspectiva externa,tudo isso veio junto em 2012. Naquela época, o campo havia sido rebatizado como DL e popularizado em grande parte devido ao AlexNet, que era uma CNNque pontuava significativamente mais alto do que qualquer outro participante de uma competição de visão computacional conhecida como desafio ImageNet. Este trabalho foi logo seguido por descobertas semelhantes em outros campos, que levaram ao boom de DL que ainda está em andamento.
REDES NEURAIS CLÁSSICAS

Chamamos de neurônio um modelo matemático que calcula uma soma ponderada de sinais,aplica uma função nessa soma e passa esse sinal transformado adiante. Como exemplo de neurônios, temos o modelo de regressão linear e o modelo de regressão logística. No primeiro, a função que aplicamos na soma ponderada é a identidade, ou seja, não aplicamos função nenhuma; simplesmente passamos a soma ponderada adiante. No caso de regressão logística,
aplicamos à soma ponderada uma função sigmoide (ou logística), que transforma o sinal de forma que possamos interpretá-lo como uma probabilidade. Esses dois exemplos de neurônios são modelos lineares e estão limitados a aprender relações igualmente lineares. Quando conectamos vários neurônios temos uma rede neural. Se utilizarmos uma função não linear nos neurônios da rede neural - como a ReLU, a função sigmoide ou a tangente hiperbólica -, ela terá o poder para aprender relações não lineares arbitrárias. Podemos visualizar uma rede neural como um grafo de neurônios conectados, como na imagem abaixo.
Esse tipo de rede neural é chamado defeedforward densa ou totalmente conectada, pois todos os neurônios de uma camada são conectados com todos os inputs da camada - por isso densa.Além disso, e os dados fluem em uma única direção, isto é, eles não voltam para camadas mais atrás nem dão voltas na mesma camada, - por \ssofeedforward.
REDES NEURAIS CoNVoLUCIoNAIS.

Embora o supercomputador Deep Blue da IBM tenha vencido o campeão mundial de xadrez
Garry
Kasparov em 1996, até recentemente os computadores eram incapazes de realizar tarefas aparentemente triviais, como detectar um cachorro em uma imagem ou reconhecer palavras faladas. Por que essas tarefas são tão fáceis para nós, humanos? A resposta está no fato de que a percepção ocorre em grande parte fora do reino de nossa consciência, dentro de módulos visuais,auditivos e sensoriais especializados em nosso cérebro. No momento em que a informação sensorial chega à nossa consciência, ela já está adornada com características de alto nível; por exemplo, quando você olha a foto de um filhote de cachorro fofo, você não pode escolher não ver o filhote ou não perceber sua fofura. Nem você pode explicar como reconhece um cachorrinho fofo; é simplesmente óbvio para você. Assim, não podemos confiar em nossa experiência subjetiva: a percepção não é nada trivial e, para compreendê-la, devemos observar como funcionam os módulos sensoriais.
Redes neurais convolucionais (CNNs) surgiram do estudo do córtex visual do cérebro e têm sido usados no reconhecimento de imagens desde a década de 1980. Nos últimos anos, graças ao aumento do poder computacional, à quantidade de dados de treinamento disponíveis e a alguns truques feitos para treinar redes profundas, as CNNs conseguiram atingir um desempenho sobre­humano em algumas tarefas visuais complexas. Eles potencializam os serviços de pesquisa de imagens, carros autônomos, sistemas automáticos de classificação de vídeo e muito mais.Além disso, as CNNs não se restringem à percepção visual: também têm sucesso em outras tarefas,como reconhecimento de voz ou processamento de linguagem natural (PNL).

O bloco mais importante na construção de uma CNN é a camada convolucional:
neurônios na primeira camada convolucional não estão conectados a cada pixel na imagem de entrada,mas apenas aos pixels em seus campos receptivos (veja na figura abaixo). Por sua vez,cada neurônio na segunda camada convolucional está conectado apenas a neurônios localizados dentro de um pequeno retângulo na primeira camada. Essa arquitetura permite que a rede se concentre em recursos de nível inferior na primeira camada oculta, depois os monte em recursos de nível superior na próxima camada oculta e assim por diante. Essa estrutura hierárquica é comum em imagens do mundo real, o que é um dos motivos pelos quais as CNNs funcionam tão bem para reconhecimento de imagens.
Convolutional layer 2
Convolutional layer 1
Input layer

Figura 7- Camadas CNN com campos receptores locais retangulares

Blocos principais de uma rede neural convolucional

Em vez de apresentar o conceito matemático de convolução, nos concentraremos em obter uma compreensão intuitiva da camada convolucional. Talvez a característica mais importante de uma rede convolucional seja uma propriedade conhecida como invariância de translação3. No caso da classificação de objetos em uma imagem, isso significa que mesmo que um objeto seja deslocado(transladado) horizontalmente ou verticalmente para uma posição diferente na imagem, a rede ainda será capaz de reconhecê-lo. Isso é verdade, independentemente de onde o objeto foi localizado na imagem nos dados de treinamento. Ou seja, mesmo que a rede tenha sido treinada principalmente com fotos de gatos no meio da imagem, uma rede convolucional ainda será capaz de classificar a imagem como contendo um gato quando apresentada a uma imagem com um gato em um dos cantos da figura. A invariância de translação é obtida empregando-se o
3 Neste contexto, translação se refere à transformação geométrica de mover todos os pontos por uma distância fixa na mesma direção em um sistema de coordenadas.
compartilhamento de peso entre os neurônios, além de torná-los escassamente conectados.Esses conceitos são descritos a seguir.

A translação é uma transformação geométrica conhecida como transformação afim. Ela muda a localização de um objeto sem alterar sua forma. Na figura abaixo, o retângulo azul representa uma versão transladada do retângulo vermelho. Outra transformação afim comum é a rotação,que muda a orientação de um objeto. O retângulo verde representa uma versão girada do retângulo vermelho.
Rotation

/ /

' / / Translation

Uma propriedade chave das camadas convolucionais é a invariância da translação, causada pelo compartilhamento de peso e uma topologia de rede escassamente conectada.
Começamos apresentando a topologia geral de uma camada convolucional usada para processamento de imagem. As camadas totalmente conectadas que estudamos em outras redes neurais são organizadas em uma única dimensão, como uma matriz de neurônios.Conforme ilustra a figura a seguir, uma camada convolucional para processamento de imagem tem uma topologia diferente, onde os neurônios são organizados em três dimensões.
4 ►

Width

Figura 8 - Topologia de uma camada convolucional 2D. Deforma um tanto não intuitiva, uma camada convolucional 2D é organizada em três dimensões: largura, altura e canais.
Duas das dimensões (largura e altura) correspondem à natureza 2D de uma imagem. Além disso,os neurônios são agrupados em canais ou mapas de recursos em uma terceira dimensão.
Assim como em uma camada normal totalmente conectada, não há conexões entre os neurônios em uma camada convolucional. Ou seja, todos os neurônios na estrutura 3D são desacoplados uns dos outros e são considerados juntos para formar uma única camada. No entanto, todos os neurônios em um único canal têm pesos idênticos (divisão de peso). Ou seja, todos os neurônios com a mesma cor na figura são cópias idênticas uns dos outros, mas receberão valores de entrada diferentes.
Agora, consideremos o comportamento de cada neurônio individual. Cada neurônio em uma camada convolucional implementa uma operação conhecida como núcleo convolucional.Os pesos são organizados em um padrão 2D e formam uma matriz convolucional.
Embora trabalhemos com imagens maiores, cada neurônio receberá valores de pixel apenas de um subconjunto da imagem (por exemplo, uma região 3x3 como para o identificador de padrão).A região de pixels da qual um neurônio recebe entradas também é conhecida como seu campo receptivo. Um problema com o qual ainda não tratamos é como lidar com imagens com vários canais. Para uma imagem colorida, cada valor de pixel consiste em três valores, também conhecidos como canais de cores. Uma maneira típica de lidar com esses canais de cores é simplesmente fornecer a cada neurônio as conexões de cada canal, de modo que um neurônio com um tamanho de kernel de 3 x 3 agora terá 3 x 3 x 3 = 27 entradas.
A figura abaixo ilustra três exemplos de como o campo receptivo de três neurônios distintos pode ser organizado para cobrir um subconjunto de pixels de uma imagem com três canais de cores.
2x2 kernel, stride = 1

Figura 9 - Exemplos de como campos receptivos de três neurônios diferentes podem se sobrepor. A
imagem consiste em 6 x 8 pixels. Esquerda:
o kernel 2x2 com stride = 1 precisa de 5 x 7 neurônios para cobrir a imagem completa. Centro: kernel 2x2 com stride = 2 precisa de 3 x 4neurônios. >4 direita: o kernel 3x3 com stride = 2 precisa de 3 x 4 neurônios.

O exemplo mais à esquerda assume um neurônio com um tamanho de kernel de 2 x 2,
organizado com uma passada (stride) de 1. Isso significa que o foco de cada neurônio é separado por apenas um único pixel. O exemplo do meio mostra um cenário semelhante, mas com uma passada de 2.Uma coisa a se notar é que quanto maior a passada, menos neurônios são necessários para cobrir toda a imagem. Finalmente, o exemplo mais à direita mostra um tamanho de kernel de 3x 3 e uma passada de 2. Uma observação importante aqui é que o tamanho e a passada do kernel são parâmetros ortogonais, mas eles interagem. Por exemplo, se escolhermos um tamanho do kernel de 2 x 2 e uma distância de 3, então alguns dos pixels na imagem não serão conectados a nenhum neurônio, o que é lamentável.
O número de neurônios necessários para cobrir a imagem é afetado principalmente pela passada (stride).
Vamos falar agora do comportamento de todos os neurônios em um único canal. Esta grade de neurônios agora cria algo chamado de mapa de características para a imagem.Cada neurônio atuará como um identificador de recurso (padrão) e disparará se o recurso específico for encontrado no local coberto pelo campo receptivo desse neurônio. Por exemplo, se os pesos do neurônio são tais que o neurônio disparará se identificar uma linha vertical, então se houver uma longa linha vertical na imagem, todos os neurônios que estão centralizados nesta linha vertical serão disparados. Dado que todos os neurônios no mapa usam pesos idênticos, não importa onde em uma imagem um elemento aparece. O mapa de feições será capaz de identificá-lo independentemente da localização. Esta é a fonte da propriedade de invariância da translação.
Mais uma coisa a se notar é que cada neurônio não recebe entradas de todos os pixels da imagem.Ou seja, não é uma rede totalmente conectada, mas está escassamente conectada.
Claramente,
isso é benéfico do ponto de vista da eficiência porque menos conexões resultarão em menos cálculos. Também parece intuitivamente errado que um neurônio seja tão especializado que precise considerar cada pixel da imagem para classificar um objeto. Afinal, a imagem de um barco deve ser classificada como um navio, independentemente de o céu estar nublado, o sol ser visível ou as ondas estarem mais altas na água. Ter um neurônio para cada uma dessas condições não seria eficiente. Dessa perspectiva, ter neurônios que simplesmente olham para pedaços menores da imagem faz sentido.
Lembre-se: Um neurônio em uma camada convolucional está escassamente conectado.

A capacidade de detectar apenas um único recurso, como uma linha vertical,
seria muito limitante. Para classificar diferentes tipos de objetos, a rede também precisa ser capaz de identificar linhas horizontais, linhas diagonais e talvez manchas coloridas ou outros blocos de construção primitivos. Isso é resolvido organizando a camada convolucional em vários canais(mapas de recursos). Ou seja, da mesma forma que descrevemos que uma imagem possui três canais (cada um correspondendo a uma cor), uma camada convolucional possui vários canais de saída. Cada canal corresponde a um recurso específico, como uma linha vertical, uma linha horizontal, uma linha diagonal ou uma mancha roxa.
Ilustramos isso na figura abaixo com uma camada convolucional com quatro canais de saída. Cada canal atua como um único mapa de característica identificando uma característica específica em qualquer local da imagem. O canal mais inferior pode identificar linhas verticais. Opróximo canal pode identificar linhas horizontais e os dois canais superiores podem identificar linhas diagonais,um canal para cada orientação. Cada canal consiste em 3x6 neurônios (indicados pelos números 3e 6 na figura), mas apenas os neurônios a serem ativados são explicitamente desenhados como pontos pretos em cada mapa de características. Você pode ver como os neurônios ativados correspondem aos padrões na imagem de entrada que correspondem ao recurso que o canal é capaz de identificar.
Diagonal 2

Diagonal 1
Horizontal

Vertical

Input image
Figura 10 - Uma única camada convolucional com quatro canais e 18 neurônios para cada canal. Cada ponto representa um neurônio excitado ou ativado.
A figura não indica o tamanho dos kernel ou a passada, mas parece que o número de neurônios em cada canal é menor que o número de pixels na imagem de entrada, já que o tamanho dos quatro retângulos é menor que o tamanho de o retângulo da imagem de entrada. Este é um arranjo comum.
É fácil se confundir com a terminologia aqui porque cada um desses canais parece uma
"camada"
de neurônios, mas a terminologia adequada é "canal" ou "mapa de características", e todos os canais de saída juntos formam uma única camada convolucional. Cada camada convolucional recebe entradas de vários canais de entrada e produz vários canais de saída. Todos os canais em uma única camada convolucional têm o mesmo número de neurônios e todos os neurônios em um canal compartilham pesos uns com os outros. No entanto, canais diferentes na mesma camada têm pesos diferentes.
Uma camada convolucional consiste em vários canais ou mapas de recursos. Todos os neurônios dentro do mesmo canal compartilham pesos.
Embora tenhamos falado sobre recursos explícitos que os canais irão identificar, como linhas horizontais, verticais e diagonais, não precisamos definir explicitamente esses recursos. A rede aprenderá quais recursos procurar durante o processo de treinamento.
REDES NEURAIS RECoRRENTES.

Eu aposto que você consegue recitar o alfabeto sem maiores problemas. Agora tente recitá-lo de trás para frente e você verá que esta última tarefa é bem mais difícil.Vamos tentar outro experimento. Tente ler a seguinte frase:
"Miséria nossa de legado o criatura nenhuma a transmiti não, filhos tive não."

Ela não faz muito sentido, mas se a colocarmos na ordem certa você facilmente reconhecerá o fim de Memórias Póstumas de Brás Cubas:
"Não tive filhos, não transmiti a nenhuma criatura o legado de nossa miséria."

Os dois experimentos acima mostram que algumas informações se fazem presente não apenas pelo conteúdo que as compõe, mas também pela maneira como esse conteúdo está disposto.Em termos mais simples, podemos dizer que existem informações que são sequenciais por natureza.Palavras, frases e enredos são os exemplos mais típico desse tipo de informação, mas não precisamos nos limitar a isso. Quando você vê uma cena em movimento seu cérebro antecipa o que vai acontecer, de forma que uma pausa ou um movimento revertido pode causar estranheza.De fato, estamos sempre prevendo o futuro, seja projetando a trajetória de um objeto que é jogado em sua direção, seja antecipando o sabor do almoço pelo aroma que vem da cozinha.
Dados sequenciais também são comuns em outros campos que não são tão relacionados com a percepção humana. Um exemplo são séries de tempo, como o preço de ações, a taxa de juros ou as exportações de um país.
A forma mais tradicional de lidar com esse tipo de dado é com variáveis defasadas.
Por exemplo,
se você tem dados diários de demanda de sorvete e temperatura, pode ser uma boa ideia usar essas duas vaiáveis defasadas 2 dias para tentar prever a demanda de sorvete no dia seguinte.Nesse caso a variável dependente seria y=demandat+ie as variáveis independentes seriam x=[demandat, demandat-i, tempt, tempt-i]. No entanto, há alguns problemas com essa representação. Por exemplo, como fazer para decidir quantas defasagens é suficiente? Uma vez decidido isso, o que fazer quando algumas observações não têm nem sequer o número mínimo de defasagens? E o que fazer quando o tamanho das sequências é variável? Além disso, se cada observação no tempo tiver muitas variáveis, defasá-las gerará um vetor x tão grande que talvez não caiba na memória!
Não seria ótimo então um modelo que pudesse operarem sequências independentemente do seu tamanho e das suas variações? Melhor ainda seria se esse modelo não aumentasse de tamanho com o aumento das sequências. É para cumprir essas necessidades que podemos utilizarRedes
Neurais Recorrentes. RNRs são Turing Completas, o que significa que seu poder é tão grande que elas têm a capacidade teórica de representar qualquer programa passível de ser feito em um computador. Esse tipo de modelo já existe há um bom tempo, mas só muito recentemente conseguimos alavancar seu enorme potencial para finalidades práticas.
Considere uma rede neural com apenas uma camada oculta. Nesse caso, há apenas uma diferença fundamental entre as redes neurais recorrentes e as redes neurais clássicas que vimos anteriormente: a camada oculta das redes neurais feedforward totalmente conectada recebe sinais apenas da camada de entrada, isto é, dos dados brutos, processa esses sinais e os passa à camada de saída; a camada oculta da rede neural recorrente, por sua vez, recebe sinais tanto da camada de entrada quanto da camada oculta na iteração de tempo anterior.
Em certo sentido, é como se a camada oculta da rede neural recorrente funcionasse como uma memória: a cada período no tempo, a rede neural não só armazena no seu estado oculto informações dos dados observados naquele período no tempo, como também recupera informações do estado oculto anterior que, num cenário ótimo, armazenou toda a informação relevante que aconteceu no passado. Mais ainda, o estado oculto nesse mesmo período pode fornecer informações para a camada de saída, caso seja o momento de realizar uma previsão, e passa informações para o estado oculto do próximo período.
De maneira mais resumida, o estado oculto da RNR recebe informações das variáveis independentes Xt, assim como de seu próprio resultado de processamento Ht-i,só que de um período anterior. Note que período aqui não representa o tempo do relógio, mas um tempo lógico que denota ordem numa sequência. Por exemplo, cada palavra em uma frase denota um período de processamento da RNR.
Redes neurais recorrentes foram feitas para processar sequências, mas tanto a forma como essas sequências são lidas para a rede, quanto a forma como são geradas por ela, são ambas escolhas de arquitetura que dependerão do tipo de aplicação do modelo. Para entender melhor sobre isso, considere a imagem abaixo.
one to one one to many many to one many to many many to many t I 1 í 1
* ► * -

t 1 1 1 1

t t t t t
[ 1 f t

► ►

1 t

No caso one to one temos a clássica rede neural feedforward. Em aplicações one to many, lemos os dados uma única vez para o estado oculto e então passamos esse estado oculto adiante por vários períodos, nos quais também lemos informações contidas nele. Um exemplo de aplicação desse tipo é quando queremos criar um modelo para descrever imagens (image-captioning).Nesse caso, lemos a imagem uma vez para o estado oculto, mas lemos desse estado oculto várias vezes,uma vez para cada palavra gerada na descrição da imagem.

No caso many to one, lemos dos dados várias vezes, mas produzimos uma previsão apenas após ler toda a sequência. Um bom exemplo desse tipo de aplicação é classificação de texto, como análise de sentimentos, onde lemos o texto todo antes de realizar uma previsão.
Por fim, existem dois casos de aplicações many to many. Na primeira delas, nós lemos os dados por alguns períodos antes de começar a soltar previsões. Em outras palavras, há uma defasagem entre a leitura da sequência de entrada e a produção da sequência de saída. Um exemplo de aplicações desse tipo são casos de tradução por máquinas ou transcrição de áudio, onde a RNR lê a sequência por algum tempo antes de começar a gerar a sequência de saída, seja ela as palavras em outra língua ou as palavras correspondentes a um áudio.
O último caso de many to many é quando temos sequências na entrada e na saída da rede, mas cada entrada corresponde a uma saída no mesmo período. Esse tipo de estrutura de dados aparece em séries de tempo e dados em painel, nas quais queremos realizar uma previsão para o período seguinte, dado o que ocorreu neste período de tempo e nos períodos anteriores.
REDES DE HoPFIELD.

Redes de Hopfield, juntamente com as Máquinas de Boltzmann, são fundamentos de diversas arquiteturas e algoritmos modernos de redes neurais. Redes de Hopfield sãoRedes Neurais
Artificiais que possuem arquitetura muito simples. Elas usam diversos recursos também utilizados por Redes Neurais Feedforward. Essas ferramentas são comumente utilizadas em problemas de visão computacional.
Em 1982, Hopfield propôs uma arquitetura muito simples de Rede Neural Artificial, com apenas uma camada. Os neurônios que compõem essa camada são ligados a todos os outros. Isso que faz com que essa rede seja chamada de auto associativa. Esse tipo de rede, após recebertreinamento,busca reconhecer os padrões e retornar os próprios padrões. Isso torna esse tipo de aplicação ideal para preencher gaps de padrões incompletos ou corrompidos.
Na figura abaixo é possível observar uma representação gráfica de uma Redes de
Hopfield. Essa arquitetura de rede é facilmente representável por uma matriz n x n, onde n é o número de neurônios da rede. O valor n que também corresponde ao número de elementos de uma instância de entrada. Cada elemento dessa matriz representa o peso associado à ligação do neurônio j com o neurônio i. Nessa matriz, a diagonal principal terá sempre valor zero, pois os neurônios não estão ligados a si mesmos.
Como a saída dos neurônios está ligada à entrada de todos os outros, elas são aqui chamadas de estados. Esses estados seguem a lógica booleana. A saída dos estados é dada por estados verdadeiros (true = 1) ou falsos (false = -1).
Aplicações Práticas De Redes De Hopfield

Detecção De Limites Tumorais Em Tomografias Computadorizadas

Uma parte importante do diagnóstico médico por imagem é a determinação dos limites de uma área de interesse. A figura abaixo apresenta um exemplo da aplicação desse problema. Esse problema pode ser modelado como um problema de otimização, que busca minimizar a função de energia de uma rede baseada em um modelo de contorno ativo.
Uma aplicação importante para esse tipo de problema é a caracterização de tumores cerebrais a partir de imagens geradas em tomografias computadorizadas ou em exames de ressonância magnética. As informações obtidas nesse tipo de exame são importantes para o planejamento do tratamento. Nesse caso, pode-se utilizar uma versão modificada da Rede de Hopfield para tratar o problema4.
Reconhecimento De Objetos

Existem diversas aplicações onde é importante reconhecer padrões em imagens. A
maior parte das ferramentas de aprendizado segue um modelo feed-fbrward. Essas aplicações possuem como principal desvantagem a propagação de quaisquer falhas que aconteçam na camada inicial do modelo, devido à direção do fluxo de dados.
Afigura acima exemplifica uma aplicação de reconhecimento de objetos. Uma solução proposta para o problema de redes feed-forward é o uso de diversas Redes de Hopfield interligadas em cascata, para garantir que os valores sejam bidireccionalmente atualizados a cada iteração.
LoNG SHoRT-TERM MEMoRY (LSTM).

Para superar alguns dos problemas das RNNs, podemos usar algumas de suas variações. Uma delas é chamada LSTM ou Long Short Term Memory, um tipo de rede neural recorrente,que é usada em diversos cenários de Processamento de Linguagem Natural. Nos últimos anos, tem
4 Para saber mais acesse: fonte: http://dlia.ir/Scientific/IEEE/iell/42/11977/00552055.pdf havido um incrível sucesso ao aplicar as RNNs a uma variedade de problemas:reconhecimento de fala, modelagem de idiomas, tradução, legendas de imagens...
Entretanto, boa parte do sucesso das RNNs se deve a uma de suas variações, as LSTMs,
um tipo muito especial de rede neural recorrente que funciona, para muitas tarefas, muito melhor do que a versão padrão. Quase todos os resultados empolgantes baseados em redes neurais recorrentes são alcançados com LSTMs. Vamos então compreender o que torna as LSTMs tão especiais.
A LSTM é uma arquitetura de rede neural recorrente (RNN) que "lembra" valores em intervalos arbitrários. A LSTM é bem adequada para classificar, processar e prever séries temporais com intervalos de tempo de duração desconhecida. A insensibilidade relativa ao comprimento do gap dá uma vantagem à LSTM em relação a RNNs tradicionais (também chamadas "vaniIla"),Modelos
Ocultos de Markov (MOM) e outros métodos de aprendizado de sequências.

A estrutura de uma RNN é muito semelhante ao Modelo Oculto de Markov. No entanto, a principal diferença é como os parâmetros são calculados e construídos. Uma das vantagens daLSTM é a insensibilidade ao comprimento do gap. RNN e MOM dependem do estado oculto antes da emissão/sequência. Se quisermos prever a sequência após 1.000 intervalos em vez de10, o modelo esqueceu o ponto de partida até então. Mas um modelo LSTM é capaz de"lembrar" por conta de sua estrutura de células, o diferencial da arquitetura LSTM.
A LSTM possui uma estrutura em cadeia que contém quatro redes neurais e diferentes blocos de memória chamados células.
A informação é retida pelas células e as manipulações de memória são feitas pelos portões(gates). Existem três portões:

Forget Gate: As informações que não são mais úteis no estado da célula são removidas com o forget gate. Duas entradas: xt (entrada no momento específico) e ht-i (saída de célula anterior)são alimentadas ao gate e multiplicadas por matrizes de peso, seguidas pela adição do bias. Oresultante é passado por uma função de ativação que fornece uma saída binária. Se para um determinado estado de célula a saída for o, a informação é esquecida e para a saída 1, a informação é retida para uso futuro.
Input Gate: A adição de informações úteis ao estado da célula é feita pelo input gate. Primeiro, a informação é regulada usando a função sigmoide que filtra os valores a serem lembrados de forma similar ao forget gate usando as entradas ht-i e xt. Então, um vetor é criado usando a função tanh
(hyperbolic tangentfunction') que dá saída de -1 a +1, que contém todos os valores possíveis de ht-i e xt. Os valores do vetor e os valores regulados são multiplicados para obter as informações úteis
Output Gate: A tarefa de extrair informações úteis do estado da célula atual para ser apresentadas como uma saída é feita pelo output gate. Primeiro, um vetor é gerado aplicando a função tanh na célula. Então, a informação é regulada usando a função sigmóide que filtra os valores a serem lembrados usando as entradas ht-i e xt. Os valores do vetor e os valores regulados são multiplicados para serem enviados como uma saída e entrada para a próxima célula.
A célula RNN recebe duas entradas, a saída do último estado oculto e a observação no tempo = t.Além do estado oculto, não há informações sobre o passado para se lembrar. A memória de longo prazo é geralmente chamada de estado da célula. As setas em loop indicam a natureza recursiva da célula. Isso permite que as informações dos intervalos anteriores sejam armazenadas na célulaLSTM. O estado da célula é modificado pelo forget gate colocado abaixo do estado da célula e ajustado pela porta de modulação de entrada.
(Não ser preocupe em entender o funcionamento das LSTM, para concurso, até hoje, não temos questões deste assunto, acredito que a primeira cobrança será relacionado aos tipos das portas ou ao fato de LSTM ser um tipo de RNN)
Algumas das famosas aplicações das LSTMs incluem:

* Modelagem de Linguagem

* Tradução de Idiomas

* Legendas em Imagens

* Geração de Texto

* Chatbots

REDES PERCEPTRoN MULTICAMADAS RECoRRENTES.

Inputs Weights m
^(wixi)+bias

Summatíon and Bias
1, if^wx+b^O

0, if£ wx+b<D y

Activatíon Output

Um Perceptron é um classificador linear; ou seja, é um algoritmo que classifica a entrada separando duas categorias com uma linha reta. A entrada geralmente é um vetor de recursos x multiplicado por pesos w e adicionado a um viés (ou bias) b. Aqui um exemplo doPerceptron: y =
w * x + b. Um Perceptron produz uma única saída com base em várias entradas de valor real,formando uma combinação linear usando os pesos (e às vezes passando a saída através de uma função de ativação não linear).
Rosenblatt construiu um Perceptron de uma camada. Ou seja, seu algoritmo não inclui múltiplas camadas, o que permite que as redes neurais modelem uma hierarquia de recursos. Isso impede que o Perceptron consiga realizar classificação não linear, como a função XOR (um disparador do operador XOR quando a entrada exibe uma característica ou outra, mas não ambas,significa "OR
exclusivo").

Um Multilayer Perceptron (MLP) é uma rede neural artificial composta por mais de umPerceptron. Eles são compostos por uma camada de entrada para receber o sinal, uma camada de saída que toma uma decisão ou previsão sobre a entrada, e entre esses dois, um número arbitrário de camadas ocultas que são o verdadeiro mecanismo computacional do MLP. MLPs com uma camada oculta são capazes de aproximarqualquerfunção contínua.
O Multilayer Perceptron é uma espécie de "Hello World" da aprendizagem profunda: uma boa forma de começar quando você está aprendendo sobre Deep Learning.
Os MLPs são frequentemente aplicados a problemas de aprendizagem supervisionados:
treinam em um conjunto de pares entrada-saída e aprendem a modelar a correlação (ou dependências)entre essas entradas e saídas. O treinamento envolve o ajuste dos parâmetros, ou os pesos e bias,do modelo para minimizar o erro. O backpropagation é usado para fazer os ajustes dos pesos e de bias em relação ao erro, e o próprio erro pode ser medido de várias maneiras,inclusive pelo erro quadrático médio (MSE - Mean Squared Error).
As redes feed forward, como MLPs, são como ping-pong. Elas são principalmente envolvidas em dois movimentos, uma constante de ida e volta. Na passagem para a frente, o fluxo de sinal se move da camada de entrada através das camadas ocultas para a camada de saída e a decisão da camada de saída é medida em relação às saídas esperadas.
Na passagem para trás, usando o backpropagation e a regra da cadeia (Chain Rule),
derivadas parciais da função de erro dos vários pesos e bias são reproduzidos através do MLP.Esse ato de diferenciação nos dá um gradiente, ao longo do qual os parâmetros podem ser ajustados à medida que movem o MLP para valores mais próximos do erro mínimo. Isso pode ser feito com qualquer algoritmo de otimização baseado em gradiente, como descida estocástica do gradiente. A rede continua jogando aquele jogo de ping-pong até que o erro não possa mais ser reduzido(chegou ao mínimo possível). Este estado é conhecido como convergência.
MÁQUINAS DE BoLTZMANN.

Uma Máquina de Boltzmann é um tipo de rede neural recorrente estocástica. Pode ser visto como a contrapartida estocástica e generativa das Redes Hopfield. Foi uma das primeiras redes neurais capazes de aprender representações internas e é capaz de representar e resolver problemas combinatórios difíceis.
O objetivo do aprendizado do algoritmo da Máquina de Boltzmann é maximizar o produto das probabilidades que a Máquina de Boltzmann atribui aos vetores binários no conjunto de treinamento. Isso equivale a maximizar a soma das probabilidades de log que a Máquina deBoltzmann atribui aos vetores de treinamento. Também é equivalente a maximizar a probabilidade de obtermos exatamente os N casos de treinamento se fizéssemos o seguinte:
1) Deixar a rede se estabelecer em sua distribuição estacionária no tempo
N diferente, sem entrada externa e;
2) Mudaro vetorvisível uma vez em cada passada.

Um procedimento eficiente de aprendizado de mini-lote foi proposto para as
Máquinas de
Boltzmann por Salakhutdinov e Hinton em 2012.

Em uma Máquina de Boltzmann geral, as atualizações estocásticas de unidades precisam ser sequenciais. Existe uma arquitetura especial que permite alternar atualizações paralelas que são muito mais eficientes (sem conexões dentro de uma camada, sem conexões de camada ignorada).Este procedimento de mini-lote torna as atualizações da Máquina de Boltzmann mais paralelas.Isso é chamado de Deep Boltzmann Machines (DBM), uma Máquina de Boltzmann geral, mas com muitas conexões ausentes.
Em 2014, Salakhutdinov e Hinton apresentaram outra atualização para seu modelo,
chamando-o de Máquinas Boltzmann Restritas. Elas restringem a conectividade para facilitar a inferência e a aprendizagem (apenas uma camada de unidades escondidas e sem conexões entre unidades ocultas). Em um RBM, é preciso apenas um passo para alcançar o equilíbrio.
DEEP BELIEF NETwoRKS.

O backpropagation é considerado o método padrão em redes neurais artificiais para calcular a contribuição de erro de cada neurônio após processar um lote de dados. No entanto, existem alguns problemas importantes no backpropagation. Em primeiro lugar, requer dados de treinamento rotulados; enquanto muitas vezes quase todos os dados estão sem rótulos. Em segundo lugar, o tempo de aprendizagem não escala bem, o que significa que é muito lento em redes com múltiplas camadas ocultas. Em terceiro lugar, você pode ficar preso em um"máximo local", não atingindo o melhor valor para a solução. Portanto, para redes profundas, o backpropagation está longe de ser ótimo.
Para superar as limitações do backpropagation, os pesquisadores consideraram o uso de abordagens de aprendizado sem supervisão. Isso ajuda a manter a eficiência e a simplicidade de usar um método de gradiente para ajustar os pesos, mas também usá-lo para modelar a estrutura da entrada sensorial. Em particular, eles ajustam os pesos para maximizar a probabilidade de um modelo gerador ter gerado a entrada sensorial. A questão é que tipo de modelo generativo devemos aprender? Pode ser um modelo baseado em energia como uma Máquina de Boltzmann?Ou um modelo causal feito de neurônios? Ou um híbrido dos dois?

Deep Belief Network (DBN)

O Backfed Input Cell
Input Cell

A Noisy Input Cell
Hidden Cell

O Probablistic Hidden Cell
A Spiking Hidden Cell

Output Cell

Match Input Output Cell
Recurrent Cell

Memory Cell

Different Memory Cell
Kemel

O Convolution or Pool

Uma Deep Belief Network pode ser definida como uma pilha de Máquinas de Boltzmann
Restritas
(RBM - Restricted Boltzmann Machines), em que cada camada RBM se comunica com as camadas anterior e posterior. Os nós de qualquer camada única não se comunicam lateralmente.
Esta pilha de RBMs pode terminar com uma camada Softmax para criar um classificador, ou simplesmente pode ajudar a agrupar dados não gravados em um cenário de aprendizado sem supervisão.
Com a exceção das camadas inicial e final, cada camada em uma Deep Belief Network tem uma função dupla: ela serve como a camada oculta para os nós que vem antes, e como a camada de entrada (ou "visível") para a nós que vem depois. É uma rede construída de redes de camada única.
As Deep Belief Networks são usadas para reconhecer, agrupar e gerar imagens, sequências de vídeos e dados de captura de movimento. Outra aplicação das Deep BeliefNetworks é no
Processamento de Linguagem Natural.

