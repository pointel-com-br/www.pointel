# Análise de Pontos de Função

A Análise de Pontos de Função (APF) é uma técnica de estimativa utilizada para medir o tamanho funcional de um software com base nas funcionalidades e nos requisitos do sistema. Ela é independente de tecnologia e linguagem de programação, focando na quantificação do valor entregue ao usuário final.

A análise de Pontos de Função envolve os seguintes passos:

1. Identificação das Funcionalidades: O primeiro passo é identificar as funcionalidades do software que serão analisadas. Essas funcionalidades podem incluir funções de entrada de dados, funções de saída, consultas a bancos de dados, interfaces com outros sistemas, entre outros.

2. Classificação das Funcionalidades: Cada funcionalidade identificada é classificada de acordo com as categorias definidas no método de análise de Pontos de Função. As categorias mais comuns são:
- Funções de Entrada de Dados (Input): São as funcionalidades que recebem dados do usuário.
- Funções de Saída de Dados (Output): São as funcionalidades que apresentam informações ao usuário.
- Funções de Consulta (Inquiry): São as funcionalidades que fornecem informações ao usuário, sem modificar os dados.
- Funções de Arquivos Lógicos Internos (Internal Logical Files - ILFs): São as funcionalidades que mantêm informações dentro do sistema.
- Funções de Interfaces Externas (External Interface Files - EIFs): São as funcionalidades que interagem com outros sistemas externos.

3. Contagem dos Pontos de Função: Com base nas classificações atribuídas a cada funcionalidade, são aplicadas fórmulas e regras definidas pela Análise de Pontos de Função para calcular a pontuação total. Essas fórmulas consideram a complexidade das funcionalidades, o número de entradas e saídas, as relações entre os elementos do sistema, entre outros fatores.

4. Ajustes por Fatores de Complexidade: Após a contagem inicial dos Pontos de Função, podem ser aplicados ajustes para considerar fatores adicionais que afetam a complexidade do software, como desempenho, segurança, usabilidade, entre outros. Esses ajustes são multiplicadores que podem aumentar ou diminuir a pontuação inicialmente calculada.

5. Validação e Revisão: Após a contagem dos Pontos de Função, é importante validar e revisar a análise para garantir que todos os requisitos e funcionalidades relevantes foram considerados e que a pontuação final está correta.

A Análise de Pontos de Função é uma técnica amplamente utilizada na engenharia de software para auxiliar na estimativa de tamanho e esforço de desenvolvimento de um projeto. Ela fornece uma medida objetiva e consistente do valor entregue pelo software e pode ser usada como base para estimativas de prazos, custos e recursos necessários.

## Segundo o IFPUG quais são os tipos de contagem de pontos de função?

Segundo o International Function Point Users Group (IFPUG), existem três tipos de contagem de pontos de função:

1. Contagem de Pontos de Função Não Ajustada (UFP - Unadjusted Function Points): É a contagem inicial dos pontos de função antes de aplicar os ajustes de complexidade. Nessa contagem, são consideradas apenas as cinco principais características funcionais: Arquivos Lógicos Internos (Internal Logical Files - ILFs), Transações Externas (External Inputs - EIs), Consultas Externas (External Outputs - EOs), Arquivos de Interface Externos (External Interface Files - EIFs) e Arquivos Referenciados (Referenced Files).

2. Contagem de Pontos de Função Ajustada (AFP - Adjusted Function Points): É a contagem resultante após a aplicação dos ajustes de complexidade. Os ajustes consideram fatores como a complexidade dos processos, a interface do usuário, a reutilização de componentes, a performance, a facilidade de instalação e a manutenibilidade do sistema. A contagem ajustada reflete melhor a complexidade e o esforço necessário para desenvolver ou manter o sistema.

3. Contagem de Pontos de Função Detalhada (DFP - Detailed Function Points): É uma contagem mais detalhada e refinada, que leva em consideração uma maior quantidade de características funcionais e suas respectivas complexidades. Essa contagem é mais granular e pode ser utilizada em casos especiais ou para análises mais aprofundadas.

Esses tipos de contagem de pontos de função são utilizados para medir o tamanho funcional de um software e servem como base para estimar o esforço necessário para desenvolver, manter ou modificar um sistema.

## Segundo o IFPUG quais são os momentos de uma aplicação que podemos fazer uma contagem de pontos de função?

Segundo o International Function Point Users Group (IFPUG), existem quatro momentos em que é possível fazer a contagem de pontos de função:

1. Contagem de Pontos de Função de Pré-Implementação (Pre-Implementation Function Point Counting): É feita antes do início do desenvolvimento ou modificação do sistema. Nesse momento, a contagem é baseada em documentos de requisitos, especificações funcionais e outros artefatos que descrevem o escopo do sistema a ser desenvolvido.

2. Contagem de Pontos de Função de Detalhamento (Detail Function Point Counting): É feita durante ou após o desenvolvimento do sistema, com base em documentos detalhados, como modelos de banco de dados, especificações técnicas e outros artefatos que descrevem com mais precisão as funcionalidades implementadas.

3. Contagem de Pontos de Função de Revisão (Review Function Point Counting): É feita durante uma revisão do sistema já desenvolvido ou modificado. Nesse momento, a contagem é realizada com base no sistema em funcionamento, considerando as funcionalidades implementadas e os documentos que descrevem essas funcionalidades.

4. Contagem de Pontos de Função de Aplicação (Application Function Point Counting): É feita após a conclusão do desenvolvimento ou modificação do sistema, com base no sistema em funcionamento. Essa contagem é útil para determinar o tamanho funcional do sistema implementado e pode ser usada para comparar com outras aplicações semelhantes ou para fins de estimativas de manutenção.

Esses diferentes momentos de contagem de pontos de função permitem obter medidas do tamanho funcional do sistema em diferentes estágios do desenvolvimento ou modificação. Cada momento de contagem possui suas peculiaridades e pode ser mais apropriado em determinadas situações, dependendo do contexto e da disponibilidade de informações sobre o sistema.
