# DataBase

- [DataBase](#database)
  - [Resumo](#resumo)
    - [Resumo em Java](#resumo-em-java)
      - [Resumo SQLite em Java](#resumo-sqlite-em-java)
      - [Resumo MySQL em Java](#resumo-mysql-em-java)
      - [Resumo PostgreSQL em Java](#resumo-postgresql-em-java)
      - [Resumo SQL Server em Java](#resumo-sql-server-em-java)
      - [Resumo Oracle em Java](#resumo-oracle-em-java)
    - [Resumo em Python](#resumo-em-python)
      - [Resumo SQLite em Python](#resumo-sqlite-em-python)
      - [Resumo MySQL em Python](#resumo-mysql-em-python)
      - [Resumo PostgreSQL em Python](#resumo-postgresql-em-python)
      - [Resumo SQL Server em Python](#resumo-sql-server-em-python)
      - [Resumo Oracle em Python](#resumo-oracle-em-python)
  - [JDBC em Java](#jdbc-em-java)
    - [SQLite em Java](#sqlite-em-java)
    - [MySQL em Java](#mysql-em-java)
    - [PostgreSQL em Java](#postgresql-em-java)
    - [SQL Server em Java](#sql-server-em-java)
    - [Oracle em Java](#oracle-em-java)
    - [Operações de SQL com o JDBC](#operações-de-sql-com-o-jdbc)
    - [Operações de SQL com o JDBC usando o PrepareStatement](#operações-de-sql-com-o-jdbc-usando-o-preparestatement)
  - [Banco de Dados em Python](#banco-de-dados-em-python)
    - [SQLite em Python](#sqlite-em-python)
    - [MySQL em Python](#mysql-em-python)
    - [PostgreSQL em Python](#postgresql-em-python)
    - [SQL Server em Python](#sql-server-em-python)
    - [Oracle em Python](#oracle-em-python)
  - [Banco de Dados em JavaScript](#banco-de-dados-em-javascript)
    - [SQLite em JavaScript](#sqlite-em-javascript)
    - [MySQL em JavaScript](#mysql-em-javascript)
    - [PostgreSQL em JavaScript](#postgresql-em-javascript)
    - [SQL Server em JavaScript](#sql-server-em-javascript)
    - [Oracle em JavaScript](#oracle-em-javascript)

## Resumo

### Resumo em Java

#### Resumo SQLite em Java

```java
Class.forName("org.sqlite.JDBC");
connection = DriverManager.getConnection("jdbc:sqlite:/caminho/para/seu/banco.db");
```

#### Resumo MySQL em Java

```java
Class.forName("com.mysql.cj.jdbc.Driver");
connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/seu_banco_de_dados", user, pass);
```

#### Resumo PostgreSQL em Java

```java
Class.forName("org.postgresql.Driver");
connection = DriverManager.getConnection("jdbc:postgresql://localhost:5432/seu_banco_de_dados", user, pass);
```

#### Resumo SQL Server em Java

```java
Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
connection = DriverManager.getConnection("jdbc:sqlserver://localhost:1433;databaseName=seu_banco_de_dados", user, pass);
```

#### Resumo Oracle em Java

```java
Class.forName("oracle.jdbc.driver.OracleDriver");
connection = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:seu_sid", user, pass);
```

### Resumo em Python

#### Resumo SQLite em Python

```python
import sqlite3
conn = sqlite3.connect('/caminho/para/seu/banco.db')
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (?, ?)", (valor1, valor2))
```

#### Resumo MySQL em Python

`pip install mysql-connector-python`

```python
import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s)", (valor1, valor2))
```

#### Resumo PostgreSQL em Python

`pip install psycopg2`

```python
import psycopg2
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s)", (valor1, valor2))
```

#### Resumo SQL Server em Python

`pip install pyodbc`

```python
import pyodbc
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=seu_banco_de_dados;UID=seu_usuario;PWD=sua_senha'
)
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (?, ?)", (valor1, valor2))
```

#### Resumo Oracle em Python

`pip install cx_Oracle`

```python
import cx_Oracle
conn = cx_Oracle.connect('seu_usuario/sua_senha@localhost:1521/seu_sid')
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (:val1, :val2)", val1=valor1, val2=valor2)
```

## JDBC em Java

### SQLite em Java

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class SQLiteConnection {
    public static void main(String[] args) {
        Connection connection = null;
        try {
            // Carregar o driver JDBC do SQLite
            Class.forName("org.sqlite.JDBC");
            // Estabelecer a conexão com o banco de dados SQLite
            connection = DriverManager.getConnection("jdbc:sqlite:/caminho/para/seu/banco.db");
            System.out.println("Conexão com o banco de dados SQLite estabelecida.");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### MySQL em Java

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class MySQLConnection {
    public static void main(String[] args) {
        Connection connection = null;
        try {
            // Carregar o driver JDBC do MySQL
            Class.forName("com.mysql.cj.jdbc.Driver");
            // Estabelecer a conexão com o banco de dados MySQL
            String url = "jdbc:mysql://localhost:3306/seu_banco_de_dados";
            String user = "seu_usuario";
            String password = "sua_senha";
            connection = DriverManager.getConnection(url, user, password);
            System.out.println("Conexão com o banco de dados MySQL estabelecida.");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### PostgreSQL em Java

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class PostgreSQLConnection {
    public static void main(String[] args) {
        Connection connection = null;
        try {
            // Carregar o driver JDBC do PostgreSQL
            Class.forName("org.postgresql.Driver");
            // Estabelecer a conexão com o banco de dados PostgreSQL
            String url = "jdbc:postgresql://localhost:5432/seu_banco_de_dados";
            String user = "seu_usuario";
            String password = "sua_senha";
            connection = DriverManager.getConnection(url, user, password);
            System.out.println("Conexão com o banco de dados PostgreSQL estabelecida.");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### SQL Server em Java

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class SQLServerConnection {
    public static void main(String[] args) {
        Connection connection = null;
        try {
            // Carregar o driver JDBC do SQL Server
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            // Estabelecer a conexão com o banco de dados SQL Server
            String url = "jdbc:sqlserver://localhost:1433;databaseName=seu_banco_de_dados";
            String user = "seu_usuario";
            String password = "sua_senha";
            connection = DriverManager.getConnection(url, user, password);
            System.out.println("Conexão com o banco de dados SQL Server estabelecida.");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### Oracle em Java

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class OracleConnection {
    public static void main(String[] args) {
        Connection connection = null;
        try {
            // Carregar o driver JDBC do Oracle
            Class.forName("oracle.jdbc.driver.OracleDriver");
            // Estabelecer a conexão com o banco de dados Oracle
            String url = "jdbc:oracle:thin:@localhost:1521:seu_sid";
            String user = "seu_usuario";
            String password = "sua_senha";
            connection = DriverManager.getConnection(url, user, password);
            System.out.println("Conexão com o banco de dados Oracle estabelecida.");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### Operações de SQL com o JDBC

1. Conectar ao banco de dados:
Antes de executar qualquer operação, você precisa estabelecer uma conexão com o banco de dados usando a classe `java.sql.Connection`. Isso é feito carregando o driver JDBC específico para o banco de dados e criando a conexão usando a URL de conexão.

2. Executar consultas de leitura (SELECT):
Para recuperar dados do banco de dados, você pode usar a classe `java.sql.Statement` para criar uma consulta SQL e, em seguida, executá-la usando o método `executeQuery()`. O resultado é retornado como um objeto `java.sql.ResultSet`, que você pode iterar para obter os dados.

3. Executar operações de atualização (INSERT, UPDATE, DELETE):
Para inserir, atualizar ou excluir dados no banco de dados, você também usa a classe `java.sql.Statement`, mas desta vez você chama os métodos `executeUpdate()` ou `execute()` passando a consulta SQL adequada.

4. Utilizar transações:
O JDBC suporta transações, que são blocos de operações que são executados em conjunto como uma única unidade de trabalho. Você pode iniciar uma transação usando o método `setAutoCommit(false)` na conexão e, em seguida, executar várias operações. Se todas as operações forem bem-sucedidas, você pode confirmar a transação usando `commit()`. Caso contrário, você pode reverter as alterações usando `rollback()`.

5. Tratar exceções:
Sempre é importante tratar exceções ao trabalhar com bancos de dados para lidar com erros de conexão, problemas de consulta ou violações de integridade de dados. Use blocos `try-catch` para capturar e lidar com exceções de forma adequada.

6. Fechar recursos:
Após executar as operações, lembre-se de fechar os recursos, como objetos `ResultSet`, `Statement` e `Connection`, para liberar recursos e evitar vazamentos de recursos.

Aqui está um exemplo geral que mostra como realizar uma operação de leitura com JDBC:

```java
import java.sql.*;
public class ReadDataExample {
    public static void main(String[] args) {
        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;
        try {
            // Carregar o driver JDBC do banco de dados (por exemplo, SQLite)
            Class.forName("org.sqlite.JDBC");
            // Estabelecer a conexão com o banco de dados
            connection = DriverManager.getConnection("jdbc:sqlite:/path/to/your/database.db");
            // Criar um objeto Statement
            statement = connection.createStatement();
            // Executar a consulta SQL de leitura
            String selectQuery = "SELECT * FROM users";
            resultSet = statement.executeQuery(selectQuery);
            // Iterar sobre os resultados
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                int age = resultSet.getInt("age");
                System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age);
            }
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                // Fechar os recursos
                if (resultSet != null) {
                    resultSet.close();
                }
                if (statement != null) {
                    statement.close();
                }
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### Operações de SQL com o JDBC usando o PrepareStatement

O JDBC (Java Database Connectivity) é uma API do Java que permite que os programas Java interajam com bancos de dados por meio de consultas SQL. O uso do `PreparedStatement` em JDBC é uma prática recomendada para executar consultas parametrizadas, o que aumenta a segurança e a eficiência das operações de banco de dados. Aqui está um exemplo de como realizar operações de SQL usando o `PreparedStatement`:

1. **Importar as classes necessárias:**
Certifique-se de importar as classes relevantes do pacote `java.sql`.

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
```

2. **Conectar ao banco de dados:**
Antes de executar qualquer consulta, você precisa criar uma conexão com o banco de dados.

```java
String url = "jdbc:mysql://localhost:3306/seu_banco_de_dados";
String username = "seu_usuario";
String password = "sua_senha";

try {
    Connection connection = DriverManager.getConnection(url, username, password);
} catch (SQLException e) {
    e.printStackTrace();
}
```

3. **Preparar e executar consultas parametrizadas:**
Aqui estão alguns exemplos de como usar `PreparedStatement` para operações de SQL:

**Inserção de Dados:**

```java
String insertQuery = "INSERT INTO tabela (coluna1, coluna2) VALUES (?, ?)";

try {
    PreparedStatement preparedStatement = connection.prepareStatement(insertQuery);
    preparedStatement.setString(1, valorColuna1);
    preparedStatement.setString(2, valorColuna2);
    preparedStatement.executeUpdate();
} catch (SQLException e) {
    e.printStackTrace();
}
```

**Atualização de Dados:**

```java
String updateQuery = "UPDATE tabela SET coluna1 = ? WHERE coluna2 = ?";

try {
    PreparedStatement preparedStatement = connection.prepareStatement(updateQuery);
    preparedStatement.setString(1, novoValorColuna1);
    preparedStatement.setString(2, valorColuna2);
    preparedStatement.executeUpdate();
} catch (SQLException e) {
    e.printStackTrace();
}
```

**Seleção de Dados:**

```java
String selectQuery = "SELECT coluna1, coluna2 FROM tabela WHERE coluna3 = ?";

try {
    PreparedStatement preparedStatement = connection.prepareStatement(selectQuery);
    preparedStatement.setString(1, valorColuna3);
    ResultSet resultSet = preparedStatement.executeQuery();

    while (resultSet.next()) {
        String coluna1 = resultSet.getString("coluna1");
        String coluna2 = resultSet.getString("coluna2");
        // Fazer algo com os resultados
    }
} catch (SQLException e) {
    e.printStackTrace();
}
```

4. **Fechar recursos:**
Sempre feche a conexão, os `PreparedStatement` e os `ResultSet` após o uso.

```java
if (resultSet != null) {
    resultSet.close();
}

if (preparedStatement != null) {
    preparedStatement.close();
}

if (connection != null) {
    connection.close();
}
```

Usar `PreparedStatement` é uma prática recomendada para evitar ataques de injeção de SQL e melhorar o desempenho, já que a consulta preparada pode ser reutilizada com diferentes parâmetros. Certifique-se de tratar exceções de forma adequada para lidar com problemas de conexão ou de consulta.

## Banco de Dados em Python

### SQLite em Python

```python
import sqlite3
# Conectar ao banco de dados SQLite
conn = sqlite3.connect('/caminho/para/seu/banco.db')
# Criar um cursor para executar consultas
cursor = conn.cursor()
# Exemplo: Executar uma consulta de leitura
cursor.execute("SELECT * FROM sua_tabela")
rows = cursor.fetchall()
# Exemplo: Executar uma operação de atualização
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (?, ?)", (valor1, valor2))
conn.commit()
# Fechar a conexão
conn.close()
```

### MySQL em Python

```bash
pip install mysql-connector-python
```

```python
import mysql.connector
# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
# Criar um cursor para executar consultas
cursor = conn.cursor()
# Exemplo: Executar uma consulta de leitura
cursor.execute("SELECT * FROM sua_tabela")
rows = cursor.fetchall()
# Exemplo: Executar uma operação de atualização
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s)", (valor1, valor2))
conn.commit()
# Fechar a conexão
conn.close()
```

### PostgreSQL em Python

```bash
pip install psycopg2
```

```python
import psycopg2
# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
# Criar um cursor para executar consultas
cursor = conn.cursor()
# Exemplo: Executar uma consulta de leitura
cursor.execute("SELECT * FROM sua_tabela")
rows = cursor.fetchall()
# Exemplo: Executar uma operação de atualização
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s)", (valor1, valor2))
conn.commit()
# Fechar a conexão
conn.close()
```

### SQL Server em Python

```bash
pip install pyodbc
```

```python
import pyodbc
# Conectar ao banco de dados SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=seu_banco_de_dados;UID=seu_usuario;PWD=sua_senha'
)
# Criar um cursor para executar consultas
cursor = conn.cursor()
# Exemplo: Executar uma consulta de leitura
cursor.execute("SELECT * FROM sua_tabela")
rows = cursor.fetchall()
# Exemplo: Executar uma operação de atualização
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (?, ?)", (valor1, valor2))
conn.commit()
# Fechar a conexão
conn.close()
```

### Oracle em Python

```bash
pip install cx_Oracle
```

```python
import cx_Oracle
# Conectar ao banco de dados Oracle
conn = cx_Oracle.connect('seu_usuario/sua_senha@localhost:1521/seu_sid')
# Criar um cursor para executar consultas
cursor = conn.cursor()
# Exemplo: Executar uma consulta de leitura
cursor.execute("SELECT * FROM sua_tabela")
rows = cursor.fetchall()
# Exemplo: Executar uma operação de atualização
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (:val1, :val2)", val1=valor1, val2=valor2)
conn.commit()
# Fechar a conexão
conn.close()
```

## Banco de Dados em JavaScript

### SQLite em JavaScript

```bash
npm install sqlite3
```

```javascript
const sqlite3 = require('sqlite3').verbose();
// Conectar ao banco de dados SQLite
const db = new sqlite3.Database('/caminho/para/seu/banco.db');
// Exemplo: Executar uma consulta de leitura
db.all('SELECT * FROM sua_tabela', [], (err, rows) => {
  if (err) {
    throw err;
  }
  console.log(rows);
});
// Exemplo: Executar uma operação de atualização
const valor1 = 'Valor 1';
const valor2 = 42;
db.run('INSERT INTO sua_tabela (coluna1, coluna2) VALUES (?, ?)', [valor1, valor2], (err) => {
  if (err) {
    throw err;
  }
  console.log('Dados inseridos com sucesso!');
});
// Fechar a conexão
db.close();
```

### MySQL em JavaScript

```bash
npm install mysql
```

```javascript
const mysql = require('mysql');
// Configurar as informações de conexão
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'seu_usuario',
  password: 'sua_senha',
  database: 'seu_banco_de_dados'
});
// Conectar ao banco de dados MySQL
connection.connect((err) => {
  if (err) {
    throw err;
  }
  console.log('Conexão com o banco de dados MySQL estabelecida.');
  // Exemplo: Executar uma consulta de leitura
  connection.query('SELECT * FROM sua_tabela', (err, rows) => {
    if (err) {
      throw err;
    }
    console.log(rows);
  });
  // Exemplo: Executar uma operação de atualização
  const valor1 = 'Valor 1';
  const valor2 = 42;
  connection.query('INSERT INTO sua_tabela (coluna1, coluna2) VALUES (?, ?)', [valor1, valor2], (err, result) => {
    if (err) {
      throw err;
    }
    console.log('Dados inseridos com sucesso!');
  });
  // Fechar a conexão
  connection.end();
});
```

### PostgreSQL em JavaScript

```bash
npm install pg
```

```javascript
const { Pool, Client } = require('pg');
// Configurar as informações de conexão
const pool = new Pool({
  user: 'seu_usuario',
  host: 'localhost',
  database: 'seu_banco_de_dados',
  password: 'sua_senha',
  port: 5432,
});
// Conectar ao banco de dados PostgreSQL
pool.query('SELECT NOW()', (err, res) => {
  if (err) {
    throw err;
  }
  console.log('Conexão com o banco de dados PostgreSQL estabelecida.');
  // Exemplo: Executar uma consulta de leitura
  pool.query('SELECT * FROM sua_tabela', (err, res) => {
    if (err) {
      throw err;
    }
    console.log(res.rows);
  });
  // Exemplo: Executar uma operação de atualização
  const valor1 = 'Valor 1';
  const valor2 = 42;
  pool.query('INSERT INTO sua_tabela (coluna1, coluna2) VALUES ($1, $2)', [valor1, valor2], (err, res) => {
    if (err) {
      throw err;
    }
    console.log('Dados inseridos com sucesso!');
  });
  // Fechar a conexão
  pool.end();
});
```

### SQL Server em JavaScript

```bash
npm install mssql
```

```javascript
const sql = require('mssql');
// Configurar as informações de conexão
const config = {
  user: 'seu_usuario',
  password: 'sua_senha',
  server: 'localhost',
  database: 'seu_banco_de_dados',
  options: {
    enableArithAbort: true,
  }
};
// Conectar ao banco de dados SQL Server
sql.connect(config).then(pool => {
  console.log('Conexão com o banco de dados SQL Server estabelecida.');
  // Exemplo: Executar uma consulta de leitura
  pool.request().query('SELECT * FROM sua_tabela', (err, result) => {
    if (err) {
      throw err;
    }
    console.log(result.recordset);
  });
  // Exemplo: Executar uma operação de atualização
  const valor1 = 'Valor 1';
  const valor2 = 42;
  pool.request().query('INSERT INTO sua_tabela (coluna1, coluna2) VALUES (@valor1, @valor2)', (err, result) => {
    if (err) {
      throw err;
    }
    console.log('Dados inseridos com sucesso!');
  });
  // Fechar a conexão
  sql.close();
}).catch(err => {
  console.log(err);
});
```

### Oracle em JavaScript

```bash
npm install oracledb
```

```javascript
const oracledb = require('oracledb');
// Configurar as informações de conexão
const config = {
  user: 'seu_usuario',
  password: 'sua_senha',
  connectString: 'localhost/seu_sid'
};
// Conectar ao banco de dados Oracle
oracledb.getConnection(config, (err, connection) => {
  if (err) {
    throw err;
  }
  console.log('Conexão com o banco de dados Oracle estabelecida.');
  // Exemplo: Executar uma consulta de leitura
  connection.execute('SELECT * FROM sua_tabela', (err, result) => {
    if (err) {
      throw err;
    }
    console.log(result.rows);
  });
  // Exemplo: Executar uma operação de atualização
  const valor1 = 'Valor 1';
  const valor2 = 42;
  connection.execute('INSERT INTO sua_tabela (coluna1, coluna2) VALUES (:val1, :val2)', [valor1, valor2], (err, result) => {
    if (err) {
      throw err;
    }
    console.log('Dados inseridos com sucesso!');
  });
  // Fechar a conexão
  connection.close();
});
```
