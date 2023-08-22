# DateTime

- [DateTime](#datetime)
  - [Manipulação de Datas em JavaScript](#manipulação-de-datas-em-javascript)
    - [Como calcular a diferença entre datas em JavaScript](#como-calcular-a-diferença-entre-datas-em-javascript)
    - [Formatação de Datas em JavaScript](#formatação-de-datas-em-javascript)
  - [Manipulação de Datas em Java](#manipulação-de-datas-em-java)
    - [Como calcular a diferença de datas em Java](#como-calcular-a-diferença-de-datas-em-java)
    - [Classe Instant em Java](#classe-instant-em-java)
    - [Formatação de Datas em Java](#formatação-de-datas-em-java)
    - [Padrões de Formatação de Datas em Java](#padrões-de-formatação-de-datas-em-java)
  - [Manipulação de Datas em Python](#manipulação-de-datas-em-python)
    - [Como calcular a diferença de datas em Python](#como-calcular-a-diferença-de-datas-em-python)
    - [Formatação de Datas com Python](#formatação-de-datas-com-python)
    - [Padrões de Formatação de Datas em Python](#padrões-de-formatação-de-datas-em-python)

## Manipulação de Datas em JavaScript

1. Criar uma data:

```javascript
// Criar uma data representando a data e hora atuais
const dataAtual = new Date();
// Criar uma data específica (ano, mês, dia, hora, minuto, segundo, milissegundo)
const dataEspecifica = new Date(2023, 7, 6, 12, 30, 0, 0); // 6 de agosto de 2023, 12:30:00
```

2. Obter informações da data:

```javascript
const data = new Date();
const ano = data.getFullYear();
const mes = data.getMonth(); // Janeiro é 0, fevereiro é 1, e assim por diante
const dia = data.getDate();
const hora = data.getHours();
const minuto = data.getMinutes();
const segundo = data.getSeconds();
const milissegundo = data.getMilliseconds();
const diaDaSemana = data.getDay(); // Domingo é 0, segunda-feira é 1, e assim por diante
```

3. Manipular datas:

```javascript
const data = new Date();
// Adicionar 5 dias à data atual
data.setDate(data.getDate() + 5);
// Adicionar 2 horas à hora atual
data.setHours(data.getHours() + 2);
// Definir uma data específica
data.setFullYear(2024);
data.setMonth(3); // Abril (0 a 11)
data.setDate(15);
data.setHours(18);
data.setMinutes(45);
data.setSeconds(30);
data.setMilliseconds(0);
```

4. Formatar datas:
```javascript
const data = new Date();
const formatoPadrao = data.toString(); // Exemplo: "Sat Aug 06 2023 15:30:00 GMT+0300 (Eastern European Summer Time)"
// Formatando data no formato "dd/mm/yyyy"
const diaFormatado = data.getDate().toString().padStart(2, '0');
const mesFormatado = (data.getMonth() + 1).toString().padStart(2, '0'); // Adiciona 1 ao mês, pois janeiro é 0
const anoFormatado = data.getFullYear();
const dataFormatada = `${diaFormatado}/${mesFormatado}/${anoFormatado}`;
```

### Como calcular a diferença entre datas em JavaScript

```javascript
// Função para calcular a diferença em dias entre duas datas
function calcularDiferencaEmDias(data1, data2) {
  // Converter as datas para objetos do tipo Date
  const dataInicial = new Date(data1);
  const dataFinal = new Date(data2);
  // Calcular a diferença em milissegundos
  const diferencaEmMilissegundos = Math.abs(dataFinal - dataInicial);
  // Calcular a diferença em dias
  const umDiaEmMilissegundos = 1000 * 60 * 60 * 24;
  const diferencaEmDias = Math.floor(diferencaEmMilissegundos / umDiaEmMilissegundos);
  return diferencaEmDias;
}
// Exemplo de uso da função
const dataInicial = '2023-01-01';
const dataFinal = '2023-08-06';
const diferencaEmDias = calcularDiferencaEmDias(dataInicial, dataFinal);
console.log(`A diferença em dias entre as datas é: ${diferencaEmDias}`);
```

### Formatação de Datas em JavaScript

1. Usando o objeto `Date` nativo:

```javascript
// Criar uma data
const data = new Date();
// Formato padrão: "Sat Aug 06 2023 00:00:00 GMT+0000 (Coordinated Universal Time)"
console.log(data.toString());
// Formato ISO 8601: "2023-08-06T00:00:00.000Z"
console.log(data.toISOString());
// Formato personalizado
const dia = data.getDate().toString().padStart(2, '0');
const mes = (data.getMonth() + 1).toString().padStart(2, '0');
const ano = data.getFullYear();
const hora = data.getHours().toString().padStart(2, '0');
const minuto = data.getMinutes().toString().padStart(2, '0');
const segundo = data.getSeconds().toString().padStart(2, '0');
const formatoPersonalizado = `${dia}/${mes}/${ano} ${hora}:${minuto}:${segundo}`;
console.log(formatoPersonalizado); // "06/08/2023 00:00:00"
```

2. Usando a biblioteca `moment.js` (é necessário instalar a biblioteca primeiro):

```javascript
// Importar a biblioteca moment.js
const moment = require('moment');
// Criar uma data usando o moment.js
const dataMoment = moment();
// Formato padrão: "2023-08-06T00:00:00.000Z"
console.log(dataMoment.toISOString());
// Formato personalizado
const formatoPersonalizadoMoment = dataMoment.format('DD/MM/YYYY HH:mm:ss');
console.log(formatoPersonalizadoMoment); // "06/08/2023 00:00:00"
```

## Manipulação de Datas em Java

1. Criar uma data:

```java
import java.time.LocalDate;
import java.time.LocalDateTime;
// Criar a data atual
LocalDate dataAtual = LocalDate.now();
// Criar uma data específica
LocalDate dataEspecifica = LocalDate.of(2023, 8, 6); // 6 de agosto de 2023
// Criar uma data e hora específica
LocalDateTime dataHoraEspecifica = LocalDateTime.of(2023, 8, 6, 12, 30); // 6 de agosto de 2023, 12:30
```

2. Obter informações da data:
   
```java
import java.time.LocalDate;
import java.time.LocalDateTime;
LocalDate data = LocalDate.now();
int ano = data.getYear();
int mes = data.getMonthValue(); // Janeiro é 1, fevereiro é 2, e assim por diante
int dia = data.getDayOfMonth();
LocalDateTime dataHora = LocalDateTime.now();
int hora = dataHora.getHour();
int minuto = dataHora.getMinute();
int segundo = dataHora.getSecond();
```

3. Manipular datas:
   
```java
import java.time.LocalDate;
LocalDate data = LocalDate.now();
// Adicionar 5 dias à data atual
data = data.plusDays(5);
// Adicionar 2 meses à data atual
data = data.plusMonths(2);
// Definir uma data específica
data = LocalDate.of(2024, 4, 15);
```

4. Formatar datas:

```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
LocalDate data = LocalDate.now();
// Formatando data no formato "dd/MM/yyyy"
DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");
String dataFormatada = data.format(formato);
```

### Como calcular a diferença de datas em Java

```java
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
public class CalculadoraDiferencaDatas {
    public static void main(String[] args) {
        // Exemplo de datas
        String dataInicialStr = "2023-01-01";
        String dataFinalStr = "2023-08-06";
        // Converter as strings para objetos LocalDate
        LocalDate dataInicial = LocalDate.parse(dataInicialStr);
        LocalDate dataFinal = LocalDate.parse(dataFinalStr);
        // Calcular a diferença em dias
        long diferencaEmDias = ChronoUnit.DAYS.between(dataInicial, dataFinal);
        System.out.println("A diferença em dias entre as datas é: " + diferencaEmDias);
    }
}
```

### Classe Instant em Java

A classe `Instant` faz parte do pacote `java.time` introduzido no Java 8 para lidar com manipulação de datas e horas. A classe `Instant` representa um ponto específico no tempo, sendo uma das formas mais simples e úteis de representar um instante na linha do tempo.

Principais características da classe `Instant`:

1. Representação de tempo absoluto: O `Instant` representa um momento específico no tempo, sem considerar qualquer data ou fuso horário. É uma representação de tempo absoluto desde o Epoch Unix (1º de janeiro de 1970 às 00:00:00 UTC).

2. Precisão: A classe `Instant` armazena o tempo com precisão de nanossegundos.

3. Imutabilidade: Assim como outras classes de data e hora do pacote `java.time`, `Instant` é imutável, ou seja, uma vez criado, não é possível alterar o valor de um objeto `Instant`.

4. Convergência de máquinas: O `Instant` é independente de fuso horário e não é afetado por alterações de fuso horário ou por outras configurações do sistema. Isso o torna especialmente útil para registros de data e hora em sistemas distribuídos.

Exemplo de uso da classe `Instant`:

```java
import java.time.Instant;

public class ExemploInstant {
    public static void main(String[] args) {
        // Criar um Instant representando o momento atual
        Instant instantAtual = Instant.now();
        System.out.println("Instant atual: " + instantAtual);

        // Criar um Instant a partir de um timestamp em segundos e nanossegundos
        Instant instantCustomizado = Instant.ofEpochSecond(1679876543, 987654321);
        System.out.println("Instant customizado: " + instantCustomizado);

        // Obter o número de segundos desde o Epoch Unix
        long segundosDesdeEpoch = instantCustomizado.getEpochSecond();
        System.out.println("Segundos desde o Epoch Unix: " + segundosDesdeEpoch);

        // Obter os nanossegundos dentro do segundo
        int nanossegundos = instantCustomizado.getNano();
        System.out.println("Nanossegundos: " + nanossegundos);
    }
}
```

Neste exemplo, criamos objetos `Instant` representando o momento atual com `Instant.now()` e um instante personalizado usando `Instant.ofEpochSecond()`. Podemos obter o número de segundos desde o Epoch Unix e os nanossegundos dentro do segundo usando os métodos `getEpochSecond()` e `getNano()`, respectivamente.

A classe `Instant` é muito útil para registrar timestamps em aplicativos, cálculos de duração entre dois instantes, e para comunicação de datas e horas em ambientes distribuídos.

### Formatação de Datas em Java

1. Utilizando `SimpleDateFormat` (antes do Java 8):

```java
import java.text.SimpleDateFormat;
import java.util.Date;
public class ExemploFormatacaoData {
    public static void main(String[] args) {
        Date data = new Date();
        // Formato padrão: "yyyy-MM-dd HH:mm:ss"
        SimpleDateFormat sdfPadrao = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String dataFormatadaPadrao = sdfPadrao.format(data);
        System.out.println(dataFormatadaPadrao); // "2023-08-06 12:34:56"
        // Outros formatos
        SimpleDateFormat sdfOutroFormato = new SimpleDateFormat("dd/MM/yyyy");
        String dataFormatadaOutroFormato = sdfOutroFormato.format(data);
        System.out.println(dataFormatadaOutroFormato); // "06/08/2023"
        SimpleDateFormat sdfHora = new SimpleDateFormat("HH:mm:ss");
        String horaFormatada = sdfHora.format(data);
        System.out.println(horaFormatada); // "12:34:56"
    }
}
```

2. Utilizando `DateTimeFormatter` (a partir do Java 8):

```java
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
public class ExemploFormatacaoData {
    public static void main(String[] args) {
        LocalDateTime dataHora = LocalDateTime.now();
        // Formato padrão: "yyyy-MM-dd HH:mm:ss"
        DateTimeFormatter dtfPadrao = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String dataHoraFormatadaPadrao = dataHora.format(dtfPadrao);
        System.out.println(dataHoraFormatadaPadrao); // "2023-08-06 12:34:56"
        // Outros formatos
        DateTimeFormatter dtfOutroFormato = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String dataFormatadaOutroFormato = dataHora.format(dtfOutroFormato);
        System.out.println(dataFormatadaOutroFormato); // "06/08/2023"
        DateTimeFormatter dtfHora = DateTimeFormatter.ofPattern("HH:mm:ss");
        String horaFormatada = dataHora.format(dtfHora);
        System.out.println(horaFormatada); // "12:34:56"
    }
}
```

### Padrões de Formatação de Datas em Java

Padrões para `SimpleDateFormat` (antes do Java 8):
- `'yyyy'`: Ano com 4 dígitos.
- `'yy'`: Ano com 2 dígitos.
- `'MM'`: Mês com 2 dígitos (ex: "08" para agosto).
- `'MMM'`: Abreviação do nome do mês (ex: "Aug" para agosto).
- `'MMMM'`: Nome completo do mês (ex: "August" para agosto).
- `'dd'`: Dia do mês com 2 dígitos (ex: "06" para o sexto dia).
- `'HH'`: Hora do dia (formato de 24 horas) com 2 dígitos.
- `'hh'`: Hora do dia (formato de 12 horas) com 2 dígitos.
- `'mm'`: Minutos com 2 dígitos.
- `'ss'`: Segundos com 2 dígitos.
- `'SSS'`: Milissegundos com 3 dígitos.
- `'a'`: AM/PM (usado em conjunto com `'hh'` para formatar a hora no formato de 12 horas).
- `'EEE'`: Abreviação do dia da semana (ex: "Sat" para sábado).
- `'EEEE'`: Nome completo do dia da semana (ex: "Saturday" para sábado).
- `'Z'`: Offset do fuso horário em relação ao UTC (ex: "+0800" para fuso horário de 8 horas à frente do UTC).

Padrões para `DateTimeFormatter` (a partir do Java 8):
Os padrões para `DateTimeFormatter` são muito semelhantes aos padrões do `SimpleDateFormat`, mas com algumas diferenças:
- `'y'`: Ano com o número mínimo de dígitos necessários.
- `'M'`: Mês sem zeros à esquerda (ex: "8" para agosto).
- `'d'`: Dia do mês sem zeros à esquerda (ex: "6" para o sexto dia).
- `'H'`: Hora do dia (formato de 24 horas) sem zeros à esquerda.
- `'h'`: Hora do dia (formato de 12 horas) sem zeros à esquerda.
- `'m'`: Minutos sem zeros à esquerda.
- `'s'`: Segundos sem zeros à esquerda.
- `'S'`: Frações de segundos sem zeros à esquerda.
- `'a'`: AM/PM (usado em conjunto com `'h'` para formatar a hora no formato de 12 horas).
- `'E'`: Nome curto do dia da semana (ex: "Sat" para sábado).
- `'EEEE'`: Nome completo do dia da semana (ex: "Saturday" para sábado).
- `'Z'`: Offset do fuso horário em relação ao UTC (ex: "+0800" para fuso horário de 8 horas à frente do UTC).

## Manipulação de Datas em Python

1. Importar o módulo `datetime`:

```python
import datetime
```

2. Obter a data e hora atual:

```python
data_hora_atual = datetime.datetime.now()
print(data_hora_atual)  # Exemplo de saída: 2023-08-06 12:30:00.123456
```

3. Obter informações da data e hora atual:

```python
ano_atual = data_hora_atual.year
mes_atual = data_hora_atual.month
dia_atual = data_hora_atual.day
hora_atual = data_hora_atual.hour
minuto_atual = data_hora_atual.minute
segundo_atual = data_hora_atual.second
microsegundo_atual = data_hora_atual.microsecond
```

4. Criar uma data específica:

```python
data_especifica = datetime.datetime(2023, 8, 6, 12, 30, 0)
print(data_especifica)  # Exemplo de saída: 2023-08-06 12:30:00
```

5. Manipular datas:

```python
# Adicionar 5 dias à data atual
nova_data = data_hora_atual + datetime.timedelta(days=5)
# Adicionar 2 horas à hora atual
novo_horario = data_hora_atual + datetime.timedelta(hours=2)
# Definir uma data específica
outra_data = datetime.datetime(2024, 4, 15)
```

6. Formatar datas:

```python
data_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)  # Exemplo de saída: "06/08/2023 12:30:00"
```

### Como calcular a diferença de datas em Python

Em Python, você pode calcular a diferença entre duas datas utilizando a biblioteca padrão `datetime`. Para isso, você pode criar objetos `datetime` para cada data e, em seguida, calcular a diferença entre eles. Vamos ver um exemplo de como fazer isso:

```python
from datetime import datetime

# Função para calcular a diferença em dias entre duas datas
def calcular_diferenca_em_dias(data_inicial, data_final):
    # Converter as strings para objetos datetime
    data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
    data_final = datetime.strptime(data_final, '%Y-%m-%d')

    # Calcular a diferença em dias
    diferenca = data_final - data_inicial

    # Acessar o atributo 'days' da diferença para obter o número de dias
    diferenca_em_dias = diferenca.days

    return diferenca_em_dias

# Exemplo de uso da função
data_inicial_str = '2023-01-01'
data_final_str = '2023-08-06'

diferenca_em_dias = calcular_diferenca_em_dias(data_inicial_str, data_final_str)
print(f"A diferença em dias entre as datas é: {diferenca_em_dias}")
```

Neste exemplo, utilizamos a função `datetime.strptime()` para converter as strings de datas em objetos `datetime`, fornecendo o formato `'%Y-%m-%d'`, que corresponde a "ano-mês-dia". Em seguida, calculamos a diferença entre as duas datas subtraindo `data_inicial` de `data_final`. O resultado será um objeto `timedelta`, que representa a diferença entre duas datas. Para obter o número de dias, acessamos o atributo `days` do objeto `timedelta`.

Essa é uma maneira simples e eficaz de calcular a diferença entre duas datas em dias usando Python e a biblioteca `datetime`. Se você precisar calcular a diferença com mais precisão, também pode trabalhar com outras unidades de tempo, como horas, minutos ou segundos, a partir do objeto `timedelta`.

### Formatação de Datas com Python

Em Python, a formatação de datas é realizada principalmente usando a classe `datetime` do módulo `datetime`. A classe `datetime` permite que você trabalhe com datas, horários e intervalos de tempo. Para formatar datas em Python, você precisa seguir os seguintes passos:

1. Importar o módulo `datetime`.
2. Criar um objeto `datetime` com a data que você deseja formatar.
3. Utilizar o método `strftime()` (string format time) para aplicar a formatação desejada.

Aqui está um exemplo de como você pode formatar uma data em Python:

```python
from datetime import datetime

# Exemplo de data para formatar
data_para_formatar = datetime(2023, 8, 6)

# Formatação da data para o formato 'dd/mm/aaaa'
data_formatada = data_para_formatar.strftime('%d/%m/%Y')
print(data_formatada)  # Saída: '06/08/2023'

# Formatação da data para o formato 'dia da semana, dd de mês por extenso de aaaa'
data_formatada_extenso = data_para_formatar.strftime('%A, %d de %B de %Y')
print(data_formatada_extenso)  # Saída: 'Sunday, 06 de August de 2023'
```

Aqui estão alguns dos formatos de formatação de data mais comuns:

- `%Y`: Ano com quatro dígitos (ex: 2023).
- `%y`: Ano com dois dígitos (ex: 23).
- `%m`: Mês com dois dígitos (ex: 08).
- `%B`: Nome completo do mês (ex: August).
- `%b`: Nome abreviado do mês (ex: Aug).
- `%d`: Dia do mês com dois dígitos (ex: 06).
- `%A`: Nome completo do dia da semana (ex: Sunday).
- `%a`: Nome abreviado do dia da semana (ex: Sun).

Você pode combinar esses formatos como desejar para obter a formatação desejada. Lembre-se de que a classe `datetime` oferece muitas outras funcionalidades para manipulação de datas e horários, como cálculos de diferenças entre datas, manipulação de fusos horários e muito mais.

### Padrões de Formatação de Datas em Python

Em Python, a formatação de datas é realizada utilizando diretivas de formatação, que são representadas por caracteres especiais precedidos do símbolo de porcentagem (%). Essas diretivas são usadas no método `strftime()` da classe `datetime` para definir o padrão de formatação que você deseja aplicar à data.

Aqui estão algumas das diretivas mais comuns utilizadas para formatar datas em Python:

- `%Y`: Ano com quatro dígitos (ex: 2023).
- `%y`: Ano com dois dígitos (ex: 23).
- `%m`: Mês com dois dígitos (ex: 08).
- `%B`: Nome completo do mês (ex: August).
- `%b`: Nome abreviado do mês (ex: Aug).
- `%d`: Dia do mês com dois dígitos (ex: 06).
- `%A`: Nome completo do dia da semana (ex: Sunday).
- `%a`: Nome abreviado do dia da semana (ex: Sun).
- `%H`: Hora (00 a 23).
- `%I`: Hora (01 a 12).
- `%M`: Minuto (00 a 59).
- `%S`: Segundo (00 a 59).
- `%p`: AM ou PM.
- `%f`: Microssegundos (até seis dígitos).
- `%j`: Dia do ano (001 a 366).
- `%U`: Semana do ano, onde domingo é o primeiro dia da semana (00 a 53).
- `%W`: Semana do ano, onde segunda-feira é o primeiro dia da semana (00 a 53).
- `%w`: Dia da semana como um número decimal (0 a 6, onde 0 é domingo).
- `%z`: Deslocamento do fuso horário UTC (+HHMM ou -HHMM).
- `%Z`: Nome do fuso horário (ex: UTC, EST, PST).

Você pode combinar várias diretivas para criar o formato desejado. Por exemplo:

```python
from datetime import datetime

data_para_formatar = datetime(2023, 8, 6, 15, 30, 45)

# Formatação da data para o formato 'dd/mm/aaaa HH:MM:SS'
data_formatada = data_para_formatar.strftime('%d/%m/%Y %H:%M:%S')
print(data_formatada)  # Saída: '06/08/2023 15:30:45'

# Formatação da data para o formato 'AAAA-MM-DD'
data_formatada_2 = data_para_formatar.strftime('%Y-%m-%d')
print(data_formatada_2)  # Saída: '2023-08-06'
```

Esses são apenas alguns exemplos das possibilidades de formatação de datas em Python. As diretivas de formatação podem ser usadas de várias maneiras para atender às suas necessidades específicas. Lembre-se de consultar a documentação oficial do Python para obter mais informações sobre formatação de datas com `strftime()`.