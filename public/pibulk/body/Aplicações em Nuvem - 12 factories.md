# Aplicações em Nuvem - 12 factories

A arquitetura de 12 factories, também conhecida como "The Twelve-Factor App", é um conjunto de práticas e princípios para desenvolver aplicações em nuvem que são escaláveis, flexíveis e fáceis de manter. Essa abordagem foi definida por Adam Wiggins e descreve um conjunto de boas práticas que podem ser aplicadas ao desenvolvimento de software para ambientes em nuvem. Aqui estão os 12 fatores principais:

1. Base de código: Utilize um controle de versão para rastrear as mudanças no código-fonte e garantir uma base de código sólida.

2. Dependências: Gerencie as dependências do projeto explicitamente e evite depender do ambiente de execução.

3. Configurações: Armazene as configurações do aplicativo em variáveis de ambiente, permitindo uma configuração flexível e portável.

4. Backing Services: Trate serviços externos, como bancos de dados, filas de mensagens e serviços de armazenamento, como recursos anexos que podem ser facilmente substituídos.

5. Build, Release, Run: Separe o processo de construção (build), lançamento (release) e execução (run) do aplicativo para garantir uma implantação consistente e repetível.

6. Processos: Execute o aplicativo como um ou mais processos sem estado e garanta que esses processos possam ser escalados e interrompidos de forma independente.

7. Vínculo de porta: Exponha serviços por meio de uma interface de rede declarada, normalmente usando a ligação de porta (binding de porta) em um ambiente de nuvem.

8. Concorrência: Dimensione o aplicativo horizontalmente, adicionando mais instâncias em vez de aumentar a escala verticalmente, permitindo maior resiliência e desempenho.

9. Descartabilidade: Projete o aplicativo para ser facilmente iniciado e encerrado, permitindo a rápida recuperação de falhas e atualizações.

10. Dev/Prod Parity: Mantenha a paridade entre os ambientes de desenvolvimento, teste e produção, minimizando as diferenças para evitar problemas causados por disparidades de configuração.

11. Logs: Trate os logs como fluxos de eventos e envie-os para um sistema de log centralizado para facilitar o monitoramento e a depuração.

12. Administração de processos: Execute tarefas de administração como processos de primeira classe, automatizando e documentando essas tarefas.

Esses 12 fatores fornecem diretrizes valiosas para projetar e desenvolver aplicações em nuvem de forma escalável, resiliente e fácil de gerenciar. Ao seguir esses princípios, você pode criar aplicativos que são mais fáceis de implantar, manter e dimensionar em um ambiente de nuvem.
