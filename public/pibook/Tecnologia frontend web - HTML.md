# Tecnologia frontend web - HTML

HTML (Hypertext Markup Language) é uma linguagem de marcação utilizada para estruturar e exibir o conteúdo de uma página web. É a base fundamental de qualquer aplicação web e fornece a estrutura para a criação dos elementos da página, como textos, imagens, links e formulários.

Aqui estão alguns conceitos e recursos importantes relacionados ao HTML:

1. Tags HTML: As tags HTML são usadas para marcar os diferentes elementos de uma página web. Cada tag é definida por um nome delimitado por "<>" e, em alguns casos, possui atributos que fornecem informações adicionais sobre o elemento. Por exemplo, a tag "<h1>" é usada para criar um cabeçalho de nível 1, enquanto a tag "<img>" é usada para inserir uma imagem na página.

2. Estrutura básica do documento HTML: Um documento HTML geralmente começa com a declaração do tipo de documento (<!DOCTYPE html>) seguida pela tag "<html>", que engloba todo o conteúdo da página. Dentro da tag "<html>", há as tags "<head>" e "<body>". A tag "<head>" é usada para fornecer metadados, como o título da página e referências a arquivos CSS e JavaScript. A tag "<body>" contém o conteúdo visível da página, como texto, imagens e outros elementos.

3. Elementos de texto: Existem várias tags HTML usadas para estruturar o texto na página. Por exemplo, as tags "<h1>" a "<h6>" são usadas para títulos de diferentes níveis, sendo "<h1>" o mais importante e "<h6>" o menos importante. As tags "<p>" são usadas para parágrafos de texto, "<strong>" e "<em>" são usadas para destacar o texto em negrito e itálico, respectivamente, e assim por diante.

4. Links e âncoras: A tag "<a>" é usada para criar links em uma página HTML. O atributo "href" especifica o URL de destino do link. Além disso, é possível usar âncoras ("<a name='nome'></a>") para criar links internos dentro de uma página. Dessa forma, os usuários podem ser direcionados para uma parte específica da página clicando em um link.

5. Imagens: A tag "<img>" é usada para inserir imagens em uma página HTML. O atributo "src" especifica o caminho ou URL da imagem, e outros atributos, como "alt" e "title", fornecem descrições ou textos alternativos que são exibidos quando a imagem não pode ser carregada.

6. Formulários: O HTML também fornece elementos para criar formulários interativos, como campos de entrada de texto ("<input type='text'>"), botões ("<button>") e seletores ("<select>"). Os dados inseridos em um formulário podem ser enviados para um servidor para processamento usando a tag "<form>" e o atributo "action".

Esses são apenas alguns conceitos básicos relacionados ao HTML. Existem muitos outros elementos, atributos e recursos que podem ser explorados para criar páginas web mais complexas e interativas. O HTML trabalha em conjunto com CSS e JavaScript para fornecer uma experiência completa de desenvolvimento frontend.

## Como declarar um manifesto de cache em HTML

Para declarar um manifesto de cache em HTML, você pode usar a especificação do Manifesto de Aplicativo Web (Web App Manifest) fornecida pela Web Application Manifest specification. O Manifesto de Aplicativo Web é um arquivo JSON que descreve as características e configurações de um aplicativo web progressivo (PWA). Ele inclui informações como o nome do aplicativo, ícones, cores de tema, orientação de tela e também pode especificar arquivos para serem armazenados em cache.

Aqui está um exemplo básico de como declarar um manifesto de cache em HTML:

1. Crie um arquivo JSON chamado `manifest.json` com as configurações desejadas. Por exemplo:

```json
{
  "name": "Meu PWA",
  "short_name": "PWA",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "icons": [
    {
      "src": "/path/to/icon.png",
      "sizes": "192x192",
      "type": "image/png"
    }
  ],
  "cache": [
    "/path/to/file1.css",
    "/path/to/file2.js"
  ]
}
```

2. Em seu arquivo HTML, adicione a seguinte tag `<link>` no cabeçalho para especificar o manifesto:

```html
<link rel="manifest" href="/path/to/manifest.json">
```

Certifique-se de substituir `/path/to/` pelos caminhos corretos em seu servidor.

Ao adicionar a tag `<link>` com o atributo `rel` definido como "manifest" e o atributo `href` apontando para o caminho do arquivo `manifest.json`, você está indicando ao navegador que o arquivo JSON especificado contém o manifesto do aplicativo web. O navegador usará essas informações para configurar o PWA e armazenar em cache os arquivos listados na propriedade "cache" do manifesto.

Lembre-se de que o suporte a PWAs e a capacidade de armazenamento em cache podem variar entre diferentes navegadores e versões. É sempre uma boa prática verificar a compatibilidade com os navegadores-alvo e testar o comportamento do cache em diferentes cenários.

## Como declarar um manifesto de cache para trabalhar com arquivos offline em HTML

Para declarar um manifesto de cache em HTML e permitir que seu site funcione offline, você pode usar o recurso de Cache de Aplicativo Web HTML5 (HTML5 Application Cache). O Cache de Aplicativo Web permite que você especifique quais arquivos do seu site devem ser armazenados em cache pelo navegador, permitindo o acesso offline a esses arquivos.

Aqui está um exemplo básico de como declarar um manifesto de cache em HTML:

1. Crie um arquivo de texto chamado `manifest.appcache`. Este arquivo deve ter a extensão `.appcache`.

2. Dentro do arquivo `manifest.appcache`, liste os arquivos que você deseja armazenar em cache, incluindo HTML, CSS, JavaScript, imagens e outros recursos estáticos. Por exemplo:

```
CACHE MANIFEST
# Versão do manifesto: v1.0

CACHE:
index.html
styles.css
script.js
image.jpg

NETWORK:
*

FALLBACK:
```

- A seção `CACHE:` lista os arquivos que serão armazenados em cache.
- A seção `NETWORK:` especifica quais recursos devem ser acessados ​​pela rede (online). O caractere curinga `*` indica que todos os recursos serão buscados na rede.
- A seção `FALLBACK:` pode ser usada para fornecer fallbacks para recursos específicos, caso eles não estejam disponíveis offline.

3. Em seu arquivo HTML, adicione a seguinte tag `<html>` no cabeçalho para especificar o manifesto:

```html
<!DOCTYPE html>
<html manifest="/path/to/manifest.appcache">
<head>
  <!-- Seu cabeçalho HTML -->
</head>
<body>
  <!-- Conteúdo do seu site -->
</body>
</html>
```

Certifique-se de substituir `/path/to/` pelo caminho correto em seu servidor.

Ao adicionar o atributo `manifest` à tag `<html>` e especificar o caminho para o arquivo `manifest.appcache`, você está indicando ao navegador que esse arquivo é o manifesto de cache para o seu site. O navegador usará as informações contidas no manifesto para armazenar em cache os arquivos listados na seção `CACHE` e permitir o acesso offline a esses recursos.

Lembre-se de que o uso do Cache de Aplicativo Web HTML5 está sendo descontinuado em favor das Service Workers e das APIs de Cache de Armazenamento. Recomenda-se explorar essas tecnologias mais recentes para fornecer recursos offline em seus aplicativos da web.

## Quais as principais tags do HTML

O HTML (HyperText Markup Language) possui várias tags que são usadas para estruturar e formatar o conteúdo de uma página da web. Aqui estão algumas das principais tags do HTML:

1. `<html>`: Define o início e o fim de um documento HTML.
2. `<head>`: Contém informações sobre o documento HTML, como o título, meta informações e referências a arquivos externos.
3. `<body>`: Contém todo o conteúdo visível da página, como texto, imagens, links e outros elementos.
4. `<h1>` a `<h6>`: Define os cabeçalhos de nível 1 a 6, onde `<h1>` é o maior e `<h6>` é o menor.
5. `<p>`: Define um parágrafo de texto.
6. `<a>`: Cria um link para outra página ou recurso. O atributo `href` especifica o destino do link.
7. `<img>`: Insere uma imagem na página. O atributo `src` especifica o URL da imagem.
8. `<ul>` e `<li>`: Cria uma lista não ordenada. Os itens da lista são definidos dentro das tags `<li>`.
9. `<ol>` e `<li>`: Cria uma lista ordenada. Os itens da lista são definidos dentro das tags `<li>`.
10. `<div>`: Cria um bloco genérico que pode ser usado para agrupar elementos e aplicar estilos.
11. `<span>`: Cria um elemento em linha para aplicar estilos ou agrupar elementos em uma linha.
12. `<table>`, `<tr>`, `<td>`: Cria uma tabela com linhas (`<tr>`) e células (`<td>`).
13. `<form>`, `<input>`, `<button>`: Cria um formulário com campos de entrada e um botão de envio.
14. `<header>`, `<nav>`, `<footer>`: Define as seções de cabeçalho, navegação e rodapé de uma página.
15. `<section>`, `<article>`, `<aside>`: Define seções, artigos e conteúdo relacionado em uma página.

Essas são apenas algumas das principais tags do HTML. Existem muitas outras tags disponíveis para diferentes finalidades, como formatação de texto, inclusão de vídeos, áudio, estilos CSS e muito mais. É importante consultar a documentação oficial do HTML ou recursos adicionais para obter uma lista completa das tags e sua utilização adequada.

## Quais as principais tags do HTML para edição

Se você está se referindo a tags do HTML para criar um editor de texto ou fornecer recursos de edição de texto em um site, aqui estão algumas das principais tags que podem ser usadas:

1. `<textarea>`: Cria uma área de texto editável onde os usuários podem inserir e editar texto.
2. `<input type="text">`: Cria uma caixa de texto simples onde os usuários podem inserir e editar texto.
3. `<input type="password">`: Cria uma caixa de texto onde o texto digitado é ocultado, como em campos de senha.
4. `<input type="email">`: Cria uma caixa de texto para inserir endereços de e-mail, com validação específica para endereços de e-mail.
5. `<input type="number">`: Cria uma caixa de texto para inserir valores numéricos, com validação específica para números.
6. `<input type="date">`: Cria um campo para inserir datas, com um seletor de calendário.
7. `<input type="checkbox">`: Cria uma caixa de seleção que permite aos usuários marcar/desmarcar uma opção.
8. `<input type="radio">`: Cria botões de opção onde apenas uma opção pode ser selecionada de um grupo de opções.
9. `<select>` e `<option>`: Cria uma lista suspensa (dropdown) onde os usuários podem selecionar uma opção de um conjunto pré-definido.
10. `<button>`: Cria um botão que pode ser usado para executar ações, como enviar um formulário ou executar um script.
11. `<label>`: Associa um rótulo de texto a um elemento de entrada, fornecendo uma descrição ou instrução.
12. `<strong>` e `<em>`: Aplicam ênfase ao texto, com `<strong>` indicando ênfase forte e `<em>` indicando ênfase enfática.
13. `<b>` e `<i>`: Aplicam negrito (`<b>`) e itálico (`<i>`) ao texto, respectivamente.
14. `<u>`: Sublinha o texto.
15. `<s>`: Aplica uma linha horizontal através do texto, indicando que está riscado.

Essas são apenas algumas das principais tags do HTML que podem ser usadas para recursos de edição de texto em um site. Além dessas, existem várias outras tags e atributos que podem ser explorados dependendo das necessidades específicas de edição de texto em seu projeto.
