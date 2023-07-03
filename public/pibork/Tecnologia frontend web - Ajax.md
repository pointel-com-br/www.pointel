# Tecnologia frontend web - Ajax

Ajax (Asynchronous JavaScript and XML) é uma tecnologia que permite realizar chamadas assíncronas a um servidor web para buscar ou enviar dados, sem a necessidade de recarregar toda a página. Com o Ajax, é possível criar aplicações web mais interativas, rápidas e responsivas, proporcionando uma experiência de usuário aprimorada.

Aqui estão alguns conceitos e recursos importantes relacionados ao Ajax:

1. Chamadas assíncronas: Ao contrário das chamadas síncronas, em que a página é recarregada completamente ao fazer uma requisição ao servidor, o Ajax permite que as chamadas sejam feitas de forma assíncrona, em segundo plano. Isso significa que é possível enviar ou buscar dados do servidor sem interromper a interação do usuário com a página.

2. XMLHttpRequest: O objeto XMLHttpRequest é a base do Ajax. Ele permite criar uma requisição HTTP para enviar e receber dados do servidor. O JavaScript é usado para manipular esse objeto, definindo os parâmetros da requisição, como método (GET, POST, etc.), URL e manipuladores de eventos para tratar as respostas do servidor.

3. Manipulação de dados: Com o Ajax, é possível enviar dados para o servidor e receber dados em diferentes formatos, como XML, JSON (JavaScript Object Notation) ou até mesmo texto simples. Esses dados podem ser processados e manipulados no lado do cliente, permitindo atualizações dinâmicas de conteúdo na página sem a necessidade de recarregá-la por completo.

4. Atualizações parciais: Uma das principais vantagens do Ajax é a capacidade de atualizar partes específicas de uma página, em vez de recarregar toda a página. Isso permite criar interfaces mais dinâmicas, onde apenas os elementos relevantes são atualizados conforme necessário, resultando em uma experiência de usuário mais rápida e fluída.

5. Manipulação de eventos: O JavaScript é utilizado para manipular os eventos relacionados às chamadas Ajax, como o envio da requisição, o recebimento da resposta e o tratamento de erros. É possível definir funções de callback que são executadas em diferentes estágios do processo, permitindo que você atualize a interface do usuário de acordo com o progresso da requisição.

6. Frameworks e bibliotecas: Existem vários frameworks e bibliotecas JavaScript, como jQuery, Axios e Fetch API, que simplificam o uso do Ajax, fornecendo abstrações e métodos convenientes para realizar chamadas assíncronas. Essas ferramentas oferecem uma sintaxe mais simples e recursos adicionais para facilitar o desenvolvimento frontend com Ajax.

O Ajax revolucionou o desenvolvimento web ao permitir a criação de aplicações mais interativas e responsivas. Com ele, é possível buscar dados do servidor de forma assíncrona, atualizar partes específicas da página e melhorar a experiência do usuário.

## Quais os estados do XMLHttpRequest?

O objeto XMLHttpRequest (XHR) é usado em JavaScript para fazer requisições HTTP assíncronas a um servidor web. Durante o ciclo de vida de uma requisição, o objeto XHR passa por vários estados diferentes, que são representados pela propriedade `readyState`. Aqui estão os diferentes estados do XMLHttpRequest:

1. `0 - UNSENT`: O objeto XHR foi criado, mas o método `open()` não foi chamado ainda.

2. `1 - OPENED`: O método `open()` foi chamado. Neste estado, você pode configurar os cabeçalhos da requisição usando o método `setRequestHeader()`.

3. `2 - HEADERS_RECEIVED`: O método `send()` foi chamado e os cabeçalhos da resposta estão disponíveis. Você pode acessar os cabeçalhos da resposta através do método `getAllResponseHeaders()`.

4. `3 - LOADING`: A resposta está sendo recebida. Neste estado, você pode acessar partes da resposta em andamento usando o método `responseText` ou `responseXML`.

5. `4 - DONE`: A operação foi concluída e a resposta está pronta. Neste estado, você pode acessar a resposta completa usando o método `responseText` ou `responseXML`. Além disso, você pode verificar o código de status da resposta usando a propriedade `status`.

Durante o ciclo de vida da requisição, você pode acompanhar esses estados verificando a propriedade `readyState` do objeto XMLHttpRequest. Você também pode adicionar um evento `readystatechange` para ser notificado quando o estado da requisição mudar.

É importante observar que a propriedade `readyState` não é suficiente para determinar se a requisição foi bem-sucedida ou não. É necessário também verificar o código de status da resposta (propriedade `status`) para obter informações adicionais sobre o resultado da requisição.
