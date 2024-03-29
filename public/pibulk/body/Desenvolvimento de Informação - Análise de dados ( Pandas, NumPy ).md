# Desenvolvimento de Informação - Análise de dados ( Pandas, NumPy )

Índice

1) Pandas

PANDAS

pandas yit =/3'xit + /li + eit
Pandas é uma biblioteca Python de código aberto para análise de dados. Ele dá ao
Python a capacidade de trabalhar com dados semelhantes a planilhas para carregamento,manipulação,
alinhamento e fusão rápida de dados, entre outras funções. Para fornecer ao Python esses recursos aprimorados, o Pandas apresenta dois novos tipos de dados ao Python: Series e DataFrame.
O tipo DataFrame representa a planilha inteira ou os dados retangulares
(bidimensionais), enquanto o Series é uma única coluna do DataFrame. Um Pandas DataFrame também pode ser considerado um dicionário ou coleção de objetos Series.
Mas aí surge uma pergunta ... por que você deve usar uma linguagem de programação como Python e uma ferramenta como Pandas para trabalhar com dados? Tudo se resume a automação e reprodutibilidade. Se um determinado conjunto de análises precisa ser executado em vários conjuntos de dados, uma linguagem de programação tem a capacidade de automatizar a análise nesses conjuntos de dados. Embora muitos programas de planilhas tenham suas próprias linguagens de programação de macro, muitos usuários não as utilizam.
Além disso, nem todos os programas de planilhas estão disponíveis em todos os sistemas operacionais. A execução da análise de dados usando uma linguagem de programação força o usuário a manter um registro contínuo de todas as etapas executadas nos dados. Muitas pessoas não conseguem visualizar que dados em um programa de planilha não fazem mais sentido devido a dados incorretos. Isso não quer dizer que os programas de planilhas sejam ruins ou que não tenham seu lugar no fluxo de trabalho de dados, eles têm. Em vez disso, o nosso ponto é que existem ferramentas melhores e mais confiáveis por aí.
O Pandas é uma solução muito interessante para isso ... vamos aprender um pouco sobre isso. Mas antes gostaria que você soubesse que quando se trata de ciência de dados em Python,a biblioteca é praticamente onipresente. Ele é construído em cima da biblioteca NumPy, o que nos permite realizar operações matemáticas em matrizes de dados de tipo único com eficiência.
Carregando seu primeiro conjunto de dados

Quando recebemos um conjunto de dados, primeiro o carregamos e começamos a examinar sua estrutura e conteúdo. A maneira mais simples de olhar para um conjunto de dados é examinar e criar um subconjunto de linhas e colunas específicas. Podemos ver que tipo de informação está armazenado em cada coluna e podemos começar a procurar padrões agregando estatísticas descritivas.
Como o Pandas não faz parte da biblioteca padrão do Python, primeiro temos que dizer ao Python para carregar (import) a biblioteca.
import pandas

Com a biblioteca carregada, podemos usar a função read_csv para carregar um arquivo de dadosCSV. Para acessar a função read_csv do Pandas, usamos a notação de ponto. Vamos carregar o arquivo estratégia.csv.
df = pandas.read_csv/data/estretegia.csv', sep='\t')

Por padrão, a função read_csv lerá um arquivo separado por vírgulas, se nossa arquivos"estratégia.csv" estiver separado por tabulações podemos usar o parâmetros "sep" e o valor \t para indicar que o separador é uma tabulação. O código acima carrega o DataFrame (df) com os dados presentes no arquivo. Se quisermos mostrar as 5 primeiras linhas carregadas podemos usar a função head da seguinte forma:
#Isso é um comentário em Python

#Abaixo um exemplo de código que chama a função head print(df.head())
Ao trabalhar com as funções do Pandas, é prática comum fornecer pandas o apelido pd.
Portanto,
o código a seguir é equivalente ao exemplo anterior:

import pandas as pd

Podemos verificar se estamos trabalhando o DataFrame do pacote Pandas podemos usar a função type embutida (ou seja, vem diretamente do Python, não de qualquer pacote como o Pandas).
print(type(df))

#esse código acima vai imprimir

<class 'pandas.core.frame.DataFrame'>

A função type é útil quando você começa a trabalhar com muitos tipos diferentes de objetos Python e precisa saber em qual objeto está trabalhando no momento. O conjunto de dados que carregamos está atualmente salvo como um objeto DataFrame do Pandas e é relativamente pequeno. Cada objeto DataFrame tem um atributo shape que nos dará o número de linhas e colunas do DataFrame.
## a função pega o número de linhas e colunas do DataFrame print(df.shape)
(1704,6)

O atributo shape retorna uma tupla em que o primeiro valor é o número de linhas e o segundo número é o número de colunas. A partir dos resultados anteriores, vemos que nosso conjunto de dados Estratégia tem 1.704 linhas e 6 colunas. Como shape é um atributo do Dataframe e não uma função ou método, ele não tem parênteses após o ponto. Se você cometeu o erro de colocar parênteses após o atributo shape, ele retornaria um erro.
Visualização e inspeção de dados

Agora que já carregamos nosso primeiro conjunto de dados vamos olhar para algumas funções que podem ser úteis. Além do df.head() para apresentar as primeiras linhas de um data frame, podemos usar o df.tail() para apresentar as últimas linhas. Outra função interessante é o df.info() que exibe o índice o tipo de dados e as informações de memória.
Um comando muito útil é df.describe() insere estatísticas de resumo para colunas numéricas. Também é possível obter as seguintes estatísticas sobre todo o data frame ou série(uma coluna):
## Para retornar a média de todas as colunas:

df.mean()

## Para retornar a correlação entre colunas em um quadro de dados:
df.corr()

#Para retornar o número de valores não nulos em cada coluna do
#quadro de dados:

df.count ()

#Para retornar df.max()
#Para retornar df.min()
#Para retornar df.median()#Para retornar df.std()
o maior valor em cada coluna:

o menor valor em cada coluna:
a mediana de cada coluna:

o desvio padrão de cada coluna:

Seleção de Dados

Uma das coisas que é muito fácil de fazer no Pandas é selecionar os dados que você deseja em comparação com a seleção de um valor de uma lista. Você pode selecionar uma coluna(df[col]) e retornar a coluna com o rótulo "col" como uma Series (s) ou algumas colunas(df[[coll, col2]j) e retornar as colunas como um novo DataFrame. Você pode selecionar por posição(s.iloc[OJ) ou por índice (s.loc['index_one']). Para selecionar a primeira linha, você pode usar df.iloc[0,:]1 e para selecionar o primeiro elemento da primeira coluna que você executaria df.iloc[0,0]. Eles também podem ser usados em diferentes combinações, portanto, espero que dê uma ideia das diferentes seleções e indexações que você pode realizar no Pandas.
Filtrar, classificar e agrupar

Você pode usar diferentes condições para filtrar colunas. Por exemplo, df [df [yea r] > 1984]
forneceria apenas a coluna ano é maior que 1984. Você pode usar & (e) ou | (ou) para adicionar diferentes condições à sua filtragem. Isso também é chamado de filtragem booleana.
É possível classificar os valores em uma determinada coluna em ordem crescente usando:

df.sort_values(coll)

E em ordem decrescente usando:

1 Lembre-se que em Python o primeiro elemento é referenciado com o zero (0).

df.sort_values(col 2,ascending=False)

Além disso, é possível classificar os valores da coll em ordem crescente e depois da col2 em ordem decrescente usando:
df.sort_values([coll,col2],ascending=[True,False])

O último comando nesta seção é groupby. Envolve a divisão dos dados em grupos com base em alguns critérios, aplicando uma função a cada grupo independentemente e combinando os resultados em uma estrutura de dados. O código abaixo retorna um objeto agrupado para valores de uma coluna df.groupby(col)
Já o código a seguir, retorna um objeto agrupado para valores de várias colunas.

df.groupby([coll,col2])

Limpeza de Dados

A limpeza de dados é uma etapa muito importante na análise de dados. Por exemplo,
sempre verificamos se há valores ausentes nos dados executando o pd.isnull()que verifica os valores nulos e retorna uma matriz booleana (uma matriz de verdadeiro para valores ausentes e falso para valores não ausentes).
Para obter uma soma de valores nulos/ausentes, execute pd.isnull().sum().

pd.notnull() é o oposto de pd.isnull(). Depois de obter uma lista de valores ausentes,
você pode se livrar deles ou eliminá-los usando df.dropnaf) para eliminar as linhas ou df.dropna(axis=l) colunas.Uma abordagem diferente seria preencher os valores ausentes com outros valores usando o df.fillna(x) que preenche os valores ausentes com x (você pode colocar lá o que quiser) ou s.fillna(s.mean()) para substituir todos os valores nulos pela média (a média pode ser substituída por quase qualquer função da seção de estatísticas).
Às vezes, é necessário substituir os valores por valores diferentes. Por exemplo,
s.replacefl/one1)
substituiria todos os valores iguais a 1 por 'one'. É possível fazer isso para vários valores:s.replaceUl^LroneYthree1]) substituiria todos os 1 por 'one'e 3 por 'three'.
Você também pode renomear colunas específicas executando: df.rename(columns={'old_name': 'new_name'}).

Unir / Combinar

O último conjunto de comandos básicos do Pandas é para juntar ou combinar frames de dados ou linhas/colunas. Os três comandos são:
dfl.append(df2) - adiciona as linhas dfl ao final de df2 (as colunas devem ser idênticas)

df.concat([dfl, df2],axis=l) - adiciona as colunas dflao final de df2 (a quantidade linhas deve ser idênticas)
dfl.join(df2, on=coll, how='inner') - usa o padrão SQL para unir as colunas dflcom as colunas de df2 nas quais as linhas coll têm valores idênticos. O parâmetro "how" pode ser igual a um dos seguintes: 'left', 'right', 'outer','inner'
Estes são os comandos básicos do Pandas, mas espero que você possa ver como o Pandas pode ser poderoso para a análise de dados depois que for aprovado no concurso! Vamos em frente.
