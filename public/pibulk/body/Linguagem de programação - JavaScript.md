# Linguagem de programação - JavaScript

JavaScript é uma linguagem de programação de alto nível, interpretada e orientada a objetos. Ela é amplamente utilizada para desenvolvimento web, permitindo a criação de interatividade e dinamismo nas páginas da web. Aqui estão algumas informações importantes sobre JavaScript:

1. Desenvolvimento web: JavaScript é a principal linguagem de programação usada para desenvolver aplicativos web interativos. Ela é executada no navegador do cliente e permite a manipulação do conteúdo HTML, estilização CSS e interação com o usuário por meio de eventos, validações de formulários, animações, entre outros recursos.

2. Suporte ao lado do cliente e do servidor: Além de ser executada no navegador do cliente, o JavaScript também pode ser usado no lado do servidor com o auxílio de plataformas como o Node.js. Isso permite que os desenvolvedores escrevam aplicativos web completos usando JavaScript em ambos os lados, facilitando a criação de aplicativos em tempo real, APIs e serviços web.

3. Orientação a objetos: JavaScript é uma linguagem orientada a objetos, suportando conceitos como objetos, classes, herança e polimorfismo. No entanto, a abordagem de orientação a objetos em JavaScript é baseada em protótipos, em vez de classes tradicionais.

4. Bibliotecas e frameworks: JavaScript possui uma ampla variedade de bibliotecas e frameworks populares, como jQuery, React, Angular, Vue.js e muitos outros. Essas bibliotecas e frameworks fornecem funcionalidades e recursos adicionais para facilitar o desenvolvimento de aplicativos web complexos.

5. Integração com HTML e CSS: JavaScript pode ser facilmente incorporado em documentos HTML, permitindo a manipulação dinâmica do conteúdo e estilos. Ele permite que os desenvolvedores acessem elementos da página, modifiquem seu conteúdo, estilo e comportamento, além de responder a eventos do usuário.

6. Ecossistema ativo e comunidade vibrante: JavaScript possui uma comunidade de desenvolvedores extremamente ativa e um ecossistema rico. Há uma grande quantidade de recursos, bibliotecas, frameworks, tutoriais e documentação disponíveis para ajudar os desenvolvedores a aprender e expandir seus conhecimentos em JavaScript.

JavaScript desempenha um papel fundamental no desenvolvimento web moderno. Sua capacidade de criar interatividade e dinamismo nas páginas da web, juntamente com seu suporte em ambientes cliente e servidor, torna-o uma linguagem essencial para desenvolvedores web. Com sua ampla adoção e recursos avançados, JavaScript permite a criação de experiências interativas e envolventes na web.

## Linguagem de programação - JavaScript - Lista das 10 principais funções com Strings

Aqui estão as 10 principais funções para manipulação de strings em JavaScript:

1. length: Retorna o comprimento de uma string.
```javascript
const texto = "Olá, mundo!";
console.log(texto.length); // Saída: 12
```

2. indexOf: Retorna a posição da primeira ocorrência de um caractere ou substring em uma string. Retorna -1 se a substring não for encontrada.
```javascript
const texto = "Olá, mundo!";
console.log(texto.indexOf("mundo")); // Saída: 5
```

3. slice: Extrai uma parte de uma string com base nos índices especificados.
```javascript
const texto = "Olá, mundo!";
console.log(texto.slice(0, 3)); // Saída: "Olá"
```

4. substring: Similar ao slice, mas não permite índices negativos.
```javascript
const texto = "Olá, mundo!";
console.log(texto.substring(4, 9)); // Saída: "mundo"
```

5. replace: Substitui uma substring por outra em uma string.
```javascript
const texto = "Olá, mundo!";
console.log(texto.replace("mundo", "planeta")); // Saída: "Olá, planeta!"
```

6. toUpperCase: Converte uma string em letras maiúsculas.
```javascript
const texto = "Olá, mundo!";
console.log(texto.toUpperCase()); // Saída: "OLÁ, MUNDO!"
```

7. toLowerCase: Converte uma string em letras minúsculas.
```javascript
const texto = "Olá, mundo!";
console.log(texto.toLowerCase()); // Saída: "olá, mundo!"
```

8. trim: Remove espaços em branco no início e no final de uma string.
```javascript
const texto = " Olá, mundo! ";
console.log(texto.trim()); // Saída: "Olá, mundo!"
```

9. charAt: Retorna o caractere em uma determinada posição em uma string.
```javascript
const texto = "Olá, mundo!";
console.log(texto.charAt(1)); // Saída: "l"
```

10. split: Divide uma string em um array de substrings com base em um separador especificado.
```javascript
const texto = "Olá, mundo!";
console.log(texto.split(" ")); // Saída: ["Olá,", "mundo!"]
```

Essas são 10 das principais funções para manipulação de strings em JavaScript. No entanto, a linguagem possui muitas outras funções e métodos úteis para trabalhar com strings, dependendo do cenário de programação em que você está envolvido.

## Linguagem de programação - JavaScript - Lista das principais funções para verificações de Strings

Aqui estão algumas das principais funções em JavaScript para realizar verificações em strings:

1. startsWith: Verifica se uma string começa com determinados caracteres.
```javascript
const texto = "Olá, mundo!";
console.log(texto.startsWith("Olá")); // Saída: true
console.log(texto.startsWith("mundo")); // Saída: false
```

2. endsWith: Verifica se uma string termina com determinados caracteres.
```javascript
const texto = "Olá, mundo!";
console.log(texto.endsWith("mundo!")); // Saída: true
console.log(texto.endsWith("Olá")); // Saída: false
```

3. includes: Verifica se uma string contém uma determinada substring.
```javascript
const texto = "Olá, mundo!";
console.log(texto.includes("mundo")); // Saída: true
console.log(texto.includes("Planeta")); // Saída: false
```

4. match: Realiza uma correspondência de uma string com uma expressão regular.
```javascript
const texto = "Olá, mundo!";
const regex = /mundo/;
console.log(texto.match(regex)); // Saída: ["mundo"]
```

5. search: Pesquisa por uma expressão regular em uma string e retorna a posição da primeira ocorrência.
```javascript
const texto = "Olá, mundo!";
const regex = /mundo/;
console.log(texto.search(regex)); // Saída: 5
```

6. matchAll: Retorna um iterador com todas as correspondências de uma expressão regular em uma string.
```javascript
const texto = "Olá, mundo! Olá, planeta!";
const regex = /Olá/g;
const matches = [...texto.matchAll(regex)];
console.log(matches); // Saída: [ ["Olá"], ["Olá"] ]
```

7. test: Testa se uma string corresponde a uma expressão regular e retorna true ou false.
```javascript
const texto = "Olá, mundo!";
const regex = /mundo/;
console.log(regex.test(texto)); // Saída: true
```

8. isNaN: Verifica se uma string não é um número.
```javascript
console.log(isNaN("123")); // Saída: false
console.log(isNaN("abc")); // Saída: true
```

Essas são algumas das principais funções em JavaScript para realizar verificações em strings. Existem muitas outras funções e métodos disponíveis para manipulação e verificação de strings na linguagem, dependendo das necessidades específicas do seu código.

## Linguagem de programação - JavaScript - Como usar o map e o filter

Em JavaScript, as funções `map()` e `filter()` são métodos de array muito úteis para trabalhar com listas de elementos e aplicar transformações ou filtrar os elementos com base em determinados critérios. Aqui está como usá-los:

1. `map()`: O método `map()` cria um novo array com os resultados de chamar uma função de callback em cada elemento do array original. Ele retorna um novo array com o mesmo tamanho do array original, onde cada elemento é o resultado da função de callback aplicada ao elemento correspondente do array original.

Exemplo de uso do `map()`:
```javascript
const numeros = [1, 2, 3, 4, 5];

const dobrados = numeros.map((numero) => {
return numero * 2;
});

console.log(dobrados); // Saída: [2, 4, 6, 8, 10]
```

Neste exemplo, o `map()` é usado para criar um novo array chamado `dobrados`, onde cada elemento é o dobro do elemento correspondente no array `numeros`.

2. `filter()`: O método `filter()` cria um novo array com todos os elementos que passam em um teste especificado por uma função de callback. Ele retorna um novo array contendo apenas os elementos do array original que atendem à condição definida na função de callback.

Exemplo de uso do `filter()`:

    ```javascript
        const numeros = [1, 2, 3, 4, 5];

        const pares = numeros.filter((numero) => {
            return numero % 2 === 0;
        });

        console.log(pares); // Saída: [2, 4]
    ```

Neste exemplo, o `filter()` é usado para criar um novo array chamado `pares`, que contém apenas os números pares do array original `numeros`. A função de callback retorna `true` para os elementos que são divisíveis por 2 (ou seja, números pares) e `false` para os elementos que não são divisíveis por 2.

Ambos `map()` e `filter()` são métodos poderosos para manipular arrays em JavaScript. Eles permitem que você transforme os elementos de um array ou filtre-os com facilidade, respectivamente. Além disso, esses métodos são não-destrutivos, ou seja, eles não modificam o array original, mas retornam um novo array com os resultados.

## Como são feitos testes unitários em JavaScript

Os testes unitários em JavaScript podem ser feitos usando frameworks de teste populares, como Jest, Mocha, Jasmine e QUnit. Esses frameworks fornecem uma estrutura para escrever e executar testes automatizados no ambiente JavaScript. Aqui está um exemplo básico de como criar e executar testes unitários em JavaScript usando o Jest:

1. Configuração do ambiente:
Certifique-se de ter o Jest configurado no seu projeto. Isso pode ser feito instalando o Jest via npm ou yarn e configurando o arquivo de configuração do Jest, geralmente chamado de `jest.config.js`.

2. Crie uma função de teste:
Escreva uma função de teste para cada função que você deseja testar. Uma função de teste é um bloco de código que executa uma ou mais asserções para verificar se o resultado está correto.

```javascript
// Importe as funções e módulos necessários
const { soma } = require('./meuModulo');

// Escreva a função de teste
test('Teste da função de soma', () => {
  // Execute a função que você deseja testar
  const resultado = soma(2, 3);

  // Verifique se o resultado está correto usando os métodos de asserção do Jest
  expect(resultado).toBe(5);
});
```

3. Execute os testes:
Execute os testes usando um comando de teste fornecido pelo framework que você está usando. Por exemplo, com o Jest, você pode executar `npx jest` no terminal para executar todos os testes no seu projeto.

Ao executar os testes, você verá os resultados indicando se cada teste passou ou falhou. Se um teste falhar, você pode usar as informações fornecidas para depurar e corrigir problemas em sua implementação.

Essas são as etapas básicas para escrever testes unitários em JavaScript usando o Jest. Cada framework de teste tem sua própria sintaxe e recursos específicos, mas a ideia geral é a mesma: definir funções de teste, executá-las e verificar se os resultados estão corretos usando asserções. Você pode explorar recursos avançados desses frameworks, como testes assíncronos, mocks e spies, para lidar com casos de teste mais complexos.

## Quais os tipos de laços de repetição do JavaScript

O JavaScript oferece várias formas de criar laços de repetição, permitindo que você execute blocos de código repetidamente. Abaixo estão os tipos de laços de repetição disponíveis em JavaScript:

1. **for**: O laço `for` é usado para iterar por uma sequência de valores por um número específico de vezes. Ele consiste em três partes: inicialização, condição e expressão final.

   ```javascript
   for (inicialização; condição; expressão final) {
       // código a ser executado
   }
   ```

2. **for...in**: O laço `for...in` é usado para iterar sobre as propriedades de um objeto. Ele percorre todas as propriedades enumeráveis do objeto.

   ```javascript
   for (variavel in objeto) {
       // código a ser executado
   }
```

3. **for...of**: O laço `for...of` é usado para iterar sobre elementos iteráveis, como arrays, strings, etc. Ele itera diretamente sobre os valores dos elementos, em vez dos índices ou chaves.

   ```javascript
   for (variavel of iteravel) {
       // código a ser executado
   }
```

4. **while**: O laço `while` é usado para repetir um bloco de código enquanto uma condição específica for verdadeira.

   ```javascript
   while (condição) {
       // código a ser executado
   }
```

5. **do...while**: O laço `do...while` é semelhante ao `while`, mas a condição é verificada após a execução do bloco de código. Isso garante que o bloco de código seja executado pelo menos uma vez.

   ```javascript
   do {
       // código a ser executado
   } while (condição);
```

Cada tipo de laço de repetição tem suas próprias características e é adequado para diferentes situações. A escolha do tipo de laço depende dos requisitos e da lógica específica do seu código.
