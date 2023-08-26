# UnitTest

- [UnitTest](#unittest)
  - [Como se faz Unit Test em JavaScript](#como-se-faz-unit-test-em-javascript)
    - [Como se monta uma Suite de diversos Unit Test em JavaScript](#como-se-monta-uma-suite-de-diversos-unit-test-em-javascript)
  - [Como se faz Unit Test em Java](#como-se-faz-unit-test-em-java)
    - [Como se monta uma Suite de diversos Unit Test em Java](#como-se-monta-uma-suite-de-diversos-unit-test-em-java)
  - [Como se faz Unit Test em Python](#como-se-faz-unit-test-em-python)
    - [Como se monta uma Suite de diversos Unit Test em Python](#como-se-monta-uma-suite-de-diversos-unit-test-em-python)


## Como se faz Unit Test em JavaScript

Realizar testes de unidade em JavaScript é uma prática importante para garantir que as partes individuais do seu código (funções, módulos) funcionem corretamente. Existem várias bibliotecas e estruturas para escrever testes de unidade em JavaScript, sendo o **Jest** uma das opções mais populares. Aqui está um guia básico sobre como criar testes de unidade em JavaScript usando o Jest:

1. **Configurar o ambiente:**
   Certifique-se de ter o Node.js instalado no seu sistema. Você pode criar um projeto Node.js ou usar um ambiente já existente.

2. **Instalar o Jest:**
   No diretório do seu projeto, execute o seguinte comando para instalar o Jest como dependência de desenvolvimento:

   ```
   npm install --save-dev jest
   ```

3. **Escrever funções/módulos para testar:**
   Crie as funções ou módulos que você deseja testar. Por exemplo:

```javascript
// math.js
function somar(a, b) {
    return a + b;
}

module.exports = {
    somar
};
```

4. **Escrever testes:**
   Crie um arquivo separado para seus testes. Nomeie-o com o sufixo `.test.js` ou `.spec.js` para que o Jest reconheça automaticamente como arquivos de teste.

```javascript
// math.test.js
const { somar } = require('./math');

test('soma 1 + 2 para ser igual a 3', () => {
    expect(somar(1, 2)).toBe(3);
});

test('soma -1 + 1 para ser igual a 0', () => {
    expect(somar(-1, 1)).toBe(0);
});

test('soma -1 + -1 para ser igual a -2', () => {
    expect(somar(-1, -1)).toBe(-2);
});
```

5. **Executar os testes:**
   Você pode executar os testes através do comando `npx jest` no terminal. Jest irá procurar automaticamente por arquivos de teste com os sufixos mencionados e executar os testes.

6. **Analisar os resultados:**
   Após a execução, você verá uma saída que indica quantos testes passaram, falharam ou foram ignorados.

O exemplo acima é bastante simples, mas o Jest oferece muitos recursos avançados, como testes assíncronos, mocks, spies, e mais. Lembre-se de que a criação de testes de unidade eficazes pode ajudar a manter seu código confiável e fácil de manter.

### Como se monta uma Suite de diversos Unit Test em JavaScript

Uma suite de testes é um conjunto de testes de unidade que são agrupados para serem executados juntos. No contexto do Jest, uma das bibliotecas de testes mais populares para JavaScript, você pode criar uma suite de testes definindo vários arquivos de teste e usando a funcionalidade de agrupamento fornecida pelo próprio Jest. Aqui está como montar uma suite de vários testes de unidade usando o Jest:

1. **Estrutura de diretórios:**
   Primeiro, organize seus arquivos de teste em uma estrutura de diretórios adequada. Por exemplo:

   ```
   project-root/
   ├── src/
   │   ├── math.js
   ├── tests/
   │   ├── math.test.js
   │   ├── other.test.js
   ├── package.json
   ```

2. **Instalar o Jest:**
   Certifique-se de ter o Jest instalado como uma dependência de desenvolvimento no seu projeto, como mencionado anteriormente.

3. **Escrever testes individuais:**
   Crie arquivos de teste individuais para cada parte do código que você deseja testar. Nomeie esses arquivos com o sufixo `.test.js` ou `.spec.js`. Por exemplo, `math.test.js`:

```javascript
// math.test.js
const { somar } = require('../src/math');

test('soma 1 + 2 para ser igual a 3', () => {
    expect(somar(1, 2)).toBe(3);
});
```

4. **Agrupar testes em suites:**
   Você pode agrupar os testes em "suites" usando a função `describe` fornecida pelo Jest. Isso ajuda a organizar os testes relacionados.

```javascript
// other.test.js
describe('Outros testes', () => {
    test('algum outro teste', () => {
        // código do teste
    });

    test('mais um teste', () => {
        // código do teste
    });
});
```

5. **Executar os testes:**
   Para executar todos os testes, simplesmente execute o seguinte comando no terminal:

   ```
   npx jest
   ```

   Jest automaticamente localizará todos os arquivos de teste no diretório e subdiretórios, executando-os e exibindo os resultados no terminal.

A organização dos testes em suites usando `describe` é opcional, mas pode tornar a estrutura do teste mais clara, especialmente quando você tem muitos testes.

Lembre-se de ajustar os caminhos dos módulos (`require` ou `import`) conforme necessário para corresponder à estrutura do seu projeto.

## Como se faz Unit Test em Java

Realizar testes de unidade em Java é uma prática importante para garantir que as partes individuais do seu código (métodos, classes) funcionem corretamente. O framework de testes de unidade mais comum em Java é o JUnit. Aqui está um guia básico sobre como criar testes de unidade em Java usando o JUnit:

1. **Configurar o ambiente:**
   Certifique-se de que você tenha o ambiente Java configurado corretamente e o JUnit instalado ou configurado como dependência no seu projeto.

2. **Criar as classes que serão testadas:**
   Crie as classes e métodos que você deseja testar.

```java
public class Calculadora {
    public int somar(int a, int b) {
        return a + b;
    }
}
```

3. **Criar classes de teste:**
   Crie uma classe de teste que utilize o framework JUnit. Crie métodos de teste públicos dentro dessa classe e utilize as anotações fornecidas pelo JUnit para definir os casos de teste.

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestCalculadora {
    
    @Test
    public void testSomar() {
        Calculadora calculadora = new Calculadora();
        assertEquals(8, calculadora.somar(3, 5));
        assertEquals(0, calculadora.somar(-1, 1));
        assertEquals(-2, calculadora.somar(-1, -1));
    }
}
```

4. **Executar os testes:**
   Geralmente, você executa os testes através de ferramentas de construção como Maven ou Gradle, que possuem integração com o JUnit. Você também pode executar os testes diretamente na IDE (como Eclipse ou IntelliJ) se elas tiverem suporte ao JUnit.

5. **Analisar os resultados:**
   Após a execução, você verá uma saída que indica quantos testes passaram, falharam ou foram ignorados.

O exemplo acima é bastante simples, mas você pode criar testes mais complexos, incluindo testes parametrizados, testes de exceções, configurações de teste e muito mais. Lembre-se de que a criação de testes de unidade eficazes pode ajudar a manter seu código confiável e fácil de manter.

### Como se monta uma Suite de diversos Unit Test em Java

Em Java, você pode criar uma suite de testes usando o framework de testes JUnit. Uma suite de testes é uma maneira de agrupar vários casos de teste em uma única unidade de execução. Você pode criar e executar uma suite de testes que inclui múltiplos casos de teste. Aqui está como montar uma suite de diversos testes de unidade em Java usando o JUnit:

1. **Configurar o ambiente:**
   Certifique-se de ter o ambiente Java configurado corretamente e o JUnit instalado ou configurado como dependência no seu projeto.

2. **Criar testes individuais:**
   Crie classes de teste individuais para cada parte do código que você deseja testar. Essas classes devem ter métodos de teste (métodos que começam com "test") e usar as anotações do JUnit para definir os casos de teste.

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestCalculadora {
    
    @Test
    public void testSomar() {
        Calculadora calculadora = new Calculadora();
        assertEquals(8, calculadora.somar(3, 5));
    }
}
```

3. **Criar a suite de testes:**
   Crie uma classe que representa a suite de testes. Você pode usar a anotação `@RunWith` e a classe `Suite` do JUnit para agrupar os testes.

```java
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
    TestCalculadora.class,
    OutroTeste.class
})
public class TestSuite {
    // Esta classe não precisa de nenhum conteúdo, serve apenas para agrupar os testes.
}
```

4. **Executar a suite de testes:**
   Você pode executar a suite de testes como faria com qualquer outro caso de teste JUnit, executando a classe `TestSuite` através de sua IDE ou ferramenta de build (como Maven ou Gradle).

5. **Analisar os resultados:**
   Após a execução, você verá uma saída que indica quantos testes passaram, falharam ou foram ignorados.

Lembre-se de que você deve criar uma classe de teste individual para cada classe que você deseja testar e adicionar essas classes à suite de testes. A criação de suites de testes é útil quando você deseja executar um conjunto específico de testes em vez de executar todos os testes no projeto. Isso pode ser especialmente útil em projetos maiores.

## Como se faz Unit Test em Python

Realizar testes de unidade (Unit Tests) em Python é uma prática importante para garantir que as partes individuais do seu código (funções, métodos, classes) funcionem corretamente. O módulo padrão `unittest` é amplamente utilizado para escrever e executar testes de unidade em Python. Aqui está um guia básico sobre como criar testes de unidade em Python usando o módulo `unittest`:

1. **Importar o módulo unittest:**
   Comece importando o módulo `unittest`.

```python
import unittest
```

2. **Definir as funções/métodos que serão testados:**
   Crie as funções ou métodos que você deseja testar.

```python
def somar(a, b):
    return a + b
```

3. **Criar classes de teste:**
   Crie uma classe que herde de `unittest.TestCase`. Cada método dentro dessa classe de teste deve começar com "test_" para que o `unittest` reconheça-o como um caso de teste.

```python
class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(somar(3, 5), 8)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(-1, -1), -2)
```

4. **Executar os testes:**
   Geralmente, você executa os testes diretamente a partir do arquivo Python ou através da linha de comando.

   **Opção 1: Executar a partir do arquivo Python:**

   ```python
   if __name__ == '__main__':
       unittest.main()
   ```

   Execute o arquivo Python e os testes serão executados, exibindo os resultados no console.

   **Opção 2: Executar através da linha de comando:**

   No terminal, navegue até o diretório onde seu arquivo Python de testes está localizado e execute o seguinte comando:

   ```
   python -m unittest nome_do_arquivo_de_teste.py
   ```

   Substitua `nome_do_arquivo_de_teste.py` pelo nome do seu arquivo de teste.

5. **Analisar os resultados:**
   Após a execução, você verá uma saída que indica quantos testes passaram, falharam ou foram ignorados.

Os exemplos acima são bastante simples, mas você pode criar testes mais complexos, incluindo a manipulação de exceções, configurações de teste e muito mais. Lembre-se de que a criação de testes de unidade eficazes pode ajudar a manter seu código confiável e fácil de manter.

### Como se monta uma Suite de diversos Unit Test em Python

Em Python, você pode criar uma suite de testes combinando vários casos de teste usando o módulo `unittest`. Uma suite de testes é útil quando você deseja executar um conjunto específico de casos de teste em vez de todos os casos de teste em um único arquivo. Aqui está como montar uma suite de diversos testes de unidade em Python usando o módulo `unittest`:

1. **Importar o módulo unittest:**
   Comece importando o módulo `unittest`.

```python
import unittest
```

2. **Criar testes individuais:**
   Crie classes de teste individuais para cada parte do código que você deseja testar. Cada classe deve herdar de `unittest.TestCase` e conter métodos de teste (métodos que começam com "test") que usam as assertivas fornecidas pelo `unittest`.

```python
import unittest

class TestCalculadora(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(somar(3, 5), 8)
```

3. **Criar a suite de testes:**
   Crie uma classe que representa a suite de testes. Nessa classe, você pode usar `unittest.TestLoader()` para carregar os casos de teste.

```python
import unittest

class TestSuite(unittest.TestSuite):
    
    def suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(TestCalculadora('test_soma'))
        test_suite.addTest(OutroTeste('test_alguma_coisa'))
        return test_suite
```

4. **Executar a suite de testes:**
   Você pode executar a suite de testes da mesma forma que executaria um único caso de teste, mas chamando o método `unittest.TextTestRunner().run()` na sua instância de suite.

```python
import unittest

if __name__ == '__main__':
    suite = TestSuite()
    unittest.TextTestRunner().run(suite.suite())
```

5. **Analisar os resultados:**
   Após a execução, você verá uma saída que indica quantos testes passaram, falharam ou foram ignorados.

Certifique-se de que as classes de teste individuais (como `TestCalculadora`) estejam definidas e importadas corretamente. Cada uma delas deve ter seus próprios métodos de teste, que serão incluídos na suite de testes por meio do método `addTest`.

Lembre-se de que a criação de suites de testes é útil quando você deseja agrupar e executar um conjunto específico de testes em vez de todos os testes no projeto. Isso pode ser especialmente útil em projetos maiores.