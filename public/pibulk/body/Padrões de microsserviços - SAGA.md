# Padrões de microsserviços - SAGA

O padrão SAGA (Sagas) é um padrão de projeto usado em arquitetura de microsserviços para coordenar transações distribuídas entre diferentes serviços. Ele ajuda a manter a consistência dos dados e a garantir a integridade das operações em um ambiente distribuído.

O conceito central do padrão SAGA é dividir uma transação complexa em várias etapas ou passos menores, chamados de "ações" ou "compensações". Cada ação representa uma operação atômica executada por um serviço específico. Essas ações são executadas em sequência para cumprir a transação completa.

Quando uma ação é executada com sucesso, o padrão SAGA avança para a próxima ação. No entanto, se ocorrer um erro em uma ação, o padrão SAGA inicia uma ação de compensação correspondente para desfazer ou reverter as alterações feitas até o momento. Isso garante que as transações sejam revertidas de maneira adequada e consistente em caso de falha.

Existem duas abordagens principais para implementar o padrão SAGA: a abordagem baseada em eventos e a abordagem baseada em comandos.

Na abordagem baseada em eventos, cada ação e ação de compensação são acionadas por eventos. Cada serviço publica eventos relacionados às suas ações e consome eventos de outros serviços para desencadear suas próprias ações. Essa abordagem torna a coordenação de transações mais assíncrona e permite uma maior flexibilidade e desacoplamento entre os serviços.

Na abordagem baseada em comandos, as ações são executadas por meio de chamadas de API síncronas entre os serviços. Cada serviço invoca uma ação em outro serviço e aguarda a resposta antes de prosseguir para a próxima ação. Isso torna a coordenação de transações mais síncrona e requer uma maior comunicação entre os serviços.

A escolha entre as abordagens depende dos requisitos e das características específicas do sistema.

O padrão SAGA é útil em cenários em que as transações distribuídas são necessárias, como em casos de pedidos online, fluxos de trabalho complexos ou processamento de pedidos em várias etapas. Ele ajuda a manter a consistência dos dados e a lidar com falhas em um ambiente de microsserviços, permitindo a execução de operações distribuídas de forma coordenada e confiável.
