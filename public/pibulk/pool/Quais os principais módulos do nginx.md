# Quais os principais módulos do nginx?

O Nginx é um servidor web e proxy reverso altamente modular, com uma arquitetura flexível que permite adicionar funcionalidades por meio de módulos. Abaixo estão alguns dos principais módulos do Nginx:

1. **HttpCoreModule**: É o módulo central do Nginx que define o comportamento básico do servidor.

2. **HttpProxyModule**: Fornece recursos de proxy reverso, permitindo ao Nginx atuar como um intermediário entre clientes e servidores web.

3. **HttpSslModule**: Adiciona suporte para criptografia SSL/TLS, permitindo a comunicação segura entre o servidor e os clientes.

4. **HttpRewriteModule**: Permite a reescrita de URLs, redirecionamento e manipulação de solicitações HTTP com base em regras personalizadas.

5. **HttpGzipModule**: Habilita a compressão Gzip de conteúdo para melhorar a eficiência da transferência de dados entre o servidor e os clientes.

6. **HttpAccessModule**: Permite configurar regras de acesso e controle de autenticação para proteger diretórios e páginas com senhas e restrições de acesso.

7. **HttpHeadersModule**: Permite a manipulação de cabeçalhos HTTP, incluindo a adição, remoção e modificação de cabeçalhos em solicitações e respostas.

8. **HttpRealIpModule**: Permite a substituição do endereço IP do cliente com base em cabeçalhos proxy, para que os logs e configurações considerem o IP real do cliente.

9. **HttpSecureLinkModule**: Fornece recursos de link seguro, permitindo a criação de URLs com tempo de vida limitado e verificação de integridade.

10. **HttpUpstreamModule**: Fornece recursos para balanceamento de carga e distribuição de solicitações entre servidores backend.

Esses são apenas alguns dos principais módulos disponíveis no Nginx. Existem muitos outros módulos que podem ser adicionados para adicionar funcionalidades específicas, como cache, autenticação, streaming de mídia, entre outros. A modularidade do Nginx permite que os administradores personalizem e ajustem o servidor de acordo com suas necessidades específicas.
