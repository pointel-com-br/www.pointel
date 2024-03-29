# Autenticação e autorização - Open ID Connect

O OpenID Connect (OIDC) é uma extensão do protocolo OAuth 2.0 que adiciona recursos de autenticação de identidade. Ele fornece uma camada de autenticação em cima do OAuth 2.0, permitindo que os provedores de identidade autentiquem os usuários e forneçam informações de identidade aos clientes de forma segura.
O OIDC é construído em torno do conceito de provedores de identidade (IdPs) que emitem tokens de identificação. Esses tokens de identificação são usados para autenticar um usuário e fornecer informações sobre a identidade do usuário ao cliente solicitante.

Aqui estão as principais características e componentes do OpenID Connect:

1. Identity Provider (Provedor de Identidade): O provedor de identidade é responsável pela autenticação do usuário e pela emissão de tokens de identificação. Ele mantém as informações de identidade do usuário e fornece essas informações aos clientes que solicitam.

2. Relying Party (Cliente): O cliente é o aplicativo ou serviço que deseja autenticar o usuário usando o OpenID Connect. Ele confia no provedor de identidade para autenticar o usuário e receber informações de identidade.

3. Authorization Server (Servidor de Autorização): O servidor de autorização é responsável por gerenciar o fluxo de autenticação e autorização. Ele lida com as solicitações de autenticação, emite tokens de acesso e tokens de identificação, e fornece informações de configuração para os clientes.

4. ID Token: O ID Token é um token de identificação emitido pelo provedor de identidade após uma autenticação bem-sucedida. Ele contém informações de identidade do usuário, como ID do usuário, nome e outras informações relevantes.

5. UserInfo Endpoint: É um endpoint fornecido pelo provedor de identidade onde o cliente pode solicitar informações adicionais sobre o usuário autenticado. O cliente faz uma solicitação ao UserInfo Endpoint, fornecendo o token de acesso, e recebe informações adicionais de identidade, se autorizado.

6. Discovery Endpoint: É um endpoint fornecido pelo servidor de autorização para permitir que os clientes descubram as informações de configuração necessárias para interagir com o provedor de identidade. Ele fornece detalhes como URLs dos endpoints, tipos de suporte para autenticação e outras informações relevantes.

O OpenID Connect oferece benefícios como simplificação da autenticação e autorização, interoperabilidade entre provedores de identidade e clientes, suporte a autenticação social (por exemplo, login com contas do Google ou Facebook) e integração fácil com aplicativos e serviços existentes.

Ao usar o OpenID Connect, os clientes podem confiar na autenticação e nas informações de identidade fornecidas pelo provedor de identidade, em vez de gerenciar a autenticação internamente. Isso simplifica o processo de autenticação e permite que os usuários utilizem suas credenciais existentes para acessar vários aplicativos e serviços de forma segura e conveniente.
