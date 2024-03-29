# Testes com Mock e stubs

Os testes com mocks e stubs são técnicas comuns usadas nos testes de software para isolar componentes e simular comportamentos de dependências externas durante os testes de unidades.

1. Mocks: Um mock é um objeto simulado que replica o comportamento de um componente real para fins de teste. Os mocks são usados para simular interações com dependências externas, como bancos de dados, serviços web ou sistemas legados. Eles permitem controlar as respostas esperadas e verificar se o componente testado se comporta corretamente diante dessas respostas.

- Exemplo: Em um teste de unidade para um serviço que realiza chamadas a um banco de dados, um mock pode ser usado para simular o comportamento do banco de dados. O mock será configurado para retornar dados específicos quando uma consulta for feita, permitindo que o serviço seja testado independentemente do banco de dados real.

2. Stubs: Um stub é um objeto que fornece respostas predefinidas aos métodos chamados durante os testes. Diferentemente dos mocks, os stubs geralmente não têm expectativas de comportamento específicas ou verificações, mas fornecem apenas as respostas necessárias para executar o teste.

- Exemplo: Suponha que um componente dependa de uma API externa para obter informações. Durante os testes, um stub pode ser usado para fornecer respostas fixas em vez de fazer chamadas reais à API. Isso permite que o componente seja testado sem depender do estado atual da API externa.

Tanto os mocks quanto os stubs são usados para isolar o componente testado e garantir que ele seja testado de forma independente, sem depender de sistemas externos ou de dados em tempo real. Isso traz benefícios, como a execução de testes mais rápidos, a criação de cenários específicos para verificar casos de teste complexos e a redução de dependências externas durante o processo de teste.

É importante notar que mocks e stubs devem ser usados com cautela e de forma adequada aos contextos de teste. Eles devem ser configurados corretamente para refletir o comportamento real das dependências e garantir que os testes sejam representativos do sistema em execução.
