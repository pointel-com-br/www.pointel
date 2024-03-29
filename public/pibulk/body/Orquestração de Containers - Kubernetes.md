# Orquestração de Containers - Kubernetes

A orquestração de containers refere-se ao gerenciamento de aplicações em containers, como Docker, em ambientes distribuídos. O Kubernetes é uma plataforma de orquestração de containers amplamente utilizada que foi desenvolvida pelo Google e agora é mantida pela Cloud Native Computing Foundation (CNCF). O Kubernetes fornece um conjunto de ferramentas e recursos que permitem implantar, dimensionar e gerenciar aplicativos em containers de forma eficiente.

Aqui estão alguns conceitos-chave relacionados à orquestração de containers com Kubernetes:

1. Pods: O Kubernetes agrupa os containers em unidades lógicas chamadas de pods. Um pod é a menor unidade de implantação no Kubernetes e pode conter um ou mais containers que são sempre co-localizados e compartilham recursos, como endereço IP e espaço de armazenamento.

2. Replication Controller/Replica Set: Esses recursos do Kubernetes garantem que um número especificado de réplicas (pods) esteja em execução em todos os momentos. Eles são responsáveis por manter a alta disponibilidade dos aplicativos e lidar com o balanceamento de carga entre os pods.

3. Deployment: Um objeto de implantação no Kubernetes permite gerenciar a implantação de aplicativos, permitindo atualizações e rollbacks. Ele controla a criação e atualização de pods com base em uma descrição declarativa das especificações do aplicativo.

4. Service: Um serviço Kubernetes fornece uma abstração de rede estável para um conjunto de pods. Ele permite a descoberta dinâmica de endpoints de pod e balanceamento de carga para garantir que os aplicativos possam se comunicar entre si.

5. ConfigMap e Secrets: Esses recursos permitem a separação de configurações e segredos do código do aplicativo. Eles permitem que as configurações sejam gerenciadas separadamente e injetadas nos pods conforme necessário.

6. Persistent Volumes e Persistent Volume Claims: Esses recursos permitem que os aplicativos acessem armazenamento persistente no Kubernetes. Os Persistent Volumes representam o armazenamento subjacente, enquanto os Persistent Volume Claims são solicitações feitas pelos aplicativos para obter acesso a um volume persistente.

7. Helm: O Helm é um gerenciador de pacotes para o Kubernetes que simplifica a implantação e o gerenciamento de aplicativos Kubernetes. Ele permite a definição e o compartilhamento de gráficos (charts) que contêm informações sobre os recursos e dependências do aplicativo.

Esses são apenas alguns dos principais conceitos e recursos do Kubernetes. A plataforma oferece muitos outros recursos avançados, como autoscaling, políticas de segurança, monitoramento e muito mais. A orquestração de containers com Kubernetes ajuda as equipes de desenvolvimento e operações a implantar e gerenciar aplicativos de forma escalável, confiável e flexível.

O Kubernetes é um sistema de código aberto que foi desenvolvido pelo Google para gerenciamento de aplicativos em containers através de múltiplos hosts de um cluster. Tem como principal objetivo facilitar a implantação de aplicativos baseados em microservices. Ele foi baseado na experiência do Google de muitos anos trabalho com containers, adaptando-o para se trabalhar com Docker.
O Kubernetes é uma ferramenta de orquestração que oferece recursos de gerenciamento para containers, foi muito útil para ser utilizado até o Docker Swarm 1.0, pois disponibilizava muitos recursos que o Docker não disponibilizava até aquele momento, entre eles: Balanceamento de carga e movimento de containers sem perda de dados.

A principal vantagem que se tem ao utilizar o Kubernetes é que você não está preso as limitações da API do Docker, logo você tem total liberdade já que o Kubernetes não foi desenvolvido especialmente para o Docker, você pode trocar a sua estrutura de Docker para Rockets e vice-versa por exemplo.
Hoje o Kubernetes é mantido pela Cloud Native Computing Foundation e tem como papel principal prover o gerenciamento de clusters que executam as aplicações. Esses clusters podem ser hots disponíveis em nuvem, logo kubernetes é ideal para cloud native apps que podem exigir escalabilidade rápida.
Para ficar mais claro, imagine o seguinte: Você precisa fazer deploy de uma nova versão de uma aplicação em nuvem, milhares de coisas podem dar errado e você pode precisar realizar rollback para a versão anterior. Porém além disso, a aplicação é composta por dezenas de microsserviços, cada um com um ciclo de vida diferente do outro, releases diferentes, tecnologias diferentes, etc.

Pensando nisso a arquitetura de microsserviços adotou o Kubernetes como uma referência, já que na prática as aplicações baseadas em arquitetura de microsserviços, incorporam automação em todo seu ciclo de vida, logo diferente de aplicações monolíticas, com forte acomplamento, as APIs com microsserviços tem características descentralizadas e fracamente acopladas. Logo, basta encapsular as principais características dos serviços em containers.

Como esses contêineres possuem o serviço e todas as suas dependências, eles se tornam independentes da infraestrutura, podendo ser facilmente migrados de uma cloud para outra, por exemplo, facilitando escalabilidade e deploy.
Dentro desse contexto, o Kubernetes oferece várias funcionalidades, dentre eles temos a ideia central, isto é, o estado da aplicação. Para o Kubernetes existes dois estados de uma aplicação: o atual e o desejado. O estado atual da aplicação descreve a realidade. Por exemplo, quantas réplicas de um determinado serviço estão em execução, qual a versão em produção de cada serviço e por aí vai.

Já o estado desejado descreve como o time ou a pessoa responsável pela aplicação deseja que ela esteja naquele momento. O Kubernetes implementa uma série de loops que ficam constantemente verificando se o estado atual é igual ao estado desejado. Esse papel é desempenhado pelos chamados Controllers.
Quando um controller identifica que o estado atual é diferente do estado desejado, ele aciona outros componentes do sistema para fazer novamente com que o estado atual se iguale ao estado desejado. Todo esse processo de monitoramento e gestão do estado da aplicação, sem contar a execução da aplicação em si, exige uma série de componentes. É por isso que a arquitetura de um ambiente Kubernetes é baseada em um cluster de máquinas.

Pessoal, o Kubernetes é composto por uma vários componentes, cada um com um propósito diferente. Para garantir que exista uma separação de responsabilidades e que o sistema seja resiliente, o kubernetes utiliza um cluster de máquinas para ser executado, logo as máquinas de um cluster são separadas em três tipos: Node, Etcd e Master.

NODE

O papel de um node é executar os contêineres que encapsulam as aplicações.

ETCD

O etcd é a base de dados distribuída que é utilizada para armazenar tudo o que acontece dentro do cluster, incluindo o estado da aplicação.

MASTER

O master é responsável pelos principais componentes do kubernetes, como o scheduler, que tem a responsabilidadae de controlar a alocação de recursos no cluster.

Como já vimos as aplicações que utilizam microsserviços, constumam utilizar containers para encapsulamento dos microsserviços. No entanto, quando falamos sobre aplicações sendo executadas em um cluster Kubernetes, não falamos sobre contêineres diretamente, mas sim sobre Pods. No Kubernetes, temos o kubelet que é uma pequena aplicação localizada em um nó que se comunica com o plano de controle, assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.
Pods são a unidade básica de um cluster. Os Pods encapsulam um ou mais containers de uma aplicação e representam um processo dentro do cluster. Logo, quando fazemos o deploy de uma aplicação no Kubernetes, estamos criando uma ou mais Pods. No Kubernetes, kubelet é uma pequena aplicação localizada em um nó que se comunica com o plano de controle, assegurando que os containers estejam em execução em um pod, que consiste no menor e mais simples objeto do Kubernetes.

Por fim, para garantir que o acesso a um microsserviços esteja sempre disponível, temos um objeto no Kubernetes, chamado de Service, o Service é que encapsula um ou mais Pods e é capaz de encontra-los dinamicamente em qualquer lugar do cluster.
Precisamos por últimos falar do CNFC (Cloud Native Computing Foundation).
Pessoal, o CNFC é parte do Linux foundation e oferece suporte para projetos nativos em nuvem, como o Kubernetes, o Envoy e o Prometheus. Como fundação a CNFC é responsável por diversas certificações em Kubernetes, que é seu principal expoente, além de promover a cultura DevOps mundo a fora.
O que a Cloud Native Computing Foundation busca é promover o desenvolvimento e evolução do emprego de containers no desenvolvimento de soluções, principalmente em soluções nativas de nuvem.

