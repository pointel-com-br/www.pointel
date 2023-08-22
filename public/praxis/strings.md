# Strings

- [Strings](#strings)
  - [JavaScript](#javascript)
    - [Concatenação de Strings em JavaScript](#concatenação-de-strings-em-javascript)
    - [String Slicing em JavaScript](#string-slicing-em-javascript)
    - [Formatação de Números em Strings em JavaScript](#formatação-de-números-em-strings-em-javascript)
    - [Formatação de Datas em Strings em JavaScript](#formatação-de-datas-em-strings-em-javascript)
    - [Funções de Strings em JavaScript](#funções-de-strings-em-javascript)
  - [Java](#java)
    - [Concatenação de Strings em Java](#concatenação-de-strings-em-java)
    - [String Slicing em Java](#string-slicing-em-java)
    - [Formatação de Números em Strings em Java](#formatação-de-números-em-strings-em-java)
    - [Formatação de Datas em Strings em Java](#formatação-de-datas-em-strings-em-java)
    - [Funções de Strings em Java](#funções-de-strings-em-java)
  - [Python](#python)
    - [Concatenação de Strings em Python](#concatenação-de-strings-em-python)
    - [String Slicing em Python](#string-slicing-em-python)
    - [Formatação de Números em Strings em Python](#formatação-de-números-em-strings-em-python)
    - [Formatação de Datas em Strings em Python](#formatação-de-datas-em-strings-em-python)
    - [Funções de Strings em Python](#funções-de-strings-em-python)

## JavaScript

### Concatenação de Strings em JavaScript

1. Usando o operador de adição (+):

```javascript
let str1 = "Olá";
let str2 = "Mundo";
let resultado = str1 + " " + str2;
console.log(resultado); // Saída: "Olá Mundo"
```

2. Usando o método `concat()`:

```javascript
let str1 = "Olá";
let str2 = "Mundo";
let resultado = str1.concat(" ", str2);
console.log(resultado); // Saída: "Olá Mundo"
```

3. Utilizando template literals:

```javascript
let str1 = "Olá";
let str2 = "Mundo";
let resultado = `${str1} ${str2}`;
console.log(resultado); // Saída: "Olá Mundo"
```

### String Slicing em JavaScript

1. `substring(startIndex, endIndex)`: Este método retorna uma nova string que é uma cópia da porção da string original entre os índices `startIndex` (inclusive) e `endIndex` (exclusive).

```javascript
const str = 'Hello, World!';
const substring1 = str.substring(0, 5); // Resultado: 'Hello'
const substring2 = str.substring(7, 12); // Resultado: 'World'
```

2. `slice(startIndex, endIndex)`: Similar ao método `substring()`, o método `slice()` também retorna uma nova string que é uma cópia da porção da string original entre os índices `startIndex` (inclusive) e `endIndex` (exclusive).

```javascript
const str = 'Hello, World!';
const slice1 = str.slice(0, 5); // Resultado: 'Hello'
const slice2 = str.slice(7, 12); // Resultado: 'World'
```

3. `substr(startIndex, length)`: Este método retorna uma nova string que começa no índice `startIndex` e possui um comprimento de `length` caracteres.

```javascript
const str = 'Hello, World!';
const substr1 = str.substr(0, 5); // Resultado: 'Hello'
const substr2 = str.substr(7, 5); // Resultado: 'World'
```

4. `charAt(index)`: Retorna o caractere na posição `index` da string.

```javascript
const str = 'Hello, World!';
const char = str.charAt(4); // Resultado: 'o'
```

5. `charAt()`: Você também pode usar o acesso direto aos índices para obter um caractere específico.

```javascript
const str = 'Hello, World!';
const char = str[4]; // Resultado: 'o'
```

6. `substring(startIndex)`: Se você omitir o `endIndex` em `substring()` e `slice()`, eles retornarão uma substring a partir do `startIndex` até o final da string.

```javascript
const str = 'Hello, World!';
const substring = str.substring(7); // Resultado: 'World!'
const slice = str.slice(7); // Resultado: 'World!'
```

### Formatação de Números em Strings em JavaScript

1. Método `toFixed()`:

```javascript
let numero = 123.456;
let numeroFormatado = numero.toFixed(2);
console.log(numeroFormatado); // Saída: "123.46"
```

2. Método `toPrecision()`:

```javascript
let numero = 12345.6789;
let numeroFormatado = numero.toPrecision(5);
console.log(numeroFormatado); // Saída: "12345"
```

3. Método `toLocaleString()`:

```javascript
let numero = 1234567.89;
let numeroFormatado = numero.toLocaleString();
console.log(numeroFormatado); // Saída: "1,234,567.89" (dependendo da configuração regional do usuário)
```

4. Utilizando `Intl.NumberFormat`:

```javascript
let numero = 9876543.21;
let formatadorNumero = new Intl.NumberFormat('pt-BR', {
  style: 'decimal',
  minimumFractionDigits: 2,
  maximumFractionDigits: 2
});
let numeroFormatado = formatadorNumero.format(numero);
console.log(numeroFormatado); // Saída: "9.876.543,21"
```

### Formatação de Datas em Strings em JavaScript

1. Método `toLocaleDateString()`:

```javascript
let data = new Date();
let dataFormatada = data.toLocaleDateString();
console.log(dataFormatada); 
// Saída: dependendo da configuração regional do usuário 
// (por exemplo, "06/08/2023" em formato MM/DD/YYYY)
```

2. Utilizando `Intl.DateTimeFormat`:

```javascript
let data = new Date();
let formatadorData = new Intl.DateTimeFormat('pt-BR', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit'
});
let dataFormatada = formatadorData.format(data);
console.log(dataFormatada); // Saída: "06/08/2023"
```

3. Bibliotecas de terceiros:

Exemplo usando Moment.js:

```javascript
const moment = require('moment');
let data = new Date();
let dataFormatada = moment(data).format('DD/MM/YYYY');
console.log(dataFormatada); // Saída: "06/08/2023"
```

Exemplo usando Day.js:

```javascript
const dayjs = require('dayjs');
let data = new Date();
let dataFormatada = dayjs(data).format('DD/MM/YYYY');
console.log(dataFormatada); // Saída: "06/08/2023"
```

### Funções de Strings em JavaScript

1. String: length
   - Uso: É uma propriedade que retorna o comprimento da string, ou seja, o número de caracteres na string.
   - Parâmetros: Não possui parâmetros, pois é uma propriedade.

2. String.prototype.at
   - Uso: O método `at` permite acessar o caractere em um determinado índice da string.
   - Parâmetros: Requer um parâmetro, que é o índice do caractere a ser acessado.

3. String.prototype.charAt
   - Uso: O método `charAt` retorna o caractere em um índice específico da string.
   - Parâmetros: Requer um parâmetro, que é o índice do caractere a ser retornado.

4. String.prototype.charCodeAt
   - Uso: O método `charCodeAt` retorna o valor Unicode (UTF-16 code unit) do caractere em um índice especificado da string.
   - Parâmetros: Requer um parâmetro, que é o índice do caractere cujo valor Unicode deve ser retornado.

5. String.prototype.codePointAt
   - Uso: O método `codePointAt` retorna o valor Unicode (code point) completo do caractere em um índice especificado da string.
   - Parâmetros: Requer um parâmetro, que é o índice do caractere cujo valor Unicode deve ser retornado.

6. String.prototype.concat
   - Uso: O método `concat` combina uma ou mais strings e retorna uma nova string resultante da concatenação.
   - Parâmetros: Aceita um ou mais parâmetros, que são as strings a serem concatenadas.

7. String.prototype.endsWith
   - Uso: O método `endsWith` verifica se a string termina com uma substring específica.
   - Parâmetros: Requer um parâmetro, que é a substring a ser procurada no final da string.

8. String.fromCharCode
   - Uso: O método estático `fromCharCode` retorna uma string criada usando a sequência de valores Unicode (UTF-16 code units) especificada.
   - Parâmetros: Aceita um ou mais parâmetros inteiros que representam os valores Unicode.

9. String.fromCodePoint
   - Uso: O método estático `fromCodePoint` retorna uma string criada usando a sequência de valores Unicode (code points) especificada.
   - Parâmetros: Aceita um ou mais parâmetros inteiros que representam os valores Unicode (code points).

10. String.prototype.includes
    - Uso: O método `includes` verifica se a string contém uma substring específica.
    - Parâmetros: Requer um parâmetro, que é a substring a ser procurada na string.

11. String.prototype.indexOf
    - Uso: O método `indexOf` retorna o índice da primeira ocorrência de uma substring na string.
    - Parâmetros: Requer um parâmetro, que é a substring a ser encontrada.

12. String.prototype.isWellFormed
    - Uso: Não é um método padrão do JavaScript. O propósito e uso específico dessa função não são conhecidos com base nas informações fornecidas.

13. String.prototype.lastIndexOf
    - Uso: O método `lastIndexOf` retorna o índice da última ocorrência de uma substring na string.
    - Parâmetros: Requer um parâmetro, que é a substring a ser encontrada.

14. String.prototype.localeCompare
    - Uso: O método `localeCompare` compara duas strings com base na localidade atual e retorna um número indicando se a primeira string é menor, maior ou igual à segunda string.
    - Parâmetros: Requer um parâmetro, que é a string de comparação.

15. String.prototype.match
    - Uso: O método `match` é usado para encontrar correspondências de uma expressão regular na string e retornar um array contendo as correspondências.
    - Parâmetros: Requer um parâmetro, que é a expressão regular para procurar na string.

16. String.prototype.matchAll
    - Uso: O método `matchAll` é usado para encontrar todas as correspondências de uma expressão regular na string e retornar um iterador contendo as correspondências.
    - Parâmetros: Requer um parâmetro, que é a expressão regular para procurar na string.

17. String.prototype.normalize
    - Uso: O método `normalize` é usado para normalizar uma string Unicode, convertendo caracteres com formas equivalentes em uma forma canônica comum.
    - Parâmetros: Pode receber um parâmetro opcional especificando o tipo de normalização (por exemplo, "NFC", "NFD", "NFKC" ou "NFKD").

18. String.prototype.padEnd
    - Uso: O método `padEnd` preenche o final da string com um caractere específico até atingir o tamanho desejado.
    - Parâmetros: Requer dois parâmetros, o primeiro é o comprimento final da string após o preenchimento, e o segundo é o caractere a ser usado para o preenchimento (opcional, padrão é o espaço em branco).

19. String.prototype.padStart
    - Uso: O método `padStart` preenche o início da string com um caractere específico até atingir o tamanho desejado.
    - Parâmetros: Requer dois parâmetros, o primeiro é o comprimento final da string após o preenchimento, e o segundo é o caractere a ser usado para o preenchimento (opcional, padrão é o espaço em branco).

20. String.raw
    - Uso: O método estático `raw` é usado para obter a string raw de uma template literal, sem processar as sequências de escape.
    - Parâmetros: Aceita um ou mais parâmetros, que são as partes da template literal.

21. String.prototype.repeat
    - Uso: O método `repeat` retorna uma nova string que consiste em repetir a string original um determinado número de vezes.
    - Parâmetros: Requer um parâmetro, que é o número de vezes que a string deve ser repetida.

22. String.prototype.replace
    - Uso: O método `replace` é usado para substituir partes da string por outra substring ou por uma substring resultante de uma função de substituição.
    - Parâmetros: Aceita dois parâmetros, o primeiro é a substring ou expressão regular a ser substituída, e o segundo é a nova substring ou a função de substituição.

23. String.prototype.replaceAll
    - Uso: O método `replaceAll` é similar ao `replace`, mas substitui todas as ocorrências da substring ou expressão regular na string.
    - Parâmetros: Aceita dois parâmetros, o primeiro é a substring ou expressão regular a ser substituída, e o segundo é a nova substring.

24. String.prototype.search
    - Uso: O método `search` é usado para procurar uma substring ou expressão regular na string e retornar o índice da primeira ocorrência.
    - Parâmetros: Requer um parâmetro, que é a substring ou a expressão regular a ser procurada.

25. String.prototype.slice
    - Uso: O método `slice` retorna uma parte da string, selecionada entre os índices fornecidos.
    - Parâmetros: Aceita dois parâmetros, o primeiro é o índice de início da parte a ser retornada, e o segundo é o índice final (opcional, se não for fornecido, vai até o final da string).

26. String.prototype.split
    - Uso: O método `split` é usado para dividir a string em um array de substrings com base em um separador especificado.
    - Parâmetros: Requer um parâmetro, que é o separador usado para dividir a string.

27. String.prototype.startsWith
    - Uso: O método `startsWith` verifica se a string começa com uma substring específica.
    - Parâmetros: Requer um parâmetro, que é a substring a ser procurada no início da string.

28. String.prototype.substring
    - Uso: O método `substring` retorna uma parte da string, selecionada entre os índices fornecidos.
    - Parâmetros: Aceita dois parâmetros, o primeiro é o índice de início da parte a ser retornada, e o segundo é o índice final (opcional, se não for fornecido, vai até o final da string).

29. String.prototype.toLocaleLowerCase
    - Uso: O método `toLocaleLowerCase` retorna uma nova string com todos os caracteres convertidos para letras minúsculas com base na localidade atual.
    - Parâmetros: Não possui parâmetros.

30. String.prototype.toLocaleUpperCase
    - Uso: O método `toLocaleUpperCase` retorna uma nova string com todos os caracteres convertidos para letras maiúsculas com base na localidade atual.
    - Parâmetros: Não possui parâmetros.

31. String.prototype.toLowerCase
    - Uso: O método `toLowerCase` retorna uma nova string com todos os caracteres convertidos para letras minúsculas.
    - Parâmetros: Não possui parâmetros.

32. String.prototype.toString
    - Uso: O método `toString` retorna uma string representando o objeto String.
    - Parâmetros: Não possui parâmetros.

33. String.prototype.toUpperCase
    - Uso: O método `toUpperCase` retorna uma nova string com todos os caracteres convertidos para letras maiúsculas.
    - Parâmetros: Não possui parâmetros.

34. String.prototype.toWellFormed
    - Uso: Não é um método padrão do JavaScript. O propósito e uso específico dessa função não são conhecidos com base nas informações fornecidas.

35. String.prototype.trim
    - Uso: O método `trim` retorna uma nova string com os espaços em branco removidos do início e do final da string.
    - Parâmetros: Não possui parâmetros.

36. String.prototype.trimEnd
    - Uso: O método `trimEnd` é similar ao `trim`, mas remove os espaços em branco apenas do final da string.
    - Parâmetros: Não possui parâmetros.

37. String.prototype.trimStart
    - Uso: O método `trimStart` é similar ao `trim`, mas remove os espaços em branco apenas do início da string.
    - Parâmetros: Não possui parâmetros.

38. String.prototype.valueOf
    - Uso: O método `valueOf` retorna o valor primitivo da String.
    - Parâmetros: Não possui parâmetros.

## Java

### Concatenação de Strings em Java

1. Utilizando o operador de adição (+):

```java
String str1 = "Hello";
String str2 = "World";
String resultado = str1 + " " + str2;
System.out.println(resultado); // Saída: "Hello World"
```

2. Utilizando o método `concat()`:

```java
String str1 = "Hello";
String str2 = "World";
String resultado = str1.concat(" ").concat(str2);
System.out.println(resultado); // Saída: "Hello World"
```

3. Concatenação com outras variáveis ou literais:

```java
String nome = "Alice";
int idade = 30;
String mensagem = "Meu nome é " + nome + " e tenho " + idade + " anos.";
System.out.println(mensagem); // Saída: "Meu nome é Alice e tenho 30 anos."
```

5. Concatenando com StringBuilder:

```java
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(" ");
sb.append("World");
String resultado = sb.toString();
System.out.println(resultado); // Saída: "Hello World"
```

### String Slicing em Java

1. `substring(int beginIndex)`: Este método retorna uma nova string que é uma cópia da porção da string original a partir do índice `beginIndex` até o final da string.

```java
String str = "Hello, World!";
String substring1 = str.substring(7); // Resultado: "World!"
```

2. `substring(int beginIndex, int endIndex)`: Este método retorna uma nova string que é uma cópia da porção da string original entre os índices `beginIndex` (inclusive) e `endIndex` (exclusive).

```java
String str = "Hello, World!";
String substring2 = str.substring(0, 5); // Resultado: "Hello"
```

3. `charAt(int index)`: Retorna o caractere na posição `index` da string.

```java
String str = "Hello, World!";
char character = str.charAt(4); // Resultado: 'o'
```

4. `toCharArray()`: Retorna um array de caracteres contendo todos os caracteres da string.

```java
String str = "Hello";
char[] charArray = str.toCharArray(); // Resultado: ['H', 'e', 'l', 'l', 'o']
```

5. `getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)`: Copia os caracteres desta string para um array de caracteres de destino.

```java
String str = "Hello, World!";
char[] destArray = new char[5];
str.getChars(0, 5, destArray, 0); // Copia os primeiros 5 caracteres para destArray
```

### Formatação de Números em Strings em Java

1. Usando `DecimalFormat`:

```java
import java.text.DecimalFormat;
public class Main {
    public static void main(String[] args) {
        double numero = 12345.6789;
        DecimalFormat formato = new DecimalFormat("#,##0.00");
        String numeroFormatado = formato.format(numero);
        System.out.println(numeroFormatado); // Saída: "12,345.68"
    }
}
```

2. Usando `Formatter`:

```java
import java.util.Formatter;
public class Main {
    public static void main(String[] args) {
        double numero = 12345.6789;
        Formatter formato = new Formatter();
        String numeroFormatado = formato.format("%.2f", numero).toString();
        System.out.println(numeroFormatado); // Saída: "12345.68"
    }
}
```

3. Usando `getCurrencyInstance`:

```java
import java.text.DecimalFormat;
import java.util.Currency;
import java.util.Locale;
public class Main {
    public static void main(String[] args) {
        double numero = 12345.6789;
        DecimalFormat formato = (DecimalFormat) DecimalFormat.
                getCurrencyInstance(Locale.US);
        String numeroFormatado = formato.format(numero);
        System.out.println(numeroFormatado); // Saída: "$12,345.68"
    }
}
```

Lembre-se de importar as classes necessárias no início do arquivo Java:

```java
import java.text.DecimalFormat;
import java.util.Formatter;
import java.util.Locale;
```

### Formatação de Datas em Strings em Java

Em Java, para formatar datas em strings, você pode usar a classe `java.text.SimpleDateFormat` ou a classe `java.time.format.DateTimeFormatter`. Ambas as classes permitem formatar datas de acordo com um padrão específico. Abaixo estão exemplos de como formatar datas em strings usando essas classes:

1. Usando `SimpleDateFormat` (antes do Java 8):

```java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
    public static void main(String[] args) {
        Date data = new Date();
        SimpleDateFormat formato = new SimpleDateFormat("dd/MM/yyyy");
        String dataFormatada = formato.format(data);
        System.out.println(dataFormatada); // Saída: "06/08/2023"
    }
}
```

2. Usando `DateTimeFormatter` (Java 8 e posteriores):

```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
public class Main {
    public static void main(String[] args) {
        LocalDate data = LocalDate.now();
        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String dataFormatada = data.format(formato);
        System.out.println(dataFormatada); // Saída: "06/08/2023"
    }
}
```

Lembre-se de importar as classes necessárias no início do arquivo Java:

```java
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
```

### Funções de Strings em Java

1. `charAt(int index)`:
   - Uso: Retorna o caractere no índice especificado da String.
   - Parâmetros: `index` - o índice do caractere a ser retornado.

2. `codePointAt(int index)`:
   - Uso: Retorna o ponto de código Unicode no índice especificado da String.
   - Parâmetros: `index` - o índice do ponto de código a ser retornado.

3. `codePointBefore(int index)`:
   - Uso: Retorna o ponto de código Unicode antes do índice especificado da String.
   - Parâmetros: `index` - o índice do ponto de código a ser retornado.

4. `codePointCount(int beginIndex, int endIndex)`:
   - Uso: Retorna o número de pontos de código Unicode no intervalo de texto especificado da String.
   - Parâmetros: `beginIndex` - o índice do primeiro ponto de código do intervalo, `endIndex` - o índice após o último ponto de código do intervalo.

5. `compareTo(String anotherString)`:
   - Uso: Compara duas strings lexicograficamente.
   - Parâmetros: `anotherString` - a string a ser comparada.

6. `compareToIgnoreCase(String str)`:
   - Uso: Compara duas strings lexicograficamente, ignorando diferenças de maiúsculas e minúsculas.
   - Parâmetros: `str` - a string a ser comparada.

7. `concat(String str)`:
   - Uso: Concatena a string especificada no final desta string.
   - Parâmetros: `str` - a string a ser concatenada.

8. `contains(CharSequence s)`:
   - Uso: Retorna true se e somente se esta string contém a sequência de caracteres especificada.
   - Parâmetros: `s` - a sequência de caracteres a ser pesquisada.

9. `contentEquals(CharSequence cs)`:
   - Uso: Compara esta string com a CharSequence especificada.
   - Parâmetros: `cs` - a CharSequence a ser comparada.

10. `contentEquals(StringBuffer sb)`:
    - Uso: Compara esta string com a StringBuffer especificada.
    - Parâmetros: `sb` - a StringBuffer a ser comparada.

11. `copyValueOf(char[] data)`:
    - Uso: Equivalente a `valueOf(char[])`.
    - Parâmetros: `data` - o array de caracteres a ser utilizado.

12. `copyValueOf(char[] data, int offset, int count)`:
    - Uso: Equivalente a `valueOf(char[], int, int)`.
    - Parâmetros: `data` - o array de caracteres a ser utilizado, `offset` - o índice inicial do subarray, `count` - o número de caracteres a serem utilizados.

13. `endsWith(String suffix)`:
    - Uso: Verifica se esta string termina com o sufixo especificado.
    - Parâmetros: `suffix` - o sufixo a ser verificado.

14. `equals(Object anObject)`:
    - Uso: Compara esta string com o objeto especificado.
    - Parâmetros: `anObject` - o objeto a ser comparado.

15. `equalsIgnoreCase(String anotherString)`:
    - Uso: Compara esta string com outra string, ignorando diferenças de maiúsculas e minúsculas.
    - Parâmetros: `anotherString` - a outra string a ser comparada.

16. `format(Locale l, String format, Object... args)`:
    - Uso: Retorna uma string formatada usando a localização (Locale), a string de formatação e os argumentos especificados.
    - Parâmetros: `l` - a localização (Locale) a ser utilizada, `format` - a string de formatação, `args` - os argumentos a serem inseridos na string de formatação.

17. `format(String format, Object... args)`:
    - Uso: Retorna uma string formatada usando a string de formatação e os argumentos especificados.
    - Parâmetros: `format` - a string de formatação, `args` - os argumentos a serem inseridos na string de formatação.

18. `getBytes()`:
    - Uso: Codifica esta string em uma sequência de bytes usando o conjunto de caracteres padrão da plataforma, armazenando o resultado em um novo array de bytes.
    - Parâmetros: Nenhum.

19. `getBytes(Charset charset)`:
    - Uso: Codifica esta string em uma sequência de bytes usando o conjunto de caracteres especificado, armazenando o resultado em um novo array de bytes.
    - Parâmetros: `charset` - o conjunto de caracteres a ser utilizado para a codificação.

20. `getBytes(String charsetName)`:
    - Uso: Codifica esta string em uma sequência de bytes usando o conjunto de caracteres nomeado, armazenando o resultado em um novo array de bytes.
    - Parâmetros: `charsetName` - o nome do conjunto de caracteres a ser utilizado para a codificação.

21. `getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)`:
    - Uso: Copia os caracteres desta string para o array de caracteres de destino.
    - Parâmetros: `srcBegin` - o índice do primeiro caractere a ser copiado, `srcEnd` - o índice após o último caractere a ser copiado, `dst` - o array de caracteres de destino, `dstBegin` - o índice de destino inicial.

22. `hashCode()`:
    - Uso: Retorna um código hash para esta string.
    - Parâmetros: Nenhum.

23. `indexOf(int ch)`:
    - Uso: Retorna o índice da primeira ocorrência do caractere especificado nesta string.
    - Parâmetros: `ch` - o caractere a ser pesquisado.

24. `indexOf(int ch, int fromIndex)`:
    - Uso: Retorna o índice da primeira ocorrência do caractere especificado nesta string, começando a pesquisa a partir do índice especificado.
    - Parâmetros: `ch` - o caractere a ser pesquisado, `fromIndex` - o índice de início da pesquisa.

25. `indexOf(String str)`:
    - Uso: Retorna o índice da primeira ocorrência da substring especificada nesta string.
    - Parâmetros: `str` - a substring a ser pesquisada.

26. `indexOf(String str, int fromIndex)`:
    - Uso: Retorna o índice da primeira ocorrência da substring especificada nesta string, começando a pesquisa a partir do índice especificado.
    - Parâmetros: `str` - a substring a ser pesquisada, `fromIndex` - o índice de início da pesquisa.

27. `intern()`:
    - Uso: Retorna uma representação canônica (única) do objeto String.
    - Parâmetros: Nenhum.

28. `isEmpty()`:
    - Uso: Retorna true se o tamanho (length) da string for igual a 0.
    - Parâmetros: Nenhum.

29. `join(CharSequence delimiter, CharSequence... elements)`:
    - Uso: Retorna uma nova String composta de cópias dos elementos CharSequence unidos por um delimitador especificado.
    - Parâmetros: `delimiter` - o delimitador a ser inserido entre os elementos, `elements` - os elementos a serem unidos.

30. `join(CharSequence delimiter, Iterable<? extends CharSequence> elements)`:
    - Uso: Retorna uma nova String composta de cópias dos elementos CharSequence unidos por um delimitador especificado.
    - Parâmetros: `delimiter` - o delimitador a ser inserido entre os elementos, `elements` - os elementos a serem unidos.

31. `lastIndexOf(int ch)`:
    - Uso: Retorna o índice da última ocorrência do caractere especificado nesta string.
    - Parâmetros: `ch` - o caractere a ser pesquisado.

32. `lastIndexOf(int ch, int fromIndex)`:
    - Uso: Retorna o índice da última ocorrência do caractere especificado nesta string, começando a pesquisa a partir do índice especificado.
    - Parâmetros: `ch` - o caractere a ser pesquisado, `fromIndex` - o índice de início da pesquisa.

33. `lastIndexOf(String str)`:
    - Uso: Retorna o índice da última ocorrência da substring especificada nesta string.
    - Parâmetros: `str` - a substring a ser pesquisada.

34. `lastIndexOf(String str, int fromIndex)`:
    - Uso: Retorna o índice da última ocorrência da substring especificada nesta string, começando a pesquisa a partir do índice especificado.
    - Parâmetros: `str` - a substring a ser pesquisada, `fromIndex` - o índice de início da pesquisa.

35. `length()`:
    - Uso: Retorna o tamanho (número de caracteres) desta string.
    - Parâmetros: Nenhum.

36. `matches(String regex)`:
    - Uso: Indica se esta string corresponde à expressão regular especificada.
    - Parâmetros: `regex` - a expressão regular a ser utilizada.

37. `offsetByCodePoints(int index, int codePointOffset)`:
    - Uso: Retorna o índice nesta string que é deslocado a partir do índice fornecido por um deslocamento em pontos de código.
    - Parâmetros: `index` - o índice base, `codePointOffset` - o deslocamento em pontos de código.

38. `regionMatches(boolean ignoreCase, int toffset, String other, int ooffset, int len)`:
    - Uso: Testa se duas regiões de string são iguais.
    - Parâmetros: `ignoreCase` - se true, a comparação é feita ignorando diferenças de maiúsculas e minúsculas, `toffset` - o índice de início nesta string da região a ser verificada, `other` - a outra string para comparar, `ooffset` - o índice de início da região na outra string, `len` - o número de caracteres a serem comparados.

39. `regionMatches(int toffset, String other, int ooffset, int len)`:
    - Uso: Testa se duas regiões de string são iguais.
    - Parâmetros: `toffset` - o índice de início nesta string da região a ser verificada, `other` - a outra string para comparar, `ooffset` - o índice de início da região na outra string, `len` - o número de caracteres a serem comparados.

40. `replace(char oldChar, char newChar)`:
    - Uso: Retorna uma string resultante da substituição de todas as ocorrências de um caractere antigo por um caractere novo nesta string.
    - Parâmetros: `oldChar` - o caractere a ser substituído, `newChar` - o caractere de substituição.

41. `replace(CharSequence target, CharSequence replacement)`:
    - Uso: Substitui cada ocorrência da sequência de caracteres alvo por uma sequência de caracteres de substituição especificada nesta string.
    - Parâmetros: `target` - a sequência de caracteres a ser substituída, `replacement` - a sequência de caracteres de substituição.

42. `replaceAll(String regex, String replacement)`:
    - Uso: Substitui cada substring que corresponde à expressão regular especificada por uma string de substituição.
    - Parâmetros: `regex` - a expressão regular a ser utilizada para a busca, `replacement` - a string de substituição.

43. `replaceFirst(String regex, String replacement)`:
    - Uso: Substitui a primeira substring que corresponde à expressão regular especificada por uma string de substituição.
    - Parâmetros: `regex` - a expressão regular a ser utilizada para a busca, `replacement` - a string de substituição.

44. `split(String regex)`:
    - Uso: Divide esta string em torno das ocorrências da expressão regular especificada.
    - Parâmetros: `regex` - a expressão regular a ser utilizada como delimitador.

45. `split(String regex, int limit)`:
    - Uso: Divide esta string em torno das ocorrências da expressão regular especificada, limitando o número de divisões.
    - Parâmetros: `regex` - a expressão regular a ser utilizada como delimitador, `limit` - o número máximo de divisões a serem realizadas.

46. `startsWith(String prefix)`:
    - Uso: Verifica se esta string começa com o prefixo especificado.
    - Parâmetros: `prefix` - o prefixo a ser verificado.

47. `startsWith(String prefix, int toffset)`:
    - Uso: Verifica se a substring desta string que começa no índice especificado começa com o prefixo especificado.
    - Parâmetros: `prefix` - o prefixo a ser verificado, `toffset` - o índice de início da substring.

48. `subSequence(int beginIndex, int endIndex)`:
    - Uso: Retorna uma sequência de caracteres que é uma sub-sequência desta sequência.
    - Parâmetros: `beginIndex` - o índice inicial da sub-sequência, `endIndex` - o índice após o último caractere da sub-sequência.

49. `substring(int beginIndex)`:
    - Uso: Retorna uma substring desta string, começando no índice especificado até o final da string.
    - Parâmetros: `beginIndex` - o índice de início da substring.

50. `substring(int beginIndex, int endIndex)`:
    - Uso: Retorna uma substring desta string, começando no índice especificado e terminando no índice anterior ao índice final.
    - Parâmetros: `beginIndex` - o índice de início da substring, `endIndex` - o índice após o último caractere da substring.

51. `toCharArray()`:
    - Uso: Converte esta string em um novo array de caracteres.
    - Parâmetros: Nenhum.

52. `toLowerCase()`:
    - Uso: Converte todos os caracteres desta string para minúsculas usando as regras da localização (Locale) padrão.
    - Parâmetros: Nenhum.

53. `toLowerCase(Locale locale)`:
    - Uso: Converte todos os caracteres desta string para minúsculas usando as regras da localização (Locale) especificada.
    - Parâmetros: `locale` - a localização (Locale) a ser utilizada.

54. `toString()`:
    - Uso: Retorna esta string (que já é uma string, por isso o método simplesmente retorna a instância atual).
    - Parâmetros: Nenhum.

55. `toUpperCase()`:
    - Uso: Converte todos os caracteres desta string para maiúsculas usando as regras da localização (Locale) padrão.
    - Parâmetros: Nenhum.

56. `toUpperCase(Locale locale)`:
    - Uso: Converte todos os caracteres desta string para maiúsculas usando as regras da localização (Locale) especificada.
    - Parâmetros: `locale` - a localização (Locale) a ser utilizada.

57. `trim()`:
    - Uso: Retorna uma string cujo valor é esta string, removendo qualquer espaço em branco (espaços em branco no início e no final da string).
    - Parâmetros: Nenhum.

58. `valueOf(boolean b)`:
    - Uso: Retorna a representação de string do argumento booleano.
    - Parâmetros: `b` - o valor booleano a ser representado como string.

59. `valueOf(char c)`:
    - Uso: Retorna a representação de string do argumento char.
    - Parâmetros: `c` - o caractere a ser representado como string.

60. `valueOf(char[] data)`:
    - Uso: Retorna a representação de string do array de caracteres.
    - Parâmetros: `data` - o array de caracteres a ser representado como string.

61. `valueOf(char[] data, int offset, int count)`:
    - Uso: Retorna a representação de string de um subarray específico do array de caracteres.
    - Parâmetros: `data` - o array de caracteres que contém o subarray, `offset` - o índice inicial do subarray, `count` - o número de caracteres a serem incluídos no subarray.

62. `valueOf(double d)`:
    - Uso: Retorna a representação de string do argumento double.
    - Parâmetros: `d` - o valor double a ser representado como string.

63. `valueOf(float f)`:
    - Uso: Retorna a representação de string do argumento float.
    - Parâmetros: `f` - o valor float a ser representado como string.

64. `valueOf(int i)`:
    - Uso: Retorna a representação de string do argumento inteiro.
    - Parâmetros: `i` - o valor inteiro a ser representado como string.

65. `valueOf(long l)`:
    - Uso: Retorna a representação de string do argumento long.
    - Parâmetros: `l` - o valor long a ser representado como string.

66. `valueOf(Object obj)`:
    - Uso: Retorna a representação de string do argumento objeto.
    - Parâmetros: `obj` - o objeto a ser representado como string.

## Python

### Concatenação de Strings em Python

1. Usando o operador `+`:

```python
str1 = "Olá"
str2 = "Mundo"
resultado = str1 + " " + str2
print(resultado)  # Saída: "Olá Mundo"
```

1. Usando o método `join()`:

```python
lista = ["Olá", "Mundo"]
separador = " "
resultado = separador.join(lista)
print(resultado)  # Saída: "Olá Mundo"
```

2. Utilizando f-string (Python 3.6+):

```python
str1 = "Olá"
str2 = "Mundo"
resultado = f"{str1} {str2}"
print(resultado)  # Saída: "Olá Mundo"
```

3. Utilizando métodos de formatação (Python 2 e 3):

```python
str1 = "Olá"
str2 = "Mundo"
resultado = "{} {}".format(str1, str2)
print(resultado)  # Saída: "Olá Mundo"
```

### String Slicing em Python


1. Índices de fatiamento (slicing): O fatiamento é uma técnica muito comum em Python para obter substrings usando índices.

```python
str = "Hello, World!"
substring1 = str[7:]   # Resultado: "World!"
substring2 = str[0:5]  # Resultado: "Hello"
substring3 = str[:5]   # Resultado: "Hello" (índice inicial omitido)
substring4 = str[7:12] # Resultado: "World" (índice final exclusivo)
```

2. Método `slice(start, stop, step)`: O método `slice()` permite criar um objeto slice que pode ser usado para obter uma substring.

```python
str = "Hello, World!"
s = slice(7, 12) # Cria um objeto slice para obter de 7 a 11 (exclusivo)
substring = str[s] # Resultado: "World"
```

3. Método `split(separator, maxsplit)`: O método `split()` divide a string em substrings com base em um separador especificado e retorna uma lista com as substrings resultantes.

```python
str = "Hello, World!"
substring_list = str.split(", ") # Resultado: ['Hello', 'World!']
```

4. Método `find(substring, start, end)`: O método `find()` retorna o índice da primeira ocorrência da substring dentro da string ou -1 se não for encontrada.

```python
str = "Hello, World!"
index = str.find("World") # Resultado: 7
```

5. Método `index(substring, start, end)`: O método `index()` é semelhante ao `find()`, mas gera uma exceção `ValueError` se a substring não for encontrada.

```python
str = "Hello, World!"
index = str.index("World") # Resultado: 7
```

6. Método `replace(old, new, count)`: O método `replace()` retorna uma nova string em que todas as ocorrências da substring `old` são substituídas por `new`.

```python
str = "Hello, World!"
new_str = str.replace("Hello", "Hi") # Resultado: "Hi, World!"
```

### Formatação de Números em Strings em Python

1. Usando o método `format()`:

```python
numero = 12345.6789
numero_formatado = "{:.2f}".format(numero)
print(numero_formatado)  # Saída: "12345.68"
```

2. Usando f-string (Python 3.6+):

```python
numero = 12345.6789
numero_formatado = f"{numero:.2f}"
print(numero_formatado)  # Saída: "12345.68"
```

3. Usando a biblioteca `locale`:

```python
import locale
numero = 12345.6789
locale.setlocale(locale.LC_ALL, 'en_US')  # Definindo a localização (no caso, EUA)
numero_formatado = locale.format_string("%.2f", numero)
print(numero_formatado)  # Saída: "12,345.68" (dependendo da configuração regional)
```


### Formatação de Datas em Strings em Python

1. Usando `strftime()`:

```python
from datetime import datetime
data = datetime(2023, 8, 6)
data_formatada = data.strftime("%d/%m/%Y")
print(data_formatada)  # Saída: "06/08/2023"
```

2. Usando `strptime()`:

```python
from datetime import datetime
data_str = "06/08/2023"
data = datetime.strptime(data_str, "%d/%m/%Y")
print(data)  # Saída: 2023-08-06 00:00:00
```

3. Usando `strftime()` com localização (locale):

```python
from datetime import datetime
import locale
data = datetime(2023, 8, 6)
# Definindo a localização (no caso, Brasil - pt_BR)
locale.setlocale(locale.LC_ALL, 'pt_BR')
data_formatada = data.strftime("%d de %B de %Y")
print(data_formatada)  # Saída: "06 de agosto de 2023"
```

### Funções de Strings em Python

1. capitalize():
   - Uso: Converte o primeiro caractere da string em uma letra maiúscula (capital).
   - Parâmetros: Não possui parâmetros.

2. casefold():
   - Uso: Implementa a correspondência de strings sem diferenciação de maiúsculas e minúsculas (caseless).
   - Parâmetros: Não possui parâmetros.

3. center(width, fillchar):
   - Uso: Centraliza a string em um campo de largura especificada e preenche os espaços à esquerda e à direita com um caractere especificado (ou espaço, se não fornecido).
   - Parâmetros:
     - width: O comprimento total do campo para centralizar a string.
     - fillchar (opcional): O caractere usado para preencher os espaços vazios ao redor da string. O padrão é um espaço em branco.

4. count(substring, start, end):
   - Uso: Retorna o número de ocorrências de uma substring na string.
   - Parâmetros:
     - substring: A substring a ser contada.
     - start (opcional): O índice a partir do qual a busca deve começar.
     - end (opcional): O índice no qual a busca deve parar.

5. encode(encoding, errors):
   - Uso: Codifica a string usando o esquema de codificação especificado e retorna uma sequência de bytes.
   - Parâmetros:
     - encoding (opcional): A codificação a ser usada. O padrão é 'utf-8'.
     - errors (opcional): A estratégia de tratamento de erros, se a codificação falhar. O padrão é 'strict'.

6. endswith(suffix, start, end):
   - Uso: Retorna "True" se a string termina com o sufixo especificado.
   - Parâmetros:
     - suffix: O sufixo a ser verificado.
     - start (opcional): O índice a partir do qual a verificação deve começar.
     - end (opcional): O índice no qual a verificação deve parar.

7. expandtabs(tabsize):
   - Uso: Especifica a quantidade de espaços a serem substituídos pelo caractere '\t' (tabulação) na string.
   - Parâmetros:
     - tabsize (opcional): O número de espaços equivalentes a um caractere de tabulação. O padrão é 8.

8. find(substring, start, end):
   - Uso: Retorna o índice da primeira ocorrência de uma substring na string. Retorna -1 se a substring não for encontrada.
   - Parâmetros:
     - substring: A substring a ser procurada.
     - start (opcional): O índice a partir do qual a busca deve começar.
     - end (opcional): O índice no qual a busca deve parar.

9. format(*args, **kwargs):
   - Uso: Formata a string para exibição, substituindo marcadores de posição {} pelos valores fornecidos.
   - Parâmetros:
     - *args: Argumentos posicionais para substituir os marcadores de posição.
     - **kwargs: Argumentos de palavra-chave para substituir os marcadores de posição nomeados.

10. format_map(mapping):
    - Uso: Formata a string para exibição, substituindo marcadores de posição nomeados {} pelos valores em um dicionário.
    - Parâmetros:
      - mapping: Um dicionário contendo os valores para substituir os marcadores de posição nomeados.

11. index(substring, start, end):
    - Uso: Retorna o índice da primeira ocorrência de uma substring na string. Gera um erro se a substring não for encontrada.
    - Parâmetros:
      - substring: A substring a ser procurada.
      - start (opcional): O índice a partir do qual a busca deve começar.
      - end (opcional): O índice no qual a busca deve parar.

12. isalnum():
    - Uso: Verifica se todos os caracteres na string são alfanuméricos (letras e números).
    - Parâmetros: Não possui parâmetros.

13. isalpha():
    - Uso: Verifica se todos os caracteres na string são letras do alfabeto.
    - Parâmetros: Não possui parâmetros.

14. isdecimal():
    - Uso: Verifica se todos os caracteres na string são dígitos decimais.
    - Parâmetros: Não possui parâmetros.

15. isdigit():
    - Uso: Verifica se todos os caracteres na string são dígitos.
    - Parâmetros: Não possui parâmetros.

16. isidentifier():
    - Uso: Verifica se a string é um identificador válido do Python (por exemplo, nome de variável).
    - Parâmetros: Não possui parâmetros.

17. islower():
    - Uso: Verifica se todos os caracteres na string estão em minúsculas.
    - Parâmetros: Não possui parâmetros.

18. isnumeric():
    - Uso: Verifica se todos os caracteres na string são caracteres numéricos.
    - Parâmetros: Não possui parâmetros.

19. isprintable():
    - Uso: Verifica se todos os caracteres na string são imprimíveis ou se a string está vazia.
    - Parâmetros: Não possui parâmetros.

20. isspace():
    - Uso: Verifica se todos os caracteres na string são caracteres de espaço em branco.
    - Parâmetros: Não possui parâmetros.

21. istitle():
    - Uso: Verifica se a string está em título (cada palavra com letra maiúscula no início).
    - Parâmetros: Não possui parâmetros.

22. isupper():
    - Uso: Verifica se todos os caracteres na string estão em maiúsculas.
    - Parâmetros: Não possui parâmetros.

23. join(iterable):
    - Uso: Retorna uma string resultante da concatenação dos elementos de um iterable (lista, tupla, etc.) usando a string como separador.
    - Parâmetros:
      - iterable: O iterable contendo os elementos a serem concatenados.

24. ljust(width, fillchar):
    - Uso: Alinha a string à esquerda e preenche os espaços à direita com um caractere especificado (ou espaço, se não fornecido).
    - Parâmetros:
      - width: O comprimento total da string após a formatação.
      - fillchar (opcional): O caractere usado para preencher os espaços vazios à direita da string. O padrão é um espaço em branco.

25. lower():
    - Uso: Converte todos os caracteres da string em minúsculas.
    - Parâmetros: Não possui parâmetros.

26. lstrip(chars):
    - Uso: Remove os caracteres especificados à esquerda da string. Se não for fornecido, remove espaços em branco à esquerda.
    - Parâmetros:
      - chars (opcional): Os caracteres a serem removidos. Se não for fornecido, remove espaços em branco à esquerda.

27. maketrans(x, y, z):
    - Uso: Retorna uma tabela de tradução que pode ser usada na função translate().
    - Parâmetros:
      - x: String contendo os caracteres a serem substituídos.
      - y: String contendo os caracteres de substituição.
      - z: String contendo os caracteres a serem removidos.

28. partition(separator):
    - Uso: Divide a string na primeira ocorrência do separador e retorna uma tupla com as três partes.
    - Parâmetros:
      - separator: A string a ser usada como separador.

29. replace(old, new, count):
    - Uso: Substitui todas as ocorrências de uma substring por outra substring.
    - Parâmetros:
      - old: A substring a ser substituída.
      - new: A nova substring para substituição.
      - count (opcional): O número máximo de substituições a serem feitas. O padrão é substituir todas as ocorrências.

30. rfind(substring, start, end):
    - Uso: Retorna o índice da última ocorrência de uma substring na string. Retorna -1 se a substring não for encontrada.
    - Parâmetros:
      - substring: A substring a ser procurada.
      - start (opcional): O índice a partir do qual a busca deve começar.
      - end (opcional): O índice no qual a busca deve parar.

31. rindex(substring, start, end):
    - Uso: Retorna o índice da última ocorrência de uma substring na string. Gera um erro se a substring não for encontrada.
    - Parâmetros:
      - substring: A substring a ser procurada.
      - start (opcional): O índice a partir do qual a busca deve começar.
      - end (opcional): O índice no qual a busca deve parar.

32. rjust(width, fillchar):
    - Uso: Alinha a string à direita e preenche os espaços à esquerda com um caractere especificado (ou espaço, se não fornecido).
    - Parâmetros:
      - width: O comprimento total da string após a formatação.
      - fillchar (opcional): O caractere usado para preencher os espaços vazios à esquerda da string. O padrão é um espaço em branco.

33. rpartition(separator):
    - Uso: Divide a string na última ocorrência do separador e retorna uma tupla com as três partes.
    - Parâmetros:
      - separator: A string a ser usada como separador.

34. rsplit(separator, maxsplit):
    - Uso: Divide a string a partir do lado direito usando o separador especificado e retorna uma lista de substrings.
    - Parâmetros:
      - separator (opcional): O separador a ser usado para dividir a string. Se não for fornecido, usa espaços em branco.
      - maxsplit (opcional): O número máximo de splits a serem feitos. O padrão é dividir em todas as ocorrências.

35. rstrip(chars):
    - Uso: Remove os caracteres especificados à direita da string. Se não for fornecido, remove espaços em branco à direita.
    - Parâmetros:
      - chars (opcional): Os caracteres a serem removidos. Se não for fornecido, remove espaços em branco à direita.

36. split(separator, maxsplit):
    - Uso: Divide a string usando o separador especificado e retorna uma lista de substrings.
    - Parâmetros:
      - separator (opcional): O separador a ser usado para dividir a string. Se não for fornecido, usa espaços em branco.
      - maxsplit (opcional): O número máximo de splits a serem feitos. O padrão é dividir em todas as ocorrências.

37. splitlines(keepends):
    - Uso: Divide a string em linhas e retorna uma lista de linhas.
    - Parâmetros:
      - keepends (opcional): Se True, mantém o caractere de quebra de linha (\n ou \r\n) no final de cada linha. O padrão é False.

38. startswith(prefix, start, end):
    - Uso: Retorna "True" se a string começar com o prefixo especificado.
    - Parâmetros:
      - prefix: O prefixo a ser verificado.
      - start (opcional): O índice a partir do qual a verificação deve começar.
      - end (opcional): O índice no qual a verificação deve parar.

39. strip(chars):
    - Uso: Remove os caracteres especificados tanto à esquerda quanto à direita da string. Se não for fornecido, remove espaços em branco.
    - Parâmetros:
      - chars (opcional): Os caracteres a serem removidos. Se não for fornecido, remove espaços em branco.

40. swapcase():
    - Uso: Converte caracteres em maiúsculas para minúsculas e vice-versa.


    - Parâmetros: Não possui parâmetros.

41. title():
    - Uso: Converte a string em título (cada palavra com letra maiúscula no início).
    - Parâmetros: Não possui parâmetros.

42. translate(table):
    - Uso: Modifica a string de acordo com uma tabela de tradução criada com a função maketrans().
    - Parâmetros:
      - table: A tabela de tradução criada com a função maketrans().

43. upper():
    - Uso: Converte todos os caracteres da string em maiúsculas.
    - Parâmetros: Não possui parâmetros.

44. zfill(width):
    - Uso: Retorna uma cópia da string preenchida com '0' à esquerda para atingir o comprimento especificado.
    - Parâmetros:
      - width: O comprimento total da string após o preenchimento.
