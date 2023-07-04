# Servidor web e de aplicação - IIS

O IIS (Internet Information Services) é um servidor web desenvolvido pela Microsoft para hospedar e fornecer serviços baseados na web. Ele é amplamente utilizado para hospedar sites e aplicativos da web em ambientes Windows. Aqui estão algumas informações importantes sobre o IIS:

1. Recursos e funcionalidades: O IIS oferece uma ampla gama de recursos e funcionalidades para hospedar aplicativos e sites da web. Isso inclui suporte para protocolos como HTTP, HTTPS, FTP, SMTP, e mais. Ele também oferece recursos avançados de segurança, como autenticação integrada do Windows, certificados SSL/TLS, restrições de acesso baseadas em IP e muito mais.

2. Plataforma Windows: O IIS é nativo da plataforma Windows e está integrado ao sistema operacional Windows Server. Isso torna o IIS uma escolha popular para empresas que utilizam a infraestrutura Windows e desejam hospedar aplicativos e sites em um ambiente familiar.

3. Integração com outras tecnologias Microsoft: O IIS é altamente integrado com outras tecnologias e produtos Microsoft, como o ASP.NET e o .NET Framework. Isso permite que os desenvolvedores criem aplicativos da web usando essas tecnologias e os hospedem no IIS com facilidade.

4. Gerenciamento e configuração: O IIS oferece uma interface de gerenciamento baseada em GUI (Interface Gráfica do Usuário), o Gerenciador do IIS, que permite configurar e gerenciar vários aspectos do servidor web. Ele também fornece ferramentas de linha de comando e APIs para automação e gerenciamento programático.

5. Desempenho e escalabilidade: O IIS é conhecido por sua eficiência e desempenho. Ele suporta recursos de balanceamento de carga e escalabilidade horizontal, permitindo distribuir a carga de trabalho entre vários servidores web para lidar com um grande número de solicitações.

6. Extensibilidade: O IIS é altamente extensível e permite a adição de módulos personalizados para fornecer funcionalidades adicionais. Esses módulos podem ser desenvolvidos pelos administradores ou por terceiros para atender a requisitos específicos.

O IIS é uma escolha comum para empresas que utilizam tecnologias Microsoft e desejam hospedar aplicativos e sites da web em seus servidores Windows. Ele oferece um conjunto abrangente de recursos, integração com outras tecnologias Microsoft e ferramentas de gerenciamento para facilitar a hospedagem e o gerenciamento de serviços web.

## Principais configurações do servidor IIS

O IIS (Internet Information Services) é um servidor web da Microsoft que é amplamente utilizado em ambientes Windows. Aqui estão algumas das principais configurações e recursos do servidor IIS:

1. Sites e aplicativos: No IIS, você pode configurar vários sites e aplicativos para hospedar diferentes projetos web. Cada site ou aplicativo pode ter configurações individuais, como nome, diretório raiz, configurações de log, entre outros.

2. Pools de aplicativos: Os pools de aplicativos no IIS são responsáveis por isolar e gerenciar os processos de aplicativos web. Você pode configurar opções de pool de aplicativos, como versão do .NET Framework, modo de pipeline, tamanho máximo de worker processes, tempo limite, entre outros.

3. Bindings: As configurações de bindings permitem definir os endereços IP, portas e protocolos nos quais os sites ou aplicativos do IIS serão acessíveis. Você pode configurar vários bindings para acomodar diferentes necessidades de hospedagem.

4. Autenticação e autorização: O IIS oferece suporte a várias opções de autenticação e autorização para proteger seus sites e aplicativos. Você pode configurar autenticação básica, autenticação do Windows, autenticação de certificado, entre outras opções. Além disso, você pode definir regras de autorização para controlar o acesso a recursos específicos.

5. URLs amigáveis e reescrita de URL: O IIS possui recursos embutidos para configurar URLs amigáveis e reescrita de URL. Você pode usar as configurações de regras de URL para direcionar solicitações de URL para manipuladores específicos ou para reescrever URLs de forma personalizada.

6. Compressão de conteúdo: O IIS oferece suporte à compressão de conteúdo para reduzir o tamanho dos arquivos transferidos pela rede. Você pode habilitar a compactação de conteúdo para tipos de arquivo específicos, como HTML, CSS, JavaScript, imagens, entre outros.

7. Logging: O IIS fornece recursos de registro detalhados para acompanhar e analisar o tráfego do servidor web. Você pode configurar as opções de registro, como o formato de log, campos registrados, diretório de log, entre outros.

Essas são apenas algumas das principais configurações do servidor IIS. O IIS também oferece recursos avançados, como balanceamento de carga, cache de saída, monitoramento de desempenho e muito mais. A interface de gerenciamento do IIS, o Internet Information Services (IIS) Manager, fornece uma interface gráfica intuitiva para configurar e gerenciar todas essas opções.

## Principais comandos de linha do servidor IIS

O servidor IIS (Internet Information Services) da Microsoft pode ser gerenciado usando a interface gráfica do IIS Manager, mas também oferece alguns comandos de linha para realizar tarefas de configuração e gerenciamento. Aqui estão alguns dos principais comandos de linha do servidor IIS:

1. `appcmd`: O comando `appcmd` é uma ferramenta de linha de comando usada para gerenciar configurações e operações do IIS. Alguns exemplos de uso são:
- Listar todos os sites: `appcmd list site`
- Listar todos os pools de aplicativos: `appcmd list apppool`
- Iniciar um site: `appcmd start site "NomeDoSite"`
- Parar um site: `appcmd stop site "NomeDoSite"`
- Reciclar um pool de aplicativos: `appcmd recycle apppool "NomeDoPool"`

2. `iisreset`: O comando `iisreset` é usado para reiniciar o serviço do IIS. Isso pode ser útil para aplicar alterações de configuração ou para resolver problemas de funcionamento do servidor. Por exemplo:
- Reiniciar o IIS: `iisreset /restart`
- Parar o IIS: `iisreset /stop`
- Iniciar o IIS: `iisreset /start`

3. `certutil`: O comando `certutil` é usado para gerenciar certificados no IIS. Você pode usá-lo para importar, exportar, exibir e gerenciar certificados SSL. Alguns exemplos de uso são:
- Exibir informações sobre um certificado: `certutil -dump "CaminhoDoCertificado"`
- Importar um certificado: `certutil -importpfx "CaminhoDoCertificado" password`
- Exportar um certificado: `certutil -exportpfx "CaminhoDoCertificado" "CaminhoDeSaida"`

4. `netsh`: O comando `netsh` é uma ferramenta de linha de comando usada para configurar várias configurações de rede, incluindo configurações do IIS. Alguns exemplos de uso são:
- Exibir informações sobre configurações do IIS: `netsh http show`
- Adicionar uma reserva de URL: `netsh http add urlacl url=URL user=USERNAME`
- Remover uma reserva de URL: `netsh http delete urlacl url=URL`

Esses são apenas alguns exemplos de comandos de linha comumente usados para gerenciar e configurar o servidor IIS. Lembre-se de que a sintaxe e os argumentos exatos podem variar dependendo da versão do IIS e do sistema operacional. É sempre uma boa prática consultar a documentação oficial da Microsoft para obter informações detalhadas sobre os comandos e configurações específicas do IIS.

## Como se configura HTTPS no IIS

Para configurar o suporte a HTTPS no IIS (Internet Information Services) da Microsoft, você precisará obter um certificado SSL/TLS válido e configurar o servidor para usá-lo. Aqui está um guia geral para configurar o HTTPS no IIS:

Passo 1: Obtenha um certificado SSL/TLS
- Você pode obter um certificado SSL/TLS válido de uma Autoridade de Certificação (CA) reconhecida ou usar um certificado autoassinado para fins de desenvolvimento ou teste.

Passo 2: Instale o certificado no servidor
- Abra o Gerenciador do IIS (Internet Information Services Manager).
- No painel esquerdo, selecione o servidor onde deseja configurar o HTTPS.
- No painel central, abra a seção "Certificados de Servidor" e clique em "Associar Certificado".
- Siga as instruções para importar o certificado no IIS. Se você estiver usando um certificado de terceiros, geralmente será necessário fornecer o arquivo .pfx contendo o certificado e a chave privada.

Passo 3: Configure o site para usar HTTPS
- No Gerenciador do IIS, navegue até o site ou aplicativo que deseja configurar para HTTPS.
- No painel central, abra a seção "Configurações de SSL".
- Selecione "Editar" e marque a opção "Exigir SSL".
- Selecione o certificado que você instalou no servidor na lista suspensa "Certificado SSL".

Passo 4: Redirecione HTTP para HTTPS (opcional)
- Se desejar redirecionar automaticamente todas as solicitações HTTP para HTTPS, você pode criar uma regra de redirecionamento.
- No Gerenciador do IIS, selecione o site ou aplicativo e abra a seção "URL Rewrite".
- Crie uma nova regra de redirecionamento com as seguintes configurações:
- Condição: {HTTPS} off
- Ação: Redirecionar para https://{HTTP_HOST}/{R:1}

Passo 5: Reinicie o IIS
- Reinicie o serviço do IIS para que as configurações de HTTPS entrem em vigor.

Após configurar o HTTPS, você poderá acessar seu site ou aplicativo IIS usando a URL com HTTPS (por exemplo, `https://seusite.com`).

Lembre-se de substituir os valores dos caminhos e nomes de arquivo pelos valores corretos do seu certificado.

Este é um exemplo básico de configuração HTTPS no IIS. Dependendo das suas necessidades e ambiente, pode ser necessário ajustar outras configurações, como as versões de SSL/TLS, as opções de criptografia e as configurações de segurança adicionais. Consulte a documentação oficial da Microsoft para obter informações mais detalhadas sobre a configuração HTTPS no seu ambiente específico.
