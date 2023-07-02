# Tecnologia backend - Quarkus.

Quarkus é um framework de desenvolvimento de aplicativos Java nativo da nuvem. Ele foi projetado para otimizar o desenvolvimento de aplicativos Java para a nuvem, fornecendo alta velocidade de inicialização, baixo consumo de memória e suporte nativo para contêineres.

O Quarkus é baseado no ecossistema Java padrão, utilizando o Apache Maven para gerenciamento de dependências e o Jakarta EE (anteriormente Java EE) para fornecer recursos e APIs familiares aos desenvolvedores Java. No entanto, ele introduz uma abordagem inovadora para criar aplicativos Java eficientes em termos de recursos.

Algumas das principais características e benefícios do Quarkus são:

1. Baixa latência e alta velocidade de inicialização: O Quarkus é otimizado para oferecer um tempo de inicialização rápido e uma baixa latência de execução. Isso é especialmente útil em ambientes de nuvem, onde a escalabilidade rápida e o provisionamento dinâmico de recursos são importantes.

2. Baixo consumo de memória: O Quarkus é projetado para consumir menos recursos de memória em comparação com outros frameworks Java. Isso é alcançado através de técnicas como compilação nativa, que reduz a quantidade de código e bibliotecas necessárias para a execução do aplicativo.

3. Suporte a contêineres: O Quarkus oferece suporte nativo a contêineres, permitindo que os aplicativos sejam executados em plataformas de contêiner como Docker e Kubernetes. Isso facilita a implantação e o gerenciamento de aplicativos em ambientes de nuvem distribuídos.

4. Desenvolvimento reativo: O Quarkus suporta programação reativa e oferece suporte a fluxos de dados assíncronos. Isso permite que os desenvolvedores criem aplicativos resilientes e eficientes, capazes de lidar com cargas de trabalho intensivas e altamente concorrentes.

5. Ecossistema Java familiar: O Quarkus é construído com base nas tecnologias e padrões Java existentes, como CDI (Contexts and Dependency Injection), JPA (Java Persistence API) e RESTEasy. Isso significa que os desenvolvedores Java podem aproveitar suas habilidades e conhecimentos existentes ao trabalhar com o Quarkus.

6. Extensibilidade: O Quarkus oferece um modelo de extensibilidade flexível, permitindo que os desenvolvedores adicionem facilmente recursos e bibliotecas específicas para atender às necessidades de seus aplicativos. Isso é alcançado por meio do conceito de "extensões", que simplifica a integração de bibliotecas e frameworks de terceiros.

Em resumo, o Quarkus é uma tecnologia backend moderna e eficiente, especialmente adequada para o desenvolvimento de aplicativos Java nativos da nuvem. Ele oferece recursos de alto desempenho, baixo consumo de recursos e suporte nativo a contêineres, permitindo que os desenvolvedores criem aplicativos escaláveis e resilientes para ambientes de nuvem.

# O que é o Quarkus?

Publicado em 13 de janeiro de 2020 * Leitura de %t minutos

Copiar URL

- Visão geral
- Projetado para desenvolvedores
- Foco em contêineres
- Código imperativo e reativo

## Visão geral

O Quarkus é um framework Java de pilha completa, nativo do Kubernetes, feito para máquinas virtuais Java (JVMs) e compilação nativa, otimizando o Java especificamente para contêineres e permitindo que ele se torne uma plataforma eficiente para ambientes de serverless, nuvem e Kubernetes.

O Quarkus foi projetado para funcionar com padrões, frameworks e bibliotecas Java populares, como Eclipse MicroProfile e Spring, além de Apache Kafka, RESTEasy (JAX-RS), Hibernate ORM (JPA), Spring, Infinispan, Camel e muitos outros.

A solução de injeção de dependência do Quarkus é baseada no CDI (Contextos e Injeção de Dependência) e inclui uma estrutura de extensão para expandir a funcionalidade e configurar, inicializar e integrar um framework em sua aplicação. Adicionar uma extensão é tão fácil quanto adicionar uma dependência, ou você pode usar as ferramentas do Quarkus.

Ele também fornece as informações corretas para o GraalVM (uma máquina virtual universal para executar aplicativos escritos em várias linguagens, incluindo Java e JavaScript) para a compilação nativa de sua aplicação.

### Quatro razões para experimentar o Quarkus

Java™ ainda é a linguagem de programação escolhida por muitos desenvolvedores, mas a evolução das tecnologias nativas da nuvem, como o Kubernetes e o serverless, apresenta um desafio. Veja por que o Quarkus é o framework Java de que os desenvolvedores precisam para trabalhar com o Knative e o serverless.

Obtenha a lista de verificação Icon-Red_Hat-Directional-A-Black-RGB

## Projetado para desenvolvedores

O Quarkus foi projetado para ser fácil de usar desde o início, com recursos que funcionam bem com pouca ou nenhuma configuração.

Os desenvolvedores podem escolher os frameworks Java que desejam para suas aplicações, que podem ser executadas no modo JVM ou compiladas e executadas no modo nativo.

Construído com foco na facilidade de uso para os desenvolvedores, o Quarkus também inclui as seguintes capacidades:

- Codificação ao vivo para que os desenvolvedores possam verificar imediatamente o efeito das alterações de código e solucioná-las rapidamente
- Programação imperativa e reativa unificada com um barramento de eventos gerenciado incorporado
- Configuração unificada
- Geração fácil de executáveis nativos

## Foco em contêineres

Seja uma aplicação hospedada em uma nuvem pública ou em um cluster Kubernetes hospedado internamente, características como inicialização rápida e baixo consumo de memória são importantes para manter os custos totais do host baixos.

O Quarkus foi construído com base na filosofia de ser orientado a contêineres, o que significa que ele é otimizado para
uso de memória reduzido e tempos de inicialização mais rápidos das seguintes maneiras:

- Suporte de primeira classe para Graal/SubstrateVM
- Processamento de metadados em tempo de compilação
- Redução no uso de reflexão
- Pré-inicialização da imagem nativa

Dessa forma, o Quarkus constrói aplicativos que consomem 1/10 da memória em comparação com o Java tradicional, e possui um tempo de inicialização mais rápido (até 300 vezes mais rápido), o que reduz consideravelmente o custo dos recursos da nuvem.

## Código imperativo e reativo

O Quarkus foi projetado para combinar perfeitamente o código no estilo imperativo familiar e o estilo reativo, não bloqueante, ao desenvolver aplicações.

Isso é útil tanto para desenvolvedores Java acostumados a trabalhar com o modelo imperativo e que não desejam mudar, quanto para aqueles que trabalham com uma abordagem nativa em nuvem/reactiva.

O modelo de desenvolvimento do Quarkus pode se adaptar ao tipo de aplicativo que você está desenvolvendo.

O Quarkus é uma solução eficaz para executar Java nesse novo mundo de arquitetura serverless, microsserviços, contêineres, Kubernetes, function-as-a-service (FaaS) e nuvem, porque foi criado tendo todas essas coisas em mente.
