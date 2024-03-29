# Autenticação e autorização - OAuth 2

OAuth 2 (Open Authorization 2) é um protocolo de autorização amplamente utilizado para delegar acesso a recursos protegidos em nome de um usuário. Ele fornece uma estrutura para que os usuários autorizem aplicativos de terceiros a acessarem suas informações armazenadas em serviços online, como redes sociais, provedores de e-mail e plataformas de armazenamento em nuvem, sem compartilhar suas credenciais de login.
O OAuth 2 é projetado para ser seguro e escalável, permitindo que os usuários concedam permissões específicas a aplicativos de terceiros sem a necessidade de compartilhar suas senhas. O fluxo típico do OAuth 2 envolve três partes principais: o usuário (proprietário dos recursos), o aplicativo de terceiros (cliente) e o provedor de serviços que hospeda os recursos protegidos (servidor).

Aqui estão as principais etapas do fluxo de autenticação OAuth 2:

1. Registro do aplicativo: O desenvolvedor do aplicativo de terceiros registra o aplicativo no provedor de serviços. Isso geralmente envolve fornecer informações básicas sobre o aplicativo, como nome, URL de redirecionamento e permissões solicitadas.

2. Redirecionamento do usuário: Quando um usuário deseja conceder acesso ao aplicativo de terceiros, ele é redirecionado para o provedor de serviços para autenticação. O usuário é solicitado a fazer login em sua conta no provedor de serviços, se ainda não estiver autenticado.

3. Autorização do usuário: Após o login bem-sucedido, o provedor de serviços solicita ao usuário que autorize o acesso do aplicativo de terceiros aos recursos protegidos. O usuário revisa as permissões solicitadas pelo aplicativo e, se concordar, concede a autorização.

4. Geração do token de acesso: Após a autorização do usuário, o provedor de serviços gera um token de acesso para o aplicativo de terceiros. Esse token é usado pelo aplicativo para acessar os recursos protegidos em nome do usuário. O token de acesso é geralmente de curta duração e pode ser renovado conforme necessário.

5. Acesso aos recursos protegidos: Com o token de acesso, o aplicativo de terceiros pode fazer solicitações ao provedor de serviços para acessar os recursos protegidos. O provedor de serviços verifica o token de acesso e, se válido, fornece os recursos solicitados ao aplicativo.

O OAuth 2 é amplamente adotado e oferece várias vantagens, como a capacidade de delegar acesso granular aos recursos, permitindo que os usuários controlem quais permissões são concedidas aos aplicativos de terceiros. Além disso, ele reduz o risco de exposição de senhas, uma vez que as credenciais de login do usuário não são compartilhadas com os aplicativos de terceiros.

No entanto, é importante que os desenvolvedores implementem o OAuth 2 corretamente, seguindo as melhores práticas de segurança para proteger a integridade e a confidencialidade dos tokens de acesso. Além disso, os usuários devem estar cientes das permissões que estão concedendo ao autorizar um aplicativo de terceiros e revisar regularmente as permissões concedidas aos aplicativos em suas contas.
