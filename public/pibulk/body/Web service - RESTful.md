# Web service - RESTful

Um Web service RESTful (Representational State Transfer) é um estilo de arquitetura de software que permite a comunicação entre sistemas distribuídos usando os princípios do Protocolo de Transferência de Estado Representacional (HTTP). Ele é projetado para ser simples, escalável, leve e interoperável.

As principais características de um Web service RESTful são:

1. Recursos (Resources): Os recursos são os elementos fundamentais de um Web service RESTful e representam entidades ou objetos de um sistema. Eles são identificados por meio de URLs (Uniform Resource Locators) ou URIs (Uniform Resource Identifiers).

2. Métodos HTTP: Os métodos HTTP (GET, POST, PUT, DELETE) são usados para definir as operações que podem ser executadas em um recurso. Cada método possui um propósito específico:
- GET: Recupera informações de um recurso.
- POST: Cria um novo recurso.
- PUT: Atualiza um recurso existente.
- DELETE: Remove um recurso.

3. Representações: As representações são o formato em que os dados são trocados entre o cliente e o serviço web. Os formatos mais comuns são JSON (JavaScript Object Notation) e XML (Extensible Markup Language). O cliente pode especificar o formato preferido por meio do cabeçalho "Accept" na solicitação HTTP.

4. Stateless (Sem Estado): Um Web service RESTful é stateless, o que significa que cada solicitação para o serviço contém todas as informações necessárias para ser processada. O serviço não mantém nenhum estado sobre o cliente, o que torna a comunicação mais simples e escalável.

5. Hipertexto como motor de estado (HATEOAS): O princípio HATEOAS sugere que o serviço forneça links navegáveis que representem as transições de estado possíveis. Isso permite que o cliente descubra dinamicamente as ações disponíveis e navegue pela API de forma autônoma.

6. Cache: O uso de cache é incentivado em um Web service RESTful para melhorar o desempenho e a escalabilidade. O serviço pode enviar cabeçalhos de resposta HTTP para indicar se uma resposta pode ser armazenada em cache pelo cliente ou por intermediários.

Web services RESTful são amplamente utilizados na construção de APIs (Interfaces de Programação de Aplicativos) para aplicativos web, móveis e outros sistemas distribuídos. Eles oferecem uma abordagem flexível e leve para a comunicação entre sistemas, permitindo a interoperabilidade entre diferentes plataformas e linguagens de programação.
