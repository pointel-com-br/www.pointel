# Sistemas de banco de dados - álgebra relacional

A álgebra relacional é um conjunto de operações matemáticas que formam a base teórica dos sistemas de banco de dados relacionais. Essas operações são aplicadas a relações, que são conjuntos de tuplas (linhas) com atributos (colunas). A álgebra relacional permite realizar consultas e manipulações nos dados armazenados no banco de dados. Aqui estão algumas das principais operações da álgebra relacional:

1. Projeção (π): A operação de projeção seleciona um subconjunto de colunas de uma relação, produzindo uma nova relação que contém apenas as colunas especificadas. Por exemplo, π(nome, idade)(Clientes) retorna uma nova relação que contém apenas as colunas "nome" e "idade" da relação Clientes.

2. Seleção (σ): A operação de seleção filtra as tuplas de uma relação com base em uma condição especificada. Por exemplo, σ(idade > 18)(Clientes) retorna uma nova relação que contém apenas as tuplas da relação Clientes em que a idade é maior que 18.

3. União (∪): A operação de união combina as tuplas de duas relações compatíveis (com o mesmo conjunto de atributos) para formar uma nova relação. Por exemplo, R ∪ S retorna uma nova relação que contém todas as tuplas de R e S, eliminando duplicatas.

4. Interseção (∩): A operação de interseção retorna as tuplas que são comuns a duas relações compatíveis. Por exemplo, R ∩ S retorna uma nova relação que contém apenas as tuplas que existem tanto em R quanto em S.

5. Diferença (-): A operação de diferença retorna as tuplas que estão em uma relação, mas não na outra. Por exemplo, R - S retorna uma nova relação que contém as tuplas que estão em R, mas não em S.

6. Produto Cartesiano (×): A operação de produto cartesiano combina cada tupla de uma relação com cada tupla de outra relação, formando uma nova relação. Por exemplo, R × S retorna uma nova relação que contém todas as combinações de tuplas de R e S.

Essas são apenas algumas das operações básicas da álgebra relacional. Elas podem ser combinadas para formar consultas mais complexas e realizar operações de junção, agregação e ordenação nos dados. A álgebra relacional fornece uma base teórica sólida para a manipulação de dados em sistemas de banco de dados relacionais e é amplamente utilizada no desenvolvimento de consultas e na otimização de desempenho.
