# Servidor web e de aplicação - Wildfly

WildFly é um servidor de aplicação de código aberto desenvolvido pela Red Hat, que é uma implementação do Java Enterprise Edition (Java EE). Ele é baseado no projeto JBoss Application Server, mas com um novo nome e versões atualizadas.

O WildFly é projetado para hospedar e executar aplicativos Java EE em um ambiente empresarial. Ele oferece suporte a um conjunto completo de especificações do Java EE, como servlets, JavaServer Pages (JSP), Enterprise JavaBeans (EJB), Java Persistence API (JPA), Java Message Service (JMS), entre outros.

Aqui estão algumas características e recursos-chave do WildFly:

1. Suporte Java EE: O WildFly oferece suporte às especificações Java EE, permitindo que os desenvolvedores criem aplicativos corporativos escaláveis e robustos.

2. Administração e monitoramento: Ele fornece uma interface de administração baseada na web, chamada de Console de Administração do WildFly, que permite configurar, implantar e gerenciar aplicativos e recursos do servidor. Além disso, o WildFly oferece recursos de monitoramento para monitorar o desempenho e a saúde do servidor.

3. Modularidade: O WildFly é construído com uma arquitetura modular, permitindo que os administradores selecionem apenas os recursos necessários para seus aplicativos. Isso ajuda a otimizar a utilização de recursos e simplificar a configuração.

4. Implantação rápida: O WildFly suporta implantação rápida de aplicativos, permitindo que você faça alterações nos aplicativos implantados sem reiniciar o servidor. Isso é útil para facilitar o processo de desenvolvimento e implementação contínua.

5. Alta disponibilidade e escalabilidade: O WildFly oferece recursos para criar ambientes altamente disponíveis e escaláveis, como clustering e balanceamento de carga. Isso permite distribuir a carga de trabalho entre vários nós do servidor e garantir a disponibilidade do aplicativo mesmo em caso de falha.

6. Integração com outras tecnologias: Além do suporte às especificações do Java EE, o WildFly também pode ser integrado a outras tecnologias, como Spring Framework e Hibernate, permitindo aos desenvolvedores aproveitar os recursos dessas tecnologias em conjunto com o Java EE.

Em resumo, o WildFly é uma opção popular para hospedar aplicativos Java EE em um ambiente empresarial. Ele oferece um conjunto abrangente de recursos, suporte às especificações Java EE e ferramentas de administração e monitoramento para facilitar o desenvolvimento, implantação e gerenciamento de aplicativos corporativos.

## Principais configurações do Wildfly

O WildFly, anteriormente conhecido como JBoss, é um servidor de aplicação Java de código aberto e amplamente utilizado. Ele oferece várias configurações e recursos para hospedar aplicativos Java EE e Spring. Aqui estão algumas das principais configurações do WildFly:

1. Arquivo de configuração standalone.xml: O arquivo standalone.xml é o arquivo de configuração principal do WildFly. Ele contém configurações para os subsistemas do servidor, como servidores da web, recursos de banco de dados, segurança, EJB, JMS e muito mais. Você pode personalizar esse arquivo para ajustar as configurações do servidor conforme necessário.

2. Datasources: O WildFly oferece suporte a configuração de datasources, que são conexões com bancos de dados. Você pode definir as propriedades do datasource, como URL do banco de dados, nome de usuário, senha, pool de conexões, validação e outras opções de configuração.

3. Configurações de segurança: O WildFly possui recursos de segurança robustos. Você pode configurar autenticação e autorização baseadas em contêiner usando o módulo JAAS (Java Authentication and Authorization Service). Além disso, você pode configurar SSL/TLS para comunicação segura.

4. Deployments: O WildFly permite implantar seus aplicativos Java EE e Spring de forma fácil e flexível. Você pode fazer o deploy de um arquivo .war, .ear ou .jar diretamente para o servidor. O WildFly também suporta hot deployment, onde as alterações nos arquivos do aplicativo são automaticamente refletidas no servidor sem a necessidade de reinicialização.

5. Logging: O WildFly fornece recursos de registro para ajudar na depuração e monitoramento de aplicativos. Você pode configurar o nível de log, destinos de log, formatos de log e outros parâmetros relacionados ao logging.

6. Clustering e balanceamento de carga: O WildFly suporta recursos avançados de clustering e balanceamento de carga. Você pode configurar várias instâncias do servidor WildFly para trabalhar em conjunto, compartilhando a carga de trabalho e garantindo alta disponibilidade e escalabilidade.

7. Gerenciamento remoto: O WildFly oferece recursos de gerenciamento remoto, permitindo que você gerencie e monitore o servidor a partir de uma máquina remota. Você pode usar a interface de gerenciamento baseada na web ou comandos CLI (Command Line Interface) para realizar tarefas de gerenciamento.

Essas são apenas algumas das principais configurações do WildFly. O servidor oferece muitos recursos e opções de configuração adicionais para atender às necessidades dos aplicativos Java EE e Spring. Consulte a documentação oficial do WildFly para obter informações detalhadas sobre as configurações específicas e como ajustá-las de acordo com suas necessidades.

## Como se configura HTTPS no Wildfly

Para configurar o suporte a HTTPS no WildFly, você precisará gerar ou obter um certificado SSL/TLS válido e configurar o servidor para usá-lo. Aqui está um guia geral para configurar o HTTPS no WildFly:

Passo 1: Obtenha um certificado SSL/TLS
- Você pode obter um certificado SSL/TLS válido de uma Autoridade de Certificação (CA) reconhecida ou usar um certificado autoassinado para fins de desenvolvimento ou teste.

Passo 2: Importe o certificado no Keystore do Java
- Converta o certificado em um formato apropriado, como o formato PKCS12 ou JKS.
- Use a ferramenta "keytool" do Java para importar o certificado no keystore.
- Por exemplo, para importar um certificado no formato PKCS12 para o keystore JKS padrão, você pode usar o seguinte comando:
```
keytool -importkeystore -srckeystore cert.p12 -srcstoretype PKCS12 -destkeystore keystore.jks -deststoretype JKS
```

Passo 3: Configure o HTTPS no WildFly
- Abra o arquivo de configuração standalone.xml (ou domain.xml, se estiver usando o modo de domínio) do WildFly.
- Localize a seção de configuração do servidor HTTP no arquivo. Ela está dentro do elemento `<subsystem xmlns="urn:jboss:domain:undertow:7.0">`.
- Dentro da seção `<server>` ou `<https-listener>` (dependendo da versão do WildFly), adicione ou modifique as seguintes propriedades:
```
<https-listener name="https" socket-binding="https" security-realm="ssl-realm"/>
```
- No mesmo arquivo, adicione a seção `<security-realm>` para configurar as propriedades de segurança do SSL/TLS:
```
<security-realm name="ssl-realm">
    <server-identities>
        <ssl>
            <keystore path="caminho/para/keystore.jks" relative-to="jboss.server.config.dir" keystore-password="senha-do-keystore" alias="alias-do-certificado" key-password="senha-da-chave"/>
        </ssl>
    </server-identities>
</security-realm>
```

Passo 4: Reinicie o WildFly
- Reinicie o servidor WildFly para que as configurações de HTTPS entrem em vigor.

Depois de configurar o HTTPS, você poderá acessar seu aplicativo WildFly usando a URL com HTTPS (por exemplo, `https://seuapp.com`).

Lembre-se de substituir os valores dos caminhos, senhas e aliases pelas informações corretas do seu certificado e keystore.

Este é um exemplo básico de configuração HTTPS no WildFly. Dependendo das suas necessidades e ambiente, pode ser necessário ajustar outras configurações, como o protocolo SSL/TLS, as versões de criptografia e as opções de segurança adicionais. Consulte a documentação oficial do WildFly para obter informações mais detalhadas sobre a configuração HTTPS no seu ambiente específico.
