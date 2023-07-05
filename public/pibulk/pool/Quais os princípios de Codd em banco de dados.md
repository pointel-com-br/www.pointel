# Quais os princípios de Codd em banco de dados?

Os princípios de Codd, também conhecidos como as "12 regras de Codd", são um conjunto de diretrizes propostas por Edgar F. Codd, o pioneiro dos bancos de dados relacionais. Esses princípios visam estabelecer os fundamentos para um sistema de gerenciamento de banco de dados relacional confiável e consistente. Aqui estão os princípios de Codd:

1. **Regra da Informação**: Todo o acesso aos dados deve ser feito através de estruturas lógicas de alto nível (como consultas SQL), e não através de acesso físico direto.

2. **Regra do Tratamento Sistemático de Null**: O sistema de gerenciamento de banco de dados deve fornecer um tratamento consistente e sistemático para valores nulos (NULL), que representam a ausência de um valor em uma coluna.

3. **Regra do Catálogo Dinâmico Online**: O catálogo do banco de dados, que contém metadados sobre a estrutura do banco de dados, deve ser acessível e modificável pelo próprio sistema de gerenciamento de banco de dados.

4. **Regra da Sublinguagem de Dados Completa**: O sistema de gerenciamento de banco de dados deve incluir uma sublinguagem de dados completa, que possibilite a definição, manipulação e controle dos dados armazenados.

5. **Regra da Garantia de Integridade**: O sistema de gerenciamento de banco de dados deve suportar a especificação e aplicação de regras de integridade, garantindo a consistência dos dados armazenados.

6. **Regra da Independência Lógica de Dados**: As aplicações que utilizam o banco de dados devem ser independentes das estruturas de armazenamento físico dos dados.

7. **Regra da Independência Física de Dados**: As aplicações que utilizam o banco de dados devem ser independentes dos detalhes físicos de armazenamento e acesso aos dados.

8. **Regra da Independência de Distribuição**: A distribuição dos dados em diferentes locais (por exemplo, em um ambiente de banco de dados distribuído) não deve afetar a capacidade das aplicações acessarem e manipularem esses dados.

9. **Regra da Não-Subversão**: O sistema de gerenciamento de banco de dados não deve permitir que os usuários contornem as regras de integridade e segurança estabelecidas.

10. **Regra da Atualização em Visões**: O sistema de gerenciamento de banco de dados deve permitir a atualização de dados através de visões, que são representações lógicas dos dados armazenados.

11. **Regra da Independência de Programas de Aplicação**: As aplicações que utilizam o banco de dados devem ser independentes dos detalhes de programação e linguagens de programação.

12. **Regra da Não Dupla Interpretação de Dados**: O sistema de gerenciamento de banco de dados deve evitar ambiguidades na interpretação dos dados armazenados, garantindo a consistência e a integridade das informações.

Esses princípios estabelecem diretrizes importantes para o projeto, implementação e uso de sistemas de gerenciamento de banco de dados relacionais, promovendo a consistência, a integridade e a independência dos dados.
