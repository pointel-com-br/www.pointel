# Desenvolvimento de Informação - Aprendizado de máquina. Classificação. Regressão. Agrupamento. Redução. Associação. Recomendação

Índice

1) Aprendizado Não Supervisionado w ww. estrategiaconcursos. com.br
Conteúdo da Aula

Aprendizado Não Supervisionado

Redução da dimensionalidade

Clusterização

Agrupamento K-Means.

Fuzzy K-means.

Agrupamento Hierárquico

Mistura de Gaussianas.

Problemas associados E Aplicações possíveis ao agrupamento

Regras de associação

THIAGO CAVALCANTI

PROFESSOR

CoNTEÚDo DA AULA

2 Aprendizado não supervisionado. 2.1 Redução de dimensionalidade: PCA. 2.2 Agrupamento
K-
Means. 2.3 Mistura de Gaussianas. 2.4 Agrupamento Hierárquico. 2.5 Regras de associação.
2.6
Aprendizado não supervisionado com Python scikit-learn.

APRENDIZADo NÃo SUPERVISIoNADo

Em alguns problemas de reconhecimento de padrões, os dados de treinamento consistem em um conjunto de vetores de entrada x sem nenhum valor alvo correspondente. Oobjetivo em tais problemas de aprendizado não supervisionado pode ser descobrir grupos de exemplos semelhantes dentro dos dados, onde é chamado de agrupamento, ou determinar como os dados são distribuídos no espaço, conhecido como estimativa de densidade . Para apresentar em termos mais simples, para um espaço n amostrado xl a xn, rótulos de classe verdadeiros não são fornecidos para cada amostra.
Vamos começar nosso estudo de aprendizado supervisionado com os seus pontos fracos ou problemas, na lista abaixo apresentamos os problemas do Aprendizado Não Supervisionado:
* O aprendizado não supervisionado é mais difícil em comparação com as tarefas de aprendizado supervisionado.
* Como sabemos se os resultados são significativos, já que não há rótulos de resposta disponíveis?
o Deixar o especialista ver os resultados (avaliação externa)

o Definir uma função objetivo no agrupamento (avaliação interna)

Então ... por que o aprendizado não supervisionado é necessário apesar desses problemas?

Primeiramente porque rotular grandes conjuntos de dados é muito caro e,
portanto, podemos rotular apenas alguns exemplos manualmente. Exemplo: reconhecimento de fala
Segundo, pode haver casos em que não sabemos em quantas/quais classes os dados são divididos.Exemplo: mineração de dados

Por fim, podemos querer usar o agrupamento para obter algumas informações sobre a estrutura dos dados antes de projetar um classificador.
Agora que já entendemos a importância das tarefas de aprendizado não supervisionado,
vamos falar um pouco sobre a sua taxonomia. A aprendizagem não supervisionada pode ser classificada em duas categorias:
* Aprendizado Paramétrico Não Supervisionado - Neste caso, assumimos uma distribuição paramétrica de dados. Ela assume que os dados da amostra vêm de uma população que segue uma distribuição de probabilidade baseada em um conjunto fixo de parâmetros.Teoricamente, em uma família que segue a distribuição normal, todos os membros têm a mesma forma e são parametrizados pela média e desvio padrão. Isso significa que se você conhece a média e o desvio padrão, e que a distribuição é normal, você conhece a probabilidade de qualquer observação futura. O Aprendizado ParamétricoNão
Supervisionado envolve a construção de Modelos de Mistura Gaussianas e o uso do algoritmo Expectativa-Maximização para prever a classe da amostra em questão. Este caso é muito mais difícil do que o aprendizado supervisionado padrão porque não há rótulos de resposta disponíveis e, portanto, não há uma medida correta de precisão disponível para verificar o resultado.
* Aprendizado não supervisionado não paramétrico - Na versão não parametrizada do aprendizado não supervisionado, os dados são agrupados em clusters, onde cada cluster(espera-se) diz algo sobre categorias e classes presentes nos dados. Esse método é comumente usado para modelar e analisar dados com tamanhos de amostra pequenos. Ao contrário dos modelos paramétricos, os modelos não paramétricos não exigem que o modelador faça suposições sobre a distribuição da população e, portanto, às vezes são chamados de métodos livre de distribuição.
REDUçÃo DA DIMENSIoNALIDADE.

Muitos problemas de aprendizado de máquina envolvem milhares ou até milhões de recursos para cada instância de treinamento. Todos esses recursos não apenas tornam o treinamento extremamente lento, mas também podem tornar muito mais difícil encontrar uma boa solução. Este problema é muitas vezes referido como a maldição da dimensionalidade. Felizmente, em problemas do mundo real, muitas vezes é possível reduzir consideravelmente o número de recursos, transformando um problema intratável em um problema tratável.
Reduzir a dimensionalidade causa alguma perda de informação (assim como a compactação de uma imagem em JPEG pode degradar sua qualidade),portanto, mesmo que isso acelere o treinamento, pode piorar um pouco o desempenho do sistema. Também torna seus pipelines um pouco mais complexos e, portanto, mais difíceis de manter. Desta forma, se o treinamento for muito lento, você deve primeiro tentar treinar seu sistema com os dados originais antes de considerar o uso de redução de dimensionalidade.Em alguns casos, reduzir a dimensionalidade dos dados de treinamento pode filtrar alguns ruídos e detalhes desnecessários e, assim, resultar em maior desempenho, mas em geral não; só vai acelerar o treinamento.
Nós estamos tão acostumados a viver em um mundo de três dimensões que nossa intuição falha quando tentamos imaginar um espaço de dimensão mais alta. Mesmo um hipercubo4D básico é incrivelmente difícil de imaginar em nossas mentes (veja a
Figura abaixo), muito menos um elipsoide de 200 dimensões dobrado em um espaço de 1.000 dimensões.
*-- *

*rçy Y

* *----►*

0 1

*-- * A

2 3

Z

\r V

4 #Dim

Acontece que muitas coisas se comportam de maneira muito diferente no espaço de alta dimensão. Por exemplo, se você escolher um ponto aleatório em um quadrado unitário (um quadrado 1 x 1), ele terá apenas cerca de 0,4% de chance de estar localizado a menos de0,001 de uma borda (em outras palavras, é muito improvável que um ponto aleatório será"extremo" ao longo de qualquer dimensão). Mas em um hipercubo de unidade de
10.000
dimensões, essa probabilidade é maior que 99,999999%. A maioria dos pontos em um hipercubo de alta dimensão está muito próxima da borda.
Aqui está uma diferença mais problemática: se você escolher dois pontos aleatoriamente em um quadrado unitário, a distância entre esses dois pontos será, em média,aproximadamente 0,52. Se você escolher dois pontos aleatórios em um cubo 3D
unitário,
a distância média será de aproximadamente 0,66. Mas e quanto a dois pontos escolhidos aleatoriamente em um hipercubo de 1.000.000 dimensões? A distância média,acredite ou não, será de cerca de 408,25 (aproximadamente)! Isso é contraintuitivo: como dois pontos podem estar tão distantes quando ambos estão dentro do mesmo hipercubo unitário?Bem, há muito espaço em grandes dimensões. Como resultado, conjuntos de dados de alta dimensão correm o risco de serem muito esparsos: a maioria das instâncias de treinamento provavelmente estarão distantes umas das outras. Isso também significa que uma nova instância provavelmente estará longe de qualquer outra instância de treinamento, tornando as previsões muito menos confiáveis do que em dimensões inferiores, pois serão baseadas em extrapolações muito maiores. Em suma,quanto mais dimensões o conjunto de treinamento tiver, maior o risco de overfitting.
Em teoria, uma solução para a maldição da dimensionalidade poderia ser aumentar o tamanho do conjunto de treinamento para atingir uma densidade suficiente de instâncias de treinamento. Infelizmente, na prática, o número de instâncias de treinamento necessárias para atingir uma determinada densidade cresce exponencialmente com o número de dimensões.
Antes de apresentarmos alguns algoritmos específicos de redução de dimensionalidade,vamos dar uma olhada nas duas principais abordagens para reduzir a dimensionalidade:projeção e aprendizado de variedades.

Projeção

Na maioria dos problemas do mundo real, as instâncias de treinamento não são distribuídas uniformemente em todas as dimensões. Muitos recursos são quase constantes, enquanto outros são altamente correlacionados. Como resultado, todas as instâncias de treinamento estão dentro (ou próximas a) um subespaço de dimensão muito inferior do espaço de alta dimensão. Isso soa muito abstrato, então vamos ver um exemplo. Na figura abaixo você pode ver um conjunto de dados 3D representado por círculos.
1.00

0.75

0.50

025 m

0.00

-0.25

-0.50

-0.75

-1.00

-0.5

Figura 1 - Um conjunto de dados 3D próximo a um subespaço 2D

Observe que todas as instâncias de treinamento ficam próximas a um plano:
este é um subespaço de dimensão inferior (2D) do espaço de alta dimensão (3D). Se projetarmos cada instância de treinamento perpendicularmente nesse subespaço (como representado pelas linhas curtas que conectam as instâncias ao plano), obteremos o novo conjunto de dados2D mostrado na figura abaixo. Show! Acabamos de reduzir a dimensionalidade do conjunto de dados de 3D para 2D. Observe que os eixos correspondem às novas feições zi e Z2 (as coordenadas das projeções no plano).
H- *

*

►

*

*

*

*

*

+

* *

á Fb

►

* *

—

-1.5 -1.0 -0.5 0.0 0.5 1.0

Zi

Figura 2 - O novo conjunto de dados 2D após a projeção

No entanto, a projeção nem sempre é a melhor abordagem para redução de dimensionalidade. Em muitos casos, o subespaço pode girar (tw/st and turn), como no famoso conjunto de dados de brinquedo de rolo suíço (no Brasil a gente chama de rocambole!:) representado na figura a seguir.
Figura 3 - Conjunto de dados de brinquedo de rolo suíço

Simplesmente projetar em um plano (por exemplo, soltando X3) esmagaria diferentes camadas do rocambole, como mostrado no lado esquerdo da figura abaixo. Oque você realmente quer é desenrolar o rolo suíço para obter o conjunto de dados2D no lado direito da figura a seguir.
Xi Zi

Figura 4 - Esmagar projetando em um plano (esquerda) versus desenrolar o rocambole (direita)

Aprendizado múltiplo (manifold learning)

O rolo suíço é um exemplo de manifold 2D. Simplificando, um manifold 2D é uma forma2D que pode ser dobrada e torcida em um espaço de dimensão superior. Mais geralmente,um manifold d-dimensional é uma parte de um espaço n-dimensional (onde d
<ri) que se assemelha localmente a um hiperplano d-dimensional. No caso do rolo suíço, d= 2 e n =
3: assemelha-se localmente a um plano 2D, mas quando enrolado chega a terceira dimensão.
Muitos algoritmos de redução de dimensionalidade funcionam modelando a variedade na qual estão as instâncias de treinamento; isso é chamado deAprendizagem Múltipla
(manifold learing). Isso está associado a suposição da variedade
(manifold assumption),
também chamada de hipótese da variedade (manifold hypothesis), que sustenta que a maioria dos conjuntos de dados de alta dimensão do mundo real fica perto de uma variedade de dimensão muito mais baixa. Esta suposição é muitas vezes observada empiricamente.
A suposição da variedade é frequentemente acompanhada por outra suposição implícita:que a tarefa em mãos (por exemplo, classificação ou regressão) será mais simples se expressa no espaço de dimensão inferior da variedade. Por exemplo, na parte superior da figura seguir, o rolo suíço é dividido em duas classes: no espaço 3D (à esquerda), o limite de decisão seria bastante complexo, mas no espaço múltiplo desenrolado 2D (à direita ), o limite de decisão é uma linha reta.
No entanto, essa suposição implícita nem sempre se sustenta. Por exemplo, na parte inferior da figura a seguir, o limite de decisão está localizado em xi =5. Esse limite de decisão parece muito simples no espaço 3D original (um plano vertical), mas parece mais complexo no manifold desenrolado (uma coleção de quatro segmentos de linha independentes).
Resumindo, reduzir a dimensionalidade do seu conjunto de treinamento antes de treinar um modelo geralmente acelera o treinamento, mas nem sempre pode levar a uma solução melhor ou mais simples; tudo depende do conjunto de dados.
Espero que agora você tenha uma boa noção do que é a maldição da dimensionalidade e como os algoritmos de redução de dimensionalidade podem combatê-la,especialmente quando a suposição da variedade é válida.
Figura 5 - O limite de decisão nem sempre pode ser mais simples com dimensões mais baixas

Vamos aproveitar o restante desta seção para apresentarmos o algoritmo de
PCA. (Sei que já falamos sobre ele na aula passada, mas queria apresentá-lo em outra perspectiva, pode ser?)
PCA - Principal component analysis

Análise de Componentes Principais (PCA)é de longe o algoritmo de redução de dimensionalidade mais popular. Primeiro, ele identifica o hiperplano mais próximo dos dados e, em seguida, projeta os dados nele, exatamente como na figura 16.
Preservando a Variação

Antes de você pode projetar o conjunto de treinamento em um hiperplano de dimensão inferior, primeiro você precisa escolher o hiperplano correto. Por exemplo, um conjunto de dados 2D simples é representado à esquerda na figura a seguir, juntamente com três eixos diferentes (ou seja, hiperplanos 1 D). À direita está o resultado da projeção do conjunto de dados em cada um desses eixos. Como você pode ver, a projeção na linha sólida preserva a variação máxima, enquanto a projeção na linha pontilhada preserva muito pouca variação e a projeção na linha tracejada preserva uma quantidade intermediária de variação.
i 1 r

—I 1 1 1 V-

-1.0 -0.5 0.0 0.5 1.0

Xi

2 1 ( ) 2

Zi

Figura 6 - Selecionando o subespaço para projetar

Parece razoável selecionar o eixo que preserva a quantidade máxima de variância, pois provavelmente perderá menos informações do que as outras projeções.Outra forma de justificar essa escolha é que é o eixo que minimiza a distância quadrática média entre o conjunto de dados original e sua projeção nesse eixo. Esta é a ideia bastante simples por trás do PCA.
Componentes principais

O PCA identifica o eixo que responde pela maior quantidade de variação no conjunto de treinamento. Na figura acima, é a linha contínua. Ele também encontra um segundo eixo,ortogonal ao primeiro, que responde pela maior quantidade de variância restante. Neste exemplo 2D não há escolha: é a linha pontilhada. Se fosse um conjunto de dados de dimensão superior, o PCA também encontraria um terceiro eixo, ortogonal aos dois eixos anteriores, e um quarto, um quinto e assim por diante - tantos eixos quanto forem o número de dimensões no conjunto de dados.
O / -esimo eixo é chamado de /-esimo componente principal (PC) dos dados.
Na figura acima,
o primeiro PC é o eixo no qual o vetor d se encontra, e o segundo PC é o eixo no qual o vetor c2 se encontra. Na Figura 16, os dois primeiros PCs são os eixos ortogonais sobre os quais as duas setas repousam, no plano, e o terceiro PC é o eixo ortogonal a esse plano.
Então, como você pode encontrar os principais componentes de um conjunto de treinamento? Felizmente, existe uma técnica de fatoração de matriz padrão chamadaSingular Value Decomposition (SVD) que pode decompor a matriz do conjunto de treinamento X na multiplicação de três matrizes UZVT, onde V contém os vetores unitários que definem todos os componentes principais que estamos procurando.
/I

V = Cl

\l

Figura - Matriz de componentes principais

O seguinte código em Python usa a função do NumPy svd() para obter todos os componentes principais do conjunto de treinamento e, em seguida, extrai os dois vetores unitários que definem os dois primeiros PCs:
X_centered = X - X.mean(axis=0)
U, s, Vt = np.linalg.svd(X_centered)
d = Vt.T[:, 0]

c2 = Vt.T[:, 1]

O PCA assume que o conjunto de dados está centrado em torno da origem. Como veremos, o PCA das classes do Scikit-Learn cuida de centralizar os dados para você. Se você mesmo implementar o PCA (como no exemplo anterior) ou se usar outras bibliotecas,não se esqueça de centralizar os dados primeiro.

Projetando para Dimensões d

Uma vez que você identificou todos os componentes principais, você pode reduzir a dimensionalidade do conjunto de dados para d dimensões projetando-o no hiperplano definido pelos primeiros d componentes principais. A seleção desse hiperplano garante que a projeção preservará o máximo de variação possível. Por exemplo, naFigura 16, o conjunto de dados 3D é projetado no plano 2D definido pelos dois primeiros componentes principais, preservando grande parte da variação do conjunto de dados.Como resultado,
a projeção 2D se parece muito com o conjunto de dados 3D original.

Para projetar o conjunto de treinamento no hiperplano e obter um conjunto de dados reduzido Xd.proj de dimensionalidade d, calcule a multiplicação da matriz do conjunto de treinamento X pela matriz Wd, definida como a matriz contendo as primeiras d colunas deV, como mostrado na equação abaixo.

xd.proj = xwd

Projetando o conjunto de treinamento para d dimensões

O código Python a seguir projeta o conjunto de treinamento no plano definido pelos dois primeiros componentes principais:
W2 = Vt.T[:, :2]

X2D = X_centered.dot(W2)

Aí está! Agora você sabe como reduzir a dimensionalidade de qualquer conjunto de dados em qualquer número de dimensões, preservando o máximo de variação possível.
Usando o Scikit-Learn

A classe que implementa o PCA de Scikit-Learn usa a decomposição SVD para implementar o PCA, assim como fizemos anteriormente. O código a seguir aplica o PCApara reduzir a dimensionalidade do conjunto de dados para duas dimensões (observe que ele automaticamente se encarrega de centralizar os dados):
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)

X2D = pca.fit_transform(X)

Após ajustar o transformador do PCA ao conjunto de dados, seu atributo components_mantém a transposição de Wd (por exemplo, o vetor unitário que define o primeiro componente principal é igual a pca.components_.T[:, 0]).
Razão de Variação Explicada

Outra informação útil é a razão de variância explicada de cada componente principal,disponível através da variável explained_variance_ratio_.A razão indica a proporção da variância do conjunto de dados que se encontra ao longo de cada componente principal.Por exemplo, vejamos as razões de variação explicadas dos dois primeiros componentes do conjunto de dados 3D representados na Figura 16:
>>> pca.explained_variance_ratio_
array([0.84248607, 0.14631839])

Essa saída informa que 84,2% da variância do conjunto de dados está no primeiro PC e14,6% no segundo PC. Isso deixa menos de 1,2% para o terceiro PC,
portanto, é razoável supor que o terceiro PC provavelmente carrega poucas informações.
Escolhendo o número certo de dimensões

Em vez dede escolher arbitrariamente o número de dimensões para reduzir, é mais simples escolher o número de dimensões que somam uma porção suficientemente grande da variância (por exemplo, 95%). A menos, é claro, que você esteja reduzindo a dimensionalidade para visualização de dados - nesse caso, você desejará reduzir a dimensionalidade para 2 ou 3.
O código a seguir executa o PCA sem reduzir a dimensionalidade e, em seguida, calcula o número mínimo de dimensões necessárias para preservar 95% da variância do conjunto de treinamento:
pca = PCA()
pca.fit(X_train)

cumsum = np.cumsum(pca.explained_variance_ratio_)
d = np.argmax(cumsum >= 0.95) + 1

Você pode então definir n_components=d e executar o PCA novamente.
Mas há uma opção muito melhor: em vez de especificar o número de componentes principais que você deseja preservar, você pode definir n_component para ser um número entre 0,0 e 1,0,indicando a proporção de variância que deseja preservar:

pca = PCA(n_components=0.95)
X_reduced = pca.fit_transform(X_train)

Ainda outra opção é plotar a variância explicada em função do número de dimensões(simplesmente plotar cumsum; veja a figura abaixo). Geralmente haverá um cotovelo(elbow) na curva, onde a variância explicada para de crescer rapidamente.
Nesse caso, você pode ver que reduzir a dimensionalidade para cerca de 100 dimensões não perderia muita variância explicada.
Figura 7 -Variação explicada em função do número de dimensões

Se você chegou até aqui e está com dificuldade de entender esse conteúdo de redução de dimensionalidade. Deixa-me resumir os conceitos básicos para você:
* Redução de dimensionalidade é uma tarefa cujo objetivo é simplificar os dados sem perder muitas informações.
* Uma maneira de fazer isso é mesclar vários recursos correlacionados em um.

* Por exemplo, a quilometragem de um carro pode estar fortemente correlacionada com sua idade, então o algoritmo de redução de dimensionalidade irá mesclá-los em um recurso que representa o desgaste do carro. Esse método é chamado de extração de recurso .
* Alguns algoritmos

* Análise de componente principal (PCA) : Encontra a transformação linear que captura a maior parte da variação no conjunto de dados existente.
* Aprendizagem múltipla: identifica uma transformação não linear que produz uma representação dimensional inferior dos dados.
* Autoencoders: usa uma rede neural para compactar dados de forma não linear com perda mínima de informações
* A redução da dimensionalidade produz novos dados que capturam as informações mais importantes contidas nos dados de origem. Em vez de agrupar dados em clusters enquanto retêm os dados originais, esses algoritmos transformam os dados com o objetivo de usar menos recursos para representar as informações originais.
Antes de continuarmos, vamos resolver uma questão sobre o assunto ...

1. Questão inédita

São considerados algoritmos para redução de dimensionalidade:

a) PCA, Autoencoder e aprendizagem múltipla b) KNN, CART, K-means c) C4.5, Apriori, FP-Growth d) Árvore de decisão, SVM e PageRank e) SVM, KNN, Naive Bayes
Comentário: A alternativa A apresentar algoritmos usados para a redução de dimensionalidade. As demais letras apresentam algoritmos de:
Classificação: KNN, SVM, Naive Bayes

Árvore de decisão: CART, C4.5

Regra de associação: Apriori, FP-Growth

Clusterização: K-means

Gabarito: A

CLUSTERIZAçÃo

O agrupamento pode ser considerado um problema de aprendizado não supervisionado mais importante; assim, como qualquer outro problema desse tipo, trata-se de encontrar uma estrutura em uma coleção de dados não rotulados. Uma definição vaga de agrupamento poderia ser "o processo de organizar objetos em grupos cujos membros são semelhantes de alguma forma".Um cluster é, portanto, uma coleção de objetos que são "semelhantes" entre eles e são"dissimilares"
dos objetos pertencentes a outros clusters.

Agrupamento baseado em distância .

Dado um conjunto de pontos, com noção de distância entre os pontos, agrupar os pontos em um certo número de clusters , tal que
* as distâncias internas (dentro do cluster) devem ser pequenas, ou seja, os membros dos clusters são próximos/semelhantes entre si.
* as distâncias externas devem ser grandes, ou seja, os membros de diferentes clusters são diferentes.
Os objetivos do agrupamento

O objetivo do clustering é determinar o agrupamento interno em um conjunto de dados não rotulados. Mas como decidir o que constitui um bom agrupamento? Pode-se mostrar que não existe um critério absoluto de "melhor" que seja independente do objetivo final do agrupamento.Consequentemente, é o usuário que deve fornecer esse critério, de forma que o resultado da clusterização atenda às suas necessidades.
Na imagem acima, como sabemos qual é a melhor solução de clustering?

Para encontrar uma solução de clusterização específica, precisamos definir as medidas de similaridade para os clusters.
Medidas de proximidade

Para clustering, precisamos definir uma medida de proximidade para dois pontos de dados. Proximidade aqui significa quão semelhantes/dissimilares as amostras são em relação umas às outras.
* Medida de similaridade S(Xj,xk): grande se Xj,xk são semelhantes

* Medida de dissimilaridade (ou distância) D(xi,xk): pequena se Xi,xk são semelhantes large d, small s large s, small d
Existem várias medidas de similaridade que podem ser usadas.

* Vetores: Distância do Cosseno

* Conjuntos: Distância Jaccard

J(A,B) = |.4nz?| |4nB|

|.4uB| " |.4| + |B| - |.4n B\'

(lf A and B are both empty, we define J(A.B) = 1.)

0 < J(A.B) < 1.

* Pontos: Distância Euclidiana ... q=2

d(x,x') =

Uma "boa" medida de proximidade depende MUITO da aplicação. Os clusters devem ser invariantes sob as transformações "naturais" do problema. Além disso, durante o agrupamento, não é aconselhável normalizar os dados extraídos de várias distribuições.
Algoritmos de agrupamento

Os algoritmos de agrupamento podem ser classificados conforme listado abaixo:
Agrupamento exclusivo

Sobreposição de clusters
Agrupamento hierárquico
Agrupamento probabilístico

No primeiro caso, os dados são agrupados de forma exclusiva, de modo que, se um determinado ponto de dados pertence a um determinado cluster, ele não pode ser incluído em outro cluster. Um exemplo simples disso é mostrado na figura abaixo, onde a separação dos pontos é feita por uma linha reta em um plano bidimensional.
Ao contrário, o segundo tipo, o agrupamento sobreposto, utiliza conjuntos difusos para agrupar dados, de modo que cada ponto pode pertencer a dois ou mais agrupamentos com diferentes graus de pertinência. Nesse caso, os dados serão associados a um valor apropriado.
Um algoritmo de agrupamento hierárquico é baseado na união entre os dois agrupamentos mais próximos. A condição inicial é realizada definindo cada ponto de dados como um cluster. Após algumas iterações, ele atinge os clusters finais desejados.
Finalmente, o último tipo de agrupamento usa uma abordagem completamente probabilística.
Vamos falar sobre quatro dos algoritmos de clustering mais usados:

* K-médias

* Fuzzy K-means

* Agrupamento hierárquico

* Mistura de Gaussianos

Cada um desses algoritmos pertence a um dos tipos de agrupamento listados acima.
Enquanto, K-
means é um algoritmo de agrupamento exclusivo, Fuzzy K-means é um algoritmo de agrupamento sobreposto, agrupamento hierárquico é óbvio e, por último, Mixture of Gaussians é um algoritmo de agrupamento probabilístico . Discutiremos sobre cada método de agrupamento nas próximas seções.
AGRUPAMENTo K-MEANS

K-means é um dos algoritmos de aprendizado não supervisionado mais simples que resolve o conhecido problema de agrupamento. O procedimento segue uma maneira simples e fácil de classificar um dado conjunto de dados através de um certo número de clusters (suponha k clusters)fixados a priori. A ideia principal é definir k centros, um para cada cluster. Esses centróides devem ser colocados de forma inteligente, pois a localização diferente causa resultados diferentes.Então, a melhor escolha é colocá-los o mais longe possível um do outro.
O próximo passo é pegar cada ponto pertencente a um dado conjunto de dados e associá-lo ao centróide mais próximo. Quando nenhum ponto está pendente, a primeira etapa é concluída. Neste ponto, precisamos recalcular k novos centróides como baricentros (média) dos clusters resultantes da etapa anterior. Depois de termos esses k novos centróides, vamos, mais uma vez,associar os pontos aos centroóides mais próximos. Perceba que entramos em um loop. Como resultado desse loop, podemos notar que os k centróides mudam sua localização passo a passo até que não haja mais mudanças. Em outras palavras, os centróides não se movem mais.
Por fim, este algoritmo visa minimizar uma função objetivo, neste caso uma função de erro ao quadrado. A função objetivo é
Onde

J-l i-1

é uma medida de distância escolhida entre um ponto de dados xi e o centro de cluster q, é um indicador da distância dos n pontos de dados de seus respectivos centros de cluster.De forma mais estruturada, podemos dizer que o algoritmo é composto pelos seguintes passos:
* Seja X = {x^,x3,... ,xn} o conjunto de pontos de dados e V- {v1,v2, ,vc} o conjunto de centros.
* Selecione aleatoriamente os centros de cluster 'c' (centróides).

* Calcule a distância entre cada ponto de dados e centros de cluster.

* Atribua o ponto de dados ao centro do cluster cuja distância do centro do clusterseja a mínima de todos os centros do cluster.
* Recalcule o novo centro de cluster usando:

onde, 'Cj' representa o número de pontos de dados no Q cluster.

* Recalcule a distância entre cada ponto de dados e os novos centros de cluster obtidos.

* Se nenhum ponto de dados foi reatribuído, pare, caso contrário, repita a partir da etapa 3).

Embora possa ser provado que o procedimento sempre terminará, o algoritmo k-means não necessariamente encontra a melhor configuração, correspondente ao mínimo da função objetivo global.O algoritmo também é significativamente sensível aos centróides iniciais de cluster selecionados aleatoriamente. O algoritmo k-means pode ser executado várias vezes para reduzir esse efeito.
K-means é um algoritmo simples que foi adaptado para muitos domínios de problemas. Como veremos, é um bom candidato para trabalhar com a extensão de vetores de características difusas.
O procedimento k-means pode ser visto como um algoritmo guloso para particionar as n amostras em k clusters de modo a minimizar a soma das distâncias quadradas aos centros dos clusters. Tem alguns pontos fracos:
* A maneira de inicializar os centróides não foi especificada. Uma maneira popular de começar é escolher aleatoriamente k das amostras.
* Pode acontecer que o conjunto de amostras mais próximo de um centróide m,
esteja vazio,
de modo que m, não possa ser atualizado. Este é um problema que precisa ser tratado durante a implementação, mas geralmente é ignorado.
* Os resultados dependem do valor de k e não existe uma maneira ótima de descrever um melhor "k".
Este último problema é particularmente problemático, pois muitas vezes não temos como saber quantos clusters existem. No exemplo mostrado acima, o mesmo algoritmo aplicado aos mesmos dados produz o seguinte agrupamento de 3 médias. É melhor ou pior do que o agrupamento de 2médias?

Infelizmente, não existe uma solução teórica geral para encontrar o número ótimo de clusters para qualquer conjunto de dados. Uma abordagem simples é comparar os resultados de várias execuções com diferentes k classes e escolher a melhor de acordo com um determinado critério, mas precisamos ter cuidado porque aumentar k resulta em valores de função de erro menores por definição, mas também aumenta o risco de sobreajuste.
FUZZY K-MEANS

No agrupamento fuzzy, cada ponto tem uma probabilidade de pertencer a cada cluster, ao invés de pertencer completamente a apenas um cluster, como é o caso do k-means tradicional.Fuzzy k-
means especificamente tenta lidar com o problema em que os pontos estão equidistantes de dois centróides ou de outra forma ambíguos, substituindo a distância por probabilidade.
Fuzzy k-means usa um centroide ponderado com base nessas probabilidades. Os processos de inicialização, iteração e finalização são os mesmos usados no k-means. Os clusters resultantes são melhor analisados como distribuições probabilísticas em vez de uma atribuição rígida de rótulos.
O algoritmo fuzzy k-means é o seguinte:

* Suponha um número fixo de clusters K.

* Inicialização: Inicialize aleatoriamente as k-médias associadas aos clusters e calcule a probabilidade de que cada ponto de dados Xi seja membro de um determinado cluster K,P(PontoXiPossuiRotuloKIXi, K).

* Iteração: Recalcule o centróide do cluster como o centróide ponderado, dadas as probabilidades de pertinência de todos os pontos de dados Xi:
Xi X P(nk(\xi)b«I* )6

* Término : Iterar até a convergência ou até que um número de iterações especificado pelo usuário seja alcançado (a iteração pode ficar presa em alguns máximos ou mínimos locais)
Para uma melhor compreensão, podemos considerar este simples exemplo monodimensional. Dado um determinado conjunto de dados, suponha que o represente como distribuído em um eixo. Afigura abaixo mostra isso:

* * ****** * * *-* ***** * * * * ► x

Olhando para a imagem, podemos identificar dois clusters nas proximidades das duas concentrações de dados. Vamos nos referir a eles usando 'A' e 'B'. Na primeira abordagem mostrada—o algoritmo k-means — associamos cada ponto de dados a um centroide específico; portanto, esta função de pertinência ficaria assim:
Na abordagem Fuzzy k-means, em vez disso, o mesmo ponto de dados não pertence exclusivamente a um cluster bem definido, mas pode ser colocado em um caminho intermediário. Nesse caso, a função de pertinência segue uma linha mais suave para indicar que cada ponto de dados pode pertencer a vários clusters com diferentes graus de pertinência.
Na figura acima, o ponto de dados mostrado como um ponto marcado em vermelho pertence mais ao cluster B do que ao cluster A. O valor 0,2 de 'm' indica o grau de pertinência a A para tal ponto de dados.
AGRUPAMENTo HIERÁRQUICo.

Dado um conjunto de N itens a serem agrupados e uma matriz de distância N*N (ou similaridade), o processo básico de agrupamento hierárquico é este:
* Comece atribuindo cada item a um cluster, de modo que, se você tiver N itens,
agora terá N
clusters, cada um contendo apenas um item. Sejam as distâncias (semelhanças) entre os clusters iguais às distâncias (semelhanças) entre os itens que eles contêm.
* Encontre o par de clusters mais próximo (mais semelhante) e mescle-os em um único cluster,para que agora você tenha um cluster a menos.

* Calcular distâncias (semelhanças) entre o novo cluster e cada um dos clusters antigos.

* Repita as etapas 2 e 3 até que todos os itens estejam agrupados em um único cluster de tamanho N.
A figura abaixo mostra a sequência de passos do algoritmo na prática para um conjunto de 6 itens de dados. Logo abaixo um gráfico bastante conhecido denominado dendrograma.
MISTURA DE GAUSSIANAS.

Há outra maneira de lidar com problemas de clustering: uma abordagem baseada em modelo, que consiste em usar determinados modelos para clusters e tentar otimizar o ajuste entre os dados e o modelo.
Na prática, cada cluster pode ser representado matematicamente por uma distribuição paramétrica,como uma gaussiana. Todo o conjunto de dados é, portanto, modelado por uma mistura dessas distribuições.
Um modelo de mistura com alta probabilidade tende a ter as seguintes características:

* as distribuições de componentes têm altos "picos" (os dados em um cluster são apertados);

* o modelo de mistura "cobre" bem os dados (os padrões dominantes nos dados são capturados por distribuições de componentes).
Principais vantagens do clustering baseado em modelo:

* técnicas de inferência estatística bem estudadas disponíveis;

* flexibilidade na escolha da distribuição dos componentes;

* obter uma estimativa de densidade para cada cluster;

* uma classificação "soft" está disponível.

Mistura de Gaussianas

Vamos supor que temos um conjunto de dados que se parece com a figura abaixo:

o o
O o o o o
O O n

°o o o
Nosso trabalho é encontrar conjuntos de pontos que aparecem próximos uns dos outros.
Neste caso, podemos identificar claramente dois grupos de pontos que coloriremos de azul e vermelho,respectivamente:

Observe que agora estamos introduzindo algumas notações adicionais. Aqui, pl e p2 são os centróides de cada cluster e são parâmetros que identificam cada um deles.Um algoritmo de agrupamento popular é conhecido como K-means, que seguirá uma abordagem iterativa para atualizar os parâmetros de cada agrupamento. Mais especificamente, o que ele fará é calcular as médias (ou centróides) de cada cluster e, em seguida, calcular sua distância para cada um dos pontos de dados. Os últimos são então rotulados como parte do cluster que é identificado pelo centróide mais próximo. Esse processo é repetido até que algum critério de convergência seja atendido, por exemplo, quando não vemos mais mudanças nas atribuições dos clusters.
Uma característica importante do K-means é que ele é um método de agrupamento rígido,
o que significa que ele associará cada ponto a um e apenas um agrupamento. Uma limitação dessa abordagem é que não há medida de incerteza ou probabilidade que nos diga quanto um ponto de dados está associado a um cluster específico. Então, que tal usar um agrupamento flexível em vez de um agrupamento rígido? Isso é exatamente o que os Modelos de MisturaGaussianas, ou simplesmente GMMs, tentam fazer. Vamos agora discutir mais este método.
Definições

Uma Mistura Gaussiana é uma função composta por várias Gaussianas, cada uma identificada por kG {1,..., K}, onde Ké o número de clusters do nosso conjunto de dados. Cada Gaussiana k na mistura é composto pelos seguintes parâmetros:
* Uma média p que define seu centro.

* Uma covariância Z que define sua largura. Isso seria equivalente às dimensões de um elipsoide em um cenário multivariado.
* Uma probabilidade de mistura n que define quão grande ou pequena será a função gaussiana.

Vamos agora ilustrar esses parâmetros graficamente:

Cluster 2

Aqui, podemos ver que existem três funções gaussianas, portanto K=3. Cada gaussiana explica os dados contidos em cada um dos três clusters disponíveis. Os coeficientes de mistura são probabilidades e devem atender a esta condição:
527rk = 1 (!)

fc=l

Agora, como determinamos os valores ideais para esses parâmetros? Para conseguir isso,
devemos garantir que cada gaussiana se ajuste aos pontos de dados pertencentes a cada cluster.Isso é exatamente o que a probabilidade máxima faz. Em geral, a função densidade gaussiana é dada por:
*V(XIM,S) = (27r)D/12|S|i/2exP (-|íx - - g)

Onde x representa nossos pontos de dados, D é o número de dimensões de cada ponto de dados, p e 1 são a média e a covariância, respectivamente. Se tivermos um conjunto de dados composto porN = 1000 pontos tridimensionais (D = 3), então x será uma matriz 1000 x 3. p será um vetor 1 x 3 eZ será uma matriz 3x3. Para fins posteriores, também acharemos útil tomar o logaritmo dessa equação, que é dado por:
ln JV(x|g, S) = - y ln 2?r - ± ln E - | (x - (x - g)

Se diferenciarmos esta equação em relação à média e covariância e depois igualarmos a zero,poderemos encontrar os valores ótimos para esses parâmetros, e as soluções corresponderão àsEstimativas de Máxima Verossimilhança para essa configuração. No entanto, como estamos lidando não apenas com uma, mas com muitas gaussianas, as coisas ficarão um pouco complicadas quando chegar a hora de encontrarmos os parâmetros para toda a mistura. Nesse sentido,precisaremos introduzir alguns aspectos adicionais que discutiremos na próxima seção.
Derivações iniciais

Vamos agora introduzir algumas notações adicionais. Apenas uma palavra de advertência. Amatemática está chegando! Não se preocupe. Tentarei manter a notação o mais limpa possível para melhor compreensão das derivações. Primeiro, vamos supor que queremos saber qual é a probabilidade de que um ponto de dados xn venha da gaussiana k. Podemos expressar isso como:
Que se lê "dado um ponto de dados x, qual é a probabilidade de ter vindo da
Gaussiana k?" Nesse caso,z é uma variável latente que recebe apenas dois valores possíveis. É um quando x veio daGaussiana k, e zero caso contrário. Na verdade, não conseguimos ver essa variável z na realidade,mas conhecer sua probabilidade de ocorrência será útil para nos ajudar a determinar os parâmetros da mistura gaussiana, como discutiremos mais adiante.
Da mesma forma, podemos afirmar o seguinte:

O que significa que a probabilidade geral de se observar um ponto que vem da
Gaussiana k é na verdade equivalente ao coeficiente de mistura para aquela Gaussiana. Isso faz sentido, porque quanto maior for a Gaussiana, maior será essa probabilidade. Agora seja z o conjunto de todas as possíveis variáveis latentes z, portanto:
Sabemos de antemão que cada z ocorre independentemente dos outros e que eles só podem assumir o valor de um quando k é igual ao cluster de onde vem o ponto. Portanto:
p(z)=p(~i=í)zip(z2=í)z2—p(^k=i)zk=H"**

K

k=i

Agora, que tal encontrar a probabilidade de observar nossos dados, dado que eles vieram da gaussiana k ? Acontece que na verdade é a própria função gaussiana! Seguindo a mesma lógica que usamos para definir p(z), podemos afirmar:
p(xn|z) =

K

fc=l

Ok, agora você pode estar se perguntando, por que estamos fazendo tudo isso? Lembre-se que nosso objetivo inicial era determinar qual a probabilidade de z dada nossa observação x? Bem,acontece que as equações que acabamos de derivar, juntamente com a regra de Bayes, nos ajudarão a determinar essa probabilidade. Pela regra do produto de probabilidades, sabemos que p(xn,z) = p(xn|z)p(z)
Hmm, parece que agora estamos chegando a algum lugar. Os operandos à direita são o que acabamos de encontrar. Talvez alguns de vocês estejam antecipando que vamos usar a regra deBayes para obter a probabilidade de que eventualmente precisamos. No entanto,
primeiro precisaremos de p(xn), não de p(xn, z). Então, como nos livramos de z aqui? Sim,você acertou.

Marginalização! Só precisamos somar os termos em z, portanto

K K

pM = ^p(xn|z)p(z) = ^TTfcjVjXnlp*.,!:*.)

fc=l k=l

Esta é a equação que define uma Mistura Gaussiana, e você pode ver claramente que ela depende de todos os parâmetros que mencionamos anteriormente! Para determinar os valores ótimos para estes, precisamos determinar a máxima verossimilhança do modelo. Podemos encontrar a verossimilhança como a probabilidade conjunta de todas as observações x n , definida por:
TV TV K

p(x)=n =n 7TfcjV(xn|^fc, Sfc)

n=l n=lfc=l

Como fizemos para a função densidade gaussiana original, vamos aplicar o logaritmo a cada lado da equação:
TV K

lnp(X) = ElnE TTfeVjXnlpjt, Efc)

n=l k=l

Excelente! Agora, para encontrar os parâmetros ótimos para a mistura gaussiana,
tudo o que precisamos fazer é diferenciar essa equação em relação aos parâmetros e pronto, certo?Espera!
Não seja tão rápido. Temos um problema aqui. Podemos ver que há um logaritmo que está afetando a segunda soma. Calcular a derivada dessa expressão e depois resolver os parâmetros será muito difícil!
O que podemos fazer? Bem, precisamos usar um método iterativo para estimar os parâmetros. Mas primeiro, lembre-se de que deveríamos encontrar a probabilidade de z dado x ? Bem,vamos fazer isso, pois neste momento já temos tudo para definir como será essa probabilidade.
Pela regra de Bayes, sabemos que p(zk
- l|x„) = p(xn|zfc = l)p(zfe = 1)
EjÂ=lP(Xn|^ = = 1)

De nossas derivações anteriores, aprendemos que:

p(zk = 1) = 7Tfc, p(x„|cfc = 1) = jV(xn|^fc,Sfc)

Então, vamos agora substituí-los na equação anterior:

fl~fc-A/~(xn|pfc, Sfc)

E é isso que estamos procurando! Resumindo um modelo de mistura é uma mistura de k distribuições de componentes que coletivamente fazem uma distribuição de mistura/( x):
A'

/(*) = 52 a* AM
4=1

O otk representa a contribuição do k-és/mo componente na construção de f(x).
Na prática, a distribuição paramétrica (por exemplo, gaussianas) é frequentemente usada, pois muito trabalho foi feito para entender seu comportamento. Se você substituir cada/U*) por um gaussiano,obterá o que é conhecido como modelos de mistura gaussiana (GMM).
O algoritmo EM

Expectativa-Maximização assume que seus dados são compostos de múltiplas distribuições normais multivariadas (observe que esta é uma suposição muito forte, em particular quando você fixa o número de clustersl). Alternativamente, EM é um algoritmo para maximizar uma função de verossimilhança quando algumas das variáveis em seu modelo não são observadas (ou seja,quando você tem variáveis latentes).
Você pode perguntar, se estamos apenas tentando maximizar uma função, por que não usamos o maquinário existente para maximizar uma função. Bem, se você tentar maximizar isso tomando derivadas e definindo-as como zero, descobrirá que, em muitos casos, as condições de primeira ordem não têm solução. Há um problema do ovo e da galinha em que, para resolver os parâmetros do seu modelo, você precisa conhecer a distribuição de seus dados não observados; mas a distribuição de seus dados não observados é uma função dos parâmetros do seu modelo.
Expectativa-Maximização tenta contornar isso adivinhando iterativamente uma distribuição para os dados não observados, então estimando os parâmetros do modelo maximizando algo que é um limite inferior na função de verossimilhança real e repetindo até a convergência:
O algoritmo de maximização de expectativa

* Comece com uma estimativa para os valores dos parâmetros do seu modelo

* Etapa E: Para cada ponto de dados que possui valores ausentes, use sua equação de modelo para resolver a distribuição dos dados ausentes, considerando sua estimativa atual dos parâmetros do modelo e dados observados (observe que você está resolvendo uma distribuição para cada valor, não para o valor esperado). Agora que temos uma distribuição para cada valor ausente, podemos calcular a expectativa da função de verossimilhança em relação às variáveis não observadas. Se nosso palpite para o parâmetro do modelo estiver correto, essa probabilidade esperada será a probabilidade real de nossos dados observados;se os parâmetros não estiverem corretos, será apenas um limite inferior.

* Etapa M: Agora que temos uma função de verossimilhança esperada sem variáveis não observadas, maximize a função como faria no caso totalmente observado, para obter uma nova estimativa dos parâmetros do seu modelo.
* Repita até a convergência.

PRoBLEMAS ASSoCIADoS E APLICAçõES PoSSÍVEIS Ao AGRUPAMENTo

Há uma série de problemas com clustering. Entre eles:

* Lidar com muitas dimensões e um grande número de itens de dados pode ser problemático devido à complexidade do tempo;
* A eficácia do método depende da definição de "distância" (para agrupamento baseado em distância). Se não existe uma medida de distância óbvia devemos "defini-la", o que nem sempre é fácil, principalmente em espaços multidimensionais;
* O resultado do algoritmo de agrupamento (que em muitos casos pode ser arbitrário) pode ser interpretado de diferentes maneiras.
Aplicações possíveis

Os algoritmos de agrupamento podem ser aplicados em muitos campos, por exemplo:

* Marketing : encontrar grupos de clientes com comportamento semelhante, dado um grande banco de dados de clientes contendo suas propriedades e registros de compras anteriores;
* Biologia : classificação de plantas e animais em função de suas características;

* Seguros : identificação de grupos de segurados de automóveis com um custo médio de sinistro elevado; identificação de fraudes;
* Estudos de terremotos : agrupamento de epicentros de terremotos observados para identificar zonas perigosas;
* World Wide Web : classificação de documentos; agrupar dados de weblog para descobrir grupos de padrões de acesso semelhantes.
REGRAS DE ASSoCIAçÃo

As regras de associação são um dos conceitos muito importantes de aprendizado de máquina usados na análise de cestas de compras. Em uma loja, todos os vegetais são colocados no mesmo corredor,todos os laticínios são colocados juntos e os cosméticos formam outro conjunto desses grupos.Investir tempo e recursos em colocações deliberadas de produtos como essa não apenas reduz o tempo de compra de um cliente, mas também lembra ao cliente quais itens relevantes ele pode estar interessado em comprar, ajudando as lojas a fazer vendas cruzadas no processo.As regras de associação ajudam a descobrir todas essas relações entre itens de bancos de dados enormes. Uma coisa importante a notar é-
As regras não extraem a preferência de um indivíduo, mas encontram relações entre o conjunto de elementos de cada transação distinta. É isso que os diferencia da filtragem colaborativa.
Para elaborar essa ideia — as regras não vinculam as diferentes transações de um usuário ao longo do tempo para identificar relacionamentos. Ao invés disto, uma lista de itens com IDs de transação exclusivos (de todos os usuários) são estudadas como um grupo. Isso é útil na colocação de produtos nos corredores. Por outro lado, a filtragem colaborativa vincula todas as transações correspondentes a um ID de usuário para identificar a semelhança entre as preferências dos usuários.Isso é útil para recomendar itens em sites de comércio eletrônico, recomendar músicas no spotify, etc.
Vamos agora ver como é exatamente uma regra de associação. Consiste em um antecedente(também chamado de lado da mão esquerda) e um consequente (ou lado da mão direita),
ambos sendo uma lista de itens. Observe que a implicação aqui é co-ocorrência e não causalidade. Para uma determinada regra, o conjunto de itens (itemset) é a lista de todos os itens no antecedente e no consequente.
{Bread, Egg)

Antecedent

{Milk}

Consequent

Itemset = {Bread, Egg, Milk}

Várias métricas podem ser usadas para nos ajudar a entender a força da associação entre o antecedente e o consequente. Vamos passar por elas.
1. Suporte

Esta medida dá uma ideia de quão frequente é um conjunto de itens em todas as transações.Considere itemsetl = {pão} e itemset2 = {shampoo}. Haverá muito mais transações contendo pão do que aquelas contendo xampu. Então, como você adivinhou, itemsetl geralmente terá um suporte maior que o itemset2. Agora considere itemsetl = {pãoa, manteiga} e itemset2 = {pão,shampoo}.
Muitas transações terão pão e manteiga no carrinho, mas e pão e xampu? Não muito.
Portanto,
neste caso, o itemsetl geralmente terá um suporte maior que o itemset2.
Matematicamente,
suporte é a fração do número total de transações em que o conjunto de itens ocorre.

Transações que possuem X eY

Suporte (X -> Yj =

Total de transações

O valor do suporte nos ajuda a identificar as regras que valem a pena considerar para análise posterior. Por exemplo, pode-se querer considerar apenas os conjuntos de itens que ocorrem pelo menos 50 vezes de um total de 10.000 transações, ou seja, suporte = 0,005. Se um conjunto de itens tiver um suporte muito baixo, não temos informações suficientes sobre o relacionamento entre seus itens e, portanto, nenhuma conclusão pode ser tirada de tal regra.
2. Confiança

Esta medida define a probabilidade de ocorrência de consequentes no carrinho dado que o carrinho já possui os antecedentes. Isso é para responder à pergunta - de todas as transações contendo,digamos, {sucrilhos}, quantas também tinham {leite} nelas? Podemos dizer por conhecimento comum que {sucrilhos} -> {leite} deve ser uma regra de alta confiança. Tecnicamente,confiança é a probabilidade condicional de ocorrência do consequente dado o antecedente.
Transações contendo X eY
ConfiançaçX Y) = - -— -

Transações contendo apenas X

Vamos considerar mais alguns exemplos antes de prosseguir. Qual você acha que seria a confiança para {Manteiga} -> {Pão}? Ou seja, que fração das transações com manteiga também teve pão?Muito alto, ou seja, um valor próximo a 1? Está certo. E quanto a
{Iogurte} -> {Leite}? Alta novamente. {Escova de dentes} -> {Leite}? Não tão certo? A confiança para esta regra também será alta, pois {Leite} é um conjunto de itens tão frequente e estaria presente em todas as outras transações.
Não importa o que você tem no antecedente para um consequente tão frequente. A confiança para uma regra de associação com um consequente muito frequente será sempre alta.
Vou introduzir alguns números aqui para esclarecer isso ainda mais.

Milk ÈToothbrush

70 4

Total de transações - 100. 10 delas têm leite e escova de dentes, 70 têm leite mas não têm escova de dentes e 4 têm escova de dentes mas não têm leite.
Considere os números da figura à esquerda. Confiança para {Parta de dente} -> {Leite} será
10/(10+4)

= 0,7

Parece um valor de confiança alto. Mas sabemos intuitivamente que esses dois produtos têm uma associação fraca e há algo enganoso nesse alto valor de confiança. O elevador ou lift é introduzido para superar este desafio.
Considerar apenas o valor da confiança limita nossa capacidade de fazer qualquer inferência de negócios.
3 . Lift

Levante os controles para o suporte (frequência) do consequente enquanto calcula a probabilidade condicional de ocorrência de {Y} dado {X}. Lift é um termo muito literal dado a esta medida. Pense nisso como o *elevador* que {X} fornece à nossa confiança por termos {Y}no carrinho. Para reformular, lift é o aumento na probabilidade de ter {Y} no carrinho com o conhecimento de {X} estar presente sobre a probabilidade de ter {Y} no carrinho sem qualquer conhecimento sobre a presença de {X}. Matematicamente,
Lift (X y) =

Transações contendedo X e Y
Transações contendo X

Fração das transações que contem Y

Nos casos em que {X} realmente leva a {Y} no carrinho, o valor da sustentação será maior que 1.Vamos entender isso com um exemplo que será continuação da regra {Pasta de dente} {Leite}.

Probabilidade de ter leite no carrinho sabendo que a escova de dentes está presente (ou seja, confiança ): 10/(10+4) = 0,7
Agora, para colocar esse número em perspectiva, considere a probabilidade de ter leite no carrinho sem nenhum conhecimento sobre escova de dentes: 80/100 = 0,8
Esses números mostram que ter escova de dentes no carrinho realmente reduz a probabilidade de ter leite no carrinho de 0,8 para 0,7! Agora temos um resultado mais parecido com a realidade. Um valor de sustentação menor que 1 mostra que ter escova de dentes no carrinho não aumenta as chances de ocorrência de leite no carrinho apesar da regra apresentar um alto valor de confiança.Um valor de lift maior que 1 atesta alta associação entre {Y} e {X}. Quanto maior o valor do lift,maiores são as chances de compra de {Y} caso o cliente já tenha comprado {X}. Lift é a medida que ajudará os gerentes de loja a decidir a colocação de produtos no corredor mesmo corredor.
Mineração de regras de associação

Agora que entendemos como quantificar a importância da associação de produtos dentro de um conjunto de itens, o próximo passo é gerar regras de toda a lista de itens e identificar os mais importantes. Isso não é tão simples quanto pode parecer. Supermercados terão milhares de produtos diferentes na loja. Após alguns cálculos simples, pode-se mostrar que apenas10 produtos levarão a 57.000 regras!! E esse número aumenta exponencialmente com o aumento do número de itens. Encontrar valores de lift para cada um deles será computacionalmente muito caro.Como lidar com este problema? Como chegar a um conjunto de regras de associação mais importantes a serem consideradas? O algoritmo a priori vem em nosso socorro!
1. Gerando conjuntos de itens de uma lista de itens

O primeiro passo na geração de regras de associação é obter todos os conjuntos de itens frequentes nos quais partições binárias podem ser executadas para obter o antecedente e o consequente. Por exemplo, se houver 6 itens {Pão, Manteiga, Ovo, Leite, Caderno, Escova de Dentes} em todas as transações combinadas, os conjuntos de itens serão parecidos com {Pão},{Manteiga}, {Pão,
Caderno}, {Leite, Escova de Dentes}, {Leite, Ovo, Legumes} etc. O tamanho de um conjunto de itens pode variar de um até o número total de itens que temos. Agora, buscamos apenas conjuntos de itens frequentes e não todos para verificar o número total de conjuntos de itens gerados.
Os conjuntos de itens frequentes são aqueles que ocorrem pelo menos um número mínimo de vezes nas transações. Tecnicamente, esses são os conjuntos de itens para os quais o valor de suporte (fração de transações contendo o conjunto de itens) está acima de um limite mínimo
— minsup .

Portanto, {Pão, Notebook} pode não ser um conjunto de itens frequente se ocorrer apenas 2 vezes em 100 transações e (2/100) = 0,02 ficar abaixo do valor de minsup.
Uma abordagem de força bruta para encontrar conjuntos de itens frequentes é formar todos os conjuntos de itens possíveis e verificar o valor de suporte de cada um deles. Oprincípio a priori ajuda a tornar essa busca eficiente. Diz que
Todos os subconjuntos de um conjunto de itens frequentes também devem ser frequentes.

Isso equivale a dizer que o número de transações contendo os itens {Pão, Ovo} é maior ou igual ao número de transações contendo {Pão, Ovo, Legumes}. Se o último ocorrer em 30transações, o primeiro está ocorrendo em todas as 30 e possivelmente ocorrerá em até mais transações. Portanto,se o valor de suporte de {Pão, Ovo, Legumes}, ou seja, (30/100) = 0,3 estiver acima de minsup,podemos ter certeza de que o valor de suporte de {Pão, Ovo}, ou seja, - >0,3 está acima minup também. Isso é chamado de propriedade antimonotonicidade do suporte, onde se retirarmos um item de um conjunto de itens, o valor de suporte do novo conjunto de itens gerado será o mesmo ou aumentará.
O princípio a priori é resultado da propriedade antimonótona do suporte.

O princípio a priori nos permite podar todos os superconjuntos de um conjunto de itens que não satisfaça a condição de limite mínimo para suporte. Por exemplo, se {Milk, Notebook}não satisfizer nosso limite de minsup, um conjunto de itens com qualquer item adicionado a esses nunca alcançará o limite também.
Essa metodologia é chamada de algoritmo a priori. As etapas envolvidas são:

Gere todos os conjuntos de itens frequentes (suporte > minsup) com apenas um item. Em seguida,gere conjuntos de itens de comprimento 2 como todas as combinações possíveis dos conjuntos de itens acima. Em seguida, podar aqueles para os quais o valor de suporte caiu abaixo de minsup.
Agora gere conjuntos de itens de comprimento 3 como todas as combinações possíveis de conjuntos de itens de comprimento 2 (que permaneceram após a poda) e execute a mesma verificação no valor de suporte.
Continuamos aumentando o comprimento dos conjuntos de itens em um e verificamos o limite em cada etapa.
Como pode ser visto no gráfico, a poda de conjuntos de itens infrequentes reduz o número de conjuntos de itens a serem considerados em mais da metade! Essa proporção de redução no poder computacional torna-se cada vez mais significativa à medida que o número de itens aumenta.
Essa proporção também depende do limite mínimo de suporte (minsup) que captamos, que é completamente subjetivo ao problema em questão e pode ser baseado em experiências anteriores.
2. Gerando todas as regras possíveis dos conjuntos de itens frequentes

Uma vez que os conjuntos de itens frequentes são gerados, identificar regras é comparativamente menos oneroso. As regras são formadas pela partição binária de cada conjunto de itens.Se {Pão,
Ovo, Leite, Manteiga} for o conjunto de itens frequente, as regras candidatas terão a seguinte aparência:
(Ovo, Leite, Manteiga Pão), (Pão, Leite, Manteiga Ovo), (Pão, Ovo Leite, Manteiga), (Ovo,
Leite -> Pão, Manteiga), (Manteiga -> Pão, Ovo, Leite)

A partir de uma lista de todas as regras candidatas possíveis, buscamos identificar regras que estejam acima de um nível mínimo de confiança (minconf). Assim como a propriedade antimonótona do suporte, a confiança das regras geradas a partir do mesmo conjunto de itens também segue uma propriedade antimonótona. É antimonótono em relação ao número de elementos em consequente.
Isso significa que a confiança de (A,B,C->D) > (B,C -> A,D) > (C -> A,B,D). Para lembrar, confiança para
{X -> Y} = suporte de {X,Y}/suporte de {X}

Como sabemos, o suporte de todas as regras geradas a partir de um mesmo conjunto de itens permanece o mesmo e a diferença ocorre apenas no cálculo do denominador de confiança. Àmedida que o número de itens em X diminui, o suporte(X) aumenta (como sugere da propriedade antimonótona do suporte) e, portanto, o valor de confiança diminui.
Vejamos uma explicação intuitiva para a ideia apresentada acima.
Considere F1 e F2:

F1 - fração de transações tendo (manteiga) também tendo (ovo, leite, pão)

#tem manteiga, ovo, leite e pão
#transações que tem manteiga

Haverá muitas transações com manteiga e todos os três de ovo, leite e pão poderão encontrar lugar apenas em um pequeno número deles.
F2 = fração de transações tendo (leite, manteiga, pão) também tendo (ovo)

#tem manteiga, ovo, leite e pão ütransações que tem leite, manteiga e pão
Haverá apenas algumas de transações com todos os três de leite, manteiga e pão (em comparação com apenas manteiga) e haverá grandes chances de ter ovo neles.
Assim será observado que F1 < F2. Usando essa propriedade de confiança, a poda é feita de maneira semelhante a feita ao procurar conjuntos de itens frequentes. Está ilustrado na figura abaixo.
Low-Confidence

Começamos com um itemset frequente {a,b,c,d} e começamos a formar regras com apenas um consequente. Remova as regras que não satisfazem a condição minconf. Agora, comece a formar regras usando uma combinação de consequentes das restantes. Continue repetindo até que reste apenas um item no antecedente. Este processo deve ser feito para todos os conjuntos de itens frequentes.
Aqui, novamente, o limite mínimo de confiança que pegamos é completamente subjetivo ao problema em questão.
Com essas duas etapas, identificamos um conjunto de regras de associação que satisfazem tanto a condição de suporte mínimo quanto a condição de confiança mínima. O número de regras obtidas irá variar com os valores de minsup e minconf. Agora, esse subconjunto de regras gerado pode ser pesquisado pelos valores mais altos de lift para tomar decisões de negócios.Existem algumas bibliotecas bem construídas em R para buscar regras de associação de transações colocando minsup e minconf como parâmetros. Elas também fornecem recursos para visualizar o mesmo.
Antes de concluir, eu introduziria mais dois termos, conjuntos de itens frequentes máximos e conjuntos de itens frequentes fechados, que são usados como uma representação compacta de todos os conjuntos de itens frequentes.
Conjunto de itens frequente máximo: É um conjunto de itens frequente para o qual nenhum dos superconjuntos imediatos é frequente. Isso é como um conjunto de itens Xfrequente ao qual nenhum item y pode ser adicionado, de modo que {X,y} ainda permaneça acima do limite minsup.
Frequent
Itemset kets havingbread and butteralso have e nd support of the basket with bread,butter and g is abovethe valueof minsup

At least one basket with bread and butter has something different from egg and support for that basket is above threshold
Closed
Frequent
Itemset

I II r

All baskets with one item added to bread and butter fali below the value of minsup
Casos diferentes para o conjunto de itens {Pão, Manteiga}

Conjunto de itens frequente fechado : É um conjunto de itens frequente para o qual não existe um superconjunto que tenha o mesmo suporte que o conjunto de itens
Conjuntos de itens frequentes máximos são valiosos porque são a forma mais compacta de representação de conjuntos de itens frequentes.
Todos os conjuntos de itens frequentes podem ser derivados como subconjuntos de conjuntos de itens frequentes máximos. No entanto, as informações sobre o suporte dos subconjuntos são perdidas. Se esse valor for necessário, o conjunto de itens frequentes fechado é outra maneira de representar todos os conjuntos de itens frequentes.
Conjuntos de itens fechados ajudam a remover alguns conjuntos de itens redundantes sem perder informações sobre os valores de suporte.
O cálculo de valores de suporte de conjuntos de itens não fechados de conjuntos de itens fechados dado por outro algoritmo, cujos detalhes estão fora do escopo desta aula.
Eu tentei cobrir todos os termos e conceitos importantes relacionados à mineração de regras de associação, entrando em detalhes sempre que necessário. A seguir estão resumos de uma linha para alguns termos introduzidos neste processo -
1. Mineração de regras de associação: (a) Geração de conjuntos de itens, (b) Geração de regras

2. Princípio a priori: Todos os subconjuntos de um conjunto de itens frequentes também devem ser frequentes
3. Algoritmo a priori: poda para obter com eficiência todos os conjuntos de itens frequentes

4. Conjunto de itens frequente máximo: nenhum dos superconjuntos imediatos é frequente

5. Conjunto de itens frequente fechado: nenhum dos superconjuntos imediatos tem o mesmo valor de suporte
THIAGO CAVALCANTI

PROFESSOR

