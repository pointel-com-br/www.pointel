# Tecnologia backend - Especificação JEE - JSP

A tecnologia backend JEE (Java Enterprise Edition) é uma plataforma de desenvolvimento para criação de aplicativos corporativos em Java. As páginas JSP (JavaServer Pages) são uma das especificações incluídas no JEE, fornecendo uma abordagem baseada em tags para criar interfaces de usuário dinâmicas.

As páginas JSP permitem a mistura de código Java com código HTML, facilitando a criação de páginas web dinâmicas. Aqui estão algumas características e recursos relacionados às páginas JSP no contexto da especificação JEE:

1. Estrutura MVC: As páginas JSP são frequentemente usadas no padrão de arquitetura MVC (Model-View-Controller) em aplicativos JEE. Elas atuam como a camada de visualização (View), onde o código Java no JSP interage com o modelo de dados (Model) e as classes de controle (Controller).

2. Suporte a tags: As páginas JSP fornecem uma variedade de tags para facilitar o desenvolvimento web. Essas tags podem ser usadas para iterar sobre coleções de dados, controlar fluxos condicionais, incluir arquivos externos, formatar datas, internacionalização, entre outros.

3. Acesso a objetos do servlet: As páginas JSP têm acesso direto a objetos e funcionalidades fornecidos pelo servlet container, como o objeto HttpServletRequest e HttpServletResponse. Isso permite a interação com os dados recebidos da solicitação HTTP e a geração da resposta apropriada.

4. Suporte a expressões e scriptlets: As páginas JSP permitem a inclusão de expressões embutidas `<%= %>` e scriptlets `<% %>` para executar código Java no contexto da página. Isso permite a manipulação de dados, chamadas de métodos e tomadas de decisão dentro do JSP.

5. Escopo de objetos: As páginas JSP suportam diferentes escopos para objetos, como request, session, application e page. Esses escopos determinam a vida útil dos objetos e sua visibilidade entre diferentes partes da aplicação.

6. Tags personalizadas: A especificação JEE permite a criação de tags personalizadas em JSP. Isso possibilita a criação de tags reutilizáveis para funcionalidades específicas, encapsulando lógica complexa em componentes personalizados.

É importante notar que, com o avanço das tecnologias web, como o surgimento de frameworks de desenvolvimento mais modernos (por exemplo, Spring Boot), o uso direto de páginas JSP tem diminuído em favor de abordagens mais modernas, como o uso de templates e engines de renderização, como o Thymeleaf ou o AngularJS. No entanto, as páginas JSP ainda são amplamente utilizadas em muitas aplicações legadas JEE.

## Principais tipos de tag de uma página JSP

As páginas JSP (JavaServer Pages) são arquivos HTML misturados com código Java que são executados no servidor para gerar páginas web dinâmicas. Existem várias tags disponíveis no JSP para ajudar no desenvolvimento dessas páginas. Aqui estão alguns dos principais tipos de tags em uma página JSP:

1. Declaração de tag (`<%@ %>`): Essa tag é usada para declarar diretivas para a página JSP, como importações de classes Java, configurações de página, entre outras.

Exemplo:
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" %>
```

2. Scriptlet tag (`<% %>`): Essa tag permite inserir código Java diretamente na página JSP. O código dentro das tags scriptlet é executado quando a página é processada no servidor.

Exemplo:
```jsp
<%
String nome = "João";
out.println("Bem-vindo, " + nome);
%>
```

3. Expressão tag (`<%= %>`): Essa tag é usada para inserir o resultado de uma expressão Java na página. O resultado é convertido em uma string e enviado ao navegador.

Exemplo:
```jsp
<p>O resultado da expressão é: <%= 2 + 2 %></p>
```

4. Tag de declaração de variável (`<%! %>`): Essa tag é usada para declarar variáveis e métodos que são acessíveis em toda a página JSP. Geralmente, é usada para definir métodos de utilidade ou variáveis que são compartilhadas entre diferentes partes da página.

Exemplo:
```jsp
<%! int contador = 0; %>
```

5. Tag de inclusão (`<%@ include %>`): Essa tag é usada para incluir o conteúdo de outro arquivo JSP ou HTML na página atual. O conteúdo do arquivo incluído é copiado diretamente para a página durante o processamento.

Exemplo:
```jsp
<%@ include file="header.jsp" %>
```

Essas são apenas algumas das principais tags utilizadas em páginas JSP. Existem outras tags disponíveis, como tags de controle de fluxo (if, switch, loop), tags JSP padrão (JSTL), tags de ação (utilizadas com o framework Struts) e tags personalizadas criadas pelos desenvolvedores. O uso de tags pode variar dependendo do framework ou bibliotecas adicionais utilizadas no projeto.
