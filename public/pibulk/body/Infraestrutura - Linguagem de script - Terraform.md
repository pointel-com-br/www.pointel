# Infraestrutura - Linguagem de script - Terraform

Embora o Terraform não seja estritamente uma linguagem de script, é uma ferramenta amplamente utilizada para provisionar e gerenciar a infraestrutura como código. O Terraform utiliza uma linguagem declarativa própria para descrever a infraestrutura desejada, conhecida como HashiCorp Configuration Language (HCL).

O HCL é uma linguagem de configuração projetada especificamente para o Terraform. Ele permite que os usuários descrevam a infraestrutura desejada de forma declarativa, especificando os recursos, suas configurações e as dependências entre eles. A sintaxe do HCL é simples e legível, facilitando a criação e a manutenção dos arquivos de configuração do Terraform.

Embora o HCL seja usado principalmente para descrever a infraestrutura, o Terraform também suporta o uso de expressões e funções embutidas para realizar cálculos, manipulação de strings e outras operações. Essas expressões permitem a configuração dinâmica e personalizada da infraestrutura.

Uma das principais características do Terraform é a capacidade de provisionar e gerenciar recursos em várias plataformas, incluindo provedores de nuvem pública, como AWS, Azure, Google Cloud, bem como provedores locais, como VMware e OpenStack. O Terraform possui um ecossistema de provedores extensível, que permite aos usuários definirem recursos específicos do provedor em seus arquivos de configuração.

Ao executar o Terraform, ele lê os arquivos de configuração, analisa a infraestrutura desejada e compara com o estado atual. Em seguida, ele cria, atualiza ou remove os recursos necessários para alcançar o estado desejado. O Terraform também mantém um estado do ambiente de infraestrutura gerenciado, permitindo a rastreabilidade e a verificação das mudanças realizadas.

Embora o Terraform não seja uma linguagem de script genérica, ele permite uma abordagem de "infraestrutura como código", em que a configuração da infraestrutura é versionada, automatizada e tratada como qualquer outro código de software. Isso traz benefícios significativos em termos de consistência, rastreabilidade e facilidade de colaboração em projetos de infraestrutura.

Portanto, embora o Terraform não seja uma linguagem de script tradicional, é uma ferramenta poderosa para descrever e gerenciar a infraestrutura como código, tornando a automação e a configuração da infraestrutura mais eficientes e escaláveis.
