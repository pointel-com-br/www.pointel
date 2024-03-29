# Análise de dados - NumPy

O NumPy (Numerical Python) é uma biblioteca de computação numérica em Python que fornece suporte para manipulação eficiente de arrays multidimensionais e funções matemáticas de alto desempenho. É uma das principais bibliotecas utilizadas para análise de dados e científica em Python.

Aqui estão algumas funcionalidades e conceitos-chave do NumPy relacionados à análise de dados:

1. Arrays NumPy: O NumPy introduz o objeto de array, que permite a criação de arrays multidimensionais. Os arrays NumPy são eficientes em termos de espaço e tempo de execução, além de oferecerem uma variedade de métodos e operações para manipulação e cálculos em arrays.

2. Operações em arrays: O NumPy fornece um conjunto abrangente de funções matemáticas que podem ser aplicadas a arrays completos ou a elementos individuais. Isso inclui operações aritméticas, funções trigonométricas, exponenciais, logarítmicas, entre outras.

3. Indexação e fatiamento: O NumPy oferece recursos avançados para acessar e manipular elementos de arrays usando indexação e fatiamento. É possível selecionar elementos específicos, extrair subconjuntos de arrays e realizar atribuições em massa.

4. Broadcasting: O broadcasting no NumPy é um recurso poderoso que permite realizar operações entre arrays de diferentes tamanhos, expandindo automaticamente as dimensões do array menor para corresponder ao array maior. Isso simplifica o código e evita a necessidade de escrever loops explícitos.

5. Funções estatísticas: O NumPy possui uma ampla gama de funções estatísticas integradas que podem ser aplicadas a arrays, como média, mediana, desvio padrão, máximo, mínimo, entre outras. Essas funções são úteis para a análise descritiva de dados.

6. Álgebra linear: O NumPy oferece suporte a operações de álgebra linear, como multiplicação de matrizes, decomposição de valores singulares, resolução de sistemas de equações lineares, cálculo de autovalores e autovetores, entre outros.

Além disso, o NumPy é frequentemente combinado com outras bibliotecas populares, como pandas (para manipulação de dados em formato tabular) e matplotlib (para visualização de dados), para realizar análises de dados mais avançadas em Python.

Para utilizar o NumPy, você precisa primeiro instalá-lo em seu ambiente Python. Você pode fazer isso usando o gerenciador de pacotes pip. Aqui está um exemplo de como instalar o NumPy:

```
pip install numpy
```

Depois de instalado, você pode importar o NumPy em seu código Python da seguinte forma:

```python
import numpy as np
```

A partir daí, você pode utilizar todas as funcionalidades e recursos do NumPy em sua análise de dados.

## Análise de dados - NumPy - Principais funções

O NumPy é uma biblioteca fundamental para análise de dados em Python, fornecendo suporte para arrays multidimensionais e uma ampla variedade de funções para manipulação e cálculos numéricos eficientes. Aqui estão algumas das principais funções do NumPy para análise de dados:

1. Criação de arrays:
- `numpy.array()`: Cria um array a partir de uma sequência de elementos.
- `numpy.zeros()`: Cria um array preenchido com zeros.
- `numpy.ones()`: Cria um array preenchido com uns.
- `numpy.arange()`: Cria um array com uma sequência de valores.
- `numpy.linspace()`: Cria um array com uma sequência de valores espaçados uniformemente.

2. Manipulação de arrays:
- `numpy.shape()`: Retorna a forma (dimensões) de um array.
- `numpy.reshape()`: Modifica a forma de um array.
- `numpy.concatenate()`: Concatena dois ou mais arrays ao longo de um eixo.
- `numpy.split()`: Divide um array em múltiplos subarrays.
- `numpy.transpose()`: Troca os eixos de um array.

3. Operações matemáticas:
- `numpy.mean()`: Calcula a média dos valores de um array.
- `numpy.sum()`: Calcula a soma dos valores de um array.
- `numpy.min()`: Retorna o valor mínimo de um array.
- `numpy.max()`: Retorna o valor máximo de um array.
- `numpy.std()`: Calcula o desvio padrão dos valores de um array.

4. Operações de álgebra linear:
- `numpy.dot()`: Calcula o produto escalar entre dois arrays.
- `numpy.linalg.inv()`: Calcula a matriz inversa de um array.
- `numpy.linalg.det()`: Calcula o determinante de uma matriz.
- `numpy.linalg.eig()`: Calcula os autovalores e autovetores de uma matriz.

5. Operações de estatística:
- `numpy.histogram()`: Calcula o histograma de um array.
- `numpy.percentile()`: Calcula o percentil de um array.
- `numpy.corrcoef()`: Calcula a matriz de correlação entre arrays.

Essas são apenas algumas das principais funções do NumPy para análise de dados. O NumPy oferece muitas outras funcionalidades, como operações de álgebra linear avançadas, geração de números aleatórios, manipulação de strings, entre outros. Você pode consultar a documentação oficial do NumPy para obter mais informações sobre todas as funções disponíveis e suas opções de uso.

## Análise de dados - NumPy - Exemplos de usos mais comuns

Claro! Aqui estão alguns exemplos de uso comuns do NumPy na análise de dados:

1. Criação de arrays: O NumPy permite criar arrays multidimensionais que são a base para muitas operações de análise de dados. Você pode criar arrays a partir de listas ou usar funções como `numpy.arange()` e `numpy.linspace()` para criar sequências de valores:

```python
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5]) # Cria um array a partir de uma lista
arr2 = np.arange(0, 10, 2) # Cria um array com valores de 0 a 10 (exclusivo) com um passo de 2
arr3 = np.linspace(0, 1, 5) # Cria um array com 5 valores igualmente espaçados entre 0 e 1
```

2. Operações numéricas: O NumPy oferece uma ampla gama de funções para realizar operações numéricas em arrays. Isso inclui operações aritméticas, funções trigonométricas, operações matriciais e muito mais:

```python
arr = np.array([1, 2, 3])

np.sum(arr) # Soma os valores do array
np.mean(arr) # Calcula a média dos valores do array
np.sin(arr) # Calcula o seno de cada valor do array
np.dot(arr, arr) # Calcula o produto escalar do array consigo mesmo
```

3. Indexação e slicing: O NumPy oferece uma sintaxe flexível para indexar e fatiar arrays, permitindo acessar e manipular subconjuntos de dados:

```python
arr = np.array([1, 2, 3, 4, 5])

arr[0] # Acessa o primeiro elemento do array
arr[2:4] # Retorna um novo array com os elementos das posições 2 e 3
arr[arr > 2] # Retorna um novo array com os elementos maiores que 2
```

4. Operações estatísticas: O NumPy possui funções estatísticas úteis para análise de dados, permitindo calcular estatísticas descritivas, como média, mediana, desvio padrão e correlação:

```python
arr = np.array([1, 2, 3, 4, 5])

np.mean(arr) # Calcula a média dos valores do array
np.median(arr) # Calcula a mediana dos valores do array
np.std(arr) # Calcula o desvio padrão dos valores do array
np.corrcoef(arr1, arr2) # Calcula a matriz de correlação entre dois arrays
```

5. Álgebra linear: O NumPy fornece funcionalidades para álgebra linear, como decomposição de matriz, inversão de matriz, resolução de sistemas de equações lineares e cálculo de autovalores e autovetores:

```python
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([5, 6])

np.linalg.inv(matrix) # Calcula a inversa da matriz
np.linalg.solve(matrix, vector) # Resolve o sistema de equações lineares
np.linalg.eig(matrix) # Calcula os autovalores e autovetores da matriz
```

Esses são apenas alguns exemplos dos usos mais comuns do NumPy na análise de dados. A biblioteca oferece uma ampla variedade de funções e recursos para manipulação e cálculos numéricos eficientes em arrays multidimensionais.

