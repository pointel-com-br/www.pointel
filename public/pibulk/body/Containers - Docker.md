# Containers - Docker

O Docker é uma plataforma de código aberto que permite criar, implantar e executar aplicativos em contêineres. Um contêiner é uma unidade leve e isolada que empacota todo o ambiente necessário para executar um aplicativo, incluindo o código, as bibliotecas, as dependências e as variáveis de ambiente. Com o Docker, é possível criar contêineres independentes e portáteis que podem ser executados em qualquer ambiente, desde servidores locais até ambientes em nuvem.

Aqui estão alguns conceitos-chave relacionados ao Docker:

1. Imagens: Uma imagem Docker é uma representação somente leitura de um contêiner. Ela contém todo o sistema de arquivos necessário para executar um aplicativo, juntamente com as dependências e configurações específicas. As imagens Docker são criadas a partir de um arquivo chamado Dockerfile, que especifica as instruções para construir a imagem.

2. Contêineres: Um contêiner Docker é uma instância em execução de uma imagem. Ele oferece um ambiente isolado para a execução de um aplicativo, garantindo que as dependências e configurações sejam consistentes. Os contêineres Docker são leves, inicializam rapidamente e compartilham o kernel do sistema operacional host, o que os torna eficientes em termos de recursos.

3. Registro: Um registro Docker é um repositório de imagens Docker. O Docker Hub é o registro público padrão, que oferece uma ampla variedade de imagens prontas para uso. No entanto, também é possível configurar registros privados para armazenar e compartilhar imagens personalizadas dentro de uma organização.

4. Docker Compose: O Docker Compose é uma ferramenta que permite definir e executar aplicativos multi-container. Com um arquivo chamado docker-compose.yml, você pode especificar os serviços, as redes e os volumes necessários para um aplicativo composto por vários contêineres. O Docker Compose simplifica a orquestração e a execução de aplicativos com várias partes.

5. Orquestração: Embora o Docker seja uma ferramenta poderosa para criar e executar contêineres isolados, ele não oferece recursos avançados de orquestração, como o dimensionamento automático e o gerenciamento de vários contêineres em cluster. Para isso, são usadas plataformas de orquestração de contêineres, como o Kubernetes ou o OpenShift, que podem gerenciar e orquestrar os contêineres Docker em ambientes distribuídos.

O Docker revolucionou a forma como os aplicativos são empacotados e implantados, fornecendo uma solução padronizada para a execução de aplicativos em contêineres. Ele facilita a criação de ambientes consistentes e reproducíveis, além de simplificar o processo de implantação e escalabilidade de aplicativos em contêineres.

Caros alunos (as), o Docker é um software usado como contêiner da empresa Docker, Inc, que fornece uma camada de abstração e automação para virtualização de sistema operacional no Windows e no Linux.
Como ele faz isso? Segundo o fornecedor: o Docker emprega isolamento de recurso do núcleo do Linux e espaços de nomes do núcleo, e um sistema de arquivos com recursos de união, como OverlayFS criando contêineres independentes para executar dentro de uma única instância do sistema operacional, evitando a sobrecarga de manter máquinas virtuais (VM).

O docker então é uma alternativa de virtualização em que o kernel da máquina hospedeira é compartilhado com a máquina virtualizada ou o software em operação, portanto um desenvolvedor pode agregar a seu software a possibilidade de levar as bibliotecas e outras dependências do seu programa junto ao software com menos perda de desempenho do que a virtualização do hardware de um servidor completo. Assim, o docker torna operações em uma infraestrutura como serviços web mais intercambiável, eficientes e flexíveis.

Na prática o docker é utilizado como uma ferramenta que pode empacotar um aplicativo e suas dependências em um recipiente virtual que pode ser executado em qualquer servidor que contenha o Docker instalado. Isso ajuda a permitir flexibilidade e portabilidade de onde o aplicativo pode ser executado, quer nas instalações, nuvem pública, nuvem privada, entre outros. Então o que exatamente o Docker faz e por que utilizamos ele? Docker é uma plataforma que utiliza containers como solução arquitetural, para aumentar a portabilidade e eficiência. Perai professor eu ainda não sei o que são containers.

Pessoal, um container é um ambiente isolado, que representa um conjunto de processos executados a partir de uma imagem, a imagem é o local onde estão todos os arquivos necessários para execução do container, logo os containers compartilham o kernel e isolam os processos das aplicações do resto do sistema.
Por exemplo: se você está desenvolvendo uma aplicação para um cliente, você pode fazer suas configurações nessa aplicação. Mas, em um ambiente convencional, você precisará replicar estas configurações para os outros ambientes de execução. Ok?!

Com o Docker, você pode ir fazendo isso em um ambiente isolado e, por causa da facilidade para replicação de containers, você acaba criando ambientes padronizados, tanto em desenvolvimento como em produção, por exemplo. Assim, você pode disponibilizar essa arquitetura toda para seu cliente, onde ele estiver: basta replicar os containers, que serão executados da mesma maneira em qualquer lugar.

Como o container possui uma imagem que contém todas as dependências de um aplicativo, ele é portátil e consistente em todas as etapas de desenvolvimento. Essa imagem é um modelo de somente leitura que é utilizada para subir um container. O Docker nos permite construir nossas próprias imagens e utilizá-las como base para os containers.

Pessoal, Docker é então uma plataforma open source escrito em Go, que é uma linguagem de programação de alto desempenho desenvolvida dentro do Google, que facilita a criação e administração de ambientes isolados. O Docker possibilita o empacotamento de uma aplicação ou ambiente inteiro dentro de um container, e a partir desse momento o ambiente inteiro torna-se portável para qualquer outro host que contenha o Docker instalado. O Docker pode ler instruções através de um arquivo texto que contém instruções para montar uma imagem (dockerfile).

Isso reduz drasticamente o tempo de deploy (implantação) de alguma infraestrutura ou até mesmo aplicação, pois não há a necessidade de ajustes de ambiente para o correto funcionamento do serviço. O ambiente é sempre o mesmo, basta configurar uma vez e replicar quantas vezes quiser! Outra facilidade do Docker é poder criar suas imagens (containers prontos para deploy) a partir de arquivos de definição, os chamados Dockerfiles.
Outro fator importante é que o Docker utiliza como backend padrão o LXC (Linux Containers), com isso é possível definir limitações de recursos por container (memória, CPU, E/S etc.).

O LXC é um método de virtualização a nível de sistema operacional que permite executar múltiplos Sistemas Linux (denominados containers) usando um único kernel. Pessoal, importante ressaltar um dos principais comandos do Docker, que serve para visualizar informações referentes ao consumo de recursos de todos os containers, deve-se executar no terminal: Docker container stats.

Assim, pode-se criar ambientes de teste e/ou produção utilizando o LXC de forma ágil e segura (isolada). Não há a necessidade de se preocupar com tantos detalhes como na virtualização tradicional.
Quanto as instruções Docker, uma se destaca por ser responsável por indicar ao docker a porta que o container deve utilizar em tempo de execução, trata-se da EXPOSE. Outras instruções importantes, seriam:

- ADD : Adiciona um arquivo ou diretório dos sistemas de arquivo local para a imagem;

- COPY : Copia arquivos remotos e/ou locais para a imagem.

- CMD : Comando padrão a ser executado pela imagem;

- ENTRYPOINT : Permite configurar o contêiner ou apenas definir o comando a ser executado (Sobrepõe o CMD);

- ENV : Define variáveis de ambiente;

- FROM : Inicia a imagem a partir de outra imagem: Ex "FROM debian:8";

- RUN : Roda um comando no sistema operacional da imagem;

- ARG : Define variáveis de ambiente, mas permite que no momento da construção da imagem seja passado o valor para a variável específicada. Útil para quando se deseja permitir que o usuário construa imagens para mais de uma versão do mesmo software usando o mesmo DockerFile.

Como o Docker trabalha utilizando cliente e servidor (toda a comunicação entre o Docker Daemon e Docker client é realizada através de API), basta apenas ter instalado o serviço do Docker em um lugar, e apontar em o Docker Client para esse servidor. A plataforma do Docker em si utilizada alguns conjuntos de recursos, seja para a criação ou administração dos containers.

Entre esses conjuntos podemos destacar a biblioteca libcontainer, que é responsável pela comunicação entre o Docker Daemon e o backend utilizado, sendo ela a responsável pela criação do container, e através dela é possível configurar os limites de recursos por container.

Vale lembrar que, apesar do Docker ter sido desenvolvido inicialmente com base na tecnologia LXC (Linux Containers - sendo, portanto, mais associado aos containers Linux), hoje essa tecnologia tornou-se independente de sistema operacional: podemos utilizar o Docker em ambientes Linux, Windows e até mesmo MacOS.

