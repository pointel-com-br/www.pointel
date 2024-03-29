# Arquitetura hexagonal

A arquitetura hexagonal, também conhecida como arquitetura ports and adapters, é um padrão arquitetural que busca promover a separação de preocupações e a modularidade em sistemas de software. Ela foi proposta por Alistair Cockburn em 2005 e se baseia no princípio de que as regras de negócio do sistema devem ser o núcleo central e independente de qualquer tecnologia ou detalhes de implementação externos.

Principais conceitos da arquitetura hexagonal:

1. Domínio: É o núcleo central da arquitetura, onde residem as regras de negócio e a lógica do sistema. É um componente independente, que não conhece detalhes da infraestrutura externa.

2. Portas (Ports): As portas são interfaces que definem os contratos entre o domínio e o mundo externo. Elas são responsáveis por permitir a interação entre o domínio e os adaptadores.

3. Adaptadores (Adapters): Os adaptadores são responsáveis por implementar as portas, conectando o domínio às tecnologias e frameworks externos. Eles adaptam as interfaces do domínio para as interfaces específicas da infraestrutura.

4. Camadas externas: Além do domínio, a arquitetura hexagonal possui camadas externas, como a camada de aplicação, que coordena a interação entre o domínio e as interfaces externas, e a camada de infraestrutura, que lida com as tecnologias e frameworks específicos.

Benefícios da arquitetura hexagonal:

1. Testabilidade: A separação clara entre o domínio e as interfaces externas facilita a realização de testes automatizados, uma vez que o domínio pode ser testado de forma isolada, sem depender de infraestrutura externa.

2. Manutenibilidade: A modularidade promovida pela arquitetura hexagonal facilita a manutenção do sistema, pois permite que as partes sejam alteradas de forma independente, desde que as interfaces sejam mantidas.

3. Flexibilidade: A arquitetura hexagonal permite a troca de tecnologias e frameworks externos sem afetar o núcleo do sistema, uma vez que a lógica do domínio não depende desses detalhes de implementação.

4. Reutilização: A separação de preocupações facilita a reutilização de componentes e a composição de diferentes partes do sistema, promovendo a modularidade e reduzindo a duplicação de código.

A arquitetura hexagonal é especialmente útil em sistemas que possuem regras de negócio complexas e que precisam se adaptar a mudanças frequentes nos requisitos e tecnologias. Ela ajuda a manter o foco nas regras de negócio e a evitar o acoplamento excessivo com detalhes de implementação, resultando em sistemas mais flexíveis, testáveis e de fácil manutenção.
