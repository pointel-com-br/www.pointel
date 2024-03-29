# Web service - SOAP

Um Web service SOAP (Simple Object Access Protocol) é um serviço baseado no protocolo SOAP, que define um formato de mensagem XML estruturado para a comunicação entre sistemas distribuídos. Ele é projetado para ser independente de plataforma e linguagem, permitindo que aplicativos se comuniquem de forma padronizada.

Principais características de um Web service SOAP:

1. Formato de mensagem: As mensagens SOAP são escritas em XML (Extensible Markup Language) e possuem uma estrutura bem definida. Elas consistem em um envelope SOAP, que contém um cabeçalho opcional e um corpo obrigatório. O cabeçalho pode conter informações adicionais sobre a mensagem, como informações de autenticação ou segurança.

2. Protocolo de transporte: As mensagens SOAP podem ser transportadas por diferentes protocolos de transporte, como HTTP, SMTP ou TCP. No entanto, o protocolo HTTP é o mais comum para o transporte de mensagens SOAP pela internet.

3. Interface de descrição: Para que um cliente possa interagir com um Web service SOAP, é necessário ter acesso à sua interface de descrição. O WSDL (Web Services Description Language) é usado para descrever a interface do serviço, especificando os métodos disponíveis, seus parâmetros e tipos de dados. Isso permite que os clientes saibam como interagir corretamente com o serviço.

4. Modelos de comunicação: O Web service SOAP define dois modelos principais de comunicação: RPC (Remote Procedure Call) e Document. No modelo RPC, as mensagens SOAP são usadas para chamar métodos remotos, passando parâmetros e obtendo resultados. No modelo Document, as mensagens SOAP são usadas para trocar documentos XML estruturados.

5. Extensibilidade: O protocolo SOAP permite a extensão do formato de mensagem através do uso de elementos e atributos personalizados. Isso possibilita a adição de informações específicas do domínio ou de funcionalidades adicionais ao Web service.

Web services SOAP são amplamente utilizados em cenários empresariais, onde a segurança, confiabilidade e interoperabilidade são essenciais. Eles são compatíveis com várias tecnologias e plataformas, permitindo a integração de sistemas heterogêneos. No entanto, devido à sua complexidade e sobrecarga de XML, eles podem ser menos utilizados em cenários de desenvolvimento web mais leves e orientados a recursos.
