# Aggregates

- [Aggregates](#aggregates)
  - [Dicionários em JavaScript](#dicionários-em-javascript)
    - [Funções de Dicionário em JavaScript](#funções-de-dicionário-em-javascript)
  - [Conjuntos em JavaScript](#conjuntos-em-javascript)
  - [Funções de Conjuntos em JavaScript](#funções-de-conjuntos-em-javascript)
  - [Listas em JavaScript](#listas-em-javascript)
    - [Funções de Lista em JavaScript](#funções-de-lista-em-javascript)
  - [O Operador Spread em JavaScript](#o-operador-spread-em-javascript)
  - [Iteração em JavaScript](#iteração-em-javascript)
  - [Pilha em JavaScript](#pilha-em-javascript)
  - [Fila em JavaScript](#fila-em-javascript)
  - [Dicionários em Python](#dicionários-em-python)
    - [Funções de Dicionário em Python](#funções-de-dicionário-em-python)
  - [Conjuntos em Python](#conjuntos-em-python)
    - [Funções de Conjuntos em Python](#funções-de-conjuntos-em-python)
  - [Tuplas em Python](#tuplas-em-python)
  - [Listas em Python](#listas-em-python)
    - [Funções de Lista em Python](#funções-de-lista-em-python)
  - [Funções Comuns de Sequências em Python](#funções-comuns-de-sequências-em-python)
  - [Compreensão de Listas em Python](#compreensão-de-listas-em-python)
  - [O Operador Spread em Python](#o-operador-spread-em-python)
  - [Pilha em Python](#pilha-em-python)
  - [Fila em Python](#fila-em-python)
  - [Collections em Python](#collections-em-python)
  - [Arrays em Java](#arrays-em-java)
    - [Funçoes com Arrays em Java](#funçoes-com-arrays-em-java)
  - [Listas em Java](#listas-em-java)
    - [Funções de Lista em Java](#funções-de-lista-em-java)
  - [Tuplas em Java](#tuplas-em-java)
  - [Conjuntos em Java](#conjuntos-em-java)
  - [Funções de Coleções em Java](#funções-de-coleções-em-java)
  - [Dicionários em Java](#dicionários-em-java)
  - [Pilha em Java](#pilha-em-java)
  - [Fila em Java](#fila-em-java)

## Dicionários em JavaScript

1. Criação de um objeto (dicionário):
Você pode criar um objeto usando a sintaxe literal de objeto ou o construtor `Object()`.

```javascript
// Sintaxe literal
let dicionario1 = {
  chave1: 'valor1',
  chave2: 'valor2',
  chave3: 'valor3'
};
// Usando o construtor Object()
let dicionario2 = new Object();
dicionario2['nome'] = 'João';
dicionario2['idade'] = 30;
```

2. Acessando e modificando valores:
Você pode acessar os valores de um dicionário usando a chave entre colchetes ou a notação de ponto.

```javascript
let pessoa = {
  nome: 'João',
  idade: 30,
  cidade: 'São Paulo'
};
console.log(pessoa['nome']); // Saída: 'João'
console.log(pessoa.idade);   // Saída: 30
pessoa.cidade = 'Rio de Janeiro';
console.log(pessoa); // Saída: { nome: 'João', idade: 30, cidade: 'Rio de Janeiro' }
```

3. Verificando a existência de uma chave:
Você pode verificar se uma chave existe em um dicionário usando o operador `in` ou o método `hasOwnProperty()`.

```javascript
let pessoa = {
  nome: 'João',
  idade: 30,
  cidade: 'São Paulo'
};
console.log('nome' in pessoa);             // Saída: true
console.log(pessoa.hasOwnProperty('idade')); // Saída: true
console.log('profissao' in pessoa);         // Saída: false
```

### Funções de Dicionário em JavaScript

Claro, aqui estão as descrições do uso e parâmetros de cada uma das funções de objetos em JavaScript:

1. **Object.assign(target, ...sources)**
   - Uso: Copia as propriedades de um ou mais objetos de origem (sources) para o objeto de destino (target).
   - Parâmetros:
     - target: O objeto de destino onde as propriedades serão copiadas.
     - sources: Um ou mais objetos de origem de onde as propriedades serão copiadas.

2. **Object.create(proto, [propertiesObject])**
   - Uso: Cria um novo objeto com o protótipo especificado.
   - Parâmetros:
     - proto: O objeto que será o protótipo do novo objeto.
     - propertiesObject (opcional): Um objeto que define propriedades adicionais para o novo objeto.

3. **Object.defineProperties(obj, props)**
   - Uso: Define várias propriedades em um objeto.
   - Parâmetros:
     - obj: O objeto no qual as propriedades serão definidas.
     - props: Um objeto cujas chaves são os nomes das propriedades e os valores são descritores de propriedades.

4. **Object.defineProperty(obj, prop, descriptor)**
   - Uso: Define uma propriedade em um objeto com o descritor fornecido.
   - Parâmetros:
     - obj: O objeto no qual a propriedade será definida.
     - prop: O nome da propriedade a ser definida.
     - descriptor: Um objeto que define o comportamento da propriedade (configurável, enumerável, valor, etc.).

5. **Object.entries(obj)**
   - Uso: Retorna uma matriz contendo matrizes de pares chave/valor para as propriedades enumeráveis de um objeto.
   - Parâmetros:
     - obj: O objeto cujas propriedades enumeráveis serão retornadas como uma matriz.

6. **Object.freeze(obj)**
   - Uso: Congela um objeto, tornando suas propriedades não modificáveis.
   - Parâmetros:
     - obj: O objeto que será congelado.

7. **Object.fromEntries(entries)**
   - Uso: Retorna um novo objeto a partir de uma matriz de pares chave/valor.
   - Parâmetros:
     - entries: Uma matriz contendo pares chave/valor representando as propriedades do novo objeto.

8. **Object.getOwnPropertyDescriptor(obj, prop)**
   - Uso: Retorna o descritor de uma propriedade de um objeto.
   - Parâmetros:
     - obj: O objeto que contém a propriedade.
     - prop: O nome da propriedade cujo descritor será retornado.

9. **Object.getOwnPropertyDescriptors(obj)**
   - Uso: Retorna um objeto contendo todos os descritores de propriedades de um objeto.
   - Parâmetros:
     - obj: O objeto cujos descritores de propriedades serão retornados.

10. **Object.getOwnPropertyNames(obj)**
    - Uso: Retorna uma matriz contendo os nomes de todas as propriedades enumeráveis e não enumeráveis de um objeto.
    - Parâmetros:
      - obj: O objeto cujos nomes de propriedades serão retornados como uma matriz.

11. **Object.getOwnPropertySymbols(obj)**
    - Uso: Retorna uma matriz contendo os símbolos de todas as propriedades de um objeto.
    - Parâmetros:
      - obj: O objeto cujos símbolos de propriedades serão retornados como uma matriz.

12. **Object.getPrototypeOf(obj)**
    - Uso: Retorna o protótipo de um objeto.
    - Parâmetros:
      - obj: O objeto cujo protótipo será retornado.

13. **Object.hasOwn(obj, prop)**
    - Uso: Verifica se um objeto tem sua própria propriedade (não herdada) com o nome especificado.
    - Parâmetros:
      - obj: O objeto que será verificado.
      - prop: O nome da propriedade que será verificada.

14. **Object.prototype.hasOwnProperty(prop)**
    - Uso: Verifica se o objeto possui uma propriedade própria (não herdada) com o nome especificado.
    - Parâmetros:
      - prop: O nome da propriedade que será verificada.

15. **Object.is(value1, value2)**
    - Uso: Compara se dois valores são iguais.
    - Parâmetros:
      - value1: O primeiro valor a ser comparado.
      - value2: O segundo valor a ser comparado.

16. **Object.isExtensible(obj)**
    - Uso: Verifica se um objeto pode ter novas propriedades adicionadas a ele.
    - Parâmetros:
      - obj: O objeto que será verificado.

17. **Object.isFrozen(obj)**
    - Uso: Verifica se um objeto está congelado, ou seja, suas propriedades não podem ser modificadas.
    - Parâmetros:
      - obj: O objeto que será verificado.

18. **Object.prototype.isPrototypeOf(obj)**
    - Uso: Verifica se o objeto atual está no protótipo da cadeia de um objeto especificado.
    - Parâmetros:
      - obj: O objeto que será verificado.

19. **Object.isSealed(obj)**
    - Uso: Verifica se um objeto está selado, ou seja, suas propriedades existentes não podem ser modificadas, mas novas propriedades não são permitidas.
    - Parâmetros:
      - obj: O objeto que será verificado.

20. **Object.keys(obj)**
    - Uso: Retorna uma matriz contendo os nomes de todas as propriedades enumeráveis de um objeto.
    - Parâmetros:
      - obj: O objeto cujos nomes de propriedades enumeráveis serão retornados como uma matriz.

21. **Object.preventExtensions(obj)**
    - Uso: Impede que novas propriedades sejam adicionadas a um objeto.
    - Parâmetros:
      - obj: O objeto que será tornado não extensível.

22. **Object.prototype.propertyIsEnumerable(prop)**
    - Uso: Verifica se uma propriedade específica é enumerável no objeto.
    - Parâmetros:
      - prop: O nome da propriedade que será verificada.

23. **Object.seal(obj)**
    - Uso: Sela um objeto, tornando suas propriedades existentes não configuráveis e não adicionando novas propriedades.
    - Parâmetros:
      - obj: O objeto que será selado.

24. **Object.setPrototypeOf(obj, prototype)**
    - Uso: Define o protótipo (prototype) de um objeto.
    - Parâmetros:
      - obj: O objeto que terá o protótipo definido.
      - prototype: O objeto que será o novo protótipo do objeto.

25. **Object.prototype.toLocaleString()**
    - Uso: Retorna uma representação localizada do objeto como uma string.
    - Parâmetros: Nenhum.

26. **Object.prototype.toString()**
    - Uso: Retorna uma string representando o objeto.
    - Parâmetros: Nenhum.

27. **Object.prototype.valueOf()**
    - Uso: Retorna o valor primitivo do objeto.
    - Parâmetros: Nenhum.

28. **Object.values(obj)**
    - Uso: Retorna uma matriz contendo os valores das propriedades enumeráveis de um objeto.
    - Parâmetros:
      - obj: O objeto cujos valores de propriedades enumeráveis serão retornados como uma matriz.

## Conjuntos em JavaScript

1. Criando um conjunto:
```javascript
const mySet = new Set(); // Conjunto vazio
```

2. Adicionando elementos ao conjunto:
```javascript
mySet.add(1);
mySet.add("Hello");
mySet.add({ name: "John" });
```

3. Verificando se um elemento existe no conjunto:
```javascript
const hasElement = mySet.has(1); // true
const hasAnotherElement = mySet.has("World"); // false
```

4. Removendo elementos do conjunto:
```javascript
mySet.delete(1);
```

5. Verificando o tamanho do conjunto:
```javascript
const size = mySet.size;
```

6. Iterando sobre os elementos do conjunto:
```javascript
mySet.forEach((value) => {
  console.log(value);
});
```

7. Convertendo o conjunto para uma matriz (array):
```javascript
const myArray = [...mySet];
```

## Funções de Conjuntos em JavaScript

1. `Set.prototype.size`: Retorna o número de elementos no conjunto.

2. `Set.prototype.add(value)`: Adiciona um novo elemento ao conjunto, se ele ainda não estiver presente.

3. `Set.prototype.clear()`: Remove todos os elementos do conjunto, tornando-o vazio.

4. `Set.prototype.delete(value)`: Remove um elemento específico do conjunto, se estiver presente.

5. `Set.prototype.entries()`: Retorna um iterador com pares [valor, valor] para cada elemento no conjunto.

6. `Set.prototype.forEach(callback, thisArg)`: Executa uma função de retorno para cada elemento do conjunto.

7. `Set.prototype.has(value)`: Verifica se um elemento específico está presente no conjunto.

8. `Set.prototype.keys()`: Retorna um iterador com os valores dos elementos no conjunto.

9. `Set.prototype.values()`: Retorna um iterador com os valores dos elementos no conjunto.

## Listas em JavaScript

1. Criando um array:
```javascript
const myArray = []; // Cria um array vazio
const numbers = [1, 2, 3, 4, 5]; // Cria um array com elementos
const names = ["John", "Jane", "Alice"]; // Cria um array de strings
```

2. Acessando elementos do array:
```javascript
const myArray = [10, 20, 30];
console.log(myArray[0]); // Output: 10 (primeiro elemento)
console.log(myArray[2]); // Output: 30 (terceiro elemento)
```

3. Alterando elementos do array:
```javascript
const myArray = [10, 20, 30];
myArray[1] = 50;
console.log(myArray); // Output: [10, 50, 30]
```

4. Obtendo o tamanho do array:
```javascript
const myArray = [10, 20, 30];
console.log(myArray.length); // Output: 3
```

5. Adicionando elementos ao array:
```javascript
const myArray = [10, 20];
myArray.push(30); // Adiciona um elemento ao final do array
console.log(myArray); // Output: [10, 20, 30]
myArray.unshift(5); // Adiciona um elemento no início do array
console.log(myArray); // Output: [5, 10, 20, 30]
```

6. Removendo elementos do array:
```javascript
const myArray = [10, 20, 30];
const removedElement = myArray.pop(); // Remove e retorna o último elemento
console.log(myArray); // Output: [10, 20]
console.log(removedElement); // Output: 30
const shiftedElement = myArray.shift(); // Remove e retorna o primeiro elemento
console.log(myArray); // Output: [20]
console.log(shiftedElement); // Output: 10
```

7. Iterando sobre elementos do array:
```javascript
const myArray = [10, 20, 30];
myArray.forEach((element) => {
  console.log(element);
});
/* Output:
   10
   20
   30
*/
```

8. Procurando elementos no array:
```javascript
const myArray = [10, 20, 30];
const index = myArray.indexOf(20); // Procura o índice do elemento no array
console.log(index); // Output: 1 (índice do elemento 20)

const exists = myArray.includes(30); // Verifica se o elemento existe no array
console.log(exists); // Output: true
```

### Funções de Lista em JavaScript

Aqui está a descrição do uso e dos parâmetros de todas as funções de arrays em JavaScript, de acordo com a lista fornecida:

1. `at(index)`: Retorna o elemento do array no índice especificado.

2. `concat(array1, array2, ..., arrayN)`: Combina arrays e retorna um novo array com os arrays combinados.

3. `constructor`: Retorna a função que criou o protótipo do objeto Array.

4. `copyWithin(target, start, end)`: Copia elementos do array dentro do próprio array, de e para as posições especificadas.

5. `entries()`: Retorna um iterador de pares chave/valor do array.

6. `every(callback(element, index, array), thisArg)`: Verifica se todos os elementos do array passam em um teste especificado por uma função de retorno.

7. `fill(value, start, end)`: Preenche os elementos do array com um valor estático.

8. `filter(callback(element, index, array), thisArg)`: Cria um novo array com todos os elementos do array que passam em um teste especificado por uma função de retorno.

9. `find(callback(element, index, array), thisArg)`: Retorna o valor do primeiro elemento do array que passa em um teste especificado por uma função de retorno.

10. `findIndex(callback(element, index, array), thisArg)`: Retorna o índice do primeiro elemento do array que passa em um teste especificado por uma função de retorno.

11. `flat(depth)`: Concatena os elementos dos subarrays até a profundidade especificada.

12. `flatMap(callback(element, index, array), thisArg)`: Mapeia todos os elementos do array e cria um novo array plano.

13. `forEach(callback(element, index, array), thisArg)`: Chama uma função de retorno para cada elemento do array.

14. `from(object, mapFn, thisArg)`: Cria um novo array a partir de um objeto ou de um array-like object.

15. `includes(searchElement, fromIndex)`: Verifica se um elemento está presente no array.

16. `indexOf(searchElement, fromIndex)`: Procura o array por um elemento e retorna a sua posição.

17. `isArray(obj)`: Verifica se um objeto é um array.

18. `join(separator)`: Junta todos os elementos do array em uma string, usando um separador especificado.

19. `keys()`: Retorna um iterador contendo as chaves do array.

20. `lastIndexOf(searchElement, fromIndex)`: Procura o array por um elemento, começando pelo final, e retorna a sua posição.

21. `length`: Define ou retorna o número de elementos em um array.

22. `map(callback(element, index, array), thisArg)`: Cria um novo array com o resultado da chamada de uma função de retorno para cada elemento do array.

23. `pop()`: Remove o último elemento de um array e o retorna.

24. `prototype`: Permite adicionar propriedades e métodos ao objeto Array.

25. `push(element1, element2, ..., elementN)`: Adiciona novos elementos no final do array e retorna o novo comprimento do array.

26. `reduce(callback(accumulator, currentValue, index, array), initialValue)`: Reduz os valores de um array a um único valor (iterando da esquerda para a direita).

27. `reduceRight(callback(accumulator, currentValue, index, array), initialValue)`: Reduz os valores de um array a um único valor (iterando da direita para a esquerda).

28. `reverse()`: Inverte a ordem dos elementos em um array.

29. `shift()`: Remove o primeiro elemento de um array e o retorna.

30. `slice(start, end)`: Seleciona uma parte de um array e retorna um novo array.

31. `some(callback(element, index, array), thisArg)`: Verifica se algum dos elementos do array passa em um teste especificado por uma função de retorno.

32. `sort(compareFunction)`: Ordena os elementos de um array.

33. `splice(start, deleteCount, item1, item2, ..., itemN)`: Adiciona ou remove elementos de um array.

34. `toString()`: Converte um array para uma string e retorna o resultado.

35. `unshift(element1, element2, ..., elementN)`: Adiciona novos elementos no início de um array e retorna o novo comprimento do array.

36. `valueOf()`: Retorna o valor primitivo de um array.

## O Operador Spread em JavaScript

1. Copiando elementos de um array:
```javascript
const originalArray = [1, 2, 3];
const copiedArray = [...originalArray]; // Cria uma cópia do originalArray
```

2. Concatenando arrays:
```javascript
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const concatenatedArray = [...array1, ...array2]; // Concatena os arrays
```

3. Passando argumentos para uma função:
```javascript
function sum(a, b, c) {
  return a + b + c;
}

const numbers = [1, 2, 3];
const result = sum(...numbers); // Equivalente a sum(1, 2, 3)
```

4. Clonando objetos:
```javascript
const originalObject = { name: "John", age: 30 };
const clonedObject = { ...originalObject }; // Cria um clone do originalObject
```

5. Mesclando objetos:
```javascript
const object1 = { a: 1, b: 2 };
const object2 = { c: 3, d: 4 };
const mergedObject = { ...object1, ...object2 }; // Mescla os objetos
```

6. Criando arrays a partir de uma string:
```javascript
const str = "hello";
const charArray = [...str]; // Cria um array ["h", "e", "l", "l", "o"]
```

## Iteração em JavaScript

1. **for...in**:
O `for...in` é usado para iterar sobre as propriedades enumeráveis de um objeto. Ele percorre as chaves (índices) de um objeto e pode ser utilizado tanto para listas quanto para dicionários (objetos). No entanto, é importante tomar cuidado com seu uso em listas, pois ele pode não percorrer os elementos na ordem desejada e pode incluir propriedades herdadas indesejadas.

Exemplo de uso em objeto (dicionário):
```javascript
const person = {
  name: "John",
  age: 30,
  city: "New York"
};
for (let key in person) {
  console.log(key + ": " + person[key]);
}
```

2. **for...of**:
O `for...of` foi introduzido no ECMAScript 6 (ES6) e é mais adequado para percorrer elementos de listas e conjuntos. Ele itera sobre os valores de objetos iteráveis, como arrays e Sets. O `for...of` não percorre as propriedades enumeráveis de um objeto, portanto, não é adequado para dicionários.

Exemplo de uso em array (lista):
```javascript
const fruits = ["apple", "banana", "orange"];
for (let fruit of fruits) {
  console.log(fruit);
}
```

Exemplo de uso em conjunto (Set):
```javascript
const numberSet = new Set([1, 2, 3]);
for (let num of numberSet) {
  console.log(num);
}
```

Em resumo:
- Use o `for...in` para percorrer as propriedades enumeráveis de objetos (dicionários).
- Use o `for...of` para percorrer elementos de listas e conjuntos (Sets).

## Pilha em JavaScript

```javascript
// Criar uma pilha vazia
const stack = [];
// Adicionar elementos na pilha (no topo)
stack.push(1);
stack.push(2);
stack.push(3);
// Remover o elemento do topo da pilha
const removedElement = stack.pop();
console.log(removedElement); // Output: 3
// Acessar o elemento do topo da pilha sem removê-lo
const topElement = stack[stack.length - 1];
console.log(topElement); // Output: 2
// Verificar se a pilha está vazia
const isEmpty = stack.length === 0;
console.log(isEmpty); // Output: false
// Tamanho da pilha
const size = stack.length;
console.log(size); // Output: 2
// Limpar a pilha, removendo todos os elementos
stack.length = 0;
console.log(stack); // Output: []
```

## Fila em JavaScript

```javascript
// Criar uma fila vazia
const queue = [];
// Adicionar elementos na fila (no final)
queue.push(1);
queue.push(2);
queue.push(3);
// Remover o elemento do início da fila
const removedElement = queue.shift();
console.log(removedElement); // Output: 1
// Acessar o elemento do início da fila sem removê-lo
const frontElement = queue[0];
console.log(frontElement); // Output: 2
// Verificar se a fila está vazia
const isEmpty = queue.length === 0;
console.log(isEmpty); // Output: false
// Tamanho da fila
const size = queue.length;
console.log(size); // Output: 2
// Limpar a fila, removendo todos os elementos
queue.length = 0;
console.log(queue); // Output: []
```

## Dicionários em Python

Em Python, um dicionário é uma estrutura de dados que permite armazenar uma coleção de pares chave-valor. Cada chave em um dicionário deve ser única e imutável (como uma string, número ou tupla), enquanto os valores podem ser de qualquer tipo de dados. Os dicionários são representados por chaves `{}` e usam a sintaxe `chave: valor` para associar uma chave a um valor. Aqui estão algumas características importantes dos dicionários em Python:

1. Criação de um dicionário:
```python
dicionario_vazio = {}
dicionario_numeros = {'um': 1, 'dois': 2, 'três': 3}
dicionario_misturado = {1: 'abc', 'valor': True, (4, 5): [6, 7, 8]}
```

2. Acesso aos elementos:
Os valores dos dicionários são acessados usando as chaves associadas.
```python
dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
print(dicionario['nome'])    # Saída: 'João'
print(dicionario['idade'])   # Saída: 30
```

3. Modificação de elementos:
Você pode modificar os valores associados às chaves existentes ou adicionar novos pares chave-valor.
```python
dicionario = {'nome': 'João', 'idade': 30}
dicionario['idade'] = 31
dicionario['cidade'] = 'São Paulo'
print(dicionario)   # Saída: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo'}
```

4. Operações com dicionários:
```python
# Verificar se uma chave existe no dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3}
print('a' in dicionario)    # Saída: True
print('d' in dicionario)    # Saída: False

# Remover um par chave-valor do dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3}
del dicionario['b']
print(dicionario)   # Saída: {'a': 1, 'c': 3}

# Tamanho do dicionário (número de pares chave-valor)
tamanho = len(dicionario)
print(tamanho)      # Saída: 2
```

5. Funções úteis para dicionários:
```python
# Obter uma lista com todas as chaves do dicionário
dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
chaves = dicionario.keys()
print(chaves)       # Saída: dict_keys(['nome', 'idade', 'cidade'])

# Obter uma lista com todos os valores do dicionário
valores = dicionario.values()
print(valores)      # Saída: dict_values(['João', 30, 'São Paulo'])

# Obter uma lista de tuplas com todos os pares chave-valor do dicionário
itens = dicionario.items()
print(itens)        # Saída: dict_items([('nome', 'João'), ('idade', 30), ('cidade', 'São Paulo')])
```

Essas são algumas das funcionalidades básicas dos dicionários em Python. Os dicionários são amplamente usados para armazenar dados de forma associativa, onde cada valor é acessado através de uma chave significativa.

### Funções de Dicionário em Python

1. `clear()`: Remove todos os itens do dicionário.
   - Parâmetros: Não possui parâmetros.

2. `copy()`: Retorna uma cópia superficial (shallow copy) do dicionário.
   - Parâmetros: Não possui parâmetros.

3. `fromkeys()`: Cria um dicionário a partir da sequência fornecida, usando os elementos da sequência como chaves e um valor padrão para todos os elementos.
   - Parâmetros:
     - `seq`: A sequência (lista, tupla, conjunto, etc.) cujos elementos serão usados como chaves do dicionário.
     - `value` (opcional): O valor padrão que será atribuído a todas as chaves do dicionário (padrão é None se não for fornecido).

4. `get()`: Retorna o valor associado à chave fornecida no dicionário.
   - Parâmetros:
     - `key`: A chave cujo valor associado você deseja obter.
     - `default` (opcional): O valor padrão retornado se a chave não estiver presente no dicionário (padrão é None se não for fornecido).

5. `items()`: Retorna uma lista de tuplas contendo todos os pares chave-valor do dicionário.
   - Parâmetros: Não possui parâmetros.

6. `keys()`: Retorna uma view object (visão) que exibe uma lista de todas as chaves do dicionário na ordem em que foram inseridas.
   - Parâmetros: Não possui parâmetros.

7. `pop()`: Remove e retorna o valor associado à chave fornecida.
   - Parâmetros:
     - `key`: A chave cujo valor associado você deseja remover e retornar.

8. `popitem()`: Remove e retorna um par chave-valor aleatório do dicionário.
   - Parâmetros: Não possui parâmetros.

9. `setdefault()`: Retorna o valor associado à chave, se a chave estiver presente no dicionário. Caso contrário, insere a chave com o valor fornecido e retorna o valor fornecido.
   - Parâmetros:
     - `key`: A chave que você deseja verificar e possivelmente inserir no dicionário.
     - `default` (opcional): O valor que será atribuído à chave se a chave não estiver presente no dicionário (padrão é None se não for fornecido).

10. `update()`: Atualiza o dicionário com os elementos de outro dicionário ou com pares chave-valor de um iterável (como uma lista de tuplas).
    - Parâmetros:
      - `other`: Um dicionário ou um iterável contendo pares chave-valor que serão adicionados ou atualizados no dicionário original.

11. `values()`: Retorna uma lista de todos os valores disponíveis no dicionário.
    - Parâmetros: Não possui parâmetros.

## Conjuntos em Python

1. Criação de um conjunto:
```python
conjunto_vazio = set()
conjunto_numeros = {1, 2, 3, 4, 5}
conjunto_misturado = {1, "abc", True, (6, 7, 8)}
```

2. Acesso a elementos:
Os conjuntos não são indexados, portanto, você não pode acessar elementos individuais por índices.
```python
conjunto = {10, 20, 30, 40, 50}
# Não é possível acessar um elemento específico como conjunto[0]
```

3. Mutabilidade:
Os conjuntos são mutáveis, o que significa que você pode adicionar e remover elementos após a sua criação.
```python
conjunto = {1, 2, 3}
conjunto.add(4)     # Adiciona o elemento 4 ao conjunto
conjunto.remove(2)  # Remove o elemento 2 do conjunto
```

4. Operações com conjuntos:
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
# União de conjuntos
uniao = conjunto1.union(conjunto2)
# ou usando o operador "|"
uniao = conjunto1 | conjunto2
print(uniao)   # Saída: {1, 2, 3, 4, 5}
# Interseção de conjuntos
intersecao = conjunto1.intersection(conjunto2)
# ou usando o operador "&"
intersecao = conjunto1 & conjunto2
print(intersecao)   # Saída: {3}
# Diferença entre conjuntos
diferenca = conjunto1.difference(conjunto2)
# ou usando o operador "-"
diferenca = conjunto1 - conjunto2
print(diferenca)   # Saída: {1, 2}
# Verificar se um conjunto é subconjunto de outro
subset = conjunto1.issubset(conjunto2)
print(subset)   # Saída: False
```

5. Funções úteis para conjuntos:
```python
# Tamanho do conjunto (número de elementos)
conjunto = {1, 2, 3, 4, 5}
tamanho = len(conjunto)
print(tamanho)   # Saída: 5
# Remover um elemento do conjunto usando discard (sem erro se o elemento não existir)
conjunto.discard(3)
print(conjunto)  # Saída: {1, 2, 4, 5}
# Limpar o conjunto, removendo todos os elementos
conjunto.clear()
print(conjunto)  # Saída: set()
```

### Funções de Conjuntos em Python

1. `add()`: Adiciona um elemento ao conjunto.
   - Parâmetro: O valor do elemento que você deseja adicionar ao conjunto.

2. `clear()`: Remove todos os elementos do conjunto.
   - Parâmetros: Não possui parâmetros.

3. `copy()`: Retorna uma cópia do conjunto.
   - Parâmetros: Não possui parâmetros.

4. `difference()`: Retorna um conjunto contendo a diferença entre dois ou mais conjuntos.
   - Parâmetros: Pode receber um ou mais conjuntos como argumentos.

5. `difference_update()`: Remove os itens deste conjunto que também estão presentes em outro conjunto especificado.
   - Parâmetros: Pode receber um ou mais conjuntos como argumentos.

6. `discard()`: Remove o item especificado do conjunto, se estiver presente. Se o item não estiver no conjunto, não ocorre nenhum erro.
   - Parâmetro: O valor do elemento que você deseja remover do conjunto.

7. `intersection()`: Retorna um conjunto que é a interseção de dois ou mais conjuntos.
   - Parâmetros: Pode receber um ou mais conjuntos como argumentos.

8. `intersection_update()`: Remove os itens deste conjunto que não estão presentes em outros conjuntos especificados.
   - Parâmetros: Pode receber um ou mais conjuntos como argumentos.

9. `isdisjoint()`: Retorna um valor booleano que indica se dois conjuntos têm interseção ou não (True se não tiverem interseção, False se tiverem interseção).
   - Parâmetro: O conjunto com o qual você deseja verificar se o conjunto atual tem interseção.

10. `issubset()`: Retorna um valor booleano que indica se outro conjunto contém este conjunto (True se for subconjunto, False se não for).
    - Parâmetro: O conjunto com o qual você deseja verificar se o conjunto atual é subconjunto.

11. `issuperset()`: Retorna um valor booleano que indica se este conjunto contém outro conjunto (True se for superconjunto, False se não for).
    - Parâmetro: O conjunto com o qual você deseja verificar se o conjunto atual é superconjunto.

12. `pop()`: Remove e retorna um elemento aleatório do conjunto.
    - Parâmetros: Não possui parâmetros.

13. `remove()`: Remove o elemento especificado do conjunto.
    - Parâmetro: O valor do elemento que você deseja remover do conjunto.

14. `symmetric_difference()`: Retorna um conjunto com as diferenças simétricas de dois conjuntos (elementos que estão em um conjunto ou no outro, mas não em ambos).
    - Parâmetros: Pode receber um ou mais conjuntos como argumentos.

15. `symmetric_difference_update()`: Insere as diferenças simétricas deste conjunto e outro conjunto especificado.
    - Parâmetros: Pode receber um ou mais conjuntos como argumentos.

16. `union()`: Retorna um conjunto contendo a união de dois ou mais conjuntos (todos os elementos únicos presentes em todos os conjuntos).
    - Parâmetros: Pode receber um ou mais conjuntos como argumentos.

17. `update()`: Atualiza o conjunto com outro conjunto ou qualquer outro iterável (como uma lista, tupla, etc.).
    - Parâmetro: O conjunto ou iterável que você deseja usar para atualizar o conjunto atual.

## Tuplas em Python

1. Criação de uma tupla:
```python
tupla_vazia = ()
tupla_numeros = (1, 2, 3, 4, 5)
tupla_misturada = (1, "abc", True, (6, 7, 8))
```

2. Acesso a elementos:
Os elementos de uma tupla são acessados através de índices, da mesma forma que em listas.
```python
tupla = (10, 20, 30, 40, 50)
print(tupla[0])   # Saída: 10
print(tupla[2])   # Saída: 30
print(tupla[-1])  # Saída: 50 (índice negativo representa contagem a partir do final)
```

3. Imutabilidade:
Uma vez criada, a tupla não pode ser alterada. Tentar modificar seus elementos resultará em um erro.
```python
tupla = (1, 2, 3)
tupla[0] = 10  # Isso resultará em um TypeError, pois as tuplas são imutáveis
```

4. Operações com tuplas:
```python
# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Saída: (1, 2, 3, 4, 5, 6)
# Repetição de tuplas
tupla_repetida = tupla1 * 3
print(tupla_repetida)  # Saída: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

5. Funções úteis para tuplas:
```python
# Tamanho da tupla
tupla = (1, 2, 3, 4, 5)
tamanho = len(tupla)
print(tamanho)  # Saída: 5
# Encontrar o índice de um elemento
indice = tupla.index(3)
print(indice)   # Saída: 2
# Contar o número de ocorrências de um elemento
ocorrencias = tupla.count(2)
print(ocorrencias)  # Saída: 1
```

## Listas em Python

1. Criação de uma lista:
```python
lista_vazia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_misturada = [1, "abc", True, [6, 7, 8]]
```

2. Acesso a elementos:
Os elementos da lista são acessados através de índices, onde o primeiro elemento tem índice 0, o segundo tem índice 1 e assim por diante.
```python
lista = [10, 20, 30, 40, 50]
print(lista[0])   # Saída: 10
print(lista[2])   # Saída: 30
print(lista[-1])  # Saída: 50 (índice negativo representa contagem a partir do final)
```

3. Modificação de elementos:
Você pode modificar os elementos de uma lista atribuindo um novo valor ao índice correspondente.
```python
lista = [10, 20, 30]
lista[1] = 25
print(lista)   # Saída: [10, 25, 30]
```

4. Operações com listas:
```python
# Concatenação
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)  # Saída: [1, 2, 3, 4, 5, 6]
# Repetição
lista_repetida = lista1 * 3
print(lista_repetida)  # Saída: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

5. Funções úteis para listas:
```python
# Tamanho da lista
lista = [1, 2, 3, 4, 5]
tamanho = len(lista)
print(tamanho)  # Saída: 5
# Adicionar elementos ao final da lista
lista.append(6)
print(lista)    # Saída: [1, 2, 3, 4, 5, 6]
# Remover elemento pelo valor
lista.remove(3)
print(lista)    # Saída: [1, 2, 4, 5, 6]
# Índice do primeiro elemento encontrado
indice = lista.index(4)
print(indice)   # Saída: 2
# Ordenar a lista em ordem crescente
lista.sort()
print(lista)    # Saída: [1, 2, 4, 5, 6]
# Inverter a ordem dos elementos
lista.reverse()
print(lista)    # Saída: [6, 5, 4, 2, 1]
```

Essas são apenas algumas das funcionalidades básicas das listas em Python. Elas são amplamente usadas devido à sua flexibilidade e facilidade de uso em várias aplicações.

### Funções de Lista em Python

1. `append()`: Usado para adicionar elementos ao final da lista.
   - Parâmetros: Recebe um único argumento, que é o elemento que você deseja adicionar à lista.

2. `copy()`: Retorna uma cópia superficial (shallow copy) da lista.
   - Parâmetros: Não possui parâmetros.

3. `clear()`: Remove todos os itens da lista.
   - Parâmetros: Não possui parâmetros.

4. `count()`: Conta o número de ocorrências de um elemento na lista.
   - Parâmetro: Recebe um único argumento, que é o elemento cujas ocorrências você deseja contar.

5. `extend()`: Adiciona cada elemento de um iterável (como outra lista, tupla, conjunto, etc.) ao final da lista.
   - Parâmetro: Recebe um único argumento, que é o iterável que você deseja adicionar à lista.

6. `index()`: Retorna o índice da primeira ocorrência de um elemento na lista.
   - Parâmetros: Recebe um argumento obrigatório, que é o elemento cujo índice você deseja encontrar. Opcionalmente, você pode especificar os índices de início e fim da busca.

7. `insert()`: Insere um elemento em um índice específico na lista.
   - Parâmetros: Recebe dois argumentos, o primeiro é o índice onde você deseja inserir o elemento, e o segundo é o elemento que você deseja inserir.

8. `pop()`: Remove e retorna o último elemento da lista ou o elemento no índice especificado.
   - Parâmetro: Opcionalmente, você pode fornecer o índice do elemento que deseja remover e retornar.

9. `remove()`: Remove a primeira ocorrência de um elemento específico da lista.
   - Parâmetro: Recebe um único argumento, que é o elemento que você deseja remover da lista.

10. `reverse()`: Inverte a ordem dos elementos da lista in-place (ou seja, alterando a própria lista).
    - Parâmetros: Não possui parâmetros.

11. `sort()`: Classifica a lista em ordem ascendente, descendente ou com uma ordem personalizada definida por uma função.
    - Parâmetros: 
       - `key` (opcional): Uma função que define a ordem personalizada dos elementos.
       - `reverse` (opcional): Um booleano para especificar se a lista deve ser classificada em ordem decrescente (True) ou não (False).

12. `min()`: Retorna o menor elemento da lista.
    - Parâmetros: Não possui parâmetros.

13. `max()`: Retorna o maior elemento da lista.
    - Parâmetros: Não possui parâmetros.

## Funções Comuns de Sequências em Python

Aqui está uma descrição detalhada das funções comuns de sequências em Python, juntamente com seus parâmetros e notas:

1. `x in s`: Retorna True se um item de `s` é igual a `x`, caso contrário, retorna False.
   - Parâmetros: `x`: O valor que você deseja verificar se está presente na sequência `s`.

2. `x not in s`: Retorna False se um item de `s` é igual a `x`, caso contrário, retorna True.
   - Parâmetros: `x`: O valor que você deseja verificar se não está presente na sequência `s`.

3. `s + t`: Concatenação da sequência `s` com a sequência `t`.
   - Parâmetros: `s`: A primeira sequência que você deseja concatenar.
                 `t`: A segunda sequência que você deseja concatenar.

4. `s * n or n * s`: Retorna uma nova sequência que é equivalente a adicionar a sequência `s` a si mesma `n` vezes.
   - Parâmetros: `s`: A sequência que você deseja repetir.
                 `n`: O número de vezes que você deseja repetir a sequência.

5. `s[i]`: Retorna o item na posição `i` da sequência `s`.
   - Parâmetros: `i`: O índice do item que você deseja obter da sequência.

6. `s[i:j]`: Retorna uma fatia (slice) da sequência `s` do índice `i` até o índice `j-1`.
   - Parâmetros: `i`: O índice de início da fatia.
                 `j`: O índice de parada (não inclusivo) da fatia.

7. `s[i:j:k]`: Retorna uma fatia (slice) da sequência `s` do índice `i` até o índice `j-1` com passo `k`.
   - Parâmetros: `i`: O índice de início da fatia.
                 `j`: O índice de parada (não inclusivo) da fatia.
                 `k`: O valor do passo que determina o intervalo entre os elementos da fatia.

8. `len(s)`: Retorna o comprimento da sequência `s`.
   - Parâmetros: Não possui parâmetros.

9. `min(s)`: Retorna o menor item da sequência `s`.
   - Parâmetros: Não possui parâmetros.

10. `max(s)`: Retorna o maior item da sequência `s`.
    - Parâmetros: Não possui parâmetros.

11. `s.index(x[, i[, j]])`: Retorna o índice da primeira ocorrência de `x` na sequência `s`, a partir do índice `i` e antes do índice `j`.
    - Parâmetros: `x`: O valor que você deseja encontrar na sequência.
                  `i` (opcional): O índice inicial para iniciar a busca (padrão é 0).
                  `j` (opcional): O índice final para encerrar a busca (padrão é o comprimento da sequência).

12. `s.count(x)`: Retorna o número total de ocorrências de `x` na sequência `s`.
    - Parâmetros: `x`: O valor cujo número de ocorrências você deseja contar na sequência.

Notas:
- (1): `in` e `not in` são operadores de pertencimento, aplicados para verificar se um valor está ou não presente na sequência.
- (2): A multiplicação de uma sequência por um número inteiro cria uma nova sequência repetindo a original várias vezes.
- (3): O acesso a elementos individuais da sequência ou a criação de uma fatia é feito usando colchetes `[]`.
- (4): Quando usando uma fatia, o índice de parada é exclusivo, ou seja, o elemento no índice `j` não está incluído na fatia.
- (5): O parâmetro de passo `k` determina o intervalo entre os elementos da fatia. Se omitido, o padrão é 1.
- (6): A concatenação de sequências é feita usando o operador `+`.
- (7): A multiplicação de sequências é feita usando o operador `*`.
- (8): Se `x` não estiver presente na sequência, uma exceção `ValueError` será lançada.

## Compreensão de Listas em Python

List comprehension é uma forma concisa e elegante de criar listas em Python.

```python
[expressão for elemento in iterável if condição]
```

- `expressão`: A expressão que será aplicada a cada elemento do iterável para criar os elementos da lista resultante.
- `elemento`: A variável que representa cada elemento do iterável.
- `iterável`: O iterável (lista, tupla, conjunto, etc.) que será percorrido para criar a lista.
- `condição` (opcional): Uma expressão condicional que pode ser usada para filtrar elementos com base em uma condição.

A list comprehension é equivalente a escrever um loop for e, em seguida, usar o método `append()` para adicionar elementos a uma lista.

```python
quadrados = [x**2 for x in range(10)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Aqui estão alguns exemplos adicionais de list comprehension:

1. Criando uma lista de números pares de 0 a 9:
```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8]
```

2. Criando uma lista de palavras em maiúsculas a partir de uma lista de strings:
```python
frutas = ['maçã', 'banana', 'laranja', 'uva']
frutas_maiusculas = [fruta.upper() for fruta in frutas]
print(frutas_maiusculas)  # Saída: ['MAÇÃ', 'BANANA', 'LARANJA', 'UVA']
```

3. Criando uma lista de tuplas com elementos de duas listas:
```python
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
combinacoes = [(n, l) for n in numeros for l in letras]
print(combinacoes)  # Saída: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
```

## O Operador Spread em Python

1. Desempacotamento de listas e tuplas:
O operador spread pode ser usado para desempacotar os elementos de uma lista ou tupla e atribuí-los a variáveis individuais:

```python
# Desempacotamento de uma lista
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
# Desempacotamento de uma tupla
my_tuple = (4, 5, 6)
x, y, z = my_tuple
print(x)  # Output: 4
print(y)  # Output: 5
print(z)  # Output: 6
```

2. Unindo listas:
Você pode usar o operador spread para unir elementos de várias listas em uma única lista:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]
```

3. Criando cópias de listas e dicionários:
O operador spread também permite criar cópias de listas e dicionários:

```python
original_list = [1, 2, 3]
copied_list = [*original_list]
print(copied_list)  # Output: [1, 2, 3]

original_dict = {'a': 1, 'b': 2}
copied_dict = {**original_dict}
print(copied_dict)  # Output: {'a': 1, 'b': 2}
```

4. Passando argumentos para funções:
O operador spread pode ser usado para passar elementos de uma lista ou tupla como argumentos para uma função:

```python
def sum_numbers(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = sum_numbers(*numbers)
print(result)  # Output: 6
```

5. Unindo dicionários:
O operador spread pode ser usado para unir dicionários:

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## Pilha em Python

```python
# Criar uma pilha vazia
stack = []

# Empilhar elementos
stack.append(1)
stack.append(2)
stack.append(3)

# Desempilhar elemento
removed_element = stack.pop()
print(removed_element)  # Output: 3

# Acessar o elemento do topo da pilha sem desempilhar
top_element = stack[-1]
print(top_element)  # Output: 2

# Verificar se a pilha está vazia
is_empty = len(stack) == 0
print(is_empty)  # Output: False

# Tamanho da pilha
size = len(stack)
print(size)  # Output: 2

# Limpar a pilha, removendo todos os elementos
stack.clear()
print(stack)  # Output: []
```

## Fila em Python

```python
from collections import deque

# Criar uma fila vazia
fila = deque()

# Adicionar elementos na fila
fila.append(1)
fila.append(2)
fila.append(3)

# Remover elementos do início da fila
elemento_removido = fila.popleft()
print(elemento_removido)  # Output: 1

# Acessar o elemento do início da fila sem removê-lo
primeiro_elemento = fila[0]
print(primeiro_elemento)  # Output: 2

# Verificar se a fila está vazia
esta_vazia = len(fila) == 0
print(esta_vazia)  # Output: False

# Tamanho da fila
tamanho = len(fila)
print(tamanho)  # Output: 2

# Limpar a fila, removendo todos os elementos
fila.clear()
print(fila)  # Output: deque([])
```

## Collections em Python

1. `namedtuple()`: Esta é uma função de fábrica para criar subclasses de tuplas com campos nomeados. Ela permite definir uma estrutura semelhante a classes simples para suas tuplas, onde cada campo tem um nome e pode ser acessado usando notação de ponto. Isso é particularmente útil quando você deseja criar estruturas de dados imutáveis e leves com atributos nomeados.

2. `deque`: Este é um contêiner semelhante a uma lista que fornece inserções e remoções rápidas em ambas as extremidades. "deque" significa "fila de dupla extremidade". Ele permite a inserção e remoção eficiente de elementos em ambas as extremidades da fila, tornando-o uma escolha adequada para implementar filas e pilhas.

3. `ChainMap`: Esta é uma classe semelhante a um dicionário que cria uma visão única de várias estruturas de mapeamento (dicionários). Ela permite combinar vários dicionários em uma única visão lógica sem criar um novo dicionário. Quando você procura uma chave no ChainMap, ele pesquisa cada dicionário subjacente na ordem até encontrar a chave.

4. `Counter`: Esta é uma subclasse de dicionário projetada especificamente para contar objetos hasháveis. Ela permite contar eficientemente as ocorrências de elementos em uma coleção, criando um mapeamento entre o elemento e sua contagem. É comumente usado para realizar análise de frequência em dados.

5. `OrderedDict`: Esta é uma subclasse de dicionário que lembra a ordem em que as entradas foram adicionadas. Ao contrário de um dicionário comum, um OrderedDict mantém a ordem de inserção, o que significa que, quando você itera sobre ele, os itens são retornados na ordem em que foram adicionados.

6. `defaultdict`: Esta é uma subclasse de dicionário que chama uma função de fábrica para fornecer valores padrão quando uma chave é acessada e não está presente no dicionário. Ao criar um defaultdict, você especifica um valor padrão que será retornado se uma chave não for encontrada, podendo ser um tipo incorporado ou uma função chamável (como uma função).

7. `UserDict`: Esta é uma estrutura que envolve objetos de dicionário e fornece uma maneira mais fácil de criar subclasses de dicionários. Ela permite criar classes personalizadas semelhantes a dicionários, subclasseando `UserDict` em vez de subclassear diretamente o dicionário incorporado. Isso pode tornar mais simples substituir métodos específicos e personalizar o comportamento da sua classe personalizada de dicionário.

8. `UserList`: Esta é uma estrutura que envolve objetos de lista e fornece uma maneira mais fácil de criar subclasses de listas. Semelhante ao `UserDict`, ela permite criar classes personalizadas semelhantes a listas, subclasseando `UserList` em vez de subclassear diretamente a lista incorporada.

9. `UserString`: Esta é uma estrutura que envolve objetos de string e fornece uma maneira mais fácil de criar subclasses de strings. Assim como `UserDict` e `UserList`, ela permite criar classes personalizadas semelhantes a strings, subclasseando `UserString` em vez de subclassear diretamente a string incorporada.

## Arrays em Java

1. Declaração de um array:
```java
tipo[] nomeDoArray; // Sintaxe mais comum
tipo nomeDoArray[]; // Alternativa válida
```

2. Inicialização de um array:
```java
// Forma 1: Com tamanho e valores específicos
int[] numeros = new int[]{1, 2, 3, 4, 5};
// Forma 2: Com tamanho específico, mas valores inicializados com valor padrão
int[] idades = new int[5]; // Por padrão, todos os elementos são inicializados com 0
// Forma 3: Com valores específicos, a declaração pode ser simplificada
int[] outroArray = {10, 20, 30};
```

3. Acessando elementos do array:
```java
int[] numeros = {1, 2, 3, 4, 5};
int primeiroElemento = numeros[0]; // Acessa o primeiro elemento (valor 1)
int terceiroElemento = numeros[2]; // Acessa o terceiro elemento (valor 3)
```

4. Alterando elementos do array:
```java
int[] numeros = {1, 2, 3};
numeros[1] = 10; // Altera o segundo elemento para o valor 10
```

5. Obtendo o tamanho do array:
```java
int[] numeros = {1, 2, 3, 4, 5};
int tamanho = numeros.length; // Retorna o tamanho do array (neste caso, 5)
```

6. Percorrendo elementos do array:
```java
int[] numeros = {1, 2, 3, 4, 5};
for (int i = 0; i < numeros.length; i++) {
    System.out.println(numeros[i]);
}
// A partir do Java 5, pode-se utilizar o loop for-each (for-each loop):
for (int numero : numeros) {
    System.out.println(numero);
}
```

7. Arrays multidimensionais:
```java
int[][] matriz = new int[3][3]; // Matriz 3x3 inicializada com valores padrão (0)
int[][] outraMatriz = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}; // Matriz 3x3 com valores específicos
```

### Funçoes com Arrays em Java

A classe `Arrays` em Java é uma classe utilitária que fornece várias funções para manipulação e operações em arrays. Abaixo estão as descrições concisas e os parâmetros de cada função da classe `Arrays` listada:

1. `asList(T... a)`
   - Descrição: Retorna uma lista de tamanho fixo apoiada pelo array especificado.
   - Parâmetros:
     - `a`: Uma série de elementos do tipo `T`.

2. `binarySearch(byte[] a, byte key)` / `binarySearch(byte[] a, int fromIndex, int toIndex, byte key)`
   - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave.
   - Parâmetros:
     - `a`: O array de bytes.
     - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
     - `toIndex` (opcional): O índice final para encerrar a pesquisa.
     - `key`: O valor de chave a ser procurado no array.

3. `binarySearch(char[] a, char key)` / `binarySearch(char[] a, int fromIndex, int toIndex, char key)`
   - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave.
   - Parâmetros:
     - `a`: O array de caracteres.
     - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
     - `toIndex` (opcional): O índice final para encerrar a pesquisa.
     - `key`: O valor de chave a ser procurado no array.

4. `binarySearch(double[] a, double key)` / `binarySearch(double[] a, int fromIndex, int toIndex, double key)`
   - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave.
   - Parâmetros:
     - `a`: O array de valores do tipo `double`.
     - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
     - `toIndex` (opcional): O índice final para encerrar a pesquisa.
     - `key`: O valor de chave a ser procurado no array.

5. `binarySearch(float[] a, float key)` / `binarySearch(float[] a, int fromIndex, int toIndex, float key)`
   - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave.
   - Parâmetros:
     - `a`: O array de valores do tipo `float`.
     - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
     - `toIndex` (opcional): O índice final para encerrar a pesquisa.
     - `key`: O valor de chave a ser procurado no array.

6. `binarySearch(int[] a, int key)` / `binarySearch(int[] a, int fromIndex, int toIndex, int key)`
   - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave.
   - Parâmetros:
     - `a`: O array de valores do tipo `int`.
     - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
     - `toIndex` (opcional): O índice final para encerrar a pesquisa.
     - `key`: O valor de chave a ser procurado no array.

7. `binarySearch(long[] a, long key)` / `binarySearch(long[] a, int fromIndex, int toIndex, long key)`
   - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave.
   - Parâmetros:
     - `a`: O array de valores do tipo `long`.
     - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
     - `toIndex` (opcional): O índice final para encerrar a pesquisa.
     - `key`: O valor de chave a ser procurado no array.

8. `binarySearch(Object[] a, Object key)` / `binarySearch(Object[] a, int fromIndex, int toIndex, Object key)`
   - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave.
   - Parâmetros:
     - `a`: O array de objetos.
     - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
     - `toIndex` (opcional): O índice final para encerrar a pesquisa.
     - `key`: O valor de chave a ser procurado no array.

9. `binarySearch(short[] a, short key)` / `binarySearch(short[] a, int fromIndex, int toIndex, short key)`
   - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave.
   - Parâmetros:
     - `a`: O array de valores do tipo `short`.
     - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
     - `toIndex` (opcional): O índice final para encerrar a pesquisa.
     - `key`: O valor de chave a ser procurado no array.

10. `binarySearch(T[] a, T key, Comparator<? super T> c)` / `binarySearch(T[] a, int fromIndex, int toIndex, T key, Comparator<? super T> c)`
    - Descrição: Executa uma pesquisa binária no array especificado para o valor de chave usando um comparador personalizado.
    - Parâmetros:
      - `a`: O array de objetos do tipo `T`.
      - `fromIndex` (opcional): O índice inicial para iniciar a pesquisa.
      - `toIndex` (opcional): O índice final para encerrar a pesquisa.
      - `key`: O valor de chave a ser procurado no array.
      - `c`: O comparador usado para ordenar o array.

11. `copyOf(boolean[] original, int newLength)` / `copyOf(byte[] original, int newLength)` / `copyOf(char[] original, int newLength)` / `copyOf(double[] original, int newLength)` / `copyOf(float[] original, int newLength)` / `copyOf(int[] original, int newLength)` / `copyOf(long[] original, int newLength)` / `copyOf(short[] original, int newLength)` / `copyOf(T[] original, int newLength)`
    - Descrição: Copia o array original, truncando ou preenchendo com valores padrão se necessário, de modo que a cópia tenha o comprimento especificado.
    - Parâmetros:
      - `original`: O array original a ser copiado.
      - `newLength`: O novo comprimento da cópia.

12. `copyOfRange(boolean[] original, int from, int to)` / `copyOfRange(byte[] original, int from, int to)` / `copyOfRange(char[] original, int from, int to)` / `copyOfRange(double[] original,

 int from, int to)` / `copyOfRange(float[] original, int from, int to)` / `copyOfRange(int[] original, int from, int to)` / `copyOfRange(long[] original, int from, int to)` / `copyOfRange(short[] original, int from, int to)` / `copyOfRange(T[] original, int from, int to)`
    - Descrição: Copia o intervalo especificado do array original em um novo array.
    - Parâmetros:
      - `original`: O array original a ser copiado.
      - `from`: O índice inicial do intervalo.
      - `to`: O índice final do intervalo (exclusivo).

13. `deepEquals(Object[] a1, Object[] a2)`
    - Descrição: Retorna true se os dois arrays especificados forem profundamente iguais um ao outro.
    - Parâmetros:
      - `a1`: O primeiro array de objetos.
      - `a2`: O segundo array de objetos.

14. `deepHashCode(Object[] a)`
    - Descrição: Retorna um código hash baseado nos "conteúdos profundos" do array especificado.
    - Parâmetros:
      - `a`: O array de objetos.

15. `deepToString(Object[] a)`
    - Descrição: Retorna uma representação de string dos "conteúdos profundos" do array especificado.
    - Parâmetros:
      - `a`: O array de objetos.

16. `equals(boolean[] a, boolean[] a2)` / `equals(byte[] a, byte[] a2)` / `equals(char[] a, char[] a2)` / `equals(double[] a, double[] a2)` / `equals(float[] a, float[] a2)` / `equals(int[] a, int[] a2)` / `equals(long[] a, long[] a2)` / `equals(Object[] a, Object[] a2)` / `equals(short[] a, short[] a2)`
    - Descrição: Retorna true se os dois arrays especificados do mesmo tipo forem iguais um ao outro.
    - Parâmetros:
      - `a`: O primeiro array.
      - `a2`: O segundo array.

17. Funções `fill()`:
    - Descrição: Atribui um valor especificado a cada elemento do array ou a um intervalo específico do array.
    - Parâmetros:
      - `a`: O array a ser preenchido.
      - `fromIndex` (opcional): O índice inicial para começar o preenchimento.
      - `toIndex` (opcional): O índice final para encerrar o preenchimento.
      - `val`: O valor a ser atribuído aos elementos do array.

18. Funções `parallelPrefix()`:
    - Descrição: Executa operações cumulativas (prefixo) em paralelo em cada elemento do array.
    - Parâmetros:
      - `array`: O array a ser processado.
      - `fromIndex` (opcional): O índice inicial para começar a operação.
      - `toIndex` (opcional): O índice final para encerrar a operação.
      - `op`: O operador binário usado para realizar a operação cumulativa.

19. Funções `parallelSetAll()`:
    - Descrição: Define todos os elementos do array em paralelo usando um gerador de valores.
    - Parâmetros:
      - `array`: O array a ser definido.
      - `generator`: A função geradora usada para calcular cada elemento do array.

20. Funções `parallelSort()`:
    - Descrição: Classifica os elementos do array em paralelo.
    - Parâmetros:
      - `array`: O array a ser classificado.
      - `fromIndex` (opcional): O índice inicial para começar a classificação.
      - `toIndex` (opcional): O índice final para encerrar a classificação.
      - `c` (opcional): O comparador usado para ordenar o array.

21. Funções `setAll()`:
    - Descrição: Define todos os elementos do array usando um gerador de valores.
    - Parâmetros:
      - `array`: O array a ser definido.
      - `generator`: A função geradora usada para calcular cada elemento do array.

22. Funções `sort()`:
    - Descrição: Classifica os elementos do array.
    - Parâmetros:
      - `array`: O array a ser classificado.
      - `fromIndex` (opcional): O índice inicial para começar a classificação.
      - `toIndex` (opcional): O índice final para encerrar a classificação.
      - `c` (opcional): O comparador usado para ordenar o array.

23. Funções `spliterator()`:
    - Descrição: Retorna um Spliterator que cobre todo o array ou um intervalo específico do array.
    - Parâmetros:
      - Diferentes assinaturas dependendo do tipo de array.

24. Funções `stream()`:
    - Descrição: Retorna um fluxo (Stream) com os elementos do array ou um intervalo

 específico do array.
    - Parâmetros:
      - Diferentes assinaturas dependendo do tipo de array.

25. Funções `toString()`:
    - Descrição: Retorna uma representação de string dos elementos do array.
    - Parâmetros:
      - Diferentes assinaturas dependendo do tipo de array.

## Listas em Java

1. ArrayList:
`ArrayList` é uma das classes mais comuns para implementar listas em Java. Ela implementa a interface `List` e armazena os elementos em um array dinâmico, permitindo o redimensionamento automático conforme necessário. Isso significa que a lista pode crescer ou encolher de acordo com a quantidade de elementos adicionados ou removidos.

```java
import java.util.ArrayList;
public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> listaDeNomes = new ArrayList<>();
        listaDeNomes.add("Alice");
        listaDeNomes.add("Bob");
        listaDeNomes.add("Carlos");
        System.out.println(listaDeNomes); // Saída: [Alice, Bob, Carlos]
    }
}
```

2. LinkedList:
`LinkedList` é uma lista duplamente encadeada em Java. Cada elemento (nó) na lista possui uma referência para o próximo e o anterior. Essa estrutura é útil para inserções e remoções frequentes, mas pode ser menos eficiente para acesso aleatório aos elementos.

```java
import java.util.LinkedList;
public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<Integer> listaDeNumeros = new LinkedList<>();
        listaDeNumeros.add(10);
        listaDeNumeros.add(20);
        listaDeNumeros.add(30);
        System.out.println(listaDeNumeros); // Saída: [10, 20, 30]
    }
}
```

### Funções de Lista em Java

1. `boolean add(E e)`
   - Adiciona o elemento especificado ao final da lista.
   - Parâmetro:
     - `e`: o elemento a ser adicionado.

2. `void add(int index, E element)`
   - Insere o elemento especificado na posição especificada na lista.
   - Parâmetros:
     - `index`: a posição na qual o elemento será inserido.
     - `element`: o elemento a ser inserido.

3. `boolean addAll(Collection<? extends E> c)`
   - Adiciona todos os elementos da coleção especificada ao final da lista.
   - Parâmetro:
     - `c`: a coleção contendo os elementos a serem adicionados.

4. `boolean addAll(int index, Collection<? extends E> c)`
   - Insere todos os elementos da coleção especificada na posição especificada na lista.
   - Parâmetros:
     - `index`: a posição na qual os elementos serão inseridos.
     - `c`: a coleção contendo os elementos a serem inseridos.

5. `void clear()`
   - Remove todos os elementos da lista.

6. `boolean contains(Object o)`
   - Retorna verdadeiro se a lista contém o elemento especificado.
   - Parâmetro:
     - `o`: o elemento a ser verificado.

7. `boolean containsAll(Collection<?> c)`
   - Retorna verdadeiro se a lista contém todos os elementos da coleção especificada.
   - Parâmetro:
     - `c`: a coleção contendo os elementos a serem verificados.

8. `boolean equals(Object o)`
   - Compara o objeto especificado com esta lista para igualdade.
   - Parâmetro:
     - `o`: o objeto a ser comparado.

9. `E get(int index)`
   - Retorna o elemento na posição especificada na lista.
   - Parâmetro:
     - `index`: a posição do elemento a ser retornado.

10. `int hashCode()`
    - Retorna o valor do código hash para esta lista.

11. `int indexOf(Object o)`
    - Retorna o índice da primeira ocorrência do elemento especificado na lista, ou -1 se o elemento não estiver presente.
    - Parâmetro:
      - `o`: o elemento a ser buscado.

12. `boolean isEmpty()`
    - Retorna verdadeiro se a lista não contiver elementos.

13. `Iterator<E> iterator()`
    - Retorna um iterador sobre os elementos da lista em sequência adequada.

14. `int lastIndexOf(Object o)`
    - Retorna o índice da última ocorrência do elemento especificado na lista, ou -1 se o elemento não estiver presente.
    - Parâmetro:
      - `o`: o elemento a ser buscado.

15. `ListIterator<E> listIterator()`
    - Retorna um iterador de lista sobre os elementos da lista em sequência adequada.

16. `ListIterator<E> listIterator(int index)`
    - Retorna um iterador de lista sobre os elementos da lista em sequência adequada, começando na posição especificada na lista.
    - Parâmetro:
      - `index`: a posição inicial do iterador.

17. `E remove(int index)`
    - Remove o elemento na posição especificada na lista.
    - Parâmetro:
      - `index`: a posição do elemento a ser removido.

18. `boolean remove(Object o)`
    - Remove a primeira ocorrência do elemento especificado da lista, se presente.
    - Parâmetro:
      - `o`: o elemento a ser removido.

19. `boolean removeAll(Collection<?> c)`
    - Remove da lista todos os elementos que estão contidos na coleção especificada.
    - Parâmetro:
      - `c`: a coleção contendo os elementos a serem removidos.

20. `default void replaceAll(UnaryOperator<E> operator)`
    - Substitui cada elemento da lista pelo resultado da aplicação do operador a esse elemento.
    - Parâmetro:
      - `operator`: o operador a ser aplicado aos elementos.

21. `boolean retainAll(Collection<?> c)`
    - Retém apenas os elementos na lista que estão contidos na coleção especificada.
    - Parâmetro:
      - `c`: a coleção contendo os elementos a serem retidos.

22. `E set(int index, E element)`
    - Substitui o elemento na posição especificada na lista pelo elemento especificado.
    - Parâmetros:
      - `index`: a posição do elemento a ser substituído.
      - `element`: o novo elemento a ser colocado na posição especificada.

23. `int size()`
    - Retorna o número de elementos na lista.

24. `default void sort(Comparator<? super E> c)`
    - Ordena esta lista de acordo com a ordem induzida pelo comparador especificado.
    - Parâmetro:
      - `c`: o comparador utilizado para a ordenação.

25. `default Spliterator<E> spliterator()`
    - Cria um Spliterator sobre os elementos da lista.

26. `List<E> subList(int fromIndex, int toIndex)`
    - Retorna uma visão da porção desta lista entre o `fromIndex` (inclusive) e o `toIndex` (exclusivo).
    - Parâmetros:
      - `fromIndex`: o índice inicial da visão.
      - `toIndex`: o índice final da visão.

27. `Object[] toArray()`
    - Retorna um array contendo todos os elementos da lista em sequência adequada (do primeiro ao último elemento).

28. `<T> T[] toArray(T[] a)`
    - Retorna um array contendo todos os elementos da lista em sequência adequada (do primeiro ao último elemento), com o tipo de tempo de execução do array especificado.

## Tuplas em Java

1. **Usando Arrays:** Você pode usar arrays para criar tuplas em Java, onde cada elemento do array representa um valor da tupla. Por exemplo:

```java
Object[] tuple = { 10, "Hello", true };
```

2. **Usando Classes Personalizadas:** Uma abordagem mais legível e escalável é criar uma classe personalizada que represente a tupla. Por exemplo:

```java
public class Tuple<A, B> {
    private A first;
    private B second;
    public Tuple(A first, B second) {
        this.first = first;
        this.second = second;
    }
    public A getFirst() {
        return first;
    }
    public B getSecond() {
        return second;
    }
}
// Exemplo de uso:
Tuple<Integer, String> tuple = new Tuple<>(10, "Hello");
```

3. **Usando Bibliotecas de Terceiros:** Algumas bibliotecas de terceiros, como o Apache Commons Lang, fornecem classes para tuplas em Java. Por exemplo:

```java
import org.apache.commons.lang3.tuple.Pair;
// Exemplo de uso:
Pair<Integer, String> tuple = Pair.of(10, "Hello");
```

## Conjuntos em Java

Em Java, conjuntos são uma estrutura de dados que representa uma coleção de elementos únicos, onde não são permitidos elementos duplicados. A interface principal para trabalhar com conjuntos é a interface `Set`, que é implementada por várias classes na biblioteca padrão do Java. Algumas das implementações mais comuns de conjuntos em Java são:

1. **HashSet**: É uma das implementações mais usadas. Armazena os elementos em uma tabela de dispersão, o que permite um acesso muito eficiente aos elementos. A ordem dos elementos pode não ser previsível.

```java
Set<String> hashSet = new HashSet<>();
hashSet.add("apple");
hashSet.add("banana");
hashSet.add("orange");
```

2. **LinkedHashSet**: Essa implementação mantém a ordem de inserção dos elementos, além de garantir a exclusão de elementos duplicados.

```java
Set<String> linkedHashSet = new LinkedHashSet<>();
linkedHashSet.add("apple");
linkedHashSet.add("banana");
linkedHashSet.add("orange");
```

3. **TreeSet**: Mantém os elementos ordenados de acordo com a ordem natural dos elementos ou com um comparador personalizado.

```java
Set<Integer> treeSet = new TreeSet<>();
treeSet.add(10);
treeSet.add(5);
treeSet.add(20);
```

4. **EnumSet**: É uma implementação especializada de conjuntos projetada para trabalhar com elementos de enumerações (enums).

```java
Set<DayOfWeek> enumSet = EnumSet.of(DayOfWeek.MONDAY, DayOfWeek.TUESDAY);
```

Aqui estão algumas das principais operações que você pode realizar em um conjunto em Java:

- **Adicionar um elemento**: `add(E e)`
- **Remover um elemento**: `remove(Object o)`
- **Verificar se contém um elemento**: `contains(Object o)`
- **Verificar se está vazio**: `isEmpty()`
- **Obter o tamanho do conjunto**: `size()`
- **Iterar sobre os elementos**: Usando um loop for-each ou um Iterator.

```java
for (String element : hashSet) {
    System.out.println(element);
}
```

## Funções de Coleções em Java

1. `static <T> boolean addAll(Collection<? super T> c, T... elements)`
   - Adiciona todos os elementos especificados à coleção especificada.
   - Parâmetros:
     - `c`: a coleção onde os elementos serão adicionados.
     - `elements`: os elementos a serem adicionados.

2. `static <T> Queue<T> asLifoQueue(Deque<T> deque)`
   - Retorna uma visualização de uma `Deque` como uma fila Last-in-first-out (Lifo).
   - Parâmetro:
     - `deque`: a `Deque` a ser convertida em fila Lifo.

3. `static <T> int binarySearch(List<? extends Comparable<? super T>> list, T key)`
   - Pesquisa o elemento especificado na lista usando o algoritmo de busca binária.
   - Parâmetros:
     - `list`: a lista onde a busca será realizada.
     - `key`: o elemento a ser pesquisado.

4. `static <T> int binarySearch(List<? extends T> list, T key, Comparator<? super T> c)`
   - Pesquisa o elemento especificado na lista usando o algoritmo de busca binária.
   - Parâmetros:
     - `list`: a lista onde a busca será realizada.
     - `key`: o elemento a ser pesquisado.
     - `c`: o comparador a ser usado para a busca.

5. `static <E> Collection<E> checkedCollection(Collection<E> c, Class<E> type)`
   - Retorna uma visualização dinamicamente tipada da coleção especificada.
   - Parâmetros:
     - `c`: a coleção a ser visualizada.
     - `type`: a classe do tipo esperado para os elementos da coleção.

6. `static <E> List<E> checkedList(List<E> list, Class<E> type)`
   - Retorna uma visualização dinamicamente tipada da lista especificada.
   - Parâmetros:
     - `list`: a lista a ser visualizada.
     - `type`: a classe do tipo esperado para os elementos da lista.

7. `static <K,V> Map<K,V> checkedMap(Map<K,V> m, Class<K> keyType, Class<V> valueType)`
   - Retorna uma visualização dinamicamente tipada do mapa especificado.
   - Parâmetros:
     - `m`: o mapa a ser visualizado.
     - `keyType`: a classe do tipo esperado para as chaves do mapa.
     - `valueType`: a classe do tipo esperado para os valores do mapa.

8. `static <K,V> NavigableMap<K,V> checkedNavigableMap(NavigableMap<K,V> m, Class<K> keyType, Class<V> valueType)`
   - Retorna uma visualização dinamicamente tipada do mapa navegável especificado.
   - Parâmetros:
     - `m`: o mapa navegável a ser visualizado.
     - `keyType`: a classe do tipo esperado para as chaves do mapa.
     - `valueType`: a classe do tipo esperado para os valores do mapa.

9. `static <E> NavigableSet<E> checkedNavigableSet(NavigableSet<E> s, Class<E> type)`
   - Retorna uma visualização dinamicamente tipada do conjunto navegável especificado.
   - Parâmetros:
     - `s`: o conjunto navegável a ser visualizado.
     - `type`: a classe do tipo esperado para os elementos do conjunto.

10. `static <E> Queue<E> checkedQueue(Queue<E> queue, Class<E> type)`
    - Retorna uma visualização dinamicamente tipada da fila especificada.
    - Parâmetros:
      - `queue`: a fila a ser visualizada.
      - `type`: a classe do tipo esperado para os elementos da fila.

11. `static <E> Set<E> checkedSet(Set<E> s, Class<E> type)`
    - Retorna uma visualização dinamicamente tipada do conjunto especificado.
    - Parâmetros:
      - `s`: o conjunto a ser visualizado.
      - `type`: a classe do tipo esperado para os elementos do conjunto.

12. `static <K,V> SortedMap<K,V> checkedSortedMap(SortedMap<K,V> m, Class<K> keyType, Class<V> valueType)`
    - Retorna uma visualização dinamicamente tipada do mapa ordenado especificado.
    - Parâmetros:
      - `m`: o mapa ordenado a ser visualizado.
      - `keyType`: a classe do tipo esperado para as chaves do mapa.
      - `valueType`: a classe do tipo esperado para os valores do mapa.

13. `static <E> SortedSet<E> checkedSortedSet(SortedSet<E> s, Class<E> type)`
    - Retorna uma visualização dinamicamente tipada do conjunto ordenado especificado.
    - Parâmetros:
      - `s`: o conjunto ordenado a ser visualizado.
      - `type`: a classe do tipo esperado para os elementos do conjunto.

14. `static <T> void copy(List<? super T> dest, List<? extends T> src)`
    - Copia todos os elementos de uma lista para outra.
    - Parâmetros:
      - `dest`: a lista de destino onde os elementos serão copiados.
      - `src`: a lista de origem de onde os elementos serão copiados.

15. `static boolean disjoint(Collection<?> c1, Collection<?> c2)`
    - Retorna verdadeiro se as duas coleções especificadas não têm elementos em comum.
    - Parâmetros:
      - `c1`: a primeira coleção.
      - `c2`: a segunda coleção.

16. `static <T> Enumeration<T> emptyEnumeration()`
    - Retorna uma enumeração vazia sem elementos.

17. `static <T> Iterator<T> emptyIterator()`
    - Retorna um iterador vazio sem elementos.

18. `static <T> List<T> emptyList()`
    - Retorna uma lista vazia (imutável).

19. `static <T> ListIterator<T> emptyListIterator()`
    - Retorna um iterador de lista vazio sem elementos.

20. `static <K,V> Map<K,V> emptyMap()`
    - Retorna um mapa vazio (imutável).

21. `static <K,V> NavigableMap<K,V> emptyNavigableMap()`
    - Retorna um mapa navegável vazio (imutável).

22. `static <E> NavigableSet<E> emptyNavigableSet()`
    - Retorna um conjunto navegável vazio (imutável).

23. `static <T> Set<T> emptySet()`
    - Retorna um conjunto vazio (imutável).

24. `static <K,V> SortedMap<K,V> emptySortedMap()`
    - Retorna um mapa ordenado vazio (imutável).

25. `static <E> SortedSet<E> emptySortedSet()`
    - Retorna um conjunto ordenado vazio (imutável).

26. `static <T> Enumeration<T> enumeration(Collection<T> c)`
    - Retorna uma enumeração sobre a coleção especificada.
    - Parâmetro:
      - `c`: a coleção a ser enumerada.

27. `static <T> void fill(List<? super T> list, T obj)`
    - Substitui todos os elementos da lista especificada pelo objeto especificado.
    - Parâmetros:
      - `list`: a lista a ser preenchida.
      - `obj`: o objeto para preencher a lista.

28. `static int frequency(Collection<?> c, Object o)`
    - Retorna o número de ocorrências do objeto especificado na coleção especificada.
    - Parâmetros:
      - `c`: a coleção onde será feita a contagem.
      - `o`: o objeto a ser contado.

29. `static int indexOfSubList(List<?> source, List<?> target)`
    - Retorna a posição inicial da primeira ocorrência da lista de destino na lista de origem, ou -1 se não houver tal ocorrência.
    - Parâmetros:
      - `source`: a lista de origem.
      - `target`: a lista de destino.

30. `static int lastIndexOfSubList(List<?> source, List<?> target)`
    - Retorna a posição inicial da última ocorrência da lista de destino na lista de origem, ou -1 se não houver tal ocorrência.
    - Parâmetros:
      - `source`: a lista de origem.
      - `target`: a lista de destino.

31. `static <T> ArrayList<T> list(Enumeration<T> e)`
    - Retorna uma lista de array contendo os elementos retornados pela enumeração especificada na ordem em que são retornados pela enumeração.
    - Parâmetro:
      - `e`: a enumeração a ser convertida em lista.

32. `static <T extends Object & Comparable<? super T>> T max(Collection<? extends T> coll)`
    - Retorna o elemento máximo da coleção fornecida, de acordo com a ordem natural de seus elementos.
    - Parâmetro:
      - `coll`: a coleção da qual o máximo será retornado.

33. `static <T> T max(Collection<? extends T> coll, Comparator<? super T> comp)`
    - Retorna o elemento máximo da coleção fornecida, de acordo com a ordem induzida pelo comparador especificado.
    - Parâmetros:
      - `coll`: a coleção da qual o máximo será retornado.
      - `comp`: o comparador utilizado para determinar a ordem.

34. `static <T extends Object & Comparable<? super T>> T min(Collection<? extends T> coll)`
    - Retorna o elemento mínimo da coleção fornecida, de acordo com a ordem natural de seus elementos.
    - Parâmetro:
      - `coll`: a coleção da qual o mínimo será retornado.

35. `static <T> T min(Collection<? extends T> coll, Comparator<? super T> comp)`
    - Retorna o elemento mínimo da coleção fornecida, de acordo com a ordem induzida pelo comparador especificado.
    - Parâmetros:
      - `coll`: a coleção da qual o mínimo será retornado.
      - `comp`: o comparador utilizado para determinar a ordem.

36. `static <T> List<T> nCopies(int n, T o)`
    - Retorna uma lista imutável consistindo em `n` cópias do objeto especificado.
    - Parâmetros:
      - `n`: o número de cópias do objeto a serem incluídas na lista.
      - `o`: o objeto a ser repetido na lista.

37. `static <E> Set<E> newSetFromMap(Map<E,Boolean> map)`
    - Retorna um conjunto suportado pelo mapa especificado.
    - Parâmetro:
      - `map`: o mapa a ser utilizado como suporte do conjunto.

38. `static <T> boolean replaceAll(List<T> list, T oldVal, T newVal)`
    - Substitui todas as ocorrências de um valor especificado por outro em uma lista.
    - Parâmetros:
      - `list`: a lista em que as substituições serão feitas.
      - `oldVal`: o valor a ser substituído.
      - `newVal`: o novo valor que substituirá o valor antigo.

39. `static void reverse(List<?> list)`
    - Inverte a ordem dos elementos na lista especificada.
    - Parâmetro:
      - `list`: a lista a ser invertida.

40. `static <T> Comparator<T> reverseOrder()`
    - Retorna um comparador que impõe a ordem reversa da ordenação natural de objetos que implementam a interface `Comparable`.

41. `static <T> Comparator<T> reverseOrder(Comparator<T> cmp)`
    - Retorna um comparador que impõe a ordem reversa de um comparador especificado.

42. `static void rotate(List<?> list, int distance)`
    - Gira os elementos da lista especificada pela distância especificada.
    - Parâmetros:
      - `list`: a lista a ser rotacionada.
      - `distance`: a distância de rotação.

43. `static void shuffle(List<?> list)`
    - Permuta aleatoriamente os elementos da lista usando uma fonte de aleatoriedade padrão.

44. `static void shuffle(List<?> list, Random rnd)`
    - Permuta aleatoriamente os elementos da lista usando uma fonte de aleatoriedade especificada.

45. `static <T> Set<T> singleton(T o)`
    - Retorna um conjunto imutável contendo apenas o objeto especificado.
    - Parâmetro:
      - `o`: o objeto a ser incluído no conjunto.

46. `static <T> List<T> singletonList(T o)`
    - Retorna uma lista imutável contendo apenas o objeto especificado.
    - Parâmetro:
      - `o`: o objeto a ser incluído na lista.

47. `static <K,V> Map<K,V> singletonMap(K key, V value)`
    - Retorna um mapa imutável contendo apenas uma única chave-valor especificada.
    - Parâmetros:
      - `key`: a chave a ser incluída no mapa.
      - `value`: o valor a ser associado à chave no mapa.

48. `static <T extends Comparable<? super T>> void sort(List<T> list)`
    - Ordena a lista especificada em ordem ascendente, de acordo com a ordenação natural de seus elementos.

49. `static <T> void sort(List<T> list, Comparator<? super T> c)`
    - Ordena a lista especificada de acordo com a ordem induzida pelo comparador especificado.
    - Parâmetros:
      - `list`: a lista a ser ordenada.
      - `c`: o comparador utilizado para determinar a ordem.

50. `static void swap(List<?> list, int i, int j)`
    - Troca os elementos nas posições especificadas na lista.
    - Parâmetros:
      - `list`: a lista onde as trocas serão realizadas.
      - `i`: a posição do primeiro elemento a ser trocado.
      - `j`: a posição do segundo elemento a ser trocado.

51. `static <T> Collection<T> synchronizedCollection(Collection<T> c)`
    - Retorna uma coleção sincronizada (thread-safe) com base na coleção especificada.
    - Parâmetro:
      - `c`: a coleção a ser sincronizada.

52. `static <T> List<T> synchronizedList(List<T> list)`
    - Retorna uma lista sincronizada (thread-safe) com base na lista especificada.
    - Parâmetro:
      - `list`: a lista a ser sincronizada.

53. `static <K,V> Map<K,V> synchronizedMap(Map<K,V> m)`
    - Retorna um mapa sincronizado (thread-safe) com base no mapa especificado.
    - Parâmetro:
      - `m`: o mapa a ser sincronizado.

54. `static <K,V> NavigableMap<K,V> synchronizedNavigableMap(NavigableMap<K,V> m)`
    - Retorna um mapa navegável sincronizado (thread-safe) com base no mapa navegável especificado.
    - Parâmetro:
      - `m`: o mapa navegável a ser sincronizado.

55. `static <T> NavigableSet<T> synchronizedNavigableSet(NavigableSet<T> s)`
    - Retorna um conjunto navegável sincronizado (thread-safe) com base no conjunto navegável especificado.
    - Parâmetro:
      - `s`: o conjunto navegável a ser sincronizado.

56. `static <T> Set<T> synchronizedSet(Set<T> s)`
    - Retorna um conjunto sincronizado (thread-safe) com base no conjunto especificado.
    - Parâmetro:
      - `s`: o conjunto a ser sincronizado.

57. `static <K,V> SortedMap<K,V> synchronizedSortedMap(SortedMap<K,V> m)`
    - Retorna um mapa ordenado sincronizado (thread-safe) com base no mapa ordenado especificado.
    - Parâmetro:
      - `m`: o mapa ordenado a ser sincronizado.

58. `static <T> SortedSet<T> synchronizedSortedSet(SortedSet<T> s)`
    - Retorna um conjunto ordenado sincronizado (thread-safe) com base no conjunto ordenado especificado.
    - Parâmetro:
      - `s`: o conjunto ordenado a ser sincronizado.

59. `static <T> Collection<T> unmodifiableCollection(Collection<? extends T> c)`
    - Retorna uma visualização imutável da coleção especificada.
    - Parâmetro:
      - `c`: a coleção a ser visualizada como imutável.

60. `static <T> List<T> unmodifiableList(List<? extends T> list)`
    - Retorna uma visualização imutável da lista especificada.
    - Parâmetro:
      - `list`: a lista a ser visualizada como imutável.

61. `static <K,V> Map<K,V> unmodifiableMap(Map<? extends K,? extends V> m)`
    - Retorna uma visualização imutável do mapa especificado.
    - Parâmetro:
      - `m`: o mapa a ser visualizado como imutável.

62. `static <K,V> NavigableMap<K,V> unmodifiableNavigableMap(NavigableMap<K,? extends V> m)`
    - Retorna uma visualização imutável do mapa navegável especificado.
    - Parâmetro:
      - `m`: o mapa navegável a ser visualizado como imutável.

63. `static <T> NavigableSet<T> unmodifiableNavigableSet(NavigableSet<T> s)`
    - Retorna uma visualização imutável do conjunto navegável especificado.
    - Parâmetro:
      - `s`: o conjunto navegável a ser visualizado como imutável.

64. `static <T> Set<T> unmodifiableSet(Set<? extends T> s)`
    - Retorna uma visualização imutável do conjunto especificado.
    - Parâmetro:
      - `s`: o conjunto a ser visualizado como imutável.

65. `static <K,V> SortedMap<K,V> unmodifiableSortedMap(SortedMap<K,? extends V> m)`
    - Retorna uma visualização imutável do mapa ordenado especificado.
    - Parâmetro:
      - `m`: o mapa ordenado a ser visualizado como imutável.

66. `static <T> SortedSet<T> unmodifiableSortedSet(SortedSet<T> s)`
    - Retorna uma visualização imutável do conjunto ordenado especificado.
    - Parâmetro:
      - `s`: o conjunto ordenado a ser visualizado como imutável.

## Dicionários em Java

1. Criar um objeto HashMap:
Você pode criar um objeto `HashMap` especificando os tipos de dados para a chave (`Key`) e o valor (`Value`) que o dicionário irá conter.

```java
import java.util.HashMap;
HashMap<KeyType, ValueType> hashMap = new HashMap<>();
```

2. Adicionar elementos ao dicionário:
Para adicionar um par chave-valor ao dicionário, use o método `put()`.

```java
hashMap.put(key1, value1);
```

3. Acessar elementos do dicionário:
Para obter o valor associado a uma chave específica, use o método `get()`.

```java
ValueType value = hashMap.get(key);
```

4. Verificar se uma chave existe no dicionário:
Use o método `containsKey()` para verificar se uma chave específica está presente no dicionário.

```java
if (hashMap.containsKey(key)) {
    // A chave existe no dicionário.
} else {
    // A chave não existe no dicionário.
}
```

5. Remover elementos do dicionário:
Para remover um par chave-valor com base na chave, use o método `remove()`.

```java
hashMap.remove(key);
```

7. Iterar sobre os elementos do dicionário:
Você pode usar um loop `for-each` para iterar sobre os pares chave-valor do dicionário.

```java
for (KeyType key : hashMap.keySet()) {
    ValueType value = hashMap.get(key);
    // Faça algo com a chave e o valor.
}
```

## Pilha em Java

```java
import java.util.Stack;
public class PilhaExemplo {
    public static void main(String[] args) {
        // Criar uma instância da classe Stack para representar a pilha
        Stack<Integer> pilha = new Stack<>();
        // Inserir elementos na pilha (push)
        pilha.push(10);
        pilha.push(20);
        pilha.push(30);
        // Obter o elemento do topo da pilha (peek)
        int topo = pilha.peek();
        System.out.println("Elemento do topo da pilha: " + topo);
        // Remover o elemento do topo da pilha (pop)
        int elementoRemovido = pilha.pop();
        System.out.println("Elemento removido: " + elementoRemovido);
        // Verificar se a pilha está vazia
        boolean vazia = pilha.isEmpty();
        System.out.println("A pilha está vazia? " + vazia);
        // Obter o tamanho da pilha
        int tamanho = pilha.size();
        System.out.println("Tamanho da pilha: " + tamanho);
    }
}
```

## Fila em Java

```java
import java.util.LinkedList;
import java.util.Queue;
public class FilaExemplo {
    public static void main(String[] args) {
        // Criar uma instância da classe LinkedList para representar a fila
        Queue<Integer> fila = new LinkedList<>();
        // Inserir elementos na fila (enqueue)
        fila.offer(10);
        fila.offer(20);
        fila.offer(30);
        // Obter o elemento da frente da fila (peek)
        int frente = fila.peek();
        System.out.println("Elemento da frente da fila: " + frente);
        // Remover o elemento da frente da fila (dequeue)
        int elementoRemovido = fila.poll();
        System.out.println("Elemento removido: " + elementoRemovido);
        // Verificar se a fila está vazia
        boolean vazia = fila.isEmpty();
        System.out.println("A fila está vazia? " + vazia);
        // Obter o tamanho da fila
        int tamanho = fila.size();
        System.out.println("Tamanho da fila: " + tamanho);
    }
}
```
