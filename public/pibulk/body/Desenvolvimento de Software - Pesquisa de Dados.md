# Desenvolvimento de Software - Pesquisa de Dados

Busca Sequencial

Galera, imaginem que eu estou à procura de um valor X em um vetor L [ ]! Para tal, posso inspecionar as posições sequenciais de L[ ] a partir da primeira posição: se eu encontrar X, minha busca tem êxito; se eu alcanço a última posição e não encontro X, concluímos que esse valor não ocorre no vetor L [ ]. Como é chamada essa busca em que eu inspeciono uma estrutura posição por posição? Sequencial ou Linear.
Considerando que o vetor L [ ] contém N elementos, ordenados ou não, é fácil verificar que a busca sequencial requer tempo linearmente proporcional ao tamanho do vetor, i.e., da ordem O ( n ). Por conta disso, é comum dizer que a busca sequencial é uma Busca Linear.
Entenderam? Quanto maior o vetor, maior o tempo em média para buscar um elemento! Quanto mais ao final, mais demorado.

A Busca Sequencial é muito lenta para grandes quantidades de dados, mas aceitável para listas pequenas e que mudam constantemente. Observa-se que no Melhor Caso, X está na primeira posição, logo necessita apenas de uma comparação; no Pior Caso, X está na última posição, logo necessita de N comparações; e no Caso Médio, X é encontrado após ( n + 1 ) / 2 comparações.

A seguir, encontram-se dois algoritmos para realização de uma Busca Sequencial: o primeiro ocorre de forma simples e o segundo ocorre de forma recursiva. Galera, para vetores de médio ou grande porte, o tempo de busca sequencial é considerado completamente inaceitável, dado que existem técnicas mais eficientes! Professor, me dá um exemplo? Claro, veremos adiante: Busca Binária!

Busca Binária

A Busca Binária é um algoritmo de busca em vetores que segue o paradigma de divisão-e- conquista. Parte-se do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca, comparando o elemento chave com o elemento do meio do vetor. Possui complexidade da ordem de O ( log 2 n ), em que N é o tamanho do vetor de busca.

Quando o Vetor L [ ] estiver em ordem crescente, podemos determinar se X ocorre em L [ ] de forma mais rápida da seguinte forma: inspeciona-se a posição central do vetor! Se essa posição já contiver X, a busca para! Por que, professor? Porque nós já encontramos X! Se X for menor que esse elemento central, passamos a procurar X, recursivamente, no intervalo de L [ ] que se encontra à esquerda da posição central.

Se X for maior do que o elemento central, continuamos a procurar X, recursivamente, no intervalo de L que está à direita da posição central. Se o intervalo se tornar vazio, a busca para, tendo sido malsucedida. Esse procedimento é conhecido como Busca Binária e, facilmente, pode-se adaptar a busca em ordem decrescente.

Na imagem abaixo, estamos à procura do valor 23! Em vermelho, encontra-se o elemento inicial L [ 0 ] = 2 e, em amarelo, encontra-se o elemento final L [ N - 1 ] = 57. Procuramos, então, o elemento central! Como? Ele é o elemento de índice [ 0 + ( N - 1 ) ] / 2 = 7 / 2 = 3 , 5 = 3 (Arredonda-se para baixo). Ora, L [ 3 ] = 19! Encontramos? Não, 23 > 19! Sendo assim, L [ 0 ] = 19 e L [ 4 ] = 57.

Procuramos, então, o elemento central! Como? Ele é o elemento de índice [ 0 + ( N - 1 ) ] / 2 = 4 / 2 = 2. Ora, L [ 2 ] = 51! Encontramos? Não, 23 < 51! Sendo assim, L [ 0 ] = 19 e L [ 2 ] = 51. Procuramos, então, o elemento central! Como? Ele é o elemento de índice [ 0 + ( N - 1 ) ] / 2 = 2 / 2 = 1. Ora, L [ 1 ] = 23! Encontramos? Sim! Então, nossa busca obteve êxito e encontramos o que buscávamos.
